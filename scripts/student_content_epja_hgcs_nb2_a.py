"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 1 (parte 1): OAD-01, obtener información de fuentes sobre el pasado y el presente. Todas las fuentes y los datos son inventados («de ejemplo») y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Todas las fuentes (boletas, fotografías descritas, relatos, tablas) están escritas en cada ejercicio y son inventadas «de ejemplo»: "
             "no necesitas internet, mapas ni fotos reales. Cuando la clase habla de una foto o un objeto, usa la descripción escrita. "
             "Tu experiencia de vida es un buen punto de partida, pero nadie te pide contar datos personales: puedes trabajar con los casos del cuaderno. Si algo cuesta leer, pide apoyo.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-01"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Tres cosas encontradas en una caja de una sede vecinal. "
      "A) Una boleta de compra del almacén «Don Lucho», fechada el 12 de marzo de 2019: pan 2 kg, $2.400. "
      "B) Una fotografía sin fecha de una feria con un letrero que dice «Feria Santa Rosa». "
      "C) El relato grabado de doña Elena: «Cuando llegó la luz eléctrica a mi pasaje, mi mamá guardó las velas en un cajón.»")
build(
    O, 1, F1,
    use="Hoy reconozco que a mi alrededor hay fuentes que cuentan cosas del pasado y del presente, y aprendo a sacarles información.",
    prior=["Sé leer una boleta, una fecha y un letrero.", "Escucho relatos de personas mayores y de mi barrio.", "Distingo «antes» de «ahora»."],
    explain=[
        "Una fuente es cualquier cosa que nos entrega información sobre el pasado o el presente: una boleta, una carta, una fotografía, un objeto antiguo o el relato de una persona. Tú ya usas fuentes todos los días: lees un horario, miras una cuenta o escuchas una historia familiar.",
        "En Historia, Geografía y Ciencias Sociales las usamos para responder preguntas. Hay fuentes escritas (una boleta), orales (un relato), visuales (una fotografía) y materiales (una olla antigua o una herramienta). Cada una muestra solo una parte de lo que ocurrió.",
        "Obtener información es leer la fuente con una pregunta en mente y anotar los datos que contiene: qué dice, quién la hizo, cuándo y dónde. Distinguimos lo que la fuente dice con claridad de lo que nosotros suponemos.",
    ],
    vocab=[("fuente", "algo que entrega información sobre el pasado o el presente"), ("fuente escrita", "documento con texto: boleta, carta, diario"), ("fuente oral", "relato de una persona, dicho o grabado"), ("fuente material", "objeto de otra época: herramienta, olla, ropa"), ("información", "datos que se obtienen de una fuente")],
    worked=[
        ("Sacar datos de la boleta", "{F} Obtén información de la fuente A.", ["Leo qué dice: pan 2 kg a $2.400.", "Leo cuándo es: 12 de marzo de 2019.", "Anoto el lugar: almacén «Don Lucho»."], "Una compra de pan por $2.400 el 12 de marzo de 2019 en el almacén «Don Lucho»"),
        ("Qué dice y qué supongo", "Un vecino mira la fuente B y dice: «Esa feria era de 2019».", ["La foto no trae fecha: no dice cuándo se sacó.", "Solo se puede afirmar que existía una feria llamada «Feria Santa Rosa»."], "No se puede afirmar el año: la foto no lo dice"),
    ],
    mistakes=[("Decir que una fuente cuenta «todo» lo que pasó.", "Cada fuente muestra solo una parte: la boleta no cuenta cómo vivía la gente.", "Pregunta qué sí dice la fuente y qué no dice."),
              ("Dar por cierto un dato que la fuente no trae, como el año de una foto sin fecha.", "Se mezcla lo que dice la fuente con lo que se supone.", "Anota solo lo que está escrito o visible y marca lo demás como suposición.")],
    T=[
        ("abc", "{F} ¿Cuál de las tres es una fuente oral?", "El relato de doña Elena", "La boleta del almacén", "La fotografía de la feria", "Un relato dicho o grabado por una persona es una fuente oral; la boleta es escrita y la foto es visual."),
        ("ab", "En Historia: ¿qué es una fuente?", "Algo que da información sobre el pasado o el presente", "Solo un libro de texto escolar", "Fuente es cualquier cosa que informa; no solo los libros."),
        ("{F} ¿Qué fecha tiene la boleta de la fuente A?", "12 de marzo de 2019", "La boleta trae escrita esa fecha, así que es un dato directo."),
        ("abc", "{F} ¿Qué información entrega la fuente A sobre el presente o el pasado reciente?", "Que se compró pan por $2.400 en ese almacén en esa fecha", "Que el almacén cerró en 2020", "Que todos compraban pan los martes", "Solo dice la compra, el precio, el lugar y el día; lo demás sería inventar."),
        ("ab", "{F} Sobre la fuente B, ¿qué se puede afirmar con seguridad?", "Que existía una feria llamada «Feria Santa Rosa»", "Que la foto fue sacada en 2019", "El letrero se ve, pero la fotografía no trae año."),
        ("{F} Según doña Elena, ¿qué guardó su mamá en un cajón?", "las velas", "El relato dice que la mamá guardó las velas cuando llegó la luz."),
        ("abc", "Un cuaderno de cuentas de un almacén de ejemplo anota «3 de mayo de 2021: harina 5 kg, $5.500». ¿Qué tipo de fuente es?", "Escrita", "Oral", "Material", "Es un documento con texto, por eso es una fuente escrita."),
        ("=", "{F} Si una compra como la de la fuente A se hizo en 2019, ¿cuántos años pasaron hasta 2024?", "2024-2019", "Se restan los años para saber cuánto tiempo pasó entre ambas fechas.", " años"),
        ("abc", "{F} ¿Qué pregunta puede responder el relato de doña Elena?", "¿Cómo cambió la vida en el pasaje cuando llegó la luz eléctrica?", "¿Cuánto costaba el pan en 2019?", "¿Dónde se sacó la fotografía de la feria?", "El relato habla de la llegada de la luz y del cambio de costumbres."),
        ("abc", "Un vecino dice: «Con la boleta basta para saber cómo vivía toda la gente en 2019». ¿Qué falla en su razonamiento?", "Una sola fuente muestra solo una parte y no la vida de todos", "La boleta no puede leerse", "Las boletas nunca sirven", "Una boleta informa de una compra, no de la vida de un barrio entero."),
        ("ab", "{F} Para conocer lo que sintió doña Elena, ¿qué fuente sirve más?", "Su relato oral", "La boleta del almacén", "Un relato personal cuenta sentimientos y recuerdos; una boleta solo registra una compra."),
        ("abc", "{F} Se quiere saber si la feria de la fuente B existía antes de 2019. La foto no tiene fecha. ¿Qué conviene hacer?", "Buscar otra fuente con fecha, por ejemplo un aviso vecinal de 2015 de ejemplo", "Decidir que sí existía porque se ve vieja", "Decidir que no existía porque no hay fecha", "Se necesita una fuente que traiga fecha para comprobarlo; adivinar no sirve."),
        ("abc", "Una olla de greda de ejemplo, usada hace muchos años, está guardada en un museo local. ¿Qué tipo de fuente es?", "Material", "Escrita", "Oral", "Es un objeto de otra época; los objetos son fuentes materiales."),
    ],
    ctx=("abc", "En la sede vecinal alguien encuentra una carta de ejemplo fechada en 2008 que avisa de una reunión de la junta de vecinos. ¿Qué información se obtiene con claridad?", "Que en 2008 se convocó a una reunión de vecinos", "Que todos los vecinos asistieron", "Que la junta se formó ese año", "La carta solo asegura la convocatoria; la asistencia o el origen de la junta no están escritos."),
    sc=[("En Historia: ¿qué es una fuente oral?", "El relato de una persona, dicho o grabado", "Una fuente oral es un testimonio hablado, no un documento escrito."),
        ("¿Qué debo anotar al obtener información de una fuente?", "Lo que dice con claridad: qué, quién, cuándo y dónde", "Sirve anotar solo datos que la fuente entrega."),
        ("Una foto sin fecha, ¿permite afirmar el año?", "No, porque no lo dice", "Sin fecha escrita solo se pueden afirmar los elementos visibles.")],
    op=("Esta es la ficha de ejemplo: «Fuente 1: aviso de la junta de vecinos del 5 de octubre de 2016: corte de agua el sábado de 9 a 13 horas. Fuente 2: relato de don Pedro: ‘Antes del pozo nuevo íbamos con baldes a la vertiente’». "
        "Escribe, para cada fuente, de qué tipo es y dos datos que entrega. Después anota una cosa que NO puedes saber con esas dos fuentes.",
        "Fuente 1: escrita; dato: corte de agua el sábado de 9 a 13 horas; fecha 5 de octubre de 2016. Fuente 2: oral; dato: antes del pozo nuevo se iba a la vertiente con baldes. No puedo saber en qué año se hizo el pozo.",
        ["clasifica bien cada fuente", "da dos datos de cada una tomados del texto", "señala una limitación real"],
        ["una tabla de dos filas con tipo y datos, más una frase"], ["inventar datos que no están", "decir que las fuentes lo cuentan todo"],
        "Pregunta: «¿Eso lo dice la fuente o lo estoy suponiendo?»."),
    reinforce="Mira dos papeles que tengas a mano (una boleta, un horario) y di qué tipo de fuente son y un dato de cada uno.",
    extend="Explica con un ejemplo por qué dos fuentes sobre el mismo hecho pueden decir cosas distintas.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Cuatro fuentes sobre la plaza de un pueblo ficticio, Villa Alta. "
      "1) Un plano municipal dibujado en 1932 que muestra la plaza con una fuente de agua. "
      "2) Una carta de 1931 de una vecina, escrita pocos días después de un cambio, que cuenta: «Ayer inauguraron la fuente de la plaza». "
      "3) Un artículo de 2010, escrito por un historiador, que resume cómo fue la plaza durante el siglo XX. "
      "4) La fuente de piedra de la plaza, que aún existe.")
build(
    O, 2, F2,
    use="Hoy aprendo palabras para hablar de las fuentes y distingo qué estudian la Historia, la Geografía y las Ciencias Sociales.",
    prior=["Sé que una fuente informa sobre el pasado o el presente.", "Distingo fuente escrita, oral, visual y material.", "Conozco palabras como «plano» y «carta»."],
    explain=[
        "Una fuente primaria es la que viene de la época que se estudia: una carta escrita ese año, un plano de entonces o un objeto de esa época. Una fuente secundaria es un trabajo posterior que explica o resume lo ocurrido, como un artículo escrito por un historiador décadas después.",
        "Las tres disciplinas hacen preguntas distintas. La Historia estudia cómo cambian las sociedades en el tiempo. La Geografía estudia el espacio: dónde ocurren las cosas y cómo se relacionan las personas con el territorio. Las Ciencias Sociales estudian cómo viven y se organizan las personas: economía, política y cultura.",
        "Conocer así es distinto de recordar fechas: es hacer preguntas, buscar fuentes, compararlas y explicar con evidencia. Por eso el conocimiento cambia cuando aparecen fuentes nuevas.",
    ],
    vocab=[("fuente primaria", "viene de la misma época que se estudia"), ("fuente secundaria", "trabajo posterior que explica o resume lo ocurrido"), ("Historia", "estudia cómo cambian las sociedades en el tiempo"), ("Geografía", "estudia el espacio y cómo las personas lo habitan"), ("Ciencias Sociales", "estudian cómo viven y se organizan las personas")],
    worked=[
        ("Primaria o secundaria", "{F} Clasifica la fuente 2 (la carta de 1931).", ["La carta fue escrita pocos días después del hecho.", "Viene de la misma época que se estudia."], "Es una fuente primaria"),
        ("Qué disciplina pregunta qué", "Una persona pregunta: «¿Dónde queda la plaza y qué calles la rodean?». ¿Qué disciplina se ocupa sobre todo?", ["La pregunta es por la ubicación y el espacio.", "El espacio es el campo de la Geografía."], "Geografía"),
    ],
    mistakes=[("Creer que una fuente secundaria es «peor» y no sirve.", "La secundaria explica y ordena muchas fuentes; solo es de otro tipo.", "Úsala para entender el panorama y revisa las primarias para comprobarlo."),
              ("Creer que la Historia es solo memorizar fechas.", "Las fechas ayudan, pero se trata de hacer preguntas y usar fuentes.", "Parte siempre de una pregunta y busca evidencia.")],
    T=[
        ("abc", "{F} ¿Cuál de estas fuentes es secundaria?", "El artículo de 2010", "El plano de 1932", "La carta de 1931", "Fue escrito mucho después por alguien que resume el siglo XX; las otras son de la época."),
        ("ab", "En Historia: ¿qué es una fuente primaria?", "Una que viene de la época que se estudia", "Una que explica el hecho décadas después", "Primaria significa que nace en el tiempo estudiado."),
        ("¿Qué disciplina estudia el espacio y cómo las personas lo habitan?", "Geografía", "Esa es la pregunta propia de la Geografía, que se ocupa del territorio."),
        ("abc", "{F} ¿Cuál es una fuente material?", "La fuente de piedra de la plaza", "El plano de 1932", "El artículo de 2010", "Es un objeto que aún existe; los objetos son fuentes materiales."),
        ("ab", "{F} El plano de 1932 muestra una fuente de agua en la plaza. ¿Qué tipo de fuente es?", "Primaria y visual", "Secundaria y oral", "Es un dibujo de la época, por eso es primaria y visual."),
        ("En Historia: ¿cómo se llama la disciplina que estudia cómo cambian las sociedades en el tiempo?", "Historia", "La Historia se centra en el cambio a lo largo del tiempo."),
        ("abc", "{F} La carta de 1931 dice «Ayer inauguraron la fuente». ¿Qué dato aporta?", "Que la fuente se inauguró un día antes de escribirse la carta", "Que la fuente tiene 100 años", "Que la plaza es la más grande", "La carta indica la inauguración «ayer»; la antigüedad actual no está escrita."),
        ("ab", "Una pregunta como «¿Cómo se organizaban los vecinos para cuidar la plaza?» ¿a qué campo corresponde más?", "Ciencias Sociales", "Geografía física", "Se trata de la organización de las personas, que estudian las Ciencias Sociales."),
        ("abc", "{F} Entre la fuente 2 y la fuente 3, ¿cuál sirve mejor para comprobar la fecha exacta de inauguración?", "La carta de 1931, porque fue escrita en esos días", "El artículo de 2010, porque es más nuevo", "Ninguna sirve", "Lo escrito cerca del hecho es más directo para comprobar un detalle; la nueva es una síntesis."),
        ("abc", "Una estudiante dice: «Si el artículo es de 2010, no puede servir porque no es de la época». ¿Qué respuesta es mejor?", "Sirve para entender el panorama, pero conviene comprobarlo con fuentes de la época", "Tiene razón, hay que descartarlo", "Es mejor que cualquier fuente primaria", "Una secundaria ordena y explica; se contrasta con las primarias."),
        ("ab", "{F} Si apareciera un nuevo plano de 1925 con la fuente ya dibujada, ¿qué pasaría con lo que se cree?", "Podría cambiar la fecha estimada de la fuente", "Nada, el conocimiento nunca cambia", "El conocimiento se corrige cuando surgen fuentes nuevas."),
        ("abc", "{F} Se quiere saber cómo se usó la plaza durante el siglo XX. ¿Qué combinación de fuentes es mejor?", "Varias fuentes de distintos tipos y épocas, comparadas entre sí", "Solo el objeto de piedra", "Solo el nombre de la plaza", "Comparar tipos distintos permite ver el mismo hecho desde varios lados."),
        ("abc", "¿Cuál pregunta es propia de la Geografía?", "¿Dónde está la plaza y qué calles la rodean?", "¿Quién ganó una elección?", "¿Cuántos años tenía la vecina?", "Pregunta por la ubicación y el entorno, es decir, por el espacio."),
    ],
    ctx=("abc", "Un centro cultural quiere armar una muestra sobre una plaza de barrio. Tiene: un acta de 1950 de la junta de vecinos, una canción compuesta en 2005 sobre la plaza y un libro de 2015 que resume su historia. ¿Cuál es la fuente primaria de 1950?", "El acta de 1950", "La canción de 2005", "El libro de 2015", "El acta es de la época que se estudia; las otras son posteriores."),
    sc=[("En fuentes de HGCS: ¿qué distingue una fuente primaria de una secundaria?", "La primaria es de la época; la secundaria la explica después", "Se distinguen por cuándo se hicieron en relación con el hecho."),
        ("En Ciencias Sociales: ¿qué estudian?", "Cómo viven y se organizan las personas en sociedad", "Se ocupan de economía, política y cultura."),
        ("¿Por qué cambia el conocimiento histórico?", "Porque aparecen fuentes nuevas y se hacen nuevas preguntas", "Con evidencia nueva se corrigen las explicaciones.")],
    op=("Ficha de ejemplo: «a) acta de 1948 de un club deportivo; b) fotografía de 1960 de un partido; c) un libro de 2012 sobre el club; d) la copa de metal que ganó el club.» "
        "Escribe para cada una si es primaria o secundaria y de qué tipo (escrita, visual, oral o material). Después elige una pregunta que cada disciplina (Historia, Geografía, Ciencias Sociales) podría hacer sobre el club.",
        "a) primaria, escrita; b) primaria, visual; c) secundaria, escrita; d) primaria, material. Historia: ¿cómo cambió el club desde 1948? Geografía: ¿dónde queda su cancha? Ciencias Sociales: ¿cómo se organizan sus socios?",
        ["clasifica las cuatro fuentes con razón", "formula tres preguntas distintas", "cada pregunta corresponde a su disciplina"],
        ["una tabla con cuatro filas y tres preguntas"], ["llamar secundaria a todo lo viejo", "hacer la misma pregunta para las tres disciplinas"],
        "Pregunta: «¿Esta fuente es de la época o la explica después?»."),
    reinforce="Elige un objeto de tu casa y di si sería una fuente primaria o secundaria para un estudio.",
    extend="Escribe una pregunta de cada disciplina sobre un mismo lugar de tu barrio.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Pregunta: «¿Cómo llegaba el agua a las casas de la población Los Aromos (ficticia) antes de que existiera la red de agua potable?» "
      "Fuentes disponibles: 1) Un relato oral de doña Mirta: «Cuando yo era niña sacábamos agua de un pozo común, cada familia con su balde». "
      "2) Un aviso de 1962 de la junta de vecinos: «Se cobra una cuota para reparar el pozo común». "
      "3) Una receta de pan del libro de cocina de la misma población.")
build(
    O, 3, F3,
    use="Hoy aprendo a seguir pasos para seleccionar fuentes útiles para una pregunta y sacar de ellas información relevante.",
    prior=["Sé qué es una fuente y la clasifico.", "Distingo primaria de secundaria.", "Leo textos breves y tablas."],
    explain=[
        "Seleccionar fuentes es elegir las que sirven para tu pregunta. Una fuente puede ser interesante y no servir: un libro de recetas es una buena fuente, pero no responde cómo llegaba el agua. Primero va la pregunta y después la elección.",
        "Un buen método tiene cuatro pasos. Paso 1: escribe la pregunta con claridad. Paso 2: elige las fuentes que hablan del tema, del lugar y de la época. Paso 3: lee cada una y anota los datos relevantes: qué dice, quién lo dice y cuándo. Paso 4: compara y responde con lo que dicen las fuentes, aclarando lo que no sabes.",
        "Relevante significa que ayuda a responder la pregunta. Trabajar con autonomía es hacer estos pasos por tu cuenta, y con proactividad es buscar otra fuente cuando falta información.",
    ],
    vocab=[("seleccionar", "elegir lo que sirve para un propósito"), ("relevante", "que ayuda a responder la pregunta"), ("pregunta de investigación", "lo que quiero saber, escrito con claridad"), ("dato", "pieza concreta de información"), ("contrastar", "comparar para ver si coinciden")],
    worked=[
        ("Elegir con la pregunta", "{F} ¿Qué fuentes se seleccionan?", ["Paso 1: la pregunta es sobre el agua en las casas antes de la red.", "Paso 2: el relato 1 habla del pozo; el aviso 2 también; la receta no habla de agua."], "Se eligen las fuentes 1 y 2; la receta se descarta"),
        ("Anotar datos relevantes", "Del relato de doña Mirta se obtienen datos.", ["Quién: doña Mirta, que lo recuerda de su niñez.", "Qué: el agua se sacaba de un pozo común con baldes."], "Dato: se usaba un pozo común con baldes"),
    ],
    mistakes=[("Elegir una fuente porque es bonita o larga, aunque no responda la pregunta.", "Se olvida que la selección depende de la pregunta.", "Pregunta antes de leer: ¿esta fuente habla de mi tema, lugar y época?"),
              ("Quedarse con una sola fuente y no contrastar.", "Una sola fuente puede estar incompleta.", "Busca al menos una segunda fuente y compara.")],
    T=[
        ("abc", "{F} ¿Cuál es la pregunta de la ficha?", "Cómo llegaba el agua a las casas antes de la red de agua potable", "Cuánto cuesta el pan", "Dónde queda Los Aromos", "La ficha la escribe al comienzo entre comillas."),
        ("ab", "{F} ¿Qué fuente NO sirve para esa pregunta?", "La receta de pan", "El relato de doña Mirta", "La receta no habla de agua ni de pozos."),
        ("En Historia: ¿cómo se llama un dato o fuente que ayuda a responder la pregunta?", "relevante", "Relevante significa que sirve para lo que se busca."),
        ("abc", "{F} Según el relato 1, ¿de dónde sacaba el agua cada familia?", "De un pozo común", "De una llave en cada casa", "De un camión aljibe", "Doña Mirta cuenta que sacaban agua de un pozo común con baldes."),
        ("ab", "{F} ¿Qué dato aporta el aviso de 1962?", "Que se cobraba una cuota para reparar el pozo", "Que el pozo ya no existía", "El aviso menciona la cuota de reparación del pozo común."),
        ("=", "{F} El aviso es de 1962. Si el relato de doña Mirta se grabó en 2022, ¿cuántos años hay entre ambas fuentes?", "2022-1962", "Se restan las dos fechas para saber cuánto tiempo las separa.", " años"),
        ("abc", "{F} ¿Cuál es el paso 2 del método?", "Elegir las fuentes que hablan del tema, lugar y época", "Responder sin leer", "Copiar la receta", "El paso 2 es seleccionar fuentes que se relacionen con la pregunta."),
        ("ab", "Una persona dice: «Elijo el libro más largo». ¿Qué le falta?", "Revisar si responde su pregunta", "Contar las páginas", "Se elige por relevancia, no por tamaño."),
        ("abc", "{F} Nueva pregunta: «¿Cuánto costaba la cuota para el pozo?». Con estas tres fuentes, ¿qué se puede responder?", "Nada con seguridad: el aviso menciona la cuota pero no el monto", "El monto exacto", "Que era gratis", "El aviso no dice cuánto era; hay que buscar otra fuente."),
        ("abc", "{F} Dos vecinos concluyen cosas distintas: uno dice «todos usaban el pozo» y otro «solo algunas familias». ¿Qué dicen las fuentes?", "Dicen que el pozo era común, pero no cuántas familias lo usaban", "Dicen que lo usaban todas", "Dicen que lo usaban pocas", "Se sabe que era común; la cantidad de familias no está escrita."),
        ("ab", "¿Qué hace una persona proactiva si le falta información?", "Busca otra fuente que ayude", "Deja la pregunta sin responder", "Proactivo es actuar para completar lo que falta."),
        ("abc", "Para comprobar el relato de doña Mirta, ¿qué conviene?", "Compararlo con una fuente escrita de la época", "Repetir el mismo relato", "Cambiar la pregunta", "Contrastar una fuente oral con una escrita aumenta la confianza."),
        ("abc", "{F} Una respuesta bien hecha a la pregunta dice:", "Antes de la red, el agua se sacaba de un pozo común y se pagaba una cuota para repararlo, según un relato y un aviso", "El agua siempre fue gratis", "La población no tenía agua", "Usa los datos de las dos fuentes relevantes y cita lo que dicen."),
    ],
    ctx=("abc", "Una organización comunitaria quiere saber cómo era el transporte del barrio hace treinta años. Tiene tres fuentes de ejemplo: un horario de micros de esa época, una receta de sopaipillas y el relato de una dirigente sobre los paraderos. ¿Qué selección conviene?", "El horario y el relato de la dirigente", "Solo la receta", "Las tres, sin distinguir", "El horario y el relato hablan de transporte; la receta no."),
    sc=[("¿Qué hago primero al buscar información?", "Escribir la pregunta con claridad", "Sin pregunta no se sabe qué fuentes sirven."),
        ("¿Qué significa «relevante»?", "Que ayuda a responder la pregunta", "Una fuente relevante entrega datos útiles para lo que busco."),
        ("¿Para qué se contrastan las fuentes?", "Para ver si coinciden y completar lo que falta", "Contrastar disminuye el riesgo de errores.")],
    op=("Pregunta de ejemplo: «¿Cómo se comunicaban los vecinos del pasaje El Sauce (ficticio) cuando no había teléfono en las casas?». Fuentes de ejemplo: a) carta de 1975 de un vecino: «Avisamos con un silbato cuando llega alguien»; "
        "b) receta de tortillas; c) relato de doña Rosa: «Dejábamos recados en la almacenera». Elige las fuentes relevantes, anota dos datos de cada una y responde en dos frases.",
        "Fuentes a y c. Datos: a) se avisaba con un silbato; c) se dejaban recados en el almacén. Respuesta: se comunicaban con silbato y con recados dejados en el almacén.",
        ["descarta la receta con razón", "anota datos que están en el texto", "responde sin inventar"],
        ["lista de fuentes elegidas, datos y respuesta"], ["elegir las tres fuentes", "agregar datos que no aparecen"],
        "Pregunta: «¿Qué fuente me ayuda de verdad a responder?»."),
    reinforce="Escribe una pregunta sobre tu barrio y di qué dos tipos de fuente podrían ayudar a responderla.",
    extend="Explica qué harías si dos fuentes dan datos distintos sobre lo mismo.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Tres fuentes sobre el mercado de Puerto Claro (ficticio). "
      "Fuente 1 (registro municipal de 1985): «El mercado tenía 40 puestos». "
      "Fuente 2 (diario de 1985, un artículo): «El mercado es el mejor y más hermoso lugar del puerto». "
      "Fuente 3 (relato de un feriante, grabado en 2021): «Cuando empecé, en 1985, éramos como 40 puestos y casi todos vendíamos pescado».")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo separar un hecho de una opinión y cómo obtener datos de varias fuentes sobre un mismo tema.",
    prior=["Selecciono fuentes con ayuda de una pregunta.", "Sé qué es una fuente primaria y una secundaria.", "Anoto datos de una fuente."],
    explain=[
        "Al leer una fuente conviene separar lo que es un hecho de lo que es una opinión. Un hecho se puede comprobar: «el mercado tenía 40 puestos». Una opinión expresa lo que alguien piensa o siente: «es el lugar más hermoso». Las opiniones también son información, pero sobre lo que pensaba esa persona.",
        "Para practicar, trabaja con una tabla de tres columnas: qué dice la fuente, quién lo dice y si es hecho u opinión. Después busca coincidencias entre fuentes: si dos fuentes distintas dicen lo mismo, el dato es más firme.",
        "También ayuda preguntar: ¿quién escribió esto y para qué? Un registro municipal busca anotar; un artículo de diario puede querer opinar o convencer.",
    ],
    vocab=[("hecho", "algo que se puede comprobar"), ("opinión", "lo que alguien piensa o siente"), ("coincidir", "decir lo mismo sobre un dato"), ("registro", "documento que anota datos de forma ordenada"), ("autor", "persona que hizo o dijo la fuente")],
    worked=[
        ("Hecho u opinión", "{F} Clasifica la frase de la fuente 2.", ["«El mejor y más hermoso lugar» expresa lo que alguien piensa.", "No se puede comprobar con un conteo ni un documento."], "Es una opinión"),
        ("Coincidencia", "{F} ¿Coinciden la fuente 1 y la fuente 3 en algún dato?", ["La fuente 1 dice 40 puestos.", "La fuente 3 dice «como 40 puestos» en 1985."], "Sí: ambas dicen unos 40 puestos en 1985; la 3 dice «como», es aproximado"),
    ],
    mistakes=[("Tratar toda opinión como si fuera un hecho.", "Una opinión dice lo que alguien piensa; no es comprobable como un dato.", "Marca «opinión» y usa la frase para saber qué pensaba esa persona."),
              ("Descartar una opinión como inútil.", "La opinión sirve para conocer cómo veía la gente un lugar.", "Úsala con ese propósito, no como prueba de un hecho.")],
    T=[
        ("abc", "{F} ¿Cuál es un hecho?", "El mercado tenía 40 puestos", "Es el lugar más hermoso", "Todos deberían ir", "Se puede comprobar contando los puestos, por eso es un hecho."),
        ("ab", "En Historia: ¿qué es una opinión?", "Lo que alguien piensa o siente", "Un dato comprobable", "La opinión expresa un juicio y no se comprueba como un conteo."),
        ("{F} ¿En qué año se registró el dato de 40 puestos?", "1985", "Tanto el registro como el diario son de 1985."),
        ("abc", "{F} ¿Quién dice la fuente 3?", "Un feriante, en un relato grabado en 2021", "El municipio", "Un diario", "La fuente 3 es el relato del feriante."),
        ("ab", "{F} ¿Qué tipo de fuente es la fuente 1?", "Un registro escrito", "Una fuente material", "Es un documento municipal con datos anotados."),
        ("=", "{F} Si de los 40 puestos del registro de 1985, 36 vendían pescado, ¿cuántos NO vendían pescado?", "40-36", "Se resta lo que vendía pescado del total de puestos.", " puestos"),
        ("abc", "{F} ¿En qué coinciden las fuentes 1 y 3?", "En que había unos 40 puestos en 1985", "En que todo era pescado", "En que el mercado era hermoso", "Ambas hablan de unos 40 puestos en ese año."),
        ("ab", "{F} El feriante dice «casi todos vendíamos pescado». ¿Cómo se clasifica?", "Un hecho aproximado dicho por alguien que estuvo", "Una opinión sobre belleza", "Casi todos vendíamos pescado se refiere a lo que vendían, no a un juicio."),
        ("abc", "{F} ¿Qué conclusión es la mejor con las fuentes?", "En 1985 el mercado tenía unos 40 puestos y casi todos vendían pescado", "El mercado era el mejor del país", "El mercado se cerró en 1985", "Usa los datos que coinciden y deja fuera las opiniones y lo no escrito."),
        ("abc", "Alguien dice: «La fuente 2 es inútil porque es una opinión». ¿Qué respuesta es mejor?", "Sirve para saber cómo veía el mercado quien escribió, aunque no pruebe un hecho", "Tiene razón, se tira", "Sirve para probar los 40 puestos", "Una opinión informa sobre la mirada de una persona."),
        ("ab", "¿Por qué conviene preguntar «¿para qué lo escribió?»?", "Porque el propósito del autor influye en lo que dice", "Porque todos escriben igual", "Un diario puede querer opinar y un registro solo anotar datos."),
        ("abc", "{F} Si otro registro de 1985 dijera 55 puestos, ¿qué conviene hacer?", "Buscar más fuentes y ver cuál dato se repite", "Elegir el que más guste", "Promediar sin pensar", "Con datos distintos se necesita otra fuente para decidir."),
        ("abc", "{F} Una persona escribe: «El mercado de Puerto Claro era el mejor, según el diario de 1985». ¿Qué falla?", "Presenta una opinión del diario como si fuera un hecho comprobado", "Usa un diario", "Menciona el año", "«Mejor» es un juicio; solo es un hecho que el diario lo opinó."),
    ],
    ctx=("abc", "En una radio comunitaria leen una nota de ejemplo: «La feria de Los Cipreses tiene 25 puestos y es la más alegre de la comuna». ¿Qué parte es un hecho y qué parte es una opinión?", "Hecho: tiene 25 puestos; opinión: es la más alegre", "Hecho: es la más alegre; opinión: 25 puestos", "Las dos son hechos", "El número se puede contar; «alegre» es una impresión."),
    sc=[("En el trabajo con fuentes: ¿qué es un hecho?", "Algo que se puede comprobar", "Un hecho se verifica con datos o documentos."),
        ("¿Para qué sirve una opinión en una fuente?", "Para saber qué pensaba quien la escribió", "Muestra su mirada, no un dato comprobable."),
        ("Si dos fuentes distintas dicen lo mismo, ¿qué pasa con el dato?", "Se vuelve más firme", "Si fuentes distintas coinciden, aumenta la confianza en el dato.")],
    op=("Ficha de ejemplo: «Fuente A (acta de 1990): el club tenía 60 socios. Fuente B (carta de un socio, 1990): el club es el más querido del barrio. Fuente C (relato, 2020): ‘éramos unos 60 y nos juntábamos los viernes’». "
        "Haz una tabla con qué dice cada fuente y si es hecho u opinión. Después escribe en una frase qué se sabe con firmeza.",
        "A: 60 socios, hecho. B: más querido, opinión. C: unos 60 y se reunían los viernes, hecho. Con firmeza: unos 60 socios en 1990 y se reunían los viernes.",
        ["clasifica bien cada afirmación", "usa las coincidencias", "no presenta una opinión como hecho"],
        ["una tabla de tres filas y una frase final"], ["tratar «el más querido» como dato", "ignorar la fuente C"],
        "Pregunta: «¿Esto se puede comprobar?»."),
    reinforce="Lee un aviso o un titular y marca con un lápiz un hecho y una opinión.",
    extend="Explica por qué un artículo de opinión puede ser útil para la Historia aunque no pruebe un hecho.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). Se quiere caracterizar «el periodo en que llegó el tren al pueblo ficticio de Villa Alta, entre 1900 y 1930». "
      "Fuente 1 (tabla del municipio): población en 1900: 1.200 personas; en 1930: 3.600 personas. "
      "Fuente 2 (carta de 1912 de un comerciante): «Con el tren, mis mercaderías llegan en un día y no en una semana». "
      "Fuente 3 (relato de una nieta, 2019): «Mi abuelo contaba que antes del tren la gente se iba del pueblo porque no había trabajo». "
      "Fuente 4 (plano de 1925): muestra una estación nueva y tres calles nuevas junto a ella.")
build(
    O, 5, F5,
    use="Hoy uso varias fuentes de ejemplo sobre el pasado y el presente para caracterizar un periodo: describir cómo era y qué cambió.",
    prior=["Selecciono fuentes con una pregunta.", "Distingo hecho de opinión.", "Calculo diferencias simples entre años y cantidades."],
    explain=[
        "Caracterizar un periodo es describir sus rasgos principales: cómo vivía la gente, a qué se dedicaba, qué cambios ocurrían y cuándo. No se trata de contar todo, sino de reunir los datos más importantes en una descripción clara.",
        "Para hacerlo con varias fuentes, ordena la información en una tabla: dato, fuente y qué rasgo muestra (economía, población, transporte, vida diaria). Luego redacta dos o tres frases que describan el periodo con esos datos, y cita de qué fuente salió cada uno.",
        "Recuerda que cada fuente aporta una parte. Si falta algo, dilo: «con estas fuentes no sé cuántas personas trabajaban en el tren». Decir lo que no se sabe también es parte de un buen trabajo.",
    ],
    vocab=[("periodo", "etapa de la historia con rasgos propios"), ("caracterizar", "describir los rasgos principales de algo"), ("rasgo", "característica que distingue algo"), ("cambio", "diferencia entre un antes y un después"), ("evidencia", "dato de una fuente que apoya una afirmación")],
    worked=[
        ("Tabla de rasgos", "{F} Ordena los datos de las fuentes 1 y 2.", ["Fuente 1: la población pasó de 1.200 a 3.600: rasgo, crecimiento de población.", "Fuente 2: la mercadería llega en un día y no en una semana: rasgo, transporte más rápido."], "Rasgos: la población creció y el transporte se hizo más rápido"),
        ("Cálculo de cambio", "{F} ¿Cuántas personas más había en 1930 que en 1900?", ["Resto 3.600 menos 1.200.", "Reviso que el resultado tiene sentido: la población creció."], "2.400 personas más"),
    ],
    mistakes=[("Describir el periodo con una sola fuente.", "Una fuente da una parte; el periodo tiene más aspectos.", "Reúne al menos dos o tres fuentes y señala el rasgo de cada una."),
              ("Escribir rasgos que no tienen evidencia, como «todos vivían mejor».", "Ninguna fuente lo dice.", "Anota solo lo que apoya una fuente y declara lo que no se sabe.")],
    T=[
        ("abc", "{F} ¿Qué periodo se quiere caracterizar?", "La llegada del tren a Villa Alta entre 1900 y 1930", "La vida en 2019", "La fundación del pueblo", "La ficha lo anuncia al comienzo."),
        ("ab", "En Historia: ¿qué es caracterizar un periodo?", "Describir sus rasgos principales", "Contar todos los hechos sin ordenar", "Es resumir cómo era y qué cambió, no listar todo."),
        ("=", "{F} ¿Cuántas personas había en Villa Alta en 1930?", "3600", "La tabla del municipio entrega 3.600 personas en 1930.", " personas"),
        ("abc", "{F} ¿Qué rasgo muestra la fuente 2?", "Que el transporte de mercaderías se hizo más rápido", "Que bajó la población", "Que el tren no servía", "El comerciante cuenta que la mercadería llega en un día y no en una semana."),
        ("ab", "{F} ¿Qué muestra el plano de 1925?", "Una estación nueva y tres calles nuevas", "Un pueblo sin construcciones", "La ficha describe una estación y tres calles nuevas."),
        ("=", "{F} ¿Cuántos años abarca el periodo, desde 1900 hasta 1930?", "1930-1900", "Se restan el año de inicio y el año de término del periodo.", " años"),
        ("abc", "{F} ¿Qué cambio muestra la nieta en su relato?", "Que antes del tren la gente se iba por falta de trabajo", "Que el tren se descompuso", "Que el pueblo era más grande", "Cuenta que, antes del tren, muchas personas se iban del pueblo."),
        ("ab", "{F} Una persona escribe: «Con el tren el pueblo tuvo más gente y más movimiento». ¿Tiene evidencia?", "Sí: la tabla muestra más población y el plano muestra construcciones nuevas", "No, no hay ninguna fuente", "Se apoya en las fuentes 1 y 4."),
        ("abc", "{F} ¿Cuál afirmación NO tiene evidencia en estas fuentes?", "Que todos los habitantes consiguieron trabajo", "Que la población creció", "Que se hicieron calles nuevas", "Ninguna fuente dice que todos tuvieran trabajo; las otras dos sí tienen respaldo."),
        ("abc", "{F} La fuente 3 se grabó en 2019 y cuenta algo que contaba un abuelo. ¿Cómo conviene usarla?", "Como una pista que se compara con fuentes escritas de la época", "Como prueba definitiva", "No usarla nunca", "Es un relato transmitido; sirve, pero conviene contrastarlo."),
        ("ab", "¿Por qué conviene decir lo que «no se sabe» al describir un periodo?", "Porque muestra los límites de las fuentes", "Porque hace más largo el texto", "Declarar vacíos evita inventar y deja claro qué falta investigar."),
        ("abc", "{F} Falta un dato para saber si el tren fue la única causa del crecimiento. ¿Qué haría una persona proactiva?", "Buscar otra fuente sobre fábricas, comercio u otras razones", "Afirmar que fue la única causa", "Olvidar el tema", "Hay que buscar más evidencia antes de hablar de causa única."),
        ("abc", "{F} ¿Qué descripción breve es la mejor?", "Entre 1900 y 1930 Villa Alta creció de 1.200 a 3.600 personas y el tren aceleró el transporte de mercaderías", "Villa Alta siempre fue chica", "Con el tren todos fueron felices", "Usa datos de las fuentes y no agrega nada sin evidencia."),
    ],
    ctx=("abc", "Una junta de vecinos prepara un panel sobre su población entre 1990 y 2010. Tiene fuentes de ejemplo: un listado de 40 familias en 1990, un listado de 95 familias en 2010 y un plano con la nueva sede. ¿Qué rasgo del periodo permite afirmar?", "Que la población creció y se construyó una sede", "Que todos eran jóvenes", "Que nadie se fue", "Solo respaldan crecimiento y construcción; la edad o permanencia no están."),
    sc=[("¿Qué es un rasgo de un periodo?", "Una característica que lo distingue", "Los rasgos describen cómo era una etapa."),
        ("¿Cómo ordeno los datos de varias fuentes?", "En una tabla con dato, fuente y rasgo", "Así se ve qué fuente apoya cada rasgo."),
        ("¿Qué hago si falta información?", "Lo digo y busco otra fuente", "Reconocer el vacío evita inventar y muestra qué falta investigar.")],
    op=("Periodo de ejemplo: «los primeros años del jardín comunitario de la población Las Palmas (ficticia), 2005 a 2015». "
        "Fuentes: a) acta de 2005: 8 familias cultivan; b) acta de 2015: 31 familias cultivan; c) relato de una vecina: ‘Antes comprábamos todo, ahora compartimos lechugas y tomates’. "
        "Haz una tabla con dato, fuente y rasgo y escribe dos frases que caractericen el periodo. Anota una cosa que no sabes.",
        "Rasgos: aumentaron las familias de 8 a 31 (a, b); se comparte lo cosechado (c). No sé cuánta verdura se cosechó.",
        ["usa al menos dos fuentes", "relaciona cada rasgo con su fuente", "declara un vacío"],
        ["una tabla de tres filas y dos frases"], ["inventar cifras", "no citar la fuente"],
        "Pregunta: «¿Qué fuente apoya esa frase?»."),
    reinforce="Escribe tres datos sobre tu barrio de hace diez años y di de qué fuente podrían salir.",
    extend="Compara dos fuentes que den una mirada distinta de un mismo periodo y explica la diferencia.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Pregunta: «¿Cómo cambió el comercio en el pasaje Los Olmos (ficticio) entre 1995 y 2020?». "
      "Fuente A (lista municipal de patentes de 1995): 14 negocios, 9 de ellos almacenes de barrio. "
      "Fuente B (lista municipal de 2020): 22 negocios, 4 de ellos almacenes de barrio. "
      "Fuente C (opinión de una vecina, 2020): «Era mejor cuando había más almacenes». "
      "Fuente D (relato de un comerciante, 2020): «Con las ventas por celular, muchos pasaron a vender desde la casa y ya no atienden en local».")
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: compruebo la información, reconozco los límites del conocimiento histórico y decido qué fuente buscar después.",
    prior=["Selecciono fuentes y separo hechos de opiniones.", "Caracterizo un periodo con tabla y frases.", "Sé restar y comparar cantidades."],
    explain=[
        "El conocimiento de la Historia, la Geografía y las Ciencias Sociales se construye con preguntas, fuentes y explicaciones. No es una verdad cerrada: cuando aparecen fuentes nuevas, se corrige. Por eso se llama interpretación: es una explicación apoyada en evidencia.",
        "Para revisar tu trabajo hazte cuatro preguntas. ¿Respondí la pregunta? ¿Cada afirmación tiene evidencia de una fuente? ¿Separé hechos de opiniones? ¿Dije qué no sé? Si una respuesta es afirmativa, ese paso está logrado.",
        "Una fuente es más confiable si es de la época, si su autor estuvo cerca del hecho y si otras fuentes coinciden. Aun así, ninguna fuente es perfecta: todas se leen con cuidado.",
    ],
    vocab=[("interpretación", "explicación apoyada en evidencia"), ("confiable", "que merece confianza porque se puede comprobar"), ("evidencia", "dato de una fuente que respalda una afirmación"), ("limitación", "lo que una fuente no permite saber"), ("autoevaluar", "revisar el propio trabajo con criterios")],
    worked=[
        ("Revisar una conclusión", "Una persona concluye: «Entre 1995 y 2020 los negocios del pasaje aumentaron de 14 a 22 y los almacenes bajaron de 9 a 4». {F} ¿Está bien apoyada?", ["Comparo con A y B: 14 a 22 y 9 a 4 coinciden.", "No usa la opinión de C como hecho."], "Sí, está apoyada por las fuentes A y B"),
        ("Detectar una limitación", "{F} ¿Se sabe cuántos negocios venden por celular?", ["Reviso las fuentes: D lo menciona, pero no da cifras.", "Anoto la limitación: falta ese dato."], "No se sabe: falta una fuente con esa cifra"),
    ],
    mistakes=[("Creer que una conclusión histórica es definitiva y nunca cambia.", "Con fuentes nuevas puede ajustarse.", "Presenta la conclusión como «según estas fuentes» y deja abierta la posibilidad de revisarla."),
              ("Dar mayor peso a la fuente que coincide con lo que ya pensábamos.", "Se elige por gusto y no por evidencia.", "Evalúa todas las fuentes con los mismos criterios.")],
    T=[
        ("abc", "{F} ¿Cuántos negocios había en 2020 según la fuente B?", "22", "14", "9", "La lista municipal de 2020 entrega 22 negocios."),
        ("ab", "En Historia: ¿qué es una interpretación?", "Una explicación apoyada en evidencia", "Un dato inventado", "Interpretar es explicar con base en las fuentes."),
        ("=", "{F} ¿Cuántos negocios más había en 2020 que en 1995?", "22-14", "Se resta el número de 1995 del de 2020.", " negocios"),
        ("abc", "{F} ¿Cuántos almacenes menos había en 2020 que en 1995?", "5", "13", "4", "En 1995 había 9 almacenes y en 2020, 4; la diferencia es 9 menos 4."),
        ("ab", "{F} ¿Qué tipo de afirmación es la de la fuente C?", "Una opinión", "Un hecho comprobable", "«Era mejor» es un juicio de valor, no un dato."),
        ("{F} ¿Qué fuente menciona las ventas por celular?", "D", "El comerciante cuenta el cambio hacia ventas desde la casa."),
        ("abc", "{F} ¿Qué explicación de las fuentes es la más segura?", "Hubo más negocios en total y menos almacenes de barrio", "Nadie compra en almacenes", "El pasaje se despobló", "Está apoyada en las listas de 1995 y 2020."),
        ("abc", "{F} Una persona dice: «Los almacenes cerraron por las ventas por celular». ¿Qué evidencia falta?", "Una fuente que relacione ambos hechos", "Ninguna, está probado", "La fecha del plano", "Hay dos hechos, pero ninguna fuente prueba la causa."),
        ("ab", "¿Por qué una fuente de la época suele ser más confiable?", "Porque se hizo cerca del hecho", "Porque tiene letra más clara", "Su cercanía en el tiempo reduce el olvido y los cambios."),
        ("abc", "{F} Si apareciera una nueva lista de 2020 con 25 negocios, ¿qué pasaría con la conclusión?", "Habría que revisarla y explicar la diferencia", "Seguiría igual sin pensar", "Se borraría todo", "El dato nuevo exige comparar y ajustar."),
        ("ab", "¿Qué pregunta de autoevaluación revisa el uso de evidencia?", "¿Cada afirmación tiene una fuente que la respalde?", "¿Escribí mucho?", "Una buena respuesta se apoya en fuentes, no en la extensión."),
        ("abc", "{F} Elige la mejor forma de cerrar un informe sobre el pasaje:", "Según las fuentes A, B y D, hubo más negocios y menos almacenes; falta saber cuántos venden por celular", "Todo fue peor", "Todo fue mejor", "Resume los hechos, cita las fuentes y reconoce una limitación."),
        ("abc", "Tras revisar tu trabajo detectas que una afirmación no tiene fuente. ¿Qué haces?", "La quito o busco evidencia que la respalde", "La dejo igual", "La subrayo", "Una afirmación sin evidencia debe corregirse o sostenerse con una fuente."),
    ],
    ctx=("abc", "Un vecino arma un panel sobre su feria y tiene tres frases: «Había 30 puestos en 2000» (acta de ejemplo), «Era la más linda» (comentario) y «En 2020 hay 45 puestos» (acta). ¿Qué frases son hechos con evidencia?", "La primera y la tercera", "La segunda", "Las tres", "Las actas respaldan los números; «linda» es opinión."),
    sc=[("¿Qué cuatro preguntas me hago para revisar mi trabajo?", "Respondí la pregunta, tengo evidencia, separé hechos de opiniones y dije qué no sé", "Revisar así mejora la calidad del informe."),
        ("¿Por qué el conocimiento histórico puede cambiar?", "Porque aparecen fuentes nuevas", "Las explicaciones se ajustan con nueva evidencia."),
        ("¿Qué hago si dos fuentes no coinciden?", "Busco otra fuente y comparo", "Contrastar fuentes ayuda a decidir cuál dato es más firme.")],
    op=("Informe de ejemplo para revisar: «Entre 2000 y 2020 el club de adultos mayores creció de 20 a 55 socios (actas). Fue el mejor club de la comuna (opinión de un vecino). Se cree que las charlas de salud atrajeron socios (no hay fuente)». "
        "Revisa el informe con las cuatro preguntas de autoevaluación y reescribe una versión mejorada de tres frases.",
        "Mejorado: «Entre 2000 y 2020 el club creció de 20 a 55 socios, según las actas. Un vecino opinó que era el mejor, pero eso es una opinión. No hay fuente que pruebe que las charlas de salud atrajeron socios».",
        ["identifica hecho, opinión y afirmación sin fuente", "reescribe sin inventar", "declara una limitación"],
        ["la lista de problemas y el texto reescrito"], ["mantener la opinión como hecho", "agregar una causa sin fuente"],
        "Pregunta: «¿Qué fuente prueba esta frase?»."),
    reinforce="Elige un dato que hayas leído esta semana y pregúntate si es hecho u opinión y qué fuente lo respalda.",
    extend="Escribe una pregunta nueva que te gustaría investigar y qué dos tipos de fuente usarías.",
)

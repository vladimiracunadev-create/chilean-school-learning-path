"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 08 (quiebre de la democracia, régimen militar y recuperación de la democracia)."""
from __future__ import annotations

from hi5_lib import build

OA8 = "HI06 OA 08"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 33 (cronología, hecha para este cuaderno). "
     "1970: Salvador Allende gana las elecciones presidenciales y asume la presidencia en noviembre. "
     "1970-1973: período de profundos cambios y de fuertes desacuerdos políticos en el país. "
     "11 de septiembre de 1973: las Fuerzas Armadas y de Orden derrocan al gobierno de Allende; termina el gobierno democrático. "
     "1973-1990: gobierna un régimen militar presidido por Augusto Pinochet. Se cierra el Congreso, se prohíben los partidos políticos y se violan los derechos humanos de muchas personas. "
     "1980: se aprueba en un plebiscito una nueva Constitución. "
     "5 de octubre de 1988: plebiscito sobre si Pinochet continuaría gobernando; gana la opción NO. "
     "Diciembre de 1989: elecciones presidenciales; gana Patricio Aylwin. "
     "11 de marzo de 1990: Aylwin asume la presidencia y termina el régimen militar.")
build(
    OA8, 1, F,
    use="Aprenderé a ubicar en el tiempo el quiebre de la democracia, el régimen militar y la recuperación de la democracia. Sirve para entender el orden de los hechos antes de analizarlos.",
    prior=["Sé qué es una democracia: la gente elige a sus autoridades.", "Sé leer una línea de tiempo y restar años.", "Sé que un hecho tiene causas y consecuencias."],
    explain=[
        "En 1973 se produjo en Chile el quiebre de la democracia: el gobierno elegido de Salvador Allende fue derrocado por las Fuerzas Armadas y de Orden el 11 de septiembre. Quiebre significa que se rompió el funcionamiento normal de las instituciones democráticas, como el Congreso y las elecciones.",
        "Entre 1973 y 1990 gobernó un régimen militar encabezado por Augusto Pinochet. En esos años se cerró el Congreso, se prohibieron los partidos políticos y se cometieron graves violaciones a los derechos humanos, como detenciones, torturas y desapariciones. Los derechos humanos son los derechos que tiene toda persona por el solo hecho de serlo.",
        "El camino de regreso a la democracia se hizo con votaciones. En 1988 hubo un plebiscito sobre si Pinochet continuaba en el poder y ganó el NO. Un año después se eligió presidente a Patricio Aylwin, quien asumió en marzo de 1990. Esta secuencia de hechos se llama recuperación de la democracia.",
    ],
    vocab=[("quiebre de la democracia", "ruptura del funcionamiento normal de las instituciones democráticas"), ("régimen militar", "gobierno dirigido por las Fuerzas Armadas, no elegido en elecciones libres"), ("derechos humanos", "derechos que tiene toda persona por el solo hecho de serlo"), ("plebiscito", "votación en que los ciudadanos responden sí o no a una pregunta"), ("recuperación de la democracia", "regreso a un gobierno elegido por los ciudadanos")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años duró el régimen militar?", ["La ficha indica que fue de 1973 a 1990.", "Resto: 1990 − 1973 = 17."], "17 años"),
        ("Ordenar hechos", "{F} ¿Qué ocurrió antes: el plebiscito de 1988 o la elección de Aylwin?", ["El plebiscito fue en octubre de 1988.", "La elección fue en diciembre de 1989."], "El plebiscito de 1988"),
    ],
    mistakes=[("Creer que el régimen militar terminó en el plebiscito de 1988.", "Se confunde el plebiscito con el cambio de gobierno.", "El régimen terminó en marzo de 1990, cuando asumió Aylwin."),
              ("Confundir el plebiscito de 1980 con el de 1988.", "Se mezclan los años.", "En 1980 se aprobó una nueva Constitución; en 1988 se decidió si Pinochet continuaba.")],
    T=[
        ("{F} ¿En qué año ganó Allende las elecciones?", "1970", "La ficha lo indica."),
        ("{F} ¿Qué ocurrió el 11 de septiembre de 1973?", "las Fuerzas Armadas y de Orden derrocaron al gobierno de Allende", "La ficha lo dice."),
        ("{F} ¿Qué opción ganó el plebiscito de 1988?", "la opción NO", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre el quiebre de la democracia y el plebiscito de 1988?", "1988-1973", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Quién asumió la presidencia en marzo de 1990?", "Patricio Aylwin", "La ficha lo dice."),
        ("{F} ¿Qué se prohibió durante el régimen militar según la ficha?", "los partidos políticos", "La ficha lo indica."),
        ("{F} Ordena de más antiguo a más reciente: plebiscito de 1988, golpe de 1973, asunción de Aylwin, elecciones de 1970.", "elecciones de 1970, golpe de 1973, plebiscito de 1988, asunción de Aylwin", "Los años son 1970, 1973, 1988 y 1990."),
        ("=", "{F} ¿Cuántos años pasaron entre la nueva Constitución de 1980 y el plebiscito de 1988?", "1988-1980", "Se resta el año menor al mayor.", " años"),
        ("{F} Clasifica como «quiebre», «régimen» o «recuperación»: a) 11 de septiembre de 1973; b) cierre del Congreso; c) plebiscito de 1988; d) asunción de Aylwin.", "quiebre: a; régimen: b; recuperación: c y d", "Cada hecho pertenece a una etapa."),
        ("{F} Un compañero dice: «El plebiscito de 1988 eligió a Aylwin». Corrígelo.", "No: en 1988 se decidió si Pinochet continuaba; Aylwin fue elegido en 1989", "La ficha distingue ambos hechos."),
        ("{F} Una alumna dice: «El régimen militar duró 7 años». ¿Qué error comete?", "duró 17 años, de 1973 a 1990", "1990 − 1973 = 17."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1960. ¿A cuántos cm queda el año 1990?", "3 cm", "(1990 − 1960) ÷ 10 = 3."),
        ("{F} ¿Por qué se llama recuperación de la democracia al período 1988-1990?", "porque se volvió a un gobierno elegido por los ciudadanos", "Se volvió a elegir a las autoridades."),
    ],
    ctx=("Una placa en un parque dice «1988: la ciudadanía decidió». ¿A qué hecho de la ficha se refiere?", "al plebiscito del 5 de octubre de 1988", "En ese plebiscito la gente votó."),
    sc=[("¿Qué son los derechos humanos?", "los derechos que tiene toda persona por el solo hecho de serlo", "Es la definición de la clase."),
        ("{F} ¿En qué año asumió Aylwin?", "1990", "La ficha lo dice."),
        ("¿Qué es un plebiscito?", "una votación en que los ciudadanos responden sí o no a una pregunta", "Es la definición de la clase.")],
    op=("Dibuja una línea de tiempo desde 1970 hasta 1990 con los hechos de la ficha. Usa tres colores: uno para el quiebre de la democracia, otro para el régimen militar y otro para la recuperación de la democracia. Escribe el año junto a cada hecho. {F}",
        "1970, 1973, 1980, 1988, 1989 y 1990 en orden, con tres colores.",
        ["seis hechos ordenados", "tres colores bien usados", "años correctos"], ["línea de tiempo coloreada"], ["poner el plebiscito antes de 1980", "pintar 1990 como régimen militar"],
        "Pide que explique con sus palabras la diferencia entre quiebre y recuperación."),
    reinforce="Di en voz alta los años de la ficha y qué ocurrió en cada uno.",
    extend="Escribe una pregunta sobre cómo vivía una familia durante los años del régimen militar, para preguntarla a un adulto de tu casa solo si quieres.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 34 (fuentes inventadas para este cuaderno, basadas en hechos conocidos). "
     "Fuente A, noticia de un diario, 6 de octubre de 1988 (texto inventado): «La opción NO ganó el plebiscito. Miles de personas salieron a las calles». "
     "Fuente B, testimonio de una persona que fue detenida en 1974 (texto inventado): «Estuve detenida varios días sin que mi familia supiera dónde. Nunca olvidaré ese tiempo». "
     "Fuente C, declaración de un partidario del régimen militar, 1985 (texto inventado): «Hubo un orden en la economía que antes no existía». "
     "Fuente D, informe de una comisión de verdad, 1991: reúne casos de personas muertas o desaparecidas durante el régimen militar.")
build(
    OA8, 2, F,
    use="Aprenderé a leer fuentes sobre el quiebre de la democracia, el régimen militar y la recuperación de la democracia. Sirve para escuchar distintas voces con respeto y apoyarse en evidencia.",
    prior=["Sé la diferencia entre fuente primaria y secundaria.", "Sé ubicar los hechos de 1973 a 1990.", "Sé que cada fuente tiene un punto de vista."],
    explain=[
        "Sobre el pasado reciente existen muchas fuentes: noticias, testimonios, declaraciones e informes. Los testimonios son relatos de personas que vivieron los hechos. Los informes de comisiones reúnen casos y datos investigados. Cada fuente debe analizarse preguntando quién habla, cuándo y para qué.",
        "La noticia de 1988 (fuente A) cuenta el resultado del plebiscito. El testimonio de una persona detenida (fuente B) muestra una experiencia dolorosa. La declaración de un partidario del régimen (fuente C) muestra una valoración distinta. El informe de una comisión (fuente D) reúne casos de violaciones a los derechos humanos investigados por una comisión oficial.",
        "Es importante tratar estos temas con respeto, porque muchas familias sufrieron. También hay que distinguir entre un testimonio, que es la experiencia de una persona, y un informe que reúne muchos casos. Ninguna fuente sola cuenta todo, y hoy existe un consenso amplio en que las violaciones a los derechos humanos nunca están justificadas.",
    ],
    vocab=[("testimonio", "relato de una persona que vivió un hecho"), ("comisión", "grupo de personas que investiga un asunto"), ("informe", "documento que explica lo investigado"), ("consenso", "acuerdo amplio entre personas con ideas distintas"), ("valoración", "juicio sobre si algo fue bueno o malo")],
    worked=[
        ("Clasificar una fuente", "{F} ¿La fuente B es un testimonio o un informe?", ["Es el relato de una persona que vivió el hecho.", "No reúne muchos casos."], "Un testimonio"),
        ("Reconocer un punto de vista", "{F} ¿Qué valora el autor de la fuente C?", ["Es un partidario del régimen.", "Habla de un orden en la economía."], "El orden en la economía"),
    ],
    mistakes=[("Creer que un testimonio muestra lo que vivieron todas las personas.", "Se generaliza desde un caso.", "Un testimonio muestra una experiencia; hay que compararlo con otras fuentes."),
              ("Pensar que una valoración económica justifica violar derechos humanos.", "Se confunden aspectos distintos.", "Hoy hay consenso en que las violaciones a los derechos humanos nunca se justifican.")],
    T=[
        ("{F} ¿Qué opción ganó el plebiscito según la fuente A?", "la opción NO", "La noticia lo dice."),
        ("{F} ¿En qué año se escribió la fuente C?", "1985", "La ficha lo indica."),
        ("{F} ¿Qué reúne la fuente D?", "casos de personas muertas o desaparecidas durante el régimen militar", "La ficha lo dice."),
        ("{F} ¿Cuál de las fuentes es un informe de una comisión?", "la fuente D", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre el testimonio de 1974 y la noticia de 1988?", "1988-1974", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué fuente cuenta una experiencia personal de detención?", "la fuente B", "Es un testimonio."),
        ("{F} ¿Cuál fuente muestra una valoración favorable del régimen en la economía?", "la fuente C", "Habla de un orden económico."),
        ("{F} Compara B y C: ¿quién habla desde la experiencia de una detención y quién desde la economía?", "B desde la detención y C desde la economía", "Cada una habla de un aspecto distinto."),
        ("{F} Un compañero dice: «Como C valora la economía, no importa lo que dice B». ¿Qué respuesta le darías?", "ambas fuentes aportan información y los derechos humanos no se pueden dejar de lado", "El orden económico no justifica la violación de derechos."),
        ("{F} Una alumna dice: «La fuente A es un testimonio». ¿Qué error comete?", "es una noticia, no el relato de una persona", "La ficha la presenta como noticia."),
        ("{F} Nombra un grupo de personas que también vivió esos años y cuya voz no aparece en ninguna de las cuatro fuentes.", "por ejemplo, los niños, los jóvenes o las familias del campo (cualquier grupo razonable)", "Las fuentes solo recogen unas pocas voces."),
        ("{F} Para saber qué pasó en 1988, ¿cuál es la fuente más cercana al hecho?", "la fuente A", "Es una noticia de 1988."),
        ("{F} Ordena las fuentes de la más antigua a la más reciente.", "B, C, A, D", "Los años son 1974, 1985, 1988 y 1991."),
    ],
    ctx=("Un compañero propone presentar solo la fuente C para explicar el régimen militar. ¿Qué le dirías?", "que agregue las fuentes B y D, porque la C no habla de derechos humanos", "Hay que incluir otras voces."),
    sc=[("¿Qué es un testimonio?", "el relato de una persona que vivió un hecho", "Es la definición de la clase."),
        ("{F} ¿Qué tipo de fuente es la D?", "un informe de una comisión", "La ficha lo dice."),
        ("¿Por qué hay que tratar este tema con respeto?", "porque muchas familias sufrieron", "Son hechos dolorosos.")],
    op=("Haz una ficha con las cuatro fuentes. Anota quién habla, año, qué dice y qué no dice. Termina con dos oraciones que expliquen por qué una conclusión necesita varias fuentes y por qué los derechos humanos importan. {F}",
        "B: persona detenida, 1974, cuenta su experiencia; no dice qué pensaban otras personas. D: comisión, 1991, reúne casos; no cuenta cada vida con detalle.",
        ["cuatro fuentes analizadas", "qué dice y qué no dice", "dos oraciones finales"], ["ficha de análisis", "dos oraciones"], ["tratar un testimonio como informe", "no mencionar los derechos humanos"],
        "Pide que explique con respeto por qué eligió esas palabras."),
    reinforce="Con tus palabras, resume lo que cuenta cada fuente.",
    extend="Escribe una pregunta que le harías a una persona que vivió esos años, marcando que solo la formularás si esa persona quiere responder.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 35 (actores, causas y consecuencias, hecha para este cuaderno). "
     "Antecedentes del quiebre de 1973, según las explicaciones conocidas: fuertes desacuerdos políticos y polarización entre grupos de la sociedad; dificultades económicas y escasez de algunos productos; tensiones entre el gobierno, el Congreso y otros poderes del Estado; el contexto de la Guerra Fría, en que el mundo estaba dividido en dos bloques. "
     "Consecuencias del quiebre: se terminó el gobierno elegido; se cerró el Congreso y se prohibieron los partidos; hubo violaciones a los derechos humanos, con personas detenidas, torturadas, ejecutadas o desaparecidas, y miles se exiliaron. "
     "Actores de la recuperación de la democracia: la Iglesia, a través de la Vicaría de la Solidaridad (1976); organizaciones de familiares de detenidos desaparecidos; partidos políticos que formaron la Concertación; ciudadanos que votaron NO en 1988.")
build(
    OA8, 3, F,
    use="Aprenderé a explicar los antecedentes y las consecuencias del quiebre de la democracia y quiénes ayudaron a recuperarla. Sirve para entender que los hechos tienen varias causas y varios actores.",
    prior=["Sé ubicar los hechos de 1970 a 1990.", "Sé distinguir causa y consecuencia.", "Sé que hay distintas perspectivas sobre un mismo hecho."],
    explain=[
        "Los historiadores explican el quiebre de la democracia con varios antecedentes, no con uno solo. Entre ellos están los fuertes desacuerdos políticos y la polarización, las dificultades económicas, las tensiones entre poderes del Estado y el contexto de la Guerra Fría, que dividió al mundo en dos bloques. No hay una única explicación, y las personas discuten qué peso tuvo cada una.",
        "Entre las consecuencias del quiebre están el fin del gobierno elegido, el cierre del Congreso, la prohibición de los partidos y las violaciones a los derechos humanos. Miles de personas fueron detenidas o exiliadas, y otras fueron ejecutadas o desaparecidas. Sus familias aún buscan verdad y justicia.",
        "La democracia se recuperó gracias a muchos actores. La Iglesia, a través de la Vicaría de la Solidaridad, apoyó a víctimas y familias. Las organizaciones de familiares de detenidos desaparecidos pidieron saber la verdad. Los partidos políticos se unieron en la Concertación, y la ciudadanía votó NO en el plebiscito de 1988. Así, el cambio fue obra de muchas personas.",
    ],
    vocab=[("polarización", "división fuerte de la sociedad en dos grupos opuestos"), ("Guerra Fría", "tensión entre dos bloques de países, con ideas distintas, después de 1945"), ("exilio", "obligación de vivir fuera del país"), ("víctima", "persona que sufrió un daño injusto"), ("Concertación", "alianza de partidos políticos que se unieron para recuperar la democracia")],
    worked=[
        ("Clasificar causa y consecuencia", "{F} ¿El cierre del Congreso es causa o consecuencia del quiebre?", ["Ocurre después del 11 de septiembre de 1973.", "La ficha lo lista entre las consecuencias."], "Consecuencia"),
        ("Reconocer un actor", "{F} ¿Qué organización de la Iglesia apoyó a las víctimas?", ["Busco una organización de la Iglesia.", "Es la Vicaría de la Solidaridad."], "La Vicaría de la Solidaridad"),
    ],
    mistakes=[("Explicar el quiebre con una sola causa.", "Se simplifica un hecho complejo.", "Hubo varios antecedentes, y se discute su peso."),
              ("Creer que la democracia volvió gracias a una sola persona.", "Se olvidan los demás actores.", "Participaron la Iglesia, organizaciones de familiares, partidos y la ciudadanía.")],
    T=[
        ("{F} ¿Qué organización de la Iglesia se creó en 1976?", "la Vicaría de la Solidaridad", "La ficha lo indica."),
        ("{F} ¿Qué alianza de partidos se formó para recuperar la democracia?", "la Concertación", "La ficha la nombra."),
        ("{F} ¿Qué opción votaron en 1988 los ciudadanos que la ficha nombra entre los actores de la recuperación de la democracia?", "NO", "La ficha lo dice."),
        ("{F} Clasifica como antecedente (A) o consecuencia (C): a) polarización; b) cierre del Congreso; c) dificultades económicas; d) exilio de miles de personas.", "a: A; b: C; c: A; d: C", "Los antecedentes son anteriores a 1973."),
        ("{F} ¿Qué contexto mundial se menciona entre los antecedentes?", "la Guerra Fría", "La ficha lo nombra."),
        ("{F} ¿Qué pedían las organizaciones de familiares de detenidos desaparecidos?", "saber la verdad sobre lo ocurrido", "La explicación lo indica."),
        ("{F} Nombra dos actores de la recuperación de la democracia, aparte de los partidos y de la ciudadanía que votó.", "la Iglesia (Vicaría de la Solidaridad) y las organizaciones de familiares", "La ficha los enumera."),
        ("=", "{F} ¿Cuántos años pasaron entre la creación de la Vicaría de la Solidaridad y el plebiscito de 1988?", "1988-1976", "Se resta el año menor al mayor.", " años"),
        ("{F} Un compañero dice: «Hay una sola explicación del quiebre». Corrígelo.", "no: hubo varios antecedentes y se discute su peso", "La ficha lista varios."),
        ("{F} Una alumna dice: «La democracia volvió solo porque ganó el NO». ¿Qué le falta?", "mencionar a la Iglesia, las organizaciones de familiares y los partidos que trabajaron antes", "Hubo muchos actores."),
        ("{F} Elige la mejor frase. A) Las violaciones a los derechos humanos tuvieron consecuencias dolorosas para miles de personas. B) No pasó nada importante.", "A", "A coincide con la ficha."),
        ("{F} ¿Por qué se dice que las familias aún buscan verdad y justicia?", "porque muchas personas siguen desaparecidas", "La ficha habla de personas desaparecidas."),
        ("{F} ¿Qué pregunta ayuda a no simplificar el quiebre?", "qué antecedentes hubo y qué peso tuvo cada uno", "Obliga a considerar varias causas."),
    ],
    ctx=("En un debate escolar, un compañero dice: «El quiebre fue solo culpa de un grupo». Usa la ficha para responder con respeto.", "los antecedentes fueron varios, como la polarización, la economía, las tensiones entre poderes y la Guerra Fría", "No se puede explicar con una sola causa."),
    sc=[("¿Qué es la polarización?", "una división fuerte de la sociedad en dos grupos opuestos", "Es la definición de la clase."),
        ("{F} ¿Qué es la Concertación?", "una alianza de partidos que se unieron para recuperar la democracia", "La ficha la presenta así."),
        ("¿Por qué no hay una sola explicación del quiebre?", "porque hubo varios antecedentes y las personas discuten su peso", "Es un hecho complejo.")],
    op=("Dibuja una tabla de tres columnas: «antecedentes», «hecho» y «consecuencias». Escribe dos antecedentes, el hecho central y dos consecuencias. Debajo, escribe qué actores ayudaron a recuperar la democracia. {F}",
        "Antecedentes: polarización y dificultades económicas. Hecho: 11 de septiembre de 1973. Consecuencias: cierre del Congreso y violaciones a los derechos humanos. Actores: Iglesia, familiares, partidos y ciudadanos.",
        ["tres columnas completas", "antecedentes y consecuencias bien clasificados", "actores nombrados"], ["tabla", "lista de actores"], ["poner el cierre del Congreso como antecedente", "decir que hubo una sola causa"],
        "Pide que explique por qué eligió esos dos antecedentes."),
    reinforce="Di en voz alta dos antecedentes, dos consecuencias y dos actores de la recuperación de la democracia.",
    extend="Escribe una pregunta sobre qué papel pudieron tener los jóvenes en esos años.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 36 (visiones distintas, hechas para este cuaderno; textos inventados que resumen opiniones que existen). "
     "Visión 1 (sobre el quiebre de 1973): «Lo más importante fue la división de la sociedad; todos los sectores tuvieron responsabilidad en no lograr acuerdos». "
     "Visión 2 (sobre el quiebre de 1973): «Lo más importante fue la decisión de las Fuerzas Armadas de derrocar a un gobierno elegido por el pueblo; eso nunca debió ocurrir». "
     "Visión 3 (sobre el régimen militar): «Hubo cambios económicos que modernizaron el país, pero eso no justifica las violaciones a los derechos humanos». "
     "Visión 4 (sobre el régimen militar): «Lo central fueron las violaciones a los derechos humanos y la falta de libertades». "
     "Consenso actual: la mayoría de las personas valora la democracia y rechaza las violaciones a los derechos humanos.")
build(
    OA8, 4, F,
    use="Aprenderé a comparar distintas visiones sobre el quiebre de la democracia y el régimen militar, y a reconocer el consenso actual. Sirve para entender por qué las personas explican el mismo hecho de maneras diferentes.",
    prior=["Sé qué es una perspectiva.", "Sé distinguir hecho de opinión.", "Sé los hechos de 1970 a 1990."],
    explain=[
        "Una visión es una manera de interpretar un hecho. Sobre el quiebre de 1973, algunas visiones ponen el acento en la división de la sociedad y en que todos los sectores tuvieron responsabilidad. Otras ponen el acento en la decisión de derrocar a un gobierno elegido. Estas visiones se pueden comparar, porque cada una destaca algo distinto.",
        "Sobre el régimen militar también hay visiones diferentes. Algunas destacan los cambios económicos, y otras ponen en el centro las violaciones a los derechos humanos. Aun así, hoy existe un consenso amplio: las violaciones a los derechos humanos son inaceptables, y la democracia es el sistema más adecuado para convivir, aunque haya desacuerdos.",
        "Para comparar visiones, usamos criterios: qué destaca cada una, qué deja de lado y qué hechos se pueden comprobar. Es un hecho que hubo un golpe de Estado y violaciones a los derechos humanos; es una opinión decir cuál fue la causa principal. Comprender una visión no significa compartirla, pero ayuda a convivir en democracia.",
    ],
    vocab=[("visión", "manera de interpretar un hecho"), ("responsabilidad", "parte que le corresponde a cada persona o grupo en lo ocurrido"), ("consenso", "acuerdo amplio entre personas con ideas distintas"), ("golpe de Estado", "derrocamiento de un gobierno por la fuerza"), ("inaceptable", "que no se puede aceptar")],
    worked=[
        ("Comparar dos visiones", "{F} ¿Qué diferencia hay entre las visiones 1 y 2?", ["La visión 1 destaca la división de la sociedad.", "La visión 2 destaca la decisión de derrocar a un gobierno elegido."], "La visión 1 destaca la división de la sociedad y la 2 la decisión de derrocar al gobierno"),
        ("Reconocer el consenso", "{F} ¿En qué hay consenso actual según la ficha?", ["Leo la última parte.", "Valoran la democracia y rechazan las violaciones a los derechos humanos."], "En valorar la democracia y rechazar las violaciones a los derechos humanos"),
    ],
    mistakes=[("Creer que comprender una visión es estar de acuerdo con ella.", "Se confunde comprender con aceptar.", "Comprender es explicar por qué alguien piensa así."),
              ("Pensar que no hay ningún acuerdo posible.", "Se olvida el consenso.", "Existe consenso en valorar la democracia y rechazar las violaciones a los derechos humanos.")],
    T=[
        ("{F} ¿Qué destaca la visión 1?", "la división de la sociedad", "La ficha lo indica."),
        ("{F} ¿Qué destaca la visión 4?", "las violaciones a los derechos humanos y la falta de libertades", "La ficha lo indica."),
        ("{F} ¿Qué reconoce la visión 3, además de los cambios económicos?", "que eso no justifica las violaciones a los derechos humanos", "La ficha lo dice."),
        ("{F} ¿Cuál es el consenso actual según la ficha?", "valorar la democracia y rechazar las violaciones a los derechos humanos", "La ficha lo indica."),
        ("{F} Clasifica como hecho (H) u opinión (O): a) Hubo un golpe de Estado en 1973; b) la causa principal fue la división; c) hubo violaciones a los derechos humanos.", "a: H; b: O; c: H", "Los hechos se comprueban con fuentes."),
        ("{F} ¿Qué visiones se refieren al quiebre de 1973?", "las visiones 1 y 2", "La ficha las rotula así."),
        ("{F} ¿Qué visiones se refieren al régimen militar?", "las visiones 3 y 4", "La ficha las rotula así."),
        ("{F} Compara 3 y 4: ¿qué tienen en común?", "ambas reconocen que hubo violaciones a los derechos humanos", "La visión 3 las menciona y la 4 las pone en el centro."),
        ("{F} Un compañero dice: «Como existen distintas visiones, todo es opinión». ¿Qué error comete?", "hay hechos comprobables, como el golpe y las violaciones a los derechos humanos", "Los hechos no dependen de la opinión."),
        ("{F} Una alumna dice: «No hay acuerdos entre las personas». Corrígela con la ficha.", "sí: hay consenso en valorar la democracia y rechazar las violaciones a los derechos humanos", "La ficha lo indica."),
        ("{F} Elige la mejor oración comparativa. A) Mientras la visión 1 destaca la división, la visión 2 destaca el derrocamiento de un gobierno elegido. B) Ambas dicen exactamente lo mismo.", "A", "A contrasta lo que destaca cada visión."),
        ("{F} ¿Qué criterio de comparación usas si preguntas qué destaca cada visión?", "lo que cada una pone en el centro", "Es el primer criterio de la explicación."),
        ("{F} ¿Por qué ayuda a la democracia comprender visiones distintas?", "porque permite convivir y dialogar aunque haya desacuerdos", "La clase lo explica."),
    ],
    ctx=("En un debate escolar, dos compañeros defienden las visiones 1 y 2. ¿Cómo puedes ayudar a que conversen con respeto?", "pidiéndoles que expliquen qué destaca cada visión y que reconozcan el consenso en los derechos humanos", "Comparar y reconocer el consenso favorece el respeto."),
    sc=[("¿Qué es una visión?", "una manera de interpretar un hecho", "Es la definición de la clase."),
        ("{F} ¿Qué es un consenso?", "un acuerdo amplio entre personas con ideas distintas", "Es la definición de la clase."),
        ("¿Comprender una visión es compartirla?", "no, es entender por qué alguien piensa así", "Comprender no es aprobar.")],
    op=("Elige dos visiones de la ficha y escribe un cuadro con tres filas: «qué destaca», «qué deja de lado» y «qué hechos la apoyan». Después escribe una oración que compare ambas y otra que explique el consenso actual. {F}",
        "Visión 1: destaca la división; deja de lado la decisión de derrocar al gobierno; hechos: hubo polarización. Visión 2: destaca el derrocamiento; deja de lado la responsabilidad de otros. Consenso: valorar la democracia.",
        ["dos visiones con tres filas", "oración comparativa", "consenso explicado"], ["cuadro de comparación", "dos oraciones"], ["decir que una visión es la única correcta", "no mencionar el consenso"],
        "Pide que explique con respeto una frase que le haya parecido difícil."),
    reinforce="Di en voz alta qué destaca cada visión y en qué hay consenso.",
    extend="Escribe una pregunta que ayude a conversar con respeto con alguien que piensa distinto.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 37 (el valor de la democracia, hecha para este cuaderno). "
     "Elementos de una democracia: ciudadanos que eligen a sus autoridades en votaciones libres; división del poder en Ejecutivo, Congreso y tribunales; respeto a los derechos humanos; libertad de expresión y de asociación; posibilidad de cambiar a las autoridades sin violencia. "
     "En 1988 se decidió en un plebiscito si Pinochet continuaba o no. La opción NO ganó y se abrió el camino a elecciones libres. "
     "Hoy, la mayoría de las personas acepta el valor de la democracia y rechaza las violaciones a los derechos humanos, aunque existan desacuerdos políticos. "
     "Los desacuerdos se resuelven votando, conversando y respetando las reglas.")
build(
    OA8, 5, F,
    use="Aprenderé a argumentar por qué la democracia es valiosa, usando hechos del pasado reciente de Chile. Sirve para defender una idea con evidencia y respeto.",
    prior=["Sé qué ocurrió entre 1970 y 1990.", "Sé qué es un argumento: afirmación, evidencia y razón.", "Sé que existen visiones distintas."],
    explain=[
        "Argumentar es defender una idea con razones y evidencia. En esta clase argumentamos sobre el valor de la democracia. La democracia permite que los ciudadanos elijan a sus autoridades, que el poder esté dividido y que se respeten los derechos humanos y las libertades.",
        "La experiencia chilena entrega evidencia. Cuando se rompió la democracia en 1973, se cerró el Congreso, se prohibieron los partidos y se violaron los derechos humanos. Cuando se recuperó, en 1988-1990, se pudieron elegir libremente las autoridades. Por eso hoy hay un amplio acuerdo en valorar la democracia.",
        "Un buen argumento incluye una objeción: puede haber desacuerdos, y la democracia no resuelve todos los problemas. Sin embargo, permite discutir, cambiar autoridades sin violencia y corregir errores. Responder a la objeción hace más sólido el argumento y ayuda a convivir con respeto.",
    ],
    vocab=[("argumento", "idea defendida con una razón y una evidencia"), ("evidencia", "dato que apoya una idea"), ("libertad de expresión", "derecho a decir lo que uno piensa respetando a los demás"), ("poder dividido", "poder repartido entre varias instituciones para que ninguna mande sola"), ("objeción", "razón en contra de una idea")],
    worked=[
        ("Armar un argumento", "{F} Defiende que la democracia es valiosa porque permite cambiar autoridades sin violencia.", ["Afirmación: la democracia es valiosa.", "Evidencia y razón: en 1988 se decidió con un voto y se abrió el camino a elecciones libres."], "La democracia es valiosa porque permitió decidir con votos y llegar a elecciones libres"),
        ("Reconocer una objeción", "{F} ¿Qué objeción podría alguien hacer?", ["Piensa en lo que la democracia no hace.", "No resuelve todos los problemas."], "Que no resuelve todos los problemas"),
    ],
    mistakes=[("Defender la democracia sin dar ejemplos.", "Se queda en una opinión.", "Se necesita un dato, como el plebiscito de 1988."),
              ("Creer que la democracia elimina todos los desacuerdos.", "Se confunde democracia con unanimidad.", "La democracia permite resolver desacuerdos con votos, diálogo y reglas.")],
    T=[
        ("{F} ¿Cómo se eligen las autoridades en una democracia?", "con votaciones libres", "La ficha lo indica."),
        ("{F} ¿Qué se decidió en el plebiscito de 1988?", "si Pinochet continuaba o no", "La ficha lo dice."),
        ("{F} ¿Qué poderes del Estado se mencionan en la ficha?", "el Ejecutivo, el Congreso y los tribunales", "La ficha los enumera."),
        ("{F} ¿Cuál es un argumento con evidencia? A) La democracia es lo mejor porque sí. B) La democracia es valiosa porque en 1988 un plebiscito abrió el camino a elecciones libres.", "B", "B tiene afirmación y evidencia."),
        ("{F} ¿Qué libertad permite decir lo que uno piensa?", "la libertad de expresión", "La ficha la nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre el quiebre de 1973 y el plebiscito de 1988?", "1988-1973", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué dato de 1973 sirve como evidencia de lo que pasa cuando se rompe la democracia?", "se cerró el Congreso y se prohibieron los partidos", "La clase lo explica."),
        ("{F} ¿Qué objeción se puede hacer al argumento «la democracia resuelve todo»?", "que no resuelve todos los problemas", "La clase lo señala."),
        ("{F} Un compañero dice: «En democracia nadie discute». Corrígelo.", "en democracia hay desacuerdos, pero se resuelven votando, conversando y respetando las reglas", "La ficha lo indica."),
        ("{F} Una alumna dice: «No importa respetar los derechos humanos si se logra un buen resultado económico». ¿Qué respuesta le darías?", "hay consenso en que las violaciones a los derechos humanos no se justifican", "El consenso actual rechaza esa idea."),
        ("{F} ¿Qué razón explica por qué se dice que la democracia permite corregir errores?", "porque se pueden cambiar las autoridades sin violencia", "Es un elemento de la ficha."),
        ("{F} Completa: «La democracia es valiosa porque ______». Elige la opción con evidencia: A) permite elegir autoridades libremente; B) es un nombre bonito.", "A", "A es una razón con base en la ficha."),
        ("{F} ¿Qué parte de un argumento responde a una objeción?", "la respuesta final que reconoce el límite y lo contesta", "Es la parte que lo hace más sólido."),
    ],
    ctx=("Tu curso prepara un afiche sobre el valor de la democracia. Escribe una frase con una razón y una evidencia.", "La democracia es valiosa porque permite elegir libremente las autoridades, como ocurrió después del plebiscito de 1988", "Cualquier frase con razón y evidencia de la ficha sirve."),
    sc=[("¿Cuáles son las tres partes de un argumento?", "afirmación, evidencia y razón", "Así se organiza un argumento."),
        ("{F} ¿Qué se necesita para que el poder esté dividido?", "varias instituciones: Ejecutivo, Congreso y tribunales", "Así ninguna manda sola."),
        ("¿Para qué sirve responder a una objeción?", "para que el argumento sea más sólido", "Reconoce razones contrarias.")],
    op=("Escribe un texto de cinco oraciones: 1) afirma por qué la democracia es valiosa; 2) da un dato del plebiscito de 1988; 3) explica qué libertad o derecho se protege; 4) escribe una objeción; 5) responde a la objeción. {F}",
        "La democracia es valiosa. En 1988 un plebiscito decidió con votos. Se protege la libertad de expresión. Una objeción es que no resuelve todo. Aun así, permite corregir errores sin violencia.",
        ["afirmación clara", "dato de la ficha", "objeción y respuesta"], ["texto de cinco oraciones"], ["no incluir dato", "no responder la objeción"],
        "Pide que lea su texto en voz alta y diga cuál es la evidencia."),
    reinforce="Di en voz alta tres razones por las cuales la democracia es valiosa.",
    extend="Escribe una pregunta sobre cómo puedes practicar la democracia en tu curso.",
)

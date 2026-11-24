"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 3 (parte 3): OAD-11, contrastar perspectivas sobre los conflictos internos en Chile en la segunda mitad del siglo XX (quiebre de la democracia, Dictadura militar, transición y Derechos Humanos). Las fuentes son textos de ejemplo inventados; los hechos generales son los estándar de los programas escolares y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Todas las fuentes de esta clase son extractos inventados «de ejemplo», escritos en cada ejercicio: no son citas de personas reales y no necesitas internet, mapas ni libros. "
             "Este tema es sensible: muchas personas vivieron esos años y hay familias afectadas. Nadie te pide contar su experiencia ni la de su familia; trabaja solo con los casos del cuaderno y, si algo te incomoda, puedes pausar o pedir apoyo. "
             "Se trabaja con respeto, con hechos comprobados y sin justificar la violación de los derechos humanos.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NM1-OAD-11"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Cronología escrita para este cuaderno con hechos generales: entre 1964 y 1970 gobernó Eduardo Frei Montalva y se impulsó la reforma agraria; "
      "entre 1970 y 1973 gobernó Salvador Allende; el 11 de septiembre de 1973 las Fuerzas Armadas y de Orden derrocaron al gobierno y comenzó una dictadura militar encabezada por Augusto Pinochet, que duró hasta 1990; "
      "en 1988 se realizó un plebiscito y en 1990 volvieron los gobiernos elegidos por la ciudadanía. "
      "Dos textos inventados. Texto A (de ejemplo): «Para mí, el gobierno daba más derechos a trabajadores y campesinos; su caída fue un quiebre injusto de la democracia.» "
      "Texto B (de ejemplo): «Para mí, había escasez de productos y conflictos tan fuertes que el país parecía partido en dos; yo temía por el futuro.»")
build(
    O, 1, F1,
    use="Hoy ubico los grandes hechos de la segunda mitad del siglo XX en Chile y reconozco que hay distintas perspectivas sobre los conflictos internos de esos años.",
    prior=["Sé que una perspectiva es un punto de vista.", "Distingo un hecho de una opinión.", "He visto que dos personas pueden contar distinto un mismo suceso."],
    explain=[
        "Un conflicto interno es una disputa profunda dentro de un mismo país, entre grupos que no logran resolver sus diferencias por las vías acordadas. En la segunda mitad del siglo XX, Chile vivió conflictos políticos, económicos y sociales cada vez más intensos hasta el quiebre de la democracia en 1973, la dictadura militar y la posterior transición.",
        "Hay hechos que están comprobados, como las fechas y los acontecimientos de la cronología. Otros son interpretaciones: por qué ocurrió, quién tuvo más responsabilidad o cómo valorarlo. Las perspectivas sobre estas preguntas fueron y son distintas, y se contrastan con fuentes.",
        "Contrastar no significa que todas las afirmaciones valgan lo mismo. Que hubo graves violaciones a los derechos humanos durante la dictadura está establecido por informes oficiales y sentencias de tribunales; lo que se discute son las causas, el contexto y cómo recordarlo. Trabajamos con empatía, respeto y rigor.",
    ],
    vocab=[("conflicto interno", "disputa profunda dentro de un mismo país"), ("dictadura", "gobierno que concentra el poder sin elecciones libres ni límites democráticos"), ("quiebre de la democracia", "ruptura del orden democrático"), ("plebiscito", "votación en que la ciudadanía responde sí o no a una pregunta"), ("hecho comprobado", "dato que se verifica con documentos")],
    worked=[
        ("Hecho o interpretación", "{F} Clasifica: «El 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno».", ["Es un acontecimiento con fecha, comprobable con documentos.", "Un acontecimiento verificable es un hecho comprobado."], "Hecho comprobado"),
        ("Qué comparar", "{F} ¿Qué diferencia hay entre los textos A y B?", ["El texto A valora los derechos para trabajadores y campesinos y ve un quiebre injusto.", "El texto B destaca la escasez y el temor por un país dividido."], "A valora los derechos y B destaca la escasez y el temor"),
    ],
    mistakes=[("Creer que contrastar perspectivas significa que cualquier afirmación vale lo mismo.", "Los hechos comprobados no se discuten; se discuten causas y valoraciones.", "Separa primero lo comprobado de lo interpretado."),
              ("Usar una perspectiva para justificar violaciones a los derechos humanos.", "Las violaciones están establecidas y no tienen justificación en ningún contexto.", "Contrasta causas y valoraciones, sin justificar abusos.")],
    T=[
        ("abc", "En HGCS: ¿qué es un plebiscito?", "Una votación en que se responde sí o no a una pregunta", "Una reunión de partidos", "Un decreto del gobierno", "El plebiscito consulta a la ciudadanía con una pregunta cerrada."),
        ("abc", "{F} ¿En qué año se derrocó al gobierno según la ficha?", "1973", "1964", "1988", "La ficha indica el 11 de septiembre de 1973."),
        ("ab", "{F} ¿Hasta qué año duró la dictadura militar según la ficha?", "1990", "1973", "La ficha dice que duró hasta 1990."),
        ("abc", "{F} ¿Qué gobierno impulsó la reforma agraria en los años sesenta, según la ficha?", "El de Eduardo Frei Montalva", "El de Augusto Pinochet", "El de un gobierno extranjero", "La ficha lo menciona para el periodo de 1964 a 1970."),
        ("abc", "{F} ¿Qué valora el texto A?", "Los derechos de trabajadores y campesinos", "La caída del gobierno", "La escasez", "Lo dice en su primera frase."),
        ("ab", "{F} ¿Qué destaca el texto B?", "La escasez de productos y el temor por el futuro", "La reforma agraria", "El texto B habla de un país partido en dos y de temor."),
        ("=", "{F} ¿Cuántos años duró la dictadura según las fechas de la ficha (de 1973 a 1990)?", "1990-1973", "Se restan los años de inicio y término para saber su duración.", " años"),
        ("abc", "{F} Una persona dice: «El texto B prueba que el golpe fue justificado». ¿Qué respuesta es más exacta?", "No: el texto B cuenta un temor y no justifica quitar derechos ni la violencia posterior", "Sí, lo prueba", "El texto B no dice nada", "Un temor personal no justifica los abusos."),
        ("abc", "{F} Una persona dice: «El texto A prueba que todo el país apoyaba al gobierno». ¿Qué falla?", "Es la mirada de una persona de ejemplo, no de todo el país", "Nada, es correcto", "El texto A no dice nada", "Una fuente no representa a toda la sociedad."),
        ("abc", "Entre estas frases, ¿cuál se puede comprobar con un documento?", "El plebiscito se realizó en 1988", "La dictadura fue lo peor que pasó", "Todos estaban de acuerdo", "Un plebiscito con fecha es un hecho; las otras son juicios."),
        ("ab", "¿Por qué contrastar perspectivas no es lo mismo que justificar abusos?", "Porque los abusos están comprobados y no tienen justificación", "Porque todas las opiniones valen igual", "Los informes oficiales establecieron graves violaciones a los derechos humanos."),
        ("abc", "{F} ¿Qué fuente buscarías para comparar la perspectiva de personas que vivieron en el campo?", "Un relato de ejemplo de una familia campesina de esa época", "Otro texto idéntico al A", "La cronología sola", "Otra voz distinta completa la comparación."),
        ("abc", "{F} ¿Qué tienen en común los textos A y B?", "Ambos expresan lo que una persona valora o teme; ninguno es un dato comprobado", "Ambos describen la reforma agraria", "Ambos son informes oficiales", "Los dos comienzan con «Para mí»: son miradas personales de ejemplo, no hechos."),
    ],
    ctx=("abc", "En un centro de adultos, el grupo quiere conversar sobre estos años sin que la conversación termine en pelea. ¿Qué técnica del cuaderno ayuda?", "Separar los hechos comprobados de las interpretaciones y escuchar cada perspectiva sin descalificar", "Evitar el tema para siempre", "Imponer una sola versión", "La técnica evita que la discusión confunda datos con opiniones."),
    sc=[("En HGCS: ¿qué es una dictadura?", "Un gobierno que concentra el poder sin elecciones libres", "Se caracteriza por falta de libertades y límites."),
        ("¿Qué se discute sobre el quiebre de la democracia?", "Sus causas, su contexto y su valoración", "Son temas de interpretación, no de datos."),
        ("¿Se justifican las violaciones a los derechos humanos?", "No, están comprobadas y no tienen justificación", "Las comisiones oficiales y los tribunales las establecieron.")],
    op=("Ficha de ejemplo: «Fuente 1 (cartel de ejemplo, década de 1960): ‘La tierra para quien la trabaja’. Fuente 2 (carta de ejemplo de un agricultor de esa época): ‘Me preocupa perder el campo que cuidó mi familia’.» "
        "Escribe quién habla en cada fuente, qué valora, un hecho general que conozcas del periodo y una pregunta para entender mejor.",
        "Fuente 1: un grupo que apoya la reforma agraria; valora que quienes trabajan la tierra la tengan. Fuente 2: un agricultor; valora su campo familiar. Hecho: se impulsó la reforma agraria en los años sesenta. Pregunta: ¿cómo se organizó el reparto de las tierras?",
        ["identifica quién habla y qué valora", "incluye un hecho comprobado", "formula una pregunta respetuosa"],
        ["una tabla de dos filas, un hecho y una pregunta"], ["tomar partido sin usar la fuente", "inventar hechos"],
        "Pregunta: «¿Esto es un hecho comprobado o una interpretación?»."),
    reinforce="Elige un hecho del cuaderno y una interpretación sobre ese hecho, y escribe cuál es cuál.",
    extend="Explica con tus palabras por qué un hecho comprobado y una valoración no tienen el mismo peso en una explicación.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Glosario escrito para este cuaderno con definiciones generales. "
      "Democracia: sistema en que la ciudadanía elige a sus autoridades en elecciones libres y se respetan los derechos. "
      "Golpe de Estado: toma del poder por la fuerza, fuera de las vías legales. "
      "Junta Militar: órgano de gobierno formado por los comandantes de las Fuerzas Armadas y de Orden tras el golpe de 1973. "
      "Derechos humanos: derechos que corresponden a toda persona, como la vida, la integridad y la libertad. "
      "Detenido desaparecido: persona detenida por agentes del Estado cuyo paradero no ha sido informado. "
      "Exilio: salida forzada o por riesgo del propio país. "
      "Transición: paso de la dictadura a la democracia. "
      "Memoria: modo en que una sociedad recuerda su pasado.")
build(
    O, 2, F2,
    use="Hoy aprendo el vocabulario preciso para hablar de la democracia, la dictadura, la transición y los derechos humanos con rigor y respeto.",
    prior=["Sé qué es una perspectiva.", "Distingo hecho de interpretación.", "Conozco el orden de los hechos entre 1964 y 1990."],
    explain=[
        "Para contrastar perspectivas hace falta usar bien las palabras. La democracia es el sistema en que la ciudadanía elige a sus autoridades en elecciones libres y se respetan los derechos. Un golpe de Estado es tomar el poder por la fuerza, fuera de las vías legales. Eso ocurrió el 11 de septiembre de 1973.",
        "Después del golpe gobernó una Junta Militar y luego el régimen encabezado por Augusto Pinochet hasta 1990. Los derechos humanos son los que corresponden a toda persona, como la vida, la integridad y la libertad. Informes oficiales establecieron que hubo detenciones, torturas, ejecuciones y casos de detenidos desaparecidos, es decir, personas detenidas por agentes del Estado cuyo paradero no se informó.",
        "La transición fue el paso de la dictadura a la democracia, y la memoria es la manera en que una sociedad recuerda lo ocurrido. Las perspectivas pueden diferir en cómo explicar y recordar, pero eso no cambia lo establecido por las fuentes oficiales.",
    ],
    vocab=[("golpe de Estado", "toma del poder por la fuerza, fuera de las vías legales"), ("Junta Militar", "órgano de gobierno formado por los comandantes de las Fuerzas Armadas y de Orden"), ("derechos humanos", "derechos de toda persona, como la vida, la integridad y la libertad"), ("detenido desaparecido", "persona detenida por agentes del Estado cuyo paradero no se ha informado"), ("transición", "paso de una dictadura a la democracia")],
    worked=[
        ("Aplicar un término", "{F} ¿Cómo se llama la toma del poder por la fuerza, fuera de las vías legales?", ["La ficha define el término en su glosario.", "Esa definición corresponde a golpe de Estado."], "Golpe de Estado"),
        ("Distinguir términos", "{F} ¿Qué diferencia hay entre transición y memoria?", ["La transición es el paso de la dictadura a la democracia.", "La memoria es el modo en que una sociedad recuerda su pasado."], "La transición es el paso político; la memoria es cómo se recuerda"),
    ],
    mistakes=[("Usar «golpe» y «transición» como si fueran sinónimos.", "Son hechos distintos: uno rompió la democracia y el otro la restituyó.", "Revisa la definición de cada término en el glosario."),
              ("Decir «desaparecido» para cualquier persona que no aparece.", "El término tiene un significado preciso: detención por agentes del Estado y paradero no informado.", "Usa el término solo con esa definición.")],
    T=[
        ("abc", "{F} ¿Qué es la democracia, según el glosario?", "Un sistema en que la ciudadanía elige a sus autoridades en elecciones libres y se respetan los derechos", "Un gobierno que no pide opinión", "Una votación de un día", "Así lo define el glosario de la ficha."),
        ("abc", "{F} ¿Qué es la Junta Militar?", "Un órgano de gobierno de los comandantes de las Fuerzas Armadas y de Orden", "Un partido político", "Una ley", "Así se define en la ficha."),
        ("ab", "{F} ¿Qué es el exilio?", "La salida forzada o por riesgo del propio país", "Un viaje de vacaciones", "El glosario lo define con esas palabras."),
        ("abc", "{F} ¿Qué es un detenido desaparecido?", "Una persona detenida por agentes del Estado cuyo paradero no se ha informado", "Cualquier persona que pierde el contacto con su familia", "Una persona que decide irse", "La definición es precisa en la ficha."),
        ("ab", "{F} ¿Qué es la transición?", "El paso de la dictadura a la democracia", "Un cambio de moneda", "La ficha la define como paso de un régimen a otro."),
        ("abc", "{F} ¿Qué son los derechos humanos?", "Derechos que corresponden a toda persona, como la vida y la libertad", "Derechos solo de los adultos", "Reglas de una empresa", "Valen para toda persona sin condiciones."),
        ("=", "El plebiscito fue en 1988 y asumió un gobierno elegido en 1990. ¿Cuántos años pasaron entre ambos hechos?", "1990-1988", "Se restan los dos años.", " años"),
        ("abc", "Una noticia de ejemplo dice: «Una persona se mudó de país para estudiar». ¿Es un caso de exilio según el glosario?", "No, porque el exilio es salida forzada o por riesgo", "Sí, siempre", "Depende del aeropuerto", "El exilio exige obligación o riesgo."),
        ("abc", "Un texto de ejemplo dice: «Una persona fue detenida por agentes del Estado y no se informó su paradero». ¿Qué categoría corresponde?", "Detenido desaparecido", "Exiliado", "Votante", "El caso cumple la definición del glosario de la ficha."),
        ("abc", "Una persona dice: «Tomar el poder por votación libre también es golpe de Estado». ¿Qué falla?", "Una votación libre es una vía legal y el golpe es por la fuerza", "Nada falla", "El golpe es siempre una votación", "El golpe ocurre fuera de las vías legales."),
        ("ab", "¿Qué función tiene la memoria de una sociedad?", "Mostrar cómo se recuerda el pasado y qué lecciones se sacan", "Cambiar las fechas", "La memoria incide en cómo se enseña y se recuerda lo vivido."),
        ("abc", "¿Cuál afirmación es correcta?", "La transición ocurrió después de la dictadura", "La transición ocurrió antes del golpe", "El exilio y el plebiscito son lo mismo", "La transición pasó de la dictadura a la democracia."),
        ("abc", "¿Qué convendría hacer ante dos personas que usan «desaparecido» con significados distintos?", "Volver a la definición del glosario y usarla igual", "Prohibir el término", "Cada una usa el suyo", "Un vocabulario común permite conversar con precisión."),
    ],
    ctx=("abc", "En una charla de una biblioteca de barrio, alguien usa «transición» para hablar del golpe de 1973. El facilitador propone revisar el glosario. ¿Por qué ayuda esa propuesta?", "Porque asegura que todos usen las palabras con el mismo significado", "Porque evita la discusión para siempre", "Porque cambia los hechos", "Un vocabulario común evita malentendidos al conversar sobre el tema."),
    sc=[("¿Qué es un golpe de Estado?", "La toma del poder por la fuerza, fuera de las vías legales", "El golpe rompe el orden institucional y legal del país."),
        ("En HGCS: ¿Qué son los derechos humanos?", "Derechos de toda persona, como la vida y la integridad", "Estos derechos valen para todas las personas sin excepción."),
        ("En HGCS: ¿qué es la transición?", "El paso de la dictadura a la democracia", "Marca el regreso a gobiernos elegidos.")],
    op=("Ficha de ejemplo: «Frase 1: En 1973 una persona partió fuera del país porque su vida estaba en riesgo. Frase 2: En 1988 la ciudadanía votó en un plebiscito. Frase 3: Una comisión oficial recogió casos de personas detenidas cuyo paradero no se informó.» "
        "Escribe qué término del glosario corresponde a cada frase y define en tus palabras uno de ellos.",
        "Frase 1: exilio. Frase 2: plebiscito. Frase 3: detenidos desaparecidos. Definición: plebiscito es una votación en que se responde sí o no a una pregunta.",
        ["asocia cada frase con un término correcto", "define con sus palabras", "usa lenguaje respetuoso"],
        ["una lista de tres términos y una definición"], ["usar términos fuera de su definición", "trivializar un hecho"],
        "Pregunta: «¿Este término se ajusta a la definición del glosario?»."),
    reinforce="Elige dos palabras del glosario y escribe una frase con cada una, sin referir a personas reales.",
    extend="Explica por qué usar un término con precisión es una forma de respeto hacia las personas afectadas.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Pregunta: «¿Por qué se quebró la democracia en Chile en 1973?» Hecho comprobado: el 11 de septiembre de 1973 las Fuerzas Armadas y de Orden derrocaron al gobierno. Cuatro textos inventados. "
      "A) Discurso de un dirigente de gobierno (de ejemplo, 1972): «Estamos ampliando derechos para trabajadores y campesinos, y hay sectores que quieren impedirlo.» "
      "B) Editorial de un diario de oposición (de ejemplo, 1973): «Hay escasez, inflación y paros; el país vive una crisis que el gobierno no resuelve.» "
      "C) Relato de una vecina (de ejemplo): «En mi población había tensión; unos y otros desconfiaban, y yo solo quería que se conversara.» "
      "D) Artículo de una historiadora (de ejemplo, escrito décadas después): «Hubo polarización política, crisis económica, un contexto internacional de Guerra Fría y decisiones de actores políticos y militares; los historiadores discuten el peso de cada causa.»")
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a contrastar perspectivas sobre el quiebre de la democracia separando hechos, causas y valoraciones.",
    prior=["Distingo hecho de interpretación.", "Conozco el vocabulario del periodo.", "Sé que cada fuente tiene un autor y un contexto."],
    explain=[
        "Para contrastar perspectivas sobre un conflicto sigue estos pasos. Paso 1: anota el hecho comprobado. Paso 2: identifica quién habla y cuándo escribe. Paso 3: señala qué causas o responsabilidades atribuye cada fuente. Paso 4: observa qué valora o teme. Paso 5: clasifica las causas por dimensión (política, económica, social, internacional). Paso 6: escribe una conclusión que reconozca las distintas miradas.",
        "En el caso del quiebre de la democracia hay un hecho comprobado y varias interpretaciones sobre sus causas. Un dirigente de gobierno destaca la ampliación de derechos y la resistencia de otros sectores; un diario de oposición destaca la crisis económica; una vecina muestra la desconfianza social; y una historiadora combina varias causas.",
        "Contrastar no es repartir culpas con rapidez ni justificar una respuesta violenta o ilegal. Un conflicto político, por intenso que sea, no justifica la violación de los derechos humanos.",
    ],
    vocab=[("polarización", "división de la sociedad en dos bandos opuestos"), ("inflación", "alza general y sostenida de los precios"), ("responsabilidad", "parte que le corresponde a un actor en un hecho"), ("Guerra Fría", "rivalidad mundial de la época entre dos grandes bloques de países"), ("interpretación", "explicación que se da a un hecho")],
    worked=[
        ("Causa y dimensión", "{F} ¿Qué causa destaca B y de qué dimensión es?", ["B habla de escasez, inflación y paros.", "Son problemas de la economía y del trabajo."], "La crisis económica, dimensión económica"),
        ("Fuente primaria o secundaria", "{F} Clasifica el texto D.", ["Fue escrito décadas después por una historiadora.", "Un texto posterior que explica es secundario."], "Fuente secundaria"),
    ],
    mistakes=[("Elegir una sola causa y presentarla como «la» causa.", "Las fuentes muestran varias causas, y la historiadora lo dice expresamente.", "Anota todas las causas y su dimensión antes de concluir."),
              ("Tomar el temor de una persona como justificación de la violencia posterior.", "Un temor o un conflicto no justifica violar derechos humanos.", "Distingue explicar un hecho de justificarlo.")],
    T=[
        ("abc", "{F} ¿Cuál es el hecho comprobado de la ficha?", "Que el 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno", "Que el país estaba dividido en dos", "Que la inflación bajó", "Es el hecho con fecha incluido en la pregunta."),
        ("abc", "{F} ¿Quién escribe el texto D?", "Una historiadora, décadas después", "Un dirigente de gobierno", "Una vecina", "Se indica en su encabezado al comienzo del texto."),
        ("ab", "En HGCS: ¿qué es la inflación?", "El alza general y sostenida de los precios", "La baja de los precios", "La inflación encarece los productos y reduce lo que alcanza el dinero."),
        ("abc", "{F} ¿Qué destaca el texto A?", "La ampliación de derechos y la resistencia de otros sectores", "La escasez y los paros", "La cronología", "El dirigente lo dice con claridad en su discurso."),
        ("ab", "{F} ¿Qué tipo de medio publica el texto B?", "Un diario de oposición", "Un organismo del gobierno", "El texto B se presenta como editorial de un diario de oposición."),
        ("abc", "{F} ¿Qué muestra el relato C?", "La desconfianza y el deseo de conversar en una población", "Un reglamento", "Un discurso oficial", "Presenta una vivencia social de una población concreta."),
        ("abc", "{F} ¿Qué dice el texto D sobre el peso de cada causa?", "Que los historiadores lo discuten", "Que una sola causa lo explica todo", "Que ya está resuelto del todo", "El texto termina diciendo que se discute el peso de cada causa."),
        ("abc", "{F} ¿Qué dimensión representa «contexto de Guerra Fría»?", "La internacional y política", "La medioambiental", "La económica solamente", "Se refiere a la relación entre países y bloques."),
        ("abc", "{F} Una persona dice: «Con el texto B queda demostrado que el golpe era inevitable». ¿Qué falla?", "B muestra una perspectiva y no demuestra que fuera inevitable", "Nada falla", "B no habla de la economía", "Una perspectiva no prueba una necesidad histórica."),
        ("abc", "{F} ¿Qué diferencia hay entre explicar y justificar?", "Explicar es mostrar causas; justificar es decir que estuvo bien", "Es lo mismo", "Justificar es más breve", "Explicar un hecho no es aprobar lo ocurrido."),
        ("ab", "{F} ¿Qué texto es más útil para conocer cómo se vivió en una población?", "El relato C", "El texto B", "Es el testimonio de una vecina."),
        ("abc", "{F} ¿Cuál es una buena conclusión?", "Hay un hecho comprobado y varias causas que las fuentes destacan de manera distinta", "Hubo una sola causa", "Nada se sabe", "Une las fuentes con precisión y sin descartar ninguna."),
        ("abc", "{F} ¿Qué voz falta para completar la mirada?", "La de una persona que trabajaba en el campo o en una fábrica", "Otro diario de oposición idéntico", "Un listado de fechas", "Aporta otra experiencia social que completa la comparación."),
    ],
    ctx=("abc", "En un taller de la junta de vecinos se lee la ficha y una persona dice: «Si hubo crisis, entonces todo lo posterior fue necesario». ¿Cómo se responde con rigor?", "Una crisis explica parte de los hechos, pero no justifica la violencia ni las violaciones a los derechos humanos", "Tiene razón", "Es mejor no hablar", "Se distingue con claridad explicar de justificar lo ocurrido."),
    sc=[("¿Cuál es el primer paso para contrastar?", "Anotar el hecho comprobado", "Es el punto de partida compartido por todas las perspectivas."),
        ("En HGCS: ¿Qué es la polarización?", "La división de la sociedad en dos bandos opuestos", "La polarización dificulta el diálogo entre las partes."),
        ("¿Se pueden justificar los abusos por una crisis?", "No, un conflicto político no justifica violar derechos humanos", "Los derechos humanos valen siempre, en cualquier contexto.")],
    op=("Ficha de ejemplo: «Pregunta: ¿Por qué hubo tantas diferencias en la sociedad chilena en 1972? Fuente a) cartel de ejemplo: ‘Más derechos para los trabajadores’. Fuente b) carta de ejemplo de una comerciante: ‘Faltan productos y no sé cómo mantener mi local’. Fuente c) nota de ejemplo de una dirigente vecinal: ‘En las juntas discutíamos con pasión, pero queríamos resolver los problemas’.» "
        "Anota quién habla, qué causa señala, su dimensión y escribe una conclusión de tres líneas.",
        "a) grupo de trabajadores; derechos laborales; política y social. b) comerciante; escasez; económica. c) dirigente vecinal; participación y pasión en los debates; social y política. Conclusión: había distintos problemas y expectativas; ampliar derechos y escasez de productos coexistían.",
        ["identifica quién habla", "clasifica por dimensión", "escribe una conclusión sin justificar abusos"],
        ["una tabla de tres filas y una conclusión"], ["elegir una sola causa", "justificar violencia"],
        "Pregunta: «¿Estoy explicando o estoy justificando?»."),
    reinforce="Elige un conflicto de tu comunidad (por ejemplo, un cambio de normas) y escribe dos causas y una perspectiva.",
    extend="Explica por qué las fuentes secundarias ayudan a ordenar varias causas.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Entre 1973 y 1990 gobernó una dictadura militar. En 1980 se aprobó una nueva Constitución en un plebiscito, y en esos años se aplicaron reformas económicas de mercado. "
      "Informes oficiales y sentencias de tribunales establecieron que hubo detenciones, torturas, ejecuciones y detenidos desaparecidos. Tres textos inventados. "
      "A) Columna de un empresario (de ejemplo): «Se ordenó la economía y la inflación bajó; eso trajo estabilidad a mi negocio.» "
      "B) Declaración de una agrupación de familiares (de ejemplo): «Hubo detenciones, torturas y desapariciones; exigimos verdad, justicia y que nunca se repita.» "
      "C) Relato de una persona exiliada (de ejemplo): «Perdí mi trabajo y salí del país con mi familia; extrañé mi barrio durante años.»")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo contrastar perspectivas sobre la dictadura separando hechos comprobados, valoraciones económicas y experiencias personales.",
    prior=["Uso los seis pasos para contrastar.", "Conozco el glosario.", "Sé que explicar no es justificar."],
    explain=[
        "Durante la dictadura (1973-1990) hubo cambios económicos, políticos y sociales profundos. Se aplicaron reformas de mercado, se aprobó una nueva Constitución en 1980 y se restringieron libertades. Al mismo tiempo, informes oficiales y sentencias judiciales establecieron graves violaciones a los derechos humanos.",
        "Las perspectivas sobre esos años son distintas. Algunas personas valoran la estabilidad económica que percibieron; otras destacan el dolor de las familias de detenidos desaparecidos; otras relatan el exilio y la pérdida del trabajo. Todas las miradas se anotan, pero no todas las afirmaciones tienen el mismo respaldo en los hechos.",
        "Contrastar bien es distinguir qué se comprueba (leyes, cifras de documentos, hechos judicialmente establecidos) de qué se valora («fue bueno», «fue injusto»). Una valoración económica no borra las violaciones a los derechos humanos, ni estas anulan la experiencia de quien percibió estabilidad. Se mantienen separadas para comprender.",
    ],
    vocab=[("estabilidad económica", "situación en que los precios y los ingresos cambian poco"), ("reforma", "cambio importante en una ley o en un sistema"), ("sentencia", "decisión final de un tribunal"), ("agrupación", "grupo organizado de personas con un fin común"), ("valoración", "juicio sobre si algo fue bueno o malo")],
    worked=[
        ("Hecho o valoración", "{F} Clasifica la frase de A: «Se ordenó la economía y la inflación bajó».", ["Habla de un dato comprobable (inflación) y de una valoración («se ordenó»).", "Conviene separar la parte comprobable de la parte valorativa."], "Mezcla un dato comprobable con una valoración"),
        ("Respaldo de un hecho", "{F} ¿Qué respalda que hubo detenidos desaparecidos?", ["La ficha dice que informes oficiales y sentencias lo establecieron.", "Documentos oficiales y fallos judiciales son respaldo sólido."], "Informes oficiales y sentencias de tribunales"),
    ],
    mistakes=[("Poner en la misma balanza una opinión económica y las violaciones a los derechos humanos como si se anularan.", "Son planos distintos: lo económico se valora, los abusos están comprobados.", "Anota cada plano por separado y no uses uno para negar el otro."),
              ("Dudar de un hecho porque lo cuenta una agrupación de familiares.", "Ese hecho está respaldado por informes oficiales y sentencias, no solo por su relato.", "Revisa el respaldo documental, no solo quién lo dice.")],
    T=[
        ("abc", "{F} ¿Entre qué años gobernó la dictadura según la ficha?", "Entre 1973 y 1990", "Entre 1964 y 1970", "Entre 1988 y 1993", "La ficha lo dice en su primera frase explícita."),
        ("abc", "{F} ¿Qué se aprobó en 1980?", "Una nueva Constitución en un plebiscito", "Una reforma agraria", "El voto de las mujeres", "La ficha lo indica de forma explícita en su texto."),
        ("ab", "En HGCS: ¿qué es una sentencia?", "La decisión final de un tribunal", "Un discurso", "Una sentencia resuelve un caso judicial."),
        ("abc", "{F} ¿Qué valora el texto A?", "La estabilidad económica", "La justicia", "El exilio", "El texto lo dice de forma explícita en su frase."),
        ("ab", "{F} ¿Qué exige la agrupación del texto B?", "Verdad, justicia y que nunca se repita", "Más inflación", "El texto lo dice con esas mismas palabras."),
        ("abc", "{F} ¿Qué cuenta el texto C?", "La pérdida del trabajo y el exilio de una persona y su familia", "Una reforma económica", "Un plebiscito", "Es un relato de exilio de una persona de ejemplo."),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1980 y el fin de la dictadura en 1990?", "1990-1980", "Se restan los dos años.", " años"),
        ("abc", "{F} ¿Qué respaldo da la ficha a la frase de A «la inflación bajó»?", "Ninguno: habría que buscar datos oficiales de precios", "Las sentencias de tribunales", "El relato del texto C", "La ficha respalda con documentos lo del texto B; lo de A necesita otros datos."),
        ("abc", "{F} Una persona dice: «Como A habla de estabilidad, B exagera». ¿Qué falla?", "Mezcla una valoración económica con hechos comprobados por otros medios", "Nada falla", "B no tiene respaldo", "Los hechos de B tienen respaldo documental."),
        ("abc", "{F} Otra persona dice: «Como B denuncia abusos, A miente». ¿Qué respuesta es más exacta?", "A expresa una experiencia de estabilidad; eso no anula lo denunciado en B", "A debe descartarse", "B no sirve", "Son planos distintos que se registran por separado."),
        ("ab", "{F} ¿Qué texto muestra una consecuencia social personal?", "El texto C", "El texto A", "Habla de pérdida del trabajo y exilio."),
        ("abc", "{F} ¿Cuál es una buena síntesis?", "Hubo cambios económicos y políticos; algunos valoraron la estabilidad, y se comprobaron graves violaciones a los derechos humanos", "Todo fue bueno", "Nada de eso se comprobó", "Reúne planos sin que uno anule el otro."),
        ("abc", "{F} ¿Qué pregunta ayuda a evaluar si una afirmación tiene respaldo?", "¿Qué documento o sentencia la respalda?", "¿Quién grita más fuerte?", "¿Cuántas palabras usa?", "La pregunta busca evidencia verificable que respalde el dato."),
    ],
    ctx=("abc", "En un taller de la biblioteca una persona dice que «en esa época se vivía tranquilo» y otra menciona que hubo personas que no volvieron. El facilitador propone anotar ambas frases en una tabla. ¿Qué criterio usa?", "Registrar cada perspectiva sin que una borre la otra y apoyarse en los hechos comprobados", "Descartar a una de las dos personas", "Cambiar de tema siempre", "Se escucha con respeto y se contrasta con evidencia."),
    sc=[("¿Qué se comprueba con informes y sentencias?", "Las violaciones a los derechos humanos", "Son documentos oficiales que respaldan los hechos."),
        ("¿Qué es una valoración?", "Un juicio sobre si algo fue bueno o malo", "Es un juicio y no es un dato comprobable."),
        ("¿Una valoración económica anula los abusos comprobados?", "No, son planos distintos", "Cada plano se evalúa con su propia evidencia.")],
    op=("Ficha de ejemplo: «Fuente 1 (nota de un comerciante, de ejemplo): ‘Mi negocio creció en esos años’. Fuente 2 (relato de una persona detenida y liberada, de ejemplo): ‘Viví miedo y violencia; aún me cuesta hablar’. Fuente 3 (declaración de una agrupación, de ejemplo): ‘Queremos saber qué pasó con nuestros familiares’.» "
        "Haz una tabla con quién habla, qué valora y qué respaldo tiene, y escribe una frase que reúna las tres sin que una anule a otra.",
        "1: comerciante; valora su negocio; respaldo: su experiencia. 2: persona detenida y liberada; destaca el miedo y la violencia vividos; respaldo: su relato, coherente con lo establecido por informes y sentencias. 3: agrupación; valora la verdad; respaldo: informes. Frase: hubo experiencias de crecimiento económico y también violencia comprobada; cada una requiere su evidencia.",
        ["completa la tabla con datos del texto", "separa planos sin anularlos", "usa lenguaje respetuoso"],
        ["una tabla de tres filas y una frase"], ["tomar un texto como falso", "trivializar el sufrimiento"],
        "Pregunta: «¿Qué respaldo tiene cada afirmación?»."),
    reinforce="Escribe una frase en que separes una valoración y un hecho comprobado sobre un cambio que conozcas.",
    extend="Explica por qué respetar a quien relata una experiencia no implica aceptar cualquier afirmación sin evidencia.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). Hechos generales sobre la transición: en 1988 se realizó un plebiscito sobre la continuidad del régimen y ganó la opción «No»; en 1989 se eligió presidente y en marzo de 1990 asumió un gobierno elegido; "
      "se crearon comisiones oficiales para investigar violaciones a los derechos humanos: la Comisión Nacional de Verdad y Reconciliación (informe de 1991, llamado Informe Rettig) y la Comisión sobre Prisión Política y Tortura (informe de 2004, llamado Informe Valech). Tres textos inventados. "
      "A) Declaración de una agrupación de familiares (de ejemplo): «Verdad y justicia: queremos saber dónde están y que haya responsables.» "
      "B) Columna de un analista (de ejemplo): «Hay que consolidar la democracia mirando hacia adelante y evitando nuevos enfrentamientos.» "
      "C) Artículo de una historiadora (de ejemplo): «La transición combinó negociaciones y cambios graduales; las discusiones sobre justicia, memoria y reparación continúan hasta hoy.»")
build(
    O, 5, F5,
    use="Hoy aplico el contraste de perspectivas a la transición y a los derechos humanos, comparando posturas sobre cómo tratar el pasado.",
    prior=["Uso los pasos para contrastar.", "Separo hechos de valoraciones.", "Conozco los términos del glosario."],
    explain=[
        "La transición fue el paso de la dictadura a la democracia. En 1988 un plebiscito decidió que no continuara el régimen, en 1989 se eligió presidente y en 1990 asumió un gobierno elegido por la ciudadanía. Después se crearon comisiones oficiales que investigaron violaciones a los derechos humanos y publicaron informes.",
        "Sobre cómo tratar el pasado hay perspectivas distintas. Algunas agrupaciones exigen verdad, justicia y reparación; algunos analistas proponen mirar hacia adelante para consolidar la democracia; las historiadoras explican que la transición fue gradual y que el debate continúa. No se discute si hubo violaciones, porque están establecidas; se discute cómo hacer justicia, reparar y recordar.",
        "Contrastar estas perspectivas significa preguntarse qué valora cada una (justicia, estabilidad, memoria), qué riesgos ve y qué pide al Estado. Así se entiende mejor un debate social sin perder respeto por las víctimas.",
    ],
    vocab=[("reparación", "acciones para reconocer el daño y apoyar a las víctimas y sus familias"), ("verdad", "conocer lo que realmente ocurrió"), ("justicia", "que haya responsables y se apliquen las sanciones que corresponden"), ("garantías de no repetición", "medidas para que los hechos no vuelvan a ocurrir"), ("gradual", "que ocurre por etapas, de a poco")],
    worked=[
        ("Qué valora cada texto", "{F} ¿Qué valora el texto B?", ["Habla de consolidar la democracia y evitar enfrentamientos.", "Valora la estabilidad y la mirada hacia adelante."], "La estabilidad democrática y mirar hacia adelante"),
        ("Cómo se relacionan", "{F} ¿En qué se diferencian A y B?", ["A pide verdad y justicia sobre el pasado.", "B pone el acento en el futuro y en evitar enfrentamientos."], "A prioriza la verdad y la justicia; B, la estabilidad hacia el futuro"),
    ],
    mistakes=[("Creer que mirar hacia adelante significa negar que hubo violaciones.", "Una postura sobre qué hacer no cambia lo establecido por los informes.", "Distingue lo comprobado (los hechos) de la propuesta (qué hacer)."),
              ("Decir que «los dos tienen razón» sin precisar en qué.", "Se pierde el análisis de lo que cada perspectiva valora.", "Explica qué valora cada una y qué deja de lado.")],
    T=[
        ("abc", "{F} ¿Qué ocurrió en 1988 según la ficha?", "Un plebiscito sobre la continuidad del régimen", "Una elección municipal", "Un golpe de Estado", "La ficha lo indica de forma explícita en su texto."),
        ("abc", "{F} ¿Cuándo asumió un gobierno elegido?", "En marzo de 1990", "En 1973", "En 1980", "La ficha lo menciona de forma explícita en su texto."),
        ("ab", "En HGCS: ¿qué es la reparación?", "Acciones para reconocer el daño y apoyar a las víctimas", "Una nueva Constitución", "La reparación busca reconocer el daño y apoyar a las víctimas y sus familias."),
        ("abc", "{F} ¿Qué informe de 1991 se menciona?", "El Informe Rettig", "El Informe Valech", "La Constitución", "La ficha lo indica de forma explícita en su texto."),
        ("abc", "{F} ¿Qué informe de 2004 se menciona?", "El Informe Valech", "El Informe Rettig", "El plebiscito", "Se refiere a prisión política y tortura."),
        ("ab", "{F} ¿Qué pide el texto A?", "Verdad y justicia", "Más inflación", "La agrupación lo dice en su declaración."),
        ("=", "{F} ¿Cuántos años hay entre el Informe Rettig (1991) y el Informe Valech (2004)?", "2004-1991", "Se restan los años para ver el tiempo entre los informes.", " años"),
        ("abc", "{F} ¿Qué dimensión del proceso destaca el texto C?", "La política y la social", "La medioambiental", "La económica solamente", "Habla de negociaciones, justicia y memoria."),
        ("abc", "{F} Una persona dice: «Como B pide mirar adelante, niega los hechos». ¿Qué respuesta es más exacta?", "B propone una forma de actuar; no dice que los hechos no ocurrieron", "Tiene razón, los niega", "B no tiene perspectiva", "Se debe leer lo que el texto dice."),
        ("abc", "{F} Otra persona dice: «Como A pide justicia, no quiere la democracia». ¿Qué falla?", "Pedir justicia sobre el pasado es compatible con la democracia", "Nada falla", "A no existe", "Pedir justicia es compatible con vivir en democracia."),
        ("ab", "{F} ¿Qué texto muestra que el debate continúa hasta hoy?", "El texto C", "El texto B", "La historiadora lo afirma en su artículo de ejemplo."),
        ("abc", "{F} ¿Cuál es una buena síntesis?", "Hubo plebiscito, elecciones y comisiones; hay perspectivas que priorizan la justicia y otras la estabilidad", "No hubo debate", "Solo importa el texto B", "Reúne los hechos y las posturas sin descartar ninguna."),
        ("abc", "{F} ¿Qué pregunta ayuda a contrastar A y B?", "¿Qué valora cada una y qué riesgo ve en la otra?", "¿Quién escribe más largo?", "¿Quién es más famoso?", "La pregunta busca los valores y los riesgos de cada postura."),
    ],
    ctx=("abc", "En una asamblea comunitaria dos vecinos discuten: uno pide recordar y reparar, otro prefiere no remover el pasado. La moderadora pide que cada uno explique qué valora. ¿Qué logra con esa petición?", "Entender las posturas sin imponer una y sin negar los hechos", "Callar a ambos", "Elegir al ganador", "Preguntar por valores aclara las diferencias."),
    sc=[("¿Qué ocurrió en el plebiscito de 1988?", "Ganó la opción «No» a la continuidad del régimen", "Ese resultado abrió el camino a elecciones libres."),
        ("¿Qué es la verdad en este debate?", "Conocer lo que realmente ocurrió", "Es parte de lo que piden las agrupaciones."),
        ("¿Se discute si hubo violaciones a los derechos humanos?", "No, están establecidas; se discute cómo hacer justicia y recordar", "Informes oficiales y sentencias las establecieron con claridad.")],
    op=("Ficha de ejemplo: «Posición 1 (de ejemplo): ‘Hay que recordar y reparar para que no se repita’. Posición 2 (de ejemplo): ‘Hay que enfocarse en el desarrollo y no remover el pasado’. Posición 3 (de ejemplo): ‘Se puede recordar y a la vez mirar hacia adelante’.» "
        "Anota qué valora cada posición, qué riesgo ve y escribe tu síntesis de tres líneas sin justificar abusos ni descalificar a nadie.",
        "1: valora la memoria y la reparación; teme el olvido. 2: valora el desarrollo; teme la división. 3: valora ambas; teme que se opongan. Síntesis: las tres posiciones coinciden en querer una sociedad estable; se diferencian en cómo tratar el pasado.",
        ["identifica valores y riesgos", "no descalifica", "hace una síntesis respetuosa"],
        ["una tabla de tres filas y una síntesis"], ["descalificar a quien piensa distinto", "negar hechos comprobados"],
        "Pregunta: «¿Qué valora esta posición y qué riesgo ve?»."),
    reinforce="Escribe una frase en que reconozcas un valor de una postura con la que no coincides.",
    extend="Explica por qué la memoria, la verdad y la justicia suelen discutirse juntas en la transición.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Criterios de un contraste respetuoso: 1) parte de hechos comprobados; 2) atribuye cada afirmación a quien la dice; 3) reconoce al menos dos causas; 4) no justifica violaciones a los derechos humanos; 5) deja una pregunta abierta. "
      "Tres borradores inventados de estudiantes sobre el quiebre y la dictadura. "
      "Borrador 1: «El golpe fue inevitable porque había crisis.» "
      "Borrador 2: «Según un editorial, había escasez; según un discurso, se ampliaban derechos; la historiadora dice que hubo varias causas.» "
      "Borrador 3: «Todo lo que pasó en la dictadura es mentira o exageración.»")
build(
    O, 6, F6,
    use="Hoy evalúo contrastes sobre los conflictos internos, aplico criterios y decido cómo seguir aprendiendo con respeto y rigor.",
    prior=["Uso pasos para contrastar.", "Distingo explicar de justificar.", "Conozco los hechos comprobados del periodo."],
    explain=[
        "Evaluar un contraste es comprobar si cumple criterios. Un contraste respetuoso parte de hechos comprobados, atribuye cada afirmación a su autor, reconoce al menos dos causas, no justifica violaciones a los derechos humanos y deja preguntas abiertas para seguir investigando.",
        "Un borrador que afirma una sola causa y dice que algo fue «inevitable» simplifica; uno que niega hechos comprobados no respeta la evidencia; uno que atribuye cada idea a su fuente y reconoce varias causas está mejor encaminado. Evaluar con criterios evita decidir por simpatía.",
        "Al cerrar, decide un paso siguiente: buscar otra fuente, escribir una pregunta abierta o explicar a otra persona tu contraste. Evaluar fenómenos con apertura a distintas perspectivas y contextos es parte de pensar críticamente.",
    ],
    vocab=[("inevitable", "que no podía ser de otra manera"), ("atribuir", "indicar quién dijo o hizo algo"), ("simplificar", "reducir un proceso complejo a una sola causa"), ("negacionismo", "negar hechos comprobados"), ("apertura", "disposición a considerar otras perspectivas")],
    worked=[
        ("Evaluar un borrador", "{F} ¿Cumple el borrador 1 el criterio 3 (al menos dos causas)?", ["El borrador 1 menciona solo una crisis.", "No reconoce otras causas."], "No cumple: nombra una sola causa"),
        ("Mejorar una frase", "{F} Reescribe el borrador 3 para que respete la evidencia.", ["El borrador 3 niega hechos comprobados.", "Una frase respetuosa distingue lo comprobado de lo que se discute."], "Los informes oficiales y las sentencias establecen violaciones a los derechos humanos; lo que se discute son las causas y la memoria"),
    ],
    mistakes=[("Corregir un borrador solo por su estilo.", "El problema de fondo puede estar en una sola causa o en negar hechos.", "Revisa primero los cinco criterios."),
              ("Aceptar «inevitable» como explicación.", "Esa palabra cierra el análisis y quita responsabilidad a los actores.", "Pregunta qué decisiones y alternativas había.")],
    T=[
        ("abc", "{F} ¿Cuántos criterios hay en la ficha?", "Cinco", "Tres", "Siete", "La ficha numera de 1 a 5."),
        ("abc", "{F} ¿Qué afirma el borrador 1?", "Que el golpe fue inevitable porque había crisis", "Que hubo varias causas", "Que todo es mentira", "Es la frase que aparece escrita en el borrador."),
        ("ab", "En HGCS: ¿qué es simplificar un proceso?", "Reducirlo a una sola causa", "Estudiarlo con varias causas", "Simplificar deja afuera la complejidad del proceso."),
        ("abc", "{F} ¿Qué criterio cumple bien el borrador 2?", "Atribuye cada afirmación a quien la dice", "Niega los hechos", "Justifica abusos", "Menciona editorial, discurso e historiadora como fuentes."),
        ("ab", "{F} ¿Qué falla tiene el borrador 3?", "Niega hechos comprobados", "Atribuye cada idea", "Dice que todo es mentira, contra la evidencia."),
        ("abc", "{F} ¿Qué pasa con el criterio 2 en el borrador 1?", "No atribuye la afirmación a ninguna fuente ni persona", "Atribuye cada dato a un documento", "Cita tres fuentes distintas", "El borrador 1 afirma sin decir quién lo dice."),
        ("=", "{F} Si un contraste cumple 3 de los 5 criterios de la ficha, ¿cuántos criterios le faltan por cumplir?", "5-3", "Se resta los criterios cumplidos del total de criterios.", " criterios"),
        ("abc", "{F} ¿Cómo se mejora el borrador 1?", "Agregando otras causas y evitando decir «inevitable»", "Añadiendo adjetivos", "Dejándolo igual", "Responde a los criterios 3 y 4."),
        ("abc", "{F} Una persona dice: «El borrador 2 es perfecto». ¿Qué le falta?", "Una pregunta abierta y el hecho comprobado de partida", "Nada", "Más fechas sin contexto", "Cumple varios criterios, pero faltan el 1 y el 5."),
        ("abc", "¿Qué es el negacionismo?", "Negar hechos que están comprobados", "Criticar una política", "Hacer una pregunta", "Contradice la evidencia documental que existe."),
        ("ab", "¿Qué diferencia hay entre criticar una política y negar un hecho comprobado?", "Criticar es opinar; negar es rechazar evidencia", "Es lo mismo", "Una crítica se basa en razones; el negacionismo contradice la evidencia."),
        ("abc", "{F} ¿Cuál sería un buen cierre para el borrador 2?", "Pregunta abierta: ¿qué vivieron las personas del campo en esos años?", "Todo está claro", "No hay más preguntas", "Una pregunta final abre la investigación hacia otras fuentes."),
        ("abc", "{F} Para evaluar con apertura a distintas perspectivas, ¿qué conviene?", "Escuchar al menos dos miradas y pedir evidencia a cada una", "Aceptar solo la que gusta", "No discutir nunca", "La apertura incluye contraste con evidencia."),
    ],
    ctx=("abc", "En un taller, una persona propone una regla para conversar sobre estos años: «cada afirmación con su fuente y sin justificar violencia». ¿Qué criterios cumple esa regla?", "Atribuir cada afirmación y no justificar violaciones a los derechos humanos", "Ninguno", "Solo el de causas", "Combina los criterios 2 y 4."),
    sc=[("¿Qué debe hacer un contraste respetuoso?", "Partir de hechos, atribuir y no justificar abusos", "Son los criterios que propone el cuaderno."),
        ("¿Qué es el negacionismo?", "Negar hechos que están comprobados", "Contradice informes oficiales y sentencias de tribunales."),
        ("¿Para qué dejar una pregunta abierta?", "Para seguir investigando con otras fuentes", "Ninguna explicación es definitiva y siempre se puede ampliar.")],
    op=("Elige uno de los temas del módulo (quiebre de la democracia, dictadura o transición) y escribe un contraste de 8 líneas con: un hecho comprobado, dos perspectivas atribuidas a su fuente de ejemplo, dos causas y una pregunta abierta. "
        "Evalúalo con los cinco criterios de la ficha y anota qué mejorarías.",
        "Tema: transición. Hecho: en 1988 hubo un plebiscito. Perspectivas: una agrupación pide verdad y justicia; un analista pide mirar hacia adelante. Causas: negociaciones y presión social. Pregunta: ¿cómo se pueden reparar daños sin dividir? Evaluación: cumple 1, 2, 3, 5; mejoro el 4 explicitando que los hechos están establecidos.",
        ["parte de un hecho comprobado", "atribuye a cada fuente", "no justifica violaciones a los derechos humanos"],
        ["un texto de ocho líneas y una autoevaluación"], ["negar hechos", "usar una sola causa"],
        "Pregunta: «¿Qué criterio me falta cumplir?»."),
    reinforce="Revisa un borrador tuyo de esta unidad con los cinco criterios y marca cuáles cumple.",
    extend="Explica a otra persona por qué no basta con elegir una perspectiva: hay que revisar su evidencia.",
)

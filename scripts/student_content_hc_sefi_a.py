"""Seminario de filosofía (electivo HC, 3.º y 4.º medio): OAC-01 (explicar textos filosóficos que abordan un problema de la historia de la filosofía, clases 1 a 4). Casos, autores y textos ficticios o «de ejemplo», escritos para este cuaderno."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada caso y cada texto está escrito en el enunciado. "
             "Los autores, las ciudades y los textos son ficticios o «de ejemplo»: sirven para practicar el razonamiento y no son citas de ninguna obra real. "
             "La lectura de textos filosóficos reales queda para tu docente. Las posturas se presentan con sus razones y sin tomar partido: tu tarea es entenderlas, compararlas y evaluarlas con argumentos. "
             "Si un caso te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O1 = "FI-SEFI-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso ficticio). En el liceo «Costa Alta» (no existe), Ilse y Mateo caminan por un camino de tierra en un día muy caluroso. A lo lejos ven en el suelo una mancha brillante, como un charco. "
     "Al llegar, el suelo está seco. Ilse dice: «Mis ojos me engañaron; ¿cómo sé que no me engañan siempre?». Mateo responde: «Esta vez me equivoqué, pero casi siempre lo que veo resulta cierto.»")
build(
    O1, 1, F,
    use="Aprenderé a reconocer un problema filosófico en una situación o en un texto y a preguntar por sus antecedentes, planteamientos, supuestos y contexto.",
    prior=["Distingo un hecho de una opinión.", "Sé que una tesis se defiende con razones.", "Sé formular una pregunta abierta."],
    explain=[
        "Un problema filosófico es una pregunta abierta y de fondo que reaparece en distintas épocas, porque sus conceptos centrales se discuten y las respuestas razonadas difieren. No es una pregunta de dato, que se responde midiendo o contando, ni un acertijo, que tiene una solución cerrada que se halla con ingenio. El problema del conocimiento, por ejemplo, pregunta qué podemos saber y con qué seguridad.",
        "Para explicar un texto filosófico se parte reconociendo qué problema aborda. Luego se buscan cuatro cosas. Los antecedentes son las discusiones previas a las que el texto responde. Los planteamientos son su tesis y sus razones. Los supuestos son ideas previas que el texto da por ciertas sin demostrarlas. El contexto sociocultural son las condiciones de su época y lugar: la ciencia disponible, las creencias comunes, las instituciones y quiénes podían escribir y leer.",
        "Problematizar es convertir una situación en una pregunta filosófica. Se detecta una tensión, que es un choque entre dos ideas razonables, se nombran los conceptos en juego y se formula una pregunta abierta. En la ficha, la tensión es que los sentidos a veces engañan, pero casi siempre guían bien.",
    ],
    vocab=[("problema filosófico", "pregunta abierta y de fondo que reaparece en distintas épocas porque sus conceptos se discuten"), ("pregunta de dato", "pregunta que se responde midiendo, contando o buscando información"), ("acertijo", "problema con una solución cerrada que se encuentra con ingenio"), ("tensión", "choque entre dos ideas razonables que no caben juntas sin más"), ("antecedente", "discusión previa a la que un texto responde"), ("supuesto", "idea previa que un texto da por cierta sin demostrarla"), ("contexto sociocultural", "condiciones de la época y del lugar en que se escribió un texto")],
    worked=[
        ("Clasificar una pregunta", "Sobre la ficha se pregunta: «¿A cuántos metros de distancia estaba la mancha brillante?». ¿Qué tipo de pregunta es?",
         ["Pregunto si se responde midiendo o contando: bastaría una medición.", "No hay conceptos disputados ni razones que evaluar."],
         "Es una pregunta de dato, no un problema filosófico"),
        ("Formular el problema", "Formula como pregunta filosófica la tensión de la ficha.",
         ["Nombro la tensión: los sentidos a veces engañan, pero casi siempre guían bien.", "Nombro los conceptos en juego: sentidos, seguridad y conocimiento; y hago la pregunta abierta."],
         "«¿Podemos confiar en los sentidos como fuente de conocimiento seguro, aunque a veces nos engañen?»"),
    ],
    mistakes=[("Creer que el problema es el fenómeno («el problema es el espejismo»).", "Se nombra un tema o un hecho, no una pregunta abierta con conceptos que discutir.", "Convierte el tema en una pregunta que use conceptos como conocimiento, seguridad o verdad."),
              ("Pensar que, como no hay una respuesta única, todo es opinión y da lo mismo.", "Se confunde un problema abierto con uno sin razones mejores o peores.", "Evalúa cada respuesta por sus razones y supuestos: unas están mejor fundadas que otras.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es un problema filosófico?", "Una pregunta abierta y de fondo que reaparece en distintas épocas porque sus conceptos se discuten", "Una pregunta que se resuelve con una medición precisa", "Una pregunta que nadie ha querido responder todavía", "Se caracteriza por conceptos disputados y respuestas razonadas distintas, no por falta de interés ni por una medición."),
        ("abc", "¿Qué tipo de pregunta es «¿Cuántos grados marcó el termómetro del patio a mediodía?»?", "De dato, porque se responde midiendo", "Problema filosófico, porque trata del calor y todos lo sentimos", "Acertijo, porque la respuesta es un número que se calcula", "Se resuelve leyendo un instrumento y no exige discutir conceptos."),
        ("abc", "«Ana es mayor que Beto y Beto es mayor que Clara. ¿Quién es la menor?» ¿Qué tipo de pregunta es?", "Un acertijo, porque tiene una solución cerrada que se halla razonando", "Un problema filosófico, porque pide razonar", "Una pregunta de dato, porque hay que medir las edades", "Tiene una única solución que se deduce de lo dado, a diferencia de un problema abierto."),
        ("abc", "{F} ¿Cuál es la tensión de la ficha?", "Los sentidos a veces engañan, pero casi siempre guían bien", "El camino es largo y hace calor", "Ilse y Mateo no quieren caminar juntos", "La tensión es el choque entre la desconfianza que produce el engaño y la confianza que da el acierto habitual."),
        ("abc", "{F} ¿Quién muestra mayor desconfianza en los sentidos?", "Ilse, porque se pregunta si no la engañan siempre", "Mateo, porque dice que casi siempre acierta", "Ninguno de los dos, porque ambos creen ver un charco", "Ilse generaliza la duda a todos los casos y Mateo la limita a una vez."),
        ("ab", "Dos líneas parecen de distinto largo, pero al medirlas resultan iguales. ¿Cuál es la mejor formulación filosófica del problema que esto plantea?", "¿Qué razones hay para confiar en lo que percibimos si sabemos que puede producir ilusiones?", "¿Cuántos centímetros miden las dos líneas?", "La formulación filosófica es abierta y usa conceptos en disputa (razones, percepción); la otra pide solo un dato que se mide."),
        ("abc", "Un texto de ejemplo dice: «Antes de afirmar algo debo revisar si mis creencias tienen fundamento». ¿Qué problema aborda principalmente?", "El del conocimiento: qué justifica lo que creemos saber", "El de cómo repartir un trabajo en grupo", "El de cuál es el mejor camino para llegar a un lugar", "Examinar el fundamento de las creencias es preguntar qué hace que algo cuente como conocimiento."),
        ("abc", "Un texto ficticio responde a quienes sostenían que los sentidos bastan para saber. En la explicación de textos, ¿qué es esa discusión previa?", "El antecedente", "El supuesto", "El contexto sociocultural", "Los antecedentes son las discusiones previas a las que un texto responde."),
        ("abc", "«En la época del autor ficticio, los viajes largos traían objetos y relatos desconocidos que cuestionaban lo que antes se daba por sabido». ¿Qué parte de la explicación del texto aporta esta frase?", "El contexto sociocultural", "El planteamiento, porque es la tesis", "El supuesto, porque no está demostrado", "Describe condiciones de la época y del lugar en que se escribió el texto."),
        ("abc", "«El autor da por cierto que existe un mundo exterior, pero no lo demuestra». ¿Qué parte de la explicación del texto es esto?", "Un supuesto", "Un antecedente", "Un dato de contexto", "Una idea que el texto acepta sin demostrar es un supuesto."),
        ("abc", "Un estudiante propone como problema filosófico «los espejismos». ¿Por qué todavía no lo es?", "Nombra un fenómeno y no una pregunta abierta con conceptos que discutir", "Porque es un tema demasiado simple para preguntarse algo", "Porque los problemas filosóficos nunca parten de experiencias cotidianas", "Un tema o un hecho se vuelve problema filosófico cuando se formula como pregunta abierta con conceptos en disputa."),
        ("abc", "{F} Si Mateo hubiera visto charcos falsos todos los días, ¿qué ocurriría con la tensión?", "Pesaría más la desconfianza hacia los sentidos, cercana a la postura de Ilse", "Desaparecería, porque Mateo tendría razón siempre", "El problema dejaría de ser filosófico", "Con más engaños, la confianza basada en el acierto habitual se debilita y la duda de Ilse gana fuerza."),
        ("abc", "¿Por qué una encuesta no resuelve un problema filosófico?", "Porque la opinión de muchas personas no muestra por sí sola que haya buenas razones", "Porque una encuesta solo sirve para preguntas sobre ciencias", "Porque la respuesta más votada es siempre la verdadera", "Contar opiniones no examina razones; el problema se evalúa con argumentos y supuestos."),
    ],
    ctx=("abc", "Rocío recuerda haber dejado su mochila en la sala, pero la encontró en el pasillo. Se pregunta si puede fiarse de lo que recuerda. ¿Cuál de estas es una buena formulación filosófica del problema?", "¿Qué razones tenemos para confiar en la memoria como fuente de conocimiento?", "¿Cuántas mochilas hay en el pasillo del liceo?", "¿Dónde se guardan las mochilas que se pierden?", "Solo la primera es abierta, usa un concepto en disputa (conocimiento) y pide evaluar razones; las otras piden un dato."),
    sc=[
        ("En Seminario de filosofía: ¿qué son los antecedentes de un texto?", "Las discusiones previas a las que el texto responde", "Permiten ubicar el texto dentro de un debate y no como una idea suelta."),
        ("¿Qué cuatro cosas se buscan para explicar un texto filosófico?", "Antecedentes, planteamientos, supuestos y contexto sociocultural", "Son los cuatro ejes de la explicación de un texto en esta unidad."),
        ("¿Por qué «el espejismo» no es todavía un problema filosófico?", "Porque nombra un tema y no una pregunta abierta con conceptos en disputa", "Hay que transformarlo en una pregunta que se pueda discutir con razones."),
    ],
    op=("Elige una situación ficticia. Situación 1: Abril descubre que una noticia que creyó cierta era falsa y se pregunta cuándo debe creer lo que lee. Situación 2: dos compañeros recuerdan de modo distinto lo que pasó en una excursión y cada uno está seguro de su versión. "
        "Escribe: la tensión, los conceptos en juego, una pregunta filosófica abierta y qué buscarías en un texto sobre el tema para identificar antecedentes, supuestos y contexto.",
        "Situación 1. Tensión: creemos lo que leemos, pero a veces es falso. Conceptos: creencia, fuente y conocimiento. Pregunta: ¿qué hace confiable una fuente de información? Buscaría con qué discusiones previas dialoga, qué da por cierto sobre las fuentes y en qué época se escribió.",
        ["identifica una tensión entre dos ideas razonables", "nombra al menos dos conceptos en juego", "formula una pregunta abierta y no de dato", "indica qué buscaría para antecedentes, supuestos y contexto"],
        ["tensión, conceptos, pregunta y plan de lectura escritos sobre la situación elegida"],
        ["formular una pregunta que se responde con un dato", "nombrar el tema sin hacer una pregunta", "olvidar los conceptos en juego"],
        "Pregunta: «¿tu pregunta se podría responder solo midiendo o buscando un dato?». Si sí, pídele que agregue un concepto en disputa."),
    reinforce="Escribe tres preguntas sobre tu vida escolar: una de dato, un acertijo y un problema filosófico, y explica en una línea por qué cada una es de ese tipo.",
    extend="Elige una afirmación que escuches a diario («la experiencia enseña más que los libros») y escribe cuál es la tensión y qué problema filosófico hay detrás.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (de ejemplo). En un taller ficticio se proponen tres definiciones de «saber» algo. "
     "D1: «Saber es creer algo.» D2: «Saber es creer algo verdadero.» D3: «Saber es creer algo verdadero y tener buenas razones que lo justifiquen.» "
     "Caso X: Tomás decide con una moneda que mañana lloverá, y llueve. Caso Y: Paula revisa tres pronósticos confiables, cree que lloverá, y llueve. Caso Z: Eva está segura de que lloverá, pero se equivoca.")
build(
    O1, 2, F,
    use="Aprenderé a definir un concepto filosófico por sus rasgos y a probar la definición con casos, para entender lo que un texto quiere decir con él.",
    prior=["Sé qué es un problema filosófico.", "Sé buscar antecedentes y supuestos en un texto.", "Distingo ejemplo de contraejemplo."],
    explain=[
        "Definir un concepto filosófico no es copiar un diccionario, sino indicar qué rasgos debe tener algo para contar como ese concepto. Una condición necesaria es un rasgo sin el cual no hay concepto. Una condición suficiente es un conjunto de rasgos que, si se cumplen, bastan. Un texto filosófico casi siempre usa palabras comunes con un sentido preciso, y entenderlo exige reconstruir ese sentido.",
        "Una definición clásica de conocimiento dice que saber es tener una creencia verdadera y justificada. La creencia es aceptar algo como cierto. La verdad es que lo creído coincide con cómo son las cosas. La justificación son las buenas razones que apoyan lo creído. La certeza, en cambio, es sentirse completamente seguro, y puede darse sin que haya conocimiento: alguien puede estar muy seguro y equivocarse.",
        "Una definición se prueba con casos. Si deja entrar un caso que no debería, es demasiado amplia. Si deja fuera un caso que sí debería, es demasiado estrecha. Algunas posturas discuten incluso la definición clásica, porque piensan que una persona puede acertar por pura casualidad aunque tenga razones; por eso las definiciones filosóficas siguen discutiéndose.",
    ],
    vocab=[("condición necesaria", "rasgo sin el cual no hay concepto"), ("condición suficiente", "conjunto de rasgos que bastan para que algo cuente como el concepto"), ("creencia", "aceptar algo como cierto"), ("verdad", "coincidencia entre lo que se cree y cómo son las cosas"), ("justificación", "buenas razones que apoyan lo que se cree"), ("certeza", "sentirse completamente seguro de algo")],
    worked=[
        ("Aplicar la definición", "Según D3 de la ficha, ¿el Caso Z (Eva) es un caso de saber?",
         ["Reviso los tres rasgos: Eva cree que lloverá, así que hay creencia.", "Pero se equivoca: lo creído no es verdadero, y falta un rasgo."],
         "No: falta la verdad, aunque Eva tenga certeza"),
        ("Probar una definición", "¿Qué caso de la ficha muestra que D2 es demasiado amplia?",
         ["Busco un caso que cumpla D2 pero que no consideraríamos un saber.", "El caso X: Tomás cree algo verdadero, pero lo decidió con una moneda, sin razones."],
         "El Caso X: cumple D2 y, sin justificación, no parece saber; por eso D2 es amplia"),
    ],
    mistakes=[("Confundir certeza con conocimiento («si estoy muy seguro, entonces sé»).", "Se mide el saber por cómo uno se siente y no por la verdad y las razones.", "Pregunta si lo creído es verdadero y si hay razones que lo apoyen, además de sentirte seguro."),
              ("Probar una definición solo con los casos que la confirman.", "Los casos fáciles hacen que cualquier definición parezca buena.", "Busca un caso difícil, como un acierto por suerte o un error con certeza, antes de aceptarla.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es una condición necesaria de un concepto?", "Un rasgo sin el cual no hay concepto", "Un rasgo que basta para que haya concepto", "Un ejemplo que casi todos aceptan", "Es un rasgo imprescindible: si falta, el concepto no se aplica."),
        ("abc", "Según la explicación, ¿qué es la justificación?", "Las buenas razones que apoyan lo que se cree", "El sentirse completamente seguro", "La coincidencia entre lo que se cree y las cosas", "La justificación se refiere a las razones y no al sentimiento de seguridad."),
        ("abc", "{F} ¿Cuál de las definiciones coincide con la definición clásica de la explicación?", "D3", "D1", "D2", "D3 reúne creencia, verdad y justificación, los tres rasgos de la definición clásica."),
        ("abc", "{F} Según D3, ¿el Caso Y (Paula) es un caso de saber?", "Sí, porque cree algo verdadero y con buenas razones", "No, porque no está completamente segura", "No, porque llueve por casualidad", "Paula tiene creencia, verdad y justificación en tres pronósticos confiables."),
        ("abc", "{F} Según D3, ¿el Caso X (Tomás) es un caso de saber?", "No, porque falta la justificación", "Sí, porque lo creído resultó verdadero", "No, porque falta la creencia", "Cree algo y resulta verdadero, pero lo decidió con una moneda: no tiene razones."),
        ("ab", "{F} ¿Qué definición de la ficha es demasiado amplia, porque cuenta como saber cualquier cosa que se crea?", "D1", "D3", "Con D1 hasta una creencia falsa contaría como saber, así que deja entrar casos que no corresponden."),
        ("abc", "Un estudiante dice: «Estoy completamente seguro de que la reunión es a las 10, así que sé que es a las 10». La reunión es a las 11. ¿Qué responde la definición clásica?", "No sabe: tiene certeza y creencia, pero lo creído es falso", "Sí sabe, porque está completamente seguro", "No tiene ninguna creencia sobre la reunión", "La certeza no basta: falta que lo creído sea verdadero."),
        ("abc", "Una persona cree algo verdadero por haber leído un resumen sin fuentes ni pruebas, y por suerte acierta. Según D3, ¿qué falta?", "Buenas razones que lo justifiquen", "Una creencia sobre el tema", "Que lo creído coincida con las cosas", "Acierta y cree, pero sin razones que lo apoyen no cumple el tercer rasgo."),
        ("abc", "¿Por qué la certeza no es una condición suficiente para saber?", "Porque se puede estar completamente seguro y equivocarse", "Porque nadie puede sentir certeza", "Porque la certeza se aprende en el colegio", "La certeza es un sentimiento y puede darse con una creencia falsa."),
        ("abc", "«Lucas ve su reloj, que está funcionando bien, y cree correctamente que son las 4.» Según D3, ¿cuántos de los tres rasgos cumple su creencia?", "Los tres: creencia, verdad y justificación", "Solo dos: falta la justificación", "Solo uno: la creencia", "Cree que son las 4, es verdad y tiene una razón (un reloj que funciona)."),
        ("abc", "Alguien propone: «Saber es creer algo con muchas ganas». ¿Cuál es el problema principal?", "Deja entrar creencias falsas o sin razones, así que es demasiado amplia", "Es demasiado estrecha, porque deja fuera casi todo", "No usa la palabra «verdad» en el título", "Cualquier creencia fuerte contaría como saber, aunque sea falsa o infundada."),
        ("abc", "Un reloj detenido marca las 3 y justo son las 3. Marina lo mira y cree «son las 3». Es verdad y tiene una razón, pero por pura casualidad. ¿Qué muestra este caso a quienes discuten la definición clásica?", "Que cumplir los tres rasgos puede no bastar si el acierto es casual", "Que la creencia no es un rasgo del saber", "Que la verdad no importa para saber", "El caso hace dudar de que los tres rasgos sean suficientes, porque la razón resultó engañosa y el acierto fue suerte."),
        ("abc", "¿Qué conviene hacer al leer un texto que usa «conocimiento» con un sentido especial?", "Reconstruir qué rasgos le atribuye antes de discutir sus conclusiones", "Reemplazarlo por el significado cotidiano de la palabra", "Ignorar la palabra y leer solo las conclusiones", "Un texto filosófico usa las palabras con sentido preciso y hay que reconstruirlo para entenderlo."),
    ],
    ctx=("abc", "Dos amigas ficticias discuten. Elena: «Sé que el equipo ganará, tengo un presentimiento». El equipo gana, pero Elena no tenía ningún dato. Según la definición clásica, ¿qué se puede decir?", "Que su creencia fue verdadera, pero le faltó justificación para hablar de saber", "Que sabía, porque lo creyó y ganó", "Que no creía nada, porque no tenía datos", "Cumple creencia y verdad, pero un presentimiento sin razones no la justifica."),
    sc=[
        ("En Seminario de filosofía: ¿qué tres rasgos tiene la definición clásica de conocimiento?", "Creencia, verdad y justificación", "Son los tres rasgos de D3 en la ficha."),
        ("¿Qué muestra un caso de certeza con error?", "Que la certeza no basta para saber", "La persona está segura, pero lo creído es falso."),
        ("En Seminario de filosofía: ¿Cuándo una definición es demasiado estrecha?", "Cuando deja fuera casos que sí deberían entrar", "Excluye algo que cuenta como el concepto."),
    ],
    op=("Elige uno de estos conceptos: «mentir», «promesa» o «aprender». Escribe una definición de dos o tres rasgos, un caso que la cumpla, un caso que ponga a prueba si es amplia o estrecha y, si hace falta, una versión corregida. "
        "Indica qué rasgos serían condiciones necesarias.",
        "Concepto: mentir. Definición: decir algo que se cree falso con la intención de que otro lo crea. Caso que la cumple: decir «no tengo tarea» sabiendo que sí. Caso que la prueba: decir algo falso creyendo que es verdad (no cumple, y es lo esperado). Rasgos necesarios: decir algo, creerlo falso e intención de engañar.",
        ["la definición tiene al menos dos rasgos claros", "incluye un caso que la cumple y uno que la pone a prueba", "dice si es amplia o estrecha", "señala cuáles rasgos son necesarios"],
        ["definición, casos y versión corregida"],
        ["definir con un sinónimo", "no buscar ningún caso difícil", "confundir un rasgo frecuente con uno necesario"],
        "Pregunta: «¿qué caso extraño podría romper tu definición?». Pídele que lo busque y la corrija."),
    reinforce="Aplica la definición clásica de conocimiento a tres cosas que crees saber (por ejemplo, el nombre de un compañero) y revisa creencia, verdad y razones.",
    extend="Escribe un caso propio de acierto por suerte y explica por qué la definición clásica podría decir que sí sabe, aunque nos parezca que no.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (textos de ejemplo; autores y obras ficticios). Contexto: en la ciudad imaginaria de «Puerto Alto» crecían el comercio lejano y el uso de instrumentos de medición, y mucha gente dudaba de las historias que se transmitían solo por tradición. "
     "Texto A (Delia Marín, autora ficticia): «Todo lo que sé lo aprendí por los sentidos: nadie conoce el color sin haberlo visto. Para afirmar algo hay que observarlo y comprobarlo.» "
     "Texto B (Ramiro Salas, autor ficticio): «Los sentidos a veces se equivocan, como al ver torcido un palo metido en el agua. En cambio, que dos más dos sean cuatro lo sé con la razón, sin mirar nada. Por eso la razón es un camino más seguro que los sentidos.»")
build(
    O1, 3, F,
    use="Aprenderé a reconstruir el planteamiento de un texto filosófico y a situarlo en su contexto sin confundir su origen con su verdad.",
    prior=["Sé formular un problema filosófico.", "Sé definir conocimiento con tres rasgos.", "Sé qué es un supuesto."],
    explain=[
        "Reconstruir una perspectiva es explicar con tus palabras qué sostiene un texto y por qué, sin agregar ni quitar nada. Se busca el problema que aborda, la tesis (lo que defiende), las razones (por qué lo defiende) y los supuestos que da por ciertos. También se pregunta por el antecedente: con quién discute el texto, aunque no lo nombre. En la ficha, los dos textos responden a una pregunta común: de dónde viene el conocimiento seguro.",
        "El contexto sociocultural ayuda a entender por qué un texto se escribió así. En Puerto Alto, el comercio y los instrumentos de medición hacían atractiva la observación, y la duda sobre la tradición era frecuente. Pero el contexto explica el surgimiento de una idea y no decide si es verdadera: rechazar o aceptar una tesis solo por su origen es la falacia genética. Un error parecido es el anacronismo, que consiste en atribuir a una época ideas o conceptos de otra.",
        "Reconstruir con justicia es aplicar el principio de caridad: presentar la versión más fuerte de una postura antes de criticarla. Reconstruir no es estar de acuerdo. Para no mezclar lo que dice el texto con lo que tú piensas, separa siempre «el texto sostiene…» de «yo pienso…».",
    ],
    vocab=[("reconstruir", "explicar con palabras propias tesis, razones y supuestos sin deformarlos"), ("tesis", "idea central que un texto defiende"), ("razón", "motivo que apoya una tesis"), ("falacia genética", "rechazar o aceptar una tesis solo por su origen o su contexto"), ("anacronismo", "atribuir a una época ideas o conceptos de otra"), ("principio de caridad", "presentar la versión más fuerte de una postura antes de criticarla")],
    worked=[
        ("Reconstruir el Texto A", "Reconstruye el Texto A de la ficha: tesis, razón y supuesto.",
         ["Tesis: para afirmar algo hay que observarlo y comprobarlo.", "Razón: todo lo que se sabe se aprendió por los sentidos; nadie conoce el color sin haberlo visto."],
         "Tesis: conocer exige observar y comprobar. Razón: el saber viene de los sentidos. Supuesto: la observación comprobada es fiable"),
        ("Contexto y verdad", "Un estudiante dice: «Como en Puerto Alto había comercio, el Texto A tiene que ser verdadero». ¿Qué error comete?",
         ["Veo que usa el contexto como prueba de la tesis.", "El contexto explica por qué surgió una idea, no demuestra que sea cierta."],
         "Falacia genética: confunde el origen de la idea con su verdad"),
    ],
    mistakes=[("Reconstruir un texto con las propias opiniones y atribuirle lo que no dice.", "Se mezcla lo que dice el texto con lo que uno piensa.", "Separa «el texto sostiene…» de «yo pienso…» y vuelve a leer las frases del texto."),
              ("Usar el contexto para decidir si la tesis es verdadera o falsa.", "Se confunde la explicación del origen con la evaluación de las razones.", "Usa el contexto para entender el texto y las razones para evaluarlo.")],
    T=[
        ("abc", "{F} ¿Cuál es la tesis del Texto B?", "La razón es un camino más seguro que los sentidos", "Los sentidos nunca se equivocan", "Todo conocimiento viene de observar y comprobar", "Su conclusión es que la razón es más segura que los sentidos."),
        ("abc", "{F} ¿Qué razón da el Texto B para desconfiar de los sentidos?", "Los sentidos a veces se equivocan, como al ver torcido un palo en el agua", "Solo ven colores", "Los instrumentos de medición no existen", "Ofrece el ejemplo del palo que parece torcido en el agua."),
        ("abc", "{F} ¿Qué supuesto se aprecia en el Texto B?", "Que la razón, cuando algo es claro, no se equivoca", "Que los sentidos son infalibles", "Que nadie puede conocer nada", "Si la razón es el camino más seguro, supone que es fiable cuando el asunto es claro."),
        ("abc", "{F} ¿En qué coinciden los Textos A y B?", "Ambos responden de dónde viene el conocimiento seguro", "Ambos defienden que hay que observar y comprobar", "Ambos sostienen que los sentidos son el único camino", "Comparten el problema, aunque den respuestas distintas."),
        ("abc", "{F} ¿Qué parte de la ficha corresponde al contexto sociocultural?", "La descripción de Puerto Alto, con su comercio e instrumentos de medición", "La frase «nadie conoce el color sin haberlo visto»", "La afirmación de que la razón es más segura", "Es la descripción de las condiciones de época y lugar."),
        ("ab", "{F} ¿Cuál es una reconstrucción fiel de la razón del Texto A?", "Todo lo que sabe lo aprendió por los sentidos", "Los sentidos siempre engañan", "El Texto A apoya la observación; afirmar que los sentidos siempre engañan es lo contrario de lo que dice."),
        ("abc", "Una estudiante resume el Texto B así: «Ramiro Salas dice que los sentidos no sirven para nada». ¿Qué defecto tiene?", "Exagera la tesis: el texto dice que la razón es más segura, no que los sentidos no sirvan", "Es una reconstrucción perfecta", "Olvida mencionar a Delia Marín", "El texto solo compara seguridad; decir «para nada» deforma su tesis."),
        ("abc", "Un lector dice: «Delia Marín escribió pensando en comerciantes, así que su tesis tiene que ser falsa». ¿Qué error comete?", "Falacia genética: rechaza la tesis por su origen", "Anacronismo: la ubica en una época equivocada", "Ninguno: el contexto prueba que es falsa", "El origen de una idea no decide si es verdadera o falsa."),
        ("abc", "Alguien explica el Texto A con el vocabulario de la neurociencia actual, como si la autora ficticia la conociera. ¿Qué error comete?", "Anacronismo", "Falacia genética", "Aplicar el principio de caridad", "Atribuye a una época conceptos de otra."),
        ("abc", "{F} Un estudiante dice: «Los textos A y B no discuten entre sí porque no se nombran». ¿Es correcta la afirmación?", "No: pueden discutir el mismo problema aunque no se nombren, por sus respuestas opuestas", "Sí: solo hay discusión si se nombran", "Sí: porque son de épocas distintas", "Un antecedente puede ser una discusión implícita; basta que respondan a la misma pregunta."),
        ("abc", "{F} Aplica el principio de caridad al Texto A. ¿Cuál es la reconstrucción más fuerte?", "Sin experiencia no tendríamos ideas como la del color, y por eso conviene comprobar las afirmaciones con la observación", "Delia Marín piensa que solo vale lo que ve cualquiera", "Delia Marín quiere que nadie use la razón", "Conserva su razón y su tesis sin caricaturizarlas."),
        ("abc", "¿Qué conviene hacer para no mezclar tus ideas con las del texto?", "Separar «el texto sostiene…» de «yo pienso…»", "Escribir solo lo que opinas", "Evitar citar frases del texto", "Marcar quién dice qué mantiene la reconstrucción fiel."),
        ("abc", "Reconstruir con fidelidad una postura y estar de acuerdo con ella son cosas…", "Distintas: se puede reconstruir bien una postura que se rechaza", "La misma, porque no se puede explicar lo que no se comparte", "Opuestas, porque explicar es defender", "La reconstrucción busca comprender; la evaluación viene después."),
    ],
    ctx=("abc", "Un texto de ejemplo dice: «En mi aldea, antes de zarpar, los pescadores comprueban el viento; confiar solo en lo que contaba el abuelo nos ha costado barcas». ¿Qué idea de conocimiento sugiere?", "Que conviene comprobar con la experiencia antes de aceptar lo que dice la tradición", "Que la tradición siempre es más segura", "Que el viento no se puede conocer", "Reconoce el valor de comprobar con la experiencia frente a lo transmitido sin examen."),
    sc=[
        ("En Seminario de filosofía: ¿qué es la falacia genética?", "Rechazar o aceptar una tesis solo por su origen o contexto", "El origen de una idea no decide si es verdadera."),
        ("¿Qué es el anacronismo al leer un texto antiguo?", "Atribuir a una época ideas o conceptos de otra", "Se interpreta el texto con conceptos que su autor no tenía."),
        ("¿Para qué sirve el contexto sociocultural?", "Para entender por qué surgió el texto y no para decidir su verdad", "Explica las condiciones del texto sin evaluar sus razones."),
    ],
    op=("Lee este texto de ejemplo (autor ficticio): «Valeria Rojas sostiene que la memoria compartida de un grupo es más confiable que la de una sola persona, porque los errores de cada uno se corrigen al conversar. Escribe en un tiempo en que los pueblos guardaban su historia en relatos contados en reuniones». "
        "Reconstruye en tres líneas: tesis, razón y supuesto. Luego explica qué aporta el contexto sin usarlo como prueba de la tesis.",
        "Tesis: la memoria compartida es más confiable que la individual. Razón: al conversar se corrigen los errores de cada persona. Supuesto: quienes conversan corrigen con buena fe y sin repetir errores colectivos. Contexto: explica por qué los relatos en reuniones eran importantes, pero no prueba que la tesis sea verdadera.",
        ["reconstruye tesis, razón y supuesto sin agregar ideas propias", "distingue lo que dice el texto de lo que opina", "explica el aporte del contexto", "no usa el contexto como prueba de la tesis"],
        ["tres líneas de reconstrucción y una explicación del contexto"],
        ["mezclar su opinión con la tesis del texto", "exagerar la tesis", "usar el contexto para decidir si es verdadera"],
        "Pregunta: «¿qué frase del texto respalda cada parte de tu reconstrucción?». Pídele que marque cuál es suya y cuál del texto."),
    reinforce="Escribe en tres líneas la tesis, la razón y el supuesto del Texto B de la ficha, con tus palabras.",
    extend="Elige una idea que hoy parezca obvia y explica con un ejemplo cómo el contexto de otra época pudo hacerla surgir sin probar que sea verdadera.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (argumentos de ejemplo). Argumento 1: «Los sentidos a veces nos engañan. Lo que a veces engaña no es totalmente seguro. Por lo tanto, los sentidos no son una fuente totalmente segura.» "
     "Argumento 2: «Si una creencia está justificada, entonces es verdadera. Mi creencia es verdadera. Por lo tanto, mi creencia está justificada.» "
     "Argumento 3: «Si llueve, el patio se moja. Hoy el patio está mojado. Por lo tanto, hoy llovió.»")
build(
    O1, 4, F,
    use="Aprenderé a formular y evaluar argumentos de un texto filosófico: reconstruirlos, juzgar su validez y examinar sus premisas y objeciones.",
    prior=["Sé reconstruir tesis, razones y supuestos.", "Sé qué es una falacia genética.", "Distingo creencia de conocimiento."],
    explain=[
        "Un argumento es un conjunto de afirmaciones donde unas, las premisas, buscan apoyar otra, la conclusión. Para evaluarlo se mira primero su forma. Un argumento es válido si, suponiendo que las premisas fueran verdaderas, la conclusión tendría que ser verdadera. La validez no mide si las premisas son verdaderas. Un argumento es sólido si es válido y además todas sus premisas son verdaderas.",
        "Para evaluar un texto filosófico conviene reconstruir primero sus argumentos en forma ordenada: premisa 1, premisa 2 y conclusión. Una inferencia es el paso de las premisas a la conclusión. Una falacia es un error de razonamiento frecuente, como afirmar el consecuente («si llueve, el patio se moja; el patio está mojado; luego llovió», ya que el patio pudo mojarse por otra causa). Nombrar una falacia no basta: hay que mostrar en el argumento reconstruido dónde falla el paso.",
        "Una objeción es una razón contra una tesis o una premisa. Puede atacar una premisa (negarla o mostrar que es dudosa) o la inferencia (mostrar que la conclusión no se sigue). Evaluar bien es separar tres preguntas: qué sostiene el argumento, si su forma es válida y si sus premisas son aceptables.",
    ],
    vocab=[("argumento", "conjunto de afirmaciones donde las premisas apoyan una conclusión"), ("premisa", "afirmación que se ofrece como apoyo de la conclusión"), ("conclusión", "afirmación que el argumento busca establecer"), ("validez", "propiedad de un argumento cuya conclusión se seguiría necesariamente de las premisas si fueran verdaderas"), ("solidez", "ser válido y tener todas las premisas verdaderas"), ("inferencia", "paso de las premisas a la conclusión"), ("falacia", "error de razonamiento frecuente"), ("objeción", "razón contra una tesis o una premisa")],
    worked=[
        ("Reconstruir y evaluar", "Evalúa el Argumento 1 de la ficha: ¿es válido?",
         ["Ordeno: P1: los sentidos a veces engañan. P2: lo que a veces engaña no es totalmente seguro. C: los sentidos no son totalmente seguros.", "Si P1 y P2 fueran verdaderas, C se seguiría necesariamente."],
         "Es válido; su solidez depende de aceptar que P2 es verdadera"),
        ("Detectar y explicar una falacia", "El Argumento 3 de la ficha, ¿es válido? Explica sin solo nombrar la falacia.",
         ["Ordeno: P1: si llueve, el patio se moja. P2: el patio está mojado. C: llovió.", "Aunque P1 y P2 fueran verdaderas, el patio pudo mojarse porque alguien lo regó: la conclusión no se sigue."],
         "No es válido: afirma el consecuente, porque hay otras causas posibles del patio mojado"),
    ],
    mistakes=[("Decir «es una falacia» y no mostrar dónde falla el argumento.", "Se nombra el error sin reconstruir las premisas y la inferencia.", "Ordena premisas y conclusión y muestra un caso en que las premisas son verdaderas y la conclusión falsa."),
              ("Creer que un argumento válido tiene conclusión verdadera.", "Se confunde validez, que es de forma, con verdad de las premisas.", "Revisa por separado si las premisas son verdaderas: la validez no lo asegura.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es una premisa?", "Una afirmación que se ofrece como apoyo de la conclusión", "La afirmación que se busca establecer", "Cualquier error de razonamiento", "Las premisas apoyan; la conclusión es lo que se quiere establecer."),
        ("abc", "¿Cuándo un argumento es válido?", "Cuando, si las premisas fueran verdaderas, la conclusión tendría que serlo", "Cuando su conclusión es verdadera", "Cuando mucha gente lo acepta", "La validez se refiere a la relación entre premisas y conclusión, no a la verdad de las partes."),
        ("abc", "{F} ¿Cuál es la conclusión del Argumento 2?", "Mi creencia está justificada", "Mi creencia es verdadera", "Si una creencia está justificada, es verdadera", "La conclusión es la afirmación que viene después de «por lo tanto»."),
        ("abc", "«Si hoy hay clase de filosofía, el aula está abierta. Hoy no hay clase de filosofía. Por lo tanto, el aula no está abierta.» ¿Es válido?", "No: el aula podría estar abierta por otra razón y la conclusión no se sigue", "Sí: las dos premisas son razonables", "Sí: tiene dos premisas y una conclusión", "Aunque las premisas fueran verdaderas, el aula puede estar abierta por otro motivo."),
        ("abc", "{F} ¿Por qué el Argumento 3 no es válido?", "Porque el patio pudo mojarse por otra causa y la conclusión no se sigue", "Porque no tiene premisas", "Porque habla de lluvia y no de filosofía", "Con las premisas verdaderas, la conclusión puede ser falsa."),
        ("ab", "{F} El Argumento 2 tiene la forma «si A entonces B; B; luego A». ¿Es válido?", "No: tiene la misma forma que el del patio mojado, y la conclusión no se sigue", "Sí: porque la conclusión suena razonable", "Comparte la forma del Argumento 3, y una creencia puede ser verdadera sin estar justificada."),
        ("abc", "«Todos los textos del taller son breves. Este texto es del taller. Por lo tanto, es breve.» ¿Qué se puede decir?", "Es válido: la conclusión se sigue de las premisas", "Es inválido: falta una tercera premisa", "Es una falacia genética", "Si las dos premisas son verdaderas, la conclusión necesariamente lo es."),
        ("abc", "«Si las dos premisas fueran verdaderas, la conclusión tendría que serlo; pero la primera premisa es falsa.» ¿Qué se concluye?", "El argumento es válido, pero no sólido", "El argumento es inválido", "El argumento es sólido", "La solidez exige validez y premisas verdaderas; aquí falla una premisa."),
        ("abc", "Un estudiante responde al Argumento 1: «Eso lo dice alguien que nunca ha viajado, así que no vale». ¿Qué error comete?", "Ataca a la persona y no examina premisas ni inferencia", "Presenta una objeción a la premisa 2", "Muestra que el argumento es inválido", "Una objeción debe dirigirse a las premisas o a la inferencia, no a quien argumenta."),
        ("abc", "{F} Una objeción al Argumento 1 dice: «Que los sentidos a veces engañen no significa que dejen de ser una fuente muy segura en lo cotidiano». ¿Qué ataca?", "La premisa 2 o la fuerza de la conclusión, porque duda de que «a veces» implique «no seguro»", "La forma válida del argumento", "A la persona que lo escribió", "Cuestiona el paso entre engañar a veces y no ser seguro, es decir, una premisa."),
        ("abc", "Alguien dice «es la falacia de afirmar el consecuente» y no agrega nada más. ¿Por qué no basta?", "Porque falta mostrar, con las premisas ordenadas, un caso en que el argumento falla", "Porque antes hay que comprobar si la conclusión es verdadera", "Porque las falacias solo se aplican a argumentos de tres premisas", "Nombrar el error no muestra por qué la conclusión no se sigue."),
        ("abc", "{F} Si cambiamos el Argumento 3 a «Si llueve, el patio se moja. Hoy llovió. Por lo tanto, el patio está mojado», ¿qué ocurre?", "Pasa a ser válido: si las premisas fueran verdaderas, la conclusión se sigue", "Sigue siendo inválido", "Deja de tener conclusión", "La nueva forma, «si A entonces B; A; luego B», sí garantiza la conclusión."),
        ("abc", "Un argumento válido con una premisa falsa que se descubre falsa ¿qué permite concluir?", "Que no prueba su conclusión, aunque su forma sea buena", "Que su conclusión es necesariamente verdadera", "Que su conclusión es necesariamente falsa", "Si una premisa es falsa, el argumento no es sólido y no establece su conclusión; esta puede ser verdadera o falsa."),
    ],
    ctx=("abc", "Un texto de ejemplo argumenta: «El conocimiento exige razones. Nadie puede dar razones de lo que sintió en un sueño. Por lo tanto, nadie sabe lo que sintió en un sueño». ¿Cuál es un modo correcto de evaluarlo?", "Ordenar premisas y conclusión y examinar si la premisa 2 es aceptable", "Rechazarlo porque trata de sueños", "Aceptarlo porque es un texto filosófico", "Evaluar bien es reconstruir, comprobar la forma y examinar las premisas."),
    sc=[
        ("En Seminario de filosofía: ¿qué es un argumento sólido?", "Uno válido y con todas las premisas verdaderas", "Combina buena forma con premisas verdaderas."),
        ("¿Qué dos cosas puede atacar una objeción?", "Una premisa o la inferencia", "Se puede negar una premisa o mostrar que la conclusión no se sigue."),
        ("¿Por qué un argumento válido puede tener conclusión falsa?", "Porque alguna premisa puede ser falsa", "La validez no asegura que las premisas sean verdaderas."),
    ],
    op=("Lee este texto de ejemplo (autora ficticia): «Si una persona prefiere siempre lo que ya conoce, nunca aprende algo nuevo. Mi compañero prefiere siempre lo que ya conoce. Entonces, mi compañero nunca aprende algo nuevo.» "
        "Ordena el argumento en premisas y conclusión, decide si es válido, y escribe una objeción dirigida a una premisa.",
        "P1: si alguien prefiere siempre lo conocido, nunca aprende algo nuevo. P2: mi compañero prefiere siempre lo conocido. C: mi compañero nunca aprende algo nuevo. Es válido. Objeción a P1: una persona puede preferir lo conocido y, sin embargo, aprender por casualidad o por obligación.",
        ["ordena premisas y conclusión", "decide la validez con una razón", "formula una objeción a una premisa", "no ataca a la persona"],
        ["argumento ordenado, juicio de validez y una objeción"],
        ["nombrar una falacia sin reconstruir", "confundir validez con verdad", "atacar a quien escribió el texto"],
        "Pregunta: «¿tus premisas, si fueran verdaderas, harían necesaria la conclusión?». Si duda, pídele que pruebe con otro caso."),
    reinforce="Escribe un argumento válido de dos premisas sobre algo de tu entorno y luego cámbialo para que sea inválido, y explica la diferencia.",
    extend="Busca una conversación o texto breve con un «porque» y reconstruye su argumento en premisas y conclusión. Indica qué premisa te parece más discutible.",
)

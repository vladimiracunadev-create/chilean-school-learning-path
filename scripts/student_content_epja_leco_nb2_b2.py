"""Lenguaje y Comunicación EPJA Nivel 2 básico, módulo 2 (parte 2): OAD-06, distinguir hechos y opiniones en textos de los medios de comunicación. Notas, columnas y mensajes originales con datos inventados y rotulados; sin medios ni marcas reales."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-06"

F1 = ("Nota de ejemplo (datos inventados): «El municipio inauguró ayer una plaza con 12 bancas y 30 árboles. Es la plaza más linda de la comuna. "
      "Quedó abierta todos los días de 8:00 a 20:00 horas.»")
F2 = ("Seis oraciones de ejemplo. 1) «El bus 405 pasa cada 15 minutos.» 2) «Me parece que el bus 405 es demasiado lento.» 3) «La feria funciona los sábados y domingos.» "
      "4) «La feria es excelente.» 5) «El nuevo horario es injusto.» 6) «La obra terminó en marzo.»")
F3 = ("Nota de ejemplo (datos inventados). Titular: «Vecinos piden cambiar el paradero». Texto: «El martes, 40 vecinos firmaron una carta para pedir que el paradero de la calle Sur se traslade a la esquina. "
      "El dirigente afirmó que el lugar actual es peligroso. La municipalidad respondió que revisará el pedido en diez días.»")
F4 = ("Nota de ejemplo (datos inventados): «La feria cambiará de lugar el sábado próximo. Se instalará en la calle Los Pinos, de 8:00 a 14:00 horas. "
      "El toldo del presidente de los feriantes es azul. Todo el mundo sabe que ese lugar es mucho mejor. Los vecinos podrán llegar en el bus 12.»")
F5 = ("Mensaje reenviado de ejemplo (inventado): «URGENTE: mañana cierran todos los consultorios de la ciudad. Es una vergüenza. "
      "¡Reenvía a todos tus contactos antes de que sea tarde!»")
F6 = ("Columna de ejemplo (datos inventados): «El año pasado el taller de computación tuvo 25 inscritos; este año tiene 40. Es una noticia estupenda. "
      "Pienso que la sede debería comprar más computadores, porque hoy hay uno por cada dos personas inscritas. Sin duda, quienes se oponen no entienden nada.»")

build(
    O, 1, F1,
    use="Hoy aprendo a separar, en una nota de los medios, lo que se puede comprobar de lo que alguien opina.",
    prior=["Leo notas y avisos breves.", "Sé que las personas pueden pensar distinto sobre lo mismo.", "Reconozco datos como fechas, cifras y lugares."],
    explain=[
        "Los medios de comunicación son los canales que entregan información: diarios, radio, televisión y sitios de internet. En ellos conviven dos tipos de frases. Un hecho es algo que ocurrió o que existe y se puede comprobar. Una opinión es lo que alguien piensa o siente sobre algo.",
        "En la nota de ejemplo, «inauguró ayer una plaza con 12 bancas y 30 árboles» es un hecho: se puede ir a contar las bancas. En cambio, «es la plaza más linda» es una opinión: a otra persona le podría parecer distinto. Nadie puede comprobar con una regla lo «lindo».",
        "Distinguir hechos de opiniones no significa que las opiniones sean malas. Todas las personas opinan. Lo importante es saber cuándo estás leyendo un dato y cuándo estás leyendo un juicio, para decidir con claridad qué creer.",
    ],
    vocab=[("hecho", "algo que ocurrió o existe y se puede comprobar"), ("opinión", "lo que alguien piensa o siente sobre algo"), ("comprobar", "revisar con datos o con la observación si algo es cierto"), ("medios de comunicación", "canales que entregan información, como el diario o la radio")],
    worked=[
        ("Un hecho", "«El mercado tiene 25 puestos y abre de lunes a sábado».", ["¿Se puede comprobar? Sí: se pueden contar los puestos y revisar los días.", "Entonces es un dato de la realidad."], "Es un hecho."),
        ("Una opinión", "«Es el mercado más acogedor del barrio».", ["¿Se puede comprobar con un conteo o un registro? No.", "La palabra «más acogedor» expresa un juicio de gusto."], "Es una opinión."),
    ],
    mistakes=[
        ("Creer que algo es un hecho solo porque aparece en una nota.", "Una nota puede mezclar hechos y opiniones.", "Revisa cada oración: ¿se puede comprobar?"),
        ("Pensar que toda opinión es falsa.", "Una opinión no es verdadera ni falsa: es un juicio que puede tener o no razones.", "Reconócela como opinión y mira si tiene respaldo."),
    ],
    T=[
        ("abc", "{F} ¿Qué inauguró el municipio?", "Una plaza", "Una biblioteca", "Un mercado", "La primera oración dice que inauguró una plaza."),
        ("ab", "{F} ¿«Tiene 12 bancas» es un hecho o una opinión?", "Un hecho", "Una opinión", "Se pueden contar las bancas para comprobarlo."),
        ("ab", "{F} ¿«Es la plaza más linda de la comuna» es un hecho o una opinión?", "Una opinión", "Un hecho", "Lo «lindo» depende del gusto de cada persona."),
        ("=", "{F} La plaza abre de 8:00 a 20:00 horas. ¿Cuántas horas al día está abierta?", "20-8", "De 8 a 20 hay 12 horas, porque 20 menos 8 es 12.", "horas"),
        ("abc", "{F} ¿Cuál de estas oraciones de la nota es un hecho?", "Quedó abierta todos los días de 8:00 a 20:00 horas", "Es la plaza más linda de la comuna", "Es una noticia que alegrará a todos", "El horario se puede comprobar yendo a la plaza."),
        ("ab", "{F} ¿Qué palabra de la nota indica una opinión?", "más linda", "inauguró", "«Más linda» es un juicio de gusto; «inauguró» es una acción ocurrida."),
        ("abc", "{F} ¿Cuántos árboles dice la nota que tiene la plaza?", "30", "12", "20", "La nota dice 12 bancas y 30 árboles."),
        ("ab", "{F} Si alguien dice «La plaza tiene 30 árboles», ¿qué hace?", "Da un hecho que se puede contar", "Da una opinión", "Un número de árboles se comprueba contando."),
        ("abc", "{F} ¿Cómo se puede comprobar el hecho de las bancas?", "Yendo a la plaza y contándolas", "Preguntando quién cree que es linda", "Leyendo la nota otra vez", "Los hechos se comprueban con observación o registros."),
        ("ab", "Oración de ejemplo: «El jueves llovió en la mañana». ¿Qué es?", "Un hecho que se puede comprobar con registros del día", "Una opinión", "Se puede revisar si llovió o no ese día."),
        ("abc", "Oración de ejemplo: «El pan de esa panadería es el más rico». ¿Qué es?", "Una opinión de gusto", "Un hecho comprobable", "Un número", "«El más rico» depende del paladar de cada quien."),
        ("ab", "Oración de ejemplo: «El taller tiene 18 inscritos». ¿Qué es?", "Un hecho, porque se pueden contar los inscritos", "Una opinión", "Hay una lista que permite verificar la cifra."),
        ("abc", "Oración de ejemplo: «Esa película es aburrida». ¿Qué es?", "Una opinión", "Un hecho", "Una fecha", "Lo aburrido es una valoración personal."),
    ],
    ctx=("abc", "Un diario de ejemplo publica: «Se abrió un nuevo consultorio con cinco boxes de atención. Es lo mejor que le ha pasado al barrio». Quien lee quiere comentar con otras personas solo lo comprobable. ¿Qué dato elige?", "Que el consultorio tiene cinco boxes de atención", "Que es lo mejor que le ha pasado al barrio", "Que a todos les gusta", "Solo el número de boxes se puede comprobar; lo «mejor» es un juicio."),
    sc=[("En Lenguaje EPJA: ¿qué es un hecho?", "Algo que ocurrió o existe y se puede comprobar", "Se verifica con observación o registros."),
        ("En Lenguaje EPJA: ¿qué es una opinión?", "Lo que alguien piensa o siente sobre algo", "Una opinión expresa un juicio personal que puede no coincidir con el de otras personas."),
        ("¿Cómo sé si una frase es un hecho?", "Preguntándome si se puede comprobar", "La comprobación es la prueba de un hecho.")],
    op=("Lee esta nota de ejemplo: «La junta de vecinos plantó 15 árboles el sábado en la calle Central. Quedó preciosa. Pienso que deberíamos plantar más». Subraya con un color los hechos y con otro las opiniones, y escribe cada oración en una lista con su tipo.",
        "Hechos: «plantó 15 árboles el sábado en la calle Central». Opiniones: «Quedó preciosa»; «Pienso que deberíamos plantar más».",
        ["identifica un hecho", "identifica dos opiniones", "explica cómo comprobaría el hecho"],
        ["una lista con tipo de cada oración"],
        ["tomar «quedó preciosa» como hecho", "no justificar la clasificación"],
        "Pregunta: «¿Puedo comprobar esta frase con un conteo, un registro o una observación?»."),
    reinforce="Toma una noticia breve y escribe una frase que sea hecho y otra que sea opinión.",
    extend="Escribe tres hechos y tres opiniones sobre un lugar que conozcas y pide a otra persona que los clasifique.",
)

build(
    O, 2, F2,
    use="Hoy conozco las pistas del lenguaje que delatan una opinión y los distintos textos de los medios donde aparecen.",
    prior=["Sé qué es un hecho y qué es una opinión.", "Leo oraciones cortas.", "Reconozco adjetivos como lindo, grande o malo."],
    explain=[
        "Las opiniones suelen dejar pistas. Una pista son las expresiones «creo que», «me parece que», «pienso que» y «debería». Otra pista son las palabras que juzgan, como excelente, injusto, horrible, el mejor o demasiado. Esas palabras muestran lo que alguien siente, no lo que se mide.",
        "Los hechos, en cambio, suelen traer datos: cifras, fechas, nombres de lugares y verbos de acciones que ocurrieron, como «terminó» o «pasa». Por ejemplo, «El consultorio atiende de 8:00 a 17:00» trae horas que pueden comprobarse.",
        "Cada medio mezcla de manera distinta. La noticia busca informar con hechos. La columna de opinión y el editorial expresan lo que piensa quien escribe. La publicidad quiere convencer, y por eso usa palabras muy positivas. Saber en qué texto estás te ayuda a leerlo.",
    ],
    vocab=[("noticia", "texto que cuenta un hecho reciente"), ("columna de opinión", "texto donde alguien da su punto de vista"), ("palabra valorativa", "palabra que expresa un juicio, como injusto o excelente"), ("publicidad", "mensaje que busca convencer de comprar o usar algo")],
    worked=[
        ("Detectar la pista", "«Creo que la fila del banco es excesivamente larga».", ["Veo «creo que»: es una marca de opinión.", "Veo «excesivamente larga»: es una expresión que juzga."], "Es una opinión."),
        ("Detectar el dato", "«El consultorio cierra a las 17:00».", ["No hay marcas de opinión.", "Hay una hora concreta que se puede comprobar en el consultorio."], "Es un hecho."),
    ],
    mistakes=[
        ("Creer que todo adjetivo es una opinión.", "Hay adjetivos que describen datos, como «verde» o «cerrado».", "Pregunta si el adjetivo se puede comprobar o solo expresa un gusto."),
        ("Pensar que sin «creo que» no hay opinión.", "Algunas opiniones vienen sin marca, como «La feria es excelente».", "Busca también palabras que juzgan."),
    ],
    T=[
        ("=", "{F} Si el bus 405 pasa cada 15 minutos, ¿cuántas veces pasa en una hora?", "60/15", "Una hora tiene 60 minutos y 60 dividido en 15 da 4 pasadas.", "veces"),
        ("ab", "{F} La oración 1, ¿es hecho u opinión?", "Hecho", "Opinión", "Trae una frecuencia que se puede medir con un reloj."),
        ("ab", "{F} La oración 2, ¿es hecho u opinión?", "Opinión", "Hecho", "Tiene «me parece que» y «demasiado lento»."),
        ("abc", "{F} ¿Qué palabras marcan opinión en la oración 2?", "me parece que y demasiado", "bus 405", "cada 15 minutos", "Esas expresiones muestran un juicio personal."),
        ("ab", "{F} La oración 3, ¿es hecho u opinión?", "Hecho", "Opinión", "Los días de la feria se pueden comprobar."),
        ("ab", "{F} La oración 4, ¿es hecho u opinión?", "Opinión", "Hecho", "«Excelente» es una palabra que juzga."),
        ("abc", "{F} ¿Cuál de las seis oraciones trae la palabra valorativa «injusto»?", "La oración 5", "La oración 3", "La oración 6", "«El nuevo horario es injusto» contiene esa palabra."),
        ("{F} ¿Cuántas de las seis oraciones son hechos? (un número)", "3", "Son hechos las oraciones 1, 3 y 6; las otras tres son opiniones."),
        ("ab", "{F} La oración 6, ¿es hecho u opinión?", "Hecho", "Opinión", "Que una obra terminó en marzo se puede comprobar con registros."),
        ("abc", "¿Qué tipo de texto de los medios busca informar con hechos recientes?", "La noticia", "La columna de opinión", "La publicidad", "La noticia cuenta con hechos lo ocurrido recientemente; la columna y la publicidad no."),
        ("ab", "Un afiche dice «¡La mejor oferta del barrio!». ¿Qué expresa?", "Una opinión que busca convencer", "Un hecho confirmado", "«La mejor» es un juicio y el afiche quiere que compres."),
        ("abc", "¿Cuál es una marca de opinión?", "pienso que", "el lunes", "veinte personas", "«Pienso que» indica lo que alguien piensa, es decir, una opinión."),
        ("ab", "Oración de ejemplo: «El taller empieza a las 19:00». ¿Qué es?", "Un hecho", "Una opinión", "La hora de inicio se puede comprobar en el programa."),
    ],
    ctx=("abc", "Una radio de ejemplo transmite: «La reunión de vecinos es a las 19:00 en la sede. Creo que será la más importante del año». ¿Qué parte se puede comprobar al llegar a la sede?", "La hora y el lugar de la reunión", "Que será la más importante", "Que todos están de acuerdo", "Solo la hora y el lugar son verificables; «más importante» es un juicio."),
    sc=[("¿Qué es una palabra valorativa?", "Una palabra que expresa un juicio", "Muestra gusto o valoración, como excelente o injusto."),
        ("¿Qué texto de los medios busca informar?", "La noticia", "Su propósito es contar hechos recientes."),
        ("¿Dónde busco una opinión explícita?", "En una columna de opinión", "Allí quien escribe da su punto de vista.")],
    op=("Lee estas oraciones de ejemplo: a) «El consultorio atiende de 8:00 a 17:00». b) «Esa fila es insoportable». c) «Creo que deberían poner más sillas». d) «Hay 20 sillas en la sala». Clasifica cada una como hecho u opinión y subraya la pista que te ayudó.",
        "a) hecho (horario). b) opinión (insoportable). c) opinión (creo que, deberían). d) hecho (número de sillas).",
        ["clasifica las cuatro oraciones", "subraya la pista de cada una", "explica una clasificación con una oración"],
        ["cuatro clasificaciones con su pista"],
        ["no marcar la pista", "tomar «insoportable» como hecho"],
        "Pregunta: «¿Esa palabra muestra un dato o un gusto?»."),
    reinforce="Anota cinco oraciones con «creo que» o «me parece» y cinco con cifras o fechas.",
    extend="Escribe una oración que parezca un dato pero sea una opinión, y otra que lo contrario; explica la diferencia.",
)

build(
    O, 3, F3,
    use="Hoy practico los pasos para distinguir hechos y opiniones en una noticia, incluyendo lo que alguien afirma.",
    prior=["Reconozco marcas de opinión.", "Sé qué es un hecho.", "Leo titulares y notas breves."],
    explain=[
        "Para distinguir hechos y opiniones, sigue tres pasos. Primero, lee la oración completa. Segundo, pregunta: ¿se puede comprobar? ¿cómo? Tercero, busca pistas de opinión: marcas como «creo que» y palabras que juzgan. Si la respuesta al segundo paso es sí, es un hecho.",
        "En una noticia, a veces alguien afirma algo. «El presidente del club afirmó que el campeonato fue un éxito» contiene dos cosas. Que el dirigente lo dijo es un hecho; se puede comprobar que lo dijo. Que el campeonato haya sido un éxito es un juicio que habría que respaldar con datos, como asistencia o resultados.",
        "Un titular también puede traer hechos y opiniones. «Vecinos piden cambiar el paradero» es un hecho: hay un pedido. Un titular como «Un paradero terrible» sería una opinión. Con los tres pasos puedes revisar cualquier texto.",
    ],
    vocab=[("afirmar", "decir que algo es cierto"), ("respaldar", "apoyar una idea con datos o razones"), ("titular", "título de una noticia"), ("dirigente", "persona que lidera una organización de vecinos")],
    worked=[
        ("Aplicar los tres pasos", "«El domingo, 25 personas participaron en una caminata por el barrio».", ["Leo la oración: dice cuántas personas y qué hicieron.", "¿Se puede comprobar? Sí, con la lista de participantes.", "No hay palabras que juzguen."], "Es un hecho."),
        ("Lo que alguien afirma", "«La presidenta del club afirmó que la cancha está en mal estado».", ["Que lo afirmó se puede comprobar: es un hecho.", "Que esté en mal estado es un juicio que necesita datos.", "Separo las dos partes."], "Que lo dijo es hecho; que la cancha está en mal estado es opinión sin datos en la oración."),
    ],
    mistakes=[
        ("Tomar como hecho todo lo que dice una persona importante.", "Que alguien lo diga no lo vuelve comprobable.", "Pregunta qué datos respaldan lo que afirma."),
        ("Marcar toda la oración como opinión por una sola palabra.", "Una oración puede traer un hecho y una opinión juntos.", "Sepáralos en partes."),
    ],
    T=[
        ("abc", "{F} ¿Qué piden los vecinos?", "Que se cambie el paradero de la calle Sur a la esquina", "Que se instale un semáforo", "Que se cierre la calle", "La nota dice que firmaron una carta con ese pedido."),
        ("=", "{F} ¿Cuántos vecinos firmaron la carta? Si luego firman 10 más, ¿cuántos serían?", "40+10", "Con 40 más 10 serían 50 firmas.", "vecinos"),
        ("ab", "{F} ¿«El martes, 40 vecinos firmaron una carta» es hecho u opinión?", "Hecho", "Opinión", "Se puede comprobar con la carta firmada."),
        ("abc", "{F} ¿Qué dice la nota que hará la municipalidad?", "Revisará el pedido en diez días", "Trasladará el paradero mañana", "Negará el pedido", "La respuesta de la municipalidad es revisarlo en ese plazo."),
        ("ab", "{F} «El lugar actual es peligroso», ¿qué es en esta nota?", "Una opinión del dirigente sin datos que la respalden", "Un hecho comprobado en la nota", "La nota no da datos como accidentes que prueben el peligro."),
        ("abc", "{F} ¿Qué se puede comprobar de «El dirigente afirmó que el lugar actual es peligroso»?", "Que el dirigente lo dijo", "Que el lugar es peligroso", "Que habrá un accidente", "De esa oración solo se puede verificar que el dirigente lo dijo; el peligro necesita datos."),
        ("ab", "{F} ¿Cuál es el segundo paso para distinguir hechos y opiniones?", "Preguntar si se puede comprobar", "Contar las palabras", "Es la prueba central para reconocer un hecho."),
        ("abc", "{F} ¿Qué dato respaldaría la opinión de que el lugar es peligroso?", "Un registro de accidentes ocurridos ahí", "Que el dirigente está seguro", "Que los vecinos están cansados", "Un registro de accidentes es comprobable y sí muestra si el lugar es peligroso."),
        ("ab", "{F} El titular «Vecinos piden cambiar el paradero», ¿es hecho u opinión?", "Hecho, porque hubo un pedido", "Opinión", "No usa palabras que juzguen y describe lo que ocurrió."),
        ("abc", "Titular de ejemplo: «Un paradero terrible». ¿Qué tipo de frase es?", "Opinión", "Hecho comprobable", "Fecha", "«Terrible» es una palabra que juzga."),
        ("ab", "Oración de ejemplo: «La municipalidad respondió que revisará el pedido». ¿Qué se puede comprobar?", "Que la municipalidad respondió eso", "Que el pedido es justo", "La respuesta puede verificarse; que sea justo es un juicio."),
        ("abc", "Oración de ejemplo: «El ministro dijo que la medida es excelente». ¿Qué parte es una opinión?", "que la medida es excelente", "El ministro dijo", "la medida", "«Excelente» expresa un juicio, no un dato que se pueda medir."),
        ("ab", "Si una nota dice «Se registraron 3 accidentes en la esquina en el último mes», ¿qué es?", "Un hecho con cifra, que se puede revisar en registros", "Una opinión", "Trae un número y un periodo comprobables."),
    ],
    ctx=("abc", "En una reunión se lee la nota de ejemplo: «Según el informe, 120 personas usaron la sede en abril. Fue un mes magnífico». Para pedir recursos, el dirigente quiere citar solo lo comprobable. ¿Qué cita?", "Que 120 personas usaron la sede en abril", "Que fue un mes magnífico", "Que todos quedaron felices", "La cifra está en un informe; «magnífico» es una opinión."),
    sc=[("¿Cuál es el paso clave para reconocer un hecho?", "Preguntar si se puede comprobar", "Solo lo que se puede comprobar es un hecho; lo que expresa gusto es opinión."),
        ("Si alguien afirma algo, ¿qué es hecho?", "Que lo dijo; lo afirmado puede ser opinión", "La afirmación puede juzgar sin datos."),
        ("¿Qué respalda una opinión?", "Datos o razones", "Sin respaldo, una opinión queda débil.")],
    op=("Lee esta nota de ejemplo: «Ayer se cerró la calle Norte por trabajos de pavimento. La encargada de la obra afirmó que quedará perfecta. Los trabajos duran cinco días». Haz una tabla con dos columnas: Hechos y Opiniones, y pon las tres oraciones donde corresponda. Para la que no está clara, explica cómo la comprobarías.",
        "Hechos: «Ayer se cerró la calle Norte por trabajos de pavimento»; «Los trabajos duran cinco días»; que la encargada lo afirmó. Opinión: «quedará perfecta». Comprobación: viendo el pavimento terminado y comparando con lo prometido.",
        ["clasifica las tres oraciones", "separa lo que alguien afirma", "explica una comprobación"],
        ["una tabla de dos columnas y una explicación"],
        ["tomar «perfecta» como hecho", "olvidar la parte «afirmó»"],
        "Pregunta: «¿Qué dato necesito para comprobar esta oración?»."),
    reinforce="Elige una noticia breve y escribe cuál es el hecho principal y qué opinión aparece.",
    extend="Escribe una nota de tres oraciones con dos hechos y una opinión, y márcalos.",
)

build(
    O, 4, F4,
    use="Hoy practico con un texto mixto: separo hechos y opiniones, descubro una opinión que se disfraza de hecho y reconozco la información relevante y la accesoria.",
    prior=["Sé aplicar los tres pasos.", "Reconozco palabras valorativas.", "Sé buscar datos como fecha, hora y lugar."],
    explain=[
        "A veces una opinión se disfraza de hecho con frases como «todo el mundo sabe que», «es evidente que» o «nadie duda de que». Esas frases no entregan un dato: tratan de convencerte. Cuando las veas, pregunta: ¿quién lo comprobó?, ¿con qué datos?",
        "En una nota también hay información relevante y accesoria. La información relevante es la necesaria para entender el hecho principal: qué cambia, cuándo, dónde y a qué hora. La información accesoria es un detalle que no cambia lo esencial, como el color de un toldo. No es falsa, pero no es lo central.",
        "Por ejemplo, en «El corte de agua será el jueves, de 9:00 a 14:00, y el camión de la empresa es blanco», lo relevante es el día y el horario del corte, y es accesorio el color del camión. Y «todo el mundo sabe que ese servicio es el mejor» sería una opinión disfrazada de hecho.",
    ],
    vocab=[("información relevante", "la que se necesita para entender lo principal"), ("información accesoria", "detalle que no cambia lo esencial"), ("disfrazar", "hacer pasar una cosa por otra"), ("evidente", "que parece claro, aunque a veces no lo es")],
    worked=[
        ("Opinión disfrazada", "«Es evidente que el nuevo horario es mejor para todos».", ["La frase usa «es evidente que», que parece un dato.", "No dice quién lo comprobó ni con qué.", "«Mejor para todos» es un juicio."], "Es una opinión disfrazada de hecho."),
        ("Relevante y accesorio", "Nota de ejemplo: «La reunión será el martes, a las 19:00, en la sede. La secretaria llevará una carpeta amarilla. Se tratará el tema del alumbrado».", ["Relevante: martes, 19:00, sede, tema del alumbrado.", "Accesorio: el color de la carpeta de la secretaria.", "Ese detalle no ayuda a llegar ni a entender de qué se tratará."], "La carpeta amarilla es información accesoria."),
    ],
    mistakes=[
        ("Aceptar «todo el mundo sabe que…» como si fuera un dato.", "Nadie presenta pruebas, solo se apela a que todos lo creen.", "Pide el dato: ¿quién lo comprobó y cómo?"),
        ("Descartar un dato por ser accesorio y creer que es falso.", "Accesorio no significa falso: solo significa que no es lo principal.", "Distingue entre importancia y verdad."),
    ],
    T=[
        ("abc", "{F} ¿Qué cambia según la nota?", "El lugar de la feria", "El día de la semana de la feria", "El nombre de la feria", "La primera oración indica que cambiará de lugar."),
        ("ab", "{F} ¿En qué calle se instalará?", "Los Pinos", "Sur", "La nota nombra la calle Los Pinos."),
        ("=", "{F} Si la feria funciona de 8:00 a 14:00, ¿cuántas horas dura?", "14-8", "De 8 a 14 hay 6 horas, porque 14 menos 8 es 6.", "horas"),
        ("abc", "{F} ¿Qué frase es una opinión disfrazada de hecho?", "Todo el mundo sabe que ese lugar es mucho mejor", "Los vecinos podrán llegar en el bus 12", "El toldo es azul", "Apela a lo que «todos saben» sin dar datos."),
        ("ab", "{F} ¿Qué dato es accesorio?", "El color del toldo del presidente", "El horario", "El color del toldo no ayuda a entender el cambio."),
        ("abc", "{F} ¿Qué bus permite llegar según la nota?", "El bus 12", "El bus 405", "El bus 7", "La última oración de la nota indica qué bus permite llegar."),
        ("ab", "{F} «El toldo del presidente es azul», ¿qué es?", "Un hecho accesorio", "Una opinión", "Es comprobable, pero no es lo central."),
        ("abc", "{F} ¿Cuál es información relevante para quien quiere ir a la feria?", "Día, calle y horario", "El color del toldo", "Quién es el presidente", "Con esos datos puede organizarse para llegar."),
        ("ab", "{F} ¿Qué palabra de la nota muestra un juicio?", "mejor", "bus", "«Mucho mejor» compara según un gusto."),
        ("abc", "Frase de ejemplo: «Es evidente que esa calle es peligrosa». ¿Qué conviene preguntar?", "¿Qué datos prueban que lo es?", "¿Cuántas letras tiene?", "¿Quién la leyó primero?", "Hay que pedir datos que respalden el juicio."),
        ("ab", "Oración de ejemplo: «El taller es en la sede, el lunes a las 18:00, y el expositor usa una camisa roja». ¿Qué dato es accesorio?", "La camisa roja", "La hora", "La camisa no cambia lo que se necesita saber del taller."),
        ("abc", "Oración de ejemplo: «Nadie duda de que ese candidato ganará». ¿Qué tipo de frase es?", "Una opinión disfrazada de hecho", "Un hecho comprobado", "Un dato de fecha", "No presenta datos comprobables, solo certeza sobre algo que nadie probó."),
        ("ab", "Una nota dice «La obra empezó el lunes». ¿Es relevante conocer el día de inicio?", "Sí, si se quiere saber desde cuándo hay molestias", "No, es un detalle accesorio", "Es un dato central del hecho: cuándo comenzó."),
    ],
    ctx=("abc", "Una publicación de ejemplo dice: «Mañana se corta el tránsito en la avenida Central por una maratón, de 7:00 a 10:00. Esa maratón es absurda y todo el mundo lo sabe». Para avisar a otros, ¿qué conviene compartir?", "El corte de tránsito mañana en la avenida Central de 7:00 a 10:00", "Que la maratón es absurda", "Que todo el mundo lo sabe", "Lo útil y comprobable es el corte, el lugar y el horario."),
    sc=[("¿Qué es información accesoria?", "Un detalle que no cambia lo esencial", "No es falsa, solo no es lo central."),
        ("¿Cómo reconozco una opinión disfrazada de hecho?", "Usa «todo el mundo sabe» sin dar datos", "No presenta pruebas ni datos comprobables."),
        ("En Lenguaje EPJA: ¿qué es la información relevante de una nota?", "La necesaria para entender el hecho principal", "Sin ella se pierde lo esencial.")],
    op=("Lee esta nota de ejemplo: «El consultorio atenderá el viernes con horario especial, de 9:00 a 13:00. La recepcionista usa un delantal verde. Todos saben que el consultorio es el mejor de la comuna». Escribe: 1) dos datos relevantes, 2) un dato accesorio y 3) la opinión disfrazada, explicando por qué lo es.",
        "Relevantes: viernes; de 9:00 a 13:00. Accesorio: el delantal verde. Opinión disfrazada: «Todos saben que es el mejor de la comuna», porque no entrega datos de dónde sale.",
        ["nombra dos datos relevantes", "nombra uno accesorio", "explica la opinión disfrazada"],
        ["tres respuestas breves"],
        ["mezclar relevante con accesorio", "no explicar la razón"],
        "Pregunta: «¿Si saco este dato, se entiende igual lo principal?»."),
    reinforce="Marca en una nota breve la información relevante y tacha un detalle accesorio.",
    extend="Escribe una nota con un dato accesorio y una opinión disfrazada y pide que otra persona las encuentre.",
)

build(
    O, 5, F5,
    use="Hoy reviso un mensaje reenviado: distingo qué parte es un hecho, cuál es una opinión y cómo comprobar antes de compartir.",
    prior=["Reconozco hechos y opiniones.", "Sé detectar opiniones disfrazadas.", "He recibido mensajes reenviados por celular o redes."],
    explain=[
        "Muchos mensajes llegan reenviados por celular y no se sabe quién los escribió. Un mensaje así puede traer un supuesto hecho, una opinión y una presión para que lo compartas. Antes de reenviar, conviene comprobar.",
        "Hay señales de alerta: no dice quién lo escribió ni de dónde sale, usa palabras como «urgente» o «antes de que sea tarde», tiene frases que juzgan, como «es una vergüenza», y pide reenviarlo a todos. Eso no prueba que sea falso, pero indica que debes revisarlo.",
        "Para comprobar, busca la información en el canal oficial de la institución que se nombra: su sitio, su teléfono o un aviso en el lugar. Si no puedes confirmarlo, no lo reenvíes. Así cuidas a otras personas de la confusión. Tu juicio y tu experiencia cuentan.",
    ],
    vocab=[("reenviar", "mandar a otras personas un mensaje que recibiste"), ("señal de alerta", "pista que indica que algo merece revisarse"), ("canal oficial", "medio por el cual una institución informa de forma segura"), ("confirmar", "comprobar que algo es cierto")],
    worked=[
        ("Separar el mensaje", "Mensaje de ejemplo (inventado): «ALERTA: mañana se corta la luz en toda la región. Qué abandono. ¡Pásalo a tus conocidos ya!»", ["Posible hecho: «mañana se corta la luz en toda la región», que se comprueba con la empresa o la institución.", "Opinión: «Qué abandono».", "Presión: «¡Pásalo a tus conocidos ya!»."], "Hay un dato por comprobar, una opinión y una presión por compartir."),
        ("Señales de alerta", "El mismo mensaje de la luz.", ["No dice quién lo escribió.", "Usa «ALERTA» y «ya».", "Pide pasarlo a todos."], "Son tres señales de alerta: sin autor, urgencia y presión."),
    ],
    mistakes=[
        ("Reenviar el mensaje por si acaso.", "Si es falso, se propaga la confusión.", "Comprueba en un canal oficial antes de compartir."),
        ("Decir que el mensaje es falso solo por tener señales de alerta.", "Las señales piden revisar, no prueban que sea falso.", "Confirma con la institución y recién concluye."),
    ],
    T=[
        ("abc", "{F} ¿Qué afirma el mensaje que pasará?", "Que mañana cierran todos los consultorios", "Que mañana abren más consultorios", "Que se baja el costo de la atención", "La primera frase del mensaje afirma el cierre."),
        ("ab", "{F} «Es una vergüenza», ¿es hecho u opinión?", "Opinión", "Hecho", "«Vergüenza» expresa un juicio, no un dato comprobable."),
        ("abc", "{F} ¿Qué pide el mensaje al final?", "Reenviarlo a todos los contactos", "Llamar a un amigo", "Escribir una carta", "El mensaje pide compartirlo con todos los contactos y con urgencia."),
        ("ab", "{F} ¿El mensaje dice quién lo escribió?", "No", "Sí, un consultorio", "No hay ningún autor ni fuente mencionados."),
        ("abc", "{F} ¿Cuál es una señal de alerta del mensaje?", "Usa «URGENTE» y presiona para reenviar", "Tiene signos de exclamación en el cierre", "Habla de consultorios", "La urgencia y la presión son estrategias para que lo compartas sin pensar."),
        ("ab", "{F} ¿Qué conviene hacer antes de reenviarlo?", "Confirmarlo en un canal oficial", "Reenviarlo a quien más lo necesite", "La confirmación evita difundir información falsa."),
        ("{F} ¿Qué palabra del mensaje indica urgencia? (una palabra en mayúscula)", "URGENTE", "La palabra que abre el mensaje y marca la urgencia es «URGENTE»."),
        ("abc", "{F} ¿Cuál es un canal oficial de ejemplo para comprobarlo?", "Un aviso en el propio consultorio o su sitio informativo", "Otro mensaje reenviado sin autor", "Un comentario anónimo", "La institución nombrada es quien debe confirmar."),
        ("ab", "{F} Si no puedes confirmarlo, ¿qué conviene?", "No reenviarlo", "Reenviarlo igual", "Lo que no se confirma no debe difundirse."),
        ("abc", "Mensaje de ejemplo: «El municipio informa que el jueves habrá vacunación en la sede, de 10:00 a 13:00. Más datos en el sitio del municipio». ¿Qué tiene de mejor?", "Nombra quién informa, día, hora y dónde confirmar", "Usa palabras de miedo", "Pide reenviar a todos", "Tiene datos comprobables y una fuente."),
        ("ab", "Mensaje de ejemplo: «Es lo peor que ha pasado, ¡compártelo ya!». ¿Qué trae?", "Opinión y presión, sin datos", "Solo hechos comprobables", "No hay datos que se puedan verificar."),
        ("abc", "¿Por qué los mensajes falsos usan palabras como «URGENTE»?", "Para que se comparta sin revisar", "Para que sean más cortos", "Para que se vean bonitos", "La urgencia apura a la persona y evita que compruebe."),
        ("ab", "Una persona dice: «Lo vi en tres mensajes, así que es cierto». ¿Es suficiente?", "No, porque reenvíos repetidos no son una comprobación", "Sí, porque muchos lo dicen", "Que muchos lo repitan no lo vuelve cierto; hay que confirmarlo en la fuente."),
    ],
    ctx=("abc", "En un grupo de vecinos aparece este mensaje de ejemplo: «Mañana suspenden la recolección de basura en todo el sector. ¡Avisa a todos!». Sin autor ni fuente. ¿Qué conviene hacer?", "Consultar el aviso oficial del servicio de aseo antes de avisar", "Reenviarlo de inmediato a todos", "Ignorarlo y no mirar más", "Primero se comprueba; luego se informa lo confirmado."),
    sc=[("En Lenguaje EPJA: ¿qué señales de alerta trae un mensaje reenviado dudoso?", "Sin autor, urgencia y pide reenviar", "Son pistas para revisar antes de compartir."),
        ("¿Qué hago antes de reenviar?", "Confirmo en un canal oficial", "Así evito difundir información sin comprobar."),
        ("¿Qué hago si no logro confirmar?", "No reenvío", "Callar es mejor que difundir una duda.")],
    op=("Lee este mensaje de ejemplo: «ATENCIÓN: mañana no habrá clases en toda la comuna. Qué desorden el de las autoridades. Pásalo, que nadie se entere tarde». Escribe: 1) el posible hecho, 2) la opinión, 3) dos señales de alerta y 4) a quién o a qué canal le preguntarías para confirmar.",
        "Posible hecho: mañana no habrá clases en toda la comuna. Opinión: «Qué desorden el de las autoridades». Señales: sin autor; ATENCIÓN y «pásalo». Confirmación: aviso oficial de la escuela o del municipio.",
        ["separa hecho y opinión", "nombra dos señales de alerta", "indica un canal oficial"],
        ["cuatro respuestas breves"],
        ["reenviar sin comprobar", "no nombrar canal"],
        "Pregunta: «¿Quién debería confirmar esto de verdad?»."),
    reinforce="Revisa un mensaje reenviado y anota si tiene autor, fecha y fuente.",
    extend="Escribe un mensaje de ejemplo con las tres señales de alerta y otro bien hecho, y explica la diferencia.",
)

build(
    O, 6, F6,
    use="Hoy reviso una columna con hechos y opiniones mezclados, evalúo si las opiniones tienen respaldo y repaso lo logrado en la unidad.",
    prior=["Distingo hechos y opiniones.", "Reconozco información relevante y accesoria.", "Sé que una opinión debe tener respaldo."],
    explain=[
        "Una columna mezcla hechos y opiniones, y está bien. Lo importante es poder separarlos y ver cuáles opiniones tienen respaldo. Una opinión está respaldada si se apoya en un hecho comprobable y en una razón que tenga sentido.",
        "En la columna de ejemplo, el hecho de que el taller pasó de 25 a 40 inscritos respalda la opinión de que fue una buena noticia, aunque «estupenda» siga siendo un juicio. También respalda la petición de comprar más computadores el dato de que hay uno por cada dos personas.",
        "En cambio, «quienes se oponen no entienden nada» no tiene respaldo: descalifica a las personas en lugar de dar razones. Una buena opinión se apoya en datos y respeta a quien piensa distinto.",
    ],
    vocab=[("respaldo", "datos o razones que sostienen una opinión"), ("descalificar", "decir que alguien no vale en lugar de dar razones"), ("columna", "texto de opinión que firma quien lo escribe"), ("oponerse", "estar en contra de algo")],
    worked=[
        ("Opinión con respaldo", "Columna de ejemplo: «La junta organizó 4 ferias este año, una más que el año pasado. Creo que debería armar una feria cada mes, porque los puestos se llenan en cada una. Los que dicen lo contrario no saben nada».", ["Opinión: debería armarse una feria cada mes.", "Respaldo: los puestos se llenan en cada una.", "El dato se relaciona con lo que se pide."], "La opinión tiene respaldo."),
        ("Opinión sin respaldo", "La misma columna de las ferias.", ["Frase: «Los que dicen lo contrario no saben nada».", "No da dato ni razón y habla mal de quienes piensan distinto.", "No se puede comprobar ni debatir."], "Es una opinión sin respaldo que descalifica."),
    ],
    mistakes=[
        ("Creer que una opinión con un dato al lado ya está respaldada.", "El dato debe relacionarse con lo que se pide.", "Revisa que el dato apoye de verdad la opinión."),
        ("Dar por respaldada una opinión porque suena segura.", "Decir «sin duda» no es una razón.", "Pide datos o razones concretas."),
    ],
    T=[
        ("=", "{F} ¿Cuántos inscritos más tiene el taller este año que el año pasado?", "40-25", "40 menos 25 es 15 inscritos más.", "inscritos"),
        ("abc", "{F} ¿Cuántos inscritos tiene el taller este año?", "40", "25", "15", "La columna dice que este año tiene 40."),
        ("ab", "{F} «Es una noticia estupenda», ¿es hecho u opinión?", "Opinión", "Hecho", "«Estupenda» es un juicio sobre un dato."),
        ("abc", "{F} ¿Qué dato respalda que la sede compre más computadores?", "Hay un computador por cada dos personas inscritas", "El año pasado hubo 25 inscritos", "La noticia es estupenda", "La relación de uno por dos muestra que faltan equipos."),
        ("ab", "{F} «Quienes se oponen no entienden nada», ¿tiene respaldo?", "No, descalifica sin dar razones", "Sí, tiene datos", "No entrega ningún dato ni razón."),
        ("abc", "{F} ¿Qué es lo mejor que se puede hacer con esa frase al revisar la columna?", "Reconocerla como opinión sin respaldo", "Tomarla como un hecho", "Copiarla en una carta", "La frase no tiene razones comprobables."),
        ("ab", "{F} «El año pasado el taller tuvo 25 inscritos», ¿es hecho u opinión?", "Hecho", "Opinión", "Se puede comprobar con la lista del taller."),
        ("{F} ¿Con qué palabra comienza la opinión sobre los computadores? (una palabra)", "Pienso", "La columna dice «Pienso que la sede debería comprar...»."),
        ("abc", "{F} ¿Qué haría más fuerte la petición de comprar computadores?", "Un dato del costo y de cuántos computadores faltan", "Más adjetivos", "Repetir «sin duda»", "Un dato concreto apoya el pedido."),
        ("ab", "{F} ¿«Sin duda» es una razón?", "No, es una expresión de seguridad", "Sí, es una prueba", "Decir que no hay duda no demuestra nada."),
        ("abc", "Columna de ejemplo: «La feria debería abrir un día más, porque el sábado no alcanza a atender a toda la gente que llega». ¿Cuál es el respaldo?", "Que el sábado no alcanza a atender a toda la gente", "Que la feria debería abrir", "Que es un día más", "El respaldo es la razón que sigue a «porque»."),
        ("ab", "Frase de ejemplo: «El bus es pésimo, no sé por qué existe». ¿Tiene respaldo?", "No, no da datos ni razones", "Sí, porque es contundente", "Solo expresa molestia, sin datos ni razones."),
        ("abc", "Después de esta unidad, ¿qué es lo mejor que puedes hacer con una nota que mezcla ambas cosas?", "Separar los hechos de las opiniones y revisar el respaldo", "Quedarte solo con las opiniones", "Ignorar los datos", "Separar los hechos de las opiniones permite evaluar con claridad lo que se lee."),
    ],
    ctx=("abc", "Una radio de ejemplo dice: «Este año se plantaron 200 árboles en la comuna, el doble que el año pasado. Es hora de plantar más, porque los parques siguen con poca sombra». Quien escucha quiere repetir solo el hecho comprobable. ¿Cuál repite?", "Que este año se plantaron 200 árboles", "Que es hora de plantar más", "Que los parques tienen poca sombra", "La cifra puede verificarse en registros; «es hora de» es una opinión."),
    sc=[("¿Cuándo está respaldada una opinión?", "Cuando se apoya en un hecho y una razón", "Sin hecho ni razón, solo es una afirmación."),
        ("En Lenguaje EPJA: ¿qué significa descalificar en una columna?", "Atacar a quien piensa distinto en vez de dar razones", "Descalificar a quien piensa distinto no aporta argumentos sobre el tema."),
        ("¿Qué pasos sigo al leer una nota mixta?", "Separar hechos de opiniones y revisar el respaldo", "Separar hechos de opiniones y mirar su respaldo permite evaluar el texto con claridad.")],
    op=("Lee esta columna de ejemplo: «La biblioteca prestó 300 libros en un mes, 50 más que el mes anterior. Es un orgullo. Creo que debería tener más horario, porque hay lista de espera para varios títulos. Los que critican no leen». Haz una tabla de Hechos y Opiniones, di cuáles opiniones tienen respaldo y cuáles no, y escribe una oración con tu propia opinión sobre la biblioteca, apoyada en un hecho de la columna. Cierra con una oración sobre qué aprendiste en estas seis clases.",
        "Hechos: 300 libros en un mes; 50 más que el anterior; hay lista de espera. Opiniones: «Es un orgullo»; «debería tener más horario» (respaldada por la lista de espera); «Los que critican no leen» (sin respaldo). Mi opinión: la biblioteca funciona bien, porque prestó 50 libros más. Aprendí a separar datos de juicios.",
        ["separa hechos y opiniones", "dice cuáles tienen respaldo", "escribe una opinión con un hecho", "cierra con lo aprendido"],
        ["una tabla y dos oraciones"],
        ["tomar una opinión como hecho", "apoyar una opinión en un dato que no tiene relación"],
        "Pregunta: «¿Mi dato sirve de verdad para apoyar mi opinión?»."),
    reinforce="Elige una columna breve y anota qué opinión tiene respaldo y cuál no.",
    extend="Escribe una columna de cinco oraciones con dos hechos, dos opiniones respaldadas y una opinión sin respaldo, y pide a alguien que las encuentre.",
)

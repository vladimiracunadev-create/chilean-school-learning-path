"""Lengua y Literatura EPJA Media Nivel 1, módulo 2 (parte 1): OAD-05, analizar un texto no literario a partir de su situación comunicativa para determinar su veracidad y consistencia. Todos los textos son inventados y se leen en papel."""
from __future__ import annotations

from epja_leli_nm1_b_common import build

O = "EPJA-LELI-NM1-OAD-05"

F1 = ("Texto A (inventado), aviso pegado en la sede de la junta de vecinos «El Mirador»: «El sábado 14, a las 16:00, habrá reunión en la sede para decidir en qué se usarán los fondos de la feria. "
      "Pedimos llegar con puntualidad. A quien no pueda asistir se le entregará un resumen escrito. La directiva.» "
      "Texto B (inventado), mensaje enviado por una jefa de turno al grupo de su equipo de trabajo: «Hola, equipo. Mañana cambia el turno: entramos a las 7 y no a las 8. Confirmen con un ok. Lorena, jefa de turno.»")

F2 = ("Noticia (inventada) del boletín «Voz del Barrio»: «Nueva cancha en la plaza Los Aromos. Ayer miércoles se inauguró la cancha de la plaza, según informó la municipalidad de ejemplo en un comunicado. "
      "Asistieron unas 80 personas y se instalaron dos arcos y cuatro focos. Para el presidente de la junta de vecinos, es la mejor obra de los últimos años. "
      "Un vecino que no quiso dar su nombre aseguró que la cancha no servirá porque todos la van a ensuciar.»")

F3 = ("Noticia (inventada) de la cartelera del centro cultural «La Estación»: «Gran éxito de la obra del domingo. Se vendieron 150 entradas: 90 a público general y 70 a estudiantes. "
      "La sala, con sus 150 butacas, estuvo completa y nadie quedó de pie. La función comenzó a las 19:00 y terminó a las 20:30.»")

F4 = ("Texto 1 (inventado), mensaje reenviado en cadena: «URGENTE. El consultorio Sol Naciente cerrará mañana para siempre. Lo dijo un conocido de una funcionaria. Comparte con diez personas o perderás tu hora.» "
      "Texto 2 (inventado), comunicado en la puerta del consultorio Sol Naciente, fechado el 18 de noviembre y firmado por la dirección: «El viernes 20 el consultorio atenderá con horario reducido, de 9:00 a 13:00, "
      "por una jornada de capacitación del personal. Las horas ya agendadas se mantienen. Para consultas, acérquese al mesón de informaciones.»")

F5 = ("Aviso de trabajo (inventado): «Se necesita ayudante de bodega. Jornada de 8 horas, de lunes a viernes. Además, dos turnos de 12 horas los fines de semana. Se pide experiencia mínima de 5 años; no se requiere experiencia previa. "
      "Sueldo líquido de ejemplo: $520.000.» "
      "Cuenta de agua (inventada) de un hogar: «Consumo del mes: 14 metros cúbicos a $1.200 cada uno. Cargo fijo: $3.000. Total a pagar: $21.000.»")

F6 = ("Guion de un anuncio de la radio comunitaria «Onda Vecinal» (inventada), para leer en voz alta: «Atención, vecinas y vecinos de la población Nuevo Horizonte. Mañana jueves se cortará el agua desde las 9:00 hasta las 14:00 por trabajos en la red, "
      "según informó la empresa sanitaria de ejemplo. Se recomienda guardar agua con anticipación. Se estima que el suministro volverá a las 12:00. Gracias por su comprensión.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco la situación comunicativa de un texto: quién lo escribe, para quién, para qué y dónde circula.",
    prior=["Leo avisos, mensajes y comunicados de mi trabajo, mi barrio o mi familia.", "Sé decir de qué trata un texto.", "Distingo un mensaje formal de uno entre conocidos."],
    explain=[
        "Todo texto nace en una situación comunicativa. Tú ya la reconoces sin darte cuenta: no escribes igual a una jefatura que a un amigo. Hoy ponemos nombre a lo que haces de manera natural.",
        "La situación tiene cuatro partes. El emisor es quien escribe. El receptor es quien lee. El propósito es lo que el emisor quiere lograr: informar, convocar, pedir algo o convencer. El contexto es el lugar, el momento y el medio donde circula el texto, como un muro de la sede o un grupo de mensajes.",
        "Antes de decidir si un texto es confiable, conviene responder esas cuatro preguntas. Un aviso de la directiva en la sede y un mensaje de una jefa de turno informan, pero se escriben distinto porque cambian el emisor, el receptor y el contexto.",
    ],
    vocab=[("situación comunicativa", "conjunto de emisor, receptor, propósito y contexto de un texto"), ("emisor", "persona o grupo que escribe o dice el texto"), ("receptor", "persona o grupo a quien se dirige el texto"), ("propósito", "lo que el emisor quiere lograr con su texto")],
    worked=[
        ("Reconocer emisor y receptor", "Texto (inventado): «Se informa a los usuarios que la oficina atenderá hasta las 14:00. La administración.»", ["Busco quién firma: la administración. Ese es el emisor.", "Busco a quién se dirige: «a los usuarios». Ese es el receptor."], "Emisor: la administración. Receptor: los usuarios"),
        ("Reconocer el propósito", "Texto (inventado): «Recuerde traer cédula y certificado de residencia. No se atenderá sin documentos.»", ["Pregunto qué quiere lograr el texto: que la persona lleve sus documentos.", "Veo que da una instrucción y una advertencia."], "Propósito: indicar qué hacer y evitar que alguien vaya sin documentos"),
    ],
    mistakes=[("Creer que el emisor es siempre quien «dice la noticia».", "El emisor es quien firma o produce el texto, no la persona de la que se habla.", "Busca la firma, el sello o la voz que dice «informamos» o «pedimos»."),
              ("Pensar que cualquier texto sirve para cualquier lugar.", "El contexto cambia el modo de escribir: un mensaje entre colegas no es lo mismo que un aviso para todo el barrio.", "Pregunta dónde circula el texto y quién lo leerá.")],
    T=[
        ("abc", "{F} ¿Quién es el emisor del Texto A?", "La directiva de la junta de vecinos", "Lorena, la jefa de turno", "Cada persona que lee el aviso", "El texto A termina con la firma «La directiva»."),
        ("ab", "{F} ¿A quién se dirige el Texto A?", "A las personas del barrio que pasan por la sede y leen el aviso", "Solo a las personas de la directiva", "El aviso invita a asistir y ofrece un resumen a quien no pueda."),
        ("{F} Escribe la hora en que empieza la reunión del Texto A, tal como aparece en el texto.", "16:00", "El Texto A dice que la reunión es a las 16:00."),
        ("abc", "{F} ¿Cuál es el propósito del Texto A?", "Convocar a una reunión y avisar que se decidirá el uso de fondos", "Vender entradas para una feria", "Contar una historia de la feria", "Convoca a una reunión con fecha, hora y lugar."),
        ("abc", "{F} ¿Cuál es el propósito del Texto B?", "Avisar un cambio de horario y pedir que confirmen", "Invitar a una fiesta del equipo", "Pedir una opinión sobre el sueldo", "El mensaje anuncia que entran a las 7 y pide confirmar con un ok."),
        ("ab", "{F} ¿Cuál texto usa un tono más cercano, entre personas que se conocen?", "El Texto B, que empieza con «Hola, equipo»", "El Texto A, que firma «La directiva»", "El saludo «Hola, equipo» muestra confianza entre quienes trabajan juntos."),
        ("{F} Si pegaras el Texto B en el muro de la sede vecinal, ¿serviría para los vecinos? Responde sí o no.", "no", "Habla de un turno de trabajo que los vecinos no tienen."),
        ("abc", "{F} ¿Qué parte de la situación comunicativa muestra la firma «Lorena, jefa de turno»?", "Quién es el emisor y qué rol tiene", "Cuál es el contexto donde circula el aviso", "A quién se dirige el texto A", "La firma dice quién escribe y desde qué cargo."),
        ("Un aviso dice: «La reunión comienza a las 16:00 y dura 90 minutos». ¿A qué hora termina? Escribe la hora con cuatro cifras, por ejemplo 18:00.", "17:30", "Noventa minutos son una hora y media, de 16:00 a 17:30."),
        ("ab", "{F} Un vecino dice que el Texto A no sirve para quien no puede ir. ¿Tiene razón?", "No: el texto promete un resumen escrito para quien no asista", "Sí: el texto no dice nada de quien no puede asistir", "La frase «se le entregará un resumen escrito» considera a esas personas."),
        ("abc", "{F} ¿Por qué el Texto A y el Texto B se escriben de modo distinto?", "Porque cambian el emisor, el receptor y el contexto", "Porque uno es verdadero y el otro es falso", "Porque el Texto B es más antiguo que el A", "Cada texto responde a una situación comunicativa diferente."),
        ("abc", "Un comercio pega este cartel (inventado): «Cerrado por inventario el lunes. Disculpe las molestias.» ¿Quién es el receptor?", "Las personas que van a comprar al comercio", "El equipo de trabajo del comercio", "La municipalidad que fiscaliza", "Un cartel en la puerta se dirige a quienes llegan como clientes."),
        ("ab", "Un grupo de trabajo recibe este mensaje: «Mañana no hay camión; avisen a los clientes». Si lo reenviaran a un cliente sin cambios, ¿qué pasaría?", "El cliente no sabría quién avisa ni a quién se le pide algo", "Nada: el mensaje serviría igual para todos", "El texto fue escrito para el equipo y confunde a otro receptor."),
    ],
    ctx=("abc", "Te llega este mensaje: «Hola, vecinos. Mañana se corta el agua de 9:00 a 12:00. Guarden agua. Comité de agua». Quieres saber qué tipo de situación es. ¿Qué respuesta describe mejor su emisor y su receptor?", "Emisor: el comité de agua. Receptor: los vecinos", "Emisor: los vecinos. Receptor: el comité de agua", "Emisor: la persona que reenvía. Receptor: nadie en especial", "Firma el comité y saluda a los vecinos, a quienes dirige el aviso."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es el propósito de un texto?", "Lo que el emisor quiere lograr con él", "El propósito es la intención del emisor: informar, convocar o convencer."),
        ("En Lengua y Literatura de EPJA: ¿qué es el receptor de un texto?", "La persona o el grupo a quien se dirige", "El receptor es quien lee o escucha el mensaje."),
        ("En Lengua y Literatura de EPJA: ¿por qué conviene reconocer la situación comunicativa antes de evaluar un texto?", "Porque el emisor, el receptor y el contexto ayudan a entender qué quiere lograr el texto", "Saber quién escribe y para qué da pistas para juzgar el texto.")],
    op=("Lee otra vez el Texto A y el Texto B: {F} Escribe en tu cuaderno, para cada texto, quién es el emisor, quién es el receptor y cuál es el propósito. Después escribe una frase que cambie el Texto B para que sirva en un aviso del barrio, por ejemplo sobre un cambio de horario de la feria.",
        "Texto A: emisor, la directiva; receptor, las personas del barrio; propósito, convocar a una reunión. Texto B: emisor, Lorena; receptor, su equipo; propósito, avisar un cambio de turno. Cambio: «Vecinas y vecinos: el sábado la feria abrirá a las 9:00 y no a las 10:00. La directiva.»",
        ["identifica emisor, receptor y propósito de cada texto", "usa datos de los textos", "su frase nueva cambia el tono y el receptor"],
        ["seis datos escritos y una frase nueva"],
        ["confundir emisor con receptor", "copiar la frase sin adaptar el tono"],
        "Pregunta: «¿Quién escribe, a quién y para qué?»."),
    reinforce="Mira un mensaje que recibiste hoy y escribe quién lo envía, a quién se dirige y qué quiere lograr.",
    extend="Elige un aviso que veas en tu comunidad y cuéntale a otra persona cómo cambiaría si lo escribieras para un grupo de amigos.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy distingo hechos de opiniones, reconozco la fuente de los datos y uso estrategias para leer con atención.",
    prior=["Reconozco emisor, receptor y propósito.", "Sé que no todo lo que leo es igual de confiable.", "Puedo subrayar datos importantes."],
    explain=[
        "Un hecho es algo que ocurrió o que se puede comprobar, como una fecha, una cantidad o un lugar. Una opinión es lo que alguien piensa o siente, y no se puede comprobar de la misma manera: «es la mejor obra» es una opinión.",
        "La veracidad es qué tan cierta es la información. Para juzgarla miramos la fuente, que es de dónde viene el dato: un comunicado firmado, una persona con nombre o alguien que no se identifica. La consistencia es que el texto no se contradiga ni tenga cifras que no cuadran.",
        "Para leer con atención usa tres momentos. Antes de leer, mira el título y pregúntate de qué podría tratar. Mientras lees, subraya fechas, cantidades y nombres. Al terminar, resume el texto con tus palabras y separa lo que es hecho de lo que es opinión.",
    ],
    vocab=[("hecho", "algo que ocurrió o que se puede comprobar"), ("opinión", "lo que alguien piensa o siente sobre algo"), ("fuente", "persona o documento de donde sale la información"), ("consistencia", "que el texto no se contradiga y sus datos cuadren")],
    worked=[
        ("Separar hecho y opinión", "Frase (inventada): «El jueves se pavimentó la calle, que quedó preciosa.»", ["«El jueves se pavimentó la calle» se puede comprobar: es un hecho.", "«Quedó preciosa» es lo que alguien siente: es una opinión."], "Hecho: se pavimentó el jueves. Opinión: quedó preciosa"),
        ("Valorar la fuente", "Frase (inventada): «Según el comunicado firmado por la municipalidad de ejemplo, el bus nuevo parte a las 7:00». Otra frase: «Dicen que el bus parte a las 7:00».", ["La primera dice quién informa y menciona un documento firmado.", "La segunda no dice quién lo dice: no se puede revisar."], "La primera fuente es más confiable que «dicen que»"),
    ],
    mistakes=[("Creer que si una frase suena segura, es un hecho.", "Una opinión puede decirse con mucha seguridad y seguir siendo opinión.", "Pregunta: ¿esto se puede comprobar con un dato, un documento o un registro?"),
              ("Pensar que un dato sin fuente es falso.", "Sin fuente no sabemos si es cierto o no: queda sin comprobar.", "Anota «sin fuente» y busca confirmar el dato en un documento o una institución.")],
    T=[
        ("abc", "{F} ¿Cuál de estas frases es un hecho?", "Se inauguró la cancha el miércoles.", "Es la mejor obra de los últimos años.", "Todos la van a ensuciar.", "La inauguración en una fecha se puede comprobar; las otras son juicios."),
        ("ab", "{F} La frase «es la mejor obra de los últimos años», ¿es un hecho o una opinión?", "Una opinión, porque expresa un juicio de alguien", "Un hecho, porque lo dijo una autoridad", "No se puede comprobar con un dato: depende de lo que piense quien habla."),
        ("{F} ¿Cuántas personas, aproximadamente, asistieron según la noticia? Escribe solo el número.", "80", "La noticia dice «unas 80 personas»."),
        ("abc", "{F} ¿Cuál es la fuente de la información de la inauguración?", "Un comunicado de la municipalidad de ejemplo", "Un vecino que no quiso dar su nombre", "El presidente de la junta de vecinos", "La noticia dice «según informó la municipalidad en un comunicado»."),
        ("ab", "{F} La frase del vecino que no dio su nombre, ¿es una fuente fácil de comprobar?", "No, porque no sabemos quién es y es una predicción", "Sí, porque aparece en la noticia", "Aparecer en un texto no basta: no se puede revisar quién lo dijo."),
        ("=", "{F} Se instalaron dos arcos y cuatro focos. ¿Cuántos elementos se instalaron en total?", "2 + 4", "La noticia suma dos arcos y cuatro focos.", " elementos"),
        ("abc", "{F} ¿Qué frase del texto adelanta algo que todavía no ocurrió y no se puede comprobar hoy?", "«La cancha no servirá porque todos la van a ensuciar»", "«Ayer miércoles se inauguró la cancha»", "«Se instalaron dos arcos y cuatro focos»", "Es una predicción del vecino sobre el futuro."),
        ("abc", "Antes de leer una noticia con el título «Cierran el puente por una semana», ¿qué estrategia sirve para preparar la lectura?", "Pensar de qué podría tratar y qué datos esperas encontrar", "Leer solo la última línea", "Copiar el título sin leer el texto", "Anticipar el contenido ayuda a leer con un propósito."),
        ("abc", "Mientras lees una noticia, ¿cuál de estas acciones ayuda a revisar la consistencia?", "Subrayar fechas y cantidades para compararlas", "Saltarse los números", "Leer solo el título", "Subrayar datos permite ver si se contradicen."),
        ("ab", "Camila dice que si un texto trae una cifra, ya es verdadero. ¿Tiene razón?", "No: hay que revisar de dónde viene la cifra", "Sí: una cifra siempre se comprueba sola", "Una cifra sin fuente puede estar equivocada o inventada."),
        ("abc", "{F} ¿Cuál es un buen resumen de la noticia con tus palabras?", "Se inauguró una cancha en la plaza, con dos arcos y cuatro focos, y hay opiniones a favor y en contra", "La cancha es la mejor obra y nadie opina distinto", "La municipalidad pidió cerrar la plaza", "El resumen recoge los datos y menciona ambas opiniones."),
        ("abc", "{F} Si la noticia dijera «80 personas» en un párrafo y «200 personas» en otro, ¿qué faltaría?", "Consistencia, porque las cifras se contradicen", "Opinión, porque habría un juicio", "Fuente, porque faltaría el título", "Dos cifras distintas para lo mismo muestran contradicción."),
        ("ab", "{F} Rosa quiere citar la frase «la cancha no servirá» como un dato sobre la cancha. ¿Es buena idea?", "No: es una opinión sin fuente identificada", "Sí: quedó escrita en un boletín", "Una opinión anónima no demuestra nada sobre la cancha."),
    ],
    ctx=("abc", "Un compañero de trabajo comenta: «En el casino sirven la peor comida de la ciudad y además almuerzan 200 personas». ¿Qué parte de su frase es un hecho que se podría comprobar?", "Que almuerzan 200 personas", "Que es la peor comida", "Que la ciudad es grande", "La cantidad se puede contar; «la peor» es un juicio personal."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué diferencia hay entre un hecho y una opinión?", "El hecho se puede comprobar; la opinión expresa lo que alguien piensa", "El hecho se verifica con datos; la opinión es un juicio."),
        ("En Lengua y Literatura de EPJA: ¿qué es la fuente de una información?", "De dónde o de quién viene el dato", "La fuente permite revisar si la información es confiable."),
        ("En Lengua y Literatura de EPJA: ¿qué significa que un texto sea consistente?", "Que no se contradice y sus datos cuadran", "La consistencia revisa que las partes del texto no se contradigan.")],
    op=("Lee la noticia de nuevo: {F} Copia en tu cuaderno dos hechos y dos opiniones de la noticia. Después escribe, en dos oraciones, si la noticia es suficiente para saber si la cancha es buena o si falta información, y qué dato pedirías.",
        "Hechos: se inauguró ayer; asistieron unas 80 personas. Opiniones: «es la mejor obra»; «todos la van a ensuciar». Falta saber cuánto costó y cuántas personas la usan; pediría el comunicado completo de la municipalidad.",
        ["separa dos hechos y dos opiniones", "justifica con el texto", "nombra un dato que falta"],
        ["cuatro frases clasificadas y dos oraciones"],
        ["clasificar una opinión como hecho", "no decir qué dato falta"],
        "Pregunta: «¿Esto se puede comprobar o es un juicio?»."),
    reinforce="Elige un mensaje de tu teléfono y subraya un hecho y una opinión.",
    extend="Escribe tres frases sobre tu lugar de trabajo: una que sea hecho, una que sea opinión y una que no puedas comprobar sin más datos.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy sigo, paso a paso, una pauta para revisar la veracidad y la consistencia de una noticia.",
    prior=["Distingo hechos de opiniones.", "Sé reconocer la fuente de un dato.", "Sé sumar y restar."],
    explain=[
        "Revisar un texto no literario se vuelve más fácil con una pauta de cinco pasos. Primero, reconoce la situación comunicativa: quién escribe y para qué. Segundo, separa hechos de opiniones.",
        "Tercero, busca la fuente de cada dato importante. Cuarto, revisa la consistencia: las cifras que se pueden sumar o restar deben cuadrar, y las fechas y horas no deben contradecirse entre sí. Quinto, decide si el texto es confiable, dudoso o no se puede comprobar.",
        "Una cifra que no cuadra no prueba que el emisor mienta: puede ser un error. Pero sí muestra que el texto no es consistente, y por eso hay que pedir confirmación antes de repetirlo o tomar una decisión.",
    ],
    vocab=[("pauta", "lista de pasos para revisar algo"), ("contradicción", "dos afirmaciones que no pueden ser ciertas a la vez"), ("cifra", "número o cantidad que aparece en un texto"), ("confirmar", "comprobar un dato con otra fuente")],
    worked=[
        ("Revisar una suma", "Texto (inventado): «Asistieron 60 personas: 35 mujeres y 20 hombres».", ["Sumo las partes: 35 + 20 = 55.", "El total dice 60, pero las partes suman 55."], "No cuadra: faltan 5 personas en el desglose"),
        ("Revisar una hora", "Texto (inventado): «La charla empieza a las 18:00 y dura dos horas, por eso terminará a las 19:30».", ["Dos horas después de las 18:00 son las 20:00.", "El texto dice 19:30: se contradice."], "Hora de término inconsistente"),
    ],
    mistakes=[("Confiar en un texto porque tiene muchas cifras.", "Las cifras dan apariencia de precisión, pero pueden no cuadrar entre sí.", "Suma, resta y compara las cifras antes de creer."),
              ("Pensar que una contradicción siempre significa mentira.", "Puede ser un error de escritura.", "Di «no es consistente» y pide confirmación a la fuente.")],
    T=[
        ("=", "{F} Según la noticia, 90 entradas fueron de público general y 70 de estudiantes. ¿Cuántas entradas suman entre ambas?", "90 + 70", "Se suman las entradas de los dos grupos.", " entradas"),
        ("abc", "{F} La noticia dice que se vendieron 150 entradas. ¿Cuadra con la suma del desglose?", "No, porque el desglose suma más que 150", "Sí, porque 90 más 70 es 150", "No se puede revisar sin otra fuente", "El desglose suma 160, que no es 150."),
        ("=", "{F} ¿Cuántas entradas de diferencia hay entre el total del desglose y las 150 que dice la noticia?", "160 - 150", "El desglose suma 160 y el total anunciado es 150.", " entradas"),
        ("abc", "{F} ¿Cuántas butacas tiene la sala según el texto?", "150", "160", "70", "La noticia dice «con sus 150 butacas»."),
        ("ab", "{F} Si se vendieron más entradas que butacas y nadie quedó de pie, ¿qué ocurre con la consistencia?", "El texto se contradice", "El texto es consistente", "Con más entradas que butacas, alguien habría quedado de pie."),
        ("{F} La función comenzó a las 19:00 y terminó a las 20:30. ¿Cuántos minutos duró? Escribe solo el número.", "90", "De 19:00 a 20:30 pasan una hora y media."),
        ("abc", "{F} ¿Qué frase de la noticia es una opinión?", "«Gran éxito de la obra del domingo»", "«Se vendieron 150 entradas»", "«La función comenzó a las 19:00»", "Decir que fue un gran éxito es un juicio."),
        ("abc", "En la pauta de cinco pasos, ¿qué se hace en el cuarto paso?", "Revisar que cifras, fechas y horas no se contradigan", "Reconocer quién escribe el texto", "Decidir si se comparte el texto", "El cuarto paso revisa la consistencia."),
        ("abc", "Un texto dice: «Llegaron 45 personas: 25 de la mañana y 20 de la tarde». ¿Es consistente la suma?", "Sí, porque 25 más 20 es 45", "No, porque suman 40", "No, porque suman 50", "La suma 25 + 20 es igual a 45."),
        ("ab", "{F} Un amigo propone repetir en un mensaje que hubo «gran éxito» sin revisar las cifras. ¿Qué conviene hacer antes?", "Pedir al centro cultural la cifra exacta de entradas vendidas", "Compartirlo, porque es una cartelera oficial", "Aunque sea una cartelera, las cifras no cuadran y conviene confirmar."),
        ("abc", "{F} Si el centro cultural responde que se vendieron 150 entradas en total, ¿qué parte de la noticia estaba equivocada?", "El desglose de 90 y 70", "La hora de la función", "El nombre del centro cultural", "El total oficial corrige el desglose, que sumaba 160."),
        ("abc", "Tras una pauta de cinco pasos, un texto tiene fuente clara pero una cifra que no cuadra. ¿Cuál es la mejor decisión?", "Considerarlo dudoso hasta confirmar la cifra", "Darlo por completamente falso", "Darlo por totalmente confiable", "La fuente aporta confianza, pero la cifra exige confirmación."),
        ("ab", "Un texto dice que una reunión empieza a las 10:00 y dura 3 horas, y termina «a las 12:00». ¿Es consistente?", "No: tres horas después de las 10:00 son las 13:00", "Sí: termina a las 12:00", "De las 10:00 a las 12:00 pasan solo dos horas."),
    ],
    ctx=("abc", "Una boleta de compra de ejemplo dice: «3 sacos de cemento a $8.000 cada uno: total $27.000». Revisa la cifra. ¿Es consistente?", "No, porque tres sacos a $8.000 suman $24.000", "Sí, porque 3 por 8.000 da 27.000", "No se puede saber sin ver los sacos", "Tres veces 8.000 es 24.000, no 27.000."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué se revisa al analizar la consistencia de un texto?", "Que cifras, fechas y afirmaciones no se contradigan", "La consistencia compara las partes del texto entre sí."),
        ("En Lengua y Literatura de EPJA: ¿qué hacer cuando una cifra de un texto no cuadra?", "Pedir confirmación a la fuente antes de repetirla", "Una cifra que no cuadra necesita confirmación."),
        ("En Lengua y Literatura de EPJA: ¿qué se hace en el paso de buscar la fuente?", "Identificar de dónde viene cada dato importante", "La fuente permite revisar el origen del dato.")],
    op=("Usa la pauta de cinco pasos con esta noticia: {F} Escribe en tu cuaderno una frase por cada paso: quién escribe y para qué, un hecho y una opinión, la fuente, la cifra que no cuadra y tu decisión final.",
        "1. Escribe un centro cultural para promocionar su función. 2. Hecho: se vendieron 150 entradas; opinión: gran éxito. 3. No se indica una fuente de las cifras. 4. 90 más 70 suman 160, no 150. 5. Es dudosa hasta confirmar la cifra exacta.",
        ["usa los cinco pasos", "cita datos de la noticia", "concluye con una decisión justificada"],
        ["cinco frases"],
        ["no comprobar la suma", "decidir sin justificar"],
        "Pregunta: «¿Qué cifra no cuadra y qué harías para confirmarla?»."),
    reinforce="Revisa la suma de la última boleta o cuenta de tu hogar y comprueba si cuadra.",
    extend="Escribe una noticia inventada de cuatro líneas con una cifra que no cuadra e invita a otra persona a encontrarla.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: comparo dos textos sobre el mismo tema y decido cuál es más confiable y por qué.",
    prior=["Uso una pauta para revisar un texto.", "Separo hechos de opiniones.", "Reviso si cifras y fechas cuadran."],
    explain=[
        "Dos textos pueden hablar del mismo asunto y no merecer la misma confianza. Para compararlos, haz las mismas preguntas a los dos: ¿quién lo escribe?, ¿cuál es su fuente?, ¿trae fecha?, ¿se puede comprobar?, ¿qué quiere lograr?",
        "Un mensaje reenviado en cadena casi nunca tiene emisor identificable ni fecha, usa frases como «lo dijo un conocido» y presiona con una amenaza. Un comunicado institucional suele tener fecha, firma, datos concretos y un lugar donde consultar.",
        "Esto no significa que todo lo institucional sea perfecto ni que todo mensaje de un conocido sea falso. Significa que el texto con fuente y datos comprobables permite revisar; el otro solo pide que confíes.",
    ],
    vocab=[("comunicado", "texto oficial que una institución entrega para informar algo"), ("mensaje en cadena", "mensaje que se reenvía a muchas personas sin identificar su origen"), ("alarmista", "que busca asustar, a veces exagerando"), ("verificar", "comprobar si algo es cierto")],
    worked=[
        ("Comparar emisor y fecha", "Texto X (inventado): «Se cerrará el parque». Texto Y (inventado): «El 3 de abril, la municipalidad de ejemplo informó que el parque cerrará los lunes por mantención. Consultas: oficina de parques».", ["X no tiene emisor ni fecha ni motivo.", "Y indica quién informa, la fecha, el motivo y dónde consultar."], "Y es más confiable que X porque se puede verificar"),
        ("Detectar presión", "Mensaje (inventado): «Si no lo compartes hoy, perderás el beneficio».", ["Pide compartir para evitar una pérdida.", "No da una fuente ni muestra cuál es el beneficio."], "El mensaje presiona sin dar información comprobable"),
    ],
    mistakes=[("Creer más en el texto que se repite más veces.", "Que un texto se reenvíe mucho no lo hace verdadero.", "Fíjate en la fuente y en los datos, no en cuántas veces lo viste."),
              ("Desconfiar de un texto solo porque viene de una institución.", "También una institución puede tener errores; la diferencia es que se puede consultar.", "Revisa fecha, firma y datos, y consulta si hay dudas.")],
    T=[
        ("abc", "{F} ¿Cuál de los dos textos identifica a su emisor?", "El Texto 2, que lo firma la dirección del consultorio", "El Texto 1, que lo firma un conocido", "Ninguno de los dos", "El Texto 2 declara quién informa."),
        ("ab", "{F} ¿Cuál texto trae fecha?", "El Texto 2, con fecha 18 de noviembre", "El Texto 1, con la fecha de mañana", "El Texto 1 solo dice «mañana», sin fecha ni emisor."),
        ("{F} ¿Cuántos días de la semana atenderá con horario reducido el consultorio según el Texto 2? Escribe el número.", "1", "El Texto 2 habla solo del viernes 20."),
        ("abc", "{F} ¿Qué frase del Texto 1 muestra que su fuente no se puede comprobar?", "«Lo dijo un conocido de una funcionaria»", "«El consultorio Sol Naciente»", "«Comparte con diez personas»", "Una fuente de segunda mano y sin nombre no se puede revisar."),
        ("abc", "{F} ¿Qué intenta lograr la frase «comparte con diez personas o perderás tu hora»?", "Presionar para que se reenvíe el mensaje", "Informar el horario de atención", "Invitar a una capacitación", "Usa una amenaza para provocar que lo reenvíes."),
        ("=", "{F} El Texto 2 informa atención de 9:00 a 13:00. ¿Cuántas horas durará la atención ese viernes?", "13 - 9", "Se resta la hora de inicio a la hora de cierre.", " horas"),
        ("abc", "{F} ¿Qué hecho del Texto 2 puede comprobar una persona yendo al consultorio?", "Que existe un mesón de informaciones", "Que la capacitación será excelente", "Que el consultorio cerrará para siempre", "Un mesón se puede ver; las otras son juicios o dichos sin respaldo."),
        ("ab", "{F} El Texto 1 dice que el consultorio cerrará para siempre y el Texto 2 dice que atenderá con horario reducido. ¿Qué texto es más confiable?", "El Texto 2, porque tiene firma, fecha y datos comprobables", "El Texto 1, porque llegó a más personas", "El que se puede revisar merece más confianza que el que solo presiona."),
        ("abc", "{F} Si quieres confirmar la información, ¿cuál es la mejor acción?", "Preguntar en el mesón de informaciones del consultorio", "Reenviar el mensaje y esperar", "Preguntar al conocido de la funcionaria", "La institución que firma el comunicado puede confirmarlo."),
        ("ab", "{F} Un colega dice: «El Texto 2 es solo un papel pegado en la puerta, así que no sirve». ¿Qué respuesta es mejor?", "El papel tiene fecha, firma y datos; por eso se puede verificar", "Tiene razón: los papeles no son confiables", "Un comunicado firmado puede consultarse y tener responsabilidad."),
        ("abc", "{F} ¿Qué recurso del Texto 1 pretende asustar?", "El anuncio de un cierre definitivo y la pérdida de la hora", "El nombre del consultorio", "La frase «Lo dijo un conocido»", "Anuncia una pérdida grave para provocar reacción."),
        ("abc", "Un mensaje dice: «Se suspende el transporte desde mañana. Fuente: dicen». Falta lo más importante para verificar. ¿Qué es?", "Quién informa y desde cuándo exactamente", "Un saludo al comienzo", "Más signos de exclamación", "Sin emisor ni fecha precisa no hay cómo comprobarlo."),
        ("ab", "Un aviso de la empresa de buses (inventada) dice: «A contar del 2 de mayo, el recorrido 7 pasa por calle Roble. Consultas en la oficina de la empresa». ¿Qué lo hace verificable?", "Trae fecha, un dato concreto y dónde consultar", "Usa un lenguaje cordial", "Una fecha y un lugar de consulta permiten revisar el dato."),
    ],
    ctx=("abc", "En tu grupo de la junta de vecinos llega este mensaje: «Mañana cobran por usar la plaza. Me contó mi cuñado». Dos horas después la directiva publica: «No se cobrará por usar la plaza; consultas en la sede». ¿Qué conviene hacer?", "Creer el aviso firmado por la directiva y consultar en la sede si quedan dudas", "Reenviar el primer mensaje para avisar a todos", "No creer nada y no preguntar", "El aviso firmado se puede consultar; el primero viene de segunda mano."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué datos tiene un comunicado confiable?", "Emisor, fecha, datos concretos y un lugar de consulta", "Esos elementos permiten verificar la información."),
        ("En Lengua y Literatura de EPJA: ¿por qué un mensaje en cadena no es una fuente confiable?", "Porque no identifica su origen y presiona para reenviarlo", "No se puede revisar de dónde viene la información."),
        ("En Lengua y Literatura de EPJA: ¿qué pregunta sirve para comparar dos textos sobre el mismo tema?", "¿Quién lo escribe, con qué fuente y fecha?", "Hacer las mismas preguntas a ambos textos permite compararlos.")],
    op=("Compara los dos textos con una tabla en tu cuaderno: {F} Usa estas filas: emisor, fecha, fuente, propósito y qué se puede comprobar. Después escribe tres oraciones: qué texto es más confiable, por qué y qué harías antes de compartir uno de ellos.",
        "Emisor: texto 1 sin emisor claro; texto 2 la dirección del consultorio. Fecha: texto 1 sin fecha; texto 2 el 18 de noviembre. Fuente: texto 1 un conocido de una funcionaria; texto 2 el comunicado. Es más confiable el texto 2 porque puedo consultar en el mesón. Antes de compartir, confirmaría en el consultorio.",
        ["completa las cinco filas con datos de los textos", "elige un texto y lo justifica", "propone cómo confirmar"],
        ["tabla de cinco filas y tres oraciones"],
        ["justificar con «me parece»", "no decir cómo confirmar"],
        "Pregunta: «¿Qué dato de tu tabla prueba tu elección?»."),
    reinforce="Revisa un mensaje que hayas recibido y anota si trae emisor, fecha y fuente.",
    extend="Escribe un comunicado breve y verificable sobre un cambio de horario en tu trabajo o tu barrio, con emisor, fecha y dónde consultar.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a textos de la vida diaria: un aviso de trabajo y una cuenta del hogar.",
    prior=["Uso una pauta de cinco pasos.", "Reviso sumas, horas y fuentes.", "Reconozco hechos y opiniones."],
    explain=[
        "En el trabajo y en el hogar leemos textos que influyen en decisiones: un aviso de empleo, una cuenta, un contrato. Por eso conviene revisar su consistencia antes de actuar.",
        "En un aviso de trabajo, revisa que las condiciones no se contradigan: la jornada, los turnos y lo que se pide a quien postula. En una cuenta, revisa que las partes sumen el total y que la multiplicación de precio por cantidad esté bien hecha.",
        "Si algo no cuadra, no lo des por falso ni por cierto: pregunta a quien emite el texto, por ejemplo el empleador o la empresa de la cuenta, y pide una aclaración por escrito. Y cuando se trate de condiciones legales, di «según la norma vigente» y consulta la institución correspondiente.",
    ],
    vocab=[("jornada", "horas que se trabaja en un día o una semana"), ("desglose", "detalle de las partes de un total"), ("requisito", "condición que se pide para postular"), ("aclaración", "explicación que corrige o completa algo confuso")],
    worked=[
        ("Revisar requisitos", "Aviso (inventado): «Sin experiencia previa; se exige 3 años de experiencia».", ["Una frase dice que no se necesita experiencia.", "La otra exige tres años: se contradicen."], "Requisitos inconsistentes: pedir aclaración"),
        ("Revisar una cuenta", "Cuenta (inventada): «4 kg de pan a $1.500 el kilo; total $5.500».", ["Calculo 4 por 1.500 = 6.000.", "El total dice 5.500: no cuadra."], "La cuenta no es consistente: hay que consultar"),
    ],
    mistakes=[("Postular sin leer las condiciones completas.", "Una condición escondida, como los turnos de fin de semana, cambia la decisión.", "Lee el aviso entero y marca horarios, turnos y requisitos."),
              ("Pagar una cuenta sin comprobar su suma.", "Puede haber un error que se corrige si se pregunta a tiempo.", "Revisa que precio por cantidad y cargos sumen el total.")],
    T=[
        ("=", "{F} Según el aviso, la jornada es de 8 horas de lunes a viernes. ¿Cuántas horas semanales son de lunes a viernes?", "8 * 5", "Se multiplican 8 horas por los cinco días hábiles.", " horas"),
        ("=", "{F} Además hay dos turnos de 12 horas los fines de semana. ¿Cuántas horas suman esos turnos?", "12 * 2", "Cada turno dura doce horas y son dos.", " horas"),
        ("=", "{F} ¿Cuántas horas semanales suman en total la jornada de lunes a viernes y los dos turnos de fin de semana?", "8 * 5 + 12 * 2", "Se suman las horas de entre semana y las del fin de semana.", " horas"),
        ("abc", "{F} ¿Qué contradicción tiene el aviso de trabajo en los requisitos?", "Pide cinco años de experiencia y dice que no se requiere experiencia previa", "Ofrece un sueldo líquido", "Indica que se necesita un ayudante", "Las dos frases sobre experiencia no pueden ser ciertas a la vez."),
        ("ab", "{F} ¿Cuál es la mejor reacción de una persona interesada en el aviso?", "Pedir por escrito al empleador que aclare el requisito de experiencia y los turnos", "Postular sin preguntar para no perder la oportunidad", "Preguntar antes evita aceptar condiciones que no se entienden."),
        ("=", "{F} En la cuenta de agua, 14 metros cúbicos a $1.200 cada uno. ¿Cuánto cuesta el consumo?", "14 * 1200", "Se multiplica la cantidad por el precio de cada metro cúbico.", " pesos"),
        ("=", "{F} Si el consumo cuesta lo que calculaste y el cargo fijo es $3.000, ¿cuánto debería ser el total?", "14 * 1200 + 3000", "Se suman el consumo y el cargo fijo.", " pesos"),
        ("abc", "{F} El total que dice la cuenta es $21.000. ¿Qué se puede afirmar?", "No coincide con la suma del consumo y el cargo fijo", "Es correcto porque lo dice la cuenta", "Está bien porque es un número redondo", "La suma correcta es 19.800, no 21.000."),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre el total que dice la cuenta y el que sale de sumar sus partes?", "21000 - 19800", "Se resta el total correcto al total que figura en la cuenta.", " pesos"),
        ("ab", "{F} Jorge dice: «Pagaré los $21.000 porque así lo dice la cuenta». ¿Qué conviene hacer antes?", "Preguntar a la empresa de agua por la diferencia y pedir una aclaración", "Pagar sin preguntar y olvidar el tema", "Una diferencia que se puede comprobar se consulta antes de pagar."),
        ("abc", "{F} ¿Qué dato del aviso de trabajo se puede comprobar preguntando al empleador?", "Cuántas horas semanales trabajaría en total la persona contratada", "Si el trabajo será agradable", "Si el sueldo de ejemplo es el mejor del país", "Las horas semanales son un dato concreto; las otras opciones son juicios."),
        ("abc", "Un aviso de arriendo (inventado) dice: «Pieza amoblada, sin muebles». ¿Qué falla tiene?", "Se contradice: dice amoblada y sin muebles", "No dice el precio", "No tiene saludo", "Una pieza no puede estar amoblada y sin muebles a la vez."),
        ("ab", "Para pedir una aclaración sobre una cuenta, ¿qué dato conviene anotar primero?", "La cifra que no cuadra y el cálculo que hiciste", "Tu opinión sobre la empresa", "Con el cálculo anotado, la empresa puede revisar la diferencia."),
    ],
    ctx=("abc", "Te ofrecen cuidar un local con este aviso de ejemplo: «Horario de 9:00 a 17:00, de lunes a sábado, 3 días libres a la semana». ¿Qué conviene preguntar?", "Cuántos días se trabaja realmente, porque lunes a sábado deja un día libre", "Si el local tiene pintura nueva", "Si el aviso tiene firma bonita", "Trabajar de lunes a sábado y tener tres días libres no puede ser cierto a la vez."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué se revisa en un aviso de trabajo antes de postular?", "Que jornada, turnos y requisitos no se contradigan", "La consistencia protege de aceptar condiciones confusas."),
        ("En Lengua y Literatura de EPJA: ¿cómo se comprueba la suma de una cuenta?", "Multiplicando precio por cantidad y sumando los cargos", "Se rehace el cálculo y se compara con el total."),
        ("En Lengua y Literatura de EPJA: ¿qué se hace si una cuenta no cuadra?", "Se pide una aclaración a quien emite la cuenta", "La aclaración se pide a la fuente del texto.")],
    op=("Lee el aviso y la cuenta: {F} Escribe en tu cuaderno un mensaje breve y respetuoso al empleador, pidiendo aclarar dos puntos del aviso. Luego escribe otro a la empresa de agua con el cálculo que hiciste y la diferencia que encontraste.",
        "Al empleador: «Buenos días. Vi su aviso y quiero aclarar si se exige o no experiencia, y cuántas horas semanales se trabajan en total. Gracias.» A la empresa: «Mi cuenta indica $21.000. Al sumar el consumo, $16.800, y el cargo fijo, $3.000, obtengo $19.800. Pido revisar la diferencia de $1.200.»",
        ["identifica dos puntos concretos", "usa cifras del texto", "usa un tono respetuoso y claro"],
        ["dos mensajes breves"],
        ["no incluir los datos que no cuadran", "usar un tono agresivo"],
        "Pregunta: «¿Qué dato necesita quien te responde para ayudarte?»."),
    reinforce="Revisa la suma de una cuenta o boleta de tu casa con papel y lápiz.",
    extend="Escribe un aviso de trabajo breve y consistente para un oficio que conozcas, con jornada, requisitos y a quién consultar.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: analizo un anuncio oral escrito en papel y decido qué pasos seguir para verificar un texto.",
    prior=["Uso una pauta de cinco pasos.", "Compruebo sumas y horas.", "Comparo textos por su fuente."],
    explain=[
        "Un anuncio por altavoz o radio se escucha una sola vez, por eso conviene tomar notas. Anota las palabras clave: qué, quién, cuándo, dónde y por cuánto tiempo. Después, vuelve a revisarlas para ver si se contradicen.",
        "La comprensión oral usa estrategias parecidas a la lectura. Antes de escuchar, piensa de qué podría tratar. Mientras escuchas, anota horas, lugares y cantidades. Al terminar, resume con tus palabras y pregunta lo que no quedó claro.",
        "Hoy cierras este desempeño de análisis. Revisa lo logrado: ¿reconoces el emisor y el propósito?, ¿separas hechos de opiniones?, ¿compruebas la consistencia?, ¿sabes a quién preguntar? Decidir cómo seguir también es parte de analizar.",
    ],
    vocab=[("anuncio", "mensaje breve para dar a conocer algo"), ("palabra clave", "palabra que resume un dato importante"), ("parafrasear", "decir lo mismo con otras palabras"), ("aclarar", "pedir o dar una explicación para que algo quede claro")],
    worked=[
        ("Tomar notas de un anuncio", "Anuncio (inventado): «Mañana viernes, de 10:00 a 12:00, cerrará la calle Los Sauces por trabajos».", ["Anoto qué: cierre de calle. Cuándo: viernes, 10:00 a 12:00.", "Anoto dónde: calle Los Sauces."], "Notas: cierre, viernes, 10:00 a 12:00, Los Sauces"),
        ("Parafrasear", "Frase (inventada): «Se solicita a los usuarios abstenerse de estacionar en la zona».", ["Busco las palabras difíciles: «abstenerse» significa no hacer algo.", "Digo lo mismo con otras palabras."], "No estacionen en la zona"),
    ],
    mistakes=[("Quedarse con la primera hora que se escucha.", "Una hora oída una sola vez puede contradecirse con otra del mismo anuncio.", "Anota todas las horas y compáralas."),
              ("Creer que hacer una pregunta es desconfiar.", "Preguntar es una forma de comprender mejor y de cuidar la información.", "Pregunta a la fuente por lo que no cuadra o no entendiste.")],
    T=[
        ("abc", "{F} ¿Quién emite el anuncio?", "La radio comunitaria «Onda Vecinal», informando lo dicho por la empresa sanitaria", "La junta de vecinos de otra población", "Una persona que no se identifica", "El anuncio se emite por la radio y cita a la empresa."),
        ("ab", "{F} ¿A quién se dirige el anuncio?", "A las vecinas y vecinos de la población Nuevo Horizonte", "A todas las personas del país", "El texto saluda a vecinas y vecinos de una población en particular."),
        ("=", "{F} El corte empieza a las 9:00 y termina a las 14:00. ¿Cuántas horas dura?", "14 - 9", "Se resta la hora de inicio a la hora de término.", " horas"),
        ("abc", "{F} ¿A qué hora dice el anuncio que se estima que vuelva el suministro?", "12:00", "14:00", "9:00", "El texto dice «volverá a las 12:00»."),
        ("abc", "{F} ¿Qué contradicción hay en el anuncio?", "Dice que el corte dura hasta las 14:00 y que el agua vuelve a las 12:00", "Dice que el corte es jueves y que es mañana", "Dice que se guarda agua antes del corte", "Dos horas de regreso del agua distintas se contradicen."),
        ("ab", "{F} Al escuchar este anuncio por radio, ¿qué estrategia de comprensión oral ayuda más?", "Anotar todas las horas para compararlas", "Quedarse solo con la primera hora", "Con las horas anotadas se descubre la contradicción."),
        ("abc", "{F} ¿Cuál es una opinión o recomendación en el anuncio?", "«Se recomienda guardar agua con anticipación»", "«Se cortará el agua desde las 9:00»", "«Mañana jueves»", "Recomendar es sugerir una acción, no informar un hecho."),
        ("ab", "{F} ¿Cuál es la fuente de la información sobre los trabajos?", "La empresa sanitaria de ejemplo, según el anuncio", "Un vecino anónimo", "El anuncio dice «según informó la empresa sanitaria»."),
        ("abc", "{F} ¿Qué harías antes de repetir el anuncio a tus vecinos?", "Preguntar a la empresa o a la radio a qué hora se restablece el agua", "Repetir solo la hora que más te conviene", "Avisar que el agua volverá a las 12:00 sin comprobar", "Con dos horas distintas, conviene confirmar."),
        ("ab", "{F} ¿Cuál es una buena paráfrasis del anuncio?", "Mañana jueves habrá corte de agua en Nuevo Horizonte por trabajos; conviene guardar agua", "Todo el mes habrá corte de agua en Nuevo Horizonte", "La paráfrasis conserva el día, el lugar y la causa."),
        ("abc", "{F} ¿Qué dato falta en el anuncio para evitar la contradicción?", "Una única hora de término confirmada", "Un saludo más cordial", "El nombre del locutor", "Con una sola hora de término no habría dos versiones."),
        ("abc", "Cuando revisas lo que lograste en una unidad, ¿cuál es un buen último paso?", "Decidir qué te falta practicar y a quién pedirás apoyo", "Olvidar lo que no entendiste", "Decir que ya no necesitas revisar", "Planificar los pasos siguientes cierra el aprendizaje."),
        ("ab", "Una persona dice: «Si el texto está firmado, no necesito revisar la consistencia». ¿Qué respuesta es mejor?", "Aun con firma, hay que revisar si las cifras y horas cuadran", "Tiene razón: la firma garantiza todo", "Una firma identifica al emisor, pero no evita errores."),
    ],
    ctx=("abc", "Escuchas un anuncio en el consultorio (inventado): «Atención de 8:00 a 17:00. Cierre a las 16:00». Quieres saber a qué hora llegar. ¿Qué conviene hacer?", "Preguntar en el mesón a qué hora cierran, porque las horas se contradicen", "Llegar a las 16:30 sin preguntar", "Suponer que atienden las 24 horas", "El anuncio da dos horas de cierre distintas."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué se anota al escuchar un anuncio?", "Palabras clave: qué, quién, cuándo, dónde y cuánto tiempo", "Esas notas permiten revisar los datos después."),
        ("En Lengua y Literatura de EPJA: ¿qué es parafrasear?", "Decir lo mismo con otras palabras", "Parafrasear ayuda a comprobar que entendiste."),
        ("En Lengua y Literatura de EPJA: ¿qué se decide al final del análisis de un texto?", "Si es confiable, dudoso o necesita confirmarse, y a quién preguntar", "La evaluación termina con una decisión justificada.")],
    op=("Lee el guion como si lo escucharas por radio: {F} Escribe en tu cuaderno tus notas con cinco datos clave, la contradicción que encontraste y una pregunta que harías a la empresa sanitaria. Termina con una lista de tres cosas que ya logras hacer al analizar un texto y una que quieres mejorar.",
        "Notas: jueves; 9:00 a 14:00; Nuevo Horizonte; trabajos en la red; guardar agua. Contradicción: dice hasta las 14:00 y vuelve a las 12:00. Pregunta: «¿A qué hora se restablece el agua?». Logro: reconozco el emisor, separo hechos de opiniones, reviso cifras. Por mejorar: anotar más rápido.",
        ["cinco datos clave correctos", "señala la contradicción", "formula una pregunta clara y evalúa su avance"],
        ["notas, una pregunta y cuatro frases de revisión"],
        ["copiar el guion completo en vez de anotar", "no decir qué quiere mejorar"],
        "Pregunta: «¿Qué dato del anuncio verificarías primero?»."),
    reinforce="Escucha un aviso de la radio o de un altavoz y anota quién, qué, cuándo y dónde.",
    extend="Escribe un guion de anuncio de seis líneas para tu comunidad, con una hora de término única y una fuente.",
)

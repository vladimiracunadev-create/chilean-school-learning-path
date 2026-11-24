"""Lengua y Literatura EPJA Media Nivel 1, módulo 3: OAD-09, investigar sobre una persona de la cultura chilena o latinoamericana, evaluando la validez y confiabilidad de las fuentes y aplicando normas de citación. Personas y fuentes inventadas; todo se resuelve en papel."""
from __future__ import annotations

from epja_leli_nm1_c_common import build

O = "EPJA-LELI-NM1-OAD-09"

F1 = ("Ficha (inventada). Persona de estudio: doña Eliana Montecinos, costurera y fundadora de una cooperativa de vecinas en un barrio ficticio. "
      "Lo que se dice de ella: (a) una vecina cuenta que «ayudó a muchas familias»; (b) un afiche del barrio (inventado) la nombra como fundadora; "
      "(c) el libro de actas de la cooperativa (inventado) registra que se fundó en 1998 con 12 socias y que en 2008 ya tenía 30 socias.")

F2 = ("Cuatro fuentes (inventadas) sobre don Mateo Quiroga, poeta popular ficticio. Fuente 1: transcripción de una entrevista a su hija, hecha en 2015 por una radio comunitaria: «Mi padre escribía décimas después de su turno en el puerto». "
      "Fuente 2: una libreta manuscrita con décimas de don Mateo, con la fecha 1974 en la tapa, que guarda un archivo de la municipalidad. "
      "Fuente 3: artículo de una enciclopedia escolar, firmado por un equipo editorial, que resume su obra en cinco líneas e indica de dónde sacó los datos. "
      "Fuente 4: una publicación de red social sin autor ni fecha que dice que fue «el mejor poeta del país».")

F3 = ("Cuatro sitios (inventados) sobre doña Eliana Montecinos. Sitio A, museo del barrio: artículo firmado por la historiadora Sonia Lagos, con fecha de 2021, que cita el libro de actas y dos entrevistas. "
      "Sitio B, blog personal: texto sin autor ni fecha que dice «todos saben que doña Eliana fue la mejor costurera de Chile». "
      "Sitio C, tienda en línea: aviso «¡El libro más completo sobre doña Eliana! ¡Compre ya!», sin datos del autor. "
      "Sitio D, archivo municipal digital: fotografías del libro de actas, con la fecha de cada página y un número de archivo.")

F4 = ("Datos de tres fuentes (inventadas) para citar. Fuente A: libro «Costureras del barrio», autora Marta Lagos, año 2019, editorial Ediciones del Pasaje (ficticia). "
      "Fuente B: artículo web «La cooperativa de la calle Larga», autor Pablo Reyes, año 2021, sitio Museo del Barrio (ficticio), consultado el 5 de marzo de 2024. "
      "Fuente C: libro de actas de la cooperativa (inventado), año 1998, guardado por el archivo municipal (ficticio), sin autor persona. "
      "Formato de este cuaderno: referencia = Apellido, Inicial. (año). Título. Editorial o sitio. Cita en el texto = (Apellido, año); si no hay autor persona, se usa la institución.")

F5 = ("Notas de investigación (inventadas) sobre don Hernán Pizarro, técnico en refrigeración que fundó una escuela nocturna de oficios. "
      "Nota 1 (Fuente A: entrevista a una exalumna, radio comunitaria, 2017): la escuela partió con dos salas y ocho estudiantes. "
      "Nota 2 (Fuente B: registro del centro de oficios, 2003, archivo): la escuela se inició en 1996 con ocho estudiantes. "
      "Nota 3 (Fuente C: blog anónimo, sin fecha): don Hernán fue «el mejor maestro del mundo» y la escuela tuvo 500 estudiantes el primer año. "
      "Nota 4 (Fuente D: artículo de revista local firmado por Irene Soto, 2010): en 2010 la escuela tenía 120 estudiantes y ofrecía tres oficios.")

F6 = ("Informe de una estudiante (inventado) sobre doña Aurora Neira, dirigente de feria: «Aurora Neira fue la mejor dirigente de feria de todos los tiempos. Fundó la Asociación de Ferias del Valle en 1990. "
      "Dicen que ayudó a todos. «Organizó turnos de limpieza para los puestos». Fuente: internet.» "
      "Fuentes que la estudiante sí consultó: acta de fundación de la Asociación (1990, archivo municipal) y entrevista a una feriante hecha por la radio del barrio en 2018. "
      "Lista de verificación: 1) pregunta clara; 2) al menos dos fuentes confiables; 3) cada dato con su fuente; 4) citas textuales entre comillas con autor y año; 5) lista de referencias completa.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya sé: formulo preguntas para investigar a una persona y reconozco de dónde viene lo que se dice de ella.",
    prior=["Pregunto a otras personas cuando quiero saber algo.", "Distingo entre lo que me contaron y lo que vi en un documento.", "Sé tomar notas breves."],
    explain=[
        "Tú ya investigas en la vida diaria: preguntas el precio en tres negocios, revisas un contrato antes de firmar o comparas lo que te cuentan. Investigar sobre una persona es lo mismo: reunir datos de varias fuentes para responder preguntas.",
        "Una fuente es el lugar de donde sale un dato: una persona, un documento, un libro o un sitio web. Una pregunta de investigación se responde con datos, no con gustos. «¿Cuándo se fundó la cooperativa?» sirve; «¿Era la mejor persona?» es una opinión.",
        "Antes de buscar, escribe tus preguntas: quién fue, qué hizo, cuándo y dónde, y qué efecto tuvo. Junto a cada dato anota de qué fuente lo sacaste. Así, cualquier persona puede comprobar tu trabajo.",
    ],
    vocab=[("fuente", "persona, documento o sitio de donde sale un dato"), ("pregunta de investigación", "pregunta que se responde con datos de fuentes"), ("dato", "información concreta que se puede comprobar"), ("opinión", "juicio personal que no se puede comprobar con datos")],
    worked=[
        ("Formular preguntas", "Quieres investigar a doña Eliana Montecinos (persona inventada).", ["Escribo preguntas que se responden con datos: ¿quién fue?, ¿qué fundó?, ¿cuándo?", "Evito preguntas de opinión como «¿fue admirable?»."], "Tres preguntas que se pueden responder con fuentes"),
        ("Anotar la fuente", "El libro de actas dice que la cooperativa se fundó en 1998.", ["Escribo el dato: se fundó en 1998.", "Anoto al lado de dónde sale: libro de actas de la cooperativa."], "Dato con su fuente: se fundó en 1998 (libro de actas)"),
    ],
    mistakes=[("Escribir preguntas de opinión, como «¿era la mejor persona?».", "Una opinión no se comprueba con documentos ni fechas.", "Cambia la pregunta por una que pida un dato: «¿qué actividades organizó?»."),
              ("Anotar un dato sin escribir de dónde lo sacaste.", "Sin la fuente, nadie puede comprobar tu información.", "Escribe siempre el dato y, al lado, su fuente.")],
    T=[
        ("abc", "¿Cuál es una pregunta de investigación que se puede responder con fuentes?", "«¿Qué actividades organizó la cooperativa que fundó doña Eliana?»", "«¿Fue doña Eliana la persona más buena del barrio?»", "«¿Por qué todos deberían admirar a las costureras?»", "Las otras dos piden opiniones; la primera se responde con datos y documentos."),
        ("{F} ¿Cuántas socias tenía la cooperativa al fundarse según el libro de actas? Escribe solo el número.", "12", "El libro de actas registra que se fundó con 12 socias."),
        ("ab", "{F} ¿Qué fuente afirma «ayudó a muchas familias» sin dar datos concretos?", "El relato de la vecina", "El libro de actas", "Solo la vecina lo dice y no nombra hechos ni fechas."),
        ("abc", "{F} ¿Qué pregunta responde el dato «se fundó en 1998»?", "¿Cuándo comenzó la cooperativa?", "¿Por qué se llama así la cooperativa?", "¿Cuánto ganaba doña Eliana?", "Una fecha de fundación responde a la pregunta por el cuándo."),
        ("=", "{F} ¿Cuántas socias más tenía la cooperativa en 2008 que cuando se fundó?", "30 - 12", "Se restan las socias de 2008 a las de la fundación para ver el aumento.", "socias"),
        ("ab", "Alguien dice: «Investigar es copiar lo primero que aparece». ¿Qué es mejor?", "Hacer preguntas, mirar varias fuentes y anotar de dónde sale cada dato", "Quedarme con la primera fuente que encuentre porque es la más fácil", "Investigar exige preguntas, varias fuentes y anotar el origen de cada dato."),
        ("abc", "{F} Quieres saber cuándo se fundó la cooperativa. ¿Qué fuente de la ficha te sirve más?", "El libro de actas, porque registra el año y las socias", "El relato de la vecina, porque la conocía", "El afiche, porque tiene una imagen llamativa", "Solo el libro de actas entrega el año de fundación como dato."),
        ("{F} ¿En qué año tenía 30 socias la cooperativa? Escribe solo el número.", "2008", "El libro de actas indica que en 2008 ya tenía 30 socias."),
        ("abc", "Quieres saber en qué lugar funcionó el primer taller. ¿Qué pregunta de investigación formulas?", "«¿Dónde funcionó el primer taller de la cooperativa?»", "«¿Cuándo se fundó la cooperativa?»", "«¿Quién fundó la cooperativa?»", "La pregunta por el lugar se formula con «dónde»."),
        ("ab", "Ana anota «se fundó en 1998 (libro de actas)». Beto anota solo «1998». ¿Quién investiga mejor?", "Ana, porque indica de dónde sale el dato y otra persona puede comprobarlo", "Beto, porque su nota es más corta y rápida de escribir", "La nota con fuente permite comprobar el dato; la corta no."),
        ("abc", "{F} La vecina dice «ayudó a muchas familias» y el libro de actas no menciona ayudas. ¿Qué conviene hacer?", "Anotarlo como relato de la vecina y buscar otra fuente que lo confirme", "Escribirlo como un hecho seguro, porque la vecina la conocía", "Borrarlo y no mencionarlo jamás, aunque pueda ser cierto", "Un relato sin respaldo se anota como tal y se contrasta con otras fuentes."),
        ("abc", "{F} Tu pregunta es: «¿Qué cambió en la cooperativa entre 1998 y 2008?». ¿Qué dato de la ficha sirve para responderla?", "El aumento de 12 a 30 socias", "La opinión de que ayudó a muchas familias", "El nombre de la vecina que la recuerda", "El cambio de 12 a 30 socias es un dato comparable entre las dos fechas."),
        ("{F} Una investigadora escribe: «La cooperativa se fundó en 1988». ¿Qué fuente de la ficha contradice ese año? Responde: acta, afiche o vecina.", "acta", "El libro de actas registra 1998, no 1988."),
    ],
    ctx=("abc", "Vas a escribir una breve biografía de una dirigente de tu barrio para el diario mural del centro de estudios. ¿Qué haces antes de escribir?", "Formular preguntas de investigación y anotar de dónde obtienes cada dato", "Escribir de memoria lo que crees recordar sin consultar a nadie", "Copiar la primera página que encuentres, sin leerla completa", "Preguntas claras y datos con fuente hacen que tu texto se pueda comprobar."),
    sc=[("En Lengua y Literatura: ¿qué es una pregunta de investigación?", "Una pregunta que se responde con datos de fuentes", "Se responde con datos y no con gustos u opiniones."),
        ("En Lengua y Literatura: ¿qué es una fuente de información?", "La persona, documento o sitio de donde sale un dato", "La fuente es el origen del dato y permite comprobarlo."),
        ("En Lengua y Literatura: ¿por qué se anota de dónde sale cada dato?", "Para que otras personas puedan comprobarlo", "Con la fuente anotada, cualquiera puede revisar el dato.")],
    op=("{F} Escribe en tu cuaderno cuatro preguntas de investigación sobre doña Eliana que se puedan responder con datos. Luego, para cada una, anota qué fuente de la ficha (vecina, afiche o libro de actas) podría ayudar y por qué.",
        "Pregunta: ¿Cuándo se fundó la cooperativa? Fuente: libro de actas, porque registra el año (1998). Pregunta: ¿Cuántas socias tenía en 2008? Fuente: libro de actas (30).",
        ["las cuatro preguntas piden datos y no opiniones", "cada pregunta tiene una fuente propuesta", "justifica por qué la fuente sirve"],
        ["cuatro preguntas con fuente y justificación escritas"],
        ["escribir preguntas de opinión", "proponer una fuente sin explicar por qué"],
        "Pregunta de revisión: «¿Se puede responder esta pregunta con un documento o con un dato?». Si la respuesta es no, reescríbela."),
    reinforce="Escribe tres preguntas de investigación sobre una persona de tu comunidad (sin datos personales) y marca cuál pide un dato y cuál una opinión.",
    extend="Elige una persona conocida de tu comuna y anota quién o qué documento podría darte datos sobre su vida. Explica por qué confiarías en cada uno.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy distingo tipos de fuentes (primarias y secundarias) y el vocabulario para hablar de ellas: autor, fecha, institución, testimonio.",
    prior=["Sé que un dato necesita una fuente.", "Formulo preguntas de investigación.", "Distingo un relato de un documento."],
    explain=[
        "Las fuentes se pueden agrupar. Una fuente primaria nace de la persona misma o de quien vivió los hechos: una libreta, una carta, un acta o una entrevista. Una fuente secundaria resume o explica lo que dicen otras, como una enciclopedia o un artículo.",
        "Un testimonio es lo que cuenta una persona que conoció a alguien o vivió un hecho. Es valioso porque trae experiencia, pero puede equivocarse con las fechas. Por eso conviene compararlo con documentos.",
        "Cada fuente tiene datos que la identifican: autor, fecha e institución que la publica o guarda. Si falta alguno de ellos, se debe tratar con más cuidado. Una fuente no es mejor por ser primaria o secundaria: se evalúa caso a caso.",
    ],
    vocab=[("fuente primaria", "creada por la persona o por quien vivió los hechos"), ("fuente secundaria", "resume o explica lo que dicen otras fuentes"), ("testimonio", "relato de alguien que conoció a la persona o vivió el hecho"), ("autor", "quien produce o firma una fuente")],
    worked=[
        ("Clasificar una fuente", "Una carta escrita en 1985 por un obrero sobre su sindicato (ejemplo).", ["La escribió una persona que vivió los hechos.", "No es un resumen de otras fuentes."], "Fuente primaria"),
        ("Clasificar otra fuente", "Un libro de 2020 que resume la historia de ese sindicato a partir de cartas y actas (ejemplo).", ["Reúne y explica lo que dicen otras fuentes.", "Su autor no vivió los hechos de 1985."], "Fuente secundaria"),
    ],
    mistakes=[("Pensar que una fuente secundaria siempre es más confiable que un testimonio.", "El tipo de fuente no decide la confiabilidad; cada fuente se evalúa.", "Revisa autor, fecha y en qué se apoya cada una."),
              ("Creer que toda fuente sin autor sirve igual que una firmada.", "Si no se sabe quién lo afirma, no se puede juzgar su seriedad.", "Busca el autor o la institución antes de usar el dato.")],
    T=[
        ("abc", "{F} ¿Cuál es una fuente primaria, creada por la propia persona de estudio?", "La Fuente 2, la libreta manuscrita de don Mateo", "La Fuente 3, el artículo de la enciclopedia escolar", "La Fuente 4, la publicación sin autor", "La libreta la escribió él mismo; la enciclopedia resume lo que dicen otros."),
        ("ab", "{F} ¿Cuál es una fuente secundaria?", "La Fuente 3, porque resume información que sacó de otras fuentes", "La Fuente 2, porque la escribió don Mateo", "La enciclopedia explica y resume; la libreta es obra de don Mateo."),
        ("{F} ¿Qué año figura en la tapa de la libreta de don Mateo? Escribe solo el número.", "1974", "La ficha dice que la libreta lleva la fecha 1974 en la tapa."),
        ("abc", "{F} ¿Qué dato falta en la Fuente 4 que impide saber si es confiable?", "El autor y la fecha, para saber quién lo afirma y cuándo", "Una imagen de don Mateo", "Más adjetivos elogiosos sobre el poeta", "Sin autor ni fecha no se puede juzgar la seriedad de lo que dice."),
        ("abc", "En Lengua y Literatura: ¿qué es una fuente de información?", "Cualquier persona, documento o sitio de donde sale un dato", "Solo un libro impreso que está en una biblioteca", "Un resumen que escribo yo sin consultar a nadie", "Una fuente puede ser una persona, un documento o un sitio web."),
        ("ab", "{F} ¿Qué ventaja tiene el testimonio de la hija (Fuente 1)?", "Aporta la experiencia de alguien cercano, aunque conviene compararla con documentos", "Es siempre exacto, porque la hija conocía a su padre", "Un testimonio da experiencia, pero la memoria puede fallar en fechas."),
        ("abc", "{F} Quieres saber en qué trabajaba don Mateo. ¿Qué fuente lo dice?", "La Fuente 1, la entrevista, que habla de su turno en el puerto", "La Fuente 2, que solo entrega una fecha en la tapa", "La Fuente 4, que solo dice que fue el mejor", "Solo la entrevista menciona su trabajo en el puerto."),
        ("Un diario escrito en 1990 por una dirigente vecinal sobre las reuniones de su junta (ejemplo), ¿es fuente primaria o secundaria? Responde: primaria o secundaria.", "primaria", "Lo escribió alguien que vivió los hechos."),
        ("Un manual escolar de 2015 que explica la historia de las juntas de vecinos a partir de libros y actas (ejemplo), ¿es fuente primaria o secundaria? Responde: primaria o secundaria.", "secundaria", "Resume y explica lo que dicen otras fuentes."),
        ("ab", "Alguien dice: «La Fuente 3 es mejor que la 1 porque es secundaria». ¿Es correcto?", "No: ninguna es mejor por su tipo; se evalúa cada una y se usan para contrastar", "Sí: las fuentes secundarias siempre son más confiables que los testimonios", "El tipo de fuente no decide su valor: se evalúan una por una."),
        ("abc", "{F} ¿Qué combinación de fuentes permite comprobar que don Mateo escribía décimas?", "Las Fuentes 1 y 2: el testimonio y la libreta con sus décimas se apoyan entre sí", "Las Fuentes 1 y 4, porque ambas dicen algo sobre él", "Solo la Fuente 4, porque tiene más difusión", "Dos fuentes de origen distinto que coinciden se refuerzan."),
        ("abc", "{F} Debes escribir un párrafo sobre la infancia de don Mateo, pero ninguna fuente de la ficha habla de ella. ¿Qué haces?", "Buscar otra fuente que trate su infancia o decir que faltan datos", "Imaginar su infancia y escribirla como si fuera un hecho", "Usar la Fuente 4, porque seguro la menciona", "No se puede afirmar lo que ninguna fuente respalda."),
        ("{F} ¿Cuántas de las cuatro fuentes indican quién las produce o las guarda? Escribe solo el número.", "3", "Las tres primeras nombran radio, archivo o equipo editorial; la cuarta no."),
    ],
    ctx=("abc", "Te llega por mensaje un texto sin firma sobre un dirigente de tu comuna y quieres usarlo en un trabajo. ¿Qué haces primero?", "Buscar quién lo escribió y contrastar sus datos con otra fuente", "Usarlo tal cual, porque llegó por un mensaje", "Pedirle a otra persona que lo reescriba para no tener que citar", "Un texto sin firma exige averiguar su origen y contrastarlo."),
    sc=[("En Lengua y Literatura: ¿qué es una fuente primaria?", "Una creada por la persona o por quien vivió los hechos", "Nace de quien vivió los hechos o de la propia persona."),
        ("En Lengua y Literatura: ¿qué es una fuente secundaria?", "Una que resume o explica lo que dicen otras fuentes", "Reúne información de otras fuentes y la explica."),
        ("En Lengua y Literatura: ¿qué es un testimonio?", "El relato de alguien que conoció a la persona o vivió el hecho", "El testimonio es experiencia contada y conviene compararla con documentos.")],
    op=("{F} Arma en tu cuaderno una tabla con cuatro filas (Fuente 1 a 4) y tres columnas: tipo (primaria o secundaria), si tiene autor o institución identificable, y qué dato de don Mateo aporta. Después escribe dos líneas: qué fuente usarías primero y por qué.",
        "Fuente 2: primaria; archivo de la municipalidad; muestra que escribía décimas en 1974. Usaría primero la 2 y la 1, porque se apoyan entre sí.",
        ["clasifica correctamente cada fuente", "señala si hay autor o institución", "justifica su elección con datos de la ficha"],
        ["tabla de cuatro filas y dos líneas de justificación"],
        ["clasificar según cuál suena más seria", "elegir la Fuente 4 sin autor"],
        "Pregunta de revisión: «¿Quién produjo esta fuente y de qué se apoya?». Si no puedes responder, usa esa fuente con cautela."),
    reinforce="Anota tres fuentes que usas en tu vida (un contrato, un mensaje, una noticia) y di si son primarias o secundarias.",
    extend="Elige un hecho de tu barrio y escribe una lista de dos fuentes primarias y una secundaria que podrían servir para investigarlo.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a evaluar si una fuente es válida y confiable con cinco preguntas.",
    prior=["Distingo fuentes primarias y secundarias.", "Sé qué datos identifican una fuente.", "Comparo lo que dicen dos textos."],
    explain=[
        "Evaluar una fuente es decidir cuánto puedo confiar en ella. La confiabilidad mira a quien produce la fuente: si se sabe quién es, si es serio y si se apoya en pruebas. La validez mira el dato: si es verdadero y sirve para mi pregunta.",
        "Usa cinco preguntas. ¿Quién lo escribió? ¿Cuándo? ¿Para qué: informar, vender u opinar? ¿En qué se apoya? ¿Otras fuentes independientes dicen lo mismo? Si una respuesta es débil, busca otra fuente.",
        "Dos sitios que copian el mismo texto cuentan como una sola fuente. Una fuente confiable puede no ser válida para tu pregunta, por ejemplo si trata de otra persona con el mismo nombre.",
    ],
    vocab=[("confiabilidad", "grado en que puedo confiar en quien produce la fuente"), ("validez", "si el dato es verdadero y sirve para mi pregunta"), ("propósito", "para qué se escribió la fuente: informar, vender u opinar"), ("contrastar", "comparar un dato con otras fuentes independientes")],
    worked=[
        ("Evaluar un blog", "Un blog dice «todos saben que fue la mejor» y no tiene autor ni fecha (ejemplo).", ["Pregunto quién lo escribió: no se sabe.", "Pregunto en qué se apoya: en «todos saben», que no es prueba.", "Pregunto el propósito: opinar."], "Poco confiable: lo uso solo como opinión y busco otra fuente"),
        ("Evaluar un archivo", "Un archivo municipal publica el acta número 4 con fecha y número de registro (ejemplo).", ["Hay institución identificable.", "Hay fecha y documento original que se puede revisar."], "Confiable: puedo usar el dato y citarlo"),
    ],
    mistakes=[("Creer que un sitio es confiable porque se ve ordenado o profesional.", "El diseño no prueba quién escribe ni en qué se apoya.", "Revisa autor, fecha, propósito y respaldo."),
              ("Contar como dos fuentes a dos sitios que copian el mismo texto.", "Si uno copia a otro, la información sale de una sola fuente.", "Busca una fuente independiente que confirme el dato.")],
    T=[
        ("abc", "Para evaluar una fuente, ¿cuál es una pregunta útil?", "¿Quién la escribió y en qué se apoya?", "¿Cuál tiene más imágenes de colores?", "¿Cuál aparece primero en la lista de resultados?", "Autor y respaldo permiten juzgar la confiabilidad; los colores no."),
        ("ab", "{F} ¿Qué sitio tiene autor y fecha identificables?", "El Sitio A, firmado por Sonia Lagos y con fecha de 2021", "El Sitio B, el blog personal", "Solo el Sitio A muestra autor y fecha."),
        ("{F} ¿Qué sitio tiene como propósito principal vender algo? Responde con la letra.", "C", "El aviso del Sitio C invita a comprar un libro."),
        ("abc", "{F} ¿Por qué el Sitio B es poco confiable?", "No tiene autor ni fecha y afirma sin pruebas", "Porque está escrito en un blog", "Porque habla bien de doña Eliana", "El problema es que no se sabe quién lo dice ni en qué se apoya."),
        ("abc", "{F} ¿En qué se apoya el artículo del Sitio A?", "En el libro de actas y en dos entrevistas", "En lo que todos saben del barrio", "En la oferta de un libro en venta", "El artículo cita sus documentos y entrevistas."),
        ("ab", "{F} ¿Qué aporta el Sitio D a la investigación?", "Documentos originales con fecha que se pueden revisar", "Opiniones de personas anónimas sobre doña Eliana", "Las fotografías del libro de actas son fuentes primarias comprobables."),
        ("abc", "{F} Debes elegir dos sitios para tu trabajo. ¿Qué par es mejor?", "A y D, porque tienen autor o archivo identificable y se apoyan en documentos", "B y C, porque llegan a más personas", "A y C, porque ambos tienen textos más largos", "Autor identificable y respaldo documental pesan más que la popularidad."),
        ("=", "{F} El artículo del Sitio A es de 2021 y lo consultas en 2024. ¿Cuántos años tiene?", "2024 - 2021", "Se restan los años para saber su antigüedad al consultarlo.", "años"),
        ("ab", "Un sitio dice «según el acta N.º 4 del 12 de mayo» y otro dice «dicen que fue en mayo». ¿Cuál permite comprobar mejor el dato?", "El primero, porque indica un documento que se puede revisar", "El segundo, porque suena más natural", "Solo el primero nombra un documento concreto que se puede buscar."),
        ("abc", "{F} El Sitio C dice que su libro es «el más completo». ¿Qué conviene hacer con ese dato?", "Tratarlo como publicidad y buscar una reseña independiente antes de creerlo", "Aceptarlo, porque lo dice el propio autor del libro", "Usarlo como prueba principal de tu informe", "Quien vende un producto no es una fuente neutral sobre su calidad."),
        ("ab", "Dos sitios coinciden en la fecha de fundación, pero uno copió al otro. ¿Sirve como confirmación independiente?", "No: si uno copia al otro, en realidad es una sola fuente", "Sí: mientras más sitios repitan el dato, más seguro es", "Dos copias del mismo texto no son confirmaciones independientes."),
        ("{F} ¿Cuántos de los cuatro sitios tienen autor o institución identificable? Escribe solo el número.", "2", "Solo el Sitio A (Sonia Lagos) y el Sitio D (archivo municipal) la tienen."),
        ("abc", "Un sitio es serio, pero habla de otra persona del mismo nombre que tu investigada, en otro país. ¿Qué significa?", "Es confiable, pero no es válido para tu pregunta porque trata de otra persona", "Es válido, porque su autor es serio", "Es falso, porque el nombre coincide con otro", "Confiable se refiere a quien lo produce; válido, a que sirva para tu pregunta."),
    ],
    ctx=("abc", "Buscas datos sobre un artesano de tu región para un trabajo. Aparecen un artículo firmado por una institución cultural y un aviso de venta de sus obras. ¿Cuál usas como base de los datos biográficos?", "El artículo firmado, y el aviso solo para saber dónde se venden las obras", "El aviso, porque tiene precios y fotografías", "Ninguno, porque ambos son de internet", "El artículo firmado informa y el aviso busca vender."),
    sc=[("En Lengua y Literatura: ¿qué mide la confiabilidad de una fuente?", "Cuánto puedo confiar en quien la produce", "Se juzga por autor, seriedad y respaldo."),
        ("En Lengua y Literatura: ¿qué significa que un dato sea válido?", "Que es verdadero y sirve para mi pregunta", "Validez es que el dato sea correcto y pertinente."),
        ("En Lengua y Literatura: ¿cuáles son las cinco preguntas para evaluar una fuente?", "Quién, cuándo, para qué, en qué se apoya y si otras fuentes coinciden", "Autor, fecha, propósito, respaldo y contraste.")],
    op=("{F} Evalúa los Sitios A, B, C y D con las cinco preguntas (quién, cuándo, para qué, en qué se apoya, si otras fuentes coinciden). Haz una tabla en tu cuaderno y marca con una cruz las respuestas débiles. Después escribe un párrafo corto (4 líneas) con los dos sitios que usarías y por qué.",
        "Sitio B: quién, no se sabe; cuándo, no tiene fecha; propósito, opinar; apoyo, «todos saben»; contraste, ninguno. Uso A y D porque tienen autor, fecha y documentos.",
        ["aplica las cinco preguntas a los cuatro sitios", "señala las respuestas débiles con datos de la ficha", "elige dos sitios y justifica"],
        ["tabla de evaluación y párrafo de cuatro líneas"],
        ["decidir por el diseño del sitio", "elegir un sitio de venta como fuente biográfica"],
        "Pregunta de revisión: «¿Esta fuente sirve para mi pregunta y se puede comprobar?»."),
    reinforce="Toma un aviso o mensaje que hayas recibido y respóndele las cinco preguntas de evaluación.",
    extend="Escribe una regla de tres líneas para decidir si usarás una fuente de internet en un trabajo. Prueba tu regla con los Sitios B y D de esta clase.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo las normas de citación: citas textuales, paráfrasis y lista de referencias.",
    prior=["Evalúo si una fuente es confiable.", "Anoto el dato y su fuente.", "Sé usar comillas para marcar palabras de otra persona."],
    explain=[
        "Citar es reconocer de dónde viene una idea. Si copias palabras exactas, van entre comillas y con la cita en el texto: (Apellido, año). Si explicas la idea con tus palabras, es una paráfrasis y también se cita.",
        "Al final del trabajo va la lista de referencias. En este cuaderno, cada referencia sigue este orden: Apellido, Inicial. (año). Título. Editorial o sitio. Si es un sitio web, se agrega la fecha en que lo consultaste. Si no hay autor persona, se usa la institución.",
        "Usar ideas o textos de otra persona sin citarla se llama plagio. Es una falta de respeto hacia quien los creó y le quita valor a tu trabajo. Tu docente puede pedir otro formato; lo importante es ser constante.",
    ],
    vocab=[("cita textual", "palabras copiadas exactas, entre comillas y con autor y año"), ("paráfrasis", "idea ajena dicha con tus palabras, también con cita"), ("referencia", "datos completos de una fuente en la lista final"), ("plagio", "usar ideas o textos ajenos sin reconocer a su autor")],
    worked=[
        ("Escribir una referencia", "Libro «Costureras del barrio», de Marta Lagos, 2019, Ediciones del Pasaje (datos de ejemplo).", ["Escribo apellido e inicial: Lagos, M.", "Agrego el año entre paréntesis: (2019).", "Sigo con el título y la editorial."], "Lagos, M. (2019). Costureras del barrio. Ediciones del Pasaje."),
        ("Citar una paráfrasis", "Explicas con tus palabras una idea del artículo de Pablo Reyes de 2021 (ejemplo).", ["Como no copio las palabras, no uso comillas.", "Aun así reconozco la fuente al final de la oración."], "Idea parafraseada con cita: (Reyes, 2021)"),
    ],
    mistakes=[("Cambiar una palabra de una frase ajena y no citar.", "Sigue siendo el texto de otra persona y eso es plagio.", "Usa comillas y cita, o explica la idea con tus palabras y cita igual."),
              ("Escribir «Fuente: internet» como referencia.", "No dice quién escribió, cuándo ni en qué sitio.", "Escribe autor, año, título, sitio y fecha de consulta.")],
    T=[
        ("abc", "{F} Según el formato de este cuaderno, ¿cómo se escribe la referencia de la Fuente C, que no tiene autor persona?", "Archivo municipal. (1998). Libro de actas de la cooperativa.", "Libro de actas de la cooperativa, Archivo municipal, 1998.", "Actas, L. (1998). Archivo municipal. Cooperativa.", "Sin autor persona se usa la institución en su lugar, y se sigue el orden: autor, año entre paréntesis y título."),
        ("ab", "{F} ¿Qué dato extra lleva la referencia de una página web?", "La fecha en que la consultaste", "El número de teléfono del sitio", "Las páginas web cambian, por eso se anota cuándo se consultaron."),
        ("{F} ¿En qué año se publicó el artículo de la Fuente B? Escribe solo el número.", "2021", "El artículo de Pablo Reyes es de 2021."),
        ("abc", "Copias una frase exacta de un libro. ¿Qué debes hacer?", "Ponerla entre comillas e indicar autor y año", "Escribirla sin comillas, porque es corta", "Cambiar una palabra y no citar", "Las palabras exactas ajenas siempre van entre comillas y con cita."),
        ("ab", "Escribes con tus palabras lo que explica una autora. ¿Debes citarla?", "Sí, porque la idea es de ella aunque cambies las palabras", "No, porque ya está escrito con tus propias palabras", "La idea sigue siendo de la autora, así que se reconoce."),
        ("abc", "{F} Copias la frase de ejemplo «Las costureras abrieron un taller común» de la Fuente A. ¿Cuál es la cita correcta?", "«Las costureras abrieron un taller común» (Lagos, 2019).", "«Las costureras abrieron un taller común» (Costureras del barrio).", "Las costureras abrieron un taller común, Lagos.", "La cita textual lleva comillas y entre paréntesis el apellido y el año."),
        ("abc", "{F} Parafraseas una idea del artículo de la Fuente B. ¿Qué cita escribes en el texto?", "(Reyes, 2021)", "(Pablo, Museo, 2021, marzo)", "(Fuente B)", "La cita en el texto lleva el apellido del autor y el año."),
        ("=", "{F} El libro de actas es de 1998 y el artículo web de 2021. ¿Cuántos años pasaron entre uno y otro?", "2021 - 1998", "Se restan los años de las dos fuentes para ver la distancia entre ellas.", "años"),
        ("{F} ¿Qué fuente no tiene autor persona y se cita por la institución que la guarda? Responde con la letra.", "C", "El libro de actas lo guarda el archivo municipal y no tiene autor persona."),
        ("ab", "Lucas copió un párrafo del Museo del Barrio y puso al final «Fuente: internet». ¿Cumple la norma de citación?", "No: faltan autor, año, título y sitio, y el párrafo debía ir entre comillas", "Sí: nombrar internet basta para reconocer la fuente", "Con «internet» nadie puede encontrar el texto original."),
        ("abc", "Elena explicó con otras palabras dos oraciones de un libro, sin citarlo. ¿Qué ocurrió?", "Plagio, porque usó una idea ajena sin reconocer a su autora", "Una paráfrasis correcta, porque cambió las palabras", "Una cita textual, porque habló de las mismas ideas", "Una paráfrasis también se cita; sin cita es plagio."),
        ("abc", "{F} ¿Cuál es la referencia correcta de la Fuente B?", "Reyes, P. (2021). La cooperativa de la calle Larga. Museo del Barrio. Consultado el 5 de marzo de 2024.", "Reyes, P. La cooperativa de la calle Larga (Museo del Barrio, 5 de marzo de 2024).", "Museo del Barrio. Pablo Reyes. 2021. Consultado la cooperativa.", "Sigue el orden del formato y agrega la fecha de consulta por ser un sitio web."),
        ("{F} Si usas las tres fuentes, ¿cuántas referencias llevará tu lista final? Escribe solo el número.", "3", "Cada fuente usada lleva su propia referencia en la lista."),
    ],
    ctx=("abc", "En tu trabajo para el centro de estudios quieres incluir una frase de un libro sobre el barrio. ¿Cómo la incluyes?", "Entre comillas y con el apellido de la autora y el año entre paréntesis", "Sin comillas, para que parezca tu texto", "Con otra letra, sin decir de quién es", "La cita textual necesita comillas y autoría."),
    sc=[("En Lengua y Literatura: ¿qué es una cita textual?", "Palabras copiadas exactas, entre comillas y con autor y año", "Se copian las palabras tal cual y se reconoce la autoría."),
        ("En Lengua y Literatura: ¿qué es una paráfrasis?", "Una idea ajena dicha con tus palabras, que también se cita", "Cambia las palabras pero la idea sigue siendo ajena."),
        ("En Lengua y Literatura: ¿qué es el plagio?", "Usar ideas o textos ajenos sin reconocer a su autor", "Se plagia al presentar como propio lo que otro creó.")],
    op=("{F} Escribe en tu cuaderno: (1) las tres referencias en el orden del formato; (2) una oración que parafrasee una idea de la Fuente B con su cita; (3) una oración con una cita textual de ejemplo de la Fuente A entre comillas y con su cita.",
        "Archivo municipal. (1998). Libro de actas de la cooperativa. Parafraseo: La cooperativa nació por iniciativa de las vecinas (Reyes, 2021).",
        ["las tres referencias siguen el formato", "la paráfrasis lleva cita y no usa comillas", "la cita textual lleva comillas, apellido y año"],
        ["tres referencias, una paráfrasis y una cita textual escritas"],
        ["olvidar la fecha de consulta del sitio web", "usar comillas en una paráfrasis"],
        "Pregunta de revisión: «¿Se puede encontrar la fuente solo con lo que escribí?»."),
    reinforce="Elige un libro o documento (puede ser inventado) y escribe su referencia con el formato de este cuaderno.",
    extend="Toma un párrafo de cuatro líneas que hayas escrito y marca qué ideas necesitan cita. Escribe cómo las citarías.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una investigación completa: elijo fuentes confiables, contrasto datos y los cito.",
    prior=["Evalúo fuentes con cinco preguntas.", "Escribo referencias y citas.", "Compruebo fechas y cifras."],
    explain=[
        "Investigar en un trabajo real significa tomar decisiones. Reúnes notas de varias fuentes, ves cuáles coinciden y descartas las que no tienen respaldo. Un dato que dos fuentes confiables e independientes repiten es más seguro que uno que dice una sola.",
        "Cuando dos fuentes dicen cosas distintas, no elijas la que te gusta más. Pregunta quién la escribió, cuándo y en qué se apoya. Si no puedes decidir, escribe ambas versiones y di que la información no coincide.",
        "Al escribir, cada dato lleva su cita. Una cifra exagerada, sin autor ni fecha, no se usa como hecho. Con tus notas ordenadas y citadas, el informe queda listo para organizarlo en la clase siguiente.",
    ],
    vocab=[("contraste", "comparación de un dato entre varias fuentes independientes"), ("coincidir", "decir lo mismo dos o más fuentes sobre un dato"), ("respaldo", "documento o prueba que apoya un dato"), ("dato dudoso", "dato sin fuente confiable que lo apoye")],
    worked=[
        ("Contrastar una cifra", "La entrevista y el registro dicen que la escuela comenzó con ocho estudiantes; un blog anónimo dice 500.", ["Dos fuentes confiables e independientes coinciden: ocho.", "El blog no tiene autor ni fecha y exagera."], "Uso «ocho estudiantes» y descarto la cifra del blog"),
        ("Escribir con cita", "Quiero decir que la escuela comenzó en 1996 según el registro de 2003.", ["Redacto el dato con claridad.", "Agrego la cita al final de la oración."], "La escuela se inició en 1996 con ocho estudiantes (Centro de oficios, 2003)."),
    ],
    mistakes=[("Elegir el dato más llamativo en lugar del mejor respaldado.", "Una cifra espectacular sin fuente confiable puede ser falsa.", "Elige el dato que apoyan fuentes confiables."),
              ("Usar un dato sin decir su fuente en el informe.", "El lector no puede comprobar nada.", "Pon la cita al lado de cada dato.")],
    T=[
        ("abc", "{F} ¿Qué dato sobre el primer año coincide en dos fuentes confiables?", "Que comenzó con ocho estudiantes (Fuentes A y B)", "Que tuvo 500 estudiantes (Fuente C)", "Que ofrecía tres oficios (Fuente D)", "Solo la cifra de ocho está en dos fuentes confiables independientes."),
        ("{F} ¿Cuántos estudiantes tenía la escuela en 2010 según la Fuente D? Escribe solo el número.", "120", "La nota 4 indica 120 estudiantes en 2010."),
        ("ab", "{F} ¿Por qué no conviene usar la Nota 3 como dato central?", "Su fuente no tiene autor ni fecha y exagera sin pruebas", "Porque está en un blog, y todos los blogs son falsos", "El problema es la falta de autor y respaldo, no el formato del blog."),
        ("=", "{F} Si en 1996 había 8 estudiantes y en 2010 había 120, ¿cuántos estudiantes más había en 2010?", "120 - 8", "Se restan los estudiantes iniciales a los de 2010 para ver el crecimiento.", "estudiantes"),
        ("abc", "{F} ¿Qué cita en el texto corresponde a la Nota 4?", "(Soto, 2010)", "(Irene, revista)", "(Fuente D, sin año)", "La cita lleva el apellido de la autora y el año."),
        ("abc", "{F} ¿Cuál es una oración bien escrita, con apoyo en fuentes, sobre el comienzo de la escuela?", "La escuela partió con dos salas, según una exalumna entrevistada (Radio comunitaria, 2017).", "La escuela partió con 500 estudiantes, según dicen en internet.", "Partió hace tiempo con algunas salas, creo que dos.", "La buena oración da el dato preciso, dice quién lo afirma y lleva su cita."),
        ("=", "{F} Desde 1996 hasta 2010, ¿cuántos años funcionó la escuela?", "2010 - 1996", "Se restan el año de inicio al año del dato más reciente.", "años"),
        ("ab", "{F} Las Notas 1 y 2 coinciden en ocho estudiantes, pero solo la Nota 1 dice «dos salas». ¿Cómo lo anotas?", "Anoto «ocho estudiantes» con las dos fuentes y «dos salas» solo con la entrevista", "Anoto «dos salas» con las dos fuentes, porque ya apareció", "Cada dato se atribuye solo a las fuentes que lo dicen."),
        ("abc", "{F} ¿Qué pregunta de investigación responden las Notas 1, 2 y 4?", "¿Cómo creció la escuela entre su inicio y 2010?", "¿Cuál fue el mejor maestro del mundo?", "¿Cuánto cuesta estudiar hoy en esa escuela?", "Las notas dan estudiantes de 1996 y 2010, es decir, el crecimiento."),
        ("abc", "Escribes: «En 2010 ofrecía tres oficios». ¿Qué falta para citar correctamente?", "Indicar la fuente, por ejemplo (Soto, 2010)", "Nada, porque es un dato breve", "Poner el dato en mayúsculas", "Todo dato tomado de una fuente lleva su cita."),
        ("ab", "{F} ¿Es suficiente usar solo la Fuente C para escribir la biografía?", "No, porque no es confiable y nada la respalda", "Sí, porque es la que más elogia a don Hernán", "Una fuente anónima y exagerada no basta para una biografía."),
        ("Ordena de la más antigua a la más reciente las Fuentes A, B y D, según su año (2017, 2003 y 2010). Escribe las letras separadas por comas.", "B, D, A", "Los años van 2003 (B), 2010 (D) y 2017 (A)."),
        ("abc", "{F} Tu informe dice «La escuela tuvo 500 estudiantes el primer año». ¿Cuál es la mejor corrección?", "Cambiarlo por ocho estudiantes en 1996, citando el registro de 2003 y la entrevista de 2017", "Dejarlo y agregar «según dicen»", "Cambiarlo por 120 estudiantes, que suena mejor", "El dato corregido se apoya en dos fuentes confiables y lleva cita."),
    ],
    ctx=("abc", "Preparas una nota para el boletín del centro sobre un maestro de oficios de tu comuna. Dos fuentes confiables dicen que abrió su taller en un año y un sitio sin firma dice otro. ¿Qué año usas?", "El que dicen las dos fuentes confiables, citándolas", "El del sitio sin firma, porque es más reciente", "Un año intermedio, para quedar bien con todas", "Se prefiere el dato apoyado por fuentes confiables independientes."),
    sc=[("En Lengua y Literatura: ¿qué es contrastar un dato?", "Compararlo con otras fuentes independientes", "Contrastar es comprobar un dato en varias fuentes."),
        ("En Lengua y Literatura: ¿qué haces si dos fuentes confiables dicen cosas distintas?", "Presento ambas versiones y digo que no coinciden", "No se elige la que gusta más sin razones."),
        ("En Lengua y Literatura: ¿dónde va la cita de un dato en un informe?", "Al lado del dato, en el texto, y la referencia completa al final", "Cita en el texto y referencia al final permiten comprobar.")],
    op=("{F} Con las notas de la ficha, escribe un párrafo de cinco a seis líneas sobre la escuela de don Hernán. Usa solo datos con fuente confiable, incluye al menos tres citas en el texto (por ejemplo, Soto, 2010) y escribe después la lista de referencias con las Fuentes A, B y D. Los datos de las referencias que falten, déjalos como «dato no entregado».",
        "La escuela nocturna se inició en 1996 con ocho estudiantes (Centro de oficios, 2003). En 2010 tenía 120 estudiantes y ofrecía tres oficios (Soto, 2010).",
        ["usa solo datos de fuentes confiables", "al menos tres citas en el texto", "incluye lista de referencias"],
        ["párrafo de cinco a seis líneas con tres citas y lista de referencias"],
        ["usar la cifra de 500 estudiantes", "olvidar citar una cifra"],
        "Pregunta de revisión: «¿Cada dato de mi párrafo tiene una fuente que otra persona pueda encontrar?»."),
    reinforce="Toma dos datos de la ficha y escribe cada uno en una oración con su cita.",
    extend="Imagina que una nueva fuente dice que la escuela comenzó en 1997. Escribe cómo presentarías la diferencia en tu informe.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso una investigación con una lista de verificación, decido qué falta y planeo los pasos siguientes.",
    prior=["Evalúo fuentes y las cito.", "Distingo opinión de dato.", "Sé usar una lista de verificación."],
    explain=[
        "Revisar una investigación es mirar tu trabajo con criterios, no con gustos. Una lista de verificación ayuda: pregunta clara, fuentes confiables, cada dato con su fuente, citas completas y lista de referencias.",
        "Al revisar, marca primero las opiniones y los datos sin fuente. Una opinión se puede dejar si se dice quién la sostiene; un dato sin fuente se reemplaza por uno con respaldo. Las citas textuales deben llevar comillas, autor y año.",
        "Cuando termines, decide los pasos siguientes: qué fuente falta, qué dato conviene confirmar y qué parte reescribir. La revisión también puede hacerla otra persona con respeto: se comenta el texto, no a quien lo escribió.",
    ],
    vocab=[("lista de verificación", "conjunto de criterios con que se revisa un trabajo"), ("opinión", "juicio personal que no se puede comprobar con documentos"), ("referencias", "lista final con los datos de cada fuente usada"), ("revisión", "lectura crítica de un trabajo para mejorarlo")],
    worked=[
        ("Marcar una opinión", "Frase de otro informe (ejemplo): «fue la dirigente más querida de la región».", ["Pregunto si se puede comprobar con un documento.", "No hay fecha, cifra ni hecho: es un juicio."], "Es una opinión: se reemplaza por un hecho con fuente"),
        ("Corregir una frase sin fuente", "Frase de otro informe (ejemplo): «Se comenta que la feria creció mucho».", ["No dice quién lo comenta.", "No da cifras ni fechas que se puedan comprobar."], "Se reemplaza por un dato con fuente o se elimina"),
    ],
    mistakes=[("Revisar solo la ortografía y no las fuentes ni las ideas.", "Un texto bien escrito puede estar mal respaldado.", "Primero revisa datos y citas; después, la ortografía."),
              ("Decir «está bien» sin leer con la lista de verificación.", "Sin criterios no se descubren los errores.", "Lee el trabajo con la lista y marca cada criterio.")],
    T=[
        ("abc", "{F} ¿Cuál afirmación del informe es una opinión y no un dato comprobable?", "«Fue la mejor dirigente de feria de todos los tiempos»", "«Fundó la Asociación de Ferias del Valle en 1990»", "«Organizó turnos de limpieza para los puestos»", "Quién fue «la mejor» es un juicio; la fundación y los turnos son hechos."),
        ("{F} ¿En qué año dice el informe que se fundó la Asociación? Escribe solo el número.", "1990", "El informe afirma que la Asociación se fundó en 1990."),
        ("ab", "{F} ¿Qué criterio de la lista incumple la frase «Fuente: internet»?", "El 5: falta una referencia completa con autor, año, título y sitio", "El 1: la pregunta no es clara", "«Internet» no entrega los datos completos de ninguna fuente."),
        ("abc", "{F} La frase «Dicen que ayudó a todos» es débil porque...", "No dice quién lo afirma ni da hechos que se puedan comprobar", "Es demasiado larga para un informe", "Usa la palabra «ayudó», que no se permite", "Un «dicen» sin autor ni hechos no se puede comprobar."),
        ("ab", "{F} A la frase entre comillas sobre los turnos de limpieza le falta...", "Indicar quién fue entrevistada y el año, por ejemplo (Radio del barrio, 2018)", "Más comillas al final", "Una cita textual necesita autoría y año para poder comprobarse."),
        ("abc", "{F} ¿Cuál es la mejor reescritura de la primera oración?", "Aurora Neira fue dirigente de feria y fundó la Asociación de Ferias del Valle en 1990 (Archivo municipal, 1990).", "Aurora Neira fue la mejor dirigente de todos los tiempos y todos lo saben.", "Aurora Neira creo que fundó algo en 1990, más o menos.", "La mejor versión reemplaza la opinión por un hecho con su cita."),
        ("=", "{F} Si la Asociación se fundó en 1990 y la entrevista es de 2018, ¿cuántos años pasaron entre ambas fuentes?", "2018 - 1990", "Se restan los años de las dos fuentes para ver la distancia entre ellas.", "años"),
        ("abc", "{F} ¿Qué fuentes debería incluir la lista de referencias final?", "El acta de fundación (1990) y la entrevista de la radio del barrio (2018)", "Solo «internet»", "Ninguna, porque son datos conocidos del barrio", "Debe listar cada fuente realmente usada, con datos completos."),
        ("ab", "{F} ¿Cumple el informe el criterio 3 (cada dato con su fuente)?", "No: el dato de 1990 aparece sin decir de qué fuente sale", "Sí, porque al final aparece la palabra «fuente»", "Escribir «fuente» no reemplaza citar cada dato."),
        ("abc", "{F} ¿Qué paso conviene primero para mejorar el informe?", "Marcar opiniones y datos sin fuente y reemplazarlos por datos con fuente", "Alargar el texto con más elogios", "Corregir solo las tildes y dejar el resto igual", "Primero se mejora el respaldo de los datos; la forma después."),
        ("ab", "Dos estudiantes revisan un informe. Una persona marca errores con la lista y propone cambios; la otra dice «está bien» sin leerlo. ¿Qué revisión ayuda más?", "La primera, porque usa criterios y propone cambios concretos", "La segunda, porque no desanima a quien escribió", "Una revisión útil usa criterios y se dice con respeto."),
        ("{F} Según la ficha, ¿cuántas fuentes consultó la estudiante? Escribe solo el número.", "2", "Consultó el acta de fundación y la entrevista de la radio."),
        ("abc", "{F} Si usas la entrevista de 2018 en una frase textual, ¿qué cita pones después de las comillas?", "(Radio del barrio, 2018)", "(entrevista)", "(Radio, internet)", "La cita lleva autor o institución y año."),
    ],
    ctx=("abc", "Tu centro de estudios pide un informe de una página sobre una persona importante de tu comuna. Ya reuniste los datos. ¿Qué haces antes de entregar?", "Revisar con una lista que cada dato tenga fuente y que las citas estén completas", "Entregarlo de inmediato para no atrasarte", "Borrar las fuentes para que se vea más limpio", "Una revisión con criterios asegura datos comprobables."),
    sc=[("En Lengua y Literatura: ¿para qué sirve una lista de verificación?", "Para revisar un trabajo con criterios claros", "Ordena la revisión en pasos y criterios."),
        ("En Lengua y Literatura: ¿cómo se corrige una opinión sin respaldo?", "Se reemplaza por un hecho con fuente o se dice quién la sostiene", "Un hecho con fuente reemplaza al juicio sin respaldo."),
        ("En Lengua y Literatura: ¿qué debe tener cada referencia?", "Autor o institución, año, título y sitio o editorial", "Con esos datos se puede encontrar la fuente.")],
    op=("{F} Revisa el informe con la lista de verificación. En tu cuaderno marca con una cruz cada criterio que no cumple, escribe qué frase lo muestra y reescribe el informe en cuatro o cinco líneas con la información de las dos fuentes consultadas. Al final, escribe dos pasos siguientes para mejorar la investigación.",
        "Criterio 3 no cumple: «Fundó la Asociación en 1990» no dice su fuente. Reescritura: Aurora Neira fundó la Asociación de Ferias del Valle en 1990 (Archivo municipal, 1990). Paso siguiente: buscar una tercera fuente.",
        ["identifica criterios que no se cumplen con frases concretas", "reescribe con datos y citas", "propone dos pasos siguientes realistas"],
        ["lista de criterios marcada, reescritura de cuatro o cinco líneas y dos pasos siguientes"],
        ["cambiar solo la ortografía", "agregar elogios en lugar de datos"],
        "Pregunta de revisión: «¿Una persona que no me conoce podría encontrar cada dato en su fuente?»."),
    reinforce="Revisa un mensaje o un aviso que hayas escrito esta semana con tres preguntas de la lista de verificación.",
    extend="Escribe una lista de verificación propia de cinco criterios para revisar una investigación y pídele a otra persona que la use con tu trabajo.",
)

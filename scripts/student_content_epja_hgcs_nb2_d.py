"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 4 (parte 1): OAD-13, comunicar ideas con un afiche sobre los Derechos Humanos a partir de fuentes confiables. Todo en papel; datos de ejemplo rotulados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma; si quieres, lápices de colores. Todo se resuelve con lo escrito en la ficha: los afiches, tablas y fuentes son de ejemplo y no se usa internet."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-13"
PRIOR = ["Ya he visto afiches en el paradero, el consultorio o la municipalidad.", "Sé que hay cosas que toda persona merece, como respeto y atención."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ====================================================== clase 1
F = ("Ficha 1 (situaciones de ejemplo). Situación 1: a una mujer le pagan menos que a un compañero por la misma tarea, solo por ser mujer. "
     "Situación 2: una vecina publica en el boletín del barrio su opinión sobre el servicio de la micro. "
     "Situación 3: un joven de 16 años retoma sus estudios en una escuela para personas jóvenes y adultas. "
     "Situación 4: una persona mayor pide hora y es atendida en el consultorio.")
K(1, F,
  "Hoy reconozco qué son los derechos humanos y en qué situaciones de la vida diaria se ven, para después comunicarlos en un afiche.",
  ["Los derechos humanos son las condiciones básicas que tiene toda persona por el solo hecho de serlo: vivir con dignidad, ser tratada con igualdad, estudiar, atenderse en salud, expresar sus ideas. Tú ya los reconoces cuando haces una fila en el consultorio o pides un certificado.",
   "Son universales: valen para todas las personas, sin importar su origen, edad, sexo, religión u oficio. Nadie los gana ni los pierde por portarse bien o mal. Tampoco se pueden quitar, por eso se dice que son inalienables.",
   "En 1948 la Asamblea General de las Naciones Unidas aprobó la Declaración Universal de Derechos Humanos, que tiene 30 artículos. Hoy leemos situaciones cotidianas y decimos qué derecho está presente; en las próximas clases lo comunicaremos con un afiche."],
  [("derecho humano", "condición básica que tiene toda persona por ser persona"), ("dignidad", "el valor que tiene toda persona"), ("universal", "que vale para todas las personas"), ("discriminar", "tratar peor a alguien por una característica suya, como su sexo, origen o edad")],
  [("Nombrar el derecho", "Un hombre pide un certificado y le atienden con respeto, igual que a las demás personas de la fila. ¿Qué principio se ve?", ["Veo que todas las personas reciben el mismo trato.", "Ese trato parejo es la igualdad."], "Igualdad en el trato"),
   ("Detectar una falta", "En un taller, a una persona la dejan fuera de una charla solo por ser migrante. ¿Se respetan los derechos?", ["Se le trata peor por su origen.", "Eso es discriminar y va contra la igualdad."], "No: hay discriminación por origen")],
  [("Pensar que los derechos humanos valen solo para quien cumple la ley.", "Se confunden los derechos con un premio por buena conducta.", "Recuerda: son de todas las personas, siempre."),
   ("Creer que un derecho es un favor que la autoridad puede dar o quitar.", "Se mira el derecho como permiso y no como condición propia de toda persona.", "Di: «es mi derecho», no «me hicieron el favor».")],
  [("abc", "{F} ¿Qué derecho se ve en la situación 3, la del joven que retoma sus estudios?", "La educación", "La libertad de expresión", "La atención de salud", "Retomar los estudios en una escuela es ejercer el derecho a la educación."),
   ("ab", "{F} ¿Qué derecho se ve en la situación 4, la de la persona mayor atendida en el consultorio?", "La salud", "La educación", "Ir a un consultorio y recibir atención corresponde al derecho a la salud."),
   ("Según esta clase, ¿en qué año aprobó la Asamblea General de la ONU la Declaración Universal de Derechos Humanos?", "1948", "La Asamblea General de las Naciones Unidas la aprobó en 1948, como dice la explicación."),
   ("abc", "¿Qué significa que los derechos humanos son universales?", "Que valen para todas las personas", "Que valen solo para las personas adultas", "Que valen solo en el país donde se escribieron", "Universal quiere decir para todas las personas, sin excepción de edad ni lugar."),
   ("ab", "¿Cuál frase explica mejor la palabra dignidad?", "El valor que tiene toda persona", "El dinero que gana una persona", "La dignidad no depende del dinero: es el valor propio de cada persona."),
   ("abc", "{F} En la situación 1 pagan menos a una mujer solo por ser mujer. ¿Cómo se llama esa conducta?", "Discriminación", "Participación", "Responsabilidad", "Tratar peor a alguien por una característica suya, como su sexo, es discriminar."),
   ("abc", "Una persona recién llegada de otro país y otra nacida en el barrio viven en la misma calle. ¿Cuál de las dos tiene derechos humanos?", "Las dos, por igual", "Solo la nacida en el barrio", "Solo la recién llegada", "Los derechos humanos son universales, así que no dependen del lugar de nacimiento."),
   ("abc", "{F} ¿En cuál situación se ejerce el derecho a expresar opiniones?", "Situación 2, la vecina que opina en el boletín", "Situación 3, el joven que estudia", "Situación 4, la atención en el consultorio", "Publicar una opinión sobre la micro es ejercer la libertad de expresión."),
   ("{F} De las cuatro situaciones, ¿cuántas muestran un derecho que se respeta y no una falta?", "3", "Las situaciones 2, 3 y 4 muestran derechos que se ejercen; solo la 1 muestra discriminación."),
   ("abc", "Un vecino dice: «los derechos humanos son favores de las autoridades». ¿Qué error tiene esa idea?", "Los derechos no se piden como favor: toda persona los tiene", "Ninguno, porque las autoridades los reparten", "Que solo valen para las autoridades", "Los derechos pertenecen a las personas; las autoridades deben respetarlos, no regalarlos."),
   ("ab", "¿Por qué se dice que los derechos humanos son inalienables?", "Porque no se pueden quitar a nadie", "Porque solo los tiene quien los pide", "Inalienable significa que no se puede quitar ni transferir a otra persona."),
   ("abc", "En una fila de trámites, el funcionario atiende primero a un conocido y deja esperando a quien llegó antes. ¿Qué principio no se respeta?", "La igualdad en el trato", "La libertad de expresión", "El derecho a la educación", "Atender por amistad y no por orden de llegada rompe el trato igualitario."),
   ("abc", "Una ficha dice: (1) «Todas las personas nacen libres e iguales en dignidad». (2) «Cada país decide qué personas merecen derechos». ¿Cuál es coherente con el carácter universal?", "Solo la afirmación 1", "Solo la afirmación 2", "Las dos afirmaciones", "Si los derechos son universales, no los decide un país persona por persona.")],
  ("abc", "En la sede de una junta de vecinos aparece un cartel: «Solo quienes viven aquí hace diez años pueden usar la posta». ¿Qué idea de derechos humanos contradice?", "Que son universales y no dependen de la antigüedad", "Que cada persona debe pagar para atenderse", "Que las opiniones deben ser breves", "El derecho a la salud no se limita por cuántos años alguien vive en un lugar."),
  [("En Historia: ¿qué son los derechos humanos?", "Condiciones básicas que tiene toda persona por ser persona", "Se tienen por ser persona, no por mérito ni por permiso."),
   ("En la explicación de esta clase, ¿cuántos artículos tiene la Declaración Universal que aprobó la ONU?", "30", "El documento aprobado en 1948 reúne 30 artículos."),
   ("En Historia: ¿qué es discriminar?", "Tratar peor a alguien por una característica suya", "Se discrimina cuando se perjudica a alguien por su origen, sexo, edad u otra condición.")],
  ("Lee estas tres situaciones de ejemplo. (a) Una persona con discapacidad visual pide que le lean un formulario y se lo leen. (b) A una persona la rechazan en un arriendo por su origen. (c) Un grupo de vecinos presenta una petición por escrito a la municipalidad. Para cada una escribe el derecho o principio y si se respeta o no.",
   "(a) Igualdad y acceso a la información: se respeta. (b) Igualdad y no discriminación: no se respeta.",
   ["nombra un derecho o principio en cada situación", "dice si se respeta o no", "usa palabras como igualdad, dignidad o discriminación"],
   ["tres frases escritas en el cuaderno"],
   ["decir solo «es malo» sin nombrar el derecho", "creer que el derecho depende del origen de la persona"],
   "Pregunta: «¿Qué derecho está en juego y quién lo ejerce?»."),
  "Mira un afiche o aviso de tu barrio y di qué derecho podría comunicar.",
  "Escribe dos situaciones de un lugar público en que se respete la igualdad y una en que no.")

# ====================================================== clase 2
F = ("Ficha 2 (tarjetas de ejemplo). A: «El consultorio atiende a todas las personas inscritas». B: «Yo cuido la plaza y no boto basura». "
     "C: «Tengo derecho a opinar en la reunión de vecinos». D: «El Estado ofrece escuelas públicas». E: «Escucho a quien piensa distinto sin gritar». "
     "F: «Llego a la reunión a la hora acordada».")
K(2, F,
  "Hoy distingo cuatro palabras clave: derecho, deber del Estado, responsabilidad de las personas y actitud cívica, para usarlas bien en un afiche.",
  ["Un derecho es algo que puedes ejercer y exigir: estudiar, atenderte en salud, opinar. Un deber del Estado es lo que las instituciones públicas deben hacer para que los derechos se cumplan: ofrecer escuelas, consultorios, justicia y seguridad.",
   "Las personas también tenemos responsabilidades: respetar los derechos de los demás, cumplir las normas acordadas y cuidar lo que es común, como la plaza o la sede del barrio. Tener un derecho no quita la responsabilidad de respetar el de otros.",
   "Una actitud cívica es una forma de actuar que cuida la vida en común: respeto, diálogo, solidaridad y participación. Para escribir un afiche necesitas estas palabras con precisión. Estado, en Historia, es el conjunto de instituciones públicas que organizan y sirven a un país."],
  [("Estado", "conjunto de instituciones públicas de un país, como escuelas públicas, consultorios y tribunales"), ("deber del Estado", "lo que las instituciones públicas deben hacer para que los derechos se cumplan"), ("responsabilidad", "hacerse cargo de lo que uno hace y respetar a los demás"), ("actitud cívica", "forma de actuar que cuida la vida en común")],
  [("Clasificar una frase", "«La municipalidad mantiene el alumbrado de la calle». ¿Es derecho, deber del Estado o responsabilidad de las personas?", ["Alumbrar la calle lo hace una institución pública.", "Lo que hace una institución para servir a todos es un deber del Estado."], "Deber del Estado"),
   ("Reconocer una actitud cívica", "En una reunión, una persona espera su turno y escucha a quien piensa distinto. ¿Qué actitud muestra?", ["Espera y escucha sin gritar.", "Eso es respeto y diálogo."], "Actitud cívica de respeto y diálogo")],
  [("Creer que el Estado es solo el presidente o el gobierno de turno.", "Se reduce el Estado a una persona.", "Piensa en el conjunto de instituciones públicas, que continúa más allá de cada gobierno."),
   ("Pensar que tener derechos significa no tener responsabilidades.", "Se olvida que los derechos de los demás también deben respetarse.", "Un derecho se ejerce respetando el derecho de otros.")],
  [("abc", "{F} ¿Qué tarjeta muestra un deber del Estado?", "D, las escuelas públicas", "B, cuidar la plaza", "F, llegar a la hora", "Ofrecer escuelas públicas es algo que una institución del Estado debe hacer."),
   ("ab", "{F} ¿La tarjeta C, opinar en la reunión de vecinos, es un derecho o una responsabilidad?", "Un derecho", "Una responsabilidad", "Opinar es algo que la persona puede ejercer: es un derecho."),
   ("abc", "¿Qué es el Estado, según esta clase?", "Conjunto de instituciones públicas de un país", "Solo la persona que preside el país", "El conjunto de empresas privadas", "El Estado reúne instituciones como escuelas públicas, consultorios y tribunales."),
   ("abc", "{F} ¿Qué tarjetas muestran responsabilidades de las personas?", "B y F", "A y D", "C y E", "Cuidar la plaza y llegar a la hora son compromisos de la persona con los demás."),
   ("ab", "{F} La tarjeta E dice «Escucho a quien piensa distinto sin gritar». ¿Qué muestra?", "Una actitud cívica de respeto", "Un deber del Estado", "Escuchar sin gritar es una forma de actuar que cuida la convivencia."),
   ("abc", "¿Cuál es un ejemplo de deber del Estado?", "Mantener consultorios públicos abiertos", "Llevar la basura a un punto limpio", "Opinar en una reunión del barrio", "Los consultorios públicos los mantiene una institución del Estado."),
   ("abc", "Una persona dice: «Tengo derecho a todo, así que puedo gritarle a quien me atiende». ¿Qué falla en su idea?", "Ejercer un derecho no permite faltar el respeto a otra persona", "Nada: los derechos no tienen límites", "Que no debería atenderse en un consultorio", "El derecho propio se ejerce respetando los derechos de los demás."),
   ("abc", "{F} Si juntas las tarjetas A y D, ¿qué tienen en común?", "Muestran servicios que presta el Estado", "Muestran faltas de respeto", "Muestran opiniones personales", "Atender en el consultorio y ofrecer escuelas son servicios públicos."),
   ("{F} ¿Cuántas de las seis tarjetas describen algo que hace una persona (una responsabilidad o una actitud) y no un derecho ni un deber del Estado?", "3", "Son las tarjetas B, E y F; la A y la D son del Estado y la C es un derecho."),
   ("abc", "{F} ¿Cuál tarjeta mezcla mejor una acción de la persona con el cuidado de un espacio compartido?", "B, cuidar la plaza", "A, atender a las personas inscritas", "D, ofrecer escuelas públicas", "Cuidar la plaza es algo que hace la persona en beneficio de todos."),
   ("ab", "Una persona deja basura en la plaza y dice: «para eso paga impuestos el municipio». ¿Qué opinas?", "También es una responsabilidad de las personas cuidar lo común", "Tiene razón: cuidar la plaza es solo del municipio", "Cuidar el espacio de todos no es solo tarea del municipio, también de quien lo usa."),
   ("abc", "El consultorio se queda sin horas por la tarde. ¿Qué derecho se ve afectado y quién debe responder?", "El derecho a la salud, y debe responder la institución pública", "El derecho a opinar, y debe responder el vecino", "El derecho a la educación, y debe responder la junta", "Ofrecer atención de salud accesible es deber de las instituciones públicas."),
   ("abc", "Una reunión vecinal vota con calma, aunque unas personas pierden. ¿Qué actitud cívica se destaca?", "Aceptar el resultado y seguir dialogando", "Dejar de ir a las reuniones", "Imponer su idea al día siguiente", "Dialogar y aceptar resultados acordados es una actitud cívica.")],
  ("abc", "Un afiche del barrio dice: «Sé tu derecho, cuida lo nuestro». ¿Qué combina ese mensaje?", "Un derecho y una responsabilidad", "Un deber del Estado y una multa", "Una opinión y un chiste", "Habla de conocer un derecho y de cuidar lo común, que es responsabilidad."),
  [("En Historia: ¿qué es un deber del Estado?", "Lo que las instituciones públicas deben hacer para que los derechos se cumplan", "Se refiere a servicios e instituciones públicas que protegen derechos."),
   ("Para un afiche de derechos humanos, ¿qué es una actitud cívica?", "Una forma de actuar que cuida la vida en común", "Incluye respeto, diálogo, solidaridad y participación."),
   ("¿Qué es una responsabilidad de las personas?", "Respetar a los demás y cuidar lo común", "Es lo que cada persona hace para no dañar a otros ni a los bienes de todos.")],
  ("Con estas seis frases: (1) La escuela pública tiene profesores. (2) Respeto el turno en la fila. (3) Puedo opinar en la junta de vecinos. (4) El tribunal atiende reclamos. (5) Separo la basura. (6) El consultorio atiende a mi barrio. Escribe una columna «Derecho», otra «Deber del Estado» y otra «Responsabilidad de las personas» y ubica cada número.",
   "Derecho: 3. Deber del Estado: 1, 4 y 6. Responsabilidad de las personas: 2 y 5.",
   ["ubica las seis frases en una columna", "explica una decisión con una razón", "usa las palabras del vocabulario"],
   ["una tabla de tres columnas en el cuaderno"],
   ["poner todo en una sola columna", "creer que el Estado es una sola persona"],
   "Pregunta: «¿Quién actúa en esta frase: una institución o una persona?»."),
  "Escribe una frase propia para cada una de las tres columnas.",
  "Piensa en un servicio público que usas y escribe qué derecho lo respalda.")

# ====================================================== clase 3
F = ("Ficha 3 (borrador de afiche de ejemplo). Título: «Todas las personas, mismos derechos». Imagen: tres siluetas de distinta altura de pie bajo un mismo techo. "
     "Texto pequeño: «La Declaración Universal de Derechos Humanos fue aprobada el 10 de diciembre de 1948. Fuente: Naciones Unidas». "
     "Colores: letras amarillas claras sobre fondo blanco. Público: vecinos y vecinas de un barrio.")
K(3, F,
  "Hoy aprendo, paso a paso, cómo se construye un afiche claro: mensaje, público, lema, imagen, dato con fuente y colores legibles.",
  ["Un afiche es un cartel que comunica una idea a quien pasa y lo mira por pocos segundos. Por eso lleva una sola idea central, un lema corto y una imagen que ayuda a entenderla. Tú ya has leído afiches en el paradero o el consultorio.",
   "Los pasos son: primero, decidir el mensaje en una frase; segundo, pensar en el público; tercero, escribir un lema de pocas palabras; cuarto, elegir una imagen sencilla; quinto, agregar un dato con su fuente; y por último, revisar que las letras se lean desde lejos.",
   "Para un afiche de derechos humanos, el dato debe venir de una fuente confiable, y se anota su nombre en letra pequeña. El contraste importa: letras oscuras sobre fondo claro se leen mejor que letras claras sobre fondo claro."],
  [("afiche", "cartel que comunica una idea con texto breve e imagen"), ("lema", "frase muy corta que resume el mensaje"), ("público", "las personas a quienes va dirigido el mensaje"), ("contraste", "diferencia entre el color de las letras y el del fondo que permite leer bien")],
  [("Del mensaje al lema", "Mensaje: «Todas las personas merecen ser atendidas con respeto en el consultorio». Escribe un lema de hasta seis palabras.", ["Quito lo secundario y dejo la idea central.", "Cuento las palabras para que no pasen de seis."], "«Atención respetuosa para todas las personas» (6 palabras)"),
   ("Revisar el contraste", "Un afiche tiene letras azul oscuro sobre fondo celeste claro. ¿Se lee bien?", ["Comparo lo oscuro de las letras con lo claro del fondo.", "Hay buena diferencia entre ambos colores."], "Sí, el contraste es bueno")],
  [("Poner muchos mensajes en un solo afiche.", "Se quiere decir todo y el público no sabe qué recordar.", "Elige una idea central y apóyala con un lema."),
   ("Usar letras muy pequeñas para el lema y grandes para el dato de la fuente.", "Se invierte la importancia de los elementos.", "El lema va grande; la fuente va pequeña, pero visible.")],
  [("abc", "{F} ¿Cuál es el lema del borrador?", "«Todas las personas, mismos derechos»", "«La Declaración Universal de Derechos Humanos»", "«Fuente: Naciones Unidas»", "El lema es el título corto y destacado que resume el mensaje."),
   ("ab", "{F} ¿A quién va dirigido el afiche?", "A vecinos y vecinas de un barrio", "A turistas de otro país", "La ficha señala que el público son los vecinos y vecinas del barrio."),
   ("abc", "¿Cuál es el primer paso para construir un afiche?", "Decidir el mensaje en una frase", "Elegir los colores del marco", "Pedir una imagen a otra persona", "Sin un mensaje claro, el resto de las decisiones no tiene guía."),
   ("{F} ¿Cuántas palabras tiene el lema «Todas las personas, mismos derechos»?", "5", "Se cuentan: Todas, las, personas, mismos, derechos; son cinco palabras."),
   ("abc", "{F} ¿Qué problema tiene el color de las letras del borrador?", "Poco contraste: amarillo claro sobre blanco se lee mal", "Demasiado contraste con el fondo", "Que usa mayúsculas", "Las letras amarillas claras sobre fondo blanco casi desaparecen."),
   ("abc", "{F} ¿Qué parte del borrador indica de dónde viene el dato?", "El texto pequeño «Fuente: Naciones Unidas»", "La imagen de las tres siluetas", "El título del afiche", "La fuente se anota al final del dato, en letra pequeña."),
   ("abc", "Un afiche tiene el lema en letra muy pequeña y cinco párrafos largos. ¿Qué conviene hacer?", "Dejar una idea central, un lema grande y poco texto", "Agregar más párrafos", "Quitar la imagen y el lema", "Un afiche se lee en pocos segundos, así que necesita pocas palabras."),
   ("abc", "{F} ¿Cuál es la fecha que menciona el dato del borrador?", "10 de diciembre de 1948", "1 de enero de 2000", "10 de diciembre de 1984", "El texto pequeño del borrador dice que la Declaración se aprobó el 10 de diciembre de 1948."),
   ("ab", "{F} ¿La imagen de tres siluetas de distinta altura bajo un mismo techo apoya el lema?", "Sí: muestra personas distintas con los mismos derechos", "No: no tiene relación con el lema", "Siluetas distintas bajo un mismo techo representan igualdad en la diferencia."),
   ("abc", "¿Cuál de estos lemas es el más adecuado para un afiche?", "«Respeta, escucha, participa»", "«Todas las personas que viven en un lugar tienen una serie de derechos que deben respetarse siempre»", "«Derechos»", "Es breve y tiene tres acciones claras; el largo no se lee de pasada y la sola palabra no comunica."),
   ("ab", "Una persona dice: «Un afiche necesita mucho texto para ser serio». ¿Qué respuesta es correcta?", "No: un afiche eficaz usa poco texto y una idea clara", "Sí: mientras más texto, más serio", "El afiche se lee en pocos segundos, por eso el texto debe ser breve."),
   ("abc", "Se quiere un afiche para el derecho a la educación dirigido a jóvenes y adultos. ¿Cuál es el mejor lema?", "«Estudiar también es un derecho»", "«Estudiar solo cuando hay tiempo»", "«Los exámenes son difíciles»", "Comunica el derecho y se dirige a todas las edades."),
   ("abc", "{F} Para mejorar el borrador, ¿cuál cambio es el más útil?", "Pasar las letras a un color oscuro", "Quitar la fuente", "Agregar cinco datos más", "El contraste mejora la lectura y la fuente debe permanecer.")],
  ("abc", "Un centro comunitario quiere un afiche sobre el derecho a ser atendido con respeto. ¿Cuál orden de pasos es mejor?", "Mensaje, público, lema, imagen, dato con fuente, revisión", "Colores, imagen, lema, mensaje, público", "Dato sin fuente, lema, imagen", "Primero se define la idea y a quién va dirigida; después se diseña."),
  [("En Historia: ¿qué es un afiche?", "Un cartel que comunica una idea con texto breve e imagen", "Se lee de pasada, por eso es breve."),
   ("¿Para qué sirve el lema?", "Para resumir el mensaje en pocas palabras", "Es la frase que la gente recuerda del afiche."),
   ("¿Qué mejora la lectura de las letras de un afiche?", "El contraste con el fondo", "Letras oscuras sobre fondo claro, o al revés, se distinguen bien.")],
  ("Usa este mensaje: «Todas las personas merecen ser tratadas con respeto en los trámites públicos». Escribe: (1) un lema de hasta seis palabras, (2) una imagen sencilla que lo apoye, descrita en una frase, (3) un público al que va dirigido, (4) los colores de letras y fondo.",
   "Lema: «Trato respetuoso en todo trámite». Imagen: dos personas en una ventanilla dándose la mano. Público: personas que hacen trámites. Colores: letras negras sobre fondo amarillo claro.",
   ["el lema tiene seis palabras o menos", "la imagen apoya el lema", "indica un público y colores con buen contraste"],
   ["cuatro frases escritas en el cuaderno o un boceto con los cuatro elementos"],
   ["lema demasiado largo", "letras claras sobre fondo claro"],
   "Pregunta: «¿Se entiende el mensaje en cinco segundos?»."),
  "Cuenta las palabras del lema de tu boceto y quita las que no hacen falta.",
  "Imagina el mismo mensaje para otro público y cambia el lema.")

# ====================================================== clase 4
F = ("Ficha 4 (fuentes de ejemplo para un afiche sobre el derecho a la educación). Fuente A: página de una institución pública de educación (ficha de ejemplo), con nombre de la institución, fecha de actualización y texto completo. "
     "Fuente B: mensaje reenviado por chat, sin autor ni fecha, que dice: «el 95 % de las personas no sabe sus derechos». Fuente C: libro de la biblioteca pública sobre derechos humanos, con autor, editorial y año. "
     "Fuente D: publicación de una cuenta anónima en una red social, sin origen del dato. Encuesta de ejemplo de un centro vecinal: de 80 personas consultadas, 62 conocían el derecho a reclamar.")
K(4, F,
  "Hoy practico cómo elegir información confiable para un afiche y cómo anotar la fuente junto al dato.",
  ["Un afiche sobre derechos humanos necesita datos verdaderos. Antes de usar un dato, mira de dónde viene: ¿quién lo dice, cuándo lo dijo y cómo lo sabe? Una fuente confiable muestra su autor o institución, su fecha y de dónde sacó la información.",
   "Un mensaje reenviado sin autor ni fecha no sirve de base, aunque suene convincente. Un libro de biblioteca con autor y año, o una página de una institución pública con fecha, ofrece una base mejor. Si dudas, busca el mismo dato en una segunda fuente.",
   "Cuando uses un dato en el afiche, escribe la fuente en letra pequeña: su nombre y el año. Si la cifra viene de una encuesta, di cuántas personas se consultaron. Así quien lee puede comprobarla y confía más en tu mensaje."],
  [("fuente", "lugar o persona de donde viene una información"), ("confiable", "que se puede creer porque muestra quién lo dice, cuándo y de dónde lo sacó"), ("dato", "información concreta, como una cifra o una fecha"), ("contrastar", "comparar un dato con otra fuente para ver si coincide")],
  [("Elegir la mejor fuente", "Hay dos fuentes sobre el derecho a la salud: un mensaje de chat sin autor y una página de una institución pública con fecha. ¿Cuál usas?", ["Reviso si muestran autor y fecha.", "La página muestra ambos; el mensaje no."], "La página de la institución pública"),
   ("Calcular una proporción", "Una encuesta de ejemplo consultó a 50 personas y 40 conocían un derecho. ¿Cuántas no lo conocían?", ["Resto lo que conocen al total: 50 − 40.", "Anoto el resultado como parte del dato."], "10 personas")],
  [("Usar un dato porque «lo dijo mucha gente» en un chat.", "Se confunde popularidad con confiabilidad.", "Busca autor, fecha y origen del dato."),
   ("Copiar la cifra y no anotar la fuente en el afiche.", "Se olvida que el lector necesita comprobar.", "Escribe el nombre de la fuente y el año junto al dato.")],
  [("abc", "{F} ¿Cuál fuente muestra su institución, fecha y texto completo?", "Fuente A", "Fuente B", "Fuente D", "La fuente A es la única de las tres que indica institución y fecha."),
   ("ab", "{F} ¿Qué falta en la fuente B, el mensaje de chat?", "Autor y fecha", "Una imagen", "No dice quién lo escribió ni cuándo, y eso impide comprobarlo."),
   ("abc", "{F} ¿Cuál es el dato de la encuesta del centro vecinal?", "62 de 80 personas conocían el derecho a reclamar", "80 de 62 personas conocían el derecho a reclamar", "El 95 % conocía el derecho a reclamar", "La ficha dice que de 80 personas consultadas, 62 conocían el derecho."),
   ("=", "{F} En la encuesta de ejemplo, ¿cuántas de las 80 personas consultadas no conocían el derecho a reclamar?", "80-62", "Se resta lo que sí conocían al total consultado.", " personas"),
   ("abc", "{F} ¿Cuál fuente permite saber quién escribió, quién publicó y en qué año?", "Fuente C, el libro de la biblioteca", "Fuente D, la cuenta anónima", "Fuente B, el chat reenviado", "El libro muestra autor, editorial y año; las otras no."),
   ("ab", "{F} ¿Se puede usar como base del afiche la afirmación de la fuente B, «el 95 % no sabe sus derechos»?", "No, porque no muestra autor, fecha ni origen", "Sí, porque es un dato muy alto", "Una cifra sin origen no se puede comprobar, por llamativa que sea."),
   ("abc", "Para el afiche necesitas un dato sobre la Declaración Universal. ¿Cuál es la mejor práctica?", "Buscarlo en una fuente con autor y fecha y anotarla en el afiche", "Copiar el dato del primer mensaje que llega", "Inventar un dato parecido", "Una fuente identificable permite que otros comprueben el dato."),
   ("abc", "Dos fuentes dan fechas distintas para un mismo hecho histórico. ¿Qué haces?", "Contrastar con una tercera fuente confiable", "Elegir la fecha que te guste más", "Sacar la fecha del afiche y no decir nada", "Contrastar con otra fuente ayuda a decidir cuál dato es correcto."),
   ("abc", "{F} ¿Cuál fuente es la menos útil para respaldar una cifra en el afiche?", "Fuente D, la cuenta anónima sin origen", "Fuente A, la institución pública", "Fuente C, el libro de la biblioteca", "Sin autor ni origen nadie puede comprobar lo que dice la publicación anónima."),
   ("{F} Si usas la encuesta en el afiche, ¿qué dato de la cantidad total debes incluir?", "80 personas consultadas", "Para entender una proporción hay que decir cuántas personas se consultaron."),
   ("ab", "Una persona argumenta: «si lo leí en tres chats distintos, es confiable». ¿Es correcto?", "No: tres chats pueden repetir el mismo mensaje sin origen", "Sí: la repetición lo vuelve confiable", "Repetirse no prueba que algo sea cierto, hay que ver el origen."),
   ("abc", "¿Cuál es una forma correcta de anotar la fuente en el afiche?", "Fuente: nombre de la institución, año", "Fuente: me lo dijeron", "Fuente: internet", "Debe nombrar quién lo publicó y cuándo, para poder ubicarlo."),
   ("abc", "{F} Si quieres decir en el afiche «casi 8 de cada 10 personas consultadas conocían el derecho», ¿qué cifra de la encuesta lo respalda?", "62 de 80, que es algo menos de 8 de cada 10", "95 % de las personas", "40 de 80", "62 de 80 equivale a 77,5 de cada 100, es decir, cerca de 8 de cada 10.")],
  ("abc", "Una persona quiere afichar «El derecho a la educación está en la Declaración Universal de 1948». ¿Qué fuente la respalda mejor?", "El texto de la Declaración publicado por una institución, con fecha", "Un mensaje reenviado sin autor", "Un comentario en una red social", "La fuente institucional con fecha puede comprobarse; los otros no."),
  [("En Historia: ¿qué es una fuente?", "Lugar o persona de donde viene una información", "Una fuente puede ser un libro, un documento o una página institucional."),
   ("¿Qué muestra una fuente confiable?", "Quién lo dice, cuándo y de dónde sacó el dato", "Esos tres datos permiten comprobar la información."),
   ("Al elegir un dato para un afiche, ¿qué significa contrastar?", "Comparar un dato con otra fuente", "Si dos fuentes confiables coinciden, el dato se fortalece.")],
  ("Mira estas cuatro fuentes de ejemplo sobre el derecho a la salud: (1) página de una institución de salud con fecha, (2) mensaje de chat sin autor, (3) libro con autor y año, (4) captura sin origen. Escribe cuáles usarías para un afiche y por qué, y cómo escribirías la fuente en letra pequeña.",
   "Usaría (1) y (3) porque tienen autor y fecha. Fuente: Institución de salud (ejemplo), 2023.",
   ["elige las fuentes con autor y fecha", "da una razón", "escribe la fuente en el formato nombre y año"],
   ["frase con las fuentes elegidas y la línea de fuente"],
   ["elegir una fuente por popularidad", "olvidar la fecha"],
   "Pregunta: «¿Esta información dice quién la dio y cuándo?»."),
  "Revisa un dato que viste esta semana y di si podrías anotar su fuente.",
  "Escribe dos preguntas que harías para saber si un mensaje reenviado es confiable.")

# ====================================================== clase 5
F = ("Ficha 5 (tres borradores de afiche de ejemplo para una campaña de un centro comunitario). "
     "Afiche A: lema «Trato digno en la fila» (5 palabras); imagen de personas esperando su turno; dato: «Todas las personas tienen derecho a recibir un trato respetuoso» y fuente: «Declaración Universal de Derechos Humanos, 1948»; letras negras sobre fondo amarillo claro. "
     "Afiche B: título largo de 21 palabras, sin imagen, sin fuente; letras grises sobre fondo gris. "
     "Afiche C: lema «Todos y todas importamos», imagen de una mano abierta, sin fuente; letras negras sobre fondo blanco; incluye la cifra «el 80 % de las personas sufre discriminación» sin decir de dónde sale.")
K(5, F,
  "Hoy aplico lo aprendido a una situación de comunidad: comparo borradores de afiche y decido cuál comunica mejor un derecho y una responsabilidad.",
  ["Un centro comunitario quiere un afiche que invite a tratar con respeto a todas las personas en las filas y trámites. Para saber cuál borrador funciona, usamos una pauta: mensaje claro, lema breve, imagen que apoya, dato con fuente y buen contraste.",
   "Un buen afiche de derechos humanos tiene dos partes que conversan: el derecho (todas las personas merecen trato digno) y la responsabilidad (yo trato con respeto a las demás). Esa mirada evita que el mensaje suene solo a reclamo o solo a norma.",
   "También cuida el cuidado con las cifras: un dato fuerte sin fuente es un punto débil. Si no puedes mostrar de dónde sale, mejor usa una frase cualitativa. Hoy comparamos tres borradores de ejemplo y decidimos cuál se acerca más a la pauta."],
  [("campaña", "conjunto de acciones para comunicar una idea a una comunidad"), ("pauta", "lista de criterios para revisar un trabajo"), ("cualitativo", "que describe algo con palabras y no con cifras"), ("trato digno", "trato que respeta el valor de cada persona")],
  [("Usar la pauta", "Un borrador tiene lema breve, imagen, dato con fuente y buen contraste. ¿Cumple la pauta?", ["Reviso los cinco criterios uno por uno.", "Cumple los cinco."], "Sí, cumple los cinco criterios"),
   ("Corregir un dato sin fuente", "Un borrador dice «el 70 % de las personas no sabe sus derechos» sin fuente. ¿Qué haces?", ["No puedo comprobar la cifra.", "La cambio por una frase cualitativa o agrego una fuente."], "Cambio la cifra por una frase sin cifra o agrego la fuente")],
  [("Elegir el afiche más llamativo y no el más claro.", "Se mira el color y no el mensaje.", "Usa la pauta: mensaje, lema, imagen, fuente y contraste."),
   ("Hablar solo de derechos y olvidar las responsabilidades.", "El mensaje queda incompleto.", "Agrega qué podemos hacer las personas para respetar los derechos de otras.")],
  [("abc", "{F} ¿Cuántas palabras tiene el lema del afiche A, «Trato digno en la fila»?", "5", "4", "6", "Se cuentan Trato, digno, en, la, fila: son cinco palabras."),
   ("ab", "{F} ¿Qué afiche usa letras de poco contraste?", "Afiche B", "Afiche A", "Las letras grises sobre fondo gris casi no se distinguen."),
   ("abc", "{F} ¿Cuál afiche cita una fuente para su dato?", "Afiche A", "Afiche B", "Afiche C", "Solo el afiche A nombra la Declaración Universal de Derechos Humanos como fuente."),
   ("abc", "{F} ¿Qué debilidad tiene el afiche C?", "Una cifra sin fuente", "Letras sin contraste", "Un título de 21 palabras", "Dice «el 80 %» sin decir de dónde sale, así que no se puede comprobar."),
   ("abc", "{F} ¿Qué debilidad tiene el afiche B?", "Título muy largo, sin imagen ni fuente y sin contraste", "Lema corto", "Letras negras sobre fondo blanco", "Reúne varios fallos: demasiado texto, sin apoyo visual, sin fuente y sin contraste."),
   ("abc", "{F} Según la pauta, ¿qué afiche es el más completo?", "Afiche A", "Afiche B", "Afiche C", "Cumple lema breve, imagen, dato con fuente y buen contraste."),
   ("ab", "{F} En el afiche A, ¿la frase «Todas las personas tienen derecho a recibir un trato respetuoso» expresa un derecho?", "Sí, el derecho a un trato digno", "No, es solo una opinión", "La frase afirma algo que corresponde a toda persona: es un derecho."),
   ("abc", "Para completar el afiche A con una responsabilidad, ¿qué frase agregarías?", "«Yo respeto el turno de las demás personas»", "«El Estado debe construir más calles»", "«Los reclamos son inútiles»", "Habla de lo que hace cada persona para respetar el derecho de otras."),
   ("abc", "El afiche C quiere mantener la cifra. ¿Qué cambio lo mejora más?", "Agregar de dónde sale: institución, año y cantidad de personas consultadas", "Poner la cifra en letras más grandes", "Cambiar el color de la mano", "Citar el origen del dato permite que otras personas lo comprueben."),
   ("ab", "¿Es correcto reemplazar una cifra sin fuente por «muchas personas sufren discriminación»?", "Solo si es una afirmación que puedes respaldar con una fuente confiable", "Sí, porque así no hay que comprobar nada", "Aun sin cifra, una afirmación necesita respaldo en una fuente."),
   ("abc", "Una persona dice: «el afiche más bonito es el mejor». ¿Qué responde la pauta?", "Importa más que el mensaje sea claro, con fuente y legible", "Importa solo el color", "Importa solo el tamaño", "Un afiche eficaz se mide por claridad, respaldo y legibilidad."),
   ("abc", "En una campaña de respeto en las filas, ¿cuál es la mejor imagen?", "Personas esperando su turno con calma", "Una calle vacía", "Un animal dibujado", "Muestra la conducta que el afiche quiere promover."),
   ("abc", "Al decidir con la pauta entre los afiches A, B y C, ¿cuál es el orden de menor a mayor cumplimiento de la pauta?", "B, C, A", "A, B, C", "C, A, B", "B falla en casi todo, C falla en la fuente y A cumple todos los criterios.")],
  ("abc", "Una persona de la comunidad pide agregar al afiche A la frase «Todos podemos reclamar con respeto». ¿Qué aporta?", "Une un derecho y una forma respetuosa de ejercerlo", "Quita importancia al derecho", "Cambia el tema a deportes", "Reclamar es ejercer un derecho, y hacerlo con respeto es una responsabilidad."),
  [("En Historia: ¿qué es un trato digno?", "Trato que respeta el valor de cada persona", "Implica escuchar, esperar el turno y no humillar."),
   ("¿Qué debe hacerse con una cifra sin fuente en un afiche?", "Agregar su fuente o reemplazarla por una frase respaldada", "Sin fuente no se puede comprobar."),
   ("¿Por qué un afiche debe incluir una responsabilidad?", "Porque los derechos se ejercen respetando a las demás personas", "Así el mensaje invita a actuar y no solo a exigir.")],
  ("Diseña un afiche corto para una campaña de «trato digno en los trámites». Escribe: lema (hasta seis palabras), una frase de derecho, una frase de responsabilidad, la fuente (puedes usar «Declaración Universal de Derechos Humanos, 1948») y colores de letras y fondo.",
   "Lema: «Trato digno en cada trámite». Derecho: toda persona merece respeto. Responsabilidad: yo trato con respeto. Fuente: Declaración Universal de Derechos Humanos, 1948. Letras negras sobre fondo amarillo claro.",
   ["lema de seis palabras o menos", "incluye un derecho y una responsabilidad", "cita la fuente y usa buen contraste"],
   ["borrador del afiche en una hoja"],
   ["olvidar la responsabilidad", "usar una cifra sin fuente"],
   "Pregunta: «¿Qué derecho y qué responsabilidad aparecen en tu afiche?»."),
  "Cambia el lema de tu afiche por otro de menos palabras.",
  "Haz un segundo borrador para otro derecho, como la educación, y compáralo con el primero.")

# ====================================================== clase 6
F = ("Ficha 6 (pauta de revisión de ejemplo, un punto por criterio cumplido). 1) Mensaje central en una frase. 2) Lema de seis palabras o menos. 3) Imagen que apoya el mensaje. "
     "4) Dato con fuente nombrada. 5) Buen contraste de colores. 6) Incluye una responsabilidad de las personas. "
     "Afiche revisado: lema «Escuchar también es participar» (4 palabras); imagen de dos personas conversando; dato sin fuente; letras negras sobre fondo blanco; no menciona responsabilidades.")
K(6, F,
  "Hoy reviso mi afiche con una pauta, corrijo lo que falta y decido los próximos pasos.",
  ["Revisar es mirar lo hecho con una pauta clara y decidir qué mejorar. Una pauta de seis criterios, un punto por cada uno cumplido, permite ver qué falta y no quedarse con la impresión de «me gusta» o «no me gusta».",
   "Revisa en este orden: mensaje central, lema, imagen, dato con fuente, contraste y responsabilidad. Si falta un criterio, escribe la mejora concreta, por ejemplo «agregar la fuente al dato» o «cambiar el color de las letras».",
   "Al terminar, resume lo aprendido sobre derechos humanos, deberes del Estado y responsabilidades de las personas, y decide qué práctica seguirás: leer fuentes con atención, escribir lemas breves o conversar con otras personas sobre tu afiche."],
  [("pauta", "lista de criterios para revisar un trabajo"), ("criterio", "regla para decidir si algo está bien hecho"), ("mejora", "cambio concreto que hace mejor un trabajo"), ("autoevaluación", "revisar el propio trabajo con una pauta")],
  [("Poner puntaje", "Un afiche cumple el mensaje, el lema, la imagen y el contraste, pero no tiene fuente ni responsabilidad. ¿Cuántos puntos tiene de seis?", ["Cuento los criterios cumplidos: 4.", "Los dos que faltan son la fuente y la responsabilidad."], "4 de 6 puntos"),
   ("Escribir una mejora", "El dato del afiche no tiene fuente. ¿Qué mejora escribes?", ["Digo qué falta y cómo corregirlo.", "Debo nombrar la institución y el año."], "Agregar al dato la fuente con su nombre y año")],
  [("Decir «está bien» sin revisar uno por uno los criterios.", "No se compara con la pauta.", "Marca cada criterio con un sí o un no."),
   ("Anotar una mejora vaga como «mejorar todo».", "No dice qué cambiar.", "Escribe una acción concreta por cada criterio no cumplido.")],
  [("abc", "{F} ¿Cuántas palabras tiene el lema «Escuchar también es participar»?", "4", "5", "6", "Cuenta: Escuchar, también, es, participar: son cuatro palabras."),
   ("ab", "{F} ¿El afiche revisado cumple el criterio 3, imagen que apoya el mensaje?", "Sí, dos personas conversando apoyan la idea de escuchar", "No, la imagen no tiene relación", "Conversar apoya el lema de escuchar y participar."),
   ("ab", "{F} ¿El afiche revisado cumple el criterio 4, dato con fuente?", "No: el dato no tiene fuente", "Sí: tiene dato y fuente", "La ficha dice que el dato carece de fuente."),
   ("abc", "{F} ¿Qué criterios no cumple el afiche revisado?", "El 4 y el 6", "El 1 y el 2", "El 3 y el 5", "Le falta la fuente del dato y mencionar una responsabilidad."),
   ("{F} ¿Cuántos puntos, de seis, obtiene el afiche revisado?", "4", "Cumple 1, 2, 3 y 5; no cumple 4 ni 6, así que suma cuatro puntos."),
   ("abc", "{F} ¿Qué mejora concreta resuelve el criterio 6?", "Agregar una frase como «yo trato con respeto a las demás personas»", "Cambiar el color de fondo", "Quitar la imagen", "Una frase de responsabilidad cumple lo que pide el criterio."),
   ("abc", "Un afiche sale con 2 puntos de 6. ¿Qué haces primero?", "Escribir una mejora para cada criterio no cumplido", "Botarlo sin revisar", "Dejarlo igual porque está terminado", "La revisión sirve para corregir lo que falta."),
   ("ab", "¿Qué es mejor para guiar una revisión?", "Una pauta con criterios claros", "Una opinión sin criterios", "Con una pauta se revisa lo mismo en cada afiche y se justifica lo que se concluye."),
   ("abc", "Tras revisar tu afiche, ¿cuál es un próximo paso razonable?", "Mostrarlo a otra persona y escuchar sus comentarios", "Esconderlo", "Cambiar el tema sin revisar", "Recibir comentarios ayuda a mejorar el mensaje."),
   ("abc", "Dos personas revisan el mismo afiche con la pauta de seis puntos. ¿Qué esperas?", "Resultados parecidos, porque usan los mismos criterios", "Resultados siempre distintos", "Que no se pueda revisar", "Los criterios compartidos reducen las diferencias."),
   ("abc", "{F} Si agregas al afiche revisado una fuente y una frase de responsabilidad, ¿cuántos puntos obtiene?", "6", "5", "4", "Los criterios 4 y 6 se suman a los cuatro ya cumplidos."),
   ("abc", "¿Cuál afirmación resume bien lo aprendido en este módulo sobre afiches de derechos humanos?", "Un afiche eficaz tiene mensaje claro, lema breve, dato con fuente y buen contraste", "Un afiche eficaz tiene mucho texto y colores claros", "Un afiche eficaz no necesita fuentes", "Resume los criterios trabajados en las clases anteriores."),
   ("ab", "Una persona dice: «Si mi afiche tiene 6 puntos, ya no puedo mejorarlo». ¿Qué respuesta es correcta?", "Siempre se puede revisar con nuevas personas o fuentes", "Tiene razón, es perfecto", "La pauta mide mínimos; el afiche puede seguir mejorando con más fuentes o comentarios.")],
  ("abc", "Una organización vecinal revisa su afiche sobre educación: cumple 5 de 6 criterios y le falta la fuente. ¿Qué decide?", "Agregar la fuente antes de imprimirlo", "Imprimirlo igual sin cambios", "Quitar el lema", "Con una mejora concreta llega al puntaje completo."),
  [("En Historia: ¿qué es una pauta de revisión?", "Una lista de criterios para revisar un trabajo", "Permite saber qué falta de manera ordenada."),
   ("¿Qué es una mejora concreta?", "Un cambio específico, como agregar la fuente", "Una mejora concreta dice qué cambiar y dónde hacerlo."),
   ("¿Qué hace una autoevaluación?", "Revisar el propio trabajo con una pauta", "Compara lo hecho con criterios claros.")],
  ("Con la pauta de seis puntos, revisa tu afiche de la clase 5 (o este de ejemplo: lema «Respeto para todas las personas», imagen de una fila ordenada, dato «Declaración Universal de Derechos Humanos, 1948», letras negras sobre fondo amarillo claro, sin responsabilidad). Marca sí o no en cada criterio, suma los puntos y escribe una mejora para cada «no».",
   "Criterios 1 a 5: sí; criterio 6: no. Puntaje: 5 de 6. Mejora: agregar «yo respeto el turno de las demás personas».",
   ["marca los seis criterios", "suma bien los puntos", "escribe una mejora concreta por cada criterio no cumplido"],
   ["pauta marcada y lista de mejoras"],
   ["marcar sí sin comprobar", "escribir mejoras vagas"],
   "Pregunta: «¿Qué cambio haría que el criterio pase de no a sí?»."),
  "Muestra tu afiche a una persona y anota un comentario que te sirva.",
  "Prepara una versión final de tu afiche, con letra clara, para colgar en un lugar de la comunidad.")

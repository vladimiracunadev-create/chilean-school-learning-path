"""Lengua y Literatura EPJA Media N1, módulo 1, OAD-01: usar el contexto de producción y de recepción para comprender un texto literario. Todos los textos y datos son inventados y se resuelven en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los textos, fichas, autores y datos de este cuaderno son inventados («de ejemplo») y están escritos en cada ejercicio: "
    "no necesitas libros, audio, video ni internet. Si algo te cuesta leer, pide que te lo lean en voz alta; pedir apoyo es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)
build = make_build(MATERIALS)

O = "EPJA-LELI-NM1-OAD-01"
PRIOR = ["He leído o escuchado cuentos, canciones o relatos de otras personas.", "Sé contar con mis palabras de qué trató un texto.", "He comentado con alguien una historia y hemos entendido cosas distintas."]

CUENTO = ("Cuento (inventado), «El farolero», de Anselmo Rivas (autor ficticio): Cada tarde, don Telmo subía por el cerro con una escalera al hombro y encendía los faroles de la caleta, uno por uno. "
          "Los pescadores, al volver del mar, buscaban esas luces para ubicar el muelle. Un día llegó la luz eléctrica y don Telmo quedó sin oficio. "
          "Esa noche subió igual, se sentó en el último escalón y miró cómo el pueblo se encendía solo.")
BIO = ("Ficha informativa (inventada): Anselmo Rivas, autor ficticio, nació en 1902 en Punta Alerce, una caleta ficticia. Fue pescador de joven y después escribió cuentos. "
       "Publicó el libro «Luces de la caleta» en 1938. En esos años llegaban las primeras luces eléctricas a los pueblos de la costa y muchas familias dejaban los oficios antiguos para trabajar en la ciudad. "
       "Hoy el libro se lee en talleres de lectura de barrio.")
CUENTO2 = ("Cuento (inventado), «La red de doña Inés», de Anselmo Rivas (autor ficticio): Doña Inés remendaba redes en el patio mientras sus hijos aprendían a leer con un libro prestado. "
           "Cuando el hijo menor dijo que quería estudiar en la ciudad, ella siguió tejiendo y no contestó. Esa noche dejó junto a su cama un atado de monedas envuelto en un trapo.")
BIO2 = ("Dato de contexto (inventado): en la época y la región de este cuento ficticio, muchas familias de caleta mandaban a un hijo a estudiar a la ciudad con gran esfuerzo, porque en el pueblo había pocas escuelas. "
        "El autor ficticio fue el primero de su familia en terminar los estudios.")


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(O, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ============================================================ clase 1
K(1, CUENTO + " Comentario de Paula, lectora que vive en un puerto de pescadores: «Para mí es la historia de un trabajo que une a todo el pueblo». "
      "Comentario de Raúl, lector que vive en una ciudad sin mar: «Para mí es la historia de un hombre que se queda sin trabajo por la tecnología».",
  "Hoy parto de lo que ya sé: veo que dos personas pueden entender de modo distinto un mismo cuento y que ese cambio tiene explicación.",
  ["Tú ya sabes que dos personas pueden escuchar el mismo relato y entenderlo distinto. Un chiste que a una persona le da risa, a otra no le dice nada, porque no vivió lo mismo. Con la literatura pasa igual: lo que entendemos depende también de lo que sabemos y hemos vivido.",
   "Una obra literaria nace en un momento y un lugar: alguien la escribe, en una época, con ciertas ideas y experiencias. A eso se le llama contexto de producción. Después la obra llega a lectores que viven en otro momento y lugar: eso es el contexto de recepción.",
   "Interpretar no es repetir la historia con otras palabras. Resumir es contar qué pasó; interpretar es proponer qué significa lo que pasó y apoyarse en datos del texto. Hoy usaremos un cuento corto para notar cómo la experiencia de cada persona cambia lo que ve."],
  [("obra literaria", "texto escrito con intención artística, como un cuento o un poema"), ("lector", "persona que lee y construye un sentido del texto"), ("interpretar", "proponer un sentido para un texto y apoyarlo con datos"), ("resumir", "contar brevemente qué ocurre, sin explicar qué significa")],
  [("Resumir y interpretar", "Frases sobre «El farolero»: A) «Don Telmo enciende faroles y luego llega la luz eléctrica». B) «El cuento muestra cómo un cambio puede dejar sin lugar a un oficio».",
    ["A dice qué ocurre: es un resumen.", "B propone un significado sobre lo que ocurre: es una interpretación.", "Para sostener B habría que citar que don Telmo «quedó sin oficio»."], "A resume; B interpreta"),
   ("Dos lecturas, un texto", "Paula ve un trabajo que une al pueblo; Raúl ve un hombre sin trabajo. ¿Qué dato apoya a cada una?",
    ["Paula: los pescadores buscaban esas luces para ubicar el muelle.", "Raúl: don Telmo quedó sin oficio cuando llegó la luz eléctrica.", "Cada lectura usa un dato real del cuento."], "Ambas se apoyan en datos distintos del texto")],
  [("Contar otra vez el cuento y creer que eso es interpretar.", "Se resume lo que pasa, pero no se dice qué significa.", "Agrega una oración que explique qué podría significar lo que ocurre."),
   ("Pensar que una lectura distinta de la mía es un error.", "Cada persona lee desde su experiencia y puede ver algo real.", "Pregunta en qué dato del texto se apoya la otra lectura.")],
  [("abc", "{F} ¿Quién es el personaje central del cuento?", "Don Telmo, el farolero de la caleta", "Paula, la lectora del puerto", "Raúl, el lector de la ciudad", "El cuento cuenta lo que hace don Telmo; Paula y Raúl solo lo comentan."),
   ("ab", "{F} ¿Qué cambió en la caleta cuando llegó la luz eléctrica?", "Los faroles ya no se encendían a mano", "Los pescadores dejaron de salir al mar", "El texto dice que el pueblo se encendía solo; no menciona que dejaran de pescar."),
   ("{F} ¿Cuántos comentarios de lectores aparecen en la ficha? Escribe el número.", "2", "Se leen el comentario de Paula y el de Raúl."),
   ("abc", "En Lengua y Literatura: dos personas leen el mismo cuento y entienden cosas distintas. ¿Qué lo explica mejor?", "Cada una lee desde su propia experiencia y su contexto", "Una de las dos leyó mal las palabras del texto", "El cuento cambia de palabras cada vez que se lee", "La experiencia de cada lector influye en lo que destaca del texto."),
   ("abc", "{F} ¿Qué experiencia de Paula influye en su lectura?", "Vive en un puerto de pescadores y conoce el trabajo de la caleta", "Escribe cuentos desde hace muchos años", "Trabajó como farolera en una ciudad", "La ficha dice que Paula vive en un puerto de pescadores."),
   ("ab", "{F} Raúl lee el cuento como un problema de la tecnología. ¿Qué dato lo apoya?", "Don Telmo queda sin oficio cuando llega la luz eléctrica", "Don Telmo sube por el cerro con una escalera", "El dato que respalda a Raúl es la pérdida del oficio al llegar la luz eléctrica."),
   ("abc", "Una mujer que trabajó de guardia nocturna lee un cuento sobre un guardia que cuida un edificio de noche y dice: «Entiendo su cansancio». ¿Qué influyó en su lectura?", "Su experiencia de trabajo", "El número de páginas del libro", "El nombre de la editorial", "Su vivencia laboral le permite entender el cansancio del personaje."),
   ("abc", "Un cuento comienza: «Esa noche cortaron el agua y todo el pasaje salió con baldes a la llave de la esquina». ¿Qué conocimiento previo ayuda más a entender la escena?", "Haber vivido o conocido un corte de agua en el barrio", "Saber cuántos versos tiene un soneto", "Conocer el año de fundación de la editorial", "Haber vivido algo parecido ayuda a entender la escena."),
   ("abc", "Un lector dice: «El texto es sobre un farolero». Otra lectora dice: «Muestra cómo un cambio puede quitarle su lugar a un oficio». ¿Quién interpreta?", "La lectora, porque propone un sentido", "El lector, porque nombra al personaje", "Ninguno de los dos, porque ambos hablan del cuento", "Interpretar es proponer qué significa lo ocurrido, no solo nombrarlo."),
   ("ab", "{F} Paula ve un trabajo que une al pueblo; Raúl, un hombre sin trabajo. ¿Ambas lecturas pueden apoyarse en el texto?", "Sí, cada una usa datos distintos del cuento", "No, solo una puede apoyarse en el cuento", "Los faroles guían a los pescadores y don Telmo queda sin oficio: hay datos para ambas."),
   ("abc", "{F} Un tercer lector dice: «El cuento trata de astronautas». ¿Qué problema tiene esa lectura?", "No hay ningún dato del texto que la apoye", "Es distinta de la lectura de Paula", "Es una frase demasiado corta", "Una interpretación válida necesita datos del texto; esta no los tiene."),
   ("abc", "{F} ¿Qué pregunta ayuda a pasar de resumir a interpretar?", "¿Qué podría significar que don Telmo suba igual esa noche?", "¿Cuántas líneas tiene el cuento?", "¿Cómo se llama el cerro?", "Pregunta por el sentido de un hecho, no por un dato suelto."),
   ("ab", "{F} Si el cuento terminara con don Telmo contratado para cuidar la luz nueva, ¿la lectura de Raúl cambiaría?", "Sí, ya no estaría tan claro que queda sin oficio", "No, la lectura nunca depende de lo que pasa al final", "Cambiaría el dato en que Raúl se apoya, por eso su conclusión se debilita.")],
  ("abc", "En un taller de lectura de tu centro, dos compañeros discuten qué quiso decir un cuento. Antes de decidir quién tiene razón, ¿qué conviene hacer?", "Pedirle a cada uno el dato del texto en que apoya su lectura", "Votar levantando la mano", "Quedarse con la opinión de quien habla más fuerte", "Una interpretación se evalúa por el apoyo que tiene en el texto."),
  [("En Lengua y Literatura: ¿qué es interpretar un texto?", "Proponer un sentido y apoyarlo con datos del texto", "Interpretar es más que contar lo que pasa: es explicar qué significa."),
   ("¿Qué diferencia hay entre resumir e interpretar?", "Resumir cuenta qué pasó; interpretar propone qué significa", "El resumen repite hechos y la interpretación les busca sentido."),
   ("¿Por qué dos personas pueden leer distinto el mismo cuento?", "Porque cada una lee desde su experiencia y su contexto", "Lo que vivimos nos hace notar unos datos y otros no.")],
  ("Lee el cuento «El farolero»: {F} Escribe en tu cuaderno (1) un resumen de dos líneas y (2) una interpretación de dos líneas que diga qué podría significar la última escena y en qué dato del cuento te apoyas. No incluyas datos personales.",
   "Resumen: don Telmo enciende faroles hasta que llega la luz eléctrica y se queda sin oficio; esa noche sube igual. Interpretación: el cuento muestra la pena de perder un oficio que servía a todos; me apoyo en que «quedó sin oficio» y en que sube «igual».",
   ["el resumen cuenta hechos sin opinar", "la interpretación propone un sentido", "cita un dato del cuento"],
   ["dos textos de dos líneas cada uno"],
   ["copiar el resumen como interpretación", "interpretar sin citar ningún dato"],
   "Pregunta: «¿Qué dato del cuento prueba lo que dices?»."),
  "Cuenta a otra persona una historia que conozcas y dile qué crees que significa.",
  "Pregúntale a alguien cercano qué entendió de «El farolero» y anota en qué dato se apoya.")

# ============================================================ clase 2
K(2, BIO + " " + CUENTO,
  "Hoy reconozco las palabras «contexto de producción» y «contexto de recepción» y las distingo con ejemplos.",
  ["El contexto de producción es todo lo que rodea el momento en que se escribió una obra: quién la escribió, en qué época y lugar, qué ideas y costumbres había y qué vivió esa persona. No es solo la fecha: incluye las creencias, los trabajos y las formas de vida de entonces.",
   "El contexto de recepción es el momento y el lugar desde donde se lee la obra: quién lee, en qué época, con qué experiencias. Una misma obra puede leerse de una manera cuando se publica y de otra cien años después, porque los lectores cambian.",
   "Para usar esta información, pregúntate dos cosas. Primero: ¿qué sé de quien escribió y de su tiempo, y qué detalle del texto lo muestra? Segundo: ¿desde qué lugar y época lo leo yo, y cómo eso cambia lo que veo? Con ambas respuestas la lectura se hace más profunda."],
  [("contexto de producción", "situación, época, ideas y vida del autor cuando se escribió la obra"), ("contexto de recepción", "momento y lugar desde donde las personas leen la obra"), ("autor", "persona que escribe la obra"), ("época", "período histórico con sus ideas y costumbres")],
  [("Clasificar un dato", "Dato de la ficha: «Rivas fue pescador de joven». ¿Es contexto de producción o de recepción?", ["Habla de la vida de quien escribió.", "Eso rodea el momento de escritura.", "No habla de quien lee hoy."], "Es contexto de producción"),
   ("Clasificar otro dato", "Dato de la ficha: «Hoy el libro se lee en talleres de lectura de barrio». ¿De cuál es?", ["Habla de quienes leen la obra ahora.", "Describe el lugar desde donde se lee."], "Es contexto de recepción")],
  [("Creer que el contexto de producción es solo la fecha de publicación.", "El año es un dato, pero faltan las ideas, el lugar y la vida del autor.", "Agrega quién escribió, dónde, y qué se pensaba y vivía entonces."),
   ("Pensar que el contexto de recepción es el mismo de la época del autor.", "Los lectores de hoy no leen desde el año en que se escribió.", "Pregunta quién lee, cuándo y desde dónde.")],
  [("abc", "{F} ¿En qué año se publicó «Luces de la caleta»?", "En 1938", "En 1902", "En el presente", "La ficha dice que se publicó en 1938; 1902 es el año de nacimiento."),
   ("ab", "{F} ¿Qué oficio tuvo el autor de joven?", "Fue pescador", "Fue farolero", "La ficha informativa dice que Anselmo Rivas fue pescador de joven."),
   ("{F} ¿Cómo se llama la caleta ficticia donde nació el autor? Escribe solo el nombre.", "Punta Alerce", "La ficha nombra Punta Alerce como el lugar donde nació."),
   ("abc", "En Lengua y Literatura: ¿qué es el contexto de producción de una obra?", "La época, el lugar y las ideas en que se escribió, y la vida del autor", "El número de personas que la compraron", "La opinión de quien la lee hoy", "Es lo que rodea el momento y las condiciones en que se escribió."),
   ("abc", "{F} El dato «Hoy el libro se lee en talleres de lectura de barrio» pertenece al contexto de", "recepción, porque habla de quienes leen hoy", "producción, porque habla del autor", "producción, porque dice cuándo nació", "Informa dónde y quiénes leen la obra ahora."),
   ("ab", "{F} El dato «llegaban las primeras luces eléctricas a los pueblos de la costa» pertenece al contexto de", "producción, porque describe la época en que se escribió", "recepción, porque habla de lectores de hoy", "Muestra qué ocurría cuando se escribió el libro, en 1938."),
   ("abc", "{F} ¿Qué detalle del cuento se conecta con el dato de la ficha sobre la luz eléctrica?", "Que la luz eléctrica deja a don Telmo sin oficio", "Que don Telmo se sienta en un escalón", "Que los pescadores vuelven del mar", "El cuento muestra lo mismo que la época: la luz eléctrica cambiaba oficios."),
   ("abc", "{F} ¿Qué dato de la vida del autor puede explicar que escriba sobre pescadores?", "Fue pescador de joven", "Publicó su libro en 1938", "Su libro se lee en talleres", "Conoce el mar y su trabajo por experiencia propia."),
   ("abc", "Una lectora hoy dice: «No sabía que antes alguien encendía los faroles a mano». ¿Qué contexto explica que ella se sorprenda?", "El de recepción, porque lee desde un tiempo con otra tecnología", "El de producción, porque nació en otra época", "Ninguno, porque su sorpresa no tiene relación con la época", "Su sorpresa viene de leer hoy, desde otra época y forma de vida."),
   ("ab", "{F} Un estudiante afirma: «El contexto de producción es solo la fecha: 1938». ¿Tiene razón?", "No, también incluye el lugar, las ideas y la vida del autor", "Sí, el contexto es solamente el año", "La ficha agrega que había cambios en los oficios y que el autor fue pescador."),
   ("abc", "{F} ¿Qué diferencia hay entre el contexto de producción y el de recepción?", "El primero rodea la escritura; el segundo rodea la lectura", "El primero se refiere a hoy y el segundo a 1938", "No hay ninguna diferencia entre los dos", "Uno mira el momento de escribir; el otro, el momento de leer."),
   ("abc", "{F} Un lector dice que el cuento «solo habla de un señor con una escalera». ¿Qué le falta para profundizar?", "Relacionar el cuento con los cambios de oficios que muestra la ficha", "Contar cuántos faroles hay", "Copiar la ficha completa sin leer el cuento", "Conectar el cuento con su contexto muestra qué significa el hecho."),
   ("ab", "{F} Si la ficha dijera que el autor nunca vivió cerca del mar, ¿qué dato dejaría de explicar el cuento?", "Que conoce el trabajo de la caleta por haber sido pescador", "Que don Telmo enciende faroles cada tarde", "La explicación por la vida del autor se pierde; lo que cuenta el texto sigue igual.")],
  ("abc", "Vas a presentar una obra en la junta de vecinos. ¿Cuál dato sirve para el contexto de producción?", "Dónde y cuándo vivió quien la escribió", "Cuánto tiempo tardaste en leerla", "Cuántas personas hay hoy en la sala", "Lo que rodea al autor al escribir es contexto de producción."),
  [("En Lengua y Literatura: ¿qué es el contexto de recepción?", "El momento y lugar desde donde se lee la obra", "Habla de quienes leen, no de quien escribe."),
   ("¿Qué incluye el contexto de producción además de la fecha?", "El lugar, las ideas de la época y la vida del autor", "Todo eso rodea la escritura de la obra."),
   ("Escribe un ejemplo de dato de recepción.", "Hoy el libro se lee en talleres de barrio", "Es un dato sobre quienes leen la obra ahora.")],
  ("Lee la ficha y el cuento: {F} Haz una tabla con dos columnas, «producción» y «recepción»: escribe dos datos de producción de la ficha y el dato de recepción que ella trae. Después escribe una oración que relacione un dato de producción con un detalle del cuento.",
   "Producción: nació en 1902 en Punta Alerce; fue pescador. Recepción: hoy se lee en talleres de lectura de barrio. Relación: como Rivas fue pescador, el cuento muestra el valor de las luces para los pescadores.",
   ["dos datos de producción y uno de recepción", "datos tomados de la ficha", "una oración que une un dato con un detalle del cuento"],
   ["una tabla de dos columnas y una oración"],
   ["mezclar datos de producción con los de recepción", "relacionar sin citar un detalle del cuento"],
   "Pregunta: «¿Este dato habla de quien escribe o de quien lee?»."),
  "Escribe con tus palabras qué es el contexto de producción y qué es el de recepción.",
  "Piensa en una canción o relato que te marcó y anota en qué época lo conociste y cómo lo entendías entonces.")

# ============================================================ clase 3
K(3, BIO + " " + CUENTO,
  "Hoy aprendo, paso a paso, a usar un organizador que une lo que dice el texto informativo con citas del cuento.",
  ["Para usar el contexto sin perderse, conviene un organizador de dos columnas. A la izquierda anotas una característica del contexto, tomada de un texto informativo, como una ficha sobre el autor. A la derecha anotas una cita del cuento que se relaciona con esa característica.",
   "Los pasos son cuatro. Uno: lee la ficha informativa y subraya tres datos importantes. Dos: lee el cuento y busca frases que se conecten con cada dato. Tres: copia la frase entre comillas, tal como aparece. Cuatro: escribe una oración que explique la relación.",
   "Una cita textual es una frase copiada exactamente del texto y puesta entre comillas. Sirve de prueba: muestra que tu idea sale del texto y no de una suposición. Si no puedes encontrar una cita para un dato, quizás ese dato no ayuda a leer este cuento."],
  [("organizador gráfico", "cuadro que ordena ideas en filas y columnas"), ("cita textual", "frase copiada exactamente del texto, entre comillas"), ("característica", "rasgo que describe algo"), ("relación", "vínculo entre dos cosas")],
  [("Armar una fila del organizador", "Dato de la ficha: «llegaban las primeras luces eléctricas a los pueblos de la costa». Busca una cita del cuento.",
    ["Subrayo el dato: llegada de la luz eléctrica.", "Busco en el cuento: «Un día llegó la luz eléctrica y don Telmo quedó sin oficio».", "Escribo la relación: el cuento muestra qué provoca ese cambio en un oficio."], "Fila: luces eléctricas / «Un día llegó la luz eléctrica…»"),
   ("Citar bien", "Se quiere citar lo que hacía don Telmo cada tarde.", ["Busco la frase: «Cada tarde, don Telmo subía por el cerro con una escalera al hombro».", "La copio entre comillas, sin cambiar palabras.", "Explico: era su oficio de farolero."], "Cita textual con comillas y explicación")],
  [("Parafrasear y poner comillas como si fuera una cita.", "Si cambias palabras, ya no es una cita exacta.", "Copia la frase tal cual o no uses comillas."),
   ("Escribir una cita que no tiene relación con el dato.", "La cita debe probar o ilustrar la característica anotada.", "Comprueba que la frase hable de lo mismo que el dato.")],
  [("abc", "{F} ¿Cuál es la cita exacta que muestra el oficio de don Telmo?", "«Cada tarde, don Telmo subía por el cerro con una escalera al hombro»", "«Don Telmo era un hombre muy trabajador y siempre subía»", "«Cada tarde subía don Telmo, a hombros, por el cerro»", "Solo la primera copia las palabras exactas del cuento."),
   ("ab", "{F} ¿Qué dato de la ficha se relaciona con la frase «quedó sin oficio»?", "Muchas familias dejaban los oficios antiguos", "Rivas nació en 1902", "La ficha dice que dejaban los oficios antiguos, igual que le pasa a don Telmo."),
   ("{F} ¿En qué año se publicó el libro, según la ficha? Escribe el número.", "1938", "Es el año de publicación que indica la ficha informativa."),
   ("abc", "En Lengua y Literatura: ¿qué es una cita textual?", "Una frase copiada exactamente del texto y puesta entre comillas", "Un resumen del texto con mis palabras", "La opinión de otra persona sobre el texto", "La cita conserva las palabras del texto sin cambios."),
   ("abc", "{F} Completa el organizador. Característica: «Rivas fue pescador de joven». ¿Qué cita del cuento se relaciona?", "«Los pescadores, al volver del mar, buscaban esas luces»", "«Esa noche subió igual»", "«Un día llegó la luz eléctrica»", "La vida del autor se conecta con el mundo de los pescadores del cuento."),
   ("ab", "{F} Característica: «el pueblo recibe luces eléctricas». ¿Qué cita corresponde?", "«Un día llegó la luz eléctrica y don Telmo quedó sin oficio»", "«Cada tarde, don Telmo subía por el cerro»", "La cita nombra la llegada de la luz eléctrica, que es la característica anotada."),
   ("abc", "{F} Un estudiante escribe, como cita: «Don Telmo se puso triste cuando llegó la luz». ¿Qué problema tiene?", "Esas palabras no aparecen en el cuento: no es una cita exacta", "Es demasiado corta", "Está escrita en pasado", "El cuento no dice esa frase; es una paráfrasis puesta entre comillas."),
   ("abc", "{F} ¿Qué paso va después de «lee la ficha y subraya tres datos»?", "Leer el cuento y buscar frases conectadas con cada dato", "Escribir la conclusión final", "Copiar la ficha completa", "Primero se leen los datos y luego se buscan las citas."),
   ("abc", "{F} ¿Cuál de estas filas del organizador está bien armada?", "Dato: oficios antiguos que desaparecen / Cita: «quedó sin oficio»", "Dato: la edad del lector / Cita: «subió igual»", "Dato: el color de la tapa / Cita: «los faroles»", "Solo la primera une un dato de la ficha con una cita relacionada."),
   ("ab", "{F} ¿Qué explica mejor la relación entre «luces eléctricas» y «El farolero»?", "El cuento muestra cómo ese cambio afecta a quien encendía los faroles", "El cuento no tiene ninguna relación con las luces eléctricas", "Don Telmo enciende faroles y la luz eléctrica los deja de necesitar."),
   ("abc", "{F} ¿Qué cita apoyaría la idea «el oficio de don Telmo era importante para otros»?", "«Los pescadores, al volver del mar, buscaban esas luces para ubicar el muelle»", "«Se sentó en el último escalón»", "«Uno por uno»", "La cita muestra que los pescadores dependían de su trabajo."),
   ("abc", "{F} Una lectora dice: «Como Rivas fue pescador, el cuento muestra de cerca la vida de la caleta». ¿Qué dos cosas relaciona?", "Un dato de la vida del autor con un rasgo del cuento", "Dos citas del mismo párrafo", "Dos lectores distintos", "Une el contexto de producción con lo que narra el texto."),
   ("ab", "{F} Si no se encuentra ninguna cita del cuento para un dato de la ficha, ¿qué conviene concluir?", "Que ese dato quizá no ayuda a leer este cuento", "Que se debe inventar una cita", "Una cita inventada no prueba nada; el dato puede no servir para este texto.")],
  ("abc", "Debes explicar a tu grupo por qué el taller de lectura eligió «El farolero». Tienes una ficha sobre el autor y el cuento. ¿Qué haces primero?", "Anoto datos de la ficha y busco frases del cuento que se relacionen", "Repito de memoria lo que recuerdo del cuento", "Leo solo el título", "El organizador une datos informativos con citas del texto."),
  [("En Lengua y Literatura: ¿para qué sirve una cita textual?", "Para probar que mi idea sale del texto", "La cita muestra que la lectura se apoya en lo escrito."),
   ("¿Qué se escribe en la columna izquierda del organizador?", "Una característica del contexto sacada del texto informativo", "Es el dato que se va a relacionar con una cita."),
   ("¿Qué se hace si cambio una palabra de la frase?", "Ya no es cita y no debo poner comillas", "La cita exige copiar exactamente las palabras.")],
  ("Usa la ficha y el cuento: {F} Arma en tu cuaderno un organizador con tres filas. En cada una, escribe un dato de la ficha y una cita exacta del cuento. Termina con una oración que diga qué entendiste mejor del cuento gracias a la ficha.",
   "Fila 1: llegada de la luz eléctrica / «Un día llegó la luz eléctrica y don Telmo quedó sin oficio». Fila 2: fue pescador / «Los pescadores, al volver del mar, buscaban esas luces». Fila 3: oficios antiguos / «Cada tarde, don Telmo subía por el cerro con una escalera al hombro». Gracias a la ficha entiendo que el cuento habla de una época de cambios.",
   ["tres filas completas", "citas copiadas exactas con comillas", "una oración que explica lo que se entendió mejor"],
   ["un organizador de tres filas y una oración"],
   ["citas que cambian palabras", "datos de la ficha sin cita que los relacione"],
   "Pregunta: «¿Esa frase está igual en el cuento?»."),
  "Copia tres frases del cuento entre comillas y comprueba que no cambiaste ninguna palabra.",
  "Elige otro cuento corto que conozcas, anota un dato sobre su autor y busca una frase que se relacione.")

# ============================================================ clase 4
K(4, CUENTO2 + " " + BIO2,
  "Hoy practico con apoyo cómo el contexto del autor y de su época ayuda a explicar un detalle de otro cuento.",
  ["Ya sabes armar un organizador con datos del contexto y citas. Hoy vamos un paso más: usar ese dato para explicar un detalle que, sin el contexto, podríamos pasar por alto. Un detalle es un gesto, un objeto o una frase pequeña que tiene un significado.",
   "En el cuento de hoy, doña Inés no contesta y deja un atado de monedas. Sin contexto, podríamos pensar que no le importa lo que dijo su hijo. Con el dato de que las familias hacían grandes sacrificios para que un hijo estudiara, el gesto de las monedas se entiende como apoyo silencioso.",
   "La secuencia es: observar el detalle, preguntar qué podría significar, buscar un dato del contexto que ayude y formular una explicación. Si el dato del contexto no cambia lo que entiendes, quizá no sea el adecuado. Y cuidado: el contexto ayuda a leer, pero no reemplaza al texto; la explicación siempre debe apoyarse en una cita."],
  [("detalle", "gesto, objeto o frase pequeña que aporta significado"), ("explicación", "razón que aclara por qué algo ocurre o qué significa"), ("sacrificio", "esfuerzo grande que alguien hace por otra persona"), ("silencio significativo", "momento en que alguien no habla pero comunica algo con sus actos")],
  [("Del detalle al contexto", "Detalle: doña Inés «siguió tejiendo y no contestó». Dato: las familias hacían grandes esfuerzos para que un hijo estudiara.",
    ["Observo el detalle: ella no dice nada.", "Pregunto qué podría significar: ¿rechazo o preocupación?", "Uso el dato: el estudio de un hijo exigía sacrificios; el silencio puede ser pensar cómo lograrlo."], "El silencio puede mostrar preocupación y decisión"),
   ("Probar la explicación", "Explicación: el atado de monedas es un apoyo silencioso. Cita: «dejó junto a su cama un atado de monedas».",
    ["La cita muestra una acción concreta.", "Esa acción coincide con la idea de apoyo.", "Además el dato de contexto apoya que ahorrar era un sacrificio."], "Explicación apoyada en cita y en contexto")],
  [("Usar el dato de contexto para inventar hechos que el cuento no dice.", "El contexto ayuda a explicar lo que el texto muestra, no a agregar hechos.", "Parte de una cita y usa el dato solo para explicarla."),
   ("Decir que el dato ficticio es una verdad histórica real.", "Los datos de la ficha están rotulados como inventados.", "Mantén claro qué viene del texto y qué es dato de ejemplo.")],
  [("abc", "{F} ¿Qué hacía doña Inés mientras sus hijos aprendían a leer?", "Remendaba redes en el patio", "Vendía pescado en la caleta", "Enseñaba en la escuela del pueblo", "El cuento dice que remendaba redes en el patio."),
   ("ab", "{F} ¿Cuándo deja doña Inés el atado de monedas?", "Esa noche, junto a su cama", "Al amanecer, en la mesa de la cocina", "El texto dice que lo dejó esa noche junto a su cama."),
   ("{F} ¿Qué dejó doña Inés junto a su cama, envuelto en un trapo? Escribe una sola palabra.", "monedas", "El cuento dice que dejó un atado de monedas envuelto en un trapo."),
   ("abc", "{F} ¿Qué dato de contexto ayuda a entender el atado de monedas?", "Las familias hacían grandes esfuerzos para que un hijo estudiara en la ciudad", "El cuento está escrito en tercera persona", "El libro se publicó en un año reciente", "El dato sobre el esfuerzo de las familias explica el ahorro de doña Inés."),
   ("abc", "{F} Sin el dato de contexto, ¿cómo podría malentenderse el silencio de doña Inés?", "Como indiferencia hacia su hijo", "Como alegría por un regalo", "Como una orden para que se quede", "Sin el contexto parece que no le importa, pero sus actos dicen otra cosa."),
   ("ab", "{F} ¿Qué cita apoya la idea de que doña Inés ayuda a su hijo?", "«dejó junto a su cama un atado de monedas»", "«siguió tejiendo»", "La cita muestra un acto concreto de ayuda; seguir tejiendo solo muestra silencio."),
   ("abc", "{F} Una lectora escribe: «Doña Inés odia que su hijo estudie». ¿Qué problema tiene?", "No tiene ninguna cita que la apoye y contradice el acto de las monedas", "Está escrita en tercera persona", "Es demasiado clara", "El texto muestra un gesto de ayuda, no de rechazo."),
   ("abc", "{F} ¿Qué paso va primero al analizar un detalle?", "Observar el detalle en el texto", "Escribir la conclusión final", "Buscar la fecha de nacimiento del autor", "Antes de interpretar hay que fijarse en qué dice el texto."),
   ("abc", "{F} ¿Qué detalle del cuento muestra el valor del estudio para esa familia?", "Los hijos aprenden a leer con un libro prestado", "Doña Inés teje redes de pesca", "El patio donde trabaja ella", "Aprender con un libro prestado muestra el esfuerzo por estudiar."),
   ("ab", "{F} Un lector dice: «El dato del contexto me permite inventar que la familia era muy rica». ¿Es correcto?", "No, el cuento muestra esfuerzo y monedas envueltas en un trapo", "Sí, el contexto sirve para suponer cualquier cosa", "El texto no habla de riqueza; el trapo y el esfuerzo sugieren recursos escasos."),
   ("abc", "{F} ¿Qué relación hay entre el dato «el autor fue el primero de su familia en terminar los estudios» y el cuento?", "Puede explicar que el autor muestre con respeto el esfuerzo por estudiar", "Prueba que doña Inés existió de verdad", "Demuestra que el cuento es un reportaje", "El dato de la vida del autor se conecta con el tema del cuento."),
   ("abc", "{F} ¿Cuál es la explicación mejor apoyada del silencio de doña Inés?", "Piensa cómo hacer posible el estudio y lo expresa con un acto", "Se olvidó de contestar porque estaba distraída", "No entendió lo que dijo su hijo", "El silencio se completa con el acto de dejar las monedas."),
   ("ab", "{F} Si el dato dijera que en esa región no había familias que enviaran hijos a estudiar, ¿cambiaría la explicación?", "Sí, el dato de contexto ya no apoyaría la idea del sacrificio", "No, el contexto nunca cambia una explicación", "Sin el dato, la explicación del sacrificio perdería parte de su apoyo.")],
  ("abc", "Un taller de lectura de tu comunidad lee «La red de doña Inés». Una persona dice que no entiende por qué ella no responde. ¿Qué ayuda ofrecerías?", "Mostrar el dato de contexto y la cita del atado de monedas", "Decirle que no lea ese cuento", "Pedirle que adivine sin ayuda", "Dato de contexto más cita ayudan a entender el detalle."),
  [("En Lengua y Literatura: ¿qué es un detalle en un cuento?", "Un gesto, objeto o frase pequeña con significado", "Aunque sea pequeño, el detalle puede explicar mucho."),
   ("¿Para qué se usa un dato de contexto al leer?", "Para explicar mejor lo que muestra el texto", "El contexto ilumina lo que el texto ya muestra."),
   ("¿Qué debe acompañar siempre a una explicación?", "Una cita del texto", "Sin cita, la explicación se queda en suposición.")],
  ("Lee el cuento y el dato de contexto: {F} Elige un detalle del cuento (el silencio de doña Inés, el libro prestado o el atado de monedas). Escribe cuatro oraciones: el detalle con su cita exacta, qué crees que significa, qué dato de contexto te ayuda y cómo cambia tu lectura.",
   "Detalle: «dejó junto a su cama un atado de monedas». Significa apoyo silencioso al hijo. El dato de que las familias hacían sacrificios para que un hijo estudiara me ayuda. Sin ese dato pensaría que no le importaba; con él veo ahorro y cariño.",
   ["elige un detalle y lo cita exacto", "dice qué podría significar", "usa un dato de contexto sin inventar hechos"],
   ["cuatro oraciones"],
   ["explicar sin citar", "inventar hechos que el texto no cuenta"],
   "Pregunta: «¿Qué te dijo el dato de contexto que no veías antes?»."),
  "Anota un gesto silencioso que hayas visto en tu familia o trabajo y qué significaba.",
  "Escribe una oración que diga cómo cambia el cuento si cambia el dato de contexto.")

# ============================================================ clase 5
CARTA = ("Cuento (inventado), «La carta que tardó», de Anselmo Rivas (autor ficticio): Elena esperó tres semanas una carta de su hermano, que trabajaba en el sur. "
         "Cada tarde miraba al cartero por la ventana. Cuando por fin llegó, ella no la abrió enseguida: la dejó sobre la mesa y preparó té. Después la leyó despacio, dos veces. "
         "Dato de contexto (inventado): en la época de este cuento ficticio no había teléfonos en la caleta y las noticias viajaban por carta.")
RECEP = ("Comentario de un lector de 1938 (inventado): «Me emocionó la espera, porque yo también esperé cartas así». "
         "Comentario de una lectora de hoy (inventado): «Me costó entender por qué ella no abrió la carta enseguida, porque hoy los mensajes llegan al instante».")
K(5, CARTA + " " + RECEP,
  "Hoy aplico lo aprendido a una situación de comunidad: preparar un discurso breve para presentar un cuento en la junta de vecinos usando el contexto de producción y de recepción.",
  ["Presentar una obra ante otras personas es una situación real: puede ocurrir en un taller de lectura, en una reunión de vecinos o en un trabajo. Una buena presentación no cuenta todo el cuento; ayuda a que la audiencia lo entienda mejor.",
   "Un discurso breve de presentación tiene tres partes. Primero, se dice de qué obra se trata y quién la escribió. Segundo, se da un dato de contexto de producción que ayude a entender un detalle. Tercero, se invita a leer pensando en cómo lo leemos hoy, es decir, en el contexto de recepción.",
   "Hoy compararemos dos recepciones del mismo cuento, la de 1938 y la actual. Verás que ninguna lectura es mejor por sí sola: cada una se apoya en lo que sabe y vive. Ese reconocimiento de la diversidad de lecturas enriquece la conversación y el respeto entre quienes participan."],
  [("discurso breve", "exposición oral corta que presenta una idea o una obra"), ("audiencia", "personas que escuchan o leen"), ("recepción", "modo en que un público recibe y entiende una obra"), ("espera", "tiempo en que se aguarda algo")],
  [("Armar el inicio del discurso", "Se quiere presentar «La carta que tardó» ante la junta de vecinos.",
    ["Digo el título y el autor: «La carta que tardó», de Anselmo Rivas, autor ficticio.", "Doy un dato de producción: en esa época no había teléfono y las noticias viajaban por carta.", "Invito a pensar cómo cambia hoy la espera."], "Inicio con título, autor y contexto"),
   ("Comparar dos recepciones", "Lector de 1938: «Me emocionó la espera». Lectora de hoy: «Me costó entender por qué no la abrió enseguida».",
    ["En 1938, esperar cartas era común.", "Hoy los mensajes llegan al instante.", "Cada lector entiende la espera según su época."], "La recepción cambia con la época")],
  [("Contar todo el cuento en el discurso y no decir nada del contexto.", "La presentación se vuelve resumen y no ayuda a profundizar.", "Presenta pocas ideas y agrega un dato de contexto."),
   ("Decir que la lectora de hoy se equivoca.", "Su lectura nace de otro contexto de recepción.", "Reconoce que cada época lee desde lo que vive.")],
  [("abc", "{F} ¿Cuánto tiempo esperó Elena la carta?", "Tres semanas", "Tres días", "Tres meses", "El cuento dice que esperó tres semanas."),
   ("ab", "{F} ¿Qué hace Elena cuando por fin llega la carta?", "La deja sobre la mesa, prepara té y la lee despacio", "La abre enseguida y la lee de pie", "El cuento dice que no la abrió enseguida y la leyó despacio, dos veces."),
   ("{F} ¿Cuántas veces lee la carta Elena? Escribe el número.", "2", "El texto indica que la leyó despacio, dos veces."),
   ("abc", "{F} ¿Qué dato de producción ayuda a entender la espera de Elena?", "No había teléfonos en la caleta y las noticias viajaban por carta", "El cartero usaba una bicicleta nueva", "El hermano vivía en una ciudad grande", "Sin teléfonos, una carta era la única vía de noticias."),
   ("abc", "{F} ¿Por qué la lectora de hoy se extraña de la escena?", "Porque hoy los mensajes llegan al instante", "Porque el cuento no está bien escrito", "Porque no sabe leer cartas", "Su extrañeza viene de su contexto de recepción actual."),
   ("ab", "{F} El comentario del lector de 1938 muestra principalmente", "que reconocía esa espera por experiencia propia", "que no entendía la escena", "El lector de 1938 dice que él también esperó cartas así."),
   ("abc", "Para presentar el cuento en la junta de vecinos, ¿qué debe decir primero el discurso?", "El título de la obra y quién la escribió", "Cómo termina el cuento", "Una opinión sobre el autor sin datos", "Una presentación comienza ubicando la obra y su autor."),
   ("abc", "{F} ¿Qué frase sería un buen dato de contexto de producción para el discurso?", "«En esa época las noticias viajaban por carta»", "«A mí me dio sueño»", "«La carta es de color blanco»", "Es un dato de época que ayuda a entender el cuento."),
   ("abc", "{F} ¿Qué frase invita a pensar en la recepción actual?", "«Hoy esperamos mensajes de otra manera: ¿qué cambia para el personaje?»", "«Elena se llama así por su abuela»", "«Las cartas siempre llegan tarde»", "Compara la época del cuento con la actual."),
   ("ab", "{F} Una vecina dice: «El lector de 1938 leyó bien y la lectora de hoy leyó mal». ¿Es una buena conclusión?", "No, cada lectura se apoya en una experiencia distinta", "Sí, la lectura de 1938 siempre es la correcta", "Ambas lecturas se apoyan en el cuento y en un contexto de lectura propio."),
   ("abc", "{F} ¿Qué parte del cuento muestra cuánto valor tenía la carta para Elena?", "Que miraba cada tarde al cartero por la ventana", "Que preparó té", "Que su hermano trabajaba en el sur", "La espera diaria muestra el valor que le daba a la noticia."),
   ("abc", "{F} Un oyente pregunta: «¿Por qué no abrió la carta enseguida?». ¿Qué respuesta usa el cuento y el contexto?", "Quizá quería saborear la noticia tras una espera larga, algo posible en esa época", "Porque era una carta falsa", "Porque no le interesaba su hermano", "Se apoya en la espera de tres semanas y en el contexto de época."),
   ("ab", "{F} Si Elena hubiera podido hablar con su hermano por teléfono el mismo día, ¿se perdería algo del cuento?", "Sí, desaparecería la espera, que es lo que da sentido a la escena", "No, el cuento sería igual", "La espera de tres semanas es el centro de la escena, y el contexto la explica.")],
  ("abc", "Te piden hablar dos minutos en una reunión de vecinos sobre un libro que leíste. ¿Cuál es una buena organización?", "Título y autor, un dato de contexto y una invitación a leer", "Todo el argumento con detalles", "Una lista de personajes sin explicar", "Tres partes breves hacen un discurso claro y respetuoso del tiempo."),
  [("En Lengua y Literatura: ¿para qué sirve conocer el contexto de recepción?", "Para entender cómo cambia la lectura según la época", "Muestra por qué distintas personas leen distinto."),
   ("¿Qué tres partes tiene el discurso breve de hoy?", "Título y autor, dato de contexto e invitación a leer", "Es una organización simple para presentar una obra."),
   ("¿Una lectura de hoy sobre un cuento antiguo es un error?", "No, parte de otro contexto de recepción", "Cada época lee desde lo que vive.")],
  ("Prepara tu discurso a partir del cuento: {F} Escribe en tu cuaderno un discurso de cinco oraciones para presentar «La carta que tardó» en la junta de vecinos: título y autor, un dato de contexto de producción, un detalle del cuento con cita y una invitación a pensar en la recepción actual. Léelo en voz alta, sin datos personales.",
   "«Hoy presentaré «La carta que tardó», de Anselmo Rivas, autor ficticio. En esa época las noticias viajaban por carta. Elena «esperó tres semanas» una carta de su hermano. Los invito a leerlo pensando cómo cambia hoy esa espera. Así veremos qué nos dice sobre quienes esperamos noticias».",
   ["incluye título y autor", "un dato de contexto de producción", "una cita exacta del cuento", "una invitación sobre la recepción actual"],
   ["un discurso de cinco oraciones leído en voz alta"],
   ["contar todo el argumento", "decir que una lectura es la única correcta"],
   "Pregunta: «¿Qué dato ayuda a la audiencia a entender mejor?»."),
  "Cuenta a alguien de tu familia o trabajo cómo se recibían noticias de personas lejanas antes de los mensajes instantáneos.",
  "Escribe qué cambiaría en el cuento si Elena viviera hoy y tuviera un teléfono.")

# ============================================================ clase 6
CASOS = ("Cuento de referencia (inventado), «El farolero», de Anselmo Rivas (autor ficticio): don Telmo enciende los faroles de la caleta cada tarde, hasta que, según el cuento, «un día llegó la luz eléctrica y don Telmo quedó sin oficio»; «esa noche subió igual». "
         "Comentario A: «Don Telmo sube al cerro, enciende faroles y llega la luz eléctrica». "
         "Comentario B: «El cuento trata de la pena de perder un trabajo». "
         "Comentario C: «Cuando el autor escribió, llegaban las luces eléctricas y se perdían oficios; por eso el cuento muestra la pena de don Telmo: ‘quedó sin oficio’». "
         "Pauta: 1) resume el tema; 2) usa una cita; 3) relaciona con el contexto de producción; 4) explica un aspecto de la obra.")
K(6, CASOS,
  "Hoy reviso lo logrado: evalúo comentarios con una pauta, distingo resumen e interpretación con contexto y decido mis próximos pasos.",
  ["Hemos recorrido el camino completo: partimos de lo que ya sabíamos, aprendimos los conceptos de contexto de producción y de recepción, armamos organizadores con citas y los usamos para explicar detalles y preparar una presentación. Hoy revisamos qué tan bien lo hacemos.",
   "Para evaluar un comentario puedes usar una pauta. Esta pauta pregunta si el comentario resume el tema, si usa una cita exacta, si relaciona la obra con su contexto de producción y si explica un aspecto del texto, como un personaje o una acción. Cuantos más criterios cumple, más sólida es la lectura.",
   "Evaluar no es humillar: es descubrir qué falta para mejorar. Un comentario que solo resume tiene una base útil, pero le falta sentido. Una interpretación sin cita es una opinión sin prueba. Y cuando cambia una condición, como el dato de contexto, la conclusión también puede cambiar; eso muestra que está bien pensada."],
  [("pauta", "lista de criterios para evaluar un trabajo"), ("criterio", "aspecto que se mira para evaluar"), ("evidencia", "dato o cita que prueba una idea"), ("conclusión", "idea final a la que se llega con razones")],
  [("Aplicar la pauta", "Comentario A: «Don Telmo sube al cerro, enciende faroles y llega la luz eléctrica». ¿Cuántos criterios de la pauta cumple?",
    ["1) Resume el tema: solo cuenta hechos, no nombra un tema: no cumple.", "2) Usa una cita: no hay comillas: no cumple.", "3) Contexto: no cumple. 4) Explicar un aspecto: no cumple."], "Cumple 0 criterios; es solo un resumen"),
   ("Mejorar un comentario", "Comentario B: «El cuento trata de la pena de perder un trabajo». ¿Qué le falta?",
    ["Sí enuncia un tema (criterio 1).", "No cita el cuento ni usa contexto.", "Puedo agregar: «quedó sin oficio» y que en esa época llegaban las luces eléctricas."], "Le faltan la cita y el contexto")],
  [("Dar por buena una interpretación porque «suena bien».", "Sin cita ni contexto no se puede comprobar.", "Revisa con la pauta si hay prueba en el texto."),
   ("Pensar que una conclusión no debe cambiar nunca.", "Si cambia la evidencia, una buena lectura se ajusta.", "Revisa qué datos sostienen tu conclusión y qué pasa si cambian.")],
  [("abc", "{F} ¿Cuál comentario solo cuenta hechos y no interpreta?", "El A", "El B", "El C", "El A repite lo que ocurre sin proponer un sentido."),
   ("ab", "{F} ¿Qué comentario enuncia un tema sin apoyarlo con cita?", "El B", "El C", "El B dice que trata de perder un trabajo, pero no cita ni usa contexto."),
   ("{F} ¿Cuántos criterios tiene la pauta? Escribe el número.", "4", "La pauta del enunciado enumera cuatro criterios numerados."),
   ("abc", "{F} ¿Qué comentario cumple los cuatro criterios de la pauta?", "El C", "El A", "El B", "El C resume el tema, cita, relaciona con el contexto y explica un aspecto."),
   ("abc", "{F} ¿Qué cita usa el comentario C?", "«quedó sin oficio»", "«enciende los faroles»", "«subió igual»", "La cita aparece entre comillas en el comentario C."),
   ("ab", "{F} ¿Qué dato de contexto de producción usa el comentario C?", "Que cuando el autor escribió llegaban luces eléctricas y se perdían oficios", "Que hoy el libro se lee en talleres de barrio", "El comentario C relaciona el cuento con la época en que se escribió."),
   ("abc", "{F} Un participante dice: «El comentario C es mejor porque es más largo». ¿Qué respondes?", "Es mejor porque cumple más criterios, no por su largo", "Es mejor porque usa palabras difíciles", "No hay ninguna diferencia entre los comentarios", "La calidad se evalúa con criterios, no con la extensión."),
   ("abc", "{F} Agrega un criterio de la pauta al comentario B: ¿qué podrías añadir para cumplir el segundo?", "La cita «quedó sin oficio»", "Un nuevo título", "El nombre del autor repetido", "El criterio 2 pide una cita exacta del cuento."),
   ("abc", "{F} ¿Qué comentario necesita más apoyo para pasar de resumir a interpretar?", "El A, porque no propone ningún sentido", "El C, porque tiene cita", "El C, porque nombra el contexto", "El comentario A solo repite hechos sin dar sentido."),
   ("ab", "{F} Si el dato de contexto del comentario C fuera falso, ¿qué pasaría con su conclusión?", "Perdería apoyo y habría que revisarla", "Se mantendría igual de sólida", "La relación con el contexto dependería de un dato que ya no es válido."),
   ("abc", "{F} ¿Qué conviene hacer antes de decir que una interpretación es correcta?", "Comprobar la cita y la relación con el contexto", "Preguntar quién habla más fuerte", "Ver cuántas palabras tiene", "La evidencia permite comprobar una interpretación."),
   ("abc", "{F} Una persona logró escribir algo parecido al comentario B. ¿Cuál es su siguiente paso?", "Agregar cita y contexto para llegar al nivel del C", "Dejarlo igual", "Reducirlo a una sola palabra", "El siguiente paso es sumar los criterios que le faltan."),
   ("ab", "{F} ¿Qué actitud es correcta al evaluar el comentario de otra persona?", "Señalar con respeto qué logró y qué le falta", "Decirle que su trabajo no sirve", "Evaluar sirve para ayudar a mejorar, nunca para humillar.")],
  ("abc", "En tu trabajo te piden dar opinión sobre un informe de un compañero. ¿Qué actitud se parece más a evaluar con una pauta?", "Mirar criterios claros y decir qué cumple y qué falta", "Decir solamente «me gustó» o «no me gustó»", "Corregirlo delante de todos", "La pauta permite una opinión respetuosa y concreta."),
  [("En Lengua y Literatura: ¿qué es una pauta?", "Una lista de criterios para evaluar un trabajo", "Permite revisar con claridad lo que está logrado."),
   ("¿Qué criterio distingue una interpretación de un resumen?", "Que propone un sentido y lo apoya con cita y contexto", "El resumen cuenta hechos; la interpretación les da sentido."),
   ("¿Para qué sirve evaluar mi propio trabajo?", "Para saber qué mejorar y decidir los pasos siguientes", "Evaluar el propio avance es parte de aprender.")],
  ("Aplica la pauta: {F} En tu cuaderno copia el comentario B y reescríbelo para cumplir los cuatro criterios (tema, cita exacta, dato de contexto de producción y un aspecto explicado). Después escribe qué parte te costó más y qué harás para practicarla.",
   "Reescritura: «El cuento trata de la pena de perder un trabajo: don Telmo ‘quedó sin oficio’. Cuando el autor escribió, llegaban las luces eléctricas y se perdían oficios; por eso el cuento muestra su pena al subir igual esa noche». Me costó citar exacto; practicaré copiando frases.",
   ["cumple los cuatro criterios", "cita exacta con comillas", "reflexiona sobre qué le costó"],
   ["un párrafo reescrito y una reflexión de dos líneas"],
   ["cumplir menos de cuatro criterios", "no decir qué parte le costó"],
   "Pregunta: «¿Qué criterio te falta para pasar al siguiente nivel?»."),
  "Revisa con la pauta algo que hayas escrito en esta unidad y marca los criterios que cumple.",
  "Elige un cuento corto que conozcas y escribe cuál sería el dato de contexto que más ayudaría a entenderlo.")

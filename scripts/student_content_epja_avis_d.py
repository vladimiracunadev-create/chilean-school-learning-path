"""Artes Visuales EPJA Media N1 y N2, módulo 4, OAD-13: seleccionar y evaluar, como curadores, obras y proyectos propios con criterios estéticos para una muestra. Obras y fichas ficticias; todo en papel."""
from __future__ import annotations

from epja_avis_d_common import K, O13, build  # noqa: F401

# ====================================================== OAD-13 clase 1
F = ("Ficha 1 (obras de ejemplo de un taller ficticio de una sede vecinal; tema de la muestra: «Oficios del barrio»; cupo: 3 obras). "
     "Obra A: acuarela de una panadera amasando, colores cálidos y composición equilibrada. "
     "Obra B: dibujo a lápiz de una costurera ante su máquina; muy detallado, pero una esquina quedó sin terminar. "
     "Obra C: collage de manos de distintos oficios, recortes bien pegados y título claro. "
     "Obra D: video de 2 minutos de un zapatero reparando, imagen estable y sonido con ruido de fondo. "
     "Obra E: pintura acrílica de un cerro al atardecer, color intenso, sin relación con el tema.")
K(O13, 1, F,
  "Hoy aprenderé qué hace una persona curadora, qué es un criterio estético y cómo elegir obras propias para una muestra con razones y no solo por gusto.",
  ["Una muestra es un conjunto de obras que se presenta a un público. La curaduría es el trabajo de elegir y organizar esas obras. Quien la hace se llama curador o curadora. Ya haces algo parecido cuando eliges qué fotos poner en la pared de tu casa: la diferencia es que ahora explicamos por qué.",
   "Un criterio estético es una característica de la obra que se observa para valorarla. Algunos son la composición, que es cómo se distribuyen los elementos en el espacio; el color; la técnica, es decir, cómo está hecha; y la originalidad. También se mira si la obra tiene relación con el tema de la muestra y si está bien terminada.",
   "Elegir por gusto personal es válido, pero no basta para decidir con otras personas. Con criterios acordados, cualquiera puede revisar la elección y entender las razones. Cuando hay un cupo, que es el número máximo de obras que caben, se compara cada obra con los criterios y se dejan fuera las que menos los cumplen. Todas las obras de ejemplo de esta clase son inventadas."],
  [("curaduría", "trabajo de elegir y organizar las obras de una muestra"), ("criterio estético", "característica de la obra que se observa para valorarla"), ("composición", "forma en que se distribuyen los elementos dentro de la obra"), ("cupo", "número máximo de obras que caben en la muestra")],
  [("Elegir con un criterio", "En la ficha, la obra E es un cerro al atardecer y el tema es «Oficios del barrio». ¿Se ajusta E al tema?", ["Se compara el contenido de la obra con el tema.", "El cerro no muestra ningún oficio."], "No se ajusta al tema"),
   ("Calcular cuántas quedan fuera", "Hay 7 obras y el cupo es 4. ¿Cuántas quedan fuera?", ["Se resta el cupo al total de obras.", "7 - 4 = 3."], "Quedan fuera 3 obras")],
  [("Elegir solo la obra que más me gusta.", "Se confunde el gusto personal con una razón compartida.", "Compara cada obra con el tema y los criterios, y anota por qué la eliges."),
   ("Dejar fuera una obra buena porque no es mía favorita.", "Se mezcla el cariño por la obra con su ajuste a la muestra.", "Una obra puede ser buena y aun así no calzar con el tema o el espacio disponible.")],
  [("abc", "En Artes Visuales: ¿qué hace una persona curadora?", "Elige y organiza obras para una muestra, apoyándose en criterios", "Pinta todas las obras de la muestra por su cuenta", "Cobra la entrada y cuida la puerta de la sala", "Curar es seleccionar y ordenar obras con razones explicables."),
   ("ab", "Un criterio estético es", "una característica de la obra que se observa para valorarla", "la opinión de quien la hizo sobre su propio talento", "Se observa algo concreto de la obra, como su composición o su color."),
   ("abc", "{F} ¿Cuál obra se aparta del tema «Oficios del barrio»?", "La obra E, el cerro al atardecer", "La obra A, la panadera amasando", "La obra C, el collage de manos", "Solo el cerro no muestra ningún oficio del barrio."),
   ("=", "Si la muestra incluyera tres videos como la obra D, de 2 minutos cada uno, ¿cuántos minutos duraría verlos todos seguidos?", "3*2", "Se multiplica la duración de un video por el número de videos.", " minutos"),
   ("abc", "{F} En la obra B, la esquina sin terminar afecta sobre todo el criterio de", "terminación de la técnica", "relación con el tema", "originalidad del título", "Una zona sin resolver revela un trabajo todavía incompleto."),
   ("ab", "Elegir obras para una muestra con criterios sirve porque", "otras personas pueden entender y revisar las razones", "así nadie tiene que mirar las obras", "Los criterios hacen visibles los motivos de la decisión."),
   ("abc", "{F} El video D tiene sonido con ruido de fondo. ¿Qué criterio se ve afectado?", "La calidad técnica de la presentación", "El color de la acuarela", "El tamaño del cupo", "El ruido dificulta escuchar y es un aspecto técnico del video."),
   ("abc", "{F} El cupo es 3. ¿Qué selección respeta el tema y la variedad de medios?", "A, C y D", "A, B y E", "B, C y E", "Las otras dos incluyen la obra E, que no se relaciona con el tema."),
   ("=", "Una persona tiene 5 obras listas y el cupo es de 3. ¿Cuántas obras debe dejar fuera?", "5-3", "Se resta el cupo al total de obras disponibles.", " obras"),
   ("abc", "Una persona dice: «Elijo mi obra E porque es mi favorita». ¿Qué le falta a su razón?", "Relacionarla con el tema y los criterios de la muestra", "Pintarla de nuevo con otros colores", "Mostrarla solo a su familia", "El gusto personal necesita apoyarse en criterios compartidos."),
   ("ab", "¿Por qué una obra muy bien hecha puede quedar fuera de una muestra?", "Porque puede no calzar con el tema o con el espacio", "Porque las obras buenas nunca se exponen", "El curador compara con el tema y el cupo, no solo con la calidad."),
   ("abc", "Dos obras tienen el mismo tema, la misma técnica y casi la misma imagen, y el cupo es limitado. ¿Qué decisión es más razonable?", "Elegir una y dejar espacio a obras con otra técnica", "Elegir ambas y quitar una obra distinta", "Elegir al azar sin mirar las obras", "La variedad de técnicas enriquece lo que el público puede mirar."),
   ("abc", "Una obra tuya muy querida no calza con el tema de esta muestra. ¿Qué decisión curatorial es coherente?", "Guardarla para otra muestra y explicar por qué no entra ahora", "Colgarla igual para no dar explicaciones", "Cambiar el tema de la muestra a la fuerza", "Dejarla fuera no la desvaloriza: solo no calza con esta muestra.")],
  ("abc", "Una persona adulta debe elegir tres obras suyas para una muestra en la biblioteca del barrio. ¿Qué es lo primero que conviene hacer?", "Revisar el tema y los criterios de la muestra antes de elegir", "Elegir las tres primeras que encuentre", "Elegir por sorteo, sin mirar el tema", "Sin tema ni criterios claros, cualquier elección queda sin razones."),
  [("En Artes Visuales: ¿qué es una muestra?", "Un conjunto de obras que se presenta a un público", "La muestra reúne obras con un propósito y un espacio."),
   ("¿Para qué sirve un criterio estético al elegir obras?", "Para dar razones observables de la elección", "Con criterios, la decisión se puede explicar y revisar."),
   ("¿Qué es el cupo de una muestra?", "El número máximo de obras que caben", "El cupo obliga a comparar y dejar algunas obras fuera.")],
  ("{F} Elige las tres obras que pondrías en la muestra «Oficios del barrio» y deja fuera dos. Para cada obra escribe el criterio que usaste: tema, composición, técnica u otro.",
   "Elijo A (tema claro y composición equilibrada), C (tema claro y buena terminación) y D (suma el medio video). Dejo fuera B por la esquina sin terminar y E porque no se relaciona con el tema.",
   ["elige exactamente tres obras", "indica un criterio por cada obra elegida", "explica por qué deja fuera las otras dos"],
   ["texto breve con las tres obras elegidas, sus criterios y las dos dejadas fuera"],
   ["elegir solo por gusto sin criterio", "elegir más de tres obras"],
   "Revisa que cada obra tenga un criterio observable. Si alguien escribe «me gusta», pide que diga qué se ve en la obra que lo hace valiosa. Acepta selecciones distintas si están bien justificadas."),
  "Escribe tres criterios estéticos y, con tus palabras, qué mira cada uno en una obra.",
  "Elige dos obras o imágenes (reales o inventadas) y escribe cuál pondrías en una muestra sobre «mi barrio» y por qué.")

# ====================================================== OAD-13 clase 2
F = ("Ficha 2 (obras de ejemplo de un grupo ficticio; tema de la muestra: «Agua y vida en el barrio»; cupo: 4 obras). "
     "Pauta con cuatro criterios, cada uno de 1 a 4 puntos: tema, composición, técnica y originalidad. "
     "Obra F, fotografía de una llave de agua con un balde: tema 4, composición 3, técnica 4, originalidad 2. "
     "Obra G, grabado de un río entre casas: tema 3, composición 4, técnica 3, originalidad 4. "
     "Obra H, pintura de una fila de personas con baldes: tema 4, composición 3, técnica 3, originalidad 3. "
     "Obra I, video de 3 minutos de una vecina regando su huerta: tema 4, composición 2, técnica 2, originalidad 4. "
     "Obra J, dibujo de un paisaje seco con una nube: tema 2, composición 3, técnica 4, originalidad 2.")
K(O13, 2, F,
  "Hoy aprenderé a evaluar obras con una pauta de criterios y puntajes, a sumar el puntaje de cada obra y a decidir qué obras entran cuando hay un cupo.",
  ["Una pauta es una tabla con criterios y una escala de puntos. En esta clase cada criterio vale de 1 a 4 puntos y el puntaje total de una obra es la suma de sus cuatro criterios, así que va de 4 a 16. Evaluar con pauta ayuda a comparar obras distintas con la misma vara.",
   "Para decidir se ordenan las obras de mayor a menor puntaje y se llenan los cupos desde arriba. Pero el puntaje no lo dice todo. El curador también mira que el conjunto sea coherente con el tema, que haya variedad de técnicas y que la muestra se entienda como un todo. Si dos obras empatan, se desempata con una razón explícita, por ejemplo el ajuste al tema.",
   "Un puntaje es una ayuda, no una sentencia sobre quien hizo la obra. Una obra con puntaje bajo en un criterio puede mejorar con más trabajo. Evalúa la obra, no a la persona, y comunica las decisiones con respeto: así quien no entra en esta muestra puede volver a intentarlo en otra."],
  [("pauta", "tabla con criterios y una escala de puntos para evaluar"), ("puntaje total", "suma de los puntos de todos los criterios"), ("empate", "situación en que dos obras tienen el mismo puntaje"), ("coherencia", "relación lógica entre las obras y el tema de la muestra")],
  [("Sumar una pauta", "En la ficha, la obra F tiene 4, 3, 4 y 2 puntos. ¿Cuál es su puntaje total?", ["Se suman los cuatro criterios.", "4 + 3 + 4 + 2 = 13."], "13 puntos"),
   ("Decidir con cupo", "Cinco obras tienen 15, 14, 12, 11 y 9 puntos y el cupo es 3. ¿Cuál es el puntaje más bajo que entra?", ["Se ordenan de mayor a menor.", "Entran las tres primeras: 15, 14 y 12."], "12 puntos")],
  [("Sumar solo tres de los cuatro criterios.", "Se olvida uno de los criterios de la pauta.", "Revisa que cada obra tenga cuatro puntajes antes de sumar."),
   ("Elegir solo por el puntaje total sin mirar el conjunto.", "Se cree que el número reemplaza el juicio del curador.", "Después de sumar, mira si el conjunto es coherente y variado.")],
  [("abc", "{F} ¿Cuál es el puntaje máximo posible de una obra con esa pauta?", "16 puntos, porque son cuatro criterios de hasta 4", "4 puntos, porque la escala llega a 4", "8 puntos, porque son dos categorías", "El máximo es 4 puntos multiplicados por 4 criterios."),
   ("=", "{F} Calcula el puntaje total de la obra G sumando sus cuatro criterios (3, 4, 3 y 4).", "3+4+3+4", "Se suman los cuatro puntajes de la pauta de la obra G.", " puntos"),
   ("ab", "En una pauta, el puntaje total de una obra se obtiene", "sumando los puntos de todos los criterios", "eligiendo solo el criterio más alto", "El total reúne todos los criterios evaluados."),
   ("=", "{F} Calcula el puntaje total de la obra H sumando 4, 3, 3 y 3.", "4+3+3+3", "Se suman los cuatro criterios de la obra H.", " puntos"),
   ("abc", "{F} La obra I tiene puntaje bajo en composición y técnica. ¿Qué tiene alto?", "El tema y la originalidad", "La técnica y la composición", "Solamente la composición", "En la ficha, I tiene 4 en tema y 4 en originalidad."),
   ("=", "{F} Calcula el puntaje total de la obra I (4, 2, 2 y 4).", "4+2+2+4", "Se suman los cuatro puntajes de la obra I.", " puntos"),
   ("abc", "{F} Con puntajes G 14, F 13, H 13, I 12 y J 11, ¿qué obras entran con cupo de 4?", "G, F, H e I", "G, F, H y J", "F, H, I y J", "Se llenan los cuatro cupos de mayor a menor puntaje."),
   ("=", "{F} ¿Cuántos puntos de diferencia hay entre la obra G (14) y la obra J (11)?", "14-11", "Se resta el puntaje menor al mayor.", " puntos"),
   ("abc", "F y H empatan con 13 puntos y solo cabe una de las dos. El tema es «Agua y vida en el barrio». ¿Qué desempate es una razón válida?", "Elegir la que muestre más personas del barrio usando el agua", "Elegir la que tenga el marco más caro", "Sortear sin mirar el tema", "El desempate debe apoyarse en un criterio explícito de la muestra."),
   ("abc", "Una obra tiene puntaje total bajo, pero es la única que muestra el tema desde un ángulo nuevo. ¿Qué puede hacer el curador?", "Revisarla de nuevo y evaluar si aporta variedad al conjunto", "Rechazarla sin mirarla porque el número es bajo", "Subirle el puntaje sin explicar nada", "El puntaje orienta, pero el juicio también mira el conjunto."),
   ("ab", "Una persona dice: «Mi obra sacó pocos puntos, así que soy mala artista». ¿Qué respuesta es más adecuada?", "El puntaje evalúa esta obra en esta muestra, no el valor de la persona", "Tiene razón: el puntaje mide el talento completo", "La pauta califica una obra con criterios concretos, no a quien la hizo."),
   ("abc", "Cuatro obras entran y todas son fotografías de llaves de agua casi iguales. ¿Qué problema tiene la muestra?", "Falta variedad de técnicas y miradas", "Tiene demasiados puntos", "No cabe en el cupo", "Aunque puntúen bien, el conjunto se vuelve repetitivo."),
   ("abc", "Un curador anota: «Dejo fuera la obra J porque tiene 11 puntos y el tema de la muestra es el agua, mientras que J tiene 2 en tema». ¿Qué tiene de bueno esa razón?", "Usa el puntaje y un criterio concreto de la pauta", "No usa ningún dato", "Se basa solo en el gusto", "Une el número con el criterio que más pesó en la decisión.")],
  ("abc", "Un grupo comunitario ficticio evalúa tres obras con la misma pauta y obtiene 12, 15 y 15 puntos. Solo hay dos cupos. ¿Cuál es el primer paso?", "Aceptar las dos de 15 puntos y revisar con el tema si hay algo que cambiar", "Descartar las tres y empezar de nuevo", "Elegir la de 12 por ser la primera", "Las dos con más puntos entran; conviene confirmar su coherencia."),
  [("En Artes Visuales: ¿qué es una pauta?", "Una tabla con criterios y una escala de puntos", "La pauta permite comparar obras con una misma vara."),
   ("¿Cómo se calcula el puntaje total de una obra?", "Sumando los puntos de todos los criterios", "El total reúne cada criterio evaluado."),
   ("¿Qué se hace cuando dos obras empatan?", "Se desempata con una razón explícita, como el ajuste al tema", "Un empate se resuelve con criterios, no con el azar.")],
  ("{F} Con los puntajes de la ficha, ordena las cinco obras de mayor a menor, elige las cuatro que entran y escribe una razón de conjunto: ¿la muestra queda variada y coherente con el tema?",
   "Orden: G 14, F 13, H 13, I 12, J 11. Entran G, F, H e I. La muestra tiene grabado, fotografía, pintura y video, y todas hablan del agua; J queda fuera por su bajo ajuste al tema.",
   ["suma o usa los puntajes de las cinco obras", "elige cuatro con el orden correcto", "justifica la variedad o la coherencia del conjunto"],
   ["lista ordenada con los puntajes, cuatro obras elegidas y una razón de conjunto"],
   ["no sumar los cuatro criterios", "justificar solo con «me gusta»"],
   "Comprueba las sumas: G 14, F 13, H 13, I 12, J 11. Si alguien deja una obra de mayor puntaje fuera, pide el criterio que usó. Acepta una razón que mencione variedad de técnicas."),
  "Suma tú el puntaje de una de las obras de la ficha y escribe cuál criterio fue el más alto.",
  "Inventa una pauta de cuatro criterios para evaluar fotografías de tu barrio y define qué significa 1 y qué significa 4.")

# ====================================================== OAD-13 clase 3
F = ("Ficha 3 (caso ficticio de una sede vecinal; tema de la muestra: «Memorias del barrio»; cupo: 5 espacios; la sala puede proyectar un máximo de 6 minutos de video en total). "
     "Hay 9 obras propias disponibles: cinco pinturas o dibujos (P1 a P5), una serie de 6 fotografías (S1) y tres videos: V1 de 3 minutos, V2 de 4 minutos y V3 de 2 minutos. "
     "Notas del grupo: P1 y P2 muestran la misma esquina con la misma técnica. P3 trata del tema, pero su título no se lee. P4 y P5 son claras y muy distintas entre sí. "
     "S1 cuenta la historia de una calle. V2 es el que mejor cuenta el tema, pero es el más largo.")
K(O13, 3, F,
  "Hoy aprenderé a aplicar la curaduría a una situación comunitaria: elegir obras de distintos medios, respetar los límites de espacio y tiempo y justificar la selección.",
  ["En una muestra real las obras no siempre son del mismo tipo. Puede haber pinturas, fotografías y videos. Cada medio tiene límites distintos: una pintura necesita espacio en el muro y un video necesita tiempo de proyección. El curador reparte los espacios y el tiempo para que ninguna parte quede sobrando ni faltando.",
   "Para decidir con varios límites, conviene ordenar el trabajo en pasos: revisar el tema, descartar lo que no calza, comprobar que lo elegido cabe en el espacio y en el tiempo, y mirar si el conjunto es variado. Un buen conjunto tiene un comienzo claro, un recorrido y una idea común que lo une.",
   "Al terminar, cada obra elegida lleva una ficha corta con título, nombre de la autoría, técnica y una línea que explica por qué está en la muestra. Si hay obras de otras personas, se pide permiso antes de usarlas. Este grupo y sus obras son inventados, para que nadie tenga que exponer su vida."],
  [("recorrido", "orden en que el público mira las obras"), ("medio", "tipo de obra, como pintura, fotografía o video"), ("ficha de obra", "texto breve con título, autoría, técnica y una línea sobre la obra"), ("conjunto", "obras elegidas vistas como un todo coherente")],
  [("Tiempo de proyección", "El límite es 6 minutos. ¿Caben juntos V1 (3 min) y V3 (2 min)?", ["Se suman las duraciones.", "3 + 2 = 5, y 5 es menor que 6."], "Sí caben: son 5 minutos"),
   ("Repartir cupos", "Hay 5 espacios. Se eligen 2 videos y la serie S1, que ocupa un espacio. ¿Cuántos espacios quedan para pinturas?", ["Se cuentan los espacios usados: 2 videos y la serie.", "5 - 3 = 2."], "Quedan 2 espacios")],
  [("Elegir obras que caben cada una por separado pero no juntas.", "No se suman los límites de espacio y de tiempo.", "Suma duraciones y espacios antes de confirmar la selección."),
   ("Dejar un video largo sin pensar si cabe en el tiempo.", "Se mira el contenido pero no el tiempo disponible.", "Comprueba la duración total frente al máximo antes de decidir.")],
  [("abc", "{F} ¿Cuál es el límite total de video que puede proyectarse en la sala?", "6 minutos", "9 minutos", "3 minutos", "La ficha fija un máximo de 6 minutos de proyección."),
   ("=", "{F} Suma la duración de los videos V2 y V3.", "4+2", "Se suman los minutos de los dos videos.", " minutos"),
   ("abc", "{F} ¿Qué par de videos NO cabe junto en la proyección?", "V1 y V2, porque suman más de 6 minutos", "V1 y V3, porque suman 5 minutos", "V2 y V3, porque suman exactamente 6", "V1 y V2 dan 7 minutos y superan el máximo."),
   ("abc", "{F} P1 y P2 muestran la misma esquina con la misma técnica. ¿Qué decisión mejora la variedad?", "Elegir solo una de las dos", "Elegir las dos y quitar P4 y P5", "No elegir ninguna", "Repetir la misma imagen resta variedad al conjunto."),
   ("=", "{F} Se elige un video de 4 minutos y otro de 2. ¿Cuántos minutos de proyección quedan libres en el máximo?", "6-4-2", "Se restan al máximo las duraciones elegidas.", " minutos"),
   ("ab", "{F} El título de P3 no se lee. Antes de exponerla, lo más adecuado es", "mejorar la legibilidad de su título", "dejar el título como está para evitar trabajo", "Si el título no se lee, el público pierde información de la obra."),
   ("abc", "{F} Si se eligen V2, P4, P5 y S1, ¿cuántos espacios de los 5 quedan por ocupar?", "1 espacio", "3 espacios", "0 espacios", "Se usan cuatro de los cinco espacios disponibles."),
   ("=", "{F} Hay 9 obras disponibles y solo 5 espacios. ¿Cuántas obras quedan fuera?", "9-5", "Se resta el número de espacios al total de obras.", " obras"),
   ("abc", "Una selección tiene cinco pinturas muy parecidas y ningún video ni fotografía. ¿Cuál es su mayor debilidad?", "Poca variedad de medios en el conjunto", "Demasiado tiempo de proyección", "Exceso de fotografías", "Un conjunto uniforme ofrece menos formas de mirar el tema."),
   ("abc", "El grupo dice que V2 cuenta mejor el tema, pero es largo. Con las demás obras elegidas, ¿qué razonamiento es más sólido?", "Incluirlo si cabe en los 6 minutos junto con otro video corto", "Descartarlo solo por ser largo, sin hacer ninguna suma", "Incluirlo y proyectar 10 minutos igual", "Comprobar tiempo y valor del contenido permite decidir con datos."),
   ("ab", "Una persona dice: «Elijo cinco obras al azar para no pelear». ¿Qué respuesta es más adecuada?", "Mejor comparar con criterios, aunque tome más tiempo", "Tiene razón: el azar siempre es más justo", "Con criterios, el grupo entiende y puede revisar la decisión."),
   ("abc", "En la ficha de una obra de la muestra, ¿qué línea conviene escribir?", "Por qué la obra está en la muestra y qué muestra del tema", "El precio de venta de la obra", "La edad de la persona que la hizo", "La línea explicativa ayuda al público a relacionar obra y tema."),
   ("abc", "Un grupo debe presentar su selección en la reunión del barrio. ¿Qué formato comunica mejor sus razones?", "Una tabla con cada obra elegida, su criterio y su ficha", "Una lista de nombres sin explicación", "Un comentario oral sobre gustos personales", "La tabla muestra decisión y evidencia a la vez.")],
  ("abc", "Un taller de una biblioteca ficticia quiere sumar a su muestra la serie de 6 fotografías de otra vecina. ¿Qué debe hacer antes?", "Pedirle permiso y acordar cómo aparecerá su nombre", "Usarlas sin avisar porque son para la comunidad", "Cambiarles el nombre de la autora", "Pedir permiso y dar el crédito es una buena práctica; los detalles dependen de la norma vigente."),
  [("En Artes Visuales: ¿qué es el recorrido de una muestra?", "El orden en que el público mira las obras", "Un recorrido claro ayuda a comprender el conjunto."),
   ("¿Qué dos límites hay que revisar con obras de pintura y video?", "El espacio en el muro y el tiempo de proyección", "Cada medio usa un recurso distinto y limitado."),
   ("¿Qué lleva la ficha de una obra?", "Título, autoría, técnica y una línea que explica su lugar en la muestra", "La ficha da al público la información básica para mirar.")],
  ("{F} Elige las obras de la muestra «Memorias del barrio»: máximo 5 espacios y 6 minutos de video. Escribe tu selección, comprueba la suma de minutos y da una razón por cada obra.",
   "Elijo V2 (4 min) y V3 (2 min): suman 6 minutos. Elijo S1, P4 y P5. Cinco espacios, tema contado desde medios distintos. Dejo fuera P1, P2, P3 y V1: P1 y P2 repiten, P3 tiene el título ilegible y V1 no cabe junto a V2.",
   ["elige como máximo 5 obras", "comprueba que los videos suman 6 minutos o menos", "da una razón por cada obra elegida"],
   ["lista de selección, suma de minutos y una razón por obra"],
   ["superar el límite de tiempo sin sumar", "repetir obras casi iguales sin razón"],
   "Revisa que la suma de minutos sea correcta y que no haya más de cinco obras. Acepta selecciones distintas si respetan los límites y justifican cada obra con un criterio."),
  "Resta: si de 6 minutos de proyección ya usaste 3, ¿cuántos quedan? Escribe qué video de la ficha podría entrar.",
  "Escribe una ficha de obra de tres líneas para una pintura inventada: título, técnica y una línea que la relacione con el tema «Memorias del barrio».")

"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 09 (tectónica de placas y actividad geológica) y OA 10 (actividad volcánica, consecuencias y riesgo)."""
from __future__ import annotations

from student_content_cn7_a import L, task
from student_lessons import arith

OA9, OA10 = "CN07 OA 09", "CN07 OA 10"

# ---------------------------------------------------------------- OA 09
L(OA9, 1,
  materials="Este cuaderno y lápiz. Las distancias y velocidades están escritas en los ejercicios; opcional: papel para dibujar las capas.",
  use="Aprenderé cuáles son las capas de la Tierra y cómo se mueven las placas tectónicas. Sirve para entender por qué existen volcanes, sismos y cordilleras.",
  prior=["Sé que la Tierra es una esfera de rocas.", "Sé que la energía calienta y mueve los materiales."],
  explain=[
      "La Tierra tiene capas. La corteza es la capa más externa, delgada y rocosa: mide entre 5 y 70 km de espesor. Bajo ella está el manto, de roca caliente que fluye muy lentamente y que llega hasta unos 2.900 km de profundidad. Más adentro está el núcleo externo, líquido, y al centro el núcleo interno, sólido. Ambos núcleos son de hierro y níquel.",
      "La corteza junto con la parte superior rígida del manto forma la litosfera. La litosfera está rota en grandes trozos llamados placas tectónicas. Las placas se desplazan sobre la astenosfera, la parte del manto que es más blanda y fluye lentamente. El calor interno de la Tierra genera corrientes de convección en el manto, y esas corrientes contribuyen al movimiento.",
      "Las placas se mueven unos pocos centímetros por año, más o menos como crecen las uñas. Parece poco, pero en un millón de años suma decenas de kilómetros. Como 1 km tiene 100.000 cm, una placa que avanza 5 cm por año recorre 5.000.000 cm, o 50 km, en un millón de años.",
  ],
  vocab=[("corteza", "capa más externa de la Tierra, delgada y rocosa"), ("manto", "capa de roca caliente bajo la corteza"), ("litosfera", "corteza más la parte rígida superior del manto"), ("placa tectónica", "gran trozo de la litosfera que se mueve"), ("astenosfera", "parte del manto que fluye lentamente bajo la litosfera")],
  worked=[
      ("Ordenar las capas", "Ordena de afuera hacia adentro: manto, núcleo interno, corteza, núcleo externo.", ["La más externa es la corteza.", "Sigue el manto.", "Luego el núcleo externo y al centro el núcleo interno."], "Corteza, manto, núcleo externo, núcleo interno"),
      ("Distancia recorrida", "Una placa avanza 4 cm por año. ¿Cuántos cm avanza en 1.000 años?", ["Multiplico la velocidad por el tiempo.", "4 × 1.000 = 4.000."], "4.000 cm, o 40 m"),
  ],
  mistakes=[
      ("Pensar que las placas flotan sobre el núcleo líquido.", "Se mueven sobre la astenosfera, que es parte del manto.", "El manto está entre la corteza y los núcleos."),
      ("Decir que las placas se mueven rápido.", "Se mueven unos pocos centímetros por año.", "Compara con el crecimiento de las uñas."),
  ],
  rec=[
      ("¿Cuál es la capa más externa de la Tierra: la corteza o el manto?", "La corteza", "Es delgada y rocosa."),
      ("¿Qué capa es líquida: el núcleo externo o el núcleo interno?", "El núcleo externo", "El interno es sólido."),
      ("¿Las placas se mueven unos pocos centímetros por año o varios kilómetros por año?", "Unos pocos centímetros por año", "Es un movimiento muy lento."),
  ],
  und=[
      ("¿Qué forman la corteza y la parte rígida superior del manto? A) La litosfera; B) El núcleo.", "A", "Se rompe en placas."),
      ("¿Sobre qué capa se mueven las placas? A) La astenosfera; B) El núcleo interno.", "A", "Es una parte blanda del manto."),
      ("¿Qué mueve a las placas, en parte? A) Corrientes de convección del manto por el calor interno; B) La luz del Sol.", "A", "El calor interior genera corrientes en el manto."),
  ],
  app=[
      arith("Una placa avanza 5 cm por año. ¿Cuántos cm avanza en 2.000.000 de años?", "5*2000000", "Velocidad × tiempo."),
      arith("Con 1 km = 100.000 cm, ¿cuántos km son 10.000.000 cm?", "10000000//100000", "Se divide en 100.000."),
      ("Ordena las capas de afuera hacia adentro: manto, corteza, núcleo interno, núcleo externo. ¿Cuál queda en tercer lugar?", "El núcleo externo", "Corteza, manto, núcleo externo, núcleo interno."),
  ],
  rea=[
      ("Un compañero dice: «Las placas flotan sobre el núcleo». Corrígelo en una frase.", "Se mueven sobre la astenosfera, una parte del manto", "El núcleo está mucho más profundo."),
      ("¿Por qué no sentimos el movimiento de las placas en la vida diaria? Responde en una frase.", "Porque es de pocos centímetros por año", "Es muy lento."),
  ],
  cha=[
      ("Dos placas se alejan, cada una a 4 cm por año. ¿Cuántos cm se separan entre sí en un año?", "8", "4 + 4 = 8 cm."),
      ("Con esa separación de 8 cm por año, ¿cuántos km se separan en 1.000.000 de años? (1 km = 100.000 cm)", "80", "8 × 1.000.000 ÷ 100.000 = 80 km."),
  ],
  context=[("Dato de ejemplo. Una placa avanza 3 cm por año. ¿Cuántos cm avanza en 100 años?", "300", "3 × 100 = 300 cm.")],
  selfcheck=[("¿Cuáles son las capas de la Tierra?", "Corteza, manto, núcleo externo y núcleo interno", "Van de afuera hacia adentro."), ("¿Qué es la litosfera?", "La corteza más la parte rígida superior del manto", "Está dividida en placas."), ("¿Qué velocidad tienen las placas?", "Unos pocos cm por año", "Es muy lenta.")],
  open_task=task("Dibuja un corte de la Tierra con las cuatro capas rotuladas y marca la litosfera y la astenosfera. Escribe debajo cuántos km se mueve una placa que avanza 6 cm por año en 1.000.000 de años (1 km = 100.000 cm).", "Corte con corteza, manto, núcleo externo y núcleo interno; litosfera arriba y astenosfera bajo ella. Cálculo: 6 × 1.000.000 ÷ 100.000 = 60 km.", ["cuatro capas rotuladas", "litosfera y astenosfera ubicadas", "cálculo de 60 km"], ["dibujo y cálculo"], ["poner el manto fuera de la corteza", "olvidar la conversión a km"], "Pregunta por qué se llama astenosfera a la zona blanda."),
  reinforce="Escribe el orden de las capas de la Tierra de afuera hacia adentro.",
  extend="Explica por qué un movimiento de pocos cm por año puede cambiar el mapa en millones de años.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Los mapas son tablas de ejemplo escritas en los ejercicios.",
  use="Aprenderé a leer patrones de sismos y volcanes en mapas y a relacionarlos con los bordes de las placas. Sirve para saber dónde ocurre más actividad geológica.",
  prior=["Sé qué son las placas tectónicas.", "Sé leer tablas de datos."],
  explain=[
      "Un sismo es una vibración de la corteza. Se origina en un punto profundo llamado foco, y el punto de la superficie justo encima es el epicentro. Un volcán es una abertura por donde sale material desde el interior. Si se marcan en un mapa del mundo los sismos y volcanes, no aparecen al azar: forman franjas.",
  "La más conocida es el Cinturón de Fuego del Pacífico, que rodea el océano Pacífico e incluye la costa de Chile. Otras franjas siguen las dorsales oceánicas, como la del océano Atlántico, y el cinturón que cruza el sur de Europa y Asia, del Mediterráneo al Himalaya. Esas franjas coinciden con los bordes de las placas, donde se tocan, se separan o se rozan. En el interior de las placas hay pocos. Hay excepciones: algunos volcanes, como los de Hawái, están lejos de los bordes y se explican por puntos calientes, zonas fijas del manto desde donde sube magma.",
      "En las zonas donde una placa se hunde bajo otra, los focos se hacen más profundos a medida que se avanza desde la fosa hacia el continente. Leer un mapa significa buscar el patrón: dónde hay más puntos, qué los une y qué hay en común con los bordes de las placas. Un patrón es una pista, y debe contrastarse con más datos.",
  ],
  vocab=[("sismo", "vibración de la corteza terrestre"), ("foco", "punto profundo donde se origina un sismo"), ("epicentro", "punto de la superficie sobre el foco"), ("Cinturón de Fuego", "franja de sismos y volcanes que rodea el océano Pacífico"), ("punto caliente", "zona fija del manto desde donde sube magma, lejos de un borde de placas"), ("dorsal oceánica", "cadena de montañas submarinas donde se separan placas")],
  worked=[
      ("Leer un mapa de conteos", "Datos de ejemplo de 600 sismos: 450 en bordes convergentes, 100 en dorsales y 50 en el interior de placas. ¿Qué porcentaje ocurre en bordes convergentes?", ["450 de 600.", "450 × 100 ÷ 600 = 75."], "75 %"),
      ("Profundidad del foco", "Focos de ejemplo: a 100 km de la fosa, 20 km de profundidad; a 300 km, 110 km. ¿Cómo cambia la profundidad hacia el continente?", ["Comparo 20 y 110.", "Aumenta con la distancia."], "Aumenta"),
  ],
  mistakes=[
      ("Creer que los sismos y volcanes ocurren al azar.", "Se concentran en franjas, en los bordes de las placas.", "Busca el patrón en el mapa."),
      ("Confundir foco con epicentro.", "El foco es el punto profundo; el epicentro, el punto en la superficie.", "El epicentro está sobre el foco."),
  ],
  rec=[
      ("¿Dónde se origina un sismo: en el foco o en el epicentro?", "En el foco", "El epicentro está en la superficie."),
      ("¿Los sismos y volcanes forman franjas en el mapa: sí o no?", "Sí", "Coinciden con los bordes de las placas."),
      ("¿La costa de Chile está dentro del Cinturón de Fuego: sí o no?", "Sí", "Rodea el océano Pacífico."),
  ],
  und=[
      ("¿Qué patrón muestran los volcanes en un mapa? A) Forman franjas que coinciden con los bordes de las placas; B) Están repartidos por igual.", "A", "No están repartidos al azar."),
      ("¿Dónde hay menos sismos? A) En el interior de las placas; B) En los bordes de las placas.", "A", "En los bordes se concentra la actividad."),
      ("¿Qué punto está justo sobre el foco, en la superficie?", "El epicentro", "Es el punto de la superficie sobre el foco."),
  ],
  app=[
      arith("Datos de ejemplo: de 400 volcanes, 300 están en el Cinturón de Fuego. ¿Qué porcentaje es?", "300*100//400", "Parte entre total × 100."),
      arith("De 400 volcanes, 300 están en el Cinturón de Fuego. ¿Cuántos están fuera de él?", "400-300", "Se resta."),
      ("Focos de ejemplo: 20 km a 100 km de la fosa, 60 km a 200 km, 110 km a 300 km. Si el patrón sigue, ¿a qué profundidad estará un foco a 400 km de la fosa? A) Cerca de 150 km; B) Cerca de 10 km.", "A", "Aumenta unos 45 km cada 100 km."),
  ],
  rea=[
      ("En un mapa, los volcanes de Chile, Perú y Ecuador forman una línea a lo largo de la cordillera de los Andes, cerca de la costa del Pacífico. ¿Qué explica el patrón? Responde en una frase.", "Se ubican sobre un borde de placas donde una placa se hunde bajo otra", "Siguen el borde convergente."),
      ("Un mapa de ejemplo muestra un volcán en el centro de una placa, lejos de los bordes. ¿El modelo de bordes lo explica por completo? Responde Sí o No.", "No", "Existen excepciones como los puntos calientes."),
  ],
  cha=[
      ("Un mapa de ejemplo tiene 120 sismos: 90 en una franja angosta y 30 repartidos. ¿Qué porcentaje está en la franja?", "75", "90 ÷ 120 × 100 = 75 %."),
      ("Un compañero dice: «Si hay un volcán, hay un borde de placa cerca siempre». ¿Qué cuidado hay que tener? A) Hay excepciones como los puntos calientes; B) Los volcanes nunca están en bordes.", "A", "La generalización tiene excepciones."),
  ],
  context=[("Dato de ejemplo. Un mapa registra 50 sismos en una zona de borde y 10 en el interior de una placa. ¿Cuántos sismos más hay en el borde?", "40", "50 − 10 = 40.")],
  selfcheck=[("¿Qué es el epicentro?", "El punto de la superficie sobre el foco", "El foco es el origen profundo."), ("¿Dónde se concentran sismos y volcanes?", "En franjas, en los bordes de las placas", "Es el patrón."), ("¿Qué es el Cinturón de Fuego?", "Una franja de sismos y volcanes alrededor del océano Pacífico", "La costa de Chile forma parte de esa franja.")],
  open_task=task("Con estos datos de ejemplo de 5 volcanes (A: costa de Chile; B: costa de Japón; C: centro de Australia; D: dorsal del Atlántico; E: costa de Perú), indica cuáles están en el Cinturón de Fuego o en una dorsal y cuál no sigue el patrón. Explica en una frase por qué se agrupan.", "A, B y E están en el Cinturón de Fuego; D está en una dorsal; C no sigue el patrón del borde. Se agrupan porque los bordes de placas concentran la actividad.", ["clasifica los cinco", "identifica el que no sigue el patrón", "explica con bordes de placas"], ["lista y una frase"], ["poner C en el Cinturón de Fuego", "decir que es azar"], "Pregunta qué dato nuevo ayudaría a explicar el caso C."),
  reinforce="Escribe dónde se concentran los sismos en un mapa del mundo.",
  extend="Explica por qué un patrón en un mapa no es lo mismo que una explicación.")

L(OA9, 3,
  materials="Este cuaderno y lápiz. Los esquemas son descripciones escritas en los ejercicios.",
  use="Aprenderé los tres tipos de límites de placas (convergente, divergente y transformante) y qué fenómenos produce cada uno. Sirve para explicar cordilleras, dorsales y fallas.",
  prior=["Sé qué son las placas y cómo se mueven.", "Sé que los sismos y volcanes se concentran en los bordes."],
  explain=[
      "Los límites de placas pueden ser de tres tipos según su movimiento. En un límite convergente, las placas se acercan. Si una es oceánica y otra continental, la oceánica, más densa, se hunde bajo la continental (subducción). Esto forma una fosa oceánica, cordilleras con volcanes y sismos intensos. Si chocan dos continentes, se levantan cordilleras, como el Himalaya.",
      "En un límite divergente, las placas se separan. Sube magma que forma nueva corteza, como en la dorsal del Atlántico, y hay volcanes y sismos poco profundos. En un límite transformante, las placas se deslizan de lado, una al lado de la otra. No se forma ni se destruye corteza, pero se producen sismos importantes, como en la falla de San Andrés, en California.",
      "Para identificar un límite se mira cómo se mueven las placas. Si se acercan, es convergente; si se alejan, divergente; si se deslizan lateralmente, transformante. Un esquema simplifica y no muestra todos los detalles, como la velocidad o la profundidad.",
  ],
  vocab=[("límite convergente", "borde donde dos placas se acercan"), ("límite divergente", "borde donde dos placas se separan"), ("límite transformante", "borde donde dos placas se deslizan de lado"), ("subducción", "hundimiento de una placa bajo otra"), ("fosa oceánica", "depresión profunda del fondo marino donde una placa se hunde")],
  worked=[
      ("Tipo de límite", "Dos placas se acercan y una se hunde bajo la otra. ¿Qué tipo de límite es y qué se forma?", ["Se acercan: convergente.", "La que se hunde produce una fosa y volcanes."], "Convergente; se forman fosa, cordillera y volcanes"),
      ("Separación de placas", "Dos placas se separan y sube magma. ¿Qué tipo de límite es y qué se forma?", ["Se alejan: divergente.", "El magma forma nueva corteza."], "Divergente; se forma nueva corteza"),
  ],
  mistakes=[
      ("Pensar que en un límite transformante se forman volcanes.", "Las placas se deslizan de lado y no se funde ni se forma corteza.", "Asocia los transformantes a sismos."),
      ("Decir que la placa continental se hunde bajo la oceánica.", "La oceánica es más densa y se hunde.", "Recuerda: la más densa se hunde."),
  ],
  rec=[
      ("Si dos placas se alejan, ¿el límite es convergente o divergente?", "Divergente", "Las placas se separan."),
      ("¿Qué placa se hunde en la subducción: la oceánica o la continental?", "La oceánica", "Es más densa."),
      ("¿Se forma nueva corteza en un límite divergente: sí o no?", "Sí", "Sube magma y se enfría."),
  ],
  und=[
      ("La falla de San Andrés es un ejemplo de límite: A) transformante; B) divergente.", "A", "Las placas se deslizan de lado."),
      ("¿Qué se forma cuando chocan dos placas continentales? A) Cordilleras como el Himalaya; B) Una dorsal.", "A", "Ninguna se hunde fácilmente y la corteza se levanta."),
      ("¿Qué fenómeno es típico de un límite transformante? A) Sismos importantes; B) Volcanes.", "A", "No hay magma que suba."),
  ],
  app=[
      ("Cinco descripciones: (1) las placas se acercan, (2) las placas se alejan, (3) las placas se deslizan de lado, (4) una placa se hunde, (5) sube magma entre las placas. ¿Cuántas corresponden a un límite convergente?", "2", "La 1 y la 4."),
      ("Un esquema muestra una dorsal oceánica y rocas más antiguas lejos de ella. ¿Qué tipo de límite es?", "Divergente", "Se separa y se forma corteza nueva."),
      ("Un esquema muestra una costa con una fosa y volcanes tierra adentro. ¿Qué tipo de límite es?", "Convergente", "Hay subducción de una placa."),
  ],
  rea=[
      ("Explica por qué en un límite transformante no se forman volcanes ni se destruye corteza.", "Porque las placas solo se deslizan de lado, sin que haya subducción ni magma que suba", "El movimiento es lateral."),
      ("¿Por qué la placa oceánica es la que se hunde cuando choca con una continental?", "Porque es más densa", "Su densidad es mayor."),
  ],
  cha=[
      ("Caso 1: la placa Pacífica y la Norteamericana se deslizan de lado en California. Caso 2: África y Sudamérica se separan en el Atlántico. ¿Cuál caso es un límite divergente? Escribe 1 o 2.", "2", "En el caso 2 las placas se separan."),
      ("Un esquema simple no muestra la velocidad de las placas. ¿Es un límite del esquema? Responde Sí o No.", "Sí", "Un esquema simplifica y omite detalles."),
  ],
  context=[("Dato de ejemplo. Una dorsal separa dos placas 5 cm por año. ¿Cuántos cm se separan en 40 años?", "200", "5 × 40 = 200 cm.")],
  selfcheck=[("¿Cuáles son los tres tipos de límites?", "Convergente, divergente y transformante", "Dependen del movimiento."), ("¿Qué es la subducción?", "El hundimiento de una placa bajo otra", "Ocurre en límites convergentes."), ("¿Qué produce un límite divergente?", "Nueva corteza, volcanes y sismos poco profundos", "Las placas se separan.")],
  open_task=task("Dibuja tres esquemas de bordes, con flechas que muestren el movimiento de las placas: uno convergente (placa oceánica hundiéndose), uno divergente y uno transformante. Rotula el tipo y escribe un fenómeno propio de cada uno.", "Convergente: fosa, cordillera, volcanes. Divergente: dorsal y corteza nueva. Transformante: sismos por el deslizamiento lateral.", ["tres esquemas con flechas", "tipo rotulado", "un fenómeno por tipo"], ["tres dibujos rotulados"], ["flechas al revés", "poner volcanes en el transformante"], "Pregunta qué esquema explica la cordillera de los Andes."),
  reinforce="Escribe qué hacen las placas en cada tipo de límite.",
  extend="Explica por qué la corteza oceánica es más joven cerca de una dorsal.")

L(OA9, 4,
  materials="Este cuaderno y lápiz. Los datos son aproximados y se escriben en los ejercicios.",
  use="Aprenderé cómo la tectónica de placas explica la actividad geológica de Chile, como un caso más del modelo y no como una excepción. Sirve para entender por qué hay volcanes, cordillera y terremotos en nuestro país.",
  prior=["Sé qué es un límite convergente.", "Sé que el Cinturón de Fuego rodea el Pacífico."],
  explain=[
      "Chile está sobre un límite convergente. La placa de Nazca, oceánica, se hunde bajo la placa Sudamericana, continental, a unos 6 a 7 cm por año. Esa subducción forma la fosa Perú-Chile, de más de 8.000 m de profundidad, a lo largo de la costa. La cordillera de los Andes y los volcanes se levantan sobre la placa que queda arriba.",
      "Este proceso produce terremotos muy grandes. El terremoto de Valdivia de 1960, de magnitud 9,5, es el mayor registrado en el mundo, y el de 2010, de magnitud 8,8, afectó la zona del Maule. Los sismos grandes cerca de la costa pueden generar tsunamis. En la costa, si un sismo es tan fuerte que cuesta mantenerse en pie, se evacúa de inmediato a una zona alta, sin esperar una alerta, y se avisa a los adultos cercanos. En el sur, donde se juntan las placas de Nazca, Sudamericana y Antártica, hay un punto triple frente a la península de Taitao.",
      "Chile no es una excepción. Japón también está sobre un límite convergente, donde una placa oceánica se hunde bajo otra, y comparte volcanes y sismos grandes. Entender el modelo permite preparar a la población: mapas de riesgo, rutas de evacuación y construcciones sismorresistentes.",
  ],
  vocab=[("placa de Nazca", "placa oceánica que se hunde bajo Sudamérica"), ("fosa Perú-Chile", "depresión profunda del fondo marino frente a la costa"), ("magnitud", "medida de la energía liberada en un sismo"), ("tsunami", "serie de olas generadas por un movimiento del fondo marino"), ("punto triple", "lugar donde se juntan tres placas")],
  worked=[
      ("Qué placa se hunde", "En Chile, ¿cuál placa se hunde y bajo cuál?", ["La placa de Nazca es oceánica y más densa.", "Se hunde bajo la placa Sudamericana."], "La placa de Nazca bajo la placa Sudamericana"),
      ("Tiempo de desplazamiento", "La placa de Nazca avanza 5 cm por año. ¿Cuántos años tarda en avanzar 50 km (5.000.000 cm)?", ["Divido la distancia entre la velocidad.", "5.000.000 ÷ 5 = 1.000.000."], "1.000.000 de años"),
  ],
  mistakes=[
      ("Decir que Chile tiene sismos porque es un país especial.", "Tiene sismos por estar sobre un límite convergente, como otros países.", "Explica con el modelo."),
      ("Pensar que un terremoto se puede predecir con exactitud.", "Se conocen las zonas de riesgo, pero no el día exacto.", "Por eso se debe estar siempre preparado."),
  ],
  rec=[
      ("¿Qué placa se hunde bajo Sudamérica: la de Nazca o la Antártica?", "La de Nazca", "Es oceánica y más densa."),
      ("¿La cordillera de los Andes se formó por subducción: sí o no?", "Sí", "Es consecuencia de la convergencia."),
      ("¿Chile es la única zona del mundo con subducción: verdadero o falso?", "Falso", "También ocurre en Japón y otros lugares."),
  ],
  und=[
      ("¿Por qué hay volcanes en Chile? A) La subducción de la placa de Nazca produce magma; B) Porque está cerca del Ecuador.", "A", "La placa que se hunde produce magma."),
      ("El terremoto de Valdivia de 1960 tuvo magnitud 9,5. ¿Qué lo hace especial? A) Es el mayor registrado en el mundo; B) Es el único de Chile.", "A", "Ningún sismo registrado liberó tanta energía."),
      ("¿Qué país también está sobre un límite convergente, como Chile? A) Japón; B) Australia, en el centro de su placa.", "A", "Una placa oceánica se hunde bajo otra."),
  ],
  app=[
      arith("La placa de Nazca avanza 6 cm por año. ¿Cuántos cm avanza en 100 años?", "6*100", "Velocidad × tiempo."),
      arith("El fondo de la fosa frente a la costa está a 8.000 m bajo el nivel del mar y una cima de los Andes a 6.000 m sobre él. ¿Cuántos metros separan el fondo de la fosa de esa cima?", "8000+6000", "Se suman la profundidad y la altura."),
      ("La magnitud 9,5 de 1960 y la 8,8 de 2010, ¿cuál es mayor?", "La de 1960", "9,5 es mayor que 8,8."),
  ],
  rea=[
      ("Un compañero dice: «Japón no se parece a Chile». Usa el modelo para responder en una frase.", "Ambos están sobre límites convergentes con subducción", "Eso explica sus volcanes y sismos."),
      ("¿Por qué se construyen edificios sismorresistentes en Chile? Responde en una frase.", "Porque hay terremotos grandes y se debe proteger a las personas", "El modelo permite anticipar el riesgo."),
  ],
  cha=[
      ("Un tsunami se genera por un sismo grande en el fondo del mar. Si hay un sismo fuerte y estás en la costa, ¿qué conviene hacer? A) Evacuar de inmediato hacia zonas altas por las rutas oficiales y avisar a los adultos cercanos; B) Ir a la playa a mirar.", "A", "La evacuación rápida protege."),
      ("El punto triple de Chile se encuentra frente a Taitao. ¿Cuántas placas se juntan en él?", "3", "Nazca, Sudamericana y Antártica."),
  ],
  context=[("Dato de ejemplo. La placa de Nazca avanza 7 cm por año. ¿Cuántos cm avanza en 30 años?", "210", "7 × 30 = 210 cm.")],
  selfcheck=[("¿Qué placa se hunde bajo la Sudamericana?", "La de Nazca", "Es la subducción de Chile."), ("¿Por qué hay volcanes y sismos en Chile?", "Por la subducción de la placa de Nazca", "El modelo los explica."), ("¿Chile es una excepción?", "No; otros lugares como Japón tienen el mismo tipo de límite", "El modelo es general.")],
  open_task=task("Escribe una explicación de cinco frases sobre por qué Chile tiene volcanes, cordillera y terremotos. Usa las palabras: Nazca, Sudamericana, subducción, fosa, y menciona otro país con un límite del mismo tipo.", "La placa de Nazca se hunde bajo la Sudamericana (subducción) y forma la fosa frente a la costa. La subducción produce magma y volcanes, levanta los Andes y genera terremotos. Japón tiene un límite de tipo similar.", ["usa las cuatro palabras", "explica volcanes, cordillera y sismos", "incluye otro país"], ["texto de cinco frases"], ["decir que Chile es una excepción", "no usar el modelo"], "Pregunta qué medida de seguridad se desprende de la explicación."),
  reinforce="Escribe qué pasa con la placa de Nazca en la costa de Chile.",
  extend="Explica por qué conocer el modelo ayuda a prepararse pero no permite predecir el día de un terremoto.")

L(OA9, 5,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé qué evidencias apoyan la deriva continental y la tectónica de placas y a evaluar el modelo con datos. Sirve para entender cómo una idea científica gana apoyo.",
  prior=["Sé qué son los tres tipos de límites.", "Sé contrastar una explicación con datos."],
  explain=[
      "En 1912 Alfred Wegener propuso la deriva continental: los continentes estuvieron unidos en un supercontinente, Pangea, y luego se separaron. Sus evidencias fueron el encaje de las costas de Sudamérica y África, fósiles iguales a ambos lados del Atlántico (como el reptil Mesosaurus), rocas y cordilleras que se continúan y huellas de glaciares en continentes que hoy están en zonas cálidas.",
      "Su idea no se aceptó entonces, porque no explicaba qué movía a los continentes. En el siglo XX se midió el fondo marino y se encontró que la corteza oceánica es más joven cerca de las dorsales y más antigua lejos de ellas, y que las rocas guardan franjas magnéticas simétricas a cada lado. Con esto se formuló la tectónica de placas: los continentes se mueven porque forman parte de placas que se desplazan.",
      "Hoy el movimiento se mide con GPS, en centímetros por año. El modelo es muy sólido, pero tiene límites: explica la mayoría de los volcanes y sismos, pero no todos; los volcanes del interior de una placa, como los de Hawái, se explican con puntos calientes, y no se puede predecir el día de un terremoto.",
  ],
  vocab=[("deriva continental", "idea de que los continentes se mueven"), ("Pangea", "supercontinente en que estuvieron unidos los continentes"), ("evidencia", "dato que apoya una explicación"), ("punto caliente", "zona fija del manto que produce volcanes en el interior de una placa"), ("GPS", "sistema que mide posiciones con satélites")],
  worked=[
      ("Clasificar evidencias", "Fósiles del mismo reptil en Sudamérica y en África, ¿qué idea apoyan?", ["El reptil no cruzaba el océano.", "Los continentes estuvieron unidos."], "Apoyan la deriva continental"),
      ("Calcular una velocidad", "Rocas de 8 millones de años están a 400 km de una dorsal. ¿Cuántos km por millón de años se alejaron?", ["400 ÷ 8 = 50.", "Son 50 km por millón de años."], "50 km por millón de años"),
  ],
  mistakes=[
      ("Pensar que Wegener no tenía evidencias.", "Tenía varias; le faltaba explicar el mecanismo.", "Distingue evidencia de mecanismo."),
      ("Decir que el modelo explica absolutamente todo.", "Tiene límites, como los puntos calientes.", "Declara qué no explica."),
  ],
  rec=[
      ("¿Quién propuso la deriva continental en 1912: Wegener o Darwin?", "Wegener", "Propuso que los continentes estuvieron unidos."),
      ("¿Cómo se llama el supercontinente: Pangea o Gondwana?", "Pangea", "Reunía todos los continentes."),
      ("¿La corteza oceánica es más antigua cerca o lejos de la dorsal?", "Lejos", "Se forma en la dorsal y se aleja."),
  ],
  und=[
      ("¿Qué evidencia apoya que Sudamérica y África estuvieron unidas? A) El encaje de sus costas; B) El color del mar.", "A", "Las costas encajan como un rompecabezas."),
      ("¿Por qué no se aceptó al principio la idea de Wegener? A) No explicaba qué movía los continentes; B) No había continentes.", "A", "Le faltaba un mecanismo."),
      ("¿Qué mide hoy el GPS en las placas? A) Su movimiento de unos centímetros por año; B) Su color.", "A", "Mide cuánto se desplazan."),
  ],
  app=[
      arith("Rocas de 10 millones de años están a 500 km de una dorsal. ¿Cuántos km por millón de años se alejaron?", "500//10", "Distancia ÷ tiempo."),
      arith("Con esa velocidad de 50 km por millón de años, ¿cuántos km se alejan en 30 millones de años?", "50*30", "Velocidad × tiempo."),
      ("Evidencias: (1) encaje de costas, (2) fósiles iguales en continentes separados, (3) edades de la corteza oceánica, (4) color de las nubes. ¿Cuántas son evidencias de la deriva y de las placas?", "3", "Las tres primeras."),
  ],
  rea=[
      ("Edades de ejemplo: 0 millones de años en la dorsal, 4 a 200 km, 8 a 400 km. ¿Qué patrón muestran?", "A mayor distancia de la dorsal, mayor edad", "Apoya que se forma corteza nueva en la dorsal."),
      ("Un volcán en Hawái está lejos de los bordes de placas. ¿Contradice por completo el modelo? Responde Sí o No y explica.", "No; se explica con un punto caliente", "El modelo tiene un complemento para esos casos."),
  ],
  cha=[
      ("Juzga: «Como el modelo es tan sólido, podemos predecir el día de un terremoto». ¿Es correcto?", "No", "El modelo explica dónde, pero no el día exacto."),
      ("Escribe un límite del modelo de la tectónica de placas.", "No explica los volcanes de puntos calientes ni permite predecir el día de un terremoto", "Todo modelo tiene límites."),
  ],
  context=[("Dato de ejemplo. Se hallaron fósiles del mismo reptil de agua dulce: 45 en Sudamérica y 38 en África. ¿Cuántos fósiles hay en total?", "83", "45 + 38 = 83; que estén a ambos lados del Atlántico apoya que los continentes estuvieron unidos.")],
  selfcheck=[("¿Qué propuso Wegener?", "Que los continentes estuvieron unidos y se separaron", "Es la deriva continental."), ("¿Qué evidencia apoya el movimiento de los continentes?", "Encaje de costas, fósiles iguales y edades de la corteza oceánica", "Son evidencias independientes."), ("¿Qué límite tiene el modelo?", "No explica todos los volcanes ni predice el día de un terremoto", "El modelo tiene excepciones.")],
  open_task=task("Escribe una carta corta de Wegener (inventada) a otro científico con tres evidencias a favor de la deriva continental, y una respuesta del científico que mencione la evidencia moderna del fondo marino y un límite del modelo.", "Wegener: costas que encajan, fósiles iguales, rocas que se continúan. Respuesta: la corteza oceánica más joven cerca de las dorsales y el GPS apoyan la idea; el modelo no predice el día de un terremoto.", ["tres evidencias", "evidencia moderna", "un límite del modelo"], ["dos textos breves"], ["decir que Wegener inventó la tectónica de placas completa", "no mencionar límites"], "Pregunta qué evidencia le parece más convincente y por qué."),
  reinforce="Escribe dos evidencias de la deriva continental.",
  extend="Explica por qué el GPS es una evidencia más fuerte que el encaje de costas.")

# ---------------------------------------------------------------- OA 10
L(OA10, 1,
  materials="Este cuaderno y lápiz. Las medidas están escritas en los ejercicios. No se hace ninguna actividad con fuego ni con calor.",
  use="Aprenderé la diferencia entre magma, lava, gases y ceniza y las partes de un volcán. Sirve para describir una erupción con palabras precisas.",
  prior=["Sé qué es un volcán y dónde se ubican.", "Sé que las rocas pueden fundirse a alta temperatura."],
  explain=[
      "El magma es roca fundida que está bajo la superficie, en la cámara magmática. Tiene gases disueltos. Cuando sale por el cráter y llega a la superficie se llama lava; su temperatura suele estar entre 700 y 1.200 °C. Al enfriarse, la lava se convierte en roca volcánica.",
      "Con el magma salen también gases como vapor de agua, dióxido de carbono y dióxido de azufre. Si un magma sale con fuerza, se rompe en fragmentos llamados piroclastos. La ceniza son fragmentos menores a 2 mm; el lapilli mide entre 2 y 64 mm y las bombas volcánicas son más grandes. La ceniza puede viajar por el viento a grandes distancias.",
      "El magma sube por la chimenea desde la cámara magmática hasta el cráter. Estas palabras no son sinónimos: lava es magma que ya salió, ceniza es un fragmento sólido y los gases son un componente aparte. Para describir una erupción conviene decir qué sale: lava, gases o ceniza.",
  ],
  vocab=[("magma", "roca fundida bajo la superficie"), ("lava", "magma que sale a la superficie"), ("ceniza volcánica", "fragmentos de roca menores a 2 mm"), ("piroclastos", "fragmentos sólidos lanzados por un volcán"), ("cámara magmática", "depósito de magma bajo el volcán")],
  worked=[
      ("Magma o lava", "Roca fundida dentro de la cámara bajo el volcán, ¿es magma o lava?", ["Está bajo la superficie.", "Aún no salió."], "Magma"),
      ("Clasificar fragmentos", "Un fragmento mide 1 mm, otro 30 mm y otro 100 mm. ¿Cuál es ceniza, cuál lapilli y cuál bomba?", ["Menos de 2 mm: ceniza.", "De 2 a 64 mm: lapilli.", "Más de 64 mm: bomba."], "1 mm ceniza; 30 mm lapilli; 100 mm bomba"),
  ],
  mistakes=[
      ("Llamar lava al magma que está bajo tierra.", "Se llama lava solo cuando llega a la superficie.", "Si está bajo tierra, es magma."),
      ("Pensar que la ceniza volcánica es lo mismo que la ceniza de una fogata.", "La ceniza volcánica son fragmentos de roca y vidrio.", "No es el residuo de quemar algo."),
  ],
  rec=[
      ("¿Cómo se llama el magma que sale a la superficie: lava o ceniza?", "Lava", "Es magma que ya salió."),
      ("¿La cámara magmática está bajo o sobre el volcán?", "Bajo el volcán", "Almacena el magma."),
      ("¿La ceniza volcánica es un gas o fragmentos sólidos?", "Fragmentos sólidos", "Son trocitos de roca."),
  ],
  und=[
      ("¿Qué gas volcánico es el más abundante? A) Vapor de agua; B) Oxígeno puro.", "A", "Es el componente principal de los gases volcánicos."),
      ("¿Cuál es la diferencia entre magma y lava? A) El magma está bajo la superficie y la lava ya salió; B) La lava es más fría que el magma bajo tierra siempre.", "A", "La ubicación es la clave."),
      ("¿Qué tamaño tiene la ceniza? A) Menor a 2 mm; B) Mayor a 64 mm.", "A", "Mayor a 64 mm son bombas."),
  ],
  app=[
      arith("Un volcán lanza ceniza a 5 km de altura y otra erupción llega a 12 km. ¿Cuántos km más alto llega la segunda?", "12-5", "Se resta."),
      ("Fragmentos de 0,5 mm, 10 mm, 70 mm y 1,5 mm. ¿Cuántos son ceniza (menor a 2 mm)?", "2", "Son 0,5 mm y 1,5 mm."),
      ("Un volcán emite vapor de agua y dióxido de azufre. ¿Qué componente es?", "Gases", "Ambos son gases volcánicos."),
  ],
  rea=[
      ("Un compañero dice: «Lava y magma son lo mismo». Corrígelo en una frase.", "El magma está bajo la superficie y la lava es el magma que salió", "La diferencia es dónde está."),
      ("¿Por qué la ceniza puede viajar lejos? Responde en una frase.", "Porque son fragmentos muy livianos que el viento puede llevar", "Su tamaño es muy pequeño."),
  ],
  cha=[
      ("Una lava sale a 1.100 °C y se enfría hasta 100 °C. ¿Cuántos °C bajó?", "1.000", "1.100 − 100 = 1.000 °C."),
      ("Ordena de menor a mayor tamaño de fragmento: bomba, ceniza, lapilli. ¿Cuál queda en el medio?", "Lapilli", "Ceniza, lapilli, bomba."),
  ],
  context=[("Dato de ejemplo. Un volcán emitió 3 columnas de ceniza en un día: 2 km, 4 km y 6 km de altura. ¿Cuántos km sumaron las tres alturas?", "12", "2 + 4 + 6 = 12 km.")],
  selfcheck=[("¿Qué es el magma?", "Roca fundida bajo la superficie", "Contiene gases disueltos."), ("¿Qué es la lava?", "Magma que sale a la superficie", "Se enfría y forma roca."), ("¿Qué es la ceniza volcánica?", "Fragmentos de roca menores a 2 mm", "Son piroclastos pequeños.")],
  open_task=task("Dibuja un volcán en corte y rotula: cámara magmática, chimenea, cráter, magma, lava, gases y ceniza. Escribe una frase que explique la diferencia entre magma y lava.", "Corte con cámara en la base, chimenea, cráter, magma dentro, lava en la ladera, gases y ceniza saliendo. El magma está bajo la superficie y la lava salió.", ["siete rótulos", "ubicación correcta", "frase de diferencia"], ["dibujo rotulado"], ["poner la lava en la cámara", "llamar ceniza a los gases"], "Pregunta qué sale primero en una erupción explosiva."),
  reinforce="Escribe tres cosas que salen de un volcán.",
  extend="Explica por qué la ceniza volcánica es distinta de la ceniza de una fogata.")

L(OA10, 2,
  materials="Este cuaderno y lápiz. Opcional: miel y agua para comparar cómo fluyen en un plato inclinado, sin calor y con supervisión.",
  use="Aprenderé cómo las propiedades del magma, como su viscosidad y su contenido de gases, determinan si una erupción es tranquila o explosiva. Sirve para anticipar el tipo de peligro de un volcán.",
  prior=["Sé qué son magma, lava, gases y ceniza.", "Sé que los gases pueden quedar atrapados en un líquido."],
  explain=[
      "La viscosidad es la resistencia de un líquido a fluir. La miel es más viscosa que el agua. El magma también varía: un magma con mucha sílice es viscoso y fluye con dificultad, y uno con poca sílice es fluido. La sílice es un componente de las rocas.",
      "El magma lleva gases disueltos, igual que una bebida gaseosa cerrada. Si es fluido, los gases escapan con facilidad y la erupción es efusiva: la lava corre por las laderas como un río, como en Hawái. Si es viscoso, los gases quedan atrapados, la presión aumenta y al final el magma se rompe con fuerza: la erupción es explosiva, con ceniza, piroclastos y nubes de gas caliente.",
      "Por eso el estilo de erupción depende de la viscosidad y de los gases. Los volcanes de los Andes de Chile tienen frecuentemente magmas viscosos y erupciones explosivas, como la del volcán Calbuco en 2015, aunque algunos tienen erupciones más tranquilas. El estilo es una guía de riesgo, no una regla exacta.",
  ],
  vocab=[("viscosidad", "resistencia de un líquido a fluir"), ("sílice", "componente de las rocas que hace más viscoso al magma"), ("erupción efusiva", "erupción con salida tranquila de lava"), ("erupción explosiva", "erupción con ceniza y fragmentos lanzados con fuerza"), ("gas disuelto", "gas mezclado dentro del magma")],
  worked=[
      ("Predecir el estilo", "Un magma es viscoso y tiene muchos gases. ¿La erupción será efusiva o explosiva?", ["Es viscoso: los gases quedan atrapados.", "La presión aumenta y el magma se rompe."], "Explosiva"),
      ("Analogía con líquidos", "Datos de ejemplo: la miel tarda 20 s en bajar por un plato inclinado y el agua 2 s. ¿Cuál es más viscosa y cuántas veces más lenta es?", ["La miel tarda más.", "20 ÷ 2 = 10."], "La miel; 10 veces más lenta"),
  ],
  mistakes=[
      ("Pensar que todas las erupciones son explosivas.", "Si el magma es fluido, la erupción es tranquila.", "Revisa la viscosidad."),
      ("Creer que el color de la lava dice el estilo.", "El estilo depende de la viscosidad y los gases.", "Mide la viscosidad, no el color."),
  ],
  rec=[
      ("¿Cuál es más viscosa: la miel o el agua?", "La miel", "Fluye con más dificultad."),
      ("Un magma fluido, ¿produce erupción efusiva o explosiva?", "Efusiva", "Los gases escapan con facilidad."),
      ("Un magma viscoso con gases, ¿produce erupción tranquila o explosiva?", "Explosiva", "Los gases quedan atrapados."),
  ],
  und=[
      ("¿Por qué un magma viscoso puede causar una explosión? A) Atrapa gases y sube la presión; B) Pierde su temperatura de inmediato.", "A", "La presión aumenta hasta romperlo."),
      ("¿Qué componente aumenta la viscosidad del magma? A) La sílice; B) El agua del mar.", "A", "La sílice forma redes que dificultan el flujo."),
      ("¿Con qué se parece una bebida gaseosa agitada y abierta de golpe? A) Con una erupción explosiva; B) Con una erupción efusiva.", "A", "El gas sale de golpe."),
  ],
  app=[
      arith("Datos de ejemplo: la miel tarda 30 s y el agua 3 s en bajar por una rampa. ¿Cuántas veces más lenta es la miel?", "30//3", "Se divide."),
      arith("Una lava fluida avanza 4 km en 2 horas. ¿Cuántos km por hora avanza?", "4//2", "Distancia ÷ tiempo."),
      ("Un volcán produce lava fluida que baja por la ladera sin explotar. ¿Su erupción es efusiva o explosiva?", "Efusiva", "No hay explosión."),
  ],
  rea=[
      ("Un compañero dice: «Si el magma tiene muchos gases, siempre habrá explosión». ¿Qué falta considerar?", "La viscosidad: si es fluido, los gases escapan", "Importa la combinación."),
      ("Explica por qué en Hawái la lava corre como un río.", "Porque el magma es fluido y los gases escapan sin explotar", "Es una erupción efusiva."),
  ],
  cha=[
      ("Dos volcanes de ejemplo: A tiene magma fluido y pocos gases; B tiene magma viscoso y muchos gases. ¿Cuál es más peligroso por explosión?", "B", "Atrapa los gases."),
      ("Predice: si a un magma viscoso se le agrega más gas, ¿la erupción será más o menos explosiva?", "Más explosiva", "Aumenta la presión."),
  ],
  context=[("Dato de ejemplo. Un plato inclinado muestra que una crema espesa tarda 40 s y el agua 4 s en bajar. ¿Cuántos segundos más tarda la crema?", "36", "40 − 4 = 36 s.")],
  selfcheck=[("¿Qué es la viscosidad?", "La resistencia de un líquido a fluir", "La miel es muy viscosa."), ("¿Qué tipo de erupción produce un magma fluido?", "Efusiva", "Los gases escapan."), ("¿Qué tipo produce un magma viscoso con gases?", "Explosiva", "Los gases quedan atrapados.")],
  open_task=task("Completa una tabla con dos volcanes inventados: Volcán Norte (magma fluido, pocos gases) y Volcán Sur (magma viscoso, muchos gases). Escribe para cada uno el estilo de erupción, qué sale y qué peligro principal puede traer.", "Norte: efusiva; sale lava en ríos; peligro: avance de la lava. Sur: explosiva; salen ceniza y piroclastos; peligro: ceniza y flujos de gas caliente.", ["dos filas", "estilo correcto", "peligro asociado"], ["tabla de dos filas"], ["invertir los estilos", "no nombrar el peligro"], "Pregunta qué propiedad del magma decidió el estilo."),
  reinforce="Escribe una diferencia entre una erupción efusiva y una explosiva.",
  extend="Explica por qué la viscosidad y los gases se consideran juntos.")

L(OA10, 3,
  materials="Este cuaderno y lápiz. Los casos son descripciones; los datos son aproximados y están escritos en los ejercicios.",
  use="Aprenderé qué efectos tienen las erupciones en la naturaleza y en la sociedad, positivos y negativos. Sirve para entender por qué se vigilan los volcanes.",
  prior=["Sé qué sale de un volcán.", "Sé que hay erupciones efusivas y explosivas."],
  explain=[
      "Una erupción afecta la naturaleza. La ceniza puede cubrir el suelo y, con el tiempo, lo fertiliza con minerales. La lava forma nuevas rocas y terrenos. Cuando la erupción derrite nieve o hielo, se forman lahares, flujos rápidos de barro y rocas que bajan por los ríos. La ceniza en el aire puede ensuciar ríos y dañar plantas.",
      "También afecta a la sociedad. La ceniza dificulta la respiración y la visión, puede acumularse sobre los techos y hacer que colapsen, y obliga a cerrar aeropuertos. En 2011, la erupción del complejo Puyehue-Cordón Caulle afectó vuelos en el sur de Sudamérica. En 2008, la erupción del volcán Chaitén obligó a evacuar al pueblo. Las comunidades de la zona deben cambiar sus actividades por un tiempo.",
      "No todo es negativo: los suelos volcánicos son fértiles, algunos volcanes entregan energía geotérmica y atraen turismo. Para analizar los efectos se separan los naturales y los sociales, y los positivos y los negativos, y se recuerda que los efectos dependen de la distancia y de la preparación de la gente.",
  ],
  vocab=[("lahar", "flujo rápido de barro y rocas que baja por un cauce"), ("evacuar", "sacar a las personas de una zona peligrosa"), ("suelo fértil", "suelo con minerales que ayudan a crecer a las plantas"), ("energía geotérmica", "energía que viene del calor interior de la Tierra"), ("efecto", "consecuencia de un hecho")],
  worked=[
      ("Efecto natural o social", "Clasifica: (1) un lahar baja por un río, (2) un aeropuerto cierra por ceniza, (3) el suelo se fertiliza con minerales.", ["El lahar y el suelo son cambios de la naturaleza.", "El cierre afecta a las personas."], "1 natural; 2 social; 3 natural"),
      ("Positivo o negativo", "¿La ceniza que fertiliza el suelo es un efecto positivo o negativo?", ["Los minerales de la ceniza se incorporan al suelo.", "Ayuda a crecer a las plantas con el tiempo."], "Positivo"),
  ],
  mistakes=[
      ("Pensar que los volcanes solo traen daños.", "También dan suelos fértiles, energía y turismo.", "Evalúa efectos positivos y negativos."),
      ("Creer que el riesgo es igual en todas partes.", "Depende de la distancia y la preparación.", "Revisa los mapas de peligro."),
  ],
  rec=[
      ("¿Un lahar es un flujo de barro y rocas o de gas?", "De barro y rocas", "Baja por un cauce."),
      ("¿La ceniza acumulada en un techo puede hacerlo colapsar: sí o no?", "Sí", "La ceniza acumulada pesa mucho."),
      ("¿La ceniza con minerales puede fertilizar el suelo: verdadero o falso?", "Verdadero", "A largo plazo."),
  ],
  und=[
      ("¿Cuál es un efecto social de una erupción? A) Cierre de un aeropuerto; B) Formación de nuevas rocas.", "A", "Afecta a las personas."),
      ("¿Cuál es un efecto natural? A) Un lahar; B) La evacuación de un pueblo.", "A", "Es un cambio del entorno."),
      ("¿Qué puede hacer la ceniza en el aire? A) Dificultar la respiración; B) No tiene ningún efecto en las personas.", "A", "Irrita las vías respiratorias."),
  ],
  app=[
      ("Cinco efectos: lahar, cierre de aeropuerto, suelo fértil, evacuación de un pueblo, formación de roca nueva. ¿Cuántos son efectos sociales?", "2", "Son el cierre y la evacuación."),
      arith("Una erupción obliga a evacuar a 1.200 personas y a otras 800 a prepararse. ¿Cuántas personas están involucradas en total?", "1200+800", "Se suman."),
      ("Un pueblo está a 10 km de un volcán y otro a 60 km. ¿Cuál tiene mayor riesgo por lahares y flujos? A) El de 10 km; B) El de 60 km.", "A", "Está más cerca."),
  ],
  rea=[
      ("Explica por qué un mismo volcán puede producir efectos positivos y negativos.", "Destruye por un tiempo, pero entrega suelos fértiles y energía", "Los efectos cambian con el tiempo."),
      ("¿Por qué se cierran aeropuertos cuando hay ceniza en el aire?", "Porque la ceniza daña los motores y reduce la visibilidad", "Es un riesgo para los aviones."),
  ],
  cha=[
      ("Una comunidad pierde 30 hectáreas de cultivo por ceniza y gana 12 hectáreas de suelo fértil con el tiempo. ¿Cuántas hectáreas netas pierde?", "18", "30 − 12 = 18."),
      ("Haz una recomendación: ¿qué conviene hacer ante una nube de ceniza? A) Usar mascarilla y quedarse en un lugar cerrado; B) Salir a mirarla de cerca.", "A", "Disminuye el contacto con la ceniza."),
  ],
  context=[("Dato de ejemplo. Una escuela cierra 4 días por ceniza y debe recuperar las clases en 2 semanas de 5 días de clases. ¿Cuántos días de clases le sobran para otras actividades?", "6", "10 − 4 = 6.")],
  selfcheck=[("¿Cuál es un efecto natural de una erupción?", "Lahares, nuevas rocas o suelos fértiles", "Cambian el entorno."), ("¿Cuál es un efecto social?", "Evacuación, cierre de aeropuertos o daños en techos", "Afectan a las personas."), ("¿Por qué no todo es negativo?", "Porque también hay suelos fértiles, energía geotérmica y turismo", "Hay efectos positivos.")],
  open_task=task("Elabora una tabla de cuatro columnas (efecto, natural o social, positivo o negativo, distancia desde el volcán donde importa más) con cuatro efectos: lahar, ceniza en techos, suelo fértil, cierre de aeropuerto.", "Lahar: natural, negativo, cerca de ríos. Ceniza en techos: social, negativo, zonas con caída de ceniza. Suelo fértil: natural, positivo, zonas con ceniza. Cierre: social, negativo, lejos si el viento lleva ceniza.", ["cuatro filas", "clasificación correcta", "distancia indicada"], ["tabla"], ["decir que todos son negativos", "olvidar la distancia"], "Pregunta qué efecto positivo prefiere y por qué."),
  reinforce="Escribe dos efectos naturales y dos sociales de una erupción.",
  extend="Explica por qué la preparación de una comunidad reduce los daños.")

L(OA10, 4,
  materials="Este cuaderno y lápiz. El mapa y los datos son ejemplos escritos en los ejercicios; para información real hay que consultar los sitios oficiales vigentes.",
  use="Aprenderé a tomar decisiones de prevención usando mapas de peligro y alertas oficiales. Sirve para saber qué hacer antes, durante y después de una erupción.",
  prior=["Sé qué efectos tiene una erupción.", "Sé evaluar fuentes confiables."],
  explain=[
      "En Chile, el Servicio Nacional de Geología y Minería (Sernageomin) vigila los volcanes y publica mapas de peligros y alertas técnicas. El Servicio Nacional de Prevención y Respuesta ante Desastres (Senapred) coordina la preparación y las evacuaciones. Un mapa de peligros divide el entorno del volcán en zonas según el tipo de fenómeno (flujos de lava, flujos piroclásticos, lahares o caída de ceniza) y la distancia.",
      "La alerta técnica de un volcán usa cuatro colores (verde, amarillo, naranja y rojo) que van desde un volcán estable (verde) hasta una erupción inminente o en curso (rojo). Siempre se debe comprobar la definición vigente en el sitio oficial. Una alerta no se interpreta sola: se combina con el mapa y con las instrucciones de las autoridades.",
      "Una buena decisión de prevención incluye conocer la zona de la casa en el mapa, preparar un kit de emergencia con agua, linterna, mascarillas y documentos, definir un punto de encuentro y una ruta, y seguir las indicaciones oficiales. Durante una caída de ceniza se usa mascarilla y se cubren las fuentes de agua; no se cruzan quebradas ni cauces de ríos. Si una alerta o una erupción te sorprende lejos de tu familia, avisa de inmediato a una persona adulta de confianza y sigue sus instrucciones.",
  ],
  vocab=[("mapa de peligros", "mapa que divide un lugar en zonas según el tipo y el nivel de peligro"), ("alerta técnica", "color que indica el estado de actividad de un volcán"), ("Sernageomin", "servicio que vigila los volcanes de Chile"), ("Senapred", "servicio que coordina la prevención y respuesta ante desastres"), ("kit de emergencia", "conjunto de elementos listos para una evacuación")],
  worked=[
      ("Leer un mapa de peligros", "Mapa de ejemplo: zona 1 (0 a 5 km): flujos de lava y piroclásticos; zona 2 (5 a 15 km): lahares por ríos; zona 3 (15 a 40 km): caída de ceniza. Una casa está a 8 km, junto a un río. ¿Qué peligro principal enfrenta?", ["8 km está en la zona 2.", "La casa está junto a un río.", "El peligro de la zona 2 son los lahares."], "Lahares"),
      ("Decidir qué hacer", "Con una alerta naranja, una familia ve que su casa está en la zona 2. ¿Qué conviene hacer?", ["La alerta indica riesgo creciente.", "Debe seguir las instrucciones oficiales y preparar la evacuación."], "Preparar el kit y seguir las instrucciones oficiales; evacuar si lo indican"),
  ],
  mistakes=[
      ("Basarse en rumores de redes sociales.", "Pueden ser falsos o desactualizados.", "Usa solo fuentes oficiales."),
      ("Cruzar un río seco durante una alerta.", "Los lahares bajan por esos cauces.", "No cruces cauces ni quebradas."),
  ],
  rec=[
      ("¿Quién vigila los volcanes de Chile: Sernageomin o un diario?", "Sernageomin", "Es el servicio oficial."),
      ("¿Cuántos colores usa la alerta técnica de un volcán: cuatro o dos?", "Cuatro", "Verde, amarillo, naranja y rojo."),
      ("¿Se debe cruzar un cauce de río durante una alerta: sí o no?", "No", "Por ahí bajan los lahares."),
  ],
  und=[
      ("¿Qué muestra un mapa de peligros? A) Zonas según el tipo de fenómeno y la distancia; B) El color de las lavas.", "A", "Ayuda a decidir qué hacer."),
      ("¿Qué se debe incluir en un kit de emergencia? A) Agua, linterna y mascarillas; B) Un videojuego y golosinas, porque la espera será larga.", "A", "Sirven para una evacuación."),
      ("¿Dónde se informa una persona sobre una erupción? A) En los sitios oficiales de Sernageomin y Senapred; B) En un mensaje reenviado sin fuente.", "A", "Son fuentes oficiales."),
  ],
  app=[
      ("Mapa de ejemplo (zona 1: 0 a 5 km; zona 2: 5 a 15 km; zona 3: 15 a 40 km). Una escuela está a 20 km. ¿En qué zona está?", "Zona 3", "20 km está entre 15 y 40 km."),
      ("Con ese mapa, una casa está a 3 km. ¿Cuál es su peligro principal?", "Flujos de lava y piroclásticos", "Está en la zona 1."),
      arith("Una familia debe recorrer 12 km para llegar a una zona segura a pie a 4 km por hora. ¿Cuántas horas tarda?", "12//4", "Distancia ÷ velocidad."),
  ],
  rea=[
      ("Alguien dice: «Con alerta amarilla ya no hay que hacer nada». ¿Qué responderías?", "Hay que informarse y prepararse porque pueden cambiar las condiciones", "La alerta amarilla indica cambios."),
      ("¿Por qué se recomienda un punto de encuentro y una ruta definidos de antemano?", "Porque permite actuar rápido y mantener juntas a las personas", "En una evacuación no hay tiempo para improvisar."),
  ],
  cha=[
      ("Un pueblo ficticio tiene 9 familias en zona 1, 15 en zona 2 y 26 en zona 3. ¿Cuántas están en zonas 1 y 2, que son las más cercanas?", "24", "9 + 15 = 24."),
      ("Redacta tres acciones para tu hogar ante una erupción, usando mapas, kit y fuentes oficiales.", "Revisar mi zona en el mapa, preparar un kit y seguir las instrucciones de las fuentes oficiales", "Resume la prevención."),
  ],
  context=[("Dato de ejemplo. Un simulacro tarda 18 minutos en evacuar a 360 personas. Si el ritmo es parejo, ¿cuántas personas se evacuan por minuto?", "20", "360 ÷ 18 = 20.")],
  selfcheck=[("¿Qué hace Sernageomin?", "Vigila los volcanes y publica mapas y alertas", "Es una fuente oficial."), ("¿Qué incluye un kit de emergencia?", "Agua, linterna, mascarillas y documentos", "Sirve para evacuar."), ("¿Qué no se debe hacer durante una alerta?", "Cruzar cauces o confiar en rumores", "Pueden ser peligrosos.")],
  open_task=task("Con el mapa de ejemplo de la clase (zona 1: 0 a 5 km; zona 2: 5 a 15 km; zona 3: 15 a 40 km), imagina que tu casa está a 12 km junto a un río. Escribe un plan de 5 pasos: qué zona es, qué peligro principal, qué llevar en el kit, a dónde ir y qué fuente consultar.", "Zona 2; lahares; kit con agua, linterna, mascarillas y documentos; ir a una zona más alta o más lejana por una ruta definida; consultar las fuentes oficiales.", ["cinco pasos", "usa el mapa", "fuente oficial"], ["plan escrito"], ["no mencionar el río", "usar rumores"], "Pregunta qué cambiaría si la alerta fuera roja."),
  reinforce="Escribe tres elementos de un kit de emergencia.",
  extend="Explica por qué un mapa de peligros y una alerta técnica se usan juntos.")

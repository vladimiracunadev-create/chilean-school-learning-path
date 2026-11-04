"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 16 (astronomía en Chile, instrumentos y lectura de radiación)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _x(items):
    return [ex(*i) if isinstance(i, tuple) else i for i in items]


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": w[0], "problem": w[1], "steps": w[2], "answer": w[3]} for w in worked],
        mistakes=[{"wrong": m[0], "why": m[1], "fix": m[2]} for m in mistakes],
        tiers={"recovery": _x(rec), "understand": _x(und), "apply": _x(app), "reason": _x(rea), "challenge": _x(cha)},
        context=_x(context), selfcheck=_x(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


OA = "CN1M OA 16"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Los datos de los sitios de observación son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé por qué el norte de Chile es tan bueno para observar el cielo y cómo comparar sitios con datos. Sirve para entender por qué hay tantos observatorios en nuestro país.",
  prior=["Sé que la atmósfera está formada por gases y vapor de agua.", "Sé que la luz artificial puede dificultar ver las estrellas."],
  explain=[
      "Para observar los astros desde la Tierra se necesita un cielo despejado, aire seco, una atmósfera estable y mucha oscuridad. Las nubes tapan los astros; el vapor de agua absorbe parte de la radiación infrarroja y de radio; la turbulencia, que es el movimiento del aire, hace que las estrellas titilen y las imágenes se vean borrosas; y la luz artificial de las ciudades ilumina el cielo y oculta los astros débiles.",
      "El norte de Chile reúne estas condiciones. El desierto de Atacama es uno de los lugares más secos del planeta, con muchas noches despejadas al año. Hay lugares a gran altitud, entre 2.000 y 5.000 m, donde hay menos atmósfera sobre el telescopio. La Corriente de Humboldt enfría el aire cercano a la costa y mantiene las nubes bajas por debajo de los cerros. Además, hay pocas ciudades grandes, así que hay poca luz artificial.",
      "Desde el hemisferio sur se ven partes del cielo que no se ven desde el norte, como el centro de la Vía Láctea y las Nubes de Magallanes. Para elegir un sitio se comparan datos: noches despejadas por año, humedad, altitud y oscuridad. Una pregunta investigable es: «¿En qué sitio hay más noches despejadas por año en un registro de cinco años?».",
  ],
  vocab=[("turbulencia atmosférica", "movimiento del aire que hace titilar las estrellas y desenfoca las imágenes"), ("humedad", "cantidad de vapor de agua en el aire"), ("altitud", "altura sobre el nivel del mar"), ("cielo despejado", "cielo sin nubes"), ("contaminación lumínica", "exceso de luz artificial que dificulta ver el cielo"), ("desierto de Atacama", "desierto del norte de Chile, muy seco")],
  worked=[
      ("Elegir un sitio", "Sitio A: 120 noches despejadas al año, humedad alta, 100 m de altitud. Sitio B: 310 noches despejadas, humedad baja, 2.600 m. Datos de ejemplo. ¿Cuál es mejor para un observatorio?", ["Comparo las noches despejadas: B tiene más.", "Comparo humedad y altitud: B es más seco y más alto.", "B reúne más condiciones favorables."], "El sitio B"),
      ("Noches sin observación", "Un sitio tiene 310 noches despejadas al año. ¿Cuántas noches no son despejadas?", ["Un año tiene 365 noches.", "Calculo 365 − 310."], "55 noches"),
  ],
  mistakes=[
      ("Creer que a más calor siempre es mejor observar.", "Lo importante es que el aire sea seco, estable y el cielo esté despejado.", "Revisa humedad, nubes y turbulencia."),
      ("Pensar que Chile es bueno solo por estar en el hemisferio sur.", "Además del hemisferio, importan el clima seco, la altitud y la oscuridad.", "Menciona al menos tres condiciones."),
  ],
  rec=[
      ("¿Qué desierto del norte de Chile es famoso por sus cielos?", "El desierto de Atacama", "Es muy seco y tiene muchas noches despejadas."),
      ("Verdadero o falso: el vapor de agua ayuda a observar en infrarrojo y radio.", "Falso", "El vapor de agua absorbe parte de esas radiaciones."),
      ("Un observatorio a más altitud tiene ______ (más o menos) atmósfera sobre él.", "Menos", "Hay menos aire entre el telescopio y el espacio."),
  ],
  und=[
      ("¿Por qué es una ventaja la humedad baja? A) Hay menos vapor de agua que absorba radiación infrarroja y de radio B) Hay más nubes bajas", "A", "El vapor de agua absorbe parte de esas radiaciones."),
      ("¿Por qué ayuda que haya pocas ciudades grandes cerca?", "Hay menos luz artificial", "El cielo se mantiene oscuro."),
      ("¿Qué es la turbulencia atmosférica?", "El movimiento del aire que hace titilar las estrellas", "Desenfoca las imágenes del telescopio."),
  ],
  app=[
      arith("Un sitio tiene 300 noches despejadas al año. ¿Cuántas noches despejadas tiene en 5 años, suponiendo que cada año es igual?", "300*5", "Se multiplica el número de noches por los años.", " noches"),
      ("Datos de ejemplo. Sitio A: 120 noches despejadas, humedad 60 %, 100 m. Sitio B: 310 noches, humedad 10 %, 2.600 m. Sitio C: 200 noches, humedad 30 %, 1.000 m. ¿Cuál es mejor para un telescopio?", "El sitio B", "Tiene más noches despejadas, es el más seco y el más alto."),
      arith("El observatorio de Paranal está a unos 2.600 m de altitud y ALMA a unos 5.000 m. ¿Cuántos metros más alto está ALMA?", "5000-2600", "Se resta la altitud menor a la mayor.", " m"),
  ],
  rea=[
      ("Un compañero dice que Chile es bueno para observar solo por estar cerca del ecuador. ¿Cuál es la respuesta correcta? A) Lo principal es el clima seco y despejado, la altitud y la oscuridad B) Lo principal es la cercanía al ecuador", "A", "Esas condiciones determinan la calidad de las imágenes."),
      ("¿Qué pregunta es investigable? A) ¿En qué sitio hay más noches despejadas en un registro de cinco años? B) ¿Cuál es el sitio más hermoso?", "A", "Se contesta contando noches despejadas."),
  ],
  cha=[
      ("Un pueblo agrega muchas luces nuevas que apuntan hacia el cielo cerca de un observatorio. ¿Qué efecto tendrá en las observaciones?", "Aumentará la luz del cielo y dificultará ver astros débiles", "La contaminación lumínica reduce el contraste."),
      arith("Un sitio de ejemplo tiene 310 noches despejadas y otro 155. ¿Cuántas veces más noches despejadas tiene el primero?", "310/155", "Se divide el mayor número de noches por el menor.", " veces"),
  ],
  context=[ex("Quieres fotografiar la Vía Láctea. ¿Qué lugar elegirías? A) Un campo oscuro del norte de Chile, lejos de ciudades B) El centro de una ciudad grande", "A", "Hay mucha menos luz artificial y el cielo es más oscuro.")],
  selfcheck=[("Nombra tres condiciones que debe tener un buen sitio astronómico.", "Cielo despejado, aire seco y oscuridad", "Son condiciones para observar con claridad."), ("¿Qué ayuda a mantener bajas las nubes en la costa norte de Chile?", "La Corriente de Humboldt", "Enfría el aire cercano al mar."), ("¿Qué ve el hemisferio sur que no ve el norte?", "Las Nubes de Magallanes", "Son dos galaxias vecinas del cielo austral.")],
  open_task=task("Cuatro sitios de ejemplo. P: 80 noches despejadas, humedad 70 %, 50 m, mucha luz artificial. Q: 300 noches, humedad 10 %, 2.400 m, casi sin luz artificial. R: 220 noches, humedad 25 %, 1.500 m, poca luz artificial. S: 320 noches, humedad 5 %, 5.000 m, sin luz artificial. Ordénalos de mejor a peor para un telescopio de luz visible y justifica con tres criterios. Escribe una pregunta investigable que compare dos sitios.", "Orden: S, Q, R, P. Se usan noches despejadas, humedad, altitud y luz artificial. Pregunta: «¿En cuál de los sitios Q y S hay más noches despejadas en un registro de cinco años?».", ["orden correcto", "tres criterios con datos", "pregunta con algo medible"], ["lista ordenada y justificación"], ["ordenar por altitud solamente", "formular una pregunta de opinión"], "Pregunta qué dato adicional necesitarías para un telescopio de radio."),
  reinforce="Escribe tres ventajas del norte de Chile para la astronomía.",
  extend="Explica por qué un observatorio de luz visible se beneficia más de la oscuridad que uno de radio.")

L(OA, 2,
  materials="Este cuaderno, lápiz y calculadora. Los datos de los instrumentos son aproximados y están escritos en los ejercicios.",
  use="Aprenderé cómo funcionan los telescopios ópticos y los radiotelescopios y qué instrumentos hay en Chile. Sirve para entender qué observa cada tipo de instrumento.",
  prior=["Sé qué hacen las lentes y los espejos con la luz.", "Sé que la luz es una onda electromagnética."],
  explain=[
      "Un telescopio óptico recoge luz visible. El refractor usa una lente como objetivo; el reflector usa un espejo cóncavo. Los telescopios grandes son reflectores porque un espejo se puede apoyar por detrás y construir muy grande. Mientras mayor es el diámetro del espejo, más luz recoge: la cantidad de luz crece con el cuadrado del diámetro. Un espejo de 8 m recoge 16 veces más luz que uno de 2 m, porque (8 ÷ 2) × (8 ÷ 2) = 16, y permite ver objetos más débiles y lejanos.",
      "Un radiotelescopio es una antena parabólica que capta ondas de radio de los astros. Varias antenas pueden trabajar juntas y comportarse como un solo telescopio mayor con más detalle. ALMA, en el llano de Chajnantor, a unos 5.000 m de altitud, tiene 66 antenas: 54 de 12 m y 12 de 7 m. Observa ondas milimétricas, emitidas por gas frío y polvo donde nacen estrellas y planetas.",
      "En Chile hay muchos otros instrumentos: el Very Large Telescope en Paranal, con cuatro espejos de unos 8 m; el telescopio Gemini Sur y el observatorio Vera C. Rubin, en Cerro Pachón; y el Extremely Large Telescope, en construcción en Cerro Armazones, con un espejo de unos 39 m. Los telescopios espaciales, como Hubble y James Webb, orbitan fuera de la atmósfera y observan radiaciones que no llegan al suelo. Los instrumentos de apoyo incluyen cámaras digitales y espectrógrafos, que separan la luz en sus colores.",
  ],
  vocab=[("refractor", "telescopio que usa una lente como objetivo"), ("reflector", "telescopio que usa un espejo cóncavo como espejo principal"), ("radiotelescopio", "antena parabólica que capta ondas de radio de los astros"), ("diámetro del espejo", "ancho del espejo principal; determina cuánta luz recoge"), ("espectrógrafo", "instrumento que separa la luz en sus colores"), ("telescopio espacial", "telescopio que orbita fuera de la atmósfera")],
  worked=[
      ("Luz recogida", "¿Cuántas veces más luz recoge un espejo de 6 m que uno de 3 m?", ["La luz crece con el cuadrado del diámetro.", "Calculo (6 ÷ 3) × (6 ÷ 3) = 2 × 2."], "4 veces"),
      ("Elegir el instrumento", "Quieres detectar ondas de radio de una nube de gas. ¿Qué instrumento usas?", ["Las ondas de radio no se captan con lentes ni espejos ópticos.", "Se usa una antena."], "Un radiotelescopio"),
  ],
  mistakes=[
      ("Pensar que un telescopio grande solo sirve para ver más aumentado.", "Su ventaja principal es recoger más luz y ver detalles más finos.", "Compara la luz recogida y el detalle, no solo el aumento."),
      ("Creer que los radiotelescopios captan luz visible.", "Captan ondas de radio, que tienen mayor longitud de onda.", "Pregunta qué parte del espectro capta el instrumento."),
  ],
  rec=[
      ("¿Qué tipo de telescopio usa un espejo principal cóncavo?", "El reflector", "El espejo recoge y enfoca la luz."),
      ("¿Qué captan los radiotelescopios?", "Ondas de radio", "No captan luz visible."),
      ("Verdadero o falso: los telescopios espaciales observan fuera de la atmósfera.", "Verdadero", "Así evitan que el aire absorba parte de la radiación."),
  ],
  und=[
      ("Si duplicas el diámetro del espejo de un telescopio, la luz que recoge: A) se multiplica por 4 B) se duplica", "A", "La luz depende del área, es decir, del cuadrado del diámetro."),
      ("¿Para qué se unen las 66 antenas de ALMA?", "Para funcionar como un telescopio mayor y ver más detalle", "Combinan sus señales."),
      ("¿Qué hace un espectrógrafo?", "Separa la luz en sus colores", "Permite estudiar los espectros."),
  ],
  app=[
      arith("¿Cuántas veces más luz recoge un espejo de 8 m que uno de 2 m?", "(8/2)*(8/2)", "La luz crece con el cuadrado del diámetro.", " veces"),
      arith("¿Cuántas veces más luz recoge un telescopio de 10 m que uno de 5 m?", "(10/5)*(10/5)", "La luz crece con el cuadrado del diámetro.", " veces"),
      ("ALMA se ubica a unos 5.000 m de altitud. ¿Qué ventaja tiene?", "Hay menos atmósfera y menos vapor de agua sobre las antenas", "Menos vapor de agua absorbe menos ondas milimétricas."),
  ],
  rea=[
      ("Un compañero dice que los telescopios grandes solo sirven para ver más grande. ¿Qué respuesta es correcta? A) Su ventaja principal es recoger más luz para ver objetos débiles y con más detalle B) Su única ventaja es agrandar la imagen", "A", "El diámetro del espejo determina la luz recogida."),
      ("¿Cuál da más detalle: una antena de radio aislada de 12 m o 66 antenas combinadas?", "Las 66 antenas combinadas", "Combinadas, equivalen a un telescopio mucho mayor."),
  ],
  cha=[
      arith("Un telescopio de 8 m (8.000 mm) y la pupila de un ojo humano de 8 mm. ¿Cuántas veces más luz recoge el telescopio?", "(8000/8)*(8000/8)", "Se divide un diámetro por el otro y se eleva al cuadrado.", " veces"),
      ("¿Por qué un telescopio espacial puede observar radiaciones que no llegan al suelo?", "Porque está fuera de la atmósfera, que las absorbe", "En el espacio no hay aire que las detenga."),
  ],
  context=[ex("En un observatorio, la cúpula está cerrada durante el día. ¿Por qué? A) Para proteger los instrumentos de la luz solar intensa y del calor B) Para que las estrellas no vean el telescopio", "A", "La luz del Sol y el calor podrían dañar los espejos y los sensores.")],
  selfcheck=[("¿Qué diferencia hay entre refractor y reflector?", "El refractor usa una lente y el reflector un espejo", "Ambos recogen y enfocan la luz."), ("¿Cuántas antenas tiene ALMA?", "66", "54 de 12 m y 12 de 7 m."), ("¿Qué telescopio se construye en Cerro Armazones?", "El Extremely Large Telescope", "Tendrá un espejo de unos 39 m.")],
  open_task=task("Completa una tabla con cinco instrumentos: Very Large Telescope (Paranal), ALMA (Chajnantor), Gemini Sur (Cerro Pachón), Hubble (espacio) y Extremely Large Telescope (Cerro Armazones). Para cada uno, escribe si usa espejos o antenas, qué radiación observa y dónde está. Calcula cuántas veces más luz recoge un espejo de 8 m que uno de 4 m y explica por qué se prefieren espejos grandes.", "VLT: espejos de 8 m, luz visible e infrarroja, Paranal. ALMA: antenas, ondas milimétricas, Chajnantor. Gemini Sur: espejo de 8 m, Cerro Pachón. Hubble: espejo, en el espacio. ELT: espejo de 39 m en construcción. Un espejo de 8 m recoge (8 ÷ 4) × (8 ÷ 4) = 4 veces más luz que uno de 4 m, así que ve objetos más débiles.", ["cinco filas completas", "cálculo de 4 veces", "explica con la luz recogida"], ["tabla y cálculo"], ["confundir ALMA con un telescopio óptico", "calcular la luz con el diámetro sin elevar al cuadrado"], "Pregunta qué instrumento usarías para ver rayos X."),
  reinforce="Escribe una diferencia entre un telescopio óptico y un radiotelescopio.",
  extend="Explica por qué ALMA combina las señales de sus antenas.")

L(OA, 3,
  materials="Este cuaderno, lápiz y calculadora. Los datos son aproximados y están escritos en los ejercicios.",
  use="Aprenderé qué información entrega cada tipo de radiación de los astros y por qué algunos telescopios van al espacio. Sirve para elegir el instrumento adecuado.",
  prior=["Sé el orden del espectro electromagnético.", "Sé que la atmósfera absorbe algunas radiaciones."],
  explain=[
      "Los astros emiten radiación en todo el espectro electromagnético, y cada banda muestra un proceso distinto. Las ondas de radio y milimétricas revelan gas frío y polvo donde nacen estrellas. El infrarrojo muestra objetos tibios, como el polvo alrededor de estrellas jóvenes y planetas. La luz visible muestra estrellas y gas caliente. El ultravioleta, los rayos X y los rayos gamma revelan procesos muy energéticos, como explosiones y materia que cae hacia agujeros negros.",
      "La atmósfera deja pasar casi toda la luz visible y las ondas de radio, deja pasar solo una parte del infrarrojo y bloquea casi todo el ultravioleta, los rayos X y los rayos gamma. El vapor de agua absorbe infrarrojo y ondas milimétricas, por eso los telescopios para esas bandas se ponen en lugares secos y altos, como ALMA. Para ultravioleta, X y gamma se necesitan telescopios espaciales.",
      "Un mismo objeto se ve distinto en cada banda. Una galaxia puede mostrar estrellas en luz visible, polvo tibio en infrarrojo y nubes de gas en ondas de radio. Por eso los astrónomos combinan imágenes de distintos instrumentos para entender un objeto completo.",
  ],
  vocab=[("banda del espectro", "rango de longitudes de onda de un tipo de radiación"), ("infrarrojo", "radiación emitida por objetos tibios, con longitud de onda mayor que el rojo"), ("rayos X", "radiación muy energética emitida por gas muy caliente o materia cayendo a un agujero negro"), ("ventana atmosférica", "rango de radiaciones que pasan a través de la atmósfera"), ("telescopio espacial", "telescopio ubicado fuera de la atmósfera"), ("agujero negro", "región donde la gravedad es tan intensa que ni la luz escapa")],
  worked=[
      ("Elegir la banda", "Quieres observar el polvo tibio alrededor de una estrella joven. ¿Qué banda conviene?", ["Los objetos tibios emiten sobre todo infrarrojo.", "Esa es la banda que muestra el polvo tibio."], "Infrarroja"),
      ("Por qué ir al espacio", "¿Por qué los rayos X de un astro no se pueden observar desde el desierto de Atacama?", ["La atmósfera absorbe los rayos X.", "Por eso hay que salir de la atmósfera."], "Porque la atmósfera los absorbe"),
  ],
  mistakes=[
      ("Creer que un astro que no se ve a simple vista no emite nada.", "Puede emitir radiaciones que el ojo no percibe, como radio o rayos X.", "Pregunta en qué banda se observa."),
      ("Pensar que todos los telescopios pueden observar todas las bandas desde el suelo.", "La atmósfera bloquea varias bandas.", "Revisa qué radiaciones llegan al suelo."),
  ],
  rec=[
      ("Verdadero o falso: la atmósfera bloquea los rayos X.", "Verdadero", "Por eso se usan telescopios espaciales."),
      ("¿Qué ondas capta ALMA?", "Ondas milimétricas", "Las emite el gas frío y el polvo."),
      ("¿Para qué se envían telescopios al espacio?", "Para observar radiaciones que la atmósfera bloquea", "Así se ven rayos X, gamma y ultravioleta."),
  ],
  und=[
      ("Las ondas de radio y milimétricas revelan principalmente: A) gas frío y polvo donde nacen estrellas B) explosiones de estrellas", "A", "Esa materia fría emite en esas bandas."),
      ("¿Por qué ALMA está en un lugar seco y alto? A) El vapor de agua absorbe ondas milimétricas B) Allí hay más luz artificial", "A", "Menos vapor significa más señal."),
      ("Un astro emite rayos X intensos. ¿Qué tipo de proceso hay allí? A) Muy energético B) Muy frío", "A", "Los rayos X indican gas muy caliente o procesos violentos."),
  ],
  app=[
      ("Tres equipos quieren observar un mismo astro: uno en ondas de radio, otro en luz visible y otro en rayos X. ¿Cuántos de los tres equipos necesitan un telescopio espacial?", "1", "Solo los rayos X son bloqueados por la atmósfera; la radio y la luz visible llegan al suelo."),
      arith("El telescopio Hubble orbita a unos 540 km de altura (dato aproximado) y se considera que la atmósfera útil termina cerca de los 100 km. ¿Cuántos kilómetros por encima de ese límite orbita?", "540-100", "Se resta el límite de la atmósfera a la altura de la órbita.", " km"),
      ("Quieres estudiar la materia que cae hacia un agujero negro y emite rayos X. ¿Dónde pones el telescopio? A) En el espacio B) En el desierto", "A", "La atmósfera absorbe los rayos X."),
  ],
  rea=[
      ("Alguien dice que si un astro no se ve con el ojo, no emite nada. ¿Qué respuesta es correcta? A) Puede emitir radiaciones que el ojo no ve, como radio o infrarrojo B) Es correcto, solo la luz visible existe", "A", "El ojo es sensible a una pequeña parte del espectro."),
      ("Dos imágenes de una galaxia: en luz visible se ven estrellas y en radio, grandes nubes de gas. ¿Por qué son distintas? A) Cada banda muestra componentes que emiten en esa banda B) Las cámaras están rotas", "A", "Estrellas y gas emiten en bandas diferentes."),
  ],
  cha=[
      ("Un telescopio espacial infrarrojo debe mantenerse muy frío. ¿Por qué? A) Su propio calor emitiría infrarrojo y taparía las señales débiles B) El frío aumenta su tamaño", "A", "El calor propio del instrumento es una fuente de ruido infrarrojo."),
      arith("El telescopio James Webb está a unos 1.500.000 km de la Tierra. La luz viaja a 300.000 km/s. ¿Cuántos segundos tarda una señal de radio, que viaja a esa rapidez, en llegar?", "1500000/300000", "El tiempo es distancia dividida por rapidez.", " s"),
  ],
  context=[arith("El vapor de agua disponible sobre dos sitios de ejemplo es de 1 mm en el sitio A y de 10 mm en el sitio B. ¿Cuántas veces más vapor hay sobre el sitio B?", "10/1", "Se divide el vapor de B por el de A.", " veces")],
  selfcheck=[("¿Qué banda muestra el polvo tibio?", "El infrarrojo", "Los objetos tibios emiten infrarrojo."), ("¿Qué bandas llegan casi completas al suelo?", "La visible y la de radio", "La atmósfera es transparente a ellas."), ("¿Por qué se combinan imágenes de varias bandas?", "Porque cada banda muestra un componente distinto del objeto", "Así se entiende el objeto completo.")],
  open_task=task("Completa una tabla con las bandas radio, infrarrojo, visible, ultravioleta y rayos X: ¿llega al suelo? (sí, parcial o no), ¿qué proceso o componente revela? y ¿dónde se coloca el telescopio (desierto seco y alto o espacio)? Después elige la banda y el lugar para estudiar (a) nubes de gas frío donde nacen estrellas y (b) explosiones de estrellas.", "Radio: sí, gas frío, desierto alto y seco. Infrarrojo: parcial, objetos tibios y polvo, lugar alto y seco o espacio. Visible: sí, estrellas, suelo. Ultravioleta: no, procesos energéticos, espacio. Rayos X: no, gas muy caliente, espacio. (a) Radio o milimétrica, ALMA. (b) Rayos X o gamma, en el espacio.", ["cinco filas completas", "dos elecciones justificadas"], ["tabla y dos frases"], ["poner rayos X en un telescopio del suelo", "olvidar que el infrarrojo llega parcialmente"], "Pregunta qué combinación de imágenes usarías para una galaxia completa."),
  reinforce="Escribe una radiación que llega al suelo y una que no.",
  extend="Explica por qué se colocan en el espacio los telescopios para rayos X.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Los datos de longitudes de onda son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a leer un espectro para saber de qué está hecho un astro y a qué velocidad se mueve. Sirve para entender cómo se descubren planetas y cómo se expande el universo.",
  prior=["Sé que la luz se separa en colores.", "Sé que el efecto Doppler cambia la longitud de onda."],
  explain=[
      "Un espectro es la luz separada en sus colores. Un gas caliente emite luz solo en algunos colores, que se ven como líneas brillantes: líneas de emisión. Un gas más frío que está delante de una fuente de luz absorbe algunos colores, que se ven como líneas oscuras: líneas de absorción. Cada elemento químico produce un patrón de líneas único, como una huella digital. Al comparar el espectro de un astro con los de laboratorio se identifica de qué está hecho.",
      "El color general de un astro indica su temperatura: más caliente, más azulado. Las líneas también permiten medir el movimiento. Si el astro se aleja, sus líneas se corren a longitudes de onda mayores: desplazamiento al rojo. Si se acerca, se corren a longitudes de onda menores: desplazamiento al azul. Para velocidades mucho menores que la de la luz, la velocidad en km/s es: 300.000 × Δλ ÷ λ, donde Δλ es el corrimiento de la línea y λ su longitud de onda en el laboratorio.",
      "Esta técnica tiene grandes aplicaciones. Si una estrella oscila hacia nosotros y se aleja de nosotros con regularidad, puede haber un planeta que tira de ella con su gravedad al orbitar. Las galaxias lejanas muestran desplazamiento al rojo, lo que indica que se alejan de nosotros y que el universo se expande.",
  ],
  vocab=[("espectro", "luz separada en sus colores"), ("línea de emisión", "línea brillante que produce un gas caliente"), ("línea de absorción", "línea oscura que produce un gas más frío frente a una fuente de luz"), ("desplazamiento al rojo", "corrimiento de las líneas a mayor longitud de onda, que indica alejamiento"), ("velocidad radial", "velocidad con que un astro se acerca o se aleja de nosotros"), ("exoplaneta", "planeta que orbita otra estrella")],
  worked=[
      ("Velocidad desde el corrimiento", "Una línea de laboratorio mide 500 nm y en una galaxia mide 501 nm. ¿A qué velocidad se mueve y en qué sentido?", ["El corrimiento es 501 − 500 = 1 nm, hacia longitudes mayores: se aleja.", "Velocidad = 300.000 × 1 ÷ 500 = 600 km/s."], "Se aleja a 600 km/s"),
      ("Identificar un elemento", "Un espectro estelar tiene líneas oscuras en los mismos colores que el patrón del hidrógeno del laboratorio. ¿Qué indica?", ["Cada elemento tiene un patrón único de líneas.", "El mismo patrón indica el mismo elemento."], "Que la estrella contiene hidrógeno"),
  ],
  mistakes=[
      ("Pensar que el desplazamiento al rojo significa que el astro es rojo.", "Significa que las líneas se corren hacia longitudes de onda mayores, no que el astro sea de ese color.", "Compara las líneas con las del laboratorio."),
      ("Creer que el espectro solo sirve para ver los colores.", "También entrega composición, temperatura y velocidad.", "Pregunta qué propiedad se lee de las líneas."),
  ],
  rec=[
      ("¿Qué instrumento separa la luz en colores?", "Un espectrógrafo", "Entrega el espectro."),
      ("Verdadero o falso: cada elemento tiene un patrón único de líneas.", "Verdadero", "Es como una huella digital."),
      ("Si las líneas se corren hacia el azul, ¿el astro se acerca o se aleja?", "Se acerca", "Las longitudes de onda se acortan."),
  ],
  und=[
      ("Las líneas de absorción aparecen cuando: A) un gas más frío absorbe colores de la luz de una fuente detrás B) un gas caliente emite luz", "A", "Faltan los colores absorbidos."),
      ("Las líneas de una galaxia se corren hacia el rojo. ¿Qué indica?", "Que se aleja", "Las longitudes de onda aumentan."),
      ("¿Qué indica el color general de un astro?", "Su temperatura: más azul, más caliente", "El color depende de la temperatura."),
  ],
  app=[
      arith("Una línea mide 600 nm en el laboratorio y se corre 2 nm en una estrella. Con v = 300.000 × Δλ ÷ λ, ¿cuántos km/s se mueve?", "300000*2/600", "Se reemplazan los datos en la fórmula.", " km/s"),
      arith("Una línea mide 400 nm en el laboratorio y se corre 1 nm en otra estrella. ¿A cuántos km/s se mueve?", "300000*1/400", "Se reemplazan los datos en la fórmula.", " km/s"),
      ("Una línea de laboratorio mide 656 nm. En la galaxia A mide 660 nm; en B, 656 nm; en C, 652 nm. ¿Cuál se acerca y cuál se aleja?", "C se acerca y A se aleja", "Una longitud mayor indica alejamiento y una menor, acercamiento."),
  ],
  rea=[
      ("Una estrella muestra un corrimiento que cambia de rojo a azul y de azul a rojo con regularidad. ¿Qué puede haber? A) Un planeta que la hace oscilar al orbitarla B) Una estrella que se apaga y se enciende", "A", "La estrella oscila alrededor del centro de masa con su planeta."),
      ("Las galaxias más lejanas muestran mayor desplazamiento al rojo. ¿Qué sugiere esto? A) Que el universo se expande B) Que las galaxias lejanas son rojas", "A", "Las galaxias se alejan unas de otras."),
  ],
  cha=[
      arith("Una línea mide 500 nm en el laboratorio y se corre 3 nm en una estrella. ¿A cuántos km/s se mueve?", "300000*3/500", "Se reemplazan los datos en la fórmula.", " km/s"),
      ("Si una línea no se corre respecto del laboratorio, ¿qué sabemos del movimiento del astro?", "Que no se acerca ni se aleja de nosotros", "No hay velocidad radial."),
  ],
  context=[ex("Una sirena que se acerca suena más aguda. ¿Qué corrimiento de la luz es equivalente? A) Al azul B) Al rojo", "A", "Al acercarse aumenta la frecuencia, igual que en el sonido agudo.")],
  selfcheck=[("¿Qué es una línea de absorción?", "Una línea oscura en un espectro continuo", "La produce un gas más frío que absorbe colores."), ("¿Qué indica el desplazamiento al rojo?", "Que el astro se aleja", "Las líneas se corren a mayor longitud de onda."), ("¿Para qué sirve comparar con el laboratorio?", "Para identificar elementos y medir corrimientos", "Se conocen las líneas de cada elemento.")],
  open_task=task("Una línea del hidrógeno mide 656 nm en el laboratorio. En cuatro galaxias mide: A, 657 nm; B, 656 nm; C, 655 nm; D, 659 nm. Para cada una, escribe si se acerca, se aleja o no se mueve en la línea de visión, y ordénalas de la que más rápido se aleja a la que más rápido se acerca. Con v = 300.000 × Δλ ÷ λ, estima la rapidez de D con la parte entera.", "A se aleja; B no se mueve; C se acerca; D se aleja. Orden: D, A, B, C. D: 300.000 × 3 ÷ 656 = 1.371 km/s con la parte entera.", ["clasificación correcta de las cuatro", "orden correcto", "rapidez de D"], ["tabla y cálculo"], ["invertir acercamiento y alejamiento", "no usar el corrimiento Δλ"], "Pregunta qué cambiaría si la longitud de onda de laboratorio fuera 500 nm."),
  reinforce="Escribe qué indica un desplazamiento al azul.",
  extend="Explica cómo se puede detectar un planeta con el corrimiento de las líneas de su estrella.")

L(OA, 5,
  materials="Este cuaderno y lápiz. Los datos de las científicas y los científicos son generales y de dominio público; si quieres saber más, puedes pedir ayuda en la biblioteca.",
  use="Aprenderé quiénes son algunas astrónomas y astrónomos chilenos y qué aportes hicieron. Sirve para ver que la ciencia en Chile se hace con equipos y colaboración internacional.",
  prior=["Sé qué es una estrella y qué es una supernova en términos generales.", "Sé que los observatorios de Chile reciben astrónomos de varios países."],
  explain=[
      "María Teresa Ruiz es astrónoma de la Universidad de Chile. Fue la primera mujer en recibir el Premio Nacional de Ciencias Exactas. Descubrió una enana marrón, un objeto más masivo que un planeta gigante pero sin la masa suficiente para fusionar hidrógeno como una estrella. También ha estudiado las enanas blancas, que son los restos muy densos de estrellas pequeñas.",
      "José Maza, astrónomo de la Universidad de Chile, ha estudiado supernovas, que son explosiones al final de la vida de ciertas estrellas, y la cosmología. También es muy conocido como divulgador de la astronomía. Mario Hamuy es un astrónomo chileno que trabajó con supernovas de tipo Ia; como estas supernovas tienen casi el mismo brillo real, sirven para medir distancias en el universo, y estas mediciones aportaron a descubrir que la expansión del universo se acelera.",
      "La ciencia es una tarea colectiva: los resultados se publican, otros especialistas los revisan y se pueden repetir. En los observatorios instalados en Chile, una parte del tiempo de observación está reservada para la comunidad astronómica chilena. ALMA es una colaboración entre Europa, Norteamérica, Asia Oriental y Chile. Por eso formar astrónomas y astrónomos en el país y comunicar la ciencia a la comunidad son tareas importantes.",
  ],
  vocab=[("enana marrón", "objeto más masivo que un planeta gigante, pero sin masa suficiente para fusionar hidrógeno"), ("enana blanca", "resto muy denso de una estrella pequeña"), ("supernova", "explosión de una estrella al final de su vida"), ("cosmología", "estudio del origen y la evolución del universo"), ("divulgación científica", "comunicar la ciencia al público general"), ("colaboración internacional", "trabajo conjunto de países para un proyecto científico")],
  worked=[
      ("Asociar aportes", "Relaciona cada persona con su aporte. Personas: (1) María Teresa Ruiz, (2) José Maza, (3) Mario Hamuy. Aportes: a) supernovas de tipo Ia para medir distancias, b) descubrimiento de una enana marrón, c) estudio de supernovas y divulgación.", ["Ruiz se asocia con la enana marrón: b.", "Maza se asocia con supernovas y divulgación: c.", "Hamuy se asocia con supernovas para medir distancias: a."], "1 con b, 2 con c, 3 con a"),
      ("Brillo y distancia", "Dos supernovas del mismo tipo tienen el mismo brillo real. Una se ve mucho más débil. ¿Cuál está más lejos?", ["Con el mismo brillo real, la que se ve más débil está más lejos.", "Así se usan para medir distancias."], "La que se ve más débil"),
  ],
  mistakes=[
      ("Creer que un descubrimiento es obra de una sola persona.", "Los resultados se logran con equipos, instrumentos compartidos y revisión de otros especialistas.", "Pregunta quiénes participaron y quién revisó los datos."),
      ("Confundir una enana marrón con un planeta común.", "Es más masiva que un planeta gigante, pero sin fusión de hidrógeno como una estrella.", "Recuerda que está entre planeta y estrella."),
  ],
  rec=[
      ("¿Qué astrónoma chilena descubrió una enana marrón?", "María Teresa Ruiz", "Es astrónoma de la Universidad de Chile."),
      ("¿Qué es una supernova?", "La explosión de una estrella al final de su vida", "Libera una enorme cantidad de energía."),
      ("Verdadero o falso: José Maza es conocido como divulgador de la astronomía.", "Verdadero", "Comunica la ciencia al público general."),
  ],
  und=[
      ("Una enana marrón es: A) un objeto más masivo que un planeta gigante pero sin fusión de hidrógeno B) una estrella en explosión", "A", "Está entre un planeta y una estrella."),
      ("Las supernovas de tipo Ia sirven para medir distancias porque: A) tienen casi el mismo brillo real B) son de color azul", "A", "Si el brillo real es igual, el brillo aparente indica la distancia."),
      ("¿Qué regiones del mundo colaboran con Chile en ALMA?", "Europa, Norteamérica y Asia Oriental", "ALMA es un proyecto internacional."),
  ],
  app=[
      ("Dos supernovas del mismo tipo, X e Y. X se ve 4 veces más débil que Y. ¿Cuál está más lejos?", "La X", "Con igual brillo real, la más débil está más lejos."),
      arith("Un telescopio dispone de 300 noches de observación al año. Si 1 de cada 10 noches se reserva para astrónomas y astrónomos chilenos (dato de ejemplo), ¿cuántas noches son?", "300/10", "Se divide el total por 10.", " noches"),
      ("Una compañera te pide explicar qué es una enana blanca. ¿Qué respondes?", "El resto muy denso de una estrella pequeña", "Es lo que queda cuando la estrella agota su combustible."),
  ],
  rea=[
      ("Un compañero dice que un solo científico descubre todo por sí mismo. ¿Cuál es la respuesta correcta? A) La ciencia es colaborativa: se trabaja en equipos y otros revisan los datos B) Es correcto, la ciencia es un trabajo individual", "A", "La ciencia moderna depende de colaboración y revisión."),
      ("Para que una afirmación astronómica sea aceptada, debe: A) publicarse y ser revisada por otros especialistas con datos B) ser dicha por alguien famoso", "A", "La evidencia y la revisión dan confianza."),
  ],
  cha=[
      ("Al medir muchas supernovas, se vio que las galaxias lejanas se alejan más rápido. ¿Qué sugiere sobre el universo?", "Que se expande", "El alejamiento generalizado indica expansión."),
      ("Alguien dice que los observatorios en Chile pertenecen solo a países extranjeros. ¿Qué dato lo contradice? A) Hay astrónomos chilenos y una parte del tiempo de observación se reserva para la comunidad chilena B) No hay ningún astrónomo chileno", "A", "La participación chilena existe en muchos proyectos."),
  ],
  context=[ex("Una noticia de ejemplo dice que un equipo con participación chilena estudió la explosión de una estrella en una galaxia lejana. ¿Cómo se llama ese fenómeno?", "Supernova", "Es la explosión de una estrella al final de su vida.")],
  selfcheck=[("¿Qué es una enana marrón?", "Un objeto entre planeta y estrella", "No fusiona hidrógeno."), ("¿Por qué las supernovas Ia sirven para medir distancias?", "Porque tienen casi el mismo brillo real", "Su brillo aparente indica la distancia."), ("¿Qué es la divulgación científica?", "Comunicar la ciencia al público", "Ayuda a que más personas la comprendan.")],
  open_task=task("Haz una ficha para cada una de estas tres personas: María Teresa Ruiz, José Maza y Mario Hamuy, con dos datos: tema de estudio y aporte. Después escribe tres preguntas que le harías a una astrónoma o un astrónomo en una entrevista y una razón por la que la colaboración internacional ayuda a la astronomía en Chile. Los datos de esta lección deben ser contrastados con una fuente oficial antes de usarlos en un trabajo.", "Ruiz: Universidad de Chile, enanas marrones y enanas blancas, descubrió una enana marrón. Maza: Universidad de Chile, supernovas y cosmología, divulgación. Hamuy: supernovas de tipo Ia, medición de distancias. Preguntas: ¿qué te llevó a estudiar astronomía?; ¿qué instrumentos usas?; ¿cómo se comprueba un descubrimiento? Colaboración: comparte instrumentos y datos que un país no podría costear solo.", ["tres fichas con dos datos", "tres preguntas abiertas", "una razón de colaboración", "reconoce que hay que contrastar los datos"], ["tres fichas y tres preguntas"], ["atribuir un aporte a la persona equivocada", "preguntas de respuesta sí o no solamente"], "Pregunta qué fuente oficial usarías para comprobar un dato."),
  reinforce="Escribe una frase que explique por qué una supernova Ia sirve para medir distancias.",
  extend="Explica por qué la divulgación científica también es parte del trabajo de un astrónomo.")

L(OA, 6,
  materials="Este cuaderno, lápiz y calculadora. Los datos de los casos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a evaluar beneficios, riesgos y límites de la astronomía en Chile: la contaminación lumínica, la radioeléctrica y la seguridad de las visitas. Sirve para tomar decisiones informadas.",
  prior=["Sé qué instrumentos usa la astronomía en Chile.", "Sé qué es la contaminación lumínica."],
  explain=[
      "La astronomía trae beneficios: descubrimientos científicos, tecnologías nuevas, educación, empleo y astroturismo, que es el turismo para observar el cielo con guías. También tiene costos: usa agua y energía en un desierto, genera residuos y ocupa territorios donde viven comunidades locales y pueblos originarios, que deben ser consultadas y respetadas. Por eso, antes de construir un proyecto grande se hace una evaluación de impacto ambiental, que estudia sus efectos y incluye la consulta a las comunidades.",
      "Hay amenazas para la observación. La contaminación lumínica es el exceso de luz artificial; se reduce con luminarias que apuntan hacia abajo, luz cálida y apagado de luces innecesarias. La contaminación radioeléctrica es la interferencia de celulares y antenas con los radiotelescopios; por eso hay zonas de silencio radioeléctrico. Las constelaciones de satélites artificiales reflejan luz y dejan trazos en las imágenes. También afectan los sismos, las obras cercanas y el polvo.",
      "Las visitas requieren cuidado. Nunca se mira el Sol directamente. A 5.000 m de altitud hay menos oxígeno por cada respiración, y las personas pueden sufrir mal de altura, con dolor de cabeza y mareo; se debe subir con aclimatación y guías. Toda decisión debe usar datos y reconocer sus límites: las mediciones tienen incertidumbre y los resultados deben revisarse.",
  ],
  vocab=[("astroturismo", "turismo para observar el cielo con guías"), ("contaminación radioeléctrica", "interferencia de señales de radio artificiales con los radiotelescopios"), ("zona de silencio radioeléctrico", "área donde se limitan las emisiones de radio para proteger a los radiotelescopios"), ("constelación de satélites", "grupo grande de satélites artificiales que orbitan juntos"), ("mal de altura", "malestar por la baja cantidad de oxígeno a gran altitud"), ("incertidumbre", "margen de duda de una medición")],
  worked=[
      ("Evaluar una medida", "Un pueblo cambia sus luminarias por otras que apuntan hacia abajo. ¿Qué efecto tendrá en el cielo?", ["La luz que sube al cielo disminuye.", "El cielo se mantiene más oscuro."], "Reduce la contaminación lumínica"),
      ("Beneficio y costo", "Un proyecto trae empleo local, pero usa agua en el desierto. ¿Cómo se evalúa?", ["Se enumeran beneficios y costos con datos.", "Se escucha a las comunidades y se buscan medidas para reducir el costo."], "Comparando beneficios y costos con datos y consulta a las comunidades"),
  ],
  mistakes=[
      ("Pensar que más luz en la noche siempre es más seguridad sin costos.", "El exceso de luz que apunta al cielo afecta la observación y a los animales; se puede iluminar mejor con luz dirigida.", "Evalúa también la dirección y el color de la luz."),
      ("Creer que los celulares no afectan a los telescopios de radio.", "Emiten ondas de radio que pueden interferir con las señales débiles.", "Respeta las zonas de silencio radioeléctrico."),
  ],
  rec=[
      ("¿Qué es la contaminación lumínica?", "El exceso de luz artificial que dificulta ver el cielo", "Aumenta el brillo del cielo nocturno."),
      ("Verdadero o falso: los celulares pueden interferir con los radiotelescopios.", "Verdadero", "Emiten ondas de radio."),
      ("¿Qué medida reduce la contaminación lumínica: luminarias hacia abajo o hacia arriba?", "Hacia abajo", "Así no iluminan el cielo."),
  ],
  und=[
      ("Las constelaciones de satélites afectan a la astronomía porque: A) reflejan luz y dejan trazos en las imágenes B) calientan la atmósfera y producen turbulencia", "A", "Los trazos perjudican las observaciones."),
      ("¿Por qué puede haber mal de altura a 5.000 m? A) Hay menos oxígeno por cada respiración porque el aire es menos denso B) Los gases del aire cambian y a esa altura ya no hay oxígeno", "A", "La presión del aire es menor."),
      ("El astroturismo es: A) turismo para observar el cielo con guías B) turismo para fotografiar paisajes de día", "A", "Se hace en lugares con cielos oscuros."),
  ],
  app=[
      arith("Un pueblo tenía 200 luminarias que apuntaban hacia arriba y reemplazó 150 por luminarias dirigidas hacia abajo. ¿Cuántas siguen apuntando hacia arriba?", "200-150", "Se resta lo reemplazado del total.", " luminarias"),
      arith("Un observatorio recibe 1.200 visitantes al año repartidos en 4 grupos iguales. ¿Cuántos visitantes tiene cada grupo?", "1200/4", "Se divide el total por el número de grupos.", " visitantes"),
      ("Antes de construir una planta cerca de un observatorio, ¿qué evaluación corresponde?", "Una evaluación de impacto ambiental con consulta a las comunidades", "Permite evaluar efectos y escuchar a las personas afectadas."),
  ],
  rea=[
      ("Alguien dice que el cielo oscuro no tiene valor. ¿Qué argumento lo contradice? A) Permite la ciencia, el turismo y es patrimonio natural B) Solo sirve para dormir", "A", "El cielo oscuro es un recurso con valor científico y cultural."),
      ("Una antena de un pueblo vecino interfiere con las señales de radio de un observatorio. ¿Qué medida corresponde? A) Ordenar las frecuencias y proteger una zona de silencio radioeléctrico B) Aumentar la potencia de la antena", "A", "Se reduce la interferencia."),
  ],
  cha=[
      ("A 5.000 m de altitud el aire tiene aproximadamente la mitad de presión que a nivel del mar. Una persona sin aclimatación respira por bocanada: A) cerca de la mitad del oxígeno que al nivel del mar B) el doble del oxígeno", "A", "La cantidad de oxígeno depende de la presión."),
      ("La luz azulada se dispersa más en la atmósfera que la luz cálida. ¿Qué luz perturba más el cielo nocturno?", "La azulada", "Se dispersa más y aumenta el brillo del cielo."),
  ],
  context=[arith("Un grupo escolar cuenta las estrellas visibles de una constelación de 20 posibles: ve 8 en la ciudad y 18 en el campo. ¿Cuántas estrellas más ve en el campo?", "18-8", "Se resta lo visto en la ciudad a lo visto en el campo.", " estrellas")],
  selfcheck=[("Nombra un beneficio y un costo de la astronomía en el desierto.", "Beneficio: descubrimientos y empleo; costo: uso de agua y energía", "Hay que evaluar ambos."), ("¿Qué es una zona de silencio radioeléctrico?", "Un área donde se limitan las emisiones de radio", "Protege a los radiotelescopios."), ("¿Qué precaución se toma por el mal de altura?", "Aclimatarse y subir con guías", "Hay menos oxígeno a gran altitud.")],
  open_task=task("Un municipio de ejemplo tiene 100 luminarias que apuntan hacia arriba y quiere cambiarlas por luminarias cálidas dirigidas hacia abajo, a $200.000 cada una (precio de ejemplo). Calcula el costo total. Escribe dos beneficios (uno para el cielo y uno para la comunidad) y un costo o límite del proyecto. Propón cómo comprobar con datos que mejoró la oscuridad del cielo.", "Costo: 100 × $200.000 = $20.000.000. Beneficios: cielo más oscuro para observar y menor consumo de energía. Límite: el costo inicial. Comprobación: contar estrellas visibles de una constelación antes y después.", ["costo correcto de $20.000.000", "dos beneficios", "un costo o límite", "forma de comprobar con datos"], ["cálculo y respuestas escritas"], ["olvidar el costo", "proponer una comprobación sin datos"], "Pregunta qué grupos de la comunidad deberían participar de la decisión."),
  reinforce="Escribe dos medidas para proteger el cielo oscuro.",
  extend="Explica por qué es importante consultar a las comunidades locales antes de construir un observatorio.")

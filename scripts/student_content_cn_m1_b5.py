"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 15 (escalas y propiedades de estructuras cósmicas)."""
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


OA = "CN1M OA 15"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Todos los tamaños y distancias están escritos en los ejercicios y son valores aproximados.",
  use="Aprenderé las unidades y escalas con que se miden tamaños y distancias en el universo. Sirve para ordenar estructuras cósmicas y entender que mirar lejos es mirar el pasado.",
  prior=["Sé que la luz viaja a unos 300.000 km/s.", "Sé multiplicar, dividir y comparar números grandes."],
  explain=[
      "En el universo los kilómetros se quedan cortos, por eso se usan otras unidades. La unidad astronómica (UA) es la distancia media entre la Tierra y el Sol, unos 150 millones de km; sirve para medir distancias dentro del sistema solar. El año luz es la distancia que recorre la luz en un año, unos 9,5 billones de km; sirve para medir distancias entre estrellas y galaxias. Un año luz es una unidad de distancia, no de tiempo.",
      "Algunos tamaños aproximados: la Luna mide unos 3.500 km de diámetro, la Tierra unos 12.700 km y el Sol unos 1.400.000 km. La Luna está a unos 384.000 km de la Tierra. La estrella más cercana al Sol está a unos 4 años luz. La Vía Láctea, nuestra galaxia, mide unos 100.000 años luz de diámetro, y la galaxia de Andrómeda está a unos 2.500.000 años luz.",
      "Como la luz tarda en llegar, al mirar un objeto lejano lo vemos como era en el pasado. La luz del Sol tarda unos 500 segundos; la de una estrella a 8 años luz salió hace 8 años. Para comparar escalas se usa el orden de magnitud, que dice cuántas veces es mayor una cantidad que otra, en potencias de 10 aproximadas.",
  ],
  vocab=[("unidad astronómica (UA)", "distancia media Tierra–Sol, unos 150 millones de km"), ("año luz", "distancia que recorre la luz en un año, unos 9,5 billones de km"), ("diámetro", "longitud de un lado a otro de un objeto esférico, pasando por su centro"), ("orden de magnitud", "cuántas veces mayor es una cantidad, expresado en potencias de 10"), ("escala", "rango de tamaños o distancias con que se estudia un objeto"), ("estrella", "esfera de gas que emite luz propia")],
  worked=[
      ("Distancias en UA", "Júpiter está a unos 780 millones de km del Sol y 1 UA son 150 millones de km. ¿A cuántas UA está, con la parte entera?", ["Divido la distancia por el valor de 1 UA.", "Calculo 780 ÷ 150 y tomo la parte entera."], "Unas 5 UA"),
      ("Mirar el pasado", "Una estrella está a 8 años luz. ¿Cuándo salió la luz que vemos hoy?", ["La luz tarda 8 años en recorrer 8 años luz.", "Lo que vemos hoy salió de la estrella hace 8 años."], "Hace 8 años"),
  ],
  mistakes=[
      ("Creer que el año luz es una unidad de tiempo.", "Es la distancia que recorre la luz en un año.", "Pregunta si la cantidad se expresa en kilómetros o en años."),
      ("Pensar que el Sol está a 1 año luz de la Tierra.", "La luz del Sol tarda solo unos 500 segundos: está a 1 UA.", "Compara el tiempo que tarda la luz."),
  ],
  rec=[
      ("¿Qué mide el año luz: tiempo o distancia?", "Distancia", "Es lo que recorre la luz en un año."),
      ("Verdadero o falso: la distancia media Tierra–Sol es 1 UA.", "Verdadero", "Es la definición de unidad astronómica."),
      ("¿Qué es mayor: un año luz o una UA?", "Un año luz", "Un año luz son unos 9,5 billones de km y una UA, 150 millones de km."),
  ],
  und=[
      ("Para medir la distancia entre dos estrellas, ¿qué unidad es más cómoda: el metro, la UA o el año luz?", "El año luz", "Las distancias entre estrellas son enormes incluso en UA."),
      ("Una estrella está a 12 años luz. La luz que vemos hoy salió de ella hace: A) 12 años B) 12 días", "A", "La luz tarda 8 años en llegar."),
      ("Ordena de menor a mayor diámetro: Sol, Luna, Tierra.", "Luna, Tierra, Sol", "La Luna mide 3.500 km, la Tierra 12.700 km y el Sol 1.400.000 km."),
  ],
  app=[
      arith("La Luna está a unos 384.000 km de la Tierra y el Sol a 150.000.000 km. ¿Cuántas veces más lejos está el Sol que la Luna, con la parte entera?", "150000000//384000", "Se divide la distancia al Sol por la distancia a la Luna.", " veces"),
      arith("El diámetro del Sol es de unos 1.400.000 km y el de la Tierra de 12.700 km. ¿Cuántas veces mayor es el diámetro del Sol, con la parte entera?", "1400000//12700", "Se divide el diámetro del Sol por el de la Tierra.", " veces"),
      arith("Saturno está a unos 1.430 millones de km del Sol y 1 UA son 150 millones de km. ¿A cuántas UA está, con la parte entera?", "1430//150", "Se divide la distancia por el valor de 1 UA.", " UA"),
  ],
  rea=[
      ("Un compañero dice que el año luz es una unidad de tiempo. ¿Qué respuesta es correcta? A) No: es una distancia, la que recorre la luz en un año B) Sí: se mide en años", "A", "El nombre incluye «año», pero mide longitud."),
      ("La Vía Láctea mide unos 100.000 años luz de diámetro. ¿Qué significa? A) La luz tarda unos 100.000 años en cruzarla B) Tiene 100.000 años de antigüedad", "A", "Es una medida de tamaño, no de edad."),
  ],
  cha=[
      arith("La galaxia de Andrómeda está a unos 2.500.000 años luz. El diámetro de la Vía Láctea es de unos 100.000 años luz. ¿Cuántos diámetros de la Vía Láctea caben en esa distancia?", "2500000/100000", "Se divide la distancia por el diámetro.", " diámetros"),
      ("La luz de una estrella a 50 años luz nos muestra la estrella como es hoy o como era. ¿Cuál es la respuesta correcta?", "Como era hace 50 años", "La luz tardó 50 años en llegar."),
  ],
  context=[arith("Una persona tiene hoy 70 años y mira una estrella que está a 40 años luz. ¿Qué edad tenía cuando salió de la estrella la luz que ve?", "70-40", "Se restan los años que tardó la luz.", " años")],
  selfcheck=[("¿Qué es una unidad astronómica?", "La distancia media entre la Tierra y el Sol", "Son unos 150 millones de km."), ("¿Qué unidad usarías para medir una galaxia?", "El año luz", "Es la unidad de las grandes distancias."), ("¿Por qué mirar lejos es mirar el pasado?", "Porque la luz tarda en llegar", "Lo que vemos salió hace tiempo.")],
  open_task=task("Datos aproximados: gota de lluvia, 0,002 m; Tierra, 12.700 km; Sol, 1.400.000 km; distancia Tierra–Sol, 150 millones de km; estrella cercana, 4 años luz; Vía Láctea, 100.000 años luz. Ordena estas seis medidas de menor a mayor, escribe la unidad más cómoda para cada una (m, km, UA o año luz) y explica en dos líneas por qué una estrella a 4 años luz se ve como era en el pasado.", "Orden: gota (m), Tierra (km), Sol (km), Tierra–Sol (km o 1 UA), estrella cercana (año luz), Vía Láctea (año luz). Explicación: la luz de la estrella tarda 4 años en llegar, así que vemos cómo era hace 4 años.", ["orden correcto", "unidades coherentes", "explica con el tiempo que tarda la luz"], ["lista ordenada con unidades y dos líneas"], ["poner la Vía Láctea antes de la estrella", "decir que el año luz mide tiempo"], "Pregunta qué se vería hoy desde allí si miráramos la Tierra."),
  reinforce="Escribe dos ejemplos de distancias que conviene medir en UA y dos que conviene medir en años luz.",
  extend="Explica por qué un telescopio que mira una galaxia lejana permite estudiar la historia del universo.")

L(OA, 2,
  materials="Este cuaderno y lápiz. Los datos de los cuerpos están descritos en los ejercicios y son aproximados.",
  use="Aprenderé a distinguir meteoroides, asteroides, cometas, satélites y planetas por su tamaño, forma y posición. Sirve para nombrar bien lo que ves en el cielo.",
  prior=["Sé que los planetas orbitan el Sol.", "Sé qué es la gravedad."],
  explain=[
      "Un meteoroide es un fragmento pequeño de roca o metal que viaja por el espacio; puede medir desde granos de polvo hasta algunos metros. Cuando entra en la atmósfera de la Tierra, se calienta por la fricción y deja un trazo luminoso breve: ese fenómeno es un meteoro, o «estrella fugaz». Si un fragmento llega al suelo, se llama meteorito. Un asteroide es un cuerpo rocoso o metálico mayor, de metros a cientos de kilómetros, de forma irregular si es pequeño; la mayoría orbita en el cinturón de asteroides, entre Marte y Júpiter.",
      "Un cometa es un cuerpo de hielo, polvo y roca, de pocos kilómetros, con una órbita muy alargada. Al acercarse al Sol, el hielo se evapora y forma una nube brillante y una cola que siempre apunta lejos del Sol, empujada por la radiación y el viento solar. Un satélite es un cuerpo que orbita a otro mayor. Los satélites naturales, como la Luna, se formaron en el cosmos; los artificiales los construyen las personas para comunicaciones, observación y otros usos.",
      "Un planeta orbita una estrella, tiene masa suficiente para que su gravedad lo vuelva casi esférico y ha despejado de otros cuerpos la zona de su órbita. Un planeta enano, como Plutón, es esférico, pero comparte su órbita con muchos otros cuerpos. Los cuerpos con gran masa son esféricos porque su gravedad atrae todo el material hacia el centro; los pequeños pueden ser irregulares.",
  ],
  vocab=[("meteoroide", "fragmento pequeño de roca o metal que viaja por el espacio"), ("meteoro", "trazo luminoso que deja un meteoroide al entrar en la atmósfera"), ("meteorito", "fragmento que llega al suelo de un planeta"), ("asteroide", "cuerpo rocoso o metálico que orbita el Sol, de forma muchas veces irregular"), ("cometa", "cuerpo de hielo y polvo que forma una cola al acercarse al Sol"), ("satélite", "cuerpo que orbita a otro mayor")],
  worked=[
      ("Nombre correcto", "Ves una línea luminosa muy breve en el cielo nocturno. ¿Qué es?", ["Es un trazo luminoso por fricción en la atmósfera.", "Ese fenómeno se llama meteoro."], "Un meteoro"),
      ("Cola de cometa", "Un cometa pasa cerca del Sol. ¿Hacia dónde apunta su cola?", ["La radiación y el viento solar empujan el material.", "El material sale en la dirección contraria al Sol."], "Hacia el lado opuesto al Sol"),
  ],
  mistakes=[
      ("Llamar «meteoro» a la piedra que está en el espacio.", "El meteoro es el trazo luminoso; la piedra se llama meteoroide.", "Pregunta si hablas del objeto o del fenómeno luminoso."),
      ("Creer que la cola de un cometa apunta en la dirección en que se mueve.", "Siempre apunta lejos del Sol.", "Dibuja el Sol y la cola al lado contrario."),
  ],
  rec=[
      ("¿Cómo se llama un fragmento que llega al suelo?", "Meteorito", "Es lo que queda de un meteoroide que sobrevivió al paso por la atmósfera."),
      ("¿Entre qué dos planetas está el cinturón de asteroides?", "Entre Marte y Júpiter", "Allí orbitan la mayoría de los asteroides."),
      ("Verdadero o falso: la cola de un cometa siempre apunta hacia el Sol.", "Falso", "Apunta en la dirección contraria al Sol."),
  ],
  und=[
      ("Un fragmento de roca de pocos centímetros que viaja por el espacio se llama: A) meteoroide B) meteoro", "A", "El meteoro es el destello que produce al entrar en la atmósfera."),
      ("¿Cuál es el satélite natural de la Tierra?", "La Luna", "Orbita nuestro planeta."),
      ("¿Por qué un planeta es esférico y un asteroide pequeño puede ser irregular? A) La gravedad de un cuerpo muy masivo lo redondea B) El tamaño no influye en la forma", "A", "Solo la gravedad de una gran masa jala el material hacia el centro."),
  ],
  app=[
      ("Un cuerpo de hielo y polvo de unos 10 km muestra una cola brillante cuando se acerca al Sol. ¿Qué cuerpo es?", "Un cometa", "El hielo se evapora y forma la cola."),
      ("Un cuerpo rocoso irregular de unos 300 m orbita entre Marte y Júpiter. ¿Qué cuerpo es?", "Un asteroide", "Es rocoso, irregular y está en el cinturón."),
      arith("La cola de un cometa mide 2.000.000 km y su núcleo, 10 km. ¿Cuántas veces mayor es la cola que el núcleo?", "2000000/10", "Se divide el largo de la cola por el diámetro del núcleo.", " veces"),
  ],
  rea=[
      ("Un estudiante dice: «Los meteoros son piedras que flotan en el espacio». ¿Cuál es la corrección? A) El meteoro es el destello; la piedra se llama meteoroide B) Es correcto, así se llaman las piedras", "A", "El nombre cambia según sea el objeto o el fenómeno."),
      ("Un cuerpo esférico orbita el Sol, pero comparte su órbita con muchos otros objetos. ¿Qué es?", "Un planeta enano", "No ha despejado su órbita."),
  ],
  cha=[
      arith("Un satélite artificial da una vuelta a la Tierra cada 90 minutos. ¿Cuántas vueltas da en un día de 1.440 minutos?", "1440/90", "Se divide el tiempo total por la duración de una vuelta.", " vueltas"),
      ("Un cuerpo de ejemplo es una esfera casi perfecta de 1.000 km y otro es irregular de 20 km. ¿Cuál tiene más probablemente una gran masa?", "La esfera de 1.000 km", "La gravedad de una gran masa redondea el cuerpo."),
  ],
  context=[arith("Una persona cuenta 12 meteoros en 20 minutos durante una lluvia de meteoros. Con el mismo ritmo, ¿cuántos esperaría contar en 1 hora?", "12*3", "Una hora tiene tres períodos de 20 minutos.", " meteoros")],
  selfcheck=[("¿Cuál es la diferencia entre meteoro y meteorito?", "El meteoro es el trazo luminoso y el meteorito es el fragmento que llega al suelo", "Son un fenómeno y un objeto distintos."), ("¿De qué está hecho un cometa?", "De hielo, polvo y roca", "Por eso forma cola al calentarse."), ("¿Qué es un satélite artificial?", "Un cuerpo construido por las personas que orbita otro", "Se usa para comunicaciones y observación.")],
  open_task=task("Clasifica estos cuerpos con una palabra de la lección y justifica con un criterio de tamaño, forma o posición: (1) fragmento de 2 cm que deja un destello al entrar en la atmósfera; (2) roca irregular de 500 m en el cinturón de asteroides; (3) cuerpo de hielo de 8 km con cola cuando pasa cerca del Sol; (4) esfera de 3.500 km que orbita la Tierra; (5) esfera de 12.700 km que orbita el Sol y ha despejado su órbita; (6) aparato construido por personas que orbita la Tierra cada 90 minutos.", "1 meteoroide (el destello es un meteoro); 2 asteroide; 3 cometa; 4 satélite natural, la Luna; 5 planeta, la Tierra; 6 satélite artificial. Criterios: tamaño, forma esférica por gravedad y posición del cinturón.", ["seis clasificaciones correctas", "un criterio para cada una", "distingue meteoro y meteoroide"], ["tabla de seis filas con criterio"], ["llamar planeta a la Luna", "no distinguir fenómeno de objeto"], "Pregunta cuál cuerpo de la lista es el mayor y cuál el menor."),
  reinforce="Escribe una frase que distinga un asteroide de un cometa.",
  extend="Explica por qué un planeta enano no es lo mismo que un asteroide grande.")

L(OA, 3,
  materials="Este cuaderno, lápiz y calculadora. Los datos de estrellas son aproximados y de ejemplo, escritos en los ejercicios.",
  use="Aprenderé a relacionar el color, la temperatura, la masa y la magnitud de las estrellas. Sirve para interpretar el color y el brillo que ves en el cielo.",
  prior=["Sé que el Sol es una estrella.", "Sé que el color de la luz se relaciona con su longitud de onda."],
  explain=[
      "Una estrella es una esfera de gas que emite luz propia porque en su núcleo ocurre fusión nuclear. El color de una estrella depende de su temperatura superficial: las rojas son las más frías, con unos 3.000 °C; las amarillas, como el Sol, tienen unos 5.500 °C; las blancas, unos 10.000 °C; y las azules son las más calientes, con más de 20.000 °C.",
      "La masa de una estrella se compara con la del Sol. Una estrella azul puede tener 20 veces la masa del Sol y una roja pequeña, una fracción de ella. En general, mientras más masa tiene una estrella, más alta es su temperatura, más luz emite y menos tiempo vive.",
      "El brillo que vemos se mide con la magnitud aparente: mientras menor es el número, más brillante se ve la estrella. Una diferencia de 5 magnitudes equivale a 100 veces en brillo. A simple vista se ven estrellas hasta la magnitud 6 en un cielo muy oscuro. El brillo aparente depende de la luz que emite la estrella y de su distancia: una estrella débil cercana puede verse más brillante que una potente muy lejana.",
  ],
  vocab=[("fusión nuclear", "proceso en que núcleos se unen y liberan energía, como en el núcleo de las estrellas"), ("temperatura superficial", "temperatura de la capa externa visible de una estrella"), ("masa solar", "unidad que compara una masa con la del Sol"), ("magnitud aparente", "medida del brillo con que vemos una estrella desde la Tierra"), ("luminosidad", "cantidad de luz que emite una estrella por segundo"), ("estrella", "esfera de gas que emite luz propia por fusión nuclear")],
  worked=[
      ("Color y temperatura", "Una estrella A es azul y una estrella B es roja. ¿Cuál es más caliente?", ["El color azul corresponde a temperaturas más altas.", "El color rojo corresponde a temperaturas más bajas."], "La estrella azul"),
      ("Diferencia de magnitudes", "Una estrella tiene magnitud 1 y otra magnitud 6. ¿Cuántas veces más brillante se ve la primera?", ["La diferencia es de 5 magnitudes.", "Cada 5 magnitudes equivalen a 100 veces en brillo."], "100 veces"),
  ],
  mistakes=[
      ("Creer que las estrellas rojas son las más calientes porque el rojo se asocia al fuego.", "Entre las estrellas, las rojas son las más frías y las azules las más calientes.", "Asocia el color con la temperatura superficial."),
      ("Pensar que la estrella que se ve más brillante es siempre la que emite más luz.", "El brillo que vemos depende también de la distancia.", "Distingue magnitud aparente y luminosidad."),
  ],
  rec=[
      ("¿Qué color tienen las estrellas más calientes?", "Azul", "Su temperatura supera los 20.000 °C."),
      ("¿Cuál se ve más brillante: una estrella de magnitud 2 o una de magnitud 4?", "La de magnitud 2", "Mientras menor es la magnitud, mayor es el brillo."),
      ("Verdadero o falso: el Sol es una estrella.", "Verdadero", "Emite luz propia por fusión nuclear."),
  ],
  und=[
      ("Una estrella tiene unos 3.000 °C en su superficie. Su color será: A) rojizo B) azulado", "A", "Las estrellas más frías son rojizas."),
      ("Dos estrellas emiten la misma luz, pero B está 10 veces más lejos. ¿Cómo se ve B? A) Más débil que A B) Más brillante que A", "A", "A mayor distancia, el brillo aparente disminuye."),
      ("Una magnitud de −1 comparada con una de 3, ¿es más brillante o más débil?", "Más brillante", "Menor número significa mayor brillo."),
  ],
  app=[
      arith("Cada 5 magnitudes de diferencia equivalen a 100 veces en brillo. ¿Cuántas veces más brillante se ve una estrella de magnitud 1 que una de magnitud 11?", "100*100", "Hay 10 magnitudes de diferencia, es decir, dos tramos de 5.", " veces"),
      arith("Una estrella azul tiene 20 veces la masa del Sol y una estrella blanca tiene 2 veces la masa del Sol. ¿Cuántas veces mayor es la masa de la azul?", "20/2", "Se divide la masa mayor por la menor.", " veces"),
      ("Cuatro estrellas de ejemplo tienen estas temperaturas superficiales: A, 3.000 °C; B, 5.500 °C; C, 12.000 °C; D, 25.000 °C. ¿Cuál se ve más azulada?", "La D", "A mayor temperatura, color más azulado."),
  ],
  rea=[
      ("Un estudiante dice: «La estrella X se ve más brillante que la Y, así que emite más luz». ¿Qué respuesta es correcta? A) No necesariamente: X puede estar más cerca B) Sí, el brillo aparente mide la luz emitida", "A", "La distancia también influye en el brillo que vemos."),
      ("Una estrella roja gigante es muy luminosa aunque su superficie es fría. ¿Cómo es posible? A) Tiene una superficie enorme, así que emite mucha luz en total B) Su color rojo indica gran temperatura", "A", "La luz total depende de la temperatura y del tamaño de la superficie."),
  ],
  cha=[
      ("Una estrella X tiene magnitud −1 y otra Y tiene magnitud 4. ¿Cuál se ve más brillante y cuántas veces?", "La X, 100 veces", "Hay 5 magnitudes de diferencia."),
      arith("El Sol tiene unos 5.500 °C en su superficie y una estrella azul de ejemplo, 25.000 °C. ¿Cuántos grados más caliente es la estrella azul?", "25000-5500", "Se resta la temperatura del Sol a la de la estrella azul.", " °C"),
  ],
  context=[arith("En el campo se ven estrellas hasta la magnitud 6, pero en la ciudad, por el exceso de luz, solo hasta la magnitud 3. ¿Cuántas magnitudes menos se alcanzan a ver en la ciudad?", "6-3", "Se restan las magnitudes límite.", " magnitudes")],
  selfcheck=[("¿Qué color tienen las estrellas más frías?", "Rojas", "Su temperatura superficial es la menor."), ("¿Qué significa una magnitud aparente menor?", "Que la estrella se ve más brillante", "Se mide al revés que una escala común."), ("¿De qué depende el brillo aparente?", "De la luz emitida y de la distancia", "Una estrella cercana puede verse más brillante.")],
  open_task=task("Datos de ejemplo de cuatro estrellas: A, color rojo, 3.500 °C, magnitud aparente 1; B, color blanco, 10.000 °C, magnitud aparente 3; C, color azul, 25.000 °C, magnitud aparente 2; D, color amarillo, 5.500 °C, magnitud aparente 5. Ordénalas de mayor a menor temperatura y de mayor a menor brillo aparente. Explica por qué la más fría puede ser la que se ve más brillante.", "Temperatura: C, B, D, A. Brillo aparente: A (magnitud 1), C, B, D. A puede verse más brillante aunque sea fría porque puede estar muy cerca de nosotros o ser muy grande.", ["orden por temperatura", "orden por brillo con magnitud menor primero", "dos razones posibles"], ["dos listas y una explicación"], ["ordenar el brillo con la magnitud mayor primero", "asociar el rojo con mayor temperatura"], "Pregunta qué dato necesitarías para saber cuál emite más luz."),
  reinforce="Escribe el color que corresponde a las temperaturas 3.000 °C, 5.500 °C y 25.000 °C.",
  extend="Explica por qué una estrella más masiva vive menos tiempo que una de poca masa.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Los datos de tamaños y distancias son aproximados y están en los ejercicios.",
  use="Aprenderé qué son las nebulosas, las galaxias y los cúmulos de galaxias y cómo se diferencian por tamaño y forma. Sirve para ubicarnos en el universo.",
  prior=["Sé qué es una estrella y qué es el año luz.", "Sé que la gravedad une la materia."],
  explain=[
      "Una nebulosa es una nube de gas y polvo en el espacio, formada sobre todo por hidrógeno. Algunas son cunas de estrellas: la gravedad junta el gas y el polvo hasta formar nuevas estrellas. Otras son restos de estrellas que murieron. Pueden medir decenas de años luz.",
      "Una galaxia es un conjunto enorme de estrellas, gas y polvo unido por la gravedad. Pueden ser espirales, con brazos en forma de remolino; elípticas, de forma ovalada y sin brazos; o irregulares, sin forma definida. Nuestra galaxia, la Vía Láctea, es una espiral con barra central de unos 100.000 años luz de diámetro; el Sistema Solar está en uno de sus brazos, a unos 26.000 años luz del centro. Desde un cielo oscuro se ve como una franja pálida, que es el disco de la galaxia visto desde dentro. Las Nubes de Magallanes son dos pequeñas galaxias vecinas que se ven a simple vista desde el hemisferio sur.",
      "Un cúmulo de galaxias es un grupo de galaxias unidas por la gravedad, desde decenas hasta miles de galaxias. La Vía Láctea forma parte del Grupo Local, junto con Andrómeda, que está a unos 2.500.000 años luz, y decenas de galaxias más pequeñas. A mayor escala, los cúmulos se organizan en estructuras todavía mayores.",
  ],
  vocab=[("nebulosa", "nube de gas y polvo en el espacio"), ("galaxia", "conjunto de estrellas, gas y polvo unido por la gravedad"), ("galaxia espiral", "galaxia con brazos en forma de remolino"), ("galaxia elíptica", "galaxia de forma ovalada y sin brazos"), ("cúmulo de galaxias", "grupo de galaxias unidas por la gravedad"), ("Grupo Local", "cúmulo de galaxias al que pertenece la Vía Láctea")],
  worked=[
      ("Clasificar", "Una nube de gas y polvo donde la gravedad está formando nuevas estrellas. ¿Qué es?", ["Es una nube de gas y polvo.", "Si forma estrellas, es una cuna de estrellas."], "Una nebulosa"),
      ("Distancia al borde", "El radio de la Vía Láctea es de unos 50.000 años luz y el Sol está a unos 26.000 años luz del centro. ¿A qué distancia del borde está el Sol?", ["Resto la distancia al centro del radio.", "Calculo 50.000 − 26.000."], "24.000 años luz"),
  ],
  mistakes=[
      ("Creer que la Vía Láctea es todo el universo.", "Es solo una galaxia entre miles de millones.", "Recuerda que existen muchas galaxias."),
      ("Confundir una galaxia con una nebulosa.", "La galaxia contiene miles de millones de estrellas; la nebulosa es una nube de gas y polvo.", "Compara el tamaño y el contenido."),
  ],
  rec=[
      ("¿En qué galaxia está el Sistema Solar?", "En la Vía Láctea", "Es nuestra galaxia."),
      ("¿Cómo se llama el cúmulo de galaxias que incluye a la Vía Láctea y a Andrómeda?", "Grupo Local", "Es nuestro cúmulo."),
      ("Verdadero o falso: una nebulosa es una nube de gas y polvo.", "Verdadero", "Es su definición."),
  ],
  und=[
      ("¿Qué forma tiene la Vía Láctea?", "Espiral con barra central", "Tiene brazos y una barra en el centro."),
      ("Una nebulosa se llama cuna de estrellas porque: A) la gravedad junta su gas y polvo y forma estrellas B) las estrellas viejas se enfrían en ella", "A", "De la nube nacen estrellas nuevas."),
      ("¿Qué contiene un cúmulo de galaxias?", "Muchas galaxias unidas por la gravedad", "Pueden ser decenas o miles."),
  ],
  app=[
      arith("La Vía Láctea mide unos 100.000 años luz de diámetro y la Gran Nube de Magallanes está a unos 160.000 años luz. ¿Cuántos años luz más que ese diámetro hay hasta la Nube?", "160000-100000", "Se resta el diámetro a la distancia.", " años luz"),
      ("Una galaxia de forma ovalada, sin brazos y con estrellas viejas rojizas. ¿Qué tipo es?", "Elíptica", "Las elípticas son ovaladas y sin brazos."),
      arith("Un grupo de ejemplo tiene 30 galaxias y cada una tiene 50 mil millones de estrellas. ¿Cuántos miles de millones de estrellas hay en total?", "30*50", "Se multiplica el número de galaxias por las estrellas de cada una.", " miles de millones"),
  ],
  rea=[
      ("Alguien dice que la Vía Láctea es el conjunto de todas las estrellas del universo. ¿Cuál es la corrección? A) Es solo nuestra galaxia; hay miles de millones de galaxias B) Es correcto, no existen otras galaxias", "A", "Hay muchas más galaxias."),
      ("En un cielo oscuro ves una franja pálida de lado a lado. ¿Qué es? A) El disco de la Vía Láctea visto desde dentro B) Una nube de la atmósfera", "A", "Vemos millones de estrellas lejanas del disco de nuestra galaxia."),
  ],
  cha=[
      ("Una galaxia espiral tiene mucho gas y polvo y una elíptica casi no. ¿En cuál se forman más estrellas nuevas?", "En la espiral", "Se necesita gas y polvo para formar estrellas."),
      arith("Las Nubes de Magallanes están a unos 160.000 años luz y Andrómeda a unos 2.500.000 años luz. ¿Cuántas veces más lejos está Andrómeda, con la parte entera?", "2500000//160000", "Se divide la distancia a Andrómeda por la de las Nubes.", " veces"),
  ],
  context=[ex("Un observatorio de ejemplo registra tres galaxias: A, espiral de 100.000 años luz de diámetro; B, elíptica de 200.000; C, irregular de 30.000. ¿Cuál es la mayor?", "La B", "Su diámetro, 200.000 años luz, es el mayor.")],
  selfcheck=[("¿Qué es una galaxia?", "Un conjunto de estrellas, gas y polvo unido por la gravedad", "Contiene miles de millones de estrellas."), ("¿Qué son las Nubes de Magallanes?", "Dos pequeñas galaxias vecinas", "Se ven a simple vista desde el hemisferio sur."), ("¿Qué es un cúmulo de galaxias?", "Un grupo de galaxias unidas por la gravedad", "El Grupo Local es el nuestro.")],
  open_task=task("Completa una tabla con tres columnas (nebulosa, galaxia y cúmulo de galaxias) y estas filas: qué es, de qué está hecha, tamaño aproximado y un ejemplo. Usa estos datos: nebulosa, decenas de años luz; Vía Láctea, 100.000 años luz; Grupo Local, unos 10 millones de años luz; Sistema Solar hasta la órbita de Neptuno, menos de 0,001 años luz. Luego ordena de menor a mayor: nebulosa, Sistema Solar, Vía Láctea y Grupo Local.", "Nebulosa: nube de gas y polvo, decenas de años luz, nebulosa de formación de estrellas. Galaxia: estrellas, gas y polvo unidos por la gravedad, 100.000 años luz, Vía Láctea. Cúmulo: galaxias unidas por la gravedad, unos 10 millones de años luz, Grupo Local. Orden: Sistema Solar, nebulosa, Vía Láctea, Grupo Local.", ["tabla completa", "orden correcto", "usa los datos de tamaño"], ["tabla y lista ordenada"], ["poner el Sistema Solar después de la nebulosa", "confundir galaxia y nebulosa"], "Pregunta qué hay más allá del Grupo Local."),
  reinforce="Escribe los tres tipos de galaxias y una característica de cada uno.",
  extend="Explica por qué se dice que las nebulosas son parte del ciclo de vida de las estrellas.")

L(OA, 5,
  materials="Este cuaderno, lápiz y calculadora. La tabla de estrellas es de ejemplo y está escrita en el texto y en los ejercicios.",
  use="Aprenderé a comparar estructuras cósmicas con una ficha de datos y a explicar patrones entre color, temperatura, masa y distancia. Sirve para sacar conclusiones con evidencia.",
  prior=["Sé las unidades astronómicas y las propiedades de las estrellas.", "Sé leer una tabla y comparar sus filas."],
  explain=[
      "Para comparar estructuras cósmicas se usan propiedades que se pueden medir: tamaño, forma, posición, temperatura, masa, color y magnitud. Una ficha de datos reúne estas propiedades y permite buscar patrones. Datos de ejemplo de cinco estrellas (color, temperatura superficial, masa en veces la masa del Sol): roja, 3.000 °C, 0,2; amarilla, 5.500 °C, 1; blanca, 9.000 °C, 2; blanco-azulada, 15.000 °C, 5; azul, 30.000 °C, 20.",
      "En la tabla aparece un patrón: a mayor masa, mayor temperatura y color más azulado. También se sabe que las estrellas masivas gastan su combustible más rápido: una estrella de 5 masas solares vive del orden de 100 millones de años, mientras que el Sol vive del orden de 10.000 millones de años (valores de ejemplo). Un patrón en una tabla pequeña es una pista, no una prueba: se confirma con muchos más datos.",
      "Un tercer aspecto es la posición. Como la luz tarda en llegar, la distancia es también una distancia en el tiempo: una estrella a 100 años luz se ve como era hace 100 años. Si una estrella dejara de existir hoy, la seguiríamos viendo mientras llegue la última luz que emitió.",
  ],
  vocab=[("ficha de datos", "tabla con propiedades medidas de un objeto"), ("patrón", "regularidad que se repite en los datos"), ("secuencia", "serie ordenada de datos o casos"), ("masa solar", "unidad que compara una masa con la del Sol"), ("evidencia", "dato que apoya o contradice una explicación"), ("distancia en el tiempo", "años que tarda la luz en llegar desde un objeto")],
  worked=[
      ("Buscar un patrón", "Con la tabla, ¿cómo cambia la temperatura cuando la masa aumenta?", ["Miro las masas: 0,2; 1; 2; 5; 20.", "Las temperaturas son 3.000; 5.500; 9.000; 15.000; 30.000 °C: también aumentan."], "A mayor masa, mayor temperatura"),
      ("Luz del pasado", "Una estrella está a 20 años luz. Si hoy explota, ¿cuándo veremos la explosión?", ["La luz tarda 20 años en recorrer 20 años luz.", "La veremos 20 años después."], "Dentro de 20 años"),
  ],
  mistakes=[
      ("Concluir una regla general con solo uno o dos casos.", "Un patrón en una tabla pequeña es una pista que debe confirmarse con más datos.", "Declara siempre cuántos casos usaste."),
      ("Creer que una estrella que vemos hoy existe tal cual.", "Su luz salió hace años y podría haber cambiado.", "Resta el tiempo que tardó la luz."),
  ],
  rec=[
      ("¿Qué color tiene la estrella de 30.000 °C de la tabla?", "Azul", "Es la más caliente de la ficha."),
      ("Verdadero o falso: según la tabla, la estrella de mayor masa es la de mayor temperatura.", "Verdadero", "La de 20 masas solares tiene 30.000 °C."),
      ("¿Qué mide la magnitud aparente?", "El brillo con que vemos una estrella desde la Tierra", "No mide la luz total emitida."),
  ],
  und=[
      ("Según la tabla, ¿qué estrella tiene la mayor masa?", "La azul de 20 masas solares", "Es el valor mayor de la columna de masa."),
      ("El patrón de la tabla es que, a mayor masa, la temperatura: A) aumenta B) disminuye", "A", "Las dos columnas crecen juntas."),
      ("Una estrella está a 100 años luz. ¿Cómo la vemos hoy?", "Como era hace 100 años", "La luz tardó 100 años en llegar."),
  ],
  app=[
      arith("La estrella azul de la tabla tiene 30.000 °C y la roja, 3.000 °C. ¿Cuántos grados más caliente es la azul?", "30000-3000", "Se resta la temperatura menor a la mayor.", " °C"),
      arith("Una estrella de 5 masas solares vive unos 100 millones de años y el Sol unos 10.000 millones (valores de ejemplo). ¿Cuántas veces más vive el Sol?", "10000/100", "Se divide la vida del Sol por la de la estrella masiva.", " veces"),
      ("Con la tabla, ¿qué color esperas en una estrella de 3 masas solares (entre las de 2 y 5)? A) Blanca B) Roja", "A", "Su temperatura estaría entre 9.000 y 15.000 °C."),
  ],
  rea=[
      ("Dos estrellas se ven con el mismo brillo, pero una está a 10 años luz y la otra a 100 años luz. ¿Cuál emite más luz? A) La que está a 100 años luz B) La que está a 10 años luz", "A", "Para verse igual estando más lejos, debe emitir más luz."),
      ("Alguien dice que una estrella a 5 años luz que desapareció hoy ya no se ve. ¿Qué respuesta es correcta? A) Aún la veremos durante 5 años, hasta que llegue su última luz B) Deja de verse al instante", "A", "La luz emitida antes sigue viajando."),
  ],
  cha=[
      arith("La estrella de 20 masas solares tiene 4 veces la masa de otra. ¿Cuántas masas solares tiene la otra?", "20/4", "Se divide la masa mayor por 4.", " masas solares"),
      ("Una estrella A es roja, de magnitud 1, y una estrella B es azul, de magnitud 3. ¿Cuál es más caliente y cuál se ve más brillante?", "B es más caliente y A se ve más brillante", "El color indica la temperatura y la menor magnitud indica mayor brillo."),
  ],
  context=[ex("Una persona observa dos estrellas con la misma magnitud aparente: una anaranjada y otra azulada. ¿Cuál tiene mayor temperatura superficial?", "La azulada", "El color azul corresponde a mayor temperatura.")],
  selfcheck=[("¿Qué patrón hay entre masa y temperatura en la tabla?", "A mayor masa, mayor temperatura", "Las dos columnas crecen juntas."), ("¿Por qué ver lejos es ver el pasado?", "Porque la luz tarda en llegar", "Lo que vemos salió hace años."), ("¿Por qué un patrón de cinco casos es solo una pista?", "Porque se necesitan más datos para confirmarlo", "Pocos casos pueden no representar a todos.")],
  open_task=task("Completa una ficha comparativa con estos datos de ejemplo: meteoroide, 1 m, en la atmósfera terrestre; asteroide, 100 km, a 2,7 UA del Sol; Júpiter, 140.000 km, a 5 UA; Sol, 1.400.000 km, centro del sistema solar; Vía Láctea, 100.000 años luz, en el Grupo Local. Ordena de menor a mayor tamaño y escribe una frase que compare dos objetos con un número (por ejemplo, cuántas veces mayor es uno que otro). Añade una frase que explique qué pasado vemos de una estrella a 40 años luz.", "Orden: meteoroide, asteroide, Júpiter, Sol, Vía Láctea. Comparación: el Sol (1.400.000 km) es unas 10 veces mayor que Júpiter (140.000 km). De una estrella a 40 años luz vemos cómo era hace 40 años.", ["orden correcto", "comparación con un número", "explicación del pasado de la luz"], ["ficha ordenada y dos frases"], ["comparar sin unidades", "decir que vemos la estrella como es hoy"], "Pregunta qué propiedad de la ficha usarías para saber la edad de un objeto."),
  reinforce="Escribe dos propiedades que usarías para comparar una estrella y un planeta.",
  extend="Explica por qué se necesitan muchos datos para confirmar un patrón cósmico.")

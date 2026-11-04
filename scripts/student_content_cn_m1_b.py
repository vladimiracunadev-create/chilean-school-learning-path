"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 11 (luz, modelos, imágenes y color)."""
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


OA = "CN1M OA 11"

L(OA, 1,
  materials="Este cuaderno, lápiz, regla y calculadora. Si quieres comprobar la sombra, usa la linterna de un celular lejos de los ojos y un objeto pequeño; todos los datos de los ejercicios están escritos.",
  use="Aprenderé cómo viaja la luz, cómo se forman las sombras y qué tan rápida es. Sirve para predecir el tamaño de una sombra y para entender distancias en el espacio.",
  prior=["Sé que la luz es una forma de energía que nos permite ver.", "Sé usar proporciones y calcular una rapidez como distancia dividida por tiempo."],
  explain=[
      "La luz se propaga en línea recta mientras viaja por un medio uniforme, como el aire. Por eso un rayo de luz se dibuja como una línea con una flecha que indica hacia dónde va. Una fuente luminosa, como el Sol o una ampolleta, emite luz propia. Un objeto iluminado, como la Luna o este cuaderno, solo refleja la luz que recibe, y lo vemos cuando esa luz llega a nuestros ojos.",
      "Un objeto opaco no deja pasar la luz; uno transparente la deja pasar casi completa; uno translúcido deja pasar una parte sin que se vea nítido lo que hay detrás. Detrás de un objeto opaco se forma una sombra, una zona a la que no llega luz directa de la fuente. Con una fuente pequeña, el tamaño de la sombra es igual al tamaño del objeto multiplicado por la distancia fuente–pantalla y dividido por la distancia fuente–objeto. Con una fuente grande, el borde queda difuso y se llama penumbra.",
      "La luz tiene una rapidez finita: en el vacío es de unos 300.000 km por segundo, y nada conocido va más rápido. Como la rapidez es distancia dividida por tiempo, el tiempo de viaje se calcula dividiendo la distancia por la rapidez. La luz del Sol recorre unos 150.000.000 km hasta la Tierra, y por eso vemos el Sol como era hace unos 500 segundos.",
  ],
  vocab=[("rayo de luz", "línea con flecha que representa la dirección en que viaja la luz"), ("opaco", "material que no deja pasar la luz"), ("translúcido", "material que deja pasar parte de la luz sin imagen nítida"), ("sombra", "zona sin luz directa detrás de un objeto opaco"), ("penumbra", "zona de sombra con borde difuso, que forma una fuente de luz grande"), ("rapidez de la luz", "distancia que recorre la luz en cada segundo: unos 300.000 km/s en el vacío")],
  worked=[
      ("Tamaño de una sombra", "Un objeto de 4 cm de alto está a 20 cm de una lámpara pequeña. La pantalla está a 60 cm de la lámpara. ¿Cuánto mide la sombra?", ["Escribo la regla: sombra = objeto × distancia lámpara–pantalla ÷ distancia lámpara–objeto.", "Reemplazo: 4 × 60 ÷ 20.", "Calculo: 240 ÷ 20 = 12."], "12 cm"),
      ("Tiempo de viaje de la luz", "Un destello recorre 600.000 km en el vacío. ¿Cuánto tarda?", ["Uso tiempo = distancia ÷ rapidez.", "Reemplazo: 600.000 km ÷ 300.000 km/s.", "Calculo: 2."], "2 s"),
  ],
  mistakes=[
      ("Pensar que vemos porque los ojos lanzan rayos hacia los objetos.", "Vemos cuando la luz emitida o reflejada por el objeto entra a los ojos; en una pieza totalmente oscura no se ve nada.", "Dibuja siempre la flecha del rayo desde la fuente o el objeto hacia el ojo."),
      ("Creer que la luz llega de forma instantánea.", "La luz tiene rapidez finita; en distancias astronómicas el tiempo de viaje se nota.", "Calcula el tiempo con distancia ÷ rapidez."),
  ],
  rec=[
      ("¿Cómo se propaga la luz en un medio uniforme como el aire?", "En línea recta", "La luz mantiene su dirección mientras el medio no cambie."),
      ("Verdadero o falso: la Luna es una fuente luminosa porque emite luz propia.", "Falso", "La Luna solo refleja la luz del Sol."),
      ("Un material que no deja pasar la luz se llama ______ (opaco o transparente).", "Opaco", "El material opaco bloquea la luz y forma sombra."),
  ],
  und=[
      ("Una pelota se ilumina primero con una ampolleta pequeña y luego con un tubo fluorescente largo. ¿Con cuál se forma una penumbra más ancha? A) Con el tubo largo B) Con la ampolleta pequeña", "A", "Una fuente extensa envía luz desde muchos puntos y deja bordes difusos."),
      ("En un dibujo, la flecha de un rayo de luz indica: A) la dirección en que se propaga la luz B) el color que tiene la luz", "A", "La flecha muestra hacia dónde viaja la luz."),
      ("Ordena de menos a más luz que dejan pasar: vidrio limpio, cuaderno, papel mantequilla.", "cuaderno, papel mantequilla, vidrio limpio", "El cuaderno es opaco, el papel es translúcido y el vidrio limpio es transparente."),
  ],
  app=[
      arith("Un objeto de 2 cm está a 10 cm de una lámpara pequeña. La pantalla está a 50 cm de la lámpara. ¿Cuántos centímetros mide la sombra?", "2*50/10", "Se multiplica el tamaño por la distancia a la pantalla y se divide por la distancia al objeto.", " cm"),
      arith("La distancia entre el Sol y la Tierra es de 150.000.000 km y la luz viaja a 300.000 km/s. ¿Cuántos segundos tarda la luz del Sol en llegar a la Tierra?", "150000000/300000", "El tiempo se obtiene dividiendo la distancia por la rapidez.", " s"),
      arith("Un objeto de 5 cm ahora está a 10 cm de una lámpara pequeña y la pantalla sigue a 50 cm de la lámpara. ¿Cuántos centímetros mide su sombra?", "5*50/10", "Al acercar el objeto a la lámpara, la sombra crece según la misma relación.", " cm"),
  ],
  rea=[
      ("Ana dice que vemos porque los ojos emiten rayos hacia el objeto. Julián dice que vemos porque la luz del objeto llega al ojo. ¿Quién tiene el modelo correcto? A) Julián B) Ana", "A", "En un cuarto totalmente oscuro no vemos nada: hace falta luz que llegue al ojo."),
      ("Tienes linterna, cartulina y regla. ¿Cuál es una pregunta investigable? A) ¿Cómo cambia el ancho de la sombra al alejar la cartulina de la linterna? B) ¿Es más bonita una sombra grande que una pequeña?", "A", "Se puede medir el ancho de la sombra; la belleza es opinión."),
  ],
  cha=[
      arith("Un objeto de 3 cm produce una sombra de 18 cm en una pantalla que está a 90 cm de la lámpara. ¿A cuántos centímetros de la lámpara está el objeto?", "3*90/18", "Se despeja la distancia lámpara–objeto de la misma regla de proporción.", " cm"),
      arith("Un relámpago se ve casi al instante y el trueno llega 3 segundos después. Si el sonido viaja a 340 m/s, ¿a cuántos metros ocurrió el relámpago?", "340*3", "La luz llega casi sin demora, así que el tiempo medido es el que tarda el sonido: distancia = rapidez × tiempo.", " m"),
  ],
  context=[ex("Para un teatro de sombras, un títere de 10 cm debe proyectar una sombra de 30 cm en una pantalla que está a 60 cm de la lámpara. ¿A cuántos centímetros de la lámpara debes poner el títere?", "20 cm", "De 30 = 10 × 60 ÷ d resulta d = 10 × 60 ÷ 30 = 20.", "10*60/30")],
  selfcheck=[("¿Qué es una sombra?", "Una zona detrás de un objeto opaco a la que no llega luz directa de la fuente", "Se forma porque la luz viaja en línea recta y el objeto la bloquea."), ("¿Qué rapidez tiene la luz en el vacío?", "Unos 300.000 km/s", "Es una rapidez muy grande pero finita."), ("¿Qué pasa con la sombra si acercas el objeto a la lámpara?", "Crece", "Menor distancia lámpara–objeto da mayor tamaño de sombra.")],
  open_task=task("Otro grupo midió la sombra de un objeto de 4 cm con una pantalla fija a 60 cm de la lámpara. Distancia lámpara–objeto: 10 cm, 20 cm y 40 cm; sombras: 24 cm, 12 cm y 6 cm. Arma una tabla, describe cómo cambia la sombra al alejar el objeto de la lámpara, predice la sombra a 30 cm y explica el resultado con un dibujo de rayos. Si tienes linterna, repite una medición.", "A 30 cm: 4 × 60 ÷ 30 = 8 cm. Al alejar el objeto de la lámpara la sombra disminuye, porque los rayos que pasan por los bordes del objeto se abren menos. Dibujo: dos líneas rectas desde la lámpara pasan por los extremos del objeto y llegan a la pantalla.", ["tabla con las tres mediciones", "describe que la sombra disminuye al alejar el objeto", "predice 8 cm con el cálculo", "dibujo con rayos rectos"], ["tabla y predicción escritas", "dibujo de rayos"], ["decir que la sombra aumenta al alejar el objeto de la lámpara", "dibujar rayos curvos", "predecir sin hacer el cálculo"], "Pregunta qué medición cambiarías para comprobar tu predicción y qué dato nuevo necesitarías."),
  reinforce="Calcula la sombra de un objeto de 6 cm que está a 30 cm de la lámpara, con la pantalla a 90 cm de ella.",
  extend="Explica por qué el tiempo que tarda la luz en llegar desde un astro permite hablar de «ver el pasado».")

L(OA, 2,
  materials="Este cuaderno, lápiz, regla y transportador. Si tienes un espejo pequeño sin bordes filosos, puedes comprobar la reflexión con la linterna de un celular lejos de los ojos; todos los datos están escritos.",
  use="Aprenderé la ley de la reflexión y cómo los espejos forman imágenes. Sirve para entender espejos retrovisores, linternas y telescopios.",
  prior=["Sé que la luz viaja en línea recta.", "Sé medir ángulos con transportador."],
  explain=[
      "La reflexión ocurre cuando la luz rebota al chocar con una superficie. La ley de la reflexión dice que el ángulo de incidencia es igual al ángulo de reflexión. Ambos se miden respecto de la normal, que es una línea imaginaria perpendicular a la superficie en el punto donde llega el rayo. Una superficie lisa, como un espejo, produce reflexión regular; una superficie rugosa, como una hoja de papel, produce reflexión difusa y por eso la vemos desde cualquier lado.",
      "En un espejo plano, la imagen es virtual: parece estar detrás del espejo, aunque ahí no llega luz real. Tiene el mismo tamaño que el objeto, es derecha y está a la misma distancia detrás del espejo que el objeto delante de él. El espejo no cambia izquierda por derecha: tu mano derecha y la de tu imagen quedan del mismo lado. Lo que se invierte es adelante–atrás, y por eso la imagen parece mirarte.",
      "Un espejo curvo cambia la forma de la imagen. El espejo cóncavo, como la parte interior de una cuchara, hace converger los rayos paralelos en un punto llamado foco. Se usa en linternas, espejos de maquillaje y telescopios reflectores. El espejo convexo, como la parte exterior de la cuchara, hace divergir los rayos y entrega imágenes pequeñas de una zona amplia; se usa en espejos retrovisores y en espejos de seguridad en esquinas.",
  ],
  vocab=[("reflexión", "rebote de la luz al chocar con una superficie"), ("normal", "línea perpendicular a la superficie en el punto de incidencia"), ("imagen virtual", "imagen que parece estar donde no llega luz real"), ("espejo cóncavo", "espejo curvo que hace converger los rayos paralelos"), ("espejo convexo", "espejo curvo que hace divergir los rayos"), ("foco", "punto donde se juntan los rayos paralelos reflejados por un espejo cóncavo")],
  worked=[
      ("Ángulos de reflexión", "Un rayo llega a un espejo plano con 35° respecto de la normal. ¿Cuánto mide el ángulo entre el rayo incidente y el reflejado?", ["El ángulo de reflexión es igual al de incidencia: 35°.", "El ángulo entre ambos rayos es la suma 35° + 35°.", "Calculo: 70°."], "70°"),
      ("Distancia a la imagen", "Una persona está a 2 m de un espejo plano. ¿A qué distancia está de su imagen?", ["La imagen queda a 2 m detrás del espejo.", "Sumo la distancia al espejo y la distancia de la imagen: 2 + 2."], "4 m"),
  ],
  mistakes=[
      ("Medir el ángulo de incidencia con la superficie del espejo.", "La ley de la reflexión usa la normal, no la superficie.", "Dibuja primero la normal y mide desde ella."),
      ("Creer que el espejo plano cambia izquierda por derecha.", "El espejo invierte adelante–atrás; tu mano derecha y la de tu imagen quedan del mismo lado.", "Verifica con la mano: levanta la derecha y mira de qué lado queda la mano de tu imagen."),
  ],
  rec=[
      ("Si el ángulo de incidencia mide 20°, ¿cuánto mide el ángulo de reflexión?", "20°", "Según la ley de la reflexión ambos ángulos son iguales."),
      ("¿Con respecto a qué línea se miden los ángulos de incidencia y reflexión?", "La normal", "La normal es perpendicular a la superficie."),
      ("Verdadero o falso: una pared rugosa produce reflexión difusa.", "Verdadero", "Las irregularidades envían la luz en muchas direcciones."),
  ],
  und=[
      ("Una hoja de papel se ve desde cualquier lado, pero un espejo plano no. ¿Por qué? A) El papel refleja la luz de forma difusa B) El papel absorbe toda la luz", "A", "La superficie rugosa dispersa la luz en muchas direcciones."),
      ("La imagen que ves en un espejo plano es: A) virtual B) real y formada sobre la superficie del espejo", "A", "La luz no pasa por el lugar donde parece estar la imagen."),
      ("Quieres ver una zona amplia de un pasillo desde una esquina. ¿Qué espejo usas: cóncavo o convexo?", "Convexo", "El espejo convexo hace divergir los rayos y abarca una zona más amplia."),
  ],
  app=[
      arith("Un rayo llega a un espejo plano y forma 40° con la normal. ¿Cuántos grados mide el ángulo entre el rayo incidente y el rayo reflejado?", "40*2", "Los dos ángulos son iguales, así que el ángulo entre rayos es el doble.", "°"),
      arith("Una persona está a 3 m de un espejo plano. ¿Cuántos metros hay entre ella y su imagen?", "3*2", "La imagen está a igual distancia detrás del espejo.", " m"),
      arith("Un rayo forma 30° con la superficie del espejo, no con la normal. ¿Cuántos grados forma con la normal?", "90-30", "La normal es perpendicular a la superficie, es decir, forma 90° con ella.", "°"),
  ],
  rea=[
      ("Un compañero dice: «El espejo cambia mi izquierda por mi derecha». ¿Qué afirmación es más precisa? A) El espejo invierte adelante–atrás y tu mano derecha queda del mismo lado que la de tu imagen B) El espejo gira la imagen de lado a lado", "A", "La inversión es en la dirección perpendicular al espejo, no horizontal."),
      ("Una linterna tiene un espejo cóncavo detrás de la ampolleta, que está en el foco. ¿Para qué sirve? A) Para que los rayos salgan casi paralelos y formen un haz B) Para que los rayos se dispersen en todas direcciones", "A", "Los rayos que salen del foco se reflejan paralelos."),
  ],
  cha=[
      arith("Una persona está a 4 m de un espejo plano y camina 1 m hacia él. ¿Cuántos metros hay ahora entre ella y su imagen?", "(4-1)*2", "Ahora está a 3 m del espejo y su imagen a 3 m detrás de él.", " m"),
      arith("El ángulo entre el rayo incidente y el rayo reflejado mide 100°. ¿Cuántos grados mide el ángulo de incidencia?", "100/2", "Los dos ángulos son iguales y suman 100°.", "°"),
  ],
  context=[ex("Un conductor de bus mira por un espejo retrovisor convexo y ve los autos más pequeños que en un espejo plano. ¿Por qué se usa de todas formas? A) Porque abarca una zona más amplia detrás del bus B) Porque forma una imagen real más grande", "A", "El espejo convexo sacrifica tamaño para ganar campo de visión.")],
  selfcheck=[("¿Qué dice la ley de la reflexión?", "El ángulo de incidencia es igual al ángulo de reflexión", "Ambos se miden respecto de la normal."), ("¿La imagen de un espejo plano es real o virtual?", "Virtual", "Parece estar detrás del espejo, donde no hay luz."), ("¿Qué espejo hace converger los rayos paralelos en un foco?", "El cóncavo", "Su forma interior junta los rayos.")],
  open_task=task("Un lápiz de 6 cm está de pie a 5 cm de un espejo plano. En tu cuaderno dibuja a escala 1:1 el espejo, el lápiz y su imagen. Indica la distancia y el tamaño de la imagen y si es real o virtual. Dibuja además un rayo que sale de la punta del lápiz, choca con el espejo formando 30° con la normal y se refleja.", "La imagen está a 5 cm detrás del espejo, mide 6 cm y es virtual. El rayo reflejado forma 30° con la normal, del otro lado de ella; si lo prolongas hacia atrás del espejo, pasa por la punta de la imagen.", ["imagen a 5 cm detrás del espejo", "tamaño 6 cm", "dice virtual", "ángulos de 30° a ambos lados de la normal"], ["dibujo a escala con mediciones", "frase que clasifica la imagen"], ["dibujar la imagen sobre el espejo", "medir el ángulo desde la superficie", "decir que la imagen es real"], "Pregunta cómo cambiaría el dibujo si el lápiz estuviera a 8 cm del espejo."),
  reinforce="Escribe la distancia a la imagen cuando un objeto está a 7 cm de un espejo plano.",
  extend="Explica por qué un espejo cóncavo usado como espejo de maquillaje amplía el rostro solo si estás muy cerca de él.")

L(OA, 3,
  materials="Este cuaderno, lápiz, regla y calculadora. Con ayuda de una persona adulta puedes observar un lápiz en un vaso transparente de plástico con agua; todos los datos están escritos.",
  use="Aprenderé por qué la luz se desvía al cambiar de medio y cómo las lentes forman imágenes. Sirve para entender lupas, cámaras, telescopios y prismáticos.",
  prior=["Sé que la luz tiene rapidez y viaja en línea recta.", "Sé la ley de la reflexión y la noción de normal."],
  explain=[
      "La refracción es el cambio de dirección de la luz cuando pasa de un medio a otro, por ejemplo del aire al agua. Ocurre porque la rapidez de la luz cambia: en el aire es de unos 300.000 km/s, en el agua de unos 225.000 km/s y en el vidrio de unos 200.000 km/s (valores aproximados). Si la luz pasa a un medio donde va más lenta, el rayo se acerca a la normal; si pasa a uno donde va más rápida, se aleja. Si el rayo llega siguiendo la normal, no se desvía.",
      "Una lente es una pieza transparente con superficies curvas que refracta la luz. La lente convergente es más gruesa en el centro y junta los rayos paralelos en el foco; la distancia entre la lente y el foco es la distancia focal. La lente divergente es más delgada en el centro y separa los rayos. Una lupa es una lente convergente: si pones el objeto más cerca de la lente que su distancia focal, ves una imagen derecha, virtual y más grande.",
      "Muchos instrumentos combinan lentes. La cámara y el ojo usan una lente convergente que forma sobre una pantalla una imagen real e invertida. Un telescopio refractor y los prismáticos tienen una lente objetivo, que reúne la luz del objeto lejano, y una lente ocular, que amplía la imagen para el ojo. Los anteojos corrigen la visión cambiando la dirección de los rayos antes de que entren al ojo.",
  ],
  vocab=[("refracción", "cambio de dirección de la luz al pasar de un medio a otro"), ("lente convergente", "lente más gruesa al centro que junta los rayos paralelos"), ("lente divergente", "lente más delgada al centro que separa los rayos"), ("distancia focal", "distancia entre la lente y su foco"), ("objetivo", "lente de un instrumento que reúne la luz del objeto"), ("ocular", "lente de un instrumento que se pone frente al ojo")],
  worked=[
      ("Acercarse o alejarse de la normal", "Un rayo pasa del aire (300.000 km/s) al vidrio (200.000 km/s). ¿Se acerca o se aleja de la normal?", ["Comparo las rapideces: en el vidrio la luz va más lenta.", "Si el medio es más lento, el rayo se acerca a la normal."], "Se acerca a la normal"),
      ("Elegir una lente", "Quieres leer letras muy pequeñas con una lupa. ¿Qué lente usas y dónde pones el objeto?", ["La lupa es una lente convergente.", "Para imagen derecha y ampliada, el texto va a menos de una distancia focal de la lente."], "Lente convergente, con el texto más cerca que el foco"),
  ],
  mistakes=[
      ("Creer que la luz se desvía porque «se cansa» en el agua.", "Se desvía porque su rapidez cambia al cambiar de medio.", "Compara siempre las rapideces antes de decidir el sentido del desvío."),
      ("Pensar que una lupa crea más luz.", "La lente solo cambia la dirección de los rayos y forma una imagen.", "Describe la imagen y no la cantidad de luz."),
  ],
  rec=[
      ("¿Qué propiedad de la luz cambia cuando pasa del aire al agua y causa la refracción?", "Su rapidez", "El cambio de rapidez desvía el rayo."),
      ("¿La lente convergente es más gruesa en el centro o en los bordes?", "En el centro", "Esa forma junta los rayos paralelos."),
      ("Verdadero o falso: un rayo que llega siguiendo la normal no se desvía al cambiar de medio.", "Verdadero", "No hay ángulo respecto de la normal para cambiar."),
  ],
  und=[
      ("Un rayo pasa del agua (225.000 km/s) al aire (300.000 km/s). ¿Qué ocurre con su dirección? A) Se aleja de la normal B) Se acerca a la normal", "A", "En el medio más rápido, el rayo se aleja de la normal."),
      ("¿Qué tipo de lente junta los rayos paralelos en un punto?", "La lente convergente", "Su forma curva refracta los rayos hacia el foco."),
      ("El fondo de una piscina parece menos profundo de lo que es. ¿Por qué? A) La luz se refracta al salir del agua y vemos el fondo más arriba B) El agua absorbe la luz del fondo", "A", "El desvío cambia la posición aparente del fondo."),
  ],
  app=[
      arith("La luz tiene en el agua una rapidez de 225.000 km/s. ¿Cuántos segundos tarda en recorrer 450.000 km en agua?", "450000/225000", "El tiempo es la distancia dividida por la rapidez.", " s"),
      arith("Un destello de luz recorre 600.000 km. En el aire va a 300.000 km/s y en un vidrio de ejemplo va a 200.000 km/s. ¿Cuántos segundos más tarda en el vidrio?", "600000/200000-600000/300000", "Se calcula cada tiempo y se restan.", " s"),
      ("Una lupa de 10 cm de distancia focal se usa para leer. ¿Dónde se debe poner el texto? A) A 4 cm de la lente B) A 25 cm de la lente", "A", "Para una imagen derecha y ampliada, el objeto debe estar a menos de una distancia focal."),
  ],
  rea=[
      ("Una estudiante dice: «La lupa hace más luz que la ampolleta». ¿Es correcto? A) No: la lente solo refracta los rayos y forma una imagen mayor B) Sí: la lente crea luz nueva", "A", "Una lente no genera energía luminosa."),
      ("Un dibujo de ejemplo muestra tres rayos paralelos que llegan a una lente y salen abiertos como un abanico. ¿Qué tipo de lente es?", "Divergente", "Los rayos paralelos se separan después de pasar por la lente."),
  ],
  cha=[
      ("Un rayo pasa del aire al vidrio con un ángulo de incidencia de 0°. ¿Cuánto mide el ángulo de refracción?", "0°", "Un rayo que sigue la normal no se desvía."),
      arith("En un material de ejemplo la luz viaja a 150.000 km/s. ¿Cuántas veces es mayor su rapidez en el aire (300.000 km/s)?", "300000/150000", "Se divide la rapidez en el aire por la del material.", " veces"),
  ],
  context=[ex("Un telescopio refractor de aficionado tiene dos lentes convergentes. Una está al final del tubo, apuntando a la Luna, y la otra está donde se pone el ojo. ¿Cuál se llama objetivo? A) La del final del tubo, que reúne la luz de la Luna B) La que está junto al ojo", "A", "El objetivo es la lente que recibe la luz del objeto lejano.")],
  selfcheck=[("¿Por qué se produce la refracción?", "Porque cambia la rapidez de la luz al pasar a otro medio", "El cambio de rapidez desvía el rayo."), ("¿Qué lente usa una lupa?", "Una convergente", "Junta rayos y amplía la imagen si el objeto está cerca."), ("¿Para qué sirve la lente ocular?", "Para ampliar la imagen que mira el ojo", "Se coloca frente al ojo.")],
  open_task=task("Rapidez de la luz en materiales (valores aproximados de ejemplo): aire 300.000 km/s, agua 225.000 km/s, vidrio 200.000 km/s, diamante 125.000 km/s. Ordena los materiales según cuánto acercan a la normal un rayo que llega desde el aire con el mismo ángulo, de menos a más. Justifica con las rapideces y dibuja un rayo del aire al agua con 45° de incidencia.", "De menos a más: agua, vidrio, diamante. Mientras menor es la rapidez en el material, más se acerca el rayo a la normal. En el dibujo, el rayo en el agua forma un ángulo menor que 45° con la normal.", ["orden agua, vidrio, diamante", "relaciona rapidez menor con mayor acercamiento", "dibujo con ángulo menor que 45° en el agua"], ["lista ordenada y dibujo"], ["ordenar al revés", "dibujar el rayo alejándose de la normal", "no usar las rapideces"], "Pregunta qué pasaría si el rayo saliera del diamante hacia el aire."),
  reinforce="Escribe una frase que explique por qué un lápiz parece quebrado dentro de un vaso transparente con agua.",
  extend="Explica por qué un telescopio refractor necesita dos lentes y no solo una.")

L(OA, 4,
  materials="Este cuaderno y lápiz. Los datos de los experimentos están escritos en los ejercicios; no necesitas láser ni rendijas.",
  use="Aprenderé dos modelos para explicar la luz y fenómenos como la difracción, la interferencia y el efecto Doppler. Sirve para decidir qué modelo explica cada observación.",
  prior=["Sé que la luz se refleja y se refracta.", "Sé que una onda tiene crestas, valles, amplitud, frecuencia y longitud de onda."],
  explain=[
      "El modelo corpuscular imagina la luz como un chorro de partículas diminutas que viajan en línea recta. Explica bien la reflexión y las sombras nítidas. El modelo ondulatorio imagina la luz como una onda con longitud de onda y frecuencia. Explica además la refracción, la difracción y la interferencia. La física actual acepta que la luz se comporta como onda en unos experimentos y como partículas, llamadas fotones, en otros.",
      "La difracción es el curvado y la apertura de una onda al pasar por una rendija u orificio de tamaño parecido a su longitud de onda. La interferencia ocurre cuando dos ondas se superponen. Si coinciden cresta con cresta, la interferencia es constructiva y las amplitudes se suman. Si coincide cresta con valle, la interferencia es destructiva y las amplitudes se restan. Dos rendijas muy finas producen en una pantalla franjas claras y oscuras, evidencia de que la luz se comporta como onda. Los colores de una pompa de jabón también nacen de interferencia.",
      "El efecto Doppler es el cambio de la frecuencia que percibe un observador cuando la fuente y el observador se acercan o se alejan. Una ambulancia suena más aguda al acercarse y más grave al alejarse. Con la luz ocurre algo parecido: si una galaxia se aleja, sus líneas de color se corren hacia longitudes de onda mayores (desplazamiento al rojo); si se acerca, se corren hacia longitudes menores (al azul). El radar de velocidad usa este efecto con ondas de radio.",
  ],
  vocab=[("modelo corpuscular", "idea de que la luz es un chorro de partículas"), ("modelo ondulatorio", "idea de que la luz es una onda"), ("difracción", "apertura de una onda al pasar por una rendija u orificio"), ("interferencia", "superposición de dos ondas que se suman o se restan"), ("efecto Doppler", "cambio de frecuencia percibida por el movimiento relativo entre fuente y observador"), ("fotón", "partícula de luz, un paquete de energía luminosa")],
  worked=[
      ("Interferencia de dos ondas", "Dos ondas de luz llegan a un punto con amplitudes de 3 y 2 unidades. ¿Cuál es la amplitud si llegan en fase y cuál si llegan en oposición?", ["En fase se suman: 3 + 2 = 5.", "En oposición se restan: 3 − 2 = 1."], "5 unidades en fase y 1 unidad en oposición"),
      ("Elegir el modelo", "Una caja bloquea la luz y deja una sombra de bordes nítidos. ¿Qué modelo la explica sin dificultad?", ["La sombra nítida se explica con luz que viaja en línea recta.", "Ambos modelos lo explican, porque la longitud de onda de la luz es muy pequeña frente a la caja."], "Ambos modelos; basta la propagación en línea recta"),
  ],
  mistakes=[
      ("Creer que una onda no puede dar sombras nítidas.", "La longitud de onda de la luz es tan pequeña que la difracción se nota solo en aberturas muy pequeñas.", "Compara el tamaño de la abertura con la longitud de onda."),
      ("Pensar que el efecto Doppler cambia el tono porque la fuente cambia de potencia.", "Cambia la frecuencia que llega al observador por el movimiento relativo.", "Pregunta si la fuente y el observador se acercan o se alejan."),
  ],
  rec=[
      ("¿Cómo se llama la apertura de la luz al pasar por una rendija muy estrecha?", "Difracción", "Es un fenómeno propio de las ondas."),
      ("Cuando dos ondas coinciden cresta con cresta, la interferencia es ______ (constructiva o destructiva).", "Constructiva", "Las amplitudes se suman."),
      ("Verdadero o falso: una ambulancia que se acerca suena más aguda que cuando está detenida.", "Verdadero", "Al acercarse, llegan más ondas por segundo al oído."),
  ],
  und=[
      ("Con dos rendijas muy finas aparecen en la pared franjas claras y oscuras. ¿Qué modelo las explica mejor? A) El ondulatorio B) El corpuscular simple", "A", "Las franjas son un patrón de interferencia."),
      ("Una ambulancia se aleja de ti. ¿Cómo percibes su sirena? A) Más grave B) Más aguda", "A", "Al alejarse, llegan menos ondas por segundo."),
      ("La luz de una galaxia está desplazada hacia el rojo. ¿Qué indica? A) La galaxia se aleja B) La galaxia se acerca", "A", "El corrimiento a longitudes de onda mayores indica alejamiento."),
  ],
  app=[
      arith("Dos ondas de luz de amplitud 6 y 4 llegan en fase a un punto. ¿Cuál es la amplitud resultante?", "6+4", "Con interferencia constructiva las amplitudes se suman."),
      arith("Dos ondas de igual amplitud 6 llegan en oposición a un punto. ¿Cuál es la amplitud resultante?", "6-6", "Con interferencia destructiva se restan y queda oscuridad."),
      ("Un haz de luz pasa por un orificio muy pequeño y proyecta un círculo borroso rodeado de anillos, más grande que el orificio. ¿Qué fenómeno ocurrió?", "Difracción", "La onda se abre al pasar por una abertura muy pequeña."),
  ],
  rea=[
      ("Un estudiante dice: «Como la luz hace sombras nítidas, no puede ser una onda». ¿Qué respuesta es correcta? A) Incorrecto: su longitud de onda es muy pequeña y la difracción solo se nota en aberturas diminutas B) Correcto: las ondas nunca forman sombras", "A", "Las sombras nítidas no descartan el modelo ondulatorio."),
      ("¿Por qué una pompa de jabón muestra colores? A) Por interferencia de la luz reflejada en las dos caras de la capa delgada B) Porque el agua con jabón tiene un tinte de colores fijos", "A", "Las ondas reflejadas en dos superficies se refuerzan o se anulan según el color."),
  ],
  cha=[
      ("En un punto de una pantalla llegan dos ondas de luz de igual amplitud: una con cresta y la otra con valle. ¿Qué se ve en ese punto?", "Oscuridad", "Es una interferencia destructiva total."),
      arith("Una línea de color mide 656 nm en el laboratorio y 664 nm en la luz de una galaxia. ¿Cuántos nanómetros aumentó la longitud de onda?", "664-656", "Se resta la medida del laboratorio a la de la galaxia: un corrimiento hacia el rojo.", " nm"),
  ],
  context=[arith("Una ambulancia emite una sirena de 800 Hz (valor de ejemplo). Al acercarse, un peatón percibe 880 Hz y al alejarse percibe 730 Hz. ¿Cuántos hertz de diferencia hay entre lo que percibe al acercarse y al alejarse?", "880-730", "Se resta la frecuencia percibida al alejarse de la percibida al acercarse.", " Hz")],
  selfcheck=[("¿Qué es la interferencia destructiva?", "Cuando cresta y valle coinciden y las amplitudes se restan", "Puede llegar a anular la onda."), ("¿Qué modelo explica la difracción?", "El ondulatorio", "La apertura de la luz al pasar por rendijas es propia de las ondas."), ("¿Qué indica el corrimiento al azul de una galaxia?", "Que se acerca", "Las longitudes de onda se acortan al acercarse la fuente.")],
  open_task=task("Observaciones: (1) sombra nítida de una silla, (2) franjas claras y oscuras con dos rendijas finas, (3) rayo que se acerca a la normal al entrar al agua, (4) colores en una pompa de jabón, (5) sirena que cambia de tono al pasar, (6) círculo borroso con anillos al pasar un haz por un orificio diminuto. Escribe en una tabla qué fenómeno ocurre en cada una (propagación recta, refracción, interferencia, difracción o efecto Doppler) y un párrafo de tres líneas que explique por qué hoy se usan los dos modelos de luz.", "1 propagación recta; 2 interferencia (y difracción); 3 refracción; 4 interferencia; 5 efecto Doppler; 6 difracción. Párrafo: el modelo de partículas explica bien la propagación recta y la reflexión; el de onda explica interferencia y difracción; la luz se comporta como onda o como fotones según el experimento.", ["seis filas con el fenómeno correcto", "justifica que 2, 4 y 6 requieren el modelo ondulatorio", "párrafo con ambos modelos"], ["tabla de seis filas y párrafo"], ["rotular franjas como reflexión", "decir que un modelo anula al otro"], "Pregunta qué observación nueva obligaría a revisar el modelo."),
  reinforce="Explica con tus palabras por qué una sirena suena más grave al alejarse.",
  extend="Explica por qué el radar de velocidad usa el efecto Doppler y qué mide.")

L(OA, 5,
  materials="Este cuaderno, lápices de colores y calculadora. Si tienes un vaso transparente con agua y la luz del sol por una ventana, puedes ver colores separados; todos los datos están escritos.",
  use="Aprenderé cómo se forman los colores con luces, con filtros y con pigmentos. Sirve para entender pantallas, focos de escenario y por qué vemos los objetos de cierto color.",
  prior=["Sé que la luz se refracta al cambiar de medio.", "Sé que la luz blanca viene del Sol y de ampolletas."],
  explain=[
      "La luz blanca es una mezcla de luces de muchos colores. Un prisma de vidrio la separa porque cada color se refracta con un ángulo distinto: el rojo se desvía menos y el violeta más. Este fenómeno se llama dispersión. Un arcoíris se forma cuando gotas de lluvia refractan, reflejan y vuelven a refractar la luz del Sol; para verlo, el Sol debe estar a tus espaldas y la lluvia delante de ti. La difracción en un disco compacto también separa colores.",
      "En la mezcla de luces, los colores primarios son rojo, verde y azul. Al mezclarlos de a dos se obtienen los secundarios: rojo más verde da amarillo, verde más azul da cian y rojo más azul da magenta. Los tres primarios juntos dan luz blanca. Así funcionan las pantallas y los focos de colores de un escenario. En la mezcla de pigmentos, como las tintas, los primarios son cian, magenta y amarillo y cada pigmento absorbe parte de la luz, por eso mezclar pinturas oscurece.",
      "Un filtro de color deja pasar la luz de su color y absorbe las demás. Un filtro rojo sobre luz blanca deja pasar solo luz roja; sobre luz verde no deja pasar nada. El color de un objeto es la luz que refleja: una manzana roja refleja luz roja y absorbe el resto, y bajo luz verde se ve casi negra porque no recibe luz roja que reflejar.",
  ],
  vocab=[("dispersión", "separación de la luz blanca en sus colores al refractarse"), ("color primario de luz", "uno de los colores rojo, verde o azul, con los que se forman los demás"), ("color secundario de luz", "color que resulta de mezclar dos primarios de luz"), ("filtro", "material que deja pasar ciertos colores y absorbe los demás"), ("pigmento", "sustancia que da color porque absorbe parte de la luz"), ("mezcla aditiva", "mezcla de luces: al sumar colores se obtiene luz más clara")],
  worked=[
      ("Mezcla de luces", "Un foco rojo y uno verde iluminan el mismo punto de una pared blanca. ¿Qué color se ve?", ["Los dos colores son primarios de luz.", "Rojo más verde da amarillo."], "Amarillo"),
      ("Filtro y objeto", "Una manzana roja se ilumina con luz verde. ¿De qué color se ve?", ["La manzana solo refleja luz roja.", "La luz verde no contiene luz roja para reflejar y la manzana la absorbe."], "Casi negra"),
  ],
  mistakes=[
      ("Creer que mezclar luces de colores se comporta como mezclar pinturas.", "Las luces se suman y aclaran; los pigmentos absorben y oscurecen.", "Pregunta si mezclas luces o pigmentos antes de predecir."),
      ("Pensar que un filtro «pinta» la luz.", "El filtro solo deja pasar su color y absorbe los demás.", "Revisa qué colores contiene la luz que llega al filtro."),
  ],
  rec=[
      ("¿Cuáles son los colores primarios de la luz?", "Rojo, verde y azul", "Con ellos se forman todos los demás."),
      ("Verde más azul, mezclados como luces, dan ______ (cian o amarillo).", "Cian", "Es un color secundario de luz."),
      ("Al pasar por un prisma, ¿qué color se desvía más: el rojo o el violeta?", "El violeta", "El violeta se refracta con mayor ángulo."),
  ],
  und=[
      ("Un prisma separa la luz blanca en colores porque: A) cada color se refracta con un ángulo distinto B) el prisma agrega colores a la luz", "A", "La luz blanca ya contiene todos los colores."),
      ("¿Qué color sale de un filtro azul si le llega luz blanca?", "Azul", "El filtro deja pasar solo luz azul."),
      ("¿Cómo se ve una polera azul bajo luz roja?", "Casi negra", "No recibe luz azul que reflejar."),
  ],
  app=[
      ("Un escenario tiene un foco de luz roja y otro de luz azul apuntando al mismo lugar. ¿Qué color ve el público?", "Magenta", "Rojo más azul da magenta."),
      ("Un foco de luz roja y otro de luz verde se enfocan en el escenario junto con un tercero de luz azul. ¿Qué color se ve en la zona donde se juntan los tres?", "Blanco", "Los tres primarios de luz suman luz blanca."),
      ("La luz blanca pasa por un filtro rojo y después por un filtro azul. ¿Qué luz sale del segundo?", "Ninguna", "El rojo no puede atravesar el filtro azul."),
  ],
  rea=[
      ("Una polera blanca se ilumina con luz roja. ¿Qué ocurre? A) Se ve roja porque refleja la luz roja que recibe B) Se ve blanca porque la luz roja se vuelve blanca", "A", "El objeto solo refleja los colores que recibe."),
      ("¿Por qué mezclar pinturas da un color más oscuro y mezclar luces uno más claro? A) Los pigmentos absorben más luz y las luces se suman B) Las pinturas emiten menos luz que los focos", "A", "Los pigmentos restan luz al absorberla; las luces la suman."),
  ],
  cha=[
      arith("Una pantalla de ejemplo tiene 1.000 × 2.000 píxeles y cada píxel usa 3 subpíxeles (rojo, verde y azul). ¿Cuántos subpíxeles tiene la pantalla?", "1000*2000*3", "Se multiplica el número de píxeles por los subpíxeles de cada uno."),
      ("Escribes con lápiz rojo sobre papel blanco y lo miras a través de un filtro rojo. ¿Qué ves? A) La escritura desaparece porque ambos colores dejan pasar luz roja B) La escritura se ve más oscura", "A", "Las letras rojas y el papel blanco reflejan luz roja que pasa por el filtro, así que se igualan."),
  ],
  context=[ex("Para ver un arcoíris, ¿dónde debe estar el Sol respecto de ti y la lluvia? A) Detrás de ti, con la lluvia delante B) Delante de ti, con la lluvia detrás", "A", "La luz debe entrar a las gotas y volver hacia tus ojos.")],
  selfcheck=[("¿Qué es la dispersión de la luz?", "La separación de la luz blanca en colores al refractarse", "Cada color se desvía de manera distinta."), ("¿Qué luz sale de un filtro verde si le llega luz blanca?", "Luz verde", "El filtro deja pasar solo su color."), ("¿Qué hace un filtro verde con la luz roja?", "La absorbe", "Solo deja pasar la luz verde.")],
  open_task=task("Completa una tabla con el color que se ve en cada caso: (a) luz roja + luz verde, (b) luz verde + luz azul, (c) luz roja + luz azul, (d) las tres luces, (e) manzana roja bajo luz roja, (f) manzana roja bajo luz azul. Después escribe dos líneas que expliquen la diferencia entre mezclar luces y mezclar pinturas.", "a amarillo; b cian; c magenta; d blanco; e roja; f casi negra. Las luces se suman y aclaran; los pigmentos absorben luz, así que al mezclarlos el resultado es más oscuro.", ["seis colores correctos", "explica suma de luces", "explica absorción de pigmentos"], ["tabla completa y dos líneas"], ["decir que rojo y verde dan café", "olvidar que el objeto refleja solo lo que recibe"], "Pregunta qué cambia si el foco es de luz amarilla en lugar de luz blanca."),
  reinforce="Escribe el color que resulta de mezclar luz azul con luz roja.",
  extend="Explica por qué la pantalla de un celular puede mostrar amarillo sin tener ningún subpíxel amarillo.")

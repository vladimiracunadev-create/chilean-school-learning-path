"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 07 (sistema nervioso) y OA 08 (efectos del consumo excesivo de alcohol)."""
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


OA7, OA8 = "CN04 OA 07", "CN04 OA 08"

# ---------------------------------------------------------------- OA 07
L(OA7, 1,
  materials="Este cuaderno y lápiz. Dos objetos seguros de tu casa para tocar con los ojos cerrados, por ejemplo una cuchara de madera y un paño suave.",
  use="Aprenderé qué estructuras forman el sistema nervioso y a separar lo que siento de lo que supongo. Sirve para entender cómo mi cuerpo recibe y responde a la información.",
  prior=["Sé que tengo sentidos como vista, tacto y oído.", "Sé anotar lo que observo."],
  explain=[
      "El sistema nervioso es el conjunto de órganos que recibe información, la lleva por el cuerpo y ordena respuestas. Sus estructuras son el cerebro, la médula espinal y los nervios. El cerebro está dentro del cráneo. La médula espinal baja por dentro de la columna vertebral. Los nervios salen de ella y llegan a todo el cuerpo.",
      "Los nervios son como cables delgados. Llevan mensajes desde la piel, los ojos, los oídos y otros órganos hasta la médula y el cerebro. También llevan órdenes desde el cerebro hasta los músculos. La médula espinal conduce la información entre los nervios y el cerebro. El cerebro elabora la información y controla las respuestas.",
      "Si tocas algo con los ojos cerrados, observas: «se siente suave» o «se siente duro». Eso es lo que percibes. Decir «es el objeto más bonito» es una opinión. Lo que anotas por tus sentidos es evidencia de que el sistema nervioso recibió información.",
  ],
  vocab=[("sistema nervioso", "conjunto de órganos que recibe información, la conduce y controla las respuestas"), ("cerebro", "órgano dentro del cráneo que elabora la información y controla el cuerpo"), ("médula espinal", "cordón nervioso dentro de la columna vertebral que conduce información"), ("nervio", "estructura delgada como un cable que lleva mensajes"), ("conducir", "llevar información de un lugar a otro")],
  worked=[
      ("Unir estructura y función", "La médula espinal, ¿conduce información o elabora pensamientos?", ["Recuerdo dónde está: dentro de la columna.", "Recibe y envía información entre nervios y cerebro.", "Quien elabora es el cerebro."], "Conduce información"),
      ("Observación o interpretación", "«Siento el paño suave» y «El paño es el mejor del mundo». ¿Cuál es evidencia?", ["Reviso qué dice un sentido.", "Suave se percibe al tocar.", "'El mejor' es una opinión."], "Siento el paño suave"),
  ],
  mistakes=[
      ("Pensar que el cerebro está en el pecho o que el corazón piensa.", "El cerebro está en la cabeza y es quien elabora y controla.", "Ubica el cerebro dentro del cráneo."),
      ("Creer que los nervios son huesos.", "Son cables delgados que llevan mensajes; los huesos son duros.", "Piensa en un cable y no en un palo."),
  ],
  rec=[
      ("¿El cerebro está dentro del cráneo o de la columna?", "Del cráneo", "El cráneo lo protege."),
      ("¿La médula espinal baja por la columna o por el brazo?", "Por la columna", "Está dentro de las vértebras."),
      ("Completa con «nervios» o «huesos»: los ______ llevan mensajes por el cuerpo.", "Nervios", "Son como cables delgados."),
  ],
  und=[
      ("¿Qué hace el cerebro? A) Elabora la información y controla el cuerpo. B) Solo late y manda sangre.", "A", "El que late y manda sangre es el corazón."),
      ("¿Qué estructura conduce información entre los nervios y el cerebro?", "La médula espinal", "Pasa por dentro de la columna."),
      ("¿Por qué el cráneo y la columna son importantes para el sistema nervioso?", "Porque protegen el cerebro y la médula", "Los huesos rodean y protegen esos órganos."),
  ],
  app=[
      ("Ordena con letras el camino de un mensaje de tacto: A) cerebro, B) nervio de la mano, C) médula espinal. ¿Cuál es el orden?", "B, C, A", "El mensaje sube por el nervio, la médula y llega al cerebro."),
      arith("Un niño anota 6 sensaciones con la mano derecha y 5 con la mano izquierda. ¿Cuántas sensaciones anotó en total?", "6+5", "Se suman las sensaciones de cada mano."),
      ("Un niño toca una cuchara de madera y dice: 'Está dura y lisa'. ¿Cuántas sensaciones nombra?", "2", "Dura y lisa."),
  ],
  rea=[
      ("Ana dice que el cerebro solo sirve para pensar, no para controlar el cuerpo. ¿Tiene razón? Responde Sí o No y explica.", "No; también controla las respuestas, como mover los músculos", "El cerebro envía órdenes."),
      ("Mario toca algo caliente y quita la mano. Nombra la estructura, parecida a un cable delgado, que lleva el mensaje desde la piel hasta la médula espinal.", "Los nervios", "Los nervios llevan el mensaje desde la piel."),
  ],
  cha=[
      ("Escribe una observación y una interpretación sobre cómo sientes un objeto con los ojos cerrados.", "Observación: siento la cuchara dura. Interpretación: es de madera", "Una se siente; la otra es una suposición."),
      ("Explica por qué dañar la médula espinal sería grave.", "Porque se cortaría la comunicación entre el cerebro y el cuerpo", "La médula conduce información."),
  ],
  context=[("Un niño toca 5 objetos seguros con los ojos cerrados: 2 suaves y 3 duros. Su cerebro elaboró la información de todos. ¿Cuántos objetos fueron en total?", "5", "2 + 3 = 5.")],
  selfcheck=[("Nombra tres estructuras del sistema nervioso.", "Cerebro, médula espinal y nervios", "Son las estudiadas."), ("¿Qué hace la médula espinal?", "Conduce información entre los nervios y el cerebro", "Es el camino principal."), ("¿Qué hace el cerebro?", "Elabora la información y controla las respuestas", "Es el centro de control.")],
  open_task=task("Con una persona de tu casa, cierra los ojos y toca con cuidado dos objetos seguros: una cuchara de madera y un paño. No uses objetos filosudos, calientes ni pequeños. Anota dos observaciones por objeto (por ejemplo: duro, suave, liso) y una interpretación. Dibuja el camino del mensaje: mano, nervio, médula, cerebro.", "Cuchara: dura y lisa. Paño: suave y blando. Interpretación: la cuchara es de madera, aunque no la veo. Camino: mano → nervio → médula → cerebro.", ["dos observaciones por objeto", "una interpretación marcada", "dibujo del camino"], ["tabla y dibujo"], ["confundir sentir con opinar", "olvidar la médula"], "Pregunta qué estructura envía la orden para soltar un objeto."),
  reinforce="Dibuja una silueta del cuerpo y marca con rojo el cerebro, con azul la médula y con verde los nervios.",
  extend="Averigua en un libro qué otra parte del sistema nervioso protegen los huesos de la cabeza.")

L(OA7, 2,
  materials="Este cuaderno, lápiz y una regla de 30 cm. Una persona de tu casa para ayudar.",
  use="Aprenderé a hacer preguntas y predicciones sobre la rapidez con que el sistema nervioso responde. Sirve para entender cómo viaja la información.",
  prior=["Sé nombrar cerebro, médula y nervios.", "Sé que una predicción se hace antes de probar."],
  explain=[
      "Cuando algo pasa, el cuerpo responde. Los ojos ven, los nervios llevan el mensaje al cerebro y el cerebro ordena a los músculos. Todo ese camino se hace en una fracción de segundo. Si el camino es más corto o la atención es mayor, la respuesta es más rápida.",
      "Una prueba segura es la regla que cae. Una persona sostiene la regla vertical y la suelta. La otra, con los dedos abiertos abajo, intenta atraparla lo más rápido que pueda. Se anota por qué centímetro la atrapó. Si la atrapa en un número menor de centímetros, respondió más rápido.",
      "Una pregunta comprobable es: «¿Atrapo la regla en menos centímetros si estoy atento o si estoy distraído contando hacia atrás?». Una predicción: «Atento atraparé más cerca del inicio, porque el mensaje llega pronto al cerebro». Se repite varias veces y se anota cada intento.",
  ],
  vocab=[("reacción", "respuesta del cuerpo a algo que ocurre"), ("estímulo", "algo que provoca una respuesta, como ver caer una regla"), ("respuesta", "lo que el cuerpo hace ante un estímulo"), ("intento", "cada vez que se repite una prueba"), ("distraerse", "no prestar atención a lo que ocurre")],
  worked=[
      ("Leer la prueba", "Primer intento: se atrapa en 12 cm. Segundo intento: se atrapa en 8 cm. ¿En cuál reaccionó más rápido?", ["Menos centímetros significa menos caída.", "8 es menor que 12.", "Reaccionó más rápido en el segundo."], "En el segundo intento"),
      ("Hacer una predicción", "Predice: ¿atraparé más cerca del inicio con atención o con distracción?", ["Con atención el cerebro recibe el mensaje antes.", "Se atrapa antes.", "Escribo la razón."], "Con atención, porque el mensaje llega pronto"),
  ],
  mistakes=[
      ("Concluir con un solo intento.", "Un intento puede ser suerte.", "Repite varias veces y anota todos."),
      ("Cambiar de mano y de atención a la vez.", "No sabes cuál cambio causó el resultado.", "Cambia una sola cosa."),
  ],
  rec=[
      ("Si atrapas la regla en un número menor de centímetros, ¿reaccionaste más rápido o más lento?", "Más rápido", "La regla cayó menos."),
      ("¿Quién ordena a los músculos que se muevan?", "El cerebro", "Controla las respuestas."),
      ("Completa con «uno» o «varios»: para tener buenos datos se hacen ______ intentos.", "Varios", "Un solo intento puede ser suerte."),
  ],
  und=[
      ("¿Cuál pregunta se puede comprobar? A) ¿En cuántos centímetros atrapo la regla con atención? B) ¿Es linda la regla?", "A", "Se mide en centímetros."),
      ("Datos de ejemplo. Intentos: 14 cm, 10 cm, 12 cm. ¿Cuál fue la reacción más rápida?", "10 cm", "Es el número menor."),
      ("¿Por qué conviene repetir la prueba?", "Para tener más datos confiables", "Un intento puede deberse al azar."),
  ],
  app=[
      arith("Datos de ejemplo. Intento 1: 15 cm. Intento 2: 11 cm. ¿Cuántos centímetros menos cayó la regla en el segundo?", "15-11", "Se resta el menor al mayor."),
      arith("Datos de ejemplo. Tres intentos: 10 cm, 12 cm y 8 cm. ¿Cuántos centímetros suman?", "10+12+8", "Se suman todos los intentos."),
      ("Predice: si estás distraído mirando otra cosa, ¿atraparás la regla en más o menos centímetros?", "Más", "Tardas más en reaccionar."),
  ],
  rea=[
      ("Luis atrapó la regla en 6 cm y Ema en 9 cm. ¿Qué muestra el dato: que Luis reaccionó más rápido en este intento o que Luis es mejor persona?", "Que Luis reaccionó más rápido en este intento", "El dato solo habla de rapidez, no de otras cosas."),
      ("Para comparar dos personas, ¿qué conviene dejar igual: la altura desde la que se suelta o el color de la regla? Escribe una de las dos.", "La altura desde la que se suelta", "Si la altura cambia, cambia la medida."),
  ],
  cha=[
      ("Escribe una pregunta comprobable con la regla y qué cambiarías.", "¿Atrapo mejor con la mano que uso más o con la otra? Cambio la mano", "Se cambia una sola cosa."),
      ("Datos de ejemplo. Con atención: 9, 8 y 10 cm. Con distracción: 14, 12 y 13 cm. ¿Qué conclusión es prudente?", "En esta prueba reaccionó más rápido con atención", "La conclusión se limita a los datos."),
  ],
  context=[("En una clase de 20 estudiantes cada uno hace 3 intentos con la regla. ¿Cuántos intentos se hacen en total?", "60", "20 × 3 = 60.")],
  selfcheck=[("¿Qué se mide con la regla que cae?", "La rapidez de reacción", "Se mide en centímetros."), ("¿Cuál reacción es más rápida: la que cae menos o más?", "La que cae menos", "Se atrapa antes."), ("¿Por qué se repite la prueba?", "Para tener datos más confiables", "Un solo intento puede ser suerte.")],
  open_task=task("Con una persona de tu casa, haz la prueba de la regla de 30 cm: tu ayudante la suelta sin avisar y tú la atrapas con los dedos. Haz cinco intentos mirando solo la regla y cinco contando en voz alta de 20 hacia atrás mientras miras la regla. Anota los centímetros en una tabla, escribe tu predicción antes y una conclusión prudente después.", "Predicción: con atención atrapo en menos centímetros. Atento: 9, 10, 8, 11, 9. Contando hacia atrás: 14, 13, 15, 12, 14. Conclusión: en esta prueba reaccioné más rápido con atención.", ["predicción con razón", "diez intentos anotados", "conclusión prudente"], ["tabla de diez datos"], ["un solo intento", "cambiar dos cosas a la vez"], "Pregunta cuál fue su mejor intento y qué influyó."),
  reinforce="Haz tres intentos con la regla y anota cuántos centímetros cayó en cada uno.",
  extend="Escribe una nueva pregunta comprobable con la regla y la mano que usas menos.")

L(OA7, 3,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar cerebro, médula espinal y nervios con un mismo criterio. Sirve para entender qué hace cada estructura.",
  prior=["Sé qué son el cerebro, la médula y los nervios.", "Sé comparar con un criterio."],
  explain=[
      "Para comparar las estructuras del sistema nervioso uso criterios: dónde están, cómo se ven y qué función cumplen. El cerebro está en la cabeza, protegido por el cráneo. La médula espinal está dentro de la columna. Los nervios están repartidos por todo el cuerpo.",
      "La función del cerebro es elaborar la información: pensar, recordar, decidir y controlar. La función de la médula y de los nervios es conducir información. Los nervios llevan mensajes desde los sentidos hacia la médula y desde ella hacia los músculos. La médula conecta con el cerebro.",
      "Si falla una estructura, falla su función. Si se daña un nervio de la mano, el mensaje de tacto no llega bien. Si se daña la médula, se interrumpe la comunicación entre el cerebro y parte del cuerpo. Por eso los cuidamos con cascos y buenas posturas.",
  ],
  vocab=[("elaborar", "procesar la información para pensar o decidir"), ("controlar", "dirigir las acciones del cuerpo"), ("conducir", "llevar información de un lugar a otro"), ("estructura", "parte de un sistema con una función"), ("casco", "protección rígida para la cabeza")],
  worked=[
      ("Comparar funciones", "Cerebro y nervios: ¿cuál elabora información y cuál la conduce?", ["El cerebro piensa y decide: elabora.", "Los nervios llevan mensajes: conducen.", "Cada estructura tiene su función."], "El cerebro elabora y los nervios conducen"),
      ("Predecir un fallo", "Si un nervio de la mano se daña, ¿qué mensaje no llega bien?", ["El nervio lleva mensajes desde la piel.", "Si falla, el cerebro no los recibe.", "No siente bien el tacto."], "El mensaje del tacto de la mano"),
  ],
  mistakes=[
      ("Pensar que la médula y los nervios piensan.", "Solo conducen; quien elabora es el cerebro.", "Recuerda: cerebro = elabora; médula y nervios = conducen."),
      ("Creer que el cerebro está dentro de la columna.", "Está dentro del cráneo.", "Ubica cada estructura."),
  ],
  rec=[
      ("¿Quién elabora la información: el cerebro o los nervios?", "El cerebro", "Es el centro de control."),
      ("¿Quién conduce mensajes por el cuerpo: los nervios o el cráneo?", "Los nervios", "Son como cables."),
      ("Completa con «cráneo» o «columna»: la médula espinal está dentro de la ______.", "Columna", "Las vértebras la protegen."),
  ],
  und=[
      ("¿Cuál criterio sirve para comparar el cerebro y la médula? A) Dónde están. B) Si me gustan.", "A", "La ubicación es una característica."),
      ("¿Qué función tienen los nervios? A) Conducir mensajes. B) Proteger el cerebro.", "A", "Proteger es función de los huesos."),
      ("¿Por qué conviene usar casco al andar en bicicleta?", "Para proteger la cabeza y el cerebro", "El casco amortigua los golpes."),
  ],
  app=[
      ("Une cada estructura con su función: cerebro, médula espinal, nervios. Funciones: elaborar y controlar, conducir entre cerebro y nervios, llevar mensajes por el cuerpo. Escribe la función de la médula.", "Conducir entre cerebro y nervios", "La médula es el camino principal."),
      arith("Datos de ejemplo. Un esquema muestra 1 cerebro, 1 médula y 8 nervios. ¿Cuántas estructuras dibuja en total?", "1+1+8", "Se suman todas las estructuras."),
      ("Ordena de arriba hacia abajo en el cuerpo: A) médula en la columna, B) cerebro, C) nervio del pie. ¿Cuál es el orden?", "B, A, C", "Cabeza, espalda y pie."),
  ],
  rea=[
      ("Mario dice que los nervios y el cerebro hacen lo mismo. ¿Tiene razón? Responde Sí o No y explica.", "No; los nervios conducen y el cerebro elabora y controla", "Tienen funciones distintas."),
      ("Datos de ejemplo. Si se interrumpe la médula a media espalda, ¿qué comunicación se pierde? Escribe 'entre el cerebro y las piernas' o 'entre los ojos y las orejas'.", "Entre el cerebro y las piernas", "La médula conecta el cerebro con el cuerpo."),
  ],
  cha=[
      ("Escribe una comparación entre el cerebro y los nervios con el criterio 'función'.", "El cerebro elabora y controla; los nervios conducen mensajes", "Compara con un mismo criterio."),
      ("¿Por qué los huesos que rodean el cerebro y la médula son importantes?", "Porque los protegen de golpes", "Cráneo y columna son protectores."),
  ],
  context=[("Un esquema tiene 1 cerebro, 1 médula y 12 nervios. Se agregan 6 nervios más. ¿Cuántos nervios hay ahora?", "18", "12 + 6 = 18.")],
  selfcheck=[("¿Qué estructura elabora y controla?", "El cerebro", "Es el centro."), ("¿Qué estructuras conducen información?", "La médula espinal y los nervios", "Son los caminos."), ("¿Cómo protegemos el cerebro?", "Con casco y cuidando la cabeza", "El casco evita golpes fuertes.")],
  open_task=task("Haz una tabla con tres estructuras: cerebro, médula espinal y nervios. Columnas: dónde está, qué hace y qué pasaría si se daña. Escribe una comparación con un solo criterio y una forma de cuidar el sistema nervioso. Puedes usar un libro de la casa.", "Cerebro: cabeza, elabora y controla, no podría pensar. Nervios: todo el cuerpo, llevan mensajes. Comparación: el cerebro elabora y los nervios conducen. Cuidado: usar casco.", ["tabla completa", "criterio común", "una forma de cuidado"], ["tabla"], ["confundir funciones", "olvidar la ubicación"], "Pregunta cuál estructura le parece más difícil de proteger."),
  reinforce="Escribe tres formas de cuidar tu cabeza y tu espalda.",
  extend="Averigua qué es un reflejo y escríbelo con tus palabras.")

L(OA7, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: dos vasos de papel y un hilo largo con ayuda de una persona adulta.",
  use="Aprenderé a explicar con un modelo cómo viaja un mensaje por el sistema nervioso y qué límites tiene el modelo. Sirve para comunicar mis ideas con claridad.",
  prior=["Sé nombrar las estructuras del sistema nervioso.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo del sistema nervioso puede ser un esquema con flechas: estímulo → nervio → médula espinal → cerebro → médula espinal → nervio → músculo → respuesta. Cada flecha muestra hacia dónde viaja el mensaje. Esta secuencia sirve, por ejemplo, para el tacto: la piel de la mano siente un objeto y el cerebro decide apretarlo. La vista es parecida, pero el nervio del ojo llega directo al cerebro.",
      "Otro modelo es el teléfono de vasos: dos vasos de papel unidos por un hilo tenso. Cuando uno habla, la voz viaja por el hilo hasta el otro vaso. Representa cómo un mensaje viaja por un cable. Si el hilo se afloja o se corta, el mensaje no llega.",
      "Todo modelo tiene límites. El hilo no elabora la información como lo hace el cerebro, y el cuerpo real tiene millones de nervios. Un modelo sirve para entender una idea, no para copiar todo el cuerpo.",
  ],
  vocab=[("esquema", "dibujo simple con nombres y flechas"), ("mensaje", "información que viaja por los nervios"), ("tenso", "estirado, sin quedar flojo"), ("teléfono de vasos", "modelo con dos vasos unidos por un hilo"), ("límite", "lo que el modelo no muestra")],
  worked=[
      ("Leer el esquema", "Piel de la mano → nervio → médula → cerebro. ¿Qué estructura recibe el mensaje al final?", ["Leo las flechas de izquierda a derecha.", "Termina en el cerebro.", "Ahí se elabora."], "El cerebro"),
      ("Predecir en el modelo", "En el teléfono de vasos, si el hilo se afloja, ¿se escucha bien?", ["El hilo debe estar tenso.", "Si se afloja, el sonido no viaja.", "No se escucha bien."], "No, el sonido no viaja por un hilo flojo"),
  ],
  mistakes=[
      ("Pensar que el modelo muestra todo el sistema nervioso.", "Solo muestra una parte.", "Escribe un límite."),
      ("Olvidar que el cerebro elabora y no solo transmite.", "El hilo solo transmite; el cerebro elabora.", "Anota esa diferencia como límite."),
  ],
  rec=[
      ("En el esquema, ¿las flechas muestran hacia dónde viaja el mensaje?", "Sí", "Indican el camino."),
      ("¿El hilo del modelo representa un nervio o un hueso?", "Un nervio", "Conduce el mensaje."),
      ("Completa con «tenso» o «flojo»: el hilo del teléfono debe estar ______.", "Tenso", "Si está flojo no transmite."),
  ],
  und=[
      ("¿Qué sucede en el cerebro del esquema? A) Se elabora la información. B) Se rompe el hilo.", "A", "Ahí se piensa y decide."),
      ("¿Por qué el teléfono de vasos es un modelo? A) Porque representa cómo viaja un mensaje. B) Porque es un juguete caro.", "A", "Representa una idea."),
      ("¿Qué estructuras se omiten en un esquema que dice 'mano → cerebro'?", "Los nervios y la médula", "Faltan los caminos del mensaje."),
  ],
  app=[
      ("Ordena el esquema: A) músculo, B) cerebro, C) nervio de la vista. ¿Cuál es el orden de un mensaje que va desde la vista hasta el músculo?", "C, B, A", "Va desde el estímulo al cerebro y de ahí al músculo."),
      arith("Un esquema tiene 7 flechas. Se agregan 2 más para mostrar la médula. ¿Cuántas flechas tiene ahora?", "7+2", "Se suman las flechas nuevas."),
      ("Predice: si el hilo del teléfono se corta, ¿qué parte del cuerpo representa la falla? Elige: nervio o hueso.", "Nervio", "El hilo representa un nervio."),
  ],
  rea=[
      ("Ana dice que el teléfono de vasos explica cómo piensa el cerebro. ¿Tiene razón? Responde Sí o No y explica.", "No; solo muestra cómo viaja un mensaje", "No explica el pensamiento."),
      ("Luis dibujó 'ojo → músculo' sin cerebro. ¿Qué le falta y por qué?", "El cerebro, porque es quien elabora la información", "Sin él no se decide la respuesta."),
  ],
  cha=[
      ("Escribe un límite del modelo del teléfono de vasos y cómo lo mejorarías.", "El hilo no elabora información; agregaría una tarjeta de cerebro", "Reconoce lo que falta."),
      ("Dibuja con palabras un esquema para: sentir con la mano que un vaso resbala y apretarlo. Usa estructuras vistas.", "Mano → nervio → médula → cerebro → médula → nervio → músculo → apretar el vaso", "Va del estímulo a la respuesta."),
  ],
  context=[("Un grupo hace 4 teléfonos de vasos. Cada teléfono usa 2 vasos. ¿Cuántos vasos necesitan?", "8", "4 × 2 = 8.")],
  selfcheck=[("¿Qué muestran las flechas del esquema?", "El camino del mensaje", "Van del estímulo a la respuesta."), ("¿Qué representa el hilo del modelo?", "Un nervio", "Conduce el mensaje."), ("¿Qué límite tiene el modelo?", "No elabora información como el cerebro", "Un modelo siempre simplifica la realidad.")],
  open_task=task("Dibuja un esquema del camino de un mensaje en este caso: te dan una pelota en la mano, la sientes y la aprietas. Usa estas estructuras: piel de la mano, nervio, médula espinal, cerebro y músculo. Usa flechas con verbo. Escribe un límite de tu esquema. Si tienes ayuda, prueba también el teléfono de vasos.", "La piel de la mano siente la pelota → el nervio lleva el mensaje → la médula conduce → el cerebro decide → la médula conduce la orden → el nervio la lleva → el músculo aprieta la mano. Límite: no muestra los demás sentidos.", ["camino completo con flechas", "uso de cinco estructuras", "un límite"], ["esquema dibujado"], ["saltar el cerebro", "olvidar la respuesta"], "Pregunta qué cambiaría si en vez de sentir la pelota la viera."),
  reinforce="Dibuja un esquema con tres pasos que muestre cómo sientes un objeto tibio con la mano.",
  extend="Explica por qué el cerebro y la médula necesitan protección.")

# ---------------------------------------------------------------- OA 08
L(OA8, 1,
  materials="Este cuaderno y lápiz. Una persona adulta de confianza para conversar. No necesitas ninguna bebida.",
  use="Aprenderé qué es el alcohol y a separar lo que se observa de lo que se supone cuando se habla de sus efectos. Sirve para tomar decisiones informadas sobre mi salud.",
  prior=["Sé que mi cuerpo tiene sistema nervioso y músculos.", "Sé separar observación de interpretación."],
  explain=[
      "El alcohol es una sustancia que está en algunas bebidas para personas adultas, como el vino, la cerveza y el pisco. Es una droga que actúa sobre el sistema nervioso. Las personas menores de edad no deben consumirlo y es peligroso en exceso para cualquier persona.",
      "El consumo excesivo es beber mucho en poco tiempo o beber de forma muy frecuente. Los efectos que se pueden observar son: descoordinación, es decir, torpeza al caminar o al mover las manos; confusión, que es dificultad para pensar con claridad; y lentitud, que es reaccionar más tarde de lo normal.",
      "Para estudiar el tema se miran descripciones y se separan los datos de las opiniones. «Camina con pasos desparejos» es una observación. «Es una mala persona» es un juicio sin evidencia. Una persona que consume alcohol puede necesitar ayuda y apoyo, no burlas.",
  ],
  vocab=[("alcohol", "sustancia presente en ciertas bebidas para adultos que afecta al sistema nervioso"), ("consumo excesivo", "beber mucha cantidad o con mucha frecuencia"), ("descoordinación", "torpeza para mover el cuerpo de forma ordenada"), ("confusión", "dificultad para pensar con claridad"), ("lentitud", "reaccionar más tarde de lo normal")],
  worked=[
      ("Reconocer un efecto", "Una persona que bebió demasiado camina con pasos desparejos y casi se cae. ¿Qué efecto muestra?", ["Miro cómo se mueve.", "No puede mover el cuerpo de forma ordenada.", "Eso es descoordinación."], "Descoordinación"),
      ("Observación o juicio", "«Habla muy despacio y se confunde» y «Es una persona mala». ¿Cuál es observación?", ["Reviso qué se puede ver y oír.", "Hablar despacio se oye.", "'Es mala' es un juicio."], "Habla muy despacio y se confunde"),
  ],
  mistakes=[
      ("Pensar que beber poco o mucho es igual de seguro para niñas y niños.", "Los menores de edad no deben consumir alcohol.", "Recuerda: no es para menores."),
      ("Burlarse de quien bebió en exceso.", "Puede necesitar ayuda, no burlas.", "Pide ayuda a una persona adulta de confianza."),
  ],
  rec=[
      ("¿Descoordinación es torpeza al moverse o buena puntería?", "Torpeza al moverse", "Moverse de forma desordenada."),
      ("¿El alcohol afecta al sistema nervioso o al sistema esquelético?", "Al sistema nervioso", "Actúa sobre el cerebro y los nervios."),
      ("Completa con «menores» o «adultos»: el alcohol no es para ______ de edad.", "Menores", "Los menores no deben consumirlo."),
  ],
  und=[
      ("¿Cuál es un efecto del consumo excesivo? A) Lentitud para reaccionar. B) Más fuerza en los huesos.", "A", "El alcohol hace más lenta la respuesta."),
      ("¿Qué significa confusión?", "Dificultad para pensar con claridad", "Es uno de los efectos."),
      ("Marca la observación: A) Se tropieza al caminar. B) Seguro es un mal vecino.", "A", "A se ve; B es un juicio."),
  ],
  app=[
      arith("Datos de ejemplo. Un afiche nombra 3 efectos del alcohol y otro afiche nombra 2 más. ¿Cuántos efectos nombran los dos?", "3+2", "Se suman los efectos nombrados."),
      ("Clasifica el efecto: 'Le cuesta reaccionar rápido ante un ruido'. ¿Es lentitud o descoordinación?", "Lentitud", "Reacciona más tarde de lo normal."),
      ("Clasifica el efecto: 'No logra abotonar su camisa con sus dedos torpes'. ¿Es confusión o descoordinación?", "Descoordinación", "Los dedos no se mueven de forma ordenada."),
  ],
  rea=[
      ("Ema dice: 'Si un niño prueba un poco, no pasa nada'. ¿Es una afirmación segura? Responde Sí o No y explica.", "No; los menores no deben consumir alcohol", "El alcohol afecta a niñas y niños de forma peligrosa."),
      ("Un compañero se ríe de alguien que bebió. ¿Qué es mejor hacer? Escribe 'avisar a una persona adulta' o 'burlarse'.", "Avisar a una persona adulta", "Puede necesitar ayuda."),
  ],
  cha=[
      ("Escribe una observación y un juicio sobre alguien que camina con pasos desparejos.", "Observación: camina con pasos desparejos. Juicio: es un irresponsable", "La observación se ve; el juicio es una opinión."),
      ("Explica por qué el alcohol puede afectar la coordinación.", "Porque actúa sobre el sistema nervioso, que controla los movimientos", "El cerebro envía órdenes a los músculos."),
  ],
  context=[("Un afiche de salud tiene 5 dibujos sobre efectos del alcohol y 4 sobre cómo pedir ayuda. ¿Cuántos dibujos tiene?", "9", "5 + 4 = 9.")],
  selfcheck=[("Nombra tres efectos del consumo excesivo de alcohol.", "Descoordinación, confusión y lentitud", "Son los vistos en clase."), ("¿Pueden consumir alcohol las personas menores de edad?", "No", "Es peligroso para su salud."), ("¿Qué haces si ves a alguien en riesgo?", "Aviso a una persona adulta de confianza", "Puede necesitar ayuda.")],
  open_task=task("Con una persona adulta de tu casa, lee estas tres descripciones y clasifica el efecto: A) 'Se tropieza con las sillas', B) 'Tarda mucho en contestar una pregunta fácil', C) 'No recuerda dónde está'. Elige para cada una descoordinación, lentitud o confusión. Después escribe una observación y un juicio sobre una de ellas.", "A: descoordinación. B: lentitud. C: confusión. Observación: se tropieza con las sillas. Juicio: es un descuidado.", ["clasifica las tres", "una observación y un juicio", "usa los términos de la clase"], ["tabla de tres filas"], ["mezclar efectos", "anotar juicios como observaciones"], "Pregunta por qué la persona necesitaría ayuda y no burlas."),
  reinforce="Escribe con tus palabras qué es descoordinación, confusión y lentitud.",
  extend="Pregunta a una persona adulta de confianza por qué los menores no deben consumir alcohol.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Una persona adulta de tu casa o un libro de salud.",
  use="Aprenderé a hacer preguntas y a buscar información confiable sobre el alcohol. Sirve para investigar con calidad y no quedarme con rumores.",
  prior=["Sé qué es el consumo excesivo y sus efectos.", "Sé que una predicción se hace antes de comprobar."],
  explain=[
      "Investigar significa buscar información en diversas fuentes: libros, sitios web de organismos de salud, folletos de centros de salud, o preguntar a un profesional de la salud. Una fuente confiable dice quién la escribió, cuándo y en qué se basa. Un rumor o un mensaje sin autor no es confiable.",
      "Una pregunta comprobable de investigación puede ser: «¿Qué dicen los centros de salud sobre cómo afecta el alcohol a la coordinación?». Una predicción: «Dirán que afecta los movimientos, porque actúa sobre el sistema nervioso». Después se compara lo que dicen varias fuentes.",
      "Si varias fuentes confiables dicen lo mismo, la información es más segura. Si una fuente dice algo distinto y no explica por qué, desconfiamos. Al final, comunicamos lo que averiguamos con nuestras palabras, sin copiar, e indicando de dónde salió.",
  ],
  vocab=[("fuente", "lugar de donde sale una información"), ("fuente confiable", "fuente que dice quién la hizo y en qué se basa"), ("investigar", "buscar información para responder una pregunta"), ("rumor", "información sin autor ni prueba"), ("profesional de la salud", "persona formada para cuidar la salud, como un médico o una enfermera")],
  worked=[
      ("Elegir fuentes", "¿Cuál fuente es más confiable? A) Un folleto de un centro de salud con fecha y autor. B) Un mensaje sin nombre que circula entre amigos.", ["Busco quién escribió.", "El folleto tiene autor y fecha.", "El mensaje no tiene autor."], "A"),
      ("Comparar fuentes", "Fuente 1 dice que el alcohol afecta el equilibrio. Fuente 2 dice lo mismo. Fuente 3 (sin autor) dice que no afecta. ¿Qué es más seguro?", ["Dos fuentes coinciden.", "La tercera no tiene autor.", "Lo que coincide y tiene autor es más seguro."], "Que sí afecta el equilibrio"),
  ],
  mistakes=[
      ("Creer todo lo que aparece en un mensaje compartido.", "Puede ser un rumor.", "Revisa quién lo escribió y compáralo con otra fuente."),
      ("Copiar el texto sin explicarlo.", "No muestra que lo entendiste.", "Escribe con tus palabras y cita la fuente."),
  ],
  rec=[
      ("¿Una fuente confiable dice quién la escribió?", "Sí", "Eso permite saber de dónde viene."),
      ("¿Un rumor tiene autor o no tiene autor?", "No tiene autor", "Por eso no es confiable."),
      ("Completa con «una» o «varias»: para estar más seguros, usamos ______ fuentes.", "Varias", "Si coinciden, la información es más segura."),
  ],
  und=[
      ("¿Cuál es una fuente confiable? A) Un libro de salud con autor. B) Un mensaje sin autor.", "A", "Tiene autor y base."),
      ("¿Por qué conviene consultar varias fuentes?", "Para comprobar que coinciden", "Si coinciden, la información es más segura."),
      ("¿Qué debes hacer con la información que encuentras?", "Escribirla con tus palabras e indicar la fuente", "Así muestras que la entendiste."),
  ],
  app=[
      arith("Datos de ejemplo. Un grupo revisa 4 libros y 3 folletos. ¿Cuántas fuentes revisó?", "4+3", "Se suman las fuentes."),
      ("Datos de ejemplo. De 5 fuentes, 4 dicen que el alcohol afecta la coordinación. ¿Cuántas coinciden?", "4", "Las que dicen lo mismo."),
      ("Predice: una fuente de salud dirá que el alcohol afecta la rapidez de reacción. ¿Es una predicción razonable? Responde Sí o No.", "Sí", "Lo respalda el efecto de lentitud."),
  ],
  rea=[
      ("Mario copió un párrafo y no sabe qué significa. ¿Aprendió? Responde Sí o No y explica.", "No; hay que entenderlo y explicarlo con sus palabras", "Copiar no es comprender."),
      ("Datos de ejemplo. 3 fuentes con autor dicen A y 1 sin autor dice B. ¿Qué conclusión conviene?", "A, porque más fuentes con autor coinciden", "Se confía más en lo respaldado."),
  ],
  cha=[
      ("Escribe una pregunta de investigación sobre el alcohol y dónde buscarías.", "¿Cómo afecta el alcohol la coordinación? Buscaría en un libro de salud y en un folleto", "La pregunta es comprobable."),
      ("Explica por qué un cartel sin autor podría no ser confiable.", "Porque no se sabe quién lo hizo ni en qué se basa", "Falta quien responda por la información."),
  ],
  context=[("Un curso busca información en 6 fuentes. De ellas, 2 no tienen autor y no se usan. ¿Cuántas se usan?", "4", "6 − 2 = 4.")],
  selfcheck=[("¿Qué es una fuente confiable?", "Una que dice quién la hizo y en qué se basa", "Permite comprobar la información."), ("¿Por qué usar varias fuentes?", "Para ver si coinciden", "Aumenta la seguridad."), ("¿Cómo comunicas lo que averiguaste?", "Con tus palabras y citando la fuente", "Así se muestra que comprendiste.")],
  open_task=task("Con una persona adulta, lee dos fuentes sobre el alcohol: puede ser un libro de salud y un folleto de un centro de salud. Si no los tienes, pregunta a un profesional de la salud. Anota tu pregunta, tu predicción, qué dice cada fuente con tus palabras y si coinciden.", "Pregunta: ¿cómo afecta el alcohol la coordinación? Predicción: dirá que afecta los movimientos. Fuente 1: afecta la coordinación. Fuente 2: lo mismo. Coinciden.", ["pregunta y predicción", "dos fuentes con tus palabras", "indica si coinciden"], ["tabla de fuentes"], ["copiar sin entender", "no indicar la fuente"], "Pregunta cuál fuente le pareció más clara y por qué."),
  reinforce="Escribe tres características de una fuente confiable.",
  extend="Escribe una pregunta distinta de investigación sobre el cuidado de tu salud.")

L(OA8, 3,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar los efectos del alcohol en distintas funciones del cuerpo con un mismo criterio. Sirve para entender por qué es riesgoso.",
  prior=["Sé que el alcohol actúa sobre el sistema nervioso.", "Sé comparar con un criterio."],
  explain=[
      "El alcohol afecta distintas funciones al mismo tiempo. Afecta el equilibrio y los movimientos, porque el cerebro coordina los músculos. Afecta el pensamiento, porque produce confusión. Y afecta la rapidez de respuesta, porque hace más lento el viaje de los mensajes.",
      "Para compararlos uso un criterio: qué función del cuerpo se altera. Descoordinación altera el movimiento. Confusión altera el pensamiento. Lentitud altera la rapidez de respuesta. Estos tres efectos pueden juntarse y aumentan el riesgo de caídas y accidentes.",
      "Cuando alguien ha bebido en exceso, pueden ocurrir accidentes. Por eso es importante que esa persona no conduzca ni cruce solo una calle. Si ves a una persona así, avisa a un adulto de confianza. Cuidar a otros también es parte de cuidar la salud.",
  ],
  vocab=[("equilibrio", "capacidad de mantenerse en pie sin caerse"), ("función", "tarea que cumple una parte del cuerpo"), ("accidente", "suceso inesperado que puede causar daño"), ("riesgo", "posibilidad de que ocurra un daño"), ("prevenir", "hacer algo para evitar que ocurra un problema")],
  worked=[
      ("Clasificar efectos", "Tropezar con una silla, olvidar qué iba a decir y contestar muy tarde. ¿A qué efecto corresponde cada uno?", ["Tropezar = movimiento torpe.", "Olvidar = pensamiento.", "Contestar tarde = rapidez."], "Descoordinación, confusión y lentitud"),
      ("Evaluar un riesgo", "¿Es más riesgoso cruzar una calle con descoordinación y lentitud, o sin esos efectos?", ["Cruzar exige moverse bien y reaccionar rápido.", "Con esos efectos hay más riesgo.", "Se compara según la función necesaria."], "Con descoordinación y lentitud"),
  ],
  mistakes=[
      ("Pensar que los efectos solo son 'cosas graciosas'.", "Aumentan el riesgo de caídas y accidentes.", "Piensa en la seguridad."),
      ("Comparar efectos con criterios distintos.", "No hay un criterio común.", "Compara según la función afectada."),
  ],
  rec=[
      ("¿La descoordinación altera el movimiento o el pensamiento?", "El movimiento", "Es torpeza al mover el cuerpo."),
      ("¿La confusión altera el pensamiento o el equilibrio?", "El pensamiento", "Es dificultad para pensar con claridad."),
      ("Completa con «mayor» o «menor»: con lentitud el riesgo de accidente es ______.", "Mayor", "Se reacciona más tarde."),
  ],
  und=[
      ("¿Qué efecto hace más lenta la respuesta? A) Lentitud. B) Equilibrio.", "A", "Reaccionar tarde es lentitud."),
      ("¿Por qué el alcohol afecta los movimientos?", "Porque actúa sobre el sistema nervioso que coordina los músculos", "El cerebro envía las órdenes."),
      ("¿Qué debes hacer si ves a alguien en riesgo?", "Avisar a una persona adulta de confianza", "Puede necesitar ayuda."),
  ],
  app=[
      ("Une cada efecto con la función que altera: descoordinación, confusión, lentitud. Funciones: pensamiento, rapidez, movimiento. Escribe la que altera la lentitud.", "Rapidez", "Reacciona más tarde."),
      arith("Datos de ejemplo. Una persona tarda 2 segundos en reaccionar normalmente y 5 segundos cuando ha bebido en exceso. ¿Cuántos segundos más tarda?", "5-2", "Se resta el menor al mayor."),
      ("Ordena de más a menos riesgoso para cruzar una calle: A) con descoordinación y lentitud, B) con lentitud solamente, C) sin efectos.", "A, B, C", "Más efectos significan más riesgo."),
  ],
  rea=[
      ("Ana dice que una persona que bebió mucho puede conducir si va despacio. ¿Es correcto? Responde Sí o No y explica.", "No; sus reflejos y su pensamiento están afectados", "Conducir exige reaccionar bien."),
      ("Datos de ejemplo. Una persona con confusión y lentitud necesita cruzar una calle. ¿Qué es lo más seguro? Escribe 'esperar a un adulto' o 'cruzar rápido'.", "Esperar a un adulto", "Con esos efectos es más riesgoso."),
  ],
  cha=[
      ("Escribe una comparación entre descoordinación y confusión usando el criterio 'función alterada'.", "La descoordinación altera el movimiento y la confusión altera el pensamiento", "Compara según lo que se afecta."),
      ("Explica por qué estos efectos aumentan el riesgo de caídas.", "Porque se pierde el equilibrio y se reacciona más tarde", "Se combinan descoordinación y lentitud."),
  ],
  context=[("Una campaña de salud tiene 3 afiches sobre equilibrio, 2 sobre pensamiento y 4 sobre rapidez. ¿Cuántos afiches tiene en total?", "9", "3 + 2 + 4 = 9.")],
  selfcheck=[("¿Qué función altera la descoordinación?", "El movimiento", "Torpeza en el cuerpo."), ("¿Qué función altera la confusión?", "El pensamiento", "Cuesta pensar con claridad."), ("¿Qué función altera la lentitud?", "La rapidez de respuesta", "Se reacciona más tarde.")],
  open_task=task("Haz una tabla con tres columnas: efecto, función del cuerpo que altera y un riesgo en la vida diaria. Escribe una fila para descoordinación, otra para confusión y otra para lentitud. Escribe una frase con una forma de ayudar a una persona en riesgo.", "Descoordinación: movimiento; riesgo de caídas. Confusión: pensamiento; riesgo de perderse. Lentitud: rapidez; riesgo de accidentes. Ayuda: avisar a una persona adulta.", ["tabla completa", "criterio común", "una forma de ayuda"], ["tabla de tres filas"], ["inventar datos", "burlarse de las personas"], "Pregunta qué efecto podría ser más peligroso en la calle."),
  reinforce="Escribe dos situaciones diarias en que reaccionar rápido es importante.",
  extend="Escribe cómo ayudarías a un amigo que no quiere consumir alcohol pero le insisten.")

L(OA8, 4,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a explicar con un modelo cómo el alcohol llega a producir descoordinación, confusión y lentitud. Sirve para comprender los efectos y comunicarlos con claridad.",
  prior=["Sé qué hace el sistema nervioso.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo del efecto del alcohol puede ser un esquema con flechas: alcohol en el cuerpo → llega al cerebro → los mensajes del sistema nervioso se vuelven más lentos y confusos → descoordinación, confusión y lentitud. Cada flecha dice qué causa qué.",
      "El modelo ayuda a explicar. Si el cerebro recibe y envía los mensajes con dificultad, los músculos no reciben órdenes claras. Por eso la persona se mueve con torpeza. Si se interrumpe la causa, es decir, si no hay consumo excesivo, no aparecen esos efectos.",
      "Pero el modelo tiene límites. No muestra cuánto alcohol produce cada efecto, ni otros daños a largo plazo, como los que pueden afectar al hígado. Tampoco muestra todo lo que sienten las personas. Es un resumen, no un diagnóstico.",
  ],
  vocab=[("esquema causal", "dibujo con flechas que muestra qué causa qué"), ("a largo plazo", "después de mucho tiempo"), ("hígado", "órgano del abdomen que ayuda a limpiar la sangre"), ("diagnóstico", "decisión de un profesional sobre una enfermedad"), ("consumo excesivo", "beber mucho o con mucha frecuencia")],
  worked=[
      ("Leer el esquema", "Consumo excesivo → mensajes lentos en el cerebro → descoordinación. ¿Qué causa la descoordinación en el esquema?", ["Sigo las flechas hacia atrás.", "La causa es que los mensajes se vuelven lentos.", "Eso viene del consumo excesivo."], "Los mensajes lentos en el cerebro por el consumo excesivo"),
      ("Cortar la causa", "¿Qué pasa con los efectos si no hay consumo excesivo?", ["Sin causa no hay efecto.", "No se alteran los mensajes por esa razón.", "No aparecen esos efectos."], "No aparecen esos efectos"),
  ],
  mistakes=[
      ("Creer que el modelo permite diagnosticar a una persona.", "Solo un profesional de la salud puede hacerlo.", "Usa el modelo para explicar, no para diagnosticar."),
      ("Pensar que todos los efectos aparecen igual en todas las personas.", "Cada persona es distinta.", "Escribe 'pueden aparecer'."),
  ],
  rec=[
      ("¿El esquema causal muestra qué causa qué o la historia de una persona?", "Qué causa qué", "Las flechas indican la causa."),
      ("¿El alcohol llega al cerebro en el esquema, sí o no?", "Sí", "Así afecta los mensajes."),
      ("Completa con «nervioso» o «esquelético»: el alcohol afecta el sistema ______.", "Nervioso", "Actúa sobre el cerebro y los nervios."),
  ],
  und=[
      ("¿Qué muestran las flechas de un esquema causal? A) Qué provoca qué. B) Solo nombres.", "A", "Muestran causa y efecto."),
      ("¿Quién puede diagnosticar a una persona?", "Un profesional de la salud", "El modelo no reemplaza a un profesional."),
      ("¿Por qué el modelo tiene límites? A) Porque simplifica. B) Porque está mal.", "A", "Resume una idea compleja."),
  ],
  app=[
      ("Completa el esquema: alcohol → cerebro → mensajes lentos → ______. Elige: lentitud o más fuerza.", "Lentitud", "Es un efecto de los mensajes lentos."),
      arith("Un esquema tiene 5 recuadros y se agrega 1 recuadro para el hígado. ¿Cuántos recuadros tiene ahora?", "5+1", "Se suma el recuadro nuevo."),
      ("Predice con el modelo: si el cerebro no se ve afectado, ¿habrá descoordinación? Responde Sí o No.", "No", "Sin alteración del cerebro no aparece."),
  ],
  rea=[
      ("Luis dice que el esquema permite saber cuánto alcohol bebió alguien. ¿Tiene razón? Responde Sí o No y explica.", "No; el modelo no muestra cantidades", "Solo indica una relación general."),
      ("Ana ve a alguien tropezar y dice: 'Seguro bebió alcohol'. ¿Tiene evidencia? Responde Sí o No y explica.", "No; puede tropezar por otras causas", "Tropezar no prueba el consumo."),
  ],
  cha=[
      ("Escribe una explicación de dos frases usando el esquema causal para la lentitud.", "El alcohol llega al cerebro y los mensajes se vuelven lentos. Por eso la persona reacciona tarde", "Sigue la cadena."),
      ("Escribe un límite del modelo y cómo lo mejorarías.", "No muestra efectos a largo plazo; agregaría un recuadro para el hígado", "Reconoce lo que falta."),
  ],
  context=[("Un cartel de salud muestra 4 recuadros con efectos y 3 con consejos para pedir ayuda. ¿Cuántos recuadros tiene?", "7", "4 + 3 = 7.")],
  selfcheck=[("¿Qué muestra un esquema causal?", "Qué causa qué", "Las flechas indican la causa."), ("¿Qué límite tiene el modelo?", "No muestra cantidades ni todos los daños", "Es un resumen."), ("¿Quién diagnostica?", "Un profesional de la salud", "El modelo no diagnostica.")],
  open_task=task("Dibuja un esquema causal con al menos cuatro recuadros: consumo excesivo de alcohol, llega al cerebro, mensajes lentos y los tres efectos vistos. Usa flechas con verbo. Escribe un límite del esquema y a quién pedirías ayuda si alguien está en riesgo.", "Consumo excesivo → llega al cerebro → mensajes lentos → descoordinación, confusión y lentitud. Límite: no muestra cantidades. Pediría ayuda a una persona adulta de confianza.", ["cuatro recuadros con flechas", "un límite", "a quién pedir ayuda"], ["esquema dibujado"], ["usar el modelo para diagnosticar", "olvidar el límite"], "Pregunta qué parte del esquema le parece más importante."),
  reinforce="Dibuja un esquema de dos pasos que muestre un efecto del alcohol.",
  extend="Explica con tus palabras por qué un modelo no puede diagnosticar a una persona.")

L(OA8, 5,
  materials="Este cuaderno, lápiz, lápices de colores y cartulina opcional. Una persona adulta de confianza para conversar.",
  use="Aprenderé a comunicar con responsabilidad lo que averigüé sobre los efectos del alcohol. Sirve para informar a otras personas sin burlas ni mentiras.",
  prior=["Sé los efectos del consumo excesivo.", "Sé que debo usar fuentes confiables."],
  explain=[
      "Comunicar una conclusión significa explicarla con claridad a otras personas. Un buen mensaje de salud tiene el dato verdadero, la razón y qué hacer. Por ejemplo: «El alcohol causa descoordinación, confusión y lentitud porque afecta al sistema nervioso. Los menores no deben consumirlo. Si ves a alguien en riesgo, avisa a un adulto».",
      "El mensaje debe respetar a las personas. No se burla de quien tiene un problema ni usa miedo exagerado. Puede usar dibujos, un afiche o una exposición breve. Debe incluir la fuente de la información. No debe inventar cifras.",
      "También es importante saber decir no. Si alguien insiste en que pruebes alcohol, puedes decir «no, gracias» y alejarte. Puedes pedir ayuda a una persona adulta de confianza, como un familiar, un profesor o un profesional de la salud.",
  ],
  vocab=[("comunicar", "dar a conocer una idea con claridad"), ("mensaje de salud", "texto o imagen que informa cómo cuidar la salud"), ("respeto", "trato amable hacia las personas"), ("fuente", "lugar de donde sale la información"), ("persona de confianza", "adulto al que puedo pedir ayuda")],
  worked=[
      ("Evaluar un mensaje", "«El alcohol causa lentitud porque afecta al sistema nervioso. Los menores no deben consumirlo. Si ves a alguien en riesgo, avisa a un adulto». ¿Tiene dato, razón y qué hacer?", ["Busco el dato: causa lentitud.", "Busco la razón: afecta al sistema nervioso.", "Busco la acción: avisar a un adulto."], "Sí, tiene las tres partes"),
      ("Respuesta asertiva", "Alguien te ofrece alcohol. ¿Cuál respuesta es mejor? A) 'No, gracias'. B) 'Bueno, solo un poco.'", ["Pienso en mi salud.", "Los menores no deben consumir.", "A cuida mi salud."], "A"),
  ],
  mistakes=[
      ("Hacer un afiche con cifras inventadas.", "Una cifra falsa quita credibilidad.", "Usa solo datos de fuentes confiables."),
      ("Burlarse de personas en el afiche.", "Es irrespetuoso y no ayuda.", "Muestra efectos y cómo ayudar."),
  ],
  rec=[
      ("¿Un mensaje de salud debe incluir un dato verdadero o una cifra inventada?", "Un dato verdadero", "La información debe ser correcta."),
      ("¿Puedes decir 'no, gracias' si te ofrecen alcohol?", "Sí", "Es una forma de cuidarte."),
      ("Completa con «adulto» o «desconocido»: pido ayuda a un ______ de confianza.", "Adulto", "Es quien puede ayudar."),
  ],
  und=[
      ("¿Qué incluye un buen mensaje de salud? A) Dato, razón y qué hacer. B) Solo un dibujo.", "A", "Así es claro."),
      ("¿Por qué se debe respetar a las personas en el mensaje?", "Porque burlarse no ayuda y es irrespetuoso", "El objetivo es cuidar."),
      ("¿A quién puedes pedir ayuda?", "A una persona adulta de confianza", "Puede ayudar o buscar apoyo."),
  ],
  app=[
      arith("Un curso de 28 estudiantes hace afiches en parejas. ¿Cuántos afiches hacen?", "28//2", "Se divide el curso en parejas."),
      ("Ordena el mensaje con letras: A) 'Avisa a un adulto', B) 'El alcohol causa confusión', C) 'Porque afecta al sistema nervioso'. ¿Cuál es el mejor orden?", "B, C, A", "Dato, razón y qué hacer."),
      ("Un afiche dice: 'Todos los que beben se vuelven peligrosos'. ¿Es un mensaje respetuoso y exacto? Responde Sí o No.", "No", "Generaliza y estigmatiza."),
  ],
  rea=[
      ("Mario dice que basta con asustar a los niños para que no consuman. ¿Es mejor asustar o informar? Escribe una palabra.", "Informar", "La información clara ayuda a decidir."),
      ("Datos de ejemplo. Un afiche afirma que el alcohol 'cura el frío'. ¿Qué haces? Responde 'revisar otra fuente' o 'creerlo'.", "Revisar otra fuente", "Hay que comprobar con fuentes confiables."),
  ],
  cha=[
      ("Escribe un mensaje de tres frases para tu curso sobre el alcohol: dato, razón y qué hacer.", "El alcohol causa lentitud porque afecta al sistema nervioso. Los menores no deben consumirlo. Si ves a alguien en riesgo, avisa a un adulto", "Contiene las tres partes."),
      ("Escribe una frase para decir no a un ofrecimiento de alcohol.", "No, gracias; no quiero", "Es clara y respetuosa."),
  ],
  context=[("Un curso reparte 5 afiches por sala en 6 salas. ¿Cuántos afiches reparten?", "30", "5 × 6 = 30.")],
  selfcheck=[("¿Qué debe tener un mensaje de salud?", "Dato, razón y qué hacer", "Con esas partes el mensaje es completo."), ("¿Puede un menor consumir alcohol?", "No", "Es peligroso para su salud."), ("¿A quién pides ayuda?", "A una persona adulta de confianza", "Ella puede apoyarte y ayudarte.")],
  open_task=task("Haz un afiche o una exposición breve para tu curso sobre los efectos del consumo excesivo de alcohol. Incluye: tres efectos (descoordinación, confusión y lentitud), la razón (afecta al sistema nervioso), que los menores no deben consumir, y a quién pedir ayuda. Indica de qué fuente salió tu información. Muéstralo a una persona adulta de confianza.", "Afiche: 'El alcohol afecta el sistema nervioso'. Efectos: descoordinación, confusión, lentitud. Los menores no deben consumir. Pide ayuda a un adulto. Fuente: libro de salud.", ["tres efectos", "razón y mensaje", "fuente y ayuda"], ["afiche o guion"], ["inventar cifras", "burlarse"], "Pregunta qué parte del mensaje es más clara y cuál mejoraría."),
  reinforce="Escribe una frase para decir no a un ofrecimiento de alcohol.",
  extend="Escribe una lista de tres personas adultas de confianza a quienes podrías pedir ayuda.")

"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 07 (fuerzas gravitacional, de roce y elástica) y OA 08 (presión en sólidos, líquidos y gases)."""
from __future__ import annotations

from student_content_cn7_a import L, task
from student_lessons import arith

OA7, OA8 = "CN07 OA 07", "CN07 OA 08"

# ---------------------------------------------------------------- OA 07
L(OA7, 1,
  materials="Este cuaderno y lápiz. Opcional: una banda elástica, una regla y 3 monedas iguales para imaginar el experimento; todos los datos están escritos en los ejercicios.",
  use="Aprenderé qué son las fuerzas gravitacional, de roce y elástica y a transformar una duda en una pregunta que se pueda medir. Sirve para planificar una investigación experimental.",
  prior=["Sé que una pregunta comprobable se responde midiendo u observando.", "Sé que en un experimento se cambia una sola condición."],
  explain=[
      "Una fuerza es una interacción que puede cambiar el movimiento de un objeto o deformarlo. Se mide en newton (N) con un instrumento llamado dinamómetro. La fuerza gravitacional es la atracción que ejerce la Tierra sobre los objetos hacia su centro; esa fuerza es el peso. Un objeto de 1 kg pesa aproximadamente 10 N.",
      "La fuerza de roce aparece entre dos superficies en contacto y se opone al deslizamiento. Depende de cómo son las superficies (lisas o rugosas) y de qué tan apretadas están. La fuerza elástica es la que ejerce un resorte o una banda elástica cuando se estira o se comprime: tiende a recuperar su forma.",
      "Una pregunta medible nombra qué se cambia y qué se mide, con su unidad. «¿Cuánto se alarga (en cm) una banda elástica al colgarle 1, 2 y 3 monedas?» es medible. «¿Qué banda es más bonita?» no lo es, porque depende del gusto.",
  ],
  vocab=[("fuerza", "interacción que cambia el movimiento o deforma un objeto"), ("newton (N)", "unidad de medida de la fuerza"), ("peso", "fuerza con que la Tierra atrae un objeto"), ("roce", "fuerza entre superficies en contacto que se opone al deslizamiento"), ("fuerza elástica", "fuerza con que un resorte o elástico deformado recupera su forma")],
  worked=[
      ("Peso de un objeto", "Una mochila tiene una masa de 4 kg. ¿Cuál es su peso aproximado en newton?", ["1 kg pesa aproximadamente 10 N.", "4 × 10 = 40."], "Aproximadamente 40 N"),
      ("Pregunta medible", "¿Cuál es medible? A) ¿Cuántos cm avanza un auto de juguete al soltarlo en una rampa sobre cartón? B) ¿Qué superficie es más agradable?", ["Busco algo que se cuente o mida con unidad.", "En A se miden centímetros.", "En B depende del gusto."], "A"),
  ],
  mistakes=[
      ("Confundir masa en kg con peso en N.", "La masa es la cantidad de materia; el peso es una fuerza.", "Recuerda: 1 kg pesa unos 10 N."),
      ("Escribir preguntas sin decir qué se mide ni con qué unidad.", "No se puede comprobar sin una medición.", "Nombra la variable que cambia y la que mides con su unidad."),
  ],
  rec=[
      ("¿En qué unidad se mide la fuerza: newton o metro?", "Newton", "El newton (N) es la unidad de fuerza."),
      ("¿Qué instrumento mide fuerzas: el dinamómetro o el termómetro?", "El dinamómetro", "Marca la fuerza en newton."),
      ("La atracción de la Tierra sobre los objetos, ¿es fuerza gravitacional o elástica?", "Gravitacional", "Es la fuerza que llamamos peso."),
  ],
  und=[
      ("¿Cuál es una pregunta medible? A) Cuánto se alarga, en cm, una banda elástica al colgarle 3 monedas; B) Qué banda elástica es más linda", "A", "Se mide con regla; el gusto no se mide."),
      ("La fuerza de roce, ¿ayuda o se opone al deslizamiento entre dos superficies?", "Se opone", "Frena el deslizamiento."),
      ("¿Qué es la fuerza elástica? A) La que ejerce una banda estirada para recuperar su forma; B) La que atrae los objetos al suelo.", "A", "La B describe la fuerza gravitacional."),
  ],
  app=[
      arith("Un balón de 2 kg se cuelga de un dinamómetro. ¿Cuántos newton marca aproximadamente?", "2*10", "Se multiplica la masa por 10."),
      ("En el experimento «¿Cuánto se alarga una banda al colgarle 1, 2 y 3 monedas?», ¿qué variable se cambia?", "El número de monedas", "Es lo que se modifica."),
      ("En ese mismo experimento, ¿qué variable se mide y en qué unidad?", "El alargamiento, en cm", "Es lo que se mide con la regla."),
  ],
  rea=[
      ("Dos estudiantes miden la misma mochila: uno dice «tiene una masa de 4 kg» y otro «pesa 40 N». ¿Pueden hablar de la misma mochila? Responde Sí o No.", "Sí", "4 kg pesan aproximadamente 40 N."),
      ("¿Cuál es una versión medible de «¿cómo afecta la superficie al roce?»? A) Cuántos cm avanza un auto de juguete soltado en una rampa sobre cartón, toalla y mesa lisa; B) Qué superficie es más agradable", "A", "Mide una distancia con una regla."),
  ],
  cha=[
      ("Un dinamómetro de ejemplo mide hasta 50 N. ¿Se puede medir en él el peso de una mochila de 6 kg? Responde Sí o No.", "No", "6 kg pesan unos 60 N, más que 50 N."),
      ("En «¿Cuántos N se necesitan para empezar a mover una caja sobre cartón y sobre alfombra?», ¿qué se mide?", "La fuerza, en N", "Se lee en el dinamómetro."),
  ],
  context=[("Dato de ejemplo. Un dinamómetro marca 12 N al tirar una caja sobre alfombra y 8 N sobre cartón. ¿Cuántos N más se necesitan sobre alfombra?", "4", "12 − 8 = 4 N.")],
  selfcheck=[("¿Qué es una fuerza?", "Una interacción que cambia el movimiento o deforma un objeto", "Se mide en newton."), ("¿Cuánto pesa aproximadamente un objeto de 1 kg?", "10 N", "Es la regla de la clase."), ("¿Qué debe tener una pregunta medible?", "La variable que cambia y la que se mide, con unidad", "Así se puede comprobar.")],
  open_task=task("Escribe tres preguntas medibles, una para cada fuerza: gravitacional (con una pelota), de roce (con un auto de juguete en una rampa) y elástica (con una banda elástica). Para cada una indica qué variable cambias y qué mides, con su unidad.", "Gravitacional: ¿cuántos segundos tarda en caer una pelota desde 1 m y desde 2 m? Cambia: altura; mide: segundos. Roce: ¿cuántos cm avanza un auto sobre cartón y sobre toalla? Cambia: superficie; mide: cm. Elástica: ¿cuántos cm se alarga la banda con 1, 2 y 3 monedas? Cambia: monedas; mide: cm.", ["tres preguntas medibles", "variable cambiada y medida", "unidades"], ["tres preguntas con sus variables"], ["no indicar la unidad", "preguntar por gustos"], "Pregunta qué instrumento usarías para medir en cada caso."),
  reinforce="Escribe el nombre de las tres fuerzas de la clase y un ejemplo de cada una.",
  extend="Explica por qué la masa de un objeto es distinta de su peso.")

L(OA7, 2,
  materials="Este cuaderno y lápiz. Opcional: un libro, un auto de juguete, una regla y tres superficies (cartón, toalla y mesa lisa). Todos los datos están escritos en los ejercicios.",
  use="Aprenderé a diseñar una comparación controlada para investigar el roce, la gravedad o la elasticidad. Sirve para que los resultados se puedan atribuir a una sola causa.",
  prior=["Sé qué es una pregunta medible.", "Sé que hay una variable que se cambia y otra que se mide."],
  explain=[
      "Una comparación controlada cambia solo una variable y mantiene iguales las demás. A lo que se cambia se le llama variable independiente; a lo que se mide, variable dependiente; a lo que se mantiene igual, variables controladas. Si dos cosas cambian a la vez, no se puede saber cuál causó el resultado.",
      "Ejemplo para el roce: se suelta un mismo auto de juguete desde la misma altura de una rampa de libros y se mide cuántos centímetros avanza sobre cartón, toalla y mesa lisa. La variable independiente es la superficie; la dependiente, la distancia; y se controlan el auto, la altura y el punto de salida.",
      "Un ensayo puede tener errores por casualidad. Por eso se repite cada condición, por ejemplo tres veces, y se usa el promedio: se suman los resultados y se divide por el número de ensayos. Además se cuida la seguridad: superficies estables, objetos livianos y nada de bandas estiradas hacia la cara de otra persona.",
  ],
  vocab=[("variable independiente", "lo que se cambia a propósito"), ("variable dependiente", "lo que se mide como resultado"), ("variable controlada", "lo que se mantiene igual"), ("ensayo", "cada repetición de una medición"), ("promedio", "suma de los resultados dividida por el número de ensayos")],
  worked=[
      ("Identificar variables", "Un auto de juguete se suelta desde 20 cm de altura sobre cartón, toalla y mesa lisa, y se mide la distancia que avanza. ¿Cuál es la variable independiente, la dependiente y una controlada?", ["Lo que cambia es la superficie.", "Lo que se mide es la distancia.", "Se mantiene el auto y la altura."], "Independiente: superficie; dependiente: distancia; controlada: altura (o el auto)"),
      ("Calcular un promedio", "En la toalla el auto avanzó 30, 33 y 27 cm en tres ensayos. ¿Cuál es el promedio?", ["Sumo: 30 + 33 + 27 = 90.", "Divido en 3: 90 ÷ 3 = 30."], "30 cm"),
  ],
  mistakes=[
      ("Cambiar la altura de la rampa y la superficie a la vez.", "No se sabe cuál causó el resultado.", "Cambia solo una variable."),
      ("Sacar conclusiones con un único ensayo.", "Un ensayo puede tener un error por casualidad.", "Repite tres veces y usa el promedio."),
  ],
  rec=[
      ("¿La variable independiente es la que se cambia o la que se mide?", "La que se cambia", "Se modifica a propósito."),
      ("Si dos variables cambian a la vez, ¿se puede saber cuál causó el resultado: sí o no?", "No", "Los efectos se mezclan."),
      ("¿Para qué sirve repetir un ensayo: para reducir errores o para cambiar la pregunta?", "Para reducir errores", "Un solo ensayo puede fallar por casualidad."),
  ],
  und=[
      ("En un experimento de roce se compara un auto sobre cartón y sobre toalla. ¿Cuál debe mantenerse igual? A) La altura de la rampa; B) La superficie.", "A", "La superficie es la variable que se cambia."),
      ("¿Qué diseño es correcto? A) El mismo auto en tres superficies, soltado desde la misma altura; B) Un auto distinto en cada superficie y a distintas alturas.", "A", "Cambia solo una variable."),
      ("¿Cuál es la variable dependiente en «distancia que avanza el auto en cada superficie»?", "La distancia", "Es lo que se mide."),
  ],
  app=[
      arith("En la mesa lisa el auto avanzó 80, 84 y 76 cm en tres ensayos. ¿Cuál es el promedio?", "(80+84+76)//3", "Se suman y se divide en 3."),
      arith("En el cartón el auto avanzó 42, 45 y 39 cm. ¿Cuál es el promedio?", "(42+45+39)//3", "Se suman y se divide en 3."),
      ("Con los promedios 30 cm (toalla), 42 cm (cartón) y 80 cm (mesa lisa), ¿en cuál superficie hay menos roce? A) En la toalla; B) En la mesa lisa.", "B", "Avanza más porque el roce lo frena menos."),
  ],
  rea=[
      ("Una estudiante comparó el auto sobre cartón desde 20 cm de altura y sobre toalla desde 30 cm. ¿Qué error tiene su diseño?", "Cambió dos variables: superficie y altura", "No puede atribuir la diferencia al roce."),
      ("Un grupo midió una vez cada superficie y concluyó. ¿Qué mejora le sugieres?", "Repetir cada condición tres veces y usar el promedio", "Reduce el efecto de errores casuales."),
  ],
  cha=[
      ("Diseña una comparación para la fuerza elástica: ¿qué variable cambiarías? A) El número de monedas colgadas de la misma banda; B) La banda usada en cada medición.", "A", "Con la misma banda se evita otra variable."),
      ("En ese diseño, ¿cuál sería una variable controlada?", "La banda elástica (o la regla)", "Debe mantenerse igual."),
  ],
  context=[("Dato de ejemplo. Un grupo hizo 3 ensayos en alfombra: 18, 21 y 15 cm. ¿Cuántos cm es el promedio?", "18", "(18 + 21 + 15) ÷ 3 = 18.")],
  selfcheck=[("¿Qué es la variable independiente?", "La que se cambia a propósito", "Se modifica para ver el efecto."), ("¿Cómo se calcula un promedio?", "Se suman los resultados y se divide por el número de ensayos", "Así se resumen varios ensayos."), ("¿Por qué se controlan las demás variables?", "Para saber qué causó el resultado", "Si no, los efectos se mezclan.")],
  open_task=task("Diseña un experimento para comparar el roce en tres superficies con un auto de juguete y una rampa de libros. Escribe la pregunta, la variable independiente, la dependiente, dos variables controladas, cuántos ensayos harás y una medida de seguridad.", "Pregunta: ¿cuántos cm avanza el auto sobre cartón, toalla y mesa lisa? Independiente: superficie. Dependiente: distancia. Controladas: auto y altura. Tres ensayos por superficie. Seguridad: la rampa debe estar estable.", ["pregunta medible", "variables bien rotuladas", "ensayos y seguridad"], ["diseño escrito"], ["cambiar dos variables", "no repetir ensayos"], "Pregunta qué harías si un ensayo da un valor muy distinto."),
  reinforce="Escribe una variable independiente, una dependiente y una controlada de un experimento con una banda elástica.",
  extend="Explica por qué repetir tres veces es mejor que medir una sola vez.")

L(OA7, 3,
  materials="Este cuaderno y lápiz. Las tablas de datos están escritas en los ejercicios; opcional: papel cuadriculado para dibujar el gráfico.",
  use="Aprenderé a registrar y representar mediciones de fuerzas y a buscar patrones. Sirve para predecir cuánto se alarga una banda y para comparar el roce.",
  prior=["Sé diseñar una comparación controlada.", "Sé calcular un promedio."],
  explain=[
      "Los resultados se ordenan en una tabla y se representan en un gráfico. En una banda elástica, si se cuelgan pesas iguales una a una, se mide la longitud de la banda. Los datos suelen mostrar un patrón: cada pesa adicional alarga la banda en una cantidad parecida. Ese patrón permite predecir cuánto medirá con otra pesa.",
      "La fuerza elástica tiene un límite. Si se estira demasiado, la banda ya no vuelve a su largo original y el patrón se rompe. En el roce, se mide la fuerza necesaria para mover una caja con un dinamómetro: una superficie más rugosa requiere más fuerza. Además, suele hacer falta un poco más de fuerza para empezar a mover que para mantener la caja en movimiento.",
      "Al representar, el eje horizontal lleva la variable independiente (por ejemplo, el número de pesas) y el vertical la dependiente (el largo en cm). Cada eje debe llevar su nombre y su unidad. Los puntos que se alejan mucho del patrón se revisan, porque pueden ser un error de medición.",
  ],
  vocab=[("patrón", "regularidad que se repite en los datos"), ("predicción", "valor estimado para una condición no medida"), ("eje", "línea de un gráfico con la variable y su unidad"), ("límite elástico", "estiramiento más allá del cual el material no recupera su forma"), ("error de medición", "diferencia entre el valor medido y el real por causas del instrumento o del método")],
  worked=[
      ("Buscar el patrón", "Largo de una banda: sin pesas, 10 cm; con 1 pesa, 12 cm; con 2 pesas, 14 cm; con 3 pesas, 16 cm. ¿Cuánto se alarga por cada pesa?", ["De 10 a 12 hay 2 cm.", "De 12 a 14 hay 2 cm.", "El patrón es 2 cm por pesa."], "2 cm por pesa"),
      ("Predecir", "Con ese patrón, ¿cuánto medirá la banda con 5 pesas, si no pasa su límite?", ["Sin pesas mide 10 cm.", "5 pesas alargan 5 × 2 = 10 cm.", "10 + 10 = 20."], "20 cm"),
  ],
  mistakes=[
      ("Predecir sin pensar en el límite elástico.", "Un estiramiento excesivo rompe el patrón.", "Predice solo dentro del rango medido."),
      ("Poner el número de pesas en el eje vertical.", "La variable independiente va en el eje horizontal.", "Ubica cada variable en su eje."),
  ],
  rec=[
      ("¿Qué variable va en el eje horizontal: la que se cambia o la que se mide?", "La que se cambia", "Es la variable independiente."),
      ("Si la banda mide 10 cm sin pesas y 14 cm con 2 pesas, ¿cuántos cm se alargó?", "4", "14 − 10 = 4."),
      ("¿Hace falta más fuerza para empezar a mover una caja o para mantenerla en movimiento?", "Para empezar a mover", "El roce inicial suele ser un poco mayor."),
  ],
  und=[
      ("Una banda mide 10, 12, 14 y 16 cm con 0, 1, 2 y 3 pesas. ¿Qué patrón hay? A) Aumenta 2 cm por pesa; B) Aumenta 4 cm por pesa.", "A", "De 10 a 12, de 12 a 14 y de 14 a 16 hay 2 cm."),
      ("¿Qué indica un punto muy alejado del patrón? A) Un posible error de medición; B) Que el patrón es falso siempre.", "A", "Conviene repetir esa medición."),
      ("¿Qué le ocurre a la banda si se estira más allá de su límite elástico?", "No recupera su forma original", "La banda queda deformada."),
  ],
  app=[
      arith("Con el patrón de 2 cm por pesa y 10 cm sin pesas, ¿cuánto medirá la banda con 4 pesas?", "10+4*2", "Se suma el alargamiento al largo inicial."),
      arith("Una caja necesita 9 N para empezar a moverse y 6 N para mantenerse en movimiento. ¿Cuántos N más para empezar?", "9-6", "Se resta."),
      ("Datos de ejemplo del roce: mesa lisa 4 N, cartón 7 N, alfombra 12 N. Ordena de menor a mayor roce. ¿Cuál queda en el medio?", "El cartón", "Su valor 7 N está entre 4 y 12."),
  ],
  rea=[
      ("Una banda mide 10, 12, 14, 16 y 25 cm con 0, 1, 2, 3 y 4 pesas. ¿Qué valor se aparta del patrón y qué podría explicarlo?", "25 cm; pasó su límite elástico o hubo un error", "El patrón predecía 18 cm."),
      ("Un compañero predice que con 100 pesas la banda medirá 210 cm. ¿Por qué es una mala predicción?", "Porque no se midió tanto y la banda tiene un límite", "Solo se puede predecir dentro del rango medido."),
  ],
  cha=[
      ("Se miden tres ensayos de la fuerza para mover una caja en cartón: 7 N, 8 N y 6 N. ¿Cuál es el promedio?", "7 N", "(7 + 8 + 6) ÷ 3 = 7."),
      ("Se tira de una caja: en alfombra se necesitan 12 N y en mesa lisa 4 N. ¿Cuántas veces mayor es la fuerza en alfombra?", "3", "12 ÷ 4 = 3."),
  ],
  context=[("Dato de ejemplo. Una banda mide 8 cm sin pesas y 20 cm con 4 pesas. ¿Cuántos cm se alarga por cada pesa si el alargamiento es parejo?", "3", "(20 − 8) ÷ 4 = 3 cm.")],
  selfcheck=[("¿Qué es un patrón en los datos?", "Una regularidad que se repite", "Un patrón permite predecir."), ("¿Qué variable va en el eje horizontal?", "La independiente", "La que se cambia."), ("¿Qué es el límite elástico?", "El estiramiento más allá del cual no se recupera la forma", "Rompe el patrón.")],
  open_task=task("Con estos datos de ejemplo de una banda (pesas: 0, 1, 2, 3, 4; largo en cm: 10, 12, 14, 16, 18), dibuja una tabla y un gráfico de puntos con ejes rotulados. Calcula el alargamiento por pesa y predice el largo con 6 pesas, indicando un límite de tu predicción.", "Eje horizontal: pesas; eje vertical: largo (cm). Alargamiento: 2 cm por pesa. Con 6 pesas: 22 cm. Límite: solo si no pasa su límite elástico.", ["tabla y gráfico con unidades", "patrón calculado", "predicción con límite"], ["tabla, gráfico y dos frases"], ["intercambiar los ejes", "no mencionar el límite"], "Pregunta qué mediría para comprobar la predicción."),
  reinforce="Calcula el alargamiento por pesa de una banda que pasa de 10 cm a 16 cm con 3 pesas.",
  extend="Explica por qué una predicción solo es confiable dentro del rango medido.")

L(OA7, 4,
  materials="Este cuaderno y lápiz. Las situaciones son descripciones; no necesitas hacer los experimentos.",
  use="Aprenderé a distinguir en qué situaciones actúan la fuerza gravitacional, la de roce y la elástica, y a usar resultados para explicar un fenómeno. Sirve para analizar situaciones cotidianas.",
  prior=["Sé medir y representar fuerzas.", "Sé que el roce se opone al deslizamiento."],
  explain=[
      "En una misma situación pueden actuar varias fuerzas. Una pelota que cae está bajo la fuerza gravitacional. Un auto de juguete que se frena sobre una toalla está bajo la fuerza de roce. Un resorte que vuelve a su largo después de estirarlo actúa por la fuerza elástica.",
      "Para distinguir qué fuerza explica un resultado, se pregunta: ¿hay una atracción hacia la Tierra?, ¿hay superficies en contacto que se oponen al deslizamiento?, ¿hay un objeto deformado que intenta volver a su forma? En una rampa, la gravedad hace bajar el auto y el roce lo frena.",
      "Las conclusiones deben apoyarse en los datos. Si el auto avanza más sobre la mesa lisa que sobre la toalla, el dato apoya que la mesa lisa produce menos roce. Si la banda no vuelve a su largo, se superó el límite elástico. Una conclusión no debe afirmar más de lo medido.",
  ],
  vocab=[("fuerza gravitacional", "atracción de la Tierra hacia su centro"), ("fuerza de roce", "oposición al deslizamiento entre superficies"), ("fuerza elástica", "fuerza con que un objeto deformado recupera su forma"), ("resultado", "dato obtenido en una medición"), ("conclusión", "afirmación apoyada en los resultados")],
  worked=[
      ("Qué fuerza actúa", "Un libro se desliza por una rampa y se detiene en la alfombra. ¿Qué fuerza lo hace bajar y cuál lo detiene?", ["La Tierra lo atrae hacia abajo: gravitacional.", "La alfombra se opone al deslizamiento: roce."], "Gravitacional lo hace bajar; el roce lo detiene"),
      ("Apoyar una conclusión", "Un auto avanza 80 cm en mesa lisa y 30 cm en toalla. ¿Qué conclusión apoyan los datos?", ["En la mesa lisa avanza más.", "Eso indica menos roce.", "La toalla produce más roce."], "La toalla produce más roce que la mesa lisa"),
  ],
  mistakes=[
      ("Decir que el roce hace que los objetos caigan.", "Caen por la fuerza gravitacional; el roce los frena.", "Asocia la caída a la gravedad."),
      ("Decir que cualquier resorte vuelve siempre a su forma.", "Si supera su límite, queda deformado.", "Recuerda el límite elástico."),
  ],
  rec=[
      ("Una manzana cae de un árbol. ¿Qué fuerza actúa: gravitacional o elástica?", "Gravitacional", "La Tierra la atrae."),
      ("Una zapatilla frena en el piso. ¿Qué fuerza se opone al deslizamiento: el roce o la gravedad?", "El roce", "Actúa entre la zapatilla y el piso."),
      ("Un resorte estirado vuelve a su forma. ¿Qué fuerza actúa: elástica o de roce?", "Elástica", "El resorte intenta recuperar su forma."),
  ],
  und=[
      ("Una persona salta en un trampolín y este se deforma y la impulsa hacia arriba. ¿Qué fuerza la impulsa? A) La elástica; B) La de roce.", "A", "El trampolín deformado recupera su forma."),
      ("Una bicicleta se detiene al apretar los frenos. ¿Qué fuerza actúa entre las zapatas y la rueda? A) La de roce; B) La gravitacional.", "A", "Las superficies en contacto se oponen al giro."),
      ("Una pelota lanzada hacia arriba cae de vuelta. ¿Qué fuerza la hace caer?", "La gravitacional", "La Tierra la atrae."),
  ],
  app=[
      ("Cuatro situaciones: una hoja cae, un freno de bicicleta, una cuerda elástica que se contrae, una caja que se arrastra. ¿Cuántas se deben a la fuerza de roce?", "2", "El freno de bicicleta y la caja arrastrada."),
      arith("Una caja tiene una masa de 5 kg. ¿Cuántos N pesa aproximadamente (1 kg ≈ 10 N)?", "5*10", "Peso = masa × 10."),
      ("Datos de ejemplo: un auto avanza 80 cm en mesa lisa, 42 cm en cartón y 30 cm en toalla. ¿Qué superficie tiene más roce?", "La toalla", "Es donde menos avanza."),
  ],
  rea=[
      ("Una banda no vuelve a su largo original después de estirarla mucho. ¿Qué explica el resultado?", "Superó su límite elástico", "La banda quedó deformada."),
      ("Un auto baja una rampa y se detiene en la alfombra. Explica en una frase qué fuerzas actúan.", "La gravedad lo hace bajar y el roce lo detiene", "Son dos fuerzas con efectos opuestos."),
  ],
  cha=[
      ("Un grupo concluye «la alfombra no tiene roce porque el auto se detuvo». ¿Qué error tiene? A) El auto se detuvo justamente por el roce; B) La alfombra es demasiado blanda.", "A", "El roce frena el deslizamiento."),
      ("Datos: la caja pesa 20 N y necesita 8 N para moverse sobre cartón. En alfombra necesita 14 N. ¿Cuántos N más se necesitan en la alfombra?", "6", "14 − 8 = 6."),
  ],
  context=[("Dato de ejemplo. Un resorte mide 12 cm sin carga y 20 cm con una pesa. Al quitar la pesa mide 12 cm. ¿Cuántos cm se estiró?", "8", "20 − 12 = 8 cm; volvió a su largo, así que no pasó su límite elástico.")],
  selfcheck=[("¿Qué fuerza explica que un objeto caiga?", "La gravitacional", "La Tierra lo atrae."), ("¿Qué fuerza frena un objeto que se desliza?", "El roce", "Se opone al deslizamiento."), ("¿Qué fuerza hace que un resorte vuelva a su forma?", "La elástica", "Recupera su forma.")],
  open_task=task("Analiza esta situación inventada: un auto de juguete baja una rampa de libros, avanza por una mesa lisa y se detiene en una toalla. Indica qué fuerza hace bajar el auto, qué fuerza lo frena y qué resultado medido apoyaría tu respuesta (con un dato de ejemplo).", "La gravedad hace bajar el auto; el roce con la toalla lo frena. Dato: avanza 80 cm en mesa lisa y 30 cm en toalla.", ["identifica gravedad y roce", "usa un dato", "no afirma más de lo medido"], ["tres frases y un dato"], ["decir que el roce lo hace caer", "no usar un dato"], "Pregunta qué mediría para comprobar la afirmación."),
  reinforce="Escribe una situación cotidiana para cada fuerza: gravitacional, de roce y elástica.",
  extend="Explica con la rampa por qué la gravedad y el roce actúan a la vez.")

# ---------------------------------------------------------------- OA 08
L(OA8, 1,
  materials="Este cuaderno y lápiz. Los cálculos usan N y cm² y están escritos en los ejercicios. Opcional: plasticina y la parte roma de un lápiz para comparar.",
  use="Aprenderé que la presión depende de la fuerza y del área de contacto. Sirve para explicar por qué un cuchillo afilado corta más que uno sin filo y por qué las raquetas de nieve evitan hundirse.",
  prior=["Sé que una fuerza se mide en newton.", "Sé calcular áreas de rectángulos."],
  explain=[
      "La presión es la fuerza que se reparte en cada unidad de área. Se calcula dividiendo la fuerza por el área sobre la que actúa: presión = fuerza ÷ área. En esta clase usamos newton por centímetro cuadrado (N/cm²); la unidad oficial es el pascal (Pa), donde 1 Pa es 1 newton en cada metro cuadrado.",
      "Con la misma fuerza, un área pequeña produce más presión que un área grande. Por eso la punta de un clavo penetra la madera y un cuchillo afilado corta: toda la fuerza se concentra en un área mínima. En cambio, los esquís o las raquetas de nieve reparten el peso en un área grande y disminuyen la presión, lo que evita hundirse. Una persona de 600 N parada en dos pies que ocupan 300 cm² ejerce 2 N/cm²; en un pie que ocupa 150 cm² ejerce 4 N/cm².",
      "La presión también aumenta si aumenta la fuerza con la misma área. En herramientas mecánicas como tijeras, cinceles y hachas se afila el borde para que el área sea pequeña y la presión grande. Siempre se manejan las herramientas con cuidado y bajo supervisión.",
  ],
  vocab=[("presión", "fuerza dividida por el área sobre la que actúa"), ("área de contacto", "superficie donde se apoya o actúa una fuerza"), ("N/cm²", "unidad usada en esta clase para medir presión"), ("pascal (Pa)", "unidad oficial de presión: 1 N por metro cuadrado"), ("concentrar", "reunir una fuerza en un área pequeña")],
  worked=[
      ("Calcular una presión", "Una caja que pesa 120 N se apoya en un área de 60 cm². ¿Cuál es la presión?", ["Presión = fuerza ÷ área.", "120 ÷ 60 = 2."], "2 N/cm²"),
      ("Cambiar el área", "La misma caja se apoya ahora sobre un área de 30 cm². ¿Cómo cambia la presión?", ["120 ÷ 30 = 4 N/cm².", "El área se redujo a la mitad.", "La presión se duplicó."], "Aumenta a 4 N/cm²; se duplica"),
  ],
  mistakes=[
      ("Creer que la presión depende solo de la fuerza.", "También depende del área de contacto.", "Divide la fuerza entre el área."),
      ("Pensar que un objeto más pesado siempre se hunde más.", "Un área grande reparte el peso.", "Compara las presiones, no solo los pesos."),
  ],
  rec=[
      ("¿Con la misma fuerza, el área pequeña produce más o menos presión que el área grande?", "Más presión", "La fuerza se concentra."),
      ("¿La fórmula es fuerza ÷ área o fuerza × área?", "Fuerza ÷ área", "Es la definición de presión."),
      ("¿Un cuchillo afilado tiene un filo de área pequeña o grande?", "Pequeña", "Por eso concentra la fuerza."),
  ],
  und=[
      ("¿Por qué las raquetas de nieve evitan hundirse? A) Reparten el peso en un área grande; B) Aumentan el peso de la persona.", "A", "Disminuyen la presión sobre la nieve."),
      ("Un clavo penetra la madera por la punta y no por la cabeza. ¿Por qué? A) La punta tiene menos área y más presión; B) La punta es más pesada.", "A", "La misma fuerza en menos área da más presión."),
      ("Si la fuerza se mantiene igual y el área se hace 3 veces mayor, ¿la presión aumenta o disminuye?", "Disminuye", "Se reparte en más área."),
  ],
  app=[
      arith("Una persona de 480 N se apoya en un pie que ocupa 160 cm². ¿Cuál es la presión en N/cm²?", "480//160", "Fuerza ÷ área."),
      arith("Un tractor de 24.000 N se apoya sobre 6.000 cm² de orugas. ¿Cuál es la presión en N/cm²?", "24000//6000", "Fuerza ÷ área."),
      arith("Un bloque pesa 600 N. Apoyado en su cara grande (300 cm²) y en su cara chica (100 cm²), ¿cuántos N/cm² más de presión ejerce en la cara chica?", "600//100-600//300", "Se calcula la presión de cada cara y se resta."),
  ],
  rea=[
      ("Explica por qué una tijera con filo desgastado corta peor aunque se apriete con la misma fuerza.", "Porque el filo tiene más área y la presión es menor", "Menos presión corta peor."),
      ("Una persona camina sobre nieve blanda y se hunde con zapatos normales, pero no con esquís. Explica con presión.", "Los esquís reparten el peso y disminuyen la presión", "Mayor área, menor presión."),
  ],
  cha=[
      ("Se pone una pesa de 80 N sobre dos bases: base A de 20 cm² y base B de 40 cm². ¿Qué base hace más presión y cuánto es la diferencia en N/cm²?", "La A; 2 N/cm² más", "A: 80 ÷ 20 = 4; B: 80 ÷ 40 = 2."),
      ("Un cincel de ejemplo ejerce 50 N sobre una punta de 2 cm². ¿Qué presión ejerce en N/cm²?", "25", "50 ÷ 2 = 25."),
  ],
  context=[("Dato de ejemplo. Una caja de 180 N se apoya sobre 4 patas pequeñas que suman 30 cm² y luego sobre una base de 90 cm². ¿Cuántos N/cm² baja la presión al cambiar a la base?", "4", "180 ÷ 30 = 6 y 180 ÷ 90 = 2; 6 − 2 = 4 N/cm².")],
  selfcheck=[("¿Cómo se calcula la presión?", "Fuerza dividida por área", "Es la definición."), ("¿Qué pasa con la presión si el área disminuye?", "Aumenta", "La fuerza se concentra."), ("¿Por qué un cuchillo afilado corta mejor?", "Porque el filo tiene poca área y concentra la fuerza", "La presión es mayor.")],
  open_task=task("Elige tres objetos de la casa que usen área pequeña para aumentar la presión (por ejemplo un destornillador, un tenedor, una tijera escolar) y tres que usen área grande para disminuirla (por ejemplo una tabla ancha, la suela de una zapatilla, una cama). Explica en una frase por qué cada uno funciona así. No uses objetos filosos sin supervisión.", "Área pequeña: tijera (filo), destornillador (punta), tenedor (puntas). Área grande: zapatilla, mochila con correa ancha, tabla de picar. Explicación: reparten o concentran la fuerza.", ["tres objetos de cada tipo", "explicación con área y fuerza", "no manipula objetos peligrosos"], ["lista de seis objetos"], ["confundir área con peso", "usar objetos filosos sin supervisión"], "Pregunta qué cambiaría si agrandara el área de la punta."),
  reinforce="Calcula la presión de una fuerza de 90 N sobre 30 cm².",
  extend="Explica por qué los camiones pesados usan muchas ruedas.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Los datos de presión son de ejemplo y están escritos en los ejercicios; no hace falta ninguna actividad con agua profunda.",
  use="Aprenderé cómo cambia la presión dentro de un líquido con la profundidad. Sirve para explicar por qué los oídos duelen al bucear en una piscina honda y por qué las represas son más gruesas abajo.",
  prior=["Sé que la presión es fuerza ÷ área.", "Sé que los líquidos fluyen y toman la forma del recipiente."],
  explain=[
      "Un líquido ejerce presión sobre el fondo y las paredes del recipiente. La presión dentro de un líquido aumenta con la profundidad, porque hay más líquido encima. Además actúa en todas las direcciones: hacia abajo, hacia los lados y hacia arriba. A la misma profundidad, la presión es igual en todos los puntos.",
      "En el agua, cada 10 metros de profundidad la presión aumenta aproximadamente en 1 atmósfera (atm). En la superficie actúa la atmósfera, de 1 atm. A 10 m, la presión total es de unas 2 atm; a 20 m, unas 3 atm. Por eso los oídos se sienten apretados al sumergirse, y los buceadores deben seguir normas estrictas y entrenamiento.",
      "La presión depende de la profundidad y de la densidad del líquido, no de la forma del recipiente. Las paredes de las represas son más gruesas en la base, porque ahí la presión es mayor. Un submarino debe resistir la presión creciente a medida que baja.",
  ],
  vocab=[("profundidad", "distancia medida desde la superficie del líquido hacia abajo"), ("atmósfera (atm)", "unidad de presión: la que ejerce el aire al nivel del mar"), ("densidad", "cantidad de materia en un volumen"), ("presión total", "suma de la presión del aire y la del líquido"), ("represa", "muro que contiene agua")],
  worked=[
      ("Presión en el agua", "¿Cuál es la presión total a 20 m de profundidad? (Cada 10 m se suma 1 atm; en la superficie hay 1 atm.)", ["20 m son 2 tramos de 10 m: 2 atm.", "Se suma la atmósfera de la superficie: 1 + 2 = 3."], "3 atm"),
      ("Dónde es mayor", "Dos puntos en una piscina: uno a 1 m y otro a 3 m de profundidad. ¿Dónde es mayor la presión?", ["A mayor profundidad, más agua encima.", "3 m es más profundo que 1 m."], "A 3 m"),
  ],
  mistakes=[
      ("Creer que la presión en un líquido solo actúa hacia abajo.", "Actúa en todas las direcciones.", "Piensa en las paredes y en los objetos sumergidos."),
      ("Pensar que un recipiente más ancho produce más presión en el fondo.", "Depende de la profundidad y de la densidad, no de la forma.", "Compara las alturas del líquido."),
  ],
  rec=[
      ("¿La presión en un líquido aumenta o disminuye con la profundidad?", "Aumenta", "Hay más líquido encima."),
      ("¿La presión de un líquido actúa en todas las direcciones: verdadero o falso?", "Verdadero", "Actúa hacia abajo, hacia los lados y hacia arriba."),
      ("En la superficie del mar, ¿cuántas atm ejerce el aire?", "1 atm", "Es la presión atmosférica normal."),
  ],
  und=[
      ("¿Por qué las represas son más gruesas en la base? A) Porque ahí la presión del agua es mayor; B) Porque ahí hay menos agua.", "A", "Mayor profundidad significa mayor presión."),
      ("Dos recipientes tienen formas distintas pero el agua llega a la misma altura. ¿La presión en el fondo es igual o distinta?", "Igual", "Depende de la profundidad, no de la forma."),
      ("Un buzo desciende de 5 m a 15 m. ¿Qué ocurre con la presión que siente? A) Aumenta; B) Disminuye.", "A", "A más profundidad, mayor presión."),
  ],
  app=[
      arith("¿Cuál es la presión total, en atm, a 30 m de profundidad en el agua? (1 atm en la superficie y +1 atm cada 10 m.)", "1+30//10", "Se suma la atmósfera de la superficie."),
      arith("¿Cuántos metros de profundidad corresponden a una presión total de 4 atm? (Parte de 1 atm en la superficie, +1 atm cada 10 m.)", "(4-1)*10", "Se restan la atmósfera de la superficie y se multiplica por 10."),
      ("En un tubo con agua se miden presiones de ejemplo: 1,2 atm a 2 m, 1,5 atm a 5 m y 1,8 atm a 8 m. ¿A qué profundidad es mayor la presión?", "A 8 m", "Tiene el mayor valor."),
  ],
  rea=[
      ("Un submarino baja de 100 m a 300 m. ¿Qué debe cambiar en su diseño? Explica en una frase.", "Debe resistir una presión mayor", "La presión aumenta con la profundidad."),
      ("Si dos puntos están a la misma profundidad en un lago, ¿tienen la misma presión? Responde Sí o No.", "Sí", "La presión es igual a la misma profundidad."),
  ],
  cha=[
      ("En una botella de ejemplo con tres agujeros a distintas alturas, el chorro del agujero más bajo llega más lejos. Explica la razón.", "Porque en el punto más bajo la presión es mayor", "A mayor profundidad hay más presión."),
      ("Un buzo desciende de 10 m a 40 m. ¿Cuántas atm sube la presión?", "3", "40 m − 10 m = 30 m, o sea 3 tramos de 10 m."),
  ],
  context=[("Dato de ejemplo. Una piscina tiene 1 m de profundidad en un extremo y 4 m en el otro. ¿Cuántos metros más profundo es un extremo que el otro?", "3", "4 − 1 = 3 m; en el extremo hondo la presión es mayor.")],
  selfcheck=[("¿Cómo cambia la presión en un líquido con la profundidad?", "Aumenta", "Hay más líquido encima."), ("¿Hacia dónde actúa la presión de un líquido?", "En todas las direcciones", "También hacia arriba y hacia los lados."), ("¿Por qué las represas son más gruesas en la base?", "Porque ahí hay mayor presión", "Está a mayor profundidad.")],
  open_task=task("Dibuja una represa con agua. Marca con flechas la presión en tres profundidades (superficie, mitad y fondo), haciendo las flechas más largas a mayor profundidad. Escribe por qué la pared debe ser más gruesa abajo y cuánta presión total habría a 20 m.", "Flechas cortas arriba, medianas al medio y largas abajo. La pared es más gruesa abajo porque ahí la presión es mayor. A 20 m: 3 atm.", ["flechas crecientes", "explica el grosor", "calcula 3 atm"], ["dibujo y dos frases"], ["flechas iguales", "olvidar la atmósfera de la superficie"], "Pregunta qué pasaría con la pared si el agua fuera más densa."),
  reinforce="Escribe una frase que relacione profundidad y presión en un líquido.",
  extend="Explica por qué los buzos sienten presión en los oídos al descender.")

L(OA8, 3,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están en los ejercicios.",
  use="Aprenderé qué es la presión atmosférica, cómo cambia con la altura y qué efectos tiene en la vida diaria. Sirve para explicar por qué se tapan los oídos en un cerro y por qué una bolsa sellada se infla en altura.",
  prior=["Sé que la presión es fuerza ÷ área.", "Sé que el aire es una mezcla de gases."],
  explain=[
      "La atmósfera es la capa de aire que rodea la Tierra. El aire tiene peso, y ese peso ejerce una presión sobre todo lo que está en la superficie: la presión atmosférica. Al nivel del mar es de aproximadamente 1 atm, o 1.013 hectopascales (hPa). Actúa en todas las direcciones, aunque no la sentimos porque nuestro cuerpo la equilibra por dentro.",
      "La presión atmosférica disminuye con la altura, porque hay menos aire encima. A unos 5.500 m es aproximadamente la mitad que al nivel del mar. En Santiago, a unos 520 m sobre el nivel del mar, es cercana a 950 hPa, algo menor que en la costa. Por eso una bolsa sellada en la costa se hincha al subir a un cerro, y los oídos pueden taparse al cambiar de altura.",
      "También afecta la ebullición del agua: con menor presión, el agua hierve a menor temperatura (a nivel del mar hierve a 100 °C; a 3.000 m, cerca de 90 °C), por lo que cocinar en altura toma más tiempo. Cuando tomamos líquido con una bombilla, el aire de la boca baja la presión y la atmósfera empuja el líquido hacia arriba.",
  ],
  vocab=[("atmósfera", "capa de aire que rodea la Tierra"), ("presión atmosférica", "presión que ejerce el peso del aire"), ("hectopascal (hPa)", "unidad de presión: 100 pascales"), ("altura", "distancia vertical sobre el nivel del mar"), ("ebullición", "paso rápido de líquido a gas al hervir")],
  worked=[
      ("Presión y altura", "Datos de ejemplo: costa, 1.013 hPa; Santiago, 950 hPa; cerro alto, 800 hPa. ¿Dónde hay más aire encima?", ["Mayor presión indica más aire encima.", "El mayor valor es 1.013 hPa."], "En la costa"),
      ("Bolsa en altura", "Una bolsa de papas sellada en la costa se hincha en un cerro. ¿Por qué?", ["En el cerro la presión externa es menor.", "El aire de dentro empuja más que el de fuera."], "Porque la presión exterior disminuye y el aire de dentro la expande"),
  ],
  mistakes=[
      ("Creer que el aire no pesa.", "Tiene peso y ejerce presión.", "Piensa en la capa de aire sobre nosotros."),
      ("Pensar que la presión atmosférica es igual en un cerro que en la costa.", "Disminuye con la altura.", "Compara las alturas."),
  ],
  rec=[
      ("¿La presión atmosférica aumenta o disminuye con la altura?", "Disminuye", "Hay menos aire encima."),
      ("¿El aire tiene peso: verdadero o falso?", "Verdadero", "Por eso ejerce presión."),
      ("¿Cuántas atm hay al nivel del mar, aproximadamente?", "1", "Es la presión atmosférica normal."),
  ],
  und=[
      ("¿Dónde hay mayor presión atmosférica? A) En la costa; B) En la cima de un cerro alto.", "A", "Hay más aire encima."),
      ("¿Por qué se tapan los oídos al subir a un cerro? A) Cambia la presión del aire; B) Se acaba el oxígeno de inmediato.", "A", "La presión externa disminuye y el oído debe equilibrarla."),
      ("En una montaña muy alta, ¿el agua hierve a una temperatura mayor o menor que a nivel del mar?", "Menor", "Con menor presión, hierve antes."),
  ],
  app=[
      arith("Al nivel del mar hay 1.013 hPa y en una ciudad de ejemplo a 1.200 m hay 880 hPa. ¿Cuántos hPa menos hay en esa ciudad?", "1013-880", "Se resta."),
      arith("Una cumbre tiene la mitad de la presión del nivel del mar (1.013 hPa; redondea a 1.000 hPa). ¿Cuántos hPa tiene aproximadamente?", "1000//2", "Es la mitad."),
      ("Una persona toma un jugo con una bombilla. ¿Qué empuja el líquido hacia arriba? A) La presión atmosférica sobre el líquido; B) La fuerza de roce.", "A", "Al bajar la presión en la boca, el aire exterior empuja el líquido."),
  ],
  rea=[
      ("Una bolsa sellada en altura se infla. Explica con presión qué ocurre.", "La presión exterior baja y el aire de dentro se expande", "Hay menos presión afuera."),
      ("¿Por qué cocinar legumbres en altura toma más tiempo? Responde en una frase.", "Porque el agua hierve a menor temperatura", "Con menos presión hierve a menos de 100 °C."),
  ],
  cha=[
      ("A 3.000 m el agua hierve a unos 90 °C. ¿Cuántos °C menos que a nivel del mar (100 °C)?", "10", "100 − 90 = 10 °C."),
      ("Alguien dice: «En un avión no hay presión, por eso se tapan los oídos». Corrígelo en una frase.", "Hay presión; lo que cambia es su valor al subir o bajar", "El aire siempre ejerce presión."),
  ],
  context=[("Dato de ejemplo. Un instrumento que mide la presión del aire marca 1.000 hPa en la mañana y 990 hPa en la tarde. ¿Cuántos hPa bajó?", "10", "1.000 − 990 = 10 hPa.")],
  selfcheck=[("¿Qué es la presión atmosférica?", "La presión que ejerce el peso del aire", "Actúa en todas las direcciones."), ("¿Cómo cambia con la altura?", "Disminuye", "Hay menos aire encima."), ("¿Qué le pasa al agua que hierve en altura?", "Hierve a menor temperatura", "La presión es menor.")],
  open_task=task("Con estos datos de ejemplo (nivel del mar: 1.013 hPa; ciudad a 520 m: 950 hPa; cerro a 3.000 m: 700 hPa), ordena los lugares de mayor a menor presión y explica con una frase por qué una bolsa sellada se infla al subir de la costa al cerro.", "Orden: nivel del mar, ciudad, cerro. La bolsa se infla porque afuera hay menos presión y el aire de dentro se expande.", ["orden correcto", "explica con presión", "usa los datos"], ["orden y una frase"], ["ordenar al revés", "decir que el aire no pesa"], "Pregunta qué pasaría con una botella cerrada al bajar al nivel del mar."),
  reinforce="Escribe un efecto de la presión atmosférica en la vida diaria.",
  extend="Explica por qué la presión atmosférica disminuye con la altura.")

L(OA8, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están en los ejercicios.",
  use="Aprenderé a explicar con un modelo de partículas la presión en gases y líquidos y cómo funcionan las máquinas hidráulicas. Sirve para entender frenos, gatas y neumáticos.",
  prior=["Sé que la presión es fuerza ÷ área.", "Sé que la materia está formada por partículas en movimiento."],
  explain=[
      "En un gas, las partículas están muy separadas y se mueven en todas las direcciones, chocando con las paredes del recipiente. Esos choques producen la presión. Si hay más partículas, o si la temperatura sube y se mueven más rápido, hay más choques y aumenta la presión. Si el gas se comprime en un volumen menor, los choques son más frecuentes y la presión sube.",
      "Por eso un neumático inflado tiene más presión que uno desinflado, y por eso la presión sube un poco si se calienta. En los líquidos las partículas están juntas y casi no se pueden comprimir. Si se aplica presión sobre un líquido encerrado, esta se transmite a todo el líquido.",
      "Una máquina hidráulica usa esa propiedad. Una fuerza pequeña sobre un émbolo de área pequeña crea una presión que se transmite a un émbolo de área grande y produce una fuerza mayor. Así funcionan las gatas hidráulicas y los frenos de los autos. La fuerza se multiplica, pero el émbolo grande se mueve menos distancia.",
  ],
  vocab=[("partícula", "unidad muy pequeña que forma la materia"), ("choque", "golpe de una partícula con una pared u otra partícula"), ("émbolo", "pieza que se mueve dentro de un cilindro y empuja el fluido"), ("máquina hidráulica", "máquina que usa un líquido para transmitir presión"), ("compresión", "reducción del volumen de un gas")],
  worked=[
      ("Calentar un gas", "Un gas se calienta en un recipiente cerrado. ¿Cómo cambia su presión y por qué?", ["Las partículas se mueven más rápido.", "Chocan más veces y con más fuerza.", "La presión aumenta."], "Aumenta, por más choques con las paredes"),
      ("Gata hidráulica", "Se empuja con 50 N un émbolo de 5 cm². La presión se transmite a otro émbolo de 100 cm². ¿Qué fuerza obtiene el émbolo grande?", ["Presión = 50 ÷ 5 = 10 N/cm².", "La fuerza en el grande es 10 × 100 = 1.000 N."], "1.000 N"),
  ],
  mistakes=[
      ("Pensar que las partículas de un gas se quedan quietas.", "Se mueven constantemente y chocan.", "Imagina choques continuos con las paredes."),
      ("Creer que una máquina hidráulica crea energía.", "Multiplica la fuerza, pero el émbolo grande se mueve menos.", "La fuerza mayor cuesta menos recorrido."),
  ],
  rec=[
      ("¿Qué produce la presión de un gas: los choques de las partículas con las paredes o su color?", "Los choques", "A más choques, mayor presión."),
      ("¿Se pueden comprimir fácilmente los líquidos: sí o no?", "No", "Sus partículas están muy juntas."),
      ("¿Qué usa una gata hidráulica: un líquido o un gas?", "Un líquido", "Transmite la presión."),
  ],
  und=[
      ("Si se reduce el volumen de un gas encerrado, ¿qué pasa con su presión? A) Aumenta; B) Disminuye.", "A", "Hay más choques por la misma cantidad de partículas."),
      ("¿Por qué conviene medir la presión de los neumáticos cuando están fríos? A) Porque al calentarse la presión sube; B) Porque el aire se acaba.", "A", "El calor aumenta los choques."),
      ("En una máquina hidráulica, ¿qué se transmite por el líquido? A) La presión; B) El color.", "A", "La presión se transmite a todo el líquido."),
  ],
  app=[
      arith("Se aplica 40 N sobre un émbolo de 4 cm². ¿Qué presión se transmite, en N/cm²?", "40//4", "Fuerza ÷ área."),
      arith("Con esa presión de 10 N/cm², ¿qué fuerza se obtiene en un émbolo de 50 cm²?", "10*50", "Presión × área."),
      ("En el frenado de un auto, el pedal empuja un émbolo pequeño y el líquido de frenos empuja émbolos grandes. ¿Qué se logra? A) Una fuerza mayor sobre los frenos; B) Un menor uso del líquido de frenos.", "A", "El área grande multiplica la fuerza."),
  ],
  rea=[
      ("Explica por qué un globo se infla al soplar usando el modelo de partículas.", "Entran más partículas de gas y chocan más con las paredes", "Más choques aumentan la presión."),
      ("¿Por qué el émbolo grande de una gata se mueve menos que el pequeño?", "Porque el mismo volumen de líquido se reparte en un área mayor", "La fuerza se multiplica a costa de la distancia."),
  ],
  cha=[
      ("Una gata hidráulica tiene émbolos de 2 cm² y 80 cm². Si se empuja con 25 N en el pequeño, ¿qué fuerza obtiene el grande?", "1.000 N", "25 ÷ 2 × 80 = 1.000 N, porque 25 × 40 = 1.000."),
      ("Un compañero propone usar aire en vez de aceite en los frenos. ¿Qué problema tendría? A) El aire se comprime y no transmite bien la presión; B) El aire pesa más que el aceite.", "A", "Los gases se comprimen; los líquidos casi no."),
  ],
  context=[("Dato de ejemplo. Un neumático tiene 30 unidades de presión en frío y 33 unidades después de rodar. ¿Cuántas unidades subió?", "3", "33 − 30 = 3 unidades.")],
  selfcheck=[("¿Cómo se origina la presión de un gas?", "Por los choques de sus partículas con las paredes", "A más choques, más presión."), ("¿Por qué las máquinas hidráulicas usan líquidos?", "Porque los líquidos casi no se comprimen y transmiten la presión", "Así se multiplica la fuerza."), ("¿Qué ocurre con la presión si se calienta un gas encerrado?", "Aumenta", "Las partículas se mueven más rápido.")],
  open_task=task("Dibuja dos recipientes con partículas de gas: uno con 10 partículas y otro con 20, del mismo tamaño, y flechas de choque con las paredes. Explica en dos frases cuál tiene mayor presión y qué pasaría si el segundo se calienta.", "El de 20 partículas tiene más choques y mayor presión. Si se calienta, las partículas se mueven más rápido y la presión sube aún más.", ["dibujo con 10 y 20 partículas", "explica con choques", "predice el efecto del calor"], ["dibujo y dos frases"], ["decir que el recipiente de 10 tiene más presión", "olvidar los choques"], "Pregunta qué pasaría si se agrandara el recipiente."),
  reinforce="Escribe cómo explica el modelo de partículas la presión de un gas.",
  extend="Explica por qué en una máquina hidráulica la fuerza se multiplica pero no la energía.")

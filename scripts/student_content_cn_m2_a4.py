"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 09 (movimiento rectilíneo uniforme y acelerado) y OA 10 (fuerza neta, leyes de Newton y diagrama de cuerpo libre)."""
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


OA9 = "CN2M OA 09"
OA10 = "CN2M OA 10"

# ---------------------------------------------------------------- OA 09

L(OA9, 1,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios. Si quieres medir, usa un pasillo o patio despejado, una huincha o pasos de largo conocido y un reloj o celular con cronómetro.",
  use="Aprenderé a describir un movimiento con un sistema de referencia, a distinguir distancia y desplazamiento y a escribir una pregunta que se pueda investigar sobre movimiento.",
  prior=["Sé medir longitudes en metros y tiempos en segundos.", "Sé operar con números enteros positivos y negativos."],
  explain=[
      "Para describir un movimiento hay que elegir un sistema de referencia: un punto de origen, una dirección positiva y un reloj. La posición es dónde está el objeto respecto del origen, medida en metros (m) sobre una recta. Un objeto se mueve si su posición cambia con el tiempo respecto de ese sistema. Quien viaja sentado en un bus está quieto respecto del bus, pero se mueve respecto del paradero.",
      "El desplazamiento es el cambio de posición: posición final menos posición inicial, con signo según la dirección elegida. La distancia recorrida es el largo total del camino y nunca es negativa. Si caminas 6 m hacia la derecha y luego 2 m de vuelta, recorriste 8 m, pero tu desplazamiento es 4 m. La rapidez media es la distancia recorrida dividida por el tiempo empleado y se mide en metros por segundo (m/s).",
      "Una pregunta investigable sobre movimiento nombra el sistema de referencia y lo que se mide. Por ejemplo: «¿Cuántos segundos tarda una persona en caminar 10 m en línea recta por un pasillo, a paso normal y a paso lento?». La pregunta «¿es más lindo correr que caminar?» no se puede investigar, porque «lindo» no indica qué medir.",
  ],
  vocab=[("sistema de referencia", "origen, dirección positiva y reloj con que se describe un movimiento"), ("posición", "lugar del objeto medido desde el origen"), ("desplazamiento", "posición final menos posición inicial"), ("distancia recorrida", "largo total del camino, sin signo"), ("rapidez media", "distancia recorrida dividida por el tiempo")],
  worked=[
      ("Posición y desplazamiento", "El origen está en la puerta de una sala y la derecha es positiva. Una persona pasa de la posición 3 m a la posición 11 m. ¿Cuál es su desplazamiento?", ["Posición final menos inicial: 11 − 3.", "El resultado es 8, positivo: fue hacia la derecha."], "8 m hacia la derecha"),
      ("Rapidez media", "Un carrito de juguete recorre 12 m en 4 s sobre un piso plano. ¿Cuál es su rapidez media?", ["Se divide la distancia por el tiempo: 12 ÷ 4.", "Se escribe la unidad: metros por segundo."], "3 m/s"),
  ],
  mistakes=[
      ("Decir que el desplazamiento y la distancia recorrida son siempre iguales.", "Si el objeto vuelve atrás, la distancia suma todo el camino y el desplazamiento solo compara el inicio con el final.", "Calcula primero el camino total y luego posición final menos inicial."),
      ("Decir que un objeto está quieto o en movimiento sin nombrar respecto de qué.", "El movimiento depende del sistema de referencia.", "Escribe siempre «respecto de…» antes de afirmar que algo se mueve."),
  ],
  rec=[
      ("¿Cómo se llama el punto desde el que se mide la posición en un sistema de referencia?", "Origen", "Todas las posiciones se miden desde ese punto."),
      ("Verdadero o falso: la distancia recorrida puede ser negativa.", "Falso", "Es el largo del camino y no tiene signo."),
      ("¿En qué unidad se mide la rapidez media en este cuaderno?", "Metros por segundo (m/s)", "Es distancia en metros dividida por tiempo en segundos."),
  ],
  und=[
      ("Una persona viaja sentada en un tren en marcha. Respecto del tren, ¿está quieta o en movimiento? A) Quieta; B) En movimiento.", "A", "Su posición no cambia respecto del tren."),
      ("Una persona camina 5 m a la derecha y luego 5 m de vuelta hasta su punto de partida. ¿Cuál es su desplazamiento? A) 0 m; B) 10 m.", "A", "Termina donde empezó, así que su posición no cambió."),
      ("¿Qué dos medidas se dividen para obtener la rapidez media?", "Distancia recorrida y tiempo", "La rapidez media es distancia recorrida dividida por tiempo."),
  ],
  app=[
      arith("El origen está en la entrada de un pasillo. Un estudiante estaba en la posición 14 m y pasó a la posición 5 m. ¿Cuál es su desplazamiento? (El signo negativo indica hacia el origen).", "5-14", "Se resta la posición inicial a la final.", " m"),
      arith("Una persona de ejemplo camina 9 m hacia la derecha y luego 4 m de vuelta. ¿Cuántos metros recorrió en total?", "9+4", "La distancia recorrida suma todo el camino.", " m"),
      arith("Un carrito recorre 20 m en 5 s con rapidez constante. ¿Cuál es su rapidez media?", "20//5", "Distancia dividida por tiempo.", " m/s"),
  ],
  rea=[
      ("Una compañera dice: «Fui y volví al mismo punto, así que no me moví». ¿Qué le respondes? A) Te moviste y recorriste distancia, aunque tu desplazamiento fue 0; B) Tienes razón, la distancia recorrida fue 0.", "A", "La distancia suma el camino; el desplazamiento compara solo inicio y final."),
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos segundos tarda una pelota en recorrer 2 m de una rampa de cartón al soltarla desde la misma marca?; B) ¿Es más entretenido ver rodar una pelota?", "A", "Indica qué se mide y en qué condiciones; la otra depende de una opinión."),
  ],
  cha=[
      ("El origen está en la salida de un pasillo y la derecha es positiva. Ana está en la posición 6 m y Bruno en −2 m. ¿Cuántos metros los separan?", "8 m", "Se resta 6 − (−2) = 8, que es la distancia entre ambas posiciones."),
      arith("Una persona parte del origen, camina 7 m a la derecha, luego 3 m a la izquierda y después 2 m más a la izquierda. ¿En qué posición termina?", "7-3-2", "Se suman los tramos con signo.", " m"),
  ],
  context=[arith("Un recorrido de ejemplo por el patio mide 50 m y se hace con rapidez constante en 25 s. ¿Cuál es la rapidez media?", "50//25", "Distancia dividida por tiempo.", " m/s")],
  selfcheck=[("¿Qué diferencia hay entre distancia recorrida y desplazamiento?", "La distancia suma todo el camino y el desplazamiento compara posición final con inicial", "El desplazamiento puede ser cero aunque se haya caminado."), ("¿Para qué sirve un sistema de referencia?", "Para describir la posición y el movimiento de un objeto", "Sin origen y dirección no se puede medir la posición."), ("¿Qué hace investigable a una pregunta de movimiento?", "Que indica qué se mide y en qué condiciones", "Así se contesta con datos.")],
  open_task=task("Datos de ejemplo: en un pasillo, con el origen en la puerta, un estudiante camina desde la posición 2 m hasta la posición 10 m y tarda 8 s. Calcula su desplazamiento y su rapidez media. Después escribe una pregunta investigable sobre su caminata que indique qué se mide y qué se compara.", "Desplazamiento: 10 − 2 = 8 m a la derecha. Rapidez media: 8 m ÷ 8 s = 1 m/s. Pregunta: «¿Cuántos segundos tarda el mismo estudiante en recorrer esos 8 m al caminar normal y al caminar más lento?».", ["calcula bien desplazamiento y rapidez con unidades", "la pregunta indica qué se mide", "la pregunta compara dos condiciones"], ["dos cálculos y una pregunta"], ["omitir las unidades", "escribir una pregunta de opinión"], "Pregunta qué instrumentos usarías para medir con más precisión."),
  reinforce="Escribe un ejemplo de tu casa en que la distancia recorrida sea mayor que el desplazamiento.",
  extend="Explica por qué dos personas pueden describir el mismo objeto como quieto y en movimiento sin contradecirse.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Las tablas de datos de ejemplo están escritas en los ejercicios. Para graficar, una hoja cuadriculada.",
  use="Aprenderé a leer tablas y gráficos de posición contra tiempo, a reconocer un movimiento rectilíneo uniforme y a calcular la velocidad con dos puntos.",
  prior=["Sé qué es posición, desplazamiento y rapidez media.", "Sé ubicar puntos en un plano con dos ejes."],
  explain=[
      "Un movimiento rectilíneo uniforme (MRU) ocurre en línea recta con velocidad constante: en tiempos iguales recorre desplazamientos iguales. La velocidad es el desplazamiento dividido por el tiempo y se mide en m/s. A diferencia de la rapidez, la velocidad tiene dirección: en una recta se indica con el signo, positivo hacia la derecha y negativo hacia la izquierda.",
      "Los datos de un movimiento se ordenan en una tabla de posición y tiempo. Si la posición cambia lo mismo en cada segundo, el movimiento es uniforme. Al graficar la posición en el eje vertical y el tiempo en el eje horizontal, los puntos quedan sobre una recta. La inclinación de esa recta, llamada pendiente, es la velocidad: mientras más empinada, mayor velocidad. Una recta horizontal indica que el objeto está detenido.",
      "Al leer un gráfico, primero se miran los ejes, las unidades y la escala. Para calcular la velocidad se toman dos puntos de la recta y se divide el cambio de posición por el cambio de tiempo. Los datos medidos tienen pequeñas variaciones; un buen análisis dice si los puntos se acercan a una recta y no exige que coincidan exactamente.",
  ],
  vocab=[("MRU", "movimiento rectilíneo uniforme: línea recta y velocidad constante"), ("velocidad", "desplazamiento dividido por tiempo, con signo"), ("pendiente", "inclinación de la recta de un gráfico"), ("detenido", "objeto cuya posición no cambia con el tiempo"), ("tabla de datos", "lista ordenada de tiempos y posiciones medidas")],
  worked=[
      ("Reconocer un MRU en una tabla", "Datos de ejemplo. Tiempo (s): 0, 1, 2, 3. Posición (m): 2, 6, 10, 14. ¿Es un MRU? Calcula la velocidad.", ["Los cambios de posición cada segundo son 4, 4 y 4 m: son iguales.", "Como es constante, el movimiento es uniforme.", "Velocidad: 4 m ÷ 1 s."], "Sí es MRU, con velocidad de 4 m/s"),
      ("Velocidad desde un gráfico", "Una recta pasa por los puntos (0 s, 10 m) y (5 s, 0 m). ¿Cuál es la velocidad y hacia dónde se mueve?", ["Cambio de posición: 0 − 10 = −10 m.", "Cambio de tiempo: 5 − 0 = 5 s; velocidad = −10 ÷ 5.", "El signo negativo indica que se acerca al origen."], "−2 m/s, hacia el origen"),
  ],
  mistakes=[
      ("Calcular la velocidad dividiendo solo la posición final por el tiempo.", "Se olvida restar la posición inicial; la velocidad usa el cambio de posición.", "Resta siempre posición final menos posición inicial."),
      ("Creer que una recta horizontal en un gráfico de posición significa que el objeto va rápido.", "Una recta horizontal indica que la posición no cambia: está detenido.", "Recuerda: más empinada, más velocidad; horizontal, detenido."),
  ],
  rec=[
      ("¿Qué indica una recta horizontal en un gráfico de posición contra tiempo?", "Que el objeto está detenido", "La posición no cambia mientras pasa el tiempo."),
      ("Verdadero o falso: en un MRU el objeto recorre desplazamientos iguales en tiempos iguales.", "Verdadero", "Esa es la definición de velocidad constante."),
      ("En los gráficos de esta clase, ¿qué eje muestra el tiempo?", "El eje horizontal", "La posición va en el eje vertical."),
  ],
  und=[
      ("En una tabla, la posición cambia 5 m, 5 m y 5 m en tres segundos seguidos. ¿El movimiento es uniforme? A) Sí; B) No.", "A", "Los cambios de posición son iguales en tiempos iguales."),
      ("Dos rectas de un gráfico de posición contra tiempo parten del mismo punto. La recta P es más empinada que la recta Q. ¿Cuál objeto tiene mayor velocidad? A) P; B) Q.", "A", "Mayor pendiente significa mayor velocidad."),
      ("Con la derecha como positiva, ¿qué signo tiene la velocidad de un objeto que se mueve hacia la izquierda?", "Negativo", "El signo indica el sentido del movimiento."),
  ],
  app=[
      arith("Un carrito está en 3 m cuando t = 0 s y en 18 m cuando t = 5 s, con MRU (datos de ejemplo). ¿Cuál es su velocidad?", "(18-3)//5", "Cambio de posición dividido por cambio de tiempo.", " m/s"),
      arith("Un objeto se mueve con velocidad constante de 6 m/s. ¿Cuántos metros avanza en 7 s?", "6*7", "El desplazamiento es velocidad por tiempo.", " m"),
      ("Tabla de ejemplo: t = 0, 1, 2, 3 s; posición = 0, 2, 6, 12 m. ¿Es un MRU? A) Sí; B) No.", "B", "Los cambios de posición (2, 4 y 6 m) no son iguales."),
  ],
  rea=[
      ("Un carrito se mueve sobre una mesa plana y los puntos medidos quedan casi alineados, con desviaciones pequeñas de 1 cm. ¿Qué conclusión es prudente? A) Es aproximadamente uniforme, con pequeños errores de medición; B) No es uniforme porque los puntos no quedaron exactamente en línea.", "A", "Las mediciones reales tienen variaciones pequeñas."),
      ("Dos estudiantes usan los puntos (0 s, 6 m) y (3 s, 21 m). Uno dice 7 m/s (21 ÷ 3) y otro dice 5 m/s. ¿Quién tiene razón? A) Quien dice 5 m/s; B) Quien dice 7 m/s.", "A", "El cambio de posición es 21 − 6 = 15 m, dividido por 3 s."),
  ],
  cha=[
      arith("Un objeto está en x = 20 m cuando t = 0 s y se mueve con velocidad constante de −5 m/s (dato de ejemplo). ¿En qué posición está a los 3 s?", "20-5*3", "A la posición inicial se le suma la velocidad por el tiempo.", " m"),
      ("Gráfico de ejemplo: el objeto M pasa por (0 s, 0 m) y (4 s, 8 m); el objeto N pasa por (0 s, 10 m) y (4 s, 14 m). ¿Cuál es más veloz y por cuántos m/s? Responde con la letra y el número.", "M, por 1 m/s", "M tiene 2 m/s y N tiene 1 m/s."),
  ],
  context=[arith("En una pista recta, un estudiante trota en MRU y pasa de 5 m a 55 m en 10 s (datos de ejemplo). ¿Cuál es su velocidad?", "(55-5)//10", "Cambio de posición dividido por cambio de tiempo.", " m/s")],
  selfcheck=[("¿Cómo se reconoce un MRU en una tabla?", "Porque la posición cambia lo mismo en tiempos iguales", "Eso significa velocidad constante."), ("¿Qué representa la pendiente en un gráfico de posición contra tiempo?", "La velocidad", "Indica cuánto cambia la posición por segundo."), ("¿Qué mide una recta que baja?", "Una velocidad negativa", "La posición disminuye con el tiempo.")],
  open_task=task("Datos de ejemplo de un carrito sobre una mesa plana. Tiempo (s): 0, 2, 4, 6. Posición (cm): 5, 25, 45, 65. Grafica los puntos en una hoja cuadriculada, une con una recta, calcula la velocidad en cm/s con dos puntos y escribe una oración que diga si es un MRU y por qué.", "Cambio de posición: 65 − 5 = 60 cm en 6 s, es decir 10 cm/s. Es un MRU porque la posición aumenta 20 cm cada 2 s; los puntos quedan sobre una recta.", ["grafica con ejes rotulados", "calcula la velocidad con unidades", "justifica el MRU con los datos"], ["gráfico, cálculo y oración"], ["no rotular los ejes", "dividir sin restar la posición inicial"], "Pregunta qué cambiaría en el gráfico si el carrito fuera más rápido."),
  reinforce="Calcula la velocidad de un objeto que pasa de 4 m a 16 m en 3 s.",
  extend="Explica con tus palabras por qué la pendiente de un gráfico de posición es la velocidad.")

L(OA9, 3,
  materials="Este cuaderno y lápiz. Los gráficos de ejemplo se describen con sus puntos en los ejercicios. Hoja cuadriculada para graficar.",
  use="Aprenderé el modelo del MRU como ecuación y como gráfico de velocidad contra tiempo, y a contrastarlo con mediciones.",
  prior=["Sé calcular la velocidad con dos puntos de un gráfico de posición.", "Sé calcular el área de un rectángulo."],
  explain=[
      "El modelo del MRU se escribe con la ecuación x = x0 + v·t. Aquí x es la posición en el tiempo t, x0 es la posición inicial, v es la velocidad constante y t es el tiempo transcurrido. Si v es negativa, la posición disminuye con el tiempo. Esta ecuación permite predecir dónde estará el objeto en cualquier instante.",
      "En un MRU, el gráfico de velocidad contra tiempo es una recta horizontal, porque la velocidad no cambia. El desplazamiento durante un intervalo es el área del rectángulo bajo esa recta: base igual al tiempo y altura igual a la velocidad. Así, la misma información aparece en la ecuación, en el gráfico de posición y en el gráfico de velocidad.",
      "Un modelo es una simplificación. El MRU supone que la velocidad no cambia, algo que casi nunca ocurre exactamente: el roce y los errores de medición producen diferencias. Para contrastar el modelo se calcula una predicción, se mide y se compara. Si la diferencia es pequeña, el modelo sirve en esas condiciones; si es grande y repetida, hay que revisar el modelo o el montaje.",
  ],
  vocab=[("x0", "posición inicial del objeto"), ("ecuación del MRU", "x = x0 + v·t"), ("modelo", "simplificación que permite predecir un fenómeno"), ("predicción", "valor calculado con el modelo antes de medir"), ("gráfico velocidad-tiempo", "gráfico de la velocidad en el eje vertical")],
  worked=[
      ("Predecir una posición", "Un objeto parte de x0 = 4 m con velocidad de 3 m/s. ¿Dónde estará a los 6 s?", ["Se escribe x = 4 + 3·6.", "3·6 = 18 y 4 + 18 = 22."], "A los 22 m"),
      ("Área bajo el gráfico", "Un objeto se mueve con velocidad constante de 5 m/s durante 4 s. ¿Cuánto se desplaza según el gráfico velocidad-tiempo?", ["El gráfico es una recta horizontal en 5 m/s entre 0 y 4 s.", "El área del rectángulo es 5 × 4."], "20 m"),
  ],
  mistakes=[
      ("Olvidar sumar la posición inicial en x = x0 + v·t.", "El objeto no parte siempre del origen; sin x0 se obtiene solo el desplazamiento.", "Escribe primero x0 y luego suma v·t."),
      ("Creer que el modelo debe coincidir exactamente con toda medición.", "El modelo es una simplificación; hay errores y pérdidas de velocidad.", "Compara el modelo y la medición y comenta la diferencia."),
  ],
  rec=[
      ("En x = x0 + v·t, ¿qué representa x0?", "La posición inicial", "Es dónde estaba el objeto cuando t = 0."),
      ("¿Qué forma tiene el gráfico velocidad-tiempo de un MRU?", "Una recta horizontal", "La velocidad no cambia con el tiempo."),
      ("Verdadero o falso: el área bajo el gráfico velocidad-tiempo de un MRU es el desplazamiento.", "Verdadero", "Base por altura da tiempo por velocidad."),
  ],
  und=[
      ("¿Por qué se dice que x = x0 + v·t es un modelo? A) Porque simplifica el movimiento suponiendo velocidad constante; B) Porque describe cualquier movimiento real sin error.", "A", "Los modelos simplifican y tienen condiciones de uso."),
      ("Con x = x0 + v·t, si v es negativa, ¿qué pasa con la posición al pasar el tiempo?", "Disminuye", "El término v·t es negativo y se resta a x0."),
      ("En un gráfico velocidad-tiempo de un MRU a 4 m/s, ¿cómo es la recta? A) Horizontal a la altura de 4 m/s; B) Inclinada hacia arriba.", "A", "La velocidad es constante, por eso la recta no se inclina."),
  ],
  app=[
      arith("Un objeto parte de x0 = 10 m con velocidad de 2 m/s. ¿En qué posición estará a los 15 s?", "10+2*15", "Se aplica x = x0 + v·t.", " m"),
      arith("Un objeto viaja a velocidad constante de 9 m/s durante 4 s. ¿Cuánto se desplaza, calculado como área del gráfico velocidad-tiempo?", "9*4", "El área del rectángulo es velocidad por tiempo.", " m"),
      arith("Un objeto parte de x0 = 50 m con velocidad de −6 m/s. ¿En qué posición estará a los 5 s?", "50-6*5", "Con velocidad negativa la posición disminuye.", " m"),
  ],
  rea=[
      ("El modelo predice que a los 10 s un carrito estará en 30 m, pero se midieron 27 m. ¿Qué conclusión es adecuada? A) El modelo es una aproximación; conviene revisar la medición y las pérdidas de velocidad; B) El modelo es correcto y la medición no importa.", "A", "Se compara la predicción con la medición y se explica la diferencia."),
      ("Un compañero dice que el área bajo el gráfico velocidad-tiempo de un MRU es un triángulo. ¿Qué le respondes? A) Es un rectángulo, porque la velocidad es constante; B) Tiene razón, siempre es un triángulo.", "A", "Con velocidad constante la altura no cambia: base por altura."),
  ],
  cha=[
      arith("Un objeto con velocidad de 4 m/s parte de x0 = 6 m. ¿En cuántos segundos llega a la posición 26 m?", "(26-6)//4", "El desplazamiento necesario dividido por la velocidad da el tiempo.", " s"),
      ("Ana parte de 0 m con velocidad de 3 m/s y Beto parte de 12 m con velocidad de 1 m/s, ambos hacia la derecha por la misma recta. Escribe la posición de cada uno en función del tiempo y busca el instante en que coinciden. ¿Cuántos segundos pasan?", "6 s", "3t = 12 + t, es decir 2t = 12 y t = 6 s."),
  ],
  context=[arith("Una persona camina con velocidad constante de 2 m/s por un pasillo de ejemplo de 30 m, partiendo de un extremo. ¿Cuántos segundos tarda en llegar al otro extremo?", "30//2", "El tiempo es la distancia dividida por la velocidad.", " s")],
  selfcheck=[("¿Qué significa cada letra en x = x0 + v·t?", "x es la posición, x0 la posición inicial, v la velocidad y t el tiempo", "Cada símbolo representa una medición."), ("¿Qué se obtiene del área bajo un gráfico velocidad-tiempo?", "El desplazamiento", "Es velocidad por tiempo."), ("¿Por qué el MRU es un modelo?", "Porque supone velocidad constante, algo aproximado", "En la realidad hay roce y errores.")],
  open_task=task("Datos de ejemplo: un carrito parte de x0 = 8 cm con velocidad de 12 cm/s. Escribe la ecuación, predice su posición a los 5 s y dibuja el gráfico velocidad-tiempo de 0 a 5 s sombreando el área. Luego compara con una medición de ejemplo de 66 cm a los 5 s y escribe una causa posible de la diferencia.", "x = 8 + 12·t. A los 5 s: 8 + 60 = 68 cm. El área es 12 × 5 = 60 cm. La medición dio 66 cm, 2 cm menos que la predicción; pudo deberse al roce del carrito o a un error al medir.", ["escribe la ecuación con sus datos", "predice correctamente la posición", "compara con la medición y propone una causa"], ["ecuación, gráfico y comparación"], ["no sumar la posición inicial", "no explicar la diferencia"], "Pregunta qué medirías para saber si el roce influyó."),
  reinforce="Calcula la posición a los 4 s de un objeto que parte de 3 m con 5 m/s.",
  extend="Explica por qué el mismo MRU se puede representar con una ecuación y con dos gráficos distintos.")

L(OA9, 4,
  materials="Este cuaderno y lápiz. Para repetir la idea en casa: una pelota de goma, una tabla o cartón firme como rampa apoyada en libros y un cronómetro de celular. Los datos de los ejercicios están escritos.",
  use="Aprenderé qué es la aceleración, el modelo del movimiento rectilíneo uniformemente acelerado (MRUA) y cómo se relacionan velocidad, aceleración y tiempo.",
  prior=["Sé calcular la velocidad en un MRU.", "Sé leer un gráfico con dos ejes."],
  explain=[
      "En un movimiento rectilíneo uniformemente acelerado (MRUA) la velocidad cambia lo mismo en cada segundo. La aceleración es ese cambio de velocidad por unidad de tiempo: a = (v final − v inicial) ÷ t, y se mide en metros por segundo cada segundo (m/s²). Si la aceleración tiene el mismo sentido que el movimiento, la rapidez aumenta; si tiene sentido contrario, el objeto frena.",
      "Con aceleración constante se cumple v = v0 + a·t. Si un objeto parte del reposo (v0 = 0) con a = 2 m/s², su velocidad es 2, 4 y 6 m/s al pasar 1, 2 y 3 s. En el gráfico velocidad-tiempo los puntos quedan sobre una recta inclinada y su pendiente es la aceleración. La distancia recorrida es el área bajo esa recta, un trapecio: d = (v0 + v) ÷ 2 × t.",
      "Para investigar la relación entre variables se cambia una sola, por ejemplo la inclinación de una rampa, y se mide otra, como el tiempo que tarda una pelota de goma en bajar. Se repite cada medición y se compara el promedio. Una rampa más inclinada produce mayor aceleración, aunque con instrumentos caseros la medición tiene incertidumbre.",
  ],
  vocab=[("aceleración", "cambio de velocidad por cada segundo, en m/s²"), ("MRUA", "movimiento rectilíneo con aceleración constante"), ("reposo", "velocidad igual a cero"), ("v0", "velocidad inicial"), ("frenar", "aceleración con sentido contrario a la velocidad")],
  worked=[
      ("Calcular la aceleración", "Un carrito pasa de 6 m/s a 18 m/s en 4 s. ¿Cuál es su aceleración?", ["Cambio de velocidad: 18 − 6 = 12 m/s.", "Se divide por el tiempo: 12 ÷ 4."], "3 m/s²"),
      ("Velocidad y distancia", "Un objeto parte del reposo con a = 4 m/s² durante 5 s. ¿Qué velocidad alcanza y qué distancia recorre?", ["v = 0 + 4·5 = 20 m/s.", "Distancia: (0 + 20) ÷ 2 × 5 = 10 × 5."], "Velocidad 20 m/s y distancia 50 m"),
  ],
  mistakes=[
      ("Confundir velocidad con aceleración.", "La velocidad dice qué tan rápido se mueve; la aceleración dice cuánto cambia esa velocidad cada segundo.", "Pregunta: ¿me piden cuánto avanza o cuánto cambia la velocidad?"),
      ("Pensar que aceleración cero significa objeto detenido.", "Con aceleración cero la velocidad es constante, que puede ser distinta de cero.", "Aceleración 0 puede ser reposo o MRU."),
  ],
  rec=[
      ("¿En qué unidad se mide la aceleración?", "En m/s²", "Es metros por segundo cada segundo."),
      ("Verdadero o falso: en un MRUA la velocidad cambia lo mismo en cada segundo.", "Verdadero", "Esa es la definición de aceleración constante."),
      ("¿Qué indica la pendiente de un gráfico velocidad-tiempo?", "La aceleración", "Muestra cuánto cambia la velocidad por segundo."),
  ],
  und=[
      ("Un objeto se mueve a 10 m/s y tiene una aceleración de 2 m/s² en sentido contrario a su movimiento. ¿Qué pasa con su rapidez? A) Disminuye; B) Aumenta.", "A", "La aceleración tiene sentido contrario al movimiento, así que frena."),
      ("En una rampa de cartón, ¿qué relación esperas entre la inclinación y la aceleración de la pelota? A) A mayor inclinación, mayor aceleración; B) A mayor inclinación, menor aceleración.", "A", "Una rampa más inclinada hace que la velocidad crezca más rápido."),
      ("¿Cómo se ve en un gráfico velocidad-tiempo un objeto que parte del reposo con aceleración constante?", "Como una recta inclinada que parte del origen", "La velocidad crece lo mismo cada segundo desde cero."),
  ],
  app=[
      arith("Un carrito pasa de 4 m/s a 16 m/s en 3 s. ¿Cuál es su aceleración?", "(16-4)//3", "Cambio de velocidad dividido por el tiempo.", " m/s²"),
      arith("Un objeto parte del reposo con aceleración de 5 m/s² durante 6 s. ¿Qué velocidad alcanza?", "5*6", "Con v0 = 0, la velocidad es a por t.", " m/s"),
      arith("Un objeto tiene 7 m/s y acelera a 3 m/s² durante 4 s. ¿Qué velocidad tiene al final?", "7+3*4", "Se aplica v = v0 + a·t.", " m/s"),
  ],
  rea=[
      ("Un estudiante dice: «Si la aceleración es 0, el objeto está detenido». ¿Qué le respondes? A) Es falso: puede moverse con velocidad constante; B) Es verdadero siempre.", "A", "Aceleración cero significa que la velocidad no cambia, no que sea cero."),
      ("Dos pelotas parten del reposo y bajan la misma distancia por rampas distintas: una tarda 4 s y la otra 2 s. ¿Cuál tuvo mayor aceleración? A) La que tardó 2 s; B) La que tardó 4 s.", "A", "Para la misma distancia, llegar antes exige que la velocidad crezca más rápido."),
  ],
  cha=[
      arith("Un objeto parte del reposo con a = 2 m/s² durante 8 s. ¿Qué distancia recorre? (Usa d = (v0 + v) ÷ 2 × t).", "(2*8)*8//2", "Primero v = 16 m/s; luego el promedio de velocidades por el tiempo.", " m"),
      arith("Un ciclista de ejemplo frena de 12 m/s hasta detenerse con una aceleración de −3 m/s². ¿Cuántos segundos tarda?", "12//3", "El cambio de velocidad es 12 m/s y se divide por 3 m/s² cada segundo.", " s"),
  ],
  context=[arith("Una pelota de goma baja por una rampa partiendo del reposo; a los 3 s su velocidad es 6 m/s (dato de ejemplo). ¿Cuál es su aceleración?", "6//3", "Cambio de velocidad dividido por el tiempo.", " m/s²")],
  selfcheck=[("¿Qué mide la aceleración?", "Cuánto cambia la velocidad en cada segundo", "Se expresa en m/s²."), ("¿Qué indica el área bajo el gráfico velocidad-tiempo?", "La distancia recorrida", "Es el producto de velocidad y tiempo."), ("¿Cómo se sabe que un objeto frena?", "Porque su aceleración tiene sentido contrario a su velocidad", "La rapidez disminuye.")],
  open_task=task("Datos de ejemplo de una pelota que baja una rampa desde el reposo. Tiempo (s): 0, 1, 2, 3. Velocidad (m/s): 0, 2, 4, 6. Calcula la aceleración, escribe la ecuación v = a·t con sus valores y calcula la distancia recorrida en 3 s. Después propone cómo cambiarías una sola variable para investigar si la inclinación de la rampa afecta la aceleración.", "a = 6 ÷ 3 = 2 m/s². Ecuación: v = 2·t. Distancia: (0 + 6) ÷ 2 × 3 = 9 m. Para investigar, mediría el tiempo de bajada con tres inclinaciones, manteniendo la misma pelota y la misma distancia.", ["calcula la aceleración con unidad", "calcula la distancia con el área", "cambia solo una variable y controla las demás"], ["tres cálculos y un diseño breve"], ["cambiar inclinación y pelota a la vez", "olvidar el signo de la aceleración"], "Pregunta cuántas repeticiones harías por inclinación."),
  reinforce="Calcula la aceleración de un objeto que pasa de 0 a 12 m/s en 4 s.",
  extend="Explica por qué la distancia en un MRUA se calcula con el promedio de las velocidades inicial y final.")

L(OA9, 5,
  materials="Este cuaderno y lápiz. Para observar: una hoja de papel y la misma hoja arrugada en bola, que se sueltan desde la altura de la cintura (sin subirse a nada). Los datos están escritos en los ejercicios.",
  use="Aprenderé a explicar movimientos con evidencia: caída libre, comparación entre MRU y MRUA, y lectura de tablas y gráficos para decidir qué movimiento ocurre.",
  prior=["Sé qué es un MRU y un MRUA.", "Sé usar v = v0 + a·t."],
  explain=[
      "La caída libre es el movimiento de un objeto que cae solo por la atracción de la Tierra, sin considerar el aire. Es un MRUA con aceleración cercana a 10 m/s² hacia abajo. En este cuaderno usamos g = 10 m/s² para simplificar los cálculos. Un objeto soltado desde el reposo tiene velocidad 10, 20 y 30 m/s al cabo de 1, 2 y 3 segundos.",
      "Para explicar un movimiento con evidencia se combinan tabla, gráfico y ecuación. Si la velocidad medida crece lo mismo en cada segundo, se concluye MRUA y la aceleración es la pendiente del gráfico velocidad-tiempo. Si la velocidad no cambia, se concluye MRU. Un gráfico de posición curvo, que se empina con el tiempo, indica que la velocidad aumenta.",
      "En la vida diaria el aire frena más a los objetos livianos y de gran superficie: una hoja abierta cae más lento que la misma hoja hecha una bola. Eso no contradice el modelo, porque el modelo de caída libre ignora el aire. Toda explicación debe decir qué supone y en qué situaciones deja de servir.",
  ],
  vocab=[("caída libre", "caída solo por atracción de la Tierra, sin considerar el aire"), ("g", "aceleración de caída libre; aquí vale 10 m/s²"), ("evidencia", "dato medido que apoya una explicación"), ("supuesto", "condición que el modelo da por cierta"), ("roce con el aire", "fuerza que el aire hace contra el movimiento")],
  worked=[
      ("Decidir el tipo de movimiento", "Datos de ejemplo. Tiempo (s): 0, 2, 4. Velocidad (m/s): 3, 9, 15. ¿Qué movimiento es y cuál es la aceleración?", ["La velocidad aumenta 6 m/s cada 2 s: el cambio es constante.", "Aceleración: 6 ÷ 2 = 3 m/s²."], "MRUA con aceleración de 3 m/s²"),
      ("Caída libre", "Se suelta un objeto desde el reposo y cae 4 s en caída libre (g = 10 m/s²). ¿Qué velocidad alcanza y cuántos metros cae?", ["v = 10·4 = 40 m/s.", "Distancia: (0 + 40) ÷ 2 × 4 = 20 × 4."], "Velocidad 40 m/s y caída de 80 m"),
  ],
  mistakes=[
      ("Decir que los objetos pesados siempre caen con mayor aceleración.", "Sin roce con el aire, todos caen con la misma aceleración; las diferencias diarias vienen del aire.", "Separa lo que dice el modelo de lo que agrega el aire."),
      ("Concluir MRUA mirando solo un par de datos.", "Hay que comprobar que el cambio de velocidad sea el mismo en todos los intervalos.", "Calcula el cambio en cada intervalo antes de concluir."),
  ],
  rec=[
      ("¿Qué valor de g se usa en este cuaderno?", "10 m/s²", "Es un valor aproximado para simplificar."),
      ("Verdadero o falso: el modelo de caída libre ignora el roce con el aire.", "Verdadero", "Es uno de sus supuestos."),
      ("En una tabla, si la velocidad no cambia con el tiempo, ¿qué movimiento es?", "MRU", "Velocidad constante significa aceleración cero."),
  ],
  und=[
      ("Una hoja abierta cae más lento que la misma hoja hecha una bola. ¿Qué lo explica? A) El aire frena más a la hoja abierta; B) La Tierra atrae menos a la hoja abierta.", "A", "La hoja abierta tiene más superficie expuesta al aire."),
      ("Un gráfico de posición contra tiempo se empina cada vez más. ¿Qué pasa con la velocidad? A) Aumenta; B) Disminuye.", "A", "Una recta más empinada significa mayor velocidad."),
      ("En caída libre, ¿qué velocidad tiene un objeto soltado desde el reposo al cabo de 1 s?", "10 m/s", "v = g·t = 10 × 1."),
  ],
  app=[
      arith("Se suelta un objeto desde el reposo en caída libre. ¿Qué velocidad tiene a los 5 s?", "10*5", "La velocidad es g por t.", " m/s"),
      arith("Un objeto cae libremente 2 s desde el reposo. ¿Cuántos metros cae? (Primero v = 20 m/s; luego d = (v0 + v) ÷ 2 × t).", "(10*2)*2//2", "Se usa el promedio de las velocidades por el tiempo.", " m"),
      arith("Tabla de ejemplo: la velocidad es 2 m/s a los 0 s y 14 m/s a los 2 s, con cambio constante. ¿Cuál es la aceleración?", "(14-2)//2", "Cambio de velocidad dividido por el tiempo.", " m/s²"),
  ],
  rea=[
      ("Un compañero dice: «Los objetos pesados siempre caen con mayor aceleración». ¿Qué respondes según el modelo? A) Sin aire, todos caen con la misma aceleración; B) Tiene razón, porque la Tierra los atrae más.", "A", "El modelo de caída libre da el mismo g a todos los objetos."),
      ("Datos de ejemplo: velocidad 0, 5, 10 y 15 m/s en t = 0, 1, 2 y 3 s. ¿Qué conclusión es correcta? A) MRUA con aceleración de 5 m/s²; B) MRU con velocidad de 5 m/s.", "A", "La velocidad cambia 5 m/s cada segundo."),
  ],
  cha=[
      arith("Se suelta un objeto que llega al suelo a los 3 s de caída libre. ¿Desde qué altura cayó?", "(10*3)*3//2", "v = 30 m/s y la distancia es el promedio de velocidades por 3 s.", " m"),
      arith("Un objeto es lanzado hacia abajo con 15 m/s. En caída libre, ¿qué velocidad tiene a los 2 s?", "15+10*2", "Se aplica v = v0 + g·t.", " m/s"),
  ],
  context=[arith("En un video de ejemplo, un objeto soltado desde el reposo cae durante 2 s hasta el suelo. ¿Con qué velocidad llega?", "10*2", "La velocidad en caída libre es g por t.", " m/s")],
  selfcheck=[("¿Qué es la caída libre?", "Una caída solo por la atracción de la Tierra, sin considerar el aire", "Es un MRUA con g."), ("¿Por qué una hoja abierta cae más lento que una bola de papel?", "Porque el aire la frena más", "El modelo ignora ese efecto."), ("¿Cómo se decide si un movimiento es MRUA con una tabla?", "Se comprueba que la velocidad cambie lo mismo en cada intervalo", "El cambio constante es aceleración constante.")],
  open_task=task("Con una hoja de papel y la misma hoja arrugada en bola, sueltas ambas desde la altura de tu cintura, sin subirte a nada, y observas cuál llega antes al suelo. Escribe lo que observas, qué dice el modelo de caída libre y una explicación de la diferencia. Declara un límite de tu observación.", "Observación: la bola llega antes que la hoja abierta. El modelo sin aire predice igual aceleración para ambas. La diferencia se explica por el roce con el aire, que frena más a la hoja abierta. Límite: la altura es pequeña y el tiempo es difícil de medir a simple vista.", ["describe lo observado", "contrasta con el modelo", "explica con el aire y declara un límite"], ["tres oraciones y un límite"], ["decir que la hoja pesa menos y por eso cae lento sin hablar del aire", "no declarar ningún límite"], "Pregunta qué instrumento mejoraría la medición del tiempo."),
  reinforce="Calcula la velocidad de un objeto en caída libre a los 4 s si parte del reposo.",
  extend="Explica por qué la velocidad de caída crece con el tiempo pero la aceleración no cambia.")

# ---------------------------------------------------------------- OA 10

L(OA10, 1,
  materials="Este cuaderno y lápiz. Para observar: un libro pequeño que se desliza sobre el piso. Los datos están escritos en los ejercicios.",
  use="Aprenderé qué es una fuerza, cómo se obtiene la fuerza neta, qué dice la primera ley de Newton y cómo plantear una pregunta investigable sobre fuerzas.",
  prior=["Sé sumar y restar números enteros.", "Sé qué es velocidad y aceleración."],
  explain=[
      "Una fuerza es una interacción que puede cambiar el movimiento o la forma de un objeto. Se mide en newtons (N) y tiene valor, dirección y sentido. Sobre un objeto suelen actuar varias fuerzas a la vez. La fuerza neta es la suma de todas ellas: si van en el mismo sentido se suman, y si van en sentidos contrarios se restan. El roce es una fuerza que se opone al deslizamiento entre dos superficies.",
      "La primera ley de Newton, o ley de inercia, dice que un objeto en reposo sigue en reposo, y uno en movimiento sigue con velocidad constante en línea recta, mientras la fuerza neta sobre él sea cero. La inercia es la tendencia de un objeto a mantener su estado de movimiento. Por eso un pasajero se inclina hacia adelante cuando el bus frena: su cuerpo tiende a seguir con la velocidad que llevaba.",
      "Una pregunta investigable sobre fuerzas dice qué se cambia y qué se mide. Por ejemplo: «¿Cuántos centímetros se desliza un libro después del mismo empujón si el piso es de cerámica o está cubierto por una toalla?». La pregunta «¿qué piso es más bonito?» no se puede investigar, porque no indica ninguna medición.",
  ],
  vocab=[("fuerza", "interacción que puede cambiar el movimiento o la forma de un objeto"), ("newton (N)", "unidad de fuerza"), ("fuerza neta", "suma de todas las fuerzas sobre un objeto"), ("inercia", "tendencia a mantener el estado de movimiento"), ("roce", "fuerza que se opone al deslizamiento")],
  worked=[
      ("Calcular la fuerza neta", "Sobre un cajón actúan 30 N hacia la derecha y 10 N hacia la izquierda. ¿Cuál es la fuerza neta?", ["Las fuerzas tienen sentidos contrarios, así que se restan: 30 − 10.", "La mayor va a la derecha."], "20 N hacia la derecha"),
      ("Aplicar la primera ley", "Un libro se desliza en línea recta con velocidad constante de 2 m/s. ¿Qué se puede decir de la fuerza neta sobre él?", ["La velocidad no cambia ni en valor ni en dirección.", "Según la primera ley, eso ocurre solo si la fuerza neta es cero."], "La fuerza neta es 0 N"),
  ],
  mistakes=[
      ("Creer que un objeto en movimiento siempre tiene una fuerza neta sobre él.", "Puede moverse con velocidad constante si la fuerza neta es cero.", "La fuerza neta se relaciona con el cambio de velocidad, no con la velocidad."),
      ("Sumar fuerzas de sentidos contrarios.", "Las fuerzas contrarias se restan.", "Elige un sentido positivo y asigna signo a cada fuerza."),
  ],
  rec=[
      ("¿En qué unidad se mide la fuerza?", "Newton (N)", "Es la unidad de fuerza del Sistema Internacional."),
      ("Verdadero o falso: una fuerza neta de 0 N es compatible con un objeto que se mueve con velocidad constante.", "Verdadero", "Es lo que dice la primera ley."),
      ("¿Cómo se llama la tendencia de un objeto a mantener su estado de movimiento?", "Inercia", "Es el concepto de la primera ley."),
  ],
  und=[
      ("Sobre un cajón en reposo actúan 15 N a la derecha y 15 N a la izquierda. ¿Cuál es la fuerza neta? A) 0 N; B) 30 N.", "A", "Fuerzas iguales y contrarias se anulan."),
      ("Un bus frena y un pasajero se inclina hacia adelante. ¿Qué lo explica? A) La inercia: su cuerpo tiende a seguir con la velocidad que llevaba; B) El bus lo empuja hacia adelante.", "A", "Sin fuerza que lo frene, el cuerpo tiende a mantener su velocidad."),
      arith("Dos fuerzas de 8 N y 5 N actúan sobre un objeto en el mismo sentido. ¿Cuál es la fuerza neta?", "8+5", "Fuerzas en el mismo sentido se suman.", " N"),
  ],
  app=[
      arith("Sobre un objeto actúan 12 N y 7 N hacia la derecha y 9 N hacia la izquierda. ¿Cuál es la fuerza neta, con la derecha como positiva?", "12+7-9", "Se suman las de la derecha y se resta la de la izquierda.", " N"),
      arith("Sobre una caja actúan 25 N hacia la izquierda y 40 N hacia la derecha. ¿Cuál es el valor de la fuerza neta?", "40-25", "Se resta la menor a la mayor.", " N"),
      ("Un objeto recibe una fuerza neta de 0 N y está en reposo. ¿Qué ocurre con su movimiento? A) Sigue en reposo; B) Empieza a moverse lentamente.", "A", "Sin fuerza neta no cambia su estado de movimiento."),
  ],
  rea=[
      ("Un compañero dice: «Si un objeto se mueve, necesariamente hay una fuerza neta sobre él». ¿Qué respondes? A) Es falso: puede moverse con velocidad constante y fuerza neta cero; B) Es verdadero, porque sin fuerza no hay movimiento.", "A", "La primera ley permite el movimiento con fuerza neta cero."),
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos centímetros se desliza un libro tras el mismo empujón sobre cerámica y sobre una toalla?; B) ¿Qué piso es más agradable de pisar?", "A", "La que mide centímetros con dos pisos indica qué se cambia y qué se mide."),
  ],
  cha=[
      ("Un cajón recibe 50 N hacia la derecha y el roce con el piso es de 20 N hacia la izquierda. ¿Cuál es la fuerza neta y hacia dónde apunta?", "30 N hacia la derecha", "Se restan: 50 − 20 y la mayor va a la derecha."),
      ("Un cajón se mueve con velocidad constante empujado con 35 N hacia la derecha. ¿Cuánto vale el roce y en qué sentido?", "35 N hacia la izquierda", "Velocidad constante implica fuerza neta cero, así que el roce iguala la fuerza de empuje."),
  ],
  context=[arith("Tres personas empujan un carro en la misma dirección y sentido con 20 N, 15 N y 10 N (datos de ejemplo). ¿Cuál es la fuerza neta, sin considerar el roce?", "20+15+10", "Fuerzas en el mismo sentido se suman.", " N")],
  selfcheck=[("¿Qué es la fuerza neta?", "La suma de todas las fuerzas que actúan sobre un objeto", "Se suman las del mismo sentido y se restan las contrarias."), ("¿Qué dice la primera ley de Newton?", "Con fuerza neta cero, el objeto mantiene su reposo o su velocidad constante", "Es la ley de inercia."), ("¿Qué hace investigable a una pregunta sobre fuerzas?", "Que indica qué se cambia y qué se mide", "Así se puede contestar con datos.")],
  open_task=task("Desliza un libro pequeño sobre el piso con un empujón suave, sin golpear a nadie ni a muebles. Si no puedes, usa estos datos de ejemplo: con el piso liso se deslizó 80 cm y con una toalla 20 cm. Escribe qué fuerza se opone al movimiento, explica con la primera ley por qué el libro termina deteniéndose y escribe una pregunta investigable sobre el mismo libro.", "El roce frena al libro. Sin roce la fuerza neta sería cero y el libro seguiría con velocidad constante; con roce hay fuerza neta contraria al movimiento y se detiene. Pregunta: «¿Cuántos centímetros se desliza el libro con el mismo empujón sobre piso liso y sobre una toalla?».", ["nombra el roce", "usa la primera ley", "la pregunta indica qué se mide"], ["tres ideas escritas"], ["decir que el libro se detiene por falta de fuerza", "preguntas de opinión"], "Pregunta cómo harías que el empujón fuera siempre igual."),
  reinforce="Calcula la fuerza neta de 18 N a la derecha y 11 N a la izquierda.",
  extend="Explica por qué en el espacio, lejos de todo roce, un objeto lanzado sigue moviéndose sin ser empujado.")

L(OA10, 2,
  materials="Este cuaderno y lápiz. Las tablas de datos de ejemplo están escritas en los ejercicios. Calculadora opcional.",
  use="Aprenderé la segunda ley de Newton, F = m·a, y a leer tablas de fuerza, masa y aceleración para comprobar si cumplen la ley.",
  prior=["Sé calcular la fuerza neta.", "Sé qué es aceleración."],
  explain=[
      "La segunda ley de Newton relaciona la fuerza neta, la masa y la aceleración: F = m·a. La masa, en kilogramos (kg), mide cuánta materia tiene un objeto y también su inercia. Si la fuerza neta es F newtons y la masa es m kilogramos, la aceleración es a = F ÷ m en m/s². Un newton es la fuerza neta que da a un objeto de 1 kg una aceleración de 1 m/s².",
      "Con la misma masa, al duplicar la fuerza neta se duplica la aceleración. Con la misma fuerza neta, al duplicar la masa la aceleración se reduce a la mitad. Una tabla de datos permite comprobarlo: en cada fila se calcula F ÷ m y se compara con la aceleración medida. Si la aceleración y la fuerza tienen el mismo sentido, el objeto aumenta su rapidez.",
      "En datos reales las aceleraciones medidas se alejan un poco de las calculadas. Si la diferencia es pequeña, la ley sigue siendo un buen modelo; si la diferencia es grande y repetida, hay que revisar el montaje, por ejemplo el roce. Al examinar una tabla, también hay que revisar que todas las magnitudes estén en las unidades correctas: newtons, kilogramos y m/s².",
  ],
  vocab=[("masa", "cantidad de materia de un objeto, en kg"), ("segunda ley", "F = m·a"), ("newton", "1 N = 1 kg·m/s²"), ("aceleración", "cambio de velocidad por segundo"), ("proporcional", "que al duplicar una magnitud se duplica la otra")],
  worked=[
      ("Calcular la aceleración", "Una fuerza neta de 12 N actúa sobre un objeto de 3 kg. ¿Cuál es su aceleración?", ["Se despeja a = F ÷ m.", "a = 12 ÷ 3."], "4 m/s²"),
      ("Leer una tabla", "Datos de ejemplo con masa de 2 kg. Fuerza neta (N): 4, 8, 12. Aceleración (m/s²): 2, 4, 6. ¿Cumple F = m·a?", ["Se calcula F ÷ m en cada fila: 4 ÷ 2 = 2, 8 ÷ 2 = 4 y 12 ÷ 2 = 6.", "Coincide con las aceleraciones y al duplicar F se duplica a."], "Sí, la aceleración es proporcional a la fuerza neta"),
  ],
  mistakes=[
      ("Dividir la masa por la fuerza para obtener la aceleración.", "La aceleración es la fuerza neta dividida por la masa.", "Usa a = F ÷ m y comprueba las unidades."),
      ("Usar una fuerza que no es la neta.", "La ley usa la suma de todas las fuerzas, incluido el roce.", "Calcula la fuerza neta antes de aplicar la ley."),
  ],
  rec=[
      ("¿Cuál es la fórmula de la segunda ley de Newton?", "F = m·a", "Relaciona fuerza neta, masa y aceleración."),
      ("¿En qué unidad se mide la masa en este cuaderno?", "Kilogramos (kg)", "Es la unidad del Sistema Internacional."),
      ("Verdadero o falso: con la misma fuerza neta, a mayor masa, menor aceleración.", "Verdadero", "a = F ÷ m disminuye al aumentar m."),
  ],
  und=[
      ("Si se duplica la fuerza neta sobre el mismo objeto, ¿qué ocurre con la aceleración? A) Se duplica; B) Se reduce a la mitad.", "A", "La aceleración es proporcional a la fuerza neta."),
      ("Se aplica la misma fuerza neta a dos carritos. El carrito M tiene el doble de masa que el N. ¿Cuál acelera más? A) El N; B) El M.", "A", "Con igual fuerza, el de menor masa acelera más."),
      ("¿Cuántos newtons de fuerza neta se necesitan para dar 1 m/s² a un objeto de 1 kg?", "1 N", "Es la definición del newton."),
  ],
  app=[
      arith("Un objeto de 5 kg tiene una aceleración de 3 m/s². ¿Cuál es la fuerza neta sobre él?", "5*3", "Se aplica F = m·a.", " N"),
      arith("Una fuerza neta de 35 N actúa sobre un objeto de 7 kg. ¿Cuál es su aceleración?", "35//7", "Se aplica a = F ÷ m.", " m/s²"),
      arith("Una fuerza neta de 36 N produce una aceleración de 9 m/s². ¿Cuál es la masa del objeto?", "36//9", "Se despeja m = F ÷ a.", " kg"),
  ],
  rea=[
      ("Tabla de ejemplo con masa de 4 kg: fuerza 8 N y aceleración 2 m/s²; fuerza 16 N y aceleración 4 m/s²; fuerza 20 N y aceleración 6 m/s². ¿Qué fila no calza con a = F ÷ m? A) La de 20 N y 6 m/s²; B) La de 16 N y 4 m/s².", "A", "20 ÷ 4 = 5, no 6."),
      ("Un estudiante dice: «Si se duplica la masa, la aceleración también se duplica». ¿Cuál es el error? A) Con la misma fuerza neta, al duplicar la masa la aceleración se reduce a la mitad; B) No hay error, es correcto.", "A", "a = F ÷ m: más masa, menos aceleración."),
  ],
  cha=[
      arith("Un carro de 8 kg acelera a 3 m/s² mientras el roce lo frena con 4 N. ¿Con qué fuerza lo empujan? (La fuerza neta es el empuje menos el roce).", "8*3+4", "La neta es 24 N; el empuje debe sumar además los 4 N del roce.", " N"),
      arith("Un objeto de 10 kg parte del reposo con una fuerza neta de 50 N. ¿Qué velocidad tiene a los 3 s? (Primero a = F ÷ m y luego v = a·t).", "50//10*3", "a = 5 m/s² y v = 5 × 3.", " m/s"),
  ],
  context=[arith("Un carro de 20 kg se empuja con una fuerza neta de 40 N sobre un piso plano (dato de ejemplo). ¿Cuál es su aceleración?", "40//20", "Fuerza neta dividida por masa.", " m/s²")],
  selfcheck=[("¿Qué relaciona la segunda ley de Newton?", "La fuerza neta, la masa y la aceleración", "F = m·a."), ("¿Qué pasa con la aceleración si la masa aumenta y la fuerza neta no cambia?", "Disminuye", "Son inversamente relacionadas."), ("¿Cómo se comprueba una tabla con la ley?", "Se calcula F ÷ m en cada fila y se compara con a", "Si coinciden, cumple la ley.")],
  open_task=task("Datos de ejemplo. Un carrito de 2 kg: con fuerza neta de 6 N aceleró 3 m/s²; con 10 N, 5 m/s²; con 14 N, 6 m/s². Calcula F ÷ m en cada fila, indica qué fila se aleja de la ley y escribe una causa posible. Escribe también qué ocurriría con la aceleración si la masa fuera de 4 kg y la fuerza neta de 10 N.", "Filas: 6 ÷ 2 = 3 (coincide), 10 ÷ 2 = 5 (coincide), 14 ÷ 2 = 7 (se midió 6, se aleja). Causa posible: error de medición o roce no considerado. Con 4 kg y 10 N: 10 ÷ 4 = 2,5 m/s², menor que 5 m/s² porque aumentó la masa.", ["calcula las tres filas", "identifica la fila discrepante", "propone una causa y razona sobre la masa"], ["tres cálculos y dos explicaciones"], ["dividir al revés", "no proponer causa"], "Pregunta cuántas veces repetirías esa medición."),
  reinforce="Calcula la aceleración de un objeto de 6 kg con fuerza neta de 18 N.",
  extend="Explica por qué un camión cargado necesita más fuerza que uno vacío para acelerar igual.")

L(OA10, 3,
  materials="Este cuaderno y lápiz. Para practicar el dibujo: un cuadrado de papel que representa el objeto y flechas dibujadas con regla.",
  use="Aprenderé a dibujar el diagrama de cuerpo libre de un objeto, a identificar peso, normal, roce y fuerza aplicada y a usarlo para calcular la fuerza neta.",
  prior=["Sé calcular la fuerza neta y la aceleración con F = m·a.", "Sé dibujar flechas para representar magnitudes."],
  explain=[
      "Un diagrama de cuerpo libre (DCL) es un dibujo simple de un solo objeto, representado por un punto o un cuadrado, con flechas que muestran todas las fuerzas que otros cuerpos hacen sobre él. La flecha indica el sentido y su largo es proporcional al valor de la fuerza. No se dibujan las fuerzas que el objeto hace sobre otros ni el resto del entorno.",
      "Las fuerzas más comunes son el peso, que apunta hacia abajo y vale m × g con g = 10 m/s²; la normal, que la superficie ejerce hacia arriba, perpendicular a ella; el roce, que se opone al deslizamiento; la tensión, que es el tirón de una cuerda; y la fuerza aplicada, como un empujón. Un objeto en reposo sobre una mesa horizontal tiene peso y normal iguales y contrarias, y la fuerza neta vertical es cero.",
      "Para usar el DCL se dibuja el objeto, se pone una flecha por cada fuerza, se elige un sentido positivo y se suman las fuerzas de cada dirección. Con la fuerza neta y la masa se calcula la aceleración con a = F ÷ m. Un DCL incompleto, que olvida la normal o el roce, lleva a una aceleración equivocada.",
  ],
  vocab=[("diagrama de cuerpo libre", "dibujo de un objeto con las fuerzas que actúan sobre él"), ("peso", "fuerza hacia abajo; m × g"), ("normal", "fuerza de una superficie sobre un objeto apoyado"), ("tensión", "fuerza que ejerce una cuerda al tirar"), ("fuerza aplicada", "empujón o tirón sobre el objeto")],
  worked=[
      ("DCL de un libro en reposo", "Un libro de 2 kg descansa sobre una mesa horizontal. Dibuja mentalmente su DCL y da el valor de peso y normal (g = 10 m/s²).", ["Peso: 2 × 10 = 20 N hacia abajo.", "Como está en reposo, la normal iguala al peso: 20 N hacia arriba."], "Peso 20 N hacia abajo y normal 20 N hacia arriba; fuerza neta vertical 0 N"),
      ("Usar el DCL para la aceleración", "Un cajón de 10 kg es empujado con 30 N hacia la derecha y el roce es de 10 N hacia la izquierda. ¿Cuál es su aceleración?", ["Fuerza neta horizontal: 30 − 10 = 20 N a la derecha.", "Aceleración: 20 ÷ 10."], "2 m/s² hacia la derecha"),
  ],
  mistakes=[
      ("Dibujar en el DCL la fuerza que el objeto ejerce sobre la mesa.", "El DCL solo incluye fuerzas que actúan sobre el objeto estudiado.", "Pregunta de cada flecha: ¿quién la hace y sobre quién actúa?"),
      ("Olvidar la normal en un objeto apoyado.", "Sin normal, la fuerza neta vertical no sería cero y el objeto se hundiría.", "Revisa que haya una fuerza hacia arriba que equilibre el peso."),
  ],
  rec=[
      ("¿Hacia dónde apunta el peso?", "Hacia abajo", "La Tierra atrae a los objetos hacia su centro."),
      ("¿Qué fuerza ejerce una superficie sobre un objeto apoyado en ella?", "La normal", "Es perpendicular a la superficie."),
      ("Verdadero o falso: en un DCL se dibujan solo las fuerzas que actúan sobre el objeto estudiado.", "Verdadero", "Las otras fuerzas pertenecen a otros diagramas."),
  ],
  und=[
      arith("¿Cuánto vale el peso de un objeto de 3 kg? (g = 10 m/s²).", "3*10", "El peso es masa por g.", " N"),
      ("Un libro está en reposo sobre una mesa. ¿Qué DCL es correcto? A) Peso hacia abajo y normal hacia arriba, de igual valor; B) Solo el peso hacia abajo.", "A", "La mesa empuja al libro hacia arriba."),
      ("Respecto del movimiento del objeto, ¿cómo apunta el roce?", "En sentido contrario", "El roce se opone al deslizamiento."),
  ],
  app=[
      arith("¿Cuánto vale el peso de un objeto de 12 kg? (g = 10 m/s²).", "12*10", "Masa por g.", " N"),
      arith("Un cajón de 6 kg es tirado con 30 N hacia la derecha y el roce es de 12 N. ¿Cuál es la fuerza neta horizontal?", "30-12", "Se resta el roce de la fuerza aplicada.", " N"),
      arith("Con los datos del cajón de 6 kg, 30 N de fuerza aplicada y 12 N de roce, ¿cuál es su aceleración?", "(30-12)//6", "Fuerza neta dividida por la masa.", " m/s²"),
  ],
  rea=[
      ("Un estudiante dibuja un objeto en reposo sobre una mesa con la normal más larga que el peso. ¿Qué error tiene? A) En reposo vertical, la normal debe igualar al peso; B) Ninguno, la mesa siempre empuja más.", "A", "Si no hay aceleración vertical, la fuerza neta vertical es cero."),
      ("Un compañero incluye en el DCL de un libro la fuerza que el libro ejerce sobre la mesa. ¿Por qué no debe ir? A) Porque actúa sobre la mesa, no sobre el libro; B) Porque es muy pequeña.", "A", "El DCL solo muestra fuerzas sobre el objeto estudiado."),
  ],
  cha=[
      arith("Una caja de 5 kg es empujada con 40 N hacia la derecha y el roce es de 15 N. ¿Cuál es su aceleración?", "(40-15)//5", "Fuerza neta 25 N dividida por 5 kg.", " m/s²"),
      ("Un objeto de 4 kg cuelga quieto de una cuerda. ¿Cuánto vale la tensión de la cuerda y hacia dónde apunta? (g = 10 m/s²).", "40 N hacia arriba", "Está en reposo: la tensión iguala al peso de 4 × 10 = 40 N."),
  ],
  context=[arith("Una persona empuja una caja de 15 kg con 60 N y el roce con el piso es de 30 N (datos de ejemplo). ¿Cuál es la aceleración de la caja?", "(60-30)//15", "Fuerza neta 30 N dividida por 15 kg.", " m/s²")],
  selfcheck=[("¿Qué es un diagrama de cuerpo libre?", "Un dibujo de un objeto con las fuerzas que actúan sobre él", "Sirve para calcular la fuerza neta."), ("Nombra tres fuerzas que pueden aparecer en un DCL.", "Peso, normal y roce", "También puede haber tensión o fuerza aplicada."), ("¿Qué se hace con las flechas para obtener la fuerza neta?", "Se suman las del mismo sentido y se restan las contrarias", "Con signo según el sentido elegido.")],
  open_task=task("Datos de ejemplo: una caja de 8 kg es empujada sobre el piso con 36 N hacia la derecha y el roce es de 12 N. Dibuja su diagrama de cuerpo libre con las cuatro fuerzas (peso, normal, roce y fuerza aplicada), escribe el valor de cada una con g = 10 m/s², calcula la fuerza neta horizontal y la aceleración.", "Peso 80 N hacia abajo; normal 80 N hacia arriba; roce 12 N hacia la izquierda; fuerza aplicada 36 N hacia la derecha. Neta horizontal: 24 N. Aceleración: 24 ÷ 8 = 3 m/s² hacia la derecha.", ["dibuja las cuatro fuerzas con el sentido correcto", "calcula peso y normal", "calcula neta y aceleración"], ["dibujo y tres cálculos"], ["omitir la normal", "restar mal el roce"], "Pregunta qué cambiaría si el roce fuera 36 N."),
  reinforce="Dibuja el DCL de un libro sobre una mesa y rotula las fuerzas.",
  extend="Explica por qué en un DCL no se dibujan las fuerzas que el objeto ejerce sobre otros.")

L(OA10, 4,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios. Para observar: dos libros pequeños que se empujan mutuamente sobre una mesa, con cuidado.",
  use="Aprenderé la tercera ley de Newton, la acción y la reacción, y combinaré las tres leyes para analizar relaciones entre variables en situaciones de ejemplo.",
  prior=["Sé la primera y la segunda ley de Newton.", "Sé hacer un diagrama de cuerpo libre."],
  explain=[
      "La tercera ley de Newton dice que, cuando un objeto A ejerce una fuerza sobre un objeto B, B ejerce sobre A una fuerza de igual valor y sentido contrario. Se llaman pareja de acción y reacción. Actúan sobre cuerpos distintos, por eso no se anulan entre sí en el diagrama de cuerpo libre de un solo objeto.",
      "Al empujar una pared con 40 N, la pared te empuja a ti con 40 N: esa reacción actúa sobre tu cuerpo. Dos carritos de juguete que se empujan reciben fuerzas iguales, pero si sus masas son distintas sus aceleraciones también lo son, porque a = F ÷ m. El carrito más liviano acelera más.",
      "Para investigar las relaciones entre variables se cambia una sola: la fuerza, la masa o el roce, y se mide la aceleración o el tiempo. Un análisis completo dice qué se controló, calcula la fuerza neta con el DCL y compara la aceleración medida con la calculada, señalando posibles fuentes de error como el roce o la medición del tiempo.",
  ],
  vocab=[("acción y reacción", "pareja de fuerzas iguales y contrarias sobre cuerpos distintos"), ("tercera ley", "a toda fuerza de A sobre B corresponde una igual y contraria de B sobre A"), ("variable controlada", "la que se mantiene igual"), ("relación inversa", "al aumentar una magnitud, disminuye la otra"), ("fuente de error", "causa posible de una diferencia entre cálculo y medición")],
  worked=[
      ("Acción y reacción", "Un carrito A de 2 kg empuja a un carrito B de 3 kg con 6 N. ¿Qué fuerza recibe A y qué aceleración tiene cada carrito, sin roce?", ["La reacción sobre A vale 6 N y apunta al lado contrario.", "Aceleración de B: 6 ÷ 3 = 2 m/s²; de A: 6 ÷ 2 = 3 m/s²."], "A recibe 6 N contraria; aA = 3 m/s² y aB = 2 m/s², en sentidos contrarios"),
      ("Leer una relación", "Datos de ejemplo con fuerza neta fija de 12 N. Masa (kg): 2, 3, 4. Aceleración (m/s²): 6, 4, 3. ¿Qué relación hay entre masa y aceleración?", ["Al aumentar la masa, la aceleración disminuye.", "El producto masa por aceleración es 12 en todas las filas."], "Relación inversa: m × a = 12 N"),
  ],
  mistakes=[
      ("Pensar que acción y reacción se anulan y por eso nada se mueve.", "Actúan sobre cuerpos distintos; cada cuerpo puede tener fuerza neta.", "Revisa sobre qué cuerpo actúa cada fuerza."),
      ("Concluir con un solo experimento.", "Un dato no muestra la relación entre variables.", "Repite con varios valores de la variable que cambias."),
  ],
  rec=[
      ("Verdadero o falso: las fuerzas de acción y reacción actúan sobre el mismo cuerpo.", "Falso", "Actúan sobre cuerpos distintos."),
      ("Si la acción vale 25 N, ¿cuánto vale la reacción?", "25 N", "Tienen igual valor."),
      ("¿Cómo es el sentido de la reacción respecto de la acción?", "Contrario", "La tercera ley lo establece así."),
  ],
  und=[
      ("Una persona empuja una pared con 50 N. ¿Qué fuerza ejerce la pared sobre la persona? A) 50 N en sentido contrario; B) 0 N, porque la pared no se mueve.", "A", "La reacción existe aunque la pared no se desplace."),
      ("¿Por qué la acción y la reacción no se anulan en el DCL de un solo objeto? A) Porque actúan sobre cuerpos distintos; B) Porque una es mayor que la otra.", "A", "En un DCL solo hay fuerzas sobre ese objeto."),
      ("Dos carritos se empujan con fuerzas iguales. El primero es más liviano. ¿Cuál acelera más?", "El más liviano", "Con la misma fuerza, menor masa da mayor aceleración."),
  ],
  app=[
      arith("Un carrito de 5 kg empuja a otro con 20 N. Por reacción, ¿qué aceleración recibe el carrito de 5 kg? (sin roce)", "20//5", "La reacción de 20 N dividida por 5 kg.", " m/s²"),
      arith("Una fuerza neta de 20 N actúa sobre un carrito de 4 kg. ¿Cuál es su aceleración?", "20//4", "Fuerza neta dividida por masa.", " m/s²"),
      arith("Datos de ejemplo: con fuerza neta fija de 30 N, ¿qué aceleración tiene un objeto de 6 kg?", "30//6", "Fuerza neta dividida por masa.", " m/s²"),
  ],
  rea=[
      ("Un estudiante dice: «Como acción y reacción son iguales y contrarias, nada puede moverse». ¿Qué respondes? A) Es un error: actúan sobre cuerpos distintos y cada uno puede tener fuerza neta; B) Tiene razón, se anulan.", "A", "La suma solo se anula si ambas actúan sobre el mismo cuerpo."),
      arith("Dos carritos de 2 kg y 8 kg se empujan con fuerzas iguales. ¿Cuántas veces mayor es la aceleración del carrito de 2 kg?", "8//2", "La aceleración es inversamente proporcional a la masa.", " veces"),
  ],
  cha=[
      arith("Un bloque de 6 kg es empujado con 50 N y el roce es de 14 N. ¿Cuál es su aceleración?", "(50-14)//6", "Fuerza neta 36 N dividida por 6 kg.", " m/s²"),
      ("Un objeto de 3 kg se mueve a 4 m/s y la fuerza neta sobre él pasa a ser 0 N. ¿Qué velocidad tendrá 5 s después?", "4 m/s", "Con fuerza neta cero mantiene su velocidad por la primera ley."),
  ],
  context=[arith("Un carrito de 7 kg recibe, por reacción, una fuerza de 21 N de otro carrito, sin roce (dato de ejemplo). ¿Qué aceleración adquiere?", "21//7", "Fuerza dividida por masa.", " m/s²")],
  selfcheck=[("¿Qué dice la tercera ley de Newton?", "Cada fuerza de A sobre B tiene una igual y contraria de B sobre A", "Son acción y reacción."), ("¿Por qué las fuerzas de acción y reacción no se anulan?", "Porque actúan sobre cuerpos distintos", "Cada una afecta a un objeto diferente."), ("¿Qué relación hay entre masa y aceleración si la fuerza neta es fija?", "Inversa", "A más masa, menos aceleración.")],
  open_task=task("Diseña una investigación para comprobar cómo cambia la aceleración de un carrito al aumentar su masa, con la misma fuerza neta. Usa estos datos de ejemplo: fuerza neta 12 N y masas de 1 kg, 2 kg y 4 kg. Calcula la aceleración en cada caso, di qué variable cambias, cuál mides y cuáles controlas, y escribe una conclusión con un límite.", "Aceleraciones: 12, 6 y 3 m/s². Cambio la masa, mido la aceleración y controlo la fuerza neta y el piso. Conclusión: al duplicar la masa la aceleración se reduce a la mitad. Límite: son tres valores y el roce real podría cambiar los resultados.", ["calcula las tres aceleraciones", "nombra variable independiente, dependiente y controladas", "concluye y declara un límite"], ["tres cálculos y una conclusión"], ["no controlar la fuerza", "no declarar límite"], "Pregunta qué medirías para conocer el roce real."),
  reinforce="Escribe una pareja de acción y reacción de tu vida diaria y di sobre qué cuerpo actúa cada una.",
  extend="Explica por qué al empujar una pared tú puedes retroceder aunque la pared no se mueva.")

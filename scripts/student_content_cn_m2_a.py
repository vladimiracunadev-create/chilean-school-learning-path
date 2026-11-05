"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 01 (sistema nervioso, estímulos y cuidados) y OA 02 (regulación hormonal de la glicemia y de la reproducción)."""
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


OA1 = "CN2M OA 01"
OA2 = "CN2M OA 02"

# ---------------------------------------------------------------- OA 01

L(OA1, 1,
  materials="Este cuaderno y lápiz. Todos los casos y datos están escritos en el cuaderno; no necesitas salir de tu casa.",
  use="Aprenderé cómo está organizado el sistema nervioso, qué hace una neurona y cómo se escribe una pregunta que se puede investigar sobre estímulos y respuestas. Sirve para separar lo que se puede medir de lo que es opinión.",
  prior=["Sé que el cuerpo está formado por células, tejidos y órganos.", "Sé que una pregunta investigable se contesta con observaciones o mediciones."],
  explain=[
      "El sistema nervioso coordina las acciones del cuerpo: recibe información del ambiente y del interior del organismo, la procesa y ordena una respuesta. Se divide en el sistema nervioso central (SNC), formado por el encéfalo y la médula espinal, y el sistema nervioso periférico, formado por los nervios que recorren el cuerpo. Un estímulo es un cambio del ambiente que detecta un receptor, como un ojo o la piel. La respuesta la ejecuta un efector, que es un músculo o una glándula.",
      "La unidad del sistema nervioso es la neurona. Tiene un cuerpo celular, dendritas que reciben señales y un axón largo que conduce el impulso nervioso hacia otras células. Las neuronas sensitivas llevan información desde los receptores hasta el SNC. Las neuronas motoras llevan la orden desde el SNC hasta los efectores. Las interneuronas conectan unas con otras dentro del SNC.",
      "Una pregunta investigable nombra algo que se puede medir y qué se compara. «¿Cambia la distancia que cae una regla antes de que una persona la atrape si hay música de fondo?» se puede investigar midiendo centímetros. «¿Es mejor tener reflejos rápidos?» no se puede investigar, porque «mejor» depende de cada persona y no indica qué medir.",
  ],
  vocab=[("estímulo", "cambio del ambiente que detecta un receptor"), ("receptor", "estructura que capta un estímulo, como un ojo o la piel"), ("efector", "músculo o glándula que ejecuta la respuesta"), ("neurona", "célula especializada en conducir impulsos nerviosos"), ("axón", "prolongación larga de la neurona que conduce el impulso")],
  worked=[
      ("Estímulo y respuesta", "Una persona siente que el agua de la ducha está muy fría y se aleja del chorro. Identifica el estímulo, el receptor y el efector.", ["El cambio del ambiente es la baja temperatura del agua: ese es el estímulo.", "La piel capta la temperatura: la piel es el receptor.", "Alejarse del chorro lo hacen los músculos: son el efector."], "Estímulo: agua fría; receptor: piel; efector: músculos"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Es genial atrapar una regla que cae?» para que se pueda investigar.", ["Quito la palabra de opinión: «genial».", "Indico qué se mide: los centímetros que cae la regla antes de ser atrapada.", "Indico qué se compara: con los ojos abiertos y con los ojos cerrados."], "«¿Cae más centímetros la regla antes de ser atrapada con los ojos cerrados que con los ojos abiertos?»"),
  ],
  mistakes=[
      ("Decir que el encéfalo es todo el sistema nervioso.", "El encéfalo es solo una parte del SNC; la médula espinal y los nervios también forman parte del sistema.", "Recuerda: SNC = encéfalo + médula espinal; los nervios son el sistema periférico."),
      ("Confundir el receptor con el efector.", "El receptor capta el estímulo; el efector ejecuta la respuesta.", "Pregunta: ¿esta estructura capta el cambio o ejecuta la acción?"),
  ],
  rec=[
      ("¿Cuáles son las dos partes del sistema nervioso central?", "Encéfalo y médula espinal", "El SNC está formado por esas dos estructuras."),
      ("Un ruido fuerte hace que una persona gire la cabeza. ¿Cómo se llama el ruido fuerte en este caso?", "Estímulo", "Es el cambio del ambiente que detecta un receptor."),
      ("Verdadero o falso: las dendritas son las prolongaciones de la neurona que reciben señales.", "Verdadero", "Las dendritas reciben información y el axón la conduce hacia otras células."),
  ],
  und=[
      ("¿Qué tipo de neurona lleva información desde un receptor de la piel hasta la médula espinal? A) Sensitiva; B) Motora.", "A", "Las neuronas sensitivas llevan la información hacia el SNC; las motoras la llevan desde él."),
      ("Una persona huele pan recién horneado y siente hambre. ¿Cuál es el receptor? A) El estómago; B) Las células de la nariz que captan el olor.", "B", "El receptor capta el estímulo, que aquí es el olor."),
      ("¿Qué parte de la neurona conduce el impulso nervioso hacia otras células?", "El axón", "El axón es la prolongación larga que conduce el impulso."),
  ],
  app=[
      ("¿Cuál de estas preguntas es investigable? A) ¿Cuántos milisegundos tarda una persona en apretar un botón después de ver una luz verde, con y sin sueño?; B) ¿Es injusto que algunas personas reaccionen más lento?", "A", "Indica qué se mide y qué se compara; la otra depende de una opinión."),
      arith("Un estudiante registró cuántos centímetros cayó una regla antes de atraparla en 5 intentos de ejemplo: 14, 18, 16, 12 y 15. ¿Cuál es el promedio?", "(14+18+16+12+15)//5", "Se suman los cinco datos y se divide por la cantidad de intentos."),
      ("Un semáforo cambia a verde y el conductor pisa el acelerador. ¿Qué estructura es el efector? A) Los ojos; B) Los músculos de la pierna.", "B", "Los músculos ejecutan la respuesta; los ojos son el receptor."),
  ],
  rea=[
      ("Un compañero dice: «Las neuronas motoras detectan el estímulo». ¿Qué le responderías? A) Los receptores detectan el estímulo; las neuronas motoras llevan la orden al efector; B) Tiene razón, porque «motor» significa que capta.", "A", "La detección corresponde al receptor; la neurona motora conduce la orden hacia el efector."),
      ("¿Por qué «¿Reaccionan mejor las personas simpáticas?» no es una pregunta investigable? A) Porque «simpática» y «mejor» no indican qué dato medir; B) Porque a las personas simpáticas no se les puede medir el tiempo de reacción.", "A", "Una pregunta investigable debe señalar una medición concreta."),
  ],
  cha=[
      ("En la vía receptor → neurona sensitiva → ___ → neurona motora → efector, ¿qué tipo de neurona va en el espacio?", "Interneurona", "Dentro del SNC las interneuronas conectan la neurona sensitiva con la motora."),
      ("Para investigar si el ruido cambia el tiempo de reacción, ¿qué diseño es correcto? A) Cambiar el ruido y medir cuánto cae la regla; B) Cambiar cuánto cae la regla y medir el ruido.", "A", "Se cambia a propósito lo que se estudia (ruido) y se mide el resultado (distancia)."),
  ],
  context=[arith("En una prueba de ejemplo la regla cayó 11, 13, 9 y 15 centímetros en cuatro intentos. ¿Cuántos centímetros más cayó en el intento más largo que en el más corto?", "15-9", "Se resta el menor valor al mayor.")],
  selfcheck=[("¿Qué diferencia hay entre receptor y efector?", "El receptor capta el estímulo y el efector ejecuta la respuesta", "Uno inicia la vía y el otro la termina."), ("Nombra las dos partes del sistema nervioso central.", "Encéfalo y médula espinal", "Los nervios pertenecen al sistema periférico."), ("¿Qué hace investigable a una pregunta?", "Que indica qué se mide y qué se compara", "Eso permite contestarla con datos.")],
  open_task=task("Lee estos tres casos: (1) una persona oye su nombre y se da vuelta; (2) alguien toca una olla tibia y retira la mano; (3) una persona ve una pelota que se acerca y la ataja. En cada caso escribe el estímulo, el receptor y el efector. Después escribe una pregunta investigable sobre uno de los casos que indique qué se mide.", "Caso 1: estímulo, sonido de su nombre; receptor, oído; efector, músculos del cuello. Pregunta: «¿Cuántos segundos tarda una persona en girar la cabeza al oír su nombre con la radio apagada y con la radio encendida?»", ["nombra estímulo, receptor y efector de los tres casos", "no confunde receptor con efector", "la pregunta indica qué se mide y qué se compara"], ["tres filas completas y una pregunta"], ["poner el encéfalo como receptor de todo", "escribir una pregunta de opinión"], "Pregunta qué instrumento o dato necesitarías para contestar tu pregunta."),
  reinforce="Dibuja una neurona y rotula cuerpo celular, dendritas y axón.",
  extend="Explica por qué una pregunta como «¿es mejor reaccionar rápido?» necesita cambiarse antes de investigarla.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. Las tablas con datos de ejemplo están escritas en los ejercicios. Si quieres repetir la prueba, necesitas una regla de plástico de 30 cm y una persona de tu casa.",
  use="Aprenderé a leer y comparar datos de tiempo de reacción, a calcular un promedio y a distinguir qué variable se cambia y cuál se mide. Sirve para concluir con datos y no solo con impresiones.",
  prior=["Sé qué es un estímulo, un receptor y un efector.", "Sé calcular un promedio de números enteros."],
  explain=[
      "El tiempo de reacción es el lapso entre que aparece un estímulo y comienza la respuesta. Una prueba segura para estimarlo es la caída de la regla: una persona suelta una regla y otra la atrapa con los dedos. Mientras más centímetros cae la regla antes de ser atrapada, más lento fue el tiempo de reacción. Así la distancia sirve como medida del tiempo.",
      "En una investigación hay tres tipos de variables. La variable independiente es la que se cambia a propósito, por ejemplo con ruido o sin ruido. La variable dependiente es la que se mide, aquí los centímetros. Las variables controladas se mantienen iguales, como la misma regla, la misma persona y la misma mano. Si no se controlan, no se sabe qué causó la diferencia.",
      "Un solo intento puede salir raro por distracción o suerte. Por eso se repite la medición y se calcula el promedio: se suman los datos y se divide por la cantidad de intentos. Un dato muy distinto de los demás se anota, se revisa qué ocurrió y se repite; no se borra sin explicación.",
  ],
  vocab=[("tiempo de reacción", "tiempo entre el estímulo y el inicio de la respuesta"), ("variable independiente", "la que se cambia a propósito"), ("variable dependiente", "la que se mide"), ("variable controlada", "la que se mantiene igual"), ("promedio", "suma de los datos dividida por la cantidad de datos")],
  worked=[
      ("Comparar promedios", "Datos de ejemplo en cm. Silencio: 12, 14, 13, 13. Con ruido: 17, 19, 16, 20. Calcula el promedio de cada condición y compara.", ["Silencio: 12 + 14 + 13 + 13 = 52; 52 ÷ 4 = 13 cm.", "Con ruido: 17 + 19 + 16 + 20 = 72; 72 ÷ 4 = 18 cm.", "18 es mayor que 13: con ruido la regla cayó más."], "Con ruido el promedio fue 18 cm y en silencio 13 cm: reacción más lenta con ruido en esta muestra"),
      ("Identificar variables", "Se estudia si el tiempo de reacción cambia con la mano que se usa. ¿Cuál es la variable independiente, cuál la dependiente y cuál se controla?", ["Lo que se cambia a propósito es la mano usada.", "Lo que se mide es la distancia de caída de la regla.", "Se mantienen iguales la regla y la persona que la suelta."], "Independiente: mano; dependiente: centímetros; controladas: regla y persona que suelta"),
  ],
  mistakes=[
      ("Concluir con un solo intento.", "Un intento puede estar afectado por la distracción o la suerte.", "Repite varias veces y usa el promedio."),
      ("Cambiar dos cosas a la vez, por ejemplo ruido y regla distinta.", "No se sabe cuál de las dos causó la diferencia.", "Cambia una sola variable y controla las demás."),
  ],
  rec=[
      ("Si la regla cae más centímetros antes de ser atrapada, ¿la reacción fue más rápida o más lenta?", "Más lenta", "Una caída mayor significa que tardó más en reaccionar."),
      ("¿Cómo se llama la variable que se mide en una investigación?", "Variable dependiente", "Es la que depende de lo que se cambia."),
      ("Verdadero o falso: repetir la medición varias veces ayuda a que un intento raro pese menos en la conclusión.", "Verdadero", "Con el promedio de varios intentos un dato raro influye menos."),
  ],
  und=[
      ("¿Por qué se usa la misma regla y la misma persona en todas las condiciones? A) Para que solo cambie la variable que se estudia; B) Para que los resultados salgan más grandes.", "A", "Controlar las demás variables permite atribuir la diferencia a lo que se cambió."),
      ("En la pregunta «¿cambia el tiempo de reacción según la hora del día?», ¿cuál es la variable independiente?", "La hora del día", "Es lo que se cambia a propósito."),
      ("Un dato es 31 cm y los otros tres son 13, 14 y 12. ¿Qué conviene hacer? A) Anotarlo, revisar qué ocurrió y repetir ese intento; B) Borrarlo sin decir nada porque no calza.", "A", "Un dato atípico se revisa y se repite; no se elimina sin explicación."),
  ],
  app=[
      arith("Con luz tenue la regla cayó 20, 22, 18 y 24 cm en cuatro intentos de ejemplo. ¿Cuál fue el promedio?", "(20+22+18+24)//4", "Se suman los cuatro datos y se divide por cuatro."),
      arith("Mano dominante: 9, 11 y 10 cm; mano no dominante: 14, 16 y 15 cm (datos de ejemplo). ¿Cuántos cm más cayó la regla en promedio con la mano no dominante?", "(14+16+15)//3-(9+11+10)//3", "Se calcula el promedio de cada mano y se restan."),
      ("Un gráfico de barras de ejemplo muestra el promedio de caída de la regla: condición A, 8 cm; condición B, 12 cm; condición C, 5 cm. ¿Qué condición tuvo la reacción más rápida?", "C", "La menor distancia de caída indica el menor tiempo de reacción."),
  ],
  rea=[
      ("Una persona hizo un intento por condición: con ruido 15 cm y en silencio 12 cm. Concluye que el ruido siempre empeora el tiempo de reacción. ¿Qué falla tiene? A) Con un intento por condición no puede afirmar «siempre»; B) Debió usar una regla más larga.", "A", "Pocos datos permiten, como máximo, una conclusión prudente."),
      ("Dos grupos midieron lo mismo, pero uno cambió la regla y el ruido a la vez. ¿Por qué su conclusión es débil? A) No puede saber si la diferencia vino del ruido o de la regla; B) Porque usó demasiadas condiciones.", "A", "Al cambiar dos variables a la vez se mezclan las causas."),
  ],
  cha=[
      arith("Cinco intentos de ejemplo dieron 12, 15, 11, 18 y 14 cm. Un sexto intento dio 20 cm. ¿Cuál es el promedio de los seis intentos?", "(12+15+11+18+14+20)//6", "Se suman los seis datos y se divide por seis."),
      ("Un equipo quiere saber si dormir poco cambia el tiempo de reacción. ¿Qué debe controlar? A) La misma regla, la misma persona y la misma hora de medición; B) Cambiar la regla en cada intento para variar.", "A", "Lo que no se estudia debe mantenerse igual."),
  ],
  context=[arith("En un grupo de ejemplo con poco sueño, la regla cayó 19, 23, 21 y 25 cm. ¿Cuál fue el promedio del grupo?", "(19+23+21+25)//4", "Se suman los datos y se divide por la cantidad de intentos.")],
  selfcheck=[("¿Qué mide la caída de la regla?", "El tiempo de reacción", "Más centímetros significan reacción más lenta."), ("Explica qué es una variable controlada.", "Es la que se mantiene igual en todas las condiciones", "Así solo cambia lo que se estudia."), ("¿Cómo se calcula un promedio?", "Se suman los datos y se divide por la cantidad de datos", "Resume varios intentos en un solo valor.")],
  open_task=task("Datos de ejemplo de caída de la regla en cm. Con música: 16, 18, 15, 19. Sin música: 12, 13, 11, 14. Calcula el promedio de cada condición, indica la variable independiente, la dependiente y una controlada, y escribe una conclusión de dos oraciones; la segunda debe declarar un límite de los datos.", "Con música el promedio es 17 cm y sin música 12,5 cm. Independiente: música; dependiente: centímetros; controlada: la misma regla. Con música la regla cayó más, es decir, la reacción fue más lenta. Son solo cuatro intentos por condición, por lo que no se puede generalizar a todas las personas.", ["calcula bien los dos promedios", "nombra las tres variables", "declara un límite de los datos"], ["dos promedios, tres variables y dos oraciones"], ["no declarar ningún límite", "afirmar «siempre» con cuatro datos"], "Pregunta cuántos intentos más harías y por qué."),
  reinforce="Escribe con tus palabras la diferencia entre variable independiente y dependiente.",
  extend="Explica por qué el promedio de varios intentos es más confiable que un intento aislado.")

L(OA1, 3,
  materials="Este cuaderno y lápiz. Para el modelo, hoja de papel y lápices de dos colores.",
  use="Aprenderé un modelo de cómo viaja una señal por una neurona, cómo pasa a la siguiente por la sinapsis y cómo se diferencia un acto reflejo de uno voluntario. Sirve para explicar qué pasa dentro del cuerpo entre un estímulo y una respuesta.",
  prior=["Sé qué hacen las neuronas sensitivas, motoras e interneuronas.", "Sé que un modelo simplifica la realidad."],
  explain=[
      "El impulso nervioso es una señal eléctrica que viaja por el axón de una neurona. Entre una neurona y la siguiente hay un pequeño espacio llamado sinapsis. Cuando el impulso llega al final del axón, la neurona libera neurotransmisores, que son sustancias químicas. Estas cruzan el espacio y se unen a receptores de la neurona siguiente; si hay suficiente señal, se genera un nuevo impulso.",
      "El modelo del arco reflejo representa una vía corta: receptor, neurona sensitiva, interneurona en la médula espinal, neurona motora y efector. Un acto reflejo es rápido e involuntario, porque la respuesta se organiza en la médula sin esperar una decisión del encéfalo, como retirar la mano de algo caliente. La información igual sigue hacia el encéfalo, por eso la persona se da cuenta de lo ocurrido un instante después. Un acto voluntario, como escribir, involucra al encéfalo y a muchas más sinapsis.",
      "Un modelo sirve para explicar, pero simplifica. Dibuja una cadena de pocas neuronas, mientras que el cuerpo real usa miles de conexiones al mismo tiempo. Por eso un modelo se usa para razonar, no para describir cada detalle. Mientras más sinapsis tenga una vía, más tiempo tarda la respuesta.",
  ],
  vocab=[("impulso nervioso", "señal eléctrica que viaja por el axón"), ("sinapsis", "espacio de comunicación entre dos neuronas"), ("neurotransmisor", "sustancia química que cruza la sinapsis"), ("acto reflejo", "respuesta rápida e involuntaria organizada en la médula"), ("arco reflejo", "vía que va del receptor al efector en un reflejo")],
  worked=[
      ("Rastrear un reflejo", "Una persona pisa una piedra puntiaguda y retira el pie. Ordena la vía del arco reflejo.", ["El receptor es la piel de la planta del pie: capta la presión.", "La neurona sensitiva lleva el impulso a la médula, donde una interneurona lo transmite.", "La neurona motora lleva la orden a los músculos de la pierna, que son el efector."], "Receptor, neurona sensitiva, interneurona, neurona motora, efector"),
      ("Describir una sinapsis", "Explica cómo pasa la señal de la neurona A a la neurona B.", ["El impulso llega al final del axón de A.", "A libera neurotransmisores en la sinapsis.", "Los neurotransmisores se unen a receptores de B y pueden generar un nuevo impulso."], "Un neurotransmisor cruza la sinapsis y activa a la neurona B"),
  ],
  mistakes=[
      ("Pensar que las neuronas se tocan y la señal pasa como por un cable continuo.", "Entre neuronas hay sinapsis y la señal pasa con neurotransmisores.", "Dibuja siempre el espacio entre las neuronas."),
      ("Decir que en un reflejo la persona no se entera nunca de lo ocurrido.", "El encéfalo recibe la información poco después y la persona la percibe.", "El reflejo parte en la médula, pero la información también sube al encéfalo."),
  ],
  rec=[
      ("¿Cómo se llama el espacio de comunicación entre dos neuronas?", "Sinapsis", "Es donde la señal pasa de una neurona a otra."),
      ("¿Cómo se llama la sustancia química que cruza la sinapsis?", "Neurotransmisor", "Transmite la señal de una neurona a la siguiente."),
      ("Verdadero o falso: en un acto reflejo la respuesta se organiza en la médula espinal.", "Verdadero", "Por eso es rápida e involuntaria."),
  ],
  und=[
      ("¿Qué diferencia a un reflejo de un acto voluntario? A) El reflejo es rápido, involuntario y se organiza en la médula; B) El reflejo siempre lo decide la corteza del encéfalo.", "A", "La corteza interviene en los actos voluntarios."),
      ("¿Cómo pasa la señal de una neurona a la siguiente? A) Un neurotransmisor cruza la sinapsis y se une a la neurona siguiente; B) El impulso eléctrico salta directamente de un axón al siguiente sin sustancias químicas.", "A", "La comunicación es química en la sinapsis."),
      ("En un arco reflejo de retirada ante algo caliente, ¿qué estructura capta primero el estímulo?", "El receptor de la piel", "La vía comienza donde se capta el estímulo."),
  ],
  app=[
      ("Una persona se quema el dedo con una vela y lo retira sin pensarlo. ¿Es un acto reflejo o voluntario?", "Reflejo", "Es rápido, involuntario y la respuesta se organiza en la médula sin una decisión."),
      arith("Una vía de ejemplo tiene 2 sinapsis y otra tiene 6 sinapsis. Cada sinapsis agrega 3 milisegundos. ¿Cuántos milisegundos más tarda la vía larga?", "(6-2)*3", "Se multiplica la diferencia de sinapsis por el tiempo de cada una."),
      ("La neurona motora lleva información. ¿Hacia dónde? A) Desde el sistema nervioso central hacia el efector; B) Desde el receptor hacia el sistema nervioso central.", "A", "La motora conduce la orden hacia músculos o glándulas."),
  ],
  rea=[
      ("Un compañero dice: «Como el reflejo no pasa por el encéfalo, la persona nunca se entera». ¿Qué le corriges? A) El encéfalo recibe la información después y la persona percibe lo ocurrido; B) Tiene razón, porque la médula no avisa a nadie.", "A", "El reflejo es rápido, pero la información sigue hacia el encéfalo."),
      ("Un fármaco de ejemplo bloquea los receptores de neurotransmisor de la neurona B. ¿Qué pasaría con la señal que llega desde A? A) No se transmitiría bien a B; B) Pasaría más rápido a B.", "A", "Sin receptores disponibles, el neurotransmisor no puede activar a la neurona siguiente."),
  ],
  cha=[
      ("Una persona retira la mano de una superficie muy caliente. ¿Qué ocurre antes? A) La mano se retira y después se percibe el dolor; B) Primero se decide retirarla y después se mueve.", "A", "El reflejo ocurre en la médula antes de que la información llegue a la parte consciente."),
      ("¿Qué simplifica el modelo del arco reflejo de cinco pasos? A) Que en el cuerpo real participan miles de neuronas y conexiones, no una sola cadena; B) Que las neuronas nunca se comunican entre sí.", "A", "Un modelo reduce la complejidad para poder razonar."),
  ],
  context=[("Una persona de ejemplo pisa una piedra y retira el pie. ¿Qué estructuras son el efector?", "Los músculos de la pierna", "El efector ejecuta la respuesta de retirar el pie.")],
  selfcheck=[("¿Qué cruza la sinapsis?", "Un neurotransmisor", "Es una sustancia química liberada por la neurona."), ("Nombra una característica de un acto reflejo.", "Es rápido e involuntario", "Se organiza en la médula espinal."), ("¿Qué limita a un modelo del arco reflejo?", "Que simplifica la gran cantidad de conexiones reales", "Sirve para razonar, no para describir todo.")],
  open_task=task("Dibuja el arco reflejo de una persona que toca una olla caliente. Rotula receptor, neurona sensitiva, interneurona, neurona motora y efector. Debajo escribe dos oraciones: una que explique cómo pasa la señal por una sinapsis y otra que diga un límite de tu dibujo.", "Receptor: piel de la mano; sensitiva: lleva el impulso a la médula; interneurona en la médula; motora: lleva la orden; efector: músculos del brazo. En la sinapsis el neurotransmisor cruza el espacio y activa a la neurona siguiente. Mi dibujo muestra pocas neuronas, pero en el cuerpo hay miles.", ["rotula las cinco estructuras en orden", "explica la sinapsis con neurotransmisor", "declara un límite del modelo"], ["dibujo rotulado y dos oraciones"], ["omitir la interneurona", "decir que la señal pasa sin espacio entre neuronas"], "Pregunta qué cambiaría si la vía llegara hasta el encéfalo."),
  reinforce="Escribe los cinco pasos de un arco reflejo en el orden correcto.",
  extend="Explica por qué un acto voluntario tarda más que un reflejo.")

L(OA1, 4,
  materials="Este cuaderno y lápiz. Las tablas con datos de ejemplo están escritas en los ejercicios; no necesitas medir nada.",
  use="Aprenderé cómo se relacionan las horas de sueño y el consumo de cafeína con la atención, y cómo leer una tabla para decir si la relación es directa o inversa. Sirve para cuidar tu sistema nervioso con evidencia.",
  prior=["Sé qué son variable independiente y dependiente.", "Sé calcular promedios y diferencias."],
  explain=[
      "Dormir es necesario para que el sistema nervioso funcione bien. Durante el sueño el cerebro ordena recuerdos y se recupera del día. Para personas de 14 a 17 años se recomienda dormir entre 8 y 10 horas. Con poco sueño disminuyen la atención y la memoria, y el tiempo de reacción se alarga.",
      "Dos variables se pueden relacionar de dos formas. En una relación directa, si una aumenta, la otra también. En una relación inversa, si una aumenta, la otra disminuye. Por ejemplo, a más horas de sueño suelen aparecer menos errores en una prueba de atención: es una relación inversa.",
      "La cafeína del café, el té y algunas bebidas energéticas es un estimulante: bloquea receptores de la adenosina, una sustancia que produce la sensación de sueño. Por eso quita el sueño por un rato, pero no reemplaza el descanso, y tomarla en la tarde puede dificultar dormir. Que dos variables se relacionen no prueba que una cause la otra: puede haber una tercera variable, como el estrés, que afecte a ambas.",
  ],
  vocab=[("relación directa", "si una variable aumenta, la otra también"), ("relación inversa", "si una variable aumenta, la otra disminuye"), ("cafeína", "estimulante presente en café, té y algunas bebidas energéticas"), ("adenosina", "sustancia que produce la sensación de sueño"), ("variable de confusión", "tercera variable que afecta a las otras dos")],
  worked=[
      ("Leer una relación", "Tabla de ejemplo. Horas de sueño: 5, 6, 7, 8. Errores en una prueba de atención: 12, 9, 6, 3. ¿Qué tipo de relación hay?", ["Al pasar de 5 a 8 horas, los errores bajan de 12 a 3.", "Cuando una variable aumenta, la otra disminuye."], "Relación inversa: más horas de sueño, menos errores"),
      ("Cuidado con la causa", "Las personas que duermen poco también toman más café y tienen más errores. ¿Se puede concluir que solo la falta de sueño causa los errores?", ["El café también cambia entre los grupos.", "No se puede separar el efecto del sueño del efecto del café con estos datos."], "No, porque hay otra variable que cambia a la vez"),
  ],
  mistakes=[
      ("Creer que el café reemplaza las horas de sueño.", "La cafeína solo tapa la sensación de sueño; el cerebro igual necesita descansar.", "Prioriza dormir las horas recomendadas."),
      ("Concluir que si dos variables se mueven juntas, una es la causa de la otra.", "Puede existir una tercera variable que explique ambas.", "Escribe «se relacionan», no «causa», salvo que se controlen las demás variables."),
  ],
  rec=[
      ("¿Cuántas horas se recomienda dormir entre los 14 y los 17 años?", "Entre 8 y 10 horas", "Es el rango recomendado para la adolescencia."),
      ("Si una variable aumenta y la otra disminuye, ¿qué relación hay?", "Inversa", "Una sube mientras la otra baja."),
      ("Verdadero o falso: la cafeína es un estimulante.", "Verdadero", "Reduce la sensación de sueño al bloquear a la adenosina."),
  ],
  und=[
      ("¿Qué efecto tiene la adenosina en el cuerpo? A) Produce la sensación de sueño; B) Aumenta la energía de forma permanente.", "A", "La cafeína actúa bloqueando los receptores de la adenosina."),
      ("¿Por qué no conviene tomar bebidas con cafeína en la tarde si se quiere dormir bien? A) Porque pueden dificultar quedarse dormido; B) Porque la cafeína causa sueño.", "A", "Como estimulante, retrasa la sensación de sueño."),
      ("A más horas de práctica de piano, más notas correctas. ¿Qué relación hay entre esas dos variables?", "Directa", "Ambas aumentan juntas."),
  ],
  app=[
      ("Tabla de ejemplo. Estudiante 1: 6 h de sueño, 10 errores; estudiante 2: 8 h, 4 errores; estudiante 3: 7 h, 7 errores. ¿Quién durmió menos y cometió más errores?", "El estudiante 1", "Tiene el menor valor de horas y el mayor de errores."),
      arith("En un grupo de ejemplo, 5 estudiantes que durmieron 6 horas tuvieron en total 40 errores y 5 que durmieron 9 horas tuvieron 15 errores. ¿Cuántos errores más tuvo en promedio por estudiante el grupo que durmió menos?", "40//5-15//5", "Se calcula el promedio de cada grupo y se restan."),
      ("Los datos muestran que, al subir las horas de pantalla antes de dormir, bajan las horas de sueño. ¿Qué relación es? A) Inversa; B) Directa.", "A", "Una variable sube mientras la otra baja."),
  ],
  rea=[
      ("Un estudio de ejemplo encontró que quienes toman más bebidas energéticas tienen peores notas. Un compañero dice: «Las bebidas causan las malas notas». ¿Qué crítica es correcta? A) Podría haber otra variable, como dormir poco, que afecte a ambas; B) No puede ser, porque las bebidas no se relacionan con nada.", "A", "Una relación no prueba causa; falta controlar otras variables."),
      ("Dos grupos de ejemplo: el grupo A durmió 9 h y el B durmió 6 h, pero B también estudió más tarde. Si B rinde peor, ¿qué se puede afirmar con prudencia? A) Hay relación entre dormir poco y rendir peor, pero no se descarta el efecto de la hora de estudio; B) Dormir poco es la única causa, sin duda.", "A", "Dos variables cambian a la vez y no se pueden separar."),
  ],
  cha=[
      ("Tabla de ejemplo. Café al día (tazas): 0, 1, 2, 3. Horas de sueño: 9, 8, 7, 6. ¿Cuántas horas de sueño bajan por cada taza adicional?", "1 hora", "Cada fila baja 1 hora al subir 1 taza."),
      ("Para saber si dormir más mejora la atención, un equipo mide a las mismas personas dos noches: una con 6 horas y otra con 9 horas. ¿Qué mejora ese diseño? A) Compara a las mismas personas y reduce diferencias entre individuos; B) Permite que cada persona elija cuántas horas dormir.", "A", "Usar a las mismas personas controla variables personales."),
  ],
  context=[arith("Una estudiante de ejemplo duerme 7 horas de lunes a viernes y 10 horas el sábado y el domingo. ¿Cuántas horas duerme en la semana?", "7*5+10*2", "Se multiplican las horas por los días de cada tipo y se suman.")],
  selfcheck=[("¿Qué es una relación inversa?", "Cuando una variable aumenta y la otra disminuye", "Se mueven en direcciones opuestas."), ("¿Por qué la cafeína no reemplaza el sueño?", "Porque solo tapa la sensación de sueño y el cerebro igual necesita descansar", "No cumple las funciones del descanso."), ("¿Qué es una variable de confusión?", "Una tercera variable que afecta a las otras dos", "Impide atribuir la causa con seguridad.")],
  open_task=task("Datos de ejemplo de cuatro estudiantes. Analiza esta tabla: horas de sueño 6, 7, 8, 9 y errores 14, 11, 6, 4. Describe la relación (directa o inversa), calcula cuántos errores menos hay entre 6 h y 9 h, y escribe una recomendación para una persona de tu edad con un límite de los datos.", "La relación es inversa. Entre 6 h y 9 h hay 10 errores menos (14 − 4). Recomendación: dormir entre 8 y 10 horas. Los datos son de ejemplo y de solo cuatro personas, así que no prueban la causa.", ["indica la relación correcta", "calcula la diferencia bien", "da una recomendación y un límite"], ["descripción, cálculo y recomendación"], ["decir que la relación es directa", "afirmar que los datos prueban la causa"], "Pregunta qué otra variable podría influir."),
  reinforce="Escribe dos ejemplos de relaciones directas y dos de relaciones inversas de tu vida diaria.",
  extend="Explica por qué se recomienda dormir las horas necesarias y no reemplazar el sueño con cafeína.")

L(OA1, 5,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios. Los casos son ficticios.",
  use="Aprenderé cómo el alcohol y otras drogas alteran la comunicación entre neuronas y por qué eso cambia la conducta, los reflejos y el juicio. Sirve para tomar decisiones informadas y saber a quién pedir ayuda.",
  prior=["Sé qué es la sinapsis y qué hace un neurotransmisor.", "Sé leer relaciones directas e inversas."],
  explain=[
      "Una droga es una sustancia que, al entrar al cuerpo, modifica el funcionamiento del sistema nervioso. Muchas actúan en las sinapsis: imitan, bloquean o aumentan la acción de los neurotransmisores. Algunas son estimulantes, que aceleran la actividad nerviosa; otras son depresoras, que la enlentecen. El alcohol es una droga depresora, aunque sea legal para personas adultas.",
      "El alcohol enlentece la transmisión de señales en el cerebro. Como efecto, aumenta el tiempo de reacción, empeora la coordinación, el equilibrio y el juicio, y se toman más riesgos. Por eso nunca se debe conducir después de beber. En la adolescencia el cerebro aún está madurando, y el consumo puede afectarlo más. El consumo repetido puede producir tolerancia, que es necesitar más cantidad para el mismo efecto, y dependencia.",
      "Ante la presión para consumir, o si te preocupa tu consumo o el de alguien cercano, lo correcto es contarlo a una persona adulta de confianza, como una familiar, un docente o un profesional de salud. No se guarda en secreto ni se enfrenta solo a quien presiona.",
  ],
  vocab=[("droga", "sustancia que modifica el funcionamiento del sistema nervioso"), ("estimulante", "droga que acelera la actividad nerviosa"), ("depresor", "droga que enlentece la actividad nerviosa"), ("tolerancia", "necesidad de más cantidad para obtener el mismo efecto"), ("dependencia", "necesidad del cuerpo y la mente de seguir consumiendo")],
  worked=[
      ("Explicar un efecto", "Datos de ejemplo: sin alcohol, una persona atrapa la regla tras caer 12 cm; con alcohol, tras caer 24 cm. ¿Qué indica y cuál es el mecanismo?", ["La regla cayó el doble: el tiempo de reacción aumentó.", "El alcohol enlentece la transmisión de señales entre neuronas."], "La reacción es más lenta porque el alcohol enlentece la transmisión nerviosa"),
      ("Clasificar", "Una bebida con mucha cafeína hace que una persona se sienta alerta y con el corazón acelerado. ¿Es estimulante o depresora?", ["Alerta y corazón acelerado indican mayor actividad nerviosa.", "Eso corresponde a un estimulante."], "Estimulante"),
  ],
  mistakes=[
      ("Pensar que el alcohol es estimulante porque la persona se pone habladora.", "El alcohol es depresor; al principio baja el control y por eso hay más conversación y más riesgos.", "Recuerda el efecto en las neuronas: enlentece."),
      ("Creer que, si algo es legal, no daña el sistema nervioso.", "La ley regula quién puede consumir, pero la sustancia afecta igual al cerebro.", "Evalúa el efecto biológico, no solo la ley."),
  ],
  rec=[
      ("¿El alcohol es una droga estimulante o depresora?", "Depresora", "Enlentece la actividad del sistema nervioso."),
      ("¿Cómo se llama la necesidad de más cantidad de una sustancia para obtener el mismo efecto?", "Tolerancia", "Es un cambio del cuerpo ante el consumo repetido."),
      ("Verdadero o falso: muchas drogas actúan modificando la acción de los neurotransmisores en las sinapsis.", "Verdadero", "Imitan, bloquean o aumentan la acción de los neurotransmisores."),
  ],
  und=[
      ("¿Por qué no se debe conducir después de beber alcohol? A) Porque aumenta el tiempo de reacción y empeora el juicio; B) Porque el alcohol mejora los reflejos pero cansa.", "A", "La reacción más lenta aumenta el riesgo de accidentes."),
      ("¿Qué hace una droga estimulante? A) Acelera la actividad del sistema nervioso; B) La enlentece.", "A", "El estimulante aumenta la actividad nerviosa."),
      ("Una persona de ejemplo siente presión de sus amistades para consumir una sustancia. ¿Qué es lo más seguro? A) Contarlo a una persona adulta de confianza; B) Aceptar para evitar conflictos y no contarlo a nadie.", "A", "Pedir apoyo a un adulto protege y no deja a la persona sola."),
  ],
  app=[
      arith("Una persona de ejemplo reaccionó en 15 cm sin alcohol y en 30 cm con alcohol. ¿Cuántos cm más cayó la regla con alcohol?", "30-15", "Se resta la distancia sin alcohol a la distancia con alcohol."),
      ("Datos de ejemplo de una investigación: con 0 vasos, 11 cm; con 1 vaso, 15 cm; con 2 vasos, 20 cm; con 3 vasos, 26 cm. ¿Qué relación hay entre vasos y distancia? A) Directa; B) Inversa.", "A", "Al subir los vasos sube la distancia de caída."),
      ("Un fármaco bloquea la acción de un neurotransmisor que activa músculos. ¿Qué efecto se espera? A) Menos respuesta muscular; B) Más respuesta muscular.", "A", "Si la señal no se transmite, el efector responde menos."),
  ],
  rea=[
      ("Un compañero dice: «Tomé café, así que puedo dormir menos sin problema». ¿Qué le responderías? A) La cafeína tapa el sueño pero no reemplaza el descanso del cerebro; B) Tiene razón, la cafeína repone el sueño.", "A", "Dormir tiene funciones que la cafeína no cumple."),
      ("Alguien dice: «El alcohol afecta igual a todas las personas». ¿Qué falta en esa afirmación? A) Depende de la cantidad, la edad, el peso y el estado de salud, entre otros factores; B) Nada, siempre es igual.", "A", "Los efectos varían entre personas y circunstancias."),
  ],
  cha=[
      ("Un caso ficticio: Ana ve que un amigo está muy preocupado por su consumo de alcohol y le pide que no lo cuente. ¿Qué es lo más responsable? A) Avisar a una persona adulta de confianza, porque la ayuda de un adulto protege; B) Guardar el secreto para no perder la amistad.", "A", "Los riesgos de salud no se guardan en secreto: se cuentan a un adulto."),
      ("Un gráfico de ejemplo muestra que, con más alcohol, el tiempo de reacción sube. ¿Qué límite tiene concluir que el alcohol siempre causa accidentes? A) Los datos de reacción no miden todos los factores de un accidente; B) Ninguno, porque en el laboratorio se miden todos los factores de un accidente.", "A", "Una medida de laboratorio no cubre todas las causas de un accidente."),
  ],
  context=[arith("Una campaña de ejemplo informa que 3 de cada 10 estudiantes encuestados no sabían que el alcohol es depresor. Si se encuestó a 200 estudiantes, ¿cuántos no lo sabían?", "200//10*3", "Se calcula un décimo del total y se multiplica por tres.")],
  selfcheck=[("¿Cómo actúan muchas drogas en el sistema nervioso?", "Modifican la acción de los neurotransmisores en las sinapsis", "Imitan, bloquean o aumentan su acción."), ("¿Por qué el alcohol aumenta el riesgo al conducir?", "Porque enlentece la reacción y empeora el juicio", "Eso aumenta la probabilidad de accidentes."), ("¿A quién le cuentas si te sientes presionado o presionada a consumir?", "A una persona adulta de confianza", "No se guarda en secreto ni se enfrenta solo.")],
  open_task=task("Caso ficticio: Tomás, de 16 años, va a una fiesta y le ofrecen alcohol varias veces. Escribe tres consecuencias del alcohol en el sistema nervioso que explicarían por qué es riesgoso volver a casa en bicicleta o cruzar calles, y una frase que Tomás puede decir para negarse. Cierra con a quién puede pedir ayuda después.", "Consecuencias: reacción más lenta, peor coordinación y peor juicio. Frase: «Gracias, yo no tomo». Después puede contarle a una persona adulta de confianza, como un familiar o un docente.", ["nombra tres efectos en el sistema nervioso", "da una frase breve para negarse", "indica una persona adulta de confianza"], ["tres efectos, una frase y una persona de apoyo"], ["decir que el alcohol estimula", "sugerir ocultar el caso"], "Pregunta qué otro plan seguro tendría Tomás para volver a casa."),
  reinforce="Explica con tus palabras qué hace el alcohol en las sinapsis y en el tiempo de reacción.",
  extend="Explica por qué contar a un adulto de confianza es una conducta de cuidado y no una traición.")

L(OA1, 6,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a prevenir traumatismos que dañan el encéfalo y la médula espinal, a evaluar un dato de una campaña y a comunicar un cuidado con evidencia. Sirve para proteger tu sistema nervioso y el de otras personas.",
  prior=["Sé que el encéfalo y la médula espinal forman el SNC.", "Sé que una conclusión debe declarar límites."],
  explain=[
      "Un traumatismo es una lesión causada por un golpe o una fuerza externa. El traumatismo encefalocraneano (TEC) es un golpe en la cabeza que puede dañar el encéfalo. La médula espinal también puede lesionarse en la columna, y un daño allí puede afectar el movimiento y la sensibilidad por debajo de la lesión. El sistema nervioso central tiene poca capacidad de recuperarse, por eso conviene prevenir.",
      "La prevención usa medidas simples: casco en bicicleta, patineta y moto; cinturón de seguridad y sillas adecuadas para niñas y niños; no conducir tras consumir alcohol; evitar zambullirse en aguas poco profundas o desconocidas. Después de un golpe fuerte en la cabeza, con mareo, vómitos, confusión o pérdida de conocimiento, se debe pedir ayuda a una persona adulta y consultar a un servicio de salud. Si hay sospecha de lesión en la columna, no se mueve a la persona y se avisa a emergencia.",
      "Para evaluar una campaña se mira el dato y sus límites. Un dato de ejemplo puede mostrar que quienes usan casco tienen menos lesiones, pero no prueba todo: pueden usarlo más las personas que además van más lento. Comunicar un cuidado significa dar un mensaje breve, claro y apoyado en evidencia.",
  ],
  vocab=[("traumatismo", "lesión causada por un golpe o una fuerza externa"), ("TEC", "traumatismo encefalocraneano: golpe en la cabeza que puede dañar el encéfalo"), ("prevención", "medidas que se toman antes para evitar un daño"), ("lesión medular", "daño en la médula espinal"), ("evidencia", "dato u observación que apoya una afirmación")],
  worked=[
      ("Evaluar un dato", "Datos de ejemplo: de 100 ciclistas sin casco, 20 sufrieron TEC; de 100 ciclistas con casco, 8. ¿Qué indican y cuál es su límite?", ["Hubo 20 − 8 = 12 casos menos con casco por cada 100 ciclistas.", "Los datos son de ejemplo y no controlan velocidad ni lugar."], "El casco se asocia con menos TEC, pero los datos no prueban toda la causa"),
      ("Elegir una medida", "Una persona quiere andar en patineta por una calle con baja pendiente. ¿Qué medida de prevención corresponde?", ["El riesgo principal es un golpe en la cabeza.", "La medida es usar casco y protecciones."], "Usar casco y protecciones"),
  ],
  mistakes=[
      ("Mover a una persona con sospecha de lesión en la columna para «ayudarla».", "Moverla puede dañar más la médula espinal.", "No muevas a la persona y avisa a emergencia o a una persona adulta."),
      ("Pensar que, si no hubo pérdida de conocimiento, el golpe en la cabeza no es grave.", "Algunas lesiones no causan desmayo y se notan después, con mareo, vómitos o confusión.", "Observa síntomas y consulta si aparecen."),
  ],
  rec=[
      ("¿Qué significa la sigla TEC?", "Traumatismo encefalocraneano", "Es un golpe en la cabeza que puede dañar el encéfalo."),
      ("Nombra un elemento de protección para andar en bicicleta.", "Casco", "Protege la cabeza ante caídas y golpes."),
      ("Verdadero o falso: si hay sospecha de lesión en la columna, conviene mover a la persona para acomodarla.", "Falso", "Moverla puede dañar más la médula espinal."),
  ],
  und=[
      ("¿Por qué conviene prevenir los traumatismos del sistema nervioso central? A) Porque tiene poca capacidad de recuperarse; B) Porque siempre se curan solos.", "A", "El daño en el SNC suele ser difícil de revertir."),
      ("Tras un golpe fuerte en la cabeza, una persona tiene mareo y vómitos. ¿Qué corresponde? A) Avisar a un adulto y consultar a un servicio de salud; B) Seguir jugando para ver si pasa.", "A", "Esos síntomas pueden indicar daño y requieren evaluación."),
      ("¿Para qué se usa el cinturón de seguridad en un auto?", "Para evitar golpes fuertes de la cabeza y el cuerpo en un frenazo", "Limita el movimiento del cuerpo ante un frenazo o choque."),
  ],
  app=[
      arith("En un curso de ejemplo de 40 estudiantes, 28 usan casco al ir en bicicleta. ¿Cuántos no lo usan?", "40-28", "Se resta a las personas del curso las que usan casco."),
      ("Datos de ejemplo: 150 ciclistas con casco, 12 con lesión de cabeza; 150 ciclistas sin casco, 30 con lesión de cabeza. ¿Qué grupo tuvo más casos de lesión de cabeza?", "Los que no usaban casco", "30 es mayor que 12."),
      ("Un mensaje de campaña dice: «Usa casco: reduces el riesgo de lesión en la cabeza». ¿Qué cumple como mensaje? A) Es breve, claro y apoyado en una medida de prevención; B) Es largo y no dice qué hacer.", "A", "Un buen mensaje es breve y dice qué conducta cuidar."),
  ],
  rea=[
      ("Una campaña de ejemplo dice: «El casco evita el 100 % de las lesiones». ¿Qué crítica es correcta? A) Los datos de ejemplo muestran menos lesiones, no ausencia total; la frase exagera; B) La frase es correcta porque el casco es duro.", "A", "Los datos apoyan una reducción, no una eliminación."),
      ("En un estudio de ejemplo, quienes usan casco tienen menos TEC, pero también andan más lento. ¿Qué limita la conclusión? A) La velocidad es otra variable que también cambia entre los grupos; B) Ninguna variable la limita, porque el casco es lo único que cambia entre los grupos.", "A", "No se puede atribuir toda la diferencia al casco."),
  ],
  cha=[
      arith("En una escuela de ejemplo hubo 36 caídas en bicicleta en un año, sin campaña. Tras una campaña de casco hubo 27. ¿Cuántas caídas menos hubo?", "36-27", "Se resta el número de caídas tras la campaña al número inicial."),
      ("Un compañero propone zambullirse en una laguna que no conoce. ¿Qué riesgo de traumatismo hay? A) Golpearse la cabeza o la columna si es poco profunda; B) Ninguno, porque el agua siempre amortigua el golpe.", "A", "No conocer la profundidad aumenta el riesgo de golpe en cabeza y columna."),
  ],
  context=[("Una estudiante de ejemplo se cae del patín y se golpea la cabeza; se siente confusa. ¿Qué debe hacer primero?", "Avisar a una persona adulta y consultar a un servicio de salud", "La confusión tras un golpe es una señal de alerta.")],
  selfcheck=[("¿Qué es un TEC?", "Un golpe en la cabeza que puede dañar el encéfalo", "Es un traumatismo encefalocraneano."), ("Nombra dos medidas para prevenir traumatismos.", "Casco y cinturón de seguridad", "También no zambullirse en aguas desconocidas."), ("¿Qué límite tiene un dato de ejemplo sobre el casco?", "Que puede haber otras variables, como la velocidad", "Un dato aislado no prueba toda la causa.")],
  open_task=task("Usa estos datos de ejemplo: de 200 personas sin casco, 40 sufrieron lesión de cabeza; de 200 con casco, 16. Escribe un mensaje de campaña de máximo 20 palabras que use un dato, y una oración que declare un límite del dato. Después escribe qué haría una persona de tu edad si un amigo se golpea la cabeza y está confuso.", "Mensaje: «Con casco hubo 24 casos menos por cada 200 personas: cuídate, usa casco». Límite: son datos de ejemplo y no controlan la velocidad. Se avisa a un adulto y se consulta a un servicio de salud.", ["usa correctamente el dato (40 − 16 = 24)", "el mensaje es breve y claro", "declara un límite y avisa a un adulto"], ["mensaje, límite y acción"], ["exagerar con «100 %»", "proponer no consultar a nadie"], "Pregunta qué dato extra mejoraría la campaña."),
  reinforce="Escribe tres medidas de prevención de traumatismos en tu vida diaria.",
  extend="Explica por qué un mensaje de campaña debe evitar exagerar los datos.")

# ---------------------------------------------------------------- OA 02

L(OA2, 1,
  materials="Este cuaderno y lápiz. Todos los datos están escritos en los ejercicios.",
  use="Aprenderé qué es la glicemia, qué hormonas del páncreas la regulan y cómo escribir una pregunta investigable sobre ella. Sirve para entender cómo el cuerpo mantiene la energía disponible.",
  prior=["Sé que las células usan glucosa como fuente de energía.", "Sé que el sistema digestivo absorbe nutrientes a la sangre."],
  explain=[
      "La glicemia es la concentración de glucosa en la sangre. En una persona sana, en ayunas, suele estar en un rango estrecho de alrededor de 70 a 100 mg/dL. Mantenerla estable es importante, porque las células, sobre todo las neuronas, necesitan glucosa de forma continua.",
      "Una hormona es un mensajero químico que una glándula libera a la sangre y que actúa sobre células blanco. El páncreas produce dos hormonas que regulan la glicemia. La insulina baja la glicemia: permite que las células tomen glucosa y que el hígado la almacene como glucógeno. El glucagón sube la glicemia: hace que el hígado libere la glucosa almacenada.",
      "Después de comer aumenta la glicemia y el páncreas libera insulina. Entre comidas o durante el ayuno la glicemia baja y el páncreas libera glucagón. Una pregunta investigable sobre esto indica qué se mide y cuándo: «¿Cuánto sube la glicemia 60 minutos después de un desayuno con pan, comparada con uno con avena?».",
  ],
  vocab=[("glicemia", "concentración de glucosa en la sangre"), ("hormona", "mensajero químico liberado a la sangre por una glándula"), ("insulina", "hormona del páncreas que baja la glicemia"), ("glucagón", "hormona del páncreas que sube la glicemia"), ("glucógeno", "forma en que el hígado almacena glucosa")],
  worked=[
      ("Elegir la hormona", "Una persona lleva 8 horas sin comer y su glicemia está bajando. ¿Qué hormona libera el páncreas?", ["La glicemia baja y hay que subirla.", "La hormona que sube la glicemia es el glucagón."], "Glucagón"),
      ("Mejorar una pregunta", "Mejora «¿Es bueno comer dulces?» para que sea investigable.", ["Quito «bueno», que es opinión.", "Indico qué se mide y cuándo: la glicemia 30 minutos después de comer."], "«¿Cuánto sube la glicemia 30 minutos después de comer un alimento dulce, en comparación con una fruta?»"),
  ],
  mistakes=[
      ("Confundir insulina con glucagón.", "La insulina baja la glicemia; el glucagón la sube.", "Asocia insulina con «guardar» glucosa y glucagón con «liberar» glucosa."),
      ("Decir que la glucosa de la sangre es siempre perjudicial.", "La glucosa es necesaria; lo importante es mantenerla en un rango estable.", "Habla de regulación, no de «eliminar» glucosa."),
  ],
  rec=[
      ("¿Qué órgano produce la insulina y el glucagón?", "El páncreas", "Es la glándula que regula la glicemia."),
      ("¿Qué es la glicemia?", "La concentración de glucosa en la sangre", "Es lo que se mide al evaluar el azúcar en la sangre."),
      ("Verdadero o falso: la insulina baja la glicemia.", "Verdadero", "Permite que las células tomen glucosa y que el hígado la almacene."),
  ],
  und=[
      ("¿Qué hace el glucagón? A) Hace que el hígado libere glucosa y sube la glicemia; B) Hace que las células guarden glucosa y baja la glicemia.", "A", "El glucagón actúa cuando la glicemia está baja."),
      ("¿Por qué las hormonas actúan solo sobre algunas células? A) Porque solo las células blanco tienen receptores para esa hormona; B) Porque la hormona viaja solo por los nervios.", "A", "La hormona viaja por la sangre, pero actúa donde hay receptores."),
      ("¿Cómo almacena el hígado la glucosa que sobra?", "Como glucógeno", "El glucógeno es la forma de almacenar glucosa."),
  ],
  app=[
      ("Una persona terminó de almorzar y su glicemia sube. ¿Qué hormona libera el páncreas? A) Insulina; B) Glucagón.", "A", "Con glicemia alta se libera insulina para bajarla."),
      arith("En ayunas, la glicemia de ejemplo es de 85 mg/dL. Tras comer sube 40 mg/dL. ¿Cuántos mg/dL marca ahora?", "85+40", "Se suma el aumento al valor inicial."),
      ("¿Cuál de estas preguntas es investigable? A) ¿Cuántos mg/dL cambia la glicemia a las 2 horas de comer un plato de legumbres?; B) ¿Son las legumbres la comida más rica?", "A", "Indica qué se mide y cuándo."),
  ],
  rea=[
      ("Un compañero dice: «La insulina sube la glicemia porque lleva glucosa a la sangre». ¿Qué le corriges? A) La insulina baja la glicemia: ayuda a que las células tomen glucosa de la sangre; B) Tiene razón, porque la insulina es azúcar.", "A", "La insulina no es azúcar: es una hormona que baja la glicemia."),
      ("Después de un ayuno largo, ¿por qué es útil que el hígado libere glucosa? A) Para que las neuronas y otras células sigan recibiendo energía; B) Para que el páncreas deje de producir insulina.", "A", "Las células necesitan glucosa continuamente."),
  ],
  cha=[
      ("Dos personas de ejemplo se midieron en ayunas y obtuvieron 150 mg/dL y 95 mg/dL. Si el rango habitual en ayunas es de 70 a 100, ¿cuál valor está por encima del rango? A) 150 mg/dL; B) 95 mg/dL.", "A", "Es mayor que el rango habitual."),
      ("¿Qué variable debería mantenerse igual para comparar la glicemia tras dos desayunos? A) La cantidad total de comida y la hora de medición; B) El tipo de alimento.", "A", "El tipo de alimento es lo que se cambia; lo demás se controla."),
  ],
  context=[arith("Una estudiante de ejemplo registra su glicemia en cuatro momentos: 82, 118, 96 y 88 mg/dL. ¿Cuál es la diferencia entre el valor más alto y el más bajo?", "118-82", "Se resta el menor valor al mayor.")],
  selfcheck=[("¿Qué hormona baja la glicemia?", "La insulina", "El glucagón la sube."), ("¿Qué órgano libera glucosa cuando la glicemia baja?", "El hígado", "Lo hace por acción del glucagón."), ("¿Qué indica una pregunta investigable?", "Qué se mide y cuándo", "Permite contestarla con datos.")],
  open_task=task("Lee estos tres momentos: (1) justo después de una comida abundante; (2) tras 10 horas de ayuno; (3) a media tarde sin haber comido desde el almuerzo. En cada uno indica si es más probable que la glicemia suba o baje y qué hormona libera el páncreas. Después escribe una pregunta investigable sobre uno de los momentos.", "1: sube, se libera insulina. 2: baja, se libera glucagón. 3: baja, se libera glucagón. Pregunta: «¿Cuántos mg/dL baja la glicemia 4 horas después del almuerzo?»", ["relaciona cada momento con una hormona", "usa «sube» y «baja» con sentido", "la pregunta indica qué se mide y cuándo"], ["tres respuestas y una pregunta"], ["invertir insulina y glucagón", "escribir una pregunta de opinión"], "Pregunta qué dato necesitarías para responder tu pregunta."),
  reinforce="Escribe con tus palabras qué hacen la insulina y el glucagón.",
  extend="Explica por qué las neuronas necesitan que la glicemia se mantenga estable.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Las tablas con datos de ejemplo están escritas en los ejercicios.",
  use="Aprenderé a leer una curva de glicemia después de comer y a describir cuándo sube, cuándo baja y qué hormona actúa. Sirve para interpretar datos de regulación hormonal.",
  prior=["Sé qué hacen la insulina y el glucagón.", "Sé leer tablas y gráficos de línea."],
  explain=[
      "Una curva de glicemia muestra cómo cambia la glucosa de la sangre a lo largo del tiempo. En una persona sana, antes de comer está en su valor basal. Después de comer sube, alcanza un máximo y luego vuelve a bajar hasta cerca del valor inicial gracias a la insulina. El tiempo que tarda en volver al valor basal depende de lo que se comió y de cuánta insulina hay.",
      "Para leer una curva se identifican tres cosas: el valor inicial, el valor máximo y el momento en que alcanza el máximo. También se calcula el cambio, que es el valor final menos el valor inicial. Si la curva baja demasiado, el glucagón actúa para subir la glicemia.",
      "Los datos de ejemplo permiten practicar, pero no se usan para decidir un tratamiento. El diagnóstico y el control de la glicemia lo hacen profesionales de la salud con exámenes. Una sola medición no basta: se miran varias a lo largo del tiempo.",
  ],
  vocab=[("valor basal", "valor inicial, antes de comer"), ("máximo", "valor más alto de la curva"), ("curva de glicemia", "gráfico de la glicemia en el tiempo"), ("cambio", "valor final menos valor inicial"), ("ayuno", "periodo sin comer")],
  worked=[
      ("Leer una curva", "Datos de ejemplo (minutos: mg/dL): 0: 88; 30: 126; 60: 138; 120: 98. Identifica el valor basal, el máximo y el momento del máximo.", ["El valor basal es el de minuto 0: 88 mg/dL.", "El mayor valor es 138 mg/dL.", "Ocurre a los 60 minutos."], "Basal 88 mg/dL; máximo 138 mg/dL a los 60 minutos"),
      ("Calcular un cambio", "Con los mismos datos, ¿cuánto cambió la glicemia entre el minuto 0 y el minuto 120?", ["El cambio es el valor final menos el inicial.", "98 − 88 = 10."], "Subió 10 mg/dL respecto del valor basal"),
  ],
  mistakes=[
      ("Decir que el máximo es el último dato de la tabla.", "El máximo es el valor mayor, que puede estar en cualquier momento.", "Compara todos los datos antes de elegir."),
      ("Concluir sobre la salud de una persona con una sola medición.", "Un valor aislado no basta; hacen falta varias mediciones y un profesional de la salud.", "Describe los datos sin diagnosticar."),
  ],
  rec=[
      ("¿Cómo se llama el valor de glicemia antes de comer?", "Valor basal", "Es el valor inicial de la curva."),
      ("Datos de ejemplo: 0 min: 90; 30 min: 135; 60 min: 120. ¿Cuál es el máximo?", "135", "Es el mayor de los tres valores."),
      ("Verdadero o falso: después de comer, la glicemia suele subir y luego volver a bajar.", "Verdadero", "La insulina ayuda a bajarla."),
  ],
  und=[
      ("¿Qué hormona hace bajar la curva de glicemia después del máximo? A) Insulina; B) Glucagón.", "A", "La insulina baja la glicemia alta."),
      ("¿Cómo se calcula el cambio de la glicemia entre dos momentos? A) Valor final menos valor inicial; B) Valor inicial más valor final.", "A", "El cambio es la diferencia entre los dos valores."),
      ("¿Por qué una sola medición no basta para evaluar la regulación de la glicemia?", "Porque la glicemia cambia en el tiempo y se necesitan varias mediciones", "Una curva muestra la evolución."),
  ],
  app=[
      arith("Curva de ejemplo: 0 min, 92 mg/dL; 60 min, 145 mg/dL. ¿Cuántos mg/dL subió la glicemia?", "145-92", "Se resta el valor inicial al valor del minuto 60."),
      ("Datos de ejemplo: 0 min: 84; 30 min: 110; 60 min: 129; 90 min: 117; 120 min: 96. ¿En qué minuto está el máximo?", "60", "El mayor valor es 129 y aparece a los 60 minutos."),
      arith("Dos personas de ejemplo tienen valor basal 90 y 86 mg/dL, y máximos de 140 y 128 mg/dL. ¿Cuántos mg/dL más subió la primera que la segunda?", "(140-90)-(128-86)", "Se calcula cuánto subió cada una y se restan."),
  ],
  rea=[
      ("La persona A alcanza su máximo a los 30 minutos y vuelve a su basal a los 90; la persona B alcanza su máximo a los 30 minutos y sigue elevada a los 150. ¿Qué se puede afirmar con prudencia? A) A volvió antes a su valor basal que B; B) B tiene un diagnóstico seguro.", "A", "Se compara el tiempo de regreso; los datos no permiten diagnosticar."),
      ("Un compañero dice: «La glicemia no sube después de comer». Los datos de ejemplo muestran 88 mg/dL antes y 126 mg/dL después. ¿Qué le responderías? A) Los datos muestran un aumento de 38 mg/dL; B) Tiene razón, porque 126 es un número normal.", "A", "126 menos 88 muestra que subió."),
  ],
  cha=[
      ("Dos desayunos de ejemplo: el desayuno P produce un máximo de 150 mg/dL a los 40 minutos y el Q un máximo de 125 mg/dL a los 40 minutos, con el mismo basal. ¿Qué desayuno produce un aumento menor de la glicemia? A) Q; B) P.", "A", "Con el mismo basal, el máximo menor implica un aumento menor."),
      ("Para comparar dos desayunos, ¿qué debe quedar igual? A) La persona, la hora y la cantidad de comida; B) El tipo de alimento.", "A", "Solo debe cambiar la variable estudiada."),
  ],
  context=[arith("Un registro de ejemplo de una estudiante dice: antes del desayuno 87 mg/dL, a la hora 133 mg/dL y a las dos horas 101 mg/dL. ¿Cuántos mg/dL bajó entre la hora y las dos horas?", "133-101", "Se resta el valor posterior al valor del máximo.")],
  selfcheck=[("¿Qué es el valor basal?", "El valor de glicemia antes de comer", "Es el punto de partida de la curva."), ("¿Cómo se calcula el cambio entre dos momentos?", "Valor final menos valor inicial", "Muestra cuánto subió o bajó."), ("¿Qué hormona baja la glicemia alta?", "La insulina", "Se libera cuando la glicemia sube.")],
  open_task=task("Curva de ejemplo (minuto: mg/dL): 0: 90; 30: 138; 60: 150; 90: 124; 120: 99. Identifica el valor basal, el máximo y el momento del máximo; calcula cuánto bajó entre el máximo y el minuto 120; y escribe una conclusión de dos oraciones con un límite.", "Basal 90; máximo 150 a los 60 minutos; bajó 51 mg/dL (150 − 99). La glicemia subió tras la comida y volvió cerca de su valor inicial gracias a la insulina. Son datos de ejemplo de una sola persona, por lo que no sirven para diagnosticar.", ["identifica basal, máximo y momento", "calcula 51 correctamente", "declara un límite"], ["tres datos, un cálculo y dos oraciones"], ["tomar el último valor como máximo", "diagnosticar con una curva"], "Pregunta cuántas curvas más compararías."),
  reinforce="Dibuja una curva de glicemia con basal, máximo y regreso al basal, y rotula los tres puntos.",
  extend="Explica por qué el máximo y el tiempo de regreso al valor basal sirven para comparar dos curvas.")

L(OA2, 3,
  materials="Este cuaderno y lápiz. Para el modelo, una hoja de papel con flechas dibujadas.",
  use="Aprenderé el modelo de retroalimentación negativa que regula la glicemia con insulina y glucagón, y cómo se interpreta la diabetes con ese modelo. Sirve para explicar por qué el cuerpo mantiene estable un valor.",
  prior=["Sé qué hacen la insulina y el glucagón.", "Sé leer una curva de glicemia."],
  explain=[
      "La retroalimentación negativa es un mecanismo en que el cambio de una variable activa una respuesta que lo revierte. Si la glicemia sube, las células beta del páncreas liberan insulina; la glicemia baja y la liberación de insulina disminuye. Si la glicemia baja, las células alfa liberan glucagón; la glicemia sube y se libera menos glucagón. Así la variable oscila alrededor de un valor.",
      "El modelo se representa con un esquema: variable (glicemia), sensor (células del páncreas que detectan la glucosa), efectores (hígado, músculo y otras células) y respuesta (la glicemia vuelve al rango). Como todo modelo, simplifica: en el cuerpo participan más hormonas y órganos.",
      "La diabetes es una condición en que la regulación falla y la glicemia queda elevada. En la diabetes tipo 1, el páncreas produce muy poca insulina. En la diabetes tipo 2, las células responden menos a la insulina. Su control y tratamiento los define un equipo de salud; no se resuelve con modelos ni con consejos de internet.",
  ],
  vocab=[("retroalimentación negativa", "mecanismo en que una respuesta revierte el cambio que la provocó"), ("célula beta", "célula del páncreas que libera insulina"), ("célula alfa", "célula del páncreas que libera glucagón"), ("diabetes", "condición en que la regulación de la glicemia falla y queda elevada"), ("rango de referencia", "intervalo de valores habituales")],
  worked=[
      ("Aplicar el modelo", "La glicemia sube por encima del rango. Describe la cadena de retroalimentación.", ["Las células beta detectan la glicemia alta.", "Liberan insulina.", "Las células y el hígado toman glucosa y la glicemia baja."], "Glicemia alta, insulina, glicemia baja: retroalimentación negativa"),
      ("Interpretar una falla", "Una persona de ejemplo tiene un páncreas que produce muy poca insulina. ¿Qué pasa con su glicemia tras comer?", ["Sin insulina suficiente, las células no toman glucosa.", "La glucosa se queda en la sangre."], "La glicemia queda elevada"),
  ],
  mistakes=[
      ("Pensar que la retroalimentación negativa significa que algo «malo» ocurre.", "«Negativa» indica que la respuesta revierte el cambio, no que sea dañina.", "Piensa en un termostato que corrige la temperatura."),
      ("Creer que la diabetes se explica solo por comer mucha azúcar.", "La diabetes implica una falla en la insulina o en la respuesta a ella; la alimentación influye, pero no es la única causa.", "Explica la falla con el modelo y deriva el tratamiento a profesionales."),
  ],
  rec=[
      ("¿Qué célula del páncreas libera insulina?", "La célula beta", "Responde a la glicemia alta."),
      ("¿Qué célula libera glucagón?", "La célula alfa", "Responde a la glicemia baja."),
      ("Verdadero o falso: en la retroalimentación negativa, la respuesta revierte el cambio que la provocó.", "Verdadero", "Por eso la variable se mantiene estable."),
  ],
  und=[
      ("Si la glicemia baja, ¿cuál es la cadena correcta? A) Células alfa, glucagón, el hígado libera glucosa, la glicemia sube; B) Células beta, insulina, la glicemia baja más.", "A", "El glucagón revierte la baja."),
      ("¿Qué diferencia a la diabetes tipo 1 de la tipo 2 según el modelo? A) En la tipo 1 hay poca insulina y en la tipo 2 las células responden menos a ella; B) En la tipo 2 no se produce nada de insulina y en la tipo 1 las células responden menos.", "A", "Ambas elevan la glicemia por fallas distintas."),
      ("En el modelo, ¿qué representa el sensor?", "Las células del páncreas que detectan la glucosa", "Son las que perciben el cambio de glicemia."),
  ],
  app=[
      ("Una persona de ejemplo hace ejercicio y su glicemia baja bastante. ¿Qué hormona es más probable que aumente? A) Glucagón; B) Insulina.", "A", "Con glicemia baja se libera glucagón."),
      arith("En un modelo de ejemplo, la glicemia sube de 90 a 130 mg/dL y luego la insulina la baja 35 mg/dL. ¿Cuánto marca ahora?", "130-35", "Se resta la bajada al valor máximo."),
      ("Una persona tiene glicemia alta tras comer pese a que su páncreas libera insulina normal. ¿Qué falla podría explicarlo? A) Sus células responden poco a la insulina; B) Su hígado libera demasiado glucagón al comer.", "A", "Es el patrón de la diabetes tipo 2 en el modelo."),
  ],
  rea=[
      ("Un compañero dice: «El modelo de retroalimentación explica toda la regulación de la glicemia». ¿Qué límite tiene? A) En el cuerpo participan más hormonas y órganos que en el modelo; B) Ninguno, porque el modelo incluye todas las hormonas y órganos.", "A", "Un modelo simplifica la realidad."),
      ("Un video dice: «Con este jugo se cura la diabetes». ¿Qué conviene hacer? A) Desconfiar y consultar al equipo de salud; B) Dejar el tratamiento y probar el jugo.", "A", "El control de la diabetes lo define un equipo de salud."),
  ],
  cha=[
      ("Si un tumor del páncreas liberara insulina sin control, ¿qué le pasaría a la glicemia? A) Bajaría demasiado; B) Subiría demasiado.", "A", "Más insulina baja la glicemia."),
      ("¿Por qué la retroalimentación negativa mantiene la glicemia en un rango y no en un valor exacto? A) Porque la respuesta se activa después de que el cambio ocurre; B) Porque el páncreas libera insulina siempre en la misma cantidad.", "A", "La respuesta corrige un cambio ya iniciado, por eso hay oscilaciones."),
  ],
  context=[("Una persona de ejemplo salta una comida y siente mareo leve. ¿Qué hormona del páncreas está actuando probablemente para subir su glicemia?", "El glucagón", "Con ayuno la glicemia baja y se libera glucagón.")],
  selfcheck=[("¿Qué es una retroalimentación negativa?", "Un mecanismo en que la respuesta revierte el cambio que la provocó", "Mantiene la variable estable."), ("¿Qué falla en la diabetes tipo 1?", "El páncreas produce muy poca insulina", "En la tipo 2 las células responden menos."), ("¿Quién define el tratamiento de la diabetes?", "Un equipo de salud", "No los modelos ni consejos de internet.")],
  open_task=task("Dibuja un esquema de retroalimentación negativa para la glicemia después de comer. Incluye: glicemia alta, células beta, insulina, células y hígado, glicemia baja. Escribe debajo dos oraciones: una que explique por qué es negativa y otra que declare un límite del modelo.", "Glicemia alta → células beta → insulina → células y hígado toman glucosa → glicemia baja. Es negativa porque la respuesta revierte el cambio. El modelo solo muestra una hormona, pero en el cuerpo participan más hormonas y órganos.", ["incluye las cinco etapas en orden", "explica por qué es negativa", "declara un límite del modelo"], ["esquema y dos oraciones"], ["omitir la insulina", "decir que sube la glicemia al final"], "Pregunta cómo se dibujaría el caso de glicemia baja."),
  reinforce="Dibuja el mismo esquema para el caso de glicemia baja y glucagón.",
  extend="Explica por qué el esquema de retroalimentación negativa también sirve para entender un termostato.")

L(OA2, 4,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé qué hormonas sexuales producen los testículos y los ovarios, cómo las controla el cerebro y qué cambios producen en la pubertad. Sirve para explicar los caracteres sexuales y las funciones reproductivas.",
  prior=["Sé qué es una hormona y qué es una glándula.", "Sé que la retroalimentación negativa mantiene estable una variable."],
  explain=[
      "Las hormonas sexuales se producen en las gónadas: los testículos producen testosterona y los ovarios producen estrógenos y progesterona. Están controladas por el cerebro: el hipotálamo libera una hormona que estimula la hipófisis, y esta libera FSH y LH, que actúan sobre las gónadas. Es una cadena de control con retroalimentación negativa.",
      "En la pubertad aumentan las hormonas sexuales y aparecen los caracteres sexuales secundarios. Con testosterona: vello facial y corporal, voz más grave y mayor masa muscular. Con estrógenos: desarrollo de las mamas y ensanchamiento de las caderas. Los caracteres sexuales primarios son los órganos reproductores, que ya existen desde el nacimiento.",
      "Las hormonas también regulan las funciones reproductivas: la producción de espermatozoides en los testículos y la maduración de óvulos en los ovarios. Todas las personas producen testosterona y estrógenos, pero en distinta cantidad. El inicio de la pubertad varía entre personas, y esa variación es normal. Dudas sobre el desarrollo se conversan con una persona adulta de confianza o con un profesional de salud.",
  ],
  vocab=[("gónada", "órgano que produce gametos y hormonas sexuales"), ("testosterona", "hormona sexual producida en los testículos"), ("estrógenos", "hormonas sexuales producidas principalmente en los ovarios"), ("hipófisis", "glándula del encéfalo que libera FSH y LH"), ("carácter sexual secundario", "rasgo que aparece en la pubertad por acción hormonal")],
  worked=[
      ("Seguir la cadena de control", "El hipotálamo estimula a la hipófisis. ¿Qué hace la hipófisis y qué órgano responde?", ["La hipófisis libera FSH y LH a la sangre.", "Las gónadas (testículos u ovarios) responden produciendo hormonas sexuales y gametos."], "La hipófisis libera FSH y LH; responden las gónadas"),
      ("Clasificar un carácter", "El cambio de voz a un tono más grave durante la adolescencia, ¿es un carácter sexual primario o secundario?", ["Aparece en la pubertad.", "No es un órgano reproductor."], "Secundario"),
  ],
  mistakes=[
      ("Creer que solo los hombres tienen testosterona y solo las mujeres estrógenos.", "Ambas hormonas existen en todas las personas, en distinta cantidad.", "Habla de «mayor cantidad» y no de «exclusiva»."),
      ("Pensar que cualquier cambio fuera del promedio de edad indica un problema.", "El inicio de la pubertad varía mucho entre personas.", "Si hay dudas, conversa con un adulto de confianza o un profesional de salud."),
  ],
  rec=[
      ("¿Qué hormona sexual se produce en los testículos?", "Testosterona", "Es la principal hormona sexual masculina."),
      ("¿Qué glándula del encéfalo libera FSH y LH?", "La hipófisis", "Controla la actividad de las gónadas."),
      ("Verdadero o falso: los caracteres sexuales secundarios aparecen en la pubertad.", "Verdadero", "Los provocan las hormonas sexuales."),
  ],
  und=[
      ("¿Qué órgano responde a la FSH y la LH? A) Las gónadas; B) El páncreas.", "A", "Las gónadas producen gametos y hormonas sexuales."),
      ("¿Cuál es un carácter sexual secundario? A) Desarrollo de las mamas; B) Presencia de ovarios.", "A", "Los ovarios son un carácter primario."),
      ("¿Qué mecanismo permite mantener estable la cantidad de hormona sexual?", "Retroalimentación negativa", "La hormona alta frena la señal de la hipófisis."),
  ],
  app=[
      ("En la pubertad, una persona de ejemplo nota que su voz se vuelve más grave y aparece vello facial. ¿Qué hormona aumentó? A) Testosterona; B) Insulina.", "A", "Estos cambios los provoca la testosterona."),
      ("Una persona de ejemplo tiene testosterona baja en la sangre y la hipófisis libera mucha FSH y LH. ¿Cómo se explica con la retroalimentación negativa? A) Con poca hormona sexual no hay freno sobre la hipófisis; B) La hormona sexual baja estimula a la hipófisis a liberar menos.", "A", "La hormona sexual alta frena a la hipófisis; si está baja, el freno falta y se libera más FSH y LH."),
      ("Una persona de ejemplo no tiene los niveles de LH que se esperan; ¿qué órgano recibiría menos estímulo? A) Las gónadas; B) El páncreas.", "A", "La LH actúa sobre las gónadas."),
  ],
  rea=[
      ("Un compañero dice: «La pubertad tiene que empezar a la misma edad en todos». ¿Qué le respondes? A) Es variable entre personas; si hay dudas, se conversa con un adulto de confianza o un profesional; B) Tiene razón.", "A", "El inicio de la pubertad varía."),
      ("Si la hormona sexual está alta en la sangre, ¿qué esperarías en la hipófisis? A) Menos liberación de FSH y LH; B) Más liberación de FSH y LH.", "A", "En la retroalimentación negativa, la hormona alta frena la señal."),
  ],
  cha=[
      ("Una persona con tratamiento médico recibe una hormona sexual desde afuera. ¿Qué podría pasar con la liberación de FSH y LH por retroalimentación negativa? A) Disminuiría; B) Aumentaría.", "A", "El nivel alto de hormona frena a la hipófisis."),
      ("¿Por qué hablar de «hormonas masculinas» y «hormonas femeninas» simplifica demasiado? A) Porque todas las personas producen ambas, en distinta cantidad; B) Porque solo los hombres producen testosterona y solo las mujeres producen estrógenos.", "A", "Es una simplificación frecuente."),
  ],
  context=[("Una persona de 14 años se pregunta por qué sus compañeros han crecido más. ¿A quién podría conversar sus dudas?", "A una persona adulta de confianza o a un profesional de salud", "El ritmo de la pubertad varía y las dudas se resuelven con apoyo.")],
  selfcheck=[("¿Qué glándula controla a las gónadas?", "La hipófisis", "Libera FSH y LH."), ("Nombra un carácter sexual secundario.", "Voz más grave, vello o desarrollo de mamas", "Aparecen por acción hormonal en la pubertad."), ("¿Qué ocurre si hay mucha hormona sexual en la sangre?", "La hipófisis libera menos FSH y LH", "Es retroalimentación negativa.")],
  open_task=task("Esquema: escribe la cadena de control hormonal desde el hipotálamo hasta las gónadas y de vuelta (con la retroalimentación negativa). Después elige dos caracteres sexuales secundarios y escribe qué hormona los provoca. Finalmente, escribe a quién conversarías una duda sobre tu desarrollo.", "Hipotálamo → hipófisis → FSH y LH → gónadas → hormonas sexuales → se frena la hipófisis. Voz más grave: testosterona; desarrollo de mamas: estrógenos. Conversaría con una persona adulta de confianza o con un profesional de salud.", ["la cadena está en orden", "relaciona dos caracteres con su hormona", "nombra a una persona de apoyo"], ["cadena, dos relaciones y una persona de apoyo"], ["omitir la retroalimentación", "decir que cada hormona es exclusiva de un sexo"], "Pregunta qué pasaría si falla la hipófisis."),
  reinforce="Escribe tres caracteres sexuales secundarios y la hormona que los provoca.",
  extend="Explica por qué las dudas sobre la pubertad deben conversarse con un adulto de confianza.")

L(OA2, 5,
  materials="Este cuaderno y lápiz. Los datos del ciclo están escritos en los ejercicios; son de ejemplo.",
  use="Aprenderé cómo las hormonas regulan el ciclo menstrual y la producción de espermatozoides, y cómo leer una curva hormonal. Sirve para explicar cómo el cuerpo coordina las funciones reproductivas.",
  prior=["Sé qué son la hipófisis, las gónadas y la retroalimentación negativa.", "Sé leer una curva en el tiempo."],
  explain=[
      "El ciclo menstrual es una secuencia de cambios en los ovarios y el útero que se repite, en promedio, cada 28 días, aunque varía entre personas. En la primera fase, la FSH hace madurar un folículo en el ovario, que libera estrógenos. Los estrógenos engrosan el endometrio, que es la pared interna del útero. Hacia la mitad del ciclo, un pico de LH provoca la ovulación: el folículo libera un óvulo.",
      "Después de la ovulación, el folículo vacío forma el cuerpo lúteo, que libera progesterona. Esta mantiene el endometrio listo para recibir un embrión. Si no hay fecundación, el cuerpo lúteo se degrada, bajan la progesterona y los estrógenos, y el endometrio se desprende: es la menstruación.",
      "En los testículos, la FSH y la testosterona estimulan la producción continua de espermatozoides. A diferencia del ciclo femenino, no hay un ciclo mensual: la producción es constante. En ambos casos opera la retroalimentación: las hormonas sexuales regulan a la hipófisis.",
  ],
  vocab=[("ciclo menstrual", "secuencia repetida de cambios en ovarios y útero"), ("folículo", "estructura del ovario donde madura un óvulo"), ("ovulación", "liberación del óvulo desde el ovario"), ("endometrio", "pared interna del útero"), ("progesterona", "hormona que mantiene el endometrio")],
  worked=[
      ("Ordenar el ciclo", "Ordena: ovulación, maduración del folículo, menstruación, formación del cuerpo lúteo.", ["Primero madura el folículo por la FSH.", "Luego ocurre la ovulación por el pico de LH.", "Después se forma el cuerpo lúteo.", "Si no hay fecundación, viene la menstruación."], "Maduración del folículo, ovulación, cuerpo lúteo, menstruación"),
      ("Leer un dato", "En un ciclo de ejemplo de 28 días, la ovulación ocurre el día 14. ¿Cuántos días pasan desde la ovulación hasta el final del ciclo?", ["Identifico los datos: el ciclo dura 28 días y la ovulación ocurre el día 14.", "Resto: 28 − 14 = 14."], "14 días"),
  ],
  mistakes=[
      ("Creer que el ciclo dura siempre exactamente 28 días.", "28 días es un promedio; el ciclo varía entre personas y de un mes a otro.", "Usa la expresión «en promedio»."),
      ("Confundir la ovulación con la menstruación.", "La ovulación es la liberación del óvulo; la menstruación es el desprendimiento del endometrio.", "Asocia ovulación con el ovario y menstruación con el útero."),
  ],
  rec=[
      ("¿Qué hormona provoca la ovulación a mitad del ciclo?", "La LH", "Su pico desencadena la liberación del óvulo."),
      ("¿Cómo se llama la pared interna del útero?", "Endometrio", "Se engrosa durante el ciclo."),
      ("Verdadero o falso: la menstruación ocurre si no hay fecundación.", "Verdadero", "Bajan las hormonas y el endometrio se desprende."),
  ],
  und=[
      ("¿Qué produce el cuerpo lúteo? A) Progesterona; B) Insulina.", "A", "La progesterona mantiene el endometrio."),
      ("¿Qué hormona estimula la maduración del folículo? A) FSH; B) Progesterona.", "A", "La FSH inicia la maduración del folículo."),
      ("La formación de espermatozoides en los testículos, ¿es cíclica como el ciclo menstrual o continua?", "Continua", "La FSH y la testosterona la estimulan de manera constante."),
  ],
  app=[
      arith("En un ciclo de ejemplo de 30 días, la ovulación ocurre el día 16 y la menstruación siguiente comienza el día 31. ¿Cuántos días pasan desde la ovulación hasta el último día del ciclo, sin contar el día 16?", "30-16", "Se restan al largo del ciclo los días hasta la ovulación."),
      ("Curva de ejemplo: los estrógenos suben durante los primeros 12 días y luego hay un pico de LH. ¿Qué evento sigue al pico de LH? A) La ovulación; B) La menstruación.", "A", "El pico de LH desencadena la ovulación."),
      ("Un ciclo de ejemplo dura 26 días y otro 31 días. ¿Cuántos días más dura el segundo? Responde con el número.", "5", "31 menos 26 da la diferencia."),
  ],
  rea=[
      ("Un compañero dice: «Si el ciclo dura 31 días, algo está mal». ¿Qué le respondes? A) El ciclo varía entre personas; solo un profesional puede evaluar si hay un problema; B) Tiene razón, el ciclo siempre dura 28.", "A", "28 es un promedio; la variación es normal."),
      ("¿Por qué bajan la progesterona y los estrógenos si no hay fecundación? A) Porque el cuerpo lúteo se degrada; B) Porque el óvulo se degrada.", "A", "Sin embrión, el cuerpo lúteo deja de producir hormonas."),
  ],
  cha=[
      ("Si una persona recibe progesterona desde afuera durante todo el ciclo, ¿qué efecto tendría en la retroalimentación? A) Frenaría la liberación de FSH y LH; B) La aumentaría.", "A", "Mucha hormona frena a la hipófisis por retroalimentación negativa."),
      ("¿Por qué la producción de espermatozoides no es cíclica? A) Porque la FSH y la testosterona estimulan de manera continua los testículos; B) Porque los testículos solo funcionan una semana al mes.", "A", "Hay un estímulo hormonal constante."),
  ],
  context=[arith("En un ciclo de ejemplo de 29 días, la menstruación dura 5 días. ¿Cuántos días del ciclo no corresponden a menstruación?", "29-5", "Se restan los días de menstruación a los del ciclo.")],
  selfcheck=[("¿Qué provoca la ovulación?", "El pico de LH", "Libera un óvulo del folículo."), ("¿Qué hormona mantiene el endometrio después de la ovulación?", "La progesterona", "La libera el cuerpo lúteo."), ("¿Por qué el ciclo no dura siempre 28 días?", "Porque 28 es un promedio y varía entre personas", "La variación es normal.")],
  open_task=task("Con un ciclo de ejemplo de 28 días: día 1, comienza la menstruación; días 1 a 13, madura el folículo; día 14, ovulación; días 15 a 28, actúa el cuerpo lúteo. Dibuja una línea de tiempo con estos hitos y rotula en cada tramo la hormona principal (FSH y estrógenos, LH, progesterona). Escribe una oración que explique por qué baja la progesterona si no hay fecundación y otra que diga un límite del modelo.", "Días 1–13: FSH y estrógenos; día 14: pico de LH; días 15–28: progesterona. Si no hay fecundación, el cuerpo lúteo se degrada y baja la progesterona. Es un modelo promedio: cada ciclo real puede ser más corto o más largo.", ["la línea de tiempo está en orden", "asocia cada tramo con su hormona", "declara un límite"], ["línea de tiempo y dos oraciones"], ["fijar el ciclo en 28 días para todas las personas", "invertir ovulación y menstruación"], "Pregunta qué cambiaría en un ciclo de 32 días."),
  reinforce="Escribe en orden cuatro eventos del ciclo menstrual y la hormona de cada uno.",
  extend="Explica por qué el ciclo menstrual es un ejemplo de regulación hormonal con retroalimentación.")

"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 09 (ondas: energía, propiedades y clasificación) y OA 10 (sonido, modelo ondulatorio y aplicaciones)."""
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


OA9 = "CN1M OA 09"
OA10 = "CN1M OA 10"

# ---------------------------------------------------------------- OA 09

L(OA9, 1,
  materials="Una cuerda larga o un cordón de zapatilla, una fuente o recipiente con agua y un corcho o tapa plástica pequeña. Si no tienes, usa las descripciones de los ejercicios.",
  use="Aprenderé que una onda transmite energía sin transportar materia de un lugar a otro, y a escribir preguntas investigables con experimentos seguros. Sirve para entender luz, sonido y olas.",
  prior=["Sé que la energía puede pasar de un lugar a otro.", "Sé que una pregunta investigable se contesta midiendo."],
  explain=[
      "Una onda es una perturbación que se propaga y transporta energía de un lugar a otro. El medio por el que viaja, como una cuerda o el agua, sube y baja o se mueve de un lado a otro, pero no avanza con la onda. Si pones un corcho en el agua y pasa una ola, el corcho sube y baja casi en el mismo lugar, mientras que la energía de la ola sigue avanzando.",
      "Una cuerda estirada permite ver un pulso: si la sacudes una vez, una joroba recorre la cuerda y llega al otro extremo, pero el cordón no se va. Mientras más energía pones al sacudir, más grande es la joroba. Por eso, una ola grande puede mover objetos pesados: transporta más energía.",
      "Una pregunta investigable sobre ondas indica qué se mide. «¿Cuántos segundos tarda un pulso en recorrer una cuerda de 4 metros?» se contesta con un cronómetro. «¿Es bonita una ola?» no, porque depende de opiniones. En los experimentos, se usan materiales seguros: cuerdas, agua en una fuente y objetos livianos; sin electricidad de red ni objetos que puedan lastimar.",
  ],
  vocab=[("onda", "perturbación que se propaga y transporta energía"), ("medio", "material por el que viaja una onda"), ("pulso", "una sola perturbación que recorre un medio"), ("cresta", "punto más alto de una onda"), ("energía", "capacidad de producir cambios")],
  worked=[
      ("Qué se transporta", "Un corcho flota en una fuente. Pasa una ola y el corcho sube y baja. ¿Qué viaja con la ola: el agua o la energía?", ["Veo que el corcho queda casi en su lugar.", "Lo que avanza es la perturbación con su energía."], "La energía"),
      ("Mejorar una pregunta", "Mejora «¿Es linda una ola en la cuerda?» para que se pueda investigar.", ["Quito la palabra de opinión.", "Indico qué se mide: el tiempo que tarda un pulso en recorrer una cuerda de 4 metros.", "Queda: «¿Cuántos segundos tarda un pulso en recorrer 4 metros de cuerda?»"], "«¿Cuántos segundos tarda un pulso en recorrer 4 metros de cuerda?»"),
  ],
  mistakes=[
      ("Pensar que el agua de una ola viaja hasta la orilla con ella.", "El agua sube y baja y es la energía la que avanza.", "Observa un corcho: queda casi en el mismo lugar."),
      ("Creer que una onda transporta materia de un extremo a otro.", "Transporta energía y la materia solo oscila.", "Di «energía» y no «materia» al explicar."),
  ],
  rec=[
      ("¿Qué transporta una onda de un lugar a otro?", "Energía", "La materia solo oscila."),
      ("Completa: el punto más alto de una onda se llama ______ (cresta o valle).", "Cresta", "El valle es el punto más bajo."),
      ("Verdadero o falso: el medio avanza junto con la onda.", "Falso", "Solo oscila alrededor de su posición."),
  ],
  und=[
      ("Un corcho sube y baja al pasar una ola. ¿Qué indica esto? A) Que el agua no viaja con la ola, sino que oscila; B) Que el corcho es más liviano que el aire.", "A", "El corcho muestra el movimiento del medio."),
      ("¿Por qué una ola grande mueve objetos pesados? A) Porque transporta más energía; B) Porque el agua de la ola viaja más lejos que la de una ola chica.", "A", "A mayor energía, mayor efecto."),
      ("¿Qué es un pulso?", "Una sola perturbación que recorre un medio", "Es una onda corta y única."),
  ],
  app=[
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos segundos tarda un pulso en recorrer una cuerda de 5 metros?; B) ¿Es divertido sacudir una cuerda?", "A", "Se contesta con un cronómetro."),
      arith("Un pulso de ejemplo recorre 6 metros de cuerda en 3 segundos. ¿Cuántos metros avanza por segundo?", "6//3", "Se divide la distancia entre el tiempo.", " m/s"),
      ("En un recipiente con agua se deja caer una gota y se forman círculos que se alejan del centro. Un trozo de papel flotando en el agua, ¿qué hace? A) Sube y baja casi en el mismo lugar; B) Es llevado hasta el borde.", "A", "El medio solo oscila y la energía se aleja."),
  ],
  rea=[
      ("Un compañero dice: «Una onda en una cuerda lleva un trozo de cuerda de un extremo al otro». ¿Qué evidencia lo contradice? A) Una marca en la cuerda solo sube y baja y vuelve a su lugar; B) La cuerda no se mueve.", "A", "La marca muestra que el medio no se traslada."),
      ("Dos pulsos en la misma cuerda: el A se produce con una sacudida pequeña y el B con una sacudida grande. ¿Cuál transporta más energía? A) El B; B) El A.", "A", "Una sacudida más grande entrega más energía."),
  ],
  cha=[
      ("Un grupo de ejemplo midió el tiempo de un pulso en una cuerda de 8 metros en 4 intentos: 2, 2, 3 y 1 segundos. ¿Cuál es el promedio de tiempo?", "2", "La suma es 8 y 8 dividido por 4 es 2 segundos."),
      ("Un estudiante propone medir ondas usando un enchufe de la casa y un cable pelado. ¿Qué respondes? A) No es seguro; se usa una cuerda y una fuente con agua, sin electricidad de red; B) Es seguro si se hace rápido.", "A", "Los experimentos deben ser seguros."),
  ],
  context=[arith("En una playa de ejemplo llegan 12 olas por minuto. ¿Cuántas llegan en 5 minutos?", "12*5", "Se multiplica el ritmo por los minutos.")],
  selfcheck=[("¿Qué transporta una onda?", "Energía", "No transporta materia."), ("¿Qué le pasa al medio cuando pasa una onda?", "Oscila y vuelve a su lugar", "No avanza con la onda."), ("¿Qué hace investigable a una pregunta sobre ondas?", "Que indica qué se mide", "Por ejemplo, un tiempo o una distancia.")],
  open_task=task("Con una cuerda o cordón de 3 metros, amárralo a una silla y sacúdelo una vez para formar un pulso. Anota (a) qué le pasa a una marca hecha con cinta en el medio y (b) cuántas veces sube y baja la marca en 10 segundos cuando sacudes la cuerda con ritmo regular, con un cronómetro de teléfono, en tres intentos. Si no tienes cuerda, usa estos datos de ejemplo: 8, 9 y 10 veces. Escribe una conclusión de dos oraciones sobre qué se transportó y qué no.", "La marca sube y baja y vuelve a su lugar. Conteos: 8, 9 y 10 veces en 10 segundos, promedio 9 veces. Se transportó energía y no la cuerda.", ["describe el movimiento de la marca", "registra tres conteos", "distingue energía de materia"], ["tabla de tres conteos y conclusión"], ["decir que la cuerda viaja", "no repetir las medidas"], "Pregunta qué cambiaría si sacudes más fuerte."),
  reinforce="Explica con un corcho en el agua qué viaja y qué no cuando pasa una ola.",
  extend="Explica por qué las olas del mar pueden dañar un muelle aunque el agua no viaje con ellas.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Los gráficos de ondas están descritos con medidas en los ejercicios.",
  use="Aprenderé a medir las características de una onda: amplitud, longitud de onda, frecuencia, período y rapidez. Sirve para leer gráficos y comparar ondas.",
  prior=["Sé que una onda transporta energía.", "Sé medir distancias y tiempos."],
  explain=[
      "La amplitud es la altura máxima de la onda medida desde la posición de equilibrio hasta una cresta. A mayor amplitud, mayor energía. La longitud de onda (λ) es la distancia entre dos crestas seguidas, y se mide en metros. La frecuencia (f) es el número de oscilaciones por segundo; se mide en hercios (Hz): 1 Hz es una oscilación por segundo.",
      "El período (T) es el tiempo de una oscilación completa; cuanto mayor es la frecuencia, menor es el período. La rapidez de propagación (v) es la distancia que recorre la onda en un segundo y depende del medio. Se calcula con v = λ × f. Por ejemplo, si λ = 2 m y f = 3 Hz, v = 6 m/s.",
      "Para leer un gráfico, se identifican las crestas y valles y se miden las distancias entre ellos. Una onda de la misma amplitud pero mayor frecuencia tiene más crestas en el mismo espacio. Las mediciones tienen incertidumbre porque se leen con regla, por eso conviene repetir y promediar.",
  ],
  vocab=[("amplitud", "altura máxima de la onda desde el equilibrio"), ("longitud de onda", "distancia entre dos crestas seguidas"), ("frecuencia", "número de oscilaciones por segundo, en hercios"), ("período", "tiempo de una oscilación completa"), ("rapidez de propagación", "distancia que recorre la onda por segundo")],
  worked=[
      ("Leer la longitud de onda", "En una cuerda, una cresta está a 0 cm y la siguiente a 60 cm. ¿Cuál es la longitud de onda?", ["Mido la distancia entre dos crestas seguidas.", "60 menos 0 es 60."], "60 cm"),
      ("Calcular la rapidez", "Una onda tiene λ = 4 m y f = 5 Hz. ¿Cuál es su rapidez?", ["Uso v = λ × f.", "4 por 5 es 20."], "20 m/s"),
  ],
  mistakes=[
      ("Medir la longitud de onda desde una cresta hasta un valle.", "Esa es solo media longitud de onda.", "Mide de cresta a cresta."),
      ("Confundir amplitud con longitud de onda.", "La amplitud es altura y la longitud es una distancia horizontal.", "Pregunta si mides hacia arriba o a lo largo."),
  ],
  rec=[
      ("¿En qué unidad se mide la frecuencia?", "Hercios (Hz)", "Un hercio es una oscilación por segundo."),
      ("Completa: la distancia entre dos crestas seguidas es la ______ (longitud de onda o amplitud).", "Longitud de onda", "Se mide en metros."),
      ("Verdadero o falso: a mayor amplitud, mayor energía.", "Verdadero", "La energía depende de la amplitud."),
  ],
  und=[
      ("¿Qué mide la amplitud? A) La altura máxima desde el equilibrio; B) El tiempo de una oscilación.", "A", "El tiempo corresponde al período."),
      ("Si aumenta la frecuencia, ¿qué pasa con el período? A) Disminuye; B) Aumenta.", "A", "Hay más oscilaciones por segundo y cada una dura menos."),
      ("¿Qué fórmula relaciona rapidez, longitud de onda y frecuencia?", "v = λ × f", "La rapidez es la longitud por la frecuencia."),
  ],
  app=[
      arith("Una onda tiene λ = 3 m y f = 6 Hz. ¿Cuál es su rapidez en m/s?", "3*6", "Se multiplica la longitud de onda por la frecuencia.", " m/s"),
      ("En una cuerda, las crestas están a 10 cm, 45 cm y 80 cm. ¿Cuál es la longitud de onda en cm?", "35", "45 menos 10 es 35 y 80 menos 45 también."),
      arith("Una fuente produce 20 oscilaciones en 10 segundos. ¿Cuál es su frecuencia en Hz?", "20//10", "Se divide el número de oscilaciones entre el tiempo.", " Hz"),
  ],
  rea=[
      ("Dos ondas de ejemplo en agua: la A tiene amplitud de 2 cm y la B de 5 cm; ambas con la misma frecuencia. ¿Cuál transporta más energía? A) La B; B) La A.", "A", "Mayor amplitud significa mayor energía."),
      ("Un estudiante mide de una cresta a un valle 20 cm y dice que λ = 20 cm. ¿Cuál es la corrección? A) λ = 40 cm, porque cresta a valle es media longitud; B) λ = 10 cm.", "A", "Cresta a cresta es el doble de cresta a valle."),
  ],
  cha=[
      arith("Una onda de ejemplo tiene f = 4 Hz y λ = 5 m. ¿Cuántos metros recorre en 3 segundos?", "4*5*3", "Se calcula la rapidez 20 m/s y se multiplica por 3 s.", " m"),
      ("Datos de ejemplo: onda 1, λ = 2 m, f = 9 Hz; onda 2, λ = 6 m, f = 4 Hz. ¿Cuál es más rápida? Responde 1 o 2.", "2", "La onda 1 va a 18 m/s y la 2 a 24 m/s."),
  ],
  context=[arith("En una piscina de ejemplo llega una ola cada 4 segundos. ¿Cuántas olas llegan en 60 segundos?", "60//4", "Se divide el tiempo total entre el tiempo de cada ola.")],
  selfcheck=[("¿Qué mide la longitud de onda?", "La distancia entre dos crestas seguidas", "Se mide en metros."), ("¿Qué mide la frecuencia?", "Las oscilaciones por segundo", "Se mide en hercios."), ("¿Cómo se calcula la rapidez de una onda?", "Multiplicando la longitud de onda por la frecuencia", "v = λ × f.")],
  open_task=task("Con una cuerda o con estos datos de ejemplo, completa una tabla: onda A, λ = 2 m, f = 5 Hz; onda B, λ = 4 m, f = 3 Hz; onda C, λ = 1 m, f = 9 Hz. Calcula la rapidez de cada una, ordénalas de la más rápida a la más lenta y escribe una limitación de las mediciones.", "A: 10 m/s; B: 12 m/s; C: 9 m/s. Orden: B, A y C. Limitación: las medidas con regla tienen incertidumbre.", ["calcula tres rapideces", "ordena correctamente", "declara una limitación"], ["tabla y orden"], ["sumar en vez de multiplicar", "olvidar las unidades"], "Pregunta qué mediría para disminuir la incertidumbre."),
  reinforce="Dibuja una onda y marca la amplitud y la longitud de onda.",
  extend="Explica por qué dos ondas con la misma rapidez pueden tener distinta longitud de onda.")

L(OA9, 3,
  materials="Este cuaderno y lápiz. Los ejemplos de ondas están descritos en los ejercicios.",
  use="Aprenderé a clasificar las ondas en mecánicas y electromagnéticas, y en transversales, longitudinales y superficiales. Sirve para organizar los tipos de ondas con un modelo.",
  prior=["Sé qué son la amplitud y la longitud de onda.", "Sé que una onda transporta energía."],
  explain=[
      "Según el medio, hay dos grandes grupos. Las ondas mecánicas necesitan un medio material para propagarse, como el sonido en el aire o las olas en el agua. Las ondas electromagnéticas no necesitan medio y pueden viajar por el vacío; son la luz, las ondas de radio y los rayos X. En el vacío viajan a unos 300.000 km por segundo.",
      "Según la dirección de la oscilación, hay tres tipos. En una onda transversal, el medio oscila perpendicular a la dirección en que avanza la onda: una cuerda sacudida hacia arriba y abajo. En una onda longitudinal, oscila en la misma dirección: un resorte comprimido y estirado, o el sonido. Una onda superficial combina ambos movimientos, como las olas del agua.",
      "Un modelo de clasificación es una tabla con las dos entradas. Por ejemplo, el sonido es mecánico y longitudinal; la luz es electromagnética y transversal; la ola es mecánica y superficial. Clasificar ayuda a predecir su comportamiento, aunque algunas ondas reales mezclan características.",
  ],
  vocab=[("onda mecánica", "onda que necesita un medio material"), ("onda electromagnética", "onda que puede viajar por el vacío"), ("onda transversal", "onda donde el medio oscila perpendicular al avance"), ("onda longitudinal", "onda donde el medio oscila en la dirección del avance"), ("onda superficial", "onda que combina ambos movimientos, como las olas")],
  worked=[
      ("Clasificar según el medio", "El sonido no se propaga en el vacío. ¿Es mecánico o electromagnético?", ["Pregunto si necesita un medio material.", "Sí, lo necesita."], "Mecánico"),
      ("Clasificar según la oscilación", "Una cuerda se sacude de arriba hacia abajo y la onda avanza horizontalmente. ¿Qué tipo de onda es?", ["La oscilación es perpendicular al avance.", "Es transversal."], "Transversal"),
  ],
  mistakes=[
      ("Decir que la luz necesita aire para llegar a la Tierra.", "La luz es electromagnética y viaja por el vacío.", "Recuerda que la luz del Sol atraviesa el espacio vacío."),
      ("Decir que el sonido es transversal.", "En el sonido las partículas oscilan en la misma dirección del avance.", "Piensa en un resorte comprimido."),
  ],
  rec=[
      ("¿Qué ondas necesitan un medio material?", "Las ondas mecánicas", "Como el sonido y las olas."),
      ("Completa: la luz es una onda ______ (electromagnética o mecánica).", "Electromagnética", "Viaja por el vacío."),
      ("Verdadero o falso: el sonido es una onda longitudinal.", "Verdadero", "Las partículas oscilan en la dirección de avance."),
  ],
  und=[
      ("¿Por qué las ondas electromagnéticas pueden venir del Sol a la Tierra? A) Porque no necesitan un medio material; B) Porque el espacio está lleno de aire.", "A", "El espacio entre el Sol y la Tierra es casi vacío."),
      ("En una onda transversal, ¿cómo oscila el medio? A) Perpendicular al avance; B) En la misma dirección del avance.", "A", "Esa es la diferencia con la longitudinal."),
      ("¿Qué tipo de onda es una ola del mar?", "Superficial", "Combina ambos movimientos."),
  ],
  app=[
      ("Tabla de ejemplo: sonido, luz, ola, onda de radio. ¿Cuál de ellas es mecánica y longitudinal?", "El sonido", "Necesita medio y sus partículas oscilan en la dirección del avance."),
      ("Con la misma lista (sonido, luz, ola, onda de radio), ¿cuántas son electromagnéticas?", "2", "Son la luz y la onda de radio."),
      arith("La luz recorre 300.000 km en 1 segundo. ¿Cuántos kilómetros recorre en 3 segundos?", "300000*3", "Se multiplica la distancia por segundo por los segundos.", " km"),
  ],
  rea=[
      ("Un compañero dice que, en el espacio vacío, un astronauta no podría oír una explosión pero sí verla. ¿Cuál es la razón? A) El sonido necesita medio y la luz no; B) La luz es longitudinal.", "A", "Una es mecánica y la otra electromagnética."),
      ("Una persona sacude un resorte empujándolo y tirándolo en la misma dirección en que avanza la onda. ¿Qué onda produce? A) Longitudinal; B) Transversal.", "A", "La oscilación es en la dirección del avance."),
  ],
  cha=[
      ("Una tabla de ejemplo tiene 6 ondas: 3 mecánicas transversales, 2 mecánicas longitudinales y 1 electromagnética. ¿Cuántas ondas mecánicas hay?", "5", "Son 3 más 2."),
      ("Un modelo clasifica «la ola del mar» como transversal pura. ¿Cuál es la limitación del modelo? A) Las olas combinan movimientos transversales y longitudinales; B) Las olas no son ondas.", "A", "Por eso se llaman superficiales."),
  ],
  context=[arith("En una feria de ciencias de ejemplo hay 4 experimentos con cuerdas (transversales) y 3 con resortes (longitudinales). ¿Cuántos experimentos hay?", "4+3", "Se suman los experimentos de cada tipo.")],
  selfcheck=[("¿Qué diferencia hay entre mecánicas y electromagnéticas?", "Las mecánicas necesitan un medio y las electromagnéticas no", "El vacío las separa."), ("¿Cómo oscila el medio en una onda longitudinal?", "En la dirección del avance", "Como un resorte comprimido."), ("Clasifica la luz.", "Electromagnética y transversal", "Viaja por el vacío.")],
  open_task=task("Con esta lista de ejemplo, completa una tabla de clasificación (mecánica o electromagnética; transversal, longitudinal o superficial): sonido, luz, onda en una cuerda, ola del mar, onda de radio. Explica con una frase por qué no se pueden oír las explosiones en el espacio.", "Sonido: mecánica, longitudinal. Luz: electromagnética, transversal. Cuerda: mecánica, transversal. Ola: mecánica, superficial. Radio: electromagnética, transversal. En el espacio no hay medio para el sonido.", ["cinco filas correctas", "explica con medio material", "no confunde los tipos"], ["tabla y explicación"], ["clasificar el sonido como transversal", "decir que el sonido viaja por el vacío"], "Pregunta qué otra onda clasificarías con la tabla."),
  reinforce="Escribe un ejemplo de onda mecánica y uno de electromagnética.",
  extend="Explica por qué el modelo de clasificación no describe toda la complejidad de las ondas reales.")

L(OA9, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a relacionar la rapidez, la frecuencia y la longitud de onda mediante v = λ × f y a analizar datos de un experimento con una cuerda. Sirve para predecir cómo cambia una onda.",
  prior=["Sé qué son amplitud, frecuencia y longitud de onda.", "Sé que v = λ × f."],
  explain=[
      "La rapidez de una onda depende del medio, no de la frecuencia. En una cuerda dada, la rapidez es la misma sea que la sacudas rápido o lento. Entonces, si aumenta la frecuencia, la longitud de onda debe disminuir para que v = λ × f siga igual. Eso es una relación inversa entre f y λ cuando v es constante.",
      "Esto se puede comprobar en una tabla de datos. Si una cuerda tiene v = 12 m/s: con f = 2 Hz, λ = 6 m; con f = 3 Hz, λ = 4 m; con f = 6 Hz, λ = 2 m. El producto λ × f es siempre 12. Si el producto cambia, la rapidez cambió o hubo error de medición.",
      "Otro factor es el medio: si la cuerda se tensa más, la rapidez aumenta. En una cuerda más tensa, para la misma frecuencia, la longitud de onda es mayor. Al interpretar datos, es importante controlar variables: cambiar una cosa a la vez y repetir las mediciones para detectar errores.",
  ],
  vocab=[("relación inversa", "cuando una variable aumenta, la otra disminuye"), ("constante", "que no cambia"), ("tensión", "fuerza con que se estira una cuerda"), ("producto", "resultado de multiplicar"), ("error de medición", "diferencia entre lo medido y el valor real")],
  worked=[
      ("Hallar la longitud de onda", "En una cuerda con v = 12 m/s, f = 4 Hz. ¿Cuál es la longitud de onda?", ["De v = λ × f despejo λ = v ÷ f.", "12 dividido por 4 es 3."], "3 m"),
      ("Comprobar el producto", "Datos de ejemplo: f = 2 Hz, λ = 5 m y f = 5 Hz, λ = 2 m. ¿El producto es constante?", ["Calculo 2 × 5 = 10.", "Calculo 5 × 2 = 10."], "Sí, v = 10 m/s en ambos casos"),
  ],
  mistakes=[
      ("Pensar que sacudir más rápido hace la onda más veloz.", "La rapidez depende del medio y no de la frecuencia.", "Con v fija, aumenta f y disminuye λ."),
      ("Multiplicar en vez de dividir al despejar la longitud de onda.", "λ = v ÷ f.", "Escribe la fórmula antes de calcular."),
  ],
  rec=[
      ("¿De qué depende la rapidez de una onda en una cuerda: del medio o de la frecuencia?", "Del medio", "La frecuencia no cambia la rapidez."),
      ("Completa: si la rapidez es constante y aumenta la frecuencia, la longitud de onda ______ (disminuye o aumenta).", "Disminuye", "La relación es inversa."),
      ("Verdadero o falso: λ = v ÷ f.", "Verdadero", "Se despeja de v = λ × f."),
  ],
  und=[
      ("Una cuerda con v = 20 m/s y f = 5 Hz. ¿Cuál es λ? A) 4 m; B) 100 m.", "A", "20 dividido por 5 es 4."),
      ("¿Qué le pasa a λ si f se duplica y v no cambia? A) Se reduce a la mitad; B) Se duplica.", "A", "El producto debe seguir igual."),
      ("¿Qué indica que el producto λ × f cambie en una tabla?", "Que cambió la rapidez o hubo un error de medición", "En un mismo medio debe ser constante."),
  ],
  app=[
      arith("Una cuerda con v = 18 m/s tiene f = 3 Hz. ¿Cuál es la longitud de onda?", "18//3", "Se divide la rapidez entre la frecuencia.", " m"),
      arith("En agua de ejemplo, una onda tiene λ = 5 m y v = 15 m/s. ¿Cuál es su frecuencia?", "15//5", "Se divide la rapidez entre la longitud de onda.", " Hz"),
      ("Tabla de ejemplo: f = 2 Hz, λ = 8 m; f = 4 Hz, λ = 4 m; f = 8 Hz, λ = 2 m. ¿Cuál es la rapidez constante?", "16 m/s", "2 por 8, 4 por 4 y 8 por 2 son 16."),
  ],
  rea=[
      ("Un estudiante mide: f = 3 Hz, λ = 4 m; f = 6 Hz, λ = 3 m. ¿Qué concluye bien? A) Hay un dato inconsistente: 3 × 4 = 12 pero 6 × 3 = 18, por lo que hay que revisar la medición; B) Todo está bien.", "A", "En el mismo medio el producto debería ser igual."),
      ("Se tensa más una cuerda y la rapidez aumenta de 10 a 15 m/s. Para f = 5 Hz, ¿qué le pasa a λ? A) Aumenta de 2 a 3 m; B) Disminuye.", "A", "Con v mayor y f igual, λ crece."),
  ],
  cha=[
      arith("Una cuerda de ejemplo tiene v = 24 m/s. ¿Cuántos metros mayor es λ con f = 2 Hz que con f = 8 Hz?", "24//2-24//8", "Con 2 Hz λ = 12 m, con 8 Hz λ = 3 m; se restan."),
      ("Un compañero predice con la tabla de ejemplo (v = 16 m/s, datos de 2 a 8 Hz) que, para f = 1 Hz, λ = 16 m. ¿Qué limitación tiene? A) El valor está fuera del rango medido y no se sabe si la cuerda se comporta igual; B) La cuerda no tiene frecuencia.", "A", "Extrapolar es dudoso."),
  ],
  context=[arith("Una cuerda de guitarra de ejemplo vibra a 200 Hz. ¿Cuántas oscilaciones completas hace en 5 segundos?", "200*5", "Se multiplica la frecuencia por el tiempo.")],
  selfcheck=[("¿De qué depende la rapidez de una onda en una cuerda?", "Del medio", "No de la frecuencia."), ("¿Cómo se calcula λ?", "Dividiendo la rapidez entre la frecuencia", "λ = v ÷ f."), ("¿Qué relación hay entre f y λ si v es constante?", "Inversa", "Si una aumenta, la otra disminuye.")],
  open_task=task("Con una cuerda de v = 10 m/s (dato de ejemplo), completa la tabla: f = 1 Hz, f = 2 Hz, f = 5 Hz, f = 10 Hz. Calcula λ de cada una, escribe qué patrón ves y señala si el producto λ × f es constante.", "λ: 10 m, 5 m, 2 m, 1 m. Al aumentar f, λ disminuye (relación inversa). El producto es 10 en todos.", ["calcula cuatro valores", "describe la relación inversa", "verifica el producto"], ["tabla y conclusión"], ["multiplicar al despejar", "no verificar el producto"], "Pregunta qué cambiaría si la cuerda se tensara más."),
  reinforce="Calcula λ para v = 30 m/s y f = 6 Hz.",
  extend="Explica por qué dos ondas de la misma cuerda con distinta frecuencia tienen la misma rapidez.")

L(OA9, 5,
  materials="Una lámina brillante (por ejemplo, papel de aluminio liso pegado a un cartón), un vaso transparente de plástico con agua y un lápiz. Si no tienes, usa las descripciones de los ejercicios.",
  use="Aprenderé a explicar la reflexión, la refracción y la absorción de las ondas con ejemplos de la luz y del sonido. Sirve para entender espejos, el eco y por qué un lápiz parece quebrado en el agua.",
  prior=["Sé que las ondas transportan energía.", "Sé que la rapidez depende del medio."],
  explain=[
      "La reflexión ocurre cuando una onda choca con una superficie y rebota. El ángulo con que llega (ángulo de incidencia) es igual al ángulo con que sale (ángulo de reflexión), ambos medidos respecto de una línea perpendicular a la superficie llamada normal. El eco es sonido reflejado y un espejo refleja la luz.",
      "La refracción ocurre cuando una onda pasa de un medio a otro y cambia su rapidez, lo que desvía su dirección. Si la luz pasa del aire al agua, va más lenta y se acerca a la normal. Por eso, un lápiz parcialmente sumergido parece quebrado.",
      "La absorción ocurre cuando el medio recibe la energía de la onda y la transforma, por ejemplo en calor. Una prenda oscura absorbe más luz y se calienta más que una clara; una pared con espuma absorbe sonido y disminuye el eco. Una onda puede reflejarse, refractarse y absorberse a la vez, en distintas proporciones.",
  ],
  vocab=[("reflexión", "rebote de una onda en una superficie"), ("refracción", "desvío de una onda al cambiar de medio"), ("absorción", "transformación de la energía de la onda en el medio"), ("normal", "línea perpendicular a la superficie"), ("ángulo de incidencia", "ángulo entre la onda que llega y la normal")],
  worked=[
      ("Aplicar la reflexión", "Un rayo de luz llega a un espejo con 30° respecto de la normal. ¿Con qué ángulo sale?", ["El ángulo de reflexión es igual al de incidencia.", "Sale con 30°."], "30°"),
      ("Reconocer la refracción", "Un lápiz parece quebrado en un vaso con agua. ¿Qué fenómeno explica esto?", ["La luz pasa del agua al aire.", "Cambia su rapidez y se desvía."], "Refracción"),
  ],
  mistakes=[
      ("Medir el ángulo de reflexión desde la superficie en vez de desde la normal.", "Los ángulos se miden respecto de la normal.", "Dibuja primero la normal."),
      ("Pensar que la refracción siempre aleja la onda de la normal.", "Depende de si la onda pasa a un medio donde va más lenta o más rápida.", "Compara la rapidez en cada medio."),
  ],
  rec=[
      ("¿Cómo se llama el rebote de una onda en una superficie?", "Reflexión", "El eco y los espejos son ejemplos."),
      ("Completa: el desvío de una onda al cambiar de medio se llama ______ (refracción o absorción).", "Refracción", "Cambia su rapidez."),
      ("Verdadero o falso: la absorción transforma la energía de la onda en el medio.", "Verdadero", "Por ejemplo en calor."),
  ],
  und=[
      ("¿Qué fenómeno produce el eco? A) La reflexión del sonido; B) La refracción del sonido en el vacío.", "A", "El sonido rebota en una superficie."),
      ("¿Por qué una prenda negra se calienta más al sol? A) Porque absorbe más luz; B) Porque refleja toda la luz.", "A", "Absorbe más energía."),
      ("Cuando la luz pasa del aire al agua, ¿qué le pasa a su rapidez?", "Disminuye", "Por eso se acerca a la normal."),
  ],
  app=[
      ("Un rayo llega a una superficie reflectante con un ángulo de incidencia de 45°. ¿Cuál es el ángulo de reflexión?", "45°", "Los dos ángulos son iguales."),
      arith("Un rayo de ejemplo llega con un ángulo de incidencia de 25° respecto de la normal. ¿Cuántos grados forman en total el rayo que llega y el reflejado entre sí?", "25+25", "Se suman ambos ángulos medidos desde la normal.", "°"),
      ("En un salón con paredes cubiertas de espuma, el eco se reduce mucho. ¿Qué fenómeno explica esto? A) Absorción del sonido; B) Refracción de la luz.", "A", "La espuma transforma energía sonora."),
  ],
  rea=[
      ("Un estudiante dice: «Si la luz se refleja en un espejo, no puede ser absorbida». ¿Qué respuesta es mejor? A) Una parte se refleja y otra se absorbe; B) Tiene razón.", "A", "Los fenómenos ocurren en distintas proporciones."),
      ("Una persona ve su reflejo claro en un lago calmo y desordenado en un lago con olas. ¿Cuál es la razón? A) La superficie irregular refleja en muchas direcciones; B) El agua absorbe el reflejo.", "A", "Una superficie rugosa dispersa los rayos."),
  ],
  cha=[
      arith("Un sonido de ejemplo tarda 2 segundos en ir a una pared y volver como eco. Si el sonido viaja a 340 m/s, ¿a qué distancia está la pared?", "340*2//2", "Se calcula la distancia total de ida y vuelta y se divide por 2.", " m"),
      ("Una pecera de ejemplo parece más baja de lo que es al mirarla desde arriba. ¿Qué fenómeno lo explica? A) La refracción de la luz al pasar del agua al aire; B) La reflexión en el fondo.", "A", "La luz cambia de dirección al cambiar de medio."),
  ],
  context=[arith("Un auditorio de ejemplo cubre 120 m² de sus paredes con paneles que absorben sonido, y la mitad de ese material lo coloca en el techo. ¿Cuántos m² van en el techo?", "120//2", "La mitad de 120 es 60.")],
  selfcheck=[("¿Qué ley cumple la reflexión?", "El ángulo de incidencia es igual al de reflexión", "Se miden desde la normal."), ("¿Por qué ocurre la refracción?", "Porque la onda cambia de rapidez al pasar a otro medio", "Eso desvía su dirección."), ("Da un ejemplo de absorción.", "Una prenda negra que se calienta al sol", "Transforma energía en calor.")],
  open_task=task("Haz o imagina estas tres pruebas con tu lámina brillante, tu vaso con agua y tu lápiz: (1) apunta la linterna del teléfono a la lámina y anota los ángulos de incidencia y de reflexión (usa 30° y 60° de ejemplo); (2) mete un lápiz en el vaso con agua y describe cómo se ve; (3) cubre la lámina con tela oscura y describe qué pasa con el reflejo. Para cada una escribe qué fenómeno ocurrió.", "(1) reflexión: 30° y 30°, 60° y 60°. (2) refracción: el lápiz parece quebrado. (3) absorción: la tela absorbe la luz y no hay reflejo claro.", ["tres fenómenos nombrados", "ángulos iguales", "explica con rapidez o energía"], ["tabla de tres observaciones"], ["confundir reflexión con refracción", "medir desde la superficie"], "Pregunta qué cambiaría si el vaso tuviera aceite en vez de agua."),
  reinforce="Dibuja un rayo reflejado en un espejo con 40° de incidencia.",
  extend="Explica por qué un buzo ve los peces en un lugar distinto del real.")

# ---------------------------------------------------------------- OA 10

L(OA10, 1,
  materials="Una regla plástica de 30 cm, una mesa y un elástico grande. Si no tienes, usa las descripciones de los ejercicios.",
  use="Aprenderé que el sonido es una onda mecánica longitudinal producida por vibraciones, que necesita un medio y viaja con cierta rapidez. Sirve para formular preguntas investigables sobre el sonido.",
  prior=["Sé que las ondas mecánicas necesitan un medio.", "Sé qué es la frecuencia."],
  explain=[
      "El sonido se produce cuando un objeto vibra: la regla sujeta al borde de una mesa, las cuerdas vocales o la membrana de un parlante. La vibración empuja las partículas del aire, que se juntan y se separan formando zonas de compresión y de enrarecimiento. Es una onda mecánica longitudinal que viaja por el aire hasta el oído.",
      "El sonido necesita un medio: no se propaga en el vacío. Viaja en sólidos, líquidos y gases. En el aire a temperatura ambiente su rapidez es de unos 340 m/s; en el agua es mayor, unos 1.500 m/s, y en los sólidos suele ser aún mayor. Por eso se ve el rayo antes de oír el trueno: la luz es mucho más rápida.",
      "Una pregunta investigable sobre el sonido dice qué se mide. «¿Cuánto tarda el eco de una palmada en volver desde una pared a 34 metros?» se contesta con un cronómetro. «¿Es lindo el sonido de una campana?» no. Los experimentos con sonido deben hacerse a volumen moderado, sin acercar parlantes al oído. Un sonido agudo es de tono alto, como un silbato; uno grave es de tono bajo, como un tambor.",
  ],
  vocab=[("sonido", "onda mecánica longitudinal producida por una vibración"), ("compresión", "zona donde las partículas están más juntas"), ("vibración", "movimiento rápido de ida y vuelta"), ("rapidez del sonido", "distancia que recorre el sonido por segundo"), ("vacío", "espacio sin materia")],
  worked=[
      ("Origen del sonido", "Una regla sujeta al borde de una mesa se golpea y suena. ¿De dónde viene el sonido?", ["La regla vibra.", "La vibración mueve las partículas del aire."], "De la vibración de la regla"),
      ("Calcular una distancia", "Una tormenta de ejemplo: el trueno llega 3 segundos después del rayo. Con 340 m/s, ¿a qué distancia cayó el rayo?", ["Uso distancia = rapidez × tiempo.", "340 por 3 es 1.020."], "1.020 m"),
  ],
  mistakes=[
      ("Decir que el sonido viaja por el vacío.", "Necesita un medio material.", "Recuerda que es una onda mecánica."),
      ("Pensar que las partículas del aire viajan desde la fuente hasta el oído.", "Las partículas vibran en su lugar y la onda avanza.", "Piensa en una fila de personas que se empujan."),
  ],
  rec=[
      ("¿Qué produce el sonido?", "Una vibración", "Las vibraciones mueven las partículas del medio."),
      ("Completa: el sonido ______ (necesita o no necesita) un medio material.", "Necesita", "No se propaga en el vacío."),
      ("Verdadero o falso: el sonido viaja más rápido en el agua que en el aire.", "Verdadero", "En el agua es mayor."),
  ],
  und=[
      ("¿Por qué se ve el rayo antes de oír el trueno? A) Porque la luz es mucho más rápida que el sonido; B) Porque el sonido nace después de la luz.", "A", "Ambos se producen casi a la vez, pero llegan en tiempos distintos."),
      ("¿Qué tipo de onda es el sonido? A) Mecánica y longitudinal; B) Electromagnética y transversal.", "A", "Necesita medio y las partículas oscilan en la dirección del avance."),
      ("¿Qué es una compresión?", "Una zona donde las partículas están más juntas", "Alterna con zonas más separadas."),
  ],
  app=[
      arith("Un trueno de ejemplo llega 5 segundos después del rayo. Con 340 m/s, ¿a cuántos metros cayó el rayo?", "340*5", "Se multiplica la rapidez por el tiempo.", " m"),
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos segundos tarda el eco de una palmada en volver desde una pared a 34 m?; B) ¿Es hermoso el eco?", "A", "Se contesta midiendo el tiempo."),
      arith("En 3 segundos, ¿cuántos metros más recorre el sonido en el agua (1.500 m/s) que en el aire (340 m/s)?", "1500*3-340*3", "Se calcula la distancia en cada medio y se restan.", " m"),
  ],
  rea=[
      ("Un astronauta golpea una herramienta en el espacio vacío. Su compañero, a 2 metros, no oye nada directamente. ¿Por qué? A) No hay medio material para el sonido; B) La herramienta no vibra.", "A", "El sonido necesita medio."),
      ("Una persona apoya el oído sobre una mesa y oye el golpe de un lápiz en el otro extremo antes que por el aire. ¿Qué explica esto? A) El sonido viaja más rápido en el sólido que en el aire; B) La mesa produce sonido nuevo.", "A", "En los sólidos la rapidez suele ser mayor."),
  ],
  cha=[
      arith("Si el sonido va a 1.500 m/s en el agua, ¿cuántos metros recorre en 2 segundos?", "1500*2", "Se multiplica la rapidez por el tiempo.", " m"),
      ("Un estudiante mide el tiempo del eco con un cronómetro y obtiene 0 segundos, y concluye que el sonido es instantáneo. ¿Cuál es la crítica? A) El cronómetro no mide tiempos tan cortos con una pared cercana, por lo que usa una pared más lejana; B) El sonido es instantáneo.", "A", "Hay que escoger una distancia mayor para medir."),
  ],
  context=[arith("En un patio de ejemplo, una persona aplaude y oye el eco 2 segundos después. ¿Cuántos metros recorrió el sonido en total (ida y vuelta) a 340 m/s?", "340*2", "Se multiplica la rapidez por el tiempo.", " m")],
  selfcheck=[("¿Qué origina físicamente un sonido en una fuente como un tambor?", "Una vibración", "Mueve las partículas del medio."), ("¿Se propaga el sonido en el vacío?", "No", "Necesita un medio material."), ("¿Cuál es la rapidez aproximada del sonido en el aire?", "340 m/s", "En el agua es mayor.")],
  open_task=task("Con una regla de 30 cm sujeta firmemente al borde de una mesa con la mano (sin hacer fuerza excesiva), deja 20 cm fuera y vibra la regla; luego deja 10 cm fuera y vibra. Anota si el sonido es más agudo o más grave en cada caso. Si no tienes regla, usa estos datos de ejemplo: con 20 cm, grave; con 10 cm, agudo. Escribe una pregunta investigable y una conclusión.", "Con 10 cm el sonido es más agudo. Pregunta: «¿Cómo cambia el sonido al acortar la parte libre de la regla?». Conclusión: al acortar la parte que vibra, el tono sube.", ["registra las dos observaciones", "pregunta con algo observable", "conclusión coherente"], ["tabla y conclusión"], ["afirmar sin observar", "pregunta de opinión"], "Pregunta qué otra variable podrías cambiar."),
  reinforce="Explica qué produce el sonido en un tambor.",
  extend="Explica por qué en el espacio las naves no hacen ruido para los astronautas fuera de ellas.")

L(OA10, 2,
  materials="Este cuaderno y lápiz. Los gráficos de ondas y las tablas están descritos con medidas en los ejercicios.",
  use="Aprenderé las cualidades del sonido: intensidad, tono, timbre y rapidez, y su relación con la onda. Sirve para describir y comparar sonidos con datos.",
  prior=["Sé la amplitud y la frecuencia.", "Sé que el sonido es una onda."],
  explain=[
      "La intensidad es qué tan fuerte se percibe el sonido (volumen) y depende de la amplitud: a mayor amplitud, mayor intensidad. Se mide en decibeles (dB). El tono es qué tan agudo o grave es el sonido y depende de la frecuencia: mayor frecuencia, tono más agudo. Se mide en hercios (Hz).",
      "El timbre es la cualidad que permite distinguir dos instrumentos que tocan la misma nota con la misma intensidad: depende de la forma de la onda. La rapidez es la velocidad con que el sonido recorre un medio y depende del medio, no de la intensidad ni del tono. Las personas oyen frecuencias entre unos 20 y 20.000 Hz. Menos de 20 Hz es infrasonido y más de 20.000 Hz es ultrasonido.",
      "Valores de referencia en decibeles (aproximados): un susurro, 30 dB; una conversación, 60 dB; tráfico intenso, 80 dB; un concierto fuerte, 110 dB. Escuchar sonidos muy intensos por largo tiempo puede dañar el oído.",
  ],
  vocab=[("intensidad", "qué tan fuerte se percibe un sonido; depende de la amplitud"), ("tono", "qué tan agudo o grave es un sonido; depende de la frecuencia"), ("timbre", "cualidad que distingue dos fuentes que dan la misma nota"), ("decibel (dB)", "unidad con que se mide la intensidad del sonido"), ("ultrasonido", "sonido con frecuencia mayor que 20.000 Hz")],
  worked=[
      ("Relacionar cualidad y onda", "Un sonido tiene mayor frecuencia que otro. ¿Cuál cualidad cambia?", ["La frecuencia está asociada al tono.", "Mayor frecuencia significa tono más agudo."], "El tono; es más agudo"),
      ("Rango de audición", "Un sonido de 30.000 Hz, ¿puede oírlo una persona?", ["El rango humano llega hasta unos 20.000 Hz.", "30.000 es mayor."], "No, es ultrasonido"),
  ],
  mistakes=[
      ("Decir que un sonido más agudo es más fuerte.", "El tono se relaciona con la frecuencia y la intensidad con la amplitud.", "Pregunta si cambia la frecuencia o la amplitud."),
      ("Pensar que el timbre depende de la intensidad.", "El timbre depende de la forma de la onda.", "Compara la forma de las ondas."),
  ],
  rec=[
      ("¿De qué magnitud depende el tono?", "De la frecuencia", "A mayor frecuencia, más agudo."),
      ("Completa: la intensidad depende de la ______ (amplitud o frecuencia).", "Amplitud", "Mayor amplitud, mayor volumen."),
      ("Verdadero o falso: el timbre permite distinguir dos instrumentos que tocan la misma nota.", "Verdadero", "Depende de la forma de la onda."),
  ],
  und=[
      ("Dos sonidos tienen la misma frecuencia y el segundo tiene mayor amplitud. ¿Qué cambia? A) La intensidad; B) El tono.", "A", "La amplitud fija la intensidad."),
      ("Una flauta y un violín tocan la misma nota con igual volumen. ¿Por qué suenan distinto? A) Por su timbre; B) Por su tono.", "A", "Las formas de onda son distintas."),
      ("¿Cuál es el rango de frecuencias que oyen las personas?", "De unos 20 a 20.000 Hz", "Fuera de ese rango son infrasonido o ultrasonido."),
  ],
  app=[
      ("Dos sonidos de ejemplo: el A de 200 Hz y el B de 800 Hz. ¿Cuál es más agudo?", "El B", "Tiene mayor frecuencia."),
      arith("Un ultrasonido de ejemplo tiene 40.000 Hz. ¿Cuántos Hz más que 20.000 Hz tiene?", "40000-20000", "Se resta el límite superior del rango humano.", " Hz"),
      arith("Con los valores de referencia, ¿cuántos dB más intenso es un concierto fuerte (110 dB) que una conversación (60 dB)?", "110-60", "Se resta el valor de la conversación al del concierto.", " dB"),
  ],
  rea=[
      ("Un estudiante dice que el timbre depende de la frecuencia. ¿Qué corrección haces? A) El tono depende de la frecuencia y el timbre de la forma de la onda; B) Tiene razón.", "A", "Son cualidades distintas."),
      ("Un gráfico de ejemplo muestra dos ondas con la misma frecuencia; la B es el doble de alta que la A. ¿Cuál se oye más fuerte? A) La B; B) La A.", "A", "Mayor amplitud significa mayor intensidad."),
  ],
  cha=[
      ("Un sonido de 500 Hz tiene el doble de frecuencia que otro. ¿Cuántos hercios tiene el otro?", "250", "500 dividido por 2 es 250."),
      ("Un perro responde a un silbato que las personas no oyen. ¿Qué característica tiene probablemente el sonido? A) Una frecuencia mayor que 20.000 Hz; B) Una frecuencia de 100 Hz.", "A", "Es un ultrasonido."),
  ],
  context=[arith("Una orquesta de ejemplo tiene 8 violines, 5 flautas y 3 tambores. ¿Cuántos instrumentos hay en total?", "8+5+3", "Se suman los instrumentos de los tres grupos.")],
  selfcheck=[("¿De qué depende el tono?", "De la frecuencia", "A mayor frecuencia, más agudo."), ("¿De qué depende la intensidad?", "De la amplitud", "A mayor amplitud, más fuerte."), ("¿Qué es el timbre?", "La cualidad que distingue dos fuentes que dan la misma nota", "Depende de la forma de la onda.")],
  open_task=task("Con esta tabla de ejemplo clasifica cada sonido: tambor grande, 100 Hz, 90 dB; flauta, 1.000 Hz, 60 dB; voz de una persona, 200 Hz, 55 dB; silbato, 3.000 Hz, 70 dB. Ordena de más grave a más agudo y de menos a más intenso. Escribe una frase sobre el cuidado del oído.", "Del más grave al más agudo: tambor, voz, flauta, silbato. De menos a más intenso: voz (55), flauta (60), silbato (70), tambor (90). Cuidado: evitar sonidos muy fuertes por mucho tiempo.", ["dos órdenes correctos", "usa frecuencia para el tono", "frase de cuidado coherente"], ["tabla y frase"], ["confundir tono con intensidad", "orden invertido"], "Pregunta qué ocurriría con otro instrumento que suene igual de agudo."),
  reinforce="Escribe una diferencia entre tono e intensidad.",
  extend="Explica por qué el ultrasonido no se oye aunque sea una onda sonora.")

L(OA10, 3,
  materials="Un elástico, una regla y un vaso de plástico. Si no tienes, usa las descripciones de los ejercicios.",
  use="Aprenderé cómo se producen los sonidos en cuerdas vocales, parlantes e instrumentos, y qué es la resonancia. Sirve para explicar por qué cambia el tono de un instrumento.",
  prior=["Sé qué es la frecuencia y el tono.", "Sé que el sonido nace de una vibración."],
  explain=[
      "Las cuerdas vocales son dos pliegues en la laringe que vibran cuando pasa aire. Al tensarlas, vibran más rápido y el tono es más agudo. Un parlante tiene una membrana que vibra según una señal eléctrica y empuja el aire. En los instrumentos de cuerda, el tono depende de la longitud, la tensión y el grosor de la cuerda.",
      "Para una misma cuerda: si se acorta, la frecuencia aumenta y el tono es más agudo; si se tensa más, la frecuencia aumenta; si es más gruesa, la frecuencia disminuye. En los instrumentos de viento vibra una columna de aire: un tubo más corto produce un tono más agudo.",
      "La resonancia ocurre cuando un cuerpo es hecho vibrar por una onda con una frecuencia igual a la suya, y vibra con gran amplitud. La caja de una guitarra resuena y amplifica el sonido de las cuerdas. Un modelo con una cuerda y una caja muestra esto, aunque no incluye todos los detalles del material.",
  ],
  vocab=[("cuerdas vocales", "pliegues de la laringe que vibran al pasar aire"), ("membrana", "lámina delgada que vibra, como la de un parlante"), ("tensión", "fuerza con que está estirada una cuerda"), ("resonancia", "vibración de gran amplitud cuando la onda tiene la frecuencia natural del cuerpo"), ("caja de resonancia", "parte de un instrumento que amplifica el sonido")],
  worked=[
      ("Efecto de acortar", "Una cuerda de guitarra se presiona en un traste y queda más corta. ¿Cómo cambia el tono?", ["Una cuerda más corta vibra más rápido.", "Su frecuencia aumenta."], "Más agudo"),
      ("Efecto del grosor", "Dos cuerdas igual de largas y tensas: una delgada y una gruesa. ¿Cuál suena más grave?", ["La gruesa tiene más masa.", "Vibra más lento."], "La cuerda gruesa"),
  ],
  mistakes=[
      ("Pensar que una cuerda más tensa suena más grave.", "Al tensar, la frecuencia aumenta y el tono es más agudo.", "Relaciona tensión con tono agudo."),
      ("Creer que la caja de una guitarra produce energía.", "Resuena y amplifica el sonido sin crear energía.", "La energía viene de la cuerda al ser pulsada."),
  ],
  rec=[
      ("¿Qué vibra en la garganta cuando hablamos?", "Las cuerdas vocales", "Vibran cuando pasa el aire."),
      ("Completa: una cuerda más corta produce un tono más ______ (agudo o grave).", "Agudo", "Su frecuencia aumenta."),
      ("Verdadero o falso: una cuerda más gruesa suena más grave.", "Verdadero", "Vibra más lento."),
  ],
  und=[
      ("¿Qué ocurre si se tensan más las cuerdas vocales? A) El tono es más agudo; B) El tono es más grave.", "A", "Vibran más rápido."),
      ("¿Para qué sirve la caja de una guitarra? A) Para resonar y amplificar el sonido; B) Para cambiar la frecuencia de las cuerdas.", "A", "Resuena con las cuerdas."),
      ("¿Qué vibra en un parlante?", "Una membrana", "Empuja el aire y produce el sonido."),
  ],
  app=[
      ("Una cuerda de 60 cm suena más grave que una de 30 cm de igual material y tensión. ¿Es coherente? A) Sí, porque la cuerda más larga tiene menor frecuencia; B) No, porque la más larga debe sonar más aguda.", "A", "Mayor longitud, menor frecuencia."),
      arith("Una cuerda vibra 440 veces por segundo. ¿Cuántas oscilaciones hace en 5 segundos?", "440*5", "Se multiplica la frecuencia por el tiempo."),
      ("Un tubo de flauta se acorta de 40 cm a 20 cm. ¿Qué pasa con el tono? A) Se vuelve más agudo; B) Se vuelve más grave.", "A", "Una columna de aire más corta vibra más rápido."),
  ],
  rea=[
      ("Una persona canta una nota aguda y luego una grave. ¿Qué cambió en sus cuerdas vocales? A) La tensión y la frecuencia de vibración; B) El tamaño del cuerpo.", "A", "Al tensarlas aumenta la frecuencia."),
      ("Un estudiante dice que, en un violín, la caja de resonancia crea sonido sin vibración de cuerdas. ¿Qué evidencia lo contradice? A) Sin vibrar las cuerdas no se produce sonido, y la caja solo lo amplifica; B) La caja no existe.", "A", "La fuente es la cuerda."),
  ],
  cha=[
      ("Datos de ejemplo: una cuerda de 50 cm produce 200 Hz. Si se acorta a la mitad (25 cm) con la misma tensión, su frecuencia se duplica. ¿Qué frecuencia tiene?", "400", "El doble de 200 es 400 Hz."),
      ("Una copa de cristal vibra cuando se emite un sonido que coincide con su frecuencia natural. ¿Qué fenómeno ocurre? A) Resonancia; B) Absorción.", "A", "El cuerpo vibra con gran amplitud."),
  ],
  context=[arith("Una banda de ejemplo tiene 3 guitarras de 6 cuerdas cada una. ¿Cuántas cuerdas vibran en total?", "3*6", "Se multiplica el número de guitarras por las cuerdas.")],
  selfcheck=[("¿Cómo cambia el tono si se acorta una cuerda?", "Sube", "Aumenta su frecuencia."), ("¿Qué es la resonancia?", "Una vibración de gran amplitud cuando coincide la frecuencia", "Amplifica el sonido."), ("¿Qué vibra en las cuerdas vocales?", "Pliegues de la laringe", "Se mueven al pasar el aire.")],
  open_task=task("Con un elástico grande estirado entre dos dedos, pulsa el elástico en tres situaciones y anota si el tono es más agudo o más grave: (1) estirado poco; (2) estirado bastante, sin llegar al máximo; (3) estirado igual que en (2) y acortado con un dedo a la mitad. Hazlo con cuidado y, si es posible, con una persona adulta cerca: usa un elástico nuevo, no lo estires hasta el máximo ni cerca de la cara, no lo apuntes hacia ninguna persona y protege tus ojos. Si no tienes elástico, usa estos datos de ejemplo: (1) grave; (2) agudo; (3) muy agudo. Escribe una conclusión sobre la tensión y la longitud.", "Más tensión aumenta el tono; menos longitud también. Orden de grave a agudo: (1), (2), (3).", ["anota tres observaciones", "relaciona tensión y longitud con tono", "conclusión coherente"], ["tabla y conclusión"], ["relacionar tensión con tono grave", "no registrar los casos"], "Pregunta qué pasaría con un elástico más grueso."),
  reinforce="Explica por qué una guitarra tiene cuerdas de distinto grosor.",
  extend="Explica por qué la resonancia exige que la frecuencia de la onda coincida con la frecuencia natural del cuerpo.")

L(OA10, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a explicar el eco, el efecto Doppler y a calcular distancias con el tiempo del sonido. Sirve para entender sirenas que pasan, el sonar y el eco.",
  prior=["Sé que el sonido viaja a unos 340 m/s en el aire.", "Sé qué es la reflexión."],
  explain=[
      "El eco es el sonido reflejado que llega a nuestros oídos al menos 0,1 segundos después del sonido original. Para calcular la distancia a una pared: el sonido va y vuelve, por eso d = v × t ÷ 2. Si el eco tarda 2 segundos y v = 340 m/s, d = 340 × 2 ÷ 2 = 340 m.",
      "El efecto Doppler es el cambio de la frecuencia que percibe una persona cuando la fuente sonora y el observador se acercan o se alejan. Cuando una ambulancia se acerca, las ondas llegan más juntas y el tono se oye más agudo; cuando se aleja, llegan más separadas y se oye más grave. La ambulancia emite siempre la misma frecuencia.",
      "En el sonar, un barco emite un sonido bajo el agua y mide el tiempo del eco para calcular la profundidad o la distancia a un objeto, con v ≈ 1.500 m/s en el agua. Estas relaciones permiten calcular y predecir con datos, siempre que se conozca la rapidez en cada medio.",
  ],
  vocab=[("eco", "sonido reflejado que se oye después del original"), ("efecto Doppler", "cambio de la frecuencia percibida por el movimiento relativo de fuente y observador"), ("sonar", "sistema que usa el eco del sonido para medir distancias bajo el agua"), ("ida y vuelta", "recorrido hasta el obstáculo y de regreso"), ("frecuencia percibida", "la que oye el observador")],
  worked=[
      ("Calcular la distancia al obstáculo", "Un eco tarda 4 segundos. Con 340 m/s, ¿a qué distancia está la pared?", ["El sonido va y vuelve, así que d = v × t ÷ 2.", "340 por 4 es 1.360 y 1.360 dividido por 2 es 680."], "680 m"),
      ("Aplicar el Doppler", "Una ambulancia se acerca. ¿El tono que oyes es más agudo o más grave que el real?", ["Al acercarse, las ondas llegan más juntas.", "La frecuencia percibida aumenta."], "Más agudo"),
  ],
  mistakes=[
      ("Olvidar dividir por 2 al calcular la distancia con un eco.", "El tiempo medido incluye ida y vuelta.", "Escribe d = v × t ÷ 2."),
      ("Decir que la sirena cambia su frecuencia al pasar a un lado.", "La sirena emite siempre igual; cambia lo que percibe el observador.", "Distingue lo emitido de lo percibido."),
  ],
  rec=[
      ("¿Qué fórmula da la distancia con un eco?", "d = v × t ÷ 2", "El tiempo es de ida y vuelta."),
      ("Completa: cuando una fuente sonora se aleja, el tono percibido es más ______ (grave o agudo).", "Grave", "La frecuencia percibida disminuye."),
      ("Verdadero o falso: el sonar usa el eco del sonido para medir distancias.", "Verdadero", "Mide el tiempo de ida y vuelta."),
  ],
  und=[
      ("¿Por qué se divide entre 2? A) Porque el sonido recorre la distancia dos veces; B) Porque el sonido es lento.", "A", "El eco es ida y vuelta."),
      ("Una moto pasa y su sonido se vuelve más grave al alejarse. ¿Cómo se llama el fenómeno? A) Efecto Doppler; B) Resonancia.", "A", "Cambia la frecuencia percibida por el movimiento."),
      ("¿Qué rapidez se usa para el sonido en el agua en el sonar?", "Unos 1.500 m/s", "Es mayor que en el aire."),
  ],
  app=[
      arith("Un eco tarda 6 segundos en volver desde un acantilado. Con 340 m/s, ¿a qué distancia está?", "340*6//2", "Se multiplica la rapidez por el tiempo y se divide entre 2.", " m"),
      arith("Un sonar de ejemplo recibe el eco del fondo del mar a los 2 segundos. Con 1.500 m/s, ¿qué profundidad tiene?", "1500*2//2", "Se multiplica por el tiempo y se divide entre 2.", " m"),
      ("Una bocina emite siempre la misma frecuencia. Una persona quieta la oye a 540 Hz mientras se acerca y a 470 Hz mientras se aleja. ¿Cuál puede ser la frecuencia que emite? A) 500 Hz; B) 600 Hz.", "A", "Al acercarse se oye más aguda y al alejarse más grave, así que la real queda entre 470 y 540 Hz."),
  ],
  rea=[
      ("Una persona dice: «La ambulancia cambia su sirena cuando pasa». ¿Qué evidencia lo contradice? A) El conductor oye siempre el mismo tono, y solo cambia para el observador que está quieto; B) La ambulancia no tiene sirena.", "A", "El cambio depende del movimiento relativo."),
      ("Un eco tarda 0,05 segundos en una sala pequeña y no se distingue del sonido original. ¿Por qué? A) El tiempo es demasiado corto para oírlo separado; B) El eco no existe en salas pequeñas.", "A", "Hace falta un retraso mayor a unos 0,1 segundos."),
  ],
  cha=[
      arith("Un barco de ejemplo registra un eco a los 8 segundos y otro a los 12 segundos de un segundo objeto. Con 1.500 m/s, ¿cuántos metros más lejos está el segundo objeto?", "1500*12//2-1500*8//2", "Se calculan ambas distancias y se restan.", " m"),
      ("Un murciélago usa sonidos para orientarse en la oscuridad. ¿Qué principio usa? A) El eco para ubicar objetos; B) La refracción de la luz.", "A", "Mide el retorno del sonido."),
  ],
  context=[arith("Una persona de ejemplo grita frente a un cerro y oye el eco a los 10 segundos. A 340 m/s, ¿a qué distancia está el cerro?", "340*10//2", "Se multiplica y se divide entre 2.", " m")],
  selfcheck=[("¿Cómo se calcula la distancia con un eco?", "Con d = v × t ÷ 2", "Se divide por 2 por la ida y vuelta."), ("¿Cuándo se oye más agudo el sonido de una fuente en movimiento?", "Cuando se acerca", "Las ondas llegan más juntas."), ("¿Para qué se usa el sonar?", "Para medir distancias bajo el agua con el eco", "Mide el tiempo de ida y vuelta.")],
  open_task=task("Resuelve estos datos de ejemplo: (1) un eco tarda 8 segundos en el aire (340 m/s); calcula la distancia; (2) un sonar recibe un eco a los 4 segundos en el agua (1.500 m/s); calcula la profundidad; (3) una ambulancia emite 700 Hz y se aleja; ¿el tono percibido es mayor o menor que 700 Hz? Explica con una frase.", "(1) 340 por 8 dividido por 2 es 1.360 m. (2) 1.500 por 4 dividido por 2 es 3.000 m. (3) Menor, porque al alejarse las ondas llegan más separadas.", ["tres respuestas correctas", "usa d = v × t ÷ 2", "explica el Doppler"], ["cálculos y frase"], ["olvidar dividir por 2", "decir que la ambulancia cambia su frecuencia"], "Pregunta qué cambiaría si la temperatura del aire fuera menor."),
  reinforce="Calcula la distancia de un eco que tarda 2 segundos en el aire.",
  extend="Explica por qué el sonar usa sonido y no luz bajo el agua profunda.")

L(OA10, 5,
  materials="Este cuaderno y lápiz. Los valores de intensidad son aproximados y se entregan en los ejercicios.",
  use="Aprenderé las consecuencias del sonido (contaminación acústica y comunicación) y sus aplicaciones tecnológicas: ecógrafo, sonar, estetoscopio y entretención. Sirve para cuidar el oído y entender tecnologías de la salud.",
  prior=["Sé las cualidades del sonido.", "Sé el eco y el ultrasonido."],
  explain=[
      "El sonido sirve para comunicarse: hablamos, usamos teléfonos y parlantes. Pero un sonido muy intenso o muy prolongado produce contaminación acústica y puede dañar el oído. Como referencia aproximada, exponerse por mucho tiempo a más de unos 85 dB puede producir daño. Para cuidar el oído, se baja el volumen de los audífonos, se hacen descansos y se avisa a una persona adulta o al médico si hay zumbidos o dolor persistentes.",
      "Las aplicaciones tecnológicas usan las propiedades del sonido. El ecógrafo emite ultrasonido, que se refleja en los tejidos; el equipo mide los ecos y forma una imagen, por ejemplo de un embarazo, sin radiación. El sonar usa ecos bajo el agua para medir profundidades. El estetoscopio conduce los sonidos del cuerpo, como los latidos, al oído del profesional de la salud.",
      "Los parlantes y los instrumentos musicales usan la vibración para entretener. Al evaluar una tecnología se consideran su beneficio, sus límites (por ejemplo, el ultrasonido no atraviesa bien el aire ni el hueso) y su seguridad. Decidir sobre estudios médicos es una tarea de profesionales de la salud.",
  ],
  vocab=[("contaminación acústica", "exceso de ruido que perjudica a las personas"), ("ecógrafo", "equipo que usa ultrasonido para formar imágenes"), ("estetoscopio", "instrumento que conduce sonidos del cuerpo al oído"), ("sonar", "sistema que usa ecos para medir distancias bajo el agua"), ("exposición", "tiempo durante el que se está en contacto con un sonido")],
  worked=[
      ("Evaluar un riesgo", "Una persona escucha música a 95 dB durante 3 horas con audífonos. ¿Es un nivel de riesgo?", ["La referencia indica riesgo sobre unos 85 dB por mucho tiempo.", "95 es mayor que 85 y son 3 horas."], "Sí, hay riesgo de daño al oído"),
      ("Identificar una aplicación", "Un equipo envía ultrasonido, recibe los ecos y forma una imagen del interior del cuerpo. ¿Cómo se llama?", ["Usa ultrasonido y ecos.", "Forma imágenes del interior."], "Ecógrafo"),
  ],
  mistakes=[
      ("Pensar que el ultrasonido es peligroso porque no se oye.", "El ecógrafo usa ultrasonido de forma segura con control profesional.", "Distingue ultrasonido de ruido intenso."),
      ("Subir el volumen de los audífonos para tapar el ruido de la calle.", "Se aumenta la exposición y el riesgo.", "Baja el volumen, haz descansos y busca lugares más tranquilos."),
  ],
  rec=[
      ("¿Qué equipo usa ultrasonido para formar imágenes del cuerpo?", "El ecógrafo", "Mide los ecos de los tejidos."),
      ("Completa: el exceso de ruido que perjudica a las personas es la contaminación ______ (acústica o lumínica).", "Acústica", "Se relaciona con sonidos intensos."),
      ("Verdadero o falso: el estetoscopio conduce los sonidos del cuerpo al oído.", "Verdadero", "Permite oír latidos y respiración."),
  ],
  und=[
      ("¿Qué mide el sonar? A) Distancias o profundidades usando el eco; B) La temperatura del agua.", "A", "Mide el tiempo del eco."),
      ("¿Qué debe hacer una persona con zumbidos persistentes en el oído? A) Avisar a una persona adulta y consultar a un profesional de la salud; B) Subir el volumen para ignorarlos.", "A", "Pueden indicar daño y requieren evaluación."),
      ("¿Por qué el ecógrafo es una aplicación del eco?", "Porque forma imágenes con los ecos del ultrasonido", "Mide los sonidos reflejados."),
  ],
  app=[
      ("Escalas aproximadas: susurro 30 dB, conversación 60 dB, tráfico intenso 80 dB, concierto fuerte 110 dB. ¿Cuál de esas fuentes supera los 85 dB?", "El concierto fuerte", "Es la única con más de 85 dB."),
      arith("Una persona escucha música a 100 dB con audífonos 2 horas diarias durante 5 días a la semana. ¿Cuántas horas a la semana se expone a un nivel sobre los 85 dB?", "2*5", "Se multiplican las horas diarias por los días."),
      ("Una escuela instala paneles en un gimnasio ruidoso. ¿Qué fenómeno aprovechan para reducir el ruido? A) Absorción del sonido; B) Refracción de la luz.", "A", "Los paneles transforman energía sonora."),
  ],
  rea=[
      ("Un estudiante dice: «El ecógrafo sirve porque el ultrasonido pasa igual por el hueso y por el agua». ¿Cuál es la corrección? A) El ultrasonido se refleja distinto en distintos tejidos, y eso permite formar la imagen; B) El ultrasonido es luz.", "A", "Las diferencias de reflexión generan la imagen."),
      ("Un grupo propone que el sonar sirva para medir la altura de una montaña desde un avión. ¿Qué limitación tiene? A) El sonido se atenúa y es lento en el aire, y el sonar está pensado para el agua; B) El sonar no usa sonido.", "A", "El sonar se diseñó para el agua."),
  ],
  cha=[
      ("Un cuadro de ejemplo muestra 4 lugares con ruido de 55, 70, 90 y 100 dB. ¿Cuántos superan los 85 dB?", "2", "Son los de 90 y 100 dB."),
      ("Una escuela quiere hacer un plan para reducir el ruido en el patio. ¿Qué medida tiene más sentido? A) Medir primero el ruido por franjas horarias y luego proponer medidas; B) Prohibir hablar durante todo el día.", "A", "Una decisión con datos es más efectiva."),
  ],
  context=[arith("En una enfermería de ejemplo, 3 profesionales usan cada uno 2 estetoscopios. ¿Cuántos estetoscopios hay?", "3*2", "Se multiplica el número de profesionales por los instrumentos.")],
  selfcheck=[("¿Qué es la contaminación acústica?", "El exceso de ruido que perjudica a las personas", "Puede dañar el oído."), ("¿Qué usa un ecógrafo?", "Ultrasonido y sus ecos", "Forma imágenes con los ecos."), ("¿Qué hacer si hay zumbidos persistentes?", "Avisar a una persona adulta y consultar a un profesional de la salud", "Pueden ser señales de daño.")],
  open_task=task("Con estos datos de ejemplo de ruido en una escuela: sala de clases 55 dB, pasillo en recreo 85 dB, taller 95 dB, biblioteca 40 dB. Ordena de menor a mayor, señala cuáles superan los 85 dB y propone dos medidas concretas, una para el taller y otra para el cuidado personal del oído (por ejemplo, descansos y volumen moderado). Cierra con una aplicación tecnológica del sonido y su principio.", "Orden: biblioteca, sala, pasillo, taller. Supera 85 dB: el taller (95). Medidas: paneles absorbentes en el taller y descansos con volumen moderado. Aplicación: sonar, usa el eco del sonido bajo el agua.", ["orden correcto", "identifica el nivel de riesgo", "dos medidas y una aplicación"], ["lista ordenada y medidas"], ["incluir el pasillo en el riesgo", "no relacionar la aplicación con el eco"], "Pregunta qué dato más mediría para decidir qué medida aplicar primero."),
  reinforce="Escribe tres hábitos para cuidar el oído al usar audífonos.",
  extend="Explica por qué el ultrasonido sirve para ver el interior del cuerpo sin usar radiación.")

"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 13 (ondas sísmicas, medición y consecuencias)."""
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


OA = "CN1M OA 13"

L(OA, 1,
  materials="Este cuaderno, lápiz, regla y calculadora. Los datos de los boletines sísmicos de los ejercicios son de ejemplo y están escritos completos.",
  use="Aprenderé cómo se origina un sismo y qué parámetros lo describen: hipocentro, epicentro, área de ruptura, magnitud e intensidad. Sirve para leer un boletín sísmico sin confundir los datos.",
  prior=["Sé que la corteza terrestre está dividida en placas que se mueven.", "Sé que una onda transmite energía sin transportar materia."],
  explain=[
      "Un sismo es una vibración del terreno causada por la liberación brusca de energía acumulada en las rocas. En Chile, la mayoría de los grandes sismos se origina por subducción: la placa de Nazca se hunde bajo la placa Sudamericana. Las placas se traban y acumulan energía; cuando la fricción se vence, las rocas se rompen y deslizan, y la energía sale como ondas. También hay sismos en fallas de la corteza.",
      "Para describirlo se usan varios parámetros. El hipocentro, o foco, es el punto del interior de la Tierra donde comienza la ruptura. El epicentro es el punto de la superficie que está justo sobre el hipocentro; la distancia vertical entre ambos es la profundidad. El área de ruptura es la superficie de la falla que se desplazó, y es mayor en los sismos más grandes. Para hallar la distancia en línea recta entre un lugar de la superficie y el hipocentro se usa el teorema de Pitágoras: el cuadrado de esa distancia es la suma de los cuadrados de la distancia sobre la superficie y de la profundidad.",
      "La magnitud mide la energía liberada en la fuente y es un único valor para cada sismo. La intensidad describe los efectos que se observan en un lugar, como lo que sienten las personas y los daños, y se mide con la escala de Mercalli, con números romanos de I a XII. La intensidad cambia con la distancia, el tipo de suelo y la calidad de las construcciones. Un sismo tiene una magnitud y muchas intensidades.",
  ],
  vocab=[("sismo", "vibración del terreno por liberación brusca de energía en las rocas"), ("subducción", "hundimiento de una placa bajo otra"), ("hipocentro", "punto del interior donde comienza la ruptura"), ("epicentro", "punto de la superficie sobre el hipocentro"), ("magnitud", "medida de la energía liberada por un sismo"), ("intensidad", "medida de los efectos del sismo en un lugar")],
  worked=[
      ("Profundidad focal", "Un boletín indica que el hipocentro está a 30 km bajo el epicentro. ¿Qué distancia hay entre ambos?", ["El epicentro está justo sobre el hipocentro.", "La distancia entre ellos es la profundidad."], "30 km"),
      ("Magnitud o intensidad", "Un sismo de magnitud 7,0 produjo intensidad VII en la ciudad A e intensidad IV en la ciudad B. ¿Por qué hay dos valores de intensidad?", ["La magnitud es única.", "La intensidad depende de la distancia, el suelo y las construcciones, que son distintos en cada lugar."], "Porque la intensidad varía de un lugar a otro"),
  ],
  mistakes=[
      ("Decir que un sismo tiene una magnitud distinta en cada ciudad.", "La magnitud mide la energía en la fuente y es una sola; lo que cambia es la intensidad.", "Pregunta si el dato se refiere a la fuente o a un lugar."),
      ("Confundir epicentro con hipocentro.", "El epicentro está en la superficie y el hipocentro, en el interior.", "Piensa que el epicentro está «encima» del hipocentro."),
  ],
  rec=[
      ("¿Cómo se llama el punto de la superficie que está sobre el foco de un sismo?", "Epicentro", "Es la proyección vertical del hipocentro."),
      ("¿Qué dos placas interactúan en la subducción frente a Chile?", "Nazca y Sudamericana", "La placa de Nazca se hunde bajo la Sudamericana."),
      ("Verdadero o falso: un sismo tiene una magnitud distinta en cada ciudad.", "Falso", "La magnitud es un único valor para el sismo."),
  ],
  und=[
      ("La magnitud de un sismo mide: A) la energía liberada B) los daños observados en una ciudad", "A", "Los daños corresponden a la intensidad."),
      ("¿Qué escala usa números romanos de I a XII para describir efectos?", "La escala de Mercalli", "Mide la intensidad."),
      ("El hipocentro es: A) el punto del interior donde comienza la ruptura B) el punto de la superficie sobre el foco", "A", "El epicentro es el punto de la superficie."),
  ],
  app=[
      ex("El hipocentro está a 35 km de profundidad y el epicentro queda a 120 km de una ciudad, medidos sobre la superficie. ¿A qué distancia en línea recta está la ciudad del hipocentro?", "125 km", "El triángulo es rectángulo: 35 al cuadrado más 120 al cuadrado es 15.625, que es 125 al cuadrado."),
      arith("El área de ruptura de un sismo de ejemplo se aproxima por un rectángulo de 100 km de largo y 50 km de ancho. ¿Cuántos km² tiene?", "100*50", "El área de un rectángulo es largo por ancho.", " km²"),
      ("Un boletín de ejemplo dice: «Magnitud 6,5. Intensidad VII en la ciudad A e intensidad V en la ciudad B». ¿Cuántos valores de magnitud tiene el sismo?", "Uno", "La magnitud es única; solo la intensidad cambia según el lugar."),
  ],
  rea=[
      ("Pedro dice: «El terremoto fue de magnitud 8 en mi casa y de magnitud 6 en la casa de mi tía». ¿Qué corrección es correcta? A) La magnitud es única; lo que cambia es la intensidad B) La magnitud disminuye con la distancia", "A", "La magnitud describe el sismo en la fuente."),
      ("Dos sismos tienen igual magnitud: uno con hipocentro a 10 km bajo una ciudad y otro a 300 km de profundidad bajo la misma ciudad. ¿Cuál produce, en general, mayor intensidad en esa ciudad? A) El de 10 km B) El de 300 km", "A", "La energía llega con menos pérdida cuando el foco está cerca."),
  ],
  cha=[
      ("Un sismo se sintió en cuatro ciudades con intensidades V, VII, III y VI. Suponiendo suelos y construcciones parecidos, ¿qué ciudad estaba probablemente más cerca del epicentro?", "La de intensidad VII", "La intensidad suele ser mayor cerca del epicentro."),
      ex("Tu casa está a 30 km del epicentro, en la superficie, y el hipocentro está a 40 km de profundidad. ¿A qué distancia en línea recta de tu casa está el hipocentro?", "50 km", "30 al cuadrado más 40 al cuadrado es 2.500, que es 50 al cuadrado."),
  ],
  context=[ex("Nota de prensa de ejemplo: «Sismo de magnitud 6,2 con epicentro a 20 km de la costa. Intensidad V en la ciudad costera». ¿Qué valor de la nota describe al sismo en su fuente y cuál describe sus efectos en un lugar?", "La magnitud 6,2 describe la fuente; la intensidad V, los efectos en la ciudad", "La magnitud es única y la intensidad depende del lugar.")],
  selfcheck=[("¿Qué es el área de ruptura?", "La superficie de la falla que se desplazó", "Es mayor en los sismos más grandes."), ("¿Por qué se produce un sismo por subducción?", "Porque las placas se traban, acumulan energía y se rompen", "La energía liberada se propaga como ondas."), ("¿De qué depende la intensidad en un lugar?", "De la distancia, el tipo de suelo y las construcciones", "Por eso varía de ciudad en ciudad.")],
  open_task=task("Boletín de ejemplo: magnitud 7,2; profundidad 40 km; epicentro 30 km al oeste de la ciudad A (sobre el mar); intensidad VII en la ciudad A; intensidad IV en la ciudad B, a 300 km. Dibuja un corte lateral con la placa de Nazca hundiéndose bajo la Sudamericana y ubica hipocentro, epicentro y el área de ruptura. Calcula la distancia en línea recta de la ciudad A al hipocentro. Explica por qué la intensidad es distinta en A y en B.", "Distancia: 30 al cuadrado más 40 al cuadrado es 2.500 y su raíz es 50 km. A está más cerca de la fuente, por eso la intensidad es mayor (VII frente a IV); la magnitud, 7,2, es una sola.", ["dibujo con placas, hipocentro, epicentro y área de ruptura", "distancia de 50 km con el cálculo", "diferencia de intensidad explicada por la distancia", "distingue magnitud e intensidad"], ["dibujo rotulado y cálculo"], ["poner el epicentro bajo el hipocentro", "decir que la magnitud es distinta en A y B"], "Pregunta qué otro dato, además de la distancia, cambiaría la intensidad en la ciudad B."),
  reinforce="Escribe una frase que distinga magnitud e intensidad.",
  extend="Explica por qué dos ciudades a la misma distancia del epicentro pueden tener intensidades distintas.")

L(OA, 2,
  materials="Este cuaderno, lápiz, calculadora y, si quieres, un resorte largo de juguete sobre el piso o una cuerda. Los valores de rapidez son de ejemplo y están escritos en cada ejercicio.",
  use="Aprenderé a distinguir las ondas P, S y superficiales y a usar sus tiempos de llegada para calcular la distancia al epicentro. Sirve para entender un sismograma.",
  prior=["Sé que las ondas pueden ser longitudinales o transversales.", "Sé calcular distancia = rapidez × tiempo."],
  explain=[
      "La energía de un sismo se propaga como ondas. Las ondas de cuerpo viajan por el interior de la Tierra. Las ondas P, o primarias, son longitudinales: comprimen y expanden el material en la dirección en que avanzan. Son las más rápidas, llegan primero y atraviesan sólidos y líquidos. Las ondas S, o secundarias, son transversales: mueven el material de lado a lado. Son más lentas y solo atraviesan sólidos.",
      "Las ondas superficiales viajan por la superficie del terreno, como las ondas en un estanque. Son las más lentas, llegan al final, tienen mayor amplitud y causan la mayor parte de los daños. En un sismograma se ven en este orden: P, S y superficiales.",
      "Con los tiempos de llegada se calcula la distancia al epicentro. Si la rapidez de las ondas P es 6 km/s y la de las ondas S es 3 km/s (valores de ejemplo), el retardo entre S y P es: tiempo S menos tiempo P, es decir, d ÷ 3 − d ÷ 6, que es d ÷ 6. Entonces, la distancia en kilómetros es 6 veces el retardo en segundos. Con tres estaciones se ubica el epicentro.",
  ],
  vocab=[("onda P", "onda de cuerpo longitudinal, la más rápida, que llega primero"), ("onda S", "onda de cuerpo transversal, más lenta, que no atraviesa líquidos"), ("onda superficial", "onda que viaja por la superficie, lenta y de mayor amplitud"), ("onda longitudinal", "onda en que el material vibra en la dirección en que avanza"), ("onda transversal", "onda en que el material vibra perpendicular a la dirección en que avanza"), ("retardo S–P", "diferencia entre el tiempo de llegada de la onda S y el de la P")],
  worked=[
      ("Retardo S–P", "Una estación está a 120 km del epicentro. P viaja a 6 km/s y S a 3 km/s. ¿Cuál es el retardo?", ["Tiempo de P: 120 ÷ 6 = 20 s.", "Tiempo de S: 120 ÷ 3 = 40 s.", "Retardo: 40 − 20 = 20 s."], "20 s"),
      ("Qué onda no pasa", "¿Cuál de las ondas P o S no atraviesa un líquido?", ["Las ondas S son transversales y necesitan un material que resista el corte.", "Un líquido no lo hace."], "La onda S"),
  ],
  mistakes=[
      ("Creer que las ondas superficiales son las primeras en llegar porque están en la superficie.", "Son las más lentas y llegan al final, aunque son las más dañinas.", "Recuerda el orden P, S y superficiales."),
      ("Usar solo un tiempo de llegada para ubicar el epicentro.", "Un tiempo da solo una distancia, no una dirección.", "Se necesitan tres estaciones para ubicar el epicentro."),
  ],
  rec=[
      ("¿Qué onda sísmica llega primero a las estaciones?", "La onda P", "Es la más rápida."),
      ("La onda S es ______ (longitudinal o transversal).", "Transversal", "Mueve el material perpendicular a su avance."),
      ("Verdadero o falso: las ondas superficiales son las más rápidas.", "Falso", "Son las más lentas."),
  ],
  und=[
      ("A las ondas P se las llama primarias porque: A) llegan primero a las estaciones B) son las más destructivas", "A", "Su rapidez es mayor que la de las otras ondas."),
      ("¿Cómo mueve el terreno una onda P al pasar?", "Lo comprime y lo expande en la misma dirección en que avanza", "Es una onda longitudinal."),
      ("¿Qué ondas causan la mayor parte de los daños en la superficie?", "Las superficiales", "Tienen mayor amplitud y llegan al lugar donde hay construcciones."),
  ],
  app=[
      arith("Las ondas P viajan a 6 km/s y una estación está a 210 km del epicentro. ¿En cuántos segundos llegan las ondas P?", "210/6", "El tiempo es la distancia dividida por la rapidez.", " s"),
      arith("Una estación está a 90 km del epicentro. Las ondas P viajan a 6 km/s y las S a 3 km/s. ¿Cuántos segundos de retardo hay entre la llegada de S y la de P?", "90/3-90/6", "Se resta el tiempo de la onda P al tiempo de la onda S.", " s"),
      arith("Una estación mide un retardo S–P de 25 s. Si la distancia en kilómetros es 6 veces el retardo en segundos, ¿a cuántos kilómetros está el epicentro?", "6*25", "Se multiplica el retardo por 6.", " km"),
  ],
  rea=[
      ("En un sismograma de ejemplo aparecen primero oscilaciones pequeñas, luego unas mayores y, al final, unas grandes y lentas. ¿Qué ondas son las últimas? A) Las superficiales B) Las P", "A", "Las superficiales son las más lentas y de mayor amplitud."),
      ("Tomás dice: «Mientras más lejos está el epicentro, mayor es el retardo S–P». ¿Es correcto? A) Sí, porque la diferencia de tiempos crece con la distancia B) No, porque el retardo no depende de la distancia", "A", "La onda más lenta se atrasa más cuanto más camino recorre."),
  ],
  cha=[
      arith("Dos estaciones registran retardos S–P de 18 s y de 30 s. Si la distancia en kilómetros es 6 veces el retardo en segundos, ¿cuántos kilómetros más lejos del epicentro está la segunda estación?", "(30-18)*6", "Se resta un retardo del otro y se multiplica la diferencia por 6.", " km"),
      arith("Una estación está a 180 km del epicentro. Las ondas P viajan a 6 km/s y las superficiales a 2 km/s (valores de ejemplo). ¿Cuántos segundos después de las P llegan las superficiales?", "180/2-180/6", "Se calcula el tiempo de cada onda y se restan.", " s"),
  ],
  context=[arith("Una ciudad está a 240 km de un epicentro. Un sistema de alerta detecta las ondas P (6 km/s) y avisa antes de que lleguen las S (3 km/s). ¿Cuántos segundos hay entre la llegada de P y la de S para protegerse?", "240/3-240/6", "Es el retardo entre las dos ondas.", " s")],
  selfcheck=[("¿Cuál es el orden de llegada de las ondas?", "P, S y superficiales", "Va de la más rápida a la más lenta."), ("¿Qué onda es longitudinal?", "La P", "Comprime y expande en la dirección de avance."), ("¿Para qué sirven tres estaciones?", "Para ubicar el epicentro", "Cada una da una distancia.")],
  open_task=task("Con un resorte largo de juguete sobre el piso (o una cuerda), dos personas lo estiran. Empuja y suelta una punta en la dirección del resorte (como onda P) y luego muévela de lado a lado (como onda S); anota qué ves. Luego usa estos datos: tres estaciones registran retardos S–P de 10 s (A), 15 s (B) y 20 s (C). La distancia es 6 veces el retardo. Calcula las tres distancias, di cuál estación está más cerca del epicentro y explica por qué se necesitan tres estaciones para ubicarlo.", "Onda P: el resorte se comprime y se estira en la misma dirección en que avanza el pulso. Onda S: el resorte se mueve de lado. Distancias: A 60 km, B 90 km, C 120 km. La estación A es la más cercana. Una estación da solo una distancia (una circunferencia); con tres circunferencias que se cruzan se ubica el epicentro.", ["describe la onda longitudinal y la transversal", "tres distancias correctas", "identifica A como la más cercana", "explica que se necesitan tres estaciones"], ["descripción y cálculos"], ["confundir la dirección del movimiento en la onda longitudinal", "no multiplicar por 6"], "Pregunta qué pasaría con el retardo si el epicentro estuviera al doble de distancia."),
  reinforce="Escribe tres diferencias entre las ondas P y las S.",
  extend="Explica por qué un sismograma de una estación lejana muestra mayor separación entre las llegadas de P y S.")

L(OA, 3,
  materials="Este cuaderno, lápiz, calculadora y, si lo deseas, una caja, una cuerda y un lápiz para imaginar el sismógrafo del ejercicio. Los datos de sismos son de ejemplo.",
  use="Aprenderé cómo funciona un sismógrafo, qué es un sismograma y cómo se compara la magnitud de dos sismos. Sirve para interpretar noticias sobre sismos.",
  prior=["Sé la diferencia entre magnitud e intensidad.", "Sé que las ondas P llegan antes que las S."],
  explain=[
      "Un sismógrafo registra el movimiento del suelo. Tiene una masa suspendida que, por inercia, tiende a quedar casi quieta, y un soporte fijado al terreno que se mueve con el sismo. El movimiento relativo entre la masa y el soporte se registra en un sismograma, que es un gráfico del movimiento del suelo en el tiempo. Los sismógrafos actuales son sensores electrónicos que envían datos digitales. En Chile, el Centro Sismológico Nacional de la Universidad de Chile reúne los datos de una red de estaciones.",
      "La magnitud se calcula con la amplitud de las ondas registradas, corregida por la distancia. La escala es logarítmica: cuando la magnitud sube 1 unidad, la amplitud de las ondas registradas se multiplica por 10 y la energía liberada se multiplica por unas 32 veces. Entre magnitud 5 y magnitud 7 la amplitud es 100 veces mayor y la energía es unas 1.000 veces mayor.",
      "La intensidad se describe con la escala de Mercalli, que usa los efectos observados: I casi no se siente y XII es destrucción total. Para ubicar el epicentro se usa la triangulación: cada estación calcula su distancia al epicentro con el retardo S–P y se dibuja una circunferencia de ese radio; el epicentro está donde se cruzan las tres circunferencias.",
  ],
  vocab=[("sismógrafo", "instrumento que registra el movimiento del suelo"), ("sismograma", "gráfico del movimiento del suelo en el tiempo"), ("inercia", "tendencia de un cuerpo a mantener su estado de reposo o movimiento"), ("escala logarítmica", "escala en que cada paso multiplica la cantidad por un mismo número"), ("triangulación", "método que usa tres distancias para ubicar un punto"), ("escala de Mercalli", "escala de efectos observados, de I a XII")],
  worked=[
      ("Comparar amplitudes", "¿Cuántas veces es mayor la amplitud de un sismo de magnitud 6 que la de uno de magnitud 4?", ["Entre 4 y 6 hay 2 unidades.", "Cada unidad multiplica por 10.", "Calculo 10 × 10."], "100 veces"),
      ("Sismógrafo", "¿Por qué la masa del sismógrafo queda casi quieta cuando el suelo se mueve?", ["La masa tiene inercia.", "El soporte se mueve con el suelo y la masa tiende a mantenerse quieta."], "Por su inercia"),
  ],
  mistakes=[
      ("Pensar que magnitud 8 es solo el doble de magnitud 4.", "La escala es logarítmica: cada unidad multiplica la amplitud por 10.", "Cuenta cuántas unidades separan los sismos."),
      ("Creer que un sismograma muestra los daños del sismo.", "Muestra el movimiento del suelo en el tiempo; los daños se describen con la intensidad.", "Distingue registro del instrumento y efectos observados."),
  ],
  rec=[
      ("¿Cómo se llama el gráfico que produce un sismógrafo?", "Sismograma", "Registra el movimiento del suelo en el tiempo."),
      ("¿Qué mide la escala de Mercalli?", "La intensidad", "Se basa en efectos observados."),
      ("Verdadero o falso: la escala de magnitud es logarítmica.", "Verdadero", "Cada unidad multiplica la amplitud por 10."),
  ],
  und=[
      ("Cuando la magnitud aumenta 1 unidad, la amplitud de las ondas registradas: A) se multiplica por 10 B) aumenta en 1 unidad", "A", "Es una escala logarítmica."),
      ("La masa de un sismógrafo queda casi quieta porque: A) tiene inercia B) está pegada al suelo", "A", "Tiende a mantener su reposo cuando el soporte se mueve."),
      ("¿Cuántas estaciones se necesitan para ubicar un epicentro por triangulación?", "Tres", "Cada una aporta una circunferencia y se cruzan en un punto."),
  ],
  app=[
      arith("¿Cuántas veces es mayor la amplitud de las ondas de un sismo de magnitud 7 que la de uno de magnitud 4?", "10*10*10", "Hay 3 unidades de diferencia y cada una multiplica por 10.", " veces"),
      arith("Cada unidad de magnitud libera unas 32 veces más energía. Con ese valor, ¿cuántas veces más energía libera un sismo de magnitud 7 que uno de magnitud 5?", "32*32", "Hay 2 unidades de diferencia: 32 × 32 = 1.024, es decir, cerca de 1.000 veces.", " veces"),
      ("Una ciudad lejana del epicentro, de ejemplo, registra intensidad II con un sismo muy grande. ¿Es contradictorio? A) No, porque la intensidad disminuye con la distancia B) Sí, porque un sismo grande siempre produce intensidad alta", "A", "La intensidad depende del lugar, y lejos de la fuente es menor."),
  ],
  rea=[
      ("Un estudiante dice: «Magnitud 8 es solo el doble de magnitud 4». ¿Qué corrección es correcta? A) Son cuatro unidades de diferencia: la amplitud es 10.000 veces mayor B) Tiene razón porque 8 es el doble de 4", "A", "Cada unidad multiplica por 10; cuatro unidades dan 10 × 10 × 10 × 10."),
      ("Dos estaciones registran el mismo sismo: una mide 1 mm de amplitud y la otra 10 mm. ¿Cuál está, probablemente, más cerca del epicentro?", "La que registró 10 mm", "La amplitud disminuye con la distancia."),
  ],
  cha=[
      arith("¿Cuántas veces es mayor la amplitud de las ondas de un sismo de magnitud 8 que la de uno de magnitud 3?", "10*10*10*10*10", "Hay 5 unidades de diferencia y cada una multiplica por 10.", " veces"),
      ("Tres estaciones calculan distancias al epicentro de 50 km, 80 km y 100 km. ¿Dónde está el epicentro?", "En el punto donde se cruzan las tres circunferencias", "Cada distancia da una circunferencia y solo un punto cumple las tres."),
  ],
  context=[arith("Una aplicación de ejemplo muestra sismos de magnitud 3 y de magnitud 5. ¿Cuántas veces es mayor la amplitud registrada del segundo respecto del primero?", "10*10", "Hay 2 unidades de diferencia.", " veces")],
  selfcheck=[("¿Qué registra un sismógrafo?", "El movimiento del suelo", "El resultado es un sismograma."), ("¿Qué significa que la escala sea logarítmica?", "Que cada unidad multiplica la amplitud por 10", "No crece de forma lineal."), ("¿Para qué sirve la escala de Mercalli?", "Para describir los efectos de un sismo en un lugar", "Va de I a XII.")],
  open_task=task("Dibuja un sismógrafo simple: un soporte fijo al suelo, un lápiz sujeto a una masa suspendida de un hilo y un papel pegado al soporte que se mueve con el suelo. Explica por qué el lápiz traza una línea cuando el suelo se mueve. Después usa este sismograma de ejemplo: la onda P llega a los 8 s y la S a los 20 s. Calcula el retardo y la distancia, sabiendo que la distancia en kilómetros es 6 veces el retardo en segundos.", "La masa con el lápiz tiene inercia y se mantiene casi quieta; el papel se mueve con el suelo y el lápiz dibuja la diferencia. Retardo: 20 − 8 = 12 s. Distancia: 6 × 12 = 72 km.", ["dibujo con masa, hilo, lápiz y papel", "explica con la inercia", "retardo de 12 s", "distancia de 72 km"], ["dibujo y cálculo"], ["no usar la inercia en la explicación", "restar al revés los tiempos"], "Pregunta cómo identificarías en el sismograma de otra estación el sismo más intenso."),
  reinforce="Calcula cuántas veces es mayor la amplitud de un sismo de magnitud 8 que la de uno de magnitud 7.",
  extend="Explica por qué se usan varias estaciones y no una sola para ubicar el epicentro.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Los datos y mapas de los ejercicios son de ejemplo y están escritos; el plan de evacuación se completa con una persona adulta de tu casa.",
  use="Aprenderé las consecuencias directas e indirectas de un sismo, cómo se forma un tsunami y cómo prepararse. Sirve para tomar decisiones seguras.",
  prior=["Sé que los sismos se originan por la ruptura de rocas.", "Sé que la rapidez es distancia dividida por tiempo."],
  explain=[
      "Las consecuencias directas son efectos causados por el sismo mismo: la vibración del suelo, grietas, deslizamientos de tierra, licuefacción (suelo saturado de agua que se comporta como líquido) y daños en edificios y puentes. Las consecuencias indirectas aparecen después, como efecto de las primeras: incendios por cortocircuitos, cortes de agua, luz y comunicaciones, problemas de salud, pérdidas económicas y tsunamis.",
      "Un tsunami es un conjunto de olas muy largas que se forma cuando un sismo submarino, cerca de la costa, levanta o hunde bruscamente el fondo y mueve una gran masa de agua. En mar abierto sus olas son bajas, pero muy rápidas: pueden llevar unos 700 km/h. Al llegar a la costa el fondo es menos profundo, la ola se frena y su altura aumenta. Llegan varias olas y la primera no siempre es la mayor; a veces el mar se retira antes. Si estás en la costa y el sismo es tan fuerte que cuesta mantenerse en pie, o hay una alerta oficial, hay que evacuar de inmediato, a pie, a una zona alta.",
      "Chile está en una zona sísmica y ha tenido grandes terremotos, como el de Valdivia de 1960, el mayor registrado en el mundo con instrumentos, y el del Maule de 2010. Por eso se usan normas de construcción sismorresistente, vías de evacuación señalizadas y simulacros. Tener un plan familiar, una mochila de emergencia y conocer la zona segura reduce los riesgos.",
  ],
  vocab=[("consecuencia directa", "efecto causado por el sismo mismo, como grietas o caída de muros"), ("consecuencia indirecta", "efecto que aparece después como resultado de las consecuencias directas"), ("licuefacción", "pérdida de firmeza de un suelo saturado de agua por la vibración"), ("tsunami", "conjunto de olas muy largas causado por un sismo submarino u otra perturbación del fondo"), ("sismorresistente", "diseñado para soportar sismos sin colapsar"), ("zona de evacuación", "lugar alto y seguro hacia donde ir tras una alerta de tsunami")],
  worked=[
      ("Directa o indirecta", "Clasifica: grietas en el pavimento, incendio por una tubería de gas rota, caída de un muro.", ["Grietas y caída de muro ocurren por la vibración misma.", "El incendio ocurre después, por una falla provocada por el sismo."], "Grietas y muro, directas; incendio, indirecta"),
      ("Tiempo de llegada", "Una ola de tsunami viaja a 700 km/h y debe recorrer 1.400 km. ¿Cuánto tarda?", ["Uso tiempo = distancia ÷ rapidez.", "Calculo 1.400 ÷ 700."], "2 horas"),
  ],
  mistakes=[
      ("Pensar que, si el mar se retira, hay que acercarse a ver.", "El retiro del mar puede ser una señal de tsunami; hay que evacuar de inmediato.", "Ante un sismo fuerte en la costa o una alerta oficial, sube a pie a la zona alta."),
      ("Creer que el tsunami es solo una ola gigante.", "Es una serie de olas y la primera no siempre es la mayor.", "No vuelvas hasta que las autoridades indiquen que es seguro."),
  ],
  rec=[
      ("¿Qué tipo de sismo suele generar un tsunami: submarino cerca de la costa o profundo bajo una cordillera?", "Submarino cerca de la costa", "Mueve el fondo del mar y la masa de agua."),
      ("Verdadero o falso: la licuefacción es una consecuencia directa de la vibración del suelo.", "Verdadero", "Ocurre en el suelo durante el sismo."),
      ("Si hay alerta oficial de tsunami en la costa, ¿qué debes hacer?", "Evacuar a pie a una zona alta", "Hay que alejarse del mar sin esperar."),
  ],
  und=[
      ("Un cerro cercano al epicentro se desliza por la vibración del suelo. ¿Es una consecuencia directa o indirecta?", "Directa", "Es un efecto inmediato de la vibración."),
      ("¿Por qué la ola de un tsunami crece al llegar a la costa? A) El fondo menos profundo la frena y su altura aumenta B) El viento la empuja", "A", "Al frenarse, la energía se concentra en una ola más alta."),
      ("¿La primera ola de un tsunami es siempre la más grande?", "No", "Llegan varias olas y cualquiera puede ser la mayor."),
  ],
  app=[
      arith("Una ola de tsunami viaja a 700 km/h. ¿Cuántas horas tarda en recorrer 2.100 km?", "2100/700", "El tiempo es distancia dividida por rapidez.", " h"),
      arith("La zona segura de ejemplo está a 30 m sobre el nivel del mar y una casa está a 8 m. ¿Cuántos metros hay que subir?", "30-8", "Se resta la altura de la casa a la altura segura.", " m"),
      ("Tras un sismo fuerte en la costa suena una alerta oficial de tsunami. Una persona dice «voy a mirar cómo está el mar». ¿Qué corresponde? A) Evacuar a pie a la zona alta sin esperar B) Esperar a ver una ola grande", "A", "Cuando se ve la ola ya es tarde para evacuar."),
  ],
  rea=[
      ("Un compañero propone acercarse al mar cuando se retira, para recoger conchas. ¿Qué respuesta es correcta? A) No: el retiro del mar es una señal de tsunami y hay que alejarse B) Sí: el agua retirada no es peligrosa", "A", "Después del retiro puede llegar una ola grande."),
      ("Dos ciudades reciben la misma vibración del suelo, pero una tiene edificios sismorresistentes. ¿Cuál tiene menos daños? A) La de edificios sismorresistentes porque se deforman sin colapsar B) La otra, porque recibe menos ondas", "A", "El diseño reduce los daños aunque la vibración sea la misma."),
  ],
  cha=[
      arith("Un tsunami viaja a 720 km/h en mar abierto y a 36 km/h cerca de la costa. ¿Cuántas veces disminuye su rapidez?", "720/36", "Se divide la rapidez en mar abierto por la rapidez cerca de la costa.", " veces"),
      arith("El epicentro de un sismo submarino está a 90 km de la costa y la ola viaja a 180 km/h. ¿Cuántos minutos tarda en llegar?", "90/180*60", "Primero se calcula el tiempo en horas (0,5 h) y se convierte a minutos.", " minutos"),
  ],
  context=[arith("La zona segura de una familia de ejemplo está a 600 m de la casa y se camina a 60 m por minuto. ¿Cuántos minutos se tarda en llegar?", "600/60", "El tiempo es la distancia dividida por la rapidez al caminar.", " minutos")],
  selfcheck=[("¿Qué es un tsunami?", "Un conjunto de olas largas causado por un sismo submarino", "Se produce cuando el fondo se mueve bruscamente."), ("Da un ejemplo de consecuencia indirecta de un sismo.", "Un incendio o un corte de agua", "Aparecen como efecto de otras consecuencias."), ("¿Qué hay que hacer tras un sismo fuerte en la costa?", "Evacuar a una zona alta a pie", "El tsunami puede llegar en pocos minutos.")],
  open_task=task("Con una persona adulta de tu casa, escriban un plan de ejemplo de cinco pasos para un sismo fuerte. Usa estos datos: la casa está a 6 m sobre el nivel del mar, la zona segura está a 40 m, la ruta mide 800 m y se camina a 80 m por minuto. Calcula cuánto tarda la ruta, cuántos metros hay que subir y nombra una consecuencia directa y una indirecta que el plan ayudaría a enfrentar.", "Ruta: 800 ÷ 80 = 10 minutos. Altura: 40 − 6 = 34 m. Pasos: protegerse durante el sismo, evacuar a pie si es en la costa, llevar mochila de emergencia, seguir la ruta señalizada y quedarse en la zona alta. Directa: caída de objetos. Indirecta: tsunami.", ["calcula 10 minutos", "calcula 34 m", "cinco pasos coherentes", "una consecuencia directa y una indirecta"], ["plan escrito y cálculos"], ["usar auto para evacuar", "confundir consecuencia directa con indirecta"], "Pregunta qué dato del plan cambiarías si la ruta tuviera una cuesta empinada."),
  reinforce="Escribe una consecuencia directa y una indirecta de un sismo fuerte.",
  extend="Explica por qué la ola del tsunami es poco visible en mar abierto, pero muy alta en la costa.")

L(OA, 5,
  materials="Este cuaderno, lápiz y calculadora. Los datos del interior de la Tierra están redondeados y escritos en los ejercicios.",
  use="Aprenderé cómo las ondas sísmicas revelan la estructura interna de la Tierra y los límites de las placas. Sirve para entender cómo se estudia lo que no se puede ver.",
  prior=["Sé que las ondas S no atraviesan líquidos.", "Sé que las ondas se reflejan y se refractan al cambiar de medio."],
  explain=[
      "Nadie ha podido perforar hasta el centro de la Tierra: el pozo más profundo llega a unos 12 km. La estructura interna se conoce estudiando cómo viajan las ondas sísmicas. Al cambiar de material, las ondas cambian de rapidez, se refractan o se reflejan, y las estaciones de todo el mundo registran esos cambios.",
      "El interior tiene capas. La corteza es delgada: unos 5 a 10 km bajo los océanos y hasta unos 70 km bajo las cordilleras. El manto es roca sólida que fluye muy lentamente y llega a unos 2.900 km de profundidad. El núcleo externo, de hierro y níquel, es líquido, porque las ondas S no lo atraviesan: tras un gran sismo, las estaciones al otro lado de la Tierra no registran ondas S. El núcleo interno es sólido por la enorme presión, aunque está muy caliente. El límite entre la corteza y el manto se llama discontinuidad de Mohorovičić (Moho).",
      "Los sismos también muestran dónde están los bordes de las placas. Si se marcan los epicentros en un mapa, forman franjas, como el Cinturón de Fuego del Pacífico, donde está Chile. Bajo Chile, los hipocentros son más profundos hacia el este, siguiendo la placa de Nazca que se hunde. Esta información se usa para evaluar el riesgo sísmico y diseñar construcciones.",
  ],
  vocab=[("corteza", "capa externa y delgada de la Tierra"), ("manto", "capa de roca sólida que fluye lentamente bajo la corteza"), ("núcleo externo", "capa líquida de hierro y níquel bajo el manto"), ("núcleo interno", "esfera sólida en el centro de la Tierra"), ("discontinuidad de Mohorovičić", "límite entre la corteza y el manto, llamado Moho"), ("Cinturón de Fuego", "franja alrededor del océano Pacífico con muchos sismos y volcanes")],
  worked=[
      ("Una capa líquida", "Tras un gran sismo, las estaciones al otro lado de la Tierra registran ondas P pero no ondas S. ¿Qué indica?", ["Las ondas S no atraviesan líquidos.", "Algo en el camino impidió su paso: hay una capa líquida en el interior."], "Que existe una capa líquida: el núcleo externo"),
      ("Profundidad de los hipocentros", "Los hipocentros de una zona están a 10 km de profundidad en la costa, a 50 km de profundidad 100 km al este de la costa y a 100 km de profundidad 200 km al este de la costa. ¿Qué indican?", ["La profundidad aumenta hacia el este.", "Siguen la placa que se hunde."], "Que una placa se hunde hacia el este"),
  ],
  mistakes=[
      ("Creer que se conoce el interior de la Tierra por haber perforado hasta el centro.", "La perforación más profunda llega a unos 12 km; el interior se estudia con ondas.", "Piensa en el sismo como una «linterna» que atraviesa el planeta."),
      ("Pensar que el núcleo interno es líquido porque está muy caliente.", "La presión es tan alta que se mantiene sólido.", "Recuerda que temperatura y presión actúan juntas."),
  ],
  rec=[
      ("¿Qué capa de la Tierra es líquida?", "El núcleo externo", "Las ondas S no la atraviesan."),
      ("Verdadero o falso: la corteza es la capa más delgada de la Tierra.", "Verdadero", "Mide entre unos 5 y 70 km."),
      ("¿Qué onda sísmica no atraviesa el núcleo externo?", "La onda S", "No viaja por líquidos."),
  ],
  und=[
      ("¿Qué evidencia indica que el núcleo externo es líquido? A) Las ondas S no lo atraviesan B) Las ondas P viajan más rápido en la corteza", "A", "Un líquido no transmite ondas transversales."),
      ("Los epicentros del mundo se agrupan en franjas porque: A) marcan límites entre placas B) están distribuidos al azar", "A", "Los sismos ocurren donde las placas interactúan."),
      ("¿Cómo se llama el límite entre la corteza y el manto?", "Discontinuidad de Mohorovičić (Moho)", "Allí cambia la rapidez de las ondas."),
  ],
  app=[
      arith("El radio de la Tierra es de unos 6.400 km y el manto llega a unos 2.900 km de profundidad (valores redondeados). ¿Cuál es el radio aproximado del núcleo completo (núcleo externo e interno juntos)?", "6400-2900", "El núcleo comienza donde termina el manto: se resta su profundidad al radio.", " km"),
      ("Profundidad de los hipocentros de ejemplo: costa, 10 km; 100 km al este, 60 km; 200 km al este, 110 km; 300 km al este, 160 km. ¿Cuántos kilómetros aumenta la profundidad por cada 100 km hacia el este?", "50 km", "La profundidad crece 50 km en cada tramo de 100 km."),
      ("Las estaciones registran un cambio brusco en la rapidez de las ondas sísmicas a unos 2.900 km de profundidad. ¿Qué indica?", "Que allí cambia el material", "Las ondas cambian de rapidez al pasar de un material a otro."),
  ],
  rea=[
      ("Alguien dice que se conoce el interior de la Tierra perforando hasta el centro. ¿Qué respuesta es correcta? A) No: el pozo más profundo llega a unos 12 km y se usan ondas sísmicas B) Sí: ya se perforó el manto completo", "A", "Las ondas permiten estudiar zonas inaccesibles."),
      ("Dos modelos: uno de Tierra sólida y homogénea, y otro de Tierra con capas. ¿Cuál explica que las ondas S no lleguen al lado opuesto? A) El de capas B) El homogéneo", "A", "Requiere una capa líquida que bloquee las ondas S."),
  ],
  cha=[
      arith("La corteza continental mide unos 40 km de espesor y el radio de la Tierra es de unos 6.400 km. ¿Cuántas veces cabe el espesor de la corteza en el radio?", "6400/40", "Se divide el radio por el espesor.", " veces"),
      ("El núcleo interno está más caliente que el externo, pero es sólido. ¿Por qué?", "Por la enorme presión", "La presión extrema mantiene los átomos juntos."),
  ],
  context=[arith("Una estación de Santiago registra un retardo S–P de 30 s en un sismo de ejemplo. Con ondas P de 6 km/s y S de 3 km/s, la distancia en kilómetros es 6 veces el retardo. ¿A cuántos kilómetros ocurrió?", "6*30", "Se multiplica el retardo por 6.", " km")],
  selfcheck=[("¿Cómo se conoce la estructura interna de la Tierra?", "Con las ondas sísmicas registradas en muchas estaciones", "Las ondas cambian de rapidez al cambiar de material."), ("¿Qué capa es sólida y está en el centro?", "El núcleo interno", "La presión lo mantiene sólido."), ("¿Qué caracteriza al Cinturón de Fuego del Pacífico?", "Una franja alrededor del Pacífico con muchos sismos y volcanes", "Coincide con bordes de placas.")],
  open_task=task("Datos redondeados de profundidades: la corteza llega hasta 40 km; el manto hasta 2.900 km; el núcleo externo hasta 5.100 km; el núcleo interno hasta 6.400 km (el centro). Dibuja un círculo con cuatro capas rotuladas y escribe el estado de cada una. Calcula el espesor del núcleo externo y el radio del núcleo interno. Explica qué evidencia sísmica muestra que el núcleo externo es líquido.", "Corteza y manto sólidos; núcleo externo líquido; núcleo interno sólido. Espesor del núcleo externo: 5.100 − 2.900 = 2.200 km. Radio del núcleo interno: 6.400 − 5.100 = 1.300 km. Evidencia: las ondas S no atraviesan el núcleo externo.", ["cuatro capas rotuladas con su estado", "2.200 km", "1.300 km", "usa las ondas S como evidencia"], ["dibujo y cálculos"], ["decir que el núcleo interno es líquido", "olvidar la evidencia de las ondas S"], "Pregunta qué otra onda daría información sobre el núcleo."),
  reinforce="Escribe las cuatro capas de la Tierra, de la superficie al centro, y su estado.",
  extend="Explica cómo se usan los sismos para saber por dónde se hunde una placa bajo el continente.")

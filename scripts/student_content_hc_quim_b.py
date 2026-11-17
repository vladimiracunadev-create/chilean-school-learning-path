"""Química (electivo 3.º y 4.º medio HC): OAC-03 (termodinámica y cinética, clases 1 a 5) y OAC-04 (cambio climático, ciclos biogeoquímicos y equilibrios, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado o en la ficha de la clase. "
             "Este cuaderno no propone experimentos, mezclas ni procedimientos con sustancias: los resultados que se analizan vienen ya escritos y los cálculos se hacen en papel. "
             "Las masas atómicas y las constantes que se usan se entregan en cada ficha; si necesitas otras, pídelas a tu docente. Ante cualquier duda sobre sustancias reales, consulta a tu docente y nunca manipules productos químicos por tu cuenta.")
build = make_build(MATERIALS)

O3 = "CN-QUIM-3y4-OAC-03"
O4 = "CN-QUIM-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (datos de ejemplo). Tipos de sistema: abierto (intercambia materia y energía con el entorno), cerrado (intercambia energía pero no materia) y aislado (no intercambia ninguna de las dos). "
     "Calor absorbido o liberado por una masa de agua: q = m × c × ΔT, con c = 4 J/(g·°C) (valor aproximado que se entrega). "
     "Reacciones de ejemplo (variación de entalpía ΔH por mol): R1: ΔH = −50 kJ; R2: ΔH = +30 kJ; R3: ΔH = −120 kJ. ΔH negativo significa que la reacción libera energía al entorno; ΔH positivo, que la absorbe. "
     "Tres preguntas de ejemplo: P1 «¿Qué pasa con la energía en la naturaleza?». P2 «¿Cuánto sube la temperatura de una masa de agua que absorbe la energía liberada por una reacción?». P3 «¿Es la termodinámica más importante que la cinética?».")
build(
    O3, 1, F,
    use="Aprenderé a delimitar una pregunta sobre energía y velocidad de reacciones en un sistema natural, distinguiendo qué responde la termodinámica y qué responde la cinética. Sirve para argumentar con evidencia cómo funcionan los sistemas y cómo responden a los cambios.",
    prior=["Sé qué es una reacción química.", "Sé usar unidades de energía como joule (J) y kilojoule (kJ).", "Sé la diferencia entre un dato y una conclusión."],
    explain=[
        "La termodinámica química estudia los intercambios de energía en las reacciones y si un proceso puede ocurrir por sí solo, es decir, si es espontáneo. La cinética química estudia la velocidad: qué tan rápido ocurre una reacción y de qué depende. Son dos preguntas distintas. Una reacción puede ser espontánea y, aun así, muy lenta, como la oxidación de una pieza de hierro seca, que tarda años.",
        "La entalpía (ΔH) mide el calor intercambiado en una reacción a presión constante. Si ΔH es negativo, la reacción es exotérmica: libera energía. Si es positivo, es endotérmica: absorbe energía. El calor que gana o pierde una masa de agua se calcula con q = m × c × ΔT, donde ΔT es el cambio de temperatura. Si el agua absorbe 2.400 J y tiene 200 g, la temperatura sube 2.400 ÷ (200 × 4) = 3 °C.",
        "Para argumentar con evidencia hay que delimitar el sistema, que puede ser abierto, cerrado o aislado. Un lago es un sistema abierto: intercambia agua, gases y energía con la atmósfera. Una buena pregunta nombra el sistema, la variable que se mide y la rama que la responde. «¿Qué pasa con la energía en la naturaleza?» es demasiado amplia para contestarse con datos.",
    ],
    vocab=[("espontáneo", "proceso que ocurre por sí solo, sin aporte continuo de energía externa"), ("exotérmica", "reacción que libera energía al entorno (ΔH negativo)"), ("endotérmica", "reacción que absorbe energía del entorno (ΔH positivo)"), ("sistema abierto", "sistema que intercambia materia y energía con el entorno"), ("velocidad de reacción", "cambio de la cantidad de reactivo o producto por unidad de tiempo")],
    worked=[
        ("Calor y temperatura", "Una reacción libera 4.800 J y esa energía la absorben 300 g de agua. ¿Cuánto sube la temperatura del agua?",
         ["Se usa q = m × c × ΔT, entonces ΔT = q ÷ (m × c).", "m × c = 300 × 4 = 1.200 J por grado.", "ΔT = 4.800 ÷ 1.200 = 4 °C."],
         "Sube 4 °C"),
        ("Qué rama responde", "¿Qué rama responde «¿cuántos segundos tarda en consumirse la mitad de un reactivo?»?",
         ["La pregunta trata del tiempo, es decir, de qué tan rápido ocurre.", "La rapidez es el tema de la cinética.", "La termodinámica trata de la energía y de si el proceso es espontáneo."],
         "La cinética"),
    ],
    mistakes=[("Pensar que si una reacción es espontánea, entonces es rápida.", "Espontáneo habla de si ocurre por sí sola; la rapidez la estudia la cinética.", "Pregunta por separado: ¿ocurre? (termodinámica) y ¿qué tan rápido? (cinética)."),
              ("Creer que ΔH negativo significa que la reacción «pierde» algo importante.", "ΔH negativo solo indica que se libera energía hacia el entorno.", "Interpreta el signo: negativo es exotérmica y positivo es endotérmica.")],
    T=[
        ("abc", "En Química: ¿qué estudia la termodinámica química?", "Los intercambios de energía y si un proceso puede ocurrir por sí solo", "La velocidad con que ocurre una reacción", "La cantidad de átomos de un elemento", "La termodinámica trata de energía y espontaneidad, no de rapidez."),
        ("{F} ¿Qué reacción de la ficha (R1, R2 o R3) libera más energía por mol?", "R3", "R3 tiene ΔH = −120 kJ, el valor negativo de mayor tamaño."),
        ("{F} ¿La reacción R2 absorbe o libera energía?", "Absorbe energía", "Su ΔH es +30 kJ, positivo, así que es endotérmica y absorbe energía."),
        ("abc", "{F} Un lago intercambia agua, gases y energía con la atmósfera. ¿Qué tipo de sistema es?", "Abierto", "Cerrado", "Aislado", "Un sistema que intercambia materia y energía con el entorno es abierto."),
        ("=", "{F} Una reacción libera 6.000 J y los absorben 250 g de agua. ¿Cuántos °C sube la temperatura?", "6000/(250*4)", "Se divide la energía por el producto de la masa y el valor de c entregado.", " °C"),
        ("=", "{F} ¿Cuántos joules absorben 150 g de agua cuando su temperatura sube 6 °C?", "150*4*6", "Se multiplican masa, c y cambio de temperatura según q = m × c × ΔT.", " J"),
        ("ab", "¿Cuál de estas preguntas se responde con cinética?", "¿Cuántos segundos tarda en consumirse la mitad del reactivo?", "¿La reacción libera o absorbe energía?", "La cinética mide cuánto tarda una reacción, no el signo de la energía."),
        ("abc", "{F} ¿Por qué P3 «¿Es la termodinámica más importante que la cinética?» está mal delimitada?", "Compara dos ramas que responden preguntas distintas y no nombra sistema ni variable medible", "Porque nombra la cinética", "Porque es demasiado corta", "Una pregunta delimitada necesita sistema y variable; P3 compara ramas sin datos."),
        ("abc", "Una pieza de hierro seca se oxida sola, pero tarda años en mostrar óxido visible. ¿Cómo se explica?", "El proceso es espontáneo, pero su velocidad es muy baja", "Si es lento, entonces no es espontáneo", "Si es espontáneo, siempre es rápido", "Espontáneo y rápido son ideas distintas: una es energía, la otra es tiempo."),
        ("=", "{F} Se tienen 4 mol de R3. ¿Cuántos kJ de energía libera en total?", "120*4", "La energía total es la energía por mol por el número de mol; R3 libera 120 kJ por mol.", " kJ"),
        ("abc", "Quieres estudiar cuánto se calienta un estanque de ejemplo en un día de sol. ¿Qué sistema delimita mejor?", "El agua del estanque, con su masa, su temperatura inicial y la energía que recibe", "Toda la energía del universo", "El clima de todas las regiones", "Un sistema acotado permite medir masa, temperatura y energía."),
        ("ab", "{F} Un estudiante dice: «ΔH negativo significa que la reacción es rápida». ¿Qué corrige?", "El signo de ΔH habla de la energía intercambiada; la rapidez es tema de la cinética", "Tiene razón: libera energía, así que es rápida", "ΔH se refiere a energía y no dice nada sobre el tiempo que tarda."),
        ("=", "{F} Una reacción libera 12.000 J y el agua que los absorbe sube 6 °C. ¿Cuántos gramos de agua eran?", "12000/(4*6)", "Se despeja la masa dividiendo la energía por el producto de c y el cambio de temperatura.", " g"),
    ],
    ctx=("abc", "Contexto: en una planta de tratamiento de ejemplo, una reacción libera energía y calienta el agua del estanque. La jefa pregunta cuánto se calentará en una hora. ¿Qué pregunta de investigación es la mejor?", "¿Cuánto sube la temperatura de los 5.000 kg de agua del estanque por hora con la energía que libera la reacción?", "¿Es buena la energía de las reacciones?", "¿Qué hace la química en el mundo?", "La mejor pregunta nombra el sistema, la variable que se mide y la unidad de tiempo."),
    sc=[
        ("En Química: ¿qué es una reacción exotérmica?", "Una que libera energía al entorno", "En una reacción exotérmica ΔH es negativo."),
        ("ab", "La velocidad de una reacción es tema de:", "La cinética", "La termodinámica", "La cinética mide cuánto tarda una reacción."),
        ("ab", "Un lago que intercambia agua y gases con el aire es un sistema:", "Abierto", "Aislado", "El lago intercambia materia y energía con el entorno."),
    ],
    op=("Con los datos de la ficha {F}: (1) elige un sistema natural (lago, suelo, glaciar u océano); (2) escribe una pregunta de termodinámica y otra de cinética sobre él; (3) indica qué variable medirías en cada una y qué dato de la ficha usarías para calcular algo.",
        "(1) Lago. (2) Termodinámica: ¿cuánto sube la temperatura de 1.000 g de agua del lago si absorbe 8.000 J? Cinética: ¿cómo cambia con la temperatura el tiempo en que se consume la mitad del oxígeno disuelto? (3) Mediría temperatura y tiempo; usaría q = m × c × ΔT con c = 4.",
        ["sistema elegido", "una pregunta de cada rama", "variable de cada una", "uso de un dato de la ficha"],
        ["tres respuestas numeradas"],
        ["mezclar las dos ramas en una pregunta", "no nombrar el sistema", "no usar ningún dato"],
        "Pregunta: «¿qué dato nuevo necesitarías para responder la pregunta de cinética?»."),
    reinforce="Escribe tres reacciones de ejemplo con ΔH distinto y clasifícalas como exotérmicas o endotérmicas, indicando cuál libera más energía.",
    extend="Explica con tus palabras por qué una reacción puede ser espontánea y muy lenta, y qué rama estudia cada característica.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (datos de ejemplo de un estudio ya realizado; solo se analizan los datos). Un reactivo A se consume en una reacción en disolución a 20 °C; concentración [A] en mmol/L: tiempo 0 s: 100; 10 s: 80; 20 s: 64; 30 s: 52. "
     "Velocidad media en un intervalo = (disminución de [A]) ÷ (tiempo del intervalo). Efecto de la temperatura (misma concentración inicial y mismo reactivo): velocidad inicial a 20 °C: 2 mmol/(L·s); a 30 °C: 4; a 40 °C: 8. Con un catalizador a 20 °C: 6 mmol/(L·s). "
     "Fuente A: informe con método descrito, tabla de datos y réplica del resultado. Fuente B: afirmación sin datos: «cualquier reacción duplica su velocidad cada 10 °C».")
build(
    O3, 2, F,
    use="Aprenderé a evaluar fuentes y variables de un estudio de cinética: qué se cambia, qué se mide y cómo se calcula una velocidad de reacción. Sirve para argumentar con datos cómo la temperatura, la concentración y un catalizador influyen en la velocidad.",
    prior=["Sé qué es una variable independiente y dependiente.", "Sé calcular una diferencia y dividir.", "Sé qué es una concentración."],
    explain=[
        "La velocidad media de una reacción es el cambio de concentración dividido por el tiempo. Si un reactivo baja de 100 a 80 mmol/L en 10 s, su velocidad media es 20 ÷ 10 = 2 mmol/(L·s). Con el tiempo, el reactivo se consume y su concentración baja, por eso la velocidad media suele disminuir a lo largo de la reacción.",
        "La velocidad depende de varios factores. Al subir la temperatura, las partículas se mueven más rápido, chocan más veces y más de ellas tienen la energía suficiente, así que la velocidad aumenta. Al subir la concentración, hay más choques por segundo. Un catalizador acelera la reacción por un camino de menor energía de activación y no se consume. Para saber qué factor causa un cambio, hay que variar solo uno y mantener controlados los otros.",
        "Al evaluar una fuente se mira si describe método y datos y si el resultado se repitió. Una regla general, como «se duplica cada 10 °C», es una aproximación que no se cumple siempre y no sustituye a los datos de la reacción estudiada. Además, una predicción fuera del rango medido, por ejemplo a 50 °C, no tiene respaldo en la tabla.",
    ],
    vocab=[("velocidad media", "disminución de reactivo (o aumento de producto) dividida por el tiempo"), ("catalizador", "sustancia que acelera una reacción sin consumirse"), ("variable controlada", "la que se mantiene igual en todo el estudio"), ("rango medido", "intervalo de valores en que sí hay datos"), ("réplica", "repetición independiente de un resultado")],
    worked=[
        ("Velocidad media", "Con la tabla de la ficha, ¿cuál es la velocidad media entre 0 y 20 s?",
         ["Disminución de [A]: 100 − 64 = 36 mmol/L.", "Tiempo del intervalo: 20 s.", "Velocidad: 36 ÷ 20 = 1,8 mmol/(L·s)."],
         "1,8 mmol/(L·s)"),
        ("Variable independiente", "En la comparación con y sin catalizador a 20 °C de la ficha, ¿qué variable se cambió?",
         ["Se comparó la misma reacción con y sin catalizador.", "Lo que decidió el estudio fue agregar o no el catalizador.", "Esa es la variable independiente; la velocidad es la dependiente."],
         "La presencia del catalizador"),
    ],
    mistakes=[("Dar por cierta la regla «se duplica cada 10 °C» para cualquier reacción.", "Es una aproximación que depende de cada reacción y no se cumple siempre.", "Usa los datos de la reacción estudiada y declara el rango medido."),
              ("Predecir a 50 °C extendiendo la tabla.", "No hay mediciones a 50 °C y la tendencia podría cambiar.", "Escribe «no hay datos para esa temperatura».")],
    T=[
        ("abc", "En Química: ¿qué es la velocidad media de una reacción?", "El cambio de concentración dividido por el tiempo", "La suma de las concentraciones", "La temperatura máxima alcanzada", "La velocidad mide cuánto cambia una cantidad por unidad de tiempo."),
        ("{F} ¿Cuál era la concentración de A a los 30 s?", "52 mmol/L", "El valor de la tabla para 30 s es 52 mmol/L."),
        ("{F} En el estudio de la temperatura, ¿cuál es la variable independiente?", "La temperatura", "Es la que se cambió entre 20, 30 y 40 °C para ver su efecto."),
        ("=", "{F} ¿Cuál es la velocidad media entre 0 y 10 s?", "(100-80)/10", "Se divide la disminución de [A] por el tiempo del intervalo.", " mmol/(L·s)"),
        ("=", "{F} ¿Cuál es la velocidad media entre 10 y 20 s?", "(80-64)/10", "Se divide la disminución de [A] en ese intervalo por 10 s.", " mmol/(L·s)"),
        ("=", "{F} ¿Cuántas veces mayor es la velocidad inicial a 40 °C que a 20 °C?", "8/2", "Se divide la velocidad inicial a 40 °C por la velocidad inicial a 20 °C.", " veces"),
        ("abc", "{F} ¿Por qué la velocidad media de la reacción disminuye de un intervalo al siguiente a lo largo de los 30 s?", "Porque el reactivo se va consumiendo y su concentración baja", "Porque la temperatura baja con el tiempo", "Porque el catalizador se gasta", "A temperatura constante, menos reactivo significa menos choques por segundo."),
        ("=", "{F} ¿Cuántas veces mayor es la velocidad inicial con catalizador que sin él, a 20 °C?", "6/2", "Se divide la velocidad con catalizador por la velocidad sin catalizador.", " veces"),
        ("abc", "{F} ¿Qué problema tiene la afirmación de la fuente B?", "Generaliza a cualquier reacción sin datos; es una regla aproximada que no siempre se cumple", "Que usa números", "Que habla de temperatura", "Una regla general sin datos no reemplaza lo medido en cada reacción."),
        ("ab", "{F} Para atribuir el aumento de velocidad al catalizador, ¿qué debe mantenerse igual?", "La temperatura y la concentración inicial", "La velocidad que se quiere medir", "Controlar las otras variables permite atribuir el cambio al catalizador."),
        ("abc", "{F} Un estudiante predice que a 50 °C la velocidad inicial sería 16 mmol/(L·s). ¿Qué falta?", "Que no hay datos a 50 °C: la predicción sale del rango medido", "Nada: la tendencia siempre se cumple", "Que 16 no es un número", "Los datos llegan hasta 40 °C; más allá no hay respaldo."),
        ("=", "{F} ¿Cuántos mmol/L de A se consumieron entre 0 y 30 s?", "100-52", "Se resta la concentración a los 30 s de la inicial.", " mmol/L"),
        ("=", "{F} ¿Cuál es la velocidad media entre 10 y 30 s?", "(80-52)/20", "Se divide la disminución de [A] entre 10 y 30 s por los 20 s del intervalo.", " mmol/(L·s)"),
    ],
    ctx=("abc", "Contexto: un equipo de ejemplo quiere decir en un informe qué ocurre con la velocidad al subir de 20 a 40 °C. ¿Qué frase respeta los datos?", "Para esta reacción y esta concentración, la velocidad inicial pasó de 2 a 8 mmol/(L·s), es decir, 4 veces mayor", "Toda reacción se vuelve 4 veces más rápida al subir 20 °C", "La velocidad no depende de la temperatura", "La frase correcta nombra la reacción, el rango y los valores medidos."),
    sc=[
        ("En Química: ¿qué es un catalizador?", "Una sustancia que acelera una reacción sin consumirse", "Ofrece un camino con menor energía de activación."),
        ("ab", "Al avanzar la reacción, la velocidad media suele:", "Disminuir porque baja la concentración de reactivo", "Aumentar porque hay más reactivo", "Menos reactivo implica menos choques por segundo."),
        ("ab", "Una predicción fuera del rango medido:", "No tiene respaldo en los datos", "Siempre es válida", "No hay mediciones en ese rango."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula la velocidad media de dos intervalos distintos de la tabla de concentración; (2) escribe qué variable se cambió y cuál se midió en el estudio de la temperatura; (3) escribe una conclusión que no vaya más allá de los datos y una limitación.",
        "(1) 0–10 s: 2 mmol/(L·s); 20–30 s: 1,2 mmol/(L·s). (2) Se cambió la temperatura y se midió la velocidad inicial. (3) A mayor temperatura, mayor velocidad inicial entre 20 y 40 °C. Falta probar con otras concentraciones.",
        ["dos velocidades correctas", "variables identificadas", "conclusión acotada", "limitación"],
        ["tres respuestas numeradas"],
        ["confundir disminución con aumento", "extender la tendencia fuera del rango", "no declarar limitaciones"],
        "Pregunta: «¿qué otra variable mantendrías controlada?»."),
    reinforce="Calcula la velocidad media entre 20 y 30 s y explica por qué es menor que entre 0 y 10 s.",
    extend="Explica por qué un catalizador acelera una reacción sin cambiar la cantidad de producto que se obtiene al final.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (datos de ejemplo). Diagrama de energía de una reacción A (kJ/mol): energía de los reactivos 40; cima de la barrera (estado de transición) 140; energía de los productos −10. Con un catalizador de ejemplo, la cima baja a 90. "
     "Definiciones: energía de activación de la reacción directa Ea = energía de la cima − energía de los reactivos; ΔH = energía de los productos − energía de los reactivos; energía de activación de la reacción inversa = energía de la cima − energía de los productos. "
     "Reacción B de ejemplo (kJ/mol): reactivos 30; cima 100; productos 80.")
build(
    O3, 3, F,
    use="Aprenderé a interpretar un diagrama de energía: la energía de activación, la variación de entalpía y el efecto de un catalizador. Sirve para explicar por qué las reacciones tienen distinta velocidad y por qué la temperatura las acelera.",
    prior=["Sé qué es ΔH y su signo.", "Sé leer un gráfico de energía contra camino de reacción.", "Sé restar números positivos y negativos."],
    explain=[
        "El diagrama de energía es un modelo que muestra la energía de los reactivos, una barrera y la energía de los productos. Para que la reacción ocurra, las partículas deben chocar con una energía mínima, llamada energía de activación (Ea), que corresponde a la altura de la barrera medida desde los reactivos. Cuanto mayor es Ea, más lenta suele ser la reacción a una temperatura dada.",
        "La diferencia entre la energía de los productos y la de los reactivos es ΔH. Es independiente de la altura de la barrera. Una reacción puede ser exotérmica, con ΔH negativo, y tener una barrera alta o baja. Al subir la temperatura, una mayor fracción de partículas tiene energía suficiente para superar la barrera y la velocidad aumenta.",
        "Un catalizador ofrece un camino alternativo con una cima más baja, y por lo tanto con menor Ea, tanto en la reacción directa como en la inversa. No cambia la energía de los reactivos ni de los productos, así que ΔH queda igual. Como todo modelo, el diagrama simplifica: representa un solo camino y no muestra los choques ni el tiempo.",
    ],
    vocab=[("energía de activación (Ea)", "energía mínima que deben tener los choques para que ocurra la reacción"), ("estado de transición", "punto de mayor energía en el camino de reacción"), ("diagrama de energía", "gráfico de la energía de reactivos, barrera y productos"), ("camino de reacción", "secuencia de cambios desde los reactivos hasta los productos"), ("catalizador", "sustancia que baja la barrera de energía sin consumirse")],
    worked=[
        ("Energía de activación", "Una reacción C de ejemplo tiene reactivos en 20, cima en 90 y productos en 50 (kJ/mol). ¿Cuánto vale su Ea?",
         ["Ea = energía de la cima − energía de los reactivos.", "Cima: 90; reactivos: 20.", "90 − 20 = 70 kJ/mol."],
         "70 kJ/mol"),
        ("Entalpía de la reacción C", "Con los datos de la reacción C, ¿cuánto vale ΔH y qué tipo de reacción es?",
         ["ΔH = energía de los productos − energía de los reactivos.", "50 − 20 = +30 kJ/mol.", "ΔH positivo: es endotérmica."],
         "ΔH = +30 kJ/mol; endotérmica"),
    ],
    mistakes=[("Creer que un catalizador cambia ΔH.", "El catalizador baja la barrera, pero los reactivos y productos mantienen su energía.", "Recuerda: baja Ea, no cambia ΔH."),
              ("Confundir Ea con ΔH.", "Ea se mide hasta la cima; ΔH se mide hasta los productos.", "Marca en el diagrama dónde termina cada flecha.")],
    T=[
        ("abc", "En Química: ¿qué es la energía de activación?", "La energía mínima que deben tener los choques para que ocurra la reacción", "La energía total que libera la reacción", "La temperatura final del sistema", "La energía de activación es la altura de la barrera desde los reactivos."),
        ("=", "{F} ¿Cuánto vale la Ea de la reacción A sin catalizador?", "140-40", "Se resta la energía de los reactivos a la de la cima.", " kJ/mol"),
        ("=", "{F} ¿Cuánto vale ΔH de la reacción A?", "-10-40", "Se resta la energía de los reactivos a la de los productos.", " kJ/mol"),
        ("abc", "{F} Con el ΔH de la reacción A, ¿qué tipo de reacción es?", "Exotérmica", "Endotérmica", "No se puede saber", "ΔH negativo indica que se libera energía."),
        ("=", "{F} ¿Cuánto vale la Ea de la reacción A con catalizador?", "90-40", "Con el catalizador la cima está en 90, que se resta a la energía de los reactivos.", " kJ/mol"),
        ("abc", "{F} ¿Cuánto vale ΔH de la reacción A con catalizador?", "−50 kJ/mol, igual que sin catalizador", "−100 kJ/mol", "0 kJ/mol", "El catalizador no cambia la energía de los reactivos ni de los productos."),
        ("=", "{F} ¿Cuánto vale la energía de activación de la reacción inversa de A sin catalizador?", "140-(-10)", "Se resta la energía de los productos a la de la cima.", " kJ/mol"),
        ("ab", "¿Por qué subir la temperatura aumenta la velocidad según el modelo?", "Más partículas tienen energía suficiente para superar la barrera", "La barrera de energía de activación desaparece", "Con más temperatura más choques alcanzan la energía mínima necesaria."),
        ("abc", "¿Cómo acelera un catalizador una reacción?", "Ofrece un camino con menor energía de activación sin consumirse", "Aumenta la energía de los reactivos", "Cambia el valor de ΔH", "El catalizador baja la barrera y no se consume."),
        ("abc", "{F} Un estudiante dice: «con catalizador, la reacción A libera más energía». ¿Qué respondes?", "No: ΔH sigue siendo −50 kJ/mol; solo baja la barrera", "Sí: la cima más baja libera más energía", "Sí, porque Ea y ΔH son lo mismo", "ΔH depende de reactivos y productos, que no cambian."),
        ("=", "{F} ¿Cuánto vale la energía de activación de la reacción inversa de A con catalizador?", "90-(-10)", "Se resta la energía de los productos a la nueva cima de 90.", " kJ/mol"),
        ("abc", "{F} ¿Cuál afirmación sobre la reacción B (reactivos 30, cima 100, productos 80) es correcta?", "Es endotérmica (ΔH = +50) y su Ea es 70", "Es exotérmica porque su Ea es grande", "Es endotérmica y su Ea es 50", "ΔH = 80 − 30 = +50 y Ea = 100 − 30 = 70."),
        ("=", "{F} ¿Cuánto vale la energía de activación de la reacción inversa de B?", "100-80", "Se resta la energía de los productos a la de la cima.", " kJ/mol"),
    ],
    ctx=("abc", "Contexto: un laboratorio de ejemplo compara dos catalizadores para la reacción A. El catalizador 1 baja la cima a 90 y el 2 la baja a 110. ¿Cuál acelera más la reacción directa a la misma temperatura y por qué?", "El 1, porque deja una barrera de 50 kJ/mol frente a los 70 del 2", "El 2, porque su cima está más alta", "Ambos igual, porque ΔH es −50", "A menor Ea, mayor fracción de choques efectivos y mayor velocidad."),
    sc=[
        ("En Química: ¿qué es el estado de transición?", "El punto de mayor energía en el camino de reacción", "Corresponde a la cima de la barrera de energía."),
        ("ab", "Un catalizador cambia:", "La energía de activación", "El valor de ΔH", "El catalizador solo baja la barrera de energía."),
        ("ab", "Una reacción con ΔH negativo:", "Libera energía", "Absorbe energía", "Un ΔH negativo indica que la reacción es exotérmica."),
    ],
    op=("Con los diagramas de la ficha {F}: (1) calcula Ea y ΔH de la reacción A sin catalizador; (2) explica con dos oraciones qué cambia y qué no cambia al agregar el catalizador; (3) señala un supuesto del modelo de diagrama de energía.",
        "(1) Ea = 100 kJ/mol; ΔH = −50 kJ/mol. (2) Cambia la altura de la barrera (Ea baja a 50); no cambia ΔH. (3) El diagrama supone un solo camino de reacción y no muestra el tiempo.",
        ["Ea y ΔH correctos", "qué cambia y qué no cambia", "supuesto formulado"],
        ["tres respuestas numeradas"],
        ["confundir Ea con ΔH", "decir que el catalizador cambia ΔH", "no declarar supuestos"],
        "Pregunta: «¿qué dato de velocidad apoyaría tu explicación?»."),
    reinforce="Dibuja en tu cuaderno el diagrama de la reacción B con una flecha para Ea y otra para ΔH, y escribe sus valores.",
    extend="Explica por qué subir la temperatura y agregar un catalizador aceleran una reacción por razones distintas.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (datos de ejemplo). Reacción reversible A ⇌ 2B en disolución, a temperatura constante; concentraciones en unidades de ejemplo. Constante de equilibrio Kc = [B] × [B] ÷ [A]. "
     "Cociente de reacción Q: la misma expresión con las concentraciones de un momento cualquiera. Si Q < Kc, la reacción avanza hacia los productos; si Q > Kc, hacia los reactivos; si Q = Kc, hay equilibrio. "
     "Datos del equilibrio a 25 °C: [A] = 9 y [B] = 6. Tres momentos de otro ensayo, a la misma temperatura: Momento 1: [A] = 20 y [B] = 6; Momento 2: [A] = 4 y [B] = 6; Momento 3: [A] = 9 y [B] = 6. "
     "Sistema natural de ejemplo: CO2(g) ⇌ CO2(aq) entre el aire y el agua de un lago.")
build(
    O3, 4, F,
    use="Aprenderé a analizar evidencia de un equilibrio químico: calcular la constante de equilibrio y el cociente de reacción, y predecir hacia dónde se desplaza el sistema. Sirve para argumentar cómo responden los sistemas naturales a los cambios.",
    prior=["Sé qué es una reacción reversible.", "Sé calcular productos y cocientes.", "Sé leer una tabla de concentraciones."],
    explain=[
        "En una reacción reversible, los productos pueden volver a formar reactivos. El equilibrio químico se alcanza cuando la reacción directa y la inversa ocurren con la misma velocidad: las concentraciones dejan de cambiar, pero las reacciones no se detienen, por eso se llama equilibrio dinámico. La constante de equilibrio Kc resume ese estado: multiplica las concentraciones de los productos y divide por las de los reactivos, con cada concentración elevada a su coeficiente.",
        "Para saber hacia dónde avanza un sistema que todavía no está en equilibrio, se calcula Q con las concentraciones del momento y se compara con Kc. Si Q es menor que Kc, falta producto y la reacción avanza hacia los productos; si es mayor, avanza hacia los reactivos. Un catalizador acelera ambas direcciones por igual y no cambia Kc ni la posición del equilibrio.",
        "El principio de Le Châtelier dice que, si se perturba un equilibrio, el sistema se desplaza para contrarrestar la perturbación. Agregar reactivo lo desplaza hacia los productos; retirar producto también. En una bebida con gas cerrada, el CO2 disuelto está en equilibrio con el CO2 de arriba; al destaparla baja la presión y sale gas del líquido. Si el equilibrio tiene una reacción directa endotérmica, calentar favorece los productos.",
    ],
    vocab=[("equilibrio químico", "estado en que las reacciones directa e inversa tienen igual velocidad"), ("Kc", "constante de equilibrio, a una temperatura dada"), ("cociente de reacción (Q)", "expresión de Kc con las concentraciones de un momento cualquiera"), ("principio de Le Châtelier", "un sistema en equilibrio se desplaza para contrarrestar una perturbación"), ("equilibrio dinámico", "equilibrio en que las dos reacciones siguen ocurriendo")],
    worked=[
        ("Calcular Kc", "Otro equilibrio A ⇌ 2B tiene [A] = 5 y [B] = 10. ¿Cuánto vale Kc?",
         ["Kc = [B] × [B] ÷ [A].", "Se reemplaza: 10 × 10 ÷ 5.", "100 ÷ 5 = 20."],
         "Kc = 20"),
        ("Dirección de avance", "En ese equilibrio (Kc = 20), un momento tiene [A] = 2 y [B] = 8. ¿Hacia dónde avanza?",
         ["Q = 8 × 8 ÷ 2 = 32.", "Q = 32 es mayor que Kc = 20.", "Si Q > Kc, avanza hacia los reactivos."],
         "Hacia los reactivos"),
    ],
    mistakes=[("Pensar que en el equilibrio las reacciones se detienen.", "Siguen ocurriendo, pero con igual velocidad en ambos sentidos.", "Escribe «equilibrio dinámico»."),
              ("Creer que un catalizador desplaza el equilibrio hacia los productos.", "Acelera ambas direcciones por igual y no cambia Kc.", "Reserva los cambios de posición para cambios de concentración, presión o temperatura.")],
    T=[
        ("abc", "En Química: ¿qué es el equilibrio químico?", "Un estado en que las reacciones directa e inversa tienen igual velocidad", "Un estado en que la reacción se detiene por completo", "Un estado en que solo existen productos", "En el equilibrio las concentraciones no cambian porque ambas velocidades son iguales."),
        ("=", "{F} Con los datos del equilibrio a 25 °C ([A] = 9 y [B] = 6), ¿cuánto vale Kc?", "6*6/9", "Se multiplica [B] por [B] y se divide por [A].", ""),
        ("=", "{F} ¿Cuánto vale Q en el momento 1?", "6*6/20", "Se aplica la expresión de Kc con [A] = 20 y [B] = 6.", ""),
        ("abc", "{F} En el momento 1, ¿hacia dónde avanza la reacción?", "Hacia los productos, porque Q es menor que Kc", "Hacia los reactivos, porque Q es menor que Kc", "No avanza: ya está en equilibrio", "Q es 1,8, menor que Kc = 4, por lo que falta producto."),
        ("=", "{F} ¿Cuánto vale Q en el momento 2?", "6*6/4", "Se aplica la expresión con [A] = 4 y [B] = 6.", ""),
        ("abc", "{F} En el momento 2, ¿hacia dónde avanza la reacción?", "Hacia los reactivos, porque Q es mayor que Kc", "Hacia los productos, porque Q es mayor que Kc", "No avanza", "Q = 9 es mayor que Kc = 4, así que sobra producto."),
        ("{F} ¿Está en equilibrio el momento 3? Responde sí o no y explica con Q.", "Sí, porque Q es igual a Kc (4)", "Q = 6 × 6 ÷ 9 = 4, igual que Kc."),
        ("abc", "{F} Si en el equilibrio de la ficha se agrega más A, ¿hacia dónde se desplaza?", "Hacia los productos", "Hacia los reactivos", "No se desplaza", "Al agregar un reactivo, el sistema se desplaza para consumirlo."),
        ("abc", "{F} Si de ese equilibrio se retira B de forma continua, ¿qué ocurre?", "Se forma más B a partir de A", "Se forma más A a partir de B", "No ocurre nada", "Retirar un producto desplaza el equilibrio hacia los productos."),
        ("abc", "{F} Aumenta la presión de CO2 en el aire sobre un lago. ¿Qué predice Le Châtelier?", "Se disuelve más CO2 en el agua", "Se disuelve menos CO2", "El CO2 desaparece del aire por completo", "El sistema contrarresta el aumento de CO2(g) pasándolo a CO2(aq)."),
        ("=", "{F} En otro equilibrio de A ⇌ 2B a la misma temperatura (Kc = 4), [B] = 8. ¿Cuánto vale [A]?", "8*8/4", "Se despeja [A] dividiendo [B] por [B] entre Kc.", ""),
        ("ab", "{F} Un estudiante dice: «en el equilibrio, todas las reacciones se detienen». ¿Qué corrige?", "Las reacciones directa e inversa siguen ocurriendo con igual velocidad", "Tiene razón: no ocurre nada", "Las concentraciones no cambian porque las dos velocidades se igualan, no porque se detengan."),
        ("abc", "{F} Un estudiante afirma que agregar un catalizador aumenta Kc. ¿Qué respondes?", "No: el catalizador acelera ambas direcciones por igual y no cambia Kc", "Sí: más velocidad significa más Kc", "Sí, pero solo a 25 °C", "El catalizador no cambia la posición del equilibrio."),
    ],
    ctx=("abc", "Contexto: en un lago de ejemplo, la presión de CO2 del aire aumenta durante años. Un grupo comunica el resultado. ¿Qué mensaje es el más preciso?", "Según el equilibrio CO2(g) ⇌ CO2(aq), se espera que el lago disuelva más CO2, lo que habría que confirmar midiendo", "El lago dejará de intercambiar gases", "El CO2 del aire no afecta al agua", "El principio de Le Châtelier permite predecir la dirección, pero la predicción se contrasta con mediciones."),
    sc=[
        ("En Química: ¿qué es el cociente de reacción Q?", "La expresión de Kc con las concentraciones de un momento cualquiera", "Comparar Q con Kc indica hacia dónde avanza el sistema."),
        ("ab", "Si Q es mayor que Kc, la reacción avanza hacia:", "Los reactivos", "Los productos", "Hay demasiado producto, así que avanza hacia los reactivos."),
        ("ab", "Si en un equilibrio la reacción directa es endotérmica, calentar favorece:", "Los productos", "Los reactivos", "Se desplaza hacia el lado que absorbe energía."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula Kc y Q para dos momentos; (2) predice hacia dónde avanza cada uno; (3) elige una perturbación (agregar A, retirar B o aumentar CO2 del aire) y explica la respuesta del sistema con Le Châtelier.",
        "(1) Kc = 4; Q del momento 1 = 1,8; Q del momento 2 = 9. (2) Momento 1 avanza hacia los productos; momento 2, hacia los reactivos. (3) Si se retira B, el sistema forma más B para contrarrestarlo.",
        ["Kc y dos Q correctos", "predicciones consistentes con Q", "explicación con Le Châtelier"],
        ["tres respuestas numeradas"],
        ["comparar Q con Kc al revés", "decir que el catalizador cambia Kc", "decir que el equilibrio detiene las reacciones"],
        "Pregunta: «¿qué medición confirmaría tu predicción?»."),
    reinforce="Calcula Q para [A] = 3 y [B] = 6 y decide si el sistema está en equilibrio (Kc = 4).",
    extend="Explica por qué un sistema natural en equilibrio, como el CO2 de un lago, responde a un cambio sin que nadie intervenga.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (datos de ejemplo). Relación de Gibbs: ΔG = ΔH − T × ΔS, con T en kelvin (K = °C + 273). Si ΔG < 0, el proceso es espontáneo a esa temperatura; si ΔG > 0, no lo es. "
     "Fusión de una sustancia X de ejemplo: ΔH = +6.000 J/mol y ΔS = +20 J/(mol·K). Reacción Y de ejemplo: ΔH = −40.000 J/mol y ΔS = −100 J/(mol·K). "
     "Modelo de argumento: afirmación (lo que se sostiene) + evidencia (datos) + razonamiento (por qué los datos apoyan la afirmación). "
     "Dos argumentos de ejemplo sobre un estanque industrial de ejemplo: Argumento 1: «la sustancia X del estanque se funde porque hace calor». Argumento 2: «a 330 K, la fusión de X es espontánea porque su ΔG es −600 J/mol, ya que el término T × ΔS pesa más que ΔH».")
build(
    O3, 5, F,
    use="Aprenderé a comparar argumentos sobre la espontaneidad de un proceso usando ΔG, y a comunicar una conclusión con afirmación, evidencia y razonamiento. Sirve para explicar por qué un sistema natural cambia con la temperatura.",
    prior=["Sé qué es ΔH y qué es la espontaneidad.", "Sé convertir °C a K.", "Sé multiplicar y restar números con signo."],
    explain=[
        "Además de la energía, los procesos dependen de la entropía (S), una medida del desorden o de las formas en que pueden distribuirse la materia y la energía. Fundir una sustancia aumenta la entropía (ΔS positivo). La energía libre de Gibbs reúne ambos factores: ΔG = ΔH − T × ΔS. Un proceso es espontáneo a una temperatura dada si ΔG es negativo.",
        "El signo de ΔG depende de la temperatura cuando ΔH y ΔS tienen el mismo signo. Para la fusión de X, con ΔH y ΔS positivos, el término T × ΔS crece con la temperatura y supera a ΔH cuando T es alta: a baja temperatura la fusión no es espontánea y a alta temperatura sí. La temperatura en que ΔG = 0 se calcula como ΔH ÷ ΔS. Para la reacción Y, con ΔH y ΔS negativos, ocurre lo contrario.",
        "Para comparar argumentos, se mira cuál tiene afirmación clara, evidencia medible y razonamiento que conecte ambas cosas. El argumento 1 da una causa sin datos; el 2 usa ΔG. Además, ΔG negativo dice que el proceso puede ocurrir por sí solo, pero no dice qué tan rápido: esa es la pregunta de la cinética. Decirlo es parte de comunicar los límites de la conclusión.",
    ],
    vocab=[("entropía (S)", "medida del desorden o de las formas de distribuir materia y energía"), ("energía libre de Gibbs (ΔG)", "ΔH − T × ΔS; si es negativa el proceso es espontáneo"), ("kelvin (K)", "unidad de temperatura: °C + 273"), ("afirmación", "lo que se sostiene en un argumento"), ("razonamiento", "explicación de por qué la evidencia apoya la afirmación")],
    worked=[
        ("Calcular ΔG", "Con los datos de la fusión de X, ¿cuánto vale ΔG a 350 K y es espontánea?",
         ["ΔG = ΔH − T × ΔS = 6.000 − 350 × 20.", "350 × 20 = 7.000.", "6.000 − 7.000 = −1.000 J/mol; como es negativo, es espontánea."],
         "ΔG = −1.000 J/mol; espontánea"),
        ("Partes de un argumento", "En «a 330 K la fusión de X es espontánea porque su ΔG es −600 J/mol», ¿qué parte es la evidencia?",
         ["La afirmación es que la fusión es espontánea a 330 K.", "El dato «ΔG = −600 J/mol» es lo medido o calculado.", "Esa es la evidencia."],
         "ΔG = −600 J/mol"),
    ],
    mistakes=[("Creer que ΔG negativo significa que el proceso es rápido.", "ΔG habla de espontaneidad, no de velocidad.", "Declara que la rapidez depende de la cinética."),
              ("Usar la temperatura en °C dentro de ΔG.", "La fórmula requiere kelvin.", "Convierte siempre: K = °C + 273.")],
    T=[
        ("abc", "En Química: ¿qué indica un valor negativo de ΔG?", "Que el proceso es espontáneo a esa temperatura", "Que el proceso es muy rápido", "Que el proceso absorbe energía", "ΔG negativo indica espontaneidad, no velocidad."),
        ("=", "{F} ¿Cuántos kelvin son 7 °C?", "7+273", "Se suma 273 a la temperatura en °C.", " K"),
        ("=", "{F} ¿Cuánto vale ΔG de la fusión de X a 280 K?", "6000-280*20", "Se calcula T × ΔS = 280 × 20 y se resta a ΔH.", " J/mol"),
        ("abc", "{F} A 280 K, ¿la fusión de X es espontánea?", "No, porque ΔG es positivo", "Sí, porque ΔG es positivo", "Sí, porque ΔH es positivo", "ΔG = +400 J/mol, positivo, no es espontánea a esa temperatura."),
        ("=", "{F} ¿Cuánto vale ΔG de la fusión de X a 320 K?", "6000-320*20", "Se calcula 320 × 20 y se resta a ΔH.", " J/mol"),
        ("abc", "{F} A 320 K, ¿qué se concluye sobre la fusión de X?", "Es espontánea, porque ΔG es negativo", "No es espontánea, porque ΔG es negativo", "No se puede saber", "ΔG = −400 J/mol, negativo, indica espontaneidad."),
        ("ab", "{F} ¿Por qué la fusión de X se vuelve espontánea al subir la temperatura?", "Porque T × ΔS crece y supera a ΔH", "Porque ΔH se vuelve negativo", "Con ΔH y ΔS positivos, el término T × ΔS pesa más cuando T es alta."),
        ("=", "{F} ¿Cuánto vale ΔG de la reacción Y a 300 K?", "-40000-300*(-100)", "Se calcula T × ΔS = −30.000 y se resta a ΔH, es decir, −40.000 + 30.000.", " J/mol"),
        ("=", "{F} ¿Cuánto vale ΔG de la reacción Y a 500 K?", "-40000-500*(-100)", "Se calcula T × ΔS = −50.000 y se resta a ΔH, es decir, −40.000 + 50.000.", " J/mol"),
        ("abc", "{F} ¿Cuál es la afirmación mejor argumentada sobre la reacción Y a 500 K?", "No es espontánea, porque ΔG = +10.000 J/mol: el término −T × ΔS vale +50.000 y supera a ΔH = −40.000", "Es espontánea porque ΔH es negativo, sin considerar la temperatura", "No es espontánea porque se siente caliente", "Un buen argumento tiene afirmación, dato de ΔG y razonamiento con ΔH y T × ΔS."),
        ("abc", "{F} Entre los argumentos 1 y 2 sobre el estanque, ¿cuál es más sólido y por qué?", "El 2, porque entrega un dato calculado (ΔG) y razona con él", "El 1, porque es más breve", "Ambos igual, porque dicen lo mismo", "El argumento 2 une afirmación, evidencia y razonamiento."),
        ("ab", "{F} Un argumento concluye que, como ΔG < 0, la solidificación de X será muy rápida. ¿Qué falta aclarar?", "Que ΔG no dice la velocidad; la rapidez la estudia la cinética", "Nada: ΔG negativo implica rapidez", "Espontáneo no significa rápido; son preguntas distintas."),
        ("=", "{F} ¿A qué temperatura, en K, la fusión de X tiene ΔG = 0?", "6000/20", "Se iguala ΔG a 0 y se despeja T = ΔH ÷ ΔS.", " K"),
    ],
    ctx=("abc", "Contexto: un grupo de ejemplo debe comunicar a su curso si la fusión de X en un estanque industrial a 330 K es espontánea. ¿Qué frase sigue el modelo de argumento y respeta los límites?", "A 330 K es espontánea, porque su ΔG es −600 J/mol (T × ΔS supera a ΔH); esto no indica cuánto tardará", "Se congela porque suena lógico", "Se congela rápido, porque ΔG es negativo", "La frase correcta contiene afirmación, evidencia, razonamiento y un límite."),
    sc=[
        ("En Química: ¿qué es la entropía?", "Una medida del desorden o de las formas de distribuir materia y energía", "Un aumento de entropía suele favorecer la espontaneidad."),
        ("ab", "La temperatura que se usa en ΔG debe estar en:", "Kelvin", "Grados Celsius", "La fórmula de Gibbs exige temperatura absoluta."),
        ("ab", "Un buen argumento científico contiene:", "Afirmación, evidencia y razonamiento", "Solo una afirmación", "Sin evidencia ni razonamiento solo hay una opinión."),
    ],
    op=("Con la ficha {F}: (1) elige una temperatura y calcula ΔG de la fusión de X; (2) escribe un argumento con afirmación, evidencia y razonamiento sobre si es espontánea; (3) agrega una oración que comunique un límite de tu conclusión.",
        "(1) A 310 K: ΔG = 6.000 − 310 × 20 = −200 J/mol. (2) Afirmo que la fusión de X es espontánea a 310 K; la evidencia es ΔG = −200 J/mol; el razonamiento es que T × ΔS (6.200) supera a ΔH (6.000). (3) ΔG no indica qué tan rápido ocurre la fusión.",
        ["ΔG calculado en kelvin", "afirmación, evidencia y razonamiento", "límite comunicado"],
        ["tres respuestas numeradas"],
        ["usar °C en la fórmula", "confundir espontáneo con rápido", "argumento sin evidencia"],
        "Pregunta: «¿qué cambiaría en tu argumento si la temperatura fuera 250 K?»."),
    reinforce="Calcula la temperatura en K en que ΔG = 0 para una fusión de ejemplo con ΔH = 8.000 J/mol y ΔS = 40 J/(mol·K).",
    extend="Explica por qué dos procesos pueden tener el mismo ΔH y comportarse distinto con la temperatura, usando ΔS.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (datos de ejemplo, no son mediciones reales; las unidades son de ejemplo). Ciclo del carbono simplificado con cuatro reservorios: atmósfera, océano, vegetación y suelo. "
     "En un año de ejemplo entran a la atmósfera 9 unidades por quema de combustibles y 2 por respiración y descomposición neta de los suelos; salen de la atmósfera 4 hacia el océano y 3 hacia la vegetación. La atmósfera tenía 800 unidades al inicio del año. "
     "El CO2 se intercambia entre el aire y el océano en un equilibrio: CO2(g) ⇌ CO2(aq). En el ciclo del nitrógeno, el N2 del aire no lo usa la mayoría de las plantas; algunas bacterias lo transforman en amonio y nitrato, que las plantas absorben.")
build(
    O4, 1, F,
    use="Aprenderé a delimitar una pregunta sobre cómo el cambio climático altera los ciclos biogeoquímicos y los equilibrios del océano, la atmósfera, el agua dulce y el suelo. Sirve para ordenar flujos y reservorios con balances antes de explicar efectos.",
    prior=["Sé qué es un equilibrio químico.", "Sé sumar y restar para hacer un balance.", "Sé que el CO2 es un gas del aire."],
    explain=[
        "Un ciclo biogeoquímico es el recorrido de un elemento, como el carbono o el nitrógeno, entre los seres vivos (parte «bio»), el aire, el agua y las rocas o el suelo (parte «geo»), mediante procesos químicos. Cada lugar donde el elemento se almacena es un reservorio, y el movimiento entre reservorios es un flujo. Un balance suma las entradas y resta las salidas de un reservorio en un período.",
        "El cambio climático es el cambio de largo plazo del clima de la Tierra, hoy muy ligado a la acumulación de gases como el CO2 en la atmósfera. Altera los ciclos porque cambia las temperaturas, las lluvias y el hielo, y con ello los flujos. Los gases se disuelven menos en agua cálida, y los suelos secos o inundados cambian cuánto carbono y nitrógeno guardan. Cada ambiente (océano, atmósfera, aguas dulces, suelos) tiene sus propios equilibrios químicos.",
        "Para investigar, se delimita una pregunta que nombre un reservorio, un flujo y una variable medible, por ejemplo cuánto carbono pasa de la atmósfera al océano por año en una región. Preguntas como «¿qué pasa con el planeta?» no se responden con un balance. Además, las cifras de esta clase son de ejemplo: sirven para practicar el método, no para describir mediciones reales.",
    ],
    vocab=[("ciclo biogeoquímico", "recorrido de un elemento entre seres vivos, aire, agua y suelo"), ("reservorio", "lugar donde se almacena un elemento"), ("flujo", "movimiento de un elemento entre reservorios"), ("balance", "entradas menos salidas de un reservorio en un período"), ("cambio climático", "cambio de largo plazo del clima de la Tierra")],
    worked=[
        ("Balance de un reservorio", "Un reservorio de ejemplo recibe 10 y 4 unidades por dos vías, y pierde 6 y 3 por otras dos. ¿Cuál es su balance neto?",
         ["Entradas: 10 + 4 = 14.", "Salidas: 6 + 3 = 9.", "Balance: 14 − 9 = +5; el reservorio aumenta."],
         "+5 unidades"),
        ("Pregunta delimitada", "¿Cuál pregunta está mejor delimitada: «¿qué le pasa al planeta con el CO2?» o «¿cuántas unidades de carbono pasan por año de la atmósfera al océano en una región de ejemplo?»",
         ["La primera no nombra un reservorio, un flujo ni una variable medible.", "La segunda nombra el flujo (atmósfera a océano), la unidad y el período.", "Se puede responder con un balance de datos."],
         "La segunda pregunta"),
    ],
    mistakes=[("Confundir reservorio con flujo.", "El reservorio es donde se almacena; el flujo es el movimiento entre reservorios.", "Pregunta: ¿es un lugar donde se guarda o un traslado?"),
              ("Tomar las cifras de ejemplo como datos reales.", "Los valores de esta clase son ilustrativos para practicar balances.", "Rotula siempre «de ejemplo» y busca datos publicados cuando la pregunta lo requiera.")],
    T=[
        ("abc", "En Química: ¿qué es un ciclo biogeoquímico?", "El recorrido de un elemento entre seres vivos, aire, agua y suelo mediante procesos químicos", "El recorrido diario del Sol", "Una reacción que ocurre solo en el laboratorio", "Un ciclo biogeoquímico une la parte viva y la parte física del planeta."),
        ("{F} ¿Qué proceso de la ficha pone CO2 en la atmósfera por actividad humana?", "La quema de combustibles", "La ficha lo indica con 9 unidades de entrada por quema de combustibles."),
        ("=", "{F} ¿Cuántas unidades entran en total a la atmósfera en el año de ejemplo?", "9+2", "Se suman las dos entradas de la ficha.", " unidades"),
        ("=", "{F} ¿Cuántas unidades salen en total de la atmósfera en el año de ejemplo?", "4+3", "Se suman las dos salidas de la ficha.", " unidades"),
        ("=", "{F} ¿Cuál es el balance neto de la atmósfera en el año de ejemplo (entradas menos salidas)?", "(9+2)-(4+3)", "Se resta el total de salidas al total de entradas.", " unidades"),
        ("=", "{F} ¿Cuántas unidades tiene la atmósfera al final del año de ejemplo?", "800+(9+2)-(4+3)", "Se suma el balance neto a la cantidad inicial de la atmósfera.", " unidades"),
        ("abc", "{F} ¿Qué describe CO2(g) ⇌ CO2(aq) entre el aire y el océano?", "Un intercambio reversible que tiende a un equilibrio", "Un flujo que solo va del océano al aire", "Una reacción que destruye el carbono", "La flecha doble indica que el CO2 pasa en ambos sentidos hasta equilibrarse."),
        ("abc", "¿Cuál pregunta está mejor delimitada?", "¿Cuántas unidades de carbono pasan por año de la atmósfera al océano en una región de ejemplo?", "¿Qué le pasa al planeta?", "¿Es malo el CO2?", "La mejor pregunta nombra reservorios, flujo, unidad y período."),
        ("abc", "{F} ¿Por qué importan las bacterias que transforman N2 en amonio y nitrato en el ciclo del nitrógeno?", "Porque convierten el N2 del aire en formas que las plantas pueden absorber", "Porque producen CO2", "Porque eliminan el nitrógeno del planeta", "Sin esa transformación, la mayoría de las plantas no usaría el nitrógeno del aire."),
        ("ab", "Un balance neto positivo en la atmósfera significa:", "Que entraron más unidades de las que salieron", "Que salieron más unidades de las que entraron", "Balance positivo es entradas menos salidas mayor que cero."),
        ("=", "{F} Si la quema de combustibles bajara de 9 a 5 unidades y los demás flujos siguieran igual, ¿cuál sería el balance neto?", "(5+2)-(4+3)", "Se suman las entradas con 5 y se restan las salidas; el resultado cero indica que no cambia.", " unidades"),
        ("abc", "Un océano más cálido disuelve menos gas. ¿Qué efecto tiene esto sobre el flujo de CO2 de la atmósfera al océano, si lo demás no cambia?", "Tiende a disminuir", "Tiende a aumentar", "No cambia", "Los gases se disuelven menos en agua más cálida, de modo que el océano absorbe menos."),
        ("=", "{F} Si el flujo hacia el océano fuera 6 en vez de 4 (y la quema 9), ¿cuál sería el balance neto de la atmósfera?", "(9+2)-(6+3)", "Se recalculan las salidas con 6 y 3 y se restan de las entradas.", " unidades"),
    ],
    ctx=("abc", "Contexto: un equipo de ejemplo quiere estudiar el carbono de un humedal costero. ¿Qué pregunta de investigación elige?", "¿Cuántas unidades de carbono almacena por año la vegetación del humedal y cuántas se liberan a la atmósfera?", "¿Es importante el carbono?", "¿Qué pasa con las costas?", "La pregunta elegida nombra un reservorio, dos flujos y una variable medible."),
    sc=[
        ("En Química: ¿qué es un reservorio?", "Un lugar donde se almacena un elemento", "La atmósfera, el océano, la vegetación y el suelo son reservorios de carbono."),
        ("ab", "Un flujo es:", "El movimiento de un elemento entre reservorios", "El lugar donde se almacena", "Un flujo es traslado, no almacenamiento."),
        ("ab", "Un balance se calcula como:", "Entradas menos salidas", "Salidas más entradas", "El balance indica cuánto cambia el reservorio."),
    ],
    op=("Con los datos de la ficha {F}: (1) elige un reservorio (atmósfera, océano, vegetación o suelo) y escribe una pregunta sobre cómo el cambio climático podría cambiar uno de sus flujos; (2) nombra la variable que medirías; (3) escribe qué balance calcularías con los datos de ejemplo.",
        "(1) Océano: ¿cómo cambia el flujo de CO2 que entra al océano si sube la temperatura del agua superficial? (2) Mediría la temperatura y el CO2 disuelto. (3) Entradas menos salidas del océano; con los datos de ejemplo, 4 entran y no se muestran salidas.",
        ["reservorio y flujo nombrados", "pregunta delimitada", "variable medible", "balance descrito"],
        ["tres respuestas numeradas"],
        ["pregunta demasiado amplia", "confundir reservorio con flujo", "tratar los datos de ejemplo como reales"],
        "Pregunta: «¿qué dato real necesitarías para reemplazar los de ejemplo?»."),
    reinforce="Haz un esquema con los cuatro reservorios del carbono y rotula con flechas los cuatro flujos de la ficha.",
    extend="Explica por qué el agua más cálida disuelve menos gas y qué efecto podría tener eso en el ciclo del carbono.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (datos de ejemplo aproximados, no son mediciones oficiales). Oxígeno disuelto en agua dulce, a la misma presión atmosférica: a 5 °C: 12 mg/L; a 20 °C: 9 mg/L; a 30 °C: 8 mg/L. "
     "Estudio de ejemplo de un río: la temperatura media de un verano al siguiente subió 2 °C y el oxígeno disuelto en el punto de medición bajó de 9 a 8 mg/L. "
     "Otro punto del río: 10 mg/L en invierno y 7 mg/L en verano. Una especie de pez de ejemplo necesita al menos 9 mg/L. "
     "Fuente A: red de estaciones con sensores calibrados y registros de 20 años. Fuente B: nota que dice «los ríos se están quedando sin oxígeno», sin datos.")
build(
    O4, 2, F,
    use="Aprenderé a evaluar fuentes y variables en un estudio sobre temperatura y gases disueltos en aguas dulces. Sirve para explicar cómo el calentamiento puede afectar el equilibrio de gases y el bienestar de los seres vivos del agua.",
    prior=["Sé qué es un equilibrio entre un gas y su disolución.", "Sé calcular un cambio porcentual.", "Sé distinguir variable independiente y dependiente."],
    explain=[
        "Un gas se disuelve en agua en un equilibrio: gas ⇌ gas disuelto. Al subir la temperatura, el equilibrio se desplaza hacia el gas y el agua retiene menos gas disuelto. Por eso el agua cálida contiene menos oxígeno que el agua fría. Cuando el oxígeno disuelto baja de lo que necesitan los peces y otros organismos, su bienestar y el de las personas que dependen de ellos se ven afectados.",
        "Para evaluar un estudio, se identifican sus variables. La variable independiente es la que cambia, aquí la temperatura. La dependiente es la que se mide, el oxígeno disuelto. Las controladas son las que se mantienen iguales, como la presión y el tipo de agua. En un río real hay más variables que cambian a la vez, como el caudal y la materia orgánica, por lo que atribuir un cambio a una sola causa exige cuidado.",
        "Una fuente es más confiable si publica método, instrumentos y registros largos. Una nota sin datos, aunque suene alarmante, solo es una pista. Para describir la rapidez de un cambio se usa la tasa, que es el cambio dividido por la variación de la otra variable: por ejemplo, mg/L de oxígeno que se pierden por cada grado que sube la temperatura.",
    ],
    vocab=[("oxígeno disuelto", "oxígeno gaseoso presente en el agua, medido en mg/L"), ("solubilidad", "cantidad máxima de una sustancia que se disuelve en un disolvente"), ("tasa", "cambio de una variable dividido por la variación de otra"), ("variable controlada", "la que se mantiene igual para poder comparar"), ("bienestar", "condiciones de salud, alimento y trabajo que las personas necesitan")],
    worked=[
        ("Clasificar variables", "En la tabla de oxígeno disuelto de la ficha, ¿qué variable se mide como efecto?",
         ["La temperatura es la que cambia de una fila a otra.", "Lo que se registra en cada temperatura es el oxígeno disuelto.", "Esa es la variable dependiente."],
         "El oxígeno disuelto"),
        ("Diferencia entre estaciones", "En el otro punto del río de la ficha, ¿cuántos mg/L menos de oxígeno hay en verano que en invierno?",
         ["Invierno: 10 mg/L.", "Verano: 7 mg/L.", "Diferencia: 10 − 7 = 3 mg/L."],
         "3 mg/L menos"),
    ],
    mistakes=[("Atribuir toda la baja de oxígeno solo a la temperatura.", "En un río real también influyen el caudal y la materia orgánica.", "Escribe «la temperatura contribuye» y señala qué otras variables faltan controlar."),
              ("Aceptar una nota alarmante porque suena grave.", "Sin datos ni método no se puede evaluar.", "Pide los datos o busca una fuente con registros.")],
    T=[
        ("abc", "En Química: ¿cómo cambia la cantidad de gas disuelto en agua al subir la temperatura?", "Disminuye", "Aumenta", "No cambia", "Al calentar, el equilibrio se desplaza hacia el gas y el agua retiene menos."),
        ("{F} ¿A qué temperatura tiene más oxígeno disuelto el agua dulce de ejemplo?", "A 5 °C, con 12 mg/L", "Entre 12, 9 y 8 mg/L el mayor valor corresponde a 5 °C."),
        ("{F} ¿Qué fuente (A o B) es más confiable?", "La fuente A", "Tiene sensores calibrados y registros de 20 años, a diferencia de la B, que no tiene datos."),
        ("=", "{F} ¿Cuántos mg/L menos de oxígeno hay a 30 °C que a 5 °C?", "12-8", "Se resta el valor a 30 °C al valor a 5 °C.", " mg/L"),
        ("=", "{F} ¿Cuál es el cambio porcentual del oxígeno disuelto entre 5 °C y 20 °C?", "(9-12)*100/12", "Se divide la diferencia por el valor de comparación (5 °C) y se multiplica por 100; el signo negativo indica baja.", " %"),
        ("=", "{F} ¿Cuántos mg/L de oxígeno se pierden por cada °C que sube la temperatura entre 5 y 20 °C?", "(12-9)/(20-5)", "Se divide la baja de oxígeno por el aumento de temperatura entre ambos puntos.", " mg/L por °C"),
        ("abc", "{F} En el estudio del río, ¿cuál es la variable dependiente?", "El oxígeno disuelto", "La temperatura media del verano", "La presión atmosférica", "La dependiente es la que se mide como efecto, aquí el oxígeno disuelto."),
        ("abc", "{F} En el otro punto del río, ¿en qué estación se cumple el mínimo del pez de ejemplo (9 mg/L)?", "En invierno, con 10 mg/L", "En verano, con 7 mg/L", "En ninguna estación", "Solo el valor de invierno, 10 mg/L, alcanza o supera 9 mg/L."),
        ("abc", "{F} Un estudiante concluye: «el aumento de 2 °C causó solo la baja de 9 a 8 mg/L». ¿Qué falta?", "Controlar otras variables, como caudal y materia orgánica, antes de atribuir una sola causa", "Nada: la conclusión es correcta", "Que el oxígeno no se puede medir", "En un río real cambian varias variables a la vez."),
        ("ab", "{F} ¿Qué dato mejoraría el estudio del río?", "Registros de varios años y estaciones, con temperatura y caudal", "Más opiniones de vecinos sin mediciones", "Series largas con variables registradas permiten separar efectos."),
        ("=", "{F} ¿Cuántos mg/L de oxígeno se pierden por cada °C que sube la temperatura entre 20 y 30 °C?", "(9-8)/(30-20)", "Se divide la baja de oxígeno entre ambos puntos por el aumento de temperatura.", " mg/L por °C"),
        ("abc", "{F} Un compañero calcula que la pérdida de oxígeno por °C es mayor entre 5 y 20 °C que entre 20 y 30 °C. ¿Qué indica esa comparación?", "Que el oxígeno baja más rápido por °C entre 5 y 20 °C que entre 20 y 30 °C", "Que el oxígeno baja igual en ambos tramos", "Que el oxígeno sube con la temperatura", "La tasa menor en el segundo tramo indica una baja más lenta por grado."),
        ("abc", "{F} La fuente B dice «los ríos se están quedando sin oxígeno». ¿Qué problema tiene?", "Generaliza a todos los ríos sin datos, mientras la tabla muestra una baja moderada en un punto", "Ninguno: es una conclusión sólida", "Que usa la palabra oxígeno", "Una afirmación general necesita datos de muchos ríos y de varios años."),
    ],
    ctx=("abc", "Contexto: una junta de vigilancia de ejemplo debe avisar a la comunidad sobre el río de la ficha, donde el oxígeno bajó de 9 a 8 mg/L y el pez de ejemplo necesita 9. ¿Qué mensaje es el más preciso?", "En el punto medido el oxígeno quedó bajo el mínimo del pez de ejemplo; hay que seguir midiendo y revisar otras variables", "El río está muerto", "No pasa nada, porque 8 es cercano a 9", "El mensaje correcto compara con el umbral y declara que se necesitan más datos."),
    sc=[
        ("En Química: ¿qué es la solubilidad?", "La cantidad máxima de una sustancia que se disuelve en un disolvente", "La solubilidad de un gas disminuye al subir la temperatura."),
        ("ab", "Una fuente es más confiable si:", "Publica método, instrumentos y registros", "Suena alarmante", "Los datos y el método permiten revisar y repetir."),
        ("ab", "La variable que se mide como efecto es la:", "Dependiente", "Independiente", "Es la que responde al cambio."),
    ],
    op=("Con los datos de la ficha {F}: (1) clasifica las variables del estudio del río; (2) calcula una tasa o un cambio porcentual de la tabla; (3) escribe una conclusión sobre el bienestar de los peces de ejemplo y una limitación.",
        "(1) Independiente: temperatura; dependiente: oxígeno disuelto; controlada: presión. (2) Entre 5 y 20 °C el oxígeno bajó 25 %. (3) A 20 °C el agua cumple el mínimo de 9 mg/L, pero a 30 °C no; falta medir caudal y materia orgánica.",
        ["variables bien clasificadas", "cálculo correcto", "conclusión acotada", "limitación"],
        ["tres respuestas numeradas"],
        ["confundir variable que cambia con la que se mide", "atribuir una causa única", "olvidar el umbral"],
        "Pregunta: «¿qué otra variable agregarías al estudio?»."),
    reinforce="Calcula la diferencia de oxígeno disuelto entre 20 y 30 °C y compárala con el mínimo de 9 mg/L del pez de ejemplo.",
    extend="Explica por qué un agua dulce más cálida puede afectar la pesca o el agua para riego, usando el oxígeno disuelto.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (datos de ejemplo). Modelo del CO2 en el agua (equilibrios): (1) CO2(g) ⇌ CO2(aq); (2) CO2(aq) + H2O ⇌ H2CO3 ⇌ H+ + HCO3−; (3) H+ + CO3 con carga 2− ⇌ HCO3− (el carbonato consume H+); (4) CaCO3(s) ⇌ Ca con carga 2+ + CO3 con carga 2− (el CaCO3 forma conchas y esqueletos de algunos organismos). "
     "Dato aproximado que se entrega: bajar el pH en 0,1 unidades equivale a un aumento de alrededor de 26 % en [H+]. Dato de ejemplo: el pH superficial de un océano de ejemplo pasó de 8,2 a 8,1. "
     "Masas atómicas que se entregan: C = 12, O = 16, Ca = 40.")
build(
    O4, 3, F,
    use="Aprenderé a interpretar el modelo de equilibrios del CO2 en el agua y a usarlo para explicar la acidificación del océano y su efecto sobre organismos con conchas. Sirve para relacionar el cambio climático con equilibrios químicos y con consecuencias para las personas.",
    prior=["Sé el principio de Le Châtelier.", "Sé qué es el pH y que su escala es logarítmica.", "Sé calcular masas molares sumando masas atómicas."],
    explain=[
        "Cuando el CO2 del aire se disuelve en el océano, parte reacciona con el agua y forma ácido carbónico, que libera H+ y ion bicarbonato. Eso hace bajar el pH, un proceso llamado acidificación del océano. Si el CO2 del aire aumenta, el equilibrio (1) se desplaza hacia el CO2 disuelto, y el equilibrio (2) produce más H+.",
        "Los iones carbonato consumen H+ al formar bicarbonato, de modo que parte del H+ nuevo se compensa, pero a costa de bajar la cantidad de carbonato disponible. Organismos como moluscos y corales forman sus conchas y esqueletos con carbonato de calcio, CaCO3, en el equilibrio (4). Con menos carbonato, ese equilibrio se desplaza hacia la disolución de CaCO3, lo que dificulta formar y mantener conchas.",
        "Este modelo supone que el sistema está en equilibrio y a temperatura constante, aunque la temperatura también cambia y altera las solubilidades. Una baja de solo 0,1 unidades de pH parece pequeña, pero equivale a un aumento cercano a 26 % en la concentración de H+. Por eso las conclusiones se expresan como tendencias que se contrastan con mediciones, y se informa su incertidumbre.",
    ],
    vocab=[("acidificación del océano", "disminución del pH del océano por CO2 disuelto"), ("bicarbonato (HCO3−)", "ion que se forma cuando el carbonato recibe un H+"), ("carbonato (CO3 2−)", "ion que consume H+ y forma parte del CaCO3"), ("CaCO3", "carbonato de calcio, material de conchas y esqueletos"), ("supuesto", "condición que el modelo da por cierta")],
    worked=[
        ("Masa molar del CaCO3", "¿Cuál es la masa molar del CaCO3?",
         ["Se suman las masas atómicas: Ca + C + 3 × O.", "40 + 12 + 3 × 16 = 40 + 12 + 48.", "El total es 100 g/mol."],
         "100 g/mol"),
        ("Aplicar Le Châtelier", "Si sube la cantidad de H+ en el agua, ¿qué le ocurre al carbonato según el equilibrio (3)?",
         ["El carbonato se combina con H+ para formar bicarbonato.", "Más H+ desplaza (3) hacia la derecha.", "La cantidad de carbonato disminuye."],
         "Disminuye"),
    ],
    mistakes=[("Decir que el CO2 disuelto sube el pH del océano.", "El CO2 forma ácido carbónico y libera H+, lo que baja el pH.", "Recuerda: más H+ significa menos pH."),
              ("Pensar que una baja de 0,1 de pH es insignificante.", "Por ser logarítmica, equivale a un aumento cercano a 26 % de H+.", "Interpreta el cambio de pH como cambio relativo de [H+].")],
    T=[
        ("abc", "En Química: ¿qué ocurre con el CO2 cuando se disuelve en el océano?", "Parte forma ácido carbónico y libera H+, lo que baja el pH", "Sube el pH del agua", "Se transforma en oxígeno puro", "El CO2 disuelto forma ácido carbónico, que libera H+."),
        ("{F} ¿Qué ion consume H+ según el equilibrio (3)?", "El ion carbonato", "En (3), el carbonato se combina con H+ y forma bicarbonato."),
        ("=", "{F} ¿Cuál es la masa molar del CO2?", "12+2*16", "Se suma la masa del carbono y la de dos oxígenos.", " g/mol"),
        ("=", "{F} Una concha de ejemplo tiene 300 g de CaCO3. ¿Cuántos mol de CaCO3 son? Usa la masa molar del CaCO3.", "300/(40+12+3*16)", "Se divide la masa por la masa molar del CaCO3, calculada con las masas atómicas dadas.", " mol"),
        ("abc", "{F} Si aumenta el CO2 del aire, ¿hacia dónde se desplaza el equilibrio (1)?", "Hacia CO2(aq), disolviendo más CO2", "Hacia CO2(g), liberando CO2", "No se desplaza", "Al aumentar el CO2 gaseoso, el sistema consume parte pasándolo al agua."),
        ("abc", "{F} Si disminuyera la cantidad de H+ del agua, ¿hacia dónde se desplazaría el equilibrio (3)?", "Hacia la izquierda: el bicarbonato libera H+ y aumenta el carbonato", "Hacia la derecha: se forma más bicarbonato", "No se desplazaría", "Al retirar un producto de la derecha del equilibrio (3) el sistema repone H+ y carbonato."),
        ("abc", "{F} Con menos carbonato disponible, ¿qué le ocurre al equilibrio (4)?", "Se desplaza hacia la disolución del CaCO3", "Se desplaza hacia la formación de más CaCO3", "No se altera", "Menos carbonato favorece que el CaCO3 se disuelva para reponerlo."),
        ("abc", "{F} El pH de un océano de ejemplo pasó de 8,2 a 8,1. ¿Qué ocurrió con [H+]?", "Aumentó cerca de 26 %", "Disminuyó cerca de 26 %", "Aumentó 10 veces", "Una baja de 0,1 unidades de pH equivale a alrededor de 26 % más de H+."),
        ("ab", "¿Qué supuesto hace el modelo de equilibrios del CO2?", "Que el sistema está en equilibrio y a temperatura constante", "Que el pH nunca cambia", "El modelo describe equilibrios a una temperatura dada y no incluye otros cambios."),
        ("abc", "{F} ¿Qué consecuencia podría tener la menor disponibilidad de carbonato para los organismos con conchas?", "Mayor dificultad para formar y mantener sus conchas", "Conchas más gruesas en todos los casos", "Ninguna, porque no usan carbonato", "Las conchas se forman con CaCO3, que depende del carbonato."),
        ("ab", "Un estudiante dice: «el CO2 disuelto sube el pH del océano». ¿Qué corrige?", "El CO2 disuelto libera H+ y baja el pH", "Tiene razón: sube el pH", "Más H+ implica menor pH, y el CO2 disuelto aporta H+."),
        ("abc", "Si el océano se calienta, disuelve menos CO2; pero el aire tiene más CO2. ¿Qué conclusión es prudente?", "Hay efectos opuestos y conviene medir ambos antes de predecir el resultado", "El resultado es siempre más acidificación sin importar lo demás", "El océano nunca absorbe CO2", "Dos efectos opuestos requieren datos para saber cuál domina."),
        ("=", "{F} Una concha de ejemplo tiene 2 mol de CaCO3. ¿Cuántos gramos de CaCO3 son? Usa la masa molar calculada con las masas atómicas dadas.", "2*(40+12+3*16)", "Se multiplica el número de mol por la masa molar del CaCO3.", " g"),
    ],
    ctx=("abc", "Contexto: una cooperativa de mariscadores de ejemplo pregunta si la acidificación podría afectar sus cultivos de moluscos. ¿Qué respuesta es la más honesta?", "Según el modelo, menos carbonato podría dificultar formar conchas, pero hay que medir pH y carbonato en la zona antes de afirmar un efecto", "Sí, todos los cultivos desaparecerán", "No, el pH no importa para las conchas", "La respuesta correcta usa el modelo y reconoce que falta medir en el lugar."),
    sc=[
        ("En Química: ¿qué es el CaCO3?", "El carbonato de calcio, material de conchas y esqueletos", "Se forma a partir de calcio y carbonato disueltos."),
        ("ab", "Al bajar el pH, la concentración de H+:", "Aumenta", "Disminuye", "Un pH menor significa una mayor concentración de H+."),
        ("ab", "El modelo del CO2 en el agua sirve para:", "Predecir tendencias que luego se contrastan con mediciones", "Reemplazar toda medición", "Un modelo se contrasta con datos."),
    ],
    op=("Con el modelo de la ficha {F}: (1) explica en tres oraciones cómo el aumento de CO2 del aire llega a afectar la formación de conchas; (2) indica un supuesto del modelo; (3) propón una medición del océano que permitiría poner a prueba tu explicación.",
        "(1) Más CO2 del aire se disuelve y produce más H+. El H+ consume carbonato. Con menos carbonato, el CaCO3 se forma con más dificultad. (2) Supone equilibrio y temperatura constante. (3) Medir pH y concentración de carbonato en una misma zona durante varios años.",
        ["cadena causal completa", "supuesto identificado", "medición propuesta"],
        ["tres respuestas numeradas"],
        ["saltar un paso de la cadena", "decir que el CO2 sube el pH", "no proponer una medición verificable"],
        "Pregunta: «¿qué resultado te haría dudar de tu explicación?»."),
    reinforce="Escribe la cadena de efectos desde más CO2 en el aire hasta menos CaCO3 formado, con una flecha entre cada paso.",
    extend="Explica por qué una baja pequeña de pH equivale a un cambio relativo grande de H+.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (datos de ejemplo, valores aproximados e ilustrativos; no son mediciones oficiales). CO2 en el aire: período A: 280 ppm; período B: 420 ppm. Océano de ejemplo: pH superficial promedio de 8,2 a 8,1. "
     "Puerto pesquero de ejemplo, desembarque de mariscos por década (en toneladas): década 1: 1.000; década 2: 900; década 3: 700. En ese puerto cambiaron también las zonas de pesca y el número de embarcaciones. "
     "Suelo de ejemplo, materia orgánica: bosque 6 %; cultivo con cobertura vegetal 4 %; suelo desnudo 2 %. "
     "Desarrollo sostenible: satisfacer las necesidades de las personas de hoy sin comprometer la capacidad de las generaciones futuras de satisfacer las suyas.")
build(
    O4, 4, F,
    use="Aprenderé a analizar datos sobre efectos del cambio climático en la atmósfera, el océano y el suelo, y a relacionarlos con el bienestar de las personas y el desarrollo sostenible. Sirve para comunicar qué se sabe, qué no y qué decisiones conviene considerar.",
    prior=["Sé calcular cambios porcentuales.", "Sé que correlación no es causalidad.", "Sé el modelo de equilibrios del CO2 en el agua."],
    explain=[
        "Analizar evidencia es calcular cambios y relacionarlos con las preguntas de la investigación. Si el CO2 del aire pasa de 280 a 420 ppm, el aumento es de 140 ppm, es decir, 140 ÷ 280 × 100 = 50 %. Un porcentaje permite comparar cambios en cosas de distinto tamaño. Los valores de esta clase son aproximados y de ejemplo, así que sirven para practicar el análisis, no para citar cifras.",
        "Cuando dos cosas cambian a la vez, por ejemplo el pH del océano y los desembarques de mariscos, no se puede concluir sin más que una causa a la otra. Pueden influir otras variables, como las zonas de pesca. Se habla de coincidencia en el tiempo (correlación) y se pide más evidencia, como mediciones repetidas en el mismo lugar con variables controladas, antes de afirmar una relación causal.",
        "El bienestar de las personas incluye alimento, agua, trabajo y salud. Si los ecosistemas cambian, esos aspectos pueden verse afectados, por ejemplo los ingresos de un puerto pesquero. El desarrollo sostenible busca decisiones que cuiden a las personas de hoy y a las futuras. En suelos, mantener cobertura vegetal ayuda a conservar la materia orgánica, que almacena carbono y retiene agua.",
    ],
    vocab=[("ppm", "partes por millón, unidad de concentración de un gas en el aire"), ("correlación", "coincidencia en el tiempo entre dos variables"), ("causalidad", "relación en que una variable produce el cambio en otra"), ("desarrollo sostenible", "satisfacer necesidades presentes sin comprometer las futuras"), ("materia orgánica del suelo", "restos de seres vivos que almacenan carbono y retienen agua")],
    worked=[
        ("Cambio porcentual", "En un bosque de ejemplo, la materia orgánica baja de 6 % a 3 % tras el cultivo. ¿Cuál es el cambio porcentual?",
         ["Diferencia: 3 − 6 = −3 puntos.", "Cambio relativo: −3 ÷ 6 × 100.", "El resultado es −50 %."],
         "−50 %"),
        ("Correlación y causa", "En un puerto de ejemplo, el desembarque baja mientras el pH del océano baja. ¿Se puede concluir que el pH es la causa?",
         ["Ambas cosas ocurren a la vez, lo que es una correlación.", "También cambiaron zonas de pesca y número de embarcaciones.", "Sin controlar esas variables no se puede afirmar causalidad."],
         "No, solo hay correlación"),
    ],
    mistakes=[("Concluir causalidad porque dos variables cambian juntas.", "Otras variables pueden explicar el cambio.", "Escribe «coinciden» y propone qué mediciones faltan."),
              ("Dividir el cambio por el valor final en vez del inicial.", "El cambio porcentual se mide respecto del valor de partida.", "Usa siempre el valor inicial como base.")],
    T=[
        ("abc", "En Química: ¿qué es el desarrollo sostenible?", "Satisfacer las necesidades de hoy sin comprometer la capacidad de las generaciones futuras", "Explotar los recursos lo más rápido posible", "Evitar toda actividad humana", "La definición considera a las personas actuales y a las futuras."),
        ("=", "{F} ¿Cuántos ppm aumentó el CO2 del aire entre el período A y el B?", "420-280", "Se resta el valor del período A al del período B.", " ppm"),
        ("=", "{F} ¿Cuál es el cambio porcentual del CO2 del aire entre el período A y el B?", "(420-280)*100/280", "Se divide el aumento por el valor inicial y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el cambio porcentual del desembarque de mariscos entre la década 1 y la década 3?", "(700-1000)*100/1000", "Se divide la diferencia por el valor inicial; el signo negativo indica disminución.", " %"),
        ("abc", "{F} El desembarque de mariscos baja mientras baja el pH del océano. ¿Qué conclusión es prudente?", "Coinciden en el tiempo, pero faltan datos y controles para atribuir la baja a la acidificación", "El pH causó la baja con certeza", "El pH no tiene relación posible", "Cambiaron otras variables, como zonas de pesca y embarcaciones."),
        ("=", "{F} ¿Cuántas toneladas menos se desembarcaron en la década 3 que en la década 1?", "1000-700", "Se resta el valor de la década 3 al de la década 1.", " toneladas"),
        ("{F} ¿Qué suelo de ejemplo tiene más materia orgánica?", "El bosque, con 6 %", "Entre 6, 4 y 2 %, el mayor valor corresponde al bosque."),
        ("=", "{F} ¿Cuántas veces más materia orgánica tiene el bosque que el suelo desnudo?", "6/2", "Se divide el porcentaje del bosque por el del suelo desnudo.", " veces"),
        ("abc", "{F} Comparando cultivo con cobertura y suelo desnudo, ¿qué muestran los datos?", "El suelo con cobertura tiene el doble de materia orgánica (4 % frente a 2 %)", "El suelo desnudo tiene más materia orgánica", "No hay diferencia", "4 % es el doble de 2 %."),
        ("ab", "{F} Para evaluar si la acidificación explica la baja de mariscos, ¿qué dato falta?", "Mediciones de pH y de otras variables, año a año, en el mismo lugar", "Más fotos del puerto", "Hacen falta series repetidas con variables controladas."),
        ("abc", "{F} Si bajan los desembarques, ¿qué consecuencia puede haber para el bienestar de las personas del puerto?", "Menos ingresos y menos alimento local", "Más ingresos de forma automática", "Ninguna consecuencia posible", "Los mariscos son fuente de trabajo y alimento para el puerto."),
        ("abc", "{F} ¿Qué medida es coherente con el desarrollo sostenible para el puerto de ejemplo?", "Seguir midiendo, cuidar la presión de pesca mientras se investiga y diversificar ingresos", "Pescar lo más rápido posible antes de que se acaben", "No hacer nada hasta tener certeza absoluta", "La sostenibilidad cuida el recurso y a las personas, actuando con la mejor información disponible."),
        ("abc", "{F} ¿Qué frase comunica mejor los resultados y su incertidumbre?", "El CO2 del aire aumentó y el pH bajó 0,1 en el ejemplo; la relación con la baja de mariscos requiere más estudios", "El CO2 explicó la baja de mariscos", "No se sabe nada de lo ocurrido", "Una buena comunicación entrega cambios medidos y declara lo que falta."),
    ],
    ctx=("abc", "Contexto: una municipalidad de ejemplo debe presentar a la comunidad costera qué muestran los datos. ¿Qué elige decir?", "Los datos de ejemplo muestran aumento de CO2 y baja de pH y de mariscos; falta establecer si hay causalidad, por lo que se seguirá midiendo y se cuidará el recurso", "El océano ya está arruinado", "No hay ningún cambio", "El mensaje correcto muestra datos, límites y una decisión prudente."),
    sc=[
        ("En Química: ¿qué es la correlación?", "La coincidencia en el tiempo entre dos variables", "Dos variables pueden coincidir sin que una cause la otra."),
        ("ab", "Para afirmar causalidad se necesita:", "Evidencia adicional con variables controladas", "Que dos cosas cambien al mismo tiempo", "La coincidencia por sí sola no basta."),
        ("ab", "El desarrollo sostenible considera:", "A las personas de hoy y a las futuras", "Solo a las personas de hoy", "El concepto incluye a las generaciones futuras también."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula dos cambios porcentuales de la ficha; (2) escribe una conclusión sobre el bienestar de las personas del puerto que no afirme causalidad; (3) propón una decisión sostenible y qué dato adicional pedirías.",
        "(1) CO2: +50 %; mariscos: −30 %. (2) El desembarque bajó 30 % en tres décadas, lo que puede afectar ingresos y alimento, aunque no se sabe si la causa es la acidificación. (3) Reducir la presión de pesca mientras se investiga; pediría series anuales de pH y esfuerzo de pesca.",
        ["dos cálculos correctos", "conclusión sin causalidad", "decisión y dato adicional"],
        ["tres respuestas numeradas"],
        ["afirmar causalidad", "dividir por el valor final", "no justificar la decisión"],
        "Pregunta: «¿qué otra variable podría explicar la baja de mariscos?»."),
    reinforce="Calcula el cambio porcentual de materia orgánica entre el bosque y el suelo desnudo, e interpreta el signo.",
    extend="Explica por qué mantener cobertura vegetal en el suelo puede ayudar a la vez al carbono y al agua del suelo.",
)

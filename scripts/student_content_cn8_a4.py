"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 04 (transporte, intercambio gaseoso y respuesta en plantas)."""
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


OA4 = "CN08 OA 04"

L(OA4, 1,
  materials="Este cuaderno y lápiz. Si quieres comprobarlo en casa: una planta común, un poroto en algodón húmedo y una ventana, sin tocar plantas desconocidas.",
  use="Aprenderé qué estructuras permiten a las plantas transportar sustancias, intercambiar gases y responder al ambiente, y a plantear preguntas investigables. Sirve para ver que las plantas también tienen sistemas organizados.",
  prior=["Sé que la fotosíntesis usa luz, agua y dióxido de carbono.", "Sé distinguir variable independiente y dependiente."],
  explain=[
      "Las plantas tienen estructuras especializadas, como los animales. Las raíces absorben agua y sales minerales del suelo. El xilema es un conjunto de tubos que lleva esa agua y sales hacia arriba, hasta las hojas. El floema lleva los azúcares que se fabrican en las hojas hacia el resto de la planta. Esto se parece al transporte de sustancias por los vasos sanguíneos del cuerpo humano.",
      "El intercambio de gases ocurre por los estomas, que son poros pequeños, sobre todo en la cara inferior de muchas hojas. Por ellos entra dióxido de carbono para la fotosíntesis y sale oxígeno y vapor de agua. Cada estoma está rodeado por dos células guardianas que lo abren y lo cierran. Algo parecido hace el sistema respiratorio humano al intercambiar gases.",
      "Las plantas también responden a estímulos. El fototropismo es el crecimiento del tallo hacia la luz y el gravitropismo es el crecimiento de la raíz hacia abajo. Una pregunta investigable sobre esto es: «¿Cuántos grados se inclina un tallo de poroto hacia una ventana en 5 días?». Indica qué se mide y se contesta con datos.",
  ],
  vocab=[("xilema", "tubos que llevan agua y sales desde la raíz hacia arriba"), ("floema", "tubos que reparten los azúcares fabricados en las hojas"), ("estoma", "poro de la hoja por donde pasan gases y vapor de agua"), ("fototropismo", "crecimiento de una parte de la planta hacia la luz"), ("gravitropismo", "crecimiento de una parte de la planta en respuesta a la gravedad")],
  worked=[
      ("Qué tubo es", "Una sustancia sube desde la raíz con agua y sales minerales. ¿Por qué tubo viaja?", ["Reviso: agua y sales hacia arriba.", "Eso lo hace el xilema."], "Por el xilema"),
      ("Pregunta investigable", "¿Es investigable «¿Se doblan más los tallos hacia la luz de una ventana que hacia una pared?»?", ["Pregunto si se puede medir.", "Se puede medir la inclinación del tallo en grados o centímetros."], "Sí, porque se contesta midiendo la inclinación"),
  ],
  mistakes=[
      ("Confundir xilema y floema.", "El xilema sube agua y sales; el floema reparte azúcares.", "Recuerda xilema = agua que sube."),
      ("Creer que las plantas no tienen estructuras especializadas porque no se mueven.", "Tienen tubos, poros y células que cumplen funciones.", "Piensa en su semejanza con sistemas del cuerpo humano."),
  ],
  rec=[
      ("¿Qué tubos llevan el agua desde la raíz hacia las hojas: el xilema o el floema?", "El xilema", "Transporta agua y sales minerales."),
      ("¿Por dónde entra el dióxido de carbono a la hoja: por los estomas o por la raíz?", "Por los estomas", "Son poros de la hoja."),
      ("Verdadero o falso: el fototropismo es el crecimiento hacia la luz.", "Verdadero", "El tallo se orienta hacia la luz."),
  ],
  und=[
      ("¿Qué lleva el floema? A) Azúcares fabricados en las hojas; B) Agua que sube desde la raíz.", "A", "El agua que sube la lleva el xilema."),
      ("¿Con qué sistema del cuerpo humano se parece el transporte de sustancias de la planta? A) El circulatorio; B) El óseo.", "A", "Ambos transportan sustancias por tubos."),
      ("¿Qué hacen las células guardianas?", "Abren y cierran el estoma", "Regulan el paso de gases y vapor de agua."),
  ],
  app=[
      ("¿Cuál pregunta es investigable? A) ¿Cuántos centímetros crece el tallo de un poroto en la oscuridad y cuántos con luz en una semana? B) ¿Son felices las plantas con la luz?", "A", "Se responde midiendo; la otra es una opinión."),
      ("En «¿Crece más rápido un poroto con luz que en la oscuridad?», ¿qué variable se cambia?", "La cantidad de luz", "Es la condición que difiere entre las dos plantas."),
      ("En esa misma pregunta, ¿qué variable se mide?", "El crecimiento del tallo", "Es el resultado que se registra."),
  ],
  rea=[
      ("Una estudiante dice: «El floema y el xilema son lo mismo porque ambos son tubos». ¿Qué falla ve en su idea? A) Transportan sustancias distintas; B) El xilema no existe.", "A", "El xilema lleva agua y sales; el floema, azúcares."),
      ("Alguien afirma: «Las plantas no necesitan intercambiar gases porque no respiran». ¿Qué proceso lo contradice?", "La fotosíntesis, que necesita dióxido de carbono", "Los gases entran y salen por los estomas."),
  ],
  cha=[
      arith("Datos de ejemplo: un tallo de poroto crece 3 cm al día hacia la luz. ¿Cuántos centímetros crece en 5 días?", "3*5", "Se multiplica el crecimiento diario por los días."),
      ("Una planta se deja de lado sobre una mesa. Con los días, la raíz se curva hacia abajo. ¿Qué respuesta muestra? A) Gravitropismo; B) Fototropismo.", "A", "La raíz responde a la gravedad."),
  ],
  context=[("Una persona de tu casa deja una maceta junto a una ventana y nota que las hojas se orientan hacia el vidrio. ¿Qué respuesta de la planta es?", "Fototropismo", "La planta crece hacia la luz.")],
  selfcheck=[("¿Para qué sirven los estomas?", "Para el paso de gases y vapor de agua", "Regulan el intercambio con el aire."), ("¿Qué lleva el xilema?", "Agua y sales minerales hacia arriba", "Va desde la raíz a las hojas."), ("¿Qué es el fototropismo?", "El crecimiento hacia la luz", "Es una respuesta a un estímulo.")],
  open_task=task("Escribe una pregunta investigable sobre cómo responde una planta a la luz usando un poroto en algodón húmedo junto a una ventana y otro en un lugar oscuro. Indica la variable que cambias, la que mides, dos que controlas y una predicción.", "Pregunta: ¿Crece más el tallo de un poroto con luz que en la oscuridad en 7 días? Cambio: luz. Mido: centímetros de crecimiento. Controlo: cantidad de agua y tipo de algodón. Predicción: crecerá más hacia la luz.", ["pregunta con variables", "dos controladas", "una predicción"], ["pregunta y plan breve"], ["no decir qué se mide", "cambiar la luz y el agua a la vez"], "Pregunta qué resultado contradiría tu predicción."),
  reinforce="Escribe una función del xilema y una del floema.",
  extend="Explica por qué las plantas necesitan intercambiar gases con el aire.")

L(OA4, 2,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en cada ejercicio.",
  use="Aprenderé a examinar datos y descripciones de estomas, xilema y floema para sacar conclusiones. Sirve para interpretar evidencia sobre el transporte y los gases.",
  prior=["Sé qué hacen xilema, floema y estomas.", "Sé calcular razones y cambios con enteros."],
  explain=[
      "Una evidencia clásica del transporte es poner un tallo de apio en agua con colorante de alimentos. Después de unas horas, las nervaduras se tiñen: el colorante subió por el xilema. Datos de ejemplo: a las 2 horas el color subió 6 cm; a las 4 horas, 12 cm. La rapidez es 12 ÷ 4 = 3 cm por hora.",
      "Otra evidencia es contar estomas. En muchas hojas hay más estomas en la cara inferior que en la superior. Datos de ejemplo: en la cara inferior se cuentan 180 estomas por milímetro cuadrado (mm²) y en la superior, 30. La cara inferior tiene 6 veces más (180 ÷ 30 = 6). Eso se relaciona con perder menos agua, pues el sol da más en la cara superior.",
      "Al examinar evidencia hay que distinguir la observación (el colorante subió) de la conclusión (se transporta por el xilema), indicar el dato decisivo y declarar una limitación. Por ejemplo, un solo tallo de apio es una muestra pequeña. También hay que fijarse en la escala de cada representación: «por mm²» no es lo mismo que «en toda la hoja».",
  ],
  vocab=[("nervadura", "línea de la hoja que contiene xilema y floema"), ("muestra", "grupo pequeño que se estudia para sacar conclusiones"), ("densidad de estomas", "número de estomas por milímetro cuadrado"), ("rapidez de ascenso", "distancia que sube una sustancia dividida por el tiempo"), ("escala", "unidad o tamaño al que se refiere el dato")],
  worked=[
      ("Rapidez del colorante", "El color sube 15 cm en 5 horas. ¿Cuál es su rapidez?", ["Rapidez = distancia ÷ tiempo.", "15 ÷ 5 = 3."], "3 cm por hora"),
      ("Comparar estomas", "La cara inferior tiene 120 estomas por mm² y la superior 40. ¿Cuántas veces más tiene la inferior?", ["Divido 120 entre 40.", "120 ÷ 40 = 3."], "3 veces más"),
  ],
  mistakes=[
      ("Generalizar desde un solo tallo.", "Una muestra pequeña puede dar un resultado distinto al promedio.", "Repite con varios tallos."),
      ("Confundir estomas por mm² con estomas totales de la hoja.", "La escala es distinta.", "Revisa la unidad antes de comparar."),
  ],
  rec=[
      ("En el experimento del apio con colorante, ¿por dónde sube el colorante: por el xilema o por el floema?", "Por el xilema", "Allí viaja el agua con lo disuelto."),
      ("¿En qué cara de la hoja hay más estomas en muchas plantas: la inferior o la superior?", "La inferior", "Así se pierde menos agua por el sol."),
      ("Verdadero o falso: una muestra pequeña puede dar una conclusión poco confiable.", "Verdadero", "Conviene repetir con más muestras."),
  ],
  und=[
      ("El color subió por las nervaduras del apio. ¿Qué indica? A) Que el agua con lo disuelto sube por tubos; B) Que el apio fabrica colorante.", "A", "La subida muestra el transporte por xilema."),
      ("¿Por qué conviene contar estomas en varias zonas de la hoja? A) Para tener una estimación confiable; B) Porque los estomas aparecen al contarlos.", "A", "Una sola zona podría no ser representativa."),
      ("Un dato dice «80 estomas por mm²». ¿Qué escala usa?", "Estomas en una superficie de un milímetro cuadrado", "El dato se refiere a un mm² de hoja."),
  ],
  app=[
      arith("Datos de ejemplo: el colorante subió 8 cm en 2 horas y 20 cm en 5 horas. ¿Cuántos cm más subió en el período entre ambas mediciones?", "20-8", "Se resta la primera altura a la segunda."),
      arith("Una hoja tiene 200 estomas por mm² en la cara inferior y 25 en la superior. ¿Cuántas veces más tiene la inferior?", "200//25", "Se divide el mayor por el menor."),
      arith("En una zona de 3 mm² de la cara inferior hay 90 estomas por mm². ¿Cuántos estomas hay en esa zona?", "3*90", "Se multiplica la superficie por la densidad."),
  ],
  rea=[
      ("Un grupo dice: «El colorante subió 2 cm en un tallo cortado; por lo tanto, todas las plantas transportan agua a 2 cm por hora». ¿Qué falla tiene? A) Generaliza desde un solo caso y sin datos de tiempo; B) El colorante no sube.", "A", "No se pueden extender los resultados de una muestra a todas las plantas."),
      ("En una hoja de ejemplo, la cara superior tiene 20 estomas por mm² y la inferior 160. Explica en una frase por qué esto puede reducir la pérdida de agua.", "Porque hay menos estomas en la cara más expuesta al sol", "Menos estomas en la cara superior reduce la pérdida de vapor."),
  ],
  cha=[
      ("Se tiñó un tallo de apio y se cortó a 5 cm de la base: se ven puntos de color. ¿Qué conclusión es la más prudente? A) El colorante subió por tubos que se ven como puntos en el corte; B) El apio no tiene tubos.", "A", "Los puntos coloreados son los haces con xilema."),
      ("Un cuadro de ejemplo registra la altura del colorante cada hora: 4, 8, 12, 16 y 20 cm. ¿Cuántos cm sube por hora, de forma constante?", "4", "Entre dos mediciones consecutivas hay 4 cm.", ),
  ],
  context=[arith("En un cuadro de ejemplo, dos hojas del mismo tamaño tienen 2 mm² cada una examinada: una con 70 estomas por mm² y otra con 110. ¿Cuántos estomas más hay en la segunda zona examinada?", "2*110-2*70", "Se calculan los totales por zona y se resta.")],
  selfcheck=[("¿Qué muestra el apio con colorante?", "Que el agua sube por tubos", "El color sigue el camino del xilema."), ("¿Por qué una muestra pequeña es una limitación?", "Porque puede no representar a las demás", "Hay que repetir."), ("¿Qué significa «por mm²»?", "Que se cuenta en un milímetro cuadrado", "Es la escala del dato.")],
  open_task=task("Con estos datos de ejemplo (apio con colorante: 2 h, 10 cm; 4 h, 20 cm; 6 h, 30 cm) haz una tabla con la rapidez en cada intervalo y escribe una conclusión con una limitación.", "Cada intervalo de 2 h sube 10 cm, o sea 5 cm por hora; la rapidez se mantiene constante en este ejemplo. Conclusión: el colorante sube por el xilema a rapidez constante. Limitación: un solo tallo.", ["tabla con tres valores", "conclusión coherente", "una limitación"], ["tabla y frase"], ["confundir observación y conclusión", "olvidar la limitación"], "Pregunta qué pasaría si el apio estuviera en un lugar más caluroso."),
  reinforce="Calcula cuántos cm sube el color en 3 horas si sube 4 cm por hora.",
  extend="Explica por qué una muestra de un solo tallo es una limitación.")

L(OA4, 3,
  materials="Este cuaderno y lápiz. Las tablas están escritas en los ejercicios.",
  use="Aprenderé a construir y contrastar un modelo que compara la planta con el cuerpo humano. Sirve para explicar el transporte, el intercambio de gases y la respuesta a estímulos con un modelo y sus límites.",
  prior=["Sé qué hacen xilema, floema y estomas.", "Sé que el sistema circulatorio y el respiratorio humanos intercambian sustancias."],
  explain=[
      "Un modelo comparativo relaciona estructuras de la planta con las del cuerpo humano que cumplen un papel parecido. Xilema y floema se parecen a los vasos sanguíneos, porque transportan sustancias por tubos. Los estomas se parecen a las vías de entrada de aire de los pulmones, porque dejan pasar gases. Las hormonas vegetales se parecen a las hormonas humanas, que son mensajeros químicos.",
      "Pero el modelo tiene límites. La planta no tiene corazón: el agua sube por la fuerza de la transpiración (pérdida de vapor de agua por los estomas), que tira del agua dentro del xilema, y por la absorción en la raíz. La sangre circula en un circuito cerrado y la savia del xilema solo sube. Las plantas no tienen nervios; responden por cambios hormonales más lentos.",
      "Un buen modelo declara qué estructura corresponde a cuál, qué función comparten y qué no se parece. Al contrastarlo con la evidencia se mejora. Si el apio teñido muestra que el color sube sin bomba, el modelo no debe poner un «corazón» en la planta.",
  ],
  vocab=[("transpiración", "pérdida de vapor de agua por los estomas"), ("savia", "líquido que circula por xilema y floema"), ("hormona vegetal", "mensajero químico que regula el crecimiento de una planta"), ("circuito cerrado", "recorrido en el que la sangre vuelve al punto de partida"), ("modelo comparativo", "modelo que relaciona estructuras de dos sistemas")],
  worked=[
      ("Parte equivalente", "En el modelo comparativo, ¿qué estructura humana se parece al xilema y al floema?", ["Transportan sustancias por tubos.", "En el cuerpo lo hacen los vasos sanguíneos."], "Los vasos sanguíneos"),
      ("Límite del modelo", "¿Qué falla tiene decir que la planta tiene un «corazón» que bombea la savia?", ["La planta no tiene corazón.", "El agua sube por transpiración y absorción."], "Que la planta no tiene bomba: el agua sube por transpiración y absorción"),
  ],
  mistakes=[
      ("Creer que las plantas tienen sangre y corazón.", "Tienen savia, que no circula en circuito cerrado.", "Compara la función, no la estructura exacta."),
      ("Pensar que un modelo comparativo es una copia exacta.", "Solo muestra semejanzas de función.", "Siempre agrega los límites."),
  ],
  rec=[
      ("¿Con qué se parece el xilema en el cuerpo humano: con los vasos sanguíneos o con los huesos?", "Con los vasos sanguíneos", "Ambos transportan sustancias por tubos."),
      ("¿Qué es la transpiración de una planta?", "Pérdida de vapor de agua por los estomas", "Ayuda a que el agua suba."),
      ("Verdadero o falso: las plantas tienen corazón.", "Falso", "El agua sube sin bomba."),
  ],
  und=[
      ("¿Qué parte de una planta se parece a una vía de entrada de aire de los pulmones? A) Los estomas; B) La raíz.", "A", "Dejan pasar gases."),
      ("¿Por qué el modelo con «corazón» no sirve? A) Porque la savia sube sin una bomba; B) Porque la planta no tiene agua.", "A", "El agua sube por transpiración."),
      ("¿Qué se parece entre las hormonas vegetales y las humanas?", "Son mensajeros químicos", "Regulan funciones y crecimiento."),
  ],
  app=[
      ("Une cada estructura vegetal con su equivalente humano: xilema y floema; estomas. Opciones: vasos sanguíneos; vías de paso de aire. ¿A qué corresponde «estomas»?", "A las vías de paso de aire", "Ambas dejan pasar gases."),
      ("Una tabla de ejemplo dice que el modelo compara «sistema de transporte» con «circulatorio». ¿Qué diferencia debe agregar sobre la savia? A) Solo sube por el xilema y no recorre un circuito cerrado; B) Es roja como la sangre.", "A", "Es un límite real del modelo."),
      arith("En un modelo de ejemplo, un árbol pierde 40 litros de agua por transpiración en un día y absorbe 38 litros. ¿Cuántos litros más pierde de los que absorbe?", "40-38", "Se resta lo absorbido a lo perdido."),
  ],
  rea=[
      ("Una afirmación dice: «Si la planta no tiene corazón, no puede mover agua hacia arriba». ¿Qué evidencia la contradice? A) El apio teñido muestra que el color sube sin bomba; B) El apio no tiene tubos.", "A", "La evidencia directa indica ascenso sin bomba."),
      ("¿Por qué las plantas responden más lento que los animales a los estímulos? Responde en una frase.", "Porque responden con hormonas y crecimiento, y no con nervios", "El cambio hormonal tarda más."),
  ],
  cha=[
      ("Un compañero propone el modelo: «el estoma es un vaso sanguíneo». ¿Es una buena comparación de función? Responde Sí o No.", "No", "El estoma deja pasar gases y vapor de agua; el vaso sanguíneo transporta sangre."),
      ("Un modelo de ejemplo dice que una planta pierde 50 mL de agua y absorbe 52 mL en un día. ¿Qué pasa con el agua de la planta? A) Ganó 2 mL; B) Perdió 2 mL.", "A", "Absorbió más de lo que perdió: 52 − 50 = 2."),
  ],
  context=[("En un huerto de ejemplo, una planta de tomate recibe poco riego y a mediodía sus hojas se marchitan porque las células pierden agua. ¿Qué tubos llevan el agua del suelo hasta esas hojas: el xilema o el floema?", "El xilema", "Sin agua suficiente, las células pierden firmeza.")],
  selfcheck=[("¿Con qué se parecen xilema y floema?", "Con los vasos sanguíneos", "Transportan sustancias por tubos."), ("¿Qué limita al modelo de la planta con corazón?", "Que la planta no tiene bomba", "El agua sube por transpiración."), ("¿Qué debe declarar un modelo comparativo?", "Semejanzas y límites", "Para no exagerar.")],
  open_task=task("Haz una tabla de tres filas con la estructura vegetal, su equivalente humano y un límite de la comparación: (1) xilema y floema, (2) estomas, (3) hormonas vegetales. Escribe una frase final con la pregunta que aún no responde tu modelo.", "(1) Vasos sanguíneos; la savia no circula en circuito cerrado. (2) Vías de paso de aire; los estomas también dejan salir vapor de agua. (3) Hormonas humanas; las vegetales actúan más lento. Pregunta: ¿cómo sube el agua en un árbol muy alto?", ["tres filas completas", "un límite por fila", "una pregunta abierta"], ["tabla y pregunta"], ["decir que la planta tiene sangre", "no señalar límites"], "Pregunta qué evidencia aportarías para probar un límite."),
  reinforce="Escribe una semejanza y una diferencia entre el xilema y un vaso sanguíneo.",
  extend="Explica por qué un modelo útil debe decir qué no explica.")

L(OA4, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a relacionar variables como luz, temperatura y viento con la transpiración y el crecimiento de las plantas. Sirve para planificar y leer experimentos sobre respuestas de las plantas.",
  prior=["Sé qué es la transpiración.", "Sé que un experimento justo cambia una sola variable."],
  explain=[
      "La transpiración depende del ambiente. Con más luz, los estomas se abren y la planta pierde más agua. Con más temperatura y más viento, el vapor sale más rápido. Con aire muy húmedo, sale menos. Estas son relaciones entre variables: la variable ambiental cambia y la pérdida de agua es la variable que se mide.",
      "Datos de ejemplo: tres plantas iguales pierden agua en 1 hora. A la sombra pierden 4 g, con luz del día 10 g y con luz y viento 16 g. La diferencia entre luz y sombra es 10 − 4 = 6 g. Para que la comparación sea justa, se mantiene igual el tamaño de la planta y la cantidad de agua inicial.",
      "En las respuestas a estímulos, la relación también se mide. Un tallo se inclina hacia la luz porque la hormona auxina se acumula en el lado sombreado, donde hace que las células crezcan más. Ese lado se alarga más y el tallo se curva hacia la luz. Una gráfica de ángulo de inclinación contra tiempo muestra una curva que sube.",
  ],
  vocab=[("auxina", "hormona vegetal que estimula el crecimiento de las células"), ("humedad del aire", "cantidad de vapor de agua que hay en el aire"), ("variable ambiental", "condición del ambiente que se cambia o se mide"), ("tasa de pérdida", "cantidad de agua perdida en un tiempo"), ("curva", "forma que muestra la relación entre dos variables")],
  worked=[
      ("Comparar con luz y sombra", "Una planta pierde 5 g de agua a la sombra y 12 g con luz en una hora. ¿Cuántos gramos más pierde con luz?", ["Resto: 12 − 5.", "12 − 5 = 7."], "7 g más"),
      ("Por qué se curva el tallo", "¿En qué lado del tallo se acumula la auxina cuando la luz llega desde un lado?", ["La auxina se acumula en el lado sombreado.", "Ese lado crece más y el tallo se curva hacia la luz."], "En el lado sombreado"),
  ],
  mistakes=[
      ("Creer que la planta se inclina porque el lado con luz crece más.", "El lado sombreado es el que crece más, por la auxina.", "Recuerda que la auxina se acumula donde hay sombra."),
      ("Cambiar la luz y el viento a la vez.", "No se sabría cuál variable causó la pérdida de agua.", "Cambia una variable y controla las otras."),
  ],
  rec=[
      ("Con más luz, ¿los estomas se abren más o se cierran?", "Se abren más", "La planta realiza más fotosíntesis y pierde más vapor."),
      ("¿Con aire muy húmedo la transpiración aumenta o disminuye?", "Disminuye", "Sale menos vapor si el aire ya tiene mucha agua."),
      ("Verdadero o falso: la auxina se acumula en el lado sombreado del tallo.", "Verdadero", "Eso hace que ese lado crezca más."),
  ],
  und=[
      ("¿Cuál variable cambia en: «¿Pierde más agua una planta con viento que sin viento?»? A) El viento; B) El tamaño de la planta.", "A", "Es la condición que se compara."),
      ("¿Por qué el tallo se curva hacia la luz? A) El lado sombreado crece más; B) El lado iluminado crece más.", "A", "La auxina estimula el crecimiento del lado con sombra."),
      ("Con alta temperatura y viento, ¿qué ocurre con el vapor que sale de la hoja?", "Sale más rápido", "Ambas condiciones favorecen la transpiración."),
  ],
  app=[
      arith("Datos de ejemplo: una planta pierde 4 g a la sombra y 16 g con luz y viento. ¿Cuántos gramos más pierde con luz y viento?", "16-4", "Se resta lo perdido en sombra a lo perdido con luz y viento."),
      arith("Tres plantas pierden 6, 9 y 12 g de agua en una hora. ¿Cuál es el promedio de pérdida?", "(6+9+12)//3", "Se suman y se divide por 3."),
      arith("Un tallo se inclina 4 grados cada día. ¿Cuántos grados se inclina en 6 días si el ritmo es constante?", "4*6", "Se multiplica la inclinación diaria por los días."),
  ],
  rea=[
      ("Un grupo compara una planta grande a la luz con una planta pequeña a la sombra y concluye que la luz hace perder más agua. ¿Qué falla tiene? A) Cambió también el tamaño de la planta; B) No usó plantas.", "A", "Dos variables cambiaron a la vez."),
      ("Una persona dice: «El aire húmedo provoca que la planta pierda más agua». ¿Qué corrección haces?", "El aire húmedo disminuye la pérdida de agua", "Con aire más húmedo, sale menos vapor."),
  ],
  cha=[
      ("Datos de ejemplo de pérdida de agua en una hora según la temperatura: 10 °C, 3 g; 20 °C, 7 g; 30 °C, 12 g. ¿Qué relación se observa? A) A mayor temperatura, mayor pérdida de agua; B) A mayor temperatura, menor pérdida de agua.", "A", "Los valores aumentan al subir la temperatura."),
      arith("Con esos datos de ejemplo (3, 7 y 12 g a 10, 20 y 30 °C), ¿cuántos gramos más se pierden a 30 °C que a 10 °C?", "12-3", "Se resta la pérdida de 10 °C a la de 30 °C."),
  ],
  context=[("Una jardinera de ejemplo riega sus plantas en la tarde y no a mediodía. Con lo visto, ¿qué ventaja tiene? A) Se pierde menos agua por evaporación y transpiración; B) Las plantas crecen sin luz.", "A", "A mediodía hay más temperatura y luz.")],
  selfcheck=[("¿Cómo afecta la luz a la transpiración?", "La aumenta porque los estomas se abren", "También sube la fotosíntesis."), ("¿Dónde se acumula la auxina?", "En el lado sombreado", "Ahí hay más crecimiento."), ("¿Por qué se controlan las variables?", "Para saber cuál causó el efecto", "Se cambia solo una.")],
  open_task=task("Diseña un experimento seguro con tres plantas de poroto iguales para ver el efecto de la luz en el crecimiento del tallo: dónde pondrías cada planta, qué variable cambias, qué mides cada día, dos variables que controlas y una tabla vacía para 5 días.", "Plantas A (ventana), B (sombra), C (oscuridad). Cambio: luz. Mido: altura del tallo en cm. Controlo: agua y tipo de algodón. Tabla: día 1 a 5, altura de A, B y C.", ["tres condiciones", "variable medida clara", "tabla de 5 días"], ["plan y tabla"], ["no controlar el riego", "olvidar la tabla"], "Pregunta qué cambiarías si una planta se secara."),
  reinforce="Escribe una condición que aumenta la pérdida de agua por transpiración.",
  extend="Explica por qué el lado sombreado del tallo crece más que el lado con luz.")

L(OA4, 5,
  materials="Este cuaderno y lápiz. Los ejemplos están escritos en los ejercicios.",
  use="Aprenderé a explicar el mecanismo del transporte de agua y de azúcares en una planta y cómo las respuestas a estímulos se relacionan con estructuras especializadas. Sirve para unir las ideas de todo el OA.",
  prior=["Sé qué hacen xilema, floema, estomas y hormonas vegetales.", "Sé que la osmosis mueve agua hacia donde hay más soluto."],
  explain=[
      "El camino del agua comienza en la raíz: los pelos absorbentes toman agua del suelo por osmosis, porque dentro de las células hay más soluto. El agua entra al xilema y sube hasta las hojas. En las hojas, parte del agua se usa en la fotosíntesis y la mayor parte sale como vapor por los estomas (transpiración). La transpiración tira del agua dentro del xilema, como una pajilla al succionar, y mantiene la columna de agua unida.",
      "Los azúcares fabricados en las hojas viajan por el floema hasta donde se necesitan: raíces, frutos y zonas de crecimiento. El intercambio de gases ocurre por los estomas, que se abren cuando las células guardianas se llenan de agua (turgentes) y se cierran cuando se pierden agua. Esto relaciona el intercambio gaseoso con la osmosis.",
      "Los patrones en las respuestas a estímulos tienen explicación. El tallo crece hacia la luz (fototropismo positivo) y hacia arriba (gravitropismo negativo). La raíz crece hacia abajo (gravitropismo positivo) y hacia el agua. Explicar un mecanismo significa decir el estímulo, la estructura que lo recibe y el cambio que ocurre, sin saltarse pasos.",
  ],
  vocab=[("pelo absorbente", "prolongación de las células de la raíz que absorbe agua"), ("tracción por transpiración", "fuerza con que la pérdida de agua tira de la columna de agua"), ("células guardianas", "células que abren y cierran el estoma"), ("estímulo", "cambio del ambiente que provoca una respuesta"), ("mecanismo", "serie de pasos que explica cómo ocurre algo")],
  worked=[
      ("Camino del agua", "Ordena mentalmente el camino del agua desde el suelo hasta el aire: raíz, hojas, xilema, estomas. ¿Cuál es el orden?", ["El agua entra por la raíz.", "Sube por el xilema.", "Llega a las hojas y sale por los estomas."], "Raíz, xilema, hojas, estomas"),
      ("Apertura del estoma", "¿Qué pasa en las células guardianas para que el estoma se abra?", ["Entra agua a las células guardianas.", "Se ponen turgentes y se separan, abriendo el poro."], "Se llenan de agua y se ponen turgentes"),
  ],
  mistakes=[
      ("Pensar que el agua sube porque la raíz la empuja con una bomba.", "La transpiración y la absorción explican el ascenso.", "Describe los pasos de absorción, xilema y transpiración."),
      ("Creer que los estomas se abren solos sin relación con el agua.", "Se abren cuando las células guardianas se llenan de agua.", "Relaciona con osmosis."),
  ],
  rec=[
      ("¿Dónde absorbe agua la planta: en la raíz o en la hoja?", "En la raíz", "Los pelos absorbentes toman agua del suelo."),
      ("¿Por dónde sale la mayor parte del agua que sube a la hoja?", "Por los estomas", "Sale como vapor en la transpiración."),
      ("Verdadero o falso: el floema reparte los azúcares fabricados en las hojas.", "Verdadero", "Los lleva a raíces, frutos y zonas de crecimiento."),
  ],
  und=[
      ("¿Por qué entra agua a los pelos absorbentes? A) Por osmosis, porque dentro hay más soluto; B) Porque la raíz la empuja con un corazón.", "A", "El agua va hacia donde hay más soluto."),
      ("¿Qué pasa con las células guardianas cuando se llenan de agua? A) Se abre el estoma; B) Se cierra el estoma.", "A", "Al ponerse turgentes se separan y abren el poro."),
      ("¿Por qué la transpiración ayuda a subir el agua?", "Porque tira de la columna de agua dentro del xilema", "Al salir agua por las hojas, sube más desde abajo."),
  ],
  app=[
      ("Cuatro estructuras: raíz, xilema, hoja, floema. ¿Cuántas participan en el camino del agua desde el suelo hasta la hoja?", "3", "Son la raíz, el xilema y la hoja."),
      ("Una raíz crece hacia abajo y un tallo crece hacia arriba. ¿Qué respuesta muestran ambos? A) Gravitropismo; B) Fototropismo.", "A", "Responden a la gravedad."),
      arith("Un árbol de ejemplo absorbe 120 litros de agua en un día y usa 6 en la fotosíntesis. Si se ignora el agua que la planta guarda, ¿cuántos litros salen como vapor por transpiración?", "120-6", "Se resta el agua usada a la absorbida."),
  ],
  rea=[
      ("En un día muy seco y con viento, una planta cierra sus estomas. ¿Qué ventaja tiene? A) Pierde menos agua, aunque entra menos dióxido de carbono; B) Hace más fotosíntesis.", "A", "Cerrar el estoma reduce la pérdida de agua."),
      ("Una planta sin agua en el suelo se marchita. Explica en una frase qué pasa en las células guardianas.", "Pierden agua, se ponen flácidas y el estoma se cierra", "Sin agua, las células guardianas no están turgentes."),
  ],
  cha=[
      ("Un tallo se pone en una caja con una rendija de luz al lado izquierdo. Con los días se curva hacia la izquierda. ¿En qué lado hay más auxina? Escribe derecho o izquierdo.", "Derecho", "La auxina se acumula en el lado sombreado, el derecho."),
      ("Explica el mecanismo de la respuesta del tallo con tres palabras clave: estímulo, auxina y crecimiento.", "La luz es el estímulo; la auxina se acumula en el lado sombreado; ese lado crece más y el tallo se curva", "Es un mecanismo con estímulo, mensajero y respuesta."),
  ],
  context=[("Una persona de ejemplo pone una planta en un rincón oscuro y, a los días, sus tallos se estiran hacia una rendija de luz. ¿Qué estímulo causa esa respuesta?", "La luz", "El tallo crece hacia la luz: fototropismo.")],
  selfcheck=[("¿Cuál es el camino del agua en una planta?", "Raíz, xilema, hojas y estomas", "Sale como vapor."), ("¿Qué abre el estoma?", "Las células guardianas llenas de agua", "Se ponen turgentes y se separan."), ("¿Cómo se orienta la raíz?", "Hacia abajo", "Es gravitropismo positivo.")],
  open_task=task("Escribe un texto de cinco o seis oraciones que explique el mecanismo del camino del agua en una planta, desde la raíz hasta el aire, con las palabras: osmosis, xilema, transpiración y estoma. Agrega una oración sobre qué pasa si falta agua en el suelo.", "El agua entra a la raíz por osmosis y sube por el xilema. En las hojas sale como vapor por los estomas (transpiración), y esa pérdida tira del agua hacia arriba. Si falta agua en el suelo, las células guardianas pierden turgencia y el estoma se cierra.", ["usa las cuatro palabras", "respeta el orden", "incluye la consecuencia"], ["texto de cinco o seis oraciones"], ["invertir el orden", "decir que el agua sube por una bomba"], "Pregunta qué cambia si la planta está en un lugar muy ventoso."),
  reinforce="Escribe en orden el camino del agua en una planta.",
  extend="Explica cómo se relacionan los estomas con la osmosis.")

"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 01 (fósiles, estratos y antigüedad relativa) y OA 02 (evidencias de evolución y selección natural)."""
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


OA1 = "CN1M OA 01"
OA2 = "CN1M OA 02"

# ---------------------------------------------------------------- OA 01

L(OA1, 1,
  materials="Este cuaderno y lápiz. Todos los casos y datos están escritos en el cuaderno; no necesitas salir de tu casa.",
  use="Aprenderé qué es un fósil, cómo se forma a partir de restos de animales y plantas y cómo se escribe una pregunta que se puede investigar sobre ellos. Sirve para separar un hecho comprobable de una opinión.",
  prior=["Sé que los seres vivos mueren y se descomponen.", "Sé que una pregunta se puede contestar con observaciones o mediciones."],
  explain=[
      "Un fósil es un resto o una huella de un ser vivo del pasado que quedó conservado en una roca. Puede ser una concha, un hueso, una hoja, una pisada o el hueco que dejó un organismo. Un hueso reciente que encuentras en la tierra no es un fósil, porque no se conservó en la roca ni pasó por un proceso largo.",
      "La fosilización necesita condiciones especiales. Primero, el organismo muere y es cubierto rápido por sedimentos, que son partículas como barro o arena. Ese entierro lo protege de carroñeros, del oxígeno y de la descomposición. Después, durante miles de años, el agua deja minerales que rellenan o reemplazan los restos: eso se llama mineralización. Las partes duras, como conchas, huesos y madera, se conservan mucho mejor que las partes blandas.",
      "Una pregunta investigable se contesta con observaciones o mediciones e indica qué se observa o qué se cuenta. «¿Qué partes de un animal aparecen más veces como fósil en una roca marina?» se puede investigar contando. «¿Es bonito un fósil?» no, porque depende del gusto de cada persona.",
  ],
  vocab=[("fósil", "resto o huella de un ser vivo antiguo conservado en una roca"), ("sedimento", "partículas como barro o arena que se depositan en capas"), ("mineralización", "proceso en que los minerales del agua rellenan o reemplazan los restos"), ("molde", "hueco con la forma de un organismo que quedó en la roca"), ("pregunta investigable", "pregunta que se contesta observando o midiendo")],
  worked=[
      ("¿Es un fósil?", "Una persona encuentra una concha marina convertida en piedra dentro de una roca de un cerro, lejos del mar actual. ¿Es un fósil?", ["Reviso si es un resto de un ser vivo: es una concha.", "Reviso si está conservada en una roca: sí, convertida en piedra.", "Cumple las dos condiciones del concepto."], "Sí, es un fósil"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Son fascinantes las huellas fósiles?» para que se pueda investigar.", ["Quito la palabra que depende de la opinión: «fascinantes».", "Indico qué se observa o se cuenta: huellas en una roca.", "Queda: «¿Cuántas huellas de cada tamaño hay en una roca de 1 m²?»"], "«¿Cuántas huellas de cada tamaño hay en una roca de 1 m²?»"),
  ],
  mistakes=[
      ("Llamar fósil a cualquier hueso que se encuentra enterrado.", "Un fósil debe ser muy antiguo y estar conservado en la roca.", "Pregunta siempre si el resto está dentro de una roca y si pasó por un proceso largo."),
      ("Creer que todos los seres vivos se fosilizan.", "Se necesita entierro rápido y, de preferencia, partes duras; casi todos los organismos se descomponen.", "Recuerda que los fósiles son una muestra incompleta de la vida del pasado."),
  ],
  rec=[
      ("¿Qué es un fósil?", "Un resto o huella de un ser vivo antiguo conservado en una roca", "Ese es el concepto de fósil."),
      ("Verdadero o falso: las partes duras, como conchas y huesos, se fosilizan con más facilidad que las partes blandas.", "Verdadero", "Las partes duras resisten más la descomposición."),
      ("¿Qué material, como barro o arena, debe cubrir rápido a un organismo muerto para que pueda fosilizarse?", "Sedimentos", "El sedimento lo protege de carroñeros y de la descomposición."),
  ],
  und=[
      ("¿Cuál es un fósil? A) Una concha de caracol que dejó el mar en la playa hoy; B) La huella de un helecho conservada en una roca muy antigua.", "B", "La huella está en la roca y es de un organismo del pasado; la concha de hoy no lo es."),
      ("¿Por qué ayuda un entierro rápido a que un organismo se fosilice? A) Protege los restos de carroñeros y de la descomposición; B) Hace que el cuerpo crezca dentro del sedimento.", "A", "El sedimento aísla los restos y retrasa su destrucción."),
      ("Una concha se disuelve y deja en la roca un hueco con su forma. ¿Cómo se llama ese hueco?", "Molde", "El molde conserva la forma aunque ya no esté la concha."),
  ],
  app=[
      ("Para saber si las conchas se conservan mejor que las medusas, ¿qué dato necesita una investigadora? A) Contar cuántos fósiles de cada tipo hay en las mismas rocas; B) Preguntar a la gente cuál animal le parece más famoso.", "A", "Una pregunta investigable se contesta contando observaciones."),
      arith("En una cantera de ejemplo se contaron 48 fósiles de conchas, 15 de huesos y 3 de huellas. ¿Cuántos fósiles se contaron en total?", "48+15+3", "Se suman las tres cantidades contadas."),
      ("Dos lugares de ejemplo: en uno, un lago calmo cubre el fondo con barro fino; en el otro, un río rápido arrastra los restos. ¿Dónde es más probable que se conserve una hoja delicada? Responde lago o río.", "Lago", "El barro fino la cubre sin romperla; el río rápido la destruye o la arrastra."),
  ],
  rea=[
      ("Un compañero dice: «Una momia de ratón encontrada en una casa hace 60 años es un fósil». ¿Qué responderías? A) No lo es, porque no se conservó en una roca ni pasó por un proceso largo de mineralización; B) Sí lo es, porque es un resto de animal.", "A", "Que sea un resto no basta: el concepto exige conservación en roca por un proceso largo."),
      ("En rocas marinas antiguas aparecen muchas conchas fósiles y casi ningún fósil de medusas. ¿Cuál es la mejor explicación? A) Las partes blandas se descomponen antes de quedar cubiertas, y las conchas duras resisten; B) Las medusas nunca vivieron en el mar.", "A", "La diferencia se explica por la dureza de las partes del cuerpo."),
  ],
  cha=[
      ("Tres sitios de ejemplo: S1, un delta donde el barro entierra rápido a los animales muertos; S2, un desierto abierto donde los cuerpos quedan al aire; S3, un bosque con suelo húmedo y muchos descomponedores. ¿En cuál esperarías más fósiles? Responde S1, S2 o S3.", "S1", "El entierro rápido protege los restos; en los otros dos se destruyen antes."),
      arith("En un sitio de ejemplo con entierro rápido se encuentran 3 fósiles por cada metro cuadrado. Si se excavan 12 metros cuadrados, ¿cuántos fósiles se esperan?", "3*12", "Se multiplica la cantidad por metro cuadrado por la superficie excavada."),
  ],
  context=[arith("Una persona visita una cantera de ejemplo y anota 9 conchas en la primera pared, 7 en la segunda y 4 huellas en la tercera. ¿Cuántos restos anotó en total?", "9+7+4", "Se suman los restos de las tres paredes.")],
  selfcheck=[("Define fósil con tus propias palabras.", "Un resto o huella de un ser vivo antiguo conservado en una roca", "Debe estar en la roca y ser antiguo."), ("¿Por qué las partes duras se fosilizan más fácil?", "Porque resisten más la descomposición", "Las partes blandas se destruyen antes."), ("¿Qué hace investigable a una pregunta?", "Que se contesta observando o midiendo algo concreto", "Indica qué se observa o se cuenta.")],
  open_task=task("Lee estos cuatro casos: (1) una roca con la huella de un helecho; (2) un hueso de pollo del almuerzo enterrado hace dos semanas en el jardín; (3) una concha de caracol vacía hallada en la playa hoy; (4) una piedra con el hueco en forma de concha que dejó un molde. Rotula cada caso como fósil o no fósil y explica con una frase. Después escribe una pregunta investigable sobre el caso 1 que indique qué se observa o se cuenta.", "1 fósil (huella en roca); 2 no (reciente, sin roca); 3 no (de hoy); 4 fósil (molde en roca). Pregunta: «¿Cuántas hojas del helecho se distinguen en la huella?»", ["rotula los cuatro casos", "explica con roca y antigüedad", "la pregunta indica qué se observa o se cuenta"], ["cuatro rótulos con motivo y una pregunta"], ["llamar fósil al hueso reciente", "escribir una pregunta de opinión"], "Pregunta qué dato necesitarías para contestar tu pregunta."),
  reinforce="Escribe con tus palabras tres condiciones que ayudan a que un organismo se fosilice.",
  extend="Explica por qué los fósiles encontrados no representan a todos los seres vivos que existieron.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. La tabla de muestras de roca está escrita en los ejercicios; no necesitas salir de tu casa.",
  use="Aprenderé cómo se forman las rocas sedimentarias y por qué casi todos los fósiles aparecen en ellas. Sirve para leer una tabla de muestras y concluir con evidencia.",
  prior=["Sé qué es un fósil y que necesita entierro rápido.", "Sé que una conclusión debe apoyarse en datos."],
  explain=[
      "Las rocas sedimentarias se forman cuando los sedimentos (arena, barro, restos de conchas) se acumulan en capas en un lago, un río o el mar. Con el tiempo, el peso de las capas superiores los compacta y los minerales los pegan entre sí. Ejemplos: la arenisca, hecha de granos de arena, y la caliza, formada en gran parte por restos de conchas.",
      "Las rocas ígneas se forman cuando el magma, roca fundida muy caliente, se enfría y se endurece, como el granito y el basalto. Las rocas metamórficas se forman cuando el calor y la presión transforman una roca anterior, como el mármol. Estos procesos destruyen o deforman cualquier resto de ser vivo.",
      "Por eso los fósiles aparecen casi siempre en rocas sedimentarias: se depositan en capas a temperaturas bajas y los restos quedan atrapados sin quemarse ni deformarse. Si una tabla de muestras muestra fósiles en rocas sedimentarias y ninguno en rocas ígneas, es evidencia que apoya esta idea, pero no la prueba con una sola muestra.",
  ],
  vocab=[("roca sedimentaria", "roca formada por sedimentos compactados y pegados"), ("roca ígnea", "roca formada por el enfriamiento de magma"), ("roca metamórfica", "roca transformada por calor y presión"), ("magma", "roca fundida muy caliente bajo la superficie"), ("compactación", "apretamiento de las capas por el peso de las superiores")],
  worked=[
      ("Clasificar una roca", "Una roca tiene granos de arena pegados entre sí y contiene una concha. ¿De qué tipo es?", ["Los granos de arena pegados indican sedimentos compactados.", "Una roca con granos de arena pegados y una concha se formó por depósito en capas."], "Sedimentaria"),
      ("Leer una tabla", "Tabla de ejemplo: granito, ígnea, 0 fósiles; caliza, sedimentaria, 5 fósiles; basalto, ígnea, 0 fósiles; arenisca, sedimentaria, 3 fósiles. ¿Qué rocas tienen fósiles?", ["Busco las filas con valor mayor que 0 en fósiles.", "Son la caliza y la arenisca; ambas son sedimentarias."], "La caliza y la arenisca, ambas sedimentarias"),
  ],
  mistakes=[
      ("Pensar que un fósil puede conservarse dentro de granito.", "El granito se forma por enfriamiento de magma, que es tan caliente que destruiría cualquier resto.", "Asocia los fósiles con rocas formadas a baja temperatura, en capas."),
      ("Afirmar «todas las rocas sedimentarias tienen fósiles».", "Muchas rocas sedimentarias no tienen ninguno: solo es más probable encontrarlos en ellas.", "Escribe «casi siempre aparecen en sedimentarias», no «siempre»."),
  ],
  rec=[
      ("¿En qué tipo de roca se encuentran casi siempre los fósiles?", "En rocas sedimentarias", "Los restos quedan atrapados entre sedimentos."),
      ("Completa: el magma al enfriarse forma rocas ______ (ígneas o sedimentarias).", "Ígneas", "Las rocas ígneas nacen del magma enfriado."),
      ("Verdadero o falso: la arenisca está hecha de granos de arena pegados.", "Verdadero", "Es un ejemplo de roca sedimentaria."),
  ],
  und=[
      ("¿Por qué no se espera hallar fósiles en el basalto? A) Porque se forma a partir de magma muy caliente que destruiría los restos; B) Porque el basalto es demasiado liviano para contener restos.", "A", "El calor del magma elimina cualquier resto de ser vivo."),
      ("¿Qué ocurre con los sedimentos para formar una roca sedimentaria? A) Se acumulan en capas, se compactan y se pegan entre sí; B) Se funden y luego se enfrían.", "A", "La fusión corresponde a las rocas ígneas."),
      ("El mármol se forma cuando el calor y la presión transforman otra roca. ¿A qué grupo pertenece?", "Metamórficas", "Una roca transformada por calor y presión es metamórfica."),
  ],
  app=[
      ("Tabla de ejemplo: roca P, ígnea, 0 fósiles; roca Q, sedimentaria, 7 fósiles; roca R, sedimentaria, 0 fósiles; roca S, metamórfica, 0 fósiles. ¿Cuál es la única roca de la tabla que tiene fósiles?", "La roca Q", "Es la única fila con un número de fósiles mayor que cero."),
      arith("En una cantera de ejemplo se revisaron 6 muestras de caliza con 5 fósiles cada una y 4 muestras de arenisca con 3 fósiles cada una. ¿Cuántos fósiles hay en total?", "6*5+4*3", "Se multiplica cada grupo por sus fósiles y se suman los resultados."),
      ("Una persona recoge una roca con capas finas de barro endurecido y una hoja marcada. ¿Qué tipo de roca es más probable que sea? A) Sedimentaria; B) Ígnea.", "A", "Las capas de barro endurecido son sedimentos compactados."),
  ],
  rea=[
      ("Un equipo revisó 20 rocas ígneas y no halló ningún fósil. Concluye: «Es imposible que exista algún fósil en una roca ígnea». ¿Qué falla tiene esa conclusión? A) Generaliza más de lo que permite la muestra; B) Debió revisar solo rocas metamórficas.", "A", "Una muestra puede apoyar la idea, pero no probar que sea imposible."),
      ("Una persona dice: «El mármol viene de la caliza, que tiene fósiles, así que el mármol debe conservarlos intactos». ¿Qué proceso lo contradice? A) La presión y el calor deforman o borran los restos; B) El mármol se forma por entierro rápido.", "A", "El metamorfismo transforma la roca y suele borrar los fósiles."),
  ],
  cha=[
      ("Datos de ejemplo: de 40 rocas sedimentarias revisadas, 25 tenían fósiles. De 30 rocas ígneas, ninguna. ¿Cuántas rocas sedimentarias revisadas no tenían fósiles?", "15", "Son 40 menos 25 rocas con fósiles."),
      ("Un cerro tiene una capa de roca ígnea entre dos capas sedimentarias con fósiles. ¿Qué esperas encontrar en la capa ígnea? A) Ningún fósil, porque se formó por enfriamiento de magma; B) Muchos fósiles, porque está entre capas con fósiles.", "A", "El tipo de roca determina si hay fósiles, no su vecindad."),
  ],
  context=[arith("En una excursión escolar de ejemplo se examinan 5 muestras de arenisca, 3 de caliza y 2 de granito. ¿Cuántas muestras son de rocas sedimentarias?", "5+3", "Arenisca y caliza son sedimentarias; el granito es ígneo.")],
  selfcheck=[("¿Cómo se forma una roca sedimentaria?", "Con sedimentos acumulados en capas, compactados y pegados", "Eso las diferencia de las ígneas y metamórficas."), ("¿Por qué no hay fósiles en el granito?", "Porque se forma de magma muy caliente", "El calor destruye cualquier resto."), ("¿Qué tipo de roca sufre calor y presión?", "La metamórfica", "El calor y la presión transforman una roca anterior.")],
  open_task=task("Con esta tabla de ejemplo, redacta una conclusión de dos oraciones. Tabla: granito, ígnea, 0 fósiles; basalto, ígnea, 0 fósiles; mármol, metamórfica, 0 fósiles; caliza, sedimentaria, 6 fósiles; arenisca, sedimentaria, 2 fósiles; lutita (barro endurecido), sedimentaria, 4 fósiles. La primera oración debe citar al menos dos datos; la segunda debe declarar un límite de la evidencia.", "Los fósiles aparecen en la caliza (6), la lutita (4) y la arenisca (2), todas sedimentarias, y no en granito, basalto ni mármol. Con solo seis muestras no se puede asegurar que ninguna roca ígnea o metamórfica tenga fósiles.", ["cita al menos dos datos", "relaciona fósiles con roca sedimentaria", "declara un límite de la tabla"], ["conclusión de dos oraciones"], ["afirmar que todas las sedimentarias tienen fósiles", "no declarar ningún límite"], "Pregunta qué muestra adicional cambiaría la conclusión."),
  reinforce="Dibuja o describe cómo se forma una roca sedimentaria en cuatro pasos.",
  extend="Explica por qué la presencia de fósiles en una roca ayuda a saber en qué ambiente se formó.")

L(OA1, 3,
  materials="Hojas de papel de distintos colores o de cuaderno (cinco hojas bastan) y lápiz. Si no tienes, dibuja los estratos con lápiz.",
  use="Aprenderé a usar un modelo de capas para ubicar los fósiles según su antigüedad en los estratos de la Tierra. Sirve para saber qué fósil es más antiguo que otro sin conocer sus años.",
  prior=["Sé que los fósiles están en rocas sedimentarias.", "Sé que las rocas sedimentarias se forman por capas."],
  explain=[
      "Un estrato es una capa de roca sedimentaria. Cuando los sedimentos se depositan, la primera capa queda abajo y las nuevas se apilan encima. Esa es la idea del principio de superposición: en una secuencia que no ha sido alterada, el estrato de abajo es más antiguo y el de arriba es más joven.",
      "Un modelo sirve para entender esto: si apilas hojas de papel una sobre otra, la primera que pusiste queda abajo, igual que el primer sedimento. Los fósiles que están dentro de cada estrato son de organismos que vivieron cuando ese estrato se depositaba. Por eso un fósil en un estrato inferior es más antiguo que otro de un estrato superior. Esa es su antigüedad relativa: se dice «más antiguo que», sin dar años.",
      "Un fósil guía es el fósil de una especie que vivió durante poco tiempo y en una zona amplia. Si aparece en estratos de dos lugares distintos, esos estratos tienen aproximadamente la misma edad. Un modelo simplifica: las capas reales no siempre son parejas y pueden estar inclinadas, pero ayuda a razonar.",
  ],
  vocab=[("estrato", "capa de roca sedimentaria"), ("principio de superposición", "en capas sin alterar, la de abajo es más antigua"), ("antigüedad relativa", "comparación de edades sin usar años"), ("fósil guía", "fósil de una especie de vida corta y amplia distribución"), ("secuencia", "serie de capas ordenadas una sobre otra")],
  worked=[
      ("Ordenar estratos", "Un corte de ejemplo muestra de arriba hacia abajo: estrato 1 con fósil de helecho, estrato 2 con fósil de pez, estrato 3 con fósil de alga. ¿Qué fósil es el más antiguo?", ["Aplico la superposición: lo de más abajo es más antiguo.", "El estrato de más abajo es el 3."], "El fósil de alga"),
      ("Comparar dos lugares", "En el lugar X, el fósil guía M está en el estrato 2. En el lugar Y, el fósil M está en el estrato 5. ¿Qué se puede decir de esos dos estratos?", ["El mismo fósil guía indica la misma época.", "Los estratos 2 de X y 5 de Y tienen aproximadamente la misma edad."], "Tienen aproximadamente la misma edad"),
  ],
  mistakes=[
      ("Creer que el estrato de arriba es siempre el más antiguo.", "Los sedimentos se acumulan desde abajo hacia arriba, por lo que lo nuevo queda encima.", "Dibuja la pila de hojas y recuerda qué hoja pusiste primero."),
      ("Dar una edad en años a partir de la posición de un estrato.", "La posición solo permite decir más antiguo o más joven, no cuántos años.", "Usa la frase «más antiguo que» para la antigüedad relativa."),
  ],
  rec=[
      ("¿Qué es un estrato?", "Una capa de roca sedimentaria", "Los sedimentos se depositan formando capas."),
      ("En una secuencia sin alterar, el estrato de abajo es ______ (más antiguo o más joven) que el de arriba.", "Más antiguo", "Se depositó primero."),
      ("Verdadero o falso: la antigüedad relativa indica los años exactos de un fósil.", "Falso", "Solo compara cuál es más antiguo."),
  ],
  und=[
      ("Apilas tres hojas: roja primero, azul después y verde al final. ¿Cuál representa el estrato más joven? A) La verde; B) La roja.", "A", "La última capa depositada queda arriba y es la más joven."),
      ("¿Para qué sirve un fósil guía? A) Para decir que estratos de lugares distintos tienen aproximadamente la misma edad; B) Para medir la profundidad de un pozo.", "A", "Una especie de vida corta y amplia distribución marca una época."),
      ("Un fósil está en el estrato 4 y otro en el estrato 2, contando desde arriba hacia abajo. ¿Cuál es más antiguo?", "El del estrato 4", "El estrato 4 está más abajo."),
  ],
  app=[
      ("Corte de ejemplo, de arriba hacia abajo: estrato A con fósil de erizo, estrato B con fósil de concha, estrato C con fósil de coral, estrato D sin fósiles. ¿Cuál es el fósil más antiguo de la secuencia?", "El coral", "Está en el estrato más bajo que contiene fósiles."),
      arith("Una pared de ejemplo tiene 6 estratos de 25 cm cada uno. ¿Cuántos centímetros de alto tiene la secuencia?", "6*25", "Se multiplica el número de estratos por el espesor de cada uno."),
      ("Un fósil guía aparece en el estrato 3 de un cerro y en el estrato 1 de otro cerro. Un compañero concluye que ambos estratos se depositaron en la misma época. ¿Es razonable? A) Sí, porque tienen el mismo fósil guía; B) No, porque tienen números distintos.", "A", "El número del estrato depende de cada lugar; el fósil guía indica la edad."),
  ],
  rea=[
      ("Un equipo coloca cuatro hojas de colores y numera de abajo hacia arriba: azul 1, verde 2, amarilla 3, roja 4. Pone un fósil dibujado en la amarilla y otro en la azul. ¿Cuál fósil es más antiguo y por qué? A) El de la azul, porque está más abajo; B) El de la amarilla, porque tiene un número mayor.", "A", "Lo que está más abajo se depositó antes."),
      ("Un fósil de pez aparece en un estrato más profundo que un fósil de mamífero en el mismo corte. ¿Qué dice eso de ellos? A) El pez es más antiguo que el mamífero en ese corte; B) El pez era más grande que el mamífero.", "A", "La posición en la secuencia da antigüedad relativa, no tamaño."),
  ],
  cha=[
      ("Dos cortes de ejemplo. Corte 1, de arriba hacia abajo: fósil W, fósil M, fósil K. Corte 2, de arriba hacia abajo: fósil M, fósil K, fósil T. Ordena los cuatro fósiles del más antiguo al más joven, escribiendo las letras separadas por comas.", "T, K, M, W", "En el corte 2 T es el más antiguo; K y M mantienen el orden de ambos cortes; W es el más joven del corte 1."),
      ("Un modelo de cinco hojas apiladas se pega con cinta y se dobla como un pliegue. Un compañero dice que ahora no se puede aplicar la superposición. ¿Qué respuesta es mejor? A) La superposición solo vale si las capas no han sido alteradas, así que hay que revisar el pliegue; B) La superposición vale siempre, aunque se doble.", "A", "El pliegue puede invertir o mover capas; el principio exige una secuencia sin alterar."),
  ],
  context=[arith("Una persona hace un modelo de capas con 7 hojas de papel. Coloca un fósil dibujado en cada hoja par. ¿Cuántos fósiles dibuja?", "7//2", "Entre 7 hojas hay 3 pares: la 2, la 4 y la 6.")],
  selfcheck=[("¿Cuál estrato es más antiguo en una secuencia sin alterar?", "El de abajo", "Se depositó primero."), ("¿Qué es un fósil guía?", "Un fósil de una especie de vida corta y amplia distribución", "Sirve para comparar edades entre lugares."), ("¿Qué significa antigüedad relativa?", "Decir cuál es más antiguo sin dar años", "Compara posiciones, no mide años.")],
  open_task=task("Con 5 hojas de papel o 5 rectángulos dibujados, haz este modelo: de abajo hacia arriba, estrato 1 (fósil de alga), estrato 2 (fósil de pez), estrato 3 (fósil de helecho), estrato 4 (sin fósiles), estrato 5 (fósil de ave). Después escribe tres comparaciones con «más antiguo que» y una limitación de tu modelo.", "El alga es más antigua que el pez; el pez es más antiguo que el helecho; el helecho es más antiguo que el ave. Limitación: el modelo es plano y parejo, pero las capas reales pueden estar inclinadas o dobladas.", ["tres comparaciones correctas", "usa «más antiguo que»", "limitación coherente con el modelo"], ["modelo dibujado o armado y tres frases"], ["invertir el orden de las capas", "dar años sin datos"], "Pregunta qué evidencia te diría que una capa fue movida."),
  reinforce="Apila tres hojas y explica a otra persona cuál es la más antigua.",
  extend="Explica por qué un fósil guía de vida corta es mejor para comparar edades que uno de vida muy larga.")

L(OA1, 4,
  materials="Este cuaderno y lápiz. Las tablas con profundidades y fósiles están escritas en los ejercicios.",
  use="Aprenderé a relacionar la profundidad de un estrato con su antigüedad y a reconocer cuándo una secuencia no está intacta. Sirve para leer datos de un corte y decidir con cuidado.",
  prior=["Sé ordenar estratos por antigüedad relativa.", "Sé qué es un fósil guía."],
  explain=[
      "En un corte de roca puedes ver dos variables: la profundidad del estrato (variable que se mide) y su antigüedad relativa (lo que se quiere averiguar). Si la secuencia no está alterada, a mayor profundidad, mayor antigüedad. Esa relación se puede escribir en una tabla y comprobar con datos.",
      "Los sedimentos se acumulan a una tasa que cambia según el lugar. Si en un lago de ejemplo se depositan 2 mm cada año, una capa de 30 mm representa 15 años de depósito. Pero esa tasa no es constante en la naturaleza, por eso estos cálculos son estimaciones con incertidumbre.",
      "Los estratos no siempre conservan una secuencia intacta. Una falla es una fractura donde un bloque de roca se desplaza respecto de otro. Un pliegue curva las capas y a veces las invierte. Una erosión puede quitar capas completas. Antes de ordenar los fósiles, un buen investigador busca señales de estas alteraciones.",
  ],
  vocab=[("variable", "dato que puede cambiar y se mide u observa"), ("tasa de sedimentación", "espesor de sedimento que se acumula en un tiempo"), ("falla", "fractura donde un bloque de roca se desplaza"), ("pliegue", "curvatura de las capas de roca"), ("erosión", "desgaste que quita material de la superficie")],
  worked=[
      ("Calcular años de depósito", "En un lago de ejemplo se depositan 4 mm de sedimento cada año. ¿Cuántos años representa una capa de 40 mm?", ["Divido el espesor entre lo que se acumula por año.", "40 dividido por 4 es 10."], "10 años"),
      ("Detectar una alteración", "En un corte, un fósil de pez aparece en un estrato superior al de un fósil de alga, pero una falla corta ambos estratos y los desplaza. ¿Se puede asegurar que el pez es más joven?", ["Reviso si hay alteraciones: hay una falla.", "Los bloques pueden estar movidos, así que la posición ya no es confiable."], "No, hay que verificar primero el efecto de la falla"),
  ],
  mistakes=[
      ("Usar la tasa de sedimentación de un lugar para fechar otro lugar.", "Cada sitio acumula sedimento a un ritmo distinto.", "Declara que el resultado es una estimación válida solo para ese sitio."),
      ("Ordenar fósiles sin revisar fallas, pliegues o erosión.", "Estas alteraciones pueden cambiar el orden original de las capas.", "Busca primero señales de alteración en el corte."),
  ],
  rec=[
      ("En una secuencia sin alterar, ¿a mayor profundidad la antigüedad es mayor o menor?", "Mayor", "Lo más profundo se depositó primero."),
      ("¿Cómo se llama la fractura donde un bloque de roca se desplaza respecto de otro?", "Falla", "Una falla puede alterar el orden de las capas."),
      ("Verdadero o falso: una erosión puede quitar capas completas de una secuencia.", "Verdadero", "Eso deja una secuencia incompleta."),
  ],
  und=[
      ("¿Por qué el cálculo de años a partir del espesor es solo una estimación? A) Porque la tasa de sedimentación cambia según el lugar y la época; B) Porque el espesor de una capa no se puede medir con una regla.", "A", "Una tasa distinta cambiaría el resultado."),
      ("Un pliegue invierte las capas de un corte. ¿Qué pasa con la regla «lo de abajo es más antiguo»? A) Deja de cumplirse en la parte invertida; B) Se cumple siempre sin excepción.", "A", "Al invertirse las capas, lo de abajo puede ser más joven."),
      ("Tabla de ejemplo: estrato a 2 m, fósil F; estrato a 5 m, fósil G; estrato a 9 m, fósil H. ¿Qué fósil es el más antiguo si no hay alteraciones?", "H", "Es el estrato más profundo, a 9 m."),
  ],
  app=[
      arith("En una laguna de ejemplo se acumulan 3 mm de sedimento por año. ¿Cuántos años representa una capa de 54 mm?", "54//3", "Se divide el espesor entre lo que se acumula por año.", " años"),
      arith("En otro sitio de ejemplo hay 4 estratos que se depositaron en 12, 8, 15 y 5 años. ¿Cuántos años representa toda la secuencia?", "12+8+15+5", "Se suman los años de cada estrato."),
      ("Tabla de ejemplo: profundidad 1 m, 2 fósiles; 3 m, 5 fósiles; 6 m, 9 fósiles; 8 m, 12 fósiles. Al aumentar la profundidad, ¿qué ocurre con el número de fósiles?", "Aumenta", "Cada profundidad mayor trae más fósiles en esta tabla."),
  ],
  rea=[
      ("Un equipo dice: «Como el estrato de 12 m tiene el fósil Q y el de 4 m tiene el fósil R, Q es más antiguo». Pero el corte tiene una falla que cruza justo entre ambos. ¿Qué es lo más prudente? A) Revisar cómo la falla movió los bloques antes de concluir; B) Concluir igual, porque la profundidad es lo único que importa.", "A", "Una falla puede haber movido uno de los bloques."),
      ("En un sitio de ejemplo falta un estrato entre dos capas, porque una erosión lo removió. ¿Cómo afecta eso a la historia que cuenta la secuencia? A) Queda un tiempo sin registro en las rocas; B) Los fósiles de arriba son más antiguos.", "A", "Lo erosionado ya no está para mostrar lo ocurrido entonces."),
  ],
  cha=[
      ("Datos de ejemplo: una capa de 60 mm se formó en un lago a 2 mm por año; otra capa de 60 mm se formó en un río a 6 mm por año. ¿Cuántos años más representa la capa del lago que la del río?", "20", "El lago representa 30 años y el río 10 años; la diferencia es 20."),
      ("Una pared de ejemplo tiene tres fósiles guía: M en el estrato superior, N en el medio y P en el inferior. En otra pared aparecen N y P, pero ordenados al revés. ¿Qué explicación es más probable? A) Una de las paredes tiene capas plegadas o invertidas; B) Los fósiles se cambiaron de lugar solos.", "A", "Un pliegue invertido cambia el orden de las capas."),
  ],
  context=[arith("En la visita a un corte de camino, una guía mide 4 estratos con espesores de 30, 45, 20 y 35 centímetros. ¿Cuántos centímetros mide el corte completo?", "30+45+20+35", "Se suman los espesores de los cuatro estratos.")],
  selfcheck=[("¿Qué relación hay entre profundidad y antigüedad en una secuencia sin alterar?", "A mayor profundidad, mayor antigüedad", "Lo de abajo se depositó primero."), ("Nombra dos alteraciones que cambian el orden de las capas.", "Falla y pliegue", "Mueven o invierten los estratos."), ("¿Por qué una edad calculada con la tasa de sedimentación es una estimación?", "Porque la tasa cambia según el lugar y la época", "Hay incertidumbre en el cálculo.")],
  open_task=task("Usa este corte de ejemplo, de arriba hacia abajo: estrato 1 (0 a 1 m, fósil de ave), estrato 2 (1 a 3 m, fósil de mamífero), estrato 3 (3 a 6 m, fósil de reptil), estrato 4 (6 a 10 m, fósil de pez). Una falla corta los estratos 2 y 3. Escribe el orden del más antiguo al más joven, qué dato tienes en duda por la falla y una pregunta investigable para resolver la duda.", "Pez, reptil, mamífero, ave. La posición relativa de reptil y mamífero queda en duda por la falla. Pregunta: «¿Los bloques de los estratos 2 y 3 se desplazaron hacia arriba o hacia abajo y cuántos metros?».", ["orden coherente con la profundidad", "señala la duda por la falla", "la pregunta indica qué se observa o se mide"], ["orden, duda y pregunta escritos"], ["ignorar la falla", "formular una pregunta de opinión"], "Pregunta qué observación en la roca mostraría el desplazamiento de la falla."),
  reinforce="Escribe una regla en una frase para ordenar fósiles según la profundidad de sus estratos.",
  extend="Explica por qué dos cortes con fósiles distintos pueden representar el mismo período de tiempo.")

# ---------------------------------------------------------------- OA 02

L(OA2, 1,
  materials="Este cuaderno y lápiz. Todos los casos y descripciones de evidencias están escritos en el cuaderno.",
  use="Aprenderé qué es la evolución y cuáles son sus cuatro evidencias: el registro fósil, las estructuras homólogas, la embriología y el ADN. Sirve para formular preguntas que se pueden contestar con datos.",
  prior=["Sé qué es un fósil y cómo se ordenan los estratos.", "Sé distinguir una pregunta investigable de una opinión."],
  explain=[
      "La evolución es el cambio de las características hereditarias de las poblaciones de seres vivos a lo largo de muchas generaciones. Explica por qué existen tantos organismos distintos y por qué algunos se parecen. No es el cambio de un individuo durante su vida.",
      "Hay cuatro grandes tipos de evidencia. El registro fósil muestra organismos del pasado, ordenados por estratos. Las estructuras homólogas son partes del cuerpo de especies distintas con el mismo origen, como el hueso del brazo humano y el de la aleta de una ballena. La embriología compara las etapas tempranas del desarrollo: embriones de peces y de humanos muestran estructuras parecidas. Las secuencias de ADN permiten comparar el material hereditario: mientras más parecido, más cercano es el parentesco.",
      "Una pregunta investigable sobre evolución dice qué dato se compara. Por ejemplo: «¿Cuántos huesos del brazo humano tienen un equivalente en la aleta de una ballena?» se contesta con observaciones. «¿Es justo que la evolución haya ocurrido?» no se puede contestar con datos.",
  ],
  vocab=[("evolución", "cambio hereditario de una población a lo largo de las generaciones"), ("registro fósil", "conjunto de fósiles ordenados por antigüedad"), ("estructura homóloga", "parte del cuerpo con el mismo origen evolutivo en especies distintas"), ("embriología", "estudio de las etapas tempranas del desarrollo"), ("secuencia de ADN", "orden de las letras químicas del material hereditario")],
  worked=[
      ("¿Qué evidencia es?", "Se comparan los huesos de un ala de murciélago con los huesos del brazo humano y se ven los mismos huesos con distinta forma. ¿Qué tipo de evidencia es?", ["Comparo partes del cuerpo de especies distintas.", "Hay el mismo plan de huesos con distinta forma."], "Estructuras homólogas (anatomía comparada)"),
      ("Pregunta investigable", "Convierte «¿Son lindos los fósiles de ballenas antiguas?» en una pregunta investigable.", ["Quito la palabra de opinión: «lindos».", "Indico qué se observa: huesos de las patas posteriores en fósiles de ballenas antiguas.", "Queda: «¿Cuántos huesos de las patas posteriores se conservan en un fósil de ballena antigua?»"], "«¿Cuántos huesos de las patas posteriores se conservan en un fósil de ballena antigua?»"),
  ],
  mistakes=[
      ("Pensar que la evolución es un cambio que un individuo hace para adaptarse.", "La evolución ocurre en poblaciones durante muchas generaciones, no en un solo individuo.", "Habla de «poblaciones» y «generaciones»."),
      ("Creer que la evolución es solo una opinión.", "Se apoya en varias evidencias independientes que se pueden comprobar.", "Nombra qué evidencia sostiene cada afirmación."),
  ],
  rec=[
      ("¿Qué es la evolución?", "El cambio hereditario de las poblaciones a lo largo de las generaciones", "Ocurre en poblaciones, no en individuos."),
      ("Completa: el estudio de las etapas tempranas del desarrollo se llama ______ (embriología o estratigrafía).", "Embriología", "Compara embriones de especies distintas."),
      ("Verdadero o falso: las secuencias de ADN sirven para comparar el parentesco entre especies.", "Verdadero", "Mientras más parecidas, más cercano el parentesco."),
  ],
  und=[
      ("Los embriones de pez y de humano muestran estructuras parecidas en el cuello al inicio del desarrollo. ¿Qué evidencia es? A) Embriología; B) Registro fósil.", "A", "Compara etapas tempranas del desarrollo."),
      ("Un fósil de ballena antigua conserva huesos pequeños de patas posteriores. ¿Qué sugiere eso? A) Que las ballenas descienden de animales con patas; B) Que las ballenas actuales nadan con patas.", "A", "Esos huesos son evidencia de un ancestro con extremidades."),
      ("¿Qué par de estructuras es homólogo? A) El brazo humano y la aleta de una ballena; B) El ala de un insecto y el ala de un ave.", "A", "Ambas tienen el mismo plan de huesos del brazo; las alas de insecto y de ave sirven para volar, pero no tienen ese origen."),
  ],
  app=[
      ("Un fósil de pez, un esqueleto humano y una molécula de ADN son tres tipos de datos. ¿Cuál de esas tres evidencias se organiza por estratos? A) El fósil de pez; B) La molécula de ADN.", "A", "El registro fósil se ordena según los estratos donde se halla."),
      ("¿Cuál es una pregunta investigable sobre evolución? A) ¿Cuántas diferencias hay entre dos secuencias cortas de ADN de especies distintas?; B) ¿Es bueno que cambien las especies?", "A", "Se contesta comparando dos secuencias."),
      arith("Un esqueleto de ejemplo tiene 1 hueso en la parte alta del brazo, 2 en el antebrazo, 8 en la muñeca y 19 en la mano. ¿Cuántos huesos tiene en total?", "1+2+8+19", "Se suman los huesos de cada parte del miembro."),
  ],
  rea=[
      ("Una persona dice: «Si la evolución fuera cierta, yo vería cambiar a mi perro durante su vida». ¿Qué falla tiene? A) Confunde el cambio de un individuo con el cambio de una población en muchas generaciones; B) La evolución solo ocurre en animales pequeños.", "A", "La evolución se mide en poblaciones a lo largo de generaciones."),
      ("Un compañero propone la evidencia «los humanos y las ballenas tienen sangre caliente». ¿Qué falta para usarla? A) Mostrar que ese rasgo tiene el mismo origen y no apareció por separado; B) Nada, porque cualquier rasgo parecido sirve.", "A", "Un rasgo parecido solo prueba parentesco si tiene origen común."),
  ],
  cha=[
      ("Tres equipos reúnen evidencias: E1, huesos de ala de murciélago y brazo humano; E2, fósiles de ballenas con patas pequeñas; E3, secuencias cortas de ADN de dos especies. ¿Cuántos tipos distintos de evidencia reúnen en total?", "3", "Son anatomía comparada, registro fósil y ADN, tres tipos distintos."),
      ("¿Qué datos necesitarías para contestar «¿Qué tan parecidas son las secuencias de ADN de dos especies?»? A) Las dos secuencias escritas para compararlas letra por letra; B) El tamaño de las dos especies.", "A", "La comparación exige tener las dos secuencias."),
  ],
  context=[arith("Una exposición de ejemplo presenta 4 fósiles de ballenas antiguas, 3 esqueletos de aletas y 5 láminas de embriones. ¿Cuántas piezas tiene la exposición?", "4+3+5", "Se suman las tres cantidades de piezas.")],
  selfcheck=[("¿Cuáles son las cuatro evidencias de la evolución que se estudian?", "Registro fósil, estructuras homólogas, embriología y secuencias de ADN", "Son las cuatro que nombra el objetivo."), ("¿Dónde ocurre la evolución: en un individuo o en una población?", "En una población", "El cambio es hereditario y toma muchas generaciones."), ("¿Qué hace investigable a una pregunta sobre evolución?", "Que indica qué dato se compara", "Se contesta con observaciones o mediciones.")],
  open_task=task("Lee estas cuatro preguntas: (1) «¿Cuántos huesos tiene en común el brazo humano con la aleta de una ballena?» (2) «¿Es más agradable pensar que las especies cambian que pensar que no cambian?» (3) «¿Qué estructuras similares se ven en embriones de pez y humano en las primeras semanas?» (4) «¿Debemos alegrarnos de que existan los fósiles?». Rotula cada una como investigable o no y reescribe una no investigable para que sí lo sea, indicando qué dato compararías.", "1 investigable; 2 no (opinión); 3 investigable; 4 no (opinión). Reescritura de la 4: «¿Cuántas especies distintas aparecen en los fósiles de un estrato de un cerro?»", ["rotula las cuatro", "justifica con «se observa o se mide» o «es opinión»", "la reescritura indica un dato que se compara o cuenta"], ["cuatro rótulos y una pregunta reescrita"], ["llamar investigable a una pregunta de opinión", "reescribir sin decir qué se observa"], "Pregunta qué de la evidencia tendrías que mirar para contestar tu pregunta nueva."),
  reinforce="Escribe una pregunta investigable que compare los huesos de dos animales.",
  extend="Explica por qué una sola evidencia es menos convincente que cuatro evidencias que coinciden.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Las tablas de huesos y fósiles están escritas en los ejercicios; no necesitas ver esqueletos reales.",
  use="Aprenderé a interpretar el registro fósil y las estructuras homólogas, y a distinguirlas de las análogas. Sirve para decidir si un parecido entre especies se debe a parentesco.",
  prior=["Sé nombrar las cuatro evidencias de la evolución.", "Sé leer una tabla y un corte de estratos."],
  explain=[
      "Las estructuras homólogas tienen el mismo origen evolutivo aunque hoy sirvan para cosas distintas. El brazo humano, la pata del gato, la aleta de la ballena y el ala del murciélago tienen los mismos grupos de huesos: húmero, radio, cúbito, huesos de la muñeca y dedos. Esto es evidencia de un ancestro común, que es una especie antigua de la que descienden varias especies.",
      "Las estructuras análogas cumplen la misma función, pero con distinto origen. El ala de un insecto y el ala de un ave sirven para volar, pero no comparten el plan de huesos. Una estructura vestigial es una parte reducida que parece haber perdido su función; por ejemplo, los huesos pequeños de la pelvis de las ballenas actuales, que recuerdan a un ancestro con patas.",
      "El registro fósil también aporta evidencia. Los fósiles intermedios muestran rasgos de dos grupos. El Archaeopteryx tenía plumas como las aves, pero también dientes y una cola larga con huesos como algunos reptiles. Por eso se usa para mostrar la relación entre aves y reptiles.",
  ],
  vocab=[("estructura homóloga", "parte del cuerpo con el mismo origen aunque su función sea distinta"), ("estructura análoga", "parte con la misma función pero distinto origen"), ("ancestro común", "especie antigua de la que descienden varias especies"), ("estructura vestigial", "parte reducida que parece haber perdido su función"), ("fósil intermedio", "fósil con rasgos de dos grupos distintos")],
  worked=[
      ("Homóloga o análoga", "El ala de un murciélago y la aleta de una ballena tienen húmero, radio, cúbito y dedos. ¿Son homólogas o análogas?", ["Reviso si comparten el plan de huesos: sí.", "Cumplen funciones distintas, volar y nadar, pero con el mismo origen."], "Homólogas"),
      ("Leer un fósil intermedio", "Un fósil tiene plumas, dientes y una cola larga con huesos. ¿Qué dos grupos de rasgos combina?", ["Las plumas son rasgos de aves.", "Los dientes y la cola ósea larga son rasgos de reptiles."], "Rasgos de aves y de reptiles"),
  ],
  mistakes=[
      ("Llamar homólogas a estructuras solo porque se parecen en su función.", "Una misma función no prueba el mismo origen.", "Compara el plan de huesos y el origen, no solo lo que hacen."),
      ("Pensar que una estructura vestigial es inútil por completo.", "Es una parte reducida que perdió su función original, aunque pueda tener otra menor.", "Describe el vestigio como «reducido y sin su función original»."),
  ],
  rec=[
      ("¿Cómo se llaman las partes del cuerpo con el mismo origen aunque cumplan funciones distintas?", "Estructuras homólogas", "Tienen el mismo plan y un ancestro común."),
      ("Completa: el ala de un insecto y el ala de un ave son estructuras ______ (homólogas o análogas).", "Análogas", "Tienen la misma función con distinto origen."),
      ("Verdadero o falso: un fósil intermedio tiene rasgos de dos grupos.", "Verdadero", "Eso lo hace evidencia de relación entre grupos."),
  ],
  und=[
      ("¿Qué indican las estructuras homólogas? A) Un ancestro común; B) Que las especies viven en el mismo lugar.", "A", "Compartir el plan de huesos señala origen común."),
      ("El Archaeopteryx tenía plumas y también dientes. ¿Qué evidencia aporta? A) Una relación entre aves y reptiles; B) Que las aves nunca tuvieron dientes.", "A", "Mezcla rasgos de ambos grupos."),
      ("Los huesos pequeños de la pelvis de una ballena actual son una estructura ______ (vestigial o análoga).", "Vestigial", "Están reducidos y recuerdan a un ancestro con patas."),
  ],
  app=[
      ("Tabla de ejemplo (1 = presente, 0 = ausente). Humano: húmero 1, radio 1, cúbito 1, dedos 1. Ballena: húmero 1, radio 1, cúbito 1, dedos 1. Ave: húmero 1, radio 1, cúbito 1, dedos 1 (reducidos). ¿Qué huesos comparten las tres especies?", "Húmero, radio, cúbito y dedos", "Las tres filas tienen un 1 en todos los huesos."),
      arith("Una colección de ejemplo tiene 12 fotos de estructuras homólogas y 9 de estructuras análogas. ¿Cuántas fotos más hay de homólogas que de análogas?", "12-9", "Se resta el número de fotos análogas al de homólogas."),
      ("Un estudiante compara el ala de una mariposa con la de un pájaro y dice que son homólogas. ¿Qué dato falta para decidir? A) Si comparten el plan de huesos y el origen; B) El color de las alas.", "A", "La homología se decide por origen común, no por apariencia."),
  ],
  rea=[
      ("Una persona dice que la aleta de un tiburón y la aleta de un delfín son homólogas porque se parecen por fuera. ¿Qué evidencia anatómica lo contradice? A) La aleta del delfín tiene húmero, radio, cúbito y dedos, y la del tiburón no tiene ese plan de huesos; B) Ambos animales viven en el agua.", "A", "El plan óseo distinto indica que la semejanza externa es análoga."),
      ("Si dos especies comparten un hueso reducido que en una tercera está completo, ¿cómo lo explicaría la evolución? A) Descienden de un ancestro común que lo tenía completo; B) Lo perdieron por usar poco ese hueso durante la vida de cada individuo.", "A", "El rasgo se heredó y luego se redujo en algunas líneas."),
  ],
  cha=[
      ("Un museo muestra 8 especies con alas: 6 son vertebrados con alas de plan óseo de brazo (como el murciélago) y 2 son insectos. ¿Cuántas de las 8 tienen alas homólogas al brazo humano?", "6", "Solo en los 6 vertebrados el plan de huesos es el mismo; las de los insectos son análogas."),
      ("En un corte de ejemplo, el fósil X (reptil con plumas pequeñas) está en un estrato más antiguo que el fósil Y (ave con cola corta). ¿Qué puede predecir un investigador sobre fósiles más antiguos que X? A) Rasgos de reptiles sin plumas; B) Aves modernas.", "A", "Si X es intermedio, lo más antiguo debería parecerse más al grupo ancestral."),
  ],
  context=[arith("En una sala del museo hay 3 vitrinas con 5 esqueletos de extremidades cada una y 2 vitrinas con 4 fósiles cada una. ¿Cuántas piezas hay en total?", "3*5+2*4", "Se multiplica cada tipo de vitrina por sus piezas y se suman.")],
  selfcheck=[("¿Qué prueban las estructuras homólogas?", "Un ancestro común", "Comparten el origen aunque cambie la función."), ("¿Qué diferencia hay entre homóloga y análoga?", "La homóloga comparte origen y la análoga solo la función", "El origen decide."), ("¿Por qué el Archaeopteryx es un fósil intermedio?", "Tiene rasgos de aves y de reptiles", "Muestra una relación entre ambos grupos.")],
  open_task=task("Completa la siguiente tabla de ejemplo con homóloga, análoga o vestigial: (a) brazo humano y aleta de ballena (mismo plan de huesos); (b) ala de insecto y ala de ave (vuelo con distinto origen); (c) huesos pequeños de la pelvis de una ballena actual; (d) ala de murciélago y brazo humano. Explica una fila en una frase con la palabra «origen».", "(a) homóloga; (b) análoga; (c) vestigial; (d) homóloga. Explicación de (b): sirven para volar pero no tienen el mismo origen.", ["las cuatro filas correctas", "explica una fila con «origen»", "no confunde función con origen"], ["tabla de cuatro filas y una explicación"], ["llamar homóloga a la fila (b)", "explicar sin nombrar el origen"], "Pregunta qué otro dato sobre los huesos ayudaría a confirmar una fila."),
  reinforce="Dibuja un brazo humano y una aleta de ballena y marca con colores los huesos equivalentes.",
  extend="Explica por qué una estructura vestigial es evidencia de evolución y no de diseño inútil.")

L(OA2, 3,
  materials="Un puñado de papelitos de dos colores (por ejemplo, 20 verdes y 20 rojos) y una hoja de color verde. Si no los tienes, dibuja puntos con dos lápices.",
  use="Aprenderé los postulados de la selección natural y cómo Darwin y Wallace llegaron a ella. Sirve para explicar con un modelo por qué ciertos rasgos se vuelven más comunes en una población.",
  prior=["Sé que la evolución ocurre en poblaciones.", "Sé que algunos rasgos se heredan."],
  explain=[
      "La teoría de la selección natural se apoya en cuatro postulados. Primero, hay variación: los individuos de una población no son idénticos. Segundo, algunas de esas variaciones se heredan. Tercero, nacen más individuos de los que pueden sobrevivir, por lo que compiten por alimento, refugio o pareja. Cuarto, los individuos con rasgos que les dan ventaja sobreviven y dejan más descendientes, por lo que ese rasgo se vuelve más común.",
      "Charles Darwin recogió observaciones durante su viaje en el barco Beagle y publicó «El origen de las especies» en 1859. Alfred Russel Wallace llegó por su cuenta a una idea muy parecida estudiando animales en el sureste de Asia. En 1858 sus trabajos se presentaron juntos en la misma reunión científica. Ambos son reconocidos como creadores de la teoría.",
      "Un modelo simple: papelitos verdes y rojos sobre una hoja verde representan insectos. Un «depredador» que mira rápido ve antes los rojos. Después de varias rondas quedan más verdes que rojos. El modelo muestra la selección sin intención: el ambiente favorece un rasgo, pero los individuos no cambian por querer.",
  ],
  vocab=[("variación", "diferencias entre los individuos de una población"), ("herencia", "transmisión de rasgos a los descendientes"), ("selección natural", "supervivencia y reproducción diferencial según el rasgo"), ("ventaja", "rasgo que aumenta la supervivencia o la reproducción"), ("postulado", "idea básica de una teoría")],
  worked=[
      ("Aplicar los postulados", "En una población de ejemplo hay saltamontes verdes y cafés. Las aves ven más fácil los cafés sobre pasto verde. ¿Qué rasgo tiene ventaja?", ["Reviso qué rasgo hace que sobrevivan más.", "Los verdes se camuflan en el pasto y las aves los comen menos."], "El color verde"),
      ("Contar cambios", "En una ronda del modelo hay 20 papelitos verdes y 20 rojos. El depredador se lleva 12 rojos y 4 verdes. ¿Cuántos de cada color quedan?", ["Resto lo que se llevó de cada color.", "Rojos: 20 menos 12 es 8. Verdes: 20 menos 4 es 16."], "8 rojos y 16 verdes"),
  ],
  mistakes=[
      ("Decir que los individuos cambian porque «necesitan» adaptarse.", "Los individuos no cambian por necesidad; las variaciones ya existen y el ambiente favorece a algunas.", "Describe quién sobrevive y deja más descendientes."),
      ("Creer que sobrevive «el más fuerte» siempre.", "Sobrevive quien tiene el rasgo con más ventaja en ese ambiente, que puede ser camuflaje, tamaño u otro.", "Pregunta siempre: ventaja en qué ambiente."),
  ],
  rec=[
      ("¿Cuántos postulados tiene la selección natural que se explicó?", "Cuatro", "Variación, herencia, más nacimientos que supervivientes y supervivencia diferencial."),
      ("Completa: en una población los individuos no son idénticos; eso se llama ______ (variación o herencia).", "Variación", "Es el primer postulado."),
      ("Verdadero o falso: Wallace llegó por su cuenta a una idea parecida a la de Darwin.", "Verdadero", "Ambos propusieron la selección natural."),
  ],
  und=[
      ("¿Cuál es el tercer postulado? A) Nacen más individuos de los que pueden sobrevivir; B) Los individuos cambian a voluntad.", "A", "Eso genera competencia por recursos."),
      ("¿Quién publicó «El origen de las especies» en 1859? A) Charles Darwin; B) Alfred Russel Wallace.", "A", "Darwin publicó esa obra."),
      ("En el modelo, ¿qué representan los papelitos verdes y rojos sobre la hoja verde? A) Individuos de una misma población con dos rasgos distintos, en un ambiente verde; B) Dos especies de plantas que compiten.", "A", "Muestran variación de un rasgo y su efecto de camuflaje."),
  ],
  app=[
      ("Una población de ejemplo de escarabajos tiene 30 oscuros y 30 claros sobre un tronco claro. Las aves comen 20 oscuros y 5 claros. ¿Qué color tiene ventaja en ese ambiente?", "Claro", "Al camuflarse en el tronco claro sufren menos depredación."),
      arith("En otra ronda del modelo quedan 18 papelitos verdes y 6 rojos. Cada papelito que queda deja 2 descendientes del mismo color. ¿Cuántos papelitos verdes habrá en la siguiente generación?", "18*2", "Se multiplica el número de verdes que quedan por sus descendientes."),
      arith("En esa misma ronda del modelo (18 verdes y 6 rojos), ¿cuántos papelitos rojos habrá en la siguiente generación si cada rojo deja 2 descendientes?", "6*2", "Se multiplica el número de rojos que quedan por sus descendientes."),
  ],
  rea=[
      ("Una persona dice: «Los saltamontes se volvieron verdes porque lo necesitaban». ¿Cuál es una mejor explicación? A) Había saltamontes verdes y cafés; los verdes se camuflaron mejor, sobrevivieron más y dejaron más descendientes; B) Cada saltamontes se pintó de verde para sobrevivir.", "A", "La selección actúa sobre variaciones que ya existen."),
      ("Si una variación no se hereda, por ejemplo una cicatriz, ¿puede aumentar en la población por selección natural? A) No, porque no pasa a los descendientes; B) Sí, porque ayuda a sobrevivir.", "A", "Sin herencia no hay cambio en las generaciones siguientes."),
  ],
  cha=[
      ("Un depredador come primero lo que ve más fácil. Si cambian el fondo de la hoja de verde a roja, ¿qué ocurriría con los papelitos del modelo? A) Los rojos tendrían ventaja porque se camuflan; B) Los verdes seguirían teniendo ventaja.", "A", "La ventaja depende del ambiente, no del color por sí solo."),
      ("Darwin y Wallace llegaron a la misma idea de forma independiente. ¿Qué dice eso de la idea? A) Que dos investigadores con distintas evidencias llegaron a una explicación semejante, lo que la fortalece; B) Que no es posible comprobar la idea.", "A", "Una conclusión que coincide desde evidencias separadas gana respaldo."),
  ],
  context=[arith("En un jardín de ejemplo hay 50 orugas, 28 de color verde y las demás de color café. Los pájaros se comen 4 verdes y 15 café. ¿Cuántas orugas quedan en total?", "50-4-15", "Se restan las orugas comidas al total.")],
  selfcheck=[("Nombra los cuatro postulados de la selección natural.", "Variación, herencia, más nacimientos que supervivientes y supervivencia diferencial", "Forman el mecanismo de la teoría."), ("¿Quiénes propusieron la selección natural?", "Charles Darwin y Alfred Russel Wallace", "Lo hicieron de forma independiente."), ("¿Cambian los individuos por necesidad?", "No, el ambiente favorece variaciones que ya existían", "La selección actúa sobre la variación existente.")],
  open_task=task("Pon 20 papelitos verdes y 20 rojos sobre una hoja verde (o dibuja puntos). Calcula en una tabla tres rondas: en cada ronda el «depredador» ve antes los rojos y quita 6 rojos y 2 verdes, y después se duplica lo que queda de cada color. La primera ronda puedes comprobarla con los papelitos y las otras dos hacerlas solo con números. Explica con los postulados qué rasgo se vuelve más común.", "Ronda 1: quedan 14 rojos y 18 verdes, y luego 28 y 36. Ronda 2: quedan 22 y 34, y luego 44 y 68. Ronda 3: quedan 38 y 66, y luego 76 y 132. Los verdes pasan de la mitad a casi dos tercios. Explicación: hay variación de color, se hereda, nacen más individuos de los que sobreviven y los verdes tienen ventaja sobre la hoja verde.", ["registra tres rondas", "usa al menos tres postulados", "concluye qué rasgo aumenta"], ["tabla con conteos y explicación"], ["decir que los papelitos cambian de color", "no registrar los números"], "Pregunta qué cambiarías en el modelo para que los rojos tuvieran ventaja."),
  reinforce="Explica con un ejemplo de animal por qué el camuflaje puede aumentar en una población.",
  extend="Explica por qué la selección natural no tiene un objetivo ni una dirección fija.")

L(OA2, 4,
  materials="Este cuaderno, lápiz y regla. Las secuencias de ADN y las tablas de comparación están escritas en los ejercicios.",
  use="Aprenderé a comparar secuencias de ADN y datos de embriología para estimar qué tan emparentadas están dos especies. Sirve para relacionar dos variables: diferencias en el ADN y cercanía de parentesco.",
  prior=["Sé que el ADN es el material hereditario.", "Sé leer tablas y comparar datos."],
  explain=[
      "El ADN de un ser vivo es una secuencia larga de cuatro letras químicas: A, T, G y C. Al comparar dos secuencias letra por letra, se cuentan las diferencias. Mientras menos diferencias hay, más cercano es el parentesco: las dos especies tuvieron un ancestro común más reciente. Con más diferencias, el ancestro común es más antiguo.",
      "Esto ocurre porque las mutaciones, que son cambios aleatorios en el ADN, se acumulan con el tiempo. Si dos líneas se separaron hace mucho, tuvieron más tiempo para acumular diferencias. Esta relación entre dos variables, número de diferencias y tiempo de separación, es la base del llamado reloj molecular.",
      "La embriología aporta datos parecidos. Embriones de peces, aves y mamíferos se parecen mucho en etapas tempranas y se diferencian más tarde. Cuando la evidencia anatómica, la de ADN y la de los fósiles coinciden, la conclusión es más sólida.",
  ],
  vocab=[("ADN", "molécula que guarda la información hereditaria"), ("mutación", "cambio aleatorio en la secuencia del ADN"), ("reloj molecular", "idea de que las diferencias de ADN aumentan con el tiempo de separación"), ("comparar secuencias", "contar diferencias letra por letra"), ("variable", "dato que cambia y se puede medir")],
  worked=[
      ("Contar diferencias", "Secuencia 1: ATGC; secuencia 2: ATCC. ¿Cuántas diferencias hay?", ["Comparo letra por letra: A con A, T con T, G con C, C con C.", "Solo difiere la tercera letra."], "1 diferencia"),
      ("Interpretar la comparación", "Las especies P y Q difieren en 2 letras y las especies P y R en 9. ¿Con cuál está más emparentada P?", ["Menos diferencias indican ancestro común más reciente.", "2 es menor que 9."], "Con la especie Q"),
  ],
  mistakes=[
      ("Contar solo las letras iguales y olvidar las diferencias.", "El parentesco se estima a partir del número de diferencias.", "Marca cada posición distinta y suma."),
      ("Concluir el parentesco con una secuencia de solo 4 letras.", "Una muestra muy corta puede dar resultados engañosos.", "Declara que se necesitan secuencias largas para una conclusión firme."),
  ],
  rec=[
      ("¿Cuáles son las cuatro letras del ADN?", "A, T, G y C", "Son las cuatro bases químicas."),
      ("Completa: a menos diferencias en el ADN, el parentesco es ______ (más cercano o más lejano).", "Más cercano", "El ancestro común es más reciente."),
      ("Verdadero o falso: las mutaciones son cambios aleatorios en el ADN.", "Verdadero", "Se van acumulando con el tiempo."),
  ],
  und=[
      ("Dos especies tienen casi la misma secuencia de ADN. ¿Qué indica eso? A) Que se separaron hace relativamente poco tiempo; B) Que viven en el mismo hábitat.", "A", "Tuvieron poco tiempo para acumular mutaciones."),
      ("¿Por qué se acumulan más diferencias si el tiempo de separación es mayor? A) Porque las mutaciones ocurren con el tiempo y se heredan; B) Porque el ADN se cambia por voluntad.", "A", "Mientras más tiempo, más mutaciones acumuladas."),
      ("Embriones de pez y de pollo se parecen en etapas tempranas. ¿Qué evidencia es?", "Embriología", "Compara el desarrollo temprano."),
  ],
  app=[
      ("Secuencias de 10 letras. Especie 1: ATGCCGTAAC; especie 2: ATGCCGTTAC; especie 3: ATCCGGTTAG; especie 4: TTCCGGATAG. ¿Cuántas diferencias hay entre la especie 1 y la 2?", "1", "Solo difiere la octava letra (A en la 1 y T en la 2)."),
      ("Con las mismas secuencias (especie 1: ATGCCGTAAC; especie 3: ATCCGGTTAG), ¿cuántas diferencias hay entre la especie 1 y la 3?", "4", "Difieren las posiciones 3, 5, 8 y 10: G/C, C/G, A/T y C/G."),
      arith("Una tabla de ejemplo dice: P y Q difieren en 3 letras; P y R difieren en 11 letras. ¿Cuántas diferencias más tiene P con R que con Q?", "11-3", "Se resta el número menor al mayor."),
  ],
  rea=[
      ("Especies 2 y 3 difieren en 3 letras; 2 y 4 en 5 letras; 3 y 4 en 2 letras. ¿Qué par de especies está más emparentado? A) Especies 3 y 4; B) Especies 2 y 4.", "A", "El par con menos diferencias es el de las especies 3 y 4."),
      ("Un compañero dice: «Como los delfines y los tiburones se parecen por fuera, tienen ADN casi igual». ¿Qué responderías? A) La apariencia no es la medida: hay que comparar las secuencias; B) Tiene razón, porque ambos nadan.", "A", "El parecido externo puede ser análogo y no indicar parentesco."),
  ],
  cha=[
      ("Cuatro especies tienen diferencias de ADN con una especie de referencia X: A, 2; B, 8; C, 5; D, 12. Ordena las cuatro de la más cercana a la más lejana de X escribiendo las letras separadas por comas.", "A, C, B, D", "Se ordenan de menor a mayor número de diferencias: 2, 5, 8, 12."),
      arith("Un laboratorio de ejemplo compara dos secuencias de 200 letras y encuentra 14 diferencias. ¿Cuántas letras son iguales?", "200-14", "Se restan las diferencias al total de letras."),
  ],
  context=[arith("En una clase de ejemplo se comparan 5 pares de secuencias; cada par tiene 6 diferencias. ¿Cuántas diferencias se contaron en total?", "5*6", "Se multiplica el número de pares por sus diferencias.")],
  selfcheck=[("¿Qué indica un menor número de diferencias en el ADN?", "Un parentesco más cercano", "El ancestro común es más reciente."), ("¿Qué es una mutación?", "Un cambio aleatorio en el ADN", "Se acumulan con el tiempo."), ("¿Por qué conviene comparar secuencias largas?", "Porque una muestra corta puede engañar", "Más letras dan una conclusión más firme.")],
  open_task=task("Compara estas tres secuencias de 8 letras: especie X: ATGGCTAA; especie Y: ATGGCTAT; especie Z: TTGACTAT. Cuenta las diferencias entre X e Y, entre X y Z y entre Y y Z. Después escribe cuál par está más emparentado y una limitación de la comparación.", "X-Y: 1; X-Z: 3; Y-Z: 2. Más emparentadas X e Y. Limitación: solo se comparan 8 letras, una muestra muy corta.", ["tres conteos correctos", "elige el par con menos diferencias", "declara la limitación de la muestra corta"], ["tabla de conteos y conclusión"], ["contar letras iguales como diferencias", "no mencionar el tamaño de la muestra"], "Pregunta cuántas letras más compararías para tener más seguridad."),
  reinforce="Inventa dos secuencias de 6 letras con exactamente 2 diferencias y señálalas.",
  extend="Explica por qué la coincidencia entre datos de ADN, anatomía y fósiles da una conclusión más sólida.")

L(OA2, 5,
  materials="Este cuaderno y lápiz. Los datos de poblaciones y bacterias están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé a explicar patrones de evolución que se observan hoy, como la resistencia de bacterias a antibióticos, usando la selección natural. Sirve para entender un problema de salud pública.",
  prior=["Sé los postulados de la selección natural.", "Sé que la variación existe antes de la selección."],
  explain=[
      "La selección natural puede observarse en poblaciones que se reproducen rápido. Una población de bacterias tiene variación: casi todas mueren con un antibiótico, pero unas pocas, por una mutación al azar, resisten. Al aplicar el antibiótico, mueren las sensibles y sobreviven las resistentes, que se multiplican sin competencia. La población que resulta es mayormente resistente.",
      "El mecanismo es el mismo que en los postulados: variación heredable, más descendientes que supervivientes, supervivencia diferencial. Nota que el antibiótico no crea la resistencia; solo favorece a quienes ya la tenían. Por eso, dejar un tratamiento a medias deja con vida a las más resistentes, que se reproducirán.",
      "Otro patrón es la adaptación, un rasgo que mejora la supervivencia en un ambiente. Una adaptación es resultado de muchas generaciones, no de un esfuerzo individual. Las poblaciones se adaptan; los individuos no se vuelven resistentes por querer. La selección natural no tiene meta: solo favorece lo que funciona en el ambiente actual.",
  ],
  vocab=[("resistencia", "capacidad de sobrevivir a un antibiótico u otra sustancia"), ("antibiótico", "medicamento que elimina bacterias"), ("adaptación", "rasgo que mejora la supervivencia en un ambiente"), ("generación", "grupo de individuos que nacen en un mismo momento"), ("supervivencia diferencial", "algunos sobreviven más que otros por su rasgo")],
  worked=[
      ("Resistencia en bacterias", "Una población tiene 1.000 bacterias; 5 son resistentes a un antibiótico. Se aplica el antibiótico y mueren todas las sensibles. ¿Cuántas sobreviven?", ["Las sensibles mueren.", "Solo sobreviven las 5 resistentes."], "5 bacterias"),
      ("Explicar un patrón", "Con el tiempo, la proporción de bacterias resistentes aumenta en un hospital donde se usa mucho un antibiótico. Explica por qué.", ["El antibiótico elimina las sensibles.", "Las resistentes sobreviven y se reproducen y transmiten el rasgo.", "Después de varias generaciones, casi todas son resistentes."], "Porque el antibiótico favorece a las que ya eran resistentes"),
  ],
  mistakes=[
      ("Pensar que el antibiótico «provoca» la mutación de resistencia.", "La variación ya existía; el antibiótico solo selecciona.", "Explica primero la variación y después la selección."),
      ("Decir que las bacterias «aprenden» a resistir.", "No hay aprendizaje: sobreviven y se reproducen las que tienen un rasgo heredado.", "Usa «sobreviven y dejan descendientes» en vez de «aprenden»."),
  ],
  rec=[
      ("¿Qué es la resistencia a un antibiótico?", "La capacidad de sobrevivir a un antibiótico", "Algunas bacterias la tienen por una variación."),
      ("Completa: el antibiótico favorece a las bacterias ______ (resistentes o sensibles).", "Resistentes", "Son las que sobreviven al tratamiento."),
      ("Verdadero o falso: una adaptación se forma en la vida de un solo individuo.", "Falso", "Es resultado de muchas generaciones."),
  ],
  und=[
      ("¿Qué crea la variación en una población de bacterias? A) Mutaciones al azar; B) El antibiótico.", "A", "El antibiótico solo selecciona lo que ya existe."),
      ("¿Por qué una población se vuelve resistente después de varias generaciones? A) Porque las resistentes sobreviven y dejan más descendientes; B) Porque cada bacteria se esfuerza por resistir.", "A", "Es supervivencia diferencial con herencia."),
      ("Un rasgo mejora la supervivencia en el ambiente actual. ¿Cómo se llama?", "Adaptación", "Es un rasgo ventajoso en ese ambiente."),
  ],
  app=[
      arith("Una población de ejemplo tiene 2.000 bacterias y 8 son resistentes. Se aplica un antibiótico y mueren todas las sensibles. ¿Cuántas bacterias sensibles mueren?", "2000-8", "Se restan las resistentes al total."),
      arith("Las 8 bacterias resistentes se reproducen por división: en cada ronda cada bacteria se divide en dos. ¿Cuántas resistentes hay después de 3 rondas?", "8*2*2*2", "Se duplica el número tres veces seguidas."),
      ("En una isla de ejemplo, tras una sequía quedan más semillas duras que blandas, y los pájaros de pico fuerte sobreviven más. Después de varias generaciones, ¿qué esperas que aumente en la población? A) Los individuos con pico fuerte; B) Los individuos con pico débil.", "A", "El pico fuerte permite comer semillas duras y deja más descendientes."),
  ],
  rea=[
      ("Una persona deja de tomar un antibiótico recetado al sentirse mejor, antes de terminar el tratamiento. ¿Por qué es riesgoso, según lo aprendido? A) Pueden quedar vivas bacterias más resistentes que se multipliquen; B) El antibiótico se acumula y causa resistencia.", "A", "Un tratamiento incompleto favorece a las más resistentes."),
      ("Un compañero dice que las jirafas alargaron el cuello al estirarse en su vida y lo heredaron. ¿Qué falla tiene? A) Los rasgos que se adquieren en la vida no se heredan; la selección actúa sobre variaciones heredables; B) Las jirafas no tenían cuello.", "A", "Un esfuerzo individual no cambia la herencia."),
  ],
  cha=[
      ("Datos de ejemplo: generación 1, 100 bacterias con 2 resistentes; tras el antibiótico y la reproducción, la generación 2 tiene 100 bacterias con 40 resistentes. ¿En cuántas veces aumentó el número de resistentes?", "20", "Pasaron de 2 a 40, que es 20 veces."),
      ("Un hospital cambia de antibiótico cada semana sin necesidad. Un investigador dice que no soluciona el problema de fondo. ¿Qué razón es mejor? A) Usar antibióticos sin necesidad aumenta la presión de selección sobre las bacterias; B) Los antibióticos nuevos no existen.", "A", "Mientras más se usan sin necesidad, más se selecciona la resistencia."),
  ],
  context=[arith("Un hospital de ejemplo registra 120 infecciones; 45 resisten el primer antibiótico. ¿Cuántas no lo resisten?", "120-45", "Se restan las infecciones resistentes al total.")],
  selfcheck=[("¿Cómo se vuelve resistente una población de bacterias?", "Sobreviven y se reproducen las que ya eran resistentes", "El antibiótico selecciona la variación existente."), ("¿Por qué no hay que dejar un tratamiento a medias?", "Porque pueden sobrevivir las bacterias más resistentes", "Se favorece la resistencia."), ("¿Qué es una adaptación?", "Un rasgo que mejora la supervivencia en un ambiente", "Surge tras muchas generaciones.")],
  open_task=task("Usa estos datos de ejemplo de un cultivo de bacterias: inicio, 1.000 bacterias con 4 resistentes; después de aplicar el antibiótico, solo viven las resistentes; luego se reproducen y llegan a 1.000 bacterias. Escribe en un párrafo de cuatro oraciones cómo explica la selección natural el cambio entre el inicio y el final, usando las palabras variación, supervivencia y descendientes.", "Al inicio había variación: 4 bacterias eran resistentes. El antibiótico mató a las sensibles, y esa supervivencia diferencial dejó solo a esas 4. Luego se reprodujeron y dejaron descendientes resistentes. Al final, casi toda la población es resistente.", ["usa las tres palabras clave", "explica el orden de los hechos", "no dice que las bacterias aprendieron"], ["párrafo de cuatro oraciones"], ["decir que el antibiótico crea la mutación", "omitir la herencia"], "Pregunta qué cambiaría si hubiera 0 bacterias resistentes al inicio."),
  reinforce="Explica con tus palabras por qué el uso innecesario de antibióticos es un problema.",
  extend="Explica por qué dos poblaciones de la misma especie en ambientes distintos pueden adaptarse de forma diferente.")

L(OA2, 6,
  materials="Este cuaderno y lápiz. Las afirmaciones y los datos de ejemplo están escritos en los ejercicios.",
  use="Aprenderé a evaluar los límites de las evidencias de la evolución, a corregir malentendidos y a ver sus implicancias para la salud. Sirve para evaluar afirmaciones con criterio.",
  prior=["Sé las evidencias y el mecanismo de la selección natural.", "Sé que una conclusión debe declarar sus límites."],
  explain=[
      "En ciencia, una teoría es una explicación amplia, respaldada por muchas evidencias y comprobada de distintas maneras; no es una simple suposición. La evolución por selección natural es una teoría de este tipo. Aun así, cada evidencia tiene límites. El registro fósil es incompleto, porque pocos organismos se fosilizan, y hay lagunas en la secuencia. Las comparaciones de ADN dependen de cuántas especies y qué tan largas son las secuencias.",
      "Hay malentendidos frecuentes. «Evoluciona el más fuerte» es falso: sobrevive quien tiene el rasgo más ventajoso en ese ambiente. «Los humanos vienen de los chimpancés» también es falso: humanos y chimpancés comparten un ancestro común, de donde se separaron dos líneas. «La evolución tiene una meta» tampoco es cierto, porque no hay dirección prefijada.",
      "Las implicancias son prácticas: entender la selección natural ayuda a usar bien los antibióticos, a cuidar la biodiversidad y a diseñar cultivos. Una persona que usa antibióticos debe seguir la indicación médica. Si tiene dudas sobre un tratamiento, consulta a una persona adulta de confianza o a un profesional de la salud.",
  ],
  vocab=[("teoría científica", "explicación amplia respaldada por muchas evidencias"), ("laguna", "parte que falta en un registro"), ("ancestro común", "especie de la que descienden varias líneas"), ("biodiversidad", "variedad de seres vivos"), ("limitación", "aspecto que impide afirmar más de lo observado")],
  worked=[
      ("Corregir un malentendido", "Alguien dice: «Los humanos descienden de los chimpancés». Corrige la frase.", ["Recuerdo que ambos comparten un ancestro común.", "Humanos y chimpancés son dos líneas que se separaron de ese ancestro."], "Humanos y chimpancés comparten un ancestro común; unos no descienden de los otros"),
      ("Límite del registro fósil", "Un corte de roca no muestra fósiles de cierto grupo durante un largo período. ¿Qué conclusión es prudente?", ["Pocos organismos se fosilizan.", "La ausencia puede deberse a una laguna del registro y no a que el grupo no existiera."], "No se puede concluir que el grupo no existía"),
  ],
  mistakes=[
      ("Concluir que, si no hay un fósil, la especie no existió.", "El registro fósil es incompleto.", "Di «no se ha encontrado» en vez de «no existió»."),
      ("Llamar «solo una teoría» a la evolución, como si fuera una duda.", "En ciencia, una teoría está muy respaldada por evidencias.", "Explica cuántas evidencias independientes la apoyan."),
  ],
  rec=[
      ("¿Es la evolución una meta fija hacia la que avanzan los seres vivos?", "No", "La selección natural no tiene dirección ni meta."),
      ("Completa: el registro fósil es ______ (completo o incompleto).", "Incompleto", "Pocos organismos se fosilizan."),
      ("Verdadero o falso: en ciencia, una teoría es una suposición sin evidencias.", "Falso", "Una teoría es una explicación respaldada por muchas evidencias."),
  ],
  und=[
      ("¿Qué ancestro tienen humanos y chimpancés? A) Uno común; B) Los chimpancés son el ancestro de los humanos.", "A", "Ambos descienden de una especie ancestral común."),
      ("¿Por qué «evoluciona el más fuerte» es un malentendido? A) Porque sobrevive el que tiene el rasgo más ventajoso en ese ambiente; B) Porque la fuerza nunca sirve.", "A", "La ventaja depende del ambiente."),
      ("Una limitación del registro fósil es que ______ (pocos organismos se fosilizan o todos los organismos se fosilizan).", "Pocos organismos se fosilizan", "Hay lagunas en la secuencia."),
  ],
  app=[
      ("Una persona dice: «No hay fósiles de cierto grupo en este cerro, así que ese grupo no existía». ¿Qué conclusión es más prudente? A) No se han encontrado fósiles en este cerro, pero podría haber lagunas; B) El grupo no existió en ninguna parte.", "A", "La ausencia en un lugar no prueba la ausencia en el mundo."),
      arith("Un registro de ejemplo tiene 24 especies conocidas de un grupo; en un cerro solo se encuentran fósiles de 9. ¿Cuántas especies no dejaron fósiles en ese cerro?", "24-9", "Se restan las especies halladas al total."),
      ("Una receta médica dice tomar un antibiótico durante 7 días, pero a los 3 días la persona se siente bien. ¿Qué debería hacer? A) Seguir la indicación médica completa; B) Guardar las pastillas para otra enfermedad.", "A", "Cortar antes favorece a las bacterias más resistentes."),
  ],
  rea=[
      ("Un estudiante afirma: «Como la evolución tiene una meta, las especies actuales son las más perfectas». ¿Qué responderías? A) No hay meta ni perfección: cada especie se ajusta a su ambiente; B) Tiene razón, porque están vivas.", "A", "La selección natural favorece lo que funciona en cada ambiente, sin meta."),
      ("Una comparación de ADN usa solo dos especies. ¿Qué límite tiene? A) Con tan pocas especies no se puede reconstruir el parentesco de un grupo grande; B) El ADN no sirve para comparar.", "A", "Se necesitan más especies para ver el patrón de parentesco."),
  ],
  cha=[
      ("Datos de ejemplo: en un país, el 10 % de las infecciones eran resistentes hace años y hoy lo son el 30 %. Una autoridad propone reducir el uso innecesario de antibióticos. ¿Qué datos de seguimiento sostendrían que funcionó? A) Que baje el porcentaje de infecciones resistentes en los años siguientes; B) Que se vendan más antibióticos.", "A", "El resultado esperado es una menor presión de selección y menos resistencia."),
      ("Un museo quiere mostrar «la escalera de la evolución» desde un pez hasta un humano en línea recta. ¿Qué problema tiene ese diseño? A) Sugiere una meta lineal, pero la evolución se ramifica; B) No se pueden dibujar peces.", "A", "El esquema correcto es un árbol con ramas."),
  ],
  context=[arith("Un folleto de ejemplo dice que 3 de cada 10 infecciones son resistentes. En una clínica de ejemplo hay 40 infecciones; ¿cuántas serían resistentes si se cumple esa proporción?", "40//10*3", "Se calculan 4 grupos de 10 y se multiplica por 3.")],
  selfcheck=[("¿Por qué el registro fósil es incompleto?", "Porque pocos organismos se fosilizan", "Por eso hay lagunas en la secuencia."), ("¿Humanos y chimpancés descienden unos de otros?", "No, comparten un ancestro común", "Es una corrección frecuente."), ("¿Por qué se debe seguir la indicación médica con los antibióticos?", "Para no favorecer a bacterias resistentes", "Un tratamiento incompleto deja vivas a las más resistentes.")],
  open_task=task("Lee estas cuatro afirmaciones: (1) «La evolución es solo una teoría, o sea una suposición.» (2) «Sobrevive siempre el más fuerte.» (3) «No hay fósil de este animal, entonces nunca existió.» (4) «Los humanos vienen de los chimpancés.» Para cada una, escribe una corrección en una frase usando una evidencia o un concepto de esta clase, y marca cuál de las cuatro te parece más frecuente en tu entorno.", "1: una teoría científica está respaldada por muchas evidencias. 2: sobrevive quien tiene el rasgo ventajoso en su ambiente. 3: el registro fósil es incompleto. 4: ambos comparten un ancestro común.", ["cuatro correcciones", "cada una usa un concepto de la clase", "marca una afirmación como más frecuente"], ["cuatro frases y una marca"], ["repetir la afirmación sin corregirla", "usar «solo una teoría» como duda"], "Pregunta qué evidencia mostrarías a quien sostiene la afirmación que marcaste."),
  reinforce="Escribe una frase que corrija el malentendido «la evolución tiene una meta».",
  extend="Explica por qué entender la selección natural cambia la manera de usar antibióticos.")

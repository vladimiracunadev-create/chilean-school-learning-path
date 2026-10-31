"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 03 (actividad humana y redes alimentarias) y OA 04 (sistema reproductor humano)."""
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


OA3, OA4 = "CN06 OA 03", "CN06 OA 04"

# ---------------------------------------------------------------- OA 03
L(OA3, 1,
  materials="Este cuaderno y lápiz. Los registros de ecosistemas están escritos en los ejercicios y son datos de ejemplo.",
  use="Aprenderé qué acciones humanas afectan las redes alimentarias y a separar lo que muestran los datos de lo que se supone. Sirve para leer informes ambientales.",
  prior=["Sé que una red alimentaria muestra quién se alimenta de quién.", "Sé que un cambio en una población puede afectar a otras."],
  explain=[
      "Las personas modifican los ecosistemas de varias formas. La sobrepesca y la caza excesiva sacan más individuos de los que se pueden reponer. La tala y los incendios quitan el hogar y el alimento de muchas especies. Los contaminantes, como pesticidas o plásticos, entran a las cadenas. Una especie introducida es la que llega a un lugar donde no vivía y puede competir con las nativas.",
      "Estos cambios afectan a toda la red. Si se pesca demasiado de una especie, sus depredadores quedan con menos alimento y sus presas pueden aumentar. Si un contaminante entra en el agua, pasa de los organismos pequeños a los que se los comen. Por eso los efectos pueden aparecer lejos de donde ocurrió la acción.",
      "Al leer un registro hay que separar lo que se observa de lo que se supone. Una observación es «en 2020 se capturaron 800 toneladas y en 2024, 300». Una interpretación es «la causa fue únicamente la pesca». Que dos cosas ocurran a la vez no prueba que una cause la otra. Para afirmar una causa se necesitan más datos.",
  ],
  vocab=[("actividad humana", "acción de las personas que modifica el ambiente"), ("sobrepesca", "pescar más de lo que la población puede reponer"), ("especie introducida", "especie que llega a un lugar donde no vivía"), ("especie nativa", "especie que vive naturalmente en un lugar"), ("contaminante", "sustancia que daña el ambiente o a los seres vivos")],
  worked=[
      ("Observación o interpretación", "Un informe de ejemplo dice: (1) «Las capturas de un pez bajaron de 900 a 400 toneladas en 6 años». (2) «Los pescadores son los únicos culpables». ¿Cuál es la observación?", ["Pregunto qué frase tiene datos que se miden.", "La frase 1 tiene cifras.", "La frase 2 asigna una culpa sin evidencia."], "La frase 1 es la observación"),
      ("Nativa o introducida", "Una especie de mamífero llegó a un bosque desde otro continente y se come las aves del lugar. ¿Es nativa o introducida?", ["Veo de dónde viene: de otro continente.", "No vivía antes en el bosque.", "Eso define a una especie introducida."], "Es una especie introducida"),
  ],
  mistakes=[
      ("Afirmar que una acción humana causó un cambio solo porque ocurrieron al mismo tiempo.", "Dos hechos simultáneos no prueban que uno cause al otro.", "Busca más datos y otras posibles causas."),
      ("Creer que el efecto aparece solo en el lugar donde ocurre la acción.", "En una red los efectos viajan por las relaciones de alimentación.", "Sigue las flechas para ver quién más se ve afectado."),
  ],
  rec=[
      ("Pescar más de lo que la población puede reponer se llama ______. Completa con «sobrepesca» o «pesca artesanal».", "Sobrepesca", "Es la pesca excesiva."),
      ("Una especie que llega a un lugar donde no vivía, ¿es nativa o introducida?", "Introducida", "No pertenece originalmente al lugar."),
      ("¿La frase «bajaron las capturas de 500 a 300 toneladas» es observación o interpretación?", "Observación", "Contiene cifras medidas."),
  ],
  und=[
      ("¿Cuál frase es una interpretación? A) En 2022 hubo 120 aves y en 2024 hubo 80. B) Las aves se fueron por culpa de los turistas.", "B", "La causa no se midió."),
      ("Si se pescan demasiados depredadores de un pez pequeño, ¿qué le puede pasar a ese pez pequeño?", "Puede aumentar", "Tiene menos depredadores."),
      ("¿Por qué que dos hechos ocurran a la vez no prueba que uno cause al otro?", "Porque puede haber otra causa o coincidencia", "Se necesitan más datos."),
  ],
  app=[
      arith("En un registro de ejemplo las capturas de una especie bajaron de 900 a 400 toneladas. ¿Cuántas toneladas bajaron?", "900-400", "Se resta la cantidad final de la inicial."),
      arith("Un río tiene 240 truchas introducidas y 60 peces nativos. ¿Cuántos peces hay en total?", "240+60", "Se suman ambos grupos."),
      ("Una laguna tenía 50 aves en 2019 y 20 en 2023. Un comentario dice que la causa es una fábrica nueva. ¿Qué dato falta para afirmarlo? A) Cuándo empezó a funcionar y si hubo otras causas. B) De qué color es la fábrica.", "A", "Hace falta saber si coincide en el tiempo y si hay otras causas."),
  ],
  rea=[
      ("Un compañero dice: «Como bajó la lluvia y bajaron los peces, la lluvia mató a los peces». ¿Es una conclusión firme? Responde Sí o No y explica.", "No; falta evidencia de que una cause la otra", "Pueden coincidir sin que haya relación directa."),
      ("Un informe dice: (1) «Subieron los conejos introducidos y bajó el pasto». (2) «Los conejos son dañinos por naturaleza». ¿Cuál frase es la observación?", "La frase 1", "La frase 1 son hechos medidos y la 2 es un juicio."),
  ],
  cha=[
      ("Una especie introducida come huevos de aves nativas. Si las aves nativas son la presa de un zorro, ¿qué efecto indirecto puede sentir el zorro?", "Menos alimento", "Disminuyen las aves que cazaba."),
      ("En una red, un pesticida está en el pasto. Un conejo come el pasto y un zorro come al conejo. ¿Quién recibe el pesticida de forma indirecta?", "El zorro", "Lo recibe al comer al conejo."),
  ],
  context=[("Dato de ejemplo. Una costa tenía 1.200 toneladas de captura en 2015 y 700 en 2023. ¿Cuántas toneladas menos se capturaron en 2023?", "500", "1.200 − 700 = 500.")],
  selfcheck=[("¿Qué es una especie introducida?", "Una que llega a un lugar donde no vivía", "Puede competir con las nativas."), ("¿Por qué los efectos se notan lejos de la acción?", "Porque viajan por las relaciones de alimentación", "Las redes están conectadas."), ("¿Por qué hay que cuidar la palabra causa?", "Porque dos hechos simultáneos no prueban relación", "Hace falta más evidencia.")],
  open_task=task("Lee este registro simulado: en una bahía la captura de un pez bajó de 1.000 toneladas (2016) a 400 (2024) y los lobos marinos que comían ese pez pasaron de 300 a 180 individuos. Escribe tres observaciones con números y una interpretación prudente, con la palabra «podría».", "Observaciones: la captura bajó 600 toneladas; los lobos bajaron 120 individuos; ambos bajaron entre 2016 y 2024. Interpretación: la menor disponibilidad de pez podría afectar a los lobos marinos.", ["tres observaciones con números", "una interpretación prudente", "separa observación de interpretación"], ["lista de cuatro frases"], ["afirmar causa segura", "mezclar datos con suposiciones"], "Pregunta qué otro dato ayudaría a comprobar la interpretación."),
  reinforce="Escribe una actividad humana que pueda afectar a una red alimentaria y una observación que la mostraría.",
  extend="Explica por qué una especie introducida puede alterar toda una red alimentaria.")

L(OA3, 2,
  materials="Este cuaderno y lápiz. Todos los ecosistemas y datos están escritos en los ejercicios.",
  use="Aprenderé a formular preguntas y predicciones sobre cómo una actividad humana cambia una red alimentaria. Sirve para anticipar problemas ambientales.",
  prior=["Sé que las actividades humanas afectan a los ecosistemas.", "Sé que una predicción lleva una razón."],
  explain=[
      "Para analizar el efecto de una actividad humana se formula una pregunta que se pueda comprobar con datos. Por ejemplo: «¿Cuántas aves nativas viven en un humedal antes y después de que se instale una carretera cerca?». La pregunta nombra qué cambió y qué se mide, y se puede responder contando aves.",
      "Una predicción dice qué se espera y por qué. Por ejemplo: «Si se talan árboles de un bosque, los herbívoros que comen sus hojas disminuirán, porque pierden alimento; después disminuirán los carnívoros que los cazan». Fíjate que el efecto sigue las flechas de la red: primero a los que dependen directamente y luego a los demás.",
      "Una predicción útil usa la palabra «probablemente», porque en la naturaleza influyen otros factores. También conviene decir cuánto tiempo se observará y con qué datos se comprobará. Si el resultado no coincide, se revisa la idea y se buscan otras causas, no se cambian los datos.",
  ],
  vocab=[("humedal", "zona con agua poco profunda donde viven aves y plantas"), ("tala", "corte de árboles"), ("pregunta comprobable", "pregunta que se responde con datos"), ("efecto en cadena", "cambio que pasa de un organismo a otro"), ("probablemente", "palabra que indica que algo es posible pero no seguro")],
  worked=[
      ("Predecir un efecto en cadena", "En un bosque se talan los árboles que producen frutos. Un ave come esos frutos y un gavilán come al ave. ¿Qué predices para el ave y para el gavilán?", ["Sin frutos, el ave tiene menos alimento.", "Menos aves, menos alimento para el gavilán.", "Sigo las flechas: frutos, ave, gavilán."], "Probablemente disminuyan las aves y luego los gavilanes"),
      ("Pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Es mala la tala de árboles? B) ¿Cuántos ejemplares de un ave viven en 100 hectáreas antes y después de una tala?", ["Busco una pregunta con números.", "La B se responde contando.", "La A pide una opinión."], "B"),
  ],
  mistakes=[
      ("Predecir solo el efecto directo e ignorar a los demás organismos.", "El cambio llega también a organismos más lejanos de la red.", "Sigue las flechas al menos dos pasos."),
      ("Hacer una predicción que no se puede comprobar, como «todo será peor».", "No dice qué se medirá ni cuándo.", "Indica qué población se cuenta y en qué plazo."),
  ],
  rec=[
      ("Cortar árboles se llama ______. Completa con «tala» o «siembra».", "Tala", "La tala es el corte de árboles."),
      ("¿Una predicción se hace antes o después de ver los resultados?", "Antes", "Se plantea lo que se espera que ocurra."),
      ("Si desaparece el alimento de un animal, ¿su población probablemente aumenta o disminuye?", "Disminuye", "Tiene menos con qué sobrevivir."),
  ],
  und=[
      ("¿Cuál es una pregunta comprobable? A) ¿Cuántas aves nativas hay en un humedal antes y después de una obra? B) ¿Es feo un humedal sin aves?", "A", "Las aves se cuentan."),
      ("En frutos → ave → gavilán, si baja el número de aves, ¿qué probablemente le pasa al gavilán?", "Disminuye", "Tiene menos presas."),
      ("¿Por qué conviene usar «probablemente» en una predicción?", "Porque influyen otros factores", "Evita asegurar algo que puede variar."),
  ],
  app=[
      arith("En 100 hectáreas había 80 aves. Tras una tala quedó la mitad. ¿Cuántas aves quedaron?", "80//2", "Se divide en dos partes iguales."),
      arith("Se hace un conteo anual de aves en un humedal durante 5 años y se registran 12 aves cada año. ¿Cuántas aves se registran en total?", "12*5", "Se multiplica el conteo anual por los años."),
      ("Completa la predicción con una palabra: «Si aumenta el plástico en el mar, las tortugas que lo confunden con medusas probablemente ______». Elige disminuirán o aumentarán.", "Disminuirán", "El plástico les provoca daño."),
  ],
  rea=[
      ("Mario predice: «Si se prohíbe cazar zorros, los conejos disminuirán porque habrá más zorros». ¿Su razón sigue las flechas de la red? Responde Sí o No.", "Sí", "Más zorros comen más conejos."),
      ("Clara predice: «Si se pesca mucho una especie, todo el mar quedará vacío». ¿Qué palabra la vuelve difícil de comprobar?", "Todo", "No dice qué población se medirá."),
  ],
  cha=[
      ("El pasto lo comen los conejos y los conejos los come el zorro. Llega una especie introducida que también come pasto. ¿Qué predicción tiene razón? A) Los conejos podrían disminuir, porque competirían por el pasto. B) Los conejos aumentarán, porque sí.", "A", "La A da una razón basada en la red."),
      ("Una escuela quiere medir el efecto de arrojar basura cerca de un estero. ¿Cuál es una medida comprobable? A) El número de ranas por 10 metros de orilla cada mes. B) La opinión de los vecinos.", "A", "Las ranas se pueden contar."),
  ],
  context=[("Dato de ejemplo. Un humedal tenía 150 aves antes de una obra y 90 después. ¿Cuántas aves menos hay?", "60", "150 − 90 = 60.")],
  selfcheck=[("¿Qué debe tener una pregunta comprobable?", "Algo que se pueda contar o medir", "Así se responde con datos."), ("¿Cómo se sigue un efecto en cadena?", "Con las flechas de la red", "Pasa de un organismo a otro."), ("¿Qué indica la palabra «probablemente»?", "Que algo es posible pero no seguro", "Influyen otros factores.")],
  open_task=task("Una empresa quiere instalar un criadero de salmones cerca de una bahía donde viven algas, pequeños crustáceos, peces y lobos marinos. Escribe una pregunta comprobable, dos predicciones con razón siguiendo la red y qué contarías para comprobarlas.", "Pregunta: ¿cuántos peces nativos hay por mes antes y después? Predicción 1: los crustáceos podrían disminuir si hay más desechos. Predicción 2: los lobos marinos podrían acercarse al criadero. Conteo: peces y lobos en la bahía cada mes.", ["pregunta con algo contable", "dos predicciones con razón", "qué se contaría"], ["tres frases escritas"], ["predecir sin razón", "no decir qué se mide"], "Pregunta qué cambiaría si hubiera otro criadero en la bahía vecina."),
  reinforce="Escribe una predicción sobre un humedal si se vierte aceite en él.",
  extend="Explica por qué conviene medir antes y después de una actividad humana.")

L(OA3, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a modelar cómo un contaminante o un cambio viaja por una red alimentaria. Sirve para explicar por qué algunos animales grandes se ven muy afectados.",
  prior=["Sé que las flechas muestran quién come a quién.", "Sé que hay menos energía en los niveles altos."],
  explain=[
      "Un modelo de red alimentaria sirve para seguir un cambio. Si quitas una especie del dibujo, las flechas que la unían a otras se cortan. Puedes ver quién se queda sin alimento y quién tiene menos depredadores. Así se estima qué especies son más vulnerables.",
      "Algunos contaminantes, como ciertos pesticidas y metales como el mercurio, no se eliminan fácilmente del cuerpo. Cada organismo guarda lo que come. Un animal que se come a muchos organismos pequeños acumula cada vez más. A esto se le llama bioacumulación; cuando además aumenta de un nivel al siguiente de la cadena, el efecto es mayor en los depredadores finales. Por eso los depredadores finales pueden tener concentraciones mucho más altas que el agua o las plantas.",
      "Un modelo con números simulados puede mostrarlo: agua 1 unidad, fitoplancton 10, pez pequeño 100 y ave marina 1.000. Es solo un modelo: los valores reales cambian según el contaminante y el lugar. El modelo ayuda a explicar la idea, pero no entrega las concentraciones reales de un río o una costa.",
  ],
  vocab=[("bioacumulación", "aumento de una sustancia en el cuerpo de un organismo a lo largo del tiempo"), ("pesticida", "sustancia para eliminar plagas"), ("mercurio", "metal que puede dañar a los seres vivos si se acumula"), ("depredador final", "animal que ocupa el último nivel de una cadena"), ("vulnerable", "que puede ser dañado con facilidad")],
  worked=[
      ("Seguir la acumulación", "En un modelo simulado el agua tiene 1 unidad de contaminante, el plancton 10, el pez 100 y el ave 1.000. ¿En qué nivel hay más?", ["Comparo las cifras: 1, 10, 100 y 1.000.", "La mayor es 1.000.", "Corresponde al ave."], "En el ave, el depredador final"),
      ("Cortar una flecha", "En pasto → conejo → zorro, quitas al conejo del modelo. ¿Qué flechas se cortan y qué consecuencia hay?", ["Se corta pasto → conejo.", "Se corta conejo → zorro.", "El zorro pierde alimento."], "Se cortan dos flechas y el zorro pierde su alimento"),
  ],
  mistakes=[
      ("Pensar que los contaminantes desaparecen cuando un organismo los come.", "Muchos se quedan en el cuerpo y se acumulan.", "Sigue la cantidad en cada nivel del modelo."),
      ("Creer que el modelo muestra las cifras reales de un río.", "Los números del modelo son solo ejemplos.", "Di que son datos simulados."),
  ],
  rec=[
      ("En la bioacumulación, ¿la sustancia aumenta o disminuye en los depredadores finales?", "Aumenta", "Cada nivel suma lo que come."),
      ("¿Qué animal acumula más en el modelo: el plancton o el ave marina?", "El ave marina", "Está en un nivel más alto."),
      ("Si quitas una especie del modelo, ¿se cortan las flechas que la unían a otras: Sí o No?", "Sí", "Ya no hay relación con esa especie."),
  ],
  und=[
      ("¿Por qué un depredador final puede tener más contaminante que el agua?", "Porque acumula lo que comen todos los niveles anteriores", "Es la bioacumulación."),
      ("En un modelo simulado, el plancton tiene 5 unidades y el pez que lo come 50. ¿Qué indica?", "Que la sustancia se acumula", "El valor aumenta al pasar de nivel."),
      ("¿Por qué las cifras de un modelo simulado no sirven para medir un río real?", "Porque son ejemplos y no mediciones", "Para un río se necesitan datos reales."),
  ],
  app=[
      arith("En un modelo simulado, cada nivel acumula 10 veces más que el anterior. Si el pez tiene 40 unidades, ¿cuántas tiene el ave que se lo come?", "40*10", "Se multiplica por 10 el valor del nivel anterior."),
      ("Cadena: algas → caracol → pato. Si las algas se contaminan con un pesticida, ¿cuál es el orden en que llega al pato?", "Algas, caracol, pato", "Pasa por cada eslabón."),
      arith("Un modelo mostró 3 flechas que llegaban a un ave y se cortaron 2 al quitar especies. ¿Cuántas flechas le quedan?", "3-2", "Se restan las cortadas."),
  ],
  rea=[
      ("Un grupo dice: «El plancton tiene más mercurio acumulado que el ave marina». Usando el modelo de bioacumulación, ¿están en lo correcto? Responde Sí o No.", "No", "El ave acumula más."),
      ("Un modelo tiene 6 especies y 8 flechas. Quitas una especie con 3 flechas. ¿Cuántas flechas quedan?", "5", "8 − 3 = 5."),
  ],
  cha=[
      ("En el modelo simulado, el agua tiene 2 unidades y el ave 2.000. ¿Cuántas veces mayor es la concentración del ave?", "1.000", "2.000 ÷ 2 = 1.000."),
      ("¿Cuál es un límite del modelo con números simulados? A) Los valores no son mediciones reales de un lugar. B) Las flechas tienen punta.", "A", "Los números son ejemplos."),
  ],
  context=[("Dato de ejemplo. Una costa simulada tiene 4 unidades de contaminante en el agua, 40 en el plancton y 400 en un pez. ¿Cuántas unidades más tiene el pez que el plancton?", "360", "400 − 40 = 360.")],
  selfcheck=[("¿Qué es la bioacumulación?", "Que una sustancia se acumula en los organismos", "Aumenta al pasar por los niveles."), ("¿Qué pasa en el modelo si quitas una especie?", "Se cortan las flechas que la unían a otras", "Cambian las relaciones."), ("¿Por qué el modelo tiene límites?", "Porque usa datos simulados", "No son mediciones reales.")],
  open_task=task("Dibuja la cadena fitoplancton → crustáceo → pez → gaviota. Escribe sobre cada organismo estos datos simulados de un contaminante: 5, 50, 500 y 5.000 unidades. Escribe qué muestra el modelo y qué no muestra.", "Cadena dibujada con los valores 5, 50, 500 y 5.000. Muestra que la sustancia aumenta hacia la gaviota. No muestra las concentraciones reales ni todas las especies.", ["cadena bien orientada", "valores en orden creciente", "un límite del modelo"], ["dibujo con números", "frase de límite"], ["invertir la cadena", "olvidar que los datos son simulados"], "Pregunta qué pasaría con la gaviota si el pez estuviera menos contaminado."),
  reinforce="Escribe con tus palabras qué significa bioacumulación.",
  extend="Explica por qué disminuir el contaminante en el agua ayuda a toda la red.")

L(OA3, 4,
  materials="Este cuaderno y lápiz. Las tablas están escritas en los ejercicios.",
  use="Aprenderé a comparar medidas de cuidado de un ecosistema con un criterio. Sirve para decidir qué medida protege mejor una población.",
  prior=["Sé que las actividades humanas pueden afectar las redes alimentarias.", "Sé calcular diferencias y promedios con datos."],
  explain=[
      "Para decidir si una medida de protección funciona, se compara lo que pasa con y sin la medida, usando un criterio. Un criterio común es el tamaño de la población de la especie después de un tiempo. Por ejemplo: una zona con prohibición de pesca temporal (veda) y otra donde se pesca sin límite.",
      "Se registra la población al comienzo y al final en cada zona, y se calcula el cambio. Si en la zona con veda la población aumentó y en la otra disminuyó, los datos apoyan la medida. Para comparar con justicia, ambas zonas deben ser parecidas y observarse durante el mismo tiempo. Si no, la diferencia podría deberse a otra cosa.",
      "Los datos tienen límites. Con pocos años de registro no se puede asegurar qué ocurrirá después. Además, otras causas, como el clima, también influyen. Una conclusión sólida dice qué medida se comparó, con qué criterio y cuál es su límite.",
  ],
  vocab=[("veda", "período en que se prohíbe pescar o cazar para que la población se recupere"), ("área protegida", "zona cuidada por ley para conservar su naturaleza"), ("población inicial", "cantidad de individuos al comienzo del registro"), ("cambio", "diferencia entre el valor final y el inicial"), ("zona de comparación", "zona parecida usada para comparar")],
  worked=[
      ("Calcular el cambio", "En una zona con veda, un pez pasó de 200 a 320 individuos. ¿Cuál fue el cambio?", ["Identifico el valor inicial: 200.", "Identifico el valor final: 320.", "Resto: 320 − 200."], "Aumentó en 120 individuos"),
      ("Comparar dos zonas", "Zona A (veda): de 200 a 320. Zona B (sin veda): de 200 a 150. Según el criterio de tamaño de población, ¿qué zona estuvo mejor?", ["A aumentó 120.", "B disminuyó 50.", "El criterio favorece al que crece."], "La zona A"),
  ],
  mistakes=[
      ("Comparar zonas muy distintas o observadas en tiempos distintos.", "La diferencia puede deberse a eso y no a la medida.", "Compara zonas parecidas y el mismo período."),
      ("Concluir que la medida funciona siempre con un solo año de datos.", "Un año puede ser casualidad.", "Pide registros de varios años."),
  ],
  rec=[
      ("Una veda, ¿permite o prohíbe pescar por un período?", "Prohíbe", "Busca que la población se recupere."),
      ("Si una población pasa de 100 a 130, ¿aumentó o disminuyó?", "Aumentó", "130 es mayor que 100."),
      ("Para comparar, ¿las zonas deben ser parecidas o muy distintas?", "Parecidas", "Así la diferencia se atribuye a la medida."),
  ],
  und=[
      ("¿Qué criterio se usó para decidir si una veda funciona?", "El tamaño de la población después de un tiempo", "Si crece, la medida apoya la recuperación."),
      ("Zona A: de 80 a 110. Zona B: de 80 a 60. ¿Cuál tuvo mejor resultado?", "La zona A", "Su población aumentó."),
      ("¿Por qué se necesita observar el mismo tiempo en ambas zonas?", "Para que la comparación sea justa", "Los tiempos distintos pueden cambiar el resultado."),
  ],
  app=[
      arith("En una zona con veda, una especie pasó de 250 a 400. ¿Cuántos individuos aumentó?", "400-250", "Se resta el valor inicial del final."),
      arith("En una zona sin veda, la misma especie pasó de 250 a 180. ¿Cuántos individuos disminuyó?", "250-180", "Se resta el valor final del inicial."),
      arith("En cuatro años una población aumentó 30, 25, 35 y 30 individuos. ¿Cuál es el aumento promedio por año?", "(30+25+35+30)//4", "Se suma y se divide por los años."),
  ],
  rea=[
      ("Un equipo dice que la veda funciona porque en un año la población subió de 100 a 105. ¿Es suficiente evidencia? Responde Sí o No y explica.", "No; un solo año y un cambio pequeño", "Puede deberse a casualidad."),
      ("Una zona con veda es un estuario cálido y la de comparación es un mar frío y profundo. ¿Es una comparación justa? Responde Sí o No.", "No", "Las zonas son muy distintas."),
  ],
  cha=[
      ("Hay dos medidas. Medida 1: población pasa de 300 a 390. Medida 2: pasa de 300 a 360. Usando el criterio de aumento, ¿cuántos individuos más aumentó la medida 1?", "30", "90 − 60 = 30."),
      ("Marca la mejor conclusión. A) La veda siempre funciona. B) En estas dos zonas y en este período, la veda se relacionó con un aumento de población.", "B", "La B se limita a los datos."),
  ],
  context=[("Dato de ejemplo. Una reserva marina tiene 500 peces y otra zona parecida sin reserva tiene 320. ¿Cuántos peces más hay en la reserva?", "180", "500 − 320 = 180.")],
  selfcheck=[("¿Qué criterio se usó para comparar medidas?", "El tamaño de la población después de un tiempo", "Muestra si la especie se recupera."), ("¿Qué debe cumplir una comparación justa?", "Zonas parecidas y el mismo período", "Así se evita otra explicación."), ("¿Por qué un solo año de datos es débil?", "Puede ser casualidad", "Se necesitan varios registros.")],
  open_task=task("Compara estas dos zonas simuladas durante 5 años: Zona con veda: 300, 330, 360, 390, 420 peces. Zona sin veda: 300, 280, 260, 240, 220 peces. Calcula el cambio total en cada zona, indica cuál tuvo mejor resultado con el criterio y escribe un límite de estos datos.", "Con veda: +120. Sin veda: −80. La zona con veda tuvo mejor resultado. Límite: no sabemos si el clima o el alimento influyeron.", ["calcula cambio de ambas zonas", "usa el criterio", "escribe un límite"], ["cálculos escritos", "conclusión"], ["no restar bien", "olvidar el límite"], "Pregunta qué datos de años anteriores ayudarían."),
  reinforce="Calcula el cambio de una población que pasa de 90 a 135.",
  extend="Explica por qué se compara con una zona parecida.")

L(OA3, 5,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a explicar los efectos de la actividad humana con evidencia y límites, y a proponer medidas. Sirve para argumentar cómo cuidar los ecosistemas.",
  prior=["Sé que las actividades humanas afectan las redes alimentarias.", "Sé comparar medidas con un criterio."],
  explain=[
      "Una explicación sólida sobre el efecto de una actividad humana tiene cuatro partes: el dato observado, la relación en la red, la conclusión y el límite. Por ejemplo: «La captura bajó 400 toneladas (dato). Los lobos marinos comen ese pez (relación). Es probable que los lobos tengan menos alimento (conclusión). No sabemos si hubo otras causas (límite)».",
      "Las medidas para disminuir los efectos se relacionan con la causa. Contra la sobrepesca: vedas y cuotas. Contra la pérdida de hábitat: áreas protegidas y reforestación con especies nativas. Contra las especies introducidas: controlarlas y no liberar mascotas. Contra los contaminantes: reducir plásticos, tratar aguas y no botar basura. Cada persona puede reciclar, ahorrar agua y elegir productos de pesca responsable.",
      "Una buena propuesta dice quién actúa, qué hace y cómo se sabrá si funcionó, por ejemplo contando la población después de un año. También reconoce un límite: una medida sola rara vez resuelve todo, y los resultados tardan en notarse.",
  ],
  vocab=[("cuota de pesca", "cantidad máxima que se puede pescar"), ("reforestación", "plantar árboles para recuperar un bosque"), ("hábitat", "lugar donde vive un ser vivo"), ("propuesta", "medida que se sugiere para resolver un problema"), ("indicador", "dato que se mide para saber si algo mejoró")],
  worked=[
      ("Armar una explicación", "Dato: bajaron 300 aves en un humedal drenado. Relación: las aves viven y se alimentan allí. Escribe la conclusión con un «probablemente».", ["Uso el dato y la relación.", "Si el humedal se secó, las aves perdieron hábitat.", "Escribo con «probablemente»."], "Probablemente bajaron porque perdieron su hábitat y su alimento"),
      ("Elegir una medida", "El problema es que un río recibe mucho plástico. ¿Qué medida se relaciona mejor: reducir plásticos o aumentar la pesca?", ["Busco la causa: el plástico.", "Reducir plásticos ataca la causa.", "Aumentar la pesca no la resuelve."], "Reducir plásticos"),
  ],
  mistakes=[
      ("Proponer una medida que no tiene relación con la causa.", "No resuelve el problema observado.", "Relaciona la medida con la causa."),
      ("Prometer que una medida resolverá todo.", "Los ecosistemas responden despacio y hay otras causas.", "Menciona un límite y cómo medirás el resultado."),
  ],
  rec=[
      ("Plantar árboles para recuperar un bosque se llama ______. Completa con «reforestación» o «tala».", "Reforestación", "Es sembrar nuevos árboles."),
      ("Contra la sobrepesca, ¿sirve una cuota de pesca o botar basura al mar?", "Una cuota de pesca", "Limita cuánto se captura."),
      ("Para saber si una medida funcionó, ¿se cuenta la población o se cuenta la opinión?", "La población", "Es un indicador medible."),
  ],
  und=[
      ("¿Qué partes tiene una explicación sólida? Elige la lista correcta. A) Dato, relación, conclusión y límite. B) Opinión, deseo y promesa.", "A", "Las cuatro partes la hacen verificable."),
      ("El problema son especies introducidas que dañan a las nativas. ¿Qué medida se relaciona?", "Controlarlas y no liberar mascotas", "Ataca la causa."),
      ("¿Por qué una buena propuesta incluye un indicador?", "Para saber si funcionó", "Permite comprobar con datos."),
  ],
  app=[
      arith("Una cuota permite pescar 600 toneladas al año. Si en 3 años se pescó el máximo cada año, ¿cuántas toneladas fueron?", "600*3", "Se multiplica la cuota por los años."),
      arith("Una escuela planta 45 árboles nativos por curso en 6 cursos. ¿Cuántos árboles plantan en total?", "45*6", "Se multiplican árboles por cursos."),
      ("Empareja el problema con la medida. Problema: pérdida de bosque por tala. ¿Qué medida: reforestación o cuota de pesca?", "Reforestación", "Repone árboles y hábitat."),
  ],
  rea=[
      ("Dos compañeros proponen resolver la contaminación de un río. Uno dice «reducir plásticos y tratar aguas» y otro dice «pescar más». ¿Cuál propuesta se relaciona con la causa?", "La primera", "Disminuye la entrada del contaminante."),
      ("Una explicación dice: «Baja la población de lobos por culpa de la pesca». ¿Qué parte le falta para ser sólida? Responde con una palabra.", "Límite", "Falta indicar qué no se sabe."),
  ],
  cha=[
      ("Un pueblo propone una veda de 2 años para recuperar un pez. Si el pez aumenta de 400 a 700, ¿cuánto aumentó? Responde con el número.", "300", "700 − 400 = 300."),
      ("Si durante una veda un pez aumentó de 400 a 700, ¿qué dato falta para asegurar que la veda fue la causa? A) Cómo cambió una zona parecida sin veda. B) El color del pez.", "A", "Sirve para comparar con y sin la medida."),
  ],
  context=[("Dato de ejemplo. Un municipio ahorró 120 bolsas plásticas al día durante 30 días en un mercado. ¿Cuántas bolsas se evitaron?", "3.600", "120 × 30 = 3.600.")],
  selfcheck=[("¿Qué partes tiene una explicación sólida?", "Dato, relación, conclusión y límite", "Son cuatro partes que se pueden comprobar."), ("¿Cómo se relaciona la medida con el problema?", "Ataca la causa observada", "Así puede funcionar."), ("¿Cómo se sabrá si funcionó?", "Midiendo un indicador, por ejemplo la población", "Se necesitan datos.")],
  open_task=task("Un humedal tenía 200 aves y hoy tiene 90 porque se vertió basura y se secó una parte. Escribe una explicación con cuatro partes (dato, relación, conclusión y límite) y una propuesta con dos medidas y un indicador.", "Dato: bajaron 110 aves. Relación: las aves usan el humedal para vivir y alimentarse. Conclusión: probablemente perdieron hábitat. Límite: no sabemos si influyó el clima. Propuesta: limpiar el humedal y evitar el drenaje; indicador: contar aves cada mes.", ["cuatro partes presentes", "dos medidas relacionadas con la causa", "un indicador"], ["texto de 6 a 8 líneas"], ["propuestas sin relación", "olvidar el límite"], "Pregunta cómo se enterarían de si las medidas funcionaron."),
  reinforce="Escribe una medida que puedas hacer tú o tu curso para cuidar un ecosistema.",
  extend="Explica por qué una medida sola rara vez resuelve un problema ambiental.")

# ---------------------------------------------------------------- OA 04
L(OA4, 1,
  materials="Este cuaderno y lápiz. No se necesitan imágenes: las estructuras se describen con palabras.",
  use="Aprenderé los nombres y funciones de las principales estructuras del sistema reproductor femenino y masculino. Sirve para entender cómo se originan nuevas personas.",
  prior=["Sé que el cuerpo está organizado en órganos y sistemas.", "Sé que una observación es lo que se ve o se lee en un esquema."],
  explain=[
      "El sistema reproductor permite que los seres humanos tengan hijos. Se forma con órganos que producen células reproductoras, llamadas gametos. En el sistema femenino los ovarios producen óvulos y hormonas. Las trompas de Falopio conducen el óvulo y, si hay fecundación, ocurre allí. El útero es un órgano musculoso donde se desarrolla el bebé. La vagina es el canal que une el útero con el exterior.",
      "En el sistema masculino los testículos producen espermatozoides y la hormona testosterona. Están dentro del escroto, una bolsa de piel. El epidídimo guarda los espermatozoides mientras maduran. Los conductos deferentes los llevan hacia la uretra. Las vesículas seminales y la próstata agregan líquidos que forman el semen. La uretra lleva el semen al exterior a través del pene; también lleva la orina, pero no al mismo tiempo.",
      "Al leer un esquema, una observación es «el ovario está unido a la trompa». Una interpretación es «este órgano es más importante que el otro». Ningún órgano es más importante: todos cumplen una función. Estos temas se conversan con respeto, y si tienes dudas puedes preguntar a una persona adulta de confianza.",
  ],
  vocab=[("gameto", "célula reproductora: óvulo o espermatozoide"), ("ovario", "órgano que produce óvulos y hormonas"), ("testículo", "órgano que produce espermatozoides y testosterona"), ("útero", "órgano muscular donde se desarrolla el bebé"), ("fecundación", "unión de un óvulo y un espermatozoide")],
  worked=[
      ("Relacionar estructura y función", "¿Qué estructura produce los espermatozoides y cuál produce los óvulos?", ["Recuerdo el sistema masculino: testículos.", "Recuerdo el sistema femenino: ovarios.", "Relaciono cada gameto con su órgano."], "Los espermatozoides se producen en los testículos y los óvulos en los ovarios"),
      ("Observación o interpretación", "Dos frases sobre un esquema: (1) «Las trompas de Falopio están unidas al útero». (2) «El útero es el órgano más importante». ¿Cuál es una observación?", ["Pregunto qué frase se ve en el esquema.", "La frase 1 describe una unión.", "La frase 2 opina."], "La frase 1"),
  ],
  mistakes=[
      ("Confundir el útero con la vagina.", "El útero es donde se desarrolla el bebé; la vagina es el canal que va al exterior.", "Recuerda: útero = desarrollo; vagina = canal."),
      ("Decir que la uretra solo existe en hombres.", "La uretra existe en ambos sexos, pero en el sistema masculino además conduce el semen.", "Describe la función según el sistema."),
  ],
  rec=[
      ("¿Qué órgano produce los óvulos: el ovario o el testículo?", "El ovario", "Los ovarios producen óvulos."),
      ("¿Dónde se desarrolla el bebé: en el útero o en la trompa de Falopio?", "En el útero", "El útero es un órgano muscular."),
      ("¿Los espermatozoides se producen en los testículos o en la próstata?", "En los testículos", "La próstata aporta líquidos."),
  ],
  und=[
      ("¿Qué función tienen las trompas de Falopio?", "Conducen el óvulo y allí puede ocurrir la fecundación", "Une los ovarios con el útero."),
      ("¿Para qué sirven las vesículas seminales y la próstata?", "Agregan líquidos que forman el semen", "Ayudan a nutrir y transportar los espermatozoides."),
      ("¿Cuál es una interpretación? A) Los testículos están dentro del escroto. B) Los testículos son el órgano más valioso.", "B", "La B es una opinión."),
  ],
  app=[
      ("Une cada estructura con su sistema. Estructuras: ovario, testículo, útero, próstata. ¿Cuántas pertenecen al sistema femenino?", "2", "Son ovario y útero."),
      ("Ordena de arriba hacia abajo en el sistema femenino: vagina, ovario, útero, trompa de Falopio.", "Ovario, trompa de Falopio, útero, vagina", "Sigue el camino del óvulo."),
      arith("Un libro de ejemplo describe 6 estructuras femeninas y 7 masculinas. ¿Cuántas estructuras describe en total?", "6+7", "Se suman ambas listas."),
  ],
  rea=[
      ("Una compañera dice que los testículos producen óvulos. ¿Es correcto? Responde Sí o No y explica.", "No; producen espermatozoides", "Los óvulos se producen en los ovarios."),
      ("Un esquema muestra la trompa de Falopio sin conexión con el útero. ¿Qué tiene de incorrecto?", "La trompa debe estar unida al útero", "La trompa lleva el óvulo hacia el útero."),
  ],
  cha=[
      ("Una persona dice «la fecundación ocurre en el útero». Con lo que aprendiste, ¿dónde ocurre habitualmente?", "En la trompa de Falopio", "Allí se encuentran el óvulo y el espermatozoide."),
      ("Un compañero dice que el semen es solo espermatozoides. Corrígelo con una frase.", "Contiene espermatozoides y líquidos de las vesículas seminales y la próstata", "Los líquidos forman gran parte del semen."),
  ],
  context=[("Un grupo de estudio hace dos listas: la femenina tiene ovarios, trompas, útero y vagina; la masculina tiene testículos, epidídimo, conductos deferentes, vesículas seminales, próstata y uretra. ¿Cuántas estructuras tiene la lista masculina?", "6", "Se cuentan las seis estructuras.")],
  selfcheck=[("¿Qué producen los ovarios?", "Óvulos y hormonas", "Son gametos y mensajeros químicos."), ("¿Qué producen los testículos?", "Espermatozoides y testosterona", "Son gametos y una hormona."), ("¿Qué es la fecundación?", "La unión de un óvulo y un espermatozoide", "Da origen a una nueva célula.")],
  open_task=task("Dibuja dos esquemas muy simples, uno del sistema reproductor femenino y otro del masculino, y rotula las estructuras de esta clase (ovario, trompa de Falopio, útero, vagina; testículo, epidídimo, conducto deferente, uretra). Escribe al lado una frase con la función de cada una. Recuerda que puedes consultar a un adulto de confianza.", "Esquema femenino: ovario (produce óvulos), trompa (conduce el óvulo), útero (desarrolla al bebé), vagina (canal). Esquema masculino: testículo (produce espermatozoides), epidídimo (los guarda), conducto deferente (los lleva), uretra (los lleva al exterior).", ["rotula bien las estructuras", "indica una función correcta de cada una", "mantiene un lenguaje respetuoso"], ["dos dibujos rotulados", "frases de funciones"], ["intercambiar útero y vagina", "olvidar la función"], "Pregunta qué estructura no tiene equivalente en el otro sistema y por qué."),
  reinforce="Escribe la función de ovario, útero, testículo y uretra.",
  extend="Explica con tus palabras cómo se relacionan los gametos con la fecundación.")

L(OA4, 2,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a formular preguntas y predicciones sobre las funciones del sistema reproductor. Sirve para razonar con datos y con lo que ya sé de cada estructura.",
  prior=["Conozco las principales estructuras reproductoras femeninas y masculinas.", "Sé que una predicción lleva una razón."],
  explain=[
      "Los gametos son muy distintos. El óvulo es la célula más grande del cuerpo humano y no se mueve por sí sola. Desde la pubertad, normalmente se libera un óvulo por ciclo, de uno de los dos ovarios. El ciclo dura cerca de 28 días, aunque varía de una persona a otra. El espermatozoide es muy pequeño y se mueve gracias a su cola. Un testículo produce millones de ellos de manera continua.",
      "Se pueden hacer preguntas comprobables con datos. Por ejemplo: «¿Cuántos óvulos se liberan normalmente en 6 ciclos?». Y se pueden hacer predicciones con razón: «Si una trompa de Falopio está cerrada, el óvulo probablemente no se encontrará con espermatozoides por ese lado, porque la trompa es el camino y el sitio de la fecundación».",
      "Otro ejemplo: los testículos están en el escroto, fuera del abdomen, donde la temperatura es un poco menor que en el interior del cuerpo. Se predice que los espermatozoides se producen mejor a esa temperatura algo más baja. Se llega a esa predicción porque la forma y el lugar de una estructura se relacionan con su función.",
  ],
  vocab=[("ciclo", "período que se repite de forma regular"), ("hormona", "mensajero químico del cuerpo"), ("óvulo", "gameto femenino, grande e inmóvil"), ("espermatozoide", "gameto masculino, pequeño y con cola"), ("predicción", "lo que se espera y por qué")],
  worked=[
      ("Contar gametos liberados", "Normalmente se libera un óvulo por ciclo. ¿Cuántos óvulos se habrán liberado en 8 ciclos?", ["Identifico: 1 óvulo por ciclo.", "Multiplico por 8 ciclos.", "1 × 8 = 8."], "8 óvulos"),
      ("Predecir con razón", "Si una trompa de Falopio está cerrada, ¿qué se predice sobre el encuentro del óvulo con un espermatozoide por ese lado y por qué?", ["Recuerdo que la trompa es el camino del óvulo.", "Sin camino, no hay encuentro.", "Escribo la razón."], "Probablemente no se encuentren, porque la trompa es el camino y el lugar de fecundación"),
  ],
  mistakes=[
      ("Pensar que el óvulo se mueve con una cola.", "La cola la tiene el espermatozoide; el óvulo no se mueve por sí solo.", "Relaciona cola con espermatozoide."),
      ("Afirmar una predicción sin dar razón.", "No se puede comprobar ni aprender de ella.", "Agrega «porque» y usa la función de la estructura."),
  ],
  rec=[
      ("¿Qué gameto tiene cola: el óvulo o el espermatozoide?", "El espermatozoide", "La cola le permite moverse."),
      ("¿Qué gameto es la célula más grande del cuerpo: el óvulo o el espermatozoide?", "El óvulo", "Es mucho mayor que un espermatozoide."),
      ("Una hormona, ¿es un mensajero químico o una célula?", "Un mensajero químico", "Viaja por la sangre."),
  ],
  und=[
      ("¿Cuál pregunta es comprobable? A) ¿Cuántos días dura cada ciclo de una persona, anotándolos en un calendario durante 6 meses? B) ¿Cuál gameto es más bonito?", "A", "Se responde anotando y contando días; la belleza es un gusto."),
      ("¿Por qué se predice que los testículos funcionan mejor en el escroto?", "Porque allí la temperatura es algo menor", "La función depende de la temperatura."),
      ("¿Qué estructura es el camino del óvulo hacia el útero?", "La trompa de Falopio", "Conduce el óvulo hasta el útero."),
  ],
  app=[
      arith("Un ciclo dura 28 días. ¿Cuántos días hay en 6 ciclos?", "28*6", "Se multiplican los días por los ciclos."),
      arith("Un ciclo dura 28 días. ¿Cuántos ciclos completos hay en 112 días?", "112//28", "Se divide el total de días por la duración de un ciclo."),
      ("Una predicción dice: «Los espermatozoides son pequeños y con cola porque deben moverse». ¿Qué parte es la razón?", "Porque deben moverse", "La razón va después de «porque»."),
  ],
  rea=[
      ("Un compañero predice que el óvulo llegará solo al útero «volando». ¿Qué error tiene? Responde con una frase.", "El óvulo no se mueve solo; las trompas lo conducen", "El óvulo no tiene cola."),
      ("Otra persona predice que la temperatura no importa para producir espermatozoides. ¿Es compatible con lo aprendido? Responde Sí o No.", "No", "Los testículos están en el escroto, donde es algo más fresco."),
  ],
  cha=[
      ("El espermatozoide tiene cola y el óvulo no. Con la relación entre forma y función, ¿qué predices para el óvulo: nada solo o es conducido por la trompa?", "Es conducido por la trompa", "No tiene cola para moverse por sí solo."),
      ("Piensa en la cantidad que se produce o libera: ¿habrá más espermatozoides o más óvulos en un mes? Responde una palabra.", "Espermatozoides", "Se producen millones de manera continua, mientras normalmente se libera un óvulo por ciclo."),
  ],
  context=[("Una clase calcula cuántos días hay en 10 ciclos de 28 días cada uno. ¿Cuántos días son?", "280", "28 × 10 = 280.")],
  selfcheck=[("¿Qué diferencia hay entre óvulo y espermatozoide?", "El óvulo es grande e inmóvil y el espermatozoide es pequeño y con cola", "Se relacionan con sus funciones."), ("¿Por qué los testículos están en el escroto?", "Allí la temperatura es algo menor", "Favorece la producción de espermatozoides."), ("¿Qué lleva una buena predicción?", "Lo que ocurrirá y su razón", "Así se puede comprobar.")],
  open_task=task("Escribe una pregunta comprobable y una predicción con razón que usen los datos de la clase: ciclo de 28 días, un óvulo por ciclo, millones de espermatozoides, testículos en el escroto. Luego calcula cuántos óvulos se liberan en 9 ciclos.", "Pregunta: ¿cuántos óvulos se liberan normalmente en 9 ciclos? Predicción: los espermatozoides se producen en mayor cantidad porque los testículos producen de forma continua. Cálculo: 9 óvulos.", ["pregunta con cálculo", "predicción con razón", "cálculo correcto"], ["tres frases escritas"], ["no dar razón", "equivocar el cálculo"], "Pregunta qué dato necesitaría para comprobar su predicción."),
  reinforce="Calcula cuántos días hay en 4 ciclos de 28 días.",
  extend="Explica por qué la forma de una célula se relaciona con su función.")

L(OA4, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a representar el recorrido de los gametos con un modelo. Sirve para explicar cómo se relacionan las estructuras del sistema reproductor.",
  prior=["Sé qué hace cada estructura.", "Sé que un modelo simplifica y tiene límites."],
  explain=[
      "Un modelo de recorrido muestra el camino de los gametos por flechas. En el sistema femenino, el óvulo sale de un ovario, entra a la trompa de Falopio, y si no se une a un espermatozoide continúa hacia el útero. Si hay fecundación, el óvulo fecundado llega al útero y se desarrolla allí.",
      "En el sistema masculino, los espermatozoides se producen en los testículos, pasan al epidídimo, siguen por los conductos deferentes, reciben líquidos de las vesículas seminales y la próstata, y salen por la uretra mezclados con esos líquidos como semen. Un modelo con flechas ordenadas ayuda a no perder ningún paso.",
      "Todo modelo tiene límites. El esquema de flechas no muestra tamaños reales, no muestra las hormonas que regulan el proceso ni cuánto tiempo toma cada paso. Un buen modelo indica lo que muestra y lo que no.",
  ],
  vocab=[("recorrido", "camino que sigue algo paso a paso"), ("óvulo fecundado", "óvulo que se unió con un espermatozoide"), ("semen", "líquido con espermatozoides y secreciones"), ("flecha", "símbolo que indica el sentido del recorrido"), ("límite del modelo", "algo que el modelo no muestra")],
  worked=[
      ("Ordenar el recorrido femenino", "Ordena el recorrido del óvulo: útero, ovario, trompa de Falopio.", ["Parte en el ovario, donde se produce.", "Sigue por la trompa de Falopio.", "Llega al útero."], "Ovario → trompa de Falopio → útero"),
      ("Ordenar el recorrido masculino", "Ordena el recorrido de los espermatozoides: uretra, epidídimo, testículo, conducto deferente.", ["Se producen en el testículo.", "Pasan al epidídimo y al conducto deferente.", "Salen por la uretra."], "Testículo → epidídimo → conducto deferente → uretra"),
  ],
  mistakes=[
      ("Saltarse el epidídimo o la trompa en el recorrido.", "Son pasos del camino de los gametos.", "Repasa los pasos en orden con una flecha para cada uno."),
      ("Pensar que el modelo muestra el tamaño real de los órganos.", "Los esquemas simplifican y cambian los tamaños.", "Escribe que el modelo no muestra tamaños reales."),
  ],
  rec=[
      ("En el recorrido femenino, ¿qué estructura viene después del ovario?", "La trompa de Falopio", "El óvulo pasa a ella."),
      ("En el recorrido masculino, ¿dónde se producen los espermatozoides?", "En los testículos", "Es el inicio del recorrido."),
      ("¿Las flechas de un recorrido indican el sentido o el color?", "El sentido", "Muestran el camino."),
  ],
  und=[
      ("¿Qué estructura viene justo antes de la uretra en el recorrido masculino?", "El conducto deferente", "Lleva los espermatozoides a la uretra."),
      ("Si el óvulo es fecundado, ¿hacia dónde sigue su recorrido?", "Hacia el útero", "Allí se desarrolla."),
      ("¿Qué no muestra un modelo de flechas simples?", "Los tamaños reales ni el tiempo de cada paso", "Es un límite del modelo."),
  ],
  app=[
      arith("Un modelo masculino tiene 4 estructuras en el recorrido (testículo, epidídimo, conducto deferente y uretra) y un modelo femenino tiene 3. ¿Cuántas estructuras de recorrido hay en total?", "4+3", "Se suman ambos recorridos."),
      ("Ordena las letras según el camino femenino: A útero, B ovario, C trompa de Falopio.", "B, C, A", "Ovario, trompa, útero."),
      ("En un modelo con flechas, la flecha del recorrido masculino apunta desde la uretra al testículo. ¿Está correcta? Responde Sí o No.", "No", "Debe ir del testículo a la uretra."),
  ],
  rea=[
      ("Una compañera dibujó ovario → útero → trompa. ¿Qué error tiene?", "La trompa debe ir entre el ovario y el útero", "El orden correcto es ovario, trompa, útero."),
      ("En un modelo masculino faltan los líquidos que agregan la próstata y las vesículas seminales. ¿Eso es un límite del modelo? Responde Sí o No.", "Sí", "No muestra todo lo que ocurre."),
  ],
  cha=[
      ("¿Qué dos estructuras agregan líquidos al semen durante el recorrido? Escribe sus nombres.", "Las vesículas seminales y la próstata", "Producen líquidos que se mezclan con los espermatozoides."),
      ("¿Cuántas flechas necesita un recorrido femenino de tres estructuras ordenadas?", "2", "Hay una flecha entre cada par."),
  ],
  context=[("Un esquema de clase tiene 3 flechas en el recorrido masculino y 2 en el femenino. ¿Cuántas flechas más tiene el masculino?", "1", "3 − 2 = 1.")],
  selfcheck=[("¿Cuál es el recorrido del óvulo?", "Ovario, trompa de Falopio y útero", "Es el orden de las estructuras."), ("¿Cuál es el recorrido de los espermatozoides?", "Testículo, epidídimo, conducto deferente y uretra", "Con los líquidos se forma el semen."), ("¿Qué límite tiene un esquema de flechas?", "No muestra tamaños reales ni tiempo", "Solo simplifica la realidad.")],
  open_task=task("Dibuja los dos recorridos con flechas. Femenino: ovario, trompa de Falopio, útero. Masculino: testículo, epidídimo, conducto deferente, uretra. Escribe debajo qué muestra tu modelo y un límite.", "Femenino: ovario → trompa → útero. Masculino: testículo → epidídimo → conducto deferente → uretra. Muestra el orden. Límite: no muestra tamaños reales.", ["dos recorridos en orden", "flechas bien orientadas", "un límite"], ["dibujo de flechas", "frase"], ["alterar el orden", "olvidar el límite"], "Pregunta qué estructura falta en el recorrido masculino para formar el semen."),
  reinforce="Escribe en orden las estructuras del recorrido femenino.",
  extend="Explica por qué el modelo de flechas no muestra las hormonas.")

L(OA4, 4,
  materials="Este cuaderno y lápiz. La tabla está escrita en el ejercicio.",
  use="Aprenderé a comparar los sistemas reproductores femenino y masculino con un criterio. Sirve para organizar lo que sé y ver semejanzas y diferencias.",
  prior=["Conozco las estructuras de ambos sistemas.", "Sé hacer un cuadro comparativo."],
  explain=[
      "Para comparar los dos sistemas se usan criterios claros. Un criterio es qué gameto produce cada uno. Otro es qué estructuras conducen los gametos. Otro es dónde ocurre la fecundación o el desarrollo. Con una tabla se ordena la información. Por ejemplo: en cuanto a producción de gametos, el ovario produce óvulos y el testículo produce espermatozoides.",
      "Hay semejanzas: ambos sistemas producen gametos y hormonas, y ambos tienen estructuras que conducen los gametos. También hay diferencias: solo el sistema femenino tiene un órgano donde se desarrolla el bebé, el útero, y solo el masculino tiene glándulas que agregan líquidos al semen.",
      "Al comparar, no se dice que un sistema es mejor que otro. Se dice cómo cumplen funciones distintas que se complementan para que pueda haber fecundación. Una buena tabla indica el criterio de cada fila y la respuesta de cada sistema.",
  ],
  vocab=[("criterio", "regla para comparar"), ("semejanza", "característica que es igual en dos cosas"), ("diferencia", "característica que cambia"), ("complementarse", "completarse una cosa con otra"), ("glándula", "órgano que produce y libera una sustancia")],
  worked=[
      ("Completar una tabla", "Criterio: gameto que produce. ¿Qué escribes para el sistema femenino y para el masculino?", ["Recuerdo que el ovario produce óvulos.", "El testículo produce espermatozoides.", "Escribo ambos."], "Femenino: óvulos. Masculino: espermatozoides"),
      ("Semejanza o diferencia", "Ambos sistemas producen hormonas. ¿Es una semejanza o una diferencia?", ["Veo que ocurre en los dos.", "Entonces es igual en ambos.", "Es una semejanza."], "Una semejanza"),
  ],
  mistakes=[
      ("Decir que un sistema es más importante que el otro.", "Cumplen funciones distintas y se complementan.", "Compara con un criterio, sin juzgar valor."),
      ("Mezclar dos criterios en una misma fila de la tabla.", "La tabla se vuelve confusa.", "Usa un criterio por fila."),
  ],
  rec=[
      ("¿Ambos sistemas producen gametos: Sí o No?", "Sí", "Óvulos y espermatozoides."),
      ("¿Qué sistema tiene útero?", "El femenino", "Es donde se desarrolla el bebé."),
      ("¿Qué sistema tiene próstata?", "El masculino", "Agrega líquidos al semen."),
  ],
  und=[
      ("¿Cuál es una diferencia entre los sistemas? A) Solo uno produce óvulos. B) Ambos producen hormonas.", "A", "B es una semejanza."),
      ("¿Cuál es un criterio para comparar? A) Qué gameto produce. B) Cuál tiene más color.", "A", "El color no es un criterio útil."),
      ("¿Qué estructura conduce los gametos masculinos hacia la uretra?", "El conducto deferente", "Es el tubo que los lleva."),
  ],
  app=[
      ("Tabla simulada: femenino, estructuras de conducción: 2 (trompas); masculino, 2 (conductos deferentes). ¿Cuántas estructuras de conducción hay en total entre ambos?", "4", "2 + 2 = 4."),
      ("¿Cuántas semejanzas hay en esta lista? 1) Producen gametos. 2) Producen hormonas. 3) Solo uno tiene útero. 4) Ambos tienen estructuras que conducen gametos.", "3", "Las frases 1, 2 y 4 son semejanzas."),
      arith("Un cuadro compara 5 criterios. Ambos sistemas coinciden en 2 de ellos. ¿En cuántos criterios son distintos?", "5-2", "Se restan los criterios iguales del total."),
  ],
  rea=[
      ("Alguien escribe «el sistema masculino es mejor porque produce millones de gametos». ¿Qué error tiene? Responde con una frase.", "Juzga valor y no usa un criterio de función", "Comparar no es decir cuál es mejor."),
      ("Una fila de la tabla dice: «Dónde ocurre la fecundación: trompa de Falopio». ¿A qué sistema corresponde?", "Al femenino", "La trompa es parte del sistema femenino."),
  ],
  cha=[
      ("Completa la fila del criterio «hormonas que produce el órgano que fabrica gametos»: ovario y testículo. Escribe cuál produce testosterona.", "El testículo", "El ovario produce otras hormonas."),
      ("¿Por qué ambos sistemas se complementan? Responde con una frase.", "Porque cada uno aporta un gameto para la fecundación", "El óvulo y el espermatozoide se unen."),
  ],
  context=[("En una tabla de 6 filas, un curso completó 4 filas correctas. ¿Cuántas filas faltan?", "2", "6 − 4 = 2.")],
  selfcheck=[("¿Qué es una semejanza?", "Una característica igual en ambos", "Se encuentra en los dos."), ("¿Qué es una diferencia?", "Una característica que cambia entre ambos", "Solo está en uno."), ("¿Por qué no se dice que un sistema es mejor?", "Porque cumplen funciones distintas que se complementan", "Comparar no es juzgar valor.")],
  open_task=task("Completa una tabla de tres filas con estos criterios: gameto que produce, estructura donde se desarrolla el bebé y estructuras que conducen los gametos. Escribe la respuesta del sistema femenino y del masculino. Después escribe una semejanza.", "Gameto: óvulo / espermatozoide. Desarrollo del bebé: útero / no corresponde. Conducción: trompas / conductos deferentes y uretra. Semejanza: ambos producen hormonas.", ["tres filas completas", "una semejanza", "criterios separados"], ["tabla escrita"], ["mezclar criterios", "juzgar cuál es mejor"], "Pregunta qué fila fue más fácil de completar y por qué."),
  reinforce="Escribe una semejanza y una diferencia entre los sistemas reproductores.",
  extend="Explica cómo se complementan los dos sistemas en la fecundación.")

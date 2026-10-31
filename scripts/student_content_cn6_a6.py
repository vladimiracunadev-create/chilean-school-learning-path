"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 11 (recursos energéticos renovables y no renovables, uso responsable)."""
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


OA11 = "CN06 OA 11"

L(OA11, 1,
  materials="Este cuaderno y lápiz. Los datos de los recursos están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé a clasificar los recursos energéticos en no renovables y renovables y a separar lo medido de lo supuesto. Sirve para entender por qué algunos recursos se pueden agotar.",
  prior=["Sé que la energía viene de varias fuentes y que muchas vienen del Sol.", "Sé que una observación se mide o se cuenta."],
  explain=[
      "Un recurso energético es algo de la naturaleza que usamos para obtener energía. Los recursos no renovables se forman en millones de años y se agotan cuando se usan más rápido de lo que se forman. Son el petróleo, el gas natural y el carbón mineral, llamados combustibles fósiles, y el uranio, que se usa en centrales nucleares.",
      "Los recursos renovables se reponen en un tiempo corto o no se agotan al usarlos. Son la energía solar, el viento, el agua de los ríos, el calor del interior de la Tierra (geotérmica) y las mareas. Chile tiene desierto con mucha radiación solar, zonas ventosas y ríos, por eso estos recursos se usan en el país. La leña es renovable solo si se plantan árboles al mismo ritmo que se cortan.",
      "Para decidir con datos, se comparan la rapidez de uso y la rapidez de reposición. Una observación es «un yacimiento de ejemplo tiene 1.200 barriles y se usan 100 al año». Una interpretación es «el petróleo es fácil de conseguir». Solo la primera se midió. Con datos se puede calcular cuántos años duraría un recurso si se sigue usando igual.",
  ],
  vocab=[("recurso energético", "elemento de la naturaleza usado para obtener energía"), ("no renovable", "recurso que se agota porque se forma muy lentamente"), ("renovable", "recurso que se repone o no se agota al usarlo"), ("combustible fósil", "petróleo, gas natural o carbón mineral"), ("yacimiento", "lugar donde hay mucha cantidad de un recurso")],
  worked=[
      ("Clasificar recursos", "Clasifica: petróleo, viento, carbón mineral, mareas. ¿Cuáles son no renovables?", ["El petróleo y el carbón mineral son combustibles fósiles.", "El viento y las mareas se renuevan.", "Separo en dos grupos."], "No renovables: petróleo y carbón mineral"),
      ("Calcular la duración", "Un yacimiento de ejemplo tiene 1.200 barriles y se extraen 100 al año. ¿Cuántos años duraría?", ["Total: 1.200.", "Uso por año: 100.", "Divido 1.200 ÷ 100."], "12 años"),
  ],
  mistakes=[
      ("Decir que el petróleo es renovable porque «siempre hay».", "Se forma en millones de años y puede agotarse.", "Compara el ritmo de uso con el de formación."),
      ("Pensar que renovable significa que no tiene ningún impacto.", "También pueden tener efectos en el ambiente y en el paisaje.", "Evalúa los impactos con otro criterio."),
  ],
  rec=[
      ("¿El gas natural es renovable o no renovable?", "No renovable", "Es un combustible fósil."),
      ("¿La energía solar se agota al usarla: Sí o No?", "No", "El Sol sigue enviando energía."),
      ("¿El carbón mineral es un combustible fósil: Sí o No?", "Sí", "Se formó hace millones de años."),
  ],
  und=[
      ("¿Cuál es una interpretación? A) Un yacimiento tiene 900 barriles y se usan 100 al año. B) El petróleo es fácil de conseguir.", "B", "No se midió."),
      ("¿Por qué el petróleo es no renovable?", "Porque se forma en millones de años y se agota", "Se usa más rápido de lo que se forma."),
      ("¿Cuál recurso es renovable? A) Uranio. B) Viento.", "B", "El viento se renueva."),
  ],
  app=[
      arith("Un yacimiento de ejemplo tiene 900 barriles y se extraen 100 al año. ¿Cuántos años duraría?", "900//100", "Se divide el total por el uso anual."),
      arith("Otro yacimiento tiene 2.000 barriles y se extraen 250 al año. ¿Cuántos años duraría?", "2000//250", "Se divide el total por el uso anual."),
      ("Cuenta cuántos son renovables: solar, gas natural, viento, uranio, mareas.", "3", "Son solar, viento y mareas."),
  ],
  rea=[
      ("Un estudiante dice: «El carbón mineral es renovable porque hay mucho». ¿Qué falta en su razón?", "Compara cuánto se usa con cuánto se forma", "Que haya mucho no significa que se renueve."),
      ("Alguien dice que, como el viento no se agota, un parque eólico no tiene ningún impacto. ¿Es correcto? Responde Sí o No.", "No", "También puede afectar aves y paisaje."),
  ],
  cha=[
      ("Un recurso de ejemplo se usa a 300 unidades al año, y se forman 20 unidades al año. ¿Es renovable o no renovable en la práctica?", "No renovable", "Se usa más rápido de lo que se forma."),
      ("Un bosque de ejemplo crece 500 árboles al año y se cortan 400. ¿Se puede mantener el uso de la leña? Responde Sí o No.", "Sí", "Se repone más de lo que se corta."),
  ],
  context=[("Dato de ejemplo. Una región usa 450 unidades de carbón al año y tiene 4.500. ¿Cuántos años le quedan?", "10", "4.500 ÷ 450 = 10.")],
  selfcheck=[("¿Qué es un recurso no renovable?", "Uno que se forma muy lento y se agota", "Por ejemplo, el petróleo."), ("¿Qué es un recurso renovable?", "Uno que se repone o no se agota al usarlo", "Por ejemplo, el viento."), ("¿Qué dato permite calcular la duración de un yacimiento?", "El total y cuánto se usa por año", "Se divide uno entre el otro.")],
  open_task=task("Clasifica estos recursos en una tabla de dos columnas (renovables y no renovables): petróleo, solar, gas natural, viento, carbón mineral, mareas, geotérmica, uranio. Después calcula cuántos años dura un yacimiento de ejemplo de 3.600 barriles si se usan 300 al año.", "No renovables: petróleo, gas natural, carbón mineral, uranio. Renovables: solar, viento, mareas, geotérmica. Duración: 3.600 ÷ 300 = 12 años.", ["clasifica los ocho recursos", "calcula la duración", "separa dato de suposición"], ["tabla de dos columnas", "cálculo"], ["clasificar mal el uranio", "olvidar dividir"], "Pregunta qué cambiaría si se usaran 600 barriles al año."),
  reinforce="Escribe tres recursos renovables y tres no renovables.",
  extend="Explica por qué la leña puede ser renovable o no renovable según cómo se use.")

L(OA11, 2,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a formular preguntas y predicciones sobre el uso de la energía y los recursos. Sirve para anticipar qué pasa si aumenta el consumo o si cambia el clima.",
  prior=["Sé clasificar recursos renovables y no renovables.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una pregunta comprobable se responde con datos, por ejemplo: «¿Cuántos años durará un yacimiento de 2.000 barriles si el consumo sube de 100 a 200 barriles al año?». Se responde calculando. Una pregunta como «¿Qué energía es más linda?» depende de gustos.",
      "Una predicción dice qué ocurrirá y por qué. Si un recurso no renovable se usa al doble de velocidad, probablemente se agote en la mitad del tiempo, porque se gasta más rápido. En energía solar, un panel produce menos en un día nublado, porque llega menos luz. Una predicción prudente usa «probablemente».",
      "Para comprobar se comparan los datos con lo esperado. Por ejemplo, un panel de ejemplo produce 10 unidades en un día soleado y 4 en uno nublado. La predicción de que produce menos con nubes se cumple. Pero los datos de unos pocos días no dicen cómo será todo el año. Esa es una limitación.",
  ],
  vocab=[("consumo", "cantidad de energía que se usa"), ("producción", "cantidad de energía que se obtiene"), ("nublado", "con nubes que tapan el Sol"), ("predicción prudente", "predicción que reconoce que puede haber otros factores"), ("limitación", "lo que los datos no permiten afirmar")],
  worked=[
      ("Predecir la duración", "Un yacimiento de 2.000 barriles dura 20 años a 100 barriles por año. Si el consumo sube a 200 por año, ¿qué predices que pasará con la duración?", ["Si se gasta el doble por año, dura la mitad.", "Calculo 2.000 ÷ 200.", "Obtengo 10."], "Durará unos 10 años, la mitad"),
      ("Pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Cuántas unidades produce un panel solar en un día nublado? B) ¿Es lindo un panel solar?", ["Busco la pregunta con un dato.", "En A se mide la producción.", "En B es un gusto."], "A"),
  ],
  mistakes=[
      ("Predecir sin razón: «durará mucho».", "No se puede comprobar ni calcular.", "Usa los datos del consumo y del total."),
      ("Concluir sobre todo el año con tres días de datos.", "Pocos días no representan todas las estaciones.", "Menciona la limitación."),
  ],
  rec=[
      ("Si el consumo de un recurso no renovable sube, ¿su duración aumenta o disminuye?", "Disminuye", "Se agota más rápido."),
      ("Un panel solar en un día nublado, ¿produce más o menos que en uno soleado?", "Menos", "Llega menos luz."),
      ("¿Una predicción lleva una razón: Sí o No?", "Sí", "Dice por qué se espera algo."),
  ],
  und=[
      ("¿Cuál predicción tiene razón? A) Con el doble de consumo se agotará antes, porque se gasta más por año. B) Se agotará antes porque sí.", "A", "La A da el motivo."),
      ("¿Por qué conviene decir «probablemente»?", "Porque pueden influir otros factores", "No se asegura algo que puede variar."),
      ("¿Qué limitación tienen los datos de tres días de un panel solar?", "No representan todo el año", "Cambia con las estaciones."),
  ],
  app=[
      arith("Un yacimiento de 3.000 barriles se usa a 150 al año. ¿Cuántos años dura?", "3000//150", "Se divide el total por el consumo anual."),
      arith("Si el consumo sube a 300 al año, ¿cuántos años dura?", "3000//300", "Se divide el total por el nuevo consumo."),
      ("Un panel produce 10 unidades en un día soleado y 4 en uno nublado. Si hay 3 días soleados y 2 nublados, ¿cuántas unidades produce en total? Responde con el número.", "38", "3 × 10 + 2 × 4 = 38."),
  ],
  rea=[
      ("Un compañero predice que un panel solar producirá lo mismo de noche que de día. ¿Es compatible con lo que se sabe? Responde Sí o No.", "No", "De noche no llega luz del Sol."),
      ("Alguien dice que, si se duplica el consumo, la duración será el doble. ¿Qué error cometió?", "Si el consumo se duplica, la duración se reduce a la mitad", "Se gasta más rápido."),
  ],
  cha=[
      ("Datos de ejemplo: viento flojo, 3 unidades; viento fuerte, 9 unidades. ¿Cuántas veces más produce con viento fuerte?", "3", "9 ÷ 3 = 3."),
      ("Marca la mejor pregunta comprobable. A) ¿Cuántas unidades produce una turbina de viento en un día con viento fuerte? B) ¿Es bonita una turbina?", "A", "Se mide la producción."),
  ],
  context=[("Dato de ejemplo. Un panel produce 12 unidades al día soleado y 5 al día nublado. ¿Cuántas unidades menos produce al día nublado?", "7", "12 − 5 = 7.")],
  selfcheck=[("¿Qué ocurre con la duración si aumenta el consumo?", "Disminuye", "Se gasta más rápido."), ("¿Qué lleva una buena predicción?", "Lo que ocurrirá y su razón", "Así se puede comprobar después."), ("¿Qué limitación tienen pocos días de datos?", "No representan todo el año", "Falta información de otras estaciones.")],
  open_task=task("Un yacimiento de ejemplo tiene 4.800 barriles y se usan 200 al año. Escribe una pregunta comprobable, una predicción con razón sobre qué pasa si el uso sube a 400 al año y calcula ambas duraciones. Escribe también una limitación de tu cálculo.", "Pregunta: ¿cuántos años durará con 200 y con 400? Predicción: con 400 durará la mitad, porque se gasta el doble por año. Cálculo: 24 años y 12 años. Limitación: puede haber nuevos hallazgos o cambios en el consumo.", ["pregunta con algo calculable", "predicción con razón", "dos duraciones correctas y una limitación"], ["tres frases y cálculos"], ["no dar razón", "errar la división"], "Pregunta qué medida podría evitar que el consumo se duplique."),
  reinforce="Calcula cuántos años dura un recurso de 600 unidades si se usan 50 al año.",
  extend="Explica por qué un panel solar produce distinto según el día.")

L(OA11, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Los datos de potencia son de ejemplo.",
  use="Aprenderé a representar con un esquema la clasificación de recursos y con una fórmula el consumo de energía de un aparato. Sirve para calcular cuánta energía gasta cada aparato.",
  prior=["Sé clasificar recursos renovables y no renovables.", "Sé multiplicar y dividir números naturales."],
  explain=[
      "Un esquema de clasificación ordena los recursos en grupos. Primero, recursos energéticos. De ahí salen dos ramas: no renovables (petróleo, gas natural, carbón mineral, uranio) y renovables (solar, viento, agua de ríos, geotérmica, mareas). Un esquema permite ver de un vistazo a qué grupo pertenece cada recurso y cuántos hay en cada rama.",
      "Otro modelo es una fórmula para calcular cuánta energía usa un aparato eléctrico. La potencia indica cuánta energía por hora usa y se mide en vatios (W). El consumo de energía se calcula multiplicando la potencia por las horas de uso. Se mide en vatios-hora (Wh). Por ejemplo, una ampolleta de 60 W encendida 5 horas gasta 60 × 5 = 300 Wh.",
      "El modelo tiene límites. Las potencias son datos de ejemplo; los reales dependen del aparato. La fórmula supone que el aparato usa siempre la misma potencia, lo que no siempre ocurre. El esquema no dice cuál recurso es mejor, solo cómo se clasifican. Por eso conviene decir qué muestra y qué no muestra.",
  ],
  vocab=[("potencia", "energía que usa un aparato cada hora"), ("vatio (W)", "unidad de potencia"), ("vatio-hora (Wh)", "unidad de consumo de energía"), ("rama", "parte de un esquema que sale de otra"), ("consumo de energía", "potencia multiplicada por las horas de uso")],
  worked=[
      ("Calcular el consumo", "Un televisor de ejemplo usa 100 W y está encendido 3 horas. ¿Cuántos Wh gasta?", ["Potencia: 100 W.", "Horas: 3.", "Multiplico 100 × 3."], "300 Wh"),
      ("Ubicar en el esquema", "¿En qué rama ubicas la geotérmica?", ["Recuerdo que el calor de la Tierra no se agota al usarlo.", "Eso la hace renovable.", "La ubico en la rama de los renovables."], "En los renovables"),
  ],
  mistakes=[
      ("Sumar la potencia con las horas.", "El consumo se calcula multiplicando.", "Multiplica potencia por horas."),
      ("Pensar que un aparato de más potencia siempre gasta más.", "También influye cuánto tiempo está encendido.", "Calcula potencia por horas."),
  ],
  rec=[
      ("¿La potencia se mide en vatios o en metros?", "En vatios", "Se escribe W."),
      ("Para calcular el consumo se multiplica potencia por ______. Completa con horas o colores.", "Horas", "El tiempo de uso."),
      ("¿La energía solar va en la rama de renovables o de no renovables?", "Renovables", "No se agota al usarla."),
  ],
  und=[
      ("¿Qué indica la potencia de un aparato?", "Cuánta energía usa cada hora", "Se mide en vatios."),
      ("¿En qué unidad se mide el consumo de energía?", "En vatios-hora (Wh)", "Es potencia por horas."),
      ("¿Qué no muestra el esquema de clasificación?", "Cuál recurso es mejor", "Solo agrupa los recursos."),
  ],
  app=[
      arith("Una ampolleta de 60 W está encendida 5 horas. ¿Cuántos Wh gasta?", "60*5", "Potencia por horas."),
      arith("Una ampolleta LED de 10 W está encendida 5 horas. ¿Cuántos Wh gasta?", "10*5", "Potencia por horas."),
      arith("¿Cuántos Wh se ahorran al usar la LED en vez de la de 60 W durante 5 horas?", "60*5-10*5", "Se restan los consumos de ambas."),
  ],
  rea=[
      ("Un compañero dice que una estufa de 1.000 W encendida 1 hora gasta lo mismo que una ampolleta de 10 W encendida 100 horas. Calcula ambas y responde Sí o No si es correcto.", "Sí", "1.000 × 1 = 1.000 y 10 × 100 = 1.000."),
      ("Otra persona suma 60 + 5 y dice que la ampolleta gasta 65 Wh. ¿Qué error cometió?", "Sumó en vez de multiplicar", "El consumo es potencia por horas."),
  ],
  cha=[
      ("Un cargador de 5 W está conectado 20 horas. ¿Cuántos Wh gasta?", "100", "5 × 20 = 100."),
      ("Un computador de 150 W se usa 4 horas al día. ¿Cuántos Wh gasta en 5 días?", "3.000", "150 × 4 × 5 = 3.000."),
  ],
  context=[("Dato de ejemplo. Una familia usa un hervidor de 2.000 W durante 2 horas en total en una semana. ¿Cuántos Wh gasta en esa semana?", "4.000", "2.000 × 2 = 4.000.")],
  selfcheck=[("¿Cómo se calcula el consumo de un aparato?", "Potencia por horas de uso", "Se mide en Wh."), ("¿Qué muestra el esquema de clasificación?", "A qué grupo pertenece cada recurso", "No dice cuál es mejor."), ("¿Qué límite tiene la fórmula?", "Supone una potencia constante", "En la realidad puede variar.")],
  open_task=task("Calcula el consumo diario en Wh de estos aparatos de ejemplo: ampolleta de 60 W por 4 horas, televisor de 100 W por 3 horas, cargador de 5 W por 10 horas. Súmalos y escribe un límite de tu cálculo. Dibuja también un esquema con una rama de renovables y otra de no renovables con tres recursos cada una.", "Ampolleta: 240 Wh. Televisor: 300 Wh. Cargador: 50 Wh. Total: 590 Wh. Límite: la potencia real puede variar. Esquema: renovables (solar, viento, mareas) y no renovables (petróleo, gas natural, carbón mineral).", ["tres cálculos correctos", "suma correcta", "esquema con dos ramas"], ["cálculos", "esquema"], ["sumar en vez de multiplicar", "poner un recurso en la rama equivocada"], "Pregunta cuál aparato gasta más y por qué."),
  reinforce="Calcula el consumo de una ampolleta de 20 W encendida 6 horas.",
  extend="Explica por qué un aparato de poca potencia puede gastar mucho si está encendido muchas horas.")

L(OA11, 4,
  materials="Este cuaderno y lápiz. Los datos de potencia están escritos en los ejercicios.",
  use="Aprenderé a comparar medidas de ahorro de energía con un criterio y a proponer un plan de uso responsable. Sirve para decidir qué cambios en casa o en el colegio ahorran más energía.",
  prior=["Sé calcular consumo con potencia por horas.", "Sé clasificar recursos renovables y no renovables."],
  explain=[
      "El uso responsable de la energía significa usar la que necesitamos sin desperdiciar, para cuidar los recursos y el ambiente. Algunas medidas: apagar las luces que no se usan, cambiar ampolletas por LED, desconectar los cargadores cuando no se usan, usar la luz natural de día, caminar o usar bicicleta o transporte público, usar ropa abrigada antes de encender la calefacción y mantener cerradas las ventanas con la calefacción prendida.",
      "Para comparar medidas se usa un criterio: cuántos Wh se ahorran por día. Por ejemplo, cambiar una ampolleta de 60 W por una LED de 10 W encendida 5 horas ahorra (60 − 10) × 5 = 250 Wh. Apagar un televisor de 100 W durante 2 horas ahorra 200 Wh. La primera ahorra más según el criterio.",
      "El criterio tiene límites. No considera el costo de la ampolleta nueva, si es fácil mantener el hábito ni el impacto ambiental completo. Además, algunas medidas, como caminar, ahorran energía de combustibles que no se miden en Wh eléctricos. Una buena propuesta combina varias medidas, dice cómo medir el resultado y reconoce un límite.",
  ],
  vocab=[("uso responsable", "usar la energía necesaria sin desperdiciar"), ("ahorro", "cantidad de energía que se deja de gastar"), ("LED", "tipo de ampolleta que gasta poca energía"), ("criterio", "regla para comparar y decidir"), ("plan de acción", "conjunto de medidas con pasos y metas")],
  worked=[
      ("Calcular el ahorro", "Cambiar una ampolleta de 40 W por una LED de 8 W encendida 6 horas. ¿Cuántos Wh se ahorran?", ["Diferencia de potencia: 40 − 8 = 32.", "Horas: 6.", "Multiplico 32 × 6."], "192 Wh"),
      ("Comparar con el criterio", "Medida A ahorra 192 Wh al día; medida B ahorra 150 Wh. ¿Cuál es mejor según el criterio?", ["Comparo 192 con 150.", "192 es mayor.", "Ahorra más la A."], "La medida A"),
  ],
  mistakes=[
      ("Elegir la medida que ahorra más sin pensar si se puede mantener.", "El criterio no considera el costo ni el hábito.", "Agrega un segundo análisis práctico."),
      ("Pensar que una sola medida resuelve todo.", "Un plan combina varias.", "Elige tres medidas distintas."),
  ],
  rec=[
      ("Apagar luces que no se usan, ¿ahorra o gasta más energía?", "Ahorra", "Evita consumo innecesario."),
      ("¿Una ampolleta LED gasta menos o más que una antigua?", "Menos", "Usa menos potencia para dar luz."),
      ("¿Desconectar un cargador que no se usa ahorra energía: Sí o No?", "Sí", "Evita un pequeño gasto continuo."),
  ],
  und=[
      ("¿Qué criterio se usó para comparar medidas?", "Cuántos Wh se ahorran por día", "Mientras más ahorra, mejor según el criterio."),
      ("¿Qué límite tiene el criterio de Wh ahorrados?", "No considera el costo ni si se mantiene el hábito", "Hay otros factores."),
      ("¿Cuál es una medida de uso responsable? A) Dejar el televisor prendido sin mirar. B) Apagarlo cuando no se mira.", "B", "Evita el gasto innecesario."),
  ],
  app=[
      arith("Cambiar una ampolleta de 100 W por una LED de 15 W encendida 4 horas. ¿Cuántos Wh se ahorran?", "(100-15)*4", "Diferencia de potencia por horas."),
      arith("Apagar un televisor de 120 W durante 2 horas al día. ¿Cuántos Wh se ahorran?", "120*2", "Potencia por horas."),
      arith("¿Cuántos Wh se ahorran en 7 días si cada día se ahorran 240?", "240*7", "Se multiplican por los días."),
  ],
  rea=[
      ("Medida A ahorra 340 Wh al día y cuesta $20.000. Medida B ahorra 300 Wh al día y cuesta $2.000. Según el criterio de Wh ahorrados, ¿cuál es mejor? Responde A o B.", "A", "Ahorra más Wh, aunque el costo es otro criterio."),
      ("Un compañero dice que solo conviene apagar el televisor. ¿Qué le falta a su plan?", "Combinar varias medidas", "Un plan usa distintas medidas."),
  ],
  cha=[
      ("Un plan ahorra 250 Wh con luces LED, 200 Wh apagando el televisor y 48 Wh desconectando cargadores. ¿Cuántos Wh ahorra en total al día?", "498", "250 + 200 + 48 = 498."),
      ("Con ese plan, ¿cuántos Wh se ahorran en 10 días?", "4.980", "498 × 10 = 4.980."),
  ],
  context=[("Dato de ejemplo. Un colegio ahorra 1.500 Wh por sala al día y tiene 12 salas. ¿Cuántos Wh ahorra en total al día?", "18.000", "1.500 × 12 = 18.000.")],
  selfcheck=[("¿Qué es el uso responsable de la energía?", "Usar la necesaria sin desperdiciar", "Cuida los recursos y el ambiente."), ("¿Con qué dato se compara el valor de cada medida de ahorro?", "Con los Wh ahorrados por día", "Se calcula con potencia y horas."), ("¿Por qué un plan combina varias medidas?", "Porque una sola rara vez resuelve todo", "Se logra más ahorro.")],
  open_task=task("Arma un plan de ahorro de energía con tres medidas para tu casa o colegio, usando estos datos de ejemplo: cambiar una ampolleta de 60 W por una LED de 12 W (5 horas al día), apagar un televisor de 90 W durante 2 horas al día y desconectar un cargador de 4 W (16 horas al día). Calcula cuántos Wh ahorra cada medida y en total, ordénalas de mayor a menor ahorro y escribe un límite.", "Ampolleta: (60 − 12) × 5 = 240 Wh. Televisor: 90 × 2 = 180 Wh. Cargador: 4 × 16 = 64 Wh. Total: 484 Wh. Orden: ampolleta, televisor, cargador. Límite: no considera el costo ni si se mantiene el hábito.", ["tres cálculos correctos", "total y orden", "un límite"], ["tabla de medidas con cálculos"], ["sumar en vez de multiplicar", "olvidar el límite"], "Pregunta qué medida sería más fácil de mantener."),
  reinforce="Escribe tres medidas de ahorro de energía que puedas hacer cada día.",
  extend="Explica por qué caminar o usar bicicleta también ayuda a usar la energía de manera responsable.")

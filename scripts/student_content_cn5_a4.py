"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 07 (microorganismos, salud e higiene) y OA 08 (transformaciones de energía eléctrica)."""
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




OA7, OA8 = "CN05 OA 07", "CN05 OA 08"

# ---------------------------------------------------------------- OA 07
L(OA7, 1,
  materials="Este cuaderno y lápiz. Los datos y descripciones que necesitas están escritos en los ejercicios.",
  use="Aprenderé qué son las bacterias, los virus y los hongos y que algunos ayudan y otros dañan. Sirve para entender por qué cuidamos la higiene.",
  prior=["Sé que los seres vivos están formados por células.", "Sé separar lo que se observa de lo que se supone."],
  explain=[
      "Los microorganismos son seres tan pequeños que solo se ven con microscopio. Hay tres grupos que se estudian en esta clase: las bacterias, los hongos y los virus. Las bacterias tienen una sola célula. Los hongos pueden tener una célula, como la levadura, o muchas, como las setas y el moho que sale en el pan viejo. Los virus son aún más pequeños, no son células y necesitan entrar a una célula para multiplicarse.",
      "Algunos microorganismos nos ayudan. Ciertas bacterias transforman la leche en yogur. La levadura, un hongo, hace que la masa del pan se esponje. Algunas bacterias viven en el intestino sin hacernos daño. Otros microorganismos nos dañan: unas bacterias causan infecciones de la garganta, y algunos virus causan resfríos o la influenza. Un hongo puede producir una infección en los pies.",
      "No se puede saber qué microorganismo hay por el aspecto. Decir «ese vaso se ve sucio, tiene virus» es una interpretación. Una observación es lo que se ve o se mide, como «hay 5 manchas en el vaso». Las medidas de higiene, como lavarse las manos, reducen los microorganismos dañinos.",
  ],
  vocab=[("microorganismo", "ser tan pequeño que solo se ve con microscopio"), ("bacteria", "microorganismo de una sola célula"), ("hongo", "ser vivo que puede tener una célula, como la levadura, o muchas, como las setas"), ("virus", "agente muy pequeño que no es una célula y necesita entrar a una para multiplicarse"), ("higiene", "hábitos de limpieza que cuidan la salud")],
  worked=[
      ("Clasificar un microorganismo", "La levadura del pan tiene una célula y ayuda a esponjar la masa. ¿Es bacteria, virus u hongo?", ["Es una célula y se usa para el pan.", "La levadura es un hongo unicelular.", "Además es beneficiosa."], "Hongo beneficioso"),
      ("Observación o interpretación", "«Hay 5 manchas en el vaso» y «El vaso está lleno de virus». ¿Cuál es observación?", ["Pregunto qué se cuenta.", "Las manchas se cuentan.", "No se pueden ver los virus sin microscopio."], "La primera frase"),
  ],
  mistakes=[
      ("Pensar que todos los microorganismos hacen daño.", "Muchos son beneficiosos, como los del yogur.", "Pregunta si el microorganismo ayuda o daña."),
      ("Creer que se sabe qué microorganismo hay por el aspecto de algo.", "Son demasiado pequeños para verse a simple vista.", "No supongas; usa evidencia."),
  ],
  rec=[
      ("¿Las bacterias tienen una célula o muchas?", "Una", "Son seres unicelulares."),
      ("La levadura, ¿es un hongo o un virus?", "Un hongo", "Es un hongo unicelular."),
      ("Completa con «microscopio» o «regla»: los microorganismos se ven con un ______.", "Microscopio", "Son demasiado pequeños para verse a simple vista."),
  ],
  und=[
      ("¿Qué microorganismo ayuda a esponjar la masa del pan?", "La levadura", "Es un hongo que libera gas."),
      ("¿Por qué un virus no es una célula?", "Porque no tiene la estructura de una célula y necesita entrar a una para multiplicarse", "Por sí solo no puede multiplicarse."),
      ("Marca el ejemplo de microorganismo dañino: A) Bacterias que causan una infección de garganta. B) Bacterias que hacen yogur.", "A", "Las del yogur son beneficiosas."),
  ],
  app=[
      ("Lista: levadura, bacteria del yogur, virus del resfrío, hongo del pie. ¿Cuántos son dañinos?", "2", "El virus del resfrío y el hongo del pie causan enfermedades."),
      arith("Una clase contó 12 manchas en un vaso y 7 en otro. ¿Cuántas manchas más había en el primero?", "12-7", "Se resta el valor menor al mayor."),
      ("Clasifica el moho que crece en un pan dejado muchos días como bacteria, virus u hongo.", "Hongo", "El moho es un hongo."),
  ],
  rea=[
      ("Mateo dice: «Como no veo suciedad, no hay microorganismos». ¿Tiene razón? Responde Sí o No y explica.", "No; son tan pequeños que no se ven a simple vista", "Solo se ven con microscopio."),
      ("Ema dice que el yogur es peligroso porque tiene bacterias. ¿Qué le explicas?", "Las bacterias del yogur son beneficiosas", "Algunas bacterias ayudan a elaborar alimentos."),
  ],
  cha=[
      ("Escribe un ejemplo de microorganismo beneficioso y uno dañino.", "Beneficioso: levadura. Dañino: virus del resfrío", "Cada uno tiene un efecto distinto."),
      ("Explica por qué una observación como «hay 5 manchas» es mejor evidencia que «está lleno de virus».", "Porque se puede contar, mientras que los virus no se ven sin microscopio", "Solo lo observable es evidencia."),
  ],
  context=[("Dato de ejemplo. Una clase hizo una tabla con 3 microorganismos beneficiosos y 3 dañinos. ¿Cuántos microorganismos escribieron?", "6", "3 + 3 = 6.")],
  selfcheck=[("¿Qué son los microorganismos?", "Seres tan pequeños que solo se ven con microscopio", "Hay bacterias, hongos y virus."), ("¿Todos hacen daño?", "No", "Algunos son beneficiosos."), ("¿Los virus son células? Responde Sí o No.", "No", "Necesitan entrar a una célula para multiplicarse.")],
  open_task=task("Haz una tabla de dos columnas: «beneficiosos» y «dañinos». Escribe en ella al menos tres ejemplos en cada columna entre estos: bacterias del yogur, levadura del pan, virus del resfrío, hongo del pie, bacterias de una infección de garganta, bacterias del intestino. Marca si cada ejemplo es bacteria, hongo o virus.", "Beneficiosos: bacterias del yogur (bacteria), levadura (hongo), bacterias del intestino (bacteria). Dañinos: virus del resfrío (virus), hongo del pie (hongo), bacterias de una infección de garganta (bacteria).", ["seis ejemplos clasificados", "tipo de microorganismo marcado", "usa solo los ejemplos dados"], ["tabla completa"], ["decir que todos dañan", "confundir hongo con bacteria"], "Pregunta cuál ejemplo le sorprendió y por qué."),
  reinforce="Escribe tres microorganismos y di si son bacteria, hongo o virus.",
  extend="Explica por qué lavarse las manos ayuda aunque no veamos los microorganismos.")

L(OA7, 2,
  materials="Este cuaderno y lápiz. Opcional (con una persona adulta): una botella plástica pequeña, una cucharadita de levadura seca, una de azúcar, agua tibia (no caliente) y un globo.",
  use="Aprenderé a plantear una pregunta y una predicción sobre un hongo, la levadura. Sirve para comprobar que un microorganismo puede ser beneficioso.",
  prior=["Sé que la levadura es un hongo unicelular.", "Sé que una predicción lleva una razón."],
  explain=[
      "La levadura es un hongo de una sola célula. Cuando tiene agua tibia y azúcar, usa el azúcar como alimento y libera un gas, el dióxido de carbono. Ese gas forma burbujas y hace que la masa del pan suba. Sin alimento y sin humedad, la levadura casi no produce gas.",
      "Una pregunta comprobable es: «¿Se infla más un globo cuando la levadura tiene azúcar que cuando no la tiene?». Predicción: se infla más con azúcar, porque la levadura usa el azúcar como alimento y libera gas. Se hacen dos botellas iguales; la única variable que cambia es el azúcar. El agua, la levadura y el tiempo son iguales.",
      "Para comparar se mide el contorno del globo con una cinta o un hilo y una regla. Como la medida puede cambiar si el globo se infla de forma despareja, conviene repetir. Este experimento es un modelo simple: no muestra a la levadura individual. Se hace con agua tibia y con una persona adulta.",
  ],
  vocab=[("levadura", "hongo de una célula que produce gas con azúcar"), ("dióxido de carbono", "gas que libera la levadura"), ("variable", "lo que cambia en una prueba"), ("control", "caso sin la variable, para comparar"), ("contorno", "largo de la línea que rodea al globo")],
  worked=[
      ("Identificar la variable", "Botella A: levadura, agua tibia y azúcar. Botella B: levadura y agua tibia. ¿Qué variable cambia?", ["Comparo las dos botellas.", "Lo único distinto es el azúcar.", "Todo lo demás es igual."], "Si tiene azúcar o no"),
      ("Predicción con razón", "¿Qué globo se inflará más: el de la botella con azúcar o el de la botella sin azúcar?", ["La levadura usa el azúcar como alimento.", "Con alimento libera más gas.", "Escribo la predicción con razón."], "El de la botella con azúcar, porque la levadura libera más gas con alimento"),
  ],
  mistakes=[
      ("Cambiar el azúcar y la temperatura del agua a la vez.", "No sabrás cuál causó la diferencia.", "Cambia solo una variable."),
      ("Usar agua muy caliente.", "Puede quemar y matar a la levadura.", "Usa agua tibia."),
  ],
  rec=[
      ("¿Qué gas libera la levadura?", "Dióxido de carbono", "Ese gas forma burbujas."),
      ("¿Qué usa la levadura como alimento en la prueba?", "El azúcar", "La levadura usa el azúcar para producir gas."),
      ("Completa con «tibia» o «hirviendo»: la prueba se hace con agua ______.", "Tibia", "El agua muy caliente puede dañar a la levadura y a las personas."),
  ],
  und=[
      ("¿Por qué se preparan dos botellas iguales?", "Para comparar con una sola variable distinta", "Así se sabe qué causó la diferencia."),
      ("¿Cuál es el control en el experimento: la botella sin azúcar o la botella con azúcar?", "La botella sin azúcar", "No tiene la variable que se prueba."),
      ("¿Qué pregunta se puede comprobar? A) ¿Cuántos centímetros mide el contorno de cada globo? B) ¿Qué globo es más lindo?", "A", "El contorno se mide."),
  ],
  app=[
      arith("Dato de ejemplo. A los 20 minutos el globo de la botella con azúcar medía 12 cm de contorno y el de la botella sin azúcar 3 cm. ¿Cuántos centímetros más medía el primero?", "12-3", "Se resta el valor menor al mayor."),
      arith("Dato de ejemplo. Una niña midió el contorno 3 veces con azúcar: 11, 12 y 13 cm. ¿Cuántos centímetros suman?", "11+12+13", "Se suman las tres mediciones."),
      ("Rita predijo que el globo con azúcar se inflaría más. Midió 12 cm con azúcar y 3 cm sin azúcar. ¿Se cumplió su predicción? Responde Sí o No.", "Sí", "12 es mayor que 3."),
  ],
  rea=[
      ("Pablo puso azúcar en una botella con agua tibia y no en otra con agua fría. El globo con azúcar se infló más. Dice: «Fue por el azúcar». ¿Puede asegurarlo? Responde Sí o No y explica.", "No; cambiaron el azúcar y la temperatura", "Con dos cambios no se sabe cuál causó el resultado."),
      ("Ema repitió la prueba tres veces y el globo con azúcar siempre se infló más. ¿Eso hace más confiable su resultado? Responde Sí o No y explica.", "Sí; se repitió y dio parecido", "Repetir reduce el efecto del azar."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre la levadura, indicando qué medirás.", "¿Cuántos centímetros de contorno tiene el globo con y sin azúcar a los 20 minutos?", "Nombra lo que se cambia y lo que se mide."),
      ("Un límite del experimento es que no se ve a la levadura. Escribe otro límite.", "Solo muestra el gas, no muestra qué hace cada célula", "El experimento es un modelo simple."),
  ],
  context=[("Dato de ejemplo. Un curso hizo la prueba en 5 grupos y los globos con azúcar midieron 12, 11, 13, 12 y 12 cm. ¿Cuántos centímetros sumaron?", "60", "12 + 11 + 13 + 12 + 12 = 60.")],
  selfcheck=[("¿Qué usa la levadura para producir gas?", "Azúcar", "Es su alimento."), ("¿Por qué se cambia una sola variable?", "Para saber qué causó la diferencia", "Con dos cambios no se sabe."), ("¿Qué agua se usa en la prueba?", "Agua tibia", "Es segura y no daña a la levadura.")],
  open_task=task("Con una persona adulta, prepara dos botellas pequeñas iguales con una cucharadita de levadura y agua tibia (no caliente). A una agrégale una cucharadita de azúcar. Pon un globo en la boca de cada botella. Antes escribe tu predicción con razón. A los 20 minutos mide el contorno de cada globo con un hilo y una regla. No pruebes la mezcla.", "Predicción: el globo con azúcar se inflará más porque la levadura usa el azúcar como alimento. Resultado de ejemplo: con azúcar 12 cm, sin azúcar 3 cm. Se cumplió.", ["predicción con razón", "una sola variable que cambia", "medidas anotadas y conclusión"], ["tabla con dos medidas", "frase de conclusión"], ["cambiar dos variables", "probar la mezcla"], "Pregunta qué mantuvo igual y qué mostraría el globo que no se infla."),
  reinforce="Escribe una predicción con razón sobre qué pasa si la levadura se deja en agua fría con azúcar.",
  extend="Explica por qué el pan sube cuando se hornea la masa con levadura.")

L(OA7, 3,
  materials="Este cuaderno y lápiz. Opcional: un puñado de harina en una bandeja y un objeto de plástico, como una tapa.",
  use="Aprenderé a usar un modelo de cómo se pasan los microorganismos de una persona a otra y a proponer medidas de higiene. Sirve para entender por qué nos lavamos las manos.",
  prior=["Sé que hay microorganismos beneficiosos y dañinos.", "Sé que un modelo tiene límites."],
  explain=[
      "Algunos microorganismos dañinos pasan de una persona a otra. Pueden pasar por contacto, por ejemplo al tocar un objeto que otra persona tocó; por las gotitas de la tos o el estornudo; o por alimentos y agua contaminados. Cuando una persona enferma toca una superficie, puede dejar microorganismos en ella.",
      "Un modelo con harina ayuda a ver esto. La harina representa los microorganismos. Si una persona con harina en las manos toca una tapa, deja marcas. Quien toca la tapa después se lleva harina. Si esa persona se lava las manos con agua y jabón antes de tocar la tapa, deja muchas menos marcas. El modelo muestra el recorrido, pero no son microorganismos reales.",
      "Las medidas de higiene cortan ese recorrido. Hay que lavarse las manos con agua y jabón durante unos 20 segundos y cubrirse al toser con el antebrazo. También conviene no compartir vasos, mantener cortas las uñas, cepillarse los dientes y lavar bien los alimentos. También conviene mantener las vacunas al día, siguiendo a los profesionales de la salud.",
  ],
  vocab=[("contacto", "tocar algo o a alguien"), ("gotitas", "gotas muy pequeñas que salen al toser o estornudar"), ("contaminado", "con microorganismos dañinos"), ("antebrazo", "parte del brazo entre el codo y la muñeca"), ("vacuna", "medicamento que prepara al cuerpo para defenderse")],
  worked=[
      ("Seguir el recorrido", "Una persona con harina toca una tapa. Otra persona toca la tapa y luego su cara. ¿Qué pasó con la harina?", ["La primera persona dejó harina en la tapa.", "La segunda persona la recogió.", "Llegó a su cara."], "La harina pasó de la primera persona a la cara de la segunda"),
      ("Elegir la medida", "¿Qué medida corta el recorrido? A) Lavarse las manos con agua y jabón. B) Tocarse la cara.", ["Pregunto si quita los microorganismos.", "El lavado los arrastra.", "Tocarse la cara los lleva."], "A"),
  ],
  mistakes=[
      ("Toser en la mano y luego tocar objetos.", "Los microorganismos quedan en la mano y pasan a lo que tocas.", "Cúbrete con el antebrazo."),
      ("Lavarse las manos solo un segundo con agua.", "No alcanza a arrastrar los microorganismos.", "Usa agua y jabón unos 20 segundos."),
  ],
  rec=[
      ("En el modelo, ¿la harina representa microorganismos o alimentos?", "Microorganismos", "Sirve para ver cómo se pasan."),
      ("¿Con qué parte del brazo se cubre al toser: con la mano o con el antebrazo?", "Con el antebrazo", "Así no quedan microorganismos en la mano."),
      ("Completa con «agua y jabón» o «solo aire»: las manos se lavan con ______.", "Agua y jabón", "El jabón ayuda a arrastrar los microorganismos."),
  ],
  und=[
      ("¿Por qué se recomienda no compartir vasos?", "Porque los microorganismos pueden pasar de la boca de una persona a otra", "El contacto con la saliva los traslada."),
      ("¿Qué muestra el modelo de la harina?", "Cómo pasan los microorganismos por contacto", "Las marcas de harina muestran el recorrido."),
      ("¿Qué limita al modelo de la harina? A) La harina se ve y los microorganismos no. B) La harina es blanca.", "A", "El modelo hace visible lo que no se ve."),
  ],
  app=[
      arith("Dato de ejemplo. En el modelo, una persona dejó 12 marcas de harina en una tapa y otra, que antes se lavó las manos, dejó 3. ¿Cuántas marcas menos dejó la segunda?", "12-3", "Se resta el valor menor al mayor."),
      ("Rita tose y se cubre con el antebrazo. ¿Dónde quedan las gotitas: en su mano o en su antebrazo?", "En su antebrazo", "La mano queda limpia para tocar objetos."),
      ("Lista de medidas: lavar las manos, compartir el vaso, cortar las uñas, tocarse los ojos con las manos sin lavar. ¿Cuántas son medidas de higiene?", "2", "Lavar las manos y cortar las uñas."),
  ],
  rea=[
      ("Tomás dice: «Si veo mis manos limpias, no hay microorganismos». ¿Tiene razón? Responde Sí o No y explica.", "No; los microorganismos no se ven a simple vista", "Por eso se lavan las manos aunque se vean limpias."),
      ("En el modelo, una persona se lavó las manos con agua sola y dejó 8 marcas, mientras otra con agua y jabón dejó 3. ¿Qué conclusión puedes sacar?", "En estos datos, agua y jabón dejó menos marcas que solo agua", "Compara marcas con el mismo criterio."),
  ],
  cha=[
      ("Escribe dos límites del modelo de la harina.", "La harina se ve y los microorganismos no, y la harina no se multiplica", "Un modelo no copia toda la realidad."),
      ("Propón una medida de higiene para la hora del almuerzo en la escuela y di qué recorrido corta.", "Lavarse las manos con agua y jabón antes de comer corta el paso desde las manos a los alimentos", "Quita microorganismos antes del contacto con la comida."),
  ],
  context=[("Dato de ejemplo. Una clase hizo la prueba de la harina en 4 grupos y cada grupo contó 6 marcas en la tapa. ¿Cuántas marcas contaron en total?", "24", "4 × 6 = 24.")],
  selfcheck=[("Nombra dos formas en que pasan los microorganismos dañinos.", "Por contacto y por gotitas", "También pueden pasar por alimentos o agua contaminados."), ("Nombra una medida de higiene.", "Lavarse las manos con agua y jabón", "El lavado quita microorganismos de las manos."), ("¿Para qué sirve usar harina en el modelo?", "Para hacer visible cómo se pasan los microorganismos por contacto", "Los microorganismos reales no se ven.")],
  open_task=task("Con una persona de tu casa, haz el modelo de la harina: pon una cucharada de harina en las palmas, toca una tapa de plástico sin lavarte y cuenta las marcas. Limpia la tapa con un paño húmedo. Repite: pon harina en las palmas, lávate las manos con agua y jabón durante 20 segundos, sécalas y toca de nuevo la tapa. Cuenta las marcas en cada caso y escribe una conclusión y una limitación. No uses harina si alguien en casa es alérgico.", "Sin lavar: 12 marcas. Con lavado: 3 marcas. Conclusión: lavarse las manos redujo las marcas. Limitación: la harina no son microorganismos reales.", ["dos pruebas con el mismo método", "conteo de marcas", "conclusión y limitación"], ["tabla con dos conteos", "frases"], ["usar harina con alérgicos", "no escribir la limitación"], "Pregunta qué variable cambió y qué otras medidas de higiene ayudarían."),
  reinforce="Escribe tres medidas de higiene y el recorrido que cada una corta.",
  extend="Explica por qué las vacunas se consideran una medida de cuidado de la salud.")

L(OA7, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar bacterias, virus y hongos con los mismos criterios y a comparar medidas de higiene con datos. Sirve para elegir qué medidas ayudan más.",
  prior=["Sé qué son bacterias, virus y hongos.", "Sé que para comparar uso un mismo criterio."],
  explain=[
      "Para comparar microorganismos usamos criterios como: ¿es una célula o no?, ¿tiene ejemplos beneficiosos? y ¿tiene ejemplos dañinos? Las bacterias son células y las hay beneficiosas, como las del yogur, y dañinas, como las de una infección de garganta. Los hongos son seres con células; hay beneficiosos, como la levadura, y dañinos, como el que causa una infección en los pies. Los virus no son células y los que se estudian en esta clase son dañinos, como el del resfrío.",
      "También se comparan medidas de higiene con datos. Por ejemplo, tras tocar una superficie con harina en las manos, se cuentan las marcas: sin lavar, solo agua y agua con jabón. Menos marcas indican que la medida arrastra más. El mismo método y el mismo tiempo deben usarse para todas.",
      "Un detalle importante: los antibióticos son medicamentos que actúan contra bacterias, no contra virus. Solo un profesional de la salud decide cuándo usarlos. Una tabla ayuda a ordenar los resultados.",
  ],
  vocab=[("criterio", "característica que se mira igual en todos los casos"), ("antibiótico", "medicamento que actúa contra bacterias"), ("arrastrar", "llevarse algo con el agua"), ("comparación", "mirar parecidos y diferencias con un criterio común"), ("dato", "número o hecho registrado")],
  worked=[
      ("Comparar con un criterio", "Criterio: ¿es una célula? Bacteria, hongo, virus.", ["Las bacterias son células.", "Los hongos tienen células.", "Los virus no son células."], "Bacteria: sí. Hongo: sí. Virus: no"),
      ("Comparar medidas", "Datos de ejemplo. Marcas de harina: sin lavar 12, solo agua 8, agua y jabón 3. ¿Qué medida dejó menos marcas?", ["Comparo los números.", "El menor es 3.", "Corresponde a agua y jabón."], "Agua y jabón"),
  ],
  mistakes=[
      ("Pensar que los antibióticos curan los resfríos.", "El resfrío lo causa un virus y los antibióticos actúan contra bacterias.", "Consulta a un profesional de la salud."),
      ("Comparar medidas con métodos distintos.", "No hay criterio común.", "Usa el mismo método para todas."),
  ],
  rec=[
      ("¿Los virus son células?", "No", "Son más pequeños y necesitan entrar a una célula."),
      ("¿Con qué medida quedaron menos marcas en los datos de ejemplo: agua y jabón o solo agua?", "Agua y jabón", "Dejó 3 marcas frente a 8."),
      ("Completa con «bacterias» o «virus»: los antibióticos actúan contra las ______.", "Bacterias", "No actúan contra los virus."),
  ],
  und=[
      ("¿Qué criterio permite distinguir a los virus de las bacterias?", "Si son células o no", "Las bacterias son células y los virus no."),
      ("¿Quién decide cuándo se usa un antibiótico?", "Un profesional de la salud", "Solo ellos saben si hay una infección por bacterias."),
      ("¿Qué comparación es justa? A) Contar marcas con el mismo método. B) Contar marcas con métodos distintos.", "A", "Con el mismo método se compara bien."),
  ],
  app=[
      arith("Dato de ejemplo. Sin lavar hubo 12 marcas y con agua y jabón 3. ¿Cuántas marcas se evitaron?", "12-3", "Se resta el valor menor al mayor."),
      arith("Dato de ejemplo. En 3 pruebas con solo agua se contaron 8, 9 y 7 marcas. ¿Cuántas marcas sumaron?", "8+9+7", "Se suman las tres pruebas."),
      ("De bacteria, hongo y virus, ¿cuántos tienen ejemplos beneficiosos en esta clase?", "2", "Las bacterias del yogur y la levadura (hongo)."),
  ],
  rea=[
      ("Ana toma un antibiótico por un resfrío porque lo tenía en casa. ¿Qué error hay?", "El resfrío lo causa un virus y los antibióticos no actúan contra los virus", "Además, solo un profesional decide su uso."),
      ("Raúl contó marcas 10 s después de tocar y Ema 30 s después. Dice que su medida fue mejor. ¿Qué problema hay?", "Los tiempos no son iguales", "Los métodos deben ser iguales para comparar."),
  ],
  cha=[
      ("Escribe una conclusión con los datos de ejemplo: sin lavar 12, solo agua 8, agua y jabón 3.", "En estos datos de ejemplo, agua y jabón dejó menos marcas que solo agua", "Compara con el mismo criterio."),
      ("¿Qué limitación tienen esos datos de ejemplo?", "Son de una prueba con harina y no de microorganismos reales", "Es un modelo."),
  ],
  context=[("Dato de ejemplo. Una clase probó 3 medidas en 5 grupos y anotó un dato por grupo y medida. ¿Cuántos datos anotó?", "15", "3 × 5 = 15.")],
  selfcheck=[("¿Qué microorganismos no son células?", "Los virus", "Necesitan entrar a una célula."), ("¿Contra qué actúan los antibióticos?", "Contra las bacterias", "No actúan contra virus."), ("¿Por qué se usa el mismo método al comparar?", "Para que la comparación sea justa", "Así se sabe que la diferencia viene de la medida.")],
  open_task=task("Haz una tabla de tres filas (bacterias, hongos, virus) y tres columnas: «¿es célula?», «un ejemplo beneficioso» y «un ejemplo dañino». Complétala con lo aprendido (puedes escribir «ninguno visto en esta clase»). Escribe una conclusión y una limitación.", "Bacterias: sí; yogur; infección de garganta. Hongos: sí; levadura; pie de atleta. Virus: no; ninguno visto; resfrío. Conclusión: no todos los microorganismos dañan. Limitación: hay más ejemplos que los de esta clase.", ["tabla completa", "conclusión", "limitación"], ["tabla", "frases"], ["afirmar que los virus son células", "decir que todos dañan"], "Pregunta qué columna fue más difícil y por qué."),
  reinforce="Compara bacterias y virus con el criterio «¿es una célula?».",
  extend="Explica por qué los antibióticos no sirven contra los resfríos.")

L(OA7, 5,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a explicar con evidencia qué microorganismos ayudan o dañan y a proponer medidas de higiene con sus límites. Sirve para cuidar el cuerpo con información.",
  prior=["Sé comparar microorganismos y medidas.", "Sé que una explicación necesita evidencia."],
  explain=[
      "Una explicación completa responde: qué microorganismo, si ayuda o daña, cómo llega a las personas y qué medida lo detiene. Por ejemplo: «Las bacterias del yogur son beneficiosas porque transforman la leche». O: «Un virus del resfrío pasa por gotitas y contacto, por eso conviene cubrirse al toser y lavarse las manos».",
      "Las medidas de cuidado e higiene del cuerpo incluyen lavarse las manos con agua y jabón, ducharse y cepillarse los dientes después de comer. También sirven usar ropa limpia, refrigerar los alimentos cuando corresponde y lavar frutas y verduras. Además, se mantienen las vacunas al día. También ayudan dormir bien y comer variado.",
      "Los límites importan: los resultados del modelo de la harina no son microorganismos reales, no todos los síntomas se deben a microorganismos y los medicamentos los indica un profesional de la salud. Una explicación honesta dice lo que sabemos, con qué evidencia y lo que no sabemos.",
  ],
  vocab=[("explicación", "relato que dice qué pasa y por qué"), ("evidencia", "dato que apoya una explicación"), ("medida de higiene", "hábito que cuida la salud"), ("refrigerar", "guardar en el frío para que no se echen a perder"), ("síntoma", "señal de que el cuerpo está mal, como fiebre o tos")],
  worked=[
      ("Completar una explicación", "Completa: «Lavarse las manos corta el recorrido por ______».", ["Pienso en cómo pasan los microorganismos.", "Las manos tocan objetos y alimentos.", "El recorrido es por contacto."], "Contacto"),
      ("Evidencia y límite", "En un modelo con harina, el lavado redujo las marcas de 12 a 3. ¿Qué evidencia da y qué límite tiene?", ["Hay una diferencia de marcas.", "La harina no es un microorganismo.", "Es un modelo."], "Evidencia: menos marcas con lavado. Límite: la harina no son microorganismos reales"),
  ],
  mistakes=[
      ("Dar una explicación sin evidencia, como «porque sí».", "No permite comprobar.", "Cita un dato o una observación."),
      ("Creer que cualquier tos o fiebre es causada por el mismo microorganismo.", "Hay muchas causas posibles.", "Consulta a un profesional de la salud."),
  ],
  rec=[
      ("¿Lavarse las manos corta el recorrido por contacto?", "Sí", "Quita microorganismos de las manos."),
      ("¿Quién indica un medicamento: un profesional de la salud o un amigo?", "Un profesional de la salud", "Sabe qué necesita cada persona."),
      ("Completa con «refrigerar» o «mojar»: ciertos alimentos se guardan en el frío para ______ y que no se echen a perder.", "Refrigerar", "El frío frena el crecimiento de microorganismos."),
  ],
  und=[
      ("¿Qué medida ayuda a evitar caries: cepillarse los dientes o dormir sin luz?", "Cepillarse los dientes", "Quita restos de comida donde viven bacterias."),
      ("¿Por qué el modelo de la harina tiene límites?", "Porque la harina no son microorganismos reales", "Solo muestra un recorrido por contacto."),
      ("¿Qué frase tiene evidencia? A) En los datos de ejemplo, el lavado dejó 3 marcas frente a 12. B) El lavado sirve porque sí.", "A", "A cita datos."),
  ],
  app=[
      ("Ordena la explicación: A) por eso conviene lavarse las manos, B) los microorganismos pasan por contacto, C) las manos tocan muchos objetos. Escribe el orden.", "C, B, A", "Primero el hecho, luego el recorrido y al final la medida."),
      arith("Una persona se lava las manos 5 veces al día. ¿Cuántas veces se las lava en 7 días?", "5*7", "Se multiplican las veces por los días."),
      ("De las medidas lavar frutas, cepillar dientes y compartir vasos, ¿cuántas son de higiene?", "2", "Compartir vasos puede pasar microorganismos."),
  ],
  rea=[
      ("Un afiche dice: «Esta pastilla elimina todos los microorganismos». ¿Tiene evidencia? Responde Sí o No y explica.", "No; no da datos y promete demasiado", "Ningún producto elimina todos los microorganismos y no se usan sin indicación profesional."),
      ("Nico dice que lavar las manos sirve porque así se quita lo sucio que se ve. ¿Qué agregarías para explicar mejor?", "También quita microorganismos que no se ven", "El lavado arrastra microorganismos invisibles."),
  ],
  cha=[
      ("Escribe una explicación de dos frases sobre el virus del resfrío: cómo pasa y qué medida ayuda.", "Pasa por gotitas y contacto; cubrirse con el antebrazo y lavarse las manos ayuda", "Une el recorrido con la medida."),
      ("Propón un plan de higiene de tres medidas para un campamento escolar.", "Lavarse las manos antes de comer, cuidar los alimentos y no compartir vasos", "Cada medida corta un recorrido."),
  ],
  context=[("Dato de ejemplo. Un curso de 30 estudiantes anotó cuántos se lavaron las manos antes del almuerzo: 24. ¿Cuántos no se lavaron?", "6", "30 − 24 = 6.")],
  selfcheck=[("¿Qué incluye una explicación completa?", "Qué microorganismo, cómo llega y qué medida lo detiene", "Une causa, recorrido y medida."), ("¿Por qué consultar a un profesional?", "Porque cada persona necesita un cuidado distinto", "Los síntomas pueden tener varias causas."), ("¿Qué límite tiene el modelo de la harina?", "No son microorganismos reales", "Solo muestra el recorrido.")],
  open_task=task("Escribe un plan de cuidado e higiene de cinco frases para una semana: tres medidas de higiene del cuerpo, una de cuidado de los alimentos y una de cómo cubrirse al toser. Después escribe cuál microorganismo ayuda y cuál daña (con un ejemplo de cada uno) y un límite de tu plan.", "Me lavo las manos antes de comer, me cepillo los dientes, me ducho, lavo las frutas, me cubro con el antebrazo. Ayuda: bacterias del yogur. Daña: virus del resfrío. Límite: un plan no reemplaza al profesional de la salud.", ["cinco medidas concretas", "un ejemplo beneficioso y uno dañino", "un límite"], ["lista de medidas", "frases"], ["medidas sin relación con el cuerpo", "no escribir límite"], "Pregunta qué medida le parece más fácil de mantener y qué recorrido corta."),
  reinforce="Escribe una explicación corta sobre por qué se cubre la tos con el antebrazo.",
  extend="Explica por qué hay microorganismos que conviene cuidar y no eliminar.")

# ---------------------------------------------------------------- OA 08
L(OA8, 1,
  materials="Este cuaderno y lápiz. Opcional: una linterna a pila para observar luz y calor leve. No toques enchufes ni artefactos conectados a la red.",
  use="Aprenderé qué es una transformación de energía eléctrica y a separar lo que observo de lo que supongo en los artefactos. Sirve para explicar lo que hacen los aparatos de tu casa.",
  prior=["Sé que la energía permite que algo cambie o se mueva.", "Sé separar observaciones de interpretaciones."],
  explain=[
      "La energía eléctrica es la que llega a los artefactos por los cables o la que entrega una pila. Un artefacto transforma esa energía en otra forma útil. La ampolleta la transforma en luz y calor. La estufa eléctrica y la plancha, en calor. El parlante y el timbre, en sonido. El ventilador y la licuadora, en movimiento. La pila de una linterna guarda energía química y la transforma en energía eléctrica.",
      "Para saber qué transformación ocurre, observamos con cuidado: ¿hay luz?, ¿hay calor?, ¿hay sonido?, ¿hay movimiento? Una observación es lo que percibes: «el ventilador gira y hace aire». Una interpretación es lo que supones: «el ventilador gasta mucha energía». Para afirmarlo hace falta una medición.",
      "Muy importante: la electricidad de la red es peligrosa. Nunca hagas experimentos con enchufes ni con cables conectados a la pared. Para observar un artefacto que calienta, como una plancha, mira a distancia y pide ayuda a una persona adulta. Esta clase se trabaja con descripciones.",
  ],
  vocab=[("energía eléctrica", "energía que llega por cables o la que entrega una pila"), ("transformación", "paso de una forma de energía a otra"), ("energía lumínica", "energía en forma de luz"), ("energía calórica", "energía en forma de calor"), ("energía sonora", "energía en forma de sonido")],
  worked=[
      ("Identificar la transformación", "Un parlante conectado a una pila suena. ¿En qué se transforma la energía eléctrica?", ["Pregunto qué percibo.", "Percibo sonido.", "La energía eléctrica se transforma en sonora."], "En energía sonora"),
      ("Observación o interpretación", "«El ventilador gira y mueve el aire» y «El ventilador gasta muchísima energía». ¿Cuál es observación?", ["Pregunto qué se ve o se siente.", "El giro se ve.", "El gasto no se midió."], "La primera frase"),
  ],
  mistakes=[
      ("Pensar que la ampolleta solo da luz.", "También da calor.", "Pregunta qué más percibes."),
      ("Hacer pruebas con un enchufe de la pared.", "Es peligroso.", "Usa solo descripciones o pilas con una persona adulta."),
  ],
  rec=[
      ("¿La ampolleta transforma energía eléctrica en luz y calor o en sonido?", "En luz y calor", "Una ampolleta ilumina y se calienta."),
      ("Un timbre suena. ¿Qué forma de energía produce?", "Sonora", "El sonido es energía sonora."),
      ("Completa con «eléctrica» o «química»: la pila transforma energía química en energía ______.", "Eléctrica", "Entrega energía eléctrica a la linterna."),
  ],
  und=[
      ("¿En qué transforma la energía eléctrica una plancha?", "En calor", "Se calienta para planchar."),
      ("¿En qué transforma la energía eléctrica un ventilador?", "En movimiento", "Gira y mueve el aire."),
      ("Marca la observación: A) La linterna ilumina la pared. B) La linterna es muy eficiente.", "A", "A se ve; B necesita medición."),
  ],
  app=[
      ("Artefactos: ampolleta, estufa, parlante, ventilador. ¿Cuántos se usan sobre todo para dar calor?", "1", "Solo la estufa."),
      ("Clasifica el timbre eléctrico como luz, calor o sonido, según su efecto principal.", "Sonido", "Un timbre se usa para avisar con sonido."),
      arith("Dato de ejemplo. Una casa ficticia tiene 6 ampolletas, 2 ventiladores y 1 plancha. ¿Cuántos artefactos tienen en total?", "6+2+1", "Se suman todos los artefactos."),
  ],
  rea=[
      ("Ema dice que la ampolleta solo da luz porque no la ha tocado. Una niña mayor dice que también calienta. ¿Qué evidencia puede dar Ema para comprobarlo con seguridad?", "Acercar la mano a distancia, con ayuda de una persona adulta, y sentir el calor", "El calor se percibe a distancia sin tocar la ampolleta."),
      ("Un compañero dice que el ventilador crea energía de la nada. Con lo que sabes, ¿de dónde viene su energía?", "De la energía eléctrica que recibe", "El ventilador la transforma en movimiento."),
  ],
  cha=[
      ("Una linterna a pila ilumina y se calienta un poco. Escribe la cadena: de qué forma de energía a qué formas.", "Química en eléctrica y luego en luz y calor", "La pila entrega energía eléctrica y la ampolleta la transforma."),
      ("Explica por qué no debes hacer experimentos con enchufes.", "Porque la electricidad de la red es peligrosa", "Puede causar daño grave."),
  ],
  context=[("Dato de ejemplo. Una clase observó 5 artefactos descritos en cartas y anotó 2 formas de energía producidas por cada uno. ¿Cuántas anotaciones hicieron?", "10", "5 × 2 = 10.")],
  selfcheck=[("¿Qué transforma una ampolleta?", "Energía eléctrica en luz y calor", "Ilumina y se calienta."), ("Nombra un artefacto que produzca sonido.", "Parlante o timbre", "Transforman la energía eléctrica en sonora."), ("¿Se puede experimentar con enchufes? Responde Sí o No.", "No", "La electricidad de la red es peligrosa.")],
  open_task=task("Con una persona de tu casa, busca cinco artefactos eléctricos. No los toques si están calientes ni los desarmes. Haz una tabla con el nombre, en qué se transforma la energía eléctrica (luz, calor, sonido o movimiento) y una frase de observación. Agrega una interpretación y márcala como suposición.", "Ampolleta: luz y calor. Ventilador: movimiento. Radio: sonido. Plancha: calor. Observación: el ventilador gira y mueve el aire. Interpretación: gasta mucha energía.", ["cinco artefactos", "forma de energía correcta", "observación e interpretación diferenciadas"], ["tabla", "frases"], ["tocar artefactos calientes", "afirmar gasto sin medir"], "Pregunta cómo supo en qué se transformaba la energía en cada caso."),
  reinforce="Escribe tres artefactos de tu casa y en qué forma transforman la energía eléctrica.",
  extend="Explica por qué se dice que una pila transforma energía química en eléctrica.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a plantear preguntas y predicciones sobre qué parte de la energía eléctrica se vuelve luz y cuánta se vuelve calor. Sirve para comparar ampolletas.",
  prior=["Sé que una ampolleta produce luz y calor.", "Sé que una predicción lleva una razón."],
  explain=[
      "No toda la energía eléctrica que recibe una ampolleta se transforma en luz. Una parte se transforma en calor. Una ampolleta antigua de filamento produce mucho calor y poca luz. Una ampolleta LED produce más luz y menos calor para la misma energía eléctrica. Por eso la ampolleta antigua se calienta mucho más.",
      "Una pregunta comprobable es: «¿Cuántos grados sube la temperatura cerca de una ampolleta A y cerca de una ampolleta B tras 10 minutos?». Una predicción: «Subirá más cerca de la ampolleta que produce más calor». Las pruebas deben tener las mismas condiciones: misma distancia, mismo tiempo y mismo lugar. Las ampolletas encendidas nunca se tocan, porque pueden quemar.",
      "Con los datos de ejemplo de esta clase puedes practicar. Si los resultados no coinciden con tu predicción, corriges tu idea. Y recuerda que los datos de un solo caso no representan a todas las ampolletas del mundo.",
  ],
  vocab=[("filamento", "hilo delgado que se pone muy caliente en una ampolleta antigua"), ("LED", "tipo de ampolleta que produce más luz y menos calor"), ("temperatura", "medida de qué tan caliente está algo"), ("grados Celsius", "unidad de la temperatura, con símbolo °C"), ("predicción", "lo que creo que pasará y por qué")],
  worked=[
      ("Predicción con razón", "Una ampolleta A de filamento y una LED B dan la misma luz. ¿Cerca de cuál subirá más la temperatura?", ["La ampolleta de filamento produce más calor.", "La LED produce menos calor.", "Escribo la predicción con su razón."], "Cerca de la A, porque produce más calor"),
      ("Comparar con el mismo criterio", "Datos de ejemplo. Temperatura inicial 20 °C. A los 10 minutos: ampolleta A 32 °C; ampolleta B 24 °C. ¿Cuánto subió cerca de la A?", ["Resto 32 − 20.", "Calculo la diferencia.", "Anoto los grados."], "12 °C"),
  ],
  mistakes=[
      ("Poner una ampolleta más cerca del termómetro que la otra.", "Las distancias distintas cambian el resultado.", "Usa la misma distancia."),
      ("Tocar la ampolleta para sentir cuánto calienta.", "Puede quemar.", "Mide la temperatura del aire cercano o acércate a distancia con ayuda adulta."),
  ],
  rec=[
      ("¿Una ampolleta LED produce más luz o más calor, comparada con la de filamento?", "Más luz", "Aprovecha mejor la energía para luz."),
      ("Con la misma distancia y el mismo tiempo, ¿la comparación es justa?", "Sí", "Se cambia solo la ampolleta."),
      ("Completa con «tocar» o «medir»: para saber cuánto calienta una ampolleta conviene ______ la temperatura.", "Medir", "Tocar puede quemar."),
  ],
  und=[
      ("¿Por qué las pruebas deben tener la misma distancia?", "Para que la diferencia no dependa de la distancia", "Si cambia, no se sabe la causa."),
      ("¿Qué pregunta se puede comprobar? A) ¿Cuántos °C sube la temperatura en 10 minutos? B) ¿Qué ampolleta es más linda?", "A", "La temperatura se mide."),
      ("¿Qué forma de energía aumenta cerca de una ampolleta que se calienta?", "El calor", "Es energía calórica."),
  ],
  app=[
      arith("Dato de ejemplo. Cerca de la ampolleta A la temperatura subió de 20 °C a 32 °C. ¿Cuántos grados subió?", "32-20", "Se resta la temperatura inicial a la final."),
      arith("Dato de ejemplo. Cerca de la ampolleta B subió de 20 °C a 24 °C. ¿Cuántos grados menos subió que la A (que subió 12)?", "12-4", "La B subió 4 grados y la A subió 12."),
      ("Marta predijo que la ampolleta LED se calentaría menos. Los datos de ejemplo muestran A: 12 °C y LED: 4 °C de subida. ¿Se cumplió su predicción? Responde Sí o No.", "Sí", "4 °C es menos que 12 °C."),
  ],
  rea=[
      ("Teo midió la ampolleta A durante 10 minutos y la B durante 5 minutos. Dice que la A calienta más. ¿Qué problema tiene su prueba?", "Los tiempos son distintos", "Debe medir el mismo tiempo."),
      ("Una niña dice que, como la ampolleta A se calienta más, ilumina menos. ¿Qué evidencia necesita para afirmarlo?", "Medir la luz de ambas con el mismo método", "Con calor no basta para afirmar cuánta luz da."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre dos ampolletas, indicando qué medirás.", "¿Cuántos °C sube la temperatura a 20 cm de cada ampolleta en 10 minutos?", "Nombra lo que cambia y lo que se mide."),
      ("Explica por qué sería peligroso comprobar el calor tocando la ampolleta encendida.", "Porque puede quemar", "Las ampolletas de filamento se ponen muy calientes."),
  ],
  context=[("Dato de ejemplo. En 4 grupos, la temperatura cerca de la ampolleta A subió 12, 11, 13 y 12 °C. ¿Cuántos grados sumaron los cuatro datos?", "48", "12 + 11 + 13 + 12 = 48.")],
  selfcheck=[("¿Qué ampolleta produce más calor?", "La de filamento", "Aprovecha menos la energía para luz."),
             ("¿Por qué se miden las dos ampolletas con el mismo método?", "Para que la comparación sea justa", "Así la diferencia viene de la ampolleta."),
             ("¿Se toca una ampolleta encendida? Responde Sí o No.", "No", "La ampolleta encendida puede quemar la piel.")],
  open_task=task("Con los datos de ejemplo de esta clase, haz una tabla con las temperaturas de la ampolleta A (20 °C al inicio y 32 °C a los 10 minutos) y de la ampolleta B (20 °C al inicio y 24 °C a los 10 minutos). Calcula cuánto subió cada una. Escribe una predicción previa, una conclusión y una limitación. No toques ampolletas encendidas.", "Predicción: la A subirá más porque produce más calor. A subió 12 °C y B subió 4 °C. Conclusión: se cumplió. Limitación: son datos de ejemplo de una sola prueba.", ["tabla con dos ampolletas", "cálculo de las subidas", "conclusión y limitación"], ["tabla", "frases"], ["tocar ampolletas", "cambiar el tiempo de medición"], "Pregunta qué mantuvo igual y cómo mejoraría la prueba."),
  reinforce="Escribe una predicción con razón sobre qué ampolleta calienta más una habitación.",
  extend="Explica por qué cambiar ampolletas antiguas por LED puede disminuir el calor y el gasto de electricidad.")

L(OA8, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a usar un diagrama de flujo para mostrar cómo se transforma la energía y a decir qué no muestra. Sirve para seguir el camino de la energía en un artefacto.",
  prior=["Sé qué transformaciones hace un artefacto.", "Sé que un modelo tiene límites."],
  explain=[
      "Un diagrama de flujo de energía muestra qué entra, qué hace el artefacto y qué sale. Entra energía eléctrica; sale luz, calor, sonido o movimiento. Por ejemplo, una ampolleta antigua de filamento recibe 100 unidades de energía eléctrica y entrega unas 5 de luz y unas 95 de calor (valores aproximados de un ejemplo). El total que sale es igual al que entra, porque la energía no se pierde: se transforma.",
      "En una linterna a pila hay una cadena: la pila transforma energía química en eléctrica, y la ampolleta transforma la eléctrica en luz y calor. Se dibuja con flechas: pila → energía eléctrica → ampolleta → luz y calor. Cada flecha dice qué transformación ocurre.",
      "El diagrama tiene límites: usa números aproximados, no muestra cada pieza del artefacto y no dice cuánto cuesta o cuánto dura la pila. Un buen diagrama dice qué muestra y qué deja fuera.",
  ],
  vocab=[("diagrama de flujo", "dibujo con flechas que muestra el camino de la energía"), ("entrada", "lo que recibe un artefacto"), ("salida", "lo que entrega un artefacto"), ("cadena de transformaciones", "serie de cambios de una forma de energía a otra"), ("aproximado", "cercano al valor real pero no exacto")],
  worked=[
      ("Leer el diagrama", "Diagrama de ejemplo: 100 unidades eléctricas → ampolleta → 5 unidades de luz y 95 de calor. ¿Cuánta energía se transformó en calor?", ["Miro la salida de calor.", "Dice 95 unidades.", "Anoto el valor."], "95 unidades"),
      ("Completar una cadena", "Pila → ______ → ampolleta → luz y calor.", ["La pila entrega energía eléctrica.", "La ampolleta la recibe.", "Completo el espacio."], "Energía eléctrica"),
  ],
  mistakes=[
      ("Pensar que la energía desaparece al apagar el artefacto.", "La energía se transforma en otras formas; no desaparece.", "Sigue las flechas hasta el final."),
      ("Creer que el diagrama tiene los valores exactos.", "Son aproximados.", "Escribe que son aproximados."),
  ],
  rec=[
      ("En una linterna, ¿qué entrega la energía eléctrica: la pila o la tapa?", "La pila", "Transforma energía química en eléctrica."),
      ("En el diagrama de la ampolleta, ¿la mayor parte sale como luz o como calor?", "Como calor", "Es 95 de 100 en el ejemplo."),
      ("Completa con «entrada» o «salida»: lo que recibe un artefacto se llama ______.", "Entrada", "La salida es lo que entrega."),
  ],
  und=[
      ("¿Qué muestra un diagrama de flujo de energía?", "Qué energía entra, cómo se transforma y qué sale", "Usa flechas y rótulos."),
      ("¿Cómo es el total de energía que sale de un artefacto comparado con la que entra: igual o menor?", "Igual", "La energía no se pierde, solo se transforma."),
      ("¿Qué no muestra el diagrama? A) Cada pieza interna del artefacto. B) La entrada y la salida.", "A", "Es un límite del diagrama."),
  ],
  app=[
      arith("Dato de ejemplo. Una ampolleta recibe 100 unidades de energía y entrega 5 de luz. ¿Cuántas unidades salen como calor?", "100-5", "El total que sale es igual al que entra."),
      ("Cadena: pila → energía eléctrica → motor → movimiento. ¿Cuántas transformaciones hay en esta cadena?", "2", "Química a eléctrica y eléctrica a movimiento."),
      ("Un parlante recibe 50 unidades eléctricas en un ejemplo y entrega 5 de sonido. ¿Cuántas salen como otras formas?", "45", "50 − 5 = 45."),
  ],
  rea=[
      ("Víctor dice: «La energía de la ampolleta desaparece cuando la apago». ¿Qué le respondes?", "Que se transformó en luz y calor y esas formas siguen en el ambiente", "La energía se conserva y se transforma."),
      ("Un diagrama muestra solo la luz de la ampolleta, sin el calor. ¿Qué parte falta?", "El calor", "La ampolleta también produce calor."),
  ],
  cha=[
      ("Dibuja con palabras una cadena para un ventilador con pila: de qué forma de energía a cuál.", "Pila (química) → energía eléctrica → motor → movimiento", "Cada flecha es una transformación."),
      ("Escribe dos límites de un diagrama de energía con números aproximados.", "Los valores no son exactos y no muestra cada pieza del artefacto", "Un diagrama simplifica."),
  ],
  context=[("Dato de ejemplo. Una clase dibujó 5 diagramas con 3 flechas cada uno. ¿Cuántas flechas dibujaron en total?", "15", "5 × 3 = 15.")],
  selfcheck=[("¿Qué es la entrada de un artefacto?", "Lo que recibe, como la energía eléctrica", "La salida es lo que entrega."), ("¿La energía desaparece cuando se apaga el artefacto?", "No, se transforma", "Cambia a otras formas."), ("¿Por qué se dice que los números del diagrama son aproximados?", "Porque no son valores exactos", "Dependen de cada artefacto.")],
  open_task=task("Dibuja un diagrama de flujo de energía para una linterna: pila → energía eléctrica → ampolleta → luz y calor. Escribe qué transformación hay en cada flecha. Agrega los números de ejemplo: entran 100 unidades eléctricas y salen 20 de luz. Calcula cuánto sale como calor y escribe dos límites.", "Pila (química) → eléctrica → ampolleta → luz y calor. 100 − 20 = 80 unidades de calor. Límites: los números son de ejemplo y no muestra cada pieza.", ["cadena completa", "cálculo del calor", "dos límites"], ["diagrama", "cálculo y frases"], ["decir que la energía desaparece", "olvidar los límites"], "Pregunta qué parte del diagrama es dato y cuál es ejemplo."),
  reinforce="Dibuja el diagrama de flujo de un parlante a pila.",
  extend="Explica por qué la ampolleta LED es más eficiente que la antigua usando un diagrama.")

L(OA8, 4,
  materials="Este cuaderno y lápiz. Los datos de los científicos están escritos en los ejercicios; son aproximados y se recomienda contrastarlos con una fuente confiable.",
  use="Aprenderé algunos aportes de científicos al estudio de la electricidad y a compararlos con un criterio común. Sirve para ver cómo las ideas cambian a lo largo del tiempo.",
  prior=["Sé que la electricidad se transforma en luz, calor, sonido y movimiento.", "Sé comparar con un criterio común."],
  explain=[
      "La electricidad se ha estudiado durante muchos siglos. Según relatos antiguos, hace unos 2.600 años Tales de Mileto notó que el ámbar frotado atraía objetos livianos. En 1600, William Gilbert estudió estos fenómenos de atracción con mucho cuidado y los llamó eléctricos. En 1800, Alessandro Volta construyó la primera pila eléctrica, que dio una fuente continua de electricidad. En 1831, Michael Faraday descubrió que mover un imán cerca de un cable produce corriente, base de los generadores. En 1879, Thomas Edison presentó una ampolleta eléctrica práctica y duradera, con aportes de otros inventores.",
      "Benjamin Franklin, en el siglo XVIII, propuso que el rayo es un fenómeno eléctrico y que un pararrayos puede proteger los edificios. Nunca se debe repetir un experimento con rayos, porque es muy peligroso. Comparar aportes requiere un criterio: por ejemplo, el siglo en que ocurrió o el tipo de aporte (idea, aparato o descubrimiento).",
      "Una línea de tiempo ordena a los científicos de más antiguo a más reciente. Al investigar, conviene contrastar fechas y hechos en varias fuentes confiables, porque algunos relatos mezclan leyenda y datos. En esta clase los datos son aproximados.",
  ],
  vocab=[("pila", "dispositivo que transforma energía química en eléctrica"), ("imán", "objeto que atrae algunos metales"), ("generador", "máquina que produce electricidad"), ("línea de tiempo", "orden de hechos del más antiguo al más reciente"), ("aporte", "contribución que ayuda a avanzar un conocimiento")],
  worked=[
      ("Ordenar en una línea de tiempo", "Ordena de más antiguo a más reciente: Faraday (1831), Volta (1800), Edison (1879).", ["Comparo los años.", "1800 es el menor.", "1879 es el mayor."], "Volta (1800), Faraday (1831), Edison (1879)"),
      ("Aporte de cada uno", "¿Quién construyó la primera pila eléctrica?", ["Recuerdo el invento de 1800.", "Fue una pila.", "Lo hizo Volta."], "Alessandro Volta"),
  ],
  mistakes=[
      ("Decir que Edison inventó la electricidad.", "La electricidad existe en la naturaleza; Edison presentó una ampolleta práctica.", "Di qué aportó cada persona."),
      ("Mezclar el aporte de Volta con el de Faraday.", "Volta hizo la pila y Faraday descubrió la inducción.", "Une cada nombre a su aporte."),
  ],
  rec=[
      ("¿Quién construyó la primera pila: Volta o Faraday?", "Volta", "Su pila es de 1800."),
      ("¿Quién presentó una ampolleta práctica en 1879: Edison o Gilbert?", "Edison", "Su ampolleta duraba mucho."),
      ("Completa con «antiguo» o «reciente»: Tales de Mileto es más ______ que Edison.", "Antiguo", "Vivió hace unos 2.600 años."),
  ],
  und=[
      ("¿Qué descubrió Faraday en 1831?", "Que mover un imán cerca de un cable produce corriente", "Es la base de los generadores."),
      ("¿Para qué sirve una línea de tiempo?", "Para ordenar hechos del más antiguo al más reciente", "Muestra el orden histórico."),
      ("¿Quién estudió con cuidado la atracción del ámbar frotado en 1600? A) Gilbert. B) Edison.", "A", "Edison vivió siglos después."),
  ],
  app=[
      arith("Volta construyó su pila en 1800 y Edison presentó su ampolleta en 1879. ¿Cuántos años pasaron entre ambos hechos?", "1879-1800", "Se resta el año menor al mayor."),
      arith("Faraday hizo su descubrimiento en 1831 y Volta su pila en 1800. ¿Cuántos años pasaron?", "1831-1800", "Se resta el año menor al mayor."),
      ("Ordena de más antiguo a más reciente: Edison, Gilbert, Volta. Escribe los tres nombres.", "Gilbert, Volta, Edison", "Gilbert es de 1600, Volta de 1800 y Edison de 1879."),
  ],
  rea=[
      ("Ema dice: «Edison descubrió la electricidad». ¿Qué corrección haces?", "La electricidad ya existía; Edison presentó una ampolleta práctica", "Los científicos estudian y aprovechan fenómenos que ya existen."),
      ("Un libro dice que un científico hizo todo solo. ¿Por qué conviene buscar otra fuente?", "Porque muchos aportes se hicieron entre varias personas", "Contrastar evita una historia incompleta."),
  ],
  cha=[
      ("Escribe un criterio para comparar los aportes de Volta y Faraday y aplícalo.", "Criterio: tipo de aporte; Volta construyó un aparato y Faraday descubrió un fenómeno", "Se mira lo mismo en los dos."),
      ("¿Por qué no se debe repetir el experimento de Franklin con el rayo?", "Porque es muy peligroso", "El rayo puede causar graves daños."),
  ],
  context=[("Dato de ejemplo. Una clase hizo una línea de tiempo con 6 científicos y escribió 2 datos de cada uno. ¿Cuántos datos escribieron?", "12", "6 × 2 = 12.")],
  selfcheck=[("¿Quién construyó la primera pila eléctrica?", "Alessandro Volta", "Lo hizo en 1800."), ("¿Para qué contrastar fechas en varias fuentes?", "Para comprobar que son correctas", "Algunos relatos mezclan leyenda y datos."), ("¿Se puede repetir el experimento de Franklin con el rayo? Responde Sí o No.", "No", "Es muy peligroso.")],
  open_task=task("Haz una línea de tiempo con Tales de Mileto (hace unos 2.600 años), Gilbert (1600), Volta (1800), Faraday (1831) y Edison (1879). Escribe junto a cada uno su aporte en una frase. Agrega una frase que explique por qué conviene contrastar con fuentes confiables. No necesitas internet.", "Tales: ámbar frotado atrae. Gilbert: estudia con cuidado la atracción del ámbar frotado. Volta: primera pila. Faraday: imán y cable producen corriente. Edison: ampolleta práctica. Contrastar: evita errores de fechas.", ["cinco científicos en orden", "aporte de cada uno", "frase sobre fuentes"], ["línea de tiempo", "frases"], ["decir que Edison inventó la electricidad", "desordenar las fechas"], "Pregunta qué aporte le parece más importante para hoy y por qué."),
  reinforce="Escribe tres científicos de la clase y su aporte.",
  extend="Explica cómo la pila de Volta y el generador de Faraday cambiaron la vida cotidiana.")

L(OA8, 5,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a explicar con evidencia cómo se transforma la energía eléctrica y a reconocer límites. Sirve para dar una explicación completa sobre un artefacto o un aporte científico.",
  prior=["Sé las transformaciones de energía eléctrica.", "Sé qué científicos aportaron al estudio de la electricidad."],
  explain=[
      "Una explicación completa de una transformación dice qué energía entra, qué artefacto la transforma, qué energías salen y qué evidencia lo respalda. Por ejemplo: «El ventilador recibe energía eléctrica y la transforma en movimiento; la evidencia es que las aspas giran y mueven el aire». También puede decir que parte de la energía se transforma en calor.",
      "Para los aportes científicos, la explicación une la persona, su aporte y su efecto: «Volta construyó la primera pila en 1800, lo que permitió tener una fuente continua de electricidad». La evidencia viene de fuentes que se pueden contrastar. En esta clase los datos son aproximados.",
      "Los límites son importantes: los diagramas usan números de ejemplo, los relatos históricos pueden tener versiones distintas y una sola prueba no basta para afirmar algo sobre todos los artefactos. Una buena explicación dice lo que sabemos y lo que no.",
  ],
  vocab=[("explicación", "relato que dice qué pasa y por qué"), ("evidencia", "dato que apoya una explicación"), ("límite", "lo que la evidencia no puede mostrar"), ("fuente confiable", "fuente con autor, fecha y datos comprobables"), ("conservación", "la energía no se pierde, se transforma")],
  worked=[
      ("Completar una explicación", "Completa: «La estufa eléctrica transforma energía eléctrica en ______; la evidencia es que el aire se calienta».", ["Pienso en lo que percibo.", "El aire se calienta.", "La energía se transforma en calor."], "Calor"),
      ("Evidencia y límite", "Un diagrama muestra 100 unidades que entran y 5 de luz que salen de una ampolleta. ¿Qué evidencia da y qué límite tiene?", ["Hay entrada y salida con números.", "Los números son de ejemplo.", "Es un diagrama simple."], "Evidencia: la mayor parte sale como calor. Límite: son valores aproximados"),
  ],
  mistakes=[
      ("Explicar sin decir la energía de entrada y de salida.", "Faltan los datos clave.", "Nombra la entrada y la salida."),
      ("Afirmar algo histórico sin citar la fuente.", "No se puede comprobar.", "Anota la fuente."),
  ],
  rec=[
      ("¿La estufa transforma energía eléctrica en calor o en sonido?", "En calor", "Se usa para calentar."),
      ("¿Quién construyó la primera pila: Volta o Edison?", "Volta", "Lo hizo en 1800."),
      ("Completa con «transforma» o «destruye»: la energía se ______.", "Transforma", "Cambia de forma y no se destruye."),
  ],
  und=[
      ("¿Por qué el diagrama de energía es un modelo?", "Porque simplifica y usa valores aproximados", "No muestra cada detalle."),
      ("¿Qué frase tiene evidencia? A) Las aspas giran y mueven el aire. B) El ventilador es mágico.", "A", "A se observa."),
      ("¿Qué forma de energía sale de un timbre?", "Sonora", "El timbre produce sonido que se oye."),
  ],
  app=[
      ("Ordena la explicación: A) el ventilador transforma la energía en movimiento, B) recibe energía eléctrica, C) las aspas giran. Escribe el orden.", "B, A, C", "Entrada, transformación y evidencia."),
      arith("Una ampolleta recibe 100 unidades y entrega 10 de luz. ¿Cuántas salen como calor?", "100-10", "Lo que no sale como luz sale como calor."),
      ("Cadena: pila → eléctrica → ampolleta → luz y calor. ¿Cuántas formas de energía salen al final?", "2", "Luz y calor."),
  ],
  rea=[
      ("Pía dice que el ventilador crea energía. Corrige con lo que sabes.", "No crea energía; transforma la eléctrica en movimiento", "La energía se transforma."),
      ("Un libro dice que Faraday inventó la ampolleta. ¿Qué harías?", "Contrastar con otras fuentes confiables", "El dato no coincide con lo aprendido."),
  ],
  cha=[
      ("Escribe una explicación de tres frases sobre una linterna a pila.", "La pila transforma energía química en eléctrica; la ampolleta la transforma en luz y calor; la evidencia es que ilumina y se entibia", "Une la cadena con la evidencia."),
      ("Escribe un aporte de Volta con su efecto.", "Construyó la primera pila en 1800 y permitió tener electricidad continua", "Une persona, aporte y efecto."),
  ],
  context=[("Dato de ejemplo. Una clase explicó 4 artefactos y para cada uno escribió 3 frases. ¿Cuántas frases escribieron?", "12", "4 × 3 = 12.")],
  selfcheck=[("¿Qué incluye una explicación de transformación?", "Entrada, artefacto, salida y evidencia", "Así se puede comprobar."), ("¿La energía desaparece al apagar un artefacto?", "No, se transforma", "Cambia a otras formas."), ("¿Por qué contrastar fuentes históricas?", "Porque los relatos pueden tener errores", "Contrastar da seguridad.")],
  open_task=task("Elige uno de estos artefactos: ventilador, estufa eléctrica o linterna a pila. Escribe una explicación de tres frases con la energía que entra, la que sale y la evidencia. Agrega un aporte de un científico de la clase y un límite de tu explicación. No toques artefactos calientes ni conectados.", "Ventilador: recibe energía eléctrica; la transforma en movimiento y un poco de calor; evidencia: las aspas giran y mueven el aire. Aporte: Faraday descubrió cómo producir corriente con imanes. Límite: no medí cuánta energía usa.", ["entrada y salida", "evidencia", "aporte científico y límite"], ["texto de tres frases", "dos frases más"], ["decir que la energía se destruye", "olvidar el límite"], "Pregunta qué parte es evidencia y cuál es suposición."),
  reinforce="Explica en una frase qué transforma un timbre eléctrico.",
  extend="Explica cómo cambió la vida cotidiana desde que existe la ampolleta eléctrica.")

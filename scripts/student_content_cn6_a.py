"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 01 (fotosíntesis) y OA 02 (cadenas y redes alimentarias)."""
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


OA1, OA2 = "CN06 OA 01", "CN06 OA 02"

# ---------------------------------------------------------------- OA 01
L(OA1, 1,
  materials="Este cuaderno y lápiz. Opcional: una planta de tu casa para mirar sus hojas. Los datos del experimento están escritos en cada ejercicio.",
  use="Aprenderé qué necesita una planta para hacer fotosíntesis y a separar lo que se observa de lo que se supone. Sirve para leer bien un experimento.",
  prior=["Sé que las plantas son seres vivos que crecen.", "Sé que una observación es lo que se ve o se cuenta."],
  explain=[
      "La fotosíntesis es el proceso con el que las plantas, las algas y algunas bacterias fabrican su propio alimento. Usan agua, dióxido de carbono (un gas del aire) y energía de la luz. Con ellos producen azúcar y liberan oxígeno. Ocurre sobre todo en las hojas, que tienen clorofila, el pigmento verde que capta la luz.",
      "Para saber qué necesita una planta se hace una investigación experimental. Se arman dos plantas iguales y se cambia solo una condición, por ejemplo la luz. A lo que se cambia se le llama variable que se modifica. Lo demás, como el riego y la maceta, debe mantenerse igual. Así, si hay una diferencia, se puede atribuir a esa condición.",
      "Al leer los resultados hay que separar dos tipos de frases. Una observación se ve o se cuenta, como «hay 5 hojas amarillas». Una interpretación agrega una causa o una idea, como «se pusieron amarillas porque no recibieron luz». La interpretación puede ser buena, pero necesita apoyarse en las observaciones.",
  ],
  vocab=[("fotosíntesis", "proceso con que las plantas fabrican azúcar con agua, dióxido de carbono y luz"), ("clorofila", "pigmento verde de las hojas que capta la luz"), ("dióxido de carbono", "gas del aire que las plantas usan para fotosíntesis"), ("variable", "condición que se puede cambiar o medir en un experimento"), ("interpretación", "explicación o idea que se agrega a lo observado")],
  worked=[
      ("Observación o interpretación", "En un experimento con dos geranios, el geranio P estuvo junto a una ventana y el geranio Q en un clóset. Después de 12 días, una niña anotó: (1) «Q tiene 7 hojas amarillas». (2) «Q se enfermó por falta de luz». ¿Cuál frase es una observación?", ["Pregunto si la frase se puede ver o contar.", "La frase 1 se cuenta: son 7 hojas.", "La frase 2 agrega una causa («falta de luz») que nadie vio."], "La frase 1 es la observación; la 2 es una interpretación"),
      ("Variable que cambia", "Dos lechugas crecen en macetas iguales. Reciben 50 mL de agua cada día. La lechuga M está al sol y la N, bajo una caja de cartón. ¿Qué variable se modifica y cuáles se mantienen?", ["Comparo qué es distinto entre M y N: la luz.", "Las macetas y los 50 mL de agua son iguales.", "Solo cambia una condición."], "Se modifica la luz; el riego y la maceta se mantienen"),
  ],
  mistakes=[
      ("Decir que la fotosíntesis fabrica oxígeno como alimento de la planta.", "El oxígeno se libera; el alimento que se fabrica es el azúcar.", "Recuerda: azúcar se queda como alimento, oxígeno sale."),
      ("Cambiar la luz y también el riego entre dos plantas y concluir que fue la luz.", "Si cambian dos condiciones no se sabe cuál causó la diferencia.", "Cambia una sola condición y deja iguales las demás."),
  ],
  rec=[
      ("¿Qué gas liberan las plantas durante la fotosíntesis?", "Oxígeno", "Es el gas que sale de la planta como producto."),
      ("Completa con «azúcar» o «sal»: la fotosíntesis fabrica ______.", "Azúcar", "La planta fabrica azúcar como alimento."),
      ("¿La frase «la hoja tiene 3 manchas amarillas» es una observación o una interpretación?", "Una observación", "Se puede ver y contar las manchas."),
  ],
  und=[
      ("En un experimento la planta B pasó de 10 hojas verdes a 3 verdes, 5 amarillas y 2 caídas (datos de ejemplo). De estas dos frases, ¿cuál es una interpretación? A) B tiene 5 hojas amarillas. B) B perdió el verde porque no tuvo luz.", "B", "La frase B agrega una causa que no se ve."),
      ("En un experimento se comparan dos plantas: A con luz y B a oscuras, con 100 mL de agua cada una. ¿Por qué se les da la misma cantidad de agua?", "Para que solo cambie la luz", "Así la diferencia se puede atribuir a la luz."),
      ("Entre estas frases, ¿cuántas son interpretaciones? 1) A tiene 10 hojas verdes. 2) B perdió 2 hojas. 3) B sufrió por estar a oscuras. 4) A es más feliz que B.", "2", "Las frases 3 y 4 agregan una causa o un sentimiento que no se puede ver ni contar."),
  ],
  app=[
      arith("La planta A recibió 8 horas de luz al día durante 14 días. ¿Cuántas horas de luz recibió en total?", "8*14", "Se multiplican las horas por día por los días."),
      ("En un experimento se comparan dos plantas: A con luz y B a oscuras, con 100 mL de agua cada una, en macetas iguales. ¿Qué variable se modifica?", "La luz", "Es lo único que es distinto entre A y B."),
      arith("Si en 14 días A conservó las 10 hojas verdes y B solo conservó 3 verdes, ¿cuántas hojas verdes más tiene A que B?", "10-3", "Se resta para comparar las dos plantas."),
  ],
  rea=[
      ("Ana escribe: «B no puede fabricar azúcar, por eso sus hojas se pusieron amarillas». ¿Es una observación o una interpretación? Explica en una frase.", "Una interpretación; el color amarillo se ve, pero la causa se supone", "Que no fabrica azúcar no se observa en las hojas."),
      ("Si la planta B además de estar a oscuras recibiera solo 50 mL de agua y la A recibiera 100 mL, ¿se podría saber si el amarillo se debe a la luz? Responde Sí o No y explica.", "No; cambian dos condiciones a la vez", "No se sabría si fue la luz o el agua."),
  ],
  cha=[
      ("Una familia tiene dos albahacas. La del balcón tiene 24 hojas verdes y la del baño sin ventana tiene 9 (datos de ejemplo), pero la del baño también recibe menos agua. ¿Cuál interpretación es más prudente? A) La falta de luz causó la diferencia. B) La luz o el agua, o ambas, podrían explicar la diferencia.", "B", "Como cambian dos condiciones, no se puede atribuir la diferencia a una sola."),
      ("En un experimento, ¿por qué se repite el mismo riego en ambas plantas durante todos los días?", "Para que el agua no sea otra causa de la diferencia", "Una condición controlada deja de ser explicación posible."),
  ],
  context=[("Dato de ejemplo. Una familia compara dos albahacas: la del balcón soleado tiene 24 hojas verdes y la de un baño sin ventana tiene 9 hojas verdes. ¿Cuántas hojas verdes más tiene la del balcón?", "15", "24 − 9 = 15.")],
  selfcheck=[("¿Qué necesita una planta para hacer fotosíntesis?", "Agua, dióxido de carbono y energía de la luz", "Son los tres requerimientos de la fotosíntesis."), ("¿Qué se produce en la fotosíntesis?", "Azúcar y oxígeno", "El azúcar es el alimento y el oxígeno se libera."), ("¿Cómo se reconoce una interpretación?", "Agrega una causa o idea que no se ve ni se cuenta", "Se distingue de la observación porque no se mide directamente.")],
  open_task=task("Mira estos resultados de un experimento (datos de ejemplo): una espinaca en ventana tiene 14 hojas verdes y 0 amarillas; otra espinaca igual, tapada con una caja negra, tiene 6 verdes y 8 amarillas; ambas recibieron 60 mL de agua al día. Escribe tres observaciones con números y dos interpretaciones, marcando cuál es cuál.", "Observaciones: la de la ventana tiene 14 verdes; la tapada tiene 8 amarillas; ambas recibieron 60 mL. Interpretaciones: la luz ayuda a mantener verdes las hojas; la caja evitó la fotosíntesis.", ["tres observaciones con números", "dos interpretaciones rotuladas", "no mezcla causas dentro de las observaciones"], ["lista de cinco frases rotuladas"], ["poner una causa dentro de una observación", "olvidar que el riego fue igual"], "Pregunta cómo supo que una frase era interpretación y qué dato nuevo la haría más sólida."),
  reinforce="Escribe tres cosas que se puedan ver en una planta y dos que solo se puedan suponer.",
  extend="Explica por qué en un experimento se cambia una sola condición a la vez.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. Los experimentos que se mencionan son descripciones con datos; no necesitas hacerlos.",
  use="Aprenderé a formular una pregunta comprobable y una predicción sobre lo que necesita la fotosíntesis. Sirve para diseñar un experimento justo.",
  prior=["Sé que la fotosíntesis usa agua, dióxido de carbono y luz.", "Sé que en un experimento se cambia una sola condición."],
  explain=[
      "Una pregunta de investigación se puede comprobar si se responde con mediciones u observaciones. «¿Cuántas burbujas libera una planta acuática en un minuto con luz?» se puede comprobar. «¿Qué planta es más linda?» no, porque depende de gustos. Una buena pregunta nombra qué se cambia y qué se mide.",
      "Una predicción dice lo que se cree que ocurrirá y por qué. Por ejemplo: «Si una planta no recibe luz, producirá menos azúcar, porque la luz es la energía de la fotosíntesis». La razón usa lo que ya se sabe: la planta necesita agua, dióxido de carbono y luz. Si falta uno de ellos, la fotosíntesis disminuye o se detiene.",
      "Para probar cada requerimiento se arma un experimento distinto. Para la luz se compara una planta iluminada con una a oscuras. Para el agua se compara una planta regada con otra sin riego. Para el dióxido de carbono, un laboratorio escolar compara aire normal con aire al que se le quitó ese gas. En cada caso las demás condiciones se mantienen iguales.",
  ],
  vocab=[("pregunta comprobable", "pregunta que se responde midiendo u observando"), ("predicción", "lo que se cree que ocurrirá y por qué"), ("requerimiento", "cosa que un proceso necesita para ocurrir"), ("grupo de comparación", "planta que sigue la condición normal para comparar"), ("variable medida", "lo que se mide para saber el resultado")],
  worked=[
      ("Elegir la pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Qué planta tiene el verde más bonito? B) ¿Cuántas hojas amarillas tiene un poroto sin riego después de 10 días?", ["Pregunto si se puede contar o medir.", "En B se cuentan las hojas amarillas.", "En A la respuesta es un gusto."], "B"),
      ("Predicción con razón", "Una planta recibe luz y dióxido de carbono, pero no agua. ¿Qué predices sobre su producción de azúcar y por qué?", ["Recuerdo que el agua es un requerimiento.", "Si falta un requerimiento, el proceso disminuye.", "Escribo qué pasará y la razón."], "Producirá menos azúcar, porque le falta agua"),
  ],
  mistakes=[
      ("Predecir sin dar razón: «le irá mal».", "Sin razón no se puede comprobar ni aprender del resultado.", "Escribe «porque» y usa lo que sabes de la fotosíntesis."),
      ("Hacer una pregunta que depende de gustos, como «¿qué hoja es más linda?».", "No se responde midiendo ni contando.", "Pregunta algo que se pueda contar o medir."),
  ],
  rec=[
      ("¿La predicción se hace antes o después de ver el resultado?", "Antes", "Es lo que se cree que ocurrirá y se comprueba después."),
      ("Completa con «luz» o «sombra»: la fotosíntesis necesita energía de la ______.", "Luz", "La luz es la fuente de energía de la fotosíntesis."),
      ("¿Cuál es una pregunta comprobable? A) ¿Cuántas hojas verdes quedan en la planta tapada? B) ¿Qué planta es más amable?", "A", "Las hojas verdes se pueden contar."),
  ],
  und=[
      ("Para probar que la luz es necesaria, ¿qué se compara? A) Una planta con luz y otra a oscuras. B) Una planta grande y otra pequeña.", "A", "Solo debe cambiar la luz."),
      ("Una predicción dice: «Sin dióxido de carbono el azúcar será menor, porque ese gas es un requerimiento». ¿Qué parte es la razón?", "Porque ese gas es un requerimiento", "La razón va después de «porque»."),
      ("Un grupo de comparación recibe luz, agua y aire normal. ¿Para qué sirve?", "Para comparar con la planta a la que se le quita una condición", "Muestra cómo es el resultado en condiciones normales."),
  ],
  app=[
      arith("Un estudiante predice que una planta sin agua perderá 2 hojas cada 3 días. Si la predicción se cumple, ¿cuántas hojas perderá en 12 días?", "(12//3)*2", "En 12 días hay 4 períodos de 3 días, y cada uno pierde 2 hojas."),
      ("Quieres probar si el agua es necesaria. Tienes dos plantas iguales en macetas iguales, junto a la misma ventana. ¿Qué variable debes cambiar?", "La cantidad de agua", "Se cambia solo lo que se quiere probar."),
      ("Escribe qué se mide para saber si una planta hace menos fotosíntesis, si la planta es acuática y suelta burbujas.", "El número de burbujas por minuto", "Las burbujas de oxígeno indican cuánta fotosíntesis hay."),
  ],
  rea=[
      ("Pedro predice: «Una planta sin luz seguirá igual, porque las plantas no necesitan nada». ¿Su razón es compatible con lo que se sabe? Responde Sí o No.", "No", "Las plantas necesitan agua, dióxido de carbono y luz."),
      ("Dos plantas: la P con luz y agua; la Q con luz y sin agua. Un compañero concluye que la luz no es necesaria porque Q sigue recibiendo luz y se seca. ¿Qué error cometió?", "Probó el agua, no la luz", "En este experimento lo que cambia es el agua, no la luz."),
  ],
  cha=[
      ("Una persona dice: «Si una planta acuática ya no libera burbujas, se detuvo la fotosíntesis». ¿Qué otra posibilidad habría que revisar antes de concluir? A) Que la planta esté muerta o dañada. B) Que el agua sea transparente.", "A", "Sin burbujas hay varias explicaciones posibles; una de ellas es que la planta esté dañada, y por eso hay que revisar antes de concluir."),
      ("¿Cuál pregunta sobre el agua y la fotosíntesis es comprobable? A) ¿Cuántas hojas verdes quedan en una planta sin riego a los 10 días? B) ¿Le da pena a la planta no recibir agua?", "A", "Las hojas verdes se pueden contar y la pena no se mide."),
  ],
  context=[("Dato de ejemplo. Un curso predijo que una planta sin riego perdería hojas. Después de 10 días, la regada tenía 18 hojas verdes y la sin riego 11. ¿Cuántas hojas verdes más tiene la regada?", "7", "18 − 11 = 7, así que la predicción se cumple.")],
  selfcheck=[("¿Qué debe tener una buena predicción?", "Lo que ocurrirá y la razón", "Así se puede comprobar."), ("¿Qué se compara para probar que el agua es necesaria?", "Una planta regada y otra sin riego", "Solo cambia el agua."), ("¿Por qué es útil un grupo de comparación?", "Muestra el resultado en condiciones normales", "Sirve de referencia.")],
  open_task=task("Se quiere saber si la luz es necesaria para la fotosíntesis. Dos plantas de albahaca iguales: una junto a una ventana y otra en un cajón, ambas con 60 mL de agua al día durante 10 días. Escribe una pregunta comprobable, una predicción con su razón y qué mediciones harías (con unidades).", "Pregunta: ¿cuántas hojas verdes tiene cada albahaca a los 10 días? Predicción: la del cajón tendrá menos hojas verdes, porque sin luz hace menos fotosíntesis. Medición: contar hojas verdes y medir los mL de agua diarios.", ["pregunta con algo contable", "predicción con razón", "una medición con unidad"], ["tres frases escritas"], ["no dar razón", "preguntar por gustos"], "Pregunta qué cambiaría su predicción si en la ventana hubiera mucho más calor."),
  reinforce="Convierte «¿Les gusta la luz a las plantas?» en una pregunta comprobable.",
  extend="Escribe una predicción para una planta a la que se le quita el dióxido de carbono y explica por qué.")

L(OA1, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: una hoja de papel para dibujar el modelo.",
  use="Aprenderé a representar con un modelo qué entra y qué sale en la fotosíntesis. Sirve para explicar el proceso con un esquema.",
  prior=["Sé que la fotosíntesis necesita agua, dióxido de carbono y luz.", "Sé que un modelo simplifica y tiene límites."],
  explain=[
      "Un modelo de la fotosíntesis muestra lo que entra y lo que sale. Entran agua y dióxido de carbono, y la planta usa la energía de la luz. Salen azúcar, que la planta usa como alimento y para crecer, y oxígeno. Se puede escribir así: agua + dióxido de carbono, con luz, produce azúcar + oxígeno.",
      "El modelo también dice por dónde entra cada cosa. El agua entra por las raíces y sube hasta las hojas. El dióxido de carbono entra por unos agujeros muy pequeños de las hojas, llamados estomas. La luz es captada por la clorofila, que está en los cloroplastos, estructuras verdes dentro de las células de las hojas. El oxígeno sale por los estomas.",
      "Todo modelo tiene límites. Un esquema con flechas no muestra cuánto entra de cada cosa ni cuánto tarda el proceso. Tampoco muestra que las plantas, además, respiran y usan parte del azúcar. Por eso un buen modelo indica qué simplifica y qué no representa.",
  ],
  vocab=[("estoma", "agujero muy pequeño de la hoja por donde pasan gases"), ("cloroplasto", "estructura verde de la célula vegetal donde ocurre la fotosíntesis"), ("entrada", "lo que ingresa a un proceso"), ("salida", "lo que se produce y sale de un proceso"), ("modelo", "representación simple de un fenómeno")],
  worked=[
      ("Entradas y salidas", "Del grupo «agua, azúcar, dióxido de carbono, oxígeno», ¿cuáles son entradas y cuáles salidas de la fotosíntesis?", ["Recuerdo que la planta toma agua y dióxido de carbono.", "La planta fabrica azúcar y libera oxígeno.", "Separo en dos grupos."], "Entradas: agua y dióxido de carbono. Salidas: azúcar y oxígeno"),
      ("Por dónde entra cada cosa", "Un esquema muestra una hoja con tres flechas: una desde la raíz, otra desde el aire hacia los estomas y otra desde el Sol. ¿Qué entra por cada una?", ["La raíz absorbe agua.", "Los estomas dejan pasar el dióxido de carbono.", "El Sol aporta energía de la luz."], "Raíz: agua. Estomas: dióxido de carbono. Sol: luz"),
  ],
  mistakes=[
      ("Dibujar el oxígeno como una entrada de la fotosíntesis.", "El oxígeno es un producto que sale de la planta.", "Dibuja la flecha del oxígeno saliendo de la hoja."),
      ("Pensar que la planta toma el azúcar del suelo.", "La planta fabrica el azúcar en sus hojas con agua y dióxido de carbono.", "El suelo aporta agua; el azúcar se fabrica en la hoja."),
  ],
  rec=[
      ("¿Por dónde sale el oxígeno de la hoja?", "Por los estomas", "Los estomas dejan pasar gases."),
      ("¿Qué pigmento verde capta la luz?", "La clorofila", "Está en los cloroplastos de las hojas."),
      ("El agua que usa la planta, ¿entra por las raíces o por los estomas?", "Por las raíces", "Las raíces absorben el agua del suelo."),
  ],
  und=[
      ("¿Cuál es una salida de la fotosíntesis? A) Dióxido de carbono. B) Azúcar.", "B", "El dióxido de carbono entra; el azúcar se produce."),
      ("¿Dónde está la clorofila, en las raíces o en los cloroplastos de las hojas?", "En los cloroplastos de las hojas", "Allí se capta la luz para la fotosíntesis."),
      ("Un modelo de flechas no muestra cuánto tarda el proceso. ¿Eso es un límite del modelo? Responde Sí o No.", "Sí", "Un límite es algo que el modelo no representa."),
  ],
  app=[
      ("Cuenta cuántas entradas (sin contar la luz) tiene el modelo: agua + dióxido de carbono → azúcar + oxígeno.", "2", "Son el agua y el dióxido de carbono."),
      ("En un esquema de una hoja se rotulan con letras: A raíz, B estoma, C cloroplasto. ¿Con qué letra se rotula el lugar donde se capta la luz?", "C", "La clorofila está en los cloroplastos."),
      arith("Una hoja tiene 120 estomas en un trozo muy pequeño y se cierran 45 de ellos. ¿Cuántos quedan abiertos?", "120-45", "Se restan los cerrados de los totales."),
  ],
  rea=[
      ("Luisa dibuja una flecha de oxígeno entrando en la planta y otra de azúcar entrando desde el suelo. ¿Cuántos errores tiene su modelo? Cuenta.", "2", "El oxígeno sale y el azúcar se fabrica en la hoja."),
      ("Un modelo escribe «agua + luz → azúcar + oxígeno». ¿Qué falta en las entradas? Responde con una frase.", "El dióxido de carbono", "Sin él la planta no puede fabricar azúcar."),
  ],
  cha=[
      ("Un alumno dice: «Si tapo los estomas con una capa de cera se detiene la fotosíntesis». Con el modelo, ¿qué entrada se bloquearía?", "El dióxido de carbono", "Los estomas dejan entrar ese gas."),
      ("Escribe un límite del modelo «agua + dióxido de carbono → azúcar + oxígeno» y explícalo.", "No muestra cuánto de cada cosa entra", "Un esquema de flechas no entrega cantidades."),
  ],
  context=[("Dato de ejemplo. Una escuela contó 200 estomas en un trozo de hoja y 80 estaban cerrados al mediodía. ¿Cuántos estaban abiertos?", "120", "200 − 80 = 120 estomas abiertos.")],
  selfcheck=[("¿Cuáles son las entradas y las salidas de la fotosíntesis?", "Entradas: agua y dióxido de carbono; salidas: azúcar y oxígeno", "Con luz como energía."), ("¿Qué son los estomas?", "Agujeros pequeños de la hoja por donde pasan gases", "Por ahí entra el dióxido de carbono y sale el oxígeno."), ("¿Por qué un modelo tiene límites?", "Porque simplifica y no muestra todo", "Un esquema no representa cantidades ni tiempos.")],
  open_task=task("Dibuja una hoja grande y rotula con flechas: qué entra (agua, dióxido de carbono, luz), qué sale (azúcar, oxígeno) y por dónde pasa cada cosa (raíz, estomas, clorofila). Escribe debajo un límite de tu dibujo.", "Hoja con flecha de agua desde la raíz, flecha de dióxido de carbono por los estomas, flecha del Sol; flechas de salida: oxígeno por los estomas y azúcar dentro de la hoja. Límite: el dibujo no muestra cuánto azúcar se produce.", ["entradas y salidas bien ubicadas", "indica por dónde pasa cada cosa", "escribe un límite"], ["dibujo rotulado", "frase del límite"], ["poner el oxígeno como entrada", "olvidar el dióxido de carbono"], "Pregunta por qué la flecha del azúcar queda dentro de la hoja y no en el suelo."),
  reinforce="Escribe con tus palabras qué entra y qué sale en la fotosíntesis.",
  extend="Explica por qué las plantas también necesitan respirar, aunque liberen oxígeno al hacer fotosíntesis.")

L(OA1, 4,
  materials="Este cuaderno y lápiz. Los datos del experimento están en cada ejercicio.",
  use="Aprenderé a comparar resultados de un experimento con un criterio. Sirve para decidir cuánta luz hace que una planta acuática produzca más oxígeno.",
  prior=["Sé que la planta libera oxígeno en la fotosíntesis.", "Sé que debo cambiar una sola condición en un experimento."],
  explain=[
      "En un experimento escolar se usa una planta acuática, como la elodea, dentro de un recipiente transparente con agua. Cuando recibe luz, suelta burbujas de oxígeno. Se cuentan las burbujas que salen en un minuto. Más burbujas por minuto indican más fotosíntesis. Ese conteo es el criterio para comparar.",
      "Para comparar bien, se cambia solo la cantidad de luz y se mantienen iguales el agua, la temperatura, el tamaño de la planta y el tiempo de conteo. Se repite la medición, porque un conteo único puede tener errores. Luego se organizan los resultados en una tabla y se buscan patrones: ¿aumenta o disminuye el número de burbujas cuando cambia la luz?",
      "Una conclusión debe decir lo que muestran los datos y nada más. Si con mucha luz salen más burbujas que con poca luz, se concluye que, en este experimento, más luz se relaciona con más oxígeno liberado. No se puede asegurar qué ocurriría con luz extrema, porque no se probó.",
  ],
  vocab=[("criterio", "regla que se usa para comparar y decidir"), ("patrón", "regularidad que se repite en los datos"), ("burbujas por minuto", "medida de cuánto oxígeno libera la planta acuática"), ("repetir la medición", "volver a medir para reducir errores"), ("conclusión", "afirmación apoyada en los datos")],
  worked=[
      ("Leer una tabla", "Una elodea suelta 30 burbujas por minuto a pleno sol, 15 en sombra clara y 5 en sombra oscura (datos de ejemplo). ¿En qué condición hay más fotosíntesis?", ["Uso el criterio: más burbujas, más fotosíntesis.", "Comparo 30, 15 y 5.", "El mayor valor es 30."], "A pleno sol"),
      ("Calcular la diferencia", "Con los mismos datos, ¿cuántas burbujas más por minuto salen a pleno sol que en sombra oscura?", ["Identifico los valores: 30 y 5.", "Resto el menor al mayor.", "30 − 5 = 25."], "25 burbujas más por minuto"),
  ],
  mistakes=[
      ("Concluir con una sola medición.", "Un conteo puede tener un error por casualidad.", "Repite la medición tres veces y usa los tres datos."),
      ("Decir que «más luz siempre produce más oxígeno» sin haberlo probado.", "El experimento solo probó ciertas cantidades de luz.", "Limita la conclusión a lo que se midió."),
  ],
  rec=[
      ("En el experimento con elodea, ¿qué se cuenta?", "Las burbujas por minuto", "Son las burbujas de oxígeno que suelta la planta."),
      ("¿Más burbujas indican más o menos fotosíntesis?", "Más", "El oxígeno liberado es una señal de la fotosíntesis."),
      ("Completa con «patrón» o «error»: una regularidad que se repite en los datos es un ______.", "Patrón", "Se detecta al ordenar los datos."),
  ],
  und=[
      ("Una elodea suelta 24 burbujas por minuto con luz y 0 en la oscuridad (datos de ejemplo). ¿En cuál condición hace fotosíntesis?", "Con luz", "Sin luz no se libera oxígeno."),
      ("¿Por qué se mantiene igual la temperatura del agua en todas las pruebas?", "Para que la luz sea lo único que cambia", "Así la diferencia no se debe a la temperatura."),
      ("¿Por qué conviene repetir la medición?", "Para reducir errores de una sola medida", "Un dato aislado puede no ser confiable."),
  ],
  app=[
      arith("Tres conteos de burbujas por minuto en sombra clara fueron 12, 15 y 18. ¿Cuántas burbujas se contaron en total?", "12+15+18", "Se suman los tres conteos."),
      arith("Con ese total de 45 burbujas en las 3 mediciones de un minuto cada una, ¿cuántas burbujas por minuto salen en promedio?", "45//3", "El promedio es el total dividido en la cantidad de mediciones."),
      ("Datos de ejemplo: sombra oscura 7, oscuridad 0, pleno sol 28, sombra clara 14 burbujas por minuto. Ordena las condiciones de más a menos fotosíntesis.", "Pleno sol, sombra clara, sombra oscura, oscuridad", "Se ordena según el número de burbujas."),
  ],
  rea=[
      ("Un equipo midió una sola vez: 28 burbujas con luz. Otro midió tres veces: 24, 26 y 28. ¿Cuál resultado es más confiable? Responde A para el primero o B para el segundo.", "B", "Con tres mediciones se reduce el efecto de un error."),
      ("Una niña concluye: «Con más luz siempre sale más oxígeno». Solo probó pleno sol, sombra clara y sombra oscura. ¿Su conclusión está bien limitada? Responde Sí o No.", "No", "Solo se puede afirmar para las condiciones probadas."),
  ],
  cha=[
      ("Resultado de un equipo (datos de ejemplo): a pleno sol, 20, 22 y 21 burbujas; en oscuridad, 0, 0 y 0. Calcula el promedio de pleno sol.", "21", "(20 + 22 + 21) ÷ 3 = 21."),
      ("Marca la mejor conclusión. A) La luz es la única cosa que importa. B) En este experimento, más luz se relaciona con más burbujas.", "B", "La B se limita a lo medido."),
  ],
  context=[("Dato de ejemplo. Un curso midió 36 burbujas por minuto a pleno sol y 9 en sombra oscura. ¿Cuántas burbujas más por minuto salen a pleno sol?", "27", "36 − 9 = 27.")],
  selfcheck=[("¿Qué criterio se usa para comparar en el experimento de la elodea?", "El número de burbujas por minuto", "Más burbujas indican más fotosíntesis."), ("¿Qué se mantiene igual al cambiar la luz?", "La temperatura, el agua y el tamaño de la planta", "Así solo cambia la luz."), ("¿Qué debe decir una conclusión?", "Lo que muestran los datos y nada más", "No debe pasar de lo medido.")],
  open_task=task("Un grupo midió burbujas por minuto de una elodea (datos de ejemplo): pleno sol 32, 30 y 34; sombra clara 16, 14 y 15; oscuridad 0, 0 y 0. Calcula el promedio de cada condición, ordénalas y escribe una conclusión limitada a estos datos.", "Promedios: pleno sol 32; sombra clara 15; oscuridad 0. Orden: pleno sol, sombra clara, oscuridad. Conclusión: en este experimento, a más luz salen más burbujas de oxígeno.", ["tres promedios correctos", "orden correcto", "conclusión limitada a los datos"], ["tabla con promedios", "frase de conclusión"], ["usar un solo dato", "afirmar más de lo medido"], "Pregunta qué medición adicional haría más sólida su conclusión."),
  reinforce="Calcula el promedio de 10, 12 y 14 burbujas por minuto.",
  extend="Explica por qué no sabemos qué pasa con luz mucho más fuerte si solo se probaron tres condiciones.")

L(OA1, 5,
  materials="Este cuaderno y lápiz. Los relatos de los científicos están resumidos en la clase.",
  use="Aprenderé a explicar la fotosíntesis con evidencia y a conocer aportes de científicos del pasado. Sirve para comunicar resultados y ver cómo avanza la ciencia.",
  prior=["Sé qué entra y qué sale en la fotosíntesis.", "Sé comparar resultados con un criterio."],
  explain=[
      "El conocimiento sobre la fotosíntesis se construyó con aportes de muchas personas a través del tiempo. En el siglo XVII, Jan Baptist van Helmont plantó un sauce en una maceta con tierra pesada y solo lo regó. Después de cinco años, el árbol pesaba muchísimo más y la tierra casi no había cambiado. Concluyó que el árbol se formó con el agua.",
      "Su conclusión tenía una limitación: no consideró que parte de la planta viene del dióxido de carbono del aire. En 1771, Joseph Priestley observó que una planta de menta en un recipiente cerrado volvía a hacer respirable el aire. En 1779, Jan Ingenhousz mostró que las plantas necesitan luz y que solo las partes verdes liberan oxígeno.",
      "Al comunicar tus resultados, explicas con evidencia: nombras la pregunta, lo que mediste, los datos y una conclusión. También indicas los límites, por ejemplo que no probaste otras condiciones. La ciencia avanza cuando alguien corrige o completa lo que otros ya habían encontrado.",
  ],
  vocab=[("siglo XVII", "los años 1601 a 1700"), ("aporte", "descubrimiento que ayuda a explicar algo"), ("limitación", "algo que la investigación no alcanzó a probar"), ("evidencia", "datos que apoyan una explicación"), ("comunicar", "dar a conocer resultados de forma clara")],
  worked=[
      ("Un aporte y su límite", "Van Helmont concluyó que el sauce creció solo con agua. ¿Qué dato faltó considerar?", ["Recuerdo los requerimientos de la fotosíntesis.", "Además del agua, la planta usa dióxido de carbono.", "Ese gas viene del aire y él no lo midió."], "Faltó considerar el dióxido de carbono del aire"),
      ("Ordenar descubrimientos", "Ordena de más antiguo a más reciente: Ingenhousz (1779), Van Helmont (siglo XVII), Priestley (1771).", ["Ubico el siglo XVII, que es el más antiguo.", "Comparo 1771 y 1779: 1771 es antes.", "Armo la lista."], "Van Helmont, Priestley, Ingenhousz"),
  ],
  mistakes=[
      ("Pensar que un solo científico descubrió toda la fotosíntesis.", "Muchas personas aportaron datos en distintos momentos.", "Nombra qué aportó cada una."),
      ("Concluir sin decir qué no se probó.", "Toda investigación tiene límites.", "Agrega una frase que diga qué falta probar."),
  ],
  rec=[
      ("¿Qué científico mostró que las plantas necesitan luz y que solo las partes verdes liberan oxígeno?", "Ingenhousz", "Lo mostró en 1779."),
      ("Priestley trabajó con una planta de menta. ¿En qué año hizo su observación del aire?", "1771", "Observó que la planta volvía respirable el aire."),
      ("¿Qué planta usó Van Helmont: un sauce o un cactus?", "Un sauce", "Pesó el sauce y la tierra durante cinco años."),
  ],
  und=[
      ("¿Qué concluyó Van Helmont sobre el sauce?", "Que se había formado con el agua", "Su conclusión fue que el agua formó el árbol."),
      ("¿Qué limitación tenía la conclusión de Van Helmont?", "No consideró el dióxido de carbono del aire", "La planta toma ese gas del aire."),
      ("¿Qué muestra la observación de Priestley con la menta?", "Que las plantas pueden renovar el aire", "El aire volvió a ser respirable gracias a la planta."),
  ],
  app=[
      ("¿Qué trabajo es más antiguo: el de Van Helmont (siglo XVII) o el de Ingenhousz (1779)?", "El de Van Helmont", "El siglo XVII corresponde a los años 1600."),
      arith("¿Cuántos años pasaron entre las observaciones de Priestley (1771) e Ingenhousz (1779)?", "1779-1771", "Se restan los años."),
      ("Un afiche dice «La fotosíntesis necesita luz, agua y aire». ¿Qué parte del aire es el requerimiento? Responde con el nombre del gas.", "El dióxido de carbono", "Es el gas del aire que se usa para fabricar azúcar."),
  ],
  rea=[
      ("Una compañera dice que Van Helmont estaba totalmente equivocado. ¿Es correcto? Responde Sí o No y explica en una frase.", "No; acertó en que el agua es necesaria pero le faltó el dióxido de carbono", "Su conclusión fue incompleta, no totalmente falsa."),
      ("Un estudiante comunica solo «la planta sin luz se puso amarilla». Para apoyarlo con evidencia, ¿qué debe agregar: un dato con números o una opinión?", "Un dato con números", "Los números permiten comprobar lo que afirma."),
  ],
  cha=[
      ("Resume en una frase qué aportó Ingenhousz sobre la luz.", "Mostró que las plantas necesitan luz y que solo las partes verdes liberan oxígeno", "Aportó dos ideas: luz y partes verdes."),
      ("Explica por qué sirve conocer los aportes de varios científicos.", "Porque cada uno corrigió o completó lo anterior", "La ciencia avanza sumando evidencia."),
  ],
  context=[("Ingenhousz mostró en 1779 que las plantas necesitan luz. ¿Cuántos años pasaron desde 1779 hasta 2025?", "246", "2025 − 1779 = 246.")],
  selfcheck=[("¿Qué aportó Priestley?", "Observó que una planta renovaba el aire de un recipiente cerrado", "Con su menta, el aire volvía a ser respirable."), ("¿Qué incluye una buena comunicación de resultados?", "Pregunta, datos, conclusión y límites", "Así se puede entender y comprobar."), ("¿Por qué la conclusión de Van Helmont era incompleta?", "No consideró el dióxido de carbono", "Parte del azúcar sale de ese gas.")],
  open_task=task("Escribe un mini informe de cinco líneas con estos datos (de ejemplo): una elodea con luz suelta 28 burbujas por minuto y sin luz 0. Incluye: pregunta, resultado con números, conclusión, un límite y un aporte de un científico de esta clase que se relacione.", "Pregunta: ¿cambia el oxígeno con la luz? Resultado: 28 burbujas con luz y 0 sin luz. Conclusión: la luz es necesaria. Límite: no se probaron otras temperaturas. Aporte: Ingenhousz mostró que las plantas necesitan luz.", ["incluye pregunta y números", "conclusión limitada", "un aporte bien explicado"], ["informe de cinco líneas"], ["omitir el límite", "atribuir mal el aporte"], "Pregunta cómo cambiaría su informe si agregara otra medición."),
  reinforce="Escribe en una línea qué aportó cada científico de la clase.",
  extend="Explica por qué la ciencia necesita que otros revisen y completen los resultados.")

# ---------------------------------------------------------------- OA 02
L(OA2, 1,
  materials="Este cuaderno y lápiz. Los ecosistemas están descritos en el texto.",
  use="Aprenderé qué son los productores, consumidores y descomponedores y a separar lo observado de lo supuesto. Sirve para leer una cadena alimentaria.",
  prior=["Sé que los seres vivos necesitan alimento.", "Sé que las plantas fabrican su alimento con la luz del Sol."],
  explain=[
      "Una cadena alimentaria muestra quién se alimenta de quién. Empieza con un productor, que fabrica su alimento con la energía del Sol: las plantas y el fitoplancton. Luego vienen los consumidores, que se alimentan de otros seres vivos. Los herbívoros comen vegetales y los carnívoros comen animales. Los omnívoros comen ambos. El que come productores es consumidor primario; el que come a un primario es secundario.",
      "Los descomponedores, como hongos y bacterias, se alimentan de restos de seres vivos y los transforman en nutrientes para el suelo. La flecha de una cadena apunta desde lo que es comido hacia quien lo come, porque muestra hacia dónde viaja la energía y la materia. Por ejemplo: pasto → vicuña → puma.",
      "Al observar un ecosistema, una observación es «el puma se comió una vicuña». Una interpretación es «el puma es cruel». Solo la primera es evidencia. Con observaciones se arman cadenas. Si dos observaciones se contradicen, se necesitan más datos antes de concluir.",
  ],
  vocab=[("productor", "ser vivo que fabrica su alimento, como las plantas"), ("consumidor", "ser vivo que se alimenta de otros seres vivos"), ("descomponedor", "ser vivo que se alimenta de restos y devuelve nutrientes"), ("herbívoro", "consumidor que come vegetales"), ("carnívoro", "consumidor que come animales")],
  worked=[
      ("Armar una cadena", "En el altiplano se observa: la vicuña come pasto y el puma come vicuñas. Arma la cadena e indica el productor.", ["Busco quién fabrica su alimento: el pasto.", "La flecha va de lo comido a quien come.", "Pasto → vicuña → puma."], "Pasto → vicuña → puma; el productor es el pasto"),
      ("Observación o interpretación", "Dos frases: (1) «El zorro culpeo comió un conejo». (2) «Al zorro le encanta cazar». ¿Cuál es la observación?", ["Pregunto si se vio.", "La frase 1 es un hecho visto.", "La frase 2 habla de un gusto."], "La frase 1"),
  ],
  mistakes=[
      ("Dibujar la flecha desde el consumidor hacia el alimento.", "La flecha muestra hacia dónde va la energía, desde lo que se come.", "Dibuja la flecha desde lo comido hacia quien come."),
      ("Pensar que el Sol es un productor.", "El Sol aporta energía; los productores son seres vivos que fabrican alimento.", "Marca productores solo a seres vivos."),
  ],
  rec=[
      ("¿Qué ser vivo fabrica su alimento: el pasto o el puma?", "El pasto", "El pasto es un productor."),
      ("Un animal que come solo vegetales, ¿es herbívoro o carnívoro?", "Herbívoro", "Herbívoro significa que come vegetales."),
      ("¿Los hongos que descomponen restos son productores o descomponedores?", "Descomponedores", "Se alimentan de restos de seres vivos."),
  ],
  und=[
      ("En la cadena pasto → conejo → zorro culpeo, ¿quién es el consumidor secundario?", "El zorro culpeo", "Es el carnívoro que se alimenta del herbívoro."),
      ("¿Cuál es una observación? A) La vicuña comió pasto 3 veces en 10 minutos. B) La vicuña es tranquila y feliz.", "A", "La frase A se puede contar."),
      ("¿Qué indica la flecha de una cadena alimentaria?", "Hacia dónde pasan la energía y la materia", "Apunta desde lo comido a quien lo come."),
  ],
  app=[
      ("En un mar frío se observa: el fitoplancton es comido por el krill; el krill es comido por la ballena azul. Escribe la cadena con flechas.", "Fitoplancton → krill → ballena azul", "Se sigue quién come a quién."),
      arith("En una pradera se contaron 40 plantas, 12 conejos y 3 zorros culpeos. ¿Cuántos seres vivos se contaron en total?", "40+12+3", "Se suman todos los conteos."),
      ("Pasto → insecto → lagartija → zorro culpeo. ¿Cuántos consumidores hay en la cadena?", "3", "Son el insecto, la lagartija y el zorro culpeo."),
  ],
  rea=[
      ("Un estudiante dibuja zorro culpeo → conejo → pasto. ¿Qué error tiene? Explica en una frase.", "Las flechas están al revés", "Las flechas deben ir desde lo comido hacia quien come."),
      ("Un grupo anota: «Vimos al zorro comer un conejo» y «El zorro debe sentirse poderoso». ¿Cuál frase debe ir en una tabla de evidencia?", "La primera", "Es lo que se observó."),
  ],
  cha=[
      ("En un bosque austral: hierbas → pudú → puma. Si los descomponedores actúan sobre los restos del puma, ¿qué devuelven al suelo?", "Nutrientes", "Los descomponedores transforman restos en nutrientes."),
      ("Un omnívoro come pasto y también insectos. ¿Puede ubicarse en dos niveles de una cadena? Responde Sí o No.", "Sí", "Come productores y consumidores."),
  ],
  context=[("Dato de ejemplo. En un estero un curso contó 60 algas, 18 renacuajos y 2 garzas. ¿Cuántos seres vivos son consumidores?", "20", "18 + 2 = 20.")],
  selfcheck=[("¿Qué es un productor?", "Un ser vivo que fabrica su alimento", "Las plantas y el fitoplancton son productores."), ("¿Hacia dónde apunta la flecha?", "Desde lo comido a quien lo come", "Muestra el paso de la energía."), ("¿Qué hacen los descomponedores?", "Transforman restos en nutrientes", "Devuelven materia al suelo.")],
  open_task=task("Lee esta lista de observaciones de una laguna: las algas fabrican su alimento con la luz; los renacuajos comen algas; las ranas comen insectos acuáticos; los insectos acuáticos comen algas; las garzas comen ranas. Dibuja dos cadenas distintas con flechas y rotula productor y consumidores. Escribe una interpretación y márcala como tal.", "Alga → renacuajo; alga → insecto acuático → rana → garza. Productor: alga. Interpretación: las garzas dependen de que haya algas.", ["dos cadenas con flechas bien orientadas", "productor y consumidores rotulados", "una interpretación marcada"], ["dibujo de cadenas", "frase rotulada"], ["flechas al revés", "mezclar interpretación con observación"], "Pregunta qué cambiaría si desaparecieran las algas."),
  reinforce="Escribe una cadena de tres seres vivos que conozcas.",
  extend="Explica por qué los descomponedores son necesarios en un ecosistema.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Los datos de ecosistemas están escritos en los ejercicios.",
  use="Aprenderé a hacer preguntas y predicciones sobre redes alimentarias. Sirve para anticipar qué pasa si un organismo aumenta o desaparece.",
  prior=["Sé armar una cadena alimentaria.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una red alimentaria está formada por varias cadenas entrelazadas. Muchos animales comen más de un tipo de alimento y son comidos por más de un depredador. Por eso, un cambio en una población puede afectar a otras. Una población es el conjunto de individuos de una especie que viven en un lugar.",
      "Para predecir, se usa la relación entre los organismos. Si aumentan los conejos, probablemente aumente el alimento para los zorros y su población crezca, mientras el pasto disminuya porque es más consumido. Si desaparecen los zorros, es probable que los conejos aumenten. Se dice «probable», porque en la naturaleza influyen más factores.",
      "Una pregunta comprobable puede ser: «¿Cuántos conejos hay por hectárea antes y después de que disminuya el número de zorros?». Se necesita un registro con números para comprobar la predicción. Una predicción sin razón no basta: siempre se explica con las relaciones de alimentación.",
  ],
  vocab=[("red alimentaria", "conjunto de cadenas alimentarias entrelazadas"), ("población", "conjunto de individuos de una especie en un lugar"), ("depredador", "animal que caza a otro para alimentarse"), ("presa", "animal que es cazado por otro"), ("efecto indirecto", "cambio que llega a un organismo a través de otro")],
  worked=[
      ("Predecir un efecto", "En una red, el zorro culpeo come conejos y los conejos comen pasto. Si disminuyen los zorros, ¿qué predices que pasará con los conejos y el pasto?", ["Menos zorros, menos conejos comidos.", "Más conejos comerán más pasto.", "Predigo que los conejos aumentan y el pasto disminuye."], "Los conejos aumentan y el pasto disminuye, porque hay menos depredadores"),
      ("Pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Qué especie es más importante? B) ¿Cuántos conejos hay por hectárea cada año?", ["Pregunto si se puede contar.", "En B se cuentan conejos.", "En A depende de la opinión."], "B"),
  ],
  mistakes=[
      ("Pensar que un cambio solo afecta a los organismos que se comen directamente.", "También hay efectos indirectos a través de otros organismos.", "Sigue las flechas más allá del primer paso."),
      ("Afirmar con certeza total «los conejos aumentarán».", "En la naturaleza influyen más factores, como el clima.", "Usa «probablemente» y da la razón."),
  ],
  rec=[
      ("Un animal que caza a otro, ¿es depredador o presa?", "Depredador", "El cazador es el depredador."),
      ("Si hay más alimento para un animal, ¿su población probablemente aumenta o disminuye?", "Aumenta", "Con más alimento, más individuos sobreviven."),
      ("¿La red alimentaria tiene una sola cadena o varias entrelazadas?", "Varias entrelazadas", "Muchos animales comen más de un alimento."),
  ],
  und=[
      ("En pasto → conejo → zorro, si desaparecen todos los zorros, ¿qué población probablemente aumenta primero?", "Los conejos", "Ya no los cazan."),
      ("¿Cuál es una predicción con razón? A) Los conejos aumentarán, porque habrá menos zorros. B) Los conejos aumentarán.", "A", "La A explica el motivo."),
      ("En una red con pasto, conejo, ratón y zorro, el zorro come conejos y ratones. Si desaparecen los conejos, ¿el zorro puede sobrevivir con el ratón? Responde Sí o No.", "Sí", "Aún tiene otra fuente de alimento."),
  ],
  app=[
      arith("En una pradera había 90 conejos. Tras una sequía quedó la tercera parte. ¿Cuántos conejos quedaron?", "90//3", "Se divide en 3 partes iguales y queda una."),
      ("Si disminuye mucho el pasto en una red donde lo comen los conejos y los ratones, ¿qué predices que pasará con ambos? Responde con una frase.", "Disminuirán, porque tienen menos alimento", "Dependen del pasto."),
      arith("Un zorro come 4 conejos por semana. ¿Cuántos conejos come en 6 semanas?", "4*6", "Se multiplica por el número de semanas."),
  ],
  rea=[
      ("Rosa predice: «Si hay más zorros, habrá más pasto». ¿Qué razón puede apoyar su idea? Responde con una frase.", "Menos conejos consumen el pasto", "Más zorros comen más conejos, entonces el pasto se come menos."),
      ("Un estudiante dice: «Si desaparecen los zorros, siempre desaparecerá el pasto». ¿Qué palabra de la frase es demasiado fuerte?", "Siempre", "No es seguro que ocurra siempre."),
  ],
  cha=[
      ("En una red, las garzas comen ranas y las ranas comen insectos. Si disminuyen los insectos, ¿qué le pasa probablemente a las garzas, de forma indirecta?", "Disminuyen, porque hay menos ranas", "El efecto llega por medio de las ranas."),
      ("¿Cuál pregunta se puede comprobar contando? A) ¿Es justo que el búho cace? B) ¿Cuántos ratones hay por hectárea cada mes?", "B", "Los ratones se pueden contar; la justicia no se mide."),
  ],
  context=[("Dato de ejemplo. Una reserva registró 120 conejos y 15 zorros en 2023, y 200 conejos y 8 zorros en 2024. ¿Cuántos zorros menos hay en 2024?", "7", "15 − 8 = 7.")],
  selfcheck=[("¿Qué es una red alimentaria?", "Varias cadenas alimentarias entrelazadas", "Los animales comen más de un alimento."), ("¿Qué es un efecto indirecto?", "Un cambio que llega a través de otro organismo", "Pasa por otro eslabón."), ("¿Por qué una predicción debe llevar «probablemente»?", "Porque influyen otros factores", "La naturaleza es variable.")],
  open_task=task("Red de un bosque: el pasto es comido por el conejo y por el ratón; el zorro come conejos y ratones; el búho come ratones. Predice qué pasa con cada población si el ratón disminuye mucho. Escribe tres predicciones con razón.", "Búho: disminuye, porque pierde su alimento. Zorro: come más conejos, porque tiene menos ratones. Pasto: puede disminuir un poco más por los conejos.", ["tres predicciones", "razones basadas en las flechas", "usa probablemente"], ["lista de predicciones"], ["no dar razón", "olvidar efectos indirectos"], "Pregunta qué dato necesitaría para comprobar su predicción."),
  reinforce="Escribe una predicción sobre qué pasa con el pasto si aumentan los conejos.",
  extend="Explica por qué es difícil asegurar un resultado en la naturaleza.")

L(OA2, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a representar con modelos cómo viajan la energía y la materia en una red alimentaria. Sirve para explicar por qué hay menos animales grandes que plantas.",
  prior=["Sé armar cadenas y redes alimentarias.", "Sé que las flechas apuntan desde lo comido a quien come."],
  explain=[
      "La energía entra a casi todos los ecosistemas desde el Sol. Los productores la captan por fotosíntesis y la guardan en el azúcar. Cuando un herbívoro come la planta, parte de esa energía pasa a él. Cuando un carnívoro come al herbívoro, la energía pasa de nuevo. En cada paso se pierde una buena parte como calor, movimiento y funciones de la vida.",
      "Por eso una pirámide de energía se angosta hacia arriba: hay mucha energía en los productores y poca en los consumidores finales. Como ejemplo de un modelo (datos simulados): 1.000 unidades en el pasto, 100 en el conejo y 10 en el zorro. Esto explica por qué hay menos zorros que conejos. Como regla aproximada, pasa cerca de la décima parte (10 %) de un nivel al siguiente.",
      "La materia, en cambio, se recicla. Los nutrientes de los seres vivos pasan a los descomponedores, vuelven al suelo y las plantas los usan de nuevo. La energía fluye en una sola dirección y se pierde; la materia circula. Un modelo con flechas y pirámide ayuda a verlo, pero no muestra todos los organismos ni las cantidades exactas.",
  ],
  vocab=[("pirámide de energía", "esquema que muestra cuánta energía hay en cada nivel"), ("nivel trófico", "escalón de una cadena alimentaria"), ("reciclaje de materia", "paso de nutrientes de seres vivos al suelo y de vuelta a las plantas"), ("pérdida de energía", "energía que se disipa como calor y movimiento"), ("flujo", "paso en una dirección")],
  worked=[
      ("Leer una pirámide", "Una pirámide simulada tiene 5.000 unidades de energía en el pasto, 500 en el saltamontes y 50 en la lagartija. ¿Cuánta energía llega a la lagartija desde el pasto?", ["Comparo el nivel del pasto y el de la lagartija.", "Del pasto al saltamontes, 5.000 pasan a 500.", "Del saltamontes a la lagartija, 500 pasan a 50."], "A la lagartija llegan 50 unidades"),
      ("Energía o materia", "¿Qué se recicla: la energía o los nutrientes?", ["Recuerdo que la energía se disipa.", "Los nutrientes vuelven al suelo con los descomponedores.", "Las plantas los usan de nuevo."], "Se reciclan los nutrientes (la materia)"),
  ],
  mistakes=[
      ("Pensar que la energía vuelve al Sol o se recicla como los nutrientes.", "La energía se disipa y no regresa al mismo ciclo.", "Dibuja la energía con un camino de una sola dirección."),
      ("Dibujar una pirámide con la parte más ancha arriba.", "Hay más energía en los productores.", "El nivel más ancho es el de los productores."),
  ],
  rec=[
      ("¿De dónde viene la energía de casi todos los ecosistemas?", "Del Sol", "Los productores la captan con la fotosíntesis."),
      ("¿Qué nivel de la pirámide es el más ancho: productores o carnívoros?", "Los productores", "Tienen la mayor cantidad de energía."),
      ("La materia, ¿se recicla o se pierde por completo?", "Se recicla", "Los nutrientes vuelven al suelo."),
  ],
  und=[
      ("En una pirámide de 1.000, 100 y 10 unidades, ¿cuál es el nivel con menos energía?", "El de 10 unidades", "Es el nivel final."),
      ("¿Por qué hay menos zorros que conejos?", "Porque en cada paso se pierde energía", "Llega menos energía a los niveles altos."),
      ("¿Quién devuelve los nutrientes al suelo?", "Los descomponedores", "Transforman restos en nutrientes."),
  ],
  app=[
      arith("En una pirámide simulada hay 8.000 unidades en el pasto y solo llega la décima parte al insecto. ¿Cuántas unidades tiene el insecto?", "8000//10", "Se divide en diez partes iguales."),
      arith("Si el insecto tiene 800 unidades y solo la décima parte pasa al ave, ¿cuántas unidades llegan al ave?", "800//10", "De nuevo se calcula la décima parte."),
      ("Escribe el orden correcto de los niveles de una cadena: consumidor secundario, productor, consumidor primario.", "Productor, consumidor primario, consumidor secundario", "Se sigue el camino de la energía."),
  ],
  rea=[
      ("Un compañero dice que la energía de un zorro vuelve a ser energía del pasto. ¿Es correcto? Responde Sí o No y explica.", "No; la energía se disipa", "Lo que se recicla son los nutrientes."),
      ("Un modelo muestra solo flechas entre pasto, conejo y zorro. ¿Qué no muestra? Responde con una frase.", "Las cantidades de energía y los descomponedores", "Un modelo simple no incluye todo."),
  ],
  cha=[
      ("Si un nivel tiene 2.000 unidades y el siguiente tiene 200, ¿qué porcentaje de energía pasó? Responde en porcentaje.", "10%", "200 es la décima parte de 2.000."),
      ("Un ecosistema tiene 5 niveles. ¿Por qué rara vez hay muchos más? Responde con una frase.", "Porque la energía disponible se hace muy pequeña", "En cada paso se pierde una parte."),
  ],
  context=[("Dato de ejemplo. Un estero tiene 6.000 unidades de energía en las algas y 600 en los renacuajos. ¿Cuántas unidades se pierden o no llegan al nivel de los renacuajos?", "5.400", "6.000 − 600 = 5.400.")],
  selfcheck=[("¿La energía fluye o circula?", "Fluye en una dirección y se pierde", "No se recicla."), ("¿Qué se recicla en un ecosistema?", "La materia, los nutrientes", "Vuelven al suelo."), ("¿Por qué la pirámide se angosta?", "Porque cada nivel recibe menos energía", "Hay pérdidas en cada paso.")],
  open_task=task("Dibuja una pirámide de energía de cuatro niveles con estos datos simulados: pasto 10.000, saltamontes 1.000, lagartija 100, zorro culpeo 10. Agrega una flecha de los descomponedores al suelo. Escribe qué muestra el modelo y qué no muestra.", "Pirámide: pasto en la base y zorro culpeo arriba; flecha de descomponedores al suelo. Muestra que la energía disminuye. No muestra todos los organismos.", ["cuatro niveles ordenados", "flecha de descomponedores", "un límite del modelo"], ["dibujo de pirámide", "frase de límite"], ["invertir la pirámide", "olvidar a los descomponedores"], "Pregunta por qué el nivel superior es el más angosto."),
  reinforce="Escribe una cadena de cuatro eslabones y marca cuál tiene menos energía.",
  extend="Explica por qué la energía no se recicla pero la materia sí.")

L(OA2, 4,
  materials="Este cuaderno y lápiz. Los datos de las redes están escritos en los ejercicios.",
  use="Aprenderé a comparar redes alimentarias con un criterio. Sirve para decidir cuál ecosistema resiste mejor la pérdida de una especie.",
  prior=["Sé que una red alimentaria tiene cadenas entrelazadas.", "Sé que los cambios se propagan por las flechas."],
  explain=[
      "Para comparar dos redes alimentarias se usa un criterio, por ejemplo cuántas fuentes de alimento tiene cada consumidor. Si un animal come solo un tipo de alimento, depende de él. Si come cuatro tipos, tiene más opciones. Una red con muchas conexiones suele resistir mejor la desaparición de una especie.",
      "Para aplicar el criterio se cuentan las flechas que llegan a cada consumidor. Se pueden ordenar los resultados en una tabla. Por ejemplo, si el zorro come conejo y ratón, tiene dos fuentes. Si la lechuza solo come ratones, tiene una. Si falta el ratón, la lechuza queda más afectada que el zorro.",
      "Comparar no significa decir que una red es mejor en todo sentido. Significa decidir con un criterio y con datos. También hay límites: el número de flechas no mide cuánto come el animal de cada alimento. Una conclusión debe decir qué criterio usó y cuál es su límite.",
  ],
  vocab=[("criterio", "regla para comparar"), ("fuente de alimento", "organismo del que se alimenta otro"), ("conexión", "flecha que une dos organismos en una red"), ("dependencia", "necesidad de un organismo de otro para vivir"), ("resistir", "mantenerse a pesar de un cambio")],
  worked=[
      ("Contar fuentes", "En la red X: la lechuza come solo ratones; el zorro come ratones y conejos. ¿Cuál tiene más fuentes de alimento?", ["Cuento las flechas que llegan a cada uno.", "Lechuza: 1. Zorro: 2.", "Comparo."], "El zorro tiene más fuentes (2 contra 1)"),
      ("Aplicar el criterio", "Si desaparecen los ratones, ¿cuál de los dos queda más afectado y por qué?", ["La lechuza solo comía ratones.", "El zorro aún tiene los conejos.", "Quien tiene menos fuentes queda más afectado."], "La lechuza, porque no tiene otro alimento"),
  ],
  mistakes=[
      ("Decir que una red es mejor porque tiene más animales grandes.", "El criterio es la cantidad de conexiones, no el tamaño.", "Cuenta las flechas por consumidor."),
      ("Usar dos criterios a la vez sin decirlo.", "La comparación se vuelve confusa.", "Declara un solo criterio por comparación."),
  ],
  rec=[
      ("Un animal que come tres tipos de alimento, ¿tiene más o menos opciones que uno que come uno solo?", "Más", "Tiene tres fuentes."),
      ("¿Qué se cuenta para comparar conexiones: las flechas o los colores?", "Las flechas", "Cada flecha es una relación de alimento."),
      ("Completa con «criterio» o «dibujo»: la regla para comparar es el ______.", "Criterio", "Define cómo se decide."),
  ],
  und=[
      ("En la red Y, el pudú come hierbas, hojas y brotes. ¿Cuántas fuentes tiene?", "3", "Come tres tipos de alimento."),
      ("¿Qué consumidor resiste mejor la desaparición de un alimento: el que tiene 1 fuente o el que tiene 4?", "El que tiene 4", "Si una falta, le quedan 3."),
      ("¿Por qué el número de flechas no lo dice todo?", "Porque no muestra cuánto se come de cada alimento", "Es un límite del criterio."),
  ],
  app=[
      arith("La red A tiene 5 consumidores y cada uno tiene 2 fuentes de alimento. ¿Cuántas flechas de alimentación hay en total?", "5*2", "Se multiplican consumidores por fuentes."),
      arith("La red B tiene 5 consumidores y 17 flechas. ¿Cuántas flechas más que la red A (10 flechas) tiene?", "17-10", "Se restan las flechas."),
      ("La red A tiene 10 flechas y la red B tiene 17 (con el mismo número de consumidores). Con el criterio de conexiones, ¿cuál es más resistente?", "La red B", "Tiene más fuentes por consumidor."),
  ],
  rea=[
      ("Dos redes tienen 6 flechas cada una. En la primera, un solo consumidor recibe las 6; en la segunda, tres consumidores reciben 2 cada uno. ¿Cuál sería más resistente si falla un alimento? Explica.", "La segunda; reparte las conexiones", "Si falla un alimento, ninguno se queda sin nada."),
      ("Un compañero dice que la red con más especies es siempre mejor. Escribe una razón por la que esa idea es débil.", "Porque pueden tener pocas conexiones", "El criterio es la cantidad de conexiones."),
  ],
  cha=[
      ("En la red C, el ave come insectos y frutos; el insecto come hojas; los frutos vienen del árbol. Si no hay frutos en un invierno, ¿el ave se queda sin alimento? Responde Sí o No y explica.", "No; puede comer insectos", "Tiene otra fuente."),
      ("Un animal tiene 2 fuentes de alimento y otro tiene 5. ¿Cuál conclusión está mejor limitada? A) El de 5 resiste mejor un cambio, según el número de fuentes. B) El de 5 nunca tendrá problemas.", "A", "La B afirma algo que el criterio no prueba."),
  ],
  context=[("Dato de ejemplo. Un parque tiene una red con 24 flechas y otra con 15. ¿Cuántas flechas más tiene la primera?", "9", "24 − 15 = 9.")],
  selfcheck=[("¿Qué criterio se usó para comparar redes?", "El número de fuentes de alimento por consumidor", "Se cuentan las flechas."), ("¿Qué consumidor está más en riesgo si desaparece un alimento?", "El que tiene una sola fuente", "No tiene alternativas."), ("¿Qué límite tiene el criterio?", "No dice cuánto se come de cada alimento", "Solo cuenta conexiones.")],
  open_task=task("Compara dos redes (datos de ejemplo). Red 1: el puma come solo vicuñas; la vicuña come pasto. Red 2: el puma come vicuñas, guanacos y liebres; vicuñas y guanacos comen pasto y las liebres comen hierbas. Cuenta las fuentes del puma en cada red, escribe cuál resiste mejor la pérdida de las vicuñas y un límite.", "Red 1: 1 fuente. Red 2: 3 fuentes. La red 2 resiste mejor porque el puma puede comer guanacos y liebres. Límite: no sabemos cuánto come de cada uno.", ["cuenta bien las fuentes", "usa el criterio", "escribe un límite"], ["tabla de conteo", "conclusión escrita"], ["comparar sin criterio", "olvidar el límite"], "Pregunta qué pasaría si también faltara el pasto."),
  reinforce="Cuenta las fuentes de alimento de un animal que elijas de esta clase.",
  extend="Explica por qué una red con más conexiones suele resistir mejor los cambios.")

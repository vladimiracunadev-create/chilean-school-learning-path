"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 09 (la materia tiene masa y ocupa espacio) y OA 10 (estados de la materia)."""
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


OA9, OA10 = "CN04 OA 09", "CN04 OA 10"

# ---------------------------------------------------------------- OA 09
L(OA9, 1,
  materials="Este cuaderno y lápiz. Objetos seguros de tu casa: una piedra lisa, una esponja, un vaso de plástico, una bolsa de plástico y una botella de plástico (la bolsa nunca se acerca a la cara).",
  use="Aprenderé qué es la materia y a separar lo que observo de lo que supongo. Sirve para distinguir lo que es materia de lo que no lo es.",
  prior=["Sé que hay objetos livianos y pesados.", "Sé que una observación se ve, se toca o se mide."],
  explain=[
      "La materia es todo lo que tiene masa y ocupa espacio. La masa es la cantidad de materia que tiene un objeto. Una piedra, el agua, la madera y el aire son materia. Tienen masa y ocupan un lugar, aunque en el aire no lo veamos.",
      "No todo es materia. La luz, el sonido, el calor y las ideas no tienen masa ni ocupan espacio. Una linterna prendida ilumina la pieza, pero la luz no se puede pesar ni llenar un vaso.",
      "Para explorar la materia observo con cuidado. Puedo levantar una piedra y una esponja del mismo tamaño y sentir cuál tiene más masa. Eso es una observación. Decir «la piedra es más bonita» es una opinión. Anoto solo lo que veo, toco o mido.",
  ],
  vocab=[("materia", "todo lo que tiene masa y ocupa espacio"), ("masa", "cantidad de materia que tiene un objeto"), ("espacio", "lugar que ocupa algo"), ("observación", "lo que veo, toco o mido"), ("opinión", "lo que pienso o siento sin poder medirlo")],
  worked=[
      ("¿Es materia?", "¿Una piedra es materia? ¿Y la luz de una linterna?", ["Pregunto: ¿tiene masa y ocupa espacio?", "La piedra sí: se puede pesar y ocupa lugar.", "La luz no se puede pesar ni ocupa lugar."], "La piedra es materia; la luz no"),
      ("Observación u opinión", "«La piedra es más pesada que la esponja» y «La piedra es más linda». ¿Cuál es observación?", ["Reviso qué se puede comprobar.", "Pesada se puede sentir y medir.", "'Linda' es una opinión."], "La piedra es más pesada que la esponja"),
  ],
  mistakes=[
      ("Pensar que el aire no es materia porque no se ve.", "El aire tiene masa y ocupa espacio.", "Recuerda las dos condiciones: masa y espacio."),
      ("Pensar que la luz es materia.", "La luz no tiene masa ni ocupa espacio.", "Pregunta: ¿se puede pesar o llenar un vaso?"),
  ],
  rec=[
      ("¿Una piedra es materia, sí o no?", "Sí", "Tiene masa y ocupa espacio."),
      ("¿La luz es materia, sí o no?", "No", "No tiene masa ni ocupa espacio."),
      ("Completa con «masa» o «luz»: la cantidad de materia que tiene un objeto es su ______.", "Masa", "Esa es la definición."),
  ],
  und=[
      ("¿Cuál es materia? A) El agua de un vaso. B) El sonido de un aplauso.", "A", "El agua tiene masa y ocupa espacio."),
      ("¿Cuáles dos cosas debe tener algo para ser materia?", "Masa y ocupar espacio", "Esas son las dos condiciones."),
      ("¿Por qué el aire es materia aunque no se vea?", "Porque tiene masa y ocupa espacio", "Se puede comprobar con experimentos."),
  ],
  app=[
      ("Clasifica: madera, calor, agua, sonido, arena. ¿Cuántas de estas son materia?", "3", "Madera, agua y arena son materia; calor y sonido no."),
      ("Clasifica: una esponja y una piedra del mismo tamaño. Si levantas una en cada mano, ¿cuál tiene más masa? Elige: piedra o esponja.", "Piedra", "Pesa más porque tiene más materia en el mismo espacio."),
      arith("Una bolsa tiene 3 piedras y otra tiene 4 piedras. ¿Cuántas piedras hay en total?", "3+4", "Se suman las piedras de ambas bolsas."),
  ],
  rea=[
      ("Ema dice que la sombra es materia porque se ve. ¿Tiene razón? Responde Sí o No y explica.", "No; la sombra no tiene masa ni ocupa espacio", "Verse no basta para ser materia."),
      ("Un niño dice que el aire de un globo es materia. ¿Qué dos comprobaciones harías? Responde 'masa y espacio' o 'color y olor'.", "Masa y espacio", "Esas son las condiciones de la materia."),
  ],
  cha=[
      ("Escribe una observación y una opinión sobre una piedra y una esponja.", "Observación: la piedra es más dura que la esponja. Opinión: la esponja es más agradable", "Una se comprueba; la otra no."),
      ("Escribe dos ejemplos de materia y dos que no lo sean.", "Materia: agua y madera. No materia: luz y sonido", "Los primeros tienen masa y ocupan espacio."),
  ],
  context=[("En una mesa hay 2 piedras, 3 esponjas, 1 vaso vacío y 1 linterna encendida. Sin contar la luz, ¿cuántos objetos materiales hay?", "7", "2 + 3 + 1 + 1 = 7; la luz de la linterna no cuenta, pero la linterna y el vaso sí son materia.")],
  selfcheck=[("¿Qué es la materia?", "Todo lo que tiene masa y ocupa espacio", "Esa es la definición."), ("¿Qué es la masa?", "La cantidad de materia que tiene un objeto", "Se mide con una balanza."), ("Nombra una cosa que no sea materia.", "Luz, sonido o calor", "No tienen masa ni ocupan espacio.")],
  open_task=task("Reúne con una persona adulta cinco objetos seguros de tu casa (por ejemplo: piedra lisa, esponja, vaso de plástico, hoja de papel y un trozo de madera). Haz una tabla con tres columnas: objeto, ¿tiene masa? y ¿ocupa espacio? Levanta cada uno y escribe una observación. Escribe también dos cosas que no son materia. No uses objetos filosos ni muy pequeños.", "Piedra: sí, sí; se siente pesada. Esponja: sí, sí; se siente liviana. No son materia: la luz y el sonido.", ["cinco objetos en la tabla", "una observación por objeto", "dos ejemplos de lo que no es materia"], ["tabla completa"], ["incluir la luz como materia", "anotar opiniones"], "Pregunta cómo sabe que ocupa espacio."),
  reinforce="Escribe diez cosas que veas en tu pieza y marca cuáles son materia.",
  extend="Escribe una pregunta que se pueda probar sobre la masa de dos objetos de tu casa.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Una balanza de cocina si tienes (si no, una percha con una bolsita colgada de cada extremo, sostenida de un cordel desde un lugar firme con ayuda de una persona adulta).",
  use="Aprenderé a hacer preguntas y predicciones para medir la masa con una balanza. Sirve para comparar cuánta materia tienen los objetos.",
  prior=["Sé que la masa es la cantidad de materia.", "Sé que una predicción se hace antes de probar."],
  explain=[
      "La masa se mide con una balanza. En una balanza de cocina el objeto se apoya y el número que aparece es su masa. Se mide en gramos (g) y en kilogramos (kg). 1 kg son 1.000 g. Una manzana pequeña tiene alrededor de 150 g.",
      "Una pregunta comprobable puede ser: «¿Tiene más masa una piedra que un trozo de esponja del mismo tamaño?». La predicción: «La piedra tendrá más masa, porque tiene más materia en el mismo espacio». Después se mide cada objeto y se compara.",
      "Si no tienes balanza, puedes usar una percha como balanza de brazos. Se cuelga un objeto en cada extremo. El lado que baja tiene más masa. Si queda parejo, tienen casi igual masa. Para que sea justo, los objetos deben colgarse de la misma forma.",
  ],
  vocab=[("balanza", "instrumento para medir la masa"), ("gramo (g)", "unidad para medir masa pequeña"), ("kilogramo (kg)", "unidad de masa: 1 kg son 1.000 g"), ("comparar", "mirar dos cosas para ver cuál tiene más o menos"), ("medición", "valor que se obtiene al medir")],
  worked=[
      ("Comparar masas", "Datos de ejemplo. Piedra: 120 g. Esponja: 8 g. ¿Cuántos gramos más tiene la piedra?", ["El criterio es la masa en g.", "Resto 120 − 8.", "Escribo el resultado con unidad."], "112 g más"),
      ("Leer una balanza de brazos", "En una percha, el lado de la piedra baja y el lado de la esponja sube. ¿Cuál tiene más masa?", ["El lado que baja tiene más masa.", "Baja el lado de la piedra.", "La piedra tiene más masa."], "La piedra"),
  ],
  mistakes=[
      ("Pensar que lo más grande siempre tiene más masa.", "Un objeto grande puede tener poca masa, como una esponja grande.", "Mide con la balanza."),
      ("Colgar los objetos de forma distinta en la balanza de brazos.", "La medición no es justa.", "Cuelga ambos del mismo modo."),
  ],
  rec=[
      ("¿Con qué instrumento medimos la masa?", "Con una balanza", "Mide cuánta materia hay."),
      ("¿Un kilogramo son 1.000 g o 100 g?", "1.000 g", "1 kg equivale a 1.000 gramos."),
      ("En una balanza de brazos, ¿el lado que baja tiene más o menos masa?", "Más", "Pesa más ese lado."),
  ],
  und=[
      ("¿Cuál pregunta se puede comprobar? A) ¿Cuántos gramos tiene una piedra? B) ¿Qué objeto es más bonito?", "A", "Se mide con una balanza."),
      ("¿Por qué conviene medir en vez de solo levantar?", "Porque la medición da un valor que se puede comparar", "Levantar es una impresión."),
      ("¿Por qué una esponja grande puede tener menos masa que una piedra pequeña?", "Porque la esponja tiene menos materia", "El tamaño no decide la masa."),
  ],
  app=[
      arith("Datos de ejemplo. Una manzana tiene 150 g y una pera 180 g. ¿Cuántos gramos tienen entre las dos?", "150+180", "Se suman las masas."),
      arith("Datos de ejemplo. Una caja tiene 2 kg. ¿Cuántos gramos son? (1 kg son 1.000 g)", "2*1000", "Se multiplican los kilogramos por 1.000."),
      ("Predice: en una balanza de brazos hay un trozo de madera pequeño y una piedra del mismo tamaño. ¿Cuál lado bajará probablemente? Elige: madera o piedra.", "Piedra", "La piedra suele tener más masa."),
  ],
  rea=[
      ("Ana dice: 'Como la esponja es más grande que la piedra, pesa más'. Datos de ejemplo: esponja 10 g, piedra 120 g. ¿Tiene razón? Responde Sí o No y explica.", "No; la piedra tiene más masa aunque sea más pequeña", "Los datos lo muestran."),
      ("Luis usa una balanza y mide la piedra 120 g. Luego mide otra vez 121 g. ¿Es normal tener una diferencia pequeña? Responde Sí o No.", "Sí", "Las mediciones pueden variar un poco."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre masa y qué instrumento usarás.", "¿Tiene más masa una naranja o una manzana? Usaré una balanza", "La pregunta se resuelve midiendo."),
      ("Datos de ejemplo. Una bolsa con arena pesa 500 g y una bolsa con la misma arena y una piedra pesa 620 g. ¿Cuántos gramos tiene la piedra?", "120 g", "620 − 500 = 120 g."),
  ],
  context=[("Una niña pesa 3 objetos: 150 g, 220 g y 80 g. ¿Cuál es la masa total de los tres?", "450", "150 + 220 + 80 = 450 g.")],
  selfcheck=[("¿En qué unidades se mide la masa?", "En gramos y kilogramos", "Son las unidades vistas."), ("¿Qué instrumento mide la masa?", "La balanza", "Muestra la cantidad de materia."), ("¿Cómo sabes cuál objeto tiene más masa en una balanza de brazos?", "El lado que baja", "Ese lado pesa más.")],
  open_task=task("Con una persona adulta, elige tres objetos seguros de tu casa (por ejemplo: una manzana, un vaso de plástico lleno de arena y una esponja). Escribe tu predicción de cuál tendrá más masa y por qué. Mide cada uno con una balanza de cocina y anota los gramos. Si solo tienes la balanza de percha, compáralos de a dos y anota cuál lado baja. Anota los resultados en una tabla y escribe una conclusión prudente.", "Predicción: el vaso con arena tendrá más masa. Resultado: vaso con arena 300 g, manzana 150 g, esponja 10 g. Conclusión: en estos objetos, la arena tiene más masa.", ["predicción con razón", "tres mediciones", "conclusión prudente"], ["tabla de tres filas"], ["comparar solo por tamaño", "no anotar unidades"], "Pregunta qué predijo y si el resultado lo sorprendió."),
  reinforce="Pesa tres objetos de tu casa y ordénalos de menos a más masa.",
  extend="Escribe una pregunta que se pueda probar sobre la masa de líquidos y de sólidos.")

L(OA9, 3,
  materials="Este cuaderno, lápiz y regla. Un vaso de plástico transparente con agua, una piedra lisa que quepa en el vaso, un plumón para marcar el nivel. Opcional: una bolsa de plástico.",
  use="Aprenderé a mostrar que la materia ocupa espacio comparando cuánta agua sube cuando entran objetos. Sirve para medir el espacio que ocupa un objeto.",
  prior=["Sé que la materia ocupa espacio.", "Sé comparar con un criterio."],
  explain=[
      "Dos objetos no pueden ocupar el mismo lugar al mismo tiempo. Si pones una piedra dentro de un vaso con agua, la piedra ocupa un lugar y el agua sube. Mientras más espacio ocupa el objeto, más sube el nivel del agua. Así se comprueba que la materia ocupa espacio.",
      "Para comparar dos objetos, marcamos el nivel inicial del agua y luego el nivel con el objeto. Medimos cuántos milímetros subió. Usamos el mismo vaso y la misma cantidad de agua en ambos casos. Esa es la prueba justa: solo cambia el objeto.",
      "El aire también ocupa espacio. Una bolsa de plástico abierta que se agita en el aire y se cierra atrapa aire. La bolsa se hincha. Si intentas apretarla, sientes que algo la llena. Ese algo es aire. Por seguridad, una bolsa de plástico nunca se acerca a la cara ni se pone en la cabeza. Lo que ocupa espacio y tiene masa es materia.",
  ],
  vocab=[("nivel", "altura a la que llega el agua"), ("desplazar", "mover algo de su lugar"), ("prueba justa", "prueba donde cambia una sola cosa"), ("milímetro (mm)", "unidad pequeña para medir longitud"), ("hincharse", "llenarse de aire y ponerse más grande")],
  worked=[
      ("Medir el espacio", "Datos de ejemplo. Nivel inicial: 40 mm. Con la piedra: 52 mm. ¿Cuántos milímetros subió?", ["Resto el nivel inicial al final.", "52 − 40.", "Escribo el resultado con unidad."], "12 mm"),
      ("Comparar objetos", "Datos de ejemplo. La piedra A subió el agua 12 mm y la piedra B la subió 20 mm. ¿Cuál ocupa más espacio?", ["Comparo 12 y 20.", "20 es mayor.", "B movió más agua."], "La piedra B"),
  ],
  mistakes=[
      ("Pensar que el agua sube porque la piedra pesa más.", "Sube porque la piedra ocupa espacio, no por su peso.", "Mide cuánto sube el nivel."),
      ("Usar vasos distintos para cada objeto.", "El resultado depende del vaso.", "Usa el mismo vaso y el mismo nivel inicial."),
  ],
  rec=[
      ("Si metes una piedra en un vaso con agua, ¿el agua sube o baja?", "Sube", "La piedra ocupa un lugar."),
      ("¿Dos objetos pueden ocupar el mismo lugar a la vez, sí o no?", "No", "La materia ocupa un lugar propio."),
      ("Completa con «mismo» o «distinto»: para comparar, uso el ______ vaso y la misma cantidad de agua.", "Mismo", "Así la prueba es justa."),
  ],
  und=[
      ("¿Qué muestra que una piedra ocupa espacio? A) Que el agua sube al meterla. B) Que la piedra es dura.", "A", "El agua sube porque no cabe en el mismo lugar."),
      ("¿Qué objeto hará subir más el agua: uno que ocupa más espacio o uno que ocupa menos?", "El que ocupa más espacio", "Desplaza más agua."),
      ("¿Cómo se puede mostrar que el aire ocupa espacio?", "Atrapándolo en una bolsa, que se hincha", "La bolsa se llena de aire."),
  ],
  app=[
      arith("Datos de ejemplo. Nivel inicial: 35 mm. Con una piedra pequeña: 42 mm. ¿Cuántos milímetros subió?", "42-35", "Se resta el nivel inicial al final."),
      arith("Datos de ejemplo. La piedra A subió 9 mm y la piedra B subió 14 mm. ¿Cuántos milímetros más subió B?", "14-9", "Se resta el valor menor al mayor."),
      ("Predice: si pones dos piedras iguales en el vaso, en vez de una, ¿el agua subirá más o menos que con una?", "Más", "Dos piedras ocupan más espacio."),
  ],
  rea=[
      ("Mario dice que la piedra pesada hace subir más el agua que una piedra liviana del mismo tamaño. ¿Tiene razón? Responde Sí o No y explica.", "No; sube igual porque ocupan el mismo espacio", "El agua sube por el espacio, no por la masa."),
      ("Ana mide una piedra en un vaso grande y otra en un vaso angosto. El agua sube distinto. ¿Puede comparar el espacio de las piedras? Responde Sí o No y explica.", "No; los vasos son distintos", "La prueba no es justa."),
  ],
  cha=[
      ("Diseña una prueba justa para comparar el espacio de dos objetos con el vaso de agua. Escribe qué dejas igual.", "Uso el mismo vaso y el mismo nivel de agua; mido cuánto sube con cada objeto", "Solo cambia el objeto."),
      ("Explica con tus palabras por qué el agua sube cuando entra una piedra.", "Porque la piedra ocupa un lugar y el agua no puede estar en el mismo", "Dos cosas no ocupan el mismo lugar."),
  ],
  context=[("En un experimento, el agua del vaso estaba a 30 mm. Con una piedra subió a 48 mm y con otra subió a 41 mm. ¿Cuántos milímetros más subió con la primera piedra?", "7", "La primera subió 18 mm y la segunda 11 mm; 18 − 11 = 7.")],
  selfcheck=[("¿Por qué sube el agua al meter una piedra?", "Porque la piedra ocupa espacio", "El agua es empujada hacia arriba."), ("¿Qué debe ser igual en una prueba justa?", "El vaso y el nivel inicial del agua", "Solo cambia el objeto."), ("¿Cómo muestras que el aire ocupa espacio?", "Con una bolsa que se hincha", "El aire la llena.")],
  open_task=task("Con una persona adulta, marca con plumón el nivel del agua en un vaso de plástico. Mete una piedra lisa y marca el nuevo nivel. Mide cuántos milímetros subió. Repite con un objeto distinto que se hunda (una cuchara de metal, por ejemplo). Anota tus mediciones y escribe una conclusión. No uses vidrio ni objetos que se rompan.", "Piedra: subió 10 mm. Cuchara: subió 4 mm. Conclusión: la piedra ocupa más espacio que la cuchara. Limitación: medí con regla.", ["nivel inicial y final", "dos mediciones", "conclusión que usa los datos"], ["tabla con tres columnas"], ["usar vasos distintos", "no marcar el nivel inicial"], "Pregunta qué objeto desplazó más agua y por qué."),
  reinforce="Atrapa aire en una bolsa de plástico pequeña agitándola, ciérrala sin acercarla a tu cara y dibuja lo que observas.",
  extend="Escribe una prueba que muestre que el aire ocupa espacio y que no use globos.")

L(OA9, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: balanza de cocina, vaso de plástico y bolsa de plástico.",
  use="Aprenderé a explicar con evidencia que la materia tiene masa y ocupa espacio, y a decir los límites de mis pruebas. Sirve para comunicar un experimento con claridad.",
  prior=["Sé medir masa con una balanza.", "Sé que la materia ocupa espacio."],
  explain=[
      "Una buena explicación científica usa dos pruebas. Una para la masa: la materia se puede medir con una balanza y tiene un valor en gramos. Otra para el espacio: la materia desplaza agua o llena un espacio, como el aire en una bolsa.",
      "Para explicar con un modelo puedo usar un dibujo de un vaso con agua antes y después de meter un objeto, con el nivel marcado. Escribo los datos y la conclusión: «El objeto tiene masa de 120 g y ocupa espacio, porque subió el agua 12 mm».",
      "Todo experimento tiene límites. Mi balanza puede tener un error pequeño. Mi regla no mide fracciones exactas. Y probé solo con unos pocos objetos. Por eso escribo: «En esta prueba…» y no «siempre».",
  ],
  vocab=[("explicación", "respuesta que dice cómo y por qué"), ("modelo", "dibujo o esquema que representa un experimento"), ("error de medición", "diferencia pequeña entre lo medido y el valor real"), ("límite", "lo que la prueba no permite saber"), ("conclusión", "respuesta final apoyada en los datos")],
  worked=[
      ("Completar una explicación", "Faltan datos: 'La piedra tiene ______ de masa y ocupa espacio porque el agua ______.' Elige: 120 g / subió.", ["La masa es un número con unidad.", "El espacio se muestra porque el agua sube.", "Completo con ambos."], "120 g; subió"),
      ("Encontrar un límite", "Solo probaste con piedras. ¿Qué no sabes?", ["Pienso qué falta.", "No probaste otros materiales.", "No sabes si pasa igual con todos."], "No sabes si pasa igual con otros materiales"),
  ],
  mistakes=[
      ("Concluir 'toda la materia pesa lo mismo'.", "Cada objeto tiene su propia masa.", "Compara con datos."),
      ("No escribir los límites del experimento.", "Parece que los resultados valen para todo.", "Anota qué falta probar."),
  ],
  rec=[
      ("¿La materia tiene masa y ocupa espacio, sí o no?", "Sí", "Esa es la definición."),
      ("¿Se mide la masa con balanza o con regla?", "Con balanza", "La regla mide longitud."),
      ("Completa con «datos» o «deseos»: la conclusión se apoya en los ______.", "Datos", "Los datos son la evidencia medida."),
  ],
  und=[
      ("¿Qué incluye una explicación completa? A) Datos de masa y de espacio. B) Solo la opinión.", "A", "Con esas dos pruebas se explica."),
      ("¿Por qué se escribe 'en esta prueba…'?", "Porque los resultados valen para lo que se probó", "No se debe exagerar."),
      ("¿Qué es un error de medición?", "Una diferencia pequeña entre lo medido y el valor real", "Los instrumentos no son perfectos."),
  ],
  app=[
      arith("Datos de ejemplo. Un objeto tenía 150 g y otro 90 g. ¿Cuántos gramos tienen entre los dos?", "150+90", "Se suman las masas."),
      ("Completa la conclusión: 'En esta prueba, la piedra ocupó más espacio que la cuchara porque el agua subió ______.' Elige: más / menos.", "Más", "La piedra desplazó más agua."),
      ("Un niño mide la masa de un objeto y obtiene 120 g, 121 g y 119 g. ¿Es una diferencia grande o pequeña?", "Pequeña", "Es un error normal de medición."),
  ],
  rea=[
      ("Luis dice que su experimento prueba que todo lo del mundo tiene masa. ¿Tiene razón? Responde Sí o No y explica.", "No; solo probó algunos objetos", "No puede afirmar tanto."),
      ("Datos de ejemplo. Un objeto tiene 50 g y hace subir el agua 20 mm. Otro tiene 50 g y la hace subir 5 mm. ¿Tienen igual masa? ¿Ocupan igual espacio?", "Igual masa; distinto espacio", "La masa es la misma y el desplazamiento es distinto."),
  ],
  cha=[
      ("Escribe una conclusión de dos frases con datos de masa y de espacio.", "La piedra tiene 120 g de masa. Hace subir el agua 12 mm, por lo que ocupa espacio", "Usa dos datos."),
      ("Escribe un límite de tu experimento y cómo lo mejorarías.", "Probé pocos objetos; probaría más materiales", "Reconoce lo que falta."),
  ],
  context=[("Una clase prueba 6 objetos. De ellos, 4 se miden con balanza y 2 se miden con el vaso de agua. ¿Cuántas mediciones de masa se hicieron?", "4", "Los 4 que se midieron con balanza.")],
  selfcheck=[("¿Qué dos pruebas muestran que algo es materia?", "Medir su masa y mostrar que ocupa espacio", "Son las dos condiciones."), ("¿Por qué escribir los límites?", "Para no exagerar los resultados", "Los datos valen para lo probado."), ("¿Por qué dos mediciones del mismo objeto pueden dar 120 g y 121 g?", "Por un error pequeño de medición", "Los instrumentos no son perfectos.")],
  open_task=task("Elige un objeto seguro de tu casa y demuestra que es materia con dos pruebas: masa (con balanza o balanza de percha) y espacio (con el vaso de agua o la bolsa de aire). Dibuja el montaje, anota los datos y escribe tu explicación con una conclusión y un límite.", "Objeto: una piedra. Masa 120 g. Espacio: el agua subió 12 mm. Conclusión: la piedra es materia. Límite: probé solo con una piedra.", ["dos pruebas distintas", "datos con unidades", "conclusión y límite"], ["dibujo y datos"], ["no usar unidades", "no escribir límite"], "Pregunta qué cambiaría con otro objeto."),
  reinforce="Escribe tres objetos y su masa aproximada usando una balanza.",
  extend="Averigua cómo se puede mostrar que el aire tiene masa y cuéntalo con tus palabras.")

# ---------------------------------------------------------------- OA 10
L(OA10, 1,
  materials="Este cuaderno y lápiz. Objetos seguros: una piedra lisa, un vaso de plástico con agua, una bolsa de plástico con aire (sin acercarla a la cara).",
  use="Aprenderé a reconocer sólidos, líquidos y gases y a separar lo que observo de lo que supongo. Sirve para describir la materia de todos los días.",
  prior=["Sé que la materia tiene masa y ocupa espacio.", "Sé anotar lo que observo."],
  explain=[
      "La materia se presenta en tres estados: sólido, líquido y gaseoso. Un sólido, como una piedra o un lápiz, tiene forma propia y no se derrama. Un líquido, como el agua o el aceite, fluye y toma la forma del recipiente. Un gas, como el aire, se esparce y llena todo el espacio disponible.",
      "Para observar un estado puedes pasar el objeto de un recipiente a otro. La piedra sigue igual. El agua cambia de forma, pero la cantidad es la misma. El aire de una bolsa se acomoda a la bolsa. Estas observaciones son evidencia del estado.",
      "Anota lo que ves: «el agua toma la forma del vaso». Eso es una observación. Decir «el agua es más importante que la piedra» es una opinión. Para clasificar un material, mira si tiene forma propia y si fluye.",
  ],
  vocab=[("sólido", "estado de la materia con forma propia"), ("líquido", "estado de la materia que fluye y toma la forma del recipiente"), ("gas", "estado de la materia que llena todo el espacio disponible"), ("fluir", "moverse y escurrirse"), ("recipiente", "objeto que contiene algo, como un vaso o una botella")],
  worked=[
      ("Clasificar", "¿Qué estado es un lápiz? ¿Y el agua? ¿Y el aire?", ["Miro si tiene forma propia: el lápiz sí.", "El agua fluye y toma la forma del vaso.", "El aire llena el espacio."], "Lápiz: sólido; agua: líquido; aire: gas"),
      ("Observación u opinión", "«El agua toma la forma del vaso» y «El agua es la mejor». ¿Cuál es observación?", ["Veo si se puede comprobar.", "La forma se ve.", "'La mejor' es opinión."], "El agua toma la forma del vaso"),
  ],
  mistakes=[
      ("Decir que la arena es líquida porque se derrama.", "Cada grano de arena es sólido.", "Fíjate en cada trozo, no solo en el montón."),
      ("Pensar que el aire no existe porque no se ve.", "El aire es un gas y ocupa espacio.", "Atrapa aire en una bolsa y mira cómo se hincha."),
  ],
  rec=[
      ("¿Una piedra es sólido, líquido o gas?", "Sólido", "Tiene forma propia."),
      ("¿El agua es sólido, líquido o gas?", "Líquido", "Fluye y toma la forma del recipiente."),
      ("¿El aire es sólido, líquido o gas?", "Gas", "Llena el espacio disponible."),
  ],
  und=[
      ("¿Qué estado tiene forma propia? A) Sólido. B) Líquido.", "A", "Un sólido mantiene su forma."),
      ("¿Qué pasa con la forma del agua al pasarla del vaso a una botella?", "Toma la forma de la botella", "Los líquidos toman la forma del recipiente."),
      ("¿Dónde se acomoda el aire de una bolsa?", "En toda la bolsa", "Los gases llenan el espacio disponible."),
  ],
  app=[
      ("Clasifica: leche, madera, aire de una pelota, jugo. ¿Cuántos son líquidos?", "2", "Leche y jugo son líquidos."),
      ("Clasifica: piedra, aceite, hielo, aire. ¿Cuántos son sólidos?", "2", "Piedra y hielo son sólidos."),
      arith("En una mesa hay 3 sólidos, 2 líquidos y 1 gas. ¿Cuántos materiales hay?", "3+2+1", "Se suman todos."),
  ],
  rea=[
      ("Ema dice que el hielo es líquido porque se derrite. ¿Tiene razón? Responde Sí o No y explica.", "No; mientras es hielo, es sólido", "Cambia a líquido solo cuando se derrite."),
      ("Un niño dice que el aire de una botella tapada no es materia porque no se ve. ¿Qué respondes? Escribe una palabra: 'es' o 'no es'.", "Es", "Ocupa espacio y es un gas."),
  ],
  cha=[
      ("Escribe una observación y una opinión sobre el agua en un vaso.", "Observación: toma la forma del vaso. Opinión: es la mejor bebida", "Una se comprueba."),
      ("Escribe un ejemplo de sólido, de líquido y de gas de tu casa.", "Sólido: cuchara. Líquido: aceite. Gas: aire", "Cada uno cumple su estado."),
  ],
  context=[("En la cocina hay 4 sólidos, 3 líquidos y 1 gas (el aire). ¿Cuántos estados distintos hay?", "3", "Sólido, líquido y gas.")],
  selfcheck=[("Nombra los tres estados.", "Sólido, líquido y gas", "Son los estados vistos."), ("¿Qué estado fluye y toma la forma del recipiente?", "Líquido", "Así actúa el agua."), ("¿Qué estado llena todo el espacio?", "Gas", "Como el aire de una bolsa.")],
  open_task=task("Haz una tabla con seis materiales de tu casa: tres sólidos, dos líquidos y el aire. Columnas: material, estado y una observación (tiene forma propia, toma la forma del vaso, llena la bolsa). No uses objetos filosos, calientes o de vidrio. Prueba solo con objetos seguros.", "Cuchara: sólido; tiene forma propia. Agua: líquido; toma la forma del vaso. Aire: gas; llena la bolsa.", ["seis materiales", "estado correcto", "una observación por fila"], ["tabla completa"], ["clasificar por tamaño", "no anotar la observación"], "Pregunta cómo supo el estado de cada material."),
  reinforce="Escribe tres sólidos, tres líquidos y un gas que veas en tu casa.",
  extend="Pasa agua de un vaso a una botella y dibuja su forma antes y después.")

L(OA10, 2,
  materials="Este cuaderno, lápiz y regla. Un vaso medidor o tazas medidoras de plástico, una botella de plástico con tapa y agua.",
  use="Aprenderé a preguntar y predecir si el volumen cambia cuando cambia la forma. Sirve para comprender cómo se comportan sólidos, líquidos y gases.",
  prior=["Sé qué son sólido, líquido y gas.", "Sé que una predicción se hace antes de probar."],
  explain=[
      "El volumen es el espacio que ocupa la materia. En un líquido, el volumen se mantiene aunque cambie el recipiente. Si pasas 200 mL de agua de un vaso a una botella, siguen siendo 200 mL, aunque la forma sea distinta. mL es la abreviatura de mililitro.",
      "En un sólido, la forma y el volumen se mantienen. Un gas, en cambio, puede llenar un recipiente grande o uno pequeño: se esparce o se comprime. Si aprietas una botella cerrada con aire, se puede apretar un poco, porque el aire se comprime. Una botella llena de agua y cerrada casi no se aprieta.",
      "Una pregunta comprobable: «¿Se puede apretar más una botella con aire que una botella llena de agua?». La predicción: «Sí, porque el gas se comprime». Se compara con cuidado y se anota qué ocurrió en cada una.",
  ],
  vocab=[("volumen", "espacio que ocupa la materia"), ("mililitro (mL)", "unidad para medir volumen de líquidos"), ("comprimir", "apretar algo para que ocupe menos espacio"), ("recipiente", "objeto que contiene algo"), ("vaso medidor", "recipiente con marcas para medir volumen")],
  worked=[
      ("Comparar volúmenes", "Datos de ejemplo. Un vaso tiene 250 mL de agua. Se pasa a una botella. ¿Cuántos mL hay en la botella?", ["El líquido cambia de forma, no de cantidad.", "El volumen se mantiene.", "Sigue siendo 250 mL."], "250 mL"),
      ("Hacer una predicción", "Una botella cerrada con aire y otra cerrada llena de agua. Predice cuál se aprieta más.", ["Pienso en el gas: se comprime.", "El agua casi no se comprime.", "La del aire se aprieta más."], "La botella con aire"),
  ],
  mistakes=[
      ("Pensar que el agua aumenta al pasar a un recipiente más alto.", "La altura cambia, pero el volumen es el mismo.", "Mide con el vaso medidor."),
      ("Apretar la botella con mucha fuerza.", "Puede romperse o saltar la tapa.", "Aprieta con cuidado, con ayuda de una persona adulta."),
  ],
  rec=[
      ("¿El volumen de un líquido cambia al pasarlo a otro recipiente, sí o no?", "No", "Solo cambia la forma."),
      ("¿Qué estado se comprime más fácil: un gas o un líquido?", "Un gas", "Su volumen puede cambiar."),
      ("Completa con «mL» o «kg»: el volumen de un líquido se mide en ______.", "mL", "La sigla mL significa mililitros."),
  ],
  und=[
      ("¿Cuál pregunta se puede comprobar? A) ¿Cuántos mL de agua caben en un vaso? B) ¿Qué líquido es más lindo?", "A", "Se mide con un vaso medidor."),
      ("Si pasas 300 mL de agua a un recipiente más alto y angosto, ¿cuántos mL hay?", "300 mL", "El volumen no cambia."),
      ("¿Por qué una botella con aire se aprieta un poco?", "Porque el aire se comprime", "Los gases cambian de volumen."),
  ],
  app=[
      arith("Datos de ejemplo. Tienes 150 mL de agua en un vaso y echas 100 mL más. ¿Cuántos mL hay ahora?", "150+100", "Se suman los volúmenes."),
      arith("Datos de ejemplo. Una jarra tenía 500 mL. Se sirvieron 3 vasos de 100 mL. ¿Cuántos mL quedan?", "500-3*100", "Se resta lo servido al total."),
      ("Predice: si aprietas una botella cerrada con aire, ¿su volumen interior será menor o mayor que antes?", "Menor", "El aire se comprime."),
  ],
  rea=[
      ("Ana dice que al pasar el agua a una botella angosta hay 'más agua' porque sube más. ¿Tiene razón? Responde Sí o No y explica.", "No; el volumen es el mismo", "Solo cambia la forma."),
      ("Luis aprieta una botella llena de agua y otra con aire. Dice que el agua es 'más fuerte'. ¿Qué conclusión sí está apoyada por la prueba? Responde con una frase.", "El agua se comprime mucho menos que el aire", "La prueba compara compresión."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre el volumen de un líquido y qué medirás.", "¿Cambia el volumen de 200 mL de agua al pasarla a otro vaso? Mediré con un vaso medidor", "Se responde midiendo."),
      ("Datos de ejemplo. Medida 1: 200 mL. Medida 2: 195 mL, con un poco de agua que quedó pegada al vaso. ¿Muestra eso que el volumen del agua cambió o un error pequeño de medición?", "Un error pequeño de medición", "Una parte del agua quedó en el vaso."),
  ],
  context=[("En una receta se usan 3 tazas de agua de 200 mL cada una. ¿Cuántos mL se necesitan?", "600", "3 × 200 = 600 mL.")],
  selfcheck=[("¿Qué es el volumen?", "El espacio que ocupa la materia", "Se mide en mL para líquidos."), ("¿Cambia el volumen de un líquido al cambiar de recipiente?", "No", "Solo cambia su forma."), ("¿Qué estado se comprime con facilidad?", "El gas", "Su volumen cambia.")],
  open_task=task("Con una persona adulta, mide 200 mL de agua con un vaso medidor y pásala a tres recipientes distintos (un vaso alto, un plato hondo de plástico, una botella). Dibuja la forma del agua en cada uno. Anota si el volumen cambió y escribe tu predicción antes. Luego aprieta una botella cerrada con aire con cuidado y anota qué observas.", "Predicción: el volumen no cambia. Vaso alto: 200 mL. Plato: 200 mL. Botella: 200 mL. La botella con aire se aprieta un poco.", ["predicción con razón", "tres mediciones", "observación de la botella con aire"], ["dibujo y tabla"], ["apretar con mucha fuerza", "no usar el vaso medidor"], "Pregunta qué cambió y qué no cambió."),
  reinforce="Mide 100 mL de agua y dibújala en dos recipientes distintos.",
  extend="Escribe por qué una botella cerrada llena de agua casi no se puede apretar.")

L(OA10, 3,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar los tres estados de la materia con los mismos criterios: forma, volumen y capacidad de fluir. Sirve para clasificar materiales con fundamento.",
  prior=["Sé qué son sólido, líquido y gas.", "Sé que el volumen es el espacio que ocupa la materia."],
  explain=[
      "Para comparar los estados uso criterios. El primero es la forma: un sólido tiene forma propia; un líquido toma la forma del recipiente; un gas también toma la forma del recipiente y lo llena por completo. El segundo es el volumen: el de un sólido y el de un líquido se mantienen; el de un gas cambia según el espacio.",
      "El tercer criterio es la capacidad de fluir. Un sólido no fluye. Un líquido fluye y se derrama. Un gas fluye y se esparce en todas las direcciones. Por eso podemos oler una fragancia desde otra pieza: el gas se esparce.",
      "Una tabla ayuda a comparar. En las filas pongo los criterios y en las columnas los estados. Así veo en qué se parecen y en qué se diferencian. Un líquido se parece a un gas porque ambos fluyen, y se parece a un sólido porque su volumen se mantiene.",
  ],
  vocab=[("forma propia", "forma que se mantiene sin importar el recipiente"), ("capacidad de fluir", "posibilidad de escurrirse o moverse"), ("esparcirse", "extenderse en todas las direcciones"), ("criterio", "característica que se mira igual en todos"), ("tabla comparativa", "cuadro para ordenar parecidos y diferencias")],
  worked=[
      ("Aplicar la tabla", "Criterio: ¿toma la forma del recipiente? Piedra, agua, aire. ¿Cuáles lo hacen?", ["La piedra mantiene su forma.", "El agua toma la forma del vaso.", "El aire llena el recipiente."], "Agua y aire"),
      ("Parecidos", "¿Qué tienen en común los líquidos y los gases?", ["Reviso los tres criterios.", "Ambos fluyen.", "Ambos toman la forma del recipiente."], "Ambos fluyen y toman la forma del recipiente"),
  ],
  mistakes=[
      ("Pensar que los gases tienen forma propia.", "Toman la forma y llenan el recipiente.", "Mira dónde está el gas."),
      ("Comparar los estados con criterios distintos.", "No hay un criterio común.", "Usa los mismos tres criterios para todos."),
  ],
  rec=[
      ("¿Un sólido fluye, sí o no?", "No", "Mantiene su forma."),
      ("¿Un líquido fluye, sí o no?", "Sí", "Se escurre y se derrama."),
      ("¿Un gas fluye, sí o no?", "Sí", "Se esparce en todas las direcciones."),
  ],
  und=[
      ("¿Qué estado tiene volumen que cambia según el espacio? A) Gas. B) Sólido.", "A", "El gas se esparce o se comprime."),
      ("¿Qué estado mantiene forma y volumen?", "El sólido", "No fluye ni cambia."),
      ("¿Qué estado mantiene su volumen pero cambia de forma?", "El líquido", "Toma la forma del recipiente."),
  ],
  app=[
      ("Clasifica con los tres criterios: tiene forma propia, mantiene su volumen y no fluye. ¿Qué estado es?", "Sólido", "Cumple los tres."),
      ("Clasifica: fluye, toma la forma del recipiente y mantiene su volumen. ¿Qué estado es?", "Líquido", "No cambia de volumen."),
      ("Clasifica: fluye, llena todo el recipiente y su volumen cambia según el espacio. ¿Qué estado es?", "Gas", "Solo el gas cumple los tres."),
  ],
  rea=[
      ("Mario dice que el aceite es sólido porque es espeso. Pero fluye y toma la forma del vaso. ¿Qué estado es? Explica.", "Líquido, porque fluye y toma la forma del vaso", "Espeso no significa sólido."),
      ("Ema dice que el aire de una pieza cerrada no se esparce. ¿Tiene razón? Responde Sí o No y explica.", "No; el aire llena toda la pieza", "Los gases se esparcen."),
  ],
  cha=[
      ("Completa: 'El sólido ______ forma propia, el líquido ______ la forma del recipiente y el gas ______ todo el espacio.' Usa: tiene, toma, llena.", "Tiene; toma; llena", "Cada estado se comporta distinto."),
      ("Escribe un parecido entre dos estados usando un criterio.", "Los líquidos y los gases fluyen", "Ambos se escurren."),
  ],
  context=[("Una tabla compara tres materiales: una piedra, jugo y el aire de una pelota. ¿Cuántos estados distintos aparecen?", "3", "Sólido, líquido y gas.")],
  selfcheck=[("¿Qué criterio distingue al sólido?", "Tiene forma propia", "Los otros estados la toman del recipiente."), ("¿Qué criterio comparten líquidos y gases?", "Ambos fluyen", "Se escurren o se esparcen."), ("¿Qué estado cambia más de volumen?", "El gas", "Se esparce o se comprime.")],
  open_task=task("Completa una tabla comparativa con filas: forma propia, se mantiene su volumen, fluye. Columnas: sólido, líquido y gas. Escribe sí o no en cada casilla. Luego escribe dos frases: un parecido y una diferencia. Prueba con objetos seguros de tu casa: piedra, agua y aire en una bolsa.", "Forma propia: sólido sí, líquido no, gas no. Volumen se mantiene: sólido sí, líquido sí, gas no. Fluye: sólido no, líquido sí, gas sí. Parecido: líquidos y gases fluyen.", ["tabla completa", "un parecido", "una diferencia"], ["tabla de 3 por 3"], ["usar criterios distintos", "dejar casillas vacías"], "Pregunta por qué el líquido y el gas se parecen."),
  reinforce="Dibuja tres recipientes y muestra cómo se ve un sólido, un líquido y un gas en ellos.",
  extend="Averigua qué ocurre con el estado del agua si se enfría mucho.")

L(OA10, 4,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a explicar los estados de la materia con dibujos como modelos y a decir qué no muestran. Sirve para comunicar mis ideas con claridad.",
  prior=["Sé comparar sólidos, líquidos y gases.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo de los estados de la materia puede ser un dibujo de tres recipientes. En el sólido, la piedra ocupa su forma sin cambiar. En el líquido, el agua llena la parte de abajo del recipiente con una superficie plana. En el gas, el color llena todo el recipiente.",
      "Con este modelo puedo explicar: «Si paso el agua de un vaso ancho a uno angosto, cambia su forma pero no su volumen». También puedo predecir: «Si suelto aire de una bolsa en una pieza, se esparce por todo el lugar». El modelo ayuda a pensar.",
      "El modelo tiene límites. Un dibujo no muestra las partes más pequeñas de la materia ni los cambios de estado. Tampoco muestra el movimiento. Es una ayuda para entender, no una copia de la realidad.",
  ],
  vocab=[("modelo", "dibujo que representa una idea"), ("superficie", "parte de arriba de un líquido"), ("cambio de estado", "paso de un estado a otro"), ("etiqueta", "nombre escrito junto a un dibujo"), ("límite", "lo que el modelo no muestra")],
  worked=[
      ("Leer el modelo", "En un dibujo, el agua llena la parte de abajo del vaso y deja arriba un espacio vacío. ¿Qué estado muestra?", ["Miro si llena todo.", "No llena todo.", "Es un líquido."], "Líquido"),
      ("Predecir con el modelo", "Si dibujas aire en una botella, ¿cómo lo pintas: solo abajo o en toda la botella?", ["Un gas llena todo el espacio.", "Debe cubrir toda la botella.", "Pinto toda la botella."], "En toda la botella"),
  ],
  mistakes=[
      ("Dibujar el gas solo abajo del recipiente.", "El gas llena todo el espacio.", "Pinta todo el interior."),
      ("Pensar que el dibujo muestra todo lo que pasa.", "Un dibujo simplifica.", "Escribe un límite."),
  ],
  rec=[
      ("¿Un dibujo de un gas debe llenar todo el recipiente, sí o no?", "Sí", "El gas llena todo el espacio."),
      ("¿El líquido tiene una superficie plana arriba, sí o no?", "Sí", "En un recipiente quieto se ve plana."),
      ("Completa con «forma» o «sabor»: el sólido mantiene su ______.", "Forma", "No depende del recipiente."),
  ],
  und=[
      ("¿Qué muestra el dibujo de un líquido? A) Llena abajo con superficie plana. B) Llena todo el recipiente.", "A", "Eso muestra un líquido."),
      ("¿Qué muestra el dibujo de un sólido?", "Una forma propia que no depende del recipiente", "Mantiene su forma."),
      ("¿Qué límite tiene un dibujo de los estados?", "No muestra las partes pequeñas ni el movimiento", "Es una simplificación."),
  ],
  app=[
      ("Dibujas 3 recipientes: sólido, líquido y gas. ¿En cuál pintarás todo el interior?", "En el gas", "El gas llena el espacio."),
      arith("Un modelo usa 3 dibujos de estados y se agregan 2 más para mostrar cambios. ¿Cuántos dibujos hay?", "3+2", "Se suman los dibujos."),
      ("Predice: si abres una bolsa con aire en una pieza, ¿el aire se queda en la bolsa o se esparce?", "Se esparce", "Los gases llenan el espacio."),
  ],
  rea=[
      ("Luis dice que su dibujo explica todo sobre los estados de la materia. ¿Tiene razón? Responde Sí o No y explica.", "No; solo muestra forma y volumen", "No muestra cambios ni movimiento."),
      ("Datos de ejemplo. Un dibujo muestra agua en un vaso con superficie plana. Otro muestra agua inclinada hacia un lado en el mismo vaso quieto. ¿Cuál es más probable que esté bien? Responde 1 o 2.", "1", "En reposo la superficie es plana."),
  ],
  cha=[
      ("Dibuja con palabras cómo representarías el aire en una botella y el agua en la misma botella.", "Aire: pintado en toda la botella. Agua: pintada abajo con superficie plana", "Muestra la diferencia."),
      ("Escribe un límite del modelo de recipientes y cómo lo mejorarías.", "No muestra el movimiento; agregaría flechas", "Reconoce lo que falta."),
  ],
  context=[("Un curso dibuja 6 recipientes: 2 de sólido, 2 de líquido y 2 de gas. Cada recipiente lleva 1 etiqueta. ¿Cuántas etiquetas se usan?", "6", "Hay una etiqueta por recipiente.")],
  selfcheck=[("¿Qué muestra el dibujo de un gas?", "Que llena todo el recipiente", "Eso hace un gas."), ("¿Qué muestra el dibujo de un líquido?", "Que llena la parte de abajo del recipiente", "Con superficie plana."), ("¿Qué límite tiene un dibujo?", "No muestra movimiento ni partes pequeñas", "Un dibujo siempre simplifica.")],
  open_task=task("Dibuja tres recipientes iguales y rotula: sólido (una piedra), líquido (agua) y gas (aire). Escribe debajo de cada uno una frase con la forma, el volumen y si fluye. Escribe una predicción ('si paso el agua a otro recipiente…') y un límite de tu dibujo.", "Sólido: forma propia, no fluye. Líquido: toma la forma del vaso, fluye. Gas: llena el recipiente, fluye. Predicción: si paso el agua a un vaso ancho, cambia su forma pero no su volumen. Límite: no muestra movimiento.", ["tres dibujos rotulados", "frase con tres criterios", "predicción y límite"], ["dibujo"], ["pintar el gas solo abajo", "no escribir límite"], "Pregunta cuál estado fue más difícil de dibujar y por qué."),
  reinforce="Dibuja una botella con agua y otra con aire y rotula cada una.",
  extend="Dibuja el aire de una pelota y escribe en qué estado está y por qué.")

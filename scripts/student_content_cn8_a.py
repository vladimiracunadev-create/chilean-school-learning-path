"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 01 (evolución histórica de los modelos celulares)."""
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


OA1 = "CN08 OA 01"

L(OA1, 1,
  materials="Este cuaderno y lápiz. No necesitas microscopio: todas las observaciones que se usan están descritas en cada ejercicio.",
  use="Aprenderé a formular preguntas que se pueden investigar sobre cómo se descubrió la célula. Sirve para saber qué preguntas la ciencia puede contestar con observaciones.",
  prior=["Sé que un modelo es una representación que simplifica una realidad.", "Sé distinguir lo que observo de lo que opino."],
  explain=[
      "Un modelo científico es una representación que explica cómo es o cómo funciona algo, y se cambia cuando aparece evidencia nueva. La evidencia son observaciones o mediciones que se pueden comprobar. El modelo de la célula nació así: con observaciones hechas con microscopio, un instrumento que agranda lo que el ojo no alcanza a ver.",
      "En 1665, Robert Hooke miró con un microscopio una lámina muy delgada de corcho y vio pequeñas cavidades ordenadas, que llamó «celdillas» (cells, en inglés). El corcho viene de la corteza de un árbol y está formado por células muertas, por eso Hooke solo vio sus paredes vacías. En el siglo XVII, Antonie van Leeuwenhoek usó lentes simples muy bien pulidas y observó seres vivos diminutos en gotas de agua, que llamó «animalículos».",
      "Una pregunta investigable se puede contestar con observaciones o mediciones, e indica qué se observa o qué se mide. «¿Qué se ve en una lámina delgada de corcho al aumentar 100 veces?» es investigable. «¿Cuál científico fue más simpático?» no lo es, porque depende de opiniones y no de datos.",
  ],
  vocab=[("modelo", "representación que explica cómo es o cómo funciona algo"), ("evidencia", "observación o medición que se puede comprobar"), ("microscopio", "instrumento que agranda objetos muy pequeños"), ("pregunta investigable", "pregunta que se contesta con observaciones o mediciones"), ("célula", "unidad básica de los seres vivos")],
  worked=[
      ("Investigable o no", "Clasifica: (1) «¿Cuántas celdillas por fila se ven en una lámina de corcho?» (2) «¿Es el corcho el material más bonito?»", ["Pregunto si se responde contando, midiendo u observando.", "La pregunta 1 se contesta contando celdillas.", "La pregunta 2 depende del gusto de cada persona."], "La 1 es investigable; la 2 no"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Son interesantes los animalículos?» para que sea investigable.", ["Quito la palabra que depende de la opinión («interesantes»).", "Digo qué se observa: seres diminutos en una gota de agua de un charco.", "Queda: «¿Qué seres diminutos se observan en una gota de agua de charco con un microscopio?»"], "«¿Qué seres diminutos se observan en una gota de agua de charco con un microscopio?»"),
  ],
  mistakes=[
      ("Creer que una pregunta con «por qué» sobre gustos o fama se puede investigar.", "No hay una observación que la conteste.", "Reescribe la pregunta indicando qué se observa o se mide."),
      ("Pensar que Hooke vio células vivas en el corcho.", "El corcho está formado por células muertas y solo quedan sus paredes.", "Recuerda que el nombre «celdilla» describe lo que él alcanzó a ver."),
  ],
  rec=[
      ("¿Quién llamó «celdillas» a las cavidades que vio en una lámina de corcho?", "Robert Hooke", "Hooke observó corcho en 1665 y describió esas cavidades."),
      ("Completa: una pregunta investigable se contesta con observaciones o ______ (mediciones u opiniones).", "Mediciones", "Los datos observados o medidos se pueden comprobar."),
      ("Verdadero o falso: un modelo científico se puede cambiar cuando aparece evidencia nueva.", "Verdadero", "Los modelos se revisan con nuevas evidencias."),
  ],
  und=[
      ("¿Cuál pregunta es investigable? A) ¿Qué se observa al mirar con microscopio una gota de agua de charco? B) ¿Era más bonito el microscopio de Hooke que el de Leeuwenhoek?", "A", "Se responde observando; la otra depende del gusto personal."),
      ("¿Por qué Hooke vio solo paredes y no el interior de las celdillas del corcho? A) Porque el corcho está formado por células muertas, de las que quedan las paredes. B) Porque las células no tienen nada dentro.", "A", "Las células muertas del corcho conservan paredes y pierden su contenido."),
      ("¿Qué observó Leeuwenhoek en gotas de agua con sus lentes?", "Seres vivos diminutos que llamó animalículos", "Fue de los primeros en ver microorganismos vivos."),
  ],
  app=[
      ("Se pregunta: «¿Se ven más seres diminutos en agua de charco con hojas o en agua de la llave?». ¿Qué variable cambia entre las dos gotas?", "El tipo de agua", "Se comparan dos muestras que difieren en su origen."),
      arith("Hooke publicó sus observaciones del corcho en 1665 y Schwann propuso en 1839 que los animales también están formados por células. ¿Cuántos años pasaron entre ambos hechos?", "1839-1665", "Se resta el año más antiguo al más reciente."),
      ("Un grupo escribe: «¿Cuántos seres vivos se cuentan en una gota de agua de charco al aumentar 100 veces?». ¿Qué se mide en esa pregunta?", "El número de seres vivos por gota", "La pregunta pide contar organismos."),
  ],
  rea=[
      ("Un compañero dice: «Hooke descubrió que todos los seres vivos están formados por células». ¿Es correcto? A) No: Hooke vio paredes de células muertas del corcho; la idea general vino después. B) Sí: inventó la palabra célula, por lo tanto lo demostró.", "A", "Poner un nombre a lo observado no prueba una afirmación sobre todos los seres vivos."),
      ("P1: «¿Por qué Leeuwenhoek es más famoso que Hooke?». P2: «¿Qué estructuras se distinguen en una gota de agua con 100 aumentos?». ¿Cuál de las dos es investigable? Responde P1 o P2.", "P2", "Se contesta observando la gota; la fama depende de opiniones."),
  ],
  cha=[
      ("Un museo escribe: «El modelo de célula nunca cambiará». ¿Por qué contradice la forma de trabajar de la ciencia? A) Porque los modelos se revisan cuando hay evidencia nueva, como ocurrió desde Hooke. B) Porque las células cambian de forma cada año.", "A", "La historia de la célula muestra modelos que se corrigen con nuevos datos."),
      arith("Datos de ejemplo: se contaron seres diminutos en cuatro gotas. Charco: 12 y 9. Llave: 0 y 1. ¿Cuántos seres más hay en total en las gotas de charco que en las de llave?", "12+9-(0+1)", "Se suman las dos gotas de cada agua y se restan los totales."),
  ],
  context=[arith("Dibujo de ejemplo de una lámina de corcho: 6 celdillas en cada fila y 5 filas. ¿Cuántas celdillas hay en el dibujo?", "6*5", "Se multiplica el número de celdillas por fila por el número de filas.")],
  selfcheck=[("¿Qué observó Hooke en el corcho?", "Pequeñas cavidades que llamó celdillas", "Eran las paredes de células muertas."), ("¿Qué hace investigable a una pregunta?", "Que se puede contestar con observaciones o mediciones", "Indica qué se observa o se mide."), ("¿Qué es un modelo científico?", "Una representación que explica algo y se revisa con evidencia nueva", "Los modelos cambian cuando hay datos distintos.")],
  open_task=task("Lee estas cuatro preguntas: (1) «¿Cuántas celdillas hay por fila en una lámina de corcho dibujada?» (2) «¿Quién fue más importante, Hooke o Leeuwenhoek?» (3) «¿Qué seres se ven en una gota de agua de charco al aumentar 100 veces?» (4) «¿Es lindo mirar por un microscopio?». Rotula cada una como investigable o no investigable y reescribe una de las no investigables para que sea investigable.", "1 investigable; 2 no (opinión); 3 investigable; 4 no (gusto). Reescritura de la 4: «¿Qué detalles de una hoja se ven con microscopio que no se ven a simple vista?»", ["rotula las cuatro", "explica con «se observa o se mide» o «es opinión»", "la reescritura indica qué se observa o mide"], ["cuatro rótulos y una pregunta reescrita"], ["llamar investigable a una pregunta de opinión", "reescribir sin decir qué se observa"], "Pregunta qué dato necesitarías para contestar la pregunta reescrita."),
  reinforce="Escribe una pregunta investigable sobre lo que Hooke vio en el corcho.",
  extend="Explica por qué una pregunta sobre la fama de un científico no es investigable con un microscopio.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. Las descripciones históricas están resumidas en cada ejercicio; no necesitas buscar nada más.",
  use="Aprenderé a separar lo que cada científico observó de lo que dedujo, y a ver cómo el instrumento limitó sus conclusiones. Sirve para leer evidencia con cuidado.",
  prior=["Sé que Hooke vio celdillas en el corcho y Leeuwenhoek vio seres diminutos.", "Sé que una pregunta investigable se contesta con observaciones."],
  explain=[
      "Una observación es lo que se percibe o se mide; una inferencia es la conclusión que se saca a partir de ella. Hooke observó celdillas en el corcho (observación). Su inferencia fue que el corcho está formado por pequeñas cámaras. Leeuwenhoek observó seres que se mueven en una gota de agua (observación) y dedujo que esos seres estaban vivos.",
      "Los científicos que vinieron después reunieron más evidencia. En 1838, Matthias Schleiden, que estudiaba plantas, concluyó que todas las plantas están formadas por células. En 1839, Theodor Schwann, que estudiaba animales, concluyó lo mismo para los animales. En 1855, Rudolf Virchow sostuvo que toda célula proviene de otra célula que ya existía.",
      "El instrumento limita lo que se puede observar. Un microscopio con pocos aumentos solo muestra formas gruesas. Por eso la evidencia debe leerse con prudencia: la conclusión no puede afirmar más de lo que el dato permite, y cada nueva técnica puede corregir ideas anteriores.",
  ],
  vocab=[("observación", "lo que se percibe o se mide directamente"), ("inferencia", "conclusión que se saca a partir de observaciones"), ("limitación", "aquello que impide afirmar más de lo observado"), ("aumento", "cuántas veces agranda un instrumento la imagen"), ("prudencia", "no afirmar más de lo que muestran los datos")],
  worked=[
      ("Observación o inferencia", "Clasifica: (1) «En la gota de agua se ven puntos que se desplazan». (2) «Esos puntos son seres vivos».", ["Pregunto si lo veo directamente.", "La frase 1 describe lo que se ve.", "La frase 2 es una conclusión a partir de lo visto."], "La 1 es observación; la 2 es inferencia"),
      ("Quién concluyó qué", "Schleiden estudió plantas y Schwann animales. ¿Quién propuso que los animales están formados por células?", ["Recuerdo que Schwann trabajó con animales.", "Su conclusión fue para los animales, en 1839."], "Schwann"),
  ],
  mistakes=[
      ("Confundir lo que se vio con lo que se dedujo.", "Una inferencia puede ser incorrecta aunque la observación sea correcta.", "Marca primero qué se percibió y luego qué se concluyó."),
      ("Atribuir a un científico una idea que vino de otro.", "Cada aporte tiene un autor, una fecha y una evidencia.", "Relaciona cada científico con su aporte."),
  ],
  rec=[
      ("¿Qué científico propuso que toda célula proviene de otra célula?", "Rudolf Virchow", "Esa idea se atribuye a Virchow en 1855."),
      ("«El corcho tiene cavidades ordenadas» es una ______ (observación o inferencia).", "Observación", "Describe lo que se ve directamente."),
      ("¿Quién estudiaba plantas: Schleiden o Schwann?", "Schleiden", "Schleiden concluyó en 1838 que las plantas están hechas de células."),
  ],
  und=[
      ("¿Cuál frase es una inferencia? A) «Se ven cavidades de forma regular.» B) «El corcho está formado por pequeñas cámaras.»", "B", "La frase sobre cámaras interpreta lo observado; la otra solo lo describe."),
      ("Schleiden dijo que las plantas son de células y Schwann que los animales también. ¿Qué idea general se apoya con ambas evidencias?", "Que los seres vivos están formados por células", "Juntas muestran que plantas y animales comparten esa característica."),
      ("¿Por qué un microscopio con pocos aumentos limita la conclusión? A) Porque solo muestra formas gruesas y no los detalles pequeños. B) Porque cambia el color de la muestra.", "A", "Sin suficiente aumento no se distinguen estructuras pequeñas."),
  ],
  app=[
      ("Lee: «Leeuwenhoek vio puntos que se movían en una gota de agua de lluvia que había guardado una semana». ¿Cuál es una limitación de esa evidencia? A) No se sabe si los puntos venían del recipiente o del agua; B) Las gotas de agua no se pueden observar.", "A", "Faltan controles sobre el origen de los seres observados."),
      arith("En 1838 Schleiden concluyó algo sobre las plantas y en 1855 Virchow propuso su idea. ¿Cuántos años separan ambos aportes?", "1855-1838", "Se resta 1838 a 1855."),
      ("Una tabla de ejemplo dice: Hooke, corcho, paredes vacías; Leeuwenhoek, gota de agua, seres que se mueven; Schwann, tejidos de animales, células. ¿Con qué material trabajó Leeuwenhoek?", "Con una gota de agua", "La fila de Leeuwenhoek indica la gota de agua."),
  ],
  rea=[
      ("Alguien afirma: «Con la lámina de corcho de Hooke queda probado que las células de todos los seres vivos tienen paredes y están vacías». Explica la falla. A) Se generaliza desde un material con células muertas; B) El corcho no se puede observar.", "A", "El corcho solo muestra paredes de células muertas, no representa a todas las células."),
      ("Un estudiante observa en un dibujo de ejemplo que una célula se divide y origina dos células. ¿Con qué idea de Virchow concuerda? Escríbela en tus palabras.", "Toda célula proviene de otra célula", "La idea de Virchow explica que una célula nueva nace de una célula que ya existía."),
  ],
  cha=[
      ("Schleiden y Schwann creían que las células podían formarse de manera espontánea a partir de material sin células. Virchow sostuvo que toda célula viene de otra. ¿Qué muestra este desacuerdo sobre los modelos? A) Que un modelo puede corregirse con nueva evidencia; B) Que Schleiden y Schwann se equivocaron en todo lo que concluyeron.", "A", "La idea de Virchow corrigió una parte del modelo anterior."),
      ("Datos de ejemplo: se examinaron 30 láminas de tejidos: 12 de plantas, 10 de animales y 8 de hongos. En las 30 se vieron células. ¿Cuántas láminas no eran de plantas ni de animales?", "8", "Son las láminas de hongos: 30 − 12 − 10 = 8."),
  ],
  context=[arith("Un grupo cuenta, en un dibujo de ejemplo de tejido vegetal, 14 células en la primera fila y 14 en la segunda. ¿Cuántas células hay en las dos filas?", "14+14", "Se suman las células de ambas filas.")],
  selfcheck=[("¿Qué diferencia hay entre observación e inferencia?", "La observación es lo que se percibe y la inferencia es la conclusión que se saca de ello", "Se separan para no exagerar la evidencia."), ("¿Qué propuso Schwann en 1839?", "Que los animales están formados por células", "Aplicó la idea de Schleiden a los animales."), ("¿Cómo limita el instrumento a la evidencia?", "Solo permite ver hasta cierto detalle", "Con otro instrumento se pueden corregir las conclusiones.")],
  open_task=task("Completa una tabla de tres columnas (científico, qué observó, qué concluyó) con estos datos: Hooke observó celdillas en corcho; Schleiden estudió plantas; Schwann estudió animales; Virchow reunió evidencia sobre cómo se forman las células. Después escribe una limitación del instrumento de Hooke (un microscopio simple).", "Hooke: celdillas en corcho, concluyó que el corcho está formado por cámaras. Schleiden: plantas, concluyó que están hechas de células. Schwann: animales, igual. Virchow: toda célula viene de otra. Limitación: con pocos aumentos no se ve el interior.", ["cuatro filas completas", "separa observación de conclusión", "limitación coherente con el instrumento"], ["tabla de cuatro filas y una limitación"], ["escribir la misma frase en las dos columnas", "limitación sin relación con el microscopio"], "Pregunta qué dato nuevo cambiaría la conclusión de una de las filas."),
  reinforce="Escribe una observación y una inferencia sobre una gota de agua con puntos que se mueven.",
  extend="Explica por qué una conclusión debe ser prudente cuando el instrumento tiene pocos aumentos.")

L(OA1, 3,
  materials="Este cuaderno y lápiz. Todos los ejemplos están escritos en cada ejercicio.",
  use="Aprenderé a construir y contrastar modelos de la célula: el de Hooke, la teoría celular y el modelo actual. Sirve para explicar cómo cambió una idea científica con la evidencia.",
  prior=["Sé qué observó cada científico.", "Sé que una inferencia necesita evidencia."],
  explain=[
      "La teoría celular reúne tres ideas apoyadas por mucha evidencia. Primera: todos los seres vivos están formados por una o más células. Segunda: la célula es la unidad básica de estructura y función de los seres vivos. Tercera: toda célula proviene de otra célula que ya existía. Esta teoría se fue armando entre los trabajos de Hooke, Leeuwenhoek, Schleiden, Schwann y Virchow.",
      "El modelo de Hooke mostraba celdillas con paredes y sin contenido, y solo hablaba del corcho. El modelo actual agrega que la célula viva tiene membrana, citoplasma y, en muchas células, núcleo y organelos. Contrastar modelos significa comparar qué explica cada uno y qué deja afuera. El modelo antiguo no se descarta por tonto: explicaba lo que su instrumento mostraba.",
      "Un organismo unicelular es un ser vivo formado por una sola célula, como una levadura o una bacteria. Uno pluricelular tiene muchas células, como una planta o una persona. Ambos cumplen la teoría celular. Todo modelo simplifica: un dibujo plano no muestra el volumen de la célula, y por eso tiene límites.",
  ],
  vocab=[("teoría celular", "conjunto de tres ideas sobre las células apoyado por mucha evidencia"), ("unicelular", "formado por una sola célula"), ("pluricelular", "formado por muchas células"), ("organelo", "estructura con una función dentro de la célula"), ("contrastar", "comparar para ver semejanzas y diferencias")],
  worked=[
      ("Qué idea de la teoría usa", "Una persona dice: «Una bacteria es un ser vivo completo formado por una sola célula». ¿Qué idea de la teoría celular se apoya?", ["Reviso las tres ideas.", "La frase dice que la célula es la unidad que forma al ser vivo.", "Corresponde a la primera idea: los seres vivos están formados por células."], "La primera idea: los seres vivos están formados por células"),
      ("Contrastar dos modelos", "Compara: modelo A (celdillas vacías con paredes) y modelo B (célula con membrana, citoplasma y núcleo). ¿Cuál explica mejor a una célula viva?", ["El modelo A solo muestra paredes de células muertas.", "El modelo B incluye partes de una célula viva."], "El modelo B explica mejor a la célula viva"),
  ],
  mistakes=[
      ("Pensar que un modelo antiguo era un error absurdo.", "Explicaba bien lo que su instrumento permitía observar.", "Pregunta qué explicaba y qué dejaba afuera."),
      ("Creer que unicelular quiere decir «sin vida completa».", "Un organismo unicelular realiza todas las funciones vitales en una célula.", "Recuerda que la célula es la unidad básica de la vida."),
  ],
  rec=[
      ("¿Cuántas ideas tiene la teoría celular?", "Tres", "Se resumen en seres vivos hechos de células, unidad básica y origen en otra célula."),
      ("Un ser vivo con muchas células es ______ (unicelular o pluricelular).", "Pluricelular", "El prefijo pluri- significa muchos."),
      ("¿Una levadura está formada por una sola célula: verdadero o falso?", "Verdadero", "Es un organismo unicelular."),
  ],
  und=[
      ("¿Qué idea de la teoría celular corresponde a «una célula nueva nace por la división de otra célula»? A) Toda célula proviene de otra célula; B) Todos los seres vivos tienen núcleo.", "A", "La tercera idea habla del origen de las células."),
      ("¿Cuál es una diferencia entre el modelo de Hooke y el modelo actual? A) El actual incluye membrana y citoplasma; B) El de Hooke incluye núcleo y mitocondrias.", "A", "Hooke solo vio paredes de células muertas."),
      ("Una persona es un ser pluricelular. ¿Cumple la teoría celular?", "Sí", "Está formada por células y esas células provienen de otras células."),
  ],
  app=[
      ("Cinco seres vivos: bacteria, levadura, árbol, perro, mosca. ¿Cuántos son unicelulares?", "2", "La bacteria y la levadura tienen una sola célula."),
      ("Con los mismos cinco seres vivos (bacteria, levadura, árbol, perro, mosca), ¿cuántos son pluricelulares?", "3", "El árbol, el perro y la mosca tienen muchas células."),
      ("Un dibujo plano de una célula en el papel no muestra su volumen. ¿Qué limita ese dibujo? A) Su forma de dos dimensiones; B) Que las células no existen.", "A", "Un modelo plano simplifica una estructura tridimensional."),
  ],
  rea=[
      ("Una afirmación dice: «Si un cuerpo no tiene células, tampoco cumple la teoría celular». ¿Qué ideas de la teoría permiten decirlo? A) Que los seres vivos están formados por células; B) Que toda célula tiene pared.", "A", "Si un cuerpo no tiene células, no cumple la primera idea."),
      ("¿Por qué no se desecha el modelo de Hooke aunque ahora sepamos más? Responde en una frase.", "Porque explicaba lo que su instrumento permitía ver y fue base para modelos posteriores", "La ciencia construye sobre los modelos anteriores."),
  ],
  cha=[
      ("Dos estudiantes discuten: Ana dice que la célula es la unidad básica de estructura y función; Bruno dice que es solo un compartimento vacío. ¿Quién concuerda con la teoría celular y con el modelo actual? Escribe Ana o Bruno.", "Ana", "La célula viva realiza funciones y tiene contenido; no es un compartimento vacío."),
      arith("Un modelo de ejemplo tiene 4 cuadros y cada cuadro representa 25 células de un tejido. ¿Cuántas células representa el modelo completo?", "4*25", "Se multiplica el número de cuadros por las células de cada uno."),
  ],
  context=[("Un trozo de tejido de ejemplo se observa en 3 láminas con 8 células cada una. Ninguna célula parece surgir de la nada. ¿Qué idea de la teoría respalda esta observación: la primera, la segunda o la tercera?", "La tercera", "Las células provienen de otras células ya existentes.")],
  selfcheck=[("Nombra las tres ideas de la teoría celular.", "Seres vivos hechos de células; la célula es la unidad básica; toda célula viene de otra", "Resumen de la teoría."), ("¿Qué es un organismo unicelular?", "Un ser vivo formado por una sola célula", "Ejemplos: bacteria y levadura."), ("¿Por qué todo modelo tiene límites?", "Porque simplifica la realidad", "Deja afuera detalles.")],
  open_task=task("Construye una tabla con dos columnas: «Modelo de Hooke» y «Modelo actual». Incluye al menos tres filas: qué muestra del interior, qué ser vivo describe y qué instrumento usó. Escribe una frase final con un límite de cada modelo.", "Interior: Hooke, vacío con paredes; actual, membrana, citoplasma y núcleo. Seres: Hooke, corcho; actual, todos los seres vivos. Instrumento: Hooke, microscopio simple; actual, microscopios con mayor detalle. Límites: Hooke no vio células vivas; el dibujo actual es plano.", ["tres filas completas", "diferencias correctas", "un límite por cada modelo"], ["tabla y frase final"], ["poner núcleo en el modelo de Hooke", "olvidar los límites"], "Pregunta qué agregaría a la tabla un microscopio con más aumento."),
  reinforce="Escribe un ejemplo de ser unicelular y uno de ser pluricelular.",
  extend="Explica con un ejemplo por qué comparar dos modelos ayuda a ver cómo cambió una idea científica.")

L(OA1, 4,
  materials="Este cuaderno, lápiz y calculadora si quieres. Los datos de los ejercicios son de ejemplo.",
  use="Aprenderé la relación entre el aumento del microscopio, el tamaño de la imagen y el tamaño real de una célula. Sirve para entender por qué mejores instrumentos cambiaron el modelo celular.",
  prior=["Sé que el microscopio agranda las imágenes.", "Sé multiplicar y dividir números enteros."],
  explain=[
      "El aumento de un microscopio óptico se calcula multiplicando el aumento del ocular (la lente por donde se mira) por el del objetivo (la lente cercana a la muestra). Con un ocular de 10 aumentos y un objetivo de 40, el aumento total es 10 × 40 = 400 veces. Mientras más aumento, se ven más detalles, pero se mira una zona más pequeña de la muestra.",
      "Para estimar el tamaño real de algo se usa: tamaño real = tamaño de la imagen ÷ aumento. Si una célula se ve de 4.000 µm de largo en la imagen con 400 aumentos, su tamaño real es 4.000 ÷ 400 = 10 µm. Un micrómetro (µm) es la milésima parte de un milímetro, así que 1 mm = 1.000 µm. Muchas células miden entre 10 y 100 µm.",
      "Hay un límite: el microscopio óptico no permite distinguir estructuras muy pequeñas aunque se aumente más, pues la imagen se vuelve borrosa. En el siglo XX el microscopio electrónico permitió ver el interior de la célula con más detalle y mejorar el modelo. Cada avance técnico es nueva evidencia.",
  ],
  vocab=[("ocular", "lente del microscopio por donde se mira"), ("objetivo", "lente del microscopio cercana a la muestra"), ("aumento total", "producto del aumento del ocular por el del objetivo"), ("micrómetro (µm)", "milésima parte de un milímetro"), ("microscopio electrónico", "instrumento que permite ver estructuras más pequeñas que el óptico")],
  worked=[
      ("Aumento total", "Un microscopio tiene un ocular de 10 y un objetivo de 20. ¿Cuál es el aumento total?", ["Multiplico los dos aumentos.", "10 × 20 = 200."], "200 aumentos"),
      ("Tamaño real", "Una célula se ve de 6.000 µm en la imagen con 300 aumentos. ¿Cuánto mide en realidad?", ["Divido el tamaño de la imagen por el aumento.", "6.000 ÷ 300 = 20."], "20 µm"),
  ],
  mistakes=[
      ("Sumar los aumentos del ocular y del objetivo.", "El aumento total es el producto, no la suma.", "Multiplica ocular por objetivo."),
      ("Creer que con más aumento siempre se ve más detalle.", "El microscopio óptico tiene un límite de detalle.", "Recuerda que más aumento no siempre significa más claridad."),
  ],
  rec=[
      ("¿Cómo se calcula el aumento total: multiplicando o sumando los aumentos del ocular y del objetivo?", "Multiplicando", "El aumento total es el producto de ambos."),
      ("¿Cuántos micrómetros tiene 1 milímetro?", "1.000", "Un micrómetro es la milésima parte de un milímetro."),
      ("Verdadero o falso: el microscopio electrónico permitió ver más detalle del interior de la célula.", "Verdadero", "Cada técnica nueva aporta evidencia adicional."),
  ],
  und=[
      ("Si aumenta el aumento total, ¿qué pasa con la zona de la muestra que se ve? A) Se ve una zona más pequeña; B) Se ve una zona más grande.", "A", "A mayor aumento se mira una porción menor de la muestra."),
      ("¿Para qué sirve dividir el tamaño de la imagen por el aumento? A) Para estimar el tamaño real; B) Para saber cuántas células hay.", "A", "La división deshace el efecto del agrandamiento."),
      ("¿Por qué no se puede ver todo con el microscopio óptico aunque se aumente muchísimo? A) Porque tiene un límite de detalle y la imagen se vuelve borrosa; B) Porque las células desaparecen con la luz.", "A", "La imagen pierde nitidez más allá de ese límite."),
  ],
  app=[
      arith("Un ocular de 15 aumentos se usa con un objetivo de 40 aumentos. ¿Cuántos aumentos totales se obtienen?", "15*40", "Se multiplica el aumento del ocular por el del objetivo."),
      arith("Una célula de una muestra de ejemplo se ve de 5.000 µm en la imagen con 100 aumentos. ¿Cuántos µm mide en realidad?", "5000//100", "Se divide el tamaño de la imagen por el aumento."),
      arith("Un microscopio tiene un ocular de 10 y se quiere llegar a 400 aumentos. ¿Qué aumento debe tener el objetivo?", "400//10", "El aumento total dividido por el ocular da el objetivo."),
  ],
  rea=[
      ("Dos estudiantes miden la misma célula con aumentos distintos: uno obtiene 16.000 µm de imagen con 400 aumentos y otro obtiene 8.000 µm con 200 aumentos. ¿Coinciden los tamaños reales? Responde Sí o No.", "Sí", "Ambos dan 40 µm al dividir la imagen por el aumento."),
      ("Alguien afirma: «Con 1.000 aumentos se ve la célula completa». ¿Qué dato de la clase lo contradice? A) A mayor aumento se ve una zona menor; B) El aumento no cambia el tamaño de la imagen.", "A", "Cuando se aumenta, el campo visible se reduce."),
  ],
  cha=[
      arith("Datos de ejemplo: una célula mide 25 µm de largo y se observa con 400 aumentos. ¿Cuántos µm mide su imagen?", "25*400", "El tamaño de la imagen es el tamaño real multiplicado por el aumento."),
      ("Un museo dice: «Gracias al microscopio, el modelo celular de hoy quedó terminado para siempre». ¿Qué respondes? A) Falso: nuevas técnicas pueden aportar evidencia para corregir el modelo; B) Verdadero: ya no hay nada más que ver.", "A", "La ciencia revisa sus modelos con nuevos instrumentos."),
  ],
  context=[arith("Una célula de ejemplo mide 40 µm. ¿Cuántas células puestas en fila, una junto a otra, cubren 1 mm (1.000 µm)?", "1000//40", "Se divide 1.000 µm por el ancho de cada célula.")],
  selfcheck=[("¿Cómo se calcula el aumento total del microscopio?", "Multiplicando el aumento del ocular por el del objetivo", "Es un producto."), ("¿Cómo se estima el tamaño real de una célula?", "Dividiendo el tamaño de la imagen por el aumento", "Se deshace el agrandamiento."), ("¿Qué aportó el microscopio electrónico?", "Mostrar con más detalle el interior de la célula", "Nueva evidencia para mejorar el modelo.")],
  open_task=task("Resuelve y explica este caso de ejemplo: un microscopio tiene ocular de 10 aumentos y tres objetivos: 4, 10 y 40. Escribe una tabla con los tres aumentos totales. Luego: una célula se ve de 3.000 µm con el objetivo de 10; calcula su tamaño real y explica en una frase por qué el resultado sería el mismo con otro objetivo.", "Totales: 40, 100 y 400. Con el objetivo de 10 el aumento total es 100; tamaño real 3.000 ÷ 100 = 30 µm. Con otro objetivo la imagen cambia de tamaño, pero también el aumento, y el cociente da 30 µm.", ["tres aumentos totales correctos", "usa tamaño de imagen ÷ aumento", "explica por qué el real no cambia"], ["tabla, cálculo y explicación"], ["usar solo el aumento del objetivo", "no convertir la explicación en una frase"], "Pregunta qué pasaría con la imagen si el ocular fuera de 15 aumentos."),
  reinforce="Calcula el aumento total de un ocular de 10 con un objetivo de 100.",
  extend="Explica por qué mejores instrumentos pueden obligar a corregir un modelo científico.")

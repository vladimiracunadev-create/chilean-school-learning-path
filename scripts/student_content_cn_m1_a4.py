"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 07 (fotosíntesis y respiración en el ecosistema) y OA 08 (impactos humanos, fenómenos naturales y sustentabilidad)."""
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


OA7 = "CN1M OA 07"
OA8 = "CN1M OA 08"

# ---------------------------------------------------------------- OA 07

L(OA7, 1,
  materials="Este cuaderno y lápiz. Las ecuaciones y los casos están escritos en los ejercicios; no necesitas laboratorio.",
  use="Aprenderé qué ocurre en la fotosíntesis y en la respiración celular y cómo formular preguntas investigables sobre ambas. Sirve para entender el flujo de energía y el ciclo de la materia en un ecosistema.",
  prior=["Sé que las plantas son productores.", "Sé qué es el dióxido de carbono y el oxígeno."],
  explain=[
      "La fotosíntesis ocurre en los cloroplastos de las células vegetales. Con la energía de la luz, la planta transforma dióxido de carbono (CO2) y agua (H2O) en glucosa, un azúcar, y libera oxígeno (O2). En palabras: dióxido de carbono + agua + luz → glucosa + oxígeno. Así la energía de la luz queda guardada en la glucosa.",
      "La respiración celular ocurre en las mitocondrias de casi todas las células, tanto de plantas como de animales. La célula usa oxígeno para descomponer la glucosa y obtiene energía utilizable (ATP), liberando dióxido de carbono y agua. En palabras: glucosa + oxígeno → dióxido de carbono + agua + energía. Las plantas hacen fotosíntesis y respiración; los animales solo respiración.",
      "Una pregunta investigable sobre estos procesos indica qué se mide. «¿Cuántas burbujas por minuto libera una planta acuática cuando la lámpara está a 20 cm?» se contesta contando. «¿Es mejor la fotosíntesis que la respiración?» no, porque son procesos complementarios y la pregunta es de opinión.",
  ],
  vocab=[("fotosíntesis", "proceso que transforma CO2 y agua en glucosa y oxígeno con luz"), ("respiración celular", "proceso que obtiene energía de la glucosa usando oxígeno"), ("cloroplasto", "estructura de la célula vegetal donde ocurre la fotosíntesis"), ("mitocondria", "estructura de la célula donde ocurre la respiración celular"), ("ATP", "molécula que entrega energía utilizable a la célula")],
  worked=[
      ("Reconocer el proceso", "Una célula usa oxígeno para descomponer glucosa y libera CO2 y agua. ¿Qué proceso es?", ["Revisa qué se consume: glucosa y oxígeno.", "Revisa qué se libera: CO2 y agua."], "Respiración celular"),
      ("Mejorar una pregunta", "Mejora «¿Es bonita la fotosíntesis?» para que se pueda investigar.", ["Quito la palabra de opinión.", "Indico qué se mide: burbujas de oxígeno de una planta acuática en un minuto.", "Queda: «¿Cuántas burbujas por minuto libera una planta acuática bajo una lámpara a 20 cm?»"], "«¿Cuántas burbujas por minuto libera una planta acuática bajo una lámpara a 20 cm?»"),
  ],
  mistakes=[
      ("Decir que las plantas hacen fotosíntesis de día y respiración solo de noche.", "Respiran siempre; de día además hacen fotosíntesis.", "Recuerda que la respiración ocurre las 24 horas."),
      ("Pensar que la glucosa se forma de la tierra.", "La glucosa se forma a partir de CO2 y agua con luz.", "Revisa los reactantes de la fotosíntesis."),
  ],
  rec=[
      ("¿Qué gas libera una planta en la fotosíntesis?", "Oxígeno", "Es un producto de la fotosíntesis."),
      ("Completa: la respiración celular ocurre en las ______ (mitocondrias o cloroplastos).", "Mitocondrias", "Allí se obtiene energía de la glucosa."),
      ("Verdadero o falso: los animales hacen respiración celular.", "Verdadero", "Todas las células vivas la realizan."),
  ],
  und=[
      ("¿Cuáles son los reactantes de la fotosíntesis? A) CO2 y agua; B) Glucosa y oxígeno.", "A", "La glucosa y el oxígeno son productos."),
      ("¿Qué energía transforma la fotosíntesis? A) La luz en energía química de la glucosa; B) La glucosa en luz.", "A", "La energía se guarda en la glucosa."),
      ("¿Qué obtiene una célula al hacer respiración celular?", "Energía utilizable (ATP)", "Es el objetivo del proceso."),
  ],
  app=[
      ("¿Cuál es una pregunta investigable? A) ¿Cuántas burbujas libera una planta acuática en un minuto a 20 cm de la lámpara?; B) ¿Es linda una planta acuática?", "A", "Se contesta contando burbujas."),
      ("Una planta se deja una semana en oscuridad total y sus hojas se ponen amarillas. ¿Qué proceso no puede realizar? A) Fotosíntesis; B) Respiración celular.", "A", "Sin luz no se produce glucosa."),
      arith("Una planta acuática de ejemplo libera 18 burbujas por minuto. ¿Cuántas libera en 5 minutos si el ritmo se mantiene?", "18*5", "Se multiplica el ritmo por los minutos."),
  ],
  rea=[
      ("Un compañero dice: «Las plantas no respiran, solo hacen fotosíntesis». ¿Qué evidencia lo contradice? A) Sus células necesitan obtener energía de la glucosa, que lo hacen con la respiración celular; B) Las plantas no tienen células.", "A", "Toda célula viva necesita energía utilizable."),
      ("En un frasco cerrado y oscuro hay semillas germinando. Se observa que el nivel de CO2 sube. ¿Qué proceso lo explica? A) La respiración de las semillas; B) La fotosíntesis de las semillas.", "A", "Las semillas liberan CO2 al respirar."),
  ],
  cha=[
      ("Dos frascos con plantas de ejemplo: el A está al sol y el B en un clóset. Después de 6 horas, el A tiene 30 burbujas y el B ninguna. ¿Qué variable cambió entre los dos frascos? A) La luz; B) El tamaño de la planta.", "A", "Es la única condición que se cambió."),
      arith("Una planta de ejemplo hace fotosíntesis 8 horas al día y libera 12 burbujas por hora. ¿Cuántas libera en 3 días?", "8*12*3", "Se multiplican horas, burbujas por hora y días."),
  ],
  context=[arith("En un acuario de ejemplo hay 6 plantas y cada una libera 15 burbujas por minuto. ¿Cuántas burbujas por minuto libera el acuario?", "6*15", "Se multiplica el número de plantas por las burbujas de cada una.")],
  selfcheck=[("¿Dónde ocurre la fotosíntesis?", "En los cloroplastos", "Allí está la clorofila que capta la luz."), ("¿Qué productos tiene la respiración celular?", "CO2, agua y energía", "Se libera el CO2 y el agua."), ("¿Qué hace investigable a una pregunta?", "Que indica qué se mide", "Se contesta con observaciones o conteos.")],
  open_task=task("Completa en una hoja una tabla de dos columnas, fotosíntesis y respiración celular, con estas filas: dónde ocurre, qué usa, qué produce, qué energía interviene. Después escribe dos preguntas investigables sobre una planta acuática y una lámpara de escritorio (por ejemplo, qué mides y qué cambias).", "Fotosíntesis: cloroplasto; usa CO2, agua y luz; produce glucosa y oxígeno; la luz pasa a energía química. Respiración: mitocondria; usa glucosa y oxígeno; produce CO2, agua y ATP. Preguntas: «¿Cuántas burbujas por minuto libera la planta a 10 cm y a 40 cm de la lámpara?» y «¿Cuántas burbujas libera en 5 minutos con la lámpara encendida y con la lámpara apagada?».", ["tabla completa y correcta", "dos preguntas con algo que medir", "no confunde reactantes y productos"], ["tabla y dos preguntas"], ["invertir reactantes y productos", "preguntas de opinión"], "Pregunta qué materiales de casa usarías para medir una de tus preguntas."),
  reinforce="Escribe en palabras la ecuación de la fotosíntesis.",
  extend="Explica por qué la fotosíntesis y la respiración celular se complementan.")

L(OA7, 2,
  materials="Este cuaderno y lápiz. Los datos del experimento de la planta acuática son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a examinar los datos de un experimento de fotosíntesis y respiración, a distinguir grupo control y variable cambiada. Sirve para sacar conclusiones con evidencia.",
  prior=["Sé qué ocurre en la fotosíntesis y en la respiración celular.", "Sé leer tablas."],
  explain=[
      "Un experimento compara condiciones. La variable independiente es la que el investigador cambia (por ejemplo, la distancia de la lámpara). La variable dependiente es la que mide (por ejemplo, las burbujas por minuto). Las variables controladas se mantienen iguales (la misma planta, el mismo tiempo, la misma temperatura). El grupo control es la condición de comparación.",
      "En el experimento de ejemplo, una planta acuática bajo una lámpara libera burbujas de oxígeno. Si cambias la distancia de la lámpara, cambia la cantidad de luz y también las burbujas. Con el mismo tipo de planta y el mismo tiempo, las diferencias se deben a la luz. Los datos se registran en una tabla y se repiten varias veces para disminuir errores.",
      "Para leer la evidencia, se compara cada dato con el control y se busca un patrón. Una conclusión debe citar datos y declarar una limitación, como el pequeño número de repeticiones o la dificultad de contar burbujas con exactitud.",
  ],
  vocab=[("variable independiente", "la que cambia el investigador"), ("variable dependiente", "la que se mide"), ("variable controlada", "la que se mantiene igual"), ("grupo control", "condición usada como comparación"), ("repetición", "volver a hacer una medición para dar confianza")],
  worked=[
      ("Identificar variables", "Se mide cuántas burbujas libera una planta cuando la lámpara está a 10, 20 y 40 cm. ¿Cuál es la variable independiente?", ["Pregunto qué cambia el investigador.", "Cambia la distancia de la lámpara."], "La distancia de la lámpara"),
      ("Leer un dato", "Tabla de ejemplo: lámpara a 10 cm, 30 burbujas/min; a 20 cm, 15; a 40 cm, 8. ¿Dónde hay más fotosíntesis?", ["Más burbujas indican más oxígeno liberado.", "El mayor valor es 30, a 10 cm."], "A 10 cm de la lámpara"),
  ],
  mistakes=[
      ("Cambiar dos variables a la vez en un experimento.", "No se sabría cuál produjo la diferencia.", "Cambia una sola variable y controla las demás."),
      ("Concluir con una sola medición.", "Un dato aislado puede ser un error.", "Repite la medición y calcula un promedio."),
  ],
  rec=[
      ("¿Cómo se llama la variable que mide el investigador?", "Dependiente", "Es el resultado que se observa."),
      ("Completa: las condiciones que se mantienen iguales son las variables ______ (controladas o independientes).", "Controladas", "Así se aísla el efecto de la variable cambiada."),
      ("Verdadero o falso: conviene repetir las mediciones.", "Verdadero", "Las repeticiones dan más confianza."),
  ],
  und=[
      ("¿Por qué se usa la misma planta en todos los casos? A) Para que la diferencia se deba a la luz y no a la planta; B) Para ahorrar plantas.", "A", "Es una variable controlada."),
      ("¿Qué indican más burbujas en un minuto? A) Más oxígeno liberado, es decir, más fotosíntesis; B) Menos fotosíntesis.", "A", "Las burbujas son oxígeno de la fotosíntesis."),
      ("¿Qué es un grupo control?", "Una condición de comparación", "Permite ver el efecto de cambiar la variable."),
  ],
  app=[
      ("Tabla de ejemplo: lámpara a 15 cm, 20 burbujas por minuto; a 30 cm, 10; a 60 cm, 5. ¿Cuántas burbujas por minuto se registran a 30 cm?", "10", "Es el dato de la fila de 30 cm."),
      arith("Con la misma tabla (a 15 cm, 20; a 30 cm, 10; a 60 cm, 5), ¿cuántas burbujas más hay a 15 cm que a 60 cm?", "20-5", "Se resta el valor menor al mayor."),
      ("Tres mediciones de ejemplo a 20 cm: 14, 16 y 18 burbujas por minuto. ¿Cuál es el promedio? A) 16; B) 18.", "A", "La suma es 48 y 48 dividido por 3 es 16."),
  ],
  rea=[
      ("Un estudiante cambia a la vez la distancia de la lámpara y el tipo de planta. ¿Cuál es la crítica? A) No sabrá cuál de los dos cambios produjo la diferencia; B) Las plantas no responden a la luz.", "A", "Debe cambiar una sola variable."),
      ("Tabla de ejemplo: a 10 cm, 40; a 20 cm, 20; a 40 cm, 10. Un compañero concluye: «Al duplicar la distancia, las burbujas se reducen a la mitad». ¿Es correcto? A) Sí, de 10 a 20 cm y de 20 a 40 cm cada duplicación reduce a la mitad; B) No, porque son números distintos.", "A", "40 pasa a 20 y 20 pasa a 10."),
  ],
  cha=[
      ("En un experimento de ejemplo una planta a 20 cm libera 15 burbujas y a 5 cm libera 60. ¿Cuántas veces más burbujas libera a 5 cm que a 20 cm?", "4", "60 dividido por 15 es 4."),
      ("Un estudiante concluye que «la luz hace crecer la planta» a partir de que a más luz hay más burbujas en 5 minutos. ¿Qué crítica es más razonable? A) Midió burbujas de oxígeno y no el crecimiento; B) Las burbujas no son oxígeno.", "A", "La variable medida no es el crecimiento."),
  ],
  context=[arith("Un grupo de ejemplo repite 4 veces la medición a 10 cm y obtiene 28, 30, 32 y 30 burbujas por minuto. ¿Cuál es la suma de las 4 mediciones?", "28+30+32+30", "Se suman los cuatro datos.")],
  selfcheck=[("¿Cuál es la variable independiente en el experimento de la lámpara?", "La distancia de la lámpara", "Es la que cambia el investigador."),
             ("¿Qué mide la variable dependiente?", "Las burbujas por minuto", "Es el resultado."),
             ("¿Por qué conviene repetir las mediciones?", "Para disminuir errores y dar confianza", "Un dato aislado puede ser un error.")],
  open_task=task("Con esta tabla de ejemplo de una planta acuática, calcula el promedio de cada distancia y escribe una conclusión de dos oraciones con una limitación. Tabla: 10 cm: 40, 42, 38 burbujas por minuto; 20 cm: 20, 22, 18; 40 cm: 10, 9, 11.", "Promedios: 10 cm, 40; 20 cm, 20; 40 cm, 10. A mayor distancia de la lámpara, menos burbujas. Limitación: contar burbujas a ojo puede tener errores y son solo tres repeticiones.", ["calcula tres promedios", "describe el patrón con datos", "declara una limitación"], ["tabla de promedios y conclusión"], ["no calcular el promedio", "no mencionar una limitación"], "Pregunta qué otra variable podría influir, como la temperatura."),
  reinforce="Nombra una variable independiente, una dependiente y una controlada de este experimento.",
  extend="Explica por qué contar burbujas es una medición indirecta de la fotosíntesis.")

L(OA7, 3,
  materials="Hojas y lápices de colores. Si no tienes, escribe los nombres en cajas y une con flechas.",
  use="Aprenderé a modelar cómo la fotosíntesis y la respiración conectan el flujo de energía con el ciclo de la materia. Sirve para explicar por qué la materia circula y la energía no.",
  prior=["Sé las ecuaciones de la fotosíntesis y la respiración celular.", "Sé qué es un ciclo biogeoquímico."],
  explain=[
      "Los productos de la fotosíntesis (glucosa y oxígeno) son los reactantes de la respiración celular. Y los productos de la respiración (CO2 y agua) son los reactantes de la fotosíntesis. Por eso la materia, es decir, el carbono, el oxígeno y el hidrógeno, circula en un ciclo entre los seres vivos y el ambiente.",
      "La energía, en cambio, no circula. Entra a la biosfera como luz, se guarda en la glucosa, pasa a los consumidores cuando comen y finalmente se pierde como calor en la respiración y en otras funciones. El Sol debe aportar energía continuamente para mantener la vida.",
      "Un modelo de dos cajas con flechas ayuda a explicarlo: caja 1 (productores: fotosíntesis y respiración) y caja 2 (consumidores: solo respiración), conectadas por la glucosa que pasa al comer y por el CO2 que vuelve al aire. Un modelo simplifica: no muestra otros procesos como la descomposición ni la combustión.",
  ],
  vocab=[("biosfera", "conjunto de todos los seres vivos y los lugares donde viven"), ("energía química", "energía almacenada en las moléculas como la glucosa"), ("calor", "forma de energía que se disipa al ambiente"), ("reactante", "sustancia que se transforma en un proceso"), ("producto", "sustancia que se forma en un proceso")],
  worked=[
      ("Enlazar los procesos", "¿Qué producto de la fotosíntesis usa la respiración celular como reactante?", ["Miro los productos de la fotosíntesis: glucosa y oxígeno.", "La respiración usa ambos."], "Glucosa y oxígeno"),
      ("Seguir la energía", "La luz se guarda en la glucosa de una planta. Un conejo la come. ¿Qué pasa con parte de esa energía al final?", ["El conejo la usa para moverse y respirar.", "Parte se libera como calor."], "Se pierde como calor"),
  ],
  mistakes=[
      ("Decir que la energía se recicla como la materia.", "La energía se disipa como calor y debe renovarse con la luz del Sol.", "Dibuja la energía con flechas que no vuelven."),
      ("Pensar que el oxígeno que respiramos viene del CO2 que exhalamos.", "Sale del agua y se libera en la fotosíntesis; el CO2 aporta el carbono.", "Revisa de dónde viene cada átomo."),
  ],
  rec=[
      ("¿Qué forma de energía llega a la biosfera desde el Sol?", "Luz", "La fotosíntesis la transforma."),
      ("Completa: la materia en la biosfera ______ (circula o fluye en un solo sentido).", "Circula", "Se recicla en ciclos."),
      ("Verdadero o falso: la energía se pierde como calor en las funciones vitales.", "Verdadero", "Por eso debe renovarse."),
  ],
  und=[
      ("¿Qué une la fotosíntesis con la respiración? A) Los productos de una son reactantes de la otra; B) Ambas ocurren solo de noche.", "A", "Forman un ciclo de materia."),
      ("¿Por qué la vida necesita luz del Sol continuamente? A) Porque la energía se disipa como calor y no se recicla; B) Porque la materia se acaba.", "A", "La energía no circula."),
      ("¿En qué molécula queda guardada la energía de la luz?", "Glucosa", "Es la energía química del alimento."),
  ],
  app=[
      ("Modelo de ejemplo: luz → fotosíntesis → glucosa → respiración → calor. ¿Qué flecha muestra el flujo de energía? A) Todo el recorrido de luz a calor; B) Solo glucosa a respiración.", "A", "La energía recorre todo el modelo y termina como calor."),
      arith("Una planta de ejemplo almacena 120 unidades de energía en glucosa y usa 45 en su respiración. ¿Cuántas unidades quedan almacenadas?", "120-45", "Se resta lo usado a lo almacenado."),
      ("Un modelo dibuja flechas de CO2 y agua hacia la fotosíntesis y de glucosa y oxígeno hacia la respiración. ¿Qué materia circula entre ambos procesos? A) Carbono, hidrógeno y oxígeno; B) Solo calor.", "A", "Los elementos pasan de un proceso a otro."),
  ],
  rea=[
      ("Un compañero dice que, si no hubiera descomponedores, el ciclo de la materia igual se cerraría. ¿Qué dato lo contradice? A) Los restos de seres vivos quedarían acumulados con su carbono sin volver al aire; B) Los descomponedores no respiran.", "A", "La descomposición también libera CO2."),
      ("Un museo muestra un dibujo donde la energía pasa del consumidor de vuelta a la luz del Sol. ¿Cuál es el error? A) La energía no vuelve: se pierde como calor; B) Los consumidores no existen.", "A", "La energía fluye en un solo sentido."),
  ],
  cha=[
      arith("Una cadena de ejemplo almacena 1.000 unidades de energía en los productores. Si en cada nivel solo pasa el 10 % al siguiente, ¿cuántas llegan al segundo consumidor?", "1000//10//10", "Se divide entre 10 dos veces."),
      ("Un modelo supone que las plantas solo hacen fotosíntesis. ¿Qué proceso falta para explicar cómo usan la energía de la glucosa? A) La respiración celular; B) La condensación.", "A", "Las plantas también respiran."),
  ],
  context=[arith("Una escuela de ejemplo planta 25 árboles. Cada árbol hace fotosíntesis con 50 unidades de luz al día. ¿Cuántas unidades usan entre todos?", "25*50", "Se multiplica el número de árboles por las unidades de cada uno.")],
  selfcheck=[("¿Qué circula en el ecosistema, la materia o la energía?", "La materia", "La energía fluye en un solo sentido."), ("¿Cómo termina la energía de la luz?", "Como calor", "Se disipa en las funciones vitales."), ("¿Qué une los dos procesos?", "Los productos de uno son los reactantes del otro", "Forman un ciclo.")],
  open_task=task("Dibuja un modelo con cuatro cajas (CO2 y agua; glucosa y oxígeno; planta; animal) y flechas que muestren el ciclo de la materia, y otra flecha distinta (con otro color) que muestre el flujo de la energía desde la luz hasta el calor. Escribe una limitación de tu modelo.", "CO2 y agua → fotosíntesis en la planta → glucosa y oxígeno → animal respira → CO2 y agua. Energía: luz → glucosa → animal → calor. Limitación: no muestra la descomposición.", ["ciclo de materia cerrado", "flujo de energía en un solo sentido", "limitación coherente"], ["dibujo y frase"], ["cerrar la energía en ciclo", "olvidar el calor"], "Pregunta qué agregarías al modelo para incluir a los descomponedores."),
  reinforce="Dibuja un esquema simple que una la fotosíntesis y la respiración celular.",
  extend="Explica por qué la energía solar es indispensable aunque la materia se recicle.")

L(OA7, 4,
  materials="Este cuaderno, lápiz y regla. Los datos de fotosíntesis son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a relacionar la rapidez de la fotosíntesis con la luz, la temperatura y el CO2, e interpretar un gráfico con un límite de saturación. Sirve para predecir cómo reaccionan los cultivos.",
  prior=["Sé leer tablas y gráficos de líneas.", "Sé controlar variables en un experimento."],
  explain=[
      "La rapidez de la fotosíntesis depende de varios factores. Con más luz, aumenta, hasta un punto de saturación: desde allí, aunque haya más luz, no sube porque otro factor limita el proceso (por ejemplo, el CO2 o las enzimas). La temperatura también influye: sube la rapidez con el calor moderado, pero baja si es demasiado alta.",
      "En un gráfico de líneas, el eje horizontal muestra la variable independiente (luz, temperatura) y el eje vertical muestra la dependiente (rapidez de fotosíntesis). Una curva que sube y luego se aplana indica saturación. Una curva que sube y luego baja indica un óptimo, es decir, un valor donde el proceso es máximo.",
      "Un factor limitante es el que, por ser escaso, determina la rapidez máxima. Si el CO2 es escaso, más luz no ayuda. Por eso en invernaderos se controlan la luz, la temperatura y el CO2. Los datos se usan para predecir dentro del rango medido; fuera de él, la predicción es dudosa.",
  ],
  vocab=[("saturación", "punto desde el cual más luz no aumenta la fotosíntesis"), ("factor limitante", "el factor escaso que fija la rapidez máxima"), ("óptimo", "valor en que el proceso es máximo"), ("rapidez de fotosíntesis", "cantidad de oxígeno o glucosa formada por unidad de tiempo"), ("invernadero", "recinto donde se controlan condiciones de cultivo")],
  worked=[
      ("Leer saturación", "Tabla de ejemplo: luz 10, rapidez 5; luz 20, rapidez 10; luz 30, rapidez 15; luz 40, rapidez 16; luz 50, rapidez 16. ¿Desde qué luz hay saturación?", ["Busco dónde la rapidez deja de aumentar.", "Es 16 con 40 y con 50."], "Desde una luz cercana a 40"),
      ("Reconocer un factor limitante", "Con luz máxima la rapidez es baja y sube al agregar CO2. ¿Cuál era el factor limitante?", ["Al agregar CO2 aumentó la rapidez.", "El CO2 era el escaso."], "El CO2"),
  ],
  mistakes=[
      ("Pensar que más luz siempre significa más fotosíntesis.", "Existe un punto de saturación.", "Busca dónde la curva se aplana."),
      ("Predecir lejos del rango de los datos.", "No se sabe si el patrón continúa.", "Declara que fuera del rango es incierto."),
  ],
  rec=[
      ("¿Cómo se llama el punto desde el cual más luz no aumenta la fotosíntesis?", "Saturación", "Otro factor limita."),
      ("Completa: el factor escaso que fija la rapidez máxima es el factor ______ (limitante o óptimo).", "Limitante", "Controla el proceso."),
      ("Verdadero o falso: una temperatura demasiado alta puede disminuir la fotosíntesis.", "Verdadero", "Afecta las enzimas."),
  ],
  und=[
      ("Una curva que sube y luego se aplana indica ______ (saturación o óptimo).", "Saturación", "El proceso llega a un máximo estable."),
      ("En un gráfico de la luz y la fotosíntesis, ¿qué va en el eje horizontal? A) La luz, que es la variable independiente; B) La rapidez de fotosíntesis.", "A", "La variable que se cambia va en el eje horizontal."),
      ("¿Por qué se controla el CO2 en un invernadero?", "Porque puede ser el factor limitante", "Con poco CO2, más luz no ayuda."),
  ],
  app=[
      ("Tabla de ejemplo: luz 20, rapidez 8; luz 40, rapidez 16; luz 60, rapidez 24; luz 80, rapidez 26; luz 100, rapidez 26. ¿Cuál es la rapidez máxima?", "26", "Es el valor más alto y se mantiene."),
      arith("Con la misma tabla (luz 20, rapidez 8; luz 40, 16; luz 60, 24; luz 80, 26), ¿cuánto aumentó la rapidez entre luz 60 y luz 80?", "26-24", "Se resta el valor de luz 60 al de luz 80."),
      ("En la misma tabla, entre luz 20 y luz 60, la rapidez es proporcional a la luz (por cada 20 de luz suben 8). ¿Qué rapidez se predice con luz 30? A) 12; B) 16.", "A", "A luz 20 la rapidez es 8 y por cada 10 más de luz suben 4, así que con 30 son 12."),
  ],
  rea=[
      ("Un agricultor de ejemplo duplica las lámparas de su invernadero, pero la rapidez no aumenta. ¿Qué hipótesis es más razonable? A) Otro factor, como el CO2, es limitante; B) Las plantas dejaron de necesitar luz.", "A", "Se alcanzó la saturación."),
      ("Un gráfico de ejemplo sube hasta 30 °C y luego baja. Un compañero dice que a 45 °C la rapidez será mayor. ¿Qué responderías? A) Los datos muestran que baja después de 30 °C; B) Tiene razón.", "A", "La curva tiene un óptimo."),
  ],
  cha=[
      ("Datos de ejemplo: una planta con luz 50 libera 20 burbujas por minuto y, con luz 100, 22 burbujas. Otra planta de la misma especie con luz 50 y más CO2 libera 34 burbujas. ¿Cuántas burbujas más libera por el CO2 extra?", "14", "34 menos 20 es 14."),
      ("Un proyecto propone cultivar plantas en una sala sin ventanas con una lámpara. ¿Qué dato necesita medir para evaluarlo? A) La intensidad de luz y la rapidez de fotosíntesis con esa lámpara; B) El color de las paredes.", "A", "Debe comprobar que la luz suficiente permite la fotosíntesis."),
  ],
  context=[arith("En un invernadero de ejemplo, 8 bandejas de lechuga reciben 6 horas de luz diaria. ¿Cuántas horas de luz reciben entre todas las bandejas en un día?", "8*6", "Se multiplica el número de bandejas por las horas.")],
  selfcheck=[("¿Qué es la saturación?", "El punto desde el cual más luz no aumenta la fotosíntesis", "Otro factor limita el proceso."), ("¿Qué es un factor limitante?", "El factor escaso que fija la rapidez máxima", "Controla el proceso."), ("¿Qué indica una curva que sube y luego baja?", "Un valor óptimo", "Después del óptimo el proceso decae.")],
  open_task=task("Con la tabla de ejemplo, haz un gráfico de líneas y responde. Tabla: luz 0, rapidez 0; luz 25, rapidez 10; luz 50, rapidez 20; luz 75, rapidez 28; luz 100, rapidez 30; luz 125, rapidez 30. ¿Dónde empieza la saturación? ¿Qué factor podría ser limitante? Escribe una predicción para luz 40 y di si es confiable.", "Saturación desde cerca de luz 100. Factor posible: CO2. Predicción para luz 40: aproximadamente 16, confiable porque está dentro del rango y en la parte lineal.", ["gráfico con ejes rotulados", "identifica la saturación", "predice dentro del rango y la justifica"], ["gráfico y respuestas"], ["extrapolar sin advertir", "no rotular los ejes"], "Pregunta qué experimento harías para comprobar el factor limitante."),
  reinforce="Dibuja una curva con saturación y marca el punto.",
  extend="Explica por qué un cultivo no mejora si solo se aumenta un factor.")

# ---------------------------------------------------------------- OA 08

L(OA8, 1,
  materials="Este cuaderno y lápiz. Los datos y casos están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé a distinguir recursos renovables y no renovables y a formular preguntas investigables sobre acciones humanas y fenómenos naturales. Sirve para plantear evaluaciones con evidencia.",
  prior=["Sé qué es un ecosistema y que está en equilibrio.", "Sé que una pregunta investigable se contesta con datos."],
  explain=[
      "Los recursos naturales son elementos de la naturaleza que las personas usan. Un recurso renovable se repone en un tiempo corto si se usa con cuidado: el agua, el bosque, los peces. Un recurso no renovable se repone tan lentamente que, al usarlo, se agota: el petróleo, el carbón y los minerales.",
      "Las acciones humanas cambian los ecosistemas. La conservación ambiental protege áreas y especies. Los cultivos transforman el suelo. La forestación planta árboles donde no había; la deforestación corta bosques. Los fenómenos naturales, como las sequías y las erupciones volcánicas, también alteran el equilibrio, pero ocurren sin acción humana.",
      "Una pregunta investigable indica qué se mide y dónde. «¿Cuántas hectáreas de bosque hay en una zona de ejemplo antes y después de talar?» se contesta con datos. «¿Es malo talar un bosque?» no, porque mezcla opiniones. Un desarrollo sustentable busca satisfacer las necesidades de hoy sin dañar las de las generaciones futuras.",
  ],
  vocab=[("recurso renovable", "recurso que se repone en poco tiempo si se usa con cuidado"), ("recurso no renovable", "recurso que se agota porque se repone muy lentamente"), ("deforestación", "tala de bosques sin reposición"), ("forestación", "plantación de árboles en un terreno sin bosque"), ("desarrollo sustentable", "satisfacer necesidades actuales sin dañar las de generaciones futuras")],
  worked=[
      ("Clasificar recursos", "Clasifica el agua dulce de un río y el petróleo.", ["El agua del río se repone con la lluvia.", "El petróleo tarda millones de años en formarse."], "Agua: renovable; petróleo: no renovable"),
      ("Mejorar una pregunta", "Mejora «¿Es terrible la deforestación?» para que sea investigable.", ["Quito la palabra de opinión.", "Indico qué se mide: hectáreas de bosque en una zona antes y después de talar.", "Queda: «¿Cuántas hectáreas de bosque se perdieron en una zona de ejemplo entre dos años?»"], "«¿Cuántas hectáreas de bosque se perdieron en una zona de ejemplo entre dos años?»"),
  ],
  mistakes=[
      ("Pensar que renovable significa «infinito».", "Un recurso renovable se agota si se usa más rápido de lo que se repone.", "Compara la rapidez de uso y de reposición."),
      ("Creer que todo cambio natural es dañino y todo cambio humano también.", "Un fenómeno natural puede provocar cambios grandes; una acción humana puede proteger.", "Evalúa cada caso con datos."),
  ],
  rec=[
      ("¿Cómo se llama el recurso que se repone en poco tiempo si se usa con cuidado?", "Renovable", "Por ejemplo, el agua o el bosque."),
      ("Completa: el petróleo es un recurso ______ (renovable o no renovable).", "No renovable", "Tarda millones de años en formarse."),
      ("Verdadero o falso: una erupción volcánica es un fenómeno natural.", "Verdadero", "Ocurre sin acción humana."),
  ],
  und=[
      ("¿Qué es la deforestación? A) La tala de bosques sin reposición; B) La plantación de árboles.", "A", "La plantación es forestación."),
      ("¿Qué busca un desarrollo sustentable? A) Cubrir necesidades actuales sin dañar las de futuras generaciones; B) Usar todos los recursos ahora.", "A", "Equilibra el presente y el futuro."),
      ("¿Un pez de mar es un recurso renovable o no renovable, si se pesca con cuidado?", "Renovable", "La población se repone al reproducirse."),
  ],
  app=[
      ("¿Cuál es una pregunta investigable? A) ¿Cuántas hectáreas de bosque nativo hay en una zona en dos años distintos?; B) ¿Es feo ver una ladera sin árboles?", "A", "Se contesta con datos medibles."),
      arith("Una zona de ejemplo tenía 500 hectáreas de bosque y se talaron 120. ¿Cuántas hectáreas quedan?", "500-120", "Se resta lo talado."),
      ("Un pastizal de ejemplo se seca por una sequía. ¿Es un fenómeno natural o una acción humana? A) Fenómeno natural; B) Acción humana.", "A", "La sequía ocurre sin intervención humana."),
  ],
  rea=[
      ("Un compañero dice: «Como el agua es renovable, nunca se acaba». ¿Qué responderías? A) Se agota si se usa más rápido de lo que se repone; B) Tiene razón.", "A", "La renovación tiene una rapidez limitada."),
      ("Un estudiante sostiene que una forestación siempre mejora un ecosistema. ¿Qué dato falta? A) Qué especies se plantan y qué había antes; B) Cuánto mide cada árbol.", "A", "Plantar especies no adecuadas puede cambiar el equilibrio."),
  ],
  cha=[
      ("Un río de ejemplo repone 400 litros de agua por segundo, y una ciudad usa 300. ¿Cuántos litros por segundo quedan para el ecosistema, sin otros usos?", "100", "400 menos 300 es 100."),
      ("Un informe de ejemplo mide la pérdida de bosque por año: 40, 35 y 50 hectáreas. ¿Cuántas hectáreas se perdieron en los 3 años?", "125", "40 más 35 más 50 es 125."),
  ],
  context=[arith("Una comunidad de ejemplo planta 8 hileras de 15 árboles cada una en un terreno sin bosque. ¿Cuántos árboles planta?", "8*15", "Se multiplica el número de hileras por los árboles de cada una.")],
  selfcheck=[("¿Qué diferencia hay entre recurso renovable y no renovable?", "El renovable se repone en poco tiempo y el no renovable se agota", "Cambia la rapidez de reposición."), ("¿Qué es la forestación?", "Plantar árboles donde no había bosque", "Es lo contrario de la deforestación."), ("Da un fenómeno natural que altere un ecosistema.", "Una sequía o una erupción volcánica", "Ocurren sin acción humana.")],
  open_task=task("Con esta lista de ejemplo, clasifica cada elemento como renovable o no renovable: agua de lluvia, carbón, bosque nativo, cobre, peces de un lago, petróleo. Después escribe dos preguntas investigables sobre la deforestación de una zona de ejemplo (qué mides y en qué tiempo).", "Renovables: agua de lluvia, bosque nativo, peces. No renovables: carbón, cobre, petróleo. Preguntas: «¿Cuántas hectáreas de bosque nativo hay hoy comparado con hace 10 años?» y «¿Cuántos árboles se talan por año?».", ["seis clasificaciones correctas", "dos preguntas con algo que medir", "no son de opinión"], ["clasificación y dos preguntas"], ["clasificar el cobre como renovable", "preguntas de opinión"], "Pregunta qué cambio de condiciones haría renovable a un recurso agotado."),
  reinforce="Escribe un ejemplo de recurso renovable y uno no renovable de Chile.",
  extend="Explica por qué un recurso renovable puede volverse no renovable si se sobreexplota.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Las tablas son de ejemplo y están escritas en los ejercicios.",
  use="Aprenderé a leer datos de superficie de bosque y de uso de recursos para evaluar el efecto de acciones humanas. Sirve para sacar conclusiones con tablas y cálculos.",
  prior=["Sé qué es deforestación y forestación.", "Sé calcular diferencias y porcentajes simples."],
  explain=[
      "Para evaluar una acción humana se necesitan datos antes y después. La diferencia entre dos mediciones muestra el cambio. El cambio porcentual compara esa diferencia con el valor inicial: si un bosque pasa de 200 a 150 hectáreas, la pérdida es de 50 hectáreas, que es el 25 % del inicial.",
      "Los bosques cumplen funciones: sujetan el suelo con sus raíces, regulan el agua, almacenan carbono y dan hábitat. Cuando se pierden, aumenta la erosión, puede disminuir la infiltración (la entrada del agua de lluvia al suelo) y se libera CO2. Una plantación de un solo tipo de árbol (monocultivo) no siempre cumple todas esas funciones como un bosque nativo con variedad de especies.",
      "Los cultivos también transforman el ecosistema. Un cultivo con riego usa agua; uno con rotación de cultivos cuida el suelo. Al leer una tabla se compara cada dato con el anterior y se declara qué datos faltan para atribuir la causa.",
  ],
  vocab=[("cambio porcentual", "diferencia dividida por el valor inicial, por cien"), ("monocultivo", "cultivo o plantación de una sola especie"), ("bosque nativo", "bosque con especies propias del lugar"), ("erosión", "pérdida de suelo por agua o viento"), ("rotación de cultivos", "alternar cultivos para cuidar el suelo")],
  worked=[
      ("Calcular el cambio", "Un bosque pasa de 400 a 300 hectáreas. ¿Cuántas hectáreas se perdieron?", ["Resto el valor final al inicial.", "400 menos 300 es 100."], "100 hectáreas"),
      ("Calcular el porcentaje", "En el mismo bosque, ¿qué porcentaje del inicial se perdió?", ["Divido la pérdida entre el inicial: 100 de 400.", "100 de 400 es un cuarto, 25 de cada 100."], "25 %"),
  ],
  mistakes=[
      ("Dividir la pérdida entre el valor final en vez del inicial.", "El porcentaje se calcula respecto del valor inicial.", "Usa siempre el inicial como base."),
      ("Concluir la causa de la pérdida solo con una tabla de cifras.", "Faltan datos sobre qué actividad produjo el cambio.", "Declara qué dato faltaría."),
  ],
  rec=[
      ("¿Qué función cumplen las raíces de los árboles en el suelo?", "Sujetar el suelo", "Disminuyen la erosión."),
      ("Completa: una plantación de una sola especie es un ______ (monocultivo o bosque nativo).", "Monocultivo", "Tiene una sola especie."),
      ("Verdadero o falso: la deforestación libera CO2.", "Verdadero", "Los árboles almacenaban carbono."),
  ],
  und=[
      ("¿Por qué un bosque nativo cumple más funciones que un monocultivo? A) Tiene más variedad de especies y relaciones; B) Tiene árboles más altos siempre.", "A", "La variedad sostiene más funciones ecológicas."),
      ("¿Qué consecuencia tiene perder el bosque de una ladera? A) Aumenta la erosión del suelo; B) Disminuye la erosión.", "A", "Sin raíces el suelo se arrastra."),
      ("¿Qué muestra la diferencia entre dos mediciones?", "El cambio ocurrido", "Compara el antes y el después."),
  ],
  app=[
      arith("Una zona de ejemplo tenía 800 hectáreas de bosque y hoy tiene 600. ¿Cuántas hectáreas se perdieron?", "800-600", "Se resta el valor final al inicial."),
      arith("En una cuenca de ejemplo se plantaron 3 bloques de 120 hectáreas cada uno. ¿Cuántas hectáreas se forestaron?", "3*120", "Se multiplica el número de bloques por las hectáreas."),
      ("Tabla de ejemplo: año 1, 1.000 ha de bosque nativo; año 10, 900; año 20, 750. ¿En cuál período hubo mayor pérdida: del año 1 al 10 o del año 10 al 20? A) Del 10 al 20; B) Del 1 al 10.", "A", "Del 1 al 10 se perdieron 100 ha y del 10 al 20 se perdieron 150 ha."),
  ],
  rea=[
      ("Un compañero ve una tabla en que el bosque disminuye y concluye que la causa fue un incendio. ¿Qué crítica es mejor? A) Falta un dato que muestre el incendio o la tala como causa; B) Los incendios no queman bosques.", "A", "La tabla muestra el cambio, no la causa."),
      ("Un proyecto reemplaza un bosque nativo por un monocultivo de una sola especie. ¿Qué pérdida ecológica es probable? A) Menor variedad de hábitats y de especies; B) Mayor variedad de especies.", "A", "Un monocultivo sostiene menos especies."),
  ],
  cha=[
      ("Un bosque de 200 hectáreas pierde 50 hectáreas. Otro de 800 hectáreas pierde 100. ¿Cuál perdió una proporción mayor de su superficie? Responde primero o segundo.", "Primero", "50 de 200 es un cuarto del bosque y 100 de 800 es un octavo, que es menos."),
      arith("Un predio de ejemplo cultiva 60 hectáreas de trigo y, con rotación, destina la mitad cada año a descanso. ¿Cuántas hectáreas descansan?", "60//2", "La mitad de 60 es 30 hectáreas."),
  ],
  context=[arith("Un vivero de ejemplo produce 45 plantas de árboles nativos cada semana. ¿Cuántas produce en 8 semanas?", "45*8", "Se multiplica la producción semanal por las semanas.")],
  selfcheck=[("¿Cómo se calcula el cambio entre dos mediciones?", "Restando el valor final al inicial", "La diferencia muestra el cambio."), ("¿Qué función cumplen las raíces del bosque?", "Sujetar el suelo", "Evitan la erosión."), ("¿Por qué una tabla no basta para decir la causa?", "Porque faltan datos sobre qué produjo el cambio", "Hay que investigar la causa.")],
  open_task=task("Con esta tabla de ejemplo, calcula las pérdidas y escribe una conclusión con una limitación. Tabla de hectáreas de bosque nativo: año 1, 900; año 5, 810; año 10, 720.", "Pérdida del año 1 al 5: 90 ha; del 5 al 10: 90 ha; total: 180 ha, el 20 % del inicial. Conclusión: el bosque disminuyó de forma sostenida. Limitación: la tabla no indica la causa, ni qué zonas se perdieron.", ["calcula pérdidas", "usa dos datos en la conclusión", "declara una limitación"], ["cálculos y conclusión"], ["afirmar la causa sin datos", "calcular mal el porcentaje"], "Pregunta qué dato más pedirías para identificar la causa."),
  reinforce="Calcula la pérdida de un bosque que pasa de 250 a 200 hectáreas.",
  extend="Explica por qué un bosque con muchas especies es más resistente que un monocultivo.")

L(OA8, 3,
  materials="Hojas y lápices de colores. Si no tienes, escribe los elementos en cajas con flechas.",
  use="Aprenderé a construir un modelo de causa y efecto para explicar cómo la deforestación, la forestación o un cultivo cambian el equilibrio de un ecosistema. Sirve para predecir sus consecuencias.",
  prior=["Sé qué funciones cumple un bosque.", "Sé el ciclo del carbono y del agua."],
  explain=[
      "Un modelo de causa y efecto conecta una acción con sus consecuencias mediante flechas. Por ejemplo: deforestación → menos raíces → más erosión → más sedimentos en los ríos → agua más turbia y menos vida acuática. Cada flecha es una relación que se puede medir.",
      "El bosque funciona como un sumidero de carbono: absorbe CO2 en la fotosíntesis y lo guarda en su madera. Si se tala y se quema, ese carbono vuelve al aire como CO2. Una forestación, en cambio, aumenta el carbono almacenado a medida que los árboles crecen. En un modelo de balance se compara lo que entra y lo que sale.",
      "Un cultivo con riego puede mejorar la producción de alimentos, pero usa agua y, si se aplica sin cuidado, puede empobrecer el suelo. El modelo ayuda a ver los pros y contras, y muestra que cada acción tiene varios efectos. Los modelos simplifican: no incluyen todos los factores que intervienen.",
  ],
  vocab=[("sumidero de carbono", "ecosistema que absorbe más carbono del que libera"), ("balance", "comparación entre lo que entra y lo que sale"), ("sedimento", "partículas de suelo arrastradas por el agua"), ("causa", "acción o fenómeno que produce un cambio"), ("efecto", "cambio producido por una causa")],
  worked=[
      ("Completar una cadena", "Deforestación → menos raíces → ______ → más sedimentos en el río. ¿Qué falta?", ["Sin raíces, el suelo queda suelto.", "El agua lo arrastra."], "Más erosión del suelo"),
      ("Balance de carbono", "Un bosque de ejemplo absorbe 50 unidades de CO2 al año y libera 20 por respiración. ¿Cuánto almacena?", ["Resto lo que libera a lo que absorbe.", "50 menos 20 es 30."], "30 unidades por año"),
  ],
  mistakes=[
      ("Dibujar solo un efecto de una acción.", "Cada acción tiene varios efectos.", "Agrega al menos dos consecuencias a cada causa."),
      ("Invertir el sentido de las flechas.", "Las flechas van de la causa al efecto.", "Lee cada flecha como «produce»."),
  ],
  rec=[
      ("¿Qué flujo de carbono hace el bosque con el CO2 del aire?", "Lo absorbe en la fotosíntesis", "Lo guarda en la madera."),
      ("Completa: en un modelo, una flecha va de la ______ al efecto (causa o fecha).", "Causa", "La causa produce el efecto."),
      ("Verdadero o falso: talar y quemar un bosque libera el carbono almacenado.", "Verdadero", "Vuelve al aire como CO2."),
  ],
  und=[
      ("¿Por qué la deforestación puede enturbiar un río? A) Porque la erosión arrastra sedimentos al agua; B) Porque el bosque agrega sal al agua.", "A", "El suelo suelto llega al río."),
      ("¿Qué es un sumidero de carbono? A) Un ecosistema que absorbe más carbono del que libera; B) Un lugar sin carbono.", "A", "El bosque en crecimiento lo es."),
      ("¿Qué muestra un balance?", "Lo que entra y lo que sale", "Permite saber si algo aumenta o disminuye."),
  ],
  app=[
      arith("Un bosque de ejemplo absorbe 90 unidades de CO2 al año y libera 40 por respiración. ¿Cuántas unidades almacena en un año?", "90-40", "Se resta lo liberado a lo absorbido."),
      arith("Una forestación de ejemplo almacena 6 unidades de carbono por hectárea. ¿Cuánto almacenan 150 hectáreas?", "6*150", "Se multiplica por la superficie."),
      ("Un modelo propone: tala → menos árboles → menos fotosíntesis. ¿Qué efecto sigue en el aire? A) Menos CO2 absorbido; B) Más oxígeno absorbido.", "A", "Con menos fotosíntesis, se absorbe menos CO2."),
  ],
  rea=[
      ("Un compañero dice que forestar con árboles de una especie elimina todos los problemas del suelo. ¿Cuál es la crítica? A) El modelo no incluye otros efectos, como el uso de agua y la menor diversidad; B) Los árboles no crecen.", "A", "Cada acción tiene varios efectos."),
      ("En un modelo de un cultivo con riego se omite que el agua del río baja. ¿Qué falla tiene? A) No considera el uso de un recurso limitado; B) No considera el color del cultivo.", "A", "El riego tiene un costo ambiental."),
  ],
  cha=[
      arith("Un proyecto de ejemplo planta 200 hectáreas, y cada hectárea almacena 5 unidades de carbono por año. Otro bosque de 100 hectáreas se quema y libera 40 unidades por hectárea. ¿Cuántas unidades más se liberan en la quema que las que se almacenan en un año en la plantación?", "100*40-200*5", "La quema libera 4.000 y la plantación almacena 1.000; se restan ambos valores."),
      ("Un modelo supone que los suelos de un cerro se recuperan en un año tras una tala. ¿Qué evidencia mostrarías para evaluar esa suposición? A) Mediciones de la profundidad del suelo en varios años; B) La opinión de una persona.", "A", "Hay que contrastar con datos."),
  ],
  context=[arith("En un taller de ejemplo, cada equipo planta 12 plántulas y hay 7 equipos. ¿Cuántas plántulas plantan en total?", "12*7", "Se multiplica el número de equipos por las plántulas de cada uno.")],
  selfcheck=[("¿Qué es un sumidero de carbono?", "Un ecosistema que absorbe más carbono del que libera", "El bosque en crecimiento lo es."), ("¿Hacia dónde apunta la flecha en un modelo de causa y efecto?", "De la causa al efecto", "Se lee como «produce»."), ("¿Qué efecto de la deforestación afecta a los ríos?", "Más sedimentos por la erosión", "El suelo queda suelto.")],
  open_task=task("Dibuja un modelo de causa y efecto con flechas para la acción «talar un bosque en una ladera cerca de un río». Incluye al menos tres consecuencias (por ejemplo, el suelo, el agua y el carbono) y agrega un balance numérico: el bosque absorbía 80 unidades de CO2 al año y liberaba 30; tras la tala no absorbe nada. ¿Cuántas unidades por año deja de almacenar?", "Tala → menos raíces → erosión → sedimentos en el río; tala → menos fotosíntesis → menos CO2 absorbido; tala → menos hábitat. El balance dejaba 50 unidades almacenadas por año: ahora deja de almacenar 50.", ["al menos tres consecuencias", "flechas de causa a efecto", "balance numérico correcto"], ["modelo y cálculo"], ["invertir flechas", "olvidar el carbono"], "Pregunta qué medida revertiría una de las consecuencias."),
  reinforce="Dibuja una cadena de causa y efecto con cuatro pasos para una sequía.",
  extend="Explica por qué un modelo no puede incluir todos los efectos de una acción.")

L(OA8, 4,
  materials="Este cuaderno, lápiz y regla. Los datos de consumo son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a relacionar la rapidez de uso con la rapidez de reposición de un recurso para saber si se agota. Sirve para evaluar la disponibilidad de recursos renovables y no renovables.",
  prior=["Sé la diferencia entre recursos renovables y no renovables.", "Sé calcular con divisiones y multiplicaciones simples."],
  explain=[
      "Para saber cuánto dura un recurso no renovable se divide la reserva entre el consumo anual. Si quedan 600 unidades y se consumen 20 por año, alcanzan para 30 años si el consumo se mantiene. Si el consumo aumenta, dura menos años. Esa relación entre variables es inversa: a mayor consumo, menos años.",
      "En un recurso renovable, lo importante es comparar la tasa de uso con la tasa de reposición. Un lago de ejemplo repone 100 peces al año por reproducción. Si se pescan 80, el recurso se mantiene; si se pescan 150, la población disminuye y puede colapsar. Esa regla se llama uso sostenible: no extraer más de lo que se repone.",
      "Estos cálculos son estimaciones, porque el consumo y la reposición cambian con el tiempo, y se descubren nuevas reservas o mejoran las técnicas. Para decidir con evidencia, se declaran los supuestos y se actualizan los datos.",
  ],
  vocab=[("reserva", "cantidad disponible de un recurso"), ("consumo anual", "cantidad usada en un año"), ("tasa de reposición", "cantidad que el recurso recupera por unidad de tiempo"), ("uso sostenible", "usar sin extraer más de lo que se repone"), ("supuesto", "condición que se acepta para hacer un cálculo")],
  worked=[
      ("Calcular años de duración", "Quedan 900 unidades de un recurso no renovable y se consumen 30 por año. ¿Para cuántos años alcanza?", ["Divido la reserva entre el consumo.", "900 dividido por 30 es 30."], "30 años"),
      ("Evaluar un uso sostenible", "Un lago repone 200 peces al año y se pescan 150. ¿El uso es sostenible?", ["Comparo lo que se extrae con lo que se repone.", "150 es menor que 200."], "Sí, es sostenible"),
  ],
  mistakes=[
      ("Calcular los años sin considerar que el consumo cambia.", "Si el consumo aumenta, los años son menos.", "Declara el supuesto de consumo constante."),
      ("Creer que un recurso renovable no puede agotarse.", "Si se extrae más de lo que se repone, disminuye.", "Compara extracción y reposición."),
  ],
  rec=[
      ("¿Cómo se calcula cuántos años dura una reserva?", "Dividiendo la reserva entre el consumo anual", "Da los años si el consumo no cambia."),
      ("Completa: si se extrae más de lo que se repone, la población ______ (disminuye o aumenta).", "Disminuye", "El recurso se agota."),
      ("Verdadero o falso: el uso sostenible extrae menos de lo que el recurso repone.", "Verdadero", "Así el recurso se mantiene."),
  ],
  und=[
      ("Si aumenta el consumo anual, ¿qué pasa con los años que dura la reserva? A) Disminuyen; B) Aumentan.", "A", "Es una relación inversa."),
      ("¿Por qué un cálculo de años es una estimación? A) Porque el consumo y las reservas cambian con el tiempo; B) Porque la división es inexacta.", "A", "Los supuestos pueden no cumplirse."),
      ("¿Qué es la tasa de reposición?", "La cantidad que el recurso recupera por unidad de tiempo", "Se compara con la extracción."),
  ],
  app=[
      arith("Quedan 1.200 unidades de un mineral y se consumen 40 por año. ¿Para cuántos años alcanza si el consumo no cambia?", "1200//40", "Se divide la reserva entre el consumo anual.", " años"),
      arith("Un bosque de ejemplo repone 60 árboles por año y se talan 45. ¿Cuántos árboles más se reponen que se talan?", "60-45", "Se resta lo talado a lo repuesto."),
      ("Un pozo de ejemplo repone 500 litros por día y se extraen 700. ¿Qué ocurre con el agua del pozo? A) Disminuye; B) Aumenta.", "A", "Se extrae más de lo que se repone."),
  ],
  rea=[
      ("Un informe dice: «Con 1.000 unidades de reserva y un consumo de 50 por año, alcanza para 20 años aunque el consumo se duplique». ¿Cuál es el error? A) Con el consumo duplicado, alcanzaría para 10 años; B) Alcanzaría para 40 años.", "A", "1.000 dividido por 100 es 10."),
      ("Una pesquería de ejemplo captura 300 toneladas cada año y la reposición natural es de 200. Un directivo dice que es sostenible. ¿Qué respondes? A) No, extraer más de lo que se repone hace bajar la población; B) Sí, porque 300 es un número redondo.", "A", "Extrae 100 más de lo que se repone."),
  ],
  cha=[
      arith("Una reserva de ejemplo de 2.400 unidades se consume a 60 por año durante 10 años y luego a 120 por año. ¿Cuántas unidades quedan después de los primeros 10 años?", "2400-60*10", "Se resta lo consumido en los 10 años."),
      ("Un nuevo descubrimiento de ejemplo suma 600 unidades a una reserva de 1.800 con un consumo de 60 por año. ¿Cuántos años más alcanza la reserva?", "10", "600 dividido por 60 es 10 años más."),
  ],
  context=[arith("Una familia de ejemplo gasta 150 litros de agua al día. ¿Cuántos litros gasta en 7 días?", "150*7", "Se multiplica el consumo diario por los días.")],
  selfcheck=[("¿Cómo se calcula la duración de una reserva?", "Dividiendo la reserva entre el consumo anual", "Supone un consumo constante."), ("¿Qué es el uso sostenible?", "Extraer menos de lo que se repone", "Mantiene el recurso."), ("¿Por qué el cálculo es una estimación?", "Porque el consumo y las reservas cambian", "Los supuestos pueden fallar.")],
  open_task=task("Con estos datos de ejemplo, responde: (1) Quedan 1.500 unidades de un mineral y se consumen 50 por año; ¿cuántos años alcanza? (2) Un lago repone 400 peces al año y se pescan 520; ¿es sostenible? (3) Propón una medida para cada recurso y un supuesto de tu cálculo.", "(1) 1.500 dividido por 50 es 30 años. (2) No, se pesca 120 más de lo que se repone. (3) Reducir el consumo del mineral, reciclar; limitar la pesca a 400. Supuesto: el consumo se mantiene constante.", ["cálculo correcto", "evalúa la sostenibilidad", "propone una medida y declara un supuesto"], ["cálculos y medidas"], ["no comparar extracción y reposición", "olvidar el supuesto"], "Pregunta qué pasaría si el consumo del mineral aumentara 10 unidades por año."),
  reinforce="Calcula cuántos años dura una reserva de 800 unidades con un consumo de 40 por año.",
  extend="Explica por qué reciclar alarga la duración de un recurso no renovable.")

L(OA8, 5,
  materials="Este cuaderno y lápiz. Los casos de sequía y erupción son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a explicar los mecanismos con que una sequía o una erupción volcánica alteran un ecosistema y cómo se recupera. Sirve para distinguir efectos de corto y largo plazo.",
  prior=["Sé qué factores regulan una población.", "Sé el efecto en cascada."],
  explain=[
      "Una sequía es un período largo con lluvias muy por debajo de lo normal. Reduce el agua de ríos y suelos, disminuye el pasto, aumenta el riesgo de incendios y puede provocar la muerte de plantas y animales. Su efecto se transmite por la red trófica: menos plantas, menos herbívoros, menos depredadores.",
      "Una erupción volcánica expulsa lava, gases y ceniza. La ceniza puede cubrir las hojas, bloquear la luz, contaminar el agua y enterrar los suelos. A largo plazo, la ceniza aporta minerales que pueden fertilizar el suelo. La lava forma roca nueva donde ya no hay suelo.",
      "Después de una alteración el ecosistema se recupera por sucesión ecológica: primero llegan especies pioneras, como musgos y líquenes, que preparan el suelo; después llegan pastos y arbustos; y finalmente árboles. Si el suelo se conserva, la sucesión es más rápida que sobre roca desnuda. Las acciones humanas, como el pastoreo excesivo, pueden retrasarla.",
  ],
  vocab=[("sequía", "período largo con lluvias muy por debajo de lo normal"), ("ceniza volcánica", "partículas finas que expulsa un volcán"), ("sucesión ecológica", "cambio ordenado de especies mientras un ecosistema se recupera"), ("especie pionera", "especie que llega primero a un lugar alterado"), ("corto y largo plazo", "efectos inmediatos y efectos después de años")],
  worked=[
      ("Efecto a corto plazo", "Una erupción cubre las hojas con ceniza. ¿Qué proceso se afecta primero?", ["La ceniza bloquea la luz sobre las hojas.", "Sin luz, disminuye la fotosíntesis."], "La fotosíntesis"),
      ("Ordenar una sucesión", "Ordena de primero a último: arbustos, líquenes, árboles.", ["Primero llegan las pioneras.", "Luego arbustos y por último árboles."], "Líquenes, arbustos, árboles"),
  ],
  mistakes=[
      ("Pensar que una erupción solo trae daños.", "A largo plazo la ceniza puede aportar minerales al suelo.", "Distingue corto y largo plazo."),
      ("Creer que el ecosistema vuelve a ser igual enseguida.", "La sucesión toma muchos años.", "Describe las etapas de la recuperación."),
  ],
  rec=[
      ("¿Cómo se llama el cambio ordenado de especies durante la recuperación?", "Sucesión ecológica", "Parte con las pioneras."),
      ("Completa: una sequía es un período con ______ (pocas lluvias o muchas lluvias).", "Pocas lluvias", "El agua del suelo disminuye."),
      ("Verdadero o falso: los líquenes y musgos suelen llegar antes que los árboles.", "Verdadero", "Son especies pioneras."),
  ],
  und=[
      ("¿Qué consecuencia tiene la sequía en la red trófica? A) Menos plantas, menos herbívoros y menos depredadores; B) Más herbívoros.", "A", "El efecto se transmite en cascada."),
      ("¿Qué efecto puede tener la ceniza a largo plazo? A) Aportar minerales al suelo; B) Impedir siempre el crecimiento de plantas.", "A", "Con el tiempo se incorpora al suelo."),
      ("¿Por qué las especies pioneras son importantes?", "Porque preparan el suelo para otras especies", "Permiten que lleguen pastos y arbustos."),
  ],
  app=[
      ("Cadena de ejemplo tras una sequía: menos lluvia → menos pasto → menos guanacos. ¿Qué consecuencia sigue para el puma? A) Menos alimento; B) Más alimento.", "A", "Hay menos guanacos para cazar."),
      arith("Una zona de ejemplo tenía 400 hectáreas de pasto. Una sequía dejó seco el 25 %, es decir, un cuarto. ¿Cuántas hectáreas se secaron?", "400//4", "Un cuarto de 400 es 100."),
      ("Un campo de ceniza reciente tiene líquenes. ¿Qué etapa de la sucesión es? A) Inicial, de especies pioneras; B) Final, de árboles grandes.", "A", "Los líquenes son pioneros."),
  ],
  rea=[
      ("Un estudiante dice que, tras un incendio provocado por la sequía, los árboles aparecen primero. ¿Cuál es la corrección? A) Primero aparecen pastos y arbustos; los árboles llegan después; B) Los árboles son las pioneras.", "A", "Los árboles llegan en etapas posteriores."),
      ("Una zona de lava de ejemplo no tiene suelo. Otra zona cubierta por ceniza sí lo conserva debajo. ¿Cuál se recuperará más rápido? A) La de ceniza, porque ya tiene suelo; B) La de lava, porque es más nueva.", "A", "El suelo acelera la sucesión."),
  ],
  cha=[
      ("Datos de ejemplo: tras una sequía, la población de un herbívoro cayó de 800 a 500 y la de su depredador de 60 a 45. ¿Cuántos individuos menos hay en total?", "315", "Los herbívoros bajaron 300 y los depredadores 15."),
      ("Una comunidad quiere acelerar la recuperación de un valle afectado por ceniza. ¿Qué medida es más razonable? A) Proteger el suelo y las especies pioneras de la erosión; B) Cubrir todo con cemento.", "A", "El suelo y las pioneras impulsan la sucesión."),
  ],
  context=[arith("Un monitoreo de ejemplo registra 15 especies de plantas en la primera visita después de una sequía y 9 más en la segunda. ¿Cuántas especies hay ahora?", "15+9", "Se suman las especies de ambas visitas.")],
  selfcheck=[("¿Qué efecto tiene la ceniza sobre las hojas?", "Bloquea la luz y disminuye la fotosíntesis", "Es un efecto a corto plazo."), ("¿Qué es la sucesión ecológica?", "El cambio ordenado de especies mientras un ecosistema se recupera", "Empieza con pioneras."), ("¿Cómo afecta una sequía a los depredadores?", "Tienen menos alimento por el efecto en cascada", "Hay menos presas.")],
  open_task=task("Con esta secuencia de ejemplo: año 0, erupción cubre un valle de ceniza; año 1, aparecen musgos y líquenes; año 5, aparecen pastos; año 15, aparecen arbustos; año 40, aparecen árboles. Escribe una línea de tiempo con tres efectos de corto plazo y uno de largo plazo, y explica por qué los líquenes llegan primero.", "Línea de tiempo: año 0 ceniza; año 1 musgos y líquenes; año 5 pastos; año 15 arbustos; año 40 árboles. Corto plazo: ceniza sobre hojas, menos luz, agua contaminada; largo plazo: minerales en el suelo. Los líquenes llegan primero porque soportan suelos pobres y preparan el suelo para otras especies.", ["línea de tiempo en orden", "tres efectos de corto plazo y uno de largo", "explica el papel de las pioneras"], ["línea de tiempo y explicación"], ["poner árboles al inicio", "omitir el largo plazo"], "Pregunta qué cambiaría si el valle no tuviera suelo."),
  reinforce="Ordena las etapas de una sucesión: pioneras, pastos, arbustos y árboles.",
  extend="Explica por qué el pastoreo excesivo puede retrasar la recuperación de un ecosistema.")

L(OA8, 6,
  materials="Este cuaderno y lápiz. Los casos y las cifras son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a evaluar medidas para un desarrollo sustentable con criterios ambientales, sociales y económicos y a reconocer límites de los datos. Sirve para tomar decisiones cuidadosas.",
  prior=["Sé la diferencia entre recursos renovables y no renovables.", "Sé evaluar uso sostenible."],
  explain=[
      "Un desarrollo sustentable busca que las personas satisfagan sus necesidades hoy sin comprometer las de las futuras generaciones. Para evaluar una medida se usan criterios: ambiental (cuánto daño evita), social (a quién ayuda o perjudica) y económico (cuánto cuesta). Una medida es mejor cuando cumple varios criterios a la vez.",
      "Ejemplos de medidas: usar energías renovables como la solar, reciclar, ahorrar agua, proteger áreas naturales, reforestar con especies nativas y planificar cultivos para cuidar el suelo. Cada medida tiene costos y límites: la energía solar requiere una inversión; la reforestación toma años.",
      "Al evaluar, se deben declarar los límites de los datos: si la información es de pocos años, si falta medir algún efecto o si hay intereses distintos. En un tema ambiental conviene que las decisiones se discutan con personas de la comunidad y con especialistas. Los estudiantes pueden participar proponiendo y evaluando medidas en su escuela y casa, con ayuda de personas adultas.",
  ],
  vocab=[("criterio", "regla que sirve para juzgar algo"), ("energía renovable", "energía que viene de fuentes que se reponen, como el sol y el viento"), ("inversión", "dinero que se gasta al inicio para obtener beneficios después"), ("medida", "acción propuesta para resolver un problema"), ("compromiso", "decisión que equilibra costos y beneficios")],
  worked=[
      ("Evaluar con criterios", "Medida: instalar paneles solares en una escuela. Costo inicial alto, ahorro de electricidad cada año. ¿Qué criterios cumple?", ["Ambiental: reduce el uso de energía de fuentes no renovables.", "Económico: ahorra dinero a largo plazo."], "Cumple el criterio ambiental y, a largo plazo, el económico"),
      ("Calcular un ahorro", "Una ducha de ejemplo gasta 12 litros por minuto. ¿Cuántos litros se ahorran si se reduce de 10 a 6 minutos?", ["Calculo la diferencia de minutos: 4.", "4 por 12 es 48."], "48 litros"),
  ],
  mistakes=[
      ("Elegir una medida solo porque es barata.", "Puede dañar el ambiente o perjudicar a otras personas.", "Evalúa con los tres criterios."),
      ("Creer que una medida soluciona todos los problemas.", "Cada medida tiene límites.", "Declara qué problema deja sin resolver."),
  ],
  rec=[
      ("¿Qué busca un desarrollo sustentable?", "Satisfacer necesidades actuales sin dañar las de futuras generaciones", "Equilibra presente y futuro."),
      ("Completa: la energía del sol es una energía ______ (renovable o no renovable).", "Renovable", "Se repone continuamente."),
      ("Verdadero o falso: una medida puede tener costos y beneficios al mismo tiempo.", "Verdadero", "Por eso se evalúa con criterios."),
  ],
  und=[
      ("¿Cuáles son tres criterios para evaluar una medida? A) Ambiental, social y económico; B) Color, tamaño y forma.", "A", "Equilibran los distintos efectos."),
      ("¿Por qué reforestar con especies nativas es mejor que con una sola especie ajena? A) Mantiene la variedad de especies y relaciones del lugar; B) Es siempre más barato.", "A", "Apoya la biodiversidad."),
      ("En Ciencias: ¿Qué es una inversión?", "Dinero que se gasta al inicio para obtener beneficios después", "Hay que compararla con el ahorro."),
  ],
  app=[
      arith("Una ducha de ejemplo gasta 15 litros por minuto. Una persona reduce su ducha de 8 a 5 minutos. ¿Cuántos litros ahorra?", "(8-5)*15", "Se multiplica la reducción de minutos por los litros por minuto."),
      arith("Un colegio de ejemplo ahorra 40 kWh (kilowatt-hora, una unidad de energía eléctrica) al mes con luces eficientes. ¿Cuántos kWh ahorra en un año de 12 meses?", "40*12", "Se multiplica el ahorro mensual por los meses."),
      ("Para ahorrar agua en casa, ¿qué medida es adecuada? A) Cerrar la llave mientras se enjabonan las manos; B) Dejar la llave abierta para que se enfríe el agua.", "A", "Evita el gasto innecesario de agua."),
  ],
  rea=[
      ("Un proyecto de ejemplo ahorra mucho dinero pero contamina un río cercano. ¿Qué respuesta es mejor? A) No cumple el criterio ambiental y debe rediseñarse; B) Es aceptable, porque ahorra dinero.", "A", "Un desarrollo sustentable exige varios criterios."),
      ("Un informe de ejemplo mide el efecto de una medida solo durante 6 meses. ¿Qué límite tiene? A) No muestra efectos de largo plazo; B) Los informes no pueden medir meses.", "A", "Falta información de más años."),
  ],
  cha=[
      ("Dos medidas de ejemplo: la A cuesta 200 unidades y ahorra 50 por año; la B cuesta 150 y ahorra 25 por año. ¿En cuántos años recupera su costo la medida A?", "4", "200 dividido por 50 es 4 años."),
      ("Con los mismos datos (A cuesta 200 y ahorra 50 por año; B cuesta 150 y ahorra 25 por año), ¿cuál medida recupera antes su costo? A) La A; B) La B.", "A", "La A lo recupera en 4 años y la B en 6 años."),
  ],
  context=[arith("Una escuela de ejemplo recicla 18 kg de papel por semana. ¿Cuántos kg recicla en 10 semanas?", "18*10", "Se multiplica el reciclaje semanal por las semanas.")],
  selfcheck=[("¿Cuáles son los tres criterios para evaluar una medida?", "Ambiental, social y económico", "Se evalúan juntos."), ("Da un ejemplo de energía renovable.", "La energía solar o la del viento", "Se reponen continuamente."), ("¿Por qué hay que declarar los límites de los datos?", "Porque pueden faltar efectos o años por medir", "Así se decide con prudencia.")],
  open_task=task("Elige una medida de ejemplo: (A) paneles solares en la escuela; (B) reciclar papel; (C) reforestar con árboles nativos una ladera. Evalúala con los tres criterios (ambiental, social y económico) en una frase cada uno y escribe un límite de los datos. Si quieres, calcula un ahorro con números de ejemplo (por ejemplo, 12 kg de papel por semana en 8 semanas).", "Medida B: ambiental, evita talar más árboles; social, involucra al curso; económico, ahorra compras de papel nuevo. Límite: se midieron solo 10 semanas. Cálculo: 12 por 8 son 96 kg.", ["tres criterios evaluados", "declara un límite", "usa un cálculo coherente si lo hace"], ["evaluación escrita"], ["evaluar con un solo criterio", "omitir el límite"], "Pregunta qué medida complementaria agregarías."),
  reinforce="Escribe una medida de ahorro de agua en tu casa y calcula cuántos litros ahorra a la semana.",
  extend="Explica por qué las decisiones ambientales conviene discutirlas con la comunidad y con especialistas.")

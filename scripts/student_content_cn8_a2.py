"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 02 (estructura, función y diversidad celular)."""
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


OA2 = "CN08 OA 02"

L(OA2, 1,
  materials="Este cuaderno y lápiz. No necesitas microscopio: las observaciones están descritas en cada ejercicio.",
  use="Aprenderé el nombre y la función de las estructuras de la célula y a formular preguntas investigables sobre ellas. Sirve para relacionar cada parte con lo que hace.",
  prior=["Sé que la célula es la unidad básica de los seres vivos.", "Sé que una pregunta investigable se responde con observaciones o mediciones."],
  explain=[
      "Una célula tiene estructuras con funciones distintas. La membrana celular rodea a la célula y controla qué sustancias entran y salen. El citoplasma es el medio gelatinoso donde están las demás estructuras y ocurren muchas reacciones. El núcleo guarda el material genético (ADN) y dirige las actividades de la célula.",
      "Otras estructuras tienen tareas específicas. Las mitocondrias liberan energía de los nutrientes para que la célula funcione. Las vacuolas almacenan agua y otras sustancias. Entre las células animales y las vegetales, solo las vegetales tienen cloroplastos, que contienen clorofila y realizan fotosíntesis, y una pared celular rígida por fuera de la membrana, que da soporte y protección.",
      "Para investigar se necesita una pregunta que indique qué se observa. Por ejemplo: «¿Qué estructuras se distinguen en células de una hoja y en células de la mejilla de una persona?». Es una buena pregunta porque se responde mirando y comparando. «¿Cuál estructura es la más importante?» no lo es, porque todas cumplen funciones necesarias.",
  ],
  vocab=[("membrana celular", "capa que rodea la célula y controla lo que entra y sale"), ("núcleo", "estructura que guarda el material genético"), ("mitocondria", "estructura que libera energía de los nutrientes"), ("cloroplasto", "estructura vegetal donde ocurre la fotosíntesis"), ("pared celular", "cubierta rígida que rodea a la célula vegetal")],
  worked=[
      ("Función de cada estructura", "Une cada estructura con su función: núcleo, mitocondria, pared celular. Funciones: (x) liberar energía, (y) dar soporte, (z) guardar el material genético.", ["El núcleo guarda el material genético: z.", "La mitocondria libera energía: x.", "La pared celular da soporte: y."], "Núcleo con z, mitocondria con x, pared celular con y"),
      ("Pregunta investigable", "¿Es investigable «¿Hay cloroplastos en las células de una hoja verde?»?", ["Pregunto si se puede observar.", "Con un microscopio se ven los cloroplastos como puntos verdes dentro de las células."], "Sí, es investigable porque se responde observando"),
  ],
  mistakes=[
      ("Decir que todas las células tienen cloroplastos.", "Solo las células vegetales con fotosíntesis los tienen.", "Pregunta si la célula es vegetal y recibe luz."),
      ("Confundir la membrana con la pared celular.", "La membrana está en todas las células; la pared es una cubierta rígida extra, como en las vegetales.", "Recuerda que la pared está por fuera de la membrana."),
  ],
  rec=[
      ("¿Qué estructura guarda el material genético de la célula: el núcleo o la vacuola?", "El núcleo", "Allí está el ADN."),
      ("¿Qué estructura libera energía de los nutrientes: la mitocondria o el cloroplasto?", "La mitocondria", "Allí se obtiene la energía para las funciones celulares."),
      ("Verdadero o falso: la pared celular está en las células animales.", "Falso", "Entre animales y vegetales, la pared es propia de las vegetales."),
  ],
  und=[
      ("¿Cuál función cumple la membrana celular? A) Controlar qué entra y sale de la célula; B) Fabricar la glucosa mediante fotosíntesis.", "A", "La fotosíntesis ocurre en los cloroplastos."),
      ("¿Para qué sirven las vacuolas? A) Almacenar agua y otras sustancias; B) Producir energía a partir de la luz.", "A", "La energía de la luz la capta el cloroplasto."),
      ("Una célula tiene cloroplastos y pared celular. ¿Es animal o vegetal?", "Vegetal", "Esas estructuras son propias de las células vegetales."),
  ],
  app=[
      ("¿Cuál pregunta es investigable? A) ¿Qué estructuras se ven en una célula de cebolla al microscopio? B) ¿Cuál estructura es la más importante de la célula?", "A", "Se responde observando; la otra es una opinión."),
      ("Datos de ejemplo: de 5 células observadas, 3 tenían pared celular y cloroplastos, y 2 tenían solo membrana. ¿Cuántas eran probablemente vegetales?", "3", "Las que tienen pared y cloroplastos son vegetales."),
      ("Una célula de ejemplo tiene muchas mitocondrias. ¿Qué podría necesitar esa célula? A) Mucha energía; B) Mucha luz.", "A", "Las mitocondrias liberan energía de los nutrientes."),
  ],
  rea=[
      ("Una estudiante afirma: «Las células de la raíz de una planta tienen cloroplastos porque la planta es verde». ¿Qué falla ve en su razonamiento? A) La raíz está bajo tierra sin luz, así que no es lo esperable; B) Las raíces no tienen células.", "A", "Los cloroplastos están donde llega la luz, como en las hojas."),
      ("Alguien dice que la membrana es innecesaria porque las células vegetales tienen pared. ¿Qué función cumple la membrana que la pared no reemplaza? Responde en una frase.", "Controla qué sustancias entran y salen", "La pared es rígida y deja pasar casi todo; la membrana regula."),
  ],
  cha=[
      ("Dos láminas: la lámina X tiene células con núcleo, mitocondrias y membrana, sin pared; la lámina Y tiene núcleo, pared, cloroplastos y una vacuola grande. ¿Cuál es de una hoja? Escribe X o Y.", "Y", "Tiene pared, cloroplastos y vacuola grande, propias de una hoja."),
      arith("En un dibujo de ejemplo de una célula vegetal hay 12 cloroplastos y 30 mitocondrias. ¿Cuántas de estas dos estructuras hay en total?", "12+30", "Se suman los dos conteos."),
  ],
  context=[("Una persona mira un trocito de hoja de elodea al microscopio y ve puntos verdes dentro de cada célula. ¿Qué estructura son los puntos verdes?", "Cloroplastos", "Contienen clorofila, de color verde.")],
  selfcheck=[("¿Qué hace el núcleo?", "Guarda el material genético y dirige la célula", "Contiene el ADN."), ("¿Qué estructuras son propias de las células vegetales?", "Pared celular y cloroplastos", "No están en las células animales."), ("¿Cuál es una pregunta investigable sobre estructuras?", "¿Qué estructuras se ven en una célula de cebolla?", "Se responde observando.")],
  open_task=task("Elige una de estas dos preguntas y reescríbela como pregunta investigable que diga qué se observa: (a) «¿Qué es lo más importante de la célula?», (b) «¿Son lindos los cloroplastos?». Luego escribe una función para cada estructura de esta lista: núcleo, mitocondria, vacuola.", "(a) «¿Qué estructuras se distinguen en una célula de cebolla al microscopio?». Núcleo: guarda el material genético. Mitocondria: libera energía. Vacuola: almacena agua y sustancias.", ["una pregunta que indica qué se observa", "tres funciones correctas", "sin opiniones"], ["pregunta y tres frases"], ["dejar la pregunta como opinión", "confundir mitocondria y cloroplasto"], "Pregunta qué observación te diría si una célula es vegetal."),
  reinforce="Escribe la función de la membrana celular y la de la pared celular.",
  extend="Explica por qué una célula necesita membrana aunque tenga pared.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Las tablas de observación están escritas en cada ejercicio.",
  use="Aprenderé a comparar células eucariontes (animal y vegetal) y procariontes usando una tabla de rasgos. Sirve para clasificar una célula a partir de lo que se observa.",
  prior=["Sé las funciones de las estructuras celulares.", "Sé que las células vegetales tienen pared y cloroplastos."],
  explain=[
      "Las células eucariontes tienen un núcleo rodeado por una membrana, donde está el material genético, y otras estructuras con membrana, como las mitocondrias. Las animales y las vegetales son eucariontes. Las procariontes, como las bacterias, no tienen un núcleo definido: su material genético está libre en una zona del citoplasma y no tienen mitocondrias ni cloroplastos.",
      "Los rasgos para comparar son: núcleo definido, pared celular, cloroplastos, mitocondrias y vacuola grande. Una célula animal (eucarionte) tiene núcleo y mitocondrias, y no tiene pared ni cloroplastos. Una célula vegetal (eucarionte) tiene núcleo, mitocondrias, pared, cloroplastos y una vacuola grande. Una bacteria (procarionte) tiene membrana, citoplasma y material genético sin núcleo; muchas tienen pared, pero no de los mismos componentes que la de una planta.",
      "Para clasificar una célula se lee la tabla de rasgos y se busca el que la distingue. El núcleo definido separa a las eucariontes de las procariontes. Entre las eucariontes, la pared y los cloroplastos separan a las vegetales de las animales. Una conclusión debe indicar el rasgo decisivo y no basarse solo en el tamaño.",
  ],
  vocab=[("eucarionte", "célula con núcleo definido por una membrana"), ("procarionte", "célula sin núcleo definido"), ("rasgo decisivo", "característica que permite separar un grupo de otro"), ("material genético", "ADN que guarda las instrucciones de la célula"), ("vacuola grande", "vacuola central que ocupa gran parte de la célula vegetal")],
  worked=[
      ("Clasificar con una tabla", "La célula M tiene núcleo, mitocondrias, pared y cloroplastos. ¿Qué tipo de célula es?", ["Tiene núcleo: es eucarionte.", "Tiene pared y cloroplastos: es vegetal."], "Célula vegetal (eucarionte)"),
      ("Rasgo decisivo", "La célula N no tiene núcleo definido ni mitocondrias. ¿Es procarionte o eucarionte?", ["Busco el rasgo decisivo: el núcleo definido.", "La ausencia de núcleo definido separa a las procariontes."], "Procarionte"),
  ],
  mistakes=[
      ("Creer que las bacterias tienen núcleo.", "Su material genético está libre en el citoplasma, sin membrana que lo rodee.", "Revisa si el material genético está dentro de un núcleo definido."),
      ("Clasificar solo por tamaño.", "El tamaño no es un rasgo decisivo, pues hay rangos que se traslapan.", "Usa un rasgo estructural, como el núcleo."),
  ],
  rec=[
      ("¿Qué rasgo tienen las células eucariontes que no tienen las procariontes?", "Un núcleo definido", "Su material genético está dentro de un núcleo."),
      ("¿Una bacteria es una célula procarionte o eucarionte?", "Procarionte", "No tiene un núcleo definido."),
      ("Verdadero o falso: las células animales tienen cloroplastos.", "Falso", "Los cloroplastos son propios de las vegetales."),
  ],
  und=[
      ("Una célula tiene núcleo y mitocondrias, pero no tiene pared ni cloroplastos. ¿De cuál tipo es? A) Animal; B) Vegetal.", "A", "Le faltan los rasgos propios de las vegetales."),
      ("¿Qué rasgo separa a una célula vegetal de una animal? A) La pared celular y los cloroplastos; B) El núcleo.", "A", "El núcleo está en ambas."),
      ("¿Dónde está el material genético en una bacteria?", "Libre en el citoplasma", "No está rodeado por una membrana como en un núcleo."),
  ],
  app=[
      ("Cuatro células de ejemplo: P (núcleo, pared, cloroplastos), Q (núcleo, sin pared), R (sin núcleo definido, con pared), S (núcleo, pared, cloroplastos). ¿Cuántas son vegetales?", "2", "Son P y S: tienen núcleo, pared y cloroplastos."),
      ("Con las mismas cuatro células (P: núcleo, pared, cloroplastos; Q: núcleo, sin pared; R: sin núcleo definido, con pared; S: núcleo, pared, cloroplastos), ¿cuál es procarionte? Escribe la letra.", "R", "Es la única sin núcleo definido."),
      ("Con las mismas cuatro células (P: núcleo, pared, cloroplastos; Q: núcleo, sin pared; R: sin núcleo definido, con pared; S: núcleo, pared, cloroplastos), ¿cuál es animal? Escribe la letra.", "Q", "Tiene núcleo y no tiene pared."),
  ],
  rea=[
      ("Un estudiante afirma que R es vegetal porque tiene pared. ¿Cuál es la falla? A) R no tiene núcleo definido ni cloroplastos, así que es procarionte; B) La pared no existe en ninguna célula.", "A", "La pared aparece también en muchas procariontes, pero no es el rasgo decisivo."),
      ("¿Por qué no basta decir «es chica, entonces es bacteria»? Responde en una frase.", "Porque el tamaño no es un rasgo decisivo", "Hay rangos de tamaño que se traslapan; hay que mirar el núcleo."),
  ],
  cha=[
      ("Se estudian 20 células de ejemplo: 8 vegetales, 7 animales y el resto procariontes. Un compañero dice que más de la mitad son eucariontes con pared. ¿Es correcto? Responde Sí o No.", "No", "Las vegetales son 8 de 20, menos de la mitad (10)."),
      arith("En el estudio de ejemplo con 20 células, ¿cuántas son procariontes?", "20-8-7", "Se restan las vegetales y las animales del total."),
  ],
  context=[("Un laboratorio observa una célula sin núcleo definido, de 2 µm, con pared y material genético libre. ¿Es eucarionte o procarionte?", "Procarionte", "Sin núcleo definido y con material genético libre.")],
  selfcheck=[("¿Qué es una célula eucarionte?", "Una célula con núcleo definido", "Animales y vegetales lo son."), ("¿Qué rasgo separa a una célula vegetal de una animal?", "Pared celular y cloroplastos", "Ambas son eucariontes."), ("¿Por qué el tamaño no basta para clasificar?", "Porque los rangos de tamaño se traslapan", "Hay que usar un rasgo estructural.")],
  open_task=task("Completa esta tabla con Sí o No para cada tipo de célula (animal, vegetal, bacteria): núcleo definido, pared celular, cloroplastos, mitocondrias. Después clasifica una célula X que tiene núcleo, mitocondrias, pared y cloroplastos.", "Animal: Sí, No, No, Sí. Vegetal: Sí, Sí, Sí, Sí. Bacteria: No, Sí (distinta), No, No. La célula X es vegetal.", ["12 casillas completas", "clasifica X con el rasgo decisivo", "menciona que la bacteria no tiene núcleo definido"], ["tabla y clasificación"], ["poner núcleo en la bacteria", "clasificar por tamaño"], "Pregunta qué rasgo cambiaría tu clasificación de X."),
  reinforce="Escribe tres rasgos de una célula animal.",
  extend="Explica por qué una bacteria con pared no es una célula vegetal.")

L(OA2, 3,
  materials="Este cuaderno y lápiz. Las analogías y las listas están escritas en cada ejercicio.",
  use="Aprenderé a construir un modelo de célula con analogías y a decir qué simplifica. Sirve para explicar las funciones de las estructuras con un ejemplo cotidiano.",
  prior=["Sé las estructuras de la célula y sus funciones.", "Sé que todo modelo simplifica."],
  explain=[
      "Un modelo por analogía compara partes de la célula con algo conocido. Por ejemplo, una célula se parece a una fábrica: el núcleo es la oficina de control, que guarda los planos; la membrana es la puerta con guardia, que decide qué entra y sale; las mitocondrias son los generadores que entregan energía, y las vacuolas son las bodegas.",
      "En la célula vegetal, la pared celular es como el muro exterior, y los cloroplastos son paneles que captan luz y fabrican alimento. Una buena analogía relaciona cada parte con su función, no con su forma. Si solo se parece en el aspecto, no explica nada: decir que el núcleo es una pelota porque es redondo no dice qué hace.",
      "Todo modelo tiene límites. La fábrica no se divide para formar otra fábrica y la célula sí. Por eso, al presentar un modelo hay que decir qué explica y qué deja afuera. Un modelo se contrasta con la evidencia: si algo observado no calza, se mejora el modelo.",
  ],
  vocab=[("analogía", "comparación entre dos cosas por su semejanza de función"), ("modelo por analogía", "representación que usa algo conocido para explicar otra cosa"), ("límite del modelo", "aspecto de la realidad que el modelo no explica"), ("función", "tarea que cumple una estructura"), ("contrastar", "comparar un modelo con la evidencia")],
  worked=[
      ("Analogía adecuada", "En el modelo de fábrica, ¿qué estructura celular es la «puerta con guardia»?", ["Una puerta con guardia controla lo que entra y sale.", "La membrana celular controla lo que entra y sale."], "La membrana celular"),
      ("Límite de la analogía", "La fábrica no se divide en dos fábricas. ¿Qué proceso de la célula no queda bien modelado?", ["La fábrica del modelo es una sola y no forma otra igual.", "Las células sí se dividen para formar otras células."], "La división celular"),
  ],
  mistakes=[
      ("Elegir una analogía solo porque se parece en la forma.", "No explica qué hace la estructura.", "Compara la función, no el aspecto."),
      ("Creer que un modelo muestra toda la realidad.", "Todo modelo simplifica y deja fuera aspectos.", "Dilo siempre al presentar el modelo."),
  ],
  rec=[
      ("En el modelo de fábrica, ¿qué parte de la célula es la oficina de control con los planos?", "El núcleo", "El núcleo guarda el material genético."),
      ("¿Qué estructura es como un generador que entrega energía?", "La mitocondria", "Libera energía de los nutrientes."),
      ("Verdadero o falso: una analogía debe comparar la función.", "Verdadero", "La forma sola no explica lo que hace una estructura."),
  ],
  und=[
      ("¿Cuál es una buena analogía para la pared celular? A) Un muro exterior que da soporte; B) Una oficina con planos.", "A", "La oficina con planos es el núcleo."),
      ("¿Qué estructura de la célula vegetal es como un panel que capta luz? A) Cloroplasto; B) Vacuola.", "A", "El cloroplasto capta la luz para la fotosíntesis."),
      ("¿Qué estructura es como una bodega?", "La vacuola", "Almacena agua y otras sustancias."),
  ],
  app=[
      ("Un grupo dice que la membrana es «una malla que deja pasar todo». ¿Qué parte de la función olvidó? A) Que controla qué entra y qué sale; B) Que fabrica energía.", "A", "La membrana no deja pasar todo: regula."),
      ("Un modelo propone un globo con arroz adentro. ¿Qué estructura representa el arroz si cumple la función de almacenar? A) Una vacuola; B) El núcleo.", "A", "Almacenar es la función de la vacuola."),
      arith("Un modelo de célula de ejemplo usa 1 cm para representar 10 µm. Si la célula mide 60 µm, ¿cuántos centímetros mide el modelo?", "60//10", "Cada 10 µm corresponden a 1 cm; se divide 60 por 10."),
  ],
  rea=[
      ("Alguien afirma: «El núcleo es como una pelota; por eso el modelo es bueno». ¿Qué critica corresponde? A) Compara la forma y no la función; B) Los núcleos no son redondos.", "A", "Una buena analogía debe explicar qué hace la estructura."),
      ("Explica en una frase un límite del modelo de fábrica para la célula.", "No muestra cómo la célula se divide para formar otras", "Una fábrica no se reproduce como una célula."),
  ],
  cha=[
      ("Un estudiante cambia su modelo: añade una fábrica pequeña que se divide en dos. ¿Qué mejora logra? A) Representa la división celular; B) Representa la fotosíntesis.", "A", "Ahora el modelo incluye que las células se dividen."),
      ("En el modelo de fábrica, la célula animal no tiene paneles solares. ¿Qué rasgo real de la célula animal representa? A) No tiene cloroplastos; B) No tiene mitocondrias.", "A", "La célula animal no hace fotosíntesis."),
  ],
  context=[("Un curso arma un modelo de célula vegetal con una caja rígida de cartón por fuera y gelatina por dentro. ¿Qué parte de la célula representa la caja?", "La pared celular", "Es rígida y está por fuera de la membrana.")],
  selfcheck=[("¿Qué es una analogía?", "Una comparación por semejanza de función", "Sirve para explicar con algo conocido."), ("¿Por qué comparar la función y no la forma?", "Porque la función explica qué hace la estructura", "La forma sola no explica."), ("¿Qué debe decir un modelo sobre sí mismo?", "Qué explica y qué deja afuera", "Declara sus límites.")],
  open_task=task("Elige un lugar conocido (un colegio, un mercado o una casa) y escribe una analogía para cuatro estructuras de la célula: núcleo, membrana, mitocondria y vacuola. Para cada una, explica en una frase qué función comparas. Termina con un límite de tu modelo.", "Colegio: la dirección es el núcleo (da las órdenes); el portón es la membrana (controla entradas y salidas); la sala de calderas es la mitocondria (entrega energía); la bodega es la vacuola (guarda materiales). Límite: el colegio no se divide en dos.", ["cuatro analogías", "compara la función", "un límite declarado"], ["cuatro frases y un límite"], ["comparar solo por la forma", "olvidar el límite"], "Pregunta qué parte de tu modelo no coincide con una célula real."),
  reinforce="Escribe una analogía para la pared celular.",
  extend="Explica por qué un modelo útil no tiene que parecerse a la célula, sino explicar sus funciones.")

L(OA2, 4,
  materials="Este cuaderno y lápiz. Los datos de las tablas son de ejemplo y se escriben en cada ejercicio.",
  use="Aprenderé la relación entre el tipo de célula y su función: células musculares, nerviosas, intestinales y pancreáticas. Sirve para explicar por qué la estructura se ajusta a la función.",
  prior=["Sé que las mitocondrias liberan energía.", "Sé que las células pueden ser muy distintas entre sí."],
  explain=[
      "En un organismo pluricelular hay células con formas y estructuras distintas, porque cada tipo hace una tarea distinta. Esa variedad se llama diversidad celular. La estructura de cada tipo celular se relaciona con su función. Una célula muscular se contrae y necesita mucha energía, por eso tiene muchas mitocondrias.",
      "Una célula nerviosa (neurona) tiene prolongaciones largas que conducen señales eléctricas entre partes del cuerpo. Una célula intestinal absorbe nutrientes y tiene pliegues en su superficie que aumentan el área de absorción. Una célula pancreática fabrica y libera sustancias, como enzimas digestivas y la hormona insulina, y por eso tiene muchas estructuras dedicadas a fabricarlas y liberarlas.",
      "Para investigar la relación se comparan variables: por ejemplo, el número de mitocondrias en distintos tipos de células. Si las células que más energía gastan tienen más mitocondrias, se observa un patrón. Una relación entre dos variables no prueba por sí sola que una cause la otra, pero junto a una explicación de la función hace creíble la conclusión.",
  ],
  vocab=[("diversidad celular", "variedad de formas y funciones de las células de un organismo"), ("neurona", "célula nerviosa que conduce señales"), ("absorción", "paso de sustancias desde el intestino hacia la sangre"), ("secreción", "liberación de sustancias que fabrica una célula"), ("variable", "dato que puede cambiar y se mide")],
  worked=[
      ("Estructura y función", "¿Por qué una célula muscular tiene muchas mitocondrias?", ["La célula muscular se contrae y gasta mucha energía.", "Las mitocondrias liberan energía de los nutrientes."], "Porque necesita mucha energía"),
      ("Leer un patrón", "Datos de ejemplo: célula de la piel, 200 mitocondrias; célula muscular, 2.000. ¿Cuántas veces más mitocondrias tiene la muscular?", ["Divido 2.000 entre 200.", "2.000 ÷ 200 = 10."], "10 veces más"),
  ],
  mistakes=[
      ("Pensar que todas las células de un cuerpo son iguales.", "Cada tipo tiene forma y estructuras ajustadas a su función.", "Asocia la forma de la célula con su tarea."),
      ("Decir que una relación entre variables prueba una causa por sí sola.", "Hace falta también una explicación de la función.", "Une el dato con el mecanismo."),
  ],
  rec=[
      ("¿Qué tipo de célula conduce señales eléctricas con prolongaciones largas: la nerviosa o la intestinal?", "La nerviosa", "La neurona tiene prolongaciones largas."),
      ("¿Qué estructuras abundan en una célula muscular: mitocondrias o cloroplastos?", "Mitocondrias", "Necesita mucha energía."),
      ("Verdadero o falso: la célula intestinal tiene pliegues para absorber más nutrientes.", "Verdadero", "Los pliegues aumentan la superficie de absorción."),
  ],
  und=[
      ("¿Para qué sirven los pliegues de una célula intestinal? A) Para aumentar la superficie de absorción; B) Para conducir señales eléctricas.", "A", "A mayor superficie, mayor absorción."),
      ("¿Qué fabrica y libera una célula pancreática? A) Enzimas digestivas e insulina; B) Fibras que se contraen.", "A", "Esa es su función de secreción."),
      ("¿Por qué existe la diversidad celular en un mismo cuerpo?", "Porque cada tipo de célula cumple una función distinta", "La estructura se ajusta a la tarea."),
  ],
  app=[
      ("Datos de ejemplo del número de mitocondrias: célula de la grasa, 500; célula muscular, 2.500; neurona, 1.500. ¿Cuál tiene más? Escribe el tipo.", "Muscular", "2.500 es el valor mayor."),
      arith("Con los datos de ejemplo: ¿cuántas mitocondrias más tiene la célula muscular (2.500) que la de la grasa (500)?", "2500-500", "Se resta el menor al mayor."),
      ("Una célula de ejemplo tiene una superficie de absorción de 40 unidades y otra con pliegues tiene 120. ¿Cuántas veces mayor es la segunda?", "3", "120 ÷ 40 = 3.", "120//40"),
  ],
  rea=[
      ("Un estudiante afirma: «Las neuronas tienen muchas mitocondrias, por lo tanto producen insulina». ¿Qué error comete? A) Une un dato con una función que no corresponde; B) Las neuronas no tienen mitocondrias.", "A", "La insulina la libera la célula pancreática; las neuronas conducen señales."),
      ("Si en un tejido las células tienen muchas mitocondrias, ¿qué función se espera? Responde en una frase.", "Una que gaste mucha energía", "Las mitocondrias liberan energía de los nutrientes."),
  ],
  cha=[
      ("Una tabla de ejemplo muestra: célula X con 3.000 mitocondrias y célula Y con 150. Se sabe que una es muscular y la otra de la piel. ¿Cuál es la muscular? Escribe X o Y.", "X", "La muscular necesita más energía y tiene más mitocondrias."),
      ("Un compañero dice: «Como la célula intestinal tiene pliegues, absorbe menos». ¿Qué respuesta es correcta? A) Absorbe más porque tiene más superficie; B) Absorbe igual porque los pliegues no cambian nada.", "A", "Los pliegues aumentan el área en contacto con los nutrientes."),
  ],
  context=[("Un deportista entrena y, según un estudio de ejemplo, sus células musculares aumentan de 1.800 a 2.400 mitocondrias. ¿Cuántas mitocondrias más tiene ahora?", "600", "2.400 − 1.800 = 600.", "2400-1800")],
  selfcheck=[("¿Por qué una célula muscular tiene muchas mitocondrias?", "Porque gasta mucha energía", "Las mitocondrias liberan energía."), ("¿Qué función tiene una célula pancreática?", "Fabricar y liberar enzimas digestivas e insulina", "Es una célula secretora."), ("¿Qué muestran las diferencias entre células?", "Que la estructura se ajusta a la función", "Es la diversidad celular.")],
  open_task=task("Completa una tabla de cuatro filas (muscular, nerviosa, intestinal, pancreática) con dos columnas: una característica de su estructura y la función que se relaciona con ella. Después escribe una frase que diga por qué una relación de datos no prueba por sí sola la causa.", "Muscular: muchas mitocondrias; se contrae y gasta mucha energía. Nerviosa: prolongaciones largas; conduce señales. Intestinal: pliegues; absorbe nutrientes. Pancreática: muchas estructuras para fabricar y liberar sustancias; secreta enzimas e insulina. Causa: hace falta una explicación de la función además del dato.", ["cuatro filas correctas", "relaciona estructura con función", "explica la limitación del dato"], ["tabla y una frase"], ["poner la función de una célula en otra", "olvidar la explicación de la causa"], "Pregunta qué medirías para comprobar la relación en una célula nueva."),
  reinforce="Escribe una característica de la neurona y su función.",
  extend="Explica por qué una célula muscular y una célula de la piel pueden tener cantidades distintas de mitocondrias.")

L(OA2, 5,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé a explicar patrones y mecanismos: cómo la fotosíntesis y la respiración celular se relacionan con los cloroplastos y las mitocondrias. Sirve para unir estructura, función y energía.",
  prior=["Sé las funciones de mitocondrias y cloroplastos.", "Sé que las células vegetales tienen ambas estructuras."],
  explain=[
      "La fotosíntesis ocurre en los cloroplastos: con luz, la célula transforma agua y dióxido de carbono en glucosa y oxígeno. La respiración celular ocurre en las mitocondrias: la célula combina glucosa y oxígeno para liberar energía, y produce dióxido de carbono y agua. Ambos procesos se complementan, porque lo que uno produce lo usa el otro.",
      "Las células vegetales tienen cloroplastos y mitocondrias, y realizan los dos procesos. Las animales solo tienen mitocondrias y obtienen la glucosa de los alimentos. Un patrón observable es que las células de las hojas, que reciben luz, tienen muchos cloroplastos, y las de la raíz, que están bajo tierra, no los tienen.",
      "Explicar un mecanismo es decir cómo ocurre algo, paso a paso. Para el mecanismo de la respiración celular: entra glucosa y oxígeno, se libera energía y salen dióxido de carbono y agua. Una buena explicación nombra qué entra, qué sale y en qué estructura ocurre, y no confunde el proceso con la respiración de los pulmones.",
  ],
  vocab=[("fotosíntesis", "proceso en que se fabrica glucosa con luz, agua y dióxido de carbono"), ("respiración celular", "proceso en que se libera energía de la glucosa usando oxígeno"), ("glucosa", "azúcar simple que usa la célula como fuente de energía"), ("mecanismo", "explicación paso a paso de cómo ocurre algo"), ("complementarios", "procesos que se completan porque uno produce lo que el otro usa")],
  worked=[
      ("Entradas y salidas", "En la respiración celular, ¿qué entra y qué sale?", ["Entran glucosa y oxígeno.", "Se libera energía y salen dióxido de carbono y agua."], "Entra glucosa y oxígeno; sale dióxido de carbono y agua, con liberación de energía"),
      ("Dónde ocurre", "¿Dónde ocurre la fotosíntesis y por qué una célula de raíz no la hace?", ["Ocurre en los cloroplastos.", "La raíz está sin luz y no tiene cloroplastos."], "En los cloroplastos; la raíz no los tiene"),
  ],
  mistakes=[
      ("Confundir respiración celular con respirar por los pulmones.", "Una ocurre dentro de las células y la otra mueve aire.", "Recuerda que la respiración celular libera energía."),
      ("Pensar que las plantas solo hacen fotosíntesis y no respiran.", "Sus mitocondrias liberan energía todo el tiempo.", "Una planta hace ambos procesos."),
  ],
  rec=[
      ("¿En qué estructura ocurre la fotosíntesis?", "En el cloroplasto", "Contiene clorofila que capta la luz."),
      ("¿En qué estructura ocurre la respiración celular?", "En la mitocondria", "Libera energía de la glucosa."),
      ("Verdadero o falso: las plantas también tienen mitocondrias.", "Verdadero", "Necesitan liberar energía de la glucosa."),
  ],
  und=[
      ("¿Qué produce la fotosíntesis? A) Glucosa y oxígeno; B) Dióxido de carbono y agua.", "A", "El dióxido de carbono y el agua salen de la respiración celular."),
      ("¿Por qué se dice que la fotosíntesis y la respiración celular se complementan? A) Lo que produce una lo usa la otra; B) Ocurren en la misma estructura.", "A", "La glucosa y el oxígeno de una son los insumos de la otra."),
      ("¿Qué proceso realiza una célula animal para obtener energía?", "Respiración celular", "Usa la glucosa de los alimentos."),
  ],
  app=[
      ("Cuatro células de ejemplo: hoja (muchos cloroplastos), raíz (sin cloroplastos), músculo animal, piel animal. ¿Cuántas hacen fotosíntesis?", "1", "Solo la de la hoja tiene cloroplastos."),
      ("Una hoja de ejemplo recibe luz 10 horas y otra recibe luz 2 horas, con el mismo número de células. ¿Cuál se espera que fabrique más glucosa? A) La que recibe 10 horas; B) La que recibe 2 horas.", "A", "Más luz permite más fotosíntesis."),
      arith("En un experimento de ejemplo, una planta fabrica 14 g de glucosa en el día y usa 6 g en la noche. ¿Cuántos gramos quedan?", "14-6", "Se resta lo usado a lo fabricado."),
  ],
  rea=[
      ("Un estudiante dice: «Las plantas no necesitan mitocondrias porque tienen cloroplastos». ¿Qué falla tiene? A) Los cloroplastos fabrican glucosa y las mitocondrias liberan su energía; B) Las plantas no tienen glucosa.", "A", "Los dos procesos cumplen funciones distintas."),
      ("¿Por qué una planta en un cuarto oscuro por varios días deja de fabricar glucosa?", "Porque no hay luz para la fotosíntesis", "Sin luz no se puede hacer fotosíntesis."),
  ],
  cha=[
      ("Se mide el oxígeno en un frasco con una planta: con luz sube y a oscuras baja. ¿Qué explica la subida con luz? A) La fotosíntesis produce oxígeno; B) La respiración celular produce oxígeno.", "A", "La fotosíntesis libera oxígeno."),
      ("Explica en una frase por qué a oscuras la cantidad de oxígeno del frasco baja.", "Porque la planta sigue respirando y consume oxígeno", "En la oscuridad solo ocurre la respiración celular."),
  ],
  context=[arith("Datos de ejemplo: en 1 hora una hoja produce 9 mg de oxígeno con luz y consume 2 mg por respiración. ¿Cuántos mg de oxígeno quedan de más?", "9-2", "Se resta el oxígeno consumido al producido.")],
  selfcheck=[("¿Qué produce la fotosíntesis?", "Glucosa y oxígeno", "Usa luz, agua y dióxido de carbono."), ("¿Qué libera la respiración celular?", "Energía", "Usa glucosa y oxígeno."), ("¿En qué estructuras ocurren?", "Cloroplastos y mitocondrias", "Cada una en una estructura distinta.")],
  open_task=task("Dibuja o describe un esquema de una célula vegetal con dos flechas: una que muestre qué entra y qué sale en el cloroplasto, y otra para la mitocondria. Escribe una frase con el patrón que explica por qué las células de la raíz no tienen cloroplastos.", "Cloroplasto: entran luz, agua y dióxido de carbono; salen glucosa y oxígeno. Mitocondria: entran glucosa y oxígeno; sale energía, con dióxido de carbono y agua. La raíz no recibe luz, por eso no tiene cloroplastos.", ["entradas y salidas correctas", "nombra la estructura de cada proceso", "explica el patrón de la raíz"], ["esquema y una frase"], ["invertir entradas y salidas", "decir que la raíz hace fotosíntesis"], "Pregunta qué cambiaría si faltara luz en la hoja."),
  reinforce="Escribe qué entra y qué sale en la fotosíntesis.",
  extend="Explica por qué se dice que fotosíntesis y respiración celular son procesos complementarios.")

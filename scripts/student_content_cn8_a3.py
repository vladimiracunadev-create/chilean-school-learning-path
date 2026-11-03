"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 03 (difusión y osmosis en células)."""
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


OA3 = "CN08 OA 03"

L(OA3, 1,
  materials="Este cuaderno y lápiz. Si quieres comprobarlo en casa: dos vasos de plástico, agua de la llave fría y tibia (nunca caliente) y una gota de colorante de alimentos, con una persona de tu casa cerca.",
  use="Aprenderé qué es la difusión y la osmosis, y a formular preguntas investigables con variables. Sirve para explicar cómo entran y salen sustancias de las células.",
  prior=["Sé que la membrana celular controla lo que entra y sale de la célula.", "Sé que una pregunta investigable se responde con observaciones o mediciones."],
  explain=[
      "Las células intercambian sustancias con su ambiente: entran nutrientes y oxígeno, y salen desechos y dióxido de carbono. Una forma de intercambio es la difusión: las partículas se mueven desde donde hay mayor concentración (más partículas en un mismo volumen) hacia donde hay menor concentración, hasta quedar repartidas parejo. La célula no gasta energía en este movimiento.",
      "La osmosis es la difusión del agua a través de una membrana que deja pasar el agua, pero no todos los solutos (las sustancias disueltas). El ejemplo de la vida diaria es una gota de colorante que se esparce sola en un vaso de agua: es difusión. Ocurre más rápido en agua tibia que en fría, y esa es una idea que se puede investigar.",
      "Una pregunta investigable nombra tres tipos de variables. La variable que se cambia es la independiente, la que se mide es la dependiente y las que se mantienen iguales son las controladas. Por ejemplo: «¿Se esparce más rápido una gota de colorante en 200 mL de agua tibia que en 200 mL de agua fría?». Independiente: temperatura. Dependiente: tiempo hasta que el color queda parejo. Controladas: cantidad de agua, de colorante y el tipo de vaso.",
  ],
  vocab=[("difusión", "movimiento de partículas desde mayor a menor concentración"), ("concentración", "cantidad de partículas en un volumen determinado"), ("osmosis", "difusión del agua a través de una membrana"), ("variable independiente", "la que se cambia a propósito"), ("variable dependiente", "la que se mide como resultado")],
  worked=[
      ("Dirección de la difusión", "En un vaso hay una zona con 100 partículas de colorante y otra sin colorante. ¿Hacia dónde se mueven las partículas?", ["Busco la zona con mayor concentración.", "Las partículas van desde la zona con colorante hacia la zona sin colorante."], "Hacia la zona sin colorante, hasta quedar parejas"),
      ("Identificar variables", "Pregunta: «¿Cambia la masa de una pasa si está 5 horas en agua con distinta cantidad de sal?». ¿Cuál es la variable independiente y cuál la dependiente?", ["Lo que se cambia a propósito es la cantidad de sal.", "Lo que se mide es la masa de la pasa."], "Independiente: cantidad de sal; dependiente: masa de la pasa"),
  ],
  mistakes=[
      ("Pensar que la difusión necesita que la célula gaste energía.", "Las partículas se mueven solas desde mayor a menor concentración.", "Piensa en el colorante que se esparce sin que nadie lo agite."),
      ("Cambiar dos variables a la vez en un experimento.", "Entonces no se sabe cuál causó el resultado.", "Cambia solo una y mantén iguales las demás."),
  ],
  rec=[
      ("En la difusión, las partículas se mueven desde la zona de ______ concentración hacia la de ______ concentración. Escribe las dos palabras.", "Mayor; menor", "Se mueven a favor de la diferencia de concentración."),
      ("¿La difusión necesita que la célula gaste energía: sí o no?", "No", "Es un movimiento espontáneo de las partículas."),
      ("Verdadero o falso: la osmosis es la difusión del agua a través de una membrana.", "Verdadero", "Es el nombre de ese caso particular de difusión."),
  ],
  und=[
      ("Se agrega una gota de colorante a un vaso de agua quieta. ¿Qué ocurre con el tiempo? A) Las partículas se reparten hasta quedar parejas; B) Todas se quedan juntas en el fondo.", "A", "La difusión reparte las partículas."),
      ("¿Cuál es un ejemplo de difusión en una célula? A) El oxígeno entra desde donde hay más hacia donde hay menos; B) La célula empuja el oxígeno hacia donde ya hay mucho.", "A", "La difusión va de mayor a menor concentración."),
      ("¿Cuál pregunta es investigable? A) ¿Se esparce más rápido el colorante en agua tibia que en agua fría? B) ¿Es más bonito el colorante rojo que el azul?", "A", "Se responde midiendo el tiempo; la otra es una opinión."),
  ],
  app=[
      ("En «¿Se esparce más rápido el colorante en agua tibia que en agua fría?», ¿qué variable se cambia?", "La temperatura del agua", "Es lo que difiere entre los dos vasos."),
      ("En esa misma pregunta, ¿qué variable se mide?", "El tiempo hasta que el color queda parejo", "Es el resultado que se registra."),
      ("Para que la comparación sea justa, ¿qué debe mantenerse igual en los dos vasos? A) La cantidad de agua y de colorante; B) La temperatura del agua.", "A", "La temperatura es la variable que se cambia."),
  ],
  rea=[
      ("Un estudiante compara colorante en 200 mL de agua fría con colorante en 400 mL de agua tibia. ¿Qué falla tiene su prueba? A) Cambió dos variables a la vez; B) Usó dos vasos iguales.", "A", "Cambió la temperatura y la cantidad de agua, y no sabrá cuál afectó."),
      ("Al abrir un frasco de aroma en una pieza sin corrientes de aire, el olor llega con el tiempo a todos los rincones. ¿Qué proceso explica esto?", "La difusión", "Las partículas del aroma se mueven desde donde hay más hacia donde hay menos."),
  ],
  cha=[
      ("¿Cuál es la mejor forma investigable de la pregunta «¿Qué pasa con las pasas en agua?». A) ¿Cuánto aumenta la masa de una pasa en agua de la llave después de 6 horas? B) ¿Son sabrosas las pasas mojadas?", "A", "Indica qué se mide y en qué condición."),
      arith("Se mide el tiempo que demora el color en quedar parejo: agua fría, 15 minutos; agua tibia, 6 minutos. ¿Cuántos minutos menos demoró el agua tibia?", "15-6", "Se resta el menor tiempo al mayor."),
  ],
  context=[("Una persona deja una bolsita de té en un vaso con agua tibia y ve que el color pasa de la bolsita al agua. ¿Qué proceso explica que las sustancias coloreadas salgan?", "La difusión", "Las partículas pasan de la zona de mayor concentración a la de menor.")],
  selfcheck=[("¿Qué es la difusión?", "El movimiento de partículas desde mayor a menor concentración", "No requiere gasto de energía."), ("¿Qué es la osmosis?", "La difusión del agua a través de una membrana", "Es un caso especial de difusión."), ("¿Qué variable se mide en un experimento?", "La dependiente", "Es el resultado.")],
  open_task=task("Plantea una pregunta investigable sobre difusión usando esta situación: colorante, dos vasos y agua a dos temperaturas. Escribe la variable que cambias, la que mides y dos que mantendrías iguales, y una predicción.", "Pregunta: ¿Se esparce más rápido el colorante en agua tibia que en fría? Cambio: temperatura. Mido: tiempo hasta color parejo. Iguales: cantidad de agua y de colorante. Predicción: en agua tibia será más rápido.", ["pregunta con variables claras", "dos controladas", "una predicción"], ["pregunta, variables y predicción"], ["no indicar qué se mide", "cambiar dos variables a la vez"], "Pregunta qué resultado contradiría tu predicción."),
  reinforce="Escribe un ejemplo de difusión de la vida diaria.",
  extend="Explica por qué una prueba justa cambia una sola variable.")

L(OA3, 2,
  materials="Este cuaderno y lápiz. Los datos de las tablas son de ejemplo y están escritos en cada ejercicio.",
  use="Aprenderé a leer datos y esquemas de osmosis para saber hacia dónde se mueve el agua. Sirve para interpretar una evidencia experimental.",
  prior=["Sé qué es la difusión y la osmosis.", "Sé identificar variables independiente y dependiente."],
  explain=[
      "La membrana celular es semipermeable: deja pasar el agua y ciertas sustancias, pero no todas. En la osmosis, el agua pasa a través de la membrana desde la zona con menos soluto hacia la zona con más soluto. Un soluto es una sustancia disuelta, como la sal. Una solución con más soluto tiene menos agua libre.",
      "Para leer un experimento se compara el cambio de masa. Datos de ejemplo con tiras de papa de 10 g cada una: en agua pura, a las 2 horas pesan 12 g; en agua con 1 % de sal, 10 g; en agua con 5 % de sal, 7 g. En el agua pura entró agua a las células. En 1 % no hubo cambio neto. En 5 % salió agua de las células.",
      "El cambio porcentual de masa se calcula como (cambio ÷ masa inicial) × 100. En agua pura: (12 − 10) ÷ 10 × 100 = 20 % de aumento. Un esquema con flechas puede mostrar la dirección del agua. Antes de concluir, hay que decir cuál es el dato decisivo y una limitación, por ejemplo que se hizo una sola medición.",
  ],
  vocab=[("semipermeable", "que deja pasar algunas sustancias y otras no"), ("soluto", "sustancia disuelta en un líquido"), ("cambio neto", "diferencia total entre lo que entra y lo que sale"), ("cambio porcentual", "cambio dividido por el valor inicial, multiplicado por 100"), ("dato decisivo", "el dato que más pesa para sacar una conclusión")],
  worked=[
      ("Hacia dónde va el agua", "Una tira de papa está en agua con 5 % de sal. Pasó de 10 g a 7 g. ¿Hacia dónde se movió el agua?", ["La masa disminuyó: perdió agua.", "El agua salió de las células hacia la solución con más soluto."], "Salió de las células hacia el exterior"),
      ("Cambio porcentual", "Una tira pasó de 10 g a 12 g. ¿Cuál es el cambio porcentual?", ["Cambio: 12 − 10 = 2 g.", "(2 ÷ 10) × 100 = 20 %."], "Aumentó 20 %"),
  ],
  mistakes=[
      ("Creer que el agua siempre se mueve hacia donde hay menos sal.", "En la osmosis el agua va hacia donde hay más soluto.", "Piensa en dónde hay más soluto y menos agua libre."),
      ("Decir que si la masa no cambia, no pasa nada.", "Entra y sale la misma cantidad de agua: el cambio neto es cero.", "Distingue movimiento y cambio neto."),
  ],
  rec=[
      ("¿La membrana celular es semipermeable: deja pasar todo o solo algunas sustancias?", "Solo algunas", "Regula lo que entra y sale."),
      ("En la osmosis, ¿el agua va hacia la zona con más soluto o con menos soluto?", "Con más soluto", "Es donde hay menos agua libre."),
      ("¿Qué es un soluto?", "Una sustancia disuelta", "Por ejemplo la sal en el agua."),
  ],
  und=[
      ("Una tira de papa pesa más después de estar en agua pura. ¿Qué pasó? A) Entró agua a sus células; B) Salió agua de sus células.", "A", "El interior de la célula tiene más soluto que el agua pura."),
      ("Una tira de papa pasa de 10 g a 10 g en una solución. ¿Qué indica? A) No hubo cambio neto de agua; B) El agua dejó de moverse.", "A", "Entra y sale igual cantidad."),
      ("¿Qué indica la pérdida de masa de una tira de papa en agua con mucha sal?", "Que salió agua de las células", "El agua va hacia donde hay más soluto."),
  ],
  app=[
      arith("Datos de ejemplo: una tira de zanahoria pasa de 20 g a 25 g en agua pura. ¿Cuántos gramos ganó?", "25-20", "Se resta la masa inicial a la final."),
      arith("Una tira de papa de 10 g pasa a 6 g en agua con 3 % de sal. ¿Qué porcentaje de su masa perdió?", "(10-6)*100//10", "El cambio de 4 g respecto de 10 g, por 100.", " %"),
      ("Otra tira de papa de 10 g queda con 10 g en una solución. ¿Qué tipo de movimiento neto de agua hubo?", "Ninguno", "No cambió la masa."),
  ],
  rea=[
      ("Un compañero dice: «La papa perdió masa en agua con sal porque la sal se comió el agua». ¿Qué explicación científica es mejor? A) El agua salió de las células hacia donde había más soluto; B) La sal destruyó las células.", "A", "Es el movimiento de agua por osmosis."),
      ("¿Qué dato de la tabla (agua pura 12 g, 1 % de sal 10 g, 5 % de sal 7 g; todas empezaron en 10 g) muestra que 1 % de sal es parecida al interior de la papa?", "La masa no cambió", "Con igual concentración, no hay cambio neto."),
  ],
  cha=[
      ("Una estudiante midió solo una tira por vaso. ¿Cuál es una limitación de su evidencia? A) Una sola medición puede tener errores, y conviene repetir; B) Pesar tiras de papa no sirve para estudiar la osmosis.", "A", "Repetir permite confirmar el resultado."),
      arith("Una tira de zanahoria de 40 g de ejemplo, en agua pura, gana 6 g. ¿Qué porcentaje de su masa inicial aumentó?", "6*100//40", "El cambio de 6 g sobre la masa inicial de 40 g, por 100.", " %"),
  ],
  context=[("Una persona deja lechuga en agua con mucha sal de ejemplo y a los 30 minutos las hojas se ven blandas y arrugadas. ¿Qué movimiento de agua explica el cambio?", "Salió agua de las células", "El agua fue hacia la solución con más soluto.")],
  selfcheck=[("¿Hacia dónde va el agua en la osmosis?", "Hacia donde hay más soluto", "Pasa por la membrana semipermeable."), ("¿Qué indica que la masa suba en agua pura?", "Que entró agua a las células", "Tienen más soluto dentro."), ("¿Cómo se calcula el cambio porcentual?", "Cambio dividido por la masa inicial, por 100", "Sirve para comparar tiras de distinta masa.")],
  open_task=task("Con estos datos de ejemplo (tiras de papa de 10 g): agua pura 12 g; sal 1 % 10 g; sal 5 % 7 g, haz una tabla con el cambio de masa y el cambio porcentual, y escribe una conclusión que diga hacia dónde se movió el agua en cada vaso y una limitación.", "Agua pura: +2 g, +20 %, entró agua. Sal 1 %: 0 g, 0 %, sin cambio neto. Sal 5 %: −3 g, −30 %, salió agua. Limitación: una sola tira por vaso.", ["tres filas con cambio y porcentaje", "dirección del agua en cada caso", "una limitación"], ["tabla y conclusión"], ["invertir la dirección del agua", "olvidar el signo negativo"], "Pregunta qué pasaría con una solución de 3 % de sal."),
  reinforce="Escribe hacia dónde se mueve el agua cuando hay más sal fuera de la célula.",
  extend="Explica por qué una masa constante no significa que el agua no se mueva.")

L(OA3, 3,
  materials="Este cuaderno y lápiz. Los esquemas están descritos con palabras en cada ejercicio.",
  use="Aprenderé a construir un modelo de partículas y membrana para predecir qué pasa con células animales y vegetales en distintas soluciones. Sirve para explicar por qué una célula se hincha o se arruga.",
  prior=["Sé que el agua se mueve por osmosis hacia donde hay más soluto.", "Sé que las células vegetales tienen pared celular."],
  explain=[
      "Un modelo de partículas dibuja puntos pequeños para el agua y puntos grandes para el soluto. Una membrana semipermeable tiene poros que dejan pasar los puntos pequeños (agua) y no los grandes. Con este modelo se puede predecir la dirección del agua: va hacia el lado con más puntos grandes.",
      "Se usan tres palabras para comparar la solución exterior con el interior de la célula. Hipotónica: el exterior tiene menos soluto que la célula. Isotónica: tienen igual soluto. Hipertónica: el exterior tiene más soluto. En una solución hipotónica, entra agua. En una isotónica, no hay cambio neto. En una hipertónica, sale agua.",
      "Una célula animal en solución hipotónica se hincha y puede reventar. En hipertónica se arruga. Una célula vegetal en hipotónica se pone turgente (firme), porque la pared evita que reviente. En hipertónica pierde agua y la membrana se despega de la pared, lo que se llama plasmólisis. Por eso una planta sin agua se marchita.",
  ],
  vocab=[("hipotónica", "solución con menos soluto que el interior de la célula"), ("isotónica", "solución con igual cantidad de soluto que el interior de la célula"), ("hipertónica", "solución con más soluto que el interior de la célula"), ("turgente", "firme porque la célula vegetal está llena de agua"), ("plasmólisis", "separación de la membrana y la pared por pérdida de agua")],
  worked=[
      ("Predecir con el modelo", "La célula tiene 2 partículas de soluto por unidad y la solución exterior tiene 6. ¿Qué tipo de solución es y hacia dónde va el agua?", ["El exterior tiene más soluto que la célula.", "Es hipertónica y el agua sale de la célula."], "Hipertónica; el agua sale de la célula"),
      ("Célula vegetal", "Una célula vegetal está en agua pura. ¿Qué le pasa?", ["El agua pura es hipotónica: entra agua.", "La pared evita que reviente."], "Se pone turgente"),
  ],
  mistakes=[
      ("Pensar que una célula vegetal reventará igual que una animal en agua pura.", "La pared celular lo evita.", "Recuerda que la pared sostiene a la célula vegetal."),
      ("Confundir hipotónica con hipertónica.", "Se comparan con el interior de la célula: hipo es menos soluto fuera, hiper es más fuera.", "Compara siempre el soluto del exterior con el del interior."),
  ],
  rec=[
      ("Una solución con más soluto que la célula es ______ (hipotónica o hipertónica).", "Hipertónica", "Hiper significa más."),
      ("¿Qué pasa con el agua en una solución isotónica: entra, sale o no hay cambio neto?", "No hay cambio neto", "Hay igual soluto dentro y fuera."),
      ("Verdadero o falso: la pared protege a la célula vegetal de reventar en agua pura.", "Verdadero", "La pared es rígida."),
  ],
  und=[
      ("Una célula animal está en una solución hipotónica. ¿Qué le pasa? A) Se hincha; B) Se arruga.", "A", "Entra agua a la célula."),
      ("Una célula vegetal en solución hipertónica pierde agua. ¿Cómo se llama el fenómeno en que la membrana se despega de la pared?", "Plasmólisis", "Es la separación por pérdida de agua."),
      ("¿Por qué una planta sin riego se marchita? A) Sus células pierden agua y pierden turgencia; B) Sus células crecen demasiado.", "A", "Sin agua, las células dejan de estar firmes."),
  ],
  app=[
      ("La célula tiene 4 partículas de soluto por unidad. Tres soluciones tienen 1, 4 y 9 partículas. ¿Cuál es isotónica?", "La de 4", "Tiene el mismo soluto que la célula."),
      ("Con los mismos datos (célula con 4 partículas por unidad y soluciones de 1, 4 y 9), ¿en cuál sale agua de la célula? Escribe la cantidad de partículas.", "En la de 9", "Es la hipertónica."),
      ("Un glóbulo rojo (célula animal) se coloca en agua pura. ¿Qué esperas que pase? A) Se hinche y pueda reventar; B) Se arrugue.", "A", "El agua pura es hipotónica: entra agua."),
  ],
  rea=[
      ("Un estudiante dice: «En agua pura la célula vegetal pierde agua». ¿Qué corrección haces? A) Entra agua y se pone turgente; B) No pasa nada con el agua.", "A", "El interior tiene más soluto que el agua pura."),
      ("¿Por qué sirve poner suero fisiológico (isotónico) en una herida limpia y no agua con mucha sal? Responde en una frase.", "Porque el isotónico no hace entrar ni salir agua de las células", "Con mucha sal sale agua y se dañan las células."),
  ],
  cha=[
      ("Dato de ejemplo: una célula animal y una vegetal se ponen en agua pura. Después de un rato, solo una reventó. ¿Cuál? Escribe animal o vegetal.", "Animal", "La vegetal tiene pared."),
      ("Un modelo de papel muestra una membrana con poros de 10 mm. El agua mide 5 mm y el soluto 20 mm. ¿Qué pasa por la membrana? A) Solo el agua; B) Solo el soluto.", "A", "El soluto es más grande que los poros."),
  ],
  context=[("Una persona pone hojas de lechuga marchitas en agua de la llave por una hora y quedan firmes. ¿Qué tipo de solución es el agua de la llave respecto de las células?", "Hipotónica", "Entra agua y las hojas recuperan la turgencia.")],
  selfcheck=[("¿Qué hace la membrana semipermeable?", "Deja pasar el agua y no todos los solutos", "Regula el paso."), ("¿Qué le pasa a una célula animal en solución hipertónica?", "Se arruga", "Pierde agua hacia afuera."), ("¿Qué es la turgencia?", "La firmeza de una célula vegetal llena de agua", "La pared la mantiene.")],
  open_task=task("Dibuja tres cuadros de una célula animal en solución hipotónica, isotónica e hipertónica con flechas de agua y puntos para el soluto. Debajo de cada cuadro escribe qué le ocurre a la célula. Agrega una frase sobre qué cambia si la célula es vegetal.", "Hipotónica: entra agua, se hincha. Isotónica: sin cambio neto. Hipertónica: sale agua, se arruga. Si es vegetal: en hipotónica se pone turgente porque tiene pared.", ["tres cuadros con flechas correctas", "una frase por cuadro", "diferencia con célula vegetal"], ["tres dibujos y frases"], ["invertir la dirección del agua", "olvidar la pared"], "Pregunta qué pasaría si la pared celular no existiera."),
  reinforce="Escribe qué le pasa a una célula animal en una solución hipertónica.",
  extend="Explica con tus palabras por qué las plantas se marchitan sin agua.")

L(OA3, 4,
  materials="Este cuaderno y lápiz. Las tablas de datos son de ejemplo.",
  use="Aprenderé a relacionar variables de la difusión y la osmosis: temperatura, concentración y tiempo. Sirve para planificar un experimento justo y concluir con datos.",
  prior=["Sé identificar variables.", "Sé calcular promedios y cambios porcentuales con enteros."],
  explain=[
      "Se puede investigar cómo una variable afecta la rapidez de la difusión. La rapidez se calcula como distancia ÷ tiempo. Si un colorante avanza 6 cm en 3 minutos, su rapidez es 2 cm por minuto. Con mayor temperatura, las partículas se mueven más rápido y la difusión también. Con mayor diferencia de concentración, la difusión es más rápida al comienzo.",
      "Un experimento justo cambia solo una variable, mantiene constantes las demás y repite la medición. Repetir permite calcular un promedio: se suman los resultados y se divide por el número de repeticiones. Por ejemplo, tiempos de 10, 12 y 14 minutos dan un promedio de 36 ÷ 3 = 12 minutos.",
      "Para concluir con datos, se describe la relación (a más temperatura, menos tiempo) y se declara una limitación (pocas repeticiones o un vaso distinto). Una correlación entre dos variables apoya la conclusión, pero no demuestra por sí sola la causa. Lo que sí ayuda es cambiar una variable a la vez y obtener siempre el mismo patrón.",
  ],
  vocab=[("rapidez", "distancia recorrida dividida por el tiempo"), ("promedio", "suma de los resultados dividida por el número de mediciones"), ("variable controlada", "la que se mantiene igual para que la prueba sea justa"), ("repetición", "volver a medir en las mismas condiciones"), ("limitación", "aspecto que impide afirmar más de lo medido")],
  worked=[
      ("Rapidez de difusión", "El colorante avanza 8 cm en 4 minutos. ¿Cuál es su rapidez?", ["Rapidez = distancia ÷ tiempo.", "8 ÷ 4 = 2."], "2 cm por minuto"),
      ("Promedio", "Tres repeticiones dieron 20, 22 y 24 segundos. ¿Cuál es el promedio?", ["Sumo: 20 + 22 + 24 = 66.", "Divido por 3: 66 ÷ 3 = 22."], "22 segundos"),
  ],
  mistakes=[
      ("Concluir con una sola medición.", "Un resultado único puede tener un error.", "Repite y usa el promedio."),
      ("Decir que dos variables relacionadas siempre se causan entre sí.", "Hay que cambiar una y mantener controladas las otras.", "Controla las variables."),
  ],
  rec=[
      ("Si aumenta la temperatura del agua, ¿la difusión se hace más rápida o más lenta?", "Más rápida", "Las partículas se mueven más rápido."),
      ("¿Cómo se calcula la rapidez: distancia entre tiempo o tiempo entre distancia?", "Distancia entre tiempo", "Es distancia ÷ tiempo."),
      ("Verdadero o falso: repetir una medición permite calcular un promedio.", "Verdadero", "Se suman los resultados y se divide por el número de repeticiones."),
  ],
  und=[
      ("¿Para qué sirve repetir un experimento? A) Para confirmar el resultado y reducir errores; B) Para cambiar la variable independiente.", "A", "Varias mediciones dan más confianza."),
      ("¿Qué variable debe mantenerse constante en una prueba de temperatura? A) La cantidad de agua; B) La temperatura.", "A", "La temperatura es la que se cambia."),
      ("Datos de ejemplo: a 10 °C el color se reparte en 20 min; a 30 °C, en 8 min. ¿Qué relación se observa?", "A mayor temperatura, menor tiempo", "La difusión es más rápida con calor."),
  ],
  app=[
      arith("El colorante avanza 12 cm en 6 minutos. ¿Cuántos centímetros por minuto avanza?", "12//6", "Rapidez = distancia ÷ tiempo."),
      arith("Tres repeticiones de un experimento de ejemplo dieron 9, 11 y 16 minutos. ¿Cuál es el promedio en minutos?", "(9+11+16)//3", "Se suman y se divide por 3."),
      arith("Un vaso con agua a 30 °C tarda 8 minutos y otro a 10 °C tarda 20 minutos. ¿Cuántos minutos más tarda el de 10 °C?", "20-8", "Se resta el tiempo menor al mayor."),
  ],
  rea=[
      ("Un estudiante mide una vez y escribe: «El colorante es siempre más rápido en agua tibia». ¿Qué falla tiene su afirmación? A) Generaliza con una sola medición; B) Usó agua tibia en vez de fría.", "A", "Hace falta repetir para concluir."),
      ("Un grupo cambia la temperatura y la cantidad de colorante a la vez. ¿Pueden saber cuál variable causó la diferencia?", "No", "Cambiaron dos variables a la vez."),
  ],
  cha=[
      ("Datos de ejemplo de tiras de papa en soluciones de sal de 0, 1, 2 y 4 por ciento: cambio de masa +2, 0, −1 y −3 g. ¿Qué relación hay entre el aumento de la sal y el cambio de masa? A) A más sal, la masa cambia hacia pérdida; B) A más sal, la masa siempre sube.", "A", "Los valores van de ganancia a pérdida."),
      arith("Con esos datos de ejemplo, ¿cuántos gramos de diferencia hay entre la solución de 0 % y la de 4 %? (Cambios de +2 g y −3 g.)", "2+3", "Se suman las distancias desde el cero: 2 y 3."),
  ],
  context=[arith("Una persona de ejemplo repite 4 veces la medición del tiempo en que el aroma llega a la otra esquina de una pieza y obtiene 20, 24, 28 y 24 segundos. ¿Cuál es el promedio?", "(20+24+28+24)//4", "Se suman los cuatro tiempos y se divide por 4.")],
  selfcheck=[("¿Cómo se calcula la rapidez?", "Distancia dividida por el tiempo", "Es una razón."), ("¿Por qué se repite un experimento?", "Para confirmar y reducir errores", "Permite sacar un promedio."), ("¿Qué relación hay entre temperatura y difusión?", "A mayor temperatura, más rápida", "Las partículas se mueven más rápido.")],
  open_task=task("Planifica un experimento seguro con colorante de alimentos y agua del grifo (fría y tibia, nunca caliente) para saber si la temperatura cambia la rapidez de difusión. Escribe: la pregunta, la variable que cambias, la que mides, tres variables que controlas, cuántas repeticiones harás y qué medidas de seguridad tomas.", "Pregunta: ¿Cambia la rapidez de difusión del colorante con la temperatura? Cambio: temperatura. Mido: tiempo hasta color parejo. Controlo: volumen de agua, gotas de colorante, tipo de vaso. Repito: 3 veces. Seguridad: agua tibia, sin vidrio, con una persona adulta cerca.", ["pregunta clara", "tres variables controladas", "repeticiones y seguridad"], ["plan escrito"], ["cambiar dos variables a la vez", "usar agua caliente"], "Pregunta cómo cambiaría el plan si usaras agua con sal."),
  reinforce="Calcula el promedio de 10, 12 y 14.",
  extend="Explica por qué un solo experimento no basta para afirmar una regla general.")

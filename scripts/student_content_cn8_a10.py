"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 10 (circuitos eléctricos en serie y paralelo, circuito domiciliario)."""
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


OA10 = "CN08 OA 10"

L(OA10, 1,
  materials="Este cuaderno y lápiz. Opcional: una linterna con pilas pequeñas y dos ampolletas pequeñas de linterna con cables, con una persona de tu casa cerca. NUNCA hagas experimentos con enchufes, cables de la casa ni aparatos conectados a la red.",
  use="Aprenderé qué es un circuito eléctrico, qué miden el volt, el ampere y el ohm, y a plantear preguntas investigables sobre circuitos en serie y en paralelo. Sirve para entender cómo funcionan los aparatos eléctricos.",
  prior=["Sé que una pila transforma energía química en eléctrica.", "Sé distinguir variable independiente y dependiente."],
  explain=[
      "Un circuito eléctrico es un camino cerrado por donde circulan cargas eléctricas. Tiene una fuente (una pila o la red), conductores (cables) y receptores (ampolletas, motores). Si el camino se abre, la corriente se detiene. La diferencia de potencial o voltaje (V, se mide en volts) es lo que impulsa las cargas. La intensidad de corriente (I, se mide en amperes, A) es la cantidad de carga que pasa por segundo. La resistencia (R, se mide en ohms, Ω) es la dificultad que opone un material al paso de la corriente.",
      "Hay dos formas básicas de conectar receptores. En serie, los receptores se conectan uno a continuación del otro, con un solo camino para la corriente. En paralelo, cada receptor tiene su propia rama y hay varios caminos. Por ejemplo, dos ampolletas en serie comparten el mismo camino; dos en paralelo tienen cada una su camino conectado a la fuente.",
      "Una pregunta investigable sobre esto es: «¿Cambia el brillo de una ampolleta de linterna si se conecta otra igual en serie?». Se cambia el número de ampolletas, se mide el brillo en una escala de 1 a 5 y se mantienen iguales la pila y los cables. «¿Cuál circuito es más bonito?» no se puede investigar, porque depende de gustos.",
  ],
  vocab=[("circuito eléctrico", "camino cerrado por donde circulan cargas"), ("diferencia de potencial (V)", "lo que impulsa las cargas; se mide en volts"), ("intensidad de corriente (I)", "carga que pasa por segundo; se mide en amperes"), ("resistencia (R)", "dificultad al paso de la corriente; se mide en ohms"), ("serie y paralelo", "formas de conectar receptores: un camino o varios caminos")],
  worked=[
      ("Serie o paralelo", "Dos ampolletas están conectadas una a continuación de la otra con un solo camino para la corriente. ¿Qué conexión es?", ["Reviso cuántos caminos hay.", "Hay uno solo."], "Conexión en serie"),
      ("Pregunta investigable", "¿Es investigable «¿Cambia el brillo de una ampolleta al conectar otra igual en serie?»?", ["Pregunto si se puede medir.", "Se puede medir el brillo con una escala de 1 a 5."], "Sí, porque se mide el brillo"),
  ],
  mistakes=[
      ("Pensar que la corriente se «gasta» al pasar por una ampolleta.", "La corriente es el flujo de cargas; la energía es la que se transforma.", "Piensa en cargas que circulan y energía que se transforma."),
      ("Confundir voltaje con corriente.", "El voltaje impulsa y la corriente es el flujo.", "Recuerda las unidades: volt y ampere."),
  ],
  rec=[
      ("¿En qué unidad se mide la intensidad de corriente: en amperes o en ohms?", "En amperes", "El ampere mide la intensidad de corriente."),
      ("En un circuito en serie, ¿hay un solo camino o varios?", "Un solo camino", "Los receptores se conectan uno a continuación del otro."),
      ("Verdadero o falso: en un circuito en paralelo hay más de un camino para la corriente.", "Verdadero", "Cada receptor tiene su rama."),
  ],
  und=[
      ("¿Cuál es un circuito cerrado? A) Una pila, cables y una ampolleta formando un lazo completo; B) Una pila y una ampolleta con un cable suelto.", "A", "La corriente necesita un camino completo."),
      ("¿En qué unidad se mide la resistencia? A) Ohm; B) Volt.", "A", "El volt mide la diferencia de potencial."),
      ("¿Cuál pregunta es investigable? A) ¿Cambia el brillo de una ampolleta al conectar otra igual en serie? B) ¿Cuál circuito es más bonito?", "A", "Se responde midiendo el brillo."),
  ],
  app=[
      ("En «¿Cambia el brillo si se agrega otra ampolleta en serie?», ¿qué variable se cambia?", "El número de ampolletas", "Es lo que difiere entre las pruebas."),
      ("En esa misma pregunta, ¿qué variable se mide?", "El brillo de la ampolleta", "Es el resultado que se registra."),
      arith("En una escala de brillo de ejemplo, una ampolleta sola marca 5 y con otra en serie marca 2. ¿Cuántos puntos baja el brillo?", "5-2", "Se resta el valor final al inicial."),
  ],
  rea=[
      ("Un grupo cambia el número de ampolletas y también la pila en la misma prueba. ¿Qué falla tiene? A) No sabrá cuál cambio causó el resultado; B) No puede medir el brillo.", "A", "Cambió dos variables a la vez."),
      ("Dos ampolletas están en serie y una se suelta de su base. ¿Qué pasa con la otra?", "Se apaga", "El camino queda abierto y no circula corriente."),
  ],
  cha=[
      ("Dos ampolletas en paralelo y una se suelta de su base. ¿Qué predices para la otra? A) Sigue encendida; B) Se apaga.", "A", "Tiene su propia rama conectada a la fuente."),
      ("¿Por qué un circuito necesita estar cerrado para que circule corriente? A) Las cargas necesitan un camino completo; B) Para que la pila se enfríe.", "A", "Si el camino se abre, se detiene el flujo."),
  ],
  context=[arith("Un juguete de ejemplo usa dos baterías de 9 V conectadas una a continuación de la otra. ¿Cuántos volts entregan en total?", "9*2", "En serie los voltajes se suman.")],
  selfcheck=[("¿Qué es un circuito cerrado?", "Un camino completo por donde circulan cargas", "Si se abre, se detiene la corriente."), ("¿Qué unidad mide el voltaje?", "El volt", "Es la diferencia de potencial."), ("¿Cuál es la diferencia entre serie y paralelo?", "En serie hay un solo camino y en paralelo hay varios", "Cambia cómo circula la corriente.")],
  open_task=task("Escribe una pregunta investigable sobre el brillo de dos ampolletas de linterna conectadas en serie o en paralelo con una pila. Indica la variable que cambias, la que mides, dos que mantienes iguales, una predicción y una medida de seguridad (solo pilas pequeñas, nunca enchufes).", "Pregunta: ¿Brillan más dos ampolletas en paralelo que en serie con la misma pila? Cambio: tipo de conexión. Mido: brillo en escala de 1 a 5. Igual: la pila y las ampolletas. Predicción: más brillo en paralelo. Seguridad: solo pilas pequeñas y una persona adulta cerca.", ["pregunta clara", "dos controladas", "predicción y seguridad"], ["plan breve"], ["pregunta de opinión", "usar enchufes"], "Pregunta qué cambiaría con una pila más débil."),
  reinforce="Escribe qué unidad mide el voltaje, la corriente y la resistencia.",
  extend="Explica por qué un circuito necesita estar cerrado para funcionar.")

L(OA10, 2,
  materials="Este cuaderno y lápiz. Las tablas de mediciones son de ejemplo y están escritas en cada ejercicio.",
  use="Aprenderé a examinar mediciones y esquemas de circuitos en serie y en paralelo para sacar conclusiones sobre voltaje y corriente. Sirve para leer la evidencia de un circuito.",
  prior=["Sé qué son voltaje, corriente y resistencia.", "Sé sumar y comparar valores."],
  explain=[
      "En un circuito en serie, la corriente es la misma en todos los puntos, porque hay un solo camino. El voltaje de la fuente se reparte entre los receptores: la suma de los voltajes de cada receptor es igual al voltaje total. Datos de ejemplo de una fuente de 12 V con dos ampolletas iguales en serie: cada una tiene 6 V, y 6 + 6 = 12.",
      "En un circuito en paralelo, el voltaje es el mismo en cada rama, igual al de la fuente. La corriente total se reparte entre las ramas: la suma de las corrientes de las ramas es igual a la corriente total. Datos de ejemplo con una fuente de 12 V y dos ramas: una rama con 2 A y otra con 3 A; la corriente total es 2 + 3 = 5 A.",
      "Al leer las mediciones hay que distinguir lo que se midió (valores en volts y amperes) de lo que se concluye (en serie se reparte el voltaje; en paralelo se reparte la corriente). Una limitación es que los instrumentos tienen error y que los datos son de un solo montaje. También hay que fijarse en las unidades y en qué punto del circuito se midió.",
  ],
  vocab=[("reparto de voltaje", "división del voltaje de la fuente entre los receptores en serie"), ("reparto de corriente", "división de la corriente total entre las ramas en paralelo"), ("rama", "camino independiente de un circuito en paralelo"), ("voltímetro", "instrumento que mide diferencia de potencial"), ("amperímetro", "instrumento que mide intensidad de corriente")],
  worked=[
      ("Serie: el voltaje se reparte", "Una fuente de 9 V alimenta dos receptores en serie. El primero tiene 4 V. ¿Cuántos volts tiene el segundo?", ["La suma de los voltajes es 9 V.", "9 − 4 = 5."], "5 V"),
      ("Paralelo: la corriente se reparte", "Una rama tiene 1 A y otra 4 A. ¿Cuánta corriente entrega la fuente?", ["La corriente total es la suma.", "1 + 4 = 5."], "5 A"),
  ],
  mistakes=[
      ("Creer que en serie cada receptor recibe el voltaje completo.", "El voltaje de la fuente se reparte entre ellos.", "Suma los voltajes de los receptores."),
      ("Pensar que en paralelo el voltaje se reparte.", "En paralelo cada rama tiene el voltaje de la fuente.", "Compara con la fuente."),
  ],
  rec=[
      ("En un circuito en serie, ¿la corriente es la misma en todos los puntos: sí o no?", "Sí", "Hay un solo camino."),
      ("En paralelo, ¿cada rama tiene el voltaje de la fuente: sí o no?", "Sí", "Todas están conectadas a los mismos bornes."),
      ("Verdadero o falso: un amperímetro mide intensidad de corriente.", "Verdadero", "Su unidad es el ampere."),
  ],
  und=[
      ("En serie, ¿qué se reparte entre los receptores? A) El voltaje; B) La corriente.", "A", "La corriente es igual en todo el camino."),
      ("En paralelo, ¿qué se reparte entre las ramas? A) La corriente; B) El voltaje.", "A", "El voltaje es el mismo en cada rama."),
      ("Una medición dice «5 A». ¿Qué magnitud es?", "La intensidad de corriente", "El ampere mide intensidad."),
  ],
  app=[
      arith("En serie, una fuente de 15 V alimenta tres receptores. Los dos primeros tienen 5 V y 6 V. ¿Cuántos volts tiene el tercero?", "15-5-6", "La suma de los voltajes debe ser el total."),
      arith("En paralelo hay tres ramas con 2 A, 3 A y 5 A. ¿Cuánta corriente total entrega la fuente?", "2+3+5", "Se suman las corrientes de las ramas."),
      ("En un circuito en paralelo con una fuente de 12 V, ¿cuántos volts hay en cada rama?", "12 V", "Cada rama tiene el voltaje de la fuente."),
  ],
  rea=[
      ("Alguien mide 3 A antes de una ampolleta y 2 A después de ella en un circuito en serie. ¿Qué hace dudar de la medición? A) En serie la corriente debe ser la misma; B) Las ampolletas no se miden.", "A", "Con un solo camino, la corriente es igual."),
      ("Una persona mide 6 V en una rama en paralelo y 12 V en la fuente. ¿Qué puede estar mal?", "En paralelo cada rama debe tener el voltaje de la fuente", "La rama debería marcar 12 V."),
  ],
  cha=[
      ("En una fuente de 12 V se mide 8 V en un receptor de un circuito en serie con otro. ¿Cuántos volts debería haber en el otro? Responde con el número.", "4", "12 − 8 = 4.", "12-8"),
      ("Una limitación de medir una sola vez con un instrumento es ¿cuál? A) Los instrumentos tienen error y conviene repetir; B) La corriente desaparece.", "A", "Repetir permite comprobar el valor."),
  ],
  context=[("En una casa de ejemplo, un alargador reparte la fuente de 220 V a dos artefactos conectados en paralelo. ¿Qué voltaje recibe cada uno?", "220 V", "En paralelo cada artefacto recibe el voltaje de la fuente.")],
  selfcheck=[("¿Qué se reparte en un circuito en serie?", "El voltaje", "La corriente es la misma."), ("¿Qué se reparte en paralelo?", "La corriente", "El voltaje es el mismo."), ("¿Cómo se mide la corriente?", "Con un amperímetro", "Se mide en amperes.")],
  open_task=task("Con estos datos de ejemplo completa dos tablas y escribe una conclusión: circuito 1 en serie con una fuente de 12 V y receptores de 3 V, 4 V y un tercero desconocido; circuito 2 en paralelo con ramas de 1 A, 2 A y 4 A. Calcula el voltaje que falta y la corriente total.", "Circuito 1: 12 − 3 − 4 = 5 V. Circuito 2: 1 + 2 + 4 = 7 A. Conclusión: en serie se reparte el voltaje; en paralelo, la corriente. Limitación: son datos de ejemplo de un solo montaje.", ["dos cálculos correctos", "conclusión que usa ambas reglas", "una limitación"], ["tablas y frase"], ["sumar corrientes en serie", "restar voltajes en paralelo"], "Pregunta qué cambia si se agrega una rama."),
  reinforce="Escribe qué se mantiene igual en un circuito en serie.",
  extend="Explica por qué una medición se debe repetir.")

L(OA10, 3,
  materials="Este cuaderno y lápiz. Los esquemas se describen con palabras.",
  use="Aprenderé a construir y contrastar modelos de circuitos en serie y en paralelo y del circuito de una casa. Sirve para predecir qué pasa si un receptor falla o se agrega otro.",
  prior=["Sé las reglas de voltaje y corriente en serie y en paralelo.", "Sé que un modelo simplifica."],
  explain=[
      "Un modelo comparativo usa analogías. Para el circuito en serie se puede pensar en una fila de personas que pasa por un solo pasillo, con puertas una tras otra: si una puerta se cierra, nadie pasa. Para el circuito en paralelo, en varios pasillos separados: si uno se cierra, los demás siguen funcionando. Con el modelo se predice: en serie, si un receptor se quema, todos se apagan; en paralelo, solo se apaga ese.",
      "El circuito domiciliario de Chile entrega unos 220 V. Los artefactos se conectan en paralelo, para que cada uno reciba 220 V y funcione de forma independiente. El tablero tiene protecciones: el automático corta la corriente si es excesiva por sobrecarga o cortocircuito, el diferencial corta si detecta una fuga de corriente por una persona, y el cable a tierra desvía las fugas al suelo.",
      "Contrastar un modelo es compararlo con la evidencia. Si en una casa se apaga una ampolleta y las demás siguen, el modelo en paralelo lo explica. Todo modelo tiene límites: la analogía del pasillo no muestra voltaje ni resistencia. Un buen informe dice qué predice el modelo y qué no explica.",
  ],
  vocab=[("circuito domiciliario", "circuito eléctrico de una casa, conectado en paralelo"), ("automático", "protección que corta la corriente si es excesiva"), ("diferencial", "protección que corta si detecta fuga de corriente"), ("cable a tierra", "cable que lleva las fugas de corriente al suelo"), ("sobrecarga", "corriente mayor a la que el cable soporta")],
  worked=[
      ("Predicción en serie", "Tres ampolletas están en serie y una se quema. ¿Qué pasa con las otras?", ["Con una ampolleta quemada el camino queda abierto.", "No circula corriente."], "Se apagan todas"),
      ("Predicción en paralelo", "Tres ampolletas en paralelo y una se quema. ¿Qué pasa con las otras?", ["Cada una tiene su rama.", "Las otras ramas siguen cerradas."], "Siguen encendidas"),
  ],
  mistakes=[
      ("Pensar que en una casa los artefactos están en serie.", "Si lo estuvieran, al apagar uno se apagarían todos.", "Recuerda que están en paralelo."),
      ("Creer que el automático y el diferencial hacen lo mismo.", "El automático corta por exceso de corriente; el diferencial por fugas.", "Distingue su función."),
  ],
  rec=[
      ("¿Cómo están conectados los artefactos de una casa: en serie o en paralelo?", "En paralelo", "Así cada uno recibe 220 V y funciona por separado."),
      ("¿Qué voltaje entrega la red domiciliaria en Chile, aproximadamente: 220 V o 12 V?", "220 V", "Es el voltaje de las casas."),
      ("Verdadero o falso: el cable a tierra desvía fugas de corriente al suelo.", "Verdadero", "Protege a las personas."),
  ],
  und=[
      ("¿Qué protección corta la corriente si es excesiva? A) El automático; B) El cable a tierra.", "A", "El automático protege contra sobrecarga y cortocircuito."),
      ("En serie, si se quema una ampolleta, ¿qué pasa? A) Se apagan todas; B) Siguen encendidas las demás.", "A", "El circuito queda abierto."),
      ("¿Por qué el modelo del pasillo tiene límites?", "No muestra voltaje ni resistencia", "Es una analogía cualitativa."),
  ],
  app=[
      ("Cuatro ampolletas de ejemplo están en paralelo y se queman dos. ¿Cuántas siguen encendidas?", "2", "Cada una funciona por separado."),
      ("Cuatro ampolletas de ejemplo están en serie y se quema una. ¿Cuántas siguen encendidas?", "0", "Se interrumpe el único camino."),
      ("Un enchufe de una casa entrega 220 V a una plancha y a una radio conectadas a la vez. ¿Cuántos volts recibe la radio? A) 220 V; B) 110 V.", "A", "En paralelo cada artefacto recibe el voltaje completo."),
  ],
  rea=[
      ("Alguien dice: «En mi casa se apagó la luz de la cocina y la del living sigue encendida, así que están en serie». ¿Qué falla tiene? A) Eso indica conexión en paralelo; B) No hay luces.", "A", "En serie, al apagar una se apagan todas."),
      ("Un cortocircuito produce una corriente muy alta. ¿Qué protección del tablero debería actuar?", "El automático", "Corta la corriente excesiva."),
  ],
  cha=[
      ("Una persona toca un artefacto con una fuga de corriente. ¿Qué protección debería cortar el suministro? A) El diferencial; B) El interruptor de la luz.", "A", "Detecta la fuga de corriente."),
      ("Un modelo de casa de ejemplo conecta todos los artefactos en serie. ¿Cuál es el principal problema? A) Si uno falla, todos se apagan; B) Reciben más voltaje.", "A", "Los artefactos no serían independientes."),
  ],
  context=[("Un liceo de ejemplo tiene 12 salas con luces en paralelo. Una sala se queda sin luz por una ampolleta quemada. ¿Cuántas salas siguen con luz?", "11", "Cada sala tiene su rama.", "12-1")],
  selfcheck=[("¿Cómo están conectados los artefactos de una casa?", "En paralelo", "Cada uno funciona por separado."), ("¿Para qué sirve el diferencial?", "Para cortar si hay una fuga de corriente", "Protege a las personas."), ("¿Qué pasa en serie si falla un receptor?", "Se apagan todos", "El camino queda abierto.")],
  open_task=task("Dibuja dos modelos: tres ampolletas en serie y tres en paralelo conectadas a una pila. Debajo de cada uno escribe qué pasa si una ampolleta se quema y por qué. Agrega una frase sobre por qué las casas usan conexión en paralelo y una protección del tablero.", "Serie: si una se quema, se apagan todas, porque hay un solo camino. Paralelo: si una se quema, las otras siguen, porque cada una tiene su rama. Las casas usan paralelo para que cada artefacto funcione por separado con 220 V. Protección: el automático corta si hay exceso de corriente.", ["dos dibujos correctos", "dos predicciones", "motivo y protección"], ["dibujos y frases"], ["decir que en paralelo se apagan todas", "olvidar la protección"], "Pregunta qué limita al modelo del pasillo."),
  reinforce="Escribe qué pasa en un circuito en paralelo si se quema una ampolleta.",
  extend="Explica con tus palabras para qué sirve el cable a tierra.")

L(OA10, 4,
  materials="Este cuaderno, lápiz y calculadora si quieres. Los datos son de ejemplo.",
  use="Aprenderé la relación entre voltaje, corriente y resistencia (V = I × R), la potencia (P = V × I) y la resistencia total en serie y en paralelo. Sirve para calcular valores de un circuito.",
  prior=["Sé las reglas de serie y paralelo.", "Sé multiplicar y dividir números enteros."],
  explain=[
      "La relación entre las tres magnitudes se llama ley de Ohm: V = I × R. Si el voltaje es 12 V y la resistencia 4 Ω, la corriente es I = V ÷ R = 12 ÷ 4 = 3 A. Si la resistencia aumenta y el voltaje es el mismo, la corriente disminuye. La potencia eléctrica (P) es la rapidez con que se transforma energía: P = V × I. Con 12 V y 3 A, P = 36 W (watts).",
      "Para varias resistencias, la resistencia total depende de la conexión. En serie se suman: R total = R1 + R2. Por ejemplo, 4 Ω y 6 Ω dan 10 Ω. En paralelo la resistencia total es menor que cualquiera de las ramas. Para dos resistencias iguales, R total = R ÷ 2; para 6 Ω y 3 Ω, R total = (6 × 3) ÷ (6 + 3) = 2 Ω.",
      "Estas relaciones se usan para predecir y comparar. En serie, al agregar receptores, la resistencia total aumenta y la corriente baja. En paralelo, al agregar ramas, la resistencia total baja y la corriente total sube. Una limitación es que los materiales reales cambian su resistencia con la temperatura; los valores de esta clase son idealizados.",
  ],
  vocab=[("ley de Ohm", "relación V = I × R entre voltaje, corriente y resistencia"), ("potencia eléctrica (W)", "rapidez con que se transforma la energía eléctrica; P = V × I"), ("watt (W)", "unidad de potencia"), ("resistencia total", "resistencia equivalente de todo el circuito"), ("idealizado", "simplificado, sin considerar todos los efectos reales")],
  worked=[
      ("Corriente con la ley de Ohm", "Una fuente de 12 V alimenta una resistencia de 4 Ω. ¿Cuál es la corriente?", ["I = V ÷ R.", "12 ÷ 4 = 3."], "3 A"),
      ("Resistencia en paralelo", "Dos resistencias de 6 Ω y 3 Ω están en paralelo. ¿Cuál es la resistencia total?", ["Uso (6 × 3) ÷ (6 + 3).", "18 ÷ 9 = 2."], "2 Ω"),
  ],
  mistakes=[
      ("Sumar las resistencias en paralelo.", "En paralelo la resistencia total es menor que cualquier rama.", "Usa la regla del producto sobre la suma."),
      ("Confundir potencia con energía.", "La potencia es una rapidez; la energía es la potencia por el tiempo.", "Recuerda las unidades W y Wh."),
  ],
  rec=[
      ("¿Qué fórmula relaciona voltaje, corriente y resistencia: V = I × R o V = I + R?", "V = I × R", "Es la ley de Ohm."),
      ("¿En qué unidad se mide la potencia: en watts o en ohms?", "En watts", "El watt (W) mide la potencia."),
      ("Verdadero o falso: en serie las resistencias se suman.", "Verdadero", "R total = R1 + R2."),
  ],
  und=[
      ("Si el voltaje es el mismo y la resistencia aumenta, ¿qué pasa con la corriente? A) Disminuye; B) Aumenta.", "A", "I = V ÷ R: dividir por un número mayor da un valor menor."),
      ("¿Qué pasa con la resistencia total al agregar una rama en paralelo? A) Disminuye; B) Aumenta.", "A", "Hay un nuevo camino para la corriente."),
      ("¿Qué mide P = V × I?", "La potencia eléctrica", "Es la rapidez con que se transforma la energía."),
  ],
  app=[
      arith("Una fuente de 24 V alimenta una resistencia de 8 Ω. ¿Cuántos amperes circulan?", "24//8", "I = V ÷ R."),
      arith("Un artefacto de 220 V tiene una corriente de 5 A. ¿Cuántos watts de potencia tiene?", "220*5", "P = V × I."),
      arith("Dos resistencias de 5 Ω y 7 Ω están en serie. ¿Cuántos ohms es la resistencia total?", "5+7", "En serie se suman."),
  ],
  rea=[
      ("Alguien calcula 4 Ω y 4 Ω en paralelo y obtiene 8 Ω. ¿Qué error comete? A) Los sumó; en paralelo la total es menor que 4 Ω; B) Usó ohms.", "A", "Dos iguales dan la mitad: 2 Ω."),
      ("Dos resistencias distintas se conectan a la misma fuente de 10 V: una de 5 Ω y otra de 10 Ω. ¿Cuál tiene menor corriente? Escribe el valor de la resistencia.", "10 Ω", "I = V ÷ R: con 10 Ω circulan 1 A y con 5 Ω circulan 2 A."),
  ],
  cha=[
      arith("Dos resistencias de 12 Ω y 4 Ω están en paralelo. ¿Cuál es la resistencia total en ohms?", "(12*4)//(12+4)", "Se aplica producto sobre suma."),
      arith("Una fuente de 12 V alimenta dos resistencias de 6 Ω cada una conectadas en paralelo. ¿Cuántos amperes totales entrega la fuente?", "12//(6//2)", "La resistencia total de dos iguales es la mitad, y luego I = V ÷ R total."),
  ],
  context=[arith("Una plancha de ejemplo de 220 V tiene una corriente de 10 A. ¿Cuántos watts consume?", "220*10", "P = V × I.")],
  selfcheck=[("¿Qué dice la ley de Ohm?", "V = I × R", "Relaciona voltaje, corriente y resistencia."), ("¿Cómo se calcula la potencia?", "P = V × I", "Se mide en watts."), ("¿Cómo cambia la resistencia al agregar ramas en paralelo?", "Disminuye", "Hay más caminos.")],
  open_task=task("Calcula con estos datos de ejemplo: fuente de 18 V; resistencias de 6 Ω y 3 Ω. (a) Si están en serie, resistencia total y corriente. (b) Si están en paralelo, resistencia total y corriente total. Compara cuál conexión entrega más corriente y explica por qué.", "(a) Serie: 6 + 3 = 9 Ω; I = 18 ÷ 9 = 2 A. (b) Paralelo: (6 × 3) ÷ 9 = 2 Ω; I = 18 ÷ 2 = 9 A. En paralelo hay más corriente porque la resistencia total es menor.", ["dos resistencias totales correctas", "dos corrientes correctas", "explica la diferencia"], ["cuatro cálculos y una frase"], ["sumar en paralelo", "dividir al revés"], "Pregunta qué pasaría con 24 V."),
  reinforce="Calcula la corriente de una resistencia de 10 Ω con 20 V.",
  extend="Explica por qué en paralelo la resistencia total es menor que cada rama.")

L(OA10, 5,
  materials="Este cuaderno, lápiz y calculadora si quieres. Los datos son de ejemplo y las tarifas son inventadas.",
  use="Aprenderé a explicar el consumo de energía eléctrica (E = P × t), a leer una cuenta y a comparar la eficiencia de artefactos. Sirve para entender el gasto de energía en una casa y cómo reducirlo.",
  prior=["Sé que P = V × I.", "Sé multiplicar y calcular porcentajes."],
  explain=[
      "La energía eléctrica consumida se calcula con E = P × t. Si P está en kilowatts (kW) y t en horas (h), E queda en kilowatt-hora (kWh), la unidad de la cuenta de luz. Un artefacto de 2 kW que funciona 3 horas consume 2 × 3 = 6 kWh. Para pasar de watts a kilowatts se divide por 1.000: 1.000 W = 1 kW. Con el valor de ejemplo de $200 por kWh, 6 kWh cuestan $1.200.",
      "La eficiencia energética compara la energía útil con la energía total que consume un artefacto. Eficiencia (%) = energía útil ÷ energía total × 100. Una ampolleta incandescente transforma gran parte de la energía en calor y poca en luz; una ampolleta LED transforma más energía en luz. Para una luz parecida, una LED de ejemplo usa 10 W y una incandescente 60 W. Las etiquetas de eficiencia energética ayudan a elegir.",
      "Con estos datos se explica un patrón: a mayor potencia o mayor tiempo, mayor consumo. Para ahorrar se reduce el tiempo de uso, se apagan los artefactos que no se usan y se eligen artefactos más eficientes. También hay que considerar una limitación: los valores de potencia de la etiqueta son nominales y el consumo real puede variar.",
  ],
  vocab=[("kilowatt-hora (kWh)", "unidad de energía: 1 kW durante 1 hora"), ("eficiencia energética", "relación entre la energía útil y la energía total consumida"), ("potencia nominal", "potencia indicada por el fabricante"), ("consumo", "energía que usa un artefacto durante un tiempo"), ("etiqueta de eficiencia", "información que clasifica a los artefactos según su eficiencia")],
  worked=[
      ("Energía consumida", "Un calefactor de 2 kW funciona 4 horas. ¿Cuántos kWh consume?", ["E = P × t.", "2 × 4 = 8."], "8 kWh"),
      ("Pasar a kilowatts", "Un artefacto de 2.000 W, ¿cuántos kW es?", ["Divido por 1.000.", "2.000 ÷ 1.000 = 2."], "2 kW"),
  ],
  mistakes=[
      ("Confundir kW con kWh.", "El kW mide potencia y el kWh mide energía.", "Recuerda que kWh = kW × h."),
      ("Pensar que una ampolleta de menor potencia siempre da menos luz.", "Una LED de 10 W puede dar tanta luz como una incandescente de 60 W.", "Compara luz útil y potencia."),
  ],
  rec=[
      ("¿La unidad de la cuenta de luz es el kWh o el watt?", "El kWh", "Mide la energía consumida."),
      ("¿Cuántos watts son 1 kilowatt?", "1.000", "El prefijo kilo significa mil."),
      ("Verdadero o falso: una LED transforma más energía en luz que una incandescente.", "Verdadero", "Por eso es más eficiente."),
  ],
  und=[
      ("¿Qué fórmula da la energía consumida? A) E = P × t; B) E = P + t.", "A", "Es potencia por tiempo."),
      ("¿Qué indica una etiqueta de eficiencia energética? A) Cuán eficiente es el artefacto; B) El color del artefacto.", "A", "Ayuda a comparar consumo."),
      ("¿Por qué es una limitación que la potencia sea nominal?", "Porque el consumo real puede variar", "El fabricante da un valor de referencia."),
  ],
  app=[
      arith("Un artefacto de 3 kW funciona 2 horas. ¿Cuántos kWh consume?", "3*2", "E = P × t."),
      arith("Con una tarifa de ejemplo de $200 por kWh, ¿cuánto cuesta un consumo de 15 kWh?", "200*15", "Se multiplica el consumo por la tarifa."),
      arith("Una ampolleta incandescente de 100 W y una LED de 20 W se usan 10 horas cada una. ¿Cuántos Wh más consume la incandescente?", "100*10-20*10", "Se calcula la energía de cada una y se resta."),
  ],
  rea=[
      ("Alguien dice: «Si dejo el televisor de 100 W encendido todo el día, no gasta nada porque es de baja potencia». ¿Qué corrección haces? A) Aunque la potencia sea baja, el tiempo largo aumenta el consumo; B) Un artefacto de baja potencia no consume.", "A", "E = P × t."),
      ("Una persona cambia 5 ampolletas de 60 W por LED de 10 W. Si cada una se usa 4 horas al día, ¿ahorra energía? Responde Sí o No.", "Sí", "Cada ampolleta pasa de 240 Wh a 40 Wh al día."),
  ],
  cha=[
      arith("¿Cuántos Wh por día ahorra el cambio de las 5 ampolletas de 60 W por LED de 10 W usadas 4 horas al día?", "5*(60-10)*4", "Se calcula el ahorro de potencia por las horas y las ampolletas."),
      arith("Una estufa de ejemplo recibe 500 unidades de energía eléctrica y entrega 450 como calor útil. ¿Cuál es su eficiencia?", "450*100//500", "Eficiencia = energía útil ÷ energía total × 100.", " %"),
  ],
  context=[arith("Una familia de ejemplo usa una estufa de 2 kW durante 5 horas en un día. Con una tarifa de ejemplo de $200 por kWh, ¿cuánto cuesta ese uso?", "2*5*200", "Se calcula la energía en kWh y se multiplica por la tarifa.")],
  selfcheck=[("¿Cómo se calcula la energía consumida?", "Multiplicando la potencia por el tiempo", "E = P × t."), ("¿Qué mide el kWh?", "Energía", "Es la unidad de la cuenta de luz."), ("¿Cómo se puede ahorrar energía?", "Reduciendo el uso y usando artefactos eficientes", "Se disminuye P o t.")],
  open_task=task("Compara dos opciones con datos de ejemplo: una ampolleta incandescente de 100 W y una LED de 20 W, ambas usadas 5 horas al día durante 30 días. Calcula el consumo de cada una en Wh por día y en kWh por mes, el ahorro y el costo ahorrado con una tarifa de $200 por kWh. Termina con una recomendación y una limitación.", "Incandescente: 100 × 5 = 500 Wh por día; 500 × 30 = 15.000 Wh = 15 kWh por mes. LED: 20 × 5 = 100 Wh por día; 3.000 Wh = 3 kWh por mes. Ahorro: 12 kWh. Costo ahorrado: 12 × $200 = $2.400. Recomendación: elegir LED. Limitación: son potencias nominales.", ["consumos correctos", "ahorro y costo", "recomendación y limitación"], ["cálculos y frases"], ["confundir W con kWh", "olvidar la limitación"], "Pregunta qué pasaría si se usara el doble de tiempo."),
  reinforce="Calcula la energía de un artefacto de 4 kW que funciona 3 horas.",
  extend="Explica por qué una ampolleta LED es más eficiente que una incandescente.")

L(OA10, 6,
  materials="Este cuaderno y lápiz. NUNCA toques enchufes, cables ni tablero eléctrico, y nunca toques a una persona que recibe una descarga. Avisa de inmediato a una persona adulta.",
  use="Aprenderé a evaluar riesgos de la electricidad en una casa, las protecciones y los límites de los modelos de circuitos. Sirve para tomar decisiones seguras y reconocer qué hacer ante un problema.",
  prior=["Sé cómo se conectan los artefactos de una casa.", "Sé calcular corriente con P = V × I."],
  explain=[
      "La electricidad de la red (220 V) es peligrosa. Los riesgos más frecuentes son: sobrecarga por conectar muchos artefactos de gran potencia en un mismo enchufe o alargador, cables dañados o pelados, humedad cerca de enchufes y manos mojadas. La sobrecarga calienta los cables y puede provocar incendios. Una descarga puede causar quemaduras o parar el corazón.",
      "Las soluciones son: respetar los límites de corriente (un alargador de ejemplo soporta hasta 10 A), usar artefactos con enchufe de tres patas conectados a tierra, no usar aparatos con las manos mojadas, cambiar cables dañados con un técnico y mantener el tablero con automático y diferencial. Para calcular la corriente se usa I = P ÷ V: un artefacto de 1.100 W en 220 V usa 1.100 ÷ 220 = 5 A.",
      "Evaluar incluye declarar los límites de lo que se sabe. Los modelos de circuitos son idealizados, no incluyen todas las pérdidas y los valores de la etiqueta son nominales. Si ocurre un accidente eléctrico, no se toca a la persona: se pide ayuda de inmediato a una persona adulta y a los servicios de emergencia, y solo un adulto corta la corriente desde el tablero si puede hacerlo con seguridad.",
  ],
  vocab=[("cortocircuito", "unión directa de dos puntos del circuito con muy poca resistencia"), ("alargador", "cable con enchufes para conectar varios artefactos"), ("límite de corriente", "corriente máxima que soporta un cable o enchufe"), ("descarga eléctrica", "paso de corriente por el cuerpo"), ("emergencia eléctrica", "situación de riesgo por electricidad que exige pedir ayuda adulta")],
  worked=[
      ("Corriente de un artefacto", "Un artefacto de 1.100 W se conecta a 220 V. ¿Qué corriente usa?", ["I = P ÷ V.", "1.100 ÷ 220 = 5."], "5 A"),
      ("Sobrecarga", "A un alargador que soporta 10 A se conectan artefactos de 5 A y 7 A. ¿Hay sobrecarga?", ["Sumo: 5 + 7 = 12 A.", "12 A supera los 10 A."], "Sí, hay sobrecarga"),
  ],
  mistakes=[
      ("Conectar muchos artefactos potentes en un solo alargador.", "La corriente suma y puede superar el límite.", "Calcula la corriente total."),
      ("Intentar rescatar a una persona que recibe una descarga tocándola.", "También recibirías la descarga.", "Pide ayuda a una persona adulta y a los servicios de emergencia."),
  ],
  rec=[
      ("¿Qué riesgo produce conectar demasiados artefactos de gran potencia en un alargador: sobrecarga o ahorro?", "Sobrecarga", "La corriente supera el límite del cable."),
      ("Verdadero o falso: puedes usar un artefacto eléctrico con las manos mojadas.", "Falso", "El agua aumenta el riesgo de descarga."),
      ("Si ves a alguien recibir una descarga, ¿qué haces primero: tocarlo o pedir ayuda a una persona adulta?", "Pedir ayuda a una persona adulta", "Tocarlo puede hacerte recibir la descarga."),
  ],
  und=[
      ("¿Para qué sirve la conexión a tierra? A) Para desviar fugas de corriente al suelo; B) Para aumentar el voltaje.", "A", "Protege a las personas."),
      ("¿Por qué un cable pelado es peligroso? A) Deja partes con corriente al alcance de las personas; B) Consume menos energía.", "A", "Puede causar descargas y cortocircuitos."),
      ("¿Qué protege contra una sobrecarga: el automático o el cable a tierra?", "El automático", "Corta si la corriente es excesiva."),
  ],
  app=[
      arith("Un secador de 2.200 W se conecta a 220 V. ¿Cuántos amperes usa?", "2200//220", "I = P ÷ V."),
      arith("A un alargador que soporta 10 A se conectan artefactos de 2 A, 3 A y 4 A. ¿Cuántos amperes suman?", "2+3+4", "Se suman las corrientes."),
      arith("Con los mismos artefactos (2 A, 3 A y 4 A), ¿cuántos amperes de margen quedan antes de llegar al límite de 10 A?", "10-9", "Se resta la corriente usada al límite."),
  ],
  rea=[
      ("Una persona conecta una estufa de 2.200 W y un hervidor de 2.200 W a un mismo alargador de 10 A. ¿Qué ocurre? A) La corriente total supera el límite y hay riesgo de sobrecarga; B) Todo funciona de forma segura.", "A", "Cada artefacto usa 10 A, y juntos 20 A."),
      ("Un compañero dice: «Si el automático salta, lo mejor es subirlo con la mano para que no moleste». ¿Qué corrección haces?", "Es una señal de sobrecarga o falla, y debe revisarlo una persona adulta o un técnico", "El automático protege el circuito."),
  ],
  cha=[
      ("Dos soluciones para la sobrecarga: S1 reducir los artefactos en el mismo enchufe; S2 envolver el alargador con cinta aislante para que no se vea el calor. ¿Cuál reduce realmente el riesgo? Escribe S1 o S2.", "S1", "Disminuye la corriente total."),
      ("Un informe de ejemplo dice que su modelo de circuito explica todo sobre una casa. ¿Qué límite debería declarar? A) Que es idealizado y no incluye pérdidas ni todos los efectos reales; B) Que no usa números.", "A", "Todo modelo simplifica."),
  ],
  context=[("En una casa de ejemplo se siente olor a quemado cerca de un enchufe con muchos aparatos conectados. ¿Qué haces? A) Avisar de inmediato a una persona adulta y no tocar el enchufe; B) Desenchufar todo con las manos mojadas.", "A", "El riesgo es de incendio o descarga.")],
  selfcheck=[("¿Qué causa una sobrecarga?", "Conectar artefactos cuya corriente total supera el límite", "Calienta los cables."), ("¿Cómo se calcula la corriente de un artefacto?", "Dividiendo la potencia por el voltaje", "I = P ÷ V."), ("¿Qué haces ante una descarga eléctrica?", "Pedir ayuda a una persona adulta y no tocar a la persona", "Tocarla es peligroso.")],
  open_task=task("Evalúa este caso de ejemplo: en un alargador de 10 A se conectan una estufa de 1.100 W, un hervidor de 1.100 W y un secador de 2.200 W a 220 V. Calcula la corriente de cada artefacto y la total, decide si hay sobrecarga, propone una solución y escribe una conducta segura si algo sale mal.", "Estufa: 5 A. Hervidor: 5 A. Secador: 10 A. Total: 20 A, que supera los 10 A: hay sobrecarga. Solución: no conectar los tres juntos y usar enchufes distintos. Conducta segura: si hay olor a quemado, no tocar y avisar a una persona adulta.", ["tres corrientes y total correctos", "decisión sobre sobrecarga", "solución y conducta segura"], ["cálculos y frases"], ["no sumar las corrientes", "proponer una solución peligrosa"], "Pregunta qué cambiaría con un alargador de 20 A."),
  reinforce="Escribe una conducta segura al usar artefactos eléctricos en casa.",
  extend="Explica por qué un modelo idealizado de circuito necesita límites para decidir con seguridad.")

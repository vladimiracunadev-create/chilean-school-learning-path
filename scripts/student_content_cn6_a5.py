"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 09 (transformaciones de la energía) y OA 10 (flujo del calor)."""
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


OA9, OA10 = "CN06 OA 09", "CN06 OA 10"

# ---------------------------------------------------------------- OA 09
L(OA9, 1,
  materials="Este cuaderno, lápiz y una pelota blanda de goma o de tenis. Opcional: una regla o una huincha de medir. Los datos están escritos en los ejercicios.",
  use="Aprenderé que la energía se transforma de una forma a otra y a separar lo observado de lo supuesto. Sirve para explicar qué pasa cuando una pelota rebota o frotas las manos.",
  prior=["Conozco formas de energía: luminosa, térmica, cinética, eléctrica y química.", "Sé que una observación se mide o se cuenta."],
  explain=[
      "La energía no se ve, pero se reconoce por lo que produce. Cuando algo cambia, la energía se transforma de una forma a otra. Si frotas tus manos, la energía del movimiento (cinética) se transforma en calor (energía térmica) y notas que se entibian. Una linterna transforma la energía química de la pila en energía eléctrica, y luego en luz y un poco de calor.",
      "Una pelota levantada tiene energía por su altura. Al soltarla, esa energía se transforma en movimiento mientras cae. Cuando choca con el suelo, parte se transforma en sonido y en calor, y por eso rebota menos alto cada vez. En cada transformación una parte útil se puede convertir en calor que se disipa y no vuelve a ser útil.",
      "Para investigar se separa lo que se observa de lo que se supone. Una observación es «la pelota soltada desde 100 cm rebotó hasta 60 cm». Una interpretación es «la pelota se cansó». Solo la primera es evidencia; la segunda es una manera de hablar que no explica con datos.",
  ],
  vocab=[("transformación de energía", "paso de una forma de energía a otra"), ("energía cinética", "energía del movimiento"), ("energía térmica", "energía del calor"), ("disiparse", "repartirse como calor y dejar de ser útil"), ("rebote", "movimiento hacia arriba tras chocar con una superficie")],
  worked=[
      ("Nombrar la transformación", "Una persona frota sus manos y siente calor. ¿Qué energía se transforma en qué?", ["Frotar es movimiento: energía cinética.", "Las manos se entibian: energía térmica.", "Escribo el cambio con una flecha."], "Energía cinética → energía térmica"),
      ("Observación o interpretación", "Dos frases: (1) «La pelota soltada desde 100 cm rebotó hasta 60 cm». (2) «La pelota se cansó». ¿Cuál es la observación?", ["Pregunto qué frase se midió.", "La frase 1 tiene medidas.", "La frase 2 es una forma de hablar."], "La frase 1"),
  ],
  mistakes=[
      ("Decir que la energía «se gasta» y desaparece.", "La energía se transforma; parte se dispersa como calor.", "Nombra en qué forma se transformó."),
      ("Anotar «la pelota se cansó» como observación.", "El cansancio no se mide en una pelota.", "Anota alturas medidas."),
  ],
  rec=[
      ("Al frotar las manos, ¿se producen calor o hielo?", "Calor", "El movimiento se transforma en energía térmica."),
      ("La energía del movimiento se llama energía ______. Completa con «cinética» o «lumínica».", "Cinética", "Es la energía del movimiento."),
      ("¿La pila de una linterna guarda energía química o energía sonora?", "Química", "La pila guarda energía química."),
  ],
  und=[
      ("¿Cuál es una interpretación? A) La pelota rebotó hasta 60 cm. B) La pelota se cansó.", "B", "No se mide."),
      ("En una linterna encendida, ¿en qué dos formas termina la energía de la pila?", "En luz y calor", "La ampolleta da luz y se entibia."),
      ("¿Por qué la pelota rebota cada vez menos?", "Porque parte de su energía se transforma en sonido y calor", "No toda se mantiene en movimiento."),
  ],
  app=[
      arith("Una pelota se suelta desde 120 cm y rebota hasta 70 cm (datos de ejemplo). ¿Cuántos centímetros menos rebotó que su altura inicial?", "120-70", "Se resta la altura de rebote de la inicial."),
      arith("Una pelota de ejemplo rebota 5 veces. En cada rebote pierde 8 cm de altura. ¿Cuántos centímetros pierde en total?", "8*5", "Se multiplican la pérdida por los rebotes."),
      ("Escribe qué transformación ocurre en un ventilador de pilas: de energía eléctrica a ______. Elige cinética o química.", "Cinética", "Las aspas se mueven."),
  ],
  rea=[
      ("Una compañera dice: «La energía de la pelota desapareció». ¿Es correcta su afirmación? Responde Sí o No.", "No", "La energía se transformó en sonido y calor."),
      ("Otro estudiante mide solo un rebote y concluye que todas las pelotas rebotan 60 cm. ¿Qué error cometió?", "Generalizó desde una sola medición", "Una sola medida no representa a todas."),
  ],
  cha=[
      ("Datos de ejemplo: rebotes de una pelota: 70, 49 y 34 cm. ¿Cuántos cm menos rebotó en el tercero que en el primero?", "36", "70 − 34 = 36."),
      ("Marca la mejor observación. A) La pelota llegó a 49 cm en el segundo rebote. B) La pelota quedó agotada.", "A", "La A es una medida."),
  ],
  context=[("Dato de ejemplo. Un curso midió con una huincha que una pelota soltada desde 150 cm rebotó hasta 95 cm. ¿Cuántos centímetros menos subió?", "55", "150 − 95 = 55.")],
  selfcheck=[("¿Qué es una transformación de energía?", "El paso de una forma de energía a otra", "Por ejemplo, de movimiento a calor."), ("¿Qué pasa con la energía de una pelota que rebota?", "Se transforma en movimiento, sonido y calor", "Parte se disipa."), ("¿Cómo se reconoce una observación?", "Se mide o se cuenta", "Tiene datos medidos.")],
  open_task=task("Con una pelota, suéltala desde 100 cm sobre el suelo, marca hasta dónde sube en tres rebotes y anota las alturas. Si no tienes pelota, usa estos datos de ejemplo: 100 cm, rebotes de 62, 38 y 24 cm. Escribe tres observaciones con números, una interpretación y dos transformaciones de energía.", "Observaciones: primer rebote 62 cm; segundo 38; tercero 24. Interpretación: parte de la energía se transforma en sonido y calor. Transformaciones: cinética → térmica; química → cinética.", ["tres observaciones con números", "una interpretación rotulada", "dos transformaciones"], ["lista escrita"], ["poner «se cansó» como dato", "decir que la energía desaparece"], "Pregunta cuál rebote perdió más altura y cómo lo sabe."),
  reinforce="Escribe una transformación de energía que ocurra en tu casa.",
  extend="Explica por qué se dice que la energía se transforma y no desaparece.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Opcional: una pelota blanda y una huincha. Los datos están escritos en los ejercicios.",
  use="Aprenderé a plantear una pregunta y una predicción sobre transformaciones de energía. Sirve para organizar una investigación experimental.",
  prior=["Sé que la energía se transforma.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una pregunta comprobable nombra qué se cambia y qué se mide. Por ejemplo: «¿Cuánto sube una pelota en el primer rebote si se suelta desde 60 cm y desde 120 cm?». Aquí se cambia la altura de caída y se mide la altura del rebote. Las demás condiciones, como la pelota y el piso, se mantienen iguales.",
      "Una predicción lleva una razón basada en las transformaciones: «Desde más altura la pelota rebotará más alto, porque comienza con más energía por su altura». Se predice que la altura del rebote es menor que la altura inicial, porque parte de la energía se transforma en sonido y calor en el choque.",
      "Para comprobar se repite cada medición al menos tres veces y se calcula un promedio, porque una sola medida puede tener errores. Si el resultado no coincide, se corrige la idea y no el dato. Una predicción prudente usa «probablemente».",
  ],
  vocab=[("variable independiente", "lo que se cambia a propósito"), ("variable medida", "lo que se mide para ver el efecto"), ("condición constante", "lo que se mantiene igual"), ("promedio", "suma de datos dividida por la cantidad de datos"), ("error de medición", "diferencia entre el valor medido y el real")],
  worked=[
      ("Identificar variables", "En el experimento de soltar una pelota desde 60 cm y desde 120 cm, ¿qué se cambia y qué se mide?", ["Se cambia la altura de caída.", "Se mide la altura del rebote.", "La pelota y el piso quedan iguales."], "Se cambia la altura de caída y se mide la altura del rebote"),
      ("Promedio de tres medidas", "Tres rebotes desde 100 cm midieron 58, 60 y 62 cm. ¿Cuál es el promedio?", ["Sumo 58 + 60 + 62.", "Obtengo 180.", "Divido 180 entre 3."], "60 cm"),
  ],
  mistakes=[
      ("Cambiar la pelota y la altura a la vez.", "No se sabría cuál causó la diferencia.", "Cambia solo una condición."),
      ("Predecir que la pelota rebotará más alto que su altura inicial.", "Parte de la energía se transforma en sonido y calor.", "Predice que el rebote es menor."),
  ],
  rec=[
      ("En el experimento de caída, ¿se mide la altura del rebote o el color de la pelota?", "La altura del rebote", "Es el efecto que se mide."),
      ("¿Se repiten las mediciones para reducir errores: Sí o No?", "Sí", "Así el dato es más confiable."),
      ("¿La altura del rebote es mayor o menor que la inicial?", "Menor", "Parte de la energía se transforma."),
  ],
  und=[
      ("¿Cuál es la variable que se cambia en la pregunta «¿Cuánto rebota una pelota desde 60 y desde 120 cm?»", "La altura de caída", "Es la condición que se modifica."),
      ("¿Cuál es una predicción con razón? A) Desde más altura rebotará más, porque tiene más energía al comienzo. B) Rebotará más porque sí.", "A", "La A da una razón."),
      ("¿Por qué se mantiene la misma pelota?", "Para que solo cambie la altura", "Así la diferencia se atribuye a la altura."),
  ],
  app=[
      arith("Tres rebotes midieron 36, 39 y 45 cm. ¿Cuál es el promedio?", "(36+39+45)//3", "Se suman y se divide por 3."),
      arith("Una pelota de ejemplo cae desde 120 cm y rebota hasta 70 cm. ¿Cuántos centímetros de altura se perdieron?", "120-70", "Se restan las alturas."),
      ("Si desde 60 cm la pelota rebota 35 cm, ¿qué predices para 120 cm: que rebote más que 35 o menos que 35?", "Más que 35", "Con más energía inicial sube más."),
  ],
  rea=[
      ("Un grupo midió desde 60 cm y desde 120 cm con dos pelotas distintas. ¿Qué problema tiene el experimento?", "Cambian la altura y la pelota a la vez", "No se sabe cuál causó la diferencia."),
      ("Un estudiante dice: «Mi predicción falló, cambiaré el dato». ¿Es correcto? Responde Sí o No.", "No", "Se corrige la idea, no el dato."),
  ],
  cha=[
      ("Resultados de ejemplo: desde 60 cm, promedio de 36 cm; desde 120 cm, promedio de 72 cm. ¿Cuántas veces mayor es el rebote desde 120 cm?", "2", "72 ÷ 36 = 2."),
      ("Marca la mejor pregunta comprobable. A) ¿Cuántos cm rebota una pelota soltada desde 80 cm? B) ¿Cuál pelota es más simpática?", "A", "Se mide con una huincha."),
  ],
  context=[("Dato de ejemplo. Una pelota se soltó 3 veces desde 90 cm y rebotó 50, 52 y 54 cm. ¿Cuál es el promedio?", "52", "(50 + 52 + 54) ÷ 3 = 52.")],
  selfcheck=[("¿Qué se cambia y qué se mide en el experimento de la pelota?", "Se cambia la altura de caída y se mide la altura del rebote", "Las demás condiciones quedan iguales."), ("¿Por qué se calcula un promedio?", "Para reducir el efecto de errores", "Una medida sola puede fallar."), ("¿Por qué el rebote es menor que la caída?", "Porque parte de la energía se transforma en sonido y calor", "No toda se conserva como movimiento.")],
  open_task=task("Diseña un experimento para saber si la altura de caída cambia la altura del rebote. Escribe la pregunta, la predicción con razón, qué cambiarías, qué medirías, qué dejarías igual y cuántas veces repetirías. Usa los datos de ejemplo: caída desde 50 cm, rebotes 30, 32, 31; caída desde 100 cm, rebotes 62, 64, 63. Calcula el promedio de cada caída.", "Pregunta: ¿cambia la altura del rebote si cambia la altura de caída? Predicción: desde más altura rebotará más, porque tiene más energía. Cambio: altura. Medida: rebote. Igual: pelota y piso. Repeticiones: 3. Promedios: 31 y 63.", ["pregunta y predicción con razón", "variables bien identificadas", "promedios correctos"], ["plan escrito", "cálculos"], ["cambiar dos cosas a la vez", "olvidar repetir"], "Pregunta qué cambiaría si el piso fuera de alfombra."),
  reinforce="Calcula el promedio de 20, 22 y 24 cm.",
  extend="Explica por qué conviene repetir una medición al menos tres veces.")

L(OA9, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a representar con un diagrama cómo se transforma la energía en aparatos y seres vivos. Sirve para dar ejemplos y explicar cadenas de transformaciones.",
  prior=["Sé que la energía se transforma y que parte se disipa como calor.", "Sé que un modelo simplifica."],
  explain=[
      "Un diagrama de transformación usa flechas para mostrar cómo cambia la energía. Por ejemplo, en una linterna: energía química (pila) → energía eléctrica → luz + calor. En un ventilador a pilas: energía química → eléctrica → cinética (las aspas) + un poco de calor y sonido. En un panel solar: luz → energía eléctrica.",
      "También ocurre en los seres vivos. El alimento guarda energía química. Cuando corres, parte de esa energía se transforma en movimiento (cinética) y parte en calor, por eso sientes calor al hacer ejercicio. En la fotosíntesis, la luz se transforma en energía química guardada en el azúcar. Estos diagramas permiten dar ejemplos y explicar cadenas con varias etapas.",
      "El modelo tiene límites. Las flechas no muestran cuánta energía hay en cada paso ni que parte se disipa como calor aunque no sea el objetivo. Un buen diagrama indica qué forma de energía es la útil y cuál se pierde. El diagrama solo representa una situación y no todas las condiciones del mundo real.",
  ],
  vocab=[("diagrama", "dibujo que muestra pasos o relaciones"), ("energía útil", "energía que cumple la función que queremos"), ("energía disipada", "energía que se pierde como calor"), ("cadena de transformaciones", "serie de cambios de energía uno tras otro"), ("panel solar", "dispositivo que transforma luz en electricidad")],
  worked=[
      ("Armar la cadena", "Describe las transformaciones de una linterna. ¿Cuál es la energía útil?", ["La pila guarda energía química.", "Se transforma en energía eléctrica y luego en luz y calor.", "La energía útil es la luz."], "Química → eléctrica → luz (útil) + calor"),
      ("Cadena en un ser vivo", "Un niño come pan y luego salta. ¿Qué transformaciones ocurren?", ["El pan tiene energía química.", "El cuerpo la usa para el movimiento.", "Parte se transforma en calor."], "Química → cinética + calor"),
  ],
  mistakes=[
      ("Olvidar que siempre sale calor en los aparatos.", "Parte de la energía se disipa como calor.", "Agrega el calor al final del diagrama."),
      ("Escribir las flechas al revés.", "Las flechas muestran el sentido del cambio.", "Va de la energía de origen hacia la de destino."),
  ],
  rec=[
      ("En un panel solar, ¿la luz se transforma en energía eléctrica o sonora?", "Eléctrica", "El panel produce electricidad."),
      ("¿La pila guarda energía química o cinética?", "Química", "Se transforma en electricidad."),
      ("En una linterna, ¿cuál es la energía útil: la luz o el calor?", "La luz", "Es lo que buscamos."),
  ],
  und=[
      ("En un ventilador de pilas, ¿qué energía hace girar las aspas? A) Cinética que viene de la eléctrica. B) Sonora.", "A", "Las aspas se mueven."),
      ("Cuando corres, ¿qué dos formas de energía aparecen a partir de la energía del alimento?", "Cinética y térmica", "Te mueves y te acaloras."),
      ("¿Por qué se agrega «calor» a casi todos los diagramas?", "Porque siempre se disipa algo", "Parte de la energía se pierde como calor."),
  ],
  app=[
      ("Ordena la cadena de una tostadora: térmica, eléctrica.", "Eléctrica, térmica", "La electricidad se transforma en calor."),
      arith("Un diagrama de ejemplo muestra 100 unidades de energía eléctrica en una ampolleta: 20 se transforman en luz y el resto en calor. ¿Cuántas unidades son calor?", "100-20", "Se resta la luz del total."),
      ("¿Cuántas transformaciones hay en la cadena química → eléctrica → luz?", "2", "Hay un cambio de química a eléctrica y otro de eléctrica a luz."),
  ],
  rea=[
      ("Un compañero dibuja pila → luz y no pone nada más. ¿Qué paso falta?", "La energía eléctrica", "La pila produce electricidad antes de la luz."),
      ("Un estudiante dice que toda la energía de la pila sale como luz. ¿Es correcto? Responde Sí o No.", "No", "Una parte sale como calor."),
  ],
  cha=[
      ("Una radio a pilas pasa de energía química a eléctrica y luego a ______. Completa con sonora o térmica.", "Sonora", "El parlante produce sonido."),
      ("Un diagrama de ejemplo muestra 100 unidades en una olla eléctrica: 90 son calor útil y el resto sonido y luz. ¿Cuántas unidades se disipan fuera de lo útil?", "10", "100 − 90 = 10."),
  ],
  context=[("Dato de ejemplo. Una pila entrega 50 unidades de energía a un motor de juguete: 35 se transforman en movimiento y el resto en calor y sonido. ¿Cuántas unidades se pierden en calor y sonido?", "15", "50 − 35 = 15.")],
  selfcheck=[("¿Qué muestra un diagrama de transformación?", "Cómo cambia la energía de una forma a otra", "Se dibuja con flechas."), ("¿Qué es la energía útil?", "La que cumple la función que queremos", "Por ejemplo, la luz de una linterna."), ("¿Qué forma de energía se disipa casi siempre?", "El calor", "Aparece en casi todos los procesos.")],
  open_task=task("Dibuja el diagrama de transformaciones de una linterna y el de una persona que anda en bicicleta. Marca en cada uno la energía útil y la que se disipa. Escribe un límite de tus diagramas.", "Linterna: química → eléctrica → luz (útil) + calor. Bicicleta: química del alimento → cinética (útil) + calor. Límite: no muestran cuánta energía se pierde.", ["dos cadenas con flechas", "energía útil y disipada", "un límite"], ["dos diagramas"], ["olvidar el calor", "flechas al revés"], "Pregunta qué forma de energía quisiera aumentar en cada diagrama."),
  reinforce="Dibuja la cadena de transformaciones de un ventilador a pilas.",
  extend="Explica por qué en una bicicleta sientes calor aunque tu objetivo sea avanzar.")

L(OA9, 4,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a comparar aparatos según qué tanta energía se transforma en energía útil. Sirve para decidir qué aparato desperdicia menos energía.",
  prior=["Conozco energía útil y energía disipada.", "Sé calcular diferencias y porcentajes simples."],
  explain=[
      "No todos los aparatos transforman bien la energía. La eficiencia indica cuánta de la energía recibida se transforma en energía útil. Se calcula comparando la parte útil con el total. Por ejemplo, si una ampolleta recibe 100 unidades y entrega 10 unidades de luz, su eficiencia es 10 de 100, es decir, 10 %.",
      "Un criterio para comparar es la energía útil obtenida por cada 100 unidades que entran. Una ampolleta antigua de filamento convierte unas 10 unidades de luz y 90 de calor (datos de ejemplo). Una ampolleta LED convierte, por ejemplo, 40 unidades de luz y 60 de calor. Con el criterio, la LED es más eficiente porque aprovecha más energía en luz.",
      "Comparar con un criterio no dice todo. Un aparato eficiente puede costar más o durar menos. Además, estos datos son simulados para aprender; los reales dependen de cada modelo. Una conclusión sólida dice qué criterio se usó y qué se supone.",
  ],
  vocab=[("eficiencia", "parte de la energía que se transforma en energía útil"), ("porcentaje", "parte de cada 100"), ("criterio", "regla para comparar"), ("desperdicio", "energía que no se aprovecha"), ("dato simulado", "valor inventado para aprender, no medido")],
  worked=[
      ("Calcular la eficiencia", "Un aparato de ejemplo recibe 100 unidades y entrega 25 de energía útil. ¿Cuál es su eficiencia?", ["La parte útil es 25.", "El total es 100.", "25 de 100 es 25 %."], "25 %"),
      ("Comparar con el criterio", "Aparato A: 20 de energía útil de 100. Aparato B: 35 de energía útil de 100. ¿Cuál aprovecha mejor la energía?", ["Comparo 20 con 35.", "35 es mayor.", "El B aprovecha más."], "El aparato B"),
  ],
  mistakes=[
      ("Pensar que un aparato con eficiencia 100 % existe en la vida real.", "Siempre se disipa algo de calor.", "Usa datos reales y comprende que son aproximados."),
      ("Comparar aparatos con total de energía distinto sin ajustar.", "El criterio funciona mejor con el mismo total, por ejemplo 100 unidades.", "Calcula la parte útil por cada 100 unidades."),
  ],
  rec=[
      ("¿Un aparato con más energía útil por cada 100 unidades es más o menos eficiente?", "Más eficiente", "Aprovecha más energía."),
      ("El desperdicio es energía que ______. Completa con «se aprovecha» o «no se aprovecha».", "No se aprovecha", "Se disipa como calor."),
      ("Si una ampolleta recibe 100 y entrega 10 de luz, ¿cuánto se pierde en calor?", "90", "100 − 10 = 90."),
  ],
  und=[
      ("¿Qué indica la eficiencia?", "Cuánta energía se transforma en energía útil", "Compara lo útil con el total."),
      ("Ampolleta A: 10 de luz por 100. Ampolleta B: 40 de luz por 100. ¿Cuál es más eficiente?", "La B", "Aprovecha más energía en luz."),
      ("¿Por qué los datos del ejemplo no sirven para todas las ampolletas?", "Porque son simulados", "Los reales dependen de cada modelo."),
  ],
  app=[
      arith("Una ampolleta recibe 100 unidades y entrega 15 de luz. ¿Cuántas unidades se disipan como calor?", "100-15", "Se resta la luz del total."),
      arith("Una ampolleta de ejemplo recibe 200 unidades y entrega 80 de luz. ¿Cuántas unidades de calor son?", "200-80", "Se resta la parte útil."),
      arith("Si una ampolleta tiene 20 % de eficiencia y recibe 300 unidades, ¿cuántas unidades se transforman en luz?", "300*20//100", "El 20 % de 300 se calcula multiplicando y dividiendo por 100."),
  ],
  rea=[
      ("Un aparato A entrega 30 de 100 y un aparato B entrega 60 de 200. ¿Tienen la misma eficiencia? Responde Sí o No.", "Sí", "Ambos aprovechan 30 de cada 100."),
      ("¿Existe en la vida real un aparato que transforme el 100 % de la energía en energía útil? Responde Sí o No.", "No", "Siempre se disipa algo de calor."),
  ],
  cha=[
      ("Datos de ejemplo: LED 40 de 100; incandescente 10 de 100. ¿Cuántas veces más luz entrega la LED por cada 100 unidades?", "4", "40 ÷ 10 = 4."),
      ("Marca la mejor conclusión. A) Con estos datos simulados, la LED aprovecha más la energía. B) La LED siempre es mejor en todo.", "A", "La B afirma más de lo que prueba el criterio."),
  ],
  context=[("Dato de ejemplo. Una escuela cambia ampolletas antiguas por LED. Cada antigua desperdicia 90 unidades de cada 100 y la LED desperdicia 60. ¿Cuántas unidades menos desperdicia cada cambio?", "30", "90 − 60 = 30.")],
  selfcheck=[("¿Qué es la eficiencia?", "La parte de la energía que se transforma en energía útil", "Se compara con el total."), ("¿Qué criterio se usó para comparar ampolletas?", "La energía útil por cada 100 unidades", "Así se compara el mismo total."), ("¿Qué límite tiene la comparación?", "Los datos son simulados y hay otras variables como el costo", "No dice todo.")],
  open_task=task("Compara tres aparatos con datos de ejemplo por cada 100 unidades de energía recibida: ampolleta antigua, 10 de luz; ampolleta LED, 40 de luz; motor de juguete, 60 de movimiento. Calcula cuánto se disipa en cada uno, ordénalos de más a menos eficiente y escribe un límite.", "Disipa: 90, 60 y 40. Orden: motor, LED, antigua. Límite: los datos son simulados y no incluyen el costo.", ["tres cálculos correctos", "orden correcto", "un límite"], ["tabla con cálculos"], ["ordenar al revés", "olvidar el límite"], "Pregunta qué otro criterio, además de la eficiencia, usaría para elegir."),
  reinforce="Calcula cuánta energía se disipa si una ampolleta entrega 25 de luz por cada 100.",
  extend="Explica por qué un aparato eficiente ayuda a gastar menos energía.")

L(OA9, 5,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a comunicar conclusiones sobre las transformaciones de energía con evidencia y límites. Sirve para dar ejemplos y explicar que la energía se conserva.",
  prior=["Conozco las transformaciones de energía.", "Sé que parte de la energía se disipa."],
  explain=[
      "Una regla importante de la ciencia dice que la energía no se crea ni se destruye: solo se transforma. Eso significa que, al sumar toda la energía de un proceso, el total no cambia aunque parte se convierta en calor. Por ejemplo, una pelota que cae desde cierta altura tiene al comienzo 100 unidades (datos de ejemplo). Al rebotar, 60 están en el movimiento hacia arriba y 40 se transformaron en sonido y calor. 60 + 40 = 100, el total se conserva.",
      "Al comunicar conclusiones se entregan datos y límites. Una buena conclusión dice qué se midió, qué resultados se obtuvieron y qué se interpretó. También dice qué no se pudo comprobar, por ejemplo que el calor del choque es muy pequeño y es difícil medirlo con instrumentos caseros. Por eso la regla se apoya en muchas investigaciones y no en una sola.",
      "Se pueden dar ejemplos de transformaciones en la vida diaria: el sol calienta el suelo, una batería mueve un juguete, un calentador eléctrico produce calor, una persona transforma el alimento en movimiento. Dar ejemplos y explicar la transformación con una cadena de energía muestra que se entendió la idea.",
  ],
  vocab=[("conservación de la energía", "la energía total no cambia, solo se transforma"), ("conclusión", "afirmación apoyada en los datos"), ("ejemplo", "caso que ilustra una idea"), ("límite de la investigación", "lo que la investigación no pudo comprobar"), ("total", "suma de todas las partes")],
  worked=[
      ("Comprobar la conservación", "Una pelota tiene 80 unidades de energía al caer; en el rebote hay 45 en movimiento y el resto se transformó en sonido y calor. ¿Cuántas unidades se transformaron en sonido y calor?", ["El total es 80.", "En movimiento quedan 45.", "El resto es 80 − 45."], "35 unidades"),
      ("Dar un ejemplo", "Da un ejemplo de transformación y explica la cadena: un juguete a pilas que avanza.", ["La pila guarda energía química.", "Se transforma en eléctrica y luego en cinética.", "También sale algo de calor y sonido."], "Química → eléctrica → cinética + calor y sonido"),
  ],
  mistakes=[
      ("Concluir que la energía se pierde porque la pelota rebota menos.", "Parte se transformó en sonido y calor; el total se conserva.", "Haz la suma de las partes para comprobar."),
      ("Comunicar solo el resultado sin datos.", "Sin números no se puede comprobar.", "Entrega datos, interpretación y límites."),
  ],
  rec=[
      ("Según la conservación, ¿la energía total cambia o se mantiene?", "Se mantiene", "Solo se transforma."),
      ("Si una pelota tiene 100 unidades y 60 están en movimiento, ¿cuánta energía se disipó?", "40", "100 − 60 = 40."),
      ("¿El calor del choque es fácil o difícil de medir con instrumentos caseros?", "Difícil", "Es muy pequeño."),
  ],
  und=[
      ("¿Qué significa que la energía se conserva?", "Que el total no cambia, solo se transforma", "Se reparte en distintas formas."),
      ("¿Qué debe incluir una conclusión científica? A) Datos y límites. B) Solo opiniones.", "A", "Los datos y los límites la hacen confiable."),
      ("¿Por qué no se dice que la energía «se perdió»?", "Porque se transformó en otras formas como calor y sonido", "El total sigue existiendo."),
  ],
  app=[
      arith("Una pelota tiene 120 unidades de energía; en el rebote hay 70 en movimiento. ¿Cuántas se transformaron en sonido y calor?", "120-70", "El resto del total."),
      arith("Si en el segundo rebote hay 40 unidades en movimiento y 30 se transformaron en sonido y calor, ¿cuál era la energía de ese momento?", "40+30", "Se suman las partes."),
      ("Menciona cuál es una transformación válida: A) Cinética → térmica al frenar con las manos. B) Térmica → nada.", "A", "Al frenar, el movimiento se transforma en calor."),
  ],
  rea=[
      ("Una estudiante mide 60 unidades en el rebote y dice que las otras 40 unidades, de un total de 100, «desaparecieron». ¿Qué afirmación es correcta? A) Se transformaron en sonido y calor. B) Se destruyeron.", "A", "La energía se conserva."),
      ("Un grupo concluye con una sola prueba que la energía siempre se conserva. ¿Qué falta? A) Más investigaciones. B) Más colores.", "A", "La ciencia se apoya en muchas pruebas."),
  ],
  cha=[
      ("Cadena de ejemplo: 200 unidades de energía eléctrica en un ventilador; 150 son movimiento y 30 sonido. ¿Cuántas son calor, si el total se conserva?", "20", "200 − 150 − 30 = 20."),
      ("Marca la mejor conclusión. A) En este experimento, el total de las partes coincidió con la energía inicial, aunque el calor fue difícil de medir. B) La energía se pierde siempre.", "A", "La A incluye un límite."),
  ],
  context=[("Dato de ejemplo. Un motor de juguete recibe 90 unidades de energía eléctrica y entrega 54 en movimiento. ¿Cuántas unidades se transforman en otras formas?", "36", "90 − 54 = 36.")],
  selfcheck=[("¿Qué dice la conservación de la energía?", "Que no se crea ni se destruye, solo se transforma", "El total no cambia."), ("¿Qué incluye una buena conclusión?", "Datos, interpretación y límites", "Así se puede comprobar."), ("¿Qué ejemplo cotidiano de transformación puedes dar?", "Una batería que mueve un juguete", "Pasa de química a cinética.")],
  open_task=task("Escribe una conclusión de cinco líneas a partir de estos datos de ejemplo: una pelota que cae tiene 100 unidades; en el primer rebote tiene 64 en movimiento, y el resto es sonido y calor. Incluye datos, la suma que muestra que se conserva, dos ejemplos de transformaciones de la vida diaria y un límite.", "Datos: 100 unidades al inicio; 64 en el rebote; 36 en sonido y calor. 64 + 36 = 100. Ejemplos: la pila mueve un juguete; el Sol calienta el suelo. Límite: el calor es difícil de medir con instrumentos caseros.", ["datos y suma correcta", "dos ejemplos de transformación", "un límite"], ["texto de cinco líneas"], ["decir que la energía desaparece", "olvidar los límites"], "Pregunta cómo comprobaría la suma en otro experimento."),
  reinforce="Escribe dos transformaciones de energía que veas en un día.",
  extend="Explica por qué la conservación de la energía necesita muchas investigaciones.")

# ---------------------------------------------------------------- OA 10
L(OA10, 1,
  materials="Este cuaderno y lápiz. Opcional (con una persona adulta): un termómetro de cocina, dos vasos plásticos y agua tibia que se pueda tocar sin molestia y agua fría de la llave. Nunca uses agua hirviendo.",
  use="Aprenderé que el calor pasa de un objeto caliente a uno frío y a separar lo observado de lo supuesto. Sirve para explicar por qué un té tibio se enfría.",
  prior=["Sé que el termómetro mide la temperatura en grados Celsius.", "Sé que una observación se mide o se cuenta."],
  explain=[
      "La temperatura indica qué tan caliente o fría está una cosa y se mide con un termómetro en grados Celsius (°C). El calor es la energía que pasa de un objeto con mayor temperatura a otro con menor temperatura. Si pones un vaso de agua caliente junto a uno de agua fría, el calor pasa del caliente al frío.",
      "El calor pasa hasta que ambos alcanzan la misma temperatura. Entonces ya no hay paso de calor y se dice que están en equilibrio térmico. Por eso un té caliente se enfría hasta quedar a la temperatura de la habitación. Lo frío no es una energía que «entra»: lo que ocurre es que el objeto frío recibe calor del caliente.",
      "Al medir, una observación es «el té bajó de 60 °C a 40 °C en 20 minutos». Una interpretación es «el frío del aire entró al té». Solo la primera se midió. La segunda es una idea que se corrige: lo que pasó es que el té entregó calor al aire.",
  ],
  vocab=[("temperatura", "medida de qué tan caliente o frío está algo"), ("calor", "energía que pasa del objeto más caliente al más frío"), ("equilibrio térmico", "situación en que dos objetos tienen la misma temperatura"), ("termómetro", "instrumento que mide la temperatura"), ("grado Celsius", "unidad de temperatura, °C")],
  worked=[
      ("Dirección del calor", "Un vaso a 60 °C y otro a 20 °C están en contacto. ¿Hacia dónde pasa el calor?", ["Comparo las temperaturas: 60 y 20.", "El calor va del que tiene más temperatura.", "Va hacia el que tiene menos."], "Del vaso de 60 °C al de 20 °C"),
      ("Observación o interpretación", "Dos frases: (1) «El té bajó de 60 °C a 40 °C en 20 minutos». (2) «El frío del aire entró al té». ¿Cuál es la observación?", ["Pregunto qué frase se midió.", "La frase 1 tiene medidas.", "La frase 2 supone un hecho que no se midió."], "La frase 1"),
  ],
  mistakes=[
      ("Decir que el frío pasa a los objetos.", "Lo que pasa es calor, del más caliente al más frío.", "Describe siempre hacia dónde va el calor."),
      ("Confundir calor con temperatura.", "La temperatura se mide en °C; el calor es la energía que pasa.", "Usa termómetro para la temperatura."),
  ],
  rec=[
      ("¿El calor pasa del objeto más caliente al más frío o al revés?", "Del más caliente al más frío", "Siempre en ese sentido."),
      ("¿Con qué instrumento se mide la temperatura: con un termómetro o con una regla?", "Con un termómetro", "Mide en °C."),
      ("Cuando dos objetos tienen la misma temperatura, ¿sigue pasando calor: Sí o No?", "No", "Están en equilibrio térmico."),
  ],
  und=[
      ("¿Cuál es una interpretación? A) El té bajó de 60 a 40 °C. B) El frío del aire entró al té.", "B", "No se midió."),
      ("¿Qué pasa con un té caliente que se deja en una habitación?", "Se enfría hasta tener la temperatura de la habitación", "Entrega calor al aire."),
      ("¿Qué es el equilibrio térmico?", "Cuando dos objetos tienen la misma temperatura", "Ya no pasa calor entre ellos."),
  ],
  app=[
      arith("Un té estaba a 70 °C y después de 30 minutos está a 36 °C (datos de ejemplo). ¿Cuántos grados bajó?", "70-36", "Se resta la temperatura final de la inicial."),
      arith("Una bebida fría estaba a 6 °C y después de una hora al aire de la sala está a 18 °C. ¿Cuántos grados subió?", "18-6", "Se resta la inicial de la final."),
      ("Un vaso A está a 45 °C y un vaso B a 25 °C. Si se tocan, ¿cuál recibe calor: A o B?", "B", "Recibe calor el de menor temperatura."),
  ],
  rea=[
      ("Un compañero dice: «El hielo le pasa frío a mi mano». ¿Qué afirmación es correcta? A) Mi mano le pasa calor al hielo. B) El hielo le pasa frío a mi mano.", "A", "El calor va de la mano al hielo."),
      ("Una niña mide 60 °C en un té y 20 °C en el aire de la sala. Antes del resultado, ¿hacia dónde predice que pasará el calor: del té al aire o del aire al té?", "Del té al aire", "El té tiene mayor temperatura."),
  ],
  cha=[
      ("Datos de ejemplo: té a 60 °C. A los 10 minutos, 44 °C; a los 20 minutos, 34 °C; a los 30, 28 °C. ¿En qué intervalo de 10 minutos bajó más?", "Entre 0 y 10 minutos", "Bajó 16 °C, más que en los otros."),
      ("¿Qué temperatura final esperas del té después de varias horas en una sala a 20 °C?", "Cerca de 20 °C", "Llega al equilibrio con el aire."),
  ],
  context=[("Dato de ejemplo. Un vaso de agua a 55 °C se deja en una sala a 20 °C. ¿Cuántos grados de diferencia hay al comenzar?", "35", "55 − 20 = 35.")],
  selfcheck=[("¿Hacia dónde pasa el calor?", "Del objeto más caliente al más frío", "Hasta que las temperaturas se igualan."), ("¿Qué ocurre con el paso de calor cuando se alcanza el equilibrio térmico?", "Ya no pasa calor entre los objetos", "Las temperaturas son iguales."), ("¿Cómo se reconoce una interpretación?", "No se mide", "Hay que contrastarla con datos.")],
  open_task=task("Con estos datos de ejemplo de un vaso con agua tibia en una sala a 20 °C (inicio 48 °C; 10 min, 38 °C; 20 min, 31 °C; 30 min, 26 °C), calcula cuánto bajó en cada intervalo de 10 minutos y escribe una observación con números, una interpretación y hacia dónde pasó el calor. Si puedes, hazlo con agua tibia que se pueda tocar sin molestia y un termómetro, con una persona adulta.", "Bajó 10, 7 y 5 °C. Observación: a los 30 min estaba a 26 °C. Interpretación: pronto llegará a 20 °C. El calor pasó del agua al aire.", ["tres diferencias correctas", "observación con números", "dirección del calor"], ["cálculos y frases"], ["decir que el frío entró", "mezclar observación e interpretación"], "Pregunta por qué cada intervalo baja menos que el anterior."),
  reinforce="Escribe hacia dónde pasa el calor entre una taza caliente y la mesa.",
  extend="Explica por qué el té no se enfría por debajo de la temperatura de la sala.")

L(OA10, 2,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios. Cualquier experimento real debe hacerse solo con agua tibia que se pueda tocar sin molestia y con una persona adulta.",
  use="Aprenderé a formular una pregunta y una predicción sobre el flujo del calor. Sirve para anticipar la temperatura final al mezclar o al poner objetos en contacto.",
  prior=["Sé que el calor pasa de lo caliente a lo frío.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una pregunta comprobable nombra qué se mide: «¿Cuál es la temperatura final al mezclar 200 mL de agua a 40 °C con 200 mL de agua a 20 °C?». Se responde con un termómetro. Una pregunta como «¿Qué temperatura es más agradable?» no se comprueba.",
      "Una predicción dice qué ocurrirá y por qué. Cuando se mezclan cantidades iguales de agua de la misma sustancia, la temperatura final queda más o menos a mitad de camino: para 40 °C y 20 °C, unos 30 °C, porque el agua más caliente cede calor y la más fría lo recibe hasta igualarse. Se dice «más o menos» porque algo de calor se pierde al aire y al vaso.",
      "Para comprobar se mide antes y después y se compara con la predicción. Si la medida es parecida, la predicción se apoya, pero se repite para estar más seguros. Si es muy distinta, se revisa la idea o se buscan otras causas, como el calor que se pierde al ambiente.",
  ],
  vocab=[("mezcla", "unión de dos cantidades de agua"), ("temperatura final", "temperatura que queda cuando termina el proceso"), ("ceder calor", "entregar calor a otro objeto"), ("recibir calor", "tomar calor de otro objeto"), ("pérdida de calor", "calor que pasa al ambiente")],
  worked=[
      ("Predecir la mezcla", "Se mezclan 100 mL de agua a 50 °C con 100 mL a 30 °C. ¿Qué temperatura final predices?", ["Las cantidades son iguales.", "La temperatura queda a mitad de camino.", "Calculo (50 + 30) ÷ 2."], "Cerca de 40 °C"),
      ("Pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Cuál es la temperatura final de una mezcla de agua tibia y fría? B) ¿Cuál agua es más simpática?", ["Busco la pregunta con una medida.", "En A se usa un termómetro.", "En B es un gusto."], "A"),
  ],
  mistakes=[
      ("Predecir que la temperatura final es la del agua más caliente.", "El agua caliente cede calor y la fría lo recibe.", "Predice una temperatura intermedia."),
      ("Esperar un resultado exacto.", "Algo de calor se pierde al ambiente.", "Usa «más o menos» o «cerca de»."),
  ],
  rec=[
      ("Al mezclar agua caliente y fría en cantidades iguales, ¿la temperatura final es intermedia o igual a la caliente?", "Intermedia", "El agua caliente cede calor."),
      ("¿La predicción se hace antes de mezclar: Sí o No?", "Sí", "Se plantea lo que se espera."),
      ("¿El agua caliente cede o recibe calor al mezclarse con agua fría?", "Cede", "Entrega calor al agua fría."),
  ],
  und=[
      ("Se mezclan cantidades iguales de agua a 60 °C y 20 °C. ¿Cuál es la temperatura más probable? A) 40 °C. B) 70 °C.", "A", "Queda a mitad de camino."),
      ("¿Por qué el resultado real puede ser un poco menor que la predicción?", "Porque algo de calor se pierde al aire y al vaso", "No todo queda en la mezcla."),
      ("¿Qué mide el termómetro en el experimento?", "La temperatura antes y después de mezclar", "Se compara con la predicción."),
  ],
  app=[
      arith("Se mezclan cantidades iguales de agua a 36 °C y 24 °C. ¿Qué temperatura final predices?", "(36+24)//2", "Se suman las temperaturas y se divide por 2."),
      arith("Se mezclan cantidades iguales de agua a 46 °C y 18 °C. ¿Qué temperatura final predices?", "(46+18)//2", "Se calcula el punto medio."),
      ("Si el agua A está a 50 °C y la B a 20 °C, ¿cuál cede calor?", "A", "Tiene mayor temperatura."),
  ],
  rea=[
      ("Un estudiante predice que, al mezclar partes iguales de agua a 40 °C y 20 °C, quedará a 50 °C. ¿Su predicción es compatible con el flujo del calor? Responde Sí o No.", "No", "La temperatura final debe quedar entre 20 y 40 °C."),
      ("Una niña mide 29 °C en la mezcla de 40 °C y 20 °C y predijo 30 °C. ¿Se apoya la predicción? Responde Sí o No.", "Sí", "29 está muy cerca de 30."),
  ],
  cha=[
      ("Se mezclan 100 mL a 80 °C con 100 mL a 20 °C (datos de ejemplo). ¿Cuál es la predicción?", "50 °C", "(80 + 20) ÷ 2 = 50."),
      ("Marca la mejor predicción. A) Quedará cerca de 30 °C, porque el agua caliente cede calor al agua fría. B) Quedará en 80 °C, porque sí.", "A", "La A da razón y es intermedia."),
  ],
  context=[("Dato de ejemplo. Se mezclaron 150 mL de agua a 52 °C con 150 mL de agua a 28 °C. ¿Qué temperatura final se predice?", "40", "(52 + 28) ÷ 2 = 40.")],
  selfcheck=[("¿Qué temperatura se predice al mezclar cantidades iguales?", "La mitad del camino entre ambas", "El caliente cede y el frío recibe."), ("¿Por qué se dice «más o menos»?", "Porque se pierde algo de calor al ambiente", "El resultado no es exacto."), ("¿Se cambian los datos si no coinciden con la predicción?", "No", "Se revisa la idea.")],
  open_task=task("Escribe una pregunta comprobable y una predicción con razón sobre mezclar partes iguales de agua a 46 °C y a 22 °C. Calcula la temperatura predicha y escribe una causa posible de que el resultado real sea un poco distinto.", "Pregunta: ¿qué temperatura queda al mezclar? Predicción: unos 34 °C, porque el agua caliente cede calor al fría. Cálculo: (46 + 22) ÷ 2 = 34. Causa: parte del calor pasa al vaso y al aire.", ["pregunta comprobable", "predicción con razón", "cálculo y causa"], ["tres frases"], ["no dar razón", "predecir fuera del intervalo"], "Pregunta qué pasaría con cantidades distintas de agua."),
  reinforce="Calcula el punto medio entre 30 °C y 50 °C.",
  extend="Explica por qué la temperatura final no puede estar fuera del intervalo de las temperaturas iniciales.")

L(OA10, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: papel cuadriculado para el gráfico.",
  use="Aprenderé a representar con flechas y con un gráfico cómo el calor fluye hasta igualar las temperaturas. Sirve para ver cómo se acercan dos temperaturas con el tiempo.",
  prior=["Sé que el calor pasa de lo caliente a lo frío.", "Sé leer una tabla de temperatura y tiempo."],
  explain=[
      "Un modelo con flechas dibuja los dos objetos y una flecha que apunta desde el caliente hacia el frío. Esa flecha representa el paso de calor. Puedes escribir las temperaturas: 60 °C → 20 °C. A medida que pasa el tiempo, el caliente baja y el frío sube, hasta que ambos quedan iguales y la flecha desaparece.",
      "Un gráfico de líneas muestra lo mismo. En el eje horizontal se pone el tiempo y en el vertical la temperatura. La línea del objeto caliente baja y la del frío sube. Las dos líneas se acercan y se juntan cuando llegan al equilibrio térmico. Al principio cambian rápido, y al final cambian lento porque ya hay poca diferencia entre ellos.",
      "El modelo tiene límites. No muestra cuánto calor pasa, cómo es el contacto ni el calor que se pierde al aire. Por ejemplo, una taza se enfría no solo por la mesa sino también por el aire que la rodea. Un buen modelo dice qué muestra y qué no.",
  ],
  vocab=[("flecha de calor", "flecha que indica hacia dónde pasa el calor"), ("eje horizontal", "línea del gráfico donde se escribe el tiempo"), ("eje vertical", "línea del gráfico donde se escribe la temperatura"), ("curva", "línea que une los puntos de un gráfico"), ("cruce de líneas", "punto donde las temperaturas se igualan")],
  worked=[
      ("Leer un gráfico", "Tabla de ejemplo: caliente 60 °C, 50 °C, 45 °C, 42 °C, 40 °C; frío 20 °C, 30 °C, 35 °C, 38 °C, 40 °C, cada 5 minutos. ¿Cuándo se igualan las temperaturas?", ["Busco el momento en que ambos valores coinciden.", "En el quinto dato ambos son 40 °C.", "Es a los 20 minutos."], "A los 20 minutos, a 40 °C"),
      ("Dibujar la flecha", "Un vaso a 30 °C y otro a 10 °C se tocan. ¿Hacia dónde apuntas la flecha?", ["Identifico el de mayor temperatura: 30 °C.", "La flecha parte de él.", "Apunta al de 10 °C."], "Del vaso de 30 °C al de 10 °C"),
  ],
  mistakes=[
      ("Apuntar la flecha hacia el objeto más caliente.", "El calor va hacia el más frío.", "Parte de la mayor temperatura."),
      ("Pensar que las temperaturas siguen cambiando después de igualarse.", "En el equilibrio ya no pasa calor.", "Las líneas se juntan y dejan de cambiar."),
  ],
  rec=[
      ("En el gráfico, ¿qué va en el eje horizontal: el tiempo o la temperatura?", "El tiempo", "La temperatura va en el vertical."),
      ("¿La flecha de calor apunta hacia el más caliente o hacia el más frío?", "Hacia el más frío", "El calor va hacia allí."),
      ("Cuando las líneas del gráfico se juntan, ¿hay equilibrio térmico: Sí o No?", "Sí", "Las temperaturas son iguales."),
  ],
  und=[
      ("En el gráfico del caliente y el frío, ¿qué hace la línea del frío? A) Sube. B) Baja.", "A", "El frío recibe calor."),
      ("¿Por qué al final la temperatura cambia más lento?", "Porque ya hay poca diferencia entre los objetos", "El calor pasa menos."),
      ("Un límite del modelo es que no muestra ______. Elige el calor perdido al aire o la flecha.", "El calor perdido al aire", "Es algo que el modelo no representa."),
  ],
  app=[
      arith("Un objeto caliente baja de 70 °C a 46 °C. ¿Cuántos grados bajó?", "70-46", "Se resta la final de la inicial."),
      arith("Un objeto frío sube de 14 °C a 38 °C. ¿Cuántos grados subió?", "38-14", "Se resta la inicial de la final."),
      ("Las líneas se encuentran a 36 °C. ¿Cuál es la temperatura final de ambos?", "36 °C", "Están en equilibrio térmico."),
  ],
  rea=[
      ("Una compañera dibujó la línea del caliente subiendo en el gráfico. ¿Qué error tiene?", "La línea del caliente debe bajar", "El objeto caliente cede calor."),
      ("Otro dice que el gráfico muestra cuánto calor pasó. ¿Es correcto? Responde Sí o No.", "No", "Solo muestra temperaturas."),
  ],
  cha=[
      ("Datos de ejemplo: caliente 70 °C → 54 °C → 46 °C → 42 °C → 40 °C; frío 10 °C → 26 °C → 34 °C → 38 °C → 40 °C. ¿Cuántos grados cambió el frío en el primer intervalo?", "16", "26 − 10 = 16."),
      ("Con esos datos, ¿en qué intervalo hubo más cambio, en el primero o en el último?", "En el primero", "Al comienzo hay más diferencia."),
  ],
  context=[("Dato de ejemplo. Un vaso a 64 °C y otro a 12 °C llegan a 38 °C después de media hora. ¿Cuántos grados bajó el caliente?", "26", "64 − 38 = 26.")],
  selfcheck=[("¿Qué indica la flecha de calor?", "Hacia dónde pasa el calor", "Del más caliente al más frío."), ("¿Qué pasa con las líneas del gráfico?", "Se acercan y se juntan", "Hasta alcanzar el equilibrio."), ("¿Qué límite tiene el modelo?", "No muestra el calor perdido al aire", "Solo representa algunas cosas.")],
  open_task=task("Con estos datos de ejemplo, haz un gráfico de líneas (tiempo horizontal, temperatura vertical): minutos 0, 10, 20, 30; vaso caliente: 56, 44, 38, 36 °C; vaso frío: 16, 28, 34, 36 °C. Dibuja las dos líneas, marca el punto de equilibrio y escribe un límite.", "Las líneas se juntan a los 30 minutos en 36 °C. El caliente bajó 20 y el frío subió 20. Límite: no muestra el calor perdido al aire.", ["ejes rotulados", "dos líneas correctas", "punto de equilibrio y límite"], ["gráfico dibujado"], ["invertir las líneas", "olvidar el límite"], "Pregunta por qué las líneas cambian más rápido al principio."),
  reinforce="Dibuja una flecha de calor entre un vaso a 40 °C y otro a 15 °C.",
  extend="Explica por qué el cambio de temperatura es más rápido al principio.")

L(OA10, 4,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a comparar materiales según qué tan rápido dejan pasar el calor. Sirve para entender por qué una cuchara de metal se calienta más rápido que una de plástico.",
  prior=["Sé que el calor fluye de lo caliente a lo frío.", "Sé comparar datos de tiempo."],
  explain=[
      "No todos los materiales dejan pasar el calor con la misma rapidez. Los metales son buenos conductores: el calor pasa por ellos rápidamente. El plástico, la madera y la espuma son malos conductores, también llamados aislantes. Por eso una cuchara de metal en una taza caliente se calienta rápido y una de plástico demora más.",
      "Para comparar, se puede medir el tiempo que demora cada material en alcanzar cierta temperatura. Con el criterio «menos tiempo, mejor conductor», se ordenan los materiales. Por ejemplo, si la cuchara de metal demora 2 minutos, la de madera 7 y la de plástico 9, el metal es el mejor conductor.",
      "Para que la comparación sea justa, las cucharas deben tener un tamaño parecido, partir de la misma temperatura y estar en el mismo agua tibia. Un límite es que se miden pocos materiales y que cada medición tiene errores. Una buena conclusión dice qué criterio usó y qué materiales probó.",
  ],
  vocab=[("conductor", "material que deja pasar el calor con facilidad"), ("aislante", "material que deja pasar poco el calor"), ("criterio", "regla para comparar"), ("comparación justa", "comparación en que solo cambia el material"), ("espuma", "material liviano que aísla")],
  worked=[
      ("Ordenar según el criterio", "Tiempos de ejemplo para calentarse: metal 2 minutos, madera 7, plástico 9. Ordena de mejor a peor conductor.", ["Menor tiempo, mejor conductor.", "El menor es 2: metal.", "Luego madera y plástico."], "Metal, madera, plástico"),
      ("Calcular una diferencia", "Con esos datos, ¿cuántos minutos más demora el plástico que el metal?", ["Plástico: 9.", "Metal: 2.", "Resto 9 − 2."], "7 minutos"),
  ],
  mistakes=[
      ("Pensar que los metales son más fríos porque se sienten fríos.", "Se sienten fríos porque conducen rápido el calor de tu mano, no porque tengan menos temperatura.", "Mide con un termómetro."),
      ("Comparar cucharas de distintos tamaños.", "El tamaño también influye en el tiempo.", "Usa cucharas parecidas."),
  ],
  rec=[
      ("¿Los metales son buenos conductores del calor: Sí o No?", "Sí", "Dejan pasar el calor rápido."),
      ("Un material que deja pasar poco el calor, ¿es conductor o aislante?", "Aislante", "Aísla del calor."),
      ("¿Demora menos tiempo en calentarse el buen conductor o el aislante?", "El buen conductor", "El calor pasa rápido."),
  ],
  und=[
      ("¿Qué criterio se usó para ordenar los materiales?", "El tiempo que demoran en calentarse", "Menos tiempo, mejor conductor."),
      ("¿Por qué una cuchara de metal se siente fría al tocarla?", "Porque conduce rápido el calor de tu mano", "No es porque esté a menos temperatura."),
      ("¿Cuál es un aislante? A) Plástico. B) Metal.", "A", "El plástico deja pasar poco calor."),
  ],
  app=[
      arith("Tres cucharas tardaron 3, 8 y 10 minutos en calentarse. ¿Cuántos minutos suman en total?", "3+8+10", "Se suman los tres tiempos."),
      arith("Una cuchara de aluminio tardó 4 minutos y otra de madera 11. ¿Cuántos minutos más tardó la de madera?", "11-4", "Se restan los tiempos."),
      ("Tiempos: cobre 2 min, vidrio 6 min, plástico 9 min, espuma 12 min. ¿Cuál es el mejor aislante?", "La espuma", "Demoró más tiempo."),
  ],
  rea=[
      ("Un estudiante compara una cuchara grande de plástico con una chica de metal y dice que el metal conduce mejor. ¿Qué problema tiene?", "Cambian el material y el tamaño", "No es una comparación justa."),
      ("Otro dice que, como la madera tardó 7 minutos, es mejor aislante que el plástico que tardó 9. ¿Es correcto? Responde Sí o No.", "No", "El plástico tardó más, por lo que aísla más."),
  ],
  cha=[
      ("Datos de ejemplo: metal 3 minutos y espuma 15 minutos. ¿Cuántas veces más tiempo tardó la espuma que el metal?", "5", "15 ÷ 3 = 5."),
      ("Marca la mejor conclusión. A) En estas pruebas, el metal conduce el calor más rápido que la madera y el plástico. B) El metal es siempre el mejor para todo.", "A", "La A se limita a los datos."),
  ],
  context=[("Dato de ejemplo. Un termo mantiene el agua a 60 °C y baja 4 °C en 2 horas. Una taza de metal baja 28 °C en el mismo tiempo. ¿Cuántos grados más baja la taza?", "24", "28 − 4 = 24.")],
  selfcheck=[("¿Qué es un conductor?", "Un material que deja pasar el calor con facilidad", "Por ejemplo, el metal."), ("¿Qué es un aislante?", "Un material que deja pasar poco calor", "Por ejemplo, el plástico."), ("¿Qué hace justa una comparación?", "Que solo cambie el material", "Lo demás debe ser igual.")],
  open_task=task("Con estos tiempos de ejemplo para calentarse en agua tibia: cuchara de acero 3 min, de madera 8, de plástico 10, de espuma 14, ordena de mejor a peor conductor, calcula cuántos minutos más tarda la espuma que el acero y escribe cómo harías justa la comparación. Si quieres probar en casa, usa agua tibia que se pueda tocar sin molestia y con ayuda de una persona adulta.", "Orden: acero, madera, plástico, espuma. La espuma tarda 11 minutos más. Comparación justa: cucharas del mismo tamaño, mismo agua y misma temperatura inicial.", ["orden correcto", "cálculo correcto", "condiciones de comparación justa"], ["lista ordenada", "frase"], ["ordenar al revés", "comparar tamaños distintos"], "Pregunta qué material elegiría para una manilla de olla y por qué."),
  reinforce="Escribe un material conductor y uno aislante de tu casa.",
  extend="Explica por qué las ollas tienen mangos de plástico o de madera.")

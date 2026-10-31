"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 09 (circuitos eléctricos simples) y OA 10 (conductores, aisladores y seguridad eléctrica)."""
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




OA9, OA10 = "CN05 OA 09", "CN05 OA 10"

# ---------------------------------------------------------------- OA 09
L(OA9, 1,
  materials="Este cuaderno y lápiz. Opcional, con una persona adulta: una pila de 1,5 V (tamaño AA o D), cables con pinzas, una ampolleta pequeña de linterna con su soporte y un interruptor. Nunca uses enchufes.",
  use="Aprenderé las partes de un circuito eléctrico simple y a separar lo que observo de lo que supongo. Sirve para saber por qué una ampolleta enciende o no.",
  prior=["Sé que la ampolleta transforma energía eléctrica en luz y calor.", "Sé que una pila entrega energía eléctrica."],
  explain=[
      "Un circuito eléctrico simple tiene cuatro partes. La pila entrega la energía. Los cables forman el camino. La ampolleta transforma la energía en luz y calor. El interruptor abre o cierra el camino. La corriente eléctrica es el paso de electricidad por ese camino.",
      "Para que la ampolleta encienda, el camino debe ser un círculo sin cortes que salga de un polo de la pila, pase por la ampolleta y vuelva al otro polo. Eso se llama circuito cerrado. Si el camino tiene un corte, por ejemplo un cable suelto o el interruptor abierto, es un circuito abierto y la ampolleta no enciende. La ampolleta tiene dos puntos de contacto: la punta de abajo y el borde metálico lateral. Ambos deben estar conectados.",
      "Al observar un circuito, anota lo que ves: «la ampolleta no enciende y un cable está suelto». Decir «la pila está mala» es una interpretación hasta que se compruebe. Importante: nunca unas los dos polos de una pila solo con un cable, porque se calienta. Y nunca conectes un circuito a un enchufe de la pared.",
  ],
  vocab=[("circuito eléctrico", "camino cerrado por donde pasa la corriente"), ("pila", "fuente que entrega energía eléctrica"), ("interruptor", "pieza que abre o cierra el camino de la corriente"), ("circuito cerrado", "circuito sin cortes, por donde pasa la corriente"), ("circuito abierto", "circuito con un corte, por donde no pasa la corriente")],
  worked=[
      ("Reconocer circuito cerrado o abierto", "Una pila, dos cables, una ampolleta y un interruptor cerrado forman un círculo sin cortes. ¿Es circuito cerrado o abierto?", ["Reviso si hay cortes.", "No hay cortes y el interruptor está cerrado.", "El camino es un círculo completo."], "Cerrado"),
      ("Observación o interpretación", "«Un cable está suelto y la ampolleta no enciende» y «La pila está mala». ¿Cuál es la observación?", ["Pregunto qué se ve.", "El cable suelto y la ampolleta apagada se ven.", "Que la pila esté mala no se comprobó."], "La primera frase"),
  ],
  mistakes=[
      ("Pensar que basta tocar un solo punto de la ampolleta con el cable.", "La ampolleta necesita dos contactos para formar el círculo.", "Conecta la punta y el borde lateral."),
      ("Unir los dos polos de la pila solo con un cable.", "El cable se calienta y la pila se gasta o puede dañarse.", "Siempre pasa por la ampolleta."),
  ],
  rec=[
      ("¿La pila entrega energía o la transforma en luz?", "La entrega", "La ampolleta es la que transforma en luz."),
      ("¿Para qué sirve el interruptor?", "Para abrir o cerrar el camino de la corriente", "Controla si hay paso de electricidad."),
      ("Completa con «cerrado» o «abierto»: si el circuito tiene un corte, es un circuito ______.", "Abierto", "La corriente no puede pasar."),
  ],
  und=[
      ("¿Cuántas partes tiene el circuito simple de esta clase?", "4", "Pila, cables, ampolleta e interruptor."),
      ("¿Por qué una ampolleta con un cable suelto no enciende?", "Porque el circuito queda abierto", "El camino no es un círculo completo."),
      ("Marca la observación: A) La ampolleta está apagada y el interruptor está abierto. B) La ampolleta está enojada.", "A", "A se ve; B es una idea."),
  ],
  app=[
      ("Un circuito tiene pila, dos cables y ampolleta, pero el interruptor está abierto. ¿Enciende la ampolleta? Responde Sí o No.", "No", "El interruptor abierto corta el camino."),
      arith("Un grupo armó 4 circuitos y 3 encendieron la ampolleta. ¿Cuántos circuitos no encendieron?", "4-3", "Se resta los que encendieron al total."),
      ("Pasos para armar el circuito: A) cerrar el interruptor, B) conectar los cables a la ampolleta, C) conectar los cables a la pila. ¿Qué paso conviene dejar al final para armar con orden y seguridad?", "A", "Se conecta todo primero y al final se cierra el interruptor, para que la pila no se gaste mientras armas."),
  ],
  rea=[
      ("Sofi dice: «Con un solo cable de la pila a la ampolleta ya enciende». ¿Tiene razón? Responde Sí o No y explica.", "No; falta el camino de vuelta al otro polo", "El circuito debe ser un círculo completo."),
      ("Un compañero ve que la ampolleta no enciende y dice: «La pila está gastada». ¿Es una observación? Responde Sí o No y explica.", "No; es una suposición que falta comprobar", "Lo observado es que la ampolleta no enciende."),
  ],
  cha=[
      ("Una ampolleta no enciende en un circuito con todo conectado y el interruptor cerrado. Escribe dos posibles causas.", "La pila está gastada o la ampolleta está quemada", "Hay que comprobar cada pieza."),
      ("Explica por qué nunca se debe conectar el circuito a un enchufe de la pared.", "Porque la electricidad de la red es peligrosa", "Las pilas de linterna son seguras; la red no."),
  ],
  context=[("Dato de ejemplo. Una clase armó 5 circuitos y cada uno tenía 4 partes. ¿Cuántas partes usaron en total?", "20", "5 × 4 = 20.")],
  selfcheck=[("Nombra las cuatro partes de un circuito simple.", "Pila, cables, ampolleta e interruptor", "Forman el camino completo."), ("¿Qué es un circuito cerrado?", "Un circuito sin cortes por donde pasa la corriente", "La ampolleta enciende."), ("¿Se puede conectar un circuito al enchufe? Responde Sí o No.", "No", "La electricidad de la red es peligrosa.")],
  open_task=task("Dibuja un circuito simple con una pila, dos cables, una ampolleta y un interruptor. Rotula cada parte. Después escribe una observación (qué pasa con el interruptor abierto y cerrado) y una interpretación. Si lo armas de verdad, hazlo con una persona adulta y solo con una pila de 1,5 V, nunca con enchufes.", "Dibujo con cuatro partes rotuladas. Observación: con el interruptor abierto la ampolleta está apagada y con el interruptor cerrado enciende. Interpretación: el interruptor corta el camino.", ["cuatro partes rotuladas", "observación del interruptor abierto y cerrado", "interpretación marcada"], ["dibujo", "dos frases"], ["conectar a un enchufe", "unir solo los polos de la pila con un cable"], "Pregunta por qué la ampolleta apaga cuando se abre el interruptor."),
  reinforce="Dibuja un circuito abierto y uno cerrado y explica la diferencia.",
  extend="Explica por qué una linterna tiene un interruptor.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Opcional, con una persona adulta: pila de 1,5 V, cables con pinzas, ampolleta de linterna y un interruptor.",
  use="Aprenderé a hacer preguntas y predicciones sobre cuándo enciende un circuito. Sirve para encontrar por qué una ampolleta no funciona.",
  prior=["Sé las partes de un circuito simple.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una pregunta comprobable sobre circuitos puede ser: «¿Enciende la ampolleta si el interruptor está abierto?». Una predicción es lo que esperas con su razón: «No enciende, porque el interruptor abierto corta el camino». Para comprobarla se cambia una sola cosa y se observa si la ampolleta enciende.",
      "Cuando un circuito no funciona, se busca la falla con orden. Primero revisa que el interruptor esté cerrado. Luego revisa que los cables estén bien conectados a los dos puntos de la ampolleta y a los polos de la pila. Después cambia la ampolleta por otra y, por último, la pila. Así encuentras la causa, que es una de las partes.",
      "Anota cada prueba en una tabla con lo que cambiaste y lo que observaste. Cambia una sola cosa por prueba. Si cambias varias a la vez, no sabrás cuál arregló el circuito. Y repite la prueba para confirmar el resultado.",
  ],
  vocab=[("falla", "problema que impide que algo funcione"), ("prueba", "intento para comprobar una idea"), ("conexión", "unión entre dos partes"), ("variable", "lo que cambia en una prueba"), ("polo", "extremo de la pila donde se conecta un cable")],
  worked=[
      ("Predicción con razón", "El interruptor está abierto y todo lo demás está conectado. Predice si enciende la ampolleta.", ["El interruptor abierto es un corte.", "Sin camino completo no pasa corriente.", "Escribo la predicción con razón."], "No enciende, porque el camino queda cortado"),
      ("Buscar la falla", "Un circuito no enciende. El interruptor está cerrado y los cables están bien conectados. Cambias la ampolleta y enciende. ¿Cuál era la falla?", ["Antes no encendía.", "Solo cambiaste la ampolleta.", "Con otra ampolleta enciende."], "La ampolleta estaba quemada"),
  ],
  mistakes=[
      ("Cambiar a la vez la pila, la ampolleta y los cables.", "No se sabe qué estaba fallando.", "Cambia una sola cosa por prueba."),
      ("Concluir con una sola prueba.", "Puede haber sido casualidad.", "Repite la prueba."),
  ],
  rec=[
      ("Si el circuito no enciende, ¿qué se revisa primero según esta clase: el interruptor o la pila?", "El interruptor", "Puede estar abierto y es lo más fácil de revisar."),
      ("¿Cuántas cosas se cambian por prueba?", "Una", "Así se sabe qué arregló el circuito."),
      ("Completa con «antes» o «después»: la predicción se hace ______ de probar.", "Antes", "Es una idea previa que luego se comprueba."),
  ],
  und=[
      ("¿Por qué se cambia solo una pieza en cada prueba?", "Para saber cuál era la falla", "Si se cambian varias, no se sabe cuál arregló."),
      ("¿Qué pregunta se puede comprobar? A) ¿Enciende la ampolleta si el interruptor está abierto? B) ¿Es lindo el circuito?", "A", "Se observa si enciende."),
      ("Si la ampolleta enciende con otra pila, ¿qué pieza estaba mala?", "La pila", "Solo cambió la pila."),
  ],
  app=[
      ("Prueba 1: se cierra el interruptor y no enciende. Prueba 2: se cambia la ampolleta y enciende. ¿Qué pieza fallaba?", "La ampolleta", "Con otra ampolleta enciende."),
      arith("Dato de ejemplo. Se hicieron 6 pruebas y en 4 la ampolleta encendió. ¿En cuántas no encendió?", "6-4", "Se resta las que encendieron al total."),
      ("Rita predijo que no encendería con el interruptor abierto. Observó que no encendió. ¿Se cumplió su predicción? Responde Sí o No.", "Sí", "El resultado coincide con lo predicho."),
  ],
  rea=[
      ("Teo cambió la pila y la ampolleta a la vez y la ampolleta encendió. Dice: «Era la pila». ¿Puede asegurarlo? Responde Sí o No y explica.", "No; cambió dos cosas", "Pudo ser la pila o la ampolleta."),
      ("Ema repitió tres veces la prueba con el interruptor abierto y nunca encendió. ¿Qué ganó con repetirla?", "Más confianza en el resultado", "Repetir muestra que no fue casualidad."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre un circuito, indicando qué observarás.", "¿Enciende la ampolleta cuando el interruptor está cerrado y cuando está abierto?", "Nombra lo que cambia y lo que se observa."),
      ("Un circuito no enciende. ¿Qué pieza revisas primero y cuál por último, según el orden de esta clase?", "Primero el interruptor y por último la pila", "Se parte por lo más fácil y se avanza con orden."),
  ],
  context=[("Dato de ejemplo. Una clase hizo 3 pruebas por circuito en 5 circuitos. ¿Cuántas pruebas hizo?", "15", "3 × 5 = 15.")],
  selfcheck=[("¿Qué lleva una buena predicción?", "Lo que pasará y la razón", "Así se puede comprobar."), ("¿Por qué cambiar una sola pieza?", "Para saber cuál era la falla", "Con varios cambios no se sabe."), ("¿Qué haces si todo parece conectado y no enciende?", "Reviso el interruptor, la ampolleta y la pila de a una", "Así se encuentra la falla.")],
  open_task=task("Con una persona adulta, arma un circuito simple con pila de 1,5 V, ampolleta de linterna, cables e interruptor. Antes de cerrar el interruptor, escribe tu predicción con razón. Prueba con el interruptor abierto y cerrado y anota qué observaste. Si no puedes armarlo, usa el dibujo de la clase anterior y escribe tus predicciones.", "Predicción: no encenderá con el interruptor abierto porque el camino está cortado. Resultado de ejemplo: abierto, apagada; cerrado, encendida. La predicción se cumplió.", ["predicción con razón", "dos pruebas anotadas", "conclusión con la observación"], ["tabla con dos pruebas", "frase de conclusión"], ["cambiar varias piezas a la vez", "conectar a un enchufe"], "Pregunta qué cambió entre las pruebas y qué más podría influir en el resultado."),
  reinforce="Escribe una predicción con razón sobre qué pasa si un cable no toca la ampolleta.",
  extend="Explica con tus palabras cómo buscarías la falla de una linterna que no enciende.")

L(OA9, 3,
  materials="Este cuaderno, lápiz y regla.",
  use="Aprenderé a dibujar un circuito con símbolos y a explicar su funcionamiento. Sirve para comunicar un circuito sin armarlo.",
  prior=["Sé las partes de un circuito.", "Sé que un modelo tiene límites."],
  explain=[
      "Un esquema de circuito es un dibujo con símbolos. En esta clase usamos símbolos simples. Una línea es el cable y un círculo con una X es la ampolleta. Dos rayitas paralelas, una larga y una corta, son la pila. Una línea con un hueco y una palanca es el interruptor. La línea corta de la pila es el polo negativo y la larga es el positivo.",
      "En un esquema el camino debe ser un círculo. Si ves una línea cortada, ese es el interruptor abierto o un cable suelto. Para explicar el funcionamiento, sigue el camino con el dedo: sale de un polo de la pila, pasa por el interruptor, llega a la ampolleta y vuelve al otro polo. Si el interruptor se cierra, el camino es completo y la ampolleta se enciende.",
      "Una analogía es un circuito de agua: la pila sería una bomba, los cables serían tuberías y la ampolleta sería una rueda. Este modelo ayuda a imaginar un camino cerrado, pero tiene límites: en un cable no se ve moverse nada y la corriente no es agua.",
  ],
  vocab=[("símbolo", "dibujo simple que representa una pieza"), ("esquema", "dibujo con símbolos que muestra cómo se conecta un circuito"), ("polo positivo", "extremo de la pila marcado con más (+)"), ("polo negativo", "extremo de la pila marcado con menos (−)"), ("analogía", "comparación con algo conocido para entender mejor")],
  worked=[
      ("Leer un esquema", "Un esquema tiene una pila, un interruptor abierto y una ampolleta unidos en círculo. ¿Enciende la ampolleta?", ["Sigo el camino con el dedo.", "El interruptor abierto corta el círculo.", "No hay paso completo."], "No enciende"),
      ("Encontrar un límite", "En la analogía del agua, la pila es una bomba. ¿Es un límite que el agua se vea y la corriente no?", ["En un cable no se ve nada moverse.", "El agua sí se ve.", "Eso real no coincide con el modelo."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Dibujar un circuito con el camino cortado sin querer.", "Un esquema con un corte representa un circuito abierto.", "Revisa que el círculo esté completo."),
      ("Pensar que la analogía del agua es exacta.", "La corriente no es agua.", "Escribe el límite."),
  ],
  rec=[
      ("¿Qué símbolo representa el cable: una línea o un círculo con X?", "Una línea", "El círculo con X es la ampolleta."),
      ("¿Qué representa el círculo con una X?", "La ampolleta", "Es el símbolo de la ampolleta."),
      ("Completa con «círculo» o «línea cortada»: el camino de un circuito cerrado es un ______.", "Círculo", "Debe volver al otro polo de la pila."),
  ],
  und=[
      ("¿Qué indica una línea cortada en un esquema?", "Un interruptor abierto o un cable suelto", "El camino no está completo."),
      ("¿Por qué conviene seguir el camino con el dedo?", "Para ver si hay un círculo completo", "Así se encuentra el corte."),
      ("En la analogía del agua, ¿qué representa la bomba? A) La pila. B) La ampolleta.", "A", "Impulsa el movimiento como la pila."),
  ],
  app=[
      ("Un esquema tiene 4 símbolos unidos por 4 líneas en círculo. ¿Es un circuito cerrado o abierto, si el interruptor dibujado está cerrado?", "Cerrado", "El círculo está completo."),
      arith("Un grupo dibujó 3 esquemas con 5 símbolos cada uno. ¿Cuántos símbolos dibujó?", "3*5", "Se multiplican los esquemas por los símbolos."),
      ("En un esquema, el interruptor se dibuja con la palanca levantada y un hueco. ¿Está abierto o cerrado?", "Abierto", "El hueco corta el camino."),
  ],
  rea=[
      ("Carlos dice que el modelo del agua prueba que la corriente es agua en los cables. ¿Tiene razón? Responde Sí o No y explica.", "No; es solo una analogía", "En un cable no circula agua."),
      ("Un esquema tiene dos ampolletas sin pila. ¿Puede funcionar? Responde Sí o No y explica.", "No; falta la fuente de energía", "Sin pila no hay energía eléctrica."),
  ],
  cha=[
      ("Escribe dos límites de la analogía del agua.", "El agua se ve y la corriente no, y los cables no son tuberías", "Una analogía no es igual a la realidad."),
      ("Explica con el esquema por qué la ampolleta apaga al abrir el interruptor.", "Porque el círculo queda cortado y la corriente no puede pasar", "El camino completo es necesario."),
  ],
  context=[("Dato de ejemplo. Un esquema de una clase usa 1 pila, 1 interruptor, 1 ampolleta y 4 tramos de cable. ¿Cuántos símbolos o tramos tiene en total?", "7", "1 + 1 + 1 + 4 = 7.")],
  selfcheck=[("¿Qué es un esquema de circuito?", "Un dibujo con símbolos que muestra cómo se conecta", "Permite comunicar sin armar."), ("¿Qué muestra una línea cortada?", "Un circuito abierto", "No hay camino completo."), ("¿Qué límite tiene la analogía del agua?", "En un cable no se ve moverse nada", "La corriente no es agua.")],
  open_task=task("Dibuja el esquema de un circuito con pila, interruptor y ampolleta. Dibuja el interruptor abierto en un esquema y cerrado en otro. Escribe un párrafo corto que explique, siguiendo el camino, por qué la ampolleta enciende solo en uno de los dos. Agrega un límite del esquema.", "Esquema 1: interruptor abierto, la ampolleta no enciende porque el camino está cortado. Esquema 2: interruptor cerrado, el camino es un círculo y la ampolleta enciende. Límite: el esquema no muestra la corriente moviéndose.", ["dos esquemas con símbolos", "explicación del camino", "un límite"], ["dibujos", "párrafo"], ["dejar el círculo cortado sin querer", "olvidar el límite"], "Pregunta qué símbolo usó para cada pieza y cómo reconoce un circuito abierto."),
  reinforce="Dibuja el esquema de una linterna simple.",
  extend="Piensa en otra analogía para un circuito y escribe su límite.")

L(OA9, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar diseños de circuitos que resuelven un problema cotidiano. Sirve para elegir el diseño que funciona mejor.",
  prior=["Sé dibujar y leer un esquema de circuito.", "Sé que para comparar uso un mismo criterio."],
  explain=[
      "Los circuitos resuelven problemas cotidianos. Una linterna usa un circuito con interruptor para iluminar cuando se necesita. Un timbre usa un pulsador, que es un interruptor que cierra el circuito solo mientras se presiona. Una alarma de puerta puede usar un interruptor que se cierra cuando la puerta se abre, y así enciende una ampolleta.",
      "Para elegir el mejor diseño, definimos un criterio: ¿resuelve el problema? Por ejemplo, para encender una luz solo mientras se presiona, el diseño necesita un pulsador conectado en el camino. Si el pulsador está al lado sin conectar, no controla la luz. Se prueba cada diseño y se anota si la ampolleta enciende cuando debe y se apaga cuando debe.",
      "Una tabla con las columnas diseño, qué ocurre al presionar y qué ocurre al soltar ayuda a comparar. Las pruebas deben hacerse igual para todos los diseños. Y siempre con pilas, nunca con enchufes.",
  ],
  vocab=[("pulsador", "interruptor que cierra el circuito solo mientras se presiona"), ("diseño", "plan de cómo armar algo para resolver un problema"), ("problema cotidiano", "situación de la vida diaria que se quiere resolver"), ("criterio", "característica que se mira igual en todos los casos"), ("alarma", "aparato que avisa de algo")],
  worked=[
      ("Elegir el diseño", "Problema: una luz que solo enciende mientras se presiona. Diseño A: pulsador en el camino. Diseño B: pulsador al lado sin conectar. ¿Cuál resuelve el problema?", ["Reviso dónde está el pulsador.", "En A está en el camino.", "En B no controla nada."], "El diseño A"),
      ("Completar la tabla", "Diseño A: al presionar, la ampolleta ______; al soltar, se apaga.", ["El pulsador cierra el circuito al presionar.", "La corriente pasa.", "La ampolleta enciende."], "Enciende"),
  ],
  mistakes=[
      ("Poner el pulsador fuera del camino de la corriente.", "No corta ni cierra el circuito.", "Conéctalo en el camino."),
      ("Probar los diseños de distinta forma.", "No se pueden comparar bien.", "Prueba todos igual."),
  ],
  rec=[
      ("¿Un pulsador cierra el circuito solo mientras se presiona o siempre?", "Solo mientras se presiona", "Al soltar, el circuito se abre."),
      ("Un timbre necesita sonar al presionar. ¿Usa pulsador?", "Sí", "Cierra el circuito al presionar."),
      ("Completa con «problema» o «color»: un circuito sirve para resolver un ______ cotidiano.", "Problema", "Por ejemplo, iluminar o avisar."),
  ],
  und=[
      ("¿Por qué el diseño con el pulsador al lado no funciona?", "Porque no está en el camino de la corriente", "No controla el paso de electricidad."),
      ("¿Cuál criterio sirve para comparar diseños de una luz con pulsador? A) Si enciende al presionar y se apaga al soltar. B) El color de los cables.", "A", "Es lo que se necesita."),
      ("Una alarma de puerta se activa al abrir la puerta. ¿Qué pieza cambia el estado del circuito?", "El interruptor de la puerta", "Se cierra cuando la puerta se abre."),
  ],
  app=[
      arith("Dato de ejemplo. Se probaron 5 diseños y 3 resolvieron el problema. ¿Cuántos no lo resolvieron?", "5-3", "Se resta los que sirvieron al total."),
      ("Diseño de linterna: pila, ampolleta, interruptor y cables en un solo camino cerrado. ¿Resuelve el problema de iluminar a voluntad? Responde Sí o No.", "Sí", "El interruptor controla el paso."),
      ("Un diseño tiene dos pulsadores uno tras otro en el mismo camino. Para que la ampolleta encienda, ¿es necesario presionar los dos o uno solo?", "Los dos", "Si cualquiera está abierto, el camino queda cortado."),
  ],
  rea=[
      ("Marcos dice que la linterna sirve porque tiene una ampolleta. ¿Qué falta en su explicación?", "El interruptor y el camino cerrado", "Una ampolleta sola no basta."),
      ("Dos diseños de timbre: A suena siempre y B suena al presionar. ¿Cuál resuelve el problema de avisar solo cuando alguien llama?", "B", "A suena sin necesidad."),
  ],
  cha=[
      ("Escribe un problema cotidiano que se resuelva con un circuito y qué pieza usarías para controlarlo.", "Una luz de velador que se enciende con un interruptor", "El interruptor controla el paso de la corriente."),
      ("Un diseño enciende la ampolleta aunque el interruptor esté abierto. ¿Qué error probable tiene el armado?", "El interruptor no está conectado en el camino", "Hay otro camino cerrado."),
  ],
  context=[("Dato de ejemplo. Una clase probó 4 diseños con 3 pruebas cada uno. ¿Cuántas pruebas hicieron?", "12", "4 × 3 = 12.")],
  selfcheck=[("¿Para qué sirve un pulsador?", "Para cerrar el circuito solo mientras se presiona", "Se usa en timbres."), ("¿Qué criterio usaste para elegir el mejor diseño?", "Si resuelve el problema", "Se prueba cada diseño igual."), ("¿Con qué fuente se prueban los circuitos?", "Con pilas", "Nunca con enchufes.")],
  open_task=task("Elige uno de estos problemas: (1) una luz que enciende solo mientras presionas; (2) una luz que se enciende a voluntad. Dibuja el esquema de un circuito con pila, ampolleta y el interruptor o pulsador adecuado. Explica en tres frases cómo funciona y compara en una tabla tu diseño con uno que no funciona (por ejemplo, con la pieza fuera del camino). Si lo armas, usa una pila de 1,5 V y a una persona adulta.", "Problema 1: luz con pulsador. Esquema: pila, pulsador, ampolleta en un círculo. Funciona: al presionar se cierra el camino y enciende; al soltar se abre y apaga. Diseño que no funciona: pulsador al lado sin conectar.", ["esquema con las piezas", "explicación de tres frases", "comparación con un diseño que no funciona"], ["dibujo", "tabla"], ["poner el pulsador fuera del camino", "usar enchufes"], "Pregunta cómo supo que el diseño resolvía el problema y qué probó."),
  reinforce="Dibuja el esquema de una luz que se enciende con un interruptor.",
  extend="Explica cómo cambiarías el diseño para que dos ampolletas enciendan con un solo interruptor, sin armarlo.")

# ---------------------------------------------------------------- OA 10
L(OA10, 1,
  materials="Este cuaderno y lápiz. Los resultados de las pruebas están escritos en los ejercicios; si pruebas materiales, usa solo pila de 1,5 V con una persona adulta, nunca enchufes.",
  use="Aprenderé qué son los materiales conductores y aisladores y a leer los resultados de una prueba. Sirve para elegir materiales seguros.",
  prior=["Sé armar y leer un circuito simple.", "Sé separar observaciones de interpretaciones."],
  explain=[
      "Un material conductor deja pasar la corriente eléctrica. Los metales como el cobre y el aluminio son conductores. También lo es el hierro, que está en los clips y los clavos. Un material aislador no deja pasar la corriente. Los plásticos y la goma son aisladores. La madera seca, el papel y la tela también lo son.",
      "Para probar un material se arma un circuito con la pila y la ampolleta y se deja un hueco entre dos cables. Se pone el material en el hueco. Si la ampolleta enciende, el material es conductor. Si no enciende, es aislador. Esa es la observación. Decir «el plástico es el material más aburrido» es solo una opinión.",
      "Los resultados se anotan en una tabla: material, qué observaste y qué concluyes. Para comparar, todas las pruebas deben usar la misma pila y la misma ampolleta. Una prueba con pila no reemplaza las precauciones con la electricidad de la casa: nunca pruebes materiales con enchufes.",
  ],
  vocab=[("conductor", "material que deja pasar la corriente eléctrica"), ("aislador", "material que no deja pasar la corriente eléctrica"), ("cobre", "metal rojizo que conduce muy bien la electricidad"), ("aluminio", "metal liviano y plateado que conduce la electricidad"), ("goma", "material elástico que aísla de la electricidad")],
  worked=[
      ("Clasificar con los resultados", "Resultados de ejemplo: alambre de cobre, la ampolleta enciende; regla de plástico, no enciende. ¿Cuál es conductor?", ["Reviso en qué caso enciende.", "Con el cobre enciende.", "Con el plástico no enciende."], "El cobre es conductor y el plástico es aislador"),
      ("Observación o interpretación", "«Con el clip, la ampolleta encendió» y «El clip es el mejor material del mundo». ¿Cuál es observación?", ["Pregunto qué se vio.", "La ampolleta encendió.", "«El mejor» es una opinión."], "La primera frase"),
  ],
  mistakes=[
      ("Pensar que todos los materiales brillantes conducen.", "El brillo no decide; hay que probar.", "Usa el circuito de prueba."),
      ("Decir que el aislador deja pasar un poquito siempre.", "En esta prueba se clasifica según si la ampolleta enciende o no.", "Anota el resultado observado."),
  ],
  rec=[
      ("Un material que deja pasar la corriente, ¿es conductor o aislador?", "Conductor", "Así se define."),
      ("El cobre, ¿es conductor o aislador?", "Conductor", "Es un metal."),
      ("Completa con «enciende» o «no enciende»: si el material es aislador, la ampolleta ______.", "No enciende", "El aislador no deja pasar la corriente."),
  ],
  und=[
      ("¿Qué indica que la ampolleta encienda al poner un material en el hueco?", "Que el material es conductor", "Dejó pasar la corriente."),
      ("¿Por qué las pruebas usan siempre la misma pila y la misma ampolleta?", "Para que la comparación sea justa", "Si cambian, no se sabe la causa."),
      ("Marca la observación: A) Con el papel aluminio, la ampolleta enciende. B) El papel aluminio es muy lindo.", "A", "A se observa; B es opinión."),
  ],
  app=[
      ("Resultados de ejemplo: clip, enciende; goma, no enciende; aluminio, enciende; plástico, no enciende. ¿Cuántos materiales son conductores?", "2", "El clip y el aluminio."),
      arith("Dato de ejemplo. Se probaron 8 materiales y 5 fueron conductores. ¿Cuántos fueron aisladores?", "8-5", "Se resta los conductores al total."),
      ("Clasifica la goma de un borrador en conductor o aislador según esta clase.", "Aislador", "La goma no deja pasar la corriente."),
  ],
  rea=[
      ("Dani dice: «La madera es conductora porque es dura». ¿Tiene razón? Responde Sí o No y explica.", "No; la madera seca es aisladora y la dureza no decide", "La clasificación depende de si deja pasar la corriente."),
      ("Un compañero escribe: «El plástico es aislador porque no enciende la ampolleta». ¿Qué evidencia usó?", "La ampolleta no encendió", "Su conclusión se apoya en una observación."),
  ],
  cha=[
      ("Escribe una observación y una interpretación sobre una prueba con papel aluminio.", "Observación: la ampolleta enciende. Interpretación: el aluminio es un buen conductor", "La observación se ve; la interpretación explica."),
      ("Explica por qué nunca se prueban materiales con un enchufe.", "Porque la electricidad de la red es peligrosa", "Solo se usan pilas de baja energía."),
  ],
  context=[("Dato de ejemplo. Un curso probó 6 materiales en 4 grupos. ¿Cuántas pruebas hicieron en total?", "24", "6 × 4 = 24.")],
  selfcheck=[("¿Qué es un conductor?", "Un material que deja pasar la corriente", "Los metales lo son."), ("¿Qué es un aislador?", "Un material que no deja pasar la corriente", "El plástico y la goma lo son."), ("¿Con qué fuente se prueban materiales?", "Con pilas, nunca con enchufes", "La red es peligrosa.")],
  open_task=task("Con una persona adulta, si tienes pila de 1,5 V, ampolleta de linterna y cables, prueba cuatro materiales (por ejemplo, un clip, papel aluminio, una regla de plástico y un borrador de goma). Si no puedes, usa estos resultados de ejemplo: clip enciende, papel aluminio enciende, regla de plástico no enciende, borrador no enciende. Haz una tabla con material, observación y conclusión. Nunca uses enchufes.", "Clip: enciende, conductor. Papel aluminio: enciende, conductor. Regla de plástico: no enciende, aislador. Borrador de goma: no enciende, aislador.", ["tabla con cuatro materiales", "observación y conclusión separadas", "seguridad con pilas"], ["tabla", "frases"], ["usar enchufes", "decir que el brillo decide"], "Pregunta cómo supo si el material era conductor o aislador."),
  reinforce="Clasifica cinco objetos de tu casa como probables conductores o aisladores y di por qué.",
  extend="Explica por qué los cables de la casa tienen una parte de metal y otra de plástico.")

L(OA10, 2,
  materials="Este cuaderno y lápiz. Opcional, con una persona adulta: pila de 1,5 V, ampolleta de linterna, cables, clip, papel aluminio, regla de plástico y borrador de goma.",
  use="Aprenderé a predecir si un material conducirá o aislará y a comprobarlo. Sirve para decidir qué materiales usar en un circuito.",
  prior=["Sé qué son conductor y aislador.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una predicción sobre un material usa lo que sabes: los metales como el cobre, el aluminio y el hierro conducen; los plásticos, la goma, el papel y la tela aíslan. Por ejemplo: «La cuchara de metal conducirá, porque los metales conducen la electricidad». Una pregunta comprobable es: «¿Enciende la ampolleta si pongo un clip en el hueco del circuito?».",
      "Una buena prueba cambia una sola cosa, el material, y mantiene igual la pila, la ampolleta y los cables. Se anota la predicción antes y el resultado después. Si el resultado no coincide, se revisa: puede que el material tenga pintura o una cubierta que aísla, o que un contacto esté flojo.",
      "Esta prueba solo vale para una pila pequeña. No se debe usar para decidir si un objeto es seguro cerca de enchufes, porque en la red de la casa la electricidad es mucho más fuerte y la humedad cambia las cosas.",
  ],
  vocab=[("predicción", "lo que creo que pasará y por qué"), ("contacto", "unión entre dos piezas por donde puede pasar corriente"), ("cubierta", "capa que cubre un objeto"), ("variable", "lo que cambia en una prueba"), ("humedad", "agua presente en el aire o en un objeto")],
  worked=[
      ("Predecir un material", "Predice si una cuchara de metal conducirá la electricidad.", ["Es un metal.", "Los metales conducen.", "Escribo la predicción con razón."], "Conducirá, porque los metales conducen la electricidad"),
      ("Revisar un resultado inesperado", "Predijiste que una tijera de metal conduciría, pero no encendió. ¿Qué puede haber pasado?", ["Revisa si hay una cubierta.", "Los mangos de plástico aíslan.", "Puede que tocaste solo el mango."], "Probablemente el contacto fue con una parte aisladora"),
  ],
  mistakes=[
      ("Predecir sin razón: «conducirá porque sí».", "No se aprende cuando no hay razón.", "Escribe «porque…» con una propiedad del material."),
      ("Cambiar el material y la pila a la vez.", "No se sabe qué causó el resultado.", "Cambia solo el material."),
  ],
  rec=[
      ("¿Los metales conducen o aíslan?", "Conducen", "Los metales son conductores."),
      ("¿La goma conduce o aísla?", "Aísla", "Es un aislador."),
      ("Completa con «antes» o «después»: la predicción se escribe ______ de probar.", "Antes", "Es una idea previa."),
  ],
  und=[
      ("¿Por qué se cambia solo el material en la prueba?", "Para saber si el resultado depende del material", "Si cambian más cosas, no se sabe la causa."),
      ("¿Qué predicción tiene razón? A) El clip conducirá porque es de metal. B) El clip conducirá porque es pequeño.", "A", "El tamaño no decide; el material sí."),
      ("¿Qué puede impedir que un metal con pintura conduzca bien?", "La capa de pintura aísla", "Hay que tocar la parte sin pintura."),
  ],
  app=[
      ("Predice: ¿conducirá una regla de plástico? Responde Sí o No.", "No", "El plástico es aislador."),
      arith("Dato de ejemplo. Una niña predijo 6 materiales y acertó en 5. ¿En cuántos no acertó?", "6-5", "Se resta los aciertos al total."),
      ("Resultado de ejemplo: papel aluminio enciende la ampolleta. ¿Coincide con la predicción «el aluminio conduce»? Responde Sí o No.", "Sí", "El resultado confirma la predicción."),
  ],
  rea=[
      ("Hugo predijo que el clip conduciría pero no encendió. Dice: «Los metales no conducen». ¿Es una buena conclusión? Responde Sí o No y explica.", "No; puede haber un contacto flojo o pintura", "Hay que revisar la prueba antes de concluir."),
      ("Lía probó el clip una vez. ¿Qué le sugieres para confiar en el resultado?", "Repetir la prueba varias veces", "Una sola prueba puede fallar por un contacto flojo."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre un material y un circuito, indicando qué observarás.", "¿Enciende la ampolleta si pongo papel aluminio en el hueco?", "Nombra el material y lo que se observa."),
      ("Explica por qué no sirve predecir con «es bonito» o «es grande».", "Porque la conducción depende del material y no de su aspecto", "Hay que usar propiedades del material."),
  ],
  context=[("Dato de ejemplo. Un curso predijo 5 materiales en 6 grupos. ¿Cuántas predicciones hicieron?", "30", "5 × 6 = 30.")],
  selfcheck=[("¿Qué lleva una buena predicción?", "Lo que pasará y la razón", "Así se puede comprobar."), ("¿Qué materiales conducen?", "Los metales", "Por ejemplo cobre y aluminio."), ("¿Por qué repetir la prueba?", "Para confirmar el resultado", "Un contacto flojo puede engañar.")],
  open_task=task("Escribe tus predicciones, con razón, para estos cuatro materiales: cuchara de metal, tapa de plástico, goma de borrar y papel aluminio. Si puedes, con una persona adulta, pruébalos con pila de 1,5 V, ampolleta y cables. Si no, usa estos resultados de ejemplo: cuchara de metal enciende, tapa no, goma no, aluminio enciende. Compara tus predicciones con los resultados.", "Predicciones: cuchara conduce (metal), tapa no (plástico), goma no, aluminio conduce. Resultados de ejemplo: se cumplieron las cuatro.", ["cuatro predicciones con razón", "resultados anotados", "comparación"], ["tabla", "frase de comparación"], ["predecir sin razón", "probar con enchufes"], "Pregunta qué predicción fue más difícil y por qué."),
  reinforce="Predice cómo se comportará un clavo de hierro y explica por qué.",
  extend="Explica por qué un cable con pintura puede dar un resultado distinto en la prueba.")

L(OA10, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a usar un modelo de un cable por dentro y de un circuito de prueba, y a decir qué no muestran. Sirve para relacionar conductores y aisladores con los cables de la casa.",
  prior=["Sé qué materiales conducen y cuáles aíslan.", "Sé que un modelo tiene límites."],
  explain=[
      "Un cable eléctrico tiene dos partes. Por dentro lleva un metal conductor, como cobre o aluminio, por donde pasa la corriente. Por fuera tiene una cubierta de plástico o goma que aísla. Así, la corriente va por el metal y las personas están protegidas al tocar la cubierta.",
      "El circuito de prueba es un modelo del circuito de una casa. El hueco entre los dos cables es el lugar donde se conecta algo. Si lo que se pone en el hueco es conductor, se cierra el camino. Los enchufes también combinan materiales: las patas son metálicas para conducir y la carcasa es de plástico para proteger.",
      "El modelo tiene límites: la pila de prueba es de baja energía y la red de la casa es mucho más fuerte. Por eso un material que parece seguro en la prueba puede no serlo en la casa, sobre todo si está húmedo o dañado. Nunca se hacen pruebas con enchufes.",
  ],
  vocab=[("cubierta aisladora", "capa de plástico o goma que cubre el metal del cable"), ("pata del enchufe", "pieza metálica que entra en el tomacorriente"), ("carcasa", "parte de afuera de un aparato o enchufe"), ("tomacorriente", "lugar de la pared donde se conecta un enchufe"), ("daño", "rotura o desgaste de un cable")],
  worked=[
      ("Leer el modelo del cable", "Un cable tiene cobre por dentro y plástico por fuera. ¿Qué parte conduce y qué parte aísla?", ["El cobre es un metal.", "El plástico es un aislador.", "Cada parte hace su trabajo."], "El cobre conduce y el plástico aísla"),
      ("Encontrar un límite", "La pila de prueba es de baja energía y la red es mucho más fuerte. ¿Es un límite del modelo?", ["La pila no es la red de la casa.", "El modelo no muestra esa diferencia.", "Es algo real que queda fuera."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Creer que un cable con la cubierta rota sigue siendo seguro.", "Si la cubierta se rompe, el metal queda expuesto.", "No lo uses y avisa a una persona adulta."),
      ("Pensar que la prueba con pila sirve para decidir qué es seguro con enchufes.", "La red es mucho más fuerte.", "Nunca pruebes con enchufes."),
  ],
  rec=[
      ("¿Qué metal suele ir dentro de los cables: el cobre o el plástico?", "El cobre", "El plástico va por fuera."),
      ("¿La cubierta del cable es conductora o aisladora?", "Aisladora", "Protege a las personas."),
      ("Completa con «patas» o «cubierta»: las ______ del enchufe son de metal.", "Patas", "Conducen la corriente al tomacorriente."),
  ],
  und=[
      ("¿Por qué las patas del enchufe son metálicas?", "Para conducir la corriente", "Los metales son conductores."),
      ("¿Por qué la carcasa del enchufe es de plástico?", "Para proteger a las personas", "El plástico aísla."),
      ("¿Qué no muestra el circuito de prueba? A) La diferencia de energía con la red de la casa. B) La ampolleta que enciende.", "A", "La pila de prueba es mucho más débil."),
  ],
  app=[
      ("Un cable tiene 2 hilos de cobre y cada uno está cubierto de plástico. ¿Cuántas cubiertas aisladoras hay?", "2", "Una por cada hilo."),
      arith("Un esquema de cable tiene 3 partes dibujadas. Dibujaste 2. ¿Cuántas faltan?", "3-2", "Se resta lo dibujado al total."),
      ("Un tomacorriente tiene la carcasa rota. Con lo aprendido, ¿es seguro usarlo? Responde Sí o No.", "No", "Quedan partes de metal sin protección."),
  ],
  rea=[
      ("Tomás dice que un cable pelado es seguro si está apagado el artefacto. ¿Tiene razón? Responde Sí o No y explica.", "No; si está conectado, el metal puede dar descarga", "El cobre expuesto conduce la corriente."),
      ("Ema dice que el modelo prueba que todo el plástico es seguro siempre. ¿Qué corriges?", "Que el plástico aísla en la prueba, pero una cubierta dañada o mojada no protege", "El modelo no cubre los daños ni la humedad."),
  ],
  cha=[
      ("Escribe dos límites del modelo del cable con cubierta.", "No muestra la diferencia de energía con la red y no muestra el desgaste", "Un modelo simplifica."),
      ("Dibuja con palabras un cable y rotula conductor y aislador.", "Cobre por dentro (conductor) y plástico por fuera (aislador)", "Cada parte cumple una función distinta."),
  ],
  context=[("Dato de ejemplo. Una clase dibujó 6 cables con 2 partes rotuladas cada uno. ¿Cuántas partes rotularon?", "12", "6 × 2 = 12.")],
  selfcheck=[("¿Qué lleva un cable por dentro?", "Un metal conductor como el cobre", "Por ahí pasa la corriente."), ("¿Qué lleva por fuera?", "Una cubierta aisladora de plástico o goma", "Protege a las personas."), ("¿Qué límite tiene el modelo?", "Es de baja energía y no muestra la red de la casa", "Todo modelo simplifica.")],
  open_task=task("Dibuja un cable por dentro y por fuera, un enchufe y un tomacorriente. Rotula con colores los materiales conductores y los aisladores. Escribe dos límites de tu dibujo. No manipules enchufes ni cables conectados.", "Cable: cobre dentro (conductor, rojo) y plástico fuera (aislador, azul). Enchufe: patas de metal (rojo) y carcasa de plástico (azul). Límites: no muestra la diferencia de energía y no muestra el desgaste.", ["partes rotuladas con conductor o aislador", "dos límites", "no manipula artefactos conectados"], ["dibujo rotulado", "frases"], ["tocar cables conectados", "olvidar los límites"], "Pregunta por qué cada parte está hecha de ese material."),
  reinforce="Rotula qué parte de una extensión eléctrica es conductora y cuál aisladora.",
  extend="Explica por qué el mango de un destornillador suele ser de plástico.")

L(OA10, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar los resultados de las pruebas con un criterio común y a relacionarlos con la manipulación segura. Sirve para elegir materiales y conductas seguras.",
  prior=["Sé qué son conductores y aisladores.", "Sé que para comparar uso un mismo criterio."],
  explain=[
      "Para comparar materiales usamos un criterio común: si la ampolleta enciende. Los resultados de ejemplo de una prueba fueron: cobre, enciende; aluminio, enciende; clip de acero, enciende; plástico, no enciende; goma, no enciende; madera seca, no enciende. Con eso se forman dos grupos: conductores (cobre, aluminio, clip) y aisladores (plástico, goma, madera seca).",
      "Esta clasificación se relaciona con la manipulación segura. Las partes que debes tocar, como la cubierta de un cable o el mango de un destornillador, son aisladoras. Las partes metálicas, como las patas de un enchufe, son conductoras y no se tocan con el artefacto conectado. Por eso se desenchufa tomando el enchufe y no el cable, y no se usan artefactos con el cable dañado.",
      "Otras normas de seguridad son mantener las manos secas, no tocar enchufes ni cables pelados, no meter objetos en los tomacorrientes y avisar a una persona adulta si algo está roto. El agua y la humedad ayudan a que la electricidad pase por el cuerpo, por eso los artefactos eléctricos se mantienen lejos del agua.",
  ],
  vocab=[("clasificar", "ordenar en grupos según un criterio"), ("manipulación segura", "forma de usar algo sin riesgos"), ("desenchufar", "sacar el enchufe del tomacorriente"), ("dañado", "roto o gastado"), ("avisar", "comunicar a otra persona")],
  worked=[
      ("Clasificar con un criterio", "Resultados: cobre, enciende; goma, no enciende; clip, enciende; madera seca, no enciende. ¿Cuántos conductores hay?", ["El criterio es si enciende.", "Cobre y clip encienden.", "Goma y madera no."], "2 conductores"),
      ("Relacionar con la seguridad", "¿Por qué los mangos de las herramientas eléctricas son de plástico o goma?", ["El plástico y la goma son aisladores.", "Protegen las manos.", "Relaciono con el material."], "Porque aíslan y protegen a la persona"),
  ],
  mistakes=[
      ("Tirar del cable para desenchufar.", "Se puede dañar el cable y dejar el metal expuesto.", "Sostén el enchufe, no el cable."),
      ("Tocar un aparato eléctrico con las manos mojadas.", "El agua ayuda a que la electricidad pase por el cuerpo.", "Sécate las manos antes."),
  ],
  rec=[
      ("¿Qué criterio se usa para clasificar: si la ampolleta enciende o el color del material?", "Si la ampolleta enciende", "Es lo que se observa."),
      ("¿El mango de un destornillador debe ser conductor o aislador?", "Aislador", "Protege las manos."),
      ("Completa con «tomando el enchufe» o «tirando del cable»: se desenchufa ______.", "Tomando el enchufe", "Así no se daña el cable."),
  ],
  und=[
      ("¿Por qué se mantienen las manos secas al usar aparatos eléctricos?", "Porque el agua ayuda a que la electricidad pase por el cuerpo", "La humedad aumenta el riesgo."),
      ("¿Qué grupo forman cobre, aluminio y clip?", "Conductores", "Dejaron encender la ampolleta."),
      ("¿Qué debe hacer una persona si ve un cable con la cubierta rota? A) Avisar a una persona adulta. B) Arreglarlo con cinta.", "A", "La reparación la hace una persona capacitada."),
  ],
  app=[
      arith("Dato de ejemplo. Se probaron 12 materiales y 7 fueron conductores. ¿Cuántos fueron aisladores?", "12-7", "Se resta los conductores al total."),
      ("Clasifica la madera seca como conductor o aislador según los resultados de ejemplo.", "Aislador", "No encendió la ampolleta."),
      ("De estas conductas, ¿cuántas son seguras: desenchufar tomando el enchufe, tocar el enchufe con manos mojadas, avisar de un cable roto?", "2", "La primera y la tercera."),
  ],
  rea=[
      ("Ana dice que como el plástico aísla en la prueba, un cable con plástico roto es seguro. ¿Tiene razón? Responde Sí o No y explica.", "No; si el plástico se rompe, el metal queda expuesto", "La protección depende de que la cubierta esté sana."),
      ("Rafa compara el cobre con el plástico pero usó una pila distinta en cada prueba. ¿Qué problema tiene su comparación?", "No usó el mismo criterio y condiciones", "Debe usar la misma pila y ampolleta."),
  ],
  cha=[
      ("Escribe una conclusión con los resultados de ejemplo: cobre, aluminio y clip encienden; plástico, goma y madera no.", "Los metales conducen y los plásticos, la goma y la madera seca aíslan", "Agrupa según el mismo criterio."),
      ("Escribe una norma de seguridad en casa y la razón.", "No meter objetos en los tomacorrientes, porque pueden conducir la corriente y dar una descarga", "La razón une el material con el riesgo."),
  ],
  context=[("Dato de ejemplo. Un curso clasificó 6 materiales en 5 grupos de trabajo. ¿Cuántas clasificaciones hicieron?", "30", "6 × 5 = 30.")],
  selfcheck=[("¿Qué criterio permite clasificar los materiales?", "Si la ampolleta enciende", "Se observa en la prueba."), ("¿Cómo se desenchufa de forma segura?", "Tomando el enchufe", "Así no se daña el cable."), ("¿Por qué evitar el agua cerca de aparatos eléctricos?", "Porque ayuda a que la electricidad pase por el cuerpo", "Aumenta el riesgo.")],
  open_task=task("Haz una tabla con seis materiales (cobre, aluminio, clip, plástico, goma, madera seca) y su resultado de ejemplo (enciende o no enciende). Clasifícalos en conductores y aisladores. Después escribe tres normas de seguridad con electricidad y la razón de cada una. No manipules artefactos conectados.", "Conductores: cobre, aluminio, clip. Aisladores: plástico, goma, madera seca. Normas: manos secas, porque el agua ayuda a conducir; desenchufar tomando el enchufe, para no dañar el cable; avisar de un cable roto, porque el metal queda expuesto.", ["tabla de seis materiales", "dos grupos", "tres normas con razón"], ["tabla", "lista de normas"], ["probar con enchufes", "normas sin razón"], "Pregunta cuál norma practica más en su casa y qué otra agregaría."),
  reinforce="Escribe dos normas de seguridad con enchufes y la razón de cada una.",
  extend="Explica por qué los electricistas usan herramientas con mango aislador.")

L(OA10, 5,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a explicar con evidencia por qué algunos materiales conducen y otros aíslan, y a reconocer los límites de las pruebas. Sirve para tomar decisiones seguras en casa.",
  prior=["Sé clasificar materiales y conocer normas de seguridad.", "Sé que una explicación necesita evidencia."],
  explain=[
      "Una buena explicación une un material, el resultado de la prueba y una decisión de seguridad. Por ejemplo: «El cobre conduce porque la ampolleta encendió; por eso se usa dentro de los cables. El plástico aísla porque no encendió; por eso se usa como cubierta». La evidencia son las observaciones de la prueba.",
      "En la vida diaria, los conductores y aisladores se combinan: en un enchufe, en un cable, en un destornillador y en las herramientas de un electricista. La elección de los materiales explica por qué un artefacto es seguro cuando está en buen estado.",
      "Los límites son importantes. La prueba con una pila pequeña no es lo mismo que la electricidad de la casa. La humedad y los daños cambian la seguridad de un aislador. Además, no todos los materiales se probaron. Para decisiones de seguridad real, se sigue la orientación de personas capacitadas y las normas de la casa y la escuela.",
  ],
  vocab=[("explicación", "relato que dice qué pasa y por qué"), ("evidencia", "dato que apoya una explicación"), ("límite", "lo que la evidencia no puede mostrar"), ("decisión de seguridad", "acción para evitar riesgos"), ("capacitado", "formado para hacer un trabajo con seguridad")],
  worked=[
      ("Completar una explicación", "Completa: «El plástico se usa como cubierta porque ______ la corriente».", ["Pienso en el resultado de la prueba.", "No encendió la ampolleta.", "El plástico aísla."], "Aísla"),
      ("Evidencia y límite", "En la prueba, el cobre hizo encender la ampolleta. ¿Qué evidencia hay y qué límite tiene?", ["Hay una observación: encendió.", "La prueba usó una pila pequeña.", "No dice nada de la red de la casa."], "Evidencia: la ampolleta encendió. Límite: no sirve para decidir seguridad con enchufes"),
  ],
  mistakes=[
      ("Afirmar que un material es siempre seguro.", "Un daño o la humedad cambian su seguridad.", "Di «mientras esté en buen estado y seco»."),
      ("Dar una explicación sin evidencia.", "No se puede comprobar.", "Nombra la observación de la prueba."),
  ],
  rec=[
      ("¿El cobre se usa dentro de los cables porque conduce o porque aísla?", "Porque conduce", "Deja pasar la corriente."),
      ("¿La cubierta de plástico del cable protege porque conduce o porque aísla?", "Porque aísla", "Evita que la corriente pase a las personas."),
      ("Completa con «evidencia» o «gusto»: una explicación se apoya en ______.", "Evidencia", "Los datos sostienen la explicación."),
  ],
  und=[
      ("¿Qué evidencia apoya que el aluminio conduce?", "Que la ampolleta encendió al probarlo", "Es una observación de la prueba."),
      ("¿Por qué una prueba con pila tiene límites?", "Porque no es igual a la electricidad de la casa", "La red es mucho más fuerte."),
      ("¿Qué frase está mejor explicada? A) El plástico aísla porque la ampolleta no encendió. B) El plástico aísla porque es azul.", "A", "A usa evidencia."),
  ],
  app=[
      ("Ordena la explicación: A) por eso se usa como cubierta, B) el plástico no hizo encender la ampolleta, C) el plástico es aislador. Escribe el orden.", "B, C, A", "Evidencia, conclusión y uso."),
      arith("Dato de ejemplo. Un grupo probó 9 materiales en total y 3 resultaron conductores. ¿Cuántos resultaron aisladores?", "9-3", "Se resta los conductores al total."),
      ("Un cable tiene la cubierta mojada y rota. ¿Qué haces: usarlo o avisar a una persona adulta?", "Avisar a una persona adulta", "El cable está dañado y la humedad aumenta el riesgo."),
  ],
  rea=[
      ("Un afiche dice: «Este cable es 100 % seguro para siempre». ¿Por qué no es una afirmación con evidencia?", "Porque la seguridad depende de que no esté dañado ni mojado", "Ningún material es seguro en cualquier condición."),
      ("Luis dice que como el cobre conduce, hay que tocar los cables de cobre para comprobarlo. ¿Qué respondes?", "Nunca se tocan cables conectados; se prueba con pila y con ayuda adulta", "Tocar cables conectados es peligroso."),
  ],
  cha=[
      ("Escribe una explicación de tres frases sobre un enchufe: qué es conductor, qué es aislador y por qué.", "Las patas son de metal y conducen; la carcasa es de plástico y aísla; así la corriente llega al aparato y protege a la persona", "Une materiales y funciones."),
      ("Escribe un límite de las pruebas de conductores y aisladores de esta clase.", "Se hicieron con una pila pequeña y no con la electricidad de la casa", "No sirve para decidir la seguridad de un enchufe."),
  ],
  context=[("Dato de ejemplo. Un grupo escribió 3 normas de seguridad para cada una de 4 situaciones del hogar. ¿Cuántas normas escribió?", "12", "3 × 4 = 12.")],
  selfcheck=[("¿Qué incluye una buena explicación?", "Material, resultado de la prueba y decisión de seguridad", "Une evidencia y uso."), ("¿Qué no puede decirte la prueba con pila?", "Si un objeto es seguro con la electricidad de la casa", "La red es mucho más fuerte."), ("¿Qué haces ante un cable dañado?", "Avisar a una persona adulta", "No lo tocas ni lo arreglas.")],
  open_task=task("Elige un artefacto de tu casa con cable (por ejemplo, un cargador o una lámpara). Sin tocar nada conectado, escribe una explicación de cinco frases: qué parte del cable es conductora, cuál aisladora, qué evidencia de la prueba lo apoya, una norma de seguridad con su razón y un límite de tu explicación.", "Lámpara: el cable tiene cobre por dentro, que conduce porque en la prueba la ampolleta encendió. La cubierta de plástico aísla porque no encendió. Norma: no tocar el cable si está pelado, porque el metal queda expuesto. Límite: la prueba usó una pila y no la red.", ["conductor y aislador identificados", "evidencia de la prueba", "norma con razón y un límite"], ["texto de cinco frases"], ["tocar artefactos conectados", "olvidar el límite"], "Pregunta qué parte es evidencia y qué parte es consejo de seguridad."),
  reinforce="Explica en una frase por qué el cobre se usa dentro de los cables.",
  extend="Explica por qué un cable mojado y roto es peligroso aunque el plástico sea aislador.")

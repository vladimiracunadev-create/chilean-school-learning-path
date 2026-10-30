"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 01 (ecosistemas), OA 02 (adaptaciones) y OA 03 (cadenas alimentarias de Chile)."""
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


OA1, OA2, OA3 = "CN04 OA 01", "CN04 OA 02", "CN04 OA 03"

# ---------------------------------------------------------------- OA 01
L(OA1, 1,
  materials="Este cuaderno y lápiz. Si quieres, un rincón de tu casa, una plaza o una maceta para mirar sin tocar animales ni arrancar plantas.",
  use="Aprenderé qué es un ecosistema y a separar lo que veo de lo que supongo. Sirve para describir un lugar natural con datos y no con ideas sueltas.",
  prior=["Sé que las plantas y los animales son seres vivos.", "Sé anotar lo que observo con ojos, regla o conteo."],
  explain=[
      "Un ecosistema es un lugar donde seres vivos y cosas no vivas conviven e interactúan. Interactuar es afectarse unos a otros. Una laguna, un bosque, un desierto y una playa son ecosistemas. También lo es un jardín pequeño.",
      "Los componentes vivos son plantas, animales, hongos y otros seres que nacen, crecen, se alimentan y se reproducen. Los componentes no vivos son, por ejemplo, el agua, las piedras, la tierra, el aire y la luz del Sol. No nacen ni crecen, pero los seres vivos dependen de ellos.",
      "Al explorar un ecosistema, primero anotas observaciones: lo que ves, oyes o cuentas, como «hay 3 piedras y 5 hormigas». Una interpretación es lo que supones sin verlo, como «las hormigas viven aquí porque están felices». Solo las observaciones son evidencia.",
  ],
  vocab=[("ecosistema", "lugar donde seres vivos y componentes no vivos interactúan"), ("componente vivo", "ser que nace, crece, se alimenta y se reproduce"), ("componente no vivo", "elemento del ambiente que no nace ni crece, como el agua o una piedra"), ("interactuar", "afectarse unos a otros"), ("interpretación", "lo que supongo sin haberlo visto")],
  worked=[
      ("Clasificar componentes", "En una laguna hay: patos, agua, juncos, barro y peces. ¿Cuáles son vivos y cuáles no vivos?", ["Pregunto de cada uno: ¿nace, crece y se alimenta?", "Patos, juncos y peces cumplen eso.", "Agua y barro no nacen ni crecen."], "Vivos: patos, juncos y peces. No vivos: agua y barro"),
      ("Observación o interpretación", "Una niña escribe: «Vi 4 piedras junto al agua» y «Los patos están contentos de vivir aquí». ¿Cuál es evidencia?", ["Reviso qué frase se puede contar o ver.", "Las 4 piedras se pueden contar.", "«Contentos» es lo que ella supone."], "Es evidencia «Vi 4 piedras junto al agua»"),
  ],
  mistakes=[
      ("Decir que el agua es un ser vivo porque se mueve.", "Moverse no basta: el agua no nace, no crece ni se alimenta.", "Usa las tres preguntas: ¿nace?, ¿crece?, ¿se alimenta?"),
      ("Anotar «el bosque es triste» como observación.", "Es un sentimiento puesto por quien mira, no un dato.", "Anota lo que ves: «hay pocas hojas verdes»."),
  ],
  rec=[
      ("¿Una piedra es un componente vivo o no vivo?", "No vivo", "La piedra no nace, no crece ni se alimenta."),
      ("¿Una planta es un componente vivo o no vivo?", "Vivo", "La planta nace, crece y fabrica su alimento."),
      ("Completa con «vivos» o «no vivos»: en un ecosistema hay componentes ______ y componentes no vivos.", "Vivos", "El ecosistema incluye ambos tipos de componentes."),
  ],
  und=[
      ("Un jardín tiene pasto, lombrices, tierra, mariposas y aire. ¿Cuántos componentes son vivos?", "3", "Pasto, lombrices y mariposas son vivos; tierra y aire no."),
      ("Marca la observación: A) Hay 6 hojas amarillas en el suelo. B) Estas hojas están enojadas con el viento.", "A", "A se puede contar; B es una idea inventada."),
      ("¿Por qué la luz del Sol es un componente no vivo importante para un ecosistema?", "Porque las plantas la necesitan para fabricar su alimento", "Aunque no está viva, los seres vivos dependen de ella."),
  ],
  app=[
      arith("En una charca contaste 7 renacuajos, 5 caracoles y 3 plantas acuáticas. ¿Cuántos seres vivos contaste en total?", "7+5+3", "Se suman todos los seres vivos contados."),
      ("Una playa tiene arena, olas, gaviotas, algas y sol. Escribe cuántos son no vivos.", "3", "Arena, olas (agua) y sol no son seres vivos; gaviotas y algas sí."),
      ("Ordena con letras: A) Anoto lo que veo. B) Miro el lugar con cuidado. C) Separo lo que supuse. ¿Cuál es el orden más lógico?", "B, A, C", "Se mira, se anota y recién después se revisa qué fue suposición."),
  ],
  rea=[
      ("Tomás dice: «El tronco caído está muerto, así que no importa para el bosque». Un hongo crece sobre él. ¿Tiene razón? Responde Sí o No y explica.", "No; el tronco es refugio y soporte de seres vivos como el hongo", "Un componente sin vida igual interactúa con los seres vivos."),
      ("Una niña anota: «Hay 2 lagartijas sobre la piedra». Otro anota: «La piedra es el hogar favorito de las lagartijas». ¿Quién dio evidencia?", "La primera niña", "Contó lo que vio; el otro afirmó una idea que no vio."),
  ],
  cha=[
      ("Un acuario cerrado tiene peces, plantas, agua y arena. ¿Es un ecosistema pequeño? Responde Sí o No y nombra un componente vivo y uno no vivo.", "Sí; peces (vivo) y agua (no vivo)", "Hay seres vivos y no vivos que interactúan."),
      ("Escribe una observación y una interpretación sobre una maceta con una planta de hojas caídas.", "Observación: las hojas están caídas y la tierra se ve seca. Interpretación: la planta tiene sed", "La observación se ve; la interpretación es una suposición."),
  ],
  context=[("En una plaza una niña anota: 12 hormigas, 2 árboles, 1 banca de madera, 1 charco y 4 palomas. Usando solo lo que anotó, ¿cuántos seres vivos contó?", "18", "Hormigas 12 + árboles 2 + palomas 4 = 18. La banca y el charco no son seres vivos.")],
  selfcheck=[("¿Qué es un ecosistema?", "Un lugar donde seres vivos y componentes no vivos interactúan", "Reúne componentes vivos y no vivos que se afectan."), ("Nombra dos componentes no vivos.", "Dos entre agua, tierra, piedras, aire o luz del Sol", "No nacen ni crecen."), ("¿Una interpretación es evidencia? Responde Sí o No.", "No", "Es una suposición, no algo visto o medido.")],
  open_task=task("Mira con una persona de tu casa un lugar: una maceta, un patio o una plaza cercana. No toques animales ni arranques plantas. Haz una tabla de dos columnas: «vivos» y «no vivos», con al menos tres componentes en cada una. Después escribe una observación y una interpretación sobre el lugar.", "Patio: vivos, pasto, hormigas, un limonero. No vivos: tierra, piedras, agua de la regadera. Observación: hay 8 hormigas junto a una piedra. Interpretación: les gusta la piedra.", ["tabla con tres vivos y tres no vivos", "una observación que se pueda contar o ver", "una interpretación marcada como suposición"], ["tabla completa", "dos frases rotuladas"], ["poner al agua o al viento entre los seres vivos", "anotar sentimientos como observaciones"], "Pregunta cómo supo que algo era vivo y cuál frase sería distinta si otra persona mirara el mismo lugar."),
  reinforce="Escribe seis cosas que veas por la ventana y marca cuáles son vivas y cuáles no.",
  extend="Describe un ecosistema distinto del que miraste (por ejemplo un desierto) y anota dos componentes vivos y dos no vivos que esperarías encontrar.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. Opcional: una maceta con una planta de tu casa y una regadera.",
  use="Aprenderé a hacer preguntas y predicciones sobre cómo interactúan los componentes de un ecosistema. Sirve para pensar qué pasa en un lugar cuando algo cambia.",
  prior=["Sé que un ecosistema tiene componentes vivos y no vivos.", "Sé que una predicción se hace antes de comprobar."],
  explain=[
      "Los componentes de un ecosistema se afectan unos a otros. La planta toma agua de la tierra y energía de la luz. El caracol come hojas. La lombriz vive en la tierra y la deja suelta. Cada relación es una interacción entre algo vivo y algo vivo, o entre algo vivo y algo no vivo.",
      "Una pregunta comprobable se puede responder observando o midiendo: «¿Cuántas hojas se comen los caracoles en dos días?». «¿Es bonito el bosque?» no sirve. Una predicción es lo que creo que pasará y debe decir por qué: «Si no hay luz, la planta se pondrá pálida porque la necesita».",
      "Para comprobar una predicción cambio una sola cosa y dejo lo demás igual. Anoto antes y después. Si el resultado no coincide con mi predicción, no fracasé: aprendí algo y puedo corregir mi idea.",
  ],
  vocab=[("interacción", "relación en que un componente afecta a otro"), ("pregunta comprobable", "pregunta que se responde observando o midiendo"), ("predicción", "lo que creo que pasará y por qué"), ("variable", "lo que puede cambiar en una prueba"), ("comprobar", "revisar con observaciones si una idea es cierta")],
  worked=[
      ("Elegir la pregunta comprobable", "¿Cuál sirve? A) ¿Es linda una laguna? B) ¿Cuántos renacuajos hay en 1 balde de agua de charca y en otro sin plantas?", ["Pienso si puedo contar o medir.", "En B puedo contar renacuajos.", "En A cada persona opina distinto."], "B"),
      ("Hacer una predicción con razón", "Una planta de una maceta se deja en un armario cerrado una semana. Haz una predicción.", ["Recuerdo qué necesita la planta: luz.", "Sin luz no puede fabricar alimento.", "Escribo qué verá y por qué."], "Las hojas se pondrán pálidas, porque sin luz la planta no fabrica su alimento"),
  ],
  mistakes=[
      ("Hacer una predicción sin razón: «pasará algo».", "No se puede comprobar ni aprender de ella.", "Di qué pasará y por qué, usando lo que sabes."),
      ("Cambiar luz y agua a la vez en la prueba.", "No sabrás cuál causó el cambio.", "Cambia una sola variable y deja igual lo demás."),
  ],
  rec=[
      ("¿Una predicción se hace antes o después de comprobar?", "Antes", "Es una idea previa que luego se pone a prueba."),
      ("¿El agua es un componente vivo o no vivo?", "No vivo", "El agua no nace ni crece."),
      ("Completa con «cuenta» o «opina»: una pregunta comprobable se responde cuando se ______ o se mide.", "Cuenta", "Un dato contado o medido permite responder."),
  ],
  und=[
      ("¿Cuál es una interacción entre un ser vivo y uno no vivo? A) La planta toma agua del suelo. B) Un caracol come una hoja.", "A", "En A participan una planta (viva) y el agua (no viva); en B los dos son vivos."),
      ("¿Cuál pregunta se puede comprobar? A) ¿Cuánto crece una planta en 5 días con luz? B) ¿Qué planta es más simpática?", "A", "El crecimiento se puede medir en centímetros."),
      ("¿Por qué conviene cambiar una sola variable en una prueba?", "Para saber cuál produjo el cambio", "Si cambian dos, no se sabe cuál fue la causa."),
  ],
  app=[
      arith("Una planta medía 8 cm al inicio y 14 cm después de una semana con luz. ¿Cuántos centímetros creció?", "14-8", "Se resta la altura inicial a la final."),
      ("Un niño pone dos plantas iguales en el mismo lugar. A una la riega cada día y a la otra no. ¿Qué variable cambia?", "El agua", "Lo único distinto es el riego."),
      ("Predice: en una charca desaparece la mitad de las plantas acuáticas que comen los renacuajos. ¿Habrá más o menos alimento para ellos? Escribe «más» o «menos».", "Menos", "Hay menos plantas que comer."),
  ],
  rea=[
      ("Ema predice: «Si dejo un caracol una noche en una caja con 4 hojas de lechuga, mañana habrá menos hojas enteras, porque el caracol come hojas». ¿Es una predicción comprobable? Responde Sí o No y explica.", "Sí; se pueden contar las hojas enteras antes y después", "Se compara lo que hay antes y después, y la predicción trae su razón."),
      ("Luis puso una planta junto a la ventana y otra en un armario, pero a la del armario no la regó. Ella se secó. Dice: «Fue por la falta de luz». ¿Lo puede asegurar?", "No; cambiaron la luz y el agua a la vez", "Con dos cambios no se sabe cuál causó el resultado."),
  ],
  cha=[
      ("Una planta y un caracol están en un terrario cerrado con tierra húmeda. Predice qué pasará si retiras al caracol y por qué.", "Habrá más hojas enteras porque nadie las come", "El caracol se alimenta de hojas, así que sin él hay menos hojas comidas."),
      ("Escribe una pregunta comprobable sobre cómo afecta el agua a una planta, indicando qué medirás.", "¿Cuántos centímetros crece una planta regada cada día en una semana?", "Nombra qué se cambia y qué se mide."),
  ],
  context=[("En una maceta dos plantas iguales miden 5 cm. Una recibe agua cada día y la otra no. A los 6 días la primera mide 11 cm y la segunda 7 cm. ¿Cuántos centímetros más creció la regada?", "4", "La regada creció 6 cm y la otra 2 cm, y 6 − 2 = 4.")],
  selfcheck=[("¿Qué debe tener una buena predicción?", "Lo que pasará y la razón", "Así puede comprobarse y aprenderse de ella."), ("¿Qué significa interactuar?", "Afectarse unos a otros", "Los componentes de un ecosistema se influyen."), ("Si el resultado no coincide con la predicción, ¿qué haces?", "Corregir la idea con lo aprendido", "La evidencia manda sobre la suposición.")],
  open_task=task("Con una persona de tu casa, elige una maceta o una planta de tu casa. Escribe una pregunta comprobable sobre la luz o el agua, tu predicción con su razón y qué vas a medir durante cuatro días (por ejemplo, altura o color). No arranques la planta ni la dejes sin agua más de una semana.", "Pregunta: ¿Se mantiene verde una hoja si la planta está en un lugar con poca luz? Predicción: se pondrá pálida porque necesita luz. Mediré el color cada día: día 1 verde, día 4 verde claro.", ["pregunta comprobable", "predicción con razón", "tabla de cuatro días"], ["pregunta escrita", "tabla con fechas"], ["cambiar dos variables a la vez", "predecir sin dar razón"], "Pregunta qué cambió, qué quedó igual y si el resultado confirmó su predicción."),
  reinforce="Escribe una predicción con razón sobre qué le pasa a una planta de interior si se riega en exceso, y una forma de comprobarla.",
  extend="Escribe una pregunta comprobable sobre cómo interactúan una piedra y un animal pequeño, como una hormiga o un bicho bolita, sin tocarlos.")

L(OA1, 3,
  materials="Este cuaderno, lápiz y regla. Opcional: lupa y observar sin tocar animales.",
  use="Aprenderé a comparar dos ecosistemas con un mismo criterio. Sirve para encontrar parecidos y diferencias con datos y no con impresiones.",
  prior=["Sé separar componentes vivos y no vivos.", "Sé leer una tabla simple."],
  explain=[
      "Para comparar dos ecosistemas usamos un criterio, que es la característica que miramos en los dos. Por ejemplo: cuántos tipos de seres vivos hay, cuánta agua hay o cuánta luz llega. Si cambio de criterio a mitad de camino, la comparación pierde sentido.",
      "Una tabla ayuda a ordenar. En una fila ponemos el criterio y en las columnas cada ecosistema. Así vemos a simple vista dónde hay más y dónde hay menos. Un desierto tiene poca agua y pocos tipos de plantas. Un bosque húmedo tiene más agua y muchos tipos de plantas.",
      "También comparo las interacciones: en la laguna los patos comen plantas del agua; en el bosque los pájaros anidan en los árboles. Aunque los ecosistemas sean distintos, en todos hay seres vivos y componentes no vivos que se afectan. Los datos de una tabla valen solo para ese día y ese lugar.",
  ],
  vocab=[("criterio", "característica que se mira igual en todos los casos que se comparan"), ("comparar", "buscar parecidos y diferencias con un mismo criterio"), ("tabla", "cuadro de filas y columnas para ordenar datos"), ("desierto", "ecosistema con muy poca lluvia"), ("humedad", "cantidad de agua presente en el aire o la tierra")],
  worked=[
      ("Comparar con un criterio", "Datos de ejemplo. Laguna: 6 tipos de seres vivos. Desierto: 2 tipos de seres vivos. ¿Cuántos tipos más tiene la laguna?", ["El criterio es «tipos de seres vivos».", "Miro el valor de cada ecosistema.", "Resto 6 − 2."], "4 tipos más"),
      ("Encontrar un parecido", "Laguna: patos, juncos, agua, barro. Desierto: lagartijas, cactus, arena, roca. ¿Qué tienen en común ambos?", ["Reviso la lista de cada ecosistema.", "Ambos tienen seres vivos.", "Ambos tienen componentes no vivos."], "Los dos tienen seres vivos y componentes no vivos"),
  ],
  mistakes=[
      ("Comparar tamaños en uno y colores en otro.", "No hay un criterio común.", "Elige un solo criterio y mídelo en los dos casos."),
      ("Decir «el desierto no es un ecosistema porque tiene pocos seres vivos».", "Basta con que haya seres vivos y no vivos que interactúan.", "Revisa que haya componentes vivos y no vivos."),
  ],
  rec=[
      ("¿Un criterio se usa en uno de los casos o en todos los casos comparados?", "En todos", "Si no, no se podría comparar."),
      ("Ecosistema A tiene 9 plantas. Ecosistema B tiene 4 plantas. ¿Cuál tiene más?", "A", "9 es mayor que 4."),
      ("Completa con «igual» o «distinto»: para comparar mido el criterio de manera ______ en los dos.", "Igual", "La medición debe ser la misma."),
  ],
  und=[
      ("Un bosque y un desierto se comparan según su cantidad de lluvia. ¿Cuál es el criterio?", "La cantidad de lluvia", "Es lo que se mira en ambos."),
      ("¿Qué comparación tiene un criterio común? A) Contar animales en el bosque y medir agua en el desierto. B) Contar animales en el bosque y en el desierto.", "B", "En B se mide lo mismo en ambos."),
      ("¿Por qué el desierto es un ecosistema aunque tenga pocas plantas?", "Porque tiene seres vivos y no vivos que interactúan", "La definición no pide muchos seres vivos."),
  ],
  app=[
      arith("Datos de ejemplo. Laguna: 12 seres vivos contados. Playa: 7 seres vivos contados. ¿Cuántos más hay en la laguna?", "12-7", "Se resta el valor menor al mayor."),
      arith("Datos de ejemplo. Bosque: 8 plantas y 10 animales. ¿Cuántos seres vivos se contaron en total?", "8+10", "Se suman plantas y animales."),
      ("Datos de ejemplo. Charca A: 15 renacuajos. Charca B: 9 renacuajos. ¿Qué charca tiene menos?", "Charca B", "9 es menor que 15."),
  ],
  rea=[
      ("Ana cuenta 10 insectos en el patio de día, y Beto cuenta 4 insectos en la plaza de noche. Ana dice que su patio tiene más. ¿La comparación es justa? Responde Sí o No y explica.", "No; contaron en horas distintas", "El momento del conteo debe ser el mismo."),
      ("Quieres comparar una laguna y un desierto. ¿Qué criterio sirve? A) La cantidad de agua que hay en cada uno. B) Cuál te gusta más.", "A", "La cantidad de agua se puede medir en los dos."),
  ],
  cha=[
      ("Un niño dice: «El bosque es mejor ecosistema que la playa». ¿Por qué esa frase no es una comparación científica?", "Porque «mejor» no es un criterio medible", "Falta una característica que se pueda contar o medir."),
      ("Datos de ejemplo. Bosque: 6 tipos de plantas y 5 de animales. Desierto: 2 de plantas y 3 de animales. ¿Cuántos tipos de seres vivos más tiene el bosque?", "6", "Bosque: 11 tipos. Desierto: 5 tipos. Diferencia: 11 − 5 = 6."),
  ],
  context=[("Datos de ejemplo. Una escuela compara la plaza y el patio. Plaza: 3 árboles, 20 hormigas y 5 palomas. Patio: 1 árbol, 12 hormigas y 2 palomas. ¿Cuántos seres vivos más contaron en la plaza?", "13", "Plaza: 28. Patio: 15. Diferencia: 28 − 15 = 13.")],
  selfcheck=[("¿Qué es un criterio de comparación?", "Una característica que se mira igual en todos los casos", "Permite comparar con justicia."), ("¿Qué tienen en común todos los ecosistemas?", "Seres vivos y componentes no vivos que interactúan", "Es la definición de ecosistema."), ("¿Para qué sirve una tabla?", "Para ordenar los datos y compararlos", "Muestra dónde hay más y dónde hay menos.")],
  open_task=task("Compara dos lugares cercanos a tu casa, por ejemplo una maceta y un patio, o dos plazas. Usa un solo criterio: cantidad de tipos de seres vivos que ves en 5 minutos. Haz una tabla con dos columnas y escribe dos parecidos y dos diferencias. No toques animales ni arranques plantas.", "Plaza: 4 tipos (árbol, pasto, paloma, hormiga). Patio: 3 tipos (pasto, hormiga, planta en maceta). Parecidos: ambos tienen pasto y hormigas. Diferencias: solo la plaza tiene palomas.", ["un criterio común", "tabla con datos de dos lugares", "dos parecidos y dos diferencias"], ["tabla", "lista de parecidos y diferencias"], ["usar dos criterios", "mirar un lugar más tiempo que el otro"], "Pregunta qué criterio usó y si mirar otro día cambiaría el resultado."),
  reinforce="Compara con una tabla dos objetos de tu casa usando un solo criterio, por ejemplo su peso aproximado.",
  extend="Escribe dos criterios distintos para comparar un desierto y un bosque y di cuál te parece más fácil de medir.")

L(OA1, 4,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a hacer un modelo de un ecosistema con flechas y a decir qué no muestra. Sirve para explicar cómo se relacionan sus componentes.",
  prior=["Sé qué componentes tiene un ecosistema.", "Sé que cambiar un componente puede afectar a otros."],
  explain=[
      "Un modelo es un dibujo, una maqueta o un esquema que representa algo real para entenderlo mejor. Para un ecosistema puedes dibujar componentes y flechas. Cada flecha dice qué relación hay: «la planta toma agua», «el caracol come hojas», «el sol da luz».",
      "Un buen modelo permite explicar y predecir. Si en tu dibujo quitas el agua, las flechas hacia la planta desaparecen y puedes decir que ella tendrá problemas. Así usas el modelo para pensar qué pasaría si algo cambia.",
      "Todo modelo tiene límites. Un dibujo no muestra todos los seres vivos, ni los cambios del clima, ni el paso del tiempo. Por eso, al terminar, debes escribir qué no muestra tu modelo. Un modelo es útil, pero no es el ecosistema real.",
  ],
  vocab=[("modelo", "representación simple de algo real para explicarlo"), ("flecha", "símbolo que indica una relación entre dos componentes"), ("límite del modelo", "algo real que el modelo no muestra"), ("explicación", "respuesta que dice cómo o por qué ocurre algo"), ("esquema", "dibujo simple con nombres y flechas")],
  worked=[
      ("Leer un modelo", "Modelo de jardín: Sol → planta; Agua → planta; Planta → caracol (el caracol come la planta). ¿Qué recibe la planta?", ["Busco las flechas que llegan a «planta».", "Llegan desde el Sol y el agua.", "Escribo ambos."], "La planta recibe luz del Sol y agua"),
      ("Encontrar un límite", "El modelo del jardín no muestra las lombrices. ¿Es un límite del modelo?", ["Reviso qué hay en el jardín real.", "Hay lombrices y el dibujo no las pone.", "Eso es algo real que falta."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Pensar que el modelo es igual al ecosistema real.", "Un modelo siempre simplifica.", "Escribe al menos un límite del modelo."),
      ("Dibujar flechas sin decir qué significan.", "Nadie sabe qué relación muestran.", "Escribe cerca de cada flecha un verbo: toma, come, da."),
  ],
  rec=[
      ("¿Un modelo es el ecosistema real o una representación?", "Una representación", "Sirve para entender, pero simplifica."),
      ("En el modelo Sol → planta, ¿qué componente da algo?", "El Sol", "La flecha sale del Sol hacia la planta."),
      ("Completa con «límite» o «dato»: lo que un modelo no muestra es un ______.", "Límite", "Es algo real que el modelo deja fuera."),
  ],
  und=[
      ("Modelo: Agua → planta → conejo. ¿Qué componente recibe algo del conejo?", "Ninguno", "No hay flecha que salga del conejo."),
      ("¿Por qué conviene escribir verbos junto a las flechas?", "Para que se entienda qué relación muestran", "Sin verbo la flecha no explica nada."),
      ("¿Qué muestra mejor cómo se relacionan los componentes? A) Una lista de nombres. B) Un esquema con flechas.", "B", "Las flechas muestran las relaciones."),
  ],
  app=[
      ("Modelo: Sol → pasto; Agua → pasto; Pasto → oveja. Si desaparece el agua, ¿a qué componente dejan de llegarle flechas de agua: al pasto o a la oveja?", "Al pasto", "La flecha del agua llega al pasto."),
      arith("Un modelo tiene 5 componentes y 6 flechas. Se agregan 2 componentes y 3 flechas. ¿Cuántos componentes hay ahora?", "5+2", "Se suman los componentes agregados."),
      ("Un modelo dice: agua → planta → saltamontes. ¿Quién depende de la planta para alimentarse?", "El saltamontes", "La flecha va de la planta al saltamontes."),
  ],
  rea=[
      ("Ema dibuja un modelo de patio con pasto y hormigas. Dice que su modelo explica todo el patio. ¿Tiene razón? Responde Sí o No y explica.", "No; no muestra los demás seres vivos ni el clima", "Un modelo siempre deja cosas fuera."),
      ("En un modelo cerrado hay tierra, agua, planta y caracol. Se saca el caracol. ¿Qué pasará con las hojas? Explica con una flecha del modelo.", "Se comerán menos porque la flecha del caracol a la hoja desaparece", "Sin el caracol, nadie come la hoja."),
  ],
  cha=[
      ("Un modelo de laguna muestra patos, juncos y agua, pero no el barro del fondo. Escribe un límite y una posible mejora.", "Límite: no muestra el barro; mejora: agregar el barro con una flecha", "Se reconoce lo que falta y se propone agregar."),
      ("Predice con un modelo: Sol → planta → oruga → pájaro. Si desaparecen las plantas, ¿quién se queda sin alimento primero?", "La oruga", "La oruga se alimenta directamente de la planta."),
  ],
  context=[("Una niña hizo un modelo de su patio. Dibujó 3 plantas, 4 hormigas y 2 piedras. Después vio 5 hormigas más que no estaban en su dibujo. ¿Cuántas hormigas había en total?", "9", "Dibujó 4 y vio 5 más; 4 + 5 = 9.")],
  selfcheck=[("¿Qué es un modelo?", "Una representación simple de algo real", "Ayuda a entender y explicar."), ("¿Para qué sirven las flechas?", "Para mostrar relaciones entre componentes", "Cada flecha indica una interacción."), ("¿Qué debe decir siempre un modelo sobre sí mismo?", "Qué no muestra", "Reconocer límites evita confundirlo con lo real.")],
  open_task=task("Dibuja un modelo de un ecosistema pequeño, por ejemplo una maceta con tierra, una planta, agua y el Sol. Usa al menos cuatro flechas con un verbo cada una. Escribe una predicción: ¿qué pasaría si quitas uno de los componentes? Escribe también un límite de tu modelo. No saques ni dañes seres vivos de verdad.", "Modelo: Sol → planta (da luz); Agua → planta (da agua); Tierra → planta (la sujeta). Si quito el agua, la planta se secará. Límite: no muestra las raíces.", ["al menos cuatro flechas con verbo", "una predicción con razón", "un límite del modelo"], ["dibujo", "predicción y límite escritos"], ["flechas sin verbo", "no escribir límites"], "Pregunta qué flecha es la más importante y qué parte real falta en el dibujo."),
  reinforce="Dibuja un esquema con tres componentes de tu casa y flechas que digan cómo se relacionan.",
  extend="Dibuja un modelo de una laguna con cinco componentes y escribe dos límites.")

# ---------------------------------------------------------------- OA 02
L(OA2, 1,
  materials="Este cuaderno y lápiz. Opcional: un libro o fotos de animales y plantas de Chile.",
  use="Aprenderé qué es una adaptación y a separar lo que veo de lo que supongo en animales y plantas. Sirve para explicar por qué viven donde viven.",
  prior=["Sé que los seres vivos viven en ecosistemas.", "Sé anotar lo que observo."],
  explain=[
      "Una adaptación es una característica o una conducta de un ser vivo que lo ayuda a sobrevivir en su ambiente. Una estructura es una parte del cuerpo, como el pelaje, las plumas o las hojas. Una conducta es lo que el ser vivo hace, como esconderse o dormir en invierno.",
      "Algunos ejemplos: el guanaco tiene un pelaje grueso y se mantiene abrigado en lugares fríos. El pingüino de Humboldt tiene plumas densas que protegen del agua. El cactus tiene espinas en lugar de hojas anchas y pierde poca agua.",
      "Al observar un ser vivo, anoto lo que veo: «tiene plumas, pico corto, patas con membrana». Interpretar es explicar para qué sirve. Primero va la observación y después la interpretación. Así no mezclo lo que vi con lo que supongo.",
  ],
  vocab=[("adaptación", "característica o conducta que ayuda a sobrevivir en un ambiente"), ("estructura", "parte del cuerpo de un ser vivo"), ("conducta", "lo que hace un animal"), ("cubierta corporal", "lo que cubre el cuerpo, como pelaje, plumas, escamas o caparazón"), ("sobrevivir", "seguir con vida")],
  worked=[
      ("Estructura o conducta", "Un guanaco tiene pelaje grueso. Otro animal se queda quieto cuando ve un depredador. ¿Cuál es estructura y cuál conducta?", ["El pelaje es una parte del cuerpo.", "Quedarse quieto es una acción.", "Parte del cuerpo = estructura; acción = conducta."], "El pelaje es estructura; quedarse quieto es conducta"),
      ("Observación o interpretación", "«El pingüino tiene plumas densas» y «Las plumas lo ayudan a no mojarse». ¿Cuál es la observación?", ["Veo si se puede mirar directamente.", "Las plumas densas se ven.", "«Lo ayudan» es la explicación."], "La primera frase"),
  ],
  mistakes=[
      ("Decir que el animal «decidió» cambiar su cuerpo para adaptarse.", "Las adaptaciones se heredan; un animal no las crea a voluntad.", "Di que la característica ayuda a sobrevivir."),
      ("Confundir adaptación con cualquier parte del cuerpo.", "Es adaptación si ayuda a sobrevivir en su ambiente.", "Pregunta: ¿cómo le sirve en su ambiente?"),
  ],
  rec=[
      ("Las plumas de un pingüino, ¿son estructura o conducta?", "Estructura", "Son una parte del cuerpo."),
      ("Un animal que se esconde, ¿muestra estructura o conducta?", "Conducta", "Esconderse es algo que hace."),
      ("Completa con «ayuda» o «molesta»: una adaptación ______ a sobrevivir.", "Ayuda", "Esa es la definición de adaptación."),
  ],
  und=[
      ("¿Cuál es una cubierta corporal? A) Pelaje. B) Dormir en invierno.", "A", "El pelaje cubre el cuerpo; dormir es conducta."),
      ("¿Para qué sirve el pelaje grueso del guanaco?", "Para mantener el calor en lugares fríos", "Atrapa calor y evita que el cuerpo se enfríe."),
      ("Marca la observación: A) La lagartija es del color de la roca. B) La lagartija quiere esconderse.", "A", "El color se ve; el deseo es suposición."),
  ],
  app=[
      ("Un cactus tiene espinas y tallo grueso. ¿Cuántas estructuras nombra la frase?", "2", "Las espinas y el tallo grueso."),
      ("Un ave tiene plumas impermeables y nada en el mar. ¿De qué la protegen esas plumas: del agua o de la arena?", "Del agua", "La pluma impermeable evita que el ave se moje."),
      ("Ordena con letras: A) Escribo para qué sirve. B) Miro el animal. C) Anoto lo que veo. ¿Cuál es el mejor orden?", "B, C, A", "Primero se observa y anota, después se explica."),
  ],
  rea=[
      ("Mario dice: «El conejo tiene orejas largas porque quiere oír mejor». ¿Qué está mezclando? Responde con una palabra: «observación» o «interpretación».", "Interpretación", "Dice una razón sin haberla probado."),
      ("Una niña dice que el cactus «inventó» sus espinas para el desierto. Corrige con una frase.", "Las espinas son una adaptación que lo ayuda a sobrevivir en el desierto", "Las adaptaciones no se inventan; se heredan."),
  ],
  cha=[
      ("Un animal vive en la nieve. Tiene pelaje blanco y grueso. Separa una observación de una interpretación sobre su pelaje.", "Observación: el pelaje es blanco y grueso. Interpretación: lo ayuda a mantener calor y a esconderse", "La observación es visible y la interpretación explica."),
      ("Una tortuga tiene un caparazón duro. ¿Es estructura o conducta, y de qué la protege?", "Estructura; la protege de golpes y de depredadores", "Es una parte del cuerpo con función protectora."),
  ],
  context=[("Un guía de un parque mira un puma y un guanaco. Anota: pelaje denso, patas fuertes y orejas grandes. ¿Cuántas estructuras anotó?", "3", "Pelaje denso, patas fuertes y orejas grandes son tres partes del cuerpo.")],
  selfcheck=[("¿Qué es una adaptación?", "Una característica o conducta que ayuda a sobrevivir", "Conecta un rasgo con el ambiente."), ("Da un ejemplo de estructura.", "Pelaje, plumas, hojas, espinas u otro", "Son partes del cuerpo."), ("Da un ejemplo de conducta.", "Esconderse, hibernar u otro", "Es algo que hace el animal.")],
  open_task=task("Elige uno de estos seres vivos: guanaco, pingüino de Humboldt o cactus. Escribe tres observaciones de su cuerpo (lo que se ve) y una interpretación sobre cómo lo ayuda a sobrevivir. Marca cuál es cada cosa. Si puedes, apóyate en un libro con una persona de tu casa; no necesitas ver un animal real.", "Guanaco. Observaciones: pelaje grueso, cuello largo, patas delgadas. Interpretación: el pelaje lo abriga en lugares fríos.", ["tres observaciones", "una interpretación marcada", "relación con el ambiente"], ["lista rotulada"], ["mezclar observación e interpretación", "usar datos sin fuente"], "Pregunta cómo sabe lo que escribió y si otra persona vería lo mismo."),
  reinforce="Mira un animal doméstico o una planta de tu casa y anota tres observaciones sobre su cubierta o su forma.",
  extend="Elige un animal de Chile y anota una adaptación de estructura y una de conducta.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Opcional: dos botellas pequeñas de plástico, un trozo de lana o tela gruesa y agua tibia de la llave.",
  use="Aprenderé a hacer preguntas y predicciones sobre cómo ayuda una adaptación. Sirve para comprobar con datos si una cubierta o una conducta protege.",
  prior=["Sé qué es una adaptación.", "Sé que una predicción se hace antes de comprobar."],
  explain=[
      "Para saber si una adaptación ayuda, se puede hacer una prueba con un modelo. Por ejemplo, el pelaje abriga. Para comprobarlo, envuelves una botella con agua tibia en lana y dejas otra sin envolver. Después de un rato, mides cuál se enfrió más.",
      "Una pregunta comprobable es: «¿Se enfría menos una botella envuelta en lana que una sin envolver?». La predicción dice qué creo que pasará y por qué: «La envuelta se enfriará menos, porque la lana guarda el calor».",
      "En una prueba justa cambio una cosa, aquí la lana, y dejo igual la temperatura inicial, el tamaño de la botella y el tiempo. Un modelo no es un animal real, pero permite probar una idea de manera segura.",
  ],
  vocab=[("modelo", "objeto o dibujo que representa algo real para probarlo"), ("prueba justa", "prueba donde cambia una sola cosa"), ("aislar", "evitar que el calor entre o salga"), ("temperatura", "medida de qué tan caliente o fría está una cosa"), ("grados Celsius (°C)", "unidad para medir la temperatura")],
  worked=[
      ("Qué se cambia", "Botella A: envuelta en lana. Botella B: sin lana. Ambas con agua tibia de igual temperatura y del mismo tamaño. ¿Qué es lo que cambia?", ["Comparo A y B.", "Tamaño y temperatura inicial son iguales.", "La lana es lo único distinto."], "La lana"),
      ("Leer datos", "Datos de ejemplo. A los 30 min, la botella A bajó 3 °C y la botella B bajó 8 °C. ¿Cuántos grados más bajó B?", ["Veo cuánto bajó cada botella.", "Resto 8 − 3.", "El resultado es la diferencia."], "5 °C más"),
  ],
  mistakes=[
      ("Usar botellas de distinto tamaño.", "El tamaño también cambia cuánto se enfría el agua.", "Usa botellas iguales."),
      ("Concluir que todos los animales con pelaje abrigan igual.", "La prueba muestra solo lo que ocurrió con ese modelo.", "Escribe una conclusión que se limite a lo probado."),
  ],
  rec=[
      ("En una prueba justa, ¿cuántas cosas cambias a propósito?", "Una", "Así sabes cuál produjo el resultado."),
      ("La lana en el modelo representa el ______ del animal. Escribe «pelaje» o «hueso».", "Pelaje", "El pelaje cubre y abriga al animal."),
      ("¿Cuál de estas es una unidad de temperatura: °C o cm?", "°C", "Los grados Celsius miden temperatura."),
  ],
  und=[
      ("¿Cuál es una pregunta comprobable? A) ¿Es bonito el pelaje del guanaco? B) ¿Se enfría menos una botella con lana que una sin lana?", "B", "B se responde midiendo temperatura."),
      ("Datos de ejemplo. Botella A empezó en 35 °C y quedó en 31 °C. ¿Cuántos grados bajó?", "4", "35 − 31 = 4."),
      ("¿Por qué las dos botellas deben empezar con la misma temperatura?", "Para que la diferencia final se deba solo a la lana", "Si empiezan distinto, el resultado se confunde."),
  ],
  app=[
      arith("Datos de ejemplo. Botella con lana: de 38 °C a 34 °C. Botella sin lana: de 38 °C a 30 °C. ¿Cuántos grados más bajó la que no tenía lana?", "(38-30)-(38-34)", "Se calcula cuánto bajó cada una y se comparan."),
      ("Predice: una botella con agua tibia se envuelve en lana y otra no. Después de 30 minutos, ¿cuál estará más tibia?", "La envuelta en lana", "La lana guarda el calor."),
      ("Escribe cuál es la variable que cambias si comparas dos cubiertas: lana y papel de diario.", "El material de la cubierta", "Es lo único que cambia entre las botellas."),
  ],
  rea=[
      ("Rosa comparó una botella grande con lana y una pequeña sin lana. Dice que la lana abriga. ¿Puede asegurarlo? Responde Sí o No y explica.", "No; cambió el tamaño además de la lana", "Con dos cambios no sabe cuál produjo el resultado."),
      ("Datos de ejemplo. Con lana: baja 3 °C. Sin lana: baja 7 °C. Dice: «Todos los animales con pelo abrigan igual». ¿Qué conclusión sí está apoyada?", "En esta prueba, la lana evitó que el agua se enfriara tanto", "La conclusión se limita a la prueba."),
  ],
  cha=[
      ("Diseña una prueba con tres botellas iguales para comparar lana, papel de diario y ninguna cubierta. Escribe qué mides y qué dejas igual.", "Mido la temperatura del agua después de 30 minutos; dejo igual el tamaño de las botellas, el agua inicial y el tiempo", "Una prueba justa mide lo mismo en todas."),
      ("Una persona dice que un modelo de botella no sirve porque la botella no es un animal. Escribe una razón a favor de usar el modelo.", "Permite probar una idea sin dañar animales", "El modelo ayuda a probar de forma segura."),
  ],
  context=[("Una profesora prepara 3 botellas iguales con agua tibia: una con lana, una con papel de diario y una sin cubierta. Anotó la baja de temperatura en 30 minutos: 3 °C, 5 °C y 8 °C, no necesariamente en ese orden. La sin cubierta es la que más baja. ¿Cuántos grados más bajó la sin cubierta que la de 3 °C?", "5", "La sin cubierta bajó 8 °C y 8 − 3 = 5.")],
  selfcheck=[("¿Para qué sirve un modelo en una prueba?", "Para probar una idea de forma segura", "Representa algo real sin dañarlo."), ("¿Qué es una prueba justa?", "Una prueba donde cambia una sola cosa", "Permite saber qué causó el resultado."), ("¿Dónde se escribe una predicción?", "Antes de comprobar", "Es una idea previa al resultado.")],
  open_task=task("Con una persona adulta, usa dos botellas de plástico iguales con la misma cantidad de agua tibia (no caliente). Envuelve una con tela gruesa y deja la otra sin envolver. Anota la temperatura al inicio y a los 30 minutos con un termómetro, o toca con la palma de la mano y anota «más tibia» o «más fría». Escribe tu predicción antes y tu conclusión después.", "Predicción: la envuelta quedará más tibia. Resultado: envuelta, 36 °C; sin envolver, 31 °C. Conclusión: en esta prueba la tela ayudó a guardar el calor.", ["predicción antes de probar", "dos botellas iguales", "conclusión limitada a lo probado"], ["tabla de datos", "conclusión"], ["usar agua muy caliente", "no medir a los 30 minutos"], "Pregunta qué parte del modelo representa al pelaje y qué limitación tiene."),
  reinforce="Explica con tus palabras por qué un abrigo ayuda a mantener el calor del cuerpo.",
  extend="Diseña una prueba segura para ver si un color claro o uno oscuro se calienta más al sol, y dibuja tu tabla.")

L(OA2, 3,
  materials="Este cuaderno, lápiz y regla.",
  use="Aprenderé a comparar adaptaciones de distintos seres vivos con un mismo criterio. Sirve para entender cómo cada ambiente pide características distintas.",
  prior=["Sé qué es una adaptación.", "Sé que una comparación necesita un criterio común."],
  explain=[
      "Seres vivos de ambientes distintos tienen adaptaciones distintas. Para compararlas uso un criterio: el ambiente donde viven, la parte del cuerpo adaptada o la función de esa adaptación. Siempre miro el mismo criterio en todos.",
      "La cubierta corporal cambia según el ambiente. Un animal de lugares fríos suele tener pelaje denso o grasa. Uno del agua suele tener plumas impermeables o escamas lisas. El caparazón protege a una tortuga o a un caracol. El camuflaje es parecerse al lugar para no ser visto.",
      "Las plantas también se adaptan. En lugares secos, algunas tienen hojas con espinas o cubiertas con cera, que pierden poca agua. En lugares muy húmedos, las hojas son anchas. En invierno, algunos animales hibernan: pasan semanas o meses dormidos y gastan poca energía.",
  ],
  vocab=[("camuflaje", "parecerse al ambiente para no ser visto"), ("hibernación", "estado de sueño profundo en invierno para gastar poca energía"), ("caparazón", "cubierta dura que protege el cuerpo"), ("cera", "capa que protege las hojas y evita perder agua"), ("depredador", "animal que caza a otros para alimentarse")],
  worked=[
      ("Ordenar por función", "Cubiertas: pelaje denso, plumas impermeables, caparazón. Funciones: abrigar, protegerse de golpes, no mojarse. Une cada una.", ["Pienso para qué sirve cada cubierta.", "El pelaje abriga.", "Las plumas impermeables evitan mojarse y el caparazón protege de golpes."], "Pelaje → abrigar; plumas → no mojarse; caparazón → protegerse de golpes"),
      ("Comparar plantas", "Cactus: hojas convertidas en espinas, vive en lugares secos. Planta de selva: hojas muy anchas, vive en lugares muy húmedos. ¿Cuál pierde menos agua por sus hojas?", ["Las espinas tienen muy poca superficie.", "Las hojas anchas tienen mucha.", "Menos superficie pierde menos agua."], "El cactus"),
  ],
  mistakes=[
      ("Decir que el camuflaje es cambiar de lugar.", "El camuflaje es parecerse al ambiente.", "Piensa en color y forma parecidos al lugar."),
      ("Decir que hibernar es morir.", "El animal sigue vivo y despierta.", "Hibernar es dormir profundamente y gastar poca energía."),
  ],
  rec=[
      ("¿Qué adaptación protege de golpes a una tortuga?", "El caparazón", "Es una cubierta dura."),
      ("Un insecto que parece una rama, ¿usa camuflaje o hibernación?", "Camuflaje", "Se parece al ambiente."),
      ("Completa con «dormido» o «despierto»: durante la hibernación el animal permanece ______ mucho tiempo.", "Dormido", "Es un sueño profundo."),
  ],
  und=[
      ("¿Qué adaptación tiene un cactus para perder poca agua? A) Espinas. B) Pelaje.", "A", "El cactus es una planta y las espinas reducen la pérdida de agua."),
      ("¿Para qué hiberna un animal?", "Para gastar poca energía en la estación fría", "Dormir ahorra energía cuando hay poco alimento."),
      ("¿Cuál criterio usarías para comparar un pingüino y un guanaco? A) El ambiente donde viven. B) El color de mi ropa.", "A", "El ambiente es una característica de ambos."),
  ],
  app=[
      ("Une la cubierta con su función: plumas impermeables, pelaje denso, caparazón. Funciones: abrigar, no mojarse, proteger de golpes. Escribe la que corresponde al pelaje denso.", "Abrigar", "El pelaje grueso guarda el calor."),
      ("Un animal de lugares muy fríos tiene pelaje denso. Otro de aguas cálidas tiene piel lisa. ¿Cuál tiene la cubierta que más abriga?", "El de pelaje denso", "El pelaje denso guarda más calor."),
      arith("Un animal hiberna durante 12 semanas. Una semana tiene 7 días. ¿Cuántos días hiberna?", "12*7", "Se multiplican las semanas por los días de cada una."),
  ],
  rea=[
      ("Ana dice que un lagarto verde sobre una hoja verde usa camuflaje. Beto dice que usa hibernación. ¿Quién tiene razón? Explica.", "Ana; se parece al ambiente", "El color verde coincide con la hoja y eso es camuflaje."),
      ("Datos de ejemplo. Planta A: hojas gruesas y con cera, vive en lugar seco. Planta B: hojas delgadas, vive junto a un río. ¿Cuál se adapta mejor a un lugar seco? Explica.", "La A, porque la cera evita perder agua", "La cera cubre la hoja y reduce la pérdida de agua."),
  ],
  cha=[
      ("Un animal cambia a color blanco en invierno. ¿Qué adaptación crees que sea y qué ventaja da?", "Camuflaje; se parece a la nieve", "El color blanco ayuda a no ser visto en la nieve."),
      ("Compara un guanaco y un pingüino: ¿qué tienen en común y qué tienen distinto en su cubierta corporal?", "Ambos tienen cubierta que los protege; el guanaco tiene pelo y el pingüino plumas", "Ambos se protegen del ambiente, con materiales distintos."),
  ],
  context=[("En un zoológico una guía cuenta: «Hay 4 animales con pelaje, 3 con plumas y 2 con caparazón». ¿Cuántos animales nombró en total?", "9", "4 + 3 + 2 = 9.")],
  selfcheck=[("¿Qué es el camuflaje?", "Parecerse al ambiente para no ser visto", "Ayuda a escapar de los depredadores."), ("¿Qué hace un animal que hiberna?", "Duerme profundamente y gasta poca energía", "Así supera el invierno."), ("¿Cómo cambia la cubierta según el ambiente?", "Cada ambiente favorece una cubierta distinta", "Pelaje en frío, plumas en el agua, caparazón para protegerse.")],
  open_task=task("Haz una tabla con tres seres vivos, por ejemplo: guanaco, pingüino de Humboldt y cactus. Las columnas deben ser: ambiente, parte del cuerpo adaptada y para qué sirve. Escribe dos frases que comparen dos de ellos con el mismo criterio. Puedes apoyarte en un libro de tu casa o de la biblioteca.", "Guanaco: ambiente frío y árido; pelaje denso; abriga. Cactus: ambiente seco; espinas; pierde poca agua. Ambos tienen una adaptación para el ambiente, pero uno es animal y otro planta.", ["tabla completa", "criterio común", "dos frases comparativas"], ["tabla con tres filas"], ["comparar con criterios distintos", "no decir para qué sirve"], "Pregunta qué criterio usó y si otro ser vivo cambiaría la comparación."),
  reinforce="Escribe tres animales que conozcas y su cubierta corporal.",
  extend="Elige dos ambientes (por ejemplo desierto y mar) y escribe una adaptación distinta para cada uno.")

L(OA2, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: papel de diario y recortes de papel de colores.",
  use="Aprenderé a explicar una adaptación con un modelo y a decir qué no muestra. Sirve para comunicar cómo ayuda sobrevivir.",
  prior=["Sé comparar adaptaciones.", "Sé que un modelo tiene límites."],
  explain=[
      "Una explicación completa de una adaptación tiene tres partes: qué rasgo es, en qué ambiente vive el ser vivo y cómo lo ayuda a sobrevivir. Por ejemplo: «La mariposa tiene alas con colores de hoja seca. Vive en el bosque. Así los depredadores no la ven».",
      "Un modelo de camuflaje es usar papelitos de colores sobre un papel de diario o sobre un papel de color. Si los papelitos son del mismo color que el fondo, cuesta encontrarlos. Si el color es distinto, se encuentran rápido. Así puedo probar la idea con datos.",
      "El modelo tiene límites. Los papelitos no se mueven, no tienen sombra y no huelen. Por eso sirve para probar la idea del color, pero no muestra todo lo que ocurre en la naturaleza. Debo escribir ese límite junto a mi conclusión.",
  ],
  vocab=[("explicación", "respuesta que dice cómo o por qué"), ("rasgo", "característica de un ser vivo"), ("modelo de camuflaje", "juego con papelitos para probar cómo el color ayuda a esconderse"), ("fondo", "superficie sobre la que está algo"), ("límite", "algo que un modelo no muestra")],
  worked=[
      ("Completar una explicación", "Falta una parte: «El conejo de pelaje pardo vive en el pasto seco. ______». ¿Qué parte falta?", ["Reviso: rasgo y ambiente están.", "Falta decir cómo lo ayuda.", "Debo explicar por qué sobrevive."], "Falta decir cómo lo ayuda a sobrevivir; por ejemplo, que su pelaje se confunde con el pasto"),
      ("Leer datos del modelo", "Datos de ejemplo. De 20 papelitos del mismo color que el fondo, se encontraron 6. De 20 de color distinto, se encontraron 18. ¿Qué color se encontró mejor?", ["Comparo 6 y 18.", "18 es mayor que 6.", "Se encontró mejor el color distinto."], "El color distinto del fondo"),
  ],
  mistakes=[
      ("Dar solo el nombre de la adaptación sin decir cómo ayuda.", "La explicación queda incompleta.", "Completa con rasgo, ambiente y función."),
      ("Concluir que el camuflaje siempre salva.", "El modelo solo mostró una parte.", "Escribe: «en esta prueba…»."),
  ],
  rec=[
      ("¿Una explicación debe decir cómo ayuda el rasgo o solo su nombre?", "Cómo ayuda", "Si no, no explica."),
      ("Si un papelito es del mismo color que el fondo, ¿es más difícil o más fácil de encontrar?", "Más difícil", "Se confunde con el fondo."),
      ("Completa con «mueve» o «no se mueve»: el papelito del modelo ______.", "No se mueve", "Es un límite del modelo."),
  ],
  und=[
      ("¿Cuáles son las tres partes de una buena explicación de adaptación?", "Rasgo, ambiente y cómo ayuda", "Juntas explican por qué sobrevive."),
      ("En el modelo de camuflaje, ¿qué cambia: el color de los papelitos o el tamaño del papel de diario?", "El color de los papelitos", "Es la variable que se prueba."),
      ("¿Por qué el modelo de papelitos tiene límites?", "Porque no muestra movimiento, sombras ni olores", "Un modelo simplifica la realidad."),
  ],
  app=[
      arith("Datos de ejemplo. Del mismo color que el fondo: se encontraron 4 de 20. De color distinto: se encontraron 17 de 20. ¿Cuántos papelitos más se encontraron de color distinto?", "17-4", "Se resta el valor menor al mayor."),
      ("Explicación: «La lagartija es parda y vive entre piedras». ¿Qué parte falta: el rasgo, el ambiente o cómo la ayuda?", "Cómo la ayuda", "Falta decir que así los depredadores no la ven."),
      ("Un modelo muestra que los papelitos verdes sobre fondo verde son difíciles de ver. ¿Qué afirmación está apoyada? A) El verde siempre esconde. B) En el modelo, el verde se esconde en fondo verde.", "B", "La conclusión se limita a lo probado."),
  ],
  rea=[
      ("Luis dice que el modelo prueba que ningún depredador verá un insecto verde. ¿Está bien? Responde Sí o No y explica.", "No; el modelo no incluye el movimiento ni la visión real", "El modelo es una prueba parcial."),
      ("Ana y Beto comparan cuántos papelitos encuentran. Para que sea justo, ¿qué deben dejar igual: el tiempo de búsqueda o el color de los papelitos que cambian?", "El tiempo de búsqueda", "Lo que no se prueba debe ser igual para ambos."),
  ],
  cha=[
      ("Escribe una explicación completa de la adaptación del pingüino de Humboldt con plumas impermeables.", "El pingüino tiene plumas densas e impermeables, vive en el mar y la costa; así no se moja y mantiene su calor", "Incluye rasgo, ambiente y función."),
      ("Escribe un límite de un modelo de camuflaje con papelitos y cómo lo mejorarías.", "No muestra el movimiento; podría mover los papelitos con un hilo", "Reconoce lo que falta y propone una mejora."),
  ],
  context=[("En una clase se usó el modelo de papelitos. Con papelitos camuflados se encontraron 7 de 25. Con papelitos de color distinto se encontraron 20 de 25. ¿Cuántos papelitos camuflados NO se encontraron?", "18", "25 − 7 = 18.")],
  selfcheck=[("¿Qué incluye una explicación de adaptación?", "Rasgo, ambiente y cómo ayuda a sobrevivir", "Así queda completa."), ("¿Para qué sirve un modelo de camuflaje?", "Para probar si el color ayuda a no ser visto", "Permite comparar con datos."), ("¿Qué debe escribirse junto a la conclusión del modelo?", "Un límite del modelo", "Evita exagerar los resultados.")],
  open_task=task("Con una persona de tu casa, recorta 20 papelitos del color del fondo y 20 de otro color, y espárcelos sobre un papel de diario o un mantel estampado. Mira durante 20 segundos y cuenta cuántos de cada color encuentras. Escribe una explicación de camuflaje con tus datos y un límite del modelo. No uses tijeras si eres menor sin ayuda de una persona adulta.", "Del mismo color encontré 6 de 20 y de color distinto 16 de 20. El color igual al fondo se esconde mejor. Límite: los papelitos no se mueven.", ["conteo de dos colores", "explicación con datos", "un límite del modelo"], ["tabla de conteos", "explicación"], ["mirar tiempos distintos", "no escribir límite"], "Pregunta qué cambiaría si los papelitos se movieran."),
  reinforce="Explica con tus palabras por qué algunos insectos se parecen a hojas.",
  extend="Investiga la adaptación de una planta de Chile y escribe una explicación con rasgo, ambiente y función.")

# ---------------------------------------------------------------- OA 03
L(OA3, 1,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé qué es una cadena alimentaria y quiénes son productores, consumidores y descomponedores. Sirve para saber de dónde sale el alimento en un ecosistema.",
  prior=["Sé que los seres vivos necesitan alimento.", "Sé qué es un ecosistema."],
  explain=[
      "Una cadena alimentaria muestra quién se alimenta de quién. Se dibuja con flechas que van desde el alimento hacia quien lo come. Por ejemplo: pasto → guanaco → puma. La flecha significa «es comido por» y también «pasa energía a».",
      "Los productores son seres vivos que fabrican su propio alimento, como las plantas y las algas. Los consumidores comen otros seres vivos: los herbívoros comen plantas, los carnívoros comen animales y los omnívoros comen de ambos. Los descomponedores, como los hongos y las bacterias, descomponen restos de seres vivos y los devuelven al suelo.",
      "En una cadena siempre empieza un productor. Después vienen uno o más consumidores. Los descomponedores actúan sobre los restos de todos los niveles. Así la materia vuelve al suelo y las plantas pueden usarla otra vez.",
  ],
  vocab=[("cadena alimentaria", "serie de seres vivos donde cada uno se alimenta del anterior"), ("productor", "ser vivo que fabrica su propio alimento"), ("consumidor", "ser vivo que se alimenta de otros seres vivos"), ("descomponedor", "ser vivo que descompone restos y los devuelve al suelo"), ("herbívoro", "animal que come plantas")],
  worked=[
      ("Ordenar una cadena", "Seres vivos: puma, pasto, guanaco. Ordénalos como cadena alimentaria.", ["Busco el productor: el pasto.", "Después el que come pasto: el guanaco.", "Después el que come al guanaco: el puma."], "Pasto → guanaco → puma"),
      ("Reconocer el rol", "¿Qué rol tiene un hongo que descompone una hoja caída?", ["Veo qué hace: descompone restos.", "Los que hacen eso son descomponedores.", "Devuelve materia al suelo."], "Descomponedor"),
  ],
  mistakes=[
      ("Dibujar la flecha desde el animal que come hacia el alimento.", "La flecha muestra hacia dónde pasa el alimento.", "Dibuja la flecha desde el alimento hacia el que se lo come."),
      ("Pensar que el Sol es un productor.", "Los productores son seres vivos.", "El Sol aporta energía; la planta es la productora."),
  ],
  rec=[
      ("Una planta fabrica su alimento. ¿Es productor o consumidor?", "Productor", "Fabrica su propio alimento."),
      ("Un zorro que se come un ratón, ¿es productor o consumidor?", "Consumidor", "Se alimenta de otro animal."),
      ("Completa con «descomponedores» o «herbívoros»: los hongos y las bacterias son ______.", "Descomponedores", "Descomponen restos de seres vivos."),
  ],
  und=[
      ("¿Quién empieza una cadena alimentaria? A) El productor. B) El carnívoro.", "A", "Sin productor no hay alimento inicial."),
      ("En pasto → conejo → zorro, ¿qué come el zorro?", "Al conejo", "La flecha va del conejo al zorro."),
      ("¿Qué tipo de consumidor es un animal que come solo plantas?", "Herbívoro", "Los herbívoros se alimentan de plantas."),
  ],
  app=[
      ("Ordena con letras: A) lechuza, B) semillas, C) ratón. ¿Cuál es la cadena?", "B, C, A", "Semillas → ratón → lechuza."),
      ("En la cadena fitoplancton → anchoveta → pingüino de Humboldt, ¿cuál es el productor?", "El fitoplancton", "Es el que fabrica su alimento."),
      arith("Una cadena tiene 1 productor, 2 consumidores y 1 descomponedor que actúa al final. ¿Cuántos seres vivos intervienen?", "1+2+1", "Se suman todos los tipos."),
  ],
  rea=[
      ("Una niña dibuja la cadena puma → guanaco → pasto. ¿Está bien? Responde Sí o No y explica.", "No; las flechas van al revés", "La flecha debe ir del alimento al que lo come."),
      ("Un hongo crece sobre una hoja seca. Beto dice que es un consumidor porque «come». ¿Qué responderías?", "Es un descomponedor, porque descompone restos y los devuelve al suelo", "Su función es descomponer restos."),
  ],
  cha=[
      ("Escribe una cadena alimentaria con tres seres vivos del mar de Chile: fitoplancton, anchoveta y pingüino de Humboldt, sin usar flechas al revés.", "Fitoplancton → anchoveta → pingüino de Humboldt", "Va del productor al consumidor."),
      ("Escribe el rol de cada ser vivo en: pasto → vicuña → puma.", "Pasto: productor; vicuña: consumidor herbívoro; puma: consumidor carnívoro", "Cada uno cumple un rol distinto."),
  ],
  context=[("En el altiplano de Chile una guía anota: pasto → vicuña → puma. Si en un recorrido ve 8 vicuñas y 1 puma, ¿cuántos consumidores ve?", "9", "8 vicuñas + 1 puma = 9 consumidores.")],
  selfcheck=[("¿Qué muestran las flechas de una cadena?", "Quién se alimenta de quién", "Van del alimento al que lo come."), ("¿Qué hace un productor?", "Fabrica su propio alimento", "Las plantas y las algas son productores."), ("¿Qué hacen los descomponedores?", "Descomponen restos y los devuelven al suelo", "Hongos y bacterias cumplen este rol.")],
  open_task=task("Escribe dos cadenas alimentarias de ecosistemas de Chile, de tres seres vivos cada una. Puedes usar: fitoplancton, anchoveta y pingüino de Humboldt; pasto, vicuña y puma; semillas, ratón y lechuza. Marca el rol de cada ser vivo y agrega un descomponedor para una de ellas.", "Pasto → vicuña → puma. Pasto: productor; vicuña: herbívoro; puma: carnívoro. Los hongos descomponen restos del puma.", ["flechas del alimento al consumidor", "rol de cada ser vivo", "un descomponedor"], ["dos cadenas dibujadas"], ["flechas al revés", "olvidar el productor"], "Pregunta qué pasaría si el productor desapareciera."),
  reinforce="Escribe una cadena con tres seres vivos de tu casa o plaza.",
  extend="Escribe una cadena de cuatro seres vivos en la que haya un herbívoro y dos carnívoros.")

L(OA3, 2,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a preguntar y predecir qué pasa en una cadena alimentaria cuando un ser vivo cambia. Sirve para entender que todos dependen de todos.",
  prior=["Sé qué son productores, consumidores y descomponedores.", "Sé que las flechas van del alimento al que lo come."],
  explain=[
      "En una cadena alimentaria, si cambia la cantidad de un ser vivo, cambian los demás. Si hay menos pasto, hay menos alimento para los herbívoros. Si hay menos herbívoros, hay menos alimento para los carnívoros. Esto se llama efecto en cadena.",
      "Una pregunta comprobable puede ser: «¿Qué pasa con el número de vicuñas si baja el pasto?». La predicción dice qué creo y por qué: «Habrá menos vicuñas, porque tendrán menos alimento».",
      "Para probar una idea en el aula podemos usar datos de ejemplo o un modelo de papel. No cambiamos un ecosistema real. Un cambio puede tener varias causas. Por eso la conclusión debe decir qué datos la apoyan y qué no sabemos.",
  ],
  vocab=[("efecto en cadena", "cambio en un ser vivo que afecta a los demás"), ("población", "conjunto de seres vivos de la misma especie en un lugar"), ("predicción", "lo que creo que pasará y por qué"), ("causa", "lo que produce un cambio"), ("alimento disponible", "cantidad de alimento que hay para comer")],
  worked=[
      ("Hacer una predicción", "En la cadena pasto → vicuña → puma baja la cantidad de pasto. Predice qué pasará con las vicuñas.", ["Pienso de qué se alimentan.", "Las vicuñas comen pasto.", "Menos pasto, menos alimento."], "Habrá menos vicuñas, porque tendrán menos alimento"),
      ("Usar datos", "Datos de ejemplo. Año 1: 50 vicuñas. Año 2: 38 vicuñas. ¿Cuántas vicuñas menos hay?", ["Resto 50 − 38.", "El resultado es la disminución.", "Escribo la respuesta con la unidad."], "12 vicuñas menos"),
  ],
  mistakes=[
      ("Pensar que solo cambia el ser vivo al que se le hizo el cambio.", "Los demás dependen de él y también cambian.", "Sigue las flechas para ver quién más se afecta."),
      ("Decir que hay una sola causa segura para un cambio.", "Pueden existir varias causas.", "Escribe qué datos apoyan tu idea y qué falta."),
  ],
  rec=[
      ("Si baja el pasto, ¿bajan o suben los herbívoros que lo comen?", "Bajan", "Tienen menos alimento."),
      ("¿Una predicción se escribe antes o después de ver los datos?", "Antes", "Es una idea previa que luego se comprueba."),
      ("En pasto → vicuña → puma, ¿quién come pasto?", "La vicuña", "La flecha del pasto llega a la vicuña."),
  ],
  und=[
      ("¿Cuál pregunta se puede comprobar con datos? A) ¿Cuántas vicuñas hay en cada año? B) ¿Es linda la vicuña?", "A", "Se puede contar."),
      ("Si hay menos vicuñas, ¿qué le pasa al alimento disponible del puma?", "Disminuye", "El puma se alimenta de vicuñas."),
      ("¿Qué quiere decir efecto en cadena?", "Que un cambio en un ser vivo afecta a los demás", "Los seres vivos de la cadena dependen unos de otros."),
  ],
  app=[
      arith("Datos de ejemplo. Un año había 60 ratones y al siguiente 45. ¿Cuántos ratones menos hay?", "60-45", "Se resta la cantidad menor a la mayor."),
      ("Predice: en semillas → ratón → lechuza, las semillas aumentan mucho. ¿Qué pasará con los ratones? Escribe «más» o «menos».", "Más", "Habrá más alimento para ellos."),
      ("Una cadena es: algas → lapa → gaviota. Si disminuyen las algas, ¿qué se afecta primero?", "Las lapas", "Son las que comen algas."),
  ],
  rea=[
      ("Datos de ejemplo. Año 1: 40 vicuñas y 5 pumas. Año 2: 20 vicuñas y 5 pumas. Ana dice que los pumas tendrán menos alimento. ¿Tiene razón? Explica.", "Sí; hay menos vicuñas para alimentarlos", "Las vicuñas son alimento de los pumas."),
      ("Un niño dice: «Si desaparecen los pumas, no pasa nada con el pasto». Predice si es correcto y explica con la cadena.", "Es incorrecto; habría más vicuñas y se comerían más pasto", "Un cambio en un nivel llega a los otros."),
  ],
  cha=[
      ("Escribe una pregunta comprobable para una cadena y qué datos necesitarías.", "¿Cuántas lapas hay con más o menos algas? Necesito contar lapas y algas en lugares distintos", "La pregunta se resuelve con conteos."),
      ("Datos de ejemplo. Antes: 100 anchovetas. Después: 70 anchovetas. ¿Puedes asegurar que la causa fue la falta de fitoplancton?", "No; faltan datos sobre otras causas", "Pudieron existir otras causas."),
  ],
  context=[("En una laguna un conteo de ejemplo dio: 80 plantas acuáticas, 30 peces y 4 aves. Al año siguiente hubo 50 plantas acuáticas. ¿Cuántas plantas menos hay?", "30", "80 − 50 = 30.")],
  selfcheck=[("¿Qué pasa si baja el productor?", "Bajan los consumidores que dependen de él", "Hay menos alimento."), ("¿Qué debe tener una predicción?", "Lo que pasará y la razón", "Así se puede comprobar."), ("¿Por qué una conclusión debe decir qué falta saber?", "Porque pueden existir otras causas", "Es honesto sobre los límites.")],
  open_task=task("Con la cadena pasto → vicuña → puma, escribe una pregunta comprobable, una predicción con razón y una tabla con los datos de ejemplo: año 1, 50 vicuñas; año 2, 35 vicuñas; año 3, 25 vicuñas. Calcula cuánto bajaron en total y escribe una conclusión que diga qué no sabes.", "Pregunta: ¿qué pasa con las vicuñas si baja el pasto? Predicción: bajan porque hay menos alimento. Bajaron 25. No sé si hubo otra causa.", ["pregunta comprobable", "predicción con razón", "conclusión con límite"], ["tabla de tres años", "conclusión"], ["afirmar una causa segura sin datos", "restar mal"], "Pregunta qué otro dato ayudaría a decidir la causa."),
  reinforce="Escribe una cadena de tres seres vivos y predice qué pasa si falta el primero.",
  extend="Explica por qué cuidar los productores ayuda a todos los demás.")

L(OA3, 3,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar cadenas alimentarias de distintos ecosistemas de Chile con un mismo criterio. Sirve para ver qué se repite en todos.",
  prior=["Sé qué son productores, consumidores y descomponedores.", "Sé comparar con un criterio."],
  explain=[
      "Aunque los ecosistemas de Chile son muy distintos, sus cadenas siguen la misma idea: empiezan con un productor y siguen con consumidores. En todas actúan además los descomponedores. En el mar: fitoplancton → anchoveta → pingüino de Humboldt. En el altiplano: pasto → vicuña → puma.",
      "En un bosque puede haber: semillas → ratón → lechuza. Para compararlas usamos un criterio común: qué productor tienen, qué tipo de consumidores hay o cuántos eslabones tiene la cadena. Un eslabón es cada ser vivo de la cadena.",
      "Cambian los seres vivos, pero se repiten los roles. Siempre hay alguien que fabrica alimento y alguien que lo consume. Los descomponedores, como hongos y bacterias, actúan en todos los ecosistemas y devuelven materia al suelo.",
  ],
  vocab=[("eslabón", "cada ser vivo de una cadena alimentaria"), ("ecosistema marino", "ecosistema del mar"), ("altiplano", "zona alta y fría del norte de Chile"), ("rol", "función de un ser vivo en el ecosistema"), ("carnívoro", "animal que se alimenta de otros animales")],
  worked=[
      ("Contar eslabones", "Cadena: fitoplancton → anchoveta → pingüino de Humboldt. ¿Cuántos eslabones tiene?", ["Cuento cada ser vivo.", "Hay fitoplancton, anchoveta y pingüino.", "Son tres."], "3 eslabones"),
      ("Encontrar lo común", "Cadena 1: pasto → vicuña → puma. Cadena 2: semillas → ratón → lechuza. ¿Qué rol tienen pasto y semillas?", ["Pregunto qué hacen.", "Son plantas o partes de plantas que son alimento inicial.", "En ambas cadenas son el inicio."], "Son productores (el inicio de la cadena)"),
  ],
  mistakes=[
      ("Pensar que las cadenas de distintos ecosistemas no tienen nada en común.", "Todas tienen productor, consumidores y descomponedores.", "Compara los roles."),
      ("Comparar cadenas con criterios distintos, por ejemplo tamaño en una y alimento en otra.", "No hay criterio común.", "Elige un criterio para todas."),
  ],
  rec=[
      ("¿Qué rol tiene el pasto en pasto → vicuña → puma?", "Productor", "Fabrica su alimento."),
      ("¿Cuántos eslabones tiene semillas → ratón → lechuza?", "3", "Hay tres seres vivos o alimentos nombrados."),
      ("Completa con «igual» o «distinto»: los roles se repiten, pero los seres vivos son ______ en cada ecosistema.", "Distintos", "Cada ecosistema tiene sus propios seres vivos."),
  ],
  und=[
      ("¿Qué tienen en común las cadenas del mar y del altiplano? A) Tienen un productor al inicio. B) Tienen los mismos animales.", "A", "En ambas empieza un productor."),
      ("¿En qué cadena el carnívoro es la lechuza: semillas → ratón → lechuza o pasto → vicuña → puma?", "Semillas → ratón → lechuza", "La lechuza come ratones."),
      ("¿Dónde actúan los descomponedores: solo en el mar o en todos los ecosistemas?", "En todos", "Están en cualquier ecosistema donde haya restos."),
  ],
  app=[
      arith("Tres cadenas de tres eslabones cada una. ¿Cuántos eslabones hay en total?", "3*3", "Se multiplican cadenas por eslabones."),
      ("Cadena 1: pasto → vicuña → puma. Cadena 2: fitoplancton → anchoveta → pingüino de Humboldt. ¿Cuál ecosistema es el mar?", "La cadena 2", "El fitoplancton y la anchoveta son del mar."),
      ("Ordena de menos a más eslabones: A) fitoplancton → anchoveta, B) pasto → vicuña → puma, C) semillas.", "C, A, B", "C tiene 1, A tiene 2 y B tiene 3."),
  ],
  rea=[
      ("Beto dice que una cadena sin productor puede existir. ¿Tiene razón? Responde Sí o No y explica.", "No; sin productor no hay alimento inicial", "Los consumidores dependen de él."),
      ("Datos de ejemplo. Cadena A: 3 eslabones. Cadena B: 4 eslabones. Ana dice que B es mejor. ¿Qué responderías?", "Tener más eslabones no la hace mejor; solo es distinta", "Es una diferencia, no un valor."),
  ],
  cha=[
      ("Explica con una frase qué se repite en todas las cadenas de Chile.", "Siempre empiezan con un productor, tienen consumidores y los descomponedores actúan", "Los roles se repiten en todos."),
      ("Propón una cadena de cuatro eslabones: pasto, saltamontes, lagartija, zorro culpeo. Escríbela con flechas.", "Pasto → saltamontes → lagartija → zorro culpeo", "Va del productor al último consumidor."),
  ],
  context=[("Un parque tiene tres rutas: la ruta del mar, del altiplano y del bosque. En cada una se dibujó una cadena de 3 eslabones y se agregó 1 descomponedor. ¿Cuántos seres vivos aparecen dibujados por ruta?", "4", "3 + 1 = 4 por ruta.")],
  selfcheck=[("¿Qué se repite en todas las cadenas?", "Los roles de productor, consumidor y descomponedor", "Aunque los seres vivos cambien."), ("¿Qué es un eslabón?", "Cada ser vivo de una cadena", "Son los pasos de la cadena."), ("Nombra un productor del mar.", "Fitoplancton o algas", "Fabrican su alimento.")],
  open_task=task("Haz una tabla con tres cadenas de Chile: mar (fitoplancton, anchoveta, pingüino de Humboldt), altiplano (pasto, vicuña, puma) y bosque (semillas, ratón, lechuza). Columnas: ecosistema, productor, primer consumidor y último consumidor. Escribe una frase que diga qué se repite.", "Mar: productor fitoplancton; primer consumidor anchoveta; último consumidor pingüino de Humboldt. Se repite que todas empiezan con un productor.", ["tabla completa", "roles bien asignados", "frase final"], ["tabla de tres filas"], ["asignar mal el rol", "olvidar el productor"], "Pregunta por qué se repiten los roles aunque cambien los animales."),
  reinforce="Escribe una cadena de un ecosistema que conozcas y marca el productor.",
  extend="Compara dos cadenas con un criterio nuevo: por ejemplo, cuántos carnívoros hay.")

L(OA3, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: tarjetas de papel.",
  use="Aprenderé a hacer un modelo de cadena alimentaria y a decir sus límites. Sirve para explicar cómo circula el alimento en un ecosistema.",
  prior=["Sé hacer cadenas alimentarias.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo de cadena alimentaria es un esquema con tarjetas y flechas. Cada tarjeta es un ser vivo y cada flecha muestra hacia dónde pasa el alimento. Con tarjetas puedes mover, quitar o agregar seres vivos y predecir qué pasa.",
      "Pero la naturaleza es más compleja que una cadena. Un animal suele comer más de un alimento y es comido por más de un animal. Por eso se forman redes alimentarias, que son varias cadenas unidas. Una cadena simple muestra solo una parte.",
      "Un buen modelo se acompaña de una explicación: describo la cadena, cito un ejemplo y escribo qué no muestra. Por ejemplo: «No muestra los descomponedores ni otros alimentos de la vicuña».",
  ],
  vocab=[("red alimentaria", "varias cadenas unidas"), ("modelo", "representación simple de algo real"), ("tarjeta", "papel que representa un ser vivo en el modelo"), ("energía", "capacidad para vivir, moverse y crecer"), ("límite", "algo que el modelo no muestra")],
  worked=[
      ("Mover una tarjeta", "Modelo: pasto → vicuña → puma. Se quita la tarjeta de la vicuña. ¿Qué le pasa al puma en este modelo?", ["Veo la flecha de la vicuña al puma.", "Sin vicuña, la flecha desaparece.", "El puma queda sin ese alimento."], "Queda sin ese alimento"),
      ("Encontrar un límite", "El modelo dice solo pasto → vicuña. En la realidad la vicuña también come otras plantas. ¿Qué límite tiene?", ["Comparo modelo y realidad.", "La realidad tiene más alimentos.", "El modelo muestra uno solo."], "No muestra todo lo que come la vicuña"),
  ],
  mistakes=[
      ("Creer que cada animal come un solo alimento.", "Muchos animales comen varios alimentos.", "Piensa en redes alimentarias."),
      ("Olvidar los descomponedores.", "Sin ellos, los restos no volverían al suelo.", "Agrega una tarjeta de descomponedores."),
  ],
  rec=[
      ("¿Una red alimentaria tiene una cadena o varias cadenas unidas?", "Varias unidas", "Esa es la definición."),
      ("¿Qué representa cada tarjeta del modelo?", "Un ser vivo", "Cada tarjeta es un eslabón."),
      ("Completa con «alimento» o «sombra»: la flecha muestra hacia dónde pasa el ______.", "Alimento", "Va del alimento al que lo come."),
  ],
  und=[
      ("¿Por qué una cadena es un modelo simple? A) Porque muestra solo una parte. B) Porque es falsa.", "A", "Muestra una parte de lo que ocurre."),
      ("Si agregas una tarjeta de «hongos» que descomponen restos, ¿qué rol agregas?", "Descomponedor", "Los hongos descomponen restos."),
      ("¿Cuál es un límite de la cadena pasto → vicuña → puma? A) No muestra todos los alimentos. B) Tiene tres eslabones.", "A", "El número de eslabones no es un límite."),
  ],
  app=[
      ("En la red: pasto → vicuña → puma y pasto → ratón → puma. ¿Cuántos animales comen pasto?", "2", "La vicuña y el ratón."),
      arith("Una red tiene 2 cadenas de 3 eslabones que comparten el primero. ¿Cuántos seres vivos distintos hay?", "3+2", "El primero es el mismo, así que sumamos 3 más 2."),
      ("Predice con el modelo: se saca la tarjeta del puma. ¿Qué pasará con las vicuñas, que ya no son comidas?", "Podrían aumentar", "Al no ser cazadas, su número puede subir."),
  ],
  rea=[
      ("Luis dice que, como el modelo es solo una cadena, lo que muestra es lo único que pasa. ¿Está bien? Responde Sí o No y explica.", "No; la realidad tiene más relaciones", "El modelo es una parte."),
      ("Datos de ejemplo. Una red tiene 4 animales y 2 plantas. Si desaparecen las 2 plantas, ¿qué pasa con los animales herbívoros?", "Se quedan sin alimento", "Dependen de las plantas."),
  ],
  cha=[
      ("Dibuja con palabras una red con: pasto, vicuña, ratón y puma. Escribe las flechas.", "Pasto → vicuña → puma; pasto → ratón → puma", "Así se muestran dos cadenas unidas."),
      ("Escribe un límite de tu modelo de cadena y cómo lo mejorarías.", "No muestra los descomponedores; agregaría una tarjeta de hongos", "Reconoce lo que falta y propone agregar."),
  ],
  context=[("Un parque tiene en un modelo: 3 plantas, 2 herbívoros, 1 carnívoro y 1 descomponedor. Cada ser vivo tiene una tarjeta. ¿Cuántas tarjetas hay?", "7", "3 + 2 + 1 + 1 = 7.")],
  selfcheck=[("¿Qué es una red alimentaria?", "Varias cadenas unidas", "Muestra que los animales comen más de un alimento."), ("¿Qué muestra una flecha?", "Hacia dónde pasa el alimento", "Va del alimento al consumidor."), ("Nombra un límite de una cadena.", "No muestra todos los alimentos ni los descomponedores", "Simplifica la realidad.")],
  open_task=task("Haz seis tarjetas de papel con: pasto, vicuña, ratón, puma, lechuza y hongos. Ordénalas en una red con flechas. Escribe qué pasa con cada animal si falta el pasto y un límite de tu modelo. Hazlo con papel y lápiz; no uses tijeras sin ayuda de una persona adulta.", "Pasto → vicuña → puma; pasto → ratón → lechuza. Sin pasto, no hay alimento para vicuña ni ratón. Límite: la vicuña también come otras plantas, y el modelo no las muestra.", ["una red con al menos dos cadenas", "predicción con razón", "un límite"], ["red dibujada", "texto corto"], ["flechas al revés", "no explicar la predicción"], "Pregunta por qué dibujó cada flecha y si cambiaría alguna."),
  reinforce="Dibuja una red con dos cadenas que compartan el productor.",
  extend="Explica por qué una red alimentaria es más parecida a la realidad que una cadena sola.")

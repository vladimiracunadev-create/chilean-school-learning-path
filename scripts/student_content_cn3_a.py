"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 01 (necesidades y estructuras de las plantas) y OA 02 (diversidad de plantas de Chile)."""
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


OA1, OA2 = "CN03 OA 01", "CN03 OA 02"

# ---------------------------------------------------------------- OA 01
L(OA1, 1,
  materials="Este cuaderno, lápiz y lápices de colores. Si quieres, una planta de tu casa o de una plaza para mirarla sin arrancarla ni probarla.",
  use="Aprenderé a hacer preguntas sobre las plantas que se puedan probar. Sirve para averiguar con evidencia qué necesita una planta y no quedarme solo con ideas.",
  prior=["Sé que una planta es un ser vivo.", "Sé observar con los ojos y anotar lo que veo."],
  explain=[
      "Una planta es un ser viviente. Para vivir y crecer necesita agua, luz del Sol, aire y suelo. También necesita una temperatura adecuada: ni demasiado fría ni demasiado caliente. Las plantas no se mueven de lugar, por eso toman lo que necesitan del sitio donde crecen. Si pasan muchos días sin luz, suelen ponerse pálidas y débiles.",
      "Los científicos empiezan con una pregunta que se puede probar, por ejemplo: ¿crece más un poroto con luz que uno sin luz? Después hacen una predicción, que es lo que creen que pasará. Luego observan y anotan lo que de verdad pasó. Lo que se anota es la evidencia.",
      "Una observación es algo que ves, mides o cuentas: «la hoja mide 6 cm». Una predicción es lo que crees que pasará: «sin agua, la planta se secará». Una opinión, como «esta planta es linda», no sirve para probar nada. Tampoco sirve adivinar sin mirar.",
  ],
  vocab=[("necesidad", "algo que un ser vivo debe tener para vivir"), ("pregunta que se puede probar", "pregunta que se responde observando, midiendo o contando"), ("predicción", "lo que creo que pasará antes de probar"), ("observación", "lo que veo, mido o cuento"), ("evidencia", "datos anotados que muestran lo que pasó")],
  worked=[
      ("Convertir una idea en una pregunta", "Mateo ve una planta con las hojas caídas y piensa: «Tiene sed». ¿Qué pregunta puede probar?", ["Piensa qué puede cambiar: si la riega, ¿se levantan las hojas?", "Escribe la pregunta con algo que se pueda mirar.", "Anota qué mirará: si las hojas se levantan en dos días."], "¿Se levantan las hojas de la planta si la riego?"),
      ("Observación o predicción", "Frases: «La planta A tiene 5 hojas verdes hoy» y «La planta A tendrá 8 hojas la próxima semana». ¿Cuál es la observación?", ["Una observación habla de lo que ya se ve ahora.", "La primera frase cuenta hojas que existen hoy.", "La segunda dice lo que pasará más adelante: es una predicción."], "La primera frase es la observación"),
  ],
  mistakes=[
      ("Decir «la planta está triste» al ver hojas caídas.", "Se pone un sentimiento en lugar de evidencia.", "Anota lo que ves: hojas caídas y tierra seca."),
      ("Decir «las plantas solo necesitan agua».", "Se olvidan las otras necesidades.", "Una planta necesita agua, luz, aire y suelo, y una temperatura adecuada."),
  ],
  rec=[
      ("¿Una planta es un ser vivo? Responde Sí o No.", "Sí", "Una planta nace, crece y necesita agua y luz, como los seres vivos."),
      ("Elige las dos cosas que necesita una planta: agua, luz del Sol, helado, televisión.", "Agua y luz del Sol", "El agua y la luz son necesidades de las plantas."),
      ("Completa con «ves» o «crees»: una predicción es lo que ______ que pasará.", "Crees", "La predicción es una idea antes de probar."),
  ],
  und=[
      ("¿Cuál pregunta se puede probar? A) ¿Es linda la albahaca? B) ¿Crece más un poroto con luz que uno sin luz?", "B", "Se puede medir y comparar cuánto crece cada poroto."),
      ("Marta anota: «La hoja mide 6 cm». ¿Es una observación o una predicción?", "Observación", "Dice algo que se midió, no algo que pasará."),
      ("¿Por qué la frase «me gusta esta planta» no sirve como evidencia?", "Porque es una opinión y no se puede medir ni contar", "La evidencia debe ser algo que se pueda mirar, medir o contar."),
  ],
  app=[
      arith("La planta A tenía 4 hojas el lunes y 7 hojas el viernes. ¿Cuántas hojas nuevas salieron?", "7-4", "Se resta lo que había al inicio a lo que había al final."),
      ("Una niña dejará una planta varios días sin luz. ¿Qué predicción es más acertada? A) Seguirá igual de verde y firme. B) Se pondrá pálida y débil.", "B", "Sin luz, las hojas pierden su color verde y la planta se debilita."),
      ("Ordena con letras los pasos de una investigación: A) observar y anotar, B) hacer la pregunta, C) hacer la predicción.", "B, C, A", "Primero se pregunta, luego se predice y al final se observa."),
  ],
  rea=[
      ("Ana ve una planta con las hojas caídas y dice: «Seguro le falta agua». ¿Ya tiene evidencia? Responde Sí o No y explica.", "No; solo vio hojas caídas y aún no probó regarla", "Una idea sin probar es una predicción, no evidencia."),
      ("Luis dice que a una planta amarilla le falta luz. Rosa dice que le sobra agua. ¿Cómo pueden saber quién tiene razón?", "Probando cada idea con una prueba y anotando lo que pasa", "Solo probar y anotar resultados permite decidir."),
  ],
  cha=[
      ("Una planta tenía tierra seca, hojas caídas y poca luz. La riegas y mejora. ¿Puedes asegurar que le faltaba agua y no luz?", "No; solo sabes que el agua ayudó, porque la luz no se probó", "Para saber de la luz habría que probar la luz."),
      ("Escribe una pregunta que se pueda probar sobre el agua y una planta, con algo que se pueda contar o medir.", "Por ejemplo: ¿Cuántas hojas se ponen amarillas si riego una vez por semana?", "Una buena pregunta nombra qué se cambia y qué se mide."),
  ],
  context=[("Julián deja dos plantas iguales en su pieza y les da el mismo riego. Una está junto a la ventana y la otra dentro de un armario cerrado. Después de varios días anota: ventana, hojas verdes y firmes; armario, hojas pálidas y caídas. ¿Qué necesidad de las plantas muestra su registro?", "La luz", "La única diferencia entre las plantas era la luz.")],
  selfcheck=[("¿Qué es la evidencia de una investigación?", "Los datos que se anotan sobre lo que pasó", "Es lo observado y medido, no lo que se supone."), ("¿Una predicción se escribe antes o después de probar?", "Antes", "La predicción es lo que se cree antes de ver el resultado."), ("Nombra tres cosas que necesita una planta.", "Agua, luz, aire o suelo (tres de ellas)", "Son necesidades de las plantas vistas en la clase.")],
  open_task=task("Elige una de estas preguntas: A) ¿Crece más un poroto con luz que uno sin luz? B) ¿Se secan más rápido las hojas de una planta sin agua? Escribe tu predicción y qué vas a mirar o medir. Con una persona adulta, anota durante tres días qué observas en una planta de tu casa. No pruebes ni comas ninguna planta.", "Elegí B. Predigo que sin agua las hojas se secarán antes. Miraré el color y si las hojas se caen. Día 1: verdes. Día 3: una hoja un poco caída.", ["elige una pregunta que se puede probar", "escribe una predicción", "anota al menos dos observaciones con fecha"], ["tabla con tres días de observaciones", "predicción escrita"], ["anotar opiniones en vez de lo que se ve", "no escribir la predicción antes"], "Revisa que cada anotación sea algo que se ve o se mide, y pregunta qué cambiaría su predicción."),
  reinforce="Mira una planta de tu casa o de una plaza y escribe tres observaciones: color, tamaño y cantidad de hojas.",
  extend="Escribe una pregunta que se pueda probar sobre una necesidad de las plantas distinta del agua y de la luz.")

L(OA1, 2,
  materials="Este cuaderno, lápiz y regla. Si lo haces en casa con una persona adulta: dos vasos de plástico con tierra, semillas de lenteja o poroto y un lugar con luz.",
  use="Aprenderé a investigar el agua y la luz con una prueba justa. Sirve para saber qué provoca un cambio en una planta y no confundir dos causas.",
  prior=["Sé que una planta necesita agua y luz.", "Sé que una predicción se escribe antes de probar."],
  explain=[
      "Una variable es algo que puede cambiar en una investigación, como el agua, la luz o el tamaño de la planta. En una prueba justa se cambia una sola variable: la que quiero investigar. Todo lo demás se deja igual. Lo que se deja igual se llama constante.",
      "Para investigar el agua uso dos plantas iguales, en vasos iguales, con la misma tierra y la misma luz. A una la riego y a la otra no. Cada día mido y anoto en una tabla. Si cambio también la luz, ya no sabré cuál de las dos cosas produjo el resultado.",
      "Para investigar la luz hago lo contrario: las dos plantas reciben el mismo riego, pero una está en un lugar con luz y la otra en un lugar oscuro, como un armario. Después de varios días comparo el color y la firmeza de las hojas y escribo mi conclusión. Mi conclusión solo vale para lo que probé.",
  ],
  vocab=[("variable", "algo que puede cambiar en una investigación"), ("constante", "lo que se deja igual en una prueba justa"), ("prueba justa", "prueba donde cambia una sola variable"), ("comparar", "mirar dos cosas para ver en qué se parecen y en qué se diferencian"), ("conclusión", "respuesta a la pregunta que se apoya en la evidencia")],
  worked=[
      ("Qué cambia y qué se queda igual", "Dos porotos iguales en vasos iguales, con la misma tierra, junto a la misma ventana. A recibe 3 cucharadas de agua cada día. B no recibe agua. ¿Qué cambia? ¿Qué es constante?", ["Miro qué es distinto entre A y B: solo el agua.", "Miro qué es igual: tipo de poroto, vaso, tierra y lugar.", "Lo distinto es la variable; lo igual son las constantes."], "Cambia el agua; son constantes el poroto, el vaso, la tierra y el lugar"),
      ("Una prueba que no es justa", "La planta A está al sol y con agua. La planta B está a la sombra y sin agua. B se pone débil. ¿Se puede decir que fue por falta de luz?", ["Cuento cuántas cosas cambian entre A y B.", "Cambian dos: la luz y el agua.", "Con dos cambios no sé cuál produjo el resultado."], "No, porque cambiaron la luz y el agua a la vez"),
  ],
  mistakes=[
      ("Cambiar el agua y la luz a la vez.", "Con dos cambios no se sabe cuál causó el resultado.", "Cambia una sola variable y deja iguales las demás."),
      ("Usar una planta grande y otra pequeña en la misma prueba.", "La diferencia de tamaño ya cambia el resultado.", "Usa plantas del mismo tipo y del mismo tamaño."),
  ],
  rec=[
      ("En una prueba justa, ¿cuántas variables cambias a propósito: una o dos?", "Una", "Cambiar una sola permite saber qué produjo el resultado."),
      ("Dos plantas son iguales. A una le das agua y a la otra no. ¿Qué cambia: el agua o el tipo de planta?", "El agua", "Las plantas son iguales; solo el riego es distinto."),
      ("Completa con «variable» o «constante»: lo que se deja igual en una prueba justa es la ______.", "Constante", "La constante es lo que no cambia en la prueba."),
  ],
  und=[
      ("¿Por qué las dos plantas deben tener el mismo tamaño al empezar?", "Para que la diferencia final se deba solo a la variable que se cambió", "Si no son iguales, el tamaño podría explicar la diferencia."),
      ("¿Cuál es una prueba justa sobre luz? A) Una planta en la ventana con agua y otra en el armario sin agua. B) Dos plantas con el mismo riego, una en la ventana y otra en el armario.", "B", "Solo cambia la luz; el agua es igual."),
      ("Dos plantas reciben el mismo riego; una está en la ventana y la otra en el armario. ¿Qué se deja igual: el riego o el lugar?", "El riego", "El lugar es lo que cambia; el riego es constante."),
  ],
  app=[
      arith("La planta A (con agua) midió 5 cm el día 1 y 12 cm el día 7. ¿Cuántos centímetros creció?", "12-5", "Se resta la altura inicial a la final."),
      arith("La planta B (sin agua) midió 5 cm el día 1 y 5 cm el día 7. La A creció de 5 cm a 12 cm. ¿Cuántos centímetros más creció la A que la B?", "12-5-(5-5)", "Se calcula cuánto creció cada una y se comparan."),
      ("Quieres probar la luz. Las dos plantas reciben un vaso de agua al día y tienen la misma tierra. ¿Qué variable cambias?", "La luz", "Si el agua y la tierra son iguales, lo que cambia es la luz."),
  ],
  rea=[
      ("Pedro puso la planta A al sol con agua y la B a la sombra sin agua. La B se debilitó. Pedro dice: «Fue por la falta de luz». ¿Tiene evidencia suficiente? Responde Sí o No y explica.", "No; cambió dos cosas a la vez, luz y agua", "No sabe si fue la luz o el agua."),
      ("Elena riega la planta A con un vaso al día y la B con dos vasos al día. Las dos están junto a la ventana. ¿Qué variable investiga Elena?", "La cantidad de agua", "Lo único distinto es cuánta agua recibe cada planta."),
  ],
  cha=[
      ("Un niño quiere saber si una planta crece mejor en tierra de jardín o en arena. Escribe qué cambia y una cosa que debe dejar igual.", "Cambia el tipo de suelo; deja igual el agua, la luz o la planta", "Solo el suelo debe cambiar."),
      ("Tras 7 días, una planta con luz tiene hojas verdes y otra sin luz las tiene pálidas. ¿Qué conclusión es correcta? A) Las plantas no necesitan luz. B) En esta prueba, la planta sin luz se puso pálida.", "B", "La conclusión solo habla de lo que se vio en la prueba."),
  ],
  context=[("En el patio hay dos maceteros iguales con la misma planta y el mismo riego diario. El macetero 1 está al sol y el 2 está en la sombra. El lunes ambos medían 6 cm. El viernes el 1 medía 11 cm y el 2 medía 8 cm. ¿Cuántos centímetros más creció el macetero 1 que el 2?", "3", "El 1 creció 5 cm y el 2 creció 2 cm. Cálculo: (11 − 6) − (8 − 6) = 3.")],
  selfcheck=[("¿Qué es una constante en una prueba justa?", "Lo que se deja igual", "Se mantiene igual para saber qué produjo el cambio."), ("Si en una prueba cambian el agua y la luz, ¿la prueba es justa? Responde Sí o No.", "No", "Se cambiaron dos variables a la vez."), ("¿Qué se hace cada día en la prueba para tener evidencia?", "Medir y anotar en una tabla", "Los datos anotados son la evidencia.")],
  open_task=task("Diseña con una persona adulta una prueba justa sobre el agua. Usa dos vasos iguales con tierra y 3 semillas de lenteja en cada uno, en el mismo lugar con luz. Un vaso se riega con una cucharada de agua al día y el otro no se riega. Dibuja la tabla con cinco días, anota qué cambia y qué dejas igual, y escribe tu predicción. Las lentejas no se comen durante la prueba.", "Cambia el agua. Constantes: vaso, tierra, lentejas y lugar. Predicción: el vaso sin agua tendrá menos plantitas. Día 3: vaso con agua, dos brotes; sin agua, ningún brote.", ["nombra la variable que cambia", "nombra al menos dos constantes", "registra datos de varios días"], ["tabla de cinco días", "predicción y conclusión"], ["cambiar dos variables", "anotar sin fecha"], "Pregunta cuál sería la conclusión y qué limitación tiene si solo probó con lentejas."),
  reinforce="Mira dos objetos iguales de tu casa, como dos vasos, y escribe una cosa que cambiarías y tres que dejarías igual para hacer una prueba justa.",
  extend="Diseña una prueba justa para saber si una planta necesita luz. Escribe la variable, tres constantes y qué vas a medir.")

L(OA1, 3,
  materials="Este cuaderno, lápiz y lápices de colores. En casa: un poroto o lenteja que ya tenga raíz (en algodón húmedo) o una zanahoria con una persona adulta.",
  use="Aprenderé qué hace la raíz de una planta. Sirve para entender por qué una planta necesita suelo con agua y por qué no se debe arrancar.",
  prior=["Sé que una planta necesita agua y suelo.", "Sé que la raíz, el tallo y las hojas son partes de una planta."],
  explain=[
      "La raíz es la parte de la planta que crece bajo la tierra. Tiene tres tareas. Sujeta la planta al suelo para que no se caiga ni la arrastre el viento. Absorbe agua del suelo. Y también absorbe sales minerales, que son los nutrientes que están disueltos en el agua.",
      "Cerca de la punta, la raíz tiene pelitos muy finos, llamados pelos absorbentes. Con ellos la planta toma el agua. Si arrancas una planta, esos pelitos se rompen y a la planta le cuesta mucho tomar agua de nuevo. Por eso las plantas no se arrancan sin necesidad.",
      "Hay raíces que además guardan alimento. La zanahoria es una raíz que guarda alimento para la planta, y nosotros la comemos. Si miras un poroto que está germinando en algodón húmedo, verás que la raíz sale primero y se ve blanca con pelitos finos.",
  ],
  vocab=[("raíz", "parte de la planta que crece bajo la tierra"), ("absorber", "tomar un líquido hacia adentro"), ("sales minerales", "nutrientes del suelo que la planta toma disueltos en el agua"), ("pelos absorbentes", "pelitos de la raíz que toman el agua"), ("sujetar", "mantener firme en un lugar")],
  worked=[
      ("Qué hace la raíz", "Un niño saca con cuidado una plantita de lenteja y ve una raíz con muchos pelitos blancos. ¿Para qué le sirven esos pelitos a la planta?", ["Recuerdo que los pelitos están cerca de la punta de la raíz.", "Se llaman pelos absorbentes y toman agua del suelo.", "Con el agua entran también sales minerales."], "Los pelitos toman agua y sales minerales del suelo"),
      ("Raíz o no raíz", "La zanahoria crece bajo la tierra y guarda alimento. ¿Es una raíz? ¿Por qué?", ["Miro dónde crece: bajo la tierra.", "Miro qué hace: guarda alimento para la planta.", "Eso coincide con las raíces que guardan alimento."], "Sí, la zanahoria es una raíz que guarda alimento"),
  ],
  mistakes=[
      ("Decir «la raíz solo sirve para sujetar la planta».", "Se olvida que también absorbe agua y sales minerales.", "La raíz sujeta, absorbe agua y absorbe sales minerales."),
      ("Decir «las hojas toman el agua del suelo».", "Se confunde la parte que absorbe.", "El agua del suelo la toma la raíz con sus pelos absorbentes."),
  ],
  rec=[
      ("¿La raíz crece sobre la tierra o bajo la tierra?", "Bajo la tierra", "La raíz está dentro del suelo."),
      ("¿Cuál es una tarea de la raíz: sujetar la planta o recibir la luz del Sol?", "Sujetar la planta", "La raíz mantiene la planta firme en el suelo."),
      ("Los pelitos de la raíz se llaman pelos ______. Completa: absorbentes o secos.", "Absorbentes", "Con ellos la planta absorbe agua."),
  ],
  und=[
      ("¿Qué toma la raíz del suelo además del agua?", "Sales minerales", "Son nutrientes disueltos en el agua del suelo."),
      ("¿Por qué no es buena idea arrancar una planta para ver sus raíces?", "Porque los pelitos se rompen y la planta no puede tomar agua", "Sin sus pelos absorbentes la planta no absorbe bien el agua."),
      ("Explica con tus palabras qué significa «absorber».", "Tomar un líquido hacia adentro", "La raíz toma el agua hacia adentro de la planta."),
  ],
  app=[
      ("Un poroto en algodón húmedo muestra primero una raíz blanca y después un tallito. ¿Qué parte sale primero?", "La raíz", "En la germinación sale primero la raíz."),
      arith("Una raíz de lenteja midió 2 cm el lunes y 7 cm el viernes. ¿Cuántos centímetros creció?", "7-2", "Se resta la medida inicial a la final."),
      ("Un niño dice: «La zanahoria que comí era una raíz». ¿Tiene razón? Responde Sí o No.", "Sí", "La zanahoria es una raíz que guarda alimento."),
  ],
  rea=[
      ("Una planta tiene la tierra mojada, pero se ve caída porque le cortaron todas las raíces. ¿Por qué no se recupera aunque haya agua?", "Porque sin raíces no puede absorber el agua", "La absorción de agua depende de la raíz."),
      ("Un árbol de un cerro tiene raíces largas y anchas. ¿Qué tarea de la raíz ayuda a que el viento no lo derribe?", "Sujetarlo al suelo", "Las raíces anclan el árbol a la tierra."),
  ],
  cha=[
      ("Dos lentejas germinan: A en algodón húmedo y B en algodón seco, en el mismo lugar. Tras tres días, A tiene raíz y B no. ¿Qué necesita la semilla para sacar su raíz? Explica.", "Agua, porque donde hubo agua salió la raíz", "La única diferencia era la humedad."),
      ("Un niño rompe sin querer la punta de las raíces finas de una plantita. Según la clase, ¿por qué ahora le costará tomar agua?", "Porque se rompen los pelos absorbentes, que están cerca de la punta", "Los pelos absorbentes toman el agua y están cerca de la punta."),
  ],
  context=[("En una plaza se riega un árbol joven cada semana. Un niño ve que el agua se hunde y desaparece. ¿Qué parte del árbol toma esa agua del suelo?", "La raíz", "La raíz absorbe el agua con sus pelos absorbentes.")],
  selfcheck=[("¿Qué dos cosas absorbe la raíz?", "Agua y sales minerales", "Son lo que la planta toma del suelo."), ("¿Qué parte de la raíz toma el agua: los pelos absorbentes o la punta de la hoja?", "Los pelos absorbentes", "Son los pelitos de la raíz."), ("¿Para qué sirve que la raíz sujete la planta?", "Para que no se caiga ni la arrastre el viento", "Mantiene la planta firme.")],
  open_task=task("Con una persona adulta, haz germinar un poroto o una lenteja en algodón húmedo dentro de un vaso de plástico, en un lugar con luz suave. Dibuja la raíz cada día durante cinco días, con su medida en centímetros. Rotula el dibujo con las palabras raíz, pelos absorbentes y tallito si los ves. Si no tienes semillas, dibuja y rotula la raíz de una zanahoria.", "Día 1: sin raíz. Día 3: raíz blanca de 1 cm. Día 5: raíz de 3 cm con pelitos finos. Rótulos: raíz y pelos absorbentes.", ["dibuja la raíz con rótulos", "anota la medida de varios días", "escribe una tarea de la raíz"], ["cinco dibujos con medidas", "frase sobre la tarea de la raíz"], ["rotular mal las partes", "no anotar medidas"], "Revisa que las medidas aumenten con los días y pregunta qué tarea de la raíz muestran los pelitos."),
  reinforce="Dibuja una planta con sus raíces bajo la tierra y flechas que muestren hacia dónde entra el agua.",
  extend="Averigua con una persona adulta otra raíz que comemos, como la betarraga o el rábano, y dibuja dónde crece.")

L(OA1, 4,
  materials="Este cuaderno y lápices de colores. Para el experimento con una persona adulta: un tallo de apio con hojas, un vaso con agua y colorante para alimentos.",
  use="Aprenderé qué hacen el tallo y las hojas. Sirve para entender cómo el agua llega a todas las partes de la planta y cómo la planta fabrica su alimento.",
  prior=["Sé que la raíz absorbe agua y sales minerales.", "Sé que una planta necesita luz, aire y agua."],
  explain=[
      "El tallo es la parte de la planta que sostiene las hojas, las flores y los frutos. Los lleva hacia la luz. Por dentro tiene tubitos muy finos. Por ellos el agua y las sales minerales suben desde la raíz hasta las hojas.",
      "Las hojas reciben la luz del Sol. También toman aire por agujeros muy pequeños. Con la luz, el agua y el aire, las hojas fabrican el alimento de la planta. Ese alimento después viaja por el tallo a las otras partes, como la raíz y los frutos.",
      "Puedes ver los tubitos del tallo con un experimento. Una persona adulta corta la base de un tallo de apio con hojas y lo pone en un vaso con agua y colorante para alimentos. Después de un día, el tallo y las hojas muestran líneas de color. El agua subió por los tubitos del tallo.",
  ],
  vocab=[("tallo", "parte de la planta que sostiene las hojas y lleva agua y alimento"), ("hoja", "parte de la planta que recibe luz y fabrica alimento"), ("alimento de la planta", "sustancia que la planta fabrica con luz, agua y aire"), ("tubitos", "conductos muy finos dentro del tallo"), ("sostener", "mantener algo en alto")],
  worked=[
      ("Seguir el camino del agua", "El agua entra a la planta por los pelos de la raíz y llega hasta las hojas. ¿Por dónde sube en medio?", ["Empiezo por donde entra: la raíz.", "Después sube por los tubitos del tallo.", "Termina llegando a las hojas."], "Sube por el tallo"),
      ("Leer un experimento con colorante", "El apio en agua con colorante azul tiene, al día siguiente, líneas azules en el tallo y las hojas. ¿Qué muestra?", ["Las líneas azules están dentro del tallo.", "El colorante viajó con el agua.", "Entonces el agua sube por el tallo hasta las hojas."], "Muestra que el agua sube por los tubitos del tallo hasta las hojas"),
  ],
  mistakes=[
      ("Decir «la hoja fabrica alimento con agua y aire, sin luz».", "Se olvida la luz del Sol.", "Las hojas necesitan luz, agua y aire para fabricar alimento."),
      ("Decir «el tallo solo sirve para que la planta se vea alta».", "Se olvida que lleva agua y sostiene hojas.", "El tallo sostiene la planta y lleva agua y alimento por sus tubitos."),
  ],
  rec=[
      ("¿Qué parte de la planta sostiene las hojas y las flores: el tallo o la raíz?", "El tallo", "El tallo las lleva hacia la luz."),
      ("¿Qué parte de la planta recibe la luz del Sol: las hojas o las raíces?", "Las hojas", "Las hojas están al aire, donde llega la luz."),
      ("El agua sube por unos tubitos del ______. Completa con tallo o pétalo.", "Tallo", "Los tubitos del tallo llevan el agua."),
  ],
  und=[
      ("Nombra las tres cosas que usan las hojas para fabricar alimento.", "Luz, agua y aire", "Las hojas fabrican alimento con esas tres cosas."),
      ("¿Qué muestran las líneas de color en el tallo del apio?", "Por dónde sube el agua", "El colorante viaja con el agua por los tubitos."),
      ("¿Hacia dónde viaja el alimento que fabrican las hojas?", "Hacia las otras partes de la planta", "Va por el tallo a la raíz, las flores y los frutos."),
  ],
  app=[
      ("Ordena el camino del agua con letras: A) hojas, B) raíz, C) tallo.", "B, C, A", "El agua entra por la raíz, sube por el tallo y llega a las hojas."),
      arith("Un tallo de apio con colorante tenía líneas de color de 3 cm el primer rato. Después de un día las líneas llegaban a 11 cm. ¿Cuántos centímetros más subió el color?", "11-3", "Se resta lo que había al comienzo al resultado final."),
      ("Una planta tiene el tallo roto bajo las hojas. ¿Qué parte del camino del agua se corta: de la raíz a las hojas o de las hojas al Sol?", "De la raíz a las hojas", "Los tubitos del tallo conectan la raíz con las hojas."),
  ],
  rea=[
      ("Una rama con hojas se corta y queda en un vaso con agua. Al día siguiente las hojas siguen firmes. ¿Qué parte de la rama les llevó el agua?", "El tallo", "El agua sube por los tubitos del tallo."),
      ("Un niño dice: «Si tapo las hojas con papel negro varios días, la planta fabricará menos alimento». ¿Qué necesidad de la fabricación de alimento está probando?", "La luz", "El papel negro bloquea la luz."),
  ],
  cha=[
      ("Un niño dice: «El color del apio solo manchó por fuera». Una persona adulta abre el tallo con un cuchillo. ¿Qué debe verse adentro para probar que el agua subió por dentro del tallo?", "Líneas o puntitos de color dentro del tallo", "El color dentro del tallo muestra que el agua subió por sus tubitos."),
      ("Un girasol tiene un tallo largo. Explica con una idea por qué eso le sirve para recibir luz.", "Porque el tallo lleva las hojas hacia arriba, donde llega la luz", "El tallo sostiene las hojas hacia la luz."),
  ],
  context=[("Una persona riega un helecho seco y las puntas de las hojas se ponen verdes de nuevo al cabo de unos días. ¿Por qué parte de la planta tuvo que pasar el agua para llegar a las hojas?", "Por el tallo", "El agua que absorbe la raíz sube por el tallo hasta las hojas.")],
  selfcheck=[("¿Qué hacen las hojas con la luz, el agua y el aire?", "Fabrican el alimento de la planta", "Es la tarea principal de las hojas."), ("¿Qué parte lleva el agua desde la raíz hasta las hojas?", "El tallo", "El tallo tiene tubitos que llevan el agua."), ("¿La planta puede fabricar alimento en un lugar completamente oscuro? Responde Sí o No.", "No", "Sin luz no se fabrica alimento.")],
  open_task=task("Con una persona adulta, prepara el experimento del apio: un tallo con hojas, cortado en la base por la persona adulta, dentro de un vaso con agua y unas gotas de colorante para alimentos. Mira cada pocas horas durante un día. Dibuja el tallo al inicio y al final, pinta por dónde sube el color y escribe la conclusión. No comas el apio del experimento. Sin materiales, usa este dato: tras un día, el color llegó a las hojas.", "Inicio: tallo blanco. Final: líneas azules en el tallo y hojas. Conclusión: el agua sube por el tallo hasta las hojas.", ["dibuja el antes y el después", "pinta por dónde sube el color", "escribe una conclusión con evidencia"], ["dos dibujos rotulados", "conclusión escrita"], ["decir que el color sube por fuera", "no escribir qué muestra"], "Pregunta cómo supo que el color subió por dentro del tallo y no por fuera."),
  reinforce="Dibuja una planta con raíz, tallo y hojas, y escribe una tarea de cada parte.",
  extend="Explica cómo se relacionan la raíz, el tallo y las hojas para que una planta reciba agua y fabrique alimento.")

# ---------------------------------------------------------------- OA 02
L(OA2, 1,
  materials="Este cuaderno, lápiz y lápices de colores. Una planta que puedas mirar en una plaza, jardín o macetero, sin arrancarla ni probarla.",
  use="Aprenderé a describir una planta por lo que se ve. Sirve para registrar plantas con exactitud y no inventar un nombre que no sé.",
  prior=["Sé que las plantas tienen raíz, tallo y hojas.", "Sé que observar es mirar con atención y anotar."],
  explain=[
      "Para identificar una planta primero hay que observar sus rasgos, que son las características que se ven. Un rasgo es el tamaño, la forma de la hoja, el color de la flor o si la planta tiene tronco. Se anotan los rasgos antes de decir un nombre.",
      "Según su tallo, las plantas se agrupan en tres tipos. Un árbol tiene un tronco principal grueso y es alto. Un arbusto tiene varios tallos duros que salen desde el suelo y es más bajo que un árbol. Una hierba tiene el tallo blando y verde, y es baja.",
      "En la hoja se observa su forma (larga, redonda o con puntas), su borde (liso o con dientes) y su color. Si no conozco el nombre de una planta, escribo «no sé su nombre» y registro mis observaciones. No debo adivinar ni tocar plantas que no conozco. Tampoco las debo probar, porque algunas hacen daño.",
  ],
  vocab=[("rasgo", "característica que se puede ver de una planta"), ("árbol", "planta alta con un tronco principal grueso"), ("arbusto", "planta de varios tallos duros que salen desde el suelo"), ("hierba", "planta baja de tallo blando y verde"), ("registro", "anotación de lo que se observó")],
  worked=[
      ("Clasificar por tipo de tallo", "La planta A mide 6 m, tiene un solo tronco grueso y las ramas salen arriba. ¿Es árbol, arbusto o hierba?", ["Miro el tallo: es un tronco grueso y único.", "Miro la altura: es alta.", "Esos rasgos son de un árbol."], "Es un árbol"),
      ("Describir sin adivinar", "Una niña ve una planta baja de tallo blando, hojas redondas con borde liso y flores amarillas. No sabe su nombre. ¿Qué escribe?", ["Anota el tipo: hierba baja de tallo blando.", "Anota hoja y flor: redonda con borde liso, flor amarilla.", "Escribe que no sabe el nombre."], "Hierba baja, hojas redondas con borde liso, flores amarillas, nombre desconocido"),
  ],
  mistakes=[
      ("Decir «es un cardo» sin mirar sus rasgos.", "Se adivina un nombre sin evidencia.", "Primero anota los rasgos y después busca el nombre en una fuente."),
      ("Decir «es árbol porque es verde».", "El color no decide el tipo de planta.", "El tipo se decide por el tronco y la altura."),
  ],
  rec=[
      ("Una planta tiene un solo tronco grueso y es alta. ¿Es árbol o hierba?", "Árbol", "Un tronco grueso único y gran altura son rasgos de árbol."),
      ("Una planta baja con el tallo blando y verde, ¿es hierba o arbusto?", "Hierba", "El tallo blando es rasgo de hierba."),
      ("Si no sabes el nombre de una planta, ¿escribes un nombre inventado o «no sé su nombre»?", "No sé su nombre", "No se debe adivinar ni inventar un nombre."),
  ],
  und=[
      ("¿Qué es un rasgo de una planta?", "Una característica que se puede ver", "Por ejemplo, la forma de la hoja."),
      ("¿En qué se diferencia un arbusto de un árbol?", "El arbusto tiene varios tallos desde el suelo y es más bajo", "El árbol tiene un tronco principal grueso."),
      ("¿Por qué no se prueban ni se tocan las plantas que no se conocen?", "Porque algunas pueden hacer daño", "Una planta desconocida puede ser peligrosa."),
  ],
  app=[
      ("Ficha: planta con varios tallos duros que salen del suelo, altura 2 m. ¿Es árbol, arbusto o hierba?", "Arbusto", "Varios tallos duros desde el suelo y baja altura son rasgos de arbusto."),
      ("La hoja de la planta A es larga, con borde liso. La de la planta B es redonda, con borde con dientes. ¿Qué dos rasgos de la hoja se están comparando?", "La forma y el borde", "Una hoja es larga y la otra redonda; una tiene borde liso y la otra con dientes."),
      arith("Una hierba midió 12 cm el lunes y 20 cm el domingo. ¿Cuántos centímetros creció?", "20-12", "Se resta la medida inicial a la final."),
  ],
  rea=[
      ("Dos plantas tienen hojas verdes y flores amarillas, pero una es árbol y otra es hierba. ¿Qué rasgos sirven para distinguirlas: color de flor o tipo de tallo y altura?", "Tipo de tallo y altura", "Ambas coinciden en color; difieren en el tallo."),
      ("Sofía anota: «Es una planta bonita y simpática». ¿Es un buen registro? Responde Sí o No y explica.", "No; son opiniones y no rasgos que se vean o se midan", "Un buen registro anota rasgos observables."),
  ],
  cha=[
      ("Planta A: árbol de 8 m con hojas largas y borde liso. Planta B: arbusto de 2 m con hojas largas y borde liso. ¿Qué rasgo las distingue claramente?", "El tipo de tallo y la altura", "La hoja es igual en ambas."),
      ("Escribe tres rasgos que usarías para describir una planta de tu patio o de una plaza.", "Por ejemplo: tipo (árbol, arbusto o hierba), forma de la hoja y color de la flor", "Son rasgos observables."),
  ],
  context=[("En una plaza ves una planta de 1 m, con varios tallos duros que salen del suelo, hojas pequeñas redondas y flores blancas. Nadie sabe su nombre. ¿Qué tipo de planta es?", "Arbusto", "Varios tallos duros desde el suelo y 1 m de altura son rasgos de arbusto.")],
  selfcheck=[("¿Qué es un registro?", "Una anotación de lo que se observó", "Contiene rasgos y datos."), ("¿Cuál de estas tres tiene el tallo blando: árbol, arbusto o hierba?", "Hierba", "La hierba tiene tallo blando y verde."), ("¿Se debe adivinar el nombre de una planta que no conoces? Responde Sí o No.", "No", "Se anotan los rasgos y se busca el nombre en una fuente.")],
  open_task=task("Elige una planta de un macetero, patio o plaza. Con una persona adulta cerca, anota su fecha, el lugar, el tipo (árbol, arbusto o hierba), la forma y el borde de la hoja y el color de la flor o fruto, si los tiene. Dibuja una hoja. Si no sabes su nombre, escribe «no sé su nombre». No la arranques ni la pruebes. Si no puedes salir, describe la planta de este ejemplo: hierba baja, hojas largas de borde liso, flores amarillas.", "Fecha: 12 de mayo. Lugar: plaza. Tipo: arbusto de 1 m. Hoja: redonda, borde liso. Flor: blanca. Nombre: no sé su nombre.", ["anota al menos cuatro rasgos", "dibuja una hoja", "no inventa un nombre"], ["ficha con fecha y lugar", "dibujo de una hoja"], ["escribir opiniones", "inventar un nombre"], "Pide que cuente qué rasgo usó para decidir el tipo de planta y que corrija opiniones por observaciones."),
  reinforce="Dibuja una hoja de una planta de tu casa y escribe su forma, su borde y su color.",
  extend="Describe dos plantas distintas usando los mismos tres rasgos y escribe en qué se diferencian.")

L(OA2, 2,
  materials="Este cuaderno, lápiz y lápices de colores. Pide ayuda a una persona adulta para buscar información en un libro o en una ficha de un parque o jardín botánico.",
  use="Aprenderé qué es una planta autóctona y cómo comprobar que lo es con fuentes. Sirve para valorar las plantas propias de Chile y no confundirlas con las traídas de otros países.",
  prior=["Sé describir una planta por sus rasgos.", "Sé que tengo que anotar de dónde sale una información."],
  explain=[
      "Una planta autóctona, o nativa, es una planta que crece de forma natural en un lugar, sin que las personas la hayan traído desde lejos. Las plantas traídas de otros países se llaman introducidas. Unas autóctonas de Chile son el copihue, la araucaria, el quillay, el boldo y la palma chilena.",
      "El copihue es una trepadora de flores en forma de campana, rojas o blancas, y es la flor nacional de Chile. La araucaria es un árbol de hojas duras y puntiagudas de las montañas del sur; sus semillas se llaman piñones. El quillay es un árbol de la zona central: su corteza hace espuma con agua. El boldo tiene hojas aromáticas. La palma chilena es una palma muy alta de la zona central.",
      "Para saber si una planta es autóctona no basta mirarla. Hay que usar una fuente: un libro de botánica, la ficha de un jardín botánico o una persona experta. En la fuente se anota el nombre, el lugar de origen y quién lo dice. Algunas plantas muy comunes en Chile, como el eucalipto y el pino radiata, son introducidas.",
  ],
  vocab=[("autóctona", "planta que crece de forma natural en un lugar"), ("introducida", "planta traída de otro lugar por las personas"), ("fuente", "libro, ficha o persona que entrega información confiable"), ("flor nacional", "flor que representa a un país"), ("origen", "lugar donde una planta crece de forma natural")],
  worked=[
      ("Usar una ficha", "Ficha: «Quillay. Árbol de Chile central. Su corteza hace espuma con agua». ¿Es autóctona?", ["La ficha dice que es un árbol de Chile central.", "Eso indica que crece de forma natural en Chile.", "Entonces es una planta autóctona."], "Sí, el quillay es autóctono según la ficha"),
      ("No adivinar por la apariencia", "Un eucalipto es un árbol alto y muy común en Chile. ¿Se puede decir que es autóctono porque lo vemos en todas partes?", ["Que sea común no prueba su origen.", "La fuente dice que el eucalipto es introducido.", "Se confía en la fuente y no en la apariencia."], "No, es introducido aunque sea muy común"),
  ],
  mistakes=[
      ("Decir «es autóctona porque hay muchas en mi barrio».", "Que sea común no indica de dónde viene.", "Se revisa el origen en una fuente."),
      ("Decir «el pino radiata es autóctono de Chile porque hay bosques de pino».", "Se supone sin revisar una fuente.", "El pino radiata es introducido, aunque hoy se cultive mucho en Chile."),
  ],
  rec=[
      ("Una planta que crece de forma natural en Chile, ¿es autóctona o introducida?", "Autóctona", "Crece sin que la hayan traído de otro lugar."),
      ("¿Cuál es la flor nacional de Chile: copihue o girasol?", "Copihue", "El copihue es la flor nacional de Chile."),
      ("¿La araucaria crece en las montañas del sur o en el desierto del norte?", "En las montañas del sur", "La araucaria es un árbol de montañas del sur."),
  ],
  und=[
      ("¿Qué significa que una planta sea «introducida»?", "Que fue traída de otro lugar por las personas", "No crece de forma natural allí."),
      ("¿Por qué una ficha de un jardín botánico es una buena fuente?", "Porque da el nombre y el origen de la planta con información revisada", "Entrega datos confiables."),
      ("¿Qué se debe anotar al usar una fuente: solo el nombre o también de dónde sale la información?", "También de dónde sale la información", "Se anota la fuente para poder comprobarla."),
  ],
  app=[
      ("Tarjetas: A) copihue, B) eucalipto, C) quillay, D) pino radiata. Escribe las letras de las autóctonas de Chile.", "A y C", "El copihue y el quillay son autóctonos; los otros son introducidos."),
      arith("En un parque hay 9 quillayes y 6 boldos autóctonos. ¿Cuántas plantas autóctonas hay en total?", "9+6", "Se suman las plantas de cada tipo."),
      ("Una ficha dice: «Araucaria. Árbol de montañas del sur de Chile. Semillas: piñones». ¿Qué parte de la ficha da su origen?", "Árbol de montañas del sur de Chile", "Dice dónde crece de forma natural."),
  ],
  rea=[
      ("Un niño dice que el eucalipto es autóctono porque hay muchos en su ciudad. ¿Qué respondes?", "Que ser común no prueba el origen; hay que mirar una fuente", "El origen se comprueba con información confiable."),
      ("Dos amigas discuten si el boldo es autóctono. Una dice que sí «porque lo vio» y otra revisa una ficha del jardín botánico. ¿Cuál tiene mejor evidencia?", "La que revisó la ficha", "La ficha es una fuente confiable."),
  ],
  cha=[
      ("Una ficha dice que una planta «vino de Australia». ¿Es autóctona de Chile? Explica.", "No; fue traída de otro país", "Su origen está fuera de Chile."),
      ("Escribe dos fuentes que sirven para comprobar si una planta es autóctona.", "Por ejemplo: un libro de botánica y la ficha de un jardín botánico", "Son fuentes confiables."),
  ],
  context=[("En un parque de Chile central hay una placa: «Quillay. Árbol autóctono. Su corteza hace espuma con agua». Un grupo de niños cuenta 4 quillayes en una fila y 3 en otra. ¿Cuántos quillayes cuentan en total?", "7", "Se suman los de las dos filas. Cálculo: 4 + 3 = 7.")],
  selfcheck=[("¿Qué es una planta autóctona?", "Una planta que crece de forma natural en un lugar", "No fue traída por las personas."), ("Nombra una planta autóctona de Chile.", "Copihue, araucaria, quillay, boldo o palma chilena (una de ellas)", "Todas son autóctonas de Chile."), ("¿El eucalipto es autóctono o introducido?", "Introducido", "Fue traído de otro lugar.")],
  open_task=task("Elige una de estas fichas y úsala como fuente para completar una tarjeta. Copihue: trepadora de flor en forma de campana, roja o blanca, flor nacional de Chile. Araucaria: árbol de hojas duras de montañas del sur de Chile, semillas llamadas piñones. Boldo: planta de hojas aromáticas de Chile. En la tarjeta escribe nombre, rasgos, origen y de dónde sacaste la información. Dibuja la planta.", "Copihue. Rasgos: trepadora, flor roja en forma de campana. Origen: Chile. Fuente: ficha de este cuaderno. Es autóctona.", ["escribe nombre y rasgos", "anota el origen y la fuente", "dice si es autóctona"], ["tarjeta completa", "dibujo de la planta"], ["no citar la fuente", "decir que es autóctona sin evidencia"], "Revisa que la tarjeta nombre la fuente y que el origen venga de la ficha."),
  reinforce="Dibuja un copihue y una araucaria y escribe una frase que diga por qué son autóctonos.",
  extend="Pregunta a una persona de tu casa qué plantas autóctonas conoce y anota de dónde sabe que lo son.")

L(OA2, 3,
  materials="Este cuaderno, lápiz y una regla para hacer una tabla. Si puedes, mira los alimentos vegetales que hay en tu casa.",
  use="Aprenderé qué es un cultivo y cuáles son cultivos importantes en Chile. Sirve para saber de dónde vienen muchos alimentos y que no todo se cultiva en todas partes.",
  prior=["Sé que algunas plantas se comen.", "Sé que las plantas necesitan agua, luz y suelo."],
  explain=[
      "Un cultivo es una planta que las personas siembran y cuidan para obtener alimentos u otros productos. Un cultivo puede ser autóctono o introducido. Muchos cultivos importantes de Chile, como el trigo, la vid, el manzano y el palto, son plantas que se trajeron de otros lugares.",
      "Los cultivos no se dan igual en todo el país porque cada zona tiene un clima y un suelo distintos. La vid, el palto y el manzano se cultivan sobre todo en la zona central. El trigo se cultiva en el centro y el sur. El olivo se cultiva en el norte y en el centro; la aceituna de Azapa, en la Región de Arica y Parinacota, es conocida. La papa se cultiva sobre todo en el sur, incluida la isla de Chiloé, que pertenece a la Región de Los Lagos. La papa es originaria de América.",
      "Un cultivo nacional es uno que se cultiva en muchas regiones del país. Un cultivo regional es uno que es muy importante en una región. Cada cultivo da una parte distinta de la planta: del trigo comemos el grano, de la vid la uva, del manzano la manzana y de la papa el tubérculo, que es un tallo que crece bajo la tierra.",
  ],
  vocab=[("cultivo", "planta que las personas siembran y cuidan para obtener un producto"), ("región", "zona grande en que se divide el país"), ("clima", "tiempo habitual de un lugar durante el año"), ("grano", "semilla pequeña y seca que se come, como la del trigo"), ("tubérculo", "tallo que crece bajo la tierra y guarda alimento")],
  worked=[
      ("Leer una tabla de cultivos", "Tabla: Trigo, grano, centro y sur. Uva, fruta, zona central. Papa, tubérculo, sur. ¿Qué cultivo se da en el sur y en el centro?", ["Busco 'sur' en la tabla.", "El trigo aparece en centro y sur; la papa, en el sur.", "El trigo es el que está en las dos zonas."], "El trigo"),
      ("Cultivo y producto", "De una vid comemos la uva. ¿La uva es el cultivo o el producto?", ["El cultivo es la planta que se siembra: la vid.", "El producto es lo que se obtiene: la uva.", "La uva es el producto."], "La uva es el producto; el cultivo es la vid"),
  ],
  mistakes=[
      ("Decir «todos los cultivos crecen en todo Chile».", "Cada zona tiene clima y suelo distintos.", "Cada cultivo se da mejor en ciertas zonas del país."),
      ("Decir «un cultivo siempre es autóctono».", "Muchos cultivos fueron traídos de otros lugares.", "El trigo y la vid, por ejemplo, son plantas introducidas."),
  ],
  rec=[
      ("¿Un cultivo es una planta que las personas siembran y cuidan, o una que nace sola en el bosque?", "Que las personas siembran y cuidan", "Eso es un cultivo."),
      ("¿De qué planta viene la manzana: manzano o trigo?", "Manzano", "La manzana es el fruto del manzano."),
      ("¿Qué comemos del trigo: la raíz o el grano?", "El grano", "El grano del trigo se usa para hacer harina."),
  ],
  und=[
      ("Explica con tus palabras qué es una región de Chile.", "Una zona grande en que se divide el país", "Cada región tiene su propio territorio."),
      ("¿Por qué un cultivo se da mejor en unas zonas que en otras?", "Porque el clima y el suelo son distintos en cada zona", "Los cultivos necesitan ciertas condiciones."),
      ("¿La papa es un tubérculo que crece sobre la tierra o bajo la tierra?", "Bajo la tierra", "Es un tallo subterráneo que guarda alimento."),
  ],
  app=[
      ("Cultivos: trigo (centro y sur), olivo (norte y centro), papa (sur). ¿Cuál de ellos se da en el sur?", "El trigo y la papa", "Ambos aparecen con la zona sur."),
      arith("En un campo hay 12 hileras de papas y en otro campo hay 15 hileras de trigo. ¿Cuántas hileras hay en total?", "12+15", "Se suman las hileras de los dos campos."),
      ("Una tabla dice «Uva, zona central». Si vives en la zona central, ¿es probable que cerca se cultive uva? Responde Sí o No.", "Sí", "La tabla indica que se cultiva allí."),
  ],
  rea=[
      ("Nicolás dice que en el desierto del norte se cultivan manzanas, igual que en el centro. ¿Cómo comprobarías si tiene razón?", "Buscando en una tabla o en un libro dónde se cultiva el manzano", "Se comprueba con una fuente."),
      ("Dos cultivos: A se cultiva en casi todas las regiones; B solo en una región. ¿Cuál es nacional y cuál es regional?", "A es nacional y B es regional", "El nacional se cultiva en muchas regiones."),
  ],
  cha=[
      ("Una ficha dice: «Olivo. Se cultiva en el norte y en el centro de Chile». Otra dice: «Papa. Se cultiva en el sur, incluida Chiloé». ¿Cuál de los dos cultivos se da en una zona más cercana a Arica?", "El olivo", "El norte está más cerca de Arica que el sur."),
      ("Escribe un cultivo de tu región o de una región que conozcas y qué parte de la planta se come. Si no sabes uno, usa el trigo.", "Por ejemplo: trigo, se come el grano", "Une cultivo y producto."),
  ],
  context=[("En una feria venden 5 kilos de papas del sur, 8 kilos de manzanas de la zona central y 3 kilos de trigo en grano. ¿Cuántos kilos de frutas y tubérculos hay (papas más manzanas)?", "13", "Se suman papas y manzanas. Cálculo: 5 + 8 = 13.")],
  selfcheck=[("¿Qué es un cultivo?", "Una planta que se siembra y se cuida para obtener un producto", "Es el cultivo de una especie."), ("¿Qué comemos del trigo?", "El grano", "Se muele para hacer harina."), ("¿Todos los cultivos se dan igual en todo Chile? Responde Sí o No.", "No", "Cada zona tiene un clima y un suelo distintos.")],
  open_task=task("Completa esta tabla con los cultivos de la clase: trigo, vid, manzano, papa y olivo. Para cada uno escribe qué producto se obtiene y en qué zona de Chile se cultiva, usando solo los datos de la explicación. Luego escribe una pregunta que le harías a una persona de tu región sobre un cultivo cercano. Si en tu casa hay un alimento vegetal, escribe de qué planta viene.", "Trigo: grano, centro y sur. Vid: uva, zona central. Manzano: manzana, zona central. Papa: tubérculo, sur. Olivo: aceituna, norte y centro.", ["completa los cinco cultivos", "usa los datos de la explicación", "escribe una pregunta"], ["tabla de cinco cultivos", "pregunta para una persona de la región"], ["inventar zonas", "confundir el producto con la planta"], "Revisa que cada zona sea la de la explicación y que la pregunta sea sobre un cultivo cercano."),
  reinforce="Escribe el nombre de tres alimentos vegetales de tu casa y de qué planta salen.",
  extend="Averigua con una persona adulta qué se cultiva cerca de donde vives y anota la fuente de tu información.")

L(OA2, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Una planta de un macetero, patio o plaza que puedas mirar con una persona adulta.",
  use="Aprenderé a hacer un registro de una planta con cuidado y respeto. Sirve para guardar datos confiables sin dañar las plantas ni a las personas que las conocen.",
  prior=["Sé describir una planta por sus rasgos.", "Sé que una fuente respalda una información."],
  explain=[
      "Un buen registro de una planta tiene la fecha y el lugar donde la viste, su tipo (árbol, arbusto o hierba), los rasgos de la hoja, la flor y el fruto, un dibujo y la fuente del nombre. Si no conoces el nombre, escribes «no sé su nombre» y anotas qué fuente vas a revisar.",
      "Para registrar con respeto, no arranques ni pises las plantas, ni las pruebes. En parques y áreas protegidas, como los parques nacionales, no se recogen plantas ni semillas. En un terreno ajeno se pide permiso a la persona dueña. Después de tocar una planta, es bueno lavarse las manos.",
      "Muchas personas y pueblos originarios conocen y usan plantas hace mucho tiempo. Ese saber pertenece a las personas que lo guardan. No se anota como si fuera propio ni se inventan usos o ceremonias. Si quieres saber cómo usa una comunidad una planta, se le pregunta con respeto a una persona de esa comunidad.",
  ],
  vocab=[("registro", "ficha donde se anotan los datos de lo que se observó"), ("respeto", "tratar con cuidado a las plantas, a las personas y a su saber"), ("área protegida", "lugar donde se cuida la naturaleza y no se pueden sacar plantas"), ("saber tradicional", "conocimiento que una comunidad guarda y transmite"), ("permiso", "autorización para entrar o tocar algo ajeno")],
  worked=[
      ("Completar una ficha", "Ficha: lugar plaza, fecha 5 de mayo, tipo arbusto, hoja ovalada de borde liso, flor blanca, nombre: sin revisar. ¿Qué falta para que el registro esté completo?", ["Reviso la lista: fecha, lugar, tipo, rasgos, dibujo y fuente.", "Hay fecha, lugar, tipo y rasgos.", "Faltan el dibujo y la fuente del nombre."], "Faltan el dibujo y la fuente del nombre"),
      ("Decidir con respeto", "Un niño ve una planta con semillas bonitas dentro de un parque nacional. ¿Puede llevarse algunas?", ["Un parque nacional es un área protegida.", "En un área protegida no se recogen plantas ni semillas.", "Puede dibujarlas y fotografiarlas."], "No, solo puede dibujarlas o fotografiarlas"),
  ],
  mistakes=[
      ("Arrancar una hoja o una flor «para llevar la muestra».", "Se daña la planta y puede estar prohibido.", "Dibuja o fotografía la planta en su lugar."),
      ("Escribir que una comunidad usa la planta para una ceremonia, sin saberlo.", "Se inventa un saber que no se conoce.", "Pregunta a una persona de la comunidad o cita una fuente."),
  ],
  rec=[
      ("¿Un registro debe incluir la fecha? Responde Sí o No.", "Sí", "La fecha permite saber cuándo se observó."),
      ("Si no sabes el nombre de la planta, ¿qué escribes: un nombre inventado o «no sé su nombre»?", "No sé su nombre", "No se inventa un nombre."),
      ("¿Se pueden recoger plantas en un parque nacional? Responde Sí o No.", "No", "Es un área protegida."),
  ],
  und=[
      ("Nombra tres datos que lleva un buen registro de una planta.", "Fecha, lugar y tipo (u otros rasgos)", "Son datos que la ficha de la clase pide."),
      ("¿Por qué no se arrancan las plantas que se observan?", "Porque se dañan y otros no podrán verlas", "Se cuida la planta."),
      ("¿A quién se le pregunta cómo usa una comunidad indígena una planta?", "A una persona de esa comunidad", "Es quien conoce y guarda ese saber."),
  ],
  app=[
      ("Ficha incompleta: tiene lugar, fecha, tipo y rasgos, pero no tiene dibujo ni fuente. ¿Cuántos elementos de la lista de seis faltan: dos o cuatro?", "Dos", "Faltan el dibujo y la fuente."),
      ("Un niño quiere registrar una planta en un jardín ajeno. ¿Qué debe hacer primero: pedir permiso o entrar corriendo?", "Pedir permiso", "En un terreno ajeno se pide permiso."),
      arith("Una ficha de registro tiene 6 elementos y una niña ya completó 4. ¿Cuántos le faltan?", "6-4", "Se resta lo completado del total."),
  ],
  rea=[
      ("Un niño dice: «En la plaza hay una planta que usan para una ceremonia». No tiene fuente. ¿Debe escribirlo en su registro?", "No, porque no sabe si es verdad ni tiene fuente", "Sin fuente es un dato no comprobado."),
      ("Dos registros: A dice «arbusto bonito, me gusta»; B dice «arbusto de 1 m, hoja ovalada, flor blanca, 5 de mayo, plaza». ¿Cuál es mejor registro?", "B", "Tiene rasgos y datos que se pueden comprobar."),
  ],
  cha=[
      ("Quieres saber el nombre de una planta del patio. Escribe una forma respetuosa de averiguarlo sin dañarla.", "Fotografiarla o dibujarla y buscar sus rasgos en un libro o preguntar a una persona experta", "Se averigua sin arrancarla."),
      ("Un registro dice que una planta es «autóctona» pero no muestra ninguna fuente. ¿Qué le falta?", "La fuente de esa información", "Sin fuente no se puede comprobar."),
  ],
  context=[("En una plaza una niña registra una hierba. Anota: fecha, lugar, tipo, hoja larga de borde liso y flor amarilla. Dibuja la hoja. No sabe el nombre y escribe «no sé su nombre; revisaré un libro». ¿Qué elemento del registro falta todavía para estar completo?", "La fuente del nombre", "Aún no consulta una fuente.")],
  selfcheck=[("¿Qué se hace con una planta que no se conoce: se prueba o se observa y se dibuja?", "Se observa y se dibuja", "Probarla puede ser peligroso."), ("¿Se deben inventar usos de plantas de un pueblo originario? Responde Sí o No.", "No", "Ese saber lo guarda la comunidad."), ("Nombra un dato de un buen registro.", "Fecha, lugar, tipo, rasgos, dibujo o fuente (uno de ellos)", "Son datos de un buen registro.")],
  open_task=task("Haz el registro de una planta con ayuda de una persona adulta. Incluye fecha, lugar, tipo, rasgos de la hoja, flor o fruto, un dibujo y la fuente del nombre. Si no sabes el nombre, escribe «no sé su nombre». No arranques nada. Si no puedes salir, completa el registro de esta planta: arbusto de 1 m, hoja ovalada de borde liso, flor blanca, vista en una plaza el 5 de mayo.", "5 de mayo, plaza. Arbusto de 1 m. Hoja ovalada de borde liso. Flor blanca. Nombre: no sé su nombre; revisaré un libro.", ["incluye al menos cinco elementos", "dibuja la planta", "no daña ni inventa datos"], ["ficha completa", "dibujo"], ["no anotar fuente", "arrancar la planta"], "Revisa que los datos se puedan comprobar y que la ficha no contenga opiniones ni usos inventados."),
  reinforce="Dibuja una planta de tu casa y escribe tres rasgos y una regla de respeto al registrarla.",
  extend="Escribe una pregunta respetuosa que harías a una persona mayor de tu familia sobre una planta de tu zona.")

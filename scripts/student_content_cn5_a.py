"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 01 (células y niveles de organización) y OA 02 (sistema digestivo)."""
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


OA1, OA2 = "CN05 OA 01", "CN05 OA 02"

# ---------------------------------------------------------------- OA 01
L(OA1, 1,
  materials="Este cuaderno y lápiz. No necesitas microscopio: las imágenes de microscopio se describen por escrito en los ejercicios.",
  use="Aprenderé qué es una célula y a separar lo que se observa de lo que se supone. Sirve para saber si un ser vivo tiene una célula o muchas.",
  prior=["Sé que las plantas, los animales y las personas son seres vivos.", "Sé que una observación es lo que se ve o se cuenta."],
  explain=[
      "Todos los seres vivos están formados por células. Una célula es la unidad más pequeña de un ser vivo: puede usar alimento, crecer y dar origen a otras células. Casi todas son tan pequeñas que no se ven a simple vista. Para verlas se usa el microscopio, un instrumento que agranda las imágenes.",
      "Algunos seres vivos tienen una sola célula y se llaman unicelulares, como las bacterias y las levaduras. Otros tienen muchas células y se llaman pluricelulares, como las personas, los árboles y los peces. Ser pequeño no significa ser unicelular: una hormiga es diminuta y tiene muchísimas células.",
      "Cuando miras una imagen de microscopio, una observación es lo que se ve o se cuenta, como «hay 12 cuadrados pegados». Una interpretación es lo que supones, como «esta planta está feliz». Solo las observaciones son evidencia. Con la evidencia puedes decidir si una muestra viene de un ser con una célula o con muchas.",
  ],
  vocab=[("célula", "unidad más pequeña de un ser vivo"), ("microscopio", "instrumento que agranda imágenes de cosas muy pequeñas"), ("unicelular", "ser vivo formado por una sola célula"), ("pluricelular", "ser vivo formado por muchas células"), ("evidencia", "observación o medición que apoya una explicación")],
  worked=[
      ("Clasificar seres vivos", "Una bacteria del yogur tiene 1 célula. Un pino tiene millones de células. Una levadura del pan tiene 1 célula. ¿Cuáles son unicelulares?", ["Reviso cuántas células tiene cada uno.", "La bacteria y la levadura tienen 1 célula.", "El pino tiene muchas células."], "Unicelulares: la bacteria y la levadura. Pluricelular: el pino"),
      ("Observación o interpretación", "Una niña escribe: «En la muestra hay 20 células pegadas» y «A las células les gusta estar juntas». ¿Cuál frase es evidencia?", ["Pregunto qué frase se puede contar o ver.", "Las 20 células se cuentan en la imagen.", "«Les gusta» es lo que ella supone."], "Es evidencia «En la muestra hay 20 células pegadas»"),
  ],
  mistakes=[
      ("Decir que un ser vivo es unicelular porque es muy pequeño.", "El tamaño no decide: una hormiga es pequeña y tiene muchas células.", "Cuenta o revisa cuántas células lo forman."),
      ("Anotar «las células se ven contentas» como observación.", "Un sentimiento no se ve ni se mide; es una suposición.", "Anota lo que se ve: forma, color y cantidad."),
  ],
  rec=[
      ("¿Con qué instrumento se ven las células muy pequeñas?", "Con un microscopio", "El microscopio agranda la imagen."),
      ("Una bacteria tiene una sola célula. ¿Es unicelular o pluricelular?", "Unicelular", "Uni significa una sola célula."),
      ("Completa con «células» o «huesos»: todos los seres vivos están formados por ______.", "Células", "La célula es la unidad básica de los seres vivos."),
  ],
  und=[
      ("Un pez, un roble y una persona tienen muchas células. ¿Son unicelulares o pluricelulares?", "Pluricelulares", "Los tres están formados por muchas células."),
      ("¿Cuál es una observación? A) Hay 9 células con forma de rectángulo. B) Estas células están cansadas.", "A", "A se cuenta y se ve; B es una idea sin evidencia."),
      ("¿Por qué una hormiga es pluricelular aunque sea diminuta?", "Porque su cuerpo está formado por muchas células", "El tamaño no decide cuántas células tiene."),
  ],
  app=[
      arith("En una imagen de piel de cebolla (dato de ejemplo) hay 4 filas con 9 células cada una. ¿Cuántas células hay en total?", "4*9", "Se multiplican las filas por las células de cada fila."),
      ("Lista: levadura, ballena, bacteria, abeto, caracol. ¿Cuántos de ellos son unicelulares?", "2", "Solo la levadura y la bacteria tienen una célula; los otros tres son pluricelulares."),
      ("Ordena con letras para investigar una muestra: A) Anoto lo que veo. B) Miro la imagen con cuidado. C) Escribo qué supongo. ¿Cuál es el mejor orden?", "B, A, C", "Primero se mira, luego se anota y al final se interpreta."),
  ],
  rea=[
      ("Ignacio mira una gota de agua de charca y ve una sola célula que se mueve. Dice: «Todos los seres vivos tienen una célula». ¿Es correcta su conclusión? Responde Sí o No y explica.", "No; una muestra no representa a todos los seres vivos", "Las personas, los árboles y los peces tienen muchas células."),
      ("Marta anota: «Se ven 15 células pegadas en capas» y «Esta muestra seguro es de una planta rica en vitaminas». ¿Qué frase no tiene evidencia en la imagen?", "La segunda", "Que sea rica en vitaminas no se puede ver en una imagen de células."),
  ],
  cha=[
      ("Muestra A: 5 seres de una célula cada uno nadan sueltos. Muestra B: un trozo de hoja con 40 células pegadas. ¿Cuál muestra viene de un ser pluricelular?", "La muestra B", "Una hoja es parte de una planta, que tiene muchas células."),
      arith("Un niño contó 5 células en la muestra A y 40 en la muestra B. ¿Cuántas células más contó en la muestra B?", "40-5", "Se resta la cantidad menor a la mayor."),
  ],
  context=[("Dato de ejemplo. Una escuela miró 3 imágenes de microscopio. En la primera contaron 14 células, en la segunda 22 y en la tercera 9. ¿Cuántas células contaron en total?", "45", "14 + 22 + 9 = 45.")],
  selfcheck=[("¿Qué es una célula?", "La unidad más pequeña de un ser vivo", "Todos los seres vivos están formados por células."), ("¿Qué diferencia hay entre unicelular y pluricelular?", "Unicelular tiene una célula y pluricelular tiene muchas", "Se distinguen por el número de células."), ("¿Una interpretación es evidencia? Responde Sí o No.", "No", "Es una suposición, no algo que se vea o se mida.")],
  open_task=task("Con una persona de tu casa, haz una tabla de dos columnas: «unicelular» y «pluricelular». Escribe en ella estos seres: levadura, gato, bacteria, lechuga, mosca, árbol. Después escribe una observación y una interpretación sobre esta descripción: «En una imagen se ven 16 células pegadas, todas con forma de caja».", "Unicelular: levadura y bacteria. Pluricelular: gato, lechuga, mosca y árbol. Observación: hay 16 células con forma de caja. Interpretación: es parte de una planta.", ["clasifica los seis seres", "una observación que se cuente o se vea", "una interpretación marcada como suposición"], ["tabla de dos columnas", "dos frases rotuladas"], ["clasificar por tamaño", "poner un sentimiento como observación"], "Pregunta cómo supo que un ser tenía una sola célula y qué frase sería distinta si otra persona mirara la misma imagen."),
  reinforce="Escribe cinco seres vivos que conozcas y marca cuáles son pluricelulares.",
  extend="Explica con tus palabras por qué una muestra de piel de cebolla no sirve para afirmar que todas las células son iguales.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. Opcional: una hoja de papel para dibujar tres formas de células.",
  use="Aprenderé a hacer preguntas y predicciones sobre las células. Sirve para pensar qué se puede comprobar observando imágenes y datos.",
  prior=["Sé que los seres vivos están formados por células.", "Sé que una predicción lleva una razón."],
  explain=[
      "Las células no son todas iguales. Tienen formas y tamaños distintos según el trabajo que hacen. Una célula muscular es larga y puede acortarse para mover el cuerpo. Un glóbulo rojo de la sangre es pequeño y redondeado, y transporta oxígeno. Una célula nerviosa tiene ramas largas y lleva mensajes por el cuerpo.",
      "Una pregunta comprobable se responde observando o contando, por ejemplo: «¿Cuántas células de forma alargada hay en esta muestra de músculo?». Una pregunta como «¿Qué célula es más bonita?» no se puede comprobar. Una predicción es lo que crees que verás y siempre lleva un porque.",
      "Para comprobar una predicción comparas lo que predijiste con lo que realmente se observa. Si no coinciden, corriges tu idea y no el dato. Así la ciencia aprende. Recuerda que una muestra pequeña no basta para afirmar algo sobre todas las células de un ser vivo.",
  ],
  vocab=[("función", "trabajo que hace una parte de un ser vivo"), ("célula muscular", "célula larga que se acorta y mueve el cuerpo"), ("glóbulo rojo", "célula de la sangre que transporta oxígeno"), ("célula nerviosa", "célula con ramas que lleva mensajes"), ("predicción", "lo que creo que verá y por qué")],
  worked=[
      ("Elegir la pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Qué célula es más linda? B) ¿Cuántas células alargadas hay en una imagen de músculo con 30 células?", ["Pregunto si se puede contar o medir.", "En B se cuentan las células alargadas.", "En A cada persona opina distinto."], "B"),
      ("Predicción con razón", "Una célula muscular debe acortarse para mover el brazo. ¿Qué forma predices que tendrá: larga o redonda?", ["Recuerdo que su trabajo es acortarse.", "Una forma larga se acorta con claridad.", "Escribo la predicción con su razón."], "Larga, porque necesita acortarse para mover el cuerpo"),
  ],
  mistakes=[
      ("Predecir «las células serán todas iguales» sin mirar.", "Las células cambian de forma según su función.", "Predice usando la función de cada célula."),
      ("Afirmar algo de todas las células a partir de una sola imagen.", "Una muestra pequeña no representa a todas.", "Di que el dato vale solo para esa muestra."),
  ],
  rec=[
      ("¿La predicción se hace antes o después de observar?", "Antes", "Es una idea previa que luego se comprueba."),
      ("Un glóbulo rojo transporta algo por la sangre. ¿Transporta oxígeno o mensajes?", "Oxígeno", "Los mensajes los lleva la célula nerviosa."),
      ("Completa con «forma» o «sabor»: las células tienen distinta ______ según su función.", "Forma", "La forma de la célula se relaciona con su trabajo."),
  ],
  und=[
      ("¿Cuál pregunta se puede comprobar? A) ¿Cuántas células hay en esta imagen? B) ¿Qué célula es más simpática?", "A", "Las células de una imagen se pueden contar."),
      ("¿Qué célula lleva mensajes por el cuerpo?", "La célula nerviosa", "Tiene ramas largas que conducen mensajes."),
      ("¿Por qué una buena predicción debe incluir un porque?", "Porque muestra la razón y se puede comprobar", "Sin razón no se aprende del resultado."),
  ],
  app=[
      arith("En una imagen de músculo (dato de ejemplo) hay 30 células, y 24 tienen forma alargada. ¿Cuántas no son alargadas?", "30-24", "Se resta las alargadas del total."),
      ("Predice la forma de una célula que debe llevar mensajes a distancia: ¿con ramas largas o redonda y sin ramas? Responde con una de las dos opciones.", "Con ramas largas", "Las ramas largas permiten llevar mensajes lejos."),
      arith("Una niña contó 6 células nerviosas en cada una de 3 imágenes (dato de ejemplo). ¿Cuántas contó en total?", "6*3", "Se multiplican las células por las imágenes."),
  ],
  rea=[
      ("Teo predice: «Las células de la piel de cebolla serán más largas que una célula muscular, porque son más grandes». ¿Qué falta para poder comprobarlo? Responde con una frase.", "Medir ambas células con la misma regla o escala", "Sin medir con el mismo criterio no se compara el tamaño."),
      ("Sofía mira 1 imagen con 10 células redondas y dice: «Todas las células del cuerpo son redondas». ¿Su conclusión es válida? Responde Sí o No y explica.", "No; una imagen no representa todas las células", "Hay células alargadas y con ramas en otras partes del cuerpo."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre una imagen de 20 células, indicando qué cuentas.", "¿Cuántas de las 20 células tienen forma alargada?", "Nombra lo que se cuenta y se puede responder con la imagen."),
      ("Una predicción dice: «En una imagen de sangre habrá más glóbulos rojos que células de otro tipo, porque los glóbulos rojos son muy numerosos». ¿Cómo la comprobarías en la imagen?", "Contando cada tipo de célula en la imagen y comparando", "Los números contados permiten aceptar o corregir la predicción."),
  ],
  context=[("Dato de ejemplo. En una imagen de sangre de una clase hay 45 glóbulos rojos y 5 de otro tipo. Teo predijo que los rojos serían la mayoría. ¿Cuántos glóbulos rojos más hay que de otro tipo?", "40", "45 − 5 = 40, así que la predicción se cumple.")],
  selfcheck=[("¿Por qué las células tienen distintas formas?", "Porque cada una hace un trabajo distinto", "La forma se relaciona con la función."), ("¿Qué lleva una buena predicción?", "Lo que pasará y la razón", "Así puede comprobarse."), ("¿Una imagen sirve para afirmar algo de todas las células? Responde Sí o No.", "No", "Una muestra pequeña no representa a todas.")],
  open_task=task("Dibuja tres células: una larga como las musculares, una redonda como un glóbulo rojo y una con ramas como una nerviosa. Escribe junto a cada una su función. Después escribe una pregunta comprobable y una predicción con su razón sobre cuál célula tiene más ramas.", "Dibujos: muscular larga (acorta), glóbulo redondo (lleva oxígeno), nerviosa con ramas (lleva mensajes). Pregunta: ¿cuántas ramas tiene cada dibujo? Predicción: la nerviosa tendrá más ramas porque lleva mensajes a distancia.", ["tres dibujos con su función", "una pregunta comprobable", "una predicción con razón"], ["dibujo rotulado", "frases escritas"], ["predecir sin razón", "decir que todas las células son iguales"], "Pregunta por qué dibujó esa forma para cada función y qué cambiaría si una célula tuviera otro trabajo."),
  reinforce="Escribe una pregunta comprobable y otra no comprobable sobre las células y explica la diferencia.",
  extend="Explica por qué una célula muscular larga cumple mejor su función que una redonda.")

L(OA1, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé los niveles de organización de un ser vivo y a hacer un modelo con ellos. Sirve para explicar cómo muchas células forman un cuerpo.",
  prior=["Sé que las células tienen distintas formas.", "Sé qué es un modelo y que todo modelo tiene límites."],
  explain=[
      "En los seres vivos pluricelulares las células se organizan en niveles. Un tejido es un grupo de células parecidas que trabajan juntas, como el tejido muscular. Un órgano reúne varios tejidos y cumple una función, como el corazón. Un sistema es un grupo de órganos que trabajan juntos, como el sistema digestivo. Todo el conjunto forma el organismo.",
      "El orden es siempre el mismo, de lo más pequeño a lo más grande: célula, tejido, órgano, sistema y organismo. Un modelo con una analogía ayuda a recordarlo: las letras (células) forman palabras (tejidos), las palabras forman oraciones (órganos), las oraciones forman párrafos (sistemas) y los párrafos forman un texto (organismo).",
      "Los modelos tienen límites. Las letras no están vivas ni hacen ningún trabajo, pero las células sí: cada una usa alimento y cumple su función. Además, las letras de una palabra pueden ser idénticas, pero las células del cuerpo no. Por eso un buen modelo debe decir qué no muestra.",
  ],
  vocab=[("tejido", "grupo de células parecidas que trabajan juntas"), ("órgano", "parte del cuerpo formada por varios tejidos que cumple una función"), ("sistema", "grupo de órganos que trabajan juntos"), ("organismo", "ser vivo completo"), ("nivel de organización", "escalón que va de la célula al organismo")],
  worked=[
      ("Ordenar los niveles", "Ordena de menor a mayor: sistema, célula, órgano, tejido.", ["Parto de lo más pequeño: la célula.", "Las células forman tejidos y los tejidos forman órganos.", "Los órganos forman sistemas."], "Célula, tejido, órgano, sistema"),
      ("Usar la analogía", "En el modelo del texto, ¿qué nivel corresponde a una palabra si las letras son las células?", ["Las palabras se forman con letras.", "Las células forman tejidos.", "Por tanto la palabra es el nivel siguiente."], "La palabra corresponde al tejido"),
  ],
  mistakes=[
      ("Poner el tejido por encima del órgano.", "Los tejidos forman los órganos, no al revés.", "Recuerda: célula, tejido, órgano, sistema, organismo."),
      ("Pensar que todas las células del cuerpo son idénticas, como ladrillos.", "Hay células de formas y funciones distintas, según el tejido.", "Dilo como límite de tu modelo."),
  ],
  rec=[
      ("¿Qué nivel es mayor: la célula o el tejido?", "El tejido", "Un tejido está formado por muchas células."),
      ("El corazón, ¿es una célula o un órgano?", "Un órgano", "Reúne varios tejidos y cumple una función."),
      ("Completa con «tejidos» o «sistemas»: los órganos juntos forman ______.", "Sistemas", "Un sistema es un grupo de órganos que trabajan juntos."),
  ],
  und=[
      ("¿Qué nivel está justo antes del órgano en la secuencia?", "El tejido", "Los tejidos forman los órganos."),
      ("El estómago, el esófago y el intestino trabajan juntos para digerir. ¿Qué nivel forman juntos?", "Un sistema", "Varios órganos que trabajan juntos son un sistema."),
      ("¿Qué muestra mejor el orden correcto? A) Órgano, célula, tejido. B) Célula, tejido, órgano.", "B", "Se parte de lo pequeño y se llega a lo grande."),
  ],
  app=[
      ("Clasifica «tejido muscular» como célula, tejido u órgano.", "Tejido", "Es un grupo de células parecidas que trabajan juntas."),
      ("Una persona tiene sistemas digestivo, respiratorio y circulatorio. ¿Qué nivel es una persona entera?", "Organismo", "El ser vivo completo es el organismo."),
      arith("Un modelo tiene 5 niveles. Dibujaste 2 niveles. ¿Cuántos niveles te faltan por dibujar?", "5-2", "Se resta lo dibujado al total de niveles."),
  ],
  rea=[
      ("Ana dice: «El pulmón es un tejido porque está hecho de células». ¿Tiene razón? Responde Sí o No y explica.", "No; el pulmón es un órgano porque reúne varios tejidos", "Un tejido es un grupo de células parecidas; el pulmón combina tejidos."),
      ("Un modelo compara las células con ladrillos todos iguales. ¿Cuál es el límite de ese modelo?", "Las células no son todas iguales", "Hay células de formas y funciones distintas."),
  ],
  cha=[
      ("Ordena de menor a mayor: persona, célula muscular, tejido muscular, corazón. Escribe las cuatro palabras en ese orden.", "Célula muscular, tejido muscular, corazón, persona", "La célula forma el tejido, el tejido forma el corazón y la persona es el organismo completo."),
      ("Usa la analogía de las letras: ¿qué nivel corresponde al texto completo?", "El organismo", "El texto es lo más grande, igual que el organismo."),
  ],
  context=[("Dato de ejemplo. Un esquema de un cuaderno muestra 4 sistemas y cada sistema tiene 3 órganos dibujados. ¿Cuántos órganos hay dibujados en total?", "12", "4 × 3 = 12.")],
  selfcheck=[("Nombra los niveles de organización en orden.", "Célula, tejido, órgano, sistema, organismo", "Van de lo más pequeño a lo más grande."), ("¿Qué es un tejido?", "Un grupo de células parecidas que trabajan juntas", "Es el nivel que sigue a la célula."), ("¿Qué límite tiene comparar las células con ladrillos?", "Las células no son todas idénticas", "Hay células de formas y funciones distintas.")],
  open_task=task("Dibuja un esquema con flechas que vaya de la célula al organismo usando este ejemplo: células musculares, tejido muscular, corazón, sistema circulatorio, persona. Escribe junto a cada flecha el verbo «forman». Agrega una frase que diga un límite de tu esquema.", "Células musculares → forman → tejido muscular → forma → corazón → forma → sistema circulatorio → forma → persona. Límite: no muestra los otros tejidos del corazón.", ["cinco niveles en orden", "flechas con verbo", "un límite escrito"], ["esquema rotulado", "frase de límite"], ["invertir los niveles", "no escribir un límite"], "Pregunta por qué ese orden y qué otro tejido podría tener el corazón."),
  reinforce="Escribe otra cadena de niveles con un órgano que conozcas (por ejemplo, el estómago).",
  extend="Inventa una analogía distinta a la de las letras para los cinco niveles y escribe su límite.")

L(OA1, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar seres vivos y niveles con un criterio común. Sirve para ordenar la información y sacar conclusiones justas.",
  prior=["Sé ordenar los niveles de organización.", "Sé que para comparar uso un mismo criterio."],
  explain=[
      "Comparar con un criterio común significa mirar la misma característica en todos los casos. Un criterio posible es el número de células: una bacteria tiene una, mientras que una persona tiene muchísimas. Otro criterio es el nivel de organización: ¿es una célula, un tejido, un órgano o un sistema?",
      "En un ser unicelular, como la levadura, la única célula realiza todas las funciones y también es el organismo completo. No tiene tejidos ni órganos. Los seres pluricelulares sí tienen niveles: sus células forman tejidos, órganos y sistemas.",
      "Una tabla ayuda a comparar. Pones los casos en filas y el criterio en una columna. Antes de concluir revisa si usaste el mismo criterio en todos. Si cambias de criterio a mitad de camino, la comparación no es justa.",
  ],
  vocab=[("criterio", "característica que se mira igual en todos los casos"), ("comparar", "buscar parecidos y diferencias con un criterio común"), ("unicelular", "ser vivo de una sola célula"), ("nivel", "escalón de la organización, de célula a organismo"), ("conclusión", "respuesta final que se apoya en los datos")],
  worked=[
      ("Comparar con un criterio", "Criterio: nivel de organización. Clasifica: neurona, estómago, tejido óseo, sistema nervioso.", ["Una neurona es una célula.", "El estómago reúne tejidos: es un órgano.", "El tejido óseo es un tejido y el sistema nervioso es un sistema."], "Neurona: célula. Estómago: órgano. Tejido óseo: tejido. Sistema nervioso: sistema"),
      ("Comparar por número de células", "Criterio: número de células. Levadura (1 célula), mosca (muchas), bacteria (1 célula). ¿Cuántos tienen una sola célula?", ["Reviso el número de células de cada ser.", "La levadura y la bacteria tienen 1.", "La mosca tiene muchas."], "2"),
  ],
  mistakes=[
      ("Comparar un ser por su tamaño y otro por su número de células.", "No hay criterio común.", "Elige un criterio y úsalo con todos."),
      ("Decir que la levadura tiene tejidos y órganos.", "Una sola célula hace todas las funciones; no hay niveles superiores.", "Recuerda que es unicelular."),
  ],
  rec=[
      ("¿La levadura tiene una célula o muchas?", "Una", "La levadura es un ser unicelular."),
      ("Al comparar, ¿el criterio debe ser el mismo en todos los casos o puede cambiar?", "El mismo", "Si cambia, la comparación no es justa."),
      ("Completa con «órgano» o «célula»: el estómago es un ______.", "Órgano", "Reúne varios tejidos y cumple una función."),
  ],
  und=[
      ("Criterio: nivel de organización. ¿Qué nivel es el hígado?", "Órgano", "Reúne varios tejidos que cumplen una función."),
      ("¿Por qué una levadura no tiene órganos?", "Porque tiene una sola célula que hace todas las funciones", "Los órganos requieren muchas células organizadas."),
      ("¿Qué comparación es justa? A) Contar células de una bacteria y de un pez. B) Contar células de una bacteria y medir el peso de un pez.", "A", "En A se usa el mismo criterio para ambos."),
  ],
  app=[
      arith("Datos de ejemplo. Un trozo de tejido tiene 14 células en una fila y hay 6 filas. ¿Cuántas células tiene el trozo?", "14*6", "Se multiplican las células por fila por el número de filas."),
      ("Criterio: número de células. Ordena de menos a más: persona, bacteria, mosca. Escribe el orden.", "Bacteria, mosca, persona", "La bacteria tiene una célula; la mosca, muchas; la persona, muchísimas más."),
      arith("Un niño comparó 8 seres vivos y 3 eran unicelulares. ¿Cuántos eran pluricelulares?", "8-3", "Se resta los unicelulares al total."),
  ],
  rea=[
      ("Pablo dice: «La bacteria es más importante que la persona porque tiene menos células». ¿Qué problema tiene su comparación?", "Usa un criterio que no mide importancia", "El número de células no dice qué ser es más importante."),
      ("Clara quiere comparar el hígado y el sistema digestivo por nivel de organización. ¿Cuál tiene un nivel mayor?", "El sistema digestivo", "Un sistema agrupa varios órganos, como el hígado."),
  ],
  cha=[
      ("¿Cuántos niveles de organización tiene una levadura: 1, 3 o 5? Escribe el número y explica.", "1; la célula es todo el organismo", "No tiene tejidos, órganos ni sistemas."),
      ("Datos de ejemplo. Muestra A: 25 células. Muestra B: 18 células. Un niño dice que A viene de un ser más grande. ¿Es una conclusión válida? Responde Sí o No y explica.", "No; el número de células de una muestra no dice el tamaño del ser", "Una muestra puede ser un trozo muy pequeño de cualquier ser."),
  ],
  context=[("Dato de ejemplo. Una clase comparó dos tejidos en imágenes: el tejido A tenía 5 filas de 8 células y el tejido B tenía 4 filas de 7 células. ¿Cuántas células más tenía el tejido A?", "12", "A tenía 40 y B tenía 28, y 40 − 28 = 12.")],
  selfcheck=[("¿Qué es un criterio común?", "Una característica que se mira igual en todos los casos", "Permite comparar con justicia."), ("¿Qué nivel de organización tiene una levadura?", "Solo el nivel de célula", "Es unicelular y no tiene tejidos ni órganos."), ("¿Para qué sirve una tabla al comparar?", "Para ordenar los casos y el criterio", "Muestra a simple vista las diferencias.")],
  open_task=task("Haz una tabla con dos columnas: «ser vivo» y «número de células». Escribe estos seres: bacteria, mosca, persona, levadura, abeto. Usa solo «una» o «muchas». Debajo escribe una conclusión y una limitación de tu tabla.", "Bacteria: una. Mosca: muchas. Persona: muchas. Levadura: una. Abeto: muchas. Conclusión: 2 de 5 son unicelulares. Limitación: no dice cuántas células exactas tiene cada ser.", ["los cinco seres clasificados", "un solo criterio", "conclusión y limitación"], ["tabla completa", "frases de conclusión y limitación"], ["cambiar de criterio", "decir que el tamaño decide"], "Pregunta qué cambiaría en su tabla si usara el criterio «tiene órganos»."),
  reinforce="Haz una tabla de tres seres vivos con el criterio «una célula o muchas».",
  extend="Escribe un criterio distinto al número de células para comparar una levadura y una persona.")

# ---------------------------------------------------------------- OA 02
L(OA2, 1,
  materials="Este cuaderno y lápiz. Opcional: un vaso con agua para observar cómo se siente al tragar.",
  use="Aprenderé el recorrido del alimento por el sistema digestivo y a separar lo que se observa de lo que se supone. Sirve para entender qué hace cada órgano.",
  prior=["Sé que los órganos forman sistemas.", "Sé que una observación es lo que se ve o se siente."],
  explain=[
      "El sistema digestivo transforma los alimentos en partes tan pequeñas que el cuerpo puede usarlas. El alimento recorre un largo tubo. Entra por la boca, baja por el esófago y llega al estómago. Luego pasa por el intestino delgado, el intestino grueso y el recto, y sale por el ano. El hígado no forma parte de ese tubo, pero ayuda desde un lado.",
      "El sistema digestivo hace tres trabajos. La digestión rompe los alimentos en partes pequeñas. La absorción pasa los nutrientes a la sangre. La eliminación saca los desechos que el cuerpo no usa. Un nutriente es una sustancia de los alimentos que el cuerpo aprovecha.",
      "Puedes observar tu propio cuerpo: al tragar un sorbo de agua sientes que baja por la garganta. Eso es una observación. Decir «el agua ya llegó al estómago en un segundo» es una interpretación, porque no la mediste ni la viste. Al explicar, usa solo lo que observaste.",
  ],
  vocab=[("digestión", "proceso que rompe los alimentos en partes pequeñas"), ("absorción", "paso de los nutrientes del intestino a la sangre"), ("eliminación", "salida de los desechos del cuerpo"), ("nutriente", "sustancia de los alimentos que el cuerpo aprovecha"), ("esófago", "tubo que lleva el alimento de la boca al estómago")],
  worked=[
      ("Ordenar el recorrido", "Ordena el viaje de un trozo de pan: estómago, boca, intestino delgado, esófago.", ["El pan entra por la boca.", "Baja por el esófago al estómago.", "Después pasa al intestino delgado."], "Boca, esófago, estómago, intestino delgado"),
      ("Observación o interpretación", "«Al tragar siento que el agua baja por mi garganta» y «El agua llegó al estómago en un segundo». ¿Cuál frase es observación?", ["Pregunto si la persona lo sintió o lo midió.", "Sintió bajar el agua por la garganta.", "El segundo no se midió: es suposición."], "La primera frase"),
  ],
  mistakes=[
      ("Pensar que el hígado es un tramo por donde pasa el alimento.", "El alimento no pasa por el hígado; este produce bilis y ayuda a la digestión.", "Dibuja el hígado al lado del tubo, con una flecha de ayuda."),
      ("Decir que absorber es lo mismo que eliminar desechos.", "Absorber es pasar nutrientes a la sangre; eliminar es sacar lo que sobra.", "Pregunta si algo entra a la sangre o sale del cuerpo."),
  ],
  rec=[
      ("¿Por dónde entra el alimento al sistema digestivo?", "Por la boca", "La boca es el primer órgano del recorrido."),
      ("¿Qué órgano está justo después del esófago?", "El estómago", "El esófago lleva el alimento al estómago."),
      ("Completa con «absorción» o «eliminación»: pasar los nutrientes a la sangre se llama ______.", "Absorción", "Absorber es pasar nutrientes a la sangre."),
  ],
  und=[
      ("¿Cuál de estos órganos no está en el recorrido del alimento: estómago, hígado o esófago?", "El hígado", "Está al lado del tubo y ayuda con la bilis."),
      ("¿Qué trabajo hace la digestión?", "Romper los alimentos en partes pequeñas", "Así el cuerpo puede aprovecharlos."),
      ("Marca la observación: A) Sentí que el agua bajaba por la garganta. B) El agua vive feliz en mi cuerpo.", "A", "Lo sentido es evidencia; B es una idea inventada."),
  ],
  app=[
      ("Ordena con letras el recorrido: A) intestino grueso, B) estómago, C) boca, D) esófago. Escribe el orden que sigue el alimento.", "C, D, B, A", "Boca, esófago, estómago e intestino grueso."),
      arith("Un tubo digestivo se dibuja con 8 estructuras en una tabla. Ya rotulaste 5. ¿Cuántas te faltan por rotular?", "8-5", "Se resta lo rotulado al total."),
      ("Un trozo de galleta pasa de la boca al estómago. ¿Por qué órgano pasa en el medio?", "Por el esófago", "El esófago une la boca con el estómago."),
  ],
  rea=[
      ("Dani dice: «El hígado es parte del tubo digestivo porque el alimento pasa por él». ¿Tiene razón? Responde Sí o No y explica.", "No; el alimento no pasa por el hígado, que ayuda desde un lado", "El hígado produce bilis, pero no es un tramo del recorrido."),
      ("Lea anota: «Mi estómago hizo ruido a las 11:00» y «Mi estómago tenía rabia». ¿Cuál es evidencia?", "La primera", "El ruido y la hora se pueden registrar; la rabia es una idea."),
  ],
  cha=[
      ("Explica con el orden del recorrido por qué un trozo de pan llega al intestino delgado después del estómago y no antes.", "Porque el estómago está antes en el recorrido", "El recorrido va de la boca al estómago y luego al intestino delgado."),
      ("Un niño dice que la digestión termina en la boca. Con lo que sabes, ¿qué trabajo ocurre después de la boca?", "La digestión sigue en el estómago y el intestino delgado y luego viene la absorción", "La boca inicia, pero otros órganos continúan."),
  ],
  context=[("Dato de ejemplo. Un esquema del cuaderno muestra el recorrido de 3 comidas y en cada comida se rotulan 7 estructuras del tubo. ¿Cuántos rótulos hay en total?", "21", "3 × 7 = 21.")],
  selfcheck=[("Nombra los tres trabajos del sistema digestivo.", "Digestión, absorción y eliminación", "Son las tres funciones que se estudian."), ("¿Qué hace el esófago?", "Lleva el alimento de la boca al estómago", "Es el tubo que une esos órganos."), ("¿Una suposición es evidencia? Responde Sí o No.", "No", "Solo las observaciones sirven como evidencia.")],
  open_task=task("Dibuja el sistema digestivo como un tubo largo y rotula, en orden, boca, esófago, estómago, intestino delgado, intestino grueso, recto y ano. Dibuja el hígado a un lado con una flecha. Escribe una observación de tu cuerpo al tragar y una interpretación.", "Rótulos en orden y el hígado al lado. Observación: al tragar agua sentí que bajaba por la garganta. Interpretación: el agua llegó rápido al estómago.", ["siete rótulos en orden", "hígado fuera del tubo", "observación e interpretación diferenciadas"], ["dibujo rotulado", "dos frases"], ["poner el hígado en el recorrido", "anotar una suposición como observación"], "Pregunta por qué el hígado no está en el recorrido y cuál de sus frases se puede comprobar."),
  reinforce="Escribe el recorrido de una manzana desde la boca hasta el ano.",
  extend="Explica con tus palabras la diferencia entre digestión y absorción.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Opcional (con una persona adulta): dos terrones de azúcar, un vaso de plástico con agua tibia (no caliente) y reloj.",
  use="Aprenderé a hacer preguntas y predicciones sobre la digestión. Sirve para entender por qué masticar bien ayuda al cuerpo.",
  prior=["Sé el recorrido del alimento.", "Sé que una predicción lleva una razón."],
  explain=[
      "La digestión tiene dos partes que trabajan juntas. La digestión mecánica rompe el alimento en trozos más pequeños: los dientes lo trituran en la boca y los músculos del estómago lo mezclan. La digestión química usa sustancias, como la saliva, los jugos del estómago y la bilis del hígado, que ayudan a romper el alimento aún más.",
      "Una pregunta comprobable sería: «¿Un terrón de azúcar entero se disuelve más lento que uno molido?». Predicción: se disuelve más lento el entero, porque tiene menos superficie en contacto con el agua. Para comprobarlo, el agua, el tiempo y la cantidad de azúcar deben ser iguales; solo cambia si está entero o molido.",
      "Este experimento sirve como analogía: masticar parte el alimento en trozos pequeños y deja más superficie para los jugos digestivos. Pero es un modelo simple; en el cuerpo también actúan los jugos y los músculos. Siempre se hace con un adulto, con agua tibia y sin tragar el contenido.",
  ],
  vocab=[("digestión mecánica", "rompe y mezcla el alimento sin cambiar lo que es"), ("digestión química", "usa sustancias como saliva o jugo gástrico para romper el alimento"), ("saliva", "líquido de la boca que humedece y ayuda a digerir"), ("bilis", "líquido que produce el hígado y ayuda a digerir las grasas"), ("variable", "lo que cambia en una prueba")],
  worked=[
      ("Predicción con razón", "¿Se disolverá más rápido un terrón entero o uno molido en la misma agua tibia? Predice con razón.", ["El molido tiene muchos trozos pequeños.", "Hay más superficie en contacto con el agua.", "Escribo qué pasará y por qué."], "El molido, porque tiene más superficie en contacto con el agua"),
      ("Identificar la variable", "En la prueba, un vaso tiene azúcar entero y otro azúcar molido; el agua tibia y el tiempo son iguales. ¿Qué variable cambia?", ["Comparo los dos vasos.", "Lo único distinto es el azúcar.", "El resto se mantiene igual."], "Si el azúcar está entero o molido"),
  ],
  mistakes=[
      ("Cambiar a la vez la temperatura del agua y el tamaño del azúcar.", "No sabrás cuál causó la diferencia.", "Cambia solo una variable."),
      ("Creer que masticar es digestión química.", "Masticar parte el alimento en trozos: es mecánica.", "La química usa sustancias como la saliva."),
  ],
  rec=[
      ("¿Triturar el alimento con los dientes es digestión mecánica o química?", "Mecánica", "Los dientes rompen el alimento sin usar sustancias."),
      ("¿La saliva participa en la digestión química o en la mecánica?", "En la química", "La saliva es una sustancia que ayuda a digerir."),
      ("Completa con «antes» o «después»: la predicción se escribe ______ de hacer la prueba.", "Antes", "Es una idea previa que luego se comprueba."),
  ],
  und=[
      ("¿Qué produce el hígado que ayuda a digerir las grasas?", "La bilis", "La bilis es el líquido del hígado para las grasas."),
      ("¿Por qué conviene que el agua sea igual en los dos vasos?", "Para saber que la diferencia viene del azúcar", "Si cambia el agua, no se sabe qué causó el resultado."),
      ("¿Qué pregunta se puede comprobar? A) ¿Cuántos minutos demora en disolverse un terrón molido en agua tibia? B) ¿Qué comida es más rica?", "A", "El tiempo se puede medir."),
  ],
  app=[
      arith("Dato de ejemplo. El terrón entero demoró 8 minutos y el molido 3 minutos. ¿Cuántos minutos menos demoró el molido?", "8-3", "Se resta el tiempo menor al mayor."),
      ("Predice: si masticas muy poco una galleta, ¿tus jugos digestivos tendrán más o menos superficie para actuar? Escribe «más» o «menos».", "Menos", "Trozos grandes tienen menos superficie expuesta."),
      arith("Una niña repitió la prueba 3 veces y el molido demoró 3 minutos cada vez. ¿Cuántos minutos sumó en total?", "3*3", "Se multiplican los minutos por las repeticiones."),
  ],
  rea=[
      ("Joaquín puso el terrón entero en agua tibia y el molido en agua fría. El molido demoró más. Dice: «Moler no ayuda». ¿Puede asegurarlo? Responde Sí o No y explica.", "No; cambiaron el tamaño y la temperatura a la vez", "Con dos cambios no se sabe cuál causó el resultado."),
      ("Rita predice: «Si pico la manzana en trozos chicos, mis jugos digestivos actuarán más rápido». ¿Es una predicción con razón? Responde Sí o No y explica.", "Sí; la razón es que los trozos chicos tienen más superficie", "Dice qué pasará y por qué."),
  ],
  cha=[
      ("Escribe una pregunta comprobable que use el terrón de azúcar y el agua tibia, indicando qué medirás.", "¿Cuántos minutos demora en disolverse un terrón entero comparado con uno molido?", "Nombra lo que cambia y lo que se mide."),
      ("Un límite del experimento del azúcar es que el estómago real también mezcla y usa jugos. Escribe otro límite del modelo.", "El azúcar no tiene jugos digestivos ni músculos como el estómago", "Un modelo siempre deja cosas del cuerpo fuera."),
  ],
  context=[("Dato de ejemplo. En una clase 5 grupos midieron el tiempo del terrón molido: 3, 2, 3, 4 y 3 minutos. ¿Cuántos minutos suman en total?", "15", "3 + 2 + 3 + 4 + 3 = 15.")],
  selfcheck=[("¿Qué diferencia hay entre digestión mecánica y química?", "La mecánica rompe en trozos y la química usa sustancias", "Ambas ocurren juntas en el cuerpo."), ("¿Qué hace la bilis?", "Ayuda a digerir las grasas", "La produce el hígado."), ("¿Por qué se cambia solo una variable?", "Para saber cuál causó el resultado", "Con dos cambios no se puede concluir.")],
  open_task=task("Con una persona adulta, usa dos terrones iguales: deja uno entero y rompe el otro en polvo dentro de una bolsa cerrada. Ponlos en dos vasos de plástico con la misma cantidad de agua tibia (no caliente) y mide el tiempo hasta que no se vean trozos. No tragues el contenido. Anota tu predicción antes y los tiempos después.", "Predicción: el molido se disolverá antes porque tiene más superficie. Resultado de ejemplo: molido 3 min y entero 8 min. Conclusión: la predicción se cumplió; limitación: solo es una prueba.", ["predicción con razón", "una sola variable que cambia", "tiempos anotados y conclusión"], ["tabla con dos tiempos", "frase de conclusión"], ["usar agua caliente", "cambiar dos variables"], "Pregunta qué mantuvo igual, qué cambió y qué relación tiene con masticar."),
  reinforce="Escribe una predicción con razón sobre qué pasa si masticas un trozo de pan solo dos veces.",
  extend="Explica por qué masticar bien también ayuda a la digestión química.")

L(OA2, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional (con una persona adulta): una bolsa plástica con pan y agua.",
  use="Aprenderé a usar un modelo del sistema digestivo y a decir qué no muestra. Sirve para explicar qué hace cada órgano.",
  prior=["Sé el recorrido del alimento.", "Sé que todo modelo tiene límites."],
  explain=[
      "Un modelo del estómago puede ser una bolsa plástica con trozos de pan y un poco de agua. Si la aprietas con las manos, el pan se deshace en una papilla. Las manos representan los músculos del estómago, el agua representa los jugos y la bolsa representa la pared del estómago. Así se entiende que el estómago mezcla y ablanda el alimento.",
      "Otro modelo es un colador que representa el intestino delgado: el líquido pasa por los huecos y lo sólido queda. En el cuerpo, los nutrientes pasan por las paredes del intestino delgado a la sangre. Esto es la absorción. El intestino delgado es mucho más largo que el grueso, pero se llama delgado porque es más angosto.",
      "En el intestino grueso se absorbe sobre todo agua y se forman los desechos sólidos. El recto los guarda y el ano los expulsa. Todo modelo tiene límites: la bolsa no tiene jugos reales y el colador no manda nutrientes a la sangre. Un buen modelo siempre dice qué deja fuera.",
  ],
  vocab=[("papilla", "mezcla blanda de alimento y jugos"), ("pared del estómago", "capa de músculos que aprieta y mezcla el alimento"), ("intestino delgado", "tubo largo y angosto donde se absorben los nutrientes"), ("intestino grueso", "tubo más ancho que absorbe agua y forma los desechos sólidos"), ("modelo", "representación simple de algo real")],
  worked=[
      ("Leer el modelo de la bolsa", "En el modelo, las manos aprietan una bolsa con pan y agua. ¿Qué representan las manos?", ["Las manos aprietan la bolsa.", "En el estómago aprietan los músculos de su pared.", "Relaciono lo que hace cada parte."], "Los músculos del estómago"),
      ("Encontrar un límite", "El modelo del colador deja pasar líquido pero no lo manda a la sangre. ¿Es un límite?", ["En el cuerpo los nutrientes pasan a la sangre.", "En el colador solo caen a un vaso.", "Eso es algo real que el modelo no muestra."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Pensar que el intestino delgado es más corto que el grueso.", "Es mucho más largo; se llama delgado por lo angosto.", "Piensa en el ancho y no en el largo."),
      ("Creer que el modelo de la bolsa es igual al estómago real.", "Un modelo siempre simplifica.", "Escribe al menos un límite."),
  ],
  rec=[
      ("En el modelo de la bolsa, ¿qué representa el agua?", "Los jugos del estómago", "El agua se mezcla con el pan como los jugos."),
      ("¿Dónde se absorben principalmente los nutrientes?", "En el intestino delgado", "Sus paredes dejan pasar los nutrientes a la sangre."),
      ("Completa con «grueso» o «delgado»: en el intestino ______ se absorbe sobre todo agua.", "Grueso", "El intestino grueso absorbe agua y forma desechos."),
  ],
  und=[
      ("¿Qué muestra mejor la absorción? A) Un colador que deja pasar líquido. B) Una bolsa que se aprieta.", "A", "El colador muestra el paso de lo líquido por una pared."),
      ("¿Por qué se llama delgado al intestino delgado?", "Porque es angosto", "No se llama así por su largo."),
      ("¿Qué órgano guarda los desechos antes de expulsarlos?", "El recto", "El ano los expulsa después."),
  ],
  app=[
      arith("Un modelo de papel tiene 8 estructuras. Pegaste 6. ¿Cuántas te faltan?", "8-6", "Se resta lo pegado al total."),
      ("En el modelo, apretar la bolsa ablanda el pan. ¿Qué parte de la digestión muestra: mecánica o química?", "Mecánica", "Apretar rompe y mezcla sin sustancias reales."),
      ("En el modelo del colador, lo sólido queda atrapado y no pasa. ¿Qué representa ese sólido en el cuerpo: los nutrientes absorbidos o los restos que no se absorben?", "Los restos que no se absorben", "Lo que no pasa a la sangre sigue hacia el intestino grueso y se elimina."),
  ],
  rea=[
      ("Ema dice que la bolsa con pan y agua es un modelo perfecto del estómago. ¿Tiene razón? Responde Sí o No y explica.", "No; no tiene jugos reales ni pared muscular", "Todo modelo deja cosas fuera."),
      ("En el modelo del colador, el líquido pasa y lo sólido queda. ¿Qué parte del cuerpo representa el líquido que pasa?", "Los nutrientes absorbidos", "En el cuerpo pasan a la sangre."),
  ],
  cha=[
      ("Escribe dos límites del modelo de la bolsa y el agua.", "No tiene jugos reales y no tiene músculos verdaderos", "El agua no digiere y las manos no son la pared del estómago."),
      ("Predice con el modelo: si la bolsa se aprieta más fuerte, ¿el pan se deshará más rápido o más lento? Explica.", "Más rápido, porque se rompe en trozos más pequeños", "Más fuerza produce más trituración."),
  ],
  context=[("Dato de ejemplo. Una clase pegó rótulos del sistema digestivo: 4 grupos pegaron 8 rótulos cada uno. ¿Cuántos rótulos pegaron en total?", "32", "4 × 8 = 32.")],
  selfcheck=[("¿Qué representan las manos en el modelo de la bolsa?", "Los músculos del estómago", "Aprietan y mezclan."), ("¿Qué muestra el colador?", "El paso de nutrientes por una pared", "Es un modelo de la absorción."), ("¿Para qué se escribe un límite?", "Para decir qué no muestra el modelo", "Un modelo no es igual a la realidad.")],
  open_task=task("Dibuja un esquema del sistema digestivo con flechas de verbo: «la boca tritura», «el esófago lleva», «el estómago mezcla». Agrega tres órganos más con su verbo. Escribe dos límites de tu esquema.", "Boca tritura; esófago lleva; estómago mezcla; intestino delgado absorbe; intestino grueso absorbe agua; ano expulsa. Límites: no muestra el hígado y no muestra el largo real del intestino.", ["seis órganos con verbo", "flechas en el orden del recorrido", "dos límites"], ["esquema con flechas", "frases de límite"], ["flechas sin verbo", "no escribir límites"], "Pregunta qué órgano falta en su esquema y por qué es importante."),
  reinforce="Explica con tus palabras qué es la absorción usando un colador como ejemplo.",
  extend="Crea tu propio modelo del intestino grueso con objetos de la casa y escribe su límite.")

L(OA2, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar las estructuras del sistema digestivo según su función principal. Sirve para saber qué hace cada órgano.",
  prior=["Sé las tres funciones del sistema digestivo.", "Sé usar un criterio común para comparar."],
  explain=[
      "Para comparar los órganos digestivos usamos un criterio: su función principal. En la boca se tritura el alimento y la saliva comienza la digestión. El esófago lleva el alimento al estómago. El estómago lo mezcla con jugos ácidos. El hígado produce bilis, que ayuda a digerir grasas.",
      "El intestino delgado termina la digestión y es el lugar de la absorción de nutrientes. El intestino grueso absorbe agua y forma los desechos. El recto los guarda hasta que se expulsan y el ano los deja salir. Cada órgano tiene una función principal, aunque también ayude en otras.",
      "Una tabla de dos columnas ordena la comparación: en una pones el órgano y en la otra su función principal. Para clasificarlos, pregunta: ¿ayuda a digerir, a absorber, a eliminar desechos o a trasladar el alimento? Si dos órganos comparten función, pueden ir juntos.",
  ],
  vocab=[("función principal", "trabajo más importante de un órgano"), ("jugo gástrico", "líquido ácido del estómago que ayuda a digerir"), ("desechos", "restos que el cuerpo no usa"), ("recto", "último tramo del intestino grueso que guarda los desechos"), ("ano", "abertura por donde salen los desechos sólidos")],
  worked=[
      ("Clasificar por función", "Clasifica con el criterio «función principal»: intestino delgado, ano, estómago.", ["Intestino delgado: absorbe nutrientes.", "Ano: deja salir desechos.", "Estómago: mezcla y digiere."], "Intestino delgado: absorción. Ano: eliminación. Estómago: digestión"),
      ("Comparar dos órganos", "Compara el esófago y el intestino delgado con el criterio «absorbe nutrientes».", ["El esófago solo lleva el alimento.", "El intestino delgado absorbe.", "Comparo la respuesta de cada uno."], "El intestino delgado absorbe nutrientes; el esófago no"),
  ],
  mistakes=[
      ("Decir que el intestino grueso absorbe nutrientes como el delgado.", "Absorbe sobre todo agua; los nutrientes se absorben en el delgado.", "Une cada intestino a su función principal."),
      ("Clasificar al ano como parte de la digestión.", "Su función es dejar salir los desechos.", "Pregunta si el órgano elimina."),
  ],
  rec=[
      ("¿El ano participa en la absorción o en la eliminación?", "En la eliminación", "Es la salida de los desechos sólidos."),
      ("¿Qué órgano produce la bilis?", "El hígado", "La bilis ayuda a digerir las grasas."),
      ("Completa con «mezcla» o «absorbe»: el estómago ______ el alimento con jugos.", "Mezcla", "Mezcla y ablanda el alimento."),
  ],
  und=[
      ("¿Qué función principal tiene el intestino delgado?", "Absorber nutrientes", "Sus paredes pasan los nutrientes a la sangre."),
      ("¿Qué órgano guarda los desechos antes de eliminarlos?", "El recto", "Los guarda hasta que salen por el ano."),
      ("¿Qué comparación usa un criterio común? A) Función principal de cada órgano. B) Función de un órgano y color de otro.", "A", "En A se usa el mismo criterio para todos."),
  ],
  app=[
      ("Clasifica el estómago como digestión, absorción o eliminación según su función principal.", "Digestión", "Mezcla el alimento con jugos para romperlo."),
      ("Clasifica el recto como digestión, absorción o eliminación según su función principal.", "Eliminación", "Guarda los desechos sólidos hasta que salen del cuerpo."),
      arith("De 8 estructuras, 3 se relacionan sobre todo con la eliminación. ¿Cuántas no?", "8-3", "Se resta las de eliminación al total."),
  ],
  rea=[
      ("Víctor dice que el esófago absorbe nutrientes porque está en el sistema digestivo. ¿Tiene razón? Responde Sí o No y explica.", "No; el esófago solo lleva el alimento al estómago", "La absorción ocurre en el intestino delgado."),
      ("Una tabla muestra en una columna la función y en otra el color de cada órgano. ¿Sirve para comparar funciones? Responde Sí o No y explica.", "No; el color no es el criterio de función", "Para comparar funciones hay que usar la función en todos."),
  ],
  cha=[
      ("Ordena los órganos según el viaje de los desechos: ano, intestino grueso, recto. Escribe el orden.", "Intestino grueso, recto, ano", "Los desechos se forman, se guardan y salen."),
      ("Un niño dice: «El hígado digiere las grasas». Corrige la frase con lo aprendido.", "El hígado produce bilis, que ayuda a digerir las grasas", "El hígado no recibe el alimento; solo aporta la bilis."),
  ],
  context=[("Dato de ejemplo. Un grupo hizo una tabla con 8 órganos y escribió 2 frases sobre cada órgano. ¿Cuántas frases escribieron en total?", "16", "8 × 2 = 16.")],
  selfcheck=[("¿Cuál es la función principal del intestino grueso?", "Absorber agua y formar los desechos", "Prepara la eliminación."), ("¿Qué órgano ayuda con la bilis?", "El hígado", "Produce la bilis."), ("¿Qué criterio usaste para comparar los órganos?", "Su función principal", "Se mira la misma característica en todos.")],
  open_task=task("Haz una tabla de dos columnas con los ocho órganos: boca, esófago, estómago, hígado, intestino delgado, intestino grueso, recto y ano. Escribe la función principal de cada uno en una frase corta. Después marca cuáles participan en la absorción y cuáles en la eliminación.", "Boca: tritura. Esófago: lleva el alimento. Estómago: mezcla con jugos. Hígado: produce bilis. Delgado: absorbe nutrientes. Grueso: absorbe agua y forma desechos. Recto: guarda desechos. Ano: expulsa desechos. Absorción: delgado (nutrientes) y grueso (agua). Eliminación: recto y ano.", ["ocho órganos con función", "marca la absorción y la eliminación", "usa un solo criterio"], ["tabla completa", "marcas en la tabla"], ["poner el hígado en el recorrido", "confundir absorción con eliminación"], "Pregunta qué órgano tiene la función más fácil de recordar y cuál se confunde más."),
  reinforce="Escribe cuatro órganos y su función principal sin mirar tu tabla.",
  extend="Explica por qué el intestino delgado es el principal lugar de absorción de nutrientes.")

L(OA2, 5,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a explicar la digestión con evidencia y a reconocer los límites de mis explicaciones. Sirve para entender qué ocurre con un alimento en el cuerpo.",
  prior=["Sé las funciones de los órganos digestivos.", "Sé que un modelo tiene límites."],
  explain=[
      "Una buena explicación cuenta qué pasa, en qué orden y por qué. Por ejemplo, un trozo de pan se tritura en la boca, baja por el esófago, se mezcla en el estómago y sigue al intestino delgado, donde los nutrientes pasan a la sangre. Lo que no se absorbe llega al intestino grueso, que absorbe agua y forma los desechos.",
      "La evidencia puede venir del recorrido del alimento, de modelos como la bolsa y el colador o de un experimento como el del terrón. Cada evidencia apoya una parte de la explicación. Si falta evidencia, hay que decirlo: no puedes afirmar algo que no observaste ni mediste.",
      "También hay límites: los modelos simplifican, una prueba pequeña no vale para todos y los nombres de los órganos no muestran todo lo que ocurre dentro. Una explicación honesta dice qué sabemos, con qué evidencia y qué no sabemos todavía.",
  ],
  vocab=[("explicación", "relato que dice qué pasa, en qué orden y por qué"), ("evidencia", "observación o dato que apoya una explicación"), ("límite", "algo que la evidencia o el modelo no puede mostrar"), ("nutriente", "sustancia de los alimentos que el cuerpo aprovecha"), ("desecho", "resto que el cuerpo elimina")],
  worked=[
      ("Completar una explicación", "Completa: «Los nutrientes pasan a la sangre en el ______ porque sus paredes los absorben».", ["Busco el órgano de la absorción.", "Es el intestino delgado.", "Verifico que la razón coincide."], "Intestino delgado"),
      ("Evidencia y límite", "Un niño usa un colador como modelo del intestino. ¿Qué evidencia da y qué límite tiene?", ["El colador deja pasar el líquido y retiene lo sólido.", "En el cuerpo pasan los nutrientes a la sangre.", "El colador no envía nada a la sangre."], "Evidencia: muestra el paso por una pared. Límite: no lleva nada a la sangre"),
  ],
  mistakes=[
      ("Explicar sin decir el orden de los órganos.", "Sin orden no se entiende el recorrido.", "Usa palabras como primero, luego y después."),
      ("Afirmar algo que no tiene evidencia.", "Una explicación debe apoyarse en datos u observaciones.", "Di «según el modelo» o «según los datos»."),
  ],
  rec=[
      ("¿Dónde pasan los nutrientes a la sangre?", "En el intestino delgado", "Es el lugar principal de la absorción."),
      ("¿Qué órgano forma los desechos sólidos?", "El intestino grueso", "Absorbe agua y forma los desechos."),
      ("Completa con «evidencia» o «gusto»: una explicación se apoya en ______.", "Evidencia", "Los datos sostienen la explicación."),
  ],
  und=[
      ("¿Qué pasa con lo que no se absorbe en el intestino delgado?", "Pasa al intestino grueso y luego se elimina", "Los restos siguen su camino hacia la eliminación."),
      ("¿Por qué conviene decir los límites de un modelo?", "Porque no es igual al cuerpo real", "Así evitas creer cosas que no mostró."),
      ("¿Qué evidencia apoya que masticar ayuda a digerir? A) El terrón molido se disolvió antes. B) A mi abuela no le gusta el pan.", "A", "A es un dato medido; B es opinión."),
  ],
  app=[
      ("Ordena los pasos de un trozo de pan: A) se absorben los nutrientes, B) se tritura en la boca, C) se mezcla en el estómago. Escribe el orden.", "B, C, A", "Primero se tritura, luego se mezcla y después se absorben."),
      arith("Una niña dibujó 4 flechas por cada comida y repitió el dibujo para 3 comidas. ¿Cuántas flechas dibujó?", "4*3", "Se multiplican las flechas por las comidas."),
      ("Un modelo muestra el pan pasando por una bolsa y un colador, pero no muestra el hígado. Escribe qué parte de la explicación quedaría incompleta.", "La ayuda de la bilis para digerir las grasas", "El hígado produce la bilis y el modelo no la muestra."),
  ],
  rea=[
      ("Nico explica: «El pan se convierte en sangre en el estómago». ¿Qué corrección harías? Responde con una frase.", "Los nutrientes del pan pasan a la sangre en el intestino delgado", "La absorción no ocurre en el estómago."),
      ("Una niña midió una vez que el terrón molido se disolvió en 3 minutos. Dice: «Siempre se disuelve en 3 minutos». ¿Es correcto? Responde Sí o No y explica.", "No; una medición no vale para todos los casos", "Con otras condiciones el tiempo puede cambiar."),
  ],
  cha=[
      ("Escribe una explicación de tres frases sobre qué pasa con una manzana desde la boca hasta el intestino delgado.", "La boca tritura la manzana; el esófago la lleva al estómago, que la mezcla con jugos; en el intestino delgado los nutrientes pasan a la sangre", "Sigue el orden del recorrido y nombra las funciones."),
      ("Dos explicaciones: A) «El hígado recibe el alimento y lo absorbe». B) «El hígado produce bilis que ayuda a digerir grasas». ¿Cuál es correcta?", "B", "El alimento no pasa por el hígado."),
  ],
  context=[("Dato de ejemplo. Un grupo ficticio hizo 3 comidas distintas y en cada una el alimento pasó por 7 estructuras del tubo digestivo. ¿Cuántos pasos por estructuras fueron en total?", "21", "3 × 7 = 21.")],
  selfcheck=[("¿Qué debe tener una buena explicación?", "Qué pasa, en qué orden y por qué", "Así se entiende el proceso."), ("¿Qué órgano elimina los desechos sólidos?", "El ano", "Es la salida del tubo digestivo."), ("¿Por qué una sola medición no basta?", "Porque puede variar en otras condiciones", "Una prueba es un solo caso.")],
  open_task=task("Escribe una explicación de cinco frases sobre lo que le pasa a una galleta desde que entra a la boca. Nombra al menos cinco órganos. Después escribe un límite: algo que tu explicación no muestra.", "La boca tritura la galleta y la saliva la humedece. El esófago la lleva al estómago, que la mezcla con jugos. En el intestino delgado los nutrientes pasan a la sangre. El intestino grueso absorbe agua y forma desechos. El ano los expulsa. Límite: no muestra el hígado.", ["cinco órganos en orden", "digestión, absorción y eliminación", "un límite"], ["texto de cinco frases", "frase de límite"], ["saltarse órganos", "poner el hígado en el recorrido"], "Pregunta qué evidencia usó y qué parte de su explicación es solo una suposición."),
  reinforce="Cuéntale a otra persona el recorrido de un alimento sin mirar tu cuaderno.",
  extend="Explica por qué se dice que el intestino grueso y el delgado cumplen funciones distintas.")

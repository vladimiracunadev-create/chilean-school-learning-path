"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 03 (ciclo de vida de las plantas con flor) y OA 04 (importancia y cuidado de las plantas)."""
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


OA3, OA4 = "CN03 OA 03", "CN03 OA 04"

# ---------------------------------------------------------------- OA 03
L(OA3, 1,
  materials="Este cuaderno, lápiz y lápices de colores. En casa, con una persona adulta: un vaso de plástico transparente, algodón húmedo y un poroto o una lenteja.",
  use="Aprenderé cómo una semilla se transforma en una plantita. Sirve para entender el primer paso del ciclo de vida de una planta con flor y registrar cambios en el tiempo.",
  prior=["Sé que una planta necesita agua, aire y una temperatura adecuada.", "Sé que la raíz sale primero cuando germina un poroto."],
  explain=[
      "Una semilla es el comienzo de una nueva planta. En este cuaderno estudiamos las plantas con flor; las coníferas, como la araucaria y los pinos, no tienen flores y guardan sus semillas en conos. Por fuera la semilla tiene una cubierta que la protege. Por dentro guarda una plantita muy pequeña y una reserva de alimento. Mientras está seca, la semilla puede esperar mucho tiempo sin crecer.",
      "La germinación es el momento en que la semilla empieza a crecer. Para germinar necesita agua, aire y una temperatura adecuada. La mayoría de las semillas no necesita luz para germinar. Primero la semilla absorbe agua y se hincha. Luego la cubierta se abre y sale la raíz. Después sale el tallito con las primeras hojas.",
      "Para observar la germinación se anota en una tabla qué se ve cada día. La tabla ordena los cambios en el tiempo. Como las semillas son seres vivos, cada una germina a su ritmo. Por eso no se espera que todas tengan el mismo tamaño el mismo día. Si una semilla no germina, es evidencia que también se anota.",
  ],
  vocab=[("semilla", "parte de la planta con flor que guarda una plantita y alimento"), ("germinación", "momento en que la semilla empieza a crecer"), ("cubierta", "capa externa que protege la semilla"), ("reserva de alimento", "alimento guardado dentro de la semilla"), ("registro en el tiempo", "tabla donde se anota qué cambia cada día")],
  worked=[
      ("Ordenar la germinación", "Escenas: A) sale el tallito con hojas, B) la semilla se hincha con agua, C) sale la raíz. ¿En qué orden pasan?", ["La semilla primero absorbe agua y se hincha.", "Luego sale la raíz.", "Al final sale el tallito con hojas."], "B, C, A"),
      ("Leer un registro", "Registro de un poroto en algodón húmedo, que es un ejemplo: día 1, semilla hinchada; día 3, raíz de 1 cm; día 5, raíz de 3 cm y tallito. ¿Cuántos centímetros creció la raíz entre el día 3 y el día 5?", ["Busco la raíz el día 3: 1 cm.", "Busco la raíz el día 5: 3 cm.", "Resto: 3 − 1 = 2."], "2 cm"),
  ],
  mistakes=[
      ("Decir «la semilla germina solo si tiene mucha luz».", "Se confunde la germinación con el crecimiento de la planta.", "La mayoría de las semillas germina con agua, aire y temperatura adecuada, aunque no tenga luz."),
      ("Decir «la semilla seca ya es una planta grande».", "Se olvida que es una plantita muy pequeña dentro de una cubierta.", "La semilla guarda una plantita muy pequeña que crece al germinar."),
  ],
  rec=[
      ("Cuando una semilla empieza a crecer, ¿se llama germinación o dispersión?", "Germinación", "La germinación es el comienzo del crecimiento de la semilla."),
      ("¿Qué sale primero de una semilla que germina: la raíz o las hojas?", "La raíz", "La raíz sale primero."),
      ("¿La semilla guarda una reserva de alimento? Responde Sí o No.", "Sí", "Ese alimento ayuda a la plantita a crecer al principio."),
  ],
  und=[
      ("Nombra dos cosas que necesita una semilla para germinar.", "Agua, aire o temperatura adecuada (dos de ellas)", "Son las condiciones para germinar."),
      ("¿Para qué sirve la cubierta de la semilla?", "Para proteger a la plantita que está dentro", "La cubierta cuida a la plantita."),
      ("¿Por qué conviene anotar los cambios en una tabla con los días?", "Para ver cómo cambia la semilla en el tiempo", "La tabla permite comparar un día con otro."),
  ],
  app=[
      ("Ordena con letras: A) sale el tallito con hojas, B) la semilla se hincha con agua, C) sale la raíz.", "B, C, A", "Primero se hincha, luego sale la raíz y al final el tallito."),
      arith("Un poroto de ejemplo tenía una raíz de 1 cm el día 3 y una raíz de 4 cm el día 7. ¿Cuántos centímetros creció la raíz entre esos días?", "4-1", "Se resta la medida del día 3 a la del día 7."),
      ("En un vaso hay dos semillas iguales en algodón: una húmedo y otra seco. Pasan tres días. ¿Cuál tiene más probabilidad de germinar: la del algodón húmedo o la del seco?", "La del algodón húmedo", "La semilla necesita agua para germinar."),
  ],
  rea=[
      ("De 5 semillas de lenteja, 4 germinaron y 1 no. Un niño dice: «Mi prueba no sirve». ¿Tiene razón? Responde Sí o No y explica.", "No; una semilla sin germinar también es evidencia", "Los datos anotados sirven aunque no todas germinen."),
      ("Una semilla puesta en un cajón seco por una semana no cambió. Otra en algodón húmedo ya tiene raíz. ¿Qué necesidad de la germinación muestran?", "El agua", "La única diferencia es la humedad."),
  ],
  cha=[
      ("Un niño dice: «Mi poroto germina en un cajón oscuro, así que la luz no es necesaria para germinar». ¿Su afirmación es correcta para la mayoría de las semillas?", "Sí", "La mayoría de las semillas no necesita luz para germinar."),
      ("Escribe una predicción para esta pregunta: ¿germina una semilla en el refrigerador (muy frío)?", "Por ejemplo: germinará muy poco o nada porque está muy frío", "Una temperatura muy baja frena la germinación."),
  ],
  context=[("Julia pone 6 lentejas en algodón húmedo. El día 4 han germinado 4. ¿Cuántas aún no han germinado?", "2", "Se resta lo germinado al total. Cálculo: 6 − 4 = 2.")],
  selfcheck=[("¿Qué guarda una semilla por dentro?", "Una plantita pequeña y una reserva de alimento", "Es lo que permite que crezca."), ("¿Cuál es el primer paso de la germinación: se hincha con agua o sale la hoja?", "Se hincha con agua", "La semilla primero absorbe agua."), ("¿Las semillas germinan todas igual y el mismo día? Responde Sí o No.", "No", "Cada semilla germina a su ritmo.")],
  open_task=task("Con una persona adulta, pon un poroto o una lenteja en algodón húmedo dentro de un vaso transparente, en un lugar tibio. Durante siete días, dibuja y anota cada día qué ves y mide la raíz en centímetros. Marca el día en que ves la raíz y el día en que sale el tallito. Si no tienes semillas, ordena y completa este registro de ejemplo: día 1 hinchada, día 3 raíz de 1 cm, día 5 raíz de 3 cm y tallito.", "Día 1: hinchada. Día 3: raíz de 1 cm. Día 5: raíz de 3 cm y tallito. Día 7: raíz de 4 cm y 2 hojitas. La raíz salió primero.", ["registra varios días con medidas", "nombra el orden de aparición", "dibuja los cambios"], ["tabla de siete días con dibujos", "frase con el orden de la germinación"], ["no anotar el día de cada cambio", "decir que la hoja sale antes que la raíz"], "Pide que explique qué necesidades de la semilla tuvo en el vaso y qué cambiaría si faltara el agua."),
  reinforce="Dibuja la germinación en tres pasos: semilla hinchada, raíz y tallito con hojas.",
  extend="Escribe una pregunta que se pueda probar sobre la germinación, por ejemplo con otra temperatura o con otra cantidad de agua.")

L(OA3, 2,
  materials="Este cuaderno, lápiz y lápices de colores. Si puedes, una flor de un jardín o macetero para mirar sin arrancar (si tienes alergia al polen, míralo de lejos).",
  use="Aprenderé cómo crece una planta con flor y cómo es una flor por dentro. Sirve para entender de dónde salen el fruto y las semillas.",
  prior=["Sé que la semilla germina.", "Sé que las hojas fabrican alimento con luz, agua y aire."],
  explain=[
      "Después de germinar, la plantita crece. El tallo se alarga, salen hojas nuevas y la raíz se hace más larga. Crecer significa aumentar de tamaño. Para crecer, la planta necesita agua, luz, aire y suelo. Con el tiempo, la planta se hace adulta.",
      "Cuando la planta adulta está lista, forma botones florales. Un botón floral es una flor cerrada y pequeña, que luego se abre. Una flor suele tener pétalos de colores, que atraen a los insectos. Dentro de la flor están los estambres, que son como hilitos que producen un polvo fino llamado polen. En el centro está el pistilo, que recibe el polen.",
      "La base del pistilo, con el tiempo, se transforma en fruto. Por eso, sin flor no hay fruto. No todas las plantas florecen a la misma edad ni en la misma estación. Muchas plantas florecen en primavera. Si una flor se arranca, esa planta ya no podrá formar el fruto de esa flor.",
  ],
  vocab=[("crecimiento", "aumento de tamaño de una planta"), ("botón floral", "flor cerrada y pequeña que luego se abre"), ("pétalo", "parte de color de la flor que atrae insectos"), ("estambre", "parte de la flor que produce el polen"), ("pistilo", "parte de la flor que recibe el polen y forma el fruto")],
  worked=[
      ("Nombrar las partes de una flor", "En una flor hay unas hojitas de color, unos hilos con un polvo amarillo y una parte central. ¿Cómo se llaman?", ["Las hojitas de color son los pétalos.", "Los hilos con polvo amarillo son los estambres y el polvo es el polen.", "La parte central que recibe el polen es el pistilo."], "Pétalos, estambres y pistilo"),
      ("Seguir el crecimiento", "Una planta de ejemplo midió 4 cm el día 1, 9 cm el día 15 y 18 cm el día 30. ¿Cuántos centímetros creció entre el día 15 y el 30?", ["Busco la medida del día 15: 9 cm.", "Busco la medida del día 30: 18 cm.", "Resto: 18 − 9 = 9."], "9 cm"),
  ],
  mistakes=[
      ("Decir «el fruto sale de la raíz».", "Se confunde la parte donde se forma el fruto.", "El fruto se forma desde la flor, en el pistilo."),
      ("Decir «los pétalos fabrican el polen».", "Se confunden las partes de la flor.", "Los estambres producen el polen; los pétalos atraen a los insectos."),
  ],
  rec=[
      ("¿Qué parte de la flor tiene colores y atrae a los insectos: el pétalo o el estambre?", "El pétalo", "Los colores de los pétalos llaman la atención."),
      ("¿Qué produce el polen: el estambre o el pistilo?", "El estambre", "El polen se forma en los estambres."),
      ("Una flor cerrada y pequeña que luego se abre se llama botón ______. Completa con floral o verde.", "Floral", "El botón floral es una flor cerrada."),
  ],
  und=[
      ("¿Qué significa «crecer» en una planta?", "Aumentar de tamaño", "La planta se hace más grande."),
      ("¿Para qué sirve el pistilo de una flor?", "Para recibir el polen y formar el fruto", "En su base se forma el fruto."),
      ("¿Por qué no se debe arrancar una flor de una planta que queremos que dé frutos?", "Porque el fruto se forma a partir de la flor", "Sin flor no hay fruto."),
  ],
  app=[
      arith("Una planta de ejemplo midió 7 cm el día 10 y 19 cm el día 40. ¿Cuántos centímetros creció?", "19-7", "Se resta la medida inicial a la final."),
      ("Ordena con letras: A) flor abierta, B) botón floral, C) planta joven con hojas.", "C, B, A", "Primero crece la planta joven, luego aparece el botón y después la flor abierta."),
      ("Rotula: la parte con polvo amarillo en una flor, ¿es estambre o pistilo?", "Estambre", "El polvo amarillo es polen y sale del estambre."),
  ],
  rea=[
      ("Mario dice que una flor con pétalos de colores intensos atrae más insectos que una sin color. ¿Qué parte de la flor usa para decirlo?", "Los pétalos", "Los pétalos llaman la atención de los insectos."),
      ("Un jardinero arranca todas las flores de un manzano en primavera. ¿Qué le pasará a la producción de manzanas ese año?", "No habrá manzanas o habrá muy pocas", "Los frutos se forman desde las flores."),
  ],
  cha=[
      ("Dos plantas iguales crecen con el mismo riego. La A recibe sol y la B recibe poca luz. La A florece y la B no. ¿Qué variable pudo influir?", "La luz", "La luz es lo único que cambió."),
      ("Dibuja con palabras una flor: escribe en una línea sus tres partes (pétalos, estambres y pistilo) y qué hace cada una.", "Pétalos atraen insectos, estambres producen polen, pistilo recibe el polen", "Describe las tres partes y sus tareas."),
  ],
  context=[("Un niño mide una planta de arveja cada diez días: 5 cm, 12 cm y 23 cm. ¿Cuántos centímetros creció entre la primera y la última medida?", "18", "Se resta la medida inicial a la final. Cálculo: 23 − 5 = 18.")],
  selfcheck=[("¿Qué es un botón floral?", "Una flor cerrada y pequeña que luego se abre", "Es la flor antes de abrirse."), ("¿Qué parte de la flor forma el fruto?", "El pistilo", "En su base se forma el fruto."), ("¿Crece una planta solo con agua? Responde Sí o No.", "No", "También necesita luz, aire y suelo.")],
  open_task=task("Dibuja una flor grande y rotula pétalos, estambres y pistilo. Debajo escribe una frase para cada parte con lo que hace. Con una persona adulta, mira de lejos una flor de un jardín o un macetero y compara tu dibujo con la flor real. No la arranques. Si no tienes una, usa esta descripción: una flor con cinco pétalos rosados, hilos con polvo amarillo y una parte central larga.", "Pétalos: rosados, atraen insectos. Estambres: producen polen amarillo. Pistilo: recibe el polen y forma el fruto.", ["rotula las tres partes", "escribe qué hace cada parte", "dibuja con detalle"], ["dibujo rotulado", "tres frases"], ["confundir estambre con pistilo", "no explicar la tarea de cada parte"], "Pide que explique de qué parte se forma el fruto y qué pasaría si faltara el pistilo."),
  reinforce="Dibuja una planta creciendo en tres momentos: plantita, planta con botón floral y planta con flor abierta.",
  extend="Elige una planta que conozcas con flor y escribe en qué estación suele florecer, preguntándole a una persona adulta.")

L(OA3, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Si puedes, una flor de un jardín que puedas mirar de lejos, sin arrancarla.",
  use="Aprenderé la diferencia entre polinización y dispersión. Sirve para no confundir cómo se forma un fruto con cómo viajan las semillas.",
  prior=["Sé las partes de la flor.", "Sé que el fruto se forma desde la flor."],
  explain=[
      "La polinización ocurre cuando el polen llega al pistilo de una flor. El polen sale del estambre, y suele viajar de una flor a otra. Lo transportan los insectos, como las abejas, o las aves, como el picaflor. También lo puede llevar el viento. Gracias a la polinización se forman el fruto y las semillas.",
      "La dispersión de las semillas ocurre más tarde, cuando las semillas ya están formadas. Es el viaje de las semillas lejos de la planta madre. El viento se lleva semillas livianas, como las del diente de león. Los animales comen frutos y las semillas salen después en sus excrementos. Algunas semillas se pegan al pelo de un animal. Otras flotan en el agua.",
      "Polinización y dispersión son dos pasos distintos. La polinización mueve el polen, antes del fruto. La dispersión mueve las semillas, después del fruto. Ambas son importantes. Sin polinización no hay semillas. Sin dispersión las semillas caen todas junto a la planta madre y tienen poco espacio y poca luz para crecer.",
  ],
  vocab=[("polinización", "viaje del polen hasta el pistilo de una flor"), ("polen", "polvo fino que se produce en los estambres"), ("dispersión", "viaje de las semillas lejos de la planta madre"), ("insecto polinizador", "insecto que lleva polen de una flor a otra"), ("planta madre", "planta que produjo las semillas")],
  worked=[
      ("Decidir si es polinización", "Una abeja visita una flor, se le pega polen en el cuerpo y luego visita otra flor. ¿Es polinización o dispersión?", ["La abeja lleva polen.", "El polen va de una flor a otra.", "Eso es polinización."], "Es polinización"),
      ("Decidir si es dispersión", "Una semilla de diente de león, liviana, sale volando con el viento y cae lejos de la planta. ¿Es polinización o dispersión?", ["Lo que viaja es una semilla.", "Se aleja de la planta madre.", "Eso es dispersión."], "Es dispersión"),
  ],
  mistakes=[
      ("Decir «la abeja dispersa las semillas cuando va de flor en flor».", "Se confunde el viaje del polen con el viaje de las semillas.", "La abeja que lleva polen hace polinización."),
      ("Decir «la dispersión pasa antes de que se forme el fruto».", "Se cambia el orden de los pasos.", "Primero hay polinización y fruto; después dispersión de las semillas."),
  ],
  rec=[
      ("Cuando el polen llega al pistilo, ¿se llama polinización o germinación?", "Polinización", "La polinización es la llegada del polen al pistilo."),
      ("¿Qué viaja en la dispersión: el polen o las semillas?", "Las semillas", "La dispersión mueve las semillas."),
      ("Nombra un animal que puede llevar polen de una flor a otra.", "Abeja, picaflor u otro insecto o ave", "Los insectos y las aves polinizan."),
  ],
  und=[
      ("¿Qué se forma gracias a la polinización?", "El fruto y las semillas", "Sin polinización no hay semillas."),
      ("¿Para qué sirve que las semillas se dispersen lejos de la planta madre?", "Para que tengan más espacio y luz para crecer", "Cerca de la planta madre compiten por espacio y luz."),
      ("Explica la diferencia entre polinización y dispersión con una frase.", "La polinización mueve polen y la dispersión mueve semillas", "Son dos viajes distintos."),
  ],
  app=[
      ("Casos: A) una abeja lleva polen a otra flor, B) el viento se lleva una semilla, C) un picaflor lleva polen en su pico. Escribe las letras de los casos de polinización.", "A y C", "En A y C viaja el polen."),
      ("Una semilla con ganchitos se pega al pelo de un perro y cae en otro lugar. ¿Es polinización o dispersión?", "Dispersión", "Lo que viaja es una semilla."),
      arith("En un jardín hay 8 flores. Las abejas visitaron 5. ¿Cuántas flores no fueron visitadas?", "8-5", "Se resta a las 8 flores las 5 visitadas."),
  ],
  rea=[
      ("Una persona cubre una flor con una malla fina que no deja entrar insectos. ¿Qué paso del ciclo se impide: polinización o dispersión?", "La polinización", "Sin insectos, el polen no llega a otras flores."),
      ("Las semillas de un diente de león flotan con el viento. Las de un coco flotan en el mar. ¿Qué tienen en común estos dos viajes?", "Son formas de dispersión", "En ambos viajan semillas lejos de la planta madre."),
  ],
  cha=[
      ("Un huerto tiene pocas abejas y los zapallos dan pocos frutos. ¿Cuál paso del ciclo puede estar fallando?", "La polinización", "Sin abejas hay menos transporte de polen."),
      ("Una niña dice que un animal que come cerezas y deja las semillas lejos hace dispersión. ¿Tiene razón? Responde Sí o No.", "Sí", "Las semillas viajan lejos de la planta madre."),
  ],
  context=[("En un jardín, 4 abejas visitan la flor A y 3 abejas visitan la flor B. ¿Cuántas visitas de abejas hubo en total a las dos flores?", "7", "Se suman las visitas. Cálculo: 4 + 3 = 7.")],
  selfcheck=[("¿Qué transportan las abejas de una flor a otra?", "Polen", "Es el polvo de los estambres."), ("¿La dispersión es el viaje del polen o el viaje de las semillas?", "El viaje de las semillas", "Las semillas se alejan de la planta madre."), ("Nombra un modo de dispersión de las semillas.", "Viento, animales o agua (uno de ellos)", "Son modos de dispersión.")],
  open_task=task("Completa una tabla con dos columnas, «polinización» y «dispersión». Escribe en la columna correcta estos casos: una abeja con polen, una semilla que flota en el agua, un picaflor con polen, una semilla pegada en el pelo de un perro, una semilla liviana que vuela con el viento. Después dibuja un caso de cada columna.", "Polinización: abeja con polen, picaflor con polen. Dispersión: semilla en agua, semilla en el pelo del perro, semilla con el viento.", ["clasifica los cinco casos", "dibuja un caso de cada tipo", "escribe qué viaja en cada columna"], ["tabla de dos columnas", "dos dibujos"], ["confundir polen con semilla", "poner un caso en ambas columnas"], "Revisa que la columna de polinización solo tenga viajes de polen y pregunta qué viaja en cada caso."),
  reinforce="Dibuja una abeja llevando polen y una semilla con alas volando, y rotula cuál es polinización y cuál es dispersión.",
  extend="Escribe un ejemplo de un animal que ayuda a la dispersión y uno que ayuda a la polinización, y explica la diferencia.")

L(OA3, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Si quieres, una fruta de tu casa, como un tomate o una manzana, para mirarla por dentro con una persona adulta.",
  use="Aprenderé qué es un fruto, para qué sirve y cómo se repite el ciclo de vida. Sirve para entender que de una semilla sale una planta que da otras semillas.",
  prior=["Sé que el fruto se forma desde la flor.", "Sé que la dispersión lleva las semillas lejos."],
  explain=[
      "El fruto es la parte de la planta que se forma desde la flor, después de la polinización. Protege a las semillas y ayuda a que viajen. La manzana, el tomate, el zapallo y la vaina de la arveja son frutos, porque tienen semillas dentro, aunque a algunos los llamemos verduras.",
      "Si una semilla cae en un lugar con agua, aire y una temperatura adecuada, germina y forma una planta nueva. Esa planta crece, florece, se poliniza y forma frutos con más semillas. Así el ciclo de vida de la planta con flor se repite una y otra vez: semilla, germinación, crecimiento, flor, polinización, fruto y dispersión.",
      "No todas las semillas llegan a ser una planta. Muchas caen en lugares sin agua o sin luz, o las come un animal. Por eso una planta produce muchas semillas. Es normal que solo algunas germinen. Una persona puede ayudar guardando semillas secas y sembrándolas en un macetero con tierra.",
      "Recuerda que no todas las plantas tienen flor. La araucaria es una conífera: no tiene flores con pétalos ni frutos como la manzana. Sus semillas, los piñones, están dentro de un cono. Su ciclo también empieza en una semilla, pero se distingue del ciclo de las plantas con flor que viste aquí.",
  ],
  vocab=[("fruto", "parte de la planta que se forma desde la flor y guarda las semillas"), ("ciclo de vida", "serie de etapas por las que pasa un ser vivo, que se repite"), ("etapa", "paso dentro de una serie de cambios"), ("vaina", "fruto alargado que guarda semillas, como el de la arveja"), ("sembrar", "poner semillas en la tierra para que crezcan")],
  worked=[
      ("Reconocer un fruto", "Un tomate se forma desde una flor y guarda semillas. ¿Es un fruto?", ["Un fruto se forma desde la flor.", "Un fruto guarda semillas.", "El tomate cumple las dos cosas."], "Sí, el tomate es un fruto"),
      ("Ordenar el ciclo", "Etapas: A) fruto con semillas, B) flor, C) germinación, D) planta adulta. ¿En qué orden suceden?", ["Primero germina la semilla.", "Luego crece la planta adulta y forma la flor.", "Después de la flor se forma el fruto con semillas."], "C, D, B, A"),
  ],
  mistakes=[
      ("Decir «el ciclo termina cuando se forma el fruto».", "Se olvida que las semillas pueden germinar y empezar otra vez.", "Las semillas del fruto, si germinan, empiezan un nuevo ciclo."),
      ("Decir «el tomate no es un fruto porque se come en ensalada».", "Se confunde cómo se cocina con lo que es.", "Es un fruto porque se forma desde la flor y guarda semillas."),
  ],
  rec=[
      ("¿Un fruto guarda semillas? Responde Sí o No.", "Sí", "Una función del fruto es proteger las semillas."),
      ("La parte de la planta que se forma desde la flor y guarda semillas es el ______. Completa con fruto o tallo.", "Fruto", "Esa es la definición de fruto."),
      ("¿Un ciclo de vida se repite o ocurre una sola vez?", "Se repite", "De cada planta salen semillas que pueden formar otra."),
  ],
  und=[
      ("Nombra dos frutos que conozcas.", "Manzana, tomate, zapallo u otro fruto con semillas (dos de ellos)", "Tienen semillas y se forman desde la flor."),
      ("¿Por qué una planta produce muchas semillas?", "Porque no todas llegan a germinar", "Muchas caen en lugares sin agua o sin luz."),
      ("¿Qué etapa viene justo después de la polinización?", "La formación del fruto", "Después de la polinización se forman el fruto y las semillas."),
  ],
  app=[
      ("Ordena con letras: A) flor, B) germinación, C) fruto, D) crecimiento.", "B, D, A, C", "Germinación, crecimiento, flor y fruto."),
      arith("Una vaina de arveja tiene 6 semillas. Una planta tiene 4 vainas. ¿Cuántas semillas hay en total?", "6*4", "Se multiplican las semillas de cada vaina por la cantidad de vainas."),
      ("La araucaria guarda sus semillas, los piñones, en un cono y no tiene flores con pétalos. ¿Es una planta con flor? Responde Sí o No.", "No", "Es una conífera: sus semillas están en conos."),
  ],
  rea=[
      ("Un niño siembra 10 semillas y germinan 7. Dice: «Fracasó mi siembra». ¿Qué le respondes?", "Que no, porque germinó la mayoría y es normal que algunas no germinen", "Siete de diez es un buen resultado."),
      ("Una manzana se pudre en el suelo y sus semillas quedan en la tierra húmeda. ¿Qué etapa del ciclo puede comenzar?", "La germinación", "Las semillas con agua y temperatura adecuada pueden germinar."),
  ],
  cha=[
      ("Un niño dice: «El fruto ayuda a la dispersión porque un animal lo come y lleva las semillas lejos». ¿Está en lo correcto? Responde Sí o No.", "Sí", "Muchos animales comen frutos y dispersan semillas."),
      ("Explica con tus palabras por qué el ciclo de vida de una planta con flor es un ciclo y no una línea.", "Porque las semillas pueden formar nuevas plantas y volver a empezar", "El final de una etapa lleva al comienzo."),
  ],
  context=[("Una niña guardó las semillas de un zapallo. Las sembró en 3 maceteros con 4 semillas cada uno. ¿Cuántas semillas sembró en total?", "12", "Se multiplican maceteros por semillas. Cálculo: 3 × 4 = 12.")],
  selfcheck=[("¿Qué etapa viene después de la flor?", "El fruto", "El fruto se forma desde la flor."), ("¿Qué guarda el fruto?", "Las semillas", "Las semillas están dentro del fruto."), ("¿Una semilla que cae en un lugar sin agua puede germinar? Responde Sí o No.", "No", "Sin agua no germina.")],
  open_task=task("Dibuja el ciclo de vida de una planta con flor en círculo, con flechas. Las siete etapas son: semilla, germinación, crecimiento, flor, polinización, fruto y dispersión. Escribe una frase corta en cada etapa y marca con color dónde se repite el ciclo. Con una persona adulta, mira por dentro un tomate o una manzana y anota cuántas semillas ves (la persona adulta lo corta).", "Semilla, germinación, crecimiento, flor, polinización, fruto, dispersión y de nuevo semilla. En el tomate conté 30 semillas.", ["incluye las siete etapas", "usa flechas en círculo", "escribe una frase por etapa"], ["dibujo del ciclo en círculo", "conteo de semillas"], ["ponerlo como línea sin volver a empezar", "mezclar polinización con dispersión"], "Revisa el orden y pregunta qué etapa lleva de nuevo a la semilla."),
  reinforce="Dibuja un fruto abierto con sus semillas y rotula fruto y semillas.",
  extend="Explica por qué una planta que produce muchas semillas tiene más posibilidades de que alguna germine.")

# ---------------------------------------------------------------- OA 04
L(OA4, 1,
  materials="Este cuaderno, lápiz y lápices de colores. Si quieres, mira un árbol o una planta de un patio y cuenta qué animales se acercan.",
  use="Aprenderé por qué las plantas son importantes para los seres vivos y el ambiente. Sirve para entender cómo dependemos de ellas y cómo ellas dependen de otros seres.",
  prior=["Sé que las hojas fabrican alimento con luz, agua y aire.", "Sé que los animales necesitan alimento y un lugar para vivir."],
  explain=[
      "Las plantas son importantes para los seres vivos porque son alimento. Los animales herbívoros comen hojas, frutos y semillas. Las personas comemos frutas, verduras, legumbres y cereales. Cuando las hojas fabrican su alimento con luz, agua y aire, liberan oxígeno al aire. Las personas y los animales necesitamos oxígeno para respirar.",
      "Las plantas también son un hábitat, es decir, el lugar donde vive un ser vivo. En un árbol hacen su nido las aves, y bajo sus hojas viven insectos. Algunas plantas dan sombra y refugio del calor. Las raíces mantienen el suelo firme y evitan que el agua y el viento se lo lleven.",
      "Todos estos usos forman una red: las plantas dan alimento, oxígeno y refugio, y los animales ayudan a las plantas con la polinización y la dispersión. Si desaparecen muchas plantas de un lugar, también les cuesta vivir a los animales que dependen de ellas. Por eso es importante cuidarlas.",
  ],
  vocab=[("oxígeno", "gas del aire que los seres vivos necesitan para respirar"), ("hábitat", "lugar donde vive un ser vivo"), ("herbívoro", "animal que se alimenta de plantas"), ("depender", "necesitar algo para poder vivir"), ("refugio", "lugar que protege del calor, del frío o de peligros")],
  worked=[
      ("Identificar una importancia", "Una paloma hace su nido en un plátano oriental. ¿Qué importancia del árbol muestra esto?", ["La paloma vive y cría en el árbol.", "El lugar donde vive un ser vivo es su hábitat.", "El árbol es un hábitat."], "El árbol es hábitat de la paloma"),
      ("Seguir el oxígeno", "Un pasto crece con luz, agua y aire. ¿Qué gas que necesitamos libera al aire?", ["El pasto tiene hojas que fabrican alimento.", "Al hacerlo, libera un gas al aire.", "Ese gas es el oxígeno."], "Libera oxígeno"),
  ],
  mistakes=[
      ("Decir «las plantas solo sirven para comer».", "Se olvidan otros aportes.", "También dan oxígeno, hábitat, sombra y mantienen firme el suelo."),
      ("Decir «los animales no necesitan a las plantas».", "Muchos animales dependen de las plantas.", "Los herbívoros comen plantas y muchos animales viven en ellas."),
  ],
  rec=[
      ("¿Qué gas liberan las plantas al aire que los seres vivos necesitan para respirar: oxígeno o humo?", "Oxígeno", "Las hojas liberan oxígeno."),
      ("El lugar donde vive un ser vivo se llama ______. Completa con hábitat o fruto.", "Hábitat", "Esa es la definición."),
      ("¿Los herbívoros se alimentan de plantas o de otros animales?", "De plantas", "Herbívoro significa que come plantas."),
  ],
  und=[
      ("Nombra dos cosas que las plantas dan a los seres vivos.", "Alimento, oxígeno, hábitat o sombra (dos de ellas)", "Son aportes de las plantas."),
      ("¿Por qué se dice que las plantas y los animales forman una red?", "Porque se ayudan: las plantas dan alimento y refugio y los animales las polinizan o dispersan sus semillas", "Se necesitan entre sí."),
      ("¿Qué ayuda a hacer la raíz de las plantas con el suelo?", "Mantenerlo firme y evitar que se lo lleven el agua o el viento", "Las raíces sujetan el suelo."),
  ],
  app=[
      ("Casos: A) un pájaro hace su nido en un árbol, B) una vaca come pasto, C) un niño respira aire con oxígeno. ¿Qué casos muestran alimento?", "B", "En B el pasto es alimento."),
      arith("En un árbol hay 3 nidos de aves y en otro árbol hay 5 nidos. ¿Cuántos nidos hay en total?", "3+5", "Se suman los nidos de ambos árboles."),
      ("Una persona dice: «En esta plaza hay sombra gracias a los árboles». ¿Qué aporte de las plantas menciona?", "La sombra", "La sombra protege del calor."),
  ],
  rea=[
      ("En un cerro se corta el pasto y los arbustos. Un tiempo después ya no se ven los conejos que vivían ahí. ¿Qué relación entre plantas y animales muestra esto?", "Los conejos dependían de las plantas para comer y vivir", "Sin plantas perdieron alimento y refugio."),
      ("Una niña dice: «Respiramos oxígeno que ya estaba en el aire, así que las plantas no importan». ¿Qué falta en su idea?", "Que las plantas liberan oxígeno al aire", "Las plantas aportan oxígeno al aire."),
  ],
  cha=[
      ("Cuenta cuántos usos de las plantas hay en esta frase: «El pino da sombra, es hábitat de aves y de su madera se hacen muebles».", "3", "Hay sombra, hábitat y madera."),
      ("Escribe una cadena sencilla con flechas que empiece en una planta y termine en una persona, por ejemplo con trigo.", "Trigo → harina → pan → persona", "La persona obtiene alimento del trigo."),
  ],
  context=[("En una plaza hay 4 plátanos orientales y 2 palmeras. Todos dan sombra y en algunos hay nidos. ¿Cuántos árboles dan sombra en total?", "6", "Se suman los árboles. Cálculo: 4 + 2 = 6.")],
  selfcheck=[("¿Qué es un hábitat?", "El lugar donde vive un ser vivo", "Un árbol puede ser hábitat de aves."), ("¿Qué gas liberan las plantas?", "Oxígeno", "Lo necesitamos para respirar."), ("¿Dependen los herbívoros de las plantas? Responde Sí o No.", "Sí", "Se alimentan de ellas.")],
  open_task=task("Dibuja un árbol y rotula con flechas cuatro aportes que da: alimento, oxígeno, hábitat y sombra. Al lado, escribe qué animal o persona recibe cada aporte. Con una persona adulta, mira un árbol de tu barrio durante diez minutos y anota cuántos animales ves cerca. Si no puedes salir, usa este dato: en un ciprés hay 2 aves y 4 insectos.", "Alimento: frutos, para las aves. Oxígeno: lo respiramos. Hábitat: nido de las aves. Sombra: protege del sol. En el árbol vi 3 aves.", ["rotula los cuatro aportes", "escribe quién recibe cada uno", "anota una observación real o el dato dado"], ["dibujo del árbol con flechas", "conteo de animales"], ["olvidar el oxígeno", "inventar datos"], "Revisa que cada aporte tenga quién lo recibe y pregunta qué pasaría si se cortara el árbol."),
  reinforce="Escribe tres frases que empiecen con «Las plantas son importantes porque...».",
  extend="Piensa en un animal que viva en tu barrio y explica de qué planta depende.")

L(OA4, 2,
  materials="Este cuaderno y lápiz. Si quieres, mira en tu casa objetos hechos con plantas, como papel, madera o ropa de algodón.",
  use="Aprenderé para qué usamos las plantas las personas. Sirve para valorar lo que hacen por nosotros y para usarlas con cuidado y con evidencia.",
  prior=["Sé que las plantas son alimento y hábitat.", "Sé que un hábitat es el lugar donde vive un ser vivo."],
  explain=[
      "Las personas usamos las plantas de muchas maneras. Las comemos: frutas, verduras, legumbres y cereales. También son materia prima, que es un material que sirve para fabricar otras cosas. De la madera se hacen muebles y también el papel de los cuadernos, y del algodón se hace tela. Las flores y las plantas de los jardines se usan para ornamentación, es decir, para decorar y embellecer.",
      "Otro uso es el medicinal. Algunas plantas se usan en infusiones, como la manzanilla, para aliviar molestias leves. Pero algo natural no siempre es seguro. Muchas plantas hacen daño si se comen o se toman. Nunca se debe probar una planta sin que una persona adulta de confianza sepa qué es. Si una molestia sigue, hay que consultar a un profesional de la salud.",
      "Los usos de las plantas se deben comprobar con evidencia. Un libro, un profesional o una ficha de un jardín botánico pueden ser fuentes. Un comentario como «dicen que cura todo» no es evidencia. Algunos pueblos originarios guardan saberes sobre plantas; ese saber se pregunta con respeto a la comunidad.",
  ],
  vocab=[("materia prima", "material que sirve para fabricar otras cosas"), ("ornamentación", "uso de algo para decorar"), ("medicinal", "que se usa para aliviar una molestia"), ("infusión", "bebida que se prepara con hojas o flores en agua caliente"), ("evidencia", "dato confiable que apoya una afirmación")],
  worked=[
      ("Clasificar un uso", "El algodón se usa para hacer toallas. ¿Es alimento, materia prima o ornamentación?", ["Las toallas se fabrican con algodón.", "Un material que sirve para fabricar cosas es materia prima.", "El algodón es materia prima."], "Materia prima"),
      ("Pedir evidencia", "Un video dice: «Esta hierba cura todo». ¿Es suficiente para usarla?", ["La frase no cita fuente.", "Una afirmación sin evidencia no basta.", "Antes hay que consultar a un profesional de la salud."], "No, falta evidencia y consultar a una persona adulta o un profesional"),
  ],
  mistakes=[
      ("Decir «si una planta es natural, es segura».", "Algunas plantas naturales hacen daño.", "Una planta se come o se toma solo si una persona adulta de confianza sabe qué es."),
      ("Decir «una planta medicinal sirve para curar cualquier enfermedad».", "Se generaliza sin evidencia.", "Cada planta se usa para molestias concretas y se consulta a un profesional."),
  ],
  rec=[
      ("La madera se usa para fabricar muebles. ¿Es una materia prima o una medicina?", "Materia prima", "La madera es un material para fabricar cosas."),
      ("Las flores de un jardín que decoran una plaza, ¿son ornamentación o alimento?", "Ornamentación", "Se usan para decorar."),
      ("¿Se puede probar una planta desconocida sin avisar a una persona adulta? Responde Sí o No.", "No", "Algunas plantas hacen daño."),
  ],
  und=[
      ("¿Qué es una materia prima?", "Un material que sirve para fabricar otras cosas", "Por ejemplo, la madera."),
      ("¿Por qué «es natural» no quiere decir «es seguro»?", "Porque algunas plantas naturales hacen daño", "Hay plantas dañinas."),
      ("¿Qué fuente sirve para saber si una planta se puede usar como infusión: un video sin fuente o un profesional de la salud?", "Un profesional de la salud", "Es una fuente confiable."),
  ],
  app=[
      ("Usos: A) pan de trigo, B) cuaderno de papel, C) ramo de flores en un jarrón. Escribe la letra de la ornamentación.", "C", "Las flores decoran."),
      arith("Una familia usa 4 cajas de cartón hechas de papel y 3 cuadernos de papel. ¿Cuántos objetos de papel son?", "4+3", "Se suman los objetos."),
      ("«Una taza de infusión de manzanilla ayuda con molestias leves». ¿Qué uso de las plantas muestra: alimento, materia prima o medicinal?", "Medicinal", "Se usa para aliviar una molestia."),
  ],
  rea=[
      ("Una niña quiere probar un fruto rojo de un arbusto del patio que nadie conoce. ¿Qué debe hacer?", "No probarlo y preguntar a una persona adulta que sepa qué es", "Puede hacer daño."),
      ("Juan dice: «Mi vecina dice que esta planta cura todo». ¿Qué evidencia le pedirías?", "Una fuente confiable, como un profesional o una ficha", "Es una afirmación sin fuente."),
  ],
  cha=[
      ("Un cuaderno, una silla de madera y una camisa de algodón. ¿Cuál usa un material que viene de un árbol?", "El cuaderno y la silla", "El papel y la madera vienen de árboles."),
      ("Escribe un ejemplo de uso de una planta en cada categoría: alimento, materia prima y ornamentación.", "Por ejemplo: trigo, madera y rosa", "Cada una pertenece a un uso distinto."),
  ],
  context=[("En una feria hay un puesto de verduras, otro de muebles de madera y otro de flores. Una niña cuenta 6 verduras, 4 muebles y 5 ramos de flores. ¿Cuántos productos de ornamentación y de materia prima ve (muebles más ramos)?", "9", "Se suman muebles y ramos. Cálculo: 4 + 5 = 9.")],
  selfcheck=[("¿Para qué se usan las flores de un jardín?", "Para ornamentación", "Las flores decoran y embellecen el lugar."), ("¿Qué es una infusión?", "Una bebida que se prepara con hojas o flores en agua caliente", "Es un modo de usar una planta."), ("¿Se debe probar cualquier planta desconocida? Responde Sí o No.", "No", "Puede hacer daño.")],
  open_task=task("Haz una tabla con cuatro columnas: alimento, materia prima, ornamentación y medicinal. En cada columna escribe un objeto o producto de tu casa o barrio y la planta de la que viene. Si no sabes el uso medicinal con seguridad, escribe «lo averiguaré con un profesional». No pruebes ninguna planta.", "Alimento: pan, trigo. Materia prima: mesa, madera. Ornamentación: rosas en un jarrón. Medicinal: lo averiguaré con un profesional.", ["completa las cuatro columnas", "escribe la planta de origen", "no afirma usos medicinales sin fuente"], ["tabla de cuatro columnas"], ["afirmar usos medicinales sin fuente", "poner un producto en la columna equivocada"], "Revisa que cada producto esté en su columna y que lo medicinal tenga fuente o quede pendiente."),
  reinforce="Busca en tu casa tres objetos hechos con plantas y escribe de cuál planta viene cada uno.",
  extend="Pregunta a una persona mayor qué infusión usa en tu casa y anota qué fuente confiable podría confirmar su uso.")

L(OA4, 3,
  materials="Este cuaderno y lápiz. Para el experimento, con una persona adulta: dos bandejas o fuentes, tierra, un trozo de pasto con tierra o césped y una jarra con agua.",
  use="Aprenderé qué pasa cuando se pierde la vegetación de un lugar. Sirve para entender por qué es importante no destruir bosques, pastos y arbustos.",
  prior=["Sé que las raíces sujetan el suelo.", "Sé que las plantas son hábitat y dan sombra."],
  explain=[
      "La vegetación es el conjunto de plantas de un lugar. Si se pierde, pasan varias cosas. Primero, el suelo queda desnudo y la lluvia y el viento se lo llevan. Esto se llama erosión. Segundo, desaparece el hábitat de animales y estos tienen que irse. Tercero, hay menos sombra y el lugar se calienta más.",
      "Sin raíces que sujeten la tierra, la lluvia fuerte puede arrastrar barro desde un cerro hacia las casas y los ríos. También el agua entra menos al suelo. Los incendios forestales destruyen la vegetación muy rápido. La mayoría de los incendios forestales los inician las personas, por eso nunca se hace fuego en el campo y siempre se avisa a una persona adulta si hay humo.",
      "Puedes comprobar la erosión con un modelo. Se ponen dos bandejas inclinadas: una con tierra cubierta de pasto y otra con tierra suelta. Con una jarra se echa la misma cantidad de agua en cada una. El agua de la bandeja sin pasto sale mucho más turbia y con más barro. Esa es la evidencia.",
  ],
  vocab=[("vegetación", "conjunto de plantas de un lugar"), ("erosión", "pérdida de suelo arrastrado por la lluvia o el viento"), ("suelo desnudo", "suelo sin plantas que lo cubran"), ("incendio forestal", "fuego que destruye la vegetación de un lugar"), ("modelo", "montaje pequeño que imita lo que pasa en la naturaleza")],
  worked=[
      ("Leer un resultado", "Con una jarra se echó un vaso de agua en cada bandeja. De la bandeja con pasto salió agua casi clara. De la bandeja con tierra suelta, agua muy turbia. ¿Qué bandeja perdió más suelo?", ["La turbiedad indica cuánto barro arrastró el agua.", "La tierra suelta dejó salir agua muy turbia.", "Esa bandeja perdió más suelo."], "La bandeja con tierra suelta"),
      ("Predecir una consecuencia", "Se corta toda la vegetación de un cerro. Llega una lluvia fuerte. ¿Qué es probable que pase?", ["Las raíces ya no sujetan el suelo.", "El agua arrastra la tierra.", "Ocurre erosión y baja barro."], "Habrá erosión y barro bajando del cerro"),
  ],
  mistakes=[
      ("Decir «si se pierden las plantas, el suelo queda igual».", "Se olvida que las raíces sujetan el suelo.", "Sin plantas, el viento y la lluvia se llevan el suelo."),
      ("Decir «los incendios se apagan solos y no dañan a los animales».", "Se subestima el daño del fuego.", "Un incendio destruye hábitat y los animales no siempre pueden escapar."),
  ],
  rec=[
      ("Cuando la lluvia o el viento se llevan el suelo, ¿se llama erosión o germinación?", "Erosión", "Erosión es la pérdida de suelo."),
      ("¿Qué sujeta el suelo: las raíces o las flores?", "Las raíces", "Las raíces sujetan la tierra."),
      ("Si desaparecen los árboles, ¿hay más sombra o menos sombra?", "Menos sombra", "Los árboles dan sombra."),
  ],
  und=[
      ("¿Qué es la vegetación?", "El conjunto de plantas de un lugar", "Incluye árboles, arbustos y pastos."),
      ("Nombra dos consecuencias de perder la vegetación de un cerro.", "Erosión, pérdida de hábitat o menos sombra (dos de ellas)", "Son consecuencias vistas en la clase."),
      ("¿Por qué el agua sale más turbia de la bandeja sin pasto?", "Porque sin raíces el agua arrastra más tierra", "Las raíces del pasto sujetan la tierra."),
  ],
  app=[
      arith("En un modelo, la bandeja sin pasto dejó 5 cucharaditas de barro en el vaso y la bandeja con pasto dejó 1 cucharadita. ¿Cuántas cucharaditas más de barro dejó la bandeja sin pasto?", "5-1", "Se resta el barro de la bandeja con pasto al de la bandeja sin pasto."),
      ("Un niño ve humo en un cerro lejano. ¿Qué debe hacer: avisar a una persona adulta o ir a mirar de cerca?", "Avisar a una persona adulta", "Un incendio es peligroso."),
      ("Una ladera tiene arbustos y otra no. Llueve fuerte. ¿En cuál es más probable que baje barro?", "En la ladera sin arbustos", "Sin raíces el suelo se arrastra más."),
  ],
  rea=[
      ("Dos bandejas reciben un vaso de agua. La A tiene pasto y la B no. El agua de B sale turbia. Un niño dice: «El pasto sujeta la tierra». ¿Qué evidencia usa?", "El agua turbia de B y el agua casi clara de A", "La turbiedad muestra cuánto barro se arrastró."),
      ("Un camping deja basura y pisa el pasto hasta que queda tierra desnuda. ¿Qué puede pasar con la lluvia?", "Puede haber erosión", "Sin pasto, la lluvia arrastra el suelo."),
  ],
  cha=[
      ("En el modelo de erosión, ¿qué se debe dejar igual en las dos bandejas para que la prueba sea justa?", "La inclinación y la cantidad de agua", "Solo debe cambiar la cobertura de la tierra."),
      ("Explica cómo la pérdida de árboles afecta a un pájaro que hacía su nido en ellos.", "Pierde su hábitat y su lugar para criar", "Sin árboles no tiene dónde anidar."),
  ],
  context=[("En una ladera de un cerro se cortaron 12 arbustos de un total de 20. ¿Cuántos arbustos quedan?", "8", "Se resta lo cortado al total. Cálculo: 20 − 12 = 8.")],
  selfcheck=[("¿Qué es la erosión?", "La pérdida de suelo arrastrado por la lluvia o el viento", "Pasa más cuando no hay plantas."), ("¿Se hace fuego en el campo? Responde Sí o No.", "No", "Puede iniciar un incendio forestal."), ("¿Qué pasa con el hábitat de los animales si se pierde la vegetación?", "Se pierde", "Los animales se quedan sin refugio y alimento.")],
  open_task=task("Con una persona adulta, haz el modelo de erosión: dos bandejas inclinadas con un libro debajo; una con tierra cubierta de pasto y otra con tierra suelta. Echa un vaso de agua en cada una desde una jarra, sobre un vaso transparente donde caiga el agua. Compara el color del agua y escribe tu conclusión. Si no puedes hacerlo, usa este resultado: con pasto, agua casi clara; sin pasto, agua muy turbia.", "Con pasto, el agua cayó casi clara. Sin pasto, muy turbia. Conclusión: el pasto sujeta la tierra y evita la erosión.", ["dibuja el montaje", "compara el agua de las dos bandejas", "concluye con evidencia"], ["dibujo del modelo", "conclusión escrita"], ["cambiar la cantidad de agua entre bandejas", "concluir sin mirar la evidencia"], "Revisa que la cantidad de agua y la inclinación sean iguales y que la conclusión cite la turbiedad."),
  reinforce="Dibuja un cerro con árboles y otro sin árboles bajo la lluvia, y muestra con flechas qué pasa con el suelo.",
  extend="Escribe dos medidas que una familia puede aplicar para evitar incendios forestales en vacaciones.")

L(OA4, 4,
  materials="Este cuaderno, lápiz, lápices de colores y una hoja grande o cartulina para un afiche. En tu casa, con una persona adulta: una maceta con una planta o un lugar de la plaza para observar.",
  use="Aprenderé a proponer una medida para cuidar las plantas y a comunicarla con claridad. Sirve para pasar de saber a actuar con una acción que se pueda comprobar.",
  prior=["Sé que perder vegetación trae consecuencias.", "Sé hacer una tabla y una conclusión con evidencia."],
  explain=[
      "Una medida de cuidado es una acción concreta que ayuda a proteger las plantas. Por ejemplo: regar una planta con el agua en que se enjuagaron verduras (sin jabón), no pisar el pasto de una plaza, no arrancar flores ni ramas, plantar un árbol con permiso y con una persona adulta, y no hacer fuego en el campo.",
      "Una medida comprobable es una medida que se puede medir o contar para saber si funcionó. Por ejemplo: «Regaré mi planta tres veces por semana y contaré cuántas hojas nuevas salen en 30 días». «Cuidar las plantas» es una idea muy general y no se puede comprobar. «Contar cuántas plantas siguen vivas después de un mes» sí se puede comprobar.",
      "Para comunicar la medida se hace un afiche: tiene un título claro, una frase que diga qué se debe hacer, una razón con un dato y un dibujo. Se lee en voz alta y se pregunta a otra persona si lo entendió. Si no lo entendió, se mejora el afiche. Al final se comprueba la medida y se registra lo que pasó.",
  ],
  vocab=[("medida de cuidado", "acción concreta que protege algo"), ("comprobable", "que se puede medir o contar para ver si funcionó"), ("afiche", "cartel con un mensaje y un dibujo"), ("razón", "dato que explica por qué se recomienda algo"), ("registro de resultados", "tabla donde se anota lo que pasó")],
  worked=[
      ("Hacer comprobable una medida", "La idea general es: «Cuidar los árboles de mi plaza». ¿Cómo la convierto en una medida comprobable?", ["Pienso en una acción: regar un árbol joven una vez por semana.", "Pienso qué puedo contar: hojas nuevas o ramas verdes.", "Escribo la medida con un plazo."], "Regaré un arbolito una vez por semana durante un mes y contaré sus hojas nuevas"),
      ("Revisar un afiche", "Un afiche dice: «¡Cuida las plantas!». No tiene razón ni dato. ¿Qué le falta?", ["Un título corto sí tiene.", "Falta una acción concreta y una razón con dato.", "Un dibujo también ayuda."], "Le faltan una acción concreta, una razón con dato y un dibujo"),
  ],
  mistakes=[
      ("Proponer «cuidar la naturaleza» como medida.", "Es una idea general que no se puede comprobar.", "Escribe una acción concreta con algo que se pueda contar o medir."),
      ("Hacer un afiche con mucho texto pequeño.", "Nadie lo lee con facilidad.", "Usa un título grande, una frase corta y un dibujo."),
  ],
  rec=[
      ("¿Cuál es una acción concreta: «regar mi planta dos veces por semana» o «cuidar la naturaleza»?", "Regar mi planta dos veces por semana", "Es una acción que se puede hacer y contar."),
      ("Una medida que se puede medir o contar para ver si funcionó es ______. Completa con comprobable o bonita.", "Comprobable", "Se puede comprobar con datos."),
      ("¿Un afiche tiene un dibujo? Responde Sí o No.", "Sí", "El dibujo ayuda a comunicar el mensaje."),
  ],
  und=[
      ("¿Por qué «cuidar las plantas» no es una medida comprobable?", "Porque es muy general y no dice qué hacer ni qué contar", "No se puede medir su resultado."),
      ("Nombra tres partes de un buen afiche.", "Título, frase de acción, razón con dato o dibujo (tres de ellas)", "Son partes del afiche de la clase."),
      ("¿Qué se hace al final para saber si la medida funcionó?", "Se comprueba y se registra lo que pasó", "Se compara con lo que se esperaba."),
  ],
  app=[
      ("Medidas: A) regar un arbolito una vez por semana y contar sus hojas nuevas, B) querer mucho a las plantas. ¿Cuál es comprobable?", "A", "En A se puede contar un resultado."),
      arith("Una niña planta 8 semillas y 6 germinan. ¿Cuántas no germinaron?", "8-6", "Se resta lo que germinó del total."),
      ("Un curso quiere proteger el pasto de la plaza. Elige una medida comprobable: A) pisar menos, B) poner un letrero «No pisar el pasto» y contar cuántas personas pisan el pasto cada día.", "B", "En B se puede contar un resultado."),
  ],
  rea=[
      ("Un afiche dice «¡Plantemos árboles!» sin explicar por qué ni cómo. ¿Qué dos cosas le faltan?", "Una razón con un dato y una acción concreta", "Un afiche debe decir qué hacer y por qué."),
      ("Un niño cuenta cuántas de 8 plantas de un macetero comunitario tienen hojas firmes: antes de ordenar el riego, 3; un mes después, 5. ¿Los datos muestran una mejora?", "Sí, porque hay 2 plantas más con hojas firmes", "Hubo más plantas con hojas firmes, aunque no prueba la causa por sí solo."),
  ],
  cha=[
      ("Escribe una medida comprobable para cuidar un árbol joven de tu cuadra, con una frecuencia y algo que contar.", "Por ejemplo: regarlo una vez por semana y contar sus hojas nuevas por un mes", "Tiene acción, plazo y algo que contar."),
      ("Explica por qué conviene mostrar el afiche a otra persona antes de colgarlo.", "Para saber si lo entiende y poder mejorarlo", "Así se comprueba que el mensaje es claro."),
  ],
  context=[("Un curso de 3.º básico planta 12 plantitas en el patio. Después de un mes siguen vivas 9. ¿Cuántas plantitas no sobrevivieron?", "3", "Se resta lo vivo del total. Cálculo: 12 − 9 = 3.")],
  selfcheck=[("¿Qué es una medida comprobable?", "Una medida que se puede medir o contar para saber si funcionó", "Tiene un resultado observable."), ("Nombra una medida de cuidado de las plantas.", "No pisar el pasto, regar con agua de enjuagar verduras, no arrancar flores u otra", "Son medidas concretas."), ("¿Un afiche debe tener un dibujo? Responde Sí o No.", "Sí", "Ayuda a comunicar el mensaje.")],
  open_task=task("Elige una de estas medidas: A) regar una planta con el agua en que se enjuagaron verduras (sin jabón), B) poner un letrero para no pisar el pasto, C) no arrancar flores en la plaza. Escribe qué contarás o medirás para comprobarla y durante cuánto tiempo. Después haz un afiche con un título, una frase de acción, una razón con dato y un dibujo. Muéstraselo a una persona y anota si lo entendió.", "Elegí A. Contaré cuántas hojas nuevas salen en 30 días. Afiche: «Riega con agua reutilizada», dibujo de una regadera.", ["elige una medida y dice qué contará", "hace un afiche con las cuatro partes", "registra si otra persona lo entendió"], ["afiche", "tabla de resultados"], ["escribir una medida general", "no incluir un dato"], "Revisa que la medida diga qué contar y que el afiche tenga razón con dato."),
  reinforce="Escribe una medida de cuidado para las plantas de tu casa y dibuja un afiche pequeño.",
  extend="Diseña una tabla para registrar durante un mes si una planta mejora con tu medida de cuidado.")

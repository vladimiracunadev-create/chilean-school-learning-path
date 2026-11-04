"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 17 (evidencias, variables y representación de reacciones químicas)."""
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


OA = "CN1M OA 17"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Si quieres comprobar la fermentación, necesitas la ayuda de una persona adulta, levadura de panadería, azúcar, agua tibia (nunca caliente), una botella plástica y un globo. No se hace ninguna combustión en casa.",
  use="Aprenderé a reconocer una reacción química por sus evidencias y a distinguirla de un cambio físico. Sirve para decidir si lo que observas es o no una reacción.",
  prior=["Sé que la materia está formada por átomos y moléculas.", "Sé distinguir una mezcla de una sustancia pura."],
  explain=[
      "Una reacción química es un proceso en que una o más sustancias, llamadas reactantes, se transforman en otras sustancias distintas, llamadas productos. Los átomos se reordenan: se rompen enlaces y se forman otros nuevos. En un cambio físico, en cambio, no se forman sustancias nuevas: fundir hielo, disolver azúcar en agua o hervir agua cambian el estado o la forma, pero la sustancia sigue siendo la misma.",
      "Las evidencias de una reacción química son la producción de un gas (burbujas), la formación de un precipitado (un sólido que aparece en un líquido), el cambio de temperatura, de color, de olor y la emisión de luz. Una sola evidencia puede engañar: hervir agua forma burbujas de vapor y disolver un colorante cambia el color, pero no hay reacción. Se necesitan varias evidencias y que el cambio no se pueda revertir con facilidad.",
      "Hay reacciones en la vida diaria. La fermentación ocurre cuando la levadura transforma el azúcar de una masa y produce gas que la hace crecer. La combustión ocurre en un calefactor o en un motor. La oxidación del hierro forma herrumbre. Una pregunta investigable debe indicar qué se mide, por ejemplo: «¿Cuántos mililitros de gas produce la levadura con azúcar en 10 minutos a 30 °C?».",
  ],
  vocab=[("reacción química", "proceso en que unas sustancias se transforman en otras"), ("reactante", "sustancia que reacciona"), ("producto", "sustancia nueva que se forma en una reacción"), ("precipitado", "sólido que aparece al mezclar líquidos"), ("cambio físico", "cambio en que no se forman sustancias nuevas"), ("evidencia", "observación que permite concluir que ocurrió una reacción")],
  worked=[
      ("Cambio físico o reacción", "Clasifica: (1) el hielo se derrite, (2) un clavo de hierro se vuelve anaranjado y quebradizo.", ["En (1) el agua sigue siendo agua.", "En (2) aparece una sustancia nueva, con otro color y otras propiedades."], "(1) es un cambio físico; (2) es una reacción química"),
      ("Una evidencia que engaña", "Al calentar agua en una olla aparecen burbujas. ¿Es suficiente para decir que hay una reacción?", ["Las burbujas son vapor de agua.", "Al enfriarse vuelve a ser agua líquida: no se formó otra sustancia."], "No, es un cambio físico"),
  ],
  mistakes=[
      ("Creer que cualquier burbuja indica una reacción.", "El agua que hierve también forma burbujas, pero son de vapor de agua.", "Pregunta si el gas es una sustancia nueva."),
      ("Pensar que un cambio de color siempre indica reacción.", "Un colorante que se disuelve cambia el color sin formar una sustancia nueva.", "Busca más de una evidencia."),
  ],
  rec=[
      ("¿Cómo se llaman las sustancias que se transforman en una reacción química?", "Reactantes", "Son las sustancias iniciales."),
      ("Verdadero o falso: fundir hielo es una reacción química.", "Falso", "El agua sigue siendo la misma sustancia."),
      ("Un sólido que aparece al mezclar dos líquidos se llama ______ (precipitado o gas).", "Precipitado", "Es una evidencia de reacción."),
  ],
  und=[
      ("¿Cuál es una evidencia de reacción? A) Se forman burbujas de un gas nuevo al mezclar dos sustancias B) Una hoja de papel cambia de forma al romperla", "A", "Aparece una sustancia nueva, el gas."),
      ("Disolver azúcar en agua, ¿es un cambio físico o químico?", "Físico", "El azúcar se puede recuperar al evaporar el agua."),
      ("¿Qué evidencia indica que la levadura fermenta el azúcar en una botella con globo?", "El globo se infla por un gas", "El gas es un producto nuevo."),
  ],
  app=[
      ("Cuatro observaciones: (a) se disuelve sal en agua, (b) una manzana cortada se pone café, (c) una masa con levadura crece, (d) el agua hierve. ¿Cuáles son reacciones químicas?", "b y c", "En b y c se forman sustancias nuevas."),
      arith("Una mezcla estaba a 20 °C y, sin ayuda de una fuente de calor, subió a 35 °C. ¿Cuántos grados aumentó?", "35-20", "Se resta la temperatura inicial a la final: es una evidencia de reacción.", " °C"),
      arith("Una levadura produce 5 mL de gas cada 10 minutos. Con el mismo ritmo, ¿cuántos mL produce en 1 hora?", "5*6", "En una hora hay 6 períodos de 10 minutos.", " mL"),
  ],
  rea=[
      ("Una compañera dice: «Si hay burbujas, siempre hay una reacción». ¿Qué respuesta es correcta? A) No: el agua hirviendo forma burbujas de vapor sin cambiar de sustancia B) Sí: toda burbuja es un gas nuevo", "A", "Las burbujas del hervor no son un producto nuevo."),
      ("Una mezcla cambió de color. ¿Qué otra observación ayudaría a concluir que hubo reacción? A) Que además se forme un gas o cambie la temperatura B) Que el recipiente sea transparente", "A", "Más de una evidencia hace más sólida la conclusión."),
  ],
  cha=[
      arith("Un grupo midió 2 mL de gas a los 3 minutos, 4 mL a los 6 minutos y 6 mL a los 9 minutos. Si el ritmo se mantiene, ¿cuántos mL habrá a los 15 minutos?", "2*5", "El gas aumenta 2 mL cada 3 minutos; en 15 minutos hay 5 intervalos.", " mL"),
      ("Para comprobar si la temperatura influye en la fermentación, ¿qué debes mantener igual en todas las pruebas? A) La cantidad de levadura, de azúcar y de agua B) La temperatura del agua", "A", "Solo debe cambiar la variable que investigas."),
  ],
  context=[arith("Una masa con levadura de 500 mL se deja en un lugar tibio y, una hora después, duplicó su volumen. ¿Cuántos mL tiene ahora?", "500*2", "Duplicar es multiplicar por 2.", " mL")],
  selfcheck=[("¿Qué es una reacción química?", "Un proceso en que unas sustancias se transforman en otras", "Los átomos se reordenan."), ("Nombra tres evidencias de reacción.", "Gas, precipitado y cambio de temperatura", "También el color, el olor y la luz."), ("¿Por qué hace falta más de una evidencia?", "Porque una sola puede engañar", "Hervir agua forma burbujas sin reacción.")],
  open_task=task("Datos de ejemplo de un experimento de fermentación: en una botella plástica con 1 cucharadita de levadura, 1 de azúcar y 100 mL de agua tibia se pone un globo en el cuello. La circunferencia del globo mide 20 cm al inicio, 24 cm a los 5 min, 28 cm a los 10 min y 32 cm a los 15 min. Haz una tabla, calcula cuántos centímetros crece cada 5 minutos, predice la medida a los 25 minutos y nombra dos evidencias de reacción. Si lo haces en casa, que lo supervise una persona adulta y no uses agua caliente.", "Crece 4 cm cada 5 minutos. A los 25 minutos: 32 + 4 + 4 = 40 cm. Evidencias: el globo se infla por el gas producido y, a veces, cambia el olor de la mezcla.", ["tabla con cuatro tiempos", "crecimiento de 4 cm por intervalo", "predicción de 40 cm", "dos evidencias nombradas"], ["tabla y cálculo"], ["decir que el globo se infla por aire de la botella", "no usar los cuatro datos"], "Pregunta qué cambiaría si el agua estuviera más fría."),
  reinforce="Escribe tres cambios físicos y tres reacciones químicas de la vida diaria.",
  extend="Explica por qué la oxidación de un clavo es una reacción aunque sea muy lenta.")

L(OA, 2,
  materials="Este cuaderno y lápiz. Las reacciones se estudian con datos escritos; no se hace fuego ni se mezclan productos en casa.",
  use="Aprenderé tres reacciones de la vida diaria: la fermentación, la combustión y la oxidación, con sus reactantes, productos y evidencias. Sirve para explicar el pan, el calefactor y el óxido.",
  prior=["Sé las evidencias de una reacción química.", "Sé qué son reactantes y productos."],
  explain=[
      "La fermentación es una reacción en que microorganismos, como la levadura, transforman un azúcar en otras sustancias sin necesitar oxígeno. En palabras: glucosa → etanol + dióxido de carbono. El dióxido de carbono es un gas que queda atrapado en la masa y la hace crecer; el etanol se evapora al hornear. También se usa para hacer yogur y bebidas fermentadas.",
      "La combustión es una reacción rápida de un combustible con oxígeno que libera energía como calor y luz. Por ejemplo, el gas de un calefactor: metano + oxígeno → dióxido de carbono + agua. En un motor se quema bencina de forma parecida. Si falta oxígeno, la combustión es incompleta y se forma monóxido de carbono, un gas tóxico, incoloro e inodoro. Por eso los calefactores deben ventilarse y no se usan braseros en piezas cerradas. Si sientes dolor de cabeza, mareo o náuseas con un calefactor encendido, sal al aire libre y avisa a una persona adulta.",
      "La oxidación de un metal es su reacción con el oxígeno, a veces con ayuda del agua. El hierro forma herrumbre: hierro + oxígeno → óxido de hierro. Es lenta y se reconoce por el cambio de color y de textura. El aluminio también se oxida, pero forma una capa muy delgada que protege al metal de seguir reaccionando. Se protege el hierro con pintura, aceite o una capa de zinc.",
  ],
  vocab=[("fermentación", "reacción en que un microorganismo transforma azúcares sin oxígeno"), ("combustión", "reacción rápida de un combustible con oxígeno que libera calor y luz"), ("oxidación", "reacción de un metal con el oxígeno"), ("combustible", "sustancia que se quema para liberar energía"), ("herrumbre", "óxido de hierro que se forma en el hierro oxidado"), ("monóxido de carbono", "gas tóxico, incoloro e inodoro, que se forma en una combustión incompleta")],
  worked=[
      ("Reactantes y productos", "En «metano + oxígeno → dióxido de carbono + agua», ¿cuáles son los reactantes y cuáles los productos?", ["Los reactantes están antes de la flecha.", "Los productos están después de la flecha."], "Reactantes: metano y oxígeno. Productos: dióxido de carbono y agua"),
      ("Evidencia de la oxidación", "Un clavo de hierro pasa de gris a anaranjado y se vuelve quebradizo con los días. ¿Qué evidencias de reacción hay?", ["Hay un cambio de color.", "Hay un cambio de textura, que indica una sustancia nueva."], "Cambio de color y de textura"),
  ],
  mistakes=[
      ("Creer que la herrumbre es suciedad que se pega al hierro.", "Es óxido de hierro, una sustancia nueva formada por una reacción.", "Pregunta si el material cambió de propiedades."),
      ("Pensar que una combustión siempre produce solo dióxido de carbono y agua.", "Con poco oxígeno también se forma monóxido de carbono.", "Revisa si hay buena ventilación."),
  ],
  rec=[
      ("¿Qué gas produce la levadura al fermentar el azúcar?", "Dióxido de carbono", "Hace crecer la masa."),
      ("Además del combustible, ¿qué reactante necesita una combustión?", "Oxígeno", "Es lo que se combina con el combustible."),
      ("Verdadero o falso: la herrumbre es un producto de la oxidación del hierro.", "Verdadero", "Es óxido de hierro."),
  ],
  und=[
      ("Productos de la combustión completa de la bencina, formada por carbono e hidrógeno, con oxígeno suficiente: A) dióxido de carbono y agua B) monóxido de carbono e hidrógeno", "A", "Con oxígeno suficiente el carbono y el hidrógeno forman estos productos."),
      ("¿Por qué crece la masa del pan? A) El dióxido de carbono queda atrapado en ella B) El agua se transforma en harina", "A", "El gas forma burbujas en la masa."),
      ("¿Por qué un calefactor necesita ventilación?", "Para evitar monóxido de carbono por falta de oxígeno", "El monóxido es tóxico y no se huele."),
  ],
  app=[
      ("En la ecuación «glucosa → etanol + dióxido de carbono», ¿cuántos productos hay?", "2", "Son el etanol y el dióxido de carbono."),
      ("Una reja de hierro de un jardín se cubre de manchas anaranjadas después de un invierno lluvioso. ¿Qué reacción ocurre y con qué sustancia del aire?", "Oxidación, con oxígeno", "El hierro reacciona con el oxígeno."),
      arith("Una masa de 500 g se hornea y el pan resultante pesa 450 g (valores de ejemplo). ¿Cuántos gramos salieron como gas y vapor?", "500-450", "Se resta la masa final a la inicial.", " g"),
  ],
  rea=[
      ("Un compañero dice que la herrumbre es solo suciedad. ¿Qué respuesta es correcta? A) No: es un compuesto nuevo, el óxido de hierro, producto de una reacción B) Sí: se puede limpiar con agua", "A", "Tiene otras propiedades que el hierro original."),
      ("El aluminio casi no se ve «oxidado». ¿Por qué? A) Su óxido forma una capa delgada que lo protege B) No reacciona con el oxígeno", "A", "La capa evita que la reacción continúe."),
  ],
  cha=[
      ("Un brasero encendido dentro de una pieza cerrada. ¿Por qué es peligroso?", "Porque produce monóxido de carbono al faltar oxígeno", "La combustión incompleta forma un gas tóxico."),
      ("Sin hacerlo en casa, predice qué le pasaría a la llama de una vela si se tapara con un vaso grande. ¿Qué ocurre y por qué? A) Se apaga cuando se consume el oxígeno B) Se hace más intensa", "A", "La combustión necesita oxígeno."),
  ],
  context=[ex("Una persona con un calefactor encendido siente dolor de cabeza y mareo. ¿Qué debe hacer primero? A) Salir a un lugar con aire fresco y avisar a una persona adulta B) Cerrar más la pieza para guardar el calor", "A", "Puede ser monóxido de carbono; hay que ventilar y pedir ayuda.")],
  selfcheck=[("¿Qué reacción permite que el pan crezca?", "La fermentación", "Produce dióxido de carbono."), ("¿Qué libera una combustión?", "Calor y luz", "Es una reacción que libera energía."), ("¿Cómo se protege el hierro de la oxidación?", "Con pintura, aceite o zinc", "Se aísla del oxígeno y de la humedad.")],
  open_task=task("Completa una tabla de tres filas (fermentación, combustión y oxidación) con las columnas reactantes, productos, evidencias y un uso o riesgo, con estos datos: glucosa → etanol + dióxido de carbono; metano + oxígeno → dióxido de carbono + agua; hierro + oxígeno → óxido de hierro. Añade una medida de seguridad para el calefactor.", "Fermentación: glucosa; etanol y dióxido de carbono; gas; pan o yogur. Combustión: metano y oxígeno; dióxido de carbono y agua; calor y luz; riesgo de monóxido si falta ventilación. Oxidación: hierro y oxígeno; óxido de hierro; color y textura; corrosión. Seguridad: ventilar la pieza y avisar a una persona adulta si hay mareo.", ["tres filas completas", "evidencias coherentes", "una medida de seguridad"], ["tabla completa y una frase"], ["poner el agua como reactante de la fermentación", "olvidar la ventilación"], "Pregunta qué cambia si falta oxígeno en la combustión."),
  reinforce="Escribe los reactantes y los productos de la combustión del metano.",
  extend="Explica por qué la fermentación de la masa deja de ser útil si se hornea durante demasiado tiempo.")

L(OA, 3,
  materials="Este cuaderno y lápiz. Para el modelo de átomos puedes usar bolitas o botones de tres colores, pero no es obligatorio: todo se puede dibujar.",
  use="Aprenderé a leer y escribir fórmulas y ecuaciones químicas y a representar una reacción con un modelo de partículas. Sirve para describir reacciones de forma universal.",
  prior=["Sé que los átomos se unen formando moléculas.", "Sé que los símbolos de los elementos tienen una o dos letras."],
  explain=[
      "Cada elemento tiene un símbolo: H es hidrógeno, C es carbono, O es oxígeno, N es nitrógeno y Fe es hierro. Una fórmula indica qué átomos forman una sustancia. El subíndice, el número pequeño, indica cuántos átomos hay: H2O tiene 2 átomos de H y 1 de O. El coeficiente es el número grande delante de la fórmula e indica cuántas unidades hay: 3 H2O son 3 moléculas de agua, es decir, 6 átomos de H y 3 de O.",
      "Una ecuación química representa una reacción: los reactantes van a la izquierda de la flecha y los productos a la derecha. Los símbolos (s), (l), (g) y (ac) indican sólido, líquido, gas y disuelto en agua. Por ejemplo, CH4 + 2 O2 → CO2 + 2 H2O se lee: una molécula de metano reacciona con dos moléculas de oxígeno y forma una molécula de dióxido de carbono y dos de agua.",
      "Un modelo de partículas dibuja cada átomo como un círculo de un color. En una reacción, los enlaces entre átomos se rompen y se forman nuevos: los átomos se reordenan, pero no desaparecen. Una ecuación es un modelo con límites: muestra qué sustancias participan y en qué proporción, pero no muestra la rapidez de la reacción ni la energía. En esta lección solo leerás y escribirás ecuaciones ya completas; el ajuste de los coeficientes se estudia en la unidad siguiente, sobre la conservación de los átomos y la masa.",
  ],
  vocab=[("símbolo químico", "una o dos letras que representan un elemento"), ("fórmula", "representación de los átomos que forman una sustancia"), ("subíndice", "número pequeño que indica cuántos átomos hay de un elemento"), ("coeficiente", "número delante de una fórmula que indica cuántas unidades hay"), ("ecuación química", "representación de una reacción con fórmulas y una flecha"), ("modelo de partículas", "dibujo que representa átomos y moléculas con círculos")],
  worked=[
      ("Contar átomos", "¿Cuántos átomos de H y de O hay en 3 H2O?", ["El subíndice da 2 H y 1 O en cada molécula.", "El coeficiente 3 multiplica: 3 × 2 = 6 H y 3 × 1 = 3 O."], "6 átomos de H y 3 átomos de O"),
      ("Leer una ecuación", "Lee 2 H2 + O2 → 2 H2O.", ["Antes de la flecha están los reactantes: 2 moléculas de H2 y 1 de O2.", "Después de la flecha está el producto: 2 moléculas de H2O."], "Dos moléculas de hidrógeno y una de oxígeno forman dos moléculas de agua"),
  ],
  mistakes=[
      ("Confundir el coeficiente con el subíndice.", "El coeficiente multiplica toda la fórmula; el subíndice se refiere solo al átomo anterior.", "Cuenta primero los átomos de una unidad y luego multiplica por el coeficiente."),
      ("Pensar que los átomos desaparecen en una reacción.", "Se reordenan: los mismos átomos forman sustancias distintas.", "Cuenta los átomos antes y después de la flecha."),
  ],
  rec=[
      ("En H2O, ¿cuántos átomos de hidrógeno hay en cada molécula?", "2", "El subíndice 2 se refiere al hidrógeno."),
      ("En 3 CO2, ¿cuál es el coeficiente?", "3", "Es el número que está delante de la fórmula."),
      ("Verdadero o falso: en una ecuación, los reactantes se escriben a la izquierda de la flecha.", "Verdadero", "Los productos van a la derecha."),
  ],
  und=[
      ("¿Cuántos átomos de oxígeno hay en 2 H2O?", "2", "Cada molécula tiene un átomo de oxígeno y hay dos moléculas."),
      ("En CH4 + 2 O2 → CO2 + 2 H2O, ¿cuáles son los reactantes?", "CH4 y O2", "Están a la izquierda de la flecha."),
      ("¿Qué significa (g) escrito después de una fórmula?", "Que la sustancia es un gas", "Es el símbolo del estado gaseoso."),
  ],
  app=[
      arith("¿Cuántos átomos de hidrógeno hay en 3 CH4?", "3*4", "Cada molécula de CH4 tiene 4 átomos de hidrógeno y hay 3 moléculas.", " átomos"),
      arith("¿Cuántos átomos hay en total en 2 H2O?", "2*3", "Cada molécula tiene 3 átomos (2 de H y 1 de O) y hay 2 moléculas.", " átomos"),
      ("Escribe con palabras la ecuación C + O2 → CO2.", "El carbono reacciona con el oxígeno y forma dióxido de carbono", "El reactante son C y O2 y el producto es CO2."),
  ],
  rea=[
      ("Un estudiante interpreta 3 H2O como 3 átomos de hidrógeno y 2 de oxígeno. ¿Cuál es el error? A) Confunde el coeficiente con el subíndice: son 6 de H y 3 de O B) No hay error", "A", "El coeficiente multiplica toda la fórmula."),
      ("H2O(s) → H2O(l) representa el derretimiento del hielo. ¿Es una reacción química?", "No, es un cambio físico", "La sustancia es la misma antes y después."),
  ],
  cha=[
      arith("En 4 Fe + 3 O2 → 2 Fe2O3, ¿cuántos átomos de oxígeno hay en los productos?", "2*3", "Cada Fe2O3 tiene 3 átomos de oxígeno y hay 2 unidades.", " átomos"),
      ("¿Qué información no entrega una ecuación química? A) La rapidez con que ocurre la reacción B) Las sustancias que participan", "A", "Una ecuación no muestra la rapidez ni la energía."),
  ],
  context=[ex("En la etiqueta de ejemplo de una cocina a gas aparece CH4 + 2 O2 → CO2 + 2 H2O. Por cada molécula de metano que se quema, ¿cuántas moléculas de agua se forman?", "2", "El coeficiente de H2O es 2.")],
  selfcheck=[("¿Qué indica un subíndice?", "Cuántos átomos hay de un elemento en la fórmula", "Se refiere al átomo que está antes."), ("¿Qué indica un coeficiente?", "Cuántas unidades hay de esa sustancia", "Multiplica toda la fórmula."), ("¿Qué pasa con los átomos en una reacción?", "Se reordenan pero no desaparecen", "Cambian de pareja.")],
  open_task=task("Dibuja con círculos (C negro, H blanco y O rojo) el modelo de partículas de CH4 + 2 O2 → CO2 + 2 H2O: una molécula de metano y dos de oxígeno a la izquierda; una de CO2 y dos de agua a la derecha. Cuenta los átomos de cada elemento antes y después. Escribe la ecuación con palabras y una limitación del modelo.", "Antes: 1 C, 4 H, 4 O. Después: 1 C, 4 H, 4 O. En palabras: una molécula de metano y dos de oxígeno forman una de dióxido de carbono y dos de agua. Limitación: el dibujo no muestra la rapidez ni la energía liberada.", ["dibujo con las cinco moléculas", "conteo antes y después", "ecuación en palabras", "una limitación"], ["dibujo y conteo"], ["dibujar menos átomos de oxígeno", "no contar antes y después"], "Pregunta cómo mostrarías que se libera energía."),
  reinforce="Cuenta los átomos de H y de O en 4 H2O.",
  extend="Explica por qué no basta con mirar un dibujo para saber si una reacción es rápida.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Los datos del experimento son de ejemplo y están escritos en la lección.",
  use="Aprenderé cómo influyen la cantidad de sustancia, la temperatura, el volumen y la presión en una reacción, y a leer datos de un experimento. Sirve para controlar la rapidez de una reacción.",
  prior=["Sé las evidencias de una reacción.", "Sé leer tablas y comparar valores."],
  explain=[
      "Para que ocurra una reacción, las partículas deben chocar con suficiente energía. Mientras más choques efectivos por segundo, más rápida es la reacción. Si hay más cantidad de sustancia en el mismo volumen, hay más partículas y más choques. Si sube la temperatura, las partículas se mueven más rápido y chocan con más energía. Cuidado: una temperatura demasiado alta mata a la levadura, que deja de fermentar sobre unos 60 °C.",
      "En los gases, si se reduce el volumen o se aumenta la presión, las partículas quedan más cerca y chocan más veces, así que la reacción es más rápida. En un experimento hay tres tipos de variables: la independiente es la que cambias, la dependiente es la que mides y las controladas son las que mantienes iguales. Si cambias dos variables a la vez, no puedes saber cuál produjo el efecto.",
      "Datos de ejemplo con 100 mL de agua. Tabla A, a 30 °C: con 1, 2 y 3 cucharaditas de levadura se obtienen 4, 8 y 12 mL de gas en 10 minutos. Tabla B, con 2 cucharaditas de levadura: a 10, 20, 30, 40 y 60 °C se obtienen 2, 5, 8, 10 y 0 mL de gas en 10 minutos.",
  ],
  vocab=[("variable independiente", "variable que el investigador cambia"), ("variable dependiente", "variable que se mide como resultado"), ("variable controlada", "variable que se mantiene igual en todas las pruebas"), ("choque efectivo", "choque entre partículas con energía suficiente para reaccionar"), ("rapidez de reacción", "cantidad de producto formado en cada unidad de tiempo"), ("presión", "fuerza que ejerce un gas por unidad de superficie")],
  worked=[
      ("Identificar variables", "En la tabla B, ¿cuál es la variable independiente y cuál la dependiente?", ["Lo que se cambia entre pruebas es la temperatura.", "Lo que se mide es el volumen de gas."], "Independiente: temperatura. Dependiente: volumen de gas"),
      ("Variables controladas", "Para comparar dos temperaturas, ¿qué hay que mantener igual?", ["Solo debe cambiar la temperatura.", "Se mantienen la cantidad de levadura, el azúcar, el agua y el tiempo."], "Levadura, azúcar, agua y tiempo"),
  ],
  mistakes=[
      ("Cambiar dos variables a la vez.", "No se sabe cuál produjo el cambio.", "Cambia una y controla las demás."),
      ("Pensar que a mayor temperatura la reacción siempre es más rápida.", "En las reacciones con seres vivos, como la levadura, una temperatura demasiado alta los mata.", "Revisa los datos hasta el valor más alto."),
  ],
  rec=[
      ("¿Qué variable se mide como resultado en un experimento?", "La variable dependiente", "Es la que responde al cambio."),
      ("Verdadero o falso: más choques efectivos por segundo hacen más rápida la reacción.", "Verdadero", "Más choques efectivos producen más producto por segundo."),
      ("¿Qué ocurre con la levadura sobre unos 60 °C?", "Muere y deja de fermentar", "La temperatura es demasiado alta."),
  ],
  und=[
      ("Según la tabla B, ¿a qué temperatura se produjo más gas?", "A 40 °C", "Se obtuvieron 10 mL, el valor mayor."),
      ("¿Por qué a 60 °C no se produjo gas? A) La levadura murió B) El azúcar desapareció", "A", "El calor excesivo destruyó la levadura."),
      ("En la tabla A, ¿cuál es la variable independiente?", "La cantidad de levadura", "Es la que se cambia entre pruebas."),
  ],
  app=[
      arith("En la tabla A, ¿cuántos mL más de gas se obtienen con 3 cucharaditas que con 1?", "12-4", "Se resta el gas de 1 cucharadita al de 3.", " mL"),
      arith("Con 2 cucharaditas de levadura a 30 °C se produjeron 8 mL de gas en 10 minutos. Si el ritmo se mantiene, ¿cuántos mL se producen en 30 minutos?", "8*3", "En 30 minutos hay 3 períodos de 10 minutos.", " mL"),
      ("Quieres comparar el efecto de la cantidad de azúcar. ¿Qué dos variables mantienes iguales?", "La temperatura y la cantidad de levadura", "Solo debe cambiar el azúcar."),
  ],
  rea=[
      ("Una compañera dice: «A más temperatura, siempre más rápido». ¿Qué responde la tabla B? A) No siempre: a 60 °C no hubo gas porque la levadura murió B) Sí: a 60 °C hubo más gas", "A", "La levadura tiene un límite de temperatura."),
      ("Un gas está en un recipiente con émbolo. Si reduces su volumen, la reacción entre sus partículas: A) es más rápida porque chocan más B) es más lenta porque chocan menos", "A", "Las partículas están más cerca."),
  ],
  cha=[
      arith("En la tabla A cada cucharadita produce 4 mL. Si el patrón continúa, ¿cuántos mL producirían 5 cucharaditas?", "4*5", "Se multiplica el gas por cucharadita por el número de cucharaditas.", " mL"),
      ("Un grupo cambia a la vez la temperatura y la cantidad de levadura y obtiene más gas. ¿Por qué no pueden concluir cuál variable lo causó?", "Porque cambiaron dos variables a la vez", "No hay forma de separar los efectos."),
  ],
  context=[ex("En invierno la masa del pan tarda más en subir que en verano. ¿Por qué? A) El frío reduce el movimiento de las partículas y los choques efectivos B) En invierno hay menos oxígeno en la masa", "A", "A menor temperatura, menos choques efectivos.")],
  selfcheck=[("¿Qué es una variable controlada?", "La que se mantiene igual en todas las pruebas", "Evita que otras causas afecten el resultado."), ("¿Cómo influye la temperatura en la rapidez de una reacción?", "Al subir, suele aumentar, hasta cierto límite", "Hay más choques con mayor energía."), ("¿Qué pasa con la rapidez si disminuye el volumen de un gas?", "Aumenta", "Hay más choques.")],
  open_task=task("Datos de ejemplo con 2 cucharaditas de levadura: a 10 °C, 2 mL de gas en 10 minutos; a 20 °C, 5 mL; a 30 °C, 8 mL; a 40 °C, 10 mL; a 60 °C, 0 mL. Haz un gráfico de líneas con la temperatura en el eje horizontal y los mL en el vertical. Indica las tres clases de variables, describe el patrón entre 10 °C y 40 °C y explica el dato de 60 °C. Propón una temperatura para probar a continuación.", "Independiente: temperatura. Dependiente: volumen de gas. Controladas: levadura, azúcar, agua y tiempo. Entre 10 y 40 °C el gas aumenta con la temperatura. A 60 °C la levadura muere. Una prueba nueva: 35 °C, para ubicar mejor la temperatura óptima.", ["gráfico con los cinco datos", "tres variables identificadas", "patrón descrito", "explica el dato de 60 °C"], ["gráfico y explicación"], ["unir 60 °C como si siguiera el patrón", "no mencionar las variables controladas"], "Pregunta qué medirías para estar seguro de que murió la levadura."),
  reinforce="Escribe una variable independiente, una dependiente y dos controladas para un experimento con levadura.",
  extend="Explica por qué una reacción con gases puede ser más rápida al reducir el volumen.")

L(OA, 5,
  materials="Este cuaderno, lápiz y calculadora. Los valores numéricos son de ejemplo y están escritos en cada ejercicio.",
  use="Aprenderé el impacto de la combustión, la oxidación y la fermentación en los seres vivos y en el entorno. Sirve para tomar decisiones informadas sobre energía, alimentos y materiales.",
  prior=["Sé qué productos tienen las reacciones de la clase anterior.", "Sé qué es el efecto invernadero."],
  explain=[
      "La combustión libera dióxido de carbono, un gas de efecto invernadero que aumenta la temperatura del planeta. También puede liberar monóxido de carbono, que es tóxico, y partículas de humo que dañan los pulmones. Los óxidos de azufre y de nitrógeno, que se producen al quemar algunos combustibles, causan lluvia ácida. En el sur y el centro de Chile, la leña húmeda y la calefacción ineficiente producen episodios de mala calidad del aire en invierno. Usar leña seca, mejorar la aislación de las casas y preferir sistemas eficientes ayuda a reducir el problema.",
      "La oxidación de los metales causa corrosión: deteriora puentes, rejas y tuberías, y tiene un costo de mantenimiento. Se reduce con pintura, aceite o galvanizado. En los seres vivos hay oxidaciones útiles: la respiración celular oxida la glucosa y libera la energía que necesitan las células. La fermentación produce alimentos como el pan y el yogur, pero la fermentación no deseada echa a perder alimentos; por eso se conservan en frío.",
      "Para evaluar el impacto se usan datos. Por ejemplo, si cada litro de bencina libera unos 2 kg de dióxido de carbono (valor de ejemplo), un auto que usa 8 L libera unos 16 kg. Comparar cantidades permite elegir alternativas, como el transporte público.",
  ],
  vocab=[("gas de efecto invernadero", "gas que retiene calor en la atmósfera, como el dióxido de carbono"), ("lluvia ácida", "lluvia con ácidos formados por óxidos de azufre y de nitrógeno"), ("material particulado", "partículas muy pequeñas de humo que se pueden respirar"), ("corrosión", "deterioro de un metal por oxidación"), ("respiración celular", "reacción en las células que libera energía a partir de glucosa y oxígeno"), ("huella de carbono", "cantidad de dióxido de carbono que libera una actividad")],
  worked=[
      ("Huella de carbono", "Un auto usa 5 L de bencina y cada litro libera 2 kg de dióxido de carbono (valor de ejemplo). ¿Cuántos kg libera?", ["Multiplico los litros por el dióxido de carbono de cada litro.", "Calculo 5 × 2."], "10 kg"),
      ("Evaluar una medida", "¿Por qué la leña seca contamina menos que la húmeda?", ["La leña húmeda gasta energía en evaporar el agua.", "Se quema peor, con más humo y más partículas."], "Porque se quema mejor y produce menos humo"),
  ],
  mistakes=[
      ("Decir que quemar siempre es malo y no tiene ventajas.", "La combustión entrega energía útil, pero sus productos tienen impactos que hay que reducir.", "Evalúa ventajas y costos con datos."),
      ("Pensar que la corrosión solo ocurre en el mar.", "Ocurre en cualquier lugar con oxígeno y humedad, solo que más rápido en ambientes salinos.", "Considera la humedad y la sal como factores."),
  ],
  rec=[
      ("¿Qué gas de efecto invernadero libera la combustión?", "Dióxido de carbono", "Retiene calor en la atmósfera."),
      ("Verdadero o falso: el monóxido de carbono es un gas tóxico.", "Verdadero", "Impide el transporte de oxígeno en la sangre."),
      ("¿Cómo se llama el deterioro de un metal por oxidación?", "Corrosión", "Debilita las estructuras metálicas."),
  ],
  und=[
      ("La lluvia ácida se forma principalmente por: A) óxidos de azufre y de nitrógeno disueltos en el agua B) nubes muy bajas", "A", "Esos gases forman ácidos en la lluvia."),
      ("Para reducir la contaminación por calefacción a leña conviene: A) usar leña seca B) usar leña húmeda", "A", "La leña seca quema mejor."),
      ("¿Cómo ayuda el frío a conservar alimentos?", "Hace más lenta la fermentación y la descomposición", "A menor temperatura, las reacciones son más lentas."),
  ],
  app=[
      arith("Un auto usa 7 L de bencina y cada litro libera 2 kg de dióxido de carbono (valor de ejemplo). ¿Cuántos kg libera?", "7*2", "Se multiplica el consumo por el dióxido de carbono de cada litro.", " kg"),
      arith("Una estufa a leña quema 6 kg por día. ¿Cuántos kg quema en 30 días?", "6*30", "Se multiplica el consumo diario por los días.", " kg"),
      ("Para proteger una reja de hierro de la oxidación conviene: A) pintarla para aislarla del oxígeno y de la humedad B) mojarla seguido", "A", "La pintura impide el contacto con los reactantes."),
  ],
  rea=[
      ("Un estudiante dice: «Quemar siempre es malo». ¿Qué respuesta es más adecuada? A) La combustión da energía útil, pero sus productos tienen impactos y se busca reducirlos B) La combustión no produce nada", "A", "Hay beneficios y costos que se deben evaluar."),
      ("Para obtener el mismo calor, ¿qué opción es más riesgosa dentro de una pieza cerrada: un brasero a carbón o un calefactor con salida de gases al exterior?", "El brasero", "Acumula monóxido de carbono en la pieza."),
  ],
  cha=[
      arith("En un día de alerta ambiental, la concentración de partículas es de 150 unidades (de ejemplo) y la referencia es de 50. ¿Cuántas veces supera la referencia?", "150/50", "Se divide la concentración por la referencia.", " veces"),
      ("La respiración celular es C6H12O6 + 6 O2 → 6 CO2 + 6 H2O + energía. ¿Es una oxidación de la glucosa?", "Sí", "La glucosa reacciona con oxígeno y libera energía."),
  ],
  context=[ex("Hay una alerta ambiental por humo. ¿Qué medida es adecuada? A) Evitar ejercicio intenso al aire libre B) Salir a correr más tiempo", "A", "Respirar más aire con partículas aumenta el daño.")],
  selfcheck=[("¿Qué efecto tiene el dióxido de carbono en la atmósfera?", "Retiene calor", "Es un gas de efecto invernadero."), ("¿Qué es la corrosión?", "El deterioro de un metal por oxidación", "Tiene un costo de mantenimiento."), ("Da una forma de reducir la contaminación por leña.", "Usar leña seca y mejorar la aislación", "Se quema mejor y se necesita menos.")],
  open_task=task("Completa una tabla con combustión, oxidación y fermentación: un efecto positivo, un efecto negativo y una medida para reducir el negativo. Usa estos datos de ejemplo: un auto libera 2 kg de dióxido de carbono por litro y un viaje usa 12 L; una estufa a leña quema 6 kg por día. Calcula el dióxido de carbono del viaje y escribe una decisión informada para reducir la contaminación en tu casa.", "Combustión: energía útil; dióxido de carbono y humo; leña seca o transporte público. Oxidación: respiración celular; corrosión; pintura. Fermentación: pan y yogur; alimentos echados a perder; conservar en frío. Viaje: 12 × 2 = 24 kg de dióxido de carbono. Decisión: usar leña seca y mejorar la aislación.", ["tabla de tres filas", "24 kg", "decisión con evidencia"], ["tabla, cálculo y decisión"], ["decir que la fermentación solo tiene efectos negativos", "olvidar la medida"], "Pregunta qué dato necesitarías para comparar dos calefactores."),
  reinforce="Escribe un efecto negativo y una medida para la combustión.",
  extend="Explica por qué el humo de leña húmeda es más dañino que el de leña seca.")

L(OA, 6,
  materials="Este cuaderno, lápiz y calculadora. No se hace ningún experimento con productos de limpieza ni con fuego. Los datos son de ejemplo.",
  use="Aprenderé los límites de las evidencias y las reglas de seguridad con las reacciones químicas del hogar. Sirve para cuidarte y para evaluar afirmaciones con criterio.",
  prior=["Sé las evidencias de una reacción.", "Sé qué es una variable y qué es una medición."],
  explain=[
      "Una evidencia aislada tiene límites. Las burbujas pueden ser vapor, un cambio de color puede ser solo una disolución y un calor puede venir de otra fuente. Para concluir se necesitan varias evidencias, un grupo de comparación y repetir las mediciones. Toda medición tiene incertidumbre, que es el margen de duda: si dos medidas difieren menos que esa incertidumbre, no se puede asegurar que sean distintas.",
      "En el hogar hay riesgos químicos. Nunca se deben mezclar productos de limpieza, porque pueden formar gases tóxicos; por ejemplo, la mezcla de cloro con otros limpiadores. Se usan en lugares ventilados, siguiendo la etiqueta, y se guardan lejos de niños y niñas. Los calefactores y braseros pueden producir monóxido de carbono; se ventilan, se revisan y no se usan braseros en piezas cerradas. Si hay olor fuerte, mareo o dolor de cabeza, sal al aire libre y avisa a una persona adulta.",
      "Las decisiones sobre reacciones químicas también tienen implicancias sociales. Elegir combustibles, regular emisiones y proteger los alimentos requieren comparar costos y beneficios con datos, reconocer incertidumbre y escuchar a las personas afectadas.",
  ],
  vocab=[("incertidumbre", "margen de duda de una medición"), ("grupo de comparación", "prueba que no recibe el factor estudiado y sirve de referencia"), ("ventilación", "entrada de aire fresco a un espacio"), ("intoxicación", "daño por respirar o tragar una sustancia tóxica"), ("regulación", "norma que limita una actividad para proteger a las personas y al ambiente"), ("costo-beneficio", "comparación de lo que se gana y lo que se pierde con una decisión")],
  worked=[
      ("Evidencia insuficiente", "Al calentar agua en una olla se forman burbujas. ¿Basta esa evidencia para decir que hubo una reacción?", ["Las burbujas son de vapor de agua.", "Hay que ver si se formó una sustancia nueva."], "No, hace falta otra evidencia"),
      ("Seguridad en el hogar", "Quieres que un limpiador funcione mejor mezclándolo con otro. ¿Qué haces?", ["Los productos de limpieza pueden formar gases tóxicos al mezclarse.", "Se usan por separado y en un lugar ventilado."], "No los mezclo"),
  ],
  mistakes=[
      ("Mezclar productos de limpieza para que limpien más.", "Pueden formar gases tóxicos.", "Úsalos por separado, ventilados y según la etiqueta."),
      ("Comparar dos mediciones sin considerar la incertidumbre.", "Si la diferencia es menor que la incertidumbre, no se puede concluir.", "Repite la medición y calcula el rango."),
  ],
  rec=[
      ("Verdadero o falso: se pueden mezclar productos de limpieza para que limpien más.", "Falso", "Pueden formar gases tóxicos."),
      ("Si sientes mareo con un calefactor encendido, ¿qué haces primero?", "Salgo al aire libre y aviso a una persona adulta", "Puede ser monóxido de carbono."),
      ("¿Una sola evidencia basta siempre para asegurar una reacción?", "No", "Una sola puede engañar."),
  ],
  und=[
      ("Las burbujas al hervir agua no indican reacción porque: A) son vapor de agua y el agua sigue siendo agua B) se forma oxígeno", "A", "No hay sustancia nueva."),
      ("¿Por qué conviene leer la etiqueta de un producto de limpieza?", "Porque indica sus riesgos y cómo usarlo con seguridad", "La etiqueta entrega advertencias."),
      ("¿Qué es la incertidumbre de una medición?", "El margen de duda de la medida", "Toda medición tiene alguna."),
  ],
  app=[
      ("Dos medidas de gas son 11 mL y 13 mL, y cada lectura tiene una incertidumbre de ±2 mL. ¿Se puede asegurar que son realmente distintas?", "No", "Los rangos, de 9 a 13 y de 11 a 15, se superponen."),
      arith("Para ventilar una pieza se abren las ventanas 10 minutos cada hora durante 6 horas. ¿Cuántos minutos de ventilación son en total?", "10*6", "Se multiplican los minutos por las horas.", " minutos"),
      ("Un frasco de limpiador dice «no mezclar con otros productos». ¿Qué haces?", "No lo mezclo y lo uso por separado y ventilado", "Se evita formar gases tóxicos."),
  ],
  rea=[
      ("Un compañero dice: «Si cambia de color, es una reacción segura». ¿Qué contraejemplo sirve? A) Disolver un colorante en agua cambia el color sin formar una sustancia nueva B) El colorante no puede disolverse", "A", "El color solo no basta."),
      ("¿Qué decisión es más informada? A) Comparar costos y beneficios con datos y escuchar a los afectados B) Elegir según la opinión de la mayoría sin datos", "A", "Los datos y la participación mejoran la decisión."),
  ],
  cha=[
      arith("Tres pruebas con la misma mezcla produjeron 10 mL, 12 mL y 11 mL de gas. ¿Cuál es el promedio?", "(10+12+11)/3", "Se suman las tres medidas y se divide por 3.", " mL"),
      ("Un vendedor afirma que su producto «no contamina». ¿Qué pregunta sobre la evidencia le harías? A) ¿Qué sustancias produce y en qué cantidad? B) ¿De qué color es el envase?", "A", "Los datos de productos y cantidades permiten evaluar la afirmación."),
  ],
  context=[ex("En una casa, el detector de monóxido de carbono suena. ¿Qué corresponde hacer? A) Salir al aire libre y avisar a una persona adulta B) Silenciar la alarma y seguir como antes", "A", "El monóxido de carbono es peligroso y no se huele.")],
  selfcheck=[("¿Por qué una evidencia aislada puede engañar?", "Porque un cambio físico puede imitarla", "Hay burbujas y colores sin reacción."), ("Nombra una regla de seguridad con productos de limpieza.", "No mezclarlos", "Pueden formar gases tóxicos."), ("¿Qué es la incertidumbre?", "El margen de duda de una medición", "Se debe considerar al comparar datos.")],
  open_task=task("Evalúa tres casos. (a) Un sólido blanco desaparece al agregarlo al agua y el líquido queda transparente. (b) Un clavo de hierro, tras una semana, está anaranjado y quebradizo. (c) Una leche con olor agrio forma burbujas. Para cada uno, decide si hay evidencia suficiente de reacción y qué otra observación pedirías. Después escribe un afiche de cuatro reglas de seguridad para productos de limpieza y calefactores.", "(a) Probablemente es una disolución: se puede recuperar el sólido al evaporar el agua. (b) Hay reacción: cambio de color y de textura. (c) Hay fermentación: gas y olor, y el producto no es apto para consumo. Reglas: no mezclar productos, ventilar, leer la etiqueta y avisar a una persona adulta ante mareo u olor fuerte.", ["tres decisiones con evidencia", "otra observación para cada caso", "cuatro reglas de seguridad"], ["tabla de tres filas y cuatro reglas"], ["decidir con una sola evidencia", "reglas que no incluyan avisar a una persona adulta"], "Pregunta qué experimento permitiría distinguir la disolución de una reacción."),
  reinforce="Escribe una regla de seguridad para calefactores y una para productos de limpieza.",
  extend="Explica por qué repetir una medición mejora una conclusión.")

"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 08 (electricidad estática e interacciones eléctricas)."""
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


OA8 = "CN08 OA 08"

L(OA8, 1,
  materials="Este cuaderno y lápiz. Opcional: un globo inflado, un peine plástico, papel picado en trocitos y cabello limpio y seco. Nunca hagas experimentos eléctricos con enchufes ni con aparatos conectados a la red.",
  use="Aprenderé qué es la electricidad estática, cuáles son los tipos de electricidad y a plantear preguntas investigables. Sirve para explicar por qué un globo frotado atrae papelitos.",
  prior=["Sé que los átomos tienen partículas con carga.", "Sé distinguir variable independiente y dependiente."],
  explain=[
      "La materia está formada por átomos, que tienen protones con carga positiva (+) en el núcleo y electrones con carga negativa (−) alrededor. Un objeto neutro tiene igual número de protones y de electrones. Si gana electrones queda con carga negativa; si los pierde queda con carga positiva. Solo los electrones se mueven de un objeto a otro.",
      "Hay dos tipos de electricidad. La electricidad estática ocurre cuando las cargas se acumulan en un objeto y quedan en reposo. La corriente eléctrica ocurre cuando las cargas se mueven por un material conductor, como un cable. Las cargas del mismo signo se repelen y las de signo distinto se atraen. Un globo frotado con el cabello se carga y por eso atrae papelitos.",
      "Una pregunta investigable es: «¿Cuántos papelitos atrae un globo después de frotarlo 5 veces con el cabello y después de frotarlo 20 veces?». La variable que se cambia es el número de frotaciones, la que se mide es el número de papelitos atraídos, y se controlan el globo, el cabello y los papelitos. Una pregunta como «¿Cuál globo es más bonito?» no se puede investigar.",
  ],
  vocab=[("carga eléctrica", "propiedad de la materia que produce atracción o repulsión eléctrica"), ("electrón", "partícula con carga negativa que puede pasar de un objeto a otro"), ("electricidad estática", "acumulación de cargas en reposo en un objeto"), ("corriente eléctrica", "movimiento de cargas por un conductor"), ("neutro", "con igual número de cargas positivas y negativas")],
  worked=[
      ("Signo de la carga", "Un objeto neutro pierde 3 electrones. ¿Qué carga neta queda?", ["Perdió partículas negativas.", "Quedó con más cargas positivas que negativas."], "Carga positiva"),
      ("Pregunta investigable", "¿Es investigable «¿Atrae más papelitos un globo frotado 10 veces que uno frotado 2 veces?»?", ["Pregunto si se puede contar.", "Se pueden contar los papelitos atraídos."], "Sí, porque se mide el número de papelitos"),
  ],
  mistakes=[
      ("Creer que se mueven los protones.", "Los protones están en el núcleo; los electrones son los que pasan de un objeto a otro.", "Piensa en electrones que se transfieren."),
      ("Confundir electricidad estática con corriente eléctrica.", "La estática acumula cargas en reposo; la corriente es un movimiento de cargas.", "Pregunta si las cargas están quietas o en movimiento."),
  ],
  rec=[
      ("¿Qué carga tiene un electrón: positiva o negativa?", "Negativa", "Los electrones tienen carga negativa."),
      ("Cargas del mismo signo, ¿se atraen o se repelen?", "Se repelen", "Es la regla de interacción entre cargas iguales."),
      ("Verdadero o falso: la corriente eléctrica es un movimiento de cargas por un conductor.", "Verdadero", "Eso la diferencia de la electricidad estática."),
  ],
  und=[
      ("Un objeto gana electrones. ¿Qué carga neta adquiere? A) Negativa; B) Positiva.", "A", "Recibe partículas con carga negativa."),
      ("¿Qué tipo de electricidad explica que un globo frotado atraiga papelitos? A) Estática; B) Corriente.", "A", "Las cargas quedan acumuladas en el globo."),
      ("¿Qué carga tiene un objeto con igual número de protones y de electrones?", "Neutra", "Las cargas se compensan."),
  ],
  app=[
      ("¿Cuál pregunta es investigable? A) ¿Cuántos papelitos atrae un globo frotado 20 veces con el cabello? B) ¿Cuál color de globo es más lindo?", "A", "Se contesta contando."),
      ("En la pregunta de las 5 y 20 frotaciones, ¿qué variable se cambia?", "El número de frotaciones", "Es lo que difiere entre las dos pruebas."),
      ("En esa misma pregunta, ¿qué variable se mide?", "El número de papelitos atraídos", "Es el resultado que se registra."),
  ],
  rea=[
      ("Un compañero cambia el número de frotaciones y el cabello usado a la vez. ¿Qué falla tiene? A) No sabrá cuál variable causó el resultado; B) El globo no se puede frotar.", "A", "Se debe cambiar una sola variable."),
      ("Alguien dice: «El globo atrae papelitos porque los protones saltan del cabello». ¿Qué corrección haces?", "Son los electrones los que pasan de un objeto a otro", "Los protones están en el núcleo y no se transfieren."),
  ],
  cha=[
      ("Un cuerpo neutro gana 4 electrones, y otro neutro pierde 4. ¿Cuál queda negativo? A) El que ganó; B) El que perdió.", "A", "Ganar electrones deja carga negativa."),
      arith("Datos de ejemplo: un globo frotado 5 veces atrae 3 papelitos y frotado 20 veces atrae 11. ¿Cuántos papelitos más atrae con 20 frotaciones?", "11-3", "Se resta el menor al mayor."),
  ],
  context=[("Una persona de ejemplo se saca un chaleco de lana en una pieza seca y oye pequeños chasquidos. ¿Qué tipo de electricidad ocurre?", "Electricidad estática", "Las cargas acumuladas se descargan.")],
  selfcheck=[("¿Qué es la electricidad estática?", "Acumulación de cargas en reposo en un objeto", "Las cargas no se mueven por un conductor."), ("¿Qué partículas pasan de un objeto a otro?", "Los electrones", "Los protones no se mueven."), ("¿Qué hace investigable una pregunta?", "Que se puede contestar midiendo o contando", "Indica qué se mide.")],
  open_task=task("Plantea una pregunta investigable sobre cuántos papelitos atrae un globo según el tiempo de frotado con el cabello (por ejemplo 10 y 40 segundos). Escribe la variable que cambias, la que mides, dos que mantienes iguales y una predicción. Agrega una medida de seguridad.", "Pregunta: ¿Atrae más papelitos un globo frotado 40 segundos que uno frotado 10 segundos? Cambio: tiempo de frotado. Mido: número de papelitos. Igual: el mismo globo y el mismo cabello. Predicción: atrae más con 40 segundos. Seguridad: no usar enchufes y no inflar el globo con la boca si hay alergia al látex.", ["pregunta clara", "dos variables controladas", "predicción y seguridad"], ["plan breve"], ["cambiar dos variables", "pregunta de opinión"], "Pregunta qué resultado contradiría tu predicción."),
  reinforce="Escribe qué carga adquiere un objeto neutro que pierde electrones.",
  extend="Explica por qué solo los electrones, y no los protones, se transfieren entre objetos.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Todos los resultados están escritos en los ejercicios y son de ejemplo.",
  use="Aprenderé a interpretar resultados de atracción y repulsión para deducir el signo de las cargas y a reconocer qué prueba una repulsión y qué no prueba una atracción. Sirve para leer evidencia eléctrica con cuidado.",
  prior=["Sé que cargas iguales se repelen y distintas se atraen.", "Sé que un objeto neutro tiene carga neta cero."],
  explain=[
      "Para saber el signo de la carga de un objeto se lo acerca a otro cuya carga se conoce. Si se repelen, ambos tienen carga del mismo signo: la repulsión prueba que los dos están cargados con el mismo signo. Si se atraen, hay dos posibilidades: tienen signos distintos o uno de ellos está neutro, porque un objeto neutro también es atraído por uno cargado.",
      "Por eso la atracción por sí sola no prueba que los dos objetos estén cargados. Resultados de ejemplo con tres varillas: P es negativa (se sabe). Q se repele con P. R se atrae con P. De Q se concluye con seguridad que es negativa. De R solo se puede decir que es positiva o neutra. Para decidir, se acerca R a Q: si se atraen, tampoco se descarta que sea neutra; se necesita otra prueba, como un electroscopio.",
      "Un electroscopio es un aparato con dos láminas metálicas muy livianas. Al acercar o tocar un objeto cargado, las láminas se cargan con el mismo signo y se separan. Mientras más carga, más se separan. Conviene leer la evidencia con prudencia: el resultado dice qué ocurrió, y la explicación incluye qué no se puede asegurar.",
  ],
  vocab=[("repulsión", "fuerza que aleja a dos objetos con cargas del mismo signo"), ("atracción", "fuerza que acerca dos objetos"), ("electroscopio", "aparato de láminas que se separan cuando se carga"), ("carga conocida", "carga cuyo signo se sabe de antemano"), ("conclusión segura", "la que no puede ser explicada por otra posibilidad")],
  worked=[
      ("Qué prueba una repulsión", "La varilla P es negativa y la varilla Q se repele con P. ¿Qué carga tiene Q?", ["Solo cargas del mismo signo se repelen.", "Q tiene el mismo signo que P."], "Q es negativa"),
      ("Qué prueba una atracción", "La varilla P es negativa y la varilla R se atrae con P. ¿Qué carga tiene R?", ["Puede ser positiva.", "También puede ser neutra, porque un objeto neutro es atraído."], "Positiva o neutra; no se puede asegurar"),
  ],
  mistakes=[
      ("Concluir que dos objetos que se atraen están cargados con signos distintos.", "Uno puede estar neutro.", "Usa la repulsión para estar seguro."),
      ("Pensar que un objeto neutro no interactúa con los cargados.", "Un cargado puede atraer a un neutro.", "Piensa en el globo que atrae papelitos neutros."),
  ],
  rec=[
      ("¿Qué prueba una repulsión: signos iguales o signos distintos?", "Signos iguales", "Solo cargas del mismo signo se repelen."),
      ("¿Un objeto neutro puede ser atraído por uno cargado: sí o no?", "Sí", "Se reordenan sus cargas y es atraído."),
      ("Verdadero o falso: en un electroscopio, las láminas se separan al cargarse.", "Verdadero", "Se cargan con el mismo signo y se repelen."),
  ],
  und=[
      ("Una varilla A se atrae con otra de carga positiva. ¿Qué se puede asegurar de A? A) Que es negativa o neutra; B) Que es positiva.", "A", "Una atracción puede ser por signos distintos o por un objeto neutro."),
      ("Dos varillas de carga desconocida se repelen. ¿Qué se puede concluir? A) Que tienen el mismo signo; B) Que una es neutra.", "A", "La repulsión exige cargas del mismo signo."),
      ("¿Qué indica que las láminas del electroscopio se separen más?", "Que hay más carga", "A mayor carga, mayor repulsión."),
  ],
  app=[
      ("Resultados de ejemplo: la varilla X es positiva. La varilla Y se repele con X. ¿Qué carga tiene Y?", "Positiva", "Se repelen, entonces tienen el mismo signo."),
      ("Resultados de ejemplo: la varilla X es positiva. La varilla Z se atrae con X. ¿Cuántas posibilidades hay para Z?", "2", "Puede ser negativa o neutra."),
      ("En un electroscopio de ejemplo se acerca una varilla negativa y las láminas se separan 6 cm; con otra varilla se separan 2 cm. ¿Cuál tiene más carga? A) La primera; B) La segunda.", "A", "Mayor separación indica más carga."),
  ],
  rea=[
      ("Alguien dice: «Como la varilla R se atrae con la negativa P, R es positiva». ¿Qué falla ve? A) R también podría ser neutra; B) P no puede estar cargada.", "A", "Un objeto neutro también es atraído."),
      ("Un estudiante acerca R a una varilla negativa Q y se repelen. ¿Qué carga tiene R?", "Negativa", "La repulsión prueba el mismo signo."),
  ],
  cha=[
      ("Cuatro varillas de ejemplo: P es negativa. Q se repele con P. R se repele con Q. S se atrae con P. ¿Cuántas de las cuatro varillas se sabe con seguridad que son negativas?", "3", "P, Q y R: las tres se repelen entre sí o con una negativa."),
      ("Con esas mismas varillas, ¿qué se puede asegurar sobre S?", "Que es positiva o neutra", "Se atrae con P, que es negativa."),
  ],
  context=[("Una persona de ejemplo ve que dos globos frotados con cabello se repelen cuando los acerca. ¿Qué concluye sobre sus cargas?", "Que tienen el mismo signo", "Dos globos frotados de igual modo adquieren cargas iguales.")],
  selfcheck=[("¿Qué prueba una repulsión?", "Que los dos tienen el mismo signo", "Es una conclusión segura."), ("¿Por qué una atracción no es concluyente?", "Porque uno de los objetos puede estar neutro", "Un objeto neutro también es atraído."), ("¿Qué hace un electroscopio?", "Separa láminas cuando recibe carga", "Muestra si hay carga.")],
  open_task=task("Con estos resultados de ejemplo, completa una tabla de «signo seguro» y «posibilidades»: P es negativa. Q se repele con P. R se atrae con P. S se atrae con R, pero no se repele con nadie. Escribe una frase que explique qué puedes asegurar y qué no.", "Q: negativa (seguro). R: positiva o neutra. S: no se puede asegurar porque solo se atrae con R. Puedo asegurar solo lo que muestra una repulsión.", ["Q marcada como segura", "R con dos posibilidades", "explica la diferencia entre repulsión y atracción"], ["tabla y frase"], ["asegurar que R es positiva", "ignorar la posibilidad neutra"], "Pregunta qué prueba adicional distinguiría a R."),
  reinforce="Escribe qué se puede asegurar si dos objetos se repelen.",
  extend="Explica por qué un objeto neutro puede ser atraído por uno cargado.")

L(OA8, 3,
  materials="Este cuaderno y lápiz. Los esquemas se describen con palabras.",
  use="Aprenderé a modelar la electrización por fricción, contacto e inducción con cargas, y a distinguir conductores de aislantes. Sirve para predecir el signo de la carga que queda en cada caso.",
  prior=["Sé que los electrones se transfieren.", "Sé que cargas iguales se repelen."],
  explain=[
      "En la electrización por fricción dos materiales distintos se frotan y los electrones pasan de uno al otro. Un globo frotado con el cabello gana electrones y queda negativo; el cabello pierde y queda positivo. Una varilla de vidrio frotada con seda queda positiva. En todos los casos la carga total se conserva: la que gana uno la pierde el otro.",
      "En la electrización por contacto, un objeto cargado toca a uno neutro y comparte su carga. Quedan ambos con carga del mismo signo. Si son metálicos e idénticos, la reparten por igual. En la inducción no hay contacto: al acercar un objeto cargado a uno neutro, las cargas del neutro se reordenan; si se conecta a tierra un momento, se quita esa conexión y luego se aleja el objeto, el neutro queda cargado con signo contrario.",
      "Los materiales conductores, como los metales, dejan que las cargas se muevan. Los aislantes, como el plástico, el vidrio y la goma, no lo hacen. Por eso un metal en la mano se descarga pasando las cargas por el cuerpo, y un aislante conserva su carga. Todo modelo de cargas simplifica: dibujar signos sobre un objeto no muestra la agitación real de los electrones.",
  ],
  vocab=[("fricción", "frotamiento entre dos materiales"), ("contacto", "transferencia de carga al tocarse dos objetos"), ("inducción", "redistribución de cargas sin tocar el objeto cargado"), ("conductor", "material por donde se mueven las cargas"), ("aislante", "material que no deja mover las cargas")],
  worked=[
      ("Fricción", "Se frota un globo con el cabello y el globo queda negativo. ¿Qué carga queda en el cabello?", ["El globo ganó electrones.", "El cabello los perdió y queda positivo."], "Positiva"),
      ("Contacto", "Una esfera metálica con 8 unidades de carga negativa toca otra idéntica neutra. ¿Cuánta carga queda en cada una?", ["La reparten por igual entre las dos.", "8 ÷ 2 = 4."], "4 unidades negativas en cada una"),
  ],
  mistakes=[
      ("Creer que en la fricción se crea carga.", "Solo se transfiere; la carga total se conserva.", "Suma las cargas antes y después."),
      ("Pensar que en la inducción hay contacto.", "No hay contacto: las cargas del neutro solo se reordenan.", "Recuerda que se acerca sin tocar."),
  ],
  rec=[
      ("¿Qué método de electrización necesita que los objetos se toquen: el contacto o la inducción?", "El contacto", "Se transfiere carga al tocarse."),
      ("¿Un metal es conductor o aislante?", "Conductor", "Las cargas se mueven por él."),
      ("Verdadero o falso: en la fricción la carga total se conserva.", "Verdadero", "Lo que gana uno lo pierde el otro."),
  ],
  und=[
      ("Una varilla de vidrio frotada con seda queda positiva. ¿Qué carga queda en la seda? A) Negativa; B) Positiva.", "A", "La seda recibió los electrones que perdió el vidrio."),
      ("Una esfera negativa toca una neutra. ¿Con qué carga quedan ambas? A) Negativa; B) Positiva.", "A", "Comparten electrones sobrantes."),
      ("En la inducción, ¿qué ocurre en el objeto neutro al acercarle uno cargado?", "Sus cargas se reordenan", "No hay contacto ni transferencia al comienzo."),
  ],
  app=[
      arith("Una esfera metálica tiene 12 unidades de carga negativa y toca a otra idéntica neutra. ¿Cuántas unidades quedan en cada una?", "12//2", "Se reparte por igual entre dos."),
      ("Un globo gana 5 unidades de carga negativa al frotarse con el cabello. ¿Cuántas unidades de carga positiva quedan en el cabello?", "5", "El cabello pierde los mismos electrones que gana el globo; la carga total se conserva."),
      ("Tres objetos: plástico, cobre, goma. ¿Cuántos son aislantes?", "2", "El plástico y la goma son aislantes; el cobre es conductor."),
  ],
  rea=[
      ("Un estudiante dice: «Al frotar, el globo crea electrones». ¿Qué corrección haces? A) Los electrones pasan del cabello al globo; no se crean; B) Los protones pasan al globo.", "A", "La carga se conserva."),
      ("Una barra metálica sostenida con la mano se descarga rápido, pero una de plástico no. ¿Por qué? Responde en una frase.", "Porque el metal conduce las cargas a través de la mano y el plástico las retiene", "El plástico es aislante."),
  ],
  cha=[
      ("Una varilla negativa se acerca, sin tocar, a una esfera metálica neutra aislada. ¿Qué ocurre con las cargas de la esfera? A) Las negativas se alejan de la varilla y las positivas quedan cerca; B) Las positivas se alejan.", "A", "Los electrones son repelidos por la varilla negativa."),
      ("Se conecta la esfera a tierra un instante, se retira la conexión y luego se aleja la varilla. ¿Con qué carga queda la esfera? A) Positiva; B) Negativa.", "A", "Perdió electrones por la conexión a tierra."),
  ],
  context=[("Una persona de ejemplo peina su cabello seco con un peine plástico y ve que los pelos se levantan. ¿Qué método de electrización ocurrió?", "Fricción", "El peine y el cabello se frotaron.")],
  selfcheck=[("¿Qué es la electrización por fricción?", "Transferencia de electrones al frotar dos materiales", "Uno queda positivo y el otro negativo."), ("¿Qué diferencia hay entre conductor y aislante?", "El conductor deja mover las cargas y el aislante no", "Por eso el metal se descarga."), ("¿Qué se conserva al electrizar?", "La carga total", "No se crea ni se destruye.")],
  open_task=task("Haz una tabla con los tres métodos (fricción, contacto, inducción). En cada fila escribe: si hay que tocar los objetos, qué carga queda en cada objeto y un ejemplo de la vida diaria. Termina con una frase sobre la conservación de la carga.", "Fricción: sí se frotan; uno queda positivo y el otro negativo; globo y cabello. Contacto: sí se tocan; ambos con el mismo signo; esfera cargada que toca una neutra. Inducción: no se toca; el neutro queda con signo contrario si se conecta a tierra; papelitos atraídos. La carga total se conserva.", ["tres filas completas", "carga correcta en cada caso", "frase de conservación"], ["tabla y frase"], ["decir que en la inducción se toca", "olvidar la conservación"], "Pregunta qué falla si el material es aislante."),
  reinforce="Escribe qué método de electrización ocurre cuando frotas un globo con el cabello.",
  extend="Explica por qué la carga se conserva cuando dos objetos se frotan.")

L(OA8, 4,
  materials="Este cuaderno y lápiz. Todos los datos son de ejemplo.",
  use="Aprenderé a relacionar la fuerza eléctrica con la distancia, la cantidad de carga y la humedad. Sirve para planificar experimentos y leer tablas sobre interacciones eléctricas.",
  prior=["Sé qué es la fuerza eléctrica.", "Sé calcular promedios y diferencias."],
  explain=[
      "La fuerza eléctrica entre dos cargas depende de dos variables. Mientras mayores son las cargas, mayor es la fuerza. Mientras mayor es la distancia, menor es la fuerza: si se acercan, la fuerza aumenta. Esta es una relación inversa con la distancia. Se puede comprobar con un globo que atrae un hilo liviano: a menor distancia, el hilo se inclina más.",
      "Otra variable es la humedad del aire. Con aire húmedo, las cargas se escapan por la capa de agua en la superficie de los objetos, y la electrización dura poco. En días secos, la electricidad estática es más notoria. Datos de ejemplo: un globo atrae 10 papelitos en un día seco y 2 en un día húmedo.",
      "Un buen experimento cambia una sola variable. Por ejemplo, para estudiar la distancia se mantiene igual el globo, el frotado y los papelitos. Se repite cada medición y se calcula el promedio. Una relación se describe con palabras (aumenta o disminuye) y se declara una limitación, como que las mediciones se hicieron en un solo día.",
  ],
  vocab=[("fuerza eléctrica", "atracción o repulsión entre cargas"), ("relación inversa", "cuando una variable aumenta, la otra disminuye"), ("humedad", "cantidad de vapor de agua en el aire"), ("variable controlada", "la que se mantiene igual para que la prueba sea justa"), ("promedio", "suma de resultados dividida por el número de mediciones")],
  worked=[
      ("Distancia y fuerza", "Un hilo se inclina 30° cuando el globo está a 5 cm y 10° cuando está a 15 cm. ¿Qué relación hay entre la distancia y la inclinación?", ["A mayor distancia, menor inclinación.", "Es una relación inversa."], "A mayor distancia, menor fuerza y menos inclinación"),
      ("Promedio", "Un globo atrae 9, 11 y 10 papelitos en tres intentos. ¿Cuál es el promedio?", ["Sumo: 9 + 11 + 10 = 30.", "30 ÷ 3 = 10."], "10 papelitos"),
  ],
  mistakes=[
      ("Pensar que la fuerza eléctrica aumenta con la distancia.", "Disminuye cuando se alejan las cargas.", "Imagina un imán o un globo cerca y lejos."),
      ("Concluir con una sola medición.", "Una sola medición puede tener error.", "Repite y promedia."),
  ],
  rec=[
      ("Si dos cargas se acercan, la fuerza eléctrica ¿aumenta o disminuye?", "Aumenta", "A menor distancia, mayor fuerza."),
      ("En un día húmedo, la electricidad estática ¿se nota más o menos?", "Se nota menos", "Las cargas se escapan por la humedad."),
      ("Verdadero o falso: a mayor carga, mayor fuerza eléctrica.", "Verdadero", "La fuerza crece con las cargas."),
  ],
  und=[
      ("¿Por qué la electrización dura poco en un día húmedo? A) Las cargas se escapan por el agua de la superficie; B) El aire crea nuevos electrones.", "A", "La capa de agua conduce las cargas."),
      ("¿Qué variable se debe mantener igual para estudiar el efecto de la distancia? A) El globo y el frotado; B) La distancia.", "A", "La distancia es la que se cambia."),
      ("Si se triplica la distancia entre dos cargas, ¿qué ocurre con la fuerza?", "Disminuye", "La fuerza es menor cuando están más lejos."),
  ],
  app=[
      arith("Datos de ejemplo: un globo atrae 12 papelitos en un día seco y 3 en un día húmedo. ¿Cuántos papelitos más atrae en el día seco?", "12-3", "Se resta el menor al mayor."),
      arith("Tres intentos de ejemplo con el mismo globo dieron 8, 12 y 7 papelitos. ¿Cuál es el promedio?", "(8+12+7)//3", "Se suman y se divide por 3."),
      ("Un hilo se inclina 40° con el globo a 4 cm y 20° a 8 cm. ¿Qué pasa con la inclinación al duplicar la distancia? A) Disminuye; B) Aumenta.", "A", "A mayor distancia, menor fuerza."),
  ],
  rea=[
      ("Un estudiante mide la distancia con un globo nuevo y otro frotado menos tiempo. ¿Qué falla tiene? A) Cambió dos variables a la vez; B) Usó un hilo.", "A", "Cambió distancia y carga."),
      ("En un experimento de ejemplo, la electricidad estática fue mayor en la mañana seca que en la tarde húmeda. ¿Qué otra variable debería registrarse? A) La humedad del aire; B) El color del globo.", "A", "La humedad cambia la persistencia de las cargas."),
  ],
  cha=[
      ("Datos de ejemplo de papelitos atraídos según la distancia: 2 cm, 10; 4 cm, 6; 6 cm, 3; 8 cm, 1. ¿Qué relación se observa? A) A mayor distancia, menos papelitos; B) A mayor distancia, más papelitos.", "A", "Los valores bajan al aumentar la distancia."),
      arith("Con esos datos de ejemplo, ¿cuántos papelitos menos se atraen a 8 cm que a 2 cm?", "10-1", "Se resta el valor a 8 cm al valor a 2 cm."),
  ],
  context=[("Un curso de ejemplo nota que en invierno, con aire seco en la sala, los chasquidos al sacarse un suéter son más frecuentes que en un día lluvioso. ¿Qué variable explica la diferencia?", "La humedad del aire", "Con humedad se descargan las cargas.")],
  selfcheck=[("¿Cómo cambia la fuerza eléctrica con la distancia?", "Disminuye al aumentar la distancia", "Es una relación inversa."), ("¿Por qué la humedad reduce la electricidad estática?", "Porque las cargas se escapan por el agua", "La superficie conduce un poco."), ("¿Por qué se repite una medición?", "Para reducir errores y calcular un promedio", "Un solo dato puede fallar.")],
  open_task=task("Planifica un experimento seguro para ver cómo cambia la inclinación de un hilo liviano con la distancia a un globo frotado. Escribe la pregunta, la variable que cambias, la que mides, tres variables controladas, cuántas repeticiones harás y una tabla vacía para tres distancias.", "Pregunta: ¿Cambia la inclinación del hilo con la distancia al globo? Cambio: distancia (4, 8 y 12 cm). Mido: ángulo de inclinación. Controlo: globo, frotado y hilo. Repito 3 veces. Tabla con columnas distancia, intento 1, 2, 3 y promedio. Seguridad: sin enchufes.", ["pregunta y variables claras", "tres controladas", "tabla con repeticiones"], ["plan y tabla"], ["cambiar dos variables", "no repetir"], "Pregunta cómo cambiaría el plan en un día húmedo."),
  reinforce="Escribe qué pasa con la fuerza eléctrica al acercar dos cargas.",
  extend="Explica por qué se debe registrar la humedad en un experimento de electricidad estática.")

L(OA8, 5,
  materials="Este cuaderno y lápiz. Los ejemplos están descritos con palabras.",
  use="Aprenderé a explicar mecanismos de la electricidad estática: la conservación de la carga, el electroscopio y el rayo. Sirve para unir las ideas de fuerza eléctrica y electrización con fenómenos de la naturaleza.",
  prior=["Sé qué son la fricción, el contacto y la inducción.", "Sé que cargas iguales se repelen."],
  explain=[
      "Un mecanismo describe paso a paso cómo ocurre un fenómeno. Electroscopio: se acerca una varilla negativa a la esfera metálica; los electrones de las láminas son repelidos hacia abajo; las láminas quedan negativas y se separan por repulsión. Si se toca la esfera con la varilla, parte de los electrones pasa al electroscopio y las láminas quedan separadas aunque se retire la varilla.",
      "Un rayo es una descarga eléctrica entre una nube y el suelo, o entre nubes. En una tormenta, el movimiento de partículas de hielo y agua dentro de la nube hace que se separen cargas: arriba predominan las positivas y abajo las negativas. Cuando la diferencia es muy grande, el aire, que es aislante, deja pasar una descarga. El trueno es el sonido de esa descarga.",
      "El patrón común es que las cargas se separan por fricción o inducción, y cuando hay un camino conductor se descargan. Por eso un objeto metálico puntiagudo y conectado a tierra, como un pararrayos, ofrece un camino seguro. Explicar un mecanismo significa nombrar el estímulo, el movimiento de cargas y el efecto observable.",
  ],
  vocab=[("descarga eléctrica", "paso brusco de cargas entre dos objetos"), ("rayo", "descarga eléctrica entre una nube y el suelo o entre nubes"), ("pararrayos", "barra metálica conectada a tierra que ofrece un camino seguro a la descarga"), ("tierra", "conexión que permite que las cargas se repartan en el suelo"), ("trueno", "sonido de la descarga de un rayo")],
  worked=[
      ("Por qué se separan las láminas", "Se toca un electroscopio con una varilla negativa. ¿Por qué se separan sus láminas?", ["Las láminas reciben electrones.", "Quedan con carga negativa y se repelen."], "Porque quedan con el mismo signo y se repelen"),
      ("Camino de la descarga", "En una tormenta, ¿por qué un pararrayos protege un edificio?", ["Es metálico y conectado a tierra.", "La descarga sigue ese camino conductor."], "Porque ofrece un camino conductor seguro hasta la tierra"),
  ],
  mistakes=[
      ("Creer que el rayo es una corriente que sale de la tierra hacia la nube solamente.", "Es una descarga entre cargas separadas; puede ir en ambos sentidos.", "Describe la separación de cargas primero."),
      ("Pensar que el aire siempre conduce la electricidad.", "El aire es aislante; solo deja pasar la descarga cuando la diferencia es muy grande.", "Recuerda el papel del aislante."),
  ],
  rec=[
      ("¿Qué es el trueno: el sonido de un rayo o un tipo de nube?", "El sonido de un rayo", "Es el estruendo de la descarga."),
      ("¿Qué protege a un edificio de un rayo: un pararrayos o una ventana?", "Un pararrayos", "Ofrece un camino seguro a tierra."),
      ("Verdadero o falso: el aire normalmente es aislante.", "Verdadero", "Solo deja pasar una descarga con diferencias muy grandes."),
  ],
  und=[
      ("¿Por qué se separan las láminas de un electroscopio cargado? A) Se repelen por tener el mismo signo; B) Se atraen por tener signos distintos.", "A", "Las dos reciben carga igual."),
      ("En una nube de tormenta, ¿qué ocurre con las cargas? A) Se separan en zonas; B) Desaparecen.", "A", "Esa separación produce una gran diferencia entre zonas."),
      ("¿Por qué el pararrayos está conectado a tierra?", "Para que las cargas se descarguen en el suelo", "Así la descarga no pasa por el edificio."),
  ],
  app=[
      ("Un electroscopio con las láminas cerradas se toca con una varilla positiva y las láminas se abren. ¿Qué carga tienen las láminas? A) Positiva; B) Negativa.", "A", "Reciben el signo de la varilla."),
      arith("Un electroscopio recibe 6 unidades de carga negativa de una varilla. Si las dos láminas la reparten por igual, ¿cuántas unidades tiene cada una?", "6//2", "Se divide por dos."),
      ("Cuatro objetos: una barra de cobre, un trozo de madera seca, un plástico y una cuchara de acero. ¿Cuántos son conductores?", "2", "El cobre y el acero son metales conductores; la madera seca y el plástico son aislantes."),
  ],
  rea=[
      ("Alguien dice: «Un rayo cae porque el cielo se enoja». ¿Qué explicación científica corresponde? A) Se separan cargas en la nube y ocurre una descarga; B) Las nubes chocan como piedras.", "A", "Es un fenómeno de cargas eléctricas."),
      ("¿Por qué un electroscopio puede mantener sus láminas abiertas aunque se retire la varilla, si hubo contacto?", "Porque recibió electrones y quedó cargado", "Hubo transferencia de carga."),
  ],
  cha=[
      ("Un objeto conductor conectado a tierra se acerca a una esfera con carga negativa. ¿Hacia dónde se mueven los electrones del conductor? A) Hacia la tierra, lejos de la esfera; B) Hacia la esfera.", "A", "Son repelidos por la carga negativa."),
      ("En una tormenta, una persona se queda de pie bajo un árbol aislado. Explica en una frase por qué es peligroso.", "Porque el árbol puede ser el camino de la descarga", "Es el objeto más alto y puede conducir el rayo."),
  ],
  context=[("Una persona ve un relámpago y cuenta 6 segundos hasta oír el trueno. El sonido recorre unos 340 metros por segundo. ¿A cuántos metros ocurrió la descarga aproximadamente?", "2.040", "6 × 340 = 2.040 metros.", "6*340")],
  selfcheck=[("¿Cómo se separan las láminas de un electroscopio?", "Reciben cargas del mismo signo y se repelen", "La repulsión las separa."), ("¿Qué es un rayo?", "Una descarga eléctrica entre cargas separadas", "Puede ser entre nube y suelo."), ("¿Para qué sirve un pararrayos?", "Para ofrecer un camino seguro a tierra", "Evita daños al edificio.")],
  open_task=task("Escribe en cinco oraciones el mecanismo de un rayo, con las palabras: cargas, separación, aire aislante, descarga y trueno. Agrega una oración con una conducta segura durante una tormenta.", "En una nube de tormenta se separan cargas. Arriba hay positivas y abajo negativas. El aire es aislante, pero cuando la diferencia es muy grande permite una descarga. Esa descarga es el rayo y el sonido es el trueno. Conducta segura: refugiarse en un lugar cerrado y alejarse de árboles aislados y del agua.", ["usa las cinco palabras", "orden lógico", "conducta segura"], ["texto de cinco oraciones"], ["decir que el aire es conductor siempre", "no incluir seguridad"], "Pregunta qué cambiaría si no hubiera una nube."),
  reinforce="Escribe una conducta segura durante una tormenta eléctrica.",
  extend="Explica con tus palabras por qué el aire deja pasar una descarga solo a veces.")

L(OA8, 6,
  materials="Este cuaderno y lápiz. Nunca pruebes riesgos eléctricos ni toques enchufes, cables ni aparatos conectados a la red.",
  use="Aprenderé a evaluar los límites de los experimentos, los riesgos de la electricidad estática en la vida cotidiana y las soluciones posibles. Sirve para tomar decisiones seguras con evidencia.",
  prior=["Sé qué es la electricidad estática y cómo se produce.", "Sé qué es un conductor y un aislante."],
  explain=[
      "La electricidad estática tiene riesgos cotidianos. Una descarga puede dañar componentes electrónicos delicados. Cerca de combustibles o de polvos finos, como harina o polvo de granos, una chispa puede iniciar un incendio. En las tormentas, los rayos son un riesgo para las personas y las construcciones. Casi siempre la descarga entre dos personas es pequeña y no peligrosa, pero molesta.",
      "Hay soluciones concretas. Para proteger equipos se usan pulseras antiestáticas y bolsas especiales. Cerca de combustibles se conectan los recipientes a tierra y se evita descargar chispas. Los pararrayos protegen los edificios. Aumentar la humedad del aire ayuda a que las cargas no se acumulen. En una tormenta, la conducta segura es refugiarse en un lugar cerrado y alejarse del agua y de árboles aislados.",
      "Evaluar un experimento incluye declarar sus límites: pocas repeticiones, humedad no controlada, materiales distintos. También se evalúa si una solución es adecuada: debe reducir el riesgo, ser posible y no crear otro peligro. Un buen informe dice qué se midió, qué se concluyó y qué no se puede asegurar.",
  ],
  vocab=[("riesgo", "posibilidad de daño"), ("conexión a tierra", "camino conductor que lleva las cargas al suelo"), ("pulsera antiestática", "accesorio que descarga la electricidad estática del cuerpo"), ("medida preventiva", "acción para reducir un riesgo"), ("límite del experimento", "aspecto que impide generalizar el resultado")],
  worked=[
      ("Elegir una solución", "En una fábrica de harina hay riesgo de chispa por estática. ¿Cuál solución es más adecuada: aumentar la humedad y conectar los equipos a tierra, o poner una luz más fuerte?", ["La causa es la acumulación de cargas.", "La humedad y la conexión a tierra reducen esa acumulación."], "Aumentar la humedad y conectar a tierra"),
      ("Límite de un experimento", "Un grupo mide papelitos atraídos solo una vez, un día lluvioso. ¿Qué límites tiene su conclusión?", ["Hay una sola medición.", "No controló la humedad."], "Una sola medición y humedad no controlada"),
  ],
  mistakes=[
      ("Pensar que cualquier chispa es muy peligrosa.", "La mayoría de las descargas cotidianas son pequeñas, pero cerca de combustibles son peligrosas.", "Evalúa el contexto."),
      ("Proponer una solución que crea otro riesgo.", "Una buena solución debe ser segura.", "Revisa que no añada un peligro nuevo."),
  ],
  rec=[
      ("¿Dónde es más peligrosa una chispa: cerca de un combustible o en una sala de clases?", "Cerca de un combustible", "Puede iniciar un incendio."),
      ("¿Qué protege un edificio de los rayos: un pararrayos o un ventilador?", "Un pararrayos", "Lleva la descarga a tierra."),
      ("Verdadero o falso: la humedad del aire ayuda a reducir la acumulación de cargas.", "Verdadero", "Las cargas se escapan por el agua de la superficie."),
  ],
  und=[
      ("¿Para qué sirve una pulsera antiestática? A) Para descargar la electricidad estática del cuerpo; B) Para cargar el cuerpo.", "A", "Protege los componentes electrónicos."),
      ("En una tormenta, ¿cuál conducta es más segura? A) Refugiarse en un lugar cerrado; B) Pararse bajo un árbol aislado.", "A", "El árbol puede atraer la descarga."),
      ("¿Qué debe cumplir una buena solución a un riesgo?", "Reducir el riesgo, ser posible y no crear otro peligro", "Se evalúa antes de aplicarla."),
  ],
  app=[
      ("Tres situaciones: (1) cargar combustible, (2) peinarse, (3) tocar la perilla de una puerta en invierno. ¿En cuántas el riesgo es mayor por la cercanía de un material inflamable?", "1", "Solo en la carga de combustible."),
      ("Un equipo electrónico delicado se daña por descargas. ¿Qué medida es más adecuada? A) Usar una pulsera antiestática y una superficie conectada a tierra; B) Frotarlo con un paño de lana.", "A", "Evita acumular cargas."),
      arith("Datos de ejemplo: un taller registró 12 descargas peligrosas antes de usar una conexión a tierra y 3 después. ¿Cuántas descargas menos hubo?", "12-3", "Se resta el valor posterior al anterior."),
  ],
  rea=[
      ("Un grupo concluye que la humedad no afecta nada, porque midió una sola vez y en un día húmedo. ¿Qué falla tiene? A) Con una sola medición y un solo día no se puede generalizar; B) La humedad no existe.", "A", "La evidencia es insuficiente."),
      ("Una persona propone mojar un enchufe para quitar la estática. ¿Por qué es peligrosa esa solución? Responde en una frase.", "Porque el agua y la electricidad de la red pueden causar una descarga grave", "Crea un riesgo mayor."),
  ],
  cha=[
      ("Tres soluciones para un laboratorio: S1 usar bolsas antiestáticas; S2 cerrar las ventanas; S3 pintar las paredes. ¿Cuál reduce mejor la estática en los equipos? Escribe S1, S2 o S3.", "S1", "Las bolsas antiestáticas evitan acumular carga."),
      ("Un informe dice: «La solución funcionó». ¿Qué dato falta para evaluarlo? A) Cuántas descargas hubo antes y después; B) El color de las paredes.", "A", "Hay que comparar con una medición."),
  ],
  context=[("En un taller de ejemplo hay polvo fino de harina en el aire y un trabajador siente chispas al tocar una máquina. ¿Qué medida inmediata es más segura? A) Detener la actividad y avisar al encargado para conectar a tierra; B) Seguir trabajando.", "A", "Hay riesgo de incendio por el polvo y las chispas.")],
  selfcheck=[("¿Qué riesgo tiene una chispa cerca de combustibles?", "Puede iniciar un incendio", "Es el riesgo más serio."), ("¿Qué conducta es segura en una tormenta?", "Refugiarse en un lugar cerrado", "Evita ser el camino del rayo."), ("¿Cuándo es adecuada una solución?", "Cuando reduce el riesgo y no crea otro peligro", "Debe ser posible.")],
  open_task=task("Elige un riesgo de la electricidad estática: (a) dañar un computador, (b) incendio por una chispa cerca de combustible, (c) tormenta eléctrica. Explica en cinco oraciones el riesgo, una solución, una limitación de esa solución y una conducta segura.", "(b) Una chispa cerca de combustible puede causar un incendio. Solución: conectar los recipientes a tierra. Limitación: requiere instalación correcta y mantención. Conducta segura: no usar llamas cerca del combustible, no subir y bajar del auto durante la carga y avisar a un adulto si hay chispas.", ["riesgo bien explicado", "solución coherente", "una limitación y una conducta segura"], ["texto de cinco oraciones"], ["proponer una solución peligrosa", "no mencionar limitaciones"], "Pregunta quién debería encargarse de la solución."),
  reinforce="Escribe una medida para proteger un equipo electrónico de la electricidad estática.",
  extend="Explica cuándo una solución a un riesgo deja de ser adecuada.")

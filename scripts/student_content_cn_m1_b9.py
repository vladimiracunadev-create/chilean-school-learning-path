"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 19 (compuestos binarios y ternarios, enlace y nomenclatura)."""
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


OA = "CN1M OA 19"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Las propiedades de las sustancias se dan como datos escritos; no se hacen pruebas eléctricas en casa.",
  use="Aprenderé cómo las fuerzas eléctricas entre partículas explican el enlace iónico y el covalente. Sirve para entender por qué unas sustancias, como la sal, funden a temperaturas muy altas.",
  prior=["Sé que el átomo tiene protones, neutrones y electrones.", "Sé que las cargas opuestas se atraen y las iguales se repelen."],
  explain=[
      "Un átomo neutro tiene el mismo número de protones, con carga positiva, y de electrones, con carga negativa. Los electrones de la última capa se llaman electrones de valencia y son los que participan en los enlaces. Muchos átomos tienden a quedar con 8 electrones en su última capa; el hidrógeno, con 2. Un ion es un átomo con carga porque ganó o perdió electrones: el catión tiene carga positiva y el anión, negativa.",
      "En el enlace iónico, un metal cede electrones y un no metal los gana. Así se forman cationes y aniones que se atraen por fuerzas eléctricas. Ejemplo: el sodio (1 electrón de valencia) cede un electrón y se convierte en Na+; el cloro (7 electrones de valencia) lo gana y se convierte en Cl−. Los iones forman un cristal: la sal NaCl, un sólido de alto punto de fusión (801 °C) que conduce la electricidad cuando está disuelto en agua, porque los iones se mueven libres.",
      "En el enlace covalente, dos no metales comparten pares de electrones. Forma moléculas, como H2O y CO2. Estas sustancias suelen tener puntos de fusión bajos y no conducen la electricidad disueltas. El azúcar, por ejemplo, funde a unos 186 °C y su solución no conduce. Estas diferencias se explican por el tipo de enlace y son la evidencia que se usa para clasificar sustancias.",
  ],
  vocab=[("electrón de valencia", "electrón de la última capa, que participa en los enlaces"), ("ion", "átomo con carga eléctrica por haber ganado o perdido electrones"), ("catión", "ion con carga positiva"), ("anión", "ion con carga negativa"), ("enlace iónico", "unión entre iones de carga opuesta por atracción eléctrica"), ("enlace covalente", "unión entre átomos que comparten electrones")],
  worked=[
      ("Formación de un ion", "Un átomo de sodio tiene 1 electrón de valencia y lo cede. ¿Qué ion forma?", ["Pierde un electrón, que tiene carga negativa.", "Queda con una carga positiva más que negativas."], "Catión Na+"),
      ("Tipo de enlace", "El magnesio es un metal y el oxígeno un no metal. ¿Qué enlace forman?", ["Un metal cede electrones y un no metal los gana.", "Se forman iones que se atraen."], "Enlace iónico"),
  ],
  mistakes=[
      ("Creer que Na+ y Cl− son átomos neutros.", "Son iones con carga porque ganaron o perdieron electrones.", "Revisa si el número de electrones es igual al de protones."),
      ("Pensar que en un enlace iónico los electrones se comparten.", "En el iónico se transfieren; en el covalente se comparten.", "Pregunta si se unen metal con no metal o dos no metales."),
  ],
  rec=[
      ("¿Qué carga tiene un protón?", "Positiva", "Los protones tienen carga positiva."),
      ("Un ion con carga positiva se llama ______ (catión o anión).", "Catión", "Perdió electrones y quedó positivo."),
      ("Verdadero o falso: en el enlace iónico se transfieren electrones.", "Verdadero", "Un metal los cede y un no metal los gana."),
  ],
  und=[
      ("¿Qué fuerza mantiene unidos a los iones Na+ y Cl−?", "La atracción eléctrica entre cargas opuestas", "Cargas contrarias se atraen."),
      ("Un átomo de cloro gana 1 electrón. ¿Qué carga tiene el ion que se forma? A) 1− B) 1+", "A", "Ganó una carga negativa más."),
      ("Dos no metales que comparten electrones forman un enlace:", "Covalente", "Comparten pares de electrones."),
  ],
  app=[
      arith("Un átomo de oxígeno tiene 6 electrones de valencia y gana 2. ¿Cuántos electrones tiene en su última capa?", "6+2", "Se suman los electrones que gana.", " electrones"),
      arith("Un átomo de calcio tiene 20 electrones. Si pierde 2, ¿cuántos electrones tiene el ion?", "20-2", "Se restan los electrones perdidos.", " electrones"),
      ("Sustancia A: funde a 801 °C y conduce en agua. Sustancia B: funde a 186 °C y no conduce en agua. ¿Cuál tiene enlace iónico?", "La A", "Alto punto de fusión y conducción en agua indican iones."),
  ],
  rea=[
      ("Un estudiante dice que Na+ y Cl− son átomos neutros. ¿Qué respuesta es correcta? A) No: tienen carga porque ganaron o perdieron electrones B) Sí: las cargas se compensan dentro de cada átomo", "A", "Son iones, no átomos neutros."),
      ("El NaCl sólido no conduce la corriente, pero disuelto sí. ¿Por qué? A) En el agua los iones quedan libres para moverse B) El agua agrega electrones a la sal", "A", "Los iones libres transportan la carga."),
  ],
  cha=[
      ("En un cristal de sal hay el mismo número de iones Na+ y Cl−. ¿Por qué el cristal es neutro?", "Porque las cargas positivas y negativas se compensan", "Cada carga positiva se anula con una negativa."),
      ("Un metal y un no metal se unen. ¿Qué enlace esperas?", "Iónico", "El metal cede electrones y el no metal los gana."),
  ],
  context=[arith("La sal de mesa funde a 801 °C. Un cocinero la calienta a 200 °C en una sartén. ¿Cuántos grados le faltan para fundirse?", "801-200", "Se resta la temperatura alcanzada al punto de fusión: la sal no se funde.", " °C")],
  selfcheck=[("¿Qué es un ion?", "Un átomo con carga por haber ganado o perdido electrones", "Cambia su número de electrones."), ("¿Qué diferencia hay entre el enlace iónico y el covalente?", "En el iónico se transfieren electrones y en el covalente se comparten", "Cambia el tipo de átomos que se unen."), ("¿Qué propiedades suelen tener los compuestos iónicos?", "Alto punto de fusión y conducen disueltos en agua", "Se explican por los iones.")],
  open_task=task("Datos de ejemplo: sal NaCl, funde a 801 °C y conduce en agua; azúcar, funde a 186 °C y no conduce en agua; cloruro de potasio KCl, funde a 770 °C y conduce en agua; cera de vela, funde a unos 60 °C y no conduce en agua. Clasifica cada sustancia como iónica o molecular, explica cada decisión con el tipo de partículas y dibuja un esquema de Na+ y Cl− que se atraen.", "NaCl y KCl: iónicas, altos puntos de fusión y conducen por tener iones libres en agua. Azúcar y cera: moleculares, puntos de fusión bajos y sin iones. Esquema: círculos con + y − alternados y flechas de atracción.", ["cuatro clasificaciones", "explicación con iones o moléculas", "esquema de atracción entre cargas"], ["tabla y dibujo"], ["clasificar KCl como molecular", "no explicar con las partículas"], "Pregunta cómo cambiaría la conducción si la sal no se disolviera."),
  reinforce="Escribe el ion que forma el sodio y el ion que forma el cloro.",
  extend="Explica por qué la sal se mantiene sólida a temperaturas donde el agua ya hirvió.")

L(OA, 2,
  materials="Este cuaderno y lápiz. Las cargas de los iones están escritas en la explicación y en los ejercicios.",
  use="Aprenderé a formar la fórmula y a nombrar compuestos binarios, es decir, de dos elementos. Sirve para leer y escribir fórmulas como NaCl, MgO y Al2O3.",
  prior=["Sé qué es un ion y su carga.", "Sé que un compuesto iónico es eléctricamente neutro."],
  explain=[
      "Un compuesto binario está formado por dos elementos. Iones frecuentes: Li+, Na+ y K+ (carga 1+); Mg2+ y Ca2+ (2+); Al3+ (3+); F−, Cl− y Br− (1−); O2− y S2− (2−). Para escribir la fórmula, la suma de las cargas debe ser cero. Un método es cruzar las cargas: el número de la carga de un ion pasa a ser el subíndice del otro, sin el signo, y luego se simplifica. Ejemplo: Ca2+ y Cl− dan CaCl2. Ejemplo: Al3+ y O2− dan Al2O3. Ejemplo: Mg2+ y O2− dan MgO, porque 2 y 2 se simplifican.",
      "Para nombrar sales binarias se dice el nombre del no metal terminado en -uro y el del metal: NaCl es cloruro de sodio, CaS es sulfuro de calcio y KBr es bromuro de potasio. Los óxidos se llaman óxido de y el metal: MgO es óxido de magnesio y Al2O3 es óxido de aluminio. Cuando el metal tiene más de una carga, la nomenclatura Stock indica la carga con un número romano entre paréntesis: FeO es óxido de hierro (II) y Fe2O3 es óxido de hierro (III).",
      "Entre no metales se usa la nomenclatura sistemática con prefijos que indican cuántos átomos hay: mono-, di-, tri-, tetra-, penta-. Así, CO es monóxido de carbono, CO2 es dióxido de carbono y SO3 es trióxido de azufre. El prefijo mono- del primer elemento se omite.",
  ],
  vocab=[("compuesto binario", "compuesto formado por dos elementos"), ("cruzar las cargas", "método para obtener los subíndices a partir de las cargas de los iones"), ("nomenclatura Stock", "sistema que indica con números romanos la carga del metal"), ("nomenclatura sistemática", "sistema que usa prefijos como mono-, di- y tri- para el número de átomos"), ("sal binaria", "compuesto de un metal y un no metal, como NaCl"), ("óxido", "compuesto binario del oxígeno con otro elemento")],
  worked=[
      ("Formular por cruce de cargas", "Escribe la fórmula del compuesto de Ca2+ y Cl−.", ["La carga 2 de Ca pasa como subíndice de Cl.", "La carga 1 de Cl pasa como subíndice de Ca, que no se escribe.", "Verifico: +2 y 2 × (−1) = −2, suma cero."], "CaCl2"),
      ("Nomenclatura Stock", "Nombra Fe2O3.", ["Hay 3 oxígenos con carga 2−: 3 × (−2) = −6.", "Los 2 hierros compensan +6, es decir, 3+ cada uno."], "Óxido de hierro (III)"),
  ],
  mistakes=[
      ("Dejar los subíndices sin simplificar, como Mg2O2.", "La fórmula debe tener la relación más simple: MgO.", "Simplifica los subíndices."),
      ("Escribir las cargas como subíndices con signo.", "Los subíndices son números positivos y las cargas se verifican aparte.", "Cruza los números sin signo y verifica la suma."),
  ],
  rec=[
      ("¿Cuántos elementos tiene un compuesto binario?", "Dos", "Binario significa dos."),
      ("¿Cuál es el nombre de NaCl?", "Cloruro de sodio", "El no metal termina en -uro."),
      ("Verdadero o falso: la suma de las cargas de un compuesto iónico debe ser cero.", "Verdadero", "El compuesto es neutro."),
  ],
  und=[
      ("¿Cuál es la fórmula del óxido de magnesio, formado por Mg2+ y O2−?", "MgO", "Las cargas 2+ y 2− se compensan 1 a 1."),
      ("¿Cuál es el nombre de SO3?", "Trióxido de azufre", "El prefijo tri- indica 3 átomos de oxígeno."),
      ("En óxido de hierro (III), ¿qué indica el número romano?", "La carga del hierro, 3+", "Es la nomenclatura Stock."),
  ],
  app=[
      ("¿Cuál es la fórmula del bromuro de calcio, formado por Ca2+ y Br−?", "CaBr2", "Se necesitan 2 Br− para compensar un Ca2+."),
      ("¿Cuál es la fórmula del cloruro de aluminio, formado por Al3+ y Cl−?", "AlCl3", "Se necesitan 3 iones Cl− para compensar un Al3+."),
      ("¿Cuál es el nombre de K2S, formado por K+ y S2−?", "Sulfuro de potasio", "El no metal termina en -uro."),
  ],
  rea=[
      ("Un estudiante escribe NaCl2 para el cloruro de sodio. ¿Cuál es el error? A) Na+ y Cl− se compensan 1 a 1, la fórmula es NaCl B) Está bien escrita", "A", "Las cargas ya son iguales."),
      ("FeO y Fe2O3 tienen nombres distintos porque: A) el hierro tiene carga 2+ en uno y 3+ en el otro B) el oxígeno tiene distinta carga en cada uno", "A", "El oxígeno siempre tiene carga 2− en los óxidos."),
  ],
  cha=[
      arith("En Al2O3 hay 2 iones Al3+ y 3 iones O2−. ¿Cuál es la carga total del compuesto?", "2*3-3*2", "La carga positiva total es 6 y la negativa total es 6.", ""),
      ("¿Cuál es el nombre de Cu2O, sabiendo que el cobre tiene carga 1+?", "Óxido de cobre (I)", "El número romano indica la carga del cobre."),
  ],
  context=[arith("El cloruro de calcio, CaCl2, se usa para evitar que se forme hielo en los caminos. ¿Cuántos iones cloruro hay en 3 unidades de CaCl2?", "3*2", "Cada unidad tiene 2 iones cloruro.", " iones")],
  selfcheck=[("¿Cómo se obtienen los subíndices cruzando cargas?", "El número de la carga de un ion pasa a ser el subíndice del otro", "Después se simplifica."), ("¿Cuál es el nombre de CO2?", "Dióxido de carbono", "El prefijo di- indica 2 átomos de oxígeno."), ("¿Qué indica la nomenclatura Stock?", "La carga del metal con un número romano", "Se usa cuando el metal tiene más de una carga.")],
  open_task=task("Con los iones Na+, Mg2+, Al3+, Cl− y O2−, escribe la fórmula y el nombre de los cinco compuestos binarios posibles: Na con Cl, Mg con O, Al con O, Mg con Cl y Na con O. Verifica en cada uno que la suma de cargas sea cero.", "NaCl, cloruro de sodio. MgO, óxido de magnesio. Al2O3, óxido de aluminio. MgCl2, cloruro de magnesio. Na2O, óxido de sodio. En cada uno la suma de cargas es cero.", ["cinco fórmulas", "cinco nombres", "verificación de cargas"], ["tabla de cinco filas"], ["no simplificar", "olvidar verificar la suma de cargas"], "Pregunta qué compuesto se formaría con K+ y S2−."),
  reinforce="Escribe la fórmula del cloruro de magnesio.",
  extend="Explica por qué el óxido de aluminio necesita 2 átomos de aluminio y 3 de oxígeno.")

L(OA, 3,
  materials="Este cuaderno y lápiz. Los ácidos y las bases solo se estudian con datos; no se manipulan en casa.",
  use="Aprenderé a formular y nombrar compuestos ternarios con iones poliatómicos: hidróxidos, ácidos y sales. Sirve para leer etiquetas como carbonato de calcio o hidróxido de sodio.",
  prior=["Sé formar compuestos binarios cruzando cargas.", "Sé simplificar subíndices."],
  explain=[
      "Un compuesto ternario tiene tres elementos. Muchos contienen iones poliatómicos, que son grupos de átomos unidos que actúan como una unidad con carga: hidróxido, OH− (1−); nitrato, NO3− (1−); sulfato, SO4 2− (2−); carbonato, CO3 2− (2−) y fosfato, PO4 3− (3−). Si se necesita más de uno, se escribe entre paréntesis: Ca(OH)2 tiene 2 iones hidróxido; Al2(SO4)3 tiene 3 iones sulfato.",
      "Hay tres familias. Los hidróxidos se forman con un metal y OH−: NaOH es hidróxido de sodio y Ca(OH)2 es hidróxido de calcio. Los oxoácidos tienen hidrógeno, un no metal y oxígeno: H2SO4 es ácido sulfúrico, HNO3 es ácido nítrico, H2CO3 es ácido carbónico y H3PO4 es ácido fosfórico. Las oxisales se forman con un metal y un ion poliatómico: CaCO3 es carbonato de calcio, Na2SO4 es sulfato de sodio y KNO3 es nitrato de potasio.",
      "Se aplican en la vida diaria: el carbonato de calcio forma conchas y calizas; el ácido carbónico está en las bebidas gaseosas; el nitrato de potasio se usa en fertilizantes, y el salitre que Chile exportó es principalmente nitrato de sodio. Los hidróxidos como el de sodio son corrosivos y están en algunos limpiadores: no se manipulan sin guía, y ante cualquier contacto hay que avisar a una persona adulta.",
  ],
  vocab=[("compuesto ternario", "compuesto formado por tres elementos"), ("ion poliatómico", "grupo de átomos unidos que actúa como un ion"), ("hidróxido", "compuesto de un metal con el ion OH−"), ("oxoácido", "compuesto de hidrógeno, un no metal y oxígeno"), ("oxisal", "compuesto de un metal con un ion poliatómico con oxígeno"), ("paréntesis", "signo que agrupa un ion poliatómico para multiplicarlo por un subíndice")],
  worked=[
      ("Formular un hidróxido", "Escribe la fórmula del compuesto de Ca2+ y OH−.", ["Cruzo las cargas: el subíndice 2 va con OH, que se encierra en paréntesis.", "Queda Ca(OH)2.", "Verifico: +2 y 2 × (−1) = −2."], "Ca(OH)2"),
      ("Nombrar una oxisal", "Nombra Na2SO4.", ["El ion poliatómico es SO4 2−, sulfato.", "El metal es sodio."], "Sulfato de sodio"),
  ],
  mistakes=[
      ("Escribir CaOH2 para el hidróxido de calcio.", "El subíndice 2 afecta a todo el ion hidróxido y requiere paréntesis.", "Encierra el ion poliatómico en paréntesis."),
      ("Cambiar los subíndices dentro del ion poliatómico.", "El ion poliatómico se mantiene igual: SO4 no puede ser SO3.", "Cruza cargas fuera del ion."),
  ],
  rec=[
      ("¿Cuántos elementos tiene un compuesto ternario?", "Tres", "Ternario significa tres."),
      ("¿Cuál es la fórmula del ion hidróxido?", "OH−", "Tiene un oxígeno y un hidrógeno, con carga 1−."),
      ("Verdadero o falso: H2SO4 es el ácido sulfúrico.", "Verdadero", "Es un oxoácido del azufre."),
  ],
  und=[
      ("¿Cuál es el nombre de NaNO3?", "Nitrato de sodio", "NO3− es el ion nitrato."),
      ("¿Por qué Al2(SO4)3 lleva paréntesis?", "Para indicar que el 3 multiplica todo el ion sulfato", "Hay tres iones SO4 completos."),
      ("¿Cuántos elementos distintos tiene CaCO3?", "Tres", "Contiene calcio, carbono y oxígeno."),
  ],
  app=[
      ("¿Cuál es la fórmula del hidróxido de magnesio, formado por Mg2+ y OH−?", "Mg(OH)2", "Se necesitan dos iones OH− para compensar Mg2+."),
      ("¿Cuál es la fórmula del nitrato de magnesio, formado por Mg2+ y NO3−?", "Mg(NO3)2", "Dos iones nitrato compensan un Mg2+."),
      arith("¿Cuántos átomos de oxígeno hay en Al2(SO4)3?", "3*4", "Hay 3 iones sulfato y cada uno tiene 4 átomos de oxígeno.", " átomos"),
  ],
  rea=[
      ("Un estudiante escribe AlOH3 para el hidróxido de aluminio (Al3+ y OH−). ¿Qué corrección es correcta? A) Debe ser Al(OH)3, porque el 3 afecta a todo el ion OH B) Está bien escrito", "A", "El paréntesis agrupa el ion."),
      ("¿Cuál de estos compuestos es una oxisal: NaCl o Na2CO3?", "Na2CO3", "Tiene un ion poliatómico con oxígeno."),
  ],
  cha=[
      arith("¿Cuántos átomos hay en total en una unidad de Ca(NO3)2?", "1+2+2*3", "Hay 1 Ca, 2 N y 6 O.", " átomos"),
      ("En Fe(OH)3, ¿qué carga tiene el hierro y cómo se nombra el compuesto?", "3+, hidróxido de hierro (III)", "Tres iones OH− suman 3−, que el hierro compensa con 3+."),
  ],
  context=[ex("Chile exportó salitre, formado principalmente por NaNO3. ¿Cómo se llama ese compuesto?", "Nitrato de sodio", "NO3− es el ion nitrato.")],
  selfcheck=[("¿Qué es un ion poliatómico?", "Un grupo de átomos unidos que actúa como un ion", "Tiene una carga total."), ("Da un ejemplo de oxoácido.", "H2SO4, ácido sulfúrico", "Contiene hidrógeno, azufre y oxígeno."), ("¿Por qué se usa el paréntesis?", "Para multiplicar un ion poliatómico completo", "El subíndice afecta a todo el grupo.")],
  open_task=task("Escribe la fórmula de estos seis compuestos y cuenta los átomos de cada elemento: hidróxido de sodio (Na+, OH−), carbonato de calcio (Ca2+, CO3 2−), sulfato de magnesio (Mg2+, SO4 2−), nitrato de potasio (K+, NO3−), fosfato de sodio (Na+, PO4 3−) y sulfato de aluminio (Al3+, SO4 2−). Anota una precaución de seguridad sobre los hidróxidos.", "NaOH: 1 Na, 1 O, 1 H. CaCO3: 1 Ca, 1 C, 3 O. MgSO4: 1 Mg, 1 S, 4 O. KNO3: 1 K, 1 N, 3 O. Na3PO4: 3 Na, 1 P, 4 O. Al2(SO4)3: 2 Al, 3 S, 12 O. Los hidróxidos son corrosivos y no se manipulan sin guía.", ["seis fórmulas", "conteo de átomos", "una precaución de seguridad"], ["tabla de seis filas"], ["olvidar el paréntesis", "no cruzar las cargas"], "Pregunta qué fórmula tendría el sulfato de potasio."),
  reinforce="Escribe la fórmula del carbonato de calcio y cuenta sus átomos.",
  extend="Explica por qué H2CO3 es un oxoácido y NaOH es un hidróxido.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Los datos de propiedades son aproximados y están escritos en los ejercicios.",
  use="Aprenderé a integrar fórmulas, cargas, nombres y propiedades de los compuestos binarios y ternarios. Sirve para resolver problemas del tipo nombre-fórmula y para predecir propiedades.",
  prior=["Sé formar y nombrar compuestos binarios y ternarios.", "Sé relacionar enlace y propiedades."],
  explain=[
      "Un procedimiento seguro para pasar del nombre a la fórmula es: 1) identifica los iones y sus cargas; 2) cruza los números de las cargas y simplifica; 3) usa paréntesis si hay más de un ion poliatómico; 4) verifica que la suma de cargas sea cero. Para pasar de la fórmula al nombre, identifica el ion poliatómico o el no metal y nombra primero el anión y luego el metal. Si el metal puede tener varias cargas, indícala con número romano.",
      "El tipo de enlace permite predecir propiedades. Los compuestos iónicos, como NaCl, CaO y CaCO3, son sólidos cristalinos con puntos de fusión altos y conducen la electricidad disueltos o fundidos. Los compuestos covalentes, formados por no metales, como CO2, H2O o CH4, suelen ser gases o líquidos y tener puntos de fusión bajos. Por ejemplo, el óxido de calcio funde a unos 2.600 °C y el dióxido de carbono sublima a −78 °C.",
      "Contar iones y átomos en una unidad de fórmula ayuda a interpretar los compuestos. En MgCl2 hay 1 ion Mg2+ y 2 iones Cl−, en total 3 iones. En Al2(SO4)3 hay 2 iones Al3+ y 3 iones SO4 2−, y 2 + 3 + 12 = 17 átomos.",
  ],
  vocab=[("unidad de fórmula", "la menor relación de iones de un compuesto iónico, como NaCl o MgCl2"), ("anión", "ion con carga negativa"), ("catión", "ion con carga positiva"), ("compuesto iónico", "compuesto formado por iones unidos por atracción eléctrica"), ("compuesto covalente", "compuesto formado por átomos que comparten electrones"), ("punto de fusión", "temperatura a la que una sustancia sólida se vuelve líquida")],
  worked=[
      ("Del nombre a la fórmula", "Escribe la fórmula del sulfato de aluminio (Al3+ y SO4 2−).", ["Cruzo los números: 2 pasa al aluminio y 3 pasa al sulfato.", "El sulfato va entre paréntesis: Al2(SO4)3.", "Verifico: 2 × 3+ = +6 y 3 × 2− = −6."], "Al2(SO4)3"),
      ("De la fórmula a la propiedad", "Predice si el KCl o el CH4 tiene mayor punto de fusión.", ["KCl es un compuesto iónico, con fuerte atracción entre iones.", "CH4 es covalente molecular, con fuerzas débiles entre moléculas."], "El KCl"),
  ],
  mistakes=[
      ("Predecir propiedades solo por el color o el aspecto.", "Las propiedades dependen del tipo de enlace.", "Identifica metal y no metal antes de predecir."),
      ("Contar solo un ion al calcular el total de átomos.", "Hay que multiplicar por los subíndices y los coeficientes.", "Cuenta ion por ion."),
  ],
  rec=[
      ("Verdadero o falso: si la suma de cargas no es cero, la fórmula está mal escrita.", "Verdadero", "Un compuesto iónico es neutro."),
      ("¿Cuál es la fórmula del óxido de sodio (Na+ y O2−)?", "Na2O", "Dos Na+ compensan un O2−."),
      ("Un ion con carga 3+ como Al3+, ¿es catión o anión?", "Catión", "Tiene carga positiva."),
  ],
  und=[
      ("Un compuesto iónico suele tener un punto de fusión: A) alto B) bajo", "A", "La atracción entre iones es fuerte."),
      ("¿Cuántos iones hay en una unidad de MgCl2?", "3", "Un Mg2+ y dos Cl−."),
      ("¿Qué compuesto es covalente: NaCl o CO2?", "CO2", "Une dos no metales que comparten electrones."),
  ],
  app=[
      ("¿Cuántos iones Cl− hay por cada Ca2+ en el CaCl2?", "2", "Dos iones Cl− compensan un Ca2+."),
      ("Sustancia X, de ejemplo: funde a 1.100 °C y conduce disuelta. Sustancia Y: funde a 50 °C y no conduce. ¿Cuál tiene enlace iónico?", "La X", "Alto punto de fusión y conducción son típicos de los compuestos iónicos."),
      ("¿Cuál es la fórmula del sulfato de potasio, formado por K+ y SO4 2−?", "K2SO4", "Dos K+ compensan un SO4 2−."),
  ],
  rea=[
      ("Un estudiante dice que el CO2 es iónico porque tiene oxígeno, que forma iones. ¿Qué respuesta es correcta? A) El CO2 une dos no metales que comparten electrones: es covalente B) Es iónico porque tiene oxígeno", "A", "Para ser iónico se necesita un metal."),
      ("Entre CaO y CO2, ¿cuál esperas que tenga mayor punto de fusión?", "El CaO", "Es iónico, con fuerte atracción entre iones."),
  ],
  cha=[
      ("Un ion X3+ se une con un ion Y2−. ¿Cuál es la fórmula del compuesto?", "X2Y3", "2 × 3+ compensa 3 × 2−."),
      arith("¿Cuántos átomos hay en total en una unidad de fosfato de calcio, Ca3(PO4)2?", "3+2+2*4", "Hay 3 Ca, 2 P y 8 O.", " átomos"),
  ],
  context=[ex("Las conchas de mar contienen CaCO3. ¿Cuántos iones Ca2+ se necesitan para neutralizar 3 iones CO3 2−?", "3", "Cada Ca2+ compensa un CO3 2−.")],
  selfcheck=[("¿Cómo se verifica una fórmula iónica?", "Comprobando que la suma de cargas sea cero", "Los compuestos iónicos son neutros."), ("¿Qué propiedades tiene un compuesto iónico?", "Punto de fusión alto y conduce disuelto", "Los iones se atraen con fuerza."), ("¿Qué compuestos suelen ser gases a temperatura ambiente?", "Los covalentes moleculares pequeños", "Las fuerzas entre moléculas son débiles.")],
  open_task=task("Con los iones Na+, Mg2+, Al3+, Cl−, O2− y SO4 2−, escribe la fórmula y el nombre de estos seis compuestos: Na con Cl, Mg con O, Al con O, Mg con SO4, Al con SO4 y Na con SO4. Clasifícalos en binarios y ternarios y verifica la suma de cargas de cada uno. Predice cuál esperas con mayor punto de fusión entre NaCl y CO2 y explica por qué.", "NaCl, cloruro de sodio (binario); MgO, óxido de magnesio (binario); Al2O3, óxido de aluminio (binario); MgSO4, sulfato de magnesio (ternario); Al2(SO4)3, sulfato de aluminio (ternario); Na2SO4, sulfato de sodio (ternario). NaCl tiene mayor punto de fusión: es iónico, con atracción fuerte entre iones; el CO2 es molecular.", ["seis fórmulas y nombres", "clasificación correcta", "verificación de cargas", "predicción con enlace"], ["tabla y respuesta escrita"], ["olvidar el paréntesis en Al2(SO4)3", "predecir por el color"], "Pregunta qué cambiaría si el metal tuviera dos cargas posibles."),
  reinforce="Escribe la fórmula del sulfato de sodio y verifica su carga total.",
  extend="Explica por qué los compuestos iónicos conducen la electricidad solo cuando están disueltos o fundidos.")

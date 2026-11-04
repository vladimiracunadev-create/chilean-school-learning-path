"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 18 (conservación de átomos y masa en reacciones)."""
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


OA = "CN1M OA 18"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Si quieres comprobarlo en casa, con una persona adulta: balanza de cocina, botella plástica, globo, levadura, azúcar y agua tibia (no caliente). No se hace ninguna combustión.",
  use="Aprenderé la ley de conservación de la masa y cómo comprobarla con una balanza. Sirve para entender por qué la masa «desaparece» solo cuando un gas se escapa.",
  prior=["Sé que en una reacción se forman productos a partir de reactantes.", "Sé usar una balanza y las unidades de masa en gramos."],
  explain=[
      "La ley de conservación de la masa, formulada por Antoine Lavoisier, dice que en una reacción química la masa total de los reactantes es igual a la masa total de los productos, siempre que ningún material entre ni salga del sistema. Un sistema cerrado es aquel en que no entra ni sale materia. Un sistema abierto permite que entren o salgan materiales, como los gases.",
      "Por eso, si fermentas azúcar con levadura en una botella cerrada con un globo, la masa total antes y después es la misma, aunque el globo se infle. En cambio, si la botella queda abierta, el dióxido de carbono escapa y la balanza marca menos masa. Al revés, cuando la lana de acero se oxida, la masa aumenta, porque el hierro se une con oxígeno del aire. En todos los casos, la masa total, incluyendo los gases, se conserva.",
      "Para comprobarlo se mide la masa del sistema completo antes y después, con una balanza. Toda medición tiene una incertidumbre: si las diferencias son menores que la precisión de la balanza, no se puede decir que haya cambiado la masa. Una pregunta investigable es: «¿Cambia la masa total de una botella cerrada con levadura y azúcar en 30 minutos?».",
  ],
  vocab=[("ley de conservación de la masa", "en una reacción, la masa de los reactantes es igual a la de los productos"), ("sistema cerrado", "sistema donde no entra ni sale materia"), ("sistema abierto", "sistema donde puede entrar o salir materia"), ("masa", "cantidad de materia de un cuerpo, que se mide en gramos"), ("balanza", "instrumento que mide la masa"), ("precisión", "diferencia más pequeña que un instrumento puede distinguir")],
  worked=[
      ("Sistema cerrado", "Una botella cerrada con levadura, azúcar y agua tiene 250 g antes de la reacción. ¿Cuánto indica la balanza después?", ["El sistema es cerrado: nada entra ni sale.", "Según la ley, la masa total se conserva."], "250 g"),
      ("Sistema abierto", "Una botella abierta tenía 250 g y después de la reacción tiene 248 g. ¿Dónde fueron los 2 g?", ["La botella abierta deja salir gases.", "Los 2 g corresponden al gas que escapó."], "Escaparon como gas"),
  ],
  mistakes=[
      ("Pensar que la masa desaparece cuando se forma un gas.", "El gas tiene masa y, si escapa, se lleva esa masa del sistema.", "Cierra el sistema o suma la masa del gas."),
      ("Creer que la masa cambia cuando solo se infla un globo.", "El globo con gas dentro de un sistema cerrado mantiene la masa total.", "Mide siempre todo el sistema."),
  ],
  rec=[
      ("¿Qué dice la ley de conservación de la masa?", "Que la masa de reactantes y de productos es igual en un sistema cerrado", "No se crea ni se destruye masa en una reacción."),
      ("Verdadero o falso: en un sistema cerrado la masa total aumenta cuando se forma un gas.", "Falso", "El gas queda dentro y la masa total es la misma."),
      ("¿Quién formuló la ley de conservación de la masa?", "Antoine Lavoisier", "Es el científico al que se atribuye esta ley."),
  ],
  und=[
      ("Una botella cerrada con globo marca 300 g antes de la reacción. ¿Cuánto marcará después? A) 300 g B) 295 g", "A", "El sistema es cerrado y la masa se conserva."),
      ("¿Por qué una botella abierta marca menos masa después de producirse un gas?", "Porque el gas escapa y se lleva masa", "El gas tiene masa."),
      ("¿Qué es un sistema cerrado?", "Un sistema donde no entra ni sale materia", "Se puede mantener tapado."),
  ],
  app=[
      arith("Una botella abierta tenía 420 g y después de la reacción tiene 416 g. ¿Cuántos gramos de gas escaparon?", "420-416", "Se resta la masa final a la inicial.", " g"),
      arith("Una lana de acero de 20 g se oxida y pasa a 26 g. ¿Cuántos gramos de oxígeno incorporó?", "26-20", "Se resta la masa inicial a la final.", " g"),
      arith("En una botella cerrada se mezclan 150 g de reactantes y 120 g de agua. ¿Cuántos gramos tendrá el sistema después de la reacción?", "150+120", "La masa total se conserva.", " g"),
  ],
  rea=[
      ("Un compañero dice que, al quemar papel, la masa desaparece. ¿Qué corrección es correcta? A) Los gases y las cenizas, sumados, igualan la masa del papel más el oxígeno usado; los gases escapan B) Tiene razón, la masa se destruye", "A", "La masa no se destruye: se encuentra en los gases."),
      ("¿Qué debes medir para comprobar la conservación de la masa en una botella cerrada? A) La masa de toda la botella, con su contenido, antes y después B) El color del contenido", "A", "Es el sistema completo el que conserva la masa."),
  ],
  cha=[
      ("Una balanza tiene una precisión de ±1 g. Una botella cerrada marca 250 g antes y 249 g después. ¿Se puede decir que la masa cambió?", "No", "La diferencia está dentro de la incertidumbre de la balanza."),
      arith("56 g de hierro reaccionan en un sistema cerrado con 24 g de oxígeno y forman óxido de hierro. ¿Cuántos gramos de producto se forman?", "56+24", "La masa del producto es igual a la suma de las masas de los reactantes.", " g"),
  ],
  context=[arith("Una masa de pan pesa 600 g antes de entrar al horno y 540 g al salir. ¿Cuántos gramos salieron como vapor y gases?", "600-540", "Se resta la masa final a la inicial.", " g")],
  selfcheck=[("¿Cuándo parece que se pierde masa en una reacción?", "Cuando un gas escapa de un sistema abierto", "El gas se lleva su masa."), ("¿Qué pasa con la masa de la lana de acero que se oxida?", "Aumenta porque incorpora oxígeno", "El oxígeno viene del aire."), ("¿Con qué instrumento se mide en gramos la masa de un sistema?", "La balanza", "Se mide en gramos.")],
  open_task=task("Datos de ejemplo de dos montajes con 2 cucharaditas de levadura, 2 de azúcar y 100 mL de agua tibia, medidos con una balanza de cocina. Montaje 1, botella cerrada con globo: 412 g antes y 412 g después. Montaje 2, botella abierta: 412 g antes y 410 g después. Calcula la diferencia de cada montaje, explica cada resultado con la ley de la conservación de la masa y escribe una pregunta investigable. Si lo haces en casa, hazlo con una persona adulta y sin usar agua caliente.", "Montaje 1: diferencia de 0 g; el sistema es cerrado, el gas queda en el globo. Montaje 2: diferencia de 2 g; el dióxido de carbono escapó. Pregunta: «¿Cuántos gramos de masa pierde una botella abierta con levadura en 30 minutos?».", ["dos diferencias correctas", "explicación con sistema cerrado y abierto", "pregunta con una medición"], ["cálculos y dos explicaciones"], ["decir que la masa se destruye en el montaje 2", "no mencionar el gas"], "Pregunta cuánto cambiaría el resultado con más levadura."),
  reinforce="Explica por qué una botella cerrada con globo mantiene su masa.",
  extend="Explica por qué una balanza poco precisa limita lo que puedes concluir.")

L(OA, 2,
  materials="Este cuaderno y lápiz. Para el modelo puedes usar botones o bolitas de tres colores; también se puede dibujar con círculos.",
  use="Aprenderé que los átomos se conservan en las reacciones químicas y a contar átomos para comprobar si una ecuación cumple la ley. Sirve para detectar ecuaciones mal escritas.",
  prior=["Sé leer fórmulas, subíndices y coeficientes.", "Sé que los átomos se reordenan en una reacción."],
  explain=[
      "En una reacción química los átomos no se crean ni se destruyen: se reordenan. Por eso el número de átomos de cada elemento es igual en los reactantes y en los productos. Una ecuación química que cumple esto está balanceada. Si no cumple, está sin ajustar y no representa una reacción posible.",
      "Para contar átomos se multiplica el coeficiente por el subíndice. En CH4 + 2 O2 → CO2 + 2 H2O hay, a la izquierda, 1 C, 4 H y 4 O; a la derecha, 1 C, 4 H (2 × 2) y 4 O (2 + 2 × 1). Todos coinciden, así que está balanceada. En H2 + O2 → H2O hay 2 O a la izquierda y 1 O a la derecha, así que no está balanceada.",
      "Un modelo de partículas ayuda a ver la conservación: se dibujan los átomos como círculos y se cuenta cada color antes y después. Si falta un círculo en un lado, la ecuación está mal. Esta comparación se resume en una tabla de conteo con una fila por elemento.",
  ],
  vocab=[("ecuación balanceada", "ecuación con igual número de átomos de cada elemento en ambos lados"), ("ecuación sin ajustar", "ecuación en que el número de átomos no coincide en ambos lados"), ("conservación de los átomos", "el número de átomos de cada elemento no cambia en una reacción"), ("tabla de conteo", "tabla que compara los átomos de cada elemento antes y después"), ("coeficiente", "número delante de una fórmula"), ("subíndice", "número pequeño que indica los átomos de un elemento")],
  worked=[
      ("Ecuación balanceada", "Cuenta los átomos de CH4 + 2 O2 → CO2 + 2 H2O.", ["Izquierda: C 1; H 4; O 2 × 2 = 4.", "Derecha: C 1; H 2 × 2 = 4; O 2 + 2 = 4.", "Los números coinciden."], "Está balanceada"),
      ("Ecuación sin ajustar", "Cuenta los átomos de H2 + O2 → H2O.", ["Izquierda: H 2; O 2.", "Derecha: H 2; O 1.", "El oxígeno no coincide."], "No está balanceada: falta un átomo de oxígeno a la derecha"),
  ],
  mistakes=[
      ("Creer que desaparece un átomo cuando no coinciden los números.", "Los átomos se conservan; lo que falla es la ecuación sin ajustar.", "Ajusta los coeficientes antes de interpretar."),
      ("Contar solo el coeficiente y olvidar el subíndice.", "En 2 H2O hay 4 H, no 2.", "Multiplica coeficiente por subíndice."),
  ],
  rec=[
      ("¿Se crean átomos nuevos en una reacción química?", "No", "Los átomos se reordenan."),
      ("Verdadero o falso: en una ecuación balanceada el número de átomos de cada elemento es igual en ambos lados.", "Verdadero", "Es la ley de conservación aplicada a los átomos."),
      ("¿Cuántos átomos de hidrógeno hay en 4 H2O?", "8", "Se multiplica 4 por 2."),
  ],
  und=[
      ("En N2 + 3 H2 → 2 NH3, ¿cuántos átomos de nitrógeno hay en cada lado?", "2 en cada lado", "Izquierda 2 de N2; derecha 2 × 1 de 2 NH3."),
      ("¿Está balanceada Mg + O2 → MgO?", "No", "Hay 2 átomos de O a la izquierda y 1 a la derecha."),
      ("¿Qué se cuenta para saber si una ecuación está balanceada?", "Los átomos de cada elemento", "Deben ser iguales en ambos lados."),
  ],
  app=[
      arith("¿Cuántos átomos de hidrógeno hay en 3 NH3?", "3*3", "Cada NH3 tiene 3 átomos de hidrógeno.", " átomos"),
      arith("¿Cuántos átomos de hidrógeno hay en 2 C2H6?", "2*6", "Cada C2H6 tiene 6 átomos de hidrógeno.", " átomos"),
      arith("¿Cuántos átomos de oxígeno hay en 2 CO2 + 3 H2O?", "2*2+3*1", "Se suman los átomos de oxígeno de cada sustancia.", " átomos"),
  ],
  rea=[
      ("Un estudiante dice que en H2 + O2 → H2O desaparece un átomo de oxígeno. ¿Qué corrección es correcta? A) Los átomos no desaparecen; la ecuación está sin ajustar y le faltan coeficientes B) Así ocurre en la reacción", "A", "La ecuación no representa la conservación."),
      ("Un dibujo de ejemplo tiene a la izquierda 2 círculos negros (C) y 6 blancos (H), y a la derecha 2 negros y 4 blancos. ¿Está balanceado?", "No", "Los átomos de hidrógeno son 6 y 4."),
  ],
  cha=[
      arith("En C3H8 + 5 O2 → 3 CO2 + 4 H2O, ¿cuántos átomos de oxígeno hay en los productos?", "3*2+4*1", "Se suman los oxígenos de 3 CO2 y de 4 H2O.", " átomos"),
      ("¿Está balanceada 4 Fe + 3 O2 → 2 Fe2O3?", "Sí", "Hay 4 Fe y 6 O en cada lado."),
  ],
  context=[arith("En la combustión del propano de un balón, C3H8 + 5 O2 → 3 CO2 + 4 H2O. ¿Cuántos átomos de hidrógeno hay en los productos?", "4*2", "Cada H2O tiene 2 átomos de hidrógeno y hay 4.", " átomos")],
  selfcheck=[("¿Qué significa que una ecuación esté balanceada?", "Que hay los mismos átomos de cada elemento en ambos lados", "Cumple la conservación."), ("¿Cómo se cuentan los átomos de un elemento en 3 H2O?", "Multiplicando 3 por el subíndice", "El coeficiente multiplica la fórmula."), ("¿Qué muestra una tabla de conteo?", "Los átomos de cada elemento antes y después", "Permite comparar fácilmente.")],
  open_task=task("Dibuja con círculos (H blanco, O rojo) el modelo de 2 H2 + O2 → 2 H2O. Completa una tabla de conteo con las filas H y O, y las columnas «antes» y «después». Luego cuenta los átomos de N2 + H2 → NH3 y explica por qué no está balanceada.", "2 H2 + O2 → 2 H2O: H, 4 antes y 4 después; O, 2 y 2. N2 + H2 → NH3: N, 2 antes y 1 después; H, 2 antes y 3 después, por lo que no está balanceada.", ["dibujo correcto", "tabla con dos filas", "conteo de la ecuación sin ajustar", "explicación"], ["dibujo y tabla"], ["contar solo moléculas y no átomos", "dar por balanceada una ecuación sin contar"], "Pregunta qué coeficientes arreglarían la segunda ecuación."),
  reinforce="Cuenta los átomos de cada elemento en 2 H2 + O2 → 2 H2O.",
  extend="Explica por qué una ecuación sin ajustar no puede representar una reacción real.")

L(OA, 3,
  materials="Este cuaderno y lápiz. Si quieres, usa bolitas o botones de colores para armar los átomos.",
  use="Aprenderé a ajustar los coeficientes de una ecuación química por tanteo. Sirve para escribir ecuaciones que respeten la ley de conservación.",
  prior=["Sé contar átomos en una ecuación.", "Sé que los subíndices no se cambian."],
  explain=[
      "Balancear una ecuación significa ajustar los coeficientes hasta que haya los mismos átomos de cada elemento en ambos lados. Solo se cambian los coeficientes, nunca los subíndices, porque cambiar un subíndice cambia la sustancia: H2O es agua y H2O2 es agua oxigenada. Los coeficientes deben ser los enteros más pequeños posibles.",
      "Un método por tanteo es: 1) cuenta los átomos de cada elemento; 2) empieza por el elemento que aparece en menos sustancias, y deja el oxígeno y el hidrógeno para el final si están en varias; 3) ajusta un coeficiente a la vez y vuelve a contar; 4) verifica todos los elementos. Ejemplo: H2 + O2 → H2O pasa a 2 H2 + O2 → 2 H2O. Ejemplo: N2 + H2 → NH3 pasa a N2 + 3 H2 → 2 NH3. Ejemplo: Mg + O2 → MgO pasa a 2 Mg + O2 → 2 MgO.",
      "En ecuaciones con carbono e hidrógeno se ajusta primero el C, luego el H y al final el O. Ejemplo: CH4 + O2 → CO2 + H2O pasa a CH4 + 2 O2 → CO2 + 2 H2O. Ejemplo: 4 Fe + 3 O2 → 2 Fe2O3 se verifica con 4 Fe y 6 O en ambos lados.",
  ],
  vocab=[("balancear", "ajustar coeficientes para igualar los átomos en ambos lados"), ("tanteo", "método de ajustar coeficientes probando y verificando"), ("coeficiente entero mínimo", "el menor conjunto de coeficientes enteros que balancea la ecuación"), ("agua oxigenada", "H2O2, una sustancia distinta del agua"), ("verificación", "conteo final de átomos para comprobar el balance"), ("sustancia", "material con composición definida")],
  worked=[
      ("Balancear Mg + O2 → MgO", "Balancea Mg + O2 → MgO.", ["Cuento: Mg 1 y 1; O 2 y 1.", "Pongo 2 delante de MgO: O queda 2 y 2, pero Mg queda 1 y 2.", "Pongo 2 delante de Mg: Mg 2 y 2."], "2 Mg + O2 → 2 MgO"),
      ("Balancear CH4 + O2 → CO2 + H2O", "Balancea CH4 + O2 → CO2 + H2O.", ["C: 1 y 1. H: 4 y 2, así que pongo 2 delante de H2O.", "Ahora O: 2 a la izquierda; a la derecha 2 + 2 = 4. Pongo 2 delante de O2."], "CH4 + 2 O2 → CO2 + 2 H2O"),
  ],
  mistakes=[
      ("Cambiar un subíndice para igualar los átomos.", "Cambiar H2O por H2O2 produce otra sustancia.", "Ajusta solo coeficientes."),
      ("Dejar de verificar al final.", "Un ajuste puede desbalancear otro elemento.", "Cuenta todos los elementos antes de terminar."),
  ],
  rec=[
      ("Para balancear una ecuación, ¿se cambian los coeficientes o los subíndices?", "Los coeficientes", "Los subíndices definen la sustancia."),
      ("Verdadero o falso: cambiar un subíndice cambia la sustancia.", "Verdadero", "H2O y H2O2 son sustancias distintas."),
      ("¿Cuántos átomos de oxígeno hay en 2 MgO?", "2", "Cada MgO tiene 1 átomo de oxígeno."),
  ],
  und=[
      ("¿Está balanceada 2 Al + 3 Cl2 → 2 AlCl3?", "Sí", "Hay 2 Al y 6 Cl en cada lado."),
      ("En H2 + Cl2 → HCl, ¿qué coeficiente falta delante de HCl?", "2", "Con 2 HCl hay 2 H y 2 Cl en ambos lados."),
      ("¿Cuál es la ecuación ajustada? A) 2 Na + Cl2 → 2 NaCl B) Na + Cl2 → NaCl2", "A", "La opción B cambió la fórmula del producto."),
  ],
  app=[
      ("Balancea Al + O2 → Al2O3. Escribe los coeficientes en orden: Al, O2, Al2O3.", "4, 3, 2", "Hay 4 Al y 6 O en cada lado."),
      ("Balancea C + O2 → CO. Escribe los coeficientes en orden: C, O2, CO.", "2, 1, 2", "Hay 2 C y 2 O en cada lado."),
      ("Balancea H2O2 → H2O + O2. Escribe los coeficientes en orden: H2O2, H2O, O2.", "2, 2, 1", "Hay 4 H y 4 O en cada lado."),
  ],
  rea=[
      ("Un estudiante balancea H2 + O2 → H2O escribiendo H2O2 como producto. ¿Es válido? A) No: cambió la sustancia y solo se cambian los coeficientes B) Sí: así queda igual el oxígeno", "A", "H2O2 es otra sustancia."),
      ("2 H2 + O2 → 2 H2O y 4 H2 + 2 O2 → 4 H2O están balanceadas. ¿Por qué se prefiere la primera? A) Tiene los coeficientes enteros más pequeños B) Tiene más átomos", "A", "Se usa el conjunto mínimo de coeficientes."),
  ],
  cha=[
      ("Balancea C2H6 + O2 → CO2 + H2O. Escribe los coeficientes en orden: C2H6, O2, CO2, H2O.", "2, 7, 4, 6", "Hay 4 C, 12 H y 14 O en cada lado."),
      ("Balancea Fe2O3 + CO → Fe + CO2. Escribe los coeficientes en orden: Fe2O3, CO, Fe, CO2.", "1, 3, 2, 3", "Hay 2 Fe, 3 C y 6 O en cada lado."),
  ],
  context=[ex("El propano de un balón de gas se quema según C3H8 + O2 → CO2 + H2O. Escribe los coeficientes en orden: C3H8, O2, CO2, H2O.", "1, 5, 3, 4", "Hay 3 C, 8 H y 10 O en cada lado.")],
  selfcheck=[("¿Qué se puede cambiar al balancear?", "Solo los coeficientes", "Los subíndices dan la identidad de la sustancia."), ("¿Cuál es el último paso del tanteo?", "Verificar todos los elementos", "Un ajuste puede alterar otro elemento."), ("¿Por qué se usan los coeficientes enteros más pequeños?", "Porque son la forma mínima de la relación", "Evitan números innecesarios.")],
  open_task=task("Balancea estas cuatro ecuaciones y verifica con una tabla de conteo: (a) Na + O2 → Na2O; (b) N2 + O2 → NO; (c) C2H4 + O2 → CO2 + H2O; (d) Ca + O2 → CaO. Para una de ellas, explica por qué no puedes cambiar los subíndices.", "(a) 4 Na + O2 → 2 Na2O. (b) N2 + O2 → 2 NO. (c) C2H4 + 3 O2 → 2 CO2 + 2 H2O. (d) 2 Ca + O2 → 2 CaO. Cambiar un subíndice cambia la sustancia: Na2O sería otra sustancia si fuera NaO2.", ["cuatro ecuaciones correctas", "tabla de conteo", "explicación sobre los subíndices"], ["ecuaciones y tablas"], ["cambiar subíndices", "no verificar el oxígeno"], "Pregunta cómo comprobarías el balance con un dibujo de átomos."),
  reinforce="Balancea H2 + Cl2 → HCl.",
  extend="Explica por qué se deja el oxígeno para el final en las combustiones.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Las masas atómicas aproximadas que se usan son H = 1, C = 12, N = 14, O = 16, Mg = 24, Ca = 40 y Fe = 56.",
  use="Aprenderé a comprobar con números que la masa se conserva en una reacción y a predecir masas de productos. Sirve para pasar del modelo de átomos a las masas en gramos.",
  prior=["Sé balancear ecuaciones.", "Sé usar proporciones."],
  explain=[
      "Cada átomo tiene una masa relativa. Valores aproximados: H = 1, C = 12, N = 14, O = 16, Mg = 24, Ca = 40 y Fe = 56. La masa relativa de una fórmula es la suma de las masas de sus átomos: H2O = 2 × 1 + 16 = 18; CO2 = 12 + 2 × 16 = 44. Si se multiplican por el coeficiente, se comprueba que la masa se conserva.",
      "Ejemplo: 2 H2 + O2 → 2 H2O. A la izquierda: 2 × 2 + 32 = 36. A la derecha: 2 × 18 = 36. Son iguales. Si se toman esas masas en gramos, 4 g de hidrógeno y 32 g de oxígeno forman 36 g de agua. Ejemplo: 2 Mg + O2 → 2 MgO. A la izquierda: 2 × 24 + 32 = 80. A la derecha: 2 × 40 = 80.",
      "Si se cambia la cantidad de reactantes, la de productos cambia en la misma proporción. Con la mitad de las masas se obtiene la mitad del producto, y con el doble de las masas se obtiene el doble. Esta relación proporcional permite predecir cuánto producto se formará y cuánto reactante hace falta.",
  ],
  vocab=[("masa atómica relativa", "masa de un átomo comparada con una unidad común"), ("masa relativa de una fórmula", "suma de las masas atómicas de los átomos de la fórmula"), ("proporcionalidad", "relación en que dos magnitudes cambian en la misma razón"), ("producto", "sustancia que se forma"), ("reactante", "sustancia que reacciona"), ("predicción", "cálculo anticipado de una cantidad")],
  worked=[
      ("Conservación con números", "Comprueba con C + O2 → CO2 (C = 12, O = 16) que la masa se conserva.", ["Reactantes: 12 + 2 × 16 = 44.", "Producto: 12 + 2 × 16 = 44."], "44 = 44: la masa se conserva"),
      ("Predicción con proporción", "En 2 Mg + O2 → 2 MgO, 48 g de Mg forman 80 g de MgO. ¿Cuánto MgO forman 24 g de Mg?", ["24 g es la mitad de 48 g.", "El producto es la mitad de 80 g."], "40 g"),
  ],
  mistakes=[
      ("Creer que la masa de los productos puede ser menor que la de los reactantes en un sistema cerrado.", "La masa se conserva; si faltan gramos, algo escapó o no reaccionó.", "Revisa si el sistema era cerrado y si todo reaccionó."),
      ("Olvidar multiplicar por el coeficiente al calcular la masa.", "2 MgO tiene el doble de masa que 1 MgO.", "Multiplica masa de la fórmula por su coeficiente."),
  ],
  rec=[
      ("Verdadero o falso: en un sistema cerrado, la masa de los reactantes es igual a la de los productos.", "Verdadero", "Es la ley de conservación de la masa."),
      ("¿Cuál es la masa relativa del NH3 (N = 14, H = 1)?", "17", "14 + 3 × 1 = 17."),
      ("¿Cuál es la masa relativa del H2O (H = 1, O = 16)?", "18", "2 × 1 + 16 = 18."),
  ],
  und=[
      ("En N2 + 3 H2 → 2 NH3, ¿cuál es la masa relativa total de los reactantes (N2 = 28, H2 = 2)?", "34", "28 + 3 × 2 = 34."),
      ("Si se duplican las masas de los reactantes, la masa del producto: A) se duplica B) se reduce a la mitad", "A", "Hay proporcionalidad directa."),
      ("¿Cuál es la masa relativa del CH4 (C = 12, H = 1)?", "16", "12 + 4 × 1 = 16."),
  ],
  app=[
      arith("En C + O2 → CO2, 6 g de carbono reaccionan con 16 g de oxígeno. ¿Cuántos gramos de CO2 se forman?", "6+16", "La masa del producto es igual a la suma de las masas de los reactantes.", " g"),
      arith("En 2 Ca + O2 → 2 CaO, 80 g de calcio reaccionan con 32 g de oxígeno. ¿Cuántos gramos de CaO se forman?", "80+32", "Se suman las masas de los reactantes.", " g"),
      arith("18 g de magnesio forman 30 g de óxido de magnesio. ¿Cuántos gramos de oxígeno reaccionaron?", "30-18", "El oxígeno es la diferencia entre la masa del producto y la del magnesio.", " g"),
  ],
  rea=[
      ("Un grupo dice que 10 g de un reactante y 10 g de otro, en un sistema cerrado, formaron 15 g de producto. ¿Qué corresponde? A) Es imposible: deberían ser 20 g; hay que revisar si algo escapó o no reaccionó B) Es posible porque la masa se destruye", "A", "La masa total debe conservarse."),
      ("Si 12 g, 24 g y 48 g de magnesio forman 20 g, 40 g y 80 g de óxido de magnesio, ¿qué relación hay entre ambas masas?", "Proporcional directa", "Al multiplicar una por un número, la otra se multiplica por el mismo."),
  ],
  cha=[
      arith("Con la relación de la tabla (12 g de Mg forman 20 g de MgO), ¿cuántos gramos de MgO se forman con 36 g de Mg?", "36*20/12", "Se multiplica la masa de Mg por la razón 20 ÷ 12.", " g"),
      arith("28 g de hierro reaccionan en un sistema cerrado y forman 40 g de óxido de hierro. ¿Cuántos gramos de oxígeno reaccionaron?", "40-28", "La masa de oxígeno es la diferencia.", " g"),
  ],
  context=[arith("Se queman 2 g de hidrógeno con 16 g de oxígeno en un sistema cerrado. ¿Cuántos gramos de agua se forman?", "2+16", "La masa de agua es igual a la suma de las masas de los reactantes.", " g")],
  selfcheck=[("¿Cómo se calcula la masa relativa de una fórmula?", "Sumando las masas atómicas de sus átomos", "Se multiplica por el subíndice de cada átomo."), ("¿Qué pasa con la masa del producto si se duplica la de los reactantes?", "Se duplica", "Hay una proporcionalidad directa."), ("¿Cuándo no se cumple aparentemente la conservación?", "Cuando escapa un gas o no reaccionó todo", "El sistema debe ser cerrado.")],
  open_task=task("Con H = 1, C = 12, O = 16 y Mg = 24, completa una tabla para las reacciones C + O2 → CO2, 2 Mg + O2 → 2 MgO y 2 H2 + O2 → 2 H2O: masa relativa de los reactantes, masa relativa de los productos y si se conserva. Después predice cuánto MgO se forma con 12 g de Mg, sabiendo que 48 g forman 80 g, y escribe una pregunta investigable sobre la masa y las reacciones.", "C + O2: 44 y 44. 2 Mg + O2: 80 y 80. 2 H2 + O2: 36 y 36; en todos se conserva. Con 12 g de Mg: 12 ÷ 48 = 1/4, entonces 80 ÷ 4 = 20 g. Pregunta: «¿Se mantiene la masa total de una botella cerrada con levadura y azúcar durante 30 minutos?».", ["tres filas correctas", "predicción de 20 g", "pregunta con una medición"], ["tabla y cálculo"], ["no multiplicar por el coeficiente", "olvidar que el sistema debe ser cerrado"], "Pregunta qué cambiaría si el sistema fuera abierto."),
  reinforce="Calcula la masa relativa del CO2 y del H2O.",
  extend="Explica por qué la conservación de la masa permite predecir cuánto producto se formará.")

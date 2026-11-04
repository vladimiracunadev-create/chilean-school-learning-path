"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 20 (estequiometría y relaciones entre reactantes y productos)."""
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


OA = "CN1M OA 20"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Masas atómicas aproximadas: H = 1, C = 12, N = 14, O = 16, Na = 23, Mg = 24, S = 32, Ca = 40 y Fe = 56.",
  use="Aprenderé qué es el mol y la masa molar, y a pasar de gramos a mol. Sirve para comparar cantidades de partículas que no se pueden contar una a una.",
  prior=["Sé calcular la masa relativa de una fórmula.", "Sé balancear ecuaciones químicas."],
  explain=[
      "Las reacciones ocurren entre partículas, pero son tan pequeñas y tan numerosas que no se pueden contar una a una. Por eso los químicos usan el mol, la unidad de cantidad de sustancia. Un mol contiene 6,02 × 10 elevado a 23 partículas, un número enorme llamado número de Avogadro. Así como una docena son 12 unidades, un mol es esa cantidad fija de partículas, sea de agua, de dióxido de carbono o de hierro.",
      "La masa molar (M) es la masa de 1 mol de una sustancia, en gramos por mol (g/mol). Es numéricamente igual a la masa relativa de su fórmula. Con los valores aproximados: H2O, 18 g/mol; CO2, 44 g/mol; O2, 32 g/mol; CH4, 16 g/mol; NH3, 17 g/mol; NaOH, 40 g/mol (23 + 16 + 1); CaCO3, 100 g/mol (40 + 12 + 3 × 16); glucosa C6H12O6, 180 g/mol.",
      "La cantidad de sustancia n, en mol, se calcula como n = m ÷ M, donde m es la masa en gramos. Así, 36 g de agua son 36 ÷ 18 = 2 mol. Al revés, 3 mol de CO2 tienen una masa de 3 × 44 = 132 g. Un mol de cualquier sustancia contiene el mismo número de partículas, pero no la misma masa.",
  ],
  vocab=[("mol", "unidad de cantidad de sustancia: 6,02 × 10 elevado a 23 partículas"), ("número de Avogadro", "número de partículas de un mol"), ("masa molar", "masa de 1 mol de una sustancia, en g/mol"), ("cantidad de sustancia (n)", "número de mol de una muestra"), ("masa (m)", "cantidad de materia de una muestra, en gramos"), ("partícula", "átomo, molécula o ion")],
  worked=[
      ("De gramos a mol", "¿Cuántos mol hay en 90 g de agua (M = 18 g/mol)?", ["Uso n = m ÷ M.", "Calculo 90 ÷ 18."], "5 mol"),
      ("De mol a gramos", "¿Cuántos gramos son 2 mol de CO2 (M = 44 g/mol)?", ["Uso m = n × M.", "Calculo 2 × 44."], "88 g"),
  ],
  mistakes=[
      ("Creer que un mol de cualquier sustancia pesa lo mismo.", "Tienen el mismo número de partículas, pero cada sustancia tiene su masa molar.", "Calcula la masa molar de la sustancia."),
      ("Dividir la masa por el número de átomos en vez de por la masa molar.", "La conversión de masa a mol usa la masa molar de toda la fórmula.", "Suma las masas atómicas de la fórmula completa."),
  ],
  rec=[
      ("¿En qué unidad se mide la cantidad de sustancia?", "En mol", "Es la unidad de cantidad de partículas."),
      ("Verdadero o falso: un mol de cualquier sustancia contiene el mismo número de partículas.", "Verdadero", "Es el número de Avogadro."),
      ("¿Cuál es la masa molar del O2 (O = 16)?", "32 g/mol", "2 × 16 = 32."),
  ],
  und=[
      ("¿Cuál es la masa molar del Na2SO4 (Na = 23, S = 32, O = 16)?", "142 g/mol", "2 × 23 + 32 + 4 × 16 = 46 + 32 + 64 = 142."),
      ("En n = m ÷ M, ¿qué representa M?", "La masa de 1 mol de la sustancia", "Es la masa molar en g/mol."),
      ("¿Qué tiene más partículas: 1 mol de H2O o 1 mol de CO2?", "Tienen igual cantidad", "Un mol siempre tiene el mismo número de partículas."),
  ],
  app=[
      arith("¿Cuántos mol hay en 54 g de agua (M = 18 g/mol)?", "54/18", "Se divide la masa por la masa molar.", " mol"),
      arith("¿Cuántos gramos son 4 mol de O2 (M = 32 g/mol)?", "4*32", "Se multiplica la cantidad de sustancia por la masa molar.", " g"),
      arith("¿Cuál es la masa molar del óxido de hierro (III), Fe2O3 (Fe = 56, O = 16)?", "2*56+3*16", "Se suman las masas atómicas de todos los átomos de la fórmula: 2 de hierro y 3 de oxígeno.", " g/mol"),
  ],
  rea=[
      ("Un estudiante dice que 1 mol de agua pesa lo mismo que 1 mol de CO2. ¿Qué respuesta es correcta? A) Falso: tienen igual número de partículas, pero masas de 18 g y 44 g B) Verdadero, porque ambos son un mol", "A", "La masa molar depende de la sustancia."),
      ("¿Por qué se usa el mol y no se cuentan las partículas una a una? A) Porque son tan pequeñas y numerosas que no se pueden contar B) Porque el mol es otra forma de medir la masa en gramos", "A", "El mol agrupa un número muy grande de partículas."),
  ],
  cha=[
      arith("¿Cuántos mol hay en 264 g de CO2 (M = 44 g/mol)?", "264/44", "Se divide la masa por la masa molar.", " mol"),
      arith("¿Cuántos mol hay en 360 g de glucosa C6H12O6 (M = 180 g/mol)?", "360/180", "Se divide la masa por la masa molar.", " mol"),
  ],
  context=[arith("Un vaso contiene 72 g de agua. ¿Cuántos mol de agua hay?", "72/18", "Se divide la masa por 18 g/mol.", " mol")],
  selfcheck=[("¿Qué es un mol?", "Una cantidad fija de partículas, 6,02 × 10 elevado a 23", "Es el número de Avogadro."), ("¿Cómo se calcula la masa molar?", "Sumando las masas atómicas de los átomos de la fórmula", "Se expresa en g/mol."), ("¿Cómo se pasa de masa a mol?", "Dividiendo por la masa molar", "n = m ÷ M.")],
  open_task=task("Completa una tabla con H2O, CO2, NH3, NaOH y CaCO3. Primero calcula la masa molar de cada una. Luego calcula los mol de estas masas: 108 g de H2O, 88 g de CO2, 51 g de NH3, 120 g de NaOH y 200 g de CaCO3. Escribe una frase que explique por qué 1 mol de cada sustancia tiene distinta masa.", "Masas molares: 18, 44, 17, 40 y 100 g/mol. Cantidades: 6 mol de H2O, 2 mol de CO2, 3 mol de NH3, 3 mol de NaOH y 2 mol de CaCO3. Cada sustancia tiene partículas de distinta masa, aunque haya la misma cantidad de partículas en un mol.", ["cinco masas molares", "cinco cantidades en mol", "explicación de la diferencia de masa"], ["tabla de cinco filas y una frase"], ["dividir por el número de átomos", "usar una masa atómica incorrecta"], "Pregunta cuántos gramos tendrían 5 mol de cada sustancia."),
  reinforce="Calcula los mol que hay en 126 g de agua.",
  extend="Explica con una analogía por qué el mol no es una unidad de masa.")

L(OA, 2,
  materials="Este cuaderno, lápiz y calculadora. Las ecuaciones están balanceadas y escritas en los ejercicios.",
  use="Aprenderé a usar los coeficientes de una ecuación balanceada como razones de mol. Sirve para saber cuánto reactante se necesita y cuánto producto se forma.",
  prior=["Sé balancear ecuaciones.", "Sé usar el mol."],
  explain=[
      "Los coeficientes de una ecuación química balanceada indican en qué proporción reaccionan las sustancias en moles. En 2 H2 + O2 → 2 H2O, 2 mol de H2 reaccionan con 1 mol de O2 y forman 2 mol de H2O. Las razones son 2 : 1 : 2. Si se duplican las cantidades, se duplican los mol de todas las sustancias.",
      "Para calcular se usa una regla de tres con la razón de los coeficientes. Ejemplo: en N2 + 3 H2 → 2 NH3, si reaccionan 6 mol de H2, se forman 6 × 2 ÷ 3 = 4 mol de NH3. Ejemplo: en CH4 + 2 O2 → CO2 + 2 H2O, 3 mol de CH4 consumen 6 mol de O2 y producen 3 mol de CO2 y 6 mol de H2O.",
      "Atención: los coeficientes son razones de mol, no de gramos. En 2 H2 + O2 → 2 H2O no reaccionan 2 g de H2 con 1 g de O2: reaccionan 2 mol de H2, que son 4 g, con 1 mol de O2, que son 32 g.",
  ],
  vocab=[("estequiometría", "estudio de las cantidades de reactantes y productos en una reacción"), ("razón molar", "cociente entre los coeficientes de dos sustancias de una ecuación"), ("regla de tres", "método para calcular una cantidad a partir de una proporción"), ("ecuación balanceada", "ecuación con igual número de átomos de cada elemento en ambos lados"), ("cantidad de sustancia", "número de mol de una muestra"), ("coeficiente", "número delante de una fórmula en una ecuación")],
  worked=[
      ("Razón mol-mol", "En 2 H2 + O2 → 2 H2O, ¿cuántos mol de O2 reaccionan con 4 mol de H2?", ["La razón H2 : O2 es 2 : 1.", "Calculo 4 × 1 ÷ 2."], "2 mol"),
      ("Producto formado", "En N2 + 3 H2 → 2 NH3, ¿cuántos mol de NH3 se forman a partir de 3 mol de N2?", ["La razón N2 : NH3 es 1 : 2.", "Calculo 3 × 2 ÷ 1."], "6 mol"),
  ],
  mistakes=[
      ("Leer los coeficientes como gramos.", "Los coeficientes son razones de mol; los gramos dependen de las masas molares.", "Pasa siempre a mol antes de usar los coeficientes."),
      ("Usar una ecuación sin balancear.", "Las razones solo son correctas si la ecuación está balanceada.", "Balancea antes de calcular."),
  ],
  rec=[
      ("En 2 H2 + O2 → 2 H2O, ¿cuál es la razón de mol entre H2 y O2?", "2 : 1", "Son los coeficientes de H2 y O2."),
      ("Verdadero o falso: los coeficientes de una ecuación balanceada indican razones de mol.", "Verdadero", "Muestran la proporción en que reaccionan."),
      ("En N2 + 3 H2 → 2 NH3, ¿cuál es el coeficiente del NH3?", "2", "Está delante de la fórmula NH3."),
  ],
  und=[
      ("En CH4 + 2 O2 → CO2 + 2 H2O, ¿cuántos mol de O2 consume 1 mol de CH4?", "2", "El coeficiente del O2 es 2."),
      ("¿Se pueden leer los coeficientes como gramos?", "No", "Son razones de mol."),
      ("En N2 + 3 H2 → 2 NH3, ¿cuántos mol de H2 se necesitan para 1 mol de N2?", "3", "La razón N2 : H2 es 1 : 3."),
  ],
  app=[
      arith("En 2 H2 + O2 → 2 H2O, ¿cuántos mol de O2 reaccionan con 6 mol de H2?", "6/2", "La razón H2 : O2 es 2 : 1.", " mol"),
      arith("En N2 + 3 H2 → 2 NH3, ¿cuántos mol de NH3 se forman con 12 mol de H2?", "12*2/3", "La razón H2 : NH3 es 3 : 2.", " mol"),
      arith("En CH4 + 2 O2 → CO2 + 2 H2O, ¿cuántos mol de H2O se forman con 5 mol de CH4?", "5*2", "La razón CH4 : H2O es 1 : 2.", " mol"),
  ],
  rea=[
      ("Un estudiante dice: «En 2 H2 + O2 → 2 H2O, 2 g de H2 reaccionan con 1 g de O2». ¿Qué corrección es correcta? A) Los coeficientes son mol: 2 mol de H2 (4 g) reaccionan con 1 mol de O2 (32 g) B) Es correcto porque los coeficientes son gramos", "A", "Hay que convertir mol a gramos con las masas molares."),
      ("Si se duplican los mol de los reactantes de una ecuación balanceada, los mol de producto: A) se duplican B) se reducen a la mitad", "A", "Se mantiene la razón de los coeficientes."),
  ],
  cha=[
      arith("En 2 Mg + O2 → 2 MgO, ¿cuántos mol de O2 reaccionan con 8 mol de Mg?", "8/2", "La razón Mg : O2 es 2 : 1.", " mol"),
      arith("En 4 Fe + 3 O2 → 2 Fe2O3, ¿cuántos mol de Fe2O3 se forman con 8 mol de Fe?", "8*2/4", "La razón Fe : Fe2O3 es 4 : 2.", " mol"),
  ],
  context=[arith("En un calefactor a gas se quema propano según C3H8 + 5 O2 → 3 CO2 + 4 H2O. Si se queman 2 mol de propano, ¿cuántos mol de CO2 se producen?", "2*3", "La razón C3H8 : CO2 es 1 : 3.", " mol")],
  selfcheck=[("¿Qué indican los coeficientes de una ecuación balanceada?", "La proporción de mol en que reaccionan las sustancias", "Son razones molares."), ("¿Qué debe cumplir una ecuación para usarla en estequiometría?", "Estar balanceada", "Si no, las razones no son correctas."), ("¿Cómo cambian los productos si se duplican los reactantes?", "Se duplican", "La proporción se mantiene.")],
  open_task=task("Con 2 H2 + O2 → 2 H2O, N2 + 3 H2 → 2 NH3 y C3H8 + 5 O2 → 3 CO2 + 4 H2O, completa una tabla con dos columnas, «dato» y «resultado». Casos: (a) 10 mol de H2 en la primera, ¿cuántos mol de O2 y de H2O?; (b) 9 mol de H2 en la segunda, ¿cuántos mol de N2 y de NH3?; (c) 3 mol de C3H8 en la tercera, ¿cuántos mol de O2 y de CO2? Explica en una frase por qué los coeficientes no son gramos.", "(a) 5 mol de O2 y 10 mol de H2O. (b) 3 mol de N2 y 6 mol de NH3. (c) 15 mol de O2 y 9 mol de CO2. Los coeficientes son razones de mol; para pasar a gramos hay que multiplicar por la masa molar.", ["seis resultados correctos", "uso de las razones", "explicación sobre mol y gramos"], ["tabla y una frase"], ["usar las razones al revés", "tratar los coeficientes como gramos"], "Pregunta cuántos mol de agua se forman si el dato fuera 20 mol de H2."),
  reinforce="En 2 H2 + O2 → 2 H2O, calcula los mol de agua que se forman con 7 mol de H2.",
  extend="Explica por qué una ecuación sin balancear daría un cálculo incorrecto.")

L(OA, 3,
  materials="Este cuaderno, lápiz y calculadora. Masas atómicas aproximadas: H = 1, C = 12, N = 14, O = 16, Mg = 24, Ca = 40 y Fe = 56.",
  use="Aprenderé a calcular cuántos gramos de producto se forman o cuántos gramos de reactante se necesitan. Sirve para resolver problemas de laboratorio y de la industria.",
  prior=["Sé pasar de gramos a mol.", "Sé usar las razones de mol de una ecuación balanceada."],
  explain=[
      "Un problema de masa a masa tiene cuatro pasos. Primero, balancea la ecuación. Segundo, pasa la masa conocida a mol dividiendo por su masa molar. Tercero, usa la razón de los coeficientes para obtener los mol de la otra sustancia. Cuarto, pasa esos mol a gramos multiplicando por su masa molar. Al final, verifica que la masa total se conserve.",
      "Ejemplo: en 2 H2 + O2 → 2 H2O, ¿cuántos gramos de agua se forman con 8 g de H2? Paso 1: 8 ÷ 2 = 4 mol de H2. Paso 2: la razón H2 : H2O es 1 : 1, así que se forman 4 mol de H2O. Paso 3: 4 × 18 = 72 g. Ejemplo: en 2 Mg + O2 → 2 MgO, 48 g de Mg son 2 mol, que forman 2 mol de MgO, es decir, 80 g.",
      "Ejemplo de verificación: en CaCO3 → CaO + CO2, 200 g de CaCO3 son 2 mol. Forman 2 mol de CaO, que son 112 g, y 2 mol de CO2, que son 88 g. Como 112 + 88 = 200, la masa se conserva.",
  ],
  vocab=[("masa a masa", "cálculo que parte de la masa de una sustancia y llega a la masa de otra"), ("masa molar", "masa de 1 mol de una sustancia, en g/mol"), ("razón molar", "cociente entre coeficientes de dos sustancias"), ("verificación", "comprobación final de que la masa se conserva"), ("caliza", "roca formada principalmente por carbonato de calcio"), ("cal viva", "óxido de calcio, CaO")],
  worked=[
      ("Masa a masa", "En C + O2 → CO2, ¿cuántos gramos de CO2 se forman con 36 g de C (C = 12, CO2 = 44 g/mol)?", ["Paso 1: 36 ÷ 12 = 3 mol de C.", "Paso 2: la razón C : CO2 es 1 : 1, así que se forman 3 mol de CO2.", "Paso 3: 3 × 44 = 132 g."], "132 g"),
      ("Verificar la conservación", "En 2 Mg + O2 → 2 MgO, 48 g de Mg forman 80 g de MgO. ¿Cuántos gramos de O2 reaccionan?", ["La masa se conserva: 80 g de producto.", "Resto 80 − 48."], "32 g"),
  ],
  mistakes=[
      ("Usar los coeficientes como gramos.", "Los coeficientes son razones de mol.", "Pasa siempre por mol."),
      ("Olvidar balancear antes de calcular.", "Con una ecuación sin balancear las razones son incorrectas.", "Verifica el balance."),
  ],
  rec=[
      ("¿Qué se hace primero al pasar de masa a masa: convertir la masa a mol o usar los coeficientes?", "Convertir la masa a mol", "Los coeficientes se usan sobre mol."),
      ("Verdadero o falso: en un problema masa a masa se pasa por mol.", "Verdadero", "Es el puente entre gramos y coeficientes."),
      ("¿Cuántos gramos son 3 mol de MgO (M = 40 g/mol)?", "120 g", "3 × 40 = 120."),
  ],
  und=[
      ("¿Cuál es el cuarto paso de un problema masa a masa?", "Pasar los mol a gramos", "Se multiplica por la masa molar de la sustancia buscada."),
      ("¿Para qué se verifica la conservación de la masa al final?", "Para comprobar que el cálculo es coherente", "La masa total de reactantes y productos debe coincidir."),
      ("¿Cuántos mol son 16 g de CH4 (M = 16 g/mol)?", "1 mol", "16 ÷ 16 = 1."),
  ],
  app=[
      arith("En CH4 + 2 O2 → CO2 + 2 H2O, 16 g de CH4 (M = 16) forman agua (M = 18). ¿Cuántos gramos de agua se forman?", "16/16*2*18", "Se pasa a mol, se aplica la razón 1 : 2 y se vuelve a gramos.", " g"),
      arith("En 2 H2 + O2 → 2 H2O, 4 g de H2 (M = 2) forman agua (M = 18). ¿Cuántos gramos de agua se forman?", "4/2*18", "La razón es 1 : 1, así que los mol de agua son iguales a los de H2.", " g"),
      arith("En N2 + 3 H2 → 2 NH3, 28 g de N2 (M = 28) forman amoníaco (M = 17). ¿Cuántos gramos de NH3 se forman?", "28/28*2*17", "Se pasa a mol, se aplica la razón 1 : 2 y se vuelve a gramos.", " g"),
  ],
  rea=[
      ("Un estudiante calcula así: «2 g de H2 forman 2 g de H2O, porque los coeficientes son 2 y 2». ¿Qué corrección es correcta? A) Debe pasar a mol: 2 g de H2 son 1 mol, que forma 1 mol de H2O, es decir, 18 g B) Está bien, los coeficientes son gramos", "A", "Los coeficientes se usan sobre mol, no sobre gramos."),
      ("En CaCO3 → CaO + CO2, 400 g de CaCO3 forman 224 g de CaO y 176 g de CO2. ¿Se conserva la masa?", "Sí", "224 + 176 = 400."),
  ],
  cha=[
      arith("En C3H8 + 5 O2 → 3 CO2 + 4 H2O, 44 g de C3H8 (M = 44) forman CO2 (M = 44). ¿Cuántos gramos de CO2 se forman?", "44/44*3*44", "Se pasa a mol, se aplica la razón 1 : 3 y se vuelve a gramos.", " g"),
      arith("En Fe2O3 + 3 CO → 2 Fe + 3 CO2, 160 g de Fe2O3 (M = 160) forman hierro (Fe = 56). ¿Cuántos gramos de hierro se forman?", "160/160*2*56", "Se pasa a mol, se aplica la razón 1 : 2 y se vuelve a gramos.", " g"),
  ],
  context=[arith("La cal viva (CaO, M = 56) se obtiene calentando caliza (CaCO3, M = 100). ¿Cuántos gramos de cal viva se obtienen de 500 g de CaCO3 puro?", "500/100*56", "500 g son 5 mol de CaCO3, que forman 5 mol de CaO.", " g")],
  selfcheck=[("¿Cuáles son los pasos de un problema masa a masa?", "Balancear, pasar a mol, aplicar la razón y pasar a gramos", "Cada paso lleva al siguiente."), ("¿Por qué se pasa por mol?", "Porque los coeficientes relacionan mol, no gramos", "Hay que convertir antes y después."), ("¿Cómo se verifica el resultado?", "Comprobando que la masa total se conserve", "Reactantes y productos deben coincidir.")],
  open_task=task("Resuelve con los cuatro pasos y verifica la conservación: en 2 Mg + O2 → 2 MgO, calcula cuántos gramos de MgO se forman con 96 g de Mg (Mg = 24, MgO = 40 g/mol) y cuántos gramos de O2 reaccionan (O2 = 32 g/mol). Luego, en CaCO3 → CaO + CO2, calcula los gramos de CO2 que se obtienen de 300 g de CaCO3 (M = 100) y de CO2 (M = 44).", "96 g de Mg son 4 mol; forman 4 mol de MgO = 160 g; reaccionan 2 mol de O2 = 64 g; 96 + 64 = 160. Con 300 g de CaCO3 son 3 mol; forman 3 mol de CO2 = 132 g.", ["pasos ordenados", "160 g de MgO", "64 g de O2", "132 g de CO2", "verificación de masa"], ["cálculos escritos"], ["usar coeficientes como gramos", "olvidar la verificación"], "Pregunta cuánto se obtendría con la mitad de la masa inicial."),
  reinforce="Calcula los gramos de MgO que se forman con 24 g de Mg.",
  extend="Explica por qué los cálculos de masa a masa permiten ahorrar reactantes en la industria.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Masas molares: CO2 = 44, H2O = 18, glucosa C6H12O6 = 180 y O2 = 32 g/mol.",
  use="Aprenderé a identificar el reactivo limitante y a explicar con números la formación de la glucosa en la fotosíntesis. Sirve para entender cuánto producto puede obtenerse y cómo los seres vivos fabrican su alimento.",
  prior=["Sé hacer cálculos mol a mol y masa a masa.", "Sé que la fotosíntesis y la respiración celular son reacciones químicas."],
  explain=[
      "El reactivo limitante es el que se agota primero y determina cuánto producto se forma. El otro reactante queda en exceso. Es como armar sándwiches: con 2 panes y 1 queso por sándwich, si tienes 10 panes y 3 quesos, el queso limita y puedes armar 3 sándwiches. En 2 H2 + O2 → 2 H2O, con 6 mol de H2 y 2 mol de O2, 2 mol de O2 solo reaccionan con 4 mol de H2; el O2 es el limitante, se forman 4 mol de H2O y sobran 2 mol de H2.",
      "La fotosíntesis es la reacción en que las plantas, algas y algunas bacterias forman glucosa a partir de dióxido de carbono y agua, usando luz: 6 CO2 + 6 H2O → C6H12O6 + 6 O2. Los reactantes pesan 6 × 44 + 6 × 18 = 264 + 108 = 372 g. Los productos pesan 180 + 6 × 32 = 180 + 192 = 372 g. Se conserva la masa.",
      "La glucosa es alimento y materia para construir otras sustancias de los seres vivos, y el oxígeno liberado se usa en la respiración. En la respiración celular ocurre la reacción inversa, que libera la energía de la glucosa. Por la relación 6 : 1, cada 6 mol de CO2 que se fijan producen 1 mol de glucosa, es decir, 180 g.",
  ],
  vocab=[("reactivo limitante", "reactante que se agota primero y limita el producto"), ("reactivo en exceso", "reactante que sobra al terminar la reacción"), ("fotosíntesis", "reacción que forma glucosa y oxígeno a partir de CO2 y agua usando luz"), ("glucosa", "azúcar C6H12O6 que sirve de alimento y de materia"), ("proporcionalidad", "relación en que dos cantidades crecen en la misma razón"), ("clorofila", "pigmento que absorbe la luz en la fotosíntesis")],
  worked=[
      ("Reactivo limitante", "En 2 H2 + O2 → 2 H2O hay 8 mol de H2 y 3 mol de O2. ¿Cuál es el limitante y cuántos mol de agua se forman?", ["3 mol de O2 necesitan 6 mol de H2, y hay 8 mol.", "El O2 limita: forma 3 × 2 = 6 mol de H2O."], "El O2; se forman 6 mol de H2O"),
      ("Fotosíntesis a mol", "¿Cuántos mol de glucosa se forman con 12 mol de CO2 en 6 CO2 + 6 H2O → C6H12O6 + 6 O2?", ["La razón CO2 : glucosa es 6 : 1.", "Calculo 12 ÷ 6."], "2 mol"),
  ],
  mistakes=[
      ("Creer que el reactante con menos masa es siempre el limitante.", "El limitante depende de los mol y de la razón de coeficientes.", "Convierte a mol y compara con las razones."),
      ("Pensar que las plantas fabrican la glucosa del suelo.", "La glucosa se forma a partir del CO2 del aire y del agua, con luz.", "Revisa los reactantes de la ecuación."),
  ],
  rec=[
      ("¿Cómo se llama el reactante que se agota primero?", "Reactivo limitante", "Determina cuánto producto se forma."),
      ("¿Qué dos productos tiene la fotosíntesis?", "Glucosa y oxígeno", "C6H12O6 y O2."),
      ("Verdadero o falso: la fotosíntesis necesita luz.", "Verdadero", "La luz aporta la energía."),
  ],
  und=[
      ("En 6 CO2 + 6 H2O → C6H12O6 + 6 O2, ¿cuántos mol de O2 se forman por cada mol de glucosa?", "6", "La razón glucosa : O2 es 1 : 6."),
      ("En 2 H2 + O2 → 2 H2O hay 4 mol de H2 y 3 mol de O2. ¿Cuál es el limitante?", "El H2", "4 mol de H2 necesitan solo 2 mol de O2."),
      ("Una gráfica de masa de producto frente a masa de reactante es una recta que parte del origen. ¿Qué indica?", "Que son proporcionales", "Al duplicar una, la otra se duplica."),
  ],
  app=[
      arith("¿Cuántos gramos de glucosa se forman con 18 mol de CO2 (razón CO2 : glucosa de 6 : 1; M glucosa = 180)?", "18/6*180", "Se obtienen 3 mol de glucosa y se multiplican por 180 g/mol.", " g"),
      ("En 2 H2 + O2 → 2 H2O hay 5 mol de H2 y 4 mol de O2. ¿Cuántos mol de H2O se forman?", "5 mol", "5 mol de H2 necesitan solo 2,5 mol de O2: el H2 limita y forma 5 mol de H2O."),
      arith("¿Cuántos mol de CO2 se fijan para formar 3 mol de glucosa?", "3*6", "La razón glucosa : CO2 es 1 : 6.", " mol"),
  ],
  rea=[
      ("Una estudiante dice: «Si aumento la luz sin límite, la planta forma glucosa sin límite». ¿Qué respuesta es correcta? A) No: también depende de la cantidad de CO2 y agua disponibles, que pueden limitar la reacción B) Sí: la luz es el único factor", "A", "Un reactante puede ser limitante."),
      ("Una receta usa 2 panes y 1 queso por sándwich. Tienes 12 panes y 5 quesos. ¿Cuál es el ingrediente limitante?", "El queso", "Con 5 quesos solo se arman 5 sándwiches y sobran 2 panes."),
  ],
  cha=[
      ("Con la receta de 2 panes y 1 queso por sándwich, tienes 7 panes y 5 quesos. ¿Cuántos sándwiches armas y qué ingrediente limita?", "3 sándwiches; limita el pan", "Con 7 panes solo se arman 3 sándwiches y sobran 1 pan y 2 quesos."),
      arith("Si 264 g de CO2 forman 180 g de glucosa, ¿cuántos gramos de glucosa se forman con 528 g de CO2?", "528/264*180", "Es el doble de CO2, así que se forma el doble de glucosa.", " g"),
  ],
  context=[arith("Un árbol de ejemplo forma 360 g de glucosa. Si 180 g de glucosa liberan 192 g de O2, ¿cuántos gramos de O2 libera?", "360/180*192", "Es el doble de glucosa, así que libera el doble de oxígeno.", " g")],
  selfcheck=[("¿Qué es el reactivo limitante?", "El reactante que se agota primero", "Determina la cantidad de producto."), ("Escribe la ecuación de la fotosíntesis.", "6 CO2 + 6 H2O → C6H12O6 + 6 O2", "Con luz y clorofila."), ("¿Para qué sirve la glucosa a los seres vivos?", "Como alimento y como materia para formar otras sustancias", "Su energía se libera en la respiración.")],
  open_task=task("Con 6 CO2 + 6 H2O → C6H12O6 + 6 O2: (a) cuenta los átomos de C, H y O de cada lado; (b) calcula la masa de los reactantes y la de los productos (CO2 = 44, H2O = 18, glucosa = 180, O2 = 32 g/mol); (c) calcula cuántos gramos de glucosa y de O2 se forman con 528 g de CO2; (d) escribe dos frases sobre la importancia de la glucosa y del oxígeno para los seres vivos.", "(a) C 6 y 6; H 12 y 12; O 18 y 18. (b) 372 g y 372 g. (c) 528 g de CO2 son 12 mol; forman 2 mol de glucosa = 360 g y 12 mol de O2 = 384 g; 528 + 216 de agua = 744 = 360 + 384. (d) La glucosa es alimento y materia; el oxígeno se usa en la respiración celular.", ["conteo de átomos", "372 g en ambos lados", "360 g y 384 g", "dos frases sobre su importancia"], ["conteo, cálculos y frases"], ["olvidar el agua al verificar la masa", "decir que la planta toma la glucosa del suelo"], "Pregunta qué ocurre en la respiración celular con la glucosa y el oxígeno."),
  reinforce="Escribe los reactantes y los productos de la fotosíntesis.",
  extend="Explica con la ecuación de la fotosíntesis por qué una planta sin luz deja de formar glucosa.")

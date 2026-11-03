"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 06 (nutrientes, alimentos y salud)."""
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


OA6 = "CN08 OA 06"

L(OA6, 1,
  materials="Este cuaderno y lápiz. Opcional: hojas de papel absorbente o servilletas y alimentos de la cocina (una galleta, un trozo de pan, un poco de aceite), con una persona de tu casa cerca. No pruebes alimentos a los que seas alérgico.",
  use="Aprenderé qué nutrientes tienen los alimentos, qué hace cada uno y a plantear preguntas investigables sobre ellos. Sirve para entender por qué el cuerpo necesita alimentos distintos.",
  prior=["Sé que los alimentos se digieren y los nutrientes pasan a la sangre.", "Sé distinguir variable independiente y dependiente."],
  explain=[
      "Los nutrientes son sustancias de los alimentos que el cuerpo usa. Hay seis grupos. Los carbohidratos (almidón y azúcares) dan energía rápida. Las proteínas construyen y reparan tejidos y forman enzimas y anticuerpos. Las grasas guardan energía, aíslan del frío y ayudan a absorber algunas vitaminas. Las vitaminas y los minerales, en cantidades pequeñas, ayudan a regular funciones. El agua disuelve y transporta sustancias y regula la temperatura.",
      "Los alimentos tienen mezclas de nutrientes. El pan tiene muchos carbohidratos; los huevos y las legumbres, proteínas; el aceite y la palta, grasas; las frutas, vitaminas y agua. Una investigación casera puede detectar grasa: se frota un alimento sobre papel absorbente, y si deja una mancha translúcida que no se va al secar, el alimento contiene grasa.",
      "Una pregunta investigable sobre nutrientes indica qué se observa o se mide. «¿Qué alimento deja una mancha de grasa más grande en un papel absorbente: la palta o la manzana?» es investigable. «¿Cuál alimento es el más rico?» no lo es. Al investigar, la variable que se cambia es el alimento y la que se mide es el tamaño de la mancha en centímetros.",
  ],
  vocab=[("nutriente", "sustancia de los alimentos que el cuerpo usa"), ("carbohidrato", "nutriente que da energía, como el almidón y los azúcares"), ("proteína", "nutriente que construye y repara tejidos"), ("grasa", "nutriente que guarda energía y aísla"), ("mineral", "nutriente inorgánico necesario en pequeña cantidad")],
  worked=[
      ("Nutriente principal", "Un alimento es rico en almidón. ¿Qué nutriente predomina y para qué lo usa el cuerpo?", ["El almidón es un carbohidrato.", "Los carbohidratos dan energía."], "Carbohidratos, para obtener energía"),
      ("Pregunta investigable", "¿Es investigable «¿Deja el pan una mancha de grasa en el papel?»?", ["Pregunto si se puede observar.", "Se puede ver si aparece una mancha translúcida."], "Sí, porque se contesta observando el papel"),
  ],
  mistakes=[
      ("Pensar que todos los alimentos tienen solo un nutriente.", "Casi todos tienen mezclas de varios.", "Identifica el que predomina."),
      ("Creer que las vitaminas dan energía.", "Regulan funciones; la energía viene de carbohidratos, grasas y proteínas.", "Recuerda su función reguladora."),
  ],
  rec=[
      ("¿Qué nutriente repara los tejidos: las proteínas o los carbohidratos?", "Las proteínas", "Construyen y reparan tejidos."),
      ("¿Qué nutriente da energía rápida: los carbohidratos o los minerales?", "Los carbohidratos", "El cuerpo los usa como fuente principal de energía."),
      ("Verdadero o falso: el agua es un nutriente.", "Verdadero", "Es uno de los seis grupos de nutrientes."),
  ],
  und=[
      ("¿Qué alimento es rico en proteínas? A) Huevo; B) Cucharada de azúcar.", "A", "El huevo tiene proteínas; el azúcar es carbohidrato."),
      ("¿Para qué sirven las grasas? A) Guardar energía y aislar del frío; B) Construir hemoglobina.", "A", "Esa es su función principal."),
      ("Una mancha translúcida que no se va al secar en un papel indica ¿qué nutriente?", "Grasa", "La grasa deja una mancha que atraviesa el papel."),
  ],
  app=[
      ("¿Cuál pregunta es investigable? A) ¿Qué alimento deja una mancha de grasa mayor en un papel absorbente: la palta o la manzana? B) ¿Cuál alimento es el más rico?", "A", "Se contesta observando y midiendo."),
      ("En «¿Qué alimento deja una mancha mayor?», ¿qué variable se cambia?", "El alimento", "Se compara un alimento con otro."),
      ("En esa misma pregunta, ¿qué variable se mide?", "El tamaño de la mancha", "Es el resultado que se registra."),
  ],
  rea=[
      ("Alguien dice: «Si el pan no deja mancha de grasa, no tiene nutrientes». ¿Qué corrección haces? A) Solo muestra que tiene poca grasa; puede tener carbohidratos y otros; B) Significa que no se digiere.", "A", "La prueba detecta únicamente grasa."),
      ("Un compañero cambia el tipo de alimento y el tiempo de frotado a la vez. ¿Qué falla tiene su prueba?", "Cambió dos variables y no sabrá cuál causó el resultado", "Una prueba justa cambia solo una variable."),
  ],
  cha=[
      arith("Datos de ejemplo: la mancha de la palta mide 5 cm de ancho y la de la manzana 1 cm. ¿Cuántos cm más ancha es la de la palta?", "5-1", "Se resta la mancha menor a la mayor."),
      ("Un alimento de ejemplo tiene 20 g de proteínas, 30 g de carbohidratos y 10 g de grasa en 100 g. ¿Cuál nutriente predomina? A) Carbohidratos; B) Proteínas.", "A", "30 g es el valor mayor."),
  ],
  context=[arith("Una persona de ejemplo come 3 porciones de un alimento con 15 g de carbohidratos cada una. ¿Cuántos gramos de carbohidratos consume?", "3*15", "Se multiplica por el número de porciones.")],
  selfcheck=[("¿Cuáles son los seis grupos de nutrientes?", "Carbohidratos, proteínas, grasas, vitaminas, minerales y agua", "Cada uno cumple una función."), ("¿Qué hacen las proteínas?", "Construyen y reparan tejidos", "También forman enzimas y anticuerpos."), ("¿Cómo se detecta grasa con papel?", "Se frota el alimento y queda una mancha translúcida", "La grasa atraviesa el papel.")],
  open_task=task("Con estos tres alimentos de ejemplo (aceite, pan, huevo duro) escribe: qué nutriente predomina en cada uno, para qué lo usa el cuerpo y una pregunta investigable que compare dos de ellos con el papel absorbente.", "Aceite: grasa; guarda energía. Pan: carbohidratos; da energía. Huevo duro: proteínas; construye tejidos. Pregunta: ¿Qué deja una mancha más grande en un papel, el aceite o el pan?", ["tres nutrientes correctos", "funciones correctas", "pregunta que dice qué se mide"], ["tres frases y una pregunta"], ["decir que el pan es una proteína", "una pregunta de opinión"], "Pregunta qué pasaría si se frota el huevo en vez del pan."),
  reinforce="Escribe un alimento rico en cada nutriente: carbohidratos, proteínas y grasas.",
  extend="Explica por qué un alimento puede tener más de un nutriente.")

L(OA6, 2,
  materials="Este cuaderno y lápiz. Las etiquetas están escritas en cada ejercicio y son de ejemplo, no de marcas reales.",
  use="Aprenderé a leer una etiqueta nutricional y los sellos «ALTO EN» para comparar alimentos. Sirve para elegir con información.",
  prior=["Sé qué hacen los nutrientes.", "Sé calcular porcentajes y comparar valores."],
  explain=[
      "Una etiqueta nutricional muestra cuánto hay de cada nutriente en 100 g del alimento y en una porción. Informa la energía en kilocalorías (kcal), las proteínas, las grasas totales, los carbohidratos, los azúcares totales y el sodio. Para comparar dos alimentos conviene usar siempre la misma base, por ejemplo 100 g, porque las porciones pueden ser distintas.",
      "En Chile, los alimentos con mucha azúcar, sodio, grasas saturadas o energía llevan un sello negro de «ALTO EN». Un sello advierte que el alimento supera el límite para ese nutriente; no dice que sea imposible comerlo, pero sí que conviene moderarlo. Una etiqueta de ejemplo: galleta X, por 100 g: 480 kcal, 6 g de proteínas, 20 g de grasas, 68 g de carbohidratos y 450 mg de sodio.",
      "Al examinar una etiqueta se separa el dato de la conclusión. El dato es «20 g de grasas por 100 g»; la conclusión, «es alta en grasas», depende del criterio que se use. Para decidir, se comparan dos alimentos con el mismo criterio. Una limitación es que la etiqueta no dice cuánto se come en realidad.",
  ],
  vocab=[("etiqueta nutricional", "tabla que informa los nutrientes de un alimento"), ("porción", "cantidad de alimento que se suele comer de una vez"), ("kilocaloría (kcal)", "unidad de energía de los alimentos"), ("sello «ALTO EN»", "advertencia negra que indica exceso de azúcares, sodio, grasas saturadas o energía"), ("base de comparación", "cantidad común, como 100 g, para comparar alimentos")],
  worked=[
      ("Comparar en la misma base", "Alimento P tiene 12 g de grasa en 100 g; alimento Q tiene 8 g de grasa en 100 g. ¿Cuál tiene más grasa?", ["Ambos están por 100 g.", "12 es mayor que 8."], "El alimento P"),
      ("Total por porción", "Una porción de 30 g de un alimento con 10 g de azúcar por 100 g, ¿cuántos gramos de azúcar tiene?", ["Por cada 100 g hay 10 g de azúcar.", "En 30 g hay 30 × 10 ÷ 100 = 3 g."], "3 g de azúcar"),
  ],
  mistakes=[
      ("Comparar dos alimentos con bases distintas.", "Una porción de 30 g y otra de 100 g no son comparables.", "Usa la columna «por 100 g»."),
      ("Pensar que un sello negro prohíbe el alimento.", "Es una advertencia para moderar su consumo.", "Interpreta el sello como información."),
  ],
  rec=[
      ("¿En qué unidad se mide la energía de los alimentos: en kilocalorías o en gramos?", "En kilocalorías", "La energía se mide en kcal."),
      ("¿Qué indica un sello negro «ALTO EN»?", "Que el alimento tiene mucho de un nutriente", "Es una advertencia sobre azúcares, sodio, grasas saturadas o energía."),
      ("Verdadero o falso: para comparar alimentos conviene usar la misma base, como 100 g.", "Verdadero", "Así las cantidades son comparables."),
  ],
  und=[
      ("¿Cuál es un dato y cuál una conclusión? «20 g de grasas por 100 g» y «es muy grasoso». ¿Cuál es el dato?", "20 g de grasas por 100 g", "Se mide; la otra es una valoración."),
      ("¿Por qué conviene usar 100 g y no la porción para comparar? A) Porque las porciones pueden ser distintas; B) Porque 100 g es siempre una porción.", "A", "La base común evita comparar cantidades diferentes."),
      ("¿Qué limitación tiene una etiqueta?", "No dice cuánto se come en realidad", "Solo informa por porción o por 100 g."),
  ],
  app=[
      ("Etiqueta de ejemplo por 100 g: galleta X, 20 g de grasa; galleta Y, 12 g de grasa. ¿Cuál tiene más grasa? Escribe X o Y.", "X", "20 g es mayor que 12 g."),
      arith("Una galleta X tiene 480 kcal por 100 g. ¿Cuántas kcal aportan 50 g?", "480*50//100", "Se calcula la mitad de 100 g."),
      arith("Una bebida de ejemplo tiene 10 g de azúcar por 100 mL. ¿Cuántos gramos de azúcar tienen 250 mL?", "10*250//100", "Se multiplica por 250 y se divide por 100."),
  ],
  rea=[
      ("Alguien afirma: «El alimento A tiene más sodio que B porque su porción es mayor». ¿Qué falla ve? A) Comparó porciones distintas, no la misma base; B) No hay sodio en los alimentos.", "A", "Hay que comparar por 100 g."),
      ("Dos cereales de ejemplo: C1 tiene 10 g de azúcar por 100 g y C2 tiene 25 g por 100 g. ¿Cuál es más probable que lleve sello «ALTO EN azúcares»?", "C2", "Tiene la mayor cantidad de azúcar."),
  ],
  cha=[
      ("Un compañero dice: «Si no tiene sello, puedo comerlo sin límite». ¿Qué respuesta es correcta? A) El sello advierte solo sobre ciertos nutrientes; igual conviene variar y moderar; B) Sin sello no tiene nutrientes.", "A", "La ausencia de sello no garantiza una alimentación equilibrada."),
      arith("Dos galletas de ejemplo: la X aporta 480 kcal por 100 g y la Z 420 kcal por 100 g. ¿Cuántas kcal más aporta la X en 200 g?", "(480-420)*2", "Se calcula la diferencia por 100 g y se duplica."),
  ],
  context=[arith("Un jugo de ejemplo declara 8 g de azúcar por 100 mL. Una persona toma 300 mL. ¿Cuántos gramos de azúcar consume?", "8*300//100", "Se multiplica por 3 los 8 g.")],
  selfcheck=[("¿Para qué sirve la columna «por 100 g»?", "Para comparar alimentos en la misma base", "Evita porciones distintas."), ("¿Qué advierte un sello «ALTO EN» en un envase?", "Que supera el límite de un nutriente", "Pide moderar el consumo."), ("¿Qué no puede informar una etiqueta sobre tu consumo?", "No dice cuánto se come en realidad", "El consumo depende de la persona.")],
  open_task=task("Con estas dos etiquetas de ejemplo por 100 g: pan (260 kcal, 9 g de proteínas, 3 g de grasa, 50 g de carbohidratos, 500 mg de sodio) y galleta (480 kcal, 6 g de proteínas, 20 g de grasa, 68 g de carbohidratos, 450 mg de sodio), haz una tabla comparativa, indica cuál tiene más energía y más grasa, y escribe una limitación de la comparación.", "Más energía y más grasa: la galleta. Más proteínas: el pan. Limitación: no se sabe cuánto se come de cada uno.", ["tabla con los dos alimentos", "dos conclusiones correctas", "una limitación"], ["tabla y frases"], ["comparar en distinta base", "olvidar la limitación"], "Pregunta qué cambiaría si la porción fuera distinta."),
  reinforce="Escribe tres datos que aparecen en una etiqueta nutricional.",
  extend="Explica por qué el sello «ALTO EN» no es lo mismo que «prohibido».")

L(OA6, 3,
  materials="Este cuaderno y lápiz. Todas las listas están escritas en los ejercicios.",
  use="Aprenderé a construir un modelo que clasifica los nutrientes según su función y a contrastarlo con la realidad. Sirve para explicar qué aporta cada alimento al cuerpo.",
  prior=["Sé las funciones principales de los nutrientes.", "Sé leer una etiqueta nutricional."],
  explain=[
      "Un modelo útil clasifica los nutrientes por su función principal. Los energéticos dan energía: carbohidratos y grasas. Los constructores forman y reparan el cuerpo: proteínas y minerales como el calcio de los huesos. Los reguladores ayudan a que el cuerpo funcione bien: vitaminas, minerales y agua. Con este modelo se puede explicar qué aporta un alimento.",
      "El modelo tiene límites. Las proteínas también pueden dar energía cuando faltan los carbohidratos, y el agua es parte de los tejidos. Un mismo nutriente puede tener más de una función. Por eso el modelo simplifica: muestra la función principal, pero no todas.",
      "Contrastar el modelo es comparar sus predicciones con la realidad. Si un alimento tiene muchas grasas y carbohidratos, el modelo predice que aporta mucha energía, y eso se comprueba en su etiqueta. Si algo no calza, el modelo se corrige. Un plato equilibrado combina los tres tipos de funciones.",
  ],
  vocab=[("energético", "nutriente cuya función principal es dar energía"), ("constructor", "nutriente que forma y repara tejidos"), ("regulador", "nutriente que ayuda a regular las funciones del cuerpo"), ("función principal", "tarea más importante de un nutriente"), ("plato equilibrado", "comida que combina distintos tipos de nutrientes")],
  worked=[
      ("Clasificar", "Clasifica: carbohidratos, proteínas, vitaminas. ¿Cuál es energético, cuál constructor y cuál regulador?", ["Carbohidratos dan energía.", "Proteínas construyen tejidos.", "Vitaminas regulan funciones."], "Carbohidratos energéticos; proteínas constructores; vitaminas reguladores"),
      ("Predecir con el modelo", "Un alimento tiene mucha grasa y mucho almidón. ¿Qué predice el modelo sobre su energía?", ["Grasa y carbohidratos son energéticos.", "Entonces aporta mucha energía."], "Mucha energía"),
  ],
  mistakes=[
      ("Creer que cada nutriente tiene una sola función.", "El modelo muestra la principal, pero hay otras.", "Recuerda que el modelo simplifica."),
      ("Pensar que un plato equilibrado tiene solo un tipo de alimento.", "Necesita energéticos, constructores y reguladores.", "Combina varios grupos."),
  ],
  rec=[
      ("¿Qué tipo de nutriente es la proteína en el modelo: energético, constructor o regulador?", "Constructor", "Forma y repara tejidos."),
      ("¿Qué nutrientes son reguladores: las vitaminas o las grasas?", "Las vitaminas", "Ayudan a regular las funciones."),
      ("Verdadero o falso: el modelo de funciones tiene límites.", "Verdadero", "Simplifica la realidad."),
  ],
  und=[
      ("¿Dónde se clasifica el calcio del hueso? A) Constructor; B) Energético.", "A", "Forma parte de los huesos."),
      ("¿Por qué el modelo es una simplificación? A) Porque un nutriente puede tener más de una función; B) Porque los nutrientes no existen.", "A", "Las proteínas también pueden dar energía."),
      ("¿Qué combina un plato equilibrado?", "Nutrientes energéticos, constructores y reguladores", "Así cubre las distintas funciones."),
  ],
  app=[
      ("Cuatro nutrientes: carbohidratos, grasas, proteínas, agua. Según la clasificación por función principal de esta clase, ¿cuántos son energéticos?", "2", "Los carbohidratos y las grasas."),
      ("Un plato de ejemplo tiene arroz, lentejas y ensalada con aceite. ¿Cuál aporta mayoritariamente proteínas? A) Lentejas; B) Arroz.", "A", "Las lentejas son legumbres ricas en proteínas."),
      ("Con el mismo plato (arroz, lentejas y ensalada con aceite), ¿qué ingrediente aporta mayoritariamente grasa?", "El aceite", "El aceite es casi totalmente grasa."),
  ],
  rea=[
      ("Un estudiante dice: «Si un alimento no tiene proteínas, no sirve para nada». ¿Qué corrección corresponde según el modelo? A) Puede aportar energía o reguladores; B) No aporta ningún nutriente.", "A", "Cada grupo cumple funciones distintas."),
      ("Cuando faltan carbohidratos, una persona de ejemplo usa proteínas como energía. ¿Qué límite del modelo muestra esto?", "Que una proteína también puede cumplir una función energética", "Un nutriente puede tener más de una función."),
  ],
  cha=[
      ("Dos desayunos de ejemplo: D1 con pan y mermelada; D2 con pan, huevo y una fruta. ¿Cuál cubre mejor los tres tipos de nutrientes? Escribe D1 o D2.", "D2", "Tiene energía, proteínas y vitaminas."),
      ("Se propone un modelo de ejemplo donde el agua se considera «relleno sin función». ¿Qué evidencia lo contradice? A) El agua transporta sustancias y regula la temperatura; B) El agua tiene muchas calorías.", "A", "El agua cumple funciones esenciales."),
  ],
  context=[("Una deportista de ejemplo prepara un almuerzo con pasta, pollo y verduras. ¿Qué función aportan principalmente las verduras en este modelo?", "Reguladora", "Aportan vitaminas, minerales y agua.")],
  selfcheck=[("¿Cómo se clasifican los nutrientes en el modelo?", "Energéticos, constructores y reguladores", "Según su función."), ("¿Qué límite tiene el modelo?", "Simplifica: un nutriente puede tener varias funciones", "No muestra todo."), ("¿Qué es un plato equilibrado?", "Uno que combina los tres tipos de nutrientes", "Cubre todas las funciones.")],
  open_task=task("Construye una tabla de tres columnas (energéticos, constructores, reguladores) con dos nutrientes en cada una y un alimento de ejemplo para cada uno. Después escribe una frase con un límite del modelo.", "Energéticos: carbohidratos (pan), grasas (aceite). Constructores: proteínas (huevo), calcio (leche). Reguladores: vitaminas (naranja), agua (sopa). Límite: las proteínas también pueden dar energía.", ["seis nutrientes bien ubicados", "un alimento por nutriente", "un límite declarado"], ["tabla y una frase"], ["poner proteínas como reguladores", "olvidar el límite"], "Pregunta qué cambiaría si faltara una columna."),
  reinforce="Escribe un alimento energético, uno constructor y uno regulador.",
  extend="Explica por qué un modelo útil muestra la función principal pero no todas.")

L(OA6, 4,
  materials="Este cuaderno, lápiz y calculadora si quieres. Los datos son de ejemplo.",
  use="Aprenderé a relacionar los gramos de cada nutriente con la energía que aportan y con el agua de los alimentos. Sirve para calcular y comparar el aporte energético.",
  prior=["Sé leer etiquetas.", "Sé multiplicar y sumar números enteros."],
  explain=[
      "Los nutrientes aportan energía según su masa. En promedio, 1 g de carbohidratos aporta 4 kcal, 1 g de proteínas aporta 4 kcal y 1 g de grasas aporta 9 kcal. Las vitaminas, los minerales y el agua no aportan energía. Por eso la energía de un alimento se calcula multiplicando los gramos de cada nutriente por su valor y sumando.",
      "Por ejemplo, 100 g de un alimento con 50 g de carbohidratos, 10 g de proteínas y 5 g de grasas aportan 50 × 4 + 10 × 4 + 5 × 9 = 200 + 40 + 45 = 285 kcal. Eso permite comparar alimentos: con la misma masa, el que tiene más grasa suele aportar más energía.",
      "Otra variable es el agua. Una fruta fresca tiene mucha agua y poca energía por 100 g; si se seca, pierde agua y la misma masa concentra más nutrientes. Las relaciones que se miden son: más gramos de un nutriente, más energía; menos agua, más concentración. Una limitación es que estas cifras son promedios y no consideran la digestión.",
  ],
  vocab=[("kcal por gramo", "energía que aporta cada gramo de un nutriente"), ("concentración", "cantidad de una sustancia por cada 100 g del alimento"), ("alimento fresco", "alimento con su agua natural"), ("alimento seco", "alimento que perdió gran parte de su agua"), ("promedio", "valor medio que sirve de referencia")],
  worked=[
      ("Energía de un alimento", "100 g de un alimento tienen 30 g de carbohidratos, 20 g de proteínas y 10 g de grasa. ¿Cuántas kcal aportan?", ["Carbohidratos: 30 × 4 = 120.", "Proteínas: 20 × 4 = 80.", "Grasas: 10 × 9 = 90; suma 120 + 80 + 90 = 290."], "290 kcal"),
      ("Efecto del agua", "Una uva pesa 10 g y tiene 8 g de agua. Si se seca y pierde casi toda el agua, ¿su masa aumenta o disminuye?", ["El agua era 8 de 10 g.", "Al perderla, la masa baja."], "Disminuye; los nutrientes quedan más concentrados"),
  ],
  mistakes=[
      ("Pensar que 1 g de grasa aporta lo mismo que 1 g de carbohidratos.", "La grasa aporta 9 kcal por gramo y el carbohidrato 4.", "Usa el valor de cada nutriente."),
      ("Contar energía del agua o de las vitaminas.", "No aportan energía.", "Calcula solo con carbohidratos, proteínas y grasas."),
  ],
  rec=[
      ("¿Cuántas kcal aporta 1 g de grasa: 4 o 9?", "9", "La grasa aporta más energía por gramo."),
      ("¿Cuántas kcal aporta 1 g de carbohidratos?", "4", "Es el valor promedio."),
      ("Verdadero o falso: el agua aporta energía.", "Falso", "No tiene kcal."),
  ],
  und=[
      ("¿Por qué 10 g de grasa aportan más energía que 10 g de proteínas? A) Porque la grasa aporta 9 kcal por gramo y la proteína 4; B) Porque la grasa pesa más.", "A", "El valor energético por gramo es mayor."),
      ("¿Qué nutrientes no aportan energía?", "Vitaminas, minerales y agua", "Regulan funciones, pero no dan kcal."),
      ("Al secar una fruta, ¿qué pasa con la concentración de nutrientes? A) Aumenta; B) Disminuye.", "A", "Hay menos agua en la misma masa."),
  ],
  app=[
      arith("Un alimento tiene 25 g de carbohidratos, 5 g de proteínas y 10 g de grasas en una porción. ¿Cuántas kcal aporta?", "25*4+5*4+10*9", "Se multiplican los gramos por su valor y se suman."),
      arith("Una porción de nueces tiene 14 g de grasa. ¿Cuántas kcal provienen solo de la grasa?", "14*9", "Se multiplican los gramos de grasa por 9."),
      arith("Un panqueque aporta 160 kcal de ejemplo. Una persona come 3. ¿Cuántas kcal consume?", "160*3", "Se multiplica por el número de panqueques."),
  ],
  rea=[
      ("Un estudiante dice: «100 g de una manzana tienen más energía que 100 g de nueces porque la manzana pesa más». ¿Qué falla ve? A) Ambos son 100 g; las nueces tienen más grasa, que aporta más kcal por gramo; B) La manzana no tiene agua.", "A", "Con la misma masa, la grasa de las nueces aporta más energía."),
      ("Explica en una frase por qué las pasas aportan más energía que las uvas frescas en 100 g.", "Porque tienen menos agua y más azúcares concentrados", "Al perder agua, la masa concentra nutrientes."),
  ],
  cha=[
      arith("Alimento P: 40 g de carbohidratos y 10 g de proteínas por 100 g. Alimento Q: 20 g de carbohidratos, 10 g de proteínas y 10 g de grasas por 100 g. ¿Cuántas kcal más aporta Q que P?", "(20*4+10*4+10*9)-(40*4+10*4)", "Se calcula la energía de cada uno y se resta."),
      ("Con esos valores, ¿qué nutriente explica la diferencia entre P y Q? A) La grasa de Q; B) Los carbohidratos de P.", "A", "La grasa aporta 9 kcal por gramo."),
  ],
  context=[arith("Una persona de ejemplo come 150 g de papas cocidas que aportan 80 kcal por 100 g. ¿Cuántas kcal consume?", "80*150//100", "Se calcula la proporción de 100 g.")],
  selfcheck=[("¿Cuántas kcal aporta 1 g de proteínas?", "4", "Igual que los carbohidratos."), ("¿Cómo se calcula la energía de un alimento?", "Multiplicando los gramos de cada nutriente por su valor y sumando", "Solo con carbohidratos, proteínas y grasas."), ("¿Qué pasa al perder agua?", "Los nutrientes se concentran", "Hay menos agua en la misma masa.")],
  open_task=task("Calcula y compara la energía de 100 g de dos alimentos de ejemplo: R (55 g de carbohidratos, 8 g de proteínas, 2 g de grasa) y S (10 g de carbohidratos, 20 g de proteínas, 25 g de grasa). Muestra los cálculos y explica qué nutriente hace la diferencia.", "R: 55×4 + 8×4 + 2×9 = 220 + 32 + 18 = 270 kcal. S: 10×4 + 20×4 + 25×9 = 40 + 80 + 225 = 345 kcal. La diferencia la hace la grasa de S (9 kcal por gramo).", ["dos cálculos correctos", "usa 4, 4 y 9 kcal por gramo", "explica la causa"], ["cálculos y frase"], ["usar 4 kcal para la grasa", "sumar el agua"], "Pregunta cuánta energía aportarían 50 g de cada uno."),
  reinforce="Calcula las kcal de 10 g de carbohidratos y de 10 g de grasa.",
  extend="Explica por qué dos alimentos con la misma masa pueden aportar distinta energía.")

L(OA6, 5,
  materials="Este cuaderno y lápiz. Los casos son inventados y no corresponden a nadie real.",
  use="Aprenderé a explicar cómo la falta o el exceso de nutrientes afecta la salud. Sirve para relacionar lo que comemos con el funcionamiento del cuerpo.",
  prior=["Sé las funciones de los nutrientes.", "Sé leer datos en una tabla."],
  explain=[
      "La falta de un nutriente produce señales conocidas. La falta de vitamina C se relaciona con el escorbuto, porque se necesita para formar colágeno, una proteína de la piel y los vasos. La falta de hierro reduce la hemoglobina y causa anemia, con cansancio. La falta de vitamina D y de calcio debilita los huesos. La falta de yodo afecta la glándula tiroides.",
      "El exceso también daña. Mucha azúcar y grasa aportan más energía de la que se gasta y se relaciona con sobrepeso. Mucha sal (sodio) se relaciona con presión arterial alta. Las grasas saturadas en exceso se relacionan con depósitos en las arterias. Beber poca agua causa deshidratación, con sed, dolor de cabeza y orina oscura.",
      "Explicar un patrón significa unir una causa y un mecanismo. «Una dieta pobre en hierro baja la hemoglobina; sin hemoglobina se transporta menos oxígeno; por eso hay cansancio». Si alguien se siente mal o cree que le falta algún nutriente, debe consultar a un profesional de salud. Una tabla de ejemplo no sirve para diagnosticar a una persona.",
  ],
  vocab=[("carencia", "falta de un nutriente"), ("exceso", "cantidad mayor que la que el cuerpo necesita"), ("anemia", "disminución de la hemoglobina que causa cansancio"), ("deshidratación", "falta de agua en el cuerpo"), ("colágeno", "proteína que da firmeza a piel, vasos y huesos")],
  worked=[
      ("Causa y mecanismo", "¿Por qué la falta de hierro puede causar cansancio?", ["El hierro forma parte de la hemoglobina.", "Con menos hemoglobina se transporta menos oxígeno y hay cansancio."], "Porque se transporta menos oxígeno"),
      ("Leer un patrón", "En una tabla de ejemplo, 3 de 10 estudiantes con dietas bajas en hierro se sienten cansados y 1 de 10 con dietas altas en hierro. ¿Cuántas veces mayor es la proporción en la dieta baja?", ["3 de 10 contra 1 de 10.", "3 ÷ 1 = 3."], "3 veces mayor"),
  ],
  mistakes=[
      ("Diagnosticar una carencia solo por un síntoma.", "Un síntoma puede tener muchas causas.", "Consulta a un profesional de salud."),
      ("Creer que más cantidad de vitaminas siempre es mejor.", "El exceso de algunas puede hacer daño.", "Busca el equilibrio."),
  ],
  rec=[
      ("¿La falta de hierro causa anemia o escorbuto?", "Anemia", "El escorbuto se asocia a la falta de vitamina C."),
      ("¿Beber poca agua causa deshidratación: verdadero o falso?", "Verdadero", "El cuerpo pierde más agua de la que repone."),
      ("¿Qué mineral se necesita para fortalecer los huesos: el calcio o el yodo?", "El calcio", "Forma parte de los huesos."),
  ],
  und=[
      ("¿Qué nutriente se necesita para formar colágeno? A) Vitamina C; B) Vitamina D.", "A", "La vitamina C interviene en la síntesis de colágeno."),
      ("¿Por qué el exceso de sal se asocia a presión alta? A) Porque el sodio influye en el volumen y la presión de la sangre; B) Porque la sal tiene mucha grasa.", "A", "El sodio retiene agua en la sangre."),
      ("¿Qué se debe hacer si alguien cree tener una carencia? A) Consultar a un profesional de salud; B) Tomar muchos suplementos por su cuenta.", "A", "Un diagnóstico necesita evaluación profesional."),
  ],
  app=[
      ("Cuatro personas de ejemplo: P1 con cansancio y poca carne, P2 con mucha sal y presión alta, P3 con poca agua y dolor de cabeza, P4 con huesos débiles. ¿Cuántas se relacionan con un exceso?", "1", "Solo P2 se relaciona con exceso de sodio."),
      arith("Datos de ejemplo: de 40 estudiantes con dieta baja en hierro, 12 se sienten cansados. ¿Qué porcentaje es?", "12*100//40", "Se divide por el total y se multiplica por 100.", " %"),
      ("¿Qué alimento ayuda a aportar vitamina C? A) Naranja; B) Aceite.", "A", "Los cítricos son ricos en vitamina C."),
  ],
  rea=[
      ("Alguien dice: «Si una persona se siente cansada, seguro le falta hierro». ¿Qué corrección haces? A) El cansancio puede tener varias causas; hay que evaluarlo con un profesional; B) El cansancio siempre significa anemia.", "A", "Un síntoma no identifica una causa única."),
      ("Explica en una frase por qué la falta de calcio y vitamina D puede debilitar los huesos.", "Porque el calcio forma los huesos y la vitamina D ayuda a absorberlo", "Sin ellos, los huesos se mineralizan menos."),
  ],
  cha=[
      ("Una tabla de ejemplo indica que quienes toman más agua tienen orina más clara. ¿Qué mecanismo lo explica? A) El riñón elimina el exceso de agua y la orina se diluye; B) El agua se transforma en color.", "A", "Hay más agua en la orina."),
      ("Un cartel dice: «Los suplementos reemplazan una alimentación variada». ¿Por qué es una afirmación débil? A) Los alimentos aportan combinaciones de nutrientes que un suplemento no reemplaza; B) Los suplementos no existen.", "A", "Una dieta variada cubre varias funciones."),
  ],
  context=[("Una estudiante de ejemplo se siente cansada y su doctor le indica un examen de hemoglobina. ¿Qué relación se espera si le falta hierro? A) Hemoglobina baja; B) Hemoglobina alta.", "A", "El hierro es necesario para formarla.")],
  selfcheck=[("¿Qué provoca la falta de hierro?", "Anemia, con cansancio", "Baja la hemoglobina."), ("¿Qué se relaciona con exceso de sal?", "Presión arterial alta", "Afecta corazón y riñones."), ("¿Qué debes hacer si crees tener una carencia?", "Consultar a un profesional de salud", "No se diagnostica solo.")],
  open_task=task("Elige dos de estos casos de ejemplo y explica para cada uno la posible causa, el mecanismo y una recomendación general de alimentación: (a) cansancio y poca carne en la dieta; (b) encías sangrantes y pocas frutas; (c) presión alta y mucho consumo de sal. Termina con una frase que diga cuándo consultar a un profesional.", "(a) Posible causa: poco hierro; mecanismo: menos hemoglobina, menos oxígeno; recomendación: incluir legumbres y carnes. (b) Causa: poca vitamina C; mecanismo: menos colágeno; recomendación: incluir cítricos. Consultar a un profesional si los síntomas persisten.", ["dos casos con causa y mecanismo", "recomendación general", "frase sobre consultar"], ["dos explicaciones y una frase"], ["dar un diagnóstico", "olvidar el mecanismo"], "Pregunta qué otros datos harían falta para decidir."),
  reinforce="Escribe una carencia y una consecuencia para la salud.",
  extend="Explica por qué el exceso de algunos nutrientes puede ser tan dañino como su falta.")

"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 05 (alimentación variada y funciones corporales) y OA 06 (efectos del humo de tabaco)."""
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




OA5, OA6 = "CN05 OA 05", "CN05 OA 06"

# ---------------------------------------------------------------- OA 05
L(OA5, 1,
  materials="Este cuaderno y lápiz. Opcional: la lista de lo que comiste ayer, anotada sin juzgarla.",
  use="Aprenderé qué grupos de alimentos existen, para qué sirve cada uno y a separar lo que se observa de lo que se supone en un registro de comidas. Sirve para analizar una alimentación con datos.",
  prior=["Sé que el sistema digestivo transforma los alimentos.", "Sé separar observaciones de interpretaciones."],
  explain=[
      "Los alimentos se pueden agrupar según lo que aportan. Los cereales, el pan, el arroz y las papas dan energía para el movimiento. Las carnes, los pescados, los huevos y las legumbres, como las lentejas, ayudan al crecimiento y a la reparación del cuerpo, por ejemplo de los músculos y la piel. Los lácteos, las frutas y las verduras aportan vitaminas y minerales que ayudan al desarrollo y al buen funcionamiento del cuerpo. Los aceites y la palta aportan grasas, que también dan energía. En este cuaderno contamos seis grupos: cereales y papas; carnes, pescados, huevos y legumbres; lácteos; frutas; verduras; y aceites y grasas.",
      "Para analizar una alimentación miramos tres cosas. La variedad es cuántos grupos distintos se comen. El tamaño de las porciones es cuánto se come de cada alimento. La frecuencia es cuántas veces al día se come. En Chile se acostumbran cuatro comidas: desayuno, almuerzo, once y cena.",
      "Un registro de comidas es una observación: «Camila comió 4 veces». Decir «Camila come perfecto» es una interpretación, porque no se midió con un criterio. Esta clase no busca decir quién come bien o mal, sino aprender a describir una alimentación con datos.",
  ],
  vocab=[("variedad", "cantidad de grupos distintos de alimentos que se comen"), ("porción", "cantidad de un alimento que se come en una vez"), ("frecuencia", "cuántas veces se come en un día o una semana"), ("energía", "capacidad del cuerpo para moverse y funcionar"), ("legumbre", "alimento como lenteja, poroto o garbanzo")],
  worked=[
      ("Clasificar por grupo", "Clasifica: arroz, pollo, manzana, leche.", ["Arroz es un cereal.", "Pollo es una carne.", "Manzana es fruta y leche es un lácteo."], "Arroz: cereal. Pollo: carne. Manzana: fruta. Leche: lácteo"),
      ("Observación o interpretación", "«Camila comió 4 veces el lunes» y «Camila se alimenta perfecto». ¿Cuál es observación?", ["Pregunto qué frase se contó.", "Las 4 veces se cuentan en el registro.", "«Perfecto» necesita un criterio y no se midió."], "La primera frase"),
  ],
  mistakes=[
      ("Decir que un alimento sirve para todo el cuerpo por igual.", "Cada grupo aporta cosas distintas.", "Une cada alimento a lo que aporta."),
      ("Juzgar a una persona por su registro de un solo día.", "Un día no muestra toda su alimentación.", "Describe con datos y no con etiquetas."),
  ],
  rec=[
      ("El arroz, ¿es un cereal o una fruta?", "Un cereal", "Es un grano que aporta energía."),
      ("¿Qué alimentos ayudan al crecimiento y la reparación: las lentejas o los aceites?", "Las lentejas", "Las legumbres aportan proteínas."),
      ("Completa con «variedad» o «gusto»: cuántos grupos distintos se comen se llama ______.", "Variedad", "Es uno de los aspectos de la alimentación."),
  ],
  und=[
      ("¿Para qué sirven sobre todo el pan y el arroz?", "Para dar energía al cuerpo", "Los cereales aportan energía para el movimiento."),
      ("¿Qué comida del día se toma entre el almuerzo y la cena en Chile?", "La once", "Las cuatro comidas son desayuno, almuerzo, once y cena."),
      ("Marca la observación: A) Tomás comió 3 frutas el martes. B) Tomás se alimenta muy mal.", "A", "A se cuenta en un registro; B es un juicio."),
  ],
  app=[
      ("Menú: leche, pan, lentejas, arroz, lechuga. ¿Cuántos grupos distintos hay si los grupos son lácteos, cereales, carnes y legumbres, y verduras?", "4", "Leche es lácteo, pan y arroz son cereales, lentejas son legumbres y lechuga es verdura."),
      arith("Camila comió 2 frutas en el desayuno, 1 en la once y 1 en la cena. ¿Cuántas frutas comió en total?", "2+1+1", "Se suman las frutas de cada comida."),
      ("Clasifica el queso como cereal, lácteo o fruta.", "Lácteo", "El queso se hace con leche."),
  ],
  rea=[
      ("Raúl dice: «Si comí 4 veces, comí con variedad». ¿Es correcto? Responde Sí o No y explica.", "No; la frecuencia no es lo mismo que la variedad", "Puede haber comido 4 veces el mismo alimento."),
      ("Ema anota: «El jueves comí pan, arroz y papas». Dice: «Ese día no comí alimentos que den energía para el movimiento». ¿Es correcto? Responde Sí o No y explica.", "No; el pan, el arroz y las papas dan energía", "Los tres son alimentos que aportan energía."),
  ],
  cha=[
      ("Menú del miércoles de Tomás: desayuno, pan con huevo y leche; almuerzo, arroz con pollo y ensalada; once, un plátano; cena, fideos. Usando los grupos cereales, carnes y huevos, lácteos, frutas y verduras, ¿cuántos grupos distintos aparecen?", "5", "Pan, arroz y fideos son cereales; huevo y pollo son carne/huevo; leche es lácteo; plátano es fruta; ensalada es verdura."),
      ("¿Por qué conviene registrar varios días y no solo uno para analizar una alimentación?", "Porque un día no muestra lo que se come habitualmente", "Los menús cambian de un día a otro."),
  ],
  context=[("Dato de ejemplo. Un curso anotó cuántas frutas comieron 5 estudiantes ayer: 2, 1, 3, 0 y 2. ¿Cuántas frutas comieron entre los 5?", "8", "2 + 1 + 3 + 0 + 2 = 8.")],
  selfcheck=[("Nombra tres grupos de alimentos.", "Tres entre cereales, carnes y legumbres, lácteos, frutas y verduras, grasas", "Cada grupo aporta cosas distintas."), ("¿Qué es la variedad?", "La cantidad de grupos distintos de alimentos que se comen", "Es un aspecto de la alimentación."), ("¿«Come perfecto» es una observación? Responde Sí o No.", "No", "Es un juicio sin criterio medible.")],
  open_task=task("Con una persona de tu casa, anota lo que comiste ayer en cada comida (desayuno, almuerzo, once, cena) sin juzgarlo. Después clasifica cada alimento en un grupo de esta clase y escribe una observación y una interpretación sobre tu registro.", "Desayuno: leche y pan. Almuerzo: lentejas, arroz y ensalada. Once: fruta. Cena: huevo y papas. Grupos: 5 (lácteos, cereales, carnes y huevos, verduras y frutas). Observación: comí 4 veces. Interpretación: comí con harta energía.", ["registro de las cuatro comidas", "alimentos clasificados por grupo", "observación e interpretación diferenciadas"], ["tabla", "dos frases"], ["usar etiquetas como «bien» o «mal»", "olvidar alguna comida"], "Pregunta qué grupo apareció más veces y qué dato necesitaría para decir algo más general."),
  reinforce="Escribe seis alimentos que conozcas y clasifícalos en un grupo.",
  extend="Explica por qué una persona que juega mucho necesita alimentos que den energía.")

L(OA5, 2,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a hacer preguntas y predicciones sobre la variedad, la frecuencia y las porciones de una alimentación. Sirve para saber qué datos necesito para analizarla.",
  prior=["Sé los grupos de alimentos.", "Sé que una predicción lleva una razón."],
  explain=[
      "Una pregunta comprobable sobre alimentación se responde con un registro. Por ejemplo: «¿Cuántos grupos de alimentos aparecen en cada uno de los tres días?» o «¿Cuántas porciones de fruta y verdura hay cada día?». Una pregunta como «¿Qué comida es más rica?» no se puede comprobar con un registro.",
      "Una predicción dice lo que esperas y por qué: «El menú del lunes tendrá menos grupos que el del martes, porque el lunes solo hay pan y arroz». Para comprobarla comparas con el registro, usando el mismo criterio: contar grupos distintos. El tamaño de una porción también se puede describir; por ejemplo, una fruta mediana es una porción.",
      "Un registro de pocos días solo describe esos días. No sirve para afirmar lo que alguien come siempre. Si la predicción no se cumple, se corrige la idea. Nadie está en falta por tener un día distinto.",
  ],
  vocab=[("registro", "lista ordenada de lo que se observó o midió"), ("pregunta comprobable", "pregunta que se responde con un registro o una medición"), ("predicción", "lo que creo que pasará y por qué"), ("criterio", "característica que se mira igual en todos los casos"), ("porción mediana", "cantidad común de un alimento, como una fruta mediana")],
  worked=[
      ("Elegir la pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Cuántas frutas hay en cada menú de tres días? B) ¿Qué fruta es la más rica?", ["Pienso si se puede contar.", "En A cuento frutas en el registro.", "En B cada persona opina distinto."], "A"),
      ("Comprobar una predicción", "Predicción: «El lunes tendrá más grupos que el martes». Lunes: 4 grupos. Martes: 5 grupos. ¿Se cumplió?", ["Comparo 4 con 5.", "El lunes tiene menos grupos.", "La predicción no coincide."], "No se cumplió"),
  ],
  mistakes=[
      ("Predecir sin razón: «comerá mejor».", "No se puede comprobar porque «mejor» no tiene criterio.", "Cuenta grupos o porciones."),
      ("Concluir sobre toda la vida de una persona con un día de registro.", "Un día no basta.", "Di que el dato vale solo para ese día."),
  ],
  rec=[
      ("¿La predicción se hace antes o después de mirar el registro?", "Antes", "Es una idea previa que luego se comprueba."),
      ("¿Qué se cuenta para saber la variedad: grupos distintos o veces que se come?", "Grupos distintos", "La variedad es la cantidad de grupos."),
      ("Completa con «cuenta» o «opina»: una pregunta comprobable se responde cuando se ______ en un registro.", "Cuenta", "Un dato contado permite responder."),
  ],
  und=[
      ("¿Cuál es una buena razón para una predicción sobre el menú del lunes? A) Habrá pocos grupos porque solo hay pan y arroz. B) Habrá pocos grupos porque sí.", "A", "A da una razón basada en los alimentos."),
      ("¿Por qué conviene usar el mismo criterio para comparar tres días?", "Para que la comparación sea justa", "Si el criterio cambia, no se pueden comparar."),
      ("¿Qué pregunta se puede comprobar? A) ¿Cuántas porciones de verdura comió Ema el viernes? B) ¿Es lindo comer verdura?", "A", "Las porciones se cuentan en el registro."),
  ],
  app=[
      arith("Dato de ejemplo. El lunes hubo 4 grupos de alimentos y el martes 6. ¿Cuántos grupos más hubo el martes?", "6-4", "Se resta el valor menor al mayor."),
      arith("Dato de ejemplo. Ema comió 2 porciones de fruta el lunes, 3 el martes y 1 el miércoles. ¿Cuántas porciones de fruta comió en los tres días?", "2+3+1", "Se suman las porciones de cada día."),
      ("Marcos predijo que el jueves tendría más grupos que el miércoles. El miércoles tuvo 5 y el jueves 5. ¿Se cumplió su predicción? Responde Sí o No.", "No", "Hubo la misma cantidad, no más."),
  ],
  rea=[
      ("Pía contó grupos en el desayuno de un día y en todas las comidas de otro día. Dice: «El segundo día tuvo más variedad». ¿Qué problema tiene su comparación?", "Contó partes distintas del día", "El criterio debe ser igual en los dos días."),
      ("Hugo dice que como un solo día de registro le basta para saber cómo come siempre. ¿Tiene razón? Responde Sí o No y explica.", "No; un día no muestra lo habitual", "Los menús cambian de un día a otro."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre la frecuencia de comidas de una semana, indicando qué contarás.", "¿Cuántas comidas anotó Sofía cada día durante la semana?", "Nombra lo que se cuenta y el período."),
      ("Un registro muestra pan, pan y pan en tres comidas. Predice cuántos grupos de alimentos habrá en esas tres comidas y explica.", "Un grupo, porque todos son cereales", "Los tres alimentos pertenecen al mismo grupo."),
  ],
  context=[("Dato de ejemplo. Un curso anotó los grupos de alimentos del almuerzo de 6 estudiantes: 4, 3, 5, 4, 3 y 5. ¿Cuántos grupos sumaron en total?", "24", "4 + 3 + 5 + 4 + 3 + 5 = 24.")],
  selfcheck=[("¿Qué lleva una buena predicción?", "Lo que pasará y la razón", "Así se puede comprobar."), ("¿Para qué sirve un registro?", "Para tener datos que se puedan contar y comparar", "Permite responder preguntas con evidencia."), ("¿Un día de registro describe toda la alimentación? Responde Sí o No.", "No", "Solo describe ese día.")],
  open_task=task("Con una persona de tu casa, anota lo que comiste en tres días distintos (puedes usar los de esta semana). Cuenta cuántos grupos distintos hubo cada día. Antes de contar, escribe una predicción con razón sobre qué día tendrá más grupos.", "Predicción: el sábado tendrá más grupos porque ese día tengo más tiempo para almorzar con calma. Registro: lunes 4 grupos, martes 5, sábado 6. Conclusión: se cumplió; vale solo para esos tres días.", ["predicción con razón", "tres días de registro", "conclusión con los datos"], ["tabla con tres días", "frase de conclusión"], ["predecir sin razón", "decir que el registro vale para siempre"], "Pregunta qué día se pareció más a su predicción y por qué."),
  reinforce="Escribe una pregunta comprobable sobre porciones de fruta en una semana.",
  extend="Explica por qué dos personas distintas pueden tener registros distintos sin que alguna esté mal.")

L(OA5, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a usar un modelo del plato de comida para entender variedad y porciones y a decir qué no muestra. Sirve para organizar una comida con distintos alimentos.",
  prior=["Sé los grupos de alimentos.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo del plato de comida es un círculo dividido en partes. En este cuaderno usamos un modelo de ejemplo: la mitad del plato para frutas y verduras, un cuarto para cereales o papas y un cuarto para carnes, huevos o legumbres. Los lácteos y las grasas se agregan en cantidades pequeñas. Es un modelo de ejemplo de esta clase y no una regla oficial.",
  "El tamaño de la porción también se modela. Una forma simple es usar la mano: una porción de carne o pescado es del tamaño de la palma de tu mano, y una fruta mediana cabe en tu puño. Esto ayuda a comparar porciones sin balanza, pero es aproximado.",
      "Todo modelo tiene límites. Este plato no muestra cuánta energía necesita cada persona, ni las comidas del resto del día, ni los alimentos que una persona no puede comer por salud. Por eso se complementa con la orientación de un profesional de la salud.",
  ],
  vocab=[("modelo", "representación simple de algo real"), ("porción", "cantidad de un alimento que se come en una vez"), ("aproximado", "cercano al valor real pero no exacto"), ("plato", "círculo que representa una comida dividida en partes"), ("profesional de la salud", "persona formada para orientar sobre alimentación, como un nutricionista")],
  worked=[
      ("Leer el plato modelo", "El plato modelo tiene la mitad para frutas y verduras. Si el plato se divide en 4 partes iguales, ¿cuántas partes son para frutas y verduras?", ["La mitad de 4 es 2.", "Dos partes se llenan con frutas y verduras.", "Las otras dos se reparten entre cereales y proteínas."], "2 partes"),
      ("Encontrar un límite", "El plato modelo no dice cuánta energía necesita cada persona. ¿Es un límite?", ["Cada persona tiene necesidades distintas.", "El plato no las muestra.", "Eso real queda fuera del modelo."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Creer que el plato modelo es una regla para todas las personas.", "Es un ejemplo; cada persona tiene necesidades distintas.", "Escribe que es un ejemplo con límites."),
      ("Medir una porción con un tamaño distinto cada vez.", "Así no se puede comparar.", "Usa la misma medida, como la palma."),
  ],
  rec=[
      ("¿Qué grupo ocupa la mitad del plato modelo?", "Frutas y verduras", "Así lo indica el modelo de esta clase."),
      ("¿Con qué parte de la mano se mide una porción de carne en el modelo?", "Con la palma", "Se usa como medida aproximada."),
      ("Completa con «ejemplo» o «ley»: el plato modelo de esta clase es un ______.", "Ejemplo", "Sirve para entender, no es una regla."),
  ],
  und=[
      ("En el plato modelo, ¿qué parte ocupan los cereales o las papas?", "Un cuarto", "El modelo los ubica en un cuarto del plato."),
      ("¿Por qué el modelo dice que las porciones son aproximadas?", "Porque las manos son de distinto tamaño", "La mano es una medida que varía."),
      ("¿Qué muestra mejor la variedad de una comida? A) Un plato con una sola parte. B) Un plato dividido en varios grupos.", "B", "Varias partes muestran más grupos."),
  ],
  app=[
      ("Un plato modelo se divide en 8 partes iguales. La mitad es para frutas y verduras. ¿Cuántas partes son?", "4", "La mitad de 8 es 4."),
      arith("Un plato modelo tiene 8 partes: 4 de frutas y verduras, 2 de cereales y el resto de proteínas. ¿Cuántas partes son de proteínas?", "8-4-2", "Se resta lo ocupado al total."),
      ("Un almuerzo tiene arroz, pollo, ensalada y fruta. En el plato modelo, ¿cuántos grupos distintos aparecen si cuentas cereal, carne, verdura y fruta?", "4", "Hay un alimento de cada uno de esos grupos."),
  ],
  rea=[
      ("Luis dice que el plato modelo es una ley que todos deben seguir exactamente. ¿Tiene razón? Responde Sí o No y explica.", "No; es un ejemplo que no muestra las necesidades de cada persona", "Todo modelo simplifica."),
      ("Un plato lleno de pasta y un plato con pasta, verduras y huevo. ¿Cuál se parece más al plato modelo? Responde con la letra: A) el de pasta sola, B) el segundo.", "B", "Tiene cereal, verdura y proteína."),
  ],
  cha=[
      ("Escribe dos límites del plato modelo.", "No muestra las necesidades de cada persona y no muestra las otras comidas del día", "Un modelo no incluye todo lo real."),
      ("Predice con el modelo: si un almuerzo es mitad pan y mitad arroz, ¿qué parte del modelo queda sin cubrir? Explica.", "Frutas, verduras y proteínas, porque solo hay cereales", "El plato modelo pide varios grupos."),
  ],
  context=[("Dato de ejemplo. Un grupo dibujó 6 platos modelo y en cada plato pintó 4 partes con colores. ¿Cuántas partes pintaron?", "24", "6 × 4 = 24.")],
  selfcheck=[("¿Qué parte del plato modelo ocupan las frutas y las verduras?", "La mitad", "Así lo propone el modelo."), ("¿Por qué las porciones con la mano son aproximadas?", "Porque las manos son de distinto tamaño", "Es una medida que varía."), ("¿Qué límite tiene el plato modelo?", "No muestra lo que necesita cada persona", "Todo modelo deja cosas fuera.")],
  open_task=task("Dibuja un plato dividido en cuatro partes iguales y pinta con colores un modelo de almuerzo usando alimentos concretos: dos partes de frutas y verduras, una de cereal o papas y una de carne, huevo o legumbres. Escribe el nombre de cada alimento y dos límites de tu modelo.", "Dos partes: ensalada de lechuga y tomate, y manzana. Una parte: arroz. Una parte: lentejas. Límites: no muestra cuánto necesita cada persona y no muestra las otras comidas.", ["plato en cuatro partes", "alimentos concretos en cada parte", "dos límites"], ["dibujo rotulado", "frases de límite"], ["afirmar que es una regla", "no escribir límites"], "Pregunta por qué eligió esos alimentos y qué cambiaría en otra comida del día."),
  reinforce="Dibuja un plato modelo para una once con alimentos de tres grupos.",
  extend="Explica por qué el plato modelo no puede reemplazar la orientación de un profesional de la salud.")

L(OA5, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar menús con un criterio común y a concluir con los datos. Sirve para describir una alimentación sin etiquetar a nadie.",
  prior=["Sé contar grupos, porciones y comidas.", "Sé que para comparar uso un mismo criterio."],
  explain=[
      "Para comparar dos menús, elegimos un criterio y lo contamos en los dos. Puede ser la variedad: cuántos grupos distintos aparecen. Puede ser la frecuencia: cuántas comidas hay en el día. Puede ser las porciones de frutas y verduras: cuántas se comieron. Una tabla con dos columnas, una por persona, ayuda a ver la diferencia.",
      "Al comparar, la conclusión debe decir solo lo que muestran los datos: «El menú de Tomás tuvo más grupos que el de Valentina ese día». No debe decir que una persona es mejor que la otra, porque un día no basta y porque cada persona tiene necesidades distintas.",
      "También se relacionan los grupos con las funciones del cuerpo: los cereales con el movimiento, las proteínas con el crecimiento y la reparación, y las frutas, verduras y lácteos con el desarrollo y el funcionamiento. Si un menú no tiene un grupo, esa función no se apoya ese día con esos alimentos.",
  ],
  vocab=[("criterio", "característica que se mira igual en todos los casos"), ("comparación", "mirar parecidos y diferencias entre dos casos"), ("conclusión", "respuesta final apoyada en los datos"), ("función del cuerpo", "trabajo que hace el cuerpo, como crecer o moverse"), ("limitación", "algo que los datos no pueden mostrar")],
  worked=[
      ("Comparar variedad", "Tomás: 5 grupos. Valentina: 3 grupos. ¿Cuántos grupos más tuvo Tomás?", ["El criterio es el número de grupos.", "Resto 5 − 3.", "Anoto la diferencia."], "2 grupos más"),
      ("Conclusión prudente", "¿Cuál conclusión usa solo los datos? A) Tomás come mejor que Valentina. B) El menú de Tomás tuvo más grupos ese día.", ["Reviso qué frase se apoya en un conteo.", "B habla del menú y del día.", "A juzga a la persona."], "B"),
  ],
  mistakes=[
      ("Comparar la variedad de un menú con la frecuencia de otro.", "No hay criterio común.", "Elige uno y cuéntalo en los dos."),
      ("Concluir que una persona es mejor por un día.", "Un día no basta y cada persona tiene necesidades distintas.", "Describe el menú, no a la persona."),
  ],
  rec=[
      ("¿Cuál tiene más grupos: un menú con 5 o uno con 3?", "El de 5", "5 es mayor que 3."),
      ("¿Qué criterio cuenta cuántas veces se come: variedad o frecuencia?", "Frecuencia", "Es el número de comidas."),
      ("Completa con «menú» o «persona»: la conclusión debe hablar del ______ y de los datos.", "Menú", "Así se evita juzgar a las personas."),
  ],
  und=[
      ("¿Qué grupo de alimentos apoya sobre todo el movimiento?", "Los cereales", "Los cereales dan energía."),
      ("¿Por qué una conclusión no debe decir «come mejor»?", "Porque «mejor» no está medido con un criterio y un día no basta", "Hay que hablar de lo observado."),
      ("¿Qué comparación es justa? A) Contar grupos en dos días completos. B) Contar grupos en un día y comidas en otro.", "A", "En A se usa el mismo criterio."),
  ],
  app=[
      arith("Dato de ejemplo. Valentina comió 3 veces el lunes y 4 veces el martes. ¿Cuántas comidas anotó en total?", "3+4", "Se suman las comidas de los dos días."),
      arith("Dato de ejemplo. Tomás comió 5 porciones de frutas y verduras y Valentina 2. ¿Cuántas más comió Tomás?", "5-2", "Se resta el valor menor al mayor."),
      ("Un menú tiene solo cereales. Con lo que sabes, ¿qué función del cuerpo apoya sobre todo: el movimiento o el crecimiento y la reparación?", "El movimiento", "Los cereales dan energía."),
  ],
  rea=[
      ("Dani compara el desayuno de Tomás con la cena de Valentina y concluye que Tomás tuvo más grupos. ¿Qué problema tiene?", "Comparó comidas distintas", "El criterio debe aplicarse a las mismas comidas."),
      ("Tomás tuvo 5 grupos y Valentina 3 un lunes. Rita concluye que Valentina siempre tiene menos grupos. ¿Se puede asegurar? Responde Sí o No y explica.", "No; es solo un día", "Otros días puede ser distinto."),
  ],
  cha=[
      ("Escribe una conclusión prudente con estos datos: Tomás tuvo 5 grupos y Valentina 3 un lunes.", "El lunes el menú de Tomás tuvo 2 grupos más que el de Valentina", "Dice qué mostraron los datos sin juzgar."),
      ("Un menú tiene muchas verduras y frutas pero ninguna carne, huevo ni legumbre. ¿Qué grupo falta para apoyar el crecimiento y la reparación ese día con esos alimentos?", "El de carnes, huevos y legumbres", "Ese grupo aporta proteínas."),
  ],
  context=[("Dato de ejemplo. Una tabla de 4 días muestra los grupos de alimentos de Tomás: 5, 4, 5 y 6. ¿Cuántos grupos sumó en los 4 días?", "20", "5 + 4 + 5 + 6 = 20.")],
  selfcheck=[("En Ciencias: ¿Qué es un criterio?", "Una característica que se mira igual en todos los casos", "Permite comparar con justicia."), ("¿Qué grupo apoya el crecimiento y la reparación?", "Carnes, huevos, pescados y legumbres", "Estos alimentos aportan proteínas."), ("¿Qué debe decir una conclusión prudente?", "Solo lo que muestran los datos", "No debe juzgar a la persona.")],
  open_task=task("Compara estos dos menús ficticios con el criterio «cuántos grupos distintos hay». Menú A: pan, leche, lentejas, arroz, ensalada, manzana. Menú B: pan, galletas, tostadas, arroz. Cuenta los grupos de cada menú (usa los seis grupos de la clase 1), escribe una conclusión prudente y una limitación.", "Menú A: cereales, lácteos, carnes y legumbres, verduras y frutas = 5 grupos. Menú B: solo cereales = 1 grupo. Conclusión: el menú A tuvo 4 grupos más. Limitación: son menús ficticios de un solo día.", ["cuenta los grupos de cada menú", "conclusión prudente", "una limitación"], ["tabla con dos menús", "frases"], ["juzgar a una persona", "cambiar el criterio"], "Pregunta qué cambiaría si comparara tres días en vez de uno."),
  reinforce="Compara dos desayunos escritos por ti con el criterio «cuántos grupos distintos hay».",
  extend="Explica por qué no conviene decir que una persona «come mal» por un registro de un día.")

L(OA5, 5,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a explicar con evidencia cómo los alimentos apoyan el cuerpo y a reconocer límites. Sirve para dar una explicación honesta sobre la alimentación.",
  prior=["Sé los grupos de alimentos y sus funciones.", "Sé comparar menús con un criterio."],
  explain=[
      "Una buena explicación une un alimento con una función del cuerpo y una evidencia. Por ejemplo: «Las lentejas ayudan a la reparación del cuerpo porque son una legumbre que aporta proteínas». La evidencia es el grupo del alimento y lo que aporta ese grupo.",
      "Para analizar una alimentación diaria se miran la variedad, el tamaño de las porciones y la frecuencia de las comidas. Si en un día falta un grupo, no se puede afirmar que una persona esté mal alimentada, solo que ese día no apareció ese grupo. Para saber más hace falta más información.",
      "Los límites son importantes. Los registros de pocos días no muestran lo habitual. Cada persona necesita cantidades distintas según su edad, su actividad y su salud. Los grupos de este cuaderno son una simplificación. Ante dudas, se consulta a un profesional de la salud.",
  ],
  vocab=[("explicación", "relato que dice qué pasa y por qué"), ("evidencia", "dato que apoya una explicación"), ("límite", "lo que la evidencia no puede mostrar"), ("necesidades", "lo que el cuerpo requiere para funcionar"), ("simplificación", "versión sencilla de algo complejo")],
  worked=[
      ("Completar una explicación", "Completa: «Los cereales ayudan al ______ porque dan energía».", ["Recuerdo la función de los cereales.", "Dan energía.", "La energía permite moverse."], "Movimiento"),
      ("Evidencia y límite", "Un registro de un día muestra solo pan y arroz. ¿Qué evidencia hay y qué límite tiene?", ["El registro muestra solo dos alimentos de un grupo.", "Es de un solo día.", "No muestra los otros días."], "Evidencia: ese día hubo solo cereales. Límite: no muestra lo habitual"),
  ],
  mistakes=[
      ("Afirmar que una persona está mal alimentada por un día de registro.", "Un día no basta.", "Describe el día y pide más datos."),
      ("Dar una explicación sin nombrar el grupo del alimento.", "Sin el grupo no hay evidencia.", "Escribe a qué grupo pertenece y qué aporta."),
  ],
  rec=[
      ("¿Qué grupo apoya la reparación del cuerpo: las legumbres o los aceites?", "Las legumbres", "Las legumbres aportan proteínas."),
      ("¿Qué apoya la energía para moverse: los cereales o el agua sola?", "Los cereales", "Los cereales dan energía."),
      ("Completa con «profesional» o «vecino»: ante dudas se consulta a un ______ de la salud.", "Profesional", "Puede orientar según cada persona."),
  ],
  und=[
      ("¿Qué grupo aporta vitaminas y minerales que ayudan al desarrollo?", "Frutas, verduras y lácteos", "Aportan vitaminas y minerales."),
      ("¿Por qué el registro de un día tiene un límite?", "Porque no muestra lo que se come habitualmente", "Los menús cambian de un día a otro."),
      ("¿Qué frase tiene evidencia? A) Los huevos aportan proteínas que ayudan a reparar el cuerpo. B) Los huevos son lo único importante.", "A", "A nombra el aporte del alimento."),
  ],
  app=[
      ("Ordena una explicación: A) ayudan a la reparación, B) las lentejas son legumbres, C) y aportan proteínas. Escribe el orden más claro.", "B, C, A", "Primero el alimento, luego lo que aporta y al final la función."),
      arith("Un registro de ejemplo muestra 4 comidas diarias durante 5 días. ¿Cuántas comidas hay anotadas?", "4*5", "Se multiplican las comidas por los días."),
      ("Un menú tiene leche, queso y yogur. ¿Qué grupo es el único que aparece?", "Los lácteos", "Todos son lácteos."),
  ],
  rea=[
      ("Pedro dice: «Como solo comí frutas hoy, estoy perfecto». ¿Qué falta en su razonamiento?", "Que las frutas son solo un grupo y falta ver los demás y otros días", "Un día de un solo grupo no muestra variedad."),
      ("Ana quiere explicar por qué un niño que juega mucho necesita alimentos con energía. ¿Qué grupo nombrarías y por qué?", "Cereales, porque dan energía para el movimiento", "La energía apoya la actividad."),
  ],
  cha=[
      ("Escribe una explicación de dos frases sobre un huevo y una manzana: qué aportan y a qué función ayudan.", "El huevo aporta proteínas para la reparación; la manzana aporta vitaminas para el desarrollo y el funcionamiento", "Cada alimento se une a un grupo y una función."),
      ("Un afiche dice: «Este alimento cura todo». ¿Por qué no es una explicación con evidencia?", "Porque ningún alimento cura todo y no da datos", "Hace una promesa sin evidencia."),
  ],
  context=[("Dato de ejemplo. Un curso registró durante 3 días las porciones de frutas y verduras de un estudiante: 3, 4 y 2. ¿Cuántas porciones registró en los 3 días?", "9", "3 + 4 + 2 = 9.")],
  selfcheck=[("¿Qué incluye una buena explicación?", "El alimento, su grupo, lo que aporta y la evidencia", "Así se apoya con datos."), ("¿Por qué consultar a un profesional?", "Porque cada persona tiene necesidades distintas", "Un registro no reemplaza esa orientación."), ("¿Un alimento puede curar todo? Responde Sí o No.", "No", "Ningún alimento tiene ese efecto.")],
  open_task=task("Elige tres alimentos de este menú de ejemplo: lentejas, pan, manzana, leche, huevo. Escribe una explicación de una frase para cada uno que diga su grupo, lo que aporta y la función del cuerpo que apoya. Termina con un límite de tu explicación.", "Lentejas: legumbre con proteínas que ayudan a la reparación. Pan: cereal que da energía para el movimiento. Manzana: fruta con vitaminas que ayudan al desarrollo. Límite: no sé cuánto necesita cada persona.", ["tres explicaciones con grupo y función", "evidencia clara", "un límite"], ["tres frases", "frase de límite"], ["prometer curas", "olvidar el límite"], "Pregunta qué parte de su explicación es dato y cuál es suposición."),
  reinforce="Escribe una explicación sobre un alimento de tu casa que diga su grupo y su aporte.",
  extend="Explica por qué ningún grupo de alimentos puede reemplazar a todos los demás.")

# ---------------------------------------------------------------- OA 06
L(OA6, 1,
  materials="Este cuaderno y lápiz. Los textos que necesitas están escritos en los ejercicios.",
  use="Aprenderé qué contiene el humo del tabaco y a separar hechos de opiniones al leer información. Sirve para investigar con cuidado.",
  prior=["Sé las estructuras de los sistemas respiratorio y circulatorio.", "Sé que una observación se puede comprobar."],
  explain=[
      "El cigarrillo es una hoja de tabaco seca enrollada. Al quemarse produce humo con miles de sustancias químicas, y muchas son dañinas. Tres que se nombran mucho son estas. La nicotina hace que la persona dependa del cigarrillo. El alquitrán es una sustancia pegajosa que se acumula en los pulmones. El monóxido de carbono es un gas que se une a la sangre e impide que lleve bien el oxígeno.",
      "Este humo pasa por la nariz, la tráquea, los bronquios y los alvéolos, y también llega a la sangre. Por eso afecta a dos sistemas: el respiratorio y el circulatorio. También daña a quienes respiran el humo de otra persona, que se llama fumador pasivo. Muchas personas adultas fuman y a muchas les cuesta dejarlo por la dependencia; dejarlo es posible con ayuda de profesionales de la salud.",
      "Para investigar, hay que distinguir un hecho de una opinión. Un hecho se puede comprobar en fuentes confiables, como «el humo contiene monóxido de carbono». Una opinión es lo que alguien piensa, como «fumar da miedo». En esta clase leeremos textos escritos para este cuaderno.",
  ],
  vocab=[("nicotina", "sustancia del tabaco que genera dependencia"), ("monóxido de carbono", "gas del humo que impide que la sangre lleve bien el oxígeno"), ("alquitrán", "sustancia pegajosa del humo que se acumula en los pulmones"), ("fumador pasivo", "persona que respira el humo de otra"), ("hecho", "información que se puede comprobar")],
  worked=[
      ("Hecho u opinión", "«El humo del cigarrillo contiene monóxido de carbono» y «Los cigarrillos son horribles». ¿Cuál es un hecho?", ["Pregunto qué frase se puede comprobar en una fuente.", "Lo del monóxido de carbono se verifica.", "«Horribles» es una opinión."], "La primera frase"),
      ("Identificar los sistemas", "El humo pasa por los bronquios y llega a la sangre. ¿Qué sistemas afecta?", ["Los bronquios son del sistema respiratorio.", "La sangre es del sistema circulatorio.", "Nombro ambos."], "El respiratorio y el circulatorio"),
  ],
  mistakes=[
      ("Creer que el humo solo afecta a quien fuma.", "También afecta a quienes lo respiran.", "Recuerda el fumador pasivo."),
      ("Tomar una opinión como si fuera un dato.", "Una opinión no se puede comprobar.", "Busca si hay una fuente que lo confirme."),
  ],
  rec=[
      ("¿El humo del tabaco afecta al sistema respiratorio?", "Sí", "Pasa por la nariz, la tráquea y los bronquios."),
      ("¿Qué sustancia del tabaco genera dependencia?", "La nicotina", "Por eso a muchas personas les cuesta dejarlo."),
      ("Completa con «hecho» o «opinión»: una información que se puede comprobar es un ______.", "Hecho", "Se verifica en fuentes confiables."),
  ],
  und=[
      ("¿Qué hace el monóxido de carbono en la sangre?", "Impide que lleve bien el oxígeno", "Se une a la sangre."),
      ("¿Quién es un fumador pasivo?", "La persona que respira el humo de otra", "No fuma, pero respira el humo."),
      ("Marca el hecho: A) El humo del tabaco contiene nicotina. B) El humo es muy feo.", "A", "A se puede comprobar; B es opinión."),
  ],
  app=[
      ("Un texto dice: «El humo contiene miles de sustancias; muchas son dañinas». ¿Qué parte es un dato que se puede revisar: «miles de sustancias» o «es horrible»?", "Miles de sustancias", "Se puede comprobar en una fuente confiable."),
      arith("Una clase leyó 3 textos y en cada uno marcó 4 hechos. ¿Cuántos hechos marcó?", "3*4", "Se multiplican los textos por los hechos."),
      ("El humo llega a la tráquea y a la sangre. ¿Cuántos sistemas del cuerpo nombra esta frase?", "2", "El respiratorio y el circulatorio."),
  ],
  rea=[
      ("Un compañero dice: «Fumar un poquito no daña a nadie». ¿Qué podrías responder usando lo aprendido?", "Que el humo tiene sustancias dañinas y también afecta a quienes lo respiran", "El humo contiene sustancias que dañan al respirarlo."),
      ("Un texto dice: «Una persona que fuma dice que se siente bien». ¿Es evidencia suficiente para decir que el humo no daña? Responde Sí o No y explica.", "No; es un solo caso y no un dato general", "Un caso no representa a todas las personas."),
  ],
  cha=[
      ("Lee: «El tabaco contiene nicotina. Es horrible. Su humo tiene monóxido de carbono». ¿Cuántas frases son hechos?", "2", "La primera y la tercera se pueden comprobar."),
      ("Explica por qué hay que respetar a las personas que fuman aunque se estudie el daño del humo.", "Porque el objetivo es informar y cuidar la salud, no juzgar a las personas", "Se rechaza el daño, no a la persona."),
  ],
  context=[("Dato de ejemplo. Una clase hizo 5 afiches y en cada uno escribió 3 hechos. ¿Cuántos hechos escribieron en total?", "15", "5 × 3 = 15.")],
  selfcheck=[("Nombra una sustancia del humo del tabaco.", "Nicotina, alquitrán o monóxido de carbono", "Son tres sustancias conocidas del humo."), ("¿Qué diferencia hay entre hecho y opinión?", "El hecho se puede comprobar y la opinión no", "Así se distingue la evidencia."), ("¿El humo afecta solo a quien fuma? Responde Sí o No.", "No", "También afecta a quien lo respira.")],
  open_task=task("Lee con una persona de tu casa este texto: «El humo del cigarrillo contiene nicotina y monóxido de carbono. Entra por la nariz y llega a los pulmones. Fumar es horrible. Algunas personas no pueden dejar de fumar». Marca con H los hechos y con O las opiniones. No es necesario preguntar a nadie sobre su salud ni sus hábitos.", "H: el humo contiene nicotina y monóxido de carbono; H: entra por la nariz y llega a los pulmones; O: fumar es horrible; H: algunas personas no pueden dejar de fumar (por la dependencia).", ["marca cuatro frases", "distingue hechos de opiniones", "no juzga a personas"], ["texto marcado", "lista de H y O"], ["tomar una opinión como hecho", "comentar sobre la salud de alguien"], "Pregunta cómo podría comprobar uno de los hechos en una fuente confiable."),
  reinforce="Escribe dos hechos y dos opiniones sobre el cuidado de los pulmones.",
  extend="Explica con tus palabras por qué se dice que el humo ajeno también puede dañar.")

L(OA6, 2,
  materials="Este cuaderno y lápiz. Las fuentes de ejemplo están escritas en los ejercicios; no necesitas internet.",
  use="Aprenderé a hacer preguntas de investigación y a elegir fuentes confiables sobre el humo del tabaco. Sirve para buscar información con criterio.",
  prior=["Sé separar hechos de opiniones.", "Sé que una pregunta comprobable se responde con datos."],
  explain=[
      "Una investigación comienza con una pregunta. Para este tema, algunas preguntas buenas son: «¿Qué sustancias hay en el humo del tabaco?», «¿Cómo afecta el humo a los pulmones?» y «¿Cómo afecta al corazón y a los vasos?». Una pregunta como «¿Quién fuma más?» necesita datos distintos. Una predicción puede ser: «El humo afecta a los pulmones porque pasa por las vías respiratorias».",
      "No toda fuente sirve. Una fuente confiable dice quién la escribió, como una institución de salud o una universidad, tiene fecha, usa datos y no vende nada. Una fuente poco confiable no tiene autor, trae publicidad o solo da opiniones. Conviene mirar al menos dos fuentes y comparar si coinciden.",
      "Cuando varias fuentes confiables dicen lo mismo, la información es más segura. Si no coinciden, hay que seguir investigando. Nunca se copia sin entender: se escribe con palabras propias y se anota de dónde viene.",
  ],
  vocab=[("fuente", "lugar de donde sale la información"), ("fuente confiable", "fuente con autor, fecha y datos que se pueden comprobar"), ("publicidad", "mensaje que busca vender algo"), ("pregunta de investigación", "pregunta que se responde buscando información"), ("contrastar", "comparar si varias fuentes dicen lo mismo")],
  worked=[
      ("Elegir la fuente confiable", "¿Cuál es más confiable? A) Un folleto de un ministerio de salud con fecha y datos. B) Un video sin autor que vende un producto.", ["Reviso quién escribe.", "El folleto tiene autor, fecha y datos.", "El video no muestra autor y vende algo."], "A"),
      ("Hacer una pregunta de investigación", "¿Cuál es una pregunta de investigación sobre el tema? A) ¿Cómo afecta el humo del tabaco a los bronquios? B) ¿Es bonito el humo?", ["Pienso si se responde con información.", "A se responde con fuentes de salud.", "B es una opinión."], "A"),
  ],
  mistakes=[
      ("Confiar en la primera información que aparece.", "Puede ser una opinión o publicidad.", "Contrasta con al menos dos fuentes."),
      ("Copiar un párrafo sin entenderlo.", "No se aprende y no se cita la fuente.", "Escribe con tus palabras y anota la fuente."),
  ],
  rec=[
      ("¿Una fuente confiable tiene autor o no tiene autor?", "Tiene autor", "Así se sabe quién responde por la información."),
      ("¿Un anuncio que vende algo es una fuente confiable para estudiar?", "No", "Su objetivo es vender."),
      ("Completa con «dos» o «ninguna»: para contrastar se consultan al menos ______ fuentes.", "Dos", "Así se puede comparar."),
  ],
  und=[
      ("¿Por qué conviene contrastar varias fuentes?", "Para ver si coinciden", "Si varias fuentes confiables dicen lo mismo, hay más seguridad."),
      ("¿Cuál es una pregunta de investigación? A) ¿Qué sustancias hay en el humo del tabaco? B) ¿Qué canción te gusta?", "A", "A se responde con información."),
      ("¿Qué debes anotar de una fuente para poder volver a ella?", "Quién la escribió y de dónde viene", "Así se puede revisar."),
  ],
  app=[
      arith("Dato de ejemplo. Una clase revisó 8 fuentes y 5 eran confiables. ¿Cuántas no eran confiables?", "8-5", "Se resta las confiables al total."),
      ("Fuente A: autor ministerio de salud, fecha 2023, con datos. Fuente B: sin autor, sin fecha, con publicidad. ¿Cuál usarías para un trabajo?", "La fuente A", "Tiene autor, fecha y datos."),
      ("Predice: si el humo pasa por los bronquios, ¿qué sistema esperas que se afecte? Escribe el nombre.", "El respiratorio", "Los bronquios pertenecen a ese sistema."),
  ],
  rea=[
      ("Lía solo buscó una fuente y dice que ya está segura. ¿Qué le recomiendas?", "Buscar otra fuente confiable y comparar", "Contrastar da más seguridad."),
      ("Una página dice: «Compra este producto y te curarás de todo». ¿Por qué no es una fuente confiable para estudiar?", "Porque vende algo y promete sin datos", "No da evidencia y tiene interés comercial."),
  ],
  cha=[
      ("Escribe una pregunta de investigación sobre el humo del tabaco y el corazón.", "¿Cómo afecta el humo del tabaco al corazón y a los vasos sanguíneos?", "Se puede responder con fuentes de salud."),
      ("Dos fuentes confiables dicen lo mismo sobre el monóxido de carbono. ¿Qué te indica eso sobre la información?", "Que es más segura", "Hay coincidencia entre fuentes."),
  ],
  context=[("Dato de ejemplo. Un grupo revisó 4 fuentes por cada una de sus 3 preguntas. ¿Cuántas fuentes revisó en total?", "12", "4 × 3 = 12.")],
  selfcheck=[("¿Qué tiene una fuente confiable?", "Autor, fecha y datos que se pueden comprobar", "Eso permite revisar la información."), ("¿Por qué contrastar fuentes?", "Para ver si coinciden", "Así se gana seguridad."), ("¿Se copia sin entender? Responde Sí o No.", "No", "Se escribe con palabras propias.")],
  open_task=task("Escribe tres preguntas de investigación sobre el humo del tabaco (una sobre sus sustancias, una sobre el sistema respiratorio y una sobre el sistema circulatorio). Para cada una, escribe tu predicción y qué tipo de fuente confiable usarías. No necesitas buscar ahora; solo planificar.", "Pregunta: ¿Qué hace el humo en los bronquios? Predicción: los irrita porque pasa por ellos. Fuente: un folleto de un ministerio de salud con fecha y datos.", ["tres preguntas de investigación", "una predicción para cada una", "tipo de fuente confiable"], ["lista de tres preguntas", "predicciones"], ["usar preguntas de opinión", "no indicar fuente"], "Pregunta cómo sabrá si la fuente es confiable y qué haría si dos fuentes no coinciden."),
  reinforce="Escribe dos criterios para saber si una fuente es confiable.",
  extend="Explica por qué la publicidad no es una buena fuente para investigar la salud.")

L(OA6, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a usar un esquema con flechas para mostrar los efectos del humo en los sistemas respiratorio y circulatorio. Sirve para comunicar con claridad y decir qué no muestra el esquema.",
  prior=["Sé las estructuras de los sistemas respiratorio y circulatorio.", "Sé que un modelo tiene límites."],
  explain=[
      "Un esquema muestra el recorrido del humo y sus efectos. El humo entra por la nariz y la boca y baja por la tráquea y los bronquios hasta los alvéolos. En el camino irrita las vías, provoca tos y daña unos pelitos diminutos llamados cilios, que normalmente ayudan a limpiar. Con el tiempo, el humo puede dañar los pulmones y dificultar la respiración.",
      "Del pulmón, las sustancias pasan a la sangre y viajan por todo el cuerpo. El monóxido de carbono ocupa el lugar del oxígeno en la sangre, de modo que llega menos oxígeno a las células. La nicotina hace que el corazón lata más rápido y estrecha los vasos. Con los años, esto aumenta el riesgo de enfermedades del corazón y de los vasos sanguíneos.",
      "Este esquema tiene límites: no muestra el tiempo que tardan los daños, ni que el riesgo cambia de persona a persona, ni todas las sustancias del humo. Un buen esquema dice lo que muestra y lo que deja fuera.",
  ],
  vocab=[("vías respiratorias", "tubos por donde pasa el aire, como la tráquea y los bronquios"), ("cilios", "pelitos diminutos que ayudan a limpiar las vías respiratorias"), ("dañar", "estropear una parte del cuerpo"), ("riesgo", "posibilidad de que algo malo ocurra"), ("esquema", "dibujo simple con nombres y flechas")],
  worked=[
      ("Leer el esquema", "Esquema: humo → tráquea → bronquios → alvéolos → sangre. ¿Qué estructura recibe el humo justo después de los bronquios?", ["Sigo las flechas.", "Después de los bronquios vienen los alvéolos.", "Escribo el nombre."], "Los alvéolos"),
      ("Encontrar un límite", "El esquema no muestra cuánto tiempo tarda el daño. ¿Es un límite?", ["El tiempo es un dato real.", "El esquema no lo incluye.", "Es algo que queda fuera."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Decir que el daño ocurre en un solo día.", "Los daños suelen aparecer con el tiempo y dependen de la exposición.", "Habla de riesgo y de exposición repetida."),
      ("Pensar que el esquema muestra todas las sustancias del humo.", "El humo tiene miles de sustancias.", "Escribe ese límite."),
  ],
  rec=[
      ("¿El humo pasa por los bronquios o por el estómago?", "Por los bronquios", "Entra por las vías respiratorias."),
      ("¿Qué gas del humo ocupa el lugar del oxígeno en la sangre?", "El monóxido de carbono", "Reduce el oxígeno que llega a las células."),
      ("Completa con «tos» o «sueño»: el humo irrita las vías y produce ______.", "Tos", "Es una reacción de irritación."),
  ],
  und=[
      ("¿Para qué sirven los cilios?", "Para ayudar a limpiar las vías respiratorias", "El humo los daña."),
      ("¿Qué le pasa al corazón por la nicotina?", "Late más rápido", "La nicotina lo acelera."),
      ("¿Qué muestra el esquema? A) El recorrido del humo y sus efectos. B) La duración exacta del daño.", "A", "El esquema no incluye el tiempo."),
  ],
  app=[
      ("Esquema: humo → bronquios; humo → sangre. ¿Cuántos sistemas aparecen afectados?", "2", "Bronquios (respiratorio) y sangre (circulatorio)."),
      arith("Un esquema tiene 7 flechas. Dibujaste 4. ¿Cuántas te faltan?", "7-4", "Se resta lo dibujado al total."),
      ("Predice con el esquema: si el monóxido de carbono ocupa el lugar del oxígeno, ¿llegará más o menos oxígeno a las células? Escribe «más» o «menos».", "Menos", "El gas ocupa espacio del oxígeno."),
  ],
  rea=[
      ("Rafa dice: «Mi esquema muestra todo el daño del humo». ¿Tiene razón? Responde Sí o No y explica.", "No; no muestra el tiempo ni todas las sustancias", "Todo esquema simplifica."),
      ("Un esquema muestra solo el sistema respiratorio. ¿Qué parte del tema deja fuera?", "El efecto en el sistema circulatorio", "El humo también llega a la sangre."),
  ],
  cha=[
      ("Escribe dos límites del esquema del humo.", "No muestra el tiempo del daño y no muestra todas las sustancias", "El humo tiene miles de sustancias y el daño depende del tiempo."),
      ("Explica con el esquema por qué el humo afecta a dos sistemas.", "Porque pasa por las vías respiratorias y las sustancias llegan a la sangre", "El pulmón y la sangre están conectados."),
  ],
  context=[("Dato de ejemplo. Una clase dibujó 6 esquemas con 5 flechas cada uno. ¿Cuántas flechas dibujaron en total?", "30", "6 × 5 = 30.")],
  selfcheck=[("¿Cómo afecta el humo a las vías respiratorias?", "Las irrita y daña los cilios", "Eso causa tos y dificulta la limpieza."), ("¿Qué hace el monóxido de carbono en la sangre?", "Impide que lleve bien el oxígeno", "Ocupa el lugar del oxígeno."), ("¿Qué límite tiene el esquema?", "No muestra el tiempo del daño ni todas las sustancias", "Todo modelo simplifica.")],
  open_task=task("Dibuja un esquema con flechas: humo → nariz → tráquea → bronquios → alvéolos → sangre → corazón. Escribe junto a cada flecha un efecto o un verbo (por ejemplo, «irrita»). Agrega dos límites de tu esquema.", "Humo irrita la tráquea y los bronquios; en los alvéolos pasa a la sangre; el monóxido de carbono reduce el oxígeno; la nicotina acelera el corazón. Límites: no muestra el tiempo y no muestra todas las sustancias.", ["siete elementos con flechas", "efectos escritos", "dos límites"], ["dibujo rotulado", "frases"], ["afirmar daños inmediatos para todos", "no escribir límites"], "Pregunta qué parte del esquema afecta al sistema respiratorio y cuál al circulatorio."),
  reinforce="Escribe dos efectos del humo en el sistema respiratorio y uno en el circulatorio.",
  extend="Explica por qué dejar de exponerse al humo puede ayudar a que el cuerpo se recupere.")

L(OA6, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar datos y fuentes con un criterio común y a comunicar lo que encontré sobre el humo del tabaco. Sirve para sacar conclusiones prudentes.",
  prior=["Sé los efectos del humo del tabaco.", "Sé que no se debe concluir más de lo que muestran los datos."],
  explain=[
      "Comparar resultados es mirar la misma característica en dos grupos. Los siguientes datos son de ejemplo y no representan a personas reales. En un grupo de 100 personas no expuestas al humo, 5 tienen tos frecuente. En un grupo de 100 personas expuestas, 20 la tienen. El criterio es el número de personas con tos frecuente por cada 100.",
      "Al comparar se ve que en el grupo expuesto hay más casos. Los datos reales de estudios grandes muestran una relación entre el humo y problemas de los pulmones y del corazón. Pero una tabla pequeña no permite decir que el humo es la única causa en cada persona: influyen otras cosas, como la edad o el aire de la ciudad.",
      "Al comunicar, una buena práctica es escribir qué dice cada fuente, si coinciden y qué no se sabe. Se usan palabras como «aumenta el riesgo» y no «siempre produce». Se cita la fuente y se evita asustar o culpar a personas.",
  ],
  vocab=[("criterio", "característica que se mira igual en todos los casos"), ("grupo", "conjunto de personas que se comparan"), ("expuesto", "que respira humo del tabaco"), ("relación", "vínculo entre dos cosas que ocurren juntas"), ("causa", "lo que produce un efecto")],
  worked=[
      ("Comparar dos grupos", "Datos de ejemplo. Grupo no expuesto: 5 con tos frecuente de 100. Grupo expuesto: 20 de 100. ¿Cuántos más hay en el grupo expuesto?", ["El criterio es personas con tos frecuente por cada 100.", "Resto 20 − 5.", "Anoto la diferencia."], "15 personas más por cada 100"),
      ("Conclusión prudente", "¿Cuál conclusión es más prudente? A) El humo es la única causa de la tos. B) En estos datos de ejemplo hay más tos en el grupo expuesto.", ["Reviso qué dice cada frase.", "A afirma más de lo que muestran los datos.", "B describe los datos."], "B"),
  ],
  mistakes=[
      ("Decir que los datos de ejemplo son reales.", "Los datos de ejemplo se inventan para practicar.", "Anota siempre que son datos de ejemplo."),
      ("Concluir una causa única con una tabla pequeña.", "Pueden influir otros factores.", "Habla de relación y de riesgo."),
  ],
  rec=[
      ("En los datos de ejemplo, ¿qué grupo tiene más casos de tos: el expuesto o el no expuesto?", "El expuesto", "Tiene 20 casos contra 5."),
      ("¿Se comparan grupos con el mismo criterio o con criterios distintos?", "Con el mismo criterio", "Así la comparación es justa."),
      ("Completa con «causa» o «relación»: una tabla pequeña muestra una ______ pero no prueba todo.", "Relación", "No basta para asegurar una causa única."),
  ],
  und=[
      ("¿Por qué se dice que los datos de la clase son «de ejemplo»?", "Porque no son de personas reales", "Sirven para practicar la comparación."),
      ("¿Qué palabra es más prudente al comunicar: «aumenta el riesgo» o «siempre produce»?", "Aumenta el riesgo", "No todas las personas se ven afectadas igual."),
      ("¿Qué comparación es justa? A) Contar tos por cada 100 personas en los dos grupos. B) Contar tos en un grupo y edad en otro.", "A", "Se usa el mismo criterio."),
  ],
  app=[
      arith("Datos de ejemplo. Grupo A: 8 personas con tos de 100. Grupo B: 23 de 100. ¿Cuántas más tiene el grupo B?", "23-8", "Se resta el valor menor al mayor."),
      ("Datos de ejemplo. Personas con tos por cada 100: grupo A, 8; grupo B, 23; grupo C, 15. Escribe los grupos de menos a más casos.", "A, C, B", "8 es menor que 15 y 15 es menor que 23."),
      ("Dos fuentes confiables coinciden en que el humo irrita los bronquios. ¿La información es más segura o menos segura?", "Más segura", "La coincidencia refuerza la información."),
  ],
  rea=[
      ("Elena concluye con los datos de ejemplo: «El humo causa tos a todas las personas». ¿Qué problema tiene?", "Afirma más de lo que muestran los datos", "Los datos no cubren a todas las personas y solo son de ejemplo."),
      ("Un afiche dice: «Una persona que fuma se enferma sí o sí». ¿Qué palabra lo hace poco prudente?", "«Sí o sí»", "El daño es un riesgo y no una certeza."),
  ],
  cha=[
      ("Escribe una conclusión prudente con los datos de ejemplo: no expuestos 5 de 100, expuestos 20 de 100.", "En estos datos de ejemplo hay más personas con tos en el grupo expuesto", "Describe sin afirmar una causa única."),
      ("Menciona dos factores, además del humo, que podrían influir en la tos de un grupo.", "La edad y el aire de la ciudad", "Otras cosas también pueden influir."),
  ],
  context=[("Dato de ejemplo. Una escuela ficticia comparó dos grupos de 50 personas. En el primero hubo 3 con tos frecuente y en el segundo 11. ¿Cuántas más tuvo el segundo?", "8", "11 − 3 = 8.")],
  selfcheck=[("¿Qué es un criterio de comparación?", "Una característica que se mira igual en los dos grupos", "Permite comparar con justicia."), ("¿Qué palabra es prudente al hablar de los efectos?", "Riesgo", "El daño no es igual para todas las personas."), ("¿Una tabla de ejemplo sirve para afirmar algo sobre todas las personas? Responde Sí o No.", "No", "Es solo para practicar la comparación.")],
  open_task=task("Con una persona de tu casa, mira estos datos de ejemplo: lunes, 3 personas con tos de 50; martes, 4 de 50; miércoles, 14 de 50 (día con mucho humo en el patio, ficticio). Haz una tabla, compara con el criterio «personas con tos por cada 50» y escribe una conclusión prudente y una limitación.", "Tabla con 3, 4 y 14. Conclusión: el miércoles hubo más personas con tos en estos datos de ejemplo. Limitación: son datos inventados y no prueban una causa.", ["tabla con los tres datos", "conclusión prudente", "una limitación"], ["tabla", "frases"], ["afirmar una causa única", "tratar datos inventados como reales"], "Pregunta qué otros factores podrían explicar los resultados."),
  reinforce="Escribe una conclusión prudente con otros dos datos de ejemplo que inventes.",
  extend="Explica por qué las investigaciones grandes son más confiables que una tabla pequeña.")

L(OA6, 5,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a comunicar con evidencia los efectos del humo del tabaco y a reconocer los límites de mi mensaje. Sirve para preparar un afiche o un texto claro y respetuoso.",
  prior=["Sé los efectos del humo en dos sistemas.", "Sé distinguir hechos, opiniones y fuentes."],
  explain=[
      "Un buen mensaje de salud tiene un título claro, hechos con fuente, una explicación con palabras propias y una recomendación respetuosa. Un ejemplo de hecho para un afiche: «El monóxido de carbono del humo impide que la sangre lleve bien el oxígeno». Una recomendación: «Evitar el humo ajeno cuida tus pulmones».",
      "Para explicar con evidencia, une el hecho con el efecto: «El humo irrita los bronquios, por eso provoca tos». Después indica los límites: no se sabe cuánto tardará el daño en una persona concreta y el riesgo cambia entre personas. Evita palabras como «seguro» y «siempre» cuando no hay evidencia.",
      "Comunicar con respeto significa no culpar ni asustar. Muchas personas que fuman quieren dejarlo y necesitan apoyo. Si conoces a alguien que quiere dejarlo, puedes sugerir que consulte en un centro de salud.",
  ],
  vocab=[("mensaje de salud", "texto o afiche que informa para cuidar el cuerpo"), ("recomendación", "consejo basado en evidencia"), ("fuente", "lugar de donde sale la información"), ("evidencia", "dato que apoya una explicación"), ("respeto", "tratar con consideración a las personas")],
  worked=[
      ("Unir hecho y efecto", "Hecho: el humo irrita los bronquios. ¿Qué efecto se espera?", ["Irritar significa molestar.", "La irritación produce tos.", "Une el hecho con el efecto."], "Provoca tos"),
      ("Revisar un mensaje", "Mensaje: «Fumar mata sí o sí a todos». ¿Qué cambio lo haría más prudente?", ["«Sí o sí» y «todos» afirman demasiado.", "El daño es un riesgo.", "Cambio por «aumenta el riesgo»."], "Decir «Fumar aumenta el riesgo de enfermedades»"),
  ],
  mistakes=[
      ("Usar palabras absolutas como «siempre» o «nunca».", "No hay evidencia para afirmarlo en todos los casos.", "Usa «aumenta el riesgo»."),
      ("Burlarse o culpar a las personas que fuman.", "Esto no ayuda y falta el respeto.", "Informa sin juzgar."),
  ],
  rec=[
      ("¿Un afiche de salud debe citar su fuente o no?", "Sí", "Así se puede comprobar la información."),
      ("¿Qué palabra es más prudente: «aumenta el riesgo» o «siempre enferma»?", "Aumenta el riesgo", "No todas las personas se afectan igual."),
      ("Completa con «respeto» o «burla»: un buen mensaje de salud usa ______.", "Respeto", "El objetivo es cuidar."),
  ],
  und=[
      ("¿Qué debe tener un mensaje de salud además de un título?", "Hechos con fuente y una recomendación", "Así se informa con evidencia."),
      ("¿Por qué conviene decir los límites en un mensaje?", "Para no afirmar más de lo que se sabe", "La honestidad da confianza."),
      ("¿Cuál recomendación es respetuosa? A) Evitar el humo ajeno cuida tus pulmones. B) Los fumadores son tontos.", "A", "A informa; B ofende."),
  ],
  app=[
      ("Un afiche tiene estas partes: A) título, B) hecho con fuente, C) insulto a quienes fuman, D) recomendación. ¿Cuál no debe estar?", "C", "Un mensaje de salud informa con respeto y no insulta."),
      arith("Una clase hizo 6 afiches y cada uno tiene 3 hechos con fuente. ¿Cuántos hechos con fuente hay en total?", "6*3", "Se multiplican los afiches por los hechos."),
      ("Mensaje: «El humo contiene monóxido de carbono». ¿Es un hecho o una opinión?", "Un hecho", "Se puede comprobar en fuentes confiables."),
  ],
  rea=[
      ("Ana quiere asustar a sus compañeros con un afiche exagerado. ¿Qué le dirías sobre el objetivo de un mensaje de salud?", "Que debe informar con evidencia y respeto, no asustar", "Un mensaje honesto ayuda a decidir."),
      ("Un afiche dice: «Todos los que respiran humo tienen cáncer». ¿Tiene evidencia? Responde Sí o No y explica.", "No; afirma «todos» sin datos", "El riesgo cambia entre personas."),
  ],
  cha=[
      ("Escribe un título, un hecho y una recomendación para un afiche sobre el humo del tabaco.", "Título: Cuida tus pulmones. Hecho: el humo irrita los bronquios. Recomendación: evita el humo ajeno", "Incluye las tres partes de un buen mensaje."),
      ("Escribe un límite de tu mensaje.", "No se sabe cuánto tarda el daño en cada persona", "El riesgo cambia entre personas."),
  ],
  context=[("Dato de ejemplo. Un curso publicó 5 afiches y cada afiche tuvo 4 partes (título, dos hechos y una recomendación). ¿Cuántas partes hubo en total?", "20", "5 × 4 = 20.")],
  selfcheck=[("¿Qué partes tiene un buen mensaje de salud?", "Título, hechos con fuente y una recomendación", "Así informa con evidencia."), ("¿Por qué evitar «siempre» y «nunca»?", "Porque no hay evidencia para todos los casos", "Los riesgos cambian entre personas."), ("¿Se debe respetar a las personas que fuman? Responde Sí o No.", "Sí", "Se informa sin culpar.")],
  open_task=task("Diseña un afiche o un texto breve para tu curso sobre los efectos del humo del tabaco en el sistema respiratorio y circulatorio. Incluye un título, dos hechos con fuente (puedes decir «según un ministerio de salud»), una recomendación respetuosa y un límite. No uses imágenes violentas ni nombres de personas.", "Título: Cuida tus pulmones y tu corazón. Hecho 1: el humo irrita los bronquios (según un ministerio de salud). Hecho 2: el monóxido de carbono reduce el oxígeno de la sangre. Recomendación: evita el humo ajeno. Límite: el daño cambia entre personas.", ["título", "dos hechos con fuente", "recomendación respetuosa y límite"], ["afiche o texto", "lista de fuentes"], ["usar palabras absolutas", "culpar o burlarse"], "Pregunta cómo sabe que sus hechos son confiables y cómo reaccionaría alguien que fuma al leerlo."),
  reinforce="Reescribe una frase absoluta del tema con palabras más prudentes.",
  extend="Explica por qué un mensaje respetuoso puede ayudar más que uno que asusta.")

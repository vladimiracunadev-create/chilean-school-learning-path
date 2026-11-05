"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 15 (soluciones, componentes y concentración) y OA 16 (propiedades coligativas en procesos cotidianos)."""
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


OA15 = "CN2M OA 15"
OA16 = "CN2M OA 16"
MAT = "Este cuaderno y lápiz. Todos los datos están escritos en el cuaderno y son de ejemplo; no necesitas manipular sustancias."

# ---------------------------------------------------------------- OA 15

L(OA15, 1,
  materials=MAT,
  use="Aprenderé qué es una solución, cuáles son sus componentes y en qué estados físicos puede estar. También escribiré una pregunta que se pueda investigar sobre soluciones.",
  prior=["Sé que la materia está formada por partículas.", "Sé distinguir mezclas en las que se ven los componentes y mezclas en las que no."],
  explain=[
      "Una solución es una mezcla homogénea: tiene el mismo aspecto y las mismas propiedades en toda su extensión, y sus componentes no se distinguen a simple vista. Tiene al menos dos componentes. El soluto es la sustancia que se disuelve y suele estar en menor cantidad. El solvente es la sustancia que disuelve y suele estar en mayor cantidad. En el agua con azúcar, el azúcar es el soluto y el agua es el solvente.",
      "Las soluciones pueden ser sólidas, líquidas o gaseosas, y su estado físico suele ser el del solvente. El aire limpio es una solución gaseosa, formada por nitrógeno, oxígeno y otros gases. El agua con sal es una solución líquida. Una aleación como el bronce, hecha de cobre y estaño, es una solución sólida. En cambio, el agua con arena es una mezcla heterogénea, porque la arena se ve en el fondo.",
      "Una pregunta investigable nombra qué se cambia y qué se mide. «¿Tarda menos segundos en disolverse una cucharadita de azúcar en agua tibia de la llave que en agua fría?» se puede investigar con un reloj. «¿Cuál solución es más rica?» no se puede investigar, porque depende del gusto de cada persona. Nunca se prueban sustancias en un experimento: las observaciones se hacen con la vista y con instrumentos.",
  ],
  vocab=[("solución", "mezcla homogénea de dos o más sustancias"), ("soluto", "sustancia que se disuelve"), ("solvente", "sustancia que disuelve al soluto"), ("mezcla homogénea", "mezcla igual en toda su extensión, sin componentes visibles"), ("aleación", "solución sólida de metales")],
  worked=[
      ("Soluto y solvente", "Una persona disuelve jugo en polvo en un jarro de agua y revuelve hasta que no se ven granos. Identifica soluto, solvente y estado de la solución.", ["El jugo en polvo es lo que se disuelve: es el soluto.", "El agua disuelve y está en mayor cantidad: es el solvente.", "El resultado es líquido, como el solvente."], "Soluto: jugo en polvo; solvente: agua; solución líquida"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Es bonito el agua con sal?» para poder investigarla.", ["Quito la palabra de opinión, «bonito».", "Elijo qué medir: los segundos que tarda una cucharadita de sal en dejar de verse.", "Elijo qué comparar: agua fría y agua tibia de la llave."], "«¿Tarda menos segundos en disolverse una cucharadita de sal en agua tibia que en agua fría?»"),
  ],
  mistakes=[
      ("Decir que el soluto es siempre el sólido.", "El soluto es lo que se disuelve y está en menor cantidad; en una bebida con gas el soluto es un gas.", "Pregunta: ¿qué sustancia se disuelve en la otra?"),
      ("Llamar solución a toda mezcla con agua.", "Si se ven los componentes, como la arena en el fondo, es una mezcla heterogénea.", "Revisa si la mezcla es igual en toda su extensión."),
  ],
  rec=[
      ("¿Cómo se llama la sustancia que se disuelve en una solución?", "Soluto", "Es el componente que se disuelve, en menor cantidad."),
      ("Verdadero o falso: una solución es una mezcla homogénea.", "Verdadero", "Es igual en toda su extensión y no se distinguen sus componentes."),
      ("En el agua con azúcar, ¿cuál es el solvente?", "El agua", "Es la sustancia que disuelve y está en mayor cantidad."),
  ],
  und=[
      ("El aire limpio es una mezcla de gases que se ve igual en todas partes. ¿Qué tipo de solución es? A) Gaseosa; B) Líquida.", "A", "El estado físico de la solución es el del solvente, que aquí es un gas."),
      ("¿Por qué el agua con sal es una solución y el agua con arena no? A) Porque la sal no se distingue a simple vista y la arena sí; B) Porque la sal pesa menos que la arena.", "A", "En una solución los componentes no se distinguen; la arena se ve en el fondo."),
      ("Un bronce de ejemplo tiene 90 g de cobre y 10 g de estaño. ¿Cuál es el solvente?", "El cobre", "Es el componente que está en mayor cantidad."),
  ],
  app=[
      ("¿Cuál de estas preguntas es investigable? A) ¿Cuántos gramos de azúcar caben en 100 mL de agua antes de que quede azúcar en el fondo?; B) ¿Es más agradable el té con más azúcar?", "A", "Indica qué medir; la otra depende de una opinión."),
      arith("Una solución de ejemplo tiene una masa total de 500 g y contiene 40 g de soluto. ¿Cuántos gramos de solvente hay?", "500-40", "La masa del solvente es la masa total menos la del soluto.", " g"),
      ("Una bebida con gas contiene dióxido de carbono, un gas, disuelto en agua. ¿Cuál es el soluto?", "El dióxido de carbono", "Es la sustancia que está disuelta en el agua."),
  ],
  rea=[
      ("Un compañero dice: «El agua con granos de arena en el fondo es una solución». ¿Qué le respondes? A) No: se distinguen los componentes, es una mezcla heterogénea; B) Sí: la arena está dentro del agua.", "A", "Una solución es homogénea y la arena se ve separada."),
      ("¿Qué le falta a la pregunta «¿Sirve más el agua tibia?» para ser investigable? A) Decir qué se mide, por ejemplo segundos; B) Hacerla más larga.", "A", "Sin una variable medible no hay datos que comparar."),
  ],
  cha=[
      ("Para comparar cuánto tarda en disolverse el azúcar en agua fría y en agua tibia, ¿qué debe mantenerse igual en ambos vasos? A) La temperatura del agua; B) La cantidad de agua y de azúcar.", "B", "Solo se cambia la temperatura; lo demás se controla."),
      ("En un aire de ejemplo, el nitrógeno es el gas más abundante y hay oxígeno y otros gases en menor cantidad. Si se elige un solvente, ¿cuál es? A) El nitrógeno; B) El oxígeno.", "A", "El solvente es el componente que está en mayor cantidad."),
  ],
  context=[("Un jugo de ejemplo se prepara con agua, jugo de limón colado y azúcar disuelta, sin trozos visibles. ¿Es una solución o una mezcla heterogénea?", "Solución", "No se ven los componentes y es igual en todo el vaso.")],
  selfcheck=[("¿Qué es el solvente?", "La sustancia que disuelve y está en mayor cantidad", "Disuelve al soluto."), ("¿Una aleación de metales es una solución sólida?", "Sí", "Sus componentes se mezclan de modo homogéneo en estado sólido."), ("¿Qué debe tener una pregunta investigable?", "Algo que se pueda medir y qué se compara", "Así se obtienen datos.")],
  open_task=task("Lee estos casos: (1) té con azúcar sin trozos; (2) agua con piedrecitas; (3) aire limpio. Para cada uno escribe si es solución o no, y en las soluciones nombra soluto, solvente y estado. Luego escribe una pregunta investigable sobre qué cambia la rapidez con que se disuelve el azúcar en agua.", "Té con azúcar: solución líquida; soluto azúcar, solvente agua. ¿Tarda menos segundos en disolverse una cucharadita de azúcar si el agua está tibia que si está fría?", ["clasifica los tres casos", "nombra soluto y solvente donde corresponde", "la pregunta nombra qué se cambia y qué se mide"], ["tres clasificaciones y una pregunta"], ["llamar solución a agua con piedrecitas", "escribir una pregunta de opinión"], "Pregunta qué se mediría en tu pregunta y con qué instrumento."),
  reinforce="Escribe tres soluciones que conozcas y nombra el soluto y el solvente de cada una.",
  extend="Explica por qué el aire limpio y el bronce son soluciones aunque no sean líquidos.")

TAB = "Tabla de ejemplo con 100 mL de agua en cada vaso y la misma temperatura: vaso 1, 10 g de sal, sin sobrante; vaso 2, 20 g, sin sobrante; vaso 3, 30 g, sin sobrante; vaso 4, 40 g, con 4 g sin disolver en el fondo. "

L(OA15, 2,
  materials=MAT,
  use="Aprenderé a leer una tabla de datos sobre soluciones, a distinguir una solución diluida, concentrada y saturada, y a reconocer qué conclusiones permiten los datos.",
  prior=["Sé qué es una solución, un soluto y un solvente.", "Sé leer una tabla con unidades."],
  explain=[
      "La concentración de una solución indica cuánto soluto hay disuelto en una cantidad determinada de solución. Se puede expresar, por ejemplo, en gramos de soluto por cada 100 mL o por cada litro de solución. Una solución diluida tiene poco soluto disuelto y una concentrada tiene mucho, comparadas con otra del mismo solvente.",
      "A una temperatura dada, el solvente puede disolver una cantidad máxima de soluto. Cuando ya no disuelve más y el soluto sobrante queda en el fondo, la solución está saturada. Por eso, en una tabla, la masa disuelta no es siempre la masa agregada: se calcula restando la masa que quedó sin disolver.",
      "Al leer una tabla se comprueba qué variable se cambió, qué se midió y qué se mantuvo igual. Las conclusiones solo valen para las condiciones de los datos: si la tabla se hizo a una sola temperatura, no se puede afirmar lo mismo a otras temperaturas.",
  ],
  vocab=[("concentración", "cantidad de soluto disuelta en una cantidad de solución"), ("diluida", "con poco soluto disuelto"), ("concentrada", "con mucho soluto disuelto"), ("saturada", "que ya no disuelve más soluto a esa temperatura"), ("sobrante", "soluto que queda sin disolver")],
  worked=[
      ("Masa disuelta", "En un vaso de ejemplo con 100 mL de agua se agregan 50 g de azúcar y quedan 6 g sin disolver. ¿Cuántos gramos se disolvieron y cómo está la solución?", ["Gramos disueltos = gramos agregados − gramos sobrantes = 50 − 6 = 44.", "Como queda soluto sin disolver, la solución ya no admite más.", "Entonces está saturada a esa temperatura."], "44 g disueltos; solución saturada"),
      ("Comparar vasos", "El vaso X tiene 5 g de sal en 100 mL y el vaso Y tiene 15 g en 100 mL, sin sobrante. ¿Cuál es más concentrado?", ["Los dos tienen el mismo volumen de solución.", "El vaso Y tiene más soluto en ese volumen.", "Por lo tanto Y es más concentrado y X más diluido."], "El vaso Y es más concentrado"),
  ],
  mistakes=[
      ("Contar como disuelto todo lo que se agregó.", "El soluto sobrante no está disuelto.", "Resta la masa que quedó en el fondo."),
      ("Generalizar a cualquier temperatura.", "Los datos de la tabla valen solo para la temperatura en que se midieron.", "Escribe la condición junto a la conclusión."),
  ],
  rec=[
      ("¿Cómo se llama una solución que ya no disuelve más soluto?", "Saturada", "El soluto sobrante queda en el fondo."),
      ("Verdadero o falso: una solución con poco soluto disuelto es diluida.", "Verdadero", "Diluida significa poco soluto en la cantidad de solución."),
      ("¿Qué indica la concentración de una solución?", "Cuánto soluto hay disuelto en una cantidad de solución", "Relaciona la cantidad de soluto con la de solución."),
  ],
  und=[
      (TAB + "¿En qué vaso apareció sal sin disolver? A) En el vaso 4; B) En el vaso 3.", "A", "Solo el vaso 4 tiene un sobrante en el fondo."),
      arith(TAB + "¿Cuántos gramos de sal se disolvieron en el vaso 4?", "40-4", "Se restan los gramos sobrantes a los agregados.", " g"),
      (TAB + "Entre los vasos 1 y 3, ¿cuál tiene la solución más diluida?", "El vaso 1", "Tiene menos sal en el mismo volumen de agua."),
  ],
  app=[
      arith(TAB + "¿Cuántos gramos más de sal tiene disuelta el vaso 3 que el vaso 1?", "30-10", "Se comparan las masas disueltas, sin sobrante en ambos.", " g"),
      arith(TAB + "Una persona prepara 3 vasos iguales al vaso 3. ¿Cuántos gramos de sal necesita en total?", "30*3", "Cada vaso lleva 30 g y son tres vasos.", " g"),
      (TAB + "Se grafican los gramos disueltos según los gramos agregados. ¿Qué ocurre con la línea al llegar a 40 g agregados? A) Deja de subir a la par, porque no todo se disuelve; B) Sigue subiendo igual que antes.", "A", "Desde 40 g agregados ya no todo el soluto se disuelve."),
  ],
  rea=[
      (TAB + "Un compañero dice: «En el vaso 4 hay 40 g de sal disueltos». ¿Qué le respondes? A) Hay 36 g disueltos, porque 4 g quedaron en el fondo; B) Tiene razón, porque se agregaron 40 g.", "A", "Lo sobrante no está disuelto, así que se resta."),
      (TAB + "¿Se puede asegurar con estos datos que 36 g es el máximo disuelto a cualquier temperatura? A) No: los datos son de una sola temperatura; B) Sí: la tabla lo demuestra.", "A", "Una tabla vale solo para las condiciones en que se obtuvo."),
  ],
  cha=[
      arith("Un vaso de ejemplo con 100 mL de agua disuelve como máximo 36 g de sal. Si se le agregan 50 g, ¿cuántos gramos quedan sin disolver?", "50-36", "Se resta el máximo disuelto a lo agregado.", " g"),
      (TAB + "Se agregan 100 mL de agua pura al vaso 3 y se revuelve. ¿Cómo queda la solución? A) Más diluida; B) Más concentrada.", "A", "La misma masa de sal queda repartida en más solvente."),
  ],
  context=[("Vaso de ejemplo: una persona cree que un vaso con cinco cucharaditas de sal en agua tibia se saturó porque al final vio sal en el fondo. ¿Qué observación respalda que está saturada? A) Quedó sal sin disolver en el fondo; B) El agua estaba tibia.", "A", "El sobrante en el fondo indica que ya no disuelve más.")],
  selfcheck=[("¿Cómo se calcula la masa disuelta si queda un sobrante?", "Masa agregada menos masa sobrante", "El sobrante no está disuelto."), ("¿Qué significa que una solución está saturada?", "Que ya no disuelve más soluto a esa temperatura", "Queda soluto en el fondo."), ("¿Por qué una conclusión debe indicar la temperatura?", "Porque los datos valen solo para esa condición", "Puede cambiar a otra temperatura.")],
  open_task=task("Con esta tabla de ejemplo (100 mL de agua, misma temperatura): vaso A, 15 g de azúcar, sin sobrante; vaso B, 35 g, sin sobrante; vaso C, 60 g, con 8 g sin disolver. Calcula los gramos disueltos en cada vaso, ordena los vasos de más diluido a más concentrado y escribe una conclusión con su condición.", "Vaso A: 15 g; vaso B: 35 g; vaso C: 60 − 8 = 52 g. Orden: A, B, C. A esa temperatura, el vaso C está saturado porque tiene sobrante.", ["calcula las tres masas disueltas", "ordena los vasos", "indica la condición de la conclusión"], ["tabla de tres resultados y una conclusión"], ["no restar el sobrante", "olvidar la condición de temperatura"], "Pregunta qué cambiaría si el agua estuviera más fría."),
  reinforce="Escribe con tus palabras la diferencia entre solución diluida, concentrada y saturada.",
  extend="Explica por qué la masa que se agrega a un vaso no siempre es la masa que se disuelve.")

L(OA15, 3,
  materials=MAT,
  use="Aprenderé a usar el modelo de partículas para explicar qué pasa cuando un soluto se disuelve y a contrastarlo con un modelo equivocado.",
  prior=["Sé que la materia está formada por partículas.", "Sé que la masa total se conserva en una mezcla."],
  explain=[
      "En el modelo de partículas, el solvente está formado por partículas que se mueven y chocan. Cuando se agrega un soluto, sus partículas se separan unas de otras y se distribuyen entre las partículas del solvente. Por eso la mezcla se ve igual en toda su extensión y el soluto deja de verse.",
      "El soluto no desaparece: sus partículas siguen ahí. Esto se comprueba con una balanza, porque la masa de la solución es la suma de la masa del soluto y la del solvente. Si se mezclan 100 g de agua y 10 g de sal, la solución tiene 110 g. En agua más tibia las partículas se mueven más, y por eso el soluto suele disolverse más rápido.",
      "Un modelo es una representación que explica y predice, pero tiene límites. Un dibujo con círculos no muestra el tamaño real de las partículas ni su movimiento. Para contrastar dos modelos se pregunta cuál explica mejor la evidencia. El modelo «la sal desaparece» no explica que la masa se conserve, y el modelo de partículas sí.",
  ],
  vocab=[("modelo", "representación que explica un fenómeno y permite predecir"), ("partícula", "porción muy pequeña de materia"), ("conservación de la masa", "la masa total no cambia al mezclar"), ("disolver", "separar las partículas del soluto entre las del solvente"), ("evidencia", "dato u observación que apoya una explicación")],
  worked=[
      ("Masa de una solución", "Se mezclan 200 g de agua y 20 g de azúcar hasta que no se ven granos. ¿Cuál es la masa de la solución?", ["La masa se conserva, así que se suman las dos masas.", "200 + 20 = 220."], "220 g"),
      ("Contrastar modelos", "Modelo A: la sal desaparece. Modelo B: la sal se separa en partículas entre las del agua. Evidencia: la balanza marca lo mismo antes y después de disolver. ¿Qué modelo apoya la evidencia?", ["Si la sal desapareciera, la masa total sería menor.", "La balanza marca lo mismo, así que la materia sigue ahí.", "Eso coincide con el modelo B."], "Modelo B"),
  ],
  mistakes=[
      ("Pensar que el soluto desaparece al disolverse.", "Sus partículas siguen en la solución y su masa se suma.", "Usa la balanza como evidencia: la masa se conserva."),
      ("Creer que el dibujo del modelo muestra el tamaño real.", "Un modelo es una representación con límites.", "Anota al menos un límite de tu modelo."),
  ],
  rec=[
      ("Verdadero o falso: al disolverse, el soluto desaparece.", "Falso", "Sus partículas siguen en la solución."),
      ("¿Qué se conserva al disolver un soluto en un solvente?", "La masa", "La masa de la solución es la suma de las masas."),
      ("¿Qué hacen las partículas del soluto al disolverse?", "Se separan y se distribuyen entre las del solvente", "Por eso la mezcla se ve homogénea."),
  ],
  und=[
      ("En un dibujo, 6 círculos representan el soluto repartidos entre 30 círculos del solvente. ¿Por qué el dibujo representa una solución? A) Porque las partículas del soluto están distribuidas entre las del solvente; B) Porque hay más partículas de solvente.", "A", "La distribución uniforme es lo que hace homogénea a la mezcla."),
      ("¿Por qué el azúcar suele disolverse más rápido en agua tibia que en agua fría? A) Porque las partículas se mueven más; B) Porque el azúcar pesa menos.", "A", "Más movimiento facilita separar y repartir las partículas."),
      ("¿Cuál es un límite de un dibujo de círculos como modelo de una solución?", "No muestra el tamaño real ni el movimiento", "Un modelo simplifica la realidad."),
  ],
  app=[
      arith("Se mezclan 150 g de agua y 25 g de sal. ¿Cuál es la masa de la solución?", "150+25", "La masa se conserva, así que se suman.", " g"),
      arith("Una balanza marca 340 g para una solución de ejemplo hecha con 300 g de agua. ¿Cuántos gramos de soluto se disolvieron?", "340-300", "La masa del soluto es la de la solución menos la del solvente.", " g"),
      ("Una balanza marca 210 g antes de disolver el azúcar y 210 g después. ¿Qué modelo apoya este dato? A) El soluto sigue en la mezcla; B) El soluto desapareció.", "A", "Si hubiera desaparecido, la masa habría disminuido."),
  ],
  rea=[
      ("Un compañero dice: «Como no veo la sal, ya no hay sal». ¿Qué evidencia sirve para responderle? A) Que la masa de la solución es igual a la suma de masas; B) Que el agua quedó transparente.", "A", "Lo que se ve no prueba que la sal ya no esté."),
      ("¿Por qué un modelo de partículas es mejor que «la sal desaparece»? A) Explica que la masa se conserve; B) Es más fácil de dibujar.", "A", "Un buen modelo debe coincidir con la evidencia."),
  ],
  cha=[
      arith("Una solución de ejemplo tiene 480 g de masa y se hizo con 60 g de soluto. ¿Cuántos gramos de solvente se usaron?", "480-60", "Se resta la masa del soluto a la de la solución.", " g"),
      ("Un estudiante dibuja el soluto agrupado en una esquina del vaso. ¿Qué debe corregir? A) Distribuir las partículas del soluto entre las del solvente; B) Dibujar más solvente.", "A", "En una solución las partículas están repartidas."),
  ],
  context=[arith("Una persona de ejemplo disuelve 35 g de azúcar en 265 g de agua para una limonada de ejemplo. ¿Cuántos gramos tendrá la limonada, sin contar el limón?", "35+265", "La masa de la solución es la suma de la masa del soluto y la del solvente.", " g")],
  selfcheck=[("¿Cómo se distribuyen las partículas del soluto en una solución?", "Entre las partículas del solvente", "Eso hace homogénea la mezcla."), ("¿Qué muestra la balanza sobre el soluto disuelto?", "Que su masa se conserva", "La masa de la solución es la suma."), ("Nombra un límite de un modelo de partículas dibujado.", "No muestra el tamaño real ni el movimiento", "Es una simplificación.")],
  open_task=task("Dibuja dos recuadros: antes y después de disolver 8 círculos negros (soluto) en 32 círculos blancos (solvente). Escribe qué evidencia de masa apoya tu dibujo con estos datos de ejemplo: 120 g de agua y 12 g de soluto. Escribe un límite de tu modelo.", "Antes: 8 círculos juntos; después: 8 círculos repartidos entre los blancos. Masa de la solución: 120 + 12 = 132 g. Límite: los círculos no muestran el tamaño real.", ["el dibujo distribuye el soluto", "calcula 132 g", "declara un límite"], ["dibujo, cálculo y una oración"], ["dibujar el soluto agrupado", "decir que la masa disminuye"], "Pregunta cómo cambiaría el dibujo si el agua estuviera más tibia."),
  reinforce="Explica con el modelo de partículas por qué el azúcar disuelto no se ve.",
  extend="Escribe una evidencia que sirva para descartar el modelo «el soluto desaparece».")

L(OA15, 4,
  materials=MAT,
  use="Aprenderé a calcular la concentración de una solución en gramos por litro y en porcentaje, y a explicar cómo cambia al agregar soluto o solvente.",
  prior=["Sé qué es una solución diluida y una concentrada.", "Sé multiplicar y dividir números enteros."],
  explain=[
      "La concentración relaciona la cantidad de soluto con la cantidad de solución. En gramos por litro (g/L) se divide la masa de soluto en gramos por el volumen de solución en litros. El porcentaje masa/volumen (% m/v) indica los gramos de soluto en 100 mL de solución. El porcentaje masa/masa (% m/m) indica los gramos de soluto en 100 g de solución.",
      "Para calcular el porcentaje se divide la masa de soluto por la cantidad de solución y se multiplica por 100. Por ejemplo, 20 g de soluto en 200 g de solución son 20 ÷ 200 × 100 = 10 % m/m. Cuando la cantidad de soluto aumenta y el volumen se mantiene, la concentración sube. Cuando el soluto es el mismo y el volumen aumenta, la concentración baja.",
      "Diluir es agregar solvente. Al diluir, la masa de soluto no cambia, pero la concentración disminuye porque la misma masa queda repartida en más solución. Si 20 g de soluto están en 100 mL, la concentración es 20 % m/v; al completar hasta 200 mL, es 10 % m/v. Una conclusión sobre concentración siempre debe nombrar la unidad.",
  ],
  vocab=[("g/L", "gramos de soluto por litro de solución"), ("% m/v", "gramos de soluto en 100 mL de solución"), ("% m/m", "gramos de soluto en 100 g de solución"), ("diluir", "agregar solvente para bajar la concentración"), ("volumen", "espacio que ocupa la solución")],
  worked=[
      ("Gramos por litro", "Una solución de ejemplo tiene 60 g de soluto en 3 L de solución. ¿Cuál es su concentración en g/L?", ["Se divide la masa de soluto por el volumen.", "60 ÷ 3 = 20."], "20 g/L"),
      ("Porcentaje masa/masa", "Una solución de ejemplo de 300 g contiene 30 g de soluto. ¿Qué % m/m tiene?", ["Se divide el soluto por la solución: 30 ÷ 300 = 0,1.", "Se multiplica por 100: 0,1 × 100 = 10."], "10 % m/m"),
  ],
  mistakes=[
      ("Dividir el soluto por el volumen de solvente.", "La concentración usa el volumen o la masa de la solución completa.", "Identifica la cantidad de solución antes de dividir."),
      ("Pensar que al diluir se pierde soluto.", "Al diluir, la masa de soluto es la misma; solo cambia el volumen.", "Compara los gramos de soluto antes y después."),
  ],
  rec=[
      ("¿Qué unidad expresa los gramos de soluto por cada litro de solución?", "g/L", "Relaciona la masa de soluto con el volumen en litros."),
      ("Verdadero o falso: al agregar más solvente, la solución se vuelve más diluida.", "Verdadero", "El mismo soluto queda repartido en más solución."),
      ("¿Cuántos gramos de soluto hay en 100 mL de una solución de 8 % m/v?", "8 g", "El % m/v indica gramos de soluto en 100 mL."),
  ],
  und=[
      ("Dos soluciones tienen el mismo volumen. La primera tiene 12 g de soluto y la segunda 30 g. ¿Cuál es más concentrada? A) La primera; B) La segunda.", "B", "A igual volumen, más soluto significa mayor concentración."),
      ("Si se agrega agua a una solución, la masa de soluto, ¿qué hace? A) Se mantiene; B) Disminuye.", "A", "Diluir no quita soluto, solo agrega solvente."),
      ("¿Cómo se llama el proceso de agregar solvente para bajar la concentración?", "Dilución", "Se reparte el mismo soluto en más solución."),
  ],
  app=[
      arith("Una solución de ejemplo tiene 24 g de soluto en 4 L de solución. ¿Cuál es su concentración en g/L?", "24//4", "Se divide la masa de soluto por el volumen.", " g/L"),
      arith("Una solución de ejemplo tiene 15 g de soluto en 150 mL de solución. ¿Cuál es su concentración en % m/v?", "15*100//150", "Los gramos por 100 mL: 15 ÷ 150 × 100.", " % m/v"),
      arith("Una solución de ejemplo de 250 mL tiene una concentración de 4 % m/v. ¿Cuántos gramos de soluto contiene?", "250*4//100", "4 g por cada 100 mL: 250 × 4 ÷ 100.", " g"),
  ],
  rea=[
      ("Una persona dice: «Si agrego agua a una solución de 20 g de soluto en 100 mL hasta completar 400 mL, quedan 5 g de soluto». ¿Es correcto? A) No: quedan 20 g de soluto, con concentración menor; B) Sí: el agua quita soluto.", "A", "El soluto no se pierde; se reparte en más volumen."),
      ("¿Por qué no se pueden comparar dos soluciones solo mirando el número 5 si una dice 5 g/L y la otra 5 % m/v? A) Porque las unidades son distintas; B) Porque 5 es un número muy pequeño.", "A", "Hay que expresar ambas en la misma unidad para comparar."),
  ],
  cha=[
      arith("Una solución de ejemplo tiene 30 g de soluto en 100 mL. Se completa con agua hasta 600 mL. ¿Cuál es la nueva concentración en % m/v?", "30*100//600", "Los 30 g quedan en 600 mL: 30 ÷ 600 × 100.", " % m/v"),
      arith("Para preparar 2 L de una solución de 15 g/L, ¿cuántos gramos de soluto se necesitan?", "15*2", "Se multiplica la concentración por el volumen.", " g"),
  ],
  context=[arith("Una persona adulta prepara 5 L de una limonada de ejemplo con 250 g de azúcar. ¿Cuál es la concentración de azúcar en g/L?", "250//5", "Se divide la masa de azúcar por el volumen de limonada.", " g/L")],
  selfcheck=[("¿Qué indica el % m/v?", "Los gramos de soluto en 100 mL de solución", "Es una forma de expresar concentración."), ("¿Qué le pasa a la concentración al agregar solvente?", "Disminuye", "El soluto queda repartido en más solución."), ("¿Por qué hay que escribir la unidad de la concentración?", "Porque el número solo no dice si es g/L o porcentaje", "Cambia el significado.")],
  open_task=task("Con estos datos de ejemplo calcula la concentración de cada solución en g/L y ordénalas de menos a más concentrada: solución 1, 18 g en 2 L; solución 2, 45 g en 3 L; solución 3, 10 g en 1 L. Luego escribe qué pasaría con la solución 2 si se le agregara más agua.", "Solución 1: 9 g/L; solución 2: 15 g/L; solución 3: 10 g/L. Orden: 1, 3, 2. Con más agua, la solución 2 quedaría más diluida porque los 45 g se repartirían en más litros.", ["calcula las tres concentraciones", "ordena correctamente", "explica el efecto de diluir"], ["tres cálculos, un orden y una explicación"], ["dividir sin usar el volumen de solución", "decir que el soluto se pierde al diluir"], "Pregunta cuántos litros tendría que tener la solución 2 para igualar a la solución 1."),
  reinforce="Calcula la concentración en g/L de 36 g de soluto en 4 L de solución de ejemplo.",
  extend="Explica por qué diluir no cambia la masa de soluto pero sí la concentración.")

# ---------------------------------------------------------------- OA 16

L(OA16, 1,
  materials=MAT,
  use="Aprenderé qué son las propiedades coligativas y escribiré una pregunta que se pueda investigar sobre cómo un soluto cambia la temperatura de congelación o de ebullición del agua.",
  prior=["Sé que el agua pura se congela a 0 °C y hierve a 100 °C a nivel del mar.", "Sé qué es una solución y qué es el soluto."],
  explain=[
      "Una propiedad coligativa es una propiedad de una solución que depende de cuántas partículas de soluto hay disueltas, y no de cuál es el soluto. Son cuatro: el descenso de la presión de vapor, el ascenso del punto de ebullición, el descenso del punto de congelación y la presión osmótica. En esta clase te concentras en las dos de temperatura.",
      "El agua pura, a nivel del mar, se congela a 0 °C y hierve a 100 °C. Si se disuelve en ella un soluto que no se evapora, como la sal o el azúcar, la solución se congela a una temperatura menor que 0 °C y hierve a una temperatura mayor que 100 °C. El descenso del punto de congelación se llama descenso crioscópico y el ascenso del punto de ebullición se llama ascenso ebulloscópico.",
      "Una pregunta investigable nombra qué se cambia y qué se mide. «¿Baja la temperatura de congelación del agua a medida que aumenta la masa de sal disuelta?» se puede investigar con un termómetro. «¿Qué solución es mejor?» no se puede investigar. En esta unidad usarás datos de ejemplo: si algún día quieres comprobar algo con calor o frío, hazlo siempre con una persona adulta.",
  ],
  vocab=[("propiedad coligativa", "propiedad de una solución que depende de la cantidad de partículas de soluto"), ("descenso crioscópico", "baja del punto de congelación por un soluto disuelto"), ("ascenso ebulloscópico", "alza del punto de ebullición por un soluto disuelto"), ("punto de congelación", "temperatura a la que un líquido pasa a sólido"), ("punto de ebullición", "temperatura a la que un líquido hierve")],
  worked=[
      ("Reconocer una coligativa", "¿Es el color de una solución una propiedad coligativa? Responde con un criterio.", ["Una propiedad coligativa depende de cuántas partículas de soluto hay disueltas.", "El color depende de qué sustancia es el soluto, no solo de cuántas partículas hay."], "No es coligativa; el punto de congelación sí lo es"),
      ("Mejorar una pregunta", "Mejora «¿Qué le hace la sal al agua?» para poder investigarla.", ["Elijo una propiedad que se mida: la temperatura de congelación.", "Indico qué se cambia: la masa de sal en 100 g de agua."], "«¿Baja la temperatura de congelación del agua al aumentar la masa de sal disuelta en 100 g de agua?»"),
  ],
  mistakes=[
      ("Pensar que la sal «enfría» el agua.", "La sal no cambia la temperatura del agua al disolverse; cambia la temperatura a la que la solución se congela.", "Habla de punto de congelación, no de temperatura del agua."),
      ("Decir que la solución se congela a 0 °C como el agua pura.", "El soluto baja la temperatura de congelación.", "Compara siempre con el valor del agua pura."),
  ],
  rec=[
      ("¿A qué temperatura se congela el agua pura a nivel del mar?", "0 °C", "Es su punto de congelación."),
      ("¿Cómo se llama el ascenso del punto de ebullición por un soluto?", "Ascenso ebulloscópico", "Es una propiedad coligativa."),
      ("Verdadero o falso: una propiedad coligativa depende de la cantidad de partículas de soluto disueltas.", "Verdadero", "Esa es la definición de propiedad coligativa."),
  ],
  und=[
      ("Al disolver sal en agua, la temperatura de congelación de la solución, ¿cómo cambia? A) Baja respecto de 0 °C; B) Sube respecto de 0 °C.", "A", "Es el descenso crioscópico."),
      ("¿Cuál de estas es una propiedad coligativa? A) El color de la solución; B) El punto de congelación de la solución.", "B", "Depende de cuántas partículas hay disueltas."),
      ("Al disolver azúcar en agua, la temperatura de ebullición, ¿cómo cambia? A) Sube respecto de 100 °C; B) Baja respecto de 100 °C.", "A", "Es el ascenso ebulloscópico."),
  ],
  app=[
      ("¿Cuál pregunta es investigable? A) ¿Baja la temperatura de congelación al aumentar la masa de sal en 100 g de agua?; B) ¿Es mejor la sal que el azúcar?", "A", "La que pregunta por la temperatura de congelación indica qué cambiar y qué medir; la otra no."),
      arith("Una solución de ejemplo se congela a −5 °C y hierve a 101 °C. ¿Cuántos grados separan estas dos temperaturas?", "101-(-5)", "Se restan los dos valores; es el intervalo en que la solución es líquida.", " °C"),
      ("En un experimento se miden las temperaturas de congelación con 0, 5 y 10 g de sal en 100 g de agua. ¿Cuál es la variable que se mide? A) La masa de sal; B) La temperatura de congelación.", "B", "Lo que se mide como resultado es la temperatura."),
  ],
  rea=[
      ("Un compañero dice: «La sal enfría el agua, por eso se congela antes». ¿Qué le respondes? A) La sal baja el punto de congelación, así que la solución necesita menos de 0 °C para congelarse; B) Tiene razón, la sal enfría.", "A", "La solución se congela a menor temperatura, no antes."),
      ("¿Por qué «¿Qué solución es mejor?» no sirve como pregunta de investigación? A) No dice qué se mide ni qué se compara; B) Es muy corta.", "A", "Sin variable medible no hay datos."),
  ],
  cha=[
      ("Dos soluciones de ejemplo tienen 100 g de agua. La primera tiene 10 g de sal y la segunda 20 g. ¿Cuál se congela a menor temperatura? A) La de 20 g; B) La de 10 g.", "A", "Más partículas disueltas producen mayor descenso."),
      ("Un estudiante afirma que el soluto solo cambia el punto de congelación. ¿Qué corriges? A) También sube el punto de ebullición; B) También cambia el color del agua.", "A", "El ascenso ebulloscópico también es coligativo."),
  ],
  context=[("En una vereda con hielo, una persona adulta esparce sal y el hielo comienza a derretirse aunque la temperatura sigue bajo 0 °C. ¿Qué propiedad coligativa lo explica? A) El descenso del punto de congelación; B) El ascenso del punto de ebullición.", "A", "La mezcla de sal y agua se congela a menor temperatura que el agua pura.")],
  selfcheck=[("¿De qué depende una propiedad coligativa?", "De la cantidad de partículas de soluto disueltas", "No depende de cuál sea el soluto."), ("¿Qué le pasa al punto de ebullición del agua al disolver sal?", "Sube", "Es el ascenso ebulloscópico."), ("¿Qué debe tener una pregunta investigable?", "Qué se cambia y qué se mide", "Permite reunir datos.")],
  open_task=task("Lee estos tres enunciados: (1) «La sal enfría el agua»; (2) «El agua con sal es peor»; (3) «Al aumentar la sal disuelta en 100 g de agua, la temperatura de congelación baja». Indica cuál se puede investigar y por qué. Luego escribe una pregunta investigable sobre la temperatura de ebullición y el azúcar.", "El enunciado 3 se puede investigar porque indica qué cambia y qué se mide. Pregunta: ¿sube la temperatura de ebullición del agua al aumentar la masa de azúcar disuelta en 100 g de agua? (Con datos de ejemplo; el calor lo maneja una persona adulta.)", ["elige el enunciado correcto con razón", "la pregunta nombra qué cambia y qué se mide"], ["una elección y una pregunta"], ["elegir un enunciado de opinión", "no incluir qué se mide"], "Pregunta qué instrumento mediría la temperatura."),
  reinforce="Escribe dos propiedades coligativas y qué le pasa a cada una al disolver un soluto.",
  extend="Explica por qué el color de una solución no es una propiedad coligativa.")

TCON = "Tabla de ejemplo, temperatura de congelación del agua según la sal disuelta en 100 g de agua: 0 g, 0 °C; 5 g, −3 °C; 10 g, −6 °C; 15 g, −9 °C. "

L(OA16, 2,
  materials=MAT,
  use="Aprenderé a leer una tabla de datos sobre el descenso del punto de congelación, a describir el patrón y a decir hasta dónde llegan las conclusiones.",
  prior=["Sé qué es una propiedad coligativa.", "Sé leer una tabla con temperaturas negativas."],
  explain=[
      "Cuando se mide la temperatura de congelación de soluciones con distintas cantidades de soluto se obtiene una tabla. En ella, la variable que se cambia es la masa de soluto y la que se mide es la temperatura de congelación. Se mantiene igual la masa de agua y el instrumento. Con eso se puede buscar un patrón.",
      "En datos de ejemplo de sal en agua, cada 5 g de sal por 100 g de agua bajan la temperatura de congelación 3 °C. Este patrón es una relación casi proporcional: al duplicar la sal, el descenso se duplica. Cuanto mayor es la cantidad de soluto disuelto, mayor es el descenso crioscópico.",
      "Una conclusión no debe ir más allá de los datos. Si la tabla llega hasta 15 g de sal, predecir lo que pasa con 30 g es una suposición, no una medición. Además, un solo resultado no basta: se repite la medición para comprobar que no fue un error. Siempre se escribe qué datos son de ejemplo.",
  ],
  vocab=[("variable independiente", "la que se cambia a propósito"), ("variable dependiente", "la que se mide como resultado"), ("patrón", "regularidad que se repite en los datos"), ("extrapolar", "predecir fuera del rango de los datos"), ("repetición", "volver a medir para comprobar el resultado")],
  worked=[
      ("Leer el patrón", "En una tabla de ejemplo, 0 g de azúcar dan 0 °C, 20 g dan −1 °C y 40 g dan −2 °C. Describe el patrón.", ["Cada 20 g más de azúcar, la temperatura baja 1 °C.", "Al duplicar el azúcar de 20 g a 40 g, el descenso se duplica de 1 °C a 2 °C."], "A más soluto, mayor descenso, de forma proporcional"),
      ("Variables", "En esa misma tabla de ejemplo, ¿cuál es la variable independiente y cuál la dependiente?", ["Se cambia la masa de azúcar: es la independiente.", "Se mide la temperatura de congelación: es la dependiente."], "Independiente: masa de azúcar; dependiente: temperatura de congelación"),
  ],
  mistakes=[
      ("Afirmar un resultado fuera del rango de los datos como si estuviera medido.", "Extrapolar es una suposición y puede fallar.", "Escribe «se espera que», no «es»."),
      ("Confundir la variable que se cambia con la que se mide.", "La independiente se cambia y la dependiente se mide.", "Pregunta: ¿qué cambié y qué medí?"),
  ],
  rec=[
      (TCON + "¿Cuál es la temperatura de congelación con 10 g de sal?", "−6 °C", "Se lee directamente en la tabla."),
      (TCON + "Al aumentar la sal, la temperatura de congelación, ¿sube o baja?", "Baja", "Los valores de la tabla son cada vez más negativos."),
      ("Verdadero o falso: el agua pura de la tabla (0 g) se congela a 0 °C.", "Verdadero", "La primera fila indica 0 g de sal y 0 °C."),
  ],
  und=[
      arith(TCON + "¿Cuántos grados baja la temperatura de congelación por cada 5 g de sal agregados?", "-3-(-6)", "Se compara una fila con la siguiente: la diferencia es 3 °C.", " °C"),
      (TCON + "¿Con cuántos gramos de sal la solución se congela a −9 °C?", "15 g", "Se lee en la fila correspondiente."),
      (TCON + "¿Qué forma tiene el patrón? A) Baja de forma pareja con la sal agregada; B) Sube con la sal agregada.", "A", "Cada 5 g la temperatura baja lo mismo."),
  ],
  app=[
      arith(TCON + "Si el patrón se mantiene, ¿a qué temperatura se esperaría que se congele con 20 g de sal?", "-3*4", "Cada 5 g baja 3 °C; con 20 g son 4 tramos de 5 g.", " °C"),
      arith(TCON + "¿Cuántos grados más baja la temperatura de congelación con 15 g que con 5 g de sal?", "-3-(-9)", "Se comparan las filas de 5 g y de 15 g.", " °C"),
      (TCON + "¿Qué variable independiente se cambió? A) La masa de sal; B) La temperatura de congelación.", "A", "La masa de sal es la que se cambia a propósito."),
  ],
  rea=[
      (TCON + "Un compañero dice: «Con 30 g de sal será −18 °C seguro». ¿Qué le respondes? A) No es seguro: no hay datos medidos sobre 15 g; B) Sí: la tabla lo muestra.", "A", "Predecir fuera del rango es una suposición."),
      ("¿Qué mejoraría la confianza en esta tabla? A) Repetir las mediciones con la misma masa de agua; B) Cambiar los colores de la tabla.", "A", "Repetir permite descartar errores de medición."),
  ],
  cha=[
      arith("Con el mismo patrón de ejemplo (3 °C de descenso cada 5 g de sal en 100 g de agua), ¿cuántos gramos de sal se necesitarían para llegar a −12 °C?", "12//3*5", "Cada 3 °C de descenso requiere 5 g: son 4 tramos de 5 g.", " g"),
      ("En todos los vasos de la tabla, ¿qué debe quedar igual? A) La masa de agua; B) La masa de sal.", "A", "Solo debe cambiar la variable independiente."),
  ],
  context=[("Agua de mar de ejemplo, con sales disueltas, se congela a −2 °C. ¿Cómo es su temperatura de congelación comparada con la del agua pura? A) Menor; B) Mayor.", "A", "Las sales disueltas bajan el punto de congelación.")],
  selfcheck=[("¿Cuál es la variable dependiente en la tabla de congelación?", "La temperatura de congelación", "Es la que se mide."), ("¿Por qué extrapolar es solo una suposición?", "Porque no hay datos medidos fuera del rango", "Puede cambiar el patrón."), ("¿Qué patrón muestra la tabla?", "A más sal, menor temperatura de congelación", "Baja de forma pareja.")],
  open_task=task("Con esta tabla de ejemplo para el azúcar en 100 g de agua: 0 g, 0 °C; 20 g, −1 °C; 40 g, −2 °C; 60 g, −3 °C, escribe el patrón, nombra variable independiente y dependiente, predice con 80 g indicando que es una suposición y propone cómo comprobar la predicción con seguridad.", "Cada 20 g baja 1 °C. Independiente: masa de azúcar; dependiente: temperatura de congelación. Se esperaría −4 °C con 80 g, pero es una suposición. Se comprobaría con un termómetro y la ayuda de una persona adulta, repitiendo la medición.", ["describe el patrón", "nombra las variables", "predice con cautela"], ["patrón, variables y una predicción"], ["presentar la predicción como dato medido", "mezclar las variables"], "Pregunta qué se repetiría para tener más confianza."),
  reinforce="Calcula cuánto baja la temperatura si la tabla del azúcar pasa de 10 g a 30 g.",
  extend="Explica por qué una conclusión no puede ir más allá de los datos.")

L(OA16, 3,
  materials=MAT,
  use="Aprenderé a usar el modelo de partículas para explicar el ascenso y el descenso de los puntos de ebullición y de congelación, y la ósmosis, y a contrastarlo con un modelo equivocado.",
  prior=["Sé que las partículas de un líquido se mueven y que algunas escapan al aire como vapor.", "Sé qué es el descenso crioscópico."],
  explain=[
      "En un líquido, las partículas se mueven y las de la superficie pueden escapar como vapor. Cuando el soluto no se evapora, sus partículas ocupan parte de la superficie y entre las del solvente. Hay menos partículas de agua que pueden escapar, por lo que la solución necesita más temperatura para hervir. Así se explica el ascenso del punto de ebullición.",
      "Para congelarse, las partículas de agua deben ordenarse en un cristal de hielo. Las partículas de soluto se interponen y dificultan ese orden, así que hay que enfriar más. Así se explica el descenso del punto de congelación. Cuantas más partículas de soluto, mayor es el efecto, por eso la propiedad es coligativa.",
      "La ósmosis es el paso de agua a través de una membrana semipermeable, que deja pasar el agua pero no el soluto. El agua pasa del lado con menos soluto al lado con más soluto. Un modelo equivocado diría que «la sal calienta o enfría el agua». Para contrastar modelos se elige el que explica los datos de punto de congelación y de ebullición, y se nombran sus límites.",
  ],
  vocab=[("membrana semipermeable", "barrera que deja pasar el solvente pero no el soluto"), ("ósmosis", "paso de solvente a través de una membrana semipermeable"), ("presión de vapor", "presión que ejerce el vapor sobre un líquido"), ("cristal", "ordenamiento regular de partículas en un sólido"), ("modelo de partículas", "explicación basada en el movimiento de partículas")],
  worked=[
      ("Explicar la ebullición", "Explica con partículas por qué el agua con azúcar hierve a más de 100 °C.", ["Las partículas de azúcar no se evaporan y ocupan la superficie.", "Menos partículas de agua escapan como vapor, así que se necesita más temperatura."], "Hay menos partículas de agua escapando, por eso hierve a mayor temperatura"),
      ("Dirección de la ósmosis", "Una membrana semipermeable separa agua con 2 partículas de soluto de otra con 8 de ejemplo. ¿Hacia dónde pasa el agua?", ["El agua pasa del lado con menos soluto al de más soluto.", "El lado con 8 partículas tiene más soluto."], "Hacia el lado con 8 partículas de soluto"),
  ],
  mistakes=[
      ("Decir que el soluto calienta o enfría el agua.", "Lo que cambia es la temperatura a la que hierve o se congela, no la temperatura del agua.", "Explica con partículas, no con «calor» de la sal."),
      ("Creer que la membrana semipermeable deja pasar todo.", "Deja pasar el solvente y no el soluto.", "Recuerda que es selectiva."),
  ],
  rec=[
      ("¿Qué deja pasar una membrana semipermeable?", "El solvente, pero no el soluto", "Es una barrera selectiva."),
      ("Verdadero o falso: las partículas de soluto dificultan que el agua se ordene en un cristal de hielo.", "Verdadero", "Por eso hay que enfriar más."),
      ("¿Cómo se llama el paso de agua por una membrana semipermeable?", "Ósmosis", "Es el movimiento de solvente."),
  ],
  und=[
      ("¿Qué explica el ascenso del punto de ebullición? A) Menos partículas de agua escapan como vapor; B) El soluto calienta el agua.", "A", "El soluto no se evapora y ocupa la superficie."),
      ("Un soluto, ¿por qué baja el punto de congelación? A) Dificulta que las partículas de agua formen el cristal; B) Hace que el agua se evapore antes.", "A", "Hay que enfriar más para que se ordenen."),
      ("En la ósmosis, el agua pasa del lado con menos soluto al lado con ____ soluto.", "Más", "El agua se mueve hacia el lado más concentrado."),
  ],
  app=[
      ("Un dibujo de ejemplo muestra la solución P con 5 partículas de soluto y la solución Q con 12, en el mismo volumen. ¿Cuál tendrá mayor ascenso del punto de ebullición? A) La solución Q; B) La solución P.", "A", "Más partículas de soluto producen mayor efecto."),
      arith("Dos lados de una membrana de ejemplo tienen 6 y 15 partículas de soluto. ¿Cuántas partículas más tiene el lado hacia el que pasa el agua?", "15-6", "El agua pasa hacia el lado con más soluto; se resta la diferencia."),
      ("En una celda, el agua pura queda a la izquierda y una solución con sal a la derecha, separadas por una membrana semipermeable. ¿Hacia dónde pasa el agua? A) A la derecha; B) A la izquierda.", "A", "El agua va hacia el lado con más soluto."),
  ],
  rea=[
      ("Un compañero dice: «La sal enfría el agua y por eso baja el punto de congelación». ¿Qué le respondes? A) La sal no enfría; dificulta la formación del cristal de hielo; B) Tiene razón porque el hielo es frío.", "A", "El modelo de partículas explica el efecto sin invocar frío de la sal."),
      ("¿Qué límite tiene un dibujo de partículas para explicar la ebullición? A) No muestra la temperatura ni la velocidad de las partículas; B) Muestra todo con exactitud.", "A", "Un modelo simplifica y deja fuera información."),
  ],
  cha=[
      ("Se comparan dos soluciones con el mismo número de partículas de soluto en el mismo volumen, pero con solutos distintos. ¿Qué se espera del descenso del punto de congelación? A) Similar en ambas; B) Muy distinto.", "A", "Una propiedad coligativa depende del número de partículas."),
      ("Un modelo dice que el soluto solo cambia el color del agua. ¿Qué dato lo contradice? A) La temperatura de congelación cambia con la masa de soluto; B) El soluto es un sólido.", "A", "El modelo no explica los datos de congelación."),
  ],
  context=[("Un cocinero de ejemplo nota que el agua con mucha sal tarda más en hervir que el agua sola en la misma olla. ¿Qué explicación apoya el modelo de partículas? A) Menos partículas de agua escapan y se necesita más temperatura; B) La sal enfría la olla.", "A", "El soluto eleva el punto de ebullición.")],
  selfcheck=[("¿Por qué sube el punto de ebullición con un soluto?", "Porque menos partículas de agua escapan como vapor", "El soluto ocupa la superficie."), ("¿Hacia dónde pasa el agua en la ósmosis?", "Hacia el lado con más soluto", "Pasa a través de la membrana."), ("Nombra un límite de un modelo de partículas dibujado.", "No muestra la velocidad ni el tamaño real", "Es una simplificación.")],
  open_task=task("Dibuja dos recuadros de agua: uno con 4 partículas de soluto y otro con 10, ambos con 30 de agua. Rotula cuál tiene mayor ascenso del punto de ebullición y escribe en una oración por qué. Añade un límite de tu dibujo.", "El recuadro con 10 partículas de soluto: tiene menos agua escapando como vapor, por eso necesita más temperatura para hervir. Límite: el dibujo no muestra el movimiento.", ["dibuja la diferencia de partículas", "elige el recuadro correcto", "explica con partículas", "declara un límite"], ["dos dibujos y una explicación"], ["decir que el soluto calienta el agua", "no explicar con partículas"], "Pregunta qué cambiaría si el soluto fuera 20 partículas."),
  reinforce="Explica con partículas por qué el agua con sal hierve a más de 100 °C.",
  extend="Describe hacia dónde se mueve el agua en una ósmosis y por qué.")

L(OA16, 4,
  materials=MAT,
  use="Aprenderé a planificar una investigación sobre propiedades coligativas, a controlar variables y a comparar el efecto de distintos solutos según la cantidad de partículas.",
  prior=["Sé qué son las variables independiente, dependiente y controlada.", "Sé que el efecto coligativo depende del número de partículas."],
  explain=[
      "Planificar una investigación significa decidir qué se cambia, qué se mide y qué se mantiene igual. Para estudiar el descenso del punto de congelación, se cambia la masa de soluto, se mide la temperatura de congelación y se controlan la masa de agua, el termómetro y el tiempo de espera. También se decide cuántas veces se repite cada medición.",
      "Una relación entre variables dice cómo una afecta a la otra. Aquí, a mayor número de partículas de soluto disueltas, mayor efecto coligativo. Hay solutos que se separan en más partículas al disolverse. En el modelo de este cuaderno, cada unidad de sal da 2 partículas y cada unidad de azúcar da 1 partícula. Para comparar el efecto hay que contar partículas, no solo gramos.",
      "La seguridad es parte del plan. Las mediciones con calor o con frío intenso las hace una persona adulta, o se trabaja con datos de ejemplo. Nunca se prueban soluciones ni se usan productos de limpieza o del auto como soluto. Un plan bien hecho se escribe de modo que otra persona pueda repetirlo.",
  ],
  vocab=[("variable controlada", "la que se mantiene igual en todo el experimento"), ("replicar", "repetir el experimento para comprobar"), ("número de partículas", "cantidad de partículas de soluto disueltas"), ("plan", "descripción de pasos, variables y seguridad"), ("comparar", "poner dos resultados lado a lado")],
  worked=[
      ("Variables del plan", "Plan de ejemplo: medir la temperatura de congelación del agua con 5, 10 y 15 g de sal en 100 g de agua. Nombra las tres clases de variables.", ["Se cambia la masa de sal: independiente.", "Se mide la temperatura de congelación: dependiente.", "Se mantienen la masa de agua y el termómetro: controladas."], "Independiente: masa de sal; dependiente: temperatura de congelación; controladas: masa de agua y termómetro"),
      ("Contar partículas", "En el modelo, cada unidad de sal da 2 partículas y cada unidad de azúcar da 1. ¿Qué tiene más partículas: 8 unidades de sal o 12 de azúcar?", ["Sal: 8 × 2 = 16 partículas.", "Azúcar: 12 × 1 = 12 partículas."], "8 unidades de sal tienen más partículas"),
  ],
  mistakes=[
      ("Cambiar dos variables a la vez.", "Si cambian la masa de soluto y la masa de agua, no se sabe cuál causó el efecto.", "Cambia una sola variable por experimento."),
      ("Comparar solutos solo por los gramos.", "El efecto depende de las partículas que se forman.", "Cuenta partículas con el modelo dado."),
  ],
  rec=[
      ("¿Cómo se llama la variable que se mantiene igual en todo el experimento?", "Variable controlada", "Evita que otros factores influyan."),
      ("Verdadero o falso: se debe cambiar una sola variable por vez.", "Verdadero", "Así se sabe qué causó el efecto."),
      ("¿De qué depende el efecto coligativo?", "Del número de partículas de soluto", "No depende de cuál es el soluto."),
  ],
  und=[
      ("¿Cuál es la variable dependiente al medir la temperatura de ebullición con distintas masas de azúcar? A) La temperatura de ebullición; B) La masa de azúcar.", "A", "Es lo que se mide como resultado."),
      ("En el modelo, ¿cuántas partículas dan 9 unidades de sal? A) 18; B) 9.", "A", "Cada unidad de sal da 2 partículas."),
      ("¿Cuál es un riesgo de este tipo de investigación que exige a una persona adulta? A) Trabajar con agua caliente o frío intenso; B) Escribir los datos.", "A", "El calor y el frío intenso pueden causar daños."),
  ],
  app=[
      arith("Una solución de ejemplo tiene 25 unidades de azúcar y otra tiene 10 unidades de sal. ¿Cuántas partículas tiene la de sal?", "10*2", "Cada unidad de sal da 2 partículas.", " partículas"),
      arith("En el modelo, 14 unidades de azúcar y 9 unidades de sal están en el mismo volumen de agua. ¿Cuántas partículas más tiene la de sal?", "9*2-14", "Sal: 9 × 2 = 18; azúcar: 14 × 1 = 14; se resta."),
      ("Se quiere comparar el efecto de la sal y del azúcar. ¿Qué debe ser igual? A) La masa de agua y la masa de soluto agregada; B) El tipo de soluto.", "A", "Si el tipo de soluto es la variable que se cambia, lo demás se mantiene igual."),
  ],
  rea=[
      ("Un plan cambia la masa de sal y la masa de agua al mismo tiempo. ¿Qué problema tiene? A) No se sabe cuál causó el cambio; B) Gasta demasiada sal.", "A", "Hay dos variables cambiando a la vez."),
      ("Un compañero dice: «10 g de sal y 10 g de azúcar bajan igual la temperatura de congelación». ¿Qué falta considerar? A) El número de partículas que se forman; B) El color de cada soluto.", "A", "Los gramos iguales no significan partículas iguales."),
  ],
  cha=[
      arith("Con el modelo dado, ¿cuántas unidades de azúcar harían falta para igualar las partículas de 20 unidades de sal?", "20*2", "La sal da el doble de partículas por unidad.", " unidades"),
      ("Un plan mide una sola vez la temperatura de congelación en cada vaso. ¿Qué mejora es mejor? A) Repetir cada medición y registrar todos los datos; B) Medir una vez y no anotar.", "A", "Repetir permite detectar errores."),
  ],
  context=[("Una persona de ejemplo quiere saber si el agua con más azúcar tarda más en hervir. ¿Quién debe encargarse del agua caliente? A) Una persona adulta; B) Cualquier persona que sepa medir.", "A", "El agua en ebullición puede causar quemaduras.")],
  selfcheck=[("¿Qué variable se cambia a propósito?", "La independiente", "Es la que se manipula."), ("¿Por qué se cuentan partículas y no solo gramos?", "Porque el efecto depende del número de partículas", "Solutos distintos forman distinto número."), ("¿Quién hace las mediciones con calor?", "Una persona adulta", "Así se evitan las quemaduras.")],
  open_task=task("Escribe un plan para investigar con datos de ejemplo si el azúcar sube la temperatura de ebullición del agua. Incluye pregunta, variable independiente, dependiente, dos variables controladas, cuántas repeticiones y una norma de seguridad.", "Pregunta: ¿sube la temperatura de ebullición al aumentar la masa de azúcar en 100 g de agua? Independiente: masa de azúcar; dependiente: temperatura de ebullición; controladas: masa de agua y termómetro; tres repeticiones; el agua caliente la maneja una persona adulta.", ["pregunta investigable", "variables bien clasificadas", "una norma de seguridad"], ["un plan de media página"], ["cambiar dos variables a la vez", "olvidar la seguridad"], "Pregunta cómo se reduciría el error de medición."),
  reinforce="Cuenta las partículas de 6 unidades de sal y de 9 unidades de azúcar y di cuál tiene más.",
  extend="Explica por qué un buen plan cambia una sola variable por vez.")

L(OA16, 5,
  materials=MAT,
  use="Aprenderé a explicar con evidencia cómo las propiedades coligativas se usan en conservas y mermeladas y en el agua de los radiadores, y a reconocer sus precauciones.",
  prior=["Sé que un soluto cambia los puntos de congelación y de ebullición.", "Sé qué es la ósmosis."],
  explain=[
      "Las mermeladas y las frutas en conserva guardan mucha azúcar disuelta. Por ósmosis, el agua sale de los microorganismos hacia el medio con más soluto, y esos microorganismos no pueden multiplicarse bien. Por eso una alta concentración de azúcar o de sal ayuda a conservar los alimentos. Aun así, una conserva casera exige higiene y recipientes limpios; si la tapa está abombada, huele raro o tiene moho, no se come y se avisa a una persona adulta.",
      "En el radiador de un auto circula agua con un aditivo anticongelante. El aditivo disuelto baja la temperatura de congelación del líquido y sube su temperatura de ebullición. Así el líquido no se congela en el frío ni hierve con facilidad con el motor caliente. Ambos efectos son propiedades coligativas.",
      "Los aditivos de los radiadores son tóxicos: no se tocan, no se prueban y los cambia una persona especialista en un taller. Una conclusión con evidencia debe decir qué dato la apoya y qué límite tiene. Por ejemplo, los datos de ejemplo de este cuaderno muestran el patrón, pero no reemplazan las instrucciones del fabricante del aditivo.",
  ],
  vocab=[("conserva", "alimento tratado para que dure más tiempo"), ("microorganismo", "ser vivo muy pequeño, como una bacteria o un moho"), ("anticongelante", "aditivo que baja el punto de congelación de un líquido"), ("aditivo", "sustancia que se agrega para dar una propiedad"), ("toxicidad", "capacidad de una sustancia de dañar la salud")],
  worked=[
      ("Mermelada", "Explica por qué una mermelada con mucha azúcar dura más que la fruta sola.", ["La alta concentración de azúcar atrae el agua de los microorganismos por ósmosis.", "Sin agua, los microorganismos no se multiplican bien."], "El azúcar disuelta quita agua a los microorganismos y limita su crecimiento"),
      ("Radiador", "Una mezcla de ejemplo se congela a −20 °C y el agua sola a 0 °C. ¿Qué ventaja tiene la mezcla en un día de helada?", ["La mezcla se congela a menor temperatura.", "Así no se congela con heladas moderadas."], "Es líquida a temperaturas donde el agua sola ya se congelaría"),
  ],
  mistakes=[
      ("Decir que el azúcar mata los microorganismos.", "Les quita agua y limita su crecimiento; no garantiza que sean eliminados.", "Habla de ósmosis y de crecimiento limitado."),
      ("Pensar que cualquier líquido de auto es seguro de manipular.", "Los aditivos del radiador son tóxicos.", "Avisa a una persona adulta y no los toques."),
  ],
  rec=[
      ("¿Qué fenómeno explica que el agua salga de un microorganismo en un medio muy azucarado?", "La ósmosis", "El agua pasa hacia el lado con más soluto."),
      ("Verdadero o falso: el aditivo del radiador baja el punto de congelación del líquido.", "Verdadero", "Es un descenso crioscópico."),
      ("¿Qué se hace con una conserva de tapa abombada?", "No se come y se avisa a una persona adulta", "Puede estar echada a perder."),
  ],
  und=[
      ("¿Por qué una mermelada se conserva más tiempo? A) Hay mucha azúcar que limita el crecimiento de microorganismos; B) La mermelada no tiene agua.", "A", "El azúcar alto quita agua a los microorganismos."),
      ("¿Qué dos propiedades coligativas ayudan en un radiador? A) Descenso del punto de congelación y ascenso del punto de ebullición; B) Cambio de color y de olor.", "A", "Protege del frío y del calor."),
      ("¿Quién cambia el aditivo de un radiador? A) Una persona especialista; B) Cualquier estudiante.", "A", "Los aditivos son tóxicos y exigen cuidado."),
  ],
  app=[
      arith("Una mezcla de ejemplo contiene 600 g de fruta y 400 g de azúcar. ¿Qué porcentaje de la masa total es azúcar?", "400*100//1000", "La masa total es 600 + 400 = 1.000 g; se divide el azúcar por el total y se multiplica por 100.", " %"),
      ("El líquido A de un radiador de ejemplo se congela a −10 °C y el líquido B a −25 °C. ¿Cuál protege mejor en una helada muy fuerte? A) El líquido B; B) El líquido A.", "A", "Se congela a menor temperatura."),
      ("Un jugo de ejemplo tiene poca azúcar y una mermelada tiene mucha. ¿Cuál limita más el crecimiento de microorganismos? A) La mermelada; B) El jugo.", "A", "A mayor soluto, más efecto osmótico."),
  ],
  rea=[
      ("Una persona dice: «Como la mermelada tiene mucha azúcar, un frasco abierto nunca se echa a perder». ¿Qué le respondes? A) La azúcar ayuda, pero el frasco abierto debe guardarse como indica su etiqueta; B) Tiene razón.", "A", "La concentración no elimina todos los riesgos."),
      ("¿Qué límite tienen los datos de ejemplo del cuaderno sobre radiadores? A) No reemplazan las instrucciones del fabricante; B) No tienen temperaturas.", "A", "Un caso de ejemplo no sirve para decidir en un vehículo real."),
  ],
  cha=[
      arith("Una mezcla de ejemplo de 800 g tiene 560 g de azúcar. ¿Qué porcentaje de la mezcla es azúcar?", "560*100//800", "Se divide el azúcar por la masa total y se multiplica por 100.", " %"),
      ("Un radiador de ejemplo hirvió con el motor caliente. ¿Qué puede haber fallado? A) Faltó aditivo que sube el punto de ebullición; B) Sobró aditivo que baja el punto de congelación.", "A", "Sin aditivo suficiente, el líquido hierve antes."),
  ],
  context=[("En una conserva de ejemplo, una persona adulta nota que el frasco está abombado. ¿Qué evidencia debe apoyar su decisión? A) Que la tapa abombada es señal de posible daño y no se debe comer; B) Que la fruta tiene mucho azúcar.", "A", "La tapa abombada es una señal observable de riesgo.")],
  selfcheck=[("¿Por qué el azúcar ayuda a conservar mermelada?", "Porque por ósmosis quita agua a los microorganismos", "Limita su crecimiento."), ("¿Qué hace el aditivo del radiador con el punto de ebullición?", "Lo sube", "Es el ascenso ebulloscópico."), ("¿Qué se hace con una conserva sospechosa?", "No se come y se avisa a una persona adulta", "Evita riesgos para la salud.")],
  open_task=task("Con estos datos de ejemplo: agua sola, se congela a 0 °C y hierve a 100 °C; mezcla con aditivo, se congela a −25 °C y hierve a 106 °C. Escribe una conclusión sobre su uso en un radiador y su evidencia, y un límite de estos datos. Añade una precaución de seguridad.", "La mezcla protege mejor porque se congela a menor temperatura y hierve a mayor: su intervalo líquido va de −25 °C a 106 °C. Límite: son datos de ejemplo y no reemplazan las instrucciones del fabricante. El aditivo es tóxico y lo cambia un especialista.", ["compara las dos temperaturas", "cita la evidencia", "declara un límite", "incluye una precaución"], ["una conclusión de cuatro oraciones"], ["afirmar que los datos de ejemplo son reales", "olvidar la toxicidad"], "Pregunta qué dato extra necesitaría un taller."),
  reinforce="Explica con ósmosis por qué la fruta con mucha azúcar se conserva más tiempo.",
  extend="Describe dos ventajas de un aditivo anticongelante en el radiador de un auto.")

"""Ciencias Naturales EPJA Media N1, módulo 2, desempeño OAD-06: organizar y presentar información sobre propiedades de compuestos orgánicos de uso cotidiano (química orgánica, grupos funcionales, carbono). Todo en papel; datos de ejemplo."""
from __future__ import annotations

from epja_cnat_nm1_b_common import K

O = "EPJA-CNAT-NM1-OAD-06"

# ====================================================== clase 1
F = ("Ficha 1 (materiales de una cocina y de un taller, de ejemplo; se indican los elementos que forman cada sustancia). M1: azúcar de mesa; carbono, hidrógeno y oxígeno. "
     "M2: sal de mesa; sodio y cloro. M3: gas licuado; propano y butano, formados por carbono e hidrógeno. M4: aceite de cocina; carbono, hidrógeno y oxígeno. "
     "M5: agua; hidrógeno y oxígeno. M6: bolsa plástica de polietileno; carbono e hidrógeno. M7: arena de vidrio; silicio y oxígeno. "
     "M8: alcohol de uso doméstico, etanol; carbono, hidrógeno y oxígeno.")
K(O, 1, F,
  "Hoy partiré de los materiales que uso en mi casa o trabajo para reconocer cuáles son compuestos orgánicos y cómo ordenar esa información en una tabla.",
  ["Tú usas todos los días sustancias del carbono: el azúcar, el aceite, el gas de la cocina, el plástico de las bolsas. A las sustancias formadas por carbono unido sobre todo a hidrógeno, y a veces a oxígeno u otros átomos, se les llama compuestos orgánicos. La química orgánica es la parte de la química que los estudia.",
   "El carbono es muy especial porque puede unirse a otros átomos de carbono y formar cadenas largas. Por eso existen millones de compuestos orgánicos. Por convención, algunas sustancias con carbono, como el dióxido de carbono, se clasifican como inorgánicas y no entran en esta definición simple.",
   "Para no perder información conviene organizarla en una tabla: una fila por material y columnas con título, por ejemplo material, elementos, si es orgánico y para qué se usa. Una tabla bien hecha permite comparar de un vistazo y compartirla con otra persona. Aquí trabajamos solo con los datos escritos en la ficha."],
  [("compuesto orgánico", "compuesto del carbono, unido sobre todo a hidrógeno"), ("compuesto inorgánico", "compuesto que no tiene la base carbono-hidrógeno de los orgánicos"), ("elemento", "tipo de átomo, como carbono, oxígeno o sodio"), ("tabla", "forma de organizar datos en filas y columnas con títulos")],
  [("Clasificar un material", "{F} ¿M3, el gas licuado, es orgánico o inorgánico?",
    ["Veo de qué elementos está formado.", "Tiene carbono e hidrógeno."], "Es orgánico, porque está formado por carbono e hidrógeno"),
   ("Armar una fila de la tabla", "{F} Escribe la fila de M2: material, elementos y si es orgánico.",
    ["El material es la sal de mesa.", "Tiene sodio y cloro, sin carbono."], "Sal de mesa | sodio y cloro | no es orgánico")],
  [("Pensar que todo lo que viene de una planta o un animal es orgánico y todo lo demás no.", "En química, orgánico habla de la composición con carbono, no del origen.", "Mira los elementos: carbono unido a hidrógeno indica un compuesto orgánico."),
   ("Armar una tabla sin títulos en las columnas.", "Sin títulos no se sabe qué significa cada dato.", "Pon un título a cada columna y la unidad si hay números.")],
  [("abc", "¿Qué elemento está presente en todos los compuestos orgánicos?", "el carbono", "el sodio", "el silicio", "La química orgánica es la química de los compuestos del carbono."),
   ("abc", "{F} ¿Cuál de estos materiales es un compuesto orgánico?", "M4, el aceite de cocina", "M2, la sal de mesa", "M5, el agua", "El aceite tiene carbono unido a hidrógeno y oxígeno."),
   ("abc", "{F} ¿Por qué M2, la sal de mesa, no es orgánica?", "No contiene carbono: tiene sodio y cloro", "Porque es blanca", "Porque se disuelve en agua", "Sin carbono no puede ser un compuesto orgánico."),
   ("=", "{F} De los 8 materiales de la ficha, 5 son orgánicos (M1, M3, M4, M6 y M8). ¿Cuántos no lo son?", "8-5", "Se restan los orgánicos del total: son M2, M5 y M7.", " materiales"),
   ("abc", "{F} ¿Qué elementos forman el polietileno de M6?", "carbono e hidrógeno", "sodio y cloro", "silicio y oxígeno", "La ficha indica carbono e hidrógeno para M6."),
   ("abc", "Se quiere comparar los materiales en una tabla. ¿Qué columnas sirven para ello?", "material, elementos, si es orgánico y uso", "solo el nombre del material", "el precio y el color de la etiqueta", "Esas columnas permiten clasificar y comparar con los datos de la ficha."),
   ("abc", "{F} Una persona dice: «el alcohol M8 es inorgánico porque es un líquido como el agua». ¿Qué respondes?", "Es orgánico: tiene carbono unido a hidrógeno; el estado no decide", "Tiene razón, es inorgánico", "Es inorgánico porque tiene oxígeno", "Lo que clasifica es la composición, no que sea líquido."),
   ("abc", "{F} ¿Qué dos materiales de la ficha están formados solo por carbono e hidrógeno?", "M3 y M6", "M1 y M4", "M2 y M5", "El gas licuado y el polietileno solo tienen carbono e hidrógeno."),
   ("abc", "{F} En la tabla, ¿dónde se anota M7, la arena de vidrio?", "como inorgánico, porque no tiene carbono", "como orgánico, porque tiene oxígeno", "no se anota", "M7 tiene silicio y oxígeno, sin carbono."),
   ("abc", "Se quiere presentar la clasificación a una vecina. ¿Cuál presentación es más clara?", "una tabla con títulos de columna", "un párrafo largo sin orden", "una lista sin títulos", "Una tabla titulada deja comparar de un vistazo."),
   ("abc", "{F} Si se agrega M9, el dióxido de carbono (carbono y oxígeno), la regla de la clase dice que el dióxido de carbono se trata como inorgánico. ¿Cómo se anota?", "como inorgánico, según esa regla", "como orgánico, porque tiene carbono", "no se puede anotar", "Aunque tiene carbono, la convención lo clasifica aparte."),
   ("=", "{F} Si 5 de los 8 materiales son orgánicos, ¿qué porcentaje de los materiales son orgánicos?", "5/8*100", "Se divide 5 entre 8 y se multiplica por 100.", " %"),
   ("abc", "Un puesto de feria de ejemplo ofrece «verduras orgánicas». ¿Cuál es el sentido de «orgánico» en la química?", "Que el compuesto tiene base de carbono e hidrógeno", "Que no contiene ningún átomo de carbono", "Que es de origen vegetal únicamente", "En química orgánico se refiere a la composición, no al cultivo.")],
  ("abc", "Un taller de ejemplo guarda aceite, alcohol, agua y sal. ¿Cuántos de estos cuatro materiales son orgánicos?", "2: el aceite y el alcohol", "4: todos", "1: solo el alcohol", "El aceite y el alcohol tienen carbono unido a hidrógeno; el agua y la sal no."),
  [("En Ciencias Naturales: ¿qué es un compuesto orgánico?", "Un compuesto del carbono unido sobre todo a hidrógeno", "Tiene base de carbono e hidrógeno."),
   ("¿Qué elemento tiene la sal de mesa en lugar de carbono?", "Sodio y cloro", "La sal es un compuesto inorgánico."),
   ("¿Para qué sirven los títulos de las columnas de una tabla?", "Para saber qué significa cada dato", "Sin títulos los datos se confunden.")],
  ("Elige cuatro materiales de tu casa o de la ficha. Arma una tabla con las columnas material, elementos que lo forman, si es orgánico y uso. Escribe una frase que diga qué aprendiste al compararlos.",
   "Material | elementos | orgánico | uso: aceite | C, H, O | sí | cocinar; sal | sodio y cloro | no | condimentar; agua | H y O | no | beber; gas licuado | C y H | sí | cocinar. Aprendí que no todo lo que uso diario es orgánico.",
   ["arma una tabla con títulos de columna", "clasifica bien los cuatro materiales", "escribe una frase de conclusión"],
   ["La tabla tiene filas y columnas claras.", "Usa el criterio del carbono.", "La frase se apoya en la tabla."],
   "Si clasifica por el estado, pregunta «¿qué elementos lo forman?»."),
  "Agrega tres materiales a tu tabla y clasifícalos.",
  "Explica con tus palabras por qué el dióxido de carbono se clasifica aparte.")

# ====================================================== clase 2
F = ("Ficha 2 (carbono y grupos funcionales, de ejemplo). Regla: cada átomo de carbono forma 4 enlaces. Un hidrocarburo solo tiene carbono e hidrógeno, como el metano CH4. "
     "Un grupo funcional es un grupo de átomos que da propiedades características. Alcohol: grupo –OH unido a un carbono; ejemplo, el etanol CH3CH2OH. "
     "Éter: un oxígeno entre dos carbonos, C–O–C; ejemplo, CH3OCH3. Haluro: un átomo de cloro, bromo, flúor o yodo unido a un carbono; ejemplo, CH3Cl. "
     "Ácido carboxílico: grupo –COOH; ejemplo, el ácido acético CH3COOH, que da el sabor ácido al vinagre. "
     "Compuestos para clasificar: Q1, CH3CH2CH2OH; Q2, CH3CH2Cl; Q3, CH3CH2OCH3; Q4, CH3CH2COOH; Q5, C2H6.")
K(O, 2, F,
  "Hoy reconoceré las propiedades del carbono y los principales grupos funcionales: alcoholes, éteres, haluros y ácidos carboxílicos.",
  ["Un átomo de carbono forma siempre cuatro enlaces. Puede unirse a hidrógenos, a otros carbonos y a átomos como oxígeno o cloro. Esa capacidad de formar cadenas y de unirse a muchos átomos explica la enorme cantidad de compuestos orgánicos. El más simple es el metano, CH4: un carbono con cuatro hidrógenos.",
   "Los hidrocarburos tienen solo carbono e hidrógeno. Si en una molécula aparece un grupo de átomos particular, ese grupo funcional le da sus propiedades. El grupo –OH forma los alcoholes; un oxígeno entre dos carbonos forma un éter; un cloro, bromo, flúor o yodo unido a un carbono forma un haluro; y el grupo –COOH forma un ácido carboxílico.",
   "Para clasificar un compuesto, se busca el grupo funcional en su fórmula. Dos compuestos pueden tener los mismos átomos y propiedades distintas si el grupo funcional es distinto: el etanol, un alcohol, y el CH3OCH3, un éter, tienen la misma fórmula C2H6O. Aquí no se hacen mezclas: solo se leen fórmulas."],
  [("grupo funcional", "grupo de átomos que da propiedades características al compuesto"), ("hidrocarburo", "compuesto formado solo por carbono e hidrógeno"), ("alcohol", "compuesto con el grupo –OH unido a un carbono"), ("haluro", "compuesto con cloro, bromo, flúor o yodo unido a un carbono")],
  [("Reconocer el grupo", "{F} ¿Q1, CH3CH2CH2OH, a qué familia pertenece?",
    ["Busco un grupo funcional en la fórmula.", "Termina en –OH: es un alcohol."], "Es un alcohol"),
   ("Contar enlaces del carbono", "{F} En CH3Cl, ¿cuántos enlaces forma el carbono?",
    ["Tiene 3 hidrógenos y 1 cloro unidos.", "Se suman 3 + 1."], "4 enlaces")],
  [("Pensar que el carbono puede formar cualquier número de enlaces.", "El carbono forma siempre cuatro enlaces.", "Cuenta los átomos unidos a cada carbono: deben sumar cuatro."),
   ("Creer que dos compuestos con la misma fórmula tienen las mismas propiedades.", "El grupo funcional distinto cambia las propiedades.", "Compara siempre los grupos funcionales, no solo el número de átomos.")],
  [("abc", "¿Cuántos enlaces forma cada átomo de carbono?", "4", "2", "6", "Cada átomo de carbono forma cuatro enlaces con otros átomos."),
   ("abc", "{F} ¿Qué grupo funcional tiene Q1, CH3CH2CH2OH?", "–OH, de alcohol", "–COOH, de ácido", "C–O–C, de éter", "Termina en –OH, característico de los alcoholes."),
   ("abc", "{F} ¿Q2, CH3CH2Cl, es un haluro?", "Sí, porque tiene un cloro unido a un carbono", "No, porque tiene hidrógeno", "No, porque es un alcohol", "El cloro unido a carbono define un haluro."),
   ("abc", "{F} ¿Q3, CH3CH2OCH3, qué es?", "un éter, porque el oxígeno está entre dos carbonos", "un alcohol, porque tiene oxígeno", "un haluro, porque tiene oxígeno", "El oxígeno entre carbonos forma la unión C–O–C."),
   ("abc", "{F} ¿Q4, CH3CH2COOH, qué grupo tiene?", "–COOH, de ácido carboxílico", "–OH, de alcohol", "un cloro, de haluro", "Termina en –COOH, propio del ácido carboxílico."),
   ("abc", "{F} ¿Por qué Q5, C2H6, es un hidrocarburo?", "Solo tiene carbono e hidrógeno", "Tiene oxígeno", "Tiene cloro", "Un hidrocarburo se forma solo con carbono e hidrógeno."),
   ("=", "{F} En CH3Cl, ¿cuántos átomos hay en total? (1 carbono, 3 hidrógenos y 1 cloro)", "1+3+1", "Se suman todos los átomos de la fórmula.", " átomos"),
   ("=", "{F} El etanol CH3CH2OH tiene 2 carbonos, 6 hidrógenos y 1 oxígeno. ¿Cuántos átomos tiene en total?", "2+6+1", "Se suman los átomos de cada elemento.", " átomos"),
   ("abc", "{F} ¿Qué compuesto de la ficha da el sabor ácido al vinagre?", "el ácido acético, CH3COOH", "el metano, CH4", "el CH3Cl", "La ficha lo indica: el ácido acético da el sabor ácido."),
   ("abc", "En un carbono hay 2 hidrógenos y 2 átomos de cloro unidos. ¿Cuántos enlaces forma?", "4", "2", "5", "Dos H más dos Cl suman cuatro enlaces."),
   ("abc", "{F} El etanol y CH3OCH3 tienen la misma fórmula C2H6O. ¿Por qué pueden tener propiedades distintas?", "Porque tienen grupos funcionales distintos", "Porque tienen distinto número de carbonos", "No pueden ser distintas", "Alcohol y éter se distinguen por el grupo funcional."),
   ("abc", "Una persona afirma: «un carbono con 5 enlaces es posible». ¿Qué respondes?", "No: el carbono forma cuatro enlaces", "Sí, si hay oxígeno", "Sí, siempre", "La regla del carbono es cuatro enlaces."),
   ("abc", "{F} ¿Qué diferencia hay entre un hidrocarburo y un alcohol?", "El alcohol tiene además un grupo –OH", "El hidrocarburo tiene oxígeno", "No hay diferencia", "El grupo –OH distingue al alcohol del hidrocarburo.")],
  ("abc", "En una etiqueta de ejemplo de un producto se lee «contiene alcohol etílico, CH3CH2OH». ¿A qué familia de compuestos pertenece?", "los alcoholes, por el grupo –OH", "los éteres, por el oxígeno", "los haluros, por el hidrógeno", "El grupo –OH es el característico de los alcoholes."),
  [("En Ciencias Naturales: ¿qué es un grupo funcional?", "Un grupo de átomos que da propiedades características", "Se usa para clasificar compuestos orgánicos."),
   ("¿Cuántos enlaces forma el carbono?", "4", "Es una regla básica del carbono."),
   ("¿Qué grupo caracteriza a un alcohol?", "–OH", "El oxígeno con hidrógeno unido a un carbono.")],
  ("Con las fórmulas Q1 a Q5 de la ficha, arma una tabla con tres columnas: fórmula, grupo funcional y familia. Para Q2, cuenta además los enlaces de cada carbono y comprueba que sumen cuatro.",
   "Q1 | –OH | alcohol; Q2 | cloro | haluro; Q3 | C–O–C | éter; Q4 | –COOH | ácido carboxílico; Q5 | ninguno | hidrocarburo. En Q2, el primer carbono tiene 3 H y 1 carbono: 4 enlaces.",
   ["identifica el grupo de cada fórmula", "arma la tabla con tres columnas", "comprueba los cuatro enlaces del carbono"],
   ["Clasifica correctamente las cinco fórmulas.", "La tabla tiene títulos.", "Cuenta bien los enlaces."],
   "Si confunde éter y alcohol, pregunta «¿dónde está el oxígeno?»."),
  "Describe con palabras una molécula de metano indicando sus cuatro enlaces.",
  "Explica por qué el etanol y el CH3OCH3 no son el mismo compuesto aunque tengan los mismos átomos.")

# ====================================================== clase 3
F = ("Ficha 3 (propiedades de ejemplo; valores aproximados a presión normal). Puntos de ebullición en °C: metano −162; etano −89; propano −42; butano −1; pentano 36; hexano 69; etanol 78; agua 100. "
     "Regla simplificada para esta clase: a 20 °C una sustancia de la lista es gas si su punto de ebullición es menor que 20 °C, y líquida si es mayor. "
     "Mezcla con agua: etanol, sí se mezcla; ácido acético del vinagre, sí se mezcla; aceite de cocina, no se mezcla y flota. "
     "Metano, etano, propano, butano, pentano y hexano son hidrocarburos de cadena con 1, 2, 3, 4, 5 y 6 carbonos.")
K(O, 3, F,
  "Hoy ordenaré en una tabla las propiedades de compuestos orgánicos de uso diario y reconoceré cómo cambian con el tamaño de la molécula y con el grupo funcional.",
  ["Las propiedades de los compuestos orgánicos se pueden medir y comparar. Dos propiedades fáciles de leer en una tabla son el punto de ebullición, la temperatura a la que el líquido hierve, y si se mezcla o no con el agua. Con ellas se decide, por ejemplo, si una sustancia es gas o líquido a la temperatura de la cocina.",
   "En los hidrocarburos de cadena hay una regularidad: a más átomos de carbono, mayor punto de ebullición. Por eso el metano y el butano, con pocos carbonos, son gases en una cocina, y el hexano, con seis, es un líquido. Esa regularidad se ve bien cuando se ordena la tabla de menor a mayor.",
   "El grupo funcional también cambia las propiedades. El etanol, con su grupo –OH, se mezcla con agua; el aceite no. Al organizar datos se ordena, se titula la tabla, se anotan las unidades y se indica de dónde vienen los números. Aquí todos los datos son aproximados y están en la ficha."],
  [("punto de ebullición", "temperatura a la que un líquido hierve"), ("propiedad", "característica que se puede observar o medir"), ("se mezcla", "forma una sola fase con el agua, sin separarse"), ("cadena de carbonos", "carbonos unidos uno tras otro")],
  [("Ordenar una tabla", "{F} Ordena de menor a mayor punto de ebullición: butano, metano, propano.",
    ["Comparo −1, −162 y −42.", "El más bajo es −162."], "Metano, propano, butano"),
   ("Calcular una diferencia", "{F} ¿Cuántos °C más alto es el punto de ebullición del hexano (69) que el del pentano (36)?",
    ["Se restan 69 − 36.", "69 menos 36 es 33."], "33 °C")],
  [("Ordenar los números negativos como si fueran positivos.", "−162 es menor que −42, aunque 162 sea mayor que 42.", "Ubica los números en una recta: más a la izquierda es menor."),
   ("Creer que todo líquido se mezcla con agua.", "El aceite no se mezcla con agua y flota.", "Revisa la propiedad en la tabla para cada sustancia.")],
  [("abc", "{F} ¿Cuál de estos tiene el punto de ebullición más bajo?", "metano, −162 °C", "etanol, 78 °C", "agua, 100 °C", "−162 es el menor de los valores de la ficha."),
   ("abc", "{F} ¿Cuál es líquida a 20 °C, según la regla simplificada?", "el hexano", "el propano", "el metano", "El hexano hierve a 69 °C, sobre 20 °C."),
   ("abc", "{F} ¿El butano es gas o líquido a 20 °C?", "gas, porque hierve a −1 °C", "líquido, porque tiene 4 carbonos", "sólido, porque es compuesto", "−1 °C es menor que 20 °C, así que es gas."),
   ("=", "{F} ¿Cuántos °C más sube el punto de ebullición del pentano (36) al del hexano (69)?", "69-36", "Se restan los puntos de ebullición.", " °C"),
   ("=", "{F} ¿Cuántos °C hay de diferencia entre el propano (−42) y el butano (−1)?", "-1-(-42)", "Al restar un número negativo se suma su valor.", " °C"),
   ("abc", "{F} ¿Qué tendencia muestran metano, etano, propano y butano?", "A más carbonos, mayor punto de ebullición", "A más carbonos, menor punto de ebullición", "No hay tendencia", "−162, −89, −42 y −1 van aumentando con cada carbono."),
   ("abc", "{F} ¿Qué diferencia de propiedad hay entre el etanol y el aceite de cocina?", "El etanol se mezcla con agua y el aceite no", "El aceite se mezcla con agua", "Ambos se mezclan con agua", "La ficha indica que el aceite flota sin mezclarse."),
   ("abc", "{F} Al ordenar de menor a mayor punto de ebullición, ¿cuál es el orden correcto de etanol, agua y pentano?", "pentano, etanol, agua", "agua, etanol, pentano", "etanol, pentano, agua", "36, 78 y 100 van de menor a mayor."),
   ("abc", "{F} Una persona dice: «el hexano hierve a menos temperatura que el propano, porque 69 es menor que −42». ¿Qué falla?", "69 es mayor que −42, así que el hexano hierve a más temperatura", "Nada, está bien", "Los dos hierven a la misma temperatura", "El hexano tiene mayor punto de ebullición que el propano."),
   ("abc", "¿Por qué una tabla de propiedades debe indicar la unidad °C?", "Porque sin unidad el número no se puede interpretar", "Para que quede más larga", "No hace falta", "Una temperatura sin unidad no dice nada."),
   ("abc", "{F} Se agrega a la tabla el heptano, con 7 carbonos. Según la tendencia, ¿su punto de ebullición será?", "mayor que el del hexano", "menor que el del metano", "igual al del hexano", "A más carbonos, mayor punto de ebullición."),
   ("abc", "{F} Se quiere separar el aceite del agua en un frasco de ejemplo. ¿Qué propiedad de la ficha lo explica?", "El aceite no se mezcla con agua y flota", "El aceite hierve a 100 °C", "El aceite se disuelve en agua", "No se mezclan, y por eso se ven dos capas."),
   ("abc", "{F} ¿Por qué sería un error afirmar que todos los hidrocarburos son gases?", "Porque el pentano y el hexano son líquidos a 20 °C", "Porque no tienen carbono", "Porque todos hierven a 100 °C", "La tabla muestra hidrocarburos líquidos y gaseosos.")],
  ("abc", "Un cilindro de ejemplo contiene propano y butano y se usa para cocinar. Según la ficha, ¿qué estado tienen ambos a 20 °C si no están comprimidos?", "gas", "líquido", "sólido", "Sus puntos de ebullición, −42 y −1 °C, son menores que 20 °C."),
  [("En Ciencias Naturales: ¿qué es el punto de ebullición?", "La temperatura a la que un líquido hierve", "Es una propiedad que se mide en °C."),
   ("¿Cuál tiene mayor punto de ebullición: metano o pentano?", "El pentano", "Tiene más carbonos: 36 °C frente a −162 °C."),
   ("¿Se mezcla el aceite de cocina con agua?", "No", "El aceite flota sobre el agua.")],
  ("Con los datos de la ficha 3, arma una tabla de las ocho sustancias con las columnas sustancia, punto de ebullición en °C y estado a 20 °C. Ordénala de menor a mayor punto de ebullición y escribe una frase que resuma lo que ves.",
   "Metano −162 gas; etano −89 gas; propano −42 gas; butano −1 gas; pentano 36 líquido; hexano 69 líquido; etanol 78 líquido; agua 100 líquido. A más carbonos, mayor punto de ebullición.",
   ["ordena de menor a mayor", "indica el estado con la regla de 20 °C", "escribe una frase de resumen"],
   ["Ordena bien incluyendo los negativos.", "Aplica la regla del estado.", "La frase refleja la tendencia."],
   "Si ordena mal los negativos, usa una recta numérica."),
  "Calcula tres diferencias entre puntos de ebullición de la ficha.",
  "Explica con un ejemplo por qué la unidad es parte del dato.")

# ====================================================== clase 4
F = ("Ficha 4 (datos de ejemplo). Fuente A, tabla de un texto escolar: el etanol hierve a 78 °C. Fuente B, mensaje anónimo reenviado por el celular: «el etanol hierve a 50 °C». "
     "Mediciones repetidas, hechas en un liceo de ejemplo, del punto de ebullición del etanol: 77, 78, 79 y 78 °C. "
     "Hidrocarburos líquidos, puntos de ebullición en °C: pentano 36; hexano 69; heptano 98; octano 126. "
     "Escala del gráfico de barras: 1 cm de alto por cada 10 °C.")
K(O, 4, F,
  "Hoy practicaré con apoyo cómo se organizan los datos en tablas y gráficos de barras, y cómo se decide si una fuente de datos es confiable.",
  ["Una tabla muestra valores exactos; un gráfico de barras permite comparar de un vistazo. Para armar un gráfico de barras se elige una escala: aquí, 1 cm de alto por cada 10 °C. La altura de cada barra se calcula dividiendo el valor entre 10. La barra del pentano, 36 °C, mide 3,6 cm. Se le pone título y unidades.",
   "No todos los datos son igual de confiables. Se confía más en un dato que viene de una fuente identificable, como un texto escolar, que en un mensaje anónimo reenviado. También en datos que se repiten: si varias mediciones dan valores muy cercanos, como 77, 78, 79 y 78 °C, se puede resumir con el promedio.",
   "Cuando dos fuentes se contradicen, se busca una tercera y se comparan con las mediciones repetidas. Si usas una planilla o la calculadora del celular para organizar datos, hazlo con responsabilidad: anota la fuente de cada dato y no compartas información personal. En esta clase todo se hace en papel con los datos de la ficha."],
  [("gráfico de barras", "gráfico en que cada valor se representa con una barra de altura proporcional"), ("escala", "relación entre lo que mide el dibujo y el valor que representa"), ("fuente confiable", "fuente identificable, revisada y que se puede comprobar"), ("promedio", "suma de los valores dividida por su cantidad")],
  [("Calcular una barra", "{F} ¿Cuánto mide la barra del hexano, 69 °C, con la escala de 1 cm por 10 °C?",
    ["Se divide 69 entre 10.", "69 dividido en 10 es 6,9."], "6,9 cm"),
   ("Elegir la fuente más confiable", "{F} ¿Qué dato del etanol es más confiable, el de la fuente A o el de la B?",
    ["La fuente A es un texto escolar identificable.", "Además coincide con las mediciones repetidas."], "El de la fuente A, 78 °C")],
  [("Dibujar un gráfico sin escala ni título.", "Sin escala no se puede leer el valor de cada barra.", "Escribe el título, la escala y las unidades."),
   ("Creer un dato porque lo reenvió mucha gente.", "Que algo se repita en mensajes no lo hace verdadero.", "Contrasta con una fuente identificable y con mediciones repetidas.")],
  [("abc", "{F} ¿Qué fuente de la ficha es identificable?", "la fuente A, el texto escolar", "la fuente B, el mensaje anónimo", "ninguna", "Un texto escolar tiene autoría y se puede comprobar."),
   ("=", "{F} ¿Cuántos cm mide la barra del heptano, 98 °C, con 1 cm por 10 °C?", "98/10", "Se divide el valor entre 10 °C por cm.", " cm"),
   ("=", "{F} ¿Cuántos cm mide la barra del octano, 126 °C?", "126/10", "Se divide 126 entre 10.", " cm"),
   ("=", "{F} ¿Cuál es el promedio de las mediciones repetidas del etanol (77, 78, 79 y 78)?", "(77+78+79+78)/4", "Se suman las cuatro mediciones y se divide por 4.", " °C"),
   ("abc", "{F} ¿Cuál es la diferencia entre la medición mayor y la menor del etanol?", "2 °C, entre 77 y 79", "10 °C", "28 °C", "79 menos 77 es 2, un rango pequeño: los datos son consistentes."),
   ("abc", "{F} ¿Con qué datos coincide el valor de la fuente A?", "con el promedio de las mediciones, 78 °C", "con el mensaje de la fuente B", "con ningún dato", "El promedio de las mediciones repetidas es 78, igual que la fuente A."),
   ("abc", "{F} Una persona dice: «el etanol hierve a 50 °C porque lo leí en un mensaje que muchos reenviaron». ¿Qué respondes?", "Hay que contrastarlo: otras fuentes dan 78 °C", "Tiene razón, mucha gente lo repite", "Los mensajes siempre son confiables", "La popularidad no prueba un dato."),
   ("abc", "{F} Para comparar de un vistazo los cuatro hidrocarburos líquidos, ¿qué conviene usar?", "un gráfico de barras", "un párrafo sin números", "un dibujo sin escala", "Las barras permiten comparar alturas proporcionales."),
   ("abc", "{F} ¿Qué barra será la más alta?", "la del octano", "la del pentano", "todas iguales", "126 °C es el mayor valor."),
   ("abc", "Si la escala cambia a 1 cm por 20 °C, ¿qué pasa con la altura de las barras?", "se hacen más bajas", "se hacen más altas", "no cambian", "Cada cm representa más °C, así que se necesitan menos cm."),
   ("abc", "¿Qué debe incluir siempre un gráfico bien presentado?", "título, escala y unidades", "solo colores", "solo el nombre de quien lo hizo", "Con esos tres elementos otra persona puede leerlo."),
   ("abc", "Al usar una planilla en el celular para ordenar datos, ¿qué es una práctica responsable?", "anotar la fuente de cada dato y no compartir datos personales", "borrar la fuente para ahorrar espacio", "compartir los datos de otras personas", "Citar la fuente y cuidar la privacidad es uso responsable."),
   ("abc", "{F} Entre las fuentes A y B, ¿qué dato falta para decidir con más seguridad?", "una tercera fuente que confirme el valor", "la cantidad de veces que se reenvió el mensaje", "el nombre de quien lo reenvió", "Una tercera fuente permite contrastar cuál es la correcta.")],
  ("abc", "En un taller de ejemplo se presenta un gráfico de barras sin título ni unidades y alguien pregunta qué mide. ¿Qué falta corregir primero?", "agregar título, unidades y escala", "cambiar los colores", "agrandar las letras", "Sin título ni unidades el gráfico no comunica."),
  [("En Ciencias Naturales: ¿qué es la escala de un gráfico?", "La relación entre el dibujo y el valor que representa", "Por ejemplo, 1 cm por cada 10 °C."),
   ("En un registro de ejemplo: ¿cuál es el promedio de 20, 22 y 24?", "22", "La suma es 66 y 66 entre 3 es 22."),
   ("¿Qué fuente es más confiable: un texto escolar o un mensaje anónimo?", "El texto escolar", "Se puede identificar quién lo escribió y comprobarlo.")],
  ("Con los datos de los hidrocarburos de la ficha 4, calcula la altura de cada barra con la escala de 1 cm por 10 °C y describe el gráfico en palabras (título, qué muestra cada barra y qué conclusión sacas).",
   "Título: Puntos de ebullición de cuatro hidrocarburos (°C). Pentano 3,6 cm; hexano 6,9 cm; heptano 9,8 cm; octano 12,6 cm. Conclusión: a más carbonos, más alta la barra.",
   ["calcula las cuatro alturas", "da título y escala", "escribe una conclusión coherente con las barras"],
   ["Las alturas son correctas.", "Tiene título, escala y unidades.", "La conclusión se apoya en el gráfico."],
   "Si olvida la escala, pregunta «¿cómo lo lee otra persona?»."),
  "Cambia la escala a 1 cm por 20 °C y recalcula las alturas.",
  "Anota tres preguntas para decidir si una fuente de datos es confiable.")

# ====================================================== clase 5
F = ("Ficha 5 (productos de ejemplo, sin marcas). P1, gas licuado en cilindro: propano y butano; en el cilindro se guarda como líquido a presión y, al salir, es gas; inflamable; úselo en un lugar con ventilación y guárdelo lejos de fuentes de calor. "
     "P2, alcohol de uso doméstico: etanol; líquido; se mezcla con agua; el etanol puro hierve a 78 °C; inflamable, guárdelo lejos de fuentes de calor. "
     "P3, vinagre: ácido acético disuelto en agua, alrededor de 5 % en el producto de ejemplo; líquido; se mezcla con agua; sabor ácido. "
     "P4, aceite de cocina: líquido; no se mezcla con agua y flota. "
     "P5, bolsa plástica de polietileno: sólida; no se disuelve en agua; flexible. "
     "Cilindro de ejemplo: contiene 15 kg de gas licuado.")
K(O, 5, F,
  "Hoy aplicaré lo aprendido: organizaré en una tabla las propiedades de productos del hogar hechos de compuestos orgánicos y usaré esos datos para decidir cómo usarlos y guardarlos.",
  ["Muchos productos de tu casa y de tu trabajo son compuestos orgánicos: el gas de la cocina, el alcohol, el vinagre, el aceite y los plásticos. Conocer sus propiedades ayuda a elegir el producto adecuado para cada tarea y a usarlo con seguridad. La información viene en las etiquetas y en las tablas de datos.",
   "La propiedad que más cambia el uso es el estado y la mezcla con agua. Si un producto se mezcla con agua se puede diluir; si flota, como el aceite, no se mezcla. Si es inflamable, como el gas y el alcohol, se guarda lejos del calor y se usa con ventilación. Una tabla con estas columnas permite decidir rápido.",
   "En este cuaderno no se hace ninguna mezcla ni se maneja ningún producto: solo se leen datos de ejemplo. Si en tu trabajo usas estos productos, sigue siempre la etiqueta y las instrucciones de tu empleador. La información de salud o de seguridad concreta la entregan las instituciones y las personas profesionales correspondientes."],
  [("inflamable", "que se enciende con facilidad y se quema"), ("ventilación", "entrada de aire fresco a un lugar"), ("dilución", "mezcla con agua que baja la concentración"), ("etiqueta", "texto del envase con composición y advertencias")],
  [("Leer una tabla de productos", "{F} ¿P2, el alcohol de uso doméstico, se mezcla con agua?",
    ["Busco la propiedad en la ficha.", "Dice que el etanol se mezcla con agua."], "Sí, se mezcla con agua"),
   ("Usar una propiedad para decidir", "{F} ¿Dónde conviene guardar P1, el gas licuado, según la ficha?",
    ["La ficha dice que es inflamable.", "Se usa con ventilación y se guarda lejos del calor."], "En un lugar ventilado y lejos de fuentes de calor")],
  [("Guardar un producto inflamable cerca de una fuente de calor.", "Los vapores o el gas pueden encenderse.", "Lee la etiqueta y guárdalo lejos del calor."),
   ("Suponer que todos los líquidos se pueden diluir con agua.", "El aceite no se mezcla con agua.", "Revisa la propiedad en la tabla antes de decidir.")],
  [("abc", "{F} ¿Cuál de estos productos es inflamable?", "P1, el gas licuado", "P3, el vinagre", "P5, la bolsa plástica", "La ficha indica que el gas licuado y el alcohol son inflamables."),
   ("abc", "{F} ¿Qué compuesto principal tiene P3, el vinagre?", "ácido acético", "etanol", "propano", "La ficha dice que el vinagre es ácido acético disuelto en agua."),
   ("abc", "{F} ¿Qué pasa con el aceite P4 al ponerlo en agua?", "no se mezcla y flota", "se mezcla por completo", "se vuelve sólido", "La ficha indica que el aceite no se mezcla con agua."),
   ("abc", "{F} ¿Cuál de los productos es sólido?", "P5, la bolsa plástica", "P2, el alcohol", "P3, el vinagre", "El polietileno de la bolsa es sólido y flexible."),
   ("=", "{F} Un cilindro de ejemplo trae 15 kg de gas licuado y se gastan 3 kg por semana. ¿Para cuántas semanas alcanza?", "15/3", "Se divide el total entre el consumo semanal.", " semanas"),
   ("abc", "{F} ¿Qué dato de P2 muestra que es un líquido a temperatura ambiente?", "hierve a 78 °C, sobre los 20 °C", "es inflamable", "se mezcla con agua", "Si hierve a 78 °C, a 20 °C todavía es líquido."),
   ("abc", "{F} ¿Qué grupo funcional tiene el etanol de P2?", "alcohol, –OH", "ácido, –COOH", "éter, C–O–C", "El etanol, CH3CH2OH, es un alcohol."),
   ("abc", "{F} ¿Qué grupo funcional da la acidez del vinagre P3?", "–COOH, de ácido carboxílico", "–OH, de alcohol", "un cloro, de haluro", "El ácido acético tiene el grupo –COOH."),
   ("abc", "En una bodega de ejemplo hay gas licuado, alcohol y aceite. ¿Qué decisión de guardado respeta las propiedades de la ficha?", "los dos inflamables, lejos del calor y ventilados", "todos juntos cerca de una estufa", "el gas dentro de un lugar cerrado sin aire", "El gas y el alcohol son inflamables y requieren ventilación."),
   ("abc", "{F} Una persona quiere diluir el aceite de cocina con agua para usarlo en una receta. ¿Qué dato lo desaconseja?", "el aceite no se mezcla con agua", "el aceite es sólido", "el aceite es inflamable", "Al no mezclarse, el aceite y el agua se separan."),
   ("abc", "{F} ¿Cuál es la ventaja de que el gas se guarde como líquido a presión?", "ocupa menos espacio en el cilindro", "pesa menos", "no se puede quemar", "En estado líquido caben más cantidad de gas en el mismo cilindro."),
   ("abc", "Una persona de una comunidad vecinal prepara una tabla de productos del hogar para un taller. ¿Qué columnas son más útiles?", "producto, compuesto, estado, mezcla con agua, advertencia", "marca, precio y color", "solo el nombre del producto", "Esas columnas organizan propiedades para decidir con seguridad."),
   ("abc", "{F} Si alguien sufre un accidente con alguno de estos productos, ¿qué indica el cuaderno?", "acudir a un servicio de salud o de urgencia", "esperar a ver qué pasa", "probar remedios caseros", "Este cuaderno no da consejos médicos.")],
  ("abc", "Se derraman juntos aceite, agua y vinagre en un frasco. ¿Qué dato de la tabla ayuda a prever cuál se separa en capas?", "que el aceite no se mezcla con agua", "que el vinagre es líquido", "que el agua es transparente", "Solo el aceite se separa en capas."),
  [("En Ciencias Naturales: ¿qué significa inflamable?", "Que se enciende con facilidad", "Se guarda lejos del calor y se usa con ventilación."),
   ("¿Qué grupo funcional tiene el vinagre?", "–COOH, de ácido carboxílico", "El ácido acético es un ácido carboxílico."),
   ("¿Se mezcla el etanol con agua?", "Sí", "El etanol es un alcohol que se mezcla con agua.")],
  ("Con la ficha 5, arma una tabla de los cinco productos con las columnas producto, compuesto, estado, mezcla con agua y advertencia. Luego elige uno y escribe una recomendación de guardado basada en la tabla.",
   "P1 | propano y butano | gas | no se indica | inflamable. P2 | etanol | líquido | sí | inflamable. P3 | ácido acético | líquido | sí | sabor ácido. P4 | aceite | líquido | no | flota. P5 | polietileno | sólido | no | no se disuelve. Recomendación: el alcohol se guarda lejos de fuentes de calor.",
   ["completa la tabla con los datos de la ficha", "elige un producto", "basa la recomendación en un dato de la tabla"],
   ["No inventa datos fuera de la ficha.", "La recomendación se apoya en una propiedad.", "Respeta la seguridad indicada."],
   "Si inventa datos, pregunta «¿dónde lo dice la ficha?»."),
  "Anota en un papel cuáles productos de tu casa tienen una advertencia de inflamable, sin abrirlos.",
  "Explica a otra persona por qué el aceite y el agua se separan.")

# ====================================================== clase 6
F = ("Ficha 6 (presentaciones de ejemplo). Tabla T1, sin título ni unidades: «etanol 78; agua 100; propano −42; hexano 69». "
     "Tabla T2, con título y columnas: «Puntos de ebullición aproximados (°C, presión normal)»; sustancia / punto de ebullición: propano / −42; hexano / 69; etanol / 78; agua / 100; fuente: texto escolar de ejemplo. "
     "Afirmación de una compañera: «los compuestos orgánicos siempre hierven a menos de 100 °C». "
     "Mediciones repetidas de ejemplo para el hexano: 68, 70 y 69 °C. Otro dato de ejemplo: el octano, un hidrocarburo, hierve a 126 °C. "
     "Propiedades de ejemplo: ácido acético, se mezcla con agua; aceite, no se mezcla; etanol, se mezcla con agua.")
K(O, 6, F,
  "Hoy revisaré lo logrado: presentaré un resumen claro de propiedades de compuestos orgánicos, evaluaré si los datos son confiables y decidiré mis próximos pasos.",
  ["Presentar información es mostrarla de forma que otra persona la entienda sin que tú estés presente. Una buena presentación tiene título, columnas rotuladas con unidades, datos ordenados y la fuente. Compara T1 y T2: los mismos números, pero solo T2 se entiende bien.",
   "Antes de confiar en una afirmación, se contrasta con los datos. La compañera dice que los compuestos orgánicos siempre hierven bajo 100 °C. Una afirmación con «siempre» se refuta con un solo caso que no la cumpla. También se revisa la confiabilidad: ¿hay fuente?, ¿hay mediciones repetidas?, ¿los valores son consistentes?",
   "Al terminar un trabajo se evalúa qué salió bien, qué falta y qué harías después. Esa revisión es parte de la ciencia: permite mejorar y comunicar con honestidad lo que se sabe y lo que no. Si usas herramientas digitales para organizar datos, cuida la privacidad de las personas y cita siempre la fuente."],
  [("presentación", "forma de mostrar información para que otra persona la entienda"), ("fuente", "origen de un dato, que se anota para poder comprobarlo"), ("contraejemplo", "caso que muestra que una afirmación general es falsa"), ("consistente", "que los datos repetidos dan valores cercanos")],
  [("Comparar presentaciones", "{F} ¿Por qué T2 es mejor presentación que T1?",
    ["T2 tiene título, columnas y fuente.", "T1 solo tiene números sueltos."], "Porque tiene título, columnas rotuladas, unidades y fuente"),
   ("Revisar una afirmación con «siempre»", "{F} La compañera dice que los orgánicos «siempre» hierven bajo 100 °C. Los tres compuestos orgánicos de la tabla T2 cumplen. ¿Queda probada la afirmación?",
    ["Tres casos son pocos.", "Un solo compuesto orgánico que hierva sobre 100 °C la refutaría."], "No: pocos casos no prueban un «siempre»; hay que buscar contraejemplos")],
  [("Dar por probada una afirmación con «siempre» porque se cumple en pocos casos.", "Pocos casos no prueban una regla general.", "Busca contraejemplos o más datos antes de afirmar «siempre»."),
   ("Presentar números sin título, unidades ni fuente.", "Otra persona no puede interpretarlos ni comprobarlos.", "Agrega título, unidades y fuente.")],
  [("abc", "{F} ¿Qué le falta a la tabla T1?", "título, unidades y fuente", "más números", "colores", "Sin esos elementos no se entiende qué miden los números."),
   ("abc", "{F} ¿Qué elemento de T2 permite comprobar los datos?", "la fuente", "el orden de las filas", "el tamaño de la letra", "Con la fuente otra persona puede verificar los valores."),
   ("=", "{F} ¿Cuál es el promedio de las mediciones repetidas del hexano (68, 70 y 69)?", "(68+70+69)/3", "Se suman las tres mediciones y se divide por 3.", " °C"),
   ("abc", "{F} ¿Son consistentes las mediciones del hexano?", "Sí, porque varían solo 2 °C entre 68 y 70", "No, porque son números distintos", "No se puede saber", "Valores cercanos entre sí indican buena repetibilidad."),
   ("abc", "{F} ¿Qué afirmación es más prudente sobre los puntos de ebullición de la ficha?", "«En T2, los tres compuestos orgánicos listados hierven bajo 100 °C»", "«Todos los compuestos orgánicos del mundo hierven bajo 100 °C»", "«Ningún compuesto hierve sobre 100 °C»", "La conclusión debe limitarse a los datos que se tienen."),
   ("abc", "¿Qué hace un contraejemplo con una afirmación general?", "Muestra que es falsa", "La confirma", "No cambia nada", "Un solo caso que no la cumple basta para refutarla."),
   ("abc", "{F} ¿Qué orden de menor a mayor punto de ebullición muestra T2?", "propano, hexano, etanol, agua", "agua, etanol, hexano, propano", "etanol, propano, agua, hexano", "−42, 69, 78 y 100 aumentan en ese orden."),
   ("=", "{F} ¿Cuántos °C hay entre el hexano (69) y el agua (100)?", "100-69", "Se resta el menor del mayor.", " °C"),
   ("abc", "{F} Según la ficha, ¿qué propiedad diferencia al aceite del ácido acético y del etanol?", "el aceite no se mezcla con agua", "el aceite hierve a 100 °C", "el aceite es sólido", "Los otros dos se mezclan con agua."),
   ("abc", "Al compartir un gráfico por el celular, ¿qué práctica es responsable?", "citar la fuente y no incluir datos personales", "quitar la fuente", "agregar los nombres de otras personas", "Citar la fuente y cuidar la privacidad es un uso responsable."),
   ("abc", "{F} ¿Qué dato de la ficha es un contraejemplo de la afirmación de la compañera?", "el octano, que hierve a 126 °C", "el propano, que hierve a −42 °C", "el etanol, que hierve a 78 °C", "Un compuesto orgánico que hierve sobre 100 °C refuta el «siempre»."),
   ("abc", "{F} Se agrega el heptano, 98 °C, a la tabla T2. ¿Dónde va ordenado?", "entre el etanol y el agua", "antes del propano", "después del agua", "98 está entre 78 y 100."),
   ("abc", "{F} ¿Qué paso siguiente mejora más la confiabilidad de la tabla T2?", "contrastar los valores con una segunda fuente", "borrar la fuente", "quitar las unidades", "Una segunda fuente permite confirmar los datos.")],
  ("abc", "Una vecina prepara una tabla de propiedades de productos del hogar para una charla comunitaria. ¿Cuál es el mejor primer paso?", "ponerle título, unidades y fuente a la tabla", "usar solo colores llamativos", "quitar los números para que no se confunda", "Eso la hace comprensible y verificable."),
  [("En Ciencias Naturales: ¿qué es un contraejemplo?", "Un caso que muestra que una afirmación general es falsa", "Basta uno para refutar un «siempre»."),
   ("¿Qué tres cosas debe tener una buena tabla de datos?", "Título, unidades y fuente", "Así otra persona la entiende y la comprueba."),
   ("En una tabla de datos: ¿cuál es el promedio de 10, 12 y 14?", "12", "La suma es 36 y 36 entre 3 es 12.")],
  ("Elige dos propiedades de la ficha (por ejemplo, punto de ebullición y mezcla con agua) y prepara una presentación en papel: una tabla con título, unidades y fuente, una frase de conclusión prudente y dos pasos siguientes para mejorar tu trabajo.",
   "Título: Propiedades aproximadas de cuatro sustancias. Columnas: sustancia, punto de ebullición (°C), se mezcla con agua. Fuente: texto escolar de ejemplo. Conclusión: en estos datos, el etanol y el ácido acético se mezclan con agua. Pasos: contrastar con otra fuente y agregar más sustancias.",
   ["arma una tabla con título, unidades y fuente", "escribe una conclusión prudente", "propone dos pasos siguientes"],
   ["Usa solo datos de la ficha.", "La conclusión no generaliza de más.", "Los pasos son concretos."],
   "Si generaliza con «siempre», pide un contraejemplo."),
  "Resume en cinco líneas lo que aprendiste sobre compuestos orgánicos y grupos funcionales.",
  "Explica a otra persona por qué una tabla sin fuente es menos confiable.")

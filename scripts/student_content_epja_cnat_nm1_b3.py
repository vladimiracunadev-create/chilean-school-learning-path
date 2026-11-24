"""Ciencias Naturales EPJA Media N1, módulo 2, desempeño OAD-07: explicar cómo se forman compuestos orgánicos presentes en sustancias de la vida cotidiana (enlaces del carbono, hidrocarburos, grupos funcionales, fermentación, combustión, ésteres, polímeros). Todo en papel; ecuaciones con átomos verificados."""
from __future__ import annotations

from epja_cnat_nm1_b_common import K

O = "EPJA-CNAT-NM1-OAD-07"

# ====================================================== clase 1
F = ("Ficha 1 (de dónde vienen algunos compuestos orgánicos de uso diario; texto de ejemplo). A1: el azúcar de mesa lo producen plantas como la caña y la remolacha, a partir de dióxido de carbono, agua y luz. "
     "A2: el alcohol del vino se forma cuando las levaduras transforman azúcares; ese proceso se llama fermentación. "
     "A3: el vinagre se forma cuando unas bacterias transforman ese alcohol en ácido acético. "
     "A4: el gas licuado se obtiene del gas natural y del petróleo. "
     "A5: el plástico polietileno se fabrica en la industria a partir de etileno, que se obtiene del petróleo o del gas natural. "
     "A6: el aceite de cocina lo producen plantas, por ejemplo el girasol.")
K(O, 1, F,
  "Hoy partiré de las sustancias que uso a diario para preguntarme de dónde vienen los compuestos orgánicos y cómo se forman.",
  ["Los compuestos orgánicos que usas en tu casa no aparecen de la nada. Algunos los forman los seres vivos: las plantas producen azúcar y aceite; las levaduras producen el alcohol del vino. Otros se obtienen en la industria a partir del petróleo y del gas natural, como el gas licuado y los plásticos.",
   "En todos los casos ocurre una reacción química: unos átomos se unen a otros de una forma nueva. Un enlace es una unión entre átomos. En los compuestos orgánicos los átomos suelen compartir electrones, unas partículas muy pequeñas, y así quedan unidos. Los átomos no se crean ni se destruyen: se reorganizan.",
   "Explicar cómo se forma un compuesto es decir de qué sustancias parte, qué proceso ocurre y qué se obtiene. Por ejemplo: la levadura parte del azúcar, fermenta y produce alcohol. En esta clase solo ordenamos esas ideas con los textos de la ficha, sin hacer experimentos."],
  [("enlace", "unión entre átomos"), ("fermentación", "proceso en que seres vivos pequeños transforman azúcares en otras sustancias"), ("levadura", "ser vivo muy pequeño que fermenta azúcares"), ("petróleo", "mezcla natural de hidrocarburos de la que se obtienen combustibles y plásticos")],
  [("Identificar el origen", "{F} ¿De qué parte el alcohol del vino, según A2?",
    ["Leo A2.", "Dice que las levaduras transforman azúcares."], "De azúcares, transformados por levaduras"),
   ("Ordenar un proceso", "{F} Ordena los pasos del vinagre según A2 y A3.",
    ["Primero hay azúcares.", "Las levaduras forman alcohol y luego unas bacterias forman ácido acético."], "Azúcar, alcohol, ácido acético")],
  [("Pensar que los compuestos orgánicos solo los hacen los seres vivos.", "También se fabrican en la industria a partir del petróleo y el gas natural.", "Pregunta siempre de qué sustancias parte y qué proceso ocurre."),
   ("Decir que en una reacción los átomos se crean o desaparecen.", "Los átomos se reorganizan y se conservan.", "Habla de átomos que se unen de otra manera.")],
  [("abc", "{F} ¿De dónde se obtiene el gas licuado, según A4?", "del gas natural y del petróleo", "de las plantas de girasol", "de las levaduras", "La ficha, en A4, lo indica así de forma directa."),
   ("abc", "{F} ¿Qué produce el azúcar de mesa, según A1?", "plantas como la caña y la remolacha", "las bacterias del vinagre", "la industria del plástico", "A1 dice que lo producen plantas."),
   ("abc", "{F} ¿Qué proceso forma el alcohol del vino?", "la fermentación", "la combustión", "la evaporación", "A2 llama fermentación a ese proceso."),
   ("abc", "{F} ¿Qué se forma cuando unas bacterias transforman el alcohol, según A3?", "ácido acético", "azúcar", "gas natural", "A3 dice que se forma el ácido acético del vinagre."),
   ("abc", "{F} ¿De qué se obtiene el etileno para fabricar polietileno, según A5?", "del petróleo o del gas natural", "de las plantas de caña", "del agua", "A5 explica el origen del etileno."),
   ("abc", "Un enlace entre átomos es", "una unión entre ellos", "una mezcla de líquidos", "un tipo de combustible", "Los enlaces mantienen unidos los átomos de una molécula."),
   ("=", "{F} De los 6 ejemplos de la ficha, 2 se obtienen de la industria (A4 y A5). ¿Cuántos los producen seres vivos?", "6-2", "Se restan los industriales del total: A1, A2, A3 y A6.", " ejemplos"),
   ("abc", "{F} ¿Cuáles de los ejemplos son producidos por seres vivos?", "A1, A2, A3 y A6", "solo A4 y A5", "ninguno", "Plantas, levaduras y bacterias los forman."),
   ("abc", "Una persona dice: «en la fermentación el azúcar desaparece». ¿Qué respondes?", "Sus átomos se reorganizan en alcohol y otros productos", "Tiene razón, los átomos desaparecen", "El azúcar se convierte en energía y nada más", "Los átomos se conservan y se reordenan."),
   ("abc", "{F} ¿Qué relación hay entre A2 y A3?", "el producto de A2 es el punto de partida de A3", "no tienen relación", "A3 ocurre antes que A2", "El alcohol que forman las levaduras lo transforman luego las bacterias."),
   ("abc", "{F} Una persona de una cooperativa dice que los plásticos «no vienen de ninguna sustancia natural». ¿Qué datos de la ficha lo cuestionan?", "A5: el polietileno parte del etileno, que se obtiene del petróleo o del gas natural", "A1: el azúcar viene de la caña", "A3: el vinagre", "El petróleo y el gas natural son recursos naturales."),
   ("abc", "Para explicar cómo se forma un compuesto, ¿qué tres cosas conviene decir?", "de qué parte, qué proceso ocurre y qué se obtiene", "su color, su precio y su marca", "dónde se vende", "Esa estructura da una explicación completa."),
   ("abc", "{F} ¿Qué sustancia de la ficha se fabrica en la industria y no la producen seres vivos?", "el polietileno", "el aceite de girasol", "el alcohol del vino", "El plástico viene de etileno obtenido del petróleo o del gas natural.")],
  ("abc", "En una cocina comunitaria de ejemplo se explica que el vinagre «se forma con azúcar de la nada». ¿Qué corrección usa la ficha?", "Parte de azúcares, que las levaduras fermentan y las bacterias transforman en ácido acético", "El vinagre es agua con sal", "El vinagre es un plástico", "A2 y A3 describen la cadena de transformaciones."),
  [("En Ciencias Naturales: ¿qué es la fermentación?", "Un proceso en que seres vivos pequeños transforman azúcares", "Por ejemplo, las levaduras forman alcohol."),
   ("¿De dónde se obtiene el etileno para el polietileno?", "Del petróleo o del gas natural", "Es materia prima de la industria del plástico."),
   ("¿Los átomos se crean o se destruyen en una reacción?", "No, se reorganizan", "La materia se conserva porque los átomos solo se reorganizan.")],
  ("Elige un producto de tu casa de la ficha (azúcar, vinagre, gas licuado, plástico, aceite). Escribe en tres líneas de qué parte, qué proceso lo forma y qué obtiene. Usa solo datos de la ficha.",
   "Vinagre: parte de azúcares; las levaduras los fermentan y forman alcohol; unas bacterias lo transforman en ácido acético.",
   ["dice de qué parte", "nombra el proceso", "dice qué se obtiene"],
   ["Usa los datos de la ficha.", "Ordena la secuencia.", "No inventa pasos."],
   "Si olvida un paso, pregunta «¿qué había antes?»."),
  "Anota tres productos de tu casa y dónde crees que se originan.",
  "Explica en una frase por qué los átomos no desaparecen cuando se forma un compuesto.")

# ====================================================== clase 2
F = ("Ficha 2 (cómo se unen los átomos, modelo simple de ejemplo). Carbono, C: forma 4 enlaces. Hidrógeno, H: forma 1 enlace. Oxígeno, O: forma 2 enlaces. Cloro, Cl: forma 1 enlace. "
     "Un enlace simple se escribe con una raya (–), uno doble con dos rayas (=) y uno triple con tres (≡). "
     "Hidrocarburos de ejemplo: metano CH4, con 1 carbono; etano C2H6, con 2 carbonos unidos por un enlace simple; eteno C2H4, con 2 carbonos unidos por un enlace doble; etino C2H2, con 2 carbonos unidos por un enlace triple. "
     "En una cadena de n carbonos con solo enlaces simples, el número de hidrógenos es 2n + 2.")
K(O, 2, F,
  "Hoy explicaré cómo el carbono forma enlaces para construir moléculas orgánicas: metano, etano y otros hidrocarburos.",
  ["Para armar una molécula orgánica se parte de una regla: el carbono forma cuatro enlaces, el hidrógeno uno, el oxígeno dos y el cloro uno. Una molécula es estable cuando todos sus átomos tienen completos sus enlaces. En el metano, CH4, el carbono se une a cuatro hidrógenos: 4 enlaces para el carbono y 1 para cada hidrógeno.",
   "Los carbonos también se unen entre sí. En el etano, C2H6, dos carbonos comparten un enlace; a cada uno le quedan tres enlaces para tres hidrógenos. Si dos carbonos comparten dos enlaces, el enlace doble, a cada uno le quedan dos para hidrógenos, y resulta el eteno, C2H4. Con un enlace triple resulta el etino, C2H2.",
   "Cuando la cadena tiene solo enlaces simples, hay una regla para contar: con n carbonos hay 2n + 2 hidrógenos. Con n = 3, el propano tiene 2 x 3 + 2 = 8 hidrógenos: C3H8. Con esa regla se pueden prever fórmulas sin dibujar. Aquí no se manipula ninguna sustancia: solo se cuentan átomos y enlaces."],
  [("enlace simple", "unión de dos átomos con una raya"), ("enlace doble", "unión de dos átomos que comparten dos enlaces"), ("cadena de carbonos", "carbonos unidos uno tras otro"), ("fórmula", "escritura que indica los átomos de una molécula")],
  [("Prever una fórmula", "{F} ¿Cuántos hidrógenos tiene un hidrocarburo de cadena simple con 4 carbonos?",
    ["Uso 2n + 2 con n = 4.", "2 x 4 + 2 = 10."], "10 hidrógenos: C4H10"),
   ("Comprobar los enlaces", "{F} En el eteno, C2H4, ¿cuántos enlaces tiene cada carbono?",
    ["Cada carbono tiene el enlace doble: 2.", "Y dos hidrógenos: 2 más. Suman 4."], "4 enlaces, como exige la regla")],
  [("Dibujar un carbono con cinco enlaces.", "El carbono forma exactamente cuatro enlaces.", "Cuenta los enlaces de cada carbono: deben sumar cuatro."),
   ("Contar mal los hidrógenos en una cadena.", "Se olvida que los carbonos de los extremos tienen un hidrógeno más.", "Usa la regla 2n + 2 y comprueba contando enlaces.")],
  [("abc", "{F} ¿Cuántos enlaces forma el átomo de hidrógeno?", "1", "2", "4", "La ficha indica un enlace para el hidrógeno."),
   ("abc", "{F} ¿Cuántos enlaces forma un átomo de oxígeno?", "2", "1", "4", "La ficha dice que el oxígeno forma dos enlaces."),
   ("=", "{F} ¿Cuántos hidrógenos tiene un hidrocarburo de cadena simple con 3 carbonos? (2n + 2)", "2*3+2", "Se aplica la regla con n = 3.", " hidrógenos"),
   ("=", "{F} ¿Cuántos hidrógenos tiene un hidrocarburo de cadena simple con 5 carbonos? (2n + 2)", "2*5+2", "Se aplica la regla con n = 5.", " hidrógenos"),
   ("=", "{F} ¿Cuántos hidrógenos tiene un hidrocarburo de cadena simple con 6 carbonos? (2n + 2)", "2*6+2", "Se aplica la regla con n = 6.", " hidrógenos"),
   ("abc", "{F} ¿Cuál es la fórmula del propano?", "C3H8", "C3H6", "C2H8", "Con 3 carbonos hay 2 x 3 + 2 = 8 hidrógenos."),
   ("abc", "{F} ¿Por qué el etano tiene seis hidrógenos?", "A cada carbono le quedan tres enlaces para hidrógenos", "Porque el carbono forma seis enlaces", "Porque los hidrógenos forman dos enlaces", "Cada carbono usa uno para unirse al otro y tres para H."),
   ("abc", "{F} ¿Qué tipo de enlace hay entre los carbonos del etino, C2H2?", "triple", "simple", "doble", "La ficha indica un enlace triple entre los dos carbonos."),
   ("=", "{F} En una molécula de metano, ¿cuántos enlaces hay en total entre el carbono y los hidrógenos?", "4*1", "Cada uno de los 4 hidrógenos forma un enlace con el carbono.", " enlaces"),
   ("abc", "Una persona dibuja un carbono unido a cinco hidrógenos. ¿Qué error tiene?", "El carbono no puede formar cinco enlaces", "Faltan oxígenos", "Los hidrógenos no se unen al carbono", "El carbono forma cuatro enlaces exactamente."),
   ("abc", "{F} En el etino, C2H2, cada carbono usa 3 enlaces para unirse al otro carbono. ¿Cuántos le quedan para hidrógenos?", "1", "2", "3", "Cada carbono forma 4 enlaces: 4 menos 3 deja uno para un hidrógeno."),
   ("abc", "{F} El hidrocarburo de 10 carbonos de cadena simple, según 2n + 2, tendría", "22 hidrógenos", "20 hidrógenos", "12 hidrógenos", "2 x 10 + 2 = 22."),
   ("abc", "{F} ¿Cuál de estas es una fórmula posible de un compuesto con un carbono y cloros, según los enlaces de la ficha?", "CCl4", "CCl2", "CCl6", "El carbono forma 4 enlaces y cada cloro uno, así que se unen 4 cloros.")],
  ("abc", "Un técnico de ejemplo dice que el octano tiene 8 carbonos y 16 hidrógenos. Con la regla de la ficha, ¿qué respondes?", "Debe tener 18 hidrógenos: C8H18", "Está bien, C8H16", "Debe tener 8 hidrógenos", "2 x 8 + 2 da 18."),
  [("En Ciencias Naturales: ¿cuántos enlaces forma el carbono?", "4", "Es la regla que explica sus compuestos."),
   ("¿Qué fórmula tiene el etano?", "C2H6", "Dos carbonos con tres hidrógenos cada uno."),
   ("¿Qué regla da el número de hidrógenos en una cadena simple de n carbonos?", "2n + 2", "Con n = 3 resultan 8.")],
  ("Explica en un texto breve cómo se forma el etano a partir de dos carbonos y seis hidrógenos: cuántos enlaces forma cada átomo, cómo se unen los carbonos entre sí y cómo comprobarías que cada carbono tiene cuatro enlaces. Usa la ficha.",
   "Cada carbono forma cuatro enlaces. Los dos carbonos comparten uno. A cada carbono le quedan tres enlaces para tres hidrógenos. Cada carbono suma 1 + 3 = 4 y cada hidrógeno tiene 1.",
   ["usa la regla de los enlaces", "describe la unión entre carbonos", "comprueba que cada carbono suma cuatro"],
   ["Usa números de enlaces correctos.", "Menciona el enlace carbono-carbono.", "La comprobación es explícita."],
   "Si cuenta cinco enlaces, pide que sume otra vez cada carbono."),
  "Calcula los hidrógenos de cadenas simples con 9 y 12 carbonos.",
  "Explica por qué el eteno tiene menos hidrógenos que el etano.")

# ====================================================== clase 3
F = ("Ficha 3 (formación de grupos funcionales, modelo de ejemplo). Idea: un átomo de hidrógeno de un hidrocarburo se puede reemplazar por otro átomo o grupo. "
     "S1: metano CH4 → clorometano CH3Cl: un hidrógeno se reemplaza por un cloro (el hidrógeno sale como HCl). "
     "S2: metano CH4 → metanol CH3OH: un hidrógeno se reemplaza por el grupo –OH. "
     "S3: etano C2H6 → etanol C2H5OH: un hidrógeno se reemplaza por el grupo –OH. "
     "Ecuación de ejemplo: CH4 + Cl2 → CH3Cl + HCl. "
     "Fermentación de la glucosa (ejemplo): C6H12O6 → 2 C2H5OH + 2 CO2.")
K(O, 3, F,
  "Hoy explicaré cómo se forman alcoholes y haluros a partir de hidrocarburos y cómo se forma el etanol en la fermentación, comprobando los átomos de cada ecuación.",
  ["Un grupo funcional se puede formar reemplazando un hidrógeno de un hidrocarburo por otro átomo o grupo. Si en el metano, CH4, un hidrógeno se reemplaza por un cloro, queda CH3Cl, un haluro. Si se reemplaza por el grupo –OH, queda CH3OH, el metanol, un alcohol. Con el etano se forma el etanol, C2H5OH.",
   "Una ecuación química debe tener los mismos átomos antes y después. En CH4 + Cl2 → CH3Cl + HCl hay 1 carbono, 4 hidrógenos y 2 cloros a cada lado: a la izquierda, 4 H en CH4 y 2 Cl en Cl2; a la derecha, 3 H + 1 H = 4 H y 1 Cl + 1 Cl = 2 Cl. Los átomos solo se reordenaron.",
   "La naturaleza también forma alcoholes. En la fermentación, una molécula de glucosa, C6H12O6, forma dos de etanol y dos de dióxido de carbono. Se comprueba contando: 6 carbonos, 12 hidrógenos y 6 oxígenos en cada lado. En esta clase solo se leen ecuaciones: no se hace ninguna reacción."],
  [("sustitución", "cambio de un átomo por otro en una molécula"), ("ecuación química", "escritura de una reacción con reactantes y productos"), ("balance de átomos", "comprobación de que hay los mismos átomos a cada lado"), ("glucosa", "azúcar simple, C6H12O6")],
  [("Contar átomos", "{F} ¿Cuántos átomos de hidrógeno hay en total en el lado derecho de CH4 + Cl2 → CH3Cl + HCl?",
    ["En CH3Cl hay 3 hidrógenos.", "En HCl hay 1: suman 4."], "4 hidrógenos"),
   ("Formar un alcohol", "{F} ¿Cómo se forma el etanol a partir del etano, según S3?",
    ["El etano es C2H6.", "Un hidrógeno se reemplaza por el grupo –OH y queda C2H5OH."], "Un hidrógeno del etano se reemplaza por –OH")],
  [("Cambiar un hidrógeno por un cloro y olvidar que el hidrógeno sale.", "El hidrógeno que sale forma otra sustancia, HCl.", "Cuenta todos los átomos de los dos lados de la ecuación."),
   ("Escribir una ecuación con distinto número de átomos a cada lado.", "Los átomos no se crean ni se destruyen.", "Cuenta cada elemento antes y después.")],
  [("abc", "{F} ¿Qué se reemplaza en S1 para formar CH3Cl?", "un hidrógeno por un cloro", "un carbono por un cloro", "un oxígeno por un cloro", "S1 explica que un hidrógeno se reemplaza por cloro."),
   ("abc", "{F} ¿Qué grupo funcional tiene el metanol, CH3OH?", "alcohol, –OH", "haluro, –Cl", "ácido, –COOH", "Tiene el grupo –OH, propio de los alcoholes."),
   ("abc", "{F} ¿Qué grupo funcional tiene CH3Cl?", "haluro", "alcohol", "éter", "Un cloro unido a carbono forma un haluro."),
   ("=", "{F} En C2H5OH, ¿cuántos átomos de hidrógeno hay? (5 en C2H5 y 1 en OH)", "5+1", "Se suman los hidrógenos de ambas partes de la fórmula.", " hidrógenos"),
   ("=", "{F} ¿Cuántos átomos de carbono hay en 2 C2H5OH? (2 moléculas)", "2*2", "Cada molécula tiene 2 carbonos y hay 2 moléculas.", " carbonos"),
   ("=", "{F} ¿Cuántos átomos de hidrógeno hay en 2 C2H5OH?", "2*6", "Cada molécula tiene 6 hidrógenos y hay 2 moléculas.", " hidrógenos"),
   ("abc", "{F} En la fermentación, ¿cuántos átomos de oxígeno hay en C6H12O6?", "6", "12", "2", "El subíndice del oxígeno es 6."),
   ("=", "{F} ¿Cuántos átomos de oxígeno hay en 2 C2H5OH + 2 CO2? (2 de alcohol y 4 de dióxido)", "2+4", "Se suman los oxígenos de los dos productos.", " oxígenos"),
   ("abc", "{F} La ecuación de la fermentación, ¿cumple la conservación de los átomos de carbono?", "Sí: 6 carbonos antes y 4 + 2 = 6 después", "No: hay más carbonos después", "No se puede comprobar", "2 etanoles aportan 4 carbonos y 2 CO2 aportan 2."),
   ("abc", "{F} Una persona dice que en S1 «el hidrógeno desaparece». ¿Qué respondes?", "Sale unido al cloro, formando HCl", "Tiene razón, desaparece", "Se convierte en carbono", "La ecuación muestra que el hidrógeno forma HCl."),
   ("abc", "{F} ¿Qué relación hay entre el metano y el metanol?", "el metanol resulta de reemplazar un H del metano por –OH", "son el mismo compuesto", "el metano resulta de agregar cloro al metanol", "La fila S2 de la ficha explica ese reemplazo."),
   ("abc", "{F} ¿Por qué el etanol y el metanol son alcoholes aunque tengan distinto número de carbonos?", "Ambos tienen el grupo –OH", "Ambos tienen cloro", "Ambos son gases", "El grupo funcional define la familia."),
   ("abc", "{F} Una persona escribe CH4 + Cl2 → CH3Cl. ¿Qué falta?", "HCl, para que haya los mismos átomos a cada lado", "más carbono", "agua", "Con HCl los hidrógenos y los cloros cuadran.")],
  ("abc", "En una fábrica de ejemplo se explica que el alcohol del vino se forma «de la nada». ¿Qué ecuación de la ficha lo explica con átomos?", "C6H12O6 → 2 C2H5OH + 2 CO2", "CH4 + Cl2 → CH3Cl + HCl", "H2 + O2 → H2O", "La fermentación forma etanol y dióxido de carbono desde la glucosa."),
  [("En Ciencias Naturales: ¿qué pasa en una sustitución?", "Un átomo o grupo reemplaza a otro en la molécula", "Por ejemplo, un H se reemplaza por –OH."),
   ("¿Cuántos átomos de carbono tiene la glucosa C6H12O6?", "6", "El subíndice del carbono es 6."),
   ("¿Qué debe cumplir toda ecuación sobre los átomos?", "Tener los mismos átomos a cada lado", "Los átomos se conservan y solo se reorganizan.")],
  ("Elige S1, S2 o S3 de la ficha. Escribe la fórmula del hidrocarburo, la del producto, qué átomo o grupo reemplaza a un hidrógeno y a qué familia pertenece el producto. Comprueba contando átomos de un elemento.",
   "S3: etano C2H6 → etanol C2H5OH. Un hidrógeno se reemplaza por –OH. Es un alcohol. Carbonos: 2 antes y 2 después.",
   ["escribe las dos fórmulas", "dice qué reemplaza al hidrógeno", "clasifica el producto y comprueba un conteo"],
   ["Las fórmulas coinciden con la ficha.", "Nombra el grupo funcional.", "El conteo es correcto."],
   "Si el conteo falla, pide que cuente elemento por elemento."),
  "Cuenta los átomos de hidrógeno de cada lado de la ecuación de S1.",
  "Escribe con tus palabras por qué se puede decir que la fermentación «reorganiza» los átomos de la glucosa.")

# ====================================================== clase 4
F = ("Ficha 4 (reacciones de formación de ejemplo, con átomos y masas). R1, combustión del metano: CH4 + 2 O2 → CO2 + 2 H2O; masas: 16 g + 64 g → 44 g + 36 g. "
     "R2, combustión del propano: C3H8 + 5 O2 → 3 CO2 + 4 H2O. "
     "R3, formación de un éster (olor frutal): ácido acético CH3COOH + etanol C2H5OH → acetato de etilo CH3COOC2H5 + agua H2O. "
     "Masas de R2, en gramos: 44 g de propano + 160 g de oxígeno → 132 g de dióxido de carbono + 72 g de agua. R4, polimerización: muchas moléculas de etileno C2H4 (28 de masa cada una) se unen en una cadena larga de polietileno. "
     "Nota de seguridad: en la combustión con poco oxígeno se forma monóxido de carbono, un gas tóxico sin olor; por eso se ventila.")
K(O, 4, F,
  "Hoy practicaré con apoyo cómo se explican las reacciones que forman compuestos orgánicos: combustión, formación de ésteres y polimerización, siempre comprobando los átomos y las masas.",
  ["Los compuestos orgánicos se forman y se transforman en distintas reacciones. En la combustión, un hidrocarburo reacciona con oxígeno y forma dióxido de carbono y agua, y libera energía. Para comprobar una ecuación se cuentan los átomos: en CH4 + 2 O2 → CO2 + 2 H2O hay 1 C, 4 H y 4 O a cada lado.",
   "En la formación de un éster, un ácido carboxílico y un alcohol se unen y sueltan una molécula de agua. Muchos ésteres tienen olores frutales. En la polimerización, muchas moléculas pequeñas, los monómeros, se unen en una cadena larga, el polímero. Así se fabrica el polietileno de las bolsas.",
   "También se comprueba la masa. En la combustión del metano, 16 g de metano y 64 g de oxígeno suman 80 g; los productos, 44 g de dióxido de carbono y 36 g de agua, también suman 80 g. Las reacciones de este cuaderno son solo ejemplos para leer: no se queman sustancias. La combustión con poco oxígeno forma un gas tóxico, por eso se ventila."],
  [("combustión", "reacción de un combustible con oxígeno que libera energía"), ("éster", "compuesto que se forma al unirse un ácido carboxílico y un alcohol"), ("monómero", "molécula pequeña que se une a otras iguales"), ("polímero", "cadena larga formada por muchos monómeros")],
  [("Balancear átomos", "{F} En R1, ¿cuántos átomos de oxígeno hay en los reactantes, 2 O2?",
    ["Cada O2 tiene 2 átomos.", "Hay 2 moléculas: 2 x 2 = 4."], "4 átomos de oxígeno"),
   ("Balancear masas", "{F} En R1, ¿se conserva la masa?",
    ["Reactantes: 16 + 64 = 80 g.", "Productos: 44 + 36 = 80 g."], "Sí, 80 g = 80 g")],
  [("Olvidar el número delante de una fórmula al contar átomos.", "El 2 delante de H2O multiplica todos sus átomos.", "Multiplica el número delante por los átomos de cada elemento."),
   ("Creer que en la polimerización se pierde materia.", "Los monómeros se unen: la masa de la cadena es la suma de las masas.", "Suma las masas de todos los monómeros.")],
  [("=", "{F} En R1, ¿cuántos átomos de oxígeno hay en los productos? (2 en CO2 y 2 en 2 H2O)", "2+2", "Se suman los oxígenos de CO2 y de las dos moléculas de agua.", " átomos"),
   ("=", "{F} En R1, ¿cuántos átomos de hidrógeno hay en los productos, 2 H2O?", "2*2", "Cada agua tiene 2 hidrógenos y hay 2 moléculas.", " átomos"),
   ("=", "{F} ¿Cuántos gramos suman los reactantes de R2 (44 g y 160 g)?", "44+160", "Se suman las masas de propano y de oxígeno.", " g"),
   ("=", "{F} ¿Cuántos gramos suman los productos de R2 (132 g y 72 g)?", "132+72", "Se suman las masas del dióxido de carbono y del agua.", " g"),
   ("=", "{F} En R2, ¿cuántos átomos de oxígeno hay en los reactantes, 5 O2?", "5*2", "Cada O2 tiene 2 átomos.", " átomos"),
   ("=", "{F} En R2, ¿cuántos átomos de oxígeno hay en los productos, 3 CO2 y 4 H2O?", "3*2+4*1", "3 CO2 aportan 6 oxígenos y 4 H2O aportan 4.", " átomos"),
   ("abc", "{F} ¿Se conservan los átomos de oxígeno en R2?", "Sí: 10 antes y 6 + 4 = 10 después", "No: hay más antes", "No se puede saber", "Los dos lados tienen 10 oxígenos."),
   ("abc", "{F} ¿Qué se forma junto con el éster en R3?", "agua", "dióxido de carbono", "metano", "El ácido y el alcohol sueltan una molécula de agua."),
   ("abc", "{F} ¿Qué es el etileno en R4?", "el monómero del polietileno", "el polímero", "un tipo de enlace entre átomos", "Las moléculas de etileno se unen para formar la cadena."),
   ("=", "{F} Si 10 moléculas de etileno se unen en una cadena, ¿cuánta masa tiene la cadena, con 28 por molécula?", "10*28", "La masa de la cadena es la suma de la de sus monómeros.", ""),
   ("abc", "{F} Una persona dice que con poco oxígeno la combustión es igual de segura. ¿Qué dice la ficha?", "Puede formarse monóxido de carbono, un gas tóxico sin olor", "Es más segura", "No cambia nada", "La nota indica el riesgo y la medida: ventilar."),
   ("abc", "{F} ¿Por qué se ventila un lugar donde hay combustión?", "para que haya oxígeno suficiente y no se forme monóxido de carbono", "para que se formen más ésteres", "para que el combustible reaccione sin oxígeno", "Con poco oxígeno se forma un gas tóxico."),
   ("abc", "{F} ¿Qué diferencia hay entre monómero y polímero?", "el polímero es la cadena larga formada por monómeros", "el monómero es la cadena larga", "son lo mismo", "Polímero significa muchas partes unidas en una misma cadena.")],
  ("abc", "Una persona de una panadería de ejemplo dice que el olor frutal de una esencia viene de un éster. ¿Qué dos tipos de compuestos se unieron para formarlo, según la ficha?", "un ácido carboxílico y un alcohol", "dos hidrocarburos", "dos haluros", "R3 forma el éster con un ácido y un alcohol."),
  [("En Ciencias Naturales: ¿qué es un polímero?", "Una cadena larga formada por muchos monómeros", "El polietileno de las bolsas es un ejemplo de polímero."),
   ("¿Qué se forma en la combustión de un hidrocarburo con suficiente oxígeno?", "Dióxido de carbono y agua", "Y además se libera energía en forma de calor."),
   ("¿Cuántos gramos suman 16 g y 64 g?", "80", "Es la masa de los reactantes de R1.")],
  ("Elige R1 o R2. Cuenta los átomos de carbono, hidrógeno y oxígeno de cada lado de la ecuación, di si se conservan y explica en dos frases qué hace cada reactante. Cierra con la medida de seguridad de la ficha.",
   "R1: antes 1 C, 4 H y 4 O; después 1 C, 4 H y 4 O. Se conservan. El metano es el combustible y el oxígeno lo permite. Se ventila para evitar monóxido de carbono.",
   ["cuenta tres elementos a cada lado", "concluye sobre la conservación", "incluye la medida de seguridad"],
   ["Los conteos son correctos.", "La conclusión se apoya en los conteos.", "Cita la ventilación."],
   "Si cuenta mal, pide que multiplique el número delante."),
  "Cuenta los átomos de R3 en cada lado.",
  "Explica por qué se dice que el polietileno es un polímero.")

# ====================================================== clase 5
F = ("Ficha 5 (productos de ejemplo y su formación). T1, pan de masa fermentada: las levaduras fermentan azúcares y forman dióxido de carbono, que infla la masa, y un poco de etanol. "
     "T2, vinagre: bacterias transforman el etanol en ácido acético. "
     "T3, aroma de fruta madura: se forman ésteres a partir de ácidos y alcoholes. "
     "T4, bolsa plástica: polietileno, formado por la unión de moléculas de etileno. "
     "T5, gas licuado: hidrocarburos como propano y butano, que se obtienen del gas natural y del petróleo. "
     "T6, azúcar: la forman plantas a partir de dióxido de carbono, agua y luz. "
     "Datos para calcular: un lote de ejemplo de 12 bolsas usa 15 g de plástico cada una.")
K(O, 5, F,
  "Hoy aplicaré lo aprendido a situaciones de trabajo, hogar y comunidad: explicaré cómo se forman compuestos orgánicos de productos cotidianos y relacionaré el proceso con su uso.",
  ["Una explicación completa de cómo se forma un compuesto responde cuatro preguntas: de qué sustancias parte, qué proceso ocurre, qué se obtiene y qué se conserva. Con ellas puedes explicar el pan, el vinagre, el aroma de una fruta, una bolsa plástica o el gas de la cocina.",
   "En el pan, la fermentación forma dióxido de carbono, que infla la masa, y un poco de alcohol. En el vinagre, unas bacterias transforman ese alcohol en ácido acético. En el aroma de la fruta se forman ésteres. En la bolsa, los monómeros de etileno se unen en un polímero. En todos los casos los átomos se conservan.",
   "Aplicar también es decidir con criterio. Un panadero necesita que la masa sea fermentada; una vecina que recicla plásticos entiende que son cadenas de carbono hechas por la industria. Aquí trabajas con la ficha, sin manipular sustancias, y relacionas la formación con el uso."],
  [("fermentar", "transformar azúcares con ayuda de seres vivos pequeños"), ("materia prima", "sustancia de la que parte la fabricación de otra"), ("proceso", "serie de pasos que transforma unas sustancias en otras"), ("conservación", "los átomos se mantienen, solo se reorganizan")],
  [("Explicar con las cuatro preguntas", "{F} Explica cómo se forma el gas dentro de la masa de T1.",
    ["Parte de azúcares.", "Las levaduras fermentan y forman CO2."], "Las levaduras fermentan azúcares y forman dióxido de carbono"),
   ("Calcular con datos", "{F} ¿Cuántos gramos de plástico usa el lote de 12 bolsas de 15 g cada una?",
    ["Se multiplica el número de bolsas por la masa de cada una.", "12 x 15 = 180."], "180 g")],
  [("Decir que el plástico «se fabrica de la nada».", "Parte de monómeros como el etileno, obtenido del petróleo o del gas natural.", "Nombra siempre de qué sustancias parte."),
   ("Explicar solo el resultado y omitir el proceso.", "Falta decir cómo se transforman las sustancias.", "Usa las cuatro preguntas: parte, proceso, obtiene y conserva.")],
  [("abc", "{F} ¿Qué gas infla la masa de T1?", "dióxido de carbono", "monóxido de carbono", "metano", "La fermentación forma dióxido de carbono."),
   ("abc", "{F} ¿Qué transforman las bacterias en T2?", "el etanol en ácido acético", "el azúcar en plástico", "el gas en agua", "La nota T2 describe esa transformación de las bacterias."),
   ("abc", "{F} ¿Qué dos tipos de compuestos forman los ésteres de T3?", "ácidos y alcoholes", "plásticos y gases", "sales y agua", "La ficha lo dice así en la nota T3."),
   ("abc", "{F} ¿Cómo se forma el polietileno de T4?", "por la unión de muchas moléculas de etileno", "por la fermentación de azúcares", "por la combustión del gas", "El polímero se forma al unirse los monómeros."),
   ("=", "{F} Otro lote tiene 20 bolsas de 15 g cada una. ¿Cuántos gramos de plástico usa?", "20*15", "Se multiplica el número de bolsas por la masa de cada una.", " g"),
   ("=", "{F} Si otro lote usa 150 g de plástico para bolsas de 15 g, ¿cuántas bolsas son?", "150/15", "Se divide la masa total por la masa de cada bolsa.", " bolsas"),
   ("abc", "{F} ¿Cuál de estos productos se forma gracias a seres vivos y no solo a la industria?", "el pan fermentado", "la bolsa plástica", "el gas licuado", "Las levaduras fermentan la masa del pan."),
   ("abc", "{F} Una persona dice que el gas licuado lo hacen las bacterias. ¿Qué dice la ficha?", "Se obtiene del gas natural y del petróleo", "Lo hacen las levaduras", "Se forma en la masa de pan", "T5 indica el origen del gas licuado."),
   ("abc", "{F} ¿Qué molécula une la cadena larga de la bolsa T4?", "el etileno", "el agua", "el oxígeno", "El polietileno se forma a partir del etileno."),
   ("abc", "{F} ¿Qué ocurre con los átomos del azúcar en T1?", "se reorganizan en dióxido de carbono y etanol", "desaparecen", "se convierten solo en energía", "La conservación explica que los átomos se mantengan."),
   ("abc", "Un panadero de ejemplo dice que sin levadura la masa no «sube». ¿Qué explicación con la ficha es correcta?", "Sin levadura no se forma el dióxido de carbono que infla la masa", "Sin levadura no hay agua", "Sin levadura no hay harina", "El gas viene de la fermentación."),
   ("abc", "{F} ¿Qué diferencia hay entre T6 y T4 en su origen?", "T6 la producen plantas y T4 se fabrica en la industria", "T6 sale del petróleo y T4 de las plantas", "los dos son iguales", "El azúcar lo forman plantas; el plástico, la industria."),
   ("abc", "{F} Para una explicación completa del vinagre T2, ¿qué falta si solo se dice «es ácido acético»?", "de qué parte y qué proceso lo forma", "su precio", "el nombre de la bacteria", "Falta explicar el origen y el proceso.")],
  ("abc", "Una junta de vecinos de ejemplo quiere explicar en un afiche cómo se forma el vinagre. ¿Cuál es la explicación más completa?", "Parte del azúcar; las levaduras forman alcohol y unas bacterias lo transforman en ácido acético", "El vinagre se compra en el almacén", "El vinagre es un líquido ácido", "Incluye de qué parte, proceso y qué se obtiene."),
  [("En Ciencias Naturales: ¿qué es una materia prima?", "La sustancia de la que parte la fabricación de otra", "Por ejemplo, el etileno para el polietileno."),
   ("¿Qué gas forma la fermentación en la masa del pan?", "Dióxido de carbono", "El gas formado infla la masa y la hace subir."),
   ("¿Cuánto es 8 x 15?", "120", "Es la masa de plástico de un lote de 8 bolsas de 15 g.")],
  ("Elige un producto de la ficha y escribe un texto de cuatro líneas para una persona de tu comunidad: de qué parte, qué proceso lo forma, qué se obtiene y qué se conserva. Incluye una comparación con otro producto.",
   "Pan: parte de azúcares y masa. Las levaduras los fermentan. Se obtiene dióxido de carbono, que infla la masa, y un poco de alcohol. Los átomos se conservan. Es distinto del plástico, que se forma por unión de monómeros.",
   ["responde las cuatro preguntas", "usa vocabulario de la clase", "compara con otro producto"],
   ["La explicación es completa.", "Usa los datos de la ficha.", "La comparación es válida."],
   "Si omite el proceso, pregunta «¿cómo se transforma?»."),
  "Explica a otra persona cómo se infla la masa del pan.",
  "Cuenta cuántos objetos de plástico hay en tu cocina y clasifícalos según para qué se usan.")

# ====================================================== clase 6
F = ("Ficha 6 (explicaciones de ejemplo escritas por tres personas; nombres inventados). Pregunta: ¿cómo se forma el etanol en la fermentación? "
     "Ana: «La glucosa, C6H12O6, se transforma por la acción de las levaduras en 2 etanol, 2 C2H5OH, y 2 dióxido de carbono, 2 CO2. Los átomos se reorganizan: hay 6 carbonos a cada lado.» "
     "Beatriz: «La glucosa desaparece y el etanol se crea de la nada.» "
     "Carla: «El carbono del etanol, C2H5OH, forma cinco enlaces porque tiene dos carbonos y seis hidrógenos.» "
     "Pauta de evaluación: 1) dice de qué parte; 2) dice el proceso; 3) dice qué se obtiene; 4) cumple la conservación de los átomos; 5) respeta las reglas de enlaces (carbono 4, hidrógeno 1, oxígeno 2).")
K(O, 6, F,
  "Hoy revisaré lo logrado: evaluaré explicaciones sobre cómo se forman compuestos orgánicos con una pauta, corregiré errores y decidiré cómo seguir.",
  ["Explicar bien cómo se forma un compuesto es una destreza que se puede revisar con una pauta. Se pregunta si la explicación dice de qué parte, qué proceso ocurre y qué se obtiene, y si respeta dos reglas: los átomos se conservan y cada átomo forma el número de enlaces que le corresponde.",
   "Con la pauta se detectan errores. Si alguien dice que algo «desaparece» o «se crea de la nada», rompe la conservación de los átomos. Si dice que un carbono forma cinco enlaces, rompe la regla de los enlaces. Para corregir, se vuelven a contar los átomos y se explica el error sin burlarse de nadie.",
   "Además se mira lo que falta: ¿hay una ecuación?, ¿se comprobó el balance?, ¿se pueden comparar dos explicaciones? Al terminar, cada persona decide qué quiere repasar. Las explicaciones de la ficha son ejemplos inventados; en este cuaderno no se hace ninguna reacción."],
  [("pauta", "lista de criterios para revisar un trabajo"), ("conservación de los átomos", "hay los mismos átomos antes y después de la reacción"), ("corregir", "cambiar un error por una versión correcta"), ("retroalimentación", "comentario que ayuda a mejorar un trabajo")],
  [("Aplicar la pauta", "{F} ¿Cuál de las tres explicaciones cumple los cinco criterios?",
    ["Reviso cada criterio.", "Solo la de Ana dice de qué parte, el proceso, qué se obtiene y los átomos."], "La de Ana"),
   ("Corregir un error", "{F} ¿Qué error tiene la explicación de Carla?",
    ["El carbono forma cuatro enlaces.", "Ella dice que forma cinco."], "Dice que un carbono forma cinco enlaces: debe ser cuatro")],
  [("Corregir una explicación solo diciendo «está mal».", "No ayuda a mejorar.", "Señala el criterio que falla y propone cómo arreglarlo."),
   ("Aceptar una explicación porque suena segura.", "Puede romper la conservación de los átomos.", "Compruébala con la pauta y con el conteo de átomos.")],
  [("abc", "{F} Beatriz dice que la glucosa «desaparece» y que el etanol «se crea de la nada». ¿Qué criterio de la pauta rompe esa frase?", "el 4, la conservación de los átomos", "el 5, las reglas de enlaces", "ninguno", "Si algo desaparece o se crea de la nada, los átomos no se conservan."),
   ("abc", "{F} ¿Cuántos carbonos hay en 3 C2H5OH?", "6", "3", "9", "Cada molécula tiene 2 carbonos y hay 3 moléculas."),
   ("=", "{F} ¿Cuántos átomos de carbono hay a la derecha, en 2 C2H5OH y 2 CO2?", "2*2+2*1", "4 carbonos del etanol más 2 del dióxido.", " átomos"),
   ("abc", "{F} ¿Se cumple la conservación de los carbonos en la explicación de Ana?", "Sí, 6 antes y 6 después", "No, hay más después", "No se puede saber", "6 carbonos en la glucosa y 4 + 2 en los productos."),
   ("abc", "{F} ¿Cuántos enlaces forma cada átomo de carbono, según la pauta?", "4", "5", "2", "La pauta pide respetar carbono 4."),
   ("abc", "{F} ¿Qué proceso nombra Ana en su explicación?", "la acción de las levaduras, la fermentación", "la combustión", "la polimerización", "Ana habla de levaduras que transforman la glucosa."),
   ("abc", "{F} Para ayudar a Beatriz, ¿qué retroalimentación es respetuosa y útil?", "«Revisa que los átomos de la glucosa siguen existiendo en los productos»", "«Eso está muy mal»", "«Mejor no escribas»", "Señala el criterio y propone un paso para mejorar."),
   ("abc", "{F} Si Carla cuenta bien, ¿cuántos átomos de hidrógeno tiene la molécula de etanol C2H5OH?", "6", "5", "2", "5 en C2H5 y 1 en OH."),
   ("abc", "{F} Además de respetar la conservación, ¿qué falta en la explicación de Beatriz?", "decir por qué proceso se forma el etanol, la acción de las levaduras", "agregar un color", "agregar su nombre", "Ana sí nombra el proceso y la de Beatriz no lo explica."),
   ("abc", "Dos personas discrepan sobre la explicación de Ana. ¿Cuál es la mejor forma de resolverlo?", "contar los átomos y revisar la pauta juntas", "votar sin revisar", "dar la razón a quien hable más fuerte", "Los datos y la pauta permiten decidir con respeto."),
   ("=", "{F} Si se fermentan 3 moléculas de glucosa, 3 C6H12O6, ¿cuántos átomos de carbono hay en los reactantes?", "3*6", "Cada glucosa tiene 6 carbonos y hay 3 moléculas.", " átomos"),
   ("abc", "{F} ¿Qué criterio de la pauta no cumple Carla?", "las reglas de enlaces", "decir de qué parte", "nombrar el etanol", "Dice que el carbono forma cinco enlaces."),
   ("abc", "{F} ¿Qué explicación sería la más completa si se agrega la conservación del oxígeno?", "la de Ana, con 6 oxígenos antes y 2 + 4 después", "la de Beatriz", "la de Carla", "2 etanoles aportan 2 oxígenos y 2 CO2 aportan 4: suman 6.")],
  ("abc", "Un grupo de una cooperativa de ejemplo debe elegir entre tres afiches sobre cómo se forma el vinagre. ¿Qué pauta usa para elegir?", "de qué parte, qué proceso, qué se obtiene y si se conservan los átomos", "cuál es más colorido", "cuál es más corto", "Esa pauta garantiza una explicación correcta."),
  [("En Ciencias Naturales: ¿qué es una pauta de evaluación?", "Una lista de criterios para revisar un trabajo", "Permite dar una retroalimentación clara y ordenada."),
   ("¿Cuántos enlaces forma el carbono?", "4", "Es una de las reglas de la pauta."),
   ("¿Qué reglas revisa la pauta sobre los átomos?", "Que se conserven y que respeten sus enlaces", "Así se detectan errores en las explicaciones.")],
  ("Escribe tu propia explicación de cómo se forma un compuesto de la clase 5 (pan, vinagre, bolsa o aroma de fruta) y evalúala con los cinco criterios de la pauta. Marca qué cumple y qué mejorarías, y escribe una retroalimentación para otra persona.",
   "Explicación: el vinagre parte de azúcares; las levaduras forman alcohol y bacterias lo transforman en ácido acético; los átomos se reorganizan. Cumple 1 a 4. Mejoraría agregando la ecuación del alcohol. Retroalimentación: buena secuencia; agrega la ecuación.",
   ["escribe una explicación con proceso", "la evalúa con la pauta", "da una retroalimentación respetuosa"],
   ["La explicación respeta la conservación.", "La autoevaluación es honesta.", "La retroalimentación propone una mejora."],
   "Si omite un criterio, pide que lo revise en voz alta."),
  "Revisa una explicación tuya anterior con la pauta.",
  "Escribe una pauta de tres criterios para revisar un afiche científico.")

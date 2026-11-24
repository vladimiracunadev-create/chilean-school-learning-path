"""Ciencias Naturales EPJA Media N1, módulo 2, desempeño OAD-05: investigaciones sobre reacciones químicas del hogar y las leyes de conservación de la materia. Todo en papel; datos de ejemplo; balances de masa con números exactos."""
from __future__ import annotations

from epja_cnat_nm1_b_common import K

O = "EPJA-CNAT-NM1-OAD-05"

# ====================================================== clase 1
F = ("Ficha 1 (situaciones del hogar, de ejemplo). S1: un clavo de hierro olvidado a la intemperie se cubre de una capa rojiza. S2: un cubo de hielo se derrite en un vaso. "
     "S3: la clara de un huevo crudo se vuelve blanca y firme al cocinarse. S4: el azúcar se disuelve en el té. S5: la masa de pan reposa y sube, y huele distinto. "
     "S6: una hoja de papel se rompe en trozos. S7: una manzana cortada se pone café. S8: la leche olvidada fuera del refrigerador se agria y huele ácida. "
     "S9: la ropa mojada se seca al aire.")
K(O, 1, F,
  "Hoy partiré de lo que ya veo en mi casa para distinguir un cambio físico de un cambio químico y formular una pregunta que se pueda investigar.",
  ["Tú ya observas cambios todos los días: la comida que se cocina, el fierro que se oxida, la masa que sube. Los científicos los separan en dos grupos. En un cambio físico la sustancia sigue siendo la misma; solo cambia su forma, su estado o su tamaño, como el hielo que se derrite.",
   "En un cambio químico aparece al menos una sustancia nueva, con propiedades distintas de las de partida. A ese proceso se le llama reacción química. Algunas señales ayudan a sospecharlo: un color nuevo, un olor nuevo, burbujas de un gas que antes no estaba, o un sólido que antes no había.",
   "Ojo con las señales: ninguna es una prueba por sí sola. Al hervir agua salen burbujas y el agua sigue siendo agua. Tampoco basta preguntar si el cambio se puede revertir. Lo decisivo es si hay una sustancia nueva. Aquí trabajamos solo con situaciones escritas, sin hacer experimentos."],
  [("cambio físico", "cambio en que la sustancia sigue siendo la misma"), ("cambio químico", "cambio en que se forman sustancias nuevas"), ("reacción química", "proceso en que unas sustancias se transforman en otras"), ("pregunta investigable", "pregunta que se responde observando o midiendo")],
  [("Clasificar un cambio", "{F} ¿La situación S2, el hielo que se derrite, es un cambio físico o químico?",
    ["Pregunto si aparece una sustancia nueva.", "El hielo derretido sigue siendo agua: solo cambió de estado."], "Es un cambio físico"),
   ("Usar las señales con cuidado", "{F} En S1 el clavo se cubre de una capa rojiza. ¿Qué indica?",
    ["El color rojizo es distinto del gris del fierro.", "Esa capa es un sólido nuevo que antes no estaba: el óxido."], "Un cambio químico, porque se formó una sustancia nueva")],
  [("Pensar que todo lo que no se puede devolver a su estado inicial es químico.", "Un papel roto tampoco se vuelve a unir, y sigue siendo papel.", "Pregunta siempre si hay una sustancia nueva, no si se puede revertir."),
   ("Creer que todas las burbujas son una reacción química.", "Al hervir, el agua forma burbujas de vapor, pero sigue siendo agua.", "Comprueba si el gas o la burbuja es una sustancia distinta de la de partida.")],
  [("abc", "{F} ¿Cuál de estas situaciones es un cambio físico?", "S2, el hielo que se derrite", "S3, el huevo que se cocina", "S1, el clavo que se oxida", "El hielo sigue siendo agua: cambia de estado sin formar sustancia nueva."),
   ("abc", "Una reacción química es un proceso en que", "unas sustancias se transforman en otras nuevas", "una sustancia cambia de tamaño y sigue igual", "dos sustancias se mezclan sin cambiar", "En una reacción se forman sustancias con propiedades nuevas."),
   ("ab", "{F} En S7 la manzana cortada se pone café. ¿Qué señal sugiere un cambio químico?", "el color nuevo", "el tamaño nuevo", "Un color nuevo que se mantiene sugiere una sustancia nueva en la fruta."),
   ("abc", "{F} ¿Por qué S4, el azúcar en el té, se considera un cambio físico?", "El azúcar se reparte en el agua pero sigue siendo azúcar", "Porque el té está caliente", "Porque el azúcar es blanca", "Disolver reparte las partículas sin formar una sustancia nueva."),
   ("abc", "{F} Alguien dice: «el papel roto de S6 no se puede volver a unir, así que es químico». ¿Qué respondes?", "Sigue siendo papel: la irreversibilidad no basta para decidir", "Tiene razón, todo lo irreversible es químico", "El papel roto se vuelve otra sustancia", "El criterio decisivo es la sustancia nueva, no la dificultad de volver atrás."),
   ("abc", "{F} ¿Cuántas de las situaciones S1, S3, S5, S7 y S8 son cambios químicos?", "las cinco", "solo tres", "solo dos", "En todas aparece un material, olor o color nuevo que antes no estaba."),
   ("=", "{F} La ficha tiene 9 situaciones y 5 son cambios químicos. ¿Cuántas son cambios físicos?", "9-5", "Se restan las químicas del total: quedan S2, S4, S6 y S9.", " situaciones"),
   ("abc", "Una persona cuelga ropa mojada y al rato está seca. ¿Qué tipo de cambio ocurre con el agua?", "físico: el agua pasa a vapor y sigue siendo agua", "químico: el agua se vuelve otra sustancia", "ninguno, porque el agua desaparece", "Evaporar es cambiar de estado sin formar sustancia nueva."),
   ("abc", "¿Cuál es una pregunta investigable sobre el clavo de S1?", "«¿Cuántos días tarda en aparecer óxido en un clavo dejado al aire?»", "«¿Es bonito el color del óxido?»", "«¿Es mejor el fierro que la madera?»", "Se puede responder contando días con una medición repetible."),
   ("abc", "Dos vecinas discuten sobre S3, el huevo cocido. Una dice que la clara cocida es un material nuevo que no vuelve a ser clara cruda. ¿Qué tipo de cambio apoya su argumento?", "químico", "físico", "ninguno", "Un material nuevo que no se recupera indica una reacción."),
   ("abc", "{F} ¿Qué señales se mencionan en S5, la masa de pan?", "olor distinto y masa que sube por un gas formado", "solo un cambio de tamaño por el calor", "solo un cambio de estado", "El olor nuevo y el aumento de volumen sugieren sustancias nuevas, entre ellas un gas."),
   ("abc", "Se afirma: «si hay burbujas, siempre hay reacción química». ¿Qué ejemplo lo contradice?", "El agua que hierve forma burbujas de vapor y sigue siendo agua", "El hielo que se derrite no forma burbujas", "El clavo que se oxida no forma burbujas", "Las burbujas de vapor no son una sustancia nueva."),
   ("abc", "En una panadería de ejemplo, la masa A reposa 1 hora y la B reposa 5 horas. ¿Qué pregunta investigable compara ambos casos?", "«¿Cómo cambia el volumen de la masa según las horas de reposo?»", "«¿Cuál masa es más rica?»", "«¿Es bueno que la masa suba?»", "Define qué se mide, el volumen, y qué se cambia, las horas.")],
  ("abc", "Una persona tuesta una rebanada de pan: se oscurece, cambia su olor y ya no vuelve a ser blanda y clara. ¿Qué concluye?", "Hubo un cambio químico, porque aparecieron un color y un olor nuevos", "Fue solo un cambio de estado", "No se puede saber nada", "Color y olor nuevos que no se revierten indican una sustancia nueva."),
  [("En Ciencias Naturales: ¿qué es un cambio químico?", "Un cambio en que se forman sustancias nuevas", "La reacción química produce materiales con propiedades distintas."),
   ("¿El hielo que se derrite es un cambio físico o químico?", "Físico", "El agua cambia de estado pero sigue siendo agua."),
   ("Nombra una señal que sugiere un cambio químico.", "Un color nuevo, un olor nuevo, un gas nuevo o un sólido nuevo", "Son pistas que se confirman viendo si hay una sustancia nueva.")],
  ("Elige una de estas situaciones de tu cocina o de la ficha: A) la fruta que se pone café; B) el pan que se tuesta; C) la ropa que se seca. Clasifícala como cambio físico o químico, nombra la señal que usaste y escribe una pregunta investigable sobre ella, con lo que medirías y su unidad.",
   "Elijo la fruta (A). Es un cambio químico, porque aparece un color café nuevo. Pregunta: ¿cuántos minutos tarda una rodaja de manzana en ponerse café al aire? Mediría minutos.",
   ["clasifica el cambio", "nombra la señal o el criterio de la sustancia nueva", "formula una pregunta que se pueda medir con unidad"],
   ["Clasificación justificada con una señal.", "Pregunta medible y con unidad.", "No usa productos peligrosos ni experimentos riesgosos."],
   "Si la clasificación no tiene razón, pregunta «¿qué sustancia nueva aparece?». Si la pregunta es de gusto, pide qué contarías o medirías."),
  "Escribe tres cambios que veas en tu casa esta semana y clasifícalos con su señal.",
  "Elige un cambio que clasificaste como físico y explica por qué no es químico.")

# ====================================================== clase 2
F = ("Ficha 2 (reacciones en palabras y fórmulas, de ejemplo). R1: hierro + oxígeno → óxido de hierro. R2: metano + oxígeno → dióxido de carbono + agua. "
     "R3: hidrógeno + oxígeno → agua. R4: bicarbonato + ácido del vinagre → sal + agua + dióxido de carbono. "
     "Fórmulas: agua H2O (2 átomos de hidrógeno y 1 de oxígeno); dióxido de carbono CO2 (1 de carbono y 2 de oxígeno); oxígeno O2 (2 átomos de oxígeno); hidrógeno H2 (2 átomos de hidrógeno); metano CH4 (1 de carbono y 4 de hidrógeno). "
     "En «3 H2O» el número 3 es el de moléculas; el número pequeño de la fórmula es el de átomos.")
K(O, 2, F,
  "Hoy reconoceré el vocabulario de las reacciones químicas: reactantes, productos, átomos, moléculas y la idea de reorganización.",
  ["Toda la materia está hecha de átomos. Un átomo es la partícula básica de un elemento, como el hidrógeno, el oxígeno o el carbono. Cuando varios átomos se unen forman una molécula: el agua, H2O, tiene dos átomos de hidrógeno y uno de oxígeno.",
   "Una reacción química se puede escribir como una ecuación: a la izquierda están los reactantes, las sustancias que se transforman; a la derecha, los productos, las sustancias nuevas. La flecha se lee «produce». Los reactantes no desaparecen: sus átomos se reorganizan y forman otras uniones.",
   "El científico francés Antoine Lavoisier, en el siglo XVIII, mostró con mediciones cuidadosas que en una reacción la masa total se mantiene. Hoy se dice: la materia no se crea ni se destruye, solo cambia de forma. Eso se llama ley de conservación de la masa."],
  [("reactante", "sustancia que se transforma en una reacción"), ("producto", "sustancia nueva que se forma en una reacción"), ("átomo", "partícula básica de un elemento"), ("conservación de la masa", "la masa total antes y después de una reacción es la misma")],
  [("Leer una ecuación", "{F} En R2, ¿cuáles son los reactantes y cuáles los productos?",
    ["Lo que está antes de la flecha son los reactantes.", "Lo que está después son los productos."], "Reactantes: metano y oxígeno; productos: dióxido de carbono y agua"),
   ("Contar átomos de una fórmula", "{F} ¿Cuántos átomos de hidrógeno hay en 3 moléculas de agua, 3 H2O?",
    ["Cada H2O tiene 2 átomos de hidrógeno.", "Se multiplica 3 x 2."], "6 átomos de hidrógeno")],
  [("Creer que los reactantes «desaparecen» en la reacción.", "Sus átomos siguen existiendo, reorganizados en los productos.", "Di «se reorganizan» y no «desaparecen»."),
   ("Confundir el número pequeño de la fórmula con el número de moléculas.", "En H2O el 2 es de átomos de hidrógeno; las moléculas se indican con el número grande delante.", "Lee el número delante para moléculas y el pequeño para átomos.")],
  [("abc", "En una ecuación química, los reactantes se escriben", "antes de la flecha", "después de la flecha", "debajo de la flecha", "Los reactantes son los que se transforman y van a la izquierda."),
   ("abc", "{F} ¿Cuál es el producto de R1, hierro + oxígeno?", "óxido de hierro", "hidrógeno", "metano", "El óxido de hierro es la sustancia nueva que se forma."),
   ("ab", "Un átomo es", "la partícula básica de un elemento", "una mezcla de sustancias", "Los átomos son las partículas con que se forman las moléculas."),
   ("abc", "{F} ¿Cuántos átomos tiene una molécula de CO2?", "3", "2", "1", "Tiene 1 átomo de carbono y 2 de oxígeno, en total 3."),
   ("abc", "{F} ¿Qué dos átomos distintos forman una molécula de agua, H2O?", "hidrógeno y oxígeno", "carbono y oxígeno", "hidrógeno y carbono", "La fórmula H2O indica hidrógeno y oxígeno."),
   ("=", "{F} ¿Cuántos átomos de oxígeno hay en 4 moléculas de oxígeno, 4 O2?", "4*2", "Cada molécula O2 tiene 2 átomos de oxígeno.", " átomos"),
   ("=", "{F} ¿Cuántos átomos de hidrógeno hay en 2 moléculas de metano, 2 CH4?", "2*4", "Cada CH4 tiene 4 átomos de hidrógeno.", " átomos"),
   ("abc", "{F} En R4, ¿cuál de estas sustancias es un reactante?", "el bicarbonato", "la sal", "el dióxido de carbono", "El bicarbonato está antes de la flecha, así que se transforma."),
   ("abc", "Según Lavoisier, en una reacción química la masa total", "se mantiene igual", "aumenta siempre", "disminuye siempre", "Medir antes y después mostró que la masa total se conserva."),
   ("abc", "Una persona dice: «Al quemar gas, el gas desaparece». ¿Qué respuesta usa bien el modelo de átomos?", "Los átomos del gas se reorganizan en productos nuevos", "Los átomos se destruyen", "Los átomos se convierten en energía y nada más", "La reorganización de átomos explica que la materia no se destruya."),
   ("abc", "{F} En R3, ¿cuántos átomos de hidrógeno tiene 1 molécula de H2 (hidrógeno)?", "2", "1", "3", "El número pequeño 2 de H2 indica dos átomos."),
   ("abc", "{F} Se lee «2 H2O». ¿Qué significa el número 2 delante?", "hay dos moléculas de agua", "cada molécula tiene dos átomos de oxígeno", "hay dos átomos de hidrógeno en total", "El número delante cuenta moléculas; el pequeño cuenta átomos."),
   ("abc", "Se afirma: «en R2 el oxígeno ya no existe porque no se escribe en los productos». ¿Qué es lo más preciso?", "Sus átomos están en el dióxido de carbono y en el agua", "Es cierto, el oxígeno se destruye", "Se transforma en el metano", "Los átomos de oxígeno se reparten en los productos.")],
  ("abc", "Un técnico de una cocina de ejemplo lee en una etiqueta: «el gas natural, al quemarse con oxígeno, forma dióxido de carbono y agua». ¿Cuáles son los reactantes?", "el gas natural y el oxígeno", "el dióxido de carbono y el agua", "solo el agua", "Lo que se consume antes de la reacción son los reactantes."),
  [("En Ciencias Naturales: ¿qué es un producto en una reacción?", "La sustancia nueva que se forma", "Está después de la flecha en la ecuación."),
   ("¿Cuántos átomos de oxígeno tiene una molécula de CO2?", "2", "El número pequeño 2 indica los átomos de oxígeno."),
   ("En una reacción del hogar: ¿qué dice la ley de conservación de la masa?", "La masa total antes y después de una reacción es la misma", "Los átomos se reorganizan, no se crean ni se destruyen.")],
  ("Elige R1, R2 o R3 de la ficha. Escribe sus reactantes y productos, cuenta los átomos de una de sus fórmulas y explica con tus palabras por qué los reactantes no «desaparecen».",
   "R3: reactantes hidrógeno y oxígeno, producto agua. En H2O hay 2 átomos de hidrógeno y 1 de oxígeno. No desaparecen: sus átomos se juntan de otra forma y forman el agua.",
   ["separa reactantes y productos", "cuenta átomos de una fórmula", "explica con la idea de reorganización"],
   ["Usa bien las palabras reactante y producto.", "El conteo es correcto.", "Explica con átomos reorganizados."],
   "Si dice que algo desaparece, pregunta «¿dónde están sus átomos?»."),
  "Escribe con tus palabras qué significan átomo, molécula, reactante y producto.",
  "Inventa una ecuación en palabras para una situación de tu casa y marca sus reactantes y productos.")

# ====================================================== clase 3
F = ("Ficha 3 (balances de masa, de ejemplo, en gramos; las masas de los átomos están simplificadas en unidades enteras). "
     "B1: carbono + oxígeno → dióxido de carbono: 12 g + 32 g → 44 g. "
     "B2: hidrógeno + oxígeno → agua: 4 g + 32 g → 36 g. "
     "B3: hierro + oxígeno → óxido de hierro: 224 g + 96 g → 320 g. "
     "B4 (bolsa cerrada con una reacción que forma gas): masa antes 150 g; masa después 150 g. "
     "B5 (vaso abierto con la misma reacción): masa antes 150 g; masa después 146 g.")
K(O, 3, F,
  "Hoy veré paso a paso cómo se comprueba la conservación de la masa: sumo las masas de los reactantes, sumo las de los productos y las comparo.",
  ["Para comprobar la ley de conservación de la masa se hace un balance: se suman las masas de todos los reactantes, se suman las de todos los productos y se comparan. Si la reacción ocurre en un sistema cerrado, del que no sale ni entra materia, las dos sumas son iguales.",
   "Ejemplo: 12 g de carbono reaccionan con 32 g de oxígeno y forman 44 g de dióxido de carbono. Antes hay 12 + 32 = 44 g y después hay 44 g. La masa se conservó. También puedes contar átomos: en los dos lados hay los mismos átomos de cada elemento, solo que unidos distinto.",
   "Si la masa parece cambiar, no hay magia: algo entró o salió del sistema. Un vaso abierto en que se forma un gas pierde masa porque el gas escapa. Un trozo de fierro que se oxida al aire gana masa porque toma oxígeno del aire. Siempre busca por dónde entró o salió la materia. En la vida real no se cierra herméticamente un envase donde se forma gas, porque podría reventar; aquí solo se leen datos."],
  [("balance de masa", "comparación de la masa de reactantes y de productos"), ("sistema cerrado", "sistema del que no entra ni sale materia"), ("sistema abierto", "sistema por el que puede entrar o salir materia"), ("gramo (g)", "unidad de masa")],
  [("Hacer un balance", "{F} En B2, ¿se conserva la masa?",
    ["Reactantes: 4 + 32 = 36 g.", "Producto: 36 g. Son iguales."], "Sí, porque 36 g = 36 g"),
   ("Explicar una pérdida de masa", "{F} En B5 la masa baja de 150 g a 146 g. ¿Por qué?",
    ["El vaso está abierto.", "Se formó un gas que escapó llevándose 4 g."], "Porque 4 g de gas salieron del sistema abierto")],
  [("Pensar que si la masa baja, la materia se destruyó.", "La materia salió del sistema, por ejemplo como gas, pero no se destruyó.", "Pregunta siempre por dónde pudo salir o entrar la materia."),
   ("Sumar solo un reactante con el producto.", "El balance compara TODOS los reactantes con TODOS los productos.", "Suma primero todos los reactantes, luego todos los productos y compara.")],
  [("=", "{F} En B1, ¿cuántos gramos suman los reactantes (12 g y 32 g)?", "12+32", "Se suman las masas de todos los reactantes.", " g"),
   ("abc", "{F} En B1, ¿se conserva la masa?", "Sí, porque 44 g = 44 g", "No, porque hay más reactantes que productos", "No se puede saber", "La suma de reactantes, 44 g, es igual a la del producto."),
   ("abc", "En un balance de masa se comparan", "la suma de los reactantes con la suma de los productos", "un reactante con un producto", "solo los productos entre sí", "La ley habla de la masa total en cada lado."),
   ("=", "{F} En B3, ¿cuántos gramos suman los reactantes (224 g y 96 g)?", "224+96", "Se suman las masas de hierro y de oxígeno.", " g"),
   ("abc", "{F} En B3, ¿cuánto óxido de hierro se forma?", "320 g", "128 g", "224 g", "Por conservación, el producto tiene la masa de los reactantes: 320 g."),
   ("=", "{F} En B2 se forman 36 g de agua con 32 g de oxígeno. ¿Cuántos gramos de hidrógeno reaccionaron?", "36-32", "La masa del hidrógeno es la del producto menos la del oxígeno.", " g"),
   ("abc", "{F} En B4, bolsa cerrada, la masa antes y después es 150 g. ¿Qué indica?", "Que el gas formado quedó dentro y la masa se conservó", "Que no hubo reacción", "Que la ley falla en bolsas", "Si nada sale ni entra, la masa total se mantiene."),
   ("=", "En un vaso abierto de ejemplo, la masa antes de la reacción es 210 g y después es 205 g. ¿Cuántos gramos de gas escaparon?", "210-205", "La masa perdida es la diferencia entre antes y después.", " g"),
   ("abc", "{F} ¿Qué diferencia de montaje explica que en B4 la masa se conserve y en B5 baje?", "B4 es un sistema cerrado y B5 uno abierto", "B4 usa menos masa", "B5 tiene más reactantes", "El gas solo pudo escapar en el vaso abierto."),
   ("abc", "Un clavo de fierro se oxida al aire y su masa sube un poco. ¿Qué explicación respeta la conservación de la masa?", "Tomó oxígeno del aire y lo incorporó al óxido", "Se creó materia nueva", "El fierro se hizo más pesado solo", "La masa que se gana viene del oxígeno del aire."),
   ("abc", "{F} En B3, ¿cuántos gramos de oxígeno se necesitan si se forman 320 g de óxido con 224 g de hierro?", "96", "224", "544", "La masa de oxígeno es 320 menos 224, es decir 96 g."),
   ("abc", "Una persona de ejemplo dice: «en B5 la ley no se cumple porque faltan 4 g». ¿Qué respondes?", "Sí se cumple: los 4 g salieron como gas del vaso abierto", "Tiene razón, la ley falla", "Los 4 g se destruyeron", "La ley se refiere al sistema completo, y el gas escapó."),
   ("abc", "Con datos de ejemplo, se quiere pesar todo el gas que forma una reacción. ¿Qué montaje lo permite?", "uno cerrado, donde el gas no escapa", "uno abierto, donde el gas sale", "da lo mismo", "En un sistema cerrado se puede pesar todo el gas formado.")],
  ("abc", "En un taller de ejemplo se anota: «antes de la reacción, 200 g; después, 200 g, con el frasco bien tapado». ¿Qué se puede afirmar?", "La masa se conservó en un sistema cerrado", "Se destruyó materia", "No hubo reacción", "Igual masa antes y después en un sistema cerrado respeta la ley."),
  [("En Ciencias Naturales: ¿qué es un sistema cerrado?", "Uno del que no entra ni sale materia", "Permite comprobar la conservación de la masa."),
   ("En B1 los reactantes suman 12 g + 32 g. ¿Cuántos gramos?", "44", "Se suman las masas de los reactantes: 44 g."),
   ("Si en un vaso abierto la masa baja, ¿qué pudo pasar?", "Salió un gas del sistema", "La materia sale del vaso, no se destruye.")],
  ("Con la ficha 3, elige B3 o B5. Escribe el balance paso a paso: las sumas de reactantes y de productos, si se conserva o no la masa y, si baja o sube, por dónde pudo salir o entrar la materia.",
   "B3: reactantes 224 + 96 = 320 g; producto 320 g. Se conserva. Si el clavo gana masa al aire, el oxígeno viene del aire.",
   ["suma reactantes y productos", "compara los dos lados", "explica la diferencia con entrada o salida de materia"],
   ["Los cálculos son correctos.", "Concluye sobre la conservación.", "Menciona sistema abierto o cerrado."],
   "Si dice que la materia se destruyó, pregunta «¿por dónde pudo salir?»."),
  "Calcula otros dos balances de masa inventados, uno que se conserve y uno con pérdida de gas.",
  "Explica con un dibujo descrito por qué la masa se conserva aunque los átomos se unan distinto.")

# ====================================================== clase 4
F = ("Ficha 4 (investigación de ejemplo; los datos son inventados). Pregunta: ¿cómo influye el líquido en el que está un clavo de fierro en el tiempo que tarda en aparecer óxido? "
     "Se usan clavos iguales, a la misma temperatura ambiente y en el mismo lugar, con 100 mL de líquido, y se mira cada día. "
     "Grupo A: clavo seco en un frasco tapado; no apareció óxido en 14 días en ninguna de las tres repeticiones. "
     "Grupo B: clavo en agua del grifo; el óxido apareció a los 6, 8 y 7 días en las tres repeticiones. "
     "Grupo C: clavo en agua con sal; el óxido apareció a los 2, 4 y 3 días en las tres repeticiones.")
K(O, 4, F,
  "Hoy practicaré con apoyo cómo se diseña y se lee una investigación: variables, repeticiones, tabla de datos y conclusión que los datos permiten.",
  ["Una investigación sencilla compara casos cambiando una sola cosa a la vez. Lo que se cambia a propósito es la variable independiente; lo que se mide para ver el efecto es la variable dependiente; y todo lo demás se mantiene igual: son las variables controladas. Así se sabe qué causó el resultado.",
   "En la ficha, el líquido cambia (seco, agua del grifo, agua con sal): es la variable independiente. Se miden los días hasta que aparece óxido: es la dependiente. Se mantienen iguales el tipo de clavo, la temperatura, el lugar y los 100 mL: son las controladas.",
   "Para que los datos sean confiables se repite cada caso varias veces y se calcula el promedio: se suman los valores y se divide por el número de repeticiones. Con el promedio de cada grupo se compara y se escribe una conclusión que diga solo lo que los datos permiten. Aquí no se hace el experimento: solo se analizan los datos de la ficha."],
  [("variable independiente", "la que se cambia a propósito"), ("variable dependiente", "la que se mide para ver el efecto"), ("variable controlada", "la que se mantiene igual en todos los casos"), ("promedio", "suma de los valores dividida por la cantidad de valores")],
  [("Identificar las variables", "{F} ¿Cuál es la variable dependiente de esta investigación?",
    ["La dependiente es lo que se mide.", "Se mide el tiempo hasta que aparece el óxido."], "Los días hasta que aparece óxido"),
   ("Calcular un promedio", "{F} ¿Cuál es el promedio de días del grupo B (6, 8 y 7)?",
    ["Se suman: 6 + 8 + 7 = 21.", "Se divide 21 entre 3 repeticiones."], "7 días")],
  [("Cambiar dos condiciones a la vez y concluir igual.", "No se puede saber cuál de los dos cambios produjo el efecto.", "Cambia una sola variable y mantén las demás iguales."),
   ("Concluir con una sola medición.", "Un dato aislado puede deberse al azar.", "Repite el caso y usa el promedio.")],
  [("abc", "La variable independiente es la que", "se cambia a propósito", "se mide al final", "se mantiene igual siempre", "Es la condición que el investigador decide variar."),
   ("abc", "{F} ¿Cuál es la variable independiente?", "el líquido en que está el clavo", "los días hasta el óxido", "el tipo de clavo", "El líquido es lo que se cambia entre grupos."),
   ("abc", "{F} ¿Cuál de estas es una variable controlada?", "la temperatura ambiente", "el líquido", "los días hasta el óxido", "La temperatura se mantiene igual en todos los grupos."),
   ("=", "{F} Promedio de días del grupo C (2, 4 y 3).", "(2+4+3)/3", "Se suman los tres valores y se divide por 3.", " días"),
   ("=", "{F} ¿Cuántos días más tardó, en promedio, el grupo B que el grupo C? (promedios 7 y 3)", "7-3", "Se restan los promedios para comparar los grupos.", " días"),
   ("abc", "{F} ¿Qué conclusión permiten los datos?", "En agua con sal el óxido apareció antes, en promedio, que en agua del grifo", "El agua con sal crea hierro nuevo", "El óxido aparece igual en los tres grupos", "Los promedios 3 y 7 muestran que con sal apareció primero."),
   ("abc", "{F} En el grupo A no apareció óxido. ¿Qué se puede decir?", "En esas condiciones secas y tapadas no apareció óxido en 14 días", "Que el fierro no se oxida nunca", "Que el frasco tapado destruye el óxido", "La conclusión se limita a lo observado: 14 días y esas condiciones."),
   ("abc", "Se cambia el líquido y también la temperatura entre grupos. ¿Qué problema tiene el diseño?", "No se sabrá cuál de los dos cambios causó el resultado", "Ninguno, mejora la comparación", "Se pierde el promedio", "Si cambian dos cosas a la vez, el efecto no se puede atribuir a una."),
   ("abc", "¿Por qué se hacen tres repeticiones por grupo?", "Para que un resultado raro pese menos y los datos sean más confiables", "Para gastar más clavos", "Para que todos los números sean iguales", "Repetir reduce el efecto del azar sobre la conclusión."),
   ("abc", "{F} Una persona dice: «la sal crea el óxido de la nada». ¿Qué respuesta respeta la conservación de la materia?", "El óxido se forma con hierro y oxígeno; la sal solo acelera el proceso", "Es cierto, la sal se convierte en óxido", "El óxido aparece sin átomos", "El óxido se forma con átomos de hierro y oxígeno ya presentes."),
   ("=", "Otro grupo D de ejemplo se repitió cinco veces: 5, 7, 6, 8 y 4 días. ¿Cuál es el promedio?", "(5+7+6+8+4)/5", "Se suman los cinco valores y se divide por 5.", " días"),
   ("abc", "Se quiere investigar si la temperatura del agua cambia el tiempo hasta el óxido. ¿Qué debe mantenerse igual?", "el tipo de clavo, el volumen de agua y el lugar", "la temperatura del agua", "el tiempo de observación solamente", "Solo la temperatura debe variar; lo demás se controla."),
   ("abc", "Un grupo concluye con «seguro que la sal funciona igual con cualquier metal». ¿Qué falla?", "Los datos solo se refieren a clavos de fierro", "Faltan más clavos de ejemplo", "No se calculó el promedio", "Una conclusión no debe ir más allá de lo investigado.")],
  ("abc", "Un taller de ejemplo quiere saber si pintar un clavo retrasa el óxido. Prueba un clavo pintado afuera y uno sin pintar adentro, bajo techo. ¿Qué falla?", "Cambian la pintura y el lugar a la vez", "Falta pintar más clavos", "Hay demasiados clavos", "Dos cambios simultáneos impiden saber cuál influyó."),
  [("En Ciencias Naturales: ¿qué es una variable controlada?", "Una que se mantiene igual en todos los casos", "Así el efecto se atribuye a la variable independiente."),
   ("¿Cuál es el promedio de 4, 6 y 8?", "6", "La suma es 18 y 18 entre 3 es 6."),
   ("¿Por qué se repiten las mediciones?", "Para tener datos más confiables", "Un valor raro pesa menos con varios.")],
  ("Diseña en papel una investigación de ejemplo: elige entre A) cómo afecta el lugar (sol o sombra) al tiempo que tarda en secarse una prenda de ejemplo, o B) cómo afecta el líquido al óxido de un clavo. Escribe la pregunta, las tres variables, cuántas repeticiones usarías y cómo registrarías los datos en una tabla.",
   "A) Pregunta: ¿cómo cambia el tiempo de secado entre sol y sombra? Independiente: lugar. Dependiente: minutos hasta secar. Controladas: mismo paño, misma cantidad de agua. Tres repeticiones y una tabla de lugar y minutos.",
   ["formula una pregunta investigable", "identifica las tres clases de variables", "propone repeticiones y una tabla de registro"],
   ["Las variables están bien identificadas.", "Solo cambia una condición.", "Incluye repeticiones y tabla."],
   "Si cambia dos condiciones, pregunta «¿cuál causó el resultado?»."),
  "Calcula el promedio de otras tres series de datos inventadas y escribe una conclusión para cada una.",
  "Explica por qué en la ficha no se puede concluir nada sobre el fierro en general.")

# ====================================================== clase 5
F = ("Ficha 5 (etiquetas y notas de ejemplo, inventadas). E1, desatascador de cañerías: «Contiene sustancias corrosivas. Use guantes y protección para los ojos. Úselo en un lugar ventilado. No lo mezcle con ningún otro producto. "
     "Si hay contacto con la piel o los ojos, siga las instrucciones de primeros auxilios del envase y consulte a un servicio de salud.» "
     "E2, cloro de uso doméstico: «No lo mezcle con amoníaco ni con vinagre ni con otros limpiadores: puede liberar gases tóxicos. Guárdelo en su envase original, lejos de otros productos.» "
     "E3, calefactor a gas: «Úselo siempre en un lugar con ventilación. Si hay olor a gas o la llama cambia, apague y pida una revisión técnica. La combustión incompleta produce monóxido de carbono, CO, un gas sin olor y tóxico.» "
     "E4, nota de cocina: «El jugo de limón sobre la fruta cortada retrasa que se ponga café al aire.»")
K(O, 5, F,
  "Hoy aplicaré lo aprendido a reacciones del hogar: leeré etiquetas de ejemplo para entender riesgos y consecuencias en la salud, y explicaré con átomos por qué ciertas advertencias existen.",
  ["En una casa ocurren reacciones químicas todo el día: la combustión del gas en una cocina, la oxidación del fierro, el dorado del pan. Muchas son útiles y otras son un riesgo si se hacen sin cuidado. Por eso los productos traen etiquetas con instrucciones y advertencias que hay que leer completas.",
   "Cuando una etiqueta dice «no mezclar con otros productos», advierte que las sustancias de dos productos pueden reaccionar entre sí. Sus átomos se reorganizan en sustancias nuevas, y algunas son gases tóxicos que no estaban en ningún envase. La materia no se destruye: se transforma en algo distinto, a veces peligroso.",
   "La combustión incompleta de un combustible, por falta de aire, produce monóxido de carbono, un gas sin olor que puede intoxicar. Por eso se ventila. En este cuaderno no se mezcla nada: solo se lee. Ante un accidente, las personas deben acudir al servicio de urgencia de salud de su zona; aquí no se dan indicaciones médicas."],
  [("etiqueta", "texto del envase con composición, usos y advertencias"), ("combustión", "reacción de un combustible con oxígeno"), ("ventilación", "entrada de aire fresco a un lugar"), ("monóxido de carbono", "gas tóxico sin olor que se forma en una combustión incompleta")],
  [("Leer una advertencia", "{F} ¿Qué pide E2 sobre mezclar el cloro con otros productos?",
    ["Busco la frase sobre mezclar.", "Dice que no se mezcle con amoníaco, vinagre ni otros limpiadores."], "No mezclarlo con ningún otro producto, porque puede liberar gases tóxicos"),
   ("Explicar con átomos", "¿Por qué una mezcla puede producir un gas que no estaba en ningún envase?",
    ["Los átomos de las sustancias se reorganizan.", "Al reorganizarse pueden formar una sustancia nueva, como un gas."], "Porque en una reacción se forman sustancias nuevas con los mismos átomos")],
  [("Mezclar dos productos «para que limpien más».", "Pueden reaccionar y formar gases tóxicos.", "Usa cada producto solo y según su etiqueta."),
   ("Creer que ventilar es opcional si no hay olor.", "El monóxido de carbono no tiene olor.", "Ventila siempre que uses un artefacto a gas, haya o no olor.")],
  [("abc", "{F} ¿Qué dice E1 sobre el lugar donde se usa?", "que sea ventilado", "que esté cerrado", "que sea muy frío", "La etiqueta pide un lugar con ventilación."),
   ("abc", "{F} ¿Qué dice E2 que puede liberar la mezcla con otros productos?", "gases tóxicos", "solo vapor de agua inofensivo", "una espuma limpiadora", "La advertencia habla de gases tóxicos."),
   ("abc", "{F} ¿Qué gas produce la combustión incompleta, según E3?", "monóxido de carbono", "hidrógeno", "nitrógeno", "E3 nombra el monóxido de carbono, CO."),
   ("abc", "{F} ¿Por qué es riesgoso el monóxido de carbono aunque no se huela?", "Porque no avisa con olor y es tóxico", "Porque huele muy fuerte", "Porque no es un gas", "Que no tenga olor impide notarlo; por eso se ventila."),
   ("abc", "Según el modelo de átomos, ¿cómo se explica que dos productos mezclados formen un gas nuevo?", "Los átomos se reorganizan en sustancias nuevas", "Los átomos de uno se destruyen", "El gas aparece sin átomos", "En toda reacción los átomos se conservan y se reordenan."),
   ("=", "Una ferretería de ejemplo guarda 24 envases del producto E1 en 3 estantes iguales, separados de los de E2. ¿Cuántos envases hay por estante?", "24/3", "Se reparten los envases en partes iguales.", " envases"),
   ("abc", "{F} ¿Qué relación tiene la nota E4 con el cambio químico de S7, la manzana cortada?", "Retrasa el cambio de color que muestra una reacción con el aire", "Convierte la fruta en una sustancia peligrosa", "No tiene relación alguna", "La nota habla de frenar el cambio de color, que es una reacción con el aire."),
   ("abc", "Una persona quiere limpiar mejor mezclando dos limpiadores. ¿Qué respuesta se apoya en la etiqueta y en la ciencia?", "No mezclarlos: pueden reaccionar y liberar gases tóxicos", "Mezclarlos, porque limpian el doble", "Mezclarlos en un lugar cerrado", "Las etiquetas advierten que la mezcla puede producir sustancias nuevas peligrosas."),
   ("abc", "{F} Al leer E3, ¿qué decisión corresponde si hay olor a gas?", "apagar el artefacto y pedir revisión técnica", "seguir usándolo", "taparlo con un paño", "La etiqueta indica apagar y pedir una revisión técnica."),
   ("abc", "Si un calefactor a gas funciona con poco aire y la combustión es incompleta, ¿qué cambia en los productos?", "se forma monóxido de carbono además de otros productos", "se forman solo agua y dióxido de carbono", "no se forma ningún producto", "Con poco oxígeno el carbono no se oxida del todo y aparece CO."),
   ("abc", "{F} Una persona sospecha una intoxicación con un limpiador. ¿Qué indica el cuaderno?", "Acudir al servicio de urgencia de salud de su zona", "Probar remedios caseros", "Esperar sin consultar", "El cuaderno no da indicaciones médicas: deriva a un servicio de salud."),
   ("abc", "Se afirma: «la reacción entre dos limpiadores crea gas de la nada». ¿Qué es más preciso?", "El gas se forma con átomos que venían en los productos", "El gas aparece sin átomos", "Es verdad, se crea materia", "La masa se conserva: el gas tiene átomos de los reactantes."),
   ("abc", "¿Qué hábito reduce riesgos en una casa con artefactos a gas?", "mantener la ventilación y seguir las instrucciones de la etiqueta", "cerrar todo para conservar el calor", "usar el artefacto sin leer el manual", "Ventilar y leer las instrucciones previene la acumulación de gases.")],
  ("abc", "Una familia de ejemplo guarda en el mismo estante bajo el lavaplatos un limpiador clorado y otro con ácido. ¿Qué decisión se apoya en las etiquetas?", "guardarlos separados y en sus envases originales", "pasarlos a una misma botella", "dejarlos mezclados para ahorrar espacio", "Las etiquetas piden envase original y no mezclarlos."),
  [("En Ciencias Naturales: ¿qué dice una etiqueta de seguridad?", "Cómo usar el producto y qué riesgos tiene", "Hay que leerla completa antes de usarlo."),
   ("¿Qué gas sin olor produce la combustión incompleta?", "Monóxido de carbono", "Por eso se ventila al usar artefactos a gas."),
   ("¿Por qué no se mezclan productos de limpieza?", "Porque pueden reaccionar y formar gases tóxicos", "Los átomos se reorganizan en sustancias nuevas.")],
  ("Elige E1, E2 o E3 de la ficha. Escribe qué riesgo advierte, qué consecuencia podría tener para la salud, cuál es la medida de prevención que se lee en la etiqueta y explica con una frase de átomos por qué ocurre la reacción. No es consejo médico: si hay un accidente, se acude a un servicio de salud.",
   "E2: advierte gases tóxicos al mezclar con otros productos. Puede afectar la respiración. Prevención: no mezclar y guardarlo en su envase. Los átomos de los dos productos se reorganizan en un gas nuevo.",
   ["nombra el riesgo de la etiqueta", "señala la medida de prevención que aparece escrita", "explica con átomos o con sustancia nueva"],
   ["Lee la etiqueta y no inventa datos.", "Explica la reacción con reorganización de átomos.", "No da consejo médico."],
   "Si inventa datos, pregunta «¿dónde lo dice la etiqueta?»."),
  "Revisa tres etiquetas reales de tu hogar sin abrir los envases y anota qué advertencia de «no mezclar» o «ventilar» traen.",
  "Explica a otra persona por qué se ventila un lugar donde hay un artefacto a gas.")

# ====================================================== clase 6
F = ("Ficha 6 (informe de ejemplo, inventado). Pregunta: ¿se destruye la materia cuando en una reacción se forma un gas? Montaje 1 (vaso abierto): masa antes 150 g, masa después 146 g. "
     "Montaje 2 (frasco tapado, con los mismos reactantes): masa antes 150 g, masa después 150 g. Se hizo un solo ensayo de cada montaje y no se anotó la temperatura. "
     "Conclusión escrita por Inés (nombre inventado): «La materia se destruye en el vaso abierto». "
     "Compuestos útiles para los seres vivos, de ejemplo: agua, H2O; dióxido de carbono, CO2, que las plantas usan; sal de mesa, formada por sodio y cloro. "
     "Dato de masa para la sección final: 24 g de carbono + 64 g de oxígeno → 88 g de dióxido de carbono.")
K(O, 6, F,
  "Hoy revisaré lo logrado: evaluaré un informe de investigación, sacaré una conclusión que los datos permiten y decidiré qué mejoraría.",
  ["Evaluar una investigación es revisar si respondió su pregunta con buenos datos. Algunas preguntas guía: ¿se cambió una sola variable?, ¿se anotaron los datos con unidades?, ¿se repitió cada caso?, ¿la conclusión dice solo lo que los datos permiten? Con ellas se detectan los puntos fuertes y los que hay que mejorar.",
   "La conservación de la masa es una buena regla para revisar conclusiones. Si en un informe «desaparece» masa, primero se pregunta si el sistema estaba abierto y por dónde pudo salir la materia. Un frasco tapado y un vaso abierto con los mismos reactantes permiten comparar y ver que el gas escapado explica la diferencia.",
   "Muchas reacciones forman compuestos útiles para la vida: el agua se forma cuando se combinan hidrógeno y oxígeno; el dióxido de carbono lo usan las plantas. Conocer las leyes que explican estos procesos ayuda a decidir con criterio y a comunicarlo con respeto. Cierra siempre diciendo qué mejorarías."],
  [("conclusión", "afirmación que responde la pregunta usando los datos"), ("confiabilidad", "grado en que los datos se repiten y se pueden creer"), ("replicable", "que otra persona puede repetirlo siguiendo los mismos pasos"), ("compuesto", "sustancia formada por átomos de distintos elementos unidos")],
  [("Evaluar una conclusión", "{F} ¿Es correcta la conclusión de Inés, «la materia se destruye en el vaso abierto»?",
    ["En el vaso abierto el gas pudo escapar.", "El frasco tapado conservó los 150 g."], "No: la masa que falta salió como gas, no se destruyó"),
   ("Proponer una mejora", "{F} ¿Qué mejora al informe daría más confiabilidad?",
    ["Hay un solo ensayo por montaje.", "Conviene repetirlos y anotar la temperatura."], "Repetir cada montaje varias veces y registrar la temperatura")],
  [("Aceptar una conclusión sin revisar los datos que la apoyan.", "Una conclusión puede ir más allá de lo que se midió.", "Contrasta cada afirmación con la tabla de datos."),
   ("Pensar que un informe con números ya es confiable.", "Sin repeticiones ni variables controladas el dato puede ser casual.", "Revisa repeticiones, variables controladas y registro.")],
  [("abc", "{F} ¿Cuántos gramos faltan en el montaje 1 después de la reacción?", "4 g", "6 g", "0 g", "150 menos 146 da 4 g que salieron del vaso."),
   ("=", "Se repitió el montaje abierto tres veces y se perdieron 4 g, 5 g y 3 g de gas. ¿Cuál es el promedio de masa perdida?", "(4+5+3)/3", "Se suman las tres pérdidas y se divide por 3.", " g"),
   ("abc", "{F} ¿Qué prueba del informe apoya que la materia no se destruyó?", "El frasco tapado terminó con 150 g, igual que al comienzo", "El vaso abierto terminó más liviano", "La conclusión de Inés", "El sistema cerrado conservó la masa total."),
   ("abc", "{F} ¿Qué debilidad tiene el informe en cuanto a confiabilidad?", "Se hizo un solo ensayo de cada montaje", "Se usaron gramos", "Se usó un frasco", "Sin repeticiones no se sabe si el resultado fue casual."),
   ("abc", "{F} ¿Qué dato falta anotar para poder replicar la investigación?", "la temperatura", "el nombre de Inés", "el color del vaso", "Sin ese dato otra persona no repite exactamente las condiciones."),
   ("abc", "¿Qué pregunta ayuda a revisar si una conclusión es válida?", "¿Se apoya en los datos de la tabla?", "¿Suena convincente?", "¿La dijo alguien seguro?", "Una conclusión válida se sostiene en los datos."),
   ("=", "{F} Si 24 g de carbono reaccionan con 64 g de oxígeno, ¿cuántos gramos de dióxido de carbono se forman?", "24+64", "La masa del producto es la suma de las masas de los reactantes.", " g"),
   ("abc", "{F} ¿Cuántos átomos de oxígeno tiene 1 molécula de CO2?", "2", "1", "3", "El número pequeño 2 de CO2 indica dos átomos de oxígeno."),
   ("abc", "Una persona propone «corregir» la conclusión de Inés. ¿Cuál es la mejor redacción?", "«La masa total se conserva; en el vaso abierto escapó un gas de 4 g»", "«La materia se destruye siempre»", "«No ocurrió ninguna reacción»", "Corrige la conclusión usando la ley y la explicación."),
   ("abc", "{F} ¿Por qué el agua, H2O, es un compuesto útil para los seres vivos?", "Porque los cuerpos la necesitan y se forma al unirse hidrógeno y oxígeno", "Porque es un metal", "Porque no tiene átomos", "El agua es indispensable para la vida y es un compuesto de H y O."),
   ("abc", "¿Qué indica que una investigación es replicable?", "Otra persona puede repetirla con los mismos pasos y datos anotados", "Solo la hizo una persona", "No se escribieron los pasos", "Los pasos claros permiten repetirla y comparar."),
   ("abc", "Un informe concluye: «en todas las reacciones del mundo pasará lo mismo que en nuestros dos ensayos». ¿Qué problema tiene?", "Generaliza más allá de los datos", "Es demasiado corto", "Usa unidades", "Las conclusiones deben limitarse a lo investigado."),
   ("abc", "En una evaluación se dan puntos fuertes y mejoras. ¿Cuál es una mejora respetuosa?", "«Repetir cada montaje y anotar la temperatura sería aún mejor»", "«Este informe es inútil»", "«Quien lo hizo no sabe»", "La crítica se centra en el trabajo y propone mejoras.")],
  ("abc", "En un taller de ejemplo se deja un frasco tapado con una reacción que produce gas y el frasco pesa lo mismo antes y después. ¿Qué se concluye con la ley?", "La masa total se conservó porque el gas quedó dentro", "Que la reacción no ocurrió", "Que se destruyó materia", "El gas formado sigue en el sistema cerrado."),
  [("En Ciencias Naturales: ¿qué es una investigación replicable?", "Una que otra persona puede repetir con los mismos pasos", "Los pasos y condiciones deben estar claros."),
   ("En un balance de ejemplo en sistema cerrado, los reactantes suman 30 g y 50 g. ¿Cuántos gramos de productos se esperan?", "80", "Por conservación, los productos suman lo mismo que los reactantes."),
   ("¿Qué se pregunta primero si «desaparece» masa en un sistema abierto?", "Por dónde salió la materia", "Un gas pudo escapar del sistema.")],
  ("Con la ficha 6, escribe una evaluación breve del informe de Inés: dos puntos fuertes, dos puntos a mejorar, una conclusión corregida con la ley de conservación y un paso siguiente que propones.",
   "Fuertes: comparó vaso abierto y frasco tapado; anotó la masa en gramos. A mejorar: repetir cada montaje; anotar la temperatura. Conclusión: la masa se conserva y 4 g escaparon como gas. Paso siguiente: repetir tres veces cada montaje.",
   ["nombra puntos fuertes y a mejorar", "corrige la conclusión con la ley", "propone un paso siguiente concreto"],
   ["La evaluación se apoya en datos.", "Usa la conservación de la masa.", "Es respetuosa y propone mejoras."],
   "Si solo critica, pide que proponga una mejora concreta."),
  "Explica a otra persona, con tus palabras y sin tecnicismos, qué dice la ley de conservación de la masa.",
  "Escribe tres preguntas de una pauta para evaluar investigaciones y aplícalas a una noticia científica que conozcas.")

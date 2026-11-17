"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-03 (dogma central de la biología molecular, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todas las secuencias, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, microscopio ni internet. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos: los resultados que se analizan se entregan ya escritos. Las secuencias se razonan a mano, letra por letra, y no corresponden a genes reales. "
             "Se trabaja con conceptos del flujo de la información genética; no se incluyen procedimientos de manipulación del ADN.")
build = make_build(MATERIALS)

O3 = "CN-BCMO-3y4-OAC-03"

TABLA = ("Tabla de codones de ejemplo (ARN mensajero → aminoácido): AUG Met (inicio); UUU Phe; UUG Leu; GGC Gly; GGU Gly; AAA Lys; AAU Asn; GAA Glu; GCA Ala; GCU Ala; CCC Pro; UGG Trp; UAA, UAG y UGA son codones de parada.")

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (esquema de ejemplo del flujo de la información). Flecha 1: ADN → ADN, copia del ADN antes de dividirse la célula (replicación). Flecha 2: ADN → ARN, copia de un gen en una molécula de ARN mensajero (transcripción). "
     "Flecha 3: ARN → proteína, lectura del mensajero en un ribosoma para unir aminoácidos (traducción). Apareamiento de bases: en el ADN, A con T y G con C; en el ARN, la timina se reemplaza por uracilo (U), así que A se aparea con U.")
build(
    O3, 1, F,
    use="Aprenderé qué dice el dogma central de la biología molecular, qué es cada flecha del flujo de la información y cómo se copia una secuencia de bases. Sirve para empezar a analizar críticamente cómo la información genética se convierte en proteínas.",
    prior=["Sé que el ADN guarda la información hereditaria.", "Conozco las bases A, T, G y C.", "Sé que los ribosomas fabrican proteínas."],
    explain=[
        "El dogma central de la biología molecular describe el flujo de la información genética en las células: el ADN se copia a sí mismo (replicación), el ADN se copia a ARN (transcripción) y el ARN dirige la fabricación de proteínas (traducción). Dogma no significa verdad indiscutible: es el nombre histórico de un modelo, que se analiza con evidencia y que tiene excepciones, como verás después.",
        "Un gen es un segmento de ADN con la información para fabricar una molécula funcional, por ejemplo una proteína. En la transcripción, una enzima lee una hebra del ADN, llamada molde, y construye un ARN mensajero con bases complementarias. El ARN se diferencia del ADN en que casi siempre tiene una sola hebra, tiene el azúcar ribosa y usa uracilo (U) en lugar de timina (T).",
        "Copiar con bases complementarias significa que cada base se aparea con una determinada: en el ADN, A con T y G con C; al transcribir hacia ARN, A del ADN se aparea con U del ARN. Por eso, a partir de una hebra molde se puede escribir con precisión la secuencia que se obtendrá. Este es un razonamiento a mano que se practica con secuencias de ejemplo.",
    ],
    vocab=[("replicación", "copia del ADN antes de la división celular"), ("transcripción", "copia de un gen en una molécula de ARN"), ("traducción", "lectura del ARN mensajero para fabricar una proteína"), ("gen", "segmento de ADN con información para una molécula funcional"), ("hebra molde", "cadena de ADN que se lee para fabricar el ARN")],
    worked=[
        ("Transcribir una secuencia", "La hebra molde de ADN de ejemplo es TACGGA. ¿Cuál es el ARN mensajero?",
         ["T se aparea con A, A con U, C con G, G con C, G con C, A con U.", "Se escribe cada base complementaria en orden."],
         "AUGCCU"),
        ("Copiar una hebra de ADN", "Se replica un trozo de ADN de ejemplo con la hebra GATTC. ¿Cuál es la hebra complementaria?",
         ["G se aparea con C, A con T, T con A, T con A y C con G.", "Se lee en el mismo orden: CTAAG."],
         "CTAAG"),
    ],
    mistakes=[("Escribir T en el ARN: «el ARN de TACGGA es ATGCCT».", "En el ARN no hay timina; el apareamiento con A del ADN es U.", "Usa U en el ARN y revisa cada base."),
              ("Decir que la traducción copia el ADN.", "La traducción lee el ARN mensajero para fabricar una proteína; la copia del ADN es la replicación.", "Asocia traducción con proteínas.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué describe el dogma central?", "El flujo de la información genética entre ADN, ARN y proteínas", "La estructura de la membrana celular", "Las fases de la mitosis", "El dogma central es un modelo del flujo de información del ADN al ARN y a las proteínas."),
        ("{F} ¿Cómo se llama el paso ADN → ARN?", "Transcripción", "Copiar un gen a ARN se llama transcripción."),
        ("{F} ¿Dónde se lee el ARN mensajero para fabricar una proteína?", "En un ribosoma", "La traducción ocurre en los ribosomas."),
        ("abc", "{F} ¿Qué base del ARN se aparea con la adenina (A) del ADN?", "Uracilo (U)", "Timina (T)", "Citosina (C)", "Al transcribir, A del ADN se aparea con U del ARN."),
        ("ab", "{F} ¿Qué paso del dogma central produce una proteína?", "La traducción", "La replicación", "La traducción lee el mensajero para unir aminoácidos."),
        ("{F} ¿Qué base nitrogenada tiene el ARN y no tiene el ADN?", "Uracilo", "El ARN usa uracilo en lugar de timina."),
        ("Transcribe la hebra molde de ADN de ejemplo ATGCAT a ARN mensajero.", "UACGUA", "Cada base se aparea: A con U, T con A, G con C, C con G, A con U y T con A."),
        ("Escribe la hebra de ADN complementaria de la hebra de ejemplo CCGTA (replicación).", "GGCAT", "C se aparea con G, C con G, G con C, T con A y A con T."),
        ("abc", "{F} Un estudiante transcribe la hebra molde CATGGT y escribe GTACCA. ¿Qué error cometió?", "Usó T en el ARN en lugar de U", "Cambió el orden de las bases", "Usó bases que no existen", "Sus bases son correctas salvo la T, que en el ARN debe ser U."),
        ("abc", "{F} Una célula de ejemplo no puede transcribir un gen. ¿Qué producto no tendrá?", "El ARN mensajero de ese gen y, por tanto, su proteína", "Una copia completa del ADN", "Sus ribosomas", "Sin transcripción no hay mensajero, y sin mensajero no se fabrica la proteína."),
        ("ab", "Un compañero dice: «dogma significa que no se puede discutir». ¿Qué corriges?", "En ciencia, dogma central es el nombre de un modelo que se analiza con evidencia", "Tiene razón: no puede discutirse", "El nombre es histórico, pero el modelo se ajusta con nueva evidencia."),
        ("=", "Un gen de ejemplo tiene 90 bases en la hebra molde. ¿Cuántas bases tendrá el ARN mensajero que se transcribe de él?", "90", "Cada base del molde se aparea con una del ARN, así que el largo se mantiene.", " bases"),
        ("abc", "{F} ¿Por qué se dice que replicación y transcripción son procesos distintos?", "La replicación copia el ADN completo y la transcripción copia un gen en ARN", "Las dos producen proteínas", "Las dos ocurren en los ribosomas", "Replicar produce ADN; transcribir produce ARN."),
    ],
    ctx=("abc", "Contexto: tu docente te pide explicar en un afiche cómo una célula pasa de un gen a una proteína, para un curso que no conoce el tema. ¿Qué secuencia de pasos pones?", "ADN, transcripción a ARN mensajero y traducción en el ribosoma a proteína", "ADN, replicación y proteína", "Proteína, ARN y ADN", "El flujo correcto va del gen en el ADN al ARN y de ahí a la proteína."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una hebra molde?", "La cadena de ADN que se lee para fabricar el ARN", "El molde es la hebra que sirve para construir el ARN complementario."),
        ("ab", "El ARN usa:", "Uracilo", "Timina", "En el ARN el uracilo reemplaza a la timina."),
        ("ab", "La traducción produce:", "Una proteína", "Una copia del ADN", "La traducción une aminoácidos según el mensajero."),
    ],
    op=("Con el esquema de la ficha {F}: (1) escribe en una tabla las tres flechas con su nombre, qué entra y qué sale; (2) transcribe a ARN la hebra molde de ejemplo TTACGA; (3) explica con una frase por qué el nombre «dogma» no significa que no pueda discutirse.",
        "(1) Replicación: ADN a ADN; transcripción: ADN a ARN; traducción: ARN a proteína. (2) AAUGCU. (3) Es un nombre histórico: el modelo se ajusta con nueva evidencia.",
        ["tabla de las tres flechas", "ARN bien transcrito con U", "explicación del sentido de «dogma»"],
        ["una tabla, una secuencia y una frase"],
        ["escribir T en el ARN", "confundir transcripción con traducción", "presentar el modelo como no discutible"],
        "Pregunta: «¿qué evidencia nueva podría cambiar el modelo?»."),
    reinforce="Transcribe a ARN tres hebras molde de ADN que inventes de cinco bases y revisa cada base con tu compañero.",
    extend="Explica por qué la secuencia de bases del ADN puede considerarse una forma de información, y qué la distingue de un texto escrito.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (código genético de ejemplo). " + TABLA + " El ARN mensajero se lee de tres en tres bases (codones). El ARN de transferencia lleva el aminoácido y tiene una secuencia complementaria al codón, el anticodón. "
     "Mensajero de ejemplo: AUGUUUGGCAAAUAA.")
build(
    O3, 2, F,
    use="Aprenderé cómo el código genético permite traducir un ARN mensajero a una cadena de aminoácidos, leyendo de tres en tres bases. Sirve para pasar de una secuencia a una proteína y analizar qué tan universal y flexible es el código.",
    prior=["Sé transcribir ADN a ARN.", "Conozco los aminoácidos.", "Sé qué es un ribosoma."],
    explain=[
        "El código genético es la correspondencia entre codones y aminoácidos. Un codón son tres bases consecutivas del ARN mensajero. Con cuatro bases hay 4 × 4 × 4 = 64 codones posibles. De ellos, 61 codifican aminoácidos y 3 indican parada. El codón AUG es el de inicio y codifica metionina (Met).",
        "El código es degenerado, porque un mismo aminoácido puede tener varios codones (por ejemplo, GGC y GGU codifican glicina), y es casi universal, porque es el mismo en bacterias, plantas y animales, lo que apoya un origen común de los seres vivos. Es no ambiguo: un codón nunca codifica dos aminoácidos distintos.",
        "En la traducción, el ribosoma recorre el mensajero. Cada ARN de transferencia, que lleva un aminoácido, reconoce un codón con su anticodón complementario. El ribosoma une los aminoácidos en orden, hasta llegar a un codón de parada. Por eso la secuencia de bases determina la secuencia de aminoácidos, y esta determina la proteína.",
    ],
    vocab=[("codón", "tres bases consecutivas del ARN mensajero"), ("anticodón", "tres bases del ARN de transferencia complementarias a un codón"), ("código degenerado", "varios codones pueden codificar el mismo aminoácido"), ("codón de parada", "codón que indica el fin de la traducción"), ("ARN de transferencia", "ARN que lleva un aminoácido hasta el ribosoma")],
    worked=[
        ("Traducir un mensajero", "Traduce AUG UUU GGC con la tabla de la ficha.",
         ["AUG es Met, UUU es Phe y GGC es Gly.", "Se escriben en orden."],
         "Met, Phe, Gly"),
        ("Hallar el anticodón", "¿Qué anticodón reconoce el codón AUG?",
         ["El anticodón es complementario: A con U, U con A, G con C.", "A, U, G da U, A, C."],
         "UAC"),
    ],
    mistakes=[("Leer el mensajero de a dos bases o de a cuatro.", "El código se lee de a tres bases consecutivas, sin saltar bases.", "Marca los codones de tres en tres desde AUG."),
              ("Creer que un cambio de codón siempre cambia el aminoácido.", "El código es degenerado: GGC y GGU codifican el mismo aminoácido.", "Consulta la tabla antes de concluir.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un codón?", "Tres bases consecutivas del ARN mensajero", "Una proteína corta", "Un organelo", "Un codón es un triplete de bases que corresponde a un aminoácido o a una parada."),
        ("{F} ¿Qué aminoácido codifica el codón AUG?", "Metionina (Met)", "La tabla indica que AUG codifica Met y es además el codón de inicio."),
        ("{F} ¿Qué aminoácido codifica el codón AAA?", "Lisina (Lys)", "La tabla asigna AAA a Lys."),
        ("abc", "{F} ¿Cuál de estos codones es de parada?", "UAA", "AUG", "GGC", "UAA aparece en la tabla como codón de parada."),
        ("ab", "{F} Los codones GGC y GGU codifican el mismo aminoácido. ¿Qué propiedad muestra esto?", "El código es degenerado", "El código es ambiguo", "Varios codones para un mismo aminoácido es degeneración, no ambigüedad."),
        ("{F} Traduce el codón GAA con la tabla.", "Glu", "La tabla asigna el codón GAA al aminoácido Glu."),
        ("=", "Un código de ejemplo usaría solo dos bases (A y U) en cada una de las tres posiciones de un codón. ¿Cuántos codones distintos tendría?", "2*2*2", "En cada posición hay dos opciones, así que se multiplican las opciones de las tres posiciones.", " codones"),
        ("{F} Traduce el mensajero de ejemplo AUGUUUGGCAAAUAA, leyendo de tres en tres. Escribe los aminoácidos separados por guiones y no incluyas la parada.", "Met-Phe-Gly-Lys", "Los codones son AUG, UUU, GGC, AAA y UAA, que es de parada y no se escribe."),
        ("Escribe el anticodón que reconoce el codón GGC.", "CCG", "El anticodón es complementario: G con C, G con C y C con G."),
        ("abc", "{F} Un ARN mensajero de ejemplo tiene 60 bases, sin contar la parada. ¿Cuántos aminoácidos tiene la proteína que codifica?", "20", "60", "180", "Cada codón son 3 bases y codifica un aminoácido, así que 60 ÷ 3 da 20."),
        ("abc", "{F} En el mensajero AUGUUUGGC se cambia la tercera base del tercer codón y se obtiene AUGUUUGGU. ¿Qué pasa con la proteína?", "No cambia, porque GGU también codifica Gly", "Cambia el último aminoácido", "Se corta la proteína", "GGC y GGU codifican Gly, por lo que la proteína es igual."),
        ("ab", "Una compañera dice: «un mismo codón puede codificar dos aminoácidos distintos». ¿Qué corriges?", "Un codón codifica un único aminoácido: el código no es ambiguo", "Tiene razón: depende del organismo", "En el código genético cada codón tiene un significado único, aunque varios codones puedan compartirlo."),
        ("abc", "El código genético es el mismo en bacterias, plantas y animales. ¿Qué sugiere esto?", "Que los seres vivos comparten un origen común", "Que cada grupo surgió sin relación", "Que el código no tiene importancia", "Un código universal es consistente con un origen común de la vida."),
    ],
    ctx=("abc", "Contexto: en un taller de pares, un compañero quiere saber cómo una célula sabe dónde empieza y termina una proteína. ¿Cómo se lo explicas?", "Empieza en el codón AUG y termina en un codón de parada", "Empieza donde está la mitocondria", "No tiene inicio ni final", "El inicio lo marca AUG y el final un codón de parada."),
    sc=[
        ("En Biología celular y molecular: ¿qué es el anticodón?", "Tres bases del ARN de transferencia complementarias a un codón", "El anticodón reconoce el codón por complementariedad."),
        ("ab", "El código genético es:", "Casi universal", "Distinto en cada animal", "Es el mismo en la gran mayoría de los seres vivos."),
        ("ab", "Un codón tiene:", "Tres bases", "Dos bases", "Un codón son tres bases consecutivas."),
    ],
    op=("Con la tabla de la ficha {F}: (1) traduce el mensajero de ejemplo AUGGCUUUUUAA (lee de tres en tres); (2) escribe la hebra molde de ADN que lo originó; (3) explica con una frase por qué dos mensajeros distintos pueden dar la misma proteína.",
        "(1) AUG GCU UUU UAA: Met-Ala-Phe y parada. (2) TACCGAAAAATT. (3) Porque el código es degenerado: varios codones codifican el mismo aminoácido.",
        ["codones separados de a tres", "aminoácidos correctos", "hebra molde correcta", "explicación de la degeneración"],
        ["tres respuestas"],
        ["incluir la parada como aminoácido", "usar T en el ARN", "no leer de tres en tres"],
        "Pregunta: «¿qué pasaría si el mensajero no tuviera codón de parada?»."),
    reinforce="Traduce con la tabla otros tres mensajeros que inventes de tres codones y exprésalos en aminoácidos.",
    extend="Explica por qué la degeneración del código protege parcialmente a las proteínas de algunos cambios en el ADN.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (mensaje original y variantes de ejemplo). " + TABLA + " Mensajero original: AUG UUU GGC AAA UAA, que da Met-Phe-Gly-Lys y parada. "
     "Variante 1: AUG UUU GGU AAA UAA. Variante 2: AUG UUU GGC GAA UAA. Variante 3: AUG UUU GGC UAA UAA (el codón AAA cambia a UAA). Variante 4: AUG UUG GCA AAU AA, por pérdida de una U del segundo codón (el resto de las bases se vuelve a leer de tres en tres).")
build(
    O3, 3, F,
    use="Aprenderé a construir un modelo que predice cómo cambios en la secuencia de ADN o ARN afectan a la proteína, y a usarlo para analizar críticamente el dogma central. Sirve para entender por qué algunas mutaciones no tienen efecto y otras sí.",
    prior=["Sé traducir un mensajero con la tabla de codones.", "Sé qué es un codón.", "Sé que el código es degenerado."],
    explain=[
        "Una mutación es un cambio en la secuencia del ADN. Para predecir su efecto se sigue el flujo del dogma: el cambio en el ADN cambia el ARN, y el cambio en el ARN puede cambiar la proteína. Pero no siempre. Si el nuevo codón codifica el mismo aminoácido, la mutación es silenciosa. Si codifica otro aminoácido, es de cambio de sentido. Si aparece un codón de parada, es sin sentido y la proteína queda cortada.",
        "Una mutación de inserción o pérdida de una o dos bases desplaza la lectura de tres en tres y cambia todos los codones siguientes. Se llama corrimiento del marco de lectura y suele afectar mucho a la proteína. Una proteína modificada puede funcionar igual, funcionar peor, funcionar distinto o no funcionar, y eso depende de dónde ocurre el cambio y de qué tan importante es esa parte.",
        "El modelo permite una crítica: la secuencia determina la proteína, pero el efecto final depende también del ambiente y de otras moléculas. Por eso se habla de predicción con límites. Un modelo útil indica qué sabe, qué supone y en qué casos podría fallar.",
    ],
    vocab=[("mutación", "cambio en la secuencia del ADN"), ("mutación silenciosa", "cambio que no modifica el aminoácido"), ("cambio de sentido", "cambio que reemplaza un aminoácido por otro"), ("mutación sin sentido", "cambio que crea un codón de parada"), ("corrimiento del marco de lectura", "pérdida o ganancia de bases que desplaza la lectura de los codones")],
    worked=[
        ("Clasificar la variante 1", "La variante 1 cambia GGC por GGU. ¿Qué tipo de mutación es?",
         ["GGC y GGU codifican Gly.", "El aminoácido no cambia."],
         "Silenciosa"),
        ("Clasificar la variante 3", "La variante 3 pasa de AAA a UAA. ¿Qué efecto tiene?",
         ["UAA es un codón de parada.", "La proteína se corta antes de agregar Lys."],
         "Sin sentido; la proteína queda más corta"),
    ],
    mistakes=[("Suponer que toda mutación daña la proteína.", "Muchas mutaciones son silenciosas o tienen efectos mínimos.", "Predice con la tabla de codones antes de concluir."),
              ("Cambiar solo un codón cuando se pierde una base.", "La pérdida de una base desplaza la lectura de todos los codones siguientes.", "Vuelve a separar de a tres desde el cambio.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es una mutación?", "Un cambio en la secuencia del ADN", "Un cambio en la forma de la membrana", "Una nueva proteína creada de la nada", "Una mutación es un cambio en la secuencia de bases del ADN."),
        ("{F} ¿Cuántos aminoácidos tiene la proteína original, sin contar la parada?", "4", "El mensajero original da Met, Phe, Gly y Lys antes de la parada."),
        ("{F} ¿Qué aminoácido codifica GAA en la variante 2?", "Glu", "La tabla asigna GAA al aminoácido Glu."),
        ("abc", "{F} ¿Qué tipo de mutación es la variante 2, que cambia AAA por GAA?", "Cambio de sentido", "Silenciosa", "Sin sentido", "AAA codifica Lys y GAA codifica Glu, así que se cambia un aminoácido."),
        ("ab", "{F} La variante 1 no cambia la proteína. ¿Qué propiedad del código lo explica?", "La degeneración", "La universalidad", "GGC y GGU codifican Gly porque varios codones pueden compartir el mismo aminoácido."),
        ("{F} ¿Cuántos aminoácidos tiene la proteína de la variante 3, sin contar la parada?", "3", "En la variante 3 la parada aparece donde estaba AAA, así que quedan Met, Phe y Gly."),
        ("{F} Traduce la variante 4 hasta donde se pueda leer de tres en tres con aminoácidos. Escribe los aminoácidos separados por guiones.", "Met-Leu-Ala-Asn", "Los codones son AUG, UUG, GCA y AAU; las dos bases finales no forman un codón completo."),
        ("=", "{F} La proteína original tiene 4 aminoácidos y la variante 3 tiene 3. ¿Cuántos aminoácidos se pierden?", "4-3", "La diferencia entre el largo original y el de la variante es lo que se pierde.", " aminoácido"),
        ("abc", "{F} ¿Qué variante cambia más aminoácidos?", "La variante 4, por el corrimiento del marco de lectura", "La variante 1", "La variante 2", "El corrimiento cambia todos los codones siguientes al cambio."),
        ("abc", "{F} Una compañera dice que como la variante 1 no cambia la proteína, entonces no hay mutación. ¿Qué respondes?", "Sí hay mutación: cambió el ADN, pero no el aminoácido", "Tiene razón: sin cambio en la proteína no hay mutación", "No se puede saber", "Una mutación es un cambio en la secuencia, aunque no se note en la proteína."),
        ("ab", "Una persona de ejemplo tiene una mutación sin sentido muy cerca del inicio de un gen. ¿Qué esperas?", "Una proteína muy corta que probablemente no funcione", "Una proteína normal", "Un codón de parada cerca del inicio corta casi toda la proteína."),
        ("abc", "{F} ¿Qué diferencia hay entre predecir con el modelo y asegurar el efecto final?", "El modelo predice la secuencia de aminoácidos, pero el efecto también depende del contexto de la célula", "No hay diferencia", "El modelo asegura el efecto final siempre", "La secuencia no basta: el efecto depende de dónde ocurre y del ambiente de la célula."),
        ("abc", "Un modelo útil debe indicar:", "Lo que sabe, lo que supone y dónde puede fallar", "Solo lo que sabe", "Que nunca puede fallar", "Declarar supuestos y límites es parte de un buen modelo."),
    ],
    ctx=("abc", "Contexto: en un trabajo grupal, tu equipo debe decidir cuál de dos mutaciones de ejemplo parece más grave: una silenciosa y una sin sentido cerca del inicio del gen. ¿Qué respondes?", "La sin sentido, porque corta la proteína; la silenciosa no cambia el aminoácido", "La silenciosa, porque cambia el ADN", "Ambas son igual de graves", "Un codón de parada temprano corta la proteína, y la silenciosa no cambia el aminoácido."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una mutación silenciosa?", "Un cambio que no modifica el aminoácido", "La silenciosa cambia el codón, pero no el aminoácido."),
        ("ab", "Perder una base desplaza:", "La lectura de los codones siguientes", "Solo el codón en que ocurre", "El corrimiento cambia todos los codones siguientes."),
        ("ab", "Un codón de parada nuevo produce:", "Una proteína más corta", "Una proteína más larga", "La traducción termina antes de lo normal."),
    ],
    op=("Con el mensaje de la ficha {F}: (1) inventa una variante del mensajero original que sea de cambio de sentido y tradúcela; (2) inventa otra que sea sin sentido y escribe cuántos aminoácidos quedan; (3) explica por qué el modelo predice la secuencia pero no asegura el efecto final.",
        "(1) AUG UUU AAU AAA UAA: Met-Phe-Asn-Lys. (2) AUG UAA GGC AAA UAA: queda solo Met. (3) Porque el efecto depende también de dónde ocurre el cambio y del contexto celular.",
        ["variante de cambio de sentido bien traducida", "variante sin sentido con el conteo correcto", "explicación de los límites del modelo"],
        ["tres respuestas"],
        ["cambiar más de un codón sin querer", "contar la parada como aminoácido", "afirmar que el modelo asegura el efecto"],
        "Pregunta: «¿qué dato adicional necesitarías para saber si la mutación daña la función?»."),
    reinforce="Traduce el mensajero original y dos variantes que inventes y rotula cada una como silenciosa, de cambio de sentido o sin sentido.",
    extend="Explica por qué un corrimiento del marco de lectura suele ser más grave que un cambio de una sola base.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (datos de ejemplo inspirados en experimentos históricos con sistemas sin células, ya escritos). Sistema con ribosomas, ARN de transferencia, aminoácidos y energía, al que se agrega un ARN artificial: ARN de solo UUU repetidos: se forma una cadena de solo fenilalanina; ARN de solo AAA repetidos: se forma una cadena de solo lisina; ARN de solo CCC repetidos: se forma una cadena de solo prolina. "
     "Sin ARN agregado: no se forma cadena. "
     "Dato de ejemplo sobre replicación: una molécula de ADN de doble hebra se replica; cada molécula hija tiene una hebra original y una hebra nueva.")
build(
    O3, 4, F,
    use="Aprenderé a analizar evidencia que apoya el flujo de información del dogma central: cómo los datos de sistemas simples permitieron asignar codones y cómo se interpreta la replicación. Sirve para distinguir lo que la evidencia dice de lo que se supone.",
    prior=["Sé qué es un codón.", "Sé cómo se leen los datos de una tabla de resultados.", "Conozco el flujo ADN, ARN, proteína."],
    explain=[
        "Para asignar significado a los codones se usaron sistemas sin células, es decir, mezclas con ribosomas, ARN de transferencia, aminoácidos y energía. Al agregar un ARN artificial de composición conocida, se miraba qué cadena de aminoácidos se formaba. Si con UUU repetidos solo se forma fenilalanina, se concluye que UUU codifica fenilalanina. Este diseño tiene un control: sin ARN agregado no se forma cadena, lo que muestra que el ARN dirige la síntesis.",
        "La evidencia sobre la replicación indica que es semiconservativa: cada molécula hija conserva una hebra original y recibe una hebra nueva. De ello se puede razonar con números. Si se parte de una molécula, tras una ronda hay 2 moléculas, tras dos rondas hay 4 y tras tres rondas hay 8, pero siempre solo dos moléculas contienen las hebras originales, una cada una.",
        "Analizar evidencia es separar tres cosas: lo que se observó (datos), lo que se concluye (inferencia) y lo que no permite concluir (límites). Por ejemplo, los datos de ARN artificial muestran qué aminoácido se asocia a cada codón repetido, pero no dicen por sí solos cómo se reconoce el inicio de una proteína en la célula completa.",
    ],
    vocab=[("sistema sin células", "mezcla de moléculas de la célula usada para estudiar un proceso"), ("ARN artificial", "ARN de secuencia conocida preparada para un experimento"), ("control", "condición sin el factor estudiado, que sirve de comparación"), ("replicación semiconservativa", "cada molécula hija conserva una hebra original y recibe una nueva"), ("inferencia", "conclusión que se deduce de los datos")],
    worked=[
        ("Asignar un codón con los datos", "El ARN con solo AAA repetidos da una cadena de solo lisina. ¿Qué codón codifica lisina?",
         ["El ARN solo contiene el codón AAA, repetido.", "La cadena solo tiene lisina."],
         "AAA codifica lisina"),
        ("Contar moléculas con hebras originales", "Una molécula se replica tres veces. ¿Cuántas moléculas hay y cuántas contienen una hebra original?",
         ["Cada ronda duplica el número: 2, 4 y 8.", "Las dos hebras originales se reparten, una en cada molécula distinta."],
         "8 moléculas, 2 con hebra original"),
    ],
    mistakes=[("Concluir que «el experimento prueba cómo empieza toda proteína en la célula».", "Los datos de ARN artificial solo asignan aminoácidos a codones; no estudian el inicio.", "Anota el límite: no permite concluir sobre el inicio de la traducción."),
              ("Olvidar el control: sin ARN agregado también podría formarse cadena.", "La condición sin ARN muestra que el ARN agregado es la causa.", "Siempre compara con una condición sin el factor.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿para qué sirve un control en un experimento?", "Para comparar con una condición sin el factor estudiado", "Para que el resultado salga como se espera", "Para ahorrar materiales", "El control muestra qué ocurre sin el factor y permite atribuir el efecto a él."),
        ("{F} ¿Qué cadena se forma con el ARN de solo UUU repetidos?", "Una cadena de solo fenilalanina", "El resultado de la ficha indica que UUU da fenilalanina."),
        ("{F} ¿Qué ocurre cuando no se agrega ARN al sistema?", "No se forma cadena", "Sin ARN agregado no se forma cadena, lo que sirve de control."),
        ("abc", "{F} ¿Qué se concluye del resultado con CCC repetidos?", "CCC codifica prolina", "CCC codifica fenilalanina", "CCC es un codón de parada", "El ARN solo con CCC da una cadena de prolina, luego CCC codifica prolina."),
        ("ab", "{F} ¿Por qué es importante la condición sin ARN agregado?", "Muestra que sin ARN no se forma la cadena, así que el ARN dirige la síntesis", "Muestra que el ARN no es necesario", "Si sin ARN no hay cadena, el ARN es necesario para dirigir la síntesis."),
        ("{F} En la replicación de ejemplo, ¿cuántas hebras originales tiene cada molécula hija?", "Una", "La replicación semiconservativa deja una hebra original en cada molécula hija."),
        ("=", "{F} Una molécula de ADN se replica dos veces seguidas. ¿Cuántas moléculas hay al final?", "2*2", "Cada ronda de replicación duplica el número de moléculas.", " moléculas"),
        ("=", "{F} Una molécula se replica cuatro veces. ¿Cuántas moléculas hay al final?", "2*2*2*2", "Cada replicación duplica el número, así que se multiplican cuatro veces por 2.", " moléculas"),
        ("abc", "{F} Tras cuatro rondas, ¿cuántas moléculas contienen alguna hebra de las originales?", "2", "1", "16", "Las dos hebras originales quedan en dos moléculas distintas, aunque haya dieciséis moléculas."),
        ("abc", "{F} Una estudiante dice: «los datos muestran que UUU es el codón de inicio de todas las proteínas». ¿Qué falla?", "Los datos solo asignan UUU a fenilalanina; no hablan del inicio", "Nada: está bien concluido", "Los datos muestran que UUU es de parada", "El experimento no estudia dónde empieza la traducción."),
        ("ab", "{F} ¿Cuál es un límite de usar un sistema sin células?", "No reproduce todos los controles que hay en una célula completa", "No sirve para estudiar nada", "Un sistema simple aísla un proceso, pero deja fuera la regulación de la célula completa."),
        ("abc", "{F} Si un ARN artificial de solo GGG repetidos produjera una cadena de glicina, ¿qué se concluiría?", "Que GGG codifica glicina", "Que GGG es de parada", "Que GGG codifica fenilalanina", "La cadena obtenida indica el aminoácido que codifica el codón repetido."),
        ("abc", "{F} ¿Qué dato adicional reforzaría la conclusión de que UUU codifica fenilalanina?", "Que otros grupos obtengan el mismo resultado", "Que el resultado sea fácil de explicar", "Que el informe tenga muchos gráficos", "La replicación del resultado por otros grupos aumenta la confianza."),
    ],
    ctx=("abc", "Contexto: en un debate de clase alguien afirma que «el código genético se descubrió por casualidad». Con la ficha, ¿qué respondes?", "Se descubrió con experimentos planificados que usaron ARN de composición conocida y un control", "Se descubrió por casualidad, sin datos", "Se descubrió leyendo libros antiguos", "Los experimentos con controles muestran un trabajo sistemático."),
    sc=[
        ("En Biología celular y molecular: ¿qué es replicación semiconservativa?", "Cada molécula hija conserva una hebra original y recibe una hebra nueva", "Semiconservativa significa que se conserva la mitad original."),
        ("ab", "Un control sirve para:", "Comparar con una condición sin el factor", "Cambiar el resultado", "El control permite atribuir el efecto al factor."),
        ("ab", "La inferencia es:", "Lo que se concluye de los datos", "El dato observado", "La inferencia va más allá del dato, apoyándose en él."),
    ],
    op=("Con los datos de la ficha {F}: (1) escribe una tabla con tres ARN artificiales y qué aminoácido se asigna a cada codón; (2) escribe qué resultado sirve de control y por qué; (3) escribe un límite: algo que estos datos no permiten concluir.",
        "(1) UUU: fenilalanina; AAA: lisina; CCC: prolina. (2) Sin ARN agregado no se forma cadena: muestra que el ARN dirige la síntesis. (3) No dicen cómo se reconoce el inicio de una proteína en la célula completa.",
        ["tabla con tres codones y su aminoácido", "control identificado con razón", "límite bien formulado"],
        ["una tabla y dos respuestas"],
        ["no identificar el control", "concluir más de lo que muestran los datos", "no declarar límite"],
        "Pregunta: «¿qué experimento nuevo ayudaría a estudiar el inicio de una proteína?»."),
    reinforce="Escribe tres frases separando dato, inferencia y límite para el experimento del ARN de solo UUU.",
    extend="Explica por qué la replicación de un resultado por grupos distintos es importante para aceptar un modelo.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (dos versiones del dogma y afirmaciones de ejemplo). Versión 1: «la información fluye de forma estricta e invariable solo en una dirección: ADN → ARN → proteína». "
     "Versión 2: «la información genética pasa entre ácidos nucleicos (ADN y ARN) en varias formas, pero no pasa desde una proteína hacia un ácido nucleico». "
     "Hechos conocidos: algunos virus tienen ARN como material genético y usan la enzima transcriptasa inversa para fabricar ADN a partir de su ARN (retrovirus, como el VIH). Otros virus copian su ARN en nuevo ARN. "
     "Muchos ARN no se traducen a proteína: el ARN de transferencia y el ARN ribosomal son ARN funcionales. En células eucariontes, el ARN recién transcrito se procesa antes de ser mensajero maduro.")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos versiones del dogma central y a decidir cuál se ajusta mejor a la evidencia, reconociendo excepciones y matices. Sirve para analizar críticamente el modelo y no repetirlo como una regla rígida.",
    prior=["Conozco replicación, transcripción y traducción.", "Sé qué es una excepción a una regla.", "Sé que un modelo puede ajustarse con nueva evidencia."],
    explain=[
        "Un modelo científico se juzga por qué tan bien explica los hechos. La versión estricta del dogma, ADN a ARN y a proteína en una sola dirección, explica la mayoría de los procesos celulares, pero no todos. Los retrovirus, por ejemplo, usan la transcriptasa inversa para pasar de ARN a ADN. Eso no derrumba el modelo; obliga a precisarlo.",
        "La versión 2 es más ajustada: la información puede pasar entre ácidos nucleicos de varias formas (ADN a ADN, ADN a ARN, ARN a ARN, ARN a ADN) y de ellos a proteínas, pero no se ha encontrado que una proteína sirva de molde para fabricar un ácido nucleico. Además, no todo ARN se traduce, y en eucariontes el ARN se procesa antes de ser mensajero. Por eso el flujo real es más rico que el esquema simple.",
        "Analizar críticamente es comparar versiones, buscar contraejemplos y decidir cuál versión explica más hechos con menos supuestos. También es reconocer que el modelo no incluye por sí mismo la regulación (cuándo y cuánto se expresa un gen), que es el tema de la siguiente unidad, ni las consideraciones éticas de usar estos conocimientos.",
    ],
    vocab=[("transcriptasa inversa", "enzima que fabrica ADN a partir de ARN"), ("retrovirus", "virus con ARN que usa la transcriptasa inversa"), ("contraejemplo", "caso que contradice una regla general"), ("ARN funcional", "ARN que cumple su función sin traducirse a proteína"), ("procesamiento del ARN", "cambios que sufre el ARN antes de ser mensajero maduro en eucariontes")],
    worked=[
        ("Poner a prueba la versión 1", "¿La versión 1 explica a un retrovirus?",
         ["La versión 1 dice que la información fluye solo de ADN a ARN a proteína.", "Un retrovirus fabrica ADN a partir de ARN: es un flujo de ARN a ADN."],
         "No: el retrovirus es un contraejemplo a la versión 1"),
        ("Revisar la versión 2", "¿La versión 2 explica el ARN de transferencia, que no se traduce a proteína?",
         ["La versión 2 dice que la información pasa entre ácidos nucleicos y hacia proteínas, sin exigir que todo ARN se traduzca.", "El ARN de transferencia es un ARN funcional."],
         "Sí: no contradice a la versión 2"),
    ],
    mistakes=[("Decir que los retrovirus «rompen» el dogma central.", "El dogma central trata de la imposibilidad de pasar información desde una proteína hacia un ácido nucleico; el paso ARN a ADN no la contradice.", "Distingue entre la versión simplificada y la formulación precisa."),
              ("Pensar que todo ARN se traduce a proteína.", "Hay ARN funcionales que cumplen su función sin traducirse.", "Pregunta si el ARN es mensajero o funcional.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué hace la transcriptasa inversa?", "Fabrica ADN a partir de ARN", "Fabrica proteínas a partir de ADN", "Copia proteínas", "La transcriptasa inversa pasa la información de ARN a ADN."),
        ("{F} ¿Cuál de las dos versiones permite el paso de ARN a ADN?", "La versión 2", "La versión 2 incluye varios flujos entre ácidos nucleicos."),
        ("{F} ¿Qué dos tipos de ARN funcionales se mencionan?", "ARN de transferencia y ARN ribosomal", "La ficha nombra el ARN de transferencia y el ribosomal como ARN que no se traducen."),
        ("abc", "{F} ¿Por qué un retrovirus es un contraejemplo a la versión 1?", "Porque fabrica ADN a partir de ARN", "Porque no tiene ARN", "Porque produce proteínas sin ARN", "La versión 1 solo admite ADN a ARN, y el retrovirus hace ARN a ADN."),
        ("ab", "{F} ¿Qué dice la versión 2 que la versión 1 no dice?", "Que la información puede pasar entre ácidos nucleicos de varias formas", "Que las proteínas fabrican ADN", "La versión 2 amplía los flujos posibles entre ADN y ARN, sin permitir proteína a ácido nucleico."),
        ("{F} ¿Hacia dónde no pasa información según la versión 2?", "Desde una proteína hacia un ácido nucleico", "La versión 2 excluye el paso de proteína a ácido nucleico."),
        ("abc", "{F} Un estudiante dice: «los retrovirus muestran que las proteínas fabrican ADN». ¿Qué corriges?", "El retrovirus fabrica ADN desde ARN con una enzima; la proteína actúa como enzima, no como molde", "Tiene razón: las proteínas son el molde del ADN", "Los retrovirus no fabrican ADN", "La enzima cataliza la reacción, pero la secuencia viene del ARN."),
        ("abc", "{F} Un ARN ribosomal de ejemplo, ¿se traduce a proteína?", "No: es un ARN funcional", "Sí: todo ARN se traduce", "Solo si es de un virus", "El ARN ribosomal cumple su función como ARN y no se traduce."),
        ("abc", "{F} En células eucariontes, ¿qué ocurre con el ARN recién transcrito antes de ser mensajero maduro?", "Se procesa", "Se traduce de inmediato sin cambios", "Se convierte en ADN", "La ficha indica que el ARN eucarionte se procesa antes de ser maduro."),
        ("ab", "{F} Para decidir entre las versiones, ¿qué criterio es mejor?", "Elegir la que explica más hechos con menos supuestos", "Elegir la más simple aunque deje hechos sin explicar", "Un buen modelo explica más hechos conocidos, no solo los más sencillos."),
        ("abc", "{F} Un compañero propone una versión 3: «el ARN nunca pasa a ADN». ¿Qué evidencia la contradice?", "La transcriptasa inversa de los retrovirus", "El ARN de transferencia", "El procesamiento del ARN", "La transcriptasa inversa muestra un paso de ARN a ADN."),
        ("abc", "El dogma central, ¿incluye cuándo y cuánto se expresa un gen?", "No: eso corresponde a la regulación génica", "Sí: lo explica todo", "Solo en animales", "El dogma describe el flujo de la información, no su regulación."),
        ("abc", "Alguien dice: «la transcriptasa inversa prueba que la ciencia se equivocó». ¿Cuál es la mejor respuesta?", "Prueba que el modelo se ajustó al encontrar nueva evidencia", "Prueba que no hay modelos útiles", "No tiene relación con el modelo", "En ciencia, los modelos se precisan con nueva evidencia, no se descartan sin más."),
    ],
    ctx=("abc", "Contexto: en una charla del liceo, alguien dice que «el dogma central dice que todo ARN se traduce a proteína». ¿Cómo lo corriges con respeto?", "Hay ARN funcionales, como el de transferencia, que no se traducen", "Tiene toda la razón", "El ARN solo existe en virus", "Corregir con un ejemplo concreto muestra que no todo ARN se traduce."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un contraejemplo?", "Un caso que contradice una regla general", "Un contraejemplo obliga a revisar la regla."),
        ("ab", "Un retrovirus pasa información de:", "ARN a ADN", "Proteína a ADN", "La transcriptasa inversa fabrica ADN desde ARN."),
        ("ab", "Los modelos científicos:", "Se precisan con nueva evidencia", "No cambian nunca", "La ciencia ajusta sus modelos con nueva evidencia."),
    ],
    op=("Con las dos versiones de la ficha {F}: (1) construye una tabla con tres hechos conocidos (retrovirus, ARN funcional, procesamiento del ARN) y marca si cada uno es coherente con la versión 1 y con la versión 2; (2) concluye cuál versión te parece mejor y por qué; (3) escribe una limitación del modelo.",
        "(1) Retrovirus: no coherente con la 1, coherente con la 2; ARN funcional: coherente con la 2; procesamiento del ARN: coherente con la 2. (2) La versión 2, porque explica más hechos con los mismos supuestos. (3) No incluye la regulación de la expresión de los genes.",
        ["tabla con tres hechos y dos versiones", "conclusión justificada con la tabla", "limitación del modelo"],
        ["una tabla y dos respuestas"],
        ["marcar como coherente un hecho que no lo es", "concluir sin usar la tabla", "no mencionar ninguna limitación"],
        "Pregunta: «¿qué hecho nuevo te haría revisar la versión 2?»."),
    reinforce="Escribe dos frases que expliquen con tus palabras por qué un contraejemplo no destruye un modelo, sino que lo precisa.",
    extend="Explica por qué dos modelos pueden convivir un tiempo y qué datos permiten decidir entre ellos.",
)

"""Cuaderno del estudiante, 4.º básico Inglés: EN04 OA 13 (escritura con modelo) y OA 14 (escritura a partir de imágenes).

Las imágenes se describen entre corchetes porque el cuaderno no incluye ilustraciones. Todas las palabras necesarias
(banco de palabras, modelos, números) están escritas en cada ejercicio; el espacio de escritura es una hoja o cuaderno propio.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en4_b import lesson
from student_lessons import arith

OA13, OA14 = "EN04 OA 13", "EN04 OA 14"

# ================================================================ OA 13
lesson(
    OA13, 1,
    "Los modelos escritos en cada ejercicio, lápiz grafito, una hoja con renglones y una hoja para tapar el modelo.",
    "Aprenderé a copiar oraciones en inglés por bloques con sentido, cuidando mayúscula, espacios, ortografía y punto final. Sirve para escribir bien sin perder palabras ni letras.",
    ["Sé escribir palabras cortas en inglés.", "Sé que una oración empieza con mayúscula y termina con punto."],
    [
        "Copiar (copy) es escribir lo mismo que dice un modelo (model). Para copiar bien no escribas letra por letra: divide la oración en bloques con sentido (chunks). Por ejemplo, «The cat | is on | the mat.» tiene tres bloques. Mira un bloque, tápalo, escríbelo de memoria y compáralo con el modelo.",
        "Revisa cuatro cosas. Primero, la oración empieza con letra mayúscula (capital letter). Segundo, hay un espacio (space) entre palabras. Tercero, la ortografía es igual a la del modelo. Cuarto, termina con punto (period). En inglés la palabra I siempre va con mayúscula, y también los nombres de personas y países y los días de la semana: Chile, Monday, Ana.",
        "Si encuentras una diferencia entre tu copia y el modelo, corrígela con otro color. Una buena copia es idéntica al modelo: no cambia ninguna letra. Copiar con cuidado es el primer paso para escribir tus propias oraciones, porque aprendes cómo se ven las palabras.",
    ],
    [("copy", "copiar"), ("model", "modelo"), ("chunk", "bloque con sentido"), ("capital letter", "letra mayúscula"), ("space", "espacio"), ("period", "punto final")],
    [
        ("Copiar por bloques", "Modelo: «The dog is in the park.» Divide en bloques con sentido y copia.", ["Separo: The dog | is in | the park.", "Copio un bloque cada vez.", "Reviso mayúscula, espacios y punto."], "The dog is in the park."),
        ("Revisar una copia", "Modelo: «The dog is in the park.» Copia de Ana: «the dog is in the park». ¿Qué le falta?", ["Miro el inicio: empieza con t minúscula.", "Miro el final: no hay punto.", "Corrijo las dos cosas."], "Le falta la mayúscula en The y el punto final."),
    ],
    [
        ("Copiar letra por letra sin mirar el sentido.", "Se pierden letras o palabras.", "Copia bloque por bloque y compara."),
        ("Olvidar la mayúscula del inicio y el punto final.", "La oración queda incompleta.", "Revisa siempre el inicio y el final."),
    ],
    [
        ("¿Qué significa «copy»?", "Copiar", "Copy es escribir lo mismo que el modelo."),
        ("¿Con qué letra empieza una oración?", "Con letra mayúscula", "La mayúscula marca el inicio."),
        ("¿Qué signo va al final de la oración?", "Un punto", "El punto indica que la oración terminó."),
    ],
    [
        ("Modelo: «The bird is in the tree.» Elige los bloques correctos: (a) The bird | is in | the tree. (b) The | bird is | in the tree.", "a", "Los bloques (a) tienen sentido completo."),
        ("Modelo: «I have a red bag.» Elige la copia correcta: (a) «I have a red bag.» (b) «i have a red bag»", "a", "La copia (a) tiene mayúscula y punto."),
        ("Modelo: «The cat is on the mat.» ¿Cuántas palabras tiene? Escribe el número.", "6", "The, cat, is, on, the, mat son seis palabras."),
    ],
    [
        ("Modelo: «She has a blue hat.» Copia: «She has a blu hat.» ¿Cuál palabra está mal escrita? Escríbela como debe ir.", "blue", "El modelo dice blue."),
        ("Modelo: «We like music.» Escribe la copia correcta.", "We like music.", "Una copia exacta lleva mayúscula, ortografía igual y punto."),
        ("Modelo: «Today is Monday.» Copia: «Today is monday.» ¿Qué palabra debe ir con mayúscula? Escríbela.", "Monday", "Los días de la semana van con mayúscula en inglés."),
    ],
    [
        ("Ana copió «the dog is big» del modelo «The dog is big.» ¿Qué dos cosas corrige? Responde en español.", "La mayúscula inicial y el punto final", "Su copia empieza con t minúscula y no tiene punto."),
        ("Luis copia letra por letra y se pierde. ¿Por qué ayuda copiar por bloques? Responde en español.", "Porque cada bloque tiene sentido y es más fácil de recordar", "Los bloques con sentido se recuerdan mejor que las letras sueltas."),
    ],
    [
        ("Modelo: «My brother plays soccer.» Copia: «My brother play soccer.» ¿Qué palabra difiere? Escribe la palabra del modelo.", "plays", "El modelo lleva plays con s."),
        ("Modelo: «I am from Chile.» Copia: «I am from chile.» ¿Qué palabra debe cambiar y cómo? Escríbela bien.", "Chile", "Los nombres de países llevan mayúscula."),
    ],
    [("En tu cuaderno de inglés copias lo que hay en la pizarra: «Today is Monday.» Elige la copia correcta: (a) «Today is Monday.» (b) «today is monday»", "a", "La copia (a) conserva mayúsculas y punto.")],
    [
        ("¿Qué es un «chunk»?", "Un bloque con sentido", "Se copia un bloque a la vez."),
        ("¿Cómo se escribe la palabra «yo» en inglés?", "I", "La palabra I siempre lleva mayúscula."),
        ("¿Qué hago si mi copia es distinta del modelo?", "La corrijo", "Una buena copia es idéntica al modelo."),
    ],
    task("Copia estas tres oraciones modelo por bloques con sentido en una hoja con renglones: (1) The cat is on the mat. (2) I have a red bag. (3) We like music. Divide cada una en bloques, escribe cada bloque de memoria y luego compara con el modelo. Revisa mayúscula, espacios, ortografía y punto. Corrige con otro color y pide a una persona de tu casa que lea tu copia en voz alta.", "Bloques: The cat | is on | the mat. Copia: The cat is on the mat.", ["divide cada oración en bloques con sentido", "las tres copias son idénticas al modelo", "tiene mayúscula, espacios y punto en cada oración", "corrige con otro color lo que difiere"], ["la hoja con las tres copias", "nota de la persona que leyó las copias"], ["olvidar el punto final", "cambiar una letra del modelo"], "La otra persona compara una oración con el modelo y señala la letra que cambió."),
    "Copia una oración corta del modelo de esta clase tapando el modelo y compárala.",
    "Escribe en tu cuaderno cinco oraciones copiadas de textos en inglés que tengas y revisa mayúscula y punto.",
)

lesson(
    OA13, 2,
    "El banco de palabras y las oraciones escritas en cada ejercicio, lápiz grafito y una hoja para escribir.",
    "Aprenderé a completar oraciones en inglés con palabras de un banco de palabras, eligiendo la que encaja por sentido y por forma. Sirve para escribir oraciones correctas con apoyo.",
    ["Sé copiar una oración por bloques.", "Sé palabras como is, are, a y an."],
    [
        "Completar (complete) una oración es escribir la palabra que falta. Un banco de palabras (word bank) es una lista de palabras entre las que puedes elegir. Por ejemplo: «The ___ is red.» con el banco apple, runs, blue. La palabra que encaja es apple, porque una oración como «The apple is red» tiene sentido.",
        "Para elegir bien, mira dos cosas. La primera es el sentido: ¿la oración tiene sentido con esa palabra? La segunda es la forma: ¿es el tipo de palabra que falta? Después de The suele venir un nombre (apple); después de is suele venir una descripción (red). Con una sola cosa se usa is, y con varias se usa are. Antes de vocal se usa an (an apple), y antes de consonante se usa a (a banana).",
        "Cuando termines, lee la oración completa para comprobar que suena bien y que está bien escrita. Escribe la palabra tal como aparece en el banco, sin cambiar letras. Si el banco tiene varias palabras para varias oraciones, usa cada una una sola vez.",
    ],
    [("complete", "completar"), ("word bank", "banco de palabras"), ("missing", "que falta"), ("meaning", "sentido, significado"), ("form", "forma de la palabra"), ("check", "revisar")],
    [
        ("Elegir con sentido", "Completa «The ___ is red.» con el banco: apple, runs, blue.", ["Pruebo apple: The apple is red tiene sentido.", "Pruebo runs: The runs is red no tiene sentido.", "Pruebo blue: The blue is red tampoco."], "apple"),
        ("Elegir con forma", "Completa «They ___ happy.» con el banco: is, are.", ["They son varios.", "Con varios se usa are.", "Leo la oración completa."], "are"),
    ],
    [
        ("Elegir una palabra por parecerse y no por sentido.", "La oración queda sin sentido.", "Prueba la palabra en la oración completa."),
        ("Cambiar las letras de la palabra del banco al escribirla.", "Aparecen errores de ortografía.", "Copia la palabra tal como está en el banco."),
    ],
    [
        ("¿Qué es un «word bank»?", "Una lista de palabras para elegir", "El banco de palabras ayuda a completar."),
        ("Completa «I have a ___.» con el banco: book, runs.", "book", "Book es un nombre y encaja después de a."),
        ("¿Qué significa «missing»?", "Que falta", "La palabra missing es la que debo escribir."),
    ],
    [
        ("Completa «She ___ a teacher.» con el banco: is, are.", "is", "She es una persona y lleva is."),
        ("Completa «The cat drinks ___.» con el banco: milk, run.", "milk", "Se toma milk, no run."),
        ("Completa «I see ___ apple.» con el banco: a, an.", "an", "Apple empieza con vocal."),
    ],
    [
        ("Completa «We play in the ___.» con el banco: park, happy, eats.", "park", "Después de in the va un lugar."),
        ("Completa «There are ___ books on the table.» con el banco: three, sleeps.", "three", "Three es un número y sleeps es un verbo."),
        ("Completa «The ___ is big.» con el banco: elephant, small.", "elephant", "Después de The va un nombre."),
    ],
    [
        ("Ana escribió «The runs is big». ¿Por qué no sirve runs? Responde en español.", "Porque runs es un verbo y falta un nombre", "Después de The va un nombre."),
        ("Luis eligió is para «The dogs ___ big.» ¿Cuál es la palabra correcta? Banco: is, are.", "are", "Dogs son varios y llevan are."),
    ],
    [
        ("Banco: brown, runs, tree. Completa: «Mia has a ___ dog. The dog ___ in the park. It is next to a ___.» Escribe las tres palabras separadas por comas.", "brown, runs, tree", "Brown describe el perro, runs es la acción y tree es un nombre."),
        ("Banco: sunny, drink, hat. Completa: «It is a ___ day. I ___ water. I wear a ___.» Escribe las tres palabras separadas por comas.", "sunny, drink, hat", "Sunny describe el día, drink es una acción y hat es una cosa."),
    ],
    [("En una tarjeta de receta lees: «Mix the ___ and the milk.» (mix es mezclar). El banco dice: flour (harina), bike. Elige la palabra que completa la tarjeta.", "flour", "Se mezcla harina con leche; no una bicicleta.")],
    [
        ("¿Cómo se dice «completar» en inglés?", "complete", "Complete es completar."),
        ("¿Qué dos cosas miro para elegir una palabra del banco?", "El sentido y la forma", "Así la oración suena bien."),
        ("¿Cuándo uso are?", "Con varias cosas o con they", "Are va con plurales."),
    ],
    task("Completa estas cinco oraciones con el banco de palabras (usa cada palabra una vez): dog, runs, green, is, three. (1) The ___ is brown. (2) The dog ___ every day. (3) I have a ___ pencil. (4) She ___ happy. (5) There are ___ cats. Escribe cada oración completa en tu cuaderno con mayúscula y punto. Lee cada una en voz alta para comprobar que tiene sentido.", "(1) The dog is brown. (2) The dog runs every day. (3) I have a green pencil. (4) She is happy. (5) There are three cats.", ["completa las cinco oraciones", "usa cada palabra del banco una sola vez", "cada oración tiene sentido", "cada oración empieza con mayúscula y termina con punto"], ["las cinco oraciones escritas", "nota de la persona que las leyó"], ["usar una palabra dos veces", "olvidar el punto final"], "Pregunta por qué elegiste cada palabra y revisa el sentido y la forma."),
    "Completa mentalmente «The ___ is red» con otra palabra que tenga sentido.",
    "Escribe tres oraciones con una palabra que falta y un banco de tres palabras, y pide a otra persona que las complete.",
)

lesson(
    OA13, 3,
    "Los modelos escritos en cada ejercicio, lápiz grafito, lápices de colores y una hoja con renglones.",
    "Aprenderé a transformar un elemento de una oración modelo (color, cosa, cantidad o persona) para decir otra idea. Sirve para escribir mis propias oraciones apoyándome en un modelo.",
    ["Sé copiar una oración y completarla con un banco de palabras.", "Sé colores, objetos y números hasta diez en inglés."],
    [
        "Transformar (transform) una oración es cambiar solo un elemento de un modelo y dejar el resto igual. Con el modelo «I have a red bag» (tengo una mochila roja) puedes cambiar el color: «I have a blue bag». Puedes cambiar la cosa: «I have a red hat». O puedes cambiar la cantidad: «I have two red bags». Si cambias la cantidad, la cosa lleva s al final: bags.",
        "El orden de las palabras (word order) es importante. En inglés la descripción va antes de la cosa: a red bag, no «a bag red». El orden básico es quién hace la acción, la acción y el resto: I have a red bag. Si cambias la persona, a veces cambia el verbo: con I decimos «I have», pero con she o he decimos «She has a red bag».",
        "Después de transformar, revisa tu oración con la lista: ¿cambié solo un elemento?, ¿está en orden?, ¿tiene mayúscula, espacios y punto? Si cambiaste más de un elemento, ya no es una transformación del modelo, sino otra oración. Así aprendes a construir tus propias oraciones con seguridad.",
    ],
    [("transform", "transformar, cambiar un elemento"), ("word order", "orden de las palabras"), ("change", "cambiar"), ("red", "rojo"), ("blue", "azul"), ("has", "tiene")],
    [
        ("Cambiar el color", "Modelo: «I have a red bag.» Cambia el color a azul (blue).", ["Identifico el elemento: red.", "Lo reemplazo por blue.", "Dejo todo lo demás igual."], "I have a blue bag."),
        ("Cambiar la persona", "Modelo: «I have a red bag.» Cambia la persona a she.", ["Cambio I por She.", "Con she el verbo es has.", "Reviso mayúscula y punto."], "She has a red bag."),
    ],
    [
        ("Cambiar dos elementos y decir que es una transformación.", "Ya no se sabe qué cambió.", "Cambia solo un elemento a la vez."),
        ("Decir «a bag red».", "En inglés la descripción va antes de la cosa.", "Di a red bag."),
    ],
    [
        ("¿Qué significa «transform»?", "Cambiar un elemento", "En esta clase se cambia un elemento del modelo."),
        ("Modelo: «I have a red bag.» ¿Qué elemento cambió en «I have a blue bag.»?", "El color", "Cambió red por blue."),
        ("¿Cómo se dice «tiene» con she en inglés?", "has", "She has es la forma correcta."),
    ],
    [
        ("Modelo: «I have a red bag.» Elige la oración con la cosa cambiada: (a) «I have a red hat.» (b) «I have two red bags.»", "a", "Cambió bag por hat."),
        ("Modelo: «I have a red bag.» Elige la oración con la cantidad cambiada: (a) «I have two red bags.» (b) «I have a blue bag.»", "a", "Cambió la cantidad a two y bag pasó a bags."),
        ("Elige la oración con el orden correcto: (a) «a red bag» (b) «a bag red»", "a", "La descripción va antes de la cosa."),
    ],
    [
        ("Modelo: «I like apples.» Cambia apples por bananas y escribe la oración.", "I like bananas.", "Solo cambia la cosa."),
        ("Modelo: «I have a red bag.» Cambia la persona a he y escribe la oración.", "He has a red bag.", "Con he el verbo es has."),
        ("Modelo: «I have a green hat.» Cambia solo el color a yellow y escribe la oración.", "I have a yellow hat.", "Se reemplaza green por yellow."),
    ],
    [
        ("Luis cambió «I have a red bag» por «I have a blue hat». ¿Cuántos elementos cambió? Escribe el número.", "2", "Cambió el color y la cosa."),
        ("Ana escribió «She have a red bag». ¿Cómo se corrige? Responde en inglés.", "She has a red bag.", "Con she el verbo es has."),
    ],
    [
        ("Modelo: «I have two red bags.» Cambia solo la cantidad a three y escribe la oración. Recuerda la s de bags.", "I have three red bags.", "Solo cambia el número."),
        ("Modelo: «I have a big dog.» Cambia solo la cosa a cat y escribe la oración.", "I have a big cat.", "Solo cambia dog por cat."),
    ],
    [("En el club de arte escribes sobre tus lápices. Modelo: «I have a blue pencil.» Tienes un lápiz verde. Cambia solo el color y escribe la oración.", "I have a green pencil.", "Solo se cambia el color.")],
    [
        ("¿Cómo se dice «rojo» en inglés?", "red", "Red es rojo."),
        ("¿Qué es el «word order»?", "El orden de las palabras", "En una oración deben ir en orden."),
        ("¿Cuántos elementos cambio en una transformación?", "Uno", "Se cambia solo un elemento del modelo."),
    ],
    task("Con este modelo: «I have a red bag.» escribe en tu cuaderno cuatro oraciones nuevas, cada una con un solo elemento cambiado: (1) cambia el color a blue, (2) cambia la cosa a hat, (3) cambia la cantidad a two (recuerda la s de la cosa), (4) cambia la persona a she. Subraya con un color distinto el elemento que cambió en cada oración. Revisa mayúscula, espacios y punto.", "(1) I have a blue bag. (2) I have a red hat. (3) I have two red bags. (4) She has a red bag.", ["escribe cuatro oraciones", "cada oración cambia solo un elemento", "usa bags y has donde corresponde", "subraya el elemento que cambió y revisa el punto"], ["las cuatro oraciones subrayadas", "nota de la persona que las revisó"], ["cambiar dos elementos", "olvidar has con she"], "La otra persona dice qué elemento cambió en cada oración y comparan con el modelo."),
    "Di en voz alta el modelo «I have a red bag» cambiando solo el color.",
    "Elige otro modelo, por ejemplo «I like pizza», y escribe tres transformaciones cambiando un elemento cada una.",
)

lesson(
    OA13, 4,
    "El modelo y la lista de revisión escritos en esta clase, lápiz grafito y lápiz de otro color para corregir.",
    "Aprenderé a escribir una oración o dos con ayuda de un modelo y a revisarlas con una lista de comprobación. Sirve para escribir con confianza y encontrar mis propios errores.",
    ["Sé copiar, completar y transformar una oración modelo.", "Sé mayúscula, punto y espacios."],
    [
        "Para escribir con apoyo, usa un modelo. Modelo: «The cat is black. It is on the sofa.» (sofa es sillón). Puedes escribir sobre otro animal cambiando elementos: «The dog is white. It is on the bed.» (bed es cama). Mantienes la estructura y cambias el animal, el color y el lugar.",
        "Después de escribir, revisa con una lista de cinco puntos que llamaremos CSPWM. C: capital letter, la oración empieza con mayúscula. S: spaces, hay espacios entre palabras. P: period, termina con punto. W: words, las palabras están bien escritas. M: meaning, la oración tiene sentido y dice lo que quise decir.",
        "Marca cada punto con una señal cuando lo hayas revisado. Si algo falla, corrígelo con otro color. Revisar no es una pérdida de tiempo: es parte de escribir bien. Una oración corta, pero correcta y completa, vale más que una larga con errores.",
    ],
    [("write", "escribir"), ("check", "revisar"), ("capital letter", "mayúscula"), ("spaces", "espacios"), ("period", "punto"), ("meaning", "sentido")],
    [
        ("Escribir con un modelo", "Modelo: «The cat is black. It is on the sofa.» Escribe sobre un perro blanco que está sobre la cama (dog, white, bed).", ["Cambio cat por dog.", "Cambio black por white y sofa por bed.", "Dejo la estructura igual."], "The dog is white. It is on the bed."),
        ("Revisar con la lista", "Revisa «the dog is white It is on the bed». ¿Qué falla según C, S, P, W y M?", ["C: falta mayúscula en The.", "P: falta punto después de white.", "El resto está bien."], "Falta la mayúscula en The y el punto después de white."),
    ],
    [
        ("Entregar la oración sin revisarla.", "No se descubren los errores.", "Usa la lista CSPWM antes de terminar."),
        ("Cambiar tanto el modelo que no se parece.", "Ya no hay apoyo del modelo.", "Mantén la estructura y cambia pocos elementos."),
    ],
    [
        ("¿Qué letra de CSPWM revisa la mayúscula?", "C", "C es capital letter."),
        ("¿Qué significa «meaning»?", "Sentido", "M revisa que tenga sentido."),
        ("¿Qué letra de CSPWM revisa el punto final?", "P", "P es period."),
    ],
    [
        ("Elige la oración que cumple C, S y P: (a) «The dog is white.» (b) «the dog is white»", "a", "La oración (a) tiene mayúscula, espacios y punto."),
        ("Elige la oración con sentido: (a) «The cat is on the sofa.» (b) «The cat is on the blue.»", "a", "On the sofa tiene sentido; on the blue no."),
        ("Elige la oración bien escrita: (a) «The cat is black.» (b) «The cat is blak.»", "a", "Black se escribe con ck."),
    ],
    [
        ("Modelo: «The cat is black.» Escribe una oración nueva sobre un pez (fish) naranja (orange).", "The fish is orange.", "Se conserva la estructura y se cambia el animal y el color."),
        ("Revisa «The dog is whit.» Escribe la oración corregida.", "The dog is white.", "White se escribe con h y e final."),
        ("Revisa «The catis black.» ¿Qué letra de CSPWM falla? Responde: C, S o P.", "S", "Faltan espacios entre cat e is."),
    ],
    [
        ("Ana escribió «The dog is white. It is on the bed» sin punto final. ¿Qué letra de CSPWM falló? Responde.", "P", "Falta el punto al final."),
        ("Leo escribió «The dog is black. It is under the sofa.» pero la imagen mostraba a un perro blanco sobre la cama. ¿Qué letra de CSPWM falló? Responde.", "M", "La oración no dice lo que muestra la imagen."),
    ],
    [
        ("Ordena las palabras para formar una oración con el modelo: is / The / white / dog. Escríbela con mayúscula y punto.", "The dog is white.", "El orden es The, dog, is y white."),
        ("Escribe dos oraciones con el modelo, sobre un gato gris (gray) que está sobre una silla (chair).", "The cat is gray. It is on the chair.", "Se conserva la estructura del modelo."),
    ],
    [("En el cuaderno de ciencias anotas lo que ves en una imagen: [un pájaro azul sobre un árbol]. Usa el modelo «The cat is black. It is on the sofa.» y escribe dos oraciones sobre el pájaro. Banco: bird, blue, tree.", "The bird is blue. It is on the tree.", "Se usa la estructura del modelo con el pájaro.")],
    [
        ("¿Cómo se llama la lista de revisión de la clase?", "CSPWM", "Son las iniciales de cinco puntos de revisión."),
        ("¿Qué hago si algo falla en la revisión?", "Lo corrijo con otro color", "Así veo mis errores."),
        ("¿Qué letra de CSPWM revisa la ortografía?", "W", "W es words."),
    ],
    task("Mira esta imagen descrita: [un perro blanco sentado sobre una cama azul]. Con el modelo «The cat is black. It is on the sofa.» escribe dos oraciones sobre el perro (palabras: dog, white, bed). Luego revisa con CSPWM: marca cada letra cuando la hayas comprobado. Corrige con otro color. Cambia después una palabra (por ejemplo, el color) para crear otra versión y revísala igual.", "The dog is white. It is on the bed.", ["escribe dos oraciones con la estructura del modelo", "las oraciones coinciden con la imagen", "marca los cinco puntos de CSPWM", "corrige con otro color y crea una segunda versión revisada"], ["las dos versiones con la lista marcada", "nota de la persona que las leyó"], ["no revisar el punto final", "escribir algo que la imagen no muestra"], "La otra persona comprueba con la imagen que cada oración diga lo que se ve."),
    "Revisa en voz alta una oración tuya con las letras C, S, P, W y M.",
    "Escribe un par de oraciones sobre un animal de tu elección con el modelo de esta clase y revísalas con CSPWM.",
)

# ================================================================ OA 14
lesson(
    OA14, 1,
    "Las imágenes descritas en cada ejercicio, lápiz grafito, hojas para dibujar y una hoja con renglones.",
    "Aprenderé a escribir rótulos (labels) para imágenes de animales, objetos, partes de la casa, ocupaciones, lugares y comidas, con la palabra más precisa. Sirve para nombrar con claridad lo que veo.",
    ["Sé copiar y completar oraciones con un modelo.", "Sé palabras como dog, house y apple."],
    [
        "Un rótulo (label) es una palabra o frase corta que nombra lo que se ve en una imagen. Para escribir un buen rótulo, mira bien la imagen y elige la palabra más precisa. Si ves una cama y un velador, la palabra precisa es bedroom (dormitorio), no solo «room» (pieza). Si ves a una persona con estetoscopio, es doctor.",
        "Palabras útiles: animales (dog, cat, bird, fish), partes de la casa (kitchen, bedroom, bathroom, living room, garden), ocupaciones (teacher, doctor, cook, firefighter), lugares (library, school, park, market) y comidas (bread, rice, soup, apple, cheese). Con una sola cosa se escribe a o an: a dog, an apple. Con varias, la palabra lleva s: two dogs.",
        "Escribe el rótulo con ortografía correcta y con mayúscula solo si es nombre propio o inicio de oración. Revisa que el rótulo coincida con la imagen. Después de aprender a rotular, puedes escribir una oración corta: «It is a dog» (es un perro). Un rótulo es la base de una descripción.",
    ],
    [("label", "rótulo"), ("kitchen", "cocina"), ("bedroom", "dormitorio"), ("doctor", "doctor/a"), ("market", "mercado"), ("an", "un/una (antes de vocal)")],
    [
        ("Rotular una parte de la casa", "Imagen: [un refrigerador, un lavaplatos, una olla y una mesa]. Escribe el rótulo más preciso.", ["Miro los objetos: refrigerador, lavaplatos, olla, mesa.", "Eso es una cocina (kitchen).", "Uso la palabra más precisa."], "kitchen"),
        ("Rotular con a o an", "Imagen: [una manzana roja]. Escribe el rótulo con a o an.", ["Apple empieza con vocal.", "Uso an.", "Escribo la frase."], "an apple"),
    ],
    [
        ("Rotular con una palabra muy general como room.", "No dice cuál lugar de la casa es.", "Elige la palabra precisa: kitchen, bedroom o bathroom."),
        ("Escribir «a apple».", "Apple empieza con vocal.", "Escribe an apple."),
    ],
    [
        ("¿Qué significa «label»?", "Rótulo", "Un label nombra lo que hay en la imagen."),
        ("¿Cómo se dice «cocina» (lugar de la casa) en inglés?", "kitchen", "Kitchen es la cocina."),
        ("Imagen: [un gato]. ¿Qué rótulo corresponde? Escribe la palabra con a.", "a cat", "Cat es gato."),
    ],
    [
        ("Imagen: [una cama y un velador]. Elige el rótulo más preciso: (a) bedroom (b) room", "a", "Bedroom dice qué pieza es."),
        ("Imagen: [una persona con estetoscopio]. Elige el rótulo: (a) doctor (b) teacher", "a", "El estetoscopio es una pista de doctor."),
        ("Imagen: [un plato con arroz]. Elige el rótulo: (a) rice (b) soup", "a", "Rice es arroz."),
    ],
    [
        ("Imagen: [un huevo]. Escribe el rótulo con a o an.", "an egg", "Egg empieza con vocal."),
        ("Imagen: [tres perros]. Escribe el rótulo en inglés con el número en palabra: three y la cosa en plural.", "three dogs", "Con tres, dog lleva s."),
        ("Imagen: [una ducha y un lavamanos]. Escribe el rótulo en inglés de la parte de la casa.", "bathroom", "Ducha y lavamanos corresponden a bathroom."),
    ],
    [
        ("Ana rotuló [una biblioteca con estantes y libros] como market. ¿Qué rótulo es mejor? Responde en inglés.", "library", "La biblioteca tiene estantes con libros."),
        ("Leo rotuló [un libro de cocina y una olla] como bedroom. ¿Qué rótulo es mejor? Responde en inglés.", "kitchen", "Los objetos son de la cocina."),
    ],
    [
        ("Imagen: [una persona con gorro y casaca que apaga un incendio con una manguera]. Elige el rótulo: (a) firefighter (b) cook", "a", "Firefighter es bombero."),
        ("Imagen: [un pez en una pecera]. Escribe el rótulo del animal con a o an.", "a fish", "Fish empieza con consonante."),
    ],
    [("Haces un afiche de tu casa. Imagen: [una cama, una frazada y una lámpara de velador]. Escribe el rótulo para pegar bajo la imagen.", "bedroom", "La cama y la lámpara de velador son de un dormitorio.")],
    [
        ("¿Cómo se dice «mercado» en inglés?", "market", "Market es mercado."),
        ("¿Qué escribo antes de egg?", "an", "Egg empieza con vocal."),
        ("¿Qué escribo antes de dog?", "a", "Dog empieza con consonante."),
    ],
    task("Escribe un rótulo para cada una de estas seis imágenes descritas: (1) [un perro café], (2) [un refrigerador, un lavaplatos y una olla], (3) [una persona que da una clase frente a una pizarra], (4) [un plato con pan], (5) [una cama y un velador], (6) [una manzana verde]. Usa a o an cuando corresponda y elige la palabra más precisa. Luego dibuja dos de ellas y escribe su rótulo bajo el dibujo con mayúscula solo donde corresponda.", "(1) a dog (2) kitchen (3) teacher (4) bread (5) bedroom (6) an apple", ["escribe los seis rótulos", "usa a y an bien", "elige palabras precisas", "los rótulos coinciden con las imágenes y la ortografía es correcta"], ["los seis rótulos", "los dos dibujos rotulados"], ["usar room en lugar de bedroom", "escribir a apple"], "La otra persona dice qué imagen se imaginó con cada rótulo y se corrige el que no calza."),
    "Rotula tres objetos de tu casa en inglés con a o an.",
    "Dibuja una pieza de tu casa y rotula cinco cosas que veas en ella.",
)

lesson(
    OA14, 2,
    "Las imágenes descritas y los números escritos en cada ejercicio, lápiz grafito y una hoja con renglones.",
    "Aprenderé a escribir cómo se siente una persona de una imagen y cuántas cosas hay, con números hasta veinte. Sirve para describir emociones y cantidades con oraciones simples.",
    ["Sé rotular imágenes con a y an.", "Sé los números hasta veinte en inglés."],
    [
        "Para escribir un sentimiento (feeling) usa «am, is o are» y una palabra de sentimiento: «He is happy» (él está contento), «She is sad» (ella está triste), «I am tired» (estoy cansado), «He is angry» (él está enojado), «She is hungry» (ella tiene hambre). Los gestos de la cara y el cuerpo son pistas: una sonrisa significa happy.",
        "Para escribir cantidades usa «There is» para una cosa y «There are» para varias: «There are twelve stars» (hay doce estrellas). Los números en palabras son: 11 eleven, 12 twelve, 13 thirteen, 14 fourteen, 15 fifteen, 16 sixteen, 17 seventeen, 18 eighteen, 19 nineteen y 20 twenty. Cuida la ortografía: fifteen y twelve.",
        "Primero mira la imagen: ¿qué cara tiene la persona?, ¿cuántas cosas hay? Si hay grupos iguales, multiplica para saber el total. Después escribe la oración completa con mayúscula y punto. Revisa que el sentimiento y el número coincidan con la imagen.",
    ],
    [("feeling", "sentimiento"), ("happy", "contento/a"), ("sad", "triste"), ("tired", "cansado/a"), ("angry", "enojado/a"), ("There are...", "hay (varios)")],
    [
        ("Escribir un sentimiento", "Imagen: [un niño que sonríe con los brazos arriba]. Escribe una oración con el sentimiento.", ["Una sonrisa y brazos arriba son pistas de happy.", "Es un niño: He is.", "Escribo la oración."], "He is happy."),
        ("Escribir una cantidad", "Imagen: [tres filas de cuatro estrellas]. Escribe una oración con el total en palabras.", ["Hay 3 × 4 = 12 estrellas.", "12 en inglés es twelve.", "Son varias: There are."], "There are twelve stars."),
    ],
    [
        ("Escribir «fiveteen».", "La ortografía de quince es otra.", "Escribe fifteen: f-i-f-t-e-e-n."),
        ("Decir «There is twelve stars».", "Son varias estrellas y se usa are.", "Di There are twelve stars."),
    ],
    [
        ("¿Qué significa «tired»?", "Cansado", "Tired es cansado."),
        ("¿Cómo se dice «triste» en inglés?", "sad", "Sad es triste."),
        ("¿Cómo se escribe 15 en inglés?", "fifteen", "Fifteen es quince."),
    ],
    [
        ("Imagen: [una niña que llora]. Elige la oración: (a) «She is sad.» (b) «She is happy.»", "a", "Llorar es una pista de sad."),
        ("Imagen: [un niño que bosteza y se frota los ojos]. Elige la oración: (a) «He is tired.» (b) «He is angry.»", "a", "Bostezar es una pista de tired."),
        arith("Imagen: [dos grupos de nueve globos]. ¿Cuántos globos hay en total? Escribe el número.", "9 + 9", "Se suman los dos grupos."),
    ],
    [
        ("Escribe en inglés el resultado de 20 − 2.", "eighteen", "20 menos 2 es 18, que se escribe eighteen."),
        ("Imagen: [un niño con las cejas bajas y los puños cerrados]. Completa: «He is ___.» Opciones: angry / sad.", "angry", "Cejas bajas y puños cerrados son pistas de enojo."),
        ("Imagen: [un niño con un plato vacío que se toca el estómago]. Completa: «He is ___.» Opciones: hungry / happy.", "hungry", "El plato vacío es una pista de hambre."),
    ],
    [
        ("Luis escribió «There is sixteen apples» para [16 manzanas]. ¿Qué palabra corrige y por cuál? Responde en inglés.", "is por are", "Hay varias manzanas y se escribe There are sixteen apples."),
        ("Ana escribió «She is happy» para [una niña que llora]. ¿Qué palabra debe cambiar y por cuál? Responde en inglés.", "sad", "Llorar es una pista de sad."),
    ],
    [
        arith("Imagen: [cuatro filas de cuatro lápices]. ¿Cuántos lápices hay en total? Escribe el número.", "4 * 4", "Hay cuatro filas con cuatro lápices cada una."),
        ("Escribe la oración completa para [un niño que sonríe y 14 estrellas]: sentimiento y cantidad en dos oraciones separadas.", "He is happy. There are fourteen stars.", "Primero el sentimiento y luego la cantidad en palabras."),
    ],
    [("En un cartel del curso hay [18 sillas]. Escribe la oración que dice cuántas hay.", "There are eighteen chairs.", "18 se escribe eighteen y chairs lleva s.")],
    [
        ("¿Cómo se dice «enojado» en inglés?", "angry", "Angry es enojado."),
        ("¿Cómo se escribe 12 en inglés?", "twelve", "Twelve es doce."),
        ("¿Uso is o are con varias estrellas?", "are", "There are se usa con varias cosas."),
    ],
    task("Mira estas imágenes descritas y escribe una oración para cada una: (1) [una niña que sonríe], (2) [un niño que llora], (3) [un niño que bosteza], (4) [tres filas de cinco manzanas], (5) [dos grupos de ocho globos]. Calcula la cantidad total en (4) y (5) y escribe la oración con el número en palabras. Revisa que cada oración tenga mayúscula y punto y que coincida con la imagen.", "(1) She is happy. (2) He is sad. (3) He is tired. (4) There are fifteen apples. (5) There are sixteen balloons.", ["escribe cinco oraciones", "el sentimiento coincide con la pista de la imagen", "calcula bien 15 y 16 y los escribe en palabras", "usa There are y revisa mayúscula y punto"], ["las cinco oraciones", "nota de la persona que las revisó"], ["escribir fiveteen", "decir There is con varias cosas"], "La otra persona comprueba el cálculo y la ortografía de los números."),
    "Escribe en inglés cómo te sientes ahora con I am...",
    "Escribe cuatro oraciones sobre cómo se sienten personas de una imagen y cuántas cosas hay.",
)

lesson(
    OA14, 3,
    "Las escenas descritas en cada ejercicio, lápiz grafito, hojas para dibujar y tres objetos de tu casa para ubicar (un libro, una caja y una taza de plástico).",
    "Aprenderé a escribir dónde está un objeto usando in, on, under, next to, behind, in front of y between. Sirve para describir ubicaciones en una imagen con oraciones completas.",
    ["Sé rotular objetos en inglés.", "Sé on, in y under por lo básico."],
    [
        "Para escribir dónde está algo usa «It is» o «They are» más una palabra de lugar (preposition) y la referencia. Palabras de lugar: in (dentro de), on (sobre), under (debajo de), next to (al lado de), behind (detrás de), in front of (delante de) y between (entre dos cosas). Ejemplo: «The ball is under the table» (la pelota está debajo de la mesa).",
        "Para varias cosas, usa are: «The shoes are behind the door» (los zapatos están detrás de la puerta). La palabra between necesita dos referencias: «The ball is between the box and the chair» (la pelota está entre la caja y la silla). Las referencias llevan the: the box, the table.",
        "Para escribir sin errores, mira bien dónde está el objeto respecto de otro. Pregúntate: ¿está sobre?, ¿dentro?, ¿delante? Escribe la oración completa con mayúscula y punto. Un buen truco es colocar tú un libro, una caja y una taza de plástico y escribir dónde están.",
    ],
    [("in", "dentro de"), ("on", "sobre"), ("under", "debajo de"), ("next to", "al lado de"), ("behind", "detrás de"), ("between", "entre")],
    [
        ("Escribir una ubicación", "Imagen: [una pelota debajo de una mesa]. Escribe la oración.", ["La pelota es the ball.", "La ubicación es debajo: under.", "La referencia es the table."], "The ball is under the table."),
        ("Entre dos cosas", "Imagen: [una pelota con una caja a la izquierda y una silla a la derecha]. Escribe dónde está.", ["La pelota está en el medio.", "Uso between con dos referencias.", "Uno con and."], "The ball is between the box and the chair."),
    ],
    [
        ("Escribir «The ball is between the box» con una sola referencia.", "Between necesita dos referencias.", "Usa the box and the chair."),
        ("Usar in cuando algo está sobre una mesa.", "In es dentro, on es sobre.", "Mira si el objeto está encima o adentro."),
    ],
    [
        ("¿Qué significa «behind»?", "Detrás de", "Behind indica que algo está atrás."),
        ("¿Qué significa «between»?", "Entre", "Between necesita dos referencias."),
        ("¿Qué significa «in front of»?", "Delante de", "Indica que está al frente."),
    ],
    [
        ("Imagen: [un libro sobre una mesa]. Elige: (a) «The book is on the table.» (b) «The book is in the table.»", "a", "El libro está encima de la mesa."),
        ("Imagen: [un gato dentro de una caja]. Elige: (a) «The cat is in the box.» (b) «The cat is under the box.»", "a", "El gato está dentro."),
        ("Imagen: [una mochila detrás de una puerta]. Elige: (a) «The bag is behind the door.» (b) «The bag is in front of the door.»", "a", "Detrás es behind."),
    ],
    [
        ("Imagen: [un perro al lado de una casa]. Completa: «The dog is ___ to the house.»", "next", "Next to es al lado de."),
        ("Imagen: [una taza delante de un libro]. Escribe la oración completa con in front of: la taza (cup) y el libro (book).", "The cup is in front of the book.", "In front of significa delante de."),
        ("Imagen: [dos zapatos debajo de una cama]. Escribe la oración con the shoes y bed.", "The shoes are under the bed.", "Shoes es plural y bed se escribe con the."),
    ],
    [
        ("Luis escribió «The cat are on the sofa». ¿Cómo se corrige? Responde en inglés.", "The cat is on the sofa.", "Cat es una sola cosa y lleva is."),
        ("Ana vio [una pelota entre una caja y una silla] y escribió «The ball is behind the box». ¿Cuál palabra de lugar debería usar? Responde.", "between", "La pelota está en el medio de dos objetos."),
    ],
    [
        ("Ordena las palabras: is / The / table / the / under / ball. Escribe la oración.", "The ball is under the table.", "El orden es The ball is under the table."),
        ("Imagen: [una pelota sobre una caja, que está al lado de una silla]. Escribe dos oraciones: una sobre la pelota (ball) y la caja (box), y otra sobre la caja y la silla (chair).", "The ball is on the box. The box is next to the chair.", "Cada oración tiene su referencia."),
    ],
    [("En el cuaderno de tu cuarto escribes dónde guardaste la mochila. Imagen: [una mochila debajo de la mesa]. Escribe la oración con the bag y the table.", "The bag is under the table.", "Under es debajo de.")],
    [
        ("¿Cómo se dice «sobre» en inglés?", "on", "On es sobre."),
        ("¿Cómo se dice «al lado de» en inglés?", "next to", "Next to es al lado de."),
        ("¿Cuántas referencias necesita between?", "Dos", "Está entre dos cosas."),
    ],
    task("Escribe una oración para cada escena descrita: (1) [una pelota debajo de una mesa], (2) [un gato dentro de una caja], (3) [un libro sobre una silla], (4) [una taza al lado de un libro], (5) [una pelota entre una caja y una silla], (6) [dos zapatos detrás de una puerta]. Luego coloca un libro, una caja y una taza de plástico en una mesa y escribe dos oraciones sobre cómo quedaron (con on, next to, in front of o behind). Revisa mayúscula, espacios y punto.", "(1) The ball is under the table. (2) The cat is in the box. (5) The ball is between the box and the chair.", ["escribe las seis oraciones", "cada palabra de lugar coincide con la escena", "usa is y are bien", "revisa mayúscula, espacios y punto y escribe dos oraciones sobre su propia disposición"], ["las ocho oraciones", "nota de la persona que comparó con las escenas"], ["usar in en vez de on", "usar between con una sola referencia"], "Cambia la posición de un objeto y pide a la otra persona que escriba la nueva oración."),
    "Mira un objeto de tu pieza y di en inglés dónde está.",
    "Dibuja una escena con cinco objetos y escribe cinco oraciones sobre dónde está cada uno.",
)

lesson(
    OA14, 4,
    "Las imágenes descritas en cada ejercicio, lápiz grafito y una hoja con renglones.",
    "Aprenderé a escribir oraciones sobre lo que las personas hacen en una imagen en este momento, con am, is o are y la forma -ing. Sirve para describir acciones visibles con oraciones completas.",
    ["Sé describir lugares con in, on y under.", "Sé acciones como read, draw y play."],
    [
        "Para escribir una acción que ocurre ahora usa «is» o «are» más el verbo con -ing: «The girl is reading a book» (la niña está leyendo un libro). Con una persona usa is, con varias personas usa are: «The boys are playing soccer» (los niños están jugando fútbol). Con I usa am.",
        "Para formar la forma -ing: casi siempre se agrega ing (read-reading, draw-drawing, play-playing, eat-eating, sing-singing). Algunos verbos duplican la última letra (run-running, swim-swimming) y algunos pierden la e final (write-writing, make-making). Para preguntar: «What is the girl doing?» (¿qué está haciendo la niña?).",
        "Mira la imagen y responde tres preguntas: ¿quién actúa?, ¿cuántas personas son?, ¿qué hacen? Escribe una oración con una persona o más y revisa la forma -ing. Si hay un objeto, agrégalo: reading a book. Escribe solo lo que se ve; no inventes acciones que la imagen no muestra.",
    ],
    [("is reading", "está leyendo"), ("are playing", "están jugando"), ("What is she doing?", "¿qué está haciendo ella?"), ("running", "corriendo"), ("swimming", "nadando"), ("writing", "escribiendo")],
    [
        ("Describir una acción", "Imagen: [una niña que lee un libro]. Escribe la oración.", ["Es una niña: The girl is.", "El verbo read en -ing es reading.", "Agrego el objeto: a book."], "The girl is reading a book."),
        ("Varias personas", "Imagen: [dos niños que juegan]. Escribe la oración.", ["Son varios: The boys are.", "Play en -ing es playing.", "Uno todo."], "The boys are playing."),
    ],
    [
        ("Escribir «The boys is playing».", "Los boys son varios y llevan are.", "Di The boys are playing."),
        ("Escribir «He is runing».", "Run duplica la n.", "Escribe running."),
    ],
    [
        ("¿Cómo se escribe «nadando» en inglés?", "swimming", "Swim duplica la m."),
        ("¿Qué significa «The girl is drawing»?", "La niña está dibujando", "Is drawing indica una acción ahora."),
        ("¿Qué significa «What is she doing?»", "¿Qué está haciendo ella?", "Pregunta por la acción."),
    ],
    [
        ("Imagen: [un niño que come un pan]. Elige: (a) «The boy is eating bread.» (b) «The boy is eat bread.»", "a", "Se necesita is y eating."),
        ("Imagen: [tres niñas que cantan]. Elige: (a) «The girls are singing.» (b) «The girls is singing.»", "a", "Girls es plural y lleva are."),
        ("Imagen: [una niña que escribe en su cuaderno]. Elige la escritura correcta: (a) writing (b) writeing", "a", "Write pierde la e y queda writing."),
    ],
    [
        ("Completa con swim en -ing: «The fish is ___.»", "swimming", "Swim duplica la m y agrega ing."),
        ("Imagen: [un niño que corre en el patio]. Escribe la oración con the boy y run en -ing.", "The boy is running.", "Run se escribe running."),
        ("Imagen: [dos niñas que dibujan]. Escribe la oración con the girls.", "The girls are drawing.", "Son dos personas y se usa are."),
    ],
    [
        ("Ana escribió «The girl are reading». ¿Cómo se corrige? Responde en inglés.", "The girl is reading.", "Girl es una persona y lleva is."),
        ("Leo escribió «The boy is sleeping» para [un niño que juega a la pelota]. ¿Qué verbo en -ing debe usar, a partir del verbo play? Responde en inglés.", "playing", "La imagen muestra a un niño jugando."),
    ],
    [
        ("Ordena las palabras: is / The / drawing / girl / a / picture. Escribe la oración.", "The girl is drawing a picture.", "El orden es The girl is drawing a picture."),
        ("Imagen: [un niño que lee y una niña que dibuja]. Escribe dos oraciones, una para cada uno.", "The boy is reading. The girl is drawing.", "Cada oración describe una acción visible."),
    ],
    [("En un diario de clase escribes lo que ves en una imagen: [dos niños que corren por el parque]. Escribe la oración con the boys.", "The boys are running in the park.", "Boys es plural y run se escribe running.")],
    [
        ("¿Cómo se escribe «leyendo» en inglés?", "reading", "Reading es leyendo."),
        ("¿Qué palabra va con varias personas: is o are?", "are", "Are se usa con varias personas."),
        ("¿Cómo se escribe «corriendo» en inglés?", "running", "Run duplica la n."),
    ],
    task("Escribe una oración para cada imagen descrita: (1) [una niña que lee un libro], (2) [dos niños que juegan fútbol (soccer)], (3) [un niño que corre], (4) [una niña que escribe una carta], (5) [tres niñas que cantan]. Usa is o are y la forma -ing. Luego escribe la pregunta «What is the girl doing?» y su respuesta para la imagen (1). Revisa mayúscula, espacios y punto.", "(1) The girl is reading a book. (2) The boys are playing soccer. (3) The boy is running. (5) The girls are singing.", ["escribe las cinco oraciones", "usa is y are correctamente", "forma bien running, writing y reading", "escribe la pregunta y su respuesta"], ["las cinco oraciones y la pregunta", "nota de la persona que las revisó"], ["decir The boys is playing", "escribir runing"], "La otra persona comprueba cada forma -ing con la imagen."),
    "Mira una imagen de un libro y di en inglés qué hace una persona.",
    "Escribe cinco oraciones sobre lo que hacen personas en una imagen que tengas en casa.",
)

lesson(
    OA14, 5,
    "La imagen descrita, el modelo de ficha y la lista de revisión escritos en esta clase, lápiz grafito, lápiz de otro color y una hoja.",
    "Aprenderé a crear una mini ficha de información con una imagen, un rótulo y tres oraciones, y a revisarla antes de entregarla. Sirve para reunir lo aprendido en una producción escrita completa.",
    ["Sé rotular, escribir sentimientos, cantidades, ubicaciones y acciones.", "Sé revisar con CSPWM."],
    [
        "Una ficha de información (information card) reúne una imagen, un rótulo y oraciones sobre lo que se ve. Modelo de ficha para la imagen [un loro verde sobre una rama con cinco hojas]: Título: «A green parrot». Oraciones: «It is a parrot. It is on a branch. There are five leaves.» (parrot es loro; branch es rama; leaves son hojas).",
        "Cada oración cumple una función. La primera identifica el animal (It is a...). La segunda dice dónde está o qué hace (It is on...). La tercera dice una cantidad o un sentimiento (There are... o It is happy). Escribe solo lo que se ve. No inventes datos que la imagen no muestra.",
        "Después de escribir, revisa con CSPWM y con una pregunta más: ¿cada oración coincide con la imagen? Corrige con otro color. Revisar es crear una segunda versión mejor. Una ficha final limpia, con título, imagen dibujada y tres oraciones correctas, es un buen trabajo.",
    ],
    [("information card", "ficha de información"), ("title", "título"), ("parrot", "loro"), ("branch", "rama"), ("leaves", "hojas"), ("revise", "mejorar al revisar")],
    [
        ("Escribir la ficha", "Imagen: [un gato gris sobre una silla]. Escribe título y dos oraciones.", ["Título con un adjetivo y el animal.", "Oración 1: identifico al animal.", "Oración 2: digo dónde está."], "Título: A gray cat. It is a cat. It is on the chair."),
        ("Revisar un borrador", "Borrador: «the cat is gray It is in the chair.» Imagen: [un gato gris sobre una silla]. ¿Qué corriges?", ["Falta mayúscula en The y un punto tras gray.", "La imagen muestra el gato sobre la silla, no dentro.", "Corrijo in por on."], "Corrijo: The cat is gray. It is on the chair."),
    ],
    [
        ("Escribir datos que la imagen no muestra.", "La ficha deja de ser verdadera.", "Escribe solo lo que se ve."),
        ("Entregar la ficha sin revisarla con CSPWM.", "Se quedan errores sin corregir.", "Revisa mayúscula, espacios, punto, ortografía y sentido."),
    ],
    [
        ("¿Qué es una «information card»?", "Una ficha de información", "Reúne un título y oraciones sobre una imagen."),
        ("¿Qué significa «title»?", "Título", "El título nombra la ficha."),
        ("¿Qué dice la primera oración de la ficha modelo?", "Identifica el animal", "Dice It is a parrot."),
    ],
    [
        ("Imagen: [un perro café sentado]. Elige el título: (a) A brown dog (b) A green fish", "a", "El título debe coincidir con la imagen."),
        ("Imagen: [un loro sobre una rama]. Elige la oración de ubicación: (a) «It is on a branch.» (b) «It is under a branch.»", "a", "Está sobre la rama."),
        ("¿Cuántas oraciones tiene la ficha modelo del loro? Escribe el número.", "3", "Son: It is a parrot; It is on a branch; There are five leaves."),
    ],
    [
        ("Ficha del loro. Completa: «There are ___ leaves.» (cinco en inglés)", "five", "La imagen muestra cinco hojas."),
        ("Imagen: [un gato gris sobre una silla]. Escribe la oración que dice dónde está el gato (cat) con the chair.", "The cat is on the chair.", "Está sobre la silla."),
        ("Borrador: «The cat is gray» sin punto. ¿Qué letra de CSPWM falla? Responde.", "P", "Falta el punto al final."),
    ],
    [
        ("Ana escribió «It is a fish» para [un loro]. ¿Qué letra de CSPWM falla? Responde.", "M", "La oración no coincide con la imagen."),
        ("Leo escribió «There is five leaves». ¿Cómo se corrige? Responde en inglés.", "There are five leaves.", "Son varias hojas y se usa are."),
    ],
    [
        ("Imagen: [un conejo blanco dentro de una caja con tres zanahorias]. Escribe una ficha con título y tres oraciones. Banco: rabbit, white, box, three, carrots.", "A white rabbit. It is a rabbit. It is in a box. There are three carrots.", "Cada oración tiene una función: identificar, ubicar y contar."),
        ("Ordena las oraciones de la ficha con los números: (1) It is on a branch. (2) A green parrot. (3) It is a parrot. (Título, identificación, ubicación)", "2, 3, 1", "Primero va el título, luego la identificación y después la ubicación."),
    ],
    [("Preparas una ficha para la feria de ciencias. Imagen: [un pez naranja en una pecera con dos piedras]. Escribe la oración que dice la cantidad de piedras (stones).", "There are two stones.", "La imagen muestra dos piedras.")],
    [
        ("¿Cómo se dice «rama» en inglés?", "branch", "Branch es rama."),
        ("¿Qué función tiene la tercera oración de la ficha?", "Dice una cantidad o un sentimiento", "Complementa la descripción."),
        ("¿Qué hago después de escribir la ficha?", "La reviso con CSPWM", "Así encuentro y corrijo errores."),
    ],
    task("Mira esta imagen descrita: [un pájaro azul sobre una rama con cuatro hojas]. Escribe una mini ficha de información en una hoja: un título, y tres oraciones (identificar el animal, decir dónde está, decir cuántas hojas hay). Palabras: bird, blue, branch, four, leaves. Dibuja la imagen sobre tu ficha. Revisa con CSPWM, corrige con otro color y pasa la ficha en limpio. Pide a una persona de tu casa que compare tu ficha con la imagen.", "Título: A blue bird. It is a bird. It is on a branch. There are four leaves.", ["tiene título y tres oraciones", "las oraciones coinciden con la imagen", "revisa con CSPWM y corrige con otro color", "pasa en limpio una versión final"], ["borrador corregido y ficha final con dibujo", "nota de la persona que comparó con la imagen"], ["escribir datos que la imagen no muestra", "no revisar el punto final"], "La otra persona compara cada oración con la imagen y señala la que no coincide."),
    "Di en inglés una oración que describa un objeto de tu casa.",
    "Haz otra ficha con una imagen que dibujes tú y revísala con CSPWM.",
)

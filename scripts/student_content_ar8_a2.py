"""Cuaderno del estudiante de 8.º básico Artes Visuales: AR08 OA 02 (impresión, papel y textil con materiales sustentables)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA2 = "AR08 OA 02"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Hojas, lápiz de mina, papel de diario limpio y, si los tienes, trozos de cartón y restos de tela limpios. Los tres referentes están descritos en esta clase.",
    "Aprenderé a observar trabajos de impresión, papel y textil hechos con materiales sustentables y a elegir un recurso sin copiar. Sirve para empezar un trabajo propio con materiales que ya tuvieron un uso.",
    ["Sé que reinterpretar es tomar un recurso y cambiar lo demás.", "Sé registrar dos detalles, una pregunta y una posibilidad."],
    [
        "La impresión es el proceso de pasar una imagen desde una matriz, que es la pieza que lleva la imagen, a otra superficie. Puedo estampar con una matriz de cartón con formas pegadas, con una hoja con relieve o con el borde de un objeto. El papel se puede reciclar, es decir, volver a usar papel ya usado para hacer papel nuevo o soportes nuevos. El textil es cualquier material hecho de fibras, como una tela o un hilo; se puede remendar, trenzar, estampar o teñir.",
        "Un material es sustentable cuando se puede reutilizar, reciclar o renovar, y su uso daña poco el entorno. Un papel de diario usado, un resto de tela de una camisa vieja o un cartón de caja son ejemplos. Un referente puede enseñarme recursos como repetir una forma para crear ritmo, usar un material de desecho como soporte o dejar visibles los remiendos.",
        "Observar sin copiar es elegir un recurso y cambiar lo demás. Si veo una bolsa estampada con huellas de hojas, puedo tomar la idea de repetir una huella y estampar otra cosa. Anoto dos detalles, una pregunta y una posibilidad propia, y también la procedencia del referente. Un referente es una elección de su autor: no muestra todas las maneras de trabajar con ese material.",
    ],
    [("impresión", "proceso de pasar una imagen desde una matriz a otra superficie"), ("matriz", "pieza que lleva la imagen que se va a estampar"), ("textil", "material hecho de fibras, como una tela o un hilo"), ("sustentable", "que se puede reutilizar, reciclar o renovar y daña poco el entorno"), ("reciclar", "volver a usar un material ya usado para hacer algo nuevo")],
    [
        w("Registro de un referente", "Referente de ejemplo: una bolsa de tela estampada con huellas de hojas de colores, hecha con restos de una camisa. Registra dos detalles, una pregunta y una posibilidad.", ["Detalle 1: la tela es un resto de camisa.", "Detalle 2: las huellas de hojas se repiten en filas.", "Pregunta: ¿por qué el autor eligió huellas de hojas?", "Posibilidad: estampar en filas la base de un vaso de cartón en vez de hojas."], "Dos detalles (resto de camisa, huellas repetidas), una pregunta sobre las hojas y una posibilidad propia que toma la repetición sin copiar las hojas"),
        w("Copia o reinterpretación", "Referente de ejemplo: un afiche impreso con una matriz de cartón sobre papel de diario, con la silueta de un pájaro. Gonzalo pega otra silueta de pájaro igual en su matriz y la estampa sobre diario. Ema usa una matriz de cartón para estampar un patrón de ondas repetidas sobre una tela. ¿Quién copia y quién reinterpreta?", ["Gonzalo repite la figura, la matriz y el soporte.", "Ema conserva solo el recurso de la matriz de cartón.", "Ema cambia la figura y el soporte."], "Gonzalo copia; Ema reinterpreta"),
    ],
    [
        m("Pensar que un material es sustentable solo porque se ve «natural» o es de color verde.", "El color o el aspecto no dicen si el material se reutiliza ni cuánto daña el entorno.", "Pregunta si el material ya tuvo un uso, si se recicla o si se puede renovar."),
        m("Tomar un referente de impresión como la única manera de trabajar con ese material.", "Un referente solo muestra las decisiones de su autor.", "Anota qué recurso te sirve y qué otras decisiones podrías tomar tú."),
    ],
    [
        ex("Un cuaderno de ejemplo tiene hojas hechas con papel reciclado. ¿Qué significa reciclar papel?", "Volver a usar papel ya usado para hacer papel o soportes nuevos", "El papel recibe un segundo uso en vez de botarse."),
        ex("En impresión, ¿cómo se llama la pieza que lleva la imagen y se estampa sobre otra superficie?", "Matriz", "Es la pieza que transfiere la imagen a la superficie final."),
        ex("¿Cuál de estos materiales es un textil? A. Un resto de camisa B. Una hoja de diario.", "A", "Una tela es un material hecho de fibras; el diario es papel."),
    ],
    [
        ex("Una bolsa de ejemplo está hecha con restos de una camisa vieja y estampada con huellas de hojas. ¿Qué la hace sustentable? A. Reutiliza una tela que ya había tenido un uso B. Tiene colores vivos.", "A", "El material se vuelve a usar en vez de botarse."),
        ex("Tres anotaciones sobre la bolsa: 1) «Las huellas se repiten en filas». 2) «Es muy linda». 3) «La tela es un resto de camisa». ¿Cuántas son detalles comprobables?", "2", "La 1 y la 3 se ven; «linda» es una opinión."),
        ex("Una compañera dice que el afiche con matriz de cartón enseña la única manera de imprimir. ¿Qué problema tiene su frase?", "Un referente muestra solo una elección de su autor", "No muestra todas las maneras de imprimir con ese material."),
    ],
    [
        ex("Quieres tomar el recurso de repetir una huella de la bolsa estampada con hojas. ¿Qué plan lo reinterpreta? A. Estampar en fila la base de un vaso de cartón mojada en témpera B. Estampar las mismas hojas, con los mismos colores y la misma disposición.", "A", "Conserva la repetición y cambia el objeto; la otra opción es la bolsa repetida."),
        ex("Tienes una caja de cartón, diario usado, témpera nueva y un resto de camiseta. ¿Cuántos de estos materiales son reutilizados?", "3", "El cartón, el diario y la camiseta ya tuvieron un uso; la témpera es nueva."),
        ex("Para imprimir con matriz de cartón necesitas un soporte reutilizado. ¿Cuál sirve? A. Una hoja de diario B. Una hoja de cuaderno nueva sin usar.", "A", "El diario ya fue usado; la hoja nueva no."),
    ],
    [
        ex("Un cuaderno de ejemplo tiene tapa de tela remendada con remiendos visibles y hojas de papel reciclado. ¿Cuál de los referentes enseña el recurso de dejar visibles los remiendos: el cuaderno o el afiche impreso sobre diario?", "El cuaderno", "Su tapa muestra remiendos; el afiche no los menciona."),
        ex("Una compañera afirma: «Mi cuaderno es sustentable porque tiene la tapa verde». ¿Es correcta su razón?", "No", "El color no dice si un material se reutiliza."),
    ],
    [
        ex("Tu criterio es reutilizar materiales para un afiche. Propuesta X: matriz de cartón sobre papel de diario. Propuesta Y: tela nueva y papel blanco nuevo. ¿Cuál cumple tu criterio?", "X", "El cartón y el diario ya tuvieron un uso; en Y todo es nuevo."),
        ex("Una estudiante imprime con matriz de cartón tomando ese recurso de un afiche de ejemplo. En su ficha escribió solo el título y los materiales. ¿Qué dato falta para saber de dónde viene el recurso?", "La procedencia del referente", "Se anota de qué referente se tomó el recurso."),
    ],
    ex("Para una feria escolar de reciclaje debes decorar bolsas de tela usadas. Tienes de referente la bolsa estampada con huellas de hojas. ¿Qué plan reinterpreta y declara la procedencia? A. Estampar bases de vasos de cartón en filas y anotar que la repetición viene de ese referente B. Pintar hojas idénticas y firmar sin mencionar el referente.", "A", "Cambia el objeto de la huella y declara de dónde viene el recurso."),
    [
        ex("En impresión, ¿qué es una matriz?", "La pieza que lleva la imagen que se estampa", "Transfiere la imagen a otra superficie."),
        ex("Verdadero o falso: un material es sustentable solo si es nuevo.", "Falso", "Un material reutilizado o reciclado puede ser sustentable."),
        ex("En Artes Visuales, ¿qué es un textil?", "Un material hecho de fibras, como una tela o un hilo", "Se puede estampar, teñir, trenzar o remendar."),
    ],
    task(
        "Elige UN referente de ejemplo. A) Una bolsa de tela hecha con restos de camisa, estampada con huellas de hojas de colores en filas. B) Un afiche impreso con una matriz de cartón sobre papel de diario, con la silueta de un pájaro. C) Un cuaderno de ejemplo con tapa de tela remendada y hojas de papel reciclado, cosido con hilo grueso. En tu bitácora anota dos detalles, una pregunta y la procedencia. Luego haz dos bocetos que reinterpreten recursos distintos con materiales reutilizados y señala cuál elegirías.",
        "Elegí la A. Detalles: la tela es un resto de camisa; las huellas están en filas. Pregunta: ¿por qué hojas y no otro objeto? Procedencia: bolsa de ejemplo de esta clase. Boceto 1: filas de círculos hechos con la base de un vaso. Boceto 2: filas de cuadrados de cartón. Elijo el 1 porque se ve el ritmo.",
        ["registra dos detalles, una pregunta y la procedencia", "hace dos bocetos con recursos distintos", "usa materiales reutilizados", "no copia las formas del referente"],
        ["bitácora de observación", "dos bocetos", "elección anotada"],
        ["repetir las hojas del referente", "llamar sustentable a un material por su color"],
        "Pregunta qué recurso tomó y qué material reutilizado eligió en vez del del referente.",
    ),
    "Busca en tu casa un objeto hecho de papel o tela que se haya reutilizado y di en voz alta qué uso tuvo antes.",
    "Elige un recurso de impresión y explica en tres frases cómo cambiaría si lo hicieras sobre tela en vez de sobre papel.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Hojas y lápiz. Las tres fichas de trabajos están escritas en esta clase; no necesitas buscarlas.",
    "Aprenderé a investigar el contexto, el material y el propósito de trabajos de impresión, papel y textil, y a juzgar qué tan sustentable es un material con cuatro preguntas. Sirve para elegir materiales con razones.",
    ["Sé separar datos de inferencias.", "Sé que un material sustentable se reutiliza, se recicla o se renueva."],
    [
        "Para elegir un material sustentable me hago cuatro preguntas: ¿reutiliza o recicla algo que ya se usó?, ¿se puede usar muchas veces?, ¿deja pocos residuos? y ¿es seguro de manipular? Una bolsa de tela hecha con restos de una sábana cumple las dos primeras; una bolsa de un solo uso, no. Un residuo es lo que sobra y se bota. Para saber si es seguro, uso materiales escolares como la témpera y evito productos fuertes.",
        "El propósito del trabajo cambia lo que necesito del material. Una bolsa que se usa todos los días debe resistir el peso y el roce; un afiche que invita a una feria debe imprimirse con nitidez y leerse bien; una cortina de tiras debe ser flexible. Además, el contexto importa: una feria de trueque, donde se intercambian cosas sin usar dinero, combina bien con materiales de segundo uso.",
        "Cuando una ficha no dice algo, no lo invento. Si la ficha no dice cuánto dura un trabajo, lo marco como pendiente. Separo los datos que aparecen escritos de las inferencias que yo deduzco. «Está impreso en papel reciclado» es un dato; «así se usó menos papel nuevo» es una inferencia. Con eso decido qué material me conviene para mi propósito.",
    ],
    [("residuo", "lo que sobra de un proceso y se bota"), ("trueque", "intercambio de cosas sin usar dinero"), ("durable", "que resiste el uso y dura mucho tiempo"), ("propósito", "para qué se hace un trabajo"), ("criterio", "pregunta o regla que uso para decidir")],
    [
        w("Aplicar las preguntas", "Ficha de ejemplo: «Bolsa de tela para el pan, hecha con restos de sábana, estampada a mano, pensada para usarse muchas veces». ¿Qué preguntas de sustentabilidad responde la ficha?", ["Reutiliza: sí, usa restos de sábana.", "Se usa muchas veces: sí, la ficha lo dice.", "Residuos y seguridad: la ficha no lo dice."], "Responde dos: reutiliza y se usa muchas veces; quedan pendientes residuos y seguridad"),
        w("Material y propósito", "Debes elegir un material para un afiche de una feria de trueque. Tienes cartón de caja y cartulina brillante nueva. ¿Cuál eliges?", ["El propósito es invitar a intercambiar cosas ya usadas.", "El cartón de caja reutiliza un material.", "El material mismo respalda el mensaje."], "El cartón de caja, porque reutiliza un material y refuerza el mensaje"),
    ],
    [
        m("Decir que un material es sustentable sin responder ninguna de las cuatro preguntas.", "Sin preguntas, la afirmación no tiene respaldo.", "Responde las cuatro preguntas y anota cuáles quedan pendientes."),
        m("Elegir el mismo material para cualquier propósito.", "Una bolsa y un afiche necesitan cualidades distintas.", "Primero define el propósito y después revisa qué cualidad necesita el material."),
    ],
    [
        ex("Ficha de ejemplo: «Cortina de tiras de tela de ropa en desuso, trenzadas». ¿Cuál es su material?", "Tela de ropa en desuso", "La ficha nombra el material con que está hecha."),
        ex("Un material que se usa muchas veces antes de botarse, ¿es más o menos sustentable que uno de un solo uso?", "Más sustentable", "Genera menos residuos por cada uso."),
        ex("Ficha: «Afiche impreso con matriz de cartón, para invitar a una feria de trueque». ¿Cuál es su propósito? A. Invitar a una feria de trueque B. Imprimir con matriz de cartón.", "A", "El propósito es para qué se hizo; la matriz es el procedimiento."),
    ],
    [
        ex("Ficha: «Bolsa de tela para el pan, hecha con restos de sábana, estampada a mano, pensada para usarse muchas veces». De las cuatro preguntas de sustentabilidad (reutiliza, se usa muchas veces, deja pocos residuos, es seguro), ¿a cuántas responde la ficha con un dato?", "2", "Responde que reutiliza (restos de sábana) y que se usa muchas veces; residuos y seguridad no aparecen."),
        ex("Una bolsa para el pan debe resistir peso y roce. ¿Qué cualidad del material importa más? A. Resistencia al uso repetido B. Que sea muy liso.", "A", "Una bolsa de uso diario debe durar."),
        ex("La ficha del afiche dice que está impreso en papel reciclado. ¿Cuál es una inferencia? A. Está impreso en papel reciclado B. Seguramente así se usó menos papel nuevo.", "B", "La ficha no afirma que se haya usado menos papel nuevo."),
    ],
    [
        arith("Una persona de ejemplo usa una bolsa de tela 3 veces por semana. ¿Cuántas veces la usa en 8 semanas?", "3*8", "Se multiplican los usos por semana por las semanas."),
        arith("Una cortina necesita 6 tiras de tela y cada tira mide 45 cm. ¿Cuántos centímetros de tela necesitas en total?", "6*45", "Se multiplica la cantidad de tiras por el largo de cada una."),
        ex("Vas a imprimir un afiche con matriz de cartón y necesitas una tinta fácil de lavar y segura. ¿Cuál eliges? A. Témpera escolar B. Pintura de aceite.", "A", "La témpera escolar es segura y se lava con agua."),
    ],
    [
        ex("Para una bolsa que se usará todos los días, ¿qué propuesta cumple mejor el propósito y la sustentabilidad? X) Papel de diario pegado con cola. Y) Tela resistente de ropa en desuso.", "Y", "Reutiliza tela y resiste el uso repetido; el papel se rompe fácil."),
        ex("Una compañera dice: «Mi afiche es sustentable porque es verde». ¿Por qué no basta su razón?", "El color no dice si el material se reutiliza ni cuánto dura", "Falta responder las preguntas de reutilización y durabilidad."),
    ],
    [
        ex("La ficha dice solo que la cortina de tiras reutiliza tela de ropa en desuso. ¿Qué criterios quedan pendientes por investigar?", "Cuánto dura, qué residuos deja y si es seguro", "La ficha solo responde a la pregunta de reutilización."),
        ex("Debes justificar por escrito el uso de papel reciclado en un afiche, relacionando material y propósito. ¿Cuál frase lo hace? A. «Usé papel reciclado porque el afiche invita a reutilizar y el soporte también lo muestra» B. «Usé papel reciclado porque me gusta».", "A", "Relaciona el material con el propósito del afiche."),
    ],
    ex("Tu curso prepara carteles para una feria de trueque del barrio, donde se intercambian cosas sin dinero. Tienes cajas de cartón de la sala y papel de diario. ¿Qué plan une mejor el material con el propósito? A. Estampar el cartel sobre cartón de caja con la frase «trae lo que ya no usas», porque el material habla de reutilizar B. Comprar cartulina brillante porque llama más la atención.", "A", "El soporte reutilizado refuerza el mensaje de segundo uso."),
    [
        ex("¿Cuáles son las cuatro preguntas para juzgar un material sustentable?", "Si reutiliza o recicla, si se usa muchas veces, si deja pocos residuos y si es seguro", "Son los criterios de la clase."),
        ex("Verdadero o falso: si la ficha no dice un dato, puedo inventarlo.", "Falso", "Un dato que falta se marca como pendiente."),
        ex("¿Qué es un trueque?", "Un intercambio de cosas sin usar dinero", "Es un tipo de intercambio entre personas."),
    ],
    task(
        "Elige UNA ficha. A) Bolsa de tela para el pan, hecha con restos de sábana, estampada a mano, para usarse muchas veces. B) Afiche impreso con matriz de cartón sobre papel reciclado, para invitar a una feria de trueque. C) Cortina de tiras de tela de ropa en desuso, trenzadas, para separar un rincón de taller. Haz una tabla con contexto, material y propósito; responde las cuatro preguntas de sustentabilidad marcando con «pendiente» las que la ficha no responde; y escribe qué material usarías tú para un trabajo con el mismo propósito.",
        "Elegí la B. Contexto: feria de trueque. Material: papel reciclado y matriz de cartón. Propósito: invitar a la feria. Preguntas: reutiliza, sí; se usa muchas veces, pendiente; residuos, pendiente; seguridad, pendiente. Mi material: cartón de caja desarmado, porque el mensaje es reutilizar.",
        ["completa contexto, material y propósito con datos de la ficha", "responde las cuatro preguntas y marca lo pendiente", "elige un material con una razón", "no inventa datos"],
        ["tabla de tres columnas", "lista de las cuatro preguntas", "material elegido con su razón"],
        ["declarar sustentable sin responder las preguntas", "inventar datos que la ficha no entrega"],
        "Señala una pregunta que quedó pendiente y pregunta dónde podrías buscar la respuesta.",
    ),
    "Mira una bolsa o un envoltorio de tu casa y di en voz alta si se podría reutilizar y para qué.",
    "Escribe dos propósitos distintos para una misma tela usada y explica qué cualidad del material importaría más en cada uno.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Papel de diario, cartón de caja, cola fría, témpera, una bandeja plástica limpia o un plato plano y restos de tela. Para hacer papel reciclado necesitas agua; pide ayuda a una persona adulta si usas agua tibia.",
    "Aprenderé procedimientos de impresión, papel y textil con materiales sustentables, y cómo decisiones como la cantidad de tinta, la presión y la repetición cambian el resultado. Sirve para decidir con pruebas antes de la obra final.",
    ["Sé que una matriz lleva la imagen que se estampa.", "Sé cambiar una sola variable al hacer pruebas."],
    [
        "En una matriz de cartón, las formas pegadas sobresalen y son las que reciben la tinta. Al estampar, la imagen sale invertida, como en un espejo: lo que está a la derecha en la matriz queda a la izquierda en el papel. Por eso las letras se pegan al revés para que se lean bien. La monotipia es otro procedimiento: pinto sobre una superficie lisa, apoyo el papel y la imagen se transfiere; cada copia sale distinta.",
        "Para hacer papel reciclado rasgo papel usado con las manos, lo remojo en agua hasta que se ablande, lo deshago hasta formar una pasta, lo extiendo en una capa delgada y lo dejo secar. En textil puedo trenzar tres tiras de tela, o teñir por amarre: amarro con elástico una tira antes de sumergirla en té o café fuerte y ya frío; la zona amarrada queda más clara porque el líquido llega menos.",
        "Las decisiones cambian el efecto. Con poca tinta y poca presión la huella sale pálida y con huecos; con demasiada tinta se mancha y pierde detalle; con tinta moderada y presión firme sale completa. Repetir una forma con espacios iguales crea ritmo; alternar dos formas crea un patrón. Pruebo en retazos y cambio una sola variable por prueba.",
    ],
    [("monotipia", "impresión en que se pinta sobre una superficie lisa y se transfiere la imagen al papel; cada copia es distinta"), ("invertida", "dada vuelta como en un espejo, con izquierda y derecha cambiadas"), ("ritmo", "repetición ordenada de formas o espacios"), ("patrón", "conjunto de formas que se repite siguiendo un orden"), ("pasta de papel", "papel remojado y deshecho que se extiende para formar una hoja nueva")],
    [
        w("La imagen sale al revés", "Pegas una flecha de cartón en tu matriz apuntando hacia la derecha. ¿Hacia dónde apuntará al estamparla?", ["La estampa invierte izquierda y derecha, como un espejo.", "Lo que apunta a la derecha en la matriz apunta a la izquierda en el papel."], "Hacia la izquierda"),
        w("Cuántos sellos caben", "Una tira de 22 cm se estampará con sellos de 3 cm separados por espacios de 2 cm, empezando y terminando con un sello. ¿Cuántos sellos caben?", ["Cada sello necesita 3 cm y su espacio de 2 cm: 5 cm.", "Sumo un espacio al largo de la tira porque el último sello no lleva espacio: 22 + 2 = 24.", "Divido 24 entre 5 y me quedo con la parte entera: 4."], "4 sellos (4 × 3 + 3 × 2 = 18 cm)"),
    ],
    [
        m("Pegar las letras en la matriz tal como se leen y esperar que se lean bien al estampar.", "La estampa invierte izquierda y derecha.", "Pega las letras en espejo para que impresas se lean correctamente."),
        m("Cargar la matriz con mucha tinta para que se vea más fuerte.", "El exceso se mancha y borra los detalles.", "Usa tinta moderada y presiona firme y parejo."),
    ],
    [
        ex("Pegas en una matriz de cartón la letra «b» y la estampas. ¿Qué letra se ve impresa en el papel?", "d", "La estampa invierte izquierda y derecha, y la «b» queda como «d»."),
        ex("En una matriz de cartón con formas pegadas, ¿qué partes reciben la tinta?", "Las formas pegadas, que sobresalen", "Solo lo que sobresale toca el papel."),
        ex("Para hacer papel reciclado, ¿qué haces primero con el papel usado: lo rasgas y lo remojas, o lo planchas?", "Lo rasgas y lo remojas", "Hay que ablandarlo para deshacerlo y formar la pasta."),
    ],
    [
        ex("Pones tinta sobre una bandeja lisa de plástico, dibujas con un palito sobre la tinta y apoyas un papel encima. ¿Cómo se llama este procedimiento? A. Monotipia B. Frottage.", "A", "Se pinta sobre una superficie lisa y se transfiere; cada copia sale distinta."),
        ex("Estampas una flecha que en la matriz apunta hacia arriba y a la derecha. ¿Hacia dónde apunta en el papel?", "Hacia arriba y a la izquierda", "Se invierten izquierda y derecha; arriba y abajo no cambian."),
        ex("Si estampas con demasiada tinta, ¿qué efecto produce? A. Las formas se manchan y pierden detalle B. Las formas quedan más nítidas.", "A", "El exceso de tinta se corre y tapa los detalles."),
    ],
    [
        arith("Una tira estampada de 34 cm lleva sellos de 4 cm separados por espacios de 2 cm, empezando y terminando con sello. ¿Cuántos sellos caben?", "(34+2)//(4+2)", "Cada sello con su espacio ocupa 6 cm; se suma un espacio al largo porque el último no lleva espacio."),
        arith("Estampas 9 formas alternando círculo y cuadrado, empezando por círculo. ¿Cuántos círculos hay?", "(9+1)//2", "Los círculos ocupan los lugares impares: 1, 3, 5, 7 y 9."),
        ex("En el teñido por amarre amarras una tira de tela con un elástico antes de sumergirla en té frío. ¿Cómo queda la zona amarrada? A. Más clara porque el té llega menos B. Más oscura.", "A", "El elástico aprieta la tela y el líquido penetra poco."),
    ],
    [
        ex("Huella 1: poca tinta y presión suave, sale pálida con huecos. Huella 2: tinta moderada y presión firme, sale completa. Tu intención es una silueta firme y nítida. ¿Cuál eliges?", "La huella 2", "Tiene la silueta completa y nítida."),
        ex("Quieres un efecto de ritmo regular. ¿Qué decisión lo logra? A. Estampar formas iguales con espacios iguales B. Estampar formas de tamaños distintos sin orden.", "A", "La repetición ordenada produce ritmo."),
    ],
    [
        ex("Quieres que la palabra «SOL» se lea bien al estamparse. ¿Cómo pegas las letras en la matriz? A. En espejo B. Normales, como se leen.", "A", "La estampa invierte las letras, así que la matriz debe llevarlas invertidas."),
        ex("Tu pasta de papel quedó con trozos grandes porque no remojaste lo suficiente. ¿Qué corrige el problema? A. Remojar más tiempo y deshacer con las manos B. Extender la pasta en una capa más gruesa para que los trozos se disimulen.", "A", "El remojo ablanda las fibras para formar una pasta pareja."),
    ],
    ex("Tienes cartón de caja, témpera y una bolsa de tela usada. Quieres un patrón repetido de olas. ¿Qué plan usa bien el procedimiento? A. Pegar tiras onduladas de cartón en una matriz y estampar en fila con tinta moderada B. Mojar la bolsa en mucha témpera sin diseño.", "A", "La matriz repetida y la tinta moderada dan un patrón nítido."),
    [
        ex("En una estampa con matriz, ¿qué pasa con izquierda y derecha de la imagen?", "Se invierten", "La imagen sale como en un espejo."),
        ex("Verdadero o falso: en la monotipia todas las copias salen idénticas.", "Falso", "Cada copia sale distinta."),
        ex("¿Qué haces con el papel usado antes de formar una pasta?", "Lo rasgas y lo remojas", "Así se ablanda y se deshace."),
    ],
    task(
        "Elige UN procedimiento. A) Estampado con matriz de cartón sobre tela o diario: haz una matriz con tres formas pegadas y estampa una fila de cuatro huellas. B) Monotipia sobre una bandeja lisa: haz dos copias y compáralas. C) Trenzado de tres tiras de tela de unos 40 cm y un nudo en cada extremo. Haz dos pruebas cambiando solo una variable (cantidad de tinta, presión o espacio entre formas), escribe qué efecto produjo cada una y cuál elegirías para lograr un ritmo regular.",
        "Elegí la A. Variable: cantidad de tinta. Prueba 1, poca tinta: huellas pálidas con huecos. Prueba 2, tinta moderada: huellas completas. Para ritmo regular elijo la 2 con espacios de 2 cm entre las cuatro huellas.",
        ["cambia una sola variable entre las dos pruebas", "describe el efecto de cada prueba", "elige una según la intención", "usa materiales reutilizados"],
        ["dos pruebas pequeñas", "texto con efectos y elección"],
        ["cambiar varias variables a la vez", "olvidar que la estampa invierte la imagen"],
        "Pregunta qué variable cambió y cómo cambió el aspecto de la huella.",
    ),
    "Moja el borde de un objeto limpio de tu casa en témpera diluida y estámpalo tres veces con espacios iguales en un papel de diario.",
    "Explica por qué una estampa de letras tiene que prepararse en espejo y dibuja una palabra de cuatro letras tal como se vería en la matriz.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Papel de diario, cartón de caja, témpera, restos de tela limpios y cola fría. Si no tienes cola, puedes hacer la matriz solo con dibujos y bocetos.",
    "Aprenderé a responder un desafío creativo con un trabajo propio de impresión, papel o textil hecho con materiales sustentables, desde la lista de restricciones hasta la ficha. Sirve para crear con límites claros.",
    ["Sé hacer pruebas cambiando una variable.", "Sé que la estampa invierte la imagen."],
    [
        "Un desafío creativo es una tarea con restricciones: qué debo hacer, con qué materiales y con qué medidas. Para resolverlo sigo cinco pasos. Primero leo el desafío y anoto las restricciones. Segundo, elijo materiales reutilizados que las cumplan. Tercero, hago pruebas pequeñas. Cuarto, hago la versión final. Quinto, escribo la ficha con título, técnica, materiales reutilizados y el referente del que tomé un recurso.",
        "Las restricciones guían las decisiones. Si el desafío pide un marcapáginas de 5 cm de ancho, el patrón debe caber en 5 cm. Si pide usar solo materiales reutilizados, no puedo agregar cartulina nueva. Si dos técnicas pueden resolver el desafío, elijo la que mejor da lo que busco: la matriz de cartón repite la misma forma, la monotipia hace cada copia distinta.",
        "Mi trabajo es propio cuando la forma, el ritmo y el mensaje son decisiones mías, aunque haya tomado un recurso de un referente. Lo declaro en la ficha. También anoto una huella sustentable: qué material reutilicé y cuántos residuos evité o aproveché. Uso materiales seguros y no uso objetos con filo ni vidrio.",
    ],
    [("desafío creativo", "tarea con restricciones que se resuelve con una obra propia"), ("restricción", "condición que el trabajo debe cumplir, como una medida o un material"), ("técnica", "manera de trabajar un material, como estampado o monotipia"), ("ficha", "texto breve con título, técnica, materiales y referente"), ("huella sustentable", "nota sobre qué material se reutilizó y qué residuos se evitaron")],
    [
        w("Leer las restricciones", "Desafío: «Un marcapáginas de 5 cm de ancho y 20 cm de largo, con un patrón repetido, solo con materiales reutilizados». ¿Qué restricciones hay?", ["De medida: 5 cm de ancho y 20 cm de largo.", "De forma: un patrón repetido.", "De material: solo materiales reutilizados."], "Tres: medida, patrón repetido y materiales reutilizados"),
        w("Completar una ficha", "Una ficha dice: «Título: Mar de retazos. Técnica: monotipia. Materiales reutilizados: cartón y bandeja plástica». ¿Qué le falta?", ["La ficha lleva título, técnica, materiales y referente.", "Faltan el referente y el recurso que se tomó de él."], "Falta anotar el referente del que se tomó un recurso"),
    ],
    [
        m("Usar un material nuevo y llamar a la obra «hecha con materiales reutilizados».", "La obra no cumple la restricción del desafío.", "Revisa cada material de tu lista: ¿ya tuvo un uso antes?"),
        m("Pasar a la versión final sin comparar al menos dos pruebas.", "No se descubre cuál decisión resuelve mejor el desafío.", "Haz dos pruebas distintas y elige una con una razón."),
    ],
    [
        ex("Según los pasos de la clase, ¿qué paso va justo antes de la versión final?", "Hacer pruebas pequeñas", "Primero se prueban las decisiones y luego se hace la obra final."),
        ex("El desafío pide usar solo materiales reutilizados. ¿Cuál lista cumple? A. Cartón de caja, diario usado y resto de camiseta B. Cartulina nueva, diario usado y resto de camiseta.", "A", "En la otra lista la cartulina es nueva."),
        ex("Una ficha dice: «Título: Olas de barrio. Técnica: estampado con matriz. Materiales reutilizados: cartón y camiseta». ¿Qué le falta?", "El referente del que tomó un recurso", "La ficha completa también declara el referente."),
    ],
    [
        ex("Desafío: marcapáginas de 5 cm de ancho y 20 cm de largo con un patrón repetido. ¿Cuál es la restricción de medida? A. 5 cm de ancho y 20 cm de largo B. Un patrón repetido.", "A", "Las medidas son el tamaño exigido; el patrón es una restricción de forma."),
        ex("Una estudiante hace un solo boceto y pasa a la versión final. ¿Qué paso omitió?", "Comparar al menos dos pruebas", "Sin comparación no sabe si su decisión es la mejor."),
        ex("¿Cuál título anuncia mejor un estampado de olas hecho con cartón de caja? A. «Olas de caja» B. «Trabajo 1».", "A", "Dice el tema y el material."),
    ],
    [
        arith("El desafío es una bolsa de tela de 40 cm de ancho. Quieres dejar sin estampar una franja de 8 cm a cada lado. ¿Cuántos centímetros de ancho quedan para estampar?", "40-8-8", "Se restan las franjas de los dos lados."),
        arith("Quieres estampar 5 filas de 6 formas cada una, pero la última fila tiene 2 formas menos. ¿Cuántas formas estampas en total?", "5*6-2", "Son 30 formas, menos las 2 que faltan en la última fila."),
        ex("Debes lograr un ritmo repetido sobre una tela. ¿Qué técnica elijes? A. Matriz de cartón con sellos repetidos B. Monotipia, donde cada copia sale distinta.", "A", "La matriz repite la misma forma una y otra vez."),
    ],
    [
        ex("Boceto 1 copia una bolsa de ejemplo con otro color. Boceto 2 usa la repetición de huellas con formas de olas. Si buscas autoría, ¿cuál desarrollas?", "El boceto 2", "Reinterpreta un recurso con una forma propia."),
        ex("Una compañera usa pliegos de papel de diario sin usar, comprados nuevos, y dice que son materiales reutilizados. ¿Es correcto?", "No", "Un material reutilizado ya tuvo un uso antes."),
    ],
    [
        arith("Una trenza de tres tiras pierde 10 cm de largo al trenzarse en esta regla de ejemplo. Quieres una trenza final de 50 cm. ¿Cuánto debe medir cada tira?", "50+10", "A la medida final se le suma lo que se pierde al trenzar."),
        ex("Dos fichas. X) «Olas de caja. Estampado con matriz. Cartón de caja y camiseta vieja. Recurso de repetición tomado de la bolsa de hojas de ejemplo». Y) «Olas de caja. Estampado». ¿Cuál está completa?", "X", "Incluye técnica, materiales reutilizados y el referente."),
    ],
    ex("Debes crear un marcapáginas para regalar, que sea resistente y reutilice materiales. ¿Qué propuesta cumple mejor? A. Una tira de cartón de caja forrada con un resto de tela, porque resiste el uso y reutiliza B. Una tira de papel de diario sin forrar, que se rompe fácil con el uso.", "A", "El cartón forrado resiste y reutiliza materiales."),
    [
        ex("¿Qué cinco pasos sigues para responder un desafío creativo, en orden?", "Leer restricciones, elegir materiales, pruebas, versión final y ficha", "Es el orden de trabajo de la clase."),
        ex("Verdadero o falso: un trabajo es propio si no declara ningún referente.", "Falso", "La ficha declara de dónde se tomó el recurso."),
        ex("¿Qué es una restricción en un desafío creativo?", "Una condición que el trabajo debe cumplir", "Puede ser una medida, un material o una forma."),
    ],
    task(
        "Elige UN desafío. A) Una bolsa para el pan en tela usada, con un patrón estampado repetido. B) Un afiche para invitar a una feria de trueque, sobre cartón o diario, con una matriz de cartón. C) Un marcapáginas de 5 cm de ancho y 20 cm de largo con patrón repetido, solo con materiales reutilizados. Anota las restricciones, haz dos pruebas pequeñas, elige una, haz la versión final y escribe una ficha con título, técnica, materiales reutilizados, referente y una nota de huella sustentable.",
        "Elegí la C. Restricciones: 5 × 20 cm, patrón repetido, materiales reutilizados. Pruebas: ondas con matriz de cartón y círculos con la base de un vaso. Elijo las ondas. Ficha: «Olas de caja. Estampado con matriz. Cartón de caja y camiseta vieja. Recurso de repetición tomado de la bolsa de hojas de ejemplo. Huella sustentable: aproveché una caja y un retazo».",
        ["anota las restricciones del desafío", "hace dos pruebas distintas y elige una", "la versión final cumple las medidas", "la ficha tiene título, técnica, materiales y referente"],
        ["lista de restricciones", "dos pruebas", "versión final", "ficha completa"],
        ["usar un material nuevo y llamarlo reutilizado", "ficha sin referente"],
        "Señala una restricción del desafío y pregunta cómo la cumplió la versión final.",
    ),
    "Mide con una regla el ancho de una hoja de tu cuaderno y calcula cuántos sellos de 3 cm caben a lo ancho con 1 cm de espacio entre sellos.",
    "Escribe una segunda ficha de tu trabajo dirigida a una persona que nunca vio la técnica, explicando cada término con palabras simples.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Tu trabajo de la clase anterior, hojas y lápiz. Si no lo tienes, usa uno de los dos estampados descritos en esta clase.",
    "Aprenderé a comparar la intención de mi trabajo de impresión, papel o textil con su efecto, y a revisar si de verdad es sustentable. Sirve para mejorar el trabajo con evidencia y con una lista de criterios.",
    ["Sé escribir restricciones de un desafío.", "Sé comparar intención y efecto mostrando la obra sin explicarla."],
    [
        "La intención es lo que quiero comunicar y el efecto es lo que percibe quien mira. En impresión, el efecto depende de la cantidad de tinta, la presión, el espacio entre formas y el soporte. Muestro mi trabajo sin explicarlo y pregunto qué ven y qué sienten. Si lo que describen no coincide con mi intención, busco la decisión que produjo ese efecto y cambio solo una.",
        "El soporte también cambia lo que se ve. Un estampado sobre papel de diario con mucho texto impreso puede confundirse con las letras del fondo. Si esto pasa, cambio una sola variable: por ejemplo, un fondo más liso. Y reviso la sustentabilidad con la lista de cuatro criterios: reutiliza, se usa muchas veces, deja pocos residuos y es seguro. Si cumple tres de cuatro, anoto qué mejoraría para cumplir el cuarto.",
        "Una obra puede cumplir todos los criterios de sustentabilidad y comunicar mal; otra puede comunicar bien y usar materiales nuevos. Busco el equilibrio: ser sustentable y lograr el efecto buscado. Para decidir uso evidencia, como las respuestas de varias personas, y no solo mi gusto. Una respuesta distinta de la esperada no es un error: me dice qué revisar.",
    ],
    [("efecto", "lo que percibe quien mira el trabajo"), ("soporte", "superficie sobre la que se imprime o se trabaja, como el papel o la tela"), ("legibilidad", "facilidad para leer un texto o distinguir una imagen"), ("equilibrio", "buena relación entre dos cosas importantes, como ser sustentable y comunicar"), ("evidencia", "respuesta o dato que permite comprobar algo")],
    [
        w("Intención y efecto", "Intención: mostrar abundancia de peces. Resultado: la gente ve «pocas formas sueltas», porque estampaste 3 peces en una tela grande. ¿Qué cambio de una sola decisión hace coincidir intención y efecto?", ["La causa probable es la cantidad de peces.", "Estampo muchos peces cerca unos de otros.", "Vuelvo a mostrarlo a las mismas personas."], "Estampar muchos peces juntos y volver a preguntar a las mismas personas"),
        w("Revisión con lista", "Tu bolsa: reutiliza una camisa (sí), se usa muchas veces (sí), sobró medio metro de tela botado (no) y usaste témpera escolar (sí). ¿Cuántos criterios cumple y qué mejoras?", ["Cumple 3 de 4: reutiliza, se usa muchas veces y es segura.", "No cumple el criterio de pocos residuos.", "Puedo usar la tela sobrante en otro estampado."], "Cumple 3 de 4; mejora usando los retazos en otro trabajo"),
    ],
    [
        m("Cambiar el color, el soporte y la forma de la matriz de una sola vez.", "No se sabe qué cambio mejoró el efecto.", "Cambia una variable y compara."),
        m("Declarar sustentable el trabajo sin revisar los cuatro criterios.", "Se puede olvidar los residuos o la seguridad.", "Usa la lista de cuatro criterios y marca cuáles cumple."),
    ],
    [
        ex("Intención: ritmo regular. Resultado: las formas tienen espacios desiguales. ¿Coinciden intención y efecto?", "No", "El ritmo regular exige espacios iguales."),
        ex("Mostraste tu estampado a una persona. ¿Qué pregunta haces primero? A. «¿Qué ves y qué sientes?» B. «¿Entiendes que es sustentable?»", "A", "Pregunta abierta, sin darle la respuesta."),
        ex("Un estampado se ve borroso porque se usó demasiada tinta. ¿Eso es parte de la intención o del efecto?", "Del efecto", "Es lo que se percibe, aunque no se quería."),
    ],
    [
        ex("Intención: un cielo lleno de estrellas. Efecto: la gente ve un cielo casi vacío porque hay 2 estrellas en un afiche grande. ¿Qué cambio hace coincidir ambos? A. Estampar muchas estrellas repartidas por todo el afiche B. Estampar las 2 estrellas con más tinta.", "A", "La cantidad de formas es lo que da la idea de abundancia."),
        ex("Criterios: 1) reutiliza material, 2) se usa muchas veces, 3) deja pocos residuos, 4) es seguro. Tu afiche: usa cartón reutilizado (sí); se tira después de la feria (no); dejó muchos recortes (no); usa témpera escolar (sí). ¿Cuántos criterios cumple?", "2", "Cumple solo el 1 y el 4."),
        ex("Tu estampado sobre diario con mucho texto impreso se confunde con las letras. ¿Qué cambio de una variable ayuda? A. Usar un soporte más liso o sin letras B. Cambiar el tamaño de la hoja.", "A", "El fondo con letras compite con la figura."),
    ],
    [
        arith("Mostraste dos versiones a 10 personas. En la versión 1, 4 entendieron la intención; en la 2, 7. ¿Cuántas más la entendieron en la versión 2?", "7-4", "Se compara cada cantidad."),
        ex("Intención: ritmo regular. Huella 1: sellos a 2 cm, 2 cm y 2 cm de distancia. Huella 2: sellos a 2 cm, 5 cm y 1 cm. ¿Cuál tiene ritmo regular?", "La huella 1", "Los espacios son iguales."),
        ex("Tu revisión encontró tela sobrante. ¿Qué mejora de proceso la aprovecha? A. Usar los retazos en otro estampado B. Botarlos porque son pequeños.", "A", "Aprovechar retazos reduce residuos."),
    ],
    [
        ex("Valeria cambia el color, el tamaño y el material en una sola revisión. Mateo cambia solo la cantidad de tinta. ¿Quién podrá saber qué cambio mejoró el efecto?", "Mateo", "Solo cambió una variable."),
        ex("Una persona dice que tu afiche «se ve sucio», pero tú querías aspecto de reciclado. ¿Qué haces? A. Preguntar qué detalle le da esa impresión y decidir si lo cambias B. Decirle que está equivocada.", "A", "Su respuesta es evidencia que se puede revisar."),
    ],
    [
        ex("Afiche X cumple los 4 criterios de sustentabilidad, pero casi no se lee su texto. Afiche Y cumple 3 y se lee claramente. La intención es invitar a una feria. ¿Cuál debe mejorar primero y qué?", "El X, su legibilidad", "Si no se lee, no invita, aunque sea sustentable."),
        ex("Pides a 4 compañeros que digan qué versión se entiende mejor, y 3 eligen la versión 2. ¿Qué decisión tomas con esa evidencia?", "Conservar y seguir desarrollando la versión 2", "La mayoría la percibió mejor."),
    ],
    ex("Tu bolsa para el pan estampada se usará en la feria. Tres personas dicen que sirve «para decorar», pero tu intención era una bolsa para el pan. ¿Qué cambio de una sola decisión ayuda? A. Estampar la silueta de un pan cerca del borde B. Cambiar el color de fondo de toda la tela.", "A", "La silueta dice para qué sirve la bolsa; el color de fondo no lo dice."),
    [
        ex("En impresión, ¿qué es el efecto?", "Lo que percibe quien mira el trabajo", "Puede coincidir o no con la intención."),
        ex("Verdadero o falso: un trabajo que cumple los cuatro criterios de sustentabilidad siempre comunica bien.", "Falso", "Puede tener mal efecto si no se lee o no se entiende."),
        ex("¿Qué haces si el efecto no coincide con la intención?", "Busco la decisión que lo produjo y cambio solo una", "Así sé qué cambio funcionó."),
    ],
    task(
        "Usa tu trabajo de la clase anterior. Si no lo tienes, usa este estampado de ejemplo: tres peces estampados con cartón en una tela grande, con la intención «mostrar abundancia de peces». Muéstralo sin explicarlo a dos personas y pregunta qué ven y qué sienten. Compara con tu intención, revisa los cuatro criterios de sustentabilidad, cambia UNA decisión y vuelve a mostrarlo.",
        "Persona 1: ve pocos peces solos. Persona 2: ve decoración. Intención: abundancia. Criterios: cumple 3 de 4; sobró tela. Cambio: estampo 12 peces juntos. Segunda ronda: la persona 1 dice «hay muchos peces». Los retazos sobrantes se usarán en otro estampado.",
        ["anota las respuestas sin explicar la obra", "compara efecto e intención", "revisa los cuatro criterios", "cambia solo una decisión y registra la nueva respuesta"],
        ["respuestas anotadas", "lista de cuatro criterios", "versión revisada"],
        ["explicar antes de preguntar", "cambiar muchas variables a la vez"],
        "Pregunta qué decisión cambió y qué respuesta nueva comprueba que funcionó.",
    ),
    "Pide a una persona de tu casa que mire tu estampado diez segundos y diga qué le recuerda, sin darle ninguna explicación antes.",
    "Compara por escrito dos soportes distintos para el mismo estampado y explica cuál comunica mejor y cuál es más sustentable.",
)

"""Cuaderno del estudiante de 7.º básico Artes Visuales: AR07 OA 02 (crear a partir de intereses personales con materiales sustentables en dibujo, pintura y escultura)."""
from __future__ import annotations

from student_content_ar7_a import lesson, m, task, w
from student_lessons import arith, ex

OA2 = "AR07 OA 02"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Una hoja, lápiz de mina y una lista de materiales de tu casa que ya no uses (cajas de cartón, diarios, retazos, tapas). Los ejemplos de esta clase están escritos aquí.",
    "Aprenderé a elegir un interés personal para una obra y a escribir criterios de sustentabilidad para elegir materiales. Sirve para crear sin gastar de más ni dañar el entorno.",
    ["Sé escribir una intención con qué, cómo y por qué.", "Sé que una prueba pequeña sirve para decidir."],
    [
        "Un interés personal es algo que me llama la atención o me gusta hacer: un deporte, una mascota, la música, mi barrio, un oficio. Puedo partir de él para crear una obra sin contar cosas privadas: basta con elegir un tema que me interese y decir qué quiero comunicar. Por ejemplo, si me interesa el skate, puedo hacer un dibujo sobre el equilibrio y el movimiento.",
        "Un material sustentable es el que se puede usar sin agotar recursos ni dejar mucho desecho. Para decidir uso criterios, que son preguntas simples: ¿es reutilizado o ya existía?, ¿genera poca basura?, ¿es seguro y no tóxico?, ¿dura lo suficiente?, ¿lo tengo cerca, sin comprar nada nuevo? Entre más preguntas responda con «sí», más sustentable es mi elección. Reducir es usar menos, reutilizar es darle otro uso a lo que existe y reciclar es transformarlo en material nuevo.",
        "Antes de crear escribo mi intención y una lista de criterios con los materiales que pienso usar. Si un material no cumple, busco otro: en lugar de una cartulina nueva, puedo usar el reverso de un afiche viejo o una caja desarmada. La sustentabilidad no significa que la obra sea pobre: significa que mis decisiones cuidan el entorno y que la obra se ve bien igual. Puedo anotar cuántos criterios cumple cada material y elegir el que más cumple.",
    ],
    [("interés personal", "tema que me gusta o me llama la atención"), ("sustentable", "que se usa sin agotar recursos ni dejar mucho desecho"), ("criterio", "pregunta o regla para decidir"), ("reutilizar", "darle otro uso a algo que ya existe"), ("reciclar", "transformar algo usado en material nuevo")],
    [
        w("Aplicar los criterios", "Tienes dos opciones para el soporte de una pintura: cartulina nueva comprada o una caja de cartón desarmada que ibas a botar. Compara con cinco criterios: reutilizado, poca basura, seguro, durable y cercano.", ["Cartulina nueva: no es reutilizada, genera envoltorio, es segura, es durable, hay que comprarla: cumple 2.", "Caja de cartón: es reutilizada, evita basura, es segura, es durable y la tengo en casa: cumple 5.", "Elijo la que cumple más criterios."], "La caja de cartón desarmada (cumple 5 de 5)"),
        w("Pasar del interés a la intención", "Te interesa tu mascota, un gato que duerme en una repisa. Escribe una intención.", ["Interés: el gato.", "Qué comunicar: lo tranquilo de su descanso.", "Cómo y por qué: con curvas suaves y tonos cálidos, porque así se siente la calma."], "Quiero mostrar la calma de mi gato con curvas suaves y tonos cálidos, porque así se siente el descanso"),
    ],
    [
        m("Pensar que sustentable es solo «material de reciclaje feo».", "Un material es sustentable por cómo se obtiene y cuánto desecho deja, no por su aspecto.", "Evalúa los criterios; una obra puede verse bien y ser sustentable."),
        m("Comprar materiales nuevos sin revisar si en casa hay otros que sirven.", "Se pierde la oportunidad de reutilizar y se genera más desecho.", "Revisa primero lo que ya tienes y completa solo lo que falte."),
    ],
    [
        ex("Una tapa de plástico que usarás de nuevo en una escultura, ¿es reutilizar o reciclar?", "Reutilizar", "Se usa tal cual con otro fin, sin transformarla."),
        ex("En Artes Visuales, ¿qué es un interés personal para crear? A. Un tema que me gusta o me llama la atención B. Un dato privado de mi vida que debo contar en la obra.", "A", "Un interés es un tema; no hace falta mostrar cosas privadas."),
        ex("Con un criterio de seguridad, ¿qué material descartas para pintar: témpera escolar o un tarro con solvente fuerte?", "El tarro con solvente fuerte", "El solvente es tóxico y no es seguro para trabajar en casa."),
    ],
    [
        ex("Un diario usado y una hoja de cuaderno nuevo. Para el criterio «reutilizado», ¿cuál cumple?", "El diario usado", "Ya existía y se le da otro uso."),
        ex("Tu interés es el fútbol. ¿Cuál es una intención completa? A. «Quiero mostrar la fuerza de una patada con diagonales y rojo fuerte, porque se siente energía» B. «Voy a hacer algo de fútbol».", "A", "La A dice qué, cómo y por qué; la B solo nombra el tema."),
        ex("Reducir, reutilizar y reciclar. ¿Cuál de las tres consiste en usar menos cantidad de material?", "Reducir", "Reducir es usar menos."),
    ],
    [
        arith("Evalúas un material con 5 criterios y cumple 4. ¿Cuántos criterios NO cumple?", "5-4", "Se restan los cumplidos del total."),
        ex("Material A: retazos de tela reutilizados, seguros y cercanos (cumple 3 criterios). Material B: un barniz con solvente fuerte, comprado y no reutilizado (cumple 0). ¿Cuál eliges para una obra que harás en tu pieza?", "El A", "Cumple más criterios de sustentabilidad y es seguro."),
        ex("Quieres pintar un mural pequeño. Opción 1: usar el reverso de un afiche viejo. Opción 2: comprar una cartulina nueva. Con el criterio «poca basura», ¿cuál eliges?", "La opción 1", "Reutiliza algo que ya existe y no suma desecho nuevo."),
    ],
    [
        ex("Una compañera dice que su obra no es sustentable porque «se ve simple». ¿Tiene razón? A. No, la sustentabilidad se mide por los materiales y el desecho B. Sí, lo simple nunca es sustentable.", "A", "La apariencia no define si un material es sustentable."),
        ex("Una obra usa una caja desarmada, pero el estudiante la corta en pedazos pequeños y los bota porque no le gustó. ¿Qué criterio incumple?", "Poca basura", "Genera desecho y no aprovecha el material."),
    ],
    [
        ex("Te interesa la música. Para tu obra reúnes: dos cajas de huevo limpias, lana sobrante y cartón. ¿Cuántos materiales reutilizados tienes en total?", "Tres", "Son tres tipos: cajas de huevo, lana sobrante y cartón."),
        ex("Dos opciones para hacer una escultura de un instrumento: A) pegar tapas y cajas que ya tenías. B) comprar una masa de modelar nueva. ¿Cuál se alinea mejor con tu criterio de reutilizar?", "A", "Usa lo que ya existe en vez de comprar material nuevo."),
    ],
    ex("Quieres hacer un dibujo de tu pasatiempo (tejer) y tienes: hojas ya impresas por un lado, lápiz de mina y lápices de colores usados. Escribe qué criterios cumple la hoja impresa por un lado y elige: A. reutiliza y evita basura B. es tóxica.", "A", "La hoja impresa por un lado se reutiliza del otro lado y no suma desecho."),
    [
        ex("En Artes Visuales, ¿qué significa sustentable?", "Que se usa sin agotar recursos ni dejar mucho desecho", "Cuida el entorno y dura."),
        ex("Verdadero o falso: se necesita comprar material nuevo para crear una obra buena.", "Falso", "Se puede crear con materiales reutilizados o ya existentes."),
        ex("¿Qué se escribe antes de elegir materiales?", "Una intención y criterios", "Así se decide con razones."),
    ],
    task(
        "Elige UN interés. A) Mi mascota que duerme en una repisa. B) El skate y el equilibrio. C) Una canción que escucho y mi lugar favorito para escucharla. Escribe una intención (qué, cómo, por qué) y completa una tabla con tres materiales que tengas en casa, marcando cuántos de estos cinco criterios cumple cada uno: reutilizado, poca basura, seguro, durable, cercano.",
        "Elegí B. Intención: mostrar el equilibrio con diagonales y líneas curvas, porque el movimiento necesita ese balance. Materiales: caja de cartón desarmada (cumple 5), diario usado (cumple 4: no es muy durable), hojas impresas por un lado (cumple 4: duran poco). Elijo la caja y el diario.",
        ["elige un interés", "escribe intención de tres partes", "lista tres materiales", "cuenta los criterios que cumple cada uno"],
        ["intención escrita", "tabla de tres materiales con criterios"],
        ["escribir solo el tema", "marcar «cumple» sin justificar"],
        "Pregunta qué material cumple más criterios y si cambiaría alguno por otro de casa.",
    ),
    "Mira tu casa y di en voz alta tres cosas que se podrían reutilizar para una obra y por qué son seguras.",
    "Escribe qué criterio agregarías a la lista de cinco para tu obra y qué material cumpliría ese criterio.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Hojas usadas por un lado, lápiz de mina, té o café diluido en un vaso (sin tomar), un pincel o un palito, diarios y harina con agua para una masa. Todo con superficie protegida.",
    "Aprenderé a probar el dibujo, la pintura y el volumen con materiales sustentables y a comparar los efectos de cada uno. Sirve para elegir el procedimiento que mejor comunica mi interés.",
    ["Sé elegir materiales con criterios de sustentabilidad.", "Sé que cambiar una variable permite comparar."],
    [
        "El dibujo trabaja sobre todo con la línea. Se puede hacer con lápiz de mina, con un palito mojado en té o café diluido, o con un trozo de lápiz ya muy corto. La línea fina muestra detalle y la gruesa muestra fuerza. La pintura trabaja con manchas de color. Puedo pintar con témpera escolar con poca agua o con té y café diluidos que dejan tonos cafés. Las manchas pueden ser planas o mezcladas.",
        "La escultura trabaja con el volumen, que es lo que ocupa un espacio y se puede mirar por todos lados. Con diarios arrugados y una masa de harina y agua (engrudo, mezcla sin calentar) se puede hacer una forma redonda o larga. Con cajas de cartón se hacen formas rectas. Preparo el engrudo el mismo día en que lo uso. Si alguien en casa es alérgico a la harina, uso cinta de papel para pegar. El volumen se prueba pegando, doblando o apilando. Tres procedimientos distintos permiten ver tres efectos de la misma idea: con línea, con mancha o con volumen.",
        "Para explorar elijo un tema de mi interés, por ejemplo mi mascota, y lo hago en los tres procedimientos con tamaño pequeño. Después comparo: ¿en cuál se ve mejor el detalle?, ¿en cuál se siente el movimiento?, ¿cuál usó menos material? Anoto qué cada uno hizo bien y elijo uno para desarrollar. Siempre limpio y guardo lo que sobró para usarlo otra vez.",
    ],
    [("dibujo", "obra hecha sobre todo con líneas"), ("pintura", "obra hecha sobre todo con manchas de color"), ("escultura", "obra con volumen, que se mira por todos lados"), ("volumen", "lo que ocupa un espacio en alto, largo y ancho"), ("engrudo", "mezcla de harina y agua que sirve para pegar papel")],
    [
        w("Elegir por efecto", "Tienes tres pruebas pequeñas de un perro: dibujo con lápiz, mancha de té y figura de papel arrugado con engrudo. Quieres mostrar el pelo suave y esponjoso. ¿Cuál eliges?", ["El lápiz muestra líneas, no esponjosidad.", "La mancha de té da un tono suave pero plano.", "El volumen de papel arrugado da una forma que parece esponjosa."], "La figura de papel arrugado con engrudo"),
        w("Medir la masa", "Para una figura pequeña usas 1 cucharada de harina y 2 de agua. Si necesitas el doble de masa, ¿cuánta harina y agua usas?", ["Doble de harina: 2 cucharadas.", "Doble de agua: 4 cucharadas.", "Mantengo la misma proporción."], "2 cucharadas de harina y 4 de agua"),
    ],
    [
        m("Pensar que dibujo, pintura y escultura son lo mismo con otro nombre.", "Cada uno trabaja distinto: línea, mancha o volumen.", "Para elegir, pregunta qué efecto necesito."),
        m("Hacer la prueba con mucho material y tirar lo que sobra.", "Genera basura y no es necesario para explorar.", "Haz pruebas pequeñas y guarda el sobrante."),
    ],
    [
        ex("¿Con qué trabaja sobre todo el dibujo: línea, mancha o volumen?", "Línea", "El dibujo se construye con líneas."),
        ex("Una figura de papel y engrudo que se puede mirar por todos lados, ¿es dibujo, pintura o escultura?", "Escultura", "Tiene volumen y se mira por todos lados."),
        ex("Una mancha amplia de té sobre una hoja usada es un ejemplo de: A. pintura B. escultura.", "A", "Trabaja con manchas de color."),
    ],
    [
        ex("Para mostrar detalle fino en el pelo de un perro, ¿qué procedimiento sirve mejor? A. Dibujo con lápiz y líneas finas B. Una mancha grande de té.", "A", "Las líneas finas muestran detalles pequeños."),
        ex("Para mostrar el peso de una piedra grande, ¿qué procedimiento ayuda a que se sienta su volumen: dibujo plano, mancha plana o escultura de papel y engrudo?", "Escultura de papel y engrudo", "El volumen se puede mirar por todos lados y transmite peso."),
        ex("Dos pruebas con la misma idea (un árbol): una hecha con líneas y otra con manchas. ¿Qué variable cambió: el procedimiento o el tema?", "El procedimiento", "El tema se mantuvo; cambiaron las herramientas y el modo de trabajar."),
    ],
    [
        arith("Para engrudo usas 1 cucharada de harina por cada 2 cucharadas de agua. Si usas 3 cucharadas de harina, ¿cuántas cucharadas de agua necesitas?", "3*2", "Cada cucharada de harina lleva 2 de agua."),
        ex("Quieres mostrar el movimiento de una pelota rodando. Haces tres pruebas: dibujo con líneas largas, una mancha redonda y quieta de té y una bola de papel inmóvil. ¿Cuál muestra mejor el movimiento?", "El dibujo con líneas largas", "Las líneas largas y estiradas sugieren desplazamiento."),
        ex("Tienes diario, harina y agua y quieres un pez que se mire por todos lados. ¿Qué haces? A. Arrugar diario para la forma y cubrirlo con tiras de diario y engrudo B. Dibujar el pez con lápiz en una hoja.", "A", "El diario arrugado da volumen y el engrudo une las tiras."),
    ],
    [
        ex("Una compañera dice que su pintura con té no sirve porque «es solo café». ¿Qué le dirías? A. Que el té y el café dan manchas y tonos válidos para pintar B. Que solo se puede pintar con témpera.", "A", "Los tintes de té y café son materiales sustentables que sirven."),
        ex("En una exploración usaste 5 hojas por prueba y botaste 4 hojas intactas. ¿Qué mejorarías? A. Hacer las pruebas con tamaño pequeño y guardar el sobrante B. Usar hojas más grandes.", "A", "Reducir tamaño y conservar lo no usado evita basura."),
    ],
    [
        ex("Quieres que tu obra sobre un árbol muestre rugosidad en el tronco. ¿Qué procedimiento ayuda más: pintura con témpera diluida plana o escultura con papel arrugado en el tronco?", "Escultura con papel arrugado en el tronco", "El papel arrugado forma una superficie con relieve."),
        arith("Haces una prueba por cada procedimiento (dibujo, pintura, escultura) y 2 intentos de cada uno. ¿Cuántas pruebas hiciste?", "3*2", "Son 3 procedimientos con 2 intentos cada uno."),
    ],
    ex("Quieres mostrar a tu mascota durmiendo. Tres opciones. A. dibujo con curvas suaves B. mancha cálida de té en una forma redonda. C. bola de papel con engrudo en forma de ovillo. Si lo que quieres mostrar es la forma redonda y mullida del cuerpo, ¿cuál sirve más?", "C", "El volumen de papel y engrudo muestra una forma mullida y redonda."),
    [
        ex("En Artes Visuales, ¿qué es el volumen?", "Lo que ocupa un espacio y se mira por todos lados", "Distingue la escultura del dibujo y la pintura."),
        ex("Verdadero o falso: para explorar hay que usar mucho material.", "Falso", "Alcanza con pruebas pequeñas."),
        ex("¿Qué mezcla sirve para pegar papel sin comprar pegamento?", "Engrudo de harina y agua", "Es una mezcla casera, segura y sustentable."),
    ],
    task(
        "Elige UN tema. A) Un animal que conozcas, dormido. B) Una pelota rodando. C) Un árbol con tronco rugoso. Haz tres pruebas pequeñas: un dibujo con lápiz o palito mojado en té, una mancha de color con té, café o témpera con poca agua, y una forma con papel y engrudo (1 cucharada de harina con 2 de agua). Anota cuál usó menos material y cuál muestra mejor tu idea.",
        "Elegí C. Dibujo: líneas cortas para el tronco. Pintura: mancha café con té. Volumen: papel arrugado con engrudo. El volumen mostró mejor la rugosidad. Usé más material en la escultura, pero reutilicé un diario y guardé la masa sobrante en un frasco.",
        ["hace tres pruebas con tres procedimientos", "compara el efecto de cada una", "elige una con una razón", "cuida el material y guarda lo que sobra"],
        ["tres pruebas pequeñas", "comparación escrita"],
        ["hacer solo una prueba", "elegir sin comparar"],
        "Destaca la comparación que usó el efecto y pregunta qué prueba repetiría con otro material.",
    ),
    "Arruga una hoja usada y mírala por todos lados; di si ocupa un espacio y cómo cambia cuando la giras.",
    "Escribe qué procedimiento usarías para mostrar el movimiento y cuál para el peso de algo, y explica por qué.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Cartón de una caja, diario, retazos de tela, tapas de plástico, cajas de huevo, lana sobrante, tijeras de punta redonda, lápiz y engrudo de harina y agua. Todo limpio y seco.",
    "Aprenderé a elegir materiales limpios y seguros y a transformarlos (doblar, arrugar, trenzar, enrollar) sin perder la idea de mi obra. Sirve para trabajar con cuidado y reutilizar sin riesgos.",
    ["Sé evaluar materiales con criterios de sustentabilidad.", "Sé que probar en pequeño evita gastar material."],
    [
        "Un material seguro es el que no hiere ni intoxica. Para reutilizar elijo envases de cartón, papel, tela, lana y plásticos blandos limpios y secos. Descarto vidrio, latas con bordes filosos, envases de productos de limpieza o químicos, pilas, ampolletas y cualquier cosa que haya contenido sustancias peligrosas aunque esté vacía. Antes de usar un objeto lo lavo con agua y jabón, lo dejo secar y reviso que no tenga puntas ni bordes cortantes.",
        "Transformar es cambiarle la forma al material sin perderlo. El papel se puede arrugar, rasgar, enrollar o trenzar. El cartón se dobla, se corta con tijeras de punta redonda o se corruga. La tela se anuda o se envuelve. Cada transformación cambia el efecto: rasgar da un borde irregular, enrollar da formas tubulares, trenzar da un trazo repetido. Pruebo cada transformación con un trozo pequeño y miro qué idea comunica.",
        "La transformación debe tener un propósito. Si quiero mostrar la sensación de apretar, enrollo y amarro; si quiero mostrar ligereza, uso pliegues finos. Un objeto reconocible puede ser parte de la obra si lo transformo para decir algo nuevo, como convertir una caja de huevos en pétalos. Mantengo mi puesto de trabajo ordenado y separo lo que sobra para usarlo en otra obra.",
    ],
    [("material seguro", "material que no hiere ni intoxica"), ("transformar", "cambiar la forma de un material para darle otro efecto"), ("corrugar", "doblar en ondas, como el cartón de las cajas"), ("trenzar", "entrelazar tres tiras o más para formar una cinta"), ("filoso", "con borde que corta")],
    [
        w("Elegir por seguridad", "Tienes cuatro objetos: una lata abierta con borde filoso, una caja de cartón limpia, un frasco de vidrio y un envase vacío de cloro. ¿Cuáles puedes usar?", ["La lata con borde filoso puede cortar.", "El vidrio puede romperse.", "El envase de cloro contuvo un químico peligroso.", "La caja de cartón limpia y seca es segura."], "Solo la caja de cartón limpia"),
        w("Transformar con propósito", "Quieres mostrar la sensación de apretar con una tira de tela. ¿Qué transformación usas: anudar con varias vueltas o dejarla suelta?", ["Apretar necesita algo ceñido y tenso.", "Varias vueltas de nudo muestran esa tensión.", "Suelta se ve libre, no apretada."], "Anudar con varias vueltas"),
    ],
    [
        m("Usar un frasco de vidrio o una lata porque «está limpio».", "Pueden romperse o cortar aunque estén limpios.", "Elige cartón, papel, tela y plásticos blandos limpios y secos."),
        m("Transformar el material sin pensar en qué idea quiere comunicar.", "El resultado se ve raro y no dice nada.", "Elige la transformación según el efecto que buscas."),
    ],
    [
        ex("Una caja de cartón limpia y seca, ¿es un material seguro para reutilizar? ¿Sí o no?", "Sí", "No tiene bordes cortantes ni sustancias peligrosas."),
        ex("¿Qué haces antes de usar un plástico blando reutilizado? A. Lavarlo con agua y jabón, secarlo y revisar que no tenga bordes cortantes B. Usarlo sin revisar.", "A", "Así se evita ensuciar la obra y herirse."),
        ex("Un envase vacío de desinfectante: ¿se puede usar en una escultura?", "No", "Contuvo un químico, aunque esté vacío."),
    ],
    [
        ex("Para dar una forma tubular a un papel, ¿qué transformación sirve: enrollar o rasgar?", "Enrollar", "Enrollar forma un tubo."),
        ex("Quieres un borde irregular, como el de una nube. ¿Qué haces con el papel: rasgar o doblar con regla?", "Rasgar", "Rasgar deja un borde irregular."),
        ex("Quieres transformar una caja de huevos en pétalos. ¿Qué haces primero? A. Separar cada espacio de la caja con tijera de punta redonda B. Pegar la caja entera en la hoja.", "A", "Separando los espacios se obtienen formas parecidas a pétalos."),
    ],
    [
        ex("Tienes lana sobrante en tres colores y quieres hacer una cinta decorativa. ¿Qué técnica usas: trenzar o cortarla en trozos pequeños?", "Trenzar", "Entrelazar las lanas forma una cinta."),
        ex("Una obra necesita mostrar ligereza. ¿Qué transformación del papel sirve: pliegues finos o muchas capas pegadas con engrudo?", "Pliegues finos", "Los pliegues finos se ven livianos; las muchas capas pesadas."),
        arith("Para una guirnalda necesitas 12 pétalos hechos con una caja de huevos de 6 espacios. ¿Cuántas cajas necesitas?", "12/6", "Cada caja da 6 pétalos."),
    ],
    [
        ex("Dos estudiantes transforman una tapa. La primera la pinta de colores sin cambiarle la forma. La segunda la aplana y le pega una tira de tela alrededor para hacer un ojo. ¿Cuál transformó más el material?", "La segunda", "Cambió su forma y la combinó con otro material."),
        ex("Un compañero propone usar una pila vieja como parte de su obra porque «está vacía». ¿Qué le dices?", "Que no, porque tiene sustancias peligrosas", "Las pilas contienen sustancias que hacen daño aunque estén gastadas."),
    ],
    [
        ex("Tu obra necesita 8 trozos de cartón corrugado. Tienes 3 cajas, y cada una te da 4 trozos. ¿Te alcanza?", "Sí", "3 × 4 = 12, y necesitas 8."),
        ex("Quieres mostrar la fuerza del viento con tiras de papel. ¿Qué transformación usas: rasgarlas en tiras largas y torcerlas o pegarlas planas en fila?", "Rasgarlas en tiras largas y torcerlas", "Las tiras torcidas sugieren movimiento."),
    ],
    ex("Debes elegir material para una escultura de un ave. Opción A: botella de vidrio limpia. Opción B: cartón y tela limpios. Opción C: lata abierta. ¿Cuál es segura y reutilizable?", "B", "El vidrio puede romperse y la lata cortar; el cartón y la tela no."),
    [
        ex("En Artes Visuales, ¿qué es un material seguro?", "El que no hiere ni intoxica", "Permite trabajar sin riesgo."),
        ex("Verdadero o falso: un envase de producto químico vacío se puede reutilizar para una obra.", "Falso", "Puede quedar con restos peligrosos."),
        ex("¿Qué transformación del papel da un borde irregular?", "Rasgar", "El rasgado no deja un corte recto."),
    ],
    task(
        "Elige UN tema. A) Un ave con alas de pliegues. B) Una flor hecha con una caja de huevos. C) Una cinta trenzada con tres colores de lana. Escribe qué materiales de tu casa usarás, por qué son seguros (limpios, secos, sin bordes filosos ni químicos) y qué dos transformaciones probarás. Haz las pruebas con trozos pequeños y anota el efecto.",
        "Elegí B. Materiales: caja de huevos limpia, lana y cartón. Seguros porque están limpios y no cortan. Transformaciones: separar los espacios para hacer pétalos y trenzar lana para el tallo. Efecto: los pétalos se ven suaves y el tallo trenzado se ve firme.",
        ["elige materiales seguros y explica por qué", "prueba dos transformaciones", "anota el efecto de cada una", "no usa vidrio, latas ni envases químicos"],
        ["lista de materiales con razón de seguridad", "dos pruebas con su efecto"],
        ["usar objetos filosos", "transformar sin propósito"],
        "Destaca la prueba cuyo efecto coincide con la idea y pregunta qué otro material cambiaría.",
    ),
    "Revisa una caja de cartón de tu casa y di si es segura y por qué.",
    "Elige un material de casa y escribe tres transformaciones distintas, con el efecto que daría cada una.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Cartón, papel, lana, retazos, cinta de papel y engrudo de harina y agua. Tijeras de punta redonda y una superficie protegida. No hace falta pegamento comprado.",
    "Aprenderé a resolver cómo unir las partes, cómo sostener una escultura (soporte) y cómo terminar la superficie (acabado). Sirve para que mi obra no se desarme y se vea cuidada.",
    ["Sé elegir materiales seguros.", "Sé transformar materiales con un propósito."],
    [
        "Una unión es la forma en que se conectan dos partes. Sin pegamento comprado puedo usar engrudo, amarras con lana o hilo, ranuras (cortes en el cartón donde encaja otra pieza), pestañas (lengüetas del mismo cartón que se doblan) y cinta de papel. Cada unión tiene un efecto: el engrudo es discreto, la amarra se ve y puede ser parte del diseño. Elijo según si quiero que la unión se note o se esconda.",
        "El soporte es lo que sostiene una escultura o una pintura. Una escultura necesita una base más ancha que su parte alta para no caerse; si es muy alta y la base es pequeña, se vuelca. Un buen soporte reparte el peso. Como guía de partida, pruebo con una base de al menos la mitad de la altura de la figura. No es una ley: lo que decide es la prueba de estabilidad (un empujón suave con un dedo) y dónde está lo pesado; si el peso está arriba, necesito más base. Puedo usar una caja plana o un cartón doble. En una pintura, el soporte es la hoja o el cartón; si es delgado y mojado, se arruga, así que uso menos agua o pego dos capas.",
        "El acabado es el último trabajo sobre la superficie: pintar, cubrir con papel, pegar una capa de engrudo diluido para dar firmeza o dejar el material a la vista. Dejo secar cada capa antes de seguir. Reviso la obra desde distintos lados y corrijo lo que se vea descuidado. Un acabado cuidado ayuda a que se entienda la intención y a que la obra dure.",
    ],
    [("unión", "forma en que se conectan dos partes"), ("ranura", "corte en el cartón donde encaja otra pieza"), ("soporte", "lo que sostiene una obra"), ("acabado", "trabajo final sobre la superficie de la obra"), ("base", "parte de abajo que apoya una escultura")],
    [
        w("Dar estabilidad", "Tu figura de cartón mide 30 cm de alto y su base es un cuadrado de 5 cm. Se cae al soplarla. ¿Qué cambias?", ["La base es muy pequeña para la altura.", "Una base más ancha reparte el peso.", "Pego la figura a una caja plana de 15 cm."], "Ampliar la base, por ejemplo con una caja plana de 15 cm"),
        w("Elegir la unión", "Quieres unir dos tiras de cartón y que la unión se vea como parte del diseño. ¿Usas engrudo escondido o una amarra de lana de color?", ["Engrudo: se esconde.", "Amarra de lana: se ve y puede decorar.", "La intención pide que se vea."], "La amarra de lana de color"),
    ],
    [
        m("Hacer la figura alta con una base muy pequeña.", "Se vuelca porque el peso no se reparte.", "Ensancha la base o agrega una pieza plana."),
        m("Pintar encima sin dejar secar el engrudo.", "El papel se arruga y la pintura se corre.", "Espera a que cada capa seque antes de seguir."),
    ],
    [
        ex("¿La base de una escultura debe ser más ancha o más angosta que la parte alta para no caerse?", "Más ancha", "Reparte el peso y evita que se vuelque."),
        ex("Una ranura es: A. un corte en el cartón donde encaja otra pieza B. una capa de pintura.", "A", "Es una unión sin pegamento."),
        ex("Dejar secar cada capa antes de pintar encima, ¿ayuda o perjudica la obra?", "Ayuda", "Evita arrugas y que la pintura se corra."),
    ],
    [
        ex("Tu escultura de un pájaro se cae hacia adelante. ¿Cuál puede ser el problema? A. Las patas están todas hacia adelante y no hay apoyo atrás B. El pájaro tiene ojos demasiado grandes.", "A", "El peso mal repartido hace que se incline."),
        ex("Para que dos cartones se unan sin pegamento y la unión sea firme, ¿qué técnica sirve: ranura con pestaña o simplemente apoyar uno sobre otro?", "Ranura con pestaña", "La pieza encajada se sostiene sola."),
        ex("Quieres que el color de tu escultura sea uniforme y firme. ¿Qué acabado ayuda? A. Cubrir con una capa de papel y engrudo diluido y pintar encima cuando esté seca B. Pintar con mucha agua sobre el papel húmedo.", "A", "La capa seca da una superficie firme para pintar."),
    ],
    [
        arith("Tu base mide 10 cm de ancho y quieres duplicarla para que sea más estable. ¿Cuánto debe medir?", "10*2", "Duplicar es multiplicar por 2."),
        ex("Como guía de partida, la base debe medir al menos la mitad de la altura. Una escultura mide 24 cm de alto. ¿Cuántos centímetros de ancho debe tener, como mínimo, la base?", "12", "La mitad de 24 cm es 12 cm."),
        ex("Quieres una unión que se vea parte del diseño en una escultura de un barco con velas de tela. ¿Qué eliges: amarrar con lana de color o esconder con engrudo?", "Amarrar con lana de color", "La lana a la vista es parte del diseño."),
    ],
    [
        ex("Dos estudiantes hacen su escultura con el mismo material. La primera tiene una base de 6 cm para 30 cm de altura. La segunda tiene una base de 15 cm para 30 cm de altura. ¿Cuál es más estable?", "La segunda", "Su base más ancha reparte mejor el peso."),
        ex("Un compañero pega con engrudo y pinta de inmediato. A la mañana siguiente la pintura se descascara. ¿Cuál fue su error principal?", "No dejar secar el engrudo antes de pintar", "El papel húmedo no sostiene la pintura."),
    ],
    [
        ex("Quieres un acabado que muestre el material original del cartón. ¿Qué haces: dejar el cartón a la vista con solo una capa de engrudo diluido o taparlo todo con pintura espesa?", "Dejar el cartón a la vista con solo una capa de engrudo diluido", "Así el material se ve y se protege."),
        arith("Necesitas 3 capas de engrudo y cada una tarda 2 horas en secar. ¿Cuántas horas esperas en total?", "3*2", "Se multiplican las capas por el tiempo de cada una."),
    ],
    ex("Tu escultura de una torre de cartón se tambalea. Opción A: agregar una base ancha de cartón doble. Opción B: pintarla de otro color. ¿Cuál la hace más estable?", "A", "La base ancha reparte el peso; el color no cambia la estabilidad."),
    [
        ex("En Artes Visuales, ¿qué es un soporte?", "Lo que sostiene una obra", "Puede ser una base o el cartón de una pintura."),
        ex("Verdadero o falso: el engrudo se puede usar como unión sin pegamento comprado.", "Verdadero", "Es una mezcla de harina y agua que pega papel."),
        ex("¿Qué se hace antes de aplicar otra capa de acabado?", "Dejar secar la anterior", "Así no se arruga ni se corre."),
    ],
    task(
        "Elige UNA obra. A) Una torre de cartón de 24 cm de alto. B) Un barco con velas de tela. C) Un animal de pie hecho con cajas. Escribe qué tipo de unión usarás y por qué, cómo harás la base y cómo será el acabado. Haz una prueba de estabilidad (soplar suave o inclinar con un dedo) y anota si se mantiene.",
        "Elegí A. Unión: ranuras con pestañas, porque no necesito pegamento. Base: cartón doble de 12 cm de ancho. Acabado: una capa de engrudo diluido y pintura de témpera cuando esté seca. La torre resistió el soplido suave.",
        ["elige y justifica la unión", "diseña una base según su altura", "describe el acabado", "hace una prueba y anota el resultado"],
        ["descripción escrita de unión, base y acabado", "resultado de la prueba de estabilidad"],
        ["base demasiado pequeña", "pintar sin dejar secar"],
        "Destaca la decisión de la base y pregunta qué cambiaría si la figura fuera más alta.",
    ),
    "Apila tres cajas de cartón de tamaños distintos y di cuál debe ir abajo para que la torre sea estable.",
    "Escribe dos formas distintas de unir dos cartones sin pegamento comprado y di cuál se ve más y cuál menos.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Una hoja, lápiz y el boceto o la maqueta de tu obra (o el ejemplo escrito en esta clase). Cartón, retazos y engrudo si quieres trabajar la versión final.",
    "Aprenderé a terminar una obra con materiales sustentables, a revisarla con una pauta de criterios y a mantener mi autoría. Sirve para entregar un trabajo cuidado, propio y fácil de explicar.",
    ["Sé elegir materiales, unirlos y darles un acabado.", "Sé que una revisión se hace con criterios."],
    [
        "La autoría es saber que la idea y las decisiones de mi obra son mías. Puedo inspirarme en otras obras, pero no las copio. Si uso una idea de un compañero o un referente, lo cito: «Me inspiré en la forma de las manos de una escultura que vi». Citar es decir de dónde viene algo. Si ayudo a un compañero con su obra, la decisión final sigue siendo de quien la hace.",
        "Para revisar uso una pauta con cuatro criterios: la intención se nota, los materiales son sustentables (reutilizados, seguros, con poco desecho), la unión, el soporte y el acabado están resueltos, y la obra es propia. Marco cada criterio con «cumple», «cumple en parte» o «no cumple» y escribo una razón. Después elijo un solo cambio para mejorar, lo hago y anoto el efecto.",
        "Al terminar, guardo el sobrante de materiales en una caja para la próxima obra. Escribo una ficha corta con título, materiales, intención y qué cambié en la revisión. Si alguien sugiere algo, decido yo si lo uso. Una buena obra sustentable se ve cuidada, comunica una idea y deja poco desecho.",
    ],
    [("autoría", "ser quien tuvo la idea y tomó las decisiones de la obra"), ("citar", "decir de dónde viene una idea o un material"), ("pauta", "lista de criterios para revisar un trabajo"), ("sobrante", "material que queda sin usar"), ("revisión", "mirar la obra de nuevo para decidir qué mejorar")],
    [
        w("Usar la pauta", "Tu escultura de un pez cumple la intención y los materiales, pero la aleta se despega. ¿Cómo marcas la pauta y qué mejoras?", ["Intención: cumple.", "Materiales: cumple.", "Unión, soporte y acabado: cumple en parte, porque la aleta se despega.", "Mejora: una amarra de lana o más engrudo en la aleta."], "Marcar «cumple en parte» en unión y reforzar la aleta"),
        w("Citar una inspiración", "Te inspiraste en una escultura de manos grandes. Haces una escultura de manos pequeñas con cartón enrollado. ¿Qué escribes?", ["No copié la forma exacta.", "Cito lo que me inspiró.", "Digo qué cambié."], "«Me inspiré en una escultura de manos grandes, pero hice las mías pequeñas y de otro material»"),
    ],
    [
        m("Copiar una obra y no decir de dónde viene la idea.", "Se pierde la autoría y no se reconoce a quien la inspiró.", "Cita la inspiración y cambia una decisión importante."),
        m("Arreglar todo a la vez en la revisión.", "No se sabe qué cambio mejoró la obra.", "Elige un cambio, hazlo y anota su efecto."),
    ],
    [
        ex("Citar una inspiración es: A. decir de dónde viene la idea B. copiar la obra.", "A", "Citar da crédito y mantiene la autoría."),
        ex("¿Cuántos criterios tiene la pauta de esta clase?", "Cuatro", "Son intención, materiales, resolución técnica y obra propia."),
        ex("Un material sobrante, ¿se bota o se guarda para otra obra?", "Se guarda", "Así se reduce el desecho."),
    ],
    [
        ex("Tu obra tiene la intención clara, usa materiales reutilizados, pero la base se tambalea. ¿Qué marcas en el criterio de unión, soporte y acabado? A. Cumple en parte B. Cumple del todo, porque lo demás está bien.", "A", "La base falla pero el resto sí funciona."),
        ex("Un amigo te propone un cambio que tapa tu idea. ¿Qué haces? A. Decido yo si lo uso, porque la autoría es mía B. Lo hago sin pensar.", "A", "La decisión final es de quien crea."),
        ex("Si ayudas a un compañero a pegar una pieza y él decide el color, ¿de quién es la autoría de la obra?", "De tu compañero", "Él tomó las decisiones de su obra."),
    ],
    [
        arith("Revisas tu obra con 4 criterios. En 1 marcas «cumple en parte» y en 1 marcas «no cumple». ¿En cuántos marcas «cumple»?", "4-1-1", "De 4 criterios, 1 es en parte y 1 no cumple; cumplen 2."),
        ex("Tu pauta marca «cumple» en intención, materiales y obra propia, y «cumple en parte» en unión, soporte y acabado. ¿Cuál es el siguiente paso?", "Elegir un solo cambio para mejorar la unión, el soporte o el acabado", "Se mejora el criterio que cumple en parte, de a uno."),
        ex("Un compañero escribe en su ficha: «Obra propia, inspirada en una escultura de manos». ¿Cumple con citar?", "Sí", "Dice en qué se inspiró."),
    ],
    [
        ex("Una estudiante entrega una obra idéntica a la de un afiche pero con cartón. En su ficha escribió «idea mía». ¿Cumple con la autoría?", "No", "No cita su inspiración ni cambió una decisión propia."),
        ex("Dos estudiantes terminan una escultura. El primero guarda su cartón sobrante en una caja y la segunda lo bota. ¿Quién cuida mejor el criterio de poco desecho?", "El primero", "Guardar el sobrante evita basura y permite reutilizarlo."),
    ],
    [
        ex("En tu revisión escribiste: «La obra se ve cuidada, los materiales son reutilizados y se entiende que es sobre una mascota». ¿Qué falta para que sea una revisión completa? A. Un cambio concreto para mejorar y su efecto B. Otro título.", "A", "La revisión pide elegir un cambio y anotar lo que logró."),
        arith("Necesitas 2 cambios de 10 minutos y 1 cambio de 15 minutos. ¿Cuánto tiempo toman en total?", "2*10+15", "Se suman los tiempos de todos los cambios."),
    ],
    ex("Terminaste una obra con cartón, retazos y engrudo. En tu ficha, ¿cuál es la forma correcta de citar una inspiración? A. «Me inspiré en el movimiento de una escultura de un ave y lo cambié a materiales de casa» B. «Esta idea la saqué de internet».", "A", "La A dice qué inspiró y qué cambió."),
    [
        ex("En Artes Visuales, ¿qué es la autoría?", "Ser quien tuvo la idea y tomó las decisiones", "Se mantiene aunque se pidan consejos."),
        ex("Verdadero o falso: puedo copiar una obra si cambio solo el color.", "Falso", "La idea sigue siendo ajena."),
        ex("¿Cuántos cambios eliges por vez al revisar?", "Uno", "Así se sabe su efecto."),
    ],
    task(
        "Elige UNA obra. A) Un pez de cartón con una aleta que se despega. B) Un ave de papel y engrudo que se inclina. C) Un barco con velas de tela y base pequeña. Completa la pauta de cuatro criterios (intención, materiales sustentables, unión-soporte-acabado, obra propia) con «cumple», «cumple en parte» o «no cumple» y una razón, elige UN cambio y escribe su efecto. Termina con una ficha de tres líneas.",
        "Elegí la C. Intención: cumple; materiales: cumple; soporte: cumple en parte porque la base es pequeña; obra propia: cumple. Cambio: ampliar la base con cartón doble. Efecto: ya no se inclina. Ficha: Barco de tela. Materiales reutilizados. Me inspiré en un barco de juguete que vi y lo hice con mis ideas.",
        ["completa la pauta con razones", "elige un solo cambio", "anota el efecto", "cita la inspiración y mantiene autoría"],
        ["pauta completa", "ficha de tres líneas"],
        ["marcar sin razón", "cambiar todo a la vez"],
        "Destaca el criterio mejor justificado y pregunta qué cambiaría si no tuviera ese material.",
    ),
    "Cuenta a una persona de tu casa qué cambio harías en una obra tuya y por qué, sin pedirle que lo haga por ti.",
    "Escribe una segunda ficha que explique cómo reducirías aún más el desecho en la misma obra.",
)

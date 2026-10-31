"""Cuaderno del estudiante de 6.º básico Artes Visuales: AR06 OA 01 (crear desde el ser humano contemporáneo y la ciudad, el arte contemporáneo y el arte en el espacio público)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR06 OA 01"


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
    OA1, 1,
    "Una hoja, un lápiz de mina y lápices de colores. Para observar puedes mirar una calle o una plaza de tu barrio, o usar las escenas de ciudad escritas en esta clase.",
    "Aprenderé a observar la vida de las personas de hoy en la ciudad y a escribir una intención: qué quiero comunicar, cómo lo muestro y por qué. Sirve para que mi obra parta de una idea propia y no de una copia.",
    ["Sé que una observación dice lo que se ve y una intención dice lo que quiero comunicar.", "Sé hacer un croquis y anotar forma, color, tamaño y movimiento."],
    [
        "El entorno cultural de esta clase es el ser humano contemporáneo y la ciudad. «Contemporáneo» quiere decir de nuestra época, de hoy. Las ciudades tienen edificios altos, autos, buses, semáforos, pantallas, ruido, apuro y mucha gente que se cruza sin conocerse. También tienen plazas, parques y personas que conversan. Todo eso puede ser el tema de una obra de arte o de un diseño.",
        "Para crear a partir de una observación, primero miro y anoto datos que se ven: cuántas personas hay, qué hacen, de qué colores son las cosas, qué tamaño tienen unas frente a otras. Después escribo mi intención con tres partes: qué quiero mostrar, cómo lo voy a mostrar y por qué. Ejemplo: «Quiero mostrar la prisa de la ciudad con líneas diagonales repetidas y colores fuertes, porque así se siente el apuro».",
        "Una misma esquina puede inspirar intenciones muy distintas. Una persona puede mostrar la soledad entre la multitud y otra puede mostrar la alegría de una plaza llena. Las dos son válidas si la intención es clara y se nota en las decisiones del dibujo: tamaños, colores, líneas y espacios vacíos. Copiar un dibujo de otra persona no sirve, porque ahí no hay una idea mía.",
    ],
    [("contemporáneo", "de nuestra época, de hoy"), ("ciudad", "lugar con muchas personas, edificios, calles y servicios"), ("intención", "lo que quiero comunicar con mi obra, cómo y por qué"), ("observación", "dato que se ve y se puede comprobar"), ("croquis", "dibujo rápido que guarda lo principal de lo que veo")],
    [
        w("De la escena a la intención", "Observas una esquina a las 8 de la mañana: buses llenos, muchas personas caminando con la vista en su teléfono y un árbol pequeño en una vereda de cemento. Escribe una intención.", ["Dato que llama mi atención: casi nadie mira el árbol.", "Cómo lo muestro: personas grises con la cabeza baja y el árbol con hojas verdes y brillantes.", "Por qué: porque quiero mostrar que en la ciudad se pasa por la naturaleza sin verla."], "Quiero mostrar que la gente no ve la naturaleza, con personas grises y un árbol verde, porque en el apuro nadie lo mira."),
        w("Separar datos y opinión", "Anotaste: «Dos niños comen helado en una banca. La plaza es aburrida». ¿Cuál parte es un dato y cuál es opinión?", ["«Dos niños comen helado en una banca» se puede ver y comprobar.", "«Aburrida» depende de quien mira.", "En el croquis anoto el dato; la opinión puede transformarse en intención si la explico."], "Dato: los dos niños con helado. Opinión: que la plaza es aburrida"),
    ],
    [
        m("Escribir como intención solo el tema: «Voy a dibujar una calle».", "El tema no dice qué quiero comunicar ni cómo.", "Agrega qué quiero mostrar, cómo lo haré y por qué."),
        m("Llenar el dibujo de todo lo que hay en la ciudad sin elegir nada.", "Sin una idea que guíe, el dibujo no comunica nada claro.", "Elige un dato que te llamó la atención y deja que mande las decisiones."),
    ],
    [
        ex("¿Cuál de estas escenas pertenece al entorno de «el ser humano contemporáneo y la ciudad»? A: Personas esperando el bus bajo un paradero entre edificios altos. B: Un campamento de cazadores de hace miles de años. C: Un bosque sin ninguna persona.", "A", "El paradero, el bus y los edificios son parte de la vida de hoy en la ciudad."),
        ex("«Contemporáneo» significa de nuestra época. ¿Qué objeto es más contemporáneo: un semáforo con luces o una antorcha de mano?", "Un semáforo con luces", "El semáforo se usa hoy en las ciudades; la antorcha es de otra época."),
        ex("Clasifica como «observación» o «intención»: «El edificio tiene doce ventanas azules en fila».", "Observación", "Dice algo que se ve y se puede contar; no dice qué se quiere comunicar."),
    ],
    [
        ex("En la intención «Quiero mostrar el apuro de la ciudad con líneas diagonales repetidas, porque así se siente la prisa», ¿cuál es el «cómo»?", "Con líneas diagonales repetidas", "El cómo son las decisiones visuales que se usarán para mostrar la idea."),
        ex("En una plaza hay niños jugando y una señora sola en una banca. Intención A: mostrar la alegría con colores cálidos y figuras en movimiento. Intención B: mostrar la soledad con una figura pequeña y gris. ¿Cuál usa el detalle de la señora sola?", "B", "La B parte de la señora sola; la A parte de los niños que juegan."),
        ex("Anotaste cuatro cosas: (1) tres buses, (2) un semáforo en rojo, (3) dos personas con paraguas y (4) «me parece que la ciudad es fea». ¿Cuántas de las cuatro son datos que se pueden ver y comprobar?", "Tres", "Las anotaciones 1, 2 y 3 se ven y se pueden comprobar; la 4, «fea», es una opinión."),
    ],
    [
        ex("Una avenida de noche muestra luces de autos que dejan rayas largas rojas y blancas. Quieres mostrar la velocidad. ¿Qué línea usas: largas y estiradas o círculos pequeños y quietos?", "Largas y estiradas", "Las líneas largas parecen movimiento rápido."),
        ex("Quieres mostrar que la ciudad es enorme frente a una persona. ¿Cómo dibujas a la persona: muy pequeña junto a edificios altos o más grande que los edificios?", "Muy pequeña junto a edificios altos", "La diferencia de tamaño hace sentir lo grande del lugar."),
        ex("Tu intención es mostrar el ruido de la ciudad. ¿Qué combinación sirve más: rojo y amarillo con líneas quebradas o azul pálido con una sola línea recta suave?", "Rojo y amarillo con líneas quebradas", "Los colores fuertes y las líneas quebradas dan sensación de ruido y tensión."),
    ],
    [
        ex("Un compañero escribe: «Mi intención es dibujar una calle». ¿Es una intención completa? A: Sí, dice qué dibujará. B: No, solo da el tema y faltan qué comunicar, cómo y por qué.", "B", "Un tema no dice qué se quiere comunicar con ese tema."),
        ex("Ana dibuja pocas personas muy pequeñas en un espacio grande y vacío. Luis dibuja muchas personas pegadas, sin espacio entre ellas. Ambos quieren mostrar la soledad entre la gente. ¿Quién la muestra mejor?", "Ana", "El espacio vacío y las figuras pequeñas aíslan a las personas; las figuras pegadas muestran multitud."),
    ],
    [
        ex("Quieres mostrar que la gente de hoy mira mucho sus pantallas. ¿Qué detalle repites en tu dibujo: caras iluminadas por pantallas pequeñas en muchas personas o un árbol grande al centro?", "Caras iluminadas por pantallas pequeñas en muchas personas", "Repetir el detalle de las pantallas deja clara la idea."),
        ex("Una intención dice: «Quiero mostrar el cansancio de volver a casa, con figuras inclinadas y colores grises, porque la ciudad cansa». Si cambias «figuras inclinadas» por «figuras saltando», ¿sigue mostrando cansancio?", "No", "Saltar transmite energía y contradice la idea de cansancio."),
    ],
    ex("Vas en micro y ves por la ventana un muro pintado, personas esperando y una grúa en un edificio en construcción. Quieres hacer un croquis rápido para recordarlo. ¿Qué anotas junto al croquis: colores, formas y tamaños que ves o solo «estaba lindo»?", "Colores, formas y tamaños que ves", "Los datos concretos sirven después para decidir; «lindo» no dice nada."),
    [
        ex("¿Qué dice una intención que no dice una observación?", "Lo que quiero comunicar", "La observación describe lo que se ve; la intención añade la idea propia."),
        ex("Verdadero o falso: dos personas pueden mirar la misma esquina y tener intenciones distintas.", "Verdadero", "Cada autor decide qué comunicar a partir de lo que ve."),
        ex("¿Qué tres partes tiene una intención completa?", "Qué, cómo y por qué", "Con las tres partes se sabe la idea, las decisiones y la razón."),
    ],
    task(
        "Elige UNA escena de ciudad. A) Una micro llena al atardecer, con personas de pie y luces anaranjadas. B) Una plaza con un mural en el muro, una niña en patineta y un señor que lee en una banca. C) Una calle con muchos letreros de colores, un perro dormido en la vereda y un semáforo en rojo. Haz un croquis, anota cinco datos que se ven y escribe tu intención con qué, cómo y por qué.",
        "Elegí la A. Datos: hay once personas de pie; las luces son anaranjadas; los vidrios tienen vapor; una persona duerme apoyada; el techo es bajo. Intención: quiero mostrar el cansancio del regreso a casa, con figuras inclinadas y tonos anaranjados apagados, porque al final del día todos van agotados.",
        ["hace un croquis", "anota cinco datos que se ven", "escribe qué, cómo y por qué", "la intención se apoya en los datos del croquis"],
        ["croquis", "cinco datos", "intención de tres partes"],
        ["escribir solo el tema", "mezclar opiniones con datos"],
        "Destaca la intención que se nota en el croquis y pregunta qué decisión del dibujo (tamaño, color, línea o espacio) la muestra.",
    ),
    "Mira una calle por la ventana durante un minuto y di en voz alta un dato que ves y una intención posible para dibujarlo.",
    "Escribe dos intenciones distintas para la misma escena y explica cuál cambiaría más los colores y los tamaños de tu dibujo.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Una hoja, lápiz de mina, tijeras de punta redonda y objetos cotidianos limpios (tapas de plástico, cuadrados de papel, clips grandes). Las obras que se nombran están descritas aquí; no necesitas buscarlas.",
    "Aprenderé qué es el arte contemporáneo y probaré una variable visual: repetir un objeto y cambiar su escala. Sirve para crear una obra que hable de la vida de hoy usando objetos y un espacio.",
    ["Sé escribir una intención con qué, cómo y por qué.", "Sé que una variable visual es una decisión que puedo cambiar para ver su efecto."],
    [
        "El arte contemporáneo es el arte que se hace en nuestra época. Sus artistas pintan y esculpen, pero también usan objetos cotidianos, fotografía, video y el propio espacio. Una instalación es una obra que ocupa un lugar y se recorre, como una sala llena de objetos puestos con un orden. A veces el público puede caminar dentro de ella. Muchas de estas obras hablan de cosas de hoy: el consumo, las ciudades, las pantallas o el medio ambiente.",
        "Dos variables muy usadas son la repetición y la escala. Repetir es poner muchas veces el mismo objeto; sirve para mostrar cantidad, orden o exceso. Escala es el tamaño de la obra o de un objeto comparado con otros o con el cuerpo de quien mira. Un objeto común, muy grande o repetido cien veces, cambia lo que sentimos al verlo. Para saberlo hago pruebas pequeñas y cambio una sola variable por vez.",
        "En la práctica pruebo dos maquetas del mismo tema con los mismos objetos: una con pocos y otra con muchos, o una con tamaños iguales y otra con tamaños distintos. Comparo cuál comunica mejor mi intención. No copio la idea de otro artista: uso la repetición y la escala para hablar de algo que observé en mi ciudad, como la cantidad de envases que se botan o las filas de autos en un atasco.",
    ],
    [("arte contemporáneo", "arte hecho en nuestra época, con materiales y formas muy variados"), ("instalación", "obra que ocupa un espacio y se recorre"), ("repetición", "poner muchas veces el mismo elemento"), ("escala", "tamaño de algo comparado con otra cosa o con el cuerpo"), ("variable visual", "decisión que se puede cambiar para ver su efecto")],
    [
        w("Elegir la variable", "Tu intención es mostrar cuántos vasos de plástico se botan en un día. Pruebas A) un vaso solo, y B) seis filas de ocho vasos. ¿Cuál muestra mejor la idea?", ["La idea habla de cantidad.", "La prueba B repite muchas veces el mismo objeto.", "La prueba A muestra un solo vaso y no da idea de cantidad."], "La prueba B"),
        w("Cambiar la escala", "Quieres que un clip se vea importante en una obra sobre el trabajo de oficina. ¿Qué cambio de escala sirve: dibujarlo del tamaño de una moneda o del tamaño de una persona?", ["Un objeto muy grande llama la atención.", "Al lado de una persona se nota su tamaño exagerado.", "El tamaño de una moneda lo deja como un objeto común."], "Del tamaño de una persona"),
    ],
    [
        m("Pensar que arte contemporáneo es solo una pintura hecha hoy.", "También incluye instalaciones, video, fotografía y objetos.", "Revisa qué medios usa la obra y cuál es su idea."),
        m("Cambiar a la vez la cantidad, el color y el tamaño en una prueba.", "Así no se sabe cuál cambio produjo el efecto.", "Cambia una sola variable por prueba y compara."),
    ],
    [
        ex("Una sala llena de zapatos viejos puestos en filas que se pueden recorrer, ¿es una pintura o una instalación?", "Una instalación", "Ocupa un espacio y se recorre."),
        ex("¿Qué variable usas si pones el mismo objeto veinte veces seguidas: la repetición o la escala?", "La repetición", "Repetir es poner muchas veces el mismo elemento."),
        ex("Un artista hace una taza de tres metros de alto. ¿Qué cambió: la escala o la cantidad de tazas?", "La escala", "El tamaño comparado con el cuerpo es la escala."),
    ],
    [
        arith("Haces una maqueta con 5 filas de 7 tapas de plástico cada una. ¿Cuántas tapas necesitas en total?", "5*7", "Se multiplican filas por tapas de cada fila."),
        ex("Dos pruebas con las mismas tapas: A) 4 tapas separadas con mucho espacio, B) 40 tapas juntas en un cuadrado. Tu intención es mostrar abundancia. ¿Cuál sirve?", "La B", "Muchas tapas juntas dan sensación de cantidad."),
        ex("En el arte contemporáneo, ¿por qué un artista usaría objetos de todos los días en vez de pintura? A: Porque habla de la vida de hoy con cosas que todos conocen. B: Porque en el arte de hoy está prohibido pintar.", "A", "Los objetos cotidianos conectan la obra con lo que vivimos hoy."),
    ],
    [
        ex("Quieres mostrar el atasco de autos de las 6 de la tarde. ¿Qué variable usas: repetir muchos autos pequeños en fila o dibujar un solo auto enorme?", "Repetir muchos autos pequeños en fila", "La fila repetida muestra la cantidad y la lentitud del atasco."),
        ex("Quieres que el público se sienta pequeño ante la basura que genera. ¿Qué escala usas para una bolsa: del tamaño de una bolsa real o más alta que una persona?", "Más alta que una persona", "El tamaño exagerado hace sentir al espectador diminuto."),
        ex("Cambias a la vez cantidad y color de tus objetos y la prueba se ve mejor. ¿Sabes cuál cambio ayudó?", "No", "Al cambiar dos cosas juntas no se puede saber cuál produjo el efecto."),
    ],
    [
        ex("Prueba 1: 30 clips del mismo tamaño en filas ordenadas. Prueba 2: 30 clips de tamaños distintos, algunos muy grandes. Tu intención es mostrar el orden rígido de una oficina. ¿Qué prueba sirve más?", "La 1", "Tamaños iguales y filas ordenadas transmiten orden rígido."),
        ex("Una compañera dice que su obra, una fila de 10 botellas de plástico idénticas, muestra «el exceso de envases». Otro dice que muestra «un solo envase importante». ¿Qué interpretación coincide mejor con la repetición?", "El exceso de envases", "Repetir lo mismo muchas veces habla de cantidad o exceso."),
    ],
    [
        ex("Quieres mostrar en una obra pequeña de escritorio que los mensajes de pantalla nos rodean. ¿Qué usas: cuadrados de papel de colores repetidos en todo el borde del cartón o un solo cuadrado en el centro?", "Cuadrados de papel repetidos en todo el borde del cartón", "Repetirlos alrededor da la idea de estar rodeado."),
        arith("Haces una instalación con 3 hileras de 9 cuadrados de papel. Agregas 2 hileras más con 9 cuadrados cada una. ¿Cuántos cuadrados hay en total?", "(3+2)*9", "Son 5 hileras de 9 cuadrados cada una."),
    ],
    ex("Quieres mostrar cuántas bolsas se usan en una feria en un día. Tienes 24 cuadrados de papel que representan bolsas. ¿Los pones repetidos en una cuadrícula ordenada de 4 filas de 6 o los dejas separados y sin orden, lejos unos de otros?", "En una cuadrícula ordenada de 4 filas de 6", "La cuadrícula repetida muestra cantidad y 4 × 6 usa los 24 cuadrados."),
    [
        ex("En arte, ¿qué es una instalación?", "Una obra que ocupa un espacio y se recorre", "Se instala en un lugar y el público puede moverse en ella."),
        ex("Verdadero o falso: repetir un objeto muchas veces puede comunicar exceso o cantidad.", "Verdadero", "La repetición hace sentir que hay mucho de algo."),
        ex("¿Por qué conviene cambiar una sola variable por prueba?", "Para saber qué cambio produjo el efecto", "Con un solo cambio se puede comparar con claridad."),
    ],
    task(
        "Elige UNA idea de la ciudad. A) Los envases que se botan en un día. B) Las filas de autos en un atasco. C) Las pantallas que miramos todo el día. Con 24 objetos pequeños (tapas, cuadrados de papel o clips) haz dos maquetas sobre una hoja: una con repetición y orden, y otra con objetos en pocas cantidades o con tamaños distintos. Fotografía o dibuja ambas, elige una y escribe tu intención.",
        "Elegí la A. Maqueta 1: 24 tapas en 4 filas de 6. Maqueta 2: 4 tapas separadas. Elijo la 1, porque quiero mostrar que se botan muchísimos envases, y la cantidad repetida se nota más.",
        ["hace dos maquetas con la misma idea", "cambia solo una variable", "elige una con razón", "escribe una intención de tres partes"],
        ["dos dibujos o fotos de las maquetas", "intención escrita"],
        ["copiar una obra conocida", "cambiar muchas variables a la vez"],
        "Pregunta qué cambió entre las dos pruebas y por qué la elegida comunica mejor la idea.",
    ),
    "Repite en la mesa un objeto de tu casa cinco veces en una fila y di qué idea sientes (orden, cantidad, aburrimiento).",
    "Cambia el tamaño de los objetos de tu maqueta de menor a mayor y explica qué idea nueva aparece.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Una hoja grande o papel de envolver, lápiz, regla, lápices de colores o témpera, y una caja de cartón pequeña. Los ejemplos de murales y esculturas están descritos aquí.",
    "Aprenderé qué son los murales y las esculturas del espacio público y cómo se eligen materiales y procedimientos para una obra grande. Sirve para planificar un boceto que pueda llevarse a un muro o a una plaza.",
    ["Sé que el arte contemporáneo usa muchos medios.", "Sé que la escala es el tamaño de una cosa comparado con otra o con el cuerpo."],
    [
        "El arte en el espacio público es el que está en la calle, en plazas o muros, y cualquier persona puede verlo sin entrar a un museo. Un mural es una pintura de gran tamaño hecha sobre un muro. Una escultura pública es una obra con volumen ubicada en un lugar abierto. En Chile hay murales en muchas ciudades; por ejemplo, en los cerros de Valparaíso se ven muros pintados con escenas y dibujos de colores. En el desierto de Atacama está «La Mano del Desierto», una escultura de una mano gigante del escultor chileno Mario Irarrázabal.",
        "Una obra pública debe resistir el sol, la lluvia y el viento, y debe verse bien desde lejos. Por eso se eligen materiales resistentes y formas grandes y claras. Los murales se planifican con un boceto pequeño que se amplía con una cuadrícula: se dibuja una cuadrícula sobre el boceto y otra, más grande, en el muro, y se copia lo que hay en cada cuadro. El procedimiento es el paso a paso: boceto, cuadrícula, colores y pintura.",
        "En casa no se pinta un muro, pero puedes practicar el procedimiento. Haces un boceto chico en una hoja, trazas una cuadrícula con regla, la amplías en un papel grande y pintas con formas simples y colores muy contrastados. Después miras la obra desde lejos, a unos pasos, para comprobar si se entiende. Los detalles muy finos desaparecen a distancia, pero las formas grandes y los colores fuertes se siguen viendo.",
    ],
    [("espacio público", "lugares abiertos a todas las personas, como calles y plazas"), ("mural", "pintura de gran tamaño hecha sobre un muro"), ("escultura pública", "obra con volumen ubicada en un lugar abierto"), ("boceto", "dibujo previo y pequeño de la obra"), ("cuadrícula", "red de cuadrados que sirve para ampliar un dibujo")],
    [
        w("Ampliar con cuadrícula", "Tu boceto mide 20 cm de largo y lo quieres pintar en un muro de 4 m (400 cm). ¿Cuántas veces más grande será la obra?", ["Paso 1: paso el largo del muro a centímetros: 4 m = 400 cm.", "Paso 2: divido el largo del muro por el del boceto: 400 ÷ 20.", "Cada cuadro de la cuadrícula del boceto será 20 veces más grande en el muro."], "20 veces más grande"),
        w("Elegir el material", "Quieres una escultura de una mano para una plaza al aire libre. ¿Sirve más papel de diario pegado o piedra y metal?", ["El lugar está expuesto a lluvia y sol.", "El papel de diario se deshace con el agua.", "La piedra y el metal resisten el clima."], "Piedra y metal"),
    ],
    [
        m("Dibujar en el boceto muchos detalles pequeños y esperar que se vean desde lejos.", "Desde lejos los detalles finos se pierden.", "Usa formas grandes y colores con mucho contraste."),
        m("Elegir materiales solo porque son bonitos, sin pensar en el clima.", "Una obra en la calle se moja y se descolora.", "Pregunta qué material resiste lluvia, sol y viento."),
    ],
    [
        ex("¿Dónde está una escultura pública: dentro de la sala de un museo cerrado o en una plaza abierta?", "En una plaza abierta", "Pública significa en un espacio abierto a todas las personas."),
        ex("Una pintura de gran tamaño sobre un muro de la calle se llama...", "Mural", "Mural es la pintura grande hecha sobre un muro."),
        ex("«La Mano del Desierto» es una escultura de una mano gigante. ¿En qué región natural de Chile está: en el desierto de Atacama o en los bosques del sur?", "En el desierto de Atacama", "Su nombre y su lugar son el desierto de Atacama, en el norte."),
    ],
    [
        arith("Un boceto mide 15 cm de largo y se amplía 10 veces para un muro. ¿Cuántos centímetros mide el largo de la obra en el muro?", "15*10", "Se multiplica el largo del boceto por las veces que se amplía."),
        ex("¿Para qué sirve la cuadrícula en un mural? A: Para ampliar el dibujo cuadro por cuadro. B: Para dar color al muro.", "A", "La cuadrícula permite copiar cada parte del boceto al tamaño grande."),
        ex("Ordena el procedimiento de un mural: 1) pintar con color, 2) hacer el boceto pequeño, 3) trazar la cuadrícula en el muro. Escribe el orden de números.", "2, 3, 1", "Primero el boceto, luego la cuadrícula y al final la pintura."),
    ],
    [
        ex("Quieres que tu mural se entienda desde la calle de enfrente. ¿Qué eliges: una figura grande de color amarillo sobre fondo azul oscuro o letras pequeñas grises sobre fondo celeste?", "Una figura grande de color amarillo sobre fondo azul oscuro", "Una figura grande y un fuerte contraste se ven de lejos."),
        ex("Una escultura estará en una calle con mucho viento. ¿Qué forma resiste mejor: una base ancha y pesada o una figura muy alta sobre un palito delgado?", "Una base ancha y pesada", "La base ancha le da estabilidad frente al viento."),
        arith("Un muro de 3 m (300 cm) de largo se cubre con una cuadrícula de cuadros de 25 cm de lado. ¿Cuántos cuadros de ancho tendrá la cuadrícula a lo largo del muro?", "300//25", "Se divide el largo del muro por el lado de cada cuadro."),
    ],
    [
        ex("Una persona dice: «Pondré en el mural un texto de 40 palabras escrito muy chico». Otra propone una sola frase de 4 palabras en letras enormes. ¿Qué propuesta sirve mejor para una obra que se mira al pasar caminando?", "La frase de 4 palabras en letras enormes", "En el espacio público la gente mira de pasada, así que lo grande y breve se lee mejor."),
        ex("Compara dos materiales para una escultura de plaza: A) cartón pegado con cola fría y B) cemento y piedra. ¿Cuál resiste más la lluvia durante años y por qué?", "B, porque el cartón se moja y se deshace", "El cemento y la piedra resisten el agua; el cartón no."),
    ],
    [
        ex("Quieres que un mural de un paradero muestre la alegría de esperar el bus con otras personas. ¿Qué boceto sirve más: personas grandes de colores cálidos conversando o una sola línea gris?", "Personas grandes de colores cálidos conversando", "Las figuras grandes, cálidas y en conversación comunican alegría y compañía."),
        ex("Dibujas en el boceto una cuadrícula de 5 cuadros de ancho por 4 cuadros de alto. ¿Cuántos cuadros tiene en total?", "20", "Son 5 cuadros por cada una de 4 filas: 5 × 4 = 20."),
    ],
    ex("El barrio quiere pintar un muro de 6 m de largo. Tu boceto en hoja mide 40 cm de largo. ¿Cuántas veces debe ampliarse el boceto para cubrir el largo? Recuerda que 1 m son 100 cm.", "15 veces", "El muro mide 600 cm y 600 ÷ 40 = 15.", calc="600//40"),
    [
        ex("¿Qué es una escultura pública?", "Una obra con volumen ubicada en un lugar abierto", "Está en la calle o plaza y se puede rodear."),
        ex("Verdadero o falso: un mural debe tener muchos detalles diminutos para verse bien desde lejos.", "Falso", "Los detalles diminutos se pierden a distancia; conviene lo grande y claro."),
        ex("¿Para qué se hace un boceto antes de un mural?", "Para planificar la imagen antes de pintar el muro", "Sirve para decidir y ensayar antes de la obra grande."),
    ],
    task(
        "Elige UN muro imaginario. A) El muro de 5 m de largo de una escuela, sobre el tema «Los juegos de mi barrio». B) La pared de 4 m de un paradero, sobre el tema «Esperar el bus». C) El muro de 6 m de una feria, sobre el tema «Los colores del mercado». Haz un boceto de 25 cm de largo con 3 formas grandes y una cuadrícula de cuadros de 5 cm, anota qué colores usarías y por qué se verían de lejos.",
        "Elegí la B. Boceto de 25 cm con tres personas grandes (amarilla, roja y celeste) sobre fondo azul oscuro. Cuadrícula de 5 × 5 cm. El fondo oscuro y las figuras claras se ven de lejos desde la calle.",
        ["boceto con formas grandes", "cuadrícula con cuadros del mismo tamaño", "colores con mucho contraste", "razón para la visibilidad a distancia"],
        ["boceto con cuadrícula", "lista de colores con razón"],
        ["demasiados detalles pequeños", "cuadros de distinto tamaño"],
        "Pide que muestre el boceto desde tres pasos de distancia y diga qué se sigue viendo y qué desaparece.",
    ),
    "Mira un muro de tu calle (o la pared de tu pieza) y di qué dibujo grande podría ir ahí y de qué colores.",
    "Calcula cuántas veces tendrías que ampliar tu boceto para cubrir una pared de tu casa y explica cómo lo medirías.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Papel, lápices, regla, cartón liso, tijeras de punta redonda y cola fría. Los lugares de la ciudad que se proponen están descritos aquí.",
    "Aprenderé a crear una propuesta propia de arte para el espacio público: elegir un lugar, una idea y una forma que se vea y que respete a quienes lo usan. Sirve para crear un trabajo con sentido para una comunidad.",
    ["Sé qué es un mural y una escultura pública.", "Sé que una obra pública debe verse desde lejos y resistir el clima."],
    [
        "Una obra de espacio público tiene que pensarse para su lugar. Primero miro el sitio: cuánta gente pasa, cuánto espacio hay, si es un muro liso o una plaza con bancas, y si la obra podría molestar el paso. Después elijo una idea propia que hable del ser humano de hoy y de la ciudad: una necesidad, una alegría o un problema del barrio. Por último decido si será mural, escultura u otra forma, y qué materiales usaría.",
        "Una propuesta clara tiene cuatro partes: el lugar, la idea, la forma (con colores o volúmenes) y la razón. Por ejemplo: «Para el muro de una escuela propongo un mural de manos de muchos tamaños que sostienen una pelota, para mostrar que el juego une a las personas». También debo cuidar que la obra no tape caminos, no moleste a los vecinos y no use imágenes que ofendan.",
        "La autoría significa que la idea es mía. Puedo mirar murales y esculturas para aprender cómo resuelven un problema, pero no los copio. Hago al menos dos bocetos del mismo lugar y elijo uno con una razón visible: se ve mejor desde lejos, comunica la idea con más claridad o respeta mejor el lugar. Anoto también una decisión que cambié mientras trabajaba.",
    ],
    [("propuesta", "idea de obra explicada para un lugar concreto"), ("autoría", "que la idea y las decisiones de la obra son de quien la crea"), ("volumen", "forma que ocupa espacio y se puede rodear"), ("contraste", "diferencia fuerte entre colores o tamaños"), ("comunidad", "personas que viven o usan un mismo lugar")],
    [
        w("Armar una propuesta", "El lugar es un muro de un consultorio de barrio donde la gente espera su turno. Propón una idea.", ["Lugar: un muro grande donde hay personas esperando, que mirarán el muro un buen rato.", "Idea: un mural calmado con colores verdes y celestes sobre cuidar la salud entre vecinos.", "Razón: los colores suaves ayudan a sentir tranquilidad en un lugar de espera."], "Mural verde y celeste con vecinos que se cuidan, para dar tranquilidad mientras esperan"),
        w("Revisar el lugar", "Quieres poner una escultura grande en el centro de una vereda angosta de una calle. ¿Qué problema hay?", ["La vereda es el camino de las personas.", "La escultura taparía el paso, sobre todo a quienes van en silla de ruedas o con coche.", "Hay que buscar otro lugar, como una plaza o un costado amplio."], "Taparía el paso; conviene ponerla en un lugar amplio"),
    ],
    [
        m("Hacer una escultura que tapa el camino por querer que se vea mucho.", "Una obra pública no debe molestar el uso del lugar.", "Revisa el espacio y deja libre el paso."),
        m("Copiar un mural famoso porque «ya se ve bien».", "La obra deja de ser una idea propia.", "Aprende cómo lo hizo y crea tu propia idea para tu lugar."),
    ],
    [
        ex("Una propuesta clara dice el lugar, la idea, la forma y...", "La razón", "La razón explica por qué esa idea y esa forma sirven en ese lugar."),
        ex("¿Qué debe mirar primero un artista antes de proponer una obra pública: el lugar o el color de su lápiz?", "El lugar", "La obra se piensa para el sitio donde estará."),
        ex("Un mural está pintado en el muro exterior de una plaza, a la vista de quien pasa. ¿Es un trabajo para el espacio público o para guardarlo en un cajón?", "Para el espacio público", "Está en un lugar abierto al que acceden muchas personas."),
    ],
    [
        ex("Propuesta A: un mural de niños jugando para el muro de una escuela. Propuesta B: una escultura enorme en medio de la salida de emergencia de un edificio. ¿Cuál respeta mejor el lugar?", "A", "La B bloquearía una salida de emergencia, lo que es peligroso."),
        ex("«Para la plaza propongo una escultura de un árbol hecha de cartones de colores, para recordar que hay pocos árboles». ¿Cuál es la razón de esa propuesta?", "Recordar que hay pocos árboles", "La razón viene después de «para recordar» y explica la idea."),
        ex("Dos bocetos del mismo muro: el 1 usa una figura grande y simple; el 2 usa 60 figuras diminutas. Para que se entienda mientras la gente pasa, ¿cuál conviene?", "El 1", "Una figura grande se entiende en poco tiempo y desde lejos."),
    ],
    [
        ex("Un barrio quiere un mural sobre el cuidado del agua. ¿Qué paleta y qué figura sirven más: celestes y azules con una gota grande o rojos y negros con una gota muy pequeña?", "Celestes y azules con una gota grande", "Los azules recuerdan el agua y una figura grande se ve de lejos."),
        ex("Quieres una escultura para una plaza donde juegan niños pequeños. ¿Qué forma eliges: con esquinas muy filosas o con bordes redondeados?", "Con bordes redondeados", "Los bordes redondeados son más seguros para quien juega cerca."),
        ex("Al hacer tu boceto, cambiaste el fondo de amarillo a azul oscuro porque la figura clara no se veía. ¿Qué tipo de decisión es esa?", "Una decisión de contraste para que se vea mejor", "Cambiar el fondo para que la figura destaque es una decisión de contraste."),
    ],
    [
        ex("Ana propone un mural de palabras sobre el cuidado de los parques con la frase «Todos cuidamos» en letras grandes. Luis propone copiar el mural de otra ciudad cambiando solo los colores. ¿Quién muestra más autoría?", "Ana", "Su idea nace de un tema propio; Luis solo modifica una obra ajena."),
        ex("Un vecino pide que el mural no tape la ventana de su casa, que da al muro. ¿Qué haces con tu boceto: dejar un espacio libre para la ventana o ignorar el pedido?", "Dejar un espacio libre para la ventana", "Una buena propuesta considera a las personas que usan el lugar."),
    ],
    [
        ex("Quieres mostrar en un muro de una biblioteca que leer abre mundos. ¿Qué imagen comunica mejor: un libro abierto de donde salen árboles, montañas y barcos o una pila de libros cerrados?", "Un libro abierto de donde salen árboles, montañas y barcos", "Mostrar mundos que salen del libro comunica la idea de «abrir mundos»."),
        arith("Tu muro mide 2 m de alto (200 cm) y el boceto mide 40 cm de alto. ¿Cuántas veces más grande es el muro que el boceto?", "200//40", "Se divide la altura del muro por la altura del boceto."),
    ],
    ex("En una plaza hay una esquina libre de 3 m por 3 m, junto a una banca. Piensas hacer una escultura con tres piezas de cartón forrado y pintura. ¿Dónde la pones: pegada a la banca sin dejar sentarse o a un costado, a un metro de la banca?", "A un costado, a un metro de la banca", "Se deja libre el uso de la banca y se respeta el lugar."),
    [
        ex("¿Qué cuatro partes tiene una propuesta de arte público?", "Lugar, idea, forma y razón", "Con esas partes se entiende qué se hará y por qué."),
        ex("Verdadero o falso: una obra pública puede tapar el paso si es muy bonita.", "Falso", "No debe molestar el uso ni la seguridad del lugar."),
        ex("¿Qué significa «autoría» en una obra?", "Que la idea y las decisiones son de quien la crea", "No se trata de copiar a otro."),
    ],
    task(
        "Elige UN lugar. A) El muro blanco de una cancha de barrio (6 m de largo). B) Un pasillo de un hospital con una pared larga de color crema. C) Una plaza con un espacio libre de 3 m × 3 m para una escultura. Haz dos bocetos y elige uno. Escribe la propuesta en cuatro partes: lugar, idea, forma y razón. Anota una decisión que cambiaste.",
        "Elegí la A. Boceto 1: figuras de jugadores pequeñas. Boceto 2: dos jugadores muy grandes saltando. Elijo el 2 porque se ve de lejos desde las gradas. Idea: mostrar la alegría de jugar juntos. Forma: colores amarillo y rojo sobre fondo azul. Cambié el fondo gris por azul para dar contraste.",
        ["hace dos bocetos", "escribe lugar, idea, forma y razón", "respeta el uso del lugar", "la idea es propia"],
        ["dos bocetos", "propuesta de cuatro partes", "una decisión cambiada"],
        ["copiar un mural conocido", "no considerar el lugar"],
        "Destaca la razón que usa el lugar y pregunta cómo cambiaría la propuesta si el muro fuera el doble de alto.",
    ),
    "Mira tu cuadra y di qué obra pondrías, dónde y para qué.",
    "Reformula tu propuesta para otro lugar y explica qué parte de la idea se mantiene y qué se adapta.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hoja, lápiz y colores. Para esta clase usas la descripción escrita de un mural y de una escultura que están dentro de los ejercicios.",
    "Aprenderé a interpretar y fundamentar una obra de espacio público: decir qué comunica y apoyarlo con detalles visuales, el lugar y la idea de su autor. Sirve para explicar mis propias obras y las de otros con evidencias.",
    ["Sé escribir una propuesta con lugar, idea, forma y razón.", "Sé que opinar («me gusta») no es lo mismo que fundamentar."],
    [
        "Interpretar una obra es decir qué creo que comunica. Fundamentar es apoyar esa interpretación con evidencias que se ven: colores, formas, tamaños, materiales, el lugar donde está y el título. Una interpretación sin evidencia es solo una opinión. La estructura útil es: «Creo que la obra comunica… porque se ve…». Dos personas pueden interpretar distinto una misma obra, y ambas sirven si se apoyan en lo que se ve.",
        "El lugar también es evidencia. Un mural en el muro de una escuela, con niños de muchas edades, dice algo distinto de uno en una carretera, que se ve a gran velocidad. Una escultura de una mano gigante en el desierto puede hacer pensar en la soledad y en lo grande del paisaje. El contexto ayuda a entender la intención del autor, pero no debo inventar datos sobre un artista real: solo digo lo que se ve o lo que sé con seguridad.",
        "Para mi propia obra uso la misma estructura. Después de crearla escribo qué comunica y señalo dos decisiones visuales que lo muestran, por ejemplo un fondo oscuro que destaca la figura y un tamaño grande que se lee desde lejos. Así convenzo con evidencias y no con adjetivos como «bonito» o «raro». También reviso si mi obra comunica lo que yo quería o si el público entiende otra cosa.",
    ],
    [("interpretar", "decir qué creo que comunica una obra"), ("fundamentar", "apoyar lo que digo con evidencias que se ven"), ("evidencia", "detalle visible que sostiene una idea"), ("contexto", "lugar y situación en que está la obra"), ("título", "nombre que el autor le pone a la obra")],
    [
        w("Interpretar con evidencia", "Mural «Las manos del barrio»: muchas manos de colores distintos sostienen un mismo árbol amarillo sobre fondo azul oscuro. Interpreta qué comunica.", ["Veo manos de colores distintos y un solo árbol que todas sostienen.", "El árbol amarillo destaca sobre el fondo oscuro.", "Interpreto: la comunidad, aunque diversa, cuida algo en común."], "Creo que comunica que personas distintas cuidan juntas algo común, porque todas las manos sostienen un solo árbol"),
        w("Distinguir opinión y fundamento", "Dos frases sobre el mismo mural: A) «Es muy lindo». B) «El árbol está al centro y es el más grande, por eso parece lo más importante». ¿Cuál fundamenta?", ["La A solo dice un gusto.", "La B señala dos evidencias visibles: posición y tamaño.", "Fundamentar es explicar con lo que se ve."], "La B"),
    ],
    [
        m("Escribir solo «me gustó porque es bonito».", "No dice qué comunica ni qué se ve.", "Usa «creo que comunica… porque se ve…»."),
        m("Inventar datos del artista («pintó esto porque estaba triste»).", "No se puede saber sin una fuente segura.", "Habla de lo que se ve en la obra y del lugar."),
    ],
    [
        ex("Interpretar una obra es decir qué creo que ella...", "Comunica", "Interpretar es dar un sentido a lo que se ve."),
        ex("En la frase «Creo que comunica soledad porque la figura es muy pequeña y está sola», ¿cuál es la evidencia?", "La figura es muy pequeña y está sola", "La evidencia es lo que se ve y viene después de «porque»."),
        ex("¿Cuál frase es un fundamento? A: «Me gusta». B: «El rojo del centro llama la atención por ser el único color fuerte».", "B", "La B apoya la idea con un detalle visible."),
    ],
    [
        ex("Escultura «Escalera al cielo»: peldaños de metal que suben y se cortan en el aire, en una plaza abierta. ¿Qué detalle visible apoya la idea de «un camino que no termina»?", "Los peldaños que suben y se cortan en el aire", "Una escalera que se corta sugiere que el camino continúa más allá."),
        ex("Un mural muestra una ciudad gris y, en una ventana, una maceta con flores rojas. ¿Qué elemento es el que más destaca por contraste?", "La maceta con flores rojas", "El rojo es el único color fuerte entre tonos grises."),
        ex("El título de un mural es «Todos caben». Se ven muchas personas de tamaños distintos dentro de un bus. ¿El título coincide con la imagen?", "Sí", "El bus lleno de personas distintas apoya la idea de que todos caben."),
    ],
    [
        ex("Interpretas que un mural comunica alegría. ¿Cuál evidencia es mejor: colores amarillos y naranjos con personas saltando o fondo gris con una persona sentada?", "Colores amarillos y naranjos con personas saltando", "Los colores cálidos y el movimiento sostienen la alegría."),
        ex("Un mural está en el muro de un jardín infantil. ¿Qué contexto ayuda a entender la obra: que lo verán niños pequeños o que se hizo un martes?", "Que lo verán niños pequeños", "El público cambia el tamaño de las figuras y los colores usados."),
        ex("Escribe la palabra que falta: «Creo que la obra comunica esfuerzo, ___ las figuras empujan una piedra enorme».", "porque", "El conector «porque» introduce la evidencia."),
    ],
    [
        ex("Dos personas miran la misma escultura de una mano gigante en un desierto. Ana dice «muestra soledad por el tamaño y el vacío». Beto dice «muestra pedir ayuda porque la mano se levanta». ¿Pueden ser válidas las dos?", "Sí", "Ambas se apoyan en detalles visibles; interpretar permite más de un sentido."),
        ex("Una compañera dice que un mural comunica tristeza «porque sí». ¿Qué le falta para fundamentar?", "Una evidencia visible", "Sin detalles visibles solo hay una afirmación."),
    ],
    [
        ex("Mural: una niña grande al centro, pintada de amarillo, con una pelota roja; alrededor, figuras grises y pequeñas. ¿Cuál interpretación tiene más apoyo visual: «lo importante es el juego de la niña» o «es un mural sobre una guerra»?", "Lo importante es el juego de la niña", "El tamaño, el color y el centro destacan a la niña y su pelota."),
        ex("Tu obra quería mostrar calma, pero una amiga dice que ve enojo. Notas que usaste rojo fuerte y líneas quebradas. ¿Qué evidencia explica lo que ella vio?", "El rojo fuerte y las líneas quebradas", "Esos recursos suelen sentirse tensos, no calmados."),
    ],
    ex("Ves un mural en un paradero con una niña enorme que sostiene un paraguas amarillo sobre varias personas pequeñas. Quieres escribir qué comunica. ¿Qué escribes: «Creo que comunica protección, porque el paraguas grande cubre a las personas pequeñas» o «Es hermoso y me gustó»?", "Creo que comunica protección, porque el paraguas grande cubre a las personas pequeñas", "Interpreta e incluye la evidencia visible."),
    [
        ex("¿Qué diferencia hay entre interpretar y fundamentar?", "Interpretar dice qué comunica; fundamentar lo apoya con evidencias", "Una idea se vuelve convincente al mostrar lo que se ve."),
        ex("Verdadero o falso: una misma obra pública puede interpretarse de maneras distintas si hay evidencias.", "Verdadero", "Cada interpretación válida se apoya en detalles que se ven."),
        ex("¿Por qué el lugar de una obra es parte de la evidencia?", "Porque ayuda a entender su sentido", "Un mismo dibujo dice cosas distintas en una escuela o en una carretera."),
    ],
    task(
        "Elige UNA obra descrita. A) Mural «El mercado despierta»: puestos de frutas de colores brillantes, personas que sonríen y un sol grande detrás, todo en tonos cálidos. B) Escultura «Puente de tapas»: una pasarela hecha de miles de tapas de plástico de colores que une dos bancas de una plaza. C) Mural «Silencio»: una ciudad en azul oscuro y una sola ventana encendida. Escribe una interpretación («Creo que comunica… porque se ve…») con dos evidencias y una frase sobre cómo influye el lugar donde estaría.",
        "Elegí la C. Creo que comunica soledad en la noche, porque casi todo es azul oscuro y solo hay una ventana encendida. Dos evidencias: el azul oscuro cubre casi todo y la ventana es la única luz. Si estuviera en una calle de noche, haría sentir compañía a quien pasa.",
        ["dice qué comunica", "usa dos evidencias visibles", "no inventa datos del autor", "relaciona la obra con su lugar"],
        ["interpretación escrita con «porque»", "dos evidencias"],
        ["opinar sin evidencias", "inventar datos del autor"],
        "Pide que señale cada evidencia en la descripción y que diga si otra persona podría interpretar la obra de otra forma.",
    ),
    "Elige una imagen o un muro de tu barrio y completa en voz alta: «Creo que comunica… porque se ve…».",
    "Escribe una segunda interpretación posible de la misma obra con otra evidencia distinta.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA1, 6,
    "Tu boceto de mural o escultura de la clase anterior (o el boceto descrito en esta clase), lápiz y colores. Los comentarios de otras personas están escritos aquí.",
    "Aprenderé a revisar mi obra con comentarios de otras personas sin perder mi autoría: escuchar, elegir qué cambio y mantener mi intención. Sirve para mejorar una obra sin dejar de ser yo quien decide.",
    ["Sé interpretar y fundamentar una obra con evidencias.", "Sé que autoría quiere decir que las decisiones son mías."],
    [
        "Revisar es mirar de nuevo mi obra para mejorarla. Los comentarios de compañeros, familiares o docentes ayudan porque ven cosas que yo ya no veo. Pero no tengo que aceptar todo lo que me digan. Primero escucho sin discutir. Luego comparo cada comentario con mi intención: si lo que me piden ayuda a comunicar mejor mi idea, lo uso; si cambia mi idea por la de otra persona, lo agradezco y no lo aplico.",
        "Un buen comentario señala un detalle visible y una razón. Por ejemplo: «El fondo gris hace que la figura se pierda; si lo cambias por un color más oscuro se vería más». Un comentario poco útil es «cámbialo, no me gusta». Cuando reviso, hago un registro corto con tres partes: qué me dijeron, qué decidí hacer y cómo cambia el efecto en mi obra. También anoto lo que decidí no cambiar y por qué.",
        "Conservar la autoría no significa no cambiar nada. Significa que yo decido el cambio y que mi idea sigue reconocible. Si después de la revisión una persona vuelve a mirar mi obra, debería poder decir qué quería comunicar. Si en cambio la obra ahora dice otra cosa porque seguí todas las sugerencias, perdí mi intención. Al final comparo la versión 1 y la versión 2 y explico qué mejoró.",
    ],
    [("revisar", "mirar de nuevo la obra para mejorarla"), ("comentario", "opinión de otra persona sobre mi obra"), ("autoría", "que la idea y las decisiones finales son mías"), ("versión", "etapa de una obra, como la versión 1 y la versión 2"), ("registro", "nota corta de lo que cambié y por qué")],
    [
        w("Elegir qué comentario usar", "Tu intención: mostrar la alegría de un patio de escuela con colores cálidos. Te dicen: A) «Las figuras se pierden porque el fondo es amarillo claro». B) «Mejor pinta todo de gris, es más serio». ¿Qué haces con cada una?", ["La A ayuda a que se vea la alegría: pruebo un fondo más oscuro.", "La B cambia la idea de alegría por seriedad.", "Uso la A y agradezco la B sin aplicarla."], "Aplico la A y no aplico la B"),
        w("Hacer el registro", "Cambiaste el fondo del mural de amarillo claro a azul oscuro. Escribe el registro de tres partes.", ["Me dijeron: las figuras se pierden.", "Decidí: cambiar el fondo a azul oscuro.", "Efecto: las figuras amarillas ahora destacan por contraste."], "Me dijeron que las figuras se perdían; cambié el fondo a azul oscuro; ahora destacan"),
    ],
    [
        m("Aplicar todos los comentarios aunque cambien mi idea.", "La obra deja de ser mía y pierde su intención.", "Compara cada comentario con tu intención y elige."),
        m("No cambiar nada porque «a mí me gusta así».", "Se pierde la ayuda que da mirar con ojos nuevos.", "Escucha y prueba al menos un cambio útil."),
    ],
    [
        ex("¿Qué haces primero cuando recibes un comentario sobre tu obra: escuchar o discutir?", "Escuchar", "Escuchar permite entender qué vio la otra persona."),
        ex("Un comentario útil señala un detalle visible y una...", "Razón", "Con la razón se entiende por qué conviene cambiar."),
        ex("«Cámbialo, no me gusta.» ¿Es un comentario útil o poco útil?", "Poco útil", "No dice qué detalle cambiar ni por qué."),
    ],
    [
        ex("¿Cuál comentario es más útil? A: «La palabra del letrero es muy chica y no se lee desde la calle». B: «Está raro».", "A", "La A indica un detalle y un problema concreto."),
        ex("Tu intención es mostrar la calma de una plaza con colores suaves. Te sugieren pintar una explosión roja al centro. ¿Esa sugerencia ayuda a tu intención?", "No", "Un rojo fuerte rompe la calma que querías mostrar."),
        ex("El registro de una revisión tiene tres partes: lo que te dijeron, lo que decidiste y...", "El efecto", "El registro de tres partes incluye qué cambió y qué efecto produjo."),
    ],
    [
        ex("Tu escultura de cartón se cae cuando la tocas. Una compañera te dice: «Hazle una base más ancha». ¿Qué decides: ensanchar la base o hacer la figura más alta?", "Ensanchar la base", "Una base más ancha da estabilidad."),
        ex("Te sugieren cambiar el título de tu obra de «Sueño de un patio» a un nombre que no te gusta. Tu intención no cambia. ¿Qué haces: cambiar la obra completa o decidir tú si cambias el título?", "Decidir yo si cambio el título", "Las decisiones finales son del autor, aunque escuche opiniones."),
        ex("Dos comentarios sobre tu mural de colores cálidos: 1) «Usa más contraste entre figura y fondo». 2) «Pinta todo de verde». Tu intención es el calor del verano. ¿Cuál aplicas?", "El 1", "Mejora la lectura sin cambiar la idea del calor."),
    ],
    [
        ex("Tras la revisión, dos personas miran tu obra: una dice que comunica alegría y la otra no sabe qué comunica. Tu intención era alegría. ¿Cuál resultado muestra que tu intención se mantiene?", "La persona que dice que comunica alegría", "Esa lectura coincide con la intención original."),
        ex("Un compañero aplicó todas las sugerencias y su obra ahora comunica algo que él no quería. ¿Qué perdió?", "Su intención", "Al aplicar todo, cambió la idea que quería comunicar."),
    ],
    [
        ex("Tu mural de un paradero muestra «esperar con otros». Recibes: A) «Agranda a las personas para que se vean desde lejos». B) «Quita a las personas y deja solo el paradero». ¿Qué comentario mantiene tu idea?", "A", "Quitar a las personas elimina «esperar con otros»; agrandarlas la refuerza."),
        arith("Tu versión 1 tenía 9 figuras pequeñas y en la versión 2 agregas 6 figuras grandes más. ¿Cuántas figuras tiene la versión 2?", "9+6", "Se suman las figuras de la versión 1 y las nuevas."),
    ],
    ex("Tu boceto de escultura para la plaza tiene una base angosta. Un vecino dice que se podría caer sobre los niños. Tu intención era una figura alta y delgada. ¿Qué decides: mantener la figura delgada pero ensanchar la base, o hacerla baja y gruesa?", "Mantener la figura delgada pero ensanchar la base", "Mejora la seguridad y conserva la idea de una figura alta y delgada."),
    [
        ex("¿Qué es el registro de revisión?", "Una nota de lo que me dijeron, lo que decidí y el efecto", "Permite seguir el proceso y justificar cambios."),
        ex("Verdadero o falso: conservar la autoría significa no cambiar nunca nada.", "Falso", "Se puede cambiar, pero las decisiones finales son del autor."),
        ex("¿Con qué debo comparar cada comentario antes de aplicarlo?", "Con mi intención", "Si ayuda a comunicar mejor mi idea, lo uso."),
    ],
    task(
        "Elige UN boceto para revisar. A) Un mural de una feria con figuras pequeñas sobre un fondo amarillo claro; intención: mostrar la alegría del mercado. B) Una escultura de cartón de un pájaro con la base muy angosta; intención: mostrar libertad. C) Un mural de un paradero con letras muy chicas; intención: dar ánimo a quien espera. Recibes estos tres comentarios: 1) «Las figuras se pierden en el fondo». 2) «Mejor haz una escena más seria». 3) «Haz las letras o las figuras más grandes». Escribe qué comentario aplicas, cuál no y el registro de tres partes.",
        "Elegí la A. Aplico el 1: cambio el fondo a azul oscuro porque las figuras se perdían. No aplico el 2, porque mi intención es alegría. Registro: me dijeron que las figuras se perdían; cambié el fondo; ahora las figuras amarillas destacan y la alegría se ve más.",
        ["decide qué comentario aplica y cuál no", "justifica con su intención", "escribe el registro de tres partes", "mantiene la idea original"],
        ["lista de comentarios con decisión", "registro de tres partes"],
        ["aceptar todo sin pensar", "rechazar todo"],
        "Pregunta qué sigue siendo igual entre la versión 1 y la versión 2 y cómo se nota la intención.",
    ),
    "Pide a una persona de tu casa un comentario sobre un dibujo tuyo y responde con «Gracias, voy a probar…» o «Gracias, no lo cambiaré porque…».",
    "Haz una versión 2 de tu boceto aplicando un solo cambio y escribe cómo cambia el efecto.",
)

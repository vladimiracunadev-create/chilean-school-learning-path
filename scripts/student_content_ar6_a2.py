"""Cuaderno del estudiante de 6.º básico Artes Visuales: AR06 OA 02 (aplicar y combinar el color: gamas y contrastes, y el volumen: lleno y vacío)."""
from __future__ import annotations

from student_content_ar6_a import lesson, m, task, w
from student_lessons import arith, ex

OA2 = "AR06 OA 02"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Lápices de colores o témpera (rojo, amarillo, azul, blanco), una hoja y un lápiz de mina. Las escenas que se describen están escritas aquí.",
    "Aprenderé qué es una gama de color (cálida, fría y monocromática) y a elegirla según lo que quiero expresar. Sirve para que los colores de mis trabajos de arte y diseños digan algo a propósito y no al azar.",
    ["Conozco los colores primarios (rojo, amarillo y azul) y los secundarios (naranjo, verde y violeta).", "Sé que la intención es lo que quiero comunicar con mi obra."],
    [
        "Una gama de color es un grupo de colores que se llevan bien entre sí y que dan una misma sensación. La gama cálida reúne rojos, naranjos y amarillos; recuerda el fuego, el sol y el calor, y da sensación de energía. La gama fría reúne azules, verdes y violetas; recuerda el agua, el hielo y la sombra, y da sensación de calma, frescura o distancia. Estas gamas son una convención: sirven como guía, no como regla que no se pueda romper.",
        "La gama monocromática usa un solo color en versiones más claras y más oscuras. Se logra agregando blanco para aclarar y un poco de negro, o de un color más oscuro, para oscurecer. Una obra monocromática en azul, por ejemplo, tiene celestes, azules medios y azules profundos. Se ve muy unida y puede dar mucha atmósfera, porque todo parece del mismo mundo.",
        "Elegir una gama es tomar una decisión visual con intención. Si quiero mostrar la calma de un lago al amanecer, uso gama fría. Si quiero mostrar el calor de un mercado lleno de gente, uso gama cálida. A veces uso casi todo de una gama y agrego una mancha pequeña de la otra para que llame la atención. Primero escribo qué quiero expresar y después elijo la gama.",
    ],
    [("gama", "grupo de colores que dan una misma sensación"), ("gama cálida", "rojos, naranjos y amarillos"), ("gama fría", "azules, verdes y violetas"), ("monocromática", "que usa un solo color en versiones claras y oscuras"), ("sensación", "lo que siente quien mira la obra")],
    [
        w("Elegir la gama", "Quieres pintar una noche tranquila junto al mar. ¿Qué gama eliges y qué colores usas?", ["La intención es calma, no energía.", "La gama fría da sensación de calma.", "Uso azul oscuro, violeta y verde azulado."], "Gama fría: azul oscuro, violeta y verde azulado"),
        w("Reconocer una monocromática", "Una pintura de un cerro tiene solo cafés: café muy claro, café medio y café oscuro. ¿Qué gama usa?", ["Hay un solo color.", "Aparece en versiones más claras y más oscuras.", "Eso es una gama monocromática."], "Monocromática de café"),
    ],
    [
        m("Pensar que las gamas son reglas obligatorias y que nunca se pueden mezclar.", "Son guías de sensación; los artistas combinan según su intención.", "Elige primero la intención y luego la gama; mezcla a propósito."),
        m("Llamar monocromática a una obra que usa rojo, azul y amarillo.", "Monocromática es un solo color con claros y oscuros.", "Cuenta cuántos colores distintos hay antes de nombrar la gama."),
    ],
    [
        ex("¿El naranjo pertenece a la gama cálida o a la fría?", "A la cálida", "El naranjo recuerda el fuego y el sol."),
        ex("¿Cuál de estos colores es de la gama fría: violeta o amarillo?", "Violeta", "Violeta, azul y verde son fríos; el amarillo es cálido."),
        ex("Un dibujo usa solo celeste, azul medio y azul oscuro. ¿Qué gama es?", "Monocromática", "Es un solo color en versiones claras y oscuras."),
    ],
    [
        ex("Un atardecer tiene un cielo naranjo, un sol rojo y cerros amarillos. ¿Qué gama domina?", "La cálida", "Naranjo, rojo y amarillo son colores cálidos."),
        ex("«Quiero mostrar la frescura de un bosque en la mañana, con verdes y azules, porque así se siente aire limpio.» ¿Qué gama eligió quien escribió esto?", "La fría", "Verdes y azules forman la gama fría."),
        ex("¿Qué sensación da más una gama cálida: energía y calor o calma y distancia?", "Energía y calor", "Los colores cálidos recuerdan el sol y el fuego."),
    ],
    [
        ex("Quieres mostrar la calma de un lago de noche. ¿Qué colores eliges? A: rojo, naranjo y amarillo. B: azul oscuro, violeta y verde azulado.", "B", "La gama fría da sensación de calma."),
        ex("Tienes lápices rojo, azul y amarillo. Para dibujar una estufa encendida en una pieza, ¿qué dos usas más?", "Rojo y amarillo", "Son cálidos y recuerdan el fuego."),
        arith("Un cuadro tiene 12 manchas de color: 8 son cálidas y el resto son frías. ¿Cuántas son frías?", "12-8", "Se resta el total menos las cálidas."),
    ],
    [
        ex("Dos dibujos del mismo mar. Ana usa solo celestes, azules y verdes. Luis usa rojos y naranjos. Ambos quieren mostrar frío. ¿Quién elige mejor la gama?", "Ana", "Los celestes, azules y verdes son fríos."),
        ex("Camila pinta una ciudad de noche toda en azul oscuro, con una sola ventana naranja. ¿Cuál es la gama que domina y qué detalle destaca?", "Domina la fría y destaca la ventana naranja", "El color cálido pequeño llama la atención entre mucho color frío."),
    ],
    [
        ex("Pintaste un cuadro casi todo en azul y verde, con una sola mancha roja. ¿Qué efecto produce la mancha roja: pasa desapercibida o llama la atención?", "Llama la atención", "Es la única mancha cálida entre colores fríos."),
        ex("Un dibujo con muchos rojos y naranjos se ve muy agitado y quieres que se sienta más tranquilo. ¿Qué haces: agregar más rojo o incluir celestes y verdes azulados?", "Incluir celestes y verdes azulados", "Los colores fríos bajan la energía de la imagen."),
    ],
    ex("Te piden un afiche sobre el verano que da la idea de frescura de una bebida helada. ¿Qué gama usas en la bebida: azules y celestes o rojos y naranjos?", "Azules y celestes", "La gama fría transmite frescura."),
    [
        ex("¿Qué colores forman la gama cálida?", "Rojos, naranjos y amarillos", "Recuerdan el sol y el fuego."),
        ex("Verdadero o falso: una obra monocromática usa solo un color en versiones claras y oscuras.", "Verdadero", "Esa es la definición de monocromática."),
        ex("¿Qué se elige primero: la gama o la intención?", "La intención", "La gama se elige para expresar lo que quiero comunicar."),
    ],
    task(
        "Elige UNA situación. A) El mediodía en una playa muy calurosa. B) Una mañana fría con neblina en un lago. C) Un mercado lleno de frutas y gente a media tarde. Haz tres cuadros de 4 cm × 4 cm con la gama que elijas y un cuarto cuadro con la gama contraria. Escribe tu intención y por qué elegiste esa gama.",
        "Elegí la B. Pinté tres cuadros fríos (celeste, gris azulado y verde) y uno cálido (naranjo). Intención: mostrar el frío tranquilo de una mañana de neblina, con celestes y grises azulados, porque esos colores dan sensación de frío.",
        ["pinta cuadros con una gama clara", "incluye un cuadro de la gama contraria", "escribe la intención", "explica la sensación del color"],
        ["cuatro cuadros de color", "intención escrita"],
        ["mezclar gamas sin intención", "elegir colores sin explicar la sensación"],
        "Pregunta qué sensación cambia entre el cuadro cálido y los fríos y cuál de los dos sirve mejor a su intención.",
    ),
    "Mira tu pieza y di qué objetos son de gama cálida y cuáles de gama fría.",
    "Haz una gama monocromática de cinco pasos, del color más claro al más oscuro, y descríbela.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Lápices de colores o témpera (rojo, verde, azul, naranjo, amarillo, violeta, blanco, negro), hoja y pincel. Todos los pares de colores están nombrados en esta clase.",
    "Aprenderé a producir contrastes con el color (de complementarios, de claro y oscuro y de cálido y frío) y a probar cuál sirve para una intención. Sirve para que lo importante de un trabajo se vea y se entienda.",
    ["Sé qué son las gamas cálida, fría y monocromática.", "Sé que una variable visual es una decisión que se cambia para ver su efecto."],
    [
        "Un contraste es una diferencia fuerte entre dos elementos que hace que uno destaque junto al otro. Con el color hay varios contrastes. Los colores complementarios están opuestos en el círculo cromático: rojo y verde, azul y naranjo, amarillo y violeta. Puestos juntos se hacen notar más el uno al otro. El contraste de valor es la diferencia entre claro y oscuro, como amarillo claro sobre azul muy oscuro. El contraste de temperatura enfrenta un color cálido con uno frío.",
        "Para decidir qué contraste usar, hago pruebas pequeñas. Pinto un mismo dibujo simple, por ejemplo una estrella, sobre tres fondos distintos: uno de color complementario, uno de color parecido y uno muy claro. Cambio solo el fondo y dejo todo lo demás igual. Después miro desde lejos cuál estrella se destaca más y comparo con lo que quería comunicar.",
        "Un contraste fuerte llama la atención, pero también puede cansar si se usa en toda la obra. Si todo contrasta, nada destaca. Por eso conviene dejar el contraste más fuerte para lo más importante y usar colores más parecidos para el resto. Las gamas y los contrastes se combinan: puedo pintar un fondo frío y una figura pequeña naranja, que es complementaria del azul.",
    ],
    [("contraste", "diferencia fuerte entre dos elementos que hace que uno destaque"), ("complementarios", "colores opuestos en el círculo cromático, como rojo y verde"), ("valor", "qué tan claro u oscuro es un color"), ("círculo cromático", "círculo que ordena los colores"), ("destacar", "hacer que algo se note más que el resto")],
    [
        w("Escoger el fondo", "Pintarás una estrella naranja y quieres que se destaque mucho. Pruebas fondo azul, fondo rojo y fondo amarillo claro. ¿Cuál sirve más?", ["El azul y el naranjo son complementarios.", "El rojo y el amarillo claro son más parecidos al naranjo.", "El fondo azul hace que la estrella se note más."], "El fondo azul"),
        w("Contraste de valor", "Una figura amarilla clara se ve sobre un fondo azul muy oscuro o sobre un fondo amarillo pálido. ¿En cuál se ve mejor?", ["Mira cuánta diferencia hay entre claro y oscuro.", "Entre amarillo claro y azul muy oscuro la diferencia es grande.", "Entre amarillo claro y amarillo pálido es pequeña."], "En el fondo azul muy oscuro"),
    ],
    [
        m("Pintar todo con contrastes fuertes para que se vea más.", "Si todo contrasta, nada destaca.", "Reserva el contraste más fuerte para lo más importante."),
        m("Cambiar el fondo y también la forma de la figura en la misma prueba.", "No se sabe qué cambio produjo el efecto.", "Cambia solo una cosa por prueba."),
    ],
    [
        ex("¿Cuál es el color complementario del rojo?", "Verde", "El rojo y el verde están opuestos en el círculo cromático."),
        ex("¿Cuál de estos pares son complementarios: amarillo y violeta o rojo y naranjo?", "Amarillo y violeta", "El violeta es el opuesto del amarillo."),
        ex("Un círculo blanco sobre fondo negro, ¿qué contraste usa principalmente: de valor o de complementarios?", "De valor", "Blanco y negro son lo más claro y lo más oscuro."),
    ],
    [
        ex("Un cartel pone naranjo sobre azul. ¿Esos colores son complementarios?", "Sí", "Azul y naranjo están opuestos en el círculo cromático."),
        ex("¿Qué efecto produce poner dos colores complementarios juntos: se destacan más o se confunden?", "Se destacan más", "Cada uno hace más notorio al otro."),
        ex("Contraste de temperatura: ¿qué enfrenta?", "Un color cálido con uno frío", "Por ejemplo, un rojo con un azul."),
    ],
    [
        ex("Quieres que una estrella violeta se vea mucho. ¿Qué fondo eliges: amarillo o azul violáceo?", "Amarillo", "El amarillo es el complementario del violeta."),
        ex("Tu figura es verde oscuro. ¿Qué fondo da más contraste de valor: verde claro muy pálido o verde casi negro?", "Verde claro muy pálido", "La diferencia entre oscuro y muy claro es mayor."),
        ex("Quieres un pájaro pequeño que llame la atención en una pintura de un cielo azul. ¿De qué color lo pintas?", "Naranjo", "El naranjo es complementario del azul y destaca."),
    ],
    [
        ex("Prueba 1: una flor roja sobre fondo verde. Prueba 2: una flor roja sobre fondo anaranjado. Quieres que la flor destaque mucho. ¿Qué prueba sirve más?", "La 1", "Rojo y verde son complementarios; rojo y naranjo son muy parecidos."),
        ex("Un afiche tiene fondo rojo, letras verdes, ilustración azul y marco naranjo, todo en contraste fuerte. Un compañero dice que cansa la vista. ¿Tiene razón?", "Sí", "Con tantos contrastes fuertes nada destaca y la imagen cansa."),
    ],
    [
        ex("Una pintura de un lago es toda de azules suaves y quieres destacar un pequeño bote. ¿De qué color lo pintas para el mayor contraste: naranjo vivo o celeste claro?", "Naranjo vivo", "El naranjo es complementario del azul y contrasta."),
        ex("Quieres que el texto de un cartel se lea de lejos. Usarás el mayor contraste de valor posible. ¿Qué combinación eliges: letras amarillas sobre fondo azul muy oscuro o letras celestes sobre fondo azul claro?", "Letras amarillas sobre fondo azul muy oscuro", "Hay mucha diferencia entre claro y oscuro."),
    ],
    ex("Diseñas una portada para un libro de aventuras de mar. El título es violeta y quieres que se lea muy bien. ¿Qué color de fondo usas: amarillo claro o violeta oscuro?", "Amarillo claro", "Amarillo es complementario del violeta y además más claro."),
    [
        ex("¿Cuál es el color complementario del azul?", "Naranjo", "El azul y el naranjo están opuestos en el círculo cromático."),
        ex("Verdadero o falso: un contraste de valor depende de qué tan claro u oscuro es cada color.", "Verdadero", "El valor mide la claridad del color."),
        ex("¿Por qué conviene dejar el contraste más fuerte para lo más importante?", "Porque si todo contrasta, nada destaca", "El contraste fuerte debe guiar la mirada a un solo lugar."),
    ],
    task(
        "Elige UN dibujo simple. A) Una estrella naranja. B) Un pez violeta. C) Una flor roja. Dibújalo tres veces del mismo tamaño y pinta tres fondos: uno complementario, uno de color parecido y uno muy claro o muy oscuro. Mira desde lejos y escribe cuál contrasta más y qué intención comunicaría.",
        "Elegí la A. Fondos: azul, rojo y amarillo claro. La estrella sobre azul destaca más por ser complementaria. Intención: mostrar una luz que brilla en la noche, con una estrella naranja y un fondo azul.",
        ["hace tres pruebas con el mismo dibujo", "cambia solo el fondo", "nombra cuál contrasta más y por qué", "escribe una intención"],
        ["tres dibujos con distintos fondos", "frase de comparación"],
        ["cambiar varias cosas a la vez", "elegir sin comparar"],
        "Pregunta qué tipo de contraste hay en la mejor prueba y cómo se relaciona con lo que quería comunicar.",
    ),
    "Mira un objeto de un color y busca cerca un objeto de su complementario.",
    "Haz un cartel con dos colores complementarios y explica dónde pones el contraste más fuerte.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Hojas de cartulina o cartón delgado, papel de diario o de revista limpio, tijeras de punta redonda, cola fría y regla. No se usan cuchillos ni cortadores.",
    "Aprenderé qué es el volumen y qué son sus partes llenas y vacías, y a elegir materiales y procedimientos para producirlos. Sirve para hacer una escultura o un diseño donde el hueco también cuenta.",
    ["Sé que una escultura tiene volumen y se puede mirar por todos lados.", "Sé usar tijeras de punta redonda y cola fría con cuidado."],
    [
        "El volumen es lo que ocupa espacio y se puede rodear con la mirada: una caja, una escultura, una jarra. La parte llena de un volumen es la que tiene material, como un cubo de cartón. La parte vacía es el espacio sin material: un hueco, una ventana, un agujero o el espacio entre dos piezas. En una obra, el vacío no es «nada»: es una parte que se diseña, porque cambia cómo se ve la forma y por dónde pasa la luz.",
        "Los materiales cambian lo que puedo hacer. Con cartulina puedo doblar y pegar cajas y cilindros. Con cartón delgado puedo cortar ventanas, que crean vacíos. Con papel de diario enrollado puedo hacer tubos que dejan espacio por dentro. Los procedimientos básicos son doblar, pegar, enrollar, apilar y perforar con tijeras de punta redonda. Siempre se recorta con cuidado y alejando los dedos del filo.",
        "Para probar lleno y vacío hago dos pruebas con el mismo tamaño: una caja casi cerrada y otra con varias ventanas. Comparo cuál se ve más pesada y cuál más ligera, y por dónde se ve el interior. Muchas veces conviene combinar partes llenas y vacías: lo lleno da peso y fuerza; lo vacío da ligereza, ritmo y permite ver a través. Así el espacio también forma parte de la obra.",
    ],
    [("volumen", "lo que ocupa espacio y se puede rodear"), ("lleno", "parte del volumen que tiene material"), ("vacío", "espacio sin material, como un hueco o una ventana"), ("procedimiento", "pasos para hacer algo, como doblar, pegar y enrollar"), ("maqueta", "versión pequeña de una obra o un edificio")],
    [
        w("Reconocer lleno y vacío", "Una escultura de cartón es una caja con tres ventanas cuadradas. ¿Qué partes son llenas y cuáles vacías?", ["Las paredes de cartón tienen material.", "Las ventanas son agujeros sin material.", "Las paredes son lo lleno y las ventanas lo vacío."], "Paredes: llenas; ventanas: vacías"),
        w("Elegir material", "Quieres una torre muy liviana que deje pasar la luz. ¿Sirve más una caja cerrada de cartón grueso o un tubo de papel enrollado con ventanas?", ["La torre debe ser liviana y dejar pasar luz.", "La caja cerrada es pesada y no deja pasar luz.", "Las ventanas dejan pasar la luz."], "El tubo de papel con ventanas"),
    ],
    [
        m("Pensar que el vacío es lo que sobró y no importa.", "El vacío cambia el peso, la forma y la luz de la obra.", "Decide dónde van los huecos como decides dónde va el material."),
        m("Cortar tantas ventanas que la pieza se debilita y se rompe.", "Si queda muy poco material se pierde la estructura.", "Deja bordes firmes entre las ventanas."),
    ],
    [
        ex("En una caja con ventanas, ¿las ventanas son parte llena o parte vacía?", "Parte vacía", "Una ventana es un hueco sin material."),
        ex("¿Qué material permite doblar y pegar cajas: la cartulina o una piedra?", "La cartulina", "La cartulina se dobla y se pega para crear volúmenes."),
        ex("El espacio entre dos piezas de una escultura, ¿es lleno o vacío?", "Vacío", "No tiene material, pero forma parte de la obra."),
    ],
    [
        ex("¿Qué parte de una escultura da sensación de peso: lo lleno o lo vacío?", "Lo lleno", "Más material se siente más pesado."),
        ex("Dos cajas del mismo tamaño: A) cerrada y B) con seis ventanas. ¿Cuál deja ver mejor el interior?", "La B", "Las ventanas son vacíos que dejan ver."),
        ex("¿Qué es un procedimiento: los pasos para hacer algo o el color de una pieza?", "Los pasos para hacer algo", "Un procedimiento ordena cómo se trabaja."),
    ],
    [
        arith("Una torre de cartón tiene 4 pisos y cada piso tiene 3 ventanas. ¿Cuántas ventanas (vacíos) tiene la torre?", "4*3", "Se multiplica pisos por ventanas de cada piso."),
        ex("Quieres una pieza que parezca ligera y muestre ritmo. ¿Qué haces: cortar ventanas del mismo tamaño repetidas en fila o dejar la caja totalmente cerrada?", "Cortar ventanas repetidas en fila", "Los vacíos repetidos crean ritmo y ligereza."),
        ex("Para hacer un tubo de papel de diario, ¿qué procedimiento usas: enrollar o cortar en trozos pequeños?", "Enrollar", "Enrollar el papel forma el tubo."),
    ],
    [
        ex("Dos maquetas de un faro: la de Sofía es una torre cerrada y pesada; la de Pedro es una torre con ventanas altas por donde pasa la luz. Se busca mostrar que el faro «deja pasar la luz». ¿Cuál lo muestra mejor?", "La de Pedro", "Sus ventanas son vacíos que dejan pasar luz."),
        ex("Un compañero dice: «Mi escultura tiene vacío porque está a medio terminar». ¿Es un vacío diseñado?", "No", "Un vacío diseñado se decide a propósito para producir un efecto."),
    ],
    [
        ex("Quieres que una escultura de cartulina parezca flotar. ¿Qué diseñas: base ancha totalmente llena o base con aberturas y apoyos delgados?", "Base con aberturas y apoyos delgados", "Los vacíos bajo la forma dan sensación de ligereza."),
        arith("Una maqueta tiene 5 cuerpos de caja y entre cada par seguido queda un espacio vacío. ¿Cuántos espacios vacíos hay entre los cuerpos?", "5-1", "Entre 5 piezas seguidas hay 4 espacios."),
    ],
    ex("Tienes tres hojas de cartulina y quieres hacer un pequeño refugio para una planta que deje pasar el aire. ¿Haces una caja totalmente cerrada o una caja con ventanas?", "Una caja con ventanas", "Las ventanas son vacíos por donde pasa el aire."),
    [
        ex("¿Qué es un vacío en una obra con volumen?", "Un espacio sin material", "Puede ser un hueco o el espacio entre piezas."),
        ex("Verdadero o falso: el vacío se diseña igual que lo lleno.", "Verdadero", "Su tamaño y posición cambian el efecto."),
        ex("¿Qué procedimiento sirve para hacer una caja con cartulina?", "Doblar y pegar", "Doblar forma las caras y pegar las une."),
    ],
    task(
        "Elige UN tema. A) Una torre ligera que deje pasar la luz. B) Un refugio para una planta con aire. C) Un edificio fuerte y pesado. Con cartulina y tijeras de punta redonda haz dos maquetas pequeñas del tema: una casi llena y otra con vacíos. Anota qué materiales y qué pasos usaste y cuál comunica mejor.",
        "Elegí la A. Maqueta 1: caja cerrada de cartulina. Maqueta 2: tubo enrollado con cuatro ventanas. Pasos: dibujar, doblar, pegar con cola fría y cortar las ventanas. La 2 comunica mejor, porque las ventanas dejan pasar la luz.",
        ["hace dos maquetas con lleno y vacío distintos", "nombra materiales y pasos", "compara cuál comunica mejor", "usa las tijeras con cuidado"],
        ["dos maquetas", "lista de pasos"],
        ["cortar demasiado y debilitar la pieza", "no justificar la elección"],
        "Pide que señale qué parte es llena y cuál vacía en cada maqueta y qué efecto da cada una.",
    ),
    "Mira un objeto de tu casa (una silla o una reja) y señala qué parte es llena y cuál es vacía.",
    "Diseña un volumen donde el vacío ocupe más lugar que lo lleno y explica por qué se sostiene.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Cartulina o cartón delgado, tijeras de punta redonda, cola fría, lápices de colores o témpera y una hoja para el boceto. Las ideas que se ofrecen están escritas aquí.",
    "Aprenderé a combinar gama de color, contraste y volumen lleno y vacío en una misma obra con un propósito expresivo. Sirve para crear una maqueta o un diseño donde color y espacio dicen lo mismo.",
    ["Sé elegir una gama de color y un contraste.", "Sé que en una obra con volumen lo lleno y lo vacío se diseñan."],
    [
        "Combinar elementos del lenguaje visual es usar varios a la vez para decir una misma cosa. Si quiero mostrar la calma de un puerto al amanecer, uso una gama fría de azules y celestes y un volumen con muchos vacíos, que da aire. Si quiero mostrar la fuerza de un edificio, uso colores cálidos y oscuros y un volumen muy lleno. Cuando color y volumen apoyan la misma idea, la obra se entiende mejor.",
        "Los propósitos expresivos son lo que quiero lograr: calma, energía, alegría, soledad o peso. Puedo escribir mi propósito y luego decidir tres cosas: la gama de color, dónde pongo el contraste más fuerte y qué partes del volumen serán llenas o vacías. Pongo el color en lo lleno y dejo lo vacío como una pausa. El contraste fuerte lo dejo en el lugar más importante, por ejemplo una puerta naranja en un edificio azul.",
        "Mi obra debe ser propia: puedo mirar casas, torres o puentes de mi ciudad, pero no copio uno exacto. Hago un boceto con notas, construyo la maqueta y reviso desde lejos. Pregunto: ¿se entiende mi propósito? ¿Algún color o hueco lo contradice? Anoto un cambio que hice y por qué. Una buena obra no tiene todos los recursos posibles, sino los que sirven a su idea.",
    ],
    [("propósito expresivo", "lo que quiero lograr o comunicar con la obra"), ("combinar", "usar varios recursos a la vez para una misma idea"), ("maqueta", "versión pequeña de una obra o un edificio"), ("boceto", "dibujo previo con notas"), ("coherencia", "que todas las decisiones apoyan la misma idea")],
    [
        w("Diseñar con propósito", "Propósito: mostrar la calma de un puerto al amanecer con una maqueta de edificios de cartulina. Decide gama, contraste y vacíos.", ["Gama fría de azules y celestes por la calma.", "Contraste: una sola puerta naranja pequeña, para que se note el punto central.", "Volumen con varias ventanas altas y espacios vacíos entre edificios, para dar aire."], "Azules y celestes, una puerta naranja y muchos vacíos entre los edificios"),
        w("Detectar una contradicción", "Alguien quiere mostrar calma, pero pinta la maqueta de rojo fuerte con muy pocos vacíos y letras en contraste violento. ¿Qué recursos contradicen el propósito?", ["El rojo fuerte es energía, no calma.", "Los pocos vacíos dan sensación de peso.", "El contraste violento tensiona la imagen."], "El rojo fuerte, los pocos vacíos y el contraste violento"),
    ],
    [
        m("Usar todos los colores y huecos posibles para que la obra «tenga de todo».", "Los recursos que no apoyan la idea la confunden.", "Elige solo los recursos que sirven al propósito."),
        m("Decidir el color y el volumen sin escribir antes el propósito.", "Sin propósito, las decisiones no se pueden justificar.", "Escribe primero qué quieres lograr."),
    ],
    [
        ex("Combinar recursos del lenguaje visual es usar varios...", "A la vez para una misma idea", "Se combinan color, forma y espacio para apoyar el propósito."),
        ex("Propósito: calma. ¿Qué gama encaja mejor: fría o cálida?", "Fría", "Azules y celestes dan sensación de calma."),
        ex("¿Qué es una maqueta: una versión pequeña de una obra o un cuaderno de apuntes?", "Una versión pequeña de una obra", "La maqueta permite probar antes de hacer la obra definitiva."),
    ],
    [
        ex("Una maqueta de una escuela muestra «alegría»: colores amarillos y naranjos y muchas ventanas grandes. ¿Qué parte de esa maqueta es vacío?", "Las ventanas", "Una ventana es un hueco sin material."),
        ex("Si quieres mostrar la fuerza de un edificio, ¿qué volumen conviene: muy lleno o con muchos vacíos?", "Muy lleno", "El material abundante da sensación de fuerza."),
        ex("En una maqueta toda verde quieres que la puerta destaque. ¿Qué color usas para la puerta: rojo o verde claro?", "Rojo", "El rojo es complementario del verde y contrasta."),
    ],
    [
        ex("Propósito: soledad. ¿Qué maqueta sirve más: un solo edificio pequeño en una hoja grande vacía o muchos edificios pegados?", "Un solo edificio pequeño en una hoja grande vacía", "El espacio vacío acentúa el aislamiento."),
        ex("Propósito: energía. ¿Qué combinación sirve: rojo, naranjo y amarillo con formas que se asoman en diagonal o azules apagados con formas quietas?", "Rojo, naranjo y amarillo con formas que se asoman en diagonal", "Los cálidos y las diagonales transmiten energía."),
        arith("Una maqueta tiene 6 edificios y cada uno lleva 4 ventanas amarillas. ¿Cuántas ventanas amarillas hay?", "6*4", "Se multiplican edificios por ventanas de cada uno."),
    ],
    [
        ex("Quieres una maqueta de una biblioteca tranquila. Un compañero te propone pintarla de rojo fuerte. ¿Es coherente con tu propósito?", "No", "El rojo fuerte da energía y tensión, no tranquilidad."),
        ex("Tu torre tiene gama fría y dos ventanas naranjas. Quieres que el contraste lleve la vista a un solo lugar. ¿Qué cambias: dejar una ventana naranja y pintar la otra azul o pintar más ventanas naranjas?", "Dejar una ventana naranja y pintar la otra azul", "Un solo contraste fuerte dirige la mirada."),
    ],
    [
        ex("Un diseño tiene gama cálida, muchos vacíos y formas livianas. Su autor dice que quiere mostrar «peso y seriedad». ¿Qué recurso contradice su propósito?", "Los muchos vacíos y las formas livianas", "Los vacíos y lo liviano dan ligereza, no peso."),
        ex("Dos diseños de un puente de cartulina. El de Lina es fuerte, de colores cálidos y oscuros y sin ventanas. El de Matías es azul claro con muchas aberturas. Se busca mostrar «ligereza y calma». ¿Cuál cumple mejor?", "El de Matías", "El azul claro y las aberturas dan calma y ligereza."),
    ],
    ex("Tienes que diseñar una maqueta de una plaza que dé sensación de alegría. Dispones de cartulina amarilla, naranja, celeste y azul oscuro. ¿Qué eliges para los edificios: amarillo y naranja con aberturas o azul oscuro sin aberturas?", "Amarillo y naranja con aberturas", "Los cálidos y los vacíos abiertos transmiten alegría."),
    [
        ex("¿Para qué se escribe el propósito antes de elegir color y volumen?", "Para decidir con una idea clara", "Todas las decisiones deben apoyar el propósito."),
        ex("Verdadero o falso: una buena obra usa todos los recursos posibles.", "Falso", "Solo conviene usar los que sirven a la idea."),
        ex("¿Dónde conviene poner el contraste más fuerte: en lo más importante o en toda la obra?", "En lo más importante", "Así la mirada va a lo central."),
    ],
    task(
        "Elige UN propósito. A) Mostrar calma en un puerto al amanecer. B) Mostrar energía en una feria llena de gente. C) Mostrar soledad en un edificio solo en un campo. Escribe el propósito, elige una gama, ubica un contraste fuerte, decide qué partes serán llenas y cuáles vacías, haz un boceto y construye una maqueta pequeña de cartulina. Anota un cambio que hiciste y por qué.",
        "Elegí la A. Propósito: calma en un puerto. Gama fría de azules y celestes. Contraste: una puerta naranja. Volumen: tres edificios con ventanas altas y espacios entre ellos. Cambié una caja cerrada por una con ventanas, porque se sentía pesada.",
        ["escribe el propósito", "elige gama, contraste y volumen coherentes", "hace boceto y maqueta", "anota un cambio con razón"],
        ["boceto", "maqueta", "propósito y cambio escritos"],
        ["recursos que contradicen el propósito", "demasiados contrastes"],
        "Pregunta qué recurso apoya mejor el propósito y qué recurso cambiaría si pudiera rehacer la maqueta.",
    ),
    "Mira una casa de tu calle y di qué propósito expresivo tiene su color y su forma.",
    "Rehaz la maqueta con el propósito contrario y compara qué recursos tuviste que cambiar.",
)

"""Cuaderno del estudiante de 5.º básico Artes Visuales: AR05 OA 02 (color complementario, formas abiertas y cerradas, luz y sombra)."""
from __future__ import annotations

from student_content_ar5_a import lesson, m, task, w
from student_lessons import arith, ex

OA2 = "AR05 OA 02"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Lápices de colores o témperas de rojo, verde, azul, naranjo, amarillo y violeta, y una hoja. Si no tienes todos, las parejas están escritas en esta clase.",
    "Aprenderé qué son los colores complementarios y para qué sirven: hacer que algo se destaque. Sirve para decidir de qué color pinto el fondo de un objeto que quiero que se vea mucho.",
    ["Sé que los colores primarios son rojo, amarillo y azul.", "Sé que mezclando primarios se forman el naranjo, el verde y el violeta."],
    [
        "Los colores se pueden ordenar en un círculo llamado rueda de color. Los colores complementarios son los que están uno frente al otro en esa rueda, es decir, opuestos. Las tres parejas básicas son: rojo y verde, azul y naranjo, amarillo y violeta. Cada pareja tiene un color primario y un color que se forma con los otros dos primarios.",
        "Cuando pongo dos complementarios juntos, cada uno se ve más fuerte y más vivo. Por eso un círculo naranjo sobre un fondo azul se nota mucho. Esto se llama contraste de color. En cambio, los colores vecinos en la rueda, como el azul y el verde, se parecen y dan una sensación más calmada. Un artista elige entre contraste y calma según lo que quiere comunicar.",
        "Para formular una intención con complementarios, escribo qué quiero destacar y qué pareja usaré. Por ejemplo: «Quiero que el sol naranjo sea lo primero que se vea, así que pintaré el cielo azul». También puedo usar poco de un color y mucho de su complementario, así lo pequeño se destaca. Anoto en el croquis qué color va en cada zona antes de pintar.",
    ],
    [("rueda de color", "círculo que ordena los colores"), ("color complementario", "color que está frente a otro en la rueda de color"), ("contraste de color", "diferencia fuerte entre dos colores que hace que se destaquen"), ("colores vecinos", "colores que están uno al lado del otro en la rueda y se parecen"), ("destacar", "hacer que algo se note más")],
    [
        w("Encontrar el complementario", "Quieres pintar un velero amarillo y que se vea mucho en el mar. ¿Qué color usas para el mar?", ["Busco el color frente al amarillo en la rueda.", "Frente al amarillo está el violeta.", "El mar violeta hará que el velero amarillo se destaque."], "Violeta"),
        w("Poco y mucho", "Pintas un campo verde y quieres que una amapola pequeña se note. ¿Qué color usas para la amapola?", ["El complementario del verde es el rojo.", "Uso el rojo en un tamaño pequeño.", "Poco rojo sobre mucho verde se destaca."], "Una amapola roja y pequeña sobre el verde"),
    ],
    [
        m("Pensar que los complementarios son colores que se parecen.", "Se confunde con los vecinos de la rueda.", "Recuerda: los complementarios están uno frente al otro, y los vecinos están al lado."),
        m("Usar la pareja de complementarios en partes iguales de la hoja.", "Se pierde el protagonista y la obra se ve cansadora.", "Usa mucho de un color y poco de su complementario."),
    ],
    [
        ex("¿Cuál es el color complementario del rojo?", "Verde", "En la rueda de color, el verde está frente al rojo."),
        ex("¿Cuál es el color complementario del azul?", "Naranjo", "El naranjo está frente al azul en la rueda."),
        ex("Los colores complementarios, ¿están uno frente al otro o uno al lado del otro en la rueda?", "Uno frente al otro", "Ser complementarios significa ser opuestos en la rueda."),
    ],
    [
        ex("¿Qué pareja es de colores complementarios? A: amarillo y violeta. B: rojo y naranjo.", "A", "El amarillo está frente al violeta; el rojo y el naranjo son vecinos."),
        ex("Una manzana roja sobre un fondo verde, ¿qué efecto principal produce esa pareja: un contraste fuerte o una calma suave?", "Un contraste fuerte", "Los complementarios juntos se resaltan uno al otro."),
        ex("¿Cuál es el complementario del violeta?", "Amarillo", "El amarillo está frente al violeta en la rueda."),
    ],
    [
        ex("Quieres que un círculo naranjo se destaque sobre el fondo. ¿Qué color usas para el fondo?", "Azul", "El azul es el complementario del naranjo."),
        ex("Quieres una imagen calmada y suave. ¿Qué pareja ayuda más: azul y verde, o rojo y verde?", "Azul y verde", "Son vecinos y se parecen; el rojo y el verde son complementarios y contrastan fuerte."),
        ex("Quieres que una flor pequeña amarilla se note en un campo. ¿Qué color usas en el fondo cerca de ella: violeta o amarillo claro?", "Violeta", "El violeta es complementario del amarillo y hace que la flor se destaque."),
    ],
    [
        ex("Dos pruebas de un faro naranjo. En la 1, el mar es azul. En la 2, el mar es naranjo claro. ¿En cuál se destaca más el faro?", "En la 1", "El faro naranjo contrasta con el azul, que es su complementario."),
        ex("Tomás dice: «Los complementarios son colores que se parecen». ¿Es correcto?", "No", "Los complementarios son opuestos en la rueda, no parecidos."),
    ],
    [
        ex("Tu afiche de la feria tiene un pimentón rojo que quieres que se destaque. Ya usaste azul y naranjo en otras partes. ¿Qué color elegirías para el fondo del pimentón?", "Verde", "El verde es el complementario del rojo."),
        ex("Usarás las parejas rojo-verde y azul-naranjo en una obra. ¿Qué pareja de complementarios falta?", "Amarillo y violeta", "Las tres parejas son rojo-verde, azul-naranjo y amarillo-violeta."),
    ],
    ex("El colegio te pide un cartel de reciclaje con un tarro azul que debe destacarse. ¿Qué color usas de fondo: naranjo o azul claro?", "Naranjo", "El naranjo es complementario del azul y hace destacar el tarro."),
    [
        ex("Verdadero o falso: el amarillo y el violeta son complementarios.", "Verdadero", "Están uno frente al otro en la rueda de color."),
        ex("¿Qué efecto tiene poner dos complementarios juntos?", "Cada uno se ve más fuerte", "Se produce contraste de color."),
        ex("Verdadero o falso: los colores vecinos de la rueda dan más contraste que los complementarios.", "Falso", "Los complementarios son los que dan más contraste."),
    ],
    task(
        "Elige UN objeto para destacar: A) una pelota roja; B) un sol naranjo; C) una flor amarilla. Escribe cuál es su color complementario. Haz un croquis con el objeto pequeño y el fondo grande. Escribe tu intención en una frase: «Quiero destacar… usando… porque…».",
        "Elegí la B, el sol naranjo. Su complementario es el azul. Dibujé un sol naranjo pequeño en un cielo azul grande. Intención: quiero destacar el sol usando el cielo azul porque el naranjo y el azul son complementarios y se resaltan.",
        ["identifica el complementario correcto", "dibuja poco del color destacado y mucho de su complementario", "escribe una intención con razón", "pinta una zona de cada color"],
        ["croquis", "pareja de colores escrita", "una frase de intención"],
        ["usar colores vecinos", "usar partes iguales de ambos colores"],
        "Muestra el objeto que más se destaca y pregunta qué hace que se note: el color, el tamaño o ambos.",
    ),
    "Mira tres objetos de tu casa y di cuál es el color complementario de cada uno, aunque no lo tengas a mano.",
    "Haz la misma imagen con una pareja de colores vecinos y compara cuál destaca más al objeto.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Témperas o lápices de colores de rojo, verde, azul, naranjo, amarillo y violeta, blanco y una hoja para pruebas. Puedes hacer las pruebas con lápices, superponiendo colores.",
    "Aprenderé qué pasa cuando uso complementarios de formas distintas: juntos sin mezclar, mezclados o en distinta cantidad. Sirve para escoger si quiero un color vivo, uno apagado o un acento pequeño.",
    ["Sé cuáles son las tres parejas de colores complementarios.", "Sé que dos complementarios juntos hacen contraste."],
    [
        "Una variable visual es una decisión que puedo cambiar para ver su efecto. Con los complementarios hay tres variables. La primera es ponerlos juntos y sin mezclar: los dos se ven vivos y parecen vibrar en el borde. La segunda es mezclarlos: si mezclo un color con su complementario, resulta un color apagado, parecido a un café o a un gris. La tercera es la cantidad: poco de uno y mucho del otro.",
        "Para apagar un color demasiado fuerte, puedo agregarle un poco de su complementario. Por ejemplo, un verde brillante se vuelve más natural con un toque de rojo. También sirve para oscurecer sin usar negro. Si quiero oscurecer un verde para la sombra de un árbol, le agrego un poco de rojo y queda oscuro, pero con color. Con blanco, un color se hace más claro.",
        "Un acento es un toque pequeño de color que llama la atención dentro de una zona grande de otro color. Por ejemplo, una mancha pequeña de naranjo en un cuadro casi todo azul. Para decidir cuál variable usar, hago pruebas pequeñas y las comparo con mi intención: ¿quiero vibración, calma, tierra o un acento? La prueba que mejor muestra mi intención es la que elijo.",
    ],
    [("vibrar", "parecer que un borde de color se mueve por el contraste fuerte"), ("color apagado", "color menos brillante, parecido al gris o al café"), ("acento", "toque pequeño de color que llama la atención"), ("mezclar", "unir dos colores para obtener otro"), ("variable visual", "decisión que puedo cambiar para ver su efecto")],
    [
        w("Apagar un color", "Tu naranjo es demasiado fuerte para el desierto que quieres pintar. ¿Qué haces?", ["Busco el complementario del naranjo: el azul.", "Agrego un poquito de azul al naranjo.", "El naranjo queda más apagado, como tierra."], "Agrego un poco de azul"),
        w("Elegir con la intención", "Quieres que un borde entre un cerro rojo y un cielo verde vibre. ¿Pones los colores juntos o los mezclas?", ["Vibrar necesita contraste fuerte en el borde.", "Si los mezclo se apagan.", "Los pongo juntos, sin mezclar."], "Juntos, sin mezclar"),
    ],
    [
        m("Mezclar dos complementarios y esperar un color más vivo.", "La mezcla de complementarios apaga el color.", "Usa los complementarios juntos para vivos y mezclados para apagar."),
        m("Oscurecer todos los colores con negro.", "El negro quita el color y deja el dibujo sin vida.", "Prueba con un poco de complementario para oscurecer con color."),
    ],
    [
        ex("Si mezclas rojo con verde, ¿el color que resulta es más brillante o más apagado?", "Más apagado", "Mezclar complementarios produce un color parecido al gris o al café."),
        ex("Para que dos complementarios vibren, ¿los pones juntos sin mezclar o los mezclas?", "Juntos sin mezclar", "El contraste se nota en el borde si están sin mezclar."),
        ex("Si agregas blanco a un color, ¿se vuelve más claro o más oscuro?", "Más claro", "El blanco aclara los colores."),
    ],
    [
        ex("Para apagar un naranjo muy fuerte, ¿agregas un poco de azul o de amarillo?", "Azul", "El azul es el complementario del naranjo y lo apaga."),
        ex("Un cuadro es casi todo azul, con una mancha pequeña de naranjo. ¿Cuál es el acento?", "El naranjo", "El acento es el toque pequeño que llama la atención."),
        ex("Si agregas un poquito de rojo a un verde brillante, ¿el verde queda más vivo o más apagado?", "Más apagado", "El rojo es el complementario del verde y lo apaga."),
    ],
    [
        ex("Pintas la sombra de un limón amarillo. Siguiendo la idea de complementarios, ¿qué color le agregas: violeta suave o negro?", "Violeta suave", "El violeta es el complementario del amarillo y da una sombra con color."),
        ex("Quieres un paisaje de tonos apagados, como una foto antigua. ¿Mezclas complementarios o los pones puros uno al lado del otro?", "Los mezclas", "Mezclarlos apaga los colores."),
        ex("Quieres que el borde entre una zona roja y otra verde vibre mucho. ¿Pintas una franja blanca entre ellas o las dejas pegadas?", "Las dejas pegadas", "Una franja blanca separaría los colores y reduciría la vibración."),
    ],
    [
        ex("Intención: el rojo debe ser un acento pequeño en un paisaje verde. Prueba A: manzana roja que ocupa casi toda la hoja. Prueba B: manzana roja pequeña en un campo verde. ¿Cuál cumple la intención?", "La prueba B", "El acento debe ser un toque pequeño."),
        ex("Ana mezcló azul y naranjo y le quedó un café grisáceo, pero quería un naranjo vivo. ¿Qué debió hacer: usar el naranjo puro o seguir mezclando?", "Usar el naranjo puro", "Al mezclar complementarios, el color se apaga."),
    ],
    [
        ex("Quieres oscurecer un verde para la sombra de un árbol, sin que quede negro. ¿Agregas un poco de rojo o un poco de blanco?", "Un poco de rojo", "El rojo oscurece y apaga; el blanco aclara."),
        ex("Dos afiches con letras naranjas: uno sobre fondo azul y otro sobre fondo amarillo claro. ¿Cuál se lee mejor?", "El de fondo azul", "El naranjo y el azul contrastan mucho; el naranjo y el amarillo son parecidos."),
    ],
    ex("Pintas cerros de naranjo en el desierto y quieres que el cielo los destaque. ¿Qué cielo eliges: azul o naranjo claro?", "Azul", "El azul es complementario del naranjo y hace destacar los cerros."),
    [
        ex("Verdadero o falso: un acento es un toque pequeño de color que llama la atención.", "Verdadero", "Así se llama a ese toque dentro de una zona grande."),
        ex("¿Qué efecto tiene mezclar dos complementarios?", "Se obtiene un color apagado", "La mezcla apaga el color."),
        ex("Verdadero o falso: para oscurecer un color con color puedo agregarle un poco de su complementario.", "Verdadero", "Así la sombra no queda negra y sin vida."),
    ],
    task(
        "Elige UN paisaje: A) cerros anaranjados de un desierto; B) un campo verde con una casa roja; C) un lago azul con un bote naranjo. Haz tres pruebas pequeñas con una sola pareja de complementarios: 1) juntos sin mezclar, 2) mezclados para apagar, 3) con poco de uno y mucho del otro. Elige la prueba que mejor muestra tu intención y explica por qué.",
        "Elegí el paisaje C. Prueba 1: bote naranjo junto al lago azul, vibra. Prueba 2: mezclé azul y naranjo en el lago, queda gris. Prueba 3: bote muy pequeño en un lago grande. Quiero mostrar un bote solo y destacado: elegí la prueba 3 porque el naranjo pequeño se destaca en el azul grande.",
        ["hace tres pruebas con la misma pareja", "describe el efecto de cada prueba", "elige según la intención", "usa bien cada variable"],
        ["tres pruebas", "obra final", "una frase de elección"],
        ["elegir sin comparar", "mezclar y esperar un color vivo"],
        "Destaca la prueba mejor comparada y pregunta qué cambiaría si la intención fuera crear calma.",
    ),
    "Mira un objeto de color vivo y di en voz alta con qué otro color lo apagarías.",
    "Haz una tabla pequeña con las tres parejas y anota qué color resulta al mezclar cada una.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Lápiz de mina, plumones o lápices de colores y una hoja. Las formas de ejemplo están descritas en la clase.",
    "Aprenderé a diferenciar formas abiertas y cerradas y a elegir procedimientos de dibujo según la sensación que quiero lograr. Sirve para decidir cómo dibujo un contorno según mi intención.",
    ["Sé dibujar líneas rectas, curvas, onduladas y quebradas.", "Sé que una obra puede tener una intención propia."],
    [
        "Una forma cerrada es una forma cuyo contorno se junta y encierra un espacio, como un círculo, un cuadrado o una hoja con el borde completo. Una forma abierta es aquella cuyo contorno no se cierra, o tiene huecos, y por eso el espacio de adentro se mezcla con el de afuera, como un trazo en forma de C, una espiral o un camino que sigue más allá del borde de la hoja.",
        "Cada tipo de forma da sensaciones distintas. Las formas cerradas se ven definidas, firmes y quietas; sirven para mostrar objetos sólidos, como un cerro o una casa. Las formas abiertas se ven ligeras y en movimiento; sirven para mostrar el viento, el agua o un camino que continúa. En una misma obra puedo combinar las dos: formas cerradas para los objetos importantes y abiertas para el ambiente.",
        "El procedimiento también cambia el efecto. Para una forma cerrada, hago un contorno completo con plumón y relleno con un color plano. Para una forma abierta, dejo huecos en el contorno o uso líneas sueltas, y el color puede salirse del borde. Los materiales sencillos, como lápiz, plumón o lápices de colores, sirven para ambos. Elijo el procedimiento según lo que quiero comunicar.",
    ],
    [("forma cerrada", "forma cuyo contorno se junta y encierra un espacio"), ("forma abierta", "forma cuyo contorno no se cierra o tiene huecos"), ("contorno", "línea que rodea una forma"), ("color plano", "área de un solo color, sin degradé"), ("trazo", "línea hecha con un movimiento de la mano")],
    [
        w("Clasificar", "Dibujas un círculo y dejas un pedazo del contorno sin trazar. ¿La forma es abierta o cerrada?", ["Miro si el contorno se junta.", "El contorno tiene un hueco.", "Entonces no encierra el espacio por completo."], "Abierta"),
        w("Elegir según la intención", "Quieres mostrar el viento moviendo el pasto. ¿Usas formas abiertas o cerradas?", ["El viento es movimiento y continúa.", "Las formas abiertas se ven ligeras y en movimiento.", "Dibujo líneas sueltas, curvas y sin cerrar."], "Formas abiertas"),
    ],
    [
        m("Pensar que una forma es cerrada solo por tener relleno.", "Lo que cuenta es el contorno, no el relleno.", "Mira si el contorno se junta y encierra un espacio."),
        m("Dibujar todos los objetos con formas cerradas y esperar que se vea movimiento.", "Las formas cerradas se ven quietas.", "Agrega formas abiertas donde quieras movimiento."),
    ],
    [
        ex("Una forma cerrada, ¿tiene el contorno completo o con huecos?", "Completo", "Cerrada significa que el contorno se junta y encierra un espacio."),
        ex("Un círculo dibujado con un contorno completo, ¿es forma abierta o cerrada?", "Cerrada", "El círculo completo encierra un espacio."),
        ex("Un trazo en forma de C, ¿es abierto o cerrado?", "Abierto", "Sus extremos no se juntan y no encierra un espacio."),
    ],
    [
        ex("Dibujas un círculo y dejas un hueco en el contorno. ¿Cómo queda la forma?", "Abierta", "El contorno no se junta por completo."),
        ex("Muchas líneas curvas que salen por el borde de la hoja, ¿qué sensación dan: movimiento o quietud?", "Movimiento", "Las formas abiertas se ven ligeras y en movimiento."),
        ex("¿Cuál es una forma abierta: un triángulo con los tres lados unidos o un zigzag hecho con una sola línea?", "El zigzag", "El zigzag no encierra ningún espacio."),
    ],
    [
        ex("Quieres mostrar un cerro firme y sólido. ¿Usas un contorno cerrado o abierto?", "Cerrado", "La forma cerrada se ve firme y definida."),
        ex("Quieres mostrar un camino que sigue lejos, más allá de la hoja. ¿Dibujas una línea abierta que sale por el borde o un círculo cerrado?", "Una línea abierta que sale por el borde", "La forma abierta sugiere que algo continúa."),
        ex("Dibujas una casa con muros firmes y humo que sube de la chimenea. ¿Qué parte puedes hacer con forma abierta: los muros o el humo?", "El humo", "El humo se mueve y se disuelve; los muros son firmes y cerrados."),
    ],
    [
        ex("Quieres una nube que se disuelve con el viento. Prueba A: contorno completo y relleno plano. Prueba B: contorno con interrupciones y rayas suaves. ¿Cuál cumple mejor la intención?", "La prueba B", "Los huecos y las rayas suaves dan sensación de algo que se deshace."),
        ex("Pablo dibuja un círculo cerrado y le agrega líneas largas que salen como rayos. ¿El círculo central sigue siendo una forma cerrada?", "Sí", "Su contorno sigue completo; solo se agregaron líneas."),
    ],
    [
        ex("En un dibujo hay un círculo cerrado, 2 espirales abiertas, 3 triángulos cerrados y 1 línea ondulada abierta. ¿Cuántas formas cerradas hay?", "4", "Se cuentan el círculo y los 3 triángulos.", calc="1+3"),
        ex("Diseñas el logo de un parque: quieres un contorno firme, pero que invite a entrar. ¿Cómo lo haces: un contorno firme con una abertura en un lado, que sería una forma abierta, o un contorno completo sin ninguna abertura?", "Un contorno firme con una abertura en un lado", "La abertura invita a entrar y el resto del contorno da firmeza."),
    ],
    ex("Te piden dibujar un sendero para un cartel del colegio que invite a seguir caminando. ¿Qué haces con la línea del sendero: la cierras en un círculo o la dejas abierta hasta el borde del cartel?", "La dejas abierta hasta el borde del cartel", "Una línea abierta que sale del cartel sugiere que el camino sigue."),
    [
        ex("Verdadero o falso: una forma rellena de color siempre es cerrada.", "Falso", "Lo que importa es el contorno: si tiene huecos, es abierta."),
        ex("¿Qué sensación dan las formas cerradas?", "Firmeza y quietud", "Se ven definidas y estables."),
        ex("Verdadero o falso: se pueden combinar formas abiertas y cerradas en una misma obra.", "Verdadero", "Combinarlas permite mostrar objetos firmes y ambientes con movimiento."),
    ],
    task(
        "Elige UNA escena: A) un faro firme junto a un mar con viento; B) una casa de campo con humo y pasto movido por el viento; C) un volcán con humo que sube. Dibuja con plumón o lápiz. Usa formas cerradas para lo firme y formas abiertas para lo que se mueve. Escribe cuáles son cerradas y cuáles abiertas, y por qué.",
        "Elegí la A. El faro es una forma cerrada con contorno completo, rellenado con color plano, porque debe verse firme. El mar tiene líneas curvas abiertas, sin cerrar, porque se mueve con el viento. Dibujé también una gaviota con una línea abierta.",
        ["dibuja formas cerradas con contorno completo", "dibuja formas abiertas con huecos o líneas sueltas", "explica la elección por la sensación", "combina ambos tipos"],
        ["dibujo", "lista de formas", "una frase de razón"],
        ["cerrar todas las formas", "confundir relleno con contorno cerrado"],
        "Destaca la combinación donde se nota la diferencia entre lo firme y lo que se mueve.",
    ),
    "Mira tu mano y di si su contorno es abierto o cerrado cuando los dedos están juntos y cuando están separados.",
    "Dibuja el mismo objeto con contorno cerrado y con contorno abierto y anota qué cambia en la sensación.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Hoja, lápiz de mina (con el que puedes hacer claros y oscuros), una pelota, una taza u otro objeto, y una lámpara o la luz de una ventana. No uses velas ni fuego.",
    "Aprenderé a mostrar luz y sombra: de dónde viene la luz, dónde caen la sombra propia y la sombra proyectada, y cómo hacer un degradé. Sirve para que los objetos se vean con volumen.",
    ["Sé que algo oscuro y algo claro se ven distintos.", "Sé dibujar una esfera o una caja simple."],
    [
        "Para dibujar luz y sombra, primero decido de dónde viene la luz. Esa es la fuente de luz. Puede ser el sol, una lámpara o una ventana. La parte del objeto que mira hacia la luz se ve clara. La parte que mira hacia el lado contrario se ve oscura. Esa zona oscura sobre el mismo objeto se llama sombra propia.",
        "La sombra proyectada es la que el objeto deja sobre la superficie donde está, como la mesa o el suelo. Siempre cae del lado contrario a la fuente de luz. Si la luz viene de la derecha, la sombra proyectada cae hacia la izquierda. Si la luz es baja, como la del sol al atardecer, las sombras son largas. Si la luz viene de arriba, como al mediodía, las sombras son cortas.",
        "Para que un objeto redondo se vea con volumen, hago un degradé: paso de lo más claro a lo más oscuro de a poco, sin saltos bruscos. Con un lápiz de mina presiono poco para el claro y más para el oscuro. Un valor es qué tan claro u oscuro es un tono. Si hay mucho contraste entre claro y oscuro, la imagen se ve dramática; si hay poco, se ve suave y tranquila.",
    ],
    [("fuente de luz", "lo que ilumina, como el sol o una lámpara"), ("sombra propia", "zona oscura del objeto, en el lado contrario a la luz"), ("sombra proyectada", "sombra que el objeto deja sobre la superficie donde está"), ("degradé", "paso de claro a oscuro de a poco"), ("valor", "qué tan claro u oscuro es un tono")],
    [
        w("Ubicar las sombras", "Una pelota está sobre una mesa. La luz de una lámpara viene desde la izquierda. ¿Dónde está la parte más clara de la pelota, la sombra propia y la sombra proyectada?", ["La luz viene de la izquierda, así que el lado izquierdo es más claro.", "La sombra propia está en el lado derecho de la pelota.", "La sombra proyectada cae sobre la mesa, hacia la derecha."], "Clara a la izquierda; sombra propia a la derecha; sombra proyectada a la derecha, sobre la mesa"),
        w("Luz baja y alta", "Quieres mostrar una tarde en que el sol está muy bajo. ¿Cómo dibujas las sombras?", ["Con el sol bajo, las sombras se estiran.", "Las dibujo largas.", "Y las hago del lado contrario al sol."], "Largas y del lado contrario al sol"),
    ],
    [
        m("Dibujar la sombra proyectada del mismo lado de donde viene la luz.", "La sombra cae siempre hacia el lado contrario a la luz.", "Primero marca de dónde viene la luz y luego dibuja la sombra al lado opuesto."),
        m("Pintar un salto brusco de claro a oscuro en una pelota.", "La pelota se ve plana y no redonda.", "Haz un degradé de a poco."),
    ],
    [
        ex("La sombra propia, ¿está en el objeto en el lado contrario a la luz o en el lado que mira a la luz?", "En el lado contrario a la luz", "Ese lado no recibe luz."),
        ex("La sombra proyectada, ¿cae sobre la mesa donde está el objeto o dentro del objeto?", "Sobre la mesa", "La sombra proyectada cae sobre la superficie donde está el objeto."),
        ex("La luz viene de la derecha. ¿Hacia qué lado cae la sombra proyectada: izquierda o derecha?", "Izquierda", "La sombra cae al lado contrario de la luz."),
    ],
    [
        ex("Para dibujar una esfera con volumen, ¿haces un salto brusco de claro a oscuro o un degradé?", "Un degradé", "El degradé muestra la curva de la esfera."),
        ex("La luz viene de arriba a la izquierda. ¿En qué parte de una pelota va lo más oscuro?", "Abajo a la derecha", "Es el lado más lejano a la luz."),
        ex("El sol está bajo, al atardecer. ¿Las sombras se ven largas o cortas?", "Largas", "Con el sol bajo, las sombras se estiran."),
    ],
    [
        ex("Dibujas una pelota con la luz desde la izquierda y la sombra proyectada cae a la derecha. ¿Dónde pones la parte más clara de la pelota?", "A la izquierda", "El lado que mira a la luz se ve más claro."),
        ex("Quieres mostrar el mediodía, con el sol alto. ¿Qué sombra dibujas: corta y bajo el objeto o larga y estirada?", "Corta y bajo el objeto", "Con el sol alto, la sombra es corta."),
        ex("Ordena los pasos para dibujar un objeto con luz y sombra: A) hacer el degradé del objeto, B) decidir de dónde viene la luz, C) revisar que la sombra proyectada caiga al lado contrario de la luz. Escribe las letras en orden.", "B, A, C", "Primero se decide la luz, luego se dibuja el objeto y al final se revisa la sombra."),
    ],
    [
        ex("Un dibujo muestra un árbol con su lado derecho muy claro y su sombra en el suelo cayendo también a la derecha. ¿Hay un error?", "Sí", "La sombra debe caer al lado contrario de la luz, es decir, hacia la izquierda."),
        ex("Quieres un ambiente misterioso, como de noche con una linterna. ¿Usas mucho contraste de claro y oscuro o valores muy parecidos?", "Mucho contraste de claro y oscuro", "El contraste fuerte da dramatismo."),
    ],
    [
        ex("Tu intención es mostrar una tarde larga y tranquila. Prueba A: sombras cortas y muy oscuras. Prueba B: sombras largas y suaves. ¿Cuál se acerca a la intención?", "La prueba B", "Las sombras largas y suaves dan sensación de tarde tranquila."),
        ex("Una linterna a un lado ilumina una taza sobre una mesa. Si bajas la linterna, acercándola a la mesa, ¿la sombra de la taza se hace más larga o más corta?", "Más larga", "Con la luz más baja, las sombras se estiran."),
    ],
    ex("La luz de la ventana de tu pieza entra por tu izquierda. Pones una fruta sobre la mesa. ¿Hacia dónde cae su sombra proyectada: hacia la derecha o hacia la izquierda?", "Hacia la derecha", "La sombra cae del lado contrario a la ventana."),
    [
        ex("Verdadero o falso: la sombra proyectada cae del mismo lado donde está la fuente de luz.", "Falso", "Cae del lado contrario."),
        ex("¿Qué es un degradé?", "Un paso de claro a oscuro de a poco", "Sirve para mostrar volumen."),
        ex("Verdadero o falso: con mucho contraste de claro y oscuro la imagen se ve más dramática.", "Verdadero", "El contraste fuerte aumenta la tensión."),
    ],
    task(
        "Elige UN objeto de tu casa sin filo y sin peso peligroso (una pelota, una taza o una fruta) o esta escena: «una fruta redonda sobre una mesa con una lámpara a la izquierda». Haz un croquis y decide de dónde viene la luz. Dibuja la sombra propia, la sombra proyectada y un degradé en el objeto. Escribe en una frase cómo muestra tu dibujo la luz.",
        "Elegí la escena. La luz viene de la izquierda. Hice un degradé: claro a la izquierda y oscuro a la derecha. La sombra propia queda a la derecha y la sombra proyectada cae hacia la derecha, sobre la mesa. Mi dibujo muestra la luz porque el lado izquierdo es más claro.",
        ["indica de dónde viene la luz", "dibuja sombra propia y proyectada en el lugar correcto", "hace un degradé", "explica cómo se ve la luz"],
        ["croquis con la luz marcada", "dibujo con degradé", "una frase"],
        ["poner la sombra del mismo lado de la luz", "saltos bruscos de claro a oscuro"],
        "Reconoce el dibujo donde la luz es coherente y pregunta qué pasa con las sombras si cambias la luz de lado.",
    ),
    "Pon un objeto sobre la mesa con la luz de una ventana y di en voz alta hacia dónde cae su sombra.",
    "Dibuja el mismo objeto con tres posiciones distintas de la luz y anota cómo cambian las sombras.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Hoja, lápices de colores o témperas y lápiz de mina. Las descripciones de obras están escritas en esta clase.",
    "Aprenderé a combinar color complementario, formas abiertas y cerradas, y luz y sombra en una misma obra, y a explicar mis decisiones. Sirve para crear trabajos con una idea clara y justificada.",
    ["Sé usar complementarios para destacar algo.", "Sé distinguir formas abiertas y cerradas y ubicar la luz y las sombras."],
    [
        "En una obra, los elementos del lenguaje visual trabajan juntos. Hasta ahora conoces el color complementario, las formas abiertas y cerradas, y la luz y la sombra. También usas elementos de otros niveles: línea, textura, plano y valor. La clave es decidir qué papel tiene cada uno para lograr mi intención, sin llenar la obra de efectos.",
        "Una forma de planificar es hacer una lista de tres decisiones. Primero, el color: cuál es el protagonista y cuál su complementario. Segundo, las formas: cuáles serán cerradas, para lo firme, y cuáles abiertas, para lo que se mueve. Tercero, la luz: de dónde viene y dónde caen las sombras. Por ejemplo, para un faro: faro naranjo con contorno cerrado, mar azul con líneas abiertas, y luz desde la izquierda con sombra a la derecha.",
        "Para fundamentar, escribo frases con «Usé… para… porque…». Por ejemplo: «Usé naranjo sobre azul para que el faro se destaque, porque son complementarios». Una buena fundamentación nombra el elemento visual y su razón. No basta decir «me gustó». Al terminar, reviso si cada decisión ayuda a mi intención; si no, la cambio.",
    ],
    [("lenguaje visual", "elementos como color, línea, forma, textura, luz y sombra que usamos para comunicar"), ("protagonista", "lo que quiero que más se note en la obra"), ("fundamentar", "explicar con razones por qué tomé una decisión"), ("composición", "cómo ordeno los elementos en la hoja"), ("decisión", "elección que hago al crear una obra")],
    [
        w("Planificar con tres decisiones", "Quieres pintar un velero al amanecer. Planifica el color, las formas y la luz.", ["Color: velero amarillo sobre mar violeta, que son complementarios.", "Formas: velero con contorno cerrado y olas con líneas abiertas.", "Luz: viene del lado izquierdo, y la sombra del velero cae sobre el mar hacia la derecha."], "Velero amarillo sobre mar violeta; velero cerrado y olas abiertas; luz desde la izquierda con sombra a la derecha"),
        w("Fundamentar", "Fundamenta la decisión de pintar un velero amarillo sobre un mar violeta.", ["Nombro el elemento: color complementario.", "Digo el propósito: que el velero se destaque.", "Armo la frase."], "Usé amarillo sobre violeta para que el velero se destaque, porque son complementarios"),
    ],
    [
        m("Usar todos los efectos en una misma obra para que se vea más completa.", "Una obra con demasiados efectos pierde claridad.", "Usa cada elemento solo si ayuda a tu intención."),
        m("Justificar con «porque me gustó».", "No explica el elemento visual ni su propósito.", "Nombra el elemento y para qué lo usaste."),
    ],
    [
        ex("Descripción de la obra «Faro»: un faro naranjo con contorno cerrado sobre un mar azul con líneas curvas abiertas; la luz viene de la izquierda y la sombra del faro cae a la derecha. ¿Qué pareja de complementarios usa la obra?", "Naranjo y azul", "El faro naranjo y el mar azul son complementarios."),
        ex("En la obra «Faro», ¿el contorno del faro es cerrado o abierto?", "Cerrado", "La descripción dice que el faro tiene contorno cerrado."),
        ex("En la obra «Faro», ¿hacia qué lado cae la sombra del faro?", "Hacia la derecha", "La descripción dice que la sombra cae a la derecha."),
    ],
    [
        ex("En «Faro», las líneas curvas del mar están abiertas. ¿Qué sensación dan?", "Movimiento", "Las formas abiertas se ven ligeras y en movimiento."),
        ex("En «Faro», ¿por qué el faro naranjo se destaca sobre el mar azul?", "Porque son complementarios", "El naranjo y el azul contrastan mucho."),
        ex("En «Faro», la luz viene de la izquierda. ¿Qué lado del faro es más claro?", "El izquierdo", "El lado que mira a la luz se ve más claro."),
    ],
    [
        ex("Quieres que la obra «Faro» se vea más tranquila. ¿Cambias las olas a líneas largas y horizontales o a zigzags?", "A líneas largas y horizontales", "Las líneas horizontales largas dan calma."),
        ex("El cielo de tu obra es violeta y quieres agregar una luna pequeña que se destaque. ¿De qué color la pintas?", "Amarilla", "El amarillo es complementario del violeta."),
        ex("Completa la frase de fundamentación con la mejor opción: «Usé naranjo sobre azul porque…». A: son complementarios y el faro se destaca. B: me gusta el naranjo.", "A", "La A da una razón visual; la B solo da un gusto."),
    ],
    [
        ex("Ana escribe: «Puse la sombra hacia la derecha porque la luz viene de la izquierda y así se ve profundidad». Beto escribe: «Puse sombra porque sí». ¿Quién fundamenta mejor?", "Ana", "Ana nombra la luz y explica el efecto."),
        ex("Una compañera usó solo formas cerradas y su obra se ve rígida. Quiere más movimiento sin perder los objetos. ¿Qué agrega: líneas abiertas curvas en el fondo o más contornos cerrados?", "Líneas abiertas curvas en el fondo", "Las formas abiertas aportan movimiento."),
    ],
    [
        ex("Una obra tiene un cerro violeta, un sol amarillo, nubes con contorno abierto, y luz desde la derecha con sombras hacia la izquierda. ¿Cuántos de estos tres contenidos usa: color complementario, formas abiertas o cerradas, y luz y sombra?", "Los tres", "Usa violeta y amarillo, nubes abiertas y sombras coherentes."),
        ex("Dos obras con la intención «mostrar calma». La A usa complementarios puros muy fuertes y sombras muy contrastadas. La B usa colores vecinos suaves, formas abiertas largas y sombras suaves. ¿Cuál cumple mejor?", "La B", "Los colores vecinos, las formas largas y las sombras suaves dan calma."),
    ],
    ex("Te piden un cartel del colegio para la semana del mar, con un pez que se vea mucho. Decides un pez naranjo sobre un fondo azul, con el contorno cerrado y una sombra a su derecha porque la luz viene de la izquierda. ¿Qué parte de tu decisión usa un color complementario?", "El pez naranjo sobre el fondo azul", "Naranjo y azul son complementarios."),
    [
        ex("Verdadero o falso: una obra mejora siempre al usar todos los efectos posibles.", "Falso", "Hay que usar solo los que ayudan a la intención."),
        ex("¿Qué dos partes tiene una buena fundamentación?", "El elemento visual y su razón", "Se dice qué se usó y por qué."),
        ex("Verdadero o falso: planificar color, formas y luz ayuda a tener una obra más clara.", "Verdadero", "La planificación une las decisiones con la intención."),
    ],
    task(
        "Elige UNA escena: A) un faro junto al mar; B) un volcán con humo en un valle; C) una casa de campo con un árbol. Planifica en una lista: color (protagonista y su complementario), formas (cuáles cerradas y cuáles abiertas) y luz (de dónde viene y dónde caen las sombras). Pinta la obra y escribe dos frases «Usé… para… porque…».",
        "Elegí la A. Color: faro naranjo y mar azul. Formas: faro cerrado y olas abiertas. Luz: desde la izquierda; la sombra del faro cae a la derecha. Usé naranjo sobre azul para que el faro se destaque, porque son complementarios. Usé olas abiertas para mostrar el movimiento del mar.",
        ["planifica color, formas y luz", "usa complementarios con intención", "ubica bien las sombras", "escribe dos frases de fundamentación"],
        ["lista de planificación", "obra terminada", "dos frases"],
        ["usar efectos que no ayudan", "justificar con gusto"],
        "Reconoce la decisión mejor justificada y pregunta qué elemento cambiaría la intención si lo quitaras.",
    ),
    "Mira una imagen que tengas a mano y di en voz alta dos elementos del lenguaje visual que reconoces.",
    "Rehaz la obra cambiando la fuente de luz y anota cuántas decisiones tuviste que ajustar.",
)

"""Cuaderno del estudiante de 1.º básico Artes Visuales, AR01 OA 02 (línea, color y textura)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA2 = "AR01 OA 02"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- Clase 1
register(
    OA2, 1,
    materials="Una hoja, un lápiz de mina y un lápiz de cera o de color. Los modelos de líneas están descritos en palabras.",
    use="Aprenderé a dibujar líneas gruesas, delgadas, rectas, onduladas e irregulares y a elegir cuál usar para cada cosa. Sirve para que mis dibujos muestren cosas distintas, como olas, pasto o rayos.",
    prior=["Sé tomar el lápiz y hacer trazos.", "Sé diferenciar entre recto y curvo."],
    explain=[
        "La línea es el camino que deja un lápiz al moverse sobre el papel. Hay muchas familias de líneas. Una línea gruesa se ve fuerte y una delgada se ve suave. Para hacer una gruesa apoyas más el lápiz o usas un crayón de lado; para una delgada, usas la punta con poca fuerza.",
        "Según su recorrido, una línea puede ser recta, como una regla; ondulada, que sube y baja suave como las olas; o irregular, que cambia de rumbo sin orden, como una grieta o un rayo. También tienen dirección: horizontal, acostada como el horizonte; vertical, parada como un poste; y diagonal, inclinada como una escalera apoyada.",
        "Cada línea cuenta algo diferente. Las horizontales suelen verse tranquilas, las diagonales dan sensación de movimiento y las irregulares parecen nerviosas o rotas. Cuando dibujas, eliges la línea que mejor muestra lo que quieres decir.",
    ],
    vocab=[("línea gruesa", "trazo ancho y fuerte"), ("línea delgada", "trazo fino y suave"), ("línea recta", "camino sin curvas, como el borde de una regla"), ("línea ondulada", "camino que sube y baja suavemente"), ("línea irregular", "camino que cambia de rumbo sin orden"), ("dirección", "hacia dónde va la línea: horizontal, vertical o diagonal")],
    worked=[
        {"title": "Elegir una línea para el mar", "problem": "Quieres dibujar olas tranquilas. ¿Qué línea eliges?", "steps": ["Pienso cómo se mueve una ola: sube y baja suave.", "La línea que sube y baja suave es la ondulada.", "La hago con poca fuerza para que se vea suave."], "answer": "Línea ondulada, de grosor delgado o medio"},
        {"title": "Reconocer una dirección", "problem": "Un poste de luz está parado derecho. ¿Qué dirección tiene la línea que lo dibuja?", "steps": ["El poste está parado, de arriba hacia abajo.", "Una línea parada se llama vertical."], "answer": "Vertical"},
    ],
    mistakes=[
        {"wrong": "Llamar «ondulada» a una línea con puntas muy puntiagudas.", "why": "Se confunde subir y bajar suave con cambiar de rumbo con ángulos.", "fix": "Si las curvas son suaves es ondulada; si hay quiebres bruscos es irregular."},
        {"wrong": "Hacer todas las líneas con la misma fuerza y grosor.", "why": "Se pierde la variedad que da vida al dibujo.", "fix": "Cambia la fuerza para hacer unas gruesas y otras delgadas."},
    ],
    tiers={
        "recovery": [
            ex("Una línea que sube y baja suavemente como las olas, ¿cómo se llama?", "Ondulada", "Ese recorrido suave es el de la línea ondulada."),
            ex("Una línea acostada como el horizonte, ¿es horizontal o vertical?", "Horizontal", "Horizontal significa acostada."),
            ex("Para hacer una línea delgada, ¿usas la punta con poca fuerza o el lápiz de lado con mucha fuerza?", "La punta con poca fuerza", "Poca presión y punta dan un trazo fino."),
        ],
        "understand": [
            ex("¿Cuál línea parece una grieta en la tierra? A: recta. B: ondulada. C: irregular.", "C", "Una grieta cambia de rumbo sin orden."),
            ex("Una línea inclinada como una escalera apoyada en la pared, ¿qué dirección tiene?", "Diagonal", "Inclinada es diagonal."),
            ex("¿Qué diferencia hay entre una línea gruesa y una delgada?", "La gruesa es ancha y fuerte; la delgada es fina y suave", "Se distinguen por el ancho del trazo."),
        ],
        "apply": [
            ex("Quieres dibujar pasto alto. ¿Qué líneas usas: A líneas verticales cortas y delgadas, B una línea horizontal gruesa?", "A", "El pasto crece hacia arriba y sus hojas son finas."),
            arith("Dibujas 3 líneas rectas gruesas y 5 líneas onduladas delgadas. ¿Cuántas líneas dibujaste en total?", "3 + 5", "Se suman las líneas de ambas clases."),
            ex("Quieres dibujar un rayo en una tormenta. ¿Qué línea eliges: recta, ondulada o irregular?", "Irregular", "Un rayo cambia de rumbo bruscamente."),
        ],
        "reason": [
            ex("Ana quiere dibujar un lago muy calmo y usó diagonales irregulares por todos lados. ¿Cuadra con lo que quiere mostrar?", "No", "Líneas nerviosas no dan sensación de calma."),
            ex("Para mostrar un cerro muy fuerte y firme, ¿conviene una línea gruesa o una muy delgada?", "Gruesa", "La línea gruesa transmite fuerza."),
        ],
        "challenge": [
            arith("Haces una hoja con 4 filas de 6 líneas verticales delgadas. ¿Cuántas líneas hiciste?", "6 + 6 + 6 + 6", "Son cuatro filas de seis líneas: se suma 6 cuatro veces."),
            ex("Describe con dos tipos de línea un camino de montaña que sube y se quiebra: escribe qué dos usarías.", "Diagonal e irregular", "Sube en diagonal y cambia de rumbo."),
        ],
    },
    context=[ex("Para el afiche del curso quieres dibujar lluvia y un charco. Escribe qué línea usas para cada una: lluvia (gotas que caen) y charco (agua que se mueve en ondas).", "Lluvia: líneas verticales o diagonales delgadas; charco: líneas onduladas", "Las gotas caen en línea y el agua se mueve en ondas.")],
    selfcheck=[
        ex("¿Cómo se llama la línea que cambia de rumbo sin orden?", "Irregular", "Es el camino sin orden."),
        ex("¿Una línea parada como un poste es vertical u horizontal?", "Vertical", "Parada se dice vertical."),
        ex("¿Qué línea muestra mejor un mar calmo?", "Ondulada", "Las ondas suaves sugieren olas tranquilas."),
    ],
    open_task=task(
        "En una hoja dividida en cuatro cuadros, dibuja con líneas: (1) un mar tranquilo, (2) una tormenta con rayos, (3) un pasto alto, (4) una escalera apoyada en la pared. Usa en cada uno la línea que mejor muestre la idea y escribe debajo su nombre, por ejemplo «ondulada delgada».",
        "Cuadro 1: ondas delgadas. Cuadro 2: rayos irregulares gruesos. Cuadro 3: verticales cortas delgadas. Cuadro 4: dos diagonales gruesas y varias horizontales.",
        ["usa líneas distintas en cada cuadro", "las nombra bien", "varía el grosor"],
        ["hoja con cuatro cuadros", "nombre de cada línea"],
        ["usar la misma línea en todos", "confundir ondulada con irregular"],
        "Reconoce la variedad y pide revisar cuáles líneas se pueden volver más gruesas o más delgadas.",
    ),
    reinforce="Con un lápiz, practica llenando una hoja con una línea recta, una ondulada y una irregular.",
    extend="Dibuja un animal usando solo líneas rectas y otro usando solo líneas onduladas; cuenta cuál se ve más suave.",
)

# ---------------------------------------------------------------- Clase 2
register(
    OA2, 2,
    materials="Témperas de rojo, amarillo, azul y blanco, o lápices de cera o de colores; un pincel o dedo, agua y una hoja. Las recetas están escritas en el cuaderno.",
    use="Aprenderé a distinguir los colores puros de los mezclados y a crear nuevos colores. Sirve para tener muchos colores aunque solo tenga pocos lápices o pinturas.",
    prior=["Sé nombrar los colores.", "Sé usar un pincel o un lápiz de color."],
    explain=[
        "Un color puro es el que sale directo del tubo o del lápiz, sin mezclar con otro. Aquí usaremos el rojo, el amarillo y el azul como colores puros. Con ellos se pueden hacer muchos otros colores.",
        "Un color mezclado se crea al juntar dos colores. Amarillo con azul da verde. Rojo con amarillo da naranja. Rojo con azul da violeta. Si mezclas más cantidad de un color, el resultado se parece más a ese color.",
        "También puedes aclarar un color mezclándolo con blanco: rojo con blanco da rosado y azul con blanco da celeste. Si solo tienes lápices, puedes pintar una capa y luego otra encima, apretando suave, y los colores se mezclan en el papel.",
    ],
    vocab=[("color puro", "color sin mezclar, como sale del tubo o del lápiz"), ("color mezclado", "color que se hizo juntando dos o más colores"), ("mezclar", "juntar colores para crear otro"), ("aclarar", "agregar blanco para que el color se vea más claro"), ("capa", "una pasada de color sobre el papel")],
    worked=[
        {"title": "Receta de un verde", "problem": "No tienes lápiz verde. ¿Cómo haces verde con tus colores puros?", "steps": ["El verde es mezcla de amarillo y azul.", "Pinto una capa de amarillo.", "Pinto encima una capa de azul con suavidad."], "answer": "Amarillo con azul"},
        {"title": "Aclarar un color", "problem": "Quieres un celeste para pintar el cielo del día. ¿Qué mezclas?", "steps": ["Partimos de azul puro.", "Agregamos un poco de blanco.", "Revolvemos hasta que el color sea claro."], "answer": "Azul con blanco"},
    ],
    mistakes=[
        {"wrong": "Mezclar demasiados colores a la vez y obtener un café sucio.", "why": "Cada color nuevo cambia el resultado y se pierde el color buscado.", "fix": "Mezcla solo dos colores a la vez y agrega de a poco."},
        {"wrong": "Pensar que rojo y azul dan verde.", "why": "Se confunden las recetas.", "fix": "Verde se hace con amarillo y azul; rojo con azul da violeta."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué color sale de mezclar amarillo con azul?", "Verde", "Esa es la receta del verde."),
            ex("¿Qué color sale de mezclar rojo con amarillo?", "Naranja", "Rojo y amarillo dan naranja."),
            ex("¿Cuál es un color puro: rojo o verde?", "Rojo", "El verde se obtiene mezclando; el rojo no."),
        ],
        "understand": [
            ex("¿Qué es un color puro? A: el que se hizo mezclando. B: el que sale sin mezclar. C: el más claro.", "B", "Puro significa que no está mezclado."),
            ex("Al mezclar azul con blanco, ¿el color queda más claro o más oscuro?", "Más claro", "El blanco aclara los colores."),
            ex("Si mezclas más amarillo que azul, ¿el verde queda más amarillento o más azulado?", "Más amarillento", "Hay más cantidad de amarillo."),
        ],
        "apply": [
            ex("Quieres un violeta para pintar uvas. ¿Qué dos colores mezclas?", "Rojo y azul", "Rojo con azul da violeta."),
            ex("Quieres un rosado. ¿Qué dos colores mezclas?", "Rojo y blanco", "El blanco aclara el rojo y lo vuelve rosado."),
            arith("Mezclas 2 gotas de amarillo y 3 gotas de azul para hacer verde. ¿Cuántas gotas hay en la mezcla?", "2 + 3", "Se suman las gotas de ambos colores."),
        ],
        "reason": [
            ex("Pilar mezcló rojo, azul, amarillo y verde a la vez, y quedó café. ¿Qué le sugieres: A mezclar solo dos colores, B mezclar más colores?", "A", "Con dos colores el resultado es más controlado."),
            ex("Un dibujo tiene un cielo celeste y un pasto verde. ¿Cuántos colores son mezclados: ninguno, uno o dos?", "Dos", "Celeste y verde se hacen mezclando."),
        ],
        "challenge": [
            arith("Para pintar una pradera usas 4 pinceladas de amarillo puro y 5 de verde mezclado. ¿Cuántas pinceladas hiciste?", "4 + 5", "Se suman las de ambos colores."),
            ex("Escribe las recetas de los tres colores mezclados que conoces: verde, naranja y violeta.", "Verde: amarillo y azul; naranja: rojo y amarillo; violeta: rojo y azul", "Cada mezcla une dos colores puros distintos."),
        ],
    },
    context=[ex("Para pintar una naranja y un limón pero solo tienes rojo, amarillo y azul, ¿cómo haces el naranja de la fruta?", "Mezclando rojo con amarillo", "Naranja es la mezcla de esos dos colores.")],
    selfcheck=[
        ex("¿Qué dos colores dan violeta?", "Rojo y azul", "Es la receta del violeta."),
        ex("¿Para qué sirve el blanco en una mezcla?", "Para aclarar", "Hace el color más claro."),
        ex("Un color mezclado, ¿está hecho con uno o con varios colores?", "Con varios", "Mezclar es juntar dos o más."),
    ],
    open_task=task(
        "Con tus colores o lápices, haz una paleta en una hoja: pinta cuadrados del tamaño de una moneda. Primero pinta tres cuadrados con rojo, amarillo y azul. Después pinta tres cuadrados mezclando de a dos: amarillo con azul, rojo con amarillo y rojo con azul. Escribe debajo el nombre del color que resultó. Por último, aclara uno con blanco y pinta un cuadrado más.",
        "Hice seis cuadrados: rojo, amarillo y azul puros; después verde, naranja y violeta mezclados. Aclaré el azul con blanco y salió celeste.",
        ["pinta tres colores puros", "hace tres mezclas", "nombra los resultados"],
        ["hoja con cuadrados de colores", "nombres escritos"],
        ["confundir recetas", "mezclar tres o más colores a la vez"],
        "Valora la paleta ordenada y sugiere probar mezclar más de un color con blanco para ver distintos tonos.",
    ),
    reinforce="Mezcla en el papel con lápices de color dos capas distintas y escribe qué color se formó.",
    extend="Haz cinco tonos de un color agregando cada vez un poco más de blanco y ordénalos del más oscuro al más claro.",
)

# ---------------------------------------------------------------- Clase 3
register(
    OA2, 3,
    materials="Lápices o témperas de colores, una hoja. Las escenas para colorear están escritas en el cuaderno.",
    use="Aprenderé a distinguir los colores cálidos de los fríos y a usarlos para dar sensación de calor o de frío. Sirve para que mis dibujos hagan sentir lo que quiero mostrar.",
    prior=["Sé nombrar los colores.", "Sé mezclar colores simples."],
    explain=[
        "Los colores pueden parecer cálidos o fríos. Los cálidos recuerdan al sol y al fuego: rojo, naranja y amarillo. Los fríos recuerdan al agua, al hielo y a la noche: azul, verde y violeta. Esto no es temperatura real, sino la sensación que dan.",
        "Un atardecer se pinta con colores cálidos, porque el cielo se ve naranja, rojo y amarillo. Una noche de nieve se pinta con fríos, como azul, violeta y verde azulado. Puedes mezclar ambos: un cielo azul con un solo sol amarillo hace que el sol resalte.",
        "Usar cálidos y fríos con intención significa decidir qué sensación quieres crear. Si pintas una playa de verano con colores cálidos y una nubecita azul, se ve más calurosa. Si pintas la misma playa con azules y violetas, se ve como una mañana helada.",
    ],
    vocab=[("color cálido", "color que parece de sol o fuego: rojo, naranja, amarillo"), ("color frío", "color que parece de agua o hielo: azul, verde, violeta"), ("temperatura del color", "sensación de calor o frío que da un color"), ("contraste", "diferencia fuerte entre dos cosas, como un punto cálido en un fondo frío"), ("sensación", "lo que me hace sentir una imagen")],
    worked=[
        {"title": "Clasificar colores", "problem": "Clasifica en cálidos y fríos: azul, naranja, verde, rojo.", "steps": ["Cálidos: recuerdan al sol y al fuego: naranja y rojo.", "Fríos: recuerdan al agua y al hielo: azul y verde."], "answer": "Cálidos: naranja y rojo. Fríos: azul y verde"},
        {"title": "Elegir colores para un atardecer", "problem": "Vas a pintar un atardecer en el desierto. ¿Qué grupo de colores usas para el cielo?", "steps": ["El sol bajo es naranja y rojo.", "Esos colores son cálidos.", "Uso cálidos para el cielo."], "answer": "Cálidos: naranja, rojo y amarillo"},
    ],
    mistakes=[
        {"wrong": "Pensar que un color frío hace que algo esté frío de verdad.", "why": "Se confunde sensación con temperatura real.", "fix": "Recuerda que es solo cómo se ve y cómo hace sentir."},
        {"wrong": "Usar solo cálidos o solo fríos en todo el dibujo sin intención.", "why": "Se pierde el contraste.", "fix": "Elige un grupo principal y agrega un pequeño toque del otro."},
    ],
    tiers={
        "recovery": [
            ex("¿El rojo es un color cálido o frío?", "Cálido", "Recuerda al fuego."),
            ex("¿El azul es un color cálido o frío?", "Frío", "Recuerda al agua y al hielo."),
            ex("¿El amarillo es un color cálido o frío?", "Cálido", "Recuerda al sol."),
        ],
        "understand": [
            ex("¿Cuál de estos grupos tiene solo colores fríos? A: azul, verde, violeta. B: rojo, naranja, azul. C: amarillo, rojo, verde.", "A", "Los tres son fríos."),
            ex("¿Para qué se usan los colores cálidos en un dibujo? A: para dar sensación de calor. B: para borrar. C: para hacerlo más pequeño.", "A", "Los cálidos hacen sentir calor."),
            ex("¿Qué es el contraste de temperatura? A: un toque cálido en un dibujo frío o al revés. B: pintar con un solo color.", "A", "Contraste es mezclar lo opuesto."),
        ],
        "apply": [
            ex("Clasifica en cálidos o fríos: violeta, naranja, verde. Escribe cuántos son fríos.", "2", "Violeta y verde son fríos; naranja es cálido."),
            ex("Vas a pintar un volcán con lava. ¿Qué colores eliges para la lava: naranja y rojo, o azul y violeta?", "Naranja y rojo", "La lava recuerda al fuego."),
            ex("Vas a pintar un glaciar. ¿Qué grupo eliges: cálidos o fríos?", "Fríos", "El hielo se asocia con azul y celeste."),
        ],
        "reason": [
            ex("Dani pintó una noche nevada con rojos y naranjas fuertes. ¿Se logra la sensación de frío?", "No", "Los cálidos dan sensación de calor."),
            ex("Para que una luna amarilla resalte en un cielo azul, ¿qué recurso usas: contraste o mezcla?", "Contraste", "Un toque cálido en un fondo frío destaca."),
        ],
        "challenge": [
            arith("En un dibujo hay 6 cuadrados cálidos y 9 cuadrados fríos. ¿Cuántos cuadrados hay en total?", "6 + 9", "Se suman ambos grupos."),
            ex("Describe en una frase cómo cambiarías una playa fría para que se vea calurosa.", "Cambiaría azules por amarillos y naranjas", "Pasar a cálidos aumenta la sensación de calor."),
        ],
    },
    context=[ex("Para la tarjeta de invierno de tu abuela quieres que parezca una mañana helada. ¿Qué grupo de colores usas?", "Fríos: azul, violeta y verde", "Los fríos transmiten sensación de hielo.")],
    selfcheck=[
        ex("¿El verde es cálido o frío?", "Frío", "Recuerda al agua y a las plantas frescas."),
        ex("¿El naranja es cálido o frío?", "Cálido", "Recuerda al sol."),
        ex("¿Qué grupo usas para un atardecer: cálido o frío?", "Cálido", "El cielo del atardecer se ve naranja y rojo."),
    ],
    open_task=task(
        "Elige UNA escena: (A) un día de mucho calor en la playa; (B) una noche de nieve en el sur; (C) un atardecer en el campo. Píntala con el grupo de colores que corresponde y agrega un pequeñísimo toque del grupo contrario para hacer contraste. Escribe: «Usé colores… porque quería mostrar…».",
        "Elegí B. Usé azul, violeta y verde porque quería mostrar frío. Puse una ventana amarilla en la casa como toque cálido.",
        ["usa un grupo de temperatura claro", "agrega un toque contrario", "explica su intención"],
        ["pintura", "frase con la intención"],
        ["usar los dos grupos sin orden", "no decir qué sensación buscó"],
        "Reconoce la intención y pide mirar si el toque contrario es pequeño y destaca bien.",
    ),
    reinforce="Con tus lápices, separa en dos montones los cálidos y los fríos.",
    extend="Pinta la misma casa dos veces, una con cálidos y otra con fríos, y cuenta qué sensación da cada una.",
)

# ---------------------------------------------------------------- Clase 4
register(
    OA2, 4,
    materials="Papel delgado, lápiz de cera o lápiz de color usado de lado, y objetos con relieve: una moneda, una hoja de árbol, una malla de bolsa de frutas, un trozo de cartón corrugado. Nada punzante.",
    use="Aprenderé a reconocer texturas que se tocan y texturas que solo se ven, y a crear texturas con la técnica del frotado. Sirve para que mis dibujos parezcan rugosos, suaves o con relieve.",
    prior=["Sé tocar objetos y decir cómo se sienten.", "Sé usar un lápiz de cera."],
    explain=[
        "La textura es cómo se ve o cómo se siente la superficie de algo. La textura táctil se siente con las manos: la lija es áspera, el algodón es suave, un vidrio es liso. La textura visual solo se ve: en una hoja lisa puedes dibujar puntitos y parecer arena.",
        "Para crear una textura puedes usar la técnica del frotado, que se hace así: 1. Pon un objeto con relieve, como una hoja, debajo de un papel delgado. 2. Toma el lápiz de cera de lado. 3. Frota con suavidad hasta que aparezca la forma. Las líneas del objeto se pasan al papel. En el frotado copias la textura de un objeto que sí se puede tocar, aunque en el papel solo se vea.",
        "También puedes crear texturas visuales con puntos, rayitas, círculos o manchas repetidas. Si repites rayitas cortas, parece pelo; si repites círculos pequeños, parece una piel con escamas. Elegir una textura es una decisión del artista.",
    ],
    vocab=[("textura", "cómo se ve o se siente la superficie de algo"), ("textura táctil", "la que se siente al tocar"), ("textura visual", "la que se ve pero no se siente, porque la superficie es lisa"), ("áspero", "que raspa al tocar, como la lija"), ("frotado", "técnica para pasar al papel el relieve de un objeto")],
    worked=[
        {"title": "Hacer un frotado", "problem": "Quieres pasar al papel las nervaduras de una hoja de árbol. ¿Qué haces?", "steps": ["Pongo la hoja debajo de un papel delgado.", "Tomo el lápiz de cera de lado.", "Froto con suavidad sobre la hoja.", "Aparecen sus líneas en el papel."], "answer": "Se frota con la cera de lado sobre el papel que cubre la hoja"},
        {"title": "Crear una textura visual", "problem": "Quieres dibujar la piel de un pez con escamas en una hoja lisa. ¿Qué repites?", "steps": ["Una escama tiene forma de medio círculo.", "Dibujo muchos medios círculos, uno junto a otro.", "La repetición crea la sensación de escamas."], "answer": "Muchos medios círculos repetidos"},
    ],
    mistakes=[
        {"wrong": "Apretar muy fuerte al frotar y romper el papel.", "why": "La presión excesiva rasga el papel delgado.", "fix": "Frota suave y con el lápiz de lado."},
        {"wrong": "Creer que una textura visual se puede tocar.", "why": "Se confunde con la táctil.", "fix": "La visual se ve en una superficie lisa; la táctil se siente con la mano."},
    ],
    tiers={
        "recovery": [
            ex("La lija raspa al tocar. ¿Es suave o áspera?", "Áspera", "Raspar es característico de lo áspero."),
            ex("Un algodón se siente muy blando. ¿Su textura es suave o áspera?", "Suave", "Blando y delicado es suave."),
            ex("Si dibujas puntitos para parecer arena en una hoja lisa, ¿la textura es táctil o visual?", "Visual", "No se siente, solo se ve."),
        ],
        "understand": [
            ex("¿Cuál se siente con la mano? A: textura visual. B: textura táctil.", "B", "Táctil viene de tocar."),
            ex("¿Para qué sirve la técnica del frotado? A: para pasar el relieve de un objeto al papel. B: para borrar. C: para recortar.", "A", "Así aparecen las líneas del objeto en el papel."),
            ex("En el frotado, ¿tomas el lápiz de cera de punta o de lado?", "De lado", "De lado cubre más superficie y marca el relieve."),
        ],
        "apply": [
            ex("Ordena los pasos del frotado con letras: A frotar suave, B poner el objeto debajo del papel, C tomar la cera de lado.", "B, C, A", "Primero se ubica el objeto, luego se toma la cera y se frota."),
            ex("Quieres dibujar la piel de un elefante, arrugada y rugosa. ¿Qué dibujas: A líneas quebradas cortas y muchas, B círculos grandes?", "A", "Las líneas cortas parecen arrugas."),
            arith("En una hoja dibujas 5 filas de 6 puntitos para parecer arena. ¿Cuántos puntitos dibujaste?", "6 + 6 + 6 + 6 + 6", "Son cinco filas iguales de seis: se suma 6 cinco veces."),
        ],
        "reason": [
            ex("Julio quiere que el pelo de su perro dibujado se vea suave. ¿Qué le conviene: líneas cortas y finas muy juntas o puntos grandes separados?", "Líneas cortas y finas muy juntas", "Así se parece al pelo."),
            ex("Luisa frota una moneda y no ve nada. Usó una hoja gruesa de cartulina. ¿Qué puede cambiar para que salga la moneda?", "Usar un papel más delgado", "El papel delgado deja pasar el relieve."),
        ],
        "challenge": [
            arith("Una tabla de texturas tiene 3 táctiles y 4 visuales. ¿Cuántas texturas hay?", "3 + 4", "Se suman los dos tipos."),
            ex("Escribe tres palabras que describan una textura táctil que conozcas, por ejemplo de una fruta o de una tela.", "Respuestas posibles: áspero, suave, rugoso, liso", "Son palabras que nombran sensaciones del tacto."),
        ],
    },
    context=[ex("Quieres que en tu dibujo un tronco de árbol parezca rugoso. ¿Qué técnica usas con una corteza de verdad?", "El frotado", "El frotado pasa al papel el relieve de la corteza.")],
    selfcheck=[
        ex("¿Qué es una textura visual?", "La que se ve pero no se siente", "La superficie del papel es lisa."),
        ex("¿Un vidrio es liso o áspero?", "Liso", "Su superficie no raspa."),
        ex("¿Con qué lápiz haces mejor un frotado: de punta fina o de cera usado de lado?", "De cera de lado", "Marca el relieve en una zona ancha."),
    ],
    open_task=task(
        "Haz un cuadrado dividido en cuatro partes. En dos partes haz frotados con dos objetos distintos de tu casa (por ejemplo una hoja y una malla de bolsa de frutas). En las otras dos partes crea dos texturas visuales con puntos, rayitas o círculos. Debajo de cada parte escribe si la textura viene de un objeto que se toca (táctil) o si la dibujaste tú (visual), y cómo se ve.",
        "Parte 1: frotado de hoja, táctil, con líneas finas. Parte 2: frotado de malla, con cuadritos. Parte 3: puntitos, visual, parece arena. Parte 4: rayitas cortas, visual, parece pasto.",
        ["usa la técnica del frotado", "crea dos texturas visuales", "las clasifica bien"],
        ["cuadro con cuatro partes", "etiquetas de clasificación"],
        ["usar papel muy grueso", "confundir táctil con visual"],
        "Reconoce la variedad de texturas y pide describir con palabras cómo se vería al tocar cada una.",
    ),
    reinforce="Con una hoja de papel delgado y un lápiz de cera, frota una moneda y mira qué aparece.",
    extend="Combina dos frotados distintos para crear un animal inventado y cuenta qué texturas usaste.",
)

# ---------------------------------------------------------------- Clase 5
register(
    OA2, 5,
    materials="Una hoja, lápices o témperas, lápiz de mina y objetos para hacer frotados. El plan de la obra está escrito en el cuaderno.",
    use="Aprenderé a juntar línea, color y textura en una misma obra y a explicar por qué elegí cada una. Sirve para hacer composiciones con intención y no al azar.",
    prior=["Sé usar líneas de distintas clases.", "Sé diferenciar colores cálidos de fríos y texturas táctiles de visuales."],
    explain=[
        "En una composición, la línea, el color y la textura trabajan juntos. La línea marca formas y caminos. El color da sensación. La textura da superficie. El artista decide cuál de los tres destaca más y cómo se combinan.",
        "Piet Mondrian, un pintor de los Países Bajos, hizo muchas obras con líneas rectas negras y rectángulos de rojo, amarillo, azul y blanco. Wassily Kandinsky, un pintor ruso, combinó líneas, círculos y triángulos de muchos colores. Cada uno decidió dar más importancia a elementos distintos.",
        "Para que una composición tenga orden puedes repetir un elemento, como una línea ondulada en varias partes, o crear un contraste, como un solo círculo cálido entre muchos fríos. Al terminar, explicas tu elección: «Usé líneas… porque…».",
    ],
    vocab=[("composición", "la manera como se ordenan los elementos en la obra"), ("repetición", "usar el mismo elemento varias veces"), ("contraste", "diferencia fuerte que hace destacar algo"), ("elemento visual", "línea, color o textura que se usan para crear"), ("explicar una elección", "dar una razón basada en lo que se ve")],
    worked=[
        {"title": "Planificar una noche de lluvia", "problem": "Quieres mostrar una noche de lluvia. ¿Qué eliges de línea, color y textura?", "steps": ["Línea: verticales delgadas, como gotas que caen.", "Color: azul y violeta, que son fríos.", "Textura: puntitos visuales para los charcos."], "answer": "Verticales delgadas, colores fríos y puntitos"},
        {"title": "Crear un contraste", "problem": "En la noche de lluvia quieres que una ventana destaque. ¿Qué haces?", "steps": ["El fondo es azul y violeta (fríos).", "Pinto la ventana de amarillo (cálido).", "El amarillo contrasta con los fríos y resalta."], "answer": "Pintar la ventana de amarillo"},
    ],
    mistakes=[
        {"wrong": "Usar todos los colores, todas las líneas y todas las texturas en un solo dibujo.", "why": "Hay demasiado y nada destaca.", "fix": "Elige pocas líneas, un grupo de colores y una o dos texturas."},
        {"wrong": "Explicar solo «lo hice así porque me gusta».", "why": "No se dice qué elemento se ve ni por qué se eligió.", "fix": "Usa «Usé… para mostrar…» y nombra una línea, un color o una textura."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuáles son los tres elementos visuales de esta unidad? A: línea, color y textura. B: letra, número y signo. C: ruido, olor y sabor.", "A", "Son los elementos del lenguaje visual."),
            ex("Un círculo rojo entre muchos círculos azules destaca. ¿Esto es repetición o contraste?", "Contraste", "Un elemento diferente resalta."),
            ex("Si repites muchas veces la misma línea ondulada, ¿usas repetición o contraste?", "Repetición", "Es el mismo elemento muchas veces."),
        ],
        "understand": [
            ex("¿Con qué colores pintó Mondrian rectángulos entre líneas negras? A: rojo, amarillo, azul y blanco. B: solo verde.", "A", "Esos fueron los colores de sus composiciones."),
            ex("¿Qué es explicar una elección? A: dar una razón basada en lo que se ve. B: decir que no sé.", "A", "La razón se apoya en un elemento visible."),
            ex("En una composición con líneas rectas negras y rectángulos de colores, ¿la textura es protagonista o el color y la línea?", "El color y la línea", "Ahí lo principal son las líneas negras y los rectángulos de color."),
        ],
        "apply": [
            ex("Quieres que tu pintura de un día de mucho sol muestre calor. ¿Qué colores usas más: cálidos o fríos?", "Cálidos", "Los cálidos dan sensación de calor."),
            arith("Tu composición tiene 4 rectángulos rojos, 3 amarillos y 2 azules. ¿Cuántos rectángulos hay?", "4 + 3 + 2", "Se suman los tres colores."),
            ex("Quieres que un pájaro rojo destaque sobre un fondo de hojas verdes. ¿Qué recurso usas: contraste o repetición?", "Contraste", "El rojo se ve distinto del verde que lo rodea."),
        ],
        "reason": [
            ex("Tere llenó la hoja de líneas, colores y texturas distintas y dice que no se entiende. ¿Qué debe hacer: A quitar elementos y dejar pocos, B agregar más?", "A", "Menos elementos aclaran la obra."),
            ex("Una frase dice «Usé azul para mostrar frío». ¿Nombra un elemento que se ve en la obra?", "Sí", "Nombra el color azul."),
        ],
        "challenge": [
            arith("En una obra pones 3 filas de 5 círculos fríos y 1 círculo cálido. ¿Cuántos círculos hay en total?", "5 + 5 + 5 + 1", "Son 3 filas de 5 círculos fríos (se suma 5 tres veces) y se agrega el círculo cálido."),
            ex("Escribe una frase que explique una elección con línea, color y textura para una playa en invierno.", "Usé líneas onduladas, colores fríos y puntitos para mostrar el frío de la arena", "La frase nombra los tres elementos y la intención."),
        ],
    },
    context=[ex("Quieres mostrar la alegría de una fiesta en un cumpleaños. ¿Qué eliges: colores cálidos y líneas onduladas, o colores fríos y líneas rectas?", "Colores cálidos y líneas onduladas", "Lo cálido y ondulado transmite alegría y movimiento.")],
    selfcheck=[
        ex("¿Qué es la composición?", "La manera como se ordenan los elementos en la obra", "Es el orden de lo que se pone en la hoja."),
        ex("¿Qué elemento visual da sensación de calor o frío?", "El color", "Los cálidos y fríos son colores."),
        ex("¿Qué recurso consiste en repetir un elemento?", "Repetición", "Se usa el mismo elemento varias veces."),
    ],
    open_task=task(
        "Elige UNA idea: (A) una noche de lluvia; (B) un día de fiesta; (C) un bosque silencioso. Decide una línea, un grupo de colores y una textura. Haz la obra en media hoja y agrega un contraste. Escribe: «Usé… para mostrar…».",
        "Elegí C. Usé líneas verticales delgadas (árboles), colores fríos y puntitos (hojas). Agregué un zorro naranja como contraste. Usé colores fríos para mostrar silencio.",
        ["elige una línea, color y textura", "incluye un contraste", "explica su elección"],
        ["obra", "frase «Usé… para mostrar…»"],
        ["usar demasiados elementos", "explicar sin nombrar un elemento visual"],
        "Valora la intención y sugiere reducir elementos si la obra se ve recargada.",
    ),
    reinforce="Observa un afiche o una caja de tu casa y nombra una línea, un color y una textura que veas en ella.",
    extend="Haz la misma composición en blanco y negro con solo líneas y texturas, y cuenta qué cambia sin el color.",
)

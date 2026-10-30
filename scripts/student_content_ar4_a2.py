"""Cuaderno del estudiante de 4.º básico Artes Visuales: AR04 OA 03 (materiales y procedimientos), AR04 OA 04 (observar obras) y AR04 OA 05 (retroalimentación)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR04 OA 03"
OA4 = "AR04 OA 04"
OA5 = "AR04 OA 05"


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


# ================================================================ OA 03
# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Plasticina, masa para modelar o arcilla; objetos con relieve y limpios (tapas, hojas, un peine de plástico); témpera, un trozo de esponja y papel. Cubre la mesa con un diario.",
    "Aprenderé a modelar una forma y a dejar una huella con un objeto, probando cómo resulta cada material. Sirve para elegir bien el material antes de crear una obra.",
    ["Sé que la textura puede ser visual o táctil.", "Sé modelar con las manos formas simples."],
    [
        "Modelar es dar forma con las manos a un material blando, como plasticina, masa o arcilla. Se puede hacer una forma redonda, alargada o plana. Una huella es la marca que deja un objeto cuando se presiona sobre un material blando o cuando se moja con pintura y se apoya en el papel. La huella es el principio del grabado: una imagen que se puede repetir muchas veces.",
        "Para probar, hazlo en tres pasos. Primero, elige un objeto con relieve, como una tapa, una hoja o un peine. Segundo, presiónalo sobre la plasticina y míralo: ¿qué marca deja? Tercero, mójalo con un poco de témpera y apóyalo sobre el papel: ¿la huella es igual? Una huella sobre plasticina es una marca hundida; una huella con pintura es una marca de color. Anota qué cambió.",
        "Cada material tiene sus ventajas. La plasticina se modela sin esfuerzo y nunca queda dura. La arcilla se puede secar y queda dura. La masa casera se seca, pero se agrieta si es muy gruesa. Usa pintura en poca cantidad y lávate las manos al terminar. Guarda los materiales cerrados para que no se sequen.",
    ],
    [("modelar", "dar forma con las manos a un material blando"), ("huella", "marca que deja un objeto al presionarlo sobre un material o sobre el papel con pintura"), ("grabado", "técnica que permite repetir una imagen muchas veces a partir de una marca"), ("relieve", "parte que sobresale en una superficie"), ("prueba", "intento pequeño que hago antes de la obra final")],
    [
        w("Probar una huella", "Quieres saber qué huella deja una tapa con relieve de círculos. ¿Cómo la pruebas?", ["Presiono la tapa sobre la plasticina.", "Miro la marca: son círculos hundidos.", "Pinto la tapa con témpera y la apoyo sobre el papel para ver la otra huella."], "Dos huellas: una hundida en la plasticina y otra de color en el papel"),
        w("Elegir un material", "Quieres hacer una figura que quede dura y pueda guardarse. ¿Qué material eliges: plasticina o arcilla?", ["La plasticina no se seca nunca.", "La arcilla se seca y queda dura.", "Elijo arcilla porque necesito que quede dura."], "Arcilla"),
    ],
    [
        m("Mojar el objeto con mucha pintura para que la huella se vea fuerte.", "La pintura se corre y la huella queda como una mancha.", "Usa poca pintura y apoya el objeto con firmeza y sin moverlo."),
        m("Hacer la obra final sin probar antes.", "No sabes cómo resultará el material y no puedes corregir.", "Haz una prueba pequeña y revisa el resultado antes."),
    ],
    [
        ex("Modelar es dar forma con las manos. ¿Un material blando para modelar es la plasticina o una regla?", "La plasticina", "La plasticina es blanda y se puede modelar."),
        ex("Una huella es una marca que deja un objeto. ¿Una tapa con relieve de círculos deja una huella de círculos o de triángulos?", "De círculos", "La huella copia el relieve del objeto."),
        ex("¿Cuál material se seca y queda duro: la plasticina o la arcilla?", "La arcilla", "La arcilla se seca y queda dura."),
    ],
    [
        ex("Presionas una hoja con nervios sobre plasticina y queda una marca hundida. ¿Esa huella es de color o es un relieve?", "Un relieve", "Está hundida en el material y no tiene pintura."),
        ex("Una huella con pintura sobre papel puede repetirse muchas veces. ¿Esa idea de repetir una imagen se parece al grabado o al modelado?", "Al grabado", "El grabado permite repetir una imagen a partir de una marca."),
        ex("Haces una prueba pequeña antes de hacer la obra final. ¿Qué ventaja tiene: puedes corregir antes de la obra final o la obra final queda lista más rápido?", "Puedes corregir antes de la obra final", "La prueba muestra cómo resulta el material antes de usarlo en la obra final."),
    ],
    [
        ex("Quieres una huella clara de un peine de plástico con pintura. ¿Usas una capa fina de pintura o mucha pintura?", "Una capa fina de pintura", "Con mucha pintura se llenan los espacios entre los dientes."),
        ex("Quieres que una figurita modelada quede dura y no se aplaste. ¿Eliges plasticina o arcilla?", "Arcilla", "La arcilla se seca y queda dura; la plasticina sigue blanda."),
        ex("Ordena: A) presionar el objeto, B) elegir un objeto con relieve, C) mirar la marca y anotar. Escribe las tres letras en orden.", "B, A, C", "Primero eliges, luego presionas y al final observas."),
    ],
    [
        ex("Una niña pintó una tapa con mucha témpera y la huella salió como una mancha. ¿Qué error cometió: usar demasiada pintura o usar la tapa al revés?", "Usar demasiada pintura", "El exceso de pintura rellenó el relieve."),
        ex("Un niño dice: «La plasticina sirve para todo, no necesito probar la arcilla». Si necesita que la figura se seque y dure, ¿tiene razón?", "No", "La plasticina nunca se seca; la arcilla sí."),
    ],
    [
        arith("Quieres hacer cinco huellas de una hoja en una tira de papel y pintas la hoja antes de cada huella. Ya hiciste dos huellas. ¿Cuántas veces más pintas la hoja?", "5-2", "Faltan las huellas que no has hecho y cada una necesita pintar la hoja de nuevo."),
        ex("Pruebas dos objetos para una huella: una tapa lisa y un peine de plástico con dientes. Quieres una huella con rayas finas. ¿Cuál eliges?", "El peine", "Los dientes del peine dejan rayas."),
    ],
    ex("Debes decorar una tira de papel para una invitación de curso con un patrón de huellas. Tienes una tapa con círculos, una hoja y una esponja. Quieres un patrón de líneas repetidas. ¿Qué objeto es mejor: la hoja con nervios o la esponja?", "La hoja con nervios", "Los nervios de la hoja dejan líneas."),
    [
        ex("¿Qué es una huella en arte?", "La marca que deja un objeto presionado", "Puede ser en material blando o con pintura."),
        ex("Verdadero o falso: antes de la obra final conviene hacer una prueba pequeña.", "Verdadero", "Sirve para ver cómo resulta el material."),
        ex("¿Qué técnica permite repetir una imagen muchas veces a partir de una marca?", "El grabado", "Así se define el grabado en esta clase."),
    ],
    task(
        "Con plasticina, masa o arcilla y dos objetos limpios con relieve (por ejemplo, una tapa y una hoja), haz una tira con tres huellas hundidas del mismo objeto. Con témpera, haz después tres huellas de color en papel. Escribe cuál te gustó más y por qué.",
        "Usé una tapa y una hoja. En la plasticina la hoja dejó una marca hundida con líneas. En el papel, con témpera verde, la huella se vio más clara. Me gustó más la de color porque se podía repetir fácil.",
        ["hace tres huellas de cada tipo", "usa poca pintura", "compara las dos huellas", "limpia y guarda los materiales"],
        ["tira de huellas hundidas", "tira de huellas de color", "una frase de comparación"],
        ["usar demasiada pintura", "no comparar las dos huellas"],
        "Reconoce la huella más clara y pregunta qué material usaría para un trabajo que debe durar mucho.",
    ),
    "Presiona un objeto con relieve de tu casa sobre plasticina o masa y describe la marca que deja con tres palabras.",
    "Combina dos huellas distintas en un mismo dibujo y anota qué efecto logras.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Hojas de papel de distintos tipos (diario, revista, de colores), cartulina, retazos de tela, pegamento en barra o cola fría, y una tijera de punta redonda. No cortes cartón grueso: dóblalo o rásgalo.",
    "Aprenderé a combinar papel, cartón y tela, y a pegarlos para que se mantengan unidos. Sirve para hacer collages y construcciones que no se despeguen.",
    ["Sé usar tijera de punta redonda con cuidado.", "Sé que cada material tiene una textura distinta."],
    [
        "El papel puede rasgarse, cortarse o doblarse. Rasgado, el borde queda irregular y suave; cortado, queda recto y limpio. El cartón es más firme que el papel y sirve de base para pegar. Los retazos de tela se pueden pegar sobre papel o cartón, y dan textura. Un collage es una obra hecha pegando varios materiales sobre una superficie.",
        "La adhesión es la forma en que dos materiales quedan pegados. El pegamento en barra sirve para papel liviano. La cola fría pega mejor papeles gruesos, cartón, tela y lana, pero se debe poner en poca cantidad y esperar a que seque. Si pones demasiado pegamento, el papel se arruga o se despega después. Presiona con un trozo de papel limpio para unir y alisar.",
        "Antes de pegar, ordena los trozos sobre la base sin pegamento: es el momento de decidir la composición. Cambia de lugar lo que no te convenza. Pega primero lo que va al fondo y al final lo que va adelante. Corta con tijera de punta redonda y siempre lejos de otras personas. Si algo no queda pegado, revisa si usaste muy poco pegamento, o muy poco tiempo de secado.",
    ],
    [("collage", "obra hecha pegando varios materiales sobre una superficie"), ("adhesión", "forma en que dos materiales quedan pegados"), ("rasgar", "romper el papel con las manos, dejando un borde irregular"), ("composición", "forma en que se ordenan los elementos de una obra"), ("secado", "tiempo que se espera para que el pegamento se endurezca")],
    [
        w("Elegir el pegamento", "Quieres pegar un retazo de tela sobre cartulina. ¿Qué pegamento eliges: barra o cola fría?", ["El pegamento en barra sirve para papel liviano.", "La tela es más pesada: necesita cola fría.", "Pongo poca cola y presiono con un papel limpio."], "Cola fría, en poca cantidad"),
        w("Ordenar antes de pegar", "Tienes cinco trozos de papel y quieres una montaña con un cielo. ¿Qué haces antes de pegar?", ["Pongo los trozos sobre la base sin pegamento.", "Cambio de lugar los que no me convencen.", "Cuando la composición me gusta, pego primero el cielo y luego la montaña."], "Probar la composición sin pegamento y pegar primero el fondo"),
    ],
    [
        m("Poner mucho pegamento para que no se despegue.", "El papel se arruga y tarda mucho en secar.", "Usa poco pegamento, distribuido parejo, y presiona."),
        m("Pegar todo sin probar la composición antes.", "Después no se puede cambiar de lugar sin romper el papel.", "Ordena los trozos sobre la base antes de pegar."),
    ],
    [
        ex("Rasgar el papel, ¿deja un borde recto o irregular?", "Irregular", "Al rasgar con las manos el borde queda desparejo."),
        ex("Un collage es una obra hecha pegando varios materiales. ¿Se puede hacer un collage con papel y tela?", "Sí", "Un collage combina materiales distintos."),
        ex("¿Qué pegamento sirve mejor para papel liviano: el pegamento en barra o la cola fría?", "El pegamento en barra", "La clase indica que la barra sirve para papel liviano."),
    ],
    [
        ex("Quieres hacer con papel las nubes suaves de un cielo. ¿Rasgas el papel o lo cortas recto con tijera?", "Lo rasgas", "El borde irregular se parece al borde suave de las nubes."),
        ex("Una niña pegó un cartón con muy poco pegamento y se cayó. ¿Qué parte del proceso falló: la adhesión o el color?", "La adhesión", "Quedó mal pegado."),
        ex("Pegas primero lo que va al fondo y al final lo que va adelante. ¿En un paisaje, pegas antes el cielo o el árbol del primer plano?", "El cielo", "El cielo está al fondo."),
    ],
    [
        ex("Quieres pegar un retazo de tela gruesa sobre cartón. ¿Usas pegamento en barra o cola fría?", "Cola fría", "La clase indica que la tela se pega mejor con cola fría."),
        ex("Tienes la cola fría y quieres que seque bien. ¿Pones una capa delgada o mucho pegamento?", "Una capa delgada", "Con poca cola seca más rápido y no arruga el papel."),
        ex("Ordena los pasos: A) pegar, B) ordenar los trozos sin pegamento, C) cortar o rasgar. Escribe las tres letras en orden.", "C, B, A", "Primero preparas los trozos, luego pruebas la composición y al final pegas."),
    ],
    [
        ex("Un niño pegó una tela en papel de diario con barra. Se despegó. Si la tela es pesada, ¿qué debió cambiar: el pegamento o el color del papel?", "El pegamento", "La barra no sostiene una tela pesada."),
        ex("Una niña dice: «Mi collage está terminado cuando pegué todo en el primer lugar donde lo puse». ¿Es el mejor método?", "No", "Conviene probar la composición antes de pegar."),
    ],
    [
        ex("Quieres un collage con tela, papel de revista y cartón. ¿Cuántos materiales distintos usas?", "Tres", "La tela, el papel de revista y el cartón son tres materiales distintos."),
        ex("Quieres que un collage de montañas dé sensación de relieve. ¿Pegas el papel rasgado formando capas o todo en una sola capa lisa?", "Formando capas", "Las capas superpuestas dan sensación de profundidad."),
    ],
    ex("En el colegio quieren hacer un mural con retazos de tela y papel para decorar la sala. Tienes cola fría y barra. Los retazos son pesados. ¿Qué eliges?", "Cola fría", "Sostiene mejor los materiales pesados."),
    [
        ex("¿Qué es un collage?", "Una obra hecha pegando varios materiales", "Los materiales se pegan sobre una superficie."),
        ex("Verdadero o falso: poner mucho pegamento siempre ayuda a que se pegue mejor.", "Falso", "Arruga el papel y demora el secado."),
        ex("¿Qué se hace antes de pegar un collage?", "Ordenar los trozos sin pegamento", "Así se decide la composición."),
    ],
    task(
        "Haz un collage de un paisaje de América (una cordillera, un lago o un desierto) con tres materiales distintos: papel, cartulina y un retazo de tela o de lana. Rasga el papel en una parte y corta la cartulina con tijera de punta redonda en otra. Antes de pegar, ordena todo. Pega primero el fondo. Escribe qué pegamento usaste en cada material y por qué.",
        "Hice una cordillera: cielo de cartulina azul cortada, montañas de papel de diario rasgado y un retazo de lana para la nieve. Usé barra para el papel de diario y cola fría para la cartulina y la lana, porque la barra pega mejor el papel liviano.",
        ["usa tres materiales", "ordena antes de pegar", "elige pegamentos adecuados", "usa la tijera con cuidado"],
        ["collage", "frase sobre los pegamentos"],
        ["pegar sin probar la composición", "usar demasiado pegamento"],
        "Valora la elección del pegamento y pregunta qué material cambiaría para dar más textura.",
    ),
    "Rasga un trozo de papel de diario y descríbele el borde a una persona de tu casa.",
    "Haz un collage pequeño con solo papel y otro con papel y tela. Anota qué diferencia de textura notas.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Materiales reutilizables limpios y secos: cajas de cartón, rollos de papel de cocina, envases de plástico blando, cartones de huevos, tapas grandes. No uses vidrio, latas ni objetos filosos. Pegamento y témpera.",
    "Aprenderé a transformar materiales limpios que ya no se usan en una obra nueva. Sirve para reutilizar con creatividad y cuidar el ambiente.",
    ["Sé pegar papel, cartón y tela.", "Sé hacer una prueba pequeña antes de una obra final."],
    [
        "Reutilizar es darle un uso nuevo a algo que ya se iba a botar. Un rollo de cartón puede ser el cuerpo de un animal. Una caja puede ser una casa. Un envase de plástico blando limpio puede ser una cabeza. Los materiales reutilizables deben estar limpios, secos y sin partes que corten, como vidrio, latas o plásticos quebrados.",
        "Transformar un material es cambiar cómo se ve para que parezca otra cosa. Puedes cubrirlo con papel, pintarlo, unirlo con otro o cortar partes con tijera de punta redonda. Para decidir qué material usar, observa su forma: un cilindro sirve para un cuerpo y una caja sirve para algo cuadrado. Elige el material por su forma y no solo por lo que era.",
        "Para unir materiales distintos, usa cola fría o cinta de papel, y deja secar bien. Pinta con témpera las zonas que quieras cubrir de color, y deja la textura original en las zonas donde quieras que se note el material. Anota qué reutilizaste y cuál era su uso original, y devuelve lo que no uses al reciclaje.",
    ],
    [("reutilizar", "dar un uso nuevo a algo que ya se iba a botar"), ("transformar", "cambiar cómo se ve algo para que parezca otra cosa"), ("material reutilizable", "material limpio y seguro que puede tener otro uso"), ("cilindro", "forma larga y redonda, como un rollo de papel"), ("reciclaje", "proceso para que un material se use otra vez")],
    [
        w("Elegir un material por su forma", "Quieres hacer el cuerpo de un pingüino. Tienes un rollo de cartón y una caja cuadrada. ¿Cuál eliges?", ["Un pingüino tiene el cuerpo redondeado y largo.", "El rollo de cartón es un cilindro.", "Elijo el rollo por su forma."], "El rollo de cartón"),
        w("Transformar un envase", "Tienes un envase de plástico blando limpio y quieres que parezca la cabeza de un animal. ¿Qué haces?", ["Lo cubro con papel pegado con cola fría.", "Le pinto la cara con témpera.", "Le agrego orejas de cartón."], "Cubrirlo con papel, pintarlo y agregar orejas de cartón"),
    ],
    [
        m("Usar un vidrio roto o una lata abierta porque «es solo para una obra».", "Pueden cortar la piel.", "Usa solo materiales sin bordes filosos, limpios y secos."),
        m("Pegar sin limpiar el envase, con restos de comida.", "Huele mal, atrae insectos y no se pega bien.", "Lava y seca el envase antes de usarlo."),
    ],
    [
        ex("¿Qué significa reutilizar: botar algo o darle un uso nuevo?", "Darle un uso nuevo", "Reutilizar es usar otra vez, de otra manera."),
        ex("¿Cuál de estos materiales NO es seguro para una obra: un rollo de cartón o una lata abierta?", "Una lata abierta", "El borde de la lata puede cortar."),
        ex("Un cilindro es largo y redondo. ¿Un rollo de papel es un cilindro?", "Sí", "Tiene forma larga y redonda."),
    ],
    [
        ex("Quieres hacer una casa. ¿Qué material reutilizable sirve mejor por su forma: una caja o un rollo de cartón?", "Una caja", "Una caja tiene forma cuadrada, como una casa."),
        ex("Un niño quiere usar un envase de yogur con restos adentro. ¿Qué debe hacer antes de usarlo: lavarlo y secarlo o pintarlo así como está?", "Lavarlo y secarlo", "Un material reutilizable debe estar limpio y seco; con restos no se pega bien."),
        ex("Transformar un material es cambiar cómo se ve para que parezca otra cosa. Si cubres un rollo con papel café y le pintas ojos, ¿lo transformaste?", "Sí", "Ahora parece un animal y no un rollo."),
    ],
    [
        ex("Quieres un cuerpo largo para un gusano. ¿Eliges un cartón de huevos o un rollo de cartón?", "Un rollo de cartón", "Es largo y redondo, como un gusano."),
        ex("Pegaste un rollo sobre una caja con cola fría y quieres mover la obra enseguida. ¿Qué haces: esperar a que seque o moverla de inmediato?", "Esperar a que seque", "Para unir materiales hay que dejar secar bien la cola."),
        ex("Ordena: A) transformar con papel y pintura, B) elegir el material por su forma, C) guardar lo que sobra para reciclar. Escribe las tres letras en orden.", "B, A, C", "Se elige, se transforma y al final se ordena lo que sobra."),
    ],
    [
        ex("Ana dice: «Mi obra sirve para cuidar el ambiente, porque usé materiales que se iban a botar». ¿Su razón se relaciona con reutilizar?", "Sí", "Reutilizar es dar un nuevo uso a lo que se iba a botar."),
        ex("Pedro hizo un robot con latas abiertas. ¿Su obra cumple la regla de seguridad de la clase?", "No", "Las latas tienen bordes que cortan."),
    ],
    [
        ex("Quieres que se note el material original en parte de tu obra. ¿Dejas una zona sin pintar o la cubres toda con pintura?", "Dejas una zona sin pintar", "Así se ve el material original."),
        ex("Un cartón de huevos tiene varios huecos redondeados. ¿Sirve mejor para hacer un panal de abejas o una torre larga?", "Un panal de abejas", "Los huecos repetidos se parecen al panal."),
    ],
    ex("En el colegio hacen una feria de reciclaje y debes presentar un animal hecho con materiales limpios. Tienes un rollo, una caja pequeña y una botella de plástico blando. Quieres un perro de cuerpo largo. ¿Qué usas para el cuerpo?", "El rollo", "Es un cilindro largo, como el cuerpo de un perro."),
    [
        ex("¿Qué debe tener un material reutilizable para una obra?", "Estar limpio, seco y sin bordes filosos", "Así es seguro y se pega bien."),
        ex("Verdadero o falso: se elige un material por su forma y no solo por lo que era.", "Verdadero", "La forma indica para qué parte de la obra sirve."),
        ex("¿Qué haces con lo que sobra de la obra y no usas?", "Lo guardas o lo reciclas", "Se devuelve al reciclaje para cuidar el ambiente."),
    ],
    task(
        "Elige UN animal de América: un zorro, un pingüino o un cóndor. Hazlo con tres materiales reutilizables limpios (un rollo, una caja, un envase de plástico blando, papel). Anota qué era cada material antes y por qué lo elegiste por su forma. No uses vidrio, latas ni objetos filosos.",
        "Hice un pingüino. Usé un rollo de cartón para el cuerpo, un envase de plástico blando para la cabeza y cartulina para las alas. Elegí el rollo porque es largo y redondeado.",
        ["usa tres materiales reutilizables", "los elige por su forma", "los materiales están limpios y seguros", "explica qué era cada material"],
        ["obra", "lista de materiales con su uso original"],
        ["usar materiales peligrosos", "no explicar la elección"],
        "Reconoce la mejor elección por forma y pregunta qué otro material podría reutilizar.",
    ),
    "Revisa un objeto que vayas a botar en tu casa y di para qué otra cosa podría servir.",
    "Transforma el mismo material de dos maneras distintas y anota con qué forma parece más real.",
)


# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Materiales naturales que ya estén caídos: hojas secas, ramitas del suelo, piedras lisas medianas, corteza suelta. Cola fría, cartón como base, lápices y una bolsa para guardar lo recogido. Sal a recoger con un adulto.",
    "Aprenderé a usar materiales naturales en una obra sin dañar el entorno. Sirve para crear con la naturaleza y a la vez cuidarla.",
    ["Sé pegar materiales sobre cartón.", "Sé que reutilizar cuida el ambiente."],
    [
        "Los materiales naturales vienen de la naturaleza: hojas, ramitas, piedras, cortezas o semillas. Para usarlos sin dañar el entorno, hay reglas. Recoge solo lo que ya está caído en el suelo; nunca arranques plantas ni cortes ramas de un árbol vivo. Junta poco, solo lo que vas a usar. En parques y reservas naturales no se recoge nada: se observa y se dibuja.",
        "Antes de recoger, mira bien a tu alrededor. No toques hongos ni insectos que no conozcas, y no recojas flores. Lávate las manos después de trabajar con materiales de la tierra. Lo que sobra se devuelve al lugar donde estaba, o se deja en un lugar donde no estorbe. Así el lugar queda igual de bien que cuando llegaste.",
        "Para crear con ellos, observa su forma, color y textura: una hoja seca es delgada y crujiente, una piedra es lisa y pesada, una ramita es larga y áspera. Puedes pegarlas sobre cartón con cola fría, o ordenarlas formando una imagen sin pegarlas, como una obra que se fotografía y se deshace. Anota qué material usaste y de dónde lo sacaste.",
    ],
    [("material natural", "material que viene de la naturaleza, como una hoja o una piedra"), ("entorno", "lugar y seres vivos que nos rodean"), ("recoger", "tomar del suelo lo que ya está caído"), ("reserva natural", "lugar protegido donde no se debe recoger nada"), ("obra efímera", "obra que dura poco tiempo y luego se deshace")],
    [
        w("Recoger bien", "En una plaza ves una rama caída en el suelo y una flor viva en un arbusto. ¿Qué puedes recoger para tu obra?", ["Recojo solo lo que ya está caído.", "La rama caída se puede recoger.", "La flor viva no se corta."], "La rama caída"),
        w("Crear sin pegar", "Ordenas hojas secas en forma de sol sobre el pasto, las fotografías y luego las dejas en su lugar. ¿Qué tipo de obra hiciste?", ["No pegaste nada.", "La obra dura poco tiempo.", "Es una obra efímera y no deja marcas en el lugar."], "Una obra efímera"),
    ],
    [
        m("Arrancar hojas verdes del árbol de la plaza porque «hay muchas».", "Se daña el árbol, y si todos hacen lo mismo se queda sin hojas.", "Recoge solo hojas ya caídas y en poca cantidad."),
        m("Recoger piedras de una reserva natural porque se ven lindas.", "En las reservas no se debe sacar nada.", "Dibuja o fotografía lo que te guste y déjalo en su lugar."),
    ],
    [
        ex("¿Una hoja seca caída en el suelo es un material natural o un material reutilizable?", "Un material natural", "Viene de la naturaleza."),
        ex("¿Puedes arrancar una rama de un árbol vivo para tu obra?", "No", "La clase indica recoger solo lo que ya está caído."),
        ex("En una reserva natural, ¿se debe recoger algo o solo observar?", "Solo observar", "En las reservas no se recoge nada."),
    ],
    [
        ex("Haces una obra con hojas ordenadas en el pasto, las fotografías y las dejas en el lugar. ¿Es una obra que dura mucho o poco?", "Poco", "Es una obra efímera y se deshace."),
        ex("Una niña ve un hongo desconocido en el suelo. ¿Lo recoge o no lo toca?", "No lo toca", "La clase indica no tocar hongos desconocidos."),
        ex("Después de trabajar con tierra y hojas, ¿qué haces con tus manos?", "Las lavas", "Se lavan las manos después de trabajar con materiales de la tierra."),
    ],
    [
        ex("Quieres hacer los rayos de un sol con ramitas largas y delgadas. ¿Recoges ramitas del suelo o cortas ramas del árbol vivo?", "Ramitas del suelo", "Se recoge solo lo que ya cayó."),
        ex("Tienes diez hojas secas y vas a usar tres. ¿Qué haces con las siete que sobran?", "Las devuelves al lugar", "Lo que sobra se devuelve al lugar donde estaba."),
        ex("Ordena los pasos: A) pegar en el cartón, B) observar y recoger lo que ya cayó, C) lavar las manos. Escribe las tres letras en orden.", "B, A, C", "Primero recoges, luego pegas y al final te lavas las manos."),
    ],
    [
        ex("Un niño llevó una bolsa llena de piedras de una reserva natural. ¿Cumplió la regla de la clase?", "No", "En las reservas no se recoge nada."),
        ex("Dos niñas hacen un árbol: una pega hojas secas sobre cartón y la otra arranca hojas vivas del árbol de la plaza. ¿Cuál cuida el entorno?", "La que pega hojas secas", "Recoge lo que ya cayó y no daña al árbol."),
    ],
    [
        ex("Quieres que tu obra no deje ninguna marca en el lugar donde la haces. ¿Pegas las piedras con cola sobre cartón o las ordenas y las fotografías?", "Las ordenas y las fotografías", "Una obra efímera no deja marcas en el lugar."),
        ex("Quieres que tu obra con hojas se vea como un pájaro. Tienes hojas largas y estrechas y hojas redondas y anchas. ¿Qué hojas usas para las alas?", "Las largas y estrechas", "Se parecen a las plumas de un ala."),
    ],
    ex("En un paseo con el curso, la profesora dice que cada uno puede juntar tres cosas caídas para la obra. Tú ves una piña caída y una flor viva. ¿Qué eliges?", "La piña caída", "La flor viva no se corta y la piña ya cayó."),
    [
        ex("¿Qué es un material natural?", "Uno que viene de la naturaleza", "Por ejemplo, hojas, ramitas o piedras."),
        ex("Verdadero o falso: se puede arrancar plantas para hacer una obra.", "Falso", "Se debe recoger solo lo que ya está caído."),
        ex("¿Qué es una obra efímera?", "Una obra que dura poco y se deshace", "No deja marcas en el lugar."),
    ],
    task(
        "Elige UNA imagen: A) un animal hecho con hojas y ramitas caídas; B) un sol hecho con piedras lisas y hojas; C) un paisaje de montañas con cortezas. Recoge solo lo que ya cayó y en poca cantidad. Pégalo sobre cartón o ordénalo y fotografíalo. Escribe qué materiales usaste y cómo cuidaste el lugar.",
        "Hice un sol con piedras y ramitas largas para los rayos. Recogí solo lo que ya estaba en el suelo de la plaza. Lo fotografié y lo dejé en el mismo lugar.",
        ["recoge solo lo que ya cayó", "usa poca cantidad", "explica cómo cuidó el lugar", "elige los materiales por su forma"],
        ["obra o fotografía", "lista de materiales y cuidados"],
        ["arrancar plantas", "no devolver lo que sobra"],
        "Valora el cuidado del entorno y pregunta qué otro material natural podría usar.",
    ),
    "Camina por un lugar y di en voz alta tres materiales naturales que ya estén caídos y que podrías usar.",
    "Haz dos versiones de la misma obra, una pegada y otra efímera, y anota qué diferencia tienen.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Lápiz de mina, lápices de colores, témpera, pinceles grueso y fino, agua en un vaso de plástico, un trapo y una hoja gruesa.",
    "Aprenderé a controlar el lápiz y el pincel para lograr lo que quiero expresar. Sirve para dibujar y pintar con intención y no por casualidad.",
    ["Sé usar matiz y tono para expresar una idea.", "Sé hacer pruebas antes de la obra final."],
    [
        "Con el lápiz de mina puedes controlar la presión. Si presionas suave, la línea sale clara y fina; si presionas fuerte, sale oscura y gruesa. Los trazos suaves sirven para boceto y para lo lejano; los fuertes sirven para el contorno y para lo cercano. Con el mismo lápiz puedes hacer una gradación, que es pasar poco a poco de lo claro a lo oscuro.",
        "Con el pincel también se controla. El pincel grueso cubre rápido las superficies grandes. El pincel fino sirve para los detalles. La cantidad de agua cambia el resultado: con mucha agua la témpera se ve clara y transparente; con poca agua se ve intensa y cubre más. Además, hay que esperar a que una capa seque antes de pintar encima, para que los colores no se mezclen.",
        "Antes de pintar, elige la herramienta según lo que quieres lograr: «quiero un cielo suave» (pincel grueso, mucha agua), «quiero un ojo con detalles» (pincel fino, poca agua). Haz una prueba en un borde de la hoja. Lava el pincel entre un color y otro. Una buena decisión técnica es la que ayuda a mi intención.",
    ],
    [("presión", "fuerza con que apoyo el lápiz sobre la hoja"), ("gradación", "paso poco a poco de un tono claro a uno oscuro"), ("trazo", "marca que deja el lápiz o el pincel"), ("capa", "una pasada de pintura sobre la hoja"), ("detalle", "parte pequeña de una forma que se dibuja con cuidado")],
    [
        w("Elegir pincel y agua", "Quieres pintar un cielo suave y claro en una hoja grande. ¿Qué pincel y cuánta agua eliges?", ["El cielo es una superficie grande: pincel grueso.", "Quiero un color claro y transparente: mucha agua.", "Hago una prueba en un borde de la hoja."], "Pincel grueso y mucha agua"),
        w("Controlar la presión", "Quieres dibujar una montaña lejana que se vea suave y otra cercana con un contorno fuerte. ¿Cómo usas la presión?", ["La lejana va con presión suave: línea clara.", "La cercana va con presión fuerte: línea oscura.", "Así se nota cuál está más lejos."], "Presión suave para la lejana y fuerte para la cercana"),
    ],
    [
        m("Pintar sobre una capa mojada con otro color y que todo se mezcle.", "La pintura húmeda se corre y se ensucia.", "Espera a que seque antes de pintar encima."),
        m("Usar el pincel grueso para dibujar los ojos de un animal.", "El pincel grueso no permite detalles.", "Usa el pincel fino para los detalles."),
    ],
    [
        ex("Si presionas fuerte con el lápiz de mina, ¿la línea sale más oscura o más clara?", "Más oscura", "Más presión deja más grafito en la hoja."),
        ex("¿Cuál pincel sirve para cubrir una superficie grande: el grueso o el fino?", "El grueso", "El grueso cubre más rápido."),
        ex("Con mucha agua, la témpera se ve ¿más clara o más intensa?", "Más clara", "El agua la diluye."),
    ],
    [
        ex("Quieres pintar las pestañas de un animal. ¿Usas el pincel fino o el grueso?", "El fino", "Las pestañas son un detalle."),
        ex("Pasas de un gris muy claro a un gris muy oscuro poco a poco. ¿Qué hiciste: una gradación o una mancha?", "Una gradación", "Es el paso poco a poco de claro a oscuro."),
        ex("Pintas un color encima de otro que aún está húmedo y se mezclan. ¿Qué debiste hacer: esperar a que seque o usar más agua?", "Esperar a que seque", "La capa seca evita que se mezclen."),
    ],
    [
        ex("Quieres un cielo de atardecer intenso y que cubra bien. ¿Usas poca agua o mucha agua?", "Poca agua", "Con menos agua el color es intenso y cubre más."),
        ex("Quieres una línea de contorno que destaque un árbol en primer plano. ¿Presionas suave o fuerte?", "Fuerte", "La línea fuerte es oscura y marca el contorno."),
        ex("Ordena: A) pintar el cielo con pincel grueso, B) esperar que seque, C) pintar un detalle con pincel fino. Escribe las tres letras en orden.", "A, B, C", "Se pinta primero lo grande, se espera que seque y al final se hacen los detalles."),
    ],
    [
        ex("Una niña pintó un cielo con poca agua y se ve muy intenso. Ella quería un cielo suave y claro. ¿Qué cambia: agrega más agua o agrega más pintura?", "Agrega más agua", "Más agua hace el color más claro."),
        ex("Un niño dibujó con presión fuerte todo el boceto y no puede borrar. ¿Qué debió hacer: usar presión suave en el boceto o apretar más?", "Usar presión suave en el boceto", "El boceto suave se puede corregir."),
    ],
    [
        ex("Quieres una gradación de oscuro a claro para el cielo de un anochecer. ¿Comienzas arriba con un tono oscuro y bajas a uno claro, o al revés?", "Arriba oscuro y bajando a claro", "El cielo suele verse más oscuro arriba y más claro cerca del horizonte."),
        ex("Pintas un árbol con el pincel grueso y quieres agregar ramitas finas. ¿Usas el fino o el grueso?", "El fino", "Las ramitas finas requieren un pincel fino."),
    ],
    ex("Para la exposición del curso, tienes que pintar un paisaje con un cielo suave y una flor con muchos detalles. Tienes un pincel grueso y uno fino. ¿Qué usas para cada parte?", "Grueso para el cielo y fino para la flor", "Cada herramienta se elige según lo que se quiere lograr."),
    [
        ex("¿Cómo se hace una línea más clara con el lápiz de mina?", "Presionando suave", "Menos presión deja menos grafito."),
        ex("Verdadero o falso: hay que esperar a que una capa de pintura seque antes de pintar encima.", "Verdadero", "Así los colores no se mezclan."),
        ex("¿Qué pincel sirve para detalles?", "El fino", "El fino permite trazos pequeños."),
    ],
    task(
        "Elige UNA intención: A) un cielo suave de amanecer con una ave pequeña; B) un animal con mucho detalle en la cara; C) una montaña lejana y otra cercana. Haz una prueba de pincel o de presión en un borde de la hoja. Dibuja o pinta usando al menos dos controles técnicos (presión, pincel, agua o secado). Escribe cuáles usaste y para qué.",
        "Elegí la intención C. Dibujé la montaña lejana con presión suave y la cercana con presión fuerte. Pinté el cielo con pincel grueso y mucha agua. Usé pincel fino para el pico de la montaña cercana.",
        ["hace una prueba antes", "usa al menos dos controles técnicos", "relaciona la técnica con su intención", "espera el secado"],
        ["prueba", "obra", "frase con los controles usados"],
        ["pintar sobre capas húmedas", "usar siempre el mismo pincel"],
        "Reconoce el control técnico mejor logrado y pregunta qué cambiaría para lograr más detalle.",
    ),
    "Dibuja tres líneas con tu lápiz: una con presión suave, una media y una fuerte. Di cuál es la más oscura.",
    "Haz una gradación de cinco tonos con lápiz de mina y anota cómo cambió la presión.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA3, 6,
    "Cartón, papel, cola fría, tijera de punta redonda, cinta de papel, lápiz. Una cámara o un teléfono con permiso de un adulto para fotografiar el proceso, o una hoja para dibujar cada paso. Fotografía solo tu construcción, nunca a otras personas.",
    "Aprenderé a resolver un problema técnico en una construcción y a documentar los pasos. Sirve para repetir lo que funcionó y explicar mis decisiones.",
    ["Sé pegar, cortar y plegar papel y cartón.", "Sé elegir un material según su forma y su función."],
    [
        "Una solución técnica es una forma de lograr que una obra se sostenga, se pegue o se mueva como yo quiero. Por ejemplo, una torre de cartón puede caerse. Hay que descubrir por qué: ¿la base es angosta?, ¿falta pegamento? Cambiando una cosa a la vez, se descubre qué funciona. Eso se llama probar y corregir.",
        "Documentar es dejar un registro del proceso. Puedes sacar fotografías con una cámara, con permiso de un adulto, o hacer un dibujo rápido de cada paso. Para cada paso, escribe tres cosas: qué problema tuve, qué cambié y qué resultado tuvo. Un registro con tres pasos permite que otra persona repita tu solución sin preguntarte nada.",
        "Una construcción puede ser un objeto sencillo, como un soporte para un lápiz, una torre de cartón o un puente de papel que aguante un objeto liviano. Usa pliegues, bases anchas y uniones con cola fría. Una solución es buena si funciona, si usa pocos materiales y si se entiende cómo se hizo. Al final, cuéntale a otra persona cuál fue tu cambio más útil.",
    ],
    [("solución técnica", "forma de lograr que una obra se sostenga, se pegue o se mueva como quiero"), ("documentar", "dejar un registro de los pasos con fotos, dibujos o notas"), ("probar y corregir", "cambiar una cosa a la vez para descubrir qué funciona"), ("base", "parte de abajo que sostiene una construcción"), ("pliegue", "doblez del papel o cartón que le da firmeza")],
    [
        w("Mejorar una torre", "Una torre de cartón se cae. Su base es angosta. ¿Qué cambias primero?", ["Veo que la base es angosta.", "La hago más ancha con un cartón más grande.", "Pruebo otra vez y anoto qué pasó."], "Ensanchar la base"),
        w("Documentar un cambio", "Anotas: «Problema: el puente se hundía. Cambié: agregué dos pliegues. Resultado: aguantó una goma». ¿Qué tres datos tiene el registro?", ["Dice cuál fue el problema.", "Dice qué se cambió.", "Dice el resultado."], "Problema, cambio y resultado"),
    ],
    [
        m("Cambiar cinco cosas a la vez en la construcción.", "No se sabe cuál cambio fue el que funcionó.", "Cambia una sola cosa por vez y vuelve a probar."),
        m("No anotar nada y confiar en recordarlo.", "Se olvidan los cambios y no se puede repetir la solución.", "Anota o dibuja cada paso con problema, cambio y resultado."),
    ],
    [
        ex("Una torre de cartón se cae. ¿La base angosta es una causa posible?", "Sí", "Una base angosta no sostiene bien."),
        ex("Documentar es dejar un registro. ¿Un dibujo rápido de cada paso sirve como registro?", "Sí", "Los dibujos y las fotos sirven para registrar."),
        ex("Un pliegue en el cartón, ¿le da más firmeza o lo debilita?", "Le da más firmeza", "El doblez refuerza el material."),
    ],
    [
        ex("Un registro dice: «Problema: la torre se inclinaba. Cambié: la base es más ancha. Resultado: se quedó derecha». ¿Qué dato falta en esta descripción: el problema, el cambio o el resultado?", "Ninguno", "Están los tres."),
        ex("Cambias el pegamento y la base al mismo tiempo, y la torre se sostiene. ¿Sabes cuál cambio funcionó?", "No", "Cambiaste dos cosas a la vez."),
        ex("¿Qué dato anota un buen registro sobre un cambio: el resultado o el color del lápiz que usaste?", "El resultado", "El resultado dice si el cambio funcionó."),
    ],
    [
        ex("Un puente de papel se hunde cuando pones una goma sobre él. ¿Qué pruebas primero: agregar pliegues al papel o poner una goma más grande y pesada?", "Agregar pliegues al papel", "Los pliegues dan firmeza; una goma más pesada lo hundiría más."),
        ex("Tu soporte de lápices se cae hacia un lado. ¿Qué parte revisas: la base o el color?", "La base", "Una base mal apoyada hace que se incline."),
        ex("Ordena el registro: A) escribir el resultado, B) escribir el problema, C) escribir el cambio. Escribe las tres letras en orden.", "B, C, A", "Primero el problema, luego el cambio y al final el resultado."),
    ],
    [
        ex("Julia dice: «Mi solución funcionó, pero no sé por qué porque no anoté nada». ¿Qué falta para poder repetirla?", "Un registro de los pasos", "Sin registro, no se puede repetir."),
        ex("Un niño probó una base ancha y la torre se cayó igual. ¿Debe dejar de probar o cambiar otra cosa?", "Cambiar otra cosa", "Se prueba y se corrige con otro cambio."),
    ],
    [
        ex("Quieres que un puente de papel aguante una goma. Pruebas con una hoja lisa, con la hoja doblada una vez y con la hoja doblada en acordeón. ¿Cuál probablemente aguanta más?", "La hoja doblada en acordeón", "Los pliegues repetidos dan más firmeza."),
        ex("Un amigo quiere repetir tu solución. ¿Le entregas tu registro de tres pasos o le dices «hazlo como pueda»?", "Tu registro de tres pasos", "El registro permite repetir la solución."),
    ],
    ex("En clase, tu grupo construye un soporte para lápices con cartón. Se cae hacia adelante. Una compañera dice que cambien todo. Tú propones algo mejor. ¿Qué propones: cambiar una sola cosa, por ejemplo la base, y anotar qué pasa?", "Cambiar una sola cosa y anotar qué pasa", "Así se descubre qué cambio funciona."),
    [
        ex("¿Qué es una solución técnica?", "Una forma de lograr que la obra se sostenga o funcione", "Se descubre probando y corrigiendo."),
        ex("Verdadero o falso: un buen registro anota problema, cambio y resultado.", "Verdadero", "Así se puede repetir la solución."),
        ex("¿Cuántos cambios haces por vez al probar?", "Uno", "Así se sabe cuál funciona."),
    ],
    task(
        "Elige UNA construcción: A) una torre de cartón que se mantenga de pie; B) un puente de papel que aguante una goma; C) un soporte para lápices. Haz una primera versión, descubre un problema, cambia UNA cosa y prueba otra vez. Documenta tres pasos con fotos (si un adulto te deja usar una cámara) o con dibujos. Para cada paso escribe problema, cambio y resultado.",
        "Hice un puente de papel. Paso 1: se hundió. Cambié: doblé el papel en acordeón. Resultado: aguantó una goma. Paso 2: se movía de lado. Cambié: pegué los extremos con cola. Resultado: se movió menos. Paso 3: aún se movía un poco. Cambié: puse cinta de papel en los bordes. Resultado: quedó firme.",
        ["resuelve un problema técnico", "cambia una sola cosa por vez", "documenta tres pasos", "escribe problema, cambio y resultado"],
        ["construcción", "registro de tres pasos con fotos o dibujos"],
        ["cambiar muchas cosas a la vez", "no registrar los pasos"],
        "Valora el cambio mejor justificado y pregunta cómo explicaría la solución a una persona que no vio el proceso.",
    ),
    "Cuéntale a una persona de tu casa qué problema tuvo tu construcción y qué cambiaste.",
    "Repite la construcción con otro material y compara qué solución necesitó.",
)

# ================================================================ OA 04
# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Una hoja y un lápiz para anotar. Las obras de este cuaderno están descritas con palabras (son descripciones escritas para practicar, no obras reales). Si puedes, mira una obra real o un objeto de artesanía, como una greda o un tejido, con una persona adulta.",
    "Aprenderé a describir lo que veo en una obra de arte o en un objeto, usando el lenguaje visual, antes de decir qué me parece. Sirve para mirar con atención y no confundir lo que veo con lo que opino.",
    ["Sé nombrar líneas, colores, formas y texturas.", "Sé separar una observación de una opinión."],
    [
        "Describir una obra es decir qué se ve en ella, sin juzgar todavía. Para hacerlo, usamos el lenguaje visual: las líneas (rectas, curvas, quebradas), los colores (cálidos, fríos, claros, oscuros), las formas (figurativas o no figurativas), las texturas (lisas, ásperas) y cómo está ordenado todo en la hoja o en el espacio. Esto sirve para obras de arte, y también para objetos de artesanía, como una vasija de greda o un tejido.",
        "Una descripción dice qué hay y dónde. Por ejemplo: «En la pintura hay un cielo naranja, olas con líneas largas azules y dos personas pequeñas sentadas a la derecha». Una interpretación dice qué significa o qué siento: «es una obra triste». Hoy solo describimos. La interpretación viene después, cuando ya miramos bien y tenemos datos en que apoyarnos.",
        "Para describir con orden, mira primero la obra completa, luego las partes grandes y al final los detalles pequeños. Anota cuántas cosas hay, de qué colores y dónde están. Cada año se recomienda observar al menos 15 obras y objetos de arte y artesanía local y chilena, 15 de arte latinoamericano y 15 de arte universal. En este cuaderno solo practicamos con descripciones escritas inventadas: pide a tu profesor o profesora que te muestre obras reales de esos tres grupos.",
    ],
    [("describir", "decir qué se ve, sin juzgar todavía"), ("lenguaje visual", "conjunto de elementos con que se hace una imagen: línea, color, forma, textura y orden"), ("interpretar", "decir qué significa una obra o qué siento al verla"), ("artesanía", "objetos hechos a mano con materiales y técnicas de una tradición, como la greda o el tejido"), ("detalle", "parte pequeña de una obra que casi no se nota")],
    [
        w("Describir sin interpretar", "Obra descrita: «Un cielo naranja, olas de líneas largas azules y dos personas pequeñas sentadas a la derecha». Escribe una descripción en una frase con color y posición.", ["Busco colores: naranja y azul.", "Busco posición: las personas están a la derecha.", "Armo la frase sin decir si es triste o alegre."], "«Hay un cielo naranja, olas azules y dos personas pequeñas a la derecha»"),
        w("Distinguir descripción e interpretación", "Dos frases sobre una vasija: A) «La vasija tiene líneas en zigzag y es de color café rojizo». B) «La vasija es muy antigua y misteriosa». ¿Cuál describe?", ["La frase A habla de líneas y color, que se ven.", "La frase B dice lo que pienso o siento: es interpretación.", "Solo A describe."], "La frase A"),
    ],
    [
        m("Decir «es triste» cuando me piden describir.", "Esa frase es una interpretación y no dice qué se ve.", "Primero nombra colores, líneas, formas y su ubicación."),
        m("Nombrar solo un detalle y quedarse ahí.", "Se pierde la información del conjunto.", "Mira primero la obra completa, luego las partes grandes y al final los detalles."),
    ],
    [
        ex("Describir es decir qué se ve. ¿«Es una obra triste» describe o interpreta?", "Interpreta", "Dice un sentimiento y no un hecho visible."),
        ex("Obra descrita: «Un jarro de greda con líneas rectas negras sobre un fondo rojizo». ¿Qué color tiene el fondo?", "Rojizo", "La descripción dice que el fondo es rojizo."),
        ex("¿Una vasija de greda hecha a mano es una obra de artesanía o un edificio?", "Una obra de artesanía", "Los objetos hechos a mano con una tradición son artesanía."),
    ],
    [
        ex("Obra descrita: «Tres círculos amarillos arriba y una línea ondulada azul abajo». ¿Cuántos círculos hay?", "Tres", "La descripción nombra tres círculos amarillos."),
        ex("¿Cuál frase usa lenguaje visual? A: «Me da pena». B: «Hay líneas quebradas negras en el centro».", "B", "La frase B nombra líneas y color."),
        ex("Describir una obra con orden: ¿miras primero los detalles pequeños o la obra completa?", "La obra completa", "La clase indica empezar por el conjunto."),
    ],
    [
        ex("Obra descrita: «Un tejido con rombos rojos en el centro y rayas azules a los lados». ¿Dónde están las rayas azules: en el centro o a los lados?", "A los lados", "La descripción ubica las rayas a los lados."),
        ex("Describes una pintura: «Un cerro café de forma triangular y, a su izquierda, un árbol verde pequeño». ¿Qué forma tiene el cerro?", "Triangular", "La frase dice que es triangular."),
        ex("Ordena el modo de describir: A) los detalles pequeños, B) la obra completa, C) las partes grandes. Escribe las tres letras en orden.", "B, C, A", "Primero el conjunto, luego las partes grandes y al final los detalles."),
    ],
    [
        ex("Dos compañeros miran la misma obra. Uno dice «Es hermosa» y la otra dice «Tiene un cielo amarillo y dos casas rojas». ¿Quién entregó más información visible?", "La otra", "Ella nombra colores y objetos que se ven."),
        ex("Una niña describe: «El jarro tiene un asa a la izquierda y mucha pintura brillante». Otro niño dice: «Eso es una opinión». ¿Tiene razón?", "No", "Asa a la izquierda y pintura brillante son datos visibles."),
    ],
    [
        ex("Obra descrita: «Un mural muy grande con muchas personas de colores cálidos en el fondo y una persona de azul en el primer plano». ¿Cuál tiene colores fríos: las personas del fondo o la del primer plano?", "La del primer plano", "La persona de azul tiene color frío; las del fondo son cálidas."),
        arith("Obra descrita: «Un tejido con 4 rombos rojos y 3 rombos azules». ¿Cuántos rombos hay en total?", "4+3", "Se suman los rombos rojos y los azules."),
    ],
    ex("Visitas un museo con tu curso y te piden anotar una descripción de una vasija de greda sin decir si te gusta. ¿Qué escribes: «Tiene el cuello angosto y líneas negras en zigzag» o «Me parece fea»?", "«Tiene el cuello angosto y líneas negras en zigzag»", "Es una descripción con datos visibles."),
    [
        ex("¿Qué es describir una obra?", "Decir qué se ve sin juzgar", "Se usan datos visibles."),
        ex("Verdadero o falso: «es misteriosa» es una descripción.", "Falso", "Es una interpretación."),
        ex("¿Qué elementos del lenguaje visual puedes nombrar? Escribe dos.", "Línea, color, forma o textura", "Son elementos del lenguaje visual."),
    ],
    task(
        "Elige UNA descripción: A) «Un cielo naranja, olas de líneas largas azules y dos personas pequeñas sentadas a la derecha». B) «Un jarro de greda con líneas negras rectas sobre un fondo rojizo». C) Un objeto de arte o de artesanía que veas en tu casa (una greda, un tejido o un cuadro). Escribe una descripción con cinco datos visibles (colores, líneas, formas, textura o ubicación), sin decir si te gusta.",
        "Elegí la descripción B. Escribí: «El jarro es de greda. Tiene líneas negras rectas. El fondo es rojizo. El cuello es angosto. El borde es liso».",
        ["escribe cinco datos visibles", "usa lenguaje visual", "no mezcla opinión", "ordena de lo general a lo particular"],
        ["lista de cinco datos"],
        ["decir solo que le gusta o no", "olvidar la ubicación"],
        "Destaca el dato más preciso y pregunta qué otro detalle podría haber observado.",
    ),
    "Mira un objeto decorado de tu casa y di tres datos visibles sin decir si te gusta.",
    "Describe la misma obra en dos momentos distintos y anota qué nuevos datos encontraste.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Una hoja y un lápiz. Las obras de esta clase están descritas con palabras en el cuaderno; son descripciones inventadas para practicar, no obras reales.",
    "Aprenderé a relacionar lo que veo (líneas, colores, formas) con lo que siento al mirar una obra. Sirve para explicar mis emociones con datos y no solo decir «me gusta».",
    ["Sé describir una obra con datos visibles.", "Sé que los colores cálidos y fríos dan sensaciones distintas."],
    [
        "Cuando miramos una obra, sentimos algo: calma, alegría, miedo, sorpresa o tristeza. Esa sensación viene de lo que se ve. Un color, una línea o una forma pueden causar una emoción. Por ejemplo, las líneas largas y suaves suelen dar calma; las líneas quebradas pueden dar tensión. Los colores cálidos pueden dar energía, y los fríos, frescura o tristeza.",
        "Para relacionar lo que veo con lo que siento, uso una frase con dos partes: «Siento (emoción) porque veo (dato visible)». Por ejemplo: «Siento calma porque veo líneas largas y colores claros». Así, mi emoción se apoya en algo concreto de la obra. Si solo digo «siento calma», nadie sabe por qué.",
        "Dos personas pueden sentir cosas distintas ante la misma obra, y las dos pueden tener razón si explican qué ven. Los colores no significan lo mismo para todos. Lo importante es poder mostrar el dato que me hizo sentir eso. También puedes comparar tu emoción con lo que quizás quiso expresar la persona que hizo la obra, pero eso es una idea, no una certeza.",
    ],
    [("emoción", "lo que siento, como alegría, calma o miedo"), ("sensación", "lo que una obra me hace sentir al mirarla"), ("dato visible", "algo que se ve en la obra y se puede mostrar"), ("tensión", "sensación de inquietud o de algo a punto de pasar"), ("expresar", "mostrar lo que se piensa o se siente")],
    [
        w("Armar la frase", "Una pintura tiene líneas largas y suaves y colores claros. Sientes calma. Escribe tu frase.", ["Elijo la emoción: calma.", "Elijo el dato visible: líneas largas y suaves y colores claros.", "Uno con «porque»."], "«Siento calma porque veo líneas largas y suaves y colores claros»"),
        w("Mismo cuadro, dos emociones", "Una niña dice «Siento miedo porque el cielo es muy oscuro». Un niño dice «Siento calma porque hay una luz amarilla pequeña». ¿Tienen razón los dos?", ["Los dos nombran un dato que se ve.", "Cada uno apoya su emoción con algo concreto.", "Los dos pueden tener razón."], "Sí, porque cada uno explica con un dato visible"),
    ],
    [
        m("Decir solo «me siento feliz» sin nombrar qué se ve.", "No se sabe qué de la obra me hizo sentir eso.", "Agrega «porque veo...» y nombra un dato."),
        m("Pensar que todas las personas deben sentir lo mismo.", "Las emociones dependen de cada persona.", "Acepta otras respuestas si se apoyan en lo que se ve."),
    ],
    [
        ex("En la frase «Siento calma porque veo líneas largas y suaves», ¿cuál es el dato visible: calma o líneas largas y suaves?", "Líneas largas y suaves", "Es lo que se ve en la obra."),
        ex("Las líneas quebradas pueden dar tensión. ¿Las líneas largas y suaves suelen dar tensión o calma?", "Calma", "Así lo indica la clase."),
        ex("¿La frase «Siento calma» explica por qué se siente calma?", "No", "Falta decir qué dato visible la causó."),
    ],
    [
        ex("Obra descrita: «Un cielo oscuro con rayos amarillos quebrados». ¿Qué emoción puede producir con más facilidad: tensión o calma?", "Tensión", "Los rayos quebrados y el cielo oscuro dan inquietud."),
        ex("Escribes: «Siento alegría porque veo muchos colores vivos y un sol grande». ¿Qué parte es el dato visible?", "Muchos colores vivos y un sol grande", "Es lo que se ve."),
        ex("Obra descrita: «Un lago azul claro, sin olas, con líneas horizontales largas». ¿Qué línea predomina: horizontal o quebrada?", "Horizontal", "La descripción dice que las líneas largas son horizontales."),
    ],
    [
        ex("Obra descrita: «Un bosque con árboles muy oscuros y una luz pequeña al fondo». Quieres decir que sientes misterio. ¿Qué dato usas en tu frase «porque veo...»?", "Árboles muy oscuros y una luz pequeña al fondo", "Es lo que provoca la sensación de misterio."),
        ex("Quieres decir «Siento calma porque veo ___». ¿Qué dato visible completa mejor la frase según la clase: A) líneas largas horizontales y colores celestes; B) rayos amarillos quebrados en un cielo oscuro?", "A", "Las líneas largas y los colores suaves dan calma; las líneas quebradas dan tensión."),
        ex("Ordena la frase: A) porque veo líneas suaves, B) siento calma. Escribe las letras en el orden correcto.", "B, A", "Primero la emoción y luego el dato visible."),
    ],
    [
        ex("Mariana dice «Siento miedo porque el cielo es oscuro». Pedro dice «Siento calma porque es oscuro y tranquilo, como la noche». ¿Los dos usan un dato visible?", "Sí", "Los dos usan el color oscuro como dato."),
        ex("Un niño dice «Esa obra da alegría a todos». ¿Puede saber lo que sienten todos?", "No", "Cada persona siente distinto."),
    ],
    [
        ex("Obra descrita: «Una persona pequeña en una playa enorme y vacía». Alguien siente soledad. ¿Qué dato visible apoya mejor la emoción: la playa vacía o el color de la arena?", "La playa vacía", "El espacio vacío da sensación de soledad."),
        ex("Obra descrita: «Colores rojos y naranjas, líneas en zigzag que suben». Alguien siente energía. ¿Qué dato visible apoya esa emoción? Elige: líneas en zigzag que suben o el marco, que no se describe.", "Líneas en zigzag que suben", "El movimiento y los colores cálidos dan energía."),
    ],
    ex("En el museo, tu profesora te pregunta qué sientes ante un cuadro con muchas líneas curvas azules y celestes. ¿Qué respuesta explica mejor: «Siento calma porque veo líneas curvas azules y celestes» o «Siento calma porque sí»?", "«Siento calma porque veo líneas curvas azules y celestes»", "Apoya la emoción en datos visibles."),
    [
        ex("¿Qué dos partes tiene la frase para relacionar lo que veo con lo que siento?", "La emoción y el dato visible", "Siento (emoción) porque veo (dato)."),
        ex("Verdadero o falso: dos personas pueden sentir cosas distintas ante la misma obra.", "Verdadero", "Las emociones dependen de cada persona."),
        ex("¿Qué línea suele dar tensión: la quebrada o la larga y suave?", "La quebrada", "Los cambios bruscos dan inquietud."),
    ],
    task(
        "Elige UNA descripción: A) «Un cielo muy oscuro con un rayo amarillo quebrado sobre un mar de olas grandes». B) «Un lago celeste con líneas largas y horizontales y una luz amarilla pequeña». C) una obra o un objeto decorado de tu casa. Escribe dos frases: «Siento ___ porque veo ___» con datos distintos. Luego escribe una emoción distinta que otra persona podría sentir y el dato en que se apoyaría.",
        "Elegí B. «Siento calma porque veo líneas largas y horizontales. Siento esperanza porque veo una luz amarilla pequeña». Otra persona podría sentir soledad porque el lago es muy grande y hay una sola luz.",
        ["escribe dos frases con emoción y dato", "los datos son visibles", "imagina otra emoción posible", "apoya cada emoción con un dato"],
        ["dos frases", "una emoción alternativa"],
        ["decir solo la emoción", "pensar que todos sienten igual"],
        "Reconoce la frase mejor apoyada en datos y pregunta qué dato cambiaría la emoción.",
    ),
    "Mira un objeto de tu casa y di una frase «Siento ___ porque veo ___».",
    "Pide a una persona de tu casa que mire lo mismo y compare su emoción con la tuya.",
)


# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Una hoja y un lápiz. Las obras de esta clase están descritas con palabras y son inventadas para practicar, no obras reales; no necesitas buscarlas.",
    "Aprenderé a defender una idea sobre una obra con detalles que se pueden señalar. Sirve para explicar mi opinión de manera que otros la entiendan y la puedan comprobar.",
    ["Sé describir una obra con datos visibles.", "Sé decir «siento ___ porque veo ___»."],
    [
        "Una idea sobre una obra es lo que pienso de ella: qué muestra, qué quiere expresar o qué me recuerda. Para que sea una buena idea, debe estar fundamentada, es decir, apoyada en detalles de la obra. Un detalle es un dato que puedo señalar con el dedo. Si digo «creo que la obra habla de la soledad», necesito mostrar qué detalle me hace pensar eso.",
        "Una forma simple de fundamentar es: «Pienso que ___ porque veo ___ y también ___». Con dos detalles, la idea es más fuerte que con uno solo. Por ejemplo: «Pienso que la pintura habla de la soledad porque veo una sola persona pequeña y un espacio muy grande y vacío». Un detalle apoya la idea si realmente tiene relación con ella. No sirve nombrar un detalle que no tiene relación, como el color del marco.",
        "Una idea también puede cambiar cuando veo más detalles. Si noto algo que contradice mi idea, puedo corregirla. Eso no es un error; es parte de mirar con atención. Cuando hables de una obra de artesanía local o de arte latinoamericano, usa el mismo método: dato visible, idea y relación entre los dos. Si no estás seguro de lo que quiso decir quien la hizo, dilo: «creo que», no «seguro que».",
    ],
    [("idea", "lo que pienso de una obra"), ("fundamentar", "apoyar una idea con detalles de la obra"), ("detalle", "dato de la obra que puedo señalar"), ("relación", "conexión clara entre un detalle y una idea"), ("contradecir", "mostrar que algo no coincide con lo que pienso")],
    [
        w("Fundamentar con dos detalles", "Obra descrita: «Una sola persona pequeña en una playa enorme y vacía, bajo un cielo gris». Escribe una idea con dos detalles.", ["Elijo una idea: la obra habla de la soledad.", "Busco dos detalles: una sola persona pequeña y un espacio enorme y vacío.", "Uno con «porque veo»."], "«Pienso que habla de la soledad porque veo una sola persona pequeña y una playa enorme y vacía»"),
        w("Elegir un detalle que sí apoya", "Idea: «La obra muestra alegría». Detalles posibles: A) colores vivos y un sol grande; B) el marco es de madera. ¿Cuál apoya la idea?", ["El marco no dice nada sobre lo que se pinta.", "Los colores vivos y el sol grande se relacionan con alegría.", "Elijo A."], "El detalle A"),
    ],
    [
        m("Dar una idea sin ningún detalle: «La obra habla de la tristeza».", "No se puede comprobar lo que se dice.", "Agrega «porque veo...» y nombra al menos un detalle."),
        m("Nombrar detalles que no tienen relación con la idea.", "El detalle no apoya lo que pienso.", "Elige detalles de colores, líneas, formas o ubicación que se relacionen con tu idea."),
    ],
    [
        ex("Fundamentar una idea es apoyarla con detalles. ¿Un detalle es algo que puedo señalar en la obra o algo que imagino?", "Algo que puedo señalar en la obra", "Los detalles son datos visibles."),
        ex("En «Pienso que habla de la soledad porque veo una sola persona pequeña», ¿cuál es el detalle?", "Una sola persona pequeña", "Es lo que se ve en la obra."),
        ex("¿Una idea con dos detalles es más fuerte o más débil que una con uno solo?", "Más fuerte", "Más datos la apoyan mejor."),
    ],
    [
        ex("Obra descrita: «Un cielo oscuro y un barco pequeño entre olas enormes». Idea: «Habla del peligro». ¿Qué detalle apoya esa idea: las olas enormes o el nombre del autor?", "Las olas enormes", "Las olas enormes dan idea de peligro."),
        ex("Idea: «La obra muestra calma». ¿Cuál detalle la apoya: líneas largas y colores claros o rayos quebrados?", "Líneas largas y colores claros", "Esos datos se relacionan con tranquilidad."),
        ex("Obra descrita: «Un jarro de greda con líneas negras en zigzag que giran alrededor». Idea: «Hay movimiento». ¿Qué detalle apoya la idea?", "Las líneas en zigzag que giran", "Las líneas que giran dan sensación de movimiento."),
    ],
    [
        ex("Obra descrita: «Un mural con muchas personas trabajando juntas en el campo». Escribes: «Pienso que habla del trabajo en comunidad porque veo ___». Completa con el mejor detalle.", "Muchas personas trabajando juntas", "Es el dato que se relaciona con la idea."),
        ex("Obra descrita: «Dos personas pequeñas frente a una montaña inmensa». Idea: «Muestra lo grande que es la naturaleza». ¿Qué detalle sirve: el tamaño de la montaña comparado con las personas o el color de la ropa?", "El tamaño de la montaña comparado con las personas", "Esa comparación apoya la idea de grandeza."),
        ex("Ordena la frase: A) porque veo una persona pequeña y un espacio vacío, B) pienso que habla de la soledad. Escribe las letras en orden.", "B, A", "Primero va la idea y luego los detalles."),
    ],
    [
        ex("Ana dice: «Pienso que la obra habla de la amistad porque el marco es dorado». ¿Su detalle apoya su idea?", "No", "El marco no se relaciona con la amistad."),
        ex("Luis ve una obra con una persona pequeña en un espacio vacío y dice «habla de la soledad». Después nota que hay una segunda persona escondida al fondo. ¿Qué puede hacer: corregir su idea o ignorar el detalle?", "Corregir su idea", "Un detalle nuevo puede cambiar lo que pensamos."),
    ],
    [
        ex("Obra descrita: «Un tejido con rombos rojos en el centro y rayas azules en los bordes». Quieres defender la idea «el centro es lo que más llama la atención». ¿Qué detalle usas?", "Los rombos rojos están en el centro", "El color rojo y la posición central hacen que se note primero."),
        ex("No estás seguro de lo que quiso expresar quien hizo una obra. ¿Dices «creo que» o «seguro que»?", "Creo que", "Si no estás seguro, hay que decir que es una idea."),
    ],
    ex("En un museo, un amigo dice que un cuadro con colores oscuros y una persona pequeña habla del miedo. Tú quieres apoyarlo. ¿Qué agregas: «porque veo colores oscuros y una persona pequeña» o «porque me gusta»?", "«porque veo colores oscuros y una persona pequeña»", "Nombra detalles que se pueden señalar."),
    [
        ex("¿Qué significa fundamentar una idea?", "Apoyarla con detalles de la obra", "Los detalles permiten comprobarla."),
        ex("Verdadero o falso: puedo cambiar mi idea si veo un detalle nuevo.", "Verdadero", "Mirar con atención puede cambiar lo que pensamos."),
        ex("¿Cuántos detalles conviene usar para apoyar una idea?", "Al menos dos", "Con dos detalles la idea es más fuerte."),
    ],
    task(
        "Elige UNA descripción: A) «Una persona pequeña en una playa enorme y vacía bajo un cielo gris». B) «Un mural con muchas personas trabajando juntas en el campo, con colores cálidos». C) una obra o un objeto decorado de tu casa. Escribe una idea fundamentada con al menos dos detalles: «Pienso que ___ porque veo ___ y ___». Escribe otro detalle que podría cambiar tu idea.",
        "Elegí A. «Pienso que la obra habla de la soledad porque veo una persona pequeña y una playa enorme y vacía». Si apareciera otra persona al fondo, mi idea podría cambiar.",
        ["la idea se relaciona con los detalles", "usa al menos dos detalles visibles", "dice qué detalle cambiaría su idea", "usa «creo que» si no está seguro"],
        ["una frase fundamentada", "un detalle que cambiaría la idea"],
        ["dar una idea sin detalles", "usar detalles que no se relacionan"],
        "Valora la relación entre idea y detalles y pregunta qué otro detalle la fortalecería.",
    ),
    "Mira un objeto de tu casa y di una idea sobre él con dos detalles.",
    "Escribe tres ideas distintas para la misma obra y fundamenta cada una con detalles distintos.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Una hoja y un lápiz. Las obras de esta clase están descritas con palabras en el cuaderno; son descripciones inventadas para practicar, no obras reales.",
    "Aprenderé a comparar respuestas de personas distintas ante una misma obra y a comparar obras de lugares distintos. Sirve para entender que el arte se puede mirar de muchas maneras.",
    ["Sé describir una obra con datos visibles.", "Sé fundamentar una idea con detalles."],
    [
        "Cada persona mira una obra con su propia experiencia. Por eso, dos respuestas pueden ser distintas y las dos pueden ser buenas, si cada una se apoya en detalles visibles. Para comparar respuestas, escribe qué detalle usa cada persona y qué idea saca. Una respuesta es más sólida cuando los detalles se pueden señalar en la obra.",
        "También se pueden comparar obras. En un año se recomienda ver arte de tres lugares: local y chileno (como la greda de Pomaire o los tejidos), latinoamericano (como el muralismo mexicano) y universal (de otras partes del mundo). Para comparar dos obras, mira qué tienen igual y qué tienen distinto en color, línea, forma, textura y tema. Una comparación completa dice «las dos tienen... pero se diferencian en...».",
        "Comparar no es decidir cuál es mejor. Es descubrir qué hace especial a cada obra. Escucha las respuestas de otras personas con respeto: pueden mostrarte detalles que tú no viste. Si una respuesta te hace cambiar de idea, díselo. Así se aprende más del arte.",
    ],
    [("comparar", "buscar qué tienen igual y qué tienen distinto dos cosas"), ("respuesta", "lo que una persona dice o siente al mirar una obra"), ("semejanza", "algo que dos cosas tienen igual"), ("diferencia", "algo que dos cosas tienen distinto"), ("sólida", "bien apoyada en datos que se pueden comprobar")],
    [
        w("Comparar dos respuestas", "Obra descrita: «Un cielo oscuro con una luz amarilla pequeña». Ana: «Siento miedo porque el cielo es oscuro». Beto: «Siento esperanza porque hay una luz». ¿En qué se diferencian?", ["Cada uno nombra un detalle distinto: Ana, el cielo oscuro; Beto, la luz.", "Las emociones son distintas: miedo y esperanza.", "Las dos se apoyan en datos visibles."], "Usan detalles y emociones distintos, y las dos se apoyan en datos"),
        w("Comparar dos obras", "Obra A: un jarro de greda con líneas negras sobre fondo rojizo. Obra B: un mural muy grande con muchas personas en colores cálidos. ¿Qué tienen igual y qué distinto?", ["Igual: las dos usan colores cálidos.", "Distinto: el jarro es pequeño y el mural, muy grande.", "También cambia el tipo de obra: objeto de artesanía y pintura sobre un muro."], "Igual: colores cálidos. Distinto: tamaño y tipo de obra"),
    ],
    [
        m("Decir que una respuesta es mala porque es distinta a la mía.", "Las personas ven cosas distintas y las dos pueden tener razón.", "Revisa si la respuesta se apoya en datos visibles."),
        m("Comparar dos obras y decidir solo cuál es la más linda.", "Eso es una opinión y no compara.", "Busca semejanzas y diferencias en color, línea, forma, textura o tema."),
    ],
    [
        ex("Comparar es buscar qué tienen igual y qué tienen distinto. ¿Dos jarros de greda, uno con líneas rectas y otro con zigzag, se diferencian en el color o en el tipo de línea?", "En el tipo de línea", "Uno tiene líneas rectas y el otro, zigzag."),
        ex("¿Dos personas pueden dar respuestas distintas sobre una obra y estar las dos bien apoyadas?", "Sí", "Si cada una usa datos visibles."),
        ex("En un año se recomienda ver arte de tres lugares: local y chileno, latinoamericano y universal. ¿Cuántos grupos son?", "Tres", "Local y chileno, latinoamericano y universal."),
    ],
    [
        ex("Obra A: un tejido con rombos rojos y azules. Obra B: un cuadro con rombos rojos y azules. ¿Qué tienen igual: los colores o el tamaño?", "Los colores", "Las dos tienen rombos rojos y azules."),
        ex("Obra descrita: «Una luz amarilla pequeña en un cielo oscuro». Ana siente miedo por lo oscuro. Beto siente esperanza por la luz. ¿Alguno usó un dato que no está en la obra?", "No", "Los dos usaron datos que están en la obra."),
        ex("¿Comparar obras significa decidir cuál es la mejor?", "No", "Es descubrir qué hace especial a cada una."),
    ],
    [
        ex("Obra A: una vasija pequeña con zigzags negros. Obra B: un mural gigante con personas. Para compararlas, ¿qué diferencia de tamaño notas: la vasija es pequeña y el mural gigante, o al revés?", "La vasija es pequeña y el mural gigante", "Es lo que dicen las descripciones."),
        ex("Dos niños miran un cuadro con colores muy vivos. Uno dice «Siento alegría porque hay muchos colores vivos» y otro dice «Siento cansancio porque hay demasiados colores». ¿Cuál frase usa un dato visible de la obra?", "Las dos", "Las dos se apoyan en los muchos colores vivos."),
        ex("Obra A: un jarro de greda con triángulos negros. Obra B: una pintura sobre papel con triángulos negros. Completa: «Las dos tienen triángulos negros, pero se diferencian en ___». Elige: que la A es un objeto con volumen y la B es plana, o que las dos tienen triángulos.", "Que la A es un objeto con volumen y la B es plana", "Es una diferencia real: lo que tienen igual es lo de los triángulos."),
    ],
    [
        ex("Un compañero dice: «Mi respuesta es la única correcta». Otra dice: «Veo que él notó la luz que yo no vi». ¿Quién escucha mejor a los demás?", "La otra", "Ella reconoce un dato nuevo."),
        ex("Tomás compara dos obras diciendo solo «la A es más linda». ¿Está comparando con semejanzas y diferencias?", "No", "Solo dio una opinión."),
    ],
    [
        ex("Obra A: un cuadro con muchas líneas curvas azules. Obra B: otro cuadro con muchas líneas curvas azules y una persona al centro. ¿Cuántas diferencias principales hay entre ellas, según las descripciones?", "Una", "La diferencia es la persona al centro."),
        ex("Una persona cambió su respuesta después de escuchar a otra y notó un detalle nuevo. ¿Es un error o una buena práctica?", "Una buena práctica", "Escuchar puede ayudar a ver más."),
    ],
    ex("En un museo, tu grupo debe comparar una vasija de greda con una pintura de un mural. Una compañera dice «la vasija es más linda». Tú propones otra cosa. ¿Qué propones: buscar dos semejanzas y dos diferencias o votar cuál gusta más?", "Buscar dos semejanzas y dos diferencias", "Así se compara con datos."),
    [
        ex("¿Qué se compara en dos obras?", "Qué tienen igual y qué tienen distinto", "Son semejanzas y diferencias."),
        ex("Verdadero o falso: dos respuestas distintas pueden ser buenas.", "Verdadero", "Si se apoyan en datos visibles."),
        ex("¿Qué puedes hacer si otra persona nota un detalle que tú no viste?", "Escucharla y revisar si cambia tu idea", "Así se aprende más."),
    ],
    task(
        "Usa estas dos descripciones. Obra A: «Un jarro de greda con líneas negras en zigzag sobre un fondo rojizo». Obra B: «Un mural con muchas personas trabajando juntas, en colores cálidos». Escribe dos semejanzas y dos diferencias. Después escribe una respuesta con emoción y detalle para cada obra. Puedes comparar con una obra que veas en tu casa.",
        "Semejanzas: las dos tienen colores cálidos; las dos son hechas por personas. Diferencias: el jarro es pequeño y el mural, grande; uno es un objeto y el otro, una pintura. Sobre la A: «Siento energía porque veo zigzags». Sobre la B: «Siento compañía porque veo muchas personas juntas».",
        ["escribe dos semejanzas y dos diferencias", "las compara con datos visibles", "da una respuesta con emoción y detalle para cada obra", "no decide solo cuál es la más linda"],
        ["lista de semejanzas y diferencias", "dos respuestas"],
        ["comparar solo con opiniones", "no usar datos visibles"],
        "Reconoce la comparación más precisa y pregunta qué otra semejanza podría haber encontrado.",
    ),
    "Pide a una persona de tu casa que mire un objeto decorado contigo. Comparen sus respuestas y busquen qué tienen igual.",
    "Compara dos obras de lugares distintos y escribe tres diferencias.",
)

# ================================================================ OA 05
# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Una hoja, un lápiz y un trabajo de arte propio (un dibujo, una pintura o una construcción). Si no tienes uno, usa los trabajos descritos en este cuaderno.",
    "Aprenderé a construir criterios que se puedan observar para revisar un trabajo de arte. Sirve para evaluar mi trabajo y el de otros con reglas claras y no solo con gustos.",
    ["Sé describir una obra con datos visibles.", "Sé que un trabajo tiene un propósito expresivo."],
    [
        "Un criterio es una regla para revisar un trabajo. Un criterio observable es uno que se puede mirar y comprobar. «Que sea lindo» no es un criterio observable, porque cada persona lo ve distinto. «Que los colores sean cálidos» sí lo es, porque lo puedo mirar y decir sí o no. En arte, los criterios se agrupan en tres: uso de materiales, procedimientos técnicos y propósito expresivo.",
        "El uso de materiales mira si el material se usó con cuidado y si ayuda al trabajo, por ejemplo: «el pegamento no deja manchas». Los procedimientos técnicos miran cómo se hizo, por ejemplo: «las líneas del contorno están marcadas». El propósito expresivo mira si el trabajo muestra lo que quería expresar, por ejemplo: «los colores fríos muestran calma». Un buen criterio dice qué mirar y cómo reconocerlo.",
        "Para armar tus criterios, antes de hacer el trabajo, escribe tres frases: una de materiales, una de técnica y una de propósito. Después las usas para revisar el trabajo: marcas «sí» o «no» y escribes la evidencia, que es el dato que lo muestra. Los criterios se pueden construir con el curso y se usan igual para todos.",
    ],
    [("criterio", "regla para revisar un trabajo"), ("observable", "que se puede mirar y comprobar"), ("evidencia", "dato que se ve en el trabajo y muestra que se cumple el criterio"), ("procedimiento técnico", "forma en que se hizo el trabajo, como el contorno o el pegado"), ("propósito expresivo", "lo que quería mostrar o hacer sentir con el trabajo")],
    [
        w("Observable o no", "¿Cuál es un criterio observable: «que sea hermoso» o «que el contorno esté marcado con línea oscura»?", ["Pregunto: ¿lo puedo mirar y decir sí o no?", "«Hermoso» depende de cada persona.", "El contorno marcado se puede comprobar."], "«Que el contorno esté marcado con línea oscura»"),
        w("Armar tres criterios", "Vas a hacer un paisaje frío para mostrar calma. Escribe un criterio de materiales, uno de técnica y uno de propósito.", ["Materiales: la pintura se aplica sin gotas ni manchas.", "Técnica: espero que seque antes de pintar encima.", "Propósito: usa colores fríos y claros para mostrar calma."], "Tres criterios, uno por cada grupo"),
    ],
    [
        m("Usar criterios como «que sea lindo» o «que me guste».", "No se pueden comprobar y cada persona ve distinto.", "Usa criterios que se puedan mirar, como colores, líneas o limpieza."),
        m("Escribir los criterios después de ver el trabajo.", "Se adaptan a lo que salió y no guían el trabajo.", "Escribe los criterios antes de empezar y úsalos para revisar."),
    ],
    [
        ex("Un criterio observable es uno que se puede mirar y comprobar. ¿«Que sea lindo» es observable?", "No", "Depende del gusto de cada persona."),
        ex("¿Cuáles son los tres grupos de criterios: materiales, técnica y propósito, o color, tamaño y precio?", "Materiales, técnica y propósito", "Así lo indica la clase."),
        ex("La evidencia es el dato que muestra que se cumple un criterio. ¿«Las líneas son oscuras y gruesas» es una evidencia o un deseo?", "Una evidencia", "Es un dato que se puede ver."),
    ],
    [
        ex("¿A cuál grupo corresponde el criterio «el pegamento no deja manchas»: materiales, técnica o propósito?", "Materiales", "Habla del uso del material."),
        ex("¿A cuál grupo corresponde «los colores fríos muestran calma»: técnica o propósito?", "Propósito", "Habla de lo que quiere expresar."),
        ex("¿A cuál grupo corresponde «esperé que secara antes de pintar encima»: materiales, técnica o propósito?", "Técnica", "Habla de cómo se hizo el trabajo."),
    ],
    [
        ex("Quieres un criterio observable de técnica para un dibujo de contorno. ¿Eliges «que se vea bien» o «que el contorno rodee toda la forma»?", "«Que el contorno rodee toda la forma»", "El segundo se puede comprobar mirando el dibujo."),
        ex("Tu propósito es mostrar alegría. ¿Qué criterio de propósito puedes escribir: «usa colores cálidos y vivos» o «que sea bonito»?", "«Usa colores cálidos y vivos»", "Se puede comprobar mirando los colores."),
        ex("Ordena: A) revisar el trabajo con los criterios, B) escribir los criterios, C) hacer el trabajo. Escribe las tres letras en orden.", "B, C, A", "Primero los criterios, luego el trabajo y al final la revisión."),
    ],
    [
        ex("Carla dice: «Mi trabajo cumple porque a una persona de mi casa le gustó». ¿Es una evidencia observable?", "No", "Es una opinión y no un dato del trabajo."),
        ex("Daniel escribe los criterios después de terminar su trabajo y los adapta a lo que salió. ¿Le sirven para mejorar?", "No", "Los criterios deben guiar el trabajo desde el inicio."),
    ],
    [
        ex("Un criterio dice: «Se ve el contraste entre claro y oscuro». ¿Cuál puede ser su evidencia: «hay un cielo amarillo claro sobre un cerro azul oscuro» o «me gustó»?", "«Hay un cielo amarillo claro sobre un cerro azul oscuro»", "Es un dato visible."),
        ex("Quieres un criterio de propósito para un animal de plasticina que muestre fuerza. ¿Cuál es el mejor: «Las patas son gruesas y grandes» o «Es un buen animal»?", "«Las patas son gruesas y grandes»", "Se puede comprobar mirando las patas."),
    ],
    ex("En el curso van a evaluar los dibujos de los compañeros. Alguien propone el criterio «que se vea lindo». Tú propones otro. ¿Qué propones: «que el contorno rodee toda la forma» o «que a todos les guste»?", "«Que el contorno rodee toda la forma»", "Es un criterio observable."),
    [
        ex("¿Qué es un criterio?", "Una regla para revisar un trabajo", "Dice qué mirar."),
        ex("Verdadero o falso: un buen criterio se puede comprobar mirando el trabajo.", "Verdadero", "Eso lo hace observable."),
        ex("¿Cuáles son los tres grupos de criterios en arte? Escribe uno.", "Materiales, técnica o propósito", "Son los tres grupos de la clase."),
    ],
    task(
        "Elige UN trabajo que harás (o hiciste): A) un collage de un paisaje; B) un dibujo de contorno de un objeto; C) una figura de plasticina. Escribe tres criterios observables: uno de materiales, uno de técnica y uno de propósito expresivo. Escribe, para cada uno, qué evidencia se vería en el trabajo.",
        "Elegí el collage de paisaje. Materiales: el pegamento no deja manchas (se ven bordes limpios). Técnica: probé la composición antes de pegar (ninguna pieza quedó tapada por error). Propósito: muestra calma (colores fríos y claros).",
        ["escribe tres criterios, uno por grupo", "son observables", "describe la evidencia de cada uno", "los escribe antes de mirar el resultado"],
        ["tres criterios", "tres evidencias"],
        ["usar «que sea lindo»", "no escribir la evidencia"],
        "Reconoce el criterio más claro y pregunta cómo comprobaría si otro compañero lo cumple.",
    ),
    "Mira un dibujo tuyo y di un criterio observable que cumple y uno que no cumple.",
    "Pide a un compañero o a una persona de tu casa que use tus criterios para revisar tu trabajo.",
)


# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los trabajos que se revisan están descritos con palabras en el cuaderno; también puedes usar un trabajo tuyo.",
    "Aprenderé a reconocer una fortaleza de un trabajo de arte y a mostrar la evidencia que la apoya. Sirve para valorar lo que está bien hecho y poder repetirlo.",
    ["Sé construir criterios observables de materiales, técnica y propósito.", "Sé fundamentar una idea con detalles."],
    [
        "Una fortaleza es algo que el trabajo hace bien. Para decirla, hay que nombrar el criterio y la evidencia. Una frase como «está bonito» no sirve, porque no dice qué está bien. Una frase como «el contorno está marcado con línea oscura, y eso ayuda a que la forma se note» sí sirve, porque dice la evidencia y el efecto.",
        "Una buena retroalimentación de una fortaleza tiene tres partes: criterio (qué se revisó), evidencia (qué se ve) y efecto (por qué ayuda al trabajo). Por ejemplo: «En el propósito de calma, usaste colores celestes y suaves, y eso hace que el lago se vea tranquilo». Así la persona sabe qué repetir en otros trabajos. Hay que mencionar fortalezas de materiales, de técnica y de propósito, no solo del color.",
        "Para revisar el trabajo de un compañero, mira primero sin juzgar, luego busca una fortaleza para cada grupo de criterios y dilo con respeto. Al revisar tu propio trabajo, haz lo mismo: mira, busca la evidencia y escribe la fortaleza. Reconocer lo que sale bien ayuda a que pueda repetirse y da confianza para seguir.",
    ],
    [("fortaleza", "algo que el trabajo hace bien"), ("evidencia", "dato que se ve en el trabajo y apoya lo que digo"), ("efecto", "lo que logra una decisión en el trabajo"), ("retroalimentación", "comentario que ayuda a ver lo que está bien y lo que puede mejorar"), ("repetir", "volver a usar una decisión que funcionó")],
    [
        w("Armar una fortaleza", "Un collage tiene bordes limpios porque el pegamento se aplicó en poca cantidad. Escribe la fortaleza con criterio, evidencia y efecto.", ["Criterio: uso del material.", "Evidencia: los bordes están limpios, sin manchas.", "Efecto: el trabajo se ve ordenado."], "«En el uso del pegamento, los bordes están limpios y sin manchas, y eso hace que el collage se vea ordenado»"),
        w("Mejorar una frase", "Un compañero escribe: «Tu dibujo está bonito». Mejora la frase para una fortaleza de propósito.", ["Pregunto: ¿qué está bien?", "Miro la evidencia: colores fríos y líneas largas.", "Digo el efecto: da calma."], "«Tus colores fríos y tus líneas largas dan calma al paisaje»"),
    ],
    [
        m("Decir solo «me gustó» como fortaleza.", "No se sabe qué está bien hecho ni qué repetir.", "Nombra el criterio, la evidencia y el efecto."),
        m("Decir fortalezas solo del color y olvidar la técnica y los materiales.", "Se pierde información sobre cómo se hizo.", "Busca una fortaleza para cada grupo de criterios."),
    ],
    [
        ex("¿Qué es una fortaleza en un trabajo de arte: algo que hace bien o algo que falta?", "Algo que hace bien", "Es lo que el trabajo logra."),
        ex("En la frase «Los bordes están limpios y sin manchas», ¿cuál es la evidencia: bordes limpios o me gusta?", "Bordes limpios y sin manchas", "Es lo que se ve en el trabajo."),
        ex("Una buena retroalimentación de una fortaleza tiene tres partes: criterio, evidencia y efecto. ¿Cuál es la que dice «qué se ve»?", "La evidencia", "La evidencia es el dato visible."),
    ],
    [
        ex("Trabajo descrito: «Un cielo celeste con líneas largas y suaves para mostrar calma». ¿Cuál es la fortaleza de propósito: «da calma» o «es bonito»?", "«Da calma»", "Dice qué se logra con relación al propósito."),
        ex("Frase: «El contorno está marcado con línea oscura y eso ayuda a que la forma se note». ¿Qué grupo de criterios menciona: materiales, técnica o propósito?", "Técnica", "Habla de cómo se hizo el contorno."),
        ex("¿Qué frase es una fortaleza bien dicha? A: «Está bonito». B: «Los colores cálidos y vivos muestran alegría».", "B", "La B nombra evidencia y efecto."),
    ],
    [
        ex("Trabajo descrito: «Una figura de plasticina con patas anchas». ¿Cuál es el efecto de las patas anchas: que la figura se mantenga de pie o que se vea más pequeña?", "Que la figura se mantenga de pie", "Las patas anchas dan firmeza."),
        ex("Trabajo descrito: «Un dibujo con un cielo oscuro y rayos amarillos para mostrar tensión». ¿Qué evidencia nombras: cielo oscuro y rayos amarillos o el tamaño de la hoja?", "Cielo oscuro y rayos amarillos", "Esos son los datos que se relacionan con la tensión."),
        ex("Ordena las partes de una frase: A) efecto, B) criterio, C) evidencia. Escribe las letras en el orden de la clase.", "B, C, A", "Criterio, evidencia y efecto."),
    ],
    [
        ex("Ana dice: «La fortaleza de tu trabajo es el color porque siempre me gusta el azul». ¿Su razón es una evidencia del trabajo?", "No", "Habla de su gusto y no de lo que se ve."),
        ex("Luis dice una fortaleza de materiales, una de técnica y una de propósito. ¿Revisó solo un grupo de criterios?", "No", "Revisó los tres grupos."),
    ],
    [
        ex("Un compañero hizo un collage con bordes limpios y ordenó antes de pegar. ¿Qué dos grupos de criterios tienen fortalezas: materiales y técnica o solo propósito?", "Materiales y técnica", "Los bordes limpios son de materiales y ordenar antes es de técnica."),
        ex("Al decir una fortaleza al compañero, ¿es mejor decir «lo hiciste bien» o «tus líneas oscuras marcan el contorno»?", "«Tus líneas oscuras marcan el contorno»", "Da información que puede repetir."),
    ],
    ex("Un compañero te muestra su pintura de un lago con colores azules suaves y te pide opinión. Tú quieres darle una fortaleza útil. ¿Qué dices: «Tu pintura es linda» o «Tus azules suaves hacen que el lago se vea tranquilo»?", "«Tus azules suaves hacen que el lago se vea tranquilo»", "Dice evidencia y efecto."),
    [
        ex("¿Qué partes tiene una buena fortaleza?", "Criterio, evidencia y efecto", "Así se dice con claridad."),
        ex("Verdadero o falso: «me gustó» es una buena fortaleza.", "Falso", "No dice qué se hizo bien."),
        ex("¿Para qué sirve decir una fortaleza con evidencia?", "Para saber qué repetir", "La persona sabe qué decisión funcionó."),
    ],
    task(
        "Elige UN trabajo: A) el collage descrito aquí: «un paisaje de montañas hecho con papel rasgado en capas, pegado con poco pegamento y sin manchas, para mostrar relieve»; B) el dibujo descrito aquí: «un cielo oscuro con un rayo amarillo quebrado»; C) un trabajo tuyo. Escribe tres fortalezas, una de materiales, una de técnica y una de propósito, cada una con criterio, evidencia y efecto.",
        "Elegí el collage. Materiales: los bordes están limpios porque usé poco pegamento, y eso lo hace ordenado. Técnica: ordené antes de pegar y la composición se ve equilibrada. Propósito: el papel rasgado de las montañas da sensación de relieve.",
        ["escribe tres fortalezas", "cada una tiene criterio, evidencia y efecto", "las fortalezas se refieren a los tres grupos", "usa datos observables"],
        ["tres frases de fortaleza"],
        ["decir solo «me gusta»", "mencionar solo el color"],
        "Valora la fortaleza con mejor evidencia y pregunta cómo podría repetirla en otro trabajo.",
    ),
    "Mira un trabajo tuyo y di una fortaleza con evidencia y efecto.",
    "Pide a una persona de tu casa que te diga una fortaleza de tu trabajo y revisa si trae evidencia.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Una hoja y un lápiz. Los trabajos que se revisan están descritos con palabras en el cuaderno.",
    "Aprenderé a proponer una mejora que sea clara, posible y coherente con el propósito del trabajo. Sirve para ayudar a mejorar un trabajo sin cambiarlo por completo.",
    ["Sé decir una fortaleza con criterio, evidencia y efecto.", "Sé construir criterios observables."],
    [
        "Un aspecto a mejorar es algo que podría estar mejor para lograr el propósito del trabajo. Para decirlo con respeto, parte por la fortaleza y luego propone una mejora. Una mejora coherente es la que ayuda al propósito expresivo y que se puede hacer con los materiales que hay. Por ejemplo, si el propósito es calma y hay colores muy oscuros, una mejora coherente es aclarar el cielo.",
        "Una mejora útil tiene tres partes: lo que se observa («el cielo es muy oscuro»), el cambio que propongo («prueba un celeste más claro») y por qué ayuda («así se ve más tranquilo»). Una mejora no dice «hazlo de nuevo» ni «cámbialo todo», porque no explica qué cambiar. Tampoco debe ser un gusto personal («pon mi color favorito»).",
        "Cuando propongas una mejora, pregúntate: ¿se relaciona con el propósito?, ¿se puede hacer con los materiales que hay?, ¿es un cambio pequeño y claro? Si respondes sí, es una buena mejora. Al final, quien hizo el trabajo decide si la usa o no, porque es su obra. Una mejora se ofrece, no se impone.",
    ],
    [("aspecto a mejorar", "algo que podría estar mejor para lograr el propósito"), ("coherente", "que se relaciona bien con el propósito del trabajo"), ("propuesta", "cambio que sugiero para mejorar un trabajo"), ("gusto personal", "lo que me gusta a mí y no necesariamente ayuda al trabajo"), ("imponer", "obligar a alguien a aceptar mi idea")],
    [
        w("Armar una mejora", "Un paisaje quiere mostrar calma, pero el cielo está pintado con negro y rojo oscuro. Escribe una mejora con observación, cambio y razón.", ["Observación: el cielo es muy oscuro.", "Cambio: probar celeste claro con nubes suaves.", "Razón: así se verá más tranquilo."], "«El cielo es muy oscuro; prueba un celeste claro para que se vea más tranquilo»"),
        w("Distinguir mejora y gusto", "Un compañero dice «Usa mi color favorito, el verde». ¿Es una mejora coherente?", ["No se relaciona con el propósito del trabajo.", "Es un gusto personal.", "No es una mejora coherente."], "No, es un gusto personal"),
    ],
    [
        m("Decir «hazlo de nuevo» cuando algo no te gusta.", "No dice qué cambiar ni por qué.", "Nombra un cambio pequeño y claro."),
        m("Imponer mi idea sin escuchar a quien hizo el trabajo.", "La obra es de quien la hizo y él o ella decide.", "Ofrece la mejora y deja que decida."),
    ],
    [
        ex("Una mejora coherente ayuda al propósito del trabajo. ¿Cambiar el cielo oscuro a uno claro ayuda a mostrar calma?", "Sí", "Los tonos claros dan calma."),
        ex("¿«Hazlo de nuevo» es una mejora clara o poco clara?", "Poco clara", "No dice qué cambiar."),
        ex("¿Quién decide si usa una mejora: quien la propone o quien hizo el trabajo?", "Quien hizo el trabajo", "La obra es suya."),
    ],
    [
        ex("Trabajo descrito: «Un animal de plasticina que quiere verse fuerte, pero tiene patas muy delgadas». ¿Qué mejora es coherente: hacer las patas más gruesas o cambiar el color de la base?", "Hacer las patas más gruesas", "Las patas gruesas dan idea de fuerza."),
        ex("Frase: «Tu cielo es muy oscuro; prueba un celeste claro para que se vea más tranquilo». ¿Cuál es la observación: cielo muy oscuro o celeste claro?", "Cielo muy oscuro", "Es lo que se ve."),
        ex("¿Qué mejora es mejor? A: «Usa mi color favorito». B: «Prueba una línea más gruesa en el contorno para que la forma se note».", "B", "La B es clara y ayuda al trabajo."),
    ],
    [
        ex("Trabajo descrito: «Un collage de un lago con papel pegado que se despega en las esquinas». Propones: «Agrega un poco más de cola en las esquinas». ¿Es una mejora de materiales o de propósito?", "De materiales", "Habla del uso del pegamento."),
        ex("Trabajo descrito: «Un dibujo que quiere mostrar alegría, pero todos los colores son grises». Propones: «Agrega un sol amarillo y flores de colores vivos». ¿La mejora es coherente con el propósito?", "Sí", "Los colores vivos van con alegría."),
        ex("Ordena las partes de una mejora: A) por qué ayuda, B) el cambio que propongo, C) lo que observo. Escribe las letras en orden.", "C, B, A", "Primero lo observado, luego el cambio y luego el porqué."),
    ],
    [
        ex("Ana dice: «Tu dibujo está mal, hazlo otra vez». Compañero: «No sé qué cambiar». ¿La mejora de Ana es clara?", "No", "No dice qué cambiar."),
        ex("Tomás propone: «Pinta de azul oscuro el cielo» a un dibujo que quiere mostrar alegría. ¿Es coherente con el propósito?", "No", "El azul oscuro no se relaciona con alegría."),
    ],
    [
        ex("Quieres sugerir una mejora a un compañero sin imponer. ¿Dices «Podrías probar...» o «Tienes que hacer...»?", "«Podrías probar...»", "Ofrece la mejora y deja decidir."),
        ex("Trabajo descrito: «Un dibujo de una montaña lejana y una cercana con la misma línea oscura». Quiere mostrar profundidad. ¿Qué cambio es coherente: línea más suave para la montaña lejana o línea más gruesa para ambas?", "Línea más suave para la montaña lejana", "Una línea suave se ve más lejana."),
    ],
    ex("Tu compañera te muestra su pintura de una playa tranquila, pero usó rayas negras muy fuertes en el mar. Quieres ayudarla. ¿Qué dices: «Prueba con líneas celestes suaves en el mar para que se vea tranquilo» o «No me gusta tu mar»?", "«Prueba con líneas celestes suaves en el mar para que se vea tranquilo»", "Es una mejora clara y coherente."),
    [
        ex("¿Qué debe tener una mejora útil? Escribe una de las tres partes.", "Lo que observo, el cambio o por qué ayuda", "Esas son las tres partes."),
        ex("Verdadero o falso: una mejora debe ayudar al propósito del trabajo.", "Verdadero", "Eso la hace coherente."),
        ex("¿Una mejora se impone o se ofrece?", "Se ofrece", "Quien hizo el trabajo decide."),
    ],
    task(
        "Elige UN trabajo: A) «Un paisaje que quiere mostrar calma, con un lago de líneas largas y suaves, pero con un cielo negro y rojo oscuro». B) «Un animal de plasticina que quiere verse fuerte, pero tiene patas muy delgadas». C) un trabajo tuyo. Escribe una fortaleza y dos mejoras coherentes con el propósito. Cada mejora debe tener: lo que observas, el cambio y por qué ayuda.",
        "Elegí A. Fortaleza: las líneas largas y suaves del lago dan quietud. Mejora 1: el cielo es muy oscuro; prueba un celeste claro para que se vea tranquilo. Mejora 2: el rojo oscuro da tensión; prueba un rosado muy claro cerca del horizonte para que se sienta calmo.",
        ["escribe una fortaleza y dos mejoras", "cada mejora tiene observación, cambio y razón", "las mejoras son coherentes con el propósito", "ofrece y no impone"],
        ["una fortaleza", "dos mejoras"],
        ["decir «hazlo de nuevo»", "proponer un gusto personal"],
        "Reconoce la mejora más clara y pregunta si esa mejora ayuda al propósito.",
    ),
    "Mira un trabajo tuyo y di una mejora con observación, cambio y razón.",
    "Propón la misma mejora de dos maneras (un cambio chico y uno más grande) y anota cuál ayuda más.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Un trabajo propio ya hecho, una hoja de papel nueva para probar y lápices. Si no tienes uno, usa el trabajo descrito en el cuaderno.",
    "Aprenderé a mejorar mi propio trabajo usando los comentarios de otras personas, sin perder mis ideas. Sirve para aprender de otros y mantener mi autoría.",
    ["Sé decir una fortaleza con evidencia.", "Sé proponer una mejora coherente."],
    [
        "Revisar un trabajo es volver a mirarlo después de recibir comentarios y decidir qué cambiar. La autoría es ser quien hizo la obra y decidir sobre ella. Los demás pueden dar ideas, pero no hacer el trabajo por mí ni cambiar mi obra sin permiso. Yo decido qué comentarios uso y cuáles no, siempre con una razón que se relacione con mi propósito.",
        "Para revisar, sigue cuatro pasos. Primero, lee los comentarios y marca los que se relacionan con tu propósito. Segundo, decide cuáles usarás y por qué. Tercero, prueba el cambio en una hoja aparte o en una parte pequeña. Cuarto, compara antes y después: ¿ayuda más al propósito? Si no ayuda, puedes volver a la primera versión.",
        "Anota los cambios en una lista: qué cambié, por qué y qué resultado tuvo. Así queda claro que las decisiones son tuyas. Si usas una idea de un compañero, escribe «gracias por la sugerencia de ___». Una obra puede mejorar sin dejar de ser tuya, porque tú decidiste cada cambio.",
    ],
    [("autoría", "ser quien hizo una obra y decidir sobre ella"), ("revisar", "volver a mirar un trabajo y decidir qué cambiar"), ("versión", "forma en que está el trabajo en un momento"), ("comentario", "cosa que dice otra persona sobre mi trabajo"), ("decisión propia", "elección que hago yo y que puedo explicar")],
    [
        w("Elegir comentarios", "Recibes dos comentarios sobre tu paisaje de calma: A) «Aclara el cielo para que se vea más tranquilo». B) «Pon un dinosaurio». ¿Cuál usas?", ["Miro mi propósito: calma.", "El comentario A ayuda a mostrar calma.", "El B no se relaciona con mi propósito."], "El comentario A"),
        w("Probar antes de cambiar", "Decidiste aclarar el cielo de tu pintura, pero te da miedo arruinarla. ¿Qué haces?", ["Pruebo el cambio en una hoja aparte.", "Comparo la prueba con mi pintura.", "Si queda mejor, hago el cambio; si no, mantengo la versión anterior."], "Probar el cambio en una hoja aparte y comparar"),
    ],
    [
        m("Aceptar todos los comentarios sin pensarlo.", "Se pierde el propósito y la idea propia.", "Elige solo los que ayudan a tu propósito y explica por qué."),
        m("Dejar que otra persona pinte sobre mi trabajo.", "Se pierde la autoría porque ya no son mis decisiones.", "Las sugerencias se dicen, pero el trabajo lo hago yo."),
    ],
    [
        ex("La autoría es ser quien hizo la obra y decidir sobre ella. ¿Puede otra persona pintar sobre mi obra sin mi permiso?", "No", "Yo decido sobre mi obra."),
        ex("Recibes un comentario. ¿Qué haces primero: lo lees y ves si se relaciona con tu propósito o lo aplicas sin pensar?", "Lo lees y ves si se relaciona con tu propósito", "Es el primer paso de la clase."),
        ex("Antes de cambiar una parte de tu pintura, ¿puedes probar el cambio en una hoja aparte?", "Sí", "Así no arriesgas tu trabajo."),
    ],
    [
        ex("Tu propósito es calma. Un compañero dice «Agrega rayos rojos». ¿Ese comentario ayuda a tu propósito?", "No", "Los rayos rojos dan tensión."),
        ex("Cambiaste el cielo de tu pintura a un celeste claro y ahora se ve más tranquilo. ¿El cambio ayudó al propósito de calma?", "Sí", "El tono más claro da más tranquilidad."),
        ex("Anotas: «Cambié el cielo a celeste claro porque mi propósito es calma». ¿Qué parte es la razón: cambié el cielo o porque mi propósito es calma?", "Porque mi propósito es calma", "Es lo que explica por qué se hizo el cambio."),
    ],
    [
        ex("Recibes tres comentarios: A) aclarar el cielo; B) agregar un dinosaurio; C) hacer más suaves las líneas. Tu propósito es calma. ¿Cuáles usas?", "A y C", "El comentario B no ayuda a la calma."),
        ex("Ordena los pasos de revisión: A) probar el cambio, B) leer los comentarios, C) comparar antes y después. Escribe las letras en orden.", "B, A, C", "Se lee, se prueba y se compara."),
        ex("Comparas antes y después y el cambio no ayuda al propósito. ¿Qué puedes hacer: volver a la versión anterior o dejarlo igual?", "Volver a la versión anterior", "La decisión es tuya y puedes volver atrás."),
    ],
    [
        ex("Pedro cambió todo su dibujo porque un compañero se lo dijo, aunque no entendía por qué. ¿Conservó su autoría?", "No", "No tomó decisiones propias."),
        ex("Ana usó un comentario porque ayuda a su propósito y lo anotó con su razón. ¿Conservó su autoría?", "Sí", "Ella decidió con una razón propia."),
    ],
    [
        ex("Recibiste el comentario: «Agrega más contraste». Tu propósito es misterio con un bosque oscuro. ¿Qué cambio propones: una luz pequeña y clara en el fondo o pintar todo del mismo oscuro?", "Una luz pequeña y clara en el fondo", "El contraste entre lo claro y lo oscuro refuerza el misterio."),
        ex("Escribes: «Gracias por la sugerencia de aclarar el cielo». ¿Qué reconoces con esa frase: la ayuda de otra persona o la autoría?", "La ayuda de otra persona", "Agradece la idea sin perder la autoría."),
    ],
    ex("En el curso, una compañera te dice que cambies tu animal de plasticina, y toma la plasticina para hacerlo ella. ¿Qué haces: le pides que no cambie tu trabajo y que te diga la sugerencia, o la dejas hacer?", "Le pides que no cambie tu trabajo y que te diga la sugerencia", "La obra es tuya y las ideas se dicen, no se imponen."),
    [
        ex("En Artes Visuales: ¿qué es la autoría de una obra?", "Ser quien hizo la obra y decidir sobre ella", "Yo decido los cambios."),
        ex("Verdadero o falso: puedo decidir no usar un comentario.", "Verdadero", "Si no ayuda a mi propósito, puedo dejarlo."),
        ex("¿Qué se compara en el paso final de revisión?", "El antes y el después", "Se mira si el cambio ayuda al propósito."),
    ],
    task(
        "Usa UN trabajo (uno tuyo o este: «un paisaje de calma con un cielo oscuro y líneas quebradas»). Recibe estos comentarios: A) aclarar el cielo; B) hacer las líneas largas y suaves; C) agregar un dinosaurio. Elige cuáles usas y cuáles no, con tu propósito como razón. Prueba un cambio en una hoja aparte y escribe una lista de cambios: qué cambié, por qué y qué resultado tuvo.",
        "Usé A y B porque mi propósito es calma. No usé C porque no tiene relación. Probé el cielo celeste en una hoja aparte y se veía más tranquilo. Lista: cambié el cielo a celeste, por calma, resultado: mejor.",
        ["elige comentarios según su propósito", "prueba antes de cambiar", "anota qué, por qué y resultado", "conserva la autoría"],
        ["prueba", "lista de cambios"],
        ["aceptar todo sin pensar", "dejar que otro cambie su obra"],
        "Valora que las decisiones sean propias y pregunta qué comentario no usó y por qué.",
    ),
    "Cuéntale a una persona de tu casa qué comentario usaste en tu trabajo y cuál no, y por qué.",
    "Haz dos versiones de tu trabajo con comentarios distintos y anota cuál ayuda más a tu propósito.",
)

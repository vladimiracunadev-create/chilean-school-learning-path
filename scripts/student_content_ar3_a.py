"""Cuaderno del estudiante de 3.º básico Artes Visuales: AR03 OA 01 (creación con propósito desde naturaleza, cultura y arte) y AR03 OA 02 (lenguaje visual)."""
from __future__ import annotations

from student_lessons import ex, register

OA1 = "AR03 OA 01"
OA2 = "AR03 OA 02"


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


# ================================================================ OA 01
# ---------------------------------------------------------------- Clase 1
lesson(
    OA1, 1,
    "Una hoja, un lápiz de mina y lápices de colores. Para observar puedes usar una planta de tu casa, un insecto o un pájaro que veas desde la ventana, o el cielo. Si no puedes, usa las descripciones escritas en este cuaderno.",
    "Aprenderé a mirar con mucho detalle un animal, una planta o un fenómeno de la naturaleza antes de dibujarlo. Sirve para que mis dibujos tengan cosas que de verdad vi y no solo lo que recuerdo.",
    ["Sé dibujar líneas, formas y colores con el lápiz.", "Sé decir si algo es grande o pequeño, liso o áspero."],
    [
        "La naturaleza es una gran fuente de ideas para el arte. Incluye animales, plantas y fenómenos naturales. Un fenómeno natural es algo que ocurre en la naturaleza sin que lo haga una persona, como la lluvia, el viento, un arcoíris o las olas del mar. Antes de dibujar, hay que observar: mirar despacio y con atención.",
        "Para observar con detalle, hazte cinco preguntas sobre lo que miras. ¿Qué forma tiene? ¿De qué color es? ¿Cómo es su textura, es decir, cómo se siente o se ve la superficie? ¿Qué tamaño tiene? ¿Cómo se mueve? Decir «es lindo» no basta. Decir «el caracol tiene una concha en espiral con rayas claras» sí es un detalle.",
        "Observar no es copiar. Cuando miras bien, descubres cosas que después puedes usar en tu propio trabajo. Cuida lo que observas: no arranques plantas de plazas o parques, no molestes ni toques animales que no conoces y mira los insectos sin aplastarlos. Un dibujo de observación se hace con calma y puede tomar varios minutos.",
    ],
    [("observar", "mirar despacio y con atención para descubrir detalles"), ("fenómeno natural", "algo que ocurre en la naturaleza, como la lluvia o el viento"), ("detalle", "una parte pequeña de algo que casi no se nota"), ("textura", "cómo se siente o se ve la superficie de algo"), ("propósito expresivo", "lo que quiero mostrar o hacer sentir con mi trabajo")],
    [
        w("Observar un caracol", "Lees: «El caracol tiene una concha en espiral, de color café con rayas claras, y avanza muy despacio». ¿Qué detalles de forma, color y movimiento hay?", ["Busco la forma: la concha es una espiral.", "Busco el color: café con rayas claras.", "Busco el movimiento: avanza muy despacio."], "Forma: espiral. Color: café con rayas. Movimiento: despacio"),
        w("Observar la lluvia", "Miras la lluvia por la ventana. Las gotas caen en líneas inclinadas y en el charco se forman círculos que se agrandan. ¿Qué dos formas aparecen?", ["Las gotas que caen forman líneas inclinadas.", "En el charco aparecen círculos que se agrandan."], "Líneas inclinadas y círculos"),
    ],
    [
        m("Decir solo «el pájaro es lindo» y empezar a dibujar.", "No se nombra ningún detalle que se pueda dibujar.", "Mira forma, color, textura, tamaño y movimiento, y anota al menos tres detalles."),
        m("Dibujar una flor de memoria y llamarlo dibujo de observación.", "No se miró la flor real ni una descripción de ella.", "Mira la planta mientras dibujas y fíjate en lo que realmente tiene."),
    ],
    [
        ex("Lees: «El caracol tiene una concha en espiral, café con rayas claras». ¿Qué forma tiene su concha?", "En espiral", "La frase dice que la concha es una espiral."),
        ex("Una planta tiene tallo largo y delgado, hojas anchas y una flor amarilla. ¿De qué color es la flor?", "Amarilla", "La descripción nombra una flor amarilla."),
        ex("En un charco, las gotas de lluvia forman círculos que se agrandan. ¿Qué forma se repite en el charco?", "Círculos", "La descripción dice que se forman círculos."),
    ],
    [
        ex("¿Cuál frase es una observación con detalle? A: «Es lindo.» B: «Las alas de la mariposa son anaranjadas con bordes negros y manchas blancas.» C: «Me gustó.»", "B", "Solo la frase B nombra colores y partes que se pueden dibujar."),
        ex("Dices que una hoja es áspera como una lija. ¿Cuál de los cinco aspectos (forma, color, textura, tamaño, movimiento) describes?", "La textura", "Áspera dice cómo se siente la superficie."),
        ex("Un fenómeno natural ocurre sin que lo haga una persona. Entre viento, mesa y lápiz, ¿cuál es un fenómeno natural?", "El viento", "La mesa y el lápiz los hace una persona; el viento ocurre en la naturaleza."),
    ],
    [
        ex("Un pájaro es pequeño y salta de rama en rama. ¿Qué dos aspectos se nombran: «pequeño» y «salta»?", "Tamaño y movimiento", "Pequeño habla del tamaño y saltar es un movimiento."),
        ex("Describes un helecho: «Sus hojitas están en filas a ambos lados del tallo». ¿Cómo las dibujarías: en filas a ambos lados del tallo o sueltas y sin orden?", "En filas a ambos lados del tallo", "El dibujo debe mostrar lo que se observó."),
        ex("Miras una nube durante cinco minutos. Al inicio era una bola y al final una línea larga. ¿Qué aspecto cambió: la forma o el color?", "La forma", "Pasó de bola a línea, y eso es un cambio de forma."),
    ],
    [
        ex("Mateo dibuja un perro sin mirar ninguno. Lucía mira uno dos minutos y dibuja su oreja caída y su cola enroscada. ¿Qué dibujo tendrá más detalles observados?", "El de Lucía", "Ella miró al perro y dibujó lo que vio."),
        ex("Ana vio que la lluvia caía inclinada porque soplaba viento, pero dibujó las rayas de lluvia rectas hacia abajo. ¿Qué detalle observado no usó?", "La inclinación de la lluvia", "Ella vio rayas inclinadas, pero las dibujó rectas."),
    ],
    [
        ex("Observación: «El pelícano abre sus alas grandes y se deja caer al agua». ¿Qué aspecto aparece con claridad: el movimiento o la textura?", "El movimiento", "Abrir las alas y dejarse caer son movimientos."),
        ex("Quieres dibujar un arcoíris, que es un fenómeno natural. ¿Qué observas primero: la forma que hace en el cielo o el número de tu casa?", "La forma que hace en el cielo", "Observar es mirar el fenómeno mismo."),
    ],
    ex("Vas a la playa y ves una gaviota que camina cerca de las olas. Quieres dibujarla. ¿Qué haces primero: mirarla con detalle o dibujar una gaviota de memoria?", "Mirarla con detalle", "Un dibujo de observación parte mirando lo que hay."),
    [
        ex("¿Cuáles son los cinco aspectos para observar? Escribe los que recuerdes: forma, color y tres más.", "Textura, tamaño y movimiento", "Los cinco aspectos son forma, color, textura, tamaño y movimiento."),
        ex("Verdadero o falso: la lluvia es un fenómeno natural.", "Verdadero", "Ocurre en la naturaleza sin que la haga una persona."),
        ex("¿Se pueden arrancar plantas de una plaza para dibujarlas?", "No", "Hay que cuidar las plantas y observarlas donde están."),
    ],
    task(
        "Elige UNA cosa para observar: A) una hoja o una planta de tu casa o de una plaza (sin arrancarla); B) un pájaro o un insecto que veas desde una ventana; C) el cielo con nubes o con lluvia. Mírala tres minutos. Escribe cinco detalles: forma, color, textura, tamaño y movimiento. Luego haz un dibujo con al menos tres de esos detalles.",
        "Elegí una hoja de limón. Forma: ovalada con punta. Color: verde oscuro arriba y claro abajo. Textura: lisa y brillante. Tamaño: del largo de mi dedo. Movimiento: se mueve con el viento. Dibujé la hoja con su punta y su nervio del centro.",
        ["escribe cinco detalles distintos", "usa lo que realmente miró", "dibuja al menos tres de los detalles", "no daña lo que observa"],
        ["lista de cinco detalles", "dibujo de observación"],
        ["escribir solo «es lindo»", "dibujar de memoria sin mirar"],
        "Reconoce el detalle más preciso y pregunta qué parte del dibujo salió de algo que vio, no de algo que recordaba.",
    ),
    "Mira durante un minuto algo de la naturaleza que haya cerca de ti. Di en voz alta tres detalles de ese objeto.",
    "Observa otro día lo mismo que miraste hoy y anota qué cambió: de luz, de color o de movimiento.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Hoja, lápiz de mina y lápices de colores o témpera. Usa tu dibujo de observación de la clase anterior o las observaciones escritas en este cuaderno.",
    "Aprenderé a decidir qué quiero expresar con un dibujo y a elegir líneas, colores y tamaños para lograrlo. Sirve para que mis trabajos digan algo mío y no solo muestren cómo se ve una cosa.",
    ["Sé observar con detalle forma, color, textura, tamaño y movimiento.", "Sé que un dibujo puede contar una idea o un sentimiento."],
    [
        "Un propósito expresivo es lo que quiero mostrar o hacer sentir con mi trabajo: calma, alegría, misterio, fuerza o sorpresa. Dos personas pueden mirar la misma tormenta y hacer dibujos distintos, porque cada una quiere expresar algo diferente. Eso es lo propio de cada artista.",
        "Para pasar de una observación a una intención visual, sigue tres pasos. Primero observa: por ejemplo, el mar con olas grandes. Segundo decide el propósito: «quiero mostrar que el mar da miedo» o «quiero mostrar que el mar me da calma». Tercero elige los recursos: líneas, colores y tamaños que ayuden a ese propósito. Para miedo puedes usar líneas quebradas, colores oscuros y olas enormes. Para calma, líneas suaves y largas y colores claros.",
        "Los recursos no tienen un significado único para todos. Muchas personas sienten calma con líneas suaves, pero cada artista decide y puede explicar su elección. Un buen trabajo muestra una relación clara entre lo que quiero expresar y lo que elegí dibujar.",
    ],
    [("propósito expresivo", "lo que quiero mostrar o hacer sentir con mi trabajo"), ("intención visual", "decidir cómo se verá mi trabajo para lograr mi propósito"), ("recurso visual", "línea, color, forma o tamaño que uso para expresar algo"), ("línea quebrada", "línea con picos y cambios bruscos de dirección"), ("línea suave", "línea larga y curva que cambia de dirección sin quiebres")],
    [
        w("Mar con miedo", "Observaste olas grandes. Quieres expresar miedo. ¿Qué recursos eliges?", ["Mi propósito es el miedo.", "Elijo líneas quebradas para las olas.", "Uso colores oscuros y hago una ola enorme sobre un barquito pequeño."], "Líneas quebradas, colores oscuros y una ola enorme"),
        w("Mar con calma", "Observaste el mismo mar, pero ahora quieres expresar calma. ¿Qué cambias?", ["Cambio mi propósito a calma.", "Dibujo líneas largas y suaves.", "Uso colores claros y dejo mucho cielo despejado."], "Líneas suaves, colores claros y cielo despejado"),
    ],
    [
        m("Dibujar lo mismo para cualquier propósito y solo cambiar el título.", "Los recursos visuales no se eligen según lo que se quiere expresar.", "Elige líneas, colores y tamaños que ayuden a tu propósito y que puedas explicar."),
        m("Decir que un color significa lo mismo para todas las personas.", "Cada persona y cada cultura pueden sentir cosas distintas.", "Explica por qué elegiste ese color para tu propósito."),
    ],
    [
        ex("Quieres mostrar miedo con un dibujo de olas. ¿Qué tipo de líneas usó el ejemplo de la clase para eso: quebradas o suaves?", "Quebradas", "La clase enseña líneas quebradas para el miedo en ese ejemplo."),
        ex("¿Qué es un propósito expresivo? A: el nombre del dibujo. B: lo que quiero mostrar o hacer sentir. C: el tipo de lápiz.", "B", "El propósito es lo que se quiere expresar con el trabajo."),
        ex("Lees: «Dibujé una flor chiquitita en una esquina para mostrar soledad». ¿Qué propósito expresivo tiene este dibujo?", "Mostrar soledad", "La frase dice que la flor pequeña y aislada muestra soledad."),
    ],
    [
        ex("Dos niñas miran la misma tormenta. Una dibuja rayos y colores oscuros. La otra dibuja una lluvia suave sobre un jardín. ¿Se parecen sus propósitos?", "No", "Una expresa fuerza o miedo y la otra expresa calma."),
        ex("Una línea suave y larga se usa en esta clase para expresar calma. ¿Para qué propósito sirve más una línea quebrada: para miedo o para calma?", "Para miedo", "En esta clase las líneas quebradas se usan para el miedo."),
        ex("Un niño pinta un sol grande y amarillo para mostrar alegría, y dice «para mí el amarillo es alegre». ¿Qué hizo bien: explicar su elección o copiar un dibujo?", "Explicar su elección", "Dio una razón personal para su recurso visual."),
    ],
    [
        ex("Quieres mostrar miedo con un barquito en el mar, como en el ejemplo de la clase. ¿Cómo dibujas la ola: enorme sobre el barquito pequeño o muy chiquita junto al barquito?", "Enorme sobre el barquito pequeño", "En el ejemplo de la clase, el miedo se muestra con una ola enorme sobre un barquito pequeño."),
        ex("Quieres mostrar calma en un dibujo de un lago. Entre líneas muy quebradas y líneas largas y suaves, ¿cuáles eliges?", "Líneas largas y suaves", "Se eligen según el propósito de calma."),
        ex("Ordena los pasos: A elegir líneas y colores, B observar, C decidir el propósito.", "B, C, A", "Primero observas, luego decides tu propósito y al final eliges los recursos."),
    ],
    [
        ex("Pedro dibujó una tormenta con líneas suaves, pero quería mostrar miedo. ¿Qué tipo de líneas puede usar, según la clase: quebradas o más suaves todavía?", "Quebradas", "Para expresar miedo, la clase enseña líneas quebradas."),
        ex("Laura dice: «Mi dibujo expresa alegría porque usé muchos colores muy vivos». ¿Su razón nombra un recurso visual que se ve en el dibujo?", "Sí", "Los muchos colores vivos son un recurso que se puede ver."),
    ],
    [
        ex("Quieres mostrar miedo con una tormenta. Anotas: «Pinté los rayos con líneas quebradas». ¿Qué recurso visual nombras: la línea o el color?", "La línea", "Las líneas quebradas son un tipo de línea."),
        ex("Dos dibujos del mismo gato. El A tiene líneas suaves y el gato dormido. El B tiene líneas quebradas y el gato erizado. ¿Cuál expresa más calma?", "El A", "Las líneas suaves y el gato dormido van con calma."),
    ],
    ex("Imagina que ves cómo cae el sol sobre un desierto, con colores naranjas. Quieres expresar tranquilidad. ¿Qué eliges: líneas suaves y largas o líneas quebradas?", "Líneas suaves y largas", "Las líneas suaves ayudan a expresar tranquilidad."),
    [
        ex("¿Qué pasos sigues para pasar de una observación a una intención visual? Escribe el segundo.", "Decidir el propósito", "Los pasos son observar, decidir el propósito y elegir recursos."),
        ex("Verdadero o falso: dos artistas pueden hacer dibujos distintos de la misma tormenta.", "Verdadero", "Cada uno puede tener un propósito diferente."),
        ex("¿Se puede explicar una elección de color con una razón personal?", "Sí", "Un buen trabajo explica por qué se eligió un recurso."),
    ],
    task(
        "Elige UNA observación: A) olas del mar muy grandes; B) un árbol solo en un cerro; C) la lluvia sobre un patio. Elige un propósito: miedo, calma o alegría. Haz un dibujo con líneas, colores y tamaños que ayuden a tu propósito. Escribe dos recursos que elegiste y por qué.",
        "Elegí el árbol solo en un cerro y el propósito de calma. Dibujé líneas largas y suaves, colores claros y mucho cielo. Elegí líneas suaves porque a mí me dan tranquilidad.",
        ["elige observación y propósito", "usa al menos dos recursos visuales", "explica por qué los eligió", "el dibujo se relaciona con el propósito"],
        ["dibujo con propósito", "dos frases de explicación"],
        ["dibujar sin decidir un propósito", "explicar con «porque sí»"],
        "Reconoce la relación entre propósito y recurso y pide que explique una elección más con una razón propia.",
    ),
    "Mira un objeto de tu casa y di en voz alta dos propósitos distintos para dibujarlo, por ejemplo calma y alegría.",
    "Haz el mismo dibujo dos veces con propósitos distintos y anota qué recursos cambiaste.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hoja, lápices de colores y un lápiz de mina. Usa el relato inventado de este cuaderno. El docente puede traer un mito real con su fuente: libro, autor, comunidad o persona que lo cuenta.",
    "Aprenderé qué es un mito, por qué hay que saber de dónde viene y cómo crear mi propia imagen de un momento del relato. Sirve para respetar los relatos de las culturas y también crear con ideas propias.",
    ["Sé escuchar o leer un cuento corto.", "Sé que un dibujo puede mostrar un momento de una historia."],
    [
        "Un mito es un relato muy antiguo que explica algo del mundo, como el origen del mar, del fuego o de las estaciones. En los mitos aparecen dioses, seres imaginarios y fuerzas de la naturaleza. Por ejemplo, en los mitos de la antigua Grecia, Poseidón es el dios del mar. Cada cultura tiene sus propios mitos.",
        "Antes de dibujar un mito, hay que identificar la fuente: quién lo cuenta y de dónde viene. Puede ser un libro con su autor, una persona de una comunidad o un docente que lo investigó. Así evitamos mezclar relatos o atribuir a una cultura algo que no es suyo. En este cuaderno usamos un relato inventado, rotulado así, para practicar.",
        "Interpretar un mito es crear tu propia imagen de él. No es copiar un dibujo ya hecho. Elige un solo momento de la historia, decide qué quieres mostrar y escoge colores y formas. Dos personas pueden interpretar el mismo mito de maneras muy distintas y ambas pueden estar bien. Los mitos de los pueblos originarios los cuentan sus comunidades, y se tratan con respeto.",
    ],
    [("mito", "relato antiguo que explica algo del mundo"), ("fuente", "persona, libro o comunidad de donde viene un relato"), ("interpretar", "crear mi propia imagen o idea de algo"), ("momento", "una escena elegida de una historia"), ("dios", "ser poderoso en que cree una cultura, que cuida algo del mundo")],
    [
        w("Elegir un momento", "Relato inventado: «El Cerro que Soñaba con el Mar». Un cerro muy viejo soñaba con el mar. Cada noche suspiraba y salía niebla por sus laderas. Una mañana la niebla bajó a la playa y se hizo la primera ola. ¿Qué momento eliges para dibujar?", ["Veo tres momentos: el cerro soñando, la niebla en las laderas y la niebla convertida en ola.", "Elijo el segundo: la niebla subiendo por las laderas.", "Pienso en colores: grises y azules suaves."], "La niebla que sale por las laderas del cerro"),
        w("Identificar la fuente", "Una amiga te cuenta un mito y no sabes de dónde lo sacó. ¿Qué haces antes de dibujarlo?", ["Le pregunto dónde lo escuchó o leyó.", "Si no lo sabe, lo anoto como «relato sin fuente conocida».", "No digo que sea de un pueblo en particular."], "Preguntar por la fuente y no atribuirlo a nadie sin saber"),
    ],
    [
        m("Decir que un mito es de un pueblo sin saber de dónde viene.", "Se mezclan relatos y se puede faltar el respeto a una cultura.", "Pregunta por la fuente y, si no la conoces, dilo."),
        m("Copiar la ilustración de un libro y decir que es tu interpretación.", "No se toma ninguna decisión propia.", "Elige un momento y crea tus propias formas y colores."),
    ],
    [
        ex("Relato inventado: un cerro suspiraba cada noche y salía niebla por sus laderas. ¿Qué salía por las laderas?", "Niebla", "El texto dice que salía niebla."),
        ex("En el mismo relato, la niebla bajó a la playa y se hizo… ¿qué?", "La primera ola", "La última escena del relato es la niebla hecha ola."),
        ex("Según la clase, en los mitos de la antigua Grecia, ¿de qué es dios Poseidón?", "Del mar", "La clase dice que Poseidón es el dios del mar."),
    ],
    [
        ex("¿Qué es un mito? A: un relato antiguo que explica algo del mundo. B: un tipo de pincel. C: una foto.", "A", "Un mito explica el origen o la forma de algo en el mundo."),
        ex("¿Qué significa identificar la fuente de un mito? A: saber quién lo cuenta y de dónde viene. B: pintarlo de un solo color.", "A", "La fuente es la persona, libro o comunidad de donde viene el relato."),
        ex("Dos niños interpretan el mismo mito con dibujos muy distintos. ¿Es posible que ambos estén bien?", "Sí", "Cada uno crea su propia imagen."),
    ],
    [
        ex("Relato: un cerro soñaba con el mar, suspiraba y salía niebla, y la niebla se hizo ola. ¿Cuántos momentos se cuentan?", "3", "Soñar, salir la niebla y hacerse ola son tres momentos."),
        ex("Quieres mostrar el momento en que la niebla se hace ola. ¿Dibujas el cerro soñando de noche o la niebla en la playa?", "La niebla en la playa", "Ese es el lugar donde ocurre ese momento."),
        ex("Tu docente te cuenta un mito y dice «lo leí en un libro de relatos». Te muestra el título y el nombre de quien lo escribió. ¿Tiene fuente identificada?", "Sí", "Se conocen el libro y quien lo escribió."),
    ],
    [
        ex("Sara dice: «Este mito es de todos los pueblos de Chile». ¿Es correcto decirlo sin saber de dónde viene?", "No", "Sin conocer la fuente no se puede atribuir el mito a un pueblo."),
        ex("Tomás copió una ilustración de un libro y dijo «es mi interpretación». ¿Qué le falta?", "Una decisión propia", "Interpretar es crear algo con decisiones propias."),
    ],
    [
        ex("En el relato inventado, ¿qué colores usarías para la niebla si quieres mostrar suavidad: grises claros o rojo intenso?", "Grises claros", "Los grises claros se relacionan con suavidad."),
        ex("Quieres dibujar un solo momento. Entre «el cerro soñando de noche» y «todo el relato completo en un dibujo», ¿cuál sigue la regla de elegir un solo momento?", "El cerro soñando de noche", "La clase dice que se elige una sola escena."),
    ],
    ex("Una persona mayor que conoces te cuenta un relato sobre un cerro de su zona. Quieres dibujarlo. ¿Qué es lo primero: dibujar o preguntar de dónde viene el relato?", "Preguntar de dónde viene", "Primero hay que identificar la fuente."),
    [
        ex("¿Qué debes decidir al interpretar un mito: el momento, los colores o ambos?", "Ambos", "Se elige un momento y los recursos para mostrarlo."),
        ex("Verdadero o falso: se puede decir que un relato es de un pueblo sin saber de dónde viene.", "Falso", "Primero se identifica la fuente."),
        ex("¿Cómo se llama el relato antiguo que explica algo del mundo?", "Mito", "Esa es la definición de mito."),
    ],
    task(
        "Lee el relato inventado «El Cerro que Soñaba con el Mar»: un cerro viejo soñaba con el mar, suspiraba cada noche y salía niebla por sus laderas, y una mañana la niebla bajó y se hizo la primera ola. Elige UN momento y haz tu dibujo. Escribe: cuál momento elegiste, qué colores usaste y que el relato es inventado para este cuaderno. Si tu docente te entrega un mito real con su fuente, puedes hacer la misma tarea con ese mito.",
        "Elegí el momento en que la niebla sube por las laderas. Usé grises y azules suaves. Mi relato es inventado para este cuaderno.",
        ["elige un solo momento", "crea su propia imagen, sin copiar", "dice la fuente del relato", "explica un color o forma elegidos"],
        ["dibujo de un momento", "una frase con momento, colores y fuente"],
        ["dibujar todo el relato en una imagen", "no decir de dónde viene el relato"],
        "Reconoce la decisión propia y pregunta qué parte del relato quiso mostrar con sus colores.",
    ),
    "Cuéntale a alguien de tu casa un cuento que sepas, y dile de dónde lo sabes: de un libro, de alguien o de la escuela.",
    "Con tu docente, lee un mito con su fuente y compara en una frase cómo cambia lo que imaginas si lo cuenta otra persona.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hoja, lápiz de mina y lápices de colores. Usa los seres inventados de este cuaderno. Si tu docente trae seres de relatos reales, acompañados de su fuente, pueden usarse en la actividad.",
    "Aprenderé a imaginar seres de creencias, fiestas y tradiciones sin repetir ideas fijas sobre las culturas. Sirve para crear con respeto y con imaginación propia.",
    ["Sé que un mito es un relato antiguo con una fuente.", "Sé dibujar formas y mezclar partes de seres vivos."],
    [
        "Muchas culturas tienen seres imaginarios: criaturas que no existen en la vida real, pero que forman parte de sus relatos, creencias, fiestas y tradiciones. En Chiloé, por ejemplo, se cuentan relatos del Caleuche, un barco misterioso. Una fiesta o una tradición es algo que una comunidad repite y celebra cada cierto tiempo.",
        "Un estereotipo es una idea fija y simplificada sobre un grupo, como dibujar a todos los miembros de una cultura con la misma ropa o con los mismos adornos. Cada cultura es diversa y sus personas son distintas. Por eso, al imaginar seres culturales, no se debe resumir a un pueblo en un solo dibujo, ni burlarse de sus creencias.",
        "Para imaginar con respeto, parte de una fuente: un libro o la comunidad. Para crear un ser imaginario propio, puedes mezclar partes de animales o plantas y darle un rasgo particular. Por ejemplo, un pájaro con alas de hojas. Luego dile a qué relato o cultura se parece y qué cambiaste. Si no conoces la cultura, no pretendas que tu ser pertenece a ella: di que es inventado.",
    ],
    [("ser imaginario", "criatura que no existe en la vida real, pero aparece en relatos"), ("creencia", "idea que un grupo cree y cuida"), ("tradición", "costumbre que una comunidad repite con el tiempo"), ("estereotipo", "idea fija y simple sobre un grupo de personas"), ("diversidad", "muchas formas distintas dentro de un mismo grupo")],
    [
        w("Un ser inventado", "Quieres crear un ser inventado con partes de un pájaro y de un árbol. ¿Cómo lo describes?", ["Tomo alas de pájaro y las hago de hojas.", "Le pongo ramas como patas.", "Digo que es inventado y no de una cultura real."], "Pájaro de alas de hojas y patas de ramas, rotulado inventado"),
        w("Evitar un estereotipo", "Alguien dice: «Para dibujar a una cultura, hay que dibujar a todos con la misma ropa y los mismos adornos». ¿Qué está mal?", ["Todas las personas de una cultura no son iguales.", "Dibujar a todos igual es un estereotipo simplificado.", "Mejor pregunto a la comunidad o miro una fuente."], "Es un estereotipo; hay que usar una fuente y respetar la diversidad"),
    ],
    [
        m("Dibujar a todas las personas de una cultura con la misma ropa y adornos.", "Se repite una idea fija en vez de mirar la diversidad.", "Usa una fuente y muestra que las personas son distintas."),
        m("Decir que un ser que inventaste es de una cultura real.", "Se atribuye a un pueblo algo que no es suyo.", "Rotula tu ser como inventado y explica qué ideas usaste."),
    ],
    [
        ex("Según la clase, ¿qué ser misterioso se cuenta en relatos de Chiloé?", "El Caleuche", "La clase nombra al Caleuche como barco misterioso de Chiloé."),
        ex("Un ser inventado tiene alas de hojas y patas de ramas. ¿De qué materiales de la naturaleza son sus partes?", "Hojas y ramas", "El texto nombra hojas y ramas."),
        ex("Una fiesta es algo que una comunidad repite y celebra. ¿Es verdad? Responde sí o no.", "Sí", "La clase define las fiestas y tradiciones así."),
    ],
    [
        ex("¿Qué es un estereotipo? A: una idea fija sobre un grupo. B: un pincel. C: un color.", "A", "Un estereotipo repite una idea simple y fija."),
        ex("Un dibujo muestra a todos los miembros de un pueblo con la misma ropa y mismos adornos. ¿Muestra diversidad?", "No", "Todos son iguales en el dibujo."),
        ex("Un ser imaginario ¿existe en la vida real? Responde sí o no.", "No", "Los seres imaginarios aparecen en relatos, no en la vida real."),
    ],
    [
        ex("Mezclas partes de un pez y de un pájaro para crear un ser inventado. ¿Es un ser real o inventado?", "Inventado", "La mezcla es tuya y no existe en la vida real."),
        ex("Creas un ser con cuerpo de zorro y cola de helecho, y quieres decir de qué cultura es. No conoces ninguna. ¿Qué escribes?", "Que es inventado", "Si no conoces la cultura, lo correcto es decir que es un ser inventado."),
        ex("Dibujas un ser inventado con una raya de colores en cada pata. ¿Cuántos rasgos propios nombras si dices «alas de hojas, patas de ramas y rayas de colores»?", "3", "Se nombran alas, patas y rayas."),
    ],
    [
        ex("Julia dibuja una fiesta de un pueblo y a todos los pone iguales, con la misma cara y la misma ropa. ¿Qué podría cambiar para evitar el estereotipo?", "Mostrar personas distintas entre sí", "Cada persona de una cultura es diferente."),
        ex("Beto dice: «Me burlo del ser de otra cultura porque es raro». ¿Es respetuoso?", "No", "Las creencias de otras culturas se tratan con respeto."),
    ],
    [
        ex("Quieres un ser inventado de agua. Entre «gota con piernas y alas de pez» y «un dibujo igual a un ser de otra cultura», ¿cuál es tu propia creación?", "Gota con piernas y alas de pez", "Es una mezcla propia y no copia un ser conocido."),
        ex("Describes tu ser como «guardián de las semillas, mitad pájaro mitad árbol». ¿Cuántas partes de seres vivos mezcla: dos o tres?", "Dos", "Mezcla un pájaro y un árbol."),
    ],
    ex("En una fiesta de tu barrio, una persona mayor te cuenta un relato sobre un animal misterioso. Quieres dibujarlo para tu cuaderno. ¿Qué haces primero: dibujar o preguntar de qué se trata y de dónde viene?", "Preguntar de qué se trata y de dónde viene", "Primero hay que conocer la fuente para crear con respeto."),
    [
        ex("¿Se puede mezclar un pájaro con un árbol para crear un ser inventado?", "Sí", "Un ser inventado puede mezclar partes de seres vivos."),
        ex("Verdadero o falso: todas las personas de una cultura son iguales.", "Falso", "Hay diversidad dentro de cada cultura."),
        ex("¿Cómo rotulas un ser que inventaste?", "Como inventado", "Es importante decir que lo creaste tú."),
    ],
    task(
        "Crea un ser imaginario inventado. Elige UNA mezcla: A) pájaro con alas de hojas; B) pez con patas de ramas; C) zorro con cola de helecho. Dibújalo con al menos dos rasgos propios (color, textura o forma). Escribe: que es inventado, qué partes mezcló y por qué. No lo atribuyas a ninguna cultura. Si tu docente trae un ser de un relato real con su fuente, puedes hacer otra versión anotando la fuente.",
        "Elegí el pez con patas de ramas. Le puse escamas verdes como hojas y una cola larga. Es un ser inventado. Mezclé un pez con un árbol porque el agua y el bosque me gustan.",
        ["mezcla al menos dos partes de seres vivos", "agrega rasgos propios", "dice que es inventado", "no lo atribuye a una cultura real"],
        ["dibujo del ser", "una frase de explicación"],
        ["decir que es de un pueblo sin fuente", "copiar un ser que ya existe"],
        "Reconoce los rasgos propios y pide que diga cuáles ideas tomó y cuáles inventó.",
    ),
    "Cuéntale a alguien de tu casa sobre un ser inventado. Cuéntale por qué es tuyo y no de una cultura.",
    "Con tu docente, escucha el relato real de un ser cultural con su fuente. Escribe una diferencia entre ese ser y el que inventaste.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hoja, lápiz de mina y lápices de colores. Las obras de este cuaderno son descripciones inventadas, rotuladas así. El docente puede mostrar imágenes reales de arte antiguo y de arte chileno con su autor o procedencia.",
    "Aprenderé a mirar arte muy antiguo y arte de Chile, y a tomar una idea para crear algo propio sin copiar. Sirve para conocer cómo se ha hecho arte y cuidar lo que nos dejaron.",
    ["Sé mirar una obra y nombrar sus colores y materiales.", "Sé que inspirarse no es copiar."],
    [
        "El arte de la Antigüedad es el que se hizo hace muchísimo tiempo, en culturas muy antiguas. Por ejemplo, el arte rupestre se pintó en paredes de cuevas con pigmentos de tierra, y muestra animales y manos. En el Antiguo Egipto se pintaron personas con la cabeza de perfil y el ojo dibujado de frente. En la antigua Grecia se hicieron vasijas de cerámica con figuras que forman franjas.",
        "El arte chileno incluye la pintura y también la artesanía, es decir, objetos hechos a mano con materiales y técnicas tradicionales, como las ollas de greda de Pomaire, los tejidos hechos en telar y las arpilleras, que son telas cosidas con imágenes. La obra y la artesanía se cuidan y se valoran porque son parte de nuestro patrimonio.",
        "Dialogar con una obra es mirarla con atención y responderle con tu propia idea. Mira su material, su forma y su color. Luego toma una idea, como las figuras en franja de una vasija, y úsala de otro modo, por ejemplo con animales de tu barrio. No copies la obra: tu respuesta es otra obra. Las obras de este cuaderno son inventadas; las reales las aporta tu docente.",
    ],
    [("arte de la Antigüedad", "arte hecho hace muchísimo tiempo por culturas antiguas"), ("arte rupestre", "pinturas en paredes de cuevas hechas hace mucho tiempo"), ("artesanía", "objeto hecho a mano con técnicas tradicionales"), ("dialogar con una obra", "mirarla bien y responderle con mi propia idea"), ("patrimonio", "lo que recibimos de antes y cuidamos")],
    [
        w("Mirar una vasija inventada", "Obra A (inventada): una vasija de cerámica con una franja de figuras de animales que corren, en negro sobre naranja. ¿Qué idea tomas para tu obra?", ["Miro la franja de figuras que se repiten.", "Tomo esa idea de franja y repetición.", "Dibujo una franja de gatos de mi barrio, no animales de la vasija."], "La franja con figuras repetidas, con animales de mi barrio"),
        w("Comparar dos obras", "Obra B (inventada): una pintura rupestre con manos y animales en rojo. Obra C (inventada): una olla de greda redonda de color tierra. ¿Qué tienen en común?", ["Obra B: pigmentos de tierra rojos.", "Obra C: greda de color tierra.", "Las dos usan colores de la tierra."], "Usan colores de tierra"),
    ],
    [
        m("Copiar la vasija igual y decir que es una obra tuya.", "No hay respuesta propia ni decisión personal.", "Toma una idea, como la franja, y cámbiala con tus propias figuras."),
        m("Pensar que la artesanía no es arte.", "Se valora más lo que se llama pintura.", "La artesanía es creación hecha a mano y forma parte del patrimonio."),
    ],
    [
        ex("Obra A (inventada): vasija con una franja de animales corriendo, negro sobre naranja. ¿Qué forma tiene la decoración: una franja o un círculo?", "Una franja", "El texto dice que la decoración es una franja."),
        ex("Obra B (inventada): una pintura rupestre con manos y animales en rojo. ¿Dónde se pintó este tipo de arte: en una cueva o en el cielo?", "En una cueva", "Las pinturas rupestres se hacen en paredes de cuevas."),
        ex("Las ollas de Pomaire se hacen de greda. ¿La greda es una arcilla? Responde sí o no.", "Sí", "La greda es una arcilla."),
    ],
    [
        ex("¿Qué es artesanía? A: un objeto hecho a mano con técnicas tradicionales. B: una foto en el celular. C: un tipo de lápiz.", "A", "La artesanía se hace a mano con materiales y técnicas tradicionales."),
        ex("Dialogar con una obra es mirarla bien y… ¿qué? A: responderle con mi idea. B: copiarla igual.", "A", "Dialogar es responder con una creación propia."),
        ex("Una arpillera es una tela cosida con imágenes. ¿Qué material principal tiene: tela o greda?", "Tela", "La definición dice que es una tela cosida."),
    ],
    [
        ex("Tomas de la vasija la idea de la franja y la haces con peces de río. ¿Copiaste o respondiste con una idea propia?", "Respondí con una idea propia", "Cambiaste las figuras y usaste solo la idea de la franja."),
        ex("Quieres usar la idea de manos en rojo de una pintura rupestre. Entre «dibujar tus manos con lápiz rojo en una hoja» y «raspar la pared de una cueva», ¿cuál es seguro?", "Dibujar tus manos con lápiz rojo en una hoja", "No se debe dañar ningún lugar; se trabaja en papel."),
        ex("Obra C (inventada): olla de greda redonda, de color tierra. ¿Qué forma básica tiene?", "Redonda", "El texto dice que es redonda."),
    ],
    [
        ex("Luis copió una olla de greda en su hoja y dijo «es mi diálogo con la obra». ¿Qué le falta?", "Una idea propia que cambie algo", "Dialogar es responder, no copiar tal cual."),
        ex("Andrea dice: «La arpillera es una obra importante aunque sea de tela». ¿Tiene razón?", "Sí", "La artesanía en tela también es patrimonio y creación."),
    ],
    [
        ex("Obra A (inventada) usa solo colores de tierra y obra B (inventada) usa solo colores muy brillantes. ¿Comparten sus colores?", "No", "Uno es de tierra y el otro brillante, así que no coinciden."),
        ex("Ordena de más antiguo a más reciente, según lo que sabes: A una pintura rupestre en una cueva, B un dibujo que hiciste hoy.", "A, B", "El arte rupestre se hizo hace muchísimo tiempo."),
    ],
    ex("En tu barrio hay un mural con una franja de peces en la pared del colegio. Quieres responderle con tu obra. ¿Qué haces: copiar el mural o tomar la idea de la franja y usarla con tus propias figuras?", "Tomar la idea de la franja y usarla con mis figuras", "Dialogar es responder con una creación propia."),
    [
        ex("¿Dónde se pintó el arte rupestre?", "En paredes de cuevas", "Esa es la definición del arte rupestre."),
        ex("Verdadero o falso: copiar una obra tal cual es una respuesta propia.", "Falso", "La respuesta propia agrega algo nuevo."),
        ex("¿La greda es el material de las ollas de Pomaire?", "Sí", "Las ollas de Pomaire se hacen con greda."),
    ],
    task(
        "Elige UNA obra inventada: A) una vasija con una franja de animales corriendo; B) una pintura rupestre con manos y animales en rojo; C) una olla de greda redonda con líneas hechas con un palito. Toma UNA idea de la obra (franja, mano o línea). Haz tu propia obra en papel con esa idea y figuras tuyas. Escribe qué idea tomaste, qué cambiaste y qué materiales usaste. Tu docente puede mostrarte una obra real de arte antiguo o chileno para comparar.",
        "Elegí la vasija. Tomé la idea de la franja. En vez de animales corriendo dibujé peces de mi río. Usé lápiz negro y naranja.",
        ["nombra la obra elegida", "toma una sola idea", "cambia algo y crea figuras propias", "dice los materiales usados"],
        ["obra propia", "tres frases: idea, cambio y materiales"],
        ["copiar la obra igual", "tomar todo y no cambiar nada"],
        "Reconoce la idea tomada y pide que muestre qué parte es completamente suya.",
    ),
    "Con tu docente, mira una artesanía chilena y di en voz alta de qué material es y cómo está decorada.",
    "Compara una obra antigua y una artesanía chilena en dos frases: qué se parece y qué es distinto.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA1, 6,
    "Hoja grande, lápices de colores o témperas, un pincel y un lápiz de mina. Las obras de este cuaderno son descripciones inventadas. El docente puede mostrar imágenes reales de fauvismo, expresionismo y art nouveau con su autor.",
    "Aprenderé qué son el fauvismo, el expresionismo y el art nouveau, y crearé una obra personal con ideas de la naturaleza, de la cultura y del arte. Sirve para juntar distintas ideas sin copiar.",
    ["Sé observar la naturaleza con detalle.", "Sé elegir un propósito expresivo y recursos para lograrlo."],
    [
        "Hace más de cien años, en Europa, algunos artistas formaron movimientos artísticos: grupos que compartían ideas sobre cómo hacer arte. El fauvismo usa colores muy intensos y no reales, por ejemplo un árbol rojo y un cielo verde, con pinceladas visibles. El expresionismo muestra emociones fuertes con formas deformadas y líneas marcadas. El art nouveau usa líneas curvas largas, como tallos, y formas de plantas y flores en objetos y construcciones.",
        "Una obra personal puede juntar tres referentes: uno de la naturaleza, uno de la cultura y uno del arte. Por ejemplo: observas una hoja de helecho (naturaleza), tomas la idea de una franja de figuras de una vasija (cultura) y usas líneas curvas largas como en el art nouveau (arte). Así creas algo nuevo y no una copia.",
        "Antes de empezar, decide tu propósito expresivo y anota qué tomaste de cada referente. Después de terminar, explica con tus palabras qué decidiste tú. Cuidar el patrimonio significa respetar las obras: no las rayamos ni las dañamos, y decimos de quién son. Las obras de este cuaderno son inventadas y no pertenecen a artistas reales.",
    ],
    [("movimiento artístico", "grupo de artistas con ideas parecidas sobre cómo hacer arte"), ("fauvismo", "movimiento que usa colores muy intensos y no reales"), ("expresionismo", "movimiento que muestra emociones fuertes con formas deformadas"), ("art nouveau", "movimiento de líneas curvas y formas de plantas"), ("referente", "obra o cosa que miro para tomar una idea")],
    [
        w("Reconocer un movimiento", "Obra D (inventada): un paisaje con árboles rojos, cielo verde y pinceladas visibles. ¿A qué movimiento se parece?", ["Veo colores intensos y no reales.", "Veo pinceladas visibles.", "Eso describe el fauvismo."], "Se parece al fauvismo"),
        w("Combinar tres referentes", "Quieres juntar: una hoja de helecho (naturaleza), una franja de figuras (cultura) y líneas curvas largas (art nouveau). ¿Cómo lo haces?", ["Dibujo la hoja de helecho con líneas curvas largas.", "Hago una franja de hojitas repetidas en el borde.", "Anoto los tres referentes."], "Helecho con líneas curvas y una franja de hojitas"),
    ],
    [
        m("Copiar una obra de un movimiento y decir que es mía.", "No hay decisión propia ni mezcla de referentes.", "Toma ideas de varios referentes y agrégales tus propias decisiones."),
        m("Pensar que todos los árboles deben pintarse de su color real.", "Se piensa que el arte solo copia lo que se ve.", "El arte puede usar colores no reales para expresar algo, como en el fauvismo."),
    ],
    [
        ex("Obra D (inventada): árboles rojos, cielo verde y pinceladas visibles. ¿Qué movimiento describe mejor?", "Fauvismo", "El fauvismo usa colores intensos y no reales."),
        ex("Obra E (inventada): una cara alargada con la boca muy abierta, líneas gruesas y fondo ondulado. ¿Qué muestra principalmente?", "Una emoción fuerte", "El expresionismo muestra emociones con formas deformadas."),
        ex("Obra F (inventada): una reja de metal con tallos curvos y flores. ¿Qué líneas predominan?", "Líneas curvas", "El texto dice que son tallos curvos."),
    ],
    [
        ex("¿Qué movimiento usa líneas curvas largas y formas de plantas? A: fauvismo. B: expresionismo. C: art nouveau.", "C", "El art nouveau usa líneas curvas y formas de plantas."),
        ex("¿Qué es un referente? A: algo que miro para tomar una idea. B: un tipo de pincel.", "A", "Un referente es lo que se mira para tomar una idea."),
        ex("Un pintor pinta una vaca azul y un pasto naranja para expresar alegría. ¿Usó colores reales o no reales?", "No reales", "Una vaca azul y un pasto naranja no son colores reales."),
    ],
    [
        ex("Tu obra mezcla una hoja de helecho, una franja de figuras y líneas curvas largas. ¿Cuántos referentes juntaste?", "3", "Son tres: naturaleza, cultura y arte."),
        ex("Quieres mostrar una emoción muy fuerte con una cara deformada y líneas marcadas. ¿Qué movimiento te sirve de referente?", "Expresionismo", "Muestra emociones fuertes con formas deformadas."),
        ex("Quieres decorar una puerta con formas de flores y tallos curvos. ¿Qué movimiento te sirve de referente?", "Art nouveau", "Usa líneas curvas y formas de plantas."),
    ],
    [
        ex("Carla copió una obra expresionista y dijo «es mía porque la hice con mis lápices». ¿Qué le falta?", "Una decisión propia", "No cambió ni creó nada propio."),
        ex("Rodrigo dice: «Si pinto el cielo verde, lo hice mal». ¿Es correcto según el fauvismo?", "No", "El fauvismo permite colores no reales para expresar."),
    ],
    [
        ex("En una obra personal anotas: naturaleza = caracol, cultura = franja de figuras, arte = colores del fauvismo. ¿Qué referente es el del arte?", "Los colores del fauvismo", "El referente de arte es el movimiento artístico."),
        ex("Si tu obra no dice de quién son las ideas que tomaste, ¿cumple con cuidar el patrimonio?", "No", "Hay que decir de dónde vienen las ideas."),
    ],
    ex("Tu docente te muestra tres imágenes: una con colores intensos y no reales, otra con una cara deformada y una tercera con tallos curvos en una reja. ¿Cuál se relaciona con el fauvismo?", "La de colores intensos y no reales", "El fauvismo se caracteriza por colores intensos y no reales."),
    [
        ex("¿Cuál movimiento usa colores intensos y no reales?", "Fauvismo", "Esa es la característica del fauvismo."),
        ex("Verdadero o falso: se puede tomar una idea de una obra y cambiarla.", "Verdadero", "Esa es la idea de inspirarse."),
        ex("¿Los tres referentes de tu obra personal son de la naturaleza, la cultura y el arte?", "Sí", "La clase propone ese tipo de mezcla."),
    ],
    task(
        "Crea tu obra personal. Elige UN referente de cada tipo. Naturaleza: A) hoja de helecho; B) caracol; C) olas. Cultura: A) franja de figuras de una vasija; B) manos de pintura rupestre; C) un ser inventado. Arte: A) colores del fauvismo; B) emoción fuerte del expresionismo; C) líneas curvas del art nouveau. Haz una obra con los tres. Escribe qué tomaste de cada uno, tu propósito expresivo y qué decidiste tú. Las obras reales las aporta tu docente.",
        "Elegí caracol, franja de figuras y líneas curvas del art nouveau. Mi propósito es calma. Dibujé una franja de caracoles con espirales suaves y colores claros. Yo decidí los colores y la cantidad de caracoles.",
        ["usa un referente de cada tipo", "dice qué tomó de cada uno", "dice su propósito", "agrega decisiones propias"],
        ["obra personal", "frases: referentes, propósito y decisiones"],
        ["copiar un referente completo", "no decir qué tomó de cada uno"],
        "Reconoce una decisión propia y pide que muestre cómo cada referente aparece en la obra.",
    ),
    "Con tu docente, mira una imagen real de arte y di en voz alta si se parece más al fauvismo, al expresionismo o al art nouveau, y por qué.",
    "Cambia solo el color de tu obra a colores muy intensos y no reales. Anota si cambió lo que expresa.",
)

# ================================================================ OA 02
# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Lápices de colores o témperas rojo, naranja, amarillo, azul, verde y violeta, y hojas. Si no tienes esos colores, usa objetos de esos colores o los nombres escritos en este cuaderno.",
    "Aprenderé a distinguir los colores cálidos de los fríos y a usarlos en un dibujo. Sirve para dar a mis trabajos la sensación que quiero.",
    ["Sé nombrar los colores básicos.", "Sé mezclar dos colores en una hoja."],
    [
        "Los colores se pueden agrupar por la sensación que producen. Los colores cálidos son el rojo, el naranja y el amarillo. Se parecen al fuego, al sol y a la luz, y parecen acercarse a quien los mira. Los colores fríos son el azul, el verde y el violeta. Se parecen al agua, al cielo y a la sombra, y parecen alejarse.",
        "Un dibujo puede tener más colores cálidos, más colores fríos o una mezcla de ambos. Si una zona es de colores cálidos y otra de colores fríos, se nota un contraste, es decir, una diferencia fuerte. Por ejemplo, un sol naranja sobre un mar azul. La temperatura del color se llama así porque el color nos hace sentir calor o frío, aunque el papel no cambie su temperatura.",
        "Los colores se pueden mezclar: el amarillo con el azul da verde, y el rojo con el amarillo da naranja. Pero cuidado: los colores no siempre tienen una temperatura fija. Un verde amarillento se siente más cálido que un verde azulado. Y además, cada persona y cada cultura pueden sentir cosas distintas con un color, así que explica siempre por qué lo elegiste.",
    ],
    [("color cálido", "rojo, naranja y amarillo; parecen acercarse"), ("color frío", "azul, verde y violeta; parecen alejarse"), ("contraste", "diferencia fuerte entre dos cosas"), ("temperatura del color", "sensación de calor o frío que da un color"), ("mezcla", "unir dos colores para obtener otro")],
    [
        w("Clasificar colores", "Tienes los colores: rojo, azul, amarillo, violeta, naranja y verde. ¿Cuáles son cálidos y cuáles fríos?", ["Cálidos: rojo, naranja y amarillo.", "Fríos: azul, verde y violeta."], "Cálidos: rojo, naranja, amarillo. Fríos: azul, verde, violeta"),
        w("Hacer un contraste", "Quieres un contraste fuerte entre un sol y un mar. ¿Qué colores eliges?", ["Para el sol elijo un color cálido, naranja.", "Para el mar elijo un color frío, azul.", "Entre cálido y frío hay un contraste fuerte."], "Sol naranja y mar azul"),
    ],
    [
        m("Pensar que el verde siempre es frío.", "Un verde con mucho amarillo se siente más cálido.", "Mira si tiene más amarillo (más cálido) o más azul (más frío)."),
        m("Pensar que un color significa lo mismo para todas las personas.", "Cada persona y cultura puede sentir cosas distintas.", "Explica qué sientes tú y por qué elegiste ese color."),
    ],
    [
        ex("Entre rojo y azul, ¿cuál es un color cálido?", "Rojo", "El rojo es uno de los colores cálidos."),
        ex("Entre verde y naranja, ¿cuál es un color frío?", "Verde", "El verde es uno de los colores fríos."),
        ex("Un sol amarillo sobre un mar azul. ¿Qué color es frío: el del sol o el del mar?", "El del mar", "El azul es frío."),
    ],
    [
        ex("¿Qué es un contraste? A: una diferencia fuerte. B: un tipo de lápiz. C: una mezcla de cuatro colores.", "A", "Contraste es una diferencia notoria entre dos cosas."),
        ex("Un dibujo tiene solo azul, verde y violeta. ¿Es de colores cálidos o fríos?", "Fríos", "Los tres son colores fríos."),
        ex("Quieres un fuego en tu dibujo. ¿Qué colores usarías: cálidos o fríos?", "Cálidos", "El fuego se parece al rojo, naranja y amarillo."),
    ],
    [
        ex("Mezclas amarillo con azul y obtienes verde. Si el verde tiene más amarillo que azul, ¿se siente más cálido o más frío?", "Más cálido", "El amarillo es un color cálido."),
        ex("Quieres un contraste fuerte entre una casa y su fondo. La casa es naranja. ¿De qué color pintas el fondo: rojo o azul?", "Azul", "El azul es frío y hace contraste con un naranja cálido."),
        ex("Pintas un cielo de invierno. Eliges entre azul con violeta y naranja con rojo. ¿Cuál es el grupo frío?", "Azul con violeta", "Ambos son colores fríos."),
    ],
    [
        ex("Nico pintó un cubo de hielo con rojo y naranja. Quería que se sintiera frío. ¿Qué colores debería usar?", "Fríos, como azul y violeta", "Esos colores producen sensación de frío."),
        ex("Rita dice: «El verde siempre es frío». ¿Es cierto en esta clase?", "No", "Un verde con mucho amarillo se siente más cálido."),
    ],
    [
        ex("Un dibujo tiene 3 colores cálidos y 2 colores fríos. ¿Predominan los cálidos o los fríos?", "Los cálidos", "Hay 3 cálidos contra 2 fríos."),
        ex("Quieres un cuadro con dos zonas: una cálida y una fría. Eliges naranja y azul. ¿Hay contraste?", "Sí", "Un cálido y un frío producen contraste."),
    ],
    ex("Imagina que quieres pintar la lluvia sobre un bosque con una sensación de frío. ¿Qué grupo de colores eliges: cálidos o fríos?", "Fríos", "Los colores fríos dan sensación de frío."),
    [
        ex("¿Cuáles son los tres colores cálidos?", "Rojo, naranja y amarillo", "Esos son los colores cálidos."),
        ex("Verdadero o falso: el violeta es un color frío.", "Verdadero", "El violeta es uno de los colores fríos."),
        ex("Un color frío ¿parece acercarse o alejarse?", "Alejarse", "Los colores fríos parecen alejarse."),
    ],
    task(
        "Elige UNA escena: A) un atardecer en el desierto; B) un lago bajo la lluvia; C) un campo con flores y un cielo azul. Pinta la escena usando colores cálidos y fríos con un contraste claro. Escribe qué zona es cálida y cuál fría, y qué sensación quiere dar tu dibujo.",
        "Elegí el atardecer en el desierto. El cielo es naranja y rojo (cálidos) y la sombra de los cerros es violeta (frío). Quiero dar sensación de calor, pero con un poco de frescura.",
        ["usa colores cálidos y fríos", "hay un contraste claro", "dice qué zona es cada una", "explica la sensación"],
        ["pintura de la escena", "dos frases de explicación"],
        ["mezclar todo y quedar café", "no explicar la sensación"],
        "Reconoce el contraste y pide que diga qué sensación logró con los colores.",
    ),
    "Mira alrededor de tu casa y di en voz alta tres objetos de colores cálidos y tres de colores fríos.",
    "Pinta la misma escena con solo colores cálidos y luego con solo fríos, y compara qué sensación cambia.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Hojas, lápices de colores o témperas y un pincel. Puedes usar las descripciones inventadas de este cuaderno para observar.",
    "Aprenderé a elegir un color según lo que quiero expresar, aunque no sea el color real de las cosas. Sirve para que mis trabajos muestren sentimientos e ideas propias.",
    ["Sé que hay colores cálidos y fríos.", "Sé que puedo tener un propósito expresivo."],
    [
        "Un color expresivo es un color que se elige para expresar un sentimiento o una idea, y no para copiar el color real de una cosa. Por ejemplo, puedes pintar un perro de azul para mostrar tristeza, o un cielo rojo para mostrar emoción. Los artistas del fauvismo hicieron esto: usaron colores intensos que no eran reales.",
        "Para elegir un color expresivo, sigue tres pasos. Primero piensa qué quieres expresar: alegría, calma, enojo, miedo. Segundo elige un color que, para ti, se relacione con eso. Tercero explica tu elección con una razón. Por ejemplo: «Pinté el cielo de naranja porque me hace sentir alegría».",
        "No hay un color correcto para cada sentimiento. Las personas y las culturas pueden relacionar los colores con ideas distintas, y los artistas deciden. Lo importante es que tu elección sea clara y que puedas explicar por qué lo elegiste. También puedes combinar varios colores, por ejemplo cálidos y fríos, para mostrar sentimientos mezclados.",
    ],
    [("color expresivo", "color elegido para expresar algo, no para copiar el color real"), ("color real", "el color que tiene una cosa en la vida"), ("sentimiento", "lo que siento por dentro, como alegría o miedo"), ("elección", "decisión que tomo entre varias opciones"), ("explicar", "dar una razón de por qué hice algo")],
    [
        w("Elegir un color expresivo", "Quieres mostrar alegría en un dibujo de un árbol. Para ti, el amarillo es alegre. ¿Cómo lo pintas?", ["Pienso en lo que quiero expresar: alegría.", "Elijo el amarillo, que para mí es alegre.", "Pinto el árbol de amarillo y explico por qué."], "Árbol amarillo, porque para mí el amarillo es alegre"),
        w("Cambiar el color real", "El cielo real es azul. Quieres mostrar miedo. ¿Qué haces?", ["Pienso en un color que me dé miedo, como el morado oscuro.", "Pinto el cielo de ese color, aunque no sea real.", "Explico que lo hice para mostrar miedo."], "Cielo morado oscuro, para mostrar miedo"),
    ],
    [
        m("Pensar que hay que pintar siempre los colores reales de las cosas.", "Se piensa que el arte solo copia la realidad.", "Puedes cambiar los colores para expresar algo y explicar tu elección."),
        m("Pensar que un color significa lo mismo para todos.", "Cada persona y cultura puede asociar colores con ideas distintas.", "Explica tu propia razón al elegir un color."),
    ],
    [
        ex("Un artista pinta un perro azul para mostrar tristeza. ¿El color es real o expresivo?", "Expresivo", "No es el color real del perro; lo eligió para expresar algo."),
        ex("Quieres mostrar alegría y eliges el amarillo porque para ti es alegre. ¿Qué diste: una razón personal o una regla para todos?", "Una razón personal", "Es tu propia explicación."),
        ex("Un cielo rojo para mostrar emoción. ¿El cielo real es rojo?", "No", "Se eligió el rojo para expresar algo, no para copiar."),
    ],
    [
        ex("¿Qué es un color expresivo? A: uno elegido para expresar algo. B: solo el color real. C: el color del papel.", "A", "Un color expresivo se elige para expresar algo."),
        ex("Ordena los pasos para elegir un color expresivo: A elegir el color, B explicar, C pensar qué expresar.", "C, A, B", "Primero piensas lo que quieres expresar, luego eliges y luego explicas."),
        ex("Una niña pinta el mar de naranja y rosado para mostrar tranquilidad. ¿Eligió colores reales?", "No", "El mar real suele verse azul o verde, no naranja ni rosado."),
    ],
    [
        ex("Quieres expresar enojo con un dibujo de un volcán. Entre azul claro y rojo intenso, ¿qué color eliges si para ti el rojo es enojo?", "Rojo intenso", "Lo elegiste porque para ti el rojo se relaciona con el enojo."),
        ex("Pintas el mar de color violeta para mostrar misterio. Alguien te pregunta por qué. ¿Qué respondes: «porque sí» o «porque para mí el violeta es misterioso»?", "Porque para mí el violeta es misterioso", "Una razón personal explica la elección."),
        ex("Quieres sentimientos mezclados: alegría y tristeza. ¿Cuántos colores usarías como mínimo: 1 o 2?", "2", "Necesitas al menos un color por sentimiento."),
    ],
    [
        ex("Mario pintó un caballo rosado y dice «lo hice mal porque no es un color real». ¿Tiene razón?", "No", "Un color expresivo no necesita ser real."),
        ex("Eva pintó un cielo amarillo y no explicó por qué. ¿Qué le falta a su trabajo?", "Una razón de su elección", "Se debe explicar por qué se eligió el color."),
    ],
    [
        ex("Un dibujo usa un sol verde, un mar naranja y un cielo rosado. ¿Son colores reales o no reales?", "No reales", "Ninguno es el color que esas cosas tienen en la vida."),
        ex("Un curso decide que para su afiche la alegría se muestra con colores intensos. ¿Cuál afiche cumple: uno con colores intensos o uno solo gris?", "Uno con colores intensos", "Cumple con la decisión del curso de usar colores intensos."),
    ],
    ex("Quieres pintar un perro café, pero quieres mostrar cuánto lo quieres. ¿Qué puedes hacer: pintarla de un color que te recuerde cariño y explicar por qué, o pintarla de gris sin pensar?", "Pintarla de un color que me recuerde cariño y explicar por qué", "Un color expresivo se elige para expresar algo."),
    [
        ex("¿Se puede pintar un cielo rojo?", "Sí", "En arte se pueden usar colores expresivos."),
        ex("Verdadero o falso: hay un solo color correcto para cada sentimiento.", "Falso", "Cada persona puede asociar colores distintos."),
        ex("¿Cómo se llama el color que se elige para expresar algo?", "Color expresivo", "Esa es la definición."),
    ],
    task(
        "Elige UN dibujo para pintar: A) un árbol; B) una casa; C) un gato. Elige UN sentimiento: alegría, calma, tristeza o miedo. Pinta el dibujo con colores no reales que expresen ese sentimiento. Escribe qué color elegiste y por qué, con una razón tuya.",
        "Elegí el gato y el sentimiento de calma. Pinté el gato de celeste y el fondo de verde claro porque para mí esos colores son tranquilos.",
        ["usa colores no reales", "elige un sentimiento", "explica con una razón propia"],
        ["pintura con colores expresivos", "una frase de explicación"],
        ["copiar colores reales", "explicar con «porque sí»"],
        "Reconoce la razón propia y pregunta qué sentimiento quiso mostrar.",
    ),
    "Piensa en una persona o animal que quieras y di en voz alta con qué color lo pintarías para mostrar cariño.",
    "Pinta el mismo dibujo con otro sentimiento y compara qué colores cambiaste.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Hojas, lápiz de mina, papeles de distintas superficies (liso, arrugado, de cartón corrugado), tela vieja y limpia, hojas secas caídas, y masa de sal o plasticina. Todo debe estar limpio y ser seguro.",
    "Aprenderé qué es una textura y la diferencia entre textura en plano (que se ve) y en volumen (que se toca). Sirve para que mis trabajos se vean y se sientan distintos.",
    ["Sé decir si algo es liso o áspero.", "Sé hacer líneas y puntos en una hoja."],
    [
        "La textura es cómo se ve o se siente la superficie de las cosas: lisa, áspera, suave, rugosa, blanda o dura. Hay dos tipos. La textura en plano es la que se dibuja o se imprime sobre una hoja plana. Se ve, pero al tocar el papel no se siente. La textura en volumen es la que se toca y se siente porque la superficie realmente es áspera, blanda o rugosa.",
        "Para dibujar una textura en plano puedes usar líneas, puntos o manchas: puntos juntos para una piel áspera, líneas largas para un pelaje suave. También puedes hacer un frottage: poner la hoja sobre una superficie con relieve, como una hoja seca, y frotar con un lápiz de mina para que aparezca la textura. En volumen, usas materiales con relieve: tela, cartón corrugado, arena pegada o plasticina marcada con un palito.",
        "Una obra puede combinar ambas texturas. Por ejemplo, un dibujo de un árbol con una corteza hecha por frottage y las hojas pegadas con papel arrugado. Al elegir una textura, piensa qué quieres expresar: una textura áspera puede comunicar fuerza, y una textura suave, calma, aunque cada artista decide.",
    ],
    [("textura", "cómo se ve o se siente la superficie de algo"), ("textura en plano", "textura que se dibuja sobre una superficie plana y solo se ve"), ("textura en volumen", "textura que se toca porque la superficie tiene relieve"), ("relieve", "parte que sobresale de una superficie"), ("frottage", "frotar un lápiz sobre una hoja puesta encima de una superficie con relieve")],
    [
        w("Textura en plano", "Quieres dibujar la piel áspera de un lagarto en una hoja plana. ¿Qué haces?", ["Uso puntos pequeños y juntos para la piel áspera.", "Como el papel queda plano, es una textura en plano."], "Puntos juntos; es textura en plano"),
        w("Textura en volumen", "Pegas arena sobre cartón para hacer un camino. ¿Qué tipo de textura es?", ["La arena sobresale y se puede tocar.", "Por eso es una textura en volumen."], "Textura en volumen"),
    ],
    [
        m("Pensar que la textura es el color.", "Se confunde cómo se ve la superficie con su color.", "La textura es cómo es la superficie, lisa o áspera, y no su color."),
        m("Pensar que dibujar puntos hace que el papel se sienta áspero.", "La textura dibujada solo se ve; no cambia el papel.", "Si quieres que se sienta, usa materiales con relieve."),
    ],
    [
        ex("Una lija se siente áspera al tocarla. ¿Es una textura que se ve o que se toca?", "Que se toca", "Tiene relieve real."),
        ex("Dibujas con puntos una piel áspera en una hoja lisa. ¿Qué tipo de textura es?", "En plano", "Se ve, pero la hoja sigue lisa."),
        ex("Pegas hojas secas sobre cartón. ¿Qué tipo de textura es?", "En volumen", "Las hojas sobresalen y se pueden tocar."),
    ],
    [
        ex("¿Qué es la textura? A: cómo se ve o se siente la superficie. B: el color. C: el tamaño.", "A", "La textura se refiere a la superficie."),
        ex("Frotas un lápiz de mina sobre una hoja puesta encima de una hoja seca y aparece su dibujo. ¿Cómo se llama esa técnica?", "Frottage", "El frottage es frotar sobre una superficie con relieve."),
        ex("Un cartón corrugado tiene líneas que sobresalen. ¿Qué tipo de textura tiene?", "En volumen", "Tiene relieve que se puede tocar."),
    ],
    [
        ex("Quieres una textura que se vea suave en un dibujo de una nube. ¿Usas líneas largas y suaves o puntos oscuros muy juntos?", "Líneas largas y suaves", "Las líneas largas dan una sensación suave."),
        ex("Quieres una textura en volumen para el tronco de un árbol. Entre cartón corrugado pegado y un dibujo con lápiz, ¿cuál sirve?", "Cartón corrugado pegado", "El cartón tiene relieve y se puede tocar."),
        ex("Tienes plasticina y un palito. Marcas pequeños hoyitos en ella. ¿Qué textura creaste: en plano o en volumen?", "En volumen", "Los hoyitos son relieve real."),
    ],
    [
        ex("Lola dibujó puntos en una hoja y dice «ahora la hoja es áspera al tocarla». ¿Tiene razón?", "No", "Los puntos dibujados se ven, pero la hoja sigue lisa."),
        ex("Pablo dijo «la textura en volumen solo se ve, no se toca». ¿Es correcto?", "No", "La textura en volumen se toca."),
    ],
    [
        ex("Haces un collage con una tela suave, cartón corrugado y papel lija. ¿Cuántas texturas en volumen distintas hay?", "3", "Son tres materiales con texturas distintas."),
        ex("Un dibujo de un tronco tiene líneas hechas con lápiz y trozos de cartón corrugado pegados. ¿Combina textura en plano y en volumen?", "Sí", "Las líneas son en plano y los trozos de cartón son en volumen."),
    ],
    ex("En tu casa tienes una hoja de árbol seca y limpia. Quieres su textura en una hoja de papel. ¿Qué haces: frotar con lápiz de mina sobre la hoja puesta bajo el papel o pintarla de verde?", "Frotar con lápiz de mina sobre la hoja bajo el papel", "El frottage reproduce la textura."),
    [
        ex("¿Cómo se llama la textura que se dibuja y solo se ve?", "Textura en plano", "Esa es la definición."),
        ex("Verdadero o falso: la textura en volumen se puede tocar.", "Verdadero", "Tiene relieve real."),
        ex("¿Qué es un relieve?", "Una parte que sobresale de una superficie", "Esa es la definición."),
    ],
    task(
        "Elige UNA cosa para mostrar su textura: A) la corteza de un árbol; B) la lana de una oveja; C) la piel de un lagarto. Haz DOS versiones: una en plano (con líneas, puntos o frottage) y otra en volumen (con cartón, tela, lana o masa). Escribe cuál de las dos se parece más a la textura real y por qué.",
        "Elegí la corteza. En plano hice frottage con una hoja seca. En volumen pegué cartón corrugado. Se parece más el cartón porque se siente áspero como la corteza.",
        ["hace una versión en plano", "hace una versión en volumen", "compara cuál se parece más", "explica con una razón"],
        ["dos muestras de textura", "una frase de comparación"],
        ["hacer solo una versión", "decir cuál es mejor sin razón"],
        "Reconoce la comparación y pide que diga qué cambió al pasar de plano a volumen.",
    ),
    "Toca tres cosas de tu casa y di en voz alta si su textura es lisa, áspera o suave, y por qué.",
    "Haz un frottage de tres superficies distintas de tu casa y anota cómo se ve cada una.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Hojas, lápiz de mina, una hoja de planta, una fruta o un objeto de tu casa, y un marco de papel. Si no puedes, usa las descripciones de este cuaderno.",
    "Aprenderé a observar las formas reales de las cosas y a dibujarlas con atención. Sirve para que mis dibujos muestren cómo son las cosas de verdad.",
    ["Sé dibujar círculos, cuadrados y triángulos.", "Sé observar con detalle."],
    [
        "La forma es el contorno de las cosas, es decir, la línea que las rodea. Una forma real es la forma que tiene una cosa de verdad. Una pelota es redonda, una hoja de limón es ovalada y una caja es un rectángulo. Para dibujar formas reales, observa el objeto y busca figuras simples que lo ayuden a dibujarlo: círculos, óvalos, rectángulos y triángulos.",
        "Existen formas geométricas, como círculos y cuadrados, que tienen medidas regulares. También hay formas orgánicas, como las de plantas y animales, que son irregulares y suaves. Una hoja tiene forma orgánica, y una caja tiene forma geométrica. Para dibujar una forma real, mira primero la forma completa, luego sus partes y al final los detalles.",
        "Si quieres comprobar tu dibujo, compara con el objeto: ¿se parece la forma de mi dibujo a la forma del objeto? Puedes usar un marco de papel para ver solo una parte. Dibujar formas reales no es copiar sin pensar: observas, decides qué incluir y cómo dibujarlo con tu estilo.",
    ],
    [("forma", "contorno de las cosas, la línea que las rodea"), ("forma real", "forma que una cosa tiene de verdad"), ("forma geométrica", "forma regular, como círculo o cuadrado"), ("forma orgánica", "forma irregular y suave, como la de plantas y animales"), ("contorno", "línea que rodea una forma")],
    [
        w("Buscar figuras simples", "Quieres dibujar una tetera con cuerpo redondo, tapa pequeña y asa curva. ¿Qué figuras simples usas?", ["El cuerpo es un círculo grande.", "La tapa es un círculo pequeño.", "El asa es una curva."], "Círculo grande, círculo pequeño y curva"),
        w("Geométrica u orgánica", "Una hoja de helecho y una caja de zapatos. ¿Cuál es orgánica y cuál geométrica?", ["La hoja de helecho es irregular y suave, por eso es orgánica.", "La caja es un rectángulo con medidas regulares, por eso es geométrica."], "La hoja es orgánica y la caja es geométrica"),
    ],
    [
        m("Dibujar la forma de una pelota como un cuadrado.", "No se observa su forma real.", "Mira el objeto: la pelota es redonda."),
        m("Dibujar una hoja con bordes rectos como una regla.", "Se usan formas geométricas para algo orgánico.", "Observa los bordes suaves e irregulares de la hoja."),
    ],
    [
        ex("¿Qué forma real tiene una pelota?", "Redonda", "Una pelota es redonda."),
        ex("Una hoja de limón es ovalada. ¿Es una forma geométrica o una forma orgánica?", "Orgánica", "Las plantas tienen formas orgánicas."),
        ex("Una caja de zapatos tiene la forma de un rectángulo. ¿Es geométrica? Responde sí o no.", "Sí", "El rectángulo es una forma geométrica."),
    ],
    [
        ex("¿Qué es una forma real? A: la que una cosa tiene de verdad. B: un color. C: una textura.", "A", "La forma real es la que tiene la cosa."),
        ex("Tetera: cuerpo redondo, tapa pequeña y asa curva. ¿Qué figura simple sirve para el cuerpo?", "Un círculo", "El cuerpo es redondo."),
        ex("¿Cómo se llama la línea que rodea una forma?", "Contorno", "Esa es la definición de contorno."),
    ],
    [
        ex("Quieres dibujar un caracol con concha redonda y cuerpo largo. ¿Qué figuras simples usas: círculo y óvalo largo o cuadrado y triángulo?", "Círculo y óvalo largo", "La concha es redonda y el cuerpo es largo."),
        ex("Un reloj tiene la forma de un círculo. Entre tres objetos, ¿cuál tiene también forma de círculo: una moneda, una caja o un libro?", "Una moneda", "La moneda es circular."),
        ex("Observas una zanahoria. ¿Qué figura simple se parece más a su forma: un triángulo largo o un círculo?", "Un triángulo largo", "La zanahoria es larga y termina en punta."),
    ],
    [
        ex("Una niña dibuja una naranja como un triángulo. ¿Qué forma real debería tener?", "Redonda", "Una naranja es redonda."),
        ex("Un niño dibuja una taza de memoria sin mirarla. ¿Está observando su forma real?", "No", "Observar exige mirar el objeto mientras se dibuja."),
    ],
    [
        ex("Un dibujo de un árbol usa un óvalo grande para la copa y un rectángulo largo para el tronco. ¿Cuántas formas simples usó?", "2", "Son el óvalo y el rectángulo."),
        ex("Quieres dibujar un gato dormido en una canasta redonda. ¿Qué figura simple sirve para la canasta?", "Un círculo", "La canasta es redonda."),
    ],
    ex("Quieres dibujar tu zapatilla, que tiene suela larga, parte de adelante redondeada y cordones. ¿Qué haces primero: dibujar los cordones o buscar la forma completa?", "Buscar la forma completa", "Primero se mira la forma completa y después los detalles."),
    [
        ex("¿Una caja es una forma orgánica o geométrica?", "Geométrica", "Tiene medidas regulares como el rectángulo."),
        ex("Verdadero o falso: observar es mirar bien un objeto antes de dibujarlo.", "Verdadero", "Eso es observar."),
        ex("¿Qué forma tiene una hoja de limón?", "Ovalada", "La clase la describe con forma ovalada."),
    ],
    task(
        "Elige UN objeto para dibujar: A) una fruta; B) una hoja de planta; C) un objeto de tu casa. Dibuja su forma real con figuras simples y luego con detalles. Escribe qué figuras simples usaste y si el objeto tiene forma geométrica u orgánica.",
        "Elegí una pera. Usé un círculo grande abajo y uno más chico arriba. Es una forma orgánica. Luego dibujé el cabito y las manchitas.",
        ["observa el objeto", "usa figuras simples", "dice si es geométrica u orgánica", "agrega detalles"],
        ["dibujo del objeto", "una frase con figuras y tipo de forma"],
        ["dibujar de memoria", "no decir qué figuras usó"],
        "Reconoce la forma lograda y pide que muestre qué parte observó con más atención.",
    ),
    "Mira tres objetos de tu casa y di en voz alta qué forma tienen: geométrica u orgánica.",
    "Dibuja el mismo objeto desde otro lado y anota cómo cambió su forma.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Hojas, lápices de colores, tijeras de punta redonda, papel de colores y un objeto de casa. Usa las descripciones inventadas de este cuaderno si no tienes los objetos.",
    "Aprenderé a recrear formas, es decir, a transformarlas con ideas mías sin calcarlas. Sirve para que mis dibujos muestren cómo veo yo las cosas.",
    ["Sé que hay formas reales y formas geométricas.", "Sé que inspirarme no es copiar."],
    [
        "Una forma recreada es una forma real que se cambia con la imaginación. Por ejemplo, una hoja real es ovalada, pero la puedes recrear alargando su punta, o hacerla con pedazos de papel. La forma recreada se parece a la real, pero tiene algo nuevo que decidiste tú. Calcar es copiar siguiendo las líneas de otra imagen. Recrear es otra cosa: tú decides qué cambiar.",
        "Hay varias maneras de recrear una forma. Simplificar: usar solo las figuras principales. Exagerar: hacer más grande o más larga una parte. Combinar: unir partes de dos formas, como un gato con cola de helecho. Repetir: dibujar la misma forma muchas veces con cambios. Cada cambio debe tener una razón: ¿qué quieres expresar?",
        "Recrear una forma ayuda a decir algo propio. Si exageras las orejas de un conejo, puedes mostrar que escucha mucho. Si simplificas un árbol a un triángulo y un rectángulo, puedes mostrar que lo más importante de él es su figura. Después de recrear, explica qué forma real tomaste y qué cambiaste.",
    ],
    [("forma recreada", "forma real transformada con ideas propias"), ("calcar", "copiar siguiendo las líneas de otra imagen"), ("simplificar", "dejar solo las partes más importantes"), ("exagerar", "hacer más grande o más largo algo"), ("combinar", "unir partes de dos cosas")],
    [
        w("Exagerar una parte", "Quieres recrear un conejo para mostrar que escucha mucho. ¿Qué cambias?", ["Observo la forma real del conejo.", "Exagero las orejas: las hago más largas.", "Explico que lo hice para mostrar que escucha mucho."], "Orejas más largas, para mostrar que escucha mucho"),
        w("Simplificar", "Un árbol real tiene muchísimas hojas. Quieres recrearlo con solo dos formas. ¿Cuáles?", ["Dejo solo lo importante.", "Uso un triángulo para la copa.", "Uso un rectángulo para el tronco."], "Un triángulo y un rectángulo"),
    ],
    [
        m("Calcar una foto y decir que es una forma recreada.", "No se toma ninguna decisión propia.", "Mira la forma real y cámbiala con una idea tuya."),
        m("Recrear sin una razón para los cambios.", "Los cambios no se relacionan con lo que se quiere expresar.", "Explica qué cambiaste y para qué."),
    ],
    [
        ex("Una forma recreada ¿es igual a la real o tiene algo cambiado?", "Tiene algo cambiado", "La forma recreada se transforma con ideas propias."),
        ex("Haces las orejas de un conejo más largas que las reales. ¿Qué hiciste: exagerar o simplificar?", "Exagerar", "Agrandaste una parte."),
        ex("Dibujas un árbol solo con un triángulo y un rectángulo. ¿Qué hiciste: simplificar o combinar?", "Simplificar", "Dejaste solo lo principal."),
    ],
    [
        ex("¿Qué es calcar? A: copiar siguiendo las líneas de otra imagen. B: inventar algo nuevo.", "A", "Calcar es copiar sobre las líneas."),
        ex("Dibujas un gato con la cola de un helecho. ¿Qué hiciste: combinar o repetir?", "Combinar", "Uniste partes de dos cosas."),
        ex("Dibujas la misma flor cinco veces cambiando el tamaño. ¿Qué hiciste: repetir o simplificar?", "Repetir", "Dibujaste la misma forma varias veces."),
    ],
    [
        ex("Quieres mostrar que un oso es fuerte. ¿Qué parte exageras: los brazos grandes o los ojos muy pequeños?", "Los brazos grandes", "Brazos grandes muestran fuerza."),
        ex("Tienes una hoja real ovalada. Alargas su punta y le agregas ondas al borde. ¿Es una forma real o recreada?", "Recreada", "Cambiaste la forma con ideas tuyas."),
        ex("Quieres recrear una casa solo con tres formas geométricas. Entre cuadrado, triángulo y círculo, ¿cuáles sirven para el cuerpo y el techo?", "Cuadrado y triángulo", "El cuadrado hace el cuerpo y el triángulo el techo."),
    ],
    [
        ex("Ema calcó una foto de un perro y dijo «es mi forma recreada». ¿Es correcto?", "No", "Calcar es copiar; recrear es cambiar con ideas propias."),
        ex("Raúl cambió la forma de un pez para que parezca un globo. ¿Qué debe explicar?", "Qué cambió y para qué", "Una forma recreada se explica."),
    ],
    [
        ex("Dibujas un pez con alas de pájaro. ¿Qué técnica usaste: combinar o simplificar?", "Combinar", "Uniste partes de dos seres distintos."),
        ex("Quieres recrear un caracol con espiral gigante y cuerpo diminuto. ¿Qué técnica usaste: exagerar o repetir?", "Exagerar", "Agrandaste una parte y achicaste otra."),
    ],
    ex("Quieres recrear el perro de tu vecino para un afiche de cuidado de mascotas. Sin calcar una foto, ¿qué haces: miras su forma y cambias una parte con una idea tuya, o copias una foto?", "Miro su forma y cambio una parte con una idea mía", "Recrear es transformar con ideas propias."),
    [
        ex("¿Cuál técnica deja solo las partes más importantes?", "Simplificar", "Simplificar es dejar lo principal."),
        ex("Verdadero o falso: calcar es lo mismo que recrear.", "Falso", "Calcar es copiar; recrear es cambiar con ideas propias."),
        ex("¿Qué técnica une partes de dos cosas?", "Combinar", "Combinar mezcla partes."),
    ],
    task(
        "Elige UNA forma real: A) un conejo; B) un árbol; C) un caracol. Observa su forma y recréala con UNA técnica: exagerar, simplificar o combinar. Dibuja la forma real y la forma recreada. Escribe qué técnica usaste, qué cambiaste y para qué. No calques.",
        "Elegí el conejo y exageré las orejas para mostrar que escucha mucho. Dibujé primero el conejo real y luego el recreado, con orejas muy largas.",
        ["dibuja la forma real", "dibuja la forma recreada", "usa una técnica y la nombra", "explica el cambio y su razón"],
        ["dos dibujos", "una frase con técnica, cambio y razón"],
        ["calcar la forma", "cambiar sin explicar"],
        "Reconoce el cambio y pregunta qué quiso expresar con él.",
    ),
    "Mira un objeto de tu casa y di en voz alta cómo lo recrearías exagerando una parte.",
    "Recrea la misma forma con otra técnica y compara cuál expresa mejor tu idea.",
)

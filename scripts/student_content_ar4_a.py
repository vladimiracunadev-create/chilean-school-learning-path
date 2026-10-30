"""Cuaderno del estudiante de 4.º básico Artes Visuales: AR04 OA 01 (creación con propósito desde naturaleza, cultura y arte) y AR04 OA 02 (color, textura y forma)."""
from __future__ import annotations

from student_lessons import ex, register

OA1 = "AR04 OA 01"
OA2 = "AR04 OA 02"


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
    "Una hoja, un lápiz de mina y lápices de colores. Para observar puedes usar un paisaje real (una plaza, un cerro, el cielo desde una ventana) o las descripciones escritas en este cuaderno.",
    "Aprenderé a hacer un registro de observación de un paisaje o de un fenómeno natural de América, con dibujo rápido y notas. Sirve para tener datos reales antes de crear una obra con un propósito.",
    ["Sé mirar la forma, el color, la textura, el tamaño y el movimiento de algo.", "Sé que un dibujo puede mostrar lo que siento y no solo lo que veo."],
    [
        "América tiene paisajes muy distintos: la cordillera de los Andes, que la recorre de norte a sur, desiertos, lagos, volcanes, glaciares y bosques con mucha lluvia. En Chile hay varios de ellos. Un fenómeno natural es algo que ocurre en la naturaleza sin que lo haga una persona, como el viento, la nieve, una erupción o la marea.",
        "Un registro de observación tiene tres partes. Primero, un croquis: un dibujo rápido, sin borrar, que muestra lo principal. Segundo, notas con los cinco aspectos que ya conoces: forma, color, textura, tamaño y movimiento. Tercero, una pregunta que te hiciste mientras mirabas. Se hace en este orden: croquis, notas y pregunta.",
        "Una nota de observación dice lo que se ve: «la cima tiene tres picos y nieve en los dos más altos». Una opinión dice lo que pienso: «es el cerro más lindo». Las opiniones sirven para decidir qué expresar, pero no reemplazan los datos. Si puedes, vuelve a mirar a otra hora: la luz cambia los colores y las sombras. Observa siempre cuidando el lugar, sin arrancar plantas ni dejar basura.",
    ],
    [("registro de observación", "dibujo rápido con notas sobre lo que veo"), ("croquis", "dibujo rápido y sin borrar que muestra lo principal"), ("paisaje", "parte de la naturaleza que se ve desde un lugar"), ("fenómeno natural", "algo que ocurre en la naturaleza sin que lo haga una persona"), ("opinión", "lo que pienso o siento sobre algo; no es un dato que se vea")],
    [
        w("Registro de un volcán", "Lees: «El volcán tiene forma de cono, con nieve arriba y roca oscura abajo. Sale un humo blanco que se inclina con el viento». Anota un dato de forma, uno de color y uno de movimiento.", ["Forma: la frase dice que es un cono.", "Color: nieve arriba y roca oscura abajo.", "Movimiento: el humo blanco se inclina con el viento."], "Forma: cono. Color: blanco arriba y oscuro abajo. Movimiento: humo inclinado"),
        w("Separar dato y opinión", "Un niño escribió: «El lago es hermoso y sus orillas tienen piedras redondas y grises». ¿Qué parte es un dato?", ["Busco lo que se puede ver y comprobar.", "«Hermoso» es lo que él piensa: es una opinión.", "«Piedras redondas y grises» se puede mirar y comprobar."], "El dato es «orillas con piedras redondas y grises»"),
    ],
    [
        m("Escribir solo «es lindo» como nota de observación.", "Una opinión no dice nada que se pueda dibujar.", "Escribe qué forma, color, textura, tamaño o movimiento ves."),
        m("Hacer el croquis de memoria y las notas después, en la casa.", "Se olvidan detalles y se mezclan con lo que uno imagina.", "Haz el croquis y las notas mientras miras el paisaje."),
    ],
    [
        ex("Lees: «El volcán tiene forma de cono, con nieve arriba y roca oscura abajo». ¿De qué color es la roca de abajo?", "Oscura", "La frase dice que abajo hay roca oscura."),
        ex("Un registro de observación tiene tres partes: croquis, notas y pregunta. ¿Cuál de ellas es un dibujo rápido?", "El croquis", "El croquis es el dibujo rápido y sin borrar."),
        ex("Anotas: «El río avanza rápido y hace espuma blanca entre las piedras». ¿Qué aspecto nombra la palabra «avanza»: el movimiento o la textura?", "El movimiento", "Avanzar es moverse, y el movimiento es uno de los cinco aspectos."),
    ],
    [
        ex("¿Cuál nota es una observación y no una opinión? A: «La montaña es la más linda». B: «La cima tiene una capa de nieve que cubre la parte de arriba».", "B", "La nota B dice algo que se puede mirar y comprobar."),
        ex("Miras un desierto al mediodía: se ve de color beige claro. Al atardecer se ve naranjo. ¿Qué cambió entre los dos momentos: el color o la forma de las dunas?", "El color", "Cambió la luz del día, y con ella el color que se ve."),
        ex("¿Cuál es una buena pregunta de observación? A: «¿Cuántas capas de colores tiene la roca?». B: «¿Qué hora es en otro país?».", "A", "La pregunta A se responde mirando mejor la roca."),
    ],
    [
        ex("Ordena las partes de un registro: A) anotar los cinco aspectos, B) escribir una pregunta, C) hacer un croquis. Escribe las tres letras en orden.", "C, A, B", "Primero se hace el croquis, luego se anotan los aspectos y al final la pregunta."),
        ex("En el croquis de un glaciar dibujas flechas que muestran hacia dónde baja el hielo. ¿Qué aspecto estás registrando con las flechas?", "El movimiento", "Las flechas muestran hacia dónde se mueve el hielo."),
        ex("Tu registro dice: «Forma: cono con punta. Color: gris con nieve. Textura: rugosa». Faltan dos de los cinco aspectos. ¿Cuáles?", "Tamaño y movimiento", "Están anotados forma, color y textura; faltan tamaño y movimiento."),
    ],
    [
        ex("Dos registros del mismo cerro. Lucas: «Hay un cerro con nieve». Rita: «Tiene tres picos, con nieve en los dos más altos y roca café en el tercero». ¿Con cuál registro puedes dibujar mejor sin volver a mirar el cerro?", "Con el de Rita", "Rita dice cuántos picos hay y dónde está la nieve; Lucas no da detalles."),
        ex("Una laguna se ve verde clara a las 9 de la mañana y gris oscura a las 6 de la tarde. Un compañero dice que la pintaron de otro color. Quieres comprobar si es cierto. ¿Qué haces: volver a mirarla a distintas horas y anotar los colores, o preguntarle a otro compañero qué cree?", "Volver a mirarla a distintas horas y anotar los colores", "Un registro se apoya en lo que se observa varias veces, no en lo que alguien cree."),
    ],
    [
        ex("En tu registro dice: «ladera muy empinada». Quieres mostrarlo en el croquis. ¿Dibujas la ladera con una línea casi vertical (parada) o casi horizontal (acostada)?", "Casi vertical", "Una ladera muy empinada sube mucho en poco espacio, y eso se ve como una línea casi parada."),
        ex("Quieres comparar dos paisajes: un desierto del norte de Chile y un bosque con mucha lluvia. Para el desierto anotaste: arena clara, superficie seca y casi nada se mueve. ¿Qué anotación hace un buen contraste: A) verde oscuro, hojas húmedas y ramas que se mueven; o B) beige, seca y quieta?", "A", "La opción A cambia color, textura y movimiento; la B repite lo del desierto."),
    ],
    ex("Estás en una plaza y quieres registrar la textura de un tronco de árbol sin dañarlo. ¿Qué haces: mirar la corteza de cerca y dibujar sus líneas o arrancar un trozo para llevártelo?", "Mirar la corteza de cerca y dibujar sus líneas", "El registro se hace observando el lugar y cuidándolo."),
    [
        ex("Verdadero o falso: «Es hermoso» es una nota de observación con detalle.", "Falso", "Es una opinión y no dice nada que se pueda dibujar."),
        ex("¿Cuáles son las tres partes de un registro de observación?", "Croquis, notas y pregunta", "Así se organiza un registro: primero dibujo, luego datos y luego una pregunta."),
        ex("Verdadero o falso: la luz de la mañana y la de la tarde pueden cambiar los colores que se ven en un paisaje.", "Verdadero", "La luz cambia durante el día y por eso cambian los colores."),
    ],
    task(
        "Elige UNA opción para tu registro: A) un cerro, árbol o planta que veas desde tu casa o en una plaza; B) el cielo con nubes; C) la siguiente escena escrita: «Un lago de agua verde, rodeado de montañas con nieve, con un volcán de punta al fondo; el viento mueve el agua en ondas pequeñas». Haz un croquis, escribe los cinco aspectos (forma, color, textura, tamaño y movimiento) y una pregunta.",
        "Elegí la opción C. Croquis: lago al centro, montañas alrededor y el volcán con punta al fondo. Forma: el volcán termina en punta. Color: lago verde y montañas con nieve arriba. Textura: el agua tiene ondas pequeñas. Tamaño: las montañas rodean al lago y el volcán se ve lejano. Movimiento: el viento mueve el agua. Pregunta: ¿se ve igual el lago por la tarde?",
        ["hace un croquis", "anota los cinco aspectos con datos y no solo opiniones", "escribe una pregunta de observación", "cuida el lugar que observa"],
        ["croquis", "cinco notas", "una pregunta"],
        ["escribir solo opiniones", "hacer el registro de memoria"],
        "Destaca la nota más precisa y pregunta qué dato del registro se podría usar después en una obra con un propósito.",
    ),
    "Mira por una ventana o desde tu patio durante un minuto. Di en voz alta tres datos que ves y una opinión; luego explica cuál es cuál.",
    "Haz el croquis del mismo lugar en dos momentos del día y anota qué cambió en los colores y en las sombras.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Hoja, lápiz de mina y lápices de colores o témpera. Para probar puedes usar tu registro de la clase anterior o las observaciones escritas en este cuaderno.",
    "Aprenderé a convertir una observación en una idea para mi obra, probando dos opciones y eligiendo una con un criterio. Sirve para que mi trabajo muestre lo que quiero expresar y no solo lo que vi.",
    ["Sé hacer un registro de observación con croquis, notas y pregunta.", "Sé que las líneas y los colores pueden dar una sensación, como calma o miedo."],
    [
        "Un propósito expresivo es lo que quiero mostrar o hacer sentir con mi obra: grandeza, soledad, calma o alegría. La misma observación puede servir para propósitos distintos. Una montaña puede mostrar grandeza o puede mostrar compañía, según cómo la dibuje. Por eso, antes de crear, hay que decidir el propósito.",
        "Para lograrlo, usa tres decisiones. El primer plano es lo que se ve más cerca y suele ser lo más grande. El fondo es lo que se ve más lejos. Los valores (también llamados tonos) son lo claro, lo medio y lo oscuro de los colores que uso. Si dibujo una montaña enorme y una persona muy pequeña delante, muestro grandeza. Si dibujo una casa grande en primer plano y una montaña pequeña detrás, muestro cercanía y calma.",
        "Un buen método es hacer dos pruebas pequeñas con decisiones distintas y elegir una según un criterio: ¿cuál muestra mejor mi propósito? No se elige «la más bonita», sino la que se parece más a lo que quiero expresar. Después desarrollo la obra y anoto una decisión que cambié durante el proceso.",
    ],
    [("propósito expresivo", "lo que quiero mostrar o hacer sentir con mi obra"), ("primer plano", "lo que se ve más cerca de quien mira"), ("fondo", "lo que se ve más lejos de quien mira"), ("valor", "qué tan claro u oscuro es un color; también se le llama tono"), ("criterio", "regla que uso para decidir entre dos opciones")],
    [
        w("Mostrar grandeza", "Observaste una cordillera nevada. Quieres expresar grandeza. ¿Qué decisiones tomas?", ["Mi propósito es grandeza.", "Dibujo la cordillera muy grande, casi hasta los bordes de la hoja.", "Pongo una persona pequeña en el primer plano para comparar los tamaños."], "Montaña enorme y persona pequeña en primer plano"),
        w("Elegir entre dos pruebas", "Hiciste dos pruebas de un lago para expresar calma. La A usa líneas quebradas y colores muy oscuros. La B usa líneas largas y colores claros. ¿Cuál eliges con el criterio «muestra calma»?", ["Reviso la prueba A: sus líneas quebradas y oscuras dan más tensión.", "Reviso la prueba B: sus líneas largas y claras dan tranquilidad.", "Aplico el criterio: elijo la que muestra calma."], "La prueba B"),
    ],
    [
        m("Elegir la prueba «más bonita» sin decir qué propósito logra.", "El criterio no se relaciona con lo que se quiere expresar.", "Pregunta: ¿cuál muestra mejor lo que quiero expresar?"),
        m("Hacer dos pruebas iguales y cambiarles solo el título.", "No se tomó ninguna decisión visual distinta.", "Cambia al menos una decisión: tamaño, primer plano, fondo o valores."),
    ],
    [
        ex("En un dibujo, ¿cómo se llama lo que se ve más cerca de quien mira: primer plano o fondo?", "Primer plano", "El primer plano es la parte más cercana."),
        ex("Un valor (o tono) es qué tan claro u oscuro es un color. ¿Cuál es más oscuro: el celeste claro o el azul muy oscuro?", "El azul muy oscuro", "Mientras más oscuro, más cerca del negro."),
        ex("Quieres expresar grandeza con una montaña. Lees: «dibujé la montaña casi hasta los bordes de la hoja». ¿La montaña quedó grande o pequeña en la hoja?", "Grande", "Ocupa casi toda la hoja."),
    ],
    [
        ex("Lees: «Dibujé una niña muy pequeña frente a un volcán gigante». ¿Qué propósito se muestra mejor: grandeza o compañía?", "Grandeza", "El volcán gigante y la niña pequeña muestran lo grande que es la naturaleza."),
        ex("Dos pruebas de una tormenta para expresar miedo. La A tiene cielo gris claro y líneas suaves. La B tiene cielo muy oscuro y rayos con líneas quebradas. ¿Cuál cumple mejor el criterio «muestra miedo»?", "La B", "Los valores oscuros y las líneas quebradas dan más tensión."),
        ex("Dibujas un perro cerca de quien mira y, lejos, una casa pequeña. ¿Qué es el fondo: el perro o la casa?", "La casa", "La casa está más lejos de quien mira, y lo más lejano es el fondo."),
    ],
    [
        ex("Quieres expresar soledad con un árbol en un desierto. ¿Qué decisión ayuda más: un árbol pequeño en medio de mucho espacio vacío o muchos árboles juntos?", "Un árbol pequeño en medio de mucho espacio vacío", "El espacio vacío refuerza la sensación de estar solo."),
        ex("Ordena los pasos: A) elegir una prueba con un criterio, B) hacer dos pruebas distintas, C) desarrollar la obra. Escribe las tres letras en orden.", "B, A, C", "Primero haces las pruebas, luego eliges con un criterio y al final desarrollas la obra."),
        ex("Tu propósito es calma. Para el cielo de un paisaje elegirías: A) rojo muy fuerte con rayas negras, o B) celeste claro con nubes suaves. ¿Cuál?", "B", "Los tonos claros y las formas suaves dan tranquilidad."),
    ],
    [
        ex("Ana dice: «Elegí la prueba B porque muestra mejor la soledad que quería expresar». ¿Usó un criterio que se relaciona con su propósito?", "Sí", "Comparó las pruebas con lo que quería expresar."),
        ex("Pablo dice: «Elegí la A porque la hice primero». ¿Es un buen criterio para elegir una prueba?", "No", "El orden en que se hizo no dice nada sobre el propósito."),
    ],
    [
        ex("Quieres que el sol de tu dibujo se note mucho y lo pintas con el valor más claro. ¿Qué valor eliges para el cielo que lo rodea, para que haya contraste: oscuro o claro?", "Oscuro", "Un valor claro junto a uno oscuro produce contraste y se nota más."),
        ex("Haces dos pruebas de un cerro con nieve. En la A el cerro ocupa toda la hoja. En la B el cerro es pequeño y hay una casa grande delante. Quieres mostrar grandeza del cerro. ¿Qué prueba eliges?", "La A", "La prueba A hace que el cerro se vea enorme."),
    ],
    ex("Cambiaste una decisión mientras desarrollabas tu obra: al inicio pintaste el fondo muy oscuro, pero tu propósito era alegría, así que lo cambiaste a un amarillo claro. ¿Qué criterio usaste para cambiar?", "Que el fondo mostrara alegría", "Cambiaste el fondo para que combinara con el propósito."),
    [
        ex("¿Qué es el fondo en un dibujo?", "Lo que se ve más lejos", "El fondo es la parte más lejana de la escena."),
        ex("Verdadero o falso: una buena razón para elegir una prueba es «la que mejor muestra mi propósito».", "Verdadero", "Ese es un criterio que se relaciona con lo que quiero expresar."),
        ex("¿Cuántas pruebas pequeñas haces antes de elegir según esta clase?", "Dos", "El método de la clase pide dos pruebas con decisiones distintas."),
    ],
    task(
        "Elige UNA observación y UN propósito. Observación: A) una cordillera con nieve; B) un lago rodeado de cerros; C) un árbol solo en una pampa. Propósito: grandeza, soledad o calma. Haz dos pruebas pequeñas con decisiones distintas (tamaño, primer plano, fondo o valores). Elige una con un criterio, desarrolla tu obra y anota una decisión que cambiaste.",
        "Elegí la opción C y el propósito de soledad. Prueba 1: árbol grande y muchos pájaros. Prueba 2: árbol pequeño con mucho cielo vacío. Elegí la 2 porque muestra mejor la soledad. Cambié el cielo de gris oscuro a celeste pálido para que se viera más tranquilo.",
        ["hace dos pruebas distintas", "elige con un criterio relacionado con el propósito", "usa primer plano, fondo o valores", "anota una decisión que cambió"],
        ["dos pruebas", "obra final", "una frase con el criterio"],
        ["elegir sin criterio", "pruebas casi iguales"],
        "Reconoce la decisión mejor justificada y pregunta qué cambiaría para expresar el propósito opuesto.",
    ),
    "Mira un objeto de tu casa y di en voz alta dos propósitos distintos para dibujarlo, y qué cambiarías del primer plano en cada caso.",
    "Haz tu obra en dos tamaños (uno grande, uno pequeño) y anota cuál muestra mejor tu propósito.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hoja, lápiz y lápices de colores. El resumen del relato que se usa está escrito en este cuaderno; no necesitas buscarlo.",
    "Aprenderé a crear una imagen a partir de un mito, indicando de dónde viene el relato y qué parte interpreto yo. Sirve para respetar el origen de una historia y a la vez expresar mi idea.",
    ["Sé separar lo que veo de lo que opino.", "Sé elegir un propósito para mi obra, como miedo, calma o alegría."],
    [
        "Un mito es un relato muy antiguo que un pueblo cuenta para explicar algo del mundo, como la forma de los cerros o el origen del mar. Los mitos pertenecen a los pueblos que los crearon y existen en distintas versiones. Para muchos pueblos son también parte de su historia y de sus creencias, así que se tratan con respeto. Por eso, al usarlos para crear, hay que decir de dónde vienen. Eso se llama citar la fuente.",
        "Una fuente identificada dice quién cuenta el relato y a qué pueblo pertenece. Por ejemplo, este es un resumen muy general de un relato del pueblo mapuche, en Chile: «Hay dos serpientes, Kaikai Vilu, ligada al agua, y Trentren Vilu, ligada a la tierra. El mar subió y Trentren Vilu hizo crecer los cerros, donde las personas se salvaron». Los nombres se escriben de varias formas y hay más de una versión. Este resumen no reemplaza el relato de las comunidades: para conocerlo bien, pide a un educador o educadora tradicional mapuche, o a una persona de la comunidad, que lo cuente.",
        "Interpretar un mito es decidir qué momento mostrar y qué sentir en ese momento: la fuerza de las olas, la calma de los cerros altos o el esfuerzo de las personas. Mi imagen es una interpretación mía, no una copia de la historia. Escribo al lado de mi obra la fuente y qué parte es mi interpretación.",
    ],
    [("mito", "relato antiguo que un pueblo cuenta para explicar algo del mundo"), ("fuente", "persona, libro o pueblo de donde viene un relato"), ("versión", "forma en que se cuenta un relato; puede cambiar de un lugar a otro"), ("interpretar", "elegir qué mostrar de un relato y cómo hacerlo"), ("ser imaginario", "personaje que existe en los relatos y no en la realidad")],
    [
        w("Citar la fuente", "Quieres dibujar la historia de las dos serpientes. ¿Qué escribes al lado de tu obra para citar la fuente?", ["Digo a qué pueblo pertenece: el pueblo mapuche.", "Aclaro que es un relato con varias versiones.", "Escribo: «Relato mapuche de Chile, interpretado por mí»."], "Relato mapuche de Chile, interpretado por mí"),
        w("Elegir un momento", "En el relato, el mar sube y los cerros crecen. Quieres expresar esperanza. ¿Qué momento eliges?", ["Pienso en lo que me da esperanza: los cerros que se levantan.", "Elijo el momento en que las personas llegan a los cerros altos.", "Uso colores claros arriba y olas lejos, abajo."], "El momento en que las personas se salvan en los cerros"),
    ],
    [
        m("Inventar un relato y decir que es un mito mapuche.", "Se atribuye a un pueblo algo que ese pueblo no contó.", "Cita relatos conocidos, o di claramente «relato inventado por mí»."),
        m("Copiar una imagen de un libro y decir que es mi interpretación.", "No hay una decisión propia sobre qué mostrar.", "Elige un momento y cámbialo con tus propios colores, formas y tamaños."),
    ],
    [
        ex("Un mito es un relato antiguo de un pueblo. ¿Para qué lo cuenta ese pueblo: para explicar algo del mundo o para vender un producto?", "Para explicar algo del mundo", "Los mitos explican cosas como el origen del mar o de los cerros."),
        ex("En el resumen de la clase, ¿con qué elemento se relaciona Kaikai Vilu: el agua o la tierra?", "El agua", "El resumen dice que Kaikai Vilu está ligada al agua."),
        ex("¿Qué significa «citar la fuente»?", "Decir de dónde viene el relato", "Citar la fuente es indicar quién cuenta el relato y a qué pueblo pertenece."),
    ],
    [
        ex("Escribes: «Relato mapuche de Chile, interpretado por mí». ¿Esa frase cita la fuente o la oculta?", "La cita", "Dice a qué pueblo pertenece el relato y que la imagen es una interpretación."),
        ex("Dos niños dibujan el mismo mito. Uno muestra olas enormes y el otro, personas llegando a un cerro. ¿Son dos interpretaciones válidas del mismo relato?", "Sí", "Cada uno eligió un momento distinto y las dos imágenes parten del mismo relato."),
        ex("En el resumen, Trentren Vilu hizo crecer algo para que las personas se salvaran. ¿Qué parte de la naturaleza crece: el cielo o los cerros?", "Los cerros", "En el resumen, los cerros crecen y allí las personas se salvan."),
    ],
    [
        ex("Quieres expresar miedo con la historia de las serpientes. ¿Qué momento eliges: el mar subiendo con olas enormes o las personas descansando en un cerro?", "El mar subiendo con olas enormes", "Las olas enormes dan sensación de peligro."),
        ex("Tu propósito es esperanza. ¿Qué colores y valores usas más: claros y cálidos o negros y rojos oscuros?", "Claros y cálidos", "Los tonos claros y cálidos se asocian con esperanza en esta obra."),
        ex("Ordena: A) elegir el momento y los recursos, B) leer el relato y su fuente, C) escribir la fuente al lado de la obra. Escribe las tres letras en orden.", "B, A, C", "Primero lees la fuente, luego decides cómo mostrarla y al final la anotas junto a tu obra."),
    ],
    [
        ex("Pedro dice: «Mi dibujo es el mito mapuche exacto». Pero él mismo eligió el color de las serpientes y cómo se ven. ¿Cuál frase es más correcta: «es mi interpretación de un relato» o «es el mito exacto»?", "Es mi interpretación de un relato", "El dibujo muestra decisiones propias de Pedro."),
        ex("Una niña inventa una criatura de agua para su dibujo y escribe «relato mapuche». ¿Es correcto?", "No", "Si inventa algo, debe decir que es inventado por ella y no atribuirlo a un pueblo."),
    ],
    [
        ex("Tu cartel dice: «Relato del pueblo mapuche. Hay varias versiones; mi dibujo muestra a las personas en el cerro». ¿Cuántas de estas tres cosas aparecen en el cartel: el pueblo, que hay varias versiones y el momento que dibujaste?", "Tres", "El cartel nombra el pueblo, dice que hay versiones e indica el momento."),
        ex("Quieres conocer la forma tradicional del relato. ¿A quién conviene pedirle que lo cuente: a un educador o educadora tradicional mapuche, o a un compañero que lo leyó una vez?", "A un educador o educadora tradicional mapuche", "La forma tradicional la cuentan las personas de las comunidades; un compañero solo tendría un resumen."),
    ],
    ex("En tu colegio te piden presentar una obra inspirada en un relato de un pueblo. Tienes el dibujo listo, pero sin texto. ¿Qué agregas para que se entienda de dónde viene: el nombre del pueblo y la frase «interpretado por mí» o solo tu nombre?", "El nombre del pueblo y la frase «interpretado por mí»", "Así se reconoce el origen del relato y tu autoría."),
    [
        ex("¿Qué es un mito?", "Un relato antiguo para explicar algo del mundo", "Un pueblo lo cuenta para entender su entorno."),
        ex("Verdadero o falso: un mito puede tener varias versiones.", "Verdadero", "Se transmite de persona en persona y puede cambiar un poco."),
        ex("¿Qué parte de la obra es tuya al interpretar un mito?", "Lo que decides mostrar y cómo", "La interpretación es tu elección de momento, colores y formas."),
    ],
    task(
        "Usa este resumen: «Según un relato del pueblo mapuche, en Chile, hay dos serpientes, Kaikai Vilu, ligada al agua, y Trentren Vilu, ligada a la tierra. El mar subió y Trentren Vilu hizo crecer los cerros, donde las personas se salvaron». Es un resumen muy general; si puedes, pide a un educador o educadora tradicional que te cuente el relato completo. Elige UN momento (el mar subiendo, los cerros creciendo o las personas llegando) y UN propósito (miedo, esperanza o fuerza). Haz un dibujo y escribe al lado la fuente y qué parte es tu interpretación.",
        "Elegí el momento de los cerros creciendo y el propósito de esperanza. Dibujé cerros grandes con tonos claros y las olas lejos, abajo. Escribí: «Relato mapuche de Chile (hay varias versiones). Yo elegí mostrar los cerros y usé colores claros para la esperanza».",
        ["cita la fuente", "elige un momento y un propósito", "usa recursos visuales relacionados con el propósito", "distingue qué es suyo"],
        ["dibujo", "texto con fuente e interpretación"],
        ["inventar y atribuir a un pueblo", "no citar la fuente"],
        "Valora la cita de la fuente y pregunta qué otra interpretación del mismo relato podría hacer.",
    ),
    "Cuenta el relato en voz alta con tus palabras a una persona de tu casa y di qué momento dibujarías.",
    "Haz el mismo momento con dos propósitos distintos y anota qué colores cambiaste.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hoja, lápiz y lápices de colores. Las descripciones que se usan están escritas en este cuaderno.",
    "Aprenderé a imaginar un ser de una cultura o de mi propia invención sin caer en estereotipos. Sirve para crear con respeto y mostrar que las culturas no son solo un disfraz.",
    ["Sé que un mito tiene una fuente que hay que citar.", "Sé interpretar un relato eligiendo un momento y un propósito."],
    [
        "Un ser imaginario es un personaje que existe en los relatos y no en la realidad. En Chile, la tradición oral de Chiloé habla, por ejemplo, del Caleuche, un barco fantasma que navega de noche. Esa es solo una idea muy general: el Caleuche tiene muchas historias y cambian según quien las cuenta. Cada ser imaginario pertenece a una tradición y a un lugar. Antes de dibujarlo, hay que saber de dónde viene; para conocerlo bien, pregunta a una persona que conozca la tradición, como un educador o educadora tradicional o un cultor de Chiloé.",
        "Un estereotipo es una imagen simple y repetida que se usa para todas las personas de un pueblo, como si fueran iguales. Por ejemplo, dibujar a todos los pueblos de América con las mismas plumas es un estereotipo, porque los pueblos son muy distintos: tienen otras ropas, casas, lenguas y artes. Para evitarlo, hazte tres preguntas. ¿De dónde viene este ser o esta forma? ¿Qué dice la tradición de él? ¿Qué parte la invento yo?",
        "También puedes crear un ser imaginario propio, inspirado en la naturaleza de América, como un guardián de un cactus del desierto. Si lo inventas, di que es invención tuya y no lo atribuyas a un pueblo. Así respetas las tradiciones y también tu libertad creativa.",
    ],
    [("ser imaginario", "personaje que existe en los relatos y no en la realidad"), ("estereotipo", "imagen simple y repetida que se usa para todas las personas de un pueblo"), ("tradición", "costumbre o relato que se cuenta de generación en generación"), ("invención propia", "algo que creo yo y que no viene de un pueblo"), ("atribuir", "decir que algo pertenece a alguien o a un pueblo")],
    [
        w("Detectar un estereotipo", "Una compañera dibuja a todas las personas de América con las mismas plumas en la cabeza. ¿Es un estereotipo?", ["Pregunto: ¿los pueblos de América son todos iguales?", "No: hay muchos pueblos, con ropas y artes distintos.", "Entonces repetir las mismas plumas para todos es un estereotipo."], "Sí, es un estereotipo"),
        w("Crear un ser propio", "Quieres crear un ser imaginario del desierto. ¿Cómo lo presentas sin atribuirlo a un pueblo?", ["Me inspiro en el cactus y en la arena del desierto.", "Dibujo un guardián con cuerpo de cactus.", "Escribo: «Ser imaginario inventado por mí»."], "Un guardián-cactus con la nota «inventado por mí»"),
    ],
    [
        m("Dibujar un ser de una tradición y cambiarle todo, pero decir que sigue siendo ese ser.", "Se atribuye a la tradición algo que la tradición no cuenta.", "Di qué parte viene de la tradición y qué parte es tuya."),
        m("Usar las mismas plumas, colores o símbolos para todos los pueblos.", "Se trata a los pueblos como si fueran iguales.", "Averigua de qué pueblo hablas y usa solo lo que sabes de él."),
    ],
    [
        ex("En la tradición de Chiloé, ¿qué es el Caleuche según la clase: un barco fantasma o una montaña?", "Un barco fantasma", "La clase lo presenta como un barco fantasma que navega de noche."),
        ex("Un estereotipo es una imagen simple y repetida para todos. ¿Es un estereotipo dibujar a todos los pueblos con la misma ropa?", "Sí", "Se trata a pueblos distintos como si fueran iguales."),
        ex("Un ser imaginario, ¿existe en los relatos o en la realidad?", "En los relatos", "Los seres imaginarios son personajes de relatos."),
    ],
    [
        ex("Inventaste un guardián con cuerpo de cactus. ¿Debes escribir «inventado por mí» o «relato tradicional»?", "Inventado por mí", "Es una creación propia y no de un pueblo."),
        ex("Carla dibuja el Caleuche y le agrega un gorro de moda actual. ¿Qué parte es invento suyo: el barco fantasma o el gorro?", "El gorro", "El barco viene de la tradición; el gorro lo agregó ella."),
        ex("¿Cuál pregunta ayuda a evitar un estereotipo? A: «¿Cuántos colores tiene mi caja?». B: «¿De dónde viene esta forma y qué dice la tradición?».", "B", "Esa pregunta lleva a conocer el origen antes de crear."),
    ],
    [
        ex("Quieres dibujar un ser de la tradición de Chiloé. Antes averiguas con una persona que conoce el relato. ¿Hiciste bien o mal?", "Bien", "Averiguar la fuente evita inventar datos sobre una tradición."),
        ex("Tu ser inventado vive en un salar, un lugar del desierto cubierto de sal. Para su cuerpo, ¿qué se relaciona más con ese lugar: cristales de sal blancos u hojas verdes de helecho?", "Cristales de sal blancos", "Un salar está cubierto de sal; los helechos crecen en lugares húmedos."),
        ex("Ordena: A) decidir qué parte invento, B) averiguar de dónde viene el ser, C) dibujar. Escribe las letras en orden.", "B, A, C", "Primero averiguas el origen, luego decides qué cambias y después dibujas."),
    ],
    [
        ex("Un niño dice: «Dibujé a todas las culturas con el mismo traje porque así se entiende más fácil». ¿Ese dibujo evita el estereotipo?", "No", "Mostrar a todos con el mismo traje repite el estereotipo."),
        ex("Dos dibujos del Caleuche: en el A, un barco que navega de noche. En el B, un auto que anda de día. ¿Cuál mantiene la idea de la tradición que cuenta la clase?", "El A", "La tradición habla de un barco que navega de noche."),
    ],
    [
        ex("Tu cartel dice: «Ser inspirado en la tradición de Chiloé. Yo agregué las luces de colores». ¿Qué dos partes distingue el cartel: lo tradicional y lo agregado, o solo lo tradicional?", "Lo tradicional y lo agregado", "Señala qué viene de la tradición y qué agregaste tú."),
        ex("Quieres que tu ser inventado no se confunda con uno tradicional. ¿Le pones un nombre claramente tuyo o le copias el nombre de un ser tradicional?", "Un nombre claramente tuyo", "Un nombre propio evita atribuir tu invención a una tradición."),
    ],
    ex("En una feria del colegio, un grupo quiere mostrar «las culturas de América» con un solo dibujo del mismo personaje con plumas. Tú propones otra cosa. ¿Qué es mejor: mostrar un ser o una artesanía de un pueblo con su fuente o repetir el personaje de plumas?", "Mostrar un ser o una artesanía de un pueblo con su fuente", "Así se respeta la diversidad de los pueblos y se evita el estereotipo."),
    [
        ex("¿Qué es un estereotipo?", "Una imagen simple repetida que se usa para todos", "Trata a personas distintas como si fueran iguales."),
        ex("Verdadero o falso: puedo crear un ser imaginario propio sin atribuirlo a un pueblo.", "Verdadero", "Si digo que es invención mía, no estoy usando una tradición ajena."),
        ex("¿Cuáles son las tres preguntas para evitar un estereotipo? Escribe la tercera.", "¿Qué parte la invento yo?", "Las preguntas son de dónde viene, qué dice la tradición y qué invento yo."),
    ],
    task(
        "Elige UNA opción: A) dibuja el Caleuche, un barco fantasma que navega de noche según la tradición de Chiloé, con tu propio estilo; B) inventa un ser imaginario inspirado en un animal o una planta de América. Escribe al lado: de dónde viene, qué es tradición y qué es invención tuya.",
        "Elegí la opción B. Mi ser es un guardián con cuerpo de cactus y ojos de luciérnaga. Escribí: «Ser inventado por mí, inspirado en el desierto. No pertenece a ningún pueblo».",
        ["dice de dónde viene el ser", "separa tradición e invención propia", "no repite un estereotipo", "usa líneas y colores con intención"],
        ["dibujo", "frase de fuente e invención"],
        ["atribuir una invención a un pueblo", "repetir las mismas plumas para todos"],
        "Valora que distinga lo tradicional de lo propio y pregunta qué dato sobre la tradición le gustaría aprender.",
    ),
    "Cuéntale a una persona de tu casa por qué dibujar a todos los pueblos igual no es respetuoso, con un ejemplo.",
    "Pide a una persona que conozca una tradición que te cuente un ser de su zona. Anota su nombre y dibújalo citándola como fuente.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hoja, lápiz y lápices de colores. Las obras que se usan están descritas en este cuaderno; si puedes ver imágenes de cerámica diaguita u obras del pintor chileno Roberto Matta, hazlo junto a una persona adulta.",
    "Aprenderé a dialogar con una obra antigua y con una obra chilena: tomar una idea de cada una y crear algo propio. Sirve para aprender de otros artistas sin copiarlos.",
    ["Sé citar la fuente de un relato.", "Sé que las culturas de América son muy distintas entre sí."],
    [
        "El arte precolombino es el arte que hicieron los pueblos de América antes de la llegada de los europeos, en 1492. Es arte antiguo, pero los pueblos siguen existiendo hoy. En Chile, por ejemplo, el pueblo diaguita hizo cerámica, vasijas hechas a mano que son una artesanía, con decoraciones geométricas: triángulos, líneas en zigzag y formas repetidas, en colores como rojo, negro y blanco. Esta es solo una descripción general. Para conocer lo que significan esas decoraciones, pregunta a una persona de una comunidad diaguita, a un educador o educadora tradicional o a un museo.",
        "También hay arte chileno más reciente. Roberto Matta fue un pintor chileno que se relacionó con el surrealismo, un movimiento que muestra imágenes como de sueños. Sus pinturas tienen formas libres, colores intensos y espacios que parecen no tener límite. Dos obras de épocas distintas pueden darme ideas distintas.",
        "Dialogar con una obra no es copiarla. Es observarla, elegir una idea (por ejemplo, repetir formas, usar tres colores o dejar un espacio libre) y usarla en mi propia creación. Respondo tres preguntas: ¿qué miré?, ¿qué idea tomé? y ¿qué agregué yo? Así mi obra conserva mi autoría.",
    ],
    [("arte precolombino", "arte que hicieron los pueblos de América antes de la llegada de los europeos"), ("arte antiguo", "arte hecho hace mucho tiempo"), ("geométrico", "hecho con formas como triángulos, cuadrados y líneas rectas"), ("surrealismo", "movimiento artístico que muestra imágenes como de sueños"), ("dialogar con una obra", "mirarla, tomar una idea y usarla en algo propio sin copiarla")],
    [
        w("Tomar una idea", "Observas una cerámica con triángulos y zigzags en rojo, negro y blanco. ¿Qué idea puedes tomar para una obra propia?", ["Miro qué se repite: triángulos y zigzags.", "Miro los colores: rojo, negro y blanco.", "Tomo una idea: repetir formas geométricas en un ritmo."], "Repetir formas geométricas en un ritmo"),
        w("Separar lo tomado de lo propio", "Tomaste de la cerámica la repetición de triángulos. Dibujas una montaña con triángulos azules y verdes. ¿Qué es tuyo?", ["La repetición viene de la cerámica.", "La montaña y los colores azules y verdes son decisión mía.", "Escribo ambas partes."], "Tuyo: la montaña y los colores azul y verde"),
    ],
    [
        m("Copiar una cerámica completa y firmarla como obra propia.", "No hay creación propia, solo copia.", "Toma una idea y agrega algo tuyo."),
        m("Decir que todo el arte antiguo de América es igual.", "Cada pueblo hizo un arte distinto.", "Nombra el pueblo y qué se observa en su obra."),
    ],
    [
        ex("¿Qué significa precolombino según la clase: antes o después de la llegada de los europeos a América?", "Antes", "Precolombino se refiere a antes de esa llegada."),
        ex("La cerámica diaguita de la clase tiene decoraciones geométricas. ¿Cuál de estas formas aparece: triángulos o estrellas de mar?", "Triángulos", "La clase nombra triángulos, zigzags y líneas."),
        ex("¿Cuál de estos colores aparece en la cerámica diaguita de la clase: rojo o verde?", "Rojo", "La clase menciona rojo, negro y blanco."),
    ],
    [
        ex("Una obra del pintor chileno Roberto Matta muestra formas libres y espacios sin límite. ¿Qué movimiento se relaciona con esa pintura según la clase?", "El surrealismo", "La clase dice que Matta se relacionó con el surrealismo."),
        ex("Miras una vasija con zigzags repetidos. Anotas: «zigzags en fila, uno tras otro». ¿Qué idea tomas: la repetición o el color?", "La repetición", "La nota habla de zigzags que se repiten."),
        ex("¿Cuál frase dialoga con una obra? A: «Copié toda la vasija». B: «Tomé la repetición de formas y dibujé mi propia montaña».", "B", "En la B hay una idea tomada y algo propio."),
    ],
    [
        ex("Quieres tomar la idea de «usar pocos colores» de la cerámica de la clase. ¿Qué tres colores nombra la clase?", "Rojo, negro y blanco", "Son los colores que menciona la clase."),
        ex("Tomaste el «espacio libre» de una pintura chilena y haces un paisaje con mucho cielo vacío. ¿Qué agregas para que sea tuyo: un animal que elegiste o la misma forma de la pintura?", "Un animal que elegiste", "Agregar una decisión propia mantiene tu autoría."),
        ex("Ordena: A) elegir qué idea tomo, B) observar la obra, C) crear mi obra. Escribe las tres letras en orden.", "B, A, C", "Se observa, se elige una idea y luego se crea."),
    ],
    [
        ex("Un compañero copió una vasija y escribió «obra de Juan». Otro tomó la repetición de formas y dibujó un cerro. ¿Cuál conserva mejor su autoría?", "El que tomó la repetición y dibujó un cerro", "Hay una idea tomada y una creación propia."),
        ex("Diana dice: «Las obras antiguas de América se parecen todas». ¿Está bien lo que dice, según la clase?", "No", "Cada pueblo hizo un arte distinto."),
    ],
    [
        ex("Quieres unir una idea del arte antiguo (repetir triángulos) y una idea de un pintor surrealista (un espacio sin límites). ¿Cómo lo haces: triángulos que se repiten en un cielo muy grande y vacío o triángulos pequeños apretados en una esquina?", "Triángulos que se repiten en un cielo muy grande y vacío", "Une la repetición con el espacio sin límites."),
        ex("Tu cartel dice: «Idea tomada: repetición de formas (cerámica diaguita). Idea propia: una montaña con luciérnagas». ¿Cuántas partes distingue: lo tomado y lo propio, o solo lo tomado?", "Lo tomado y lo propio", "El cartel separa las dos partes."),
    ],
    ex("En clase ven una vasija decorada con zigzags. Te piden crear una obra propia a partir de ella. ¿Qué haces: copiar los zigzags de la misma manera o elegir una idea, como repetir y cambiar el color?", "Elegir una idea, como repetir y cambiar el color", "Así dialogas con la obra y conservas tu autoría."),
    [
        ex("¿Qué es el arte precolombino?", "El arte de los pueblos de América antes de los europeos", "Se hizo antes de la llegada de los europeos."),
        ex("Verdadero o falso: dialogar con una obra es copiarla igual.", "Falso", "Es tomar una idea y crear algo propio."),
        ex("¿Qué tres preguntas respondes al dialogar con una obra? Escribe la segunda.", "¿Qué idea tomé?", "Las preguntas son qué miré, qué idea tomé y qué agregué yo."),
    ],
    task(
        "Usa esta descripción: «Una vasija de cerámica diaguita tiene triángulos y zigzags que se repiten en rojo, negro y blanco». Elige UNA idea para tu obra: A) repetir una forma, B) usar solo tres colores, C) llenar toda la superficie con un patrón. Crea una obra sobre un tema de la naturaleza de América. Escribe qué idea tomaste y qué agregaste tú.",
        "Elegí la idea A (repetir una forma). Dibujé un volcán cubierto de triángulos repetidos en tonos de azul y gris. Escribí: «Idea tomada: repetición de formas. Idea propia: el volcán y los azules».",
        ["elige una idea concreta de la obra", "no copia el diseño", "agrega una decisión propia", "escribe qué tomó y qué agregó"],
        ["obra", "frase con lo tomado y lo propio"],
        ["copiar el diseño completo", "no distinguir lo propio de lo tomado"],
        "Reconoce la idea tomada y pregunta qué otra decisión haría su obra más personal.",
    ),
    "Mira un objeto decorado de tu casa y di qué forma se repite en la decoración y cuántas veces la ves.",
    "Haz la misma obra con otra idea (por ejemplo, tres colores) y compara cuál conserva mejor tu estilo.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA1, 6,
    "Hoja grande, lápiz, témpera, lápices de colores o papeles de colores y pegamento en barra. Las descripciones de los movimientos están en este cuaderno.",
    "Aprenderé a crear una obra personal que une una observación de la naturaleza, un referente cultural y un referente artístico, y a explicar qué tomé de cada uno. Sirve para cerrar este tema con una obra mía.",
    ["Sé hacer un registro de observación.", "Sé tomar una idea de una obra sin copiarla."],
    [
        "Una obra personal puede unir tres referentes: uno de la naturaleza (un paisaje que observé), uno de la cultura (una tradición o artesanía de América) y uno del arte (una obra o un movimiento artístico). El muralismo mexicano, que nació en México, consiste en pinturas muy grandes hechas sobre muros públicos, que cuentan historias de la gente. El arte naif usa formas simples, colores vivos y escenas de la vida cotidiana, y muchas veces lo hacen artistas que aprendieron por su cuenta. El surrealismo muestra imágenes como de sueños, con combinaciones imposibles. El naif y el surrealismo también se han hecho en Chile, en Latinoamérica y en otras partes del mundo.",
        "Para unirlos, completa este plan: observación de la naturaleza (qué vi), referente cultural (qué idea tomo y de qué fuente) y referente artístico (qué idea tomo). Después decide tu propósito expresivo y haz dos pruebas pequeñas. Elige una con un criterio, y desarrolla tu obra con calma.",
        "Al final, escribe una ficha de autoría con tres frases: lo que observé, lo que tomé de cada referente y lo que decidí yo. Una obra personal no se evalúa por lo parecida que es a un referente, sino por la relación clara entre mi propósito y mis decisiones visuales.",
    ],
    [("muralismo mexicano", "pinturas muy grandes sobre muros públicos que cuentan historias de la gente"), ("arte naif", "arte con formas simples, colores vivos y escenas cotidianas, muchas veces hecho por artistas que aprendieron por su cuenta"), ("surrealismo", "arte que muestra imágenes como de sueños, con combinaciones imposibles"), ("referente", "obra, tradición o paisaje que me sirve de modelo para una idea"), ("ficha de autoría", "texto breve que dice qué tomé de otros y qué decidí yo")],
    [
        w("Unir tres referentes", "Observaste un lago. Quieres tomar la idea del arte naif (colores vivos y formas simples) y la repetición de formas de la cerámica diaguita. ¿Cómo los unes?", ["Naturaleza: el lago con sus ondas.", "Referente cultural: las ondas se repiten como zigzags.", "Referente artístico: uso colores vivos y formas simples."], "Un lago con ondas repetidas, colores vivos y formas simples"),
        w("Escribir la ficha", "Hiciste el lago con ondas repetidas y colores vivos. Escribe la ficha de autoría.", ["Digo qué observé: un lago.", "Digo qué tomé: la repetición y los colores vivos.", "Digo qué decidí yo: poner un pescador pequeño."], "«Observé un lago. Tomé la repetición y los colores vivos. Yo decidí agregar un pescador pequeño»"),
    ],
    [
        m("Pegar tres referentes en la hoja sin ninguna idea que los una.", "No hay propósito ni decisión propia.", "Decide qué quieres expresar y elige una idea de cada referente que ayude."),
        m("No escribir qué tomé de cada referente.", "No se sabe qué es mío y qué viene de otros.", "Escribe una ficha de autoría con tres frases."),
    ],
    [
        ex("¿Cuál movimiento usa pinturas muy grandes sobre muros públicos: el muralismo mexicano o el arte naif?", "El muralismo mexicano", "La clase lo describe así."),
        ex("El arte naif usa formas simples y colores vivos. ¿Un cuadro con formas simples y colores vivos de una escena de mercado se parece más al arte naif o al surrealismo?", "Al arte naif", "Tiene las características del naif: formas simples, colores vivos y escena cotidiana."),
        ex("El surrealismo muestra imágenes como de sueños. ¿Cuál sería surrealista: un reloj derretido sobre un árbol o una naranja sobre una mesa?", "Un reloj derretido sobre un árbol", "Es una combinación imposible, como en un sueño."),
    ],
    [
        ex("Una ficha de autoría tiene tres frases. ¿Cuál de estas NO va en la ficha: lo que observé, lo que tomé o lo que cuesta mi lápiz?", "Lo que cuesta mi lápiz", "La ficha dice qué observé, qué tomé y qué decidí."),
        ex("Un mural cuenta la vida de las personas en una plaza y ocupa un muro entero de la ciudad. ¿Qué movimiento se parece más a esa obra: el muralismo mexicano, el arte naif o el surrealismo?", "El muralismo mexicano", "Es una pintura muy grande sobre un muro público que cuenta historias de la gente."),
        ex("Pegas tres referentes sin ninguna idea que los una. ¿Tu obra tiene un propósito claro?", "No", "Sin una idea que una los referentes, no se ve qué quieres expresar."),
    ],
    [
        ex("Quieres unir un volcán (naturaleza) con una repetición de triángulos (cultura) y el surrealismo (arte). ¿Qué idea de sueño usas: el volcán con ojos que miran o el volcán igual a una foto?", "El volcán con ojos que miran", "Es una combinación imposible, propia del surrealismo."),
        ex("Quieres que tu obra parezca un mural. ¿Eliges una hoja muy pequeña o una hoja muy grande?", "Una hoja muy grande", "Un mural se caracteriza por su gran tamaño."),
        ex("Ordena: A) hacer dos pruebas y elegir una, B) completar el plan con los tres referentes, C) escribir la ficha de autoría. Escribe las letras en orden.", "B, A, C", "Primero el plan, luego las pruebas y al final la ficha."),
    ],
    [
        ex("Un niño dice: «Mi obra es buena porque se ve igual que el mural que miré». ¿Es un buen criterio para una obra personal?", "No", "Una obra personal se evalúa por la relación entre su propósito y sus decisiones, no por parecerse a otra."),
        ex("Una niña dice: «Mi propósito es alegría. Usé colores vivos y formas simples del naif, y puse un sol grande». ¿Hay relación entre propósito y recursos?", "Sí", "Los colores vivos y el sol grande ayudan a mostrar alegría."),
    ],
    [
        ex("Tu plan dice: naturaleza = nubes sobre un cerro; cultura = repetición de formas; arte = colores vivos del naif. Quieres expresar alegría. ¿Qué colores de nube eliges: amarillo y rosado vivos o gris oscuro?", "Amarillo y rosado vivos", "Los colores vivos van con los recursos del naif y con la alegría."),
        ex("En tu ficha escribes: «Tomé la repetición de formas de una cerámica». ¿Qué debes agregar para completarla: qué decidí yo o el precio de los materiales?", "Qué decidí yo", "La ficha debe distinguir lo tomado de la decisión propia."),
    ],
    ex("En la clase de arte te piden una obra final para exponer. Tienes la obra lista pero sin texto. ¿Qué agregas: una ficha de tres frases o solo tu nombre?", "Una ficha de tres frases", "La ficha explica qué observaste, qué tomaste y qué decidiste."),
    [
        ex("¿Qué usa el arte naif según la clase? Escribe una característica.", "Formas simples, colores vivos o escenas cotidianas", "Esas son características del naif."),
        ex("Verdadero o falso: el surrealismo muestra imágenes como de sueños.", "Verdadero", "Combina elementos de forma imposible."),
        ex("¿Qué es una ficha de autoría?", "Un texto que dice qué tomé de otros y qué decidí yo", "Sirve para mostrar mi parte en la obra."),
    ],
    task(
        "Crea una obra personal con tres referentes. Naturaleza: elige un lago, un cerro o un desierto. Cultura: elige repetir una forma geométrica (como en la cerámica diaguita) o un ser inventado por ti. Arte: elige el naif (colores vivos y formas simples), el muralismo (una escena grande de gente) o el surrealismo (una combinación como de sueño). Decide un propósito, haz dos pruebas, elige una y escribe una ficha de autoría de tres frases.",
        "Elegí el desierto, la repetición de triángulos y el surrealismo. Mi propósito es sorpresa. Dibujé un desierto con cactus que tienen ojos y triángulos repetidos en el cielo. Ficha: «Observé un desierto. Tomé la repetición de triángulos y las combinaciones de sueño. Yo decidí poner ojos a los cactus».",
        ["une los tres referentes", "tiene un propósito claro", "hace dos pruebas y elige con un criterio", "escribe una ficha de tres frases"],
        ["dos pruebas", "obra final", "ficha de autoría"],
        ["pegar referentes sin una idea", "no escribir la ficha"],
        "Valora la relación entre propósito y decisiones visuales y pregunta qué cambiaría si tuviera que mostrar un propósito distinto.",
    ),
    "Cuéntale a una persona de tu casa qué referentes usaste y qué idea tomaste de cada uno.",
    "Haz una versión pequeña de tu obra en otro movimiento (por ejemplo, naif en vez de surrealismo) y compara qué cambia.",
)


# ================================================================ OA 02
# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Lápices de colores, témpera o plumones, y una hoja. Si no tienes todos los colores, usa los que tengas y lee las descripciones de este cuaderno.",
    "Aprenderé a distinguir los colores cálidos y los fríos, y a usarlos para dar sensaciones distintas en una obra. Sirve para elegir colores con una intención y no al azar.",
    ["Sé nombrar los colores primarios (rojo, amarillo y azul) y que al mezclarlos salen otros.", "Sé que las líneas y las formas también expresan ideas."],
    [
        "Los colores tienen temperatura. Los colores cálidos son el rojo, el naranja y el amarillo: nos recuerdan el sol y el fuego. Los colores fríos son el azul, el verde azulado y el violeta azulado: nos recuerdan el agua, la nieve y la sombra. La temperatura no es real, no se siente en la mano; es una sensación que producen los colores al mirarlos.",
        "Los colores también se mezclan. Si a un amarillo le agrego un poco de azul, se vuelve más frío y empieza a ser verde. Si a un azul le agrego un poco de amarillo, se vuelve más cálido. Una obra puede usar casi todo en colores cálidos para dar sensación de calor, o casi todo en fríos para dar sensación de frescura. También puede usar un solo toque cálido en un fondo frío para destacar algo.",
        "El matiz es el nombre del color: rojo, azul o amarillo. Dos matices pueden ser cálidos y distintos entre sí, como el rojo y el amarillo. La temperatura ayuda a mostrar propósitos: un atardecer en el desierto es cálido y un glaciar es frío. Al elegir una temperatura, pregúntate qué sensación quiero dar.",
    ],
    [("color cálido", "color que recuerda el sol o el fuego, como el rojo, el naranja y el amarillo"), ("color frío", "color que recuerda el agua o la nieve, como el azul y el violeta azulado"), ("temperatura del color", "sensación de calor o frío que produce un color al mirarlo"), ("matiz", "nombre de un color, como rojo o azul"), ("destacar", "hacer que algo se note más que el resto")],
    [
        w("Clasificar colores", "Clasifica estos colores en cálidos o fríos: naranja, azul, amarillo, violeta azulado.", ["El naranja y el amarillo recuerdan el sol: son cálidos.", "El azul y el violeta azulado recuerdan el agua y la sombra: son fríos."], "Cálidos: naranja y amarillo. Fríos: azul y violeta azulado"),
        w("Destacar con la temperatura", "Un dibujo de un glaciar es todo azul y blanco. Quieres destacar un montañista pequeño. ¿Qué color eliges para su chaqueta?", ["El fondo es frío (azul y blanco).", "Para destacar, uso un color cálido: naranja o rojo.", "La chaqueta naranja se nota más porque contrasta con el fondo."], "Una chaqueta naranja"),
    ],
    [
        m("Pensar que un color es cálido porque está caliente al tocarlo.", "La temperatura del color es una sensación visual y no se siente con la mano.", "Fíjate en qué te recuerda: el sol o el fuego (cálido), el agua o la nieve (frío)."),
        m("Usar todos los colores cálidos y todos los fríos mezclados sin intención.", "El dibujo pierde la sensación que se quería dar.", "Elige una temperatura principal y usa la otra solo para destacar algo."),
    ],
    [
        ex("¿El rojo es un color cálido o un color frío?", "Cálido", "El rojo recuerda el fuego y el sol."),
        ex("El azul, ¿es un color cálido o frío?", "Frío", "El azul recuerda el agua y la nieve."),
        ex("De estos tres colores, ¿cuál es cálido: azul, amarillo o violeta azulado?", "Amarillo", "El amarillo recuerda la luz del sol; los otros dos son fríos."),
    ],
    [
        ex("Quieres dibujar un atardecer en el desierto. ¿Qué colores elegirías más: naranja y amarillo o azul y violeta?", "Naranja y amarillo", "Son colores cálidos, que van con el calor del atardecer."),
        ex("Un glaciar se dibuja con blanco, celeste y azul. ¿Esa paleta es mayormente cálida o fría?", "Fría", "El celeste y el azul recuerdan el hielo y el agua."),
        ex("Mezclas amarillo con un poco de azul. ¿El color nuevo se vuelve más frío o más cálido?", "Más frío", "El azul agrega frialdad y el color se acerca al verde."),
    ],
    [
        ex("Quieres un cielo que dé sensación de frío. ¿Cuál color de fondo usas: azul oscuro o naranja?", "Azul oscuro", "El azul es un color frío."),
        ex("Un dibujo tiene un fondo todo azul y quieres destacar una flor. ¿Qué color eliges para la flor: celeste o rojo?", "Rojo", "El rojo es cálido y contrasta con un fondo frío."),
        ex("Una paleta tiene cinco manchas: rojo, azul, naranja, amarillo y violeta azulado. ¿Cuántas son de colores cálidos?", "3", "El rojo, el naranja y el amarillo son cálidos; el azul y el violeta azulado son fríos."),
    ],
    [
        ex("Un niño dice: «Pinté un día de nieve usando naranja y rojo». ¿La temperatura de sus colores ayuda al propósito de mostrar frío?", "No", "Los colores cálidos van con calor y no con nieve."),
        ex("Dibujas un bosque de noche, todo con azules y violetas. En el centro pintas una fogata pequeña en naranja. ¿Para qué sirve el toque naranja?", "Para destacar la fogata", "El naranja cálido contrasta con el fondo frío y llama la atención."),
    ],
    [
        ex("Haces un dibujo con una playa al mediodía y quieres que se sienta calor. De estas paletas, ¿cuál eliges: A) amarillo, naranja y rojo suave, o B) azul oscuro, violeta y verde azulado?", "A", "La paleta cálida da sensación de calor."),
        ex("Pintaste un mar de azul. Quieres que se vea más frío todavía. ¿Agregas un poco de amarillo o un poco más de azul oscuro?", "Un poco más de azul oscuro", "El amarillo lo haría más cálido."),
    ],
    ex("Debes pintar un cartel para una campaña que dice «tomar agua en verano». Quieres que dé sensación de frescura. ¿Qué paleta eliges: celestes y verdes azulados o rojos y naranjas?", "Celestes y verdes azulados", "Esos colores fríos dan sensación de frescura."),
    [
        ex("¿Qué colores se consideran cálidos? Escribe uno de los tres de la clase.", "Rojo, naranja o amarillo", "Son los tres colores cálidos que nombra la clase."),
        ex("Verdadero o falso: un color cálido está realmente más caliente al tocarlo.", "Falso", "La temperatura del color es una sensación visual."),
        ex("¿Qué es el matiz de un color?", "El nombre del color", "Por ejemplo, rojo, azul o amarillo."),
    ],
    task(
        "Elige UN tema: A) un atardecer en el desierto; B) un glaciar; C) un bosque lluvioso de noche. Haz dos dibujos pequeños del mismo tema: uno con colores cálidos y otro con colores fríos. Escribe cuál da mejor la sensación del tema y por qué. En uno de los dos, agrega un toque de la temperatura opuesta para destacar algo.",
        "Elegí el glaciar. Hice uno con azules y blancos, y otro con naranjas. El primero da mejor la sensación de frío. Agregué una carpa naranja pequeña para destacarla.",
        ["usa colores de una temperatura clara", "hace dos dibujos con paletas distintas", "explica cuál es mejor y por qué", "usa un toque opuesto para destacar"],
        ["dos dibujos", "una frase de explicación"],
        ["mezclar temperaturas sin intención", "no explicar la elección"],
        "Reconoce la relación entre la temperatura y el tema y pregunta qué color cambiaría si quisiera una sensación opuesta.",
    ),
    "Busca en tu casa tres objetos de colores cálidos y tres de colores fríos, y nómbralos en voz alta.",
    "Pinta el mismo objeto con tres paletas distintas (cálida, fría y mezclada) y anota qué sensación da cada una.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Pinturas o lápices de colores, un poco de pintura blanca y negra si tienes, y una hoja. Los datos de color que se usan están en este cuaderno.",
    "Aprenderé a elegir el matiz y el tono de un color para expresar una idea propia. Sirve para que mis colores tengan una razón y no se usen solo porque me gustan.",
    ["Sé distinguir colores cálidos y fríos.", "Sé que mezclar colores crea colores nuevos."],
    [
        "En un color hay que mirar dos cosas. El matiz es qué color es: rojo, azul, verde, amarillo. El tono es qué tan claro u oscuro es ese color. El azul puede tener un tono muy claro (celeste) o muy oscuro (azul marino). Si agregas blanco a un color, su tono se hace más claro. Si agregas un poquito de negro, se hace más oscuro. Con lápices de colores no hay que mezclar: presiona suave para un tono claro y fuerte para uno oscuro.",
        "Elegir matiz y tono ayuda a expresar una idea. Los tonos claros suelen dar sensación de liviano y calma. Los tonos oscuros suelen dar sensación de peso, misterio o miedo. Un solo matiz en varios tonos, como el azul en tres tonos, da armonía. Si pones un tono muy claro junto a uno muy oscuro, se produce contraste, y el ojo mira primero hacia ahí.",
        "Antes de pintar, escribe tu intención con una frase: «Quiero mostrar un bosque misterioso con verdes oscuros y un toque amarillo claro». Luego prueba tus colores en una hoja aparte. Si no te gusta la prueba, cámbiala y vuelve a probar. Elegir un color es tomar una decisión y se debe poder explicar.",
    ],
    [("matiz", "qué color es: rojo, azul, verde, amarillo"), ("tono", "qué tan claro u oscuro es un color"), ("armonía", "colores que se ven bien juntos porque se parecen"), ("contraste", "diferencia fuerte entre dos colores o tonos, como claro y oscuro"), ("intención", "lo que quiero mostrar o hacer sentir con mis decisiones")],
    [
        w("Cambiar el tono", "Tienes un azul y quieres un azul más claro. ¿Qué haces con la pintura?", ["Quiero cambiar el tono: hacerlo más claro.", "Agrego un poco de blanco al azul.", "El matiz sigue siendo azul, pero el tono es más claro."], "Agregar blanco: el mismo matiz pero con un tono más claro"),
        w("Elegir colores para una intención", "Quieres pintar un bosque misterioso con un toque de luz. ¿Qué matices y tonos eliges?", ["Para el misterio uso verdes y azules de tono oscuro.", "Para la luz agrego un toque de amarillo de tono muy claro.", "El contraste entre lo oscuro y lo claro lleva la mirada a la luz."], "Verdes oscuros y un toque de amarillo claro"),
    ],
    [
        m("Pensar que tono y matiz son lo mismo.", "El matiz es qué color es y el tono es qué tan claro u oscuro.", "Pregunta: ¿qué color es? (matiz) y ¿qué tan claro u oscuro es? (tono)."),
        m("Agregar mucho negro a todos los colores para oscurecerlos.", "El color pierde fuerza y se ve sucio.", "Usa solo un poquito de negro, o prueba con un azul o café oscuro."),
    ],
    [
        ex("Si a un rojo le agregas blanco, ¿su tono se hace más claro o más oscuro?", "Más claro", "El blanco aclara el color."),
        ex("Hay un celeste y un azul marino. ¿Cuál tiene el tono más oscuro?", "El azul marino", "Es el que se parece más al negro."),
        ex("El matiz es el nombre del color. ¿Cuál de estos es un matiz: verde o claro?", "Verde", "Verde es un color; claro habla del tono."),
    ],
    [
        ex("Pintas un mar con tres azules: uno muy claro, uno medio y uno oscuro. ¿Qué cambia entre ellos: el matiz o el tono?", "El tono", "Todos son azules; solo cambia qué tan claro u oscuro son."),
        ex("En un dibujo se ve primero un círculo amarillo claro sobre un fondo azul muy oscuro. ¿Qué hay entre ellos: armonía o contraste?", "Contraste", "Hay una gran diferencia de tono entre el amarillo claro y el azul oscuro."),
        ex("Quieres mostrar calma con un cielo. ¿Qué tonos usas más: claros o muy oscuros?", "Claros", "Los tonos claros dan sensación de calma."),
    ],
    [
        ex("Quieres mostrar miedo en un bosque de noche. De estos tonos de verde, ¿cuál eliges para los árboles: verde muy claro o verde muy oscuro?", "Verde muy oscuro", "Los tonos oscuros dan sensación de misterio y miedo."),
        ex("Quieres lograr armonía con un solo matiz. ¿Pintas tu paisaje con tres tonos de azul o con rojo, verde y naranja?", "Con tres tonos de azul", "Un solo matiz en varios tonos da armonía."),
        ex("Quieres que la luna se vea en una noche oscura. ¿Cómo pintas la luna: con un amarillo muy claro o con un azul oscuro como el cielo?", "Con un amarillo muy claro", "Un tono claro sobre fondo oscuro da contraste y se nota."),
    ],
    [
        ex("Diego pintó el cielo de un atardecer tranquilo con rojo muy oscuro y negro. Dice que es un cielo en calma. ¿Sus tonos ayudan a su intención?", "No", "Los tonos muy oscuros dan peso y no calma."),
        ex("Lucía dice: «Pinté solo con celestes de distintos tonos para que se vea todo parecido y tranquilo». ¿Qué logró: armonía o contraste?", "Armonía", "Usó un solo matiz con tonos parecidos."),
    ],
    [
        ex("Mezclas un amarillo con un poco de blanco para pintar el centro de una flor. ¿Cambió el matiz o el tono?", "El tono", "Sigue siendo amarillo, pero más claro."),
        ex("Tienes tres rosados: A es muy claro, B es medio y C es oscuro. Quieres un contraste fuerte con un fondo rosado oscuro. ¿Qué tono pones encima: A o C?", "A", "El tono muy claro contrasta con un fondo oscuro; el C se confundiría."),
    ],
    ex("Debes pintar un afiche para una función de títeres de misterio. Quieres que se note el título. El fondo es azul muy oscuro. ¿Qué tono usas para las letras: amarillo claro o azul medio?", "Amarillo claro", "Un tono claro se ve con fuerza sobre fondo oscuro."),
    [
        ex("¿Qué es el tono de un color?", "Qué tan claro u oscuro es", "El tono habla de claridad u oscuridad."),
        ex("Verdadero o falso: agregar blanco a un color hace más claro su tono.", "Verdadero", "El blanco aclara."),
        ex("¿Qué se produce cuando se ponen un tono muy claro y uno muy oscuro juntos?", "Contraste", "Hay una gran diferencia entre ambos."),
    ],
    task(
        "Elige UNA intención: A) un bosque misterioso con un toque de luz; B) un mar tranquilo en la mañana; C) un volcán que despierta. Elige dos matices y haz tres tonos de cada uno (claro, medio y oscuro). Pinta el tema usando esos colores. Escribe qué matiz y tono usaste para la parte más importante y por qué.",
        "Elegí B, un mar tranquilo. Usé azul y verde azulado, con tonos claros, medios y oscuros. El mar es azul claro y medio, y las rocas son azul oscuro. Escribí: «El tono claro del mar da calma».",
        ["usa dos matices y tres tonos", "relaciona los colores con la intención", "explica el color de la parte principal", "prueba antes de pintar"],
        ["tabla de pruebas de color", "pintura final", "frase de explicación"],
        ["elegir colores solo porque me gustan", "confundir tono con matiz"],
        "Valora la relación entre color e intención y pregunta qué tono cambiaría para lograr una sensación opuesta.",
    ),
    "Mira un objeto de tu casa y di su matiz y si su tono es claro u oscuro.",
    "Haz una escala de tres tonos para cuatro matices distintos y pega una frase que diga qué sensación da cada tono.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Hojas, lápices de cera o de color, plasticina, arcilla o masa para modelar. Superficies para frotar: moneda, hoja de planta, tela con relieve. No uses herramientas filosas.",
    "Aprenderé a reconocer y crear texturas en un dibujo y en un modelado. Sirve para que mis obras se vean y se sientan distintas.",
    ["Sé que la textura es cómo se siente o se ve la superficie de algo.", "Sé modelar con plasticina o masa."],
    [
        "La textura es cómo se siente o se ve la superficie de algo: lisa, áspera, suave, rugosa o con relieve. Hay dos tipos. La textura táctil se siente con las manos, como la corteza de un árbol. La textura visual es la que se ve y que podemos dibujar, aunque la hoja sea lisa. Con líneas, puntos o manchas puedo dibujar que algo parece áspero o suave. Las líneas largas, finas y curvas dan sensación de suave; las líneas cortas y quebradas, o los puntos apretados, dan sensación de áspero.",
        "En un trabajo plano, como un dibujo o una pintura, la textura es visual. Puedes lograrla frotando un lápiz de cera sobre una hoja puesta encima de una superficie con relieve, como una hoja de planta o una tela. Esa técnica se llama frotado. En un trabajo con volumen, como un modelado de plasticina, la textura es real: se puede tocar. Puedes crearla apretando con una tapa, con un peine o con las uñas.",
        "Una buena obra combina texturas distintas para que se note la diferencia: un cerro rugoso junto a un lago liso. Antes de elegir una textura, pregúntate qué quiero mostrar: ¿algo suave y delicado o algo duro y fuerte? Prueba en una hoja aparte y deja la textura que mejor ayude a tu propósito.",
    ],
    [("textura táctil", "textura que se siente con las manos"), ("textura visual", "textura que se ve, aunque la superficie sea lisa"), ("frotado", "técnica para copiar una textura frotando un lápiz de cera sobre una hoja"), ("volumen", "forma que ocupa espacio y se puede tocar por todos lados"), ("relieve", "parte de una superficie que sobresale")],
    [
        w("Textura visual en un dibujo", "Quieres dibujar la corteza rugosa de un árbol en una hoja lisa. ¿Qué tipo de líneas usas?", ["La corteza se ve rugosa y con grietas.", "Dibujo líneas cortas, quebradas y apretadas.", "Así la textura se ve aunque la hoja sea lisa."], "Líneas cortas y quebradas: una textura visual"),
        w("Textura en un modelado", "Modelaste una bola de plasticina y quieres que parezca una piedra áspera. ¿Cómo logras la textura?", ["Aprieto la superficie con la tapa de un envase.", "Hago muchas marcas pequeñas.", "Ahora se siente áspera al tocarla: es una textura táctil."], "Marcas pequeñas con una tapa: una textura táctil"),
    ],
    [
        m("Dibujar una superficie solo con un color liso y decir que es áspera.", "No hay líneas, puntos o manchas que den sensación de aspereza.", "Usa líneas cortas, puntos o manchas para mostrar la textura."),
        m("Usar herramientas filosas para marcar el modelado.", "Pueden cortar la piel y no son necesarias.", "Usa tapas, peines de plástico o las uñas con cuidado."),
    ],
    [
        ex("La textura es cómo se siente o se ve la superficie. ¿Una corteza rugosa es lisa o áspera?", "Áspera", "Rugosa significa que tiene relieve y se siente áspera."),
        ex("En una hoja lisa dibujas una piel con puntitos para que parezca de lagarto. ¿Es una textura táctil o visual?", "Visual", "Se ve por los puntitos, pero la hoja sigue lisa."),
        ex("Frotas un lápiz de cera sobre una hoja puesta encima de una tela con relieve. ¿Cómo se llama esa técnica?", "Frotado", "Es la técnica que copia texturas con un lápiz."),
    ],
    [
        ex("Modelas una bola de plasticina y la aprietas con una tapa para marcarla. La textura que logras, ¿se puede tocar o solo se ve?", "Se puede tocar", "En un modelado la textura es real: está en el relieve de la plasticina."),
        ex("Un dibujo hecho en una hoja, ¿tiene volumen o solo alto y ancho?", "Solo alto y ancho", "Un dibujo ocupa solo el alto y el ancho de la hoja."),
        ex("¿Cuál combinación de texturas muestra más diferencia: un cerro rugoso junto a un lago liso o un cerro rugoso junto a otro cerro rugoso?", "Un cerro rugoso junto a un lago liso", "Hay dos texturas distintas en la misma obra."),
    ],
    [
        ex("Quieres que el pelo de un animal se vea suave en tu dibujo. ¿Usas líneas largas y finas o puntos gruesos y separados?", "Líneas largas y finas", "Las líneas largas y finas dan sensación de suavidad."),
        ex("Modelas la piel de un reptil con plasticina verde. ¿Marcas escamas pequeñas con una tapa o la dejas totalmente lisa?", "Marcas escamas pequeñas con una tapa", "Las marcas dan textura de escamas."),
        ex("Ordena los pasos del frotado: A) frotar con el lápiz de cera, B) poner la hoja sobre la superficie, C) mirar la textura que aparece. Escribe las letras en orden.", "B, A, C", "Primero pones la hoja, luego frotas y al final ves la textura."),
    ],
    [
        ex("Dibujaste la lana de una oveja con líneas duras y rectas, pero querías mostrar suavidad. ¿Qué cambias: usas líneas curvas y suaves o líneas más duras?", "Líneas curvas y suaves", "Las curvas suaves muestran suavidad."),
        ex("Dos compañeros pintan una playa. Uno usa el mismo punto para arena y mar. La otra usa puntos para la arena y líneas largas para el mar. ¿Quién muestra mejor dos texturas?", "La otra", "Ella usa recursos distintos para cada textura."),
    ],
    [
        ex("En un modelado de un cerro, quieres que arriba se vea liso (nieve) y abajo, rugoso (roca). ¿Dónde aprietas con la tapa: arriba o abajo?", "Abajo", "La roca rugosa va abajo; arriba queda liso."),
        ex("Quieres comparar una textura visual con una táctil. Dibujas un tronco con líneas y luego modelas uno de plasticina con marcas. ¿Cuál de los dos puedes sentir con la mano?", "El de plasticina", "La textura táctil está en el modelado."),
    ],
    ex("Te piden decorar la portada de un cuaderno con un animal del bosque, usando texturas. Quieres mostrar un zorro de pelo suave y un tronco áspero. ¿Cómo dibujas cada uno: pelo con líneas largas y finas, y tronco con líneas cortas y quebradas, o al revés?", "Pelo con líneas largas y finas, y tronco con líneas cortas y quebradas", "Cada textura se muestra con el tipo de línea que la sugiere."),
    [
        ex("¿Qué es la textura visual?", "La que se ve aunque la superficie sea lisa", "Se logra con líneas, puntos o manchas."),
        ex("Verdadero o falso: un modelado de plasticina puede tener textura táctil.", "Verdadero", "Se puede tocar el relieve de la plasticina."),
        ex("¿Cómo se llama la técnica de frotar un lápiz de cera sobre una hoja para copiar una textura?", "Frotado", "Así se llama esa técnica."),
    ],
    task(
        "Haz DOS trabajos del mismo tema. Tema: un animal o una planta de América (puedes elegir un cactus, un zorro o un árbol). Trabajo 1: un dibujo con texturas visuales. Trabajo 2: un pequeño modelado de plasticina con texturas táctiles. Escribe una frase que diga cuál textura se ve mejor y por qué. No uses herramientas filosas.",
        "Elegí el cactus. En el dibujo hice puntos para las espinas y líneas largas para las costillas. En el modelado, apreté la plasticina con una tapa para hacer marcas. La textura del modelado se siente más real porque se puede tocar.",
        ["usa al menos dos texturas distintas", "las texturas ayudan al propósito", "hace un trabajo plano y uno con volumen", "usa herramientas seguras"],
        ["dibujo", "modelado", "frase de comparación"],
        ["no mostrar la diferencia entre texturas", "usar herramientas filosas"],
        "Reconoce la textura mejor lograda y pregunta qué cambiaría para que se note más en el trabajo plano.",
    ),
    "Toca tres superficies de tu casa y di si son lisas, ásperas o suaves. Elige una y di cómo la dibujarías.",
    "Haz tres frotados de superficies distintas y escribe al lado cómo se llama cada textura.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Una hoja, un lápiz de mina y lápices de colores. Un objeto cotidiano para observar (una taza, una hoja, un zapato), o las descripciones de este cuaderno.",
    "Aprenderé a mirar la forma de las cosas y a distinguir formas figurativas y no figurativas, usando líneas de contorno. Sirve para dibujar lo que observo con orden.",
    ["Sé nombrar formas como círculo, cuadrado, triángulo y rectángulo.", "Sé observar con atención el tamaño y el color de algo."],
    [
        "Una forma figurativa representa algo que reconocemos, como una casa, un árbol o una persona. Una forma no figurativa no representa nada reconocible: son líneas, manchas o figuras libres, como un conjunto de círculos y zigzags. Las dos pueden expresar ideas. Una forma no figurativa puede mostrar el movimiento del viento sin dibujar el viento.",
        "La línea de contorno es la línea que rodea una forma y muestra su borde. Para observar una forma real, mira primero su silueta, que es su contorno completo, y busca las formas simples que la componen: una taza tiene un cilindro (el cuerpo) y una curva (el asa). Después dibuja el contorno sin levantar mucho el lápiz y mirando más el objeto que la hoja.",
        "Al comparar el objeto con tu dibujo, revisa si los tamaños son parecidos: ¿el asa es la mitad del cuerpo o casi igual de grande? Si no, corrige. La forma que dibujas puede ser muy parecida a la real o puedes simplificarla, pero debe mantener lo principal para que se reconozca. Un dibujo de observación se hace con calma y puede corregirse.",
    ],
    [("forma figurativa", "forma que representa algo que reconocemos"), ("forma no figurativa", "forma libre que no representa algo reconocible"), ("línea de contorno", "línea que rodea una forma y muestra su borde"), ("silueta", "contorno completo de una forma, como una sombra"), ("simplificar", "dibujar solo las partes principales de algo")],
    [
        w("Figurativa o no figurativa", "Un dibujo muestra una casa con techo, puerta y ventana. Otro, solo líneas curvas de colores sin nada reconocible. ¿Cuál es figurativo?", ["Pregunto: ¿puedo reconocer algo?", "En el primero reconozco una casa.", "En el segundo no reconozco nada."], "La casa es figurativa; las líneas curvas son no figurativas"),
        w("Dibujar el contorno", "Quieres dibujar una taza. ¿Qué formas simples buscas?", ["El cuerpo es como un cilindro: en la hoja, un rectángulo con la boca ovalada.", "El asa es una curva que sale del costado.", "Dibujo el contorno mirando la taza y no solo la hoja."], "Un rectángulo, un óvalo en la boca y una curva para el asa"),
    ],
    [
        m("Pensar que una forma no figurativa «no dice nada».", "Las formas libres también pueden expresar movimiento, calma o alegría.", "Pregunta qué sensación te da y por qué."),
        m("Dibujar la taza de memoria, sin mirarla, porque «ya sé cómo es».", "Se pierden detalles reales y proporciones.", "Mira el objeto mientras dibujas y compara tamaños."),
    ],
    [
        ex("Un dibujo muestra un árbol con tronco y copa. ¿Esa forma es figurativa o no figurativa?", "Figurativa", "Se reconoce un árbol."),
        ex("Un dibujo tiene solo zigzags y manchas de colores, y no se ve ningún objeto. ¿Es figurativo o no figurativo?", "No figurativo", "No representa nada reconocible."),
        ex("La línea de contorno, ¿rodea la forma o la rellena de color?", "Rodea la forma", "El contorno marca el borde."),
    ],
    [
        ex("Una taza tiene un cuerpo cilíndrico y un asa curva. ¿Cuántas formas simples ves en la descripción: una o dos?", "Dos", "El cuerpo cilíndrico y el asa curva."),
        ex("Dibujas sin soltar el lápiz el borde de una hoja de planta. ¿Qué estás dibujando: su contorno o su textura?", "Su contorno", "Dibujas la línea que rodea la hoja."),
        ex("Una silueta es el contorno completo de una forma. Si una pelota se ve de lado, ¿cuál es su silueta: un círculo o un cuadrado?", "Un círculo", "Una pelota se ve redonda desde cualquier lado."),
    ],
    [
        ex("Quieres dibujar un zapato. Su suela es larga y plana y la punta es redondeada. ¿Con qué formas simples empiezas: un rectángulo largo con la punta curva, o un triángulo y una estrella?", "Un rectángulo largo con la punta curva", "Son las formas simples que corresponden a la suela y a la punta."),
        ex("Quieres mostrar el movimiento del viento sin dibujar nada reconocible. ¿Dibujas líneas curvas que giran o una casa con árboles?", "Líneas curvas que giran", "Una forma no figurativa puede sugerir movimiento."),
        ex("Dibujaste una taza con el asa del mismo tamaño que el cuerpo, pero en la real es mucho más pequeña. ¿Qué debes corregir: el tamaño del asa o el color?", "El tamaño del asa", "Al comparar tamaños, el asa debe ser más pequeña."),
    ],
    [
        ex("Ana dice: «Mi dibujo de una manzana tiene un círculo con una hojita y un tallo: es figurativo». ¿Tiene razón?", "Sí", "Se reconoce una manzana."),
        ex("Tomás hizo líneas de colores que giran y dice que representan una canción. No se ve ningún objeto. ¿Su obra es figurativa?", "No", "No representa algo reconocible: es no figurativa."),
    ],
    [
        ex("Quieres dibujar tu mano abierta, mirándola. ¿Qué forma simple buscas en cada dedo: un rectángulo redondeado en la punta o un triángulo?", "Un rectángulo redondeado en la punta", "Cada dedo es largo y tiene la punta redondeada."),
        ex("Haces dos dibujos a partir de una hoja de planta: en uno dibujas su contorno exacto y en el otro, manchas y zigzags de colores que no se parecen a ninguna cosa. ¿Cuál es no figurativo?", "El de manchas y zigzags de colores", "En ese dibujo no se reconoce una hoja ni ningún objeto."),
    ],
    ex("Debes ilustrar la portada de un libro sobre el viento en el campo. Quieres una imagen que muestre movimiento sin dibujar ningún objeto reconocible. ¿Qué eliges: un molino de viento o líneas curvas que giran?", "Líneas curvas que giran", "Es una forma no figurativa que muestra el movimiento."),
    [
        ex("¿Qué es una forma figurativa?", "La que representa algo reconocible", "Por ejemplo, una casa o un árbol."),
        ex("Verdadero o falso: las formas no figurativas no pueden expresar ideas.", "Falso", "Pueden expresar movimiento, calma o alegría."),
        ex("¿Qué es la línea de contorno?", "La línea que rodea una forma", "Muestra su borde."),
    ],
    task(
        "Elige UN objeto de tu casa (una taza, un zapato o una hoja de planta) y haz DOS dibujos. Dibujo 1: figurativo, con el contorno del objeto mirándolo con atención. Dibujo 2: no figurativo, con líneas y manchas que muestren la sensación que te da. Escribe qué formas simples usaste y qué cambia entre los dos.",
        "Elegí un zapato. En el figurativo, un rectángulo largo con la punta curva. En el no figurativo, líneas curvas azules para mostrar movimiento. Cambió que el primero se reconoce y el segundo muestra una sensación.",
        ["dibuja el contorno mirando el objeto", "distingue lo figurativo de lo no figurativo", "nombra las formas simples", "explica la diferencia"],
        ["dibujo figurativo", "dibujo no figurativo", "frase de explicación"],
        ["dibujar de memoria", "no explicar la diferencia"],
        "Reconoce la fidelidad del contorno y pregunta qué sensación quiso mostrar en el dibujo no figurativo.",
    ),
    "Mira un objeto de tu casa y di cuántas formas simples ves en él.",
    "Dibuja tres veces el mismo objeto, simplificando cada vez más, y anota cuándo deja de reconocerse.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Una hoja, un lápiz de mina y lápices de colores. Un objeto o una planta que puedas mirar, o las descripciones de este cuaderno.",
    "Aprenderé a recrear la forma de un objeto con mis propias decisiones, sin calcarlo. Sirve para que mis dibujos sean míos y se parezcan a lo que observo.",
    ["Sé distinguir formas figurativas y no figurativas.", "Sé dibujar el contorno de un objeto mirándolo."],
    [
        "Calcar es poner un papel transparente sobre un dibujo y repasar sus líneas. Con eso no hay observación ni decisión propia. Recrear una forma es mirarla, entender cómo es y dibujarla a mi manera. La recreación puede parecerse mucho al objeto o puede cambiar su tamaño, su color o sus líneas para expresar una idea.",
        "Para recrear sin calcar, sigue estos pasos. Primero, observa el objeto y busca sus formas simples. Segundo, haz un contorno suave con el lápiz y compara los tamaños: ¿qué es más grande, qué es más pequeño? Tercero, decide qué cambias: puedes agrandar una parte, simplificar el borde o usar colores que no son los reales. Cuarto, revisa si tu dibujo aún se reconoce.",
        "Una recreación tiene dos partes: lo que mantengo del objeto real, para que se reconozca, y lo que cambio por decisión mía. Por ejemplo, si dibujo una hoja con los bordes más puntiagudos para mostrar fuerza, mantengo su forma de hoja y cambio los bordes. Dibuja sin apuro, corrige lo que no te convenza y escribe qué mantuviste y qué cambiaste.",
    ],
    [("calcar", "poner un papel sobre una imagen y repasar sus líneas"), ("recrear", "dibujar algo a mi manera después de observarlo"), ("proporción", "relación de tamaño entre las partes de algo"), ("simplificar", "dibujar solo lo principal de una forma"), ("decisión propia", "elección que hago yo y que no viene de otro dibujo")],
    [
        w("Mantener y cambiar", "Observas una hoja de planta ovalada con punta. Quieres expresar fuerza con tu recreación. ¿Qué mantienes y qué cambias?", ["Mantengo la forma ovalada con punta para que se reconozca.", "Cambio los bordes: los hago más puntiagudos para mostrar fuerza.", "Reviso que aún se reconozca como hoja."], "Mantengo la forma de hoja y cambio los bordes"),
        w("Comparar proporciones", "En la taza que observas, el asa es mucho más chica que el cuerpo. En tu dibujo, el asa mide casi lo mismo que el cuerpo. ¿Qué haces?", ["Comparo los tamaños: en la taza real, el asa es más pequeña.", "Borro el asa y la dibujo más pequeña.", "Vuelvo a mirar la taza para revisar."], "Dibujo el asa más pequeña que el cuerpo"),
    ],
    [
        m("Calcar el contorno de una foto y decir que lo dibujé yo.", "No hubo observación ni decisiones propias.", "Mira el objeto y dibuja el contorno a mano, a tu manera."),
        m("Cambiar tanto la forma que ya no se reconoce y no explicarlo.", "Se perdió lo que se quería mostrar.", "Mantén lo principal y cambia solo una o dos cosas."),
    ],
    [
        ex("Calcar es poner un papel sobre un dibujo y repasar sus líneas. ¿Hay decisión propia al calcar?", "No", "Solo se repiten las líneas de otro."),
        ex("Recrear es mirar un objeto y dibujarlo a mi manera. ¿Es lo mismo que calcar?", "No", "Al recrear, observo y decido; al calcar, repaso."),
        ex("Quieres revisar si el asa de la taza es más grande o más pequeña que el cuerpo. ¿Qué comparas: tamaños o colores?", "Tamaños", "La proporción es la relación de tamaño entre las partes."),
    ],
    [
        ex("En tu recreación mantienes la forma de hoja y cambias los bordes a puntiagudos. ¿Qué mantuviste: la forma de hoja o los bordes?", "La forma de hoja", "Los bordes son lo que cambiaste."),
        ex("¿Qué es mejor para una recreación propia: mirar el objeto mientras dibujo o mirar solo mi dibujo?", "Mirar el objeto mientras dibujo", "Así observo detalles reales y decido qué cambiar."),
        ex("Dibujas una pera y haces la parte de abajo mucho más grande que la de arriba, y se sigue reconociendo la pera. ¿Qué hiciste: cambiar una proporción o calcar?", "Cambiar una proporción", "Decidiste agrandar una parte."),
    ],
    [
        ex("Observas una taza con el asa pequeña. Quieres expresar humor y dibujas el asa gigante. ¿Qué cambiaste: el color o la proporción?", "La proporción", "Cambiaste el tamaño del asa en relación con el cuerpo."),
        ex("Quieres recrear una hoja con tres colores que no son los reales, por ejemplo azul, rosado y naranja. ¿Se sigue reconociendo la hoja si mantienes su forma?", "Sí", "La forma sigue siendo la de una hoja."),
        ex("Ordena los pasos: A) decidir qué cambio, B) observar y buscar formas simples, C) revisar si se reconoce. Escribe las tres letras en orden.", "B, A, C", "Primero observas, luego decides y al final revisas."),
    ],
    [
        ex("Una niña dice: «Mi dibujo es una recreación porque cambié el color de la hoja de verde a violeta, pero mantuve su forma». ¿Su explicación indica qué mantuvo y qué cambió?", "Sí", "Dice que mantuvo la forma y cambió el color."),
        ex("Un niño pone un papel transparente sobre la foto de una flor y la repasa con lápiz. Dice que es su recreación. ¿Es una recreación?", "No", "Calcar no incluye observación ni decisiones propias."),
    ],
    [
        ex("Quieres recrear un zapato que se ve muy pesado, pero quieres que parezca liviano. ¿Dibujas la suela muy gruesa o muy delgada?", "Muy delgada", "Una suela delgada hace que el zapato se vea liviano."),
        ex("Observas una botella baja y ancha. Quieres que tu recreación se vea alta y delgada. ¿Qué cambias: su proporción, haciéndola más alta y angosta, o solo su color?", "Su proporción", "Para que se vea alta y delgada hay que cambiar la relación entre su alto y su ancho; el color no lo logra."),
    ],
    ex("En clase te piden hacer una recreación de un objeto del patio para la exposición del curso. Tienes una foto impresa. Una compañera te sugiere calcarla. ¿Qué haces: observas un objeto real y dibujas a tu manera o la calcas?", "Observas un objeto real y dibujas a tu manera", "Así tu trabajo tiene observación y decisiones propias."),
    [
        ex("¿Qué significa calcar?", "Repasar las líneas de una imagen puesta debajo", "Se copia sin observar ni decidir."),
        ex("Verdadero o falso: una recreación puede cambiar el color o la proporción de un objeto.", "Verdadero", "Esas son decisiones propias."),
        ex("¿Qué debes revisar al final de tu recreación?", "Que aún se reconozca", "Se debe mantener lo principal."),
    ],
    task(
        "Elige UN objeto para observar: A) una hoja de planta; B) una taza o un vaso de plástico; C) un zapato. Haz una recreación sin calcar: dibuja su contorno mirándolo, compara los tamaños de sus partes, decide qué cambias (color, proporción o borde) y revisa que se reconozca. Escribe qué mantuviste y qué cambiaste.",
        "Elegí la hoja. Mantuve su forma ovalada con punta. Cambié los bordes a puntiagudos y usé tonos de violeta para expresar fuerza. Se reconoce porque la forma es de hoja.",
        ["observa el objeto y no calca", "compara tamaños de sus partes", "cambia algo por decisión propia", "escribe qué mantuvo y qué cambió"],
        ["dibujo", "frase con lo mantenido y lo cambiado"],
        ["calcar", "cambiar tanto que ya no se reconoce"],
        "Valora la decisión propia y pregunta qué cambiaría si quisiera expresar una idea opuesta.",
    ),
    "Mira un objeto de tu casa y di qué parte cambiarías para que parezca más fuerte y cuál mantendrías.",
    "Haz tres recreaciones del mismo objeto cambiando una cosa distinta cada vez y anota qué sensación da cada una.",
)

"""Cuaderno del estudiante de 5.º básico Artes Visuales: AR05 OA 01 (crear desde el entorno cultural, el entorno artístico y el diseño)."""
from __future__ import annotations

from student_lessons import ex, register

OA1 = "AR05 OA 01"


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
    "Una hoja, un lápiz de mina y lápices de colores. Para observar puedes usar un paisaje real (una plaza, un cerro, el cielo desde la ventana) o las escenas escritas en esta clase.",
    "Aprenderé a mirar un paisaje de Chile, anotar lo que veo y escribir una intención: lo que quiero comunicar con mi obra y por qué. Sirve para que mi trabajo tenga una idea propia desde el comienzo.",
    ["Sé hacer un croquis y anotar forma, color, textura, tamaño y movimiento.", "Sé que una opinión no es lo mismo que un dato que se ve."],
    [
        "Chile es largo y angosto, y por eso sus paisajes cambian mucho. En el norte está el desierto de Atacama, seco y de colores claros. En el centro hay valles con campos de cultivo. En el sur hay bosques con mucha lluvia, lagos y volcanes. En el extremo sur hay glaciares. A esto se suman las costumbres de las personas: cómo trabajan, celebran y viven en cada lugar.",
        "Una intención es lo que quiero comunicar con mi obra. Se puede escribir con tres partes: qué quiero mostrar, cómo lo voy a mostrar y por qué. Ejemplo: «Quiero mostrar la soledad del desierto, usando mucho espacio vacío y un solo árbol pequeño, porque ahí se siente lo grande que es el lugar». Una observación dice lo que se ve. La intención dice lo que yo quiero hacer con eso que vi.",
        "Mirar bien viene antes de decidir. Primero hago un croquis y anoto datos. Después elijo qué me llamó la atención y escribo mi intención. Dos personas pueden mirar el mismo paisaje y tener intenciones distintas, y las dos pueden ser buenas. Lo importante es que la intención sea clara y que se pueda ver en las decisiones del dibujo: tamaños, colores, líneas y espacios.",
    ],
    [("entorno cultural", "los lugares, paisajes y costumbres de las personas de un territorio"), ("intención", "lo que quiero comunicar con mi obra y por qué"), ("observación", "un dato que se ve y se puede comprobar"), ("referente", "obra o lugar que miro para inspirarme, sin copiarlo"), ("croquis", "dibujo rápido que muestra lo principal")],
    [
        w("De la observación a la intención", "Observas un lago del sur: agua verde oscura, orillas con árboles muy altos y una neblina que cubre la mitad de un volcán. Escribe una intención con qué, cómo y por qué.", ["Qué llama mi atención: la neblina que esconde el volcán.", "Cómo lo muestro: con colores grises claros que tapan la parte de arriba del volcán.", "Por qué: porque quiero que se sienta el misterio del lugar."], "Quiero mostrar el misterio del lago, con grises claros que tapan el volcán, porque la neblina lo esconde."),
        w("Revisar si es una intención", "Un compañero escribió: «Dibujaré un cerro con nieve». ¿Es una intención completa?", ["Dice qué dibujará: un cerro con nieve.", "No dice cómo lo hará ni por qué.", "Falta lo que quiere comunicar."], "No, solo dice el tema; faltan el cómo y el por qué"),
    ],
    [
        m("Escribir como intención solo el tema: «voy a dibujar un lago».", "El tema no dice qué quiero comunicar.", "Agrega qué quiero mostrar, cómo y por qué."),
        m("Escribir la intención sin mirar el paisaje y después dibujar otra cosa.", "La obra no se parece a lo que se quería comunicar.", "Mira primero, anota datos y recién después escribe la intención."),
    ],
    [
        ex("¿Cuál frase es una intención? A: «Hay un cerro con nieve». B: «Quiero mostrar la soledad del desierto con mucho espacio vacío».", "B", "La B dice qué se quiere comunicar; la A solo describe lo que se ve."),
        ex("En «Quiero mostrar la calma de un lago usando colores claros», ¿qué es lo que se quiere mostrar?", "La calma de un lago", "Lo que se quiere mostrar viene después de «quiero mostrar»."),
        ex("¿El desierto de Atacama está en el norte o en el sur de Chile?", "En el norte", "Atacama es el desierto del norte del país."),
    ],
    [
        ex("Una intención tiene tres partes: qué, cómo y por qué. En «porque ahí se siente lo grande que es el lugar», ¿qué parte aparece?", "El por qué", "La palabra «porque» introduce la razón de la obra."),
        ex("Una alumna observa un valle: campos de cultivo en filas ordenadas y cerros lejanos. ¿Qué intención parte de lo que vio? A: «Quiero mostrar el orden de los campos con líneas paralelas». B: «Quiero mostrar una selva con monos».", "A", "La A usa las filas ordenadas que la alumna observó; la B no tiene relación con el valle."),
        ex("Escribe «observación» o «intención»: «Los glaciares se ven blancos y celestes claros».", "Observación", "Dice un dato que se puede ver y no lo que se quiere comunicar."),
    ],
    [
        ex("Ordena los pasos: A) escribir la intención, B) mirar y anotar datos, C) decidir colores y formas. Escribe las tres letras en orden.", "B, A, C", "Primero se mira, luego se decide la intención y después se eligen los recursos."),
        ex("Tu intención es mostrar el frío del sur de Chile. ¿Qué paleta usas? A: azul, gris y blanco. B: naranjo, rojo y amarillo.", "A", "Los azules, grises y blancos dan sensación de frío."),
        ex("Quieres mostrar mucha lluvia y plantas. ¿Qué zona observas mejor: los bosques del sur o el desierto del norte?", "Los bosques del sur", "En el sur llueve mucho y hay bosques; el desierto es seco."),
    ],
    [
        ex("Ema quiere mostrar la calma de un lago con líneas largas y horizontales. Beto quiere mostrar su fuerza con olas quebradas. ¿Pueden ser válidas las dos intenciones sobre el mismo lago?", "Sí", "La observación es la misma, pero cada autor decide qué comunicar."),
        ex("Una niña escribe: «Quiero que mi dibujo sea bonito». ¿Es una intención clara?", "No", "No dice qué quiere mostrar ni cómo; «bonito» es una opinión."),
    ],
    [
        ex("Julia escribió: «Quiero mostrar el viento en la pampa con líneas curvas largas». ¿Qué parte de la intención le falta?", "El por qué", "Tiene el qué (el viento) y el cómo (líneas curvas), pero no dice la razón."),
        ex("Dos intenciones: 1) «Mostrar la altura de un volcán dibujándolo solo, sin nada al lado» y 2) «Mostrar la altura de un volcán con muchas casas pequeñas al lado». Si quieres que el tamaño del volcán se note por comparación, ¿cuál sirve más: la 1 o la 2?", "La 2", "Las casas pequeñas al lado dan algo con qué comparar, y el volcán se ve mucho más grande."),
    ],
    ex("Estás en una plaza y ves un árbol cuyas hojas se mueven con el viento. Quieres mostrar ese movimiento. ¿Qué haces primero: un croquis con notas o pintar el cuadro final de inmediato?", "Un croquis con notas", "El croquis y las notas guardan los datos para decidir bien después."),
    [
        ex("Verdadero o falso: «Hay un cerro con nieve» es una intención.", "Falso", "Es una observación; no dice qué se quiere comunicar."),
        ex("¿Qué tres partes tiene una intención completa?", "Qué, cómo y por qué", "Así se dice qué mostrar, con qué decisiones y la razón."),
        ex("Verdadero o falso: dos personas pueden mirar el mismo paisaje y tener intenciones distintas.", "Verdadero", "Cada persona decide qué comunicar con lo que ve."),
    ],
    task(
        "Elige UNA escena. A) Un desierto de arena clara, con un solo árbol pequeño y un cielo enorme. B) Un bosque lluvioso con árboles muy altos, helechos verdes y gotas que caen. C) Un puerto con botes de colores, gaviotas y gente que descarga cajas. Haz un croquis, anota cinco datos de lo que ves (forma, color, textura, tamaño y movimiento) y escribe tu intención con qué, cómo y por qué.",
        "Elegí la A. Datos: el árbol tiene forma de paraguas; la arena es beige; la textura es lisa; el árbol es muy pequeño frente al cielo; no hay movimiento. Intención: quiero mostrar la soledad del desierto, con un árbol pequeño y mucho espacio vacío, porque así se siente lo grande que es el lugar.",
        ["hace un croquis", "anota cinco datos y no solo opiniones", "escribe una intención con qué, cómo y por qué", "la intención se relaciona con los datos"],
        ["croquis", "cinco datos", "una intención de tres partes"],
        ["escribir solo el tema", "mezclar opiniones con datos"],
        "Destaca una intención que se pueda ver en el croquis y pregunta qué decisión del dibujo la muestra.",
    ),
    "Mira por la ventana un minuto y di en voz alta un dato que ves y una intención posible para dibujarlo.",
    "Escribe dos intenciones distintas para el mismo paisaje y di cuál cambiaría más el dibujo.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Hoja, témpera o lápices de colores y un pincel o un palito de algodón. Las descripciones de obras están escritas aquí; no necesitas buscarlas.",
    "Aprenderé qué fue el impresionismo y probaré una variable visual: pinceladas cortas para mostrar cómo la luz cambia los colores. Sirve para crear un paisaje con una intención sobre la luz.",
    ["Sé escribir una intención con qué, cómo y por qué.", "Sé que la luz del día cambia los colores que veo."],
    [
        "El impresionismo es un estilo de pintura que nació en Francia en el siglo XIX. Su nombre viene de un cuadro de Claude Monet que se llama «Impresión, sol naciente». Los pintores impresionistas salían a pintar al aire libre. Querían captar lo que ven en un momento: cómo la luz toca el agua, el cielo y las cosas. Por eso pintaban rápido.",
        "Estos pintores usaban pinceladas cortas y visibles. Ponían manchas de colores una al lado de la otra, sin mezclarlas del todo. De lejos, el ojo las junta y se ve la luz moverse. Muchas veces las sombras no eran negras: eran azules, violetas o verdes. Una variable visual es una decisión que puedo cambiar para ver su efecto. Aquí la variable es el tamaño y la dirección de las pinceladas.",
        "Para probar, hago dos manchas pequeñas del mismo paisaje: una con pinceladas largas y lisas, y otra con pinceladas cortas y de varios colores. Comparo cuál muestra mejor el brillo del agua o el cambio de la luz. No copio un cuadro impresionista: uso la idea, pero mi paisaje y mi intención son propios. Pinto un lugar de Chile, como la orilla de un lago, un cerro o el mar.",
    ],
    [("impresionismo", "estilo de pintura del siglo XIX que capta la luz de un momento con pinceladas cortas"), ("al aire libre", "afuera, mirando directamente el paisaje"), ("pincelada", "huella que deja el pincel al pintar"), ("variable visual", "una decisión que puedo cambiar para ver su efecto"), ("luz", "lo que hace que veamos los colores y que cambia durante el día")],
    [
        w("Elegir la variable", "Quieres mostrar el brillo del agua del mar al mediodía. Pruebas A) pinceladas largas y lisas de azul, y B) pinceladas cortas de azul, celeste, blanco y verde. ¿Cuál elegir?", ["El brillo cambia y se mueve, y eso se muestra con muchas manchas distintas.", "La prueba B tiene manchas cortas de colores claros junto a otros.", "La prueba A se ve pareja y sin brillo."], "La prueba B"),
        w("Sombras con color", "Un impresionista pinta la sombra de un árbol sobre la arena. ¿Qué color usa más probablemente para esa sombra?", ["Los impresionistas evitaban el negro puro en las sombras.", "Usaban colores como azul o violeta.", "Por eso la sombra se ve con color y luz."], "Azul o violeta, no negro"),
    ],
    [
        m("Pensar que impresionismo significa copiar un cuadro de Monet.", "El estilo es una forma de mirar y pintar, no una imagen para repetir.", "Usa la idea de la luz y pinta tu propio paisaje."),
        m("Mezclar todas las manchas hasta que queden lisas.", "Se pierde el efecto de luz en movimiento.", "Deja las pinceladas visibles y al lado unas de otras."),
    ],
    [
        ex("¿En qué país nació el impresionismo?", "En Francia", "Los pintores impresionistas partieron en Francia en el siglo XIX."),
        ex("¿Cómo se llama el cuadro de Monet que dio nombre al estilo: «Impresión, sol naciente» o «La noche estrellada»?", "Impresión, sol naciente", "El nombre «impresionismo» viene de ese título."),
        ex("Los impresionistas pintaban «al aire libre». ¿Significa que pintaban afuera o dentro de un taller cerrado?", "Afuera", "Al aire libre es afuera, mirando el paisaje."),
    ],
    [
        ex("¿Qué se logra con pinceladas cortas de varios colores puestas una al lado de otra: una superficie lisa o la sensación de luz en movimiento?", "La sensación de luz en movimiento", "Las manchas visibles hacen que el color vibre y parezca moverse."),
        ex("¿Qué quería captar un pintor impresionista: la luz de un momento o cada detalle exacto de las hojas?", "La luz de un momento", "Pintaban rápido para atrapar cómo la luz toca las cosas."),
        ex("Describes un paisaje: «Manchas cortas de amarillo, blanco y naranjo en el agua, al atardecer». ¿Qué momento del día muestra: el atardecer o la noche cerrada?", "El atardecer", "Los colores cálidos y claros indican la luz del atardecer."),
    ],
    [
        ex("Quieres mostrar un lago en calma, sin viento. ¿Qué pinceladas te sirven más: cortas y en zigzag o largas y horizontales?", "Largas y horizontales", "Las pinceladas horizontales dan sensación de agua quieta."),
        ex("Quieres mostrar que el sol cambia los colores de un cerro durante el día. Haces tres pruebas pequeñas. ¿Cómo las organizas: mañana, mediodía y tarde, o tres mañanas?", "Mañana, mediodía y tarde", "La luz cambia durante el día, y por eso se necesitan momentos distintos."),
        ex("Pintas la sombra de una casa blanca sobre el pasto verde. ¿Qué color eliges para la sombra: un verde azulado o negro puro?", "Un verde azulado", "Es un color con luz, como en el impresionismo; el negro puro la dejaría sin vida."),
    ],
    [
        ex("Prueba A: pinceladas largas y lisas. Prueba B: pinceladas cortas y de varios colores. Tu intención es mostrar el movimiento del mar con viento. ¿Qué prueba muestra mejor tu intención?", "La prueba B", "Las manchas cortas y variadas dan sensación de agua que se mueve."),
        ex("Una compañera dice: «Pinté igual que Monet, así que mi obra es impresionista». Ella copió un paisaje de él. ¿Su obra muestra una idea propia?", "No", "Copiar un cuadro no muestra una intención propia; la idea es mirar y pintar tu propio paisaje."),
    ],
    [
        ex("Quieres mostrar las hojas de un árbol que se mueven con el viento, con luz que pasa entre ellas. ¿Qué haces: muchas manchas cortas verdes y amarillas, o una sola mancha verde lisa?", "Muchas manchas cortas verdes y amarillas", "Las manchas cortas con luz entre ellas dan sensación de movimiento."),
        ex("Quieres pintar el reflejo del sol sobre el agua. ¿Qué color usas para el reflejo: un amarillo claro cerca de manchas azules o un café oscuro?", "Un amarillo claro cerca de manchas azules", "Un color claro junto a uno más oscuro hace que el reflejo brille."),
    ],
    ex("Una amiga te pide ayuda: pintó un cerro con colores lisos y quiere que se vea cómo cambia la luz. ¿Qué le propones: agregar manchas cortas de colores distintos o pintar todo con un solo color?", "Agregar manchas cortas de colores distintos", "Las manchas distintas muestran los cambios de luz sobre el cerro."),
    [
        ex("Verdadero o falso: los impresionistas pintaban siempre sus sombras con negro puro.", "Falso", "Solían usar colores como azul y violeta en las sombras."),
        ex("¿Qué es una variable visual?", "Una decisión que puedo cambiar para ver su efecto", "Cambiar una cosa a la vez permite comparar resultados."),
        ex("Verdadero o falso: pintar con pinceladas cortas es una forma de captar la luz de un momento.", "Verdadero", "Las manchas cortas muestran cómo la luz toca las cosas."),
    ],
    task(
        "Elige UNA escena. A) La orilla de un lago con un volcán al fondo, al amanecer. B) El mar con botes pequeños al mediodía. C) Un cerro con pasto seco al atardecer. Haz dos pruebas pequeñas del mismo paisaje: una con pinceladas largas y lisas, y otra con pinceladas cortas de varios colores. Escribe tu intención sobre la luz, elige una prueba y explica por qué.",
        "Elegí la B. Intención: quiero mostrar el brillo del mar al mediodía, con manchas cortas de azul y blanco, porque la luz se mueve. La prueba con pinceladas cortas se ve más brillante; la elegí. Cambié una sombra de negro a azul oscuro.",
        ["hace dos pruebas distintas", "escribe una intención sobre la luz", "elige con una razón que se ve", "no copia un cuadro conocido"],
        ["dos pruebas", "obra final", "intención y razón"],
        ["copiar un cuadro", "dejar las dos pruebas iguales"],
        "Muestra la prueba donde mejor se nota la luz y pregunta qué hizo la diferencia: el color o el tamaño de la mancha.",
    ),
    "Mira el cielo un momento y di en voz alta tres colores distintos que ves ahora.",
    "Haz la misma prueba a otra hora del día y anota cómo cambian los colores.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hoja, lápices de colores o plumones, punta de lápiz o palito de algodón para hacer puntos, y témpera si tienes. Las descripciones de los pintores están escritas aquí.",
    "Aprenderé qué fue el postimpresionismo y elegiré un procedimiento (puntos, pincelada gruesa, formas simples o colores planos) según mi intención. Sirve para que la técnica que uso tenga una razón.",
    ["Sé que el impresionismo captó la luz de un momento con pinceladas cortas.", "Sé escribir una intención y probar una variable visual."],
    [
        "El postimpresionismo agrupa a pintores que trabajaron después de los impresionistas, sobre todo en Francia, a fines del siglo XIX. Conservaron los colores vivos, pero buscaron algo distinto: expresar sentimientos, ordenar las formas o inventar sus propios colores. Cada artista tenía un estilo muy propio. No es un solo estilo, sino varios caminos.",
        "Cuatro ejemplos. Vincent van Gogh pintaba con pintura gruesa y pinceladas que giran, para mostrar emoción. Georges Seurat ponía muchos puntos pequeños de colores puros; de lejos, el ojo los junta. Paul Cézanne construía las formas con volúmenes simples, como cilindros y esferas. Paul Gauguin usaba áreas grandes de color plano y fuerte. Un procedimiento es la manera de hacer una obra; cada uno de ellos tenía el suyo.",
        "Para elegir un procedimiento, me pregunto qué quiero comunicar. Si quiero emoción fuerte, sirven las pinceladas gruesas que giran. Si quiero que el paisaje se vea ordenado y luminoso, sirven los puntos. Si quiero que los objetos se vean sólidos, uso formas simples. Si quiero una imagen audaz, uso colores planos. En los materiales, puedo usar témpera, plumones o lápices: lo importante es que la técnica combine con mi intención.",
    ],
    [("postimpresionismo", "grupo de estilos posteriores al impresionismo, con colores vivos y expresión personal"), ("procedimiento", "la manera de hacer una obra"), ("puntillismo", "técnica de poner muchos puntos de color puro, uno al lado del otro"), ("color plano", "área de un solo color, sin degradé"), ("expresar", "mostrar un sentimiento o una idea con la obra")],
    [
        w("Elegir según la intención", "Tu intención es mostrar un cielo de tormenta lleno de emoción fuerte. ¿Qué procedimiento eliges: puntos pequeños y ordenados, o pinceladas gruesas que giran?", ["La emoción fuerte pide movimiento.", "Las pinceladas gruesas que giran muestran fuerza.", "Los puntos ordenados dan una imagen tranquila."], "Pinceladas gruesas que giran"),
        w("Puntillismo con lápices", "Quieres pintar una pradera luminosa con lápices de colores. ¿Cómo aplicas la idea de Seurat?", ["Hago muchos puntos pequeños de colores puros.", "Pongo puntos amarillos y verdes uno al lado de otro.", "De lejos se juntan y brilla la pradera."], "Con puntos de verde y amarillo, uno al lado de otro"),
    ],
    [
        m("Elegir el procedimiento solo porque es el que más me gusta.", "No se relaciona con lo que quiero comunicar.", "Pregúntate qué efecto tiene la técnica y si ayuda a tu intención."),
        m("Decir que todos los postimpresionistas pintaban igual.", "Eran varios artistas con estilos distintos.", "Recuerda que es un grupo de caminos diferentes."),
    ],
    [
        ex("¿Qué técnica usaba Seurat: puntos pequeños de color puro o pinceladas gruesas que giran?", "Puntos pequeños de color puro", "Seurat es conocido por el puntillismo."),
        ex("¿Cuál artista pintaba con pintura gruesa y pinceladas que giran: Van Gogh o Seurat?", "Van Gogh", "Su pintura gruesa mostraba emoción."),
        ex("¿Qué es un procedimiento en arte?", "La manera de hacer una obra", "Incluye los pasos y las herramientas que usa el autor."),
    ],
    [
        ex("Un cuadro muestra áreas grandes de un solo color fuerte, sin degradé. ¿Qué nombre tiene esa forma de pintar: color plano o puntillismo?", "Color plano", "El color plano es un área de un solo color."),
        ex("Cézanne construía las formas con volúmenes simples. ¿Qué formas usaba: cilindros y esferas, o puntos de color puro?", "Cilindros y esferas", "Buscaba que los objetos se vieran sólidos."),
        ex("Lees: «El postimpresionismo vino antes que el impresionismo». ¿Es verdadero o falso?", "Falso", "Vino después del impresionismo."),
    ],
    [
        ex("Tu intención es mostrar un campo ordenado y luminoso. ¿Qué procedimiento sirve más: puntos de colores puros o una sola mancha negra gruesa?", "Puntos de colores puros", "Los puntos juntos dan luz y orden a la imagen."),
        ex("Quieres que una manzana dibujada se vea sólida y pesada. ¿Qué haces: construirla con formas simples como una esfera o dibujarla solo con una línea muy fina?", "Construirla con formas simples como una esfera", "Una forma simple con volumen da sensación de peso."),
        ex("Quieres un afiche de un cerro con colores audaces y planos. ¿Qué haces con el cielo: pintarlo de un solo color fuerte o pintar mil puntos de colores?", "Pintarlo de un solo color fuerte", "Eso es color plano."),
    ],
    [
        ex("Ana eligió pinceladas gruesas que giran para mostrar alegría tranquila en un campo. Luis le dice que eso muestra más emoción fuerte que calma. ¿Tiene razón Luis?", "Sí", "Las pinceladas que giran dan movimiento y emoción; para calma sirven líneas suaves o puntos ordenados."),
        ex("Una niña usa puntos porque «todos los artistas usan puntos». ¿Es una buena razón para elegir un procedimiento?", "No", "La razón debe relacionarse con su intención, no con lo que hacen los demás."),
    ],
    [
        ex("Quieres que un dibujo de una cordillera transmita emoción fuerte y movimiento. Pruebas A) pinceladas gruesas que giran en el cielo, y B) colores planos sin textura. ¿Cuál se acerca más a Van Gogh y a tu intención?", "A", "Las pinceladas gruesas que giran muestran emoción y movimiento."),
        ex("Quieres comparar dos procedimientos para la misma intención: «mostrar un amanecer sereno». Pruebas A) puntos amarillos y celestes, y B) rayas negras gruesas y cortadas. ¿Cuál se acerca más a la intención?", "A", "Los puntos amarillos y celestes dan una luz suave y serena."),
    ],
    ex("Quieres hacer un mural escolar sobre el mar, pero no tienes témpera. Tienes lápices de colores. ¿Qué cambias para seguir usando una idea de Seurat: haces el mar con puntos de lápiz o abandonas la idea?", "Hago el mar con puntos de lápiz", "La técnica se puede adaptar a otros materiales."),
    [
        ex("Verdadero o falso: el postimpresionismo es un solo estilo igual para todos.", "Falso", "Eran varios artistas con caminos propios."),
        ex("¿Qué pintor usó formas simples como cilindros y esferas?", "Cézanne", "Buscaba el orden y el volumen en las formas."),
        ex("Verdadero o falso: elegir un procedimiento debe relacionarse con lo que quiero comunicar.", "Verdadero", "El procedimiento es parte de la intención."),
    ],
    task(
        "Elige UNA intención: A) mostrar la emoción de una tormenta en el mar; B) mostrar un campo luminoso y ordenado; C) mostrar un cerro sólido y pesado. Elige UN procedimiento que combine con ella: pinceladas gruesas que giran, puntos de colores puros, formas simples o colores planos. Haz una prueba pequeña y la obra final. Explica en una frase por qué elegiste ese procedimiento.",
        "Elegí la intención B y puntos de colores puros. Pinté el campo con puntos verdes y amarillos y el cielo con puntos celestes. Elegí puntos porque se juntan de lejos y dan luz y orden. No copié un cuadro de Seurat: mi paisaje es de un campo de Chile.",
        ["elige un procedimiento que combina con la intención", "hace una prueba y la obra final", "explica la razón en una frase", "no copia a un pintor"],
        ["prueba", "obra final", "una frase con la razón"],
        ["elegir por gusto", "copiar el estilo de un pintor sin intención propia"],
        "Reconoce la razón mejor relacionada con la intención y pregunta qué cambiaría si la intención fuera la opuesta.",
    ),
    "Cierra los ojos y piensa en una emoción. Di en voz alta qué procedimiento usarías para mostrarla.",
    "Haz la misma intención con dos procedimientos distintos y anota cuál se parece más a lo que querías comunicar.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hoja grande o dos hojas pegadas, lápices de colores o témpera. Las situaciones de costumbres están escritas aquí; si quieres, conversa con una persona de tu casa o de tu barrio sobre cómo se hacía antes.",
    "Aprenderé a crear una obra propia sobre una costumbre de Chile, mostrando cómo era en el pasado y cómo es hoy. Sirve para expresar con una idea propia cómo cambian y se mantienen las costumbres.",
    ["Sé escribir una intención con qué, cómo y por qué.", "Sé que el procedimiento se elige según lo que quiero comunicar."],
    [
        "Una costumbre es algo que un grupo de personas hace de manera repetida: cómo celebra, cómo trabaja, qué come, cómo se divierte. Algunas costumbres de Chile se mantienen por mucho tiempo, como juntarse a celebrar las Fiestas Patrias o ir a una feria a comprar frutas y verduras. Otras cambian: cambian los objetos, la ropa, los medios de transporte y las herramientas.",
        "Para crear una respuesta propia, miro la costumbre en dos momentos: antes y hoy. Anoto qué cambió (por ejemplo, los objetos o la ropa) y qué sigue igual (por ejemplo, las personas reunidas). Luego decido mi intención: mostrar el cambio, mostrar lo que se mantiene o mostrar ambos. Dividir la hoja en dos partes es una buena forma de mostrar el antes y el hoy.",
        "Una respuesta propia no copia una foto ni el dibujo de un compañero. Uso una composición que yo decido: qué va grande, qué va pequeño, dónde pongo la mirada. Para el pasado puedo usar colores más apagados, como los de una foto antigua. Para hoy, colores más vivos. Si no tengo certeza de cómo se vivía antes, pregunto a una persona mayor o dejo claro que es mi interpretación.",
    ],
    [("costumbre", "algo que un grupo de personas hace de manera repetida"), ("pasado", "lo que ya ocurrió, antes de hoy"), ("presente", "lo que ocurre hoy"), ("composición", "la forma en que ordeno lo que dibujo en la hoja"), ("interpretación", "mi manera de mostrar algo, que no es una copia")],
    [
        w("Antes y hoy", "Imagina esta situación. La costumbre es comprar en la feria. Antes: se pagaba solo con monedas y billetes y se cargaban bolsas de género. Hoy: se puede pagar también con tarjeta y se usan bolsas reutilizables. ¿Qué se mantiene igual?", ["Reviso qué hay en común.", "Siempre hay personas que compran y venden.", "Lo que cambió son las formas de pago y las bolsas."], "Se mantienen las personas que compran y venden en la feria"),
        w("Dividir la hoja", "Quieres mostrar una cosecha de manzanas antes y hoy. ¿Cómo organizas la hoja?", ["Divido la hoja en dos partes.", "A la izquierda dibujo el antes con colores apagados.", "A la derecha dibujo el hoy con colores más vivos."], "Dos partes: antes a la izquierda y hoy a la derecha"),
    ],
    [
        m("Dibujar solo el pasado y olvidar mostrar el presente.", "No se ve el cambio ni lo que se mantiene.", "Muestra los dos momentos de manera que se puedan comparar."),
        m("Copiar el dibujo de un compañero o una foto sin cambiar nada.", "La obra no tiene una composición propia.", "Decide tú qué va grande, qué va pequeño y qué colores usas."),
    ],
    [
        ex("Una costumbre es algo que un grupo hace de manera repetida. Ir todas las semanas a una feria es algo que hace una comunidad. ¿Eso es una costumbre o un hecho que ocurrió una sola vez?", "Una costumbre", "Se hace de manera repetida."),
        ex("Para mostrar el antes y el hoy en una hoja, ¿la divides en dos partes o la dejas sin dividir?", "La divides en dos partes", "Así se pueden comparar los dos momentos."),
        ex("¿Qué colores usas para el pasado en la clase: más apagados o más vivos?", "Más apagados", "Los colores apagados se parecen a los de una foto antigua."),
    ],
    [
        ex("Lees: «Antes se llevaban las frutas en carretas tiradas por bueyes; hoy se llevan en camiones». ¿Qué cambió: el medio de transporte o el nombre de la fruta?", "El medio de transporte", "Cambió cómo se llevan las frutas."),
        ex("Una foto antigua de una feria muestra vendedores con delantal de tela y una balanza de dos platos. Hoy usan una balanza digital. ¿Qué cambió: la balanza o que existan vendedores?", "La balanza", "Los vendedores siguen estando; solo cambió el objeto con que pesan."),
        ex("Un dibujo muestra dos momentos de una cosecha de maíz. Antes: una familia cosecha a mano con canastos. Hoy: una familia cosecha con una cosechadora. ¿Qué objeto es del presente: la cosechadora o los canastos?", "La cosechadora", "La cosechadora es la máquina de hoy; los canastos son del pasado. La familia aparece en los dos momentos."),
    ],
    [
        ex("Tu intención es mostrar lo que se mantiene. ¿Qué repites en los dos lados de la hoja: a las personas reunidas o los objetos que cambiaron?", "A las personas reunidas", "Lo que se mantiene es lo que repites."),
        ex("Quieres mostrar mucho cambio en una costumbre. ¿Cómo haces los dos lados: muy distintos en colores y objetos o casi iguales?", "Muy distintos en colores y objetos", "Para mostrar cambio, los lados deben diferenciarse."),
        ex("Ordena: A) decidir tu intención, B) anotar qué cambió y qué se mantiene, C) dibujar los dos momentos. Escribe las letras en orden.", "B, A, C", "Primero se anotan datos, luego se decide la intención y después se dibuja."),
    ],
    [
        ex("Un niño dice: «Mi dibujo del pasado es exacto porque yo lo vi». Pero él nació después de esa época. ¿Qué debe decir para ser honesto: «es mi interpretación» o «es la realidad exacta»?", "Es mi interpretación", "No lo vivió; lo imagina con la información que tiene."),
        ex("Una amiga copió el dibujo de otro compañero y le cambió el color. ¿Tiene una composición propia?", "No", "La composición es la misma que la del compañero."),
    ],
    [
        ex("Quieres mostrar que las Fiestas Patrias se celebran juntando personas en espacios abiertos, tanto antes como hoy. ¿Qué dibujas igual en los dos lados: personas reunidas al aire libre o un edificio cerrado?", "Personas reunidas al aire libre", "Eso es lo que se mantiene en tu intención."),
        ex("Tu hoja dividida muestra a la izquierda un mercado con carretas y a la derecha un mercado con camiones. Un compañero dice que no se nota qué se mantiene. ¿Qué agregas en ambos lados: personas conversando y comprando, o más camiones?", "Personas conversando y comprando", "Lo que se mantiene debe aparecer en los dos lados."),
    ],
    ex("En tu colegio piden una obra sobre una costumbre local. No sabes cómo se hacía antes en tu barrio. ¿Qué haces: preguntar a una persona mayor o inventar y decir que es real?", "Preguntar a una persona mayor", "Así obtienes información y evitas atribuir algo falso."),
    [
        ex("Verdadero o falso: todas las costumbres cambian con el tiempo.", "Falso", "Algunas se mantienen y otras cambian."),
        ex("¿Qué es una composición?", "La forma en que ordeno lo que dibujo en la hoja", "Es el orden de tamaños, lugares y colores."),
        ex("Verdadero o falso: mostrar el antes y el hoy en una hoja dividida ayuda a comparar.", "Verdadero", "Dos partes permiten ver lo que cambia y lo que sigue igual."),
    ],
    task(
        "Elige UNA costumbre: A) la feria donde se compran frutas y verduras; B) la celebración de las Fiestas Patrias en un espacio abierto; C) un juego de calle (por ejemplo, el trompo o la rayuela). Divide una hoja en dos. Dibuja el antes y el hoy. Escribe una intención (qué, cómo y por qué) y marca una cosa que cambió y una que se mantiene.",
        "Elegí la A. Intención: quiero mostrar que en la feria cambian las bolsas y las formas de pago, pero siguen las personas conversando, porque la costumbre se mantiene aunque cambien los objetos. A la izquierda dibujé bolsas de género y colores apagados; a la derecha, bolsas reutilizables y colores más vivos.",
        ["divide la hoja y muestra el antes y el hoy", "marca algo que cambió y algo que se mantiene", "escribe una intención de tres partes", "usa una composición propia"],
        ["hoja dividida", "dos momentos", "una intención"],
        ["mostrar solo uno de los momentos", "copiar una imagen"],
        "Destaca la comparación más clara entre antes y hoy y pregunta qué decisión de color o tamaño la hace visible.",
    ),
    "Conversa con una persona de tu casa o de tu barrio y anota una diferencia entre cómo se celebraba una fiesta antes y hoy.",
    "Haz una versión de tu obra que muestre cómo podría ser esa costumbre en 20 años.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hoja, lápices de colores y regla. Los ejemplos de diseño están descritos aquí; también puedes mirar objetos de tu casa (una caja, un envase, una señal).",
    "Aprenderé qué es el diseño y a fundamentar un diseño propio, pensando en para qué sirve, quién lo usa y cómo se ve. Sirve para tomar decisiones que se puedan justificar, y no solo elegir lo que se ve bonito.",
    ["Sé escribir una intención y elegir un procedimiento.", "Sé que cada objeto que uso fue diseñado por alguien."],
    [
        "El diseño es la creación de objetos e imágenes para que sirvan a las personas y se vean bien. Un afiche, un envase, una señal de tránsito, una silla o un tejido son diseños. En todo el mundo hay diseño: en Chile, por ejemplo, la cerámica de Pomaire; en Latinoamérica, los tejidos de los Andes con figuras geométricas de colores; en el resto del mundo, los pictogramas, que son dibujos simples que se entienden sin palabras.",
        "Un buen diseño tiene tres partes que se piensan juntas. La función es para qué sirve. El usuario es la persona que lo usa, como un niño de 6 años o un adulto mayor. La forma es cómo se ve: colores, tamaños, letras y formas. Si el diseño es una señal de peligro, su función es avisar rápido, y por eso tiene pocos detalles y colores muy fuertes. Si es un envase de jugo para niños, puede tener colores alegres y letras grandes.",
        "Para fundamentar mi diseño, escribo una frase: «Elegí [decisión] porque [función o usuario]». Esa frase explica por qué hice algo y no solo dice que me gusta. Puedo inspirarme en diseños de Chile, de América Latina o del resto del mundo, pero no los copio: tomo una idea, como el uso de formas geométricas en el color, y la cambio para mi propósito.",
    ],
    [("diseño", "creación de objetos e imágenes para que sirvan a las personas y se vean bien"), ("función", "para qué sirve un diseño"), ("usuario", "persona que usa un diseño"), ("pictograma", "dibujo simple que se entiende sin palabras"), ("fundamentar", "explicar con razones por qué tomé una decisión")],
    [
        w("Función, usuario y forma", "Diseñas un afiche para avisar «no correr junto a la piscina». ¿Cuál es la función, quién es el usuario y qué forma eliges?", ["Función: avisar rápido que no se debe correr.", "Usuario: niños y adultos que pasan por el lugar.", "Forma: un dibujo simple de una persona corriendo tachada, con colores muy fuertes."], "Función avisar; usuario niños y adultos; forma con dibujo simple y colores fuertes"),
        w("Fundamentar una decisión", "Elegiste letras muy grandes en el afiche. Escribe la frase «Elegí… porque…».", ["Digo la decisión: letras muy grandes.", "Digo la razón: porque las personas deben leerlo desde lejos.", "Armo la frase."], "Elegí letras muy grandes porque las personas deben leerlo desde lejos"),
    ],
    [
        m("Decir «lo elegí porque me gusta» para justificar una decisión de diseño.", "No explica la función ni al usuario.", "Explica para qué sirve el diseño y quién lo va a usar."),
        m("Copiar un diseño y cambiar solo el nombre.", "No hay una idea propia.", "Toma una idea del referente y cámbiala para tu propósito."),
    ],
    [
        ex("¿Qué es un pictograma: un dibujo simple que se entiende sin palabras o un texto largo?", "Un dibujo simple que se entiende sin palabras", "Por eso sirve en señales para todos."),
        ex("En el diseño, «función» significa para qué sirve el objeto o la imagen. ¿Cuál es la función de una señal de «alto»?", "Avisar que hay que detenerse", "La señal sirve para que los conductores se detengan."),
        ex("¿La cerámica de Pomaire es un ejemplo de diseño de Chile o de otro país?", "De Chile", "Pomaire es un lugar de Chile conocido por su cerámica."),
    ],
    [
        ex("El usuario de un afiche para un jardín infantil son niños de 4 años. ¿Qué forma es más adecuada: dibujos grandes y simples o párrafos largos?", "Dibujos grandes y simples", "Niños de 4 años aún no leen mucho."),
        ex("Un envase de leche para niños tiene colores alegres y un dibujo de una vaca. ¿Qué parte del diseño estamos describiendo: la forma o la función?", "La forma", "Describe cómo se ve."),
        ex("Un diseñador dice: «Elegí letras grandes porque las personas leerán desde lejos». ¿Qué parte tiene la razón: «las personas leerán desde lejos» o «letras grandes»?", "Las personas leerán desde lejos", "Después de «porque» se escribe la razón."),
    ],
    [
        ex("Diseñas una señal para avisar peligro de piso mojado. ¿Qué colores usas: amarillo y negro, que se ven mucho, o pastel muy claro?", "Amarillo y negro", "Son colores de alto contraste, que se ven rápido."),
        ex("Quieres diseñar un afiche para un festival de música de tu colegio. ¿Qué información debe estar escrita sí o sí: el nombre del festival, el día y la hora, o solo tu nombre?", "El nombre del festival, el día y la hora", "El afiche sirve para informar."),
        ex("Un tejido andino muestra figuras geométricas repetidas. Tú diseñas una cinta con formas geométricas, pero con tus propios colores y formas. ¿Estás copiando o tomando una idea?", "Tomando una idea", "Usas la idea de repetir figuras geométricas con decisiones propias."),
    ],
    [
        ex("Dos afiches iguales de una feria: el A tiene letras pequeñas de color amarillo claro sobre fondo blanco; el B tiene letras grandes de color azul oscuro sobre fondo blanco. ¿Cuál se lee mejor desde lejos?", "El B", "Las letras grandes y oscuras sobre blanco contrastan más."),
        ex("Un compañero dice: «Mi afiche es el mejor porque tiene más colores». ¿Es una buena razón de diseño?", "No", "Más colores no siempre mejoran la función de informar."),
    ],
    [
        ex("Rediseñas el afiche para limpiar la plaza, pensando en niños de 5 años que aún no leen. ¿Qué cambias: agregas un dibujo grande de una escoba o agregas más párrafos?", "Agregas un dibujo grande de una escoba", "Un dibujo se entiende sin saber leer."),
        ex("Quieres que un afiche sobre cuidar el agua sea entendido por personas de distintos países. ¿Qué usas: un pictograma de una gota o un texto largo en una sola lengua?", "Un pictograma de una gota", "Un dibujo simple se entiende sin palabras."),
    ],
    ex("Te piden diseñar una señal para el patio del colegio que diga «Zona de calma». ¿Qué decisión te parece mejor fundamentada: «azul claro porque transmite tranquilidad» o «rojo porque es mi favorito»?", "Azul claro porque transmite tranquilidad", "Se relaciona con la función de la zona."),
    [
        ex("Verdadero o falso: un pictograma se entiende sin palabras.", "Verdadero", "Es un dibujo simple que muchos reconocen."),
        ex("¿Qué tres partes del diseño se piensan juntas?", "Función, usuario y forma", "Son para qué sirve, quién lo usa y cómo se ve."),
        ex("Verdadero o falso: «me gusta» es suficiente para fundamentar un diseño.", "Falso", "Hay que explicar con razones relacionadas con la función o el usuario."),
    ],
    task(
        "Elige UN encargo: A) un afiche para invitar a limpiar la plaza del barrio el sábado a las 10:00; B) un envase para unas galletas hechas en casa, para niños de 6 años; C) una señal para recordar que no se debe correr en el pasillo del colegio. Diseña en una hoja: escribe función, usuario y forma. Escribe dos frases «Elegí… porque…».",
        "Elegí el encargo A. Función: invitar y dar la información. Usuario: vecinos de todas las edades. Forma: letras grandes y oscuras, un dibujo simple de una escoba y colores verdes. Elegí letras grandes porque se leen desde lejos. Elegí la escoba porque el dibujo se entiende sin leer.",
        ["escribe función, usuario y forma", "incluye la información necesaria", "escribe dos frases «Elegí… porque…»", "toma una idea de un referente sin copiarlo"],
        ["hoja con el diseño", "tres partes escritas", "dos frases con razón"],
        ["justificar con «me gusta»", "olvidar la información clave"],
        "Reconoce la razón más conectada con el usuario y pregunta qué cambiaría si el usuario fuera distinto.",
    ),
    "Mira un envase de tu casa y di en voz alta para qué sirve y quién lo usa.",
    "Rediseña el mismo afiche para un usuario distinto, como niños de 4 años, y anota qué decisiones cambiaste.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA1, 6,
    "Tu obra de la clase anterior o la que estés haciendo, un lápiz, una hoja para anotar y colores. Los comentarios de ejemplo están escritos aquí.",
    "Aprenderé a revisar mi obra con ayuda de comentarios, decidiendo qué cambio y qué conservo, para mejorar sin perder mi idea. Sirve para que mi trabajo siga siendo mío aunque otras personas me den consejos.",
    ["Sé escribir una intención y fundamentar con «elegí… porque…».", "Sé que un referente se mira para inspirarse, no para copiar."],
    [
        "Revisar es mirar de nuevo mi obra y decidir si se ve lo que quería comunicar. No es borrar todo. Para revisar, me hago tres preguntas: ¿mi intención se ve?, ¿qué decisión no ayuda?, ¿qué decisión sí funciona y debo conservar? Si la respuesta a la primera pregunta es «no», busco qué cambiar: color, tamaño, espacio, línea o material.",
        "Los comentarios de otras personas son información, no órdenes. Un buen comentario dice qué se ve y por qué. Por ejemplo: «El cielo gris tapa el sol, y tú querías mostrar alegría». Ese comentario ayuda porque se relaciona con la intención. Un comentario como «yo lo haría azul» pide que yo haga lo que a otra persona le gusta. Yo decido qué comentarios uso y cuáles no, siempre según mi intención.",
        "La autoría es que la idea y las decisiones sean mías. Si miro un referente, anoto qué idea tomé y qué cambié. Si una persona me ayuda, lo digo. Al final dejo escrito qué decisión cambié y por qué. Con eso mi obra es honesta y se entiende cómo la hice.",
    ],
    [("revisión", "mirar de nuevo mi obra y decidir qué cambiar y qué conservar"), ("autoría", "que la idea y las decisiones de la obra sean de quien la hizo"), ("comentario", "opinión sobre una obra que da información para mejorarla"), ("conservar", "dejar sin cambio lo que funciona"), ("referente", "obra que miro para inspirarme, sin copiarla")],
    [
        w("Usar un comentario", "Tu intención es mostrar alegría. Alguien comenta: «El cielo gris tapa el sol». ¿Qué cambias?", ["El comentario se relaciona con mi intención.", "Cambio el cielo gris por un celeste claro.", "Conservo el sol amarillo, que ya funciona."], "Cambio el cielo gris por celeste claro y conservo el sol"),
        w("No usar un comentario", "Tu intención es mostrar soledad con un árbol pequeño. Alguien dice: «Agrega muchos animales para que quede más lindo». ¿Qué haces?", ["Pienso en mi intención: soledad.", "Muchos animales quitarían la sensación de estar solo.", "Decido no usar ese comentario."], "No lo uso, porque contradice mi intención"),
    ],
    [
        m("Cambiar todo lo que dicen los demás sin pensar en mi intención.", "La obra deja de expresar mi idea.", "Pregunta si el cambio ayuda a mi intención."),
        m("No cambiar nada, porque «ya está terminado».", "Se pierde la oportunidad de que la obra comunique mejor.", "Revisa con las tres preguntas y cambia al menos una decisión."),
    ],
    [
        ex("¿Cuál es la primera pregunta de la revisión: «¿mi intención se ve?» o «¿quién lo hizo mejor?»?", "¿Mi intención se ve?", "La revisión parte de lo que quería comunicar."),
        ex("Si una decisión funciona bien en mi obra, ¿la cambio o la conservo?", "La conservo", "No hay que cambiar lo que ya ayuda a la intención."),
        ex("¿Qué es la autoría de una obra?", "Que la idea y las decisiones sean de quien la hizo", "Así la obra es de su autor."),
    ],
    [
        ex("Comentario: «El cielo gris tapa el sol, y querías mostrar alegría». ¿El comentario se relaciona con la intención?", "Sí", "Habla de un detalle que va en contra de la alegría."),
        ex("Comentario: «Yo lo haría azul porque es mi color favorito». ¿Ese comentario da información sobre la intención del autor?", "No", "Dice un gusto personal y no explica nada de la obra."),
        ex("Tomaste del referente la idea de repetir figuras geométricas, pero cambiaste los colores y las figuras. ¿Qué anotas: «lo que tomé y lo que cambié» o «copié todo»?", "Lo que tomé y lo que cambié", "Así la autoría queda clara."),
    ],
    [
        ex("Tu intención es mostrar calma con colores claros. Un compañero comenta: «Los rayos rojos arriba hacen que parezca peligro». ¿Qué decisión conviene cambiar: los rayos rojos o los colores claros?", "Los rayos rojos", "Los rayos rojos contradicen la calma."),
        ex("Ordena la revisión: A) cambiar una decisión, B) preguntarte si tu intención se ve, C) anotar qué cambiaste y por qué. Escribe las letras en orden.", "B, A, C", "Primero evalúas, luego cambias y al final lo anotas."),
        ex("Una niña revisó su obra y decidió no usar un comentario que le pedía agregar más gente a un paisaje solitario. ¿Perdió su autoría o la cuidó?", "La cuidó", "Mantuvo la idea de soledad."),
    ],
    [
        ex("Ema y Luis recibieron el mismo comentario: «Hay poco contraste entre el fondo y el volcán». Ema cambió el fondo a un color claro; Luis cambió todo el tema por un barco. ¿Cuál de los dos conservó mejor su intención?", "Ema", "Cambió solo una decisión para mejorar el contraste sin perder la idea."),
        ex("Un compañero usó una imagen de un afiche conocido y la copió casi igual, diciendo que es suya. ¿Es honesto?", "No", "Dice que es suya una obra copiada."),
    ],
    [
        ex("Revisas una obra con intención de alegría. Sol amarillo: funciona. Cielo gris oscuro: no ayuda. Personas sonriendo: funciona. ¿Cuántas decisiones debes conservar?", "2", "Se conservan el sol amarillo y las personas sonriendo; el cielo se cambia."),
        ex("Tu obra muestra el mar tranquilo. Un comentario pide agregar olas muy grandes. Tú decides agregar solo olas pequeñas y suaves. ¿Qué hiciste con el comentario: lo adaptaste a tu intención o lo ignoraste por completo?", "Lo adaptaste a tu intención", "Tomaste la idea de agregar olas, pero la cambiaste para que combine con tu idea de calma."),
    ],
    ex("En una exposición, alguien te pregunta qué cambiaste durante el trabajo. ¿Qué respuesta es más clara: «cambié el cielo de gris a celeste porque quería alegría» o «cambié cosas»?", "Cambié el cielo de gris a celeste porque quería alegría", "Dice la decisión y la razón."),
    [
        ex("Verdadero o falso: revisar significa borrar todo y empezar de cero.", "Falso", "Es mirar de nuevo y cambiar lo que no ayuda."),
        ex("¿Qué se anota al final de la revisión?", "Qué decisión cambié y por qué", "Así se entiende cómo se hizo la obra."),
        ex("Verdadero o falso: un comentario es información que yo decido usar o no según mi intención.", "Verdadero", "El autor decide qué usar."),
    ],
    task(
        "Elige UNA obra para revisar: A) la que hiciste en una de las clases anteriores; B) esta escena: «Un dibujo de una playa con intención de calma; tiene un cielo con rayos rojos y una gaviota gigante». Responde: ¿tu intención se ve?, ¿qué decisión cambias?, ¿qué decisión conservas? Haz el cambio y escribe una frase: «Cambié… porque…».",
        "Elegí la B. Mi intención es calma. Los rayos rojos no ayudan; los cambio por nubes suaves celestes. Conservo la gaviota, pero la hago pequeña. Cambié los rayos rojos porque contradecían la calma de la playa.",
        ["responde las tres preguntas de revisión", "cambia una decisión con una razón", "conserva algo que funciona", "mantiene la intención propia"],
        ["obra revisada", "tres respuestas", "frase «Cambié… porque…»"],
        ["cambiar todo", "no cambiar nada"],
        "Destaca una decisión conservada y una cambiada con razón, y pregunta qué comentario ayudó más.",
    ),
    "Muestra tu obra a una persona de tu casa y pídele que diga una cosa que se vea y una duda. Anota si te sirve.",
    "Escribe dos comentarios sobre tu propia obra: uno que mantendrías y otro que descartarías, y di por qué.",
)

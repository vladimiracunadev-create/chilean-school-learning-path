"""Cuaderno del estudiante de 1.º medio Artes Visuales: AR1M OA 03 (imaginarios personales en libro de artista y arte digital)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR1M OA 03"


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
    OA3, 1,
    "Hojas, lápiz de mina, lápices de colores y papel cuadriculado. Las dos obras de ejemplo (un libro acordeón y una imagen de píxeles) están descritas en esta clase; no necesitas buscar nada ni usar un computador.",
    "Aprenderé a observar libros de artista y obras de arte digital y a ver cómo el formato ayuda a decir algo. Sirve para elegir el medio más adecuado para mi imaginario personal.",
    ["Sé que mi imaginario personal es un conjunto de imágenes y símbolos propios.", "Sé separar lo que se ve de lo que opino."],
    [
        "Un libro de artista es una obra en la que la forma del libro es parte de lo que dice: el número de páginas, cómo se pliega, el material y el orden en que se pasa. Un formato muy usado es el acordeón, una tira de papel plegada en zigzag; cada parte entre pliegues se llama panel. El arte digital es el que se crea o se muestra con medios digitales. Su unidad más pequeña es el píxel, un cuadradito de un solo color. Una imagen digital es una cuadrícula de píxeles.",
        "Cada formato tiene efectos propios. Un acordeón se recorre en secuencia: al pasar de un panel al siguiente se percibe tiempo o movimiento. Una imagen digital se ve en pantalla, se puede copiar sin perder calidad y permite probar versiones. Un libro se toca y se guarda; una imagen digital se comparte. Por eso, antes de crear, me pregunto: ¿qué quiero decir, a quién y cómo lo verá?",
        "Al observar anoto tres cosas: contexto (dónde y cómo se ve), lenguaje visual (formas, colores, orden) y propósito (para qué). Separo datos, como «tiene seis paneles», de inferencias, como «la autora extraña su casa». Y cuido mi privacidad: en un imaginario personal uso símbolos y no muestro direcciones, números de casa, rostros de otras personas ni datos que permitan ubicarme.",
    ],
    [("libro de artista", "obra en la que la forma del libro es parte de su sentido"), ("acordeón", "formato de tira de papel plegada en zigzag"), ("panel", "cada parte de una tira que queda entre dos pliegues"), ("píxel", "cuadradito de un solo color que forma una imagen digital"), ("arte digital", "arte creado o mostrado con medios digitales")],
    [
        w("Leer dos obras", "Obra 1 de ejemplo: tira de 60 cm plegada en acordeón con 6 paneles; en cada panel una ventana dibujada que se abre un poco más; sin texto; propósito: mostrar el paso de la noche a la mañana. Obra 2 de ejemplo: imagen de 16 por 16 píxeles, 4 colores, un cerro que cambia de color en 3 versiones; propósito: mostrar el cerro en tres horas del día. ¿Qué tiene en común su propósito?", ["La obra 1 muestra una secuencia en el tiempo.", "La obra 2 muestra el cerro en tres momentos.", "Ambas muestran un cambio con el paso del tiempo."], "Ambas muestran un cambio a lo largo del tiempo"),
        w("Dato o inferencia", "De la obra 1, un compañero escribe: «La autora vive cerca de un cerro». ¿Es un dato?", ["La ficha habla de ventanas y de la noche a la mañana.", "No menciona ningún cerro ni dónde vive la autora."], "No, es una inferencia sin respaldo en la ficha"),
    ],
    [
        m("Pensar que el libro de artista es cualquier cuaderno con dibujos.", "En un libro de artista la forma del libro forma parte del mensaje.", "Pregunta qué dice el formato: cuántas páginas, cómo se pliega y en qué orden."),
        m("Mostrar en un trabajo personal la dirección de la casa o el rostro de otra persona.", "Pone en riesgo la privacidad propia y ajena.", "Representa el lugar con símbolos y no incluyas datos que permitan ubicar a nadie."),
    ],
    [
        ex("¿Qué es un libro de artista? A. Una obra en la que la forma del libro es parte de su sentido B. Un libro de pintura que se compra en una tienda.", "A", "La forma del libro es parte de lo que dice la obra; no es un libro comprado."),
        ex("En un formato acordeón, ¿cómo se llama cada parte entre dos pliegues?", "Panel", "Los paneles forman la tira en zigzag."),
        ex("En arte digital, ¿qué es un píxel?", "El cuadradito de un solo color que forma la imagen", "La imagen digital es una cuadrícula de píxeles."),
    ],
    [
        ex("Un acordeón de 5 paneles muestra una flor que se abre un poco más en cada uno. ¿Qué efecto produce pasar de un panel al siguiente? A. Sensación de paso del tiempo o de movimiento B. Sensación de que todo ocurre al mismo tiempo.", "A", "La secuencia ordenada se percibe como cambio en el tiempo."),
        ex("La obra digital de ejemplo usa 4 colores. ¿Eso es un dato de lenguaje visual o de contexto?", "De lenguaje visual", "Los colores forman parte de cómo se ve la imagen."),
        ex("Ficha: «Imagen digital de un cerro en tres versiones». ¿Cuál es una inferencia? A. La autora ve ese cerro cada mañana B. Hay tres versiones.", "A", "La ficha no dice qué hace la autora cada mañana; el número de versiones sí está dicho."),
    ],
    [
        arith("Otra imagen digital de ejemplo mide 20 píxeles de ancho por 20 de alto. ¿Cuántos píxeles tiene en total?", "20 * 20", "El total de una cuadrícula es ancho por alto.", " píxeles"),
        arith("Una tira de 84 cm se pliega en paneles de 12 cm. ¿Cuántos paneles tiene?", "84 // 12", "Se divide el largo de la tira entre el largo de cada panel.", " paneles"),
        ex("Un libro se toca y se guarda; una imagen digital se comparte con facilidad. Quieres que una persona que vive en otra ciudad vea tu obra esta semana. ¿Qué formato facilita eso? A. Una imagen digital B. Un libro único.", "A", "Una imagen digital se envía sin viajar; el libro único exige llevarlo."),
    ],
    [
        ex("Tienes una sola hoja y ningún computador. Quieres mostrar una secuencia de seis momentos. ¿Qué formato eliges? A. Un acordeón de seis paneles B. Una imagen digital de tres versiones.", "A", "El acordeón se hace con papel y permite seis momentos; sin computador no puedes hacer la digital."),
        ex("Tu imaginario incluye la fachada de tu casa con el número visible. ¿Qué haces al mostrar tu obra? A. La dibujo sin el número ni el nombre de la calle B. La muestro completa para que se reconozca.", "A", "Quitar los datos que ubican protege tu privacidad sin perder la imagen."),
    ],
    [
        arith("Dibujaste 4 versiones de una imagen de 12 por 12 píxeles. ¿Cuántos píxeles dibujaste en total?", "4 * 12 * 12", "Cada versión tiene 144 píxeles y son cuatro.", " píxeles"),
        ex("Dos obras con el mismo imaginario: un acordeón de 6 paneles y una imagen digital de 3 versiones. Quieres mostrar un proceso de 6 etapas distintas. ¿Cuál lo muestra mejor?", "El acordeón de 6 paneles", "Tiene un panel por etapa; las 3 versiones no alcanzan para 6."),
    ],
    ex("Tu liceo organiza una muestra de libros de artista y de imágenes digitales. Quieres expresar «las horas de mi barrio» con una secuencia de seis momentos y que cada visitante pueda recorrerla con la mano. ¿Qué eliges? A. Un acordeón de seis paneles B. Una sola imagen digital pequeña.", "A", "El acordeón se recorre con la mano y tiene un panel por momento."),
    [
        ex("¿Qué dice un libro de artista con su forma, además de con sus imágenes?", "Dice algo con el número de páginas, el plegado, el material y el orden", "La forma es parte del sentido."),
        ex("Verdadero o falso: en un trabajo personal puedo incluir el número de mi casa para que se reconozca el lugar.", "Falso", "Un dato así permite ubicarte; se reemplaza por un símbolo."),
        ex("¿De qué está hecha una imagen digital?", "De una cuadrícula de píxeles", "Cada píxel es un cuadradito de un solo color."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Acordeón de 60 cm con 6 paneles, una ventana que se abre un poco más en cada uno, sin texto. B) Imagen de 16 por 16 píxeles y 4 colores, un cerro en 3 versiones. C) Cuaderno de 12 páginas, hojas dobladas unidas con cordel, con una escalera dibujada en cada página, cada vez más arriba. Anota contexto, lenguaje visual y propósito, marca una inferencia tuya con una pregunta para investigarla y haz un boceto pequeño de cómo la usarías para un imaginario propio, sin datos personales.",
        "Elegí la A. Contexto: es una tira que se recorre con la mano. Lenguaje visual: seis paneles y una ventana que se abre. Propósito: mostrar la noche que pasa a mañana. Inferencia: tal vez la autora mira por esa ventana cada día; pregunta: ¿qué hora representa cada panel? Boceto: seis paneles de mi patio con una planta que crece.",
        ["anota contexto, lenguaje visual y propósito", "marca una inferencia distinta de los datos", "hace un boceto propio sin datos personales", "formula una pregunta para investigar"],
        ["ficha de observación", "boceto pequeño"],
        ["tratar una inferencia como dato", "incluir datos personales"],
        "Pregunta qué parte de su ficha es un dato y cuál es una inferencia suya.",
    ),
    "Pliega una hoja en zigzag en tres paneles y cuenta en voz alta qué dibujarías en cada uno para mostrar un cambio.",
    "Explica en tres frases por qué una obra puede cambiar de sentido si pasa de libro a imagen digital.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Hojas, regla, lápiz de mina, tijeras de punta redonda, cinta de papel y papel cuadriculado. Los formatos y las herramientas digitales de ejemplo están descritos en esta clase; todo se puede hacer en papel y sin cuentas ni internet.",
    "Aprenderé a explorar formatos de libro (plegados, uniones, papel) y herramientas de arte digital (píxeles, capas, paleta) y a elegir según lo que quiero expresar. Sirve para diseñar mi obra con conocimiento.",
    ["Sé qué es un libro de artista y qué es un píxel.", "Sé que debo cuidar mi privacidad al mostrar mi imaginario."],
    [
        "Un libro de artista se explora con el papel. Doblar una hoja por la mitad muchas veces la divide en partes iguales: una vez da 2, dos veces da 4 y tres veces da 8. Las uniones se eligen según la intención: la cinta de papel o un cordel que pasa por agujeros de perforadora de oficina permiten abrir y reordenar páginas; un pegamento fijo no. El papel también comunica: uno delgado se ve liviano y translúcido; uno grueso, firme.",
        "En arte digital exploro con herramientas simuladas en papel: la cuadrícula de píxeles, la paleta (el conjunto de colores que decido usar) y las capas, que son hojas transparentes superpuestas donde cada una guarda una parte de la imagen. Con capas puedo cambiar el fondo sin tocar el personaje. La resolución es la cantidad de píxeles de la imagen: 8 por 8 es muy baja y 32 por 32 permite más detalle. Una paleta corta de 3 o 4 colores da un estilo claro.",
        "Cuando uso imágenes que no son mías necesito autorización y debo anotar el crédito. Un banco de imágenes propias o autorizadas está formado por mis dibujos, por fotos que tomé sin personas reconocibles y por imágenes cuyo autor me dio permiso. Antes de compartir un archivo, reviso que no muestre rostros ni lugares que permitan ubicar a alguien. Guardo siempre mi trabajo en una versión original y trabajo en una copia.",
    ],
    [("paleta", "conjunto de colores que se decide usar en una obra"), ("capa", "hoja transparente superpuesta que guarda una parte de la imagen digital"), ("resolución", "cantidad de píxeles de una imagen"), ("unión reversible", "forma de unir que se puede deshacer sin dañar las piezas"), ("autorización", "permiso de la persona autora para usar su imagen")],
    [
        w("Elegir una unión", "Quieres un libro de 8 páginas cuyas hojas puedas reordenar después de probar la secuencia. ¿Cinta de papel o pegamento fijo?", ["Necesito poder cambiar el orden.", "La cinta de papel se despega sin dañar las hojas.", "El pegamento fijo no deja reordenar."], "Cinta de papel, porque es reversible"),
        w("Elegir la resolución", "Quieres dibujar un ojo con párpados y pestañas en una imagen digital. ¿Sirve una cuadrícula de 8 por 8 o una de 32 por 32?", ["Un ojo con párpados y pestañas necesita detalles pequeños.", "8 por 8 tiene muy pocos píxeles.", "32 por 32 permite más detalle."], "La de 32 por 32"),
    ],
    [
        m("Usar una imagen de internet en la obra sin saber si tengo autorización.", "Se usa el trabajo de otra persona sin su permiso ni crédito.", "Usa imágenes propias o con autorización, y anota el crédito."),
        m("Trabajar directamente sobre el único archivo original.", "Si algo sale mal, no hay forma de volver atrás.", "Guarda el original y trabaja en una copia."),
    ],
    [
        ex("¿Qué es una capa en arte digital? A. Una hoja transparente superpuesta que guarda una parte de la imagen B. Un tipo de papel grueso.", "A", "Las capas permiten cambiar una parte sin tocar el resto."),
        ex("Quieres dividir una hoja en 8 partes iguales doblándola siempre por la mitad. ¿Cuántas veces la doblas?", "3", "Cada doblez duplica las partes: 2, 4 y 8."),
        ex("¿Qué es la paleta de una obra?", "El conjunto de colores que se decide usar", "Limitar la paleta da un estilo claro."),
    ],
    [
        ex("Quieres cambiar el color del fondo de tu imagen digital sin tocar el personaje. ¿Qué te sirve? A. Dibujar fondo y personaje en capas distintas B. Dibujar todo en una sola capa.", "A", "Con capas separadas, el fondo se modifica sin afectar al personaje."),
        ex("¿Qué unión permite reordenar las páginas de un libro de artista? A. Cinta de papel B. Pegamento fuerte.", "A", "La cinta se despega sin dañar; el pegamento fuerte no."),
        ex("Revisas cuatro fuentes: tus dibujos, una foto que tomaste de un árbol, una imagen cuyo autor te dio permiso y una imagen bajada de internet sin saber de quién es. ¿Cuántas son aceptables?", "3", "Las tres primeras son propias o autorizadas; la última no tiene autor ni permiso conocidos."),
    ],
    [
        arith("Una hoja se dobla por la mitad 4 veces. ¿Cuántos paneles iguales se forman?", "2 * 2 * 2 * 2", "Cada doblez multiplica por 2 las partes.", " paneles"),
        arith("Una paleta de ejemplo tiene 4 colores y la imagen es de 8 por 8 píxeles. ¿Cuántos píxeles hay que pintar?", "8 * 8", "El total es ancho por alto.", " píxeles"),
        ex("Quieres dibujar una calle con casas, ventanas y un letrero. ¿Qué resolución sirve más? A. 32 por 32 píxeles B. 4 por 4 píxeles.", "A", "A más píxeles, más detalle posible."),
    ],
    [
        ex("Un compañero guarda su única versión del archivo y la modifica directamente. En un cambio borra la cara del personaje sin querer. ¿Qué debió hacer antes?", "Guardar una copia del original", "Con una copia puede volver atrás."),
        ex("Un libro con papel delgado y translúcido y otro con papel grueso. Quieres expresar fragilidad. ¿Cuál eliges y por qué?", "El papel delgado, porque se ve liviano y translúcido", "La materialidad del papel comunica fragilidad."),
    ],
    [
        arith("Tu libro de ejemplo tiene 16 páginas y cada hoja doblada por la mitad aporta 4 páginas (dos por cada lado). ¿Cuántas hojas necesitas?", "16 // 4", "Se divide el total de páginas entre las que aporta cada hoja.", " hojas"),
        ex("Quieres usar la foto de un amigo en tu obra digital porque se ve muy bien. ¿Qué haces primero? A. Pedirle autorización a él y anotar el crédito B. Usarla y avisarle después.", "A", "El permiso se pide antes de usar su imagen."),
    ],
    ex("Para una muestra del liceo debes explorar en papel una obra con tres cambios de color en el cielo. Tienes una cuadrícula de 8 por 8 y otra de 24 por 24. Quieres incluir nubes con forma y un horizonte. ¿Cuál usas? A. La de 24 por 24 B. La de 8 por 8.", "A", "Las nubes con forma y un horizonte necesitan más píxeles; 8 por 8 es muy baja."),
    [
        ex("¿Para qué sirven las capas en arte digital?", "Para separar partes de la imagen y cambiar una sin tocar las otras", "Cada capa guarda una parte."),
        ex("Verdadero o falso: la resolución es la cantidad de colores de la paleta.", "Falso", "Es la cantidad de píxeles de la imagen."),
        ex("Antes de compartir un archivo, ¿qué debes revisar?", "Que no muestre rostros ni lugares que permitan ubicar a alguien", "Es una medida de privacidad."),
    ],
    task(
        "Elige UNA exploración. A) Dobla una hoja por la mitad tres veces, ábrela y usa las 8 partes para dibujar una secuencia de un cambio, con dos tipos de unión (cinta y clip) para probar cuál permite reordenar mejor. B) En papel cuadriculado dibuja un mismo motivo en una cuadrícula de 8 por 8 y en otra de 24 por 24 con una paleta de 4 colores y compara el detalle. C) Dibuja un fondo y un personaje en dos hojas transparentes (papel de horno limpio o calco) y prueba cambiar el fondo sin tocar el personaje. Registra qué descubriste y qué usarías para tu imaginario personal. Usa solo imágenes propias.",
        "Elegí la B. Dibujé una luna en 8 por 8 y en 24 por 24. En la pequeña solo se ve un círculo; en la grande se ven los cráteres. Para mi imaginario nocturno usaré 24 por 24 con 4 colores. Todas mis imágenes son dibujos propios.",
        ["realiza la exploración con materiales sencillos", "compara dos opciones", "registra lo que descubrió", "usa solo imágenes propias"],
        ["exploración en papel", "registro de comparación"],
        ["usar imágenes ajenas sin permiso", "no guardar el original"],
        "Pregunta qué descubrió al comparar las dos opciones y cuál elegiría para su obra.",
    ),
    "Dobla una hoja por la mitad dos veces y cuenta cuántas partes iguales quedan.",
    "Compara con tres frases dos tipos de papel de tu casa y di qué sentido darían a un libro.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Hojas, lápiz de mina, lápices de colores y papel cuadriculado. El guion de seis cuadros y los datos de las pruebas están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a probar decisiones de secuencia, ritmo, color y composición con un storyboard de seis cuadros y a elegir una versión con un criterio. Sirve para ordenar una historia visual antes de hacerla.",
    ["Sé que el formato comunica y que la paleta y la resolución cambian el detalle.", "Sé que debo trabajar con imágenes propias o autorizadas."],
    [
        "Un storyboard es una serie de cuadros dibujados en orden que muestran una secuencia. Con seis cuadros puedo ver el comienzo, el desarrollo y el final de una idea. La secuencia es el orden de los cuadros; si la cambio, cambia el sentido. El ritmo es cuánto tiempo o espacio ocupa cada momento: seis cuadros iguales dan un ritmo parejo; uno más grande hace una pausa. El encuadre es lo que decido mostrar dentro del cuadro: un detalle cerca o todo el paisaje lejos.",
        "Probar significa hacer dos versiones y compararlas con un criterio. Mi criterio puede ser claridad: si alguien entiende la secuencia sin explicación. O impacto: qué cuadro llama más la atención. Cambio una sola cosa por prueba, como el orden o el encuadre, para saber qué produjo el efecto. Anoto qué conservo y qué cambio. También puedo pedir a una persona que no conoce mi idea que cuente qué entiende; su lectura me muestra si la secuencia se entiende.",
        "En el libro de artista pruebo un acordeón que funciona como un storyboard con paneles: el orden es el de lectura y los pliegues marcan las pausas. En arte digital pruebo la paleta: con solo tres colores la imagen suele verse más clara que con diez. Mi imaginario se mantiene privado: uso símbolos y no muestro direcciones ni rostros ajenos. Si uso una imagen de otra persona, tengo su autorización por escrito y anoto el crédito.",
    ],
    [("storyboard", "serie de cuadros dibujados en orden que muestran una secuencia"), ("secuencia", "orden en que se presentan los momentos de una obra"), ("ritmo", "cuánto tiempo o espacio ocupa cada momento de una secuencia"), ("encuadre", "lo que se decide mostrar dentro de un cuadro"), ("criterio", "regla que se usa para comparar y decidir")],
    [
        w("Cambiar la secuencia", "Storyboard de ejemplo con seis cuadros de un cerro: 1 amanecer, 2 mediodía, 3 tarde, 4 atardecer, 5 noche, 6 madrugada. Si cambias el cuadro 6 por el lugar 1, ¿cómo cambia el sentido?", ["Con el orden original, la secuencia parte con el amanecer.", "Con la madrugada primero, la secuencia parte en la oscuridad.", "Cambia el punto de partida y por eso cambia el sentido."], "El sentido cambia: la secuencia ya no parte del amanecer sino de la oscuridad"),
        w("Probar con un criterio", "Dos versiones del mismo cuadro: V1 muestra todo el cerro lejos, con un punto pequeño que es la persona; V2 muestra solo la persona y un trozo de cerro. Criterio: claridad de quién es el centro. ¿Cuál conviene?", ["Criterio: se debe entender quién es el centro.", "En V2 la persona es lo principal.", "En V1 es un punto casi invisible."], "V2, porque deja claro que la persona es el centro"),
    ],
    [
        m("Cambiar muchas cosas a la vez en una prueba.", "No se sabe qué cambio produjo el efecto.", "Cambia una sola cosa por prueba y anota el resultado."),
        m("Elegir la versión por gusto sin criterio.", "No se puede justificar ni mejorar.", "Escribe un criterio, como claridad o impacto, antes de comparar."),
    ],
    [
        ex("¿Qué es un storyboard? A. Una serie de cuadros dibujados en orden B. Un solo dibujo grande.", "A", "El storyboard muestra una secuencia de cuadros."),
        ex("Si cambias el orden de los cuadros de una secuencia, ¿qué cambia?", "El sentido", "El orden de los cuadros decide cómo se lee la historia."),
        ex("En un cuadro quieres mostrar un detalle de una mano de cerca. ¿Qué decisión tomas? A. De encuadre B. De paleta.", "A", "El encuadre es lo que se muestra dentro del cuadro."),
    ],
    [
        arith("Un storyboard tiene 6 cuadros y cada cuadro se mira 5 segundos en una presentación. ¿Cuántos segundos dura?", "6 * 5", "Se multiplica el número de cuadros por la duración de cada uno.", " segundos"),
        ex("Quieres hacer una pausa dramática antes del último cuadro. ¿Qué recurso de ritmo usas? A. Hacerlo más grande o dejarlo con más espacio B. Hacerlo igual a todos.", "A", "Un cuadro con más espacio se lee como una pausa."),
        ex("Para probar bien dos versiones del mismo cuadro, ¿cuántas cosas debes cambiar entre una y otra? A. Una B. Todas las que pueda.", "A", "Si cambias una sola, sabes qué produjo la diferencia."),
    ],
    [
        ex("Probaste tres versiones de una secuencia de seis cuadros con cinco personas que no conocen tu idea; cada persona vio una sola versión. Entendieron el orden: 1 persona con la P1 (diez colores), 3 con la P2 (tres colores) y 1 con la P3 (cinco colores). Tu criterio es claridad. ¿Cuál eliges?", "La P2", "Fue la que más personas entendieron, y ese es el criterio elegido."),
        arith("Un acordeón de ejemplo tiene 8 paneles y cada panel mide 12 cm. ¿Cuántos centímetros mide la tira abierta?", "8 * 12", "El largo total es el número de paneles por el largo de cada panel.", " cm"),
        ex("Una persona mira tu storyboard y dice que entiende el orden de los cuadros 1 al 4, pero no el 5 y el 6. ¿Qué haces? A. Reviso el encuadre y el orden de los cuadros 5 y 6 B. Cambio los cuadros 1 al 4.", "A", "El problema está en los cuadros que no se entienden."),
    ],
    [
        ex("Una compañera dice: «Mi secuencia es mejor porque tiene más color». ¿Qué le falta a su argumento?", "Un criterio, como claridad o impacto, y una prueba", "Más color no es un criterio por sí solo."),
        ex("En un acordeón de seis paneles, los pliegues entre paneles marcan... A. Las pausas entre momentos B. El tamaño de la hoja.", "A", "Cada pliegue separa un momento del siguiente."),
    ],
    [
        arith("Para tu storyboard recortas hojas de 21 cm de ancho en cuadros de 7 cm de ancho. ¿Cuántos cuadros salen de cada hoja en una fila?", "21 // 7", "Se divide el ancho de la hoja entre el ancho de cada cuadro.", " cuadros"),
        ex("Tu primera versión muestra la persona de frente con su cara. Tu libro será exhibido a todo el curso y quieres proteger tu privacidad. ¿Qué cambias? A. Dibujar la persona de espaldas o como silueta B. Escribir su nombre al lado.", "A", "La silueta protege la identidad; escribir el nombre la revela."),
    ],
    ex("Para la muestra de tu liceo debes presentar una secuencia de seis cuadros: sembrar, brotar, crecer, florecer, dar frutos, volver a sembrar. Pruebas dos versiones: la V1 con los seis cuadros del mismo tamaño y la V2 con el cuadro de florecer el doble de ancho. Tu criterio es destacar el momento de florecer. ¿Cuál eliges? A. La V2 B. La V1.", "A", "El cuadro más ancho hace una pausa en ese momento."),
    [
        ex("¿Cuántas cosas conviene cambiar entre dos pruebas para entender el efecto?", "Una", "Así se sabe qué cambio produjo la diferencia."),
        ex("Verdadero o falso: si cambio el orden de los cuadros de una secuencia, el sentido puede cambiar.", "Verdadero", "El orden es parte de lo que dice la obra."),
        ex("¿Qué decides al elegir el encuadre?", "Lo que muestro dentro del cuadro", "Puede ser un detalle cercano o un paisaje lejano."),
    ],
    task(
        "Elige UNA secuencia de ejemplo. A) Una semilla que pasa por seis momentos: sembrar, brotar, crecer, florecer, dar frutos, volver a sembrar. B) Un cerro en seis horas del día, del amanecer a la noche. C) Una escalera que se sube en seis pasos hasta una ventana. Dibuja un storyboard de seis cuadros en una versión 1 y cambia UNA sola cosa (orden, encuadre o paleta) en una versión 2. Pide a una persona de tu casa que cuente qué entiende de cada una, compara con un criterio (claridad o impacto) y elige una. No uses rostros ni datos personales.",
        "Elegí la A. Versión 1: seis cuadros del mismo tamaño. Versión 2: el cuadro de florecer más grande. Criterio: impacto. La persona entendió ambas, pero dijo que la 2 le mostró lo más importante. Elijo la versión 2. Todos los dibujos son de plantas, sin personas.",
        ["dibuja seis cuadros en orden", "cambia una sola cosa entre versiones", "compara con un criterio nombrado", "elige y justifica con la lectura de otra persona"],
        ["dos storyboards de seis cuadros", "registro del criterio y la decisión"],
        ["cambiar muchas cosas a la vez", "decidir sin criterio"],
        "Pregunta qué cambió entre las versiones y qué criterio decidió la elección.",
    ),
    "Cuenta en voz alta los seis momentos de una secuencia que conozcas, en orden, y luego cambia dos de lugar para ver qué sentido tiene.",
    "Escribe qué recurso de ritmo usarías para destacar el último momento de una secuencia y por qué.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Hojas, regla, lápiz de mina, lápices de colores, papel cuadriculado, cinta de papel y tijeras de punta redonda. El encargo y los datos están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a desarrollar una propuesta propia de libro de artista o de arte digital basada en mi imaginario personal, con un plan de páginas o píxeles y una ficha de consentimiento, crédito y privacidad. Sirve para pasar de una idea a una obra que puedo mostrar con cuidado.",
    ["Sé armar un storyboard y probar una sola decisión por vez.", "Sé que las imágenes ajenas necesitan autorización y crédito."],
    [
        "Una propuesta de libro de artista o de arte digital responde cinco preguntas: qué imaginario expresa, qué formato usa, cuántas páginas, paneles o píxeles tiene, qué materiales o herramientas necesita y cómo cuida la privacidad. Con eso armo una maqueta o dummy, que es un modelo a tamaño real hecho con papel barato para probar el orden antes de la versión final.",
        "El cálculo ayuda a decidir. Un acordeón de 8 paneles de 10 cm mide 80 cm; si mi papel tiene 60 cm, necesito unir dos tiras o reducir los paneles. Una imagen de 24 por 24 píxeles tiene 576 píxeles. En un libro de hojas dobladas unidas con cordel, cada hoja doblada aporta 4 páginas. La portada es la cara que se ve primero y anuncia el tema. Todo cálculo se anota para que otra persona pueda repetir mi trabajo.",
        "La ficha de consentimiento, crédito y privacidad tiene cuatro líneas: qué imágenes son propias o autorizadas, a quién pedí permiso, cómo anoto el crédito y qué datos personales quité. Con la ficha puedo mostrar mi obra sin riesgo. Si la obra va a circular en pantalla, comparto solo la versión sin datos de ubicación y sin rostros. La propuesta es mía solo si las decisiones importantes tienen una razón mía.",
    ],
    [("dummy", "modelo a tamaño real de un libro, hecho con papel barato, para probar el orden"), ("portada", "cara de un libro que se ve primero y anuncia su tema"), ("privacidad", "derecho a que los datos personales no se muestren sin permiso"), ("consentimiento", "permiso de una persona para usar su imagen o su obra"), ("ficha de crédito", "registro de quién hizo o permitió cada imagen usada")],
    [
        w("Calcular el largo del acordeón", "Quieres un acordeón con 8 paneles de 10 cm cada uno. Tu papel es una tira de 60 cm. ¿Alcanza?", ["Largo necesario: 8 × 10 = 80 cm.", "El papel mide 60 cm.", "Faltan 80 − 60 = 20 cm."], "No alcanza: faltan 20 cm; hay que unir otra tira o hacer menos paneles"),
        w("Llenar la ficha", "Tu obra digital usa un dibujo propio de un cerro y una foto de un árbol que tomó un amigo. ¿Qué debe decir la ficha?", ["Imagen propia: el dibujo del cerro.", "Imagen ajena: la foto del amigo, con su permiso por escrito.", "Crédito: «Foto del árbol: nombre del amigo, con permiso»."], "Dibujo propio, foto del amigo con permiso y crédito anotado"),
    ],
    [
        m("Fabricar la versión final sin hacer un dummy.", "Los errores de orden o de tamaño se descubren cuando ya no tienen arreglo.", "Prueba primero con papel barato y ajusta."),
        m("Usar una foto de un familiar o amigo sin pedirle permiso porque «es solo para el curso».", "Se difunde su imagen sin su consentimiento.", "Pide permiso, anota el crédito o usa una silueta."),
    ],
    [
        ex("En un libro de artista, ¿qué es un dummy? A. Un modelo a tamaño real con papel barato para probar el orden B. La versión final con papel fino.", "A", "Sirve para probar antes de hacer la versión final."),
        ex("¿Qué líneas tiene la ficha de consentimiento, crédito y privacidad? A. Imágenes propias o autorizadas, permisos, crédito y datos quitados B. Solo el título de la obra.", "A", "La ficha registra cómo se cuidó a las personas y a los autores."),
        ex("La portada de un libro es la cara que se ve primero. ¿Qué hace? A. Anunciar el tema B. Guardar las páginas.", "A", "La portada presenta el tema al lector."),
    ],
    [
        arith("Un acordeón de ejemplo tiene 6 paneles de 12 cm cada uno. ¿Cuántos centímetros mide la tira abierta?", "6 * 12", "Largo total = paneles por largo de cada panel.", " cm"),
        arith("Una imagen digital de ejemplo mide 18 por 18 píxeles. ¿Cuántos píxeles tiene?", "18 * 18", "El total es ancho por alto.", " píxeles"),
        ex("Cada hoja doblada de un cuaderno de ejemplo aporta 4 páginas. Quieres 20 páginas. ¿Cuántas hojas necesitas? A. 5 B. 10.", "A", "20 ÷ 4 = 5 hojas."),
    ],
    [
        ex("Tu acordeón tendrá paneles de 12 cm y tu tira mide 75 cm. Si no unes tiras, ¿cuántos paneles completos caben?", "6", "75 ÷ 12 da 6 y sobran 3 cm, así que caben 6 paneles completos (72 cm)."),
        ex("Una obra digital usa un dibujo propio y la foto de una compañera. Tienes el permiso de la compañera por escrito. ¿Qué anotas en la ficha? A. Su permiso y su crédito B. Solo el título de la obra.", "A", "La ficha debe mostrar el permiso y dar crédito a la autora de la foto."),
        ex("Tu imaginario es la ventana de tu cuarto, que da a una calle con nombre. ¿Qué cambio protege tu privacidad? A. Dibujar solo la ventana y el cielo sin el nombre de la calle B. Poner la dirección completa en el título.", "A", "Quitar el nombre de la calle evita que se ubique tu casa."),
    ],
    [
        ex("Un compañero calcula que su libro de 24 páginas necesita 8 hojas dobladas, con 4 páginas por hoja. ¿Es correcto?", "No, necesita 6 hojas", "24 ÷ 4 = 6; con 8 hojas tendría 32 páginas."),
        ex("Una propuesta dice: «Mi libro es propio porque copié un libro de ejemplo y le puse mi nombre». ¿Qué le falta? A. Una decisión de imaginario y de formato que sea suya B. Un título más largo.", "A", "La autoría exige decisiones propias, no solo un nombre."),
    ],
    [
        arith("Tu acordeón tendrá 9 paneles de 10 cm, es decir, 90 cm en total. Tienes tiras de 45 cm. ¿Cuántas tiras necesitas?", "9 * 10 // 45", "Se divide el largo total entre el largo de cada tira.", " tiras"),
        ex("Si el acordeón de 9 paneles se hace con 2 tiras de 45 cm, ¿cuántas uniones entre tiras habrá?", "1", "Dos tiras se unen en un solo punto."),
    ],
    ex("Tu curso hará una muestra con libros de artista de 6 paneles. Cada panel debe medir 15 cm. Tienes tiras de 30 cm. ¿Cuántas tiras necesitas por libro? A. 3 B. 2.", "A", "El largo total es 6 × 15 = 90 cm y cada tira mide 30 cm, entonces necesitas 3."),
    [
        ex("¿Qué cinco cosas responde una propuesta de libro de artista o digital?", "Imaginario, formato, páginas o píxeles, materiales y privacidad", "Con eso la propuesta se puede realizar con cuidado."),
        ex("Verdadero o falso: puedo usar la foto de un amigo en mi obra si le aviso después.", "Falso", "El permiso se pide antes."),
        ex("¿Para qué sirve el dummy?", "Para probar el orden y el tamaño antes de la versión final", "Evita errores costosos."),
    ],
    task(
        "Elige UN encargo de ejemplo. A) Acordeón de 8 paneles de 10 cm sobre «un día en mi barrio», con papel en tiras de 40 cm. B) Libro de 24 páginas sobre «mi cerro en un año», con hojas dobladas unidas con cordel que aportan 4 páginas cada una. C) Imagen digital de 24 por 24 píxeles en 3 versiones sobre «un lugar que me calma», con 4 colores. Calcula lo que necesitas, haz un dummy en papel barato o una cuadrícula de prueba, completa la ficha de consentimiento, crédito y privacidad y anota qué cambiarías en una versión siguiente.",
        "Elegí el encargo A. Cálculo: 8 × 10 = 80 cm y las tiras son de 40 cm: necesito 2 tiras unidas con cinta de papel. Hice un dummy con hojas recicladas y ajusté el orden. Ficha: todas las imágenes son dibujos propios; no hay personas ni nombres de calles; no usé imágenes ajenas. En una versión siguiente probaría un panel más largo para el momento principal.",
        ["calcula medidas, páginas o píxeles", "hace un dummy o una cuadrícula de prueba", "completa la ficha de consentimiento, crédito y privacidad", "propone un cambio para la versión siguiente"],
        ["cálculos", "dummy o cuadrícula de prueba", "ficha completa"],
        ["no probar antes de la versión final", "usar datos personales"],
        "Pregunta cómo hizo cada cálculo y qué datos personales quitó de su obra.",
    ),
    "Cuenta a una persona de tu casa cuántas tiras de 30 cm necesitas para un acordeón de 5 paneles de 12 cm.",
    "Elige una imagen de tu imaginario y escribe tres datos personales que quitarías antes de mostrarla.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Hojas y lápiz. Las dos propuestas y la pauta están escritas en esta clase; no necesitas buscar nada.",
    "Aprenderé a contrastar propuestas de libro de artista y de arte digital con criterios y a revisar la mía. Sirve para decidir con argumentos y para mostrar mi trabajo con consentimiento, crédito y privacidad.",
    ["Sé calcular medidas de un libro o píxeles de una imagen.", "Sé completar una ficha de consentimiento, crédito y privacidad."],
    [
        "Para contrastar dos propuestas uso cuatro criterios. Coherencia: el formato sirve al imaginario. Claridad de la secuencia: se entiende el orden sin explicación. Calidad del oficio: el plegado, la impresión o el dibujo está cuidado. Cuidado de las personas: hay consentimiento, crédito y privacidad. Cada criterio recibe de 0 a 3 puntos y cada puntaje se justifica con un dato observable usando «dato, criterio, conclusión».",
        "Un criterio puede fallar aunque el total sea alto. Una obra con 3 puntos en coherencia, claridad y oficio (9 en total), pero con un 0 en cuidado de las personas porque muestra el rostro de alguien sin permiso, no se puede mostrar. Por eso reviso primero los criterios de cuidado y después los demás. También recojo la lectura de otra persona: pido que cuente qué entiende y qué parte le llama la atención, y comparo con mi intención.",
        "Revisar mi propia propuesta es parte del trabajo. Escribo la parte más fuerte, la más débil y un cambio concreto, por ejemplo «ensancho el panel final» o «cambio el encuadre del cuadro 5». Al exponer, pongo mi nombre o seudónimo según prefiera, doy el crédito de los referentes y de las imágenes autorizadas, y comparto solo versiones sin datos de ubicación.",
    ],
    [("contrastar", "comparar propuestas con los mismos criterios"), ("oficio", "cuidado y destreza en el uso de la técnica y los materiales"), ("seudónimo", "nombre inventado que una persona usa en lugar del suyo"), ("lectura de otra persona", "lo que alguien entiende de una obra sin explicación previa"), ("revisión", "análisis de la propia propuesta para decidir qué conservar y qué cambiar")],
    [
        w("Puntuar una propuesta", "Propuesta 1: acordeón de 6 paneles sobre la noche que pasa a la mañana; todas las imágenes son dibujos propios; el orden se entiende sin explicación; el plegado está parejo, pero un panel tiene el pegamento a la vista. Puntúa coherencia, claridad, oficio y cuidado de las personas.", ["Coherencia: el acordeón sirve al paso del tiempo, 3.", "Claridad: se entiende sin explicación, 3.", "Oficio: un panel tiene el pegamento a la vista, 2.", "Cuidado de las personas: dibujos propios, sin rostros, 3."], "Total 3 + 3 + 2 + 3 = 11 puntos"),
        w("Un cero que bloquea", "Propuesta 2: imagen digital con una foto de un compañero, que no sabe que la usaste; coherencia 3, claridad 3, oficio 3, cuidado de las personas 0. ¿Se puede mostrar?", ["El total es 3 + 3 + 3 + 0 = 9.", "Pero el 0 indica que no hay consentimiento.", "Hay que pedir permiso o cambiar la imagen antes de mostrarla."], "No hasta pedir permiso o reemplazar la foto, aunque el total sea 9"),
    ],
    [
        m("Mirar solo el total y no cada criterio.", "Un cero en cuidado de las personas es grave aunque el total sea alto.", "Revisa primero los criterios de cuidado y luego los demás."),
        m("Decir «la versión B es mejor porque me gusta más».", "No hay criterio ni dato que otra persona pueda comprobar.", "Usa «dato, criterio, conclusión»."),
    ],
    [
        ex("¿Cuál es el criterio que pregunta si se entiende el orden sin explicación? A. Claridad de la secuencia B. Oficio.", "A", "La claridad de la secuencia se refiere al orden entendible; el oficio, al cuidado técnico."),
        ex("Una obra usa la foto de un compañero sin su permiso. ¿Qué criterio falla?", "Cuidado de las personas", "Falta el consentimiento del compañero."),
        ex("En esta clase, ¿cuántos puntos máximos tiene cada criterio?", "3", "Cada criterio se puntúa de 0 a 3."),
    ],
    [
        arith("Una propuesta recibe coherencia 3, claridad 2, oficio 2 y cuidado de las personas 3. ¿Cuánto suma?", "3 + 2 + 2 + 3", "Se suman los cuatro puntajes.", " puntos"),
        ex("Un acordeón tiene un panel con pegamento a la vista. ¿Qué criterio afecta? A. Oficio B. Coherencia.", "A", "El pegamento a la vista es un asunto de cuidado técnico."),
        ex("Una persona que no conoce tu idea mira tu storyboard y dice que entendió «un día pasando». Tu intención era «un día pasando». ¿Qué indica eso de la claridad?", "Que la secuencia se entiende", "La lectura de otra persona coincide con tu intención."),
    ],
    [
        ex("Propuesta 1: coherencia 3, claridad 2, oficio 2, cuidado 3. Propuesta 2: coherencia 2, claridad 3, oficio 3, cuidado 0, porque muestra el rostro de un compañero sin su permiso. ¿Cuántos puntos suma cada una y cuál se debe corregir antes de mostrarse?", "La 1 suma 10 y la 2 suma 8; se debe corregir la 2", "La 1 suma 3 + 2 + 2 + 3 = 10 y la 2 suma 2 + 3 + 3 + 0 = 8; el 0 de la 2 exige corregir."),
        ex("Una compañera cree que «con 12 puntos ya no hay nada que revisar». ¿Qué le responderías? A. Que un solo cero en cuidado de las personas basta para no mostrar la obra B. Que ya terminó.", "A", "Si falta consentimiento, el total alto no importa."),
        ex("Quieres cambiar tu propuesta después de la revisión. ¿Cuál es un cambio concreto? A. Ensancho el panel final B. Mejorar la obra.", "A", "Un cambio concreto dice qué se modifica; «mejorar» no."),
    ],
    [
        ex("Vas a exponer tu libro con un dibujo de tu cerro que se parece al de otro estudiante porque tomaste su idea del encuadre. ¿Qué debes poner? A. El crédito del recurso que tomaste B. Nada, porque la obra es tuya.", "A", "Declarar el recurso reconoce su autoría."),
        ex("Para compartir tu imagen digital con el curso, ¿qué versión mandas? A. Una sin datos de ubicación y sin rostros B. La original con todos los datos del archivo.", "A", "La versión sin datos protege tu privacidad y la de otros."),
    ],
    [
        ex("La propuesta X recibe coherencia 3, claridad 3, oficio 3 y cuidado de las personas 1, porque falta anotar un crédito. ¿Cuántos puntos suma y qué debe hacer antes de exponerse?", "Suma 10; debe anotar el crédito que falta", "3 + 3 + 3 + 1 = 10, y el 1 en cuidado de las personas indica que falta el crédito."),
        arith("Un grupo expone 5 acordeones de 6 paneles de 10 cm cada uno, uno junto al otro con 20 cm de espacio entre ellos (4 espacios). ¿Cuánto mide la fila completa en centímetros?", "5 * 6 * 10 + 4 * 20", "Cada acordeón mide 60 cm; son 300 cm más los 80 cm de los espacios.", " cm"),
    ],
    ex("Tu curso debe elegir entre dos propuestas para una muestra. La del grupo A: coherencia 3, claridad 2, oficio 3, cuidado 3. La del grupo B: coherencia 3, claridad 3, oficio 2, cuidado 3. ¿Cuántos puntos tiene cada una?", "A suma 11 y B suma 11", "A suma 3 + 2 + 3 + 3 = 11 y B suma 3 + 3 + 2 + 3 = 11."),
    [
        ex("¿Qué cuatro criterios se usan para contrastar propuestas en esta clase?", "Coherencia, claridad de la secuencia, oficio y cuidado de las personas", "Cubren la idea, la lectura, la técnica y el respeto."),
        ex("Verdadero o falso: un total alto permite mostrar una obra aunque falte consentimiento.", "Falso", "Un cero en cuidado de las personas exige corregir antes de mostrar."),
        ex("¿Qué se pide a otra persona que lea tu obra?", "Que cuente qué entiende y qué le llama la atención", "Así comparas su lectura con tu intención."),
    ],
    task(
        "Compara estas propuestas de ejemplo. Propuesta 1: acordeón de 6 paneles sobre una semilla, dibujos propios, orden claro, plegado parejo. Propuesta 2: imagen digital de 24 por 24 píxeles con una foto de un amigo que no sabe que se usó, buena paleta y buena claridad. Puntúa de 0 a 3 coherencia, claridad, oficio y cuidado de las personas para cada una, con «dato, criterio, conclusión». Decide cuál se puede mostrar hoy, qué cambio concreto necesita la otra y cómo anotarías crédito, consentimiento y privacidad al exponerlas.",
        "Propuesta 1: coherencia 3, claridad 3, oficio 3, cuidado 3: total 12. Propuesta 2: coherencia 3, claridad 3, oficio 3, cuidado 0: total 9. Se puede mostrar hoy la 1. La 2 necesita pedir permiso al amigo o cambiar la foto por un dibujo. Al exponer anotaría: «dibujos propios; foto con permiso de [nombre del amigo]; sin datos de ubicación».",
        ["puntúa los cuatro criterios en ambas propuestas", "justifica con dato, criterio y conclusión", "decide qué se muestra y qué se corrige", "anota consentimiento, crédito y privacidad"],
        ["tabla de puntajes", "decisión justificada", "frase de crédito"],
        ["mirar solo el total", "no pedir permiso"],
        "Pregunta qué criterio decidió y qué permiso pediría antes de exponer.",
    ),
    "Cuenta a una persona de tu casa por qué un cero en cuidado de las personas puede impedir mostrar una obra aunque tenga un total alto.",
    "Redacta tres frases «dato, criterio, conclusión» sobre un libro o imagen digital que hayas hecho o visto.",
)

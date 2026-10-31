"""Cuaderno del estudiante de 6.º básico Artes Visuales: AR06 OA 03 (dominio de materiales, herramientas y procedimientos ante desafíos del entorno cultural y artístico)."""
from __future__ import annotations

from student_content_ar6_a import lesson, m, task, w
from student_lessons import arith, ex

OA3 = "AR06 OA 03"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Una hoja y un lápiz. Si quieres probar, puedes juntar materiales de tu casa: cartón, papel de diario, tapas, hojas secas, harina, sal y agua. Los desafíos y los materiales se describen en esta clase.",
    "Aprenderé a reconocer los tipos de materiales (de modelado, de reciclaje, naturales, papeles y cartones, pegamentos, lápices, pinturas e imágenes digitales) y a elegir el adecuado para un desafío. Sirve para que mi trabajo resulte como lo imaginé.",
    ["Sé escribir una intención con qué, cómo y por qué.", "Sé que cada material tiene una textura, un peso y una resistencia distintos."],
    [
        "Un desafío en arte es un problema que quiero resolver con una obra: por ejemplo, «mostrar el río de mi ciudad con materiales que normalmente se botan». Para resolverlo elijo materiales. Los materiales de modelado se moldean con las manos, como la arcilla o una masa casera de harina, sal y agua. Los de reciclaje son objetos usados y limpios: cajas, tapas, envases, diarios. Los naturales vienen de la naturaleza: hojas secas, ramas, piedras y arena. También hay papeles y cartones, pegamentos, lápices, pinturas e imágenes digitales, que son fotos o dibujos hechos en una pantalla.",
        "Para elegir bien me pregunto cuatro cosas. Primero, qué textura tiene: lisa, rugosa, blanda o dura. Segundo, qué tan resistente es: si aguanta peso, agua o el paso del tiempo. Tercero, cómo se une: algunos materiales se pegan con cola fría, otros necesitan engrudo o cinta. Cuarto, si es seguro y fácil de conseguir en casa. Un material no es bueno o malo en sí mismo: es adecuado o no para el desafío.",
        "Un mismo desafío se puede resolver con materiales distintos. Si el desafío es mostrar un bosque, puedo usar hojas secas pegadas, papeles rasgados o pintura. Lo importante es poder explicar por qué elegí ese material y qué efecto tiene en la obra. Por último, cuido el ambiente: reutilizo lo que puedo y no uso materiales peligrosos, como vidrio roto, objetos filosos o productos químicos.",
    ],
    [("desafío", "problema o tema que quiero resolver con una obra"), ("material", "lo que uso para hacer la obra"), ("reciclaje", "reutilizar objetos usados y limpios"), ("textura", "cómo se siente o se ve la superficie: lisa, rugosa, blanda"), ("resistencia", "cuánto aguanta un material sin romperse ni deshacerse")],
    [
        w("Elegir según el desafío", "Desafío: hacer una escultura pequeña de una montaña que se vea áspera. ¿Sirven más arena pegada con cola fría o papel lustre liso?", ["La montaña debe verse áspera.", "La arena es rugosa y se pega con cola fría.", "El papel lustre es liso."], "La arena pegada con cola fría"),
        w("Clasificar materiales", "Clasifica: tapas de botella limpias, piedras del patio y arcilla.", ["Las tapas son objetos usados: reciclaje.", "Las piedras vienen de la naturaleza: naturales.", "La arcilla se moldea con las manos: modelado."], "Tapas: reciclaje; piedras: naturales; arcilla: modelado"),
    ],
    [
        m("Elegir el material porque es el que tengo a mano, sin pensar en el desafío.", "El material cambia el resultado y puede no servir.", "Pregunta primero qué textura, resistencia y unión necesita el desafío."),
        m("Usar vidrio o cosas filosas por «ser reciclaje».", "Es peligroso y no corresponde.", "Usa solo materiales seguros: cartón, papel, plástico limpio y natural."),
    ],
    [
        ex("¿La arcilla es un material de modelado o un material de reciclaje?", "De modelado", "Se moldea con las manos para darle forma."),
        ex("¿Una caja de cartón usada y limpia es material de reciclaje o de modelado?", "De reciclaje", "Es un objeto usado que se reutiliza."),
        ex("¿Cuál de estos es un pegamento: la cola fría o la témpera?", "La cola fría", "La cola fría sirve para unir; la témpera es pintura."),
    ],
    [
        ex("Quieres mostrar la corteza de un árbol con una superficie rugosa. ¿Qué material elijes: lija gruesa de papel o papel lustre liso?", "Lija gruesa de papel", "La lija gruesa es rugosa, como una corteza."),
        ex("Un desafío dice: «mostrar un mar con olas hechas de materiales que se botan». ¿Qué material cumple mejor: bolsas plásticas limpias o hojas de cartulina nuevas recién compradas?", "Bolsas plásticas limpias", "Las bolsas son reciclaje y cumplen la condición de lo que se bota."),
        ex("Una masa casera se hace con harina, sal y agua. ¿A qué tipo de material pertenece: modelado, o imagen digital?", "Modelado", "Se amasa y se moldea con las manos."),
    ],
    [
        ex("Haces una maqueta de una isla y quieres que aguante mucho peso encima. ¿Qué eliges como base: cartón grueso o papel de seda?", "Cartón grueso", "El cartón grueso es más resistente que el papel de seda."),
        ex("Quieres pegar hojas secas sobre cartón. ¿Qué usas: cola fría o un lápiz grafito?", "Cola fría", "La cola fría une materiales; el lápiz no pega."),
        arith("Para una masa de sal usas 2 tazas de harina, 1 taza de sal y 1 taza de agua. ¿Cuántas tazas de ingredientes tienes en total?", "2+1+1", "Se suman las tazas de cada ingrediente."),
    ],
    [
        ex("Dos alumnos resuelven el desafío «mostrar un bosque». Rosa pega hojas secas sobre cartón; Mario pinta con témpera verde. ¿Pueden ser válidas las dos soluciones?", "Sí", "Un mismo desafío puede resolverse con materiales distintos si se justifica la elección."),
        ex("Un compañero quiere usar un vidrio roto para una obra de reciclaje. ¿Es una buena elección?", "No", "El vidrio roto es peligroso; se deben usar materiales seguros."),
    ],
    [
        ex("Desafío: representar la lluvia sobre una ciudad con una textura que dé sensación de agua cayendo. Opciones: A) hilos de lana azul colgando pegados con cola fría sobre cartón. B) un cuadrado de cartulina negra sin nada más. ¿Cuál resuelve mejor el desafío?", "A", "Los hilos colgantes sugieren gotas que caen."),
        ex("Tienes que mostrar una montaña con nieve. ¿Qué material natural o reciclable sirve para dar la sensación de nieve blanda: algodón limpio o piedras negras?", "Algodón limpio", "El algodón blanco y blando recuerda la nieve."),
    ],
    ex("Debes hacer un cartel con una imagen de un río para colgar en el patio y que aguante la humedad de la mañana. ¿Cuál es el mejor soporte: papel de seda o cartón grueso pintado?", "Cartón grueso pintado", "El cartón grueso aguanta mejor la humedad que el papel de seda."),
    [
        ex("Para elegir bien un material me pregunto por su textura, su resistencia, cómo se une y si es seguro y fácil de conseguir. ¿Cuántas preguntas son?", "Cuatro", "Son las cuatro preguntas de la explicación: textura, resistencia, unión y seguridad."),
        ex("Verdadero o falso: un material es siempre bueno o siempre malo, sin importar el desafío.", "Falso", "Depende de si sirve para el desafío."),
        ex("¿Qué son las imágenes digitales?", "Fotos o dibujos hechos o editados en una pantalla", "Se crean y modifican con dispositivos y programas."),
    ],
    task(
        "Elige UN desafío. A) Mostrar el río de una ciudad usando solo cosas que normalmente se botan. B) Mostrar un bosque con texturas distintas. C) Mostrar una montaña con nieve y roca. Elige tres materiales (de al menos dos tipos distintos: modelado, reciclaje, naturales, papeles y cartones, pegamentos, lápices o pinturas), haz una prueba pequeña de 10 cm × 10 cm y anota por qué elegiste cada uno.",
        "Elegí la A. Materiales: bolsas plásticas azules (reciclaje), cartón (cartón) y cola fría (pegamento). Prueba: pegué tiras de bolsa sobre el cartón para hacer ondas. Elegí la bolsa porque se bota y se ve brillante como el agua.",
        ["elige tres materiales de dos tipos distintos", "hace una prueba pequeña", "explica la elección con textura o resistencia", "usa materiales seguros"],
        ["prueba de 10 cm × 10 cm", "lista de materiales con razón"],
        ["elegir sin razón", "materiales peligrosos"],
        "Pregunta qué efecto producen los materiales elegidos y qué material cambiaría si el desafío fuera distinto.",
    ),
    "Mira tu casa y nombra un material reciclable limpio, uno natural y uno de papel.",
    "Resuelve el mismo desafío con otros tres materiales y compara cuál resultó más adecuado.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Una hoja, un lápiz, tijeras de punta redonda, un pincel o una esponja y cola fría. Las herramientas especiales se explican en esta clase y no se usan en casa.",
    "Aprenderé a elegir y usar con seguridad herramientas para dibujar, pintar, cortar, unir, modelar y herramientas tecnológicas. Sirve para trabajar mejor, con menos errores y sin accidentes.",
    ["Sé qué materiales hay y cómo elegirlos.", "Sé que cortar se hace alejando los dedos del filo."],
    [
        "Una herramienta es un objeto que uso para trabajar un material. Para dibujar uso lápices, regla y goma. Para pintar uso pinceles, esponjas y rodillos. Para cortar uso tijeras; en casa, siempre de punta redonda y con cuidado. Para unir uso cola fría, cinta o engrudo. Para modelar uso las manos, palitos y espátulas de plástico; el mirete es una herramienta de modelar con un extremo en forma de aro, que se usa con arcilla para sacar material.",
        "También existen herramientas tecnológicas. El rodillo de grabado sirve para repartir tinta sobre una matriz. La cámara de video registra imágenes en movimiento. El proyector multimedia proyecta una imagen sobre un muro, y sirve para calcar un boceto grande antes de pintar un mural. La sierra de calar corta madera en curvas, pero es una herramienta de taller: solo la usa una persona adulta capacitada, y nunca se usa en casa.",
        "Trabajar con herramientas exige reglas de seguridad. Mantengo ordenado el puesto, me siento con buena postura, corto lejos de mis dedos y de otras personas, guardo las tijeras con las puntas hacia abajo y lavo los pinceles al terminar. Si una herramienta es nueva para mí, pregunto antes de usarla. Elegir bien la herramienta también es dominar la técnica: un pincel muy grueso no sirve para un detalle fino.",
    ],
    [("herramienta", "objeto que se usa para trabajar un material"), ("rodillo de grabado", "rodillo que reparte tinta sobre una matriz"), ("proyector multimedia", "aparato que proyecta una imagen sobre un muro"), ("mirete", "herramienta de modelar con un extremo en aro, para quitar arcilla"), ("seguridad", "cuidados para no hacerse daño ni dañar a otros")],
    [
        w("Elegir la herramienta", "Quieres pintar un fondo grande y liso en una cartulina. ¿Qué usas: un pincel muy fino o una esponja o un rodillo?", ["El fondo es una superficie grande.", "El pincel fino tardaría mucho y dejaría rayas.", "La esponja o el rodillo cubren rápido y parejo."], "Una esponja o un rodillo"),
        w("Corregir un hábito inseguro", "Una compañera corta con las tijeras apuntando hacia su mano. ¿Qué debe cambiar?", ["El filo apunta hacia su mano.", "Debe girar el papel y no la mano.", "Corta lejos de los dedos."], "Cortar lejos de los dedos, girando el papel"),
    ],
    [
        m("Usar un pincel grueso para hacer un detalle muy pequeño.", "La herramienta no calza con el trabajo.", "Cambia a un pincel fino para el detalle."),
        m("Apurarse con las tijeras y cortar con los dedos cerca del filo.", "Puede haber un accidente.", "Corta despacio y aleja los dedos."),
    ],
    [
        ex("¿Qué herramienta sirve para unir dos cartones: la cola fría o la regla?", "La cola fría", "La cola une; la regla sirve para medir."),
        ex("¿La cámara de video sirve para registrar imágenes quietas o en movimiento?", "En movimiento", "El video registra secuencias en movimiento."),
        ex("¿Qué se usa para repartir tinta sobre una matriz de grabado: un rodillo o una tijera?", "Un rodillo", "El rodillo de grabado reparte la tinta."),
    ],
    [
        ex("¿Para cuál de estas acciones se usa un pincel: dibujar, pintar, cortar, unir o modelar?", "Pintar", "El pincel reparte pintura."),
        ex("El proyector multimedia se usa en un mural para...", "Proyectar el boceto sobre el muro y calcarlo", "Ayuda a ampliar el dibujo con exactitud."),
        ex("La sierra de calar es una herramienta de taller. ¿La puedes usar en casa por tu cuenta?", "No", "Solo la usa una persona adulta capacitada en un taller."),
    ],
    [
        ex("Necesitas un detalle muy fino, como las pestañas de un ojo dibujado. ¿Qué elijes: un pincel fino o una esponja?", "Un pincel fino", "El pincel fino permite hacer detalles pequeños."),
        ex("Quieres cortar una cartulina en tiras. ¿Dónde pones los dedos: lejos de la línea de corte o sobre la línea de corte?", "Lejos de la línea de corte", "Así evitas cortarte."),
        arith("Tienes 3 pinceles finos y 2 pinceles gruesos. ¿Cuántos pinceles hay en total?", "3+2", "Se suman los pinceles de cada tipo."),
    ],
    [
        ex("Una persona dice que para modelar con arcilla solo se pueden usar las manos. ¿Tiene razón?", "No", "También se usan palitos, espátulas y miretes."),
        ex("Un compañero guarda las tijeras con las puntas hacia arriba dentro de un vaso. ¿Es un hábito seguro?", "No", "Las puntas hacia arriba pueden pinchar; deben guardarse con las puntas hacia abajo."),
    ],
    [
        ex("Para un mural de 4 m quieres calcar un boceto en el muro sin errores de proporción. ¿Qué herramienta tecnológica ayuda: el proyector multimedia o el pincel grueso?", "El proyector multimedia", "Proyecta la imagen a gran tamaño para calcarla."),
        ex("Tu pincel está duro porque no lo lavaste. ¿Qué debías haber hecho al terminar de pintar?", "Lavarlo", "Lavar el pincel evita que la pintura se seque y lo endurezca."),
    ],
    ex("Tienes que pegar una hoja seca delicada sin que se rompa ni se arrugue. ¿Qué herramienta de unir eliges: un poco de cola fría con un palito delgado o mucho pegamento con las manos?", "Un poco de cola fría con un palito delgado", "Permite controlar la cantidad y no dañar la hoja."),
    [
        ex("¿Para qué sirve una herramienta en el trabajo de arte?", "Para trabajar un material", "Cada herramienta ayuda a dibujar, pintar, cortar, unir o modelar."),
        ex("Verdadero o falso: en casa se pueden usar herramientas eléctricas de taller sin supervisión.", "Falso", "Eso es peligroso y solo corresponde a un adulto capacitado."),
        ex("¿Cómo se guardan las tijeras con seguridad?", "Con las puntas hacia abajo", "Así no pinchan al sacarlas."),
    ],
    task(
        "Elige UN trabajo. A) Pintar un fondo celeste de 15 cm × 15 cm y después un detalle fino en negro. B) Cortar 8 tiras de cartulina de 2 cm × 10 cm y pegarlas formando una cerca. C) Modelar con masa de sal una figura pequeña y marcar líneas con un palito. Anota qué herramientas usaste, en qué orden, y una regla de seguridad que cumpliste.",
        "Elegí la A. Herramientas: esponja para el fondo, pincel fino para el detalle. Orden: fondo, secar, detalle. Seguridad: lavé los pinceles al terminar y mantuve la mesa ordenada.",
        ["nombra las herramientas usadas", "las ordena según el trabajo", "cumple y nombra una regla de seguridad", "explica por qué eligió esa herramienta"],
        ["trabajo terminado", "lista de herramientas y orden"],
        ["usar la herramienta equivocada", "descuidar la seguridad"],
        "Pregunta qué cambiaría si usara otra herramienta para el mismo paso y cómo cambiaría el resultado.",
    ),
    "Revisa tus útiles y di para qué sirve cada uno y cómo se guarda de forma segura.",
    "Prueba el mismo trazo con tres herramientas distintas y describe cómo cambia.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Cartón delgado, cartulina, témpera, un pincel, una esponja o un rodillo pequeño de papel enrollado, cola fría y una hoja. No se usan cuchillos ni grabado con herramientas filosas.",
    "Aprenderé tres procedimientos: la pintura, el grabado (con una matriz de cartón) y la escultura. Sirve para decidir con qué procedimiento resuelvo mejor un desafío y para dominar sus pasos.",
    ["Sé elegir materiales y herramientas según un desafío.", "Sé que un procedimiento es una secuencia de pasos."],
    [
        "La pintura se hace aplicando color sobre una superficie. Un procedimiento ordenado es: primero el fondo, después las figuras grandes y al final los detalles. Se deja secar entre capas para que los colores no se mezclen sin querer. El grabado sirve para hacer copias de una imagen. Se prepara una matriz, que es una superficie con la imagen en relieve; se reparte tinta o témpera sobre ella con un rodillo y se presiona sobre un papel. Cada copia se llama estampa.",
        "En el grabado la estampa sale invertida, como en un espejo: lo que está a la izquierda de la matriz queda a la derecha en el papel. Por eso las letras se graban al revés. Para una matriz sencilla en casa se pega cartulina recortada sobre un cartón. La escultura es el procedimiento para crear obras con volumen. Se puede modelar, que es agregar material como arcilla; tallar, que es quitar material de un bloque; o ensamblar, que es unir piezas con pegamento.",
        "Elegir un procedimiento depende del desafío. Si quiero muchas copias iguales de un afiche, elijo el grabado. Si quiero mostrar gradaciones suaves de color, elijo la pintura. Si quiero que la obra se pueda rodear con la mirada, elijo la escultura. Dominar un procedimiento significa seguir sus pasos, cuidar los materiales y poder explicar qué hice en cada etapa. También reviso el resultado y anoto qué ajustaría la próxima vez.",
    ],
    [("pintura", "procedimiento de aplicar color sobre una superficie"), ("grabado", "procedimiento para hacer copias de una imagen con una matriz"), ("matriz", "superficie con la imagen en relieve que se entinta"), ("estampa", "copia obtenida en el grabado"), ("escultura", "procedimiento para crear obras con volumen")],
    [
        w("Invertir la imagen", "Pegas en la matriz una flecha de cartulina que apunta hacia la derecha. ¿Hacia dónde apunta en la estampa?", ["La estampa se ve como en un espejo.", "Lo que apunta a la derecha en la matriz apunta a la izquierda en la estampa.", "Hay que recordarlo al grabar letras o dibujos con dirección."], "Hacia la izquierda"),
        w("Elegir el procedimiento", "Necesitas 20 afiches iguales para una feria. ¿Eliges pintura a mano en cada uno o grabado con una matriz?", ["Se necesitan muchas copias iguales.", "La matriz permite repetir la imagen.", "Pintar cada uno a mano llevaría mucho tiempo y saldrían distintos."], "Grabado con matriz"),
    ],
    [
        m("Escribir las letras en la matriz tal como se leen y sorprenderse porque salen al revés.", "La estampa invierte la imagen.", "Graba las letras invertidas, como en un espejo."),
        m("Pintar el detalle antes de que se seque el fondo.", "Los colores se mezclan y se ensucian.", "Espera a que cada capa se seque."),
    ],
    [
        ex("¿Qué procedimiento sirve para hacer muchas copias de una imagen: pintura o grabado?", "Grabado", "La matriz permite repetir la imagen."),
        ex("La copia que se obtiene en el grabado se llama...", "Estampa", "Cada impresión de la matriz es una estampa."),
        ex("¿La escultura trabaja con volumen o solo con una superficie plana?", "Con volumen", "La escultura crea obras que se rodean con la mirada."),
    ],
    [
        ex("Ordena los pasos de una pintura: 1) detalles, 2) fondo, 3) figuras grandes. Escribe los números en orden.", "2, 3, 1", "Se pinta primero el fondo, luego las figuras y al final los detalles."),
        ex("En una matriz hay un triángulo a la izquierda de un círculo. ¿Dónde queda el triángulo en la estampa?", "A la derecha del círculo", "La estampa se invierte como un espejo."),
        ex("Modelar es agregar material y tallar es...", "Quitar material", "Tallar saca material de un bloque."),
    ],
    [
        ex("Quieres grabar la palabra «SOL» para que se lea bien en la estampa. ¿Cómo debes escribirla en la matriz: igual que se lee o invertida como en un espejo?", "Invertida como en un espejo", "La estampa invierte la imagen."),
        arith("Tienes una matriz y sacas 3 estampas en una hoja y 4 en otra. ¿Cuántas estampas tienes en total?", "3+4", "Se suman las estampas de cada hoja."),
        ex("Quieres una escultura pequeña con trozos de cartón pegados. ¿Qué tipo de escultura haces: modelar, tallar o ensamblar?", "Ensamblar", "Ensamblar es unir piezas."),
    ],
    [
        ex("Un compañero quiere una imagen con colores que se mezclan suavemente del azul al verde. ¿Qué procedimiento le sirve más: pintura o grabado con una matriz de cartón?", "Pintura", "La pintura permite mezclar y difuminar colores."),
        ex("Otra compañera entinta una matriz con demasiada témpera y la estampa sale manchada. ¿Qué debe cambiar: poner menos témpera o presionar con más fuerza?", "Poner menos témpera", "El exceso de pintura mancha y borra los detalles."),
    ],
    [
        ex("Tienes que mostrar un árbol que se vea distinto desde cada lado. ¿Qué procedimiento eliges: escultura o grabado?", "Escultura", "Solo una obra con volumen se ve distinta desde cada lado."),
        ex("Tu estampa salió al revés y quieres que el dibujo de la matriz y la estampa se vean iguales. ¿Qué puedes hacer: dibujar la imagen simétrica o tallar solo la mitad?", "Dibujar la imagen simétrica", "Una imagen simétrica se ve igual aunque se invierta."),
    ],
    ex("Debes hacer un afiche para la entrada de la escuela que se repita 6 veces en una tira larga. ¿Haces 6 pinturas distintas a mano o una matriz con la que estampas 6 veces?", "Una matriz con la que estampas 6 veces", "La matriz permite repetir la misma imagen sin rehacerla."),
    [
        ex("¿Qué es una matriz?", "Una superficie con la imagen en relieve que se entinta", "Se presiona sobre el papel para obtener la estampa."),
        ex("Verdadero o falso: en el grabado la estampa sale invertida respecto de la matriz.", "Verdadero", "La imagen se ve como en un espejo."),
        ex("Nombra una forma de hacer escultura.", "Modelar, tallar o ensamblar", "Son tres procedimientos de la escultura."),
    ],
    task(
        "Elige UNA prueba. A) Haz una matriz de cartón con un pez de cartulina pegado y saca dos estampas con témpera. B) Pinta un paisaje de tres capas (fondo, figuras, detalles) esperando que cada capa se seque. C) Modela con masa de sal una figura que se pueda mirar por todos lados. Anota los pasos, qué observaste y qué ajustarías.",
        "Elegí la A. Pasos: pegué el pez, repartí témpera con una esponja, presioné sobre una hoja. Observé que el pez se estampó mirando a la izquierda, al revés que en la matriz. La segunda estampa salió más clara. Ajustaría poniendo un poco más de témpera.",
        ["sigue los pasos del procedimiento", "anota qué observó", "reconoce el efecto del procedimiento", "propone un ajuste"],
        ["trabajo terminado", "pasos y ajuste escritos"],
        ["omitir pasos", "exceso de material"],
        "Pregunta qué paso del procedimiento influyó más en el resultado y qué ajuste probaría.",
    ),
    "Mira un sello o una letra impresa y di qué cambia si se estampa en un papel.",
    "Haz el mismo dibujo con grabado y con pintura y compara cuál es más fácil de repetir.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Cartón, papeles de diario o de revista, envases limpios, témpera, un pincel, cola fría, tijeras de punta redonda y un lugar plano donde dejar una obra pequeña. Los desafíos se ofrecen en la actividad.",
    "Aprenderé a crear una obra usando técnica mixta e instalación con materiales de reciclaje. Sirve para resolver un desafío combinando materiales y procedimientos de forma coherente.",
    ["Sé elegir materiales, herramientas y procedimientos.", "Sé que una instalación es una obra que ocupa un espacio y se recorre."],
    [
        "La técnica mixta combina dos o más materiales o procedimientos en una misma obra, por ejemplo pintura con papeles pegados (collage) o dibujo con elementos naturales. Una instalación organiza objetos en un espacio para que el público los recorra. Cuando uso materiales de reciclaje, como cajas, tapas y envases limpios, además de crear cuido el ambiente. Estos recursos permiten responder a desafíos del entorno cultural, como mostrar la vida de un barrio o un problema de la ciudad.",
        "Para combinar bien, planifico. Defino el desafío, elijo dos materiales que se complementen, decido el orden de trabajo y compruebo que lo pegado quede firme. Por ejemplo, para mostrar un mercado puedo pegar papeles de colores sobre cartón, pintar encima los detalles y agregar cajitas en relieve. Algunas combinaciones no funcionan: un papel muy fino bajo mucha cola se rompe. Probar en pequeño evita perder todo el trabajo.",
        "En una instalación pienso en el recorrido: cómo caminará la persona, qué verá primero y a qué distancia estarán los objetos. Mido el espacio, aunque sea una mesa, y dejo huecos entre las piezas. Anoto qué materiales usé y por qué. También cuido la seguridad y la limpieza: nada de vidrio ni objetos filosos, y todo lo que uso debe estar limpio y seco.",
    ],
    [("técnica mixta", "obra que combina dos o más materiales o procedimientos"), ("collage", "obra hecha pegando papeles u otros materiales sobre una superficie"), ("instalación", "obra con objetos ordenados en un espacio que se recorre"), ("recorrido", "camino que sigue quien mira la instalación"), ("coherente", "que todas las partes sirven a la misma idea")],
    [
        w("Planificar una técnica mixta", "Desafío: mostrar un mercado con mucho color. Tienes papeles de revista, cartón, témpera y cola fría. Planifica el orden.", ["Primero pego papeles de colores como fondo sobre el cartón.", "Cuando la cola esté seca, pinto detalles encima con témpera.", "Por último agrego cajitas pequeñas en relieve para los puestos."], "Papeles pegados, luego detalles pintados y al final cajitas en relieve"),
        w("Pensar el recorrido", "Una instalación de 8 tapas de colores sobre una mesa de 60 cm de largo se recorrerá de izquierda a derecha. Quieres que la tapa más importante sea lo último que se vea. ¿Dónde la pones?", ["El recorrido va de izquierda a derecha.", "Lo último que se ve queda en el extremo derecho.", "La pongo al final del recorrido, a la derecha, con más espacio alrededor."], "Al final del recorrido, con más espacio alrededor"),
    ],
    [
        m("Pegar muchas capas de papel con demasiada cola, que se arruga.", "La humedad del pegamento deforma el papel.", "Usa poca cola, extendida con un pincel, y deja secar."),
        m("Poner todos los objetos de la instalación pegados, sin dejar espacio para recorrer.", "No se puede mirar cada objeto.", "Deja huecos y piensa por dónde camina quien mira."),
    ],
    [
        ex("La técnica mixta combina dos o más...", "Materiales o procedimientos", "Es combinar más de un recurso en una obra."),
        ex("Pegar papeles de revista sobre un cartón para hacer una imagen se llama...", "Collage", "El collage se hace pegando materiales sobre una superficie."),
        ex("Una instalación se hace para que el público la recorra. ¿Verdadero o falso?", "Verdadero", "Una instalación ocupa un espacio y se recorre."),
    ],
    [
        ex("Una obra tiene pintura, papeles pegados y ramitas secas. ¿Es una técnica mixta?", "Sí", "Combina tres tipos de materiales."),
        ex("¿Por qué es bueno usar materiales de reciclaje en una instalación? A: Porque se reutiliza y se cuida el ambiente. B: Porque son más caros.", "A", "El reciclaje reutiliza objetos y cuida el ambiente."),
        ex("Antes de pintar encima de papeles pegados, ¿qué debes esperar?", "Que la cola esté seca", "La cola húmeda hace que la pintura se corra o el papel se arrugue."),
    ],
    [
        arith("Armas una instalación con 4 filas de 5 envases limpios. ¿Cuántos envases usas?", "4*5", "Se multiplican filas por envases de cada fila."),
        ex("Quieres que se vean tres puestos de un mercado en relieve. ¿Qué material sirve: cajitas pequeñas pegadas sobre el cartón o una hoja lisa sin nada pegado?", "Cajitas pequeñas pegadas", "Dan relieve y sensación de volumen."),
        ex("Quieres mostrar el reciclaje en tu barrio. ¿Qué objeto es adecuado para tu obra: un envase de plástico limpio o un vidrio roto?", "Un envase de plástico limpio", "Es reutilizable y seguro; el vidrio roto es peligroso."),
    ],
    [
        ex("Tu collage se arrugó porque pegaste con mucha cola. ¿Qué haces en la próxima prueba: usar menos cola o más cola?", "Menos cola", "El exceso de humedad deforma el papel."),
        ex("En una mesa de 60 cm de largo quieres 6 objetos con el mismo espacio entre cada uno. Si cada objeto mide 6 cm y no cuentas los bordes, ¿cuántos centímetros de espacio libre te quedan para repartir?", "24", "Los objetos ocupan 36 cm y el espacio libre es 60 − 36 = 24.", calc="60-6*6"),
    ],
    [
        ex("Tu desafío es mostrar la lluvia en la ciudad. Tienes cartón gris, hilos de lana azul, cola fría y tapas. ¿Qué combinación es coherente: cartón gris de fondo con hilos azules colgando o tapas rojas sobre fondo amarillo?", "Cartón gris de fondo con hilos azules colgando", "Evoca un cielo gris y gotas que caen."),
        ex("Debes llevar tu instalación a otra mesa y quieres que no se rompa. ¿Qué haces: pegarla sobre una base de cartón firme o dejar las piezas sueltas?", "Pegarla sobre una base de cartón firme", "Una base firme mantiene unidas las piezas."),
    ],
    ex("Una obra sobre «mi barrio» usa solo pintura sobre cartón. Para convertirla en técnica mixta, ¿qué agregas: papeles de revista pegados (collage) o una segunda capa de la misma pintura?", "Papeles de revista pegados (collage)", "La técnica mixta combina otro material o procedimiento, no repite el mismo."),
    [
        ex("¿Qué debes pensar al hacer una instalación?", "El recorrido de quien mira", "Define por dónde se camina y qué se ve primero."),
        ex("Verdadero o falso: en una técnica mixta se puede pintar sobre papeles pegados cuando la cola está seca.", "Verdadero", "Así los materiales no se estropean."),
        ex("¿Qué material no debe usarse en obras de reciclaje por seguridad?", "Vidrio roto", "Puede cortar y es peligroso."),
    ],
    task(
        "Elige UN desafío. A) Mostrar un mercado de barrio con colores y texturas (cartón, papeles de revista y pintura). B) Mostrar el cuidado del agua con una instalación de 20 envases limpios en una mesa. C) Mostrar el recorrido de una calle con una maqueta de cajas pequeñas. Planifica el orden de trabajo, hazla y anota qué combinación de materiales usaste y por qué.",
        "Elegí la A. Orden: pegué papeles de colores como fondo sobre el cartón, esperé que se secara y pinté los puestos encima. Agregué tres cajitas en relieve. Combiné papel, pintura y cajas porque dan color y volumen al mercado.",
        ["planifica el orden", "combina al menos dos materiales", "explica por qué combina así", "usa materiales seguros"],
        ["obra terminada", "orden y explicación escritos"],
        ["pegar con demasiada cola", "sin recorrido"],
        "Pregunta qué combinación resultó más expresiva y qué cambiaría si tuviera otro material.",
    ),
    "Mira una caja vacía y di cómo la usarías en una obra de técnica mixta.",
    "Reorganiza tu instalación con otro recorrido y explica cómo cambia lo que se ve primero.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Una hoja, un lápiz y un cuadrado de cartulina con un marco recortado (un visor de 6 cm × 4 cm) para mirar. Si tienes un teléfono, una cámara o un computador puedes usarlo con permiso de una persona adulta; si no, haz todo con dibujos.",
    "Aprenderé qué son la fotografía, el video y el arte digital, y cómo se relacionan con el mural, para justificar el procedimiento que elijo. Sirve para explicar mis decisiones con evidencia de cómo el procedimiento cambia el resultado.",
    ["Sé qué son la pintura, el grabado y la escultura.", "Sé que cada procedimiento cambia lo que puedo expresar."],
    [
        "La fotografía registra una imagen con luz. Al fotografiar decido el encuadre, es decir, qué parte de la escena entra en la imagen y qué queda afuera. Un plano general muestra todo el lugar; un primer plano muestra un detalle de cerca. También decido el ángulo: desde arriba, desde abajo o de frente. Para practicar sin cámara, miro la escena a través de un marco recortado en cartulina y muevo el marco. Nunca fotografío a otra persona sin su permiso ni subo imágenes sin autorización.",
        "El video es una secuencia de imágenes con movimiento. Antes de grabar, muchas personas hacen un guion gráfico: dibujos en cuadros que muestran qué se verá primero, después y al final. El arte digital se crea o modifica con un dispositivo y un programa; permite trabajar por capas, deshacer errores y copiar. Estos procedimientos se parecen a los anteriores: en todos hay una intención, una elección de recursos y un resultado que se revisa.",
        "El mural también puede relacionarse con lo digital. Con un proyector multimedia se puede proyectar un boceto sobre el muro y calcarlo. Para elegir un procedimiento hago una pregunta: ¿qué quiero comunicar y cuál lo hace mejor? Si quiero mostrar un movimiento, el video sirve; si quiero conservar un instante, la fotografía; si quiero una imagen que muchas personas vean en la calle, el mural. Justificar significa explicar con ejemplos del resultado, no con gustos.",
    ],
    [("fotografía", "procedimiento que registra imágenes con luz"), ("encuadre", "parte de la escena que entra en la imagen"), ("plano general", "plano que muestra todo el lugar"), ("primer plano", "plano que muestra un detalle de cerca"), ("guion gráfico", "dibujos en cuadros que planean un video")],
    [
        w("Elegir el procedimiento", "Quieres mostrar cómo una pelota rebota en un patio. ¿Eliges fotografía de un instante o video?", ["Lo que quiero mostrar es movimiento.", "La fotografía congela un solo instante.", "El video registra la secuencia completa."], "Video"),
        w("Decidir un encuadre", "En una escena de un parque con un niño y un gran árbol, quieres mostrar lo pequeño que se ve el niño. ¿Plano general o primer plano?", ["Quiero comparar el niño con el árbol.", "El plano general deja ver todo el parque.", "El primer plano solo mostraría un detalle del niño."], "Plano general"),
    ],
    [
        m("Fotografiar a una persona sin pedirle permiso.", "Se invade su privacidad.", "Pide permiso y, si no hay, fotografía objetos o paisajes."),
        m("Elegir fotografía o video «porque se ve moderno», sin pensar en la intención.", "El procedimiento debe servir a lo que quiero comunicar.", "Pregunta qué comunica mejor tu idea."),
    ],
    [
        ex("El encuadre es la parte de la escena que...", "Entra en la imagen", "Define qué se muestra y qué se deja fuera."),
        ex("Un plano que muestra todo el lugar se llama...", "Plano general", "Muestra el conjunto de la escena."),
        ex("¿La fotografía registra una imagen fija o una secuencia en movimiento?", "Una imagen fija", "El video es el que registra secuencias en movimiento."),
    ],
    [
        ex("Quieres mostrar el detalle de una hoja con sus nervaduras. ¿Qué plano usas: general o primer plano?", "Primer plano", "El primer plano muestra detalles de cerca."),
        ex("Un guion gráfico sirve para...", "Planear qué se verá en un video", "Son dibujos en cuadros que ordenan las escenas."),
        ex("¿Cuál procedimiento permite trabajar por capas y deshacer errores: el arte digital o el grabado?", "El arte digital", "Los programas de dibujo digital usan capas y permiten deshacer."),
    ],
    [
        ex("Haces un video de 4 escenas de 5 segundos cada una. ¿Cuántos segundos dura en total?", "20 segundos", "4 escenas de 5 segundos suman 20.", calc="4*5"),
        ex("Quieres mostrar que una calle estaba vacía a las seis de la mañana. ¿Qué plano usas: general de toda la calle o primer plano de una baldosa?", "General de toda la calle", "El plano general muestra que no hay nadie."),
        ex("Quieres fotografiar desde abajo un edificio para que parezca muy alto. ¿Qué ángulo usas?", "Desde abajo", "Mirar hacia arriba exagera la altura."),
    ],
    [
        ex("Dos compañeras quieren mostrar un instante exacto, el momento en que una gota golpea el agua. Una elige fotografía y la otra video. ¿Quién resuelve mejor «un instante exacto»?", "La que elige fotografía", "La fotografía congela un momento."),
        ex("Un compañero quiere calcar un boceto de 30 cm en una pared de 3 metros sin errores. ¿Qué herramienta tecnológica sirve?", "El proyector multimedia", "Proyecta la imagen ampliada para calcarla."),
    ],
    [
        ex("Quieres mostrar un cambio: la flor cerrada por la mañana y abierta en la tarde. ¿Qué procedimiento sirve más: una pintura o una secuencia de fotos o un video?", "Una secuencia de fotos o un video", "Muestran cambios en el tiempo."),
        ex("Quieres mostrar la soledad de una banca en una plaza enorme y vacía. ¿Qué plano eliges: general o primer plano?", "General", "Se necesita ver toda la plaza para notar el espacio vacío."),
    ],
    ex("Debes explicar por qué elegiste un primer plano de unas manos que amasan pan en vez de un plano general de toda la cocina. ¿Qué razón es mejor: «porque quería mostrar el trabajo de las manos» o «porque sí»?", "Porque quería mostrar el trabajo de las manos", "La razón conecta el plano con la intención."),
    [
        ex("¿Qué diferencia hay entre plano general y primer plano?", "El general muestra todo; el primer plano, un detalle", "Cambian cuánto de la escena entra."),
        ex("Verdadero o falso: se puede fotografiar a cualquier persona sin pedirle permiso.", "Falso", "Hay que respetar su privacidad."),
        ex("¿Para qué se hace un guion gráfico?", "Para planear las escenas del video", "Ordena qué se verá primero, después y al final."),
    ],
    task(
        "Elige UNA escena. A) Un niño frente a un árbol enorme en un parque. B) Unas manos que amasan pan en una mesa. C) Una micro que se aleja por una avenida. Con el visor de cartulina (o con tu cámara, solo de objetos o paisajes) haz dos encuadres distintos de la escena, dibuja cada uno y haz un guion gráfico de 3 cuadros. Escribe qué procedimiento elegirías (fotografía, video o mural) y por qué.",
        "Elegí la A. Encuadre 1: plano general con niño pequeño bajo el árbol. Encuadre 2: primer plano de la corteza. Guion: 1) árbol, 2) niño que llega, 3) niño mirando hacia arriba. Elijo fotografía del plano general, porque quiero mostrar lo pequeño que es el niño frente al árbol.",
        ["hace dos encuadres distintos", "dibuja un guion de tres cuadros", "elige un procedimiento con razón", "respeta la privacidad"],
        ["dos dibujos de encuadre", "guion gráfico de tres cuadros"],
        ["elegir sin razón", "fotografiar personas sin permiso"],
        "Pregunta qué cambia en el mensaje entre los dos encuadres y por qué eligió ese procedimiento.",
    ),
    "Mira un objeto con el visor de cartulina y muévelo para tener dos encuadres distintos.",
    "Cambia el ángulo del encuadre y explica cómo cambia la sensación de tamaño.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA3, 6,
    "Una obra o prueba de las clases anteriores (o las pruebas descritas en esta clase), una hoja para el registro, lápiz y los materiales con que la hiciste.",
    "Aprenderé a revisar el dominio de materiales, herramientas y procedimientos en mi obra: detectar problemas de técnica, corregirlos y mantener mi autoría. Sirve para que mi trabajo mejore sin perder mi idea.",
    ["Sé elegir materiales, herramientas y procedimientos.", "Sé que revisar es mirar de nuevo la obra con criterios."],
    [
        "Revisar el dominio de la técnica es mirar si usé bien los materiales y las herramientas y si seguí los pasos del procedimiento. Algunos problemas frecuentes son: pintura que chorrea por exceso de agua, papel que se arruga por mucha cola, estampa manchada por demasiada tinta, piezas que se despegan por falta de secado o presión. Cada problema tiene una causa y una solución concreta: usar menos agua, extender poca cola, repartir menos tinta o presionar y esperar el secado.",
        "Para revisar uso una lista de preguntas: ¿el material fue adecuado para el desafío? ¿Usé la herramienta correcta? ¿Seguí los pasos en orden? ¿La obra se ve como la imaginé? Anoto lo que funcionó y lo que no. Después decido qué cambio hacer, mantengo mi idea original y registro el resultado. Si un compañero me da una sugerencia, decido yo si la aplico, según si me ayuda a comunicar mejor mi intención.",
        "Mejorar la técnica no es cambiar la idea. Si mi obra quiere mostrar un mercado alegre y el color chorrea, corrijo el chorreado, pero no cambio el mercado por un paisaje. Al final comparo la primera versión con la segunda y escribo qué aprendí sobre el material o el procedimiento. Así domino mejor mi trabajo y puedo explicarlo con claridad, usando palabras como matriz, capa, secado y encuadre.",
    ],
    [("dominio", "uso seguro y correcto de materiales, herramientas y procedimientos"), ("chorrear", "correrse la pintura por exceso de agua o de líquido"), ("secado", "tiempo que necesita la pintura o la cola para quedar firme"), ("causa", "razón por la que ocurre un problema"), ("registro", "nota de lo que cambié y por qué")],
    [
        w("Encontrar la causa", "Tu pintura chorrea por la hoja. ¿Cuál es la causa más probable y qué cambias?", ["La pintura corre cuando hay mucha agua.", "Un pincel muy mojado deja demasiada agua.", "Uso menos agua y escurro el pincel."], "Exceso de agua; usar menos y escurrir el pincel"),
        w("Conservar la idea", "Un compañero te dice: «Cambia tu mercado alegre por un paisaje gris». Tu idea es la alegría del mercado. ¿Qué haces?", ["La sugerencia cambia la idea.", "Mi intención es la alegría del mercado.", "No lo aplico y corrijo solo la técnica."], "No lo aplico; mantengo mi idea y corrijo la técnica"),
    ],
    [
        m("Cambiar toda la obra cuando hay un problema de técnica.", "Se pierde la idea que ya estaba clara.", "Corrige solo el problema técnico."),
        m("No anotar qué cambié.", "No sé qué funcionó para la próxima vez.", "Haz un registro corto de causa, cambio y resultado."),
    ],
    [
        ex("Si la pintura chorrea, ¿la causa más probable es mucha agua o poca agua?", "Mucha agua", "El exceso de agua hace que la pintura corra."),
        ex("Si el papel se arruga al pegarlo, ¿qué cantidad de cola usaste: mucha o poca?", "Mucha", "Demasiada cola moja y deforma el papel."),
        ex("Una estampa sale manchada. ¿Qué cambias: poner menos tinta o más tinta?", "Poner menos tinta", "El exceso de tinta mancha y tapa los detalles."),
    ],
    [
        ex("Una pieza se despega. ¿Qué haces: presionar y esperar el secado o moverla de inmediato?", "Presionar y esperar el secado", "La cola necesita tiempo para unir bien."),
        ex("¿Qué dice un registro de revisión: causa, cambio y resultado, o solo si te gustó?", "Causa, cambio y resultado", "Permite entender el problema y su solución."),
        ex("Cambiar la técnica para corregir el chorreado, ¿cambia también la idea de tu obra?", "No", "Corregir la técnica no cambia lo que quieres comunicar."),
    ],
    [
        ex("En la primera versión pegaste 12 papeles y en la segunda pegaste 5 menos. ¿Cuántos papeles tiene la segunda?", "7", "Son 12 menos 5.", calc="12-5"),
        ex("Tu obra es una matriz con un pez y la estampa salió muy clara. ¿Cuál es la mejor corrección: poner un poco más de témpera o cambiar el pez por una flor?", "Poner un poco más de témpera", "El problema es técnico y no cambia la idea."),
        ex("Un compañero te sugiere cambiar el color del fondo y tú ves que ayuda a que se vea tu figura. ¿Qué decisión tomas?", "Aplicarla", "La sugerencia mejora la visibilidad sin cambiar la intención."),
    ],
    [
        ex("Una amiga dice: «Mi técnica es perfecta porque terminé rápido». ¿Es un argumento válido sobre el dominio de la técnica?", "No", "Terminar rápido no demuestra que los pasos y materiales estén bien usados."),
        ex("Tu escultura se cae. Sofía propone una base más ancha y Juan propone usar menos pegamento. ¿Qué cambio explica mejor por qué se cae?", "La base más ancha", "Una base angosta no la sostiene; el pegamento no es la causa."),
    ],
    [
        ex("Tu mural pequeño de papeles pegados se despega por las esquinas. Revisas: usaste poca cola en los bordes y no esperaste el secado. ¿Qué dos correcciones haces?", "Más cola en los bordes y esperar el secado", "Atacan las dos causas encontradas."),
        ex("Dos compañeros revisaron la misma obra. Uno dijo «el color está feo». El otro dijo «el azul chorrea sobre el amarillo porque no se secó». ¿Qué comentario ayuda más a mejorar la técnica?", "El segundo", "Señala el problema y su causa."),
    ],
    ex("En una prueba de grabado, las letras de tu cartel salieron al revés. Quieres que se lean bien. ¿Qué corrección haces: invertir las letras en la matriz o dejar las letras como están?", "Invertir las letras en la matriz", "La estampa invierte la imagen, así que la matriz debe estar al revés."),
    [
        ex("¿Qué es el dominio de la técnica?", "Usar bien materiales, herramientas y procedimientos", "Incluye seguir los pasos y cuidar el resultado."),
        ex("Verdadero o falso: corregir un problema técnico obliga a cambiar la idea de la obra.", "Falso", "Se puede mejorar la técnica y mantener la idea."),
        ex("¿Qué tres datos anotas en un registro de revisión?", "Causa, cambio y resultado", "Así sabes qué pasó, qué hiciste y qué efecto tuvo."),
   ],
    task(
        "Elige UNA prueba que tenga un problema. A) Una pintura que chorrea sobre una cartulina. B) Un collage de papeles que se arruga por exceso de cola. C) Una estampa de cartón con las letras escritas al derecho. Escribe la causa, la corrección y el resultado esperado. Rehaz la prueba si puedes y compara la primera versión con la segunda.",
        "Elegí la A. Causa: puse mucha agua y el pincel estaba muy mojado. Corrección: usé menos agua y escurrí el pincel. Resultado: el color quedó firme y no corrió. Mi idea del atardecer sigue igual.",
        ["identifica la causa", "propone una corrección concreta", "mantiene la idea original", "escribe el registro"],
        ["prueba corregida", "registro de tres partes"],
        ["cambiar la idea", "no explicar la causa"],
        "Pregunta cómo supo cuál era la causa y qué diría a un compañero que tenga el mismo problema.",
    ),
    "Mira algo que hiciste en esta unidad y di un problema de técnica que tuvo y cómo lo resolviste.",
    "Haz tres pruebas de una misma técnica con distinta cantidad de material y explica cuál es la mejor.",
)

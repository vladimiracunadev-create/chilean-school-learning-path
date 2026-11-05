"""Cuaderno del estudiante de 2.º medio Artes Visuales: AR2M OA 02 (escultura y diseño con materiales sustentables)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA2 = "AR2M OA 02"


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
    OA2, 1,
    "Hojas, lápiz y, si quieres, una caja de cartón o un envase plástico bien lavado de tu casa. Las fichas de las obras de ejemplo están escritas en la clase. No se usan cuchillos ni fuego.",
    "Aprenderé a observar una escultura o un objeto de diseño mirando su contexto, su lenguaje visual y su propósito, y a juzgar si sus materiales son sustentables. Sirve para decidir con razones qué materiales usar en un proyecto propio.",
    ["Sé que una manifestación visual se lee por contexto, lenguaje visual y propósito.", "Sé separar lo que se ve de lo que interpreto."],
    [
        "Una escultura es una obra con volumen, es decir, que ocupa espacio y se rodea con la mirada. Un objeto de diseño resuelve además una necesidad, como sentarse o guardar cosas. Un material sustentable es el que se obtiene, se usa y se descarta con poco daño al ambiente. Puede ser reutilizado (se usa de nuevo en otra función) o reciclable (puede volver a procesarse como materia prima).",
        "Para saber si un material es sustentable reviso su ciclo de vida, que tiene tres etapas: origen (de dónde viene), uso (cuánto dura y cómo se usa) y descarte (qué pasa cuando ya no sirve). Un cartón de cajas usadas que se une con cordel y se puede desarmar tiene un buen ciclo de vida. Un material que se compra nuevo para una sola obra y luego se bota, no.",
        "Observo también con el lenguaje visual: forma, textura (cómo se siente o se ve la superficie), color y equilibrio. Primero describo lo que se ve, luego interpreto con «podría sugerir» y al final juzgo con un criterio, por ejemplo la facilidad de desarmar. Los envases que reutilice deben estar limpios, sin bordes filosos y sin restos de productos de limpieza.",
    ],
    [("sustentable", "que se obtiene, usa y descarta con poco daño al ambiente"), ("reutilizado", "material que se usa de nuevo en otra función"), ("ciclo de vida", "origen, uso y descarte de un material"), ("volumen", "lo que ocupa un objeto en el espacio"), ("textura", "cómo se ve o se siente una superficie")],
    [
        w("Ficha de una banca de ejemplo", "Obra de ejemplo «Banca Tres Cajas»: tres cajas de cartón usadas, de distinto tamaño, apiladas y unidas con cordel; pintadas con témpera; 45 cm de alto; ubicada en un patio escolar para que la usen estudiantes; se puede desarmar y el cartón va a reciclaje. Ubica origen, uso y descarte.", ["Origen: cajas de cartón usadas.", "Uso: banca del patio para sentarse.", "Descarte: se desarma y el cartón se recicla."], "Origen: cartón usado; uso: banca del patio; descarte: desarme y reciclaje"),
        w("Escultura o diseño", "La «Banca Tres Cajas» sirve para sentarse. ¿Es más escultura o más diseño? Justifica con un rasgo.", ["Dato: tiene volumen, como una escultura.", "Dato: resuelve una necesidad, sentarse.", "Conclusión: es más diseño, porque tiene una función."], "Diseño, porque resuelve la necesidad de sentarse"),
    ],
    [
        m("Pensar que un material es sustentable solo porque es reciclable.", "El origen, la duración y el descarte cuentan juntos; reciclable no basta.", "Revisa las tres etapas del ciclo de vida antes de juzgar."),
        m("Mezclar la descripción con la opinión: «la banca es horrible».", "Una opinión no se puede comprobar mirando la obra.", "Escribe rasgos como «las cajas están unidas con cordel» y luego un juicio con criterio."),
    ],
    [
        ex("En Artes Visuales, ¿qué es un material reutilizado? A. Uno que se usa de nuevo en otra función B. Uno que se compra nuevo para botarlo después.", "A", "Reutilizar es darle otro uso a lo que ya existe."),
        ex("En la ficha de la «Banca Tres Cajas», ¿cuál es el origen del material? A. Cajas de cartón usadas B. Cajas de cartón nuevas compradas para esta obra.", "A", "La ficha dice que son cajas usadas."),
        ex("La «Banca Tres Cajas» sirve para sentarse. ¿Se acerca más a escultura pura o a diseño?", "Diseño", "Resuelve una necesidad, no solo expresa una idea."),
    ],
    [
        ex("¿Cómo se llama la etapa del ciclo de vida que describe qué pasa cuando el material ya no sirve? A. Descarte B. Origen C. Uso.", "A", "El descarte es el final del ciclo."),
        ex("Datos de una obra de ejemplo: 1) el cartón viene de cajas usadas, 2) estudiantes la usan para sentarse, 3) al final se desarma y se recicla, 4) mide 45 cm de alto. ¿Cuál NO es una etapa del ciclo de vida?", "El 4", "La altura es una medida; las otras tres son origen, uso y descarte."),
        ex("Verdadero o falso: un material es sustentable solo con que se pueda reciclar, aunque se compre nuevo para una sola obra.", "Falso", "La sustentabilidad se juzga con origen, uso y descarte juntos."),
    ],
    [
        ex("Desafío: un asiento para el patio. ¿Qué material tiene mejor origen? A. Cajas de cartón usadas B. Plástico espumado nuevo comprado para esta obra.", "A", "Reutilizar evita fabricar material nuevo."),
        ex("Una botella plástica se lava y se usa de florero. ¿Qué es esa botella en la obra? A. Un material reutilizado B. Un material reciclado.", "A", "Se usa de nuevo en otra función sin procesarla otra vez; reciclar sería volver a procesarla como materia prima."),
        ex("¿Cuál frase es una interpretación? A. «Las cajas apiladas podrían sugerir una ciudad pequeña» B. «Hay tres cajas apiladas».", "A", "Propone un significado con «podría sugerir»; la otra solo describe."),
    ],
    [
        ex("Dos propuestas de asiento con las mismas cajas. X: pegadas con adhesivo permanente. Y: unidas con cordel y ranuras que se desarman. ¿Cuál facilita mejor el descarte?", "Y", "Se puede separar cada pieza y reciclarla por separado; el adhesivo las deja pegadas."),
        ex("Frase: «Es sustentable porque se desarma y cada parte puede volver a usarse». ¿Cuál es el criterio? A. La facilidad de desarmar y reusar B. El color de la témpera.", "A", "La razón del juicio es el desarme, que se puede comprobar."),
    ],
    [
        ex("Antes de usar un envase plástico de tu casa en una escultura, ¿qué revisas? A. Que esté limpio, sin bordes filosos y sin restos de productos de limpieza B. Que tenga la etiqueta puesta.", "A", "Así evitas cortes y contacto con sustancias; la etiqueta no importa."),
        ex("Dos fichas de ejemplo para un portalápices. P: tapas plásticas lavadas unidas con cordel. Q: arcilla nueva con adhesivo que no se separa. El criterio es «poco material nuevo y fácil de desarmar». ¿Cuál cumple mejor?", "P", "Usa tapas ya existentes y las une de forma reversible."),
    ],
    ex("En tu casa quieres hacer un organizador de escritorio con cajas que ya no usas. ¿Qué parte de su ciclo de vida estás mejorando al hacerlo? A. El origen, porque no compras material nuevo B. La altura del organizador.", "A", "Usar lo que ya existe reduce el material nuevo."),
    [
        ex("¿Cuáles son las tres etapas del ciclo de vida de un material?", "Origen, uso y descarte", "Describen de dónde viene, cómo se usa y qué pasa después."),
        ex("Verdadero o falso: «me gusta» es un criterio para valorar una escultura.", "Falso", "Un criterio es una razón comprobable, como la facilidad de desarmar."),
        ex("¿Qué cualidad hace que una obra con función sea diseño y no solo escultura?", "Resuelve una necesidad", "El diseño une forma y función."),
    ],
    task(
        "Elige UNA ficha de ejemplo. A) Escultura «Torre de Tapas»: 40 tapas plásticas lavadas unidas con cordel, 50 cm, en una biblioteca escolar. B) Diseño «Cesta de Diario»: tiras de papel de diario enrolladas y tejidas, para guardar útiles, hecha en una sala. C) Diseño «Pata de Cajas»: soporte para libros hecho con dos cajas de cartón encajadas sin pegamento. Escribe una ficha con origen, uso y descarte, dos rasgos de lenguaje visual y un propósito; agrega una interpretación con «podría» y un juicio apoyado en un criterio.",
        "Elegí la C. Origen: cajas de cartón usadas. Uso: soporte para libros. Descarte: se desarman sin pegamento y se reciclan. Rasgos: forma de cubo, color café del cartón. Propósito: ordenar libros sin comprar material nuevo. Interpretación: las cajas encajadas podrían sugerir que lo simple también sirve. Juicio: es sustentable porque se desarma sin dañar el cartón.",
        ["escribe origen, uso y descarte", "separa descripción, interpretación y juicio", "apoya el juicio en un criterio comprobable", "usa solo materiales limpios y seguros"],
        ["ficha con las tres etapas del ciclo de vida", "interpretación con «podría» y juicio con criterio"],
        ["confundir reciclable con sustentable", "escribir solo opiniones"],
        "Pregunta qué rasgo comprobable sostiene su juicio y en qué etapa del ciclo de vida se apoya.",
    ),
    "Mira un objeto de tu casa y di en voz alta de qué material es, cuánto podría durar y qué pasará con él al final.",
    "Explica con tres frases por qué un objeto que se desarma es más fácil de reciclar que uno pegado.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Hojas, cartulina, papel de diario, una caja de cartón y cuatro o cinco libros pequeños. Los datos de las pruebas de ejemplo están escritos en la clase. No necesitas cortar nada con cuchillo.",
    "Aprenderé a explorar materiales sustentables y a compararlos por sus propiedades y por sus uniones. Sirve para elegir con razones el material de una escultura o de un objeto de diseño.",
    ["Sé que un material sustentable se juzga por su ciclo de vida.", "Sé que una escultura tiene volumen y un diseño tiene función."],
    [
        "Explorar un material es probar cómo se comporta. Tres propiedades útiles son la resistencia (cuánto peso aguanta sin doblarse), la flexibilidad (cuánto se dobla sin romperse) y el peso. El cartón corrugado (una capa ondulada entre dos capas lisas) resiste más que la cartulina; el papel de diario enrollado apretado resiste más que hojas sueltas; la tela flexible sirve para amarrar. Anoto cada prueba en una tabla para comparar.",
        "Una unión es la forma en que dos piezas quedan juntas. Una unión reversible se puede deshacer sin dañar las piezas: cordel, encaje con ranuras, pestañas dobladas, pinzas de ropa. Una unión permanente, como el adhesivo, deja las piezas pegadas. Para un proyecto sustentable conviene preferir uniones reversibles, porque después cada material puede reutilizarse o reciclarse por separado.",
        "Un referente es una obra que me inspira para decidir. Lo observo, tomo una idea (por ejemplo, encajar piezas sin pegamento) y la transformo con mis propias decisiones. Copiar el referente no es hacer un proyecto propio. En esta clase los referentes son fichas de ejemplo inventadas y rotuladas «de ejemplo», porque lo importante es el análisis.",
    ],
    [("resistencia", "cuánto peso aguanta un material sin doblarse"), ("flexibilidad", "capacidad de doblarse sin romperse"), ("unión reversible", "unión que se deshace sin dañar las piezas"), ("unión permanente", "unión que deja las piezas pegadas"), ("referente", "obra que inspira, pero no se copia")],
    [
        w("Leer una tabla de pruebas", "Prueba de ejemplo: un puente de 20 cm hecho con cada material, cargado con libros pequeños de 400 g cada uno. Cartulina: aguanta 2 libros. Cartón corrugado: aguanta 6 libros. Papel de diario enrollado: aguanta 4 libros. ¿Cuál resiste más y cuántos libros más que la cartulina?", ["Comparo: 6 libros, 4 libros y 2 libros.", "El mayor es el cartón corrugado, con 6.", "Resto: 6 − 2 = 4 libros más que la cartulina."], "Cartón corrugado; aguanta 4 libros más que la cartulina"),
        w("Elegir unión", "Quieres que una escultura de cartón se arme en clase y se desarme al final de la exposición. ¿Qué unión eliges: cordel con ranuras o adhesivo?", ["Criterio: que se pueda desarmar sin dañar las piezas.", "El cordel y las ranuras se deshacen; el adhesivo no.", "Elijo cordel con ranuras."], "Cordel con ranuras, porque es reversible"),
    ],
    [
        m("Elegir el material solo por el color o la apariencia.", "Las propiedades como la resistencia no se ven a simple vista.", "Haz una prueba corta y anota el resultado en una tabla."),
        m("Copiar la forma completa del referente y llamarlo creación propia.", "El proyecto debe mostrar decisiones del propio autor.", "Toma una idea del referente y transfórmala con otro material, tamaño o función."),
    ],
    [
        ex("¿Qué mide la resistencia de un material? A. Cuánto peso aguanta sin doblarse B. Cuán brillante es su color.", "A", "La resistencia se prueba con carga."),
        ex("¿Cuál es una unión reversible? A. Encajar dos cartones con ranuras B. Pegar dos cartones con adhesivo permanente.", "A", "Las ranuras se deshacen sin dañar los cartones."),
        ex("En la prueba de ejemplo, ¿qué material aguantó 4 libros? A. Papel de diario enrollado B. Cartulina.", "A", "La tabla dice que el diario enrollado aguantó 4 libros."),
    ],
    [
        ex("Cuando se toma una idea de un referente y se cambia el material, el tamaño y la función, ¿se está copiando o transformando?", "Transformando", "Hay decisiones propias, que es lo que distingue un proyecto propio."),
        ex("¿Por qué conviene preferir uniones reversibles en una obra sustentable? A. Porque cada pieza se puede reutilizar o reciclar por separado B. Porque se ven más brillantes.", "A", "Al desarmar sin daño, el material sigue sirviendo."),
        ex("Una tira de tela se dobla mucho sin romperse. ¿Qué propiedad tiene alta? A. Flexibilidad B. Resistencia al peso.", "A", "Doblarse sin romperse es flexibilidad."),
    ],
    [
        arith("Un puente de ejemplo con cartón corrugado aguanta 6 libros de 400 g cada uno. ¿Cuántos gramos aguanta en total?", "6 * 400", "Se multiplica el número de libros por el peso de cada uno.", " g"),
        ex("Tabla de ejemplo: lámina de cartón corrugado, aguanta 6 libros; lámina doblada en acordeón, aguanta 9 libros. Para una repisa de libros, ¿qué lámina conviene? A. La doblada en acordeón B. La sin doblar.", "A", "Aguanta más peso con el mismo material."),
        ex("Quieres una escultura que se pueda guardar en una mochila. ¿Qué elección responde a eso? A. Piezas planas que se encajan y se desarman B. Una sola pieza grande pegada.", "A", "Las piezas planas se transportan y se arman donde se necesitan."),
    ],
    [
        ex("Un compañero dice: «El cartón resiste porque es de color café». ¿Qué respuesta corrige mejor su razón? A. Resiste por su estructura corrugada, y eso se comprueba con una prueba de carga B. Resiste porque es más grueso, y no hace falta probarlo.", "A", "La resistencia se debe a la estructura y se verifica con una prueba."),
        ex("Dos pruebas de ejemplo con el mismo puente: en la primera usas 3 libros y en la segunda 3 libros más una caja de 600 g. ¿Es una comparación justa con la de otro material que usó 3 libros? Responde sí o no.", "No", "Para comparar se debe usar la misma carga en cada material."),
    ],
    [
        ex("Un grupo quiere reutilizar botellas plásticas limpias como ladrillos de un muro bajo. ¿Qué prueba segura harían primero? A. Apilar tres botellas y empujar suavemente con la mano B. Apoyar todo el peso del cuerpo sobre la pila.", "A", "Se prueba la estabilidad sin riesgo de caída; subirse es peligroso."),
        ex("Un referente de ejemplo es una silla de cartón con uniones de pestañas. Tu propuesta es un velador con otro tamaño, otra función y las mismas pestañas. ¿Qué decisión propia aparece? A. La función y el tamaño B. La unión de pestañas.", "A", "Cambian la función y el tamaño; solo se toma la idea de la unión."),
    ],
    ex("Ordenas tu closet y reutilizas cajas de zapatos como cajones. ¿Qué propiedad deberías probar primero? A. Resistencia al peso de lo que guardarás B. El color de la tapa.", "A", "Los cajones deben aguantar el peso del contenido."),
    [
        ex("¿Qué diferencia hay entre una unión reversible y una permanente?", "La reversible se deshace sin dañar las piezas", "Esa es la propiedad que permite reutilizar o reciclar."),
        ex("Verdadero o falso: para comparar dos materiales conviene usar la misma carga en las pruebas.", "Verdadero", "Así la comparación es justa."),
        ex("¿Se puede copiar un referente y decir que el proyecto es propio?", "No", "Un proyecto propio muestra decisiones transformadas del autor."),
    ],
    task(
        "Completa una tabla de exploración. Pruebas de ejemplo con un puente de 20 cm cargado con libros de 400 g: cartulina aguanta 2 libros; papel de diario enrollado aguanta 4; cartón corrugado aguanta 6. Referentes de ejemplo: A) «Silla de Pestañas», cartón con pestañas dobladas; B) «Muro de Botellas», botellas plásticas lavadas unidas con cordel. Elige un material y un referente. Escribe qué propiedad mide cada prueba, qué unión usarías y qué idea tomas del referente para transformarla.",
        "Elegí cartón corrugado y la «Silla de Pestañas». Resistencia: aguanta 6 libros de 400 g, es decir, 2.400 g. Unión: pestañas dobladas, reversibles. Idea tomada: unir sin pegamento. Transformación: haré un velador pequeño, no una silla, y cambiaré las pestañas por ranuras de otra forma.",
        ["identifica la propiedad que mide cada prueba", "elige una unión reversible y la justifica", "toma una idea del referente sin copiarlo", "usa la misma carga al comparar"],
        ["tabla con material, propiedad y resultado", "idea del referente y su transformación"],
        ["elegir por apariencia", "copiar el referente"],
        "Pregunta qué decisión es propia y cómo se demuestra que la comparación fue justa.",
    ),
    "Prueba con un papel de diario enrollado y otro sin enrollar cuál soporta más libros pequeños y anota la diferencia.",
    "Describe en tres frases una unión reversible que podrías usar en un objeto y por qué sirve para reciclar.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Hojas, cartón delgado, regla, lápiz y cordel. Si quieres probar, usa piezas de cartón de tamaño pequeño. Los datos de las pruebas están escritos en la clase.",
    "Aprenderé a probar decisiones de forma, base y escala en una escultura o un objeto de diseño. Sirve para que mi propuesta se sostenga y se vea como la imagino.",
    ["Sé comparar materiales por resistencia y flexibilidad.", "Sé que una unión reversible permite desarmar."],
    [
        "Probar una decisión visual es comparar dos versiones y elegir según una intención. Una escultura de pie debe ser estable: una base ancha y las piezas más pesadas abajo la mantienen firme. Una base angosta con peso arriba puede caerse. Equilibrio es la relación de pesos y formas que hace que una obra se vea y se sostenga sin caer. Cambio una sola cosa a la vez para saber qué produjo el efecto.",
        "La proporción es la relación de tamaño entre las partes. Una maqueta es un modelo pequeño de la obra final. La escala indica cuánto se reduce: escala 1:5 significa que 1 cm de la maqueta representa 5 cm de la obra real. Si la obra real mide 90 cm de alto, la maqueta mide 90 ÷ 5 = 18 cm. Probar en maqueta ahorra material.",
        "Anoto cada prueba con una frase corta: qué cambié, qué ocurrió y qué decido. Por seguridad pruebo la estabilidad con un empujón suave del dedo, nunca me subo ni me apoyo en la pieza. Una prueba fallida es información útil: me dice qué ajustar antes de armar la versión final.",
    ],
    [("estable", "que se mantiene firme sin caer"), ("equilibrio", "relación de pesos y formas que hace que una obra se sostenga"), ("proporción", "relación de tamaño entre las partes"), ("maqueta", "modelo pequeño de una obra"), ("escala", "cuánto se reduce un objeto en el modelo")],
    [
        w("Calcular una maqueta", "Una escultura real medirá 120 cm de alto. Harás una maqueta a escala 1:5. ¿Cuántos centímetros medirá la maqueta?", ["Escala 1:5 significa que 5 cm reales se dibujan como 1 cm.", "Divido 120 entre 5.", "120 ÷ 5 = 24 cm."], "24 cm"),
        w("Decidir la base", "Prueba de ejemplo con una torre de cajas: con base de 10 cm se cae al primer empujón; con base de 20 cm aguanta cinco empujones suaves. ¿Qué decisión tomas?", ["Dato: la base de 20 cm resiste más empujones.", "Criterio: estabilidad.", "Decisión: usar la base de 20 cm."], "Usar la base de 20 cm"),
    ],
    [
        m("Cambiar tres cosas a la vez entre una prueba y otra.", "Así no se sabe cuál cambio produjo el resultado.", "Cambia una sola cosa por prueba y anota el efecto."),
        m("Descartar una prueba que falló sin anotar nada.", "La falla explica qué ajustar antes de la versión final.", "Escribe qué pasó y qué decides cambiar."),
    ],
    [
        ex("¿Qué base da más estabilidad a una escultura de pie? A. Una base ancha B. Una base muy angosta.", "A", "Una base ancha reparte el peso y evita que se caiga."),
        ex("Una maqueta es… A. Un modelo pequeño de la obra B. La obra final terminada.", "A", "Sirve para probar antes de gastar material."),
        ex("¿Cuántas cosas conviene cambiar entre una prueba y la siguiente?", "Una", "Así se sabe qué produjo el efecto."),
    ],
    [
        ex("La escala 1:5 significa que… A. 1 cm de la maqueta representa 5 cm de la obra real B. 5 cm de la maqueta representan 1 cm real.", "A", "La maqueta es cinco veces más pequeña."),
        ex("En una torre de ejemplo, ¿dónde conviene poner la pieza más pesada para ganar estabilidad? A. Abajo B. Arriba.", "A", "El peso abajo baja el centro de la obra y la hace firme."),
        ex("¿Qué es la proporción en una escultura? A. La relación de tamaño entre sus partes B. El número de colores.", "A", "Compara tamaños de las partes."),
    ],
    [
        arith("Una obra real mide 150 cm de alto. Haces una maqueta a escala 1:5. ¿Cuántos centímetros mide la maqueta?", "150 // 5", "Se divide el alto real entre cinco.", " cm"),
        ex("Un diseño de ejemplo tiene 60 cm de alto y una base de 12 cm. Otra versión tiene 60 cm de alto y base de 24 cm. Para que no se caiga, ¿cuál conviene? A. La de base de 24 cm B. La de base de 12 cm.", "A", "La base más ancha da más estabilidad."),
        ex("La maqueta a escala 1:5 de una escultura con base angosta y cabeza grande se tambalea con un empujón suave del dedo. ¿Qué es más probable en la obra real? A. Que también sea inestable, porque la escala conserva las proporciones B. Que se estabilice sola por ser más grande.", "A", "La escala conserva las proporciones, así que el problema de forma se repite; conviene corregir la maqueta primero."),
    ],
    [
        ex("En una prueba de ejemplo, un grupo cambió a la vez la base, el material y la altura, y la torre mejoró. ¿Puede decir qué cambio ayudó? Responde sí o no.", "No", "Al cambiar tres cosas no se sabe cuál produjo la mejora."),
        ex("Una maqueta cae al primer empujón con el peso arriba. ¿Qué ajuste razonable propones? A. Pasar el peso hacia abajo y ensanchar la base B. Agregar más piezas pesadas arriba.", "A", "Un centro bajo y una base ancha dan estabilidad."),
    ],
    [
        ex("Una compañera quiere probar la estabilidad subiéndose a la escultura de cajas. ¿Qué consejo seguro le das? A. Probar con un empujón suave del dedo en la maqueta B. Subirse con cuidado.", "A", "La prueba debe ser segura y sin riesgo de caída."),
        ex("Tu maqueta es de papel liviano, pero la obra real será de cajas más pesadas. ¿Qué limitación tiene la prueba de estabilidad en la maqueta? A. El peso del material real cambia el resultado, así que hay que repetir la prueba suave en la obra B. Ninguna, porque la escala lo resuelve todo.", "A", "El peso distinto puede cambiar la estabilidad; la maqueta orienta, pero no reemplaza la prueba de la obra."),
    ],
    ex("Para tu pieza de decoración del hogar, haces una maqueta de 10 cm a escala 1:5 y ves que se tambalea. ¿Qué haces con esa información? A. Ajustas la base antes de construir la versión real B. Construyes la versión real igual.", "A", "La maqueta existe para detectar fallas a bajo costo."),
    [
        ex("¿Qué ventaja tiene probar en maqueta antes de la obra final?", "Ahorra material y permite corregir antes", "Detecta fallas de estabilidad con poco gasto."),
        ex("Verdadero o falso: el peso arriba y una base angosta favorecen la estabilidad.", "Falso", "Eso aumenta el riesgo de caída."),
        ex("Con escala 1:5, ¿una pieza real de 40 cm cuántos centímetros mide en la maqueta?", "8 cm", "40 ÷ 5 = 8.", calc="40 // 5"),
    ],
    task(
        "Planifica dos pruebas para un objeto de diseño a elegir: A) una repisa de cartón para libros de 120 cm de alto; B) una escultura de cajas de 90 cm; C) un soporte de plantas de 60 cm. Calcula la altura de la maqueta a escala 1:5, escribe qué UNA cosa cambias entre la prueba 1 y la 2 (por ejemplo, el ancho de la base) y qué criterio usas para elegir. Prueba solo con empujones suaves.",
        "Elegí C, soporte de plantas de 60 cm. Maqueta: 60 ÷ 5 = 12 cm. Prueba 1: base de 6 cm. Prueba 2: base de 10 cm; cambié solo el ancho de la base. Criterio: estabilidad con tres empujones suaves del dedo. Resultado: la base de 10 cm no se cayó, así que la elijo.",
        ["calcula la altura de la maqueta", "cambia una sola cosa entre pruebas", "nombra un criterio de elección", "propone una prueba segura"],
        ["cálculo de escala", "dos pruebas anotadas con su resultado"],
        ["cambiar varias cosas a la vez", "no anotar los resultados"],
        "Pregunta qué cambió entre una prueba y otra y cómo se sabe cuál fue mejor.",
    ),
    "Arma con tres cajas una torre baja y otra alta y compara con un empujón suave del dedo cuál se mantiene más firme.",
    "Redacta tres frases que expliquen por qué una base ancha da más estabilidad.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Hojas, lápiz, regla y, si quieres, cartones o tapas limpias. Los desafíos y las listas están escritos en la clase. No se usan herramientas cortantes ni fuego.",
    "Aprenderé a desarrollar una propuesta propia de escultura o diseño desde un desafío creativo, con boceto, lista de materiales, ficha de ciclo de vida y pasos de armado. Sirve para planificar un proyecto antes de construirlo.",
    ["Sé comparar materiales y uniones.", "Sé probar la estabilidad en una maqueta con una escala."],
    [
        "Un desafío creativo es un problema abierto que puede tener muchas soluciones, por ejemplo «un objeto para ordenar cosas en una sala sin comprar material nuevo». Para responderlo desarrollo una propuesta propia: primero un boceto (dibujo rápido de la idea), después una lista de materiales con sus cantidades y luego los pasos de armado en orden.",
        "La propuesta incluye una ficha de ciclo de vida: de dónde sale cada material (origen), cuánto tiempo y cómo se usará y qué se hará con él al terminar (descarte). Incluye también una nota de seguridad: materiales limpios, sin bordes filosos, tamaño que no cause tropiezos y ningún trabajo con fuego, cuchillos ni productos químicos. Las tareas con herramientas especiales las conduce el docente.",
        "Mi propuesta debe mostrar autoría, es decir, que las decisiones son mías. Puedo inspirarme en un referente, pero cambio algo importante: función, tamaño, material o forma. Escribo por qué elegí cada decisión. Si algo no funciona en la maqueta, lo ajusto y dejo constancia del cambio, porque ese registro es parte de la evidencia del proceso.",
    ],
    [("desafío creativo", "problema abierto que puede resolverse de muchas maneras"), ("boceto", "dibujo rápido para probar una idea"), ("ficha de ciclo de vida", "registro de origen, uso y descarte de los materiales"), ("autoría", "decisiones que hace el propio autor"), ("evidencia del proceso", "bocetos, pruebas y cambios que muestran cómo se llegó a la obra")],
    [
        w("Armar la lista de materiales", "Desafío de ejemplo: «un portalápices para una sala». Idea: 10 tapas plásticas lavadas, 2 tubos de cartón de papel higiénico y 1 m de cordel, unidos sin adhesivo. ¿Cuántas piezas de material reutilizado necesitas en total, sin contar el cordel?", ["Tapas: 10 piezas.", "Tubos de cartón: 2 piezas.", "Suma: 10 + 2 = 12 piezas."], "12 piezas reutilizadas"),
        w("Escribir la ficha de ciclo de vida", "Para el mismo portalápices, completa la ficha con una frase por etapa.", ["Origen: tapas y tubos que ya había en casa.", "Uso: guardar lápices en una sala durante el año.", "Descarte: se desatan, las tapas y el cartón se reciclan por separado."], "Origen: material de casa; uso: portalápices; descarte: desarme y reciclaje separado"),
    ],
    [
        m("Escribir solo «haré un portalápices» sin lista, pasos ni ficha.", "Sin planificación no se puede construir ni evaluar la propuesta.", "Escribe el desafío, el boceto, la lista de materiales, los pasos y la ficha de ciclo de vida."),
        m("Usar herramientas cortantes o fuego porque el referente las usaba.", "Esos trabajos no son seguros en casa ni sin supervisión.", "Elige uniones reversibles y materiales que no necesiten herramientas peligrosas."),
    ],
    [
        ex("¿Qué es un boceto? A. Un dibujo rápido de la idea B. La obra terminada.", "A", "Sirve para probar la idea antes de construir."),
        ex("¿Qué incluye una ficha de ciclo de vida? A. Origen, uso y descarte B. Solo el color.", "A", "Esas son las tres etapas del ciclo."),
        ex("¿Qué es un desafío creativo? A. Un problema abierto con varias soluciones posibles B. Una pregunta con una sola respuesta correcta.", "A", "Permite varias soluciones propias."),
    ],
    [
        ex("Orden correcto de la planificación: 1) pasos de armado, 2) boceto, 3) lista de materiales. ¿Cuál es un orden lógico?", "2, 3, 1", "Primero se imagina, luego se listan materiales y después se ordenan los pasos."),
        ex("Una propuesta usa pegamento permanente en todas sus uniones. ¿Qué etapa del ciclo de vida complica? A. El descarte B. El origen.", "A", "Pegadas, las piezas no se separan para reciclar."),
        ex("¿Qué muestra la autoría en una propuesta? A. Decisiones propias explicadas B. Una copia exacta de un referente.", "A", "La autoría son las decisiones del autor."),
    ],
    [
        ex("Lista de materiales de ejemplo: 6 tapas de casa, 4 tubos de casa y cinta adhesiva comprada nueva para pegarlo todo. ¿Qué ítem empeora el ciclo de vida? A. La cinta adhesiva nueva, que agrega material nuevo y una unión permanente B. Los tubos de casa, que ya existían.", "A", "Lo nuevo y permanente complica el origen y el descarte; lo que ya existía no."),
        arith("Para unir tu obra compras un ovillo de cordel de $1.500 y un frasco de témpera de $2.000. Precios de ejemplo. ¿Cuánto gastas en total?", "1500 + 2000", "Se suman ambos precios.", " pesos"),
        ex("Desafío: «una escultura que invite a reciclar». ¿Qué boceto responde mejor? A. Tres cajas apiladas con el dibujo de una flecha circular pintada B. Tres botellas nuevas compradas y pegadas con adhesivo permanente.", "A", "La flecha circular es un símbolo conocido de reciclaje y las cajas reutilizan material; la otra opción usa material nuevo y unión permanente."),
    ],
    [
        ex("Un compañero propone usar un encendedor para sellar los bordes del plástico. ¿Qué respondes? A. No, es peligroso: se usa otra unión sin fuego B. Sí, si lo hace rápido.", "A", "El fuego queda fuera de la experiencia por seguridad."),
        ex("Un grupo cambió el tamaño y la función del referente, pero conserva la unión de pestañas. ¿Qué parte es propia? A. El tamaño y la función B. La unión de pestañas.", "A", "La unión viene del referente; lo transformado es lo propio."),
    ],
    [
        ex("Quieres dejar de comprar bolsas para tu ropa de gimnasia. Tu desafío: un organizador con material que ya tienes. ¿Qué parte de la ficha debes revisar para que sea seguro? A. Que los materiales estén limpios y sin bordes filosos B. Que el organizador tenga muchas piezas.", "A", "Es la condición de seguridad de la propuesta."),
        ex("Dos listas de ejemplo para un organizador. L1: 8 tapas y 3 tubos de cartón, todo de casa. L2: 8 tapas de casa, 3 tubos comprados nuevos y un frasco de adhesivo. El criterio es «lo menos material nuevo posible». ¿Cuál cumple mejor?", "L1", "No compra nada nuevo; la otra sí."),
    ],
    ex("Ficha de ejemplo de un portalápices. Origen: tapas de casa. Uso: guardar lápices en la sala. Descarte: «pegadas con adhesivo, se botan». ¿Qué cambio mejora la ficha? A. Unir con cordel para poder separar y reciclar las piezas B. Escribir «se botan» con otras palabras.", "A", "Cambiar la unión mejora el descarte; reescribir la frase no cambia lo que pasa con el material."),
    [
        ex("Nombra las partes de una propuesta propia.", "Boceto, lista de materiales, pasos y ficha de ciclo de vida", "Son las partes que planifican el proyecto."),
        ex("Verdadero o falso: puedes usar fuego si el referente lo usaba.", "Falso", "Se evita por seguridad."),
        ex("¿Qué debe cambiar en tu propuesta respecto del referente?", "Una decisión propia", "Así hay autoría."),
    ],
    task(
        "Elige UN desafío: A) un portalápices para tu sala; B) un soporte para guardar libros; C) una escultura que invite a reciclar. Escribe el boceto en palabras, la lista de materiales con cantidades, los pasos de armado en orden, la ficha de ciclo de vida y una nota de seguridad. Indica qué decisión tuya cambia respecto de cualquier referente y cuántas piezas son reutilizadas.",
        "Elegí A. Boceto: un cilindro bajo de 10 tapas y 2 tubos de cartón con cordel. Materiales: 10 tapas, 2 tubos, 1 m de cordel (12 piezas reutilizadas). Pasos: 1) lavar tapas, 2) apilar, 3) amarrar. Ciclo de vida: origen en casa; uso en la sala; descarte con desarme. Seguridad: materiales limpios y sin bordes filosos. Decisión propia: cambié la función del referente.",
        ["tiene desafío, boceto, materiales, pasos y ficha", "usa uniones reversibles", "explica una decisión propia", "incluye una nota de seguridad"],
        ["lista de materiales con cantidades", "ficha de ciclo de vida y pasos ordenados"],
        ["propuesta sin pasos", "olvidar la nota de seguridad"],
        "Pregunta qué decisión es propia y qué etapa del ciclo de vida se vuelve más fácil con esa decisión.",
    ),
    "Dibuja un boceto rápido de un objeto que sirva para ordenar tu mochila y marca tres materiales de tu casa que podrías usar.",
    "Escribe una ficha de ciclo de vida de tres frases para un objeto de cartón.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Hojas, lápiz, tu propuesta de la clase anterior o una de las fichas de ejemplo de esta clase. Los criterios y puntajes están escritos aquí.",
    "Aprenderé a contrastar una obra o propuesta de escultura o diseño con criterios de sustentabilidad, estabilidad, relación con el desafío y autoría. Sirve para decidir con evidencia qué conservar y qué mejorar.",
    ["Sé armar una propuesta con boceto, materiales y ficha de ciclo de vida.", "Sé probar la estabilidad en una maqueta."],
    [
        "Contrastar es comparar una obra con criterios claros y con evidencia. En esta clase usamos cuatro criterios, cada uno con 0 a 3 puntos: sustentabilidad del material (origen, uso y descarte), estabilidad (la obra se sostiene en las pruebas), relación con el desafío (responde a lo pedido) y autoría (muestra decisiones propias y no copia). El máximo es 12 puntos.",
        "La evidencia es lo que se puede mostrar: la ficha de ciclo de vida, las pruebas de maqueta, los bocetos con cambios y las fotos del proceso. Un puntaje sin evidencia no convence. Por ejemplo, para dar 3 en estabilidad necesito mostrar que la maqueta aguantó tres empujones suaves del dedo. Anoto cada puntaje con una frase de justificación.",
        "El resultado sirve para mejorar, no para etiquetar a una persona. Si un criterio saca poco puntaje, propongo un ajuste concreto para la próxima versión, como cambiar una unión permanente por cordel. Comparo mi trabajo con las pruebas, no con el de otras personas, y respeto la autoría de quien lo hizo. Los talleres con herramientas especiales quedan para el docente.",
    ],
    [("criterio", "razón con la que se juzga una obra"), ("evidencia", "prueba que se puede mostrar para respaldar un juicio"), ("sustentabilidad", "uso de materiales con poco daño al ambiente en todo su ciclo de vida"), ("autoría", "decisiones que pertenecen al propio autor"), ("ajuste", "cambio concreto para mejorar una versión")],
    [
        w("Aplicar la pauta", "Pauta de 4 criterios de 0 a 3 puntos. Obra de ejemplo «Portalápices de Tapas»: sustentabilidad 3 (todo es reutilizado y se desata), estabilidad 2 (aguantó dos de tres empujones), relación con el desafío 3, autoría 2 (cambió función pero conserva la unión del referente). ¿Cuál es el total?", ["Puntajes: 3, 2, 3 y 2.", "Sumo: 3 + 2 + 3 + 2.", "Total: 10 de 12."], "10 de 12 puntos"),
        w("Proponer un ajuste", "En el mismo portalápices, el criterio más bajo es estabilidad, con un puntaje de 2. ¿Qué ajuste concreto propones?", ["Causa probable: base angosta.", "Ajuste: ensanchar la base con más tapas abajo.", "Nueva prueba: tres empujones suaves."], "Ensanchar la base y repetir la prueba de empujones"),
    ],
    [
        m("Dar un puntaje alto sin mostrar evidencia.", "Sin evidencia el puntaje es solo una opinión.", "Junta una prueba, una ficha o un boceto para cada puntaje."),
        m("Usar la pauta para decir que una persona «es mala para el arte».", "Los criterios evalúan una obra, no a una persona.", "Habla de la obra y propone un ajuste concreto."),
    ],
    [
        ex("¿Qué evidencia respalda un 3 en estabilidad, según la clase? A. Que la maqueta aguantó tres empujones suaves del dedo B. Que el autor dice que la armó con mucho cuidado.", "A", "La evidencia se puede mostrar y repetir; una declaración del autor no."),
        ex("¿Qué criterio revisa el origen, el uso y el descarte de los materiales? A. Sustentabilidad B. Autoría.", "A", "Esas tres etapas forman el ciclo de vida del material."),
        ex("¿Qué es la evidencia en esta clase? A. Algo que se puede mostrar, como una prueba de maqueta B. Una sensación personal.", "A", "La evidencia respalda el juicio."),
    ],
    [
        ex("Una obra de ejemplo conserva la forma y las uniones de un referente sin cambiar nada. ¿Qué criterio saca el puntaje más bajo? A. Autoría B. Estabilidad.", "A", "Falta transformación y decisiones propias."),
        ex("Un grupo da 3 puntos en estabilidad, pero solo probó la maqueta una vez sin anotar nada. ¿Qué falta? A. Evidencia de las pruebas B. Color más vivo.", "A", "Sin registro de pruebas el puntaje no está respaldado."),
        ex("¿Para qué sirve el puntaje de cada criterio? A. Para decidir qué ajustar B. Para etiquetar a las personas.", "A", "La pauta orienta mejoras."),
    ],
    [
        arith("Obra de ejemplo: sustentabilidad 2, estabilidad 3, relación con el desafío 3 y autoría 1. ¿Cuántos puntos suma en total?", "2 + 3 + 3 + 1", "Se suman los cuatro puntajes.", " puntos"),
        ex("El desafío es «un objeto para ordenar cosas», pero la obra de ejemplo es una figura decorativa sin espacio para guardar nada. ¿Qué criterio saca el puntaje más bajo? A. Relación con el desafío B. Sustentabilidad C. Estabilidad.", "A", "No responde a lo pedido, aunque pueda ser estable o sustentable."),
        ex("Obra de ejemplo con bajo puntaje en sustentabilidad porque usa pegamento permanente. ¿Qué ajuste sube el criterio? A. Cambiarlo por cordel y encajes B. Pintarla de otro color.", "A", "Hace reversible la unión y mejora el descarte."),
    ],
    [
        ex("Dos obras de ejemplo suman 10 puntos cada una. X obtiene 3, 3, 3, 1; Y obtiene 3, 2, 2, 3. Si el desafío exige «autoría clara», ¿cuál conviene destacar? A. Y, porque tiene 3 en autoría B. X, porque tiene 3 en estabilidad.", "A", "Y tiene 3 en autoría y X solo 1."),
        ex("Una obra saca 2 en estabilidad. Un compañero dice «cámbiale el color». ¿Es un ajuste pertinente? Responde sí o no.", "No", "El color no cambia la estabilidad; hay que mejorar la base o el peso."),
    ],
    [
        ex("Quieres evaluar tu mueble de cartón para la sala de tu casa y solo tienes 5 minutos. ¿Qué criterio revisas con evidencia rápida? A. Estabilidad, con tres empujones suaves B. Cuánto te gusta el color.", "A", "Es comprobable en poco tiempo y con una prueba segura."),
        ex("Obra de ejemplo con 3 en sustentabilidad, 3 en estabilidad, 3 en desafío y 0 en autoría, porque es copia exacta de un referente. Total 9 de 12. ¿Qué conviene antes de celebrar el total? A. Rehacer una decisión propia para subir la autoría B. Pintar de otro color.", "A", "El total oculta que falta autoría, un criterio exigido."),
    ],
    ex("Un grupo evalúa su obra con 11 de 12 puntos y no quiere cambiar nada. ¿Qué es lo más razonable? A. Revisar el criterio que perdió un punto B. Dejar de revisar.", "A", "Siempre queda un ajuste posible."),
    [
        ex("Menciona los cuatro criterios de la pauta de esta clase.", "Sustentabilidad, estabilidad, relación con el desafío y autoría", "Son los cuatro criterios del contraste."),
        ex("Verdadero o falso: un puntaje sirve para decir que una persona no tiene talento.", "Falso", "La pauta evalúa la obra y orienta cómo mejorarla."),
        ex("¿Qué se hace con el criterio de menor puntaje?", "Se propone un ajuste concreto", "Así se mejora la próxima versión."),
    ],
    task(
        "Evalúa UNA obra con la pauta de cuatro criterios (0 a 3). A) «Banca Tres Cajas»: cajas usadas, cordel, se desarma, aguantó tres empujones, función de asiento, idea de apilado tomada de un referente. B) «Cesta de Diario»: tiras de papel de diario tejidas, se desarma, aguantó un solo empujón, sirve para guardar útiles, tejido creado por el autor. C) Tu propia propuesta de la clase anterior. Escribe un puntaje y una evidencia por criterio, suma el total y propone un ajuste para el criterio más bajo.",
        "Evalué la B. Sustentabilidad 3: papel de diario reutilizado y se desarma. Estabilidad 1: aguantó un empujón de tres. Relación con el desafío 3: guarda útiles. Autoría 3: el tejido es propio. Total: 10 de 12. Ajuste: ensanchar la base de la cesta con más tiras abajo y repetir la prueba.",
        ["asigna puntaje con evidencia a cada criterio", "suma bien el total", "propone un ajuste concreto", "evalúa la obra y no a la persona"],
        ["pauta con puntajes y evidencias", "ajuste para el criterio más bajo"],
        ["puntaje sin evidencia", "juzgar a la persona y no a la obra"],
        "Pregunta qué evidencia respalda cada puntaje y si el ajuste propuesto realmente cambia el criterio más bajo.",
    ),
    "Evalúa con tres empujones suaves de dedo un objeto de cartón de tu casa y anota si se mantiene firme.",
    "Escribe cuatro frases con un puntaje y su evidencia para una obra de ejemplo.",
)

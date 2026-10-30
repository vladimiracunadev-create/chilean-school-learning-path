"""Cuaderno del estudiante, 3.º básico Tecnología: OA 01 clases 4 a 6 y OA 02 (planificar la elaboración).

Las pantallas de software se describen con texto y son EJEMPLOS FICTICIOS: cada programa real se ve distinto.
Seguridad: tijeras de punta roma, sin cortadores, fuego ni vidrio; cortes difíciles los hace una persona adulta.
"""
from __future__ import annotations

from student_content_te3_a import reg
from student_lessons import arith

OA1, OA2 = "TE03 OA 01", "TE03 OA 02"

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz y regla. Los objetos a dibujar están descritos en el cuaderno.",
    use="Aprenderé a dibujar a mano alzada un diseño con vistas, partes con nombre, medidas y flechas de uso. Sirve para que otra persona lo entienda y lo construya.",
    prior=["Sé que un boceto es un dibujo rápido sin regla.", "Sé escribir criterios con medidas y unidades."],
    explain=[
        "Un dibujo técnico a mano alzada muestra el objeto para que otros lo construyan. Se dibuja sin regla, pero con cuidado. Conviene mostrar dos vistas: de frente, que es como lo ves de cara, y de lado, que es como lo ves desde un costado. Así se ven alto, ancho y fondo.",
        "Cada parte lleva un nombre escrito con una línea que apunta a ella. Cada medida lleva su unidad, por ejemplo 20 cm. La medida que escribes es la del objeto real, no la del tamaño del dibujo. Las flechas muestran cómo se mueve o se usa: una flecha hacia abajo indica que algo baja.",
        "Un buen dibujo responde tres preguntas: ¿qué partes tiene?, ¿cuánto mide?, ¿cómo se usa? Si falta una respuesta, agrégala. También puedes dibujar con un programa de dibujo, pero hoy practicamos el papel. Si dudas de una medida, pregunta o mide antes de escribirla.",
    ],
    vocab=[("vista de frente", "dibujo del objeto mirado de cara"), ("vista de lado", "dibujo del objeto mirado desde un costado"), ("rotular", "escribir el nombre de una parte junto a una línea que la señala"), ("medida", "número con unidad que dice cuánto mide algo"), ("flecha de uso", "flecha que muestra cómo se mueve o se usa")],
    worked=[
        ("Revisar un dibujo", "Un dibujo de un guardalápices muestra una caja y 3 lápices, sin nombres ni medidas. ¿Qué dos cosas agregas?", ["Faltan los nombres de las partes.", "Faltan las medidas con unidad.", "Agrego «caja», «lápiz» y «alto: 12 cm»."], "Nombres de las partes y medidas con unidad"),
        ("Elegir la vista", "Quieres mostrar cuán alta es una torre de cartón. ¿Qué vista sirve: de frente o desde arriba?", ["El alto se ve mirando de cara.", "Desde arriba no se ve el alto."], "De frente"),
    ],
    mistakes=[
        ("Escribir 5 cm porque el dibujo mide 5 cm, aunque el objeto mide 20 cm.", "La medida debe ser la del objeto real.", "Escribe la medida real: 20 cm."),
        ("Dibujar sin nombrar ninguna parte.", "Otra persona no sabe qué es cada pieza.", "Rotula cada parte con una línea."),
    ],
    R=[
        ("¿La vista de frente muestra el objeto de cara o desde un costado?", "De cara", "Así se ve de frente."),
        ("Escribir «base» junto a una línea que señala una parte, ¿es rotular o medir?", "Rotular", "Se pone el nombre a la parte."),
        ("¿Cuál lleva unidad: «20» o «20 cm»?", "20 cm", "La unidad dice en qué se midió."),
    ],
    C=[
        ("Un objeto real mide 15 cm y el dibujo mide 5 cm. ¿Qué número escribes en la medida?", "15 cm", "Se escribe la medida del objeto real."),
        ("¿Qué muestra una flecha de uso en el dibujo?", "Cómo se mueve o se usa", "Indica el movimiento o la acción."),
        ("¿Qué dos vistas conviene dibujar para ver alto, ancho y fondo?", "De frente y de lado", "Juntas muestran las tres medidas."),
    ],
    A=[
        ("Dibujas una caja con tapa. Escribe tres partes con su nombre para rotular.", "Caja, tapa, borde (u otras partes de la caja)", "Son partes visibles de la caja."),
        ("Una torre de 12 fichas mide 6 cm de alto en la vida real. Escribe cómo rotulas el alto en el dibujo.", "Alto: 6 cm", "Lleva el nombre de la medida y la unidad."),
        ("Quieres mostrar que la tapa se abre hacia arriba. ¿Qué agregas al dibujo?", "Una flecha hacia arriba", "La flecha indica el movimiento."),
    ],
    Z=[
        ("Un compañero dice que su dibujo está listo porque es bonito, pero no tiene medidas. ¿Está listo para construir? Responde con una frase.", "No, porque faltan las medidas", "Sin medidas no se puede construir igual."),
        ("Dos dibujos de la misma caja: A solo vista de frente, B de frente y de lado. ¿Cuál muestra mejor cuánto fondo tiene?", "B", "La vista de lado muestra el fondo."),
    ],
    D=[
        ("Reto: una caja mide 10 cm de alto, 8 cm de ancho y 5 cm de fondo. Escribe las tres medidas rotuladas.", "Alto: 10 cm; ancho: 8 cm; fondo: 5 cm", "Cada medida lleva nombre y unidad."),
        arith("El alto de una torre de cartón es 9 cm. Si le agregas otro piso de 4 cm de alto, ¿cuánto mide en total?", "9+4", "Se suman los altos de los pisos.", " cm"),
    ],
    ctx=("Pablo dibuja a mano alzada un portalápices de cartón: una caja de 12 cm de alto con una base cuadrada de 8 cm de lado. Escribe qué rotulas, qué medidas anotas y una flecha de uso.", "Rotula caja y base; anota alto 12 cm y lado 8 cm; flecha: los lápices entran hacia abajo", "Incluye nombres, medidas con unidad y flecha."),
    sc=[
        ("¿La medida del dibujo es la del objeto real o la del dibujo?", "La del objeto real", "Otros construirán el objeto real."),
        ("¿Qué respondes con partes, medidas y flechas: cómo se usa o cuántos años tiene?", "Cómo se usa", "Muestran partes, tamaños y movimiento."),
        ("¿Se necesita regla para un dibujo a mano alzada?", "No", "Mano alzada es sin regla."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: guardalápices de cartón de 12 cm de alto. Objeto 2: bolsa con asa para 3 libros, con asa de 25 cm. Dibuja a mano alzada la vista de frente y la de lado, rotula tres partes, anota dos medidas con unidad y una flecha de uso.",
        "Objeto 1: dos vistas, rotula caja, base y borde; alto 12 cm, ancho 8 cm; flecha de entrada de los lápices.",
        ["dibuja dos vistas", "rotula tres partes", "anota dos medidas con unidad", "dibuja una flecha de uso"],
        ["dibujo con dos vistas, nombres, medidas y flecha"],
        ["medidas sin unidad", "partes sin nombre"],
        "Pregunta: «¿alguien podría construirlo solo con tu dibujo?». Si falta un dato, pídelo.",
    ),
    reinforce="Dibuja a mano alzada un vaso de tu casa desde dos vistas y escribe su alto aproximado.",
    extend="Dibuja un cajón de ropa mostrando con una flecha cómo se abre.",
)

# ------------------------------------------------------------------ OA 01, clase 5
reg(
    OA1, 5,
    materials="Papel, cartón reutilizado limpio, cinta, tijeras de punta roma, regla y lápiz. Para el modelo digital, un computador con programa de dibujo es opcional; hay alternativa en papel.",
    use="Aprenderé a hacer un modelo, concreto o digital, para probar una idea antes de construir el objeto final. Sirve para descubrir fallas sin gastar mucho material.",
    prior=["Sé hacer un dibujo con vistas, nombres y medidas.", "Sé que un criterio se comprueba con una prueba."],
    explain=[
        "Un modelo es una versión simple del objeto para probar la idea. Un modelo concreto se arma con materiales reales, como papel y cartón. Un modelo digital se hace en la pantalla con formas de un programa de dibujo. Usar computador, tableta y programas es usar TIC, las tecnologías de la información y la comunicación. En esta clase las pantallas se describen con texto y son ejemplos ficticios, porque cada programa se ve distinto.",
        "El modelo no tiene que quedar bonito. Debe servir para probar. Si el modelo de una torre se cae, aprendes qué cambiar antes de usar material bueno. Un sistema tecnológico simple es un conjunto de partes que trabajan juntas: por ejemplo, una puerta de cartón con un cordel que la levanta. Se arma y se prueba cada parte.",
        "Seguridad: corta con tijeras de punta roma, siempre alejando los dedos de la línea. Si el cartón es duro, pide a una persona adulta que haga el corte. En el modelo digital, el ejemplo ficticio tiene a la izquierda una barra con rectángulos, círculos y líneas, y arriba un botón para deshacer. Haz el modelo y anota qué descubriste.",
    ],
    vocab=[("modelo", "versión simple del objeto para probar la idea"), ("modelo concreto", "modelo hecho con materiales reales"), ("modelo digital", "modelo hecho con formas en una pantalla"), ("sistema", "conjunto de partes que trabajan juntas"), ("deshacer", "botón que borra el último paso")],
    worked=[
        ("Elegir el tipo de modelo", "Quieres saber si una torre de cartón de 15 cm se mantiene de pie. ¿Haces un modelo concreto o digital?", ["Para saber si se cae necesito probarla con peso.", "Una pantalla no se cae.", "Elijo un modelo concreto."], "Modelo concreto"),
        ("Sistema simple", "Un cordel está atado a una puerta de cartón. Al tirarlo, la puerta sube. Nombra las partes del sistema.", ["Una parte es la puerta.", "Otra es el cordel.", "Cuando tiras, el cordel mueve la puerta."], "Puerta y cordel trabajando juntos"),
    ],
    mistakes=[
        ("Gastar todo el cartón bueno en el primer modelo.", "Si falla, no queda material.", "Usa papel o cartón de reúso para el modelo."),
        ("Pensar que el modelo debe verse igual al objeto final.", "El modelo sirve para probar, no para exhibir.", "Hazlo simple y prueba lo importante."),
    ],
    R=[
        ("Un modelo hecho con papel y cartón reales ¿es concreto o digital?", "Concreto", "Se arma con materiales reales."),
        ("Un modelo hecho con formas en una pantalla ¿es concreto o digital?", "Digital", "Se hace en el computador."),
        ("Para cortar cartón con tijeras de punta roma, ¿alejas los dedos de la línea o los pones sobre ella?", "Los alejas", "Así no te cortas."),
    ],
    C=[
        ("¿Para qué sirve un modelo antes del objeto final?", "Para probar la idea y encontrar fallas", "Sirve para descubrir qué cambiar."),
        ("Una puerta, un cordel y una argolla de cartón trabajan juntas para abrir. ¿Eso es un sistema o una sola pieza?", "Un sistema", "Son varias partes que trabajan juntas."),
        ("En una pantalla ficticia, ¿qué botón usas si te equivocas en el último paso?", "Deshacer", "Borra el último paso."),
    ],
    A=[
        arith("Haces un modelo de torre con 3 pisos de 5 cm de alto cada uno. Con un piso más de 5 cm, ¿cuántos cm de alto tendría en total?", "5+5+5+5", "Se suman los cuatro pisos de 5 cm.", " cm"),
        ("Tienes cartón duro difícil de cortar. ¿Quién hace el corte: tú solo o una persona adulta?", "Una persona adulta", "El corte difícil lo hace un adulto por seguridad."),
        ("Quieres probar tu idea y tienes cartón bueno y papel de reúso. ¿Cuál usas para el modelo?", "El papel de reúso", "El modelo no necesita material bueno."),
    ],
    Z=[
        ("El modelo de Rita se cayó con 4 fichas. ¿Fracasó o dio información útil? Responde con una frase.", "Dio información útil porque muestra qué cambiar", "Una falla del modelo enseña antes de construir."),
        ("Dos modelos de una torre: A de papel suave y B de cartón doblado. Si debe sostener fichas, ¿cuál tiene más probabilidad de sostenerlas y por qué?", "B, porque el cartón es más firme", "El cartón sostiene más peso que el papel suave."),
    ],
    D=[
        ("Reto: describe un modelo digital ficticio de una caja: formas que usas y qué botón usarías para borrar un error.", "Un rectángulo para la caja y un cuadrado para la tapa; botón deshacer", "Usa formas y deshacer."),
        arith("Para el modelo tienes 12 tiras de cartón y usas 5 en la base y 4 en las paredes. ¿Cuántas tiras te quedan?", "12-5-4", "Se restan las que usaste."),
    ],
    ctx=("Mateo quiere un sistema simple: una ventana de cartón que suba con un cordel para que entre luz a una caja con una planta. Escribe qué modelo concreto haría con cartón y cordel, y qué probaría.", "Una caja con ventana que sube al tirar el cordel; probaría si sube y baja 3 veces sin romperse", "Describe el modelo y una prueba."),
    sc=[
        ("¿Un modelo debe verse perfecto o servir para probar?", "Servir para probar", "Su función es probar la idea."),
        ("¿Un sistema tiene una parte o varias que trabajan juntas?", "Varias que trabajan juntas", "Eso define un sistema."),
        ("¿Todas las pantallas de programas de dibujo se ven iguales?", "No", "Cada programa se ve un poco distinto."),
    ],
    open_task=(
        "Escoge un reto. Reto 1: soporte para 12 fichas con base de máximo 20 cm por 20 cm. Reto 2: ventana de cartón que suba con un cordel. Haz un modelo concreto de papel o cartón de reúso, o descríbelo como modelo digital ficticio con formas y deshacer. Anota qué descubriste al probarlo.",
        "Reto 1: modelo de cartón doblado, base de 18 cm, sostiene 8 fichas y se cae con 12. Descubrí que debo reforzar la base.",
        ["hace un modelo concreto o describe uno digital", "lo prueba al menos una vez", "anota qué descubrió", "respeta la seguridad al cortar"],
        ["modelo o descripción del modelo y nota de lo descubierto"],
        ["gastar material bueno en el modelo", "no probar el modelo"],
        "Pregunta: «¿qué te enseñó tu modelo?». Si responde que nada, pídele probar con más peso.",
    ),
    reinforce="Haz con una hoja una torre de papel y prueba cuántas fichas o tapas de botella sostiene, con ayuda de una persona adulta.",
    extend="Describe en palabras un modelo digital ficticio de una puerta con las formas que usarías.",
)

# ------------------------------------------------------------------ OA 01, clase 6
reg(
    OA1, 6,
    materials="Hoja, lápiz. Las tres propuestas y la tabla de puntos están escritas en el cuaderno.",
    use="Aprenderé a elegir una propuesta con criterios y a comunicarla con claridad. Sirve para defender mi diseño con razones, no con gustos.",
    prior=["Sé escribir criterios comprobables.", "Sé dibujar con partes, medidas y flechas."],
    explain=[
        "Cuando tienes varias propuestas, eliges con los criterios. Una forma es la tabla de puntos: por cada criterio que la propuesta cumple, ponle 1 punto; si no lo cumple, 0. Suma los puntos. La propuesta con más puntos es la que mejor cumple. Si hay empate, usa el criterio de seguridad para decidir.",
        "Elegir con criterios evita decidir por gusto. «Me gusta más el azul» no sirve. «Cumple 4 de 4 criterios» sí. Después hay que comunicar la propuesta. Un buen mensaje dice cuatro cosas: el problema, quién es el usuario, cómo es tu solución y por qué es la mejor.",
        "Puedes comunicar con un cartel, un dibujo con notas o una explicación hablada. Usa frases cortas y muestra el dibujo con medidas. Escucha las preguntas de otras personas: pueden darte ideas para mejorar. Si descubres una falla, anótala; así tu diseño será mejor.",
    ],
    vocab=[("propuesta", "solución escrita o dibujada que se ofrece"), ("tabla de puntos", "tabla que suma 1 punto por cada criterio cumplido"), ("empate", "cuando dos propuestas tienen los mismos puntos"), ("comunicar", "mostrar y explicar una idea a otras personas")],
    worked=[
        ("Elegir con puntos", "Criterios: C1 sostiene 12 fichas, C2 sin puntas, C3 cartón reutilizado. A cumple C1 y C2. B cumple C1, C2 y C3. ¿Cuál elegir?", ["A tiene 2 puntos.", "B tiene 3 puntos.", "Gana la que tiene más puntos."], "B, con 3 puntos"),
        ("Resolver un empate", "Las propuestas A y B tienen 3 puntos. A tiene una punta que corta y B no. ¿Cuál eliges?", ["En el empate decide la seguridad.", "B no tiene punta."], "B, por seguridad"),
    ],
    mistakes=[
        ("Elegir la propuesta que más me gusta.", "El gusto no mide si resuelve el problema.", "Suma los puntos de los criterios."),
        ("Presentar solo el dibujo sin decir el problema.", "El público no sabe para qué sirve.", "Di problema, usuario, solución y razón."),
    ],
    R=[
        ("En una tabla de puntos, ¿un criterio cumplido vale 1 punto o 0 puntos?", "1 punto", "Cumplir suma un punto."),
        ("Si dos propuestas empatan, ¿decide el gusto o la seguridad?", "La seguridad", "La seguridad es lo primero."),
        ("Mostrar y explicar una idea a otros ¿se llama comunicar o sumar?", "Comunicar", "Es explicar a otras personas."),
    ],
    C=[
        ("¿Qué cuatro cosas dice un buen mensaje al comunicar?", "Problema, usuario, solución y razón", "Son los cuatro datos clave."),
        ("¿Por qué «me gusta el azul» no sirve para elegir?", "Porque no mide si cumple los criterios", "El gusto no comprueba nada."),
        arith("A suma 2 puntos y B suma 3 puntos. ¿Cuántos puntos más tiene B?", "3-2", "Se resta lo que sumó A."),
    ],
    A=[
        ("Criterios: C1 cabe en 20 cm, C2 sin puntas, C3 reúso, C4 sostiene 12 fichas. Propuesta A cumple C1, C2 y C4. ¿Cuántos puntos tiene?", "3", "Cumple tres de cuatro criterios."),
        ("Propuesta B cumple C2 y C3 de los criterios anteriores. Propuesta A cumple C1, C2 y C4. ¿Cuál gana?", "A", "A tiene 3 puntos y B tiene 2."),
        ("Escribe una frase de problema para comunicar un soporte de 12 fichas para el usuario Dani.", "Dani necesita sostener 12 fichas sin que se caigan", "Dice usuario y qué lograr."),
    ],
    Z=[
        ("Rita sumó 4 puntos a una propuesta que tiene una punta que corta. ¿Debe corregir la punta aunque tenga muchos puntos? Responde sí o no.", "Sí", "La seguridad no se negocia."),
        ("Dos carteles: A solo dibujo, B dibujo más problema, usuario y razón. ¿Cuál comunica mejor?", "B", "Da los cuatro datos."),
    ],
    D=[
        ("Reto: las propuestas A y B tienen 3 y 3 puntos y ambas son seguras. Escribe cómo desempatarías con un criterio nuevo.", "Por ejemplo: cuál usa menos material", "Un criterio nuevo permite decidir."),
        arith("Siete niños pueden votar: 4 votan A, 2 votan B y el resto no vota. ¿Cuántos no votaron?", "7-4-2", "Se restan los votos de A y de B del total."),
    ],
    ctx=("Valentina eligió su soporte de 12 fichas. Debe presentarlo en 4 frases cortas: problema, usuario, solución y razón. Escríbelas para un soporte de cartón doblado para Dani.", "Problema: se caen las fichas. Usuario: Dani. Solución: soporte de cartón doblado. Razón: cumple 4 de 4 criterios", "Incluye las cuatro partes."),
    sc=[
        ("¿Se elige con gusto o con criterios?", "Con criterios", "Los criterios se pueden comprobar."),
        ("¿Qué se hace con los puntos de cada propuesta?", "Se suman", "La que más suma cumple más."),
        ("¿Una pregunta de otra persona puede ayudarte a mejorar?", "Sí", "Da una mirada nueva."),
    ],
    open_task=(
        "Usa estas propuestas para un soporte de 12 fichas. Criterios: C1 sostiene 12 fichas, C2 sin puntas, C3 cartón reutilizado. Propuesta A: cartón doblado, cumple C1, C2, C3. Propuesta B: cartón con clips metálicos, cumple C1 y C3. Propuesta C: cartón liso, cumple C2 y C3. El usuario es Dani. Haz la tabla de puntos, elige y comunica con 4 frases.",
        "A: 3 puntos; B: 2; C: 2. Elijo A. Problema: se caen las fichas. Usuario: Dani. Solución: cartón doblado. Razón: cumple los 3 criterios.",
        ["suma bien los puntos", "elige con los puntos", "comunica en cuatro frases", "dice la razón con los criterios"],
        ["tabla de puntos y mensaje de 4 frases"],
        ["elegir por gusto", "no decir el problema"],
        "Pregunta: «¿cuántos criterios cumple tu propuesta?». Si responde con gustos, vuelve a la tabla.",
    ),
    reinforce="Elige entre dos objetos de tu casa cuál es mejor para un uso y explica con dos criterios.",
    extend="Escribe cuatro frases para presentar un objeto que resuelva un problema de tu sala.",
)

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja y lápiz. El resultado deseado está descrito en el cuaderno.",
    use="Aprenderé a dividir un resultado en tareas pequeñas y ordenadas. Sirve para saber qué hacer primero y no olvidar pasos.",
    prior=["Sé hacer un dibujo con medidas.", "Sé que un modelo se prueba antes del objeto final."],
    explain=[
        "Planificar es pensar antes de hacer. El primer paso es partir del resultado deseado: lo que quieres tener al final, descrito con medidas y criterios. Por ejemplo: «un soporte de cartón que sostiene 12 fichas y mide 15 cm de alto».",
        "Luego se divide en tareas, que son acciones cortas y claras. Una tarea empieza con un verbo: medir, marcar, cortar, plegar, pegar, pintar. Una tarea no dice «hacer el soporte», porque es muy grande. Cada tarea debe poder hacerse y comprobarse. Por eso se escribe una por línea.",
        "Después se ordena la secuencia: lo que va primero, lo que va después y lo que va al final. Si pintas antes de cortar y pegar, la pintura se mancha o se raspa al trabajar. Revisa el orden preguntándote: ¿necesito esto listo antes de hacer la siguiente? Una secuencia clara evita errores y ahorra material.",
    ],
    vocab=[("planificar", "pensar y ordenar lo que harás antes de hacerlo"), ("resultado deseado", "lo que quieres tener al final"), ("tarea", "acción corta y clara"), ("secuencia", "orden en que se hacen las tareas"), ("verbo de acción", "palabra que dice qué hacer, como cortar")],
    worked=[
        ("Dividir en tareas", "Resultado: un guardalápices con un tubo de cartón y una base. Escribe cuatro tareas.", ["Cada tarea empieza con un verbo.", "Pienso en lo que se hace: medir, cortar, pegar, pintar.", "Las escribo en orden."], "1 medir el tubo, 2 cortar la base, 3 pegar el tubo, 4 pintar"),
        ("Detectar una tarea muy grande", "Una lista dice: «1 hacer el guardalápices». ¿Está bien escrita?", ["«Hacer» es muy general.", "No se puede comprobar si está lista.", "Debo dividirla en acciones."], "No, es una tarea muy grande"),
    ],
    mistakes=[
        ("Escribir «hacer el objeto» como una sola tarea.", "Es demasiado grande y no dice cómo.", "Divide en acciones con verbos: medir, cortar, pegar."),
        ("Poner «pintar» antes de «cortar».", "La pintura se mancha o se raspa al cortar y pegar.", "Corta y pega primero; pinta cuando todo está armado."),
    ],
    R=[
        ("Planificar ¿es pensar antes de hacer o hacer sin pensar?", "Pensar antes de hacer", "Planificar es pensar antes."),
        ("«Cortar» ¿es un verbo de acción o un nombre de objeto?", "Verbo de acción", "Dice qué se hace."),
        ("El resultado deseado ¿es lo que quieres tener al final o la primera tarea?", "Lo que quieres tener al final", "Se define antes de comenzar."),
    ],
    C=[
        ("¿Por qué «hacer el objeto» no es una buena tarea?", "Porque es muy grande y no dice qué acción hacer", "Debe dividirse en acciones concretas."),
        ("Tareas: A pegar la base, B medir la base. ¿Cuál va primero?", "B", "Se mide antes de pegar."),
        ("¿Cómo empieza cada tarea bien escrita?", "Con un verbo de acción", "El verbo dice qué hacer."),
    ],
    A=[
        ("Resultado: una cajita con tapa. Escribe tres tareas en orden con verbos.", "Medir el cartón, cortar el cartón, pegar la caja (u otro orden lógico similar)", "Tres acciones ordenadas."),
        ("Lista desordenada: pintar, medir, cortar. Escribe el orden correcto.", "Medir, cortar, pintar", "Primero se mide, luego se corta y al final se pinta."),
        arith("Tu plan tiene 3 tareas de medir y marcar y 4 de cortar y pegar. ¿Cuántas tareas tiene en total?", "3+4", "Se suman las dos listas."),
    ],
    Z=[
        ("Mía puso la tarea «pegar» antes de «cortar la pieza». ¿Qué problema habrá? Responde con una frase.", "No podrá pegar una pieza que aún no está cortada", "La pieza debe estar lista antes."),
        ("Dos planes: A tiene 2 tareas muy grandes y B tiene 6 tareas claras. ¿Cuál es más fácil de seguir?", "B", "Las tareas pequeñas se pueden comprobar."),
    ],
    D=[
        ("Reto: escribe un resultado deseado con medida y criterio, y cuatro tareas ordenadas para un soporte de 12 fichas.", "Resultado: soporte de 15 cm que sostiene 12 fichas; tareas: medir, cortar, plegar, pegar", "Resultado con dato y tareas con verbos."),
        ("Una tarea dice «construir la torre y pintarla». ¿Cuántas acciones tiene?", "2", "Construir y pintar son dos acciones."),
    ],
    ctx=("Camila quiere un portalápices de cartón para 6 lápices, de 12 cm de alto. Escribe el resultado deseado y 5 tareas ordenadas con verbos.", "Resultado: portalápices de 12 cm para 6 lápices. Tareas: medir, marcar, cortar, plegar, pegar", "Resultado con medidas y tareas ordenadas."),
    sc=[
        ("¿Una tarea empieza con un verbo?", "Sí", "El verbo dice la acción."),
        ("¿La secuencia es el orden de las tareas?", "Sí", "Dice cuál va primero."),
        ("¿Se pinta antes o después de cortar y pegar?", "Después", "Si no, la pintura se mancha o se raspa."),
    ],
    open_task=(
        "Escoge un resultado. Resultado 1: soporte de cartón para 12 fichas de 15 cm de alto. Resultado 2: portalápices de 12 cm para 6 lápices. Escribe el resultado deseado con medida y cinco tareas con verbo en orden.",
        "Resultado 1: soporte de 15 cm para 12 fichas. 1 medir, 2 marcar, 3 cortar, 4 plegar, 5 pegar.",
        ["escribe un resultado con medida", "escribe cinco tareas con verbo", "el orden es lógico"],
        ["lista con resultado y tareas"],
        ["tareas muy grandes", "orden ilógico"],
        "Pregunta: «¿esta tarea se puede hacer y comprobar?». Si no, divídela.",
    ),
    reinforce="Escribe tres tareas para ordenar tu mochila antes del colegio.",
    extend="Escribe cinco tareas para hacer una tarjeta de cartulina.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja y lápiz. La tabla de materiales, herramientas y técnicas está escrita en el cuaderno.",
    use="Aprenderé a relacionar cada tarea con su material, su herramienta y su técnica. Sirve para reunir todo antes de empezar.",
    prior=["Sé dividir un resultado en tareas con verbo.", "Sé que las tareas se ordenan."],
    explain=[
        "Cada tarea necesita un material, una herramienta y una técnica. El material es de lo que está hecho el objeto, como papel, cartón, hilo o plástico. La herramienta es lo que usas para trabajar, como regla, tijeras de punta roma o pincel. La técnica es la forma de hacer la acción: medir, marcar, cortar, plegar, unir, pegar o pintar.",
        "Por ejemplo, para la tarea «cortar», el material es cartón, la herramienta son tijeras de punta roma y la técnica es cortar siguiendo la línea. Para «medir», la herramienta es la regla y la técnica es poner el cero en el borde. Si una herramienta no sirve para esa tarea, el resultado sale mal.",
        "Haz una tabla con cuatro columnas: tarea, material, herramienta y técnica. Así sabrás qué necesitas y podrás avisar si te falta algo. Cuida también el material: usa lo que ya tienes en casa, como cartón limpio o papel de reúso, para no gastar de más. Al pegar, usa cola fría escolar en poca cantidad y no te lleves las manos sucias a la cara ni a la boca.",
    ],
    vocab=[("material", "aquello de lo que está hecho el objeto"), ("herramienta", "objeto que usas para trabajar"), ("técnica", "forma de hacer una acción"), ("tijeras de punta roma", "tijeras sin punta afilada, más seguras"), ("plegar", "doblar una pieza sobre una línea")],
    worked=[
        ("Completar una tabla", "Tarea: marcar una línea recta sobre cartón. Elige herramienta entre regla y pincel.", ["Marcar es dibujar una línea.", "La regla ayuda a que sea recta.", "El pincel es para pintar."], "Regla y lápiz"),
        ("Relacionar la técnica", "Tarea: unir dos papeles con una banda de cartulina. Técnica: ¿pegar con cola fría o pintar?", ["Unir pide juntar.", "La cola fría junta papeles.", "Pintar no une."], "Pegar con cola fría"),
    ],
    mistakes=[
        ("Elegir un pincel para cortar cartulina.", "El pincel no corta; la herramienta debe servir para la tarea.", "Usa tijeras de punta roma para cortar."),
        ("Olvidar anotar la herramienta y quedarse sin regla a la mitad.", "Se detiene el trabajo.", "Revisa la tabla y reúne todo antes de empezar."),
    ],
    R=[
        ("La tijera de punta roma ¿es herramienta o material?", "Herramienta", "Se usa para trabajar."),
        ("El cartón ¿es material o técnica?", "Material", "Es de lo que está hecho el objeto."),
        ("«Plegar» ¿significa doblar o pintar?", "Doblar", "Plegar es doblar sobre una línea."),
    ],
    C=[
        ("¿Qué herramienta sirve para medir: regla o pincel?", "Regla", "La regla tiene números."),
        ("¿Por qué conviene reunir material y herramientas antes de empezar?", "Para no detener el trabajo", "Así no falta nada a la mitad."),
        ("Para pintar con témpera, ¿qué herramienta usas: pincel o tijeras?", "Pincel", "El pincel aplica la pintura."),
    ],
    A=[
        ("Completa la tabla: tarea «cortar una tira de cartón». Escribe material, herramienta y técnica.", "Material: cartón; herramienta: tijeras de punta roma; técnica: cortar siguiendo la línea", "Los tres datos corresponden a la tarea."),
        ("Tarea «medir 15 cm». ¿Dónde pones el cero de la regla?", "En el borde del cartón", "Medir bien exige partir desde el borde."),
        ("Tarea «plegar una tira». ¿Qué haces antes de doblar: marcar la línea o pintar?", "Marcar la línea", "El doblez se hace sobre una línea."),
    ],
    Z=[
        ("Pedro quiere cortar un tubo de cartón con una cuchara. ¿Servirá? Explica brevemente.", "No, porque la cuchara no corta", "La herramienta debe servir para la tarea."),
        ("Tienes cartón de una caja limpia o cartulina nueva comprada. Si quieres cuidar el medioambiente, ¿cuál eliges?", "El cartón de la caja limpia", "Reutiliza y no gasta material nuevo."),
    ],
    D=[
        ("Reto: la tarea es «unir dos tiras de cartón». Escribe dos formas posibles de unirlas (con su material) y la técnica de cada una.", "Cola fría o cinta adhesiva; técnica de pegar", "Dos formas de unir."),
        arith("El plan tiene 6 tareas y 2 de ellas usan regla. ¿En cuántas tareas NO se usa la regla?", "6-2", "Se restan las que usan regla."),
    ],
    ctx=("Sofía arma un portalápices. Tareas: medir 12 cm, cortar el cartón, pegar la base. Completa material, herramienta y técnica para las tres.", "Medir: cartón, regla, cero en el borde; cortar: cartón, tijeras de punta roma, cortar por la línea; pegar: cartón, cola fría, presionar", "Cada tarea tiene los tres datos."),
    sc=[
        ("¿La técnica es la forma de hacer la acción?", "Sí", "Dice cómo se hace."),
        ("¿La regla sirve para medir?", "Sí", "La regla tiene números para medir."),
        ("¿Se reúnen herramientas antes o después de empezar?", "Antes", "Así no se detiene el trabajo."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: soporte de cartón para 12 fichas. Objeto 2: portalápices de cartón. Usa estas tareas: medir, marcar, cortar, plegar, pegar. Haz una tabla con tarea, material, herramienta y técnica.",
        "Medir: cartón, regla, cero en el borde. Marcar: cartón, lápiz y regla, línea recta. Cortar: cartón, tijeras de punta roma, por la línea.",
        ["completa la tabla con las cinco tareas", "la herramienta sirve para la tarea", "escribe la técnica de cada una"],
        ["tabla de tareas, materiales, herramientas y técnicas"],
        ["herramienta que no sirve para la tarea", "dejar columnas vacías"],
        "Pregunta: «¿esta herramienta sirve para esta tarea?». Si no, pídele cambiarla.",
    ),
    reinforce="Mira tres herramientas de tu casa y di para qué tarea sirve cada una.",
    extend="Escribe una tabla de tarea, material, herramienta y técnica para hacer un sobre de papel.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja y lápiz. Los planes con dependencias están escritos en el cuaderno.",
    use="Aprenderé a ver qué tarea depende de otra y a poner puntos de control. Sirve para revisar el trabajo antes de seguir.",
    prior=["Sé ordenar tareas.", "Sé relacionar tareas con materiales, herramientas y técnicas."],
    explain=[
        "Algunas tareas dependen de otras. Una tarea depende de otra cuando no se puede hacer hasta que la otra esté lista. Por ejemplo, no puedes pegar una pieza hasta que esté cortada, y no puedes pintar hasta que la cola esté seca. Mira el plan y busca qué espera a qué.",
        "Hay tareas que pueden hacerse al mismo tiempo, como medir dos piezas si dos personas trabajan. Pero una tarea que depende de otra siempre va después. Dibuja flechas entre las tareas: si una flecha va de A a B, A va primero. Así ves el orden.",
        "Un punto de control es un momento en que revisas si algo salió bien antes de seguir. Por ejemplo: «comprobar que la pieza mide 15 cm antes de cortar la segunda». Poner puntos de control evita repetir todo desde el comienzo. Tras medir, revisa; tras pegar, espera que seque.",
    ],
    vocab=[("dependencia", "cuando una tarea no puede empezar hasta que otra termine"), ("punto de control", "momento para revisar antes de seguir"), ("secar", "esperar a que la cola o la pintura pierdan la humedad"), ("al mismo tiempo", "dos tareas hechas juntas")],
    worked=[
        ("Buscar dependencias", "Tareas: A pintar, B cortar, C pegar. ¿De cuál depende A (pintar)?", ["Pintar se hace sobre lo ya armado.", "Armar exige cortar y pegar.", "Entonces depende de B y de C."], "Depende de cortar y pegar"),
        ("Poner un punto de control", "Tarea: cortar dos tiras de 15 cm. ¿Dónde pondrías el control?", ["Después de cortar la primera.", "Mido que tenga 15 cm.", "Si está bien, corto la segunda."], "Después de cortar la primera tira, medir 15 cm"),
    ],
    mistakes=[
        ("Pintar apenas se pega la pieza.", "La cola aún está húmeda y la pintura se corre.", "Espera a que seque y recién pinta."),
        ("No revisar ninguna medida hasta el final.", "Si había un error, se descubre tarde y se pierde todo.", "Pon puntos de control después de medir y de cortar."),
    ],
    R=[
        ("Si no puedes pegar hasta que cortes, ¿pegar depende de cortar o cortar depende de pegar?", "Pegar depende de cortar", "Primero hay que cortar."),
        ("Un punto de control ¿es para revisar o para pintar?", "Para revisar", "Sirve para comprobar antes de seguir."),
        ("Esperar que seque la cola ¿es un paso del plan o un descanso inútil?", "Un paso del plan", "Sin secar no se puede seguir."),
    ],
    C=[
        ("¿Por qué conviene un control después de medir?", "Para descubrir un error antes de cortar", "Si la medida está mal, el corte también."),
        ("Una flecha de A a B ¿significa que A va primero o B va primero?", "A va primero", "La flecha apunta a lo que sigue."),
        ("¿Dos personas pueden medir dos piezas al mismo tiempo?", "Sí", "No dependen una de otra."),
    ],
    A=[
        ("Tareas: pintar, secar la cola, pegar, cortar. Ordénalas.", "Cortar, pegar, secar la cola, pintar", "Cada tarea depende de la anterior."),
        ("Plan: medir 15 cm, cortar. ¿Dónde pondrías un punto de control?", "Después de medir y antes de cortar", "Se revisa la medida antes de cortar."),
        arith("La cola tarda 20 minutos en secar y ya esperaste 5 minutos. ¿Cuántos minutos más debes esperar?", "20-5", "Se resta lo ya esperado al tiempo total.", " minutos"),
    ],
    Z=[
        ("Ema pinta al instante de pegar y la pintura se corre. ¿Qué dependencia olvidó? Responde con una frase.", "Pintar depende de que la cola esté seca", "Debía esperar el secado."),
        ("Dos planes: A tiene controles después de medir y de pegar; B no tiene ninguno. ¿Cuál evita mejor repetir todo?", "A", "Los controles detectan errores a tiempo."),
    ],
    D=[
        ("Reto: ordena y escribe dos puntos de control para: pintar, cortar, medir, pegar.", "Medir, (control), cortar, pegar, (control: seco), pintar", "Dos controles razonables."),
        arith("Un plan tiene 5 tareas y 2 de ellas dependen de otras. ¿Cuántas tareas no dependen de ninguna?", "5-2", "Se restan las que dependen del total."),
    ],
    ctx=("Lucas tiene este plan: medir 15 cm, marcar, cortar, plegar, pegar, secar, pintar. Escribe de qué depende pintar y dónde pondrías dos puntos de control.", "Pintar depende de pegar y secar; controles: después de medir y después de pegar y secar", "Dos controles con motivo."),
    sc=[
        ("¿Se pinta antes o después de que la cola seque?", "Después", "Sobre cola húmeda se corre."),
        ("¿Un punto de control sirve para revisar?", "Sí", "Se comprueba antes de seguir."),
        ("¿Qué es una dependencia?", "Cuando una tarea espera a otra", "No puede empezar hasta que la otra termine."),
    ],
    open_task=(
        "Usa este plan: medir 15 cm, marcar, cortar, plegar, pegar, secar la cola, pintar. Dibuja flechas entre las tareas que dependen una de otra y escribe dos puntos de control con lo que revisas.",
        "Medir → marcar → cortar → plegar → pegar → secar → pintar. Control 1: después de medir, comprobar 15 cm. Control 2: después de secar, ver que está firme.",
        ["dibuja las flechas", "escribe dos puntos de control", "dice qué revisa en cada uno"],
        ["plan con flechas y dos controles"],
        ["sin flechas", "controles sin decir qué revisar"],
        "Pregunta: «¿qué debe estar listo antes de esta tarea?». Si no sabe, mira la flecha.",
    ),
    reinforce="Anota tres tareas de tu casa donde una espera a la otra, como secar la ropa antes de guardarla.",
    extend="Escribe un plan de 5 tareas con una dependencia y un punto de control para hacer una tarjeta.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja y lápiz. Los planes a revisar están escritos en el cuaderno.",
    use="Aprenderé a armar un plan completo y seguro, con tareas, materiales, herramientas, técnicas y medidas de seguridad. Sirve para trabajar sin accidentes.",
    prior=["Sé ordenar tareas y poner controles.", "Sé relacionar tareas con materiales y herramientas."],
    explain=[
        "Un plan completo reúne lo aprendido: resultado deseado, tareas ordenadas, materiales, herramientas, técnicas, puntos de control y medidas de seguridad. Las medidas de seguridad son cuidados para no lastimarse ni lastimar a otros.",
        "Medidas de seguridad básicas: usar tijeras de punta roma y cortar alejando los dedos; no usar cortadores, fuego ni vidrio en clase; trabajar sobre una mesa despejada; amarrar el pelo largo y usar delantal con la pintura; lavar las manos al terminar; y pedir ayuda a una persona adulta para cortes difíciles. Cada tarea del plan lleva su cuidado.",
        "Un plan es realizable cuando tienes tiempo, materiales y herramientas para hacerlo. Si dice «usar madera» y no tienes, no es realizable; cámbialo por cartón. Revisa que el plan quepa en el tiempo: si cada tarea dura 10 minutos y son 5, necesitas 50 minutos. Antes de empezar, léelo completo una vez.",
    ],
    vocab=[("medida de seguridad", "cuidado para evitar accidentes"), ("realizable", "que se puede hacer con el tiempo y los materiales que hay"), ("delantal", "prenda que protege la ropa al pintar"), ("despejada", "mesa sin cosas que estorben")],
    worked=[
        ("Agregar la seguridad", "Tarea: cortar cartón con tijeras de punta roma. Escribe la medida de seguridad.", ["Pienso qué podría lastimar.", "Las tijeras cortan los dedos si se acercan.", "La medida es alejar los dedos de la línea."], "Cortar alejando los dedos de la línea de corte"),
        ("Revisar si es realizable", "El plan dice «cortar madera» y solo hay cartón. ¿Es realizable?", ["No hay madera.", "Cambio el material por cartón."], "No, hay que cambiar a cartón"),
    ],
    mistakes=[
        ("Escribir el plan sin ninguna medida de seguridad.", "No se evitan los accidentes.", "Cada tarea lleva su cuidado."),
        ("Usar un material que no tienes.", "El plan no se puede hacer.", "Cámbialo por uno que sí tengas, como cartón."),
    ],
    R=[
        ("Tijeras de punta roma ¿son más seguras que tijeras de punta afilada?", "Sí", "Su punta no pincha."),
        ("Al pintar, ¿qué usas para proteger la ropa: delantal o guantes de cocina?", "Delantal", "El delantal protege la ropa."),
        ("¿El fuego se usa en estas clases de tecnología?", "No", "No es seguro."),
    ],
    C=[
        ("Un corte difícil de cartón duro, ¿lo haces tú solo o con una persona adulta?", "Con una persona adulta", "Es más seguro."),
        ("¿Qué significa que un plan sea realizable?", "Que se puede hacer con el tiempo y materiales que hay", "No exige cosas que no tienes."),
        ("Antes de empezar, ¿lees el plan completo una vez o empiezas sin leerlo?", "Lo lees completo una vez", "Así evitas errores."),
    ],
    A=[
        ("Escribe una medida de seguridad para la tarea «pintar con témpera».", "Usar delantal y lavarse las manos al terminar", "Protege la ropa y las manos."),
        arith("Un plan tiene 5 tareas de 10 minutos cada una. ¿Cuántos minutos necesita en total?", "5*10", "Se multiplican tareas por minutos.", " minutos"),
        ("Tienes 45 minutos y el plan necesita 50. ¿Es realizable así? Responde sí o no.", "No", "50 es mayor que 45."),
    ],
    Z=[
        ("Un plan dice «cortar con un cuchillo». ¿Qué cambio de herramienta haces?", "Usar tijeras de punta roma", "El cuchillo no es seguro para esta edad."),
        ("Dos planes: A tiene cuidado en cada tarea, B no. ¿Cuál puedes empezar con menos riesgo?", "A", "Tiene seguridad en cada tarea."),
    ],
    D=[
        ("Reto: completa un plan de un portalápices con cuatro tareas, y una medida de seguridad para cada una.", "Medir: regla; cortar: dedos lejos; pegar: cola fría sin tocar la boca; pintar: delantal", "Cuatro tareas con su cuidado."),
        arith("Tienes 60 minutos. El plan usa 25 minutos en cortar y 20 en pegar. ¿Cuántos minutos te quedan para pintar y secar?", "60-25-20", "Se restan los tiempos usados.", " minutos"),
    ],
    ctx=("Inés planifica un soporte de 12 fichas. Tiene 60 minutos. Escribe el resultado, cuatro tareas con herramienta y una medida de seguridad cada una, y revisa el tiempo si cada tarea dura 10 minutos.", "Resultado: soporte de 15 cm. Medir con regla; cortar con tijeras de punta roma alejando dedos; plegar; pegar con cola fría. Total 40 minutos: cabe en 60", "Plan con seguridad y tiempo."),
    sc=[
        ("¿Cada tarea del plan lleva su cuidado?", "Sí", "Así se evitan accidentes."),
        ("¿Se usan cortadores en estas clases?", "No", "Solo tijeras de punta roma."),
        ("¿Un plan realizable cabe en el tiempo disponible?", "Sí", "Debe poder terminarse."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: soporte de cartón para 12 fichas. Objeto 2: portalápices de cartón. Escribe tu plan completo: resultado deseado con medida, cinco tareas en orden, material y herramienta de cada una, un punto de control, y una medida de seguridad por tarea.",
        "Objeto 1: resultado: soporte de 15 cm. Medir: regla. Cortar: tijeras de punta roma, dedos lejos. Plegar. Pegar: cola fría. Control: medir antes de cortar.",
        ["incluye resultado con medida", "cinco tareas en orden", "material y herramienta en cada una", "un punto de control", "una medida de seguridad por tarea"],
        ["plan completo escrito"],
        ["olvidar la seguridad", "usar herramientas que no sirven o no son seguras"],
        "Pregunta: «¿cómo cuidas tus dedos en esta tarea?». Si no sabe, revisa las medidas de seguridad.",
    ),
    reinforce="Cuéntale a una persona de tu casa tu plan y pídele que revise si tiene seguridad.",
    extend="Haz un plan con 5 tareas y sus cuidados para armar una cajita con tapa.",
)

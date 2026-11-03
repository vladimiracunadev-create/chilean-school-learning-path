"""Cuaderno del estudiante de 8.º básico Artes Visuales: AR08 OA 03 (instalación como medio de expresión contemporáneo)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR08 OA 03"


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
    "Hojas, lápiz de mina y lápices de colores. Las tres instalaciones de ejemplo están descritas en esta clase; no necesitas buscarlas.",
    "Aprenderé qué es una instalación, cómo se observa sin copiarla y qué recursos usa. Sirve para empezar una instalación propia con objetos cotidianos, sin repetir la de otra persona.",
    ["Sé que un referente se reinterpreta y no se copia.", "Sé registrar dos detalles, una pregunta y una posibilidad."],
    [
        "Una instalación es una obra que se arma en un espacio y que el público recorre o en la que se siente adentro. Es un medio de expresión contemporáneo, como la performance o el video. A diferencia de un cuadro, que se mira de frente, en una instalación importan los objetos, el espacio, el recorrido, la luz y el tiempo. El recorrido es el camino que sigue el público. Muchas instalaciones son temporales: se montan para un tiempo y se desmontan, y así será la que hagas en casa.",
        "Al observar una instalación me fijo en qué recursos usa. Puede repetir un mismo objeto muchas veces, colgarlo a distintas alturas, cambiar su escala o dejar un espacio vacío. Por ejemplo, una instalación de ejemplo cuelga botellas plásticas limpias de hilos a distintas alturas, como una lluvia que el público atraviesa. Otra pone una mesa con seis platos vacíos cubiertos de polvo gris y sillas inclinadas, como si todos se hubieran ido de pronto.",
        "Observar sin copiar es tomar un recurso y cambiar el resto. Del recurso de colgar objetos a distintas alturas puedo hacer una lluvia de papeles o de tela. También me cuido de no generalizar: una instalación muestra un punto de vista de su autor o autora, no cómo son todas las personas o todas las familias. Anoto la procedencia del referente y registro dos detalles, una pregunta y una posibilidad propia.",
    ],
    [("instalación", "obra que se arma en un espacio y que el público recorre o en la que se siente adentro"), ("recorrido", "camino que sigue el público dentro de la obra"), ("contemporáneo", "de nuestra época"), ("montaje", "armado de una obra en un espacio"), ("suspender", "colgar algo de modo que quede en el aire")],
    [
        w("Registrar una instalación", "Instalación de ejemplo: botellas plásticas limpias cuelgan de hilos a distintas alturas en un pasillo y el público pasa entre ellas. Registra dos detalles, una pregunta y una posibilidad.", ["Detalle 1: las botellas cuelgan a alturas distintas.", "Detalle 2: el público pasa entre ellas.", "Pregunta: ¿por qué el autor eligió alturas distintas?", "Posibilidad: colgar tarjetas de papel con palabras sobre el agua, a alturas distintas."], "Dos detalles (alturas distintas, el público pasa entre ellas), una pregunta sobre las alturas y una posibilidad propia con otro objeto"),
        w("Copia o reinterpretación", "Instalación de ejemplo: una mesa con seis platos vacíos cubiertos de polvo gris y sillas inclinadas. Ana arma una mesa con seis platos vacíos cubiertos de polvo gris y sillas inclinadas. Bruno toma la idea de «un lugar preparado donde falta la gente» y arma un escritorio con un cuaderno abierto y la silla echada hacia atrás, sin nadie. ¿Quién copia y quién reinterpreta?", ["Ana repite objetos, cantidad y disposición.", "Bruno conserva solo el recurso de la ausencia."], "Ana copia; Bruno reinterpreta"),
    ],
    [
        m("Pensar que una instalación es una escultura más grande.", "En una instalación el público entra, recorre o se siente dentro; no se mira solo desde afuera.", "Pregunta cómo el público se mueve y qué experimenta dentro de la obra."),
        m("Decir que una instalación muestra cómo son todas las personas o todas las familias.", "Una obra muestra un punto de vista, no un retrato de todos.", "Habla solo de lo que se ve en esa instalación y de su autoría."),
    ],
    [
        ex("¿Cuál es una diferencia de una instalación respecto de un cuadro? A. El público recorre o se siente dentro del espacio de la obra B. Siempre se hace con pintura.", "A", "En la instalación importa el espacio que rodea al público."),
        ex("La instalación de las botellas las cuelga de hilos. ¿Qué recurso usa: suspender los objetos o apoyarlos en el piso?", "Suspender los objetos", "Los cuelga de hilos, a distintas alturas."),
        ex("En una instalación hay un camino libre entre los objetos para que el público entre y salga. ¿Qué elemento de la instalación es ese camino? A. El recorrido B. La luz.", "A", "El recorrido es el camino que sigue el público."),
    ],
    [
        ex("En la instalación de las botellas, el público pasa entre los objetos suspendidos. ¿Qué experiencia destaca? A. Estar rodeado por la obra B. Mirarla solo desde lejos.", "A", "Al pasar entre las botellas, el público queda dentro de la obra."),
        ex("Un compañero dice que la mesa con platos cubiertos de polvo gris muestra cómo son todas las familias. ¿Qué error comete?", "Generaliza a todas las familias desde una sola obra", "Una instalación muestra un punto de vista de su autor."),
        ex("¿Cuál es una posibilidad propia que reinterpreta la lluvia de botellas? A. Colgar hojas de diario arrugadas a distintas alturas B. Colgar botellas idénticas a las mismas alturas.", "A", "Cambia el objeto y conserva el recurso de suspender a alturas distintas."),
    ],
    [
        arith("Una instalación de ejemplo cuelga 5 filas de 8 botellas. ¿Cuántas botellas cuelgan en total?", "5*8", "Se multiplican las filas por las botellas de cada una."),
        ex("Otra instalación de ejemplo pone 30 sillas de madera mirando hacia un árbol. Quieres tomar el recurso de objetos ordenados que miran hacia algo. ¿Qué plan lo reinterpreta? A. Libros cerrados sobre el piso, apuntando hacia una ventana B. 30 sillas mirando un árbol.", "A", "Cambia el objeto y el lugar y conserva el recurso."),
        ex("Tres anotaciones sobre la lluvia de botellas: 1) «Las botellas cuelgan a alturas distintas». 2) «Es impresionante». 3) «El público pasa entre ellas». ¿Cuántas son detalles comprobables?", "2", "La 1 y la 3 se ven; «impresionante» es una opinión."),
    ],
    [
        ex("Tomás pone 30 sillas de madera mirando un árbol. Lía pone ocho cojines en el piso apuntando hacia una puerta. ¿Quién reinterpreta y qué recurso conserva?", "Lía; conserva el de objetos ordenados que miran hacia algo", "Cambia objetos y lugar; Tomás repite la obra."),
        ex("Pía mira la lluvia de botellas y dice «habla de cuidar el agua». Sofía dice «habla de cuánto plástico se bota». ¿Pueden ser válidas las dos interpretaciones?", "Sí, si cada una se apoya en detalles", "Una instalación puede tener varias lecturas con respaldo en lo que se ve."),
    ],
    [
        ex("Quieres que tu instalación sea segura para quien la recorra. ¿Qué decisión conviene? A. Dejar un pasillo libre de objetos en el piso por donde se camina B. Cubrir todo el piso con objetos sueltos.", "A", "Un camino libre evita tropiezos."),
        ex("Montas una instalación en tu casa solo por una tarde. ¿Qué la define como temporal? A. Se desmonta y el lugar queda como estaba B. Se deja armada en el pasillo sin fecha de retiro.", "A", "Muchas instalaciones se montan para un tiempo y se desmontan; la tuya en casa también."),
    ],
    ex("Tu curso quiere hacer una instalación en el pasillo con objetos reutilizados. Tienes de referente la lluvia de botellas. ¿Qué plan reinterpreta y declara la procedencia? A. Colgar tiras de tela a distintas alturas y anotar que el recurso de suspender viene de la lluvia de botellas B. Colgar botellas iguales y presentarlas como idea propia.", "A", "Cambia el objeto y declara de dónde viene el recurso."),
    [
        ex("En Artes Visuales, ¿qué es una instalación?", "Una obra armada en un espacio que el público recorre o en la que se siente adentro", "Es un medio de expresión contemporáneo."),
        ex("Verdadero o falso: una instalación se mira solo de frente, como un cuadro.", "Falso", "El público se mueve dentro del espacio de la obra."),
        ex("¿Cómo se llama el camino que sigue el público dentro de una instalación?", "Recorrido", "Es uno de los elementos que se diseñan."),
    ],
    task(
        "Elige UNA instalación de ejemplo. A) Botellas plásticas limpias colgadas de hilos a distintas alturas en un pasillo. B) Una mesa con seis platos vacíos cubiertos de polvo gris y sillas inclinadas. C) Treinta sillas de madera ordenadas mirando hacia un árbol en un patio. En tu bitácora anota dos detalles, una pregunta y la procedencia. Luego dibuja dos bocetos que reinterpreten recursos distintos con objetos cotidianos seguros (cartón, tela, papel) y elige uno.",
        "Elegí la A. Detalles: las botellas cuelgan a alturas distintas; el público pasa entre ellas. Pregunta: ¿por qué botellas y no otro objeto? Procedencia: instalación de ejemplo de esta clase. Boceto 1: tarjetas de papel colgadas a distintas alturas. Boceto 2: calcetines viejos colgados en fila. Elijo el 1.",
        ["registra dos detalles, una pregunta y la procedencia", "hace dos bocetos con recursos distintos", "usa objetos cotidianos y seguros", "no copia los objetos del referente"],
        ["bitácora de observación", "dos bocetos", "elección anotada"],
        ["repetir los mismos objetos del referente", "generalizar a todas las personas"],
        "Pregunta qué recurso tomó y qué objeto distinto eligió.",
    ),
    "Mira un rincón de tu casa y di en voz alta qué objetos podrías colgar o ordenar allí y cómo se movería una persona al recorrerlo.",
    "Describe en tres frases cómo cambiaría la experiencia del público si la lluvia de botellas estuviera en un patio abierto en vez de un pasillo.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Hojas y lápiz. Las tres fichas de instalaciones están escritas en esta clase.",
    "Aprenderé a investigar el contexto, el material y el propósito de una instalación, y a separar datos de inferencias. Sirve para entender por qué una obra está hecha para un lugar y para un público.",
    ["Sé que una instalación se arma en un espacio y se desmonta.", "Sé separar datos de inferencias."],
    [
        "Muchas instalaciones se hacen para un sitio específico, es decir, un lugar concreto como el hueco de una escalera, un patio o un pasillo. El lugar es parte de la obra: cambia lo que se puede colgar, cuánta gente pasa y desde dónde se ve. El contexto de una instalación incluye el lugar, el tiempo que dura, quién la hizo y para quién. El público es la gente que la recorre.",
        "Los materiales suelen ser cotidianos: telas, cajas, botellas, papel, sillas. Muchas veces es una decisión de la autoría. Un material cotidiano puede hablar del tema de la obra o hacer que el público la sienta cercana. El propósito es para qué se hizo: mostrar el movimiento del agua, invitar a conversar, hablar de los envases que usamos. Para entenderlo, relaciono el lugar, el material y el propósito.",
        "Distingo datos de inferencias. Si la ficha dice «duró dos semanas», es un dato; si yo digo «duró poco por falta de presupuesto», es una inferencia que no puedo afirmar. Cuando falta información, la marco como pendiente y busco una fuente, como la ficha del lugar o el relato de quien hizo la obra. Con esto decido qué recurso tomo para mi instalación y cuál no.",
    ],
    [("sitio específico", "lugar concreto para el cual se piensa una obra"), ("público", "personas que recorren o miran una obra"), ("propósito", "para qué se hizo la obra"), ("cotidiano", "de uso común en la vida diaria"), ("ficha", "texto breve con los datos de una obra")],
    [
        w("Leer una ficha", "Ficha de ejemplo: «Corriente: 120 tiras de tela azul colgadas en el hueco de la escalera de un colegio durante dos semanas, para mostrar el movimiento del agua de un río del sector». Señala contexto, material y propósito.", ["Contexto: escalera de un colegio, dos semanas.", "Material: tiras de tela azul.", "Propósito: mostrar el movimiento del agua de un río."], "Contexto: escalera de colegio; material: tela azul; propósito: mostrar el movimiento del agua"),
        w("Dato o inferencia", "La ficha de «Mesa de espera» dice: «mesa larga con 12 sillas distintas y tazas sin usar, en el patio de una biblioteca barrial, para invitar a conversar». Un compañero escribe: «Por eso los vecinos se hicieron amigos». ¿Qué es su frase?", ["La ficha no dice qué pasó entre los vecinos.", "La frase deduce un resultado que no aparece."], "Una inferencia sin respaldo; el dato es que se armó para invitar a conversar"),
    ],
    [
        m("Pensar que una instalación puede cambiarse de lugar sin que cambie la obra.", "El lugar forma parte del sentido y de las decisiones de la obra.", "Pregunta qué cambia si el lugar es otro: cuántos objetos caben, cómo se recorre y quién la ve."),
        m("Escribir como dato algo que la ficha no dice.", "Se mezcla lo que yo imagino con lo que realmente se sabe.", "Márcalo como inferencia o como dato pendiente."),
    ],
    [
        ex("Ficha: «120 tiras de tela azul colgadas en el hueco de la escalera de un colegio». ¿Cuál es el material?", "Tiras de tela azul", "La ficha nombra el material de la instalación."),
        ex("Ficha: «Mesa larga con 12 sillas distintas y tazas sin usar, en el patio de una biblioteca barrial, para invitar a conversar». ¿Cuál es el lugar?", "El patio de una biblioteca barrial", "La ficha lo dice como parte del contexto."),
        ex("Esa misma ficha dice «para invitar a conversar». ¿Eso es el material o el propósito?", "El propósito", "Dice para qué se hizo la obra."),
    ],
    [
        ex("La ficha de «Eco», con cajas de cartón apiladas en el pasillo de una feria, dice que estuvieron una semana. ¿Cuál afirmación es un dato? A. Estuvieron una semana B. Estuvieron una semana porque la feria era corta.", "A", "La ficha afirma la duración, pero no dice la causa."),
        ex("¿Por qué una instalación de tiras azules colgadas en una escalera puede mostrar bien el movimiento del agua? A. Porque la escalera permite colgarlas desde arriba y verlas desde distintos pisos B. Porque las tiras son azules.", "A", "El lugar permite una caída larga y vista desde distintos niveles, como una corriente."),
        ex("Una ficha no dice cuánta gente recorrió la instalación. ¿Qué haces? A. Lo anoto como pendiente y busco una fuente B. Escribo una cantidad que me parece posible.", "A", "Los datos que faltan se buscan, no se inventan."),
    ],
    [
        arith("Otra instalación de ejemplo cuelga 96 tiras de papel en 8 filas iguales. ¿Cuántas tiras hay en cada fila?", "96//8", "Se reparten las tiras en partes iguales."),
        arith("Otra mesa larga de ejemplo tiene 14 sillas repartidas por igual en los dos lados. ¿Cuántas sillas hay por lado?", "14//2", "Se divide el total entre los dos lados."),
        arith("Una instalación de ejemplo apila cajas de cartón abiertas hacia el público: 6 pilas de 7 cajas cada una. ¿Cuántas cajas hay?", "6*7", "Se multiplica la cantidad de pilas por las cajas de cada pila."),
    ],
    [
        ex("«Corriente» usa telas azules para hablar de un río, y «Mesa de espera» usa sillas y tazas para invitar a conversar. ¿Cuál de las dos eligió un material que se parece a su tema?", "Corriente", "La tela azul se parece al agua que quiere mostrar."),
        ex("Una compañera dice que «Mesa de espera» se hizo para ganar un premio. La ficha solo dice que fue para invitar a conversar. ¿Qué es su afirmación?", "Una inferencia sin respaldo", "La ficha no menciona ningún premio."),
    ],
    [
        ex("Una ficha dice: «Cajas de cartón de distintos tamaños apiladas en el pasillo de una feria, abiertas hacia el público, para hablar de los envases que usamos». ¿Cuál afirmación es una inferencia? A. Está en el pasillo de una feria B. Probablemente usaron cajas porque son envases que todos conocemos.", "B", "La ficha no dice por qué eligieron cajas."),
        ex("Quieres una instalación para invitar a conversar en tu patio escolar. Propuesta X: sillas distintas alrededor de una mesa con tazas sin usar. Propuesta Y: una pared cubierta de cartulinas con letras grandes. ¿Cuál se parece más al propósito de invitar a conversar?", "X", "Una mesa con sillas invita a sentarse y hablar."),
    ],
    ex("Debes elegir dónde montar una instalación de tiras de tela que muestren el movimiento del agua. ¿Qué lugar sirve más? A. Un hueco de escalera donde las tiras pueden colgar desde arriba B. Un rincón sin altura donde solo caben dos tiras.", "A", "La altura permite que las tiras cuelguen y se vean como una corriente."),
    [
        ex("¿Qué es un sitio específico?", "Un lugar concreto para el cual se piensa una obra", "Por ejemplo, una escalera o un patio."),
        ex("Verdadero o falso: si la ficha no dice un dato, puedo escribirlo como seguro.", "Falso", "Un dato que falta se busca o se marca como pendiente."),
        ex("¿Qué tres cosas se investigan de una instalación en esta clase?", "Contexto, material y propósito", "Juntas explican por qué está hecha así."),
    ],
    task(
        "Elige UNA ficha. A) «Corriente»: 120 tiras de tela azul colgadas en el hueco de la escalera de un colegio durante dos semanas, para mostrar el movimiento del agua de un río del sector. B) «Mesa de espera»: una mesa larga con 12 sillas distintas y tazas sin usar, en el patio de una biblioteca barrial, para invitar a conversar. C) «Eco»: cajas de cartón apiladas en el pasillo de una feria, abiertas hacia el público, para hablar de los envases que usamos. Haz una tabla con contexto, material y propósito, marca una inferencia tuya con una pregunta para investigarla y anota qué recurso tomarías para una instalación propia.",
        "Elegí la A. Contexto: escalera de colegio, dos semanas. Material: tiras de tela azul. Propósito: mostrar el movimiento del agua. Inferencia: tal vez se eligió la escalera por su altura; pregunta: ¿cuántos pisos tenía? Recurso: dejar caer tiras desde arriba con una forma que se vea desde varios niveles.",
        ["completa contexto, material y propósito con datos de la ficha", "marca una inferencia distinta de los datos", "propone una pregunta para investigar", "elige un recurso para una instalación propia"],
        ["tabla de tres columnas", "inferencia con pregunta", "recurso elegido"],
        ["escribir como dato algo que la ficha no dice", "olvidar relacionar lugar, material y propósito"],
        "Señala un dato y una inferencia de la tabla y pregunta qué fuente confirmaría la inferencia.",
    ),
    "Mira un espacio de tu casa o de tu escuela y di en voz alta cómo cambiaría una instalación si se montara allí en vez de en otro lugar.",
    "Escribe dos propósitos distintos para una instalación con cajas de cartón y explica cómo cambiaría su montaje en cada uno.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Hojas, lápiz, regla, cartón, hilo y tiras de tela o de papel de diario. Para las pruebas de luz puedes usar una linterna a pilas. No uses velas ni lámparas conectadas a la red.",
    "Aprenderé a explorar decisiones de una instalación como la escala, la repetición, el recorrido, la altura y la luz, y a dibujarlas en un plano en planta. Sirve para probar un montaje en pequeño antes de hacerlo en grande.",
    ["Sé cuáles son los elementos de una instalación.", "Sé cambiar una sola variable al hacer pruebas."],
    [
        "En una instalación decido varias cosas. La escala es el tamaño de los objetos comparado con las personas: una taza de cartón de un metro de alto produce sorpresa. La repetición usa muchos objetos iguales para crear sensación de multitud o de ritmo. La agrupación junta objetos y la dispersión los reparte por el espacio. La altura, desde el piso hasta el techo, cambia cómo se mira la obra.",
        "El recorrido puede ser recto, en espiral o con tramos angostos y amplios. Un tramo estrecho con objetos muy cerca da sensación de encierro; llegar después a un espacio amplio da alivio. La luz también habla: una linterna a pilas muy cerca de un objeto proyecta una sombra grande, y más lejos la proyecta pequeña. Al montar siempre dejo un camino libre y uso objetos livianos, sin vidrio, sin cables y sin fuego; no cuelgo hilos delgados a la altura de los ojos.",
        "Para probar sin armar todo, dibujo un plano en planta: la vista desde arriba del espacio, con símbolos para los objetos y flechas para el recorrido. Uso una escala, por ejemplo 1 cm del dibujo equivale a 50 cm reales. Después hago una maqueta pequeña con cartón. Cambio una sola variable por prueba, comparo con mi intención y elijo con evidencia.",
    ],
    [("escala", "tamaño de los objetos comparado con las personas o con otros objetos"), ("planta", "dibujo del espacio visto desde arriba"), ("escala de dibujo", "relación entre una medida del dibujo y la medida real"), ("dispersión", "reparto de los objetos por todo el espacio"), ("maqueta", "versión pequeña de una obra para probarla")],
    [
        w("Leer una escala", "En tu plano en planta, 1 cm equivale a 50 cm reales. Un pasillo mide 6 cm en el plano. ¿Cuánto mide en la realidad?", ["Cada centímetro del plano vale 50 cm reales.", "Multiplico 6 por 50."], "300 cm, es decir, 3 m"),
        w("Elegir una sombra", "Prueba 1: la linterna a pilas está a 20 cm de un objeto y la sombra en la pared mide 25 cm. Prueba 2: está a 80 cm y la sombra mide 10 cm. Quieres una sombra grande. ¿Cuál eliges?", ["Cuanto más cerca está la luz, más grande es la sombra.", "La prueba 1 tiene la luz más cerca y la sombra más grande."], "La prueba 1"),
    ],
    [
        m("Llenar todo el piso de objetos para que se vea «más completa».", "Sin camino libre, el público no puede recorrerla y puede tropezar.", "Deja un recorrido libre y usa el espacio vacío como decisión."),
        m("Cambiar la cantidad, la luz y la altura al mismo tiempo en una sola prueba.", "No se sabe cuál variable produjo el efecto.", "Cambia una sola variable y anota qué cambió."),
    ],
    [
        ex("En un dibujo en planta, ¿desde dónde se ve el espacio: desde arriba o de frente?", "Desde arriba", "La planta es la vista desde arriba."),
        ex("Acercas una linterna a pilas a un objeto y su sombra en la pared se agranda. ¿Qué recurso usaste: sombra proyectada o recorrido?", "Sombra proyectada", "La luz y el objeto producen la sombra."),
        ex("Para que el público pueda recorrer una instalación en el piso, ¿qué debe quedar libre? A. Un camino sin objetos por donde caminar B. El techo.", "A", "Un camino libre permite recorrerla con seguridad."),
    ],
    [
        ex("Quieres que el público sienta que entra a un lugar apretado. ¿Qué decisión usas? A. Objetos muy cerca unos de otros, con poco espacio para pasar B. Un espacio vacío y amplio.", "A", "La poca distancia entre objetos produce encierro."),
        ex("Haces una taza de cartón de 1 m de alto. ¿Qué recurso aplicaste? A. Escala ampliada B. Repetición.", "A", "Hiciste un objeto cotidiano mucho más grande de lo normal."),
        ex("Un recorrido en espiral, ¿cómo hace avanzar al público? A. Girando hacia el centro B. En línea recta.", "A", "La espiral rodea un centro."),
    ],
    [
        arith("En tu plano, 1 cm equivale a 50 cm reales. La sala real mide 450 cm de largo. ¿Cuántos centímetros mide en el plano?", "450//50", "Se divide la medida real entre lo que vale 1 cm del plano."),
        arith("Tienes 12 objetos y los ordenas en tres filas iguales con un espacio para caminar entre ellas. ¿Cuántos objetos hay en cada fila?", "12//3", "Se reparten en partes iguales."),
        ex("En el plano, una puerta mide 2 cm con la escala de 1 cm = 50 cm. ¿Cuánto mide la puerta real?", "100 cm", "2 por 50 son 100 centímetros."),
    ],
    [
        ex("Quieres que el público sienta que la lluvia lo rodea. Propuesta X: objetos colgando solo a un lado del pasillo. Propuesta Y: objetos colgando a ambos lados y arriba del recorrido. ¿Cuál conviene?", "Y", "Rodea al público por varios lados."),
        ex("Quieres una sombra pequeña y delicada. ¿Dónde pones la linterna respecto del objeto? A. Lejos del objeto B. Muy cerca del objeto.", "A", "Cuanto más lejos está la luz, más pequeña es la sombra."),
    ],
    [
        ex("Quieres que el público entre por un tramo estrecho y llegue después a un espacio amplio. ¿Qué efecto emocional buscas? A. Alivio al llegar B. Encierro continuo.", "A", "El espacio amplio después del estrecho da alivio."),
        ex("¿Qué montaje es más seguro para el público? A. Objetos livianos de cartón colgados con hilo a un lado del recorrido, fuera de la altura de los ojos B. Objetos pesados colgados con hilo fino sobre el camino.", "A", "Los objetos livianos no lastiman si se caen y, fuera de la altura de los ojos, no hay hilos que golpeen la cara."),
    ],
    ex("El pasillo de tu casa mide 120 cm de ancho y el camino libre para el público debe medir 80 cm. ¿Cuántos centímetros quedan para ubicar objetos?", "40 cm", "Se resta el camino libre del ancho total: 120 menos 80."),
    [
        ex("¿Qué es una planta en un proyecto de instalación?", "Un dibujo del espacio visto desde arriba", "Sirve para probar la disposición."),
        ex("Verdadero o falso: una linterna más cerca del objeto da una sombra más pequeña.", "Falso", "Más cerca produce una sombra más grande."),
        ex("¿Por qué conviene cambiar una sola variable por prueba?", "Para saber cuál produjo el efecto", "Si cambian varias, no se sabe cuál causó el cambio."),
    ],
    task(
        "Elige UN espacio. A) Un pasillo de 300 cm de largo y 120 cm de ancho. B) Un rincón de 200 cm por 200 cm. C) Un patio de 400 cm por 300 cm. Dibuja un plano en planta con la escala 1 cm = 50 cm, ubica entre 6 y 12 objetos y dibuja una flecha con el recorrido. Haz dos pruebas cambiando solo una variable (escala, agrupación o altura) y escribe qué efecto produjo cada una y cuál elegirías.",
        "Elegí el pasillo: 6 cm × 2,4 cm en el plano. 9 objetos en tres grupos. Variable: agrupación. Prueba 1, todos juntos: sensación de encierro. Prueba 2, tres grupos con espacios: se puede recorrer. Elijo la 2. Camino libre de 80 cm.",
        ["dibuja el plano con la escala indicada", "deja un camino libre", "cambia una sola variable entre las pruebas", "describe el efecto y elige con una razón"],
        ["plano en planta", "dos pruebas", "elección justificada"],
        ["llenar todo el espacio sin camino libre", "cambiar varias variables a la vez"],
        "Pregunta qué variable cambió y qué efecto concreto tuvo en el recorrido.",
    ),
    "Camina por un pasillo o una pieza de tu casa y piensa qué cambiaría si hubiera objetos livianos colgando a distintas alturas, siempre dejando libre el camino.",
    "Dibuja el mismo plano con otro recorrido (recto o en espiral) y explica cómo cambia la experiencia del público.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Hojas, lápiz, regla, cartón, tela, papel de diario, hilo y cinta de papel. Elige un lugar de tu casa sin cables ni escaleras y avisa a una persona adulta.",
    "Aprenderé a planear y montar una instalación mínima propia, con plano, montaje, documentación, cartela y desmontaje. Sirve para pasar de las pruebas a una obra que otras personas puedan recorrer.",
    ["Sé dibujar un plano en planta con escala.", "Sé que una instalación deja un camino libre y se desmonta."],
    [
        "Para crear una instalación propia sigo seis pasos. Primero escribo mi intención: qué quiero que sienta o piense el público. Segundo, elijo un espacio y una lista de objetos seguros. Tercero, dibujo un plano en planta. Cuarto, hago el montaje. Quinto, documento la obra con dibujos o fotos desde tres puntos de vista. Sexto, desmonto y dejo el lugar como estaba.",
        "Una buena intención es específica: «que quien pase por el pasillo se sienta dentro de una lluvia de papeles que caen» dice qué recurso y qué efecto busco; «una instalación bonita» no dice nada. La cartela es la etiqueta que acompaña la obra con su título, la autoría, los materiales y una breve explicación. No uso datos personales: escribo, por ejemplo, «autoría: (tu nombre)».",
        "Documentar desde varios puntos de vista es importante porque una instalación se ve distinta según dónde está la persona: desde la entrada, desde el centro o desde el fondo. Cuido la seguridad: objetos livianos, camino libre, sin vidrio ni fuego, y aviso a una persona adulta antes de montar. Al desmontar, guardo los materiales para reutilizarlos.",
    ],
    [("intención", "lo que quiero que el público sienta o piense"), ("cartela", "etiqueta con título, autoría, materiales y explicación breve"), ("documentación", "registro de la obra con dibujos o fotos"), ("desmontaje", "retiro de la obra y recuperación del lugar"), ("punto de vista", "lugar desde donde se mira la obra")],
    [
        w("Mejorar una intención", "Mejora esta intención: «Quiero hacer una instalación bonita».", ["No dice qué quiero que el público sienta ni con qué recurso.", "Agrego el recurso: tiras de tela colgadas a distintas alturas.", "Agrego el efecto: que quien pase sienta que camina bajo una corriente."], "«Quiero que quien pase por el pasillo sienta que camina bajo una corriente, con tiras de tela colgadas a distintas alturas»"),
        w("Cuántos metros se cubren", "Tienes 15 objetos reutilizados y usarás 3 por cada metro de recorrido. ¿Cuántos metros cubres?", ["Cada metro necesita 3 objetos.", "Divido 15 entre 3."], "5 metros"),
    ],
    [
        m("Montar sin avisar a una persona adulta y sin revisar el lugar.", "Puede haber cables, escaleras u objetos frágiles que causen un accidente.", "Elige un lugar seguro y avisa a una persona adulta."),
        m("Documentar la obra desde un solo lugar.", "Una instalación se ve distinta según el punto de vista.", "Registra desde la entrada, el centro y el fondo."),
    ],
    [
        ex("Según los seis pasos, ¿qué paso va justo antes del montaje?", "Dibujar el plano en planta", "Primero se planifica en el plano y luego se monta."),
        ex("¿Qué datos lleva una cartela?", "Título, autoría, materiales y una breve explicación", "Es la etiqueta que acompaña la obra."),
        ex("Terminada la exposición, ¿qué haces? A. Desmontar y dejar el lugar como estaba B. Dejar los objetos tirados en el piso.", "A", "La instalación es temporal y el lugar se devuelve."),
    ],
    [
        ex("¿Cuál intención es específica? A. «Que quien pase por el pasillo se sienta dentro de una lluvia de papeles que caen» B. «Quiero hacer una instalación bonita».", "A", "Dice el recurso y el efecto."),
        ex("Quieres un camino libre de 80 cm. ¿Qué espacio sirve? A. Un pasillo de 120 cm de ancho B. Un rincón de 70 cm de ancho.", "A", "El pasillo permite dejar el camino libre; el rincón no alcanza."),
        ex("¿Por qué documentar desde varios puntos de vista? A. Porque la instalación se ve distinta según dónde está quien la mira B. Para usar más hojas.", "A", "Cada punto de vista muestra otra cosa."),
    ],
    [
        arith("Tienes 18 tiras de tela y quieres colgarlas en 3 hilos con el mismo número de tiras en cada hilo. ¿Cuántas tiras van en cada hilo?", "18//3", "Se reparten en partes iguales."),
        ex("¿Qué cartela está mejor armada? A. «Corriente de papel. Autoría: (tu nombre). Materiales: diario usado e hilo. Quise mostrar una lluvia que cae» B. «Mi instalación».", "A", "Tiene título, autoría, materiales y explicación."),
        ex("Tu instalación usa 4 metros de pasillo con 5 objetos por metro. ¿Cuántos objetos necesitas?", "20", "4 por 5 son 20 objetos."),
    ],
    [
        ex("Intención: que el público quede rodeado de objetos. Planta A: el recorrido pasa junto a todos los objetos. Planta B: el recorrido pasa por un lado y no toca ningún objeto. ¿Cuál sirve?", "La planta A", "Rodea al público con los objetos."),
        ex("Pasas tu instalación de un pasillo de 6 m a un rincón de 2 m. ¿Qué debes revisar primero? A. Cuántos objetos caben y si el recorrido sigue libre B. Si el título de la obra cabe en la cartela.", "A", "El tamaño del espacio afecta la cantidad y el recorrido."),
    ],
    [
        arith("El espacio mide 400 cm de largo. Dejas 80 cm de entrada libre y 80 cm de salida libre. ¿Cuántos centímetros quedan para los objetos?", "400-80-80", "Se restan la entrada y la salida del largo total."),
        ex("Dos cartelas. X: «Representa a todas las personas de la ciudad». Y: «Muestra una forma de mirar los residuos de mi casa». ¿Cuál evita generalizar?", "Y", "Habla de un punto de vista concreto."),
    ],
    ex("Quieres montar una instalación mínima en el pasillo de tu casa durante una tarde. ¿Qué haces antes? A. Avisar a una persona adulta y elegir un lugar sin cables ni escaleras B. Montarla de noche sin avisar.", "A", "La seguridad exige avisar y revisar el lugar."),
    [
        ex("¿Cuáles son los seis pasos para crear una instalación propia, en orden?", "Intención, espacio y objetos, plano, montaje, documentación y desmontaje", "Es el orden de trabajo de la clase."),
        ex("Verdadero o falso: la instalación que montas en tu casa se deja puesta para siempre.", "Falso", "En esta clase se monta por un tiempo y se desmonta."),
        ex("¿Qué es una cartela?", "La etiqueta con título, autoría, materiales y explicación breve", "Acompaña la obra."),
    ],
    task(
        "Elige UNA intención. A) Que quien pase se sienta bajo una lluvia de papeles. B) Que quien entre sienta que un lugar está preparado pero sin gente. C) Que quien mire sienta que muchos objetos iguales lo observan. Elige un lugar seguro de tu casa, dibuja el plano en planta con escala, haz el montaje con objetos livianos, documéntalo con tres dibujos o fotos (entrada, centro y fondo), escribe la cartela con título, autoría, materiales y explicación, y desmonta al final.",
        "Elegí la A. Lugar: pasillo, 120 cm de ancho, camino libre de 80 cm. Objetos: 18 papeles de diario colgados de hilos a alturas distintas. Documenté desde la entrada, el centro y el fondo. Cartela: «Lluvia de diarios. Autoría: (mi nombre). Materiales: diario e hilo. Quise mostrar una lluvia que cae». Desmonté y guardé el diario.",
        ["escribe una intención específica", "dibuja el plano y deja camino libre", "documenta desde tres puntos de vista", "completa la cartela y desmonta"],
        ["plano", "montaje documentado", "cartela", "desmontaje"],
        ["no dejar camino libre", "documentar desde un solo lugar"],
        "Señala una decisión del plano y pregunta cómo se ve en el montaje.",
    ),
    "Cuenta a una persona de tu casa tu intención en una frase y pídele que adivine qué objetos usarías.",
    "Escribe una segunda cartela para la misma instalación dirigida a niños de primero básico, con palabras simples.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Tu documentación de la clase anterior, hojas y lápiz. Si no la tienes, usa la instalación descrita en esta clase.",
    "Aprenderé a comparar la intención de mi instalación con el efecto que produce en quien la recorre, usando sus respuestas y mi documentación. Sirve para revisar con evidencia y mejorar una instalación.",
    ["Sé documentar una instalación desde tres puntos de vista.", "Sé que el efecto es lo que percibe quien mira."],
    [
        "En una instalación el efecto lo vive quien la recorre. Para comprobarlo le pido que la recorra sin explicarle nada y que me cuente qué sintió, qué notó primero y qué le pareció que quería decir. Anoto sus respuestas tal como las dice y las comparo con mi intención. Mi documentación, es decir, los dibujos o fotos desde varios puntos de vista, me ayuda a revisar qué decisión produjo cada efecto.",
        "Si el efecto no coincide, reviso las variables de la instalación: la cantidad de objetos, la altura, la luz, el recorrido y la distancia entre las cosas. Cambio una sola y vuelvo a pedir un recorrido. Por ejemplo, si quería sensación de multitud y la gente dijo «hay pocos objetos», aumento la cantidad. Si un objeto clave no se nota porque está en un fondo oscuro, cambio la luz o la ubicación, no el título.",
        "Mantengo la seguridad como criterio: una instalación que logra su efecto pero tiene un recorrido peligroso debe corregirse primero. Y respeto las respuestas distintas: dos personas pueden sentir cosas diferentes, y pregunto qué detalle las llevó a eso. Con ayuda de las respuestas decido qué conservar y qué cambiar, y puedo explicar mi decisión con evidencia, sin generalizar a más gente de la que consulté.",
    ],
    [("efecto", "lo que percibe o siente quien recorre la obra"), ("documentación", "registro de la obra desde varios puntos de vista"), ("evidencia", "respuesta o dato que permite comprobar algo"), ("variable", "decisión que se puede cambiar, como cantidad, altura o luz"), ("generalizar", "afirmar algo para muchas personas a partir de unas pocas respuestas")],
    [
        w("Contrastar", "Intención: transmitir calma. Cuatro personas recorren tu instalación: tres dicen «tranquilo» y una dice «apretado». ¿Cuántas percibieron el efecto?", ["«Tranquilo» coincide con calma.", "«Apretado» no coincide.", "Cuento las que coinciden."], "3 de 4"),
        w("Decidir un cambio", "Intención: invitar a entrar. Efecto: la gente dice que «no se nota desde la puerta», porque todos los objetos están al fondo. ¿Qué cambio de una sola variable haces?", ["La causa probable es la ubicación de los objetos.", "Muevo algunos objetos hacia la entrada sin cambiar nada más.", "Vuelvo a pedir un recorrido a las mismas personas."], "Mover algunos objetos hacia la entrada y volver a consultar"),
    ],
    [
        m("Explicar la instalación antes del recorrido y luego preguntar si se entiende.", "La explicación tapa lo que la obra produce por sí sola.", "Pide el recorrido primero y pregunta qué sintió y notó."),
        m("Concluir que el cambio funciona para toda la ciudad porque lo aprobaron tres personas.", "Tres respuestas no representan a mucha gente.", "Di que funcionó para las personas consultadas."),
    ],
    [
        ex("Intención: sentirse rodeado. Una persona dice «la miré desde afuera». ¿Coinciden intención y efecto?", "No", "No sintió estar dentro de la obra."),
        ex("Antes de explicar tu instalación, ¿qué le pides a la persona? A. Que la recorra y diga qué siente B. Que lea tu intención escrita.", "A", "Así el efecto no se mezcla con tu explicación."),
        ex("¿Qué es la documentación de una instalación?", "El registro con dibujos o fotos desde varios puntos de vista", "Permite revisar la obra después."),
    ],
    [
        ex("Intención: rodeado. Tres personas la recorren: dos dicen «rodeado» y una dice «espacio vacío». ¿Cuántas percibieron el efecto buscado?", "2", "Solo dos respuestas coinciden con la intención."),
        ex("La gente no nota un objeto clave porque está en un fondo oscuro. ¿Qué variable cambias? A. La luz o la ubicación del objeto B. El título de la obra.", "A", "El problema es de visibilidad, no del título."),
        ex("Intención: sensación de multitud. Efecto: «hay pocos objetos». ¿Qué cambio de una variable ayuda? A. Aumentar la cantidad de objetos B. Cambiar solo la cartela.", "A", "La cantidad de objetos produce la sensación de multitud."),
    ],
    [
        arith("Versión 1 con 12 objetos: 4 de 10 personas sintieron multitud. Versión 2 con 24 objetos: 8 de 10. ¿Cuántas personas más sintieron multitud en la versión 2?", "8-4", "Se compara la cantidad en cada versión."),
        arith("Antes, la entrada tenía 60 cm entre objetos y la gente dijo «incómodo». Para lograr un ambiente acogedor la ampliaste a 90 cm. ¿Cuántos centímetros más tiene?", "90-60", "Se resta la medida anterior a la nueva."),
        ex("Al ver tus fotos desde el fondo notas que se ve una pared vacía. ¿Qué cambio ayuda? A. Mover un grupo de objetos hacia esa pared B. Quitar todos los objetos.", "A", "Se llena la zona vacía sin perder la obra."),
    ],
    [
        ex("En la prueba 1 había 10 objetos y poca luz. En la prueba 2, 20 objetos y más luz, y mejoró la sensación de multitud. ¿Puedes saber si la causa fue la cantidad o la luz?", "No", "Cambiaron dos variables a la vez."),
        ex("Una persona dice que tu instalación le da miedo, y tu intención era la ternura. ¿Qué haces? A. Preguntarle qué detalle le dio miedo y probar un cambio B. Decirle que se equivoca.", "A", "Su respuesta es evidencia útil."),
    ],
    [
        ex("Instalación X logra su intención, pero su recorrido es angosto y se tropieza. Instalación Y no logra la intención, pero es segura. ¿Cuál debe corregir primero?", "La X, por seguridad", "La seguridad va primero, aunque logre la intención."),
        ex("Antes del cambio 1 de 4 personas sintió multitud; después, 3 de 4. ¿Qué conclusión es válida? A. El cambio mejoró el efecto para esas personas B. El cambio funciona para toda la ciudad.", "A", "Cuatro personas no representan a toda la ciudad."),
    ],
    ex("Tu instalación de papeles colgados de hilos busca que se sienta una lluvia. Dos compañeros la recorren y dicen «parece una cortina». ¿Qué variable cambias? A. Separar los papeles y colgarlos a distintas alturas B. Cambiar el color del hilo.", "A", "Una cortina es una fila pareja; la lluvia necesita alturas distintas."),
    [
        ex("En una instalación, ¿qué es el efecto?", "Lo que percibe o siente quien la recorre", "Puede coincidir o no con la intención."),
        ex("Verdadero o falso: si tres personas aprueban tu cambio, funciona para toda la ciudad.", "Falso", "Tres respuestas no representan a mucha gente."),
        ex("¿Qué pides a la persona antes de explicar tu instalación?", "Que la recorra y cuente qué sintió y qué notó", "Así comparas el efecto con tu intención."),
    ],
    task(
        "Usa tu instalación de la clase anterior. Si no la tienes, usa esta de ejemplo: 12 papeles de diario colgados de hilos a la misma altura en un pasillo, con la intención «que se sienta una lluvia». Pide a dos personas que la recorran sin explicarla, anota qué sintieron y qué notaron, compara con tu intención, cambia UNA variable (cantidad, altura o luz) y vuelve a pedir un recorrido.",
        "Persona 1: «parece una cortina». Persona 2: «me gustó, es ordenada». Intención: lluvia. Efecto: no coincide. Cambio: colgar los papeles a alturas distintas. Segunda ronda: la persona 1 dice «ahora cae como lluvia». Seguridad: el camino sigue libre.",
        ["anota las respuestas sin explicar", "compara efecto e intención", "cambia solo una variable", "registra la nueva respuesta y revisa la seguridad"],
        ["respuestas anotadas", "variable cambiada", "segunda ronda"],
        ["explicar antes del recorrido", "cambiar varias variables a la vez"],
        "Pregunta qué variable cambió y qué respuesta nueva comprueba que funcionó.",
    ),
    "Pide a una persona de tu casa que recorra tu montaje y te diga lo primero que notó, sin que le expliques nada.",
    "Escribe qué otra variable cambiarías después y qué efecto esperas lograr con ese cambio.",
)

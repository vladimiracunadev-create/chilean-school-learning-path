"""Cuaderno del estudiante, 2.º básico Tecnología: OA 05 (dibujo digital) y OA 06 (procesador de textos)."""
from __future__ import annotations

from student_lessons import ex, register

OA5, OA6 = "TE02 OA 05", "TE02 OA 06"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [ex(*i) for i in R], "understand": [ex(*i) for i in C], "apply": [ex(*i) for i in A], "reason": [ex(*i) for i in Z], "challenge": [ex(*i) for i in D]},
        context=[ex(*ctx)], selfcheck=[ex(*i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )




# ------------------------------------------------------------------ OA 05
# Las pantallas de software se describen con texto y son EJEMPLOS FICTICIOS: cada programa real se ve algo distinto.
reg(
    OA5, 1,
    materials="Un programa de dibujo del colegio o del computador, sin cuenta ni registro. Si no hay dispositivo, usa papel: dibuja el ejemplo con lápiz y borrador.",
    use="Aprenderé a usar las herramientas básicas de un programa de dibujo: lápiz, borrador, relleno, formas, color, grosor y deshacer. Sirve para dibujar mis ideas en la pantalla.",
    prior=["Sé dibujar a mano alzada.", "Sé que un boceto muestra una idea."],
    explain=[
        "Un software de dibujo es un programa para hacer imágenes en una pantalla. Casi todos tienen una barra de herramientas con botones pequeños. Cada botón hace una cosa. En el ejemplo ficticio de esta clase, la barra está a la izquierda y los colores abajo.",
        "Las herramientas básicas son estas. El lápiz dibuja líneas. El borrador quita lo dibujado. El relleno pinta un espacio cerrado con un color. Las formas dibujan círculos, cuadrados o líneas rectas. El color y el grosor cambian cómo se ve la línea. El botón deshacer borra el último paso.",
        "Para dibujar un objeto, elige la herramienta, elige el color y mueve el puntero sobre la hoja. Si te equivocas, usa deshacer en vez de borrar todo. Cada programa se ve distinto, pero las herramientas cumplen las mismas funciones.",
    ],
    vocab=[("software", "programa que se usa en un computador"), ("herramienta", "botón del programa que hace una acción"), ("relleno", "herramienta que pinta un espacio cerrado"), ("deshacer", "botón que borra el último paso"), ("puntero", "flecha o punto que mueves en la pantalla")],
    worked=[
        ("Elegir una herramienta", "Quieres pintar de azul el interior de un círculo ya dibujado. ¿Qué herramienta eliges?", ["El círculo está cerrado.", "Quiero cubrir todo su interior.", "La herramienta que hace eso es el relleno."], "El relleno, con el color azul"),
        ("Corregir un error", "Dibujaste una línea chueca por error. ¿Qué haces primero?", ["Veo que fue el último paso.", "Uso el botón deshacer.", "Vuelvo a dibujar la línea."], "Usar deshacer para borrar el último paso"),
    ],
    mistakes=[
        ("Borrar todo el dibujo por un error pequeño.", "Pierdes lo que estaba bien.", "Usa deshacer o el borrador solo en esa parte."),
        ("Usar el lápiz para pintar un espacio grande.", "Es lento y deja huecos.", "Usa el relleno en un espacio cerrado."),
    ],
    R=[
        ("En el ejemplo ficticio hay un botón con forma de goma. ¿Sirve para dibujar o para borrar?", "Para borrar", "La goma es el borrador."),
        ("El relleno pinta un espacio cerrado. ¿Un círculo con la línea cortada es cerrado o abierto?", "Abierto", "Si hay un hueco, el color se escapa."),
        ("¿Para cambiar lo grueso de la línea usas el color o el grosor?", "El grosor", "El grosor cambia cuán ancha es la línea."),
    ],
    C=[
        ("¿Qué hace el botón deshacer?", "Borra el último paso", "Vuelve atrás una acción."),
        ("¿Para qué sirve la barra de herramientas?", "Para elegir qué acción hará el puntero", "Cada botón hace una acción distinta."),
        ("Quieres una línea recta perfecta. ¿Usas la herramienta de formas o el lápiz a mano alzada?", "La herramienta de formas", "Las formas dibujan líneas rectas."),
    ],
    A=[
        ("Tienes un cuadrado cerrado en la pantalla. Quieres pintarlo de rojo. Elige la secuencia: herramienta relleno, color rojo, clic dentro del cuadrado, o color rojo y lápiz por fuera.", "Relleno, color rojo, clic dentro del cuadrado", "El relleno pinta el interior."),
        ("Dibujaste un sol amarillo y sin querer pintaste una línea verde sobre él. Fue lo último que hiciste. ¿Qué botón usas para volver atrás ese paso?", "Deshacer", "Deshacer vuelve atrás el último paso."),
        ("Quieres dibujar tres círculos del mismo tamaño. ¿Conviene la herramienta de formas o el lápiz?", "La herramienta de formas", "Los círculos de formas salen parejos."),
    ],
    Z=[
        ("Un niño dice: «Si me equivoco, empiezo de nuevo». ¿Qué le dices?", "Que use deshacer para volver atrás un paso", "Así no pierde lo que está bien."),
        ("Pintas un rectángulo con el relleno y se pinta toda la hoja. ¿Qué pasó con el rectángulo?", "Tenía un hueco y el color se escapó", "El relleno exige espacio cerrado."),
    ],
    D=[
        ("Quieres dibujar una casa: un cuadrado de pared, un triángulo de techo y rellenar la pared de café. Escribe las herramientas en orden.", "Formas (cuadrado), formas (triángulo), color café, relleno en la pared", "Primero se dibuja y luego se pinta."),
        ("En una pantalla ficticia el botón del lápiz tiene un número 3 y otro botón tiene 10. ¿Cuál línea será más gruesa: la de 3 o la de 10?", "La de 10", "Un número mayor indica más grosor."),
    ],
    ctx=("Mati dibuja un bote en el programa. Hace el casco con una forma, pero la vela triangular le queda un poco chueca. Escribe qué botón usa para corregir el último trazo y qué herramienta usa para pintar la vela de amarillo.", "Usa deshacer; luego relleno con color amarillo", "Corrige con deshacer y pinta con relleno."),
    sc=[
        ("¿Qué hace el relleno?", "Pinta un espacio cerrado", "Cubre el interior."),
        ("¿Deshacer borra el último paso?", "Sí", "Es su función."),
        ("¿Todas las pantallas se ven iguales?", "No", "Cada programa se ve distinto."),
    ],
    open_task=(
        "Con un programa de dibujo (o con papel y lápiz si no hay dispositivo), dibuja un bote con estas herramientas: formas para el casco y la vela, relleno para pintarlos, y deshacer (o borrador en papel) para corregir un trazo. Escribe qué herramienta usaste para cada cosa.",
        "Casco: forma (rectángulo) y relleno café. Vela: forma (triángulo) y relleno amarillo. Corregí una línea con deshacer.",
        ["dibuja un bote", "usa formas, relleno y deshacer", "nombra la herramienta de cada parte"],
        ["dibujo en pantalla o papel", "lista de herramientas"],
        ["usar el lápiz para todo", "no cerrar la figura antes de rellenar"],
        "Pregunta: «¿qué herramienta usaste aquí y por qué?». Si no cerró la figura, repite el relleno.",
    ),
    reinforce="Recorre la barra de herramientas de un programa de dibujo y prueba cada botón una vez.",
    extend="Dibuja un paisaje con tres formas distintas y dos colores.",
)

reg(
    OA5, 2,
    materials="Un programa de dibujo sencillo o papel y lápices de colores. En papel, simula las capas con hojas transparentes o papel vegetal.",
    use="Aprenderé que lo que dibujo después queda sobre lo que dibujé antes. Sirve para ordenar un dibujo en planos: fondo, medio y frente.",
    prior=["Sé usar las herramientas básicas de dibujo.", "Sé que deshacer vuelve un paso atrás."],
    explain=[
        "Un dibujo digital puede tener capas. Una capa es como una hoja transparente puesta sobre otra. Lo que está en la capa de arriba tapa lo que está debajo. Algunos programas sencillos no muestran capas, pero el orden sigue funcionando: lo último que dibujas queda arriba.",
        "Piensa en un paisaje. El fondo es el cielo y el pasto. En el medio va una casa. Adelante va un árbol que tapa parte de la casa. Dibuja primero el fondo, después el medio y al final el frente. Si lo haces al revés, lo de adelante queda tapado.",
        "Si algo quedó tapado, puedes usar deshacer y volver a hacerlo en otro orden. Pensar el orden antes de dibujar ahorra trabajo. Anota en papel: 1 fondo, 2 medio, 3 frente.",
    ],
    vocab=[("capa", "hoja transparente puesta sobre otra"), ("fondo", "lo que se ve más atrás"), ("frente", "lo que se ve más adelante"), ("tapar", "cubrir algo y no dejar verlo"), ("orden", "qué se dibuja primero y qué después")],
    worked=[
        ("Ordenar un paisaje", "Quieres dibujar: un sol, una casa y un árbol que tapa parte de la casa. ¿En qué orden dibujas?", ["El sol está al fondo.", "La casa va en medio.", "El árbol va al frente porque tapa la casa."], "Sol, casa, árbol"),
        ("Arreglar un tapado", "Dibujaste un árbol y luego una casa que lo tapó, pero querías el árbol delante. ¿Qué haces?", ["Deshago hasta antes de la casa.", "Dibujo la casa primero.", "Dibujo el árbol después."], "Dibujar primero la casa y después el árbol"),
    ],
    mistakes=[
        ("Dibujar primero lo que va adelante.", "Después lo de atrás lo tapa.", "Dibuja del fondo hacia el frente."),
        ("Cubrir el fondo con un trazo ancho al final.", "El trazo del fondo tapa lo que ya hiciste.", "Pinta el fondo primero."),
    ],
    R=[
        ("El cielo está al fondo. ¿Se dibuja primero o al final?", "Primero", "Lo del fondo va primero."),
        ("Una capa es como una hoja transparente. ¿Tapa a las de abajo?", "Sí", "Lo de arriba tapa lo de abajo."),
        ("Un árbol delante de una casa, ¿se dibuja antes o después de la casa?", "Después", "Debe quedar encima."),
    ],
    C=[
        ("¿Por qué conviene dibujar del fondo al frente?", "Porque lo de adelante queda encima y no lo tapa nada", "Sigue el orden de las capas."),
        ("¿Qué pasa si pintas un trazo ancho de color azul sobre una nube ya dibujada?", "La nube queda tapada", "Lo que se pinta después cubre lo anterior."),
        ("¿Qué botón usas si el orden quedó mal?", "Deshacer", "Vuelve atrás para ordenar."),
    ],
    A=[
        ("Quieres dibujar un pez, el mar y una piedra delante del pez. Escribe el orden de abajo hacia arriba.", "Mar, pez, piedra", "Del fondo al frente."),
        ("Un niño dibujó el pasto al final y tapó los pies de una niña. ¿Qué debió hacer?", "Dibujar el pasto antes que la niña", "El pasto es el fondo."),
        ("Quieres una luna detrás de una torre. ¿Cuál dibujas primero?", "La luna", "La luna está detrás de la torre."),
    ],
    Z=[
        ("Ana dice: «Da lo mismo el orden, todo se ve igual». Dibuja una casa y un árbol: ¿da lo mismo? Explica.", "No, porque el segundo tapa al primero", "El orden decide qué se ve."),
        ("Un dibujo tiene cielo, montaña y nube. La nube tapa la cima de la montaña. ¿Qué se dibujó antes: la nube o la montaña?", "La montaña", "La nube está encima."),
    ],
    D=[
        ("Escribe el orden de dibujo de cuatro cosas: un cielo, una montaña delante del cielo, una casa delante de la montaña y una flor delante de la casa.", "Cielo, montaña, casa, flor", "Del fondo al frente."),
        ("Una casa se dibujó sobre un camino y lo tapó. ¿Cómo logras ver el camino delante de la casa?", "Dibujando la casa primero y el camino después", "El camino debe quedar encima."),
    ],
    ctx=("Eli quiere dibujar una granja: un cielo azul, un establo, una vaca delante del establo y una cerca delante de la vaca. Escribe el orden de dibujo.", "Cielo, establo, vaca, cerca", "Del fondo al frente."),
    sc=[
        ("¿Lo último que dibujas queda arriba?", "Sí", "Tapa lo que hay debajo."),
        ("¿El fondo se dibuja primero?", "Sí", "Va detrás de todo."),
        ("¿Una capa es una hoja transparente?", "Sí", "Así la imaginamos."),
    ],
    open_task=(
        "Dibuja un paisaje con tres planos: fondo (cielo y sol), medio (una casa) y frente (un árbol que tape parte de la casa). Primero escribe el orden en una lista: 1, 2 y 3. Hazlo en un programa de dibujo o en papel. Si el árbol queda tapado, corrige el orden.",
        "Orden: 1 sol y cielo, 2 casa, 3 árbol. El árbol tapa la puerta de la casa.",
        ["escribe el orden antes", "dibuja del fondo al frente", "el árbol tapa parte de la casa"],
        ["lista del orden", "dibujo terminado"],
        ["dibujar primero el frente", "pintar el fondo al final"],
        "Pregunta: «¿qué dibujaste primero y por qué?». Si el orden estuvo mal, pide que lo corrija.",
    ),
    reinforce="Con dos hojas de papel, una transparente, prueba cómo una tapa a la otra.",
    extend="Dibuja un paisaje con cuatro planos y escribe el orden.",
)

reg(
    OA5, 3,
    materials="Programa de dibujo o papel y lápices. Usa el diseño de un objeto que hiciste en la clase de diseño, o el de este cuaderno.",
    use="Aprenderé a representar un diseño con formas, color y texto en la pantalla. Sirve para mostrar partes y uso de un objeto.",
    prior=["Sé dibujar con formas y rellenar.", "Sé que las etiquetas nombran partes."],
    explain=[
        "Un software de dibujo sirve para mostrar un diseño. Para eso se usan formas simples: un cuadrado para el cuerpo, un círculo para una rueda, una línea para un asa. Cada forma representa una parte del objeto.",
        "Después se agrega color. El color puede indicar el material o ayudar a distinguir partes. Y se agrega texto con la herramienta de texto, que escribe letras sobre la hoja. Así puedes poner etiquetas como «asa» o «base» y medidas como «12 cm».",
        "Un buen dibujo comunica sin explicación. Revisa estas preguntas: ¿se ven las partes?, ¿están nombradas?, ¿hay una medida con unidad? Si falta algo, agrégalo. La medida que escribes es la del objeto real, no la del tamaño del dibujo en la pantalla. Un dibujo claro ayuda a que otra persona construya tu objeto.",
    ],
    vocab=[("representar", "mostrar una idea con un dibujo"), ("forma simple", "figura básica, como cuadrado o círculo"), ("herramienta de texto", "botón que permite escribir letras en la hoja"), ("etiqueta", "nombre de una parte"), ("comunicar", "hacer que otra persona entienda")],
    worked=[
        ("Elegir formas", "Quieres dibujar un carrito: una caja y dos ruedas. ¿Qué formas usas?", ["La caja es un rectángulo.", "Las ruedas son redondas.", "Uso un rectángulo y dos círculos."], "Un rectángulo y dos círculos"),
        ("Agregar etiquetas", "En tu dibujo del carrito ya están las formas. ¿Qué agregas para que se entienda?", ["Escribo «caja» y «rueda» con la herramienta de texto.", "Escribo la medida «12 cm» con su unidad.", "Reviso que se lea bien."], "Etiquetas «caja» y «rueda» y la medida 12 cm"),
    ],
    mistakes=[
        ("Dibujar solo con líneas confusas.", "No se ven las partes.", "Usa formas simples para cada parte."),
        ("Escribir una medida sin unidad.", "Falta información.", "Escribe número y unidad: 12 cm."),
    ],
    R=[
        ("Una rueda es redonda. ¿Qué forma usas: círculo o cuadrado?", "Círculo", "El círculo es redondo."),
        ("Para escribir una etiqueta usas el texto. ¿Es la herramienta de texto o el borrador?", "La herramienta de texto", "Esa herramienta escribe letras."),
        ("«12 cm» tiene número y unidad. ¿Está completa?", "Sí", "Lleva número y unidad."),
    ],
    C=[
        ("¿Para qué sirven las formas simples en un diseño?", "Para representar las partes del objeto", "Cada forma es una parte."),
        ("¿Qué ayuda a distinguir el material en un dibujo?", "El color", "Un color distinto muestra otro material."),
        ("¿Por qué un diseño debe tener etiquetas?", "Para que otra persona entienda cada parte", "Nombran lo que se ve."),
    ],
    A=[
        ("Un portalápices: cuerpo cilíndrico y base. ¿Qué formas usas en la vista de frente: rectángulos o círculos?", "Rectángulos", "De frente un cilindro se ve como rectángulo."),
        ("Un diseño de barco tiene casco, vela y mástil. Escribe las tres etiquetas.", "Casco, vela y mástil", "Son las partes que se nombran."),
        ("Quieres decir que la vela mide 8 cm de alto. ¿Cómo lo escribes?", "8 cm", "Número y unidad."),
    ],
    Z=[
        ("Un dibujo digital tiene formas pero sin etiquetas ni medidas. ¿Un compañero podría construirlo? Explica.", "Difícil, porque no sabe los nombres ni los tamaños", "Le faltan datos."),
        ("Pía pintó todas las partes del mismo color. ¿Qué problema puede tener?", "No se distinguen las partes", "El color ayuda a diferenciar."),
    ],
    D=[
        ("Diseña con palabras un carrito en pantalla: lista tres formas, dos etiquetas y una medida con unidad.", "Rectángulo, dos círculos, un triángulo; etiquetas caja y rueda; medida 12 cm", "Cumple lo pedido."),
        ("Un dibujo mide 6 cm de ancho en pantalla pero el objeto real mide 12 cm. ¿Cuál medida escribes en el dibujo?", "12 cm", "Se escribe la medida del objeto real."),
    ],
    ctx=("Rafa dibuja en pantalla un soporte para fichas: una base rectangular y dos paredes. Quiere que su compañera lo entienda sin hablarle. ¿Qué tres cosas agrega además de las formas?", "Color, etiquetas y medidas con unidad", "Hacen el dibujo claro."),
    sc=[
        ("¿Las formas simples representan partes?", "Sí", "Cada forma es una parte."),
        ("¿La herramienta de texto escribe letras?", "Sí", "Sirve para etiquetas."),
        ("¿Una medida lleva unidad?", "Sí", "Número y unidad."),
    ],
    open_task=(
        "Representa en un programa de dibujo (o en papel) un portalápices: dibuja la vista de frente con formas, usa dos colores, escribe dos etiquetas con la herramienta de texto y una medida con unidad (por ejemplo 10 cm de alto).",
        "Rectángulo para el cuerpo (café), rectángulo para la base (azul). Etiquetas: cuerpo y base. Medida: 10 cm de alto.",
        ["usa formas simples", "usa dos colores", "escribe dos etiquetas", "escribe una medida con unidad"],
        ["dibujo con etiquetas y medida"],
        ["medida sin unidad", "partes sin nombre"],
        "Pregunta: «¿se entiende cada parte sin que expliques?». Si falta una etiqueta, pide agregarla.",
    ),
    reinforce="Dibuja un objeto de tu casa con tres formas simples.",
    extend="Agrega la vista de arriba de tu objeto.",
)

reg(
    OA5, 4,
    materials="Programa de dibujo o papel y lápices. Un dibujo ya hecho, por ejemplo el portalápices de la clase anterior.",
    use="Aprenderé a hacer variantes rápidas de un dibujo cambiando color, tamaño o posición sin perder la primera versión. Sirve para comparar ideas.",
    prior=["Sé representar un diseño con formas.", "Sé que una prueba cambia una sola variable."],
    explain=[
        "Una variante es una versión del dibujo con un cambio. Puedes cambiar el color, el tamaño o la posición de una parte. Así comparas qué se ve mejor sin empezar desde cero.",
        "Antes de cambiar nada, guarda una copia del original. En muchos programas se usa «Guardar como» con otro nombre. Si algo sale mal, tu primera versión sigue intacta. Cambia una sola cosa por variante, como en las pruebas.",
        "Anota qué cambiaste en cada variante. Por ejemplo: variante 1, color rojo; variante 2, base más ancha; variante 3, asa a la derecha. Luego mira las tres y elige la mejor según tus criterios.",
    ],
    vocab=[("variante", "versión de un dibujo con un cambio"), ("original", "la primera versión"), ("copia", "otra versión igual guardada aparte"), ("posición", "el lugar donde está una parte"), ("tamaño", "qué tan grande es una parte")],
    worked=[
        ("Hacer una variante de color", "Tu dibujo tiene la base azul. Haces la variante 1 con la base roja. ¿Qué cambiaste?", ["Miro qué es distinto.", "Solo el color de la base.", "El resto sigue igual."], "Solo el color de la base"),
        ("Proteger el original", "Quieres probar una variante. ¿Qué haces antes de cambiar el dibujo?", ["Pienso en el original.", "Guardo una copia con otro nombre.", "Trabajo la variante en la copia."], "Guardar una copia con otro nombre"),
    ],
    mistakes=[
        ("Cambiar el original sin guardar copia.", "No puedes volver a la primera idea.", "Guarda una copia con otro nombre antes de cambiar."),
        ("Cambiar color, tamaño y posición a la vez.", "No sabes qué mejoró.", "Cambia una sola cosa por variante."),
    ],
    R=[
        ("Una variante tiene un cambio. ¿Tiene un cambio o muchos?", "Un cambio", "Se cambia una sola cosa."),
        ("Antes de cambiar, ¿guardas una copia o no?", "Guardas una copia", "Protege el original."),
        ("El color rojo en lugar del azul, ¿es un cambio de color o de posición?", "De color", "Cambió el color."),
    ],
    C=[
        ("¿Por qué conviene guardar una copia del original?", "Para no perder la primera versión", "Si falla, puedes volver."),
        ("Nombra tres cosas que se pueden cambiar en una variante.", "Color, tamaño y posición", "Son los cambios de esta clase."),
        ("¿Para qué sirve comparar variantes?", "Para elegir la que se ve mejor", "Se decide con evidencia."),
    ],
    A=[
        ("Variante 1: el techo de la casa pasa de azul a rojo. ¿Qué cambió: color, tamaño o posición?", "Color", "Solo el tono del techo."),
        ("Variante 2: la puerta es el doble de ancha. ¿Qué cambió?", "El tamaño", "La puerta es más ancha."),
        ("Variante 3: la ventana pasa del lado izquierdo al derecho. ¿Qué cambió?", "La posición", "Cambió de lugar."),
    ],
    Z=[
        ("Un niño cambió el color y el tamaño de la base a la vez y le gustó más. ¿Sabe cuál cambio ayudó? Explica.", "No, porque cambió dos cosas", "No se separa el efecto de cada uno."),
        ("Sol perdió su primera idea porque guardó el cambio encima de ella. ¿Qué debió hacer?", "Guardar una copia con otro nombre", "Así conserva el original."),
    ],
    D=[
        ("Haz una tabla de tres variantes de un portalápices: variante, qué cambió y qué se ve distinto.", "V1 color rojo; V2 base más ancha; V3 asa a la derecha", "Cada variante cambia una sola cosa."),
        ("Las variantes son V1 color rojo, V2 base más ancha y V3 asa a la derecha. El criterio es «la base debe verse estable». ¿Cuál eliges y por qué?", "La base más ancha, porque se ve más estable", "Cumple el criterio."),
    ],
    ctx=("Lía tiene el dibujo de un carrito con ruedas pequeñas. Quiere probar ruedas grandes sin perder el carrito original. Escribe sus dos pasos.", "Guarda una copia con otro nombre; luego agranda las ruedas en la copia", "Protege el original y cambia una variable."),
    sc=[
        ("¿Una variante cambia una cosa?", "Sí", "Se cambia una por vez."),
        ("¿Se guarda una copia antes de cambiar?", "Sí", "Protege el original."),
        ("¿Cambiar el tamaño es una variante?", "Sí", "Es uno de los cambios."),
    ],
    open_task=(
        "Con tu dibujo de un carrito (una caja y dos ruedas), haz tres variantes rápidas: V1 cambia el color de la caja, V2 agranda las ruedas, V3 mueve la caja a la izquierda. Guarda una copia antes de cada variante. Elige cuál se ve mejor y di por qué.",
        "V1 caja verde; V2 ruedas más grandes; V3 caja a la izquierda. Elijo V2 porque parece avanzar mejor.",
        ["guarda una copia del original", "cambia una sola cosa por variante", "hace tres variantes", "elige una con una razón"],
        ["tres dibujos o hojas", "frase con la elección"],
        ["cambiar varias cosas a la vez", "perder el original"],
        "Pregunta: «¿qué cambiaste en cada variante?». Si cambió más de una cosa, repite.",
    ),
    reinforce="Haz una variante de color de un dibujo que ya tengas.",
    extend="Haz cuatro variantes y escribe un criterio para elegir la mejor.",
)

reg(
    OA5, 5,
    materials="Un programa de dibujo con las opciones Guardar, Guardar como y Abrir, o una carpeta en papel con hojas rotuladas. No uses cuentas personales.",
    use="Aprenderé a guardar un dibujo con un buen nombre, saber dónde quedó y abrirlo de nuevo. Sirve para no perder mi trabajo.",
    prior=["Sé hacer variantes de un dibujo.", "Sé que una carpeta guarda archivos."],
    explain=[
        "Un archivo es un trabajo guardado en el dispositivo. Para guardarlo, usa Guardar o Guardar como. Guardar actualiza el mismo archivo. Guardar como crea otro con otro nombre. Siempre elige un nombre claro y la carpeta donde quedará.",
        "Un buen nombre dice qué es, como «casa_variante1». No uses tu nombre completo, tu dirección ni tu teléfono. No uses tildes ni espacios si el programa te lo pide. Elige la carpeta que te indicó tu profesor o profesora.",
        "Para recuperar, abre el programa, usa Abrir, busca la carpeta y elige el nombre. Comprueba que el dibujo sea el que querías. Guarda de vez en cuando mientras trabajas, así no pierdes todo si se apaga el equipo. Si no hay dispositivo, rotula la hoja y guárdala en una carpeta de papel.",
    ],
    vocab=[("archivo", "trabajo guardado con un nombre"), ("carpeta", "lugar donde se guardan archivos"), ("guardar", "mantener el trabajo en el dispositivo"), ("guardar como", "guardar una copia con otro nombre"), ("abrir", "traer un archivo guardado a la pantalla")],
    worked=[
        ("Elegir un buen nombre", "Dibujaste una casa y harás una variante. ¿Qué nombre eliges: «dibujo1», «casa_variante1» o «Ana Pérez 5 Av. Sur»?", ["El nombre debe decir qué es.", "El tercero lleva datos personales.", "El primero no dice nada."], "casa_variante1"),
        ("Recuperar el archivo", "Ayer guardaste «casa_variante1» en la carpeta «Tecnología». ¿Cómo lo abres hoy?", ["Abro el programa.", "Uso Abrir y busco la carpeta Tecnología.", "Elijo casa_variante1."], "Abrir, carpeta Tecnología, casa_variante1"),
    ],
    mistakes=[
        ("Poner el nombre completo y la dirección en el nombre del archivo.", "Son datos personales.", "Usa un nombre que diga qué es el dibujo."),
        ("Guardar y no recordar la carpeta.", "No lo encuentras después.", "Anota la carpeta o usa la que indicó el profesor."),
    ],
    R=[
        ("Guardar como crea otra versión con otro nombre. ¿Verdadero o falso?", "Verdadero", "Esa es su función."),
        ("¿Un buen nombre dice qué es el dibujo?", "Sí", "Ayuda a encontrarlo."),
        ("¿Se abre un archivo con Abrir o con Borrar?", "Con Abrir", "Borrar lo elimina."),
    ],
    C=[
        ("¿Por qué no se pone el nombre completo ni la dirección en el archivo?", "Porque son datos personales", "Los datos personales deben protegerse."),
        ("¿Qué diferencia hay entre Guardar y Guardar como?", "Guardar actualiza; Guardar como crea otro con otro nombre", "Una cambia el mismo archivo y la otra hace una copia."),
        ("¿Por qué conviene guardar de vez en cuando?", "Para no perder el trabajo si se apaga el equipo", "Evita perder avances."),
    ],
    A=[
        ("Elige el mejor nombre para un dibujo de un barco: «barco_v2», «Rodrigo González» o «1234 teléfono».", "barco_v2", "Dice qué es y no lleva datos personales."),
        ("Quieres probar un cambio sin perder tu dibujo «gato». ¿Usas Guardar o Guardar como?", "Guardar como", "Crea otra copia."),
        ("Tu archivo «puente_v1» está en la carpeta «Tecnología». Escribe dónde lo buscas.", "En la carpeta Tecnología", "Allí lo guardaste."),
    ],
    Z=[
        ("Un compañero guardó todo con el nombre «dibujo» y ahora tiene diez archivos iguales. ¿Qué problema tiene?", "No sabe cuál es cuál", "El mismo nombre confunde."),
        ("Se apagó el equipo y perdiste media hora de trabajo porque no habías guardado. ¿Qué harás la próxima vez?", "Guardar cada cierto tiempo", "Así se pierde menos."),
    ],
    D=[
        ("Escribe tres nombres claros para tres variantes de un carrito.", "carrito_v1, carrito_v2, carrito_v3", "Cada nombre dice qué es."),
        ("Escribe en orden los pasos para guardar un dibujo en la carpeta «Tecnología» con el nombre «robot_v1».", "Guardar como, elegir carpeta Tecnología, escribir robot_v1, guardar", "Son los pasos completos en orden."),
    ],
    ctx=("Pía terminó un dibujo de un sol y debe guardarlo como entrega para su profesora, en la carpeta «Entrega Tecnología». ¿Qué nombre sencillo le pone y qué dato personal evita?", "sol_final; evita poner su nombre completo o dirección", "Nombre claro y sin datos personales."),
    sc=[
        ("¿Un buen nombre dice qué es?", "Sí", "Así se encuentra."),
        ("¿Se escribe el teléfono en el nombre?", "No", "Es un dato personal."),
        ("¿Abrir trae el archivo a la pantalla?", "Sí", "Es su función."),
    ],
    open_task=(
        "Con tu dibujo terminado, guárdalo con el nombre «paisaje_final» y haz una copia con «Guardar como» llamada «paisaje_v2». Anota en una hoja el nombre de cada archivo y la carpeta. Cierra el programa, vuelve a abrir «paisaje_final» y comprueba que está igual. Si no hay dispositivo, rotula dos hojas con esos nombres y guárdalas en una carpeta.",
        "Guardé paisaje_final en la carpeta Tecnología. Con Guardar como hice paisaje_v2. Lo abrí de nuevo y estaba igual.",
        ["usa un nombre claro", "guarda una copia con otro nombre", "anota carpeta y nombres", "abre y comprueba el archivo"],
        ["lista de archivos", "dibujo abierto otra vez"],
        ["nombres con datos personales", "no recordar la carpeta"],
        "Pregunta: «¿dónde lo guardaste y cómo lo abres?». Si usó un nombre personal, ayúdale a cambiarlo.",
    ),
    reinforce="Escribe tres nombres claros para tres dibujos distintos.",
    extend="Explica a alguien los pasos para guardar y recuperar un archivo.",
)

# ------------------------------------------------------------------ OA 06
# Pantallas del procesador de textos: ejemplos ficticios descritos con texto; cada programa se ve algo distinto.
reg(
    OA6, 1,
    materials="Un procesador de textos instalado en el computador del colegio, sin cuenta. Si no hay dispositivo, escribe el ejemplo con lápiz en una hoja.",
    use="Aprenderé a abrir un documento nuevo y escribir un texto corto con el teclado. Sirve para crear información en el computador.",
    prior=["Sé escribir palabras y oraciones a mano.", "Sé qué es un computador."],
    explain=[
        "Un procesador de textos es un programa para escribir y arreglar textos. Al abrirlo, eliges un documento nuevo y aparece una hoja en blanco. Hay una rayita que parpadea: es el cursor. Lo que escribes aparece donde está el cursor.",
        "En el teclado están las letras, la barra espaciadora y la tecla Enter. La barra deja un espacio entre palabras. Enter baja a una línea nueva. Para escribir una mayúscula, se mantiene apretada la tecla de la flecha hacia arriba y se aprieta la letra. Para borrar se usa la tecla de borrar, que está arriba de Enter.",
        "Escribe de a poco. Después de cada oración pon punto y deja un espacio. Mira la pantalla mientras escribes para ver si hay errores. En esta clase puedes escribir tu nombre de pila solo si tu profesor lo pide; para practicar, usa las frases del cuaderno.",
    ],
    vocab=[("procesador de textos", "programa para escribir y arreglar textos"), ("documento", "hoja donde se escribe"), ("cursor", "rayita que parpadea y marca dónde se escribe"), ("tecla", "botón del teclado"), ("espacio", "hueco entre dos palabras")],
    worked=[
        ("Ubicar el cursor", "Abres un documento nuevo y ves una rayita que parpadea arriba a la izquierda. ¿Qué es y qué hace?", ["La rayita parpadea.", "Marca dónde aparece lo que escribo.", "Es el cursor."], "Es el cursor y marca dónde se escribe"),
        ("Escribir una oración", "Quieres escribir «El gato duerme.». ¿Qué teclas usas al terminar «gato» y antes de «duerme»?", ["Termino la palabra gato.", "Dejo un hueco antes de duerme.", "Aprieto la barra espaciadora."], "La barra espaciadora"),
    ],
    mistakes=[
        ("Escribir todas las palabras juntas.", "Sin espacio no se lee bien.", "Aprieta la barra espaciadora entre palabras."),
        ("Apretar Enter al final de cada palabra.", "El texto baja una línea cada vez.", "Usa Enter solo para una línea nueva a propósito."),
    ],
    R=[
        ("La rayita que parpadea se llama cursor. ¿Marca dónde aparece lo que escribes?", "Sí", "Es la posición de escritura."),
        ("La barra espaciadora deja un hueco entre palabras. ¿Sí o no?", "Sí", "Es su función."),
        ("¿La tecla Enter baja una línea o borra una letra?", "Baja una línea", "Enter da una línea nueva."),
    ],
    C=[
        ("¿Para qué sirve un procesador de textos?", "Para escribir y arreglar textos", "Es su función."),
        ("¿Qué hace la tecla de borrar?", "Borra una letra", "Quita lo último escrito."),
        ("¿Dónde aparece lo que escribes?", "Donde está el cursor", "El cursor marca la posición."),
    ],
    A=[
        ("Quieres escribir «Mi casa es azul.» con espacios. ¿Cuántos espacios necesitas entre palabras?", "3", "Entre cuatro palabras hay tres espacios."),
        ("Escribiste «Elgato duerme» sin espacio entre «El» y «gato». ¿Qué tecla usas para arreglarlo?", "La barra espaciadora", "Agrega el espacio."),
        ("Quieres que la segunda oración empiece en otra línea. ¿Qué tecla aprietas?", "Enter", "Baja a una línea nueva."),
    ],
    Z=[
        ("Un niño escribe toda una página sin mirar la pantalla y hay errores. ¿Qué le recomiendas?", "Mirar la pantalla mientras escribe", "Así ve los errores a tiempo."),
        ("Dos niños escriben «hola» y uno apretó Enter después de cada letra. ¿Qué verá en la pantalla?", "Las cuatro letras en cuatro líneas distintas", "Enter baja una línea cada vez."),
    ],
    D=[
        ("Escribe cómo teclearías la frase «Hoy llueve.» con los espacios y el punto. Indica los pasos.", "H-o-y, espacio, l-l-u-e-v-e, punto", "Se escribe cada palabra, espacio y punto."),
        ("Tienes dos oraciones: «Hoy llueve.» y «Salgo con paraguas.». ¿Dónde pones Enter para que cada una quede en su línea?", "Después del punto de «Hoy llueve.»", "Ahí termina la primera."),
    ],
    ctx=("Lola escribe una nota para su curso: «Mañana traemos cartón.». Escribió «Mañanatraemos cartón.» y no se ve bien. ¿Qué le falta y qué tecla usa?", "Un espacio entre Mañana y traemos; la barra espaciadora", "Faltaba separar las palabras."),
    sc=[
        ("¿El cursor marca dónde se escribe?", "Sí", "Es su función."),
        ("¿Enter baja una línea?", "Sí", "Es la tecla de línea nueva."),
        ("¿Entre palabras va un espacio?", "Sí", "Así se lee bien."),
    ],
    open_task=(
        "Escribe en el procesador de textos (o en papel si no hay dispositivo) estas dos oraciones, cada una en su línea: «Hoy aprendo a usar el computador.» y «Escribo con cuidado.». Revisa que haya espacios y puntos. Cuenta cuántas palabras tiene cada oración.",
        "Línea 1: Hoy aprendo a usar el computador. (6 palabras). Línea 2: Escribo con cuidado. (3 palabras).",
        ["escribe las dos oraciones", "usa espacios y punto", "cada oración en su línea", "cuenta las palabras"],
        ["documento o hoja con el texto"],
        ["palabras pegadas", "Enter después de cada palabra"],
        "Pregunta: «¿qué tecla usaste para cambiar de línea?». Revisa el espacio entre palabras.",
    ),
    reinforce="Practica escribir tres frases cortas del cuaderno.",
    extend="Escribe una oración nueva sobre tu mascota o un animal que te guste.",
)

reg(
    OA6, 2,
    materials="Un procesador de textos con un documento que contenga la frase de este cuaderno, o una hoja con tijeras de punta redonda y pegamento, con un adulto cerca, para simular.",
    use="Aprenderé a mover el cursor, seleccionar, copiar, cortar, pegar y deshacer para corregir un texto. Sirve para editar sin escribir todo de nuevo.",
    prior=["Sé abrir un documento y escribir.", "Sé que borrar quita una letra."],
    explain=[
        "Editar es cambiar un texto ya escrito. Para empezar, pon el cursor donde quieres cambiar. Puedes hacer clic con el puntero o usar las teclas de las flechas. Después borra o escribe lo que falta.",
        "Para mover una parte, primero se selecciona. Seleccionar es marcar un trozo de texto, que se ve con color de fondo. Luego puedes copiar, que deja el original y guarda una copia, o cortar, que quita el original. Después pones el cursor donde quieres y pegas.",
        "Si algo sale mal, usa deshacer, que vuelve atrás un paso. Así no pierdes lo que ya estaba bien. En la hoja de papel puedes hacer lo mismo recortando y pegando papelitos.",
    ],
    vocab=[("seleccionar", "marcar un trozo de texto"), ("copiar", "guardar una copia y dejar el original"), ("cortar", "quitar el trozo del lugar de origen"), ("pegar", "poner el trozo guardado en el cursor"), ("deshacer", "volver atrás un paso")],
    worked=[
        ("Corregir una palabra", "Escribiste «El gato duerme en la cama» pero querías «cuna». ¿Qué haces?", ["Pongo el cursor al final de «cama».", "Borro la palabra.", "Escribo «cuna»."], "Borrar «cama» y escribir «cuna»"),
        ("Mover una oración", "La oración «Hoy llueve.» debe ir después de «Salgo con paraguas.». ¿Qué haces?", ["Selecciono «Hoy llueve.».", "La corto.", "Pongo el cursor después de la otra y pego."], "Seleccionar, cortar y pegar después de la otra oración"),
    ],
    mistakes=[
        ("Copiar cuando querías mover.", "El texto queda repetido en dos lugares.", "Usa cortar para mover; copiar para repetir."),
        ("Pegar sin poner el cursor en el lugar nuevo.", "Aparece donde no querías.", "Primero haz clic en el lugar de destino."),
    ],
    R=[
        ("Para mover un trozo, primero se selecciona. ¿Sí o no?", "Sí", "Hay que marcarlo antes."),
        ("Cortar quita el original. Copiar lo deja. ¿Quién deja el original?", "Copiar", "Copiar mantiene el original."),
        ("Deshacer vuelve atrás un paso. ¿Verdadero o falso?", "Verdadero", "Es su función."),
    ],
    C=[
        ("¿Qué diferencia hay entre copiar y cortar?", "Copiar deja el original y cortar lo quita", "Una duplica y la otra mueve."),
        ("¿Dónde aparece lo que pegas?", "Donde está el cursor", "El cursor marca el destino."),
        ("¿Qué haces si pegaste en un lugar equivocado?", "Uso deshacer", "Vuelve al estado anterior."),
    ],
    A=[
        ("Texto: «Mi perro come pan.». Quieres cambiar «pan» por «sopa». ¿Qué palabra seleccionas?", "pan", "Es la que se reemplaza."),
        ("Quieres repetir la palabra «hola» dos veces. ¿Usas copiar o cortar?", "Copiar", "Deja el original y duplica."),
        ("Texto: «Cuento mi día. Hoy salí al patio.». Quieres que «Hoy salí al patio.» vaya primero. ¿Qué haces con esa oración?", "La cortas y la pegas antes de «Cuento mi día.»", "Mover implica cortar y pegar."),
    ],
    Z=[
        ("Ana copió una oración para moverla y ahora está dos veces. ¿Qué debió usar?", "Cortar", "Cortar quita el original."),
        ("Beto borró una oración por error y no puede escribirla otra vez. ¿Qué puede hacer?", "Usar deshacer", "Recupera lo borrado."),
    ],
    D=[
        ("Texto: «El sol sale. La noche termina. El día empieza.». Ordena las oraciones para que quede «La noche termina. El sol sale. El día empieza.». Describe los pasos con cortar y pegar.", "Seleccionar «La noche termina.», cortar y pegar al inicio", "Es un movimiento de oración."),
        ("Quieres copiar la palabra «mamá» a tres lugares. ¿Cuántas veces pegas?", "3", "Una vez por lugar."),
    ],
    ctx=("Tomás escribió: «Ayer jugué. Comí fruta en el recreo.». Quiere que la oración «Comí fruta en el recreo.» vaya antes de «Ayer jugué.». Escribe qué hace.", "Selecciona la oración, la corta, pone el cursor al inicio y pega", "Es mover con cortar y pegar."),
    sc=[
        ("¿Seleccionar es marcar un trozo?", "Sí", "Así se indica qué mover."),
        ("¿Cortar deja el original?", "No", "Cortar quita el original."),
        ("¿Deshacer vuelve atrás?", "Sí", "Corrige el último paso."),
    ],
    open_task=(
        "Usa este texto: «Mi casa es grande. Tiene un jardín. Mi perro se llama Luna.». Haz tres cambios y una corrección: cambia «grande» por «pequeña», mueve «Tiene un jardín.» al final y copia la oración «Mi perro se llama Luna.» y pégala al final para tenerla dos veces, y luego usa deshacer para quitar la copia. Escribe los pasos que usaste.",
        "Cambié grande por pequeña (borrar y escribir). Seleccioné «Tiene un jardín.», la corté y la pegué al final. Copié «Mi perro se llama Luna.», la pegué y usé deshacer.",
        ["cambia una palabra", "mueve una oración con cortar y pegar", "usa copiar y pegar", "escribe los pasos"],
        ["texto corregido", "lista de pasos"],
        ["copiar en lugar de cortar", "pegar sin mover el cursor"],
        "Pregunta: «¿por qué usaste cortar y no copiar?». Si quedó repetido, usa deshacer.",
    ),
    reinforce="Escribe una frase y cambia dos palabras por otras.",
    extend="Reordena tres oraciones para que cuenten una historia en orden.",
)

reg(
    OA6, 3,
    materials="Un procesador de textos con un texto corto, o una hoja y lápices de colores para simular el formato.",
    use="Aprenderé a usar negrita, tamaño de letra y alineación para que un texto se lea mejor. Sirve para destacar títulos y ordenar el texto.",
    prior=["Sé seleccionar texto.", "Sé escribir y corregir un texto."],
    explain=[
        "El formato es cómo se ve el texto. Puedes cambiar el tamaño de las letras, ponerlas en negrita, que es más gruesa, y alinear el texto a la izquierda, al centro o a la derecha. Primero se selecciona el texto y luego se aplica el cambio.",
        "El formato debe ayudar a leer, no solo decorar. Un título en letras más grandes y en negrita se distingue. Un texto muy chico es difícil de leer. Usar demasiadas formas de letra cansa. Mejor pocas y claras.",
        "Por ejemplo, un cartel para el curso: el título va al centro en letra grande y negrita; el texto va a la izquierda en tamaño mediano. Así el lector sabe qué mirar primero. Si no hay dispositivo, puedes simularlo con letra más grande y subrayado.",
    ],
    vocab=[("formato", "cómo se ve el texto"), ("negrita", "letra más gruesa"), ("tamaño de letra", "qué tan grande se ve la letra"), ("alinear", "poner el texto a la izquierda, al centro o a la derecha"), ("título", "frase que dice de qué trata el texto")],
    worked=[
        ("Destacar un título", "Escribiste «Reciclaje en la sala» y quieres que se note como título. ¿Qué formato usas?", ["Selecciono el título.", "Lo pongo en negrita.", "Le agrego un tamaño de letra más grande."], "Negrita y tamaño de letra más grande"),
        ("Alinear", "Quieres el título al centro de la hoja. ¿Qué alineación eliges?", ["El título debe verse al medio.", "Hay tres opciones: izquierda, centro, derecha.", "Elijo centro."], "Centro"),
    ],
    mistakes=[
        ("Poner todo el texto en negrita.", "Si todo se destaca, nada se destaca.", "Usa negrita solo en lo importante."),
        ("Usar letra muy pequeña para que quepa más.", "Cuesta leer.", "Usa un tamaño que se lea fácil."),
    ],
    R=[
        ("La negrita hace la letra más gruesa. ¿Verdadero o falso?", "Verdadero", "Esa es su función."),
        ("Para dar formato a un texto, ¿se selecciona antes o después?", "Antes", "Hay que marcar lo que cambia."),
        ("¿Alinear al centro pone el texto a la izquierda o en el medio?", "En el medio", "Centro significa en medio."),
    ],
    C=[
        ("¿Para qué sirve dar formato a un texto?", "Para que se lea mejor y se destaque lo importante", "El formato ayuda a leer."),
        ("¿Qué formato conviene en un título: letra más grande o más pequeña que el texto?", "Más grande", "Así el título destaca más."),
        ("¿Por qué no conviene poner todo en negrita?", "Porque ya nada destaca", "Pierde su efecto."),
    ],
    A=[
        ("Texto: «Cuidemos el agua». Quieres un título al centro en letra grande. Escribe los tres cambios.", "Seleccionar, centrar y aumentar el tamaño", "Son los pasos para el título."),
        ("Un aviso de 10 palabras se ve muy chico. ¿Qué cambias: el tamaño de letra o la alineación?", "El tamaño de letra", "Más grande es más legible."),
        ("De las frases «Hoy hay prueba», «Traer lápiz» y «Gracias», ¿cuál destacarías con negrita si la prueba es lo más importante?", "Hoy hay prueba", "Es lo más importante del aviso."),
    ],
    Z=[
        ("Dani puso cinco colores y tres tamaños de letra en un aviso corto. ¿Es más fácil leerlo? Explica.", "No, porque se llena de cambios y cansa", "Pocos cambios ayudan más."),
        ("Un cartel para la sala está alineado a la derecha y pegado al borde. ¿Qué alineación sería más equilibrada para el título?", "Centro", "El centro se ve equilibrado."),
    ],
    D=[
        ("Diseña con palabras un aviso: título «Reciclamos papel» y texto «Traer papel limpio el lunes». Di formato del título y del texto.", "Título al centro, negrita y grande; texto a la izquierda, tamaño mediano", "Formato diferente según función."),
        ("Un afiche tiene un título con tamaño de letra 24 y un texto con tamaño 12 (son los números que muestra el programa). ¿Cuántas veces mayor es el título?", "2 veces", "24 dividido en 12 da 2."),
    ],
    ctx=("Eli escribe un aviso para su curso: «Feria de ciencias el viernes. Traer un experimento sencillo.». ¿Qué parte pondrías en negrita y grande y cómo alinearías?", "«Feria de ciencias el viernes» en negrita y grande, al centro", "Es lo principal del aviso."),
    sc=[
        ("¿Se selecciona antes de dar formato?", "Sí", "Para marcar lo que cambia."),
        ("¿La negrita es letra más gruesa?", "Sí", "Es su definición."),
        ("¿Un título puede ir al centro?", "Sí", "Es una alineación posible."),
    ],
    open_task=(
        "Escribe este texto: «Cuidemos la sala. Guardamos los materiales. Dejamos limpia la mesa.». Haz un título con la primera oración: negrita, letra más grande y al centro. Deja las otras dos oraciones a la izquierda. Escribe qué formato usaste y por qué.",
        "Título: «Cuidemos la sala» en negrita, grande y al centro. Las otras dos oraciones a la izquierda, tamaño normal.",
        ["aplica negrita al título", "aumenta el tamaño del título", "centra el título", "deja el resto a la izquierda"],
        ["documento con formato", "frase explicando el formato"],
        ["poner todo en negrita", "letra muy pequeña"],
        "Pregunta: «¿qué se ve primero y por qué?». Si todo se ve igual, pídele diferenciar el título.",
    ),
    reinforce="Escribe una palabra y practica cambiar el tamaño de letra.",
    extend="Haz un cartel con título, texto y una alineación distinta para cada parte.",
)

reg(
    OA6, 4,
    materials="Un procesador de textos que permita insertar imágenes y un dibujo propio guardado como imagen. Si no hay dispositivo, pega un dibujo en papel junto al texto.",
    use="Aprenderé a insertar una imagen propia en un documento y acompañarla de un texto. Sirve para explicar un objeto con dibujo y palabras.",
    prior=["Sé dar formato a un texto.", "Sé guardar y abrir un dibujo."],
    explain=[
        "Insertar una imagen es poner un dibujo dentro del documento. En el procesador de textos hay una opción Insertar, y dentro de ella la opción Imagen. Se elige el archivo del dibujo y la imagen aparece en el documento.",
        "Usa solo imágenes propias, como un dibujo que tú hiciste. No uses fotos de otras personas ni fotos con rostros sin permiso. Tampoco pongas datos personales en la imagen. Si el dibujo tiene tu nombre completo o tu dirección, no lo insertes.",
        "Después de insertar, puedes cambiar el tamaño tirando de una esquina. Mantén las proporciones, es decir, que no se estire. Escribe un texto cerca de la imagen que diga qué es. Un buen documento tiene imagen, título y una oración que la explica.",
    ],
    vocab=[("insertar", "poner algo dentro del documento"), ("imagen propia", "dibujo o foto hecha por ti"), ("proporción", "relación entre alto y ancho"), ("pie de imagen", "frase corta bajo la imagen que la explica"), ("permiso", "autorización para usar algo")],
    worked=[
        ("Elegir la imagen", "Tienes un dibujo tuyo de un portalápices y una foto de tu vecino. ¿Cuál insertas?", ["El dibujo es mío.", "La foto es de otra persona.", "Uso solo el dibujo propio."], "El dibujo del portalápices"),
        ("Escribir un pie de imagen", "Insertaste tu dibujo de un barco. ¿Qué frase pones bajo la imagen?", ["Digo qué es.", "Digo para qué sirve.", "Una oración corta."], "Mi barco de papel, que flota en el agua"),
    ],
    mistakes=[
        ("Insertar una imagen que bajaste de internet sin permiso.", "No es tuya y puede tener derechos de autor.", "Usa dibujos propios o con permiso del profesor."),
        ("Tirar del borde de un solo lado para agrandar la imagen.", "Se estira y se deforma.", "Cambia el tamaño tirando de una esquina."),
    ],
    R=[
        ("Una imagen propia es la que tú hiciste. ¿Puedes insertarla?", "Sí", "La imagen es tuya."),
        ("¿La opción para poner la imagen se llama Insertar o Borrar?", "Insertar", "Borrar la quitaría."),
        ("Un dibujo con tu dirección escrita, ¿conviene insertarlo?", "No", "Tiene datos personales."),
    ],
    C=[
        ("¿Por qué usar solo imágenes propias?", "Porque son mías y no uso el trabajo de otras personas sin permiso", "Respeta el trabajo ajeno."),
        ("¿Qué es un pie de imagen?", "Una frase corta bajo la imagen que la explica", "Dice qué es."),
        ("¿Cómo se cambia el tamaño sin deformar la imagen?", "Tirando de una esquina", "Mantiene las proporciones."),
    ],
    A=[
        ("Dibujaste un carrito de 12 cm y escribiste tu apellido en el dibujo. ¿Qué haces antes de insertarlo?", "Borro mi apellido del dibujo", "No se ponen datos personales."),
        ("Insertaste un dibujo de una casa. Escribe un pie de imagen de una oración.", "Mi casa de cartón con techo azul", "Dice qué es."),
        ("Una imagen sale muy grande y ocupa toda la hoja. ¿Qué haces: la achico o la borro?", "La achico tirando de una esquina", "Se ajusta sin perderla."),
    ],
    Z=[
        ("Rafa quiere insertar una foto de un amigo sin avisarle. ¿Qué debe hacer?", "No insertarla o pedir permiso", "Se respeta la privacidad."),
        ("Una imagen estirada se ve achatada. ¿Qué pasó con las proporciones?", "No se mantuvieron", "Tiraron de un lado y no de la esquina."),
    ],
    D=[
        ("Describe un documento de una página: título, una imagen propia, un pie de imagen y dos oraciones explicando el objeto.", "Título, imagen del objeto, pie de imagen, dos oraciones", "Reúne los elementos pedidos."),
        ("La imagen mide 10 cm de ancho y 6 cm de alto. La achicas a la mitad en ambos lados. ¿Cuánto mide ahora?", "5 cm de ancho y 3 cm de alto", "La mitad de 10 es 5 y la mitad de 6 es 3."),
    ],
    ctx=("Sol hizo un dibujo de su soporte de fichas y quiere ponerlo en un informe. El dibujo tiene su dirección escrita. ¿Qué hace antes de insertarlo y qué pie de imagen escribe?", "Borra la dirección; pie: Mi soporte de fichas", "Protege sus datos y explica la imagen."),
    sc=[
        ("¿Se usan imágenes propias?", "Sí", "Son tuyas y no tienen problema de derechos."),
        ("¿Un pie de imagen explica la imagen?", "Sí", "Es su función."),
        ("¿Se tira de una esquina para achicar?", "Sí", "Así se mantienen las proporciones."),
    ],
    open_task=(
        "Usa un dibujo propio de un objeto que diseñaste. Escribe en el documento un título, inserta la imagen (o pégala en papel), escribe un pie de imagen y dos oraciones que expliquen para qué sirve. No pongas datos personales.",
        "Título: Mi portalápices. Pie: Mi portalápices de cartón. Texto: Sirve para guardar cinco lápices. Es de cartón y mide 10 cm.",
        ["inserta una imagen propia", "escribe pie de imagen", "escribe dos oraciones", "no pone datos personales"],
        ["documento con imagen y texto"],
        ["usar imágenes ajenas", "datos personales en la imagen"],
        "Pregunta: «¿esta imagen la hiciste tú?». Revisa que no tenga nombre completo ni dirección.",
    ),
    reinforce="Dibuja un objeto simple y escribe una frase que lo explique.",
    extend="Agrega una segunda imagen propia y un pie para cada una.",
)

reg(
    OA6, 5,
    materials="Un procesador de textos con un documento ya escrito, una carpeta del colegio y una hoja para anotar. Si no hay dispositivo, usa hoja y carpeta de papel.",
    use="Aprenderé a guardar un documento con un buen nombre, cerrarlo y abrirlo otra vez para seguir. Sirve para no perder mi trabajo.",
    prior=["Sé escribir, dar formato e insertar una imagen.", "Sé guardar un dibujo."],
    explain=[
        "Un documento nuevo no se guarda solo. Para conservarlo, usa Guardar. El programa te pide un nombre y la carpeta donde queda. Elige un nombre claro, como «aviso_sala», y la carpeta que dijo tu profesor. No pongas tu nombre completo ni tu dirección.",
        "Después puedes cerrar el documento. Antes de cerrar, el programa puede preguntar si quieres guardar los cambios. Si trabajaste y no guardaste, elige guardar. Cerrar sin guardar pierde lo nuevo. Algunos programas guardan solos, pero no debes confiar en eso. Mientras trabajas, guarda cada cierto tiempo.",
        "Para recuperar el documento, abre el programa, elige Abrir y busca la carpeta y el nombre. Comprueba que está lo que escribiste. Si quieres una copia con otro nombre, usa Guardar como. Con papel puedes hacer lo mismo: rotula la hoja y guárdala en una carpeta.",
    ],
    vocab=[("guardar", "conservar el documento en el dispositivo"), ("cerrar", "terminar de trabajar con el documento"), ("recuperar", "volver a abrir lo guardado"), ("cambios", "lo nuevo que escribiste desde la última vez"), ("nombre claro", "nombre que dice qué contiene")],
    worked=[
        ("Decidir al cerrar", "Escribiste dos oraciones nuevas y el programa pregunta: «¿Guardar los cambios?». ¿Qué eliges?", ["Las oraciones nuevas son valiosas.", "Si no guardo, se pierden.", "Elijo guardar."], "Guardar los cambios"),
        ("Recuperar", "Guardaste «aviso_sala» en la carpeta «Tecnología». Hoy quieres seguir. ¿Qué haces?", ["Abro el programa.", "Elijo Abrir.", "Busco la carpeta Tecnología y el nombre aviso_sala."], "Abrir, carpeta Tecnología, aviso_sala"),
    ],
    mistakes=[
        ("Cerrar sin guardar los cambios.", "Se pierde lo nuevo.", "Responde que sí cuando el programa pregunta si guardar."),
        ("Poner un nombre como «documento1».", "No dice qué es.", "Usa un nombre claro, como «aviso_sala»."),
    ],
    R=[
        ("Si cierras sin guardar, ¿pierdes lo nuevo?", "Sí", "No quedó guardado."),
        ("Para volver a ver el documento, ¿usas Abrir o Cerrar?", "Abrir", "Cerrar lo termina."),
        ("«aviso_sala», ¿es un nombre claro?", "Sí", "Dice qué contiene."),
    ],
    C=[
        ("¿Por qué conviene guardar cada cierto tiempo?", "Para no perder el trabajo si se apaga el equipo", "Evita perder avances."),
        ("¿Qué pasa con los cambios si no guardas antes de cerrar?", "Se pierden", "No quedan en el archivo."),
        ("¿Para qué sirve Guardar como?", "Para hacer una copia con otro nombre", "Conserva el original."),
    ],
    A=[
        ("Escribiste «Tarea de Tecnología» y quieres guardarla. Elige un nombre claro: «tarea_tecnologia», «doc1» o «nombre completo y dirección».", "tarea_tecnologia", "Dice qué es y no tiene datos personales."),
        ("El programa pregunta si guardas los cambios después de que escribiste tres oraciones nuevas. ¿Respondes guardar o no guardar?", "Guardar", "Así no pierdes las oraciones."),
        ("Quieres hacer una versión nueva de «aviso_sala» sin tocar la anterior. ¿Usas Guardar o Guardar como?", "Guardar como", "Crea otra copia."),
    ],
    Z=[
        ("Un compañero cerró sin guardar y su texto desapareció. ¿Qué pasó?", "No guardó los cambios", "Sin guardar, se pierden."),
        ("Una niña guardó el documento con su dirección en el nombre. ¿Qué problema hay?", "Hay datos personales en el nombre", "Debe protegerse la privacidad."),
    ],
    D=[
        ("Escribe en orden los pasos para guardar, cerrar y volver a abrir un documento llamado «reglas_sala».", "Guardar con nombre, cerrar, abrir el programa, elegir Abrir, buscar reglas_sala", "Son los pasos completos en orden."),
        ("Guardas cada 5 minutos durante 30 minutos. ¿Cuántas veces guardas?", "6", "30 dividido en 5 da 6."),
    ],
    ctx=("Tomás terminó un aviso para el curso y apagará el equipo. Escribe qué debe hacer antes de apagarlo y cómo lo recuperará mañana.", "Guardar con nombre claro; mañana abre el programa, elige Abrir y busca el nombre", "Guardar y abrir son los pasos."),
    sc=[
        ("¿Se guarda antes de cerrar?", "Sí", "Para no perder cambios."),
        ("¿Se abre un documento con Abrir?", "Sí", "Es su función."),
        ("¿El nombre del documento dice qué contiene?", "Sí", "Es un nombre claro."),
    ],
    open_task=(
        "Escribe un documento con este texto: «Reglas de la sala: Hablamos por turnos. Guardamos los materiales.». Guárdalo con el nombre «reglas_sala». Cierra el programa, ábrelo otra vez y agrega una tercera regla: «Cuidamos las tijeras.». Guarda de nuevo y anota los pasos que seguiste. Si no hay dispositivo, usa hojas y una carpeta de papel.",
        "Guardé reglas_sala. Cerré. Abrí y agregué la tercera regla. Guardé otra vez.",
        ["guarda con nombre claro", "cierra y abre el documento", "agrega la tercera regla", "guarda de nuevo", "anota los pasos"],
        ["documento con tres reglas", "lista de pasos"],
        ["cerrar sin guardar", "nombre con datos personales"],
        "Pregunta: «¿cómo lo recuperaste?». Si no guardó el cambio final, repite.",
    ),
    reinforce="Escribe los pasos para guardar un documento y pégalos en tu cuaderno.",
    extend="Explica a un familiar la diferencia entre Guardar y Guardar como.",
)

"""Student material for 1.º básico Tecnología, OA 05 (dibujo digital) y OA 06 (software educativo y creativo)."""
from __future__ import annotations

from student_lessons import ex, register

OA5, OA6 = "TE01 OA 05", "TE01 OA 06"


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
reg(
    OA5, 1,
    materials="Un programa de dibujo sencillo en un computador, tablet o teléfono de la casa o de la escuela, con un adulto cerca. Si no hay dispositivo, usa papel y lápices: los ejercicios de este cuaderno describen la pantalla con palabras y se resuelven sin conexión.",
    use="Aprenderé a reconocer las herramientas básicas de un programa de dibujo y para qué sirve cada una. Sirve para dibujar en pantalla con seguridad y sin perderme.",
    prior=["Sé dibujar con lápiz en papel.", "Sé que un dispositivo se usa con ayuda de un adulto."],
    explain=[
        "Un programa de dibujo es una aplicación para hacer dibujos en una pantalla. Casi todos tienen las mismas herramientas. El lápiz o pincel dibuja líneas. La goma borra. Las formas hacen círculos, cuadrados y triángulos. El balde de color pinta una zona.",
        "También hay botones de ayuda. El botón deshacer, que suele ser una flecha que gira hacia atrás, borra el último paso. El botón guardar guarda tu dibujo para que no se pierda. El selector de color te deja elegir un color de una paleta.",
        "Antes de dibujar, mira la pantalla y busca cada herramienta. Prueba un botón a la vez y fíjate qué pasa. Si no sabes qué hace uno, pregunta a un adulto. En este cuaderno usamos nombres generales para los botones, sin nombrar ningún programa real: en un programa de verdad pueden tener otro dibujo o estar en otro lugar. Usa el dispositivo solo con permiso y por poco tiempo.",
    ],
    vocab=[("herramienta digital", "botón de un programa que hace una acción"), ("lápiz", "herramienta que dibuja líneas"), ("goma", "herramienta que borra"), ("deshacer", "botón que borra el último paso"), ("guardar", "botón que conserva el dibujo")],
    worked=[
        ("Elegir herramienta", "Quieres borrar una línea que dibujaste mal. ¿Qué herramienta usas?", ["La acción es borrar.", "La goma borra.", "También puedo usar deshacer si fue lo último."], "La goma o deshacer"),
        ("Guardar a tiempo", "Terminaste un dibujo y quieres que no se pierda. ¿Qué botón usas?", ["La acción es conservar el dibujo.", "El botón guardar lo conserva."], "Guardar"),
    ],
    mistakes=[
        ("Apretar todos los botones sin mirar qué hacen.", "Se pueden borrar o cambiar cosas sin querer.", "Prueba uno por uno y usa deshacer si algo sale mal."),
        ("Cerrar el programa sin guardar.", "Se pierde el dibujo.", "Guarda antes de cerrar."),
    ],
    R=[
        ("¿Qué herramienta dibuja líneas: el lápiz o la goma?", "El lápiz", "El lápiz deja trazo."),
        ("¿Qué herramienta borra: la goma o el balde de color?", "La goma", "La goma quita el trazo."),
        ("¿Qué botón conserva tu dibujo: guardar o deshacer?", "Guardar", "Guardar lo conserva."),
    ],
    C=[
        ("¿Para qué sirve el botón deshacer?", "Para borrar el último paso", "Corrige el último cambio."),
        ("¿Para qué sirve el selector de color?", "Para elegir el color", "Muestra la paleta."),
        ("¿Por qué conviene probar los botones uno por uno?", "Para ver qué hace cada uno sin confundirse", "Se aprende qué cambia cada botón."),
    ],
    A=[
        ("Quieres dibujar un círculo para el sol. ¿Qué herramienta usas: formas o goma?", "Formas", "La herramienta de formas hace círculos."),
        ("Pintaste un cuadrado y te equivocaste de color. ¿Qué botón usas para volver atrás un paso?", "Deshacer", "Borra el último paso."),
        ("Tu pantalla muestra 5 botones: lápiz, goma, formas, color y guardar. ¿Cuántos son para dibujar o pintar (lápiz, formas y color)?", "3", "Se cuentan lápiz, formas y color."),
    ],
    Z=[
        ("Luis cerró el programa sin guardar y perdió su dibujo. ¿Qué paso olvidó?", "Guardar", "Lo conserva antes de cerrar."),
        ("Ema aprieta botones sin mirar y borra su dibujo. ¿Qué debe usar para volver atrás?", "Deshacer", "Recupera el paso anterior."),
    ],
    D=[
        ("Si no hay dispositivo, ¿con qué materiales puedes practicar el dibujo y las formas: papel y lápiz o ninguno?", "Papel y lápiz", "Se practican las mismas ideas sin pantalla."),
        ("Un dibujo digital usa 4 formas: 2 círculos, 1 cuadrado y 1 triángulo. ¿Cuántas formas hay en total?", "4", "2 + 1 + 1 = 4."),
    ],
    ctx=("Rita abre un programa de dibujo con la ayuda de su mamá. Quiere dibujar una casa con un cuadrado y un triángulo, y pintar el techo de rojo. Ordena las herramientas que usa: guardar, color, formas.", "Formas, color, guardar", "Primero dibuja, luego pinta y por último conserva."),
    sc=[
        ("¿Qué herramienta borra?", "La goma", "Quita el trazo."),
        ("¿Qué botón guarda el dibujo?", "Guardar", "Conserva el dibujo."),
        ("¿Se puede usar un dispositivo sin permiso de un adulto? Responde sí o no.", "No", "Siempre se pide permiso."),
    ],
    open_task=(
        "Con un programa de dibujo (o con papel si no hay dispositivo) dibuja una casa con un cuadrado, un triángulo y una puerta rectangular. Usa estas herramientas: formas, color y deshacer. Anota qué herramienta usaste para cada parte.",
        "Cuadrado para la pared con formas, triángulo para el techo con formas, color rojo en el techo y deshacer cuando se me salió una línea.",
        ["reconoce las herramientas", "usa cada una para su propósito", "usa deshacer o goma", "pide permiso"],
        ["dibujo de casa", "lista de herramientas usadas"],
        ["usar herramientas sin entender", "no guardar"],
        "Pide mostrar dónde está cada herramienta. Si usa papel, comprueba que hizo las mismas partes.",
    ),
    reinforce="Dibuja en papel una pantalla con los botones lápiz, goma y guardar.",
    extend="Explica a un adulto qué hace cada botón del programa.",
)

reg(
    OA5, 2,
    materials="Un programa de dibujo y un dispositivo con un adulto cerca, o papel y lápiz como alternativa. El plano del rincón de lectura está descrito con palabras en este cuaderno.",
    use="Aprenderé a hacer trazos y formas con un propósito, para representar un lugar. Sirve para dibujar un plano que otra persona entienda.",
    prior=["Sé reconocer las herramientas de dibujo.", "Sé qué es un cuadrado, un círculo y un rectángulo.", "Sé qué es izquierda y derecha."],
    explain=[
        "Un plano es un dibujo de un lugar visto desde arriba. Para dibujar un plano se usan formas simples. Una mesa se puede dibujar con un rectángulo, una alfombra redonda con un círculo y una silla con un cuadrado.",
        "Cada trazo tiene una intención, o sea, una razón. Una línea recta marca el borde de la pared. Un círculo muestra una alfombra. Un rectángulo largo puede ser un estante. Dibuja pensando qué quieres mostrar y no solo llenando espacio.",
        "Recuerda dos reglas. Primero dibuja lo más grande, como las paredes, y luego lo más pequeño. Segundo, usa pocas formas y claras: si el plano tiene muchos detalles, nadie entiende lo importante. Si algo no sale bien, usa deshacer y vuelve a hacerlo.",
    ],
    vocab=[("plano", "dibujo de un lugar visto desde arriba"), ("trazo", "línea hecha con el lápiz"), ("forma", "figura como círculo, cuadrado o triángulo"), ("intención", "razón por la que dibujo algo"), ("vista desde arriba", "como si miraras el lugar desde el techo")],
    worked=[
        ("Elegir la forma", "En el rincón de lectura hay una mesa grande y larga. ¿Qué forma dibujas en el plano?", ["La mesa vista desde arriba es larga.", "Un rectángulo es largo.", "Uso un rectángulo."], "Un rectángulo"),
        ("Contar elementos", "El rincón tiene 1 mesa, 2 sillas y 1 alfombra redonda. ¿Cuántas formas dibujas en total?", ["Cuento las mesas: 1.", "Sumo las sillas: 2.", "Sumo la alfombra: 1.", "1 + 2 + 1 = 4."], "4 formas"),
    ],
    mistakes=[
        ("Dibujar la mesa de frente, como si estuviera parada.", "Un plano se ve desde arriba.", "Dibuja la mesa como un rectángulo visto desde arriba."),
        ("Llenar el plano de detalles que no ayudan.", "Se pierde lo importante.", "Dibuja solo lo necesario: mesa, sillas, alfombra y estante."),
    ],
    R=[
        ("Una alfombra redonda, vista desde arriba, ¿se dibuja con un círculo o con un triángulo?", "Un círculo", "La forma es redonda."),
        ("Una mesa larga, vista desde arriba, ¿se dibuja con un rectángulo o con un círculo?", "Un rectángulo", "La mesa es larga."),
        ("¿Un plano se ve desde arriba o de frente?", "Desde arriba", "Así se muestra el lugar."),
    ],
    C=[
        ("En Tecnología, ¿qué es un plano?", "Un dibujo de un lugar visto desde arriba", "Muestra dónde está cada cosa."),
        ("¿Por qué conviene usar pocas formas claras?", "Para que se entienda lo importante", "Muchos detalles confunden."),
        ("¿Qué dibujas primero: las paredes o los detalles pequeños?", "Las paredes", "Lo más grande da la base."),
    ],
    A=[
        ("Un estante largo y angosto, visto desde arriba, ¿qué forma tiene?", "Un rectángulo", "Es una forma alargada."),
        ("En un rincón hay 3 sillas cuadradas y 1 mesa rectangular. ¿Cuántas formas dibujas?", "4", "3 + 1 = 4."),
        ("En un plano, una pared mide 20 cm y otra pared mide 12 cm. ¿Cuántos cm más larga es la primera?", "8", "20 − 12 = 8."),
    ],
    Z=[
        ("Ana dibujó una mesa con círculo, y era rectangular. ¿Fue bien elegida la forma? Responde sí o no.", "No", "La forma no coincide con la mesa."),
        ("Teo llenó su plano de 20 adornos y no se ve la mesa. ¿Qué debe hacer?", "Quitar adornos y dejar lo importante", "Así el plano se entiende."),
    ],
    D=[
        ("En un plano hay una alfombra en el centro, una mesa a la derecha y un estante a la izquierda. ¿Qué queda a la izquierda?", "El estante", "Así lo dice la descripción."),
        ("Un rectángulo cubre 3 filas de un papel cuadriculado, con 2 casillas en cada fila. ¿Cuántas casillas cubre?", "6", "2 + 2 + 2 = 6."),
    ],
    ctx=("Nico dibuja su rincón de lectura en la pantalla. Tiene 1 mesa rectangular, 2 sillas cuadradas y 1 alfombra redonda. Escribe qué formas usa en orden: mesa, sillas, alfombra.", "Rectángulo, cuadrados y círculo", "Cada objeto se representa con su forma."),
    sc=[
        ("¿Un plano se dibuja de frente? Responde sí o no.", "No", "Se dibuja desde arriba."),
        ("¿Qué forma uso para una alfombra redonda?", "Un círculo", "Es una forma redonda."),
        ("¿Qué hago si un trazo sale mal?", "Uso deshacer", "Vuelve atrás un paso."),
    ],
    open_task=(
        "Dibuja un plano del rincón de lectura con esta lista: 1 mesa rectangular, 2 sillas cuadradas, 1 estante largo contra la pared y 1 alfombra redonda. Usa un programa de dibujo o papel. Anota qué forma usaste para cada objeto.",
        "Mesa: rectángulo. Sillas: dos cuadrados. Estante: rectángulo largo pegado a la pared. Alfombra: círculo. Usé deshacer una vez.",
        ["usa formas simples", "dibuja desde arriba", "incluye los 4 elementos", "anota las formas usadas"],
        ["plano terminado", "lista de formas"],
        ["dibujar de frente", "llenar de detalles"],
        "Pide mostrar dónde está cada elemento. Si está de frente, pregunta cómo se ve desde el techo.",
    ),
    reinforce="Dibuja desde arriba el plano de tu pieza con una cama rectangular.",
    extend="Agrega una ventana y una puerta a tu plano usando solo líneas.",
)

reg(
    OA5, 3,
    materials="El plano del rincón de lectura descrito en este cuaderno, un programa de dibujo o papel con lápices de colores. Los colores se nombran en el texto.",
    use="Aprenderé a usar color, tamaño y posición con una razón. Sirve para que mi dibujo diga cosas claras y no solo se vea lindo.",
    prior=["Sé hacer un plano con formas.", "Sé usar izquierda, derecha, arriba y abajo."],
    explain=[
        "El color, el tamaño y la posición pueden dar información. Un color funcional es un color que significa algo. Por ejemplo, en el plano usas verde para la zona de lectura y azul para la zona de guardado. Así se entiende sin explicar mucho.",
        "El tamaño muestra qué cosa es más grande. Si la mesa de lectura es grande, la dibujas grande. La posición muestra dónde está cada cosa: a la izquierda, a la derecha, arriba, abajo, cerca o lejos de otra cosa. Dibuja cada cosa donde está de verdad.",
        "Para que se entienda, agrega una leyenda: un recuadro que dice qué significa cada color. Por ejemplo, verde: leer; azul: guardar. Usa pocos colores y, además del color, escribe la palabra en la zona, por si alguien no distingue bien los colores. Si cambias un tamaño o una posición, el plano también cambia, así que hazlo con intención.",
    ],
    vocab=[("color funcional", "color que significa algo"), ("tamaño", "qué tan grande o pequeño es algo"), ("posición", "dónde está algo"), ("leyenda", "recuadro que dice qué significa cada color"), ("cerca y lejos", "poca o mucha distancia entre dos cosas")],
    worked=[
        ("Leer una leyenda", "La leyenda dice: verde es leer, azul es guardar. Hay una mesa verde y un estante azul. ¿Qué se hace en la mesa?", ["Busco el verde en la leyenda.", "Verde es leer.", "En la mesa se lee."], "Se lee"),
        ("Usar posición", "El estante está a la izquierda de la mesa. En el plano, ¿dónde dibujas el estante?", ["Izquierda es el lado de la mano izquierda.", "Lo pongo a la izquierda de la mesa."], "A la izquierda de la mesa"),
    ],
    mistakes=[
        ("Usar muchos colores sin explicar qué significan.", "Nadie entiende.", "Usa pocos colores y una leyenda."),
        ("Dibujar todo del mismo tamaño.", "No se ve qué es más grande.", "Dibuja la mesa grande y la silla más pequeña."),
    ],
    R=[
        ("En la leyenda, verde es leer. Una zona verde es para ¿leer o guardar?", "Leer", "Verde significa leer."),
        ("Una mesa grande se dibuja ¿grande o muy pequeña?", "Grande", "Se respeta el tamaño."),
        ("Si el estante está a la derecha de la mesa, ¿lo dibujas a la derecha o a la izquierda?", "A la derecha", "Se respeta la posición."),
    ],
    C=[
        ("En Tecnología, ¿qué es una leyenda?", "Un recuadro que dice qué significa cada color", "Explica los colores."),
        ("¿Por qué se respeta el tamaño de los objetos?", "Para que el plano sea parecido a la realidad", "El tamaño dice qué es grande."),
        ("¿Qué muestra la posición en un plano?", "Dónde está cada cosa", "Se ubica cada objeto."),
    ],
    A=[
        ("Leyenda: rojo es peligro, verde es seguro. Una zona verde ¿es peligro o es segura?", "Es segura", "Verde significa seguro."),
        ("En un plano hay 2 zonas verdes y 3 zonas azules. ¿Cuántas zonas de color hay en total?", "5", "2 + 3 = 5."),
        ("En el plano, la silla está arriba de la mesa y la alfombra está abajo de la mesa. ¿Qué está más cerca del borde de abajo del papel?", "La alfombra", "Ella está abajo."),
    ],
    Z=[
        ("Pía pintó la zona de lectura de rojo y la leyenda dice verde para leer. ¿Qué error hay?", "El color no coincide con la leyenda", "Debe ser verde."),
        ("Luis dibujó la mesa y la silla igual de grandes, pero la mesa es mucho más grande. ¿Qué debe cambiar?", "Dibujar la silla más pequeña o la mesa más grande", "Debe reflejar la realidad."),
    ],
    D=[
        ("Leyenda: azul guardar, verde leer, amarillo jugar. El plano tiene 1 zona azul, 2 verdes y 1 amarilla. ¿Cuántas zonas son para leer?", "2", "Hay 2 zonas verdes."),
        ("Hay 4 objetos en fila: estante, silla, mesa, alfombra. ¿Qué objeto está tercero?", "Mesa", "El tercero en la lista."),
    ],
    ctx=("Ema pinta su plano del rincón de lectura. Usa verde para leer (mesa) y azul para guardar (estante). El estante está a la derecha de la mesa. ¿Qué color usa para el estante y dónde lo dibuja?", "Azul, a la derecha de la mesa", "Sigue la leyenda y la posición."),
    sc=[
        ("¿Para qué sirve una leyenda?", "Para explicar los colores", "Dice qué significa cada uno."),
        ("¿Se respeta el tamaño real de las cosas? Responde sí o no.", "Sí", "Así se entiende."),
        ("Si el estante está a la izquierda, ¿lo dibujas a la derecha? Responde sí o no.", "No", "Debe estar a la izquierda."),
    ],
    open_task=(
        "Pinta el plano del rincón de lectura con esta leyenda: verde para leer (mesa), azul para guardar (estante), amarillo para jugar (alfombra). El estante está a la izquierda de la mesa y la alfombra está abajo de la mesa. La mesa es grande y la silla es pequeña. Escribe la leyenda dentro del dibujo y di cuál se dibuja más grande, la mesa o la silla.",
        "Pinté la mesa verde, el estante azul a la izquierda y la alfombra amarilla abajo. Escribí la leyenda con 3 colores. Dibujé la mesa más grande que la silla.",
        ["usa color funcional", "respeta tamaño", "ubica con posición", "escribe leyenda"],
        ["plano pintado", "leyenda dentro del dibujo"],
        ["colores sin leyenda", "posición cambiada"],
        "Pide leer la leyenda y señalar en el dibujo cada color. Si la posición no coincide, pregunta qué lado es la izquierda.",
    ),
    reinforce="Pinta una zona de tu casa con 2 colores y escribe qué significan.",
    extend="Agrega dos colores más a la leyenda y úsalos con razón.",
)

reg(
    OA5, 4,
    materials="El plano pintado de la clase anterior o su descripción en este cuaderno, un programa de dibujo con deshacer, o papel con lápiz y goma. Un adulto cerca.",
    use="Aprenderé a revisar y mejorar mi dibujo sin empezar de cero. Sirve para ahorrar tiempo y aprender de mis errores.",
    prior=["Sé usar deshacer o goma.", "Sé que un dibujo puede mejorar."],
    explain=[
        "Revisar es mirar tu dibujo y preguntarte qué falta y qué sobra. No hace falta empezar de cero. Muchos programas permiten mover una parte, hacerla más grande o más pequeña, cambiar su color o borrar solo una zona.",
        "Para revisar, usa una lista de preguntas: ¿están todos los objetos?, ¿están en su lugar?, ¿los colores siguen la leyenda?, ¿se entiende desde arriba? Si una respuesta es no, cambia solo esa cosa. Si algo sale peor, usa deshacer y vuelve atrás.",
        "Guarda versiones. Antes de un cambio grande, guarda con otro nombre, por ejemplo plano-1 y plano-2. Así puedes volver a la primera si la segunda queda peor. Pedir la opinión de otra persona también ayuda, siempre con respeto.",
    ],
    vocab=[("revisar", "mirar lo hecho para ver qué mejorar"), ("versión", "una copia guardada del dibujo en un momento"), ("mover", "cambiar de lugar una parte"), ("cambiar tamaño", "hacer una parte más grande o más pequeña"), ("lista de revisión", "preguntas para mirar mi dibujo")],
    worked=[
        ("Aplicar la lista", "Tu plano tiene mesa, silla y estante, pero falta la alfombra. ¿Qué falla en la lista de revisión?", ["Pregunto: ¿están todos los objetos?", "Falta la alfombra.", "Respuesta: no."], "Falta un objeto: la alfombra"),
        ("Cambiar solo una cosa", "La mesa está pintada de rojo y debía ser verde. ¿Rehaces todo el dibujo o cambias solo el color de la mesa?", ["Solo la mesa tiene el error.", "Cambio ese color.", "No empiezo de cero."], "Cambias solo el color de la mesa"),
    ],
    mistakes=[
        ("Borrar todo y empezar de nuevo por un error pequeño.", "Se pierde mucho trabajo.", "Cambia solo la parte que falla."),
        ("No guardar una versión antes de un cambio grande.", "No se puede volver atrás si sale peor.", "Guarda con otro nombre antes de cambiar."),
    ],
    R=[
        ("Una silla está en un lugar equivocado. ¿La mueves o borras todo el plano?", "La mueves", "Se corrige solo esa parte."),
        ("¿Para qué sirve deshacer cuando algo sale peor?", "Para volver atrás", "Recupera el paso anterior."),
        ("¿Guardar con otro nombre crea una versión? Responde sí o no.", "Sí", "Es una copia en ese momento."),
    ],
    C=[
        ("¿Qué es una lista de revisión?", "Preguntas para mirar mi dibujo", "Ayuda a ver qué mejorar."),
        ("¿Por qué conviene guardar versiones?", "Para poder volver si el cambio sale peor", "Se conserva la anterior."),
        ("¿Qué haces si solo un color está mal?", "Cambias solo ese color", "No es necesario rehacer todo."),
    ],
    A=[
        ("Tu plano debe tener 5 objetos y tiene 3. ¿Cuántos faltan?", "2", "5 − 3 = 2."),
        ("Guardas plano-1, plano-2 y plano-3. ¿Cuántas versiones guardaste?", "3", "Hay un archivo por versión."),
        ("En la lista de revisión de 4 preguntas contestas sí a 3. ¿A cuántas contestas no?", "1", "4 − 3 = 1."),
    ],
    Z=[
        ("Rita borró todo su plano por una silla chueca. ¿Fue necesario? Responde sí o no.", "No", "Bastaba mover la silla."),
        ("Teo hizo un cambio grande sin guardar una versión antes, cerró el programa y el dibujo quedó peor. ¿Puede volver a su dibujo anterior? Responde sí o no.", "No", "Sin versión guardada no hay copia anterior."),
    ],
    D=[
        ("Escribe una pregunta para revisar un plano del rincón de lectura (por ejemplo: ¿está la mesa?).", "¿Están todos los objetos?", "Es una pregunta de revisión válida."),
        ("Tienes dos versiones: plano-1 con 4 objetos y plano-2 con 6 objetos. Si la tarea pide 6 objetos, ¿cuál sirve?", "plano-2", "Tiene los 6 objetos."),
    ],
    ctx=("Pía revisa su plano con la lista: ¿están todos los objetos?, ¿están en su lugar?, ¿los colores siguen la leyenda? Responde sí, sí, no (el estante está pintado de rojo y debía ser azul). ¿Qué cambia?", "El color del estante", "Falla en la tercera pregunta."),
    sc=[
        ("¿Hay que empezar de cero para corregir un error pequeño? Responde sí o no.", "No", "Se corrige solo esa parte."),
        ("¿Qué botón vuelve atrás un paso?", "Deshacer", "Recupera el paso anterior."),
        ("¿Para qué guardas una versión antes de un cambio grande?", "Para poder volver atrás", "Conserva el dibujo."),
    ],
    open_task=(
        "Revisa este plano que te describimos: tiene una mesa verde, un estante rojo (debía ser azul), una alfombra amarilla y falta la silla. Haz la lista de revisión de 3 preguntas, escribe qué dos cosas cambiarías y escribe con qué nombre guardarías una versión antes de cambiar (por ejemplo plano-2) y confirma que no empezarás de cero.",
        "Pregunta 1: ¿están todos los objetos? No, falta la silla. Pregunta 2: ¿colores según la leyenda? No, el estante debe ser azul. Guardo la versión plano-2 antes de cambiar. Cambiaría el color del estante y agregaría la silla sin borrar lo demás.",
        ["usa una lista de revisión", "cambia solo lo que falla", "no empieza de cero", "guarda una versión"],
        ["lista con respuestas", "dos cambios escritos"],
        ["borrar todo", "no guardar versión"],
        "Pide mostrar qué cambió y qué quedó igual. Recuerda guardar antes del cambio grande.",
    ),
    reinforce="Mira un dibujo tuyo y cambia solo una cosa.",
    extend="Haz dos versiones de un dibujo y compáralas.",
)

reg(
    OA5, 5,
    materials="El dibujo terminado de la clase anterior o su descripción en este cuaderno, un dispositivo con permiso de un adulto, o una hoja de papel para escribir el nombre y las reglas. No hace falta internet.",
    use="Aprenderé a guardar mi dibujo con un nombre seguro y a compartirlo con permiso. Sirve para cuidar mis datos y respetar a los demás.",
    prior=["Sé guardar un dibujo.", "Sé que hay información que no se comparte."],
    explain=[
        "Guardar un dibujo es conservarlo en el dispositivo. Para encontrarlo después, le pones un nombre claro. Un buen nombre dice qué es, por ejemplo plano-rincon-1. No uses tu nombre completo, tu dirección, tu teléfono ni el nombre de tu colegio: son datos personales.",
        "Compartir es mostrar tu dibujo a otras personas. Primero pide permiso a un adulto. Comparte solo con personas que conoces, como tu familia o tu profesor. Nunca compartas con desconocidos. Y no muestres fotos de otras personas sin que ellas y un adulto lo permitan.",
        "Respeta siempre la autoría, o sea, quién hizo el dibujo. Si el dibujo lo hiciste tú, di que es tuyo. Si te ayudó otra persona, reconoce su ayuda y pregunta antes de escribir su nombre. Cuando termines, cierra el programa y deja el dispositivo como estaba. Usarlo poco tiempo cuida tus ojos.",
    ],
    vocab=[("nombre seguro", "nombre que no tiene datos personales"), ("dato personal", "información que dice quién eres, como tu dirección"), ("compartir", "mostrar el dibujo a otra persona"), ("permiso", "decir que sí un adulto antes de hacer algo"), ("autoría", "quién hizo el dibujo")],
    worked=[
        ("Elegir un nombre seguro", "¿Cuál nombre es seguro para guardar: «plano-rincon-1» o «Matilde-Rojas-calle-Flores-45»?", ["El segundo tiene nombre, apellido y dirección.", "Son datos personales.", "El primero no tiene datos personales."], "plano-rincon-1"),
        ("Compartir con permiso", "Quieres mostrar tu dibujo a tu abuela. ¿Qué haces primero?", ["Pienso: ¿quién me ayuda?", "Pido permiso a un adulto de mi casa.", "Luego se lo muestro a mi abuela."], "Pedir permiso a un adulto"),
    ],
    mistakes=[
        ("Poner mi nombre completo y mi dirección en el nombre del archivo.", "Cualquiera puede saber quién soy y dónde vivo.", "Usa un nombre que diga qué es el dibujo."),
        ("Compartir con alguien que no conozco.", "No sé si es seguro.", "Comparte solo con personas conocidas y con permiso de un adulto."),
    ],
    R=[
        ("¿Es seguro «dibujo-casa-1» como nombre de archivo? Responde sí o no.", "Sí", "No tiene datos personales."),
        ("¿Es seguro «Camila-Torres-colegio-Sol» como nombre de archivo? Responde sí o no.", "No", "Tiene nombre y colegio."),
        ("Antes de compartir un dibujo, ¿pides permiso o lo envías de una vez?", "Pides permiso", "Un adulto te cuida."),
    ],
    C=[
        ("¿Qué es un dato personal?", "Información que dice quién eres, como tu dirección", "No se debe compartir."),
        ("¿Por qué no se comparte con desconocidos?", "Porque no sé si es seguro", "Pueden hacer mal uso."),
        ("¿Qué significa respetar la autoría?", "Reconocer quién hizo el dibujo", "Cada persona merece crédito."),
    ],
    A=[
        ("Elige el nombre seguro: «mi-casa-roja», «Juan-Perez-12-años». Escribe cuál.", "mi-casa-roja", "El otro tiene nombre y edad."),
        ("Tienes 3 dibujos guardados y haces 2 más. ¿Cuántos dibujos tienes?", "5", "3 + 2 = 5."),
        ("Quieres mostrar el dibujo a: tu mamá, un desconocido y tu profesora. ¿A cuántas personas conocidas puedes mostrarlo con permiso?", "2", "Mamá y profesora."),
    ],
    Z=[
        ("Teo subió una foto de su compañera sin preguntarle. ¿Fue correcto? Responde sí o no.", "No", "Debió pedir permiso a ella y a un adulto."),
        ("Ema recibió el mensaje «te daré un premio si me dices tu dirección». ¿Debe responder? Responde sí o no.", "No", "Debe contarlo a un adulto."),
    ],
    D=[
        ("Escribe un nombre seguro para guardar un dibujo de un plano de tu salón.", "plano-salon-1", "No tiene datos personales."),
        ("Dibujaste 2 planos y tu hermano 1. Los guardas con tu nombre de autor «autor-A» en 2 y «autor-B» en 1. ¿Cuántos archivos tienen «autor-A»?", "2", "Los dos que tú hiciste."),
    ],
    ctx=("Lía terminó su plano y quiere guardarlo y mostrarlo. Su archivo se llama «plano-lia-calle-Roble-12». ¿Qué debe cambiar en el nombre?", "Quitar su dirección y su nombre", "Son datos personales."),
    sc=[
        ("¿Qué nombre es seguro: «plano-1» o «Rosa-Gómez-9-años»?", "plano-1", "No tiene datos personales."),
        ("¿A quién pides permiso antes de compartir?", "A un adulto", "Te ayuda a cuidar tus datos."),
        ("¿Puedes compartir con desconocidos? Responde sí o no.", "No", "No sabes quién es."),
    ],
    open_task=(
        "Elige uno de estos nombres para guardar tu plano y explica por qué: A) plano-rincon-lectura-1, B) Sofia-Reyes-9-anos-Calle-Pino. Luego escribe a quién sí le puedes mostrar tu dibujo (mamá, profesor, abuela, un desconocido) y qué pides antes de compartirlo.",
        "Elijo A porque no tiene datos personales. Puedo mostrarlo a mi mamá, mi profesor y mi abuela con permiso. Antes pido permiso a un adulto. No se lo muestro a desconocidos.",
        ["elige un nombre sin datos personales", "dice a quién puede mostrar", "pide permiso antes", "respeta la autoría"],
        ["nombre elegido con razón", "lista de personas"],
        ["nombres con datos personales", "compartir con desconocidos"],
        "Pide explicar qué dato personal tiene la opción B. Refuerza pedir permiso siempre.",
    ),
    reinforce="Escribe tres nombres seguros para tus dibujos.",
    extend="Explica a otra persona por qué no se comparten los datos personales.",
)

# ------------------------------------------------------------------ OA 06
reg(
    OA6, 1,
    materials="Un software educativo sencillo (sin cuenta infantil) en un dispositivo con un adulto, o la descripción de la pantalla que aparece en este cuaderno, que se resuelve sin conexión. También puedes usar tarjetas de papel.",
    use="Aprenderé a leer para qué sirve un programa educativo y a reconocer sus controles. Sirve para usarlo con seguridad y aprender de verdad.",
    prior=["Sé que un dispositivo se usa con permiso.", "Sé leer palabras cortas."],
    explain=[
        "Un software educativo es un programa para aprender algo, como clasificar objetos o contar. Los hay de muchos tipos: simuladores, libros digitales, juegos interactivos y programas para crear. En este cuaderno usamos un programa inventado, «Grupos de formas», solo para practicar. Antes de usarlo, lee el propósito, que es lo que dice que se hace en el programa, por ejemplo: «Arrastra cada objeto a su caja».",
        "Los controles son los botones y las zonas que se tocan. El botón de inicio comienza la actividad. La flecha avanza. El altavoz sube o baja el sonido. El signo de pregunta pide ayuda. La puerta o la X sale del programa. Antes de empezar, mira cada uno y pregunta si no entiendes.",
        "No necesitas cuenta ni datos personales para usar un programa educativo infantil. Si te pide tu nombre completo, tu edad o tu foto, para y avisa a un adulto. Usa el programa un rato corto, mira la pantalla con descansos y cierra bien al terminar.",
    ],
    vocab=[("software educativo", "programa para aprender algo"), ("propósito", "para qué sirve el programa"), ("control", "botón o zona que se toca"), ("ayuda", "botón que explica cómo seguir"), ("salir", "cerrar el programa")],
    worked=[
        ("Leer el propósito", "La pantalla dice: «Arrastra cada animal al grupo de los que vuelan o de los que caminan». ¿Cuál es el propósito?", ["Leo la frase.", "Pide mover animales a dos grupos.", "Es clasificar animales."], "Clasificar animales en dos grupos"),
        ("Elegir un control", "No sabes qué hacer. ¿Qué botón usas: ayuda o salir?", ["Necesito una explicación.", "El botón de ayuda da instrucciones."], "Ayuda"),
    ],
    mistakes=[
        ("Apretar botones sin leer el propósito.", "No se sabe qué se pide.", "Lee primero lo que dice la pantalla."),
        ("Poner el nombre completo cuando el programa lo pide.", "Es un dato personal.", "Para y pregunta a un adulto."),
    ],
    R=[
        ("¿El botón de ayuda explica cómo seguir o apaga el sonido?", "Explica cómo seguir", "Es su función."),
        ("¿El botón con una X sirve para salir o para empezar?", "Para salir", "La X cierra."),
        ("¿Un programa educativo sirve para aprender o solo para mirar?", "Para aprender", "Su propósito es educativo."),
    ],
    C=[
        ("¿Qué es el propósito de un programa?", "Para qué sirve", "Dice qué voy a hacer."),
        ("¿Qué haces si el programa pide tu nombre completo y tu dirección?", "Paras y avisas a un adulto", "Son datos personales."),
        ("¿Por qué se usa el programa poco tiempo seguido?", "Para descansar los ojos", "Cuida la salud."),
    ],
    A=[
        ("La pantalla dice: «Arrastra cada figura al grupo de los círculos o al grupo de los cuadrados». ¿Cuántos grupos hay?", "2", "Círculos y cuadrados."),
        ("Hay 6 figuras y ya clasificaste 4. ¿Cuántas faltan?", "2", "6 − 4 = 2."),
        ("Tienes 4 botones: inicio, ayuda, sonido y salir. ¿Cuál sirve para pedir instrucciones?", "Ayuda", "Explica cómo seguir."),
    ],
    Z=[
        ("Luis apretó salir y perdió su actividad. ¿Qué debió revisar antes de apretar?", "Qué hace el botón", "La X cierra el programa."),
        ("Una pantalla pide «escribe tu dirección para jugar». ¿Debes escribirla? Responde sí o no.", "No", "Es un dato personal."),
    ],
    D=[
        ("Si no hay dispositivo, ¿qué alternativa desconectada sirve para clasificar: tarjetas de papel con dibujos o ninguna?", "Tarjetas de papel con dibujos", "Se clasifica igual sin pantalla."),
        ("Clasificas 8 tarjetas: 5 son de animales que vuelan. ¿Cuántas son de los que no vuelan?", "3", "8 − 5 = 3."),
    ],
    ctx=("Pía abre un programa que dice: «Arrastra cada objeto a la caja de las cosas redondas o de las cosas cuadradas». Tiene 6 objetos. Escribe cuál es el propósito.", "Clasificar objetos en dos cajas", "Se mueve cada objeto a su caja."),
    sc=[
        ("¿Qué es un software educativo?", "Un programa para aprender", "Tiene un propósito educativo."),
        ("¿Qué botón sirve para pedir instrucciones?", "Ayuda", "Explica cómo seguir."),
        ("¿Das tus datos personales a un programa? Responde sí o no.", "No", "Debes avisar a un adulto."),
    ],
    open_task=(
        "Esta es la pantalla de «Grupos de formas», un programa inventado para este cuaderno: título «Grupos de formas», botones inicio, ayuda, sonido y salir, y la frase «Arrastra cada figura a su grupo: redondas o con esquinas». Hay 6 figuras: círculo, cuadrado, triángulo, óvalo, rectángulo, círculo. Escribe el propósito, qué hace cada botón y a qué grupo va cada figura.",
        "Propósito: clasificar figuras en redondas o con esquinas. Inicio comienza, ayuda explica, sonido cambia el volumen, salir cierra. Redondas: círculo, óvalo, círculo. Con esquinas: cuadrado, triángulo, rectángulo.",
        ["lee el propósito", "dice qué hace cada control", "clasifica las 6 figuras"],
        ["propósito escrito", "lista de botones", "clasificación"],
        ["no leer el propósito", "dar datos personales"],
        "Pide leer la pantalla en voz alta. Si una figura está mal clasificada, pregunta si tiene esquinas.",
    ),
    reinforce="Mira un juego educativo y nombra tres botones.",
    extend="Haz tarjetas de papel con figuras y clasifícalas sin pantalla.",
)

reg(
    OA6, 2,
    materials="Un software educativo o simulador sin cuenta, con un adulto, o la actividad de clasificación descrita en este cuaderno para resolver sin conexión. Lápiz y hoja.",
    use="Aprenderé a explorar un programa con una pregunta y a anotar lo que ocurre. Sirve para aprender probando con orden y no al azar.",
    prior=["Sé leer el propósito de un programa.", "Sé qué hace cada control."],
    explain=[
        "Explorar un programa es probar cosas para ver qué pasa. Es mejor explorar con una pregunta: «¿qué pasa si arrastro el triángulo a la caja de los círculos?». Una pregunta te dice qué probar y te ayuda a entender el programa.",
        "Prueba una cosa a la vez. Arrastra solo una figura, mira la respuesta del programa y anótala. Si cambias muchas cosas juntas, no sabrás cuál produjo el efecto. Anota: lo que probé y lo que pasó.",
        "Después responde tu pregunta con lo que viste. Si la respuesta no te convence, haz otra pregunta nueva. Explorar bien es probar con orden, anotar y sacar una conclusión. Recuerda usar el dispositivo con permiso y por poco tiempo.",
    ],
    vocab=[("explorar", "probar cosas para ver qué pasa"), ("pregunta", "algo que quiero saber"), ("anotar", "escribir lo que pasó"), ("conclusión", "lo que aprendí después de probar"), ("una cosa a la vez", "cambiar solo un elemento en cada prueba")],
    worked=[
        ("Hacer una pregunta", "En el programa inventado «Grupos de formas» quieres saber qué hace con un triángulo. Escribe una pregunta.", ["Pienso qué quiero saber.", "Quiero saber en qué grupo va el triángulo.", "Escribo: ¿en qué grupo cae el triángulo?"], "¿En qué grupo cae el triángulo?"),
        ("Anotar lo que pasó", "Arrastraste el triángulo al grupo de las redondas y el programa dijo «Inténtalo de nuevo». ¿Qué anotas?", ["Escribo lo que probé.", "Escribo lo que pasó.", "Anoto: triángulo en redondas, no correcto."], "Triángulo en redondas: no correcto"),
    ],
    mistakes=[
        ("Apretar muchos botones al azar.", "No se sabe qué causó el cambio.", "Haz una pregunta y prueba una cosa a la vez."),
        ("No anotar lo que pasó.", "Se olvida y no se aprende.", "Escribe lo que probaste y lo que ocurrió."),
    ],
    R=[
        ("¿Es mejor probar una cosa a la vez o muchas juntas?", "Una cosa a la vez", "Se ve el efecto de cada una."),
        ("«¿Qué pasa si arrastro el círculo?» ¿es una pregunta para explorar? Responde sí o no.", "Sí", "Dice qué probar."),
        ("Después de probar, ¿anotas lo que pasó o lo olvidas?", "Lo anotas", "Sirve para aprender."),
    ],
    C=[
        ("¿Para qué sirve explorar con una pregunta?", "Para saber qué probar", "La pregunta guía la exploración."),
        ("¿Qué anotas al explorar?", "Lo que probé y lo que pasó", "Son los datos de la prueba."),
        ("¿Cómo se llama lo que aprendes al responder tu pregunta después de probar?", "Conclusión", "Responde la pregunta inicial."),
    ],
    A=[
        ("Probaste 3 figuras: círculo (correcto), cuadrado (correcto), triángulo (incorrecto). ¿Cuántas fueron correctas?", "2", "Círculo y cuadrado."),
        ("Anotaste: círculo en redondas, cuadrado en esquinas, óvalo en redondas. ¿Cuántas pruebas anotaste?", "3", "Hay tres anotaciones."),
        ("Quieres saber qué hace el rectángulo. Escribe cuál de estas sirve como pregunta: «¿en qué grupo va el rectángulo?» o «¿cuántos días tiene la semana?»", "¿En qué grupo va el rectángulo?", "Es la pregunta sobre lo que probarás."),
    ],
    Z=[
        ("Ema movió 5 figuras de golpe y el programa dijo «incorrecto». No sabe cuál falló. ¿Qué debió hacer?", "Mover una figura a la vez", "Así sabe cuál falló."),
        ("Teo no anotó nada y ahora no recuerda qué probó. ¿Qué paso omitió?", "Anotar lo que probó", "Sin notas se pierde la información."),
    ],
    D=[
        ("Preguntas posibles: A) ¿en qué grupo va el óvalo?, B) ¿de qué color es el fondo? Si quieres aprender a clasificar, ¿cuál eliges?", "A", "Trata de la clasificación."),
        ("Pruebas: círculo → redondas (✔), cuadrado → redondas (✘), triángulo → esquinas (✔), óvalo → redondas (✔). ¿Cuántas ✘ hay?", "1", "Solo el cuadrado falló."),
    ],
    ctx=("Rita explora el programa «Grupos de formas» con la pregunta «¿en qué grupo va el cuadrado?». Arrastra el cuadrado a «con esquinas» y el programa inventado dice «Muy bien». ¿Qué anota?", "Cuadrado en con esquinas: correcto", "Registra lo que probó y lo que pasó."),
    sc=[
        ("¿Se explora mejor con una pregunta? Responde sí o no.", "Sí", "La pregunta guía qué probar."),
        ("¿Cuántas cosas pruebas a la vez?", "Una", "Así se ve el efecto."),
        ("¿Qué haces después de probar?", "Anotas y sacas una conclusión", "Se responde la pregunta."),
    ],
    open_task=(
        "Con las figuras de «Grupos de formas» (círculo, cuadrado, triángulo, óvalo) y los grupos redondas y con esquinas, haz esta pregunta: «¿en qué grupo va el triángulo?». En el programa inventado, si pones el triángulo en «con esquinas» dice «Muy bien»; si lo pones en «redondas» dice «Inténtalo de nuevo». Prueba el triángulo en «con esquinas». Escribe tu prueba, qué dijo el programa y tu conclusión.",
        "Pregunta: ¿en qué grupo va el triángulo? Probé triángulo en con esquinas y dijo «Muy bien». Conclusión: el triángulo va con las figuras con esquinas porque tiene tres esquinas.",
        ["escribe una pregunta", "prueba una cosa a la vez", "anota lo que pasó", "escribe una conclusión"],
        ["pregunta escrita", "nota de la prueba", "conclusión"],
        ["probar al azar", "no anotar"],
        "Pide leer la nota y decir cuál era la pregunta. Si la conclusión no responde la pregunta, que la reescriba.",
    ),
    reinforce="Haz una pregunta sobre un juego que conozcas y pruébala.",
    extend="Explora con otra pregunta: ¿en qué grupo va el rectángulo?",
)

reg(
    OA6, 3,
    materials="Los mensajes del programa escritos en este cuaderno, lápiz y hoja. Se resuelve sin conexión; también puedes usarlo con un programa real con un adulto.",
    use="Aprenderé a leer los mensajes que da el programa después de cada prueba y a decidir qué hacer. Sirve para aprender de los errores sin enojarme.",
    prior=["Sé explorar con una pregunta.", "Sé anotar lo que pasó."],
    explain=[
        "La retroalimentación es la respuesta del programa a lo que hiciste. Puede decir «muy bien», «inténtalo de nuevo» o dar una pista. Leerla bien te dice si acertaste y qué hacer después.",
        "Cuando el mensaje dice que está bien, anota lo que hiciste para repetirlo. Cuando dice que no, no es un castigo: es información. Lee la pista, como «las figuras redondas no tienen esquinas», y piensa qué cambiar. Prueba otra vez.",
        "A veces un mensaje no se entiende. Entonces usa el botón de ayuda o pregunta a un adulto. Si el programa te dice cosas que no te gustan o te pide datos personales, para y avisa a un adulto. Siempre es mejor entender el mensaje que apretar al azar.",
    ],
    vocab=[("retroalimentación", "respuesta del programa a lo que hiciste"), ("pista", "ayuda para pensar mejor"), ("acertar", "hacerlo bien"), ("error", "algo que sale mal y sirve para aprender"), ("repetir", "volver a intentar")],
    worked=[
        ("Leer una pista", "Pusiste el cuadrado en «redondas». El mensaje dice: «Mira las esquinas». ¿Qué haces?", ["Leo la pista.", "El cuadrado tiene esquinas.", "Lo muevo a con esquinas."], "Mover el cuadrado al grupo con esquinas"),
        ("Aprender del acierto", "El programa dice «Muy bien» al poner el círculo en redondas. ¿Qué anotas?", ["Anoto lo que hice.", "Círculo en redondas.", "Sirve para repetirlo."], "Círculo en redondas: correcto"),
    ],
    mistakes=[
        ("Enojarse con el mensaje de error.", "El error es información para aprender.", "Lee la pista y prueba otra cosa."),
        ("No leer el mensaje y seguir apretando.", "Se pierde la ayuda.", "Lee cada mensaje antes de volver a probar."),
    ],
    R=[
        ("El mensaje dice «Muy bien». ¿Acertaste o te equivocaste?", "Acertaste", "El mensaje confirma."),
        ("El mensaje dice «Inténtalo de nuevo». ¿Acertaste o te equivocaste?", "Te equivocaste", "Debes probar otra vez."),
        ("¿Una pista ayuda a pensar mejor o es un castigo?", "Ayuda a pensar mejor", "Es información útil."),
    ],
    C=[
        ("¿Qué es la retroalimentación?", "La respuesta del programa a lo que hiciste", "Dice si acertaste."),
        ("¿Qué haces cuando el mensaje es una pista?", "La lees y pruebas un cambio", "Te guía a corregir."),
        ("¿Qué haces si un mensaje no se entiende?", "Usas ayuda o preguntas a un adulto", "Es mejor entender."),
    ],
    A=[
        ("Mensaje: «Las redondas no tienen esquinas». Pusiste el triángulo en redondas. ¿A qué grupo lo cambias?", "Con esquinas", "El triángulo tiene esquinas."),
        ("Probaste 5 figuras. Tuviste 4 «Muy bien». ¿Cuántos «Inténtalo de nuevo» fueron?", "1", "5 − 4 = 1."),
        ("Mensaje: «Cuenta los lados: 4». Figura: cuadrado, triángulo o rectángulo. Escoge una que tenga 4 lados.", "Cuadrado o rectángulo", "Ambos tienen 4 lados."),
    ],
    Z=[
        ("Luis dice «el programa se equivocó» cuando recibió «Inténtalo de nuevo» tres veces con el mismo movimiento. ¿Qué debe hacer?", "Leer la pista y cambiar el movimiento", "Repetir lo mismo da el mismo mensaje."),
        ("Ana no lee los mensajes y solo aprieta. ¿Aprenderá lo que quiere el programa? Responde sí o no.", "No", "Sin leerlos pierde la ayuda."),
    ],
    D=[
        ("Escribe qué harías con el mensaje «Mira cuántos lados tiene» si pusiste un triángulo (3 lados) en un grupo de 4 lados.", "Cambiarlo al grupo de 3 lados", "Tiene 3 lados."),
        ("De 6 intentos, 2 tuvieron mensaje de error. ¿Cuántos fueron correctos?", "4", "6 − 2 = 4."),
    ],
    ctx=("Pía puso el óvalo en «con esquinas». El programa dijo: «Fíjate si hay esquinas». ¿A qué grupo debe cambiarlo?", "A redondas", "El óvalo no tiene esquinas."),
    sc=[
        ("¿Qué es retroalimentación?", "La respuesta del programa", "Dice si acertaste."),
        ("¿Un mensaje de error es un castigo? Responde sí o no.", "No", "Es información para aprender."),
        ("¿Qué haces con una pista?", "La lees y pruebas otra vez", "Te guía a corregir."),
    ],
    open_task=(
        "Lee estos tres intentos en «Grupos de formas» (programa inventado). 1) Cuadrado en redondas: «Inténtalo de nuevo, mira las esquinas». 2) Círculo en redondas: «Muy bien». 3) Triángulo en redondas: «Inténtalo de nuevo, cuenta los lados». Escribe para cada intento qué significa el mensaje y qué harías.",
        "1) Me equivoqué: el cuadrado tiene esquinas, lo muevo a con esquinas. 2) Acerté, anoto círculo en redondas. 3) Me equivoqué: el triángulo tiene 3 lados y esquinas, lo muevo a con esquinas.",
        ["lee cada mensaje", "dice si acertó o no", "decide qué hacer", "usa la pista"],
        ["tabla de tres filas", "frases de decisión"],
        ["no leer el mensaje", "enojarse con el error"],
        "Pide leer el mensaje y decir con sus palabras qué le dice el programa.",
    ),
    reinforce="Juega algo con un adulto y lee cada mensaje en voz alta.",
    extend="Explica a otra persona qué hacer cuando un programa dice inténtalo de nuevo.",
)

reg(
    OA6, 4,
    materials="Tarjetas de papel con los objetos descritos en este cuaderno y lápiz. Es una actividad desconectada que se resuelve sin pantalla.",
    use="Aprenderé a usar lo que aprendí en el programa en otra situación y a cerrar el programa bien. Sirve para aprender de verdad y usar los dispositivos con cuidado.",
    prior=["Sé clasificar figuras con un programa.", "Sé leer mensajes de retroalimentación."],
    explain=[
        "Transferir es usar lo que aprendiste en un lugar nuevo. En el programa aprendiste a clasificar figuras por esquinas. Ahora puedes clasificar objetos de tu casa: una pelota y una moneda son redondas, un libro y una caja tienen esquinas.",
        "Para transferir, piensa en qué regla usaste. La regla fue: si tiene esquinas, va con esquinas; si no tiene, va con redondas. Aplica la misma regla a las cosas nuevas. Si una cosa no entra en ninguna, crea un grupo nuevo y explica tu regla.",
        "Para cerrar bien, guarda lo que quieras conservar, sal del programa con el botón de salir y apaga o deja el dispositivo como estaba. Haz una pausa de pantalla, mira lejos y mueve el cuerpo. Dile a un adulto que terminaste.",
    ],
    vocab=[("transferir", "usar lo aprendido en otra situación"), ("regla", "idea que uso para decidir"), ("cerrar", "salir del programa y dejar todo como estaba"), ("pausa", "descanso para los ojos y el cuerpo"), ("clasificar", "poner en grupos según una regla")],
    worked=[
        ("Aplicar la regla", "Usa la regla de esquinas con una caja. ¿A qué grupo va?", ["Una caja tiene esquinas.", "La regla dice: esquinas va con esquinas.", "Va con esquinas."], "Con esquinas"),
        ("Cerrar bien", "Terminaste la actividad. Ordena: salir, guardar, avisar a un adulto.", ["Primero guardo.", "Luego salgo con el botón.", "Finalmente aviso a un adulto."], "Guardar, salir, avisar"),
    ],
    mistakes=[
        ("Apagar el dispositivo sin salir ni guardar.", "Se puede perder lo hecho.", "Guarda y sal con el botón de salir."),
        ("Usar la pantalla sin descansar.", "Cansa los ojos.", "Haz pausas y mira lejos."),
    ],
    R=[
        ("Una moneda es redonda. ¿Va con redondas o con esquinas?", "Con redondas", "No tiene esquinas."),
        ("Un libro tiene esquinas. ¿Va con redondas o con esquinas?", "Con esquinas", "El libro tiene esquinas."),
        ("Al terminar, ¿sales con el botón o dejas todo abierto?", "Sales con el botón", "Es cerrar bien."),
    ],
    C=[
        ("¿Qué significa transferir?", "Usar lo aprendido en otra situación", "Se aplica en un lugar nuevo."),
        ("¿Para qué haces una pausa de pantalla?", "Para descansar los ojos y el cuerpo", "Cuida la salud."),
        ("¿Qué regla usaste para clasificar figuras?", "Con esquinas o sin esquinas", "Esa regla separa los grupos."),
    ],
    A=[
        ("Clasifica con la regla: pelota, caja, plato redondo, cuaderno. ¿Cuántos tienen esquinas?", "2", "Caja y cuaderno."),
        ("Tienes 7 tarjetas de objetos y 3 son redondos. ¿Cuántos tienen esquinas?", "4", "7 − 3 = 4."),
        ("Escribe cuál de estos va con redondas: dado, moneda, libro.", "Moneda", "La moneda no tiene esquinas."),
    ],
    Z=[
        ("Tato dice que un huevo va con esquinas. ¿Es correcto? Responde sí o no.", "No", "El huevo no tiene esquinas."),
        ("Una cosa tiene una parte redonda y otra con esquinas, como una puerta con ventana redonda. ¿Qué haces con la regla?", "Creas un grupo nuevo o explicas tu regla", "No entra en un solo grupo."),
    ],
    D=[
        ("Clasifica 8 objetos: 3 redondos, 4 con esquinas y 1 mezclado. ¿Cuántos van en un grupo nuevo?", "1", "El mezclado no entra en los otros."),
        ("Un ciclo dura 15 minutos: usas la pantalla un rato y luego haces una pausa de 5 minutos. ¿Cuántos minutos usas la pantalla en cada ciclo?", "10", "15 − 5 = 10."),
    ],
    ctx=("Lía tiene 6 objetos de su pieza: pelota, caja de zapatos, reloj redondo, cuaderno, moneda y pizarra rectangular. Clasifica con la regla de esquinas. ¿Cuántos van con esquinas?", "3", "Caja, cuaderno y pizarra."),
    sc=[
        ("¿Qué es transferir?", "Usar lo aprendido en otra situación", "Se aplica en lo nuevo."),
        ("¿Cómo cierras un programa?", "Con el botón de salir", "Se cierra bien."),
        ("¿Descansas la vista? Responde sí o no.", "Sí", "Se hacen pausas."),
    ],
    open_task=(
        "Clasifica estos 8 objetos con la regla del programa (redondos o con esquinas): pelota, libro, moneda, caja de zapatos, plato redondo, cuaderno, tapa de frasco, ventana rectangular. Escribe los dos grupos y tu regla. Luego escribe tres pasos para cerrar bien un programa.",
        "Redondos: pelota, moneda, plato, tapa de frasco. Con esquinas: libro, caja de zapatos, cuaderno, ventana. Regla: si tiene esquinas, va con esquinas. Cerrar: guardar, salir, avisar a un adulto.",
        ["aplica la regla", "forma dos grupos", "explica la regla", "describe cómo cerrar"],
        ["dos listas", "frase de regla", "tres pasos de cierre"],
        ["grupos mal formados", "no cerrar bien"],
        "Pide decir la regla antes de clasificar. Si un objeto está mal, pregunta si tiene esquinas.",
    ),
    reinforce="Clasifica 6 cosas de tu pieza en redondas y con esquinas.",
    extend="Inventa otra regla para clasificar objetos y úsala.",
)

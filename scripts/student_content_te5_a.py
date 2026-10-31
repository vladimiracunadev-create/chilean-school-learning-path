"""Cuaderno del estudiante, 5.º básico Tecnología: OA 01 (diseñar objetos o sistemas tecnológicos), clases 1 a 6.

Seguridad: solo papel, cartón, cinta, cordel y tijeras de punta roma; nada de cortadores, fuego, vidrio ni herramientas con filo.
Medidas enteras en centímetros y gramos. Las pantallas se describen con texto, son ejemplos sin marcas y todo tiene alternativa en papel.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE05 OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    def conv(i):
        return i if isinstance(i, dict) else ex(*i)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [conv(i) for i in R], "understand": [conv(i) for i in C], "apply": [conv(i) for i in A], "reason": [conv(i) for i in Z], "challenge": [conv(i) for i in D]},
        context=[conv(ctx)], selfcheck=[conv(i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01, clase 1
reg(
    OA1, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus ideas.",
    use="Aprenderé a partir de un problema o de una oportunidad, con ejemplos de la vida diaria y de otras asignaturas, y a escribir criterios que se puedan comprobar. Sirve para decidir con datos y no por gusto.",
    prior=["Sé que un usuario es la persona que usará un objeto.", "Sé que un criterio es una condición que se puede comprobar.", "Sé que una restricción es un límite."],
    explain=[
        "Un objeto o sistema tecnológico nace de una necesidad. La necesidad puede ser un problema, que es algo que falla o cuesta lograr, o una oportunidad, que es algo que se puede aprovechar. Un problema: se pierden los lápices. Una oportunidad: el curso junta cajas de cartón y podrían servir para guardar cosas.",
        "Las ideas para diseñar salen de muchos ámbitos: la casa, la escuela, el transporte, la comunicación o el cuidado del ambiente. También salen de otras asignaturas. En Ciencias Naturales, una planta necesita agua; en Matemática, un cuerpo geométrico tiene medidas; en Historia, un mapa se puede representar en una maqueta.",
        "Antes de dibujar, escribe tres cosas: el usuario, la necesidad sin nombrar el objeto y dos criterios con número o acción observable. Ejemplo de criterio: «sostiene 9 fichas» o «cabe en una mochila de 30 cm de alto». Los criterios sirven después para elegir entre ideas y para probar el resultado.",
    ],
    vocab=[("necesidad", "problema que resolver u oportunidad que aprovechar"), ("oportunidad", "algo que podría mejorar o aprovecharse aunque nada falle"), ("ámbito", "área de la vida donde se usa la tecnología"), ("criterio", "condición comprobable que el diseño debe cumplir"), ("sistema tecnológico", "conjunto de partes que trabajan juntas para lograr algo")],
    worked=[
        ("Distinguir problema y oportunidad", "Caso A: a Lía se le olvida regar la planta de la sala. Caso B: el colegio tiene 40 tapas de botella limpias y sin uso. ¿Cuál es problema y cuál oportunidad?", ["En A algo falla: la planta no recibe agua a tiempo.", "En B nada falla, pero hay un recurso que se podría aprovechar."], "A es un problema y B es una oportunidad"),
        ("Escribir usuario, necesidad y criterios", "Los estudiantes del patio no saben qué hora es en el recreo. Escribe usuario, necesidad y dos criterios.", ["Usuario: los estudiantes del patio.", "Necesidad sin objeto: saber cuánto falta para terminar el recreo.", "Criterios con números: se ve desde 10 pasos de distancia; marca 5 minutos de aviso."], "Usuario: estudiantes del patio. Necesidad: saber cuánto falta del recreo. Criterios: se ve desde 10 pasos y marca el aviso de 5 minutos"),
    ],
    mistakes=[
        ("Pensar que solo se diseña cuando algo está roto.", "También se diseña para aprovechar una oportunidad.", "Pregunta: «¿qué falla?» y «¿qué podría aprovechar?»."),
        ("Escribir el criterio «debe ser genial».", "No se puede medir ni contar.", "Usa un número o una acción que se vea."),
    ],
    R=[
        ("A Tomás se le pierde la llave de su bicicleta cada semana. ¿Es un problema o una oportunidad?", "Un problema", "Algo falla, porque la llave se pierde."),
        ("El curso junta 30 botellas plásticas cada mes y podrían servir para hacer algo útil. ¿Es un problema o una oportunidad?", "Una oportunidad", "No falla nada; hay un recurso que se puede aprovechar."),
        ("En «Los vecinos necesitan saber cuándo pasa el camión de basura», ¿quién es el usuario?", "Los vecinos", "El usuario es quien usará lo que se diseñe."),
    ],
    C=[
        ("¿Cuál es un criterio comprobable? A «Se ve genial», B «Cabe en una mochila de 30 cm de alto», C «Es súper útil».", "B", "Solo B se comprueba con una medida."),
        ("Un grupo quiere hacer una maqueta del mapa de su región. ¿De qué asignatura viene ese tópico? A Historia, Geografía y Ciencias Sociales, B Educación Física.", "A", "Los mapas y las regiones se estudian en Historia, Geografía y Ciencias Sociales."),
        ("¿Por qué conviene escribir los criterios antes de dibujar?", "Para elegir entre ideas con una medida y no por gusto", "Los criterios permiten comparar las ideas con datos."),
    ],
    A=[
        arith("Un diseño debe sostener 9 fichas y por ahora sostiene 6. ¿Cuántas fichas más debe sostener para cumplir el criterio?", "9-6", "Se resta lo que ya sostiene de lo que debe sostener."),
        ("¿Cuál frase describe la necesidad sin nombrar un objeto? A «Inés necesita un cartel», B «Inés necesita ubicar un libro en la biblioteca».", "B", "A ya nombra una solución; B dice lo que se debe lograr."),
        ("Elige el criterio comprobable para «que no se vuelque»: A «Resiste 3 empujones suaves sin volcarse», B «Es difícil de volcar».", "A", "A tiene un número y se puede probar."),
    ],
    Z=[
        ("Ana define el criterio «sostiene 9 fichas» y Beto define «es bien firme». Ambos presentan un soporte que sostiene 7 fichas. ¿Quién puede decir con seguridad si cumple?", "Ana", "Con un número se sabe si 7 llega o no a 9; «firme» no se puede decidir."),
        ("Hans dice: «Si nada falla, no hay necesidad de diseñar». ¿Está en lo correcto?", "No", "Una necesidad también puede ser aprovechar una oportunidad."),
    ],
    D=[
        arith("El desafío pide una base de 20 cm de largo y 20 cm de ancho como máximo. Un diseño mide 20 cm de largo y 14 cm de ancho. ¿Cuántos centímetros más de ancho podría tener sin pasar el límite?", "20-14", "Se resta el ancho actual del ancho máximo."),
        ("Criterios: «sostiene al menos 9 fichas» y «base de 20 cm como máximo». Idea 1: 9 fichas y 18 cm. Idea 2: 10 fichas y 24 cm. Idea 3: 8 fichas y 15 cm. ¿Cuál cumple ambos?", "La idea 1", "La 2 pasa los 20 cm y la 3 no llega a 9 fichas."),
    ],
    ctx=("En Ciencias Naturales estudian que una semilla necesita agua para brotar. En tu casa tienes un vaso de papel con una semilla y a veces se te olvida regarla. Escribe usuario, si es problema u oportunidad, la necesidad sin nombrar un objeto y un criterio con número.", "Usuario: tú. Es un problema porque se olvida regar. Necesidad: recordar cuándo regar la semilla. Criterio: avisa una vez al día", "Cubre usuario, tipo de necesidad, necesidad sin objeto y un criterio con número."),
    sc=[
        ("¿Una necesidad puede ser una oportunidad?", "Sí", "También se diseña para aprovechar algo."),
        ("¿La necesidad nombra el objeto que se va a construir?", "No", "Dice qué se debe lograr, no la solución."),
        ("¿Cómo debe ser un criterio?", "Comprobable, con número o acción observable", "Así se puede decidir si se cumple."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: en la sala, a 4 de 9 compañeros se les caen las colaciones al abrir la mochila. Caso 2: el colegio tiene 25 tapas de botella limpias y sin uso. Escribe si es problema u oportunidad, el usuario, la necesidad sin nombrar un objeto y dos criterios con número.",
        "Caso 2: oportunidad. Usuario: el curso. Necesidad: aprovechar las tapas. Criterios: usa las 25 tapas; se sostiene sola.",
        ["dice si es problema u oportunidad", "nombra al usuario", "la necesidad no nombra un objeto", "dos criterios con número o acción observable"],
        ["ficha con tipo de necesidad, usuario, necesidad y dos criterios"],
        ["nombrar el objeto en la necesidad", "criterios que no se pueden comprobar"],
        "Pregunta: «¿cómo sabrías si el diseño cumple este criterio?». Si no lo puede contar o medir, pídele agregar un número.",
    ),
    reinforce="Observa un objeto de tu casa y escribe qué necesidad resuelve y para quién.",
    extend="Elige un tema que veas en Ciencias o en Historia y escribe una necesidad que un objeto podría resolver con ese tema.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja cuadriculada o común, lápiz y regla. Las medidas están escritas en este cuaderno.",
    use="Aprenderé a representar una idea con un boceto a mano alzada y con un dibujo técnico de vistas con medidas. Sirve para que otra persona pueda construir lo que imaginaste.",
    prior=["Sé que un boceto es un dibujo rápido a mano alzada.", "Sé medir con regla en centímetros.", "Sé que un criterio se puede comprobar."],
    explain=[
        "Un diseño se puede representar de dos maneras. El boceto se hace a mano alzada, es decir, sin regla, para probar ideas rápido. Es útil al comienzo, porque se puede cambiar muchas veces. El dibujo técnico se hace con regla y lleva medidas; es útil cuando ya elegiste una idea y otra persona debe construirla.",
        "El dibujo técnico muestra el objeto en vistas. La vista frontal es lo que ves de frente: muestra el ancho y el alto. La vista superior es lo que ves desde arriba: muestra el ancho y el fondo, que es la distancia de adelante hacia atrás. La vista lateral es la que ves de costado: muestra el fondo y el alto.",
        "Las medidas se escriben sobre el dibujo y se llaman cotas. Se anotan en centímetros. A veces el objeto es muy grande para el papel y se dibuja en escala. Escala 1:2 significa que cada 1 cm del dibujo vale 2 cm del objeto real. Por eso el dibujo es la mitad del tamaño real.",
    ],
    vocab=[("boceto", "dibujo rápido a mano alzada"), ("dibujo técnico", "dibujo con regla, vistas y medidas"), ("vista", "forma de mirar el objeto: de frente, desde arriba o de costado"), ("cota", "medida escrita sobre el dibujo"), ("escala", "relación entre el dibujo y el tamaño real")],
    worked=[
        ("Leer las medidas de las vistas", "Una caja mide 12 cm de ancho, 8 cm de fondo y 5 cm de alto. ¿Qué medidas se ven en la vista frontal y en la superior?", ["La frontal muestra ancho y alto: 12 cm y 5 cm.", "La superior muestra ancho y fondo: 12 cm y 8 cm."], "Frontal: 12 cm y 5 cm. Superior: 12 cm y 8 cm"),
        ("Pasar de la escala al tamaño real", "En un dibujo a escala 1:2, el largo de un soporte mide 9 cm. ¿Cuánto mide el soporte real?", ["Cada 1 cm del dibujo vale 2 cm reales.", "Multiplico 9 × 2."], "18 cm"),
    ],
    mistakes=[
        ("Dibujar con regla y medidas cuando recién buscas ideas.", "Se pierde tiempo y se tiende a quedarse con la primera idea.", "Haz primero varios bocetos rápidos y después el dibujo técnico de la idea elegida."),
        ("Mezclar el alto y el fondo al leer las vistas.", "Cada vista muestra solo dos medidas del objeto.", "Recuerda: frontal ancho y alto, superior ancho y fondo, lateral fondo y alto."),
    ],
    R=[
        ("¿Cuál se hace sin regla, el boceto o el dibujo técnico?", "El boceto", "A mano alzada quiere decir sin regla."),
        ("¿Qué vista muestra el ancho y el alto de un objeto?", "La vista frontal", "Es lo que ves de frente."),
        ("Una medida escrita sobre el dibujo, como 12 cm, ¿cómo se llama?", "Cota", "Las medidas del dibujo técnico se llaman cotas."),
    ],
    C=[
        ("Para probar cinco ideas en pocos minutos, ¿conviene boceto o dibujo técnico?", "Boceto", "Es rápido y se puede cambiar."),
        ("Una caja mide 15 cm de ancho, 10 cm de fondo y 6 cm de alto. ¿Qué dos medidas muestra la vista superior?", "15 cm y 10 cm", "La superior muestra ancho y fondo."),
        ("¿Qué significa que un dibujo está en escala 1:2?", "Que el dibujo mide la mitad del tamaño real", "Cada 1 cm del dibujo vale 2 cm reales."),
    ],
    A=[
        arith("Un objeto real mide 24 cm de alto. En un dibujo a escala 1:2, ¿cuántos centímetros mide el alto dibujado?", "24//2", "En escala 1:2 el dibujo mide la mitad."),
        arith("En un dibujo a escala 1:2, el ancho de un estante mide 13 cm. ¿Cuántos centímetros mide el estante real?", "13*2", "El objeto real mide el doble del dibujo."),
        ("Un estante mide 40 cm de ancho, 20 cm de fondo y 30 cm de alto. ¿Qué dos medidas, en este orden, muestra su vista lateral: fondo y alto?", "20 cm y 30 cm", "La lateral muestra el fondo y el alto, no el ancho."),
    ],
    Z=[
        ("Para construir un soporte, Bruno solo tiene la vista frontal con 18 cm de ancho y 6 cm de alto. ¿Qué medida del objeto aún no conoce?", "El fondo", "La frontal no muestra la distancia de adelante hacia atrás."),
        ("Clara hizo un boceto y Mario un dibujo técnico con cotas. Ambos dibujos son de una caja que otra persona construirá sin hablar con ellos. ¿Cuál ayuda más y por qué?", "El de Mario, porque trae medidas", "Con cotas se puede construir sin adivinar."),
    ],
    D=[
        arith("Un soporte tiene 18 cm de ancho, 6 cm de alto y 12 cm de fondo. Se dibuja en escala 1:2. ¿Cuántos centímetros mide el fondo en el dibujo?", "12//2", "Se divide la medida real entre 2."),
        ("Una base real de 20 cm de ancho y 20 cm de fondo se dibuja en escala 1:2. El límite del dibujo es una hoja de 12 cm de ancho. ¿Cabe?", "Sí", "La base dibujada mide 10 cm y 10 cm, y 10 es menor que 12."),
    ],
    ctx=("Quieres que alguien de tu casa fabrique un porta-fichas de cartón que mide 16 cm de ancho, 10 cm de fondo y 4 cm de alto. Escribe las medidas de la vista frontal, de la superior y de la lateral.", "Frontal: 16 y 4. Superior: 16 y 10. Lateral: 10 y 4", "Cada vista muestra solo dos medidas."),
    sc=[
        ("¿El boceto lleva regla?", "No", "Es a mano alzada."),
        ("¿Qué dos medidas muestra la vista superior?", "Ancho y fondo", "Se ve el objeto desde arriba."),
        ("En escala 1:2, ¿el dibujo es más grande o más pequeño que el objeto?", "Más pequeño", "Cada 1 cm del dibujo vale 2 cm reales."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un porta-lápices de 8 cm de ancho, 8 cm de fondo y 10 cm de alto. Objeto 2: una caja de 14 cm de ancho, 9 cm de fondo y 6 cm de alto. Haz un boceto a mano alzada y las tres vistas con cotas en papel cuadriculado, con 1 cuadro por cada 1 cm.",
        "Objeto 2: frontal de 14 por 6, superior de 14 por 9, lateral de 9 por 6, con cotas escritas.",
        ["boceto a mano alzada", "tres vistas dibujadas", "las cotas coinciden con las medidas del objeto", "cada vista muestra las dos medidas correctas"],
        ["boceto y tres vistas con cotas"],
        ["intercambiar alto y fondo", "olvidar escribir las cotas"],
        "Pregunta: «¿qué dos medidas muestra esta vista?». Si no coinciden con las cotas, pídele mirar el objeto de nuevo.",
    ),
    reinforce="Mide un libro de tu casa y anota su ancho, su alto y su grosor. Dibuja la vista frontal con esas medidas.",
    extend="Dibuja a escala 1:2 la vista frontal de una repisa de 36 cm de ancho y 24 cm de alto. Anota cuánto mide en el dibujo.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja y lápiz. El producto que se analiza está descrito en este cuaderno; si quieres, usa también un estuche o una lonchera de tu casa.",
    use="Aprenderé a analizar un producto que ya existe (sus partes, su función y sus materiales) y a decidir una modificación segura. Sirve para mejorar objetos sin partir de cero.",
    prior=["Sé que un criterio se puede comprobar.", "Sé que un objeto está hecho de materiales.", "Sé leer vistas con medidas."],
    explain=[
        "Analizar un producto es descomponerlo en preguntas. ¿Para qué sirve? Eso es su función. ¿De qué partes está hecho? ¿De qué material es cada parte? ¿Cómo se usa? ¿Qué parte falla o molesta? Cada respuesta se anota en una tabla con partes, función y material. Así se ve con claridad qué se podría cambiar.",
        "Modificar un producto es cambiarle algo para que cumpla mejor un criterio. Se puede cambiar el material, la forma, el tamaño o la manera de unir las partes. Primero escribe qué criterio mejoraría el cambio. Luego revisa si el cambio necesita otros materiales, más tiempo o medidas de seguridad nuevas.",
        "Conviene modificar una sola cosa a la vez. Si cambias tres cosas juntas y el producto mejora, no sabrás cuál de las tres ayudó. Guarda el producto original o su dibujo para poder comparar el antes con el después. Una modificación que obliga a usar herramientas peligrosas se descarta o se hace solo con una persona adulta.",
    ],
    vocab=[("función", "para qué sirve una parte o el objeto completo"), ("parte", "pieza que forma el objeto"), ("modificar", "cambiar algo de un producto para que mejore"), ("producto original", "el objeto tal como estaba antes del cambio"), ("variable", "lo que cambias para ver su efecto")],
    worked=[
        ("Analizar un estuche", "Un estuche de tela tiene un cierre de plástico, el cuerpo es de tela y dentro lleva un separador de cartón. Los lápices se caen al abrirlo. Haz la tabla de partes y señala qué parte falla.", ["Cierre: plástico, sirve para abrir y cerrar. Cuerpo: tela, sirve para guardar. Separador: cartón, sirve para ordenar.", "Los lápices se caen por cómo está puesto el separador, no por el cierre."], "La parte que falla es el separador, que no sujeta los lápices"),
        ("Elegir qué modificar", "Para que los lápices no se caigan puedes: A cambiar la tela por plástico, el cierre y el separador, o B agregar una banda elástica al separador. ¿Cuál conviene probar primero?", ["A cambia tres cosas a la vez.", "B cambia una sola variable y es fácil de probar."], "B, porque cambia una sola cosa"),
    ],
    mistakes=[
        ("Cambiar varias partes a la vez para mejorar rápido.", "No se sabe cuál cambio produjo la mejora.", "Modifica una sola variable y prueba."),
        ("Modificar sin guardar el original.", "No se puede comparar el antes con el después.", "Guarda el producto original o hazle un dibujo con medidas."),
    ],
    R=[
        ("En un estuche, ¿para qué sirve el cierre?", "Para abrir y cerrar el estuche", "Esa es la función del cierre."),
        ("En unas tijeras de punta roma, «cortar papel» ¿es una parte, una función o un material?", "Una función", "Dice para qué sirven las tijeras."),
        ("Cambiar el material de una parte, ¿es analizar o es modificar el producto?", "Modificar", "Modificar es cambiar algo del producto."),
    ],
    C=[
        ("Una lonchera tiene solo tres partes: tapa, asa y cuerpo. ¿Cuál parte sirve para llevarla?", "El asa", "La función del asa es llevar la lonchera."),
        ("¿Por qué conviene cambiar una sola variable a la vez?", "Porque así se sabe qué cambio produjo la mejora", "Si cambian varias, no se sabe cuál ayudó."),
        ("¿Qué se debe hacer con el producto original antes de modificarlo?", "Guardarlo o dibujarlo con medidas", "Sirve para comparar el antes con el después."),
    ],
    A=[
        arith("Un estuche tenía 6 lápices y se caían 4 al abrirlo. Después de la modificación se cae 1. ¿Cuántos lápices menos se caen ahora?", "4-1", "Se resta lo que se cae ahora de lo que se caía antes."),
        ("Un asa de cordel se corta con 2 kilos. Se cambia solo el material por una tira de tela gruesa y se prueba con 4 kilos. ¿Qué variable se cambió?", "El material del asa", "Solo cambió el material."),
        ("Una modificación propone serrar madera para hacer una tapa nueva. ¿Qué se debe hacer?", "Hacerla solo con una persona adulta o descartarla", "Serrar es peligroso para estudiantes sin supervisión."),
    ],
    Z=[
        ("Dos compañeras mejoran un portavasos. Una cambia el material y el tamaño; la otra solo el tamaño. Ambos portavasos mejoran. ¿Quién puede decir qué cambio ayudó?", "La que cambió solo el tamaño", "Con una sola variable se sabe cuál fue la causa."),
        ("Un producto cumple el criterio «sostiene 8 fichas» pero la modificación obliga a usar una pistola de silicona caliente, que solo maneja una persona adulta. ¿Qué hay que revisar además de si sostiene las fichas?", "La seguridad", "Toda modificación debe revisar los riesgos del material o la herramienta."),
    ],
    D=[
        arith("Un asa soportaba 2 kilos y con el cambio de material soporta 5 kilos. ¿Cuántos kilos más soporta?", "5-2", "Se resta lo que soportaba antes."),
        ("Un estuche pesa 120 gramos y la modificación agrega una banda de 15 gramos. El criterio es «pesa 130 gramos como máximo». ¿Cumple?", "No", "120 más 15 son 135, mayor que 130."),
    ],
    ctx=("Analiza esta lonchera: el cuerpo es de plástico, la tapa se une con dos broches de plástico y el asa es de cordel. A veces se abre sola en la mochila. Haz la tabla de partes con función y material, y propone una sola modificación que mejore el cierre.", "Cuerpo de plástico, guarda; tapa de plástico, cierra; broches de plástico, sujetan la tapa; asa de cordel, sirve para llevarla. Modificación: agregar una banda elástica sobre la tapa", "Incluye la tabla completa y una sola variable."),
    sc=[
        ("¿Qué es la función de una parte?", "Para qué sirve", "Dice lo que la parte logra."),
        ("¿Cuántas variables conviene cambiar a la vez?", "Una", "Así se sabe qué produjo la mejora."),
        ("¿Qué se guarda antes de modificar?", "El producto original o su dibujo", "Permite comparar el antes con el después."),
    ],
    open_task=(
        "Escoge un producto. Producto 1: un estuche de tela con cierre de plástico y separador de cartón. Producto 2: una regla de plástico de 30 cm con números pintados que se borran. Haz una tabla de partes, función y material; escribe el criterio que mejorará la modificación y propón una sola modificación segura.",
        "Producto 2: parte: cuerpo, función: medir, material: plástico. Criterio: los números no se borran. Modificación: cubrir los números con cinta transparente.",
        ["tabla de partes con función y material", "criterio que mejora la modificación", "cambia una sola variable", "la modificación es segura con papel, cartón y cinta"],
        ["tabla de análisis y propuesta de modificación"],
        ["cambiar varias cosas a la vez", "olvidar el criterio que mejora el cambio"],
        "Pregunta: «¿cuántas cosas cambias? ¿cómo sabrías que mejoró?». Si cambia varias, pídele elegir solo una.",
    ),
    reinforce="Elige un objeto de tu casa que no sea peligroso y anota sus partes, su función y su material.",
    extend="Escribe dos modificaciones posibles para el mismo objeto y di cuál probarías primero y por qué.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Papel cuadriculado y lápiz. Si tienes computador o tableta, un programa de dibujo o de presentaciones; si no, haz todo en papel.",
    use="Aprenderé a representar un diseño con un programa de dibujo o de presentaciones usando formas, medidas y alineación. Sirve para corregir un diseño sin borrar todo ni empezar de nuevo.",
    prior=["Sé hacer vistas con medidas.", "Sé que una cota es una medida en el dibujo.", "Sé guardar un archivo con nombre."],
    explain=[
        "Un programa de dibujo o de presentaciones permite diseñar con TIC, que son las tecnologías de la información y la comunicación. Se dibuja con formas básicas: rectángulos, círculos y líneas. Cada forma se puede mover, cambiar de tamaño y copiar. Así un diseño se arma como un rompecabezas y se corrige sin borrar nada.",
        "Para que el dibujo tenga medidas se usa una cuadrícula o una regla en pantalla. Si cada cuadro vale 1 cm, un rectángulo de 12 cuadros de ancho representa 12 cm. Muchos programas dejan escribir el tamaño exacto de una forma. Así dos personas obtienen el mismo dibujo. En papel cuadriculado se hace igual.",
        "Hay herramientas que ordenan el trabajo. Alinear deja varias formas en la misma línea. Agrupar une varias formas para moverlas como una sola. Copiar repite una pieza igual. Guardar con un nombre claro, por ejemplo soporte_vista_frontal, evita perder el diseño. Cada programa se ve distinto: busca el equivalente en el que uses.",
    ],
    vocab=[("TIC", "tecnologías de la información y la comunicación"), ("forma", "figura básica que se inserta: rectángulo, círculo o línea"), ("alinear", "dejar varias formas en una misma línea"), ("agrupar", "unir varias formas para moverlas como una"), ("cuadrícula", "red de cuadros que ayuda a medir")],
    worked=[
        ("Dibujar con cuadrícula", "En una cuadrícula donde cada cuadro vale 1 cm, dibuja la vista frontal de una caja de 12 cm de ancho y 5 cm de alto. ¿Cuántos cuadros mide cada lado?", ["El ancho es 12 cm, que son 12 cuadros.", "El alto es 5 cm, que son 5 cuadros."], "12 cuadros de ancho y 5 de alto"),
        ("Elegir la herramienta", "Dibujaste las 4 patas de una mesa y quieres moverlas juntas hacia la derecha sin cambiar su distancia. ¿Qué haces?", ["Si las muevo una a una, se pueden descolocar.", "Las selecciono y las agrupo; luego muevo el grupo."], "Agruparlas y mover el grupo"),
    ],
    mistakes=[
        ("Estirar una forma con el mouse hasta que «se vea bien» sin mirar la medida.", "El tamaño queda sin medida real y no coincide con el diseño.", "Escribe el tamaño exacto o cuenta los cuadros."),
        ("Guardar el archivo con el nombre «sin título» o «nuevo».", "Después no se sabe qué contiene.", "Usa un nombre que diga el contenido, como soporte_vista_frontal."),
    ],
    R=[
        ("¿Cómo se llama la herramienta que deja varias formas en una misma línea?", "Alinear", "Alinear ordena las formas sobre una línea."),
        ("Si cada cuadro vale 1 cm, ¿cuántos cuadros mide una línea de 7 cm?", "7", "Cada centímetro es un cuadro."),
        ("¿Qué herramienta une varias formas para moverlas como una sola?", "Agrupar", "Agrupar las deja unidas."),
    ],
    C=[
        ("¿Por qué conviene dibujar con formas y no con un trazo a mano alzada para un diseño con medidas?", "Porque las formas se pueden medir y corregir", "Cada forma tiene tamaño exacto y se puede mover."),
        ("Un rectángulo de 6 cm de ancho y 4 cm de alto se copia 3 veces. ¿Cuántas piezas iguales hay en total, con el original?", "4", "Hay una original y tres copias."),
        ("¿Cuál nombre de archivo es mejor? A «nuevo2», B «porta_fichas_planta».", "B", "B dice qué contiene."),
    ],
    A=[
        arith("En una cuadrícula con 1 cuadro por cm, dibujas una base de 20 cuadros de ancho. La hoja de la pantalla tiene 26 cuadros de ancho. ¿Cuántos cuadros sobran a lo ancho?", "26-20", "Se resta el ancho de la base del ancho de la hoja."),
        arith("Dibujas 5 patas iguales de un mueble. Cada pata ocupa 3 cuadros de ancho, sin espacios entre ellas. ¿Cuántos cuadros de ancho ocupan juntas?", "5*3", "Se multiplican las patas por el ancho de cada una."),
        ("Tienes dos formas, una más a la izquierda que la otra. Quieres que queden en la misma línea horizontal. ¿Qué herramienta usas?", "Alinear", "Alinear las deja en la misma línea."),
    ],
    Z=[
        ("Julia y Omar dibujaron la misma caja de 10 cm de ancho. Julia contó 10 cuadros; Omar la estiró a ojo. ¿Quién tiene seguridad de la medida y por qué?", "Julia, porque contó los cuadros", "Contar da la medida exacta; estirar a ojo no."),
        ("Un diseño tiene 8 formas y quieres moverlo completo. ¿Es mejor mover una a una o agruparlas, y por qué?", "Agruparlas, porque así no se descolocan", "Las formas agrupadas se mueven con la misma distancia entre ellas."),
    ],
    D=[
        arith("El diseño completo ocupa 24 cuadros de ancho y quieres agregar un margen de 2 cuadros a cada lado. ¿Cuántos cuadros de ancho debe tener la hoja?", "24+2+2", "Se suma el ancho del diseño y los dos márgenes."),
        ("Una pieza mide 3 cuadros de ancho y la repites sin dejar espacios hasta cubrir 15 cuadros. ¿Cuántas piezas necesitas?", "5", "15 dividido por 3 es 5."),
    ],
    ctx=("Quieres dibujar con un programa la vista frontal de un estante de 20 cm de ancho y 12 cm de alto, con cada cuadro de la cuadrícula valiendo 1 cm. Escribe cuántos cuadros de ancho y de alto tendrá, y qué nombre de archivo usarías.", "20 cuadros de ancho y 12 de alto. Nombre: estante_vista_frontal", "Lee las medidas y propone un nombre que diga el contenido."),
    sc=[
        ("¿Para qué sirve agrupar formas?", "Para moverlas como una sola", "Así no se descolocan."),
        ("¿Cómo sabes la medida de una forma en cuadrícula?", "Contando los cuadros", "Cada cuadro vale 1 cm."),
        ("¿Qué debe decir el nombre del archivo?", "Lo que contiene", "Así se encuentra después."),
    ],
    open_task=(
        "Escoge un diseño. Diseño 1: un soporte con una base de 20 cm por 8 cm y dos paredes de 20 cm por 6 cm. Diseño 2: un porta-lápices de 8 cm por 10 cm con una división de 8 cm por 5 cm. Dibújalo con un programa o en papel cuadriculado con 1 cuadro por cm. Usa formas, cuenta las medidas y escribe el nombre de archivo.",
        "Diseño 2: un rectángulo de 8 por 10 cuadros y otro de 8 por 5 dentro. Nombre: porta_lapices_vista_frontal.",
        ["usa formas básicas", "las medidas coinciden con el diseño", "las formas están alineadas", "nombre de archivo que dice el contenido"],
        ["dibujo en pantalla o en papel con nombre de archivo"],
        ["estirar formas a ojo", "nombre de archivo que no dice el contenido"],
        "Pregunta: «¿cuántos cuadros mide esta forma?». Si no coincide con el diseño, pídele contar de nuevo.",
    ),
    reinforce="En papel cuadriculado dibuja un rectángulo de 9 por 4 cuadros y una copia al lado, alineados.",
    extend="Piensa cómo copiarías y alinearías 6 patas iguales de un mueble en un programa. Escribe los pasos.",
)

# ------------------------------------------------------------------ OA 01, clase 5
reg(
    OA1, 5,
    materials="Hoja y lápiz. Los resultados de las pruebas están escritos en este cuaderno. Si quieres probar en casa, usa cartón, cinta y fichas o tapas.",
    use="Aprenderé a probar un diseño con un registro de pruebas y a decidir si cumple los criterios con datos. Sirve para mejorar con evidencia y no por opinión.",
    prior=["Sé escribir criterios con números.", "Sé modificar una sola variable.", "Sé restar y sumar números hasta 1.000."],
    explain=[
        "Probar un diseño es usarlo en una situación real o parecida y registrar lo que ocurre. Antes de probar, repasa los criterios. Una prueba comprueba un criterio a la vez. Si el criterio es «sostiene 9 fichas», la prueba es poner las 9 fichas y mirar si el soporte se mantiene firme durante 1 minuto.",
        "Una sola prueba puede engañar, porque a veces sale bien por casualidad. Por eso se hacen tres pruebas con las mismas condiciones. El registro se anota en una tabla: número de prueba, qué se hizo, qué resultado se obtuvo y si cumple o no cumple. Un diseño cumple cuando resiste las tres.",
        "Si el diseño falla, se cambia una sola variable y se repite la prueba. Se anota qué cambió y qué resultado dio. Una mejora sirve cuando los datos son mejores que los del diseño anterior. Así la decisión se apoya en evidencia: números y observaciones, no solo en que a alguien le parezca bonito.",
    ],
    vocab=[("prueba", "uso del diseño en una situación para ver si cumple"), ("registro", "tabla donde se anotan los resultados"), ("evidencia", "datos y observaciones que apoyan una decisión"), ("cumple", "logra el criterio"), ("repetir", "volver a hacer la prueba con las mismas condiciones")],
    worked=[
        ("Leer un registro de pruebas", "Criterio: sostiene 9 fichas. Prueba 1: sostuvo 9. Prueba 2: se cayó con 7. Prueba 3: sostuvo 9. ¿Cumple el diseño?", ["Cumple en las pruebas 1 y 3 y falla en la 2.", "Un diseño cumple cuando resiste las tres pruebas."], "No cumple, porque falló en la prueba 2"),
        ("Mejorar con una variable", "El soporte falló con 7 fichas. Se pegó una base más ancha y se probó otra vez con 9 fichas sin caerse. ¿Qué variable cambió y qué evidencia muestra la mejora?", ["Cambió el ancho de la base.", "Antes se caía al poner 7 fichas y ahora aguanta 9 sin caerse."], "Cambió el ancho de la base y ahora aguanta 9 fichas, más de las 7 que lo hacían caer"),
    ],
    mistakes=[
        ("Hacer una sola prueba y decir «funciona».", "Puede haber salido bien por casualidad.", "Haz tres pruebas con las mismas condiciones."),
        ("Cambiar la base y la altura a la vez después de una falla.", "No se sabe cuál cambio ayudó.", "Cambia una sola variable y vuelve a probar."),
    ],
    R=[
        ("¿Cuántas pruebas conviene hacer con las mismas condiciones?", "Tres", "Así una sola prueba no engaña."),
        ("Un soporte debía sostener 9 fichas y sostuvo 9. ¿Cumple ese criterio?", "Sí", "Sostuvo la cantidad pedida."),
        ("¿Dónde se anotan los resultados de las pruebas?", "En una tabla de registro", "La tabla ordena los datos."),
    ],
    C=[
        ("¿Por qué no basta con una sola prueba?", "Porque puede salir bien por casualidad", "Tres pruebas muestran si el resultado se repite."),
        ("Una tabla registra prueba 1: sostuvo 8; prueba 2: sostuvo 8; prueba 3: sostuvo 8. El criterio es 8 fichas. ¿Cumple?", "Sí", "Resistió las tres pruebas."),
        ("¿Qué es la evidencia en una prueba?", "Los datos y observaciones que apoyan la decisión", "La decisión se basa en números y hechos."),
    ],
    A=[
        arith("Un soporte sostuvo 11 fichas en la primera prueba y 8 en la segunda. ¿Cuántas fichas menos sostuvo en la segunda?", "11-8", "Se resta lo de la segunda prueba de lo de la primera."),
        arith("Cada ficha pesa 5 gramos. Un soporte sostiene 9 fichas. ¿Cuántos gramos sostiene?", "9*5", "Se multiplica el número de fichas por el peso de cada una."),
        ("Registro: prueba 1 sostiene 10, prueba 2 sostiene 10, prueba 3 sostiene 6. Criterio: 10 fichas. ¿Cumple?", "No", "Falló en la prueba 3."),
    ],
    Z=[
        ("Tras una falla se agranda la base y se cambia el cartón por uno más grueso. El soporte mejora. ¿Qué error hay en el método?", "Se cambiaron dos variables a la vez", "No se sabe si ayudó la base o el cartón."),
        ("Marta dice: «Mi soporte es el mejor porque es el más bonito». Ana dice: «El mío sostuvo 9 fichas en tres pruebas». ¿Quién usa evidencia para su decisión?", "Ana", "Ana da datos de las pruebas; Marta da una opinión."),
    ],
    D=[
        arith("Un soporte sostuvo 8, 9 y 10 fichas en tres pruebas. ¿Cuántas fichas más sostuvo en su mejor prueba que en la peor?", "10-8", "Se resta el resultado menor del mayor."),
        ("Un diseño nuevo debe sostener al menos 9 fichas en las tres pruebas y tiene resultados de 9, 10 y 9. Otro tiene 10, 8 y 10. ¿Cuál cumple el criterio?", "El primero", "El segundo falla en la prueba con 8, que es menor que 9."),
    ],
    ctx=("Probaste tu porta-fichas de cartón. Resultados: prueba 1 sostiene 8 fichas, prueba 2 sostiene 5 fichas, prueba 3 sostiene 8 fichas. El criterio es sostener 8 fichas. Di si cumple, qué variable cambiarías y cuál sería tu nueva prueba.", "No cumple porque falló en la prueba 2. Cambiaría solo el ancho de la base y repetiría las tres pruebas", "Decide con datos y cambia una sola variable."),
    sc=[
        ("¿Cuántas variables se cambian entre una prueba y la siguiente?", "Una", "Así se sabe qué ayudó."),
        ("¿Qué datos lleva la tabla de registro?", "Número de prueba, qué se hizo, resultado y si cumple", "Así se compara con el criterio."),
        ("¿Un diseño cumple si resiste solo una prueba de tres?", "No", "Debe resistir las tres."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: un soporte de cartón sostuvo 9, 7 y 9 fichas, y el criterio es 9. Registro 2: otro soporte sostuvo 6, 6 y 6, y el criterio es 8. Escribe si cumple, qué variable cambiarías y la tabla de pruebas que harías después con el cambio.",
        "Registro 2: no cumple, porque sostiene 6 y se pide 8. Cambiaría el ancho de la base. Tabla: prueba 1, 2 y 3 con base más ancha.",
        ["dice si cumple con datos", "elige una sola variable", "propone una tabla con tres pruebas", "la mejora se juzga por los datos"],
        ["registro con decisión y nueva tabla de pruebas"],
        ["decidir sin mirar los datos", "cambiar dos variables"],
        "Pregunta: «¿qué dato muestra que mejoró?». Si no muestra un número, pídele que lo agregue.",
    ),
    reinforce="Con cartón y 5 tapas, prueba un soporte tres veces y anota si queda firme cada vez.",
    extend="Explica con tus palabras por qué una mejora debe apoyarse en datos y no solo en opinión.",
)

# ------------------------------------------------------------------ OA 01, clase 6
reg(
    OA1, 6,
    materials="Hoja, lápiz y los datos escritos en este cuaderno. Si tienes computador, un programa de presentaciones para la ficha final.",
    use="Aprenderé a mejorar un diseño con evidencia y a comunicarlo con una ficha de diseño. Sirve para que otras personas entiendan qué problema resolviste y por qué tu solución funciona.",
    prior=["Sé hacer vistas con medidas.", "Sé probar un diseño con tres pruebas.", "Sé que una mejora cambia una sola variable."],
    explain=[
        "Mejorar un diseño es cambiar algo para cumplir mejor un criterio. La decisión se apoya en la evidencia de las pruebas. Mira qué criterio falló, elige una sola variable que podría explicarlo, cámbiala y repite las pruebas. Si los datos mejoran, la mejora se queda. Si no, vuelves al diseño anterior y pruebas otra variable.",
        "Después, el diseño se comunica. Una ficha de diseño tiene seis partes: la necesidad con su usuario, los criterios, el dibujo con medidas, el registro de pruebas, la mejora hecha y lo que aprendiste. Debe estar ordenada, con letra o texto legible, y mostrar números y no solo opiniones.",
        "Una buena presentación escucha a las demás personas. Anota qué preguntas hicieron y qué ideas de mejora sugirieron. Si usas ideas de otra persona, di quién las dio. Si usas una imagen o un dato que no es tuyo, anota la fuente. Un diseño nunca está terminado; siempre se puede probar otra mejora.",
    ],
    vocab=[("mejora", "cambio que hace que el diseño cumpla mejor un criterio"), ("ficha de diseño", "hoja que resume el problema, el diseño, las pruebas y la mejora"), ("evidencia", "datos que apoyan la decisión"), ("fuente", "origen de una imagen, dato o idea"), ("comunicar", "mostrar tu trabajo para que otras personas lo entiendan")],
    worked=[
        ("Decidir una mejora con datos", "El soporte debía sostener 11 fichas y sostuvo 11, 7 y 11. Falló en la prueba 2, cuando se movió la mesa. ¿Qué mejora pruebas primero?", ["La falla ocurrió cuando la mesa se movió: parece un problema de estabilidad.", "Cambio una sola variable: pego una base más ancha y repito las tres pruebas."], "Agrandar la base y repetir las tres pruebas"),
        ("Ordenar la ficha", "Ordena las partes de la ficha: mejora hecha, necesidad y usuario, registro de pruebas, criterios, lo aprendido y dibujo con medidas.", ["Primero el problema: necesidad y usuario, luego los criterios.", "Después el dibujo, el registro de pruebas, la mejora y lo aprendido."], "Necesidad y usuario, criterios, dibujo con medidas, registro de pruebas, mejora hecha y lo aprendido"),
    ],
    mistakes=[
        ("Decir «quedó mejor» sin mostrar datos.", "No hay forma de comprobarlo.", "Muestra el número antes y el número después."),
        ("Usar la imagen de otra persona sin decir de dónde viene.", "No se reconoce el trabajo ajeno.", "Anota la fuente de toda imagen o dato que no sea tuyo."),
    ],
    R=[
        ("¿Cuántas partes tiene la ficha de diseño de esta clase?", "Seis", "Son necesidad, criterios, dibujo, pruebas, mejora y lo aprendido."),
        ("Si los datos no mejoran con el cambio, ¿qué se hace?", "Volver al diseño anterior y probar otra variable", "Una mejora debe mostrar datos mejores."),
        ("Si usas una imagen que no es tuya, ¿qué anotas?", "La fuente", "Así se reconoce de dónde viene."),
    ],
    C=[
        ("¿Por qué una ficha de diseño debe mostrar números y no solo opiniones?", "Porque los números permiten comprobar la mejora", "Una opinión no se puede verificar."),
        ("Un diseño sostenía 6 fichas y tras el cambio sostiene 10. ¿La mejora está apoyada en evidencia?", "Sí", "Hay datos de antes y de después."),
        ("Después de presentar tu diseño, una compañera sugiere agrandar la base. ¿Qué haces con su idea?", "La anoto como idea de mejora y digo quién la dio", "Se registra y se reconoce a la persona."),
    ],
    A=[
        arith("Antes de la mejora el soporte sostenía 6 fichas; después sostiene 10. ¿Cuántas fichas más sostiene?", "10-6", "Se resta lo de antes de lo de después."),
        ("Elige el mejor registro de mejora. A «Quedó más lindo», B «Con base de 20 cm sostuvo 10 fichas en tres pruebas».", "B", "B tiene datos que se pueden comprobar."),
        ("Una ficha tiene necesidad, criterios, dibujo, registro y mejora. ¿Qué parte le falta?", "Lo que aprendiste", "Son seis partes y falta la última."),
    ],
    Z=[
        ("Dos grupos mejoraron el soporte. Grupo 1: «lo hicimos más grande». Grupo 2: «subimos de 6 a 10 fichas al ensanchar la base 4 cm». ¿Qué grupo comunica mejor la mejora y por qué?", "El grupo 2, porque muestra datos", "Da el cambio y el resultado con números."),
        ("Una mejora aumentó las fichas pero rompió el límite de base de 20 cm. ¿Se acepta?", "No", "Pasa una restricción del problema."),
    ],
    D=[
        arith("Un grupo midió 4 fichas más en cada mejora. Parte de 6 y hace 2 mejoras seguidas. ¿Cuántas fichas sostiene al final?", "6+4+4", "Se suman las dos mejoras a lo que sostenía."),
        ("Una ficha usa la fotografía de un puente de un sitio de internet, pero no indica de dónde es. ¿Qué falta?", "La fuente de la imagen", "Toda imagen ajena debe indicar su origen."),
    ],
    ctx=("Tu soporte de cartón para 9 fichas sostuvo 9, 6 y 9 en tres pruebas. Cambiaste solo el ancho de la base de 12 cm a 16 cm y ahora sostiene 9, 9 y 9. Escribe la mejora hecha, el dato de antes y de después y una frase final de lo que aprendiste.", "Mejora: base de 12 a 16 cm. Antes: falló en la prueba 2. Después: 9, 9 y 9. Aprendí que una base más ancha da más estabilidad", "Une cambio, datos y aprendizaje."),
    sc=[
        ("¿Qué muestra que una mejora funcionó?", "Datos mejores que los de antes", "La evidencia permite comprobarlo."),
        ("¿Qué haces con las ideas de otras personas?", "Las anoto y digo quién las dio", "Se reconoce el aporte."),
        ("¿Un diseño puede mejorar más después de terminarlo?", "Sí", "Siempre se puede probar otra mejora."),
    ],
    open_task=(
        "Escoge un diseño. Diseño 1: soporte de cartón para 9 fichas que sostuvo 9, 6 y 9. Diseño 2: portalápices de cartón que se vuelca con 6 lápices en 2 de 3 pruebas. Escribe la mejora que probarías, qué variable cambias, qué dato mostraría que mejoró y arma la ficha con las seis partes.",
        "Diseño 2: mejora: base más ancha. Variable: ancho de la base. Dato: no se vuelca en 3 de 3 pruebas. Ficha con las seis partes.",
        ["dice la mejora y la variable", "indica el dato que mostraría la mejora", "ficha con las seis partes", "indica la fuente de cualquier imagen o idea ajena"],
        ["ficha de diseño completa"],
        ["mejorar sin datos", "dejar partes de la ficha en blanco"],
        "Pregunta: «¿qué número muestra que mejoró?». Si no tiene, pídele volver a las pruebas.",
    ),
    reinforce="Cuéntale a una persona de tu casa qué problema resolvió tu diseño y qué mejora hiciste, mostrando un número.",
    extend="Escribe dos preguntas que te harías al ver el diseño de otra persona para entender cómo lo mejoró.",
)

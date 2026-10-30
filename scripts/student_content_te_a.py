"""Student material for 1.º básico Tecnología, OA 01 (representar diseños) y OA 02 (tareas, materiales y herramientas)."""
from __future__ import annotations

from student_lessons import ex, register

OA1, OA2 = "TE01 OA 01", "TE01 OA 02"


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


# ------------------------------------------------------------------ OA 01
reg(
    OA1, 1,
    materials="Una hoja de papel, un lápiz y los casos escritos en este cuaderno. No necesitas nada más.",
    use="Aprenderé a decir para quién y para qué sirve un objeto antes de dibujarlo. Sirve para que mis diseños ayuden de verdad a alguien.",
    prior=["Sé dibujar con lápiz.", "Sé que los objetos se hacen para algo."],
    explain=[
        "Un objeto tecnológico se hace para ayudar a una persona con algo que necesita. A esa persona la llamamos usuario. Antes de dibujar, hazte dos preguntas: ¿para quién es? y ¿para qué sirve?",
        "Por ejemplo, Lía se pierde en la línea cuando lee. Su necesidad es no perder el lugar. Un marcador de página le sirve. Un adorno bonito sin uso no resuelve su necesidad, aunque se vea lindo.",
        "Después escribe dos criterios, que son cosas que el objeto debe cumplir. Para el marcador: se ve al cerrar el libro y no rompe las hojas. Con criterios podrás saber si tu diseño funciona.",
    ],
    vocab=[("necesidad", "algo que una persona necesita resolver"), ("usuario", "la persona que usará el objeto"), ("criterio", "algo que el objeto debe cumplir"), ("diseño", "la idea de un objeto antes de hacerlo"), ("para qué", "el uso o la función del objeto")],
    worked=[
        ("Nombrar usuario y necesidad", "Teo siempre olvida dónde dejó la lectura. Quiere un objeto para marcar su libro. ¿Quién es el usuario y cuál es la necesidad?", ["El objeto lo usará Teo: es el usuario.", "Teo olvida el lugar donde quedó.", "La necesidad es marcar el lugar de su libro."], "Usuario: Teo. Necesidad: marcar dónde quedó en el libro"),
        ("Escribir dos criterios", "Para el marcador de Teo, escribe dos criterios.", ["Pienso en lo que Teo necesita.", "Debe verse al cerrar el libro.", "No debe romper las hojas."], "Se ve al cerrar el libro y no rompe las hojas"),
    ],
    mistakes=[
        ("Dibujar un objeto bonito sin pensar en quién lo usa.", "Se olvida la necesidad.", "Primero escribe para quién y para qué; luego dibuja."),
        ("Escribir un criterio como «que sea lindo».", "Lindo no se puede comprobar.", "Escribe algo que se pueda mirar o medir, como «mide 15 cm de largo»."),
    ],
    R=[
        ("Ana pierde su lugar al leer. ¿Qué le ayuda: un marcador de página, una pelota o un paraguas?", "Un marcador de página", "El marcador señala el lugar de lectura."),
        ("Un cepillo de dientes sirve para limpiar los dientes. ¿Quién lo usa: una persona o una piedra?", "Una persona", "Solo una persona usa el cepillo."),
        ("Completa con una de las dos palabras: un objeto se hace para resolver una ___ de alguien. Opciones: necesidad, sombra.", "necesidad", "Los objetos tecnológicos responden a necesidades."),
    ],
    C=[
        ("¿Qué significa la palabra «usuario»?", "La persona que usa el objeto", "Usuario es quien utiliza lo diseñado."),
        ("¿Qué pregunta ayuda a empezar un diseño: «¿para quién es?» o «¿de qué color es mi lápiz?»", "¿Para quién es?", "Conocer al usuario guía el diseño."),
        ("En Tecnología, ¿qué es un criterio?", "Algo que el objeto debe cumplir", "Con un criterio se revisa si el diseño sirve."),
    ],
    A=[
        ("Pía tiene la mano pequeña y no alcanza el interruptor de la luz. ¿Qué dos datos de su caso anotas primero: usuario y necesidad, o color y tamaño de la pared?", "Usuario y necesidad", "Primero se anota quién es y qué necesita."),
        ("Marcos necesita un objeto para guardar 5 lápices sobre su mesa. ¿Qué criterio se puede comprobar: «es lindo» o «caben 5 lápices»?", "Caben 5 lápices", "Se puede contar y comprobar."),
        ("Un abuelito ve poco y quiere un cartel para su puerta. ¿Qué criterio le sirve más: letras grandes o muchos dibujos pequeños?", "Letras grandes", "Las letras grandes responden a su necesidad de ver."),
    ],
    Z=[
        ("Rita dice: «Mi diseño es una estrella dorada de adorno, no sirve para nada, pero es linda». ¿Es un buen diseño tecnológico? Responde sí o no.", "No", "No resuelve la necesidad de nadie."),
        ("Dos niños quieren un objeto para sujetar un dibujo en la pared. Uno dice que el usuario es la pared y otro que es el niño que cuelga el dibujo. ¿Quién tiene razón?", "El que dice que es el niño", "El usuario es la persona, no la pared."),
    ],
    D=[
        ("Eli necesita que el plato de agua de su gato no se vuelque. Escribe en una frase el usuario, la necesidad y un criterio comprobable.", "Usuario Eli (o su gato); necesidad: que el agua no se vuelque; criterio: el plato no se mueve al empujarlo suave", "Lleva los tres datos pedidos."),
        ("Un diseño tiene usuario, necesidad y dos criterios, pero ningún dibujo. ¿Ya se puede construir tal como está? Responde sí o no.", "No", "Falta representarlo con un dibujo o modelo."),
    ],
    ctx=("Tato tiene 6 años y su colación se aplasta en la mochila. Escribe quién es el usuario, qué necesita y un criterio comprobable.", "Usuario: Tato. Necesidad: que la colación no se aplaste. Criterio: soporta un cuaderno encima sin deformarse", "Responde a la necesidad con algo comprobable."),
    sc=[
        ("A una prima no le alcanza el brazo para colgar su abrigo. ¿Quién es el usuario?", "La prima", "Ella usará el objeto."),
        ("¿Los criterios se escriben antes o después de dibujar?", "Antes", "Los criterios guían el dibujo."),
        ("¿Un objeto sin ningún usuario puede ser un buen diseño tecnológico? Responde sí o no.", "No", "Debe servir a alguien."),
    ],
    open_task=(
        "Escoge uno de estos casos. Caso 1: Nico siempre pierde su lápiz sobre la mesa. Caso 2: Sol no puede abrir sola la caja de sus colores. Escribe quién es el usuario, qué necesita y dos criterios. Haz un dibujo sencillo de una idea.",
        "Caso 1: Usuario Nico. Necesita no perder su lápiz. Criterios: se ve sobre la mesa; el lápiz queda sujeto sin caerse. Dibujé un vasito de cartón pegado a la mesa.",
        ["dice el usuario", "dice la necesidad", "escribe 2 criterios que se pueden comprobar", "dibuja una idea que responde al caso"],
        ["hoja con usuario y necesidad", "dos criterios escritos", "dibujo a mano alzada"],
        ["dibuja un objeto decorativo sin uso", "criterios que no se pueden comprobar"],
        "Pregunta: «¿cómo ayuda a Nico?». Si el criterio es vago, pide uno que se pueda mirar o medir.",
    ),
    reinforce="Mira un objeto de tu casa y di para quién es y qué necesidad resuelve.",
    extend="Imagina un objeto para alguien de tu familia y escribe su necesidad y dos criterios.",
)

reg(
    OA1, 2,
    materials="Hojas de papel, lápiz y los criterios escritos en este cuaderno. No se necesita ningún material especial.",
    use="Aprenderé a dibujar varias ideas distintas para un mismo problema antes de elegir una. Sirve para encontrar la mejor solución y no quedarme con la primera.",
    prior=["Sé decir quién es el usuario y su necesidad.", "Sé que un criterio se puede revisar."],
    explain=[
        "Para un mismo problema hay muchas soluciones. Antes de elegir, conviene dibujar al menos tres ideas diferentes. Así comparas y no te quedas solo con la primera que se te ocurrió.",
        "Piensa en el marcador de página. Una idea es una tira larga de cartón. Otra es una esquina doblada que se pone sobre la hoja. Otra es un cordón con un nudo. Son ideas distintas porque su forma y su modo de usarse cambian.",
        "Para elegir, revisa cada idea con los criterios y pregúntate: ¿cumple o no cumple? Cuenta cuántos criterios cumple cada idea y escoge la que cumple más. Dibujar varias ideas no es perder tiempo: ayuda a decidir mejor.",
    ],
    vocab=[("idea", "una posible solución dibujada"), ("alternativa", "otra solución distinta para el mismo problema"), ("comparar", "mirar en qué se parecen y en qué se diferencian"), ("elegir", "quedarme con la mejor según los criterios"), ("cumplir", "responder a lo que pide un criterio")],
    worked=[
        ("Contar criterios cumplidos", "Criterios: 1) se ve al cerrar el libro, 2) no rompe las hojas. Idea A: tira de cartón que sobresale, no rompe. Idea B: grapa de metal que se ve pero rompe la hoja. ¿Cuántos criterios cumple cada idea?", ["A: sobresale, cumple el 1; no rompe, cumple el 2.", "B: se ve, cumple el 1; rompe, no cumple el 2.", "A cumple 2 y B cumple 1."], "A cumple 2 criterios y B cumple 1"),
        ("Elegir la mejor idea", "Con los resultados del ejemplo anterior, ¿qué idea eliges?", ["La idea A cumple más criterios.", "Elijo la A y explico por qué."], "La idea A, porque cumple 2 criterios"),
    ],
    mistakes=[
        ("Dibujar tres veces la misma idea con pequeños cambios.", "No son ideas distintas.", "Cambia la forma o el modo de uso en cada dibujo."),
        ("Elegir la que más me gusta sin revisar los criterios.", "No se sabe si sirve.", "Cuenta qué criterios cumple cada idea."),
    ],
    R=[
        ("Para sostener una hoja en la pared, Ema dibujó una cinta, un clip grande y un imán de cocina. ¿Cuántas ideas distintas dibujó?", "3", "Son tres soluciones diferentes."),
        ("La idea 1 cumple 3 criterios y la idea 2 cumple 1. ¿Cuál se elige?", "La idea 1", "Cumple más criterios."),
        ("Dos dibujos son iguales, solo uno es más grande. ¿Son ideas distintas? Responde sí o no.", "No", "Cambia el tamaño pero no la solución."),
    ],
    C=[
        ("¿Por qué conviene dibujar varias ideas antes de elegir?", "Para comparar y escoger la mejor", "Con varias se puede decidir mejor."),
        ("¿Qué se hace con los criterios al comparar ideas?", "Se revisa si cada idea los cumple", "Los criterios son la regla para comparar."),
        ("Escribe la palabra que significa «otra solución posible».", "Alternativa", "Alternativa es una opción distinta."),
    ],
    A=[
        ("Criterios: liviano (1), cabe en una mochila (2), se cierra (3). La idea X cumple el 1 y el 2. La idea Y cumple el 1, el 2 y el 3. ¿Cuál cumple más y cuántos?", "Y; 3 criterios", "Y cumple los tres y X solo dos."),
        ("Quieres llevar 4 gomitas en la mochila. Ideas: caja pequeña con tapa, bolsa de papel bien cerrada o taza abierta sin tapa. ¿Cuál no sirve porque las gomitas se pueden caer?", "La taza abierta", "No tiene tapa y las gomitas se caen."),
        ("La idea M cumple 2 criterios. La idea N cumple 3. Si solo importa cumplir criterios, ¿cuál eliges?", "N", "Cumple un criterio más."),
    ],
    Z=[
        ("Ema escogió la idea que más le gusta, aunque cumple 1 criterio de 3. Otra idea cumple 3 de 3. ¿Qué le dirías?", "Que elija la que cumple 3", "La elección debe apoyarse en criterios."),
        ("Teo dibujó una sola idea, le pareció buena y no hizo más dibujos. ¿Qué perdió?", "La posibilidad de comparar con otras ideas", "Con una sola idea no hay comparación."),
    ],
    D=[
        ("Para un cartel que se lea desde 3 pasos de distancia, ¿qué idea cumple mejor: letras grandes o dibujos muy chicos?", "Letras grandes", "Se ven mejor desde lejos."),
        ("Cuenta cuántas ideas distintas hay: lápiz con goma, lápiz con tapita, goma suelta, lápiz con goma de otro color.", "3", "El lápiz con goma y el de otro color son la misma solución."),
    ],
    ctx=("Nico quiere no perder su lápiz. Dibujó un vaso pegado a la mesa (se ve, pero se despega), un bolsillo de papel (se ve y no se despega) y un lazo (no se ve). Criterios: se ve y no se despega. ¿Qué idea cumple los dos?", "El bolsillo de papel", "Es la única que se ve y no se despega."),
    sc=[
        ("¿Cuántas ideas conviene dibujar antes de elegir, al menos?", "Tres", "Con tres ya se puede comparar."),
        ("Una idea cumple los 2 criterios y otra cumple 1. ¿Cuál eliges?", "La que cumple 2", "Cumple más criterios."),
        ("¿Dibujar solo una idea es suficiente para elegir bien? Responde sí o no.", "No", "Falta comparar otras ideas."),
    ],
    open_task=(
        "Para un portalápices dibuja tres ideas distintas: un vaso de cartón, una caja plana con agujeros y un cordón colgado. Criterios: se ve y no se cae. Datos de la prueba: el vaso se ve y no se cae; la caja se ve, pero se cae si la empujas; el cordón no se ve y se cae. Anota cuántos criterios cumple cada idea y elige una.",
        "Dibujé el vaso, la caja y el cordón. El vaso cumple 2 criterios. La caja cumple 1. El cordón cumple 0. Elegí el vaso porque cumple los dos criterios.",
        ["dibuja 3 ideas distintas", "revisa cada una con los criterios", "elige con razón"],
        ["tres dibujos", "tabla con los criterios", "idea elegida"],
        ["tres ideas iguales", "elegir sin revisar"],
        "Pregunta en qué se diferencia cada dibujo y pide contar criterios cumplidos.",
    ),
    reinforce="Mira dos sillas de tu casa y di una diferencia de forma entre ellas.",
    extend="Inventa un criterio nuevo y revisa tus tres ideas con él.",
)

reg(
    OA1, 3,
    materials="Hoja de papel, lápiz y los dibujos descritos en este cuaderno. Un adulto puede ayudar a leer los rótulos.",
    use="Aprenderé a hacer un dibujo a mano alzada que otra persona entienda. Sirve para explicar mi idea con partes, nombres y medidas.",
    prior=["Sé dibujar formas simples.", "Sé escribir palabras cortas."],
    explain=[
        "Un dibujo que comunica permite que otra persona entienda tu idea sin que tú se la expliques. Dibujar a mano alzada quiere decir dibujar sin regla, solo con la mano. No tiene que quedar perfecto, pero sí claro.",
        "Un buen dibujo tiene tres cosas. Primero, se ven las partes del objeto, cada una con un rótulo, que es un nombre escrito. Segundo, tiene medidas, por ejemplo 15 cm de largo. Tercero, tiene una flecha que muestra cómo se usa.",
        "Si falta algo, la otra persona se confunde. Por ejemplo, un marcador de página dibujado sin medidas no dice si cabe en el libro. Mira siempre tu dibujo y pregunta: ¿lo entendería alguien que no sabe nada de mi idea?",
    ],
    vocab=[("a mano alzada", "dibujar sin regla"), ("rótulo", "palabra escrita que nombra una parte"), ("medida", "dato de tamaño, como 15 cm"), ("flecha", "línea con punta que muestra un movimiento o uso"), ("parte", "pedazo que forma el objeto")],
    worked=[
        ("Rotular un dibujo", "Un marcador de página tiene una tira larga y una lengüeta que se pone sobre la hoja. ¿Qué rótulos escribes?", ["Miro las partes del objeto.", "A la tira larga le pongo «tira».", "A la parte que se dobla le pongo «lengüeta»."], "Rótulos: tira y lengüeta"),
        ("Agregar medidas", "El libro de Teo mide 20 cm de alto. El marcador debe sobresalir 3 cm. Si la tira mide 20 + 3 = 23 cm, ¿qué medida escribes en el dibujo?", ["Sumo el alto del libro y lo que sobresale.", "20 + 3 es 23.", "Escribo 23 cm junto a la tira."], "23 cm"),
    ],
    mistakes=[
        ("Dibujar solo el contorno sin escribir nombres de partes.", "Nadie sabe qué es cada parte.", "Escribe un rótulo en cada parte importante."),
        ("Poner una medida sin unidad, como «20».", "No se sabe si son cm, pasos o dedos.", "Escribe siempre la unidad: 20 cm."),
    ],
    R=[
        ("Dibujaste un vaso de cartón. A la parte plana de abajo, donde se apoya, le pones el rótulo «base» o «nube»?", "Base", "Base es la parte donde se apoya el vaso."),
        ("¿Qué muestra una flecha en un dibujo de diseño: cómo se usa o de qué color es?", "Cómo se usa", "La flecha indica uso o movimiento."),
        ("¿Dibujar a mano alzada significa usar regla o no usarla?", "No usarla", "Se dibuja solo con la mano."),
    ],
    C=[
        ("¿Para qué sirve ponerle rótulos a las partes?", "Para que otros sepan qué es cada parte", "El nombre escrito aclara el dibujo."),
        ("Un dibujo dice «20» junto a una tira. ¿Qué le falta a esa medida?", "La unidad, como cm", "Sin unidad no se entiende."),
        ("Nombra las tres cosas de un dibujo que comunica.", "Partes con rótulos, medidas y flecha de uso", "Son los tres elementos que se explicaron."),
    ],
    A=[
        ("Dibujas una caja para 8 fichas. Mide 12 cm de largo y 6 cm de ancho. ¿Qué dos medidas escribes en el dibujo?", "12 cm de largo y 6 cm de ancho", "Se escriben ambas con unidad."),
        ("Un portalápices tiene las partes: base, pared y borde. ¿Cuántos rótulos necesitas?", "3", "Hay una palabra por cada parte."),
        ("Una tira de cartón mide 18 cm y otra mide 7 cm. ¿Cuántos cm más larga es la primera?", "11", "18 − 7 = 11."),
    ],
    Z=[
        ("Ana dibujó un cartel sin ninguna medida. Tato dice que no se sabe si cabe en la puerta. ¿Tiene razón? Responde sí o no.", "Sí", "Sin medidas no se puede comprobar el tamaño."),
        ("Dos dibujos de un marcador: uno tiene rótulos y otro no. ¿Cuál lo entiende mejor otra persona?", "El que tiene rótulos", "Los nombres evitan confusiones."),
    ],
    D=[
        ("Tu marcador mide 15 cm de largo y 3 cm de ancho. Escribe cómo pondrías las medidas, con unidades, junto al dibujo.", "15 cm de largo y 3 cm de ancho", "Cada medida lleva su unidad."),
        ("Un dibujo muestra una lengüeta con una flecha curva que baja hacia la página. ¿Qué uso se entiende: que la lengüeta se dobla sobre la página o que se corta?", "Se dobla sobre la página", "La flecha curva indica el movimiento de doblar."),
    ],
    ctx=("Lía dibujó un marcador con una tira, una lengüeta y una flecha que baja hacia la página. Escribió 18 cm junto a la tira, pero no puso nombres a las partes ni la medida de la lengüeta. ¿Qué dos cosas debe agregar: rótulos y la medida de la lengüeta, o el color del lápiz?", "Rótulos y la medida de la lengüeta", "Se necesitan nombres y medidas completas."),
    sc=[
        ("¿Qué escribimos junto a una medida para que se entienda?", "La unidad", "Dice si son cm, pasos o dedos."),
        ("¿Un dibujo a mano alzada tiene que ser perfecto? Responde sí o no.", "No", "Solo tiene que ser claro."),
        ("Nombra una cosa que muestra la flecha de un dibujo.", "El uso o el movimiento", "La flecha indica cómo funciona."),
    ],
    open_task=(
        "Dibuja un marcador de página con esta descripción: una tira de 18 cm de largo y 3 cm de ancho, con una lengüeta de 4 cm que se dobla sobre la página. Escribe un rótulo en cada parte, las medidas con unidad y una flecha que muestre cómo se usa.",
        "Dibujé una tira larga con «tira 18 cm × 3 cm», una lengüeta con «lengüeta 4 cm» y una flecha curva hacia la página que dice «se dobla».",
        ["dibuja a mano alzada", "pone rótulos en las partes", "escribe medidas con unidad", "usa una flecha de uso"],
        ["dibujo con rótulos", "medidas escritas", "flecha"],
        ["medidas sin unidad", "partes sin nombre"],
        "Pide que otra persona describa lo que entiende del dibujo y anota qué falta.",
    ),
    reinforce="Dibuja tu mochila con tres rótulos y una flecha que muestre cómo se abre.",
    extend="Agrega al dibujo del marcador una vista desde arriba y otra de lado.",
)

reg(
    OA1, 4,
    materials="Papel, tijeras de punta roma (con ayuda de un adulto), cinta adhesiva y regla. Si no tienes cartón, usa una hoja doblada. Las medidas están escritas en cada ejercicio.",
    use="Aprenderé a hacer un modelo con papel o cartón que muestre mi idea en tamaño real. Sirve para probar si mi diseño sirve antes de hacerlo bien.",
    prior=["Sé dibujar una idea con partes y medidas.", "Sé plegar y pegar papel."],
    explain=[
        "Un modelo concreto es una versión de tu idea que puedes tocar. Se hace con materiales fáciles, como papel o cartón reutilizado. Un dibujo se mira, pero un modelo se prueba con las manos.",
        "El modelo muestra cosas que el dibujo no muestra. Por ejemplo, si un marcador de 3 cm de ancho se ve bien sobre la página o si se cae al cerrar el libro. Si algo no funciona, se cambia el modelo y no se gasta el material bueno.",
        "Para hacer un modelo, sigue el dibujo: usa las mismas medidas y las mismas partes. Usa la tijera con cuidado, siempre con ayuda de un adulto. Al final, compara el modelo con el dibujo y anota las diferencias.",
    ],
    vocab=[("modelo", "versión de mi idea que puedo tocar y probar"), ("tamaño real", "con el mismo tamaño que tendría el objeto final"), ("material reutilizado", "material que ya se usó y se vuelve a usar"), ("probar", "usar el modelo para ver si funciona"), ("diferencia", "algo que cambia entre dos cosas")],
    worked=[
        ("Elegir material para el modelo", "Quieres un modelo de marcador de 18 cm de largo. Tienes una hoja de cuaderno y una caja de cereal. ¿Cuál usas para probar si el marcador queda firme?", ["El marcador debe quedar firme.", "La hoja de cuaderno se dobla mucho.", "La caja de cereal es más firme."], "La caja de cereal, porque es más firme"),
        ("Comparar modelo y dibujo", "El dibujo dice 18 cm de largo. Al medir tu modelo tiene 16 cm. ¿Cuántos cm le faltan?", ["Resto 18 − 16.", "Da 2.", "Debo hacer el modelo 2 cm más largo."], "Faltan 2 cm"),
    ],
    mistakes=[
        ("Hacer el modelo muy distinto al dibujo.", "Ya no se prueba la misma idea.", "Usa las mismas partes y medidas que dibujaste."),
        ("Usar material sin pensar si es seguro.", "Puede tener bordes cortantes o pegamento fuerte.", "Usa papel o cartón limpio y tijera de punta roma con ayuda."),
    ],
    R=[
        ("¿Un modelo se puede tocar y probar, o solo se mira como el dibujo?", "Se puede tocar y probar", "Es una versión concreta."),
        ("Para un modelo, ¿conviene usar papel o cartón limpio, o vidrio roto?", "Papel o cartón limpio", "El vidrio roto es peligroso."),
        ("Tu dibujo dice 10 cm. ¿Qué mides en tu modelo para comparar: el largo o el color?", "El largo", "Se compara con la medida del dibujo."),
    ],
    C=[
        ("¿Qué puede mostrar un modelo que un dibujo no muestra?", "Si funciona al probarlo", "Se usa con las manos."),
        ("¿Por qué se hace un modelo antes del objeto final?", "Para probar y corregir sin gastar el material bueno", "Los errores salen baratos."),
        ("¿Quién debe ayudar con las tijeras si eres pequeño?", "Un adulto", "Es una regla de seguridad."),
    ],
    A=[
        ("Tu dibujo dice 20 cm de largo. Tu modelo mide 17 cm. ¿Cuántos cm le faltan?", "3", "20 − 17 = 3."),
        ("Necesitas 3 tiras de papel de 6 cm cada una para un modelo. ¿Cuántos cm de papel necesitas en total?", "18", "6 + 6 + 6 = 18."),
        ("Un modelo de caja necesita 4 paredes. Ya hiciste 3. ¿Cuántas faltan?", "1", "4 − 3 = 1."),
    ],
    Z=[
        ("Tomás hizo su modelo con un papel muy delgado y se arrugó al probarlo. ¿Qué cambio de material propones: uno más firme o uno más delgado?", "Uno más firme", "Más firme aguanta mejor."),
        ("Rita probó su modelo y se cayó al cerrar el libro. ¿Debe cambiar el modelo o el libro? Responde cuál.", "El modelo", "Lo que se diseña es el modelo."),
    ],
    D=[
        ("Un modelo tiene 3 partes y cada parte tarda 5 minutos en armarse. ¿Cuántos minutos tarda armar todas?", "15", "5 + 5 + 5 = 15."),
        ("Tu modelo mide 15 cm y tu dibujo dice 15 cm. La cinta cubrió 1 cm de cada extremo. ¿Cuántos cm se ven sin cubrir?", "13", "15 − 1 − 1 = 13."),
    ],
    ctx=("Lía hizo un modelo de portalápices con un rollo de cartón de 10 cm de alto, pero sus lápices miden 18 cm. ¿Cuántos cm sobresalen los lápices si los pone de pie?", "8", "18 − 10 = 8 cm sobresalen."),
    sc=[
        ("En Tecnología, ¿qué es un modelo?", "Una versión de la idea que se puede tocar y probar", "Es una versión concreta."),
        ("¿El modelo debe tener las mismas medidas que el dibujo? Responde sí o no.", "Sí", "Así se prueba la misma idea."),
        ("Nombra un material seguro para un modelo.", "Papel o cartón limpio", "Es fácil de cortar y no hiere."),
    ],
    open_task=(
        "Haz un modelo en tamaño real de un marcador de página con una tira de papel o cartón de 15 cm de largo y 3 cm de ancho, con una lengüeta de 4 cm. Si cortas, usa tijera de punta roma con ayuda de un adulto. Pruébalo en un cuaderno. Anota una cosa que funciona y una que cambiarías.",
        "Mi modelo mide 15 cm × 3 cm. Funciona porque se ve al cerrar el cuaderno. Cambiaría la lengüeta porque se despega, la haría de 5 cm.",
        ["usa las medidas del dibujo", "usa material seguro", "prueba el modelo", "anota qué funciona y qué cambiar"],
        ["modelo terminado", "nota con lo que funciona", "nota con el cambio"],
        ["modelo distinto al dibujo", "usar tijeras sin ayuda"],
        "Pide que muestre cómo probó y qué vio. Si no hay cambio, pregunta qué mejoraría.",
    ),
    reinforce="Haz un modelo de papel de una mesa pequeña para una muñeca.",
    extend="Haz dos modelos con materiales distintos y compáralos.",
)

reg(
    OA1, 5,
    materials="Los dibujos y datos descritos en este cuaderno, hoja y lápiz. No necesitas ningún material más.",
    use="Aprenderé a explicar por qué elegí una idea usando criterios y pruebas. Sirve para convencer con razones y no solo con gustos.",
    prior=["Sé hacer dibujos con rótulos y medidas.", "Sé comparar ideas con criterios."],
    explain=[
        "Explicar una elección es decir qué idea escogiste y por qué. Una buena explicación usa la palabra porque y da una razón que se puede comprobar. Por ejemplo: «Elegí la idea B porque cumple los dos criterios».",
        "Una razón que se puede comprobar viene de una prueba o de una medida. «Es más linda» es un gusto. «Soporta 5 fichas sin caerse» es un dato que cualquiera puede revisar. Los gustos están bien, pero no bastan para decidir.",
        "También puedes decir qué mejorarías. Por ejemplo: «El modelo se mueve, la próxima vez lo haría con una base más ancha». Explicar con respeto significa hablar de las ideas y no burlarte de quien las dibujó.",
    ],
    vocab=[("explicar", "decir qué hice y por qué"), ("porque", "palabra que une la decisión con la razón"), ("razón", "dato o prueba que apoya lo que digo"), ("prueba", "intento para ver si algo funciona"), ("mejora", "cambio para que quede mejor")],
    worked=[
        ("Explicar con razón", "Idea A soportó 5 fichas. Idea B soportó 2 fichas. Quieres sostener 5 fichas. ¿Cómo explicas tu elección?", ["Escribo la idea que elijo: A.", "Uso porque y un dato: soportó 5 fichas.", "Compruebo que 5 fichas es lo que necesito."], "Elegí A porque soportó 5 fichas, que es lo que necesito"),
        ("Distinguir gusto de razón", "Teo dice «elegí B porque es roja». ¿Es una razón comprobable?", ["El color no dice si funciona.", "No hay una prueba.", "Necesita un dato como cuántas fichas soporta."], "No, es un gusto y falta un dato de prueba"),
    ],
    mistakes=[
        ("Decir «lo elegí porque sí».", "No hay razón.", "Escribe una frase con porque y un dato de la prueba."),
        ("Burlarse de la idea de otra persona.", "No ayuda a mejorar ni respeta a la persona.", "Di qué cumple y qué mejorarías, sin ofender."),
    ],
    R=[
        ("¿Qué palabra usas para unir tu decisión con la razón: porque o cuando?", "Porque", "Porque une decisión y razón."),
        ("«Soporta 5 fichas» ¿es un dato comprobable o un gusto?", "Un dato comprobable", "Se puede probar."),
        ("«Es más linda» ¿es un dato comprobable o un gusto?", "Un gusto", "No se puede medir."),
    ],
    C=[
        ("¿Qué debe tener una buena explicación de una elección?", "Una razón que se puede comprobar", "Con ella se convence con hechos."),
        ("¿Por qué las pruebas ayudan a explicar?", "Porque dan datos reales", "Muestran lo que pasó."),
        ("¿Cómo se debe hablar de la idea de otra persona?", "Con respeto, diciendo qué cumple y qué mejorar", "Se habla de la idea, no de la persona."),
    ],
    A=[
        ("Completa: «Elegí el vaso porque soportó ___ fichas». El vaso soportó 7 fichas y el plato 3. Escribe el número.", "7", "El dato del vaso es 7."),
        ("Idea 1 pasó la prueba 3 veces de 3. Idea 2 pasó 1 vez de 3. Escribe cuál eliges y por qué en pocas palabras.", "La idea 1 porque pasó las 3 pruebas", "Tiene más pruebas pasadas."),
        ("Marta dice «mi modelo es mejor porque lo hice yo». ¿Qué le falta a su razón?", "Un dato de prueba", "Quién lo hizo no mide si funciona."),
    ],
    Z=[
        ("Dos niños eligieron ideas distintas. Uno tiene 5 de 5 pruebas pasadas y otro 3 de 5. Sin ofender, ¿qué puede decir el segundo para mejorar?", "Que probará de nuevo para pasar más pruebas", "Propone una mejora sin burlarse."),
        ("Pedro eligió la idea A, que no pasó ninguna prueba, porque es su favorita. ¿Es una buena explicación? Responde sí o no.", "No", "Los datos no apoyan su elección."),
    ],
    D=[
        ("Ideas: A soporta 4 fichas, B soporta 6, C soporta 5. Necesitas soportar al menos 5. ¿Qué ideas sirven?", "B y C", "Ambas soportan 5 o más."),
        ("La idea B soporta 6 fichas y la idea C soporta 5 fichas. Necesitas soportar al menos 5. La base de B mide 25 cm y el máximo permitido es 20 cm. La base de C mide 18 cm. ¿Cuál eliges?", "C", "B se pasa del límite de la base; C cumple todo."),
    ],
    ctx=("Pía debe elegir entre dos portalápices. El de cartón soportó 10 lápices y se mantuvo derecho 3 de 3 pruebas. El de papel soportó 4 lápices. Ella necesita guardar 8 lápices. Escribe cuál elige y por qué.", "El de cartón porque soportó 10 lápices y pasó las 3 pruebas", "Cumple lo que ella necesita."),
    sc=[
        ("¿Qué palabra une decisión y razón?", "Porque", "Conecta decisión con razón."),
        ("¿Un gusto, como «me gusta el verde», basta para decidir un diseño? Responde sí o no.", "No", "Falta un dato."),
        ("¿Se debe burlar de las ideas de otros al explicar? Responde sí o no.", "No", "Se debe respetar."),
    ],
    open_task=(
        "Mira estos datos de dos marcadores. Marcador A: se ve al cerrar el libro, no rompe las hojas, mide 18 cm. Marcador B: no se ve al cerrar el libro, no rompe las hojas, mide 12 cm. Criterios: se ve al cerrar el libro y no rompe las hojas. Escribe cuál eliges con porque y dos datos, y una mejora para el otro.",
        "Elegí el marcador A porque cumple los dos criterios: se ve al cerrar el libro y no rompe las hojas. Al B lo haría más largo para que se vea al cerrar el libro.",
        ["escribe la elección", "usa porque y datos comprobables", "propone una mejora respetuosa"],
        ["frase escrita con porque", "dos datos", "una mejora"],
        ["razones de gusto", "frases sin porque", "burlas"],
        "Pide cambiar «me gusta» por un dato. Si no hay mejora, pregunta qué cambiaría en el otro marcador.",
    ),
    reinforce="Elige entre dos juguetes tuyos cuál es más fácil de guardar y di por qué con un dato.",
    extend="Explica una elección tuya usando tres pruebas con números.",
)

# ------------------------------------------------------------------ OA 02
reg(
    OA2, 1,
    materials="Un sobre de carta ya hecho (o la descripción de este cuaderno) y un lápiz. Puedes usar un sobre de papel que tengas en casa.",
    use="Aprenderé a mirar un objeto terminado y decir sus partes y qué trabajo hay que hacer para fabricarlo. Sirve para planear antes de empezar.",
    prior=["Sé nombrar partes de un objeto.", "Sé contar hasta 20."],
    explain=[
        "Antes de fabricar algo, miro el resultado esperado, que es el objeto ya terminado. Pregunto: ¿cómo se ve?, ¿qué partes tiene?, ¿qué tamaño tiene? Si no sé cómo termina, no sé cómo empezar.",
        "Tomemos un sobre. Tiene un cuerpo, que es el rectángulo doblado, y tiene una solapa, que se cierra con pegamento. Para fabricarlo se mide, se marca, se corta, se pliega y se une. Son cinco tareas.",
        "Una tarea es una acción que hay que hacer. Cada tarea ayuda a obtener el resultado: medir da el tamaño, cortar da la forma, plegar da las dobleces y unir cierra el sobre. Ver el resultado ayuda a pensar qué tareas se necesitan.",
    ],
    vocab=[("resultado esperado", "cómo debe quedar el objeto al terminar"), ("parte", "pedazo que forma el objeto"), ("tarea", "acción que hay que hacer en la fabricación"), ("medir", "saber el tamaño con una regla"), ("plegar", "doblar el papel formando una marca")],
    worked=[
        ("Partes del sobre", "Un sobre tiene un rectángulo doblado y una tapa que se pega. ¿Cuántas partes principales tiene?", ["Cuento el rectángulo doblado: 1.", "Cuento la tapa que se pega: 1.", "1 + 1 = 2."], "2 partes"),
        ("Tareas para el sobre", "Para fabricar un sobre hay que medir, marcar, cortar, plegar y unir. ¿Cuántas tareas hay?", ["Cuento medir: 1.", "Marcar: 2; cortar: 3; plegar: 4; unir: 5.", "Son cinco."], "5 tareas"),
    ],
    mistakes=[
        ("Empezar a cortar sin saber cómo debe quedar.", "No se conoce el resultado.", "Mira primero el objeto terminado y nombra sus partes."),
        ("Olvidar una tarea, como medir.", "El tamaño sale mal.", "Escribe todas las tareas antes de empezar."),
    ],
    R=[
        ("Un sobre tiene un cuerpo y una solapa. ¿Cuántas partes principales nombra esa frase?", "2", "Cuerpo y solapa son dos."),
        ("¿Qué tarea usas para saber el tamaño: medir o cortar?", "Medir", "Medir da el tamaño."),
        ("¿Qué tarea cierra el sobre: plegar o unir?", "Unir", "Se pega la tapa."),
    ],
    C=[
        ("¿Qué es el resultado esperado?", "Cómo debe quedar el objeto terminado", "Es la meta de la tarea."),
        ("¿Por qué conviene mirar primero el objeto terminado?", "Para saber qué partes y tareas hacen falta", "Ayuda a planear."),
        ("¿Qué es una tarea?", "Una acción que hay que hacer", "Medir y cortar son tareas."),
    ],
    A=[
        ("Para una cajita se debe medir, marcar, cortar, plegar y pegar. ¿Cuántas tareas son?", "5", "Se cuentan una por una."),
        ("Una caja de regalo tiene 1 tapa, 1 base y 4 paredes. ¿Cuántas partes tiene en total?", "6", "1 + 1 + 4 = 6."),
        ("En un marcador de página hay una tira y una lengüeta. Si hago 3 marcadores, ¿cuántas lengüetas necesito?", "3", "Cada marcador tiene una."),
    ],
    Z=[
        ("Luis ya midió y marcó las partes de un sobre, y quiere pegarlas, pero todavía no las cortó. ¿Qué tarea le falta antes de pegar?", "Cortar", "No puede pegar partes que no ha cortado."),
        ("Ana mira el sobre terminado y dice que debe medir 12 cm de ancho. ¿Qué tarea usará primero para lograrlo: medir o plegar?", "Medir", "Se necesita el tamaño antes de plegar."),
    ],
    D=[
        ("El sobre necesita 1 hoja. Si quieres hacer 5 sobres, ¿cuántas hojas necesitas?", "5", "Una hoja por sobre."),
        ("Para cada sobre se hacen 5 tareas. ¿Cuántas tareas haces en total para 2 sobres?", "10", "5 + 5 = 10."),
    ],
    ctx=("Tato quiere hacer una caja para guardar 6 tarjetas. La caja terminada tiene 1 base y 4 paredes. ¿Cuántas partes tiene que fabricar?", "5", "1 + 4 = 5 partes."),
    sc=[
        ("¿Para qué sirve mirar el resultado esperado?", "Para planear las partes y tareas", "Muestra qué hace falta."),
        ("¿Medir es una tarea? Responde sí o no.", "Sí", "Es una acción de fabricación."),
        ("¿Qué tarea da la forma: cortar o pegar?", "Cortar", "Cortar da la forma al papel."),
    ],
    open_task=(
        "Mira un sobre de carta de tu casa, o imagina uno de 12 cm de ancho con una tapa. Dibuja el sobre terminado, escribe el nombre de 2 partes y la lista de las 5 tareas que se hacen para fabricarlo: medir, marcar, cortar, plegar y unir.",
        "Dibujé un sobre con el cuerpo y la solapa rotulados. Tareas: 1 medir, 2 marcar, 3 cortar, 4 plegar, 5 unir.",
        ["dibuja el resultado esperado", "nombra 2 partes", "lista las 5 tareas"],
        ["dibujo del sobre", "lista de tareas"],
        ["olvida una tarea", "no rotula partes"],
        "Pregunta: ¿cómo debe quedar al final? Si falta una tarea, pide leer el sobre otra vez.",
    ),
    reinforce="Mira un objeto de tu casa y cuenta sus partes.",
    extend="Elige otro objeto simple, como una bolsa de papel, y escribe sus tareas de fabricación.",
)

reg(
    OA2, 2,
    materials="Tarjetas de tareas escritas en este cuaderno y un lápiz. Puedes recortar las tarjetas de papel si quieres, pero no es obligatorio.",
    use="Aprenderé a poner las tareas en orden con pasos numerados. Sirve para que el trabajo salga bien sin perder tiempo ni material.",
    prior=["Sé las tareas de fabricar un sobre.", "Sé numerar del 1 al 10."],
    explain=[
        "El orden de las tareas importa. No se puede pegar antes de cortar ni plegar antes de medir. Un buen plan dice qué va primero, qué va después y qué va al final.",
        "Para ordenar, pregunta qué necesita cada tarea. Para cortar, ya debo haber medido y marcado. Para plegar, ya debo haber cortado. Para unir, ya debo haber plegado. Así el orden sale solo.",
        "Escribe los pasos con números y una acción en cada uno: 1 medir, 2 marcar, 3 cortar. Una frase corta por paso. Si cambias el orden, el resultado puede salir mal. Un plan escrito sirve para revisar si olvidaste algo.",
    ],
    vocab=[("orden", "qué va primero, después y al final"), ("paso", "una acción dentro de un plan"), ("plan", "lista de pasos antes de trabajar"), ("antes", "va primero"), ("después", "va más tarde")],
    worked=[
        ("Ordenar tres tareas", "Ordena: cortar, medir, marcar.", ["Primero se mide.", "Luego se marca con lápiz.", "Después se corta."], "1 medir, 2 marcar, 3 cortar"),
        ("Ordenar cinco tareas", "Ordena para un sobre: unir, plegar, medir, cortar, marcar.", ["Medir va primero.", "Marcar va después.", "Cortar, luego plegar.", "Unir es al final."], "1 medir, 2 marcar, 3 cortar, 4 plegar, 5 unir"),
    ],
    mistakes=[
        ("Pegar antes de plegar.", "El sobre queda abierto o mal armado.", "Primero pliega, y al final une."),
        ("Cortar sin marcar antes.", "El corte sale chueco.", "Marca la línea con lápiz y luego corta."),
    ],
    R=[
        ("Ordena: marcar, medir. ¿Cuál va primero?", "Medir", "Se mide antes de marcar."),
        ("Ordena: unir, cortar. ¿Cuál va primero?", "Cortar", "Se pega algo que ya se cortó."),
        ("Para un sobre: ¿se pliega antes o después de unir?", "Antes", "Se pliega y luego se une."),
    ],
    C=[
        ("¿Por qué importa el orden de las tareas?", "Porque algunas necesitan que otras estén hechas", "Se depende del paso anterior."),
        ("¿Qué escribimos al lado de cada paso para ordenarlo?", "Un número", "Los números indican el orden."),
        ("¿Para qué sirve escribir el plan?", "Para revisar que no falte ningún paso", "Una lista se puede revisar."),
    ],
    A=[
        ("Ordena con números las tareas de un marcador de papel: cortar, medir, plegar la lengüeta, marcar. Escribe el orden.", "Medir, marcar, cortar, plegar la lengüeta", "El orden va de medir a plegar."),
        ("Un plan dice: 1 medir, 2 marcar, 3 cortar. ¿Qué número tiene «cortar»?", "3", "Es el tercer paso."),
        ("Para una caja: pegar las paredes, cortar el cartón, medir el cartón. ¿Cuál es el último paso?", "Pegar las paredes", "Se pega lo que ya está cortado y medido."),
    ],
    Z=[
        ("Rita ordenó: 1 unir, 2 cortar, 3 medir. ¿Está bien ordenado? Responde sí o no.", "No", "Medir debe ir antes que cortar y unir."),
        ("Ema dice que puede marcar la línea de corte después de cortar. ¿Qué problema habría?", "La línea ya no serviría para guiar el corte", "La marca se hace antes para guiar el corte."),
    ],
    D=[
        ("Ordena los 6 pasos: revisar el resultado, medir, cortar, marcar, plegar, unir. Escribe el orden completo.", "Medir, marcar, cortar, plegar, unir, revisar el resultado", "Revisar va al final, cuando el objeto ya está hecho."),
        ("En un plan de 5 pasos, ¿cuántos pasos van antes del tercero?", "2", "Antes del 3 están el 1 y el 2."),
    ],
    ctx=("Nico hace un portalápices. Sus tarjetas dicen: A pegar la base, B cortar el cartón, C medir 10 cm. ¿En qué orden las hace?", "C, B, A", "Primero medir, luego cortar, al final pegar."),
    sc=[
        ("¿Qué va primero: medir o cortar?", "Medir", "El tamaño guía el corte."),
        ("¿El orden de las tareas puede cambiarse sin problema? Responde sí o no.", "No", "Algunas dependen de otras."),
        ("¿Qué va al final en un sobre: unir o medir?", "Unir", "Es el último paso."),
    ],
    open_task=(
        "Ordena con números estas 5 tareas para fabricar una cajita de papel: pegar las orillas, cortar el rectángulo, doblar las paredes, medir 12 cm por lado, marcar con lápiz. Escribe los pasos del 1 al 5 y una frase de lo que pasaría si cambiaras uno.",
        "1 medir 12 cm por lado, 2 marcar con lápiz, 3 cortar el rectángulo, 4 doblar las paredes, 5 pegar las orillas. Si pego antes de doblar, no se arma la caja.",
        ["ordena las 5 tareas", "numera los pasos", "explica un cambio de orden"],
        ["lista numerada", "frase de explicación"],
        ["pegar antes de doblar", "no numerar"],
        "Pide leer la lista en voz alta como si fuera un trabajo real y buscar si algún paso depende de otro.",
    ),
    reinforce="Escribe en orden los pasos para lavarte los dientes.",
    extend="Escribe un plan de 6 pasos para armar una bolsa de papel.",
)

reg(
    OA2, 3,
    materials="Una lista de materiales descritos en este cuaderno y un lápiz. Si quieres, mira papel, cartón y cinta en casa.",
    use="Aprenderé a elegir el material correcto para cada parte de un objeto. Sirve para que el objeto resista y sirva lo que debe servir.",
    prior=["Sé nombrar materiales como papel y cartón.", "Sé que un objeto tiene partes."],
    explain=[
        "Los materiales tienen características. El papel es liviano y fácil de doblar. El cartón es más firme y aguanta peso. La cinta adhesiva une cosas. Cada parte de un objeto necesita un material que haga bien su trabajo.",
        "Para elegir, pregunta qué debe hacer la parte. Si debe doblarse y ser liviana, sirve el papel. Si debe sostener peso, sirve el cartón. Si debe unir dos partes, sirve la cinta o el pegamento escolar. No hay un material que sirva para todo.",
        "También piensa en la seguridad y en cuidar el medio ambiente. Usa materiales limpios y sin puntas. Siempre que puedas, reutiliza cajas y papeles que ya no uses. Así cuidas el planeta y gastas menos.",
    ],
    vocab=[("material", "lo que se usa para hacer algo"), ("firme", "que no se dobla fácil"), ("liviano", "que pesa poco"), ("unir", "pegar dos partes"), ("reutilizar", "usar de nuevo un material")],
    worked=[
        ("Elegir para sostener peso", "La base de un portalápices debe aguantar 8 lápices. Opciones: papel delgado o cartón. ¿Cuál eliges?", ["La base debe ser firme.", "El papel delgado se dobla con el peso.", "El cartón aguanta."], "Cartón"),
        ("Elegir para unir", "Debes unir dos orillas de papel. Opciones: cinta adhesiva o una piedra. ¿Cuál eliges?", ["Unir es pegar dos partes.", "La cinta adhesiva pega.", "La piedra no une."], "Cinta adhesiva"),
    ],
    mistakes=[
        ("Elegir un material solo por el color.", "El color no dice si resiste.", "Elige por lo que debe hacer la parte: sostener, doblar o unir."),
        ("Usar un material con bordes filosos.", "Puede cortar.", "Usa papel, cartón y plástico limpio sin bordes cortantes."),
    ],
    R=[
        ("¿Qué material es más firme: papel delgado o cartón?", "Cartón", "El cartón se dobla menos."),
        ("¿Qué sirve para unir dos partes: cinta adhesiva o lápiz?", "Cinta adhesiva", "La cinta pega."),
        ("¿Qué material es más fácil de doblar: papel o cartón grueso?", "Papel", "El papel se dobla mejor."),
    ],
    C=[
        ("¿Qué debes preguntar antes de elegir un material para una parte?", "Qué debe hacer esa parte", "El trabajo de la parte guía la elección."),
        ("¿Qué significa reutilizar?", "Usar de nuevo un material", "Se aprovecha lo que ya existe."),
        ("¿Por qué conviene un material sin bordes cortantes?", "Para no hacerse daño", "Es una regla de seguridad."),
    ],
    A=[
        ("Una pared de cartón se dobla al poner 2 lápices. Otra pared de cartón corrugado aguanta 8 lápices. ¿Cuál usas para guardar 8 lápices?", "La de cartón corrugado", "Aguanta los 8 lápices."),
        ("La tapa de una caja debe doblarse varias veces sin romperse. Opciones: papel resistente o cartón muy grueso. ¿Cuál sirve más?", "Papel resistente", "Se dobla y no se rompe."),
        ("Una tira de 15 cm debe sostener 3 fichas sin doblarse. Opciones: papel delgado o cartón. ¿Cuál eliges?", "Cartón", "Aguanta el peso."),
    ],
    Z=[
        ("Ana quiere hacer una caja fuerte con papel de cuaderno y dice que no se romperá nunca. ¿Tiene razón? Responde sí o no.", "No", "El papel de cuaderno es delgado y se rompe fácil."),
        ("Teo usó una lata con borde filoso para guardar lápices porque es dura. ¿Qué problema de seguridad tiene?", "Puede cortar", "El borde filoso hiere."),
    ],
    D=[
        ("Necesitas 4 paredes de cartón de 10 cm de alto cada una. ¿Cuántos cm de cartón hay en altura si las pones una sobre otra?", "40", "10 + 10 + 10 + 10 = 40."),
        ("Reutilizas 3 cajas de cereal. Cada caja da 2 paredes. ¿Cuántas paredes tienes en total?", "6", "2 + 2 + 2 = 6."),
    ],
    ctx=("Pía hace un cofre para sus 5 tarjetas. Para la base necesita algo firme; para la tapa, algo que se doble; para unir, algo que pegue. Tiene cartón, papel resistente y cinta. Une cada parte con su material en el orden base, tapa, unión.", "Base: cartón; tapa: papel resistente; unión: cinta", "Cada material cumple la función de la parte."),
    sc=[
        ("¿Qué material elegirías para una base firme?", "Cartón", "Aguanta el peso."),
        ("¿Qué material unes con cinta: papel o piedra?", "Papel", "La cinta pega papel."),
        ("¿Dónde puedes conseguir cartón reutilizado en casa?", "En cajas ya usadas", "Reutilizar cuida el planeta."),
    ],
    open_task=(
        "Para un contenedor de tarjetas hay tres partes: base, tapa y unión. Los materiales disponibles son cartón de caja de cereal, papel resistente de bolsa y cinta adhesiva. Escribe qué material usas en cada parte y por qué. Dibuja el contenedor con los materiales rotulados.",
        "Base: cartón, porque es firme. Tapa: papel de bolsa, porque se dobla. Unión: cinta, porque pega. Dibujé el contenedor con los tres rótulos.",
        ["relaciona cada parte con un material", "da una razón", "dibuja con rótulos"],
        ["tabla parte-material", "dibujo rotulado"],
        ["elegir por el color", "no dar razones"],
        "Pide cambiar «porque me gusta» por una característica del material, como firme o liviano.",
    ),
    reinforce="Toca tres materiales de tu casa y di si son firmes o livianos.",
    extend="Compara dos materiales para una misma parte y escoge uno con razón.",
)

reg(
    OA2, 4,
    materials="Una lista de herramientas escolares descritas en este cuaderno y un lápiz. Las herramientas reales solo se usan con ayuda de un adulto.",
    use="Aprenderé a elegir la herramienta correcta para cada acción y a usarla con cuidado. Sirve para trabajar bien y sin accidentes.",
    prior=["Sé las tareas de fabricar un objeto de papel.", "Sé que un material se elige por su función."],
    explain=[
        "Una herramienta es un objeto que ayuda a hacer una acción. La regla mide, el lápiz marca, la tijera de punta roma corta, el pegamento escolar une. Cada herramienta sirve para una acción distinta.",
        "Para elegir, mira la acción de tu paso. Si la acción es cortar, la herramienta es la tijera. Si es medir, la regla. Usar la herramienta equivocada, como cortar con una regla, no funciona y puede ser peligroso.",
        "Usa las herramientas con cuidado. Corta lejos de tu cuerpo y de otras personas. Pide ayuda a un adulto con la tijera. Cuando termines, guarda todo en su lugar. Trabajar con cuidado es parte de ser un buen diseñador.",
    ],
    vocab=[("herramienta", "objeto que ayuda a hacer una acción"), ("regla", "herramienta para medir"), ("tijera de punta roma", "tijera para cortar con punta redondeada"), ("pegamento escolar", "adhesivo que une papel y cartón"), ("cuidado", "usar algo sin hacerse daño ni dañar a otros")],
    worked=[
        ("Herramienta para medir", "Debes saber cuántos cm mide una tira. ¿Qué herramienta usas?", ["La acción es medir.", "La regla sirve para medir."], "La regla"),
        ("Herramienta para cortar", "Debes cortar una línea marcada en papel. ¿Qué herramienta y qué cuidado necesitas?", ["La acción es cortar.", "La tijera de punta roma corta papel.", "Se usa con ayuda de un adulto y lejos del cuerpo."], "Tijera de punta roma con ayuda de un adulto"),
    ],
    mistakes=[
        ("Cortar con la regla.", "La regla no corta y se daña.", "Mide con la regla; corta con la tijera de punta roma."),
        ("Agitar la tijera o caminar con ella abierta.", "Puede lastimar a alguien.", "Llévala cerrada, con la punta hacia abajo, y camina sin correr."),
    ],
    R=[
        ("¿Qué herramienta sirve para medir: regla o pegamento?", "Regla", "La regla tiene números."),
        ("¿Qué herramienta sirve para marcar una línea: lápiz o tijera?", "Lápiz", "El lápiz dibuja la línea."),
        ("¿Qué herramienta sirve para unir papel: pegamento escolar o regla?", "Pegamento escolar", "Une las partes."),
    ],
    C=[
        ("¿Qué es una herramienta?", "Un objeto que ayuda a hacer una acción", "Sirve para trabajar."),
        ("¿Con quién debes usar la tijera si eres pequeño?", "Con ayuda de un adulto", "Es una regla de seguridad."),
        ("¿Por qué se usa tijera de punta roma?", "Para evitar pinchazos", "La punta redondeada es más segura."),
    ],
    A=[
        ("Une cada acción con su herramienta: medir, marcar, cortar, unir. Herramientas: lápiz, pegamento, regla, tijera. Escribe las parejas en ese orden.", "Medir con regla, marcar con lápiz, cortar con tijera, unir con pegamento", "Cada acción tiene su herramienta."),
        ("Una tira mide entre las marcas 2 y 14 de la regla. ¿Cuántos cm mide?", "12", "14 − 2 = 12."),
        ("Para trazar una línea recta entre dos puntos, ¿qué dos herramientas usas: lápiz y regla o tijera y pegamento?", "Lápiz y regla", "Una dibuja y la otra guía."),
    ],
    Z=[
        ("Luis usó el pegamento para marcar una línea. ¿Fue la herramienta correcta? Responde sí o no.", "No", "Para marcar se usa lápiz."),
        ("Ema camina por la sala con la tijera abierta. ¿Qué regla de cuidado no cumple?", "Llevar la tijera cerrada", "Debe llevarla cerrada y sin correr."),
    ],
    D=[
        ("Para un sobre usas 4 herramientas: regla, lápiz, tijera y pegamento. Si hay que hacer 3 sobres, ¿cuántas herramientas distintas necesitas en total?", "4", "Las mismas herramientas sirven para los 3 sobres."),
        ("Una tira de cartón mide 24 cm. Debes cortarla en 2 partes del mismo largo. ¿Cuánto mide cada parte?", "12 cm", "12 + 12 = 24."),
    ],
    ctx=("Nico debe hacer un marcador: medir 18 cm, marcar la línea, cortar y pegar la lengüeta. Tiene regla, lápiz, tijera de punta roma y pegamento. Escribe la herramienta de cada acción en orden.", "Regla, lápiz, tijera, pegamento", "Cada acción usa la herramienta que le corresponde."),
    sc=[
        ("¿Qué herramienta corta papel con seguridad en la escuela?", "Tijera de punta roma", "Está hecha para papel."),
        ("¿La regla sirve para cortar papel? Responde sí o no.", "No", "La regla mide; para cortar se usa la tijera."),
        ("Después de trabajar, ¿qué haces con las herramientas?", "Las guardas en su lugar", "Es parte del cuidado."),
    ],
    open_task=(
        "Mira esta lista de acciones para hacer un marcador de página: medir, marcar, cortar, unir. Escribe la herramienta de cada acción (regla, lápiz, tijera de punta roma, pegamento escolar) y una regla de cuidado que cumplirás al usar la tijera.",
        "Medir con regla, marcar con lápiz, cortar con tijera de punta roma, unir con pegamento escolar. Con la tijera la uso con un adulto y cortando lejos de mi cuerpo.",
        ["une cada acción con su herramienta", "escribe una regla de cuidado", "nombra bien las herramientas"],
        ["lista acción-herramienta", "regla de cuidado escrita"],
        ["usar la herramienta equivocada", "olvidar el cuidado"],
        "Si hay error, muestra una acción y pregunta qué herramienta la hace. Pide repetir la regla de cuidado.",
    ),
    reinforce="Mira tu estuche y di para qué acción sirve cada objeto.",
    extend="Explica cómo cambiaría el trabajo si no tuvieras regla y qué usarías para medir.",
)

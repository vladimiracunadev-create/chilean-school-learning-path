"""Cuaderno del estudiante, 3.º básico Tecnología: OA 01 (diseño de objetos y sistemas simples), parte 1.

Las clases 1 a 3 del OA 01 viven aquí; las clases 4 a 6 en student_content_te3_a2.
Seguridad: solo tijeras de punta roma, papel, cartón y cinta; nada de cortadores, fuego ni vidrio.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE03 OA 01"


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
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para hacerle preguntas.",
    use="Aprenderé a investigar un problema antes de diseñar: observar, preguntar y anotar datos del usuario y del lugar. Sirve para no diseñar a ciegas.",
    prior=["Sé decir quién es el usuario, qué necesita y en qué contexto lo usa.", "Sé que un boceto es un dibujo rápido a mano alzada."],
    explain=[
        "Un problema tecnológico aparece en un ámbito: la casa, la escuela, el transporte o el cuidado de las plantas. Antes de diseñar hay que investigarlo. Investigar es reunir datos con dos acciones: observar y preguntar. Observar es mirar con atención lo que pasa. Preguntar es pedir información a quien tiene el problema.",
        "Buenas preguntas son abiertas: «¿qué parte te cuesta más?». Una pregunta cerrada solo se responde con sí o no y da pocos datos. Anota lo que ves y lo que te dicen con números cuando se pueda: cuántos libros, cuántos pasos, cuántos minutos. Los datos con número se pueden comparar después.",
        "También sirven los temas de otras asignaturas. En Ciencias aprendiste que una planta necesita luz y agua; ese dato ayuda a diseñar un regador. En Matemática, medir con la regla da datos exactos. Termina siempre con una frase: «El problema es que (usuario) necesita (lograr algo) en (lugar)». No nombres todavía el objeto.",
    ],
    vocab=[("investigar", "reunir datos observando y preguntando"), ("observar", "mirar con atención lo que ocurre"), ("pregunta abierta", "pregunta que no se responde solo con sí o no"), ("dato", "información anotada, a veces con número"), ("ámbito tecnológico", "área donde se usan objetos, como la casa o el transporte")],
    worked=[
        ("Convertir observaciones en el problema", "Observaste a Nina en el recreo: guarda 6 lápices en el bolsillo y 2 se caen cada día. Dice: «Me cuesta que no se pierdan». Escribe la frase del problema.", ["Usuaria: Nina. Lugar: el recreo.", "Lo que necesita lograr: que los lápices no se pierdan.", "Armo la frase sin nombrar un objeto."], "Nina necesita que sus lápices no se pierdan en el recreo"),
        ("Elegir la mejor pregunta", "Quieres saber cómo riega su planta Don Hugo. ¿Cuál sirve más: A «¿Riegas?» o B «¿Qué te cuesta más al regar?»", ["A se responde con sí o no.", "B pide contar lo que le pasa.", "B da más datos."], "B, porque es una pregunta abierta"),
    ],
    mistakes=[
        ("Escribir «el problema es que falta una caja».", "Nombra el objeto antes de entender el problema.", "Di qué no se logra: «los lápices se pierden»."),
        ("Preguntar solo «¿te gusta?» al usuario.", "Se responde con sí o no y no da datos útiles.", "Pregunta qué le cuesta, cuándo y dónde."),
    ],
    R=[
        ("Para investigar sirven dos acciones: observar y preguntar. ¿Mirar con atención lo que pasa es observar o preguntar?", "Observar", "Mirar es observar."),
        ("«¿Qué parte te cuesta más?» ¿es una pregunta abierta o cerrada?", "Abierta", "No se responde solo con sí o no."),
        ("«La casa» y «el transporte» son lugares de uso. ¿Cómo se llama el área donde se usan objetos: ámbito tecnológico o dato?", "Ámbito tecnológico", "Es el área de uso, como casa o transporte."),
    ],
    C=[
        ("Anotaste «se cayeron 2 de 6 lápices». ¿Es un dato con número o una opinión?", "Un dato con número", "Dice cantidades comprobables."),
        ("¿Por qué conviene anotar datos con número y no solo «se cae mucho»?", "Porque se pueden comparar después", "Los números permiten comparar antes y después."),
        ("Una planta necesita luz y agua. ¿Ese dato viene de Ciencias o de Música?", "De Ciencias", "Lo aprendiste estudiando las plantas."),
    ],
    A=[
        ("Observaste que Tomás carga 4 cuadernos y 1 botella, y que 1 cuaderno se le cae en la escalera. Escribe la frase del problema.", "Tomás necesita llevar sus cuadernos y su botella sin que se caigan en la escalera", "Lleva usuario, qué lograr y lugar."),
        ("Quieres saber cuántas veces al día Rita busca su colación en la mochila. ¿Qué haces: observar un día o inventar el número?", "Observar un día", "Los datos se obtienen mirando, no inventando."),
        ("Eres diseñadora y preguntas a Sami. Ordena: A anotar la respuesta, B hacer una pregunta abierta. ¿Cuál va primero?", "B", "Primero se pregunta; después se anota."),
    ],
    Z=[
        ("Mía dice: «Ya sé el objeto, no necesito investigar». ¿Qué riesgo corre? Responde con una frase.", "Que el objeto no resuelva el problema real", "Sin datos puede diseñar algo que no sirve."),
        ("Dos frases: A «el problema es que Luis necesita guardar 5 lápices en su pieza» y B «el problema es que falta un lapicero». ¿Cuál está mejor escrita?", "A", "A dice qué se debe lograr; B nombra el objeto."),
    ],
    D=[
        ("Caso: en la sala, 3 de 8 niños no alcanzan el interruptor de la luz. Escribe usuario, necesidad y una pregunta abierta para investigar más.", "Usuarios: 3 niños; necesidad: encender la luz; pregunta por ejemplo: ¿qué te cuesta al intentar encenderla?", "Pide tres elementos con el caso."),
        arith("Anotaste que Pía intentó regar su planta 5 veces y que el agua se derramó en 3 de ellos. ¿En cuántos intentos NO se derramó?", "5-3", "Se restan los intentos con derrame del total."),
    ],
    ctx=("Observas a doña Rosa, la vecina, en la cocina: cada vez que sirve la sopa, cae 1 gota en 4 cucharadas que echa en el plato. Dice: «Me cuesta no manchar». Escribe usuario, lugar, dato con número y la frase del problema.", "Usuaria: doña Rosa. Lugar: la cocina. Dato: cae 1 gota en 4 cucharadas. Problema: doña Rosa necesita servir la sopa sin manchar", "Cubre los cuatro elementos pedidos."),
    sc=[
        ("¿Qué dos acciones sirven para investigar un problema?", "Observar y preguntar", "Son las dos formas de reunir datos."),
        ("¿Una pregunta abierta se responde solo con sí o no?", "No", "Pide contar con más palabras."),
        ("¿La frase del problema nombra el objeto o dice qué no se logra?", "Dice qué no se logra", "El objeto se decide después."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: en una casa, a Juan se le caen 3 de 7 prendas al subir al segundo piso. Caso 2: en la sala, una planta recibe poca luz y se tuerce hacia la ventana. Escribe un dato con número, una pregunta abierta para el usuario y la frase del problema sin nombrar un objeto.",
        "Caso 1: dato: 3 de 7 prendas caen. Pregunta: ¿en qué momento se te caen más? Problema: Juan necesita subir su ropa sin que se caiga.",
        ["escribe un dato con número", "hace una pregunta abierta", "la frase del problema dice usuario, qué lograr y lugar", "no nombra el objeto"],
        ["ficha con dato, pregunta y frase del problema"],
        ["nombrar el objeto en el problema", "pregunta que se responde con sí o no"],
        "Pregunta: «¿esto dice lo que no se logra o ya dice un objeto?». Si dice un objeto, pídele reescribir con la necesidad.",
    ),
    reinforce="Observa a alguien de tu casa durante 5 minutos al hacer una tarea y anota 2 cosas que le cuesten.",
    extend="Escribe una pregunta abierta para saber qué problema tienen en la escuela con el orden de las mochilas.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz y regla. Las listas de criterios están escritas en el cuaderno.",
    use="Aprenderé a escribir criterios y restricciones que se puedan comprobar. Sirve para saber, al final, si mi diseño sí resolvió el problema.",
    prior=["Sé investigar un problema y escribir su frase.", "Sé que una restricción es un límite."],
    explain=[
        "Un criterio es algo que el diseño debe cumplir para resolver el problema. Una restricción es un límite que no se puede pasar. Por ejemplo, criterio: «sostiene 12 fichas». Restricción: «la base mide como máximo 20 cm por 20 cm». Ambos se escriben antes de diseñar.",
        "Un buen criterio se puede comprobar con una acción: contar, medir o probar. «Debe ser fuerte» no se puede comprobar. «Sostiene 12 fichas sin caerse» sí. Cuando escribas un criterio, pregúntate: ¿cómo lo comprobaré?",
        "Hay criterios de varios tipos. Los técnicos hablan de tamaño o resistencia. Los de seguridad piden que no haya puntas ni bordes que corten. Los del medioambiente piden usar material reutilizado o gastar poco. Escribe al menos uno técnico, uno de seguridad y uno del medioambiente.",
    ],
    vocab=[("criterio", "algo que el diseño debe cumplir"), ("restricción", "límite que no se puede pasar"), ("comprobar", "revisar con una acción si algo se cumple"), ("técnico", "que habla de tamaño, medida o resistencia"), ("medioambiente", "naturaleza que nos rodea y que debemos cuidar")],
    worked=[
        ("Mejorar un criterio", "Un criterio dice «el soporte debe ser fuerte». Reescríbelo para poder comprobarlo con 12 fichas.", ["«Fuerte» no se puede medir.", "Elijo una acción: poner las fichas.", "Escribo cuántas y qué debe pasar."], "El soporte sostiene 12 fichas sin caerse"),
        ("Clasificar criterios", "Clasifica: A «no tiene puntas que pinchen», B «usa cartón que ya se usó». ¿Cuál es de seguridad y cuál del medioambiente?", ["A habla de no lastimarse: seguridad.", "B habla de reutilizar: medioambiente."], "A es de seguridad y B del medioambiente"),
    ],
    mistakes=[
        ("Escribir «debe verse lindo» como criterio.", "No se puede comprobar con una medida o una prueba.", "Escribe algo medible: «tiene 3 colores» o «cabe en la mochila»."),
        ("Confundir criterio con restricción.", "Criterio es lo que debe lograr; restricción es el límite que no pasa.", "Pregunta: ¿es algo que logra o un tope? Tope es restricción."),
    ],
    R=[
        ("«La base mide como máximo 20 cm» ¿es un límite o algo que el diseño logra?", "Un límite", "Marca un tope: es restricción."),
        ("Un criterio de seguridad dice que no debe haber puntas. ¿Cuida a las personas o al medioambiente?", "A las personas", "Las puntas pueden lastimar."),
        ("Usar cartón ya usado ¿es un criterio técnico o del medioambiente?", "Del medioambiente", "Reutiliza y cuida los recursos."),
    ],
    C=[
        ("¿Cuál se puede comprobar: A «debe ser bonito» o B «cabe en una mochila de 30 cm de ancho»?", "B", "Se mide con una regla."),
        ("¿Con qué tres acciones se comprueba un criterio?", "Contar, medir o probar", "Son las formas de comprobar."),
        ("«Sostiene 12 fichas» ¿es una restricción o un criterio?", "Un criterio", "Dice lo que el diseño logra."),
    ],
    A=[
        ("Problema: llevar 3 libros sin que caigan. Escribe un criterio comprobable que use el número 3.", "Lleva 3 libros sin que caigan", "Usa el 3 y se prueba."),
        ("Una caja mide 25 cm y la mochila mide 30 cm. Si la restricción es «menos de 30 cm», ¿cumple?", "Sí", "25 es menor que 30."),
        ("Un diseño se hará con 2 cartones usados. ¿Qué tipo de criterio escribirías: técnico, de seguridad o del medioambiente?", "Del medioambiente", "Reutiliza materiales que ya existen."),
    ],
    Z=[
        ("Lalo escribe: «debe ser resistente». ¿Qué le falta? Responde con una frase.", "Una forma de comprobarlo, como una prueba con peso", "Sin prueba no se puede saber."),
        ("Un diseño cumple los criterios de tamaño y de resistencia, pero tiene una punta que corta. ¿Debe corregirse? Responde sí o no y por qué.", "Sí, porque no cumple la seguridad", "La seguridad va primero."),
    ],
    D=[
        ("Reto: soporte para 12 fichas. Escribe un criterio técnico, uno de seguridad y uno del medioambiente.", "Por ejemplo: sostiene 12 fichas; sin bordes que corten; usa cartón reutilizado", "Tres criterios de tipos distintos."),
        arith("Un soporte debe sostener 12 fichas y ya sostiene 7. ¿Cuántas fichas más debe sostener para cumplir?", "12-7", "Falta la diferencia entre lo pedido y lo logrado."),
    ],
    ctx=("Dani diseña un guardalápices con cartón reutilizado. Debe guardar 6 lápices, caber en un espacio de 15 cm de ancho y no tener puntas. Escribe tres criterios y una restricción.", "Criterios: guarda 6 lápices; no tiene puntas; usa cartón reutilizado. Restricción: ancho máximo de 15 cm", "Separa lo que debe lograr del tope."),
    sc=[
        ("¿Un criterio debe poder comprobarse?", "Sí", "Si no se comprueba no sirve para evaluar."),
        ("¿Una restricción es un límite o algo que el diseño logra?", "Un límite", "Es un tope que no se pasa."),
        ("¿Qué tipo de criterio es «sin bordes que corten»?", "De seguridad", "Cuida a quien lo usa."),
    ],
    open_task=(
        "Escoge un problema. Problema 1: un soporte que sostenga 12 fichas con una base de 20 cm por 20 cm. Problema 2: un lapicero para 6 lápices que quepa en 15 cm. Escribe tres criterios comprobables (técnico, de seguridad y del medioambiente) y una restricción con número.",
        "Problema 1: criterios: sostiene 12 fichas; sin puntas; cartón reutilizado. Restricción: base menor que 20 cm.",
        ["escribe tres criterios de tipos distintos", "cada criterio se puede comprobar", "escribe una restricción con número y unidad"],
        ["lista de criterios y restricción"],
        ["criterios como «debe ser lindo»", "restricción sin número"],
        "Pregunta: «¿cómo comprobarás este criterio?». Si no puede decirlo, ayúdale a escribirlo con una acción.",
    ),
    reinforce="Mira un objeto de tu casa e inventa un criterio comprobable y una restricción para él.",
    extend="Escribe cómo comprobarías el criterio «cabe en una mochila» usando una regla.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hojas y lápiz. Los productos que se combinan están descritos en el cuaderno.",
    use="Aprenderé a generar muchas ideas distintas y a combinar productos que ya existen. Sirve para encontrar una solución mejor.",
    prior=["Sé que dos ideas son distintas si funcionan de otra forma.", "Sé escribir criterios comprobables."],
    explain=[
        "Generar ideas es pensar muchas soluciones, aunque algunas parezcan raras. Por ahora no se critica ninguna. Se escriben o se dibujan todas. Después se elige con los criterios.",
        "Una buena técnica es combinar productos que ya existen. Por ejemplo, una pinza de ropa y una caja de cartón pueden formar un soporte para papeles. También puedes cambiar un material, agrandar una parte o usar el objeto para otra cosa. Combinar y cambiar da ideas nuevas con poco esfuerzo.",
        "Las ideas distintas funcionan de otra forma, no solo cambian de color. Pon un nombre corto a cada idea y anota qué producto existente usa. Así, después, sabrás de dónde viene cada parte. También puedes mirar otros ámbitos: cómo una pinza de ropa sujeta papeles en la casa puede servir en la escuela.",
    ],
    vocab=[("idea divergente", "idea que va por un camino distinto a las otras"), ("combinar", "unir partes de productos que ya existen"), ("producto existente", "objeto que ya se fabrica y se usa"), ("transferir", "usar una idea de un lugar en otro lugar")],
    worked=[
        ("Combinar dos productos", "Problema: sostener 3 papeles de pie sobre la mesa. Tienes una pinza de ropa y un cartón doblado. Escribe una idea que los combine.", ["Una pinza sujeta papeles.", "Un cartón doblado se mantiene de pie.", "Uno la pinza al cartón."], "Una pinza pegada al cartón doblado sujeta los papeles de pie"),
        ("Distinguir ideas", "Ideas para sostener un dibujo: A pinza de ropa, B pinza de ropa pintada de azul, C bolsillo de cartón. ¿Cuáles son distintas?", ["A y B funcionan igual: cambia el color.", "C funciona distinto: lo guarda en un bolsillo."], "A y C son distintas"),
    ],
    mistakes=[
        ("Decir «no sirve» a una idea antes de anotarla.", "Se pierden ideas que podrían servir después.", "Anota todas; elige al final con los criterios."),
        ("Pensar que combinar es copiar un producto igual.", "Combinar es unir partes de varios productos para algo nuevo.", "Escribe qué parte tomas de cada producto."),
    ],
    R=[
        ("Unir una pinza de ropa con una caja ¿es combinar productos o cambiar el color?", "Combinar productos", "Se unen partes de dos productos."),
        ("Al generar ideas, ¿se critican todas de inmediato o se anotan primero?", "Se anotan primero", "La crítica viene después."),
        ("Una pinza que sujeta papeles en la casa sirve en la escuela. ¿Eso es transferir o pintar?", "Transferir", "Se usa la idea en otro lugar."),
    ],
    C=[
        ("¿Por qué conviene anotar de qué producto sale cada parte de una idea?", "Para saber de dónde viene cada parte", "Ayuda a recordar y a conseguir los materiales."),
        ("Ideas: A caja con tapa, B caja con tapa y dibujos. ¿Funcionan de forma distinta?", "No", "Solo cambia la decoración."),
        ("¿Una idea que parece rara se descarta o se anota?", "Se anota", "Puede dar otra idea mejor."),
    ],
    A=[
        ("Problema: llevar 3 lápices en la mochila sin que se quiebren. Tienes un tubo de cartón y una bolsa de tela. Escribe una idea que combine los dos.", "Meter los lápices en el tubo de cartón y guardarlo en la bolsa de tela", "Usa los dos productos."),
        ("Ideas para sostener una hoja: A pinza de ropa, B otra pinza de ropa de distinto color, C bolsillo de cartón. ¿Cuántas ideas distintas hay?", "2", "A y B funcionan igual; C funciona distinto."),
        ("Transfiere: en la cocina un frasco tiene tapa para que no entren moscas. Escribe una idea parecida para tapar un vaso con plantas en la sala.", "Una tapa de cartón sobre el vaso", "La idea de tapar se usa en otro lugar."),
    ],
    Z=[
        ("Tato anota una idea, la critica y la borra. Luego se queda sin ideas. ¿Qué error cometió?", "Criticó antes de anotar todas", "Perdió ideas por criticar demasiado pronto."),
        ("Dos ideas para llevar 3 libros: A asa de cordel sobre una bolsa, B asa de cordel más gruesa en una bolsa. ¿Son ideas realmente distintas? Responde sí o no.", "No", "Las dos son bolsa con asa."),
    ],
    D=[
        ("Reto: cuidar un vaso con una planta que no se tuerza. Anota tres ideas, una de ellas combinando una pinza y un palito de helado.", "Por ejemplo: guiar con palito y pinza; girar el vaso a diario; poner un cartón con luz", "Tres ideas y una usa los dos productos."),
        arith("Anotaste 4 ideas el lunes y 5 el martes. ¿Cuántas ideas tienes en total?", "4+5", "Se suman las ideas de los dos días."),
    ],
    ctx=("Sol quiere que su lonchera no se mueva dentro de la mochila. Tiene un cordel, una caja de cartón con tapa y un trozo de tela. Escribe tres ideas distintas, una combinando dos materiales.", "Atar la lonchera con cordel a la asa de la mochila; meterla en la caja; envolverla en la tela. Una combina cordel y caja", "Tres formas distintas y una combinación."),
    sc=[
        ("¿Qué es combinar productos existentes?", "Unir partes de productos que ya existen", "Así se crea algo nuevo."),
        ("¿Cambiar solo el color da una idea nueva?", "No", "El funcionamiento no cambia."),
        ("¿Cuándo se elige la mejor idea: antes o después de anotarlas todas?", "Después", "Se elige con los criterios."),
    ],
    open_task=(
        "Escoge un problema. Problema 1: guardar 5 lápices en una mesa. Problema 2: sostener 3 hojas para leerlas de pie. Productos: pinza de ropa, caja de cartón, tubo de cartón, cordel. Escribe tres ideas distintas, una que combine dos productos, y dibuja una.",
        "Problema 1: idea 1: tubo parado en caja; idea 2: pinzas en el borde de la caja; idea 3: cordel con clips. Combina tubo y caja.",
        ["escribe tres ideas distintas", "una combina dos productos", "nombra cada idea", "dibuja una"],
        ["tres ideas con nombre y un dibujo"],
        ["ideas iguales con distinto color", "no usar los productos dados"],
        "Pregunta: «¿cómo funciona esta idea comparada con la otra?». Si funcionan igual, pide una forma nueva.",
    ),
    reinforce="Mira dos objetos de tu casa y piensa cómo podrías unirlos para resolver un problema pequeño.",
    extend="Escribe tres ideas para guardar tijeras de punta roma, usando algo que normalmente se bota.",
)

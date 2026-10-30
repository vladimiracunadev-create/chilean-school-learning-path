"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 16 (vocabulario nuevo) y OA 17 (obras literarias escuchadas).

Los cuentos, el poema, la fábula y la leyenda son textos originales escritos para este cuaderno.
"""
from __future__ import annotations

from student_lessons import ex, register

OA16, OA17 = "LE01 OA 16", "LE01 OA 17"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ======================================================================== OA 16
lesson(
    OA16, 1,
    "Cuaderno y lápiz. Las oraciones con palabras nuevas están escritas en los ejercicios.",
    "Aprenderé a descubrir qué significa una palabra nueva mirando las palabras que la rodean. Sirve para entender textos sin quedarme detenido.",
    ["Sé leer oraciones.", "Sé que hay palabras que no conozco."],
    [
        "Cuando encuentras una palabra que no conoces, no te detengas. Mira las otras palabras de la oración, porque suelen dar pistas. Eso se llama contexto. Por ejemplo: «El gato era diminuto: cabía en mi mano». Si cabía en la mano, diminuto significa muy pequeño.",
        "Para descubrir el significado, lee la oración completa, busca pistas, piensa qué podría significar y comprueba si tiene sentido. Una pista puede ser un ejemplo, una explicación o una palabra contraria.",
        "Después de descubrir, usa la palabra en otra oración propia. Así la recuerdas. Si aún no estás seguro, pregunta a un adulto o busca en un diccionario infantil.",
    ],
    [("contexto", "las palabras que rodean a otra y dan pistas"), ("diminuto", "muy pequeño"), ("enorme", "muy grande"), ("pista", "dato que ayuda a descubrir"), ("significado", "lo que quiere decir una palabra")],
    [
        ("Descubrir diminuto", "«El gato era diminuto: cabía en mi mano.» ¿Qué significa diminuto?", ["Pista: cabía en la mano.", "Entonces es muy pequeño."], "Muy pequeño"),
        ("Descubrir exhausto", "«Estoy exhausto: corrí tanto que ya no puedo moverme.» ¿Qué significa exhausto?", ["Pista: corrí tanto, no puedo moverme.", "Está muy cansado."], "Muy cansado"),
    ],
    [
        ("Saltarse la palabra nueva.", "Se piensa que no es importante.", "Mira las pistas de la oración."),
        ("Inventar un significado sin pistas.", "Se adivina.", "Comprueba que tu idea coincida con las pistas."),
    ],
    [
        E("«La casa era enorme: tenía veinte ventanas». ¿Qué significa enorme?", "Muy grande", "Tener veinte ventanas indica gran tamaño."),
        E("«El perro estaba hambriento: no había comido en todo el día». ¿Qué significa hambriento?", "Con mucha hambre", "No haber comido explica el significado."),
        E("«El día estaba soleado: había mucha luz». ¿Qué significa soleado?", "Con sol", "La luz es pista de sol."),
    ],
    [
        E("«Lucas está feliz: sonríe y salta». ¿Qué significa feliz?", "Contento", "Sonreír y saltar muestran alegría."),
        E("«El río es angosto: casi puedo cruzarlo de un salto». ¿Qué significa angosto?", "Poco ancho", "Se cruza de un salto."),
        E("Al descubrir una palabra nueva, ¿qué es el contexto?", "Las palabras que rodean a otra y dan pistas", "Ayuda a entender."),
    ],
    [
        E("«La mochila es liviana: casi no pesa». ¿Qué significa liviana?", "Que pesa poco", "La pista es «casi no pesa»."),
        E("«Mi hermana es muy veloz: corre más rápido que todos». ¿Qué significa veloz?", "Muy rápida", "Corre más rápido."),
        E("Escribe una oración con la palabra diminuto.", "Por ejemplo: La hormiga es diminuta", "Debe usar la palabra correctamente."),
    ],
    [
        E("Pablo leyó «El tigre es feroz: ataca a sus presas». Dijo que feroz significa lindo. ¿Es correcto? Responde sí o no.", "No", "Atacar no es de lindo; es de fuerte y peligroso."),
        E("Ana leyó «El mar estaba sereno: no había olas». ¿Qué significa sereno?", "Tranquilo", "Sin olas, calmo."),
    ],
    [
        E("«Mi abuelo es muy anciano: tiene noventa años». ¿Qué significa anciano?", "Persona muy mayor", "Noventa años es mucha edad."),
        E("«Tomás es valiente: se acercó al perro grande sin miedo». ¿Qué significa valiente?", "Que no tiene miedo ante algo difícil", "Se acercó sin miedo."),
    ],
    [E("En un cuento dice: «La luna iluminaba el camino: se veía todo claro». Tomás no conoce iluminaba. ¿Qué pista le ayuda?", "Se veía todo claro", "Muestra que daba luz.")],
    [
        E("¿Qué haces con una palabra nueva?", "Miro las pistas de la oración", "El contexto ayuda a entender."),
        E("«Diminuto» significa...", "Muy pequeño", "Es lo contrario de enorme."),
        E("¿Qué es el significado?", "Lo que quiere decir una palabra", "Es el sentido de la palabra."),
    ],
    task(
        "Lee esta oración: «El elefante era colosal: sus patas eran más grandes que un árbol». Escribe qué crees que significa colosal, qué pista usaste y una oración tuya con la palabra.",
        "Colosal significa muy grande. La pista fue que sus patas eran más grandes que un árbol. Mi oración: El edificio es colosal.",
        ["dice un significado posible", "indica la pista del texto", "escribe una oración con la palabra"],
        ["tres frases escritas", "explicación oral"],
        ["no usar pista", "oración sin sentido"],
        "Comprueba que tu significado calce con la pista.",
    ),
    "Busca una palabra nueva en un libro y di qué pistas usaste.",
    "Escribe una oración con una palabra nueva y pide a alguien que descubra su significado.",
)

lesson(
    OA16, 2,
    "Cuaderno y lápiz. Las palabras, significados y oraciones están escritos en los ejercicios.",
    "Aprenderé a precisar el significado de una palabra: a distinguir significados parecidos y a elegir el correcto. Sirve para usar las palabras con exactitud.",
    ["Sé buscar pistas en las oraciones.", "Sé qué es un significado."],
    [
        "Muchas palabras tienen un significado parecido a otra. «Grande» y «enorme» son parecidas, pero «enorme» es más grande aún. Para precisar, piensa cuál palabra dice mejor lo que quieres decir.",
        "También hay palabras con más de un significado. «Cola» puede ser la parte de atrás de un animal o una fila de personas esperando. El contexto te dice cuál es: «El perro mueve la cola» es la del animal.",
        "Para precisar un significado, lee la oración, mira las pistas y prueba con cada significado posible. Elige el que tenga sentido con todo lo demás.",
    ],
    [("precisar", "decir con exactitud"), ("sinónimo", "palabra con significado parecido"), ("cola", "parte trasera de un animal o fila de personas"), ("contexto", "palabras que rodean a otra"), ("exacto", "justo, sin errores")],
    [
        ("Elegir significado", "«El perro mueve la cola.» ¿Cola es la parte del animal o una fila?", ["El perro la mueve.", "Los animales tienen cola."], "La parte del animal"),
        ("Elegir palabra", "«La montaña es muy alta, es ___». ¿Cuál sirve más? A) enorme B) diminuta", ["Alta se parece a enorme.", "Diminuta es lo contrario."], "A) enorme"),
    ],
    [
        ("Usar una palabra con significado equivocado.", "Se mezcla con otra parecida.", "Comprueba el contexto antes de elegir."),
        ("Pensar que una palabra sólo tiene un significado.", "Se conoce uno solo.", "Prueba con otros posibles."),
    ],
    [
        E("«Cola» en «Hay mucha cola en la panadería» significa...", "Una fila de personas", "La panadería llena de gente indica fila."),
        E("«Cola» en «El gato mueve la cola» significa...", "La parte trasera del gato", "Un gato la mueve."),
        E("¿«Enorme» es más grande que «grande»? Responde sí o no.", "Sí", "Enorme indica un tamaño mayor."),
    ],
    [
        E("Elige la palabra más exacta: «El bebé es muy pequeño, es ___». A) diminuto B) colosal", "A) diminuto", "Diminuto significa muy pequeño."),
        E("Elige la palabra más exacta: «La ballena es muy grande, es ___». A) diminuta B) enorme", "B) enorme", "Enorme significa muy grande."),
        E("«Veloz» significa...", "Muy rápido", "Es un sinónimo de rápido."),
    ],
    [
        E("Escribe una oración donde «cola» sea una fila de personas.", "Por ejemplo: Hay una cola larga en el cine", "Debe mostrar el significado de fila."),
        E("Escribe una oración donde «cola» sea la de un animal.", "Por ejemplo: El perro mueve la cola", "Debe mostrar el significado de animal."),
        E("Escribe un sinónimo de «contento».", "Por ejemplo: feliz o alegre", "Debe significar lo mismo."),
    ],
    [
        E("Ana dijo «La hormiga es enorme». ¿Es una descripción exacta? Responde sí o no.", "No", "Una hormiga es diminuta, no enorme."),
        E("Beto dijo «El estadio estaba vacío: había mucha gente». ¿Qué contradice su oración?", "Vacío no puede ir con mucha gente", "Las dos partes se contradicen."),
    ],
    [
        E("«La clase está tranquila: nadie habla». ¿Qué palabra se parece a tranquila? A) silenciosa B) ruidosa", "A) silenciosa", "Si nadie habla, está silenciosa."),
        E("Ordena de menor a mayor tamaño: enorme, pequeño, grande. Escribe las palabras.", "pequeño, grande, enorme", "De menos a más tamaño."),
    ],
    [E("En la sala hay un letrero: «Hagan fila en silencio». Rosa dice que fila significa cola de personas. ¿Tiene razón?", "Sí", "Una fila es una hilera de personas esperando.")],
    [
        E("¿Qué es un sinónimo?", "Una palabra con significado parecido", "Dice casi lo mismo."),
        E("¿«Diminuto» y «enorme» significan lo mismo? Responde sí o no.", "No", "Tienen significados opuestos."),
        E("¿Qué ayuda a elegir el significado de «cola»?", "El contexto", "Las palabras que la rodean."),
    ],
    task(
        "Elige una de estas palabras con más de un significado: «cola» (animal o fila). Escribe dos oraciones, una para cada significado, y una tercera donde expliques cuál es cuál con la frase «Aquí significa...».",
        "El perro mueve la cola. Hay una cola larga en la tienda. En la primera, cola significa la parte del animal; en la segunda, significa una fila de personas.",
        ["escribe dos oraciones con significados distintos", "usa la palabra correctamente", "explica con «aquí significa»"],
        ["tres oraciones escritas", "explicación oral"],
        ["usar el mismo significado dos veces", "no explicar"],
        "Lee cada oración y comprueba si cola se entiende como debe.",
    ),
    "Di dos sinónimos de «grande».",
    "Busca con un adulto otra palabra con dos significados y escribe una oración para cada uno.",
)

lesson(
    OA16, 3,
    "Cuaderno, lápiz y hojas pequeñas de papel para hacer tarjetas. Las palabras para guardar están escritas en los ejercicios.",
    "Aprenderé a guardar palabras nuevas en tarjetas con su significado y un ejemplo. Sirve para recordarlas y usarlas después.",
    ["Sé escribir palabras.", "Sé que las palabras tienen significado."],
    [
        "Para recordar una palabra nueva, hazte una tarjeta. En la tarjeta escribes tres cosas: la palabra, qué significa y una oración de ejemplo. Si quieres, agregas un dibujo que te ayude a recordarla.",
        "Por ejemplo, la tarjeta de «diminuto» dice: Palabra: diminuto. Significa: muy pequeño. Ejemplo: La hormiga es diminuta. Con ese dibujo y esa frase la recordarás mejor.",
        "Guarda tus tarjetas en un lugar y repásalas de vez en cuando. Cada vez que uses una palabra nueva al hablar o al escribir, la aprendes un poco mejor y se vuelve parte de tu vocabulario.",
    ],
    [("tarjeta", "papel pequeño donde anoto una palabra nueva"), ("ejemplo", "oración que muestra cómo se usa"), ("repasar", "mirar de nuevo para recordar"), ("dibujo", "imagen que ayuda a recordar"), ("glosario", "lista de palabras con su significado")],
    [
        ("Hacer una tarjeta", "Palabra: veloz. ¿Qué escribes como significado?", ["Veloz es rápido.", "Escribo: muy rápido."], "Muy rápido"),
        ("Ejemplo", "Para la tarjeta de veloz, ¿cuál es un buen ejemplo? A) El leopardo es veloz. B) Veloz mesa.", ["La A es una oración con sentido.", "Muestra cómo se usa."], "A) El leopardo es veloz."),
    ],
    [
        ("Escribir sólo la palabra.", "Se piensa que basta.", "Agrega significado y ejemplo."),
        ("No repasar nunca las tarjetas.", "Se olvidan después.", "Repásalas de vez en cuando."),
    ],
    [
        E("¿Qué tres cosas lleva una tarjeta de palabra nueva?", "Palabra, significado y ejemplo", "Así se recuerda mejor."),
        E("Tarjeta: Palabra: enorme. Significa: muy grande. ¿Qué significa enorme?", "Muy grande", "Está en la tarjeta."),
        E("Tarjeta: Ejemplo: La ballena es enorme. ¿Qué palabra se explica?", "Enorme", "Está en la oración."),
    ],
    [
        E("¿Para qué sirve el ejemplo en la tarjeta?", "Para ver cómo se usa la palabra", "Muestra la palabra en una oración."),
        E("¿Qué es repasar las tarjetas?", "Mirarlas otra vez para recordar", "Ayuda a aprender."),
        E("Tarjeta: Palabra: sereno. Significa: tranquilo. Ejemplo: El mar estaba sereno. ¿Cuál es el ejemplo?", "El mar estaba sereno", "Es la oración de ejemplo."),
    ],
    [
        E("Completa la tarjeta: Palabra: feliz. Significa: ...", "Por ejemplo: contento", "Debe dar un significado correcto."),
        E("Completa la tarjeta: Palabra: diminuto. Ejemplo: ...", "Por ejemplo: La hormiga es diminuta", "Debe usar la palabra en una oración."),
        E("Escribe el significado de «liviano» para una tarjeta.", "Que pesa poco", "Es lo que significa."),
    ],
    [
        E("Una tarjeta dice: Palabra: valiente. Significa: lindo. ¿Está bien? Responde sí o no.", "No", "Valiente significa que no tiene miedo."),
        E("Camila guardó la palabra pero sin significado ni ejemplo. ¿Qué le falta?", "El significado y el ejemplo", "Sin eso no recordará qué quiere decir."),
    ],
    [
        E("Tienes 5 tarjetas y haces 3 más. ¿Cuántas tarjetas tienes?", "8", "5 más 3 es 8."),
        E("Ordena alfabéticamente tres tarjetas: veloz, enorme, diminuto. Escribe las palabras en orden.", "diminuto, enorme, veloz", "d va antes de e y e antes de v."),
    ],
    [E("En un cuento aparece la palabra «asombrado»: «Nico quedó asombrado al ver el arcoíris». Armas una tarjeta. ¿Cuál es el significado? A) muy sorprendido B) muy cansado", "A) muy sorprendido", "Ver un arcoíris produce sorpresa.")],
    [
        E("¿Dónde guardo una palabra nueva?", "En una tarjeta", "Con significado y ejemplo."),
        E("¿Para qué hago un dibujo en la tarjeta?", "Para recordar la palabra", "La imagen ayuda."),
        E("¿Qué hago con mis tarjetas de vez en cuando?", "Las repaso", "Así no las olvido."),
    ],
    task(
        "Haz tres tarjetas con estas palabras: diminuto, enorme, veloz. En cada tarjeta escribe: Palabra, Significa y una oración de Ejemplo. Dibuja algo pequeño que te ayude a recordar.",
        "Palabra: diminuto. Significa: muy pequeño. Ejemplo: La hormiga es diminuta. Palabra: enorme. Significa: muy grande. Ejemplo: La ballena es enorme. Palabra: veloz. Significa: muy rápido. Ejemplo: El guepardo es veloz.",
        ["tres tarjetas", "cada una con palabra, significado y ejemplo", "el significado es correcto"],
        ["tres tarjetas", "lectura oral"],
        ["tarjetas sin ejemplo", "significado equivocado"],
        "Guarda las tarjetas y revísalas mañana para ver cuántas recuerdas.",
    ),
    "Mira tus tarjetas y di el significado de una sin mirarla.",
    "Haz una tarjeta de una palabra nueva de un libro que leas.",
)

lesson(
    OA16, 4,
    "Cuaderno y lápiz. Las oraciones con espacios para completar están escritas en los ejercicios.",
    "Aprenderé a elegir la palabra que mejor encaja en una oración. Sirve para escribir con precisión y sentido.",
    ["Sé el significado de varias palabras nuevas.", "Sé armar oraciones."],
    [
        "No todas las palabras sirven para todas las oraciones. «El día estaba soleado» funciona; «El día estaba diminuto» no tiene sentido. Una palabra pertinente es la que calza con lo que quieres decir.",
        "Para elegir, lee la oración y prueba cada palabra. Pregúntate: ¿tiene sentido?, ¿dice lo que yo quiero decir? Así descartas las que no encajan.",
        "Cuando escribes, usa las palabras nuevas que ya conoces, pero sólo cuando calcen. Es mejor usar bien una palabra sencilla que usar mal una palabra nueva, porque lo más importante es que el lector te entienda sin confundirse.",
    ],
    [("pertinente", "que calza con lo que se quiere decir"), ("encajar", "calzar bien"), ("probar", "intentar cada opción"), ("descartar", "dejar fuera lo que no sirve"), ("sentido", "que se entiende")],
    [
        ("Elegir", "«El cielo estaba ___.» A) estrellado B) diminuto. ¿Cuál encaja?", ["Estrellado describe un cielo.", "Diminuto no calza."], "A) estrellado"),
        ("Descartar", "«La hormiga es ___.» A) enorme B) diminuta. ¿Cuál no calza?", ["Una hormiga es chica.", "Enorme no calza."], "A) enorme no calza"),
    ],
    [
        ("Usar una palabra nueva aunque no calce.", "Se quiere lucir.", "Úsala sólo si tiene sentido."),
        ("No releer la oración completa.", "Se elige apurado.", "Léela con la palabra elegida."),
    ],
    [
        E("«El perro está ___ porque no comió.» A) hambriento B) enorme", "A) hambriento", "No comer causa hambre."),
        E("«La mochila es ___: casi no pesa.» A) liviana B) veloz", "A) liviana", "No pesar es ser liviana."),
        E("«El caracol es ___: avanza muy despacio.» A) lento B) rápido", "A) lento", "Avanzar despacio es ser lento."),
    ],
    [
        E("¿Qué significa pertinente?", "Que calza con lo que quiero decir", "La palabra encaja con el sentido."),
        E("«Mi abuelo está ___ después de caminar mucho.» A) exhausto B) soleado", "A) exhausto", "Después de caminar mucho se está cansado."),
        E("«El mar está ___: no hay olas.» A) sereno B) hambriento", "A) sereno", "Sin olas es tranquilo."),
    ],
    [
        E("Completa con una palabra: «La torta estaba ___.» (por ejemplo, rica)", "Por ejemplo: rica", "La palabra debe describir una torta."),
        E("Completa con «veloz»: «El guepardo es muy ___.»", "veloz", "El guepardo corre rápido."),
        E("Completa con «diminuto»: «La semilla era ___.»", "diminuta", "Una semilla suele ser pequeña."),
    ],
    [
        E("Rosa escribió «El elefante es diminuto». ¿Es pertinente? Responde sí o no.", "No", "Un elefante es grande."),
        E("Luis escribió «El gato es veloz y corre rápido». ¿La palabra veloz calza? Responde sí o no.", "Sí", "Corre rápido es lo que significa veloz."),
    ],
    [
        E("Elige las dos palabras que encajan en «La pelota rueda ___ por la cancha»: A) rápido B) veloz C) diminuto", "A y B", "Son los que describen cómo rueda."),
        E("Corrige: «El sol estaba hambriento.» Escribe una oración correcta con otra palabra.", "Por ejemplo: El sol estaba brillante", "Hambriento no calza con sol."),
    ],
    [E("Escribes una nota: «Hoy mi perro está ___ porque corrió mucho». ¿Qué palabra elegirías? A) exhausto B) soleado", "A) exhausto", "Correr mucho cansa.")],
    [
        E("¿Cómo sé que una palabra calza?", "Porque la oración tiene sentido", "Se lee y se entiende."),
        E("«Veloz» calza en: A) «El auto es veloz.» B) «La mesa es veloz.»", "A) «El auto es veloz.»", "Un auto puede ser rápido."),
        E("Si la palabra no calza, ¿qué hago?", "Elijo otra", "Pruebo hasta que tenga sentido."),
    ],
    task(
        "Completa estas tres oraciones con la palabra que mejor calce y escríbelas completas: A) «Mi hermano está ___ porque no ha comido.» (hambriento / enorme). B) «La ballena es ___.» (enorme / diminuta). C) «Después de correr, estoy ___.» (exhausto / soleado).",
        "A) Mi hermano está hambriento porque no ha comido. B) La ballena es enorme. C) Después de correr, estoy exhausto.",
        ["tres oraciones completas", "las palabras elegidas calzan", "las oraciones tienen sentido"],
        ["tres oraciones escritas", "lectura oral"],
        ["elegir una palabra que no calza", "no escribir la oración completa"],
        "Lee cada oración con la palabra y comprueba que suene bien.",
    ),
    "Di una oración con la palabra «veloz».",
    "Escribe una oración con cada palabra: enorme, diminuto, sereno.",
)

lesson(
    OA16, 5,
    "Cuaderno y lápiz. Los textos con palabras mal usadas están escritos en los ejercicios.",
    "Aprenderé a revisar si usé bien las palabras nuevas en lo que escribo. Sirve para mejorar mis textos y no confundir significados.",
    ["Sé el significado de varias palabras nuevas.", "Sé releer lo que escribo."],
    [
        "Después de escribir, hay que revisar si las palabras nuevas están bien usadas. Para eso lee tu texto y, en cada palabra nueva, pregunta: ¿significa lo que yo quería decir?, ¿encaja con la oración?",
        "Si una palabra no calza, tienes dos opciones: cambiarla por una que sí encaje o cambiar el resto de la oración. Por ejemplo, «El perro es enorme y cabe en mi mano» tiene un problema: enorme y cabe en la mano no combinan. Se arregla con «diminuto».",
        "Revisar con tranquilidad te ayuda a aprender. No es un error equivocarse: es una forma de usar mejor las palabras la próxima vez.",
    ],
    [("revisar", "mirar con atención para mejorar"), ("calzar", "encajar bien"), ("contradicción", "dos cosas que no pueden ser verdad juntas"), ("corregir", "cambiar para mejorar"), ("uso", "forma de emplear una palabra")],
    [
        ("Detectar el error", "«El gato era diminuto y enorme.» ¿Qué falla?", ["Diminuto es muy pequeño.", "Enorme es muy grande; no pueden ir juntas."], "Diminuto y enorme se contradicen"),
        ("Corregir", "«La hormiga es enorme.» ¿Cómo se corrige?", ["Una hormiga es chica.", "Cambio a diminuta."], "La hormiga es diminuta."),
    ],
    [
        ("Usar la palabra sin revisar su significado.", "Se confía en la memoria.", "Pregunta qué significa y compara."),
        ("Borrar la palabra y no escribir otra.", "Se evita el problema.", "Elige otra palabra que calce."),
    ],
    [
        E("«El elefante es diminuto». ¿Está bien usada la palabra?", "No", "Un elefante es grande."),
        E("«La ballena es enorme». ¿Está bien usada la palabra?", "Sí", "Las ballenas son muy grandes."),
        E("«El cuaderno está hambriento». ¿Está bien usada la palabra?", "No", "Los cuadernos no tienen hambre."),
    ],
    [
        E("¿Qué se hace con una palabra mal usada? A) Cambiarla por otra B) Dejarla igual", "A) Cambiarla por otra", "Se mejora el texto."),
        E("«El día está soleado y llueve fuerte». ¿Qué falla?", "Soleado y llueve fuerte se contradicen", "Con sol no suele llover fuerte."),
        E("¿Para qué sirve revisar el uso de las palabras?", "Para saber si dicen lo que quise decir", "Se corrige antes de terminar."),
    ],
    [
        E("Corrige: «El conejo es veloz y camina muy despacio». Escribe una versión sin contradicción.", "El conejo es veloz y corre muy rápido", "Veloz y rápido no se contradicen."),
        E("Corrige: «La mosca es colosal». Escribe una versión correcta.", "La mosca es diminuta", "Una mosca es pequeña."),
        E("Completa con una palabra que calce: «El elefante es ___ y pesa mucho.»", "enorme", "Un elefante es grande."),
    ],
    [
        E("Pablo dice que está bien «La casa es diminuta y tiene diez pisos». ¿Tiene razón?", "No", "Diez pisos no son diminutos."),
        E("Ana revisó su texto y cambió «enorme» por «diminuta» en «La hormiga es enorme». ¿Mejoró? Responde sí o no.", "Sí", "Ahora tiene sentido."),
    ],
    [
        E("Texto: «El elefante es diminuto. Camina despacio. Es muy veloz.» ¿Cuántas palabras mal usadas hay (diminuto, veloz)?", "2", "El elefante no es diminuto ni veloz."),
        E("Revisa: «Nico estaba exhausto después de dormir toda la noche». ¿Qué cambiarías?", "Exhausto por descansado", "Después de dormir no se está cansado."),
    ],
    [E("Escribiste: «Mi abuela es muy veloz porque camina despacio». ¿Qué cambias para que tenga sentido? A) veloz por lenta B) despacio por rápido", "A o B", "Cualquiera de los dos arregla la contradicción.")],
    [
        E("¿Qué se revisa en un texto con palabras nuevas?", "Si calzan con lo que quiero decir", "El uso debe tener sentido."),
        E("«Enorme» y «diminuto» ¿se pueden usar para describir lo mismo? Responde sí o no.", "No", "Tienen significados opuestos."),
        E("Si una palabra no calza, ¿qué hago?", "La cambio por otra", "Así mejora el texto."),
    ],
    task(
        "Revisa este texto y corrige las palabras mal usadas, escribiéndolo de nuevo: «Mi gato es colosal: cabe en mi mano. Es muy veloz porque duerme todo el día. Hoy estaba exhausto después de dormir.»",
        "Mi gato es diminuto: cabe en mi mano. Es muy tranquilo porque duerme todo el día. Hoy estaba descansado después de dormir.",
        ["corrige colosal", "corrige veloz", "corrige exhausto", "el texto queda con sentido"],
        ["texto corregido", "explicación oral"],
        ["dejar contradicciones", "corregir sólo una palabra"],
        "Lee el texto corregido en voz alta: ¿ahora se entiende todo?",
    ),
    "Lee una oración de un libro y di si las palabras nuevas calzan.",
    "Escribe un texto de tres oraciones con dos palabras nuevas y revísalo con un adulto.",
)

# ======================================================================== OA 17
CUENTO_ZORRO = (
    "El zorro y la luna. Una noche, un zorro vio la luna reflejada en un charco. Pensó que era un queso redondo y brillante. "
    "Saltó para atraparla y cayó en el agua fría. Salió mojado y tiritando. La luna seguía en el cielo, tranquila. "
    "Desde esa noche, el zorro miró dos veces antes de saltar."
)

lesson(
    OA17, 1,
    "Un adulto que lea en voz alta el cuento escrito en los ejercicios; tú sólo escuchas y respondes. Cuaderno y lápiz.",
    "Aprenderé a prepararme antes de escuchar una obra: pensar en el título y en lo que imagino. Sirve para escuchar con atención y entender mejor.",
    ["Sé escuchar sin interrumpir.", "Sé qué es un cuento."],
    [
        "Antes de escuchar un cuento, un poema o una leyenda, conviene prepararse. Mira el título y piensa: ¿de qué podrá tratar?, ¿quién será el personaje?, ¿qué podría pasar? Eso se llama predecir.",
        "Cuando el adulto lee, escucha con atención, imagina lo que oyes y guarda tus dudas para el final. Al terminar, compara lo que pensabas con lo que pasó en la obra. Ver diferencias también es parte de aprender.",
        "Las obras tienen un comienzo, un desarrollo y un final. Prestar atención a esas partes te ayuda a entender qué pasó y en qué orden. Si te distraes, pide con respeto que repitan un fragmento.",
    ],
    [("predecir", "pensar qué pasará o de qué tratará"), ("título", "nombre de la obra"), ("personaje", "quien vive la historia"), ("comienzo", "la primera parte"), ("final", "la última parte")],
    [
        ("Predecir", "El título es «El zorro y la luna». ¿De qué crees que trata?", ["El título nombra un zorro y la luna.", "Quizá el zorro quiere algo de la luna."], "De un zorro y la luna"),
        ("Comprobar", f"Escucha: {CUENTO_ZORRO} ¿Qué pensó el zorro que era la luna reflejada?", ["Busco qué creyó el zorro.", "Un queso redondo y brillante."], "Un queso redondo y brillante"),
    ],
    [
        ("Hablar mientras se lee.", "Hay ganas de comentar.", "Espera al final."),
        ("Pensar que mi predicción debe ser igual.", "Se cree que equivocarse es malo.", "Compara y aprende."),
    ],
    [
        E(f"Escucha: {CUENTO_ZORRO} ¿Quién es el personaje principal?", "El zorro", "Es quien actúa en el cuento."),
        E(f"Escucha: {CUENTO_ZORRO} ¿Dónde vio la luna reflejada?", "En un charco", "El cuento lo dice."),
        E("¿Qué se hace antes de escuchar una obra? A) Predecir con el título B) Dormir", "A) Predecir con el título", "Prepara la atención."),
    ],
    [
        E(f"Escucha: {CUENTO_ZORRO} ¿Qué pasó cuando el zorro saltó?", "Cayó en el agua fría", "Lo cuenta el desarrollo."),
        E(f"Escucha: {CUENTO_ZORRO} ¿Qué hizo el zorro desde esa noche?", "Miró dos veces antes de saltar", "Es el final del cuento."),
        E("¿Qué es predecir?", "Pensar de qué tratará o qué pasará", "Se hace con el título y las pistas."),
    ],
    [
        E("Un cuento se llama «El oso y la miel». ¿De qué crees que trata?", "De un oso que quiere miel", "El título nombra al oso y la miel."),
        E("Un poema se llama «La lluvia». ¿Qué crees que describe?", "La lluvia", "El título nombra el tema."),
        E("Un cuento se llama «El pez que no sabía nadar». ¿Quién será el personaje?", "Un pez", "El título lo nombra."),
    ],
    [
        E(f"Escucha: {CUENTO_ZORRO} Ana pensó que el zorro atraparía la luna. ¿Pasó eso? Responde sí o no.", "No", "El zorro cayó al charco; la luna siguió en el cielo."),
        E(f"Escucha: {CUENTO_ZORRO} ¿Por qué el zorro saltó?", "Porque creyó que la luna era un queso", "Confundió el reflejo."),
    ],
    [
        E(f"Escucha: {CUENTO_ZORRO} Ordena: a) Cayó al agua. b) Vio la luna en el charco. c) Miró dos veces antes de saltar. Escribe las letras en orden.", "b, a, c", "Es el orden en que pasó."),
        E(f"Escucha: {CUENTO_ZORRO} ¿Qué aprendió el zorro?", "A mirar bien antes de actuar", "Miró dos veces antes de saltar."),
    ],
    [E("Antes de la hora del cuento la profesora anuncia «El loro que cantaba». Tomás dice que habrá un loro cantor. ¿Qué hizo Tomás? A) Predecir B) Interrumpir", "A) Predecir", "Pensó en el cuento con el título.")],
    [
        E("¿Qué hago mientras el adulto lee?", "Escucho en silencio", "Así entiendo el cuento."),
        E("¿Cómo se llama el nombre de una obra?", "Título", "Dice cómo se llama."),
        E("¿Qué hago al final con mis dudas?", "Las pregunto", "Se aclara al terminar."),
    ],
    task(
        "Pide a un adulto que lea el cuento «El zorro y la luna» que está en esta clase. Antes de que empiece, escribe qué crees que pasará (Predicción). Después de escuchar, escribe si tu predicción fue correcta y qué ocurrió realmente (Comprobación). Usa «Yo pensé que... y pasó que...».",
        "Yo pensé que el zorro iba a atrapar la luna y pasó que cayó al agua.",
        ["escribe la predicción antes", "compara con el cuento", "usa «Yo pensé que... y pasó que...»"],
        ["frase escrita", "conversación oral"],
        ["escribir la predicción después de oír", "no comparar"],
        "Pregunta a un adulto qué le sorprendió a él del cuento.",
    ),
    "Cuenta con tus palabras el cuento del zorro.",
    "Escribe una predicción para el título «El oso y la miel» y compárala con lo que imaginas luego.",
)

CUENTO_NINA = (
    "La niña y el pajarito. Primero, Lila encontró un pajarito en el patio. Tenía el ala doblada y no podía volar. "
    "Después, Lila lo puso en una caja con hojas suaves y le dio agua. Al final, el pajarito se mejoró y voló hacia el árbol."
)

lesson(
    OA17, 2,
    "Un adulto que lea en voz alta el cuento escrito en los ejercicios. Cuaderno y lápiz.",
    "Aprenderé a seguir a los personajes y los episodios de una obra. Sirve para entender qué pasa y en qué orden.",
    ["Sé escuchar una historia.", "Sé que los cuentos tienen personajes."],
    [
        "Un cuento tiene personajes, que son quienes viven la historia, y episodios, que son las partes en que pasa algo. Para seguirlos, fíjate en quién actúa, qué hace y qué cambia. Palabras como «primero», «después» y «al final» te ayudan.",
        "Cada episodio tiene una acción importante. En el cuento de Lila, primero encuentra al pajarito, después lo cuida y al final el pajarito vuela. Si ordenas esos episodios, entiendes toda la historia.",
        "También puedes pensar en cómo son los personajes y por qué actúan así. Lila es cuidadosa porque ayuda al pajarito. Los gestos y las acciones muestran cómo es cada personaje.",
    ],
    [("personaje", "quien vive la historia"), ("episodio", "parte de la historia donde pasa algo"), ("orden", "secuencia de los hechos"), ("cambio", "lo que se transforma en la historia"), ("cuidadosa", "que trata con cariño a otros")],
    [
        ("Primer episodio", f"Escucha: {CUENTO_NINA} ¿Qué encontró Lila?", ["Busco primero.", "Un pajarito."], "Un pajarito"),
        ("Último episodio", f"Escucha: {CUENTO_NINA} ¿Qué pasó al final?", ["Busco al final.", "El pajarito voló hacia el árbol."], "El pajarito se mejoró y voló al árbol"),
    ],
    [
        ("Mezclar el orden de los episodios.", "Se recuerda al azar.", "Usa primero, después y al final."),
        ("Olvidar a un personaje.", "Se mira sólo lo principal.", "Pregunta quién actúa en cada parte."),
    ],
    [
        E(f"Escucha: {CUENTO_NINA} ¿Dónde encontró Lila al pajarito?", "En el patio", "El primer episodio lo dice."),
        E(f"Escucha: {CUENTO_NINA} ¿Qué tenía el pajarito?", "El ala doblada", "Por eso no podía volar."),
        E(f"Escucha: {CUENTO_NINA} ¿Dónde puso Lila al pajarito?", "En una caja con hojas suaves", "El segundo episodio lo cuenta."),
    ],
    [
        E(f"Escucha: {CUENTO_NINA} ¿Qué hizo Lila para cuidar al pajarito además de la caja?", "Le dio agua", "Es parte del segundo episodio."),
        E(f"Escucha: {CUENTO_NINA} ¿Cuántos episodios hay (primero, después, al final)?", "3", "El cuento tiene tres partes."),
        E("¿Qué es un episodio?", "Una parte de la historia donde pasa algo", "La historia se arma con ellos."),
    ],
    [
        E(f"Escucha: {CUENTO_NINA} Ordena: a) El pajarito voló. b) Lila encontró un pajarito. c) Lila lo puso en una caja. Escribe las letras en orden.", "b, c, a", "Es el orden en que pasó."),
        E(f"Escucha: {CUENTO_NINA} ¿Quiénes son los personajes?", "Lila y el pajarito", "Ambos son quienes actúan."),
        E(f"Escucha: {CUENTO_NINA} Completa: «Lila era una niña ___ porque ayudó al pajarito».", "cuidadosa", "Cuidó al pajarito con cariño."),
    ],
    [
        E(f"Escucha: {CUENTO_NINA} ¿Cómo cambió el pajarito de principio a fin?", "Primero no podía volar y al final voló", "Se mejoró de su ala."),
        E(f"Escucha: {CUENTO_NINA} Pedro dice que Lila no ayudó al pajarito. ¿Qué parte del cuento muestra que se equivoca?", "Cuando lo puso en la caja y le dio agua", "Eso es ayudar."),
    ],
    [
        E("Cuento corto: Primero, Beto perdió su pelota. Después, la buscó con su hermana. Al final, la encontró bajo la silla. ¿Quién ayudó a Beto?", "Su hermana", "El episodio dos lo dice."),
        E("En el cuento de Beto, ¿dónde estaba la pelota?", "Bajo la silla", "El final lo cuenta."),
    ],
    [E("En clases la profesora lee el cuento de Lila y pregunta cuál fue el segundo episodio. ¿Cuál es? A) Lila cuidó al pajarito B) El pajarito voló", "A) Lila cuidó al pajarito", "Después de encontrarlo lo cuida.")],
    [
        E("¿Quién vive la historia?", "El personaje", "Es quien actúa."),
        E("¿Qué palabra marca el último episodio?", "Al final", "Cierra la historia."),
        E("¿Cómo sé cómo es un personaje?", "Por lo que hace", "Sus acciones lo muestran."),
    ],
    task(
        "Pide a un adulto que lea el cuento de Lila. Luego cuéntalo con tus palabras en tres frases: «Primero...», «Después...», «Al final...». Dibuja un episodio. Pauta de oralidad: hablo claro, sigo el orden y nombro a los personajes.",
        "Primero Lila encontró un pajarito con el ala doblada. Después lo puso en una caja y le dio agua. Al final el pajarito voló al árbol.",
        ["tres frases con primero, después y al final", "respeta el orden", "nombra a los personajes"],
        ["relato oral", "dibujo o frases escritas"],
        ["desordenar los episodios", "no nombrar a Lila"],
        "Pregunta a quien escuchó si entendió qué pasó en cada parte.",
    ),
    "Cuenta con tus palabras el cuento de Beto y la pelota.",
    "Inventa un cuarto episodio para el cuento de Lila.",
)

POEMA = (
    "Lluvia de abril. Gota, gota, gota, cae la lluvia de abril. "
    "Toca el techo, toca el patio, toca el suelo y la hoja gris. "
    "La lluvia es una música que viene desde el cielo hasta mí."
)

lesson(
    OA17, 3,
    "Un adulto que lea en voz alta el poema escrito en los ejercicios. Cuaderno y lápiz.",
    "Aprenderé a escuchar el lenguaje de los poemas: rimas, repeticiones y comparaciones. Sirve para disfrutar cómo suena y qué imagina un poema.",
    ["Sé escuchar rimas.", "Sé qué es una palabra."],
    [
        "Los poemas usan las palabras de forma especial. Pueden tener rimas, que son palabras que terminan con sonidos parecidos, como «abril» y «mí». También repiten palabras, como «gota, gota, gota», para que suene como si cayera la lluvia.",
        "Otra forma es la comparación. «La lluvia es una música» dice que la lluvia se parece a la música porque ambas suenan. Con comparaciones, el poeta nos hace imaginar cosas de manera nueva.",
        "Al escuchar un poema, no hace falta entender cada palabra. Puedes cerrar los ojos, imaginar lo que oyes y disfrutar el sonido. Después puedes comentar qué te hizo sentir o qué imagen te vino a la mente.",
    ],
    [("poema", "texto con ritmo, rimas e imágenes"), ("rima", "palabras con final parecido"), ("repetición", "decir lo mismo varias veces"), ("comparación", "decir que algo se parece a otra cosa"), ("imagen", "lo que imagino al escuchar")],
    [
        ("Encontrar rima", f"Escucha: {POEMA} ¿Con qué palabra rima «abril»?", ["Busco finales parecidos.", "«abril» termina como «gris»... y también como «mí»."], "Con «gris» o «mí»"),
        ("Comparación", f"Escucha: {POEMA} ¿Con qué compara el poeta la lluvia?", ["Busco «es una».", "La lluvia es una música."], "Con una música"),
    ],
    [
        ("Querer entender cada palabra.", "Se cree que hay que explicar todo.", "Disfruta el sonido y la imagen."),
        ("Pensar que los poemas son iguales a los cuentos.", "Se busca una historia.", "Escucha ritmo, rima e imágenes."),
    ],
    [
        E(f"Escucha: {POEMA} ¿Qué palabra se repite al comienzo?", "Gota", "El poema repite «gota»."),
        E(f"Escucha: {POEMA} ¿De qué mes habla el poema?", "Abril", "El título y el primer verso lo dicen."),
        E(f"Escucha: {POEMA} ¿Qué toca la lluvia en el segundo verso?", "El techo, el patio, el suelo y la hoja gris", "El poema lo enumera."),
    ],
    [
        E("Al escuchar «Lluvia de abril», ¿qué es una rima?", "Palabras con final parecido", "Suenan casi igual al terminar."),
        E("¿Rima «casa» con «masa»? Responde sí o no.", "Sí", "Terminan con el mismo sonido «asa»."),
        E(f"Escucha: {POEMA} ¿Qué sonido imita la repetición de «gota, gota»?", "El caer de la lluvia", "Suena como las gotas."),
    ],
    [
        E("Rima con «sol»: A) farol B) luna", "A) farol", "Sol y farol terminan igual."),
        E("Rima con «mar»: A) cantar B) nube", "A) cantar", "Mar y cantar terminan en «ar»."),
        E("Completa con una rima de «luna»: «Brilla la luna / en la ___.» (por ejemplo, laguna)", "Por ejemplo: laguna", "Debe terminar parecido a luna."),
    ],
    [
        E(f"Escucha: {POEMA} ¿Por qué el poema compara la lluvia con la música?", "Porque la lluvia también suena", "Ambas tienen sonido."),
        E("«El viento es un caballo veloz». ¿Qué compara?", "El viento con un caballo", "Dice que se parecen."),
    ],
    [
        E("Escribe una comparación sobre el sol, como «El sol es una naranja grande».", "Por ejemplo: El sol es una naranja grande", "Debe decir que se parece a otra cosa."),
        E("Escribe una frase con repetición, como «tic, tic, tic» para la lluvia o el reloj.", "Por ejemplo: Tic, tic, tic suena el reloj", "Debe repetir una palabra o sonido."),
    ],
    [E("En clases la profesora lee un poema que dice «La luna es una moneda de plata». Un niño dice que la luna es de verdad una moneda. ¿Tiene razón? Responde sí o no.", "No", "Es una comparación; la luna se parece a una moneda brillante.")],
    [
        E("¿Qué se escucha en un poema además de lo que dice?", "El ritmo y las rimas", "Dan música al texto."),
        E("¿Cómo se llama repetir una palabra varias veces?", "Repetición", "Se hace para dar ritmo."),
        E("¿Para qué sirve una comparación?", "Para imaginar algo de forma nueva", "Compara dos cosas."),
    ],
    task(
        "Pide a un adulto que lea el poema «Lluvia de abril». Luego di cuál palabra se repite, con qué compara la lluvia y escribe un verso tuyo de dos líneas sobre la lluvia que tenga una rima (por ejemplo, techo / hecho o gota / nota).",
        "Se repite gota. Compara la lluvia con una música. Mi verso: La lluvia cae en la hoja, / y su música me moja.",
        ["nombra la repetición", "nombra la comparación", "escribe un verso con rima"],
        ["respuestas orales", "verso escrito"],
        ["no reconocer la comparación", "verso sin rima"],
        "Lee tu verso en voz alta y comprueba que las palabras finales suenen parecido.",
    ),
    "Di en voz alta dos palabras que rimen con «sol».",
    "Escribe un poema de cuatro líneas sobre el sol con una rima.",
)

FABULA = (
    "La liebre y la tortuga. Una liebre se burlaba de una tortuga porque caminaba lento. "
    "La tortuga dijo: «Hagamos una carrera». La liebre aceptó y salió corriendo. A mitad de camino se echó a dormir. "
    "La tortuga siguió despacio, sin parar, y llegó primero. Moraleja: la constancia vence a la burla."
)
LEYENDA = (
    "La piedra que cantaba. Cuentan que en un cerro había una piedra redonda. Cuando soplaba el viento, la piedra sonaba como una flauta. "
    "Los niños subían a escucharla. Decían que era un regalo del cerro para quienes lo cuidaban. Hasta hoy, algunos dicen que se oye en las tardes de viento."
)

lesson(
    OA17, 4,
    "Un adulto que lea en voz alta la fábula y la leyenda escritas en los ejercicios (son textos originales). Cuaderno y lápiz.",
    "Aprenderé a comparar géneros: cuento, fábula, poema y leyenda. Sirve para saber qué esperar de cada obra y disfrutarla mejor.",
    ["Sé escuchar cuentos.", "Sé qué es un personaje."],
    [
        "Cada género tiene sus rasgos. El cuento narra una historia inventada. La fábula es una historia corta con animales que actúan como personas y termina con una enseñanza llamada moraleja. El poema usa rimas y comparaciones. La leyenda explica un lugar o un misterio y suele decir «cuentan que».",
        "Para reconocer el género, pregúntate: ¿hay animales que hablan y una enseñanza? Es fábula. ¿Hay rimas e imágenes? Es poema. ¿Se explica el origen de algo del lugar? Es leyenda. ¿Es una historia con personajes y episodios? Es cuento.",
        "Comparar géneros te ayuda a entender para qué se escribió cada uno. La fábula enseña, el poema hace sentir, la leyenda explica un misterio y el cuento entretiene con una historia.",
    ],
    [("fábula", "historia corta con animales y una enseñanza"), ("moraleja", "enseñanza final de una fábula"), ("leyenda", "relato que explica un lugar o un misterio"), ("género", "tipo de obra"), ("constancia", "seguir intentando sin rendirse")],
    [
        ("Reconocer fábula", f"Escucha: {FABULA} ¿Qué género es?", ["Hay animales que hablan.", "Termina con una moraleja."], "Es una fábula"),
        ("Reconocer leyenda", f"Escucha: {LEYENDA} ¿Qué género es?", ["Dice «cuentan que».", "Explica algo misterioso de un cerro."], "Es una leyenda"),
    ],
    [
        ("Pensar que todos los géneros son lo mismo.", "Se escucha sin comparar.", "Busca los rasgos de cada uno."),
        ("Creer que la leyenda es un dato científico.", "Se confunde con un artículo.", "La leyenda es un relato que explica de forma imaginaria."),
    ],
    [
        E(f"Escucha: {FABULA} ¿Quiénes son los personajes?", "Una liebre y una tortuga", "Son los animales de la fábula."),
        E(f"Escucha: {FABULA} ¿Quién llegó primero?", "La tortuga", "Siguió sin parar."),
        E(f"Escucha: {LEYENDA} ¿Qué había en el cerro?", "Una piedra redonda", "Es el elemento de la leyenda."),
    ],
    [
        E(f"Escucha: {FABULA} ¿Cuál es la moraleja?", "La constancia vence a la burla", "Es la enseñanza final."),
        E(f"Escucha: {LEYENDA} ¿Cuándo suena la piedra?", "Cuando sopla el viento", "El texto lo dice."),
        E("¿Qué es una moraleja?", "La enseñanza final de una fábula", "Cierra la historia con un mensaje."),
    ],
    [
        E(f"Escucha: {FABULA} ¿Qué hizo la liebre a mitad de camino?", "Se echó a dormir", "Por eso perdió."),
        E(f"Escucha: {LEYENDA} ¿Qué decían los niños de la piedra?", "Que era un regalo del cerro", "El texto lo cuenta."),
        E("Un texto dice: «Gota, gota, gota, cae la lluvia de abril». ¿Qué género es: poema o fábula?", "Poema", "Tiene repetición y ritmo."),
    ],
    [
        E("Comparando la fábula y la leyenda: ¿cuál termina con una moraleja?", "La fábula", "La leyenda no tiene moraleja."),
        E("¿Qué género usa animales que actúan como personas para enseñar?", "La fábula", "Es su rasgo principal."),
    ],
    [
        E("Une: A) fábula B) poema C) leyenda con 1) rimas e imágenes 2) animales y moraleja 3) explica un lugar misterioso. Escribe las parejas.", "A-2, B-1, C-3", "Cada género tiene su rasgo."),
        E("Escribe en una oración en qué se parecen la fábula y el cuento.", "Por ejemplo: Los dos cuentan una historia con personajes", "Ambos narran una historia."),
    ],
    [E("Una niña escuchó «Cuentan que en la laguna vive una luz azul que guía a los pescadores». ¿Qué género es: fábula o leyenda?", "Leyenda", "«Cuentan que» y un misterio del lugar son rasgos de la leyenda.")],
    [
        E("¿Qué género tiene moraleja?", "La fábula", "Termina con una enseñanza."),
        E("¿Qué género explica un lugar o un misterio?", "La leyenda", "Cuenta un relato sobre el origen."),
        E("¿Qué tiene el poema?", "Rimas, ritmo e imágenes", "Su sonido es especial."),
    ],
    task(
        "Pide a un adulto que lea la fábula «La liebre y la tortuga» y la leyenda «La piedra que cantaba». Escribe dos frases: «La fábula enseña que...» y «La leyenda cuenta que...».",
        "La fábula enseña que la constancia vence a la burla. La leyenda cuenta que una piedra sonaba como flauta cuando soplaba el viento.",
        ["completa las dos frases", "usa datos de cada obra", "distingue los géneros"],
        ["dos frases escritas", "comparación oral"],
        ["mezclar los datos de las obras", "no usar las frases pedidas"],
        "Vuelve a pedir que te lean la parte final de la fábula para comprobar su enseñanza.",
    ),
    "Di en voz alta un rasgo de la fábula y uno de la leyenda.",
    "Inventa una moraleja corta para la historia de un perro que ayuda a un gato.",
)

lesson(
    OA17, 5,
    "Un adulto que lea en voz alta los textos escritos en los ejercicios. Cuaderno y lápiz.",
    "Aprenderé a conversar después de escuchar una obra: contar lo que pasó, dar mi opinión y decir qué sentí. Sirve para compartir lo que entendí con otros.",
    ["Sé escuchar una obra completa.", "Sé esperar mi turno."],
    [
        "Después de escuchar una obra, conversamos. Primero, contamos qué pasó con nuestras palabras. Luego decimos qué nos gustó y por qué. Por último, comentamos qué sentimos: alegría, miedo, pena o sorpresa.",
        "Para conversar bien, cada uno habla en su turno, mira a quien habla y responde a lo que dijo el otro. Puedes decir «Yo pensé lo mismo porque...» o «Yo pensé distinto porque...». Así se respeta lo que dice cada uno.",
        "Contar con tus palabras una obra no es repetirla igual. Es decir lo importante: quiénes son los personajes, qué les pasa y cómo termina. Si algo no lo entendiste, pregunta.",
    ],
    [("conversar", "hablar y escuchar entre varios"), ("opinar", "decir lo que pienso"), ("sentir", "tener una emoción"), ("recontar", "contar con mis palabras"), ("turno", "momento de hablar")],
    [
        ("Recontar", f"Escucha: {CUENTO_ZORRO} ¿Cómo lo cuentas en una oración?", ["Digo quién, qué hizo y cómo terminó.", "Un zorro saltó a un charco creyendo que la luna era queso."], "Un zorro saltó a un charco porque creyó que la luna era queso y aprendió a mirar dos veces"),
        ("Opinar", "Ana dice: «Me gustó porque el zorro aprendió una lección». ¿Cuál es su razón?", ["Busco después de «porque».", "El zorro aprendió una lección."], "Que el zorro aprendió una lección"),
    ],
    [
        ("Repetir palabra por palabra.", "Se cree que recontar es repetir.", "Cuenta lo importante con tus palabras."),
        ("Decir «me gustó» sin razón.", "No se piensa por qué.", "Usa «porque» y una parte del texto."),
    ],
    [
        E(f"Escucha: {CUENTO_ZORRO} ¿Cómo terminó el cuento?", "El zorro miró dos veces antes de saltar", "Es el final."),
        E("Mía dice: «Sentí pena cuando el zorro cayó al agua». ¿Qué sintió?", "Pena", "Lo dice en su comentario."),
        E("¿Qué se hace cuando otro habla?", "Escucharlo y esperar mi turno", "Es parte de conversar."),
    ],
    [
        E(f"Escucha: {CUENTO_NINA} ¿Cómo recuentas el cuento en una oración?", "Lila encontró un pajarito herido, lo cuidó y voló", "Resume los tres episodios."),
        E("Beto dijo: «Me gustó el poema porque suena como la lluvia». ¿Cuál es su razón?", "Que suena como la lluvia", "Está después de «porque»."),
        E("¿Qué frase respeta al compañero? A) «Yo pensé distinto porque...» B) «Eso está mal»", "A) «Yo pensé distinto porque...»", "Es respetuosa y da una razón."),
    ],
    [
        E(f"Escucha: {FABULA} Completa: «Me gustó esta fábula porque...»", "Por ejemplo: la tortuga ganó sin rendirse", "Debe dar una razón basada en la fábula."),
        E(f"Escucha: {LEYENDA} Escribe una pregunta que le harías a un compañero sobre esta leyenda.", "Por ejemplo: ¿Qué sonaba como una flauta?", "Es una pregunta sobre la leyenda."),
        E("Escribe una frase sobre qué sentiste al oír el cuento del zorro.", "Por ejemplo: Sentí risa cuando el zorro saltó al charco", "Debe nombrar un sentimiento."),
    ],
    [
        E("Dos niños recuentan el cuento del zorro. Iván: «Un zorro saltó a un charco, pensó que la luna era queso y se mojó». Paula: «Había un zorro». ¿Quién lo recuenta mejor?", "Iván", "Dice más de lo importante."),
        E("Pablo dice que le gustó la leyenda sin dar razón. ¿Qué le falta?", "Decir por qué le gustó", "Una razón ayuda a que lo entiendan."),
    ],
    [
        E("Pauta de oralidad: miro a quien habla, espero mi turno, hablo claro. Si cumples las tres, ¿cuántos puntos sumas?", "3", "Son tres acciones."),
        E(f"Escucha: {FABULA} Un compañero dice que la liebre ganó. Responde con respeto usando «Yo pensé distinto porque...».", "Por ejemplo: Yo pensé distinto porque la tortuga llegó primero", "Debe usar la frase y dar la razón del texto."),
    ],
    [E("En clases conversan sobre el cuento del zorro. Tomás quiere contar lo suyo sin esperar su turno. ¿Qué debe hacer? A) Levantar la mano B) Hablar fuerte", "A) Levantar la mano", "Así respeta el turno.")],
    [
        E("¿Qué es recontar?", "Contar con mis palabras lo que escuché", "No es repetir igual."),
        E("¿Qué palabra uso para dar la razón?", "Porque", "Une mi opinión con la razón."),
        E("¿Qué hago si algo no entendí?", "Pregunto", "Aclaro mi duda."),
    ],
    task(
        "Pide a un adulto que lea el cuento de Lila o la fábula de la liebre y la tortuga. Luego, conversen: cuéntale con tus palabras qué pasó, di si te gustó y por qué («Me gustó porque...»), y di qué sentiste. Pauta de oralidad: hablo claro, espero mi turno, miro a quien me escucha.",
        "En el cuento de Lila, una niña ayudó a un pajarito herido. Me gustó porque Lila lo cuidó con cariño. Sentí alegría cuando voló.",
        ["cuenta qué pasó", "opina con «Me gustó porque...»", "dice un sentimiento", "cumple la pauta de oralidad"],
        ["conversación con un adulto", "frases escritas"],
        ["repetir palabra por palabra", "no dar razón", "no decir qué sintió"],
        "Pide al adulto que te diga qué parte de tu conversación le gustó más.",
    ),
    "Cuenta con tus palabras el poema «Lluvia de abril».",
    "Conversa con un familiar sobre el cuento de la niña y el pajarito y pregunta qué sintió.",
)

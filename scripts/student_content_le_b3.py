"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 14 (oraciones completas) y OA 15 (letra legible y espacios)."""
from __future__ import annotations

from student_lessons import ex, register

OA14, OA15 = "LE01 OA 14", "LE01 OA 15"
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


# ======================================================================== OA 14
lesson(
    OA14, 1,
    "Cuaderno y lápiz. Las frases están escritas en los ejercicios.",
    "Aprenderé que una oración dice algo completo: tiene sentido, empieza con mayúscula y termina con punto. Sirve para que otros entiendan mi mensaje.",
    ["Sé escribir palabras.", "Sé qué es una letra mayúscula."],
    [
        "Una oración es un grupo de palabras que dice algo completo. «El perro duerme» es una oración porque nos cuenta quién hace algo y qué hace. «El perro» no es una oración, porque nos quedamos esperando que diga qué pasa.",
        "Al escribir una oración, empieza con letra mayúscula y termina con punto. «La niña canta.» tiene esa forma. Las palabras van en un orden que se entiende.",
        "Para comprobar si una oración está completa, léela en voz alta y pregúntate: ¿se entiende sola?, ¿me deja esperando más palabras? Si te quedas esperando, falta algo.",
    ],
    [("oración", "palabras que dicen algo completo"), ("mayúscula", "letra grande con que empieza la oración"), ("punto", "signo que se pone al terminar"), ("completa", "que no le falta nada para entenderse"), ("sentido", "que se entiende")],
    [
        ("Oración o no", "«El perro duerme.» ¿Es una oración completa?", ["Dice quién: el perro.", "Dice qué hace: duerme."], "Sí, es una oración completa"),
        ("Falta algo", "«La niña.» ¿Es una oración completa?", ["Dice quién, pero no qué hace.", "Me quedo esperando."], "No, falta decir qué hace"),
    ],
    [
        ("Escribir sólo una palabra suelta.", "Se cree que alcanza.", "Agrega qué pasa o qué hace."),
        ("Olvidar la mayúscula y el punto.", "Se escribe apurado.", "Empieza con mayúscula y termina con punto."),
    ],
    [
        E("¿«El gato come.» es una oración completa?", "Sí", "Dice quién y qué hace."),
        E("¿«Mi mamá.» es una oración completa?", "No", "No dice qué hace o qué pasa."),
        E("¿Con qué empieza una oración?", "Con mayúscula", "La primera letra se escribe grande."),
    ],
    [
        E("¿«Corre rápido el.» está bien ordenada?", "No", "Las palabras no están en un orden que se entienda."),
        E("Al escribir «El gato come.», ¿con qué signo termina la oración?", "Con punto", "El punto marca el final."),
        E("¿«Sol brilla el.» tiene sentido?", "No", "Las palabras están desordenadas."),
    ],
    [
        E("Ordena para formar una oración: «canta / niña / la».", "La niña canta.", "Primero va el artículo, luego quién y qué hace."),
        E("Completa la oración: «El pájaro ...» (dice qué hace).", "Por ejemplo: El pájaro vuela.", "Debe agregar una acción."),
        E("Escribe una oración con la palabra «luna».", "Por ejemplo: La luna brilla.", "Debe tener sentido completo."),
    ],
    [
        E("Mía escribió «Mi perro grande». ¿Está completa? Responde sí o no.", "No", "Falta decir qué hace o cómo es."),
        E("Beto escribió «la ardilla sube» sin mayúscula ni punto. ¿Qué le falta?", "Mayúscula al inicio y punto al final", "Es una oración pero mal escrita."),
    ],
    [
        E("Corrige: «ayer comí una manzana». Escribe la oración bien escrita.", "Ayer comí una manzana.", "Se agrega mayúscula y punto."),
        E("¿Cuál de estas está completa? A) «Tomás y su mamá» B) «Tomás y su mamá van al parque.»", "B) «Tomás y su mamá van al parque.»", "La B dice qué hacen."),
    ],
    [E("Quieres decirle a tu hermano que el pan está listo. ¿Cuál es una oración completa? A) «El pan» B) «El pan está listo.»", "B) «El pan está listo.»", "Dice algo completo.")],
    [
        E("Según esta clase, ¿qué es una oración completa?", "Palabras que dicen algo completo", "Se entiende sola."),
        E("¿«El conejo salta.» es oración?", "Sí", "Tiene quién y qué hace."),
        E("¿Qué letra va al inicio de una oración?", "Una mayúscula", "Marca el comienzo."),
    ],
    task(
        "Escribe tres oraciones completas sobre estos dibujos descritos: A) un niño que come una manzana, B) una niña que lee un libro, C) un perro que corre en el parque. Cada una con mayúscula y punto.",
        "El niño come una manzana. La niña lee un libro. El perro corre en el parque.",
        ["tres oraciones", "cada una con quién y qué hace", "mayúscula y punto"],
        ["tres oraciones en el cuaderno", "lectura en voz alta"],
        ["escribir sólo palabras sueltas", "olvidar mayúscula o punto"],
        "Lee cada oración en voz alta: si te quedas esperando más palabras, agrega lo que falta.",
    ),
    "Lee en voz alta tres oraciones de un libro y marca el punto final.",
    "Escribe cuatro oraciones sobre tu familia con mayúscula y punto.",
)

lesson(
    OA14, 2,
    "Cuaderno y lápiz. Las tarjetas de «quién» y «qué hace» están escritas en los ejercicios.",
    "Aprenderé a escribir oraciones diciendo quién hace algo y qué hace. Sirve para contar lo que pasa de forma clara.",
    ["Sé que una oración dice algo completo.", "Sé escribir palabras."],
    [
        "Toda oración básica tiene dos partes. Una dice quién o qué: la niña, el perro, mi papá. La otra dice qué hace o qué pasa: salta, ladra, cocina. Juntas forman una oración: «La niña salta».",
        "Para escribirla, piensa primero quién y luego qué hace. Si uno de los dos falta, la oración queda incompleta. «Salta» no dice quién; «La niña» no dice qué hace.",
        "Puedes cambiar el quién o el qué hace para crear nuevas oraciones. Con «el perro» y «ladra» formas «El perro ladra». Con «el niño» y «ríe», «El niño ríe». Siempre deben tener sentido.",
    ],
    [("quién", "la persona, el animal o la cosa de la que hablo"), ("qué hace", "la acción o lo que pasa"), ("acción", "lo que hace alguien"), ("oración", "palabras que dicen algo completo"), ("combinar", "unir dos partes")],
    [
        ("Armar una oración", "Quién: el perro. Qué hace: ladra. ¿Cuál es la oración?", ["Uno el quién con el qué hace.", "El perro ladra."], "El perro ladra."),
        ("Reconocer partes", "En «La niña salta.», ¿quién es y qué hace?", ["Busco quién: la niña.", "Busco qué hace: salta."], "Quién: la niña. Qué hace: salta"),
    ],
    [
        ("Escribir sólo el quién.", "Se piensa que ya se entiende.", "Agrega qué hace."),
        ("Unir partes que no tienen sentido.", "Se juntan al azar.", "Lee la oración en voz alta."),
    ],
    [
        E("En «El gato duerme.», ¿quién es?", "El gato", "Es el que realiza la acción."),
        E("En «El gato duerme.», ¿qué hace?", "Duerme", "Es la acción."),
        E("En «La niña lee.», ¿quién lee?", "La niña", "Es el quién de la oración."),
    ],
    [
        E("Une: quién «mi papá» y qué hace «cocina».", "Mi papá cocina.", "Se unen las dos partes."),
        E("¿Qué le falta a «Corre en el parque.»?", "Quién corre", "No dice quién hace la acción."),
        E("¿Qué le falta a «Mi hermana.»?", "Qué hace", "No dice la acción."),
    ],
    [
        E("Completa con quién: «____ ladra fuerte.»", "El perro", "Es quien ladra."),
        E("Completa con qué hace: «El niño ____.» (por ejemplo, juega)", "Por ejemplo: juega", "Debe ser una acción."),
        E("Escribe una oración con quién «la abuela» y qué hace «teje».", "La abuela teje.", "Se unen las dos partes."),
    ],
    [
        E("Pedro escribió «Las flores canta». ¿Se entiende bien? Responde sí o no.", "No", "Las flores no cantan; la oración no tiene sentido."),
        E("Ana unió «el pez» con «vuela». ¿Tiene sentido? Responde sí o no.", "No", "Los peces nadan, no vuelan."),
    ],
    [
        E("Forma tres oraciones uniendo estas partes. Quién: el sol, la lluvia, el viento. Qué hace: moja, sopla, brilla. Escribe la oración con «la lluvia».", "La lluvia moja.", "La acción que combina es mojar."),
        E("Con las mismas partes, escribe la oración con «el viento».", "El viento sopla.", "Sopla es la acción del viento."),
    ],
    [E("Mamá pregunta: «¿Qué hace tu hermano?». Respondes: «____ juega con la pelota.» ¿Cuál completa? A) Mi hermano B) Juega", "A) Mi hermano", "Falta decir quién.")],
    [
        E("¿Cuáles son las dos partes básicas de una oración?", "Quién y qué hace", "Dicen quién actúa y qué hace."),
        E("En «El pájaro canta.», ¿qué hace el pájaro?", "Canta", "Es la acción."),
        E("En «Mi mamá trabaja.», ¿quién trabaja?", "Mi mamá", "Es la persona que actúa."),
    ],
    task(
        "Usa esta tabla: Quién: el niño, la gata, mi abuelo, la profesora. Qué hace: lee, duerme, camina, escribe. Escribe tres oraciones uniendo un quién con un qué hace que tenga sentido, con mayúscula y punto.",
        "La gata duerme. La profesora escribe. Mi abuelo camina.",
        ["tres oraciones", "cada una con quién y qué hace", "tienen sentido"],
        ["tres oraciones escritas", "lectura en voz alta"],
        ["unir partes que no tienen sentido", "olvidar el quién o el qué hace"],
        "Lee cada oración en voz alta para comprobar que se entiende.",
    ),
    "Di en voz alta quién y qué hace en cinco oraciones que te lea un adulto.",
    "Cambia el quién de una oración para formar tres nuevas.",
)

lesson(
    OA14, 3,
    "Cuaderno y lápiz. Las oraciones base están escritas en los ejercicios.",
    "Aprenderé a agregar un detalle útil a una oración: dónde, cuándo o cómo. Sirve para que el lector sepa más.",
    ["Sé armar oraciones con quién y qué hace.", "Sé escribir con mayúscula y punto."],
    [
        "Una oración puede decir más si le agregas un detalle. «El perro corre.» es completa. Pero «El perro corre en el parque.» agrega dónde; «El perro corre rápido.» agrega cómo; «El perro corre por la mañana.» agrega cuándo.",
        "Los detalles responden preguntas: ¿dónde?, ¿cuándo?, ¿cómo?, ¿con quién? Cada respuesta es un detalle nuevo para el lector. Agrega el detalle que sea útil para que el lector entienda mejor lo que cuentas.",
        "Cuidado: un detalle debe tener que ver con lo que se cuenta y no hacer la oración confusa. Una o dos ideas bien puestas son suficientes.",
    ],
    [("detalle", "dato que agrega información"), ("dónde", "el lugar"), ("cuándo", "el momento"), ("cómo", "la manera"), ("útil", "que ayuda a entender")],
    [
        ("Agregar dónde", "«La niña lee.» Agrega dónde lee en la biblioteca.", ["Pregunto dónde.", "En la biblioteca."], "La niña lee en la biblioteca."),
        ("Agregar cómo", "«El tren avanza.» Agrega cómo: despacio.", ["Pregunto cómo.", "Despacio."], "El tren avanza despacio."),
    ],
    [
        ("Agregar un detalle que no tiene que ver.", "Se llena la oración de palabras.", "Elige un detalle que ayude a entender."),
        ("Olvidar el punto.", "La oración se hace larga.", "Termina con punto."),
    ],
    [
        E("En «El gato duerme en el sofá.», ¿qué dice el detalle?", "Dónde duerme", "«En el sofá» es un lugar."),
        E("En «El niño corre rápido.», ¿qué dice el detalle?", "Cómo corre", "«Rápido» dice la manera."),
        E("En «Mi tía llega hoy.», ¿qué dice el detalle?", "Cuándo llega", "«Hoy» dice el momento."),
    ],
    [
        E("Agrega dónde: «El pájaro canta.»", "Por ejemplo: El pájaro canta en el árbol.", "Debe decir un lugar."),
        E("Agrega cuándo: «Nico estudia.»", "Por ejemplo: Nico estudia en la tarde.", "Debe decir un momento."),
        E("¿Qué pregunta responde un detalle de lugar?", "¿Dónde?", "El lugar contesta dónde."),
    ],
    [
        E("Agrega un detalle de cómo a: «La tortuga camina.»", "Por ejemplo: La tortuga camina despacio.", "Debe decir cómo camina."),
        E("Agrega un detalle de dónde a: «Los niños juegan.»", "Por ejemplo: Los niños juegan en el patio.", "Debe decir un lugar."),
        E("Escribe una oración con quién, qué hace y un detalle de tiempo sobre el desayuno.", "Por ejemplo: Mi papá prepara el desayuno temprano.", "Debe tener los tres elementos."),
    ],
    [
        E("Ana escribió «El perro corre rápido en el parque ayer hoy». ¿Está bien? Responde sí o no.", "No", "Tiene demasiados detalles confusos."),
        E("¿Cuál detalle ayuda más a «La niña come»? A) en la mesa B) con las estrellas", "A) en la mesa", "Tiene que ver con lo que se cuenta."),
    ],
    [
        E("Une dos detalles en una sola oración: «El gato duerme.» + dónde: en la cama + cómo: tranquilo.", "El gato duerme tranquilo en la cama.", "Se unen los dos detalles."),
        E("¿Qué detalle falta en «Mi mamá cocina»: dónde, cuándo o cómo? Elige uno y escribe la oración.", "Por ejemplo: Mi mamá cocina en la mañana.", "Cualquier detalle útil sirve."),
    ],
    [E("Tu amigo no sabe dónde jugaron. Escribe: «Jugamos» + dónde: en la plaza.", "Jugamos en la plaza.", "Se agrega el detalle de lugar.")],
    [
        E("¿Qué hace un detalle en una oración?", "Dice más información", "Agrega dónde, cuándo o cómo."),
        E("¿«Despacio» responde a dónde, cuándo o cómo?", "Cómo", "Dice la manera."),
        E("¿«En la escuela» responde a dónde, cuándo o cómo?", "Dónde", "Dice el lugar."),
    ],
    task(
        "Toma estas tres oraciones y agrega a cada una un detalle: «El perro corre.» (dónde), «Mi papá cocina.» (cuándo), «La niña canta.» (cómo). Escribe las tres oraciones mejoradas.",
        "El perro corre en el parque. Mi papá cocina en la noche. La niña canta bonito.",
        ["tres oraciones", "cada una con el tipo de detalle pedido", "tienen sentido y punto"],
        ["tres oraciones escritas", "lectura en voz alta"],
        ["agregar un detalle de otro tipo", "olvidar el punto"],
        "Pregunta a alguien qué dato nuevo aprendió con tu detalle.",
    ),
    "Di una oración sobre ti y agrégale un detalle de lugar.",
    "Escribe una oración con dos detalles: dónde y cómo.",
)

lesson(
    OA14, 4,
    "Cuaderno y lápiz. Los destinatarios y los mensajes están escritos en los ejercicios.",
    "Aprenderé a escribir oraciones pensando en quién las leerá. Sirve para que mi mensaje sea claro y amable para esa persona.",
    ["Sé escribir oraciones completas.", "Sé que una carta tiene saludo y firma."],
    [
        "Un mensaje se escribe para alguien: un destinatario. Antes de escribir, piensa quién lo va a leer. A tu abuela le escribes de una forma cariñosa; a tu profesora, con respeto.",
        "El mensaje debe ser claro: di lo que necesitas o quieres contar en oraciones completas. Puedes empezar con un saludo, como «Hola, Ema:» o «Querido abuelo:», y terminar con una despedida y tu nombre.",
        "Si escribes una invitación o un aviso, agrega los datos importantes: qué, cuándo y dónde. Así la persona sabe lo que debe saber y no tiene que adivinar.",
    ],
    [("destinatario", "la persona que lee mi mensaje"), ("saludo", "palabras con que empiezo, como «Hola»"), ("despedida", "palabras con que termino, como «Un abrazo»"), ("mensaje", "lo que quiero comunicar"), ("claro", "que se entiende fácilmente")],
    [
        ("Escribir a la abuela", "Quieres agradecer un abrazo a tu abuela. ¿Qué escribes?", ["Pienso en quién lee.", "Uso un saludo cariñoso y una oración completa."], "Querida abuela: Gracias por tu abrazo. Un beso, Luis"),
        ("Datos de aviso", "Invitas a Pedro a tu cumpleaños el sábado a las tres en tu casa. ¿Qué datos debes incluir?", ["Qué: cumpleaños.", "Cuándo: sábado a las tres. Dónde: mi casa."], "Qué, cuándo y dónde"),
    ],
    [
        ("Escribir sin pensar en quién lee.", "Se escribe como se habla con amigos.", "Piensa quién leerá y usa palabras adecuadas."),
        ("Dejar fuera datos importantes.", "Se cree que todos saben.", "Agrega qué, cuándo y dónde."),
    ],
    [
        E("¿Quién es el destinatario de un mensaje?", "La persona que lo lee", "El mensaje va dirigido a ella."),
        E("¿Con qué palabras puede empezar un mensaje amable? A) «Querida tía» B) «Oye tú»", "A) «Querida tía»", "Es un saludo cariñoso y respetuoso."),
        E("¿Con qué puede terminar un mensaje?", "Con una despedida y mi nombre", "Así cierra el mensaje."),
    ],
    [
        E("Lee: «Hola, Ema: Mañana vamos al parque a las cuatro. Luis». ¿Cuándo van al parque?", "Mañana a las cuatro", "El mensaje lo dice."),
        E("Lee: «Hola, Ema: Mañana vamos al parque a las cuatro. Luis». ¿Quién lo escribe?", "Luis", "Es la firma."),
        E("¿Qué tres datos importantes tiene una invitación?", "Qué, cuándo y dónde", "Con ellos la persona sabe todo."),
    ],
    [
        E("Escribe un saludo para tu profesora. Por ejemplo, usa «Estimada profesora».", "Estimada profesora:", "Es un saludo respetuoso."),
        E("Escribe un saludo para tu mejor amigo: «Hola, ...» agregando un nombre inventado.", "Por ejemplo: Hola, Pablo:", "Es un saludo cercano."),
        E("Escribe una oración para pedir un lápiz a tu compañero: «Por favor, ...»", "Por ejemplo: Por favor, ¿me prestas un lápiz?", "Pide con cortesía."),
    ],
    [
        E("Lucas escribió a su profesora: «Oye, no voy mañana». ¿Qué cambiarías?", "El saludo y la forma de decirlo, con más respeto", "Se debe escribir con respeto a la profesora."),
        E("Tomás invitó a Ana a su cumpleaños pero no dijo cuándo. ¿Qué dato falta?", "Cuándo", "Ana no sabe el día ni la hora."),
    ],
    [
        E("Escribe la invitación completa con estos datos: para Rosa, cumpleaños, sábado a las tres, en mi casa. Escribe una oración.", "Por ejemplo: Rosa, te invito a mi cumpleaños el sábado a las tres en mi casa.", "Incluye qué, cuándo y dónde."),
        E("Ordena un mensaje: a) Un abrazo, Luis. b) Querida abuela: c) Gracias por tu regalo. Escribe las letras.", "b, c, a", "Primero el saludo, luego el mensaje y al final la despedida."),
    ],
    [E("Tu curso hace una reunión de padres el viernes a las cinco en la sala. Tú escribes el aviso para tu mamá. ¿Cuál es el mejor? A) «Hay reunión» B) «Mamá: hay reunión el viernes a las cinco en la sala.»", "B) «Mamá: hay reunión el viernes a las cinco en la sala.»", "Tiene los datos completos.")],
    [
        E("¿Para quién escribes un mensaje?", "Para un destinatario", "Es quien lo leerá."),
        E("¿Qué debe tener una invitación?", "Qué, cuándo y dónde", "Son los datos clave."),
        E("¿Cómo se escribe a una profesora?", "Con respeto", "Se usan palabras amables."),
    ],
    task(
        "Elige a quién escribirás: A) tu abuela, B) tu profesora, C) un amigo. Escribe un mensaje de dos oraciones con saludo, mensaje y despedida. Contenido sugerido: A) agradecerle por una visita, B) avisar que mañana llegarás tarde, C) invitarlo a jugar el sábado a las cuatro en la plaza.",
        "Querida abuela: Gracias por venir a verme. Fue un día muy lindo. Un abrazo, Luis.",
        ["tiene saludo", "mensaje claro con oraciones completas", "tiene despedida y firma"],
        ["mensaje escrito", "lectura en voz alta"],
        ["no usar saludo", "olvidar datos importantes", "usar tono inadecuado para el destinatario"],
        "Lee el mensaje pensando en la persona: ¿se entiende y es amable?",
    ),
    "Di en voz alta un mensaje para alguien de tu casa.",
    "Escribe una invitación completa con qué, cuándo y dónde.",
)

lesson(
    OA14, 5,
    "Cuaderno y lápiz. Los textos con errores están escritos en los ejercicios.",
    "Aprenderé a releer lo que escribí para encontrar lo que falta y mejorar mi oración. Sirve para que mi mensaje se entienda.",
    ["Sé escribir oraciones completas.", "Sé usar mayúscula y punto."],
    [
        "Después de escribir, hay que releer. Lee lo que escribiste en voz alta y pregúntate: ¿se entiende?, ¿tiene mayúscula y punto?, ¿le falta alguna palabra? Si algo no suena bien, corrígelo.",
        "Usa una lista para revisar: 1) Empieza con mayúscula. 2) Dice quién y qué hace. 3) Termina con punto. 4) Las palabras están separadas. Si cumples los cuatro puntos, tu oración está lista.",
        "Si falta una palabra, la agregas. Por ejemplo, «El niño en la plaza» le falta qué hace: «El niño juega en la plaza». Releer es una forma de mejorar sin miedo a equivocarte.",
    ],
    [("releer", "leer otra vez lo que escribí"), ("corregir", "cambiar para mejorar"), ("completar", "agregar lo que falta"), ("revisar", "mirar con atención"), ("lista de revisión", "preguntas para comprobar mi escritura")],
    [
        ("Corregir", "«el niño juega en la plaza» ¿Qué le falta?", ["Empieza con minúscula.", "No termina con punto."], "Mayúscula al inicio y punto al final: El niño juega en la plaza."),
        ("Completar", "«La niña en el patio.» ¿Qué falta?", ["Dice quién y dónde, pero no qué hace.", "Agrego una acción: juega."], "Falta qué hace: La niña juega en el patio."),
    ],
    [
        ("Entregar sin releer.", "Se termina con prisa.", "Lee en voz alta antes de terminar."),
        ("Corregir y dejar otros errores.", "Se mira sólo una cosa.", "Usa la lista de revisión completa."),
    ],
    [
        E("¿Qué haces después de escribir?", "Releer", "Así se detectan errores."),
        E("¿«los perros ladran.» empieza bien? Responde sí o no.", "No", "Debe empezar con mayúscula."),
        E("¿«El sol brilla» tiene punto final? Responde sí o no.", "No", "Le falta el punto."),
    ],
    [
        E("Corrige: «mi mamá cocina»", "Mi mamá cocina.", "Mayúscula al inicio y punto al final."),
        E("Corrige: «La niña en el parque.» (agrega qué hace)", "Por ejemplo: La niña juega en el parque.", "Faltaba la acción."),
        E("En Lenguaje: ¿Para qué sirve la lista de revisión?", "Para comprobar si mi oración está bien", "Ayuda a mirar todos los puntos."),
    ],
    [
        E("Corrige las palabras pegadas: «Elgatoduerme.»", "El gato duerme.", "Se separan las palabras."),
        E("Corrige: «ayer fui al parque con mi abuelo». Escribe la oración bien escrita.", "Ayer fui al parque con mi abuelo.", "Mayúscula y punto."),
        E("Agrega la palabra que falta: «Mi hermano ___ pan.» (come)", "Mi hermano come pan.", "Falta la acción."),
    ],
    [
        E("Luis dice: «No releo porque ya está bien». Su mamá le sugiere releer. ¿Quién tiene razón?", "Su mamá", "Releer ayuda a encontrar errores."),
        E("¿Cuántos puntos tiene la lista de revisión de esta clase?", "4", "Son mayúscula, quién y qué hace, punto y separación."),
    ],
    [
        E("Revisa: «la gata duerme en el sillón» y escribe cuántas cosas corriges (mayúscula y punto).", "2", "Hay que corregir la mayúscula y el punto."),
        E("Escribe la oración completa y corregida: «mi abuela llega hoy».", "Mi abuela llega hoy.", "Mayúscula al inicio y punto al final."),
    ],
    [E("Tu compañero te muestra «Los niños juegan en la plaza». Revisa con la lista de 4 puntos. ¿Está lista? Responde sí o no.", "Sí", "Tiene mayúscula, quién y qué hace, punto y separación.")],
    [
        E("¿Qué se revisa al principio de la oración?", "La mayúscula", "Debe empezar con letra grande."),
        E("¿Qué se revisa al final de la oración?", "El punto", "Marca el final."),
        E("Si falta una palabra, ¿qué haces?", "La agrego", "Se completa la oración."),
    ],
    task(
        "Corrige estas tres oraciones y escríbelas bien: A) «el niño come pan» B) «La niña en la casa.» (agrega qué hace) C) «Mipapálee.» (separa las palabras y agrega mayúscula y punto).",
        "A) El niño come pan. B) La niña juega en la casa. C) Mi papá lee.",
        ["corrige las tres", "mayúscula y punto", "palabras separadas y completas"],
        ["tres oraciones corregidas", "lectura en voz alta"],
        ["corregir sólo una parte", "olvidar el punto"],
        "Marca con un visto cada punto de la lista cuando lo hayas revisado.",
    ),
    "Lee una oración tuya en voz alta y busca qué mejorar.",
    "Escribe tres oraciones con errores y pide a alguien que las corrija.",
)

# ======================================================================== OA 15
lesson(
    OA15, 1,
    "Cuaderno, lápiz y una hoja. Las frases a comparar están escritas en los ejercicios.",
    "Aprenderé por qué es importante escribir de forma que otros puedan leer. Sirve para que mis mensajes se entiendan.",
    ["Sé escribir mi nombre.", "Sé qué es una letra."],
    [
        "Cuando escribes, otra persona leerá lo que hiciste. Si las letras son claras y están bien separadas, esa persona entiende rápido. Si están muy chicas, muy grandes o pegadas, se vuelve difícil leer.",
        "Una letra clara tiene la forma correcta, un tamaño parecido a las demás y está sobre la línea. Una escritura clara también deja espacio entre las palabras. Así el lector no se confunde.",
        "Después de escribir, comprueba: ¿se leen todas las letras?, ¿hay espacio entre las palabras? Si alguien tiene que adivinar lo que escribiste, puedes mejorar tu letra.",
    ],
    [("legible", "que se puede leer con facilidad"), ("letra clara", "letra con buena forma y tamaño"), ("espacio", "hueco entre palabras"), ("lector", "quien lee lo que escribí"), ("línea", "raya del cuaderno donde apoyo las letras")],
    [
        ("Elegir la más clara", "A) «El gato duerme.» (letras claras y separadas) B) «Elgatoduerme» (palabras pegadas). ¿Cuál se lee mejor?", ["La A tiene espacios.", "La B está pegada."], "La A"),
        ("Pensar en el lector", "Escribes una nota. ¿Para quién tiene que ser fácil de leer?", ["Pienso en el lector.", "Debe entender sin adivinar."], "Para la persona que la leerá"),
    ],
    [
        ("Escribir muy rápido.", "Se quiere terminar pronto.", "Escribe con calma para que se lea."),
        ("Pensar que sólo yo debo entender.", "Se olvida al lector.", "Pregúntate si otro lo entenderá."),
    ],
    [
        E("¿Cuál se lee mejor? A) «Mi perro corre.» B) «Miperrocorre»", "A) «Mi perro corre.»", "Tiene espacios entre las palabras."),
        E("¿Para quién escribes una nota con letra clara?", "Para un lector", "Otra persona la leerá después."),
        E("¿Qué hace que un texto sea legible?", "Letras claras y palabras separadas", "Se puede leer con facilidad."),
    ],
    [
        E("Una nota con letras muy chicas y pegadas, ¿se lee fácil? Responde sí o no.", "No", "Las letras pequeñas y pegadas se confunden."),
        E("¿Qué debe haber entre palabras?", "Un espacio", "Separa las palabras."),
        E("¿Sobre qué se apoyan las letras?", "Sobre la línea", "La línea ayuda a escribir parejo."),
    ],
    [
        E("Copia con letra clara: «El sol brilla.»", "El sol brilla.", "Debe verse clara y separada."),
        E("Copia la frase y deja un espacio entre palabras: «Elniñojuega».", "El niño juega", "Se separan las palabras."),
        E("Copia con calma tu nombre completo en letra clara.", "Tu nombre bien escrito", "La letra debe ser clara."),
    ],
    [
        E("Ana escribió muy rápido y su nota no se entiende. ¿Qué puede hacer? A) Escribirla de nuevo con calma B) Dejarla así", "A) Escribirla de nuevo con calma", "Así podrá leerse."),
        E("Pablo dice: «Yo sé lo que dice, no importa». ¿Es correcto? Responde sí o no.", "No", "Otros deben poder leerla."),
    ],
    [
        E("Lee dos versiones: A) «Mamá fue al mercado.» B) «M a m a f u e a l m e r c a d o». ¿Cuál se lee mejor?", "A", "Las letras no están sueltas y se entiende."),
        E("Una frase tiene 4 palabras y entre ellas hay 3 espacios. ¿Cuántos espacios habrá en una frase de 5 palabras?", "4", "Siempre hay un espacio menos que palabras."),
    ],
    [E("Escribes una nota para tu vecina para avisarle que hay un paquete en tu casa. ¿Qué cuidas para que ella la lea? A) Letra clara y espacios B) Letra pequeña y pegada", "A) Letra clara y espacios", "Así se lee mejor.")],
    [
        E("¿Qué es un lector?", "Quien lee lo que escribí", "Es el destinatario del texto."),
        E("¿Qué hace legible mi letra?", "Que sea clara", "Se lee fácil."),
        E("¿Dónde escribo las letras?", "Sobre la línea", "Ayuda a mantener el orden."),
    ],
    task(
        "Copia esta frase tres veces con letra clara y espacios: «Me gusta leer cuentos.» Luego marca cuál copia se lee mejor y explica por qué en una oración.",
        "Me gusta leer cuentos. La tercera se lee mejor porque tiene espacios más parejos.",
        ["tres copias", "letras claras y separadas", "explicación con una razón"],
        ["tres copias en el cuaderno", "comparación oral"],
        ["escribir pegado", "no explicar"],
        "Mira las tres copias juntas y escoge la que se entienda más rápido.",
    ),
    "Escribe tu nombre tres veces y elige la copia que se lea mejor.",
    "Escribe una nota con letra clara para alguien de tu casa.",
)

lesson(
    OA15, 2,
    "Cuaderno, lápiz y una silla. La postura y el trazo están descritos en los ejercicios.",
    "Aprenderé cómo sentarme, tomar el lápiz y hacer los trazos para escribir cómodo. Sirve para que mis letras salgan claras y no me canse.",
    ["Sé tomar un lápiz.", "Sé escribir algunas letras."],
    [
        "Para escribir bien, siéntate con la espalda recta, los pies en el suelo y el cuaderno sobre la mesa. Toma el lápiz con tres dedos: pulgar, índice y medio. No lo aprietes fuerte; así la mano no se cansa.",
        "Los trazos de las letras van en un orden. En general, se empieza arriba y se baja, y de izquierda a derecha. Por ejemplo, la «l» comienza arriba y baja en línea recta. La «o» empieza arriba, gira hacia la izquierda y se cierra.",
        "Escribir lento y con atención ayuda a que las letras salgan parecidas entre sí. Con práctica diaria tu mano aprende los movimientos.",
    ],
    [("postura", "forma de sentarme"), ("trazo", "movimiento para hacer una letra"), ("pinza", "tomar el lápiz con tres dedos"), ("recto", "sin curvas"), ("práctica", "repetir para mejorar")],
    [
        ("Postura", "Pedro escribe con la espalda doblada y la cabeza pegada al cuaderno. ¿Qué debe cambiar?", ["Debe sentarse recto.", "Debe separar la cabeza del cuaderno."], "Sentarse con la espalda recta"),
        ("Trazo de la l", "¿Cómo se hace la letra «l»?", ["Empiezo arriba.", "Bajo en línea recta."], "Se empieza arriba y se baja en línea recta"),
    ],
    [
        ("Apretar mucho el lápiz.", "Se cree que así sale mejor.", "Toma el lápiz con tres dedos, suave."),
        ("Empezar las letras por abajo.", "Se hace lo más fácil.", "Empieza arriba y baja."),
    ],
    [
        E("¿Cómo debe estar la espalda al escribir?", "Recta", "Ayuda a no cansarse."),
        E("¿Con cuántos dedos tomas el lápiz?", "Tres", "Pulgar, índice y medio."),
        E("¿Dónde van los pies al escribir?", "En el suelo", "Dan estabilidad al cuerpo."),
    ],
    [
        E("¿Dónde empieza la letra «l»? A) Arriba B) Abajo", "A) Arriba", "Se baja en línea recta."),
        E("¿Hacia qué lado se escribe una línea de texto? A) Izquierda a derecha B) Derecha a izquierda", "A) Izquierda a derecha", "Así se lee y se escribe en español."),
        E("¿Qué pasa si aprietas mucho el lápiz?", "La mano se cansa", "Se hace fuerza de más."),
    ],
    [
        E("Escribe tres veces la letra «l» empezando arriba.", "l l l", "Debe verse parecida cada vez."),
        E("Escribe tres veces la letra «o» cerrando el círculo.", "o o o", "Debe quedar cerrada."),
        E("Escribe tu nombre despacio con trazos claros.", "Tu nombre", "La letra debe verse clara."),
    ],
    [
        E("Rosa tiene el papel torcido y se le tuercen las líneas. ¿Qué puede hacer?", "Acomodar bien el cuaderno", "El cuaderno derecho ayuda a escribir parejo."),
        E("Camila escribe con tres dedos pero muy fuerte y le duele la mano. ¿Qué cambia?", "Apretar menos el lápiz", "Con suavidad no se cansa."),
    ],
    [
        E("Ordena para empezar a escribir: a) Tomar el lápiz con tres dedos. b) Sentarme derecho. c) Comenzar a escribir despacio. Escribe las letras.", "b, a, c", "Primero la postura, luego el lápiz y después escribir."),
        E("En la letra «o», ¿hacia qué lado gira primero el trazo? A) Izquierda B) Derecha", "A) Izquierda", "Empieza arriba y gira hacia la izquierda."),
    ],
    [E("Tomás se cansa después de escribir una línea. Su postura: espalda doblada y lápiz apretado. ¿Qué dos cosas puede cambiar?", "Sentarse recto y apretar menos el lápiz", "Ambos ayudan a no cansarse.")],
    [
        E("¿Cuál es la postura correcta? A) Espalda recta B) Espalda doblada", "A) Espalda recta", "Es más cómoda."),
        E("¿Cómo se toma el lápiz?", "Con tres dedos", "Se llama pinza."),
        E("¿Qué ayuda a mejorar la letra?", "Practicar con calma", "La mano aprende los movimientos."),
    ],
    task(
        "Escribe tres veces cada una de estas palabras con buena postura y trazos claros: «lola, loro, ola». Luego cuéntale a un adulto cómo estabas sentado.",
        "lola lola lola, loro loro loro, ola ola ola. Estaba sentado con la espalda recta y los pies en el suelo.",
        ["escribe las tres palabras tres veces", "letras parecidas entre sí", "describe su postura"],
        ["hoja con las palabras", "descripción oral"],
        ["letras muy distintas entre sí", "no describir la postura"],
        "Revisa si las letras «l» y «o» salen parecidas en cada copia.",
    ),
    "Siéntate bien y escribe la letra «l» cinco veces.",
    "Dibuja cómo se ve una persona sentada correctamente para escribir.",
)

lesson(
    OA15, 3,
    "Cuaderno con líneas y lápiz. Las listas de letras están escritas en los ejercicios.",
    "Aprenderé a escribir letras de un tamaño parejo y sobre la línea. Sirve para que mi escritura se vea ordenada y se pueda leer.",
    ["Sé escribir las letras.", "Sé qué es una línea del cuaderno."],
    [
        "Las letras se apoyan sobre una línea del cuaderno. Algunas son bajas, como a, e, o, m, n, u: ocupan poco espacio. Otras son altas, como b, d, f, h, k, l, t: suben más arriba de la línea.",
        "Hay letras que además bajan por debajo de la línea: g, j, p, q, y. Su «cola» pasa la línea hacia abajo. Si todas las letras tienen el tamaño que les corresponde, la escritura se ve pareja.",
        "Para cuidar el tamaño, fíjate en las letras bajas, que deben ser parecidas entre sí, y en las altas, que deben subir más. Escribe despacio y comprueba que todas se apoyen en la misma línea.",
    ],
    [("línea", "raya donde apoyo las letras"), ("letra alta", "letra que sube, como b, d, l o t"), ("letra baja", "letra que ocupa poco espacio, como a, e, o"), ("cola", "parte que baja de g, j, p, q, y"), ("parejo", "de tamaño parecido")],
    [
        ("Clasificar", "¿La letra «l» es alta o baja?", ["La «l» sube.", "Es una letra alta."], "Alta"),
        ("Letra con cola", "¿La letra «p» sube o baja de la línea?", ["La p tiene una cola.", "Baja de la línea."], "Baja de la línea"),
    ],
    [
        ("Hacer las letras de distinto tamaño.", "Se escribe sin cuidar.", "Mantén el tamaño parecido entre las letras."),
        ("No apoyar las letras en la línea.", "Se escribe flotando.", "Apóyalas todas en la misma línea."),
    ],
    [
        E("¿La letra «a» es alta o baja?", "Baja", "Ocupa poco espacio."),
        E("¿La letra «b» es alta o baja?", "Alta", "Sube sobre la línea."),
        E("¿La letra «g» baja de la línea?", "Sí", "Tiene una cola hacia abajo."),
    ],
    [
        E("¿Cuál de estas letras tiene cola? A) m B) y", "B) y", "La y baja de la línea."),
        E("¿Cuál es alta? A) t B) o", "A) t", "La t sube más que la o."),
        E("¿Cuál es baja? A) n B) h", "A) n", "La n ocupa poco espacio."),
    ],
    [
        E("Clasifica las letras: a, d, p. ¿Cuál es alta?", "d", "La d sube; a es baja y p baja de la línea."),
        E("Clasifica las letras: e, k, q. ¿Cuál tiene cola?", "q", "La q baja de la línea."),
        E("Escribe tres letras altas.", "Por ejemplo: b, d, l", "Las letras b, d, f, h, k, l, t son altas."),
    ],
    [
        E("Ana escribió todas sus letras del mismo tamaño, incluso la «l» y la «b». ¿Qué le falta?", "Hacer las letras altas más altas", "Las altas suben más."),
        E("Beto escribió «pato» pero la p no baja de la línea. ¿Qué cambia?", "Hacer la cola de la p hacia abajo", "La p debe bajar de la línea."),
    ],
    [
        E("En la palabra «pelota», ¿cuántas letras son altas (l, t)?", "2", "La l y la t son altas."),
        E("En la palabra «jirafa», ¿cuántas letras tienen cola (j)?", "1", "Sólo la j baja de la línea."),
    ],
    [E("Camila escribe «gato» en su cuaderno. ¿Qué es correcto? A) g baja, t sube B) g sube, t baja", "A) g baja, t sube", "La g tiene cola y la t es alta.")],
    [
        E("¿Cuál es una letra alta? A) d B) a", "A) d", "La d sube."),
        E("¿Cuál tiene cola? A) y B) i", "A) y", "La y baja de la línea."),
        E("¿Dónde deben apoyarse todas las letras al escribir?", "En la misma línea", "Así la escritura queda pareja."),
    ],
    task(
        "Escribe estas cuatro palabras en tu cuaderno cuidando el tamaño: «tomate, jarra, gato, mesa». Pinta en cada una las letras altas de un color y las letras con cola de otro. Luego di cuántas letras altas tiene «tomate».",
        "tomate (la t es alta, hay 2 altas), jarra (la j tiene cola), gato (la g tiene cola, la t es alta), mesa (todas bajas).",
        ["escribe las cuatro palabras", "pinta correctamente altas y colas", "responde cuántas altas tiene tomate"],
        ["cuaderno con las palabras pintadas", "respuesta oral"],
        ["confundir alta con cola", "no cuidar el tamaño"],
        "Mira que todas las letras bajas tengan el mismo tamaño.",
    ),
    "Escribe las letras b, d, g, p e y, y di cuáles bajan de la línea.",
    "Busca tres palabras de tu casa con letras de cola y escríbelas.",
)

lesson(
    OA15, 4,
    "Cuaderno y lápiz. Las frases sin espacios están escritas en los ejercicios.",
    "Aprenderé a separar las palabras con un espacio. Sirve para que otros puedan leer mi texto fácilmente.",
    ["Sé escribir palabras.", "Sé qué es un espacio."],
    [
        "Entre una palabra y la siguiente va un espacio. Si las pegas, el texto se vuelve difícil de leer: «Elgatoduermeenlacama» se entiende más lento que «El gato duerme en la cama».",
        "Un buen tamaño de espacio es del ancho de un dedo o de una letra «o». Así las palabras no quedan ni pegadas ni muy lejanas. Los espacios deben ser parecidos entre sí.",
        "Para revisar, cuenta las palabras y los espacios. En una frase hay un espacio menos que palabras. Si la frase tiene 5 palabras, tiene 4 espacios.",
    ],
    [("espacio", "hueco entre palabras"), ("palabra", "letras juntas que significan algo"), ("pegar", "unir sin dejar espacio"), ("separar", "dejar un espacio"), ("ancho de un dedo", "medida para el espacio")],
    [
        ("Separar", "Separa: «Elniñojuega.»", ["Busco dónde terminan las palabras.", "El / niño / juega."], "El niño juega."),
        ("Contar", "¿Cuántas palabras tiene «La niña lee un libro.»?", ["Cuento: La, niña, lee, un, libro.", "Son cinco."], "5 palabras"),
    ],
    [
        ("Dejar espacios muy chicos.", "Se escribe apretado.", "Deja el ancho de un dedo."),
        ("Separar en medio de una palabra.", "Se parte donde no corresponde.", "Cada palabra va junta."),
    ],
    [
        E("¿Cuántas palabras tiene «El perro corre.»?", "3", "Son El, perro y corre."),
        E("¿Cuántos espacios hay en «El perro corre.»?", "2", "Hay uno entre cada par de palabras."),
        E("¿Cuál es mejor? A) «Elperrocorre» B) «El perro corre»", "B) «El perro corre»", "Tiene las palabras separadas."),
    ],
    [
        E("Separa: «Mamáleeunlibro.»", "Mamá lee un libro.", "Se separan cuatro palabras."),
        E("Separa: «Elsolbrillaenelcielo.»", "El sol brilla en el cielo.", "Se separan las palabras."),
        E("¿Cuántos espacios tiene «Mi papá cocina pan.»?", "3", "Son 4 palabras, 3 espacios."),
    ],
    [
        E("Escribe la frase con espacios: «Lasnubessonblancas.»", "Las nubes son blancas.", "Se separa cada palabra."),
        E("Escribe con espacios: «Elpatonadaenelrío.»", "El pato nada en el río.", "Se separan las palabras."),
        E("Escribe con espacios: «Yoleocuentoscadadía.»", "Yo leo cuentos cada día.", "Se separan las palabras."),
    ],
    [
        E("Una frase tiene 6 palabras. ¿Cuántos espacios tiene?", "5", "Siempre hay un espacio menos que palabras."),
        E("Nico escribió «El ni ño ju ega». ¿Qué error cometió?", "Separó dentro de las palabras", "Cada palabra va junta."),
    ],
    [
        E("Separa y cuenta: «Hoyvoyalaplaza.» ¿Cuántas palabras tiene?", "5", "Se separa así: Hoy voy a la plaza."),
        E("Separa: «Lagatabebeleche.»", "La gata bebe leche.", "Se separan cuatro palabras."),
    ],
    [E("Tu hermana te dice que no entiende la nota que escribiste: «Salíalaplaza». Reescríbela con espacios.", "Salí a la plaza.", "Con espacios se lee mejor.")],
    [
        E("¿Qué va entre una palabra y otra?", "Un espacio", "El espacio las separa."),
        E("¿Cuántos espacios tiene una frase de 4 palabras?", "3", "Uno menos que palabras."),
        E("¿Qué medida sirve para el espacio?", "El ancho de un dedo", "Es una forma sencilla de medirlo."),
    ],
    task(
        "Separa y escribe estas tres frases: A) «Lalunaesgrande.» B) «Mivecinaleeunlibro.» C) «Elperroduermeenlacama.» Luego cuenta las palabras de cada una.",
        "A) La luna es grande. (4) B) Mi vecina lee un libro. (5) C) El perro duerme en la cama. (6)",
        ["separa las tres", "las palabras quedan completas", "cuenta bien las palabras"],
        ["tres frases separadas", "conteo oral"],
        ["separar en medio de una palabra", "no contar bien"],
        "Pon el dedo entre cada palabra para comprobar el espacio.",
    ),
    "Escribe tu frase favorita dejando un dedo entre las palabras.",
    "Escribe una oración de ocho palabras y cuenta sus espacios.",
)

lesson(
    OA15, 5,
    "Cuaderno y lápiz. Las muestras de escritura están descritas en los ejercicios.",
    "Aprenderé a comprobar con un lector si mi escritura se entiende. Sirve para mejorar lo que escribo.",
    ["Sé escribir con letra clara.", "Sé separar palabras."],
    [
        "La mejor forma de saber si tu letra es legible es pedir a otra persona que lea lo que escribiste. Si lee sin dudar, tu escritura funciona. Si se detiene o pregunta, hay algo para mejorar.",
        "Usa esta pauta: 1) Las letras tienen forma clara. 2) Están sobre la línea. 3) Las palabras tienen espacio. 4) Se lee a la primera. Si alguna falla, escríbela otra vez con calma.",
        "No te enojes si el lector no entiende. Es una oportunidad de mejorar. Cambia lo que haga falta y vuelve a probar con el lector.",
    ],
    [("pauta", "lista de puntos para revisar"), ("lector", "quien lee mi texto"), ("probar", "comprobar si funciona"), ("mejorar", "hacer algo mejor"), ("a la primera", "sin necesidad de repetir")],
    [
        ("Usar la pauta", "Un lector se detiene en la palabra «Elgato». ¿Qué falla?", ["Las palabras están pegadas.", "Falla el espacio."], "El espacio entre palabras"),
        ("Mejorar", "Si el lector no entiende una letra, ¿qué haces?", ["Escribo de nuevo con calma.", "Pruebo otra vez con el lector."], "Escribirla de nuevo con calma"),
    ],
    [
        ("Enojarse si el lector no entiende.", "Se siente como un fracaso.", "Toma la ayuda para mejorar."),
        ("Revisar sólo la forma de las letras.", "Se olvida el resto.", "Usa los cuatro puntos de la pauta."),
    ],
    [
        E("¿Para qué se prueba la escritura con un lector?", "Para saber si se entiende", "El lector muestra si se lee."),
        E("¿Cuántos puntos tiene la pauta de revisión?", "4", "Forma, línea, espacio y lectura."),
        E("Si el lector lee a la primera, ¿la escritura funciona?", "Sí", "Se entendió sin dudar."),
    ],
    [
        E("Un lector lee «Me gusta el sol» sin detenerse. ¿Qué indica?", "Que la escritura es clara", "Se leyó a la primera."),
        E("Un lector dice «No sé si es una a o una o». ¿Qué falla?", "La forma de las letras", "No están claras."),
        E("Un lector dice «Las palabras se pegan». ¿Qué falla?", "El espacio entre palabras", "Hay que separarlas."),
    ],
    [
        E("Una frase tiene letras claras, está sobre la línea, tiene espacios y se lee a la primera. ¿Cuántos puntos de la pauta cumple?", "4", "Cumple todos los puntos de la pauta."),
        E("Una frase cumple tres puntos de la pauta. ¿Cuántos le faltan?", "1", "4 menos 3 es 1."),
        E("Escribe una frase corta con letra clara para un lector: «Hoy hace sol.»", "Hoy hace sol.", "Debe verse clara y separada."),
    ],
    [
        E("Luis escribió una nota pero su mamá no entendió una palabra. ¿Qué debe hacer?", "Escribir la palabra de nuevo con letra más clara", "Así mejora la lectura."),
        E("Dos niños prueban sus notas. A uno le dicen que se entiende todo; al otro, que hay palabras pegadas. ¿Quién debe corregir?", "El que tiene palabras pegadas", "Debe separar las palabras."),
    ],
    [
        E("Una nota dice: «Mamáfuialaplaza». Un lector no la entiende. Escribe la corrección.", "Mamá: fui a la plaza.", "Con espacios y puntuación se entiende."),
        E("Ordena los pasos para probar: a) Escribir una nota. b) Mejorar si hace falta. c) Pedir que la lean. Escribe las letras.", "a, c, b", "Primero escribes, luego pruebas y después mejoras."),
    ],
    [E("Mía escribió una nota para su vecino: «Hoy vendré a las cuatro». Su amiga la leyó sin problemas. ¿Qué concluye Mía?", "Que su escritura es legible", "El lector entendió.")],
    [
        E("¿Qué se hace para probar la escritura?", "Pedir que alguien la lea", "Así se comprueba."),
        E("¿Se debe enojar uno si el lector no entiende?", "No", "Sirve para mejorar."),
        E("¿Qué se hace si algo falla en la pauta?", "Se corrige y se vuelve a probar", "Así se mejora la escritura."),
    ],
    task(
        "Escribe esta frase con tu mejor letra: «Mi casa es azul y tiene un jardín.» Pide a alguien de tu casa que la lea y completa la pauta: ¿letras claras? ¿sobre la línea? ¿con espacios? ¿se leyó a la primera? (Sí o no en cada una).",
        "Letras claras: sí. Sobre la línea: sí. Con espacios: sí. Se leyó a la primera: sí.",
        ["escribe la frase completa", "completa los cuatro puntos de la pauta", "un lector la lee"],
        ["frase escrita", "pauta completada"],
        ["no pedir a un lector", "marcar sin comprobar"],
        "Si un punto es «no», escribe la frase otra vez mejorando ese punto.",
    ),
    "Pide a alguien que lea tu nombre y dime si lo entendió.",
    "Escribe una nota de cuatro oraciones, pruébala con un lector y mejórala.",
)

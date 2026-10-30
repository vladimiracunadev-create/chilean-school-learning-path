"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 18 (vocabulario nuevo en la escritura) y OA 19 (artículos, sustantivos y adjetivos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA18, OA19 = "LE02 OA 18", "LE02 OA 19"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 18 · clase 1
reg(
    OA18, 1,
    "Los textos de este cuaderno, lápiz y una hoja para armar tu banco de palabras.",
    "Aprenderé a encontrar una palabra nueva en un texto y a anotarla con su significado y su frase. Sirve para poder usarla después cuando escriba.",
    ["Sé buscar pistas en una frase.", "Sé escribir oraciones completas."],
    [
        "Cuando lees o escuchas un texto, aparecen palabras nuevas. Si las anotas, las puedes usar después en tus propios textos. Para eso sirve un banco de palabras: una lista donde guardas cada palabra nueva.",
        "En tu banco escribe tres cosas: la palabra, la frase donde la encontraste y lo que significa. Por ejemplo: «sendero»; «Luna caminó por un sendero angosto entre los árboles»; significa camino angosto. Para saber el significado, usa las pistas de la frase o pregunta.",
        "Anotar la frase es importante porque te recuerda cómo se usa la palabra. Así, cuando escribas, podrás recuperar la palabra del banco y ponerla en tu texto.",
    ],
    [("banco de palabras", "lista de palabras nuevas con su significado"), ("sendero", "camino angosto"), ("diminuto", "muy pequeño"), ("ágil", "que se mueve rápido y con facilidad"), ("refugio", "lugar para protegerse")],
    [
        ("Anotar una palabra nueva", "Texto: «Luna caminó por un sendero angosto entre los árboles». Anota la palabra nueva «sendero».", ["Busco pistas: «angosto» y «entre los árboles».", "Un sendero es un camino angosto.", "Escribo palabra, frase y significado."], "sendero · «Luna caminó por un sendero angosto entre los árboles» · camino angosto."),
        ("Anotar otra palabra", "Texto: «El ratón diminuto cabía en la palma de mi mano». Anota «diminuto».", ["Pista: cabía en la palma de mi mano.", "Algo que cabe en la mano es muy pequeño."], "diminuto · «El ratón diminuto cabía en la palma de mi mano» · muy pequeño."),
    ],
    [("Anotar la palabra sin su significado.", "Se piensa que se va a recordar sola.", "Escribe siempre qué significa."), ("No anotar la frase.", "Se cree que la palabra basta.", "Copia la frase para recordar cómo se usa.")],
    [
        E("Un banco de palabras es una lista de palabras nuevas con su significado. ¿Para qué sirve?", "Para recordarlas y usarlas después", "Guardar palabras ayuda a escribirlas más tarde."),
        E("En «Luna caminó por un sendero angosto entre los árboles», ¿qué palabra puede ser nueva: sendero o árboles?", "sendero", "«Árboles» es muy conocida."),
        E("Marca las pistas de «sendero» en «Luna caminó por un sendero angosto entre los árboles».", "angosto; entre los árboles", "Describen un camino angosto."),
    ],
    [
        E("Según tu banco, ¿qué significa «sendero»?", "Camino angosto", "Así lo anotamos con las pistas."),
        E("En «El ratón diminuto cabía en la palma de mi mano», ¿qué significa «diminuto»?", "Muy pequeño", "Si cabe en la mano, es muy pequeño."),
        E("¿Por qué conviene anotar la frase donde apareció la palabra?", "Porque recuerda cómo se usa", "La frase muestra el uso real."),
    ],
    [
        E("Texto: «La niña ágil saltó el muro y corrió sin cansarse». ¿Qué significa «ágil»?", "Que se mueve rápido y con facilidad", "Salta y corre sin cansarse."),
        E("Palabra: «refugio». Frase: «Los pajaritos se escondieron en su refugio durante la tormenta». ¿Qué anotas en significado?", "Lugar para protegerse", "Allí se esconden para estar a salvo."),
        E("Ordena los pasos con letras: A) escribir el significado, B) encontrar la palabra nueva, C) buscar pistas en la frase.", "B, C, A", "Primero la encuentro, luego busco pistas y al final anoto."),
    ],
    [
        E("Pedro anotó «sendero = auto». Según la frase «Luna caminó por un sendero angosto», ¿está bien? Explica.", "No, porque se camina por el sendero y es angosto, no un auto", "La frase no habla de un vehículo."),
        E("Ana anotó solo «diminuto», sin significado ni frase. ¿Qué le puede pasar después?", "Puede olvidar qué significa", "Sin significado no sirve para escribir."),
    ],
    [
        E("Texto: «El gato caminó con cautela por el tejado para no resbalar». ¿Qué significa «cautela»?", "Cuidado para evitar un peligro", "Camina con cuidado para no resbalar."),
        arith("Tu banco tiene 4 palabras. Hoy anotas 2 más. ¿Cuántas palabras tiene ahora?", "4+2", "Se suman las nuevas a las que ya tenía."),
    ],
    [E("Tu profesora lee: «Los pájaros construyeron su refugio entre las ramas». No conoces «refugio». ¿Qué dos cosas anotas junto a la palabra?", "El significado y la frase en que la encontré", "Con las dos puedes recordar y usar la palabra.")],
    [
        E("¿Qué parte del texto me ayuda a descubrir el significado de una palabra nueva?", "Las pistas de la frase", "Las palabras vecinas dan información."),
        E("¿Cuántas cosas escribo en mi banco por cada palabra: dos o tres?", "Tres", "Palabra, frase y significado."),
        E("Si no entiendo una palabra aunque busque pistas, ¿qué puedo hacer?", "Preguntar o usar un diccionario", "Hay otras fuentes para averiguarla."),
    ],
    ("Lee este texto y arma un banco de palabras con tres palabras nuevas. Texto: «Al amanecer, un zorro ágil salió de su refugio. Avanzó con cautela por un sendero angosto. Cuando el sol empezó a resplandecer, se escondió». Para cada palabra escribe: palabra, frase y significado. Ayuda: resplandecer significa brillar mucho.",
     "ágil · «un zorro ágil salió de su refugio» · que se mueve rápido y con facilidad; cautela · «Avanzó con cautela» · cuidado para evitar un peligro; resplandecer · «el sol empezó a resplandecer» · brillar mucho.",
     ["anota tres palabras", "escribe la frase", "escribe el significado correcto"], ["hoja con tres filas: palabra, frase y significado"], ["copiar solo la palabra", "inventar un significado sin mirar las pistas"],
     "Pregunta: «¿Qué pista de la frase te ayudó?». Si el significado es incorrecto, vuelve a leer la frase juntos."),
    "Anota en una hoja dos palabras nuevas que escuches hoy en casa.",
    "Arma un banco de palabras con cinco palabras de un cuento y su significado.",
)

# ================================================================ OA 18 · clase 2
reg(
    OA18, 2,
    "Las frases de este cuaderno, lápiz y hoja. Un adulto puede leer las frases en voz alta.",
    "Aprenderé a elegir, entre palabras parecidas, la que dice exactamente lo que quiero. Sirve para escribir con precisión.",
    ["Sé que hay palabras con significados parecidos.", "Tengo un banco de palabras."],
    [
        "Algunas palabras se parecen, pero no dicen lo mismo. «Cansado» y «agotado» hablan de cansancio, pero «agotado» es mucho más. Esa pequeña diferencia se llama matiz. Elegir bien el matiz hace que tu texto sea más preciso.",
        "Mira estos pares: mojado y empapado; pequeño y diminuto; luz fuerte y luz tenue. En cada par, las palabras tienen distinto matiz: «empapado» es más mojado que «mojado», «diminuto» es más pequeño que «pequeño» y «tenue» es una luz más débil que una luz fuerte. También hay tres grados: húmedo, mojado y empapado. Para elegir, pregúntate cuánto o cómo fue lo que quiero contar.",
        "Por ejemplo, si llovió toda la tarde y los zapatos goteaban, «empapados» dice mejor que «mojados». Si solo cayeron unas gotas, «mojados» es suficiente. La mejor palabra es la que encaja con lo que ocurrió.",
    ],
    [("matiz", "pequeña diferencia entre palabras parecidas"), ("empapado", "muy mojado"), ("agotado", "muy cansado"), ("tenue", "poco fuerte o débil, como una luz suave"), ("veloz", "muy rápido")],
    [
        ("Elegir entre mojado y empapado", "Llovió toda la tarde y mis zapatos goteaban. ¿Qué palabra encaja mejor: mojados o empapados?", ["Veo la pista: «toda la tarde» y «goteaban».", "Eso es muy mojado."], "Empapados."),
        ("Elegir entre pequeño y diminuto", "Una hormiga es casi imposible de ver. ¿Qué palabra dice mejor su tamaño: pequeña o diminuta?", ["La pista es «casi imposible de ver».", "Eso es más que pequeña."], "Diminuta."),
    ],
    [("Elegir siempre la palabra más difícil.", "Se piensa que suena mejor.", "Elige la que encaje con lo que pasó."), ("Pensar que dos palabras parecidas son iguales.", "No se mira el matiz.", "Compara cuánto o cómo dice cada una.")],
    [
        E("¿Cuál significa más cansancio: cansado o agotado?", "Agotado", "Agotado es muy cansado."),
        E("¿Cuál significa muy mojado: mojado o empapado?", "Empapado", "Empapado quiere decir muy mojado."),
        E("Llovió muchísimo. Completa: «Mis zapatos quedaron ___». Opciones: mojados o empapados.", "Empapados", "Llovió muchísimo, así que quedaron muy mojados."),
    ],
    [
        E("¿Qué es un matiz?", "Una pequeña diferencia entre palabras parecidas", "Dos palabras pueden parecerse pero no ser iguales."),
        E("«La hormiga es muy pequeña, casi imposible de ver.» ¿Cuál encaja: pequeña o diminuta?", "Diminuta", "Casi imposible de ver indica algo mínimo."),
        E("Juan corrió un poco rápido y Ana corrió muy rápido. ¿A quién le queda mejor «veloz»?", "A Ana", "Veloz significa muy rápido."),
    ],
    [
        E("«Después de correr diez kilómetros quedé ___». Opciones: cansado o agotado.", "Agotado", "Diez kilómetros es un esfuerzo grande."),
        E("«La luz de la vela era ___: casi no alumbraba.» Opciones: tenue o fuerte.", "Tenue", "Casi no alumbraba indica poca luz."),
        E("«El abuelo ___ despacio y tranquilo por la plaza.» ¿Qué verbo encaja mejor: pasea o corre?", "Pasea", "Pasear es caminar sin apuro."),
    ],
    [
        E("¿Por qué no siempre conviene usar la palabra más difícil?", "Porque debe encajar con lo que quiero decir", "La palabra elegida debe decir lo que ocurrió."),
        E("Sofía escribió: «Mi gato adulto tiene un tamaño diminuto». Es un gato de tamaño normal. ¿Encaja «diminuto»?", "No", "Diminuto es muy pequeño y un gato normal no lo es."),
    ],
    [
        E("Ordena de menos a más mojado: empapado, húmedo, mojado.", "Húmedo, mojado, empapado", "Húmedo es poco, mojado más y empapado muchísimo."),
        arith("En tu grupo de palabras de «cansancio» hay cansado, agotado y rendido. Agregas fatigado. ¿Cuántas palabras tiene el grupo?", "3+1", "Se agrega una a las tres que había."),
    ],
    [E("Escribes sobre una tormenta y quieres decir que tu ropa quedó muy mojada. ¿Qué palabra eliges: mojada o empapada?", "Empapada", "La tormenta moja muchísimo la ropa.")],
    [
        E("¿Dos palabras parecidas dicen siempre exactamente lo mismo?", "No", "Pueden tener distinto matiz."),
        E("Para elegir la palabra, ¿qué miro: lo que ocurrió o cuán difícil suena?", "Lo que ocurrió", "La palabra debe encajar con los hechos."),
        E("¿Qué luz es más débil: una luz «tenue» o una luz «fuerte»?", "La luz tenue", "Tenue es suave y débil."),
    ],
    ("Completa cada oración con la palabra que mejor encaja y escribe en una línea por qué la elegiste. Oración 1: «Tras la carrera, el perro quedó ___» (cansado o agotado), pues corrió todo el día. Oración 2: «La luz del pasillo era ___» (tenue o fuerte), pues casi no se veía. Oración 3: «El bichito era ___» (pequeño o diminuto), pues se veía solo con lupa.",
     "1) agotado, porque corrió todo el día. 2) tenue, porque casi no se veía. 3) diminuto, porque solo se veía con lupa.",
     ["elige la palabra con mayor matiz cuando corresponde", "explica con una pista de la oración", "escribe oraciones completas"], ["hoja con tres oraciones completadas y tres razones"], ["elegir por azar", "no dar una razón"],
     "Pide que lea cada oración con la otra palabra y diga si el sentido cambia."),
    "Piensa en dos palabras parecidas y explica en voz alta en qué se diferencian.",
    "Escribe una pareja de palabras con distinto matiz y una oración con cada una.",
)

# ================================================================ OA 18 · clase 3
reg(
    OA18, 3,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé a probar una palabra nueva en otra oración para ver si la entiendo. Sirve para usarla bien cuando escriba.",
    ["Tengo palabras nuevas en mi banco.", "Sé qué es una oración con sentido."],
    [
        "Para usar bien una palabra nueva, hay que probarla en otra oración. Si la escribo en una frase distinta a la del texto y tiene sentido, es porque entendí qué significa. Si la oración queda extraña, necesito revisar el significado.",
        "Haz tres pasos. Primero, recuerda lo que significa la palabra. Segundo, escribe una oración nueva con ella. Tercero, léela y pregúntate: ¿tiene sentido?, ¿dice lo que quise decir? Eso se llama pertinencia: que la palabra encaje.",
        "Por ejemplo, «ágil» significa que se mueve rápido y con facilidad. «El pez ágil nadó entre las rocas» tiene sentido. «La mesa ágil está en la cocina» no tiene sentido, porque una mesa no se mueve.",
    ],
    [("pertinencia", "que una palabra encaje bien en la oración"), ("probar", "usar algo para ver si funciona"), ("ágil", "que se mueve rápido y con facilidad"), ("cautela", "cuidado para evitar un peligro"), ("refugio", "lugar para protegerse")],
    [
        ("Probar «ágil»", "Prueba «ágil» en esta oración: «El pez ágil nadó entre las rocas». ¿Tiene sentido?", ["Recuerdo: ágil es que se mueve rápido y con facilidad.", "Un pez nadando entre rocas se mueve.", "La oración tiene sentido."], "Sí, tiene sentido."),
        ("Probar «refugio»", "Prueba «refugio» en esta oración: «Me comí un refugio rico». ¿Tiene sentido?", ["Recuerdo: refugio es un lugar para protegerse.", "Un lugar no se come.", "La oración no tiene sentido."], "No, no tiene sentido."),
    ],
    [("Copiar la misma oración del texto.", "Se cree que probar es repetir.", "Escribe una oración distinta con la palabra."), ("Usar la palabra sin pensar en su significado.", "Se quiere cumplir con la tarea.", "Recuerda el significado antes de escribir.")],
    [
        E("¿Tiene sentido: «El pez ágil nadó rápido entre las rocas»?", "Sí", "Un pez puede ser ágil."),
        E("¿Tiene sentido: «La mesa es muy cautela»?", "No", "Cautela no describe una mesa."),
        E("Palabra: refugio. ¿Qué oración la usa bien: a) «Me guardé en el refugio cuando llovió» o b) «Me comí un refugio rico»?", "a", "Un refugio protege de la lluvia."),
    ],
    [
        E("¿Qué hago para probar una palabra nueva?", "La escribo en otra oración y reviso si tiene sentido", "Así compruebo que la entiendo."),
        E("«La niña caminó con cautela sobre el hielo.» ¿Qué significa «con cautela»: con cuidado o con prisa?", "Con cuidado", "El hielo resbala y exige cuidado."),
        E("¿Por qué la oración de prueba debe ser distinta a la del texto?", "Para comprobar que entiendo la palabra y no solo la copio", "Una oración nueva muestra comprensión."),
    ],
    [
        E("Completa: «El insecto ___ cabía en una gota». Opciones: diminuto o ágil.", "Diminuto", "Cabe en una gota porque es muy pequeño."),
        E("¿Qué oración usa mal «resplandecer»: a) «El sol resplandece en el mar» o b) «La tarea resplandece en mi mochila»?", "b", "Una tarea en la mochila no brilla."),
        E("¿Cuál oración sirve para decir dónde se escondió un conejo: a) «El conejo corrió a su refugio bajo la tierra» o b) «El conejo comió refugio»?", "a", "Un refugio es un lugar donde esconderse."),
    ],
    [
        E("Samuel escribió: «Mi abuelo es muy ágil porque no puede caminar». ¿Está bien usada «ágil»? Explica.", "No, porque ágil es moverse con facilidad y la frase dice lo contrario", "Hay una contradicción con el significado."),
        E("¿Puede «cautela» reemplazar a «cuidado» en «Cruza la calle con ___»?", "Sí", "Con cautela es con cuidado."),
    ],
    [
        E("Escribe V (verdadero) o F (falso): 1) Un refugio protege. 2) Caminar con cautela es caminar sin mirar. 3) Un camino diminuto es muy grande.", "1 V, 2 F, 3 F", "Un refugio protege; cautela es cuidado y diminuto es muy pequeño."),
        arith("De 5 oraciones con la palabra «ágil», 4 tienen sentido. ¿Cuántas no tienen sentido?", "5-4", "Se resta las correctas del total."),
    ],
    [E("Un compañero escribió: «La tortuga ágil se demoró toda la tarde en dar un solo paso». ¿Está bien usada la palabra «ágil»?", "No, porque la oración muestra lo contrario de moverse rápido y con facilidad", "Dar un paso en toda la tarde no es ser ágil.")],
    [
        E("¿Qué es la pertinencia de una palabra?", "Que encaje bien en la oración", "La palabra debe tener sentido."),
        E("Si una oración con la palabra nueva queda rara, ¿qué debo revisar?", "El significado de la palabra", "Quizás no la entendí bien."),
        E("¿Cuántos pasos tiene probar una palabra: tres o diez?", "Tres", "Recordar, escribir y comprobar."),
    ],
    ("Escribe una oración nueva (distinta a las del cuaderno) con cada una de estas tres palabras y comprueba que tengan sentido: refugio (lugar para protegerse), ágil (se mueve rápido y con facilidad) y cautela (cuidado para evitar un peligro). Después lee tus oraciones en voz alta.",
     "Refugio: Los osos duermen en su refugio durante el invierno. Ágil: Mi gata ágil saltó al estante. Cautela: Crucé el puente con cautela.",
     ["escribe tres oraciones distintas", "cada palabra tiene sentido en su oración", "las oraciones no copian las del cuaderno"], ["hoja con tres oraciones"], ["copiar la oración del texto", "usar la palabra con otro significado"],
     "Pide que explique con sus palabras qué significa cada palabra; luego revisa si la oración lo muestra."),
    "Escribe una oración con la palabra «diminuto» y léela en voz alta.",
    "Escribe dos oraciones con una palabra nueva: una correcta y una que no tenga sentido, y explica la diferencia.",
)

# ================================================================ OA 18 · clase 4
reg(
    OA18, 4,
    "El borrador y el banco de palabras de este cuaderno, lápiz y hoja.",
    "Aprenderé a poner una palabra nueva en mi borrador sin cambiar lo que quería decir. Sirve para escribir con más precisión.",
    ["Sé probar una palabra nueva en una oración.", "Sé escribir un borrador."],
    [
        "Cuando ya entiendes una palabra nueva, puedes integrarla en tu borrador. Integrar es ponerla en tu texto de modo natural, sin cambiar lo que querías decir. La palabra debe hacer que el texto sea más preciso.",
        "Primero lee tu borrador y busca una parte donde la palabra encaje. Por ejemplo, en «Caminé por un camino angosto del bosque», puedes usar «sendero»: «Caminé por un sendero del bosque». Dice lo mismo, pero con una palabra más precisa.",
        "No uses muchas palabras nuevas en una sola oración, porque queda forzada. Usa una o dos donde realmente ayuden. Después lee la oración para comprobar que suena bien.",
    ],
    [("integrar", "poner algo dentro de un texto de forma natural"), ("natural", "que no suena forzado"), ("sendero", "camino angosto"), ("refugio", "lugar para protegerse"), ("resplandecer", "brillar mucho")],
    [
        ("Integrar «sendero»", "Mejora con la palabra «sendero»: «Salimos por un camino angosto del bosque».", ["«Camino angosto» significa sendero.", "Cambio esas palabras por «sendero»."], "Salimos por un sendero del bosque."),
        ("Integrar «refugio»", "Mejora con la palabra «refugio»: «Los pájaros se escondieron de la lluvia en un lugar».", ["Busco dónde se escondieron.", "«Refugio» dice lugar para protegerse.", "Escribo «su refugio»."], "Los pájaros se escondieron de la lluvia en su refugio."),
    ],
    [("Poner muchas palabras nuevas en una oración.", "Se quiere mostrar todo lo que se aprendió.", "Usa solo las que ayuden de verdad."), ("Cambiar el sentido de lo que se quería decir.", "No se relee la oración nueva.", "Compara la versión nueva con la anterior.")],
    [
        E("Completa: «Caminamos por un ___ entre los árboles». Banco: sendero o refugio.", "sendero", "Se camina por un camino angosto."),
        E("Completa: «Los conejos se escondieron en su ___ cuando llovió». Banco: refugio o cautela.", "refugio", "Es el lugar donde se protegen."),
        E("Completa: «El sol parecía ___ sobre el mar». Banco: resplandecer o esconderse.", "resplandecer", "El sol brilla mucho sobre el mar."),
    ],
    [
        E("En «El gato caminó por el techo», ¿qué palabra del banco dice que caminó con cuidado: cautela o refugio?", "Cautela", "Se puede escribir «caminó con cautela»."),
        E("¿Conviene usar todas las palabras nuevas en una sola oración?", "No", "Así la oración queda forzada."),
        E("Una palabra bien integrada, ¿dice lo que quería decir con más precisión o cambia todo?", "Lo dice con más precisión", "Integrar no cambia la idea."),
    ],
    [
        E("Reescribe «Salimos por un camino angosto del bosque» usando «sendero».", "Salimos por un sendero del bosque.", "Se reemplaza «camino angosto» por «sendero»."),
        E("Reescribe «Los pájaros se escondieron de la lluvia en un lugar» usando «refugio».", "Los pájaros se escondieron de la lluvia en su refugio.", "Refugio es el lugar donde se protegen."),
        E("Agrega «resplandecer» a «La luna brillaba mucho sobre el lago».", "La luna resplandecía sobre el lago.", "Resplandecer significa brillar mucho."),
    ],
    [
        E("Pablo escribió: «Mi cumpleaños fue sendero y refugio y cautela y resplandecer». ¿Por qué no funciona?", "Porque usa las palabras sin sentido y todas juntas", "Las palabras deben encajar y no amontonarse."),
        E("Elena cambió «mi gato» por «mi cautela». ¿Funciona?", "No", "Cautela no es un animal y cambia el sentido."),
    ],
    [
        E("Borrador: «Fui al bosque. Caminé por un camino angosto. Vi un lugar para esconderme». ¿Qué dos palabras del banco puedes usar?", "sendero y refugio", "Reemplazan camino angosto y lugar para esconderse."),
        arith("Tu borrador tiene 4 oraciones y integras una palabra nueva en 1 de ellas. ¿En cuántas oraciones no hiciste cambios?", "4-1", "Se resta la oración cambiada del total."),
    ],
    [E("La profesora te pide agregar una palabra nueva a «Los patitos se escondieron cuando llovió». Usa «refugio».", "Los patitos se escondieron en su refugio cuando llovió.", "Refugio dice dónde se protegieron.")],
    [
        E("¿Qué debo hacer después de integrar una palabra: releer o guardar sin mirar?", "Releer", "Hay que comprobar que suena bien."),
        E("¿Integrar una palabra puede hacer el texto más preciso?", "Sí", "Una palabra exacta dice mejor la idea."),
        E("Si la palabra nueva no encaja en ninguna parte, ¿la obligo a entrar?", "No", "Forzar una palabra empeora el texto."),
    ],
    ("Mejora este borrador integrando dos palabras de este banco: sendero (camino angosto), cautela (cuidado para evitar un peligro), refugio (lugar para protegerse), resplandecer (brillar mucho). Borrador: «Fui con mi papá al cerro. Caminamos por un camino angosto. Al llegar vimos una casita donde guardarnos de la lluvia. El sol brillaba mucho». Reescríbelo.",
     "Fui con mi papá al cerro. Caminamos por un sendero. Al llegar vimos un refugio para protegernos de la lluvia. El sol resplandecía.",
     ["usa al menos dos palabras del banco", "las palabras encajan", "la idea es la misma"], ["borrador reescrito con las palabras subrayadas"], ["usar las cuatro palabras forzadas", "cambiar lo que pasa en la historia"],
     "Pide que explique en qué parte quedó mejor su texto y cómo lo comprobó."),
    "Elige una palabra de tu banco y úsala en una oración nueva sobre tu día.",
    "Reescribe un texto tuyo con dos palabras del banco y compara las dos versiones.",
)

# ================================================================ OA 18 · clase 5
reg(
    OA18, 5,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé a explicar por qué elegí una palabra para mi texto. Sirve para escribir con más seguridad y para convencer a otros de que mi elección es buena.",
    ["Sé elegir entre palabras parecidas.", "Sé integrar una palabra nueva."],
    [
        "Cuando eliges una palabra para tu texto, puedes explicar por qué. Explicar una decisión es decir la palabra que elegiste y la razón. Una razón es lo que hace que la palabra encaje mejor que otras.",
        "Usa esta forma: «Elegí (palabra) porque (razón)». Por ejemplo: «Elegí diminuta porque la hormiga es muy pequeña». La razón debe hablar del significado, no de si la palabra te gusta o suena bonita.",
        "Explicar tu decisión te ayuda a revisar si de verdad es la mejor. Si no encuentras una buena razón, quizás debas probar otra palabra.",
    ],
    [("decisión", "elección que hago después de pensar"), ("razón", "motivo que explica por qué hice algo"), ("porque", "palabra que anuncia la razón"), ("pertinente", "que encaja con lo que quiero decir"), ("justificar", "dar razones de lo que elegí")],
    [
        ("Explicar la elección de una palabra", "Elegí «diminuta» para «La hormiga es ___». Explica por qué.", ["Escribo la palabra elegida.", "Digo qué significa y cómo encaja: es muy pequeña."], "Elegí diminuta porque la hormiga es muy pequeña."),
        ("Explicar otra elección", "Elegí «empapados» para «Mis zapatos quedaron ___» porque llovió toda la tarde. Escribe la explicación completa.", ["Uso la forma «Elegí… porque…».", "La razón es que llovió mucho."], "Elegí empapados porque llovió toda la tarde y quedaron muy mojados."),
    ],
    [("Decir «porque sí» o «porque me gusta».", "No se piensa en el significado.", "Explica con lo que significa la palabra."), ("Escribir solo la palabra, sin razón.", "Se cree que la palabra se explica sola.", "Agrega «porque…» y una razón.")],
    [
        E("Completa con la palabra que falta: «Elegí cautela ___ quería decir que caminó con cuidado».", "porque", "«Porque» anuncia la razón."),
        E("¿Qué parte de «Elegí empapados porque llovió mucho» dice la razón?", "porque llovió mucho", "Es lo que explica la elección."),
        E("Una explicación completa, ¿debe decir la palabra y la razón?", "Sí", "Con las dos partes se entiende."),
    ],
    [
        E("¿Cuál es una buena explicación: a) «Elegí diminuto porque el bicho era muy pequeño» o b) «Elegí diminuto porque sí»?", "a", "La a da una razón sobre el significado."),
        E("¿Por qué conviene decir la razón de mi elección?", "Para que el lector entienda mi decisión", "La razón la hace comprensible."),
        E("«Pertinente» significa que encaja con lo que quiero decir. ¿Es pertinente «diminuto» para un elefante?", "No", "Un elefante es enorme."),
    ],
    [
        E("Escribe una explicación completa para elegir «diminuta» en «La hormiga es ___» (diminuta o enorme).", "Elegí diminuta porque la hormiga es muy pequeña.", "Dice la palabra y el motivo."),
        E("Completa: «Elegí empapados porque ____». Contexto: llovió toda la tarde y los zapatos goteaban.", "los zapatos quedaron muy mojados", "Eso es lo que significa empapado."),
        E("Ordena: A) porque la luz casi no alumbraba, B) Elegí tenue.", "B, A", "Primero la palabra y luego la razón."),
    ],
    [
        E("Pedro explica: «Elegí agotado porque me gusta cómo suena». ¿Es una buena razón?", "No, porque la razón debe hablar del significado", "Suena bonito, pero no dice nada del sentido."),
        E("Dos niñas eligen palabras distintas para «La luz de la vela es ___»: tenue y débil. ¿Pueden ser buenas las dos elecciones?", "Sí, si explican que casi no alumbra", "Ambas se explican con el mismo sentido."),
    ],
    [
        E("Elige y explica: «Corrió diez kilómetros y apenas podía caminar». ¿Cansado o agotado? Escribe la explicación completa.", "Elegí agotado porque quedó sin fuerzas.", "Agotado es más fuerte que cansado."),
        arith("Una explicación completa tiene 2 partes: la palabra elegida y la razón. Ya escribiste la palabra. ¿Cuántas partes faltan?", "2-1", "Falta una parte: la razón."),
    ],
    [E("En clase, la profesora pregunta por qué usaste «refugio» en «Los conejos corrieron a su refugio». ¿Qué respondes?", "Usé refugio porque es el lugar donde se protegen", "Refugio significa lugar para protegerse.")],
    [
        E("¿Qué palabra anuncia la razón en una explicación?", "Porque", "Esa palabra une la elección con su motivo."),
        E("Si no encuentro una buena razón para mi palabra, ¿qué hago?", "Pruebo con otra palabra", "Una palabra sin razón no es la mejor."),
        E("¿La razón habla del significado o de si me gusta?", "Del significado", "La razón debe justificar el sentido."),
   ],
    ("Para cada oración elige una palabra y explica tu decisión con «Elegí… porque…». Oración 1: «El puente era ___» (viejo o antiguo; antiguo es de hace muchísimos años): el puente tenía muchos siglos. Oración 2: «Mi mochila quedó ___ con la lluvia» (mojada o empapada): estaba goteando. Oración 3: «Mi hermano está ___» (cansado o agotado): se sentó a descansar un rato.",
     "1) Elegí antiguo porque tenía muchos siglos. 2) Elegí empapada porque estaba goteando. 3) Elegí cansado porque solo se sentó a descansar un rato.",
     ["elige una palabra por oración", "usa «porque»", "la razón habla del significado"], ["tres explicaciones escritas"], ["decir «porque me gusta»", "no incluir la razón"],
     "Cuando la razón sea débil, pregunta: «¿Qué dice la oración que te hizo elegir esa palabra?»."),
    "Cuéntale a alguien por qué elegiste una palabra en un texto tuyo.",
    "Elige dos palabras para la misma oración, explica ambas y di cuál prefieres.",
)

# ================================================================ OA 19 · clase 1
reg(
    OA19, 1,
    "Las oraciones de este cuaderno, lápiz y hoja. Pueden usarse tarjetas de papel con palabras.",
    "Aprenderé qué son los sustantivos y a reconocerlos en una oración. Sirve para saber qué palabras nombran personas, animales, cosas y lugares.",
    ["Sé leer oraciones cortas.", "Sé que las palabras tienen distintas funciones."],
    [
        "Los sustantivos son palabras que nombran personas, animales, cosas y lugares. «Niño», «perro», «mesa» y «plaza» son sustantivos. También lo son los nombres propios, como Camila.",
        "Para encontrar un sustantivo pregúntate: ¿esta palabra nombra a alguien o a algo? En «El perro corre en la plaza», «perro» nombra un animal y «plaza» nombra un lugar. «Corre» dice qué hace el perro, por eso no es sustantivo.",
        "Reconocer sustantivos sirve para escribir con precisión. Si cambias el sustantivo, cambias de qué habla la oración. «El gato corre» y «El perro corre» no dicen lo mismo.",
    ],
    [("sustantivo", "palabra que nombra personas, animales, cosas o lugares"), ("nombre propio", "sustantivo que nombra a una persona o lugar en particular"), ("oración", "palabras que dicen una idea completa"), ("persona", "ser humano"), ("lugar", "sitio donde algo está o sucede")],
    [
        ("Encontrar sustantivos", "Busca los sustantivos de «El perro corre en la plaza».", ["Pregunto qué palabras nombran algo.", "«Perro» nombra un animal.", "«Plaza» nombra un lugar.", "«Corre» dice lo que hace."], "Los sustantivos son perro y plaza."),
        ("Distinguir un sustantivo de otras palabras", "En «La niña come una manzana», ¿cuáles son sustantivos?", ["«Niña» nombra una persona.", "«Manzana» nombra una cosa."], "Niña y manzana."),
    ],
    [("Pensar que una acción es sustantivo.", "Se confunde nombrar con hacer.", "Si dice qué hace alguien, no es sustantivo."), ("Olvidar los nombres propios.", "Se cree que solo son sustantivos las cosas.", "Los nombres de personas y lugares también son sustantivos.")],
    [
        E("¿Cuál nombra un animal: gato o correr?", "gato", "Gato nombra un animal."),
        E("Un sustantivo, ¿nombra algo o dice cómo es algo?", "Nombra algo", "Nombra personas, animales, cosas o lugares."),
        E("En «La niña come una manzana», ¿qué sustantivo nombra una fruta?", "manzana", "Una manzana es una fruta."),
    ],
    [
        E("En «El perro corre en la plaza», ¿cuáles son los sustantivos?", "perro y plaza", "Nombran un animal y un lugar."),
        E("¿Cuál de estas palabras es sustantivo: saltar, mesa o rojo?", "mesa", "Mesa nombra una cosa."),
        E("¿«Profesora» nombra una persona, un animal o un lugar?", "Una persona", "La profesora es alguien."),
    ],
    [
        E("Encuentra los sustantivos de «Mi hermano guardó el balón en la mochila».", "hermano, balón y mochila", "Nombran una persona y dos cosas."),
        E("Completa con un sustantivo: «Los niños juegan en el ___». Opciones: patio, correr o rápido.", "patio", "Es un lugar donde se juega."),
        E("¿Cuántos sustantivos hay en «El gato duerme en la cama del niño»?", "3", "Gato, cama y niño."),
    ],
    [
        E("Ana cree que «rápido» es sustantivo. ¿Tiene razón?", "No, porque dice cómo es algo y no lo nombra", "Rápido describe, no nombra."),
        E("En «Los pájaros cantan en el árbol», Tomás dice que hay dos sustantivos. ¿Cuáles son?", "pájaros y árbol", "Nombran animales y una planta."),
    ],
    [
        E("Encuentra los sustantivos de «La abuela de Camila prepara pan en la cocina».", "abuela, Camila, pan y cocina", "Nombran personas, una cosa y un lugar."),
        arith("«Mi papá pintó la pared» tiene 2 sustantivos. Si agregas «del colegio», que suma el sustantivo «colegio», ¿cuántos sustantivos hay ahora?", "2+1", "Se suma uno más."),
    ],
    [E("Haces la lista de lo que llevas a la escuela. ¿Cuáles de estas palabras son sustantivos: cuaderno, estudiar, lápiz, rápido, goma?", "cuaderno, lápiz y goma", "Nombran objetos; las otras dicen una acción o cómo es algo.")],
    [
        E("¿«Plaza» es un sustantivo?", "Sí", "Nombra un lugar."),
        E("¿Los nombres de personas, como Pedro, son sustantivos?", "Sí", "Son nombres propios."),
        E("En «Luis salta», ¿cuál palabra es sustantivo?", "Luis", "Nombra a una persona."),
    ],
    ("Lee este texto y escribe una lista con todos los sustantivos. Texto: «Sofía vio un conejo en el jardín. El conejo comía una zanahoria. La abuela de Sofía lo miró desde la ventana».",
     "Sofía, conejo, jardín, zanahoria, abuela, ventana.",
     ["encuentra al menos cinco sustantivos", "no incluye verbos", "incluye el nombre propio"], ["lista de sustantivos en la hoja"], ["incluir «vio» o «comía»", "olvidar el nombre propio"],
     "Pide que explique por qué «comía» no está en la lista y qué pregunta se hizo para cada palabra."),
    "Dime cinco sustantivos que veas ahora en tu casa.",
    "Escribe una oración con cuatro sustantivos y subráyalos.",
)

# ================================================================ OA 19 · clase 2
reg(
    OA19, 2,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé qué son los artículos y cómo acompañan al sustantivo. Sirve para escribir y hablar con claridad.",
    ["Sé reconocer un sustantivo.", "Conozco palabras como «el» y «la»."],
    [
        "Los artículos son palabras que van antes del sustantivo y lo acompañan. Hay artículos para hablar de algo conocido: el, la, los, las. Y hay artículos para hablar de algo que no es conocido: un, una, unos, unas.",
        "Los artículos cambian según el sustantivo. Se dice «el perro» y «la mesa». Se dice «los lápices» y «las flores». También se dice «un gato» y «una casa». Fíjate si el sustantivo es de uno o de varios, y si va con «el» o «la».",
        "Para encontrar el artículo, mira la palabra que está justo antes del sustantivo. En «El gato duerme», «el» es el artículo. Sin artículo, las oraciones suenan incompletas: «Gato duerme».",
    ],
    [("artículo", "palabra que acompaña al sustantivo, como el, la, un, una"), ("singular", "uno solo"), ("plural", "más de uno"), ("conocido", "algo de lo que ya sabemos"), ("acompañar", "ir junto a otra palabra")],
    [
        ("Poner el artículo correcto", "Completa con «el» o «la»: ___ mesa.", ["«Mesa» es una sola cosa.", "Se dice «la mesa»."], "La mesa."),
        ("Poner artículos en plural", "Completa con «los» o «las»: ___ flores.", ["«Flores» es más de una.", "Se dice «las flores»."], "Las flores."),
    ],
    [("Decir «la perro».", "Se mezclan los artículos.", "Dilo con el sustantivo: «el perro»."), ("Olvidar el artículo.", "Se escribe como si fuera un aviso.", "Revisa qué palabra va antes del sustantivo.")],
    [
        E("¿Qué artículo va con «perro»: el o la?", "el", "Se dice «el perro»."),
        E("¿Qué artículo va con «flores»: los o las?", "las", "Se dice «las flores»."),
        E("¿Qué artículo va con «casa»: un o una?", "una", "Se dice «una casa»."),
    ],
    [
        E("¿Para qué sirve un artículo?", "Para acompañar al sustantivo", "Va antes del sustantivo."),
        E("En «El gato duerme», ¿cuál es el artículo?", "El", "Va antes de «gato»."),
        E("¿Cuál de estas palabras es un artículo: perro, la o bonito?", "la", "«La» acompaña a un sustantivo."),
    ],
    [
        E("Completa: «Ayer vi ___ película». Opciones: una o uno.", "una", "«Película» es una sola y es femenina."),
        E("Completa: «Mi mamá compró ___ pan». Opciones: un o una.", "un", "«Pan» es masculino y singular."),
        E("Completa: «___ lápices están en la caja». Opciones: los o las.", "Los", "«Lápices» es masculino plural."),
    ],
    [
        E("Pía escribió «la perro». ¿Qué artículo corresponde y por qué?", "El, porque perro es masculino", "Se dice «el perro»."),
        E("¿Sirve «los» para acompañar a «flor»?", "No, porque flor es una sola y femenina; es «la flor»", "Los es plural y masculino."),
    ],
    [
        E("Completa con «el» y «la», en ese orden: «___ gato duerme en ___ cama».", "El gato duerme en la cama.", "«Gato» es masculino y «cama» es femenino."),
        E("¿Cuántos artículos hay en «Los niños comen las manzanas»?", "2", "«Los» y «las»."),
    ],
    [E("En tu lista de útiles falta el artículo: ___ regla, ___ lápices, ___ cuaderno. Completa con la, los y el, en ese orden.", "La regla, los lápices, el cuaderno.", "Cada artículo concuerda con su sustantivo.")],
    [
        E("¿Qué artículo va con «mesas»: las o los?", "las", "Mesas es femenino plural."),
        E("¿El artículo va antes o después del sustantivo?", "Antes", "Acompaña al sustantivo desde adelante."),
        E("¿«Un» se usa con algo conocido o desconocido?", "Con algo desconocido", "«Un» presenta algo nuevo."),
    ],
    ("Completa con el artículo que corresponde y escribe el texto completo. «___ niña tiene ___ perro y ___ gatos. ___ perro se llama Rex». Opciones: la, un, unos, el.",
     "La niña tiene un perro y unos gatos. El perro se llama Rex.",
     ["usa artículos que concuerdan", "lee el texto completo", "separa singular de plural"], ["texto completado"], ["usar «la» con «perro»", "no cambiar a plural"],
     "Lee en voz alta cada frase; si suena raro, revisa el artículo."),
    "Mira tu cuarto y escribe tres cosas con su artículo.",
    "Escribe cuatro oraciones sobre tu familia y subraya los artículos.",
)

# ================================================================ OA 19 · clase 3
reg(
    OA19, 3,
    "Las oraciones de este cuaderno, lápiz y hoja. Objetos de la casa para describir.",
    "Aprenderé qué son los adjetivos y a usarlos para decir cómo son las cosas. Sirve para describir con más precisión.",
    ["Sé reconocer sustantivos.", "Sé que las cosas tienen características."],
    [
        "Los adjetivos son palabras que dicen cómo es un sustantivo. En «el perro negro», «negro» es un adjetivo. Nos dice el color. Los adjetivos pueden decir color, tamaño, forma, sabor o cómo se siente algo.",
        "Los adjetivos ayudan al lector a imaginar. No es lo mismo decir «un perro» que «un perro negro y peludo». En «La casa azul está lejos», «azul» dice cómo es la casa. Si quitas el adjetivo, la oración sigue, pero con menos información.",
        "Para reconocer un adjetivo, pregúntate: ¿esta palabra me dice cómo es algo? Si dice «cómo es», es adjetivo. Si nombra algo, es sustantivo.",
    ],
    [("adjetivo", "palabra que dice cómo es un sustantivo"), ("característica", "algo que describe cómo es una persona o cosa"), ("describir", "decir cómo es algo"), ("peludo", "con mucho pelo"), ("preciso", "que dice exactamente lo que se quiere decir")],
    [
        ("Encontrar el adjetivo", "En «El perro veloz corre», ¿cuál es el adjetivo?", ["Pregunto: ¿cuál palabra dice cómo es el perro?", "Es veloz."], "El adjetivo es veloz."),
        ("Elegir un adjetivo para describir", "Elige un adjetivo para «sopa» que diga la temperatura: caliente o ruidosa.", ["Pienso en la temperatura.", "Una sopa puede estar caliente."], "Caliente."),
    ],
    [("Pensar que «perro» es adjetivo porque lo vemos.", "Se confunde ver con describir.", "Pregunta si la palabra nombra o describe."), ("Usar adjetivos muy generales.", "Se usa siempre «bonito» o «lindo».", "Busca uno más preciso: suave, brillante, jugoso.")],
    [
        E("¿Cuál dice cómo es algo: niña, alta o correr?", "alta", "Describe a la niña."),
        E("En «El perro veloz corre», ¿cuál es el adjetivo?", "veloz", "Dice cómo es el perro."),
        E("¿Para qué sirve un adjetivo?", "Para decir cómo es un sustantivo", "Describe lo que nombra el sustantivo."),
    ],
    [
        E("En «La casa azul está lejos», ¿cuál es el adjetivo?", "azul", "Dice cómo es la casa."),
        E("¿Cuál da más información: «un perro» o «un perro negro y peludo»?", "Un perro negro y peludo", "Tiene dos adjetivos que describen."),
        E("¿Qué adjetivo sirve para el sabor de un limón: ácido o amarillo?", "Ácido", "El sabor se dice con «ácido»; «amarillo» es un color."),
    ],
    [
        E("Completa: «El helado es ___». Opciones: frío, saltar o mesa.", "frío", "Dice cómo es el helado."),
        E("¿Qué adjetivo describe mejor una nube: esponjosa, correr o mesa?", "esponjosa", "Dice cómo parece la nube."),
        E("Para un elefante, ¿es mejor «pequeño» o «enorme»?", "enorme", "Un elefante es muy grande."),
    ],
    [
        E("¿Cuántos adjetivos hay en «La gata pequeña y blanca duerme»?", "2", "Pequeña y blanca."),
        E("Tomás dice que en «el pan caliente» el adjetivo es «pan». Explica el error.", "Pan es sustantivo porque nombra algo; el adjetivo es caliente", "Caliente dice cómo es el pan."),
    ],
    [
        E("Cambia «bonito» por adjetivos más precisos: «Vi un jardín bonito con flores bonitas». Ejemplo de respuesta.", "Vi un jardín colorido con flores perfumadas.", "Colorido y perfumadas dicen más que bonito."),
        arith("En «El libro viejo tiene hojas amarillas y letras pequeñas» hay 3 adjetivos. Si agregas «grande» para el libro, ¿cuántos adjetivos hay?", "3+1", "Se suma un adjetivo más."),
    ],
    [E("Quieres describir tu mochila para que no se pierda. ¿Cuál es el adjetivo en «Mi mochila roja está en el perchero»?", "roja", "Dice el color de la mochila.")],
    [
        E("¿Los adjetivos pueden decir el color de algo?", "Sí", "Por ejemplo, rojo o azul."),
        E("¿«Mesa» es adjetivo?", "No", "Mesa nombra un objeto."),
        E("¿«Suave» sirve para describir un peluche?", "Sí", "Dice cómo se siente."),
    ],
    ("Describe estos tres objetos con dos adjetivos cada uno. Objeto 1: una manzana (sabor y color). Objeto 2: un gato (tamaño y pelaje). Objeto 3: una pelota (forma y color). Escribe una oración por objeto.",
     "La manzana roja es dulce. El gato pequeño tiene pelo suave. La pelota redonda es azul.",
     ["usa dos adjetivos por objeto", "los adjetivos encajan", "forma oraciones completas"], ["tres oraciones con adjetivos subrayados"], ["usar el mismo adjetivo para todo", "usar un sustantivo como adjetivo"],
     "Pide que lea la oración sin los adjetivos y vea cuánta información pierde."),
    "Describe un objeto de tu casa con tres adjetivos distintos.",
    "Elige un animal y escribe cinco adjetivos precisos para describirlo.",
)

# ================================================================ OA 19 · clase 4
reg(
    OA19, 4,
    "Las oraciones de este cuaderno, lápiz y hoja. Tarjetas de papel para mover palabras.",
    "Aprenderé a combinar artículos, sustantivos y adjetivos y a cambiar uno por otro. Sirve para escribir descripciones variadas.",
    ["Sé reconocer artículos, sustantivos y adjetivos.", "Sé armar oraciones."],
    [
        "Un grupo de palabras formado por artículo, sustantivo y adjetivo se llama grupo nominal. Por ejemplo: «la casa blanca». Aquí «la» es el artículo, «casa» el sustantivo y «blanca» el adjetivo.",
        "Puedes cambiar las palabras de un grupo nominal para precisar lo que dices. Si cambias el adjetivo, cambias cómo es: «la casa blanca» pasa a «la casa enorme». Si cambias el sustantivo, cambias de qué hablas: «la casa blanca» pasa a «la torre blanca».",
        "También puedes unir dos oraciones. Por ejemplo, «Tengo un perro. El perro es pequeño» se une así: «Tengo un perro pequeño». Así no repites «perro» y el texto suena mejor.",
    ],
    [("grupo nominal", "artículo, sustantivo y adjetivo juntos, como «la casa blanca»"), ("reemplazar", "cambiar una palabra por otra"), ("combinar", "unir"), ("precisar", "decir con más exactitud"), ("repetir", "decir lo mismo otra vez")],
    [
        ("Reconocer un grupo nominal", "En «las flores rojas», ¿cuál es el artículo, el sustantivo y el adjetivo?", ["Busco la palabra que acompaña: las.", "Busco la que nombra: flores.", "Busco la que describe: rojas."], "Artículo: las; sustantivo: flores; adjetivo: rojas."),
        ("Combinar dos oraciones", "Une: «Vi un pájaro. El pájaro era azul».", ["Veo que «pájaro» se repite.", "Paso «azul» antes o después del sustantivo.", "Escribo una sola oración."], "Vi un pájaro azul."),
    ],
    [("Cambiar el adjetivo y que no tenga sentido.", "No se relee.", "Lee la oración nueva y comprueba."), ("Repetir el sustantivo al unir oraciones.", "Se copia sin pensar.", "Usa una sola vez el sustantivo.")],
    [
        E("¿Cuál es un grupo nominal: «la casa blanca» o «corre rápido»?", "la casa blanca", "Tiene artículo, sustantivo y adjetivo."),
        E("En «el gato negro», ¿cuál es el sustantivo?", "gato", "Nombra el animal."),
        E("¿Qué adjetivo reemplaza a «grande» con más fuerza: enorme o chico?", "enorme", "Enorme es muy grande."),
    ],
    [
        E("Une en una oración: «Tengo un gato. El gato es gordo».", "Tengo un gato gordo.", "Se repite «gato»; se une."),
        E("¿Cuáles son las tres partes de «las flores rojas»?", "las, flores y rojas", "Artículo, sustantivo y adjetivo."),
        E("¿Por qué ayuda combinar oraciones?", "Porque evita repetir palabras", "El texto queda más claro."),
    ],
    [
        E("Reemplaza el sustantivo de «el perro pequeño» por «pájaro».", "El pájaro pequeño.", "Se cambia la palabra que nombra."),
        E("Reemplaza el adjetivo de «la torta grande» por «deliciosa».", "La torta deliciosa.", "Se cambia la palabra que describe."),
        E("Combina: «Tengo una mochila. La mochila es roja».", "Tengo una mochila roja.", "Se une la información."),
    ],
    [
        E("Mara cambió «el niño alto» por «el niña alto». ¿Qué error hay?", "El artículo y el sustantivo no concuerdan; es «la niña alta»", "Niña es femenino y necesita «la» y «alta»."),
        E("¿Por qué «el cuaderno veloz» no tiene sentido?", "Porque un cuaderno no puede ser veloz", "Veloz no describe a un cuaderno."),
    ],
    [
        E("Combina en una oración: «Vi un gato. Era negro. Era pequeño».", "Vi un gato negro y pequeño.", "Se reúnen los dos adjetivos."),
        arith("Tienes el grupo nominal «la casa blanca» (3 palabras). Le agregas el adjetivo «grande». ¿Cuántas palabras tiene ahora?", "3+1", "Se agrega una palabra más."),
    ],
    [E("En tu cuaderno de ciencias combinas: «Vi un caracol. El caracol es lento. El caracol es pequeño». ¿Cómo queda en una sola oración?", "Vi un caracol lento y pequeño.", "Se unen los datos sin repetir el sustantivo.")],
    [
        E("¿Qué cambia si reemplazo un adjetivo?", "Cómo es lo que describo", "El adjetivo dice cómo es."),
        E("¿Qué cambia si reemplazo un sustantivo?", "De qué hablo", "El sustantivo nombra lo que describo."),
        E("¿Un grupo nominal puede tener dos adjetivos?", "Sí", "Por ejemplo, «el perro negro y pequeño»."),
    ],
    ("Haz estos tres cambios. 1) Combina «Tengo un perro. El perro es peludo» en una sola oración. 2) Reemplaza el adjetivo de «la casa blanca» por «enorme». 3) Reemplaza el sustantivo de «la casa blanca» por «torre».",
     "1) Tengo un perro peludo. 2) La casa enorme. 3) La torre blanca.",
     ["combina sin repetir", "reemplaza el adjetivo", "reemplaza el sustantivo y mantiene la concordancia"], ["tres respuestas escritas"], ["repetir la palabra «perro»", "no cambiar la palabra pedida"],
     "Pide que lea las respuestas y diga qué cambió en cada una."),
    "Cambia el adjetivo de «el sol caliente» por otro y di cómo cambió.",
    "Escribe un grupo nominal y haz con él cinco cambios distintos.",
)

# ================================================================ OA 19 · clase 5
reg(
    OA19, 5,
    "Las oraciones de este cuaderno, lápiz y hoja. Un objeto de la casa para describir.",
    "Aprenderé a escribir descripciones pensando en el lector. Sirve para que otra persona imagine lo que quiero mostrar.",
    ["Sé usar artículos, sustantivos y adjetivos.", "Sé combinar y reemplazar palabras."],
    [
        "Cuando describes algo, escribes para un lector. El lector no ve lo que tú ves, así que necesita palabras que se lo muestren. Los adjetivos le dicen cómo es lo que describes.",
        "Elige bien tus palabras. Si el lector es un niño pequeño, usa palabras simples. Usa adjetivos precisos: no «cosa bonita» sino «caracol lento y brillante». Usa artículos correctos para que se entienda de qué hablas: «el caracol», «una piedra».",
        "Después de escribir, imagina que eres el lector. ¿Puedes ver lo que describiste? Si no, agrega más información. Una buena descripción permite adivinar el objeto sin verlo.",
    ],
    [("lector", "persona que lee un texto"), ("descripción", "texto que dice cómo es algo"), ("imaginar", "formar una imagen en la mente"), ("detalle", "dato pequeño que agrega información"), ("adivinar", "descubrir algo sin que lo digan")],
    [
        ("Adivinar con una descripción", "Lee: «Es un animal grande y gris. Tiene trompa larga y orejas enormes». ¿Qué animal es?", ["Busco los adjetivos: grande, gris, larga, enormes.", "Pienso qué animal tiene trompa y es gris."], "Es un elefante."),
        ("Escribir para un lector", "Describe un limón para que alguien lo reconozca.", ["Pienso en su color, forma y sabor.", "Escribo con artículo, sustantivo y adjetivos."], "El limón es amarillo, ovalado y muy ácido."),
    ],
    [("Escribir «es bonito» sin decir cómo.", "Se piensa que el lector sabe cómo es.", "Usa adjetivos que digan color, forma, tamaño o sabor."), ("Usar palabras muy difíciles.", "Se quiere impresionar.", "Usa palabras que tu lector entienda.")],
    [
        E("¿Para qué escribimos una descripción?", "Para que el lector imagine cómo es algo", "El lector no ve lo que yo veo."),
        E("¿Cuál da más información: «una flor» o «una flor amarilla»?", "Una flor amarilla", "El adjetivo dice cómo es."),
        E("¿Quién es el lector?", "La persona que lee el texto", "Es quien recibe lo que escribo."),
    ],
    [
        E("«Es un animal grande, gris y tiene trompa.» ¿Qué animal es?", "Elefante", "Solo el elefante tiene trompa y es grande y gris."),
        E("En «El gato pequeño y blanco duerme», ¿cuáles son los adjetivos?", "pequeño y blanco", "Dicen cómo es el gato."),
        E("Si el lector es un niño de 6 años, ¿uso palabras muy difíciles?", "No", "Debe entender lo que leo."),
    ],
    [
        E("Completa para que el lector adivine una pelota: «Es un objeto ___ y rueda». Opciones: redondo o cuadrado.", "redondo", "Una pelota es redonda."),
        E("Ordena para describir, empezando con «sobre la mesa»: sobre la mesa / hay / una / manzana / roja.", "Sobre la mesa hay una manzana roja.", "Se ordenan las palabras para formar una oración."),
        E("¿Qué dos adjetivos tiene «El sol caliente y brillante»?", "caliente y brillante", "Describen al sol."),
    ],
    [
        E("Un lector no sabe qué animal es: «Es un animal». ¿Qué le falta?", "Adjetivos que digan cómo es", "No hay detalles para adivinar."),
        E("Dos descripciones del mismo gato: A «Tiene pelo.» B «Tiene pelo largo, suave y gris.» ¿Cuál ayuda más a imaginarlo?", "B", "Tiene tres adjetivos."),
    ],
    [
        E("Escribe una oración para un lector que no vio tu mochila: es azul y grande.", "La mochila es azul y grande.", "Usa artículo, sustantivo y dos adjetivos."),
        E("Cuenta los adjetivos: «La casa antigua tiene una puerta verde y ventanas pequeñas».", "3", "Antigua, verde y pequeñas."),
    ],
    [E("Perdiste un lápiz en la sala y haces un cartel. Es rojo, corto y con goma blanca. Escribe la oración.", "Perdí un lápiz rojo y corto con goma blanca.", "Los adjetivos ayudan a encontrar el lápiz.")],
    [
        E("¿Qué hago después de escribir una descripción: imagino ser el lector o la guardo?", "Imagino ser el lector", "Así compruebo si se entiende."),
        E("¿Una buena descripción permite adivinar el objeto?", "Sí", "Tiene suficientes detalles."),
        E("¿Qué agrego si mi lector no puede imaginar lo que describí?", "Más detalles y adjetivos", "Así tendrá más información."),
    ],
    ("Elige un objeto de tu casa (una taza, un zapato o una fruta). Escribe una descripción de tres oraciones con artículo, sustantivo y al menos cuatro adjetivos, sin decir el nombre del objeto. Pídele a alguien que adivine qué es. Ejemplo para guiarte: «Es un objeto redondo y liso. Tiene un asa pequeña. Sirve para tomar algo caliente».",
     "«Es una fruta redonda y roja. Tiene la cáscara lisa y brillante. Es dulce y jugosa». (Es una manzana).",
     ["usa al menos cuatro adjetivos", "las oraciones se entienden", "el lector puede adivinar el objeto"], ["hoja con tres oraciones y el objeto adivinado"], ["decir solo «es bonito»", "no usar adjetivos que describan"],
     "Pregunta: «¿Qué palabra ayudó más a adivinar?»; si no adivinan, agrega un detalle."),
    "Describe a alguien de tu casa con tres adjetivos que lo caractericen bien.",
    "Describe tu lugar favorito con seis adjetivos y léelo a un adulto.",
)

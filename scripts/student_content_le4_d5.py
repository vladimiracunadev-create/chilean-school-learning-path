"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 28 (vocabulario nuevo en intervenciones orales)."""
from __future__ import annotations

from student_content_le4_d import E, reg
from student_lessons import arith

OA28 = "LE04 OA 28"

# ================================================================ OA 28 · clase 1
reg(
    OA28, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para comentar los significados.",
    "Aprenderé a descubrir el significado de una palabra nueva usando las pistas del texto. Sirve para entender lo que leo y escucho y para tener palabras nuevas que usar al hablar.",
    ["Sé leer una oración y decir de qué trata.", "Sé que las palabras tienen significado."],
    [
        "Cuando leemos o escuchamos una palabra que no conocemos, no hace falta detenerse enseguida. El texto mismo suele dar pistas. Una pista puede ser una explicación que viene después de dos puntos, como en «La hoja de papel de seda es frágil: se rompe con facilidad». Otra pista es un ejemplo o una acción, como en «Rosa es tenaz: aunque se cayó tres veces, siguió intentando hasta lograrlo».",
        "También podemos usar el contraste. En «En verano el agua fue escasa, pero en invierno fue abundante», la palabra «pero» muestra que «escasa» y «abundante» significan cosas opuestas. Si «abundante» es mucha cantidad, «escasa» es poca cantidad. A este trabajo de buscar el significado en lo que rodea a la palabra le llamamos usar el contexto.",
        "Después de encontrar una pista, probamos el significado en la oración: ¿tiene sentido? Si sí, lo guardamos y lo usaremos en nuestras conversaciones. Si no, buscamos otra pista o preguntamos a alguien o a un diccionario.",
    ],
    [("contexto", "lo que rodea a una palabra y ayuda a entenderla"), ("abundante", "que hay en mucha cantidad"), ("escaso", "que hay en poca cantidad"), ("tenaz", "que sigue intentando sin rendirse"), ("frágil", "que se rompe con facilidad")],
    [
        ("Pista de explicación", "Texto: «La hoja de papel de seda es frágil: se rompe con facilidad». ¿Qué significa «frágil»?", ["Busco lo que viene después de los dos puntos.", "Dice que se rompe con facilidad.", "Frágil es algo que se rompe fácilmente."], "Que se rompe con facilidad."),
        ("Pista de contraste", "Texto: «En verano el agua fue escasa, pero en invierno fue abundante». Si «abundante» significa mucha cantidad, ¿qué significa «escasa»?", ["Veo la palabra «pero», que opone dos ideas.", "Lo opuesto de mucha cantidad es poca cantidad.", "Escasa es poca."], "Poca cantidad."),
    ],
    [("Saltarse la palabra nueva sin buscar pistas.", "Se cree que sin diccionario no se puede entender.", "Lee la oración completa y busca explicaciones, ejemplos o contrastes."), ("Inventar un significado sin comprobar que tiene sentido.", "Se adivina rápido.", "Prueba el significado en la oración: ¿calza con lo que dice?")],
    [
        E("Según «La lluvia fue tan abundante que los ríos subieron», ¿«abundante» significa mucha o poca cantidad?", "Mucha cantidad", "Si los ríos subieron, hubo mucha lluvia."),
        E("Según «En el desierto el agua es escasa: casi no hay», ¿«escasa» significa mucha o poca cantidad?", "Poca cantidad", "El texto dice que casi no hay."),
        E("Según «Rosa es tenaz: aunque se cayó tres veces, siguió intentando», ¿«tenaz» describe a quien se rinde o a quien sigue intentando?", "A quien sigue intentando", "Rosa siguió después de caerse."),
    ],
    [
        E("En Lenguaje: ¿Qué es el contexto de una palabra?", "Lo que la rodea y ayuda a entenderla", "Las palabras cercanas dan pistas."),
        E("En «La hoja es frágil: se rompe con facilidad», ¿qué parte explica «frágil»?", "Se rompe con facilidad", "Viene después de los dos puntos."),
        E("¿Por qué conviene probar el significado en la oración?", "Para comprobar que tiene sentido", "Si no calza, hay que buscar otra pista."),
    ],
    [
        E("Texto: «Tomás es prudente: antes de cruzar la calle mira a ambos lados». ¿Qué significa «prudente»: a) actúa con cuidado b) actúa sin pensar?", "a", "Mira a ambos lados antes de cruzar."),
        E("Texto: «El camino era estrecho: apenas cabía una persona». ¿Qué significa «estrecho»: a) angosto b) muy largo?", "a", "Apenas cabía una persona."),
        E("Une cada palabra con su significado: 1) abundante 2) escasa 3) tenaz; a) poca cantidad b) persistente c) mucha cantidad. Escribe como 1-x, 2-x, 3-x.", "1-c, 2-a, 3-b", "Abundante es mucha, escasa es poca y tenaz es persistente."),
    ],
    [
        E("Ema dice que «tenaz» significa «se enoja fácil». Luis dice que significa «persistente». Según «Rosa es tenaz: aunque se cayó tres veces, siguió intentando», ¿quién tiene razón?", "Luis", "El texto muestra que Rosa persistió."),
        E("En «El agua fue escasa, pero la comida fue abundante», ¿qué relación muestra «pero»?", "Contraste", "Opone poca agua y mucha comida."),
    ],
    [
        E("Texto: «El abuelo era meticuloso: revisaba cada tornillo dos veces y anotaba cada paso». ¿Qué significa «meticuloso»: a) apurado b) muy cuidadoso con los detalles c) cansado?", "b", "Revisaba dos veces y anotaba cada paso."),
        E("Texto: «La biblioteca estaba desierta: solo quedaba una persona». ¿Qué significa «desierta»: a) con casi nadie b) muy ordenada?", "a", "Solo quedaba una persona."),
    ],
    [E("Un compañero lee en voz alta: «Las lluvias fueron abundantes y los campos se llenaron de flores». No conoces «abundantes». ¿Qué pista te ayuda: a) los campos se llenaron de flores b) el título del libro?", "a", "Si se llenaron de flores, hubo mucha lluvia.")],
    [
        E("¿Un texto puede dar pistas para entender una palabra?", "Sí", "Con explicaciones, ejemplos y contrastes."),
        E("¿«Pero» puede señalar un contraste?", "Sí", "Une ideas opuestas."),
        E("¿Una palabra nueva se debe saltar siempre?", "No", "Conviene buscar pistas."),
    ],
    ("Descubre significados con el contexto. Lee estas tres oraciones: 1) «Lola es paciente: espera su turno sin molestarse». 2) «El paquete era liviano: lo levantó con un dedo». 3) «Hubo una cosecha abundante: no cabían las verduras en las cajas». Para cada palabra subrayada (paciente, liviano, abundante) escribe qué significa y qué parte del texto te dio la pista. Cuéntaselo a una persona de tu casa.",
     "Paciente: espera sin molestarse, porque dice que espera su turno sin molestarse. Liviano: que pesa poco, porque lo levantó con un dedo. Abundante: mucha cantidad, porque no cabían las verduras en las cajas.",
     ["explica el significado de cada palabra", "cita la pista del texto", "el significado calza con la oración"], ["tres significados con su pista, escritos u orales"], ["inventar un significado sin pista", "no citar la pista"],
     "Si no encuentras la pista, lee la oración completa otra vez y busca explicaciones o ejemplos."),
    "Elige una palabra nueva de un texto de tu casa y escribe qué pista te ayudó a entenderla.",
    "Escribe dos oraciones con pistas para que otra persona entienda la palabra «paciente».",
)

# ================================================================ OA 28 · clase 2
reg(
    OA28, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para decir las paráfrasis en voz alta.",
    "Aprenderé a explicar con mis palabras lo que significa una palabra nueva o una frase, sin cambiar su sentido. Sirve para comprobar que entendí y para usar palabras nuevas con seguridad.",
    ["Sé usar pistas del texto para descubrir significados.", "Sé decir una idea con otras palabras."],
    [
        "Parafrasear es decir con nuestras palabras lo que dijo otra persona o lo que dice un texto, sin cambiar el sentido. Por ejemplo, «La lluvia fue abundante» se puede parafrasear como «Llovió mucho». Si cambiamos el sentido, como en «Llovió poco», ya no es una paráfrasis. Para parafrasear bien, primero entendemos la palabra nueva y luego buscamos palabras sencillas que digan lo mismo.",
        "Una buena paráfrasis sigue tres pasos: leer la frase, pensar qué dice, y decirla con otras palabras. Por ejemplo, «Tomás es prudente» puede decirse como «Tomás actúa con cuidado y piensa antes de hacer algo». Luego comprobamos: ¿dice lo mismo que el original?, ¿mantiene la idea importante?, ¿no agregamos datos nuevos?",
        "Parafrasear antes de usar una palabra nueva nos ayuda a saber si realmente la entendimos. Si no logramos explicarla con nuestras palabras, volvemos al texto y buscamos más pistas.",
    ],
    [("parafrasear", "decir con otras palabras lo mismo que dice un texto"), ("sentido", "idea que expresa una frase"), ("sinónimo", "palabra que significa casi lo mismo que otra"), ("prudente", "que actúa con cuidado pensando en los riesgos"), ("persistente", "que sigue intentando sin rendirse")],
    [
        ("Parafrasear una frase", "Frase: «La lluvia fue abundante en el valle». ¿Cuál es una paráfrasis: a) «Llovió mucho en el valle» b) «Llovió poco en el valle»?", ["Busco la que mantiene el sentido.", "Abundante significa mucha cantidad.", "La a mantiene el sentido."], "a."),
        ("Comprobar la paráfrasis", "Frase: «Tomás es prudente». Paráfrasis: «Tomás actúa con cuidado y piensa antes de hacer algo». ¿Mantiene el sentido?", ["Comparo con el significado de prudente.", "Prudente es actuar con cuidado pensando en los riesgos.", "La paráfrasis dice lo mismo."], "Sí, mantiene el sentido."),
    ],
    [("Cambiar el sentido al parafrasear, como decir «llovió poco» en vez de «llovió mucho».", "Se usa un significado equivocado.", "Comprueba con el texto que sigue diciendo lo mismo."), ("Copiar la frase sin cambiar nada.", "Se cree que parafrasear es repetir.", "Dilo con tus palabras, sencillas y claras.")],
    [
        E("¿Parafrasear es decir con otras palabras lo mismo que dice un texto?", "Sí", "Esa es la idea."),
        E("«Llovió mucho» ¿parafrasea a «La lluvia fue abundante»?", "Sí", "Abundante significa mucha cantidad."),
        E("«Llovió poco» ¿mantiene el sentido de «La lluvia fue abundante»?", "No", "Dice lo contrario."),
    ],
    [
        E("¿Qué debe mantener una paráfrasis: el sentido o las mismas palabras?", "El sentido", "Se cambian las palabras, no la idea."),
        E("«Rosa es tenaz». ¿Cuál es una paráfrasis: a) «Rosa sigue intentando sin rendirse» b) «Rosa se rinde pronto»?", "a", "Tenaz es persistente."),
        E("¿Para qué sirve parafrasear antes de usar una palabra nueva?", "Para comprobar que la entendí", "Si puedo explicarla, la comprendí."),
    ],
    [
        E("Parafrasea con tus palabras: «El camino es estrecho». ¿Cuál sirve más: a) «El camino es angosto» b) «El camino es largo»?", "a", "Estrecho significa angosto."),
        E("Frase: «El agua es escasa en el desierto». ¿Qué paráfrasis es correcta: a) «En el desierto hay poca agua» b) «En el desierto sobra el agua»?", "a", "Escasa significa poca cantidad."),
        E("Ordena los pasos para parafrasear: a) decirlo con otras palabras, b) leer la frase, c) pensar qué dice. Escribe las letras.", "b, c, a", "Primero se lee, luego se piensa y después se dice."),
    ],
    [
        E("Marta parafrasea «El abuelo es meticuloso» (revisa cada detalle con cuidado) como «El abuelo es veloz». ¿Qué problema tiene su paráfrasis?", "Cambió el sentido", "Meticuloso es cuidadoso con los detalles, no veloz."),
        E("Luis parafrasea «Tomás es prudente» como «Tomás es prudente». ¿Qué le falta?", "Decirlo con otras palabras", "Repitió la frase."),
    ],
    [
        E("Frase original: «La cosecha fue abundante y las cajas se llenaron». Paráfrasis 1: «Se recogió mucho y las cajas se llenaron». Paráfrasis 2: «Se recogió poco y las cajas quedaron vacías». ¿Cuál mantiene el sentido?", "La 1", "Abundante significa mucha cantidad."),
        E("Frase original: «Ema es paciente». Paráfrasis: «Ema espera tranquila sin molestarse y además es muy rápida». ¿Qué agregó que el original no decía?", "Que es muy rápida", "Añadió un dato nuevo."),
    ],
    [E("Una compañera lee: «El camino era estrecho y la visita llegó con cuidado». Tú debes explicar con tus palabras sin cambiar el sentido. ¿Cuál es mejor: a) «El camino era angosto y la visita llegó con cuidado» b) «El camino era ancho y la visita llegó apurada»?", "a", "La a conserva el significado.")],
    [
        E("¿Una buena paráfrasis agrega datos nuevos?", "No", "Solo dice lo mismo con otras palabras."),
        E("¿Copiar la frase es parafrasear?", "No", "Parafrasear usa otras palabras."),
        E("¿Podemos parafrasear antes de usar una palabra nueva?", "Sí", "Ayuda a entenderla."),
    ],
    ("Parafrasea tres frases. Lee: 1) «La lluvia fue abundante». 2) «Rosa es tenaz». 3) «El agua es escasa en el desierto». Escribe una paráfrasis de cada frase con tus palabras, sin cambiar el sentido ni agregar datos. Luego comprueba con una persona de tu casa que ella entienda cada una.",
     "1) Llovió mucho. 2) Rosa sigue intentando sin rendirse. 3) En el desierto hay poca agua.",
     ["mantiene el sentido", "usa otras palabras", "no agrega datos nuevos"], ["tres paráfrasis escritas u orales"], ["cambiar el sentido", "repetir la misma frase"],
     "Si cambió el sentido, vuelve a la pista del texto y comprueba el significado."),
    "Parafrasea una frase de un cuento que te lean en casa.",
    "Escribe una paráfrasis para una frase con la palabra «meticuloso» y otra con «frágil».",
)

# ================================================================ OA 28 · clase 3
reg(
    OA28, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar usando las palabras.",
    "Aprenderé a usar palabras nuevas en una conversación, de forma natural y correcta. Sirve para hablar con más precisión y variedad.",
    ["Sé descubrir significados con el contexto y parafrasear.", "Sé participar en una conversación con ideas y razones."],
    [
        "Entender una palabra nueva es el primer paso; el segundo es usarla. Una palabra se usa de manera pertinente cuando calza con la situación y con el sentido que tiene. Por ejemplo, «abundante» sirve para hablar de cosas que hay en mucha cantidad: «La comida de la feria fue abundante». No tendría sentido decir «Mi lápiz es abundante», porque un solo lápiz no puede ser mucha cantidad.",
        "Para usar una palabra nueva en una conversación, pensamos en una situación donde tenga sentido, armamos una oración completa y la decimos con naturalidad, sin forzarla. Podemos agregar una razón, como «La comida fue abundante: alcanzó para todos y sobró». La razón demuestra que entendimos el significado.",
        "No hace falta usar una palabra nueva en cada frase. Usar una o dos en el momento adecuado es mejor que llenar la conversación de palabras difíciles. Si la usamos y la otra persona no la entiende, la explicamos con otras palabras.",
    ],
    [("pertinente", "que calza con la situación y con el sentido"), ("conversación", "intercambio de ideas entre personas"), ("naturalidad", "hablar sin forzar las palabras"), ("razón", "motivo que muestra que entendimos"), ("explicar", "decir con otras palabras para que se entienda")],
    [
        ("Usar la palabra en una oración", "Quieres usar «abundante» para contar cómo fue la feria. ¿Qué frase es correcta: a) «La comida de la feria fue abundante: alcanzó para todos» b) «Mi lápiz es abundante»?", ["Busco una frase donde hay mucha cantidad.", "Comida para todos es mucha cantidad.", "Un lápiz no puede ser mucha cantidad."], "a."),
        ("Agregar una razón", "Dices: «Mi amiga es tenaz». ¿Qué razón muestra que entendiste: a) «Siguió practicando hasta aprender» b) «Tiene una mochila nueva»?", ["Busco la razón que habla de persistir.", "La a muestra que no se rinde.", "La b no se relaciona."], "a."),
    ],
    [("Usar una palabra nueva sin entenderla.", "Se quiere sonar más importante.", "Usa solo palabras cuyo significado comprobaste."), ("Llenar la conversación de palabras difíciles.", "Se piensa que más palabras nuevas es mejor.", "Usa una o dos en el momento adecuado.")],
    [
        E("¿«Prudente» sirve para describir a una persona que actúa con cuidado?", "Sí", "Prudente es actuar con cuidado."),
        E("¿«Escaso» sirve para hablar de algo que hay en mucha cantidad?", "No", "Escaso es poca cantidad."),
        E("¿«Frágil» sirve para hablar de una hoja de papel de seda?", "Sí", "Se rompe con facilidad."),
    ],
    [
        E("¿Qué significa usar una palabra de manera pertinente?", "Que calza con la situación y su sentido", "No se usa al azar."),
        E("Quieres decir que en el desierto hay poca agua. ¿Qué palabra nueva sirve: abundante o escasa?", "Escasa", "Escasa significa poca cantidad."),
        E("¿Por qué ayuda agregar una razón después de usar una palabra nueva?", "Porque muestra que entendimos su significado", "La razón explica la palabra."),
    ],
    [
        E("Completa con la palabra que encaja, tenaz o frágil: «Mi hermano es ___: aunque falló, siguió intentando».", "tenaz", "Describe a quien sigue intentando."),
        E("Completa con «frágil»: «Esa tacita de loza es ___: se rompe fácilmente». Elige: frágil o abundante.", "Frágil", "Se rompe con facilidad."),
        E("Elige la frase que usa bien «prudente»: a) «Luis fue prudente y esperó el semáforo en verde» b) «La mesa es prudente»", "a", "Una persona puede actuar con prudencia; una mesa no."),
    ],
    [
        E("Ema dice: «La feria fue abundante, porque hubo poca comida». ¿Usó bien «abundante»?", "No", "Hubo poca comida contradice abundante."),
        E("Lola dice: «Mi tarea fue meticulosa: revisé cada respuesta dos veces». ¿Usó bien «meticulosa»?", "Sí", "Revisar con cuidado coincide con el significado."),
    ],
    [
        E("Conversación: «¿Cómo estuvo el paseo?» Respuesta A: «Fue abundante y el bus fue abundante». Respuesta B: «La comida fue abundante y alcanzó para todos». ¿Cuál usa mejor la palabra?", "La B", "Habla de algo que puede ser mucho."),
        E("Quieres usar «escaso» para hablar del tiempo del recreo corto. ¿Qué frase es mejor: a) «Hoy tuvimos tiempo escaso para jugar» b) «Hoy tuvimos tiempo abundante para jugar, pero casi no jugamos»?", "a", "La a mantiene el sentido de poco tiempo."),
    ],
    [E("En una conversación sobre la cosecha del huerto, alguien dice: «Este año las tomateras dieron una cosecha abundante». ¿Qué razón puedes agregar para mostrar que entiendes: a) «Había tomates en todas las cajas» b) «El cielo es azul»?", "a", "Muestra mucha cantidad.")],
    [
        E("¿Conviene usar una palabra solo si entiendo su significado?", "Sí", "Así la uso correctamente."),
        E("¿Una razón puede mostrar que entendí la palabra?", "Sí", "La razón explica el significado."),
        E("¿Hay que usar palabras nuevas en cada frase?", "No", "Basta con una o dos en el momento adecuado."),
    ],
    ("Usa palabras nuevas en una conversación. Elige dos de estas palabras: abundante, escaso, tenaz, prudente, meticuloso, frágil. Escribe una frase con cada una, con una razón. Luego conversa dos minutos con una persona de tu casa sobre «cómo te fue hoy» y usa por lo menos una de las palabras, de manera natural. Anota qué frase dijiste.",
     "Frase 1: La merienda fue abundante: alcanzó para toda la familia. Frase 2: Mi hermana es tenaz: practicó hasta que le salió el dibujo. En la conversación dije: Hoy fue un día tranquilo, aunque el tiempo del recreo fue escaso.",
     ["usa dos palabras correctamente", "agrega una razón", "usa una palabra en una conversación real", "suena natural"], ["frases escritas y nota de la conversación"], ["usar la palabra con otro significado", "forzarla"],
     "Si la palabra no calza, prueba otra situación donde tenga sentido."),
    "Usa una palabra nueva hoy en casa y cuenta cómo reaccionó la otra persona.",
    "Escribe un diálogo de cuatro líneas donde dos personas usan «abundante» y «escaso».",
)

# ================================================================ OA 28 · clase 4
reg(
    OA28, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar con distinto tono.",
    "Aprenderé a elegir el registro (más formal o más cercano) y a asegurarme de que la palabra nueva se refiera a lo correcto. Sirve para hablar de manera adecuada según con quién converso.",
    ["Sé usar palabras nuevas con razones.", "Sé saludar y hablar con distintos tratos."],
    [
        "El registro es la manera de hablar según la situación. En un registro formal, como cuando hablamos con una profesora o en una exposición, usamos palabras más cuidadas y evitamos modismos. En un registro informal, como con amigos, usamos palabras cercanas y frases más sueltas. Una palabra nueva puede ser útil en el registro formal, por ejemplo «prudente», pero con amigos quizá digamos «cuidadoso» o «que se fija».",
        "Además de elegir el registro, debemos cuidar el referente: lo que la palabra describe. «Tenaz» describe personas o animales que no se rinden, no objetos. «Escaso» describe cosas que se pueden contar o medir, como comida o agua. «Frágil» sirve para objetos que se rompen fácil. Si usamos una palabra con un referente equivocado, la oración suena rara o dice algo distinto.",
        "Para decidir, nos preguntamos tres cosas: ¿con quién hablo?, ¿de qué hablo? y ¿la palabra calza con eso? Si la respuesta es sí, la usamos; si no, buscamos otra.",
    ],
    [("registro", "manera de hablar según la situación"), ("formal", "cuidado, como al hablar con una profesora"), ("informal", "cercano, como al hablar con amigos"), ("referente", "lo que una palabra describe o nombra"), ("calzar", "ser adecuada para una situación")],
    [
        ("Elegir el registro", "Hablas con la directora sobre una tarea que revisaste con cuidado. ¿Qué frase es más formal: a) «Fui prudente al revisar las respuestas» b) «Me fijé en no meter la pata»?", ["Pienso con quién hablo.", "Con la directora usamos un registro cuidado.", "La a es más formal."], "a."),
        ("Cuidar el referente", "¿Qué frase usa bien «frágil»: a) «Ese florero de cerámica es frágil» b) «Mi amiga Ema es frágil porque es veloz»?", ["Pienso qué describe «frágil».", "Frágil describe objetos que se rompen fácil.", "La a lo usa bien."], "a."),
    ],
    [("Usar siempre el mismo registro.", "Se olvida que la situación cambia.", "Pregunta: ¿con quién hablo y qué situación es?"), ("Usar una palabra para algo que no puede describir.", "Se mezclan significados.", "Revisa qué cosa o persona describe la palabra.")],
    [
        E("¿Con una profesora usamos un registro formal o informal?", "Formal", "Es una situación de respeto."),
        E("¿Con amigos en el recreo usamos más a menudo un registro formal o informal?", "Informal", "Es una situación cercana."),
        E("¿«Tenaz» describe a una persona o a una piedra?", "A una persona", "Una persona puede seguir intentando."),
    ],
    [
        E("¿Qué es el referente de una palabra?", "Lo que la palabra describe o nombra", "Es de lo que se habla."),
        E("¿Para qué sirve preguntarnos «¿con quién hablo?»?", "Para elegir un registro adecuado", "Cambia la manera de hablar."),
        E("«Escaso» ¿sirve para hablar de la comida que casi no hay?", "Sí", "Escaso es poca cantidad."),
    ],
    [
        E("A una profesora le dices cómo te fue en una prueba. ¿Qué frase es más adecuada: a) «Revisé cada pregunta con cuidado» b) «Le puse ojo a todo, pa’ que no se me escapara nada»?", "a", "La a es más cuidada."),
        E("Con un amigo hablas de una caja de vidrio que se cayó. ¿Qué frase usa bien «frágil»: a) «Esa caja es frágil, hay que llevarla despacio» b) «Esa caja es tenaz»?", "a", "Frágil describe algo que se rompe."),
        E("Elige el referente correcto para «tenaz»: a) una persona que no se rinde b) una mesa de madera.", "a", "La persona puede persistir."),
    ],
    [
        E("Luis dice a su profesora algo sobre su experimento. ¿Qué frase es más formal: a) «El experimento quedó bacán» b) «El experimento quedó muy bien hecho»?", "b", "La b usa palabras más cuidadas."),
        E("Ema dice: «El agua del río es tenaz». ¿Qué referente equivocado hay?", "El agua no puede ser tenaz", "Tenaz describe a quien persiste."),
    ],
    [
        E("Situación: hablas con tu abuela de una olla pequeña que casi no tiene agua. Frases: A) «El agua está escasa en la olla.» B) «El agua está prudente en la olla.» ¿Cuál calza?", "A", "Escasa significa poca cantidad."),
        E("Situación: en la sala, describes a un compañero que repitió el ejercicio hasta que le salió. ¿Qué frase es formal y adecuada: a) «Fue tenaz y no se rindió» b) «Es terco, igual le salió»?", "a", "La a es cuidada y describe bien."),
    ],
    [E("Tu curso habla con la directora sobre el cuidado del patio. Uno dice: «Es necesario ser prudentes al usar los juegos, para evitar accidentes». Otro dice: «Hay que ponerle ojo a los juegos pa’ que nadie se pegue un porrazo». ¿Cuál se ajusta mejor a esa situación?", "El primero", "Usa un registro cuidado y claro.")],
    [
        E("¿El registro cambia según la situación?", "Sí", "No hablamos igual con todos."),
        E("¿Una palabra debe calzar con lo que describe?", "Sí", "Si no, la oración suena rara."),
        E("¿«Prudente» describe a una persona que actúa con cuidado?", "Sí", "Es su significado."),
    ],
    ("Ajusta tu manera de hablar. Elige una de estas situaciones: a) le cuentas a tu profesora cómo trabajaste en una tarea; b) le cuentas a un amigo lo mismo. Escribe dos frases, una para cada situación, que usen una palabra nueva (por ejemplo, meticuloso, tenaz o prudente) con el registro adecuado, y explica qué cambiaste. Di las frases en voz alta a una persona de tu casa.",
     "A la profesora: Trabajé de manera meticulosa: revisé cada paso dos veces. A mi amigo: Me fijé en cada detalle y lo revisé dos veces. Cambié las palabras cuidadas por otras más cercanas.",
     ["usa una palabra nueva con su referente correcto", "ajusta el registro a la situación", "explica el cambio"], ["dos frases y una explicación, escritas u orales"], ["usar el mismo registro para ambas", "referente equivocado"],
     "Si suenan igual, cambia una palabra formal por una más cercana o al revés."),
    "Escribe dos formas de decir lo mismo: una formal y otra informal.",
    "Escribe una conversación breve entre un estudiante y una profesora usando una palabra nueva con registro formal.",
)

# ================================================================ OA 28 · clase 5
reg(
    OA28, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para grabar o escuchar y comentar.",
    "Aprenderé a notar cuándo una palabra nueva no encaja y a corregirme con tranquilidad. Sirve para hablar con más seguridad y aprender de los errores.",
    ["Sé usar palabras nuevas con razones y con el registro adecuado.", "Sé parafrasear."],
    [
        "A veces usamos una palabra nueva y no encaja: la oración suena rara o dice algo distinto de lo que queríamos. Es normal, y es parte de aprender. Lo importante es darnos cuenta y corregirnos. Autocorregirse es revisar lo que dijimos y arreglarlo. Podemos decir «Quise decir…» o «Mejor dicho…» y decir la frase otra vez.",
        "Para darnos cuenta de un error nos hacemos tres preguntas: ¿la palabra significa lo que quise decir?, ¿describe lo que mencioné?, ¿la otra persona me entendió? Si la respuesta es no, buscamos otra palabra o volvemos al texto donde la aprendimos. A veces la solución más simple es explicar con otras palabras lo que queremos decir.",
        "Corregirse con tranquilidad no es motivo de vergüenza. Al contrario, muestra que escuchamos lo que decimos y queremos hablar bien. Y si alguien más se equivoca, podemos ayudar con amabilidad: «Creo que querías decir…».",
    ],
    [("autocorregir", "revisar lo que dijimos y arreglarlo"), ("encajar", "calzar con la situación y el sentido"), ("quise decir", "frase que se usa para corregirse"), ("error", "algo que no quedó como queríamos"), ("amabilidad", "trato respetuoso al ayudar")],
    [
        ("Darse cuenta de un error", "Dijiste: «La comida fue escasa, alcanzó para todos y sobró». ¿Qué palabra no encaja: escasa o alcanzó?", ["Reviso el sentido de cada palabra.", "Si alcanzó para todos y sobró, hubo mucha.", "«Escasa» no encaja."], "Escasa."),
        ("Corregirse", "Después de decir «La comida fue escasa, alcanzó para todos», quieres corregirte. ¿Qué dices: a) «Quise decir que fue abundante» b) «Nada, olvídenlo»?", ["Busco la forma de arreglar lo dicho.", "La a usa «quise decir».", "La b no aclara."], "a."),
    ],
    [("Seguir hablando aunque la palabra no encaje.", "Da vergüenza corregirse.", "Detente un momento y di «Quise decir…»."), ("Reírse de quien se equivoca.", "Se confunde el error con algo gracioso.", "Ayuda con amabilidad: «Creo que querías decir…».")],
    [
        E("¿Autocorregirse es revisar lo que dijimos y arreglarlo?", "Sí", "Esa es su definición."),
        E("¿Qué frase sirve para corregirse: «Quise decir…» o «Eso no importa»?", "Quise decir…", "Abre la corrección."),
        E("¿Equivocarse al usar una palabra nueva es normal cuando se aprende?", "Sí", "Es parte del proceso."),
    ],
    [
        E("Dijiste «Mi hermana es muy frágil porque nunca se rinde». ¿Qué palabra debía usarse: frágil o tenaz?", "Tenaz", "No rendirse es ser tenaz."),
        E("¿Qué pregunta ayuda a detectar un error: «¿La palabra significa lo que quise decir?» o «¿Cuántas sílabas tiene?»", "¿La palabra significa lo que quise decir?", "Comprueba el sentido."),
        E("Si una persona no entendió la palabra, ¿qué conviene hacer: explicarla con otras palabras o repetirla más fuerte?", "Explicarla con otras palabras", "Así se entiende mejor."),
    ],
    [
        E("Frase con error: «La tarea fue meticulosa porque la hice muy rápido». ¿Qué palabra no encaja con «muy rápido»: a) meticulosa b) tarea?", "a", "Meticulosa significa muy cuidadosa y no calza con hacer algo muy rápido."),
        E("Corrige: «El camino es prudente». ¿Qué palabra encaja mejor: a) estrecho b) escaso?", "a", "Estrecho describe caminos."),
        E("Ordena una autocorrección: a) Quise decir que es tenaz, b) Mi hermana es frágil, c) ... eh, no. Escribe las letras.", "b, c, a", "Primero lo dicho, luego la pausa y después la corrección."),
    ],
    [
        E("Un compañero dijo: «El agua es tenaz». Marta responde: «Creo que querías decir que el agua es escasa o abundante». ¿Qué hizo Marta?", "Ayudó con amabilidad", "Propuso una corrección sin burlarse."),
        E("¿Por qué corregirse muestra interés en hablar bien?", "Porque muestra que escuchamos lo que decimos", "Revisar es cuidar el mensaje."),
    ],
    [
        E("Grabas lo que dices: «Fue una cosecha escasa y llenamos todas las cajas». Debes corregir. ¿Qué cambio es mejor: a) cosecha abundante b) cajas escasas?", "a", "Si llenaron todas las cajas, fue abundante."),
        E("Dices: «Mi abuelo es prudente: se lanza sin mirar». ¿Cuál es la idea que no encaja con «prudente»?", "Se lanza sin mirar", "Prudente es actuar con cuidado."),
    ],
    [E("En una conversación sobre cómo cuidar una planta dices: «Hay que regarla con agua abundante cada hora». Notas que es demasiado. ¿Cómo te corriges: a) «Quise decir que hay que regarla con agua suficiente, sin exceso» b) «Da lo mismo»?", "a", "Aclaras lo que querías decir.")],
    [
        E("¿Corregirse muestra interés en hablar bien?", "Sí", "Revisar es cuidar el mensaje."),
        E("¿Se puede ayudar a otra persona a corregirse con amabilidad?", "Sí", "Se logra con respeto."),
        E("¿Un error al usar una palabra nueva significa que no podemos aprender?", "No", "Los errores ayudan a mejorar."),
    ],
    ("Practica autocorregirte. Lee estas tres frases que tienen palabras que no encajan: 1) «La biblioteca estaba desierta, había mucha gente». 2) «Mi vecino es escaso porque trabaja todos los días». 3) «El vaso de plástico es muy frágil porque no se rompe nunca». Para cada una escribe: qué palabra no encaja, cómo te corriges con «Quise decir…» y la frase corregida. Léelo en voz alta.",
     "1) No encaja «desierta»: Quise decir que estaba llena de gente. 2) No encaja «escaso»: Quise decir que es trabajador. 3) No encaja «frágil»: Quise decir que es resistente.",
     ["detecta la palabra que no encaja", "usa «Quise decir…»", "la frase corregida tiene sentido"], ["tres correcciones escritas u orales"], ["cambiar la idea completa", "no explicar por qué no encajaba"],
     "Si no sabes cuál palabra falla, revisa el significado de cada una."),
    "Cuando hables hoy, si una palabra no encaja, practica decir «Quise decir…».",
    "Escribe un diálogo de cuatro líneas en que alguien se autocorrige al usar una palabra nueva.",
)

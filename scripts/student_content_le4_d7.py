"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 30 (recitación expresiva de poemas). Los poemas son textos originales breves del proyecto."""
from __future__ import annotations

from student_content_le4_d import E, reg
from student_lessons import arith

OA30 = "LE04 OA 30"

POEMA_LLUVIA = "La lluvia llega despacio / y toca la ventana; / yo escucho su canto suave / desde mi cama de lana."

# ================================================================ OA 30 · clase 1
reg(
    OA30, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu lectura. Los poemas de esta clase son originales y breves; los poemas de autores reales los trae el docente.",
    "Aprenderé a comprender un poema antes de memorizarlo: qué dice, qué imágenes tiene y qué siente quien habla. Sirve para recitarlo con sentido y recordarlo mejor.",
    ["Sé que un poema se escribe en versos.", "Sé decir con mis palabras lo que dice un texto."],
    [
        "Un poema es un texto escrito en versos, que son cada una de sus líneas. Un grupo de versos forma una estrofa. Quien dice el poema se llama hablante, y suele expresar un sentimiento o una mirada sobre algo. Lee este poema, que se llama «La lluvia en la ventana»: «La lluvia llega despacio / y toca la ventana; / yo escucho su canto suave / desde mi cama de lana.». Tiene cuatro versos y una estrofa.",
        "Antes de memorizar, comprendemos. Primero lo leemos en voz alta. Luego buscamos de qué trata (la lluvia que se escucha desde la cama), qué siente el hablante (calma) y qué imágenes aparecen. Una imagen es una expresión que nos hace ver, oír o sentir algo, como «canto suave», que compara el sonido de la lluvia con una canción tranquila. También hay una personificación: decir que la lluvia «toca la ventana» como si fuera una persona.",
        "La rima ocurre cuando los versos terminan con sonidos iguales: «ventana» y «lana». Entender el significado y las imágenes nos ayuda a recordar el poema, porque ya no son palabras sueltas: son ideas que vemos. Si encontramos una palabra difícil, buscamos pistas o la preguntamos.",
    ],
    [("verso", "cada línea de un poema"), ("estrofa", "grupo de versos"), ("hablante", "la voz que dice el poema"), ("imagen", "expresión que nos hace ver, oír o sentir algo"), ("rima", "sonidos iguales al final de los versos")],
    [
        ("Entender el tema", "Poema: «La lluvia llega despacio / y toca la ventana; / yo escucho su canto suave / desde mi cama de lana». ¿Qué siente el hablante?", ["Miro las palabras «despacio» y «canto suave».", "Todo es tranquilo y suave.", "El hablante siente calma."], "Calma."),
        ("Interpretar una imagen", "En el mismo poema, ¿qué compara la expresión «canto suave»: a) el sonido de la lluvia con una canción tranquila b) el color de la ventana con una canción?", ["Busco qué cosa suena en el poema.", "Lo que suena es la lluvia.", "Se compara con una canción tranquila."], "a."),
    ],
    [("Memorizar las palabras sin entender qué dicen.", "Se cree que lo importante es no olvidarlas.", "Primero comprende de qué trata y qué imágenes tiene."), ("Pensar que «tocar la ventana» significa que una persona entra.", "No se reconocen las imágenes.", "Piensa qué cosa compara: la lluvia que cae sobre el vidrio.")],
    [
        E("En el poema de la lluvia, ¿cómo llega la lluvia: despacio o rápido?", "Despacio", "El primer verso dice «llega despacio»."),
        E("¿Dónde está quien escucha la lluvia: en su cama o en la calle?", "En su cama", "El último verso dice «desde mi cama de lana»."),
        E("¿Cuántos versos tiene el poema de la lluvia?", "Cuatro", "Son las cuatro líneas."),
    ],
    [
        E("En el poema de la lluvia, ¿qué quiere decir que la lluvia «toca la ventana»?", "Que cae sobre la ventana", "Es una forma de decirlo como si fuera una persona."),
        E("¿Qué palabra rima con «ventana» en el poema?", "Lana", "Terminan con el mismo sonido."),
        E("¿Para qué conviene comprender un poema antes de memorizarlo?", "Para recordarlo y decirlo con sentido", "Entender ayuda a recordar."),
    ],
    [
        E("¿Cuál dice lo mismo que «yo escucho su canto suave»: a) oigo su sonido tranquilo b) grito muy fuerte?", "a", "Es una paráfrasis del verso."),
        E("Ordena los versos de la estrofa: a) y toca la ventana; b) desde mi cama de lana. c) La lluvia llega despacio d) yo escucho su canto suave. Escribe las letras.", "c, a, d, b", "Así aparecen en el poema."),
        E("El poema habla de una cama de lana. ¿Qué idea de comodidad nos da: a) calor y suavidad b) frío y dureza?", "a", "La lana es suave y abriga."),
    ],
    [
        E("Un compañero memoriza el poema pero no sabe de qué trata. Otro lo comprende primero. ¿Quién podrá recitarlo con más sentido?", "El que lo comprendió", "Sabe qué sentimiento transmitir."),
        E("¿Sería adecuado decir este poema con voz fuerte y rápida?", "No", "Habla de calma y de algo suave."),
    ],
    [
        E("¿Cuántas estrofas tiene el poema de la lluvia si todos sus versos están juntos?", "Una", "Las cuatro líneas forman un solo grupo."),
        E("Explica con una frase corta de qué trata el poema. Elige la mejor: a) Alguien escucha la lluvia tranquila desde su cama b) Alguien corre bajo la lluvia gritando.", "a", "Refleja el tema y el sentimiento."),
    ],
    [E("Debes explicar a tu curso por qué comprender el poema ayuda a memorizarlo. Eliges este argumento: «Porque las palabras se vuelven imágenes y es más fácil recordar lo que vemos». ¿Es un buen argumento? Responde sí o no.", "Sí", "Relaciona la comprensión con la memoria.")],
    [
        E("¿Un poema se escribe en versos?", "Sí", "Los versos son sus líneas."),
        E("¿Una imagen nos hace ver, oír o sentir algo?", "Sí", "Es una expresión sensorial."),
        E("¿Memorizar sin comprender es suficiente para recitar con expresión?", "No", "Se necesita sentido."),
    ],
    ("Comprende un poema antes de memorizarlo. Lee de nuevo «La lluvia llega despacio / y toca la ventana; / yo escucho su canto suave / desde mi cama de lana». Escribe: 1) de qué trata en una frase, 2) qué siente el hablante, 3) una imagen del poema y qué significa. Léelo en voz alta dos veces a una persona de tu casa y pídele que diga qué sintió al escucharlo. Si quieres, escribe tu propio poema de dos versos sobre el clima.",
     "1) Trata de alguien que escucha la lluvia desde su cama. 2) Siente calma. 3) «Canto suave» compara el sonido de la lluvia con una canción tranquila. La persona dijo que sintió tranquilidad.",
     ["dice de qué trata", "nombra el sentimiento", "explica una imagen", "lee con sentido"], ["respuestas escritas y lectura en voz alta"], ["memorizar sin entender", "interpretar mal una imagen"],
     "Si no entiendes una imagen, pregúntate: ¿qué cosa se compara con qué?"),
    "Lee otro poema breve que te muestre una persona de tu casa y di de qué trata.",
    "Escribe una estrofa de cuatro versos sobre un día de viento, con una imagen.",
)

# ================================================================ OA 30 · clase 2
reg(
    OA30, 2,
    "Este cuaderno, lápiz y una hoja con el poema copiado en letra grande para marcar. Opcional: una persona de tu casa para escucharte.",
    "Aprenderé a marcar pausas y palabras clave en un poema para recitarlo con claridad y expresión. Sirve para que se entienda lo importante y se escuche el ritmo.",
    ["Sé comprender un poema y sus imágenes.", "Sé leer en voz alta con claridad."],
    [
        "Cuando recitamos, las pausas ayudan a que el poema se entienda. Una pausa es un pequeño silencio. Una coma pide una pausa corta, y un punto pide una pausa larga. Podemos marcarlas con una raya: / para la corta y // para la larga. Las pausas también se hacen donde cambia una idea, aunque no haya signo.",
        "Veamos «El farol»: «En la esquina duerme un farol, / pero cuando llega la noche, / despierta con un bostezo de luz / y cuida la calle en silencio.». Tiene dos comas y un punto. Las comas piden pausas cortas; el punto del final, una larga.",
        "Las palabras clave son las más importantes para el sentido. Las decimos con un poco más de fuerza o más despacio. En «El farol», podrían ser «duerme», «despierta» y «cuida». No se deben recalcar todas las palabras: si todas son importantes, ninguna lo es. Marcar el poema con pausas y palabras clave nos ayuda a ensayar.",
    ],
    [("pausa", "silencio breve al hablar"), ("coma", "signo que pide una pausa corta"), ("punto", "signo que pide una pausa larga"), ("palabra clave", "palabra importante que se dice con más énfasis"), ("énfasis", "fuerza especial que damos a una palabra")],
    [
        ("Marcar pausas", "Verso: «pero cuando llega la noche,». ¿Qué pausa pide el final de este verso: corta o larga?", ["Miro el signo al final.", "Termina con coma.", "La coma pide una pausa corta."], "Corta."),
        ("Elegir palabras clave", "En «El farol», ¿qué palabra clave muestra el cambio del día a la noche: a) despierta b) esquina?", ["Pienso qué palabra cambia la situación.", "Despierta muestra que algo comienza.", "Es la palabra clave."], "a."),
    ],
    [("Hacer una pausa larga en cada coma.", "Se confunde la coma con el punto.", "Coma es pausa corta; punto es pausa larga."), ("Dar mucha fuerza a todas las palabras.", "Se cree que así se nota más.", "Elige dos o tres palabras clave por estrofa.")],
    [
        E("¿Una coma pide una pausa corta o larga?", "Corta", "La pausa larga se hace en el punto."),
        E("¿Un punto pide una pausa corta o larga?", "Larga", "Marca un final de idea."),
        E("En «El farol», ¿cuántos puntos hay al final del poema?", "Uno", "Está al final del último verso."),
    ],
    [
        E("En «El farol», ¿cuántas comas hay: la que sigue a «farol» y la que sigue a «noche»?", "Dos", "Una en cada uno de esos versos."),
        E("¿Para qué sirven las palabras clave?", "Para destacar lo más importante", "Ayudan a transmitir el sentido."),
        E("¿Hay que hacer pausa solo donde hay signo?", "No", "También donde cambia una idea."),
    ],
    [
        E("Marca el verso con una raya donde va la pausa corta: «En la esquina duerme un farol,». ¿En qué lugar va: antes de «En» o después de «farol»?", "Después de «farol»", "La coma indica la pausa corta al final."),
        E("Elige tres palabras clave posibles de «El farol»: a) duerme, despierta, cuida b) en, la, un.", "a", "Son las que dan sentido."),
        E("Ordena los pasos para preparar un poema: a) marcar pausas y palabras clave, b) comprender el poema, c) ensayar en voz alta. Escribe las letras.", "b, a, c", "Primero se comprende, luego se marca y después se ensaya."),
    ],
    [
        E("Un niño hace pausas largas en cada coma y el poema se oye entrecortado. ¿Qué debe cambiar?", "Hacer pausas cortas en las comas", "Así fluye mejor."),
        E("Si decimos con énfasis todas las palabras, ¿se nota cuál es la más importante?", "No", "El énfasis pierde fuerza."),
    ],
    [
        E("En «despierta con un bostezo de luz», la palabra clave es «despierta». ¿Qué conviene hacer al decirla: a) darle un poco más de fuerza o claridad b) susurrarla al final?", "a", "La palabra clave se destaca."),
        E("Al final de «El farol» hay un punto. ¿Qué pausa corresponde: a) una pausa larga b) ninguna pausa?", "a", "El punto marca el final de la idea."),
    ],
    [E("Debes recitar «El farol» a tu curso. Marca pausas y palabras clave. ¿Cuál es una buena marca: a) pausa corta después de «farol», pausa corta después de «noche», pausa larga al final b) pausa larga en cada verso?", "a", "Respeta los signos del poema.")],
    [
        E("¿Una raya / puede marcar una pausa corta?", "Sí", "Es una convención para ensayar."),
        E("¿Todas las palabras de un poema son clave?", "No", "Solo algunas lo son."),
        E("¿Marcar el poema ayuda a ensayar?", "Sí", "Guía dónde pausar y destacar."),
    ],
    ("Marca y ensaya «El farol». Copia en tu hoja: «En la esquina duerme un farol, / pero cuando llega la noche, / despierta con un bostezo de luz / y cuida la calle en silencio». Marca con / las pausas cortas y con // las largas, y subraya tres palabras clave. Luego recítalo en voz alta a una persona de tu casa, siguiendo tus marcas. Pregúntale si se entendió.",
     "En la esquina duerme un farol,/ pero cuando llega la noche,/ despierta con un bostezo de luz y cuida la calle en silencio.// Palabras clave: duerme, despierta, cuida.",
     ["marca pausas cortas en las comas", "marca la pausa larga en el punto final", "elige tres palabras clave", "se entiende al recitar"], ["hoja marcada y recitación"], ["pausa larga en cada coma", "subrayar todas las palabras"],
     "Si se oye entrecortado, revisa que las pausas cortas sean realmente breves."),
    "Marca pausas en un poema corto que te muestren en casa.",
    "Marca pausas y palabras clave en «La lluvia en la ventana» y compara con «El farol».",
)

# ================================================================ OA 30 · clase 3
reg(
    OA30, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar. Ensaya en un espacio libre y seguro.",
    "Aprenderé a ajustar el ritmo, la voz y el gesto al sentido de un poema. Sirve para que la emoción del poema se escuche y se vea.",
    ["Sé comprender un poema y marcar pausas y palabras clave.", "Sé controlar mi volumen al hablar."],
    [
        "El ritmo es la velocidad con que decimos el poema. Si el poema habla de algo rápido, como unas hormigas que corren, el ritmo puede ser más rápido. Si habla de algo lento, como una tortuga, el ritmo puede ser más lento. Leamos «Las hormigas»: «Una, dos, tres hormigas / cargan migas de pan; / van de prisa, van de prisa, / y no se cansan jamás». Y «La tortuga»: «Camina la tortuga / sin prisa y sin temor; / paso a paso, despacio, / cruza el jardín en flor».",
        "La voz también expresa. Con el volumen decimos algo fuerte o suave. Con la entonación subimos o bajamos el tono: por ejemplo, sube un poco en una pregunta o en una sorpresa y baja al terminar una idea. Los gestos acompañan con pocos movimientos: una mano que señala «hormigas» o una mirada tranquila para «paso a paso».",
        "No hay que exagerar. Un gesto pequeño y bien elegido vale más que muchos movimientos. Ensayamos probando distintos ritmos y escuchamos cuál refleja mejor lo que dice el poema.",
    ],
    [("ritmo", "velocidad y cadencia con que decimos un poema"), ("entonación", "subir o bajar el tono de la voz al hablar"), ("volumen", "qué tan fuerte o suave suena la voz"), ("gesto", "movimiento de manos, cara o cuerpo que acompaña"), ("cadencia", "ritmo regular en la manera de decir algo")],
    [
        ("Elegir el ritmo", "¿Qué ritmo conviene al poema «Las hormigas», que habla de hormigas que van de prisa: a) rápido y ligero b) muy lento?", ["Pienso qué dice el poema.", "Habla de prisa.", "Un ritmo rápido refleja eso."], "a."),
        ("Elegir el ritmo del otro poema", "¿Qué ritmo conviene al poema «La tortuga», que habla de caminar paso a paso: a) rápido b) lento y tranquilo?", ["Pienso en lo que cuenta.", "Una tortuga camina despacio.", "El ritmo lento refleja eso."], "b."),
    ],
    [("Recitar todos los poemas con el mismo ritmo.", "No se piensa en lo que dice el poema.", "Elige el ritmo según el sentido."), ("Hacer muchos gestos grandes.", "Se cree que más movimiento expresa más.", "Elige uno o dos gestos pequeños.")],
    [
        E("¿«De prisa» sugiere un ritmo rápido o lento?", "Rápido", "La prisa se nota en el ritmo."),
        E("¿«Paso a paso» sugiere un ritmo rápido o lento?", "Lento", "Cada paso es pausado."),
        E("¿El volumen es qué tan fuerte o suave suena la voz?", "Sí", "Esa es su definición."),
    ],
    [
        E("En «Las hormigas», ¿cuántas hormigas se cuentan en el primer verso: «Una, dos, tres»?", "Tres", "El verso las cuenta hasta tres."),
        E("¿Por qué ajustamos el ritmo al sentido del poema?", "Para que la emoción se escuche", "El ritmo refleja lo que dice."),
        E("¿Qué es la entonación?", "Subir o bajar el tono de la voz", "Da expresión al poema."),
    ],
    [
        E("Quieres decir el verso «paso a paso, despacio,» de «La tortuga». ¿Cómo lo dices: a) lento, con pausa corta en cada coma b) muy rápido?", "a", "El ritmo lento refleja «despacio»."),
        E("En «Las hormigas», el verso «van de prisa, van de prisa,» se repite. ¿Qué conviene: a) decir la repetición más rápida la segunda vez b) decirla muy lenta?", "a", "La repetición muestra más prisa."),
        E("Elige el gesto pequeño y adecuado para «Una, dos, tres hormigas»: a) contar con los dedos b) saltar por la sala.", "a", "Es un gesto simple y seguro."),
    ],
    [
        E("Dos niños recitan «La tortuga». Uno lo dice rapidísimo y el otro con ritmo lento. ¿Quién refleja mejor el sentido?", "El del ritmo lento", "El poema habla de ir despacio."),
        E("¿Un gesto muy grande puede distraer del poema?", "Sí", "Puede ocultar las palabras."),
    ],
    [
        E("Cuenta las comas del verso «Una, dos, tres hormigas». ¿Cuántas hay?", "Dos", "Una después de «Una» y otra después de «dos»."),
        E("¿Qué pausa piden esas comas: corta o larga?", "Corta", "Las comas piden pausa corta."),
    ],
    [E("Vas a recitar «Las hormigas» en una sala pequeña. ¿Cuál es el mejor plan: a) ritmo rápido, volumen medio y un gesto con los dedos para contar b) ritmo lento, volumen muy bajo y saltos?", "a", "Concuerda con el sentido y es seguro.")],
    [
        E("¿El ritmo debe combinar con el sentido del poema?", "Sí", "Así se refleja lo que dice."),
        E("¿Los gestos deben ser pocos y adecuados?", "Sí", "Acompañan sin tapar."),
        E("¿La entonación sube y baja el tono?", "Sí", "Da expresión al poema."),
    ],
    ("Ensaya ritmo, voz y gesto. Elige «Las hormigas» o «La tortuga» (los textos están en la explicación). Decide: 1) el ritmo (rápido o lento) y por qué, 2) el volumen, 3) un gesto pequeño y seguro. Recítalo en voz alta a una persona de tu casa dos veces: primero con el ritmo equivocado a propósito y luego con el que elegiste. Pregúntale cuál reflejó mejor el poema y anótalo.",
     "Elegí «La tortuga». Ritmo lento porque dice «paso a paso, despacio». Volumen medio. Gesto: mover una mano lentamente al decir «cruza el jardín». La persona dijo que la segunda versión se sintió más tranquila.",
     ["elige el ritmo justificándolo", "decide volumen y gesto", "compara dos versiones", "anota la opinión de quien escuchó"], ["notas y recitación frente a otra persona"], ["no justificar el ritmo", "gestos grandes o inseguros"],
     "Si no se nota la diferencia, exagera un poco más el contraste en el ensayo, sin gritar."),
    "Recita un verso de «Las hormigas» con tres ritmos distintos.",
    "Escribe una estrofa corta sobre un animal rápido y otra sobre uno lento, y di cada una con su ritmo.",
)

# ================================================================ OA 30 · clase 4
reg(
    OA30, 4,
    "Este cuaderno, lápiz y una hoja. Una o dos personas de tu casa que escuchen y comenten. Si estás solo, graba tu voz o escucha tu propio ensayo.",
    "Aprenderé a recitar un poema ante otras personas, a escuchar con respeto y a revisar con una pauta. Sirve para ganar confianza y mejorar con cada intento.",
    ["Sé comprender un poema, marcar pausas y elegir ritmo, voz y gesto.", "Sé dar una opinión respetuosa."],
    [
        "Recitar es decir un poema de memoria, con expresión, frente a una audiencia. Leamos «Mi sombra»: «Mi sombra camina conmigo / y nunca me deja atrás; / si corro, corre a mi lado; / si paro, se queda quieta.». Tiene cuatro versos y dos comas. Para memorizarlo, ayuda dividirlo en versos, repetir uno o dos por vez, asociar cada verso con una imagen (una sombra que me sigue) y practicar sin mirar el papel.",
        "Quien escucha también tiene una tarea: mirar a quien recita, guardar silencio y aplaudir al final. No se interrumpe ni se burla. Luego se revisa la recitación con una pauta de cinco criterios: 1) dice el poema con pocos errores, 2) hace las pausas, 3) el ritmo y la entonación van con el sentido, 4) la voz es clara y se oye, 5) mira a la audiencia y usa gestos pequeños.",
        "La revisión se hace con respeto: se dice un criterio que cumplió con evidencia y una sugerencia concreta para el siguiente intento. Recitar ante otros puede dar nervios; reconocer lo que salió bien ayuda a ganar confianza. Cada recitación es una nueva oportunidad para aprender.",
    ],
    [("recitar", "decir un poema de memoria con expresión"), ("memorizar", "aprender algo para decirlo sin leer"), ("pauta", "lista de criterios para revisar"), ("audiencia", "personas que escuchan"), ("confianza", "seguridad en uno mismo")],
    [
        ("Usar la pauta", "Pía recita «Mi sombra» sin errores y con pausas en las comas, pero habla muy bajito y no mira a nadie. ¿Qué dos criterios de la pauta cumple?", ["Reviso lo que hizo bien.", "Lo dijo sin errores y respetó las pausas.", "La voz baja y la falta de mirada no cumplen."], "Pocos errores y pausas."),
        ("Memorizar por partes", "Quieres memorizar «Mi sombra» (4 versos). ¿Qué estrategia ayuda más: a) repetir de a uno o dos versos y asociar la imagen b) leerlo una sola vez muy rápido?", ["Pienso en cómo recordar mejor.", "Dividir el poema ayuda.", "Repetir por partes con imágenes es mejor."], "a."),
    ],
    [("Recitar leyendo el papel sin mirar a nadie.", "Se tiene miedo de olvidar.", "Practica por partes hasta poder mirar al público."), ("Criticar a quien recita sin decir qué funcionó.", "Se cree que corregir es lo único importante.", "Di algo que funcionó y una sugerencia concreta.")],
    [
        E("¿Cuántos versos tiene «Mi sombra»?", "Cuatro", "Son las cuatro líneas."),
        E("¿Qué hace la sombra cuando el hablante corre?", "Corre a su lado", "El tercer verso lo dice."),
        E("¿Qué hace el público mientras alguien recita: escuchar en silencio o interrumpir?", "Escuchar en silencio", "Es una norma de respeto."),
    ],
    [
        E("¿Cuántos criterios tiene la pauta de recitación de esta clase?", "Cinco", "Son memoria, pausas, ritmo y entonación, voz y mirada."),
        E("¿Por qué ayuda dividir el poema en versos al memorizarlo?", "Porque se aprende por partes pequeñas", "Es más fácil recordar poco a poco."),
        E("¿Por qué es importante decir algo que funcionó en la retroalimentación?", "Porque reconoce lo logrado y da confianza", "Sirve para seguir mejorando."),
    ],
    [
        arith("Practicas «Mi sombra» 3 veces al día durante 4 días. ¿Cuántas veces lo practicas en total?", "3*4", "Se repiten tres prácticas por día durante cuatro días.", " veces"),
        E("Un compañero te dice: «Tu voz clara se oyó bien; podrías mirar más al público». ¿Cuál es la sugerencia?", "Mirar más al público", "Dice qué mejorar."),
        E("Ordena: a) recitar, b) memorizar por partes, c) revisar con la pauta. Escribe las letras.", "b, a, c", "Primero se memoriza, luego se recita y después se revisa."),
    ],
    [
        E("Pedro recitó «Mi sombra»: dijo todo sin errores, hizo las pausas, usó ritmo suave, habló claro, pero miró el suelo. Con la pauta de cinco criterios, ¿cuántos cumplió?", "Cuatro", "Solo le faltó la mirada."),
        E("Ema recita y se equivoca en un verso. Sigue con calma y termina. ¿Qué actitud ayuda a ganar confianza: a) seguir adelante y aprender del error b) rendirse?", "a", "Seguir adelante muestra seguridad."),
    ],
    [
        E("Dos comentarios a Luisa: 1) «Estuvo mal.» 2) «Tus pausas en las comas ayudaron a entender el poema; podrías subir el volumen en el último verso». ¿Cuál es mejor?", "El 2", "Tiene evidencia y sugerencia."),
        E("Al final de la recitación, ¿qué hace una audiencia respetuosa: aplaudir o ignorar?", "Aplaudir", "Reconoce el esfuerzo."),
    ],
    [E("Quieres autoevaluarte tras recitar «Mi sombra». Notas que miraste al público, hablaste claro, pero olvidaste un verso. ¿Qué conviene practicar para la próxima vez: a) la memoria del poema por versos b) el color de la ropa?", "a", "Es lo que falló.")],
    [
        E("¿Recitar es decir un poema de memoria con expresión?", "Sí", "Esa es su definición."),
        E("¿Una pauta ayuda a revisar una recitación?", "Sí", "Da criterios claros."),
        E("¿Reconocer lo que salió bien ayuda a ganar confianza?", "Sí", "Da seguridad para seguir mejorando."),
    ],
    ("Recita, escucha y revisa. Memoriza «Mi sombra» por partes: «Mi sombra camina conmigo / y nunca me deja atrás; / si corro, corre a mi lado; / si paro, se queda quieta.». Recítalo a una persona de tu casa de memoria, con pausas en las comas y ritmo suave. Pídele que use los cinco criterios de la pauta y te diga uno que cumpliste con evidencia y una sugerencia. Escribe ambos y qué cambiarás en tu próximo intento.",
     "Cumplí el criterio de las pausas, porque hiciste silencio en cada coma. Sugerencia: mira más a la audiencia. Próximo intento: miraré a la persona en cada verso.",
     ["recita de memoria o con pocos errores", "respeta las pausas", "recibe retroalimentación con algo logrado y una sugerencia", "decide qué mejorar"], ["recitación y notas escritas"], ["leer el papel todo el rato", "retroalimentación sin evidencia"],
     "Si te cuesta recordar, vuelve a dividir el poema y repite un verso por vez."),
    "Recita «Mi sombra» a una mascota o a un peluche para practicar sin presión.",
    "Escribe una pauta con seis criterios para revisar una recitación e inventa una nota para cada uno.",
)

# ================================================================ OA 30 · clase 5
reg(
    OA30, 5,
    "Este cuaderno, lápiz y una hoja. Una o dos personas de tu casa que escuchen. Si quieres, ten cerca el texto del poema.",
    "Aprenderé a recitar un poema nuevo en una condición distinta, como para otro público o con otra emoción. Sirve para adaptar lo que aprendí y confiar en mi capacidad de expresarme.",
    ["Sé comprender, marcar, ensayar y revisar un poema.", "Sé que ritmo, voz y gesto dependen del sentido."],
    [
        "Un poema se puede recitar de distintas maneras según la situación. La condición puede ser el público (niños pequeños o adultos), el lugar (una sala silenciosa o un patio con ruido) o la emoción que queremos transmitir (alegría, misterio, calma). Lo que no cambia es el sentido del poema; lo que cambia es cómo lo decimos.",
        "Veamos «La luna»: «La luna sube a la loma / con su linterna de plata; / las nubes, como ovejitas, / le abren paso en la noche clara.». Tiene dos imágenes: la luna con una linterna de plata y las nubes comparadas con ovejitas, con la palabra «como». Con niños pequeños, podríamos usar una voz cálida, un ritmo suave y un gesto de mano que sube como la luna. En un patio con ruido, hablaríamos más fuerte y con palabras muy claras.",
        "Para adaptar nos preguntamos: ¿quién escucha?, ¿dónde?, ¿qué emoción quiero que sienta? Y luego ajustamos volumen, ritmo, pausas y gestos. Después de recitar, revisamos con la pauta y notamos qué ajuste resultó mejor.",
    ],
    [("condición", "circunstancia que cambia, como el público o el lugar"), ("adaptar", "ajustar algo a una situación distinta"), ("comparación", "imagen que une dos cosas con «como»"), ("claridad", "decir las palabras de modo que se entiendan bien"), ("emoción", "lo que siente quien escucha o quien habla")],
    [
        ("Encontrar la comparación", "En «La luna», ¿qué comparación usa la palabra «como»: a) las nubes como ovejitas b) la luna como linterna?", ["Busco la palabra «como».", "Está en el tercer verso.", "Compara las nubes con ovejitas."], "a."),
        ("Adaptar al público", "Vas a recitar «La luna» a niños de cinco años. ¿Qué ajuste ayuda más: a) voz cálida, ritmo suave y un gesto de mano que sube b) voz muy seria y rápida?", ["Pienso en quién escucha.", "Los niños pequeños responden a la calidez.", "La a es la mejor."], "a."),
    ],
    [("Recitar igual para todos los públicos y lugares.", "No se piensa en quién escucha.", "Pregunta: ¿quién escucha y dónde? Ajusta volumen y gestos."), ("Cambiar el sentido del poema al adaptarlo.", "Se confunde adaptar con inventar.", "Mantén el sentido; cambia cómo lo dices.")],
    [
        E("¿Cuántos versos tiene «La luna»?", "Cuatro", "Son cuatro líneas."),
        E("¿La luna sube a la loma o baja al río?", "Sube a la loma", "El primer verso lo dice."),
        E("¿Con qué compara el poema a las nubes?", "Con ovejitas", "El tercer verso dice «como ovejitas»."),
    ],
    [
        E("Cuenta las comas del tercer verso, «las nubes, como ovejitas,». ¿Cuántas hay?", "Dos", "Una después de «nubes» y otra después de «ovejitas»."),
        E("¿Qué palabra marca la comparación en el tercer verso?", "Como", "Une las nubes con las ovejitas."),
        E("¿Qué cambia al adaptar un poema: el sentido o la manera de decirlo?", "La manera de decirlo", "El sentido se mantiene."),
    ],
    [
        E("Recitarás «La luna» en un patio con ruido. ¿Qué ajuste ayuda: a) hablar más fuerte y con palabras muy claras b) susurrar?", "a", "El ruido pide más volumen y claridad."),
        E("Quieres transmitir misterio con «La luna». ¿Qué ritmo conviene: a) lento, con pausas largas b) muy rápido?", "a", "El misterio se nota en un ritmo pausado."),
        E("Ordena para adaptar un poema: a) ajustar volumen y gestos, b) preguntar quién escucha y dónde, c) recitar y revisar. Escribe las letras.", "b, a, c", "Primero se analiza, luego se ajusta y después se recita."),
    ],
    [
        E("Un niño y una niña recitan «La luna» a niños pequeños. Él lo hace con voz seria y rápida; ella, con voz cálida y suave. ¿Quién adaptó mejor?", "Ella", "Pensó en su público."),
        E("Si adaptamos un poema a otro público, ¿puede cambiar su significado?", "No", "Solo cambia cómo lo decimos."),
    ],
    [
        E("Recitas «La luna» sin mirar el papel por primera vez. Te sale bien salvo un verso. ¿Qué conviene: a) repetir ese verso varias veces y volver a intentarlo b) rendirse?", "a", "Practicar ese verso mejora la memoria."),
        E("Para recitar «La luna» a adultos en una sala silenciosa, ¿qué volumen conviene: a) medio, claro, sin gritar b) muy fuerte?", "a", "El lugar silencioso no pide mucho volumen."),
    ],
    [E("Se te pide recitar «La luna» en una ceremonia al aire libre con viento. Eliges: voz clara y fuerte, pausas cortas en las comas, ritmo medio y un gesto con la mano al decir «sube». ¿Es una buena adaptación? Responde sí o no.", "Sí", "Ajusta volumen y claridad al lugar.")],
    [
        E("¿Un poema se recita igual en todos los lugares?", "No", "El lugar y el público influyen."),
        E("¿Adaptar es ajustar a una situación distinta?", "Sí", "Se cambian voz y ritmo."),
        E("¿Una comparación puede usar la palabra «como»?", "Sí", "Une dos cosas."),
    ],
    ("Recita un poema en una condición diferente. Aprende «La luna sube a la loma / con su linterna de plata; / las nubes, como ovejitas, / le abren paso en la noche clara.». Elige una condición: a) para un niño pequeño de tu casa o un peluche, b) en un lugar con ruido, c) con la emoción de misterio. Escribe qué cambiarás en volumen, ritmo y gesto, recítalo y pide a quien escuche que te diga una cosa que funcionó y una que mejorar.",
     "Condición: misterio. Ritmo lento, volumen suave pero claro y pausas largas al final de cada verso. Gesto: mano que sube como la luna. Opinión recibida: funcionó el ritmo lento; mejorar mirar más a quien escucha.",
     ["elige una condición y justifica los cambios", "mantiene el sentido del poema", "recita con claridad", "registra una opinión"], ["plan escrito y recitación frente a otra persona"], ["cambiar el sentido del poema", "no ajustar a la condición"],
     "Si no cambió nada en tu recitación, vuelve a pensar en la condición y ajusta el volumen."),
    "Recita «La luna» con dos emociones distintas y nota la diferencia.",
    "Escribe un poema de cuatro versos con una comparación con «como» y prepara cómo lo recitarías para niños pequeños.",
)

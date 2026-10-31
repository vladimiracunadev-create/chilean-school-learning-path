"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 31 (textos orales espontáneos o planificados: poemas, narraciones, dramatizaciones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA31 = "LE06 OA 31"
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


# ================================================================ OA 31 · clase 1
P_VIENTO = ("Poema original «El viento del cerro»: «Sobre el cerro sopla el viento, / lleva nubes de algodón; / canta bajito un lamento / y se esconde en el balcón.»")
P_SOL = ("Poema original «Mañana de sol»: «Camina el sol por el cerro, / tiñe de oro la mañana, / y despierta a los jilgueros / con su luz recién lavada.»")
reg(
    OA31, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu recitación.",
    "Aprenderé a recitar un poema usando el ritmo, la rima, las pausas y la entonación para expresar lo que dice. Sirve para disfrutar la poesía y comunicar emociones con la voz.",
    ["Sé que un poema se escribe en versos.", "Sé usar pausas y entonación al leer en voz alta."],
    [
        "Un poema es un texto escrito en versos, que son sus líneas. Un grupo de versos forma una estrofa. Muchos poemas tienen rima, que es la repetición de sonidos al final de los versos. La rima consonante repite vocales y consonantes desde la última vocal acentuada: «viento» y «lamento» riman en consonante. La rima asonante repite solo las vocales: «cerro» y «jilgueros» tienen las mismas vocales (e-o) y riman en asonante.",
        "Recitar es decir un poema de memoria o con una lectura expresiva. Para hacerlo bien, se cuida el ritmo (la cadencia de los versos), las pausas al final de cada verso o donde hay una coma, y la entonación según el sentimiento. Un poema tranquilo se dice más lento y suave; uno alegre, más ágil y con la voz más clara. El énfasis destaca las palabras clave, como las que riman.",
        "Un poema es un texto planificado: se prepara y se ensaya. Pero también podemos hablar poéticamente de manera espontánea, por ejemplo al describir un paisaje con imágenes. Antes de recitar, lee el poema entero, descubre qué emoción expresa y marca con lápiz las pausas y las palabras que enfatizarás. Después ensaya hasta que tu voz acompañe el mensaje.",
    ],
    [("verso", "cada línea de un poema"), ("estrofa", "grupo de versos"), ("rima consonante", "repite vocales y consonantes finales"), ("rima asonante", "repite solo las vocales finales"), ("recitar", "decir un poema con expresión")],
    [
        ("Reconocer la rima", f"{P_VIENTO} ¿Qué palabra rima con «viento»?", ["Miro el final de cada verso.", "«Lamento» termina igual que «viento».", "Es rima consonante."], "Lamento (rima consonante)."),
        ("Elegir el modo de recitar", "Un poema habla de una noche tranquila bajo la luna. ¿Cómo lo recitas: a) lento, suave y con pausas b) rápido y a gritos?", ["Identifico la emoción: calma.", "La calma se dice lento y suave.", "Elijo la opción a)."], "a) lento, suave y con pausas."),
    ],
    [("Recitar sin pausas, como si fuera un texto corrido.", "Se piensa que hay que terminar rápido.", "Haz pausas al final de cada verso."), ("Decir todo con la misma voz.", "Se olvida la emoción del poema.", "Adapta la entonación al sentimiento del poema.")],
    [
        E(f"{P_VIENTO} ¿Cuántos versos tiene el poema?", "4", "Hay cuatro líneas separadas por barras."),
        E(f"{P_VIENTO} ¿Qué palabra rima con «algodón»: balcón o cerro?", "Balcón", "Ambas terminan en «-ón»."),
        E("¿Cómo se llama cada línea de un poema: verso o estrofa?", "Verso", "La estrofa es un grupo de versos."),
    ],
    [
        E(f"{P_SOL} ¿Qué palabras riman en asonante con «cerro»: jilgueros o mañana?", "Jilgueros", "Las vocales finales de «cerro» y «jilgueros» son e-o."),
        E(f"{P_SOL} ¿La rima entre «mañana» y «lavada» es asonante o consonante?", "Asonante", "Repiten solo las vocales a-a."),
        E("Un poema alegre sobre una fiesta. ¿Cómo lo recitas: a) ágil y con voz clara b) muy lento y casi sin voz?", "a", "La alegría pide energía."),
    ],
    [
        E("Ordena de menor a mayor: a) un verso b) una estrofa de cuatro versos c) un poema con dos estrofas. Escribe las letras.", "a, b, c", "Un verso forma una estrofa y varias estrofas forman el poema."),
        E(f"{P_VIENTO} ¿Qué dos palabras deberías enfatizar por ser las rimas de los versos 1 y 3: viento y lamento o cerro y balcón?", "Viento y lamento", "Son las palabras con que terminan el primer y el tercer verso, y riman entre sí."),
        arith("Una estrofa tiene 4 versos y el poema, 3 estrofas. ¿Cuántos versos tiene el poema?", "4*3", "Cuatro versos por tres estrofas."),
    ],
    [
        E("Un estudiante dice: «Todos los poemas riman». ¿Es correcto? Responde sí o no.", "No", "Hay poemas sin rima."),
        E("Dos amigos recitan el mismo poema triste: uno rápido y a gritos, otro lento y suave. ¿Quién respeta mejor la emoción? Responde con «el primero» o «el segundo».", "El segundo", "La tristeza se expresa con ritmo lento y voz suave."),
    ],
    [
        E("«Sol» y «flor» solo repiten la vocal «o». ¿Es rima asonante o consonante?", "Asonante", "Repiten solo las vocales."),
        E("«Canción» y «corazón» repiten vocales y consonantes (-ón). ¿Es rima asonante o consonante?", "Consonante", "Repiten vocales y consonantes."),
    ],
    [E("En el acto de tu escuela debes recitar un poema sobre la lluvia que cae suavemente. ¿Qué plan de recitado eliges: a) voz suave, ritmo lento y pausas al final de cada verso b) voz fuerte y rápida?", "a", "Armonizan con la imagen de una lluvia suave.")],
    [
        E("En un poema, ¿cómo se llama el conjunto de varios versos seguidos, separado de otros por un espacio?", "Estrofa", "Reúne varios versos."),
        E("¿Recitar con pausas ayuda a que se entienda el poema? Responde sí o no.", "Sí", "Marcan el ritmo y los versos."),
        E("¿La entonación debe acompañar la emoción del poema? Responde sí o no.", "Sí", "Así se comunica el sentimiento."),
    ],
    ("Lee en voz alta este poema original: «Llueve fino sobre el techo, / suena un tambor de cristal; / se acurruca el gato inquieto / y el jardín empieza a cantar». 1) Anota cuántos versos hay y qué palabras riman al final de los versos 1 y 3 y de los versos 2 y 4. 2) Marca con barras dónde harás pausas. 3) Recítalo con voz suave y lenta, como una lluvia tranquila, a una persona de tu casa.",
     "1) Cuatro versos. «Techo» e «inquieto» riman en asonante; «cristal» y «cantar» también. 2) Pausa al final de cada verso. 3) Voz suave y lenta.",
     ["cuenta bien los versos y encuentra las rimas", "marca las pausas", "recita con ritmo y entonación adecuados"], ["notas y recitación"], ["recitar sin pausas", "no identificar rimas"],
     "Si el poema suena apurado, haz una pausa más larga al final de cada verso."),
    "Escribe una estrofa de cuatro versos con rima en el segundo y cuarto verso sobre el mar.",
    "Pide a una persona de tu casa que recite un verso o una canción y observa qué ritmo usa.",
)

# ================================================================ OA 31 · clase 2
N_EMA = ("Cuento original: «Una mañana de lluvia, Ema salió con su paraguas amarillo. En la esquina, el viento se lo llevó volando. Ema corrió detrás, saltó un charco y casi lo alcanzó, pero se detuvo en una banca. "
         "Un señor que vendía diarios atrapó el paraguas y se lo devolvió. Desde ese día, Ema saluda al vendedor cada mañana.»")
reg(
    OA31, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu narración.",
    "Aprenderé a contar una historia en voz alta con inicio, desarrollo y final, usando conectores y una voz expresiva. Sirve para entretener y para que otros sigan la historia sin perderse.",
    ["Sé que un cuento tiene personajes y un problema.", "Sé usar conectores para ordenar ideas."],
    [
        "Narrar oralmente es contar una historia en voz alta. Una narración tiene tres momentos. El inicio presenta a los personajes, el lugar y el tiempo. El desarrollo cuenta el problema y lo que ocurre para resolverlo. El desenlace muestra cómo termina. El narrador es quien cuenta la historia: puede ser un personaje («yo salí corriendo») o alguien que mira desde afuera («Ema salió corriendo»).",
        "Para que la historia se siga fácilmente, se usan conectores de tiempo: «una mañana», «de pronto», «entonces», «después», «finalmente» y «desde ese día». También ayuda variar la voz: más baja y lenta para crear suspenso, más rápida en la acción, más cálida en el final. Las pausas antes de un momento importante crean expectativa.",
        "Una narración puede ser planificada, si preparas lo que dirás, o espontánea, si cuentas algo que te pasó sin prepararlo. En ambos casos conviene ordenar los hechos en el tiempo y contar solo lo importante. Para ensayar, divide la historia en tres partes y cuéntala con tus palabras, sin memorizar frase por frase.",
    ],
    [("narración", "texto que cuenta hechos ocurridos a personajes"), ("narrador", "quien cuenta la historia"), ("desenlace", "parte donde se resuelve el problema"), ("conector de tiempo", "palabra que ordena los hechos en el tiempo"), ("suspenso", "tensión de esperar lo que ocurrirá")],
    [
        ("Ubicar un hecho", f"{N_EMA} El viento se lleva el paraguas de Ema. ¿En qué momento ocurre: inicio, desarrollo o desenlace?", ["El inicio presenta personajes y lugar.", "El viento causa el problema.", "El problema es parte del desarrollo."], "Desarrollo."),
        ("Mejorar con conectores", "Mejora «Ema corrió. El señor atrapó el paraguas. Ema lo saludó» con conectores de tiempo.", ["Busco un orden temporal.", "Agrego «de pronto» y «desde ese día».", "Reviso que suene natural."], "«Ema corrió. De pronto, el señor atrapó el paraguas. Desde ese día, Ema lo saluda»."),
    ],
    [("Contar los hechos mezclados, sin orden.", "Se cuenta como se recuerda.", "Ordénalos en el tiempo con conectores."), ("Contar todos los detalles, incluso los que no importan.", "Se cree que más es mejor.", "Cuenta solo lo que hace avanzar la historia.")],
    [
        E(f"{N_EMA} ¿Qué personaje atrapa el paraguas?", "El señor que vendía diarios", "El texto lo dice."),
        E(f"{N_EMA} ¿Qué objeto se lleva el viento?", "El paraguas de Ema", "Es el problema de la historia."),
        E(f"{N_EMA} ¿Cuál es el desenlace: a) Ema saluda cada mañana al vendedor b) el viento se lleva el paraguas?", "a", "Muestra cómo termina todo."),
    ],
    [
        E(f"{N_EMA} Ordena: a) el señor devuelve el paraguas b) Ema sale con su paraguas c) el viento se lo lleva. Escribe las letras.", "b, c, a", "Sigue el orden de los hechos."),
        E("¿Qué conector de tiempo marca algo repentino: de pronto o después?", "De pronto", "Señala una sorpresa."),
        E("«Yo salí corriendo detrás del paraguas». ¿El narrador es un personaje o alguien de afuera?", "Un personaje", "Habla en primera persona."),
    ],
    [
        E("Para crear suspenso antes del momento clave, ¿qué haces con la voz: a) bajarla y hacer una pausa b) hablar más rápido sin parar?", "a", "La pausa genera expectativa."),
        E("Quieres contar una anécdota de tu día. ¿Cuál orden sirve: a) inicio, desarrollo, desenlace b) desenlace, inicio, desarrollo?", "a", "Es el orden natural de una historia."),
        E("Elige la frase mejor para comenzar un cuento: a) «Una mañana de lluvia, una niña salió con su paraguas.» b) «El final fue lindo.»", "a", "Presenta personaje, tiempo y lugar."),
    ],
    [
        E("Un estudiante dice: «Para contar bien, hay que memorizar todo». ¿Es correcto? Responde sí o no.", "No", "Se puede contar con tus palabras siguiendo las tres partes."),
        E("Si cuentas algo que te pasó ayer sin prepararlo, ¿es una narración espontánea o planificada?", "Espontánea", "No fue preparada con anterioridad."),
    ],
    [
        E(f"{N_EMA} Si quieres contarlo en 20 segundos, ¿qué conservas: a) problema y resolución b) todos los detalles de la lluvia?", "a", "Es lo esencial de la historia."),
        arith("Una narración dura 3 minutos: 1 de inicio, 1 de desarrollo y el resto de desenlace. ¿Cuántos minutos dura el desenlace?", "3-1-1", "Se restan inicio y desarrollo del total."),
    ],
    [E("En el recreo, un compañero te pide que le cuentes lo que viste en un accidente de bicicleta (sin heridos). ¿Cuál relato sirve más: a) «Una bicicleta chocó con otra; nadie se hirió y se ayudaron a levantarse.» b) «Fue un accidente.»", "a", "Incluye hechos y final.")],
    [
        E("¿Cómo se llama la parte final de una narración?", "Desenlace", "Muestra cómo termina."),
        E("¿Los conectores de tiempo ordenan los hechos? Responde sí o no.", "Sí", "Indican qué ocurre antes y después."),
        E("¿Una narración puede ser espontánea? Responde sí o no.", "Sí", "Se puede contar algo sin prepararlo."),
    ],
    ("Cuenta oralmente (y anota en palabras clave) una historia de cinco o seis hechos sobre un día de lluvia en que se perdió algo. Usa al menos tres conectores de tiempo (una mañana, de pronto, finalmente, desde ese día), crea suspenso con una pausa antes del momento clave y termina con un desenlace claro. Cuéntala a una persona de tu casa y pregúntale qué parte entendió mejor.",
     "Una mañana, Tomás perdió su gorro. De pronto, lo vio sobre un perro... Finalmente, lo recuperó. Desde ese día, lo ata con un elástico.",
     ["tiene inicio, desarrollo y desenlace", "usa tres conectores de tiempo", "hay una pausa para el suspenso"], ["narración oral y notas"], ["mezclar el orden", "sin desenlace"],
     "Si se pierde el orden, anota los hechos en una línea de tiempo antes de contar."),
    "Escribe en tres oraciones el inicio, el desarrollo y el desenlace de una historia sobre un perro perdido.",
    "Cuenta a alguien una historia corta que hayas leído, con tus propias palabras.",
)

# ================================================================ OA 31 · clase 3
reg(
    OA31, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu descripción.",
    "Aprenderé a describir una actividad paso a paso, en orden y con palabras precisas, de modo que otra persona pueda hacerla. Sirve para explicar juegos, recetas sencillas o experimentos en voz alta.",
    ["Sé ordenar hechos en el tiempo.", "Sé usar conectores como «primero» y «luego»."],
    [
        "Describir una actividad es contar cómo se hace o cómo se hizo algo, en orden. Para ello se necesitan tres elementos: los materiales o lo que se necesita, los pasos en el orden correcto y el resultado esperado. Cada paso empieza con un verbo preciso: «mide», «mezcla», «coloca», «espera». Los conectores «primero», «luego», «después», «a continuación» y «finalmente» ordenan la secuencia.",
        "Hay dos modos. Si explicas cómo se hace algo, usas el presente o el imperativo: «Primero, coloca algodón en el vaso». Si cuentas una actividad que ya hiciste, usas el pasado: «Primero, coloqué algodón en el vaso». También conviene incluir datos exactos, como cantidades y tiempos: «riega con una cucharada de agua cada dos días». Los datos permiten repetir la actividad igual.",
        "Cuando lo explicas en voz alta, vas más lento, haces pausas entre pasos y muestras con tus manos o con los objetos lo que dices. Un buen oyente puede repetir los pasos sin ver tu texto. Si olvidas un paso, la actividad puede fallar: por eso conviene ensayar y revisar el orden antes de explicar.",
    ],
    [("secuencia", "serie de pasos en orden"), ("paso", "cada acción dentro de una actividad"), ("imperativo", "forma del verbo para dar instrucciones, como «mide»"), ("resultado", "lo que se obtiene al terminar"), ("dato exacto", "cantidad o tiempo preciso")],
    [
        ("Ordenar los pasos", "Para germinar un poroto en casa: a) regar con una cucharada de agua b) colocar algodón en un vaso plástico c) poner el poroto sobre el algodón. ¿Cuál es el orden?", ["Primero va el material base: algodón.", "Luego el poroto.", "Al final, el riego."], "b, c, a."),
        ("Agregar un dato exacto", "Mejora «Riega la planta de vez en cuando» con un dato exacto (cada dos días, una cucharada).", ["La frase es vaga.", "Agrego cantidad y frecuencia.", "Compruebo que se entienda."], "«Riega con una cucharada de agua cada dos días»."),
    ],
    [("Saltarse un paso porque «es obvio».", "Se piensa que todos lo saben.", "Revisa que cada paso esté dicho en orden."), ("Decir «un poco» y «de vez en cuando».", "Se cree que los datos exactos sobran.", "Di cantidades y tiempos.")],
    [
        E("¿Qué conector sirve para empezar una secuencia: primero o finalmente?", "Primero", "Indica el comienzo."),
        E("¿Cuál es un verbo preciso para dar instrucciones: coloca o cosa?", "Coloca", "Indica una acción concreta."),
        E("¿Qué se logra al terminar una actividad: el resultado o el material?", "El resultado", "Es lo que se obtiene."),
    ],
    [
        E("Ya tienes el jugo de limón en una jarra. Ordena los pasos que siguen para la limonada: a) servir en un vaso b) mezclar con una cuchara c) agregar agua y azúcar a la jarra. Escribe las letras.", "c, b, a", "Primero se agrega lo que se va a mezclar, luego se mezcla y al final se sirve."),
        E("Para explicar cómo se juega a las escondidas: «Primero, un jugador cuenta hasta diez mientras los demás se esconden». ¿Qué tipo de verbo usa «cuenta»: presente o pasado?", "Presente", "Explica cómo se hace."),
        E("Para contar lo que hiciste ayer, ¿qué tiempo usas: «coloqué algodón» o «coloca algodón»?", "Coloqué algodón", "Es pasado y cuenta una actividad hecha."),
    ],
    [
        arith("Para germinar un poroto, se riega cada 2 días durante 8 días, empezando el día 2. ¿Cuántos riegos son en total?", "8//2", "Se divide el tiempo total por el intervalo de riego."),
        E("Ordena la descripción de lavarse las manos: a) enjabonar durante 20 segundos b) mojar las manos c) secar con una toalla limpia d) enjuagar. Escribe las letras.", "b, a, d, c", "Se moja, se enjabona, se enjuaga y se seca."),
        E("En «Mezcla un poco de harina con agua», ¿qué dato exacto falta: la cantidad o el nombre del bol? Elige.", "La cantidad", "«Un poco» no es una medida."),
    ],
    [
        E("Un estudiante dice: «En una descripción oral no hace falta el orden». ¿Es correcto? Responde sí o no.", "No", "El orden permite repetir la actividad."),
        E("Si alguien olvida el paso «poner el poroto sobre el algodón», ¿se puede lograr el resultado? Responde sí o no.", "No", "Falta un paso clave."),
    ],
    [
        E("Quieres explicar cómo plantar una semilla de manera clara. ¿Qué descripción es mejor: a) «Pon algodón en un vaso plástico, coloca una semilla encima y riega con una cucharada de agua cada dos días.» b) «Pon la semilla y listo.»", "a", "Tiene materiales, pasos y datos exactos."),
        E("Frase: «Espera un buen rato». ¿Cómo la mejoras: a) «Espera veinte minutos.» b) «Espera mucho.»", "a", "Entrega un dato exacto."),
    ],
    [E("En la clase de educación física debes explicar a tu curso cómo jugar a la escondida (sin riesgos). Quieres que se entienda sin errores. ¿Qué haces: a) ordenar los pasos y decir las reglas de seguridad b) explicar sin orden?", "a", "Así todos entienden y juegan seguros.")],
    [
        E("¿Cómo se llama la serie de pasos de una actividad?", "Secuencia", "Es el orden de pasos."),
        E("¿Los datos exactos ayudan a repetir una actividad? Responde sí o no.", "Sí", "Se puede hacer igual."),
        E("¿Los verbos precisos ayudan a explicar? Responde sí o no.", "Sí", "Dicen con claridad qué hacer."),
    ],
    ("Elige una actividad sencilla y segura: «preparar una limonada», «hacer un avión de papel» o «lavar las manos». Escribe en cinco pasos cómo se hace, con materiales, verbos precisos, datos exactos y conectores. Luego explícaselo en voz alta a una persona de tu casa mostrando cada paso con las manos y pregúntale si podría repetirlo.",
     "Avión de papel: Materiales: una hoja. Primero, dobla la hoja por la mitad. Luego, dobla las esquinas hacia el centro. Después, dobla de nuevo por la mitad. A continuación, baja las alas. Finalmente, lánzalo con suavidad, sin apuntar a nadie.",
     ["incluye materiales", "tiene cinco pasos en orden", "usa verbos precisos y conectores", "incluye al menos un dato exacto"], ["cinco pasos escritos y explicados en voz alta"], ["saltarse pasos", "usar frases vagas"],
     "Si la persona no logró repetirlo, revisa qué paso faltó o qué dato no era claro."),
    "Escribe tres pasos para explicar cómo guardar tu mochila al llegar a casa.",
    "Observa cómo una persona de tu casa prepara algo sencillo y cuenta los pasos que sigue.",
)

# ================================================================ OA 31 · clase 4
NOT_PLAYA = ("Noticia original: «Ayer, 25 estudiantes de sexto básico limpiaron la orilla de la playa de su ciudad durante 2 horas. Recogieron 75 kilos de basura, en su mayoría envases plásticos. "
             "La actividad fue organizada por el centro de estudiantes para cuidar el entorno.»")
reg(
    OA31, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu noticia y tu testimonio.",
    "Aprenderé a relatar una noticia (hechos) y un testimonio (vivencia propia) en voz alta, diferenciando uno de otro. Sirve para informar con claridad y para contar lo que viví con mis propias palabras.",
    ["Sé contar una historia en orden.", "Sé que una noticia informa sobre hechos reales."],
    [
        "Una noticia relata hechos reales y recientes, de manera objetiva. Para hacerlo bien se responden seis preguntas: ¿qué ocurrió?, ¿quién participó?, ¿cuándo?, ¿dónde?, ¿cómo? y ¿por qué? Se usa la tercera persona («los estudiantes limpiaron») y se evita dar opiniones personales. Primero se dice lo más importante y luego los detalles.",
        "Un testimonio es el relato de lo que una persona vivió o presenció. Se cuenta en primera persona («yo estuve allí y vi…»), incluye sentimientos y detalles de la experiencia, y por eso es subjetivo. Puede complementar una noticia: la noticia dice que 25 estudiantes recogieron 75 kilos, y el testimonio cuenta cómo se sintió una de ellas al hacerlo.",
        "Al relatar en voz alta, mantén una voz clara y un ritmo calmado. En una noticia, usa un tono serio y neutro; en un testimonio, puedes expresar emociones. Distinguir hechos de opiniones es importante: «recogieron 75 kilos» es un hecho que se puede comprobar; «fue una actividad maravillosa» es una opinión.",
    ],
    [("noticia", "relato de hechos reales y recientes"), ("testimonio", "relato de lo que alguien vivió o presenció"), ("objetivo", "que se limita a los hechos"), ("subjetivo", "que incluye sentimientos y opiniones"), ("tercera persona", "forma de contar desde afuera, con «él», «ella» o «ellos»")],
    [
        ("Responder las preguntas de la noticia", f"{NOT_PLAYA} ¿Quién participó y dónde?", ["Busco los participantes: 25 estudiantes de sexto básico.", "Busco el lugar: la playa.", "Lo uno en una respuesta."], "25 estudiantes de sexto básico participaron en la playa de su ciudad."),
        ("Distinguir hecho y opinión", "«Recogieron 75 kilos de basura» y «fue una actividad maravillosa». ¿Cuál es un hecho?", ["Un hecho se puede comprobar.", "Los kilos se pueden pesar.", "«Maravillosa» es una apreciación."], "«Recogieron 75 kilos de basura»."),
    ],
    [("Mezclar opiniones en una noticia.", "Se cree que dar opinión la hace más interesante.", "Informa los hechos y deja las opiniones para el testimonio."), ("Contar un testimonio en tercera persona.", "Se confunde con la noticia.", "Usa «yo» y cuenta cómo lo viviste.")],
    [
        E(f"{NOT_PLAYA} ¿Cuántos estudiantes participaron?", "25", "El texto lo indica."),
        E(f"{NOT_PLAYA} ¿Cuánto tiempo duró la limpieza?", "2 horas", "El texto lo indica."),
        E("«Yo estuve allí y me sentí feliz». ¿Es una noticia o un testimonio?", "Un testimonio", "Habla en primera persona y expresa emociones."),
    ],
    [
        E(f"{NOT_PLAYA} ¿Qué recogieron en su mayoría: envases plásticos o botellas de vidrio?", "Envases plásticos", "El texto lo dice."),
        E("«La jornada fue maravillosa.» ¿Es un hecho o una opinión?", "Una opinión", "No se puede comprobar con datos."),
        E(f"{NOT_PLAYA} ¿Quién organizó la actividad?", "El centro de estudiantes", "El texto lo indica."),
    ],
    [
        arith("En otra jornada de limpieza, 12 estudiantes recogieron 60 kilos de basura en total. Si cada uno recogió lo mismo, ¿cuántos kilos recogió cada uno?", "60//12", "Se reparte el total entre los participantes."),
        E("Ordena una noticia: a) los detalles b) el hecho principal c) el cierre con datos de contexto. Escribe las letras.", "b, a, c", "Primero lo más importante, luego los detalles y el contexto."),
        E("Convierte el testimonio «Yo recogí cinco botellas y me sentí orgullosa» a noticia en tercera persona: ¿cuál es adecuada? a) «Una estudiante recogió cinco botellas.» b) «Yo recogí cinco botellas.»", "a", "La noticia usa tercera persona y evita el sentimiento personal."),
    ],
    [
        E("Un estudiante dice: «Una noticia debe contar cómo me sentí». ¿Es correcto? Responde sí o no.", "No", "La noticia informa hechos; los sentimientos van en el testimonio."),
        E(f"{NOT_PLAYA} Si un testimonio dice «Fue duro cargar las bolsas», ¿agrega un sentimiento que la noticia no tiene? Responde sí o no.", "Sí", "La noticia solo da los hechos."),
    ],
    [
        E("Una compañera quiere relatar un testimonio sobre un día de lluvia. ¿Cuál comienzo es mejor: a) «Ese día, yo iba camino al colegio cuando empezó a llover fuerte.» b) «Se informa que llovió.»", "a", "Cuenta una vivencia en primera persona."),
        E("Quieres informar la noticia en 20 segundos. ¿Qué eliges contar: a) qué pasó, quién, cuándo y dónde b) tu opinión sobre el clima?", "a", "Son los datos esenciales de una noticia."),
    ],
    [E("En el diario mural del curso, tu tarea es relatar en voz alta una noticia sobre el campeonato de ajedrez. Datos: ayer, 12 estudiantes jugaron en la biblioteca y ganó Javiera. ¿Qué relato corresponde a una noticia: a) «Ayer, 12 estudiantes jugaron ajedrez en la biblioteca y ganó Javiera.» b) «Yo jugué y me encantó.»", "a", "Informa quién, qué, cuándo y dónde sin opiniones.")],
    [
        E("¿Cómo se llama el relato de lo que alguien vivió o presenció?", "Testimonio", "Se cuenta en primera persona."),
        E("¿Una noticia debe basarse en hechos reales? Responde sí o no.", "Sí", "Informa de lo que ocurrió."),
        E("¿Un testimonio puede incluir sentimientos? Responde sí o no.", "Sí", "Cuenta una experiencia personal."),
    ],
    ("Lee estos datos: «Ayer, en la biblioteca de la escuela, 12 estudiantes de sexto jugaron un torneo de ajedrez durante una hora. Ganó Javiera». 1) Relata en voz alta una noticia de 3 oraciones con qué, quién, cuándo y dónde, sin opiniones. 2) Relata un testimonio de 3 oraciones como si fueras Javiera, en primera persona y con un sentimiento. Cuéntalo a una persona de tu casa.",
     "Noticia: Ayer, 12 estudiantes jugaron un torneo de ajedrez en la biblioteca. La actividad duró una hora. Ganó Javiera. Testimonio: Yo jugué contra todos y estaba nerviosa...",
     ["la noticia responde las preguntas básicas", "evita opiniones", "el testimonio usa primera persona", "el testimonio incluye un sentimiento"], ["noticia y testimonio dichos u escritos"], ["incluir opinión en la noticia", "usar tercera persona en el testimonio"],
     "Subraya cada opinión de tu noticia y quítala."),
    "Escribe una oración de noticia y una de testimonio sobre una fiesta del colegio.",
    "Escucha una noticia en la radio y anota quién, qué, cuándo y dónde.",
)

# ================================================================ OA 31 · clase 5
G_PUERTA = ("Mini guion original «La puerta del museo»: NARRADORA: Un museo, antes de abrir. GUARDIA (mirando el reloj): «Faltan cinco minutos.» "
            "VISITANTE (golpeando, impaciente): «¡Por favor, ábrame!» GUARDIA (sonriendo): «Paciencia, ya falta poco.»")
reg(
    OA31, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para dramatizar la escena a dos voces.",
    "Aprenderé a dramatizar una escena: leer un guion, interpretar un personaje con la voz y los gestos, y respetar los turnos. Sirve para expresar emociones y trabajar en equipo.",
    ["Sé usar la voz y los gestos para expresar emociones.", "Sé respetar los turnos para hablar."],
    [
        "Dramatizar es representar una historia con personajes, hablando y actuando. Un guion es el texto que dice quién habla y qué dice. Los diálogos son las intervenciones de los personajes. Las acotaciones son indicaciones, generalmente entre paréntesis, que dicen cómo actuar: «(sonriendo)», «(golpeando, impaciente)». No se leen en voz alta: guían la voz y el gesto.",
        "Para interpretar un personaje, decide cómo es: sus emociones, cómo habla y cómo se mueve. Un personaje impaciente habla rápido y con volumen alto; uno calmado, lento y suave. Los gestos acompañan: mirar el reloj, golpear la puerta, sonreír. Y se respetan los turnos: se espera que el otro termine de hablar y se entra a tiempo con la réplica.",
        "También se puede improvisar, es decir, dramatizar sin guion, inventando lo que se dice en el momento. La improvisación es un texto espontáneo; el guion, uno planificado. En ambos casos se necesita escuchar al compañero, mantener el personaje y cuidar la historia. Antes de dramatizar, ensaya al menos dos veces y ajusta los volúmenes para que todos te oigan.",
    ],
    [("dramatizar", "representar una historia con personajes"), ("guion", "texto con los diálogos y acciones de una escena"), ("acotación", "indicación entre paréntesis sobre cómo actuar"), ("improvisar", "actuar o hablar sin texto preparado"), ("réplica", "respuesta de un personaje a lo que dijo otro")],
    [
        ("Reconocer acotaciones", f"{G_PUERTA} ¿Cuál es una acotación del guion?", ["Las acotaciones están entre paréntesis.", "Busco una de ellas.", "«(mirando el reloj)» es una."], "«(mirando el reloj)»."),
        ("Decidir la voz de un personaje", "El visitante está impaciente. ¿Cómo dices «¡Por favor, ábrame!»: a) rápido, con volumen alto y golpeando b) lento, suave y bostezando?", ["Impaciente significa con prisa.", "La prisa se expresa con rapidez y fuerza.", "Elijo a)."], "a) rápido, con volumen alto y golpeando."),
    ],
    [("Leer en voz alta las acotaciones.", "Se confunden con parte del diálogo.", "Las acotaciones se actúan, no se leen."), ("Hablar antes de que el compañero termine.", "Se olvidan los turnos.", "Espera la réplica y entra a tiempo.")],
    [
        E(f"{G_PUERTA} ¿Qué dos personajes dialogan en la escena: el guardia y el visitante, o la narradora y el guardia?", "El guardia y el visitante", "La narradora solo describe el lugar; dialogan el guardia y el visitante."),
        E(f"{G_PUERTA} ¿Qué dice el guardia sonriendo?", "Paciencia, ya falta poco", "La acotación «sonriendo» acompaña esa frase."),
        E("¿Dónde se escriben las acotaciones: entre paréntesis o entre comillas?", "Entre paréntesis", "Así se distinguen del diálogo."),
    ],
    [
        E(f"{G_PUERTA} ¿Qué gesto indica el guion para el visitante: golpear la puerta o sonreír?", "Golpear la puerta", "Está en la acotación del visitante."),
        E(f"{G_PUERTA} ¿Qué emoción debe mostrar el visitante: impaciencia o tristeza?", "Impaciencia", "La acotación lo indica."),
        E("¿Cómo se llama actuar sin guion: improvisar o recitar?", "Improvisar", "Es inventar en el momento."),
    ],
    [
        E(f"{G_PUERTA} ¿Cuál es la voz más adecuada para el guardia que sonríe y dice «Paciencia»: a) calmada y amable b) enojada y fuerte?", "a", "La acotación sugiere calma."),
        E("Ordena el ensayo de una escena: a) leer el guion b) ajustar volumen y gestos c) decidir cómo es cada personaje d) ensayar dos veces. Escribe las letras.", "a, c, d, b", "Se lee, se decide el personaje, se ensaya y se ajusta."),
        E("En un guion, un personaje debe decir «(susurrando) No hagas ruido». ¿Cómo dices la frase: en voz baja o a gritos?", "En voz baja", "La acotación indica susurrar."),
    ],
    [
        E("Un estudiante dice: «Si me equivoco en la dramatización, debo detener todo». ¿Es lo mejor? Responde sí o no.", "No", "Conviene continuar y adaptarse como en una improvisación."),
        E("Dos estudiantes hablan al mismo tiempo en una dramatización. ¿Qué norma no respetaron: los turnos o las acotaciones?", "Los turnos", "Deben esperar la réplica."),
    ],
    [
        E("En la escena del museo, el visitante pregunta «¿Falta mucho?». Elige la réplica adecuada para el guardia: a) «(mirando el reloj) Cinco minutos.» b) «(durmiendo) Zzz.»", "a", "Es coherente con la escena."),
        E("Para improvisar bien, ¿qué haces primero: escuchar al compañero o ignorarlo?", "Escuchar al compañero", "Así la réplica se conecta con lo dicho."),
    ],
    [E("Tu curso dramatizará una escena en una biblioteca. Un compañero dice sus frases muy bajito y el público no lo oye. ¿Qué le sugieres: a) subir el volumen sin gritar y mirar al público b) hablar más rápido?", "a", "Mejora lo audible sin perder expresión.")],
    [
        E("¿Cómo se llama el texto de una dramatización?", "Guion", "Dice quién habla y qué dice."),
        E("¿Las acotaciones se leen en voz alta? Responde sí o no.", "No", "Se actúan, no se leen."),
        E("¿Hay que respetar los turnos al dramatizar? Responde sí o no.", "Sí", "Permite entender la escena."),
    ],
    ("Dramatiza con una persona de tu casa o contigo mismo (cambiando de voz) esta escena original: «La biblioteca. BIBLIOTECARIA (ordenando libros): ‘Buenas tardes’. NIÑO (entrando con prisa): ‘¡Necesito un libro de dinosaurios para mañana!’. BIBLIOTECARIA (sonriendo): ‘Tenemos tres. ¿Cuál prefieres?’. NIÑO (sorprendido): ‘¡Los quiero todos!’». Ensáyala dos veces, respeta las acotaciones y los turnos, y cambia la voz de cada personaje. Anota qué mejoraste en el segundo ensayo.",
     "Mejoré el volumen del niño, que se oía poco, y la bibliotecaria hizo una pausa antes de sonreír.",
     ["respeta las acotaciones", "respeta los turnos", "cambia la voz de cada personaje", "anota una mejora"], ["dos ensayos y una nota"], ["leer las acotaciones", "hablar encima del otro"],
     "Si se pisan las voces, marca en el guion cuándo termina cada réplica."),
    "Escribe una acotación para cada frase: «¡No puede ser!» y «Te estaba esperando».",
    "Observa una escena de teatro o televisión y anota una acotación que podrías escribir.",
)

# ================================================================ OA 31 · clase 6
reg(
    OA31, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que escuche tu presentación y te ayude a revisarla.",
    "Aprenderé a elegir y adaptar un texto oral (poema, narración o dramatización) según su audiencia, y a revisarlo con una pauta antes de presentarlo. Sirve para desarrollar mi capacidad expresiva en situaciones planificadas y espontáneas.",
    ["Sé recitar, narrar y dramatizar.", "Sé la diferencia entre un texto oral planificado y uno espontáneo."],
    [
        "Un texto oral espontáneo se dice sin preparación: una conversación, una respuesta o una anécdota contada en el momento. Uno planificado se prepara antes: un poema recitado, una narración ensayada o una dramatización con guion. En los dos casos importa la capacidad expresiva, es decir, usar bien la voz, el cuerpo y las palabras para comunicar. Pero el planificado permite revisar y mejorar.",
        "Antes de presentar, hay que pensar en la audiencia: ¿quiénes son?, ¿cuánto saben del tema?, ¿cuánto tiempo tengo? Para un grupo de niños pequeños, se usan palabras más simples, frases cortas y una voz muy expresiva. Para adultos, se puede usar un vocabulario más variado. El tiempo también importa: si tienes dos minutos, conviene elegir lo esencial.",
        "Para revisar, usa una pauta con criterios observables: la voz se oye; hay pausas y entonación; se cuenta con orden; el vocabulario es claro; se usan gestos adecuados; se respeta el tiempo; y se mira a la audiencia. Marca cuáles cumples y cuáles debes mejorar. Con una segunda práctica, la mayoría de los detalles mejora de manera notoria.",
    ],
    [("texto oral espontáneo", "texto que se dice sin preparación previa"), ("texto oral planificado", "texto preparado y ensayado antes"), ("capacidad expresiva", "habilidad para comunicar usando voz, cuerpo y palabras"), ("audiencia", "personas que escuchan"), ("pauta", "lista de criterios para revisar")],
    [
        ("Clasificar", "Conversas con un amigo sobre lo que hiciste ayer, sin preparar nada. ¿Es un texto oral espontáneo o planificado?", ["No lo preparaste.", "Surgió en el momento.", "Es espontáneo."], "Espontáneo."),
        ("Adaptar a la audiencia", "Quieres contar un cuento a niños de primero básico. ¿Qué haces: a) usar palabras simples y una voz muy expresiva b) usar palabras difíciles y hablar en voz baja?", ["Pienso en quiénes me escuchan.", "Niños pequeños necesitan claridad.", "Elijo a)."], "a)."),
    ],
    [("Presentar sin pensar en quién escucha.", "Se piensa que todos entienden lo mismo.", "Pregúntate quiénes son, qué saben y cuánto tiempo tienes."), ("No revisar con ninguna pauta.", "Se cree que ensayar basta.", "Marca los criterios y mejora lo que falta.")],
    [
        E("Un poema recitado en un acto escolar tras varios ensayos, ¿es espontáneo o planificado?", "Planificado", "Se prepara y ensaya antes."),
        E("Responder una pregunta de la profesora sin preparación, ¿es espontáneo o planificado?", "Espontáneo", "Se dice en el momento."),
        E("Para niños pequeños, ¿qué conviene: palabras simples o palabras muy difíciles?", "Palabras simples", "Facilitan la comprensión."),
    ],
    [
        E("Tienes 2 minutos para contar una historia. ¿Qué haces: a) elegir lo esencial b) contar todos los detalles aunque no alcance el tiempo?", "a", "Así respetas el tiempo."),
        E("¿Cuál criterio de la pauta es observable: «se oye hasta la última fila» o «me siento bien»?", "Se oye hasta la última fila", "Se puede comprobar."),
        E("Quieres adaptar un poema de la lluvia para niños pequeños. ¿Qué aportas con la voz: más expresividad o menos expresividad?", "Más expresividad", "Ayuda a captar su atención."),
    ],
    [
        arith("Tienes 6 minutos para presentar. Planificas 2 minutos de poema, 3 de narración y el resto para saludar y agradecer. ¿Cuántos minutos quedan para saludar y agradecer?", "6-2-3", "Se restan las partes planificadas del tiempo total."),
        E("Ordena el proceso: a) presentar b) elegir el texto según la audiencia c) revisar con la pauta d) ensayar. Escribe las letras.", "b, d, c, a", "Se elige, se ensaya, se revisa y se presenta."),
        E("Revisión: tu pauta indica «hay pausas y entonación». En tu ensayo recitaste todo seguido, sin pausas. ¿Qué debes mejorar: las pausas o el vocabulario?", "Las pausas", "Es el criterio que no se cumplió."),
    ],
    [
        E("Un estudiante dice: «Un texto espontáneo no necesita cuidar la expresión». ¿Es correcto? Responde sí o no.", "No", "También se cuida la expresión, aunque no se prepare."),
        E("Dos exposiciones del mismo poema: una con voz monótona y la otra con pausas y entonación. ¿Cuál muestra mayor capacidad expresiva?", "La segunda", "Usa mejor la voz para comunicar."),
    ],
    [
        E("Vas a recitar un poema de 4 versos ante tu curso. Tu pauta incluye: se oye, hay pausas, hay entonación, mira al público. En el ensayo, cumples tres y no miras al público. ¿Qué debes mejorar?", "Mirar al público", "Es el criterio que falta."),
        E("Para contar un cuento a niños de cinco años, ¿qué ajuste es mejor: a) frases cortas y voces de personajes b) un vocabulario técnico muy formal?", "a", "Capta la atención de niños pequeños."),
    ],
    [E("Tu curso hará un acto con poema, narración y dramatización. Hay 9 minutos disponibles. ¿Cuál reparto es adecuado: a) 3 minutos para cada uno b) 9 minutos para el poema y nada para los demás?", "a", "Permite que los tres tipos de texto se presenten.")],
    [
        E("¿Cómo se llama el texto oral que se prepara y ensaya antes?", "Planificado", "Se prepara con anticipación."),
        E("¿Conviene pensar en la audiencia antes de presentar? Responde sí o no.", "Sí", "Determina las palabras y el tiempo."),
        E("¿Una pauta ayuda a revisar? Responde sí o no.", "Sí", "Permite comprobar criterios."),
    ],
    ("Elige uno de estos textos para presentar: el poema «Llueve fino sobre el techo, / suena un tambor de cristal; / se acurruca el gato inquieto / y el jardín empieza a cantar», un cuento breve que tú inventes de cinco hechos o la escena de la biblioteca de la clase anterior. Adáptalo para niños de seis años (palabras simples, voz muy expresiva) y úsalo con esta pauta: 1) se oye, 2) hay pausas, 3) hay entonación, 4) usa gestos, 5) mira al público, 6) respeta 2 minutos. Ensáyalo dos veces y marca con una cruz qué cumpliste en cada ensayo.",
     "Ensayo 1: se oye, pausas, entonación. Ensayo 2: se agregan gestos y mirada al público.",
     ["elige un texto y lo adapta", "usa la pauta de seis criterios", "ensaya dos veces", "mejora al menos un criterio"], ["pauta marcada en dos ensayos"], ["no adaptar al público", "marcar la pauta sin ensayar"],
     "Si no mejoras ningún criterio, elige el que más te cueste y practícalo tres veces."),
    "Escribe cómo cambiarías la presentación de un cuento para niños de primero básico y para adultos.",
    "Presenta tu texto a una persona de tu casa y pídele que marque la pauta.",
)

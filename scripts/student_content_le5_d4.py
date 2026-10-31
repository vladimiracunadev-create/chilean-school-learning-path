"""Cuaderno del estudiante, 5.º básico Lenguaje y Comunicación: OA 29 (clases 4 y 5) y OA 30 (clases 1 y 2)."""
from __future__ import annotations

from student_content_le5_d import E, reg
from student_lessons import arith

OA29 = "LE05 OA 29"
OA30 = "LE05 OA 30"

# ================================================================ OA 29 · clase 4
reg(
    OA29, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar sobre qué palabra elegirían ustedes.",
    "Aprenderé a comparar palabras de significado cercano y a decidir cuál es la más pertinente según la situación y la intensidad. Sirve para hablar con más exactitud.",
    ["Sé inferir el significado de una palabra con pistas.", "Sé usar palabras nuevas con sentido y concordancia."],
    [
        "Hay palabras que significan algo parecido, pero no son iguales. Por ejemplo, «molesto», «enojado» y «furioso» hablan de enojo, pero con distinta intensidad: molesto es sentir una incomodidad leve; enojado, sentir rabia; furioso, sentir una rabia muy intensa. Elegir la palabra con el matiz justo hace que nos entiendan mejor.",
        "También hay matices de situación. «Indignado» es estar muy enojado por algo que parece injusto. «Cauteloso» es actuar con cuidado para evitar un riesgo, y «temeroso» es sentir miedo. Una persona puede cruzar un puente angosto de forma cautelosa, mirando cada tabla, sin sentir terror; otra puede ir temerosa, temblando. Las dos palabras no son sinónimos exactos.",
        "Para decidir entre dos palabras, nos preguntamos: ¿qué intensidad tiene lo que pasó?, ¿qué causó el sentimiento o la acción?, ¿es una situación formal o cotidiana? Comparamos las opciones con la situación y elegimos la que mejor calza. Una decisión bien tomada se puede explicar: «Elegí indignado porque lo que pasó parece injusto».",
    ],
    [("molesto", "con una incomodidad leve"), ("enojado", "con rabia"), ("furioso", "con una rabia muy intensa"), ("indignado", "muy enojado por algo que parece injusto"), ("cauteloso", "que actúa con cuidado para evitar un riesgo"), ("temeroso", "que siente miedo")],
    [
        ("Elegir por intensidad", "A Tomás le incomodó un poco que lo interrumpieran. ¿Qué palabra es más exacta: «molesto» o «furioso»?", ["Veo cuánta rabia hubo: poca.", "Furioso es una rabia muy intensa.", "Molesto es incomodidad leve."], "Molesto."),
        ("Elegir por causa", "Los vecinos supieron que un grupo botó basura en la plaza que ellos cuidan y lo sintieron como una injusticia. ¿Qué palabra es más exacta: «molestos» o «indignados»?", ["Busco la causa: algo que parece injusto.", "Indignado se usa para eso.", "Elijo indignados."], "Indignados."),
    ],
    [("Creer que todas las palabras de una lista son iguales.", "Se piensa que sirven para lo mismo.", "Compara intensidad y causa antes de elegir."), ("Usar siempre la palabra más fuerte para que suene importante.", "Se confunde exageración con precisión.", "Elige la que corresponde a lo que pasó.")],
    [
        E("¿Cuál expresa más enojo: «molesto» o «furioso»?", "Furioso", "Es una rabia muy intensa."),
        E("¿Cuál palabra significa sentir miedo: «temeroso» o «cauteloso»?", "Temeroso", "Cauteloso significa actuar con cuidado."),
        E("¿Cuál palabra significa estar muy enojado por algo injusto: «indignado» o «contento»?", "Indignado", "Se refiere a un enojo por una injusticia."),
    ],
    [
        E("Ordena de menor a mayor enojo. a) furioso b) molesto c) enojado. Escribe las letras.", "b, c, a", "Molesto es leve, enojado es medio y furioso es lo más intenso."),
        E("Nico cruza un puente angosto mirando cada tabla para no caerse, sin temblar. ¿Qué palabra le calza: «cauteloso» o «temeroso»?", "Cauteloso", "Actúa con cuidado para evitar un riesgo."),
        E("Completa: «Al enterarse de la injusticia, los vecinos quedaron ______». Opciones: indignados / contentos.", "Indignados", "La causa es una injusticia."),
    ],
    [
        E("A Rosa le incomodó un poco que sonara un timbre mientras hablaba. ¿Qué palabra elegirías para contar cómo se sintió: a) furiosa b) molesta?", "b", "La intensidad es leve."),
        E("En una exposición formal, ¿qué frase es más adecuada: a) «La investigación fue meticulosa.» b) «La investigación fue re cuidadosa po.»", "a", "Mantiene un registro cuidado."),
        E("Pía temblaba de miedo al cruzar el pasillo oscuro. ¿Cómo estaba: «temerosa» o «cautelosa»?", "Temerosa", "Temblaba porque sentía miedo."),
    ],
    [
        E("Ema dice que «indignado» y «molesto» son lo mismo. Leo dice que «indignado» es más fuerte y se relaciona con injusticia. ¿Quién tiene razón?", "Leo", "Las dos palabras tienen distinta intensidad y causa."),
        E("Dices «estoy furioso» solo porque se te cayó el borrador. ¿Qué palabra sería más exacta: «molesto» o «indignado»?", "Molesto", "La incomodidad es leve."),
    ],
    [
        E("Compara: A) «La biblioteca tenía pocos libros, eran abundantes.» B) «La biblioteca tenía pocos libros, eran escasos.» ¿Cuál es correcta?", "B", "Escasos significa que hay pocos."),
        E("Los vecinos descubren que alguien cortó el árbol de la plaza sin avisar a nadie y les parece injusto. Elige la palabra más exacta: a) molestos b) indignados c) temerosos.", "b", "Combina enojo e injusticia."),
    ],
    [E("Ayer perdiste tu goma de borrar favorita y te incomodó un poco. En tu relato oral, ¿qué palabra es más exacta: a) molesto b) furioso?", "a", "La incomodidad fue leve.")],
    [
        E("¿«Furioso» tiene más intensidad que «enojado»? Responde sí o no.", "Sí", "Furioso es una rabia muy intensa."),
        E("¿Cauteloso y temeroso significan exactamente lo mismo? Responde sí o no.", "No", "Uno actúa con cuidado y el otro siente miedo."),
        E("Para elegir entre dos palabras, ¿conviene comparar intensidad y causa? Responde sí o no.", "Sí", "Así se elige la más exacta."),
    ],
    ("Lee estas tres situaciones y elige para cada una la palabra más exacta (molesto, furioso, indignado, cauteloso, temeroso): 1) un compañero te pisó la mochila sin querer y te incomodó un poco; 2) la señora de la panadería vio que alguien se coló en la fila delante de personas mayores y le pareció injusto; 3) un niño camina por la orilla de una vereda mojada mirando cada paso. Escribe una oración oral con cada palabra y explica por qué la elegiste.",
     "1) molesto: «Me sentí molesto porque me pisaron la mochila». 2) indignada: «La señora quedó indignada porque fue injusto». 3) cauteloso: «El niño caminó cauteloso para no resbalar».",
     ["elige la palabra por intensidad o causa", "la oración es coherente", "explica la decisión"], ["tres palabras elegidas", "tres oraciones", "explicación oral"], ["usar siempre la palabra más fuerte", "no explicar la decisión"],
     "Si dudas entre dos, pregúntate: ¿qué intensidad tuvo? ¿qué lo causó?"),
    "Escribe un sinónimo cercano y una palabra de distinta intensidad para «enojado».",
    "Anota en una lista tres palabras que expresen alegría, de menor a mayor intensidad.",
)

# ================================================================ OA 29 · clase 5
reg(
    OA29, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu intervención.",
    "Aprenderé a planificar una intervención oral breve donde uso vocabulario nuevo de forma pertinente. Sirve para mostrar lo que aprendí en una exposición o conversación.",
    ["Sé inferir el significado de palabras nuevas.", "Sé elegir la palabra más exacta."],
    [
        "Para incorporar palabras nuevas en una intervención oral, conviene planificar. Primero elegimos tres palabras que realmente encajen con el tema. Luego escribimos una oración para cada una, comprobando sentido, concordancia y registro. Después las ordenamos dentro de un plan con saludo, tema, ideas y cierre.",
        "Modelo de intervención: «Hoy les contaré cómo cuidamos el huerto del curso. Mi compañera Sara fue meticulosa: regó cada surco y anotó los días. Mi compañero Iván fue tenaz, es decir, no se rindió: aunque se secaron dos plantas, siguió intentando. Al comienzo las lechugas eran escasas; ahora la cosecha es abundante. Gracias por escucharme».",
        "Al usar vocabulario nuevo no hay que forzarlo. No sirve llenar el discurso de palabras difíciles si no calzan. Si la audiencia puede no conocer una palabra, la explicamos con una frase corta. Después de ensayar en voz alta, revisamos con una pauta: ¿encaja la palabra?, ¿concuerda?, ¿se entiende?, ¿suena natural?",
    ],
    [("intervención oral", "participación breve hablada, como un comentario o exposición"), ("planificar", "pensar y ordenar lo que se dirá antes de hablar"), ("forzar", "usar algo donde no calza"), ("pauta", "lista de criterios para revisar"), ("natural", "que suena espontáneo y sin esfuerzo")],
    [
        ("Reconocer palabras nuevas", "Lee el modelo de intervención sobre el huerto. ¿Qué palabra describe a Sara?", ["Busco el adjetivo junto a su nombre.", "Dice que fue meticulosa.", "Eso es la palabra nueva."], "Meticulosa."),
        ("Revisar la explicación", "En «Iván fue tenaz, es decir, no se rindió», ¿para qué se agrega «es decir, no se rindió»?", ["La audiencia puede no conocer «tenaz».", "La frase explica el significado.", "Ayuda a que se entienda."], "Para explicar el significado de «tenaz»."),
    ],
    [("Llenar la intervención de palabras difíciles que no calzan.", "Se quiere impresionar.", "Usa pocas, pertinentes y explicadas."), ("No ensayar y trabarse al decir la palabra.", "Se cree que bastaba con escribirla.", "Ensaya en voz alta antes de hablar.")],
    [
        E("Según el modelo, ¿cuántas plantas se secaron?", "Dos", "Lo dice la frase sobre Iván."),
        E("¿Qué palabra del modelo se usa para decir que alguien no se rinde?", "Tenaz", "Está explicada con «es decir, no se rindió»."),
        E("¿Qué palabra se usa para la cosecha que ahora es mucha?", "Abundante", "Aparece en «ahora la cosecha es abundante»."),
    ],
    [
        E("¿Cuál de estas palabras NO aparece en el modelo del huerto: meticulosa, sigiloso o abundante?", "Sigiloso", "El modelo usa meticulosa, tenaz, escasas y abundante."),
        E("¿Por qué conviene explicar una palabra nueva a la audiencia: a) para que se entienda b) para alargar la intervención?", "a", "La audiencia puede no conocerla."),
        E("¿Qué hacemos primero al planificar: elegir tres palabras que encajen con el tema o improvisar?", "Elegir tres palabras que encajen con el tema", "Planificar evita forzar palabras."),
    ],
    [
        arith("Sara regó 5 surcos por día durante 4 días. ¿Cuántos surcos regó en total?", "5*4", "Se repite la misma cantidad cada día.", " surcos"),
        E("Ordena la intervención. a) Mi compañera fue meticulosa. b) Hoy les contaré cómo cuidamos el huerto. c) Gracias por escucharme. Escribe las letras.", "b, a, c", "Primero el tema, luego las ideas y al final el cierre."),
        E("¿Cuál frase usa bien «abundante»: a) «La cosecha de tomates fue abundante: llenamos tres cajas.» b) «La cosecha de tomates fue abundante: solo salió uno.»", "a", "Tres cajas muestran mucha cantidad."),
    ],
    [
        E("Un compañero usa diez palabras difíciles en un minuto sin explicar ninguna. ¿Qué conviene: a) usar pocas, pertinentes y explicadas b) repetir más palabras difíciles?", "a", "Así la audiencia comprende."),
        E("Una niña dice: «La cosecha fue escasa, es decir, muy grande». ¿Qué error comete?", "Define mal «escasa»", "Escasa significa poca, no grande."),
    ],
    [
        E("Para contar sobre un campeonato de salto a la cuerda: «La niña lo intentó ocho veces hasta lograrlo». ¿Qué palabra nueva calza mejor: tenaz o efímera?", "Tenaz", "No se rindió."),
        E("Para evaluar tu intervención, ¿qué pregunta es clave sobre una palabra nueva: a) ¿encaja con lo que quiero decir? b) ¿es la más larga?", "a", "La pertinencia es lo central."),
    ],
    [E("Tienes un minuto para hablar de un día de lluvia usando «efímero». ¿Qué oración es pertinente: a) «El arcoíris fue efímero: apareció solo un minuto.» b) «El arcoíris fue efímero: duró toda la tarde.»", "a", "Efímero es de corta duración.")],
    [
        E("¿Se deben forzar las palabras nuevas aunque no calcen? Responde sí o no.", "No", "Hay que usarlas solo donde encajan."),
        E("¿Ensayar en voz alta ayuda a decir bien una palabra nueva? Responde sí o no.", "Sí", "Así se pronuncia con naturalidad."),
        E("¿Una pauta de revisión pregunta si la palabra concuerda? Responde sí o no.", "Sí", "La concordancia es uno de los criterios."),
    ],
    ("Prepara una intervención de 4 a 5 oraciones sobre «Un día en que ayudé en casa o en la escuela». Usa tres de estas palabras: meticuloso, tenaz, sigiloso, escaso, abundante, efímero, cauteloso. Subraya las tres que elegiste y agrega una explicación breve para una. Ensaya en voz alta y usa la pauta: ¿encaja?, ¿concuerda?, ¿se entiende?, ¿suena natural?",
     "«Hoy les contaré cómo ayudé en el huerto. Fui meticuloso: revisé cada planta. Mi compañero Iván fue tenaz, es decir, no se rindió, y regó hasta terminar. La cosecha fue abundante. Gracias por escucharme».",
     ["usa tres palabras nuevas que encajan", "explica al menos una", "la intervención tiene saludo y cierre"], ["texto escrito con palabras subrayadas", "ensayo oral"], ["forzar palabras", "olvidar la concordancia"],
     "Si una palabra suena forzada, cámbiala por otra de la lista que calce mejor."),
    "Escribe una frase oral que use una de las palabras de esta clase sin explicarla y otra que sí la explique.",
    "Anota las palabras nuevas que escuches en una conversación o programa y prueba usar una en tu casa.",
)

# ================================================================ OA 30 · clase 1
reg(
    OA30, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar los textos orales de ejemplo.",
    "Aprenderé a reconocer distintos textos orales (poema, narración, descripción de una actividad, noticia, testimonio y dramatización), su propósito y el desafío de planificarlos. Sirve para elegir qué tipo de texto oral conviene según lo que quiero comunicar.",
    ["Sé que una exposición se organiza en partes.", "Sé usar la voz con claridad."],
    [
        "Un texto oral planificado es el que preparamos antes de decirlo, pensando en el propósito y en la audiencia. Hay varios tipos. El poema expresa emociones con ritmo, imágenes y a veces rima. La narración cuenta una historia con personajes, lugar y un problema que se resuelve. La descripción de una actividad explica los pasos en orden. La noticia informa un hecho real respondiendo qué, quién, cuándo, dónde y por qué. El testimonio relata en primera persona algo vivido. La dramatización representa una escena con voz y cuerpo.",
        "Ejemplos originales. Poema: «El río corre cantando, / baja de la montaña, / lleva en su espalda de agua / el sol de la mañana». Narración: «Julia perdió su paraguas amarillo en el bus. Lo buscó en la escuela y en la plaza. Al día siguiente, el conductor lo había guardado, y Julia sonrió». Descripción: «Para ver nacer un poroto: primero se humedece algodón; luego se coloca el poroto encima; después se deja en un lugar con luz; por último se riega con una cucharada de agua cada día». Noticia: «Ayer, en la escuela Las Acacias, los estudiantes de quinto plantaron veinte árboles en el patio para tener más sombra». Testimonio: «Yo vi cómo mi vecino ayudó a limpiar la calle después de la lluvia y me sentí orgullosa de mi barrio».",
        "El desafío es elegir el texto que cumple el propósito y prepararlo. Si quiero expresar un sentimiento con ritmo, elijo un poema; si quiero contar lo que me pasó, un testimonio o una narración; si necesito que sigan una secuencia de pasos, una descripción de actividad. Planificar ayuda a no olvidar partes y a decir el texto con seguridad.",
    ],
    [("texto oral", "mensaje que se dice con la voz"), ("poema", "texto que expresa emociones con ritmo e imágenes"), ("narración", "texto que cuenta una historia"), ("noticia", "texto que informa un hecho real"), ("testimonio", "relato en primera persona de algo vivido"), ("dramatización", "representación de una escena con voz y cuerpo")],
    [
        ("Reconocer el tipo de texto", "«El río corre cantando, / baja de la montaña, / lleva en su espalda de agua / el sol de la mañana». ¿Qué tipo de texto oral es?", ["Veo versos cortos.", "Hay rima en «montaña» y «mañana».", "Expresa una imagen con ritmo."], "Un poema."),
        ("Reconocer el propósito", "«Primero se humedece algodón; luego se coloca el poroto encima; después se deja en un lugar con luz». ¿Cuál es su propósito: explicar los pasos de una actividad o contar una noticia?", ["Observo las palabras primero, luego, después.", "Indican orden de pasos.", "Explica cómo hacer algo."], "Explicar los pasos de una actividad."),
    ],
    [("Elegir un texto sin pensar en el propósito.", "Se escoge el que parece más fácil.", "Pregúntate qué quieres comunicar y a quién."), ("Improvisar sin planificar.", "Se cree que basta con hablar.", "Escribe un esquema antes de decir el texto.")],
    [
        E("«Julia perdió su paraguas amarillo en el bus. Lo buscó en la escuela y en la plaza». ¿Qué tipo de texto oral es: narración o poema?", "Narración", "Cuenta una historia con personaje y problema."),
        E("¿Qué tipo de texto tiene versos con rima: poema o noticia?", "Poema", "Los versos y la rima son propios del poema."),
        E("«Yo vi cómo mi vecino ayudó a limpiar la calle y me sentí orgullosa». ¿Habla en primera o en tercera persona?", "En primera persona", "Usa la palabra «yo»."),
    ],
    [
        E("En la noticia «Ayer, en la escuela Las Acacias, plantaron veinte árboles», ¿qué pregunta responde la palabra «Ayer»: cuándo o dónde?", "Cuándo", "Indica el momento."),
        E("¿Cuál es el propósito de una noticia: a) informar un hecho real b) expresar emociones con rima?", "a", "Informa lo que ocurrió."),
        E("¿Qué texto oral corresponde si quieres contar lo que tú viviste, en primera persona: testimonio o descripción de actividad?", "Testimonio", "Relata algo vivido."),
    ],
    [
        arith("Se plantaron 20 árboles en 4 filas iguales. ¿Cuántos árboles hay en cada fila?", "20//4", "Se reparte el total entre las filas.", " árboles"),
        E("Ordena los pasos de la descripción del poroto. a) regar con una cucharada de agua b) humedecer el algodón c) colocar el poroto d) dejar en un lugar con luz. Escribe las letras.", "b, c, d, a", "Así lo indica el texto."),
        E("Quieres expresar cómo te sentiste en un día especial con ritmo e imágenes. ¿Qué texto eliges: poema o noticia?", "Poema", "Expresa emociones con ritmo."),
    ],
    [
        E("Un niño relata una noticia diciendo «Yo creo que los árboles son lindos». ¿Qué le falta a una noticia: a) datos como quién, cuándo y dónde b) rima?", "a", "Una noticia informa hechos."),
        E("¿Qué diferencia hay entre narración y descripción de actividad: a) la narración cuenta una historia y la descripción explica pasos b) son iguales?", "a", "Tienen propósitos distintos."),
    ],
    [
        E("Quieres presentar la historia de Julia en el acto del colegio con personajes que hablan, voz y movimientos. ¿Qué tipo de texto oral usas: dramatización o noticia?", "Dramatización", "Representa la escena."),
        E("Ordena los pasos para planificar un texto oral. a) ensayar b) elegir el tipo de texto y el propósito c) escribir un esquema. Escribe las letras.", "b, c, a", "Primero se decide, luego se planifica y después se ensaya."),
    ],
    [E("Tu curso te pide un texto oral para el acto: contar cómo se plantaron los árboles del patio. Quieres un relato en primera persona de lo que tú viviste. ¿Cuál eliges: noticia, poema o testimonio?", "Testimonio", "Relata lo vivido con «yo».")],
    [
        E("¿Un poema puede tener rima? Responde sí o no.", "Sí", "La rima es un recurso frecuente."),
        E("¿La descripción de una actividad explica pasos en orden? Responde sí o no.", "Sí", "Ese es su propósito."),
        E("¿Planificar significa pensar el texto antes de decirlo? Responde sí o no.", "Sí", "Ayuda a no olvidar partes."),
    ],
    ("Elige uno de estos propósitos y escribe qué tipo de texto oral usarías: A) expresar lo bonito que es el mar en la mañana; B) contar lo que te pasó cuando perdiste algo (sirve un testimonio o una narración); C) explicar cómo se prepara un sándwich seguro sin cuchillos filosos; D) informar que tu curso limpió el patio. Para el propósito elegido, escribe dos líneas de un esquema (tipo de texto, audiencia y una idea principal) y dilas en voz alta.",
     "Propósito B: testimonio (también serviría una narración). Esquema: tipo de texto: testimonio; audiencia: mi curso; idea principal: perdí mi cuaderno, lo busqué y lo encontré gracias a una compañera.",
     ["relaciona el propósito con el tipo de texto", "el esquema tiene tipo, audiencia e idea", "se dice en voz alta"], ["tipo de texto elegido", "esquema de dos líneas"], ["elegir un tipo que no calza con el propósito", "no mencionar la audiencia"],
     "Si dudas del tipo de texto, vuelve a las preguntas: ¿emoción, historia, pasos, hecho real o vivencia?"),
    "Escribe tres frases breves, cada una de un tipo de texto distinto, sobre el mismo tema (por ejemplo, la lluvia).",
    "Escucha una noticia o una receta y anota a qué tipo de texto oral pertenece y su propósito.",
)

# ================================================================ OA 30 · clase 2
reg(
    OA30, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu narración.",
    "Aprenderé a planificar una narración oral con personajes, lugar, inicio, problema y final, y a decirla ordenadamente con marcadores de tiempo. Sirve para contar historias que otros puedan seguir.",
    ["Sé reconocer distintos tipos de texto oral.", "Sé que una historia tiene personajes y un problema."],
    [
        "Una narración oral cuenta una historia con la voz. Para planificarla, armamos un esquema con cinco elementos: personajes (quiénes participan), lugar y tiempo (dónde y cuándo ocurre), inicio (cómo empieza todo), problema (lo que se complica) y final (cómo se resuelve). Con el esquema sabemos qué decir y en qué orden.",
        "Modelo de narración: «Una mañana de lluvia, Julia subió al bus con su paraguas amarillo. Al bajar, con las prisas, lo olvidó en el asiento. Lo buscó en la escuela y en la plaza, pero no lo encontró. Al día siguiente, el conductor le dijo: ‘Aquí está, lo guardé para ti’. Julia sonrió y le dio las gracias». Aquí los personajes son Julia y el conductor; el lugar, el bus; el problema, el paraguas olvidado; y el final, la devolución.",
        "Para que el relato se siga, usamos marcadores de tiempo: «una mañana», «al bajar», «al día siguiente», «finalmente». Ordenan los hechos de principio a fin. Además, contamos con voz expresiva: más lenta cuando algo se complica y más alegre al final. Ensayar con el esquema ayuda a no olvidar partes.",
    ],
    [("narración oral", "historia contada con la voz"), ("personaje", "quien participa en la historia"), ("problema", "lo que se complica en la historia"), ("desenlace", "final en que se resuelve el problema"), ("marcador de tiempo", "palabra que ordena los hechos, como «después»")],
    [
        ("Identificar elementos", "Narración «El paraguas amarillo». ¿Cuál es el problema?", ["Busco lo que se complica.", "Julia olvida el paraguas en el bus.", "Y no logra encontrarlo."], "Julia olvidó su paraguas en el asiento del bus y no lo encontró."),
        ("Ordenar con marcadores", "¿Qué marcador de tiempo indica el momento en que el conductor devuelve el paraguas?", ["Busco en el texto la palabra que indica tiempo.", "Antes de la devolución dice «Al día siguiente».", "Ese es el marcador."], "«Al día siguiente»."),
    ],
    [("Contar sin orden, saltando de un hecho a otro.", "Se cuenta a medida que se recuerda.", "Usa el esquema y marcadores de tiempo."), ("Olvidar el problema y pasar directo al final.", "Se piensa que solo importa cómo termina.", "Incluye qué se complicó y cómo se resolvió.")],
    [
        E("¿De qué color es el paraguas de Julia?", "Amarillo", "El texto lo dice al inicio."),
        E("¿Dónde olvidó Julia su paraguas?", "En el asiento del bus", "Lo dice la segunda oración."),
        E("¿Quién devuelve el paraguas?", "El conductor", "Es quien lo guardó."),
    ],
    [
        E("Además de Julia, ¿qué otro personaje participa en el relato?", "El conductor", "Es el otro personaje con diálogo."),
        E("¿Cuál es el desenlace: a) el conductor devuelve el paraguas y Julia agradece b) Julia pierde otro paraguas?", "a", "Resuelve el problema."),
        E("¿Qué elemento del esquema responde «cómo empieza todo»: el inicio o el problema?", "El inicio", "Presenta la situación de partida."),
    ],
    [
        E("Ordena los hechos. a) Julia busca el paraguas en la escuela. b) Julia sube al bus. c) El conductor devuelve el paraguas. d) Julia olvida el paraguas. Escribe las letras.", "b, d, a, c", "Es el orden de los sucesos del relato."),
        E("Completa el esquema: Inicio: Julia sube al bus. Problema: ______. Final: recupera el paraguas.", "Olvida el paraguas en el asiento", "Es lo que se complica."),
        E("¿Cuál es el mejor inicio oral: a) «Una mañana de lluvia, Julia subió al bus.» b) «Julia.»", "a", "Presenta personaje, tiempo y lugar."),
    ],
    [
        E("Si quitas la parte en que el conductor guarda el paraguas, ¿qué falla en la narración: el desenlace o el saludo?", "El desenlace", "No se explica cómo se resuelve."),
        E("¿Por qué conviene un esquema antes de contar: a) para recordar el orden y no olvidar partes b) para leer palabra por palabra?", "a", "El esquema guía la narración."),
    ],
    [
        E("Quieres cambiar el final: Julia no recupera el paraguas, pero compra uno nuevo con sus ahorros. ¿Qué parte del esquema cambia?", "El final", "Es el desenlace del problema."),
        E("Si Julia contara su propia historia, ¿cómo diría la primera oración: a) «Una mañana subí al bus con mi paraguas» b) «Una mañana subió al bus con su paraguas»?", "a", "Narra en primera persona."),
    ],
    [E("Vas a contar a tu curso algo que te pasó, en dos minutos. ¿Qué incluye tu esquema: a) personajes, lugar, inicio, problema y final b) solo el final?", "a", "Son los cinco elementos necesarios.")],
    [
        E("¿Una narración tiene un problema que se resuelve? Responde sí o no.", "Sí", "Ese es el núcleo de la historia."),
        E("¿«Al día siguiente» es un marcador de tiempo? Responde sí o no.", "Sí", "Ordena los hechos."),
        E("¿Conviene ensayar la narración con el esquema? Responde sí o no.", "Sí", "Ayuda a no olvidar partes."),
    ],
    ("Planifica y cuenta una narración corta sobre este inicio: «Matías encontró una llave pequeña junto a la reja de la escuela». Completa un esquema con personajes, lugar y tiempo, inicio, problema y final. Luego cuenta la historia en voz alta usando al menos tres marcadores de tiempo (por ejemplo, primero, luego, al día siguiente, finalmente) y velocidad más lenta en el momento del problema.",
     "Esquema: personajes: Matías y la conserje; lugar: escuela; problema: no sabe de quién es la llave; final: la entrega y la dueña agradece. Narración: «Primero, Matías encontró una llave. Luego, la llevó a la conserje. Finalmente, apareció la dueña y le dio las gracias».",
     ["completa los cinco elementos", "usa tres marcadores de tiempo", "tiene problema y final"], ["esquema escrito", "narración oral"], ["contar sin orden", "omitir el problema"],
     "Si el relato se enreda, vuelve al esquema y cuenta en orden."),
    "Escribe un esquema para la historia de un perro perdido en el parque.",
    "Cuéntale a alguien una historia corta de tu semana usando «primero», «luego» y «finalmente».",
)

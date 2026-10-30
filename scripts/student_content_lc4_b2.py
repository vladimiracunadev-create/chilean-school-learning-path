"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF03 (comprensión de textos escritos propios de la cultura, con opinión fundamentada) y OA LF04
(construcción de oraciones para transmitir mensajes, con palabras que indican acciones).

Criterio de autoría: todos los carteles, cartas, tarjetas y oraciones de práctica son inventados, están escritos en
castellano y se declaran como tales; no son textos de ningún pueblo. Las únicas palabras en lengua indígena son las
ya atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana, maururu en rapa
nui), siempre con su ficha y copiadas con su grafía exacta. No se escribe pronunciación, no se inventan oraciones
ni gramática en lengua indígena y no se afirma cómo se forman las oraciones en esa lengua: el cuaderno solo
practica leer con apoyo, copiar con exactitud y revisar. La forma tradicional de escribir y decir la enseñan el
educador/a tradicional y la comunidad; cada tarea abierta lo remite a ellos.
"""
from __future__ import annotations

from student_content_lc4_b import FICHA_PAL, L, M, T, W
from student_lessons import arith, ex

LF3, LF4 = "LC04 OA LF03", "LC04 OA LF04"

CARTEL = "Cartel de práctica (inventado). Título: «Cuidemos el ko». Lo escribió el comité de agua de una escuela de práctica. Dibujo: una llave y una planta. Texto: «Cerremos la llave después de usar el ko. Cada gota ayuda a las plantas del patio.»"
TARJETA = "Tarjeta de práctica (inventada). Dibujo: un sol sobre una casa. Texto: «El antü brilla sobre la ruka.»"
CARTA = "Carta de práctica (inventada): «Querida Rosa: hoy plantamos 6 semillas cerca de la ruka. Les echamos ko cada mañana. Cuando salga el antü, las moveremos a un lugar con luz. Chaltumay por las semillas. Ana.»"
CARTA_EMO = "Carta de práctica (inventada): «Hoy mi ñuke me dio una semilla pequeña. Me quedé en silencio y sentí calma. La guardé en la ruka. Chaltumay, ñuke. Tomás.»"

# =================================================================== OA LF03 · comprensión de textos escritos
L(
    LF3, 1,
    materials="Lápiz y hoja. Los textos están escritos en este cuaderno y son inventados. " + FICHA_PAL,
    use="Aprenderé a mirar el título, la fuente y los dibujos antes de leer y a anticipar de qué trata un texto. Sirve para leer con una idea previa y comprobarla después.",
    prior=["Sé que un texto puede venir de una persona o de una comunidad.", "Sé usar la ficha de palabras."],
    explain=[
        "Antes de leer, miro lo que rodea al texto. El título dice de qué se trata. La fuente dice quién lo escribió y dónde. El dibujo da pistas. El tipo de texto me dice para qué sirve: un cartel avisa algo a muchas personas, una carta se escribe para una persona y una tarjeta lleva una frase breve con un dibujo. Con esas pistas anticipo, es decir, hago una suposición sobre el tema.",
        "Una anticipación no siempre acierta. Por eso, después de leer, la comparo con el texto: si coincide, la confirmo, y si no, la corrijo. Anticipar no es adivinar sin base; es usar pistas.",
        "Los textos propios de una cultura, como los de un pueblo originario, tienen una fuente que debo reconocer: quién los escribió, en qué lugar y con qué permiso. Si un texto real está en lengua indígena, el educador tradicional me ayuda a leerlo. Hoy practico con un cartel inventado en castellano.",
    ],
    vocab=[("anticipar", "suponer de qué trata un texto usando pistas"), ("título", "nombre del texto"), ("fuente", "quién escribió el texto y de dónde viene"), ("pista", "dato que ayuda a descubrir algo"), ("propósito", "para qué se escribió un texto")],
    worked=[
        W("Anticipar con pistas", CARTEL + " Solo con el título y el dibujo, ¿de qué crees que trata?", ["El título dice «Cuidemos el ko».", "La ficha dice que ko es agua.", "El dibujo muestra una llave y una planta."], "Del cuidado del agua"),
        W("Confirmar después de leer", "Daniel anticipó que el cartel pedía cerrar la llave. Después de leer el texto, ¿acertó?", ["El texto dice «Cerremos la llave después de usar el ko».", "Su idea coincide con el texto."], "Sí, acertó"),
    ],
    mistakes=[
        M("Decidir de qué trata el texto sin mirar ninguna pista.", "No tengo base para anticipar.", "Miro título, fuente y dibujo."),
        M("Quedarme con mi anticipación aunque el texto diga otra cosa.", "El texto manda sobre mi suposición.", "Comparo y la corrijo si hace falta."),
    ],
    R=[
        ex("Antes de leer, ¿qué pista me dice de qué trata el texto: A) el título B) el número de la página?", "A", "El título nombra el tema."),
        ex("Según la ficha, «ko» es: A) agua B) casa.", "A", "La ficha dice que «ko» es agua."),
        ex("La fuente de un texto dice: A) quién lo escribió y de dónde viene B) cuántas palabras tiene.", "A", "Fuente es el origen del texto."),
    ],
    C=[
        ex(CARTEL + " ¿Quién escribió el cartel?", "el comité de agua de una escuela de práctica", "La fuente está escrita en la ficha del cartel."),
        ex("Verdadero o falso: si mi anticipación no coincide con el texto, debo cambiar el texto.", "Falso", "Corrijo mi anticipación, no el texto."),
        ex("Un texto es una carta. ¿Para qué sirve una carta: A) para decirle algo a una persona B) para anunciar algo a todo el patio?", "A", "Una carta se escribe para alguien en particular."),
    ],
    A=[
        ex("Ordena los pasos antes de leer: A) leo el texto B) miro título y dibujo C) anticipo el tema. Escribe las letras.", "B, C, A", "Miro, anticipo y luego leo."),
        ex(CARTEL + " ¿Qué pide el cartel que hagamos después de usar el agua?", "cerrar la llave", "El texto lo dice en la primera frase."),
        ex(CARTEL + " Según el título, ¿qué se debe cuidar: el ko o la llave?", "el ko", "El título dice «Cuidemos el ko»."),
    ],
    Z=[
        ex("Ana dice: «Por el dibujo de una llave y una planta, el texto trata de bailar». ¿Tiene una buena anticipación? Responde Sí o No.", "No", "Las pistas apuntan al agua y las plantas."),
        ex("Dos pistas: Título «Cuidemos el ko» y fuente «comité de agua». ¿Las dos pistas apuntan al mismo tema: sí o no?", "sí", "Ambas hablan del agua."),
    ],
    D=[
        arith("El cartel tiene 2 frases en su texto. Una escuela de práctica pone 4 carteles iguales. ¿Cuántas frases hay en total?", "2 * 4", "Multiplico las frases por los carteles."),
        ex("Un cartel real está escrito en lengua indígena y no sabes leerlo. ¿Qué haces: A) pedir ayuda al educador tradicional B) inventar lo que dice?", "A", "Inventar sería falso; pedir ayuda es respetuoso."),
    ],
    context=[ex("En la entrada de la biblioteca ves un papel con un dibujo de un libro y el título «Normas de la sala». ¿De qué anticipas que trata: «de cómo comportarse en la sala» o «de recetas de cocina»?", "«de cómo comportarse en la sala»", "El título y el dibujo apuntan a normas de la sala.")],
    selfcheck=[
        ex("¿Qué significa anticipar un texto?", "suponer de qué trata usando pistas", "Anticipar usa pistas antes de leer."),
        ex("¿Qué dato dice quién escribió un texto?", "la fuente", "La fuente nombra al autor o comité."),
        ex("Si el texto contradice mi anticipación, ¿qué corrijo?", "mi anticipación", "El texto es la evidencia."),
    ],
    task=T(
        "Mira este título y este dibujo inventados: título «El antü y la ruka», dibujo de un sol sobre una casa. Anota tu anticipación: de qué crees que trata y para qué se escribió. Luego lee esta frase del texto: «El antü brilla sobre la ruka». Escribe si tu anticipación coincidió y qué corregirías.",
        "Anticipo que trata de una casa con sol. Coincidió porque la frase habla del sol sobre la casa.",
        ["anticipa con título y dibujo", "lee la frase y compara", "corrige o confirma"],
        ["anticipación escrita y comparada en el cuaderno"],
        ["anticipar sin pistas", "no comparar con el texto"],
        "Valora que usó pistas y comparó; si no comparó, pídele que relea la frase.",
    ),
    reinforce="Mira el título y el dibujo de cualquier cuento de tu casa y di de qué crees que trata.",
    extend="Pide a una persona de tu casa que lea un título y dime tu anticipación antes de oír el resto.",
)

L(
    LF3, 2,
    materials="Lápiz y hoja. Las tarjetas están escritas en este cuaderno; un adulto puede leerlas en voz alta. " + FICHA_PAL,
    use="Aprenderé a leer con ayuda de la voz de otra persona, de dibujos y de la ficha de palabras. Sirve para entender un texto aunque no conozca todas sus palabras.",
    prior=["Sé anticipar con título, fuente y dibujo.", "Sé leer las palabras de la ficha con su significado."],
    explain=[
        "Leer también se hace con apoyos. Un apoyo oral es escuchar a otra persona leer el texto en voz alta. Un apoyo visual es usar el dibujo para entender qué pasa. Una ficha de palabras también ayuda a entender las palabras nuevas.",
        "Leo en tres pasos. Primero escucho la lectura en voz alta o leo en voz baja. Luego señalo con el dedo cada palabra para no perderme. Finalmente uso el dibujo y la ficha para confirmar el significado. Si aún no entiendo, pido ayuda.",
        "Si un texto está en una lengua indígena, no adivino cómo suena ni qué dice. Pido que el educador o la educadora tradicional lo lea en voz alta y me explique. Los apoyos no son trampa: son parte de leer bien.",
    ],
    vocab=[("apoyo oral", "ayuda de una voz que lee en voz alta"), ("apoyo visual", "ayuda de un dibujo o imagen"), ("señalar", "marcar con el dedo cada palabra al leer"), ("significado", "lo que quiere decir una palabra"), ("ficha", "lista de palabras con su significado")],
    worked=[
        W("Leer con dibujo y ficha", TARJETA + " ¿Qué significan las dos palabras de la ficha que aparecen en el texto?", ["Busco antü y ruka en el texto.", "La ficha dice antü es sol y ruka es casa."], "antü es sol y ruka es casa"),
        W("Usar el dibujo", "Una tarjeta inventada dice «El kuyen sale de noche». El dibujo muestra una luna. ¿Qué significa kuyen?", ["El dibujo muestra una luna.", "La ficha dice kuyen es luna."], "luna"),
    ],
    mistakes=[
        M("Decir «no entiendo nada» y dejar de leer.", "Hay apoyos que ayudan.", "Uso el dibujo, la ficha y pido lectura en voz alta."),
        M("Adivinar cómo suena una palabra en lengua indígena.", "Puedo equivocarme y cambiar su sentido.", "Pido que el educador tradicional la lea."),
    ],
    R=[
        ex("Un apoyo oral es: A) escuchar a otra persona leer B) mirar el reloj.", "A", "Apoyo oral es la voz de otra persona."),
        ex("Un apoyo visual es: A) un dibujo que ayuda a entender B) un silencio.", "A", "El dibujo ayuda a comprender el texto."),
        ex("Según la ficha, «antü» es: A) sol B) luna.", "A", "La ficha dice sol."),
    ],
    C=[
        ex(TARJETA + " ¿Qué muestra el dibujo?", "un sol sobre una casa", "Lo dice la descripción de la tarjeta."),
        ex("Verdadero o falso: usar el dibujo y la ficha es trampa al leer.", "Falso", "Son apoyos permitidos."),
        ex("Si veo un texto en lengua indígena que no sé leer, ¿pido ayuda al educador tradicional o lo adivino?", "pido ayuda al educador tradicional", "Adivinar puede cambiar el sentido."),
    ],
    A=[
        ex("Ordena los pasos de lectura con apoyos: A) confirmo con dibujo y ficha B) escucho la lectura en voz alta C) señalo con el dedo cada palabra. Escribe las letras.", "B, C, A", "Escucho, señalo y confirmo."),
        ex(TARJETA + " ¿Sobre qué brilla el sol?", "sobre la ruka", "El texto dice «sobre la ruka»."),
        ex("Cuenta las palabras de la frase «El antü brilla sobre la ruka»: El, antü, brilla, sobre, la, ruka. ¿Cuántas son?", "6", "Cuento cada palabra una vez: son seis."),
    ],
    Z=[
        ex("Dos niños leen «El kuyen sale de noche» con un dibujo de luna. Eva: «kuyen es luna». Gaspar: «kuyen es sol». ¿Quién tiene razón?", "Eva", "La ficha y el dibujo coinciden en luna."),
        ex("Una niña no entiende una palabra del texto. ¿Qué es mejor: A) mirar el dibujo y la ficha B) saltarse esa palabra y no preguntar?", "A", "Los apoyos ayudan a comprender."),
    ],
    D=[
        arith("Un texto tiene 12 palabras. Entendiste 9 sin ayuda. ¿Cuántas palabras necesitaste revisar con la ficha o el dibujo?", "12 - 9", "Resto las entendidas del total."),
        ex("Una persona dice cómo suena una palabra en lengua indígena sin haberla escuchado nunca. ¿Qué error comete: A) inventa una pronunciación B) usa la ficha?", "A", "No puede saber cómo suena sin escucharla."),
    ],
    context=[ex("Tienes una tarjeta con un dibujo de agua y la palabra «ko». ¿Qué haces para entender: «miro la ficha y el dibujo» o «me salto la palabra»?", "«miro la ficha y el dibujo»", "Los apoyos entregan el significado.")],
    selfcheck=[
        ex("¿Cómo se llama la ayuda de un dibujo al leer?", "apoyo visual", "Un dibujo es apoyo visual."),
        ex("¿Qué hago para no perderme en una línea al leer?", "señalo con el dedo cada palabra", "Señalar ayuda a seguir el texto."),
        ex("¿Quién me ayuda a leer un texto real en lengua indígena?", "el educador o la educadora tradicional", "Ellos conocen la lengua y el texto."),
    ],
    task=T(
        "Lee esta tarjeta inventada con ayuda de la ficha: dibujo de un vaso de agua y una planta; texto «El ko ayuda a la planta». Escribe qué significa la palabra «ko» y qué te muestra el dibujo. Luego escribe qué apoyo usaste para entenderla: oral, visual o ficha.",
        "ko significa agua. El dibujo muestra un vaso y una planta. Usé la ficha y el dibujo.",
        ["lee la tarjeta con apoyos", "explica el significado de ko", "nombra los apoyos usados"],
        ["respuesta escrita en el cuaderno"],
        ["no usar ningún apoyo", "inventar una pronunciación"],
        "Valora que use ficha y dibujo; si inventó una pronunciación, pídele que pregunte a quien enseña.",
    ),
    reinforce="Escucha una frase leída por alguien de tu casa y muestra con el dedo cada palabra.",
    extend="Dibuja una tarjeta con una palabra de la ficha y su dibujo, y muéstrala a una persona de tu casa.",
)

L(
    LF3, 3,
    materials="Lápiz y hoja. La carta está escrita en este cuaderno y es inventada. " + FICHA_PAL,
    use="Aprenderé a sacar datos de un texto y a relacionarlos con lo que ya sé. Sirve para entender mejor lo que dice un texto sin confundir lo que dice con lo que yo supongo.",
    prior=["Sé leer con apoyos.", "Sé que un texto tiene una fuente."],
    explain=[
        "La información explícita es lo que el texto dice con claridad: datos, números, lugares y acciones. La información implícita es lo que no se dice, pero se puede deducir con pistas. Primero busco los datos del texto y luego los relaciono con lo que ya sé.",
        "Mis saberes previos son lo que aprendí antes. Por ejemplo, sé que las plantas necesitan agua y luz. Si un texto habla de semillas con ko y antü, puedo relacionarlo: las semillas reciben agua y sol. Para no equivocarme, marco qué parte viene del texto y qué parte viene de lo que yo sé.",
        "Cuando un texto trata de la cultura de un pueblo, mis saberes previos pueden ser incompletos. No completo con inventos lo que no sé. Hago preguntas y consulto al educador tradicional.",
    ],
    vocab=[("explícito", "lo que el texto dice con claridad"), ("implícito", "lo que no se dice pero se puede deducir"), ("saber previo", "lo que ya aprendí antes"), ("deducir", "descubrir algo usando pistas"), ("relacionar", "unir una información con otra")],
    worked=[
        W("Dato explícito", CARTA + " ¿Cuántas semillas plantaron?", ["Busco el número en la carta.", "Dice «6 semillas»."], "6"),
        W("Relacionar con un saber previo", CARTA + " Sé que las plantas necesitan luz. ¿Qué parte del texto se relaciona con eso?", ["Busco la parte de luz.", "Dice «las moveremos a un lugar con luz»."], "«las moveremos a un lugar con luz»"),
    ],
    mistakes=[
        M("Mezclar lo que dice el texto con lo que yo supongo.", "Puedo contar algo que el texto no dice.", "Marco qué viene del texto y qué de mi saber previo."),
        M("Completar con inventos algo que no sé de una cultura.", "Puede ser falso.", "Pregunto al educador tradicional."),
    ],
    R=[
        ex(CARTA + " ¿Quién escribe la carta?", "Ana", "La carta termina con el nombre Ana."),
        ex(CARTA + " ¿A quién va dirigida?", "Rosa", "Empieza con «Querida Rosa»."),
        ex("Un dato explícito es: A) lo que el texto dice con claridad B) lo que imagino.", "A", "Explícito es lo dicho."),
    ],
    C=[
        ex(CARTA + " ¿Dónde plantaron las semillas?", "cerca de la ruka", "El texto dice «cerca de la ruka»."),
        ex("Verdadero o falso: mi saber previo puede reemplazar lo que dice el texto.", "Falso", "El saber previo complementa, no reemplaza."),
        ex(CARTA + " ¿Cuándo echan ko a las semillas?", "cada mañana", "El texto dice «cada mañana»."),
    ],
    A=[
        arith("Imagina que de las 6 semillas plantadas 2 no brotaron. ¿Cuántas semillas brotaron?", "6 - 2", "Resto las que no brotaron del total."),
        ex(CARTA + " ¿Qué dos cosas reciben las semillas según la carta?", "agua y luz", "La carta dice que les echan ko, que es agua, y que las llevarán a un lugar con luz."),
        ex(CARTA + " Marca como explícito (E) o implícito (I): «Rosa le dio las semillas a Ana». Responde E o I.", "I", "La carta no lo dice; solo se deduce de «Chaltumay por las semillas»."),
    ],
    Z=[
        ex("Pía dice: «Las semillas se plantaron en un invernadero». ¿Lo dice la carta? Responde Sí o No.", "No", "La carta dice cerca de la ruka."),
        ex("Eva usa su saber previo: «las plantas necesitan agua». Gaspar dice: «la carta dice que la ruka tiene agua». ¿Quién relacionó bien el texto con un saber previo?", "Eva", "Eva conecta el agua con el cuidado de las plantas."),
    ],
    D=[
        arith("Imagina que Ana plantó 6 semillas y Rosa plantó 4 en su casa. ¿Cuántas semillas plantaron entre las dos?", "6 + 4", "Sumo las semillas de ambas."),
        ex("Una niña explica cómo un pueblo siembra sin haberlo leído ni escuchado. ¿Qué debe hacer: A) indicar que no lo sabe y preguntar B) inventar un método?", "A", "No puede afirmar lo que no sabe."),
    ],
    context=[ex("Lees una carta de práctica que dice «Pusimos las semillas cerca de la ruka». ¿Qué dato es explícito: «cerca de la ruka» o «la casa es grande»?", "«cerca de la ruka»", "El segundo dato no está en el texto.")],
    selfcheck=[
        ex("¿Cómo se llama lo que el texto dice con claridad?", "explícito", "Explícito es lo dicho."),
        ex("¿Cómo se llama lo que ya aprendí antes y uso para entender?", "saber previo", "Es lo que ya sé."),
        ex("Si algo no está en el texto ni lo sé, ¿qué hago?", "pregunto", "No invento; consulto."),
    ],
    task=T(
        "Lee esta carta inventada: " + CARTA + " Escribe dos datos explícitos y un saber previo tuyo que se relacione con el texto. Marca cuál parte viene del texto y cuál de tu saber.",
        "Explícito 1: plantaron 6 semillas. Explícito 2: les echan ko cada mañana. Saber previo mío: las plantas necesitan agua. Viene de mi saber.",
        ["escribe dos datos explícitos", "escribe un saber previo", "marca qué viene del texto y qué de su saber"],
        ["datos y saber escritos en el cuaderno"],
        ["mezclar texto y saber", "inventar datos que no están"],
        "Valora que separó texto y saber; si mezcló, pídele que subraye lo que dice la carta.",
    ),
    reinforce="Lee la carta de nuevo y di qué dato te llamó más la atención.",
    extend="Cuenta a una persona de tu casa qué dice la carta y qué agregarías tú desde lo que ya sabes.",
)

L(
    LF3, 4,
    materials="Lápiz y hoja. La carta está escrita en este cuaderno y es inventada. " + FICHA_PAL,
    use="Aprenderé a reconocer la emoción de quien escribe y a decir qué no puedo saber a partir del texto. Sirve para responder con respeto, sin inventar lo que el texto no dice.",
    prior=["Sé separar lo que dice un texto de lo que supongo.", "Sé usar la ficha de palabras."],
    explain=[
        "Los textos también expresan emociones. Para descubrirlas busco pistas: palabras como silencio, calma o contento, o una despedida como «chaltumay», que agradece. Si encuentro la pista y la cito, puedo decir qué emoción siente quien escribe.",
        "Hay cosas que un texto no dice y que no puedo saber. Por ejemplo, no puedo saber qué pasó antes de la carta, ni cómo es la familia de quien escribe, ni qué significa algo para su comunidad. Responder con respeto es decir: «El texto no lo dice».",
        "Además, nadie está obligado a contar una vivencia personal para responder. Puedo opinar sobre el texto, imaginar a un personaje o decir que prefiero no contar. Una buena respuesta cita una pista del texto y reconoce el límite.",
    ],
    vocab=[("emoción", "lo que siente una persona: calma, alegría, tristeza"), ("pista", "palabra o frase que ayuda a descubrir algo"), ("límite", "lo que no puedo afirmar porque el texto no lo dice"), ("citar", "copiar la parte del texto que apoya mi idea"), ("vivencia", "experiencia que una persona vivió")],
    worked=[
        W("Descubrir la emoción", CARTA_EMO + " ¿Qué emoción siente Tomás?", ["Busco una palabra de emoción.", "El texto dice «sentí calma»."], "calma"),
        W("Reconocer un límite", CARTA_EMO + " ¿Podemos saber si Tomás tiene hermanos?", ["Busco el dato en el texto.", "No aparece."], "No, el texto no lo dice"),
    ],
    mistakes=[
        M("Decir cómo es la familia de quien escribe.", "El texto no lo dice.", "Respondo solo lo que dice el texto."),
        M("Obligar a alguien a contar su vivencia para responder.", "Puede ser privado.", "Ofrezco opciones: opinar, imaginar o pasar."),
    ],
    R=[
        ex(CARTA_EMO + " ¿Qué le dio su ñuke a Tomás?", "una semilla pequeña", "El texto dice «una semilla pequeña»."),
        ex("La palabra «calma» expresa: A) una emoción B) un lugar.", "A", "Calma es un sentimiento."),
        ex(CARTA_EMO + " ¿Dónde guardó la semilla?", "en la ruka", "El texto dice «la guardé en la ruka»."),
    ],
    C=[
        ex(CARTA_EMO + " ¿Qué palabra de la despedida agradece?", "Chaltumay", "La ficha dice que chaltumay es gracias."),
        ex("Verdadero o falso: a partir de la carta puedo saber qué pasó la semana anterior.", "Falso", "El texto no lo dice."),
        ex("Si no quiero contar una vivencia, ¿puedo opinar sobre el texto igual?", "Sí", "Puedo opinar sin contar cosas privadas."),
    ],
    A=[
        ex(CARTA_EMO + " ¿Qué límite del texto puedes decir: A) «El texto no dice qué pasó ayer» B) «Tomás vive en una casa grande»?", "A", "La carta no cuenta qué pasó antes ni cómo es la casa; decirlo sería inventar."),
        arith("Imagina que Tomás recibió 1 semilla y luego su amiga le dio 2 más. ¿Cuántas semillas tiene ahora?", "1 + 2", "Sumo las semillas recibidas."),
        ex("Pista: «Me quedé en silencio y sentí calma». ¿Qué emoción muestra: A) calma B) enojo?", "A", "La pista dice calma."),
    ],
    Z=[
        ex("Eva: «Tomás está triste porque no tiene hermanos». ¿La carta dice eso? Responde Sí o No.", "No", "El texto no habla de hermanos ni tristeza."),
        ex("Dos respuestas: Rita dice «Siente calma, porque lo dice el texto». Lola dice «Siente calma porque su familia es feliz». ¿Cuál respeta el límite del texto?", "la de Rita", "Rita usa una pista del texto."),
    ],
    D=[
        arith("Un curso lee 4 cartas y en 3 encuentra una pista de emoción. ¿En cuántas cartas no la encontró?", "4 - 3", "Resto las que tenían pista."),
        ex("Una persona dice: «Ese texto de un pueblo se debe leer de una forma sagrada». ¿Qué debe hacer: A) consultar al educador tradicional B) afirmarlo sin saber?", "A", "El significado sagrado lo explica la comunidad."),
    ],
    context=[ex("Después de leer una carta, una compañera te pregunta cómo es la casa de quien escribe. ¿Qué respondes: «El texto no lo dice» o «Es muy grande»?", "«El texto no lo dice»", "No puedo afirmar lo que el texto no dice.")],
    selfcheck=[
        ex("¿Qué hago para descubrir una emoción en un texto?", "busco una pista", "La pista muestra la emoción."),
        ex("¿Qué frase uso cuando el texto no da un dato?", "el texto no lo dice", "Reconozco el límite."),
        ex("¿Estoy obligado a contar una vivencia personal para responder?", "No", "Puedo opinar sin contar mi vida."),
    ],
    task=T(
        "Lee esta carta inventada: " + CARTA_EMO + " Escribe qué emoción siente Tomás y la pista que lo muestra. Luego escribe una pregunta que el texto no responde y que no puedes saber.",
        "Tomás siente calma. Pista: «sentí calma». Pregunta que no se responde: ¿cómo es la familia de Tomás?",
        ["dice una emoción", "cita una pista", "formula una pregunta que el texto no responde"],
        ["emoción, pista y pregunta escritas"],
        ["inventar datos", "obligar a contar la vida personal"],
        "Valora que citó la pista; si inventó datos, pídele que vuelva al texto.",
    ),
    reinforce="Elige una carta de esta clase y di qué emoción muestra y con qué pista.",
    extend="Pregunta a una persona de tu casa qué emoción nota en una frase corta que tú le leas.",
)

L(
    LF3, 5,
    materials="Lápiz y hoja. Los textos están escritos en este cuaderno y son inventados. " + FICHA_PAL,
    use="Aprenderé a comparar dos pistas del texto para decidir una respuesta. Sirve para dar respuestas con evidencia y no al azar.",
    prior=["Sé citar una pista del texto.", "Sé que el texto manda sobre mi suposición."],
    explain=[
        "A veces una sola pista no basta. Entonces busco dos pistas y las contrasto, es decir, las comparo para ver si dicen lo mismo, si se complementan o si se contradicen. Si dos pistas coinciden, mi respuesta es más segura.",
        "Si las pistas no coinciden, miro cuál está más cerca de la pregunta, cuál viene del texto y cuál de mi suposición. Una pista del texto pesa más que una suposición. Si aún no puedo decidir, lo digo y busco ayuda.",
        "Con textos de una cultura, las pistas deben venir del texto o de la fuente. No uso estereotipos ni supuestos sobre cómo es un pueblo. Si necesito saber algo de la cultura, pregunto al educador tradicional.",
    ],
    vocab=[("contrastar", "comparar para ver si dicen lo mismo o distinto"), ("coincidir", "decir lo mismo"), ("contradecir", "decir algo opuesto"), ("evidencia", "pista del texto que apoya una respuesta"), ("estereotipo", "idea fija y simplificada sobre un grupo")],
    worked=[
        W("Dos pistas que coinciden", "Texto inventado: «Sofía llegó a la ruka con ko en una vasija. Dejó la vasija junto a la puerta y se sentó a descansar». Pregunta: ¿qué es la ruka? Pista 1: «llegó a la ruka y dejó la vasija junto a la puerta». Pista 2: la ficha dice casa. ¿Coinciden?", ["La puerta indica un lugar cerrado.", "La ficha dice casa.", "Ambas pistas apuntan a una casa."], "Sí, ruka es una casa"),
        W("Pista del texto y suposición", "Un niño supone que Sofía estaba triste. El texto dice «se sentó a descansar». ¿Qué pista pesa más?", ["La pista del texto dice descansar.", "La tristeza es una suposición."], "La pista del texto"),
    ],
    mistakes=[
        M("Responder con una sola pista sin comprobar.", "Puede ser engañosa.", "Busco una segunda pista."),
        M("Usar una idea fija sobre un pueblo como si fuera una pista.", "Es un estereotipo, no evidencia.", "Uso solo lo que dice el texto."),
    ],
    R=[
        ex("Contrastar dos pistas es: A) compararlas B) borrarlas.", "A", "Contrastar es comparar."),
        ex("Dos pistas que dicen lo mismo, ¿coinciden o se contradicen?", "coinciden", "Dicen lo mismo."),
        ex("La evidencia viene: A) del texto B) de mi suposición.", "A", "La evidencia está en el texto."),
    ],
    C=[
        ex("Texto: «Sofía llegó a la ruka y dejó la vasija junto a la puerta». ¿Qué pista del texto muestra que la ruka es un lugar donde se entra?", "la puerta", "Una puerta indica un lugar al que se entra."),
        ex("Verdadero o falso: una suposición pesa más que una pista del texto.", "Falso", "El texto pesa más."),
        ex("La ficha dice «ruka» es casa. Texto: «Sofía llegó a la ruka». ¿Las dos pistas coinciden: sí o no?", "sí", "Ambas hablan de una casa."),
    ],
    A=[
        ex("Ordena cómo decido con dos pistas: A) decido mi respuesta B) comparo si coinciden C) busco dos pistas. Escribe las letras.", "C, B, A", "Busco, comparo y decido."),
        ex("Texto: «La vasija tenía ko. Sofía la dejó junto a la puerta». Pregunta: ¿qué había en la vasija? Pista 1: el texto dice ko. Pista 2: la ficha dice que ko es...", "agua", "La ficha dice que ko es agua."),
        arith("Imagina que Sofía llevó 3 vasijas y dejó 2 junto a la puerta. ¿Cuántas vasijas le quedan en la mano?", "3 - 2", "Resto las que dejó."),
    ],
    Z=[
        ex("Texto: «Sofía llegó a la ruka con ko en una vasija y se sentó a descansar». Pista 1: «Sofía se sentó a descansar». Pista 2: «Sofía estaba llorando». ¿Cuál de las dos pistas aparece en el texto?", "Pista 1", "Solo la 1 está en el texto."),
        ex("Una persona dice «las personas de ese pueblo siempre hacen lo mismo». ¿Es evidencia del texto o estereotipo?", "estereotipo", "No viene del texto y generaliza."),
    ],
    D=[
        arith("En una actividad hay 8 preguntas y 6 se responden con dos pistas. ¿Cuántas se responden con una sola pista?", "8 - 6", "Resto las de dos pistas."),
        ex("Dos pistas se contradicen: una del texto y otra que supongo. ¿Qué sigo: A) la del texto B) la que supongo?", "A", "El texto tiene más peso."),
    ],
    context=[ex("Lees «El ko cae de la vasija». Pista 1: una vasija puede contener líquidos. Pista 2: la ficha dice que «ko» es agua. ¿Coinciden: sí o no?", "sí", "Ambas pistas hablan de un líquido: el agua.")],
    selfcheck=[
        ex("¿Qué significa contrastar pistas?", "compararlas", "Contrastar es comparar pistas."),
        ex("¿Qué pesa más: la pista del texto o mi suposición?", "la pista del texto", "El texto es la evidencia."),
        ex("En Lengua y Cultura: ¿Qué es un estereotipo?", "una idea fija sobre un grupo", "Es una idea fija y simplificada."),
    ],
    task=T(
        "Lee: «Sofía llegó a la ruka con ko en una vasija. Dejó la vasija junto a la puerta y se sentó a descansar». Escribe una pregunta sobre el texto y responde con dos pistas: una del texto y otra de la ficha. Después escribe si tus dos pistas coinciden o no.",
        "Pregunta: ¿qué había en la vasija? Pista 1: el texto dice ko. Pista 2: la ficha dice que ko es agua. Coinciden.",
        ["escribe una pregunta", "usa dos pistas", "dice si coinciden"],
        ["pregunta y respuesta escritas"],
        ["usar una sola pista", "usar estereotipos"],
        "Valora que usó dos pistas; si usó estereotipos, pídele que vuelva al texto.",
    ),
    reinforce="Elige una respuesta de esta clase y busca una segunda pista que la apoye.",
    extend="Pregunta a una persona de tu casa cuántas pistas usa cuando duda de algo.",
)

# =================================================================== OA LF04 · construcción de oraciones
L(
    LF4, 1,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a observar cómo una oración nombra personas, cosas y lugares. Sirve para escribir con cuidado y para saber qué palabra nombra qué.",
    prior=["Sé copiar las palabras de la ficha con su grafía.", "Sé que una oración dice una idea completa."],
    explain=[
        "Una oración es un grupo de palabras que dice una idea completa. Empieza con mayúscula y termina con punto. En una oración, algunas palabras nombran: nombran personas, animales, cosas y lugares. Por ejemplo, en «El antü sale temprano», la palabra «antü» nombra al sol.",
        "Otras palabras indican acciones, es decir, lo que alguien o algo hace: sale, brilla, corre, cae. Las acciones dicen qué pasa. Para observar una oración busco primero qué palabra nombra y luego qué palabra dice la acción.",
        "Las palabras de la ficha las uso tal como están escritas. Cómo se forman oraciones completas en una lengua indígena lo enseña el educador tradicional; yo aquí practico con oraciones en castellano que traen una palabra de la ficha.",
    ],
    vocab=[("oración", "grupo de palabras que dice una idea completa"), ("nombrar", "decir cómo se llama una persona, cosa o lugar"), ("acción", "lo que alguien o algo hace"), ("mayúscula", "letra grande al inicio de la oración"), ("punto", "signo al final de una oración")],
    worked=[
        W("Encontrar quién nombra", "Oración: «El antü sale temprano.» ¿Qué palabra nombra y cuál indica la acción?", ["«antü» nombra al sol.", "«sale» dice lo que hace."], "Nombra: antü. Acción: sale"),
        W("Observar mayúscula y punto", "Oración: «La ruka es grande.» ¿Con qué letra empieza y con qué signo termina?", ["Empieza con L mayúscula.", "Termina con punto."], "Mayúscula L y punto"),
    ],
    mistakes=[
        M("Escribir la oración sin punto al final.", "No se sabe dónde termina la idea.", "Cierro con punto."),
        M("Cambiar una letra de «antü».", "Puede cambiar la palabra.", "Copio con exactitud de la ficha."),
    ],
    R=[
        ex("Una oración dice: A) una idea completa B) solo una letra.", "A", "Una oración dice una idea completa."),
        ex("En «La ruka es grande.», ¿qué palabra nombra una casa: ruka o grande?", "ruka", "Ruka nombra la casa."),
        ex("En «El antü sale temprano.», ¿qué palabra indica una acción: sale o antü?", "sale", "Sale dice lo que hace el sol."),
    ],
    C=[
        ex("¿Con qué signo termina una oración: punto o coma?", "punto", "La oración termina con punto."),
        ex("Verdadero o falso: puedo cambiar una letra de «ko» porque suena parecido.", "Falso", "Debo copiarla con su grafía."),
        ex("En «El ko cae.», ¿qué nombra «ko» según la ficha?", "agua", "La ficha dice que «ko» es agua."),
    ],
    A=[
        ex("Cuenta las palabras de «El antü sale por la mañana.»: El, antü, sale, por, la, mañana. ¿Cuántas palabras tiene?", "6", "Cuento cada palabra una vez: son seis."),
        ex("En «La ñuke llama a Tomás.», ¿cuál es la palabra de la ficha que nombra a la mamá?", "ñuke", "La ficha dice que «ñuke» es madre."),
        ex("Ordena para formar una oración: A) sale B) antü C) El. Escribe las letras.", "C, B, A", "«El antü sale.»"),
    ],
    Z=[
        ex("Dos oraciones: 1) «el antü sale temprano» 2) «El antü sale temprano.» ¿Cuál está escrita correctamente?", "2", "Tiene mayúscula y punto."),
        ex("Rita dice que «brilla» nombra al sol. Lola dice que «brilla» indica una acción. ¿Quién tiene razón?", "Lola", "«Brilla» dice lo que hace."),
    ],
    D=[
        arith("En una hoja hay 3 oraciones y cada una tiene 5 palabras. ¿Cuántas palabras hay en total?", "3 * 5", "Multiplico oraciones por palabras."),
        ex("Una persona escribe cómo se dice una oración completa en lengua indígena sin haberla aprendido. ¿Qué error comete: A) la inventa B) la copia de la ficha?", "A", "No puede saber cómo se forma una oración en esa lengua."),
    ],
    context=[ex("Quieres escribir una oración corta sobre el sol. ¿Escribes «El antü brilla.» o «el antü brilla»?", "«El antü brilla.»", "Lleva mayúscula inicial y punto final.")],
    selfcheck=[
        ex("¿Cómo se llama el grupo de palabras que dice una idea completa?", "oración", "Eso es una oración."),
        ex("¿Qué indica una palabra de acción?", "lo que alguien o algo hace", "Dice qué hace."),
        ex("¿Dónde copio la palabra «kuyen» para no cambiar sus letras?", "en la ficha", "La ficha trae la grafía exacta."),
    ],
    task=T(
        "Escribe tres oraciones cortas en castellano con una palabra de la ficha cada una. Por ejemplo: «El antü sale temprano.» Subraya la palabra que nombra y encierra la que indica acción. Copia las palabras de la ficha con exactitud.",
        "El antü sale temprano. El ko cae. El kuyen brilla.",
        ["escribe tres oraciones con mayúscula y punto", "usa una palabra de la ficha en cada una", "marca la palabra que nombra y la que indica acción"],
        ["tres oraciones escritas y marcadas"],
        ["olvidar el punto", "cambiar letras de la ficha"],
        "Valora que copió con exactitud; si olvidó punto o mayúscula, pídele que los revise.",
    ),
    reinforce="Lee en voz alta una de tus oraciones y señala con el dedo la palabra que nombra.",
    extend="Pide a una persona de tu casa que te dicte una oración corta y escribe con mayúscula y punto.",
)

L(
    LF4, 2,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a caracterizar, es decir, a decir cómo es algo con palabras como grande, pequeño o claro. Sirve para escribir oraciones más completas.",
    prior=["Sé que una oración tiene palabras que nombran y palabras de acción.", "Sé copiar las palabras de la ficha."],
    explain=[
        "Caracterizar es decir cómo es algo. Para caracterizar uso palabras que dicen cualidades: grande, pequeña, clara, tibia, fría. Por ejemplo, en «La ruka es grande.» la palabra «grande» dice cómo es la casa.",
        "Una buena caracterización responde a la pregunta «¿cómo es?». No es lo mismo nombrar que caracterizar. Nombrar dice qué es: ruka. Caracterizar dice cómo es: grande, clara, antigua. Con dos palabras puedo decir qué es y cómo es.",
        "Las palabras para caracterizar en una lengua indígena las enseña el educador tradicional, porque cada lengua tiene sus propias maneras. En este cuaderno caracterizo en castellano y dejo la palabra de la ficha en su lugar, tal como se escribe.",
    ],
    vocab=[("caracterizar", "decir cómo es algo"), ("cualidad", "cómo es algo: grande, clara, fría"), ("nombrar", "decir qué es algo"), ("pregunta guía", "«¿cómo es?» sirve para caracterizar"), ("describir", "decir cómo es algo con detalle")],
    worked=[
        W("Encontrar la cualidad", "Oración: «El ko está frío.» ¿Qué palabra dice cómo es el ko?", ["«ko» nombra el agua.", "«frío» dice cómo está."], "frío"),
        W("Nombrar o caracterizar", "En «La ruka es pequeña.», ¿«ruka» nombra o caracteriza? ¿Y «pequeña»?", ["«ruka» dice qué es.", "«pequeña» dice cómo es."], "ruka nombra; pequeña caracteriza"),
    ],
    mistakes=[
        M("Usar una cualidad que no corresponde, como «La ruka es líquida».", "Una casa no es líquida.", "Pienso si la cualidad tiene sentido."),
        M("Confundir nombrar con caracterizar.", "Nombrar dice qué es; caracterizar dice cómo es.", "Pregunto «¿qué es?» y «¿cómo es?»."),
    ],
    R=[
        ex("Caracterizar es decir: A) cómo es algo B) cuántas letras tiene.", "A", "Caracterizar responde a «¿cómo es?»."),
        ex("En «El antü está claro.», ¿qué palabra dice cómo está el sol: claro o antü?", "claro", "«Claro» es la cualidad."),
        ex("¿Qué pregunta ayuda a caracterizar: «¿cómo es?» o «¿cuándo me voy?»", "¿cómo es?", "Esa pregunta pide cualidades."),
    ],
    C=[
        ex("En «La ruka es grande.», ¿qué palabra nombra: ruka o grande?", "ruka", "Ruka dice qué es."),
        ex("Verdadero o falso: «frío» es una palabra para caracterizar.", "Verdadero", "Dice cómo está el agua u otra cosa."),
        ex("¿Cuál palabra sirve para caracterizar al ko: A) frío B) corre?", "A", "«Corre» indica acción; «frío» dice cómo es."),
    ],
    A=[
        ex("Completa: «El ko está ___.» Elige la palabra que dice cómo puede estar el agua: tibio o ladrillo.", "tibio", "Una cualidad del agua puede ser tibia; ladrillo no."),
        ex("Elige la cualidad que combina con «semilla»: pequeña o líquida.", "pequeña", "Una semilla puede ser pequeña, pero no líquida."),
        arith("Una niña describe 3 cosas con 2 cualidades cada una. ¿Cuántas cualidades dijo en total?", "3 * 2", "Multiplico las cosas por las cualidades."),
    ],
    Z=[
        ex("Dos oraciones: 1) «La ruka es grande.» 2) «La ruka es líquida.» ¿Cuál caracteriza con sentido?", "1", "Una casa puede ser grande, pero no líquida."),
        ex("Una persona dice que en lengua indígena «grande» se dice de una manera concreta y la inventa. ¿Qué debe hacer: A) preguntar al educador tradicional B) escribirlo igual?", "A", "No puede inventar palabras de una lengua."),
    ],
    D=[
        arith("Un texto tiene 9 palabras para caracterizar y 4 son cualidades del agua. ¿Cuántas son cualidades de otras cosas?", "9 - 4", "Resto las cualidades del agua del total."),
        ex("Escribe una oración con la palabra «mapu» y una cualidad. Elige entre «El mapu es húmedo.» y «El mapu es volando.» ¿Cuál tiene sentido?", "El mapu es húmedo.", "La tierra puede ser húmeda; no vuela."),
    ],
    context=[ex("Quieres decir cómo es el agua de un vaso que sacaste del refrigerador. ¿Escribes «El ko está frío.» o «El ko corre.»?", "«El ko está frío.»", "Frío es una cualidad del agua.")],
    selfcheck=[
        ex("¿Cómo se llama decir cómo es algo?", "caracterizar", "Eso es caracterizar."),
        ex("¿Qué pregunta ayuda a caracterizar?", "¿cómo es?", "Esa pregunta pide cualidades."),
        ex("¿Qué palabra dice qué es en «La ruka es grande.»?", "ruka", "Ruka dice qué es la cosa."),
    ],
    task=T(
        "Escribe tres oraciones que caractericen cosas del entorno, usando una palabra de la ficha en cada una y una cualidad. Por ejemplo: «El ko está frío.» Subraya la palabra de la ficha y encierra la cualidad. Revisa que la cualidad tenga sentido.",
        "El ko está frío. La ruka es grande. El antü está claro.",
        ["tres oraciones con una palabra de la ficha", "una cualidad en cada una", "la cualidad tiene sentido"],
        ["tres oraciones marcadas en el cuaderno"],
        ["usar cualidades sin sentido", "cambiar letras de las palabras de la ficha"],
        "Valora que la cualidad tenga sentido; si usó una sin sentido, pídele que la cambie.",
    ),
    reinforce="Mira un objeto de tu casa y di dos palabras que digan cómo es.",
    extend="Pide a una persona de tu casa que describa algo sin decir su nombre y adivínalo.",
)

L(
    LF4, 3,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a construir mis propias oraciones a partir de un modelo, con una palabra que nombra y una que indica acción. Sirve para transmitir mensajes sencillos sobre el medio natural y social.",
    prior=["Sé que una oración nombra y que tiene una acción.", "Sé caracterizar con una cualidad."],
    explain=[
        "Un modelo es una oración que me muestra cómo hacer otra. El modelo «El antü sale.» tiene tres partes: un artículo (El), un nombre (antü) y una acción (sale). Puedo construir otra oración cambiando una parte y manteniendo el orden: «El ko cae.»",
        "Para construir una oración sigo cuatro pasos. Primero elijo qué quiero decir. Luego elijo el nombre, por ejemplo una palabra de la ficha. Después elijo una acción que tenga sentido con ese nombre. Finalmente escribo con mayúscula y punto. El antü puede salir, brillar o calentar. El ko puede caer o correr. Una semilla puede crecer.",
        "Mi mensaje puede hablar del medio natural, como el sol y el agua, o del medio social, como la casa y la familia. Cómo se construye esa oración en una lengua indígena lo enseña el educador tradicional; aquí practico con oraciones en castellano.",
    ],
    vocab=[("modelo", "oración que me muestra cómo hacer otra"), ("artículo", "palabra corta como el, la, un, una"), ("verbo", "palabra que indica una acción"), ("mensaje", "idea que quiero comunicar"), ("medio natural", "lo que nos rodea: agua, sol, plantas")],
    worked=[
        W("Cambiar una parte del modelo", "Modelo: «El antü sale.» Cambia el nombre por «ko» y la acción por «cae». ¿Cómo queda?", ["Mantengo El al inicio.", "Pongo ko y cae."], "El ko cae."),
        W("Elegir una acción con sentido", "Quieres decir algo del kuyen. ¿Qué acción tiene sentido: brilla o ladra?", ["La luna brilla.", "La luna no ladra."], "brilla"),
    ],
    mistakes=[
        M("Elegir una acción que no combina, como «El ko ladra.»", "El agua no ladra.", "Pienso si la acción tiene sentido."),
        M("Escribir la oración con el orden cambiado: «Sale el antü El».", "Se pierde la idea.", "Sigo el orden del modelo."),
    ],
    R=[
        ex("Un modelo es: A) una oración que me muestra cómo hacer otra B) un dibujo.", "A", "El modelo guía mi oración."),
        ex("En «El antü sale.», ¿cuál es la acción: antü o sale?", "sale", "Sale dice lo que hace el sol."),
        ex("¿Qué acción combina con el agua: cae o ladra?", "cae", "El agua cae; no ladra."),
    ],
    C=[
        ex("Modelo: «El antü sale.» ¿Qué oración sigue el modelo: A) «El ko cae.» B) «Cae el ko El.»", "A", "Mantiene el orden artículo, nombre y acción."),
        ex("Verdadero o falso: una acción siempre combina con cualquier nombre.", "Falso", "Debe tener sentido con el nombre."),
        ex("¿Qué acción combina con una semilla: crece o brilla?", "crece", "Una semilla crece."),
    ],
    A=[
        ex("Ordena las palabras para formar una oración: A) cae B) El C) ko. Escribe las letras.", "B, C, A", "Forma «El ko cae.»"),
        ex("Cambia el nombre del modelo «El antü sale.» por «kuyen» y la acción por «brilla». ¿Cómo queda?", "El kuyen brilla.", "Mantengo el artículo, el nombre y la acción."),
        arith("Escribes 4 oraciones y cada una tiene 3 palabras. ¿Cuántas palabras escribiste?", "4 * 3", "Multiplico las oraciones por las palabras."),
    ],
    Z=[
        ex("Dos oraciones sobre el sol: 1) «El antü brilla.» 2) «El antü ladra.» ¿Cuál tiene sentido?", "1", "El sol brilla; no ladra."),
        ex("Una persona dice que escribió una oración en lengua indígena con esas mismas palabras. ¿Qué es lo correcto: A) preguntar al educador tradicional si la forma es correcta B) darla por buena?", "A", "No sabe cómo se forma una oración en esa lengua."),
    ],
    D=[
        arith("En una hoja hay 10 espacios para oraciones. Llenaste 7. ¿Cuántos espacios te faltan?", "10 - 7", "Resto los llenos del total."),
        ex("Quieres escribir un mensaje sobre la casa: «La ruka es grande.» ¿Es una oración que caracteriza o una que indica acción?", "caracteriza", "Dice cómo es la casa, no lo que hace."),
    ],
    context=[ex("Quieres avisar que sale el sol. ¿Qué escribes: «El antü sale.» o «Sale sale antü»?", "«El antü sale.»", "Sigue el modelo de una oración clara.")],
    selfcheck=[
        ex("¿Qué palabra indica una acción en «El ko cae.»?", "cae", "Cae es la acción."),
        ex("¿Qué cuatro pasos sigo para construir una oración? Nombra el último.", "escribo con mayúscula y punto", "Es el último paso."),
        ex("¿Quién enseña cómo se construyen oraciones en lengua indígena?", "el educador o la educadora tradicional", "Ellos conocen la lengua."),
    ],
    task=T(
        "Usa el modelo «El antü sale.» para construir tres oraciones nuevas. Cambia el nombre por una palabra de la ficha y la acción por una que tenga sentido, como brilla, cae, corre o camina. Revisa que cada oración tenga mayúscula y punto.",
        "El ko cae. El kuyen brilla. La ñuke camina.",
        ["tres oraciones nuevas", "acción con sentido", "mayúscula y punto"],
        ["tres oraciones escritas en el cuaderno"],
        ["acciones sin sentido", "olvidar el punto"],
        "Valora que siguió el modelo; si cambió el orden, pídele que lo compare con el modelo.",
    ),
    reinforce="Di en voz alta una oración que siga el modelo.",
    extend="Pide a una persona de tu casa que escriba una oración con el mismo modelo y revísenla juntos.",
)

L(
    LF4, 4,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a revisar mis oraciones: que digan lo que quiero, que las palabras de la ficha estén bien copiadas y que tengan sentido en la situación. Sirve para escribir con cuidado y respeto.",
    prior=["Sé construir oraciones con un modelo.", "Sé usar la ficha de palabras."],
    explain=[
        "Revisar es leer de nuevo mi texto para corregirlo. Uso una lista de tres preguntas: ¿tiene sentido lo que digo?, ¿escribí cada palabra de la ficha tal como está?, ¿se entiende en la situación en que la voy a usar? Si una respuesta es no, corrijo.",
        "La grafía es la manera de escribir una palabra. En este cuaderno cada palabra se copia como está en la ficha: si escribo «antu» en vez de «antü», no coincide con la ficha. Una lengua puede escribirse de más de una manera; cuál usa cada comunidad lo explica el educador tradicional. Para revisar comparo letra por letra con la ficha. Mi revisión se ve en el cuaderno con una marca de corrección.",
        "El contexto es la situación en que uso la oración. Una oración puede estar bien escrita y no ser adecuada para la situación. Si tengo duda sobre cómo se escribe o se usa una palabra de una lengua indígena, pregunto al educador tradicional.",
    ],
    vocab=[("revisar", "leer de nuevo para corregir"), ("grafía", "manera de escribir una palabra"), ("contexto", "situación en que uso la oración"), ("corrección", "cambio que hago para que quede bien"), ("comparar", "ver si dos cosas son iguales")],
    worked=[
        W("Revisar la grafía", "Una niña escribió «El antu sale.» ¿Qué corrige comparando con la ficha?", ["La ficha dice antü con ü.", "Escribió antu sin los dos puntos de la ü."], "Escribir «antü»"),
        W("Revisar el sentido", "Un niño escribió «La ruka corre.» ¿Tiene sentido la oración?", ["Una casa no corre.", "Debe cambiar la acción."], "No; cambiar «corre» por «es grande»"),
    ],
    mistakes=[
        M("Pensar que las letras parecidas dan lo mismo.", "Cada letra cambia la palabra.", "Comparo letra por letra."),
        M("No revisar y entregar igual.", "Puede quedar con errores.", "Uso mis tres preguntas."),
    ],
    R=[
        ex("Revisar es: A) leer de nuevo para corregir B) borrar todo.", "A", "Revisar es mirar para mejorar."),
        ex("La ficha dice «antü». ¿Cuál coincide con la ficha: antü o antu?", "antü", "Debe llevar ü para coincidir con la ficha."),
        ex("La ficha dice «ruka». ¿Cuál coincide con la ficha: ruka o ruca?", "ruka", "La ficha escribe ruka con k."),
    ],
    C=[
        ex("Verdadero o falso: revisar significa solo cambiar el color del lápiz.", "Falso", "Revisar es corregir errores."),
        ex("La ficha dice «ñuke». ¿Qué letra especial lleva al inicio: ñ o n?", "ñ", "La ficha escribe ñuke."),
        ex("El contexto de una oración es: A) la situación en que la uso B) la cantidad de palabras.", "A", "El contexto es la situación."),
    ],
    A=[
        ex("Corrige: «El kuyen sale.» La ficha dice kuyen. ¿Hay un error de grafía: sí o no?", "no", "Está escrita igual que en la ficha."),
        ex("Corrige: «El ko cae.» La ficha dice ko. ¿Está bien escrita la palabra: sí o no?", "sí", "Es igual a la ficha."),
        arith("Revisaste 7 oraciones y 5 estaban bien. ¿Cuántas debes corregir?", "7 - 5", "Resto las bien escritas del total."),
    ],
    Z=[
        ex("Dos niños copiaron «ñuke». Eva escribió «ñuke» y Gaspar escribió «nuke». ¿Quién la copió bien?", "Eva", "Eva mantuvo la ñ."),
        ex("Una oración dice «El ko ladra.» ¿Qué revisión falla: A) el sentido B) la grafía de ko?", "A", "El agua no ladra."),
    ],
    D=[
        arith("Tienes 12 oraciones y cada una requiere 3 revisiones: sentido, grafía y contexto. ¿Cuántas revisiones haces en total?", "12 * 3", "Multiplico oraciones por revisiones."),
        ex("Una persona dice que una palabra que escribió está bien porque suena igual. ¿Qué debe hacer: A) comparar con la ficha letra por letra B) fiarse del sonido?", "A", "Una letra distinta puede cambiar la palabra."),
    ],
    context=[ex("Escribiste «El antu brilla.» para una tarjeta del curso. ¿Qué haces antes de entregarla: «comparo con la ficha y corrijo» o «la entrego igual»?", "«comparo con la ficha y corrijo»", "Una letra mal copiada cambia la palabra.")],
    selfcheck=[
        ex("¿Cómo se llama la manera de escribir una palabra?", "grafía", "Eso es la grafía."),
        ex("¿Con qué comparo mis palabras para revisar la grafía?", "con la ficha", "La ficha trae la grafía exacta."),
        ex("¿Quién resuelve mis dudas sobre cómo se usa una palabra de la lengua?", "el educador o la educadora tradicional", "Ellos y la comunidad conocen la lengua."),
    ],
    task=T(
        "Revisa estas tres oraciones inventadas con la lista de tres preguntas: «El antu sale.» «La ruka corre.» «El ko cae.» Escribe cuáles tienen error, qué error es (no coincide con la ficha o no tiene sentido) y cómo las corregirías. Después escribe una pregunta para el educador tradicional sobre cómo se revisa un texto en lengua indígena.",
        "«El antu sale.»: no coincide con la ficha; debe ser antü. «La ruka corre.»: error de sentido; una casa no corre. «El ko cae.»: está bien. Pregunta: ¿cómo revisan sus textos?",
        ["identifica los errores", "distingue copia de la ficha y sentido", "formula una pregunta para quien enseña"],
        ["revisión escrita en el cuaderno"],
        ["no revisar letra por letra", "corregir sin comparar con la ficha"],
        "Valora que revisó con criterios; si corrigió sin comparar, pídele que vuelva a la ficha.",
    ),
    reinforce="Elige una de tus oraciones y revísala con las tres preguntas.",
    extend="Pide a una persona de tu casa que revise una oración tuya y anota si encontró algo distinto.",
)

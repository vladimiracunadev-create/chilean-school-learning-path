"""Cuaderno del estudiante, 3.º básico Lenguaje y Comunicación: OA 29 (vocabulario nuevo en lo oral), OA 30 (caracterización de personajes) y OA 31 (recitación de poemas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA29, OA30, OA31 = "LE03 OA 29", "LE03 OA 30", "LE03 OA 31"
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


# ================================================================ OA 29 · clase 1
reg(
    OA29, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: un diccionario escolar o una persona de tu casa para consultar.",
    "Aprenderé a descubrir el significado de una palabra nueva usando las pistas del texto. Sirve para entender lo que leo o escucho y para usar esa palabra después al hablar.",
    ["Sé leer un texto breve.", "Sé qué es una palabra desconocida."],
    [
        "Cuando leemos o escuchamos una palabra que no conocemos, no hace falta detenerse. Primero miramos el contexto, que son las palabras que están antes y después. Muchas veces el texto da una pista: un ejemplo, una explicación o una palabra parecida. Con esas pistas podemos pensar qué significa la palabra.",
        "Por ejemplo: «La comunidad hacía la cosecha: recogían las papas que habían sembrado». Después de los dos puntos aparece la explicación: recoger lo que se sembró. Entonces cosecha es recoger lo que se cultivó. Cuando no hay pistas suficientes, podemos preguntar a otra persona o buscar en un diccionario.",
        "Después de pensar el significado, lo comprobamos: lo probamos en la oración y vemos si tiene sentido. Si lo cambiamos por nuestra definición y la oración sigue teniendo sentido, vamos bien. Si no, buscamos otra pista. Así aprendemos vocabulario nuevo para usarlo luego en nuestras conversaciones.",
    ],
    [("contexto", "palabras que rodean a otra palabra y ayudan a entenderla"), ("pista", "señal del texto que ayuda a entender"), ("significado", "lo que quiere decir una palabra"), ("cosecha", "recoger lo que se ha sembrado y cultivado"), ("diccionario", "libro donde se explica el significado de las palabras")],
    [
        ("Usar el contexto", "Texto: «Cada otoño, la comunidad hacía la cosecha: recogían las papas que habían sembrado en primavera». ¿Qué significa cosecha?", ["Busco los dos puntos.", "Después aparece la explicación.", "Recogían lo que habían sembrado."], "Cosecha es recoger lo que se sembró."),
        ("Comprobar el significado", "Prueba en la oración: «La comunidad recoge lo que sembró y comparte una cena». ¿Tiene sentido?", ["Cambio la palabra por mi definición.", "Leo la oración.", "Veo que se entiende."], "Sí, tiene sentido: la definición encaja."),
    ],
    [("Saltarse la palabra que no conozco.", "Se pierde parte del significado del texto.", "Mira el contexto y busca una pista."), ("Inventar un significado sin mirar el texto.", "Puede ser incorrecto.", "Apóyate en lo que dicen las palabras de alrededor y comprueba.")],
    [
        E("Texto: «El arroyo era angosto: un niño podía saltarlo de un paso». ¿Dónde está la pista que explica «angosto»: antes o después de los dos puntos?", "Después", "La explicación está tras los dos puntos."),
        E("El contexto son las palabras que rodean a una palabra nueva. ¿Verdadero o falso?", "Verdadero", "Es la definición de contexto."),
        E("Si no hay pistas en el texto, ¿qué puedo hacer: buscar en el diccionario o adivinar sin mirar?", "Buscar en el diccionario", "Allí está el significado."),
    ],
    [
        E("¿Para qué sirve mirar las palabras de alrededor?", "Para encontrar pistas del significado", "El contexto ayuda a entender."),
        E("Texto: «La maestra era paciente: esperaba sin enojarse a que todos terminaran». ¿Qué pista da el significado de paciente?", "Esperaba sin enojarse", "Eso describe a una persona paciente."),
        E("Cambias la palabra por tu definición y la oración no tiene sentido. ¿Qué haces: buscar otra pista o seguir igual?", "Buscar otra pista", "Tu definición no encajó."),
    ],
    [
        E("Texto: «Estaba entusiasmado: tenía muchas ganas de empezar». ¿Qué significa entusiasmado: con muchas ganas o con sueño?", "Con muchas ganas", "La pista dice que tenía ganas."),
        E("Texto: «El río se volvió caudaloso: llevaba tanta agua que nadie podía cruzarlo». ¿Qué significa caudaloso: con poca agua o con mucha agua?", "Con mucha agua", "La pista dice que llevaba tanta agua."),
        E("Texto: «Estaba asombrado: nunca había visto un arcoíris tan grande». ¿Qué significa asombrado: muy sorprendido o enojado?", "Muy sorprendido", "Nunca había visto algo así."),
    ],
    [
        E("Ana dice que cosecha significa «sembrar». Lucas dice «recoger lo que se sembró». El texto dice: «recogían las papas que habían sembrado». ¿Quién tiene razón?", "Lucas", "La pista dice recoger, no sembrar."),
        E("«El camino era angosto, apenas cabía una persona». ¿Qué pista muestra que angosto es estrecho?", "Apenas cabía una persona", "Muestra que el espacio es pequeño."),
    ],
    [
        E("Texto: «Esperó con paciencia: no se enojó y volvió a intentarlo con calma». ¿Qué es paciencia: esperar con calma o rendirse enseguida?", "Esperar con calma", "No se enojó y volvió a intentarlo."),
        E("Ordena los pasos para entender una palabra: a) probar la definición en la oración b) leer el contexto c) pensar un significado. Escribe las letras.", "b, c, a", "Primero leo, luego pienso y después compruebo."),
    ],
    [E("En una charla escuchas: «Fue una cosecha abundante: llenamos diez cajones de papas». ¿Qué significa abundante: mucha cantidad o muy poca?", "Mucha cantidad", "Llenaron diez cajones.")],
    [
        E("¿El contexto ayuda a entender una palabra nueva?", "Sí", "Da pistas sobre su significado."),
        E("¿Debo comprobar el significado en la oración?", "Sí", "Así veo si tiene sentido."),
        E("¿Puedo usar el diccionario si no hay pistas?", "Sí", "Es una herramienta para encontrar significados."),
    ],
    ("Descubre palabras nuevas. Lee: «El camino era angosto: apenas cabía una persona. Al final había un río caudaloso: llevaba tanta agua que sonaba muy fuerte. Los niños estaban asombrados: nunca habían visto tanta agua». Escribe qué significan angosto, caudaloso y asombrado, y la pista del texto que usaste para cada una. Luego comprueba tu definición en la oración.",
     "Angosto: estrecho; pista: apenas cabía una persona. Caudaloso: con mucha agua; pista: llevaba tanta agua que sonaba fuerte. Asombrado: muy sorprendido; pista: nunca habían visto tanta agua.",
     ["explica cada palabra con sus palabras", "indica la pista del texto", "comprueba la definición en la oración"], ["hoja con tres palabras, definiciones y pistas"], ["definir sin usar el texto", "no comprobar"],
     "Si no hay pista, pregunta qué frase del texto lo dice."),
    "Pide a una persona de tu casa que lea una oración con una palabra difícil y descubran juntos su significado.",
    "Busca tres palabras nuevas en un cuento que te lean y explica sus pistas.",
)

# ================================================================ OA 29 · clase 2
reg(
    OA29, 2,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a explicar una palabra nueva con mis propias palabras, es decir, a hacer una paráfrasis. Sirve para comprobar que la entendí y para usarla bien al hablar.",
    ["Sé encontrar pistas en el texto.", "Sé explicar algo con mis palabras."],
    [
        "Parafrasear es decir lo mismo con otras palabras. Cuando aprendo una palabra nueva, la parafraseo para ver si la entendí. Por ejemplo, «paciente» puede explicarse como «que espera con calma y sin enojarse». No repito la palabra; la explico con ideas que conozco.",
        "Una buena paráfrasis es breve y precisa. Dice qué es o cómo es, y puede incluir un ejemplo. «Cosecha: recoger lo que se sembró; por ejemplo, sacar las papas del huerto». Si mi paráfrasis cambia el significado, no sirve. «Cosecha es plantar semillas» está mal, porque plantar es lo contrario de recoger.",
        "Para parafrasear usamos una estructura: «___ es / significa ___». También podemos usar un sinónimo, que es una palabra con significado parecido, como «estrecho» para «angosto». Después comprobamos con una oración: «El camino era angosto» y «El camino era estrecho» dicen casi lo mismo.",
    ],
    [("parafrasear", "decir lo mismo con otras palabras"), ("paráfrasis", "explicación que dice lo mismo con otras palabras"), ("sinónimo", "palabra con significado parecido a otra"), ("precisa", "que dice justo lo que debe decir"), ("paciente", "que espera con calma y sin enojarse")],
    [
        ("Parafrasear una palabra", "Texto: «La maestra era paciente: esperaba sin enojarse a que todos terminaran». Explica paciente con tus palabras.", ["Busco la pista del texto.", "Digo qué hace una persona paciente.", "Armo la frase."], "Paciente es quien espera con calma y sin enojarse."),
        ("Elegir un sinónimo", "¿Cuál palabra se parece a «angosto»? a) estrecho b) ancho", ["Pienso qué significa angosto.", "Estrecho significa poco ancho.", "Ancho significa lo contrario."], "a) estrecho."),
    ],
    [("Explicar una palabra repitiéndola: «Cosecha es hacer la cosecha».", "No explica nada.", "Usa otras palabras: «recoger lo que se sembró»."), ("Dar un significado contrario.", "Cambia el sentido.", "Comprueba con una oración y con el texto.")],
    [
        E("Parafrasear es decir lo mismo con otras palabras. ¿Verdadero o falso?", "Verdadero", "Es la definición de parafrasear."),
        E("¿Cuál es un sinónimo de «contento»: feliz o triste?", "Feliz", "Significan casi lo mismo."),
        E("Para explicar «cosecha», ¿repito la palabra o uso otras palabras?", "Uso otras palabras", "Parafrasear no repite la palabra."),
    ],
    [
        E("¿Por qué sirve parafrasear una palabra nueva?", "Para comprobar si la entendí", "Si puedo explicarla, la comprendo."),
        E("«Cosecha es plantar semillas». ¿Es buena paráfrasis?", "No", "Plantar es lo contrario de recoger."),
        E("¿Qué tiene una buena paráfrasis: es breve y precisa o es larga y confusa?", "Es breve y precisa", "Dice justo lo que debe decir."),
    ],
    [
        E("Parafrasea «asombrado» usando: «Asombrado es quien está muy…». ¿Qué palabra falta: sorprendido o dormido?", "Sorprendido", "Es la idea que da el texto."),
        E("Texto: «Estaba entusiasmado: tenía muchas ganas». Elige la paráfrasis: a) «Con muchas ganas de hacer algo.» b) «Con mucho sueño.»", "a", "Coincide con la pista."),
        E("Escribe una paráfrasis de «caudaloso» con este molde: «Un río caudaloso es un río con…». ¿Qué falta: mucha agua o poca agua?", "Mucha agua", "Es el significado."),
    ],
    [
        E("Teo explica: «Paciente es el que se enoja rápido». Ana explica: «Paciente es el que espera con calma». ¿Quién parafraseó bien?", "Ana", "Teo dijo lo contrario."),
        E("«Angosto» y «estrecho» ¿dicen casi lo mismo?", "Sí", "Los dos significan poco ancho."),
    ],
    [
        E("Parafrasea «cosecha» en una frase con ejemplo. Elige: a) «Es recoger lo que se sembró, por ejemplo, las papas del huerto.» b) «Es sembrar papas.»", "a", "Tiene definición y ejemplo correctos."),
        E("Elige el mejor sinónimo de «asombrado» para esta frase: «Los niños estaban asombrados». a) sorprendidos b) cansados", "a", "Coincide con el significado."),
    ],
    [E("Escuchas esta explicación: «Entusiasmado quiere decir con muchas ganas de hacer algo». Otro compañero dice: «Es lo mismo que estar sin ganas de hacer nada». ¿Es correcto?", "No", "Es lo contrario de tener muchas ganas.")],
    [
        E("¿Una paráfrasis puede usar sinónimos?", "Sí", "Los sinónimos ayudan a explicar."),
        E("¿Debo comprobar mi paráfrasis con el texto?", "Sí", "Así evito errores."),
        E("¿Puedo repetir la palabra para explicarla?", "No", "No explica su significado."),
    ],
    ("Parafrasea palabras nuevas. Lee: «Mateo estaba entusiasmado con el paseo. Su hermana, paciente, esperaba a que él guardara sus cosas. El sendero era angosto, y un río caudaloso sonaba cerca». Escribe una paráfrasis de entusiasmado, paciente, angosto y caudaloso. Usa «es / significa» y comprueba que tu frase se entiende al reemplazar la palabra.",
     "Entusiasmado: con muchas ganas. Paciente: que espera con calma. Angosto: estrecho. Caudaloso: con mucha agua.",
     ["explica cada palabra con otras palabras", "no repite la palabra", "comprueba en la oración"], ["hoja con cuatro paráfrasis"], ["repetir la palabra", "dar el significado contrario"],
     "Si usa la misma palabra, pide otra forma de decir lo mismo."),
    "Explica a una persona de tu casa una palabra nueva sin usar esa palabra.",
    "Escribe tres sinónimos para una palabra nueva y comprueba cuál encaja mejor.",
)

# ================================================================ OA 29 · clase 3
reg(
    OA29, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar.",
    "Aprenderé a usar palabras nuevas en una conversación de forma que tengan sentido. Sirve para expresarme con más precisión y para ampliar mi vocabulario.",
    ["Sé parafrasear una palabra.", "Sé conversar sobre un tema."],
    [
        "Aprender una palabra no basta con saber su significado: hay que usarla. Si la uso al hablar, la recuerdo mejor. Para usar bien una palabra nueva, pienso en una situación donde tenga sentido y armo una oración completa. Por ejemplo, con «angosto»: «El pasillo del colegio es angosto, y no caben cuatro personas juntas».",
        "Usar una palabra de forma pertinente quiere decir que encaja con el tema de la conversación y con lo que quiero decir. Si converso sobre un paseo, puedo usar «sendero», «angosto» o «caudaloso» si el paseo lo permite. No tiene sentido usar «caudaloso» para hablar de una gota de agua.",
        "En una conversación, la idea es incluir la palabra sin forzarla. Primero escucho el tema, luego pienso si hay una palabra nueva que sirva, y la uso con una oración clara. Si dudo, puedo decir también el significado: «El río estaba caudaloso, es decir, llevaba mucha agua».",
    ],
    [("pertinente", "que encaja con el tema y con lo que quiero decir"), ("oración", "conjunto de palabras que tiene sentido completo"), ("tema", "asunto del que se conversa"), ("sendero", "camino angosto por donde se camina"), ("forzar", "usar una palabra aunque no encaje")],
    [
        ("Armar una oración", "Quieres usar «caudaloso» en una conversación sobre un paseo al río. Arma una oración.", ["Pienso en el río.", "Uso la palabra para decir cómo estaba.", "Termino la oración con sentido."], "«El río estaba caudaloso por la lluvia.»"),
        ("Elegir dónde usar la palabra", "Palabra: «angosto». ¿Cuál oración encaja: a) «El puente era angosto y pasábamos de a uno.» b) «El día estaba angosto.»", ["Pienso qué puede ser angosto.", "Un puente puede serlo.", "Un día no."], "a)."),
    ],
    [("Usar una palabra nueva sin que encaje con el tema.", "Suena extraño y confunde.", "Úsala cuando describa de verdad lo que dices."), ("Repetir la palabra muchas veces para impresionar.", "Pierde naturalidad.", "Úsala una o dos veces donde corresponda.")],
    [
        E("¿Cuál oración usa bien «paciente»: «Mi abuelo es paciente y espera sin enojarse» o «La mesa está paciente»?", "Mi abuelo es paciente y espera sin enojarse", "Paciente se dice de una persona."),
        E("¿Cuál palabra encaja para describir un río con mucha agua: caudaloso o angosto?", "Caudaloso", "Habla de la cantidad de agua."),
        E("¿Usar una palabra nueva en una oración ayuda a recordarla?", "Sí", "Usarla la fija."),
    ],
    [
        E("¿Qué significa usar una palabra de forma pertinente?", "Que encaja con el tema y lo que quiero decir", "Tiene sentido en la situación."),
        E("¿Por qué no conviene usar «caudaloso» para hablar de una gota?", "Porque caudaloso se refiere a mucha agua", "No encaja con una gota."),
        E("Si dudo que me entiendan, ¿qué puedo hacer: decir la palabra y explicarla o no usarla nunca?", "Decir la palabra y explicarla", "Así me entienden mejor."),
    ],
    [
        E("Conversas sobre un paseo. ¿Cuál oración usa «sendero» correctamente: a) «Seguimos el sendero entre los árboles.» b) «Sendero tomó helado.»", "a", "Un sendero es un camino."),
        E("¿Cuál frase usa mejor «entusiasmado»: «Estaba muy entusiasmado con el viaje» o «La mesa estaba muy entusiasmada»?", "Estaba muy entusiasmado con el viaje", "Una persona puede estar entusiasmada; una mesa no."),
        E("Quieres decir que esperaste con calma. ¿Qué palabra nueva usas: paciente o asombrado?", "Paciente", "Significa esperar con calma."),
    ],
    [
        E("Luis conversa sobre un paseo y dice: «El camino era angosto, es decir, estrecho». Ema dice: «El día, el pan y la lluvia eran angostos». ¿Quién usó mejor la palabra?", "Luis", "La explicó y la usó con sentido."),
        E("Alguien dice: «Mi gato está caudaloso». ¿Usó bien la palabra?", "No", "Caudaloso se dice de ríos con mucha agua."),
    ],
    [
        E("Conversas con una persona de tu casa sobre la lluvia. ¿Qué oración integra «caudaloso»: a) «Con la lluvia, el río quedó caudaloso.» b) «Mi lápiz es caudaloso.»", "a", "Encaja con la lluvia y el río."),
        E("Para integrar una palabra en una conversación, ¿qué orden sigo: escuchar el tema, pensar si sirve la palabra, usarla en una oración?", "Escuchar, pensar y usar", "Así encaja bien."),
    ],
    [E("Conversan sobre un paseo. Una compañera dice: «Íbamos entusiasmados por el sendero angosto». ¿Cuántas palabras nuevas usó: entusiasmados, sendero y angosto?", "Tres", "Usó entusiasmados, sendero y angosto.")],
    [
        E("¿Debo usar la palabra con sentido?", "Sí", "Debe encajar con el tema."),
        E("¿Puedo explicar la palabra después de usarla?", "Sí", "Ayuda a que me entiendan."),
        E("¿Forzar palabras nuevas es buena idea?", "No", "Suena poco natural."),
    ],
    ("Usa palabras nuevas al conversar. Conversa con una persona de tu casa sobre el tema «un paseo imaginario por un sendero junto a un río». Usa en tu conversación al menos dos de estas palabras: angosto, caudaloso, entusiasmado, paciente, sendero, asombrado. Si no tienes con quién conversar, dilo en voz alta como si hablaras con alguien. Después escribe las dos oraciones que dijiste.",
     "El sendero era angosto y yo iba entusiasmado. El río estaba caudaloso por la lluvia.",
     ["usa al menos dos palabras nuevas", "las usa con sentido", "no las repite sin necesidad"], ["conversación oral y dos oraciones escritas"], ["usar una palabra que no encaja", "repetir la palabra sin sentido"],
     "Si una palabra no encaja, pide cambiar la oración o la palabra."),
    "Usa hoy una palabra nueva en una conversación en casa y cuéntala.",
    "Escribe un diálogo de cuatro intervenciones que use tres palabras nuevas.",
)

# ================================================================ OA 29 · clase 4
reg(
    OA29, 4,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a ajustar las palabras nuevas al registro de cada situación y a dejar claro a quién o a qué se refieren. Sirve para hablar con precisión con amigos, con personas adultas o en una exposición.",
    ["Sé usar palabras nuevas con sentido.", "Sé cambiar mi forma de hablar según con quién hablo."],
    [
        "El registro es la manera de hablar según la situación y la persona. Con amigos usamos palabras cotidianas. Con una profesora o ante el curso usamos un lenguaje más cuidado, también llamado formal. Ningún registro es malo: cada uno sirve en su situación. Una palabra nueva puede ayudar en ambos casos, pero la oración que la rodea cambia. Entre amigos: «Fue un paseo súper entretenido, nos fuimos por un sendero angosto». Ante el curso: «El paseo fue entretenido, y recorrimos un sendero angosto».",
        "También debemos dejar claro el referente, es decir, a quién o a qué se aplica la palabra. «Paciente» se dice de una persona; «angosto», de un camino, un puente o una calle; «caudaloso», de un río. Si digo «Eso fue angosto», no se sabe de qué hablo. Es mejor decir: «El puente fue angosto».",
        "Para ajustar el registro y el referente, me pregunto: ¿con quién hablo?, ¿de qué o de quién hablo?, ¿la palabra se aplica a eso? Si la respuesta es sí, la uso con una oración clara. Así mi vocabulario nuevo suena natural y comprensible.",
    ],
    [("registro", "forma de hablar según la situación y la persona"), ("referente", "persona o cosa a la que se aplica una palabra"), ("cotidiano", "de todos los días"), ("cuidado", "hablado con atención y respeto"), ("adecuado", "que encaja con la situación")],
    [
        ("Cambiar el registro", "Entre amigos dices: «Ese río estaba súper caudaloso». Ahora hablas ante tu profesora. ¿Cómo lo dices?", ["Mantengo la palabra nueva.", "Cambio «súper» por una forma más cuidada.", "Armo la oración."], "«El río estaba muy caudaloso.»"),
        ("Aclarar el referente", "Dices «Eso fue angosto». ¿Qué debes aclarar si hablas del puente?", ["Pienso a qué se refiere «eso».", "Digo la cosa.", "Armo la oración."], "«El puente fue angosto.»"),
    ],
    [("Usar el mismo registro con todas las personas.", "Una forma muy informal puede no ser adecuada ante personas adultas o en una exposición.", "Piensa con quién hablas y ajusta."), ("Usar una palabra con un referente que no corresponde.", "No tiene sentido.", "Revisa a qué se aplica la palabra.")],
    [
        E("«Paciente» se dice de una persona. ¿Verdadero o falso?", "Verdadero", "Describe cómo es una persona."),
        E("«Caudaloso» se dice de un río. ¿Verdadero o falso?", "Verdadero", "Describe un río con mucha agua."),
        E("Ante tu profesora, ¿qué registro conviene: cuidado o muy informal?", "Cuidado", "Es una situación formal."),
    ],
    [
        E("¿Qué es el referente de una palabra?", "La persona o cosa a la que se aplica", "Dice de qué o de quién hablo."),
        E("¿Por qué «Eso fue angosto» es poco claro?", "Porque no se sabe a qué se refiere «eso»", "Falta decir la cosa."),
        E("¿Un registro cuidado significa hablar con atención y respeto?", "Sí", "Es la forma adecuada en situaciones formales."),
    ],
    [
        E("Entre amigos: «El paseo estuvo súper bacán». Ante el curso, ¿qué es mejor: «El paseo fue muy agradable» o «Estuvo súper bacán»?", "El paseo fue muy agradable", "Es un registro más cuidado."),
        E("Quieres decir que la calle apenas deja pasar a una persona. ¿Qué palabra usas: angosta o paciente?", "Angosta", "Se aplica a una calle."),
        E("Quieres decir que tu vecina esperó con calma. ¿Qué palabra usas: paciente o caudalosa?", "Paciente", "Se aplica a una persona."),
    ],
    [
        E("Beto dice ante el curso: «El río quedó súper caudaloso, tipo wow». Ana dice: «El río quedó caudaloso y no se podía cruzar». ¿Quién ajustó mejor el registro?", "Ana", "Su oración es más cuidada y clara."),
        E("Un niño dice: «Mi cuaderno es caudaloso». ¿Aplicó bien la palabra?", "No", "Caudaloso se aplica a ríos con mucha agua, no a un cuaderno."),
    ],
    [
        E("Explicas el paseo a tu curso. ¿Cuál es la mejor oración: a) «Caminamos por un sendero angosto junto al río caudaloso.» b) «Eso era angosto y eso caudaloso.»", "a", "Nombra el sendero y el río."),
        E("Con un amigo puedes decir «Estaba súper cansado». Ante una exposición, ¿qué cambiarías: «Estaba muy cansado» o dejarlo igual?", "Estaba muy cansado", "Es más cuidado para esa situación."),
    ],
    [E("En una charla ante el curso quieres decir: «Eso fue paciente». ¿Qué corrección aclara el referente: «Mi hermana fue paciente» o «Eso fue paciente»?", "Mi hermana fue paciente", "Nombra a la persona que lo fue.")],
    [
        E("¿Debo ajustar mi registro según con quién hablo?", "Sí", "Cambia la forma de decir las cosas."),
        E("¿Una palabra nueva se puede aplicar a cualquier cosa?", "No", "Tiene referentes que corresponden."),
        E("¿Conviene nombrar a qué se refiere una palabra si hay dudas?", "Sí", "Así se evita la confusión."),
    ],
    ("Ajusta tu registro. Escribe dos veces el mismo mensaje: primero para un amigo y luego para tu curso. El mensaje: contar un paseo por un sendero angosto, con un río caudaloso. Usa al menos dos palabras nuevas. Después escribe a qué se refiere cada palabra (referente).",
     "Amigo: El sendero estaba súper angosto y el río estaba caudaloso, ¡fue entretenido! Curso: Recorrimos un sendero angosto y vimos un río caudaloso; fue un paseo entretenido. Referentes: angosto, el sendero; caudaloso, el río.",
     ["escribe dos versiones con registros distintos", "usa dos palabras nuevas", "indica el referente de cada una"], ["hoja con dos versiones"], ["mismo registro en las dos", "palabra con referente equivocado"],
     "Si las versiones son iguales, pregunta cómo cambiarías una al hablar con el curso."),
    "Cuenta un mismo suceso a un amigo y luego a un adulto, y nota qué palabras cambian.",
    "Escribe tres frases con un referente claro para tres palabras nuevas.",
)

# ================================================================ OA 29 · clase 5
reg(
    OA29, 5,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a darme cuenta de cuándo una palabra no encaja y a corregirme con calma. Sirve para hablar con más precisión sin sentir vergüenza por equivocarme.",
    ["Sé usar palabras nuevas con sentido.", "Sé ajustar el registro."],
    [
        "Equivocarse al usar una palabra nueva es normal. Lo importante es notarlo y corregirlo. Autocorregirse es detectar yo mismo un error y arreglarlo. Cuando uso una palabra y veo que no encaja, puedo decir: «Perdón, quise decir…» o «Mejor dicho…» y decir la palabra correcta.",
        "Para notar un error, pienso: ¿la palabra significa lo que quiero decir?, ¿se aplica a esta cosa o persona?, ¿encaja con el tema? Si digo «El río está muy paciente», noto que «paciente» no se aplica a un río, y me corrijo: «Perdón, quise decir caudaloso».",
        "También puedo recibir una ayuda amable de otra persona: «¿Quisiste decir caudaloso?». La acepto con calma y repito la frase corregida. Corregirse no es fracasar: es aprender. Cada vez que me autocorrijo, mi vocabulario queda más seguro y preciso.",
    ],
    [("autocorrección", "corregir yo mismo un error que noté"), ("equivocarse", "decir o hacer algo que no es correcto"), ("quise decir", "frase que se usa para corregirse"), ("precisión", "decir justo lo que se quiere decir"), ("aprender", "ir sabiendo algo que antes no sabía")],
    [
        ("Corregir una frase", "Dijiste: «El río está muy paciente». Quieres decir que lleva mucha agua. Autocorrígete.", ["Noto que paciente no se aplica a un río.", "Pienso en la palabra correcta: caudaloso.", "Digo «quise decir»."], "«Perdón, quise decir que el río está muy caudaloso.»"),
        ("Aceptar ayuda", "Un compañero te dice: «¿Quisiste decir angosto?». Era lo que querías decir. ¿Qué respondes?", ["Escucho su ayuda.", "Verifico que sí.", "Repito la frase correcta."], "«Sí, quise decir angosto. Gracias.»"),
    ],
    [("Quedarme callado porque tengo miedo de equivocarme.", "No aprendo si no uso las palabras.", "Usa la palabra y corrígete si hace falta."), ("Reírme cuando alguien se equivoca.", "Hace sentir mal y desanima a hablar.", "Ofrece ayuda amable: «¿Quisiste decir…?».")],
    [
        E("¿Qué hago al notar que una palabra no encaja: me corrijo o sigo igual?", "Me corrijo", "Eso es autocorregirse."),
        E("¿Cuál es una frase para corregirme: «Quise decir…» o «Qué tonto»?", "Quise decir…", "Corrige sin insultarme."),
        E("Equivocarse al hablar, ¿es normal?", "Sí", "Todos nos equivocamos al aprender."),
    ],
    [
        E("¿Qué significa autocorregirse?", "Corregir yo mismo un error que noté", "Yo detecto y arreglo."),
        E("¿Por qué es importante que me ayuden con amabilidad?", "Porque así sigo hablando con confianza", "La ayuda amable motiva."),
        E("Dijiste «El camino está paciente». ¿Qué pregunta te ayuda a notar el error: «¿se aplica paciente a un camino?» o «¿cuántos caminos hay?»", "¿Se aplica paciente a un camino?", "Revisa si la palabra encaja con lo que describe."),
    ],
    [
        E("Dijiste «El puente está caudaloso». Quieres decir que es estrecho. Elige la corrección: a) «Perdón, quise decir angosto.» b) «Ya, da lo mismo.»", "a", "Corrige con la palabra correcta."),
        E("Un amigo dice «el río es paciente» y quería decir que lleva mucha agua. Para ayudarlo con amabilidad dices: a) «¿Quisiste decir caudaloso?» b) «Qué risa, te equivocaste.»", "a", "Ofrece ayuda sin burlarse."),
        E("Notas que usaste «entusiasmado» para decir «cansado». ¿Qué dices: «Perdón, quise decir cansado» o nada?", "Perdón, quise decir cansado", "Así corriges y dices lo que querías."),
    ],
    [
        E("Ana se equivocó con «caudaloso» y se corrigió. Luis se rió. ¿Quién actuó bien con el error?", "Ana", "Se corrigió; Luis se burló."),
        E("Después de corregirte, ¿debes repetir la frase correcta?", "Sí", "Así queda clara la idea."),
    ],
    [
        E("Dices: «Fue un paseo angosto». Tu intención era decir que fue breve. Elige la corrección más adecuada: a) «Mejor dicho, un paseo corto.» b) «Es lo mismo.»", "a", "Cambia por la palabra que expresa lo que quería decir."),
        E("Ordena para autocorregirte: a) decir la palabra correcta b) notar el error c) decir «perdón, quise decir». Escribe las letras.", "b, c, a", "Primero noto, luego aviso y luego corrijo."),
    ],
    [E("Estás en una charla y dices «El sendero estaba asombrado». Un compañero ayuda con voz amable: «¿Quisiste decir angosto?». Respondes: «Sí, gracias». ¿Corregiste el error?", "Sí", "Aceptaste la ayuda y la usaste.")],
    [
        E("¿Autocorregirse es aprender?", "Sí", "Cada corrección mejora mi vocabulario."),
        E("¿Debo burlarme de quien se equivoca?", "No", "Hay que ayudar con respeto."),
        E("¿«Quise decir» sirve para corregirme?", "Sí", "Anuncia la palabra correcta."),
    ],
    ("Autocorrígete. Lee estas frases con errores y corrígelas con «Quise decir…»: 1) «El río estaba muy paciente» (quiso decir caudaloso). 2) «El puente era entusiasmado» (quiso decir angosto). 3) «Mi vecino esperó muy asombrado» (quiso decir paciente). Luego escribe cómo ayudarías con amabilidad a un compañero que se equivocó con una palabra.",
     "1) Perdón, quise decir caudaloso. 2) Quise decir angosto. 3) Quise decir paciente. Ayuda: ¿Quisiste decir angosto?",
     ["usa «Quise decir» o una frase equivalente", "corrige las tres frases", "propone una ayuda amable"], ["hoja con tres correcciones y una frase de ayuda"], ["burlarse del error", "no cambiar la palabra"],
     "Si se burla, pregunta cómo se sentiría el compañero."),
    "Anota una palabra que usaste mal esta semana y cómo la corregirías.",
    "Escribe un diálogo de dos intervenciones en que alguien se autocorrige.",
)

# ================================================================ OA 30 · clase 1
reg(
    OA30, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los diálogos.",
    "Aprenderé a descubrir la intención de un personaje por lo que dice y hace. Sirve para caracterizarlo mejor y para entender a las personas en la vida diaria.",
    ["Sé leer un diálogo.", "Sé observar voz, gesto y espacio."],
    [
        "Caracterizar a un personaje es mostrar cómo es, qué quiere y cómo actúa. Para hacerlo bien, primero descubrimos su intención, que es lo que quiere lograr. La intención no siempre se dice con palabras: la inferimos, es decir, la deducimos usando pistas del texto.",
        "Las pistas pueden ser lo que dice, lo que hace y cómo lo hace. Por ejemplo: «Pía guardó su merienda en la mochila y miró al suelo cuando Teo se acercó». Podemos inferir que Pía no quiere compartir, o que está nerviosa. Para decidir, buscamos más pistas. Una intención es más clara cuando varias pistas apuntan a lo mismo.",
        "Además del querer, el personaje tiene rasgos, que son características de su forma de ser: curioso, tímido, amable, valiente. Los rasgos no se dicen siempre: se muestran con las acciones. Un personaje que ayuda sin que se lo pidan muestra el rasgo «amable». Trabajar en equipo ayuda: cada integrante propone una pista y el equipo elige.",
    ],
    [("intención", "lo que un personaje quiere lograr"), ("inferir", "deducir algo usando pistas"), ("rasgo", "característica de la forma de ser de un personaje"), ("pista", "señal del texto que ayuda a entender"), ("cooperación", "trabajar juntos para lograr algo")],
    [
        ("Inferir la intención", "Texto: «Leo ve que Mia no alcanza el libro del estante alto. Se para a su lado y le acerca el banquito». ¿Qué quiere Leo?", ["Veo lo que hace.", "Le acerca el banquito.", "Quiere ayudarla."], "Quiere ayudar a Mia a alcanzar el libro."),
        ("Descubrir un rasgo", "Texto: «Ema siempre pregunta cómo funcionan las cosas y mira de cerca cada juguete para entender cómo se mueve». ¿Qué rasgo muestra?", ["Pienso en lo que hace.", "Pregunta cómo funcionan las cosas.", "Le interesa saber."], "Es curiosa."),
    ],
    [("Decir la intención sin ninguna pista.", "Puede no ser cierto.", "Apóyate en lo que dice y hace el personaje."), ("Quedarse solo con un rasgo y olvidar lo que quiere el personaje.", "El personaje queda incompleto.", "Busca qué quiere y cómo es.")],
    [
        E("La intención es lo que el personaje quiere lograr. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        E("Un rasgo es una característica de la forma de ser. ¿Verdadero o falso?", "Verdadero", "Por ejemplo, tímido o curioso."),
        E("Leo acerca el banquito a Mia. ¿Qué quiere: ayudarla o molestarla?", "Ayudarla", "Su acción la ayuda."),
    ],
    [
        E("¿Por qué inferimos la intención y no solo la leemos?", "Porque no siempre está dicha con palabras", "Se deduce con pistas."),
        E("Ema mira de cerca cada juguete para entender cómo se mueve. ¿Eso muestra curiosidad o miedo?", "Curiosidad", "Quiere saber cómo funciona."),
        E("¿Por qué conviene buscar varias pistas?", "Para estar más seguro de la intención", "Una sola pista puede tener varios significados."),
    ],
    [
        E("Texto: «Teo guarda su balón y dice: Hoy no juego». ¿Qué pista da el texto?", "Guarda su balón y dice que no juega", "Muestra lo que hace y dice."),
        E("Texto: «Nina dibuja un cartel para que nadie bote papeles en el patio». ¿Qué quiere Nina?", "Cuidar el patio", "Su cartel busca que no se bote basura."),
        E("Texto: «Hugo habla bajito y mira al suelo cuando le preguntan algo». ¿Qué rasgo puede mostrar: timidez o rabia?", "Timidez", "Habla bajito y evita la mirada."),
    ],
    [
        E("Ana dice: «Pía quiere ayudar, porque le acerca un lápiz a Eli que lo había perdido». Bea dice: «Pía es mala». ¿Quién se apoya en la pista del texto?", "Ana", "Usa lo que hace Pía."),
        E("Un personaje dice «Estoy tranquilo», pero se muerde las uñas y no deja de mirar la puerta. ¿Hay una pista que contradice lo que dice?", "Sí", "Morderse las uñas y mirar la puerta no coincide con estar tranquilo."),
    ],
    [
        E("Texto: «Sofía dice: No importa, yo espero. Y se sienta con calma mientras los demás terminan». ¿Qué rasgo puede mostrar: paciencia o prisa?", "Paciencia", "Espera con calma."),
        E("En un equipo, Ema dice que Camilo quiere ayudar porque se sentó al lado de Vale. Teo dice que quiere ayudar porque le ofreció un ejemplo. ¿Las dos pistas apuntan a lo mismo?", "Sí", "Las dos muestran que Camilo quiere ayudar."),
    ],
    [E("Texto: «Pedro entra corriendo, deja una carta en la mesa y dice: ¡Por favor, léanla hoy!». ¿Qué quiere Pedro: que lean la carta ese mismo día o que la guarden?", "Que la lean ese mismo día", "Lo dice con su pedido.")],
    [
        E("¿La intención es lo que el personaje quiere?", "Sí", "Es su objetivo."),
        E("¿Inferir es deducir con pistas?", "Sí", "No solo copiar."),
        E("¿Un rasgo es una característica del personaje?", "Sí", "Describe su forma de ser."),
    ],
    ("Descubre la intención. Lee: «Camilo ve que su compañera Vale no entiende un ejercicio. Se sienta a su lado, saca su cuaderno y le dice: Si quieres, te lo explico con un ejemplo». Escribe con tus palabras: 1) qué quiere Camilo, 2) una pista de lo que dice y una de lo que hace, 3) un rasgo de Camilo. Luego lee tu respuesta a un compañero de equipo o a una persona de tu casa y escuchen otra idea.",
     "1) Quiere ayudar a Vale. 2) Dice: te lo explico con un ejemplo; se sienta a su lado. 3) Es colaborador.",
     ["dice qué quiere el personaje", "da una pista de lo que dice y otra de lo que hace", "nombra un rasgo con apoyo en el texto"], ["hoja con tres respuestas y comentario del equipo"], ["afirmar sin pista", "ignorar una de las pistas"],
     "Si no hay pista, pregunta qué dice o hace Camilo que muestre eso."),
    "Mira un gesto o una acción de alguien de tu casa y piensa qué intención podría tener.",
    "Escribe una escena de dos personajes y marca la intención de cada uno.",
)

# ================================================================ OA 30 · clase 2
reg(
    OA30, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar.",
    "Aprenderé a construir la voz y el gesto de un personaje a partir de sus rasgos, sin exagerar ni burlarme de nadie. Sirve para actuar con respeto, desarrollar mi lenguaje y fortalecer mi confianza.",
    ["Sé inferir la intención de un personaje.", "Sé observar voz y gesto."],
    [
        "Para caracterizar a un personaje elegimos una voz y un gesto que muestren cómo es. Un personaje tímido puede hablar bajito y encogerse un poco. Uno valiente puede hablar fuerte y mantener la cabeza en alto. La voz y el gesto deben salir de los rasgos y de la intención del personaje, no de una moda.",
        "Una caricatura es una imitación exagerada que se burla de algo. Cuando caracterizamos, no hacemos caricatura de personas reales ni de grupos. No imitamos de forma burlona la forma de hablar, la edad, el cuerpo, un acento, una discapacidad o la manera de ser de un grupo de personas. Un estereotipo es una idea fija y simple sobre cómo es todo un grupo de personas; no lo usamos para actuar. Un personaje no se reduce a una voz graciosa: tiene intenciones y sentimientos.",
        "Trabajamos con personajes de ficción, como un zorro astuto, una niña tímida, un robot curioso o una tortuga paciente. Elegimos dos o tres rasgos y los mostramos con la voz, el gesto y el espacio. Antes de actuar, el equipo acuerda cómo lo hará y revisa que nadie se sienta herido.",
    ],
    [("caracterizar", "mostrar cómo es un personaje"), ("caricatura", "imitación exagerada que se burla de algo"), ("estereotipo", "idea fija y simple sobre cómo es un grupo de personas"), ("voz", "forma de sonar al hablar"), ("gesto", "movimiento de la cara o del cuerpo")],
    [
        ("Elegir voz y gesto", "Personaje: una tortuga paciente. ¿Qué voz y gesto muestran su rasgo?", ["Pienso en la paciencia.", "La voz es calmada.", "Los gestos son lentos."], "Voz calmada y gestos lentos."),
        ("Evitar la caricatura", "Un compañero quiere imitar de forma burlona cómo habla una persona mayor. ¿Qué haces?", ["Pienso si es respetuoso.", "No lo hago.", "Elijo un personaje de ficción."], "No lo hago y propongo un personaje de ficción con un rasgo claro."),
    ],
    [("Hacer una voz graciosa para un personaje, sin pensar en lo que quiere.", "Se reduce a un chiste.", "Elige la voz según el rasgo y la intención."), ("Imitar con burla cómo habla o cómo es otra persona.", "Es una burla y puede lastimar.", "Usa personajes de ficción y rasgos de personalidad.")],
    [
        E("Un robot curioso mira todo de cerca y pregunta mucho. ¿Qué gesto sirve: mirar de cerca o dormir?", "Mirar de cerca", "Mirar de cerca muestra curiosidad."),
        E("¿Una caricatura es una imitación exagerada que se burla? ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        E("¿Los personajes de ficción, como un zorro astuto, sirven para caracterizar?", "Sí", "Permiten mostrar rasgos sin burlarse de personas reales."),
    ],
    [
        E("¿Por qué no imitamos burlonamente la forma de hablar de otras personas?", "Porque es una burla y puede lastimar", "Respetar a las personas es importante."),
        E("¿La voz y el gesto del personaje deben salir de sus rasgos o de una moda?", "De sus rasgos", "Así el personaje es coherente."),
        E("¿Un personaje tímido habla bajito y se encoge un poco o grita y salta?", "Habla bajito y se encoge un poco", "Son pistas de timidez."),
    ],
    [
        E("Personaje: una niña valiente. Elige la voz y el gesto: a) voz firme y cabeza en alto b) voz muy bajita y mirando al suelo.", "a", "Voz firme y cabeza en alto muestran valentía."),
        E("Personaje: un zorro astuto. ¿Qué gesto sirve: entrecerrar los ojos y sonreír de lado o caerse al suelo?", "Entrecerrar los ojos y sonreír de lado", "Esos gestos muestran astucia."),
        E("Personaje: una tortuga paciente. ¿Qué ritmo de voz usas: lento y calmado o rápido y nervioso?", "Lento y calmado", "La paciencia se muestra con calma."),
    ],
    [
        E("Teo actúa un personaje tímido solo con una voz chistosa y cantarina. Ema actúa el mismo personaje con voz baja, mirada al suelo y pasos cortos. ¿Quién caracteriza mejor?", "Ema", "Usa voz y gestos que muestran el rasgo."),
        E("Un compañero propone imitar cómo camina una persona con una discapacidad. ¿Es respetuoso?", "No", "Sería una burla."),
    ],
    [
        E("Un equipo debe actuar a un perro leal. ¿Qué dos gestos sirven: seguir de cerca a su amigo y mirar atento, o ignorar a todos y salir corriendo?", "Seguir de cerca a su amigo y mirar atento", "Seguir de cerca muestra lealtad."),
        E("Elige un personaje de ficción adecuado: a) un dragón miedoso con voz temblorosa b) imitar a una persona del curso con burla.", "a", "El dragón es de ficción."),
    ],
    [E("Tu equipo acuerda cómo actuar un robot curioso: ojos muy abiertos, voz suave y pregunta a todo. Un integrante propone agregar una burla a alguien del curso. ¿Cómo responde el equipo: aceptarla o decir que no y mantener el robot curioso?", "Decir que no y mantener el robot curioso", "La burla no es respetuosa.")],
    [
        E("¿Puedo caracterizar a un personaje con respeto?", "Sí", "Con rasgos, voz y gesto."),
        E("¿La caricatura se burla?", "Sí", "Es exagerada y puede herir."),
        E("¿Tengo que revisar que nadie se sienta herido?", "Sí", "Cuidar al equipo es parte del trabajo."),
    ],
    ("Construye un personaje sin caricatura. Elige uno de estos personajes de ficción: una tortuga paciente, un zorro astuto, un robot curioso o una niña valiente. Escribe: 1) dos rasgos, 2) cómo será su voz, 3) un gesto, 4) qué quiere (su intención). Actúa 30 segundos frente a un compañero de equipo o una persona de tu casa.",
     "Robot curioso. Rasgos: curioso y amable. Voz suave y clara. Gesto: mira de cerca los objetos. Intención: descubrir cómo funciona una puerta.",
     ["elige un personaje de ficción", "relaciona voz y gesto con los rasgos", "no hace burla de personas"], ["hoja con el personaje y breve actuación"], ["personaje reducido a una voz graciosa", "imitar con burla"],
     "Si la voz es solo graciosa, pregunta qué rasgo o intención muestra."),
    "Inventa un personaje de ficción con un rasgo y muestra su voz a una persona de tu casa.",
    "Crea dos versiones del mismo personaje con rasgos distintos y compáralas.",
)

# ================================================================ OA 30 · clase 3
reg(
    OA30, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para responder como otro personaje.",
    "Aprenderé a responder en una escena manteniendo el carácter y la intención de mi personaje. Sirve para improvisar con coherencia y para escuchar a mis compañeros.",
    ["Sé inferir la intención.", "Sé elegir voz y gesto sin caricatura."],
    [
        "Mantener el personaje significa que lo que dice y hace sigue siendo coherente con sus rasgos y su intención, aunque otra persona lo sorprenda. Si mi personaje es curioso, cuando otro le habla, él pregunta. Si es tímido, responde bajito. Si es valiente, enfrenta el problema. Así el público cree en el personaje.",
        "Para responder, escuchamos primero lo que dijo el otro personaje. Luego pensamos: ¿qué diría mi personaje según su rasgo?, ¿qué quiere lograr ahora? y respondemos con voz y gesto acordes. Cuando improvisamos, aceptamos lo que el otro propone y le agregamos algo: «Sí, y además…». No contradecimos sin razón.",
        "También cuidamos al equipo: respondemos con respeto, sin quitar el turno ni ridiculizar al compañero. Una escena sale bien cuando todos aportan. Si me equivoco, respiro, sigo y agrego algo coherente. Practicar da confianza y ayuda a desarrollar el lenguaje.",
    ],
    [("coherente", "que mantiene lo que es y quiere el personaje"), ("improvisar", "inventar en el momento sin haberlo escrito"), ("escuchar", "poner atención a lo que dice el otro"), ("responder", "decir algo como contestación a lo que se oyó"), ("aceptar y agregar", "tomar la idea del otro y sumar algo")],
    [
        ("Responder con coherencia", "Tu personaje es un zorro astuto. Otro personaje dice: «¿Dónde está el queso?». ¿Qué responde tu zorro?", ["Pienso en su astucia.", "Quiere conseguir el queso.", "Responde con un truco."], "«Sé dónde está; te lo digo si me ayudas a abrir la caja.»"),
        ("Aceptar y agregar", "Tu compañera dice: «Mira, hay una puerta secreta». ¿Cómo respondes, aceptando y agregando?", ["Acepto lo que dijo.", "Agrego algo.", "Mantengo mi personaje."], "«Sí, y además tiene una cerradura dorada.»"),
    ],
    [("Cambiar de personalidad a mitad de la escena.", "El público no entiende al personaje.", "Mantén sus rasgos y su intención."), ("Contradecir todo lo que dice el compañero.", "La escena se detiene.", "Acepta y agrega algo.")],
    [
        E("Un personaje valiente, ¿enfrenta el problema o huye siempre?", "Enfrenta el problema", "Es coherente con su rasgo."),
        E("Improvisar es inventar en el momento. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        E("Antes de responder, ¿escucho lo que dijo el otro o hablo enseguida?", "Escucho lo que dijo el otro", "Así respondo con sentido."),
    ],
    [
        E("¿Qué significa mantener el personaje?", "Responder según sus rasgos y su intención", "Así el personaje es coherente."),
        E("¿Para qué sirve «Sí, y además…»?", "Para aceptar lo que dijo el otro y agregar algo", "Hace crecer la escena."),
        E("¿Por qué no se ridiculiza al compañero?", "Porque se cuida al equipo", "La cooperación es parte del trabajo."),
    ],
    [
        E("Personaje: tortuga paciente. Otro dice: «¡Apúrate!». ¿Qué responde la tortuga: «Con calma llegaremos» o «¡Me voy corriendo!»?", "Con calma llegaremos", "Es coherente con su paciencia."),
        E("Personaje: robot curioso. Otro dice: «Esto es un abanico». ¿Qué pregunta el robot: «¿Cómo hace el aire?» o «No me importa»?", "¿Cómo hace el aire?", "Preguntar cómo funciona es curioso."),
        E("Personaje: niña tímida. Otra dice: «¿Quieres jugar?». ¿Cómo responde: a) «Sí, ¿puedo?» bajito b) «¡Sí! ¡Yo mando!» gritando.", "a", "Es coherente con su timidez."),
    ],
    [
        E("Ana tiene un zorro astuto. En la escena de pronto actúa como un zorro bondadoso y distraído. ¿Mantiene el personaje?", "No", "Cambió sus rasgos sin razón."),
        E("Beto dice «sí, y además…» y suma algo. Teo dice «no» a todo. ¿Quién ayuda más a la escena?", "Beto", "Acepta y construye."),
    ],
    [
        E("Dos personajes: un dragón miedoso y un zorro astuto. El zorro dice: «Yo te cuido». El dragón responde coherente con su rasgo: a) «¿De verdad? Me da un poco de miedo.» b) «No necesito a nadie.»", "a", "Es coherente con su miedo."),
        E("Ordena: a) escuchar lo que dijo el otro b) pensar qué diría mi personaje c) responder con voz y gesto. Escribe las letras.", "a, b, c", "Primero escucho, luego pienso y después respondo."),
    ],
    [E("En una escena de equipo, tu compañero improvisa: «Encontré un mapa». Tu personaje es curioso. ¿Cuál es la mejor respuesta: «¿Qué dice el mapa? Quiero verlo» o «Eso no existe»?", "¿Qué dice el mapa? Quiero verlo", "Acepta y es coherente con la curiosidad.")],
    [
        E("¿Debo aceptar lo que propone mi compañero?", "Sí", "Así la escena avanza."),
        E("¿Mantener el personaje es ser coherente?", "Sí", "Su forma de ser no cambia sin razón."),
        E("¿Improvisar significa inventar sin escribir?", "Sí", "Lo hago en el momento."),
    ],
    ("Responde manteniendo el personaje. En pareja o con una persona de tu casa, elijan personajes: tú eres una tortuga paciente o un robot curioso; la otra persona es un zorro astuto. El zorro empieza diciendo: «Hay un tesoro, pero necesito ayuda». Improvisen cuatro intervenciones cada uno, aceptando y agregando (si estás solo, puedes hablar en voz alta por los dos personajes). Después escribe una frase de lo que dijo tu personaje y el rasgo que mostró.",
     "Tortuga: Con calma podemos buscarlo. Rasgo: paciente.",
     ["responde según el rasgo del personaje", "acepta y agrega ideas", "respeta al compañero"], ["improvisación oral y frase escrita"], ["cambiar de personalidad sin razón", "contradecir todo"],
     "Si cambia de rasgo, pregunta qué diría su personaje según lo que es."),
    "Inventa una breve escena con una persona de tu casa donde ambos mantengan sus personajes.",
    "Escribe tres respuestas distintas de un mismo personaje para tres frases del otro personaje.",
)

# ================================================================ OA 30 · clase 4
reg(
    OA30, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: dos o tres personas de tu casa para formar un equipo.",
    "Aprenderé a ensayar una escena en equipo y a dar y recibir comentarios que ayuden. Sirve para trabajar junto a otros, mejorar y fortalecer la confianza en mí mismo.",
    ["Sé caracterizar personajes sin caricatura.", "Sé responder manteniendo el personaje."],
    [
        "Para ensayar una escena en equipo, primero repartimos roles: quién actúa a cada personaje, quién cuida el tiempo y quién anota los comentarios. Quien no quiere actuar puede elegir otro rol: todos los roles cuentan. Luego ensayamos más de una vez. En cada ensayo probamos una pequeña mejora: más volumen, un gesto más claro, una pausa. Ensayar no es repetir igual: es mejorar.",
        "La retroalimentación es un comentario para ayudar a mejorar. Una buena retroalimentación es amable y específica. Tiene tres partes: «Me gustó…», «Podrías…» y «Lo hiciste claro cuando…». Por ejemplo: «Me gustó tu voz baja de tímida; podrías mirar un poco más al público». No se dice «lo hiciste mal», porque no ayuda.",
        "Cuando recibimos un comentario, escuchamos hasta el final y damos las gracias. Podemos probar la sugerencia en el siguiente ensayo. La cooperación mejora el trabajo de todos y ayuda a que cada uno se sienta valorado. Un comentario amable también cuida la autoestima, que es el valor que me doy a mí mismo. Al terminar, el equipo agradece a quienes participaron y celebra lo logrado.",
    ],
    [("ensayo", "práctica de una escena antes de presentarla"), ("retroalimentación", "comentario que ayuda a mejorar"), ("específico", "que dice algo concreto"), ("rol", "tarea que tiene cada integrante"), ("autoestima", "valor que tengo de mí mismo")],
    [
        ("Dar un buen comentario", "Un compañero actuó de un robot curioso. Dale retroalimentación con las tres partes.", ["Digo lo que me gustó.", "Propongo una mejora.", "Digo qué hizo claro."], "«Me gustó cómo miraste de cerca; podrías hablar un poco más fuerte; lo hiciste claro cuando preguntaste cómo funciona.»"),
        ("Recibir un comentario", "Una compañera te dice: «Podrías hablar más despacio». ¿Qué haces?", ["Escucho hasta el final.", "Digo gracias.", "Pruebo en el siguiente ensayo."], "Agradezco y pruebo hablar más despacio."),
    ],
    [("Decir «lo hiciste mal».", "No dice qué mejorar y puede herir.", "Usa «Me gustó…, podrías…»."), ("Defenderse enojado cuando me dan un comentario.", "No se aprende.", "Escucha, agradece y prueba.")],
    [
        E("La retroalimentación es un comentario para ayudar a mejorar. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
        E("¿Una buena retroalimentación es amable o grosera?", "Amable", "Debe ayudar sin herir."),
        E("Ensayar, ¿es repetir igual o intentar mejorar?", "Intentar mejorar", "Cada ensayo prueba algo nuevo."),
    ],
    [
        E("¿Cuáles son las partes de un buen comentario: me gustó, podrías y lo hiciste claro cuando?", "Me gustó, podrías y lo hiciste claro cuando", "Son las tres partes."),
        E("¿Por qué no se dice «lo hiciste mal»?", "Porque no dice qué mejorar y puede herir", "El comentario debe ayudar."),
        E("Cuando recibo un comentario, ¿qué hago: escucho y agradezco o me enojo?", "Escucho y agradezco", "Así puedo mejorar."),
    ],
    [
        E("Un compañero habló muy bajito en su escena. Elige el comentario: a) «Me gustó tu personaje; podrías hablar un poco más fuerte.» b) «No se te oyó nada, mal.»", "a", "Es amable y específico."),
        E("Un equipo de tres personas reparte tres roles distintos: actuar al zorro, actuar a la tortuga y anotar los comentarios. Cada integrante tiene un rol. ¿Cuántas personas actúan?", "Dos", "Hay dos personajes y una persona que anota."),
        E("Quieres felicitar a una compañera. Elige: a) «Me gustó cómo usaste el gesto de la tortuga lenta.» b) «Todo bien.»", "a", "Es una felicitación específica."),
    ],
    [
        E("Después del primer ensayo, el equipo dice: «Me gustó el final; podrían dejar una pausa antes de la última frase». ¿Qué prueba el equipo en el segundo ensayo?", "Una pausa antes de la última frase", "Es la sugerencia que recibieron."),
        E("Un integrante siempre quiere ser el único protagonista. ¿Qué ayuda al equipo: repartir los roles entre todos o dejarlo?", "Repartir los roles entre todos", "Repartir roles hace participar a todos."),
    ],
    [
        E("Un niño se siente nervioso por actuar. ¿Qué comentario ayuda a su autoestima: «Gracias por atreverte; me gustó cómo lo hiciste» o «Actuaste mal, mejor no lo intentes»?", "Gracias por atreverte; me gustó cómo lo hiciste", "Valora su esfuerzo."),
        E("Ordena para ensayar bien: a) repartir roles b) dar y recibir comentarios c) ensayar más de una vez. Escribe las letras.", "a, c, b", "Se reparte, se ensaya y luego se comenta."),
    ],
    [arith("Tu equipo ensayó dos veces su escena de 3 minutos. ¿Cuántos minutos ensayaron en total?", "3+3", "Se suman los minutos de cada ensayo.", " minutos")],
    [
        E("¿Puedo dar un comentario amable y específico?", "Sí", "Ayuda a mejorar."),
        E("¿Cooperar es trabajar juntos?", "Sí", "Todos aportan para lograr algo."),
        E("¿Debo agradecer los comentarios?", "Sí", "Muestra respeto y deseo de mejorar."),
    ],
    ("Ensaya y retroalimenta en equipo. Con dos o tres compañeros o personas de tu casa, preparen una escena de 2 minutos con personajes de ficción (por ejemplo, una tortuga paciente, un zorro astuto y un robot curioso). Repartan roles, hagan dos ensayos y escriban un comentario para cada integrante con «Me gustó…, podrías… y lo hiciste claro cuando…». Anota una mejora que probaron en el segundo ensayo.",
     "Me gustó tu voz calmada de tortuga; podrías mirar más a tus compañeros; lo hiciste claro cuando esperaste tu turno. Mejora: una pausa antes de la última frase.",
     ["reparten roles", "dan comentarios amables y específicos", "prueban una mejora en el segundo ensayo"], ["comentarios escritos y escena ensayada"], ["comentarios que ofenden", "ensayo repetido igual"],
     "Si el comentario es negativo, pide que lo reformulen con «me gustó» y «podrías»."),
    "Pide a una persona de tu casa que te dé un comentario con «me gustó…, podrías…».",
    "Escribe una pauta de tres preguntas para evaluar un ensayo de teatro en equipo.",
)

# ================================================================ OA 31 · clase 1
reg(
    OA31, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer el poema en voz alta.",
    "Aprenderé a comprender un poema antes de memorizarlo: qué dice cada verso, qué imagen muestra y qué siento. Sirve para recitarlo con sentido y con más confianza.",
    ["Sé leer un poema corto.", "Sé qué es un verso."],
    [
        "Recitar es decir un poema de memoria o leyéndolo, con voz expresiva. Antes de memorizar, conviene comprender. Un poema se organiza en versos, que son las líneas, y a veces en estrofas, que son grupos de versos. Cada verso dice algo o muestra una imagen. Si entendemos las imágenes, recordamos mejor el poema. Las palabras nuevas de un poema, como «tejado» (el techo de tejas), aumentan nuestro vocabulario: preguntamos su significado y la usamos al hablar.",
        "Para comprender un poema, lo leemos entero, preguntamos por las palabras desconocidas y explicamos cada verso con nuestras palabras. Por ejemplo, «toca el techo con sus dedos» muestra la lluvia golpeando el techo como si tuviera dedos. Esa imagen nos ayuda a elegir cómo decir el verso: suave y ligero.",
        "También pensamos qué se siente en el poema: calma, alegría, misterio. Esa emoción orienta la voz. Memorizar sin comprender suele fallar y suena sin vida. Memorizar con sentido es más fácil, porque cada verso se asocia a una imagen. Recitar mejora el vocabulario, la expresión y la confianza.",
    ],
    [("verso", "cada línea de un poema"), ("estrofa", "grupo de versos"), ("imagen", "forma de ver algo con palabras"), ("recitar", "decir un poema con voz expresiva"), ("emoción", "lo que se siente, como calma o alegría")],
    [
        ("Contar los versos", "Poema «La lluvia»: «La lluvia llega despacio, / toca el techo con sus dedos, / canta bajito en la ventana / y se va cuando hay silencio». ¿Cuántos versos tiene?", ["Cada línea es un verso.", "Cuento las líneas.", "Hay cuatro."], "Cuatro versos."),
        ("Explicar una imagen", "Verso: «toca el techo con sus dedos». ¿Qué imagen muestra?", ["Pienso en la lluvia.", "Los dedos son las gotas.", "Golpean suave el techo."], "La lluvia golpea suavemente el techo como si tuviera dedos."),
    ],
    [("Memorizar sin entender lo que dice.", "Suena sin vida y se olvida más rápido.", "Explica cada verso con tus palabras antes de memorizar."), ("Saltarse las palabras que no conozco.", "No se entiende la imagen.", "Pregunta o busca su significado.")],
    [
        E("Un verso es una línea de un poema. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
        E("Poema: «El sol sale despacio, / pinta de oro el cerro, / y todos despiertan / con su luz y su aliento». ¿Cuántos versos tiene?", "Cuatro", "Hay cuatro líneas."),
        E("¿Qué hago primero: comprender el poema o memorizarlo?", "Comprenderlo", "Así recito con sentido."),
    ],
    [
        E("¿Por qué conviene comprender antes de memorizar?", "Porque cada verso se asocia a una imagen y se recuerda mejor", "Entender ayuda a memorizar."),
        E("En «canta bajito en la ventana», ¿cómo suena la lluvia: bajito o muy fuerte?", "Bajito", "El verso dice bajito."),
        E("¿Qué emoción siente «La lluvia»: calma o enojo?", "Calma", "Llega despacio y canta bajito."),
    ],
    [
        E("Verso: «y se va cuando hay silencio». ¿Qué pasa con la lluvia: sigue o se va?", "Se va", "El verso dice que se va."),
        E("Explica con tus palabras «llega despacio»: a) llega con calma y suavidad b) llega muy fuerte.", "a", "«Despacio» es lento y suave."),
        E("Verso: «pinta de oro el cerro». ¿Qué imagen muestra: el sol colorea el cerro o una persona pinta una pared?", "El sol colorea el cerro", "La luz del sol hace ver el cerro dorado."),
    ],
    [
        E("Ana memoriza «La lluvia» sin saber qué dice y lo recita muy rápido. Beto lo comprende y lo recita suave y lento. ¿Cuál recitación comunica mejor?", "La de Beto", "Entiende las imágenes y las muestra."),
        E("Una palabra de un poema es desconocida: ¿Qué haces: preguntar o buscar el significado, o saltarla?", "Preguntar o buscar el significado", "Entender las palabras ayuda a comprender."),
    ],
    [
        E("Poema: «Mi sombra camina conmigo, / se hace grande, se hace chica; / si me escondo bajo un árbol, / ya no sabe dónde está». ¿Cuántos versos tiene?", "Cuatro", "Hay cuatro líneas."),
        E("En el poema de la sombra, ¿qué pasa si el niño se esconde bajo un árbol: la sombra se pierde o se hace más grande?", "La sombra se pierde", "El poema dice que no sabe dónde está."),
    ],
    [E("Quieres memorizar «La lluvia». Escribes una imagen para cada verso. ¿Cuántas imágenes escribes si el poema tiene 4 versos?", "Cuatro", "Una por cada verso.")],
    [
        E("¿Un verso es una línea del poema?", "Sí", "Así se llaman."),
        E("¿Conviene comprender antes de memorizar?", "Sí", "Ayuda a recitar con sentido."),
        E("¿La emoción del poema guía mi voz?", "Sí", "Una voz suave o alegre se elige según el poema."),
    ],
    ("Comprende un poema. Lee «La lluvia»: «La lluvia llega despacio, / toca el techo con sus dedos, / canta bajito en la ventana / y se va cuando hay silencio». Escribe con tus palabras qué dice cada verso (cuatro explicaciones), qué emoción se siente y qué palabra no entendiste, si hubo alguna. Luego léelo en voz alta a una persona de tu casa, pensando en las imágenes.",
     "1) La lluvia empieza suave. 2) Golpea el techo con gotas ligeras. 3) Suena bajito en la ventana. 4) Se termina cuando todo queda en silencio. Emoción: calma.",
     ["explica los cuatro versos", "nombra la emoción", "lee con sentido"], ["hoja con explicaciones y lectura en voz alta"], ["memorizar sin entender", "no explicar las imágenes"],
     "Si repite el verso, pregunta qué imagen ve."),
    "Lee en voz alta un poema que te lea una persona de tu casa y explica un verso.",
    "Escribe un poema de cuatro versos sobre algo que te guste y explícalo.",
)

# ================================================================ OA 31 · clase 2
reg(
    OA31, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: lápices de colores para marcar el poema.",
    "Aprenderé a marcar las pausas y las palabras clave de un poema. Sirve para recitarlo con ritmo y destacar lo importante.",
    ["Sé qué es un verso.", "Sé entender las imágenes de un poema."],
    [
        "Cuando recitamos, no decimos todo seguido. Hacemos pausas, que son momentos de silencio breve. En un poema, la coma pide una pausa corta y el punto pide una pausa larga. El punto y coma (;) pide una pausa un poco más larga que la coma; al marcar lo tratamos como pausa larga. A veces también hacemos una pausa al terminar un verso, aunque no haya signo, si el sentido lo pide. Las pausas ayudan a respirar y a que se entienda mejor.",
        "También destacamos las palabras clave, que son las más importantes para el sentido. Por ejemplo, en «un gato mira la luna», las palabras clave pueden ser «gato» y «luna». Las destacamos subiendo un poco el volumen, alargando la palabra o haciendo un gesto pequeño. No hay que destacar todas, porque entonces ninguna se nota.",
        "Para marcar un poema usamos signos en el texto: una raya (/) para la pausa corta, dos rayas (//) para la pausa larga y un subrayado para la palabra clave. Así, cuando ensayamos, recordamos dónde respirar y qué resaltar. Marcar el poema es una guía que podemos cambiar si descubrimos una forma mejor.",
    ],
    [("pausa", "momento breve de silencio al recitar"), ("palabra clave", "palabra importante para el sentido"), ("marcar", "poner signos en el texto como guía"), ("destacar", "resaltar con la voz o el gesto"), ("signo de puntuación", "coma, punto y otras marcas que ordenan el texto")],
    [
        ("Contar pausas", "Poema: «Sobre el tejado, de noche, / un gato mira la luna. / Se estira, bosteza, calla, / y se duerme sin ninguna prisa.». Las comas piden pausa corta y los puntos pausa larga. ¿Cuántas comas hay?", ["Reviso verso por verso.", "Primer verso: dos comas (tejado, noche).", "Tercer verso: tres comas (estira, bosteza, calla)."], "Cinco comas."),
        ("Elegir palabras clave", "En «un gato mira la luna», ¿cuáles son palabras clave?", ["Busco las palabras que dan el sentido.", "Gato y luna.", "Un y la son menos importantes."], "Gato y luna."),
    ],
    [("Destacar todas las palabras.", "Ninguna se nota.", "Elige dos o tres palabras clave por verso."), ("Hacer pausas donde no hay sentido.", "Se corta una idea en dos.", "Sigue las comas, los puntos y el sentido.")],
    [
        E("La coma pide una pausa corta. ¿Verdadero o falso?", "Verdadero", "Así se lee en voz alta."),
        E("El punto pide una pausa larga. ¿Verdadero o falso?", "Verdadero", "Marca el final de una idea."),
        E("¿Cuál es una palabra clave en «un gato mira la luna»: gato o un?", "Gato", "Es una palabra importante."),
    ],
    [
        E("¿Por qué hacemos pausas al recitar?", "Para respirar y que se entienda", "Ayudan al sentido y a la voz."),
        E("En Lenguaje: ¿Qué es una palabra clave?", "Una palabra importante para el sentido", "Se destaca con la voz."),
        E("¿Por qué no se destacan todas las palabras?", "Porque entonces ninguna se nota", "Destacar es elegir."),
    ],
    [
        E("En el poema del gato, ¿cuántos puntos hay en los cuatro versos?", "Dos", "Uno tras «luna» y otro tras «prisa»."),
        E("En el verso «Se estira, bosteza, calla,», ¿cuántas pausas cortas hay?", "Tres", "Hay tres comas."),
        E("En «Sobre el tejado, de noche,» ¿cuántas pausas cortas marcas con rayas?", "Dos", "Hay una coma tras tejado y otra tras noche."),
    ],
    [
        E("Ana recita «Se estira bosteza calla» sin pausas. Beto hace pausa tras cada coma. ¿Quién recita mejor?", "Beto", "Las pausas ayudan al sentido."),
        E("Luis subraya en un verso todas las palabras. ¿Está destacando bien?", "No", "Si todas son claves, ninguna destaca."),
    ],
    [
        E("Poema: «El viento corre en la calle / y levanta las hojas secas; / silba, silba, silba muy fuerte, / pero al llegar la noche, se duerme». Hay un punto y coma (;) en el segundo verso. ¿Pide pausa corta o larga?", "Larga", "Es una pausa mayor que la coma."),
        E("En el mismo poema, ¿cuántas comas hay?", "Cuatro", "Tres en el tercer verso y una en el cuarto."),
    ],
    [E("En el poema del viento, el tercer verso dice «silba, silba, silba muy fuerte». ¿Qué palabra conviene destacar con la voz: silba o muy?", "Silba", "Es la palabra que repite el sonido.")],
    [
        E("¿Puedo marcar mi poema con rayas?", "Sí", "Es una guía para ensayar."),
        E("¿Puedo cambiar las pausas si descubro una forma mejor?", "Sí", "La marca es una guía."),
        E("¿Las pausas ayudan a respirar?", "Sí", "Dan tiempo a tomar aire."),
    ],
    ("Marca un poema. Copia en tu hoja el poema «Mi sombra camina conmigo, / se hace grande, se hace chica; / si me escondo bajo un árbol, / ya no sabe dónde está». Marca con una raya (/) las pausas cortas, con dos rayas (//) las largas y subraya dos palabras clave por verso. Recítalo a una persona de tu casa respetando tus marcas.",
     "Mi sombra camina conmigo, / se hace grande, / se hace chica; // si me escondo bajo un árbol, / ya no sabe dónde está. Claves: sombra, camina; grande, chica; escondo, árbol; sabe, está.",
     ["marca pausas cortas y largas", "subraya palabras clave", "recita respetando las marcas"], ["poema marcado y recitación"], ["subrayar todo", "pausas sin sentido"],
     "Si subraya demasiado, pide elegir solo las más importantes."),
    "Lee un poema a una persona de tu casa haciendo pausas en las comas y los puntos.",
    "Marca un segundo poema y compara tus marcas con las de otra persona.",
)

# ================================================================ OA 31 · clase 3
reg(
    OA31, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: un espejo y una persona de tu casa como público.",
    "Aprenderé a ensayar el ritmo, la voz y el gesto de un poema. Sirve para que mi recitación sea expresiva, con entonación y volumen adecuados.",
    ["Sé marcar pausas y palabras clave.", "Sé qué emoción tiene un poema."],
    [
        "El ritmo de un poema es la velocidad y el movimiento de sus versos al decirlos. Un poema sobre una tortuga pide un ritmo lento; uno sobre un viento fuerte pide un ritmo rápido y sonoro. Elegimos el ritmo según lo que dice el poema y la emoción que muestra.",
        "La voz tiene volumen, entonación y expresión. El volumen es qué tan fuerte hablo. La entonación es cómo sube y baja la voz: sube en una pregunta o una sorpresa, baja al terminar una idea. La expresión es mostrar la emoción del poema con la voz y la cara. No hay que gritar: hay que llegar hasta el último del público con claridad.",
        "Los gestos acompañan, no reemplazan, las palabras. Un gesto suave de las manos puede mostrar la lluvia; mirar hacia arriba, el viento. Los gestos deben ser pequeños y claros. Mientras ensayamos, probamos distintas formas y elegimos la que mejor comunica. Ensayar frente a un espejo o a una persona ayuda a notar qué mejorar.",
    ],
    [("ritmo", "velocidad y movimiento al decir los versos"), ("volumen", "qué tan fuerte suena la voz"), ("entonación", "cómo sube y baja la voz al hablar"), ("expresión", "mostrar la emoción con voz y cara"), ("gesto", "movimiento de las manos, cara o cuerpo")],
    [
        ("Elegir el ritmo", "Poema: «El viento corre en la calle / y levanta las hojas secas». ¿Qué ritmo conviene: rápido o lento?", ["Pienso qué hace el viento.", "Corre y levanta hojas.", "Pide movimiento rápido."], "Un ritmo rápido y ligero."),
        ("Elegir un gesto", "Poema: «La lluvia llega despacio». ¿Qué gesto sirve: bajar las manos despacio como gotas o saltar con los brazos?", ["Pienso en la lluvia suave.", "Las manos bajan despacio.", "Eso acompaña el verso."], "Bajar las manos despacio como gotas."),
    ],
    [("Recitar siempre al mismo volumen y velocidad.", "No se nota la emoción ni las imágenes.", "Cambia ritmo y volumen según el verso."), ("Gritar para que me oigan.", "La voz se cansa y no se entiende.", "Habla claro, proyecta la voz y respira.")],
    [
        E("¿Un poema sobre una tortuga pide un ritmo lento o rápido?", "Lento", "La tortuga se mueve despacio."),
        E("¿La entonación es cómo sube y baja la voz?", "Sí", "Se usa para mostrar el sentido."),
        E("¿Un gesto acompaña las palabras o las reemplaza?", "Las acompaña", "No sustituye el poema."),
    ],
    [
        E("¿Por qué es mejor no gritar al recitar?", "Porque la voz se cansa y no se entiende", "Basta con hablar claro y fuerte."),
        E("¿Qué muestra mostrar la emoción con la voz y la cara?", "Expresión", "Es la parte expresiva."),
        E("¿Cuándo sube la voz: en una pregunta o al terminar una idea?", "En una pregunta", "La entonación sube al preguntar."),
    ],
    [
        E("Verso: «silba, silba, silba muy fuerte». ¿Qué volumen conviene: fuerte o muy bajito?", "Fuerte", "El sonido del viento es fuerte."),
        E("Verso: «canta bajito en la ventana». ¿Qué volumen conviene: bajito o muy fuerte?", "Bajito", "El verso dice bajito."),
        E("Verso: «se hace grande, se hace chica». ¿Qué gesto sirve: abrir y cerrar las manos o tapar la cara?", "Abrir y cerrar las manos", "Muestra el cambio de tamaño."),
    ],
    [
        E("Ana recita todo el poema del viento a ritmo lento y en voz baja. Beto cambia: rápido en los versos del viento y bajo en la noche. ¿Quién comunica mejor las imágenes?", "Beto", "Cambia el ritmo y el volumen según el poema."),
        E("Un niño agita los brazos todo el tiempo y la audiencia deja de oír las palabras. ¿Los gestos acompañan o distraen?", "Distraen", "Deben ser pequeños y claros."),
    ],
    [
        E("Poema: «Pero al llegar la noche, se duerme». ¿Qué ritmo y volumen conviene: lento y bajo o rápido y fuerte?", "Lento y bajo", "Se duerme: la voz se calma."),
        E("Ordena para ensayar: a) elegir el ritmo b) probar los gestos c) recitar frente a alguien. Escribe las letras.", "a, b, c", "Primero decido, luego pruebo y luego recito."),
    ],
    [arith("Un poema tiene 4 versos. Ensayas cada verso dos veces. ¿Cuántos versos dices en total?", "4*2", "Se multiplican los versos por las veces que ensayas cada uno.", " versos")],
    [
        E("¿Cambiar el ritmo según el poema ayuda a expresarlo?", "Sí", "Cada poema pide un ritmo."),
        E("¿Debo respirar entre versos?", "Sí", "Las pausas ayudan a la voz."),
        E("¿Un espejo puede ayudar a ensayar los gestos?", "Sí", "Permite ver qué mejorar."),
    ],
    ("Ensaya ritmo, voz y gesto. Elige uno de estos poemas: «El viento corre en la calle / y levanta las hojas secas; / silba, silba, silba muy fuerte, / pero al llegar la noche, se duerme» o «La lluvia llega despacio…» (clase 1). Ensaya tres veces frente a un espejo o a una persona de tu casa. Escribe qué ritmo usarás en cada verso, el volumen y un gesto pequeño para dos versos.",
     "Viento: versos 1 y 2 rápidos con voz firme; verso 3 con volumen alto en «silba»; verso 4 lento y bajo. Gestos: manos que se mueven como hojas; manos juntas al dormirse.",
     ["elige ritmo y volumen según cada verso", "usa gestos pequeños", "ensaya tres veces"], ["escrito de decisiones y recitación"], ["mismo ritmo en todo el poema", "gestos exagerados"],
     "Si todo es igual, pregunta qué verso pide más calma o más fuerza."),
    "Recita un poema de cuatro versos a una persona de tu casa cambiando el ritmo en dos versos.",
    "Prueba el mismo poema con dos ritmos distintos y decide cuál comunica mejor.",
)

# ================================================================ OA 31 · clase 4
reg(
    OA31, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que escuche y comente.",
    "Aprenderé a recitar un poema ante otros, a escuchar con respeto y a revisar mi recitación con una pauta. Sirve para ganar confianza y seguir mejorando.",
    ["Sé comprender un poema.", "Sé ensayar ritmo, voz y gesto."],
    [
        "Recitar ante otros muestra el trabajo de todo el proceso: comprender, marcar pausas, ensayar ritmo, voz y gesto. Antes de empezar, respiramos y miramos al público. Decimos el título del poema y, si queremos, el nombre de quien lo escribió. Si olvidamos un verso, respiramos, pensamos en la imagen y seguimos. Equivocarse no es fracasar.",
        "Quienes escuchan también tienen un rol: miran con atención, no interrumpen y aplauden al terminar. Después pueden comentar con respeto: «Me gustó cómo bajaste la voz en el último verso» o «Podrías mirar un poco más al público». No hacen burla. Escuchar con respeto cuida la confianza de quien recitó.",
        "Para revisar una recitación usamos una pauta con criterios claros: ¿se entendió el sentido?, ¿las pausas ayudaron?, ¿el ritmo y el volumen combinaron con el poema?, ¿los gestos acompañaron? Al revisar, elegimos un aspecto para mejorar en el próximo ensayo. Así aprendemos y aumentamos nuestro vocabulario y nuestra capacidad de expresarnos.",
    ],
    [("pauta", "lista de criterios para revisar un trabajo"), ("criterio", "aspecto que se mira al revisar"), ("público", "personas que escuchan"), ("confianza", "seguridad en uno mismo"), ("revisar", "mirar con atención para mejorar")],
    [
        ("Usar una pauta", "Una pauta pregunta: ¿se entendió?, ¿hubo pausas?, ¿el ritmo combinó? Lía recitó claro, con pausas y ritmo adecuado. ¿Cuántos criterios cumplió de tres?", ["Reviso cada criterio.", "Se entendió: sí.", "Hubo pausas y ritmo adecuado."], "Cumplió los tres criterios."),
        ("Dar un comentario respetuoso", "Escuchaste a un compañero que habló muy rápido. Escribe un comentario respetuoso.", ["Digo qué me gustó.", "Propongo una mejora.", "Uso un tono amable."], "«Me gustó tu poema; podrías hablar un poco más despacio para disfrutar las imágenes.»"),
    ],
    [("Burlarse de quien se equivoca al recitar.", "Quita la confianza.", "Aplaude y comenta con respeto."), ("Recitar sin mirar al público.", "No se conecta con quienes escuchan.", "Mira a distintas personas mientras recitas.")],
    [
        E("¿Qué debe hacer el público: escuchar con atención o conversar?", "Escuchar con atención", "Así se respeta a quien recita."),
        E("Si olvido un verso, ¿qué hago: respirar y seguir o salir corriendo?", "Respirar y seguir", "Equivocarse no es fracasar."),
        E("¿Una pauta es una lista de criterios para revisar? ¿Verdadero o falso?", "Verdadero", "Es su definición."),
    ],
    [
        E("¿Por qué no se hace burla de quien se equivoca?", "Porque quita la confianza", "El respeto cuida a la persona."),
        E("¿Qué se hace antes de empezar a recitar?", "Respirar y mirar al público", "Ayuda a empezar con calma."),
        E("¿Para qué sirve elegir un aspecto para mejorar?", "Para saber qué practicar en el próximo ensayo", "Hace más claro el progreso."),
    ],
    [
        arith("Una pauta tiene tres criterios. Tomás cumplió dos. ¿Cuántos le falta cumplir?", "3-2", "Se restan los criterios cumplidos.", " criterio"),
        E("Elige el mejor comentario para una compañera que recitó con buena voz pero miró al suelo: a) «Me gustó tu voz; podrías mirar más al público.» b) «Mal, no miraste.»", "a", "Es amable y específico."),
        E("Después de recitar, ¿qué hace el público: aplaude o se burla?", "Aplaude", "Reconoce el esfuerzo."),
    ],
    [
        E("Una niña tembló al comenzar. Un compañero dice: «Qué miedosa». Otro dice: «Gracias por atreverte; me gustó tu poema». ¿Quién cuida la confianza?", "El segundo", "Valora su esfuerzo."),
        E("En una pauta se cumplen tres de cuatro criterios. ¿Qué conviene hacer: celebrar lo logrado y elegir un criterio para mejorar, o decir que todo salió mal?", "Celebrar lo logrado y elegir un criterio para mejorar", "Reconoce y orienta."),
    ],
    [
        E("Ana recitó con pausas pero a un ritmo igual en todo el poema. ¿Qué criterio de la pauta debe mejorar: pausas o ritmo?", "Ritmo", "No cambió según el poema."),
        E("Ordena el proceso: a) revisar con la pauta b) recitar ante otros c) comprender el poema. Escribe las letras.", "c, b, a", "Se comprende, se recita y se revisa."),
    ],
    [arith("En el curso hay 5 estudiantes que recitan, y cada uno dura 2 minutos. ¿Cuántos minutos de recitación hay en total?", "5*2", "Se multiplican los estudiantes por los minutos de cada uno.", " minutos")],
    [
        E("¿Equivocarse al recitar es normal?", "Sí", "Se puede seguir con calma."),
        E("¿Aplaudir es una forma de respeto?", "Sí", "Reconoce el esfuerzo."),
        E("¿La pauta me ayuda a mejorar?", "Sí", "Muestra qué revisar."),
    ],
    ("Recita, escucha y revisa. Elige uno de los poemas de esta unidad (La lluvia, El gato, El viento o Mi sombra) y recítalo ante una o más personas de tu casa. Pide que escuchen con atención y te den un comentario con «Me gustó… / Podrías…». Luego completa esta pauta con Sí o No: 1) ¿Se entendió el sentido? 2) ¿Hubo pausas adecuadas? 3) ¿El ritmo combinó con el poema? 4) ¿Los gestos acompañaron? Elige un aspecto para mejorar.",
     "1) Sí. 2) Sí. 3) A medias, fue rápido al final. 4) Sí. Mejoraré el ritmo del último verso, más lento.",
     ["recita con sentido", "usa la pauta con sinceridad", "elige un aspecto para mejorar"], ["recitación ante otros y pauta completada"], ["burlas o comentarios que ofenden", "no elegir qué mejorar"],
     "Si la pauta dice todo Sí sin evidencia, pregunta cómo lo notó."),
    "Recita un poema de memoria a una persona de tu casa y pídele un comentario con «Me gustó… / Podrías…».",
    "Escribe una pauta de cuatro criterios para revisar la recitación de un compañero.",
)

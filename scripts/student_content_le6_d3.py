"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 28 (convenciones sociales en diferentes situaciones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA28 = "LE06 OA 28"
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


# ================================================================ OA 28 · clase 1
reg(
    OA28, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: dos personas de tu casa para practicar presentaciones.",
    "Aprenderé a presentarme a mí mismo y a presentar a otras personas, según quién sea cada una y en qué situación estemos. Sirve para comenzar bien una relación en un club, una visita o una reunión.",
    ["Sé saludar y decir mi nombre.", "Sé que hay datos privados que no se entregan a desconocidos."],
    [
        "Presentarse es decir quién eres de modo que otros te conozcan. Una presentación clara tiene un saludo, tu nombre y uno o dos datos útiles para conversar, como tu curso o un interés. Por ejemplo: «Buenas tardes, me llamo Rodrigo, soy de sexto básico y me gusta la astronomía». Los datos privados, como la dirección, el teléfono o las claves, no se entregan a quien recién conoces.",
        "Presentar a otros es decir a dos personas quiénes son para que se conozcan. Se nombra a ambas y se dice cómo las conoces. Hay una norma de cortesía: primero se nombra a la persona a quien se quiere mostrar más respeto, por ejemplo una persona mayor o con un cargo, y luego a la otra: «Señora Marta, le presento a mi compañero Luis». Se usa «usted» con quien merece un trato formal.",
        "Quien recibe la presentación responde con una fórmula como «mucho gusto» o «encantada de conocerte», y puede añadir una pregunta para continuar la conversación. Si estás con amigos de tu edad, el trato es más cercano: «Luis, ella es Paula, mi vecina». Elegir entre el trato formal y el cercano es parte de adaptar nuestro lenguaje a la situación.",
    ],
    [("presentarse", "decir quién eres para que otros te conozcan"), ("dato privado", "información personal que no se comparte con desconocidos"), ("trato formal", "manera respetuosa de hablar, con «usted»"), ("trato cercano", "manera de hablar con amigos, con «tú»"), ("cortesía", "conducta amable y respetuosa")],
    [
        ("Presentar a otros", "Estás con tu profesora, la señora Ana, y llega tu amigo Pedro. ¿Qué dices para presentarlos?", ["La profesora merece trato formal y se nombra primero.", "Digo cómo conozco a Pedro.", "Uso «le presento»."], "«Señora Ana, le presento a mi amigo Pedro»."),
        ("Elegir qué datos decir", "En un club nuevo debes presentarte. ¿Qué datos eliges: a) nombre, curso y algo que te gusta b) dirección y teléfono?", ["La presentación sirve para conversar.", "La dirección y el teléfono son privados.", "Elijo los datos útiles y seguros."], "a)"),
    ],
    [("Entregar la dirección o el teléfono al presentarse.", "Se piensa que presentarse es contar todo.", "Di nombre, curso e interés; guarda los datos privados."), ("Presentar con «él» o «ella» sin decir el nombre.", "Se cree que el otro ya sabe quién es.", "Di los nombres de ambos y cómo los conoces.")],
    [
        E("Entras a un club de lectura y dices: «Buenas tardes, me llamo Rodrigo y soy de sexto básico». ¿Qué datos entregó Rodrigo: nombre y curso o dirección y teléfono?", "Nombre y curso", "Son datos que sirven para conversar y no son privados."),
        E("¿Cuál es un dato privado que no debes decir a quien recién conoces: tu interés por el ajedrez o tu dirección?", "Tu dirección", "Es información personal que puede usarse mal."),
        E("Después de una presentación se responde «mucho gusto». ¿Qué función cumple: a) mostrar que te alegra conocer a la persona b) pedir permiso?", "a", "Es una fórmula de bienvenida."),
    ],
    [
        E("A un invitado mayor, el señor Ramírez, le presentas a tu compañero Hugo. ¿Qué frase es más adecuada: a) «Señor Ramírez, le presento a mi compañero Hugo.» b) «Oye, Hugo, él.»", "a", "Nombra primero a la persona mayor y usa «le presento»."),
        E("¿Qué debes decir para presentar a tu vecina Paula con tu compañero Luis, ambos de tu edad: a) «Luis, ella es Paula, mi vecina.» b) «Luis, Paula.»", "a", "Dice la relación y usa un trato cercano."),
        E("Presentas a tu compañera Lía con una vecina de 70 años, la señora Rosa. ¿A quién nombras primero: a la señora Rosa o a Lía?", "A la señora Rosa", "Primero se nombra a la persona a quien se muestra más respeto, y luego a la otra."),
    ],
    [
        E("Ordena una presentación a una visita: a) «Mucho gusto, Lía.» b) «Lía, te presento a mi amigo Tomás.» c) «Hola, Lía.» Escribe las letras.", "c, b, a", "Primero se saluda, luego se presenta y al final se responde."),
        E("En «Hola, soy Camila, estoy en sexto y me gusta dibujar», ¿cuántos datos de ella entrega, sin contar el saludo?", "3", "Nombre, curso y gusto."),
        E("Un compañero nuevo te pregunta tu dirección y tu número de teléfono apenas se conocen. ¿Qué haces: a) dices que prefieres compartir esos datos más adelante b) se los das?", "a", "Los datos privados se comparten con calma y con personas de confianza."),
    ],
    [
        E("Un estudiante dice: «Presentarse es lo mismo con todas las personas». ¿Es correcto? Responde sí o no.", "No", "El trato cambia según quién sea la otra persona y la situación."),
        E("Pía presenta a su mamá con el director sin decir sus nombres: «Director, esta es ella». ¿Qué le falta?", "El nombre de las personas", "Una buena presentación nombra a ambas."),
    ],
    [
        E("En una visita a la radio escolar, debes presentarte ante la directora y su equipo. ¿Cuál presentación es más adecuada: a) «Buenos días, me llamo Julián, soy de sexto básico y me interesa la música.» b) «Hola, soy Juli, de ahí no más.»", "a", "Lleva saludo formal, nombre, curso e interés."),
        E("Una persona te presenta a su tío y dice «Él es mi tío». ¿Qué respuesta es cortés: a) «Mucho gusto.» b) silencio?", "a", "Responder con una fórmula muestra cortesía."),
    ],
    [E("Estás con tu profesor jefe, el señor Soto, cuando llega tu amiga Laura. ¿Cuál presentación usas: a) «Señor Soto, le presento a mi amiga Laura.» b) «Laura, esto es Soto.»", "a", "Se usa un trato formal con el profesor y se dice quién es Laura.")],
    [
        E("¿Qué le falta a esta presentación: «Hola, me gusta el fútbol»: el nombre o el saludo?", "El nombre", "Una presentación dice quién eres; aquí falta el nombre."),
        E("¿Se entrega la dirección al presentarse a desconocidos? Responde sí o no.", "No", "Es un dato privado."),
        E("Al presentar a dos personas, ¿hay que decir los nombres de ambas? Responde sí o no.", "Sí", "Así saben cómo llamarse."),
    ],
    ("Escribe y practica en voz alta dos presentaciones. A) Preséntate ante un grupo de personas que no conoces, para un club de ciencias: saludo, nombre, curso y un interés. B) Presenta a tu amigo Felipe con una persona adulta que no lo conoce, usando «le presento». No incluyas datos privados. Si puedes, practícalo con una persona de tu casa.",
     "A) «Buenas tardes, me llamo Isidora, estoy en sexto básico y me interesan los insectos». B) «Señora Carmen, le presento a mi amigo Felipe, compañero de curso».",
     ["tiene saludo y nombre", "incluye un dato útil y no privado", "presenta a ambas personas con trato adecuado"], ["dos presentaciones escritas o dichas"], ["dar datos privados", "olvidar los nombres"],
     "Si algo falta, revisa tu lista: ¿saludo?, ¿nombres?, ¿cómo lo conoces?"),
    "Escribe cómo te presentarías ante un grupo de niños de otro colegio y cómo presentarías a un compañero ante tu profesora.",
    "Anota cómo se presentan las personas en una serie o noticiero y qué datos dicen de sí mismas.",
)

# ================================================================ OA 28 · clase 2
reg(
    OA28, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar saludos formales y cercanos.",
    "Aprenderé a saludar y a despedirme según la hora, la persona y la situación, usando «tú» o «usted» cuando corresponde. Sirve para empezar y terminar bien una conversación, en persona o por teléfono.",
    ["Sé presentarme y presentar a otros.", "Sé que existen el trato formal y el cercano."],
    [
        "Saludar es la primera norma de cortesía de una conversación. El saludo cambia según la hora del día («buenos días» hasta el mediodía, «buenas tardes» desde el mediodía hasta el atardecer y «buenas noches» al anochecer y de noche) y según la persona. Con amigos de tu edad puedes decir «hola, ¿cómo estás?». Con una persona mayor o con un cargo, como una directora, conviene un saludo más formal: «Buenos días, señora Alicia, ¿cómo está usted?».",
        "La diferencia entre «tú» y «usted» se nota en el verbo. Con trato cercano decimos «¿puedes ayudarme?», y con trato formal, «¿puede ayudarme?». Cuando contestas una llamada por teléfono, es útil decir tu nombre y saludar: «Aló, buenas tardes, habla Pedro». También se responde a los saludos: si alguien dice «buenos días», lo correcto es devolver el saludo.",
        "Las despedidas también siguen normas. Con cercanos se dice «chao, nos vemos mañana». Con personas de respeto, «hasta luego, que le vaya bien». Una despedida cortés cierra la conversación con calidez. Mirar a la persona, sonreír levemente y usar un tono amable completan el saludo.",
    ],
    [("saludo", "palabras o gestos con que comenzamos a hablar con alguien"), ("tú", "tratamiento cercano para amigos y personas de tu edad"), ("usted", "tratamiento respetuoso para personas mayores o con un cargo"), ("despedida", "palabras con que terminamos una conversación"), ("aló", "palabra con que se contesta una llamada telefónica")],
    [
        ("Saludo según la hora", "Son las 4 de la tarde y saludas a la bibliotecaria. ¿Qué saludo usas?", ["Reviso la hora: 4 de la tarde.", "Es después del mediodía y antes del atardecer.", "Corresponde «buenas tardes»."], "Buenas tardes."),
        ("Cambiar de tú a usted", "Cambia «¿Puedes prestarme el libro?» para hablar con tu profesor.", ["Cambio el verbo a la forma de usted.", "«Puedes» pasa a «puede».", "Agrego «por favor»."], "«¿Puede prestarme el libro, por favor?»"),
    ],
    [("Usar «tú» con una persona de respeto.", "Se piensa que ser cercano es mejor.", "Usa «usted» con adultos que no son cercanos."), ("No responder cuando alguien saluda.", "Se cree que el saludo es opcional.", "Devuelve el saludo con una frase breve.")],
    [
        E("Son las 8 de la mañana y llegas al colegio. ¿Qué saludo corresponde: buenos días o buenas noches?", "Buenos días", "Es de mañana."),
        E("Con una amiga de tu edad dices «¿Cómo estás?». ¿Qué tratamiento usas: tú o usted?", "Tú", "El verbo «estás» corresponde a «tú»."),
        E("Con la directora dices «¿Cómo está usted?». ¿Qué tratamiento usas: tú o usted?", "Usted", "El verbo «está» y la palabra «usted» indican trato formal."),
    ],
    [
        E("A las 9 de la noche saludas por teléfono a una vecina. ¿Qué saludo usas: buenas tardes o buenas noches?", "Buenas noches", "Ya es de noche."),
        E("¿Qué frase es una forma formal de despedirse: a) «Hasta luego, que le vaya bien.» b) «Chao, nos vimos.»", "a", "Usa «le» y es más respetuosa."),
        E("Contestas una llamada. ¿Cuál es mejor: a) «Aló, buenas tardes, habla Pedro.» b) «¿Qué quieres?»", "a", "Saluda y dice quién habla."),
    ],
    [
        E("Convierte a trato formal: «¿Puedes ayudarme con la caja?». Elige: a) «¿Puede ayudarme con la caja, por favor?» b) «¿Puedes ayudarme con la caja?»", "a", "Cambia «puedes» por «puede» y agrega cortesía."),
        E("Ordena un saludo en la puerta del colegio: a) responder «bien, gracias, ¿y usted?» b) decir «buenos días, señor Mario, ¿cómo está?» c) despedirse con «hasta luego». Escribe las letras.", "b, a, c", "Saludo, respuesta y despedida."),
        E("Un compañero saluda: «¡Hola!». Tú respondes: a) «Hola, ¿cómo estás?» b) no respondes. ¿Cuál es cortés?", "a", "Responder el saludo es una norma de cortesía."),
    ],
    [
        E("Un estudiante dice: «Con todas las personas se saluda igual». ¿Es correcto? Responde sí o no.", "No", "El saludo cambia con la hora, la persona y la situación."),
        E("Alguien saluda con «buenos días» a las 11 de la noche. ¿Es el saludo adecuado a la hora? Responde sí o no.", "No", "A esa hora corresponde «buenas noches»."),
    ],
    [
        E("Cambias del trato cercano al formal. «Oye, ¿viste a la profe?» pasa a: a) «Disculpe, ¿ha visto a la profesora?» b) «Oye, ¿viste a la profe?»", "a", "Usa «disculpe», «usted» y «profesora» en lugar de «profe»."),
        E("En el teléfono, una persona adulta pregunta «¿Está Camila?». ¿Qué respuesta es cortés: a) «Sí, un momento, por favor.» b) «¡Cami! ¡Te llaman!» sin responder", "a", "Responde primero a quien llama."),
    ],
    [E("Entras a la biblioteca escolar a las 11 de la mañana y la bibliotecaria te saluda. ¿Cuál es una respuesta cortés: a) «Buenos días, señora Marta. ¿Cómo está?» b) «Hola.»", "a", "Devuelve el saludo con trato formal y nombre.")],
    [
        E("¿Qué palabra se usa para contestar una llamada?", "Aló", "Es la forma habitual de contestar el teléfono."),
        E("¿«Puede» es forma de tú o de usted?", "Usted", "«Tú puedes» frente a «usted puede»."),
        E("¿Hay que devolver el saludo? Responde sí o no.", "Sí", "Es una norma básica de cortesía."),
    ],
    ("Escribe cómo saludarías en estas tres situaciones: 1) a las 8 de la mañana a tu profesora; 2) a las 3 de la tarde a un amigo de tu edad; 3) por teléfono a las 9 de la noche a la mamá de un compañero para preguntar por una tarea. Para cada una, escribe el saludo, la pregunta de bienvenida y la despedida.",
     "1) «Buenos días, profesora, ¿cómo está?… Hasta luego, que tenga un buen día».",
     ["usa el saludo correcto para la hora", "usa tú o usted según corresponda", "incluye una despedida adecuada"], ["tres saludos completos"], ["usar «tú» con personas de respeto", "olvidar la despedida"],
     "Si dudas, mira la hora y pregúntate: ¿con quién hablo, tú o usted?"),
    "Escribe una despedida formal y una cercana para dos personas distintas.",
    "Observa cómo saludan en tu casa según la hora y la persona, y anótalo.",
)

# ================================================================ OA 28 · clase 3
reg(
    OA28, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar preguntas.",
    "Aprenderé a preguntar de manera cortés y clara, y a pedir aclaraciones sin molestar. Sirve para obtener información, ayuda o indicaciones en la escuela y en la calle.",
    ["Sé saludar de manera adecuada.", "Sé que hay preguntas que se responden con sí o no y otras con más detalle."],
    [
        "Preguntar es una forma muy frecuente de interactuar: pedimos datos, ayuda o aclaraciones. Una pregunta cortés lleva una fórmula de inicio como «disculpe» o «por favor» y dice con claridad qué se necesita. Compara «¿La biblioteca?» con «Disculpe, ¿podría decirme dónde está la biblioteca?»: ambas buscan lo mismo, pero la segunda muestra respeto y se entiende mejor.",
        "Hay preguntas cerradas, que se responden con «sí» o «no» («¿está abierta la biblioteca?»), y preguntas abiertas, que piden más detalle y comienzan con «cómo», «por qué», «qué», «dónde», «cuándo». Según lo que necesites, elegirás una u otra. Para saber el horario, sirve «¿a qué hora cierra?». Para conocer una opinión, «¿por qué te parece importante?».",
        "También podemos preguntar para aclarar: «¿Podría repetir la última parte?» o «¿Quiere decir que…?». Pedir aclaración no es de mala educación; es una forma de comprender mejor. Y al terminar, se agradece la respuesta. Cuando te cuesta entender a alguien, antes de adivinar, pregunta con respeto.",
    ],
    [("pregunta cerrada", "se responde con sí o no"), ("pregunta abierta", "pide más información o una explicación"), ("aclarar", "hacer más claro lo que no entendimos"), ("disculpe", "fórmula para llamar la atención con respeto"), ("indicación", "información sobre cómo llegar o qué hacer")],
    [
        ("Pregunta cortés", "Estás en un museo y no encuentras los baños. ¿Qué preguntas al guardia?", ["Empiezo con una fórmula: «Disculpe».", "Digo con claridad lo que busco.", "Uso «podría» para suavizar."], "«Disculpe, ¿podría decirme dónde están los baños?»"),
        ("Pedir aclaración", "Una profesora explicó rápido cómo entregar un trabajo y no entendiste la última parte. ¿Qué dices?", ["No adivino.", "Pido que repita esa parte.", "Uso una fórmula cortés."], "«Disculpe, ¿podría repetir la última parte, por favor?»"),
    ],
    [("Preguntar con una sola palabra, como «¿La hora?».", "Se piensa que las preguntas breves ahorran tiempo.", "Agrega una fórmula y la frase completa: «¿Podría decirme la hora?»."), ("No preguntar por temor a molestar.", "Se cree que pedir aclaración es debilidad.", "Pregunta con respeto: comprender es parte de aprender.")],
    [
        E("¿Cuál pregunta es más cortés: a) «Disculpe, ¿podría decirme la hora?» b) «¿La hora?»", "a", "Lleva una fórmula y una frase completa."),
        E("«¿Está abierta la biblioteca?» ¿es una pregunta abierta o cerrada?", "Cerrada", "Se responde con sí o no."),
        E("«¿Por qué cerraron la puerta?» ¿es una pregunta abierta o cerrada?", "Abierta", "Pide una explicación, no solo sí o no."),
    ],
    [
        E("Quieres saber a qué hora termina una función de teatro. ¿Qué pregunta sirve mejor: a) «¿A qué hora termina la función?» b) «¿Termina la función?»", "a", "La primera pide el dato exacto que necesitas."),
        E("No entendiste una instrucción. ¿Qué dices: a) «Disculpe, ¿podría repetir esa instrucción?» b) «No entiendo nada.»", "a", "Es cortés y dice qué necesitas."),
        E("Después de que un guardia te indica dónde están los baños, ¿qué fórmula usas: gracias o perdón?", "Gracias", "Agradeces la ayuda recibida."),
    ],
    [
        E("Ordena la interacción en el museo: a) «Muchas gracias.» b) «Disculpe, ¿podría decirme dónde está la sala de dinosaurios?» c) «Está al fondo del pasillo, a la derecha.» Escribe las letras.", "b, c, a", "Se pregunta, se responde y se agradece."),
        E("Quieres conocer la opinión de un compañero sobre un libro. ¿Qué pregunta conviene: a) «¿Qué parte del libro te pareció más interesante y por qué?» b) «¿Lo leíste?»", "a", "Es abierta y pide una explicación."),
        E("Un adulto desconocido te da una dirección rápido. ¿Qué haces: a) pides amablemente que repita b) sigues sin entender?", "a", "Pedir aclaración evita errores."),
    ],
    [
        E("Un estudiante dice: «Preguntar es de mala educación». ¿Es correcto? Responde sí o no.", "No", "Preguntar con respeto es una forma de aprender."),
        E("Quieres saber si hay entradas disponibles. ¿Qué tipo de pregunta usas: cerrada o abierta?", "Cerrada", "La respuesta es sí o no."),
    ],
    [
        E("Pregunta bien formulada para saber cuántas personas caben en una sala: a) «Disculpe, ¿cuántas personas caben en esta sala?» b) «¿Sala?»", "a", "Es cortés, clara y completa."),
        E("Quieres pedir ayuda a un vendedor para encontrar cuadernos. ¿Cuál frase inicia mejor: a) «Disculpe, ¿me podría ayudar a encontrar cuadernos?» b) «¡Cuadernos!»", "a", "Llama la atención con respeto y dice qué necesitas."),
    ],
    [E("Estás en una feria del libro y no sabes dónde pagar. Una persona de la feria está ocupada con otro cliente. ¿Qué haces: a) esperas un momento y luego dices «Disculpe, ¿dónde puedo pagar?» b) la interrumpes gritando?", "a", "Espera su turno y pregunta con cortesía.")],
    [
        E("¿Cómo se llama una pregunta que se responde con sí o no?", "Pregunta cerrada", "No pide más detalle."),
        E("¿Se debe agradecer una respuesta? Responde sí o no.", "Sí", "Reconoce la ayuda recibida."),
        E("¿Pedir aclaración es una falta de respeto? Responde sí o no.", "No", "Hacerlo con cortesía ayuda a comprender."),
    ],
    ("Escribe tres preguntas corteses para estas situaciones: 1) quieres saber el horario de la biblioteca escolar; 2) no entendiste una parte de las instrucciones de una tarea; 3) buscas la sala de música y no sabes dónde está. Identifica cuáles son abiertas y cuáles cerradas, y escribe cómo agradecerías.",
     "1) «Disculpe, ¿a qué hora cierra la biblioteca?» (abierta). Gracias: «Muchas gracias».",
     ["usa una fórmula cortés en cada pregunta", "la pregunta es clara y completa", "clasifica bien abiertas y cerradas", "incluye un agradecimiento"], ["tres preguntas con clasificación"], ["preguntas de una palabra", "no agradecer"],
     "Si la pregunta es solo una palabra, agrégale «disculpe» y un verbo."),
    "Escribe una pregunta abierta y una cerrada sobre el tema de las vacaciones.",
    "Observa cómo preguntan los adultos en una tienda y anota una pregunta cortés.",
)

# ================================================================ OA 28 · clase 4
reg(
    OA28, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar con situaciones reales.",
    "Aprenderé a expresar mis opiniones, sentimientos e ideas con respeto, usando mensajes que hablan de mí y no acusan a otros. Sirve para resolver malos ratos sin pelear.",
    ["Sé que existen emociones y puedo nombrarlas.", "Sé que mi opinión necesita una razón."],
    [
        "Expresar una opinión es decir lo que piensas sobre algo y por qué: «Creo que el patio debe tener más basureros porque hay papeles en el suelo». Expresar un sentimiento es decir cómo te sientes: «Me siento frustrado porque se perdió mi trabajo». Expresar una idea es proponer algo: «Mi idea es dividir el trabajo en tres partes». En las tres, la cortesía consiste en hablar con claridad y sin ofender.",
        "Un recurso muy útil es el mensaje en primera persona: «Me siento… cuando… porque…». Compara «Siempre me interrumpes, eres pesado» con «Me siento molesto cuando me interrumpen, porque pierdo la idea». El primero acusa y pone a la otra persona a la defensiva. El segundo habla de lo que tú sientes y por qué, y permite dialogar.",
        "También conviene nombrar con precisión la emoción: no es lo mismo estar molesto, avergonzado, preocupado u orgulloso. Y para opinar, se usan expresiones como «creo que», «en mi opinión» o «me parece que». Así se muestra que es una postura personal y no una verdad absoluta, lo que facilita el respeto mutuo.",
    ],
    [("opinión", "lo que piensas sobre algo, con una razón"), ("sentimiento", "emoción que experimentas, como alegría o frustración"), ("mensaje en primera persona", "frase que habla de lo que yo siento y por qué"), ("acusar", "culpar a otro con palabras duras"), ("defensiva", "actitud de protegerse ante un ataque")],
    [
        ("Reformular un reclamo", "Quieres decir que te molesta que te quiten el lugar en la fila. Reformula «Siempre me quitas el lugar, eres un abusador» con «me siento… cuando… porque…».", ["Nombro mi emoción.", "Describo lo que ocurre sin acusar.", "Doy la razón."], "«Me siento molesto cuando me quitan el lugar en la fila, porque llegué primero»."),
        ("Distinguir tipos de frase", "Clasifica: «Creo que el recreo es muy corto, porque casi no alcanzamos a jugar». ¿Es opinión, sentimiento o idea?", ["Veo «creo que» y una razón.", "Dice lo que piensa sobre algo.", "No nombra una emoción ni propone una acción."], "Opinión."),
    ],
    [("Acusar con «siempre» y «nunca».", "Se piensa que exagerar da más fuerza.", "Describe un hecho concreto: «hoy me interrumpieron»."), ("Decir «estoy mal» sin nombrar la emoción.", "Se cree que basta una palabra general.", "Usa una palabra precisa: «preocupado», «avergonzado»…")],
    [
        E("«Me siento molesto cuando me interrumpen, porque pierdo la idea.» ¿Es un mensaje que acusa o que habla de lo que uno siente?", "Habla de lo que uno siente", "Está en primera persona y explica la razón."),
        E("¿Cuál frase acusa: a) «Eres pesado.» b) «Me siento incómodo cuando gritas.»", "a", "Culpa a la persona en lugar de hablar de lo que yo siento."),
        E("En «Creo que el recreo es muy corto porque casi no alcanzamos a jugar», ¿qué expresa quien habla: una opinión o un sentimiento?", "Una opinión", "Dice lo que piensa y da una razón."),
    ],
    [
        E("Quieres decir que estás preocupado porque no terminaste el trabajo. ¿Cuál es mejor: a) «Estoy preocupado porque no terminé el trabajo y entrego mañana.» b) «Estoy mal.»", "a", "Nombra la emoción y la razón."),
        E("«Mi idea es dividir el trabajo en tres partes iguales.» ¿Es una opinión, un sentimiento o una idea?", "Una idea", "Propone una acción."),
        E("¿Qué expresión deja claro que es una opinión personal: a) «En mi opinión…» b) «Todos saben que…»", "a", "Muestra que es tu postura y no una verdad absoluta."),
    ],
    [
        E("Reformula «Nunca me escuchas» como mensaje en primera persona: a) «Me siento ignorado cuando no me miran mientras hablo, porque creo que no importa lo que digo.» b) «Eres un sordo.»", "a", "Habla de lo que siento y da una razón."),
        E("Ordena un mensaje en primera persona: a) «porque pierdo la idea» b) «Me siento molesto» c) «cuando me interrumpen». Escribe las letras.", "b, c, a", "Se parte por la emoción, luego el hecho y al final la razón."),
        E("Un compañero dice: «Todos piensan que tu trabajo es malo». ¿Cuál es el problema: generaliza sin evidencia o es una pregunta?", "Generaliza sin evidencia", "Usa «todos» sin mostrar datos y puede herir."),
    ],
    [
        E("Un estudiante dice: «Si me enojo, tengo derecho a decir lo que quiera». ¿Es una buena norma de cortesía? Responde sí o no.", "No", "Se puede expresar el enojo sin ofender."),
        E("¿Qué es mejor: «Me avergüenza cuando se ríen de mi error» o «Son unos burlones»? Responde con la primera o la segunda.", "La primera", "Habla de lo que siento sin atacar."),
    ],
    [
        E("Quieres explicar que sientes orgullo por tu trabajo en equipo. ¿Qué frase sirve: a) «Me siento orgulloso porque todos aportamos.» b) «Soy el mejor.»", "a", "Nombra la emoción y la razón sin menospreciar a otros."),
        E("Tu compañero llegó tarde tres veces. ¿Qué mensaje respeta más: a) «Me preocupa que llegues tarde, porque se retrasa el trabajo del grupo.» b) «Eres un irresponsable.»", "a", "Habla del hecho y de cómo afecta, sin ofender."),
    ],
    [E("Un amigo se burló de tu dibujo frente a otros. Quieres decírselo sin pelear. ¿Qué dices: a) «Me siento triste cuando se ríen de mi dibujo, porque me esforcé mucho.» b) «Eres cruel.»", "a", "Expresa tu sentimiento con razón y sin acusar.")],
    [
        E("«Me siento orgulloso porque todos aportamos» expresa... ¿un sentimiento o una idea?", "Un sentimiento", "Nombra una emoción, el orgullo, y su razón."),
        E("¿«Me siento… cuando… porque…» es un mensaje que acusa? Responde sí o no.", "No", "Habla de uno mismo y da razones."),
        E("¿Conviene nombrar con precisión una emoción? Responde sí o no.", "Sí", "Ayuda a que el otro comprenda."),
    ],
    ("Lee estas tres situaciones y escribe un mensaje en primera persona para cada una con la estructura «Me siento… cuando… porque…»: 1) un compañero se llevó tu lápiz sin pedirlo; 2) te dieron una buena nota por un trabajo en grupo que hiciste con esfuerzo; 3) un amigo se rió cuando te equivocaste al leer en voz alta. Luego, di cuál expresa una emoción positiva y cuáles una molestia.",
     "1) Me siento molesto cuando se llevan mi lápiz sin pedirlo, porque lo necesito.",
     ["usa la estructura en primera persona", "nombra la emoción con una palabra precisa", "no acusa ni ofende", "identifica cuál es positiva"], ["tres mensajes escritos"], ["acusar con «siempre» o «nunca»", "usar palabras generales como «mal»"],
     "Si tu mensaje empieza con «Tú…», cámbialo por «Me siento…»."),
    "Escribe una opinión con «creo que» y una idea con «mi idea es» sobre el uso de la biblioteca del curso.",
    "Piensa en una discusión reciente y reformúlala con un mensaje en primera persona.",
)

# ================================================================ OA 28 · clase 5
reg(
    OA28, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar las situaciones.",
    "Aprenderé a usar las fórmulas de cortesía (por favor, gracias, perdón, permiso y otras como «disculpe» y «de nada») en distintas situaciones de la vida diaria. Sirve para convivir con respeto en el transporte, la tienda, la biblioteca o la casa.",
    ["Sé saludar, presentarme y preguntar con cortesía.", "Sé qué significan «por favor», «gracias», «perdón» y «permiso»."],
    [
        "Las fórmulas de cortesía son expresiones que usamos para tratar con respeto. «Por favor» suaviza un pedido. «Gracias» reconoce lo que otro hizo. «Perdón» se usa para asumir un error. «Permiso» pide paso o autorización. «Disculpe» sirve para llamar la atención con respeto o para pedir excusas por una molestia pequeña. «De nada» o «con gusto» es la respuesta a un agradecimiento. «Con su permiso» es la forma formal de pedir permiso.",
        "Cada situación pide una fórmula distinta. En un bus, para bajar, se dice «permiso» o «disculpe, voy a bajar». Si alguien te cede el asiento, «gracias». Si pisas a alguien, «perdón». En una tienda, «por favor» al pedir y «gracias» al recibir. Cuando alguien te agradece, respondes «de nada». Y cuando te ofrecen algo que no quieres, una respuesta cortés es «no, gracias».",
        "Pedir permiso a un adulto para usar algo ajeno requiere pedir antes y esperar la respuesta: «¿Puedo usar su computador, por favor?». Si la respuesta es no, aceptas con calma. Usar las fórmulas no es un truco: es una manera de decir, con pocas palabras, que la otra persona nos importa.",
    ],
    [("por favor", "fórmula que suaviza un pedido"), ("gracias", "fórmula que reconoce lo que otro hizo por nosotros"), ("perdón", "fórmula para asumir un error o molestia"), ("permiso", "fórmula para pedir paso o autorización"), ("de nada", "respuesta cortés a un agradecimiento")],
    [
        ("Elegir la fórmula", "Quieres bajar de un bus lleno y hay gente de pie en el pasillo. ¿Qué dices?", ["La situación: pasar entre personas.", "Fórmula: permiso o disculpe.", "Lo digo con voz clara."], "«Permiso, voy a bajar»."),
        ("Responder a un agradecimiento", "Le entregas un lápiz a una compañera que dice «gracias». ¿Qué respondes?", ["Es un agradecimiento.", "La respuesta cortés es «de nada».", "También sirve «con gusto»."], "«De nada»."),
    ],
    [("Usar «perdón» para pedir paso.", "Se mezclan las fórmulas.", "Usa «permiso» para pasar y «perdón» para asumir un error."), ("No contestar a un «gracias».", "Se cree que no hace falta.", "Responde «de nada» o «con gusto».")],
    [
        E("Alguien te cede el asiento en el bus. ¿Qué dices: gracias o perdón?", "Gracias", "Reconoces el gesto."),
        E("Pisas por error a un compañero. ¿Qué dices: perdón o permiso?", "Perdón", "Asumes el error."),
        E("Quieres pasar entre dos personas que conversan en un pasillo. ¿Qué dices: permiso o gracias?", "Permiso", "Pides paso o autorización."),
    ],
    [
        E("Un compañero dice «gracias» después de que le ayudas a levantar sus cuadernos. ¿Qué respuesta es cortés: a) «De nada.» b) «Ya.»", "a", "Responde al agradecimiento."),
        E("Te ofrecen una galleta y no quieres. ¿Qué respuesta es más cortés: a) «No, gracias.» b) «No quiero.»", "a", "Rechaza con agradecimiento."),
        E("Para usar el computador de una amiga, ¿qué dices: a) «¿Puedo usar tu computador, por favor?» b) «Dame el computador.»", "a", "Pide permiso y usa «por favor»."),
    ],
    [
        E("Ordena en una tienda: a) «Gracias.» b) «Quisiera un cuaderno de cien hojas, por favor.» c) La vendedora entrega el cuaderno. Escribe las letras.", "b, c, a", "Se pide, se recibe y se agradece."),
        E("¿Qué fórmula formal usarías para pedir paso a un adulto desconocido: a) «Con su permiso» b) «Oye, sal»", "a", "Es la forma formal de pedir permiso."),
        E("Interrumpes sin querer una explicación. ¿Qué dices al darte cuenta: a) «Disculpe, no quise interrumpir.» b) «Nada.»", "a", "Reconoces la molestia."),
    ],
    [
        E("Un estudiante dice: «Decir «gracias» sin sentirlo es igual de cortés». ¿Es correcto? Responde sí o no.", "No", "La cortesía necesita actitud sincera además de la palabra."),
        E("En el bus nadie te cede el asiento, pero tú le cedes el tuyo a un adulto mayor y te dice «gracias». ¿Qué fórmula respondes? Elige: de nada o perdón.", "De nada", "Responde al agradecimiento."),
    ],
    [
        E("Te cae el cuaderno de otra persona. Se lo devuelves y dices: a) «Perdón, se me cayó; aquí lo tienes.» b) «Toma.» ¿Cuál es mejor?", "a", "Asumes el error y entregas con cortesía."),
        E("Dos fórmulas de cortesía en una frase: a) «Disculpe, ¿me puede ayudar, por favor?» b) «¿Me ayudas?» ¿Cuál tiene dos?", "a", "Lleva «disculpe» y «por favor»."),
    ],
    [E("En la biblioteca de tu escuela quieres sacar un libro que otra persona está mirando. ¿Qué dices: a) «Disculpe, cuando termine de mirarlo, ¿me lo prestaría, por favor?» b) «Dame ese libro ahora.»", "a", "Usa cortesía y espera su turno.")],
    [
        E("¿Cuál es la respuesta cortés a «gracias»?", "De nada", "Cierra el intercambio con amabilidad."),
        E("¿«Permiso» sirve para pedir paso? Responde sí o no.", "Sí", "Es su función principal."),
        E("¿Se usa «perdón» para asumir un error? Responde sí o no.", "Sí", "Reconoces la molestia causada."),
    ],
    ("Lee estas cuatro situaciones y escribe qué dirías en cada una con una fórmula distinta: 1) quieres que alguien te preste una goma; 2) alguien te la presta; 3) la botella se te cae y moja el cuaderno de una compañera; 4) quieres entrar a una sala donde hay una reunión de adultos. Anota también cómo responderías si te dicen «gracias».",
     "1) «¿Me prestas una goma, por favor?» 2) «Gracias». 3) «Perdón, fue sin querer». 4) «Con su permiso».",
     ["usa una fórmula distinta por situación", "las fórmulas corresponden a la situación", "incluye la respuesta a un «gracias»"], ["cinco frases escritas"], ["repetir siempre la misma fórmula", "usar «perdón» para pedir algo"],
     "Revisa si la fórmula calza con lo que quieres lograr: ¿pedir, agradecer, disculparte o pasar?"),
    "Escribe otras tres situaciones en que usarías «disculpe», «no, gracias» y «de nada».",
    "Observa cuántas veces, en un día, oyes «gracias» y «de nada» en tu casa y escuela.",
)

# ================================================================ OA 28 · clase 6
reg(
    OA28, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los mensajes en voz alta.",
    "Aprenderé a revisar un mensaje o un diálogo y adaptarlo a quien lo leerá: más cercano o más formal. Sirve para comunicarme bien con amigos, profesores y adultos en cualquier situación.",
    ["Sé saludar, preguntar y usar fórmulas de cortesía.", "Sé que hay tratos formal y cercano."],
    [
        "El registro es la forma de hablar que usamos según la situación. El registro cercano o informal sirve con amigos y familia: usa «tú», frases cortas, palabras de uso diario y a veces expresiones propias del grupo. El registro formal sirve con personas de respeto o en situaciones oficiales: usa «usted», frases completas, vocabulario cuidado y fórmulas de cortesía. Cambiar de registro no es ser falso: es adaptarse a quién nos escucha.",
        "Para escribir un mensaje formal, como una nota a un director, hay una estructura sencilla: saludo («Estimada profesora:»), motivo del mensaje, petición o información, agradecimiento y despedida con tu nombre («Saludos cordiales, Camila»). Se evitan los apodos, las abreviaturas como «profe» y las palabras como «chao» o «ya po».",
        "Revisar un mensaje para su audiencia significa preguntarse: ¿quién lo leerá?, ¿qué tratamiento le corresponde?, ¿están las fórmulas de cortesía?, ¿se entiende lo que pido? Si un mensaje informal se manda a una autoridad, se corrige con un registro más formal; si uno formal se manda a un amigo cercano, puede suavizarse. Lo importante es que el mensaje sea adecuado a la situación.",
    ],
    [("registro", "forma de hablar o escribir según la situación"), ("formal", "cuidado y respetuoso, con «usted»"), ("informal", "cercano y de uso diario, con «tú»"), ("estimado/a", "palabra con que se inicia un mensaje formal"), ("cordial", "amable y respetuoso")],
    [
        ("Corregir un mensaje", "Mensaje a una profesora: «Profe, mañana no voy porque tengo dentista. Chao.» Reescríbelo en registro formal.", ["Quito «profe» y «chao».", "Agrego saludo, motivo, agradecimiento y despedida.", "Uso «usted»."], "«Estimada profesora: mañana no podré asistir a clases porque tengo cita con el dentista. Le agradezco su comprensión. Saludos cordiales, Camila.»"),
        ("Identificar el registro", "«Oye, ¿me prestai tu goma?» ¿Qué registro es?", ["Veo «oye» y «prestai».", "Es lenguaje cercano y coloquial.", "Es informal."], "Informal."),
    ],
    [("Mandar un mensaje informal a una autoridad.", "Se piensa que da lo mismo.", "Reescribe con saludo, «usted» y despedida formal."), ("Usar abreviaturas o apodos con adultos que no conoces.", "Se confunde confianza con cortesía.", "Usa el título completo: «profesora», «señor».")],
    [
        E("«Estimado director:» es el comienzo de un mensaje, ¿formal o informal?", "Formal", "Es un saludo respetuoso para una autoridad."),
        E("«Oye, ¿me prestai la goma?» ¿Con quién es adecuado: con un amigo cercano o con la directora?", "Con un amigo cercano", "Es lenguaje cercano y coloquial."),
        E("Para despedir un mensaje formal, ¿sirve «Saludos cordiales» o «chao po»?", "Saludos cordiales", "Es una despedida respetuosa."),
    ],
    [
        E("¿Qué palabra de este mensaje es informal para una profesora: «Profe, mañana llego tarde»?", "Profe", "Es un apodo; lo formal es «profesora»."),
        E("Elige el mensaje formal: a) «Estimada señora Ana: Le escribo para solicitar una hora de atención. Muchas gracias.» b) «Oye, ¿tienes tiempo?»", "a", "Tiene saludo formal, motivo y agradecimiento."),
        E("Mensaje a un amigo cercano. ¿Es adecuado «Estimado amigo, le informo que mañana no podré reunirme»? Responde sí o no.", "No", "Es demasiado formal para un amigo cercano; sonaría extraño."),
    ],
    [
        E("Ordena un mensaje formal: a) «Le agradezco su atención.» b) «Estimado señor Soto:» c) «Mañana no podré asistir al taller porque tengo un control médico.» d) «Saludos cordiales, Daniela.» Escribe las letras.", "b, c, a, d", "Saludo, motivo, agradecimiento y despedida."),
        E("Reescribe en trato formal: «Tú me dijiste que podía faltar». ¿Cuál es la forma correcta para una profesora: a) «Usted me dijo que podía faltar.» b) «Tú me dijiste que podía faltar.»", "a", "Usa «usted» y el verbo en tercera persona."),
        E("Un mensaje dice: «Profe, necesito la hoja, chao». ¿Cuáles son las dos palabras informales que debes cambiar?", "Profe y chao", "Son un apodo y una despedida informal."),
    ],
    [
        E("Un estudiante dice: «Usar registro formal es ser falso». ¿Es correcto? Responde sí o no.", "No", "Adaptar el registro es respetar a quien nos lee."),
        E("Escribes a un amigo cercano que tienes que cambiar la hora de la reunión. ¿Cuál mensaje es más adecuado: a) «Hola, Vicente: ¿podemos cambiar la reunión a las cinco? Gracias.» b) «Estimado señor Vicente: Le comunico oficialmente que…»", "a", "Es claro, cortés y con trato cercano."),
    ],
    [
        E("Mensaje a la directora: «Hola, quiero que me des permiso para ir al baño». Escribe la versión formal más adecuada: a) «Buenos días, directora. ¿Me da permiso para ir al baño, por favor?» b) «Permiso, ya vuelvo.»", "a", "Tiene saludo formal, usted y fórmula de cortesía."),
        E("Revisa: «Estimada profesora: Necesito que me envíes la guía». ¿Cuál es el error: usa «envíes» (tú) en lugar de «envíe» (usted)? Responde sí o no.", "Sí", "En registro formal debe usar la forma de usted."),
    ],
    [E("Debes pedir al director permiso para usar la cancha el viernes. ¿Cuál mensaje es más adecuado: a) «Estimado director: Le escribo para solicitar permiso para usar la cancha el viernes. Agradezco su respuesta. Saludos cordiales, Elena.» b) «Director, necesito la cancha el viernes.»", "a", "Es formal, completo y con cortesía.")],
    [
        E("¿Cómo se llama la forma de hablar según la situación?", "Registro", "Puede ser formal o informal."),
        E("¿Un mensaje formal incluye saludo, motivo, agradecimiento y despedida? Responde sí o no.", "Sí", "Esa es su estructura básica."),
        E("¿Con un amigo cercano es necesario usar «usted»? Responde sí o no.", "No", "Con amigos se usa el trato cercano."),
    ],
    ("Reescribe en registro formal este mensaje para una profesora: «Profe, no pude hacer la tarea porque se me enfermó el compu. ¿Me das más plazo? Chao». Debe tener saludo, motivo, petición con «usted», agradecimiento y despedida con tu nombre. Luego escribe cómo se lo dirías a un amigo cercano, de forma informal pero respetuosa.",
     "Estimada profesora: No pude terminar la tarea porque falló mi computador. ¿Podría darme un plazo hasta el jueves? Le agradezco su comprensión. Saludos cordiales, Martín.",
     ["tiene los cinco elementos del mensaje formal", "usa «usted» de manera consistente", "la versión informal es adecuada y respetuosa"], ["dos mensajes escritos"], ["dejar «profe» o «chao»", "mezclar tú y usted"],
     "Revisa de arriba abajo: ¿saludo?, ¿motivo?, ¿petición con «usted»?, ¿agradecimiento?, ¿despedida y nombre?"),
    "Reescribe en forma cercana este mensaje formal: «Estimado Joaquín: Le comunico que la reunión se realizará a las 16:00».",
    "Elige un mensaje que hayas escrito y revisa si el registro era adecuado para quien lo recibió.",
)

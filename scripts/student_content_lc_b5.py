"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR01 (textos orales de tradición indígena, contexto de rescate y revitalización de la lengua).

Los textos de práctica están en castellano; el saludo «mari mari» (mapuzugun) aparece solo como
saludo. En contextos de revitalización puede haber pocos hablantes: las palabras y los textos
tradicionales los comparten el educador/a tradicional, los mayores o la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA = "LC01 OA LR01"

VIENTO = "Sopla, sopla, viento tibio, / sopla, sopla, mueve el trigo. / Calla, calla, viento fuerte, / calla, calla, duerme el trigo."
SALUDO = "Mari mari, buenos días; / mari mari, ya llegué; / sopla el viento en la mañana, / y yo canto como sé."
ADIV_LUNA = "Salgo de noche, no tengo velas y alumbro el camino; a veces estoy entera y a veces soy un gajo."
CONTAR = "Uno, dos, sopla el sol; tres, cuatro, vuela el pato; cinco, seis, salta el pez."
TRABA2 = "Seis sillas sin silla sirven si se sientan seis."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA, 1,
    materials="Este cuaderno y lápiz. Los textos de práctica están escritos en castellano. Los textos de la lengua los comparte el educador/a tradicional o un mayor de la comunidad.",
    use="Aprenderé a escuchar un texto completo, aunque tenga palabras que aún no conozco, y a disfrutar de su ritmo y de la voz de quien lo comparte. Sirve para acercarme a una lengua que se está recuperando.",
    prior=["Sé escuchar en silencio.", "Sé que hay lenguas que se están volviendo a aprender."],
    explain=[
        "Una lengua en revitalización es una lengua que una comunidad está volviendo a aprender y a usar. A veces hay pocos hablantes y los mayores guardan canciones, adivinanzas y poemas. Escucharlos con atención es una forma de cuidar la lengua.",
        "Al escuchar un texto breve fíjate en tres cosas. El ritmo, que es cómo suena: lento, rápido o con pausas. La voz, que es quién habla y cómo. La situación, que es cuándo y para qué se dice. Puedes disfrutar un texto aunque no entiendas todas sus palabras.",
        "No hace falta adivinar lo que no entiendes. Lo escuchas completo, lo disfrutas y después preguntas. Quien comparte el texto es su guardián: no lo cambies, no lo mezcles con otros y no lo grabes sin permiso.",
    ],
    vocab=[("revitalización", "volver a dar vida y uso a una lengua"), ("hablante", "persona que habla una lengua"), ("mayor", "persona de más edad que guarda saberes"), ("ritmo", "cómo suena un texto, con sus pausas"), ("guardián del texto", "persona que cuida y comparte un texto")],
    worked=[
        {"title": "Escuchar y disfrutar", "problem": f"Un mayor dice despacio el texto de práctica «{SALUDO}». Hay una palabra que no conoces. ¿Qué haces?", "steps": ["Escucho hasta el final.", "Disfruto el ritmo y la voz.", "Después pregunto por la palabra que no conozco."], "answer": "Escucho completo, disfruto y pregunto después"},
        {"title": "Ritmo de un texto", "problem": f"Un adulto dice: «{VIENTO}» muy despacio y bajito, como si el viento se durmiera. ¿Cómo es el ritmo?", "steps": ["Se dice despacio.", "Hay pausas entre versos.", "El ritmo es lento."], "answer": "Lento y con pausas"},
    ],
    mistakes=[
        {"wrong": "Adivinar lo que significa una palabra que no conoces.", "why": "Puedes cambiar el sentido del texto.", "fix": "Escucha entero y pregunta a quien lo comparte."},
        {"wrong": "Grabar la voz del mayor sin avisar.", "why": "La voz y el texto son de la persona y su comunidad.", "fix": "Pide permiso antes de registrar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es una lengua en revitalización?", "Una lengua que una comunidad vuelve a aprender y a usar", "La comunidad la está recuperando."),
            ex("Un mayor comparte un texto. ¿Escuchas completo o lo interrumpes con tu opinión?", "Escucho completo", "Se respeta a quien comparte."),
            ex("Si no entiendes una palabra del texto, ¿qué haces al final?", "Pregunto", "Se pregunta a quien lo comparte."),
        ],
        "understand": [
            ex("¿Por qué escuchar a los mayores ayuda a cuidar una lengua?", "Porque ellos guardan textos y saberes", "Los mayores conservan la lengua."),
            ex("¿Se puede disfrutar un texto sin entender todas sus palabras?", "Sí", "El ritmo y la voz se pueden disfrutar."),
            ex("¿Qué es el ritmo de un texto?", "Cómo suena, con sus pausas", "Es el compás de lo que se dice."),
        ],
        "apply": [
            ex(f"En el texto de práctica «{VIENTO}», ¿cuántas veces suena la palabra «sopla»?", "4", "Dos veces en el primer verso y dos en el segundo."),
            ex(f"En «{VIENTO}», ¿cuántas veces suena la palabra «trigo»?", "2", "Aparece al final del segundo y del cuarto verso."),
            ex(f"En el texto de práctica «{SALUDO}», ¿cuántas veces suena «mari mari»?", "2", "Abre el primer y el segundo verso."),
        ],
        "reason": [
            ex("Un niño escucha un texto del mayor y empieza a corregirle las palabras. ¿Por qué no está bien?", "Porque el mayor es quien guarda el texto", "El mayor conoce cómo se dice."),
            ex("Una niña dice que no necesita escuchar entero porque ya entendió el comienzo. ¿Es cierto?", "No", "El final también aporta."),
        ],
        "challenge": [
            ex(f"En «{CONTAR}», ¿cuántos números se nombran? Cuéntalos: uno, dos, tres…", "6", "Se nombran del uno al seis."),
            ex("Escribe una frase de dos partes: lo que disfrutaste del texto y lo que preguntarías.", "Cualquier frase con ambas partes", "Debe nombrar goce y pregunta."),
        ],
    },
    context=[ex("Un mayor de la comunidad canta una canción en la lengua. Dos niños se ríen porque no entienden. ¿Qué podrías hacer?", "Pedirles que escuchen con respeto", "No entender no justifica reírse.")],
    selfcheck=[
        ex("¿Quién guarda un texto tradicional?", "El mayor o la comunidad", "Ellos lo cuidan."),
        ex("¿Qué haces con una palabra que no entiendes?", "Pregunto al final", "No se adivina."),
        ex("¿Se graba sin permiso?", "No", "Se pide permiso."),
    ],
    open_task=task(
        "Pide a un adulto de tu casa que te diga el texto de práctica «" + SALUDO + "» o la adivinanza «" + ADIV_LUNA + "». Escucha completo, sin interrumpir, y anota con una palabra cómo fue el ritmo (lento, rápido) y cómo fue la voz (suave, fuerte). Después pregunta al educador/a tradicional, a un mayor o a la comunidad: ¿qué texto de nuestra lengua puedo escuchar y quién me lo puede compartir?",
        "Escuché la adivinanza de la luna. El ritmo fue lento y la voz suave. Mi pregunta: ¿qué texto de nuestra lengua puedo escuchar y quién me lo puede compartir?",
        ["escucha completo", "describe ritmo y voz", "pregunta al educador/a tradicional"],
        ["dos palabras anotadas", "pregunta escrita"],
        ["interrumpir", "adivinar palabras"],
        "Valora la escucha completa y la pregunta a quien guarda los textos.",
    ),
    reinforce="Escucha una canción de tu casa completa y di cómo es su ritmo.",
    extend="Anota tres cosas que disfrutaste de un texto que escuchaste.",
)

register(
    OA, 2,
    materials="Este cuaderno y lápiz. Los textos de práctica están en castellano.",
    use="Aprenderé a reconocer las repeticiones y a participar en el tramo que me corresponde, aunque la lengua esté aprendiéndose. Sirve para cantar o decir juntos con respeto.",
    prior=["Sé escuchar un texto completo.", "Sé esperar mi turno."],
    explain=[
        "En muchos textos orales hay partes que se repiten: un verso, una palabra o un sonido. La repetición ayuda a aprender y a participar. Cuando una lengua se está recuperando, repetir con el grupo es una forma de practicarla.",
        "Participar en un tramo verificado quiere decir que ese tramo fue confirmado por el educador o la comunidad. Solo repites lo que ellos validaron. Si no sabes cuál es tu tramo, esperas y preguntas.",
        "Hay tramos para toda la clase y tramos que solo dice la guía o una persona mayor. Respetar esa diferencia también es parte de cuidar el texto y a quien lo comparte.",
    ],
    vocab=[("repetición", "parte que vuelve igual"), ("tramo verificado", "parte confirmada por la comunidad"), ("guía", "persona que dirige"), ("coro", "grupo que dice un tramo juntos"), ("turno", "momento de participar")],
    worked=[
        {"title": "Encontrar el tramo del coro", "problem": f"En «{SALUDO}» la guía dice los dos primeros versos y el coro repite «mari mari». ¿Cuántas veces dice el coro «mari mari»?", "steps": ["«Mari mari» aparece en los versos uno y dos.", "Si el coro lo repite una vez por verso, son dos.", "Son 2 veces."], "answer": "2 veces"},
        {"title": "Tramo que no me toca", "problem": "La educadora canta una parte sola y te mira. No te dijo que cantes. ¿Qué haces?", "steps": ["No sé si es mi tramo.", "Espero.", "Pregunto después cuál tramo puedo cantar."], "answer": "Espero y pregunto cuál es mi tramo"},
    ],
    mistakes=[
        {"wrong": "Cantar un tramo que solo corresponde a la guía.", "why": "Se mezclan las voces.", "fix": "Pregunta cuál tramo es del coro."},
        {"wrong": "Cambiar palabras del tramo repetido.", "why": "El tramo verificado se dice igual.", "fix": "Repite exacto lo que se verificó."},
    ],
    tiers={
        "recovery": [
            ex(f"En «{VIENTO}», ¿qué palabra se repite dos veces seguidas en el primer verso?", "sopla", "Dice «sopla, sopla»."),
            ex("¿Qué es el coro?", "El grupo que dice un tramo juntos", "Es quien responde en grupo."),
            ex("¿Quién confirma qué tramo puedes cantar?", "El educador/a tradicional o la comunidad", "Ellos lo verificaron."),
        ],
        "understand": [
            ex("¿Por qué ayudan las repeticiones a aprender una lengua?", "Porque se practica lo mismo varias veces", "Repetir fija lo aprendido."),
            ex("¿Qué es un tramo verificado?", "Una parte confirmada por la comunidad", "Alguien que sabe la validó."),
            ex("¿Puedes decir todos los tramos de un canto tradicional?", "No siempre", "Hay tramos para la guía o personas mayores."),
        ],
        "apply": [
            ex(f"En «{VIENTO}», ¿cuántas veces suena «calla»?", "4", "Dos veces en el tercer verso y dos en el cuarto."),
            ex(f"En «{CONTAR}», ¿cuántas veces suena la palabra «sopla»?", "1", "Solo aparece en el primer tramo."),
            ex("La guía dice «¡Ola!» y el coro responde «¡Ola!». Si la guía lo dice 5 veces, ¿cuántas veces responde el coro?", "5", "Responde una vez por cada «¡Ola!»."),
        ],
        "reason": [
            ex("Un niño cambia una palabra del tramo repetido porque le suena mejor. ¿Qué pasa con el texto?", "Ya no es el texto verificado", "Cambia lo que la comunidad confirmó."),
            ex("Una niña espera su turno y canta cuando el coro entra. ¿Hizo bien?", "Sí", "Respetó los turnos."),
        ],
        "challenge": [
            ex(f"En «{VIENTO}», cuenta cuántas palabras tiene el primer verso: «Sopla, sopla, viento tibio».", "4", "Son sopla, sopla, viento y tibio."),
            ex("Escribe un verso de dos palabras repetidas, por ejemplo «sopla, sopla». Invéntalo distinto.", "Cualquier palabra repetida dos veces", "Debe repetirse la palabra."),
        ],
    },
    context=[ex("En la clase, el mayor canta y el coro repite. Rosa canta también la parte del mayor. ¿Qué le dirías?", "Que espere su tramo", "Cada voz tiene su turno.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es una repetición?", "Una parte que vuelve igual", "Es lo que se dice otra vez."),
        ex("¿Quién valida el tramo?", "La comunidad", "Ella confirma lo correcto."),
        ex("¿Cambias palabras de un tramo?", "No", "Se dice igual."),
    ],
    open_task=task(
        "Con un adulto, juega el texto de práctica «" + CONTAR + "»: él lee cada tramo y tú repites solo los números. Anota cuántos números dijiste. Luego subraya la parte que se repite en «" + VIENTO + "». Pregunta al educador/a tradicional o a la comunidad: ¿qué tramo de nuestros cantos puedo decir con el grupo y cuál es de la guía?",
        "Repetí los números uno al seis: dije seis números. Subrayé «sopla, sopla». Mi pregunta: ¿qué tramo de los cantos puedo decir con el grupo?",
        ["identifica repeticiones", "espera su turno", "pregunta al educador/a tradicional"],
        ["números anotados", "subrayado", "pregunta escrita"],
        ["cantar el tramo de la guía", "cambiar palabras"],
        "Reconoce la repetición y recuerda confirmar el tramo con la comunidad.",
    ),
    reinforce="Juega con un familiar a repetir una frase después de que él la diga.",
    extend="Inventa una rima de dos tramos, uno para la guía y otro para el coro.",
)

register(
    OA, 3,
    materials="Este cuaderno, lápiz y espacio para moverte. Los textos de práctica están en castellano.",
    use="Aprenderé a mostrar con el cuerpo y con gestos lo que entendí de un texto, aunque no conozca todas las palabras. Sirve para comprender y participar con respeto.",
    prior=["Sé escuchar un texto completo.", "Sé hacer gestos sencillos."],
    explain=[
        "Cuando una lengua se está aprendiendo, el cuerpo ayuda a comprender. Un gesto puede mostrar una idea: el viento se muestra moviendo los brazos suavemente; dormir, con las manos junto a la mejilla. No necesitas todas las palabras para entender la idea.",
        "Un gesto bien hecho es claro y respetuoso. No se hace en burla ni se exagera. Si el texto es tradicional, el educador o educadora te dice qué gestos acompañan el texto y cuáles no se cambian.",
        "Mostrar una idea con el cuerpo es una forma de decir «te entendí». Pero tu gesto no reemplaza el texto: sigues escuchando sus palabras y sus pausas.",
    ],
    vocab=[("gesto", "movimiento que muestra una idea"), ("idea", "lo principal que dice un texto"), ("exagerar", "hacer algo más grande de lo necesario"), ("respeto", "cuidado hacia otros"), ("acompañar", "ir junto con otra cosa")],
    worked=[
        {"title": "Gesto para «duerme»", "problem": f"En «{VIENTO}», el último verso dice «duerme el trigo». ¿Qué gesto muestra la idea?", "steps": ["La idea es dormir.", "Pongo las manos juntas junto a la mejilla.", "Cierro los ojos despacio."], "answer": "Manos junto a la mejilla"},
        {"title": "Gesto con burla", "problem": "Un niño imita con muecas la forma de hablar de un mayor para hacer reír. ¿Está bien?", "steps": ["Se burla de una persona.", "No muestra la idea del texto.", "Debe usar un gesto sencillo."], "answer": "No; es burla"},
    ],
    mistakes=[
        {"wrong": "Exagerar el gesto para hacer reír.", "why": "Hace burla del texto y de quien lo comparte.", "fix": "Haz un gesto claro y tranquilo."},
        {"wrong": "Cambiar un gesto que enseñó la comunidad.", "why": "Ese gesto acompaña el texto.", "fix": "Hazlo como te lo enseñaron."},
    ],
    tiers={
        "recovery": [
            ex(f"En «{VIENTO}», ¿qué gesto sirve para «sopla»: soplar suave o dar un salto?", "Soplar suave", "Sopla se muestra con aire."),
            ex("¿Qué gesto muestra «dormir»?", "Manos junto a la mejilla", "Es el gesto de descansar."),
            ex("¿Puedes comprender una idea con un gesto aunque no sepas todas las palabras?", "Sí", "El cuerpo ayuda a entender."),
        ],
        "understand": [
            ex("¿Por qué un gesto debe ser respetuoso?", "Porque no debe burlarse de nadie", "Muestra una idea, no una burla."),
            ex("¿Qué hace el educador/a con los gestos de un texto tradicional?", "Enseña cuáles se usan", "Él conoce el texto."),
            ex("¿El gesto reemplaza las palabras del texto?", "No", "Solo las acompaña."),
        ],
        "apply": [
            ex(f"En «{CONTAR}», ¿qué gesto harías para «vuela el pato»: mover los brazos como alas o quedarte quieto?", "Mover los brazos como alas", "El pato vuela."),
            ex(f"En «{CONTAR}», ¿qué gesto harías para «salta el pez»: un saltito o una vuelta larga?", "Un saltito", "El pez salta."),
            ex(f"En «{VIENTO}», el verso 3 pide «viento fuerte». ¿Mueves los brazos fuerte o suave?", "Fuerte", "El texto dice viento fuerte."),
        ],
        "reason": [
            ex("Un niño usa gestos de otro pueblo para el texto sin preguntar. ¿Qué puede pasar?", "Mostrar algo que no corresponde", "Cada pueblo tiene sus gestos."),
            ex("Una niña pregunta qué gesto usa la comunidad antes de mostrar la idea. ¿Hizo bien?", "Sí", "Preguntó antes de inventar."),
        ],
        "challenge": [
            ex(f"En «{CONTAR}», hay tres tramos. Si cada tramo lleva un gesto distinto, ¿cuántos gestos necesitas?", "3", "Uno por tramo."),
            ex("Escribe un gesto sencillo y respetuoso para «sale el sol».", "Por ejemplo, subir los brazos en arco", "Un arco de brazos muestra el sol."),
        ],
    },
    context=[ex("Durante un canto de la comunidad, Pedro hace gestos exagerados para que sus amigos se rían. ¿Qué podrías decirle?", "Que haga gestos tranquilos y respetuosos", "El canto merece respeto.")],
    selfcheck=[
        ex("¿Cómo es un buen gesto?", "Claro y respetuoso", "Muestra la idea."),
        ex("¿Quién enseña los gestos de un texto tradicional?", "El educador/a tradicional", "Él conoce el texto."),
        ex("¿Qué haces con las manos para mostrar que algo duerme?", "Las pongo junto a la mejilla", "Es el gesto de descansar."),
    ],
    open_task=task(
        "Elige uno de estos versos de práctica: «duerme el trigo», «vuela el pato» o «salta el pez». Inventa un gesto sencillo y respetuoso, muéstraselo a un adulto de tu casa y dibújalo. Escribe qué idea muestra. Pregunta al educador/a tradicional o a la comunidad: ¿qué gestos acompañan los textos de nuestra lengua y cuáles no debo cambiar?",
        "Elegí «salta el pez». Hice un saltito con las manos juntas. Mi pregunta: ¿qué gestos acompañan los textos de nuestra lengua?",
        ["gesto claro", "respetuoso", "pregunta al educador/a tradicional"],
        ["dibujo", "frase con la idea", "pregunta escrita"],
        ["burlarse", "inventar gestos tradicionales"],
        "Valora el gesto claro y recuerda preguntar a quien conoce el texto.",
    ),
    reinforce="Muestra con el cuerpo tres versos de una canción de tu casa.",
    extend="Haz una secuencia de tres gestos para los tres tramos de la rima de contar.",
)

register(
    OA, 4,
    materials="Este cuaderno y lápiz. Los textos de práctica están en castellano.",
    use="Aprenderé a relacionar un texto con mi experiencia y a volver al texto, sin apropiarme de lo que pertenece a la comunidad. Sirve para comprender y respetar.",
    prior=["Sé contar algo que me pasó.", "Sé qué dice el texto."],
    explain=[
        "Relacionar es unir lo que dice el texto con algo que te ha pasado. Si el texto habla de la luna, puedes recordar una noche en que miraste la luna. Eso te ayuda a comprender mejor.",
        "Después de contar tu experiencia, vuelve al texto y di qué verso o idea te hizo pensar en eso. Así el texto sigue siendo el centro y tu experiencia es un puente para entenderlo.",
        "Cuando una lengua se está recuperando, sus textos son muy valiosos. No digas que son tuyos ni los cambies. Di «este texto lo compartió…» y menciona a la persona o comunidad.",
    ],
    vocab=[("puente", "lo que une dos ideas"), ("experiencia", "algo que viví"), ("valioso", "que tiene mucho valor"), ("compartió", "dio a conocer a otros"), ("mencionar", "nombrar")],
    worked=[
        {"title": "Un puente con la luna", "problem": f"Escuchas «{ADIV_LUNA}». Recuerdas una noche en que miraste la luna llena. ¿Cómo lo dices?", "steps": ["Digo: «El texto habla de la luna».", "Cuento mi noche de luna llena.", "Vuelvo al verso: «a veces estoy entera»."], "answer": "Cuento mi noche y vuelvo al verso «a veces estoy entera»"},
        {"title": "No decir que es mío", "problem": "Una niña dice: «Esta canción la inventé yo» sobre un canto que compartió la comunidad. ¿Qué debe decir?", "steps": ["La canción es de la comunidad.", "Ella no la inventó.", "Debe decir que la compartió la comunidad."], "answer": "Que la compartió la comunidad"},
    ],
    mistakes=[
        {"wrong": "Hablar solo de mi experiencia y no volver al texto.", "why": "El texto queda olvidado.", "fix": "Después de contar, nombra un verso del texto."},
        {"wrong": "Decir que un canto de la comunidad es mío.", "why": "No lo inventé.", "fix": "Di quién lo compartió."},
    ],
    tiers={
        "recovery": [
            ex("Cuando terminas de contar lo que viviste, ¿a qué parte vuelves para seguir comprendiendo?", "Vuelvo al texto", "El texto es el centro."),
            ex(f"En «{ADIV_LUNA}», ¿de qué habla el texto?", "De la luna", "La respuesta es la luna."),
            ex("¿Puedes decir que un canto de la comunidad es tuyo?", "No", "No lo creaste."),
        ],
        "understand": [
            ex("¿Para qué sirve unir el texto con tu experiencia?", "Para comprender mejor", "Lo conocido ayuda a entender."),
            ex("¿Qué significa mencionar a quien compartió el texto?", "Decir su nombre o su comunidad", "Se reconoce su aporte."),
            ex("¿Por qué son valiosos los textos de una lengua que se recupera?", "Porque ayudan a que la lengua viva", "Mantienen la lengua."),
        ],
        "apply": [
            ex(f"Escribe una frase con «Me hace pensar en…» sobre el texto «{ADIV_LUNA}».", "Cualquier frase que empiece con «Me hace pensar en»", "Une el texto con una experiencia."),
            ex(f"En «{ADIV_LUNA}», ¿qué dice que hace la luna a veces: estar entera o ser un gajo? Escribe ambas.", "Estar entera y ser un gajo", "El texto dice ambas cosas."),
            ex("Ordena: a) vuelvo al texto, b) cuento mi experiencia, c) digo de qué habla el texto. Escribe las letras en orden.", "c, b, a", "Primero el texto, luego mi experiencia y vuelvo."),
        ],
        "reason": [
            ex("Un niño relaciona el texto con su vida, pero cambia sus palabras. ¿Qué debió hacer?", "Mantener las palabras del texto", "El texto no se cambia."),
            ex("Una niña dice «lo compartió un mayor de la comunidad» y luego cuenta su experiencia. ¿Hizo bien?", "Sí", "Nombró la fuente."),
        ],
        "challenge": [
            ex("Hay 3 niños que relacionan bien y 2 que se apropian. ¿Cuántos relacionan bien?", "3", "Son los que nombraron el texto y su fuente."),
            ex("Escribe una frase con tres partes: de qué habla el texto, tu experiencia y quién lo compartió.", "Cualquier frase con las tres partes", "Debe incluir las tres."),
        ],
    },
    context=[ex("Después de que la educadora tradicional compartió un canto, Emilia lo canta en su casa y dice que lo creó ella. ¿Qué debería decir?", "Que se lo compartió la educadora", "Se da crédito.")],
    selfcheck=[
        ex("¿A qué vuelves después de contar tu experiencia?", "Al texto", "El texto es el centro."),
        ex("¿Dices que el texto es tuyo?", "No", "Pertenece a la comunidad."),
        ex("¿Qué mencionas?", "A quien lo compartió", "Se da crédito."),
    ],
    open_task=task(
        "Un adulto te dice la adivinanza «" + ADIV_LUNA + "». Cuéntale una noche en que miraste el cielo. Luego escribe o dibuja: de qué habla el texto, tu experiencia y a quién se lo pedirías si fuera un texto de la comunidad. Pregunta al educador/a tradicional o a la comunidad: ¿cómo puedo contar una experiencia sobre un texto de nuestra lengua sin apropiármelo?",
        "El texto habla de la luna. Yo miré la luna desde mi ventana. Si fuera de la comunidad, diría quién lo compartió. Mi pregunta: ¿cómo cuento mi experiencia sin apropiarme del texto?",
        ["relaciona con experiencia", "vuelve al texto", "menciona la fuente"],
        ["dibujo o frase", "pregunta escrita"],
        ["apropiarse", "olvidar el texto"],
        "Valora el puente entre experiencia y texto y la mención de la fuente.",
    ),
    reinforce="Cuenta una experiencia que te recuerde una rima y luego di la rima.",
    extend="Escribe dos frases que relacionen la adivinanza con dos experiencias distintas.",
)

register(
    OA, 5,
    materials="Este cuaderno y lápiz. Un adulto lee dos veces los textos de práctica.",
    use="Aprenderé a escuchar otra vez un texto con un propósito: notar una palabra, un sonido o una imagen. Sirve para oír más detalles y aprender mejor.",
    prior=["Sé escuchar un texto completo.", "Sé contar palabras."],
    explain=[
        "La primera vez que escuchas, entiendes el conjunto. La segunda vez puedes buscar algo en particular: una palabra que se repite, un sonido que te gusta o una imagen que aparece en tu mente. Eso es escuchar con un propósito.",
        "En las lenguas que se están recuperando, volver a escuchar es muy valioso. Cada vez que escuchas, notas más cosas. Y puedes volver a escuchar las veces que el mayor o el educador lo permitan.",
        "Un propósito claro se puede comprobar. «Voy a contar cuántas veces suena una palabra» se puede verificar. Anota lo que encontraste y compara con un compañero.",
    ],
    vocab=[("propósito", "lo que busco al escuchar"), ("sonido", "lo que se oye"), ("imagen", "lo que veo en mi mente"), ("comprobar", "revisar si es cierto"), ("comparar", "mirar en qué se parecen y se diferencian")],
    worked=[
        {"title": "Contar una palabra", "problem": f"Segunda escucha de «{TRABA2}». Tu propósito: contar la palabra «seis». ¿Cuántas veces suena?", "steps": ["Hago una marca cada vez que oigo «seis».", "Suena en «Seis sillas».", "Suena otra vez al final: «sientan seis».", "Son 2."], "answer": "2 veces"},
        {"title": "Elegir una imagen", "problem": f"En «{VIENTO}», ¿qué imagen ves con «duerme el trigo»?", "steps": ["Pienso en un campo de trigo.", "El viento se calma.", "El trigo queda quieto."], "answer": "Un campo de trigo quieto"},
    ],
    mistakes=[
        {"wrong": "Escuchar la segunda vez sin buscar nada.", "why": "Pierdes la oportunidad de notar algo.", "fix": "Elige un propósito antes."},
        {"wrong": "Contar mal por distraerte.", "why": "No se puede comprobar.", "fix": "Marca cada vez que oigas la palabra."},
    ],
    tiers={
        "recovery": [
            ex("¿Para qué sirve escuchar por segunda vez con un propósito?", "Para notar algo concreto", "Hay algo que buscar."),
            ex("¿Haces una marca cada vez que oyes la palabra que buscas?", "Sí", "Así cuentas sin perderte."),
            ex("¿Cuántas palabras tiene «sopla, sopla»?", "2", "Es la misma palabra dicha dos veces."),
        ],
        "understand": [
            ex("¿Cómo se comprueba un propósito de escucha?", "Contando o anotando lo que encuentro", "Se revisa con marcas o notas."),
            ex("¿Por qué volver a escuchar es valioso en una lengua que se recupera?", "Porque cada vez se aprende algo nuevo", "Se notan más cosas."),
            ex("¿Una imagen al escuchar es algo que ves en tu mente o en la pared?", "En tu mente", "Se imagina con la mente."),
        ],
        "apply": [
            ex(f"En «{TRABA2}», ¿cuántas palabras tiene en total?", "9", "Son 5 palabras en «seis sillas sin silla sirven» y 4 en «si se sientan seis»: 5 + 4 = 9."),
            ex(f"En «{VIENTO}», ¿cuántas veces suena «viento»?", "2", "Aparece en el primer y tercer verso."),
            ex(f"En «{CONTAR}», ¿qué palabra suena en «cuatro, vuela el pato»: pato o pez?", "Pato", "El tramo dice pato."),
        ],
        "reason": [
            ex("Dos niños escucharon la misma rima y contaron distinto «sopla». ¿Qué pueden hacer?", "Escuchar de nuevo y comparar", "Se comprueba otra vez."),
            ex("Una niña dice que ya no necesita otro propósito porque ya lo escuchó una vez. ¿Es cierto?", "No", "La segunda escucha da más detalles."),
        ],
        "challenge": [
            ex(f"En «{TRABA2}», ¿cuántas palabras empiezan con «si»?", "6", "Son sillas, sin, silla, sirven, si y sientan: seis palabras."),
            ex("Escribe un propósito de escucha para una rima que te lea un adulto.", "Por ejemplo, contar una palabra", "Debe ser concreto."),
        ],
    },
    context=[ex("Un mayor comparte un canto por segunda vez. Tomás no sabe qué buscar. ¿Qué podrías sugerirle?", "Contar una palabra que se repite", "Un propósito sencillo ayuda.")],
    selfcheck=[
        ex("En la segunda escucha de un texto, ¿qué haces distinto de la primera?", "Busco algo concreto", "Escuchas con propósito."),
        ex("¿Qué es una imagen al escuchar?", "Lo que veo en mi mente", "Se imagina con la mente."),
        ex("¿Cómo comprobar la cuenta?", "Con marcas", "Cada marca es una vez."),
    ],
    open_task=task(
        "Pide a un adulto que lea dos veces «" + TRABA2 + "». La primera vez escucha completo. La segunda cuenta cuántas veces suena «seis» y anota el número. Luego elige otro propósito para una tercera lectura (una imagen o un sonido) y anótalo. Pregunta al educador/a tradicional o a la comunidad: ¿qué conviene notar al escuchar un texto de nuestra lengua?",
        "Conté dos veces «seis». En la tercera lectura noté el sonido de la s. Mi pregunta: ¿qué conviene notar al escuchar un texto de nuestra lengua?",
        ["escucha dos veces", "anota lo encontrado", "pregunta al educador/a tradicional"],
        ["número anotado", "otro propósito", "pregunta escrita"],
        ["no tener propósito", "contar mal"],
        "Valora el propósito y la comprobación.",
    ),
    reinforce="Escucha dos veces una rima de tu casa; la segunda vez cuenta una palabra.",
    extend="Elige un propósito distinto para cada escucha de una rima.",
)

register(
    OA, 6,
    materials="Este cuaderno, lápiz y colores. Los textos de práctica están en castellano.",
    use="Aprenderé a compartir lo que comprendí de un texto con mi voz, mi cuerpo o un dibujo, y a agradecer. Sirve para mostrar lo que entendí y cuidar la lengua.",
    prior=["Sé escuchar con un propósito.", "Sé dibujar o hacer un gesto."],
    explain=[
        "Compartir lo que comprendiste puede hacerse de tres modos: con la voz, cuentas qué entendiste; con el cuerpo, muestras la idea con un gesto; con un dibujo, haces lo que viste en tu mente. Cualquiera sirve si muestra la idea del texto.",
        "Una buena respuesta dice una idea del texto y la une con algo que escuchaste. Por ejemplo: «El texto dice que el viento calla y el trigo duerme, y dibujé un campo quieto».",
        "Cierra siempre con respeto. Agradece a quien compartió el texto y di de quién es. Si tienes una duda, hazla como pregunta. En una lengua que se recupera, cada pregunta ayuda a que más personas la conozcan.",
    ],
    vocab=[("compartir", "mostrar a otros"), ("respuesta", "lo que digo o muestro"), ("agradecer", "decir gracias"), ("duda", "lo que no entendí"), ("idea", "lo principal del texto")],
    worked=[
        {"title": "Responder con un dibujo", "problem": f"Escuchaste «{VIENTO}». Respondes con un dibujo. ¿Qué dibujas?", "steps": ["La idea es que el viento se calma.", "Dibujo un campo de trigo quieto.", "Escribo: «duerme el trigo»."], "answer": "Un campo de trigo quieto con el verso escrito"},
        {"title": "Responder con una pregunta", "problem": "Escuchaste una canción de la comunidad y hay una palabra que no entiendes. ¿Cómo lo dices?", "steps": ["Agradezco la canción.", "Digo qué palabra no entendí.", "Pregunto qué quiere decir."], "answer": "Agradezco y pregunto qué quiere decir esa palabra"},
    ],
    mistakes=[
        {"wrong": "Pensar que solo vale responder escribiendo.", "why": "También vale gesto, voz o dibujo.", "fix": "Elige la forma que muestre tu idea."},
        {"wrong": "No decir de quién es el texto.", "why": "No se da crédito.", "fix": "Nombra a quien lo compartió."},
    ],
    tiers={
        "recovery": [
            ex("¿De qué tres formas puedes responder a un texto?", "Voz, cuerpo o dibujo", "Son tres formas."),
            ex("¿Qué dices a quien comparte un canto?", "Gracias", "Se agradece a quien comparte."),
            ex("Si te queda una duda sobre un canto del mayor, ¿cómo la expresas?", "La digo como pregunta", "Preguntar ayuda a comprender."),
        ],
        "understand": [
            ex("¿Por qué una pregunta también muestra que comprendiste?", "Porque muestra que pusiste atención", "Quien pregunta escuchó."),
            ex("¿Qué debe decir una buena respuesta?", "Una idea del texto", "Muestra que comprendiste."),
            ex("¿Qué debes decir al final sobre el texto?", "De quién es", "Se da crédito."),
        ],
        "apply": [
            ex(f"Responde con una frase: en «{ADIV_LUNA}», ¿qué hace la luna en el camino?", "Alumbra", "El texto dice que alumbra."),
            ex(f"Responde con un gesto: en «{CONTAR}», ¿qué haces para «salta el pez»?", "Un saltito", "Muestra el salto."),
            ex(f"Responde con un dibujo: en «{VIENTO}», ¿qué dibujas para «viento fuerte»?", "Ramas y trigo doblados por el viento", "Muestra la fuerza."),
        ],
        "reason": [
            ex("Un niño responde con un dibujo y otro con un gesto. ¿Alguno está mal?", "No", "Los dos muestran la idea."),
            ex("Una niña dice que no entendió una parte y pregunta. ¿Hizo algo malo?", "No", "Preguntar es comprender."),
        ],
        "challenge": [
            ex(f"En «{ADIV_LUNA}», cuenta cuántas ideas tiene: sale de noche, no tiene velas y alumbra, y cambia de forma. Escribe el número.", "3", "Son tres ideas."),
            ex("Escribe una frase de cierre que agradezca y diga de quién es el texto.", "Cualquier frase que agradezca y nombre a quien lo compartió", "Debe tener ambas partes."),
        ],
    },
    context=[ex("Tu curso responde al canto de un mayor: unos dibujan, otros hacen gestos y una pregunta. ¿Quién respondió bien?", "Todos", "Cada forma muestra la comprensión.")],
    selfcheck=[
        ex("Al terminar de escuchar, ¿qué palabra de cortesía dices a quien compartió?", "Gracias", "Se agradece a quien comparte."),
        ex("Para mostrar que comprendiste un canto, ¿sirve hacer un dibujo?", "Sí", "Es una forma válida."),
        ex("Si algo no quedó claro del texto, ¿lo preguntas o lo inventas?", "Lo pregunto", "Preguntar ayuda a comprender."),
    ],
    open_task=task(
        "Un adulto te dice «" + VIENTO + "». Responde de una de estas formas: con un dibujo, con un gesto o con tus palabras. Escribe una frase con la idea del texto y termina con un agradecimiento. Anota una duda como pregunta. Pregunta al educador/a tradicional o a la comunidad: ¿qué texto de nuestra lengua puedo escuchar y cómo debo agradecerlo?",
        "Dibujé un campo de trigo quieto. Escribí: «El viento se calma y el trigo duerme». Gracias por leerlo. Mi duda: ¿por qué el viento calla? Mi pregunta: ¿qué texto de nuestra lengua puedo escuchar?",
        ["responde con la forma elegida", "dice una idea", "agradece y pregunta"],
        ["dibujo o gesto", "frase", "pregunta escrita"],
        ["no agradecer", "inventar respuestas"],
        "Valora la respuesta, el agradecimiento y la pregunta.",
    ),
    reinforce="Cuenta a alguien de tu casa de qué trata una rima, con un dibujo.",
    extend="Responde al mismo texto con un gesto y con un dibujo.",
)

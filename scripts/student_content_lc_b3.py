"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF03 (palabras, frases, toponimia y antroponimia significativas) y OA LF04 (relatos,
experiencia y conocimiento cultural), contexto de fortalecimiento de la lengua.

Los mapas, nombres de personas y relatos de práctica son inventados y están en castellano. El
saludo «mari mari» (mapuzugun) es el único término de lengua indígena que se usa, como saludo.
Los significados de nombres reales de lugares y personas los enseñan el educador/a tradicional y la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA3 = "LC01 OA LF03"
OA4 = "LC01 OA LF04"

MAPA = "Mapa de práctica: Quebrada del Sauce (al norte), Cerro Alto (al este), Río Claro (al sur) y Playa Larga (al oeste)."
RELATO_A = ("Lía y su abuelo caminaron al río al amanecer. Llevaban pan y una manta. En la orilla vieron una garza blanca. "
            "El abuelo dijo: «Hay que hablar bajito para no asustarla». Lía se quedó quieta y contó hasta diez. "
            "La garza abrió las alas y se fue volando.")


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ LF03
register(
    OA3, 1,
    materials="Este cuaderno y lápiz. Las palabras de práctica son del castellano; el educador/a tradicional trae las de la lengua de su pueblo.",
    use="Aprenderé que cada palabra o frase se usa en una ocasión y que tiene un significado. Sirve para decir la palabra correcta en el momento correcto.",
    prior=["Sé que las palabras quieren decir algo.", "Sé quiénes son las personas que me enseñan."],
    explain=[
        "Una palabra o frase tiene un significado y también una ocasión de uso, es decir, el momento y el lugar donde se dice. «Buenos días» se dice cuando llegas por la mañana. «Gracias» se dice cuando recibes algo. No sirven en cualquier momento.",
        "Pasa lo mismo con las palabras de la lengua de un pueblo. «Mari mari» es un saludo en mapuzugun y se dice al encontrarse con alguien. Otras palabras y frases se usan en otras ocasiones y esas las enseña el educador o educadora tradicional.",
        "Para aprender bien una palabra necesitas tres datos: qué significa, cuándo se usa y quién te la enseñó. Una ficha de uso te ayuda a guardar los tres. Si falta alguno, pregunta antes de usar la palabra.",
    ],
    vocab=[("ocasión de uso", "momento y lugar donde se dice una palabra"), ("frase", "grupo de palabras con sentido"), ("ficha de uso", "tarjeta con palabra, significado, ocasión y fuente"), ("significado", "lo que quiere decir"), ("fuente", "quién me enseñó la palabra")],
    worked=[
        {"title": "Palabra y ocasión", "problem": "Une la expresión con su ocasión: «buenos días», «gracias», «buenas noches». Ocasiones: al recibir un regalo, al irse a dormir, al llegar en la mañana.", "steps": ["«Buenos días» se dice por la mañana.", "«Gracias» se dice al recibir algo.", "«Buenas noches» se dice al irse a dormir."], "answer": "buenos días: al llegar en la mañana; gracias: al recibir un regalo; buenas noches: al irse a dormir"},
        {"title": "Saludo con su ocasión", "problem": "La educadora tradicional mapuche enseña «mari mari» como saludo. ¿En qué ocasión lo dices?", "steps": ["Es un saludo.", "Los saludos se usan al encontrarse con alguien.", "Lo digo cuando la veo llegar."], "answer": "Al encontrarme con alguien para saludarlo"},
    ],
    mistakes=[
        {"wrong": "Usar una palabra en cualquier momento.", "why": "Cada palabra tiene su ocasión.", "fix": "Pregunta cuándo se usa antes de decirla."},
        {"wrong": "Guardar una palabra sin su significado ni su fuente.", "why": "Después no sabrás qué quiere decir ni quién la enseñó.", "fix": "Anota los tres datos en la ficha de uso."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué dices cuando recibes un regalo: «gracias» o «buenas noches»?", "Gracias", "«Gracias» es para agradecer lo que recibes."),
            ex("¿Cuándo se dice «buenas noches»: al irse a dormir o al llegar a la escuela de mañana?", "Al irse a dormir", "Es un saludo de la noche."),
            ex("¿Para qué se usa «mari mari» en el ejemplo de la educadora?", "Para saludar", "Es un saludo en mapuzugun."),
        ],
        "understand": [
            ex("¿Qué es la ocasión de uso de una palabra?", "El momento y lugar donde se dice", "La ocasión dice cuándo conviene usarla."),
            ex("¿Cuáles son los tres datos de una ficha de uso?", "Significado, ocasión y fuente", "Con ellos sabes qué es, cuándo se usa y quién la enseñó."),
            ex("¿Por qué no se dice «buenos días» a medianoche?", "Porque no es la ocasión", "«Buenos días» es para la mañana."),
        ],
        "apply": [
            ex("Completa: «Cuando llego a la escuela por la mañana digo _______».", "Buenos días", "Es la expresión de la mañana."),
            ex("Una amiga te presta un lápiz. ¿Qué expresión usas: «gracias» o «hasta luego»?", "Gracias", "Agradecer es la ocasión de «gracias»."),
            ex("Completa la ficha: palabra «mari mari»; significado: saludo; ocasión: ______; fuente: la educadora tradicional. ¿Qué escribes en la ocasión?", "Al encontrarse con alguien", "Es la ocasión de un saludo."),
        ],
        "reason": [
            ex("Un niño dice «gracias» cuando entra a la sala, sin recibir nada. ¿Está bien la ocasión?", "No", "Gracias es para agradecer algo, no para llegar."),
            ex("Dos niñas saben que una palabra se usa en una fiesta, pero no saben qué significa. ¿Pueden usarla?", "No todavía", "Falta conocer el significado; deben preguntar."),
        ],
        "challenge": [
            ex("En tu ficha de uso hay: «gracias», «buenos días», «mari mari» y «buenas noches». ¿Cuántas de ellas son saludos de encuentro o de la jornada?", "3", "«Buenos días», «buenas noches» y «mari mari» son saludos; «gracias» agradece."),
            ex("Escribe una ocasión en que dirías «perdón».", "Cuando me equivoco o molesto a alguien", "«Perdón» se usa al equivocarse."),
        ],
    },
    context=[ex("Entra la educadora tradicional al aula. Los niños dicen palabras al mismo tiempo, sin saber en qué ocasión se usan. ¿Qué puedes proponer?", "Preguntar cuándo se usa cada palabra", "Cada palabra tiene su ocasión y quien la enseña la conoce.")],
    selfcheck=[
        ex("¿Una palabra se usa en cualquier momento?", "No", "Cada palabra tiene su ocasión."),
        ex("¿Qué dices al recibir un regalo?", "Gracias", "Es la expresión para agradecer."),
        ex("¿Para qué sirve la ficha de uso?", "Para guardar significado, ocasión y fuente", "Reúne lo que necesitas saber."),
    ],
    open_task=task(
        "Haz una ficha de uso con cada una de estas tres expresiones del castellano: «gracias», «buenos días» y «buenas noches». En cada ficha escribe el significado, en qué ocasión se usa y quién te la enseñó (un adulto de tu casa). Dibuja la ocasión. Luego pregunta al educador/a tradicional o a la comunidad: ¿qué palabras o frases de la lengua de su pueblo puedo aprender primero, y en qué ocasión se usa cada una?",
        "Gracias: se usa al recibir algo (dibujé un regalo). Me lo enseñó mi papá. Mi pregunta: ¿qué frases de la lengua puedo aprender primero y cuándo se usan?",
        ["escribe significado y ocasión", "anota la fuente", "pregunta al educador/a tradicional"],
        ["tres fichas con dibujo", "pregunta escrita"],
        ["usar la palabra fuera de su ocasión", "no anotar la fuente"],
        "Reconoce las fichas completas y pide que la ficha de la lengua la escriba con el educador/a tradicional.",
    ),
    reinforce="Haz una ficha de uso para una expresión de tu casa, con su ocasión y quién te la enseñó.",
    extend="Averigua en qué ocasión se usan dos expresiones más de tu casa y escríbelas en fichas.",
)

register(
    OA3, 2,
    materials="Este cuaderno, lápiz y el mapa de práctica de la clase, que está escrito aquí.",
    use="Aprenderé que los nombres de los lugares (la toponimia) cuentan algo del territorio. Sirve para ubicarse y para respetar la historia de cada lugar.",
    prior=["Sé que los lugares tienen nombre.", "Sé leer palabras cortas con ayuda de un adulto."],
    explain=[
        "La toponimia es el conjunto de nombres de los lugares: ríos, cerros, playas, pueblos. Cada nombre suele contar algo: cómo es el lugar, qué hay en él o qué pasó ahí. Por ejemplo, «Río Claro» dice que el agua es clara.",
        "Muchos lugares de Chile tienen nombres que vienen de lenguas indígenas, y otros vienen del castellano. Para saber qué cuenta un nombre, no basta con adivinar: hay que preguntar a personas de la comunidad que conocen el territorio y su historia.",
        "Un mapa te ayuda a relacionar un nombre con un lugar. Con los puntos cardinales dices dónde está cada cosa: al norte, al sur, al este, al oeste. En un mapa el norte se dibuja arriba, el sur abajo, el este a la derecha y el oeste a la izquierda. Si un nombre de la lengua del pueblo no lo conoces, no lo traduzcas tú: pide que te lo expliquen.",
    ],
    vocab=[("toponimia", "nombres de los lugares"), ("territorio", "lugar donde vive y se mueve una comunidad"), ("mapa", "dibujo de un lugar visto desde arriba"), ("norte, sur, este, oeste", "direcciones para ubicar lugares"), ("nombre", "palabra con que se llama a un lugar o persona")],
    worked=[
        {"title": "Leer un nombre de lugar", "problem": f"{MAPA} ¿Qué te cuenta el nombre «Río Claro»?", "steps": ["Leo las palabras: río y claro.", "Un río es agua que corre.", "Claro dice cómo es el agua: se ve limpia."], "answer": "Cuenta que ahí hay un río de agua clara"},
        {"title": "Ubicar un lugar", "problem": f"{MAPA} ¿Qué lugar está al norte?", "steps": ["Busco la palabra norte en el mapa.", "Al norte dice Quebrada del Sauce.", "Esa es la respuesta."], "answer": "Quebrada del Sauce"},
    ],
    mistakes=[
        {"wrong": "Inventar qué significa un nombre de lugar de la lengua indígena.", "why": "Puedes decir algo falso sobre el territorio.", "fix": "Pregunta a una persona de la comunidad."},
        {"wrong": "Confundir norte con sur en el mapa.", "why": "Se lee mal la ubicación.", "fix": "Busca la palabra exacta que dice el mapa."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA} ¿Qué lugar está al sur?", "Río Claro", "El mapa dice que Río Claro está al sur."),
            ex(f"{MAPA} ¿Qué lugar está al oeste?", "Playa Larga", "El mapa pone Playa Larga al oeste."),
            ex("¿Qué es la toponimia?", "Los nombres de los lugares", "Es el conjunto de nombres de los lugares."),
        ],
        "understand": [
            ex("¿Qué suele contar el nombre de un lugar?", "Cómo es, qué hay o qué pasó", "Los nombres guardan información del lugar."),
            ex("¿Todos los nombres de lugares de Chile vienen del castellano?", "No", "Muchos vienen de lenguas indígenas."),
            ex("¿A quién preguntas qué significa un nombre de lugar de la lengua del pueblo?", "A personas de la comunidad que conocen el territorio", "Ellas conocen la historia del lugar."),
        ],
        "apply": [
            ex(f"{MAPA} ¿Qué lugar está al este?", "Cerro Alto", "El mapa pone Cerro Alto al este."),
            ex(f"{MAPA} ¿Cuántos lugares tiene el mapa en total?", "4", "Son Quebrada del Sauce, Cerro Alto, Río Claro y Playa Larga."),
            ex(f"{MAPA} ¿En qué lugar crees que hay un árbol llamado sauce: en Quebrada del Sauce o en Playa Larga?", "En Quebrada del Sauce", "El nombre dice sauce."),
        ],
        "reason": [
            ex(f"{MAPA} Un niño dice que Playa Larga está al sur. ¿Tiene razón?", "No; está al oeste", "El mapa pone Playa Larga al oeste."),
            ex("Un compañero dice que sabe qué significa un nombre de lugar mapuche porque suena parecido a otra palabra. ¿Es buena razón?", "No", "Por sonar parecido no se puede asegurar el significado."),
        ],
        "challenge": [
            ex(f"{MAPA} Si caminas de Río Claro hacia el norte, ¿llegas a Quebrada del Sauce o a Playa Larga?", "A Quebrada del Sauce", "El norte del mapa tiene Quebrada del Sauce."),
            ex("Escribe el nombre de un lugar de tu barrio y dibuja un mapa muy simple con su ubicación.", "Cualquier nombre de lugar de su barrio", "Se acepta un lugar real y conocido."),
        ],
    },
    context=[ex("La educadora tradicional quiere contar por qué un cerro de la zona tiene cierto nombre. Una niña dice: «Yo sé, seguro es por..». ¿Qué debe hacer?", "Escuchar a la educadora", "Quien conoce el territorio explica el nombre.")],
    selfcheck=[
        ex(f"{MAPA} ¿Qué lugar está al norte?", "Quebrada del Sauce", "El mapa lo dice."),
        ex("¿Se adivina el significado de un nombre indígena de lugar?", "No, se pregunta", "Se pregunta a la comunidad."),
        ex("¿Qué es el territorio?", "El lugar donde vive y se mueve una comunidad", "Es el espacio de la comunidad."),
    ],
    open_task=task(
        "Dibuja un mapa muy simple de tu barrio o de tu casa con tres lugares, por ejemplo: la plaza, la escuela y tu casa. Escribe el nombre de cada lugar y cuál es su ubicación (arriba, abajo, a la derecha o a la izquierda). Pregunta a un adulto por qué un lugar tiene ese nombre. Anota una pregunta para el educador/a tradicional o la comunidad: ¿qué lugares de nuestro territorio tienen nombre en la lengua del pueblo y qué cuenta cada nombre?",
        "Dibujé la plaza arriba, la escuela a la derecha y mi casa abajo. La plaza se llama así porque ahí hay una feria. Mi pregunta: ¿qué lugares de nuestro territorio tienen nombre en la lengua del pueblo?",
        ["dibuja tres lugares con nombre", "ubica cada lugar", "pregunta a la comunidad por un nombre"],
        ["mapa dibujado", "pregunta escrita"],
        ["inventar el significado de un nombre", "confundir la ubicación"],
        "Reconoce el mapa y la ubicación y recuerda que el significado de nombres indígenas lo enseña la comunidad.",
    ),
    reinforce="Dibuja un mapa de tu sala con tres lugares y sus nombres.",
    extend="Averigua por qué dos lugares de tu barrio tienen el nombre que tienen y anótalo.",
)

register(
    OA3, 3,
    materials="Este cuaderno y lápiz. Las historias de nombres de práctica son inventadas.",
    use="Aprenderé que los nombres de las personas (la antroponimia) guardan historias y que cada persona decide si las cuenta. Sirve para respetar el nombre y la historia de cada uno.",
    prior=["Sé decir mi nombre.", "Sé que los nombres de mi familia vienen de alguien."],
    explain=[
        "La antroponimia son los nombres de las personas: el nombre y el apellido. Un nombre puede recordar a un abuelo, un lugar, una flor o algo que pasó. Por eso se dice que el nombre guarda memoria.",
        "Cada pueblo tiene sus propias formas de dar nombres y de entender su significado. Esas formas las conocen las familias y la comunidad. Tú no inventas el significado de un nombre indígena ni lo adivinas por cómo suena.",
        "La historia de un nombre es de la persona y de su familia. Si quieres saberla, preguntas con respeto y aceptas si no quiere contarla. Y no te ríes ni haces bromas con el nombre de nadie.",
    ],
    vocab=[("antroponimia", "nombres de las personas"), ("apellido", "nombre que comparte una familia"), ("memoria", "lo que se recuerda"), ("historia del nombre", "razón por la que alguien lleva ese nombre"), ("permiso", "autorización para contar algo de otra persona")],
    worked=[
        {"title": "Un nombre con historia", "problem": "La abuela Rosa se llama Rosa porque cuando nació, su mamá tenía un rosal en el patio. ¿Qué recuerda el nombre?", "steps": ["Leo la historia: había un rosal.", "El nombre viene de una flor.", "Recuerda el rosal del patio."], "answer": "Recuerda el rosal del patio donde nació"},
        {"title": "Preguntar con respeto", "problem": "Quieres saber por qué un compañero tiene un apellido. ¿Qué haces?", "steps": ["Le pregunto con amabilidad.", "Acepto si no quiere contar.", "No hago bromas con su apellido."], "answer": "Preguntar con respeto y aceptar si no quiere contar"},
    ],
    mistakes=[
        {"wrong": "Hacer bromas con el nombre de alguien.", "why": "Es una falta de respeto a la persona y a su familia.", "fix": "Cuida los nombres como cuidas a las personas."},
        {"wrong": "Contar la historia del nombre de otro sin su permiso.", "why": "Esa historia es de él y su familia.", "fix": "Pide permiso antes de contarla."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es la antroponimia?", "Los nombres de las personas", "Antropónimo es nombre de persona."),
            ex("La abuela Rosa se llama así por un rosal. ¿Qué flor recuerda su nombre?", "La rosa", "El nombre viene del rosal."),
            ex("¿Haces bromas con el nombre de otro niño?", "No", "Los nombres se respetan."),
        ],
        "understand": [
            ex("¿Qué quiere decir que un nombre guarda memoria?", "Que recuerda algo o a alguien", "Un nombre puede recordar a una persona, un lugar o un hecho."),
            ex("¿Quién conoce cómo se dan los nombres en un pueblo?", "Las familias y la comunidad", "Ellas conocen sus formas de dar nombres."),
            ex("¿Puedes contar la historia del nombre de otra persona sin permiso?", "No", "La historia es de la persona y su familia."),
        ],
        "apply": [
            ex("Tomás se llama como su abuelo. ¿A quién recuerda su nombre?", "A su abuelo", "Lleva el nombre de su abuelo."),
            ex("Lía quiere saber por qué su amiga se llama Marina y le pregunta. La amiga dice que prefiere no contarlo. ¿Qué hace Lía?", "Acepta y no insiste", "Respeta la decisión de la amiga."),
            ex("En tu curso hay 3 niñas que se llaman Ana y 2 niñas que se llaman Rosa. ¿Cuántas niñas tienen esos dos nombres?", "5", "3 + 2 = 5."),
        ],
        "reason": [
            ex("Un niño dice que el nombre de un compañero significa algo gracioso por cómo suena. ¿Por qué no está bien?", "Porque inventa el significado y se burla", "No se adivina ni se hace burla de un nombre."),
            ex("Una niña pregunta con amabilidad por qué su amigo tiene un apellido. El amigo cuenta. ¿Fue una buena forma de preguntar?", "Sí", "Preguntó con respeto y el amigo quiso contar."),
        ],
        "challenge": [
            ex("Escribe tu nombre y una cosa que tu familia sepa sobre él, o escribe «no lo sé todavía» y pregunta en casa.", "Cualquier respuesta que diga algo del nombre o que no se sabe", "Se acepta lo que cada uno sabe de su nombre."),
            ex("Tienes 4 amigos con nombres distintos. ¿Cuántas historias de nombres puedes pedir si cada amigo cuenta una?", "4", "Una historia por amigo."),
        ],
    },
    context=[ex("El educador tradicional cuenta la historia de su propio nombre al curso. Después un niño la repite en el recreo cambiándola. ¿Qué hizo mal?", "Cambió la historia de otro", "La historia es del educador y no se cambia.")],
    selfcheck=[
        ex("¿Qué guarda un nombre?", "Memoria", "Un nombre recuerda algo."),
        ex("¿Se bromea con los nombres?", "No", "Los nombres se respetan siempre."),
        ex("¿Qué haces antes de contar la historia del nombre de otro?", "Pedir permiso", "La historia es de la persona."),
    ],
    open_task=task(
        "Pregunta a un adulto de tu casa por qué te pusieron tu nombre y escribe o dibuja lo que te cuente. Si no lo saben o no quieren contarlo, escribe «no lo sé todavía» y dibuja tu nombre con colores. No necesitas mostrar tu historia a nadie si no quieres. Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿cómo se dan los nombres en su pueblo y qué debo cuidar cuando hablo de un nombre?",
        "Mi mamá me contó que me puse el nombre de mi bisabuela. Dibujé a mi bisabuela. Mi pregunta: ¿cómo se dan los nombres en el pueblo y qué debo cuidar?",
        ["pregunta con respeto", "registra lo que le cuentan o dice que no lo sabe", "pregunta al educador/a tradicional"],
        ["dibujo o frase", "pregunta escrita"],
        ["hacer bromas con nombres", "contar historias ajenas sin permiso"],
        "Reconoce el respeto al preguntar y agrega que no hay obligación de compartir la historia de su nombre.",
    ),
    reinforce="Pregunta a un familiar por la historia de su nombre y escúchala sin interrumpir.",
    extend="Dibuja un árbol con los nombres de tres personas de tu familia, solo si quieres compartirlo.",
)

register(
    OA3, 4,
    materials="Este cuaderno y lápiz. La expresión que se usa la valida el educador/a tradicional.",
    use="Aprenderé a hacer una interacción breve, como un saludo, solo cuando la expresión fue validada y es el momento correcto. Sirve para conversar con respeto.",
    prior=["Sé saludar con respeto.", "Sé que cada expresión tiene su ocasión."],
    explain=[
        "Una interacción breve es una conversación muy corta, como saludar y responder. Tiene turnos: primero habla uno, luego habla el otro. Para hacerla bien miras a la persona, hablas con voz clara y esperas la respuesta.",
        "Con una lengua indígena, la interacción solo se hace con expresiones que fueron validadas por el educador tradicional o la comunidad. Por ejemplo, «mari mari» es un saludo en mapuzugun que puedes usar si el educador/a tradicional te lo enseñó. No inventes respuestas.",
        "Si la persona responde algo que no entiendes, no finjas. Dices «gracias» con respeto y le preguntas al educador o educadora cómo se responde y qué significa. Así cuidas la lengua y no la usas fuera de contexto.",
    ],
    vocab=[("interacción", "conversación entre dos personas"), ("turno", "momento en que habla cada uno"), ("validada", "confirmada por quien conoce la lengua"), ("responder", "decir algo después de que te hablan"), ("fingir", "hacer como que se entiende sin entender")],
    worked=[
        {"title": "Saludo y respuesta", "problem": "La educadora te saluda y tú respondes con el saludo que ella enseñó. ¿En qué orden se hace?", "steps": ["Ella saluda primero.", "Yo la miro y escucho.", "Después respondo con el saludo validado."], "answer": "Primero ella saluda; después respondo yo"},
        {"title": "No entiendo la respuesta", "problem": "Después de tu saludo, un hablante te dice algo más que no entiendes. ¿Qué haces?", "steps": ["No finjo que entendí.", "Agradezco con respeto.", "Pregunto después al educador/a tradicional."], "answer": "Agradezco y pregunto después qué significa"},
    ],
    mistakes=[
        {"wrong": "Inventar una respuesta cuando no entiendes.", "why": "Puedes decir algo equivocado o irrespetuoso.", "fix": "Agradece y pregunta después al educador/a tradicional."},
        {"wrong": "Usar una expresión que no fue validada.", "why": "Puede no corresponder a ese pueblo.", "fix": "Usa solo las que el educador/a tradicional validó."},
    ],
    tiers={
        "recovery": [
            ex("En una interacción breve, ¿hablan los dos al mismo tiempo o por turnos?", "Por turnos", "Cada uno habla cuando le toca."),
            ex("¿A quién miras cuando saludas?", "A la persona", "Mirar muestra respeto."),
            ex("¿Qué haces si no entiendes lo que te responden?", "Agradezco y pregunto después", "No se finge entender."),
        ],
        "understand": [
            ex("¿Por qué solo se usan expresiones validadas?", "Para no usar la lengua equivocadamente", "Quien conoce la lengua confirma que está bien."),
            ex("¿Qué es un turno?", "El momento en que habla cada uno", "Es cuando te toca hablar."),
            ex("¿Es lo mismo fingir que entiendes que preguntar?", "No", "Fingir engaña; preguntar ayuda a comprender."),
        ],
        "apply": [
            ex("Ordena: a) la persona responde, b) yo saludo, c) miro a la persona. Escribe las letras en orden.", "c, b, a", "Primero miro, luego saludo y al final la persona responde."),
            ex("Llega la educadora y te saluda con «mari mari». ¿Cómo respondes, si ella te enseñó el saludo?", "Con el saludo que ella enseñó", "Se responde con lo validado."),
            ex("En un saludo hay 2 personas y cada una habla una vez. ¿Cuántos turnos hay?", "2", "Una vez cada persona son 2 turnos."),
        ],
        "reason": [
            ex("Un niño responde con una frase inventada que le sonó bien. ¿Qué podría pasar?", "Decir algo equivocado", "Sin validar, la frase puede no significar lo que cree."),
            ex("Una niña no entendió la respuesta y la anotó para preguntar después. ¿Hizo bien?", "Sí", "Preguntar después evita fingir."),
        ],
        "challenge": [
            ex("En una interacción breve hay 3 pasos: mirar, saludar y esperar la respuesta. Si hay 5 niños que saludan a la educadora uno por uno, ¿cuántos pasos se hacen en total?", "15", "3 + 3 + 3 + 3 + 3 = 15."),
            ex("Escribe una frase para agradecer cuando no entiendes lo que te responden.", "Cualquier frase de agradecimiento respetuosa", "Se acepta un gracias respetuoso."),
        ],
    },
    context=[ex("Un invitado habla con tu curso en su lengua. Pedro responde con una palabra que oyó en un video. ¿Qué podrías decirle?", "Que use solo las expresiones validadas", "La palabra del video puede no corresponder a ese pueblo.")],
    selfcheck=[
        ex("¿Se habla por turnos?", "Sí", "Cada uno espera su turno."),
        ex("¿Quién valida la expresión?", "El educador/a tradicional o la comunidad", "Ellos conocen la lengua."),
        ex("¿Qué haces si no entiendes?", "Agradezco y pregunto después", "No se finge."),
    ],
    open_task=task(
        "Con un adulto de tu casa haz tres veces una interacción breve de saludo, cada vez con una persona distinta: primero miras a la persona, luego la saludas con respeto y esperas su respuesta. Si el educador/a tradicional ya te enseñó una expresión de saludo, úsala; si no, usa un saludo en castellano. Anota qué cuidaste. Pregunta al educador/a tradicional o a la comunidad qué responden las personas a ese saludo y cuándo conviene usarlo.",
        "Saludé a mi mamá, a mi hermano y a mi abuelo. Los miré y esperé su respuesta. Mi pregunta: ¿qué responde la gente al saludo de la comunidad y cuándo se usa?",
        ["respeta turnos", "mira a la persona", "usa solo expresiones validadas"],
        ["tres saludos anotados", "pregunta escrita"],
        ["inventar respuestas", "fingir que entiende"],
        "Valora la interacción cuidada y recuerda que la respuesta correcta la enseña la comunidad.",
    ),
    reinforce="Haz una interacción breve de saludo con alguien de tu casa y espera su respuesta.",
    extend="Explica a un familiar por qué no se debe fingir que se entiende una frase en otra lengua.",
)

# ================================================================ LF04
register(
    OA4, 1,
    materials=f"Este cuaderno y lápiz. El relato de práctica está escrito aquí y un adulto puede leértelo: «{RELATO_A}»",
    use="Aprenderé a escuchar un relato completo y a decir quiénes son los personajes, dónde ocurre y qué pasa. Sirve para comprender lo que cuentan las personas mayores.",
    prior=["Sé escuchar un texto completo.", "Sé decir quién, dónde y qué."],
    explain=[
        "Un relato cuenta algo que pasa. Tiene personajes, que son quienes actúan, un lugar, que es dónde pasa, y un acontecimiento, que es lo que ocurre. Al escuchar un relato completo puedes seguir estas tres cosas.",
        "Para seguir un relato, no hace falta recordar todo. Basta con responder: ¿quiénes están?, ¿dónde están?, ¿qué pasó? En el relato de práctica, Lía y su abuelo caminan al río y ven una garza. Esas respuestas ya muestran lo principal.",
        "Los relatos de los pueblos los cuentan personas de la comunidad. Los escuchas completos, sin interrumpir, y preguntas al final. Si no entiendes una palabra, no la inventes: pregunta qué quiere decir.",
    ],
    vocab=[("relato", "texto que cuenta algo que pasa"), ("personaje", "quien actúa en el relato"), ("lugar", "dónde ocurre el relato"), ("acontecimiento", "lo que pasa en el relato"), ("orilla", "borde de un río o del mar")],
    worked=[
        {"title": "Personajes del relato", "problem": f"Relato: «{RELATO_A}» ¿Quiénes son los personajes?", "steps": ["Busco quiénes hacen cosas.", "Lía y su abuelo caminan.", "La garza vuela."], "answer": "Lía, su abuelo y la garza"},
        {"title": "Lugar y acontecimiento", "problem": f"Relato: «{RELATO_A}» ¿Dónde ocurre y qué pasa al final?", "steps": ["El lugar es la orilla del río.", "Al final la garza abre las alas.", "Se va volando."], "answer": "En la orilla del río; la garza se va volando"},
    ],
    mistakes=[
        {"wrong": "Interrumpir el relato para preguntar.", "why": "Se pierde el hilo y falta respeto a quien cuenta.", "fix": "Escucha completo y pregunta al final."},
        {"wrong": "Inventar lo que no se oyó.", "why": "Cambia el relato.", "fix": "Di solo lo que el relato dijo y pregunta lo que falta."},
    ],
    tiers={
        "recovery": [
            ex(f"Relato: «{RELATO_A}» ¿Quién camina con Lía?", "Su abuelo", "El relato dice que caminó con su abuelo."),
            ex(f"Relato: «{RELATO_A}» ¿Qué animal aparece en la orilla?", "Una garza", "El relato nombra una garza blanca."),
            ex("¿Qué haces mientras alguien cuenta un relato: escuchar o interrumpir?", "Escuchar", "Se escucha el relato completo."),
        ],
        "understand": [
            ex("¿Qué es un personaje?", "Quien actúa en el relato", "Los personajes hacen las cosas del relato."),
            ex("¿Qué es el lugar de un relato?", "Dónde ocurre", "Es el sitio de la historia."),
            ex("¿Qué es el acontecimiento?", "Lo que pasa", "Es el hecho principal."),
        ],
        "apply": [
            ex(f"Relato: «{RELATO_A}» ¿En qué momento del día caminaron al río?", "Al amanecer", "El relato empieza al amanecer."),
            ex(f"Relato: «{RELATO_A}» ¿Cuántos personajes hay: Lía, el abuelo y la garza?", "3", "Son tres personajes: Lía, el abuelo y la garza."),
            ex(f"Relato: «{RELATO_A}» ¿De qué color es la garza?", "Blanca", "El relato dice garza blanca."),
        ],
        "reason": [
            ex("Una niña escuchó el relato de práctica a medias y dice que la garza se quedó en la orilla. ¿Qué le faltó oír?", "El final", "Al final la garza se fue volando."),
            ex("Dos niños cuentan el mismo relato; uno dice que hay tres personajes y el otro dice que hay dos. ¿Quién está en lo cierto?", "El que dice tres", "Son Lía, el abuelo y la garza."),
        ],
        "challenge": [
            ex(f"Relato: «{RELATO_A}» ¿Cuántas cosas llevaban para el paseo: pan, manta y una canasta?", "2", "Llevaban pan y una manta."),
            ex(f"Relato: «{RELATO_A}» Escribe en una frase quiénes, dónde y qué.", "Lía y su abuelo vieron una garza en la orilla del río y la garza se fue volando", "Debe incluir personajes, lugar y acontecimiento."),
        ],
    },
    context=[ex("El educador tradicional cuenta un relato y un niño lo interrumpe tres veces con preguntas. ¿Qué podría hacer mejor?", "Esperar al final para preguntar", "Escuchar completo permite entender y respetar.")],
    selfcheck=[
        ex(f"Relato: «{RELATO_A}» ¿Dónde ocurre?", "En la orilla del río", "El relato menciona el río."),
        ex("¿Quién actúa en un relato?", "Los personajes", "Ellos hacen las cosas."),
        ex("¿Cuándo preguntas?", "Al final", "Después de escuchar completo."),
    ],
    open_task=task(
        "Pide a un adulto que te lea el relato de práctica «" + RELATO_A + "». Escucha completo y después dibuja tres cosas: los personajes, el lugar y lo que pasa al final. Escribe una frase para cada uno. Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿qué relato de su pueblo puedo escuchar y quién lo puede contar?",
        "Dibujé a Lía, al abuelo y a la garza; el río; y la garza volando. Mi pregunta: ¿qué relato del pueblo puedo escuchar?",
        ["escucha completo", "dice personajes, lugar y acontecimiento", "pregunta al educador/a tradicional"],
        ["tres dibujos con frases", "pregunta escrita"],
        ["interrumpir", "inventar lo que no se oyó"],
        "Reconoce que siguió personajes, lugar y acontecimiento, y pide que la pregunta sea para quien cuenta relatos.",
    ),
    reinforce="Escucha un cuento de tu casa y di quiénes son los personajes y dónde pasa.",
    extend="Cuenta con tus palabras el relato de práctica a un familiar, siguiendo el orden.",
)

register(
    OA4, 2,
    materials=f"Este cuaderno y lápiz. Relato de práctica: «{RELATO_A}»",
    use="Aprenderé a recuperar un detalle que el relato dice de forma explícita, es decir, con palabras claras. Sirve para saber con exactitud lo que cuenta el relato.",
    prior=["Sé escuchar un relato completo.", "Sé quiénes son los personajes."],
    explain=[
        "Un detalle explícito es algo que el relato dice con todas sus letras. Por ejemplo, el relato de práctica dice que Lía y su abuelo llevaban pan y una manta. No hay que adivinar: está dicho.",
        "Para recuperar un detalle explícito, vuelves a escuchar el relato y buscas la parte exacta. Puedes subrayar o hacer una marca. Si el relato no lo dice, no lo inventas. Tu respuesta debe poder demostrarse con el texto.",
        "En los relatos de los pueblos hay información cultural que solo la comunidad conoce. No se debe agregar datos que el relato no dice. Si quieres saber más, preguntas a quien lo cuenta, y le agradeces.",
    ],
    vocab=[("detalle", "dato pequeño del relato"), ("explícito", "dicho claramente en el relato"), ("subrayar", "hacer una línea bajo lo importante"), ("demostrar", "mostrar con el texto que algo es cierto"), ("información cultural", "datos sobre cómo vive y piensa un pueblo")],
    worked=[
        {"title": "Detalle del lugar", "problem": f"Relato: «{RELATO_A}» ¿Qué vieron en la orilla?", "steps": ["Busco la palabra orilla.", "Dice: «En la orilla vieron una garza blanca».", "Ese es el detalle."], "answer": "Una garza blanca"},
        {"title": "Lo que el relato no dice", "problem": f"Relato: «{RELATO_A}» ¿Cómo se llama el río?", "steps": ["Busco el nombre del río.", "El relato solo dice «el río».", "No lo sé; pregunto a quien lo cuenta."], "answer": "El relato no lo dice; hay que preguntar"},
    ],
    mistakes=[
        {"wrong": "Responder algo que el relato no dice.", "why": "Es inventar, no recuperar.", "fix": "Busca la frase del relato que lo demuestre."},
        {"wrong": "Confundir un detalle con una opinión.", "why": "Una opinión no está en el relato.", "fix": "Pregunta: ¿esto lo dice el relato?"},
    ],
    tiers={
        "recovery": [
            ex(f"Relato: «{RELATO_A}» ¿Qué llevaban además del pan?", "Una manta", "El relato dice que llevaban pan y una manta."),
            ex(f"Relato: «{RELATO_A}» ¿Hasta cuánto contó Lía?", "Hasta diez", "El relato dice que contó hasta diez."),
            ex("¿Un detalle explícito está dicho o hay que adivinarlo?", "Está dicho", "Explícito es lo dicho con claridad."),
        ],
        "understand": [
            ex("¿Cómo comprobar que un detalle es explícito?", "Buscando la frase que lo dice", "La frase demuestra el detalle."),
            ex("¿Por qué no hay que agregar datos que el relato no dice?", "Porque cambiarían el relato", "El relato debe quedar como se contó."),
            ex("¿Qué haces si quieres saber más que lo que dice el relato?", "Preguntar a quien lo cuenta", "Quien lo cuenta conoce más."),
        ],
        "apply": [
            ex(f"Relato: «{RELATO_A}» ¿Qué dijo el abuelo?", "Hay que hablar bajito para no asustarla", "Está dicho en el relato."),
            ex(f"Relato: «{RELATO_A}» ¿Qué hizo Lía cuando vieron la garza?", "Se quedó quieta y contó hasta diez", "El relato lo dice."),
            ex(f"Relato: «{RELATO_A}» ¿Qué hizo la garza al final?", "Abrió las alas y se fue volando", "Es el final del relato."),
        ],
        "reason": [
            ex("Un niño dice que Lía y su abuelo comieron pan en la orilla. ¿El relato lo dice?", "No", "Solo dice que llevaban pan."),
            ex("Una niña dice que Lía y su abuelo hablaron bajito. ¿El relato lo dice con claridad?", "No; solo dice que el abuelo pidió hablar bajito", "El relato cuenta lo que dijo el abuelo, pero no dice que hablaron bajito."),
        ],
        "challenge": [
            ex(f"Relato: «{RELATO_A}» Cuenta cuántas oraciones tiene el relato (separadas por punto).", "6", "Hay seis oraciones."),
            ex(f"Relato: «{RELATO_A}» Escribe un detalle explícito del relato que no hayamos preguntado.", "Por ejemplo, caminaron al amanecer", "Se acepta un detalle que esté escrito."),
        ],
    },
    context=[ex("La educadora tradicional cuenta un relato y un niño agrega: «y además tenían un perro». La educadora no lo dijo. ¿Qué debe decirle un compañero?", "Que eso el relato no lo dijo", "Solo se afirma lo dicho en el relato.")],
    selfcheck=[
        ex("¿Qué es un detalle explícito?", "Uno dicho claramente en el relato", "Es el que está escrito o contado."),
        ex(f"Relato: «{RELATO_A}» ¿Qué dice el relato que Lía y su abuelo vieron en la orilla?", "Una garza blanca", "El relato nombra una garza blanca en la orilla."),
        ex("¿Se inventan datos que el relato no dice?", "No", "Se pregunta si faltan."),
    ],
    open_task=task(
        "Un adulto te lee el relato de práctica «" + RELATO_A + "». Escribe o dibuja tres detalles que el relato dice claramente y subraya en el texto de dónde los sacaste. Además escribe un detalle que el relato no dice y que te gustaría preguntar. Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿qué información cultural importante tienen los relatos de su pueblo?",
        "Detalles: llevaban pan y manta; vieron una garza blanca; contó hasta diez. No dice cómo se llama el río. Mi pregunta: ¿qué información cultural importante tienen los relatos del pueblo?",
        ["recupera detalles explícitos", "separa lo que no dice el relato", "pregunta al educador/a tradicional"],
        ["tres detalles", "un detalle no dicho", "pregunta escrita"],
        ["inventar datos", "no revisar el texto"],
        "Reconoce los detalles recuperados y la honestidad de decir lo que el relato no dice.",
    ),
    reinforce="Elige un cuento corto de tu casa y encuentra tres detalles que se digan claramente.",
    extend="Escribe una pregunta que el relato de práctica no responde y a quién se la harías.",
)

register(
    OA4, 3,
    materials="Este cuaderno y lápiz. Relato de práctica: «" + RELATO_A + "»",
    use="Aprenderé a relacionar lo que me pasó con un relato, sin reemplazar lo que dice el relato. Sirve para comprender mejor y a la vez respetar el relato.",
    prior=["Sé qué dice el relato.", "Sé contar algo que me pasó."],
    explain=[
        "Relacionar un relato con tu vida es buscar algo parecido que te haya pasado. En el relato de práctica, Lía se queda quieta para no asustar a la garza. Quizás tú te quedaste quieto para ver un pajarito. Eso es una relación.",
        "Cuando relacionas, cuidas dos cosas. Primero, dices lo que dice el relato. Segundo, dices lo que te pasó a ti, como una experiencia aparte. Nunca reemplazas el relato con tu experiencia ni cambias lo que dijo la persona que lo contó.",
        "Una buena frase es: «En el relato, Lía se queda quieta. A mí me pasó que me quedé quieto para mirar un pajarito». Así se ve cuál es el relato y cuál es tu experiencia. Si el relato es de un pueblo, además dices de quién es.",
    ],
    vocab=[("relacionar", "unir el relato con algo que viví"), ("experiencia", "lo que me pasó"), ("reemplazar", "poner una cosa en lugar de otra"), ("parecido", "algo que se asemeja a otra cosa"), ("aparte", "separado, que no se mezcla")],
    worked=[
        {"title": "Relacionar con cuidado", "problem": f"Relato: «{RELATO_A}» Mateo dice: «En el relato, Lía se queda quieta. Yo me quedé quieto para ver un pajarito». ¿Relaciona bien?", "steps": ["Dice primero lo que dice el relato.", "Luego cuenta su experiencia.", "Las dos partes quedan separadas."], "answer": "Sí, relaciona con cuidado"},
        {"title": "Reemplazar el relato", "problem": "Ema dice: «En el relato, Lía va al río con su perro» porque a ella le pasó eso. ¿Qué hizo mal?", "steps": ["El relato dice que fue con su abuelo.", "Ema cambió el relato por su experiencia.", "Debió contar su experiencia aparte."], "answer": "Reemplazó el relato con su experiencia"},
    ],
    mistakes=[
        {"wrong": "Cambiar el relato para que se parezca a mi vida.", "why": "El relato deja de ser el que se contó.", "fix": "Cuenta tu experiencia aparte."},
        {"wrong": "Hablar solo de mi experiencia y olvidar el relato.", "why": "No se relaciona; se cambia de tema.", "fix": "Di primero qué dice el relato."},
    ],
    tiers={
        "recovery": [
            ex(f"Relato: «{RELATO_A}» ¿Qué hace Lía cuando ven la garza?", "Se queda quieta", "El relato lo dice."),
            ex("¿Qué haces primero al relacionar: decir lo que dijo el relato o contar tu experiencia?", "Decir lo que dijo el relato", "Primero se nombra el relato."),
            ex("¿Reemplazas el relato con tu experiencia?", "No", "Se mantienen separados."),
        ],
        "understand": [
            ex("¿Qué es una experiencia?", "Lo que me pasó", "Es algo vivido por mí."),
            ex("¿Por qué conviene separar el relato de tu experiencia?", "Para no cambiar el relato", "Así queda claro cuál es cuál."),
            ex("¿Cómo sabemos de quién es un relato de un pueblo?", "Preguntando a quien lo cuenta", "Quien lo cuenta nombra su origen."),
        ],
        "apply": [
            ex(f"Relato: «{RELATO_A}» Escribe una frase que empiece con «En el relato, Lía…» y diga qué hace.", "Cualquier frase que diga algo que Lía hizo en el relato", "Debe usar lo que dice el relato."),
            ex("Completa: «A mí me pasó que me quedé quieto para mirar _______». Escribe algo que tú podrías mirar.", "Un pajarito, un bicho o cualquier cosa", "Es una experiencia propia."),
            ex("Ordena: a) mi experiencia, b) lo que dice el relato. ¿Qué va primero?", "b", "Primero el relato."),
        ],
        "reason": [
            ex("Un niño cuenta una historia suya larga y no nombra el relato. ¿Relacionó bien?", "No", "Solo habló de sí mismo."),
            ex("Una niña dice: «El relato dice que el abuelo habló bajito. Yo hablo bajito en la biblioteca». ¿Relaciona bien?", "Sí", "Nombra el relato y luego su experiencia."),
        ],
        "challenge": [
            ex("Escribe una frase de dos partes: lo que dice el relato de la garza y lo que te pasó a ti.", "Cualquier frase con las dos partes", "Debe tener relato y experiencia por separado."),
            ex("Hay 4 niños que relacionan el relato con su vida y 2 que solo cuentan su historia. ¿Cuántos relacionaron bien?", "4", "Los que nombraron el relato y su experiencia."),
        ],
    },
    context=[ex("La educadora tradicional termina un relato y pide que cuenten algo parecido de su vida. Tomás cuenta la suya, pero no menciona el relato. ¿Qué le falta?", "Nombrar qué dice el relato", "Debe unir su experiencia con el relato.")],
    selfcheck=[
        ex("¿Qué va primero al relacionar?", "Lo que dice el relato", "Se parte desde el relato."),
        ex("¿Reemplazas el relato por tu experiencia?", "No", "Se mantienen aparte."),
        ex("¿A quién preguntas de quién es el relato?", "A quien lo cuenta", "Quien lo cuenta lo sabe."),
    ],
    open_task=task(
        "Un adulto de tu casa te lee el relato «" + RELATO_A + "». Escribe o dibuja una cosa parecida que te haya pasado a ti (por ejemplo, quedarte quieto para mirar un animal o caminar con un familiar). Escribe una frase con dos partes: «En el relato…» y «A mí me pasó…». Luego pregunta al educador/a tradicional o a la comunidad cómo puedes relacionar un relato del pueblo con tu vida sin cambiarlo.",
        "En el relato, Lía se queda quieta frente a la garza. A mí me pasó que me quedé quieto frente a una mariposa. Mi pregunta: ¿cómo relaciono un relato del pueblo con mi vida sin cambiarlo?",
        ["usa dos partes: relato y experiencia", "no reemplaza el relato", "pregunta a la comunidad"],
        ["frase de dos partes", "dibujo", "pregunta escrita"],
        ["cambiar el relato", "olvidar el relato"],
        "Valora la frase de dos partes y recuerda la pregunta a quien cuenta relatos.",
    ),
    reinforce="Cuenta un cuento de tu casa y luego algo parecido que te haya pasado.",
    extend="Relaciona el relato de práctica con dos experiencias distintas, cada una en su frase.",
)

register(
    OA4, 4,
    materials="Este cuaderno y lápiz. Relato de práctica: «" + RELATO_A + "»",
    use="Aprenderé a explicar qué aprendí de un relato y qué debo preguntar, reconociendo mis límites. Sirve para ser honesto sobre lo que sé y lo que no sé.",
    prior=["Sé decir qué dice un relato.", "Sé que hay cosas que solo la comunidad conoce."],
    explain=[
        "Al terminar un relato, puedes explicar qué aprendiste con tus palabras. Por ejemplo: «Aprendí que hay que hablar bajito cerca de los animales para no asustarlos». Eso lo sacas del relato de práctica, no lo inventas.",
        "También puedes decir qué no sabes y debes preguntar. Reconocer límites es decir con honestidad: «Esto no lo sé». En los relatos de un pueblo, hay palabras, nombres y significados que solo conoce la comunidad. No los inventas.",
        "Una buena despedida del relato tiene tres cosas: lo que aprendí, lo que debo preguntar y una palabra de agradecimiento. Así muestras que entendiste y que respetas a quien compartió el relato.",
    ],
    vocab=[("aprender", "saber algo que antes no sabía"), ("límite", "lo que no sé o no me corresponde"), ("honestidad", "decir la verdad sobre lo que sé"), ("preguntar", "pedir información a quien sabe"), ("agradecer", "decir gracias")],
    worked=[
        {"title": "Qué aprendí", "problem": f"Relato: «{RELATO_A}» Escribe qué aprendiste.", "steps": ["Releo la parte del abuelo.", "Dice que hay que hablar bajito para no asustar.", "Aprendí a hablar bajito cerca de los animales."], "answer": "Que hay que hablar bajito cerca de los animales para no asustarlos"},
        {"title": "Qué debo preguntar", "problem": "Escuchaste un relato de un pueblo con una palabra que no conoces. ¿Qué dices?", "steps": ["No invento qué significa.", "Digo: «No sé qué significa esta palabra».", "La pregunto a quien lo contó."], "answer": "Reconozco que no lo sé y pregunto a quien lo contó"},
    ],
    mistakes=[
        {"wrong": "Inventar el significado de una palabra que no conoces.", "why": "Puede ser falso y faltar el respeto.", "fix": "Di «no lo sé» y pregunta."},
        {"wrong": "No agradecer a quien contó el relato.", "why": "Quien cuenta comparte algo valioso.", "fix": "Termina con un gracias."},
    ],
    tiers={
        "recovery": [
            ex("Al terminar un relato, ¿qué dices a quien lo contó?", "Gracias", "Se agradece a quien comparte."),
            ex("Si no sabes algo, ¿lo inventas o dices «no lo sé»?", "Digo «no lo sé»", "La honestidad evita errores."),
            ex("¿A quién le preguntas lo que no sabes de un relato del pueblo?", "A quien lo cuenta", "Él o ella lo sabe."),
        ],
        "understand": [
            ex("¿Qué es un límite al aprender?", "Lo que no sé o no me corresponde", "Es honestidad sobre lo que sé."),
            ex("¿Por qué no inventas el significado de una palabra del relato?", "Porque puede ser falso", "Solo quien la conoce sabe el significado."),
            ex("¿Qué tres cosas tiene una buena despedida del relato?", "Lo que aprendí, lo que debo preguntar y un gracias", "Esas son las tres partes."),
        ],
        "apply": [
            ex(f"Relato: «{RELATO_A}» Completa: «Aprendí que hay que ______ bajito cerca de los animales».", "Hablar", "El abuelo dijo que hay que hablar bajito."),
            ex("Escribe una pregunta sobre el relato de práctica que no puedas responder con el texto.", "Por ejemplo: ¿cómo se llama el río?", "Se acepta una pregunta que el relato no responde."),
            ex("Ordena la despedida: primero lo que aprendí, después lo que pregunto y al final el gracias. a) gracias, b) pregunta, c) lo que aprendí. Escribe las letras en ese orden.", "c, b, a", "Aprendí, pregunto y agradezco."),
        ],
        "reason": [
            ex("Un niño dice que entendió todo el relato del pueblo, pero no sabe qué significa una palabra. ¿Es honesto?", "No del todo", "Debería decir qué no sabe."),
            ex("Una niña dice «No sé qué significa esta palabra, ¿me ayuda?». ¿Hizo bien?", "Sí", "Reconoció su límite y preguntó."),
        ],
        "challenge": [
            ex("Hay 5 niños en el grupo. Cada uno dice una cosa que aprendió y una cosa que debe preguntar. ¿Cuántas frases dicen en total?", "10", "2 + 2 + 2 + 2 + 2 = 10."),
            ex("Escribe una frase que diga una cosa que aprendiste y una que debes preguntar.", "Cualquier frase con las dos ideas", "Debe incluir aprendizaje y pregunta."),
        ],
    },
    context=[ex("La educadora tradicional termina su relato. Un niño dice: «Ya sé todo sobre ese pueblo». ¿Qué le dirías?", "Que hay mucho más que preguntar a la comunidad", "Un relato no enseña todo sobre un pueblo.")],
    selfcheck=[
        ex("¿Qué dices cuando no sabes?", "No lo sé", "Reconoces tu límite."),
        ex("¿Qué dices a quien contó el relato?", "Gracias", "Agradeces a quien comparte."),
        ex("¿A quién preguntas lo que no sabes?", "A quien lo cuenta", "Quien lo cuenta lo sabe."),
    ],
    open_task=task(
        "Un adulto te lee de nuevo el relato «" + RELATO_A + "». Escribe o dibuja una cosa que aprendiste y una pregunta que no puedes responder solo con el relato (por ejemplo, cómo se llama el río). Termina con un agradecimiento para quien lo leyó. Luego pregunta al educador/a tradicional o a la comunidad: ¿qué relato del pueblo puedo escuchar y qué debo preguntar después de escucharlo?",
        "Aprendí que hay que hablar bajito para no asustar a los animales. Pregunta: ¿cómo se llama el río? Gracias por leerlo. Mi pregunta: ¿qué relato del pueblo puedo escuchar?",
        ["dice qué aprendió", "dice qué debe preguntar", "agradece"],
        ["frase o dibujo", "pregunta escrita"],
        ["inventar respuestas", "no agradecer"],
        "Valora la honestidad de reconocer límites y el agradecimiento.",
    ),
    reinforce="Después de escuchar un cuento, di una cosa que aprendiste y una que quieres preguntar.",
    extend="Haz un cartel con tres frases: lo que aprendí, lo que pregunto y gracias.",
)

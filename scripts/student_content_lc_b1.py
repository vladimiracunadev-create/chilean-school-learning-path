"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF01 (textos orales de tradición indígena, fortalecimiento de la lengua).

Los textos de práctica de este cuaderno están en castellano y fueron creados para entrenar
habilidades (escuchar, seguir un ritmo, comprender con el cuerpo). No pertenecen a ningún pueblo.
Los textos tradicionales, su lengua, su entonación y su ocasión de uso los enseña el educador/a
tradicional o la comunidad; este cuaderno no inventa palabras ni gramática de ninguna lengua.
"""
from __future__ import annotations

from student_lessons import ex, register

OA = "LC01 OA LF01"

# Textos de práctica originales en castellano (compartidos con los demás módulos lc_b*).
CANCION = "Sube, sube, la luna sube, / sube, sube, y el niño ve. / Baja, baja, la luna baja, / baja, baja, y el niño ve."
POEMA = "El agua canta bajito / cuando baja por la piedra. / El agua canta bajito / y la tarde se queda quieta."
ADIV_ARBOL = "Tengo hojas y no soy libro; tengo ramas y no soy río; doy sombra en el patio y en mi tronco juega el niño."
ADIV_NUBE = "Viajo sin patas por el cielo; a veces soy gris y a veces blanca; cuando me pongo pesada, suelto gotas."
TRABA = "Tres tazas tibias toma Tomás, tomando tazas tibias tres."
RONDA = "Una vuelta a la derecha, / una vuelta a la izquierda, / aplaudo una, aplaudo dos, / y me siento en la rueda."
PRACTICA = "Texto de práctica en castellano creado para este cuaderno; no pertenece a ningún pueblo."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- Clase 1
register(
    OA, 1,
    materials="Este cuaderno, lápiz y tus manos para marcar el ritmo. Los textos de práctica están escritos aquí en castellano; los textos tradicionales los trae el educador/a tradicional.",
    use="Aprenderé a escuchar un texto oral completo, sin interrumpir, y a fijarme en su ritmo, en quién lo dice y en cuándo se usa. Sirve para respetar a quien comparte un canto, un poema o una adivinanza.",
    prior=["Sé quedarme en silencio un momento.", "Sé decir si algo suena rápido o lento."],
    explain=[
        "Un texto oral es un texto que se dice con la voz: una canción, un poema, una adivinanza o un trabalenguas. No se lee con los ojos, se escucha con los oídos. Por eso lo primero es escucharlo entero, de principio a fin, sin cortar a quien habla.",
        "Cuando escuchas, fíjate en tres cosas. El ritmo es lo que se repite como los golpes de un tambor: lento, rápido, pausas. La voz es quién habla y cómo lo hace: suave, fuerte, cantada. La situación es cuándo y dónde se dice ese texto.",
        "Los textos de los pueblos originarios tienen dueños: una familia, una comunidad, un educador o educadora tradicional. Tú los escuchas con respeto y después preguntas. No cambias palabras ni las inventas para completar lo que no entendiste.",
    ],
    vocab=[("texto oral", "texto que se dice con la voz y se escucha"), ("ritmo", "lo que se repite con pausas y golpes, como una música"), ("voz", "la forma en que alguien dice un texto"), ("situación", "cuándo y dónde se dice un texto"), ("educador/a tradicional", "persona de la comunidad que enseña la lengua y la cultura")],
    worked=[
        {"title": "Escuchar entero", "problem": f"Un adulto dice despacio este texto de práctica: «{CANCION}». ¿Qué haces durante la primera escucha?", "steps": ["Me siento quieto y miro a quien habla.", "No canto ni hablo todavía.", "Espero a que termine el último verso.", "Recién después digo qué escuché."], "answer": "Escucho el texto completo en silencio y respondo al final"},
        {"title": "Ritmo, voz y situación", "problem": f"Escuchas este poema de práctica: «{POEMA}». Una voz lo dice bajito y despacio, al caer la tarde. ¿Cómo es el ritmo, la voz y la situación?", "steps": ["El ritmo es lento porque se dice despacio.", "La voz es suave porque habla bajito.", "La situación es la tarde, cuando el día termina."], "answer": "Ritmo lento, voz suave, situación: la tarde"},
    ],
    mistakes=[
        {"wrong": "Cantar encima de quien enseña la canción.", "why": "No dejas escuchar la voz de quien comparte el texto.", "fix": "Escucha todo en silencio y canta solo cuando la persona lo invite."},
        {"wrong": "Inventar palabras para llenar lo que no se entendió.", "why": "Esas palabras no son del texto ni de la comunidad.", "fix": "Di «no entendí esta parte» y pregunta al educador/a tradicional."},
    ],
    tiers={
        "recovery": [
            ex("Una educadora tradicional comparte una canción. ¿Qué haces primero: escuchar completa o cantar de inmediato?", "Escuchar completa", "Primero se escucha; cantar encima no deja oír a quien enseña."),
            ex("Ordena estos pasos: a) respondo, b) escucho el texto entero, c) me siento y miro a quien habla, d) pienso en lo que oí. Escribe las letras en orden.", "c, b, d, a", "Primero me preparo, luego escucho, después pienso y al final respondo."),
            ex("Don Luis canta una canción y Ema la escucha en silencio. ¿Quién habla y quién escucha?", "Habla Don Luis; escucha Ema", "Quien canta es quien habla y quien está en silencio escucha."),
        ],
        "understand": [
            ex("Una voz dice: «pum, pa, pa, pum, pa, pa». ¿Qué parte se repite?", "pum, pa, pa", "El grupo de sonidos aparece dos veces igual."),
            ex("Un texto se dice muy despacio y con pausas largas. ¿Su ritmo es lento o rápido?", "Lento", "Las pausas largas y el decir despacio dan un ritmo lento."),
            ex("¿Cuál de estas cosas es la «situación» de un texto: la tarde en que se canta, el color del papel o el largo de la hoja?", "La tarde en que se canta", "La situación es cuándo y dónde se dice el texto."),
        ],
        "apply": [
            ex(f"Cuenta cuántas veces aparece la palabra «sube» (con mayúscula o minúscula) en este texto de práctica: «{CANCION}»", "5", "Aparece 3 veces en el primer verso y 2 en el segundo, y 3 + 2 = 5."),
            ex(f"En este texto de práctica: «{RONDA}», ¿cuántos versos hay? Los versos están separados por una barra (/).", "4", "Hay tres barras que separan cuatro versos."),
            ex(f"En el poema de práctica «{POEMA}», ¿qué verso se repite igual: el primero o el segundo?", "El primero", "«El agua canta bajito» aparece al principio y en el tercer verso."),
        ],
        "reason": [
            ex("Sofía escuchó solo el comienzo de una adivinanza y ya contestó. La adivinanza continuaba con más pistas. ¿Por qué fue mejor escucharla completa?", "Porque las pistas finales pueden cambiar la respuesta", "Sin oír todo, no se tienen todas las pistas."),
            ex("Un niño no entendió una palabra de la canción y puso otra que sonaba parecida. ¿Qué debió hacer?", "Preguntar al educador/a tradicional", "Solo quien enseña el texto sabe cuál es la palabra correcta."),
        ],
        "challenge": [
            ex(f"Escucha este texto de práctica: «{TRABA}». ¿Cuántas palabras tiene en total? Cuenta una por una.", "9", "Son Tres, tazas, tibias, toma, Tomás, tomando, tazas, tibias y tres: 9 palabras."),
            ex("Inventa una frase con las palabras ritmo, voz y situación para decir qué observaste en un texto. Escribe una frase que las incluya a las tres.", "Cualquier frase que contenga ritmo, voz y situación", "Se acepta toda frase que use las tres palabras con sentido."),
        ],
    },
    context=[ex("Tu curso invita a un educador tradicional. Antes de que empiece a cantar, un compañero susurra y se ríe. ¿Qué le dirías para cuidar la escucha?", "Que escuche en silencio hasta que termine", "Se escucha completo y sin ruido para respetar a quien comparte su canto.")],
    selfcheck=[
        ex("¿Cómo se llama la forma en que alguien dice un texto: suave, fuerte o cantada?", "Voz", "La forma de decir el texto es la voz."),
        ex("¿Cuántas veces escuchas un texto antes de responder la primera vez: una vez completa o a medias?", "Una vez completa", "La primera escucha debe ser del texto entero."),
        ex("¿Quién conoce de verdad la palabra correcta de un texto tradicional?", "El educador/a tradicional o la comunidad", "Ellos son los dueños y quienes enseñan el texto."),
    ],
    open_task=task(
        "Pide a un adulto de tu casa que te diga en voz alta una de estas tres cosas, sin que tú digas nada hasta el final: la adivinanza «" + ADIV_NUBE + "», el poema «" + POEMA + "» o la ronda «" + RONDA + "». Después dibuja o cuenta con tus palabras cuál es el ritmo (lento o rápido), cómo era la voz y cuándo lo dirías. Cuando venga el educador/a tradicional, pregúntale qué texto de su pueblo puedes escuchar y cuándo se dice.",
        "Escuché la ronda entera. El ritmo era rápido, la voz alegre y la diría en el patio, jugando. Voy a preguntar al educador/a tradicional qué ronda de su pueblo puedo escuchar.",
        ["escucha el texto completo sin interrumpir", "dice ritmo, voz y situación", "escribe una pregunta para el educador/a tradicional"],
        ["dibujo o relato breve", "pregunta anotada para el educador/a tradicional"],
        ["responder antes de que termine el texto", "inventar palabras que no se escucharon"],
        "Reconoce que escuchó completo y pide que agregue una pregunta honesta a quien conoce el texto tradicional.",
    ),
    reinforce="Escucha una canción de tu casa de principio a fin sin cantar y di si su ritmo es lento o rápido.",
    extend="Cuenta las pausas que oyes en un poema que te lea un adulto y marca cada una con una rayita.",
)

# ---------------------------------------------------------------- Clase 2
register(
    OA, 2,
    materials="Este cuaderno, lápiz y tus manos para dar palmas. Los textos de práctica están escritos en castellano.",
    use="Aprenderé a reconocer una repetición en un texto oral y a participar solo en el tramo que me corresponde. Sirve para cantar o decir juntos sin pisar la voz de otro.",
    prior=["Sé escuchar un texto completo en silencio.", "Sé dar palmas siguiendo un ritmo."],
    explain=[
        "Muchos textos orales repiten palabras, versos o sonidos. La repetición ayuda a recordar el texto y a seguirlo con el grupo. Cuando oyes que algo vuelve igual, ya sabes que puedes participar en ese momento.",
        "Un tramo es una parte del texto. A veces quien guía canta un tramo y el grupo responde con el tramo que se repite. Participar bien es esperar tu turno: entras cuando te corresponde y callas cuando canta otro.",
        "Antes de participar con un texto tradicional, pregunta cuál es el tramo que puedes repetir. Hay partes que solo corresponde decir a ciertas personas o en ciertas ocasiones. Eso lo explica el educador o educadora tradicional.",
    ],
    vocab=[("repetición", "parte que vuelve igual en un texto"), ("tramo", "una parte del texto"), ("turno", "momento en que te toca participar"), ("guía", "persona que dirige el canto o el juego"), ("responder", "decir el tramo que corresponde al grupo")],
    worked=[
        {"title": "Encontrar la repetición", "problem": f"Mira este texto de práctica: «{CANCION}». ¿Qué verso se repite igual?", "steps": ["Leo el segundo verso: «sube, sube, y el niño ve».", "Leo el cuarto verso: «baja, baja, y el niño ve».", "Las palabras «y el niño ve» vuelven al final de los dos versos."], "answer": "Se repite «y el niño ve»"},
        {"title": "Esperar mi turno", "problem": "La guía dice: «Un, dos, tres, palma». El grupo responde: «palma». ¿Cuándo dices tú «palma»?", "steps": ["Escucho a la guía decir su parte completa.", "Espero a que termine de decir «palma» con ella.", "Entonces respondo «palma» con el grupo."], "answer": "Después de que la guía termina su parte"},
    ],
    mistakes=[
        {"wrong": "Cantar también la parte de la guía.", "why": "Cada voz tiene su tramo y se mezclan.", "fix": "Canta solo el tramo que se repite, el del grupo."},
        {"wrong": "Participar en un tramo que no te enseñaron.", "why": "Hay partes que solo corresponde decir a ciertas personas.", "fix": "Pregunta al educador/a tradicional cuál tramo puedes decir."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama la parte que vuelve igual en una canción?", "Repetición", "Lo que vuelve igual es la repetición."),
            ex("La guía canta el primer tramo y el grupo el segundo. Si eres del grupo, ¿cuándo entras?", "Cuando termina la guía", "El grupo entra después de que la guía termina."),
            ex(f"En este texto de práctica: «{RONDA}», ¿qué verso empieza con las palabras «una vuelta»? Escribe cuántos versos empiezan así.", "2", "Los dos primeros versos empiezan con «una vuelta»."),
        ],
        "understand": [
            ex("¿Para qué sirve que un texto tenga repeticiones?", "Para recordarlo y seguirlo con el grupo", "Lo que vuelve igual se aprende más fácil."),
            ex("¿Qué es un tramo de un texto?", "Una parte del texto", "Un tramo es una parte, no todo el texto."),
            ex("Si no sabes cuál tramo te toca, ¿a quién le preguntas: al educador/a tradicional o a un compañero que adivina?", "Al educador/a tradicional", "Es quien sabe qué parte corresponde decir."),
        ],
        "apply": [
            ex(f"En el texto de práctica «{TRABA}», ¿cuántas veces se repite la palabra «tazas»?", "2", "«tazas» aparece en «Tres tazas» y en «tomando tazas»."),
            ex(f"En «{POEMA}», ¿cuántas veces aparece la palabra «agua»?", "2", "«El agua» abre el primer verso y el tercero."),
            ex("La guía dice «¡Hop!» y el grupo responde «¡Hop!». Si la guía dice «¡Hop!» tres veces, ¿cuántas veces responde el grupo?", "3", "Responde una vez por cada «¡Hop!» de la guía."),
        ],
        "reason": [
            ex("Ana canta fuerte el tramo de la guía y el grupo no se escucha. ¿Qué debería hacer Ana?", "Callar y esperar su turno", "El tramo de la guía no es de Ana; debe esperar el suyo."),
            ex("Un niño dice que como se repite una parte, puede cantarla en cualquier momento. ¿Es cierto?", "No", "Se repite en ciertos momentos y hay que esperar la señal."),
        ],
        "challenge": [
            ex(f"En «{CANCION}», cuenta cuántas veces aparece la frase «el niño ve».", "2", "Aparece al final del segundo y del cuarto verso."),
            ex("Escribe tú un verso de práctica de dos palabras que se repita dos veces, como «sube, sube». Escribe el verso repetido.", "Cualquier par de palabras repetido, por ejemplo «baja, baja»", "Se acepta un verso con la misma palabra o frase dicha dos veces."),
        ],
    },
    context=[ex("El educador tradicional canta un tramo y todos responden con un tramo que se repite. Marta no sabe si el tramo de respuesta le corresponde. ¿Qué hace?", "Pregunta cuál tramo le corresponde", "Se pregunta antes de participar en un texto tradicional.")],
    selfcheck=[
        ex("¿Qué es un tramo?", "Una parte del texto", "El tramo es una parte, no el texto entero."),
        ex("Si el grupo responde después de la guía, ¿tú entras antes o después de que ella termina?", "Después", "Se espera a que la guía termine su parte."),
        ex("¿Quién decide qué tramo puedes repetir de un texto tradicional?", "El educador/a tradicional o la comunidad", "Ellos conocen a quién corresponde cada parte."),
    ],
    open_task=task(
        "Con un adulto de tu casa juega a la ronda de práctica: «" + RONDA + "». El adulto es la guía y dice los dos primeros versos; tú respondes dando una palmada en cada «aplaudo». Luego subraya en el texto la parte que se repite y anota quién dijo cada tramo. Pregunta al educador/a tradicional o a la comunidad qué tramo de un texto de su pueblo corresponde decir al grupo.",
        "La guía dijo los dos primeros versos y yo di dos palmadas en «aplaudo una, aplaudo dos». Subrayé «una vuelta» porque se repite. Voy a preguntar qué tramo puedo decir en un canto de la comunidad.",
        ["identifica una repetición", "espera su turno", "pregunta qué tramo corresponde"],
        ["texto subrayado", "nota de quién dijo cada tramo"],
        ["cantar encima de la guía", "participar sin saber el tramo"],
        "Valora que esperó su turno y que preguntó antes de participar en un texto tradicional.",
    ),
    reinforce="Busca en una canción de tu casa una repetición y marca con una palmada cada vez que vuelve.",
    extend="Inventa una ronda de dos versos en castellano con una repetición y enséñasela a un adulto sin decir que es de ningún pueblo.",
)

# ---------------------------------------------------------------- Clase 3
register(
    OA, 3,
    materials="Este cuaderno, lápiz y espacio para mover los brazos. Los textos de práctica están escritos en castellano.",
    use="Aprenderé a mostrar con el cuerpo y con gestos una idea de un texto oral. Sirve para comprender un texto aunque no conozca todas sus palabras.",
    prior=["Sé escuchar un texto completo.", "Sé hacer un gesto con las manos o la cara."],
    explain=[
        "Comprender un texto no es solo repetir palabras. También puedes mostrar lo que entendiste con el cuerpo: subes los brazos si el texto dice que algo sube, los bajas si algo baja, abres las manos si algo se reparte.",
        "Un gesto bueno muestra una idea del texto, no una burla. No hay que exagerar ni imitar mal a las personas ni a un pueblo. Haces un movimiento sencillo, claro y respetuoso, que cualquiera podría entender.",
        "Para el texto de práctica, la idea puede ser «la luna sube y baja». Para un texto tradicional, el educador o educadora te dice qué ideas conviene mostrar y cuáles gestos no corresponden. Pregunta antes de inventar un gesto.",
    ],
    vocab=[("gesto", "movimiento de las manos, los brazos o la cara que muestra una idea"), ("idea del texto", "lo principal que dice el texto"), ("comprender", "entender de qué trata el texto"), ("respetuoso", "que cuida a las personas y a lo que se muestra"), ("mostrar", "hacer ver una idea con el cuerpo")],
    worked=[
        {"title": "Un gesto para «sube»", "problem": f"En el texto de práctica «{CANCION}» el primer verso dice «Sube, sube, la luna sube». ¿Qué gesto muestra esa idea?", "steps": ["La palabra clave es «sube».", "Algo que sube va hacia arriba.", "Subo las manos desde abajo hacia arriba, despacio."], "answer": "Subir los brazos despacio"},
        {"title": "Gesto respetuoso o burla", "problem": "Tomás quiere mostrar «el agua canta» y mueve la boca de forma exagerada para burlarse de cómo habla alguien. ¿Es buen gesto?", "steps": ["El texto dice que el agua canta, no habla de personas.", "Burlarse de cómo habla alguien falta el respeto.", "Mejor mueve las manos como ondas de agua."], "answer": "No; mejor mover las manos como ondas"},
    ],
    mistakes=[
        {"wrong": "Hacer un gesto que se burla de una persona o de un pueblo.", "why": "Muestra falta de respeto y no comprende la idea del texto.", "fix": "Haz un gesto sencillo que muestre solo la idea del texto."},
        {"wrong": "Inventar un gesto «tradicional» sin preguntar.", "why": "Puede ser un gesto que no corresponde a ese pueblo.", "fix": "Pregunta al educador/a tradicional qué gestos se usan."},
    ],
    tiers={
        "recovery": [
            ex("Un texto dice que algo baja. ¿Qué haces con los brazos: subirlos o bajarlos?", "Bajarlos", "El gesto sigue la idea de bajar."),
            ex("¿Para qué sirve un gesto en un texto oral?", "Para mostrar una idea del texto", "El gesto muestra lo que entendiste."),
            ex("El texto dice «el agua canta bajito». ¿Qué gesto sirve: manos como ondas o puños cerrados?", "Manos como ondas", "Las ondas muestran el agua."),
        ],
        "understand": [
            ex("¿Es respetuoso imitar de forma exagerada a una persona para reírse?", "No", "Burlarse falta el respeto."),
            ex("¿Se puede comprender un texto aunque no conozcas todas sus palabras si miras los gestos y el contexto?", "Sí, en parte", "El gesto y la situación ayudan a entender, pero no reemplazan lo que dice el texto."),
            ex("¿Qué es la idea del texto: lo principal que dice o la primera letra?", "Lo principal que dice", "La idea es lo central del texto."),
        ],
        "apply": [
            ex(f"En «{RONDA}», ¿qué gesto muestra «aplaudo una, aplaudo dos»: dar dos palmadas o saltar tres veces?", "Dar dos palmadas", "El verso dice aplaudo una y aplaudo dos."),
            ex(f"En «{RONDA}», ¿qué movimiento haces en «una vuelta a la derecha»?", "Girar hacia la derecha", "El verso indica girar a la derecha."),
            ex(f"En «{CANCION}», ¿qué gesto elegirías para «baja, baja, la luna baja»?", "Bajar las manos", "«Baja» se muestra yendo hacia abajo."),
        ],
        "reason": [
            ex("Un compañero muestra con el cuerpo «la luna sube» agachándose. ¿Su gesto muestra bien la idea? ¿Por qué?", "No, porque agacharse es ir hacia abajo y sube es hacia arriba", "El gesto debe ir en la misma dirección que dice el texto."),
            ex("Dos niños muestran «el agua canta» de forma distinta, pero ambos con manos que fluyen. ¿Puede haber más de un gesto bueno?", "Sí", "Distintos gestos sencillos pueden mostrar la misma idea."),
        ],
        "challenge": [
            ex(f"Cuenta cuántos gestos distintos necesitas para mostrar los cuatro versos de «{RONDA}» si cada verso pide un gesto diferente.", "4", "Hay cuatro versos y cada uno pide su gesto."),
            ex("Escribe un gesto sencillo y respetuoso para mostrar «la tarde se queda quieta».", "Por ejemplo, quedarse sin moverse con los brazos abajo", "Un gesto de quietud muestra la idea de quieta."),
        ],
    },
    context=[ex("En la clase, el educador tradicional cuenta qué muestra un canto. Lía quiere inventar un gesto nuevo para el canto. ¿Qué debe hacer antes?", "Preguntarle al educador/a tradicional", "El gesto de un texto tradicional lo define quien lo conoce.")],
    selfcheck=[
        ex("¿Un gesto debe burlarse o ser respetuoso?", "Respetuoso", "El gesto cuida a las personas."),
        ex("¿Qué movimiento muestra la palabra «sube»?", "Subir los brazos", "Subir es ir hacia arriba."),
        ex("¿Quién te dice si un gesto de un texto tradicional corresponde?", "El educador/a tradicional", "Es quien conoce el texto."),
    ],
    open_task=task(
        "Elige uno de estos versos de práctica: «el agua canta bajito», «una vuelta a la derecha» o «baja, baja, la luna baja». Inventa un gesto sencillo y respetuoso para mostrar la idea y muéstraselo a un adulto de tu casa. Dibuja el gesto y escribe qué idea muestra. Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿qué gestos acompañan los textos de tu pueblo y cuáles no se pueden cambiar?",
        "Elegí «una vuelta a la derecha». Giré hacia la derecha y dibujé una flecha. Mi pregunta: ¿qué gestos acompañan los cantos de la comunidad?",
        ["el gesto muestra la idea", "es respetuoso", "anota una pregunta al educador/a tradicional"],
        ["dibujo del gesto", "frase con la idea que muestra"],
        ["burlarse de personas", "inventar un gesto «tradicional»"],
        "Reconoce que el gesto muestra la idea y pide que la pregunta quede escrita para la comunidad.",
    ),
    reinforce="Muestra con el cuerpo tres palabras del texto «Sube, sube, la luna sube» sin hablar.",
    extend="Haz una secuencia de tres gestos para los versos 1, 3 y 4 de la ronda de práctica y enséñala a un adulto.",
)

# ---------------------------------------------------------------- Clase 4
register(
    OA, 4,
    materials="Este cuaderno y lápiz. Los textos de práctica y las situaciones están escritos aquí en castellano.",
    use="Aprenderé a relacionar un texto oral con algo que me ha pasado, y a volver siempre al texto. Sirve para comprender mejor sin quitarle el texto a su comunidad.",
    prior=["Sé decir qué idea tiene un texto.", "Sé contar algo que me pasó."],
    explain=[
        "Relacionar es unir lo que dice el texto con algo que tú has vivido. Si el texto habla del agua, puedes pensar en el día que jugaste con la lluvia. Eso te ayuda a comprender, porque conectas lo nuevo con algo que ya sabes.",
        "Después de contar tu experiencia, vuelve al texto. Lo que viviste ayuda a entender, pero no cambia lo que dice el texto. No digas que el texto es tuyo ni agregues partes como si fueran de la tradición.",
        "Un texto tradicional pertenece a una familia, a una comunidad o a un pueblo. Tú puedes decir «me hace pensar en…», pero no «esto es mío». Para saber más del texto, pregunta a quien lo comparte.",
    ],
    vocab=[("relacionar", "unir el texto con algo que viví o sé"), ("experiencia", "algo que me pasó o hice"), ("volver al texto", "mirar otra vez qué dice el texto"), ("apropiarse", "decir que algo de otros es solo mío"), ("tradición", "lo que una comunidad enseña de generación en generación")],
    worked=[
        {"title": "Relacionar y volver", "problem": f"El poema de práctica dice: «{POEMA}». Mateo recuerda una tarde en que escuchó llover. ¿Cómo relaciona sin apropiarse?", "steps": ["Dice: «El poema habla del agua; me recuerda una tarde de lluvia».", "Vuelve al poema y señala «El agua canta bajito».", "No dice que el poema es suyo."], "answer": "«Me hace pensar en la lluvia» y vuelve al verso del poema"},
        {"title": "Frase que se apropia", "problem": "Ema dice: «Este canto lo inventé yo y lo voy a cambiar». El canto es de una comunidad. ¿Qué está mal?", "steps": ["El canto pertenece a una comunidad.", "Ema dice que es suyo y quiere cambiarlo.", "Debe decir «me recuerda…» y preguntar si puede compartirlo."], "answer": "Se apropia del canto; debe preguntar a la comunidad"},
    ],
    mistakes=[
        {"wrong": "Contar tu experiencia y olvidar el texto.", "why": "Ya no se habla del texto, solo de ti.", "fix": "Después de tu experiencia, vuelve a decir qué dice el texto."},
        {"wrong": "Decir «esto es mío» de un texto tradicional.", "why": "El texto pertenece a una comunidad.", "fix": "Di «me hace pensar en…» y nombra de dónde viene el texto."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa relacionar un texto con una experiencia?", "Unir el texto con algo que viví", "Relacionar es conectar lo que dice el texto con lo vivido."),
            ex("Después de contar tu experiencia, ¿a qué vuelves?", "Al texto", "Siempre se vuelve a lo que dice el texto."),
            ex("¿Quién dice «me hace pensar en la lluvia»: alguien que relaciona o alguien que se apropia?", "Alguien que relaciona", "Esa frase conecta sin llamar mío al texto."),
        ],
        "understand": [
            ex("¿Por qué relacionar el texto con tu vida ayuda a comprender?", "Porque conectas lo nuevo con algo que ya sabes", "Lo conocido ayuda a entender lo nuevo."),
            ex("¿«Este canto es mío» es una frase que cuida o que se apropia?", "Que se apropia", "Dice que un texto de otros es solo tuyo."),
            ex("Un texto tradicional pertenece a una comunidad. ¿Puedes decir que lo inventaste tú?", "No", "No lo inventaste; te lo compartieron."),
        ],
        "apply": [
            ex("Lee la frase y elige la correcta: A) «Este canto es mío». B) «Este canto me hace pensar en mi abuela». Escribe la letra.", "B", "La frase B relaciona sin quedarse con el texto."),
            ex(f"El poema «{POEMA}» habla del agua. Escribe una frase que relacione el poema con algo que te haya pasado y que empiece con «Me hace pensar en».", "Cualquier frase que empiece con «Me hace pensar en» y nombre una experiencia", "Se acepta una frase que conecte el poema con una vivencia."),
            ex(f"Después de contar su experiencia con el canto «{CANCION}», ¿qué verso nombra Ana para volver al texto: «Sube, sube, la luna sube» o «Mi abuela hace pan»?", "«Sube, sube, la luna sube»", "El segundo no está en el texto."),
        ],
        "reason": [
            ex("Pedro cuenta tres historias suyas y no menciona el texto. ¿Qué le falta?", "Volver al texto", "Debe regresar a lo que dice el texto."),
            ex("Una compañera cambia las palabras de un canto de la comunidad «para que suene mejor». ¿Qué puede pasar con el canto?", "Se pierde cómo lo enseña la comunidad", "Cambiar el texto cambia lo que la comunidad quiere conservar."),
        ],
        "challenge": [
            ex("Une cada frase con su tipo: 1) «Me hace pensar en el mar». 2) «Ese poema es mío». 3) «Mi experiencia me ayuda a entender». Escribe los números de las que relacionan sin apropiarse.", "1 y 3", "Las frases 1 y 3 conectan sin apropiarse."),
            ex("Escribe una frase de dos partes: primero tu experiencia, después «y el texto dice…».", "Cualquier frase de dos partes con experiencia y «y el texto dice»", "Se acepta una frase que cuente algo vivido y vuelva al texto."),
        ],
    },
    context=[ex("La educadora tradicional comparte un canto. Después Rosa dice: «Lo voy a cantar en mi fiesta como si fuera mío». ¿Qué debería hacer Rosa antes?", "Preguntar si puede compartirlo y de quién es", "Un canto tradicional se comparte con permiso y diciendo de quién viene.")],
    selfcheck=[
        ex("¿Qué haces después de contar tu experiencia?", "Vuelvo al texto", "El texto es el centro."),
        ex("¿Qué frase cuida: «me hace pensar en…» o «esto es mío»?", "Me hace pensar en…", "Conecta sin apropiarse."),
        ex("¿A quién le preguntas para saber más de un texto tradicional?", "A quien lo comparte, el educador/a tradicional o la comunidad", "Ellos conocen el texto."),
    ],
    open_task=task(
        "Un adulto de tu casa te dice el poema de práctica «" + POEMA + "». Escribe o dibuja una cosa de tu vida que te recuerde ese poema y construye una frase con «Me hace pensar en…». Luego escribe cuál verso del poema te hizo pensar en eso. Anota una pregunta para el educador/a tradicional: ¿cómo puedo contar mi experiencia sobre un canto de la comunidad sin decir que es mío?",
        "Me hace pensar en la lluvia del invierno. El verso es «El agua canta bajito». Pregunta: ¿cómo cuento mi experiencia sin decir que el canto es mío?",
        ["relaciona con una experiencia propia", "vuelve a un verso del texto", "no se apropia del texto"],
        ["dibujo o frase", "verso señalado", "pregunta anotada"],
        ["olvidar el texto", "decir «esto es mío»"],
        "Reconoce que conectó con su experiencia y volvió al texto, y sugiere citar de quién es el texto.",
    ),
    reinforce="Cuenta una experiencia que te recuerde una canción y luego di un verso de la canción.",
    extend="Escribe dos frases con «Me hace pensar en…» para dos textos de práctica distintos de este cuaderno.",
)

# ---------------------------------------------------------------- Clase 5
register(
    OA, 5,
    materials="Este cuaderno y lápiz. Los textos de práctica están escritos para que un adulto los lea dos veces.",
    use="Aprenderé a escuchar otra vez un texto con un propósito, para notar una palabra, un sonido o una imagen. Sirve para comprender más cuando ya escuché el texto una primera vez.",
    prior=["Sé escuchar un texto completo.", "Sé decir de qué trata un texto."],
    explain=[
        "La primera vez escuchas todo el texto. La segunda vez escuchas con un propósito: buscas una cosa concreta. Puede ser una palabra que se repite, un sonido que te gusta o una imagen que se forma en tu cabeza.",
        "Un propósito sencillo ayuda a no perderse. Por ejemplo: «voy a contar cuántas veces suena la palabra sube». Mientras escuchas, haces una marca por cada vez. Al terminar, cuentas tus marcas y comparas con tu compañero.",
        "Si el texto es tradicional, el educador o educadora tradicional puede decirte qué conviene notar. Pregunta cuántas veces se puede reescuchar y si se puede grabar. Ningún texto de la comunidad se graba sin permiso.",
    ],
    vocab=[("reescuchar", "escuchar de nuevo el mismo texto"), ("propósito", "lo que busco al escuchar"), ("imagen", "lo que veo en mi mente cuando escucho"), ("marca", "rayita que hago para contar"), ("permiso", "autorización de la persona o comunidad para usar algo")],
    worked=[
        {"title": "Contar una palabra", "problem": f"Escuchas por segunda vez: «{CANCION}». Tu propósito es contar la palabra «baja». ¿Cuántas veces suena?", "steps": ["Hago una marca cada vez que oigo «baja».", "En el tercer verso suena 3 veces.", "En el cuarto verso suena 2 veces.", "3 + 2 = 5 marcas."], "answer": "5 veces"},
        {"title": "Elegir una imagen", "problem": f"En el poema «{POEMA}» quieres notar una imagen. ¿Cuál puedes elegir?", "steps": ["Leo los versos buscando algo que pueda ver.", "Veo el agua bajando por una piedra.", "Esa es la imagen que elijo."], "answer": "El agua bajando por la piedra"},
    ],
    mistakes=[
        {"wrong": "Escuchar por segunda vez sin buscar nada.", "why": "Sin propósito se pierde lo que querías notar.", "fix": "Antes de escuchar, di qué vas a buscar."},
        {"wrong": "Grabar a la educadora sin pedir permiso.", "why": "El texto y la voz son de la persona y de la comunidad.", "fix": "Pide permiso y pregunta si se puede registrar."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas veces escuchas el texto completo antes de buscar una palabra: una o ninguna?", "Una", "Primero se escucha entero y luego se reescucha."),
            ex("¿Qué es un propósito al escuchar?", "Lo que busco notar", "El propósito es la cosa concreta que busco."),
            ex("Si quieres contar una palabra, ¿haces una marca o grabas sin permiso?", "Haces una marca", "Contar con marcas es respetuoso y sencillo."),
        ],
        "understand": [
            ex("¿Para qué sirve tener un propósito en la segunda escucha?", "Para no perderse y notar algo concreto", "El propósito orienta la atención."),
            ex("¿Qué es una imagen al escuchar un texto?", "Lo que veo en mi mente", "La imagen es lo que imaginas."),
            ex("Antes de grabar una voz, ¿qué debes pedir?", "Permiso", "La voz de una persona se graba solo con su autorización."),
        ],
        "apply": [
            ex(f"En «{CANCION}», cuenta cuántas veces suena la palabra «luna».", "2", "«luna» aparece en el primer y en el tercer verso."),
            ex(f"En «{TRABA}», cuenta cuántas palabras empiezan con «to».", "3", "Son toma, Tomás y tomando."),
            ex(f"En «{ADIV_ARBOL}», ¿cuántas veces suena la palabra «tengo»?", "2", "«Tengo hojas» y «tengo ramas» son dos."),
        ],
        "reason": [
            ex("Ema escuchó dos veces sin tener un propósito y no recuerda nada. ¿Qué debió hacer?", "Decir antes qué iba a buscar", "Con un propósito, la segunda escucha deja algo que contar."),
            ex("Dos niños escuchan el mismo texto: uno busca un sonido y otro una palabra. ¿Pueden notar cosas distintas y estar bien?", "Sí", "Cada propósito lleva a notar algo distinto."),
        ],
        "challenge": [
            ex(f"En «{POEMA}», cuenta cuántas veces suena la palabra «el» (con mayúscula o minúscula) como palabra suelta.", "2", "«El agua» abre el primer y el tercer verso."),
            ex("Escribe un propósito de escucha para un texto de práctica: «voy a contar la palabra ______».", "Cualquier palabra que esté en el texto", "Se acepta un propósito concreto que se pueda verificar."),
        ],
    },
    context=[ex("La educadora tradicional comparte un canto y Pedro quiere grabarlo con el teléfono. ¿Qué debe hacer primero?", "Pedir permiso", "Una voz y un canto de la comunidad se graban solo con autorización.")],
    selfcheck=[
        ex("¿Qué haces la primera vez que escuchas un texto?", "Lo escucho completo", "La primera escucha es del texto entero."),
        ex("¿Qué haces la segunda vez?", "Busco algo concreto", "Escuchas con un propósito."),
        ex("¿Qué debes pedir antes de grabar una voz?", "Permiso", "Se pide autorización."),
    ],
    open_task=task(
        "Pide a un adulto que te lea dos veces la adivinanza de práctica «" + ADIV_NUBE + "». La primera vez escucha entera. La segunda vez elige un propósito: contar cuántas veces suena «y a veces» o notar una imagen. Escribe tu propósito y lo que notaste. Luego anota una pregunta para el educador/a tradicional: ¿qué conviene notar al escuchar un texto de su pueblo?",
        "Mi propósito fue notar una imagen. Vi una nube gris que suelta gotas. Mi pregunta: ¿qué conviene notar al escuchar un canto de la comunidad?",
        ["escucha dos veces", "dice su propósito", "anota lo que notó y una pregunta"],
        ["frase del propósito", "lo notado", "pregunta anotada"],
        ["no tener propósito", "grabar sin permiso"],
        "Reconoce el propósito y la observación, y pide que la pregunta sea para quien conoce el texto.",
    ),
    reinforce="Escucha una canción de tu casa dos veces: la primera completa y la segunda contando una palabra.",
    extend="Elige un propósito distinto para cada una de dos escuchas del mismo texto de práctica.",
)

# ---------------------------------------------------------------- Clase 6
register(
    OA, 6,
    materials="Este cuaderno, lápiz, hojas y colores para dibujar. Los textos de práctica están escritos en castellano.",
    use="Aprenderé a compartir lo que comprendí de un texto oral con mi voz, con mi cuerpo o con un dibujo. Sirve para mostrar lo que entendí aunque no pueda escribir mucho.",
    prior=["Sé escuchar un texto completo y notar una palabra.", "Sé hacer un gesto o un dibujo."],
    explain=[
        "Compartir lo que comprendiste puede hacerse de tres formas. Con la voz: cuentas con tus palabras de qué trata el texto. Con el cuerpo: muestras la idea con un gesto. Con un dibujo: haces lo que viste en tu mente.",
        "Una buena respuesta dice una idea del texto y la relaciona con lo que escuchaste. Por ejemplo: «El texto dice que el agua canta, y yo dibujé el agua en la piedra». Así se ve que comprendiste, aunque no hayas usado muchas palabras.",
        "Para un texto tradicional, termina siempre agradeciendo a quien lo compartió y diciendo de quién es. Si quedó una duda, la dices como pregunta: «¿Qué quiere decir esta parte?». Preguntar también es comprender.",
    ],
    vocab=[("compartir", "mostrar a otros lo que comprendí"), ("dibujo", "imagen que hago con lápices"), ("respuesta", "lo que digo o muestro después de escuchar"), ("agradecer", "decir gracias a quien compartió"), ("duda", "algo que no entendí y quiero preguntar")],
    worked=[
        {"title": "Responder con un dibujo", "problem": f"Escuchaste: «{POEMA}». Respondes con un dibujo. ¿Qué dibujas?", "steps": ["Pienso en la idea: el agua canta bajito.", "Dibujo una piedra y agua bajando por ella.", "Escribo debajo: «el agua canta bajito»."], "answer": "Una piedra con agua bajando y el verso escrito"},
        {"title": "Responder con una pregunta", "problem": "Escuchaste un canto tradicional y no entendiste una parte. ¿Cómo lo dices con respeto?", "steps": ["Agradezco: «Gracias por compartir el canto».", "Digo qué parte no entendí.", "Pregunto: «¿Qué quiere decir esta parte?»"], "answer": "Agradeciendo y preguntando qué quiere decir esa parte"},
    ],
    mistakes=[
        {"wrong": "Pensar que solo se responde bien escribiendo mucho.", "why": "También se puede mostrar la comprensión con voz, cuerpo o dibujo.", "fix": "Elige la forma que te permita mostrar lo que entendiste."},
        {"wrong": "No agradecer a quien compartió el texto.", "why": "Quien comparte da algo valioso de su comunidad.", "fix": "Termina diciendo gracias y de quién es el texto."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué tres formas puedes compartir lo que comprendiste?", "Con la voz, con el cuerpo o con un dibujo", "Esas son las tres vías de respuesta."),
            ex("Después de escuchar un canto, ¿qué dices a quien lo compartió?", "Gracias", "Se agradece a quien comparte."),
            ex("Si no entendiste una parte, ¿la dices como pregunta o la inventas?", "Como pregunta", "Inventar no es comprender; preguntar sí."),
        ],
        "understand": [
            ex("¿Por qué un dibujo puede mostrar que comprendiste?", "Porque muestra la idea del texto", "El dibujo expresa lo que entendiste."),
            ex("¿Preguntar «qué quiere decir esta parte» es comprender o es fallar?", "Es comprender", "Preguntar muestra que prestaste atención."),
            ex("Una buena respuesta, ¿dice una idea del texto o repite el título?", "Dice una idea del texto", "La comprensión se ve en la idea."),
        ],
        "apply": [
            ex(f"Responde con una frase al texto «{CANCION}»: ¿qué hace la luna en el primer verso?", "Sube", "El primer verso dice «Sube, sube, la luna sube»."),
            ex(f"Responde con un gesto al texto «{RONDA}»: ¿qué haces en «aplaudo una, aplaudo dos»?", "Dos palmadas", "Se aplaude una vez y luego otra."),
            ex(f"Responde con un dibujo al texto «{ADIV_ARBOL}»: ¿qué dibujas?", "Un árbol con hojas, ramas y un niño jugando", "El texto describe un árbol."),
        ],
        "reason": [
            ex("Matías respondió con un dibujo y Lía con un gesto. ¿Alguna respuesta es mejor que la otra?", "No, mientras muestren la idea del texto", "Lo importante es que muestren lo comprendido."),
            ex("Una niña dice: «No sé qué quiere decir esta parte, ¿me explica?». ¿Hizo algo malo?", "No, hizo una buena pregunta", "Preguntar es parte de comprender."),
        ],
        "challenge": [
            ex(f"Cuenta cuántas ideas diferentes tiene la adivinanza «{ADIV_NUBE}»: viaja por el cielo, es gris o blanca y suelta gotas. Escribe el número.", "3", "Las ideas son viajar, ser gris o blanca y soltar gotas."),
            ex("Escribe una frase de cierre para agradecer a quien compartió un canto con tu curso.", "Cualquier frase que diga gracias por compartir", "Se acepta un agradecimiento respetuoso."),
        ],
    },
    context=[ex("Al terminar la visita del educador tradicional, el curso responde. Una niña canta bajito, otro hace un dibujo y otra hace un gesto. ¿Alguien respondió mal?", "No", "Las tres respuestas son formas válidas de compartir comprensión.")],
    selfcheck=[
        ex("¿Qué dices a quien compartió un texto?", "Gracias", "Agradecer es parte de compartir."),
        ex("¿Puedes responder con un dibujo?", "Sí", "El dibujo es una forma de respuesta."),
        ex("¿Qué haces con una duda?", "La digo como pregunta", "Preguntar ayuda a comprender."),
    ],
    open_task=task(
        "Pide a un adulto que te diga la adivinanza «" + ADIV_ARBOL + "» y elige cómo responder: con un dibujo, con un gesto o con tus palabras. Muéstrale tu respuesta y escribe una frase que diga la idea. Termina diciendo «gracias por compartir». Luego anota una pregunta para el educador/a tradicional o la comunidad: ¿qué adivinanza de su pueblo puedes escuchar y cómo debes agradecerla?",
        "Dibujé un árbol con ramas y un niño debajo. Mi frase: «El texto habla de un árbol que da sombra». Dije gracias por compartir. Mi pregunta: ¿qué adivinanza del pueblo puedo escuchar?",
        ["responde con voz, cuerpo o dibujo", "dice una idea del texto", "agradece y pregunta"],
        ["dibujo, gesto o respuesta oral", "frase con la idea", "pregunta anotada"],
        ["no decir gracias", "inventar lo que no entendió"],
        "Reconoce la respuesta y la idea, y valora el agradecimiento y la pregunta.",
    ),
    reinforce="Cuéntale a alguien de tu casa de qué trata una adivinanza que escuchaste, con un dibujo.",
    extend="Responde al mismo texto de práctica de dos formas distintas: con un gesto y con un dibujo.",
)

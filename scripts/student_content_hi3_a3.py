"""Material del estudiante de 3.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (investigar sobre civilizaciones antiguas) y OA 06 (cuadrículas y puntos cardinales)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA5 = "HI03 OA 05"
OA6 = "HI03 OA 06"

# ================================================================ OA 05 · INVESTIGACIÓN
# ---------------------------------------------------------------- clase 1
P1 = ("Ficha de preguntas. Temas posibles: héroes, dioses, ciudades, viviendas, vestimenta, herramientas y esclavitud en Grecia y Roma. "
      "Una pregunta investigable se puede responder con fuentes, es clara y empieza con ¿Cómo…?, ¿Qué…?, ¿Para qué…? o ¿Por qué…?. "
      "No es investigable si es una opinión, si es demasiado grande o si se responde con un simple sí o no. "
      "Preguntas: 1) ¿Cómo eran las casas de una familia ateniense? 2) ¿Cuál dios griego es el más bonito? 3) ¿Cómo era todo en la Antigüedad? "
      "4) ¿Para qué servían los acueductos romanos? 5) ¿Qué trabajos hacían las personas esclavizadas en Roma? 6) ¿Existió Roma?")
register(
    OA5, 1,
    materials="Lápiz y papel. La ficha de preguntas está escrita en cada ejercicio.",
    use="Aprenderé a transformar algo que me interesa en una pregunta que se pueda investigar. Sirve para empezar una investigación con buen pie.",
    prior=["Sé algo de Grecia y de Roma.", "Sé qué es una fuente."],
    explain=[
        "Investigar es buscar información para responder una pregunta. Todo empieza con la curiosidad: algo te llama la atención, como los dioses, los héroes, las ciudades, las viviendas, la ropa, las herramientas o la esclavitud. Pero la curiosidad sola no basta. Hay que convertirla en una pregunta clara.",
        "Una pregunta investigable se puede responder con fuentes, como libros, imágenes o páginas de internet revisadas con una persona adulta. Suele empezar con ¿Cómo…?, ¿Qué…?, ¿Para qué…? o ¿Por qué…?. Es clara y no es ni demasiado grande ni demasiado pequeña.",
        "No sirve una pregunta de opinión, como ¿cuál es el más bonito?, porque cada persona puede responder distinto sin usar fuentes. Tampoco sirve una pregunta enorme, como ¿cómo era todo en la Antigüedad?, ni una que se responde con sí o no. Cuando una pregunta es muy grande, se achica: se elige un solo tema y un solo lugar.",
    ],
    vocab=[("investigar", "buscar información para responder una pregunta"), ("pregunta investigable", "pregunta que se puede responder con fuentes"), ("opinión", "lo que una persona piensa o siente"), ("tema", "asunto sobre el que se investiga"), ("fuente", "libro, imagen, objeto o texto que entrega información")],
    worked=[
        {"title": "Elegir una pregunta buena", "problem": f"{P1} ¿La pregunta 4 es investigable?", "steps": ["Se puede responder con libros o imágenes.", "Empieza con ¿Para qué…?.", "Es clara."], "answer": "Sí, es investigable"},
        {"title": "Descartar una pregunta", "problem": f"{P1} ¿Por qué la pregunta 2 no es investigable?", "steps": ["Pregunta cuál es el más bonito.", "Es una opinión: cada persona puede responder distinto sin fuentes."], "answer": "Porque es una opinión"},
    ],
    mistakes=[
        {"wrong": "Hacer una pregunta tan grande que no se puede responder, como ¿cómo era todo en Grecia?", "why": "Se quiere saber todo de una vez.", "fix": "Elige un solo tema y un solo lugar, como las casas de Atenas."},
        {"wrong": "Hacer una pregunta de opinión y llamarla investigación.", "why": "No hay fuente que pueda responder.", "fix": "Usa ¿Cómo…? o ¿Para qué…? para que las fuentes puedan responder."},
    ],
    tiers={
        "recovery": [
            ex(f"{P1} ¿Con qué palabra puede empezar una pregunta investigable? Nombra una.", "una de: Cómo, Qué, Para qué, Por qué", "La ficha las nombra."),
            ex(f"{P1} ¿La pregunta 1 es investigable?", "sí", "Se puede responder con fuentes sobre casas atenienses."),
            ex("Investigar, ¿es buscar información para responder una pregunta o inventar una historia?", "buscar información para responder una pregunta", "Esa es la definición de investigar."),
        ],
        "understand": [
            ex(f"{P1} ¿Por qué la pregunta 3 es demasiado grande?", "porque pregunta por todo en toda la Antigüedad", "No tiene un tema ni un lugar."),
            ex(f"{P1} ¿Por qué la pregunta 6 no sirve para una investigación?", "porque se responde con un sí o un no", "No hay nada que explorar."),
            ex(f"{P1} ¿Qué tienen en común las preguntas 1, 4 y 5?", "se pueden responder con fuentes", "Las tres son investigables."),
        ],
        "apply": [
            ex(f"{P1} Escribe los números de las tres preguntas investigables de la lista.", "1, 4 y 5", "Las demás son opinión, enorme o de sí o no."),
            ex(f"{P1} Achica la pregunta 3 eligiendo A) ¿Cómo era la ropa de los romanos? o B) ¿Cómo era todo en Roma? ¿Cuál queda mejor?", "A", "A tiene un solo tema y un solo pueblo."),
            ex("Convierte este interés en una pregunta: «Quiero saber sobre los acueductos». Elige A) ¿Para qué servían los acueductos romanos? B) ¿Son bonitos los acueductos?", "A", "A se puede responder con fuentes."),
        ],
        "reason": [
            ex(f"{P1} Marta dice que la pregunta 2 es buena porque a ella le gusta mucho. ¿Qué le respondes?", "Es una opinión y no se puede responder con fuentes", "Gustar es personal."),
            ex(f"{P1} Un niño quiere investigar los héroes de Grecia. Dice: «¿Cómo eran los héroes griegos?». Da una forma de achicar su pregunta.", "elegir un solo héroe o un solo aspecto de su vida", "Una persona o un aspecto es un tema más pequeño."),
        ],
        "challenge": [
            ex("Ordena de más grande a más pequeña: A) ¿Cómo vivían los romanos? B) ¿Cómo eran las viviendas de los romanos? C) ¿Cómo era una insula?", "A, B, C", "A abarca todo, B solo las viviendas y C un solo tipo de vivienda."),
            ex(f"{P1} Elige la mejor pregunta sobre la esclavitud. A) ¿Qué trabajos hacían las personas esclavizadas en Roma? B) ¿Era mala la esclavitud en Roma?", "A", "A se responde con fuentes y B pide una opinión."),
        ],
    },
    context=[ex("Un niño ve una foto de un teatro griego y quiere investigar. ¿Qué pregunta le sirve más? A) ¿Para qué servían los teatros griegos? B) ¿Los teatros griegos son lindos?", "A", "A se responde con fuentes.")],
    selfcheck=[
        ex("¿Qué es una pregunta investigable?", "una pregunta que se puede responder con fuentes", "Es clara y no es opinión."),
        ex("¿Una pregunta de opinión sirve para investigar?", "no", "Cada persona responde distinto."),
        ex("¿Qué se hace con una pregunta demasiado grande?", "se achica", "Se elige un tema y un lugar."),
    ],
    open_task=task(
        f"Elige un tema de esta lista: héroes, dioses, ciudades, viviendas, vestimenta, herramientas o esclavitud. Escribe tu pregunta, y revisa con las tres reglas: se puede responder con fuentes, es clara y no es enorme. {P1}",
        "Tema: vestimenta. Pregunta: ¿Cómo era la ropa de los ciudadanos romanos? Revisión: se responde con libros e imágenes, es clara y habla de un solo pueblo.",
        ["tema elegido de la lista", "pregunta investigable", "revisa las tres reglas"], ["pregunta escrita con revisión"], ["pregunta de opinión", "pregunta demasiado grande"],
        "Pregunta cómo la achicaría si fuera muy grande."),
    reinforce="Escribe dos preguntas investigables sobre Grecia y dos sobre Roma.",
    extend="Elige una pregunta no investigable de la ficha y reescríbela para que lo sea.",
)

# ---------------------------------------------------------------- clase 2
P2 = ("Ficha de fuentes. Fuente A: libro escolar de historia, hecho por un equipo de autores de una editorial, fecha de edición: hace pocos años. Texto: «Los acueductos romanos llevaban agua desde lugares altos hasta las ciudades. El agua corría por un canal con una pendiente suave.» "
      "Fuente B: cartel de un museo. Dice: «Ánfora griega. Se usaba para guardar y transportar aceite o vino. Ciudad de origen: Atenas». Lo hizo el museo para informar a quienes visitan. "
      "Fuente C: un video de internet sin autor y sin fecha que dice: «Los griegos vivían todos en palacios de oro». "
      "Para leer una fuente nos preguntamos: ¿quién la hizo? (autor), ¿para qué la hizo? (propósito), ¿cuándo? (fecha) y ¿da pistas que puedo comprobar?")
register(
    OA5, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a leer una fuente preguntando quién la hizo, para qué y cuándo. Sirve para saber cuánto puedo confiar en ella.",
    prior=["Sé qué es una pregunta investigable.", "Sé qué es una fuente."],
    explain=[
        "Una fuente es cualquier cosa que entrega información. Pero no todas valen lo mismo. Antes de usar una fuente, nos preguntamos cuatro cosas: ¿quién la hizo?, ¿para qué la hizo?, ¿cuándo se hizo? y ¿da pistas que se puedan comprobar con otra fuente?",
        "El autor es la persona o grupo que hizo la fuente. El propósito es lo que quería lograr: informar, enseñar, vender o entretener. Un libro escolar tiene como propósito enseñar. Un cartel de museo tiene como propósito informar. Un video sin autor ni fecha no permite saber quién lo hizo ni cuándo, y por eso hay que desconfiar más.",
        "Para usar internet, siempre debes hacerlo con una persona adulta. Busca páginas con autor, fecha y propósito claros. Cuando una fuente dice algo muy raro, como «todos vivían en palacios de oro», necesitas comprobarlo con otra fuente antes de creerlo.",
    ],
    vocab=[("autor", "persona o grupo que hizo la fuente"), ("propósito", "para qué se hizo una fuente"), ("fecha", "momento en que se hizo la fuente"), ("confiable", "que merece que le creamos"), ("comprobar", "revisar si algo es verdad usando otra fuente")],
    worked=[
        {"title": "Leer una fuente", "problem": f"{P2} Responde sobre la fuente A: autor, propósito y fecha.", "steps": ["Autor: un equipo de una editorial.", "Propósito: enseñar, es un libro escolar.", "Fecha: hace pocos años."], "answer": "Autor: editorial; propósito: enseñar; fecha: hace pocos años"},
        {"title": "Desconfiar con razones", "problem": f"{P2} ¿Por qué hay que desconfiar de la fuente C?", "steps": ["No tiene autor.", "No tiene fecha.", "Dice algo muy raro que no se comprueba."], "answer": "No tiene autor ni fecha y afirma algo difícil de creer"},
    ],
    mistakes=[
        {"wrong": "Creer todo lo que dice internet.", "why": "Se piensa que si está escrito, es verdad.", "fix": "Pregunta quién lo hizo, para qué y cuándo, y compruébalo."},
        {"wrong": "Decir que una fuente es mala solo porque es antigua.", "why": "Se confunde antigüedad con error.", "fix": "Revisa quién la hizo y para qué, no solo su edad."},
    ],
    tiers={
        "recovery": [
            ex(f"{P2} ¿Quién hizo la fuente A?", "un equipo de autores de una editorial", "La ficha lo dice."),
            ex(f"{P2} ¿Qué propósito tiene el cartel de museo?", "informar a quienes visitan", "Así lo dice la ficha."),
            ex("El autor de una fuente, ¿es quien la hizo o quien la lee?", "quien la hizo", "Esa es la definición de autor."),
        ],
        "understand": [
            ex(f"{P2} ¿Qué dato dice la fuente B sobre el uso del ánfora?", "se usaba para guardar y transportar aceite o vino", "Está en el cartel."),
            ex(f"{P2} ¿Qué es el propósito de una fuente?", "para qué se hizo", "Puede ser informar, enseñar, vender o entretener."),
            ex(f"{P2} ¿Cuál fuente no tiene autor ni fecha?", "la fuente C", "El video no los indica."),
        ],
        "apply": [
            ex(f"{P2} Si quieres saber para qué servían los acueductos, ¿qué fuente te sirve?", "la fuente A", "Habla de acueductos romanos."),
            ex(f"{P2} Si quieres saber qué se guardaba en un ánfora, ¿qué fuente te sirve?", "la fuente B", "Es un cartel sobre un ánfora."),
            ex(f"{P2} Une cada fuente con su propósito: A) libro escolar; B) cartel de museo. 1) informar a quienes visitan; 2) enseñar.", "A con 2; B con 1", "El libro escolar enseña y el cartel informa."),
        ],
        "reason": [
            ex(f"{P2} Pablo dice: «La fuente C es confiable porque está en internet». ¿Qué le respondes?", "No tiene autor ni fecha y dice algo difícil de creer", "Estar en internet no basta."),
            ex(f"{P2} Un niño dice que el agua de los acueductos subía con motores. ¿Qué fuente lo corrige?", "la fuente A, que dice que corría por una pendiente suave", "La fuente A explica cómo corría el agua."),
        ],
        "challenge": [
            ex(f"{P2} ¿Cuál de las tres fuentes es la menos confiable? Considera que A y B tienen autor y propósito claros, y C no.", "la fuente C", "Es la que no tiene autor ni fecha."),
            ex("Para usar internet en una investigación, ¿qué debes hacer? Elige. A) Usar cualquier página. B) Hacerlo con una persona adulta y revisar autor y fecha.", "B", "Así se cuida la seguridad y se revisa la fuente."),
        ],
    },
    context=[ex("Encuentras una página con un dato sobre los romanos, sin nombre de autor y sin fecha. ¿Qué haces primero?", "buscar el dato en otra fuente con autor y fecha", "Hay que comprobarlo.")],
    selfcheck=[
        ex("¿Qué cuatro preguntas hacemos a una fuente?", "quién la hizo, para qué, cuándo y si se puede comprobar", "Son las preguntas de la ficha."),
        ex("¿Qué propósito tiene un libro escolar?", "enseñar", "Se hace para que aprendamos."),
        ex("¿Con quién debes usar internet?", "con una persona adulta", "Es parte del cuidado."),
    ],
    open_task=task(
        f"Haz una ficha de lectura para la fuente A o para la fuente B con estos títulos: autor, propósito, fecha, dato importante y duda. {P2}",
        "Fuente B: autor, el museo. Propósito, informar a quienes visitan. Fecha, no está escrita. Dato, el ánfora servía para guardar aceite o vino. Duda, no dice cuándo se hizo el ánfora.",
        ["cinco títulos", "datos de la fuente", "una duda real"], ["ficha completa"], ["inventar un autor", "no escribir una duda"],
        "Pregunta qué más le gustaría saber de la fuente."),
    reinforce="Explica a alguien en casa las cuatro preguntas para leer una fuente.",
    extend="Escribe cómo comprobarías el dato de la fuente C usando otras dos fuentes.",
)

# ---------------------------------------------------------------- clase 3
P3 = ("Ficha para contrastar. Tema: la ropa de los romanos. "
      "Fuente 1, libro escolar con autor y fecha: «Los romanos usaban una túnica. Los ciudadanos hombres usaban además una toga sobre la túnica.» "
      "Fuente 2, cartel de museo con autor y fecha, junto a una estatua: «Estatua de un ciudadano romano vestido con toga». "
      "Fuente 3, blog sin autor y sin fecha: «Los romanos nunca usaban túnica; todos usaban solo toga». "
      "Contrastar es comparar fuentes. Si dos fuentes confiables dicen lo mismo, el dato se apoya mejor. Si una fuente dice algo distinto, buscamos una tercera y revisamos su autor y fecha.")
register(
    OA5, 3,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a comparar dos o más fuentes antes de sacar una conclusión. Sirve para no quedarme con un dato dudoso.",
    prior=["Sé leer una fuente con autor, propósito y fecha.", "Sé qué es una pregunta investigable."],
    explain=[
        "Contrastar es comparar fuentes sobre un mismo tema. Miramos en qué coinciden y en qué se diferencian. Si dos fuentes confiables dicen lo mismo, el dato se apoya mejor. Por ejemplo, un libro escolar y un cartel de museo con una estatua dicen que los ciudadanos romanos usaban toga.",
        "A veces una fuente dice algo distinto, como un blog que dice que los romanos nunca usaban túnica. Entonces hacemos preguntas: ¿tiene autor y fecha?, ¿otras fuentes dicen lo mismo?, ¿qué muestran las imágenes? Si no podemos comprobarlo, no lo usamos como un hecho.",
        "Después de contrastar escribimos una conclusión con cuidado. Una conclusión es lo que decidimos creer después de revisar las fuentes. Puede ser «las fuentes 1 y 2 coinciden: los ciudadanos hombres usaban toga» y también «no estoy seguro de lo que dice la fuente 3». Decir lo que no sabemos también es parte de investigar.",
    ],
    vocab=[("contrastar", "comparar fuentes para ver en qué coinciden y en qué difieren"), ("coincidir", "decir lo mismo"), ("conclusión", "lo que decidimos creer después de revisar las fuentes"), ("contradecir", "decir lo contrario"), ("confirmar", "comprobar que algo es cierto con otra fuente")],
    worked=[
        {"title": "Coincidencia", "problem": f"{P3} ¿En qué coinciden las fuentes 1 y 2?", "steps": ["La fuente 1 dice que los ciudadanos hombres usaban toga.", "La fuente 2 muestra una estatua de un ciudadano con toga.", "Coinciden."], "answer": "En que los ciudadanos romanos usaban toga"},
        {"title": "Desacuerdo", "problem": f"{P3} ¿Qué fuente contradice a la fuente 1?", "steps": ["La fuente 3 dice que nunca usaban túnica.", "La fuente 1 dice que usaban túnica."], "answer": "La fuente 3"},
    ],
    mistakes=[
        {"wrong": "Quedarse con la primera fuente que se encuentra.", "why": "Se cree que una sola basta.", "fix": "Busca al menos otra fuente y compáralas."},
        {"wrong": "Creer que todas las fuentes valen lo mismo.", "why": "No se revisa autor ni fecha.", "fix": "Pregunta quién la hizo, para qué y cuándo."},
    ],
    tiers={
        "recovery": [
            ex(f"{P3} ¿Qué usaban los ciudadanos hombres romanos sobre la túnica?", "una toga", "Lo dice la fuente 1."),
            ex(f"{P3} ¿Qué es contrastar?", "comparar fuentes", "Así lo dice la ficha."),
            ex(f"{P3} ¿Qué fuente no tiene autor ni fecha?", "la fuente 3", "Es el blog."),
        ],
        "understand": [
            ex(f"{P3} ¿Qué muestra la fuente 2?", "una estatua de un ciudadano romano con toga", "Así lo dice el cartel."),
            ex(f"{P3} ¿Qué es una conclusión?", "lo que decidimos creer después de revisar las fuentes", "Así la define la clase."),
            ex(f"{P3} ¿La fuente 3 coincide con la fuente 1?", "no, la contradice", "Dice que nunca usaban túnica."),
        ],
        "apply": [
            ex(f"{P3} Escribe una conclusión con las fuentes 1 y 2.", "los ciudadanos hombres romanos usaban toga", "Ambas fuentes lo apoyan."),
            ex(f"{P3} Elige qué hacer con la fuente 3. A) Creerle sin revisar. B) Buscar otra fuente con autor y fecha para comprobar.", "B", "Hay que comprobarla."),
            ex(f"{P3} Completa: la fuente 1 y la fuente 2 ___ (coinciden / se contradicen).", "coinciden", "Dicen lo mismo."),
        ],
        "reason": [
            ex(f"{P3} Tomás dice: «La fuente 3 es la correcta porque suena muy segura». ¿Qué le respondes?", "No se sabe su autor ni su fecha, y las otras dos fuentes dicen otra cosa", "Sonar seguro no prueba que algo sea verdad."),
            ex(f"{P3} Ema dice que todos los romanos usaban toga porque la ve en la estatua. ¿Qué dice la fuente 1 sobre la mayoría?", "usaban túnica y solo los ciudadanos hombres usaban toga encima", "La estatua muestra un ciudadano, no a todos."),
        ],
        "challenge": [
            ex(f"{P3} Escribe una conclusión con cuidado que diga lo que sabes y lo que no estás seguro.", "Las fuentes 1 y 2 coinciden en que los ciudadanos hombres usaban toga; no estoy seguro de lo que dice la fuente 3", "Incluye el límite."),
            ex("Para un dato importante, ¿cuántas fuentes conviene mirar al menos? Elige. A) Una. B) Dos o más.", "B", "Así se puede comparar."),
        ],
    },
    context=[ex("Un amigo te cuenta algo sobre los griegos que leyó en un solo sitio. ¿Qué le sugieres?", "buscar otra fuente para comparar", "Así se confirma el dato.")],
    selfcheck=[
        ex("¿Qué haces si una fuente dice algo distinto?", "busco otra fuente y reviso autor y fecha", "Es la regla de la ficha."),
        ex("En una investigación, ¿qué es una conclusión?", "lo que decidimos creer después de revisar las fuentes", "Debe escribirse con cuidado."),
        ex("¿Se puede escribir «no estoy seguro» en una investigación?", "sí", "Es parte de investigar."),
    ],
    open_task=task(
        f"Escribe una conclusión de 3 líneas sobre la ropa de los romanos. Debe decir en qué coinciden las fuentes, cuál fuente te da duda y qué harías para comprobarla. {P3}",
        "Las fuentes 1 y 2 coinciden en que los ciudadanos hombres usaban toga. La fuente 3 me da duda porque no tiene autor ni fecha. Buscaría una cuarta fuente, como un libro de la biblioteca.",
        ["coincidencia explicada", "una duda razonada", "una forma de comprobar"], ["conclusión escrita"], ["no mencionar la fuente dudosa", "decir que todas dicen lo mismo"],
        "Pregunta qué otra fuente buscaría."),
    reinforce="Explica a alguien en casa qué es contrastar fuentes.",
    extend="Imagina que dos fuentes confiables se contradicen. Escribe qué harías.",
)

# ---------------------------------------------------------------- clase 4
P4 = ("Ficha para organizar. Pregunta: ¿Para qué servían las calzadas romanas? "
      "Fuente 1, libro escolar con autor y fecha: «Los romanos construyeron calzadas, que eran caminos de piedra. Servían para mover soldados y mercaderías.» "
      "Fuente 2, cartel de un museo, con autor y fecha: «Calzada romana. Camino de piedra que unía ciudades». "
      "Para registrar, usamos una tabla con cuatro columnas: pregunta, dato, fuente y si lo escribí con mis palabras. "
      "Copiar es escribir las mismas palabras de la fuente. Parafrasear es decir la misma idea con palabras propias y siempre nombrando la fuente.")
register(
    OA5, 4,
    materials="Lápiz y papel. Las fuentes y la tabla están escritas en cada ejercicio.",
    use="Aprenderé a registrar lo que encuentro en una tabla, con mis palabras y diciendo de dónde viene. Sirve para ordenar la investigación y no copiar.",
    prior=["Sé leer y contrastar fuentes.", "Sé qué es una pregunta investigable."],
    explain=[
        "Cuando investigamos, anotamos lo que encontramos. Una tabla ayuda a ordenar: pregunta, dato, fuente y si lo escribí con mis palabras. Así sabemos de dónde viene cada dato y podemos volver a revisarlo.",
        "Copiar es escribir las mismas palabras de la fuente. Parafrasear es explicar la misma idea con palabras propias. Un buen registro parafrasea, no copia. Por ejemplo, la fuente dice «Servían para mover soldados y mercaderías». Yo puedo escribir: «Las calzadas ayudaban a llevar soldados y productos».",
        "Siempre nombramos la fuente de donde sacamos cada dato. Eso se llama reconocer de dónde vienen las ideas. Si usamos la idea de otra persona sin decirlo, es como quedarse con lo que no es nuestro. Además, si anotas la fuente, otra persona puede comprobar tu dato.",
    ],
    vocab=[("registrar", "anotar lo que se encuentra"), ("copiar", "escribir las mismas palabras de la fuente"), ("parafrasear", "decir la misma idea con palabras propias"), ("dato", "información precisa"), ("reconocer la fuente", "decir de dónde viene una idea")],
    worked=[
        {"title": "Parafrasear", "problem": f"{P4} Fuente 1: «Servían para mover soldados y mercaderías». Escribe la idea con tus palabras.", "steps": ["Identifico la idea: transportar soldados y productos.", "La escribo con otras palabras."], "answer": "Las calzadas ayudaban a llevar soldados y productos (fuente 1)"},
        {"title": "Llenar una fila", "problem": f"{P4} Completa una fila de la tabla con la fuente 2.", "steps": ["Pregunta: ¿para qué servían las calzadas?", "Dato: unían ciudades.", "Fuente: cartel de museo."], "answer": "Pregunta: para qué servían; dato: unían ciudades; fuente: cartel de museo"},
    ],
    mistakes=[
        {"wrong": "Copiar el texto entero de la fuente.", "why": "Es más fácil que pensar la idea.", "fix": "Lee, cierra el libro y escribe con tus palabras."},
        {"wrong": "Anotar un dato sin escribir la fuente.", "why": "Se piensa que se va a recordar.", "fix": "Anota siempre la fuente junto al dato."},
    ],
    tiers={
        "recovery": [
            ex(f"{P4} ¿Qué es parafrasear?", "decir la misma idea con palabras propias", "Así lo dice la ficha."),
            ex(f"{P4} ¿Qué eran las calzadas, según la fuente 1?", "caminos de piedra", "Así lo dice la fuente."),
            ex(f"{P4} Nombra una columna de la tabla.", "una de: pregunta, dato, fuente, con mis palabras", "La ficha las nombra."),
        ],
        "understand": [
            ex(f"{P4} ¿Por qué hay que anotar la fuente de cada dato?", "para saber de dónde viene y poder comprobarlo", "Así otra persona puede revisarlo."),
            ex(f"{P4} ¿Para qué servían las calzadas, según la fuente 1?", "para mover soldados y mercaderías", "La fuente lo dice."),
            ex(f"{P4} ¿Qué dato entrega la fuente 2?", "unía ciudades", "El cartel lo dice."),
        ],
        "apply": [
            ex(f"{P4} Elige la frase parafraseada. A) «Servían para mover soldados y mercaderías». B) Las calzadas ayudaban a llevar soldados y productos.", "B", "B usa palabras propias."),
            ex(f"{P4} Completa la fila de la tabla con la fuente 1: pregunta; dato; fuente.", "¿Para qué servían las calzadas?; mover soldados y mercaderías; libro escolar", "Contiene los tres campos."),
            ex(f"{P4} Un niño anota «las calzadas unían ciudades» sin escribir la fuente. ¿Qué le falta?", "la fuente", "Debe decir que viene del cartel de museo."),
        ],
        "reason": [
            ex(f"{P4} Ana copió palabra por palabra la fuente 1. ¿Qué le sugieres?", "escribir la idea con sus propias palabras", "Eso es parafrasear."),
            ex(f"{P4} Un niño dice: «Si anoto la fuente, pierdo tiempo». ¿Qué respondes?", "Sirve para comprobar el dato y dar crédito", "Otras personas pueden revisarlo."),
        ],
        "challenge": [
            ex(f"{P4} Junta los datos de las dos fuentes en una sola frase con tus palabras.", "Las calzadas eran caminos de piedra que unían ciudades y servían para llevar soldados y productos", "Usa ambos datos."),
            ex(f"{P4} ¿Qué dato aparece en las dos fuentes sobre las calzadas?", "que eran caminos de piedra", "Las dos las describen como caminos de piedra."),
        ],
    },
    context=[ex("Para una exposición, un niño escribe la misma frase del libro sin cambiar nada. ¿Qué debe hacer?", "escribir la idea con sus palabras y nombrar la fuente", "Así parafrasea y reconoce la fuente.")],
    selfcheck=[
        ex("¿Qué es copiar?", "escribir las mismas palabras de la fuente", "No es lo mismo que parafrasear."),
        ex("¿Qué columnas tiene la tabla de registro?", "pregunta, dato, fuente y con mis palabras", "La tabla tiene cuatro columnas."),
        ex("¿Por qué anotamos la fuente?", "para saber de dónde viene el dato", "Así se puede comprobar."),
    ],
    open_task=task(
        f"Haz una tabla con las cuatro columnas y dos filas con datos de las fuentes 1 y 2. Escribe todo con tus palabras. {P4}",
        "Fila 1: ¿Para qué servían las calzadas? / llevar soldados y productos / libro escolar / sí. Fila 2: ¿Qué eran las calzadas? / caminos de piedra que unían ciudades / cartel de museo / sí.",
        ["cuatro columnas", "dos filas", "palabras propias", "fuente nombrada"], ["tabla completa"], ["copiar", "no nombrar la fuente"],
        "Pregunta cómo supo qué decir con otras palabras."),
    reinforce="Escribe dos veces la misma idea: una copiada y una parafraseada. Marca cuál es cuál.",
    extend="Inventa una pregunta nueva y escribe qué columnas necesitarías para su tabla.",
)

# ---------------------------------------------------------------- clase 5
P5 = ("Ficha para comunicar. Una respuesta histórica tiene cuatro partes: (1) la pregunta; (2) una respuesta corta; (3) dos datos con su fuente; (4) algo que todavía no sé. "
      "Ejemplo de borrador de Lucía: «Pregunta: ¿Para qué servían los acueductos romanos? Respuesta: Servían para llevar agua a las ciudades. Dato 1: llevaban agua desde lugares altos hasta las ciudades (libro escolar). "
      "Dato 2: el agua corría por un canal con una pendiente suave (libro escolar). Lo que no sé: cuántas personas usaban el agua de cada acueducto.» "
      "Las imágenes ayudan si tienen un título y se relacionan con la pregunta.")
register(
    OA5, 5,
    materials="Lápiz y papel. El borrador de Lucía está escrito en cada ejercicio.",
    use="Aprenderé a armar una respuesta ordenada con pregunta, respuesta, datos con fuente y una duda. Sirve para comunicar lo que aprendí.",
    prior=["Sé registrar datos con la fuente.", "Sé contrastar fuentes."],
    explain=[
        "Comunicar lo aprendido es explicarlo para que otras personas lo entiendan. Una respuesta histórica tiene cuatro partes. Primero, la pregunta. Segundo, una respuesta corta. Tercero, dos datos con su fuente. Cuarto, algo que todavía no sé.",
        "La respuesta corta es lo central: dice la idea principal en una oración. Los datos son las pruebas que la apoyan. Cada dato nombra su fuente. La parte «lo que no sé» muestra que investigar siempre deja nuevas preguntas, y eso es normal.",
        "Una imagen o un dibujo ayuda si tiene un título y se relaciona con la pregunta. Hablar claro también ayuda: usa oraciones cortas, palabras de la clase y mira a quien te escucha. Si usas una palabra nueva, explícala.",
    ],
    vocab=[("comunicar", "contar a otros lo que se aprendió"), ("respuesta corta", "oración que dice la idea principal"), ("dato", "información precisa que apoya la respuesta"), ("borrador", "primera versión de un trabajo"), ("duda", "algo que todavía no se sabe")],
    worked=[
        {"title": "Reconocer las partes", "problem": f"{P5} ¿Cuál es la respuesta corta del borrador de Lucía?", "steps": ["Busco la parte llamada Respuesta.", "Dice que servían para llevar agua a las ciudades."], "answer": "Servían para llevar agua a las ciudades"},
        {"title": "Dato con fuente", "problem": f"{P5} ¿De dónde sacó Lucía el dato 2?", "steps": ["Miro entre paréntesis.", "Dice libro escolar."], "answer": "Del libro escolar"},
    ],
    mistakes=[
        {"wrong": "Mostrar datos sin una respuesta clara.", "why": "Se piensa que los datos hablan solos.", "fix": "Empieza con una respuesta corta y luego los datos."},
        {"wrong": "No decir qué aún no se sabe.", "why": "Se cree que una investigación debe saberlo todo.", "fix": "Agrega «lo que no sé»: muestra honestidad."},
    ],
    tiers={
        "recovery": [
            ex(f"{P5} ¿Cuántas partes tiene una respuesta histórica?", "4", "La ficha enumera cuatro."),
            ex(f"{P5} ¿Cuál es la pregunta del borrador de Lucía?", "¿Para qué servían los acueductos romanos?", "Está al comienzo."),
            ex(f"{P5} ¿Qué fuente usó Lucía?", "un libro escolar", "Aparece entre paréntesis."),
        ],
        "understand": [
            ex(f"{P5} ¿Qué dice Lucía que todavía no sabe?", "cuántas personas usaban el agua de cada acueducto", "Lo escribió en la última parte."),
            ex(f"{P5} ¿Para qué sirve la respuesta corta?", "para decir la idea principal", "Los datos la apoyan."),
            ex(f"{P5} ¿Para qué sirve decir lo que no sé?", "para ser honesto y mostrar nuevas preguntas", "La investigación sigue."),
        ],
        "apply": [
            ex(f"{P5} Ordena las partes: datos con fuente, pregunta, algo que no sé, respuesta corta.", "pregunta, respuesta corta, datos con fuente, algo que no sé", "Es el orden de la ficha."),
            ex(f"{P5} Marcos escribió: «Los acueductos llevaban agua». Le falta el nombre de la fuente. ¿En qué parte lo agrega?", "junto al dato", "Cada dato nombra su fuente."),
            ex(f"{P5} Elige el mejor título para el dibujo del borrador. A) Acueducto romano: lleva agua a la ciudad. B) Mi dibujo.", "A", "A se relaciona con la pregunta."),
        ],
        "reason": [
            ex(f"{P5} Camila dice: «No pongo lo que no sé, porque se vería mal». ¿Qué le respondes?", "Decir lo que no sabes muestra honestidad y abre nuevas preguntas", "Es parte de investigar."),
            ex(f"{P5} Un niño empieza su exposición con un dato aislado. ¿Qué parte falta antes?", "la pregunta y la respuesta corta", "Ordenan lo que sigue."),
        ],
        "challenge": [
            ex(f"{P5} Escribe una respuesta corta y un dato para la pregunta: ¿Para qué servían las calzadas romanas? Usa lo que viste en la clase anterior.", "Servían para mover soldados y productos; dato: eran caminos de piedra (libro escolar)", "Se basa en la tabla de la clase 4."),
            ex(f"{P5} Revisa el borrador de Lucía. ¿Tiene las cuatro partes?", "sí", "Tiene pregunta, respuesta, dos datos con fuente y duda."),
        ],
    },
    context=[ex("Vas a explicar a tu curso lo que aprendiste sobre las termas romanas. ¿Con qué parte empiezas?", "con la pregunta", "La pregunta ayuda a entender de qué se trata.")],
    selfcheck=[
        ex("¿Qué cuatro partes tiene una respuesta histórica?", "pregunta, respuesta corta, datos con fuente y algo que no sé", "Son las de la ficha."),
        ex("¿Dónde se nombra la fuente?", "junto a cada dato", "Así se reconoce de dónde viene."),
        ex("¿Qué debe tener una imagen para ayudar?", "un título y relación con la pregunta", "Así explica algo."),
    ],
    open_task=task(
        f"Arma tu respuesta histórica con las cuatro partes sobre ¿Para qué servían las calzadas romanas? Usa los datos de la clase 4: son caminos de piedra, unían ciudades, servían para mover soldados y mercaderías. {P5} Agrega un dibujo con título.",
        "Pregunta: ¿Para qué servían las calzadas romanas? Respuesta: Servían para llevar soldados y productos entre ciudades. Dato 1: eran caminos de piedra (libro escolar). Dato 2: unían ciudades (cartel de museo). Lo que no sé: cuántas calzadas había. Dibujo: «Calzada romana de piedra».",
        ["cuatro partes", "datos con fuente", "una duda", "dibujo con título"], ["texto y dibujo"], ["no nombrar fuente", "datos que no están"],
        "Pídele que lo lea en voz alta a alguien."),
    reinforce="Cuenta en voz alta la respuesta histórica de Lucía con tus palabras.",
    extend="Elige otro tema y escribe solo la pregunta y la respuesta corta.",
)

# ---------------------------------------------------------------- clase 6
P6 = ("Ficha de la feria de investigación. Pauta de revisión con cinco criterios: (1) la pregunta es clara; (2) hay una respuesta corta; (3) cada dato dice su fuente; (4) está escrito con palabras propias; (5) se dice qué aún no se sabe. "
      "Cómo dar un comentario: «Me gustó…» y «Una mejora podría ser…». "
      "Borrador de Diego: «Pregunta: ¿Cómo era un teatro griego? Respuesta: Era un lugar al aire libre en una ladera. Datos: Los actores usaban máscaras. Todos los actores eran hombres. »")
register(
    OA5, 6,
    materials="Lápiz y papel. La pauta y el borrador están escritos en cada ejercicio.",
    use="Aprenderé a presentar mi investigación y a mejorarla con comentarios. Sirve para explicar lo que aprendí y corregir lo que falta.",
    prior=["Sé armar una respuesta con cuatro partes.", "Sé parafrasear y nombrar la fuente."],
    explain=[
        "En una feria de investigación, cada estudiante explica a otras personas lo que aprendió. Para presentar bien, hablamos claro, miramos a quien escucha y mostramos nuestra pregunta, respuesta, datos y fuentes. Las imágenes tienen título y apoyan lo que decimos.",
        "Antes de presentar, revisamos con una pauta de cinco criterios. La pregunta es clara, hay una respuesta corta, cada dato dice su fuente, está escrito con palabras propias y se dice qué aún no se sabe. Si falta uno, lo corregimos.",
        "Cuando alguien comenta tu trabajo, escucha con respeto. Un buen comentario tiene dos partes: «Me gustó…» y «Una mejora podría ser…». Así ayudamos a mejorar sin herir. Luego decides qué cambiar y escribes una nueva versión.",
    ],
    vocab=[("feria", "actividad donde se muestran trabajos a otras personas"), ("pauta", "lista de criterios para revisar un trabajo"), ("comentario", "opinión para ayudar a mejorar un trabajo"), ("mejorar", "hacer que algo quede mejor"), ("presentar", "mostrar y explicar un trabajo")],
    worked=[
        {"title": "Revisar con la pauta", "problem": f"{P6} ¿Qué criterio no cumple el borrador de Diego?", "steps": ["Reviso los cinco criterios.", "Cumple pregunta y respuesta, pero los datos no dicen su fuente y falta lo que no sabe."], "answer": "Falta nombrar la fuente de cada dato y decir qué aún no sabe"},
        {"title": "Dar un comentario", "problem": f"{P6} Escribe un comentario para Diego con las dos partes.", "steps": ["Me gustó: su pregunta es clara.", "Mejora: agregar la fuente de cada dato."], "answer": "Me gustó que su pregunta es clara. Una mejora podría ser agregar la fuente de cada dato."},
    ],
    mistakes=[
        {"wrong": "Dar un comentario que solo dice «está mal».", "why": "No se explica qué cambiar.", "fix": "Usa «Me gustó…» y «Una mejora podría ser…»."},
        {"wrong": "Leer el trabajo sin mirar a nadie.", "why": "Se siente vergüenza.", "fix": "Practica en voz alta y mira al público al menos al comienzo y al final."},
    ],
    tiers={
        "recovery": [
            ex(f"{P6} ¿Cuántos criterios tiene la pauta?", "5", "La ficha enumera cinco."),
            ex(f"{P6} ¿Cuál es la pregunta de Diego?", "¿Cómo era un teatro griego?", "Está al inicio de su borrador."),
            ex(f"{P6} ¿Qué dos partes tiene un buen comentario?", "me gustó y una mejora podría ser", "Son las de la ficha."),
        ],
        "understand": [
            ex(f"{P6} ¿Para qué sirve la pauta de revisión?", "para ver qué le falta al trabajo", "Es una lista de criterios."),
            ex(f"{P6} ¿Cuál es la respuesta corta de Diego?", "era un lugar al aire libre en una ladera", "Aparece en su borrador."),
            ex(f"{P6} ¿Qué datos entrega Diego?", "los actores usaban máscaras y eran todos hombres", "Están en su borrador."),
        ],
        "apply": [
            ex(f"{P6} Revisa el borrador de Diego: ¿cada dato dice su fuente?", "no", "No nombra ninguna fuente."),
            ex(f"{P6} Elige el mejor comentario para Diego. A) Está malo. B) Me gustó que su respuesta es clara. Una mejora podría ser agregar la fuente de cada dato.", "B", "B tiene las dos partes."),
            ex(f"{P6} Diego agrega una fuente al primer dato: «(libro escolar)». ¿Qué criterio mejora?", "el 3, cada dato dice su fuente", "Ahora nombra la fuente."),
        ],
        "reason": [
            ex(f"{P6} Ema dice: «Mi trabajo es perfecto y no necesita cambios». ¿Qué puede hacer antes de decidirlo?", "revisarlo con la pauta de cinco criterios", "La pauta muestra qué falta."),
            ex(f"{P6} Pedro recibió un comentario y se enojó. ¿Qué parte del comentario le ayuda más a mejorar?", "la mejora que le proponen", "Dice qué cambiar."),
        ],
        "challenge": [
            ex(f"{P6} Escribe el primer dato de Diego agregando entre paréntesis la fuente «libro escolar». ¿Cómo queda?", "Los actores usaban máscaras (libro escolar)", "La fuente va junto al dato."),
            ex(f"{P6} Diego debe completar el criterio 5. Elige la mejor frase. A) Lo que no sé: cuántas personas cabían en un teatro griego. B) Lo que no sé: nada, ya lo sé todo.", "A", "A reconoce una duda real."),
        ],
    },
    context=[ex("En la feria, un visitante te pregunta algo que no investigaste. ¿Qué respondes?", "que no lo sé todavía y que podrías investigarlo", "Reconocer lo que no se sabe es honesto.")],
    selfcheck=[
        ex("¿Qué se revisa con la pauta?", "los cinco criterios del trabajo", "Pregunta, respuesta, fuentes, palabras propias y duda."),
        ex("¿Cómo se dan buenos comentarios?", "con «me gustó» y «una mejora podría ser»", "Así se ayuda sin herir."),
        ex("¿Qué haces después de recibir comentarios?", "decido qué cambiar y escribo una nueva versión", "Mejorar es parte del trabajo."),
    ],
    open_task=task(
        f"Mejora el borrador de Diego. Escribe una nueva versión que cumpla los cinco criterios y agrega un comentario para él con las dos partes. {P6}",
        "Pregunta: ¿Cómo era un teatro griego? Respuesta: Era un lugar al aire libre en una ladera. Dato 1: los actores usaban máscaras (libro escolar). Dato 2: todos los actores eran hombres (libro escolar). No sé: cuántas personas cabían. Comentario: Me gustó que su respuesta es clara. Una mejora podría ser explicar qué es una ladera.",
        ["cinco criterios cumplidos", "fuente en cada dato", "comentario de dos partes"], ["nueva versión y comentario"], ["no agregar fuente", "comentario solo negativo"],
        "Pide que lea su versión y diga qué cambió."),
    reinforce="Practica tu presentación en voz alta frente a una persona de tu casa.",
    extend="Escribe qué cambiarías en tu propia respuesta de la clase 5 después de revisar con la pauta.",
)

# ================================================================ OA 06 · CUADRÍCULAS
MAPA0 = ("Plano de una polis en una cuadrícula de 4 columnas (A, B, C, D, de izquierda a derecha) y 4 filas (1, 2, 3, 4, de arriba hacia abajo). "
         "Cada casilla se nombra con su columna y su fila, como B2. Lugares: templo en A1, fuente en D1, ágora en B2, olivo en C2, taller de alfarero en A3, teatro en C3, escuela en A4, puerto en D4. "
         "Las demás casillas están vacías.")
MAPA = (MAPA0 + " En el plano, el norte está arriba, el sur abajo, el este a la derecha y el oeste a la izquierda.")
# ---------------------------------------------------------------- clase 1
register(
    OA6, 1,
    materials="Lápiz y papel. El plano está descrito en cada ejercicio. Puedes dibujarlo en tu cuaderno con 4 columnas y 4 filas.",
    use="Aprenderé a ubicar lugares en una cuadrícula usando columnas y filas. Sirve para decir con exactitud dónde está algo en un plano.",
    prior=["Sé que un plano muestra un lugar visto desde arriba.", "Sé las letras A, B, C y D y los números hasta 4."],
    explain=[
        "Una cuadrícula es un dibujo con líneas que forman casillas, como un tablero. Las columnas son las líneas de casillas que van de arriba hacia abajo y se nombran con letras. Las filas son las líneas de casillas que van de izquierda a derecha y se nombran con números.",
        "Para decir dónde está algo usamos una coordenada, que es el nombre de una casilla. Se escribe primero la letra de la columna y luego el número de la fila. Por ejemplo, B2 significa columna B, fila 2. Las líneas de referencia son las líneas de la cuadrícula: separan las columnas y las filas y ayudan a leer el plano.",
        "Con una sola referencia no basta. Si dices «columna C», hay varias casillas posibles. Si dices C2, hay solo una. Por eso necesitamos la columna y la fila juntas.",
    ],
    vocab=[("cuadrícula", "dibujo con líneas que forman casillas"), ("columna", "línea de casillas de arriba hacia abajo, con letra"), ("fila", "línea de casillas de lado a lado, con número"), ("coordenada", "nombre de una casilla, como B2"), ("casilla", "cada cuadrito de la cuadrícula")],
    worked=[
        {"title": "Leer una coordenada", "problem": f"{MAPA0} ¿Qué hay en la casilla B2?", "steps": ["B es la columna y 2 es la fila.", "Busco la columna B y la fila 2."], "answer": "El ágora"},
        {"title": "Decir una coordenada", "problem": f"{MAPA0} ¿En qué casilla está el teatro?", "steps": ["Busco el teatro en el plano: está en la columna C.", "Veo que está en la fila 3, así que escribo primero la letra y luego el número."], "answer": "C3"},
    ],
    mistakes=[
        {"wrong": "Decir la fila antes que la columna, como 2B.", "why": "Se confunde el orden.", "fix": "Primero la letra de la columna y luego el número de la fila."},
        {"wrong": "Usar solo la columna para decir dónde está algo.", "why": "Se cree que basta.", "fix": "Usa la columna y la fila juntas."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA0} ¿Qué hay en la casilla B2?", "el ágora", "B2 es columna B, fila 2."),
            ex(f"{MAPA0} ¿En qué casilla está el teatro?", "C3", "Está en la columna C y la fila 3."),
            ex(f"{MAPA0} ¿Qué hay en la casilla D1?", "la fuente", "D1 es columna D, fila 1."),
        ],
        "understand": [
            ex(f"{MAPA0} ¿En qué columna está el puerto?", "D", "Su casilla es D4."),
            ex(f"{MAPA0} ¿En qué fila está la escuela?", "la fila 4", "Su casilla es A4."),
            ex("La casilla B3 significa: A) columna B, fila 3. B) columna 3, fila B. ¿Cuál es correcta?", "A", "Primero va la letra de la columna."),
        ],
        "apply": [
            ex(f"{MAPA0} Nombra los lugares de la fila 1.", "el templo y la fuente", "Están en A1 y D1."),
            ex(f"{MAPA0} Nombra los lugares de la columna C.", "el olivo y el teatro", "Están en C2 y C3."),
            ex(f"{MAPA0} ¿Qué hay en la casilla B3?", "nada, está vacía", "No aparece en la lista de lugares."),
        ],
        "reason": [
            ex(f"{MAPA0} Tomás dice que el olivo está en B3. ¿Dónde está en realidad?", "en C2", "El olivo está en la columna C, fila 2."),
            ex("¿Por qué sirven una columna y una fila juntas, y no solo una de ellas?", "porque con una sola hay varias casillas posibles", "Juntas indican una sola casilla."),
        ],
        "challenge": [
            ex(f"{MAPA0} Nombra los tres lugares de la columna A.", "el templo, el taller de alfarero y la escuela", "Están en A1, A3 y A4."),
            ex(f"{MAPA0} Escribe la coordenada del ágora, de la escuela y del puerto.", "B2, A4 y D4", "Cada lugar tiene una columna y una fila."),
        ],
    },
    context=[ex(f"{MAPA0} Rosa está parada en el ágora y Pedro está en el puerto. Escribe la coordenada de cada persona.", "Rosa en B2 y Pedro en D4", "Cada persona está en la casilla de su lugar.")],
    selfcheck=[
        ex("¿Qué es una columna?", "una línea de casillas de arriba hacia abajo, con letra", "Así se nombra en el plano."),
        ex("¿Qué es una fila?", "una línea de casillas de lado a lado, con número", "Se numera 1, 2, 3 y 4."),
        ex("¿Se dice primero la columna o la fila?", "la columna", "B2 es columna B y fila 2."),
    ],
    open_task=task(
        f"Dibuja una cuadrícula de 4 columnas y 4 filas. Marca la letra de cada columna y el número de cada fila. Ubica y rotula los ocho lugares. {MAPA0}",
        "Cuadrícula con A a D arriba y 1 a 4 a la izquierda. Templo en A1, fuente en D1, ágora en B2, olivo en C2, taller en A3, teatro en C3, escuela en A4, puerto en D4.",
        ["cuatro columnas con letra", "cuatro filas con número", "ocho lugares bien ubicados"], ["cuadrícula dibujada"], ["intercambiar columna y fila", "ubicar un lugar en otra casilla"],
        "Pide que diga la coordenada de dos lugares sin mirar la lista."),
    reinforce="Di en voz alta la coordenada de cada lugar del plano.",
    extend="Dibuja una cuadrícula de tu pieza o de tu sala y ubica tres objetos con coordenadas.",
)

# ---------------------------------------------------------------- clase 2
register(
    OA6, 2,
    materials="Lápiz y papel. El plano está descrito en cada ejercicio.",
    use="Aprenderé los puntos cardinales y cómo se usan en un plano. Sirve para decir hacia dónde queda un lugar respecto de otro.",
    prior=["Sé leer coordenadas en una cuadrícula.", "Sé qué es arriba, abajo, derecha e izquierda."],
    explain=[
        "Los puntos cardinales son el norte, el sur, el este y el oeste. Sirven para orientarnos. En un plano, el norte suele estar arriba y el sur abajo. El este está a la derecha y el oeste a la izquierda. Una forma de recordar es que el sol sale por el este y se pone por el oeste.",
        "Los puntos cardinales sirven para decir dónde queda un lugar respecto de otro. Por ejemplo, si una casilla está más arriba que otra en el plano, queda al norte. Si está más a la derecha, queda al este. Siempre se compara un lugar con otro.",
        "Una brújula es un instrumento que señala el norte. Si miras hacia el norte, el este queda a tu derecha y el oeste a tu izquierda. En el plano de esta clase usamos la regla de que el norte está arriba.",
    ],
    vocab=[("punto cardinal", "norte, sur, este u oeste"), ("norte", "dirección hacia arriba en el plano"), ("sur", "dirección hacia abajo en el plano, opuesta al norte"), ("este", "dirección hacia la derecha, por donde sale el sol"), ("oeste", "dirección hacia la izquierda, por donde se pone el sol")],
    worked=[
        {"title": "Norte y sur", "problem": f"{MAPA} ¿La fuente (D1) está al norte o al sur del puerto (D4)?", "steps": ["Están en la misma columna D.", "La fila 1 está más arriba que la fila 4.", "Arriba es norte."], "answer": "Al norte"},
        {"title": "Este y oeste", "problem": f"{MAPA} ¿El templo (A1) está al este o al oeste de la fuente (D1)?", "steps": ["Están en la misma fila 1.", "A está más a la izquierda que D.", "Izquierda es oeste."], "answer": "Al oeste"},
    ],
    mistakes=[
        {"wrong": "Confundir este con oeste.", "why": "Se mezclan las direcciones laterales.", "fix": "Recuerda: este a la derecha, oeste a la izquierda, como en el plano."},
        {"wrong": "Decir norte hacia abajo porque «la fila 1 es la primera».", "why": "Se confunde el número con la dirección.", "fix": "En el plano, el norte siempre está arriba, aunque la fila sea 1."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA} ¿Dónde está el norte en el plano?", "arriba", "Así lo define el plano."),
            ex(f"{MAPA} ¿Dónde está el este en el plano?", "a la derecha", "Así lo define el plano."),
            ex(f"{MAPA} ¿Qué punto cardinal queda a la izquierda?", "el oeste", "Así lo define el plano."),
        ],
        "understand": [
            ex("¿Qué punto cardinal es opuesto al norte?", "el sur", "Son direcciones contrarias."),
            ex("¿Por dónde sale el sol: por el este o por el oeste?", "por el este", "Así se recuerda el este."),
            ex("¿Para qué sirve una brújula?", "para señalar el norte", "Ayuda a orientarse."),
        ],
        "apply": [
            ex(f"{MAPA} El teatro está en C3 y el olivo en C2. ¿El teatro queda al norte o al sur del olivo?", "al sur", "La fila 3 está más abajo que la fila 2."),
            ex(f"{MAPA} La escuela está en A4 y el puerto en D4. ¿La escuela queda al este o al oeste del puerto?", "al oeste", "A está más a la izquierda que D."),
            ex(f"{MAPA} ¿Qué lugar está al este del ágora (B2), en la misma fila?", "el olivo", "Está en C2, a la derecha."),
        ],
        "reason": [
            ex(f"{MAPA} Ana dice: «El templo (A1) está al sur de la escuela (A4)». Corrígela.", "El templo está al norte de la escuela", "La fila 1 está arriba de la fila 4."),
            ex(f"{MAPA} Luis dice que el puerto (D4) está más al sur que el teatro (C3). ¿Tiene razón?", "sí", "La fila 4 está más abajo que la fila 3."),
        ],
        "challenge": [
            ex(f"{MAPA} Ordena de norte a sur los lugares de la columna A: escuela, templo, taller de alfarero.", "templo, taller de alfarero, escuela", "Están en A1, A3 y A4."),
            ex(f"{MAPA} Un niño camina por la fila 1 desde el templo (A1) hasta la fuente (D1). ¿Hacia qué punto cardinal camina?", "hacia el este", "Va hacia la derecha."),
        ],
    },
    context=[ex("Miras hacia el norte con una brújula. ¿De qué lado te queda el este?", "a tu derecha", "Si miras al norte, el este queda a la derecha.")],
    selfcheck=[
        ex("¿Cuáles son los cuatro puntos cardinales?", "norte, sur, este y oeste", "Son los de la ficha."),
        ex("¿Dónde queda el sur en el plano?", "abajo", "Es el opuesto al norte."),
        ex("En Historia: ¿Por dónde sale el sol?", "por el este", "Así se recuerda."),
    ],
    open_task=task(
        f"Dibuja el plano de la clase con una rosa de los vientos: una cruz con N arriba, S abajo, E a la derecha y O a la izquierda. Escribe tres frases que digan dónde queda un lugar respecto de otro. {MAPA}",
        "Rosa con N, S, E y O. El teatro está al sur del olivo. La escuela está al oeste del puerto. El templo está al norte de la escuela.",
        ["rosa de los vientos correcta", "tres frases correctas", "usa los puntos cardinales"], ["plano con rosa", "tres frases"], ["intercambiar este y oeste", "decir norte para abajo"],
        "Pide que diga una frase con cada punto cardinal."),
    reinforce="Camina en tu casa y di hacia qué punto cardinal te mueves, si el norte está hacia la ventana principal. Es un juego de práctica.",
    extend="Dibuja una rosa de los vientos y ubica en ella tu casa y tu escuela de manera aproximada.",
)

# ---------------------------------------------------------------- clase 3
register(
    OA6, 3,
    materials="Lápiz y papel. El plano está descrito en cada ejercicio.",
    use="Aprenderé a describir un recorrido paso a paso, para que otra persona pueda repetirlo. Sirve para dar indicaciones claras.",
    prior=["Sé leer coordenadas y puntos cardinales.", "Sé contar casillas."],
    explain=[
        "Un recorrido es el camino que haces de un lugar a otro. Para que otra persona pueda repetirlo, hay que decir desde dónde sale, hacia qué punto cardinal avanza y cuántas casillas. Por ejemplo: «Desde el ágora, avanza 1 casilla al este».",
        "Cada paso mueve una casilla. Al norte, la fila baja de número: de C3 pasas a C2. Al sur, la fila sube de número: de C2 pasas a C3. Al este, la letra de la columna avanza: de B2 pasas a C2. Al oeste, la letra retrocede: de C2 pasas a B2.",
        "Un buen recorrido es claro y completo. Dice el punto de partida, cada paso con su dirección y cuántas casillas, y el punto de llegada. Para comprobarlo, lo repites paso a paso en el plano.",
    ],
    vocab=[("recorrido", "camino de un lugar a otro, paso a paso"), ("punto de partida", "lugar desde donde se sale"), ("punto de llegada", "lugar donde se termina"), ("paso", "movimiento de una casilla"), ("indicación", "instrucción para llegar a un lugar")],
    worked=[
        {"title": "Seguir un recorrido", "problem": f"{MAPA} Sales del ágora (B2) y avanzas 1 casilla al este. ¿Dónde llegas?", "steps": ["Al este, la letra avanza: de B pasa a C.", "La fila sigue siendo 2: llegas a C2."], "answer": "C2, el olivo"},
        {"title": "Crear un recorrido", "problem": f"{MAPA} Describe un recorrido del ágora (B2) al taller de alfarero (A3).", "steps": ["De B2 a A2: 1 casilla al oeste.", "De A2 a A3: 1 casilla al sur."], "answer": "1 casilla al oeste y 1 casilla al sur"},
    ],
    mistakes=[
        {"wrong": "Dar un recorrido sin decir cuántas casillas.", "why": "Se piensa que se entiende solo.", "fix": "Siempre di la dirección y el número de casillas."},
        {"wrong": "Mover al norte aumentando el número de la fila.", "why": "Se confunde número con dirección.", "fix": "Al norte, el número de la fila baja; al sur, sube."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA} Sales del ágora (B2) y avanzas 1 casilla al este. ¿Dónde llegas?", "al olivo, en C2", "Al este avanza la letra."),
            ex(f"{MAPA} Sales del olivo (C2) y avanzas 1 casilla al sur. ¿Dónde llegas?", "al teatro, en C3", "Al sur el número de la fila sube."),
            ex(f"{MAPA} Sales del templo (A1) y avanzas 1 casilla al este. ¿Dónde llegas?", "a B1, una casilla vacía", "A pasa a B en la fila 1."),
        ],
        "understand": [
            ex("¿Qué tres datos necesita una indicación clara?", "punto de partida, dirección con casillas y llegada", "Son los que permiten repetir el recorrido."),
            ex("Al avanzar hacia el este, ¿qué cambia: la letra de la columna o el número de la fila?", "la letra de la columna", "Al este cambia la columna."),
            ex("Al avanzar hacia el sur, ¿qué cambia: la letra de la columna o el número de la fila?", "el número de la fila", "Al sur cambia la fila."),
        ],
        "apply": [
            ex(f"{MAPA} Desde el teatro (C3) avanzas 1 casilla al este y luego 1 casilla al sur. ¿Dónde llegas?", "al puerto, en D4", "C3 pasa a D3 y luego a D4."),
            ex(f"{MAPA} Desde la escuela (A4) avanzas 2 casillas al norte. ¿En qué casilla llegas?", "A2", "A4 pasa a A3 y luego a A2."),
            ex(f"{MAPA} Desde la escuela (A4) avanzas 1 casilla al norte y luego 2 casillas al este. ¿Dónde llegas?", "al teatro, en C3", "A4 pasa a A3 y luego a C3."),
        ],
        "reason": [
            ex(f"{MAPA} Marta dice: «Para ir de B2 a D2 avanza 2 casillas al oeste». Corrígela.", "Debe avanzar 2 casillas al este", "D está a la derecha de B."),
            ex(f"{MAPA} Dos amigos van del templo (A1) al ágora (B2): uno va 1 casilla al este y luego 1 al sur; el otro, 1 al sur y luego 1 al este. ¿Los dos llegan al ágora?", "sí", "Ambos recorridos suman 1 al este y 1 al sur."),
        ],
        "challenge": [
            ex(f"{MAPA} Escribe un recorrido del templo (A1) al teatro (C3). Usa solo este y sur.", "2 casillas al este y 2 casillas al sur, en cualquier orden", "A1 pasa a C1 y luego a C3, o al revés."),
            ex(f"{MAPA} Desde el ágora (B2) avanzas 2 casillas al este y luego 2 casillas al sur. ¿Dónde llegas?", "al puerto, en D4", "B2 pasa a D2 y luego a D4."),
        ],
    },
    context=[ex("Un turista está en el ágora (B2) y quiere ir al puerto (D4). ¿Qué recorrido le sirve? A) 2 casillas al este y 2 al sur. B) 2 casillas al oeste y 2 al sur.", "A", "Al este está D, y al sur está la fila 4.")],
    selfcheck=[
        ex("¿Qué es un punto de partida?", "el lugar desde donde se sale", "Es el comienzo del recorrido."),
        ex("Al ir al norte, ¿el número de la fila sube o baja?", "baja", "El norte está arriba."),
        ex("¿Cómo compruebas un recorrido?", "repitiéndolo paso a paso en el plano", "Así se ve si llega bien."),
    ],
    open_task=task(
        f"Escribe un recorrido desde la escuela (A4) hasta la fuente (D1). Cada paso debe decir dirección y casillas. Después, compruébalo en tu plano. {MAPA}",
        "Desde A4: 3 casillas al norte (A1), 3 casillas al este (D1). Comprobación: A4 pasa por A3, A2, A1; luego B1, C1, D1. Llega a la fuente.",
        ["partida y llegada nombradas", "cada paso con dirección y casillas", "recorrido comprobado"], ["recorrido escrito", "plano con la ruta"], ["olvidar el número de casillas", "mezclar este y oeste"],
        "Pide que lo lea a otra persona y que esa persona lo siga con el dedo."),
    reinforce="Dile a alguien en casa un recorrido en tu cuaderno y pide que lo siga.",
    extend="Inventa un recorrido de cuatro pasos que parta y termine en el ágora.",
)

# ---------------------------------------------------------------- clase 4
register(
    OA6, 4,
    materials="Lápiz y papel. El plano y las frases están escritos en cada ejercicio.",
    use="Aprenderé a comprobar y corregir ubicaciones en un plano. Sirve para detectar errores y dar indicaciones más seguras.",
    prior=["Sé leer coordenadas.", "Sé usar puntos cardinales y recorridos."],
    explain=[
        "Cuando alguien da una ubicación, podemos comprobarla. Miramos la coordenada y el punto cardinal, y vemos si coinciden con el plano. Si no coinciden, hay un error y lo corregimos. Corregir es una buena práctica, no una falla.",
        "Para comprobar una frase como «El templo está al norte de la escuela», pregunta: ¿dónde está el templo?, ¿dónde está la escuela?, ¿cuál está más arriba? Si el templo está más arriba, la frase es correcta.",
        "Los errores más comunes son: invertir la columna y la fila, confundir este con oeste, o contar mal las casillas. Para evitarlos, usa dos referencias: la coordenada y un punto cardinal. Al corregir, explica en qué parte estaba el error.",
    ],
    vocab=[("comprobar", "revisar si algo está bien"), ("corregir", "arreglar un error"), ("error", "algo que está mal"), ("referencia", "dato que ayuda a ubicar algo"), ("verdadera", "que coincide con el plano")],
    worked=[
        {"title": "Comprobar una frase", "problem": f"{MAPA} Revisa: «La fuente está en D1, al este del templo».", "steps": ["La fuente está en D1 y el templo en A1.", "D está a la derecha de A, así que está al este."], "answer": "Es verdadera"},
        {"title": "Corregir una frase", "problem": f"{MAPA} Revisa: «El puerto está al norte de la escuela». Puerto D4, escuela A4.", "steps": ["Están en la misma fila 4.", "La diferencia es de columnas: D está a la derecha de A.", "El puerto está al este de la escuela."], "answer": "Es falsa; el puerto está al este de la escuela"},
    ],
    mistakes=[
        {"wrong": "Aceptar una ubicación sin mirar el plano.", "why": "Se confía en la persona.", "fix": "Siempre compruébala con las coordenadas."},
        {"wrong": "Corregir sin decir cuál era el error.", "why": "Se arregla en silencio.", "fix": "Explica qué estaba mal para no repetirlo."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA} Revisa: «El ágora está en B2». ¿Es verdadera o falsa?", "verdadera", "El ágora está en B2."),
            ex(f"{MAPA} Revisa: «El olivo está en C3». ¿Es verdadera o falsa?", "falsa", "El olivo está en C2."),
            ex(f"{MAPA} Revisa: «El templo está en la fila 1». ¿Es verdadera o falsa?", "verdadera", "El templo está en A1."),
        ],
        "understand": [
            ex("¿Qué dos referencias conviene usar para evitar errores?", "una coordenada y un punto cardinal", "Se apoyan entre sí."),
            ex("¿Qué error es común al leer una coordenada?", "invertir la columna y la fila", "Se dice 2B en vez de B2."),
            ex("Corregir un error, ¿es una falla o una buena práctica?", "una buena práctica", "Ayuda a no repetirlo."),
        ],
        "apply": [
            ex(f"{MAPA} Revisa: «La fuente está al oeste del templo». ¿Es verdadera o falsa?", "falsa", "La fuente (D1) está al este del templo (A1)."),
            ex(f"{MAPA} Revisa: «La escuela está al sur del templo». ¿Es verdadera o falsa?", "verdadera", "La escuela (A4) está más abajo que el templo (A1)."),
            ex(f"{MAPA} Revisa: «El puerto está en la misma columna que la fuente». ¿Es verdadera o falsa?", "verdadera", "Ambos están en la columna D."),
        ],
        "reason": [
            ex(f"{MAPA} Pedro dice: «El teatro está en 3C». ¿Qué error cometió y cómo se corrige?", "invirtió el orden; debe ser C3", "Primero va la letra."),
            ex(f"{MAPA} Camila dice: «El olivo está al oeste del ágora». ¿Es correcto?", "no, está al este", "El olivo (C2) está a la derecha del ágora (B2)."),
        ],
        "challenge": [
            ex(f"{MAPA} Corrige: «Desde el templo (A1), avanza 2 casillas al sur y llegarás al ágora». Di dónde llegas realmente.", "A3, el taller de alfarero", "A1 pasa a A2 y luego a A3."),
            ex(f"{MAPA} Alguien dice: «El taller de alfarero (A3) está al este de la escuela (A4)». Corrige con el punto cardinal correcto.", "está al norte de la escuela", "A3 está en la fila de arriba de A4."),
        ],
    },
    context=[ex("Un guía dice: «El teatro (C3) queda al norte de la fuente (D1)». Compruébalo. ¿Es verdadero o falso?", "falso, el teatro queda al sur de la fuente", "La fila 3 está más abajo que la fila 1.")],
    selfcheck=[
        ex("¿Qué haces para comprobar una ubicación?", "miro la coordenada y el punto cardinal en el plano", "Así veo si coinciden."),
        ex("¿Qué se debe decir al corregir?", "en qué estaba el error", "Para no repetirlo."),
        ex("¿Una sola referencia es más segura que dos?", "no, dos son más seguras", "Se apoyan entre sí."),
    ],
    open_task=task(
        f"Escribe cuatro frases sobre el plano: dos verdaderas y dos falsas, sin decir cuáles son. Pide a otra persona que las revise y corrija las falsas. {MAPA}",
        "1) La escuela está al sur del templo (verdadera). 2) La fuente está en C1 (falsa: está en D1). 3) El olivo está al este del ágora (verdadera). 4) El puerto está en la fila 3 (falsa: está en la fila 4).",
        ["cuatro frases", "dos verdaderas y dos falsas", "correcciones con explicación"], ["frases y correcciones"], ["frases ambiguas", "no corregir"],
        "Pregunta cómo supo qué frases eran falsas."),
    reinforce="Revisa el recorrido de la clase anterior y comprueba que llegue donde dice.",
    extend="Haz un plano de 3 por 3 de tu sala y escribe dos frases verdaderas y una falsa.",
)

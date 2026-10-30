"""Material del estudiante de 3.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (Grecia antigua) y OA 02 (Roma antigua)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA1 = "HI03 OA 01"
OA2 = "HI03 OA 02"

# ================================================================ OA 01 · GRECIA
# ---------------------------------------------------------------- clase 1
G1 = ("Ficha de Grecia: Grecia está en el sur de Europa, junto al mar Mediterráneo. Su territorio tiene una parte en el continente y muchas islas. "
      "Los griegos de la Antigüedad vivieron hace más de 2.000 años. En esa época no existía un solo país griego: había muchas ciudades independientes, "
      "llamadas polis. Atenas, Esparta y Corinto eran tres de ellas.")
register(
    OA1, 1,
    materials="Lápiz y papel. La ficha de Grecia está escrita en cada ejercicio. Un mapa de Europa de tu casa o de un libro sirve, pero no es necesario.",
    use="Aprenderé dónde y cuándo vivieron los griegos de la Antigüedad. Sirve para ubicar sus historias en el mapa y en el tiempo.",
    prior=["Sé que el pasado es antes que hoy.", "Sé que un mapa muestra lugares."],
    explain=[
        "La Antigüedad es un tiempo muy lejano, de hace más de dos mil años. En ese tiempo vivieron los griegos antiguos. Ellos no tenían autos ni electricidad, y muchas cosas de su vida eran muy distintas a las de hoy.",
        "Grecia está en el sur de Europa, junto al mar Mediterráneo. Una parte de su territorio está en el continente y otra parte son islas. Para ubicarla en un mapa, buscas Europa y miras hacia el sur.",
        "Los griegos antiguos no formaban un solo país. Vivían en muchas ciudades independientes llamadas polis. Cada polis tenía sus propias leyes y su propio gobierno. Atenas, Esparta y Corinto fueron polis. Compartían el idioma y varias costumbres, pero a veces eran muy distintas entre sí.",
    ],
    vocab=[("Antigüedad", "tiempo muy lejano, de hace más de dos mil años"), ("polis", "ciudad independiente de la Grecia antigua"), ("Mediterráneo", "mar que está entre Europa, África y Asia"), ("isla", "tierra rodeada de agua por todos lados"), ("continente", "gran masa de tierra, como Europa")],
    worked=[
        {"title": "Decir dónde", "problem": f"{G1} ¿Dónde estaba Grecia?", "steps": ["Busco en la ficha las palabras sur y Europa.", "Leo que está en el sur de Europa, junto al mar Mediterráneo."], "answer": "En el sur de Europa, junto al mar Mediterráneo"},
        {"title": "Decir cuándo", "problem": f"{G1} ¿Cuándo vivieron los griegos de la Antigüedad?", "steps": ["Busco una expresión de tiempo en la ficha.", "Dice «hace más de 2.000 años»."], "answer": "Hace más de 2.000 años"},
    ],
    mistakes=[
        {"wrong": "Decir que Grecia antigua era un solo país como Chile.", "why": "Se piensa en los países de hoy.", "fix": "Recuerda que había muchas polis independientes."},
        {"wrong": "Pensar que los griegos antiguos vivieron hace pocos años.", "why": "Cuesta imaginar tanto tiempo.", "fix": "Piensa en una línea de tiempo: primero los griegos, mucho después tus abuelos, y al final tú."},
    ],
    tiers={
        "recovery": [
            ex(f"{G1} ¿En qué continente está Grecia?", "Europa", "La ficha dice que está en el sur de Europa."),
            ex(f"{G1} ¿Qué mar está junto a Grecia?", "el mar Mediterráneo", "La ficha dice que Grecia está junto al Mediterráneo."),
            ex(f"{G1} ¿Cómo se llamaban las ciudades independientes de los griegos?", "polis", "La ficha llama polis a esas ciudades."),
        ],
        "understand": [
            ex(f"{G1} ¿Los griegos de la Antigüedad vivieron hace mucho o hace poco?", "hace mucho", "La ficha dice que fue hace más de 2.000 años."),
            ex(f"{G1} Atenas y Esparta, ¿eran la misma polis o polis distintas?", "polis distintas", "Cada una era una ciudad independiente."),
            ex("Elige la frase correcta. A) La Grecia antigua era un solo país con un solo gobierno. B) La Grecia antigua tenía muchas polis independientes.", "B", "Cada polis tenía sus propias leyes y gobierno."),
        ],
        "apply": [
            ex("Ordena de lo más antiguo a lo más reciente: tus abuelos cuando eran niños, los griegos de la Antigüedad, tú hoy.", "los griegos de la Antigüedad, tus abuelos cuando eran niños, tú hoy", "Los griegos vivieron hace más de 2.000 años, mucho antes que tus abuelos."),
            ex(f"{G1} Quieres encontrar Grecia en un mapa de Europa. ¿Buscas en el norte o en el sur del mapa?", "en el sur", "La ficha ubica Grecia en el sur de Europa."),
            ex(f"{G1} Marta puso un punto para Grecia en el extremo norte de Europa. ¿Hacia qué dirección debe mover el punto?", "hacia el sur", "Grecia está en el sur de Europa."),
        ],
        "reason": [
            ex(f"{G1} Tomás dice: «Los griegos antiguos eran un solo país, como Chile». Corrige su error con un dato de la ficha.", "Eran muchas polis independientes", "La ficha dice que no existía un solo país griego."),
            ex("Ana dice que un griego de la Antigüedad pudo ver un auto. ¿Es posible? Explica con el tiempo.", "No, porque vivió hace más de 2.000 años y los autos no existían", "Los autos son de un tiempo mucho más cercano a hoy."),
        ],
        "challenge": [
            ex(f"{G1} Clasifica cada dato en «dónde» o «cuándo»: a) en el sur de Europa; b) hace más de 2.000 años; c) junto al mar Mediterráneo.", "a: dónde; b: cuándo; c: dónde", "a y c nombran lugares; b nombra un tiempo."),
            ex(f"{G1} Luis dice: «Atenas y Esparta eran barrios de una misma ciudad». Eva dice: «Eran ciudades independientes». ¿Quién tiene razón?", "Eva", "La ficha dice que eran polis independientes."),
        ],
    },
    context=[ex("En un museo, un cartel dice: «Vasija de Atenas, hace más de 2.000 años». ¿Qué dato del cartel dice el lugar y cuál dice el tiempo?", "Lugar: Atenas. Tiempo: hace más de 2.000 años", "Atenas es una polis; la otra frase mide el tiempo.")],
    selfcheck=[
        ex(f"{G1} ¿Dónde está Grecia?", "en el sur de Europa", "Así lo dice la ficha."),
        ex("¿Qué es una polis?", "una ciudad independiente de la Grecia antigua", "Cada polis tenía su gobierno y sus leyes."),
        ex("¿La Grecia antigua era un solo país o muchas polis?", "muchas polis", "No había un solo gobierno para todos."),
    ],
    open_task=task(
        f"Haz dos dibujos. Primero, una línea de tiempo con tres puntos: «Grecia antigua», «mis abuelos de niños» y «hoy». Segundo, un mapa simple: dibuja un rectángulo que sea Europa y marca un punto en la parte de abajo (el sur) para Grecia, con una línea ondulada de mar a su lado. {G1}",
        "Línea con tres puntos en orden: Grecia antigua (muy a la izquierda), mis abuelos de niños, hoy. Mapa: rectángulo con un punto abajo llamado Grecia y el mar al lado.",
        ["orden correcto en la línea de tiempo", "Grecia en el sur del mapa", "mar marcado junto a Grecia"], ["línea de tiempo dibujada", "mapa simple dibujado"], ["poner a Grecia en el norte", "poner a los griegos después de los abuelos"],
        "Pide que diga en voz alta una cosa del tiempo y una del lugar. Si pone a Grecia en el norte, vuelve a leer la ficha."),
    reinforce="Repite en voz alta: dónde está Grecia, cuándo vivieron los griegos antiguos y qué es una polis.",
    extend="Escribe dos diferencias entre vivir en una polis griega y vivir en un país como Chile hoy.",
)

# ---------------------------------------------------------------- clase 2
G2 = ("Fuentes sobre la vida cotidiana en Atenas: (1) una vasija de cerámica con forma de jarra que servía para guardar aceite de oliva; "
      "(2) un texto antiguo que dice que los hombres usaban una túnica de lana o de lino llamada quitón; "
      "(3) las ruinas de casas con habitaciones alrededor de un patio; "
      "(4) el ágora, una plaza donde las personas compraban, vendían y conversaban; "
      "(5) restos de comida: semillas de aceituna y de higos. Una fuente es cualquier cosa que entrega información sobre el pasado.")
register(
    OA1, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé cómo sabemos que los griegos comían, vestían y vivían de cierta manera. Sirve para separar lo que dice la fuente de lo que solo imaginamos.",
    prior=["Sé dónde y cuándo vivieron los griegos antiguos.", "Sé qué es una polis."],
    explain=[
        "Los historiadores estudian el pasado con fuentes. Una fuente puede ser un objeto, como una vasija o una moneda, un texto escrito, unas ruinas o una estatua. Cada fuente es una pista. Una pista sola no cuenta toda la historia.",
        "Gracias a las fuentes sabemos algunas cosas de la vida cotidiana en Atenas. Se comía pan, pescado, queso, aceitunas e higos, y se usaba mucho aceite de oliva. Se vestía una túnica de lana o de lino. Las casas tenían habitaciones alrededor de un patio. En el ágora, la plaza central, se compraba, se vendía y se conversaba.",
        "Una buena pregunta para una fuente es: ¿qué me dice con seguridad? Por ejemplo, una jarra de aceite dice que se guardaba aceite. No dice cuántas personas la usaban. Lo que no sabemos con seguridad no se debe afirmar como si fuera un hecho.",
    ],
    vocab=[("fuente", "cosa que entrega información sobre el pasado"), ("ruinas", "restos de un edificio muy antiguo"), ("ágora", "plaza de una polis griega donde se compraba, se vendía y se conversaba"), ("quitón", "túnica de lana o lino que usaban los griegos"), ("cotidiano", "de todos los días")],
    worked=[
        {"title": "Usar una fuente", "problem": f"{G2} ¿Qué nos dice la fuente 1?", "steps": ["Leo la fuente 1: una vasija en forma de jarra para aceite.", "Digo solo lo que muestra: se guardaba aceite de oliva."], "answer": "Se guardaba aceite de oliva"},
        {"title": "Una fuente que no alcanza", "problem": f"{G2} ¿Podemos saber con la fuente 5 cuántas personas comían aceitunas?", "steps": ["La fuente 5 son restos de semillas.", "Muestra qué se comía, pero no cuántas personas."], "answer": "No, solo nos dice que se comían aceitunas e higos"},
    ],
    mistakes=[
        {"wrong": "Decir que una fuente cuenta todo sobre la vida griega.", "why": "Se cree que una pista basta.", "fix": "Usa varias fuentes y di solo lo que cada una muestra."},
        {"wrong": "Mezclar lo que dice la fuente con lo que yo imagino.", "why": "Se rellena con ideas propias.", "fix": "Separa: «la fuente muestra…» y «yo creo que…»."},
    ],
    tiers={
        "recovery": [
            ex(f"{G2} ¿Qué fuente muestra que se vestía una túnica?", "la fuente 2", "El texto antiguo habla del quitón."),
            ex(f"{G2} ¿Cómo se llamaba la plaza donde se compraba y se vendía?", "ágora", "La fuente 4 la llama ágora."),
            ex("Una fuente, ¿es una cosa que entrega información sobre el pasado o un tipo de comida?", "una cosa que entrega información sobre el pasado", "Esa es la definición de fuente."),
        ],
        "understand": [
            ex(f"{G2} ¿Qué nos dicen las ruinas de la fuente 3 sobre las casas?", "que tenían habitaciones alrededor de un patio", "La fuente 3 describe esa forma."),
            ex(f"{G2} ¿Qué dos alimentos se conocen por la fuente 5?", "aceitunas e higos", "Se encontraron semillas de ambos."),
            ex(f"{G2} ¿De qué dos materiales era el quitón?", "lana o lino", "La fuente 2 nombra esos materiales."),
        ],
        "apply": [
            ex(f"{G2} Lee la frase: «En Atenas había una plaza para comprar y conversar». ¿Qué fuente la apoya?", "la fuente 4", "El ágora era esa plaza."),
            ex(f"{G2} Una niña dice que en Atenas se guardaba aceite de oliva en jarras. ¿Qué fuente la respalda?", "la fuente 1", "La vasija servía para guardar aceite."),
            ex(f"{G2} Une cada fuente con lo que muestra: A) fuente 3; B) fuente 5. 1) lo que se comía; 2) cómo eran las casas.", "A con 2; B con 1", "Las ruinas muestran casas y los restos muestran comida."),
        ],
        "reason": [
            ex(f"{G2} Pedro dice: «La fuente 1 prueba que todos los atenienses eran ricos». ¿Se puede afirmar eso?", "No, una jarra de aceite no dice cuánto dinero tenían", "La fuente solo muestra que se guardaba aceite."),
            ex(f"{G2} Clara afirma: «Los griegos comían mucho pescado». ¿Alguna fuente de la lista lo dice?", "No, ninguna de las cinco lo menciona", "Habría que buscar otra fuente para afirmarlo."),
        ],
        "challenge": [
            ex(f"{G2} Separa lo que dice la fuente de lo que se imagina. Frase A: «Se guardaba aceite en jarras». Frase B: «Los niños jugaban con las jarras». ¿Cuál se apoya en la fuente 1?", "A", "La frase B no tiene respaldo en la fuente."),
            ex(f"{G2} Elige la pregunta que las cinco fuentes NO pueden responder. A) ¿Dónde se conversaba? B) ¿Cuál era el nombre del vecino de una familia ateniense?", "B", "Las fuentes no entregan nombres de vecinos."),
        ],
    },
    context=[ex("Una profesora muestra una foto de las ruinas de una casa griega y dice: «Aquí vivía una familia feliz». ¿Qué parte de su frase no puede saberse solo con las ruinas?", "que era una familia feliz", "Las ruinas muestran la casa, no los sentimientos.")],
    selfcheck=[
        ex("¿Qué es el ágora?", "una plaza donde se compraba, se vendía y se conversaba", "Era el centro de la vida pública."),
        ex(f"{G2} ¿Con qué se vestían los hombres, según la fuente 2?", "con una túnica de lana o lino llamada quitón", "La fuente 2 lo dice."),
        ex("Al usar una fuente, ¿se debe decir solo lo que ella muestra o también todo lo que yo imagine?", "solo lo que ella muestra", "Lo demás sería una suposición."),
    ],
    open_task=task(
        f"Elige dos de las cinco fuentes de esta ficha. {G2} Escribe para cada una: qué es, qué nos dice con seguridad y una cosa que no nos dice.",
        "Fuente 1, la vasija: es una jarra. Nos dice que se guardaba aceite. No nos dice quién la usaba. Fuente 4, el ágora: es una plaza. Nos dice que se compraba y se vendía. No nos dice cuántas personas iban.",
        ["dos fuentes distintas", "lo que dice con seguridad", "algo que no dice"], ["tres datos por fuente escritos"], ["afirmar más de lo que muestra la fuente", "elegir la misma fuente dos veces"],
        "Pregunta cómo supo lo que escribió. Si dice «me lo imaginé», ayúdale a volver a la fuente."),
    reinforce="Nombra tres tipos de fuente y di para qué sirve cada uno.",
    extend="Imagina que dentro de dos mil años estudian tu casa. Escribe qué objetos serían fuentes y qué dirían.",
)

# ---------------------------------------------------------------- clase 3
G3 = ("Ficha de la polis de Atenas: la palabra democracia viene del griego y significa «poder del pueblo». En Atenas, los ciudadanos se reunían en una asamblea para discutir y votar las decisiones. "
      "Eran ciudadanos los hombres adultos hijos de atenienses. Las mujeres, los esclavos y los extranjeros no eran ciudadanos y no podían votar. "
      "Un esclavo era una persona obligada a trabajar para otra, sin libertad ni pago.")
register(
    OA1, 3,
    materials="Lápiz y papel. La ficha de Atenas está escrita en cada ejercicio.",
    use="Aprenderé qué es la ciudadanía y cómo funcionaba la democracia en Atenas. Sirve para ver que fue un comienzo importante, pero no incluía a todas las personas.",
    prior=["Sé qué es una polis.", "Sé qué es una fuente."],
    explain=[
        "En Atenas nació una forma de gobierno llamada democracia. La palabra viene del griego y significa «poder del pueblo». Los ciudadanos se reunían en una asamblea, hablaban de los problemas de la polis y votaban lo que había que hacer.",
        "Pero no todos eran ciudadanos. Solo lo eran los hombres adultos hijos de atenienses. Las mujeres, los esclavos y los extranjeros no podían votar ni participar en la asamblea. Eso quiere decir que la democracia ateniense dejaba fuera a mucha gente.",
        "Hoy decimos que la democracia debe incluir a todas las personas adultas de un país. Por eso la democracia de Atenas no es igual a la de hoy. Es un legado, es decir, algo que viene del pasado y que ha cambiado con el tiempo.",
    ],
    vocab=[("democracia", "gobierno donde las personas participan en las decisiones, por votación"), ("ciudadano", "persona con derecho a participar en las decisiones de su ciudad"), ("asamblea", "reunión donde se discute y se vota"), ("esclavo", "persona obligada a trabajar para otra, sin libertad"), ("legado", "algo que viene del pasado y llega al presente")],
    worked=[
        {"title": "¿Quién votaba?", "problem": f"{G3} ¿Podía votar un esclavo en Atenas?", "steps": ["Busco quiénes eran ciudadanos.", "Los esclavos no eran ciudadanos, así que no podían votar."], "answer": "No"},
        {"title": "Contar a los excluidos", "problem": f"{G3} En una casa viven 1 hombre adulto ateniense, 1 mujer y 2 esclavos. ¿Cuántas personas no podían votar?", "steps": ["Solo el hombre adulto ateniense era ciudadano.", "La mujer y los 2 esclavos no podían votar.", "1 + 2 = 3."], "answer": "3 personas"},
    ],
    mistakes=[
        {"wrong": "Decir que en Atenas todas las personas votaban.", "why": "Se cree que democracia siempre significó «todos».", "fix": "Recuerda que solo votaban los ciudadanos, que eran hombres adultos hijos de atenienses."},
        {"wrong": "Decir que la democracia de Atenas era igual a la de hoy.", "why": "Se ignoran los cambios.", "fix": "Compara: en Atenas votaban pocos; hoy votan todas las personas adultas con derecho a voto."},
    ],
    tiers={
        "recovery": [
            ex(f"{G3} ¿Qué significa democracia?", "poder del pueblo", "La ficha traduce la palabra del griego."),
            ex(f"{G3} ¿Dónde se reunían los ciudadanos para votar?", "en la asamblea", "La ficha dice que se reunían en una asamblea."),
            ex(f"{G3} ¿Podía una mujer ateniense votar en la asamblea?", "no", "La ficha dice que las mujeres no podían votar."),
        ],
        "understand": [
            ex(f"{G3} ¿Quiénes eran ciudadanos en Atenas?", "los hombres adultos hijos de atenienses", "Así lo dice la ficha."),
            ex(f"{G3} Escribe los tres grupos que no eran ciudadanos.", "mujeres, esclavos y extranjeros", "La ficha los nombra."),
            ex(f"{G3} ¿Qué es un esclavo?", "una persona obligada a trabajar para otra, sin libertad ni pago", "Así lo define la ficha."),
        ],
        "apply": [
            ex("En una calle de Atenas viven 3 hombres adultos hijos de atenienses, 2 mujeres, 2 esclavos y 1 extranjero. ¿Cuántas personas podían votar?", "3", "Solo los 3 hombres adultos hijos de atenienses eran ciudadanos."),
            ex("En esa misma calle viven 3 hombres adultos hijos de atenienses, 2 mujeres, 2 esclavos y 1 extranjero. ¿Cuántas personas NO podían votar?", "5", "2 mujeres + 2 esclavos + 1 extranjero = 5."),
            ex(f"{G3} Pablo es un hombre adulto, hijo de atenienses. ¿Podía ir a la asamblea y votar?", "sí", "Cumplía todos los requisitos de ciudadano."),
        ],
        "reason": [
            ex(f"{G3} Rosa dice: «La democracia de Atenas era como la de hoy». Da una razón de la ficha para decir que no.", "En Atenas no votaban las mujeres, los esclavos ni los extranjeros", "Excluía a muchas personas."),
            ex(f"{G3} Un niño dice: «La democracia de Atenas es muy antigua, así que no tiene nada que ver con hoy». ¿Tiene razón?", "No, es un legado: la idea de votar y decidir entre ciudadanos llega al presente", "Una parte de la idea sigue, aunque cambió."),
        ],
        "challenge": [
            ex(f"{G3} Compara con hoy. En Atenas votaban los hombres adultos hijos de atenienses. Hoy, en Chile, votan las personas adultas con derecho a voto, sean hombres o mujeres. Escribe un cambio.", "Hoy también votan las mujeres", "Las mujeres no votaban en Atenas."),
            ex("Elige la frase que reconoce un aporte y una limitación. A) La democracia ateniense fue perfecta. B) La democracia ateniense permitió votar, pero dejó fuera a muchas personas.", "B", "Nombra el aporte y el límite."),
        ],
    },
    context=[ex("En tu curso quieren decidir el juego del recreo. La profesora dice que solo votarán los niños nacidos en la ciudad. ¿Qué grupo se parecería a los excluidos de Atenas?", "los niños nacidos en otro lugar", "Serían como los extranjeros, que no podían votar.")],
    selfcheck=[
        ex("¿Qué significa «poder del pueblo»?", "democracia", "Es la traducción de la palabra griega."),
        ex("¿Podían votar los extranjeros en Atenas?", "no", "No eran ciudadanos."),
        ex("¿Por qué decimos que la democracia de Atenas dejaba fuera a mucha gente?", "porque solo votaban los hombres adultos hijos de atenienses", "Mujeres, esclavos y extranjeros no podían votar."),
    ],
    open_task=task(
        f"Dibuja una asamblea de Atenas con 6 personas: 3 ciudadanos y 3 personas que no pueden entrar. Rotula quién es quién. {G3}",
        "Dibujo con una plaza. Tres hombres adultos con la mano levantada, rotulados «ciudadano». Afuera, una mujer, un esclavo y un extranjero, rotulados con su grupo y la frase «no puede votar».",
        ["tres ciudadanos", "tres personas excluidas rotuladas", "grupos correctos"], ["dibujo con rótulos"], ["poner a una mujer como ciudadana", "no rotular a los excluidos"],
        "Pregunta qué piensa de que algunos no pudieran votar. Valora que explique por qué hoy se considera injusto."),
    reinforce="Explica a alguien en casa qué es una democracia y quiénes votaban en Atenas.",
    extend="Escribe una regla de tu sala que se decida votando y di quiénes deberían poder votar.",
)

# ---------------------------------------------------------------- clase 4
G4 = ("Ficha de teatro, mitos y juegos: los griegos hacían obras de teatro al aire libre, en teatros construidos en una ladera. Había tragedias, que eran historias serias, y comedias, que hacían reír. "
      "Los actores usaban máscaras y todos eran hombres. Las obras se presentaban en fiestas en honor del dios Dioniso. "
      "Un mito es un relato antiguo sobre dioses y héroes. Zeus era el rey de los dioses, Atenea era la diosa de la sabiduría y protectora de Atenas, y Poseidón era el dios del mar. "
      "Los Juegos Olímpicos se hacían en Olimpia, en honor de Zeus, cada cuatro años. Competían hombres libres griegos en carreras, lucha, lanzamiento de disco y de jabalina.")
register(
    OA1, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo se expresaban y celebraban los griegos con teatro, mitos y juegos. Sirve para reconocer legados que se parecen a cosas de hoy.",
    prior=["Sé qué es una polis.", "Sé que el pasado cambia con el tiempo."],
    explain=[
        "Los griegos creían en muchos dioses. Contaban mitos, que son relatos sobre dioses y héroes. Con los mitos explicaban el mundo y sus costumbres. Zeus era el rey de los dioses, Atenea era la diosa de la sabiduría y Poseidón era el dios del mar. Un mito no es un hecho histórico comprobado.",
        "El teatro nació en Grecia como parte de fiestas para el dios Dioniso. Los teatros eran al aire libre, en una ladera, para que mucha gente viera la obra. Había tragedias y comedias. Los actores usaban máscaras y todos eran hombres. Las palabras teatro, tragedia y comedia vienen del griego.",
        "Los Juegos Olímpicos se hacían en Olimpia, en honor de Zeus, cada cuatro años. Competían hombres libres griegos en carreras, lucha, lanzamiento de disco y de jabalina. Hoy los Juegos Olímpicos también se hacen cada cuatro años, pero participan mujeres y hombres de muchos países.",
    ],
    vocab=[("mito", "relato antiguo sobre dioses y héroes"), ("tragedia", "obra de teatro seria"), ("comedia", "obra de teatro que hace reír"), ("máscara", "cara falsa que se pone sobre el rostro"), ("Juegos Olímpicos", "competencias deportivas que se hacían en Olimpia")],
    worked=[
        {"title": "Identificar un dios", "problem": f"{G4} ¿Qué dios gobernaba el mar?", "steps": ["Busco la palabra mar.", "La ficha dice que Poseidón era el dios del mar."], "answer": "Poseidón"},
        {"title": "Comparar con hoy", "problem": f"{G4} ¿Qué se parece y qué cambió entre los Juegos de Olimpia y los de hoy?", "steps": ["Se parecen en que se hacen cada cuatro años.", "Cambió que hoy también participan mujeres y personas de muchos países."], "answer": "Se parecen en la frecuencia; cambió quiénes participan"},
    ],
    mistakes=[
        {"wrong": "Decir que los mitos griegos son historias reales que sucedieron como se cuentan.", "why": "Se confunde mito con hecho.", "fix": "Un mito es un relato antiguo sobre dioses y héroes; no es una prueba histórica."},
        {"wrong": "Decir que en el teatro griego actuaban mujeres.", "why": "Se piensa en el teatro de hoy.", "fix": "La ficha dice que todos los actores eran hombres."},
    ],
    tiers={
        "recovery": [
            ex(f"{G4} ¿Quién era el rey de los dioses?", "Zeus", "La ficha lo nombra rey de los dioses."),
            ex(f"{G4} ¿Dónde se hacían las obras de teatro: dentro de una casa o al aire libre?", "al aire libre", "Los teatros estaban en una ladera, al aire libre."),
            ex(f"{G4} ¿Cada cuántos años se hacían los Juegos Olímpicos?", "cada cuatro años", "Así lo dice la ficha."),
        ],
        "understand": [
            ex(f"{G4} ¿Qué es un mito?", "un relato antiguo sobre dioses y héroes", "Así lo define la ficha."),
            ex(f"{G4} ¿Cuál era la diferencia entre una tragedia y una comedia?", "la tragedia es seria y la comedia hace reír", "La ficha las describe así."),
            ex(f"{G4} ¿En honor de qué dios se hacían los Juegos Olímpicos?", "de Zeus", "Se hacían en Olimpia, en honor de Zeus."),
        ],
        "apply": [
            ex(f"{G4} Lee: «La diosa Atenea hizo crecer un olivo en la Acrópolis». ¿Esa frase es un mito o un hecho comprobado?", "un mito", "Habla de una diosa, y los mitos cuentan sobre dioses."),
            ex(f"{G4} Une cada dios con lo que representa: A) Atenea; B) Poseidón. 1) el mar; 2) la sabiduría.", "A con 2; B con 1", "Atenea es la sabiduría y Poseidón el mar."),
            ex(f"{G4} Un griego lanza una jabalina en Olimpia. ¿Participa en un teatro o en los Juegos Olímpicos?", "en los Juegos Olímpicos", "El lanzamiento de jabalina era una competencia olímpica."),
        ],
        "reason": [
            ex(f"{G4} Camila dice que en el teatro griego las mujeres eran actrices. Usa la ficha para corregirla.", "Todos los actores eran hombres", "La ficha lo afirma."),
            ex(f"{G4} Sofía dice que los mitos griegos prueban que Zeus existió. ¿Tiene razón?", "No, los mitos son relatos y no pruebas históricas", "Un mito es un relato."),
        ],
        "challenge": [
            ex(f"{G4} Escribe una semejanza y una diferencia entre los Juegos Olímpicos griegos y los de hoy.", "Semejanza: cada cuatro años. Diferencia: hoy participan mujeres y personas de muchos países", "La ficha da el dato griego y esta clase da el de hoy."),
            ex("Elige la frase correcta. A) La palabra teatro viene del griego, y los griegos hacían obras al aire libre. B) La palabra teatro no tiene relación con Grecia.", "A", "El teatro nació en Grecia."),
        ],
    },
    context=[ex("En tu escuela harán una obra con máscaras de colores. ¿Qué costumbre del teatro griego estarían imitando?", "usar máscaras", "Los actores griegos usaban máscaras.")],
    selfcheck=[
        ex("¿Dónde se hacían los Juegos Olímpicos de los griegos?", "en Olimpia", "La ficha lo dice."),
        ex("¿Quién era la diosa de la sabiduría?", "Atenea", "La ficha la nombra así."),
        ex("¿Un mito es un hecho comprobado o un relato antiguo?", "un relato antiguo", "Cuenta sobre dioses y héroes."),
    ],
    open_task=task(
        f"Elige una de estas dos tareas. A) Inventa un mini diálogo de 4 líneas entre Atenea y Poseidón en el que cada uno diga qué protege. B) Dibuja un teatro griego al aire libre con actores con máscaras. {G4} Escribe una línea que diga que los mitos son relatos.",
        "A) Atenea: «Yo protejo la sabiduría». Poseidón: «Yo gobierno el mar». Atenea: «Cuidemos a los griegos». Poseidón: «Cada uno desde su lugar». B) Dibujo con gradas en una ladera, actores con máscaras y la nota «los mitos son relatos».",
        ["usa datos correctos de la ficha", "no presenta el mito como hecho histórico", "una línea sobre el mito"], ["diálogo o dibujo"], ["asignar a Poseidón la sabiduría", "dibujar mujeres actrices en un teatro griego"],
        "Pregunta qué parte del mito es un relato y qué parte es un hecho. Recuerda que sus historias se contaban para explicar el mundo."),
    reinforce="Repite el nombre de tres dioses griegos y lo que representaba cada uno.",
    extend="Escribe dos deportes de hoy que se parezcan a los de Olimpia.",
)

# ---------------------------------------------------------------- clase 5
G5 = ("Legados de Grecia: (1) democracia: decidir entre ciudadanos mediante votación en una asamblea; (2) historia: Heródoto escribió el relato de las guerras entre griegos y persas, y por eso se le llama el «padre de la historia»; "
      "(3) teatro: tragedias y comedias en teatros al aire libre; (4) arte y escultura: estatuas de mármol y de bronce de dioses y de deportistas, con cuerpos que parecen reales; "
      "(5) arquitectura: templos con columnas y un techo triangular al frente, como el Partenón en Atenas, templo de la diosa Atenea; "
      "(6) mitología: relatos sobre dioses y héroes, como Zeus y Atenea; (7) geometría: Euclides, un sabio griego, escribió un famoso libro sobre figuras como el triángulo y el círculo; "
      "(8) filosofía, que significa «amor por la sabiduría»: Sócrates, Platón y Aristóteles hacían preguntas sobre la vida y el mundo; "
      "(9) alfabeto: los griegos tomaron las letras de los fenicios y agregaron letras para las vocales; la palabra «alfabeto» viene de alfa y beta, las dos primeras letras griegas; "
      "(10) Juegos Olímpicos: competencias que se hacían cada cuatro años en Olimpia.")
register(
    OA1, 5,
    materials="Lápiz y papel. La lista de legados está escrita en cada ejercicio.",
    use="Aprenderé qué cosas de hoy vienen de la Grecia antigua y cuáles han cambiado. Sirve para entender que el pasado deja huellas en el presente.",
    prior=["Sé qué es una polis.", "Sé qué es la democracia y qué es un mito."],
    explain=[
        "Un legado es algo que dejaron las personas del pasado y que llega hasta hoy. Los griegos nos dejaron muchos legados. Algunos siguen casi iguales, como las columnas en edificios. Otros han cambiado mucho, como la democracia, que hoy incluye a más personas.",
        "En arte, los escultores griegos hacían estatuas de mármol y de bronce de dioses y de deportistas. Querían mostrar cuerpos que parecieran reales. En arquitectura, construían templos con columnas y un techo triangular al frente, como el Partenón. Hoy muchos museos y edificios públicos imitan esas columnas.",
        "En las ideas, la filosofía es el amor por la sabiduría: preguntar y pensar sobre la vida. Sócrates, Platón y Aristóteles fueron filósofos griegos. La geometría estudia figuras como el triángulo y el círculo, y Euclides escribió un famoso libro sobre ella. Heródoto contó las guerras entre griegos y persas, y por eso lo llaman el «padre de la historia».",
        "La palabra alfabeto viene de alfa y beta, las dos primeras letras griegas. Los griegos tomaron las letras de los fenicios y agregaron letras para las vocales. Por eso los griegos no inventaron todo solos: aprendieron de otros pueblos y otros pueblos aprendieron de ellos. Para reconocer un legado, busca la huella griega en algo de hoy y revisa qué cambió.",
    ],
    vocab=[("legado", "algo del pasado que llega hasta hoy"), ("filosofía", "amor por la sabiduría, pensar y preguntar sobre la vida"), ("geometría", "estudio de las figuras, como el triángulo y el círculo"), ("alfabeto", "conjunto de letras de una lengua"), ("escultura", "obra de arte hecha en piedra, mármol u otro material")],
    worked=[
        {"title": "Reconocer un legado", "problem": f"{G5} ¿Qué legado griego aparece en un edificio moderno que tiene columnas en la entrada?", "steps": ["Busco algo sobre columnas en la lista.", "El punto 5 habla de templos con columnas."], "answer": "La arquitectura"},
        {"title": "Una palabra heredada", "problem": f"{G5} ¿De dónde viene la palabra alfabeto?", "steps": ["Busco alfabeto en la lista.", "Viene de alfa y beta, las dos primeras letras griegas."], "answer": "De alfa y beta"},
    ],
    mistakes=[
        {"wrong": "Decir que todo lo de hoy es igual a lo de Grecia.", "why": "No se revisa el cambio.", "fix": "Di qué se parece y qué cambió, como en la democracia."},
        {"wrong": "Decir que los griegos inventaron todo solos.", "why": "Se olvida que aprendían de otros pueblos.", "fix": "Los griegos aprendieron de otros pueblos y otros aprendieron de ellos."},
    ],
    tiers={
        "recovery": [
            ex(f"{G5} ¿Cómo se llama el templo de Atenea que está en Atenas?", "el Partenón", "El punto 5 lo nombra."),
            ex(f"{G5} ¿Qué significa filosofía?", "amor por la sabiduría", "Así lo dice el punto 8."),
            ex(f"{G5} ¿Qué dos letras griegas dan origen a la palabra alfabeto?", "alfa y beta", "Así lo dice el punto 9."),
        ],
        "understand": [
            ex(f"{G5} ¿Quién escribió sobre las guerras entre griegos y persas?", "Heródoto", "El punto 2 lo indica."),
            ex(f"{G5} ¿Qué sabio griego escribió un famoso libro de geometría?", "Euclides", "El punto 7 lo nombra."),
            ex(f"{G5} Nombra dos filósofos griegos.", "dos de: Sócrates, Platón, Aristóteles", "El punto 8 los nombra."),
        ],
        "apply": [
            ex(f"{G5} Un museo muestra una estatua de bronce de un deportista. ¿Qué legado es?", "arte y escultura", "El punto 4 habla de estatuas de mármol."),
            ex(f"{G5} Una niña lee un libro que cuenta cómo ocurrió una guerra antigua. ¿Qué costumbre griega continúa?", "escribir la historia", "Heródoto escribió relatos de hechos."),
            ex(f"{G5} Une cada ejemplo de hoy con su legado: A) una competencia deportiva cada cuatro años; B) una votación en el curso; C) un museo con columnas en la entrada. 1) democracia; 2) Juegos Olímpicos; 3) arquitectura.", "A con 2; B con 1; C con 3", "Los Juegos, la votación y las columnas vienen de Grecia."),
        ],
        "reason": [
            ex(f"{G5} Un niño dice: «Los griegos inventaron las letras de la nada». ¿Qué respondes?", "Tomaron las letras de los fenicios y agregaron letras para las vocales", "El punto 9 explica de dónde vienen las letras."),
            ex(f"{G5} Daniela dice: «La democracia de hoy es idéntica a la de Atenas». ¿Tiene razón?", "No, hoy votan más personas, incluidas las mujeres", "El legado cambió."),
        ],
        "challenge": [
            ex(f"{G5} Un curso vota para elegir a su delegada, y después presenta una obra con una tragedia y una comedia. ¿Qué dos legados griegos aparecen?", "democracia y teatro", "La votación viene de la democracia y las obras del teatro."),
            ex("Elige la frase que reconoce continuidad y cambio. A) Los Juegos Olímpicos siguen cada cuatro años, pero hoy participan mujeres. B) Los Juegos Olímpicos son exactamente iguales.", "A", "A nombra qué continúa y qué cambió."),
        ],
    },
    context=[ex("Un edificio de gobierno tiene columnas, y adentro se discuten leyes con votaciones. ¿Qué dos legados griegos se pueden reconocer?", "arquitectura y democracia", "Las columnas son arquitectura griega y la votación viene de la democracia.")],
    selfcheck=[
        ex("¿Qué es un legado?", "algo del pasado que llega hasta hoy", "Es una huella del pasado."),
        ex(f"{G5} ¿Qué es la geometría?", "el estudio de las figuras como el triángulo y el círculo", "El punto 7 la describe."),
        ex("¿Los legados siempre son idénticos a lo antiguo?", "no, algunos han cambiado", "La democracia cambió mucho."),
    ],
    open_task=task(
        f"Haz un cartel con cuatro legados griegos. Para cada uno escribe: el legado, un ejemplo de hoy y una cosa que cambió. {G5}",
        "Arquitectura: los edificios con columnas; cambió que hoy se construyen con hormigón y acero. Teatro: las obras del colegio; cambió que actúan mujeres. Democracia: votar en el curso; cambió que votan más personas. Juegos Olímpicos: se hacen cada cuatro años; cambió que participan mujeres.",
        ["cuatro legados distintos", "ejemplo de hoy correcto", "un cambio explicado"], ["cartel escrito"], ["decir que el legado es idéntico", "elegir algo que no es un legado de la lista"],
        "Pregunta cuál le sorprendió más y por qué. Valora que reconozca tanto la huella como el cambio."),
    reinforce="Nombra cinco legados griegos sin mirar la lista.",
    extend="Escribe una palabra de tu vida que venga de la lista de legados y explica su relación con Grecia.",
)

# ================================================================ OA 02 · ROMA
R1 = ("Ficha de Roma: Roma comenzó como una ciudad junto al río Tíber, en la península itálica, en lo que hoy es Italia. Los romanos de la Antigüedad vivieron hace más de 2.000 años. "
      "Con el tiempo conquistaron muchas tierras alrededor del mar Mediterráneo y formaron un imperio, que es un territorio muy grande gobernado desde una ciudad. "
      "Al principio Roma fue una república, un gobierno donde varios cargos eran elegidos. Más tarde la gobernaron emperadores.")
register(
    OA2, 1,
    materials="Lápiz y papel. La ficha de Roma está escrita en cada ejercicio.",
    use="Aprenderé dónde y cuándo vivieron los romanos y cómo crecieron. Sirve para ubicar su historia en el mapa y en el tiempo.",
    prior=["Sé dónde está Grecia y qué es una polis.", "Sé qué es una línea de tiempo."],
    explain=[
        "Roma comenzó como una ciudad junto al río Tíber, en la península itálica. Una península es una tierra rodeada de agua casi por todos lados. Hoy esa zona es parte de Italia. Los romanos vivieron hace más de dos mil años.",
        "Al principio Roma fue una república. En una república, varios cargos importantes eran elegidos y no había un rey. Con el tiempo, Roma conquistó muchas tierras alrededor del mar Mediterráneo. Así se formó un imperio, un territorio muy grande gobernado desde una ciudad. Más tarde, Roma fue gobernada por emperadores.",
        "Conquistar significa tomar el control de un territorio, muchas veces por la fuerza. Eso trajo cambios a muchos pueblos. Algunos adoptaron costumbres romanas, otros perdieron su libertad. Para entender el imperio, hay que mirar su tamaño y también cómo vivían los pueblos que quedaron dentro.",
    ],
    vocab=[("península", "tierra rodeada de agua casi por todos lados"), ("república", "gobierno donde varios cargos son elegidos y no hay rey"), ("imperio", "territorio muy grande gobernado desde una ciudad"), ("emperador", "gobernante de un imperio"), ("conquistar", "tomar el control de un territorio")],
    worked=[
        {"title": "Ubicar Roma", "problem": f"{R1} ¿Junto a qué río comenzó Roma?", "steps": ["Busco la palabra río.", "La ficha dice que comenzó junto al río Tíber."], "answer": "El río Tíber"},
        {"title": "Del cambio de gobierno", "problem": f"{R1} ¿Qué tipo de gobierno tuvo Roma primero?", "steps": ["Busco la palabra primero o al principio.", "Fue una república."], "answer": "Una república"},
    ],
    mistakes=[
        {"wrong": "Decir que Roma siempre fue un imperio.", "why": "Se mezclan las etapas.", "fix": "Primero fue una república y más tarde tuvo emperadores."},
        {"wrong": "Decir que el imperio romano está donde hoy está solo la ciudad de Roma.", "why": "Se confunde la ciudad con el imperio.", "fix": "El imperio abarcó muchas tierras alrededor del Mediterráneo."},
    ],
    tiers={
        "recovery": [
            ex(f"{R1} ¿Qué país actual ocupa la zona donde comenzó Roma?", "Italia", "La ficha dice que hoy es Italia."),
            ex(f"{R1} ¿Qué es una república según la ficha?", "un gobierno donde varios cargos eran elegidos", "Así lo define la ficha."),
            ex(f"{R1} ¿Alrededor de qué mar conquistaron tierras los romanos?", "el mar Mediterráneo", "La ficha lo nombra."),
        ],
        "understand": [
            ex(f"{R1} ¿Qué es un imperio?", "un territorio muy grande gobernado desde una ciudad", "Así lo define la ficha."),
            ex(f"{R1} ¿Los romanos vivieron hace mucho o hace poco?", "hace mucho", "La ficha dice más de 2.000 años."),
            ex(f"{R1} ¿Qué tipo de gobernante tuvo Roma más tarde?", "emperadores", "La ficha dice que más tarde la gobernaron emperadores."),
        ],
        "apply": [
            ex(f"{R1} Ordena las etapas: imperio con emperadores, ciudad junto al Tíber, república.", "ciudad junto al Tíber, república, imperio con emperadores", "Roma creció y cambió de gobierno con el tiempo."),
            ex(f"{R1} Un mapa muestra tierras alrededor del Mediterráneo controladas desde Roma. ¿Es una ciudad, una república o un imperio?", "un imperio", "Un imperio es un territorio muy grande gobernado desde una ciudad."),
            ex(f"{R1} Quieres ubicar Roma en un mapa de Europa. ¿La buscas en la península itálica o en una isla del norte?", "en la península itálica", "Roma comenzó en esa península."),
        ],
        "reason": [
            ex(f"{R1} Lucas dice: «Roma siempre tuvo emperadores». Corrige con la ficha.", "Al principio fue una república", "La ficha dice que los emperadores vinieron más tarde."),
            ex(f"{R1} Marta dice que el imperio romano y la ciudad de Roma son lo mismo. ¿Tiene razón?", "No, el imperio era un territorio muy grande y la ciudad era su centro", "Un imperio es mucho más que la ciudad."),
        ],
        "challenge": [
            ex(f"{R1} Compara Roma con una polis griega: ¿qué diferencia hay en el tamaño de lo que controlaba?", "Roma terminó controlando un territorio enorme y una polis controlaba solo su ciudad y alrededores", "Roma formó un imperio y las polis eran independientes y más pequeñas."),
            ex("Conquistar un territorio, ¿pudo ser bueno para todos los pueblos? Elige. A) Sí, para todos, siempre. B) No siempre: algunos perdieron su libertad.", "B", "La conquista afectó de manera distinta a los pueblos."),
        ],
    },
    context=[ex("Un cartel de museo dice: «Moneda hallada en una ciudad lejana, pero hecha en el imperio romano». ¿Qué dato muestra el tamaño del imperio?", "que una moneda romana llegó a una ciudad lejana", "Muestra que el imperio abarcaba muchos territorios.")],
    selfcheck=[
        ex(f"{R1} ¿Junto a qué río comenzó Roma?", "el río Tíber", "Así lo dice la ficha."),
        ex("¿Qué fue primero en Roma: la república o el imperio?", "la república", "El imperio vino más tarde."),
        ex("¿Qué es una península?", "una tierra rodeada de agua casi por todos lados", "Italia está en una."),
    ],
    open_task=task(
        f"Dibuja una línea de tiempo con tres etapas de Roma y un mapa simple: una ciudad junto a un río, y un círculo grande alrededor que represente el imperio. {R1}",
        "Línea: ciudad junto al Tíber, república, imperio con emperadores. Mapa: punto de Roma junto al río y un círculo grande alrededor del mar Mediterráneo.",
        ["tres etapas en orden", "Roma junto a un río", "imperio mucho más grande que la ciudad"], ["línea de tiempo", "mapa simple"], ["poner el imperio antes de la república", "dibujar el imperio del mismo tamaño que la ciudad"],
        "Pide que cuente con sus palabras cómo creció Roma."),
    reinforce="Repite en voz alta las tres etapas de Roma y qué es un imperio.",
    extend="Escribe dos cosas que cambian en la vida de un pueblo cuando es conquistado.",
)

# ---------------------------------------------------------------- clase 2
R2 = ("Ficha de la vida en Roma: las familias ricas vivían en casas con patio llamadas domus. Muchas familias con menos dinero vivían en edificios de varios pisos llamados insulae. "
      "El foro era la plaza principal, donde se hacían negocios y reuniones. Las termas eran baños públicos donde las personas se bañaban y conversaban. "
      "En el circo había carreras de carros. En el anfiteatro se presentaban combates de gladiadores, hombres que luchaban ante el público; muchos eran esclavizados. Los hombres ciudadanos usaban una toga sobre la túnica; la mayoría de las personas usaba túnica. "
      "Se comía pan, aceitunas, queso y legumbres. Había personas libres y personas esclavizadas, que trabajaban en casas, campos y talleres.")
register(
    OA2, 2,
    materials="Lápiz y papel. La ficha de la vida en Roma está escrita en cada ejercicio.",
    use="Aprenderé cómo vivían distintas personas en Roma. Sirve para entender que no todos vivían igual.",
    prior=["Sé dónde y cuándo vivieron los romanos.", "Sé qué es un esclavo."],
    explain=[
        "En Roma había mucha diferencia entre una familia y otra. Las familias ricas vivían en una domus, una casa con patio. Muchas familias con menos dinero vivían en una insula, un edificio de varios pisos con departamentos pequeños. En la ciudad había mucho ruido y mucha gente.",
        "Los romanos se juntaban en lugares públicos. En el foro se hacían negocios y reuniones. En las termas la gente se bañaba y conversaba. En el circo había carreras de carros. En el anfiteatro se presentaban combates de gladiadores, hombres que luchaban ante el público; muchos eran esclavizados. La mayoría de las personas vestía una túnica. Los ciudadanos hombres usaban sobre ella una toga.",
        "En Roma había personas libres y personas esclavizadas. Los esclavizados trabajaban en casas, campos y talleres sin libertad. Por eso, cuando alguien dice «los romanos hacían esto», conviene preguntar: ¿qué romanos? Una familia rica, una familia pobre y una persona esclavizada vivían de modos muy distintos.",
    ],
    vocab=[("domus", "casa romana con patio, de una familia con más dinero"), ("insula", "edificio de varios pisos donde vivían muchas familias"), ("foro", "plaza principal de Roma"), ("termas", "baños públicos de los romanos"), ("toga", "prenda que usaban sobre la túnica los ciudadanos hombres")],
    worked=[
        {"title": "Comparar viviendas", "problem": f"{R2} ¿En qué se diferencian una domus y una insula?", "steps": ["Busco domus: casa con patio de familias ricas.", "Busco insula: edificio de varios pisos de familias con menos dinero."], "answer": "Una domus es una casa con patio y una insula es un edificio de varios pisos"},
        {"title": "Un lugar público", "problem": f"{R2} ¿Dónde se bañaba y conversaba la gente?", "steps": ["Busco la palabra bañaba.", "Las termas eran baños públicos."], "answer": "En las termas"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los romanos vivían en casas con patio.", "why": "Se generaliza la vida de las familias ricas.", "fix": "Muchas familias vivían en insulae."},
        {"wrong": "Decir que todos los romanos eran libres.", "why": "No se considera la esclavitud.", "fix": "Había personas esclavizadas que trabajaban sin libertad."},
    ],
    tiers={
        "recovery": [
            ex(f"{R2} ¿Cómo se llamaba la plaza principal de Roma?", "el foro", "La ficha la llama foro."),
            ex(f"{R2} ¿Qué prenda usaba la mayoría de las personas?", "una túnica", "La ficha lo dice."),
            ex(f"{R2} ¿Cómo se llamaban los baños públicos?", "termas", "Así los nombra la ficha."),
        ],
        "understand": [
            ex(f"{R2} ¿Qué es una insula?", "un edificio de varios pisos donde vivían varias familias", "Así lo define la ficha."),
            ex(f"{R2} Nombra dos alimentos que se comían en Roma.", "dos de: pan, aceitunas, queso, legumbres", "La ficha los menciona."),
            ex(f"{R2} ¿Qué espectáculo se presentaba en el circo?", "carreras de carros", "La ficha lo menciona."),
        ],
        "apply": [
            ex(f"{R2} Una familia con poco dinero vivía en un departamento pequeño de un edificio de cuatro pisos. ¿Era una domus o una insula?", "una insula", "Era un edificio de varios pisos."),
            ex(f"{R2} Un comerciante va a hacer un negocio importante. ¿A qué lugar va: al foro o a las termas?", "al foro", "En el foro se hacían negocios."),
            ex(f"{R2} Un ciudadano hombre va a una reunión. ¿Qué usa sobre la túnica?", "una toga", "La toga era propia de ciudadanos hombres."),
        ],
        "reason": [
            ex(f"{R2} Andrés dice: «Todos los romanos vivían en domus». Corrige con la ficha.", "Muchas familias vivían en insulae", "La domus era solo para familias con más dinero."),
            ex(f"{R2} Un niño dice que todos los romanos vestían toga. ¿Es correcto?", "No, la mayoría vestía solo túnica", "La toga era de ciudadanos hombres."),
        ],
        "challenge": [
            ex(f"{R2} Escribe dos diferencias entre la vida de una familia rica y la de una persona esclavizada en Roma.", "La familia rica tenía libertad y casa propia; la persona esclavizada trabajaba sin libertad", "Había grandes diferencias sociales."),
            ex("Elige la frase más exacta. A) Los romanos vivían todos igual. B) La vida en Roma dependía de si eras rico, pobre o esclavizado.", "B", "B reconoce la diversidad social."),
        ],
    },
    context=[ex("Un visitante de hoy camina por las ruinas de Roma y ve el foro. ¿Qué actividades podía haber en ese lugar hace más de 2.000 años?", "negocios y reuniones", "La ficha dice que el foro servía para eso.")],
    selfcheck=[
        ex("¿Cómo se llamaba la casa con patio de familias ricas?", "domus", "Así se llamaba."),
        ex("¿Dónde se bañaban los romanos en público?", "en las termas", "Eran baños públicos."),
        ex("¿Todos los habitantes de Roma eran libres?", "no, había personas esclavizadas", "La ficha lo indica."),
    ],
    open_task=task(
        f"Escribe un cuento de 4 líneas sobre un día en Roma desde la mirada de una persona: elige una de estas tres. a) una niña de una familia rica; b) un niño de una insula; c) una persona esclavizada. {R2}",
        "Mira desde b): «Me llamo Marco y vivo en una insula. Subo cuatro pisos. Voy al foro con mi padre. Allí conversan de negocios.»",
        ["usa datos de la ficha", "la vida coincide con la persona elegida", "no generaliza a todos los romanos"], ["texto de cuatro líneas"], ["poner a una persona esclavizada en una domus como dueña", "decir que todos vivían igual"],
        "Pregunta qué cambiaría si fuera otra persona. Así comprende la diversidad."),
    reinforce="Nombra tres lugares públicos de Roma y para qué servían.",
    extend="Compara en una frase una insula con un edificio de departamentos de hoy.",
)

# ---------------------------------------------------------------- clase 3
R3 = ("Ficha de derecho en Roma: los romanos escribieron sus leyes en tablas, llamadas las Doce Tablas, para que las conocieran todos. El derecho es el conjunto de leyes y reglas de una sociedad. "
      "Un ciudadano romano tenía derechos, como ser protegido por la ley. Los hombres ciudadanos podían votar. Las mujeres no votaban y los esclavizados no eran ciudadanos. "
      "Con el tiempo, más personas libres de las tierras del imperio pudieron ser ciudadanas. Muchas ideas de las leyes actuales vienen del derecho romano.")
register(
    OA2, 3,
    materials="Lápiz y papel. La ficha de derecho está escrita en cada ejercicio.",
    use="Aprenderé qué eran las leyes romanas y quiénes eran ciudadanos. Sirve para entender un legado importante y también sus límites.",
    prior=["Sé qué es un ciudadano.", "Sé qué es un legado."],
    explain=[
        "El derecho es el conjunto de leyes y reglas de una sociedad. Los romanos escribieron sus leyes en tablas, las Doce Tablas, para que todos pudieran conocerlas. Cuando las leyes están escritas, es más difícil que alguien las cambie a su gusto.",
        "Un ciudadano romano tenía derechos, como ser protegido por la ley. Los hombres ciudadanos podían votar. Pero las mujeres no votaban y los esclavizados no eran ciudadanos. Con el tiempo, más personas libres de las tierras del imperio pudieron ser ciudadanas.",
        "Hoy muchas ideas de las leyes vienen del derecho romano, y varios países, entre ellos algunos de América Latina, tienen leyes con raíces romanas. Pero también hubo exclusiones. Un legado importante puede tener límites, y es bueno reconocerlos.",
    ],
    vocab=[("derecho", "conjunto de leyes y reglas de una sociedad"), ("ley", "regla que deben cumplir las personas de una sociedad"), ("ciudadano", "persona con derechos en su ciudad o imperio"), ("Doce Tablas", "leyes romanas escritas en tablas para que todos las conocieran"), ("exclusión", "dejar a alguien fuera de un derecho")],
    worked=[
        {"title": "Para qué se escribían las leyes", "problem": f"{R3} ¿Por qué los romanos escribieron las leyes en tablas?", "steps": ["Busco la razón en la ficha.", "Dice: para que todos las conocieran."], "answer": "Para que todos las conocieran"},
        {"title": "Quiénes votaban", "problem": f"{R3} ¿Podía votar una mujer romana?", "steps": ["Busco quiénes votaban.", "Solo los hombres ciudadanos votaban, y las mujeres no."], "answer": "No"},
    ],
    mistakes=[
        {"wrong": "Decir que en Roma todos tenían los mismos derechos.", "why": "Se ignoran las exclusiones.", "fix": "Los esclavizados no eran ciudadanos y las mujeres no votaban."},
        {"wrong": "Decir que las leyes romanas ya no sirven para nada.", "why": "Se olvida el legado.", "fix": "Muchas ideas de las leyes actuales vienen del derecho romano."},
    ],
    tiers={
        "recovery": [
            ex(f"{R3} ¿Cómo se llamaban las leyes escritas en tablas?", "las Doce Tablas", "La ficha las nombra."),
            ex(f"{R3} ¿Qué es el derecho?", "el conjunto de leyes y reglas de una sociedad", "Así lo define la ficha."),
            ex(f"{R3} ¿Un esclavizado era ciudadano?", "no", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{R3} Nombra un derecho de un ciudadano romano.", "ser protegido por la ley, o votar si era hombre", "La ficha nombra ambos."),
            ex(f"{R3} ¿Por qué es útil que las leyes estén escritas?", "porque todos pueden conocerlas", "Eso dice la ficha."),
            ex(f"{R3} ¿Cambió con el tiempo quiénes podían ser ciudadanos?", "sí, más personas libres pudieron serlo", "La ficha lo indica."),
        ],
        "apply": [
            ex(f"{R3} Un hombre ciudadano romano quiere votar. ¿Podía?", "sí", "Los hombres ciudadanos podían votar."),
            ex(f"{R3} Una mujer romana quiere votar. ¿Podía?", "no", "La ficha dice que las mujeres no votaban."),
            ex(f"{R3} Un esclavizado quiere ser protegido por la ley como un ciudadano. ¿Tenía ese derecho?", "no", "No era ciudadano."),
        ],
        "reason": [
            ex(f"{R3} Julia dice: «Las leyes romanas eran justas para todos». Usa la ficha para responderle.", "No, dejaban fuera a las mujeres para votar y a los esclavizados", "Hubo exclusiones de varios grupos."),
            ex(f"{R3} Tomás dice: «Las leyes escritas ayudan a que haya más justicia». Da una razón.", "Porque todos las conocen y no se pueden cambiar a gusto", "Las leyes públicas protegen a las personas."),
        ],
        "challenge": [
            ex(f"{R3} Compara las Doce Tablas con las reglas de tu sala. Elige. A) Las reglas escritas y a la vista ayudan a que todos las conozcan. B) Las reglas secretas son mejores.", "A", "Eso ocurre con las leyes escritas."),
            ex(f"{R3} Escribe un legado y un límite del derecho romano.", "Legado: leyes escritas. Límite: dejaba fuera a mujeres y esclavizados de ciertos derechos", "La ficha da ambos."),
        ],
    },
    context=[ex("En tu escuela escriben las reglas de convivencia en un cartel para que todos las lean. ¿Qué idea romana se parece?", "escribir las leyes para que todos las conozcan", "Las Doce Tablas se escribieron con ese fin.")],
    selfcheck=[
        ex("¿Qué son las Doce Tablas?", "las leyes romanas escritas en tablas", "Se escribieron para que todos las conocieran."),
        ex("¿Podían votar las mujeres romanas?", "no", "Las mujeres no votaban."),
        ex("¿Qué es una exclusión?", "dejar a alguien fuera de un derecho", "Hubo exclusiones en Roma."),
    ],
    open_task=task(
        f"Escribe tres reglas escritas para tu sala, como las Doce Tablas pero en pequeño. Debajo, escribe quiénes deberían poder opinar para hacerlas. {R3}",
        "1) Levantar la mano para hablar. 2) Cuidar los materiales. 3) Escuchar a quien habla. Deberían opinar todos los niños y la profesora.",
        ["tres reglas claras", "reglas escritas y visibles", "incluye a todos para opinar"], ["lista escrita"], ["reglas contradictorias", "dejar fuera a algún grupo sin razón"],
        "Pregunta quién debería poder opinar. Compara con quiénes votaban en Roma."),
    reinforce="Explica con tus palabras qué es el derecho y por qué conviene escribir las leyes.",
    extend="Escribe una regla actual y cómo evitarías que dejara fuera a alguien.",
)

# ---------------------------------------------------------------- clase 4
R4 = ("Ficha de legados de Roma: (1) idioma: el latín, la lengua de los romanos, dio origen al español, el italiano, el francés y el portugués. Por ejemplo, aqua dio «agua», amicus dio «amigo», terra dio «tierra», pater dio «padre» y mater dio «madre». "
      "(2) ingeniería: los romanos construyeron caminos de piedra, llamados calzadas, y acueductos, que son canales que llevan agua desde lugares altos hasta las ciudades; algunos tramos son puentes con arcos para cruzar valles, y el agua baja por una pendiente suave. "
      "(3) arquitectura: usaron el arco, la bóveda y el hormigón. Construyeron el Coliseo, un gran anfiteatro en Roma, y el Panteón, un templo con una gran cúpula. "
      "(4) derecho: leyes escritas. "
      "(5) arte: mosaicos, que son dibujos armados con piedritas de colores; pinturas en las paredes de las casas; y bustos, que son retratos de piedra de una persona. "
      "En la ciudad de Pompeya se conservan mosaicos y pinturas porque el volcán Vesubio la cubrió de ceniza hace casi dos mil años.")
register(
    OA2, 4,
    materials="Lápiz y papel. La ficha de legados está escrita en cada ejercicio.",
    use="Aprenderé qué construyeron los romanos y qué palabras de hoy vienen del latín. Sirve para reconocer huellas romanas a tu alrededor.",
    prior=["Sé qué es un legado.", "Sé dónde estaba Roma."],
    explain=[
        "El idioma de los romanos era el latín. Con el tiempo, el latín dio origen al español, al italiano, al francés y al portugués. Por eso muchas palabras se parecen: aqua dio «agua», amicus dio «amigo», terra dio «tierra».",
        "Los romanos fueron grandes constructores. Hicieron calzadas, que son caminos de piedra que unían ciudades. Hicieron acueductos, canales que llevan agua desde lugares altos hasta las ciudades. Algunos tramos eran puentes con arcos para cruzar valles. El agua baja por una pendiente suave, y no hacen falta bombas.",
        "En arquitectura usaron el arco, la bóveda y el hormigón. Construyeron el Coliseo y el Panteón. Estas obras aún se pueden visitar. Eso es un legado: algo del pasado que sigue con nosotros, aunque haya cambiado.",
        "Los romanos también hicieron arte. Un mosaico es un dibujo armado con piedritas de colores, como los que había en los pisos. También pintaron las paredes de sus casas y hicieron bustos, que son retratos de piedra de una persona. Mucho de ese arte se conserva en Pompeya, una ciudad que el volcán Vesubio cubrió de ceniza hace casi dos mil años.",
    ],
    vocab=[("latín", "idioma de los romanos"), ("acueducto", "canal, a veces sobre arcos, que lleva agua a una ciudad"), ("calzada", "camino de piedra romano"), ("arco", "forma curva que sostiene un puente o un muro"), ("Coliseo", "gran anfiteatro de Roma"), ("mosaico", "dibujo armado con piedritas de colores"), ("busto", "retrato de piedra de una persona")],
    worked=[
        {"title": "De una palabra latina a una de hoy", "problem": f"{R4} ¿Qué palabra de hoy viene de la palabra latina aqua?", "steps": ["Busco aqua en la ficha.", "Dio la palabra agua."], "answer": "Agua"},
        {"title": "Qué hacía un acueducto", "problem": f"{R4} ¿Para qué servía un acueducto?", "steps": ["Leo la definición.", "Llevaba agua desde lugares altos hasta las ciudades."], "answer": "Para llevar agua a las ciudades"},
    ],
    mistakes=[
        {"wrong": "Decir que el latín es lo mismo que el español.", "why": "Se confunde origen y resultado.", "fix": "El latín dio origen al español, pero son idiomas distintos."},
        {"wrong": "Decir que los romanos construían acueductos para pasar personas.", "why": "Se confunde con un puente común.", "fix": "Un acueducto lleva agua por un canal."},
    ],
    tiers={
        "recovery": [
            ex(f"{R4} ¿Cómo se llamaba el idioma de los romanos?", "latín", "La ficha lo dice."),
            ex(f"{R4} ¿Qué es una calzada?", "un camino de piedra romano", "Así lo describe la ficha."),
            ex(f"{R4} ¿Qué palabra de hoy viene de terra?", "tierra", "Así lo dice la ficha."),
        ],
        "understand": [
            ex(f"{R4} Nombra tres idiomas que nacieron del latín.", "tres de: español, italiano, francés, portugués", "La ficha los menciona."),
            ex(f"{R4} ¿Qué formas usaron los romanos en su arquitectura?", "el arco, la bóveda y el hormigón", "La ficha las menciona."),
            ex(f"{R4} ¿Qué hacía un acueducto con el agua?", "la llevaba desde lugares altos hasta las ciudades", "Así lo dice la ficha."),
        ],
        "apply": [
            ex(f"{R4} La palabra latina pater dio una palabra que usas en casa. ¿Cuál es?", "padre", "Así lo dice la ficha."),
            ex(f"{R4} Un canal de piedra, en parte sobre arcos, lleva agua a una ciudad. ¿Qué obra romana es?", "un acueducto", "Los acueductos llevaban agua a las ciudades."),
            ex(f"{R4} Un piso de una casa romana tiene una imagen armada con piedritas de colores. ¿Qué obra de arte es?", "un mosaico", "Los mosaicos se arman con piedritas de colores."),
        ],
        "reason": [
            ex(f"{R4} Ema dice que el agua del acueducto subía con bombas eléctricas. Corrígela con la ficha.", "El agua bajaba por una pendiente suave, sin bombas", "La ficha explica cómo bajaba el agua."),
            ex(f"{R4} Pablo dice: «El latín se murió y no dejó nada». ¿Qué le respondes?", "Dio origen a idiomas como el español", "El latín es origen de varios idiomas."),
        ],
        "challenge": [
            ex(f"{R4} Une cada obra con su descripción: A) Coliseo; B) Panteón. 1) templo con gran cúpula; 2) gran anfiteatro.", "A con 2; B con 1", "El Coliseo es un anfiteatro y el Panteón un templo con cúpula."),
            ex(f"{R4} Une cada obra de arte romana con su descripción: A) mosaico; B) busto. 1) retrato de piedra de una persona; 2) dibujo armado con piedritas de colores.", "A con 2; B con 1", "El mosaico se arma con piedritas y el busto es un retrato de piedra."),
        ],
    },
    context=[ex("Un turista ve una calle de piedra muy antigua que une dos pueblos. ¿Qué obra romana podría ser, según la ficha?", "una calzada", "Las calzadas unían ciudades.")],
    selfcheck=[
        ex("¿De qué idioma viene el español?", "del latín", "El latín dio origen a muchos idiomas."),
        ex(f"{R4} ¿Qué es el Coliseo?", "un gran anfiteatro en Roma", "Así lo dice la ficha."),
        ex("¿Qué llevaba un acueducto?", "agua", "Llevaba agua a las ciudades."),
    ],
    open_task=task(
        f"Haz una tabla con dos columnas: «Palabra latina» y «Palabra de hoy». Escribe las cinco de la ficha y agrega una idea para decir qué obra romana te gustaría visitar y por qué, o qué dibujo de mosaico harías. {R4}",
        "aqua - agua; amicus - amigo; terra - tierra; pater - padre; mater - madre. Me gustaría visitar el Coliseo porque es muy grande.",
        ["cinco pares correctos", "una obra y una razón"], ["tabla escrita"], ["unir mal una palabra", "no dar razón"],
        "Pregunta qué palabra cree que cambió más. Así nota cómo cambian los idiomas."),
    reinforce="Nombra tres legados de Roma sin mirar la ficha.",
    extend="Escribe dos palabras más de tu idioma que se parezcan a otro idioma romance, por ejemplo el italiano.",
)

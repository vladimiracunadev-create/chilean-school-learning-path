"""Material del estudiante de 3.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (referencias del planeta), OA 08 (zonas climáticas y formas de habitar) y OA 09 (entorno geográfico de Grecia y Roma)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA7 = "HI03 OA 07"
OA8 = "HI03 OA 08"
OA9 = "HI03 OA 09"

# ================================================================ OA 07 · REFERENCIAS DEL PLANETA
# ---------------------------------------------------------------- clase 1
H1 = ("Ficha de globo y mapa. Un globo terráqueo es una esfera que representa la Tierra con su forma casi redonda. Un mapa es un dibujo plano de la Tierra o de una parte de ella. "
      "El globo muestra todos los continentes y océanos juntos, sin cortes. Para dibujar la Tierra en un papel plano hay que estirar o cortar, y por eso en un mapa algunas zonas se ven más grandes o con otra forma. "
      "El mapa se puede doblar, llevar en la mochila y mostrar detalles de un lugar, como las calles de una ciudad. El globo no se puede doblar.")
register(
    OA7, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Si tienes un globo terráqueo y un mapa mundial en casa o en la escuela, puedes mirarlos, pero no es necesario.",
    use="Aprenderé en qué se parecen y en qué se diferencian un globo terráqueo y un mapa. Sirve para elegir cuál usar y entender sus límites.",
    prior=["Sé que la Tierra es el planeta donde vivimos.", "Sé que un mapa muestra lugares."],
    explain=[
        "Un globo terráqueo es una esfera, una forma como una pelota, que representa la Tierra. La Tierra es casi redonda, así que el globo muestra bien su forma. En un globo se ven todos los continentes y océanos juntos y sin cortes.",
        "Un mapa es un dibujo plano de la Tierra o de una parte de ella. Es más fácil de llevar, se puede doblar y puede mostrar detalles, como las calles de una ciudad. Pero la Tierra es redonda y el papel es plano. Para pasar de uno al otro hay que estirar o cortar, y por eso algunas zonas se ven más grandes o con otra forma en el mapa.",
        "Entonces cada uno sirve para algo distinto. El globo sirve para ver el planeta completo y su forma. El mapa sirve para ver detalles y para llevar. Ninguno es mejor siempre: depende de lo que necesites.",
    ],
    vocab=[("globo terráqueo", "esfera que representa la Tierra"), ("mapa", "dibujo plano de la Tierra o de una parte de ella"), ("esfera", "figura redonda como una pelota"), ("representar", "mostrar algo con un dibujo o un objeto"), ("planeta", "cuerpo grande que gira alrededor de una estrella, como la Tierra")],
    worked=[
        {"title": "Elegir qué usar", "problem": f"{H1} Quieres ver todos los continentes juntos y sin cortes. ¿Qué usas?", "steps": ["Busco quién muestra todo sin cortes.", "La ficha dice que lo hace el globo."], "answer": "El globo terráqueo"},
        {"title": "Entender una deformación", "problem": f"{H1} ¿Por qué algunas zonas se ven más grandes en un mapa?", "steps": ["La Tierra es redonda y el papel es plano.", "Hay que estirar o cortar para dibujarla."], "answer": "Porque al pasar la Tierra a un papel plano hay que estirar o cortar"},
    ],
    mistakes=[
        {"wrong": "Decir que si una zona se ve más grande en un mapa, siempre es más grande en la realidad.", "why": "No se recuerda que el mapa estira zonas.", "fix": "Piensa que el mapa puede cambiar tamaños y formas al pasar a un papel plano."},
        {"wrong": "Decir que el globo sirve para todo mejor que el mapa.", "why": "Se olvidan los detalles y la facilidad de llevarlo.", "fix": "Elige según lo que necesitas."},
    ],
    tiers={
        "recovery": [
            ex(f"{H1} ¿Qué forma tiene un globo terráqueo?", "de esfera", "La ficha dice que es una esfera."),
            ex(f"{H1} ¿Cuál se puede doblar: el globo o el mapa?", "el mapa", "El globo no se puede doblar."),
            ex(f"{H1} ¿Qué representa un globo terráqueo?", "la Tierra", "Así lo dice la ficha."),
        ],
        "understand": [
            ex(f"{H1} ¿Qué ventaja tiene el globo para mostrar los continentes?", "los muestra juntos y sin cortes", "Así lo dice la ficha."),
            ex(f"{H1} ¿Qué ventaja tiene el mapa?", "se puede llevar y mostrar detalles", "Así lo dice la ficha."),
            ex(f"{H1} ¿Por qué la forma de un continente puede verse distinta en un mapa?", "porque hay que estirar o cortar la Tierra para dibujarla plana", "El papel es plano."),
        ],
        "apply": [
            ex(f"{H1} Necesitas ver las calles de una ciudad. ¿Qué usas: globo o mapa?", "un mapa", "El mapa muestra detalles."),
            ex(f"{H1} Quieres saber qué forma tiene la Tierra. ¿Qué usas: globo o mapa?", "un globo", "Muestra la forma casi redonda."),
            ex(f"{H1} Vas de viaje y quieres llevar algo liviano. ¿Qué eliges?", "un mapa", "Se dobla y cabe en la mochila."),
        ],
        "reason": [
            ex(f"{H1} Pedro dice: «En el mapa una zona se ve enorme, entonces es enorme en la realidad». ¿Qué le respondes?", "El mapa puede estirar zonas y cambiar el tamaño", "Al pasar a un papel plano hay estiramientos."),
            ex(f"{H1} Ana dice que el mapa es mejor que el globo en todo. ¿Es correcto?", "No, depende de lo que se necesite", "El globo muestra mejor la forma de la Tierra."),
        ],
        "challenge": [
            ex(f"{H1} Escribe una semejanza y una diferencia entre un globo y un mapa.", "Semejanza: los dos representan la Tierra. Diferencia: el globo es una esfera y el mapa es plano", "La ficha da ambas."),
            ex("Elige la frase correcta. A) Un mapa mundial es una esfera. B) Un mapa mundial es un dibujo plano.", "B", "El mapa es plano."),
        ],
    },
    context=[ex("Un viajero quiere un objeto para mostrar a su curso todos los océanos y continentes sin cortes. ¿Qué le recomiendas?", "un globo terráqueo", "El globo los muestra juntos y sin cortes.")],
    selfcheck=[
        ex("¿Qué es un mapa?", "un dibujo plano de la Tierra o de una parte de ella", "Es plano, no una esfera."),
        ex("¿Qué es un globo terráqueo?", "una esfera que representa la Tierra", "Tiene la forma casi redonda de la Tierra."),
        ex("¿Qué tienen en común el globo y el mapa?", "los dos representan la Tierra", "Sirven para ver lugares."),
    ],
    open_task=task(
        f"Haz un cuadro con dos columnas, «Globo» y «Mapa». Escribe tres cosas de cada uno: su forma, una ventaja y un límite. {H1}",
        "Globo: esfera; muestra todo sin cortes; no se puede doblar. Mapa: plano; se puede llevar y mostrar detalles; puede cambiar la forma de las zonas.",
        ["tres datos por columna", "forma, ventaja y límite", "datos correctos"], ["cuadro completo"], ["decir que el globo es plano", "no escribir límites"],
        "Pregunta cuándo usaría cada uno."),
    reinforce="Explica a una persona de tu casa la diferencia entre un globo y un mapa.",
    extend="Dibuja una pelota y una hoja y escribe cuál de las dos se parece a un globo y cuál a un mapa.",
)

# ---------------------------------------------------------------- clase 2
H2 = ("Ficha del Ecuador y los hemisferios. El Ecuador es una línea imaginaria, que no está dibujada en el suelo, que da la vuelta a la Tierra por la mitad, a igual distancia de los dos polos. "
      "Divide a la Tierra en dos mitades llamadas hemisferios: el hemisferio norte, al norte del Ecuador, y el hemisferio sur, al sur. "
      "Otra línea imaginaria, el meridiano de Greenwich, va de un polo al otro y divide a la Tierra en hemisferio occidental, al oeste, y hemisferio oriental, al este. "
      "Chile está en el hemisferio sur y en el occidental. Grecia e Italia están en el hemisferio norte y en el oriental. El Ecuador pasa por el país llamado Ecuador, en América del Sur. "
      "El meridiano de Greenwich se llama así porque pasa por Greenwich, un barrio de Londres, en Inglaterra. "
      "En los mapas el norte se dibuja arriba por costumbre; si das vuelta el papel, el Polo Norte sigue en el mismo lugar de la Tierra.")
register(
    OA7, 2,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé qué es el Ecuador y cómo divide la Tierra en hemisferios. Sirve para ubicar países y lugares en el planeta.",
    prior=["Sé qué es un globo y un mapa.", "Sé los puntos cardinales."],
    explain=[
        "El Ecuador es una línea imaginaria que da la vuelta a la Tierra por la mitad. No está dibujada en el suelo ni en el mar: se imagina para poder ubicar lugares. Está a igual distancia del Polo Norte y del Polo Sur. En los mapas el norte se dibuja arriba por costumbre. Si das vuelta el papel, el Polo Norte sigue en el mismo lugar de la Tierra.",
        "La palabra hemisferio significa «mitad de una esfera». El Ecuador divide la Tierra en el hemisferio norte y el hemisferio sur. Los lugares al norte del Ecuador están en el hemisferio norte, como Grecia e Italia. Los lugares al sur, como Chile, están en el hemisferio sur.",
        "Otra línea imaginaria, el meridiano de Greenwich, va de un polo a otro y pasa por Greenwich, un barrio de Londres, en Inglaterra. Divide la Tierra en hemisferio oriental y hemisferio occidental. Chile está en el occidental. Grecia e Italia están en el oriental. Así, un lugar puede estar en dos hemisferios a la vez, uno de cada pareja.",
    ],
    vocab=[("Ecuador", "línea imaginaria que da la vuelta a la Tierra por la mitad"), ("hemisferio", "mitad de la Tierra"), ("imaginaria", "que no existe dibujada en el suelo, pero se usa para ubicar"), ("polo", "extremo norte o sur de la Tierra"), ("meridiano de Greenwich", "línea imaginaria que va de polo a polo")],
    worked=[
        {"title": "Hemisferio norte o sur", "problem": f"{H2} ¿En qué hemisferio, norte o sur, está Chile?", "steps": ["Busco Chile en la ficha.", "La ficha lo ubica al sur del Ecuador."], "answer": "En el hemisferio sur"},
        {"title": "Dos hemisferios a la vez", "problem": f"{H2} ¿En qué dos hemisferios está Grecia?", "steps": ["Norte o sur: está en el norte.", "Oriental u occidental: está en el oriental."], "answer": "En el hemisferio norte y en el oriental"},
    ],
    mistakes=[
        {"wrong": "Creer que el Ecuador es una línea pintada que se puede ver.", "why": "Se confunde con la línea del mapa.", "fix": "Es imaginaria: se dibuja en mapas, pero no existe en el suelo."},
        {"wrong": "Decir que Chile está en el hemisferio norte.", "why": "Se piensa que arriba del mapa es norte para todo.", "fix": "Chile está al sur del Ecuador."},
    ],
    tiers={
        "recovery": [
            ex(f"{H2} ¿Qué es el Ecuador?", "una línea imaginaria que da la vuelta a la Tierra por la mitad", "Así lo define la ficha."),
            ex(f"{H2} ¿En qué hemisferio, norte o sur, está Chile?", "en el sur", "La ficha lo dice."),
            ex(f"{H2} ¿En qué hemisferio, norte o sur, está Grecia?", "en el norte", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{H2} ¿Qué dos hemisferios forma el Ecuador?", "el norte y el sur", "Los divide al norte y al sur."),
            ex(f"{H2} ¿Qué significa hemisferio?", "mitad de la Tierra", "Es una mitad de una esfera."),
            ex(f"{H2} ¿Qué línea divide a la Tierra en hemisferio oriental y occidental?", "el meridiano de Greenwich", "Va de polo a polo."),
        ],
        "apply": [
            ex(f"{H2} Pedro da vuelta a un mapa y el norte queda abajo. ¿El Polo Norte cambió de lugar en la Tierra?", "no", "Solo se dio vuelta el papel; el Polo Norte sigue en el mismo lugar."),
            ex(f"{H2} ¿Por qué ciudad de Inglaterra pasa el meridiano de Greenwich?", "por Greenwich, un barrio de Londres", "La ficha lo dice."),
            ex(f"{H2} ¿En qué hemisferio, oriental u occidental, está Italia?", "en el oriental", "La ficha lo dice."),
        ],
        "reason": [
            ex(f"{H2} Tomás dice que el Ecuador es una línea pintada en el mar. ¿Qué le respondes?", "Es una línea imaginaria", "No existe dibujada en el suelo ni en el mar."),
            ex(f"{H2} Pedro dice que Chile y Grecia están en el mismo hemisferio norte-sur. ¿Tiene razón?", "No, Chile está en el sur y Grecia en el norte", "Están en hemisferios opuestos."),
        ],
        "challenge": [
            ex(f"{H2} Chile y Grecia, ¿están en el mismo hemisferio oriental u occidental?", "no, Chile está en el occidental y Grecia en el oriental", "La ficha da los dos datos."),
            ex(f"{H2} Une cada lugar con sus dos hemisferios: A) Chile; B) Italia. 1) norte y oriental; 2) sur y occidental.", "A con 2; B con 1", "Chile es sur y occidental e Italia, norte y oriental."),
        ],
    },
    context=[ex("Un país se llama Ecuador porque la línea del Ecuador pasa por él. ¿En qué continente está, según la ficha?", "en América del Sur", "La ficha lo ubica ahí.")],
    selfcheck=[
        ex("¿Qué divide el Ecuador?", "la Tierra en hemisferio norte y sur", "Está en la mitad."),
        ex("¿En qué hemisferio, norte o sur, vives en Chile?", "en el sur", "Chile está al sur del Ecuador."),
        ex("¿El Ecuador es una línea imaginaria o real?", "imaginaria", "No existe en el suelo."),
    ],
    open_task=task(
        f"Dibuja un círculo que sea la Tierra. Traza el Ecuador de lado a lado y rotula «hemisferio norte» y «hemisferio sur». Ubica con un punto Chile, Grecia e Italia. {H2}",
        "Círculo con una línea en el medio. Arriba: hemisferio norte, con puntos de Grecia e Italia. Abajo: hemisferio sur, con un punto de Chile.",
        ["Ecuador en el medio", "dos hemisferios rotulados", "tres puntos bien ubicados"], ["dibujo rotulado"], ["poner a Chile en el norte", "dibujar el Ecuador vertical"],
        "Pregunta por qué el Ecuador se llama imaginario."),
    reinforce="Repite en voz alta: qué es el Ecuador y qué hemisferios forma.",
    extend="Dibuja otra línea de polo a polo y rotula los hemisferios oriental y occidental.",
)

# ---------------------------------------------------------------- clase 3
H3 = ("Ficha de trópicos y polos. El Trópico de Cáncer y el Trópico de Capricornio son dos líneas imaginarias paralelas al Ecuador, es decir, que van en el mismo sentido que él. "
      "El Trópico de Cáncer está al norte del Ecuador y el Trópico de Capricornio está al sur. Entre los dos trópicos se encuentra la zona tropical, donde casi siempre hace calor. "
      "Los polos son los dos extremos de la Tierra: el Polo Norte y el Polo Sur. El Polo Norte está en el océano Glacial Ártico, cubierto de hielo. El Polo Sur está en la Antártica, un continente cubierto de hielo. "
      "El Trópico de Capricornio pasa por el norte de Chile, en la región de Antofagasta; la mayor parte de Chile está al sur de esa línea. Atenas y Roma están al norte del Trópico de Cáncer.")
register(
    OA7, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé qué son los trópicos y los polos y dónde están. Sirve para ubicar lugares y entender dónde hace más calor o más frío.",
    prior=["Sé qué es el Ecuador.", "Sé qué es un hemisferio."],
    explain=[
        "Además del Ecuador hay otras dos líneas imaginarias importantes: los trópicos. El Trópico de Cáncer está al norte del Ecuador y el Trópico de Capricornio está al sur. Van en el mismo sentido que el Ecuador. Entre los dos está la zona tropical, donde casi siempre hace calor.",
        "Los polos son los dos extremos de la Tierra. El Polo Norte está en el océano Glacial Ártico, cubierto de hielo. El Polo Sur está en la Antártica, un continente cubierto de hielo. Cerca de los polos hace mucho frío.",
        "El Trópico de Capricornio pasa por el norte de Chile, en la región de Antofagasta, y la mayor parte de Chile está al sur de esa línea. Atenas y Roma están al norte del Trópico de Cáncer. Para recordar el orden, de norte a sur: Polo Norte, Trópico de Cáncer, Ecuador, Trópico de Capricornio y Polo Sur.",
    ],
    vocab=[("trópico", "cada una de las dos líneas imaginarias paralelas al Ecuador"), ("zona tropical", "zona entre los dos trópicos, donde casi siempre hace calor"), ("polo", "extremo norte o sur de la Tierra"), ("paralela", "que va en el mismo sentido sin cruzarse"), ("Antártica", "continente cubierto de hielo en el Polo Sur")],
    worked=[
        {"title": "Ordenar las referencias", "problem": f"{H3} Ordena de norte a sur: Ecuador, Polo Sur, Trópico de Cáncer, Polo Norte, Trópico de Capricornio.", "steps": ["Empiezo en el extremo norte: Polo Norte.", "Sigo: Trópico de Cáncer, Ecuador, Trópico de Capricornio.", "Termino en el Polo Sur."], "answer": "Polo Norte, Trópico de Cáncer, Ecuador, Trópico de Capricornio, Polo Sur"},
        {"title": "Ubicar un lugar", "problem": f"{H3} ¿Atenas está al norte o al sur del Trópico de Cáncer?", "steps": ["Busco Atenas en la ficha.", "La ficha dice que está al norte del trópico."], "answer": "Al norte"},
    ],
    mistakes=[
        {"wrong": "Confundir los trópicos con el Ecuador.", "why": "Las tres son líneas paralelas.", "fix": "El Ecuador está en el medio y los trópicos a ambos lados."},
        {"wrong": "Decir que el Polo Norte es un continente.", "why": "Se confunde con el Polo Sur.", "fix": "El Polo Norte está en el océano Glacial Ártico y el Polo Sur en la Antártica."},
    ],
    tiers={
        "recovery": [
            ex(f"{H3} ¿Qué trópico está al norte del Ecuador?", "el Trópico de Cáncer", "La ficha lo dice."),
            ex(f"{H3} ¿Qué trópico está al sur del Ecuador?", "el Trópico de Capricornio", "La ficha lo dice."),
            ex(f"{H3} ¿Cuántos polos tiene la Tierra?", "2", "El Polo Norte y el Polo Sur."),
        ],
        "understand": [
            ex(f"{H3} ¿Qué zona está entre los dos trópicos?", "la zona tropical", "La ficha la nombra."),
            ex(f"{H3} ¿Qué cubre el Polo Sur?", "hielo, en la Antártica", "Es un continente cubierto de hielo."),
            ex(f"{H3} ¿Dónde está el Polo Norte?", "en el océano Glacial Ártico", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{H3} ¿Qué línea pasa por el norte de Chile?", "el Trópico de Capricornio", "Así lo dice la ficha."),
            ex(f"{H3} Roma, ¿está al norte o al sur del Trópico de Cáncer?", "al norte", "La ficha dice que Atenas y Roma están al norte."),
            ex(f"{H3} La mayor parte de Chile, ¿está al norte o al sur del Trópico de Capricornio?", "al sur", "La ficha lo dice."),
        ],
        "reason": [
            ex(f"{H3} Marta dice: «El Polo Norte está en un continente de hielo». Corrígela.", "Está en el océano Glacial Ártico cubierto de hielo", "El continente de hielo es la Antártica, en el Polo Sur."),
            ex(f"{H3} Luis dice que los trópicos son líneas pintadas en el suelo. ¿Tiene razón?", "No, son líneas imaginarias", "Se usan para ubicar lugares."),
        ],
        "challenge": [
            ex(f"{H3} Ordena de norte a sur: Trópico de Capricornio, Polo Norte, Ecuador, Polo Sur, Trópico de Cáncer.", "Polo Norte, Trópico de Cáncer, Ecuador, Trópico de Capricornio, Polo Sur", "Se sigue el orden de la ficha."),
            ex(f"{H3} ¿Entre qué dos líneas imaginarias está la zona tropical?", "entre el Trópico de Cáncer y el Trópico de Capricornio", "Es la zona entre los trópicos."),
        ],
    },
    context=[ex("Una expedición viaja a un lugar cubierto de hielo en el Polo Sur. ¿A qué continente llega?", "a la Antártica", "El Polo Sur está en la Antártica.")],
    selfcheck=[
        ex("¿Qué línea está al norte del Ecuador: Cáncer o Capricornio?", "el Trópico de Cáncer", "Capricornio está al sur."),
        ex("¿Dónde hace casi siempre calor?", "en la zona tropical", "Entre los dos trópicos."),
        ex("¿Qué polo está en un continente?", "el Polo Sur", "En la Antártica."),
    ],
    open_task=task(
        f"Dibuja un círculo que sea la Tierra con cinco líneas de lado a lado. Rotula de arriba hacia abajo: Polo Norte, Trópico de Cáncer, Ecuador, Trópico de Capricornio y Polo Sur. Pinta de un color la zona tropical. {H3}",
        "Círculo con puntos arriba (Polo Norte), una línea cerca, otra en el centro (Ecuador), otra abajo y un punto abajo (Polo Sur). Entre las dos líneas de los trópicos, zona pintada.",
        ["cinco referencias rotuladas en orden", "zona tropical entre los trópicos"], ["dibujo rotulado"], ["poner el Ecuador cerca del polo", "invertir los trópicos"],
        "Pide que diga cuál está más al norte."),
    reinforce="Repite el orden de norte a sur de las cinco referencias.",
    extend="Busca en un globo o mapa de tu casa o escuela dónde se dibujan los trópicos y cuéntalo.",
)

# ---------------------------------------------------------------- clase 4
H4 = ("Ficha de continentes y océanos. Los continentes son grandes masas de tierra: América, Europa, Asia, África, Oceanía y Antártica, seis en total para esta ficha. "
      "Los océanos son grandes extensiones de agua salada: el Pacífico, el Atlántico, el Índico y el Glacial Ártico; algunos mapas muestran además el Glacial Antártico. El Pacífico es el más grande. "
      "Un mar es una parte de agua salada más pequeña que un océano. "
      "Chile está en América del Sur, con costa en el océano Pacífico. Europa está al norte del Ecuador. El Ecuador cruza, entre otros, África y América del Sur. La Antártica rodea el Polo Sur. "
      "Grecia e Italia están en Europa, junto al mar Mediterráneo.")
register(
    OA7, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a nombrar los continentes y océanos y a ubicarlos con las referencias del planeta. Sirve para decir dónde está un lugar del mundo.",
    prior=["Sé qué es el Ecuador, los hemisferios, los trópicos y los polos.", "Sé leer un mapa."],
    explain=[
        "Los continentes son las grandes masas de tierra del planeta. Para esta clase son seis: América, Europa, Asia, África, Oceanía y Antártica. Los océanos son grandes extensiones de agua salada: el Pacífico, el Atlántico, el Índico y el Glacial Ártico. El Pacífico es el más grande. Algunos mapas muestran además el Glacial Antártico.",
        "Para ubicar un continente usamos las referencias que ya conocemos. Europa está al norte del Ecuador, en el hemisferio norte. África y América del Sur son cruzadas por el Ecuador. La Antártica rodea el Polo Sur. Chile está en América del Sur, con costa en el océano Pacífico.",
        "Un mar es una parte de agua salada más pequeña que un océano. Grecia e Italia están en Europa, junto al mar Mediterráneo. Para describir un lugar puedes decir: está en tal continente, en tal hemisferio y cerca de tal océano o mar.",
    ],
    vocab=[("continente", "gran masa de tierra del planeta"), ("océano", "gran extensión de agua salada"), ("mar", "parte de agua salada más pequeña que un océano"), ("Pacífico", "el océano más grande, junto a la costa de Chile"), ("Antártica", "continente cubierto de hielo en el Polo Sur")],
    worked=[
        {"title": "Ubicar un país", "problem": f"{H4} Describe dónde está Chile usando continente y océano.", "steps": ["Continente: América del Sur.", "Océano: Pacífico, junto a su costa."], "answer": "En América del Sur, con costa en el océano Pacífico"},
        {"title": "Mar u océano", "problem": f"{H4} ¿El Mediterráneo es un océano o un mar?", "steps": ["No está en la lista de océanos.", "La ficha dice que es un mar."], "answer": "Un mar"},
    ],
    mistakes=[
        {"wrong": "Confundir continente con país.", "why": "Se mezclan tamaños.", "fix": "Un continente es una gran masa de tierra que contiene muchos países."},
        {"wrong": "Decir que el Mediterráneo es un océano.", "why": "Es muy grande, pero la ficha lo llama mar.", "fix": "Un mar es una parte de agua salada más pequeña que un océano."},
    ],
    tiers={
        "recovery": [
            ex(f"{H4} ¿Cuántos continentes hay en esta ficha?", "6", "La ficha enumera seis."),
            ex(f"{H4} ¿Cuál es el océano más grande?", "el Pacífico", "Así lo dice la ficha."),
            ex(f"{H4} ¿En qué continente está Grecia?", "Europa", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{H4} ¿Qué es un océano?", "una gran extensión de agua salada", "Así lo define la ficha."),
            ex(f"{H4} ¿Cuál es la diferencia entre un mar y un océano?", "el mar es más pequeño", "Así lo dice la ficha."),
            ex(f"{H4} ¿Qué continente rodea el Polo Sur?", "la Antártica", "Así lo dice la ficha."),
        ],
        "apply": [
            ex(f"{H4} ¿Qué océano baña la costa de Chile?", "el Pacífico", "Así lo dice la ficha."),
            ex(f"{H4} ¿Qué mar está junto a Grecia e Italia?", "el Mediterráneo", "La ficha lo dice."),
            ex(f"{H4} ¿Europa está en el hemisferio norte o en el sur?", "en el hemisferio norte", "Está al norte del Ecuador."),
        ],
        "reason": [
            ex(f"{H4} Ema dice que Chile es un continente. Corrígela.", "Chile es un país de América del Sur", "Un continente contiene muchos países."),
            ex(f"{H4} Sofía dice que el Ecuador no pasa por ningún continente. ¿Tiene razón?", "No, cruza África y América del Sur, entre otros", "La ficha lo dice."),
        ],
        "challenge": [
            ex(f"{H4} Describe dónde está Italia usando continente, hemisferio y mar.", "En Europa, en el hemisferio norte, junto al mar Mediterráneo", "La ficha da cada dato."),
            ex(f"{H4} Une cada referencia con su lugar: A) Antártica; B) Pacífico; C) Europa. 1) océano; 2) continente al norte del Ecuador; 3) continente en el Polo Sur.", "A con 3; B con 1; C con 2", "Cada una tiene un rol distinto."),
        ],
    },
    context=[ex("Un barco sale de la costa de Chile hacia el oeste. ¿En qué océano navega?", "en el Pacífico", "La costa de Chile está junto al Pacífico.")],
    selfcheck=[
        ex("¿Cuáles son los continentes de la ficha?", "América, Europa, Asia, África, Oceanía y Antártica", "La ficha enumera seis continentes."),
        ex("¿Cuál es el océano más grande?", "el Pacífico", "Baña la costa de Chile."),
        ex("¿Qué es un mar?", "una parte de agua salada más pequeña que un océano", "Como el Mediterráneo."),
    ],
    open_task=task(
        f"Haz un cartel que diga: «Mi ubicación en el planeta». Escribe continente, hemisferio norte o sur, y océano más cercano para Chile. Agrega los mismos tres datos para Grecia. {H4}",
        "Chile: continente América del Sur, hemisferio sur, océano Pacífico. Grecia: continente Europa, hemisferio norte, mar Mediterráneo.",
        ["tres datos para Chile", "tres datos para Grecia", "datos correctos"], ["cartel escrito"], ["decir que Chile está en Europa", "no distinguir mar de océano"],
        "Pregunta qué los diferencia."),
    reinforce="Nombra los seis continentes y los cuatro océanos de la ficha.",
    extend="Elige otro país y descríbelo con continente, hemisferio y océano, con ayuda de un mapa.",
)

# ================================================================ OA 08 · ZONAS CLIMÁTICAS
# ---------------------------------------------------------------- clase 1
Z1 = ("Ficha de zonas climáticas. El tiempo atmosférico es cómo está la atmósfera hoy: si llueve, si hace sol, si hay viento. El clima es el tiempo que suele haber en un lugar durante muchos años. "
      "Las zonas climáticas del mundo son tres. La zona cálida está cerca del Ecuador, entre los trópicos, y casi siempre hace calor. La zona templada está a ambos lados, entre la cálida y la fría, y tiene estaciones: verano, otoño, invierno y primavera. "
      "La zona fría está cerca de los polos y tiene inviernos muy fríos. Los límites entre las zonas no son líneas exactas: una zona cambia poco a poco a la otra. "
      "Ejemplos: la Amazonía está en la zona cálida; Grecia, Italia y el centro de Chile están en la zona templada; la Antártica está en la zona fría.")
register(
    OA8, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cuáles son las zonas climáticas del mundo y dónde están. Sirve para entender por qué algunos lugares son cálidos y otros fríos.",
    prior=["Sé qué es el Ecuador, los trópicos y los polos.", "Sé que hay estaciones en algunos lugares."],
    explain=[
        "El tiempo atmosférico es cómo está el cielo hoy: lluvia, sol o viento. El clima es el tiempo que suele haber en un lugar durante muchos años. Por ejemplo, un día puede estar nublado en un lugar donde casi siempre hace sol. El clima se mide con muchos años de datos.",
        "El mundo tiene tres zonas climáticas. La zona cálida está cerca del Ecuador, entre los trópicos, y casi siempre hace calor. La zona templada está a ambos lados y tiene cuatro estaciones. La zona fría está cerca de los polos y tiene inviernos muy fríos.",
        "Los límites entre las zonas no son líneas exactas como una pared. Una zona cambia poco a poco a la otra. En los mapas se dibujan líneas para ayudarnos, pero en la realidad el cambio es gradual. La Amazonía está en la zona cálida. Grecia, Italia y el centro de Chile están en la zona templada. La Antártica está en la zona fría.",
    ],
    vocab=[("clima", "tiempo que suele haber en un lugar durante muchos años"), ("tiempo atmosférico", "cómo está la atmósfera en un momento, como lluvia o sol"), ("zona cálida", "zona cerca del Ecuador, donde casi siempre hace calor"), ("zona templada", "zona con cuatro estaciones, entre la cálida y la fría"), ("zona fría", "zona cerca de los polos, con inviernos muy fríos")],
    worked=[
        {"title": "Clima o tiempo", "problem": f"{Z1} «Hoy llueve en mi ciudad». ¿Es tiempo atmosférico o clima?", "steps": ["Habla de hoy.", "El tiempo atmosférico es cómo está hoy."], "answer": "Tiempo atmosférico"},
        {"title": "Ubicar una zona", "problem": f"{Z1} ¿En qué zona está la Antártica?", "steps": ["Busco Antártica en los ejemplos.", "La ficha la ubica en la zona fría."], "answer": "En la zona fría"},
    ],
    mistakes=[
        {"wrong": "Confundir tiempo atmosférico con clima.", "why": "Ambos hablan del cielo.", "fix": "El tiempo es de hoy y el clima es lo que suele haber en muchos años."},
        {"wrong": "Pensar que entre una zona y otra hay una línea exacta.", "why": "Los mapas dibujan líneas.", "fix": "Los límites son graduales: una zona cambia poco a poco."},
    ],
    tiers={
        "recovery": [
            ex(f"{Z1} ¿Cuántas zonas climáticas hay en esta ficha?", "3", "La ficha enumera tres."),
            ex(f"{Z1} ¿En qué zona está la Amazonía?", "en la zona cálida", "La ficha lo dice."),
            ex(f"{Z1} ¿Dónde está la zona fría?", "cerca de los polos", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{Z1} ¿Qué es el clima?", "el tiempo que suele haber en un lugar durante muchos años", "Así lo define la ficha."),
            ex(f"{Z1} ¿Qué tiene la zona templada que no se menciona para las otras?", "cuatro estaciones", "La ficha lo dice."),
            ex(f"{Z1} ¿Los límites entre zonas son líneas exactas?", "no, cambian poco a poco", "Así lo dice la ficha."),
        ],
        "apply": [
            ex(f"{Z1} «Mañana habrá viento fuerte». ¿Es tiempo atmosférico o clima?", "tiempo atmosférico", "Habla de un día."),
            ex(f"{Z1} Un lugar cerca del Polo Sur, ¿en qué zona está?", "en la zona fría", "Los polos tienen zona fría."),
            ex(f"{Z1} Ordena las zonas desde el Ecuador hacia un polo: fría, cálida, templada.", "cálida, templada, fría", "Se pasa de la cálida a la templada y a la fría."),
        ],
        "reason": [
            ex(f"{Z1} Pedro dice que la zona templada empieza justo en una línea, como una pared. Corrígelo.", "Las zonas cambian poco a poco", "Los límites no son exactos."),
            ex(f"{Z1} Ana dice: «Si hoy hace calor en Grecia, entonces su clima es siempre caluroso». ¿Es correcto?", "No, un día no define el clima", "El clima es lo que suele haber en muchos años."),
        ],
        "challenge": [
            ex(f"{Z1} Une cada lugar con su zona: A) Antártica; B) Italia; C) Amazonía. 1) templada; 2) cálida; 3) fría.", "A con 3; B con 1; C con 2", "La ficha da los ejemplos."),
            ex(f"{Z1} Grecia y el centro de Chile, ¿están en la misma zona climática?", "sí, en la zona templada", "La ficha las ubica ahí."),
        ],
    },
    context=[ex("Un noticiero dice «hoy lloverá en Santiago». ¿Habla de clima o de tiempo atmosférico?", "tiempo atmosférico", "Habla de un día.")],
    selfcheck=[
        ex("¿Cuáles son las tres zonas climáticas?", "cálida, templada y fría", "Son las de la ficha."),
        ex("¿En qué zona hace casi siempre calor?", "en la zona cálida", "Está cerca del Ecuador."),
        ex("¿Cómo son los límites entre las zonas?", "graduales, no son líneas exactas", "Cambian poco a poco."),
    ],
    open_task=task(
        f"Dibuja un círculo que sea la Tierra. Pinta con tres colores las franjas de las zonas climáticas, de forma que se mezclen un poco en los bordes. Rotula cálida, templada y fría. Ubica con puntos la Amazonía, Grecia y la Antártica. {Z1}",
        "Franja cálida en el centro, templadas a ambos lados y frías en los polos, con bordes suaves. Puntos: Amazonía en la cálida, Grecia en la templada del norte y Antártica en la fría del sur.",
        ["tres zonas rotuladas", "bordes graduales", "tres lugares bien ubicados"], ["dibujo coloreado"], ["líneas rígidas", "poner la Antártica en la zona cálida"],
        "Pregunta por qué los bordes se mezclan."),
    reinforce="Explica con un ejemplo la diferencia entre clima y tiempo atmosférico.",
    extend="Anota durante tres días el tiempo atmosférico de tu lugar y di si eso sirve para saber el clima.",
)

# ---------------------------------------------------------------- clase 2
Z2 = ("Ficha de paisajes y climas. Selva tropical: zona cálida, con lluvias casi todo el año y árboles muy altos, como en la Amazonía. "
      "Sabana: zona cálida, con una estación de lluvias y otra seca, con pastos y pocos árboles. "
      "Bosque templado: zona templada, con lluvias y estaciones, donde algunos árboles pierden sus hojas en otoño. "
      "Clima mediterráneo: zona templada, con inviernos con lluvia y veranos secos y calurosos, como en Grecia, Italia y el centro de Chile. "
      "Paisaje de hielo: zona fría, con nieve y hielo casi todo el año, como en la Antártica. "
      "Los desiertos son lugares donde llueve muy poco; pueden estar en distintas zonas.")
register(
    OA8, 2,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a relacionar el clima de una zona con el paisaje que se forma allí. Sirve para describir paisajes del mundo con datos.",
    prior=["Sé qué son las tres zonas climáticas.", "Sé qué es el clima."],
    explain=[
        "El clima y el paisaje se relacionan. El paisaje es lo que se ve en un lugar: plantas, relieve, agua y construcciones. Si llueve mucho y hace calor, crece una selva con árboles altos. Si llueve poco, hay pastos o desierto.",
        "En la zona cálida hay selva tropical, con lluvias casi todo el año, y sabana, con una estación de lluvias y otra seca. En la zona templada hay bosques templados y lugares con clima mediterráneo, con veranos secos y calurosos, como en Grecia, Italia y el centro de Chile. En la zona fría hay paisajes de hielo, como en la Antártica.",
        "Los desiertos son lugares donde llueve muy poco. Pueden estar en distintas zonas, porque lo que los define es la poca lluvia, no el calor o el frío. Por eso, para describir un paisaje conviene mirar dos cosas: la zona y la cantidad de lluvia.",
    ],
    vocab=[("paisaje", "lo que se ve en un lugar: plantas, relieve, agua y construcciones"), ("selva tropical", "bosque muy alto y húmedo de la zona cálida"), ("sabana", "paisaje cálido con pastos, estación de lluvias y estación seca"), ("clima mediterráneo", "inviernos con lluvia y veranos secos y calurosos"), ("desierto", "lugar donde llueve muy poco")],
    worked=[
        {"title": "Clima y paisaje", "problem": f"{Z2} Un lugar tiene calor y lluvia casi todo el año. ¿Qué paisaje es probable?", "steps": ["Calor y lluvia: zona cálida y mucha lluvia.", "La ficha dice que eso forma una selva tropical."], "answer": "Selva tropical"},
        {"title": "Un paisaje que cruza zonas", "problem": f"{Z2} ¿En qué zona están los desiertos?", "steps": ["La ficha dice que pueden estar en distintas zonas.", "Lo que los define es la poca lluvia."], "answer": "Pueden estar en distintas zonas"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los desiertos son cálidos.", "why": "Se asocia desierto con calor.", "fix": "Un desierto es un lugar donde llueve muy poco; puede estar en distintas zonas."},
        {"wrong": "Decir que en la zona cálida solo hay selva.", "why": "Se generaliza.", "fix": "También hay sabana y otros paisajes."},
    ],
    tiers={
        "recovery": [
            ex(f"{Z2} ¿En qué zona hay selva tropical?", "en la zona cálida", "La ficha lo dice."),
            ex(f"{Z2} ¿Qué paisaje hay en la Antártica?", "de hielo", "La ficha lo dice."),
            ex(f"{Z2} ¿Dónde llueve muy poco: en un desierto o en una selva?", "en un desierto", "Así lo define la ficha."),
        ],
        "understand": [
            ex(f"{Z2} ¿Cómo son los veranos del clima mediterráneo?", "secos y calurosos", "La ficha lo dice."),
            ex(f"{Z2} ¿Qué diferencia hay entre selva y sabana en las lluvias?", "la selva llueve casi todo el año y la sabana tiene una estación seca", "La ficha lo explica."),
            ex(f"{Z2} ¿Qué es un paisaje?", "lo que se ve en un lugar: plantas, relieve, agua y construcciones", "Así lo define la clase."),
        ],
        "apply": [
            ex(f"{Z2} En un lugar de la zona templada llueve en invierno y los veranos son secos y calurosos. ¿Qué clima es?", "mediterráneo", "La ficha lo describe así."),
            ex(f"{Z2} En un lugar nieva casi todo el año y todo está cubierto de hielo. ¿En qué zona está?", "en la zona fría", "El paisaje de hielo es de la zona fría."),
            ex(f"{Z2} Un lugar de la zona cálida tiene una estación de lluvias, una seca, pastos y pocos árboles. ¿Qué paisaje es?", "una sabana", "Así lo describe la ficha."),
        ],
        "reason": [
            ex(f"{Z2} Marta dice: «Todo desierto es muy caluroso». Corrígela.", "Un desierto es un lugar donde llueve muy poco y puede estar en distintas zonas", "El desierto se define por la poca lluvia."),
            ex(f"{Z2} ¿Por qué las plantas de la selva son tan altas y numerosas? Elige. A) Porque llueve mucho y hace calor. B) Porque no llueve nunca.", "A", "La lluvia y el calor ayudan a crecer."),
        ],
        "challenge": [
            ex(f"{Z2} Une cada lugar con su paisaje: A) Amazonía; B) Grecia; C) Antártica. 1) selva tropical; 2) clima mediterráneo; 3) hielo.", "A con 1; B con 2; C con 3", "La ficha da cada ejemplo."),
            ex(f"{Z2} Grecia y el centro de Chile, ¿tienen el mismo tipo de clima según la ficha?", "sí, mediterráneo", "La ficha las pone como ejemplo."),
        ],
    },
    context=[ex("Un viajero llega a un lugar con árboles altísimos y lluvia casi todos los días. ¿Qué paisaje encontró?", "una selva tropical", "Calor y lluvia forman la selva.")],
    selfcheck=[
        ex("¿Qué es un desierto?", "un lugar donde llueve muy poco", "No depende de la zona."),
        ex("¿Qué clima tiene Grecia?", "mediterráneo", "Inviernos con lluvia y veranos secos."),
        ex("¿Qué paisaje hay en la Antártica?", "de hielo", "Es de la zona fría."),
    ],
    open_task=task(
        f"Haz un cuadro con tres columnas: «Zona», «Paisaje» y «Cómo es el clima». Completa cuatro filas con datos de la ficha. {Z2}",
        "Cálida / selva tropical / lluvias casi todo el año. Cálida / sabana / estación de lluvias y estación seca. Templada / clima mediterráneo / invierno con lluvia y verano seco. Fría / hielo / nieve casi todo el año.",
        ["cuatro filas", "datos de la ficha", "zona y clima coherentes"], ["cuadro completo"], ["poner selva en la zona fría", "no explicar el clima"],
        "Pregunta cuál paisaje le gustaría visitar."),
    reinforce="Describe en voz alta un paisaje de la ficha sin decir su nombre y pide que lo adivinen.",
    extend="Escribe cómo es el paisaje cerca de tu casa y a qué clima de la ficha se parece.",
)

# ---------------------------------------------------------------- clase 3
Z3 = ("Ficha de formas de habitar. En lugares con mucha lluvia o ríos que crecen, algunas comunidades de la Amazonía construyen casas elevadas sobre palos para evitar la humedad y el agua. "
      "En Chiloé, en el sur de Chile, hay palafitos: casas de madera construidas sobre palos en la orilla del mar. "
      "En zonas frías, las casas tienen paredes gruesas para guardar el calor y techos con pendiente para que la nieve resbale, y las personas usan ropa muy abrigadora. "
      "En zonas con veranos secos y calurosos, como Grecia, hay casas con paredes gruesas, muchas pintadas de blanco, para mantener fresco adentro. "
      "Una estrategia es una forma de resolver un problema; aquí, el problema es vivir bien en un clima.")
register(
    OA8, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo las personas han ideado formas distintas de vivir en climas y paisajes diferentes. Sirve para explicar con ejemplos concretos.",
    prior=["Sé qué son las zonas climáticas.", "Sé que los paisajes dependen del clima."],
    explain=[
        "Las personas viven en climas muy distintos y han inventado formas de vivir bien en cada uno. Una estrategia es una forma de resolver un problema. Aquí, el problema es cómo vivir cómodo y seguro con el calor, el frío, la lluvia o el agua.",
        "En lugares con mucha lluvia o ríos que crecen, algunas comunidades de la Amazonía construyen casas elevadas sobre palos. En Chiloé hay palafitos, casas de madera sobre palos en la orilla del mar. En zonas frías hay paredes gruesas, techos con pendiente y ropa abrigadora. En Grecia, donde los veranos son secos y calurosos, muchas casas tienen paredes gruesas y pintadas de blanco para mantener fresco adentro.",
        "Estas estrategias dependen del clima, de los materiales disponibles y de lo que las personas saben hacer. Distintas comunidades pueden resolver el mismo problema de manera diferente. Y hoy las soluciones también cambian con la tecnología.",
    ],
    vocab=[("estrategia", "forma de resolver un problema"), ("palafito", "casa construida sobre palos"), ("pendiente", "inclinación de un techo o terreno"), ("abrigadora", "que da calor y protege del frío"), ("comunidad", "grupo de personas que viven juntas")],
    worked=[
        {"title": "Problema y estrategia", "problem": f"{Z3} En una zona fría cae mucha nieve sobre los techos. ¿Qué estrategia se usa?", "steps": ["Busco zona fría y nieve.", "La ficha dice techos con pendiente para que la nieve resbale."], "answer": "Techos con pendiente"},
        {"title": "Mismo problema, otra solución", "problem": f"{Z3} ¿Cómo evitan la humedad y el agua en una zona de ríos que crecen en la Amazonía?", "steps": ["Busco la Amazonía.", "Construyen casas elevadas sobre palos."], "answer": "Casas elevadas sobre palos"},
    ],
    mistakes=[
        {"wrong": "Decir que todas las personas de una zona viven igual.", "why": "Se generaliza.", "fix": "Distintas comunidades resuelven el problema de maneras diferentes."},
        {"wrong": "Decir que una estrategia es mejor que otra.", "why": "Se compara sin considerar el lugar.", "fix": "Cada estrategia responde a su clima, su paisaje y sus materiales."},
    ],
    tiers={
        "recovery": [
            ex(f"{Z3} ¿Qué es una estrategia?", "una forma de resolver un problema", "Así lo define la ficha."),
            ex(f"{Z3} ¿Qué es un palafito?", "una casa construida sobre palos", "Así lo dice la ficha."),
            ex(f"{Z3} ¿Dónde hay palafitos en Chile, según la ficha?", "en Chiloé", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{Z3} ¿Para qué sirven los techos con pendiente en zonas frías?", "para que la nieve resbale", "La ficha lo dice."),
            ex(f"{Z3} ¿Por qué las paredes gruesas ayudan en zonas frías?", "porque guardan el calor", "La ficha lo dice."),
            ex(f"{Z3} ¿Por qué muchas casas de Grecia se pintan de blanco?", "para mantener fresco adentro", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{Z3} Una comunidad vive junto a un río que crece cada año. ¿Qué estrategia de la ficha le sirve?", "casas elevadas sobre palos", "Evitan la humedad y el agua."),
            ex(f"{Z3} Una familia vive en una zona muy fría. ¿Qué ropa usa?", "ropa muy abrigadora", "La ficha lo dice."),
            ex(f"{Z3} Un lugar tiene veranos secos y muy calurosos. ¿Qué casa ayuda a mantener fresco?", "una con paredes gruesas, pintada de blanco", "Así lo dice la ficha."),
        ],
        "reason": [
            ex(f"{Z3} Luis dice: «Todas las casas de una zona fría son iguales». Corrígelo con un dato.", "Distintas comunidades pueden resolver el problema de maneras diferentes", "La ficha explica que hay varias estrategias."),
            ex(f"{Z3} Ema dice que los palafitos son mejores que las casas de paredes gruesas. ¿Tiene razón?", "No, cada estrategia responde a su lugar", "Son soluciones a problemas distintos."),
        ],
        "challenge": [
            ex(f"{Z3} Une cada problema con su estrategia: A) nieve en el techo; B) humedad por ríos que crecen; C) calor fuerte en verano. 1) casas elevadas; 2) techo con pendiente; 3) paredes gruesas pintadas de blanco.", "A con 2; B con 1; C con 3", "La ficha da cada pareja."),
            ex(f"{Z3} Escribe una estrategia de la ficha para un lugar frío y una para un lugar cálido.", "frío: paredes gruesas, techos con pendiente o ropa abrigadora. Cálido: casas elevadas sobre palos o paredes gruesas pintadas de blanco", "La ficha da cada una."),
        ],
    },
    context=[ex("Una persona quiere construir una casa junto al mar en Chiloé, sobre el borde del agua. ¿Qué tipo de casa tradicional puede copiar?", "un palafito", "Es una casa sobre palos en la orilla del mar.")],
    selfcheck=[
        ex("¿Qué es una estrategia para habitar?", "una forma de resolver el problema de vivir bien en un clima", "Depende del lugar."),
        ex("¿Para qué sirve un techo con pendiente?", "para que la nieve resbale", "Evita que se acumule."),
        ex("¿Qué casas hay en Chiloé?", "palafitos", "Casas sobre palos."),
    ],
    open_task=task(
        f"Elige dos estrategias de la ficha. Dibuja cada una y escribe debajo el problema que resuelve, la zona donde sirve y de qué material podría estar hecha. {Z3}",
        "Palafito: resuelve vivir junto al mar, zona templada de Chiloé, de madera. Techo con pendiente: resuelve la nieve, zona fría, de madera o chapa.",
        ["dos estrategias", "problema nombrado", "zona nombrada"], ["dos dibujos con texto"], ["decir que una es mejor", "mezclar estrategias"],
        "Pregunta por qué esa estrategia sirve en ese lugar."),
    reinforce="Cuenta en voz alta una estrategia para vivir en un lugar frío y otra en uno lluvioso.",
    extend="Escribe cómo tu casa te protege del calor, del frío o de la lluvia.",
)

# ---------------------------------------------------------------- clase 4
Z4 = ("Ficha de generalizaciones. Una generalización es una frase que dice que todo es igual, con palabras como «todos», «siempre» o «nunca». Casi nunca es exacta. "
      "Un ejemplo es un caso preciso con lugar. Datos: en la zona templada hay lugares con clima mediterráneo, como Grecia y el centro de Chile, y lugares de bosques con mucha lluvia. "
      "En Chiloé, que está en la zona templada, hay palafitos, y en otros lugares templados hay casas de distinto tipo. "
      "En una misma zona climática hay personas que viven de distinto modo. Además, la tecnología cambia las soluciones: hoy hay calefacción y ventiladores.")
register(
    OA8, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a hablar de climas y formas de vivir sin decir que todas las personas son iguales. Sirve para describir el mundo con precisión.",
    prior=["Sé qué son las zonas climáticas y los paisajes.", "Sé qué es una estrategia."],
    explain=[
        "El clima influye en cómo viven las personas, pero no decide todo. En un mismo clima, personas distintas pueden vivir de maneras diferentes. Por eso hay que cuidarse de las generalizaciones, que son frases con palabras como «todos», «siempre» o «nunca».",
        "Una generalización dice que todo es igual y casi nunca es exacta. Por ejemplo, «todas las personas de la zona fría viven igual» es una generalización. En cambio, «en esta zona fría muchas casas tienen techo con pendiente» es un ejemplo con lugar y es más preciso.",
        "También hay que recordar que la tecnología cambia las soluciones. Hoy muchas personas usan calefacción o ventiladores. Para hablar bien de un lugar, nombra el lugar, di «muchas» o «algunas» en lugar de «todas», y da un ejemplo.",
    ],
    vocab=[("generalización", "frase que dice que todo es igual, con palabras como todos o siempre"), ("ejemplo", "caso preciso con lugar"), ("influir", "tener efecto sobre algo"), ("precisa", "que dice exactamente lo que ocurre"), ("tecnología", "objetos y técnicas para resolver problemas")],
    worked=[
        {"title": "Detectar una generalización", "problem": f"{Z4} «Todos los habitantes de la zona fría viven igual». ¿Es una generalización o un ejemplo?", "steps": ["Tiene la palabra todos.", "Dice que todo es igual."], "answer": "Una generalización"},
        {"title": "Mejorar la frase", "problem": f"{Z4} Mejora la frase: «Todos los chilotes viven en palafitos».", "steps": ["Cambio todos por algunos.", "Nombro el lugar: en Chiloé hay palafitos."], "answer": "En Chiloé hay palafitos"},
    ],
    mistakes=[
        {"wrong": "Decir «todos» o «siempre» sin pensar si es cierto.", "why": "Parece una frase fuerte.", "fix": "Usa «muchos», «algunos» y nombra el lugar."},
        {"wrong": "Pensar que el clima decide todo lo que hacen las personas.", "why": "Se olvidan las elecciones y la tecnología.", "fix": "En un mismo clima hay formas distintas de vivir."},
    ],
    tiers={
        "recovery": [
            ex(f"{Z4} ¿Qué es una generalización?", "una frase que dice que todo es igual", "Así la define la ficha."),
            ex(f"{Z4} Nombra dos palabras que suelen aparecer en una generalización.", "dos de: todos, siempre, nunca", "La ficha las nombra."),
            ex(f"{Z4} ¿Qué es un ejemplo?", "un caso preciso con lugar", "Así lo define la ficha."),
        ],
        "understand": [
            ex(f"{Z4} ¿Por qué una generalización casi nunca es exacta?", "porque no todo es igual en todos los lugares", "Hay diferencias entre personas y lugares."),
            ex(f"{Z4} ¿Qué cambia las soluciones además del clima?", "la tecnología", "La ficha lo dice."),
            ex(f"{Z4} ¿En qué zona climática está Chiloé, según la ficha?", "en la zona templada", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{Z4} Clasifica como generalización o ejemplo: «En Chiloé hay palafitos».", "ejemplo", "Nombra un lugar y un caso."),
            ex(f"{Z4} Clasifica como generalización o ejemplo: «Nadie en el desierto tiene casas de madera».", "generalización", "Usa la palabra nadie."),
            ex(f"{Z4} Mejora «Todas las casas de la zona templada tienen techo inclinado». Elige. A) Algunas casas de la zona templada tienen techo inclinado. B) Todas las casas del mundo son iguales.", "A", "A cambia todas por algunas."),
        ],
        "reason": [
            ex(f"{Z4} Ana dice: «En la zona fría siempre se vive igual». ¿Qué datos de la ficha lo contradicen?", "En una misma zona hay personas que viven de distinto modo", "La ficha lo afirma."),
            ex(f"{Z4} Pedro dice que hoy no se necesitan estrategias porque hay calefacción. ¿Tiene razón?", "No, la tecnología cambia las soluciones, pero las estrategias siguen siendo necesarias", "Hoy se usan soluciones nuevas."),
        ],
        "challenge": [
            ex(f"{Z4} Reescribe sin generalizar: «Todos los chilenos viven en casas iguales».", "Muchas casas en Chile son distintas según el lugar", "Se cambia todos por muchas y se acota."),
            ex(f"{Z4} Compara Chiloé y el centro de Chile: ambos están en la zona templada. ¿Tienen siempre el mismo tipo de casa?", "no, pueden tener casas distintas", "La ficha dice que hay distintas formas."),
        ],
    },
    context=[ex("Un video dice: «Todas las personas de la selva viven en casas sobre palos». ¿Cómo lo corriges?", "Algunas comunidades de la Amazonía construyen casas elevadas sobre palos", "Se cambia todas por algunas y se nombra el lugar.")],
    selfcheck=[
        ex("¿Qué palabras avisan que puede ser una generalización?", "todos, siempre y nunca", "Dicen que todo es igual."),
        ex("¿Qué palabras puedes usar en su lugar?", "muchos o algunos", "Son más exactas."),
        ex("¿El clima decide todo lo que hacen las personas?", "no", "Hay formas distintas de vivir."),
    ],
    open_task=task(
        f"Escribe cuatro frases sobre cómo viven las personas en un clima, dos con generalizaciones y dos con ejemplos. Marca cuáles son cuáles. Luego corrige las generalizaciones. {Z4}",
        "1) Todos viven igual en la zona fría (generalización) → Muchas casas de la zona fría tienen paredes gruesas. 2) En Chiloé hay palafitos (ejemplo). 3) Nunca llueve en un desierto (generalización) → En un desierto llueve muy poco. 4) En Grecia muchas casas son blancas (ejemplo).",
        ["cuatro frases", "dos generalizaciones y dos ejemplos", "correcciones"], ["frases marcadas y corregidas"], ["confundir ejemplo con generalización", "no corregir"],
        "Pregunta cómo supo cuáles eran generalizaciones."),
    reinforce="Busca la palabra «todos» o «siempre» en algo que escuches hoy y pregunta si es exacto.",
    extend="Reescribe una frase de esta unidad usando «algunas» en lugar de «todas».",
)

# ================================================================ OA 09 · ENTORNO GEOGRÁFICO
# ---------------------------------------------------------------- clase 1
E1 = ("Ficha del país imaginario Valle Azul. Al oeste hay un océano. Al este hay una cordillera de montañas. Entre las montañas y el océano hay un valle largo, por donde corre un río que nace en las montañas y desemboca en el mar. "
      "En la costa hay una península, que es una tierra rodeada de agua por casi todos lados. Frente a la costa hay un archipiélago, que es un grupo de islas. "
      "En la desembocadura del río hay una ciudad con un puerto, donde llegan los barcos. En la plaza de la ciudad hay un monumento, que es una obra construida para recordar algo o a alguien.")
register(
    OA9, 1,
    materials="Lápiz y papel. La ficha de Valle Azul está escrita en cada ejercicio.",
    use="Aprenderé palabras para describir el relieve y el agua de un lugar. Sirve para caracterizar un entorno geográfico.",
    prior=["Sé qué es un mapa.", "Sé los puntos cardinales."],
    explain=[
        "Un entorno geográfico es el lugar donde vive una sociedad: su relieve, su agua y sus construcciones. El relieve son las formas de la tierra: montañas, valles, penínsulas e islas. El agua son los océanos, mares y ríos.",
        "Una montaña es una elevación grande de la tierra. Un valle es una zona baja entre montañas. Un río es una corriente de agua que corre hacia el mar. Una península es una tierra rodeada de agua por casi todos lados. Un archipiélago es un grupo de islas. Un océano o un mar es una gran extensión de agua salada.",
        "Las ciudades y las construcciones también son parte del entorno. Un puerto es un lugar donde llegan los barcos. Un monumento es una obra construida para recordar algo o a alguien. Para describir un lugar, usamos estas palabras con cuidado.",
    ],
    vocab=[("montaña", "elevación grande de la tierra"), ("valle", "zona baja entre montañas"), ("península", "tierra rodeada de agua por casi todos lados"), ("archipiélago", "grupo de islas"), ("monumento", "obra construida para recordar algo o a alguien")],
    worked=[
        {"title": "Usar el vocabulario", "problem": f"{E1} ¿Qué es el grupo de islas frente a la costa?", "steps": ["Busco grupo de islas.", "Es un archipiélago."], "answer": "Un archipiélago"},
        {"title": "Seguir el río", "problem": f"{E1} ¿Dónde nace y dónde desemboca el río de Valle Azul?", "steps": ["Nace en las montañas.", "Desemboca en el mar."], "answer": "Nace en las montañas y desemboca en el mar"},
    ],
    mistakes=[
        {"wrong": "Llamar península a una isla.", "why": "Ambas están rodeadas de agua.", "fix": "La península está rodeada de agua por casi todos lados, no por todos."},
        {"wrong": "Confundir valle con montaña.", "why": "Ambos están en el relieve.", "fix": "La montaña es alta; el valle es una zona baja entre montañas."},
    ],
    tiers={
        "recovery": [
            ex(f"{E1} ¿Qué hay al oeste de Valle Azul?", "un océano", "La ficha lo dice."),
            ex(f"{E1} ¿Qué hay al este de Valle Azul?", "una cordillera de montañas", "La ficha lo dice."),
            ex(f"{E1} ¿Qué es un archipiélago?", "un grupo de islas", "Así lo define la ficha."),
        ],
        "understand": [
            ex(f"{E1} ¿Qué es una península?", "una tierra rodeada de agua por casi todos lados", "Así lo define la ficha."),
            ex(f"{E1} ¿Qué es un valle?", "una zona baja entre montañas", "Así lo dice la clase."),
            ex(f"{E1} ¿Qué es un puerto?", "un lugar donde llegan los barcos", "Así lo dice la ficha."),
        ],
        "apply": [
            ex(f"{E1} ¿Dónde está el valle de Valle Azul: entre las montañas y el océano o al otro lado del mar?", "entre las montañas y el océano", "La ficha lo dice."),
            ex(f"{E1} ¿Qué construcción hay en la desembocadura del río?", "una ciudad con puerto", "La ficha lo dice."),
            ex(f"{E1} ¿Qué hay en la plaza de la ciudad?", "un monumento", "La ficha lo dice."),
        ],
        "reason": [
            ex(f"{E1} Tomás dice que el archipiélago es una península grande. Corrígelo.", "Un archipiélago es un grupo de islas", "Una península es tierra unida al continente."),
            ex(f"{E1} ¿Por qué el río es importante para la ciudad con puerto?", "porque lleva agua y desemboca en el mar donde llegan los barcos", "Une las montañas con el mar."),
        ],
        "challenge": [
            ex(f"{E1} Une cada palabra con su definición: A) montaña; B) valle; C) península. 1) tierra rodeada de agua por casi todos lados; 2) elevación grande de la tierra; 3) zona baja entre montañas.", "A con 2; B con 3; C con 1", "Cada palabra tiene su definición."),
            ex(f"{E1} Ordena de este a oeste: océano, valle, cordillera.", "cordillera, valle, océano", "La cordillera está al este y el océano al oeste."),
        ],
    },
    context=[ex("Un mapa muestra un grupo de 12 islas frente a la costa de un país. ¿Cómo se llama ese grupo?", "archipiélago", "Es un grupo de islas.")],
    selfcheck=[
        ex("¿Qué es un río?", "una corriente de agua que corre hacia el mar", "Nace en las montañas."),
        ex("¿Qué es un monumento?", "una obra construida para recordar algo o a alguien", "Está en la ciudad."),
        ex("¿Qué es una montaña?", "una elevación grande de la tierra", "No es un valle."),
    ],
    open_task=task(
        f"Dibuja el mapa de Valle Azul con el océano al oeste, la cordillera al este y el valle en el medio, con el río, la ciudad con puerto, la península y el archipiélago. Rotula cada elemento. {E1}",
        "Mapa con el océano a la izquierda, montañas a la derecha, un valle largo en el medio con río que va hacia el mar, ciudad y puerto en la desembocadura, una península en la costa y un archipiélago al frente.",
        ["al menos siete elementos", "orientación correcta", "rótulos correctos"], ["mapa dibujado"], ["poner las montañas al oeste", "no rotular"],
        "Pide que describa su mapa usando las palabras nuevas."),
    reinforce="Nombra cinco elementos del relieve o del agua y qué es cada uno.",
    extend="Describe con estas palabras un paisaje que conozcas.",
)

# ---------------------------------------------------------------- clase 2
E2 = ("Ficha del entorno de las polis griegas. Grecia tiene una parte unida al continente europeo, que es una península, y muchas islas. Hay archipiélagos, como grupos de islas en el mar Egeo. "
      "Al este está el mar Egeo, al oeste el mar Jónico y al sur el mar Mediterráneo. En el sur hay una península grande llamada el Peloponeso. "
      "Gran parte del territorio es montañoso, con valles y pocas llanuras anchas. El monte Olimpo, en el norte, era según los mitos el hogar de los dioses. "
      "Atenas está cerca de la costa y tiene un cerro, la Acrópolis, con templos como el Partenón. Esparta y Olimpia estaban en el Peloponeso. Muchas polis estaban cerca del mar y tenían puerto.")
register(
    OA9, 2,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo era el entorno geográfico donde vivieron las polis griegas. Sirve para entender por qué navegaban y por qué vivían en valles separados por montañas.",
    prior=["Sé el vocabulario del relieve y del agua.", "Sé qué es una polis."],
    explain=[
        "Grecia tiene una parte unida al continente europeo y muchas islas. Esa parte es una península. Hay archipiélagos, como los grupos de islas del mar Egeo. Al este está el mar Egeo, al oeste el mar Jónico y al sur el mar Mediterráneo.",
        "Gran parte de Grecia es montañosa. Hay valles, pero pocas llanuras anchas. En el norte está el monte Olimpo, donde, según los mitos, vivían los dioses. En el sur hay una península grande llamada el Peloponeso, donde estaban Esparta y Olimpia.",
        "Muchas polis estaban cerca del mar y tenían puerto, como Atenas. En Atenas hay un cerro llamado la Acrópolis, con templos como el Partenón. Las montañas separaban unas polis de otras, y por eso muchas se comunicaban mejor por mar que por tierra.",
    ],
    vocab=[("Peloponeso", "gran península del sur de Grecia"), ("mar Egeo", "mar al este de Grecia"), ("Acrópolis", "cerro de Atenas con templos"), ("llanura", "terreno plano y amplio"), ("monte Olimpo", "montaña del norte de Grecia, hogar de los dioses en los mitos")],
    worked=[
        {"title": "Describir con relieve", "problem": f"{E2} ¿Cómo es gran parte del territorio de Grecia?", "steps": ["Busco relieve.", "La ficha dice que es montañoso."], "answer": "Montañoso, con valles y pocas llanuras anchas"},
        {"title": "Usar el vocabulario", "problem": f"{E2} ¿Qué es el Peloponeso?", "steps": ["Busco Peloponeso.", "La ficha dice que es una península grande en el sur."], "answer": "Una península grande en el sur de Grecia"},
    ],
    mistakes=[
        {"wrong": "Decir que Grecia es una sola isla.", "why": "Se piensa que está rodeada de agua.", "fix": "Tiene una parte unida al continente europeo, que es una península, y muchas islas."},
        {"wrong": "Decir que Grecia es llana.", "why": "Se imagina un paisaje plano.", "fix": "Gran parte de Grecia es montañosa."},
    ],
    tiers={
        "recovery": [
            ex(f"{E2} ¿Qué mar está al este de Grecia?", "el mar Egeo", "La ficha lo dice."),
            ex(f"{E2} ¿Cómo es gran parte del territorio de Grecia?", "montañoso", "La ficha lo dice."),
            ex(f"{E2} ¿Cómo se llama la gran península del sur de Grecia?", "el Peloponeso", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{E2} ¿Qué es la Acrópolis?", "un cerro de Atenas con templos", "La ficha lo dice."),
            ex(f"{E2} ¿Qué es el monte Olimpo en los mitos?", "el hogar de los dioses", "La ficha lo dice."),
            ex(f"{E2} ¿Por qué muchas polis se comunicaban mejor por mar?", "porque las montañas las separaban por tierra", "La ficha lo explica."),
        ],
        "apply": [
            ex(f"{E2} ¿Cómo se llaman los grupos de islas del mar Egeo, según la ficha?", "archipiélagos", "La ficha los llama así."),
            ex(f"{E2} ¿En qué península estaban Esparta y Olimpia?", "en el Peloponeso", "La ficha lo dice."),
            ex(f"{E2} Une cada lugar con lo que es: A) Olimpo; B) Acrópolis; C) Peloponeso. 1) cerro con templos; 2) montaña de los dioses; 3) gran península.", "A con 2; B con 1; C con 3", "La ficha define cada uno."),
        ],
        "reason": [
            ex(f"{E2} Pedro dice que Grecia es un territorio plano como una gran llanura. Corrígelo.", "Gran parte es montañosa, con pocas llanuras anchas", "La ficha lo dice."),
            ex(f"{E2} ¿Por qué tenía sentido que muchas polis tuvieran puerto?", "porque estaban cerca del mar y se comunicaban por barco", "La ficha lo dice."),
        ],
        "challenge": [
            ex(f"{E2} Ordena los mares de este a oeste: Jónico, Egeo.", "Egeo, Jónico", "El Egeo está al este y el Jónico al oeste."),
            ex(f"{E2} Elige la descripción correcta de Atenas. A) Está cerca de la costa, con puerto y un cerro llamado Acrópolis. B) Está en medio de un desierto, lejos del mar.", "A", "La ficha la ubica cerca de la costa."),
        ],
    },
    context=[ex("Un turista visita las ruinas del Partenón y mira Atenas desde el cerro. ¿En qué cerro está?", "en la Acrópolis", "El Partenón está en la Acrópolis.")],
    selfcheck=[
        ex("¿Qué tiene Grecia además de una parte en el continente?", "muchas islas", "La ficha nombra sus archipiélagos."),
        ex("¿Cómo es gran parte de su relieve?", "montañoso", "Con pocas llanuras anchas."),
        ex("¿Qué mar está al este?", "el mar Egeo", "La ficha lo dice."),
    ],
    open_task=task(
        f"Dibuja un mapa simple de Grecia: una península con montañas, el Peloponeso al sur, islas al este, y tres mares rotulados: Egeo, Jónico y Mediterráneo. Marca Atenas con su Acrópolis. {E2}",
        "Península con montañas dibujadas, Peloponeso al sur, islas al este. Mar Egeo al este, Jónico al oeste, Mediterráneo al sur. Atenas cerca de la costa con la Acrópolis.",
        ["península con islas", "Peloponeso al sur", "tres mares bien ubicados", "Atenas en la costa"], ["mapa rotulado"], ["poner el Egeo al oeste", "dibujar solo una isla"],
        "Pregunta qué efecto tienen las montañas en la comunicación."),
    reinforce="Repite en voz alta cómo es el entorno geográfico de Grecia con tres palabras de la clase.",
    extend="Imagina que vives en una polis separada por montañas. Escribe cómo viajarías a otra.",
)

# ---------------------------------------------------------------- clase 3
E3 = ("Ficha de la península itálica y Roma. Italia está en una península larga en el sur de Europa, con forma de bota. Está rodeada por el mar Tirreno al oeste, el mar Adriático al este y el mar Jónico al sur. "
      "Al norte están los Alpes, montañas muy altas. Una cadena de montañas llamada los Apeninos recorre la península de norte a sur. "
      "Cerca de la península hay islas grandes, como Sicilia al sur y Cerdeña al oeste. "
      "Roma está en el centro-oeste de la península, junto al río Tíber y no muy lejos del mar Tirreno. Se cuenta que fue construida sobre siete colinas. "
      "En Roma hay construcciones y monumentos antiguos, como el Coliseo, el Foro y el Panteón.")
register(
    OA9, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo es el entorno geográfico de la península itálica y de Roma. Sirve para entender por qué Roma pudo comunicarse por mar y por tierra.",
    prior=["Sé el vocabulario del relieve y del agua.", "Sé dónde estaba Roma."],
    explain=[
        "Italia está en una península larga, con forma de bota, en el sur de Europa. Está rodeada por el mar Tirreno al oeste, el mar Adriático al este y el mar Jónico al sur. Al norte están los Alpes, montañas muy altas. Los Apeninos son una cadena de montañas que recorre la península de norte a sur.",
        "Cerca de la península hay islas grandes, como Sicilia al sur y Cerdeña al oeste. Roma está en el centro-oeste de la península, junto al río Tíber y no muy lejos del mar Tirreno. Se cuenta que fue construida sobre siete colinas.",
        "En Roma quedan construcciones y monumentos antiguos, como el Coliseo, el Foro y el Panteón. La ciudad estaba cerca del mar y junto a un río, lo que ayudaba a comunicarse con otros lugares. Desde esa posición, Roma llegó a controlar tierras alrededor del Mediterráneo.",
    ],
    vocab=[("Alpes", "montañas muy altas al norte de Italia"), ("Apeninos", "cadena de montañas que recorre la península itálica"), ("Tíber", "río junto al cual está Roma"), ("colina", "elevación del terreno más baja que una montaña"), ("Sicilia", "gran isla al sur de la península itálica")],
    worked=[
        {"title": "Ubicar Roma", "problem": f"{E3} ¿Dónde está Roma, respecto de la península itálica?", "steps": ["Busco Roma.", "La ficha dice que está en el centro-oeste, junto al río Tíber."], "answer": "En el centro-oeste, junto al río Tíber"},
        {"title": "Mares", "problem": f"{E3} ¿Qué mar está al oeste de Italia?", "steps": ["Busco al oeste.", "La ficha dice mar Tirreno."], "answer": "El mar Tirreno"},
    ],
    mistakes=[
        {"wrong": "Decir que Italia es una isla.", "why": "Se piensa que está rodeada de agua.", "fix": "Es una península, unida al resto de Europa por el norte."},
        {"wrong": "Mezclar los Alpes con los Apeninos.", "why": "Ambos son montañas.", "fix": "Los Alpes están al norte y los Apeninos recorren la península."},
    ],
    tiers={
        "recovery": [
            ex(f"{E3} ¿Qué forma tiene la península itálica?", "de bota", "La ficha lo dice."),
            ex(f"{E3} ¿Qué río pasa por Roma?", "el Tíber", "La ficha lo dice."),
            ex(f"{E3} ¿Qué montañas están al norte de Italia?", "los Alpes", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{E3} ¿Qué mar está al este de la península?", "el mar Adriático", "La ficha lo dice."),
            ex(f"{E3} ¿Qué recorre la península de norte a sur?", "los Apeninos", "Son una cadena de montañas."),
            ex(f"{E3} ¿Qué son Sicilia y Cerdeña?", "islas grandes cerca de la península", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{E3} Un barco sale de Roma hacia el oeste. ¿Qué mar encuentra primero?", "el mar Tirreno", "Está al oeste de la península."),
            ex(f"{E3} ¿En qué ciudad están el Coliseo, el Foro y el Panteón?", "en Roma", "La ficha los nombra como construcciones de Roma."),
            ex(f"{E3} ¿Qué isla está al sur de la península itálica?", "Sicilia", "La ficha lo dice."),
        ],
        "reason": [
            ex(f"{E3} Ema dice que Roma estaba lejos del mar y de todo río. Corrígela.", "Estaba junto al Tíber y no muy lejos del mar Tirreno", "La ficha lo dice."),
            ex(f"{E3} ¿Por qué ayudaba a Roma estar cerca de un río y del mar?", "porque se podía comunicar por agua con otros lugares", "Facilitaba el transporte."),
        ],
        "challenge": [
            ex(f"{E3} Compara el relieve de Grecia y el de Italia en una oración.", "Las dos son penínsulas con montañas y mares alrededor", "Las fichas de ambas lo muestran."),
            ex(f"{E3} Ordena de oeste a este los mares que rodean Italia: Adriático, Tirreno.", "Tirreno, Adriático", "El Tirreno está al oeste y el Adriático al este."),
        ],
    },
    context=[ex("Un turista visita un gran anfiteatro antiguo en Roma. ¿Cómo se llama?", "el Coliseo", "Es el gran anfiteatro de Roma.")],
    selfcheck=[
        ex("¿Qué es la península itálica?", "una península con forma de bota en el sur de Europa", "Está rodeada de mares."),
        ex("¿Dónde está Roma?", "en el centro-oeste, junto al Tíber", "Cerca del mar Tirreno."),
        ex("¿Qué montañas recorren la península?", "los Apeninos", "Van de norte a sur."),
    ],
    open_task=task(
        f"Dibuja la península itálica con forma de bota. Marca los mares Tirreno, Adriático y Jónico, los Alpes al norte, los Apeninos en el medio, las islas de Sicilia y Cerdeña, y Roma junto al río Tíber. {E3}",
        "Bota con el Tirreno a la izquierda, el Adriático a la derecha y el Jónico abajo. Alpes arriba, Apeninos en el centro, Sicilia abajo, Cerdeña a la izquierda. Roma en el centro-oeste con un río.",
        ["bota dibujada", "tres mares bien ubicados", "dos cadenas de montañas", "Roma junto al río"], ["mapa rotulado"], ["poner Roma en el este", "confundir Alpes y Apeninos"],
        "Pregunta qué ventajas tenía Roma por su ubicación."),
    reinforce="Repite en voz alta los tres mares y las dos cadenas de montañas de Italia.",
    extend="Compara en una frase la ubicación de Roma y la de Atenas respecto del mar.",
)

# ---------------------------------------------------------------- clase 4
E4 = ("Ficha para caracterizar un entorno. Una caracterización geográfica tiene cuatro partes: (1) ubicación: continente y mar o océano cercanos; (2) relieve: montañas, valles, penínsulas e islas; (3) agua: ríos, mares y océanos; (4) ciudad y construcciones: ciudades, puertos y monumentos. "
      "Modelo sobre Atenas: «Atenas está en Grecia, en el sur de Europa, cerca del mar Egeo. Grecia es una península montañosa con muchas islas. Atenas está cerca de la costa y tiene puerto. Tiene un cerro, la Acrópolis, con un templo, el Partenón.» "
      "Datos de Roma para completar: península itálica, sur de Europa; Apeninos y Alpes; río Tíber y mar Tirreno; Coliseo, Foro y Panteón.")
register(
    OA9, 4,
    materials="Lápiz y papel. La ficha con el modelo y los datos de Roma está escrita en cada ejercicio.",
    use="Aprenderé a escribir una descripción ordenada del entorno de una ciudad antigua usando el vocabulario geográfico. Sirve para comunicar lo que aprendí con precisión.",
    prior=["Sé el vocabulario del relieve y del agua.", "Sé el entorno de Grecia y de Roma."],
    explain=[
        "Caracterizar un entorno es describirlo ordenadamente. Una buena caracterización tiene cuatro partes. La ubicación dice en qué continente y cerca de qué mar o río está. El relieve dice si hay montañas, valles, penínsulas o islas. El agua nombra ríos, mares u océanos. La ciudad y las construcciones nombran puertos, templos o monumentos.",
        "Usamos el vocabulario geográfico con cuidado. Una península no es una isla. Un archipiélago es un grupo de islas. Un valle no es una montaña. Si usamos mal una palabra, el lector entiende otra cosa.",
        "Un modelo sobre Atenas dice: «Atenas está en Grecia, en el sur de Europa, cerca del mar Egeo. Grecia es una península montañosa con muchas islas. Atenas está cerca de la costa y tiene puerto. Tiene un cerro, la Acrópolis, con un templo, el Partenón». Con ese orden puedes describir también a Roma.",
    ],
    vocab=[("caracterizar", "describir cómo es un lugar de forma ordenada"), ("ubicación", "lugar donde está algo"), ("relieve", "formas de la tierra: montañas, valles y otras"), ("vocabulario geográfico", "palabras para describir lugares, como península o valle"), ("construcción", "obra hecha por las personas")],
    worked=[
        {"title": "Identificar las partes", "problem": f"{E4} En el modelo de Atenas, ¿qué parte es «Atenas está en Grecia, en el sur de Europa»?", "steps": ["Dice dónde está.", "Eso es la ubicación."], "answer": "La ubicación"},
        {"title": "Completar con datos", "problem": f"{E4} Escribe la parte de agua de Roma con los datos.", "steps": ["Datos de agua: río Tíber y mar Tirreno.", "Escribo una oración con ellos."], "answer": "Roma está junto al río Tíber y no muy lejos del mar Tirreno"},
    ],
    mistakes=[
        {"wrong": "Usar mal una palabra, como llamar isla a una península.", "why": "Se parecen.", "fix": "Revisa la definición: la península está rodeada de agua por casi todos lados."},
        {"wrong": "Mezclar las partes sin orden.", "why": "Se escribe lo primero que se recuerda.", "fix": "Sigue el orden: ubicación, relieve, agua, ciudad."},
    ],
    tiers={
        "recovery": [
            ex(f"{E4} ¿Cuántas partes tiene una caracterización?", "4", "La ficha enumera cuatro."),
            ex(f"{E4} ¿Qué parte nombra los ríos, mares y océanos?", "el agua", "Así lo dice la ficha."),
            ex(f"{E4} ¿Qué parte dice en qué continente está?", "la ubicación", "Así lo dice la ficha."),
        ],
        "understand": [
            ex(f"{E4} ¿Qué parte nombra montañas, valles, penínsulas e islas?", "el relieve", "Así lo dice la ficha."),
            ex(f"{E4} ¿Qué parte nombra puertos y monumentos?", "la ciudad y las construcciones", "Así lo dice la ficha."),
            ex(f"{E4} En el modelo de Atenas, ¿qué construcción se nombra?", "el Partenón", "Aparece en la última oración."),
        ],
        "apply": [
            ex(f"{E4} Con los datos de Roma, escribe la parte de relieve: elige. A) Roma está en una península que tiene los Apeninos y, al norte, los Alpes. B) Roma está en una isla sin montañas.", "A", "La ficha da esos datos."),
            ex(f"{E4} Elige la oración correcta sobre construcciones de Roma. A) En Roma hay monumentos como el Coliseo, el Foro y el Panteón. B) En Roma está el templo llamado Partenón.", "A", "El Partenón está en Atenas."),
            ex(f"{E4} Ordena las partes de la caracterización: agua, ubicación, ciudad, relieve.", "ubicación, relieve, agua, ciudad", "Es el orden de la ficha."),
        ],
        "reason": [
            ex(f"{E4} Luis escribió: «Roma está en una isla rodeada de mar». Corrígelo con la ficha.", "Roma está en una península, no en una isla", "La ficha dice que está en la península itálica."),
            ex(f"{E4} Ana dice que un valle es una montaña muy alta. ¿Tiene razón?", "No, el valle es una zona baja entre montañas", "La montaña es una elevación."),
        ],
        "challenge": [
            ex(f"{E4} Escribe la ubicación de Roma en una oración.", "Roma está en la península itálica, en el sur de Europa", "La ficha da esos datos."),
            ex(f"{E4} Compara en una oración el entorno de Atenas y el de Roma.", "Los dos están en penínsulas del sur de Europa, cerca del mar, con montañas", "Las fichas de ambas lo muestran."),
        ],
    },
    context=[ex("Un guía dice: «Roma está en una isla en el océano Pacífico». ¿Qué parte del dato es incorrecta, y cómo se corrige?", "isla y océano Pacífico; es una península junto al mar Tirreno", "Los datos de la ficha dicen otra cosa.")],
    selfcheck=[
        ex("¿Qué cuatro partes tiene una caracterización?", "ubicación, relieve, agua y ciudad y construcciones", "Son las de la ficha."),
        ex("¿Qué es una península?", "una tierra rodeada de agua por casi todos lados", "No es una isla."),
        ex("¿Qué parte nombra el río Tíber?", "el agua", "Es un río."),
    ],
    open_task=task(
        f"Escribe una caracterización de Roma con las cuatro partes, en cuatro oraciones. Usa los datos de la ficha y al menos cinco palabras del vocabulario geográfico. {E4}",
        "Roma está en la península itálica, en el sur de Europa. La península tiene montañas: los Apeninos y, al norte, los Alpes. Roma está junto al río Tíber y no muy lejos del mar Tirreno. Tiene construcciones antiguas, como el Coliseo, el Foro y el Panteón.",
        ["cuatro partes en orden", "cinco palabras del vocabulario", "datos correctos"], ["texto de cuatro oraciones"], ["inventar datos", "usar mal una palabra"],
        "Pregunta qué palabra del vocabulario le costó más."),
    reinforce="Lee tu caracterización en voz alta y revisa si están las cuatro partes.",
    extend="Haz una caracterización de tu ciudad con las cuatro partes.",
)

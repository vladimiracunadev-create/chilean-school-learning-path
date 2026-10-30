"""Material del estudiante de 2.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (ubicación de Chile y Sudamérica) y OA 08 (paisajes de las zonas norte, centro y sur)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA7, OA8 = "HI02 OA 07", "HI02 OA 08"

# ================================================================ OA 07
G1 = ("Ficha de globo y mapa (dada por la clase): el globo terráqueo es una esfera, como una pelota, y muestra la Tierra con sus formas parecidas a las reales. El mapa es plano y cabe en una hoja, pero estira o achica algunas partes. "
      "Sudamérica es un continente casi todo en el hemisferio sur. Chile es una franja larga y angosta en el lado oeste de Sudamérica, junto al océano Pacífico, con la cordillera de los Andes al este.")
register(
    OA7, 1,
    materials="Lápiz y papel. La ficha de globo y mapa está escrita en cada ejercicio. Un globo terráqueo o mapa de la escuela ayuda, pero no es necesario.",
    use="Aprenderé a reconocer Sudamérica y Chile en un globo y en un mapa. Sirve para saber dónde vivimos en el mundo.",
    prior=["Sé qué es un continente.", "Sé que hay norte, sur, este y oeste."],
    explain=[
        "La Tierra es redonda. El globo terráqueo es una esfera que la representa y se parece mucho a su forma real. El mapa representa la Tierra en una hoja plana. Es más fácil de llevar, pero al aplanar la forma, algunas partes se ven más grandes o más chicas de lo que son.",
        "Sudamérica es un continente que está casi todo en el hemisferio sur. Chile está en el lado oeste de Sudamérica, junto al océano Pacífico. Tiene forma de franja larga y angosta, y al este tiene la cordillera de los Andes.",
        "En un mapa, el norte suele estar arriba y el sur abajo, el este a la derecha y el oeste a la izquierda. En el globo no hay arriba ni abajo fijos, así que usamos los puntos cardinales y los referentes, como los océanos y los continentes, para orientarnos.",
    ],
    vocab=[("globo terráqueo", "esfera que representa la Tierra"), ("mapa", "dibujo plano de un lugar"), ("continente", "gran extensión de tierra rodeada de mares"), ("océano Pacífico", "gran mar que baña la costa de Chile"), ("hemisferio sur", "mitad de la Tierra que está al sur del ecuador")],
    worked=[
        {"title": "Ubicar Chile", "problem": f"{G1} ¿En qué lado de Sudamérica está Chile?", "steps": ["Leo la ficha.", "Dice: en el lado oeste, junto al océano Pacífico."], "answer": "En el lado oeste"},
        {"title": "Globo o mapa", "problem": f"{G1} ¿Qué representación se parece más a la forma real de la Tierra?", "steps": ["El globo es una esfera.", "El mapa es plano y estira algunas partes."], "answer": "El globo"},
    ],
    mistakes=[
        {"wrong": "Pensar que en el mapa todos los países tienen su tamaño real.", "why": "Al aplanar, el mapa estira algunas partes.", "fix": "Recuerda que el globo se parece más a la forma real."},
        {"wrong": "Decir que Chile está al este de Sudamérica.", "why": "Se confunden los lados.", "fix": "Chile está en el oeste, junto al océano Pacífico."},
    ],
    tiers={
        "recovery": [
            ex(f"{G1} ¿Qué forma tiene el globo terráqueo?", "esfera", "La ficha lo dice."),
            ex(f"{G1} ¿Qué océano está junto a Chile?", "el océano Pacífico", "La ficha lo dice."),
            ex("Un mapa, ¿es plano o redondo?", "plano", "Se dibuja en una hoja."),
        ],
        "understand": [
            ex(f"{G1} ¿Qué cordillera está al este de Chile?", "la cordillera de los Andes", "La ficha lo dice."),
            ex(f"{G1} ¿Por qué un mapa puede mostrar partes más grandes o más chicas?", "Porque al aplanar la Tierra se estiran algunas partes", "Así lo explica la ficha."),
            ex(f"{G1} ¿En qué hemisferio está casi todo Sudamérica?", "en el hemisferio sur", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{G1} Describe la forma de Chile.", "una franja larga y angosta", "La ficha lo indica."),
            ex("En un mapa con el norte arriba, ¿dónde queda el sur?", "abajo", "Sur es el opuesto al norte."),
            ex("En un mapa con el norte arriba, ¿dónde queda el oeste?", "a la izquierda", "El este está a la derecha."),
        ],
        "reason": [
            ex("Una niña dice: «En el mapa mi país se ve del mismo tamaño que en el globo». ¿Qué debes recordar?", "Que el mapa puede cambiar los tamaños", "El mapa estira algunas partes."),
            ex(f"{G1} ¿Qué ventaja tiene un mapa sobre un globo?", "Es plano y cabe en una hoja", "Es fácil de llevar."),
        ],
        "challenge": [
            ex(f"{G1} Escribe una frase que ubique a Chile usando el océano y la cordillera.", "Chile está entre el océano Pacífico y la cordillera de los Andes", "Usa los dos referentes."),
            ex("Si un mapa tiene el norte arriba, ¿hacia dónde está el océano Pacífico respecto de Chile?", "a la izquierda, al oeste", "Chile está en el oeste de Sudamérica."),
        ],
    },
    context=[ex("Camilo mira un globo y quiere mostrarle a su hermana dónde está Chile. ¿Qué dos referentes puede nombrar: el océano Pacífico y la cordillera de los Andes, o el desierto y la selva?", "el océano Pacífico y la cordillera de los Andes", "Esos son los referentes que ubican a Chile en la ficha.")],
    selfcheck=[
        ex("¿El globo terráqueo es plano o una esfera?", "una esfera", "Representa la Tierra redonda."),
        ex(f"{G1} ¿En qué lado de Sudamérica está Chile?", "en el oeste", "La ficha lo dice."),
        ex("¿Qué es un continente?", "una gran extensión de tierra rodeada de mares", "Sudamérica es uno."),
    ],
    open_task=task(
        f"Dibuja un mapa muy simple de Sudamérica como un triángulo grande y marca con una franja larga y angosta el lado oeste donde está Chile. {G1} Escribe el nombre del océano junto a Chile y la cordillera al este de Chile.",
        "Un triángulo grande. En el lado izquierdo, una franja larga que dice Chile. A la izquierda de la franja, océano Pacífico. A la derecha de la franja, cordillera de los Andes.",
        ["franja de Chile en el oeste", "océano a la izquierda", "cordillera a la derecha"], ["mapa dibujado"], ["poner Chile en el este", "olvidar la cordillera o el océano"],
        "Pregunta por qué usó esa forma. Debe mencionar que Chile es largo y angosto."),
    reinforce="Mira un globo o un mapa y señala con el dedo dónde está Chile.",
    extend="Escribe una diferencia entre un globo y un mapa en una oración.",
)

C2 = ("Tabla de regiones y capitales regionales (dada por la clase): Arica y Parinacota, Arica; Tarapacá, Iquique; Antofagasta, Antofagasta; Atacama, Copiapó; Coquimbo, La Serena; Valparaíso, Valparaíso; Metropolitana, Santiago; "
      "O'Higgins, Rancagua; Maule, Talca; Ñuble, Chillán; Biobío, Concepción; La Araucanía, Temuco; Los Ríos, Valdivia; Los Lagos, Puerto Montt; Aysén, Coyhaique; Magallanes, Punta Arenas. "
      "Santiago es la capital de Chile.")
register(
    OA7, 2,
    materials="Lápiz y papel. La tabla de regiones y capitales está escrita en cada ejercicio.",
    use="Aprenderé a distinguir país, región, capital nacional y capital regional. Sirve para ubicar mi ciudad dentro de Chile y de Sudamérica.",
    prior=["Sé que Chile es un país de Sudamérica.", "Sé que hay norte, centro y sur."],
    explain=[
        "Chile es un país. Está dividido en 16 regiones. Cada región tiene una ciudad principal para su administración, que se llama capital regional. La capital de todo el país, que se llama capital nacional, es Santiago.",
        "Para ubicar un lugar podemos ir de lo grande a lo pequeño: continente, país, región y ciudad o localidad. Por ejemplo: Sudamérica, Chile, la región de Los Lagos y la ciudad de Puerto Montt. Es una secuencia que va de más grande a más chico.",
        "Cuidado: la capital de un país no es igual a la capital de una región. Santiago es la capital de Chile y también la capital de la Región Metropolitana. Valparaíso es la capital de la región de Valparaíso. La ciudad donde vives puede o no ser una capital regional.",
    ],
    vocab=[("región", "parte del país con su propia capital regional"), ("capital nacional", "ciudad donde está el gobierno del país"), ("capital regional", "ciudad principal de una región"), ("localidad", "lugar donde vive la gente, como un pueblo o una ciudad"), ("secuencia", "cosas puestas una después de otra en orden")],
    worked=[
        {"title": "Capital regional", "problem": f"{C2} ¿Cuál es la capital de la región de Coquimbo?", "steps": ["Busco Coquimbo en la tabla.", "Dice La Serena."], "answer": "La Serena"},
        {"title": "Secuencia espacial", "problem": f"{C2} Ordena de más grande a más pequeño: Chile, Temuco, La Araucanía, Sudamérica.", "steps": ["Sudamérica es el continente.", "Chile es el país, La Araucanía es la región y Temuco es la ciudad."], "answer": "Sudamérica, Chile, La Araucanía, Temuco"},
    ],
    mistakes=[
        {"wrong": "Decir que Santiago es la capital de todas las regiones.", "why": "Se confunde capital nacional con capital regional.", "fix": "Cada región tiene su capital regional; Santiago es la capital nacional."},
        {"wrong": "Confundir región con ciudad.", "why": "Algunas regiones y su capital tienen el mismo nombre.", "fix": "La región es el territorio grande y la capital es una ciudad dentro de ella."},
    ],
    tiers={
        "recovery": [
            ex(f"{C2} ¿Cuál es la capital de Chile?", "Santiago", "La tabla lo dice."),
            ex(f"{C2} ¿Cuál es la capital de la región de Los Lagos?", "Puerto Montt", "La tabla lo dice."),
            ex(f"{C2} ¿Cuál es la capital de la región de Magallanes?", "Punta Arenas", "La tabla lo dice."),
        ],
        "understand": [
            ex("¿Cuántas regiones tiene Chile?", "16", "La clase lo explica."),
            ex("¿Qué es una capital regional?", "la ciudad principal de una región", "Esa es su definición."),
            ex(f"{C2} ¿En qué región está Temuco?", "La Araucanía", "La tabla lo dice."),
        ],
        "apply": [
            ex(f"{C2} Une: 1) Rancagua, 2) Iquique. A) Tarapacá, B) O'Higgins.", "1 con B; 2 con A", "La tabla une cada capital con su región."),
            ex(f"{C2} Ordena de más grande a más pequeño: Concepción, Biobío, Chile, Sudamérica.", "Sudamérica, Chile, Biobío, Concepción", "Es la secuencia continente, país, región, ciudad."),
            ex(f"{C2} ¿Cuál es la capital de Atacama?", "Copiapó", "La tabla lo dice."),
        ],
        "reason": [
            ex("Una niña dice: «La capital de la región de Valparaíso es Santiago». ¿Qué error tiene?", "La capital de esa región es Valparaíso; Santiago es la capital del país", "Mezcla capital nacional y regional."),
            ex("¿Por qué una ciudad pequeña puede estar en una región sin ser su capital?", "Porque cada región tiene muchas ciudades y una sola es la capital regional", "Una región contiene varias ciudades."),
        ],
        "challenge": [
            ex(f"{C2} Escribe la secuencia desde Sudamérica hasta Punta Arenas.", "Sudamérica, Chile, Magallanes, Punta Arenas", "Va de continente a ciudad."),
            ex(f"{C2} ¿Cuántas capitales regionales aparecen en la tabla?", "16", "Hay una por región y hay 16 regiones."),
        ],
    },
    context=[ex("Un niño de Chillán dice: «Vivo en la capital de Ñuble». ¿Tiene razón según la tabla?", "sí", "Chillán es la capital de la región de Ñuble.")],
    selfcheck=[
        ex(f"{C2} ¿Cuál es la capital de La Araucanía?", "Temuco", "La tabla lo dice."),
        ex("¿Santiago es la capital de Chile?", "sí", "Es la capital nacional."),
        ex("¿Una región tiene una sola ciudad?", "no", "Tiene varias ciudades y localidades."),
    ],
    open_task=task(
        f"Elige una región de la tabla y escribe la secuencia desde Sudamérica hasta su capital regional. Después marca un punto en un dibujo de Chile para mostrar si está al norte, al centro o al sur. {C2}",
        "Secuencia: Sudamérica, Chile, región de Los Lagos, Puerto Montt. Está en el sur de Chile.",
        ["secuencia en orden", "capital regional correcta", "zona del país marcada"], ["secuencia escrita", "dibujo de Chile"], ["poner la ciudad antes de la región", "confundir capital nacional con regional"],
        "Pide que diga qué parte de la secuencia es la más grande y cuál la más chica."),
    reinforce="Di en voz alta la capital de Chile y la capital de tres regiones de la tabla.",
    extend="Escribe una pregunta sobre la región donde vives que puedas investigar con un adulto.",
)

L3 = ("Ficha de países vecinos (dada por la clase): al norte de Chile está Perú. Al noreste de Chile está Bolivia. Al este de Chile está Argentina. Al oeste de Chile está el océano Pacífico. "
      "Rosa de los vientos: norte (N) arriba, sur (S) abajo, este (E) a la derecha, oeste (O) a la izquierda, noreste (NE) entre el norte y el este, suroeste (SO) entre el sur y el oeste.")
register(
    OA7, 3,
    materials="Lápiz y papel. La ficha de países vecinos y la rosa de los vientos están escritas en cada ejercicio.",
    use="Aprenderé a describir dónde están los países vecinos de Chile con los puntos cardinales. Sirve para orientarme en un mapa de Sudamérica.",
    prior=["Sé ubicar Chile en Sudamérica.", "Sé qué son norte, sur, este y oeste."],
    explain=[
        "Los puntos cardinales son norte, sur, este y oeste. La rosa de los vientos los muestra en un dibujo con forma de estrella. Entre el norte y el este está el noreste. Entre el sur y el oeste está el suroeste. Con los puntos cardinales podemos decir dónde queda un país respecto de otro.",
        "Chile tiene tres países limítrofes, es decir, países con los que comparte frontera. Al norte está Perú. Al noreste está Bolivia. Al este está Argentina. Al oeste, Chile no tiene un país vecino, sino el océano Pacífico.",
        "Para describir la ubicación relativa, elegimos un país como referencia. Por ejemplo, «Argentina está al este de Chile». Si cambiamos el país de referencia, cambia la frase: «Chile está al oeste de Argentina». Siempre hay que decir respecto de qué país hablamos.",
    ],
    vocab=[("punto cardinal", "norte, sur, este u oeste"), ("limítrofe", "que comparte frontera con otro"), ("frontera", "línea que separa dos países"), ("rosa de los vientos", "dibujo que muestra los puntos cardinales"), ("ubicación relativa", "dónde está algo respecto de otra cosa")],
    worked=[
        {"title": "Describir un vecino", "problem": f"{L3} ¿Dónde queda Perú respecto de Chile?", "steps": ["Busco Perú en la ficha.", "Dice: al norte de Chile."], "answer": "Al norte"},
        {"title": "Cambiar la referencia", "problem": f"{L3} ¿Dónde queda Chile respecto de Argentina?", "steps": ["Argentina está al este de Chile.", "Entonces Chile está al otro lado, al oeste de Argentina."], "answer": "Al oeste"},
    ],
    mistakes=[
        {"wrong": "Decir que Bolivia está al sur de Chile.", "why": "Se confunden los puntos cardinales.", "fix": "Mira la rosa de los vientos: Bolivia está al noreste."},
        {"wrong": "Decir «Perú está al norte» sin decir de qué país.", "why": "Falta la referencia.", "fix": "Di «Perú está al norte de Chile»."},
    ],
    tiers={
        "recovery": [
            ex(f"{L3} ¿Qué país está al este de Chile?", "Argentina", "La ficha lo dice."),
            ex(f"{L3} ¿Qué país está al norte de Chile?", "Perú", "La ficha lo dice."),
            ex(f"{L3} ¿Qué hay al oeste de Chile?", "el océano Pacífico", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{L3} ¿Qué país está al noreste de Chile?", "Bolivia", "La ficha lo dice."),
            ex("¿Qué significa limítrofe?", "que comparte frontera con otro", "Esa es su definición."),
            ex(f"{L3} ¿Entre qué dos puntos cardinales está el noreste?", "entre el norte y el este", "La rosa de los vientos lo muestra."),
        ],
        "apply": [
            ex(f"{L3} ¿Dónde queda Chile respecto de Perú?", "al sur", "Perú está al norte de Chile."),
            ex(f"{L3} ¿Dónde queda Chile respecto de Bolivia?", "al suroeste", "Bolivia está al noreste de Chile, así que Chile queda al lado opuesto."),
            ex(f"{L3} Une: 1) Perú, 2) Argentina. A) este, B) norte.", "1 con B; 2 con A", "Perú está al norte y Argentina al este."),
        ],
        "reason": [
            ex("Un niño dice: «Argentina está al oeste de Chile». ¿Qué error tiene?", "Está al este; al oeste está el océano Pacífico", "Confundió el este con el oeste."),
            ex(f"{L3} ¿Por qué hay que decir «respecto de Chile» al ubicar un país?", "Porque la ubicación cambia según el país de referencia", "Cambiar la referencia cambia la frase."),
        ],
        "challenge": [
            ex(f"{L3} Cuenta los países limítrofes de Chile.", "3", "Perú, Bolivia y Argentina."),
            ex(f"{L3} Escribe una frase que ubique a Bolivia usando noreste y a Argentina usando este.", "Bolivia está al noreste de Chile y Argentina está al este de Chile", "Usa los puntos cardinales correctos."),
        ],
    },
    context=[ex("Un viajero sale de Chile hacia el este y cruza la cordillera de los Andes. ¿A qué país llega: Perú o Argentina?", "Argentina", "Argentina está al este de Chile.")],
    selfcheck=[
        ex(f"{L3} ¿Qué país queda al norte de Chile?", "Perú", "La ficha lo dice."),
        ex("¿Cuántos países limítrofes tiene Chile?", "3", "Perú, Bolivia y Argentina."),
        ex("¿Qué dibujo muestra los puntos cardinales?", "la rosa de los vientos", "Muestra norte, sur, este y oeste."),
    ],
    open_task=task(
        f"Dibuja una rosa de los vientos con N, S, E y O. Coloca en el centro la palabra Chile y escribe en cada lado el nombre del vecino. {L3}",
        "Centro: Chile. Arriba (N): Perú. Entre N y E (NE): Bolivia. A la derecha (E): Argentina. A la izquierda (O): océano Pacífico.",
        ["rosa dibujada", "tres vecinos ubicados", "océano al oeste"], ["dibujo"], ["poner a Argentina al oeste", "olvidar el noreste"],
        "Pide que lea una frase completa: «___ está al ___ de Chile»."),
    reinforce="Señala en el mapa de tu escuela cada vecino de Chile y di su punto cardinal.",
    extend="Escribe una frase que ubique a Chile respecto de cada vecino.",
)

O4 = ("Pistas de países sudamericanos (dadas por la clase): Ecuador está al norte de Perú. Colombia está al norte de Ecuador. Brasil está al este de Perú y de Bolivia. Venezuela está al norte de Brasil. "
      "Paraguay está al este de Bolivia y al norte de Argentina. Uruguay está al este de Argentina. Chile está al oeste de Argentina.")
register(
    OA7, 4,
    materials="Lápiz y papel. Las pistas de ubicación están escritas en cada ejercicio.",
    use="Aprenderé a ubicar otros países de Sudamérica usando pistas y puntos cardinales. Sirve para no memorizar una lista sino entender cómo se relacionan los países.",
    prior=["Sé qué son los países limítrofes de Chile.", "Sé usar norte, sur, este y oeste."],
    explain=[
        "Sudamérica tiene doce países independientes, entre ellos Chile. No hace falta memorizar una lista aislada. Es mejor entender cómo se relacionan entre sí con los puntos cardinales: un país está al norte, al sur, al este o al oeste de otro.",
        "Las pistas sirven para descubrir un país. Por ejemplo, Ecuador está al norte de Perú, y Colombia está al norte de Ecuador. Brasil está al este de Perú y de Bolivia. Venezuela está al norte de Brasil. Paraguay está al este de Bolivia y al norte de Argentina. Uruguay está al este de Argentina.",
        "Para resolver una pista, usamos una o dos referencias a la vez. Si un país está al este de Argentina y al sur de Brasil, buscamos el que cumple las dos. Luego comprobamos en un mapa. Una pista sola puede servir a más de un país.",
    ],
    vocab=[("pista", "dato que ayuda a descubrir algo"), ("referencia", "lugar conocido desde el cual ubicamos otro"), ("país independiente", "país que se gobierna a sí mismo"), ("comprobar", "mirar si algo es verdadero"), ("relación espacial", "cómo se ubican dos lugares uno respecto del otro")],
    worked=[
        {"title": "Una pista", "problem": f"{O4} Un país está al norte de Perú. ¿Cuál es?", "steps": ["Busco la pista.", "Dice: Ecuador está al norte de Perú."], "answer": "Ecuador"},
        {"title": "Dos pistas", "problem": f"{O4} Un país está al este de Bolivia y al norte de Argentina. ¿Cuál es?", "steps": ["Busco Bolivia y Argentina en las pistas.", "Paraguay cumple las dos."], "answer": "Paraguay"},
    ],
    mistakes=[
        {"wrong": "Aprender los países solo como una lista.", "why": "No se entiende dónde están unos respecto de otros.", "fix": "Usa pistas con puntos cardinales."},
        {"wrong": "Responder con una sola pista cuando hay dos.", "why": "Una pista puede servir a más de un país.", "fix": "Revisa las dos pistas antes de responder."},
    ],
    tiers={
        "recovery": [
            ex(f"{O4} ¿Qué país está al norte de Ecuador?", "Colombia", "La pista lo dice."),
            ex(f"{O4} ¿Qué país está al norte de Brasil?", "Venezuela", "La pista lo dice."),
            ex(f"{O4} ¿Qué país está al este de Argentina?", "Uruguay", "La pista lo dice."),
        ],
        "understand": [
            ex(f"{O4} ¿Qué país está al este de Perú y de Bolivia?", "Brasil", "La pista lo dice."),
            ex(f"{O4} Además de Chile, ¿qué dos países se ubican en las pistas con Argentina como referencia?", "Paraguay y Uruguay", "Paraguay está al norte de Argentina y Uruguay está al este."),
            ex("¿Cuántos países independientes tiene Sudamérica?", "12", "Así lo explica la clase."),
        ],
        "apply": [
            ex(f"{O4} Está al norte de Perú y al sur de Colombia. ¿Qué país es?", "Ecuador", "Cumple las dos pistas."),
            ex(f"{O4} Está al este de Argentina. ¿Qué país es?", "Uruguay", "La pista lo indica."),
            ex(f"{O4} Está al este de Bolivia y al norte de Argentina. ¿Qué país es?", "Paraguay", "Cumple las dos pistas."),
        ],
        "reason": [
            ex("Un niño dice: «Brasil está al oeste de Perú». Usa las pistas para corregir.", "Brasil está al este de Perú", "Las pistas dicen este."),
            ex(f"{O4} ¿Por qué no basta la pista «está al norte de Argentina» para saber cuál país es?", "Porque más de un país puede estar al norte de Argentina", "Hace falta otra pista."),
        ],
        "challenge": [
            ex(f"{O4} Ordena de norte a sur: Perú, Colombia, Ecuador.", "Colombia, Ecuador, Perú", "Colombia está al norte de Ecuador y Ecuador al norte de Perú."),
            ex(f"{O4} Escribe una pista nueva usando Chile y Argentina.", "Chile está al oeste de Argentina", "Usa dos países con su punto cardinal."),
        ],
    },
    context=[ex("Una niña juega a adivinar: «Estoy al este de Chile, al sur de Bolivia y comparto frontera con Chile». Datos: Perú está al norte de Chile; Argentina está al este de Chile y al sur de Bolivia; Brasil está al este de Bolivia. ¿Qué país es: Perú, Argentina o Brasil?", "Argentina", "Es el único que cumple las tres pistas: está al este de Chile, al sur de Bolivia y es limítrofe.")],
    selfcheck=[
        ex(f"{O4} ¿Qué país está al norte de Perú?", "Ecuador", "La pista lo dice."),
        ex(f"{O4} ¿Chile está al este o al oeste de Argentina?", "al oeste", "La última pista lo dice."),
        ex("¿Se debe aprender los países solo como una lista?", "no", "Conviene entender cómo se relacionan."),
    ],
    open_task=task(
        f"Crea dos pistas para un compañero, con un punto cardinal cada una, sobre los países de la ficha. {O4} Escribe también la respuesta.",
        "Pista 1: Está al norte de Brasil. Respuesta: Venezuela. Pista 2: Está al este de Argentina. Respuesta: Uruguay.",
        ["dos pistas", "punto cardinal en cada una", "respuesta correcta"], ["pistas escritas"], ["usar un punto cardinal equivocado", "no escribir la respuesta"],
        "Pide que un compañero resuelva las pistas y diga si son claras."),
    reinforce="Elige un país de la ficha y di en voz alta dónde queda respecto de Chile o de otro país.",
    extend="Escribe una pista con dos referencias para un país de la ficha.",
)

# ================================================================ OA 08
PA1 = ("Descripciones de paisajes (dadas por la clase): Paisaje A: se ve el mar, una playa, cerros con poca vegetación, casas, calles y un muelle. "
       "Paisaje B: se ve un río, árboles, un puente, una ciudad con edificios y campos de cultivo a lo lejos. No se dice en qué zona del país están.")
register(
    OA8, 1,
    materials="Lápiz y papel. Las descripciones de los paisajes están escritas en cada ejercicio.",
    use="Aprenderé a leer un paisaje separando lo natural de lo que hacen las personas. Sirve para describirlo antes de decidir en qué zona está.",
    prior=["Sé qué es un río, un cerro y el mar.", "Sé que Chile tiene norte, centro y sur."],
    explain=[
        "Un paisaje es lo que se ve en un lugar. Tiene elementos naturales, que existen sin que los haga el ser humano, como el mar, los cerros, el río, la playa y los árboles. También tiene elementos humanos, que construyen o modifican las personas, como casas, calles, puentes, muelles y campos de cultivo.",
        "Para leer un paisaje, primero escribimos una lista de lo que vemos. Luego la dividimos en dos columnas: elementos naturales y elementos humanos. Así describimos sin adivinar. No debemos decir en qué zona de Chile está solo por un elemento, porque hay mares, cerros y ríos en todo el país.",
        "Algunas palabras geográficas ayudan a describir. Un océano es una gran extensión de agua salada. Un río es una corriente de agua que corre hacia el mar o hacia un lago. Una isla es tierra rodeada de agua. Una ciudad es un lugar grande, con muchas personas, edificios y calles. Un pueblo es un lugar más pequeño, con menos habitantes.",
        "Por ejemplo, el paisaje A tiene mar, playa y cerros como elementos naturales. Tiene casas, calles y un muelle como elementos humanos. El paisaje B tiene un río y árboles naturales, y un puente, una ciudad y campos de cultivo humanos.",
    ],
    vocab=[("paisaje", "lo que se ve en un lugar"), ("elemento natural", "algo que existe sin que lo haga el ser humano"), ("elemento humano", "algo que construyen o modifican las personas"), ("cultivo", "campo donde se siembran plantas"), ("muelle", "construcción junto al mar para que lleguen los barcos"), ("océano", "gran extensión de agua salada"), ("río", "corriente de agua que corre hacia el mar o hacia un lago"), ("isla", "tierra rodeada de agua"), ("ciudad", "lugar grande con muchas personas, edificios y calles"), ("pueblo", "lugar pequeño, con menos habitantes que una ciudad")],
    worked=[
        {"title": "Clasificar elementos", "problem": f"{PA1} Clasifica el muelle del paisaje A.", "steps": ["Un muelle lo construyen las personas.", "Es un elemento humano."], "answer": "Elemento humano"},
        {"title": "No adivinar la zona", "problem": f"{PA1} ¿Se puede saber en qué zona de Chile está el paisaje B?", "steps": ["La descripción no lo dice.", "Un río y una ciudad existen en muchas zonas."], "answer": "No; falta más información"},
    ],
    mistakes=[
        {"wrong": "Decir la zona del paisaje solo por ver el mar.", "why": "El mar está en toda la costa de Chile.", "fix": "Primero describe; para la zona usa más pistas."},
        {"wrong": "Poner los campos de cultivo como elemento natural.", "why": "Parecen parte de la naturaleza.", "fix": "Los campos de cultivo los hacen las personas."},
    ],
    tiers={
        "recovery": [
            ex(f"{PA1} ¿Qué elementos naturales tiene el paisaje A?", "mar, playa y cerros", "La descripción los nombra."),
            ex(f"{PA1} ¿Qué elementos humanos tiene el paisaje B?", "puente, ciudad y campos de cultivo", "Los construyen o modifican las personas."),
            ex("Una isla, ¿es tierra rodeada de agua o agua rodeada de tierra?", "tierra rodeada de agua", "Esa es la definición de isla."),
        ],
        "understand": [
            ex("Explica qué es un elemento humano.", "algo que construyen o modifican las personas", "Esa es su definición."),
            ex(f"{PA1} ¿Por qué no sabemos la zona del paisaje A?", "Porque hay mar y cerros en muchas zonas", "No hay una pista exclusiva de una zona."),
            ex("Una ciudad y un pueblo, ¿cuál tiene más habitantes y edificios?", "la ciudad", "Un pueblo es más pequeño que una ciudad."),
        ],
        "apply": [
            ex(f"{PA1} Clasifica como natural o humano: el puente.", "humano", "Lo construyeron las personas."),
            ex(f"{PA1} Clasifica como natural o humano: los árboles del paisaje B.", "natural", "Crecen en la naturaleza."),
            ex(f"{PA1} Cuenta cuántos elementos humanos tiene el paisaje A.", "3", "Casas, calles y un muelle."),
        ],
        "reason": [
            ex("Pablo dice: «Hay mar, entonces es el norte». ¿Qué respondes?", "Hay mar en todas las zonas de Chile", "El mar no define una sola zona."),
            ex("Una niña dice que los campos de cultivo son naturales porque tienen plantas. ¿Qué respondes?", "Los hacen las personas; son un elemento humano", "Las personas los siembran y los modifican."),
        ],
        "challenge": [
            ex(f"{PA1} Haz una tabla corta del paisaje B con dos naturales y dos humanos.", "Naturales: río, árboles. Humanos: puente, ciudad", "Cada elemento está en su columna."),
            ex(f"{PA1} Cuenta cuántos elementos humanos tiene el paisaje B.", "3", "Un puente, una ciudad y campos de cultivo: 1 + 1 + 1 = 3."),
        ],
    },
    context=[ex("Una niña mira una foto de una playa con cerros y escribe: «Cerros, mar, arena y una caseta de salvavidas». ¿Cuál de esos elementos es humano?", "la caseta de salvavidas", "Es una construcción hecha por personas.")],
    selfcheck=[
        ex("¿La playa es un elemento natural o humano?", "natural", "Existe en la naturaleza."),
        ex("¿Una calle es natural o humana?", "humana", "La construyen las personas."),
        ex("El océano Pacífico, ¿es una gran extensión de agua salada o una corriente de agua que corre por un valle?", "una gran extensión de agua salada", "Eso es un océano; la corriente de agua es un río."),
    ],
    open_task=task(
        f"Mira el paisaje A de la ficha y haz una tabla de dos columnas: elementos naturales y elementos humanos. {PA1} Escribe al final una frase que describa el paisaje sin decir la zona.",
        "Naturales: mar, playa, cerros. Humanos: casas, calles, muelle. Frase: Es un paisaje con mar y cerros donde las personas construyeron casas y un muelle.",
        ["dos columnas", "elementos bien clasificados", "frase sin la zona"], ["tabla escrita"], ["poner casas en natural", "decir la zona sin pistas"],
        "Pregunta qué más necesitaría saber para decir la zona."),
    reinforce="Mira por una ventana o en una foto y separa lo natural de lo humano.",
    extend="Haz otra tabla con un paisaje que hayas visto, con dos naturales y dos humanos.",
)

ZN = ("Ficha de la zona norte (dada por la clase): la zona norte va aproximadamente desde Arica hasta la región de Coquimbo. Los límites de las zonas cambian un poco según la fuente. "
      "Desierto de Atacama: lugar con muy poca lluvia, suelo seco y arena. Altiplano: planicie alta cerca de la cordillera de los Andes, con volcanes y lagunas. "
      "Valle del Elqui: valle de la región de Coquimbo con ríos, cultivos de parras y cielos claros. Costa: el océano Pacífico junto a ciudades y puertos, como Arica, Iquique y Antofagasta. "
      "El río Loa, el más largo de Chile, cruza el desierto de Atacama. San Pedro de Atacama es un pueblo del desierto, más pequeño que una ciudad.")
register(
    OA8, 2,
    materials="Lápiz y papel. La ficha de la zona norte está escrita en cada ejercicio.",
    use="Aprenderé a describir paisajes de la zona norte de Chile usando desierto, altiplano, valle y costa. Sirve para no decir que todo el norte es desierto.",
    prior=["Sé separar elementos naturales y humanos.", "Sé qué es una zona."],
    explain=[
        "Una zona es una gran parte del país con rasgos parecidos. Aquí usamos tres zonas: norte, centro y sur. La zona norte va aproximadamente desde Arica hasta la región de Coquimbo. Los límites exactos cambian un poco según la fuente.",
        "El norte tiene paisajes distintos. El desierto de Atacama tiene muy poca lluvia y suelo seco. El altiplano es una planicie alta, cerca de la cordillera de los Andes, con volcanes y lagunas. En el valle del Elqui hay ríos y cultivos de parras. En la costa hay ciudades y puertos junto al océano Pacífico, como Arica, Iquique y Antofagasta. El río Loa, el más largo de Chile, cruza el desierto, y San Pedro de Atacama es un pueblo del desierto.",
        "Por eso no es correcto decir que todo el norte es desierto. Cada paisaje del norte tiene sus elementos. Para comparar dos paisajes usamos las mismas preguntas: ¿qué relieve tiene?, ¿hay agua?, ¿hay ciudades o cultivos? Así comparamos con orden.",
    ],
    vocab=[("zona", "gran parte del país con rasgos parecidos"), ("desierto", "lugar con muy poca lluvia"), ("altiplano", "planicie alta cerca de la cordillera de los Andes"), ("valle", "terreno bajo entre cerros, por donde suele pasar un río"), ("costa", "borde de tierra junto al mar")],
    worked=[
        {"title": "Un paisaje del norte", "problem": f"{ZN} ¿Qué tiene el valle del Elqui que no tiene el desierto?", "steps": ["El valle tiene ríos y cultivos.", "El desierto tiene muy poca lluvia."], "answer": "Ríos y cultivos"},
        {"title": "Corregir una generalización", "problem": f"{ZN} Un niño dice «Todo el norte es desierto». ¿Qué paisajes lo contradicen?", "steps": ["El altiplano tiene volcanes y lagunas.", "El valle del Elqui tiene ríos y cultivos, y la costa tiene el mar."], "answer": "El altiplano, el valle del Elqui y la costa"},
    ],
    mistakes=[
        {"wrong": "Decir que todo el norte es desierto.", "why": "Se generaliza un solo paisaje.", "fix": "El norte tiene desierto, altiplano, valles y costa."},
        {"wrong": "Confundir altiplano con costa.", "why": "Se piensa solo en el norte en general.", "fix": "El altiplano es alto, cerca de los Andes; la costa está junto al mar."},
    ],
    tiers={
        "recovery": [
            ex(f"{ZN} ¿Qué río, el más largo de Chile, cruza el desierto de Atacama?", "el río Loa", "La ficha lo dice."),
            ex(f"{ZN} ¿Qué se cultiva en el valle del Elqui?", "parras", "La ficha lo dice."),
            ex(f"{ZN} ¿Qué tienen en común Arica, Iquique y Antofagasta?", "están en la costa", "La ficha las nombra en la costa."),
        ],
        "understand": [
            ex(f"{ZN} ¿Cómo es la lluvia en el desierto de Atacama?", "muy escasa", "La ficha dice que hay muy poca lluvia."),
            ex(f"{ZN} ¿Qué hay en el altiplano?", "volcanes y lagunas", "La ficha lo dice."),
            ex("¿Qué es una zona?", "una gran parte del país con rasgos parecidos", "Esa es su definición."),
        ],
        "apply": [
            ex(f"{ZN} Une: 1) altiplano, 2) valle del Elqui. A) ríos y parras, B) planicie alta con volcanes.", "1 con B; 2 con A", "Cada paisaje tiene sus rasgos."),
            ex(f"{ZN} Clasifica este paisaje: «arena, suelo seco y muy poca lluvia». ¿Qué paisaje del norte es?", "desierto", "Coincide con la descripción del desierto."),
            ex(f"{ZN} Clasifica este paisaje: «puertos, ciudades y mar». ¿Qué paisaje del norte es?", "costa", "La costa tiene el mar junto a ciudades."),
        ],
        "reason": [
            ex("Un niño dice: «En el norte no hay ríos». Usa la ficha para responder.", "Hay ríos, como el Loa y los del valle del Elqui", "La ficha los nombra."),
            ex(f"{ZN} ¿Por qué no es lo mismo el altiplano que la costa?", "Porque uno es una planicie alta y la otra está junto al mar", "Son relieves distintos."),
        ],
        "challenge": [
            ex(f"{ZN} Compara el desierto y el valle del Elqui con la misma pregunta: ¿hay agua?", "En el desierto hay muy poca; en el valle hay ríos", "Se comparan con una misma pregunta."),
            ex(f"{ZN} Escribe cuatro paisajes del norte.", "desierto, altiplano, valle y costa", "Son los cuatro de la ficha."),
        ],
    },
    context=[ex("Una profesora muestra una foto de una laguna con volcanes al fondo y llamas pastando. Dice que está en la zona norte. ¿Qué paisaje de la ficha es: altiplano o costa?", "altiplano", "El altiplano tiene volcanes y lagunas.")],
    selfcheck=[
        ex(f"{ZN} ¿Dónde está el valle del Elqui?", "en la región de Coquimbo", "La ficha lo dice."),
        ex("¿Todo el norte es desierto?", "no", "Tiene altiplano, valles y costa."),
        ex(f"{ZN} ¿San Pedro de Atacama es una ciudad grande o un pueblo?", "un pueblo", "La ficha dice que es un pueblo más pequeño que una ciudad."),
    ],
    open_task=task(
        f"Dibuja una franja del norte con cuatro cuadros: desierto, altiplano, valle y costa. Debajo de cada cuadro escribe dos rasgos. {ZN}",
        "Desierto: poca lluvia y arena. Altiplano: volcanes y lagunas. Valle: ríos y parras. Costa: puertos y mar.",
        ["cuatro cuadros", "dos rasgos por paisaje", "no dice que todo es desierto"], ["dibujo y rasgos escritos"], ["decir que todo el norte es desierto", "mezclar rasgos"],
        "Pide que explique en qué se diferencia el valle del desierto."),
    reinforce="Nombra los cuatro paisajes del norte y un rasgo de cada uno.",
    extend="Escribe una pregunta para comparar el altiplano con la costa.",
)

ZC = ("Ficha de la zona centro (dada por la clase): la zona centro va aproximadamente desde la región de Valparaíso hasta cerca del río Biobío. Los límites cambian un poco según la fuente. "
      "Tiene un valle central entre dos cordilleras: la cordillera de los Andes al este y la cordillera de la Costa al oeste. Hay costa con playas y puertos, como Valparaíso. "
      "Hay ríos como el Maipo, campos de cultivo y grandes ciudades como Santiago. Los veranos son secos y calurosos y los inviernos tienen lluvia. "
      "En el océano Pacífico, lejos de la costa, están la isla Rapa Nui y el archipiélago Juan Fernández, un grupo de islas. Ambos pertenecen a la región de Valparaíso.")
register(
    OA8, 3,
    materials="Lápiz y papel. La ficha de la zona centro está escrita en cada ejercicio.",
    use="Aprenderé a reconocer un paisaje de la zona centro combinando valle, cordilleras, costa y ciudades. Sirve para saber que un solo elemento no basta para decidir la zona.",
    prior=["Sé separar elementos naturales y humanos.", "Sé qué es una zona."],
    explain=[
        "La zona centro va aproximadamente desde la región de Valparaíso hasta cerca del río Biobío. Sus límites cambian un poco según la fuente. En esta zona vive mucha gente y están ciudades grandes, como Santiago.",
        "El paisaje de la zona centro combina varios elementos. Hay un valle central entre dos cordilleras: la cordillera de los Andes al este y la cordillera de la Costa al oeste. Hay costa con playas y puertos, como Valparaíso. Hay ríos como el Maipo y campos de cultivo. El clima tiene veranos secos y calurosos e inviernos con lluvia. En el océano Pacífico, frente a la costa, están la isla Rapa Nui y el archipiélago Juan Fernández, que pertenecen a la región de Valparaíso.",
        "Un solo elemento no basta para decir que un paisaje es de la zona centro. Un valle, una costa o un río también existen en otras zonas. Lo que ayuda es juntar varias pistas: valle entre dos cordilleras, ciudades grandes, cultivos y clima de veranos secos.",
    ],
    vocab=[("valle central", "terreno bajo entre la cordillera de los Andes y la cordillera de la Costa"), ("cordillera de la Costa", "cadena de cerros cerca del mar"), ("cordillera de los Andes", "cadena de montañas altas al este de Chile"), ("clima", "tiempo que hay en un lugar durante el año"), ("pista", "dato que ayuda a descubrir algo")],
    worked=[
        {"title": "Reconocer pistas", "problem": f"{ZC} Nombra dos pistas que indiquen la zona centro.", "steps": ["El valle entre dos cordilleras es una pista.", "También lo son las ciudades grandes como Santiago y el clima de veranos secos."], "answer": "Valle central y ciudades grandes"},
        {"title": "Un elemento no basta", "problem": f"{ZC} ¿Basta ver un valle para decir que es la zona centro?", "steps": ["Hay valles también en el norte, como el valle del Elqui.", "Necesitamos más pistas."], "answer": "No; hace falta juntar más pistas"},
    ],
    mistakes=[
        {"wrong": "Decir que es la zona centro solo porque hay una ciudad.", "why": "Hay ciudades en todas las zonas.", "fix": "Junta varias pistas: valle central, dos cordilleras, cultivos y clima."},
        {"wrong": "Confundir la cordillera de los Andes con la cordillera de la Costa.", "why": "Las dos son cordilleras.", "fix": "Los Andes están al este y la Costa al oeste, cerca del mar."},
    ],
    tiers={
        "recovery": [
            ex(f"{ZC} ¿Qué cordillera queda al este del valle central?", "la cordillera de los Andes", "La ficha lo dice."),
            ex(f"{ZC} ¿Qué cordillera queda al oeste del valle central?", "la cordillera de la Costa", "La ficha lo dice."),
            ex(f"{ZC} ¿Cómo son los veranos en la zona centro?", "secos y calurosos", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{ZC} ¿Qué ciudad grande se nombra en la ficha?", "Santiago", "La ficha lo dice."),
            ex(f"{ZC} ¿Qué río se nombra en la ficha?", "el Maipo", "La ficha lo dice."),
            ex("¿Qué es el valle central?", "un terreno bajo entre la cordillera de los Andes y la de la Costa", "Esa es su definición."),
        ],
        "apply": [
            ex(f"{ZC} Une: 1) cordillera de los Andes, 2) cordillera de la Costa. A) oeste, B) este.", "1 con B; 2 con A", "Los Andes están al este y la Costa al oeste."),
            ex(f"{ZC} Un paisaje tiene valle entre dos cordilleras, campos de cultivo y una gran ciudad. ¿Qué zona es probable?", "la zona centro", "Junta varias pistas de la ficha."),
            ex(f"{ZC} Clasifica como natural o humano: el río Maipo.", "natural", "Existe en la naturaleza."),
        ],
        "reason": [
            ex("Un niño dice: «Hay un valle, así que es la zona centro». ¿Qué respondes?", "Hay valles en otras zonas; faltan más pistas", "Un solo elemento no basta."),
            ex(f"{ZC} ¿Por qué ayuda el clima para reconocer la zona centro?", "Porque sus veranos son secos y calurosos y sus inviernos tienen lluvia", "Es una pista que la ficha entrega."),
        ],
        "challenge": [
            ex(f"{ZC} Escribe tres pistas juntas que apuntan a la zona centro.", "valle central, dos cordilleras y ciudades grandes", "Una sola pista no basta."),
            ex(f"{ZC} ¿Por qué se llama valle central?", "Porque está en el medio, entre las dos cordilleras", "Está entre las cordilleras."),
        ],
    },
    context=[ex("Una foto muestra una ciudad grande, un río y campos de frutas, con cerros nevados al este. ¿Qué cordillera sería: la de los Andes o la de la Costa?", "la cordillera de los Andes", "Los Andes están al este y tienen nieve en las partes altas.")],
    selfcheck=[
        ex(f"{ZC} ¿Entre qué dos cordilleras está el valle central?", "entre los Andes y la Costa", "La ficha lo dice."),
        ex(f"{ZC} ¿Qué dos lugares del océano Pacífico pertenecen a la región de Valparaíso?", "la isla Rapa Nui y el archipiélago Juan Fernández", "La ficha los nombra."),
        ex("¿Un solo elemento basta para decir la zona?", "no", "Hace falta juntar pistas."),
    ],
    open_task=task(
        f"Dibuja un corte simple de la zona centro de oeste a este: mar, cordillera de la Costa, valle central, cordillera de los Andes. {ZC} Escribe tres pistas que no bastan por sí solas y una que ayuda más.",
        "Mar, cordillera de la Costa, valle central, cordillera de los Andes. No bastan por sí solas: valle, río, ciudad. Ayuda más: valle entre dos cordilleras.",
        ["cuatro partes en orden de oeste a este", "tres pistas insuficientes", "una pista fuerte"], ["dibujo y notas"], ["poner los Andes al oeste", "decir que una sola pista basta"],
        "Pide que explique por qué un valle no es suficiente."),
    reinforce="Di en voz alta qué hay al oeste y al este del valle central.",
    extend="Compara en una frase el valle central con el valle del Elqui.",
)

ZS = ("Ficha de la zona sur (dada por la clase): la zona sur va aproximadamente desde cerca del río Biobío hasta Magallanes. Los límites cambian según la fuente. "
      "En La Araucanía hay volcanes, como el Villarrica, lagos y bosques con lluvia. Chiloé es una isla grande dentro de un archipiélago, es decir, un grupo de islas, con iglesias de madera. "
      "En la Patagonia hay fiordos, que son canales de mar entre montañas, glaciares, que son grandes masas de hielo, y mucho viento frío. Puerto Montt es una ciudad del sur junto al mar.")
register(
    OA8, 4,
    materials="Lápiz y papel. La ficha de la zona sur está escrita en cada ejercicio.",
    use="Aprenderé a distinguir lagos, volcanes, islas, fiordos y bosques del sur de Chile. Sirve para describir los paisajes del sur con vocabulario geográfico.",
    prior=["Sé separar elementos naturales y humanos.", "Sé qué es una zona."],
    explain=[
        "La zona sur va aproximadamente desde cerca del río Biobío hasta Magallanes. Sus límites cambian según la fuente. Es una zona con mucha lluvia y paisajes muy variados.",
        "En La Araucanía hay volcanes, como el Villarrica, lagos y bosques. Chiloé es una isla grande dentro de un archipiélago, que es un grupo de islas. En la Patagonia hay fiordos, que son canales de mar entre montañas, glaciares, que son grandes masas de hielo, y viento frío.",
        "Para comparar paisajes del sur usamos un mapa y fotos. La Araucanía se reconoce por volcanes y lagos. Chiloé, por islas e iglesias de madera. La Patagonia, por fiordos, glaciares y canales. Cada paisaje tiene sus rasgos y no todos los paisajes del sur son iguales.",
    ],
    vocab=[("volcán", "montaña por donde puede salir material caliente de la Tierra"), ("lago", "gran extensión de agua rodeada de tierra"), ("isla", "tierra rodeada de agua"), ("archipiélago", "grupo de islas"), ("fiordo", "canal de mar entre montañas"), ("glaciar", "gran masa de hielo")],
    worked=[
        {"title": "Reconocer rasgos", "problem": f"{ZS} ¿Qué rasgos tiene La Araucanía?", "steps": ["Busco La Araucanía.", "Tiene volcanes, lagos y bosques."], "answer": "Volcanes, lagos y bosques"},
        {"title": "Definir un término", "problem": f"{ZS} ¿Qué es un fiordo?", "steps": ["Leo la ficha.", "Es un canal de mar entre montañas."], "answer": "Un canal de mar entre montañas"},
    ],
    mistakes=[
        {"wrong": "Decir que todo el sur es igual.", "why": "Se piensa en un solo paisaje.", "fix": "Compara La Araucanía, Chiloé y la Patagonia."},
        {"wrong": "Confundir un lago con un fiordo.", "why": "Los dos tienen agua entre montañas.", "fix": "Un lago es agua rodeada de tierra; un fiordo es un canal de mar."},
    ],
    tiers={
        "recovery": [
            ex(f"{ZS} ¿Qué volcán se nombra en la ficha?", "el Villarrica", "La ficha lo dice."),
            ex(f"{ZS} ¿Qué es Chiloé?", "una isla grande dentro de un archipiélago", "La ficha lo dice."),
            ex(f"{ZS} ¿Qué es un archipiélago?", "un grupo de islas", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{ZS} ¿Qué es un fiordo?", "un canal de mar entre montañas", "La ficha lo dice."),
            ex(f"{ZS} ¿Qué hay en la Patagonia, según la ficha?", "fiordos, glaciares y viento frío", "La ficha lo dice."),
            ex("¿En qué se diferencia un lago de un fiordo?", "El lago es agua rodeada de tierra y el fiordo es un canal de mar", "El fiordo es agua de mar."),
        ],
        "apply": [
            ex(f"{ZS} Une: 1) La Araucanía, 2) Patagonia. A) fiordos y glaciares, B) volcanes y lagos.", "1 con B; 2 con A", "Cada lugar tiene sus rasgos."),
            ex(f"{ZS} Un paisaje tiene islas e iglesias de madera. ¿Qué lugar es probable?", "Chiloé", "Chiloé es una isla con iglesias de madera."),
            ex(f"{ZS} Un paisaje tiene un canal de mar entre montañas con hielo. ¿Qué rasgo es?", "un fiordo con glaciar", "La ficha define fiordo y glaciar."),
        ],
        "reason": [
            ex("Un niño dice: «El sur es solo bosque y lluvia». Usa la ficha para responder.", "También hay volcanes, lagos, islas, fiordos y glaciares", "El sur es variado."),
            ex(f"{ZS} ¿Cuál está unido al mar: un lago o un fiordo?", "un fiordo", "El fiordo es un canal de mar entre montañas."),
        ],
        "challenge": [
            ex(f"{ZS} Escribe una pista para reconocer La Araucanía y otra para la Patagonia.", "Araucanía: volcanes y lagos. Patagonia: fiordos y glaciares", "Cada lugar tiene sus pistas."),
            ex(f"{ZS} Ordena de más cerca a más lejos del norte del país: Patagonia, La Araucanía.", "La Araucanía, Patagonia", "La Araucanía está más al norte que la Patagonia."),
        ],
    },
    context=[ex("En una foto se ve un volcán nevado detrás de un lago azul y bosques. ¿Es más probable que sea La Araucanía o la Patagonia con fiordos?", "La Araucanía", "Volcán y lago son rasgos de La Araucanía en la ficha.")],
    selfcheck=[
        ex("¿Qué es una isla?", "tierra rodeada de agua", "Esa es su definición."),
        ex(f"{ZS} ¿Qué lugar tiene volcanes y lagos?", "La Araucanía", "La ficha lo dice."),
        ex("¿Todo el sur es igual?", "no", "Tiene paisajes distintos."),
    ],
    open_task=task(
        f"Haz una tabla con tres columnas: La Araucanía, Chiloé y Patagonia. Escribe en cada una tres rasgos. {ZS}",
        "La Araucanía: volcanes, lagos, bosques. Chiloé: isla, archipiélago, iglesias de madera. Patagonia: fiordos, glaciares, viento frío.",
        ["tres columnas", "tres rasgos por columna", "vocabulario correcto"], ["tabla escrita"], ["mezclar lugares", "confundir lago con fiordo"],
        "Pide que muestre cuál rasgo hace distinto a cada lugar."),
    reinforce="Di en voz alta tres palabras del sur y qué significan.",
    extend="Escribe cómo cambiaría la ropa que usarías en la Patagonia comparada con el valle central.",
)

CL = ("Tres casos de ejemplo (dados por la clase). Caso 1: fotografía de dunas de arena y cielo despejado; descripción: «llueve muy poco»; mapa: el lugar está al norte de Coquimbo. "
      "Caso 2: fotografía de un valle con viñas y cerros nevados al fondo; mapa: el lugar está entre Santiago y Rancagua. "
      "Caso 3: fotografía de montañas con glaciares y un canal de mar entre ellas; descripción: «hay mucho viento frío». "
      "Caso 4: fotografía de un cerro con nieve, sin más datos.")
register(
    OA8, 5,
    materials="Lápiz y papel. Los casos de ejemplo están escritos en cada ejercicio.",
    use="Aprenderé a justificar la zona de un paisaje usando fotografía, mapa y descripción, y a decir cuándo no tengo suficientes pistas. Sirve para clasificar con más seguridad.",
    prior=["Sé las características de las zonas norte, centro y sur.", "Sé que una sola pista no siempre basta."],
    explain=[
        "Para decir en qué zona de Chile está un paisaje, usamos varias fuentes: una fotografía, un mapa y una descripción. Cada fuente da una pista. Una pista decisiva es la que más ayuda a decidir la zona.",
        "Por ejemplo, en el caso 1 vemos dunas, la descripción dice que llueve muy poco y el mapa lo ubica al norte de Coquimbo. Eso apunta a la zona norte. En el caso 2 hay un valle con viñas y un mapa que lo ubica entre Santiago y Rancagua, así que es la zona centro. En el caso 3 hay glaciares, un canal de mar y viento frío, que son pistas del sur.",
        "A veces no hay suficientes pistas. El caso 4 tiene una foto de un cerro con nieve y nada más. Hay cerros con nieve en las tres zonas, así que no podemos decidir. En esos casos decimos: «no tengo suficientes pistas» y pedimos otra fuente. Eso se llama reconocer la incertidumbre.",
    ],
    vocab=[("fuente", "algo que da información, como una foto, un mapa o un texto"), ("pista decisiva", "dato que más ayuda a decidir"), ("incertidumbre", "cuando no estamos seguros de algo"), ("justificar", "dar razones para explicar una decisión"), ("clasificar", "poner algo en un grupo según sus rasgos")],
    worked=[
        {"title": "Pista decisiva", "problem": f"{CL} ¿Cuál es la pista decisiva del caso 2?", "steps": ["La foto muestra valle con viñas.", "El mapa lo ubica entre Santiago y Rancagua, que está en la zona centro."], "answer": "El mapa: entre Santiago y Rancagua"},
        {"title": "Reconocer la incertidumbre", "problem": f"{CL} ¿Podemos decir la zona del caso 4?", "steps": ["Solo hay una foto de un cerro con nieve.", "Hay cerros con nieve en las tres zonas."], "answer": "No; hacen falta más pistas"},
    ],
    mistakes=[
        {"wrong": "Decidir la zona con una sola pista que sirve para varias.", "why": "Se quiere responder rápido.", "fix": "Junta fotografía, mapa y descripción."},
        {"wrong": "Responder siempre, aunque falten pistas.", "why": "Se cree que no saber es malo.", "fix": "Si faltan pistas, escribe «no tengo suficientes pistas»."},
    ],
    tiers={
        "recovery": [
            ex(f"{CL} ¿Qué zona es probable en el caso 1?", "la zona norte", "Dunas, poca lluvia y ubicación al norte de Coquimbo."),
            ex(f"{CL} ¿Qué zona es probable en el caso 3?", "la zona sur", "Glaciares, canal de mar y viento frío."),
            ex(f"{CL} ¿Qué zona es probable en el caso 2?", "la zona centro", "Valle con viñas entre Santiago y Rancagua."),
        ],
        "understand": [
            ex("¿Qué es una pista decisiva?", "el dato que más ayuda a decidir", "Es la pista más fuerte."),
            ex(f"{CL} ¿Cuántas fuentes tiene el caso 1?", "3", "Fotografía, descripción y mapa."),
            ex("¿Qué significa incertidumbre?", "no estar seguro de algo", "Cuando faltan pistas."),
        ],
        "apply": [
            ex(f"{CL} Escribe la pista decisiva del caso 1.", "el mapa: al norte de Coquimbo, o poca lluvia", "Cualquiera de las dos indica el norte."),
            ex(f"{CL} Escribe la pista decisiva del caso 3.", "glaciares y un canal de mar con viento frío", "Son pistas del sur."),
            ex(f"{CL} ¿Cuántos de los cuatro casos permiten decidir la zona?", "3", "Los casos 1, 2 y 3."),
        ],
        "reason": [
            ex(f"{CL} Un niño dice que el caso 4 es de la zona sur por la nieve. ¿Qué respondes?", "Hay nieve en cerros de las tres zonas; faltan pistas", "La nieve sola no decide."),
            ex("¿Por qué es mejor decir «no tengo suficientes pistas» que adivinar?", "Porque una respuesta sin pistas puede ser falsa", "La honestidad ayuda a investigar mejor."),
        ],
        "challenge": [
            ex(f"{CL} Escribe una pista que ayudaría a decidir el caso 4.", "un mapa que diga dónde está", "El mapa da la ubicación."),
            ex(f"{CL} Escribe una frase que justifique la zona del caso 2 con dos fuentes.", "Es la zona centro porque la foto muestra viñas y el mapa lo ubica entre Santiago y Rancagua", "Usa foto y mapa."),
        ],
    },
    context=[ex("Un paisaje: fotografía de un lago con un volcán y bosques; descripción: «llueve mucho»; mapa: en La Araucanía. ¿Qué zona es probable y cuál fuente la confirma?", "la zona sur; el mapa que dice La Araucanía", "El mapa ubica el lugar en el sur.")],
    selfcheck=[
        ex(f"{CL} ¿Qué caso no se puede clasificar?", "el caso 4", "Solo hay una foto sin más pistas."),
        ex("¿Una sola pista siempre basta?", "no", "Puede servir a más de una zona."),
        ex(f"{CL} ¿Cuántos casos de la ficha incluyen un mapa?", "2", "Los casos 1 y 2 incluyen un mapa."),
    ],
    open_task=task(
        f"Resuelve los casos 1, 2 y 3 en una tabla con tres columnas: zona probable, pista decisiva y si estás seguro o no. {CL} Para el caso 4 escribe qué otra fuente pedirías.",
        "Caso 1: norte; poca lluvia y mapa al norte de Coquimbo; seguro. Caso 2: centro; mapa entre Santiago y Rancagua; seguro. Caso 3: sur; glaciares y canal de mar; seguro. Caso 4: pido un mapa.",
        ["tres casos resueltos", "pista decisiva", "incertidumbre del caso 4"], ["tabla escrita"], ["decidir el caso 4 sin pistas", "no justificar"],
        "Pide que lea una pista y diga de qué fuente salió."),
    reinforce="Elige una foto de un paisaje y escribe tres pistas que ves.",
    extend="Inventa un caso nuevo con tres fuentes para que un compañero decida su zona.",
)

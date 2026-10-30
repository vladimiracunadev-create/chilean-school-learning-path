"""Cuaderno del estudiante, 1.º básico Historia, Geografía y Ciencias Sociales: OA 09 (Chile en mapas) y OA 10 (paisajes y ubicación relativa)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA9, OA10 = "HI01 OA 09", "HI01 OA 10"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Este cuaderno, un lápiz y, si tienes, un globo terráqueo o un mapa del mundo en casa. No es obligatorio: todo lo que necesitas está escrito aquí.",
    use="Aprenderé a encontrar Chile en el mundo: en qué continente está, qué océano tiene cerca y qué países son sus vecinos. Sirve para saber dónde vivo y explicárselo a alguien de otro lugar.",
    prior=["Sé que un país es un lugar con su propio gobierno.", "Sé que hay mar y tierra en el mundo."],
    explain=[
        "La Tierra se puede mostrar de dos maneras. El globo terráqueo es una bola que se parece a la Tierra. El mapamundi es la Tierra dibujada en una hoja plana. En los dos se ven los continentes, que son las partes grandes de tierra, y los océanos, que son las grandes extensiones de agua salada.",
        "Chile es un país. Está en el continente de América, en la parte llamada América del Sur. Por el norte tiene como vecino a Perú, por el noreste a Bolivia y por el este a Argentina. Por el oeste está el océano Pacífico. Todo esto se lee en el mapa, igual que se lee un cuento.",
        "Chile tiene una forma muy especial: es largo y angosto, como una cinta que va de norte a sur. Mide más de 4.000 kilómetros de largo, pero de este a oeste es muy angosto. Por eso es fácil de reconocer en un mapa.",
    ],
    vocab=[("globo terráqueo", "bola que representa la Tierra"), ("mapamundi", "mapa plano de todo el mundo"), ("continente", "parte muy grande de tierra, con varios países"), ("país", "territorio con su gobierno, como Chile"), ("océano", "extensión muy grande de agua salada")],
    worked=[
        W("Encontrar Chile con pistas", "Busco un país que está en América del Sur, tiene forma de cinta larga y angosta y el océano Pacífico a su lado oeste. ¿Cuál es?",
          ["Busco el continente de América y, en su parte sur, miro los países.", "Busco el país largo y angosto pegado al océano.", "El océano Pacífico queda al oeste, a su lado."], "Chile"),
        W("Un país vecino", "Estoy parado en Chile y camino hacia el este, hasta salir del país. ¿En qué país entro?",
          ["Sé que el este queda donde sale el sol.", "Al este de Chile el mapa dice Argentina.", "Entro en Argentina."], "Argentina"),
    ],
    mistakes=[
        M("Decir que Chile es un continente.", "Se confunde país con continente.", "El continente es más grande; Chile es un país dentro de América del Sur."),
        M("Pensar que Chile es ancho como un círculo.", "No se mira la forma en el mapa.", "Chile es una cinta larga y angosta de norte a sur."),
    ],
    tiers=tiers(
        [ex("Un continente es una parte muy grande de tierra con varios países. Un país es una parte más pequeña con su gobierno. ¿Chile es un país o un continente?", "Un país", "Chile es una parte con su gobierno dentro de América."),
         ex("¿En qué continente está Chile?", "En América (América del Sur)", "Chile queda en la parte sur de América."),
         ex("¿Cuál se parece más a la forma de Chile: una cinta larga y angosta o una pelota redonda?", "Una cinta larga y angosta", "Chile es largo de norte a sur y angosto de este a oeste.")],
        [ex("¿En qué se diferencia un globo terráqueo de un mapamundi?", "El globo es una bola y el mapamundi es plano", "Los dos muestran la Tierra, pero en distinta forma."),
         ex("Chile mide más de 4.000 kilómetros de largo y es angosto. ¿Por qué se reconoce fácil en un mapa?", "Por su forma de cinta larga y angosta", "Casi ningún país tiene una forma tan larga y delgada."),
         ex("¿Qué océano queda al oeste de Chile?", "El océano Pacífico", "El agua que baña la costa chilena es del Pacífico.")],
        [ex("Un país tiene como capital a Lima y queda al norte de Chile. ¿Cuál país es?", "Perú", "Lima es la capital de Perú, vecino del norte."),
         ex("Chile tiene tres vecinos: uno al norte, uno al noreste y uno al este. ¿Cuál queda al este?", "Argentina", "Argentina es el vecino del lado este."),
         ex("Un barco sale de la costa de Chile hacia el oeste y navega mucho tiempo sin tocar tierra. ¿Qué océano cruza?", "El Pacífico", "Hacia el oeste de la costa chilena está el Pacífico.")],
        [ex("Sara dice: «Chile está en África porque es un país». ¿Qué está mal en lo que dice?", "Chile está en América, no en África", "Un país siempre está dentro de un continente, y el de Chile es América."),
         ex("Pablo dice que Chile es más ancho que largo. Mira la forma de Chile y di si tiene razón.", "No; es mucho más largo que ancho", "Chile mide más de 4.000 km de largo y es angosto.")],
        [ex("Ordena de lo más grande a lo más pequeño: Chile, América del Sur, el mundo.", "El mundo, América del Sur, Chile", "El mundo contiene los continentes, y el continente contiene a Chile."),
         ex("Voy en un barco desde Chile hasta Japón sin ir por tierra. ¿Qué océano atravieso?", "El Pacífico", "Japón está al otro lado del océano Pacífico.")],
    ),
    context=[ex("Mateo vive en Chile y su prima Ana vive en Argentina. Mateo dice que su prima vive en otro continente. ¿Tiene razón? Explica.", "No; los dos países están en América del Sur", "Chile y Argentina son vecinos del mismo continente.")],
    selfcheck=[ex("Chile es un país. ¿De cuál continente forma parte?", "De América", "Chile es parte de América del Sur."), ex("Nombra un océano que está al oeste de Chile.", "El Pacífico", "Es el que baña la costa de Chile."), ex("Nombra un país vecino de Chile.", "Perú, Bolivia o Argentina", "Los tres comparten frontera con Chile.")],
    open_task=task("Completa esta carta para un niño que vive en otro país: «Vivo en ____, un país del continente de ____. Al oeste de mi país está el océano ____ y al este está el país ____. Mi país tiene forma de ____». Usa estas palabras: Argentina, Pacífico, América, Chile, cinta larga y angosta.", "Vivo en Chile, un país del continente de América. Al oeste de mi país está el océano Pacífico y al este está el país Argentina. Mi país tiene forma de cinta larga y angosta.", ["usa las cinco palabras en el lugar correcto", "no mezcla país con continente", "escribe una frase completa"], ["carta completada", "dibujo opcional de la forma de Chile"], ["poner América donde va Chile", "poner un océano donde va un país"], "Lee la carta en voz alta y pregunta si cada palabra cabe en su espacio."),
    reinforce="Con un adulto, mira un mapa o globo y apunta con el dedo a Chile, al océano Pacífico y a Argentina.",
    extend="Dibuja con una línea la forma de Chile y escribe a su lado el nombre de sus tres vecinos.",
)

register(
    OA9, 2,
    materials="Este cuaderno y un lápiz. Los mapas están escritos en palabras dentro de cada ejercicio.",
    use="Aprenderé a ubicar la cordillera de los Andes y el océano Pacífico en un mapa de Chile. Sirve para saber hacia dónde queda el mar y hacia dónde las montañas.",
    prior=["Sé que Chile es un país largo y angosto de América del Sur.", "Sé que el sol sale por el este."],
    explain=[
        "Los puntos cardinales sirven para decir hacia dónde queda algo. El sol sale por el este y se esconde por el oeste. Si miras al este, el norte queda a tu izquierda y el sur a tu derecha. En un mapa, el norte se dibuja arriba y el sur abajo.",
        "El océano Pacífico queda al oeste de Chile, en el lado izquierdo del mapa. La cordillera de los Andes queda al este, en el lado derecho, y separa a Chile de Argentina. Una cordillera es una fila larga de montañas muy altas, y en muchas se ve nieve en invierno.",
        "Así, en un mapa de Chile, de izquierda a derecha se lee: océano Pacífico, Chile y cordillera de los Andes, que es la frontera natural con Argentina. Esta línea de montañas recorre todo el largo del país. Esa pista te ayuda a no confundir el mar con la cordillera.",
    ],
    vocab=[("cordillera", "fila larga de montañas altas"), ("Andes", "la cordillera que está al este de Chile"), ("Pacífico", "el océano que está al oeste de Chile"), ("norte, sur, este, oeste", "los cuatro puntos cardinales"), ("frontera", "línea que separa un país de otro")],
    worked=[
        W("Dónde queda el mar", "En un mapa con el norte arriba, ¿a qué lado de Chile se dibuja el océano Pacífico?",
          ["El mar de Chile está al oeste.", "El oeste se dibuja a la izquierda.", "El Pacífico se dibuja a la izquierda de Chile."], "A la izquierda (oeste)"),
        W("Dónde quedan las montañas", "Una persona está en la costa de Chile y camina hacia el este. ¿Qué gran cordillera encontrará al final?",
          ["Camina desde el mar hacia donde sale el sol.", "En el lado este de Chile se alzan las montañas más altas.", "Encontrará la cordillera de los Andes."], "La cordillera de los Andes"),
    ],
    mistakes=[
        M("Poner la cordillera de los Andes al oeste, junto al mar.", "Se mezclan el este y el oeste.", "El mar de Chile queda al oeste y los Andes al este."),
        M("Creer que la cordillera es un solo cerro.", "No se piensa en la forma de fila.", "Una cordillera es una fila larga de muchas montañas."),
    ],
    tiers=tiers(
        [ex("¿Por qué punto cardinal sale el sol: este u oeste?", "Por el este", "El sol aparece por el este y se esconde por el oeste."),
         ex("¿Qué queda al oeste de Chile: el océano Pacífico o la cordillera de los Andes?", "El océano Pacífico", "El mar chileno está en el lado oeste."),
         ex("¿Qué queda al este de Chile: el océano Pacífico o la cordillera de los Andes?", "La cordillera de los Andes", "Las montañas están en el lado este.")],
        [ex("En un mapa, ¿qué punto cardinal se dibuja arriba?", "El norte", "Por acuerdo, el norte va arriba en los mapas."),
         ex("¿Qué es una cordillera?", "Una fila larga de montañas altas", "No es un cerro solo, son muchas montañas en fila."),
         ex("¿Qué separa a Chile de Argentina en gran parte de su frontera?", "La cordillera de los Andes", "Las montañas forman la frontera entre los dos países.")],
        [ex("Mapa descrito, de izquierda a derecha: A) Pacífico, B) Chile, C) Andes, D) Argentina. ¿Qué letra está entre Chile y Argentina?", "La C (los Andes)", "Después de Chile y antes de Argentina están las montañas."),
         ex("En el mismo mapa, ¿qué letra queda al oeste de Chile?", "La A (el Pacífico)", "El oeste es el lado izquierdo, donde está el océano."),
         ex("Voy en auto desde la costa de Chile hacia el este, sin parar. ¿Qué paisaje veré al final: mar o montañas muy altas?", "Montañas muy altas", "Al este de la costa están los Andes.")],
        [ex("Inés dibujó la cordillera de los Andes a la izquierda de Chile, pegada al mar. ¿Qué lado debía ser?", "A la derecha (este)", "Los Andes están en el este y se dibujan a la derecha."),
         ex("Luis dice: «Los Andes son un cerro». Explica si está en lo correcto.", "No; son una cordillera de muchas montañas", "Una cordillera es una fila de montañas, no un solo cerro.")],
        [ex("Si miras hacia el Pacífico desde Chile, ¿hacia qué punto cardinal miras?", "Hacia el oeste", "El mar de Chile está al oeste."),
         ex("Estás de espaldas al mar de Chile y miras de frente. ¿Qué punto cardinal tienes de frente?", "El este", "Si el mar está al oeste, la espalda hacia el mar mira al este.")],
    ),
    context=[ex("Camila está en un puerto de la costa de Chile y quiere ver nieve en las montañas. ¿Hacia qué punto cardinal debe viajar?", "Hacia el este", "Los Andes, con nieve en invierno, quedan al este.")],
    selfcheck=[ex("¿En qué lado de Chile, en un mapa, está el océano Pacífico?", "Al oeste, a la izquierda", "El mar de Chile queda al oeste."), ex("¿Cómo se llama la cordillera que está al este de Chile?", "Los Andes", "Es la gran cordillera de la frontera este."), ex("¿Qué punto cardinal es el opuesto al este?", "El oeste", "Este y oeste son lados contrarios.")],
    open_task=task("Dibuja un rectángulo largo y angosto para Chile. Escribe «Pacífico» en el lado izquierdo, «Los Andes» en el lado derecho y «Argentina» más a la derecha todavía. Escribe las letras N arriba y S abajo. Escribe al pie: «El mar queda al ____ y las montañas al ____» con las palabras este y oeste.", "El rectángulo tiene Pacífico a la izquierda, Los Andes a la derecha y Argentina después. Escribí: El mar queda al oeste y las montañas al este.", ["Pacífico a la izquierda", "Andes a la derecha", "N arriba y S abajo", "este y oeste bien escritos"], ["dibujo con rótulos", "frase completada"], ["cambiar el este por el oeste", "olvidar la N y la S"], "Pide mostrar con el dedo dónde sale el sol y comprobar que el Pacífico queda en el lado contrario."),
    reinforce="Señala en tu casa por dónde sale el sol y di en voz alta qué punto cardinal es.",
    extend="Escribe una frase que explique por qué viajar de la costa hacia el este te lleva a las montañas.",
)

register(
    OA9, 3,
    materials="Este cuaderno y un lápiz. Las listas de regiones y localidades están escritas en cada ejercicio.",
    use="Aprenderé a ubicar la capital de Chile, las regiones y mi localidad. Sirve para decir dónde vivo con datos claros: localidad, región y país.",
    prior=["Sé ubicar Chile, el Pacífico y los Andes.", "Sé qué es un país."],
    explain=[
        "Chile se divide en 16 regiones. Una región es una parte grande del país, con sus ciudades, pueblos y campos. Cada región tiene un nombre: por ejemplo, Región de Valparaíso, Región de Los Lagos y Región de Magallanes y de la Antártica Chilena.",
        "La capital de Chile es Santiago. Santiago está en la zona central, en la Región Metropolitana de Santiago, entre la cordillera de los Andes y otra cordillera más baja cerca del mar. La capital es la ciudad principal del país, donde está la sede del gobierno.",
        "Una localidad es el lugar donde viven las personas: una ciudad, un pueblo, una aldea o un barrio. Viña del Mar es una localidad de la Región de Valparaíso. Puerto Natales es una localidad de la Región de Magallanes. Tu localidad está dentro de una región, y tu región está dentro de Chile.",
    ],
    vocab=[("región", "parte grande en que se divide el país"), ("capital", "ciudad principal del país: Santiago"), ("localidad", "lugar donde viven las personas, como un pueblo o una ciudad"), ("Región Metropolitana", "la región donde está Santiago"), ("dentro de", "que forma parte de algo más grande")],
    worked=[
        W("Región de una localidad", "Puerto Varas es una localidad de la zona de los lagos del sur de Chile. Sé que está en la Región de Los Lagos. ¿Qué es Puerto Varas y qué es Los Lagos?",
          ["Puerto Varas es un lugar donde viven personas.", "Los Lagos es una parte grande del país.", "La localidad está dentro de la región."], "Puerto Varas es una localidad; Los Lagos es una región"),
        W("La capital", "Alguien dice que la capital de Chile es Valparaíso. Reviso mi dato: la capital es la ciudad principal del país, que está en la Región Metropolitana. ¿Cuál es?",
          ["La capital de Chile es Santiago.", "Santiago está en la Región Metropolitana.", "Valparaíso es otra ciudad, de otra región."], "Santiago"),
    ],
    mistakes=[
        M("Decir que Santiago es una región.", "Se confunde la capital con la región.", "Santiago es la capital, una ciudad, y está en la Región Metropolitana."),
        M("Poner la localidad como una parte más grande que la región.", "Se invierte el tamaño.", "La localidad es pequeña: está dentro de la región."),
    ],
    tiers=tiers(
        [ex("¿Cuál es la capital de Chile?", "Santiago", "Santiago es la capital del país."),
         ex("¿Cuántas regiones tiene Chile?", "16", "Chile está dividido en 16 regiones."),
         ex("¿Un pueblo es una localidad o una región?", "Una localidad", "Un pueblo es un lugar donde viven personas.")],
        [ex("¿Qué es más grande: una localidad o una región?", "Una región", "La región contiene muchas localidades."),
         ex("¿En qué región está la capital de Chile?", "En la Región Metropolitana", "Santiago está en la Región Metropolitana."),
         ex("¿Qué quiere decir «localidad»?", "El lugar donde viven las personas", "Puede ser una ciudad, un pueblo o una aldea.")],
        [ex("Viña del Mar y Valparaíso están en la misma región. ¿En cuál?", "Región de Valparaíso", "Las dos ciudades están en esa región."),
         ex("Puerto Natales es una localidad de Magallanes y de la Antártica Chilena. ¿Es una región o una localidad?", "Una localidad", "Es un lugar con casas y personas dentro de la región."),
         ex("Pichilemu es una localidad de la Región de O'Higgins. Si vivo en Pichilemu, ¿en qué región vivo?", "Región de O'Higgins", "La localidad está dentro de esa región.")],
        [ex("Rosa dice que Santiago es una región de Chile. ¿Qué es en realidad?", "La capital, una ciudad", "Santiago es una ciudad; la región es la Metropolitana."),
         ex("Tomás dice que su región cabe dentro de su localidad. ¿Está bien?", "No; la localidad cabe dentro de la región", "La región es más grande que la localidad.")],
        [ex("Ordena de más pequeño a más grande: región, localidad, país.", "Localidad, región, país", "La localidad está en la región y la región en el país."),
         ex("Pucón es una localidad de la Región de La Araucanía. Escribe dónde vive una niña de Pucón: localidad, región y país.", "Pucón, Región de La Araucanía, Chile", "Va de lo más pequeño a lo más grande.")],
    ),
    context=[ex("Tomás vive en San Pedro de Atacama, que es una localidad de la Región de Antofagasta. Su abuela le pregunta «¿en qué región vives?». ¿Qué responde?", "En la Región de Antofagasta", "La localidad está dentro de esa región.")],
    selfcheck=[ex("¿Cómo se llama la capital de Chile?", "Santiago", "Es la ciudad principal del país."), ex("¿Una región tiene dentro varias localidades?", "Sí", "La región es una parte grande."), ex("Escribe una localidad de Chile que hayas leído hoy.", "Por ejemplo Viña del Mar, Puerto Natales, Pucón o Pichilemu", "Todas son localidades de Chile.")],
    open_task=task("Completa esta tarjeta de ubicación con tu localidad: «Mi localidad se llama ____. Está en la región de ____. Mi región está en el país ____. La capital de mi país es ____». Si no sabes tu región, usa el ejemplo de Puerto Varas, Región de Los Lagos, y pide a un adulto que te ayude con la tuya.", "Mi localidad se llama Puerto Varas. Está en la región de Los Lagos. Mi región está en el país Chile. La capital de mi país es Santiago.", ["escribe localidad, región, país y capital", "los pone de menor a mayor tamaño", "escribe Santiago como capital"], ["tarjeta completa"], ["escribir Santiago como región", "confundir país y región"], "Pide leer la tarjeta de pequeño a grande y comprobar que cada lugar cabe dentro del siguiente."),
    reinforce="Pregunta a un adulto cómo se llama tu región y escríbela con letra grande.",
    extend="Escribe una frase con el nombre de otra localidad de Chile y la región en que está.",
)

register(
    OA9, 4,
    materials="Este cuaderno y un lápiz. El mapa que usarás está escrito con palabras en cada ejercicio.",
    use="Aprenderé a seguir una ruta de localización desde el mundo hasta una localidad. Sirve para explicar dónde queda un lugar paso a paso.",
    prior=["Sé ubicar Chile, los Andes y el Pacífico.", "Sé ordenar localidad, región, país y capital."],
    explain=[
        "Para ubicar un lugar puedes acercarte poco a poco, como cuando usas una lupa. Primero miras el mundo, luego el continente, después el país, la región y por último la localidad. Cada paso es más pequeño y más cercano que el anterior.",
        "La ruta de localización de Puerto Natales se dice así: está en el mundo, en el continente de América, en América del Sur, en el país de Chile, en la Región de Magallanes y de la Antártica Chilena, y es la localidad de Puerto Natales. Cada pista dice dónde está el lugar, cada vez con más detalle.",
        "También puedes usar pistas del mapa: el océano Pacífico queda al oeste, la cordillera de los Andes al este y la capital Santiago en la zona central. Estas referencias ayudan a no perderte y a comprobar si la ruta tiene sentido.",
    ],
    vocab=[("ruta de localización", "pasos que dicen dónde está un lugar"), ("referencia", "algo conocido que sirve para ubicarse"), ("de mayor a menor", "de lo más grande a lo más pequeño"), ("zona central", "parte del medio del país, donde está Santiago"), ("acercarse", "mirar un lugar cada vez más de cerca")],
    worked=[
        W("Armar una ruta", "Ordena de lo más grande a lo más pequeño para ubicar Viña del Mar: Región de Valparaíso, Chile, América, Viña del Mar.",
          ["Lo más grande es el continente: América.", "Dentro de América está el país: Chile.", "Dentro de Chile está la región: Valparaíso.", "Dentro de la región está la localidad: Viña del Mar."], "América, Chile, Región de Valparaíso, Viña del Mar"),
        W("Revisar una ruta", "Una ruta dice: «Chile, Pucón, Región de La Araucanía». ¿Está bien ordenada?",
          ["La localidad Pucón debe ir al final, porque es la más pequeña.", "Antes debe ir la región.", "La ruta correcta es Chile, Región de La Araucanía, Pucón."], "No; el orden correcto es Chile, Región de La Araucanía, Pucón"),
    ],
    mistakes=[
        M("Empezar la ruta por la localidad.", "Se va de lo pequeño a lo grande sin avisar.", "Para acercarse, parte por lo más grande y termina en la localidad."),
        M("Saltarse la región.", "Falta un paso de la ruta.", "Nombra el continente, el país, la región y la localidad."),
    ],
    tiers=tiers(
        [ex("Ordena de más grande a más pequeño: Chile, América, Santiago.", "América, Chile, Santiago", "El continente contiene al país y el país a la ciudad."),
         ex("¿Qué va primero en una ruta de localización: el continente o la localidad?", "El continente", "La ruta parte por lo más grande."),
         ex("¿Qué va al final de una ruta de localización: la localidad o el país?", "La localidad", "Es el lugar más pequeño y preciso.")],
        [ex("¿Para qué sirve una ruta de localización?", "Para decir dónde está un lugar paso a paso", "Cada pista acerca más al lugar."),
         ex("¿Por qué conviene nombrar la región antes de la localidad?", "Porque la localidad está dentro de la región", "La región es la parte más grande."),
         ex("¿Por qué una ruta de localización termina en la localidad y no en el continente?", "Porque la localidad es el lugar más pequeño y preciso", "Cada paso se acerca más al lugar que buscamos.")],
        [ex("Arma la ruta de Puerto Varas con estas piezas: Puerto Varas, Chile, Región de Los Lagos, América del Sur.", "América del Sur, Chile, Región de Los Lagos, Puerto Varas", "Va del lugar más grande al más pequeño."),
         ex("Sigue la ruta: América del Sur, Chile, Región Metropolitana. ¿A qué ciudad capital llegas?", "Santiago", "La capital de Chile está en la Región Metropolitana."),
         ex("Mapa descrito: de izquierda a derecha están el Pacífico, Chile y los Andes. Una niña viaja de oeste a este. ¿Qué dos referencias cruza en ese orden?", "Primero el Pacífico y luego los Andes", "Va de la izquierda del mapa a la derecha.")],
        [ex("Elisa dice: «Estoy en Chile, en Pucón, en la Región de La Araucanía». ¿Qué debe cambiar?", "Poner la región antes de Pucón", "Va primero el lugar más grande: la región."),
         ex("Un amigo dice que la ruta de Santiago empieza por Santiago. ¿Está bien?", "No; empieza por el continente o el país", "Se parte por lo más grande y se llega a la ciudad.")],
        [ex("Escribe la ruta de localización de Pichilemu, que está en la Región de O'Higgins, en Chile, en América del Sur.", "América del Sur, Chile, Región de O'Higgins, Pichilemu", "Cada lugar está dentro del anterior."),
         ex("Dos niños dicen: uno «vivo en Chile» y otro «vivo en Puerto Natales, Región de Magallanes, Chile». ¿Quién dio una ubicación más precisa?", "El segundo", "Dio localidad, región y país.")],
    ),
    context=[ex("Sofía envía una postal desde Puerto Montt, que es una localidad de la Región de Los Lagos. ¿Cómo escribirías la ruta desde el país hasta Puerto Montt?", "Chile, Región de Los Lagos, Puerto Montt", "Del país a la región y luego a la localidad.")],
    selfcheck=[ex("¿Qué se nombra primero en una ruta: lo más grande o lo más pequeño?", "Lo más grande", "La ruta se acerca poco a poco."), ex("Ordena: localidad, país, región.", "País, región, localidad", "Del más grande al más pequeño."), ex("¿En qué parte de la ruta va la capital Santiago?", "Como localidad, dentro de la Región Metropolitana", "Santiago es una ciudad de esa región.")],
    open_task=task("Escribe tu ruta de localización en cuatro pasos usando estas piezas y el ejemplo de Viña del Mar: «Estoy en el continente de ____, en el país ____, en la región ____ y en la localidad ____». Después dibuja flechas que bajen de un paso a otro. Si no sabes tu región o tu localidad, usa Viña del Mar, Región de Valparaíso.", "Estoy en el continente de América, en el país Chile, en la región de Valparaíso y en la localidad Viña del Mar.", ["cuatro pasos en el orden correcto", "usa la palabra región", "flechas de grande a pequeño"], ["frase completa", "dibujo de flechas"], ["empezar por la localidad", "saltarse la región"], "Pide leer la frase y verificar que cada lugar quede dentro del anterior."),
    reinforce="Cuéntale a un adulto dónde vives usando la ruta: país, región y localidad.",
    extend="Escribe dos rutas distintas, una del norte y otra del sur de Chile, usando localidades que ya conoces de este cuaderno.",
)

# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="Este cuaderno y un lápiz. Los paisajes están descritos con palabras en cada ejercicio.",
    use="Aprenderé el vocabulario del paisaje: país, ciudad, pueblo, camino, construcciones, cordillera, mar, vegetación y desierto. Sirve para describir lo que veo con palabras exactas.",
    prior=["Sé qué es un lugar.", "Sé distinguir cosas de la naturaleza y cosas que hacen las personas."],
    explain=[
        "Un paisaje es lo que ves cuando miras un lugar: montañas, casas, árboles, caminos. Para describirlo bien usamos palabras precisas. La cordillera es una fila de montañas altas. El mar es agua salada muy grande. La vegetación son las plantas del lugar: pasto, arbustos y árboles.",
        "El desierto es un lugar donde llueve muy poco y hay poca vegetación. Hay construcciones cuando las personas hacen casas, puentes o escuelas. Un camino une un lugar con otro. Un pueblo es un lugar pequeño con pocas casas y una ciudad es un lugar grande con muchas casas, calles y edificios.",
        "Algunas cosas del paisaje son naturales, como el mar, la cordillera y la vegetación. Otras las hacen las personas, como el camino y las construcciones. Cuando describes, usa estas palabras en vez de decir solo «cosas».",
    ],
    vocab=[("paisaje", "lo que se ve al mirar un lugar"), ("vegetación", "las plantas de un lugar"), ("construcciones", "casas, puentes y edificios que hacen las personas"), ("camino", "franja por donde se va de un lugar a otro"), ("desierto", "lugar con muy poca lluvia y pocas plantas")],
    worked=[
        W("Nombrar lo que veo", "Paisaje A: «Al fondo hay una fila de montañas altas con nieve. Más cerca hay un camino de tierra y tres casas pequeñas. Hay pasto y árboles». ¿Qué palabras del vocabulario sirven?",
          ["La fila de montañas altas se llama cordillera.", "El camino de tierra es un camino.", "Las casas son construcciones; pasto y árboles son vegetación."], "Cordillera, camino, construcciones y vegetación"),
        W("Natural o hecho por personas", "En el paisaje A, ¿el camino es natural o lo hicieron personas?",
          ["Los caminos se hacen para ir de un lugar a otro.", "Los árboles y las montañas existen sin que las personas las hagan.", "El camino lo hicieron las personas."], "Lo hicieron las personas"),
    ],
    mistakes=[
        M("Llamar «ciudad» a un lugar con cinco casas.", "Se confunden pueblo y ciudad por el tamaño.", "Con pocas casas es un pueblo; con muchas calles y edificios, una ciudad."),
        M("Decir que el desierto tiene muchas plantas.", "Se olvida la poca lluvia.", "El desierto tiene pocas plantas porque casi no llueve."),
    ],
    tiers=tiers(
        [ex("¿Cómo se llama el conjunto de plantas de un lugar?", "Vegetación", "La vegetación incluye pasto, arbustos y árboles."),
         ex("¿Cómo se llama una fila larga de montañas altas?", "Cordillera", "Una cordillera es una fila de montañas."),
         ex("Un lugar con muy poca lluvia y casi sin plantas, ¿qué es?", "Un desierto", "Esa es la descripción de un desierto.")],
        [ex("¿Cuál de estas cosas es una construcción: una casa, un cerro o una nube?", "Una casa", "Las personas hacen las casas."),
         ex("¿Para qué sirve un camino?", "Para ir de un lugar a otro", "Une dos lugares."),
         ex("¿Cuál es más grande: un pueblo o una ciudad?", "Una ciudad", "La ciudad tiene muchas más casas y calles.")],
        [ex("Paisaje B: «Hay arena y piedras hasta donde llega la vista, casi no hay plantas y casi nunca llueve». ¿Qué tipo de lugar es?", "Un desierto", "Hay poca vegetación y poca lluvia."),
         ex("Paisaje C: «Hay un puente, una escuela, un camino de asfalto y un mercado». Nombra dos construcciones.", "El puente y la escuela (o el mercado)", "Son cosas que construyeron las personas."),
         ex("Paisaje D: «Hay agua salada hasta el horizonte y una playa con arena». ¿Qué parte del paisaje es el agua?", "El mar", "El agua salada muy grande es el mar.")],
        [ex("Daniel dice que una cordillera la hicieron las personas. ¿Tiene razón?", "No; es natural", "Las montañas no las construyen las personas."),
         ex("Lucía dice que un lugar con 4 casas y una plaza es una ciudad. ¿Qué palabra era mejor?", "Pueblo", "Con pocas casas, un lugar es un pueblo.")],
        [ex("En la lista «cordillera, puente, mar, escuela, desierto, camino» ¿cuántos son naturales?", "3: cordillera, mar y desierto", "El puente, la escuela y el camino los hacen las personas."),
         ex("¿Puede haber un camino en un desierto? Explica.", "Sí; las personas lo hacen para cruzarlo", "Un camino lo hacen las personas, y pueden hacerlo en cualquier lugar.")],
    ),
    context=[ex("En la plaza de un pueblo Pilar mira y dice: «Veo una iglesia, un camino de tierra, árboles y al fondo una cordillera». Clasifica: ¿cuál es vegetación?", "Los árboles", "Los árboles son las plantas del lugar.")],
    selfcheck=[ex("Escribe una palabra que sea una construcción.", "Casa, puente, escuela o edificio", "Todas las hacen las personas."), ex("¿Qué es la vegetación?", "Las plantas de un lugar", "Pasto, arbustos y árboles."), ex("¿El mar es natural o construido?", "Natural", "Las personas no lo hacen.")],
    open_task=task("Lee este paisaje: «Al fondo hay una cordillera nevada. Abajo hay un pueblo con una escuela y diez casas. Un camino de tierra baja hasta el mar. Hay árboles cerca de las casas». Dibújalo y escribe una lista con estas palabras: cordillera, pueblo, construcciones, camino, mar, vegetación.", "Dibujé arriba la cordillera, abajo el pueblo y el camino hasta el mar. Lista: cordillera, pueblo (escuela y casas), construcciones, camino, mar, vegetación (árboles).", ["incluye las seis palabras", "el dibujo coincide con el texto", "separa lo natural de lo construido"], ["dibujo", "lista de seis palabras"], ["llamar ciudad al pueblo", "olvidar la vegetación"], "Pide señalar en el dibujo dónde está cada palabra de la lista."),
    reinforce="Asómate a una ventana o puerta y di tres palabras del vocabulario que describan lo que ves.",
    extend="Escribe dos frases que describan un paisaje con desierto y otras dos con vegetación abundante.",
)

register(
    OA10, 2,
    materials="Este cuaderno y un lápiz. También puedes usar cuatro objetos de tu casa (taza, cuchara, plato y lápiz) para practicar.",
    use="Aprenderé a ubicar cosas con las palabras derecha, izquierda, delante, detrás y entre. Sirve para explicar dónde está algo sin señalarlo.",
    prior=["Sé cuál es mi mano derecha y mi mano izquierda.", "Sé nombrar cosas de un paisaje."],
    explain=[
        "La ubicación relativa dice dónde está una cosa en relación con otra. «A la derecha» es hacia el lado de tu mano derecha. «A la izquierda» es hacia el lado de tu mano izquierda. Cuando miras un dibujo de frente, tu derecha es la derecha del dibujo.",
        "«Delante de» significa más cerca de ti y «detrás de» significa más lejos. «Entre» significa en medio de dos cosas. Si en una fila hay una casa, un árbol y una escuela, el árbol está entre la casa y la escuela.",
        "Una buena descripción nombra una cosa de referencia. No basta con decir «está a la derecha». Debes decir «a la derecha de la casa». Así la otra persona sabe de dónde mirar.",
    ],
    vocab=[("ubicación relativa", "dónde está algo en relación con otra cosa"), ("derecha", "el lado de tu mano derecha, contrario a la izquierda"), ("izquierda", "el lado contrario a la derecha"), ("delante, detrás", "más cerca o más lejos de mí"), ("entre", "en medio de dos cosas")],
    worked=[
        W("Entre dos cosas", "En una calle, de izquierda a derecha, hay: panadería, escuela, plaza. ¿Qué queda entre la panadería y la plaza?",
          ["Miro la fila de izquierda a derecha.", "Primero está la panadería y al final la plaza.", "En el medio está la escuela."], "La escuela"),
        W("Delante y detrás", "En una foto hay dos filas. Delante, de izquierda a derecha: un perro y un gato. Detrás, de izquierda a derecha: un árbol y una casa. ¿Qué hay detrás del perro?",
          ["Las cosas que están lejos de mí son las de detrás.", "El perro está a la izquierda en la fila de adelante.", "Justo detrás, a la izquierda, está el árbol."], "El árbol"),
    ],
    mistakes=[
        M("Decir «está a la derecha» sin nombrar la cosa de referencia.", "La frase no dice a la derecha de qué.", "Di «a la derecha de la casa»."),
        M("Confundir la izquierda con la derecha cuando miro un dibujo.", "Se mira desde otro lado.", "Mira el dibujo de frente: tu derecha es la derecha del dibujo."),
    ],
    tiers=tiers(
        [ex("En una fila de izquierda a derecha hay: árbol, casa, escuela. ¿Qué cosa está a la izquierda de todas?", "El árbol", "Es la primera de izquierda a derecha."),
         ex("En la misma fila: árbol, casa, escuela. ¿Qué cosa está a la derecha de todas?", "La escuela", "Es la última de izquierda a derecha."),
         ex("¿Qué palabra usas para decir que algo está en el medio de dos cosas?", "Entre", "«Entre» se usa para algo ubicado en medio.")],
        [ex("¿Qué quiere decir «delante de»?", "Más cerca de mí", "Lo de adelante queda más cerca de quien mira."),
         ex("¿Qué quiere decir «detrás de»?", "Más lejos de mí", "Lo de atrás queda más lejos de quien mira."),
         ex("¿Por qué hay que nombrar una cosa de referencia, como «a la derecha de la casa»?", "Para que se sepa desde dónde mirar", "Sin referencia, la ubicación no se entiende.")],
        [ex("En una fila de izquierda a derecha hay: puente, camino, casa, árbol. ¿Qué hay entre el camino y el árbol?", "La casa", "Está en el medio de los dos."),
         ex("Dos filas: delante están una vaca y un caballo; detrás están una montaña y un lago. ¿Qué hay detrás de la vaca y el caballo?", "La montaña y el lago", "Son la fila lejana."),
         ex("En una plaza, de izquierda a derecha hay: pileta, banca, árbol, farol, quiosco. ¿Qué queda a la izquierda del árbol?", "La banca (y la pileta)", "Antes del árbol vienen la banca y la pileta.")],
        [ex("Ema dice que el árbol está a la derecha. Un dibujo muestra de izquierda a derecha: árbol, casa. ¿Qué error cometió?", "El árbol está a la izquierda de la casa", "El árbol aparece primero, a la izquierda."),
         ex("Beto dice «la escuela está entre la casa y el parque» pero en el dibujo está después del parque. ¿Qué dijo mal?", "La escuela no está en el medio", "Entre significa en el centro de las dos cosas.")],
        [ex("Si me doy vuelta y miro hacia el lado contrario, lo que antes estaba a mi derecha ahora está a mi...", "Izquierda", "Al dar media vuelta se cambian los lados."),
         ex("En una fila de tres: A, B y C, de izquierda a derecha. Si cambio de lugar A y C, ¿qué queda entre ellas?", "B", "El del medio sigue en el medio.")],
    ),
    context=[ex("Un niño explica dónde está su casa: «De izquierda a derecha en mi calle: el almacén, mi casa y la capilla». ¿Qué está a la derecha de su casa?", "La capilla", "Después de su casa, a la derecha, viene la capilla.")],
    selfcheck=[ex("En una fila de izquierda a derecha hay: sol, nube, luna. ¿Cuál queda entre las otras dos?", "La nube", "Está en el medio de las otras dos."), ex("¿Qué palabra significa «más lejos de mí»?", "Detrás", "Detrás indica lo que está más lejos."), ex("¿Qué debe llevar siempre una buena ubicación?", "Una cosa de referencia", "Sin referencia no se entiende desde dónde.")],
    open_task=task("Mira este dibujo escrito: «Fila de atrás: una cordillera en el centro. Fila del medio: una casa a la izquierda y una escuela a la derecha. Fila de adelante: una banca a la izquierda, un árbol en el medio y un perro a la derecha». Dibuja el paisaje y escribe cuatro frases con las palabras: izquierda, derecha, detrás y entre.", "La cordillera está detrás de la casa y la escuela. La casa está a la izquierda de la escuela. El árbol está entre la banca y el perro. El perro está a la derecha del árbol.", ["usa las cuatro palabras", "nombra la cosa de referencia", "coincide con el dibujo"], ["dibujo", "cuatro frases"], ["olvidar la referencia", "confundir izquierda y derecha"], "Pide señalar en el dibujo cada frase para comprobar que sea cierta."),
    reinforce="Pon tres objetos en fila sobre una mesa y describe dónde está cada uno usando entre, derecha e izquierda.",
    extend="Escribe una frase que ubique tu zapato usando una cosa de referencia que esté en tu pieza.",
)

register(
    OA10, 3,
    materials="Este cuaderno y un lápiz. Si quieres, observa por una ventana o en el patio, pero las descripciones que necesitas están escritas.",
    use="Aprenderé a describir un paisaje local con vocabulario geográfico y ubicación relativa. Sirve para contarle a otra persona cómo es el lugar donde vivo.",
    prior=["Sé las palabras cordillera, mar, vegetación y camino.", "Sé usar derecha, izquierda, delante, detrás y entre."],
    explain=[
        "Un paisaje local es el paisaje de tu entorno: tu calle, tu plaza, tu escuela o tu pueblo. Para describirlo, observa primero qué hay y luego dónde está cada cosa. Primero nombras, después ubicas.",
        "Una descripción sigue pasos: 1) dices qué lugar es, 2) nombras lo natural, como árboles, cerros o el mar, 3) nombras lo construido, como casas, calles o puentes, y 4) ubicas cada cosa con palabras como a la derecha, detrás o entre. Por ejemplo: «En mi plaza hay árboles a la izquierda, una pileta en el centro y casas detrás».",
        "Una buena descripción se entiende sin ver el lugar. Por eso usa palabras exactas y evita «cosas» o «por ahí». Si alguien lee tu descripción, debería poder dibujar tu paisaje casi igual al real.",
    ],
    vocab=[("paisaje local", "el paisaje del lugar donde vivo"), ("natural", "lo que existe sin que lo hagan las personas"), ("construido", "lo que hacen las personas"), ("describir", "decir cómo es algo con palabras"), ("entorno", "lo que rodea un lugar")],
    worked=[
        W("Describir una plaza", "Veo una plaza con una pileta en el centro, árboles a la izquierda y casas detrás. ¿Cómo la describo en una frase?",
          ["Digo qué lugar es: una plaza.", "Nombro lo que hay: pileta, árboles y casas.", "Los ubico: la pileta en el centro, los árboles a la izquierda y las casas detrás."], "En la plaza hay una pileta en el centro, árboles a la izquierda y casas detrás"),
        W("Clasificar lo que hay", "En mi calle hay: casas, un cerro, un poste de luz, un canal y árboles. ¿Qué es natural?",
          ["Las casas y el poste los hicieron las personas.", "El cerro y los árboles son de la naturaleza.", "El canal de la calle lo hicieron las personas."], "El cerro y los árboles"),
    ],
    mistakes=[
        M("Nombrar cosas sin decir dónde están.", "La descripción no se puede dibujar.", "Añade una ubicación para cada cosa: a la derecha, detrás, entre."),
        M("Mezclar lo natural con lo construido en la misma lista sin ordenar.", "No se distingue qué hizo la naturaleza.", "Haz dos listas: natural y construido."),
    ],
    tiers=tiers(
        [ex("En mi escuela hay: patio, árboles, sala y reja. ¿Cuál es la vegetación?", "Los árboles", "Los árboles son plantas."),
         ex("En mi escuela hay: patio, árboles, sala y reja. ¿Cuáles son construcciones?", "Sala y reja (y el patio)", "Las personas las hacen."),
         ex("¿Qué se dice primero al describir un paisaje: qué lugar es o dónde está cada cosa?", "Qué lugar es", "Primero se presenta el lugar.")],
        [ex("¿Por qué una descripción no debe decir «hay cosas por ahí»?", "Porque no dice qué ni dónde", "No se puede imaginar el lugar."),
         ex("Después de nombrar lo que hay, ¿qué paso sigue al describir?", "Ubicar cada cosa", "Se dice dónde está."),
         ex("¿Para qué sirve describir con palabras exactas?", "Para que otro pueda imaginar o dibujar el lugar", "Las palabras exactas permiten dibujar el paisaje.")],
        [ex("Texto: «En mi pueblo, a la izquierda está la cordillera, a la derecha el mar y en medio las casas». ¿Qué hay entre la cordillera y el mar?", "Las casas", "Están en el medio."),
         ex("Texto: «Mi calle tiene árboles delante de las casas y un cerro detrás». ¿Qué está más lejos de mí?", "El cerro", "Detrás significa más lejos."),
         ex("Texto: «En la plaza, la pileta queda a la derecha de la banca y a la izquierda del quiosco». Ordena de izquierda a derecha.", "Banca, pileta, quiosco", "La pileta está en medio.")],
        [ex("Mica describió su patio: «Hay cosas bonitas». ¿Qué le falta a esa descripción?", "Nombrar qué hay y dónde", "Dice una opinión, no lo que se ve."),
         ex("Teo dice que el cerro de su calle es construido. ¿Está bien?", "No; es natural", "El cerro no lo hicieron las personas.")],
        [ex("Ordena los pasos de una descripción: ubicar cada cosa, decir qué lugar es, nombrar lo natural y lo construido.", "Decir qué lugar es; nombrar lo natural y lo construido; ubicar cada cosa", "Primero se presenta, luego se nombra y al final se ubica."),
         ex("Escribe una frase con un lugar y dos cosas ubicadas. Ejemplo para completar: «En el patio, ____ está a la ____ del ____».", "Por ejemplo: En el patio, el árbol está a la derecha de la sala", "Debe tener una cosa y su referencia.")],
    ),
    context=[ex("Nico describe el pueblo de su abuela por teléfono: «Tiene una plaza con cuatro árboles, una iglesia detrás de la plaza y un camino a la izquierda». ¿Qué hay detrás de la plaza?", "Una iglesia", "Detrás significa más lejos de quien mira.")],
    selfcheck=[ex("¿Qué hace natural a una cosa?", "Que existe sin que la hagan las personas", "Cerros, mar y árboles son naturales."), ex("¿Qué dos pasos usa una descripción?", "Nombrar y ubicar", "Se dice qué hay y dónde."), ex("Escribe una cosa construida que veas en tu calle.", "Casa, poste, reja, puente o calle", "Todas las hacen las personas.")],
    open_task=task("Lee este paisaje local: «Calle de un pueblo: a la izquierda hay un almacén y dos árboles; en el centro está la plaza con una pileta; a la derecha hay una escuela; detrás de todo se ve un cerro». Escribe una descripción de cuatro frases: el lugar, lo natural, lo construido y dónde está cada cosa. Después, si quieres, haz lo mismo con tu propia calle.", "Es la calle de un pueblo. Lo natural son los árboles y el cerro. Lo construido es el almacén, la pileta y la escuela. A la izquierda están el almacén y los árboles, la plaza está en el centro y el cerro está detrás.", ["nombra lugar, natural y construido", "ubica con derecha, izquierda, detrás o entre", "se puede dibujar a partir del texto"], ["cuatro frases", "dibujo opcional"], ["no ubicar", "mezclar natural y construido"], "Pide dibujar solo con la descripción y comparar con el texto original."),
    reinforce="Describe en voz alta el lugar donde estás ahora usando dos palabras de ubicación.",
    extend="Compara la descripción de tu calle con la de la calle del texto y nombra una cosa igual y otra distinta.",
)

register(
    OA10, 4,
    materials="Este cuaderno y un lápiz. Los dos paisajes están descritos con palabras.",
    use="Aprenderé a comparar dos paisajes de Chile y a decir en qué se parecen y en qué se diferencian. Sirve para entender que los lugares de un mismo país pueden ser muy distintos.",
    prior=["Sé describir un paisaje local.", "Sé usar el vocabulario del paisaje."],
    explain=[
        "Comparar es mirar dos cosas y decir en qué se parecen y en qué se diferencian. Para comparar paisajes usa las mismas preguntas en los dos: ¿hay montañas?, ¿hay mar?, ¿hay plantas?, ¿cómo son las construcciones? Así comparas lo mismo con lo mismo.",
        "En Chile hay paisajes muy distintos. En el norte hay zonas de desierto, como el desierto de Atacama, donde llueve muy poco y hay pocas plantas. En el sur hay bosques con árboles altos, lagos y mucha lluvia. Los dos paisajes están en Chile, pero no se ven iguales.",
        "Al comparar, usa palabras como «los dos tienen» y «en cambio». Por ejemplo: «Los dos paisajes tienen una cordillera, pero el desierto tiene pocas plantas, en cambio el bosque tiene muchos árboles».",
    ],
    vocab=[("comparar", "decir en qué se parecen y en qué se diferencian dos cosas"), ("semejanza", "algo que tienen igual"), ("diferencia", "algo que no es igual"), ("lluvia", "agua que cae del cielo"), ("en cambio", "palabra para marcar una diferencia")],
    worked=[
        W("Semejanza y diferencia", "Paisaje 1 (norte): arena y piedras, casi sin plantas, poca lluvia, un pueblo de casas bajas y una cordillera al fondo. Paisaje 2 (sur): bosque verde, lago, mucha lluvia, casas con techo inclinado y una cordillera al fondo. ¿Qué tienen igual?",
          ["Reviso lo mismo en los dos.", "Los dos tienen una cordillera al fondo.", "Los dos tienen casas."], "Una cordillera al fondo y casas"),
        W("Una diferencia", "Con los mismos paisajes, ¿en qué se diferencian sus plantas?",
          ["El paisaje 1 casi no tiene plantas.", "El paisaje 2 tiene un bosque verde.", "Uso «en cambio»."], "El paisaje 1 tiene pocas plantas; en cambio el 2 tiene muchos árboles"),
    ],
    mistakes=[
        M("Decir solo lo que tiene un paisaje.", "No se compara con el otro.", "Revisa lo mismo en los dos y escribe la semejanza o la diferencia."),
        M("Creer que todo Chile se ve igual.", "Se piensa en un solo paisaje.", "Chile tiene desierto, bosques, cordillera y mar."),
    ],
    tiers=tiers(
        [ex("Paisaje X: desierto con poca lluvia. Paisaje Y: bosque con mucha lluvia. ¿En cuál llueve más?", "En el bosque", "El bosque recibe más lluvia que el desierto."),
         ex("Paisaje X tiene cordillera y Paisaje Y tiene cordillera. ¿Es una semejanza o una diferencia?", "Una semejanza", "Los dos tienen lo mismo."),
         ex("Paisaje X tiene mar y Paisaje Y no tiene mar. ¿Es una semejanza o una diferencia?", "Una diferencia", "Uno lo tiene y el otro no.")],
        [ex("Para comparar, ¿conviene hacer las mismas preguntas a los dos paisajes?", "Sí", "Así se compara lo mismo con lo mismo."),
         ex("¿Qué palabra sirve para marcar una diferencia: «los dos» o «en cambio»?", "En cambio", "Marca algo que no es igual."),
         ex("¿Los paisajes de un mismo país pueden ser muy distintos?", "Sí", "Chile tiene desierto y bosques.")],
        [ex("Paisaje 1: arena, sin árboles, casas bajas. Paisaje 2: pasto, árboles, casas con techo inclinado. ¿Qué paisaje tiene vegetación abundante?", "El 2", "Tiene pasto y árboles."),
         ex("Paisaje 1 tiene una escuela y un camino. Paisaje 2 tiene una escuela y un puente. ¿Qué tienen igual?", "Una escuela", "Aparece en los dos."),
         ex("Paisaje 1 tiene mar y playa. Paisaje 2 tiene cordillera nevada. ¿Cuál es un paisaje de montaña?", "El 2", "La cordillera nevada es de montaña.")],
        [ex("Ana dice: «El desierto es más bonito». ¿Es una semejanza, una diferencia o una opinión?", "Una opinión", "No se puede comprobar mirando el paisaje."),
         ex("Pedro dice que, como el desierto de Atacama está en Chile, todo Chile es desierto. ¿Qué error comete?", "Cree que todo Chile es igual; tiene muchos paisajes", "Un lugar no representa a todo el país.")],
        [ex("Escribe una semejanza y una diferencia entre un desierto y un bosque.", "Por ejemplo: los dos pueden tener cordillera; el desierto tiene pocas plantas y el bosque muchas", "Compara lo mismo en los dos."),
         ex("Hay un paisaje con mar, un puente y casas, y otro con mar, lago y árboles. ¿Cuál es la semejanza?", "Los dos tienen mar", "Aparece en los dos.")],
    ),
    context=[ex("Mía viajó del norte al sur de Chile. En el norte vio arena y pocas plantas; en el sur vio bosque y lluvia. Ella dice: «Es el mismo paisaje». ¿Tiene razón?", "No; son paisajes distintos", "Cambian la vegetación y la lluvia.")],
    selfcheck=[ex("En Historia, ¿qué es una semejanza?", "Algo que tienen igual", "Es lo que se repite en los dos."), ex("En Historia, ¿qué es una diferencia?", "Algo que no es igual", "Uno lo tiene distinto al otro."), ex("¿En qué paisaje llueve menos: desierto o bosque?", "Desierto", "El desierto casi no recibe lluvia.")],
    open_task=task("Compara estos dos paisajes escritos: PAISAJE A (norte): arena y piedras, casi sin plantas, una cordillera al fondo, un pueblo pequeño de casas bajas, casi nunca llueve. PAISAJE B (sur): bosque de árboles altos, un lago, mucha lluvia, una cordillera nevada al fondo, casas con techo inclinado. Escribe dos semejanzas y dos diferencias, usando «los dos tienen» y «en cambio».", "Los dos tienen una cordillera al fondo y los dos tienen casas. El paisaje A casi no tiene plantas, en cambio el B tiene un bosque. En el A casi no llueve, en cambio en el B llueve mucho.", ["dos semejanzas", "dos diferencias", "usa «en cambio»"], ["cuatro frases"], ["describir un solo paisaje", "dar opiniones"], "Pide señalar en el texto cada dato usado y evitar frases con «es más bonito»."),
    reinforce="Elige un lugar que conozcas y compáralo con el desierto o el bosque de este cuaderno, diciendo una semejanza.",
    extend="Escribe una pregunta que sirva para comparar dos paisajes cualquiera y respóndela para los dos paisajes del texto.",
)

register(
    OA10, 5,
    materials="Este cuaderno, un lápiz y una hoja para dibujar. El croquis está escrito en un cuadro de palabras.",
    use="Aprenderé a leer y hacer un croquis comentado, un dibujo simple de un lugar visto desde arriba con frases que explican dónde está cada cosa. Sirve para guiar a alguien a un lugar.",
    prior=["Sé usar derecha, izquierda, delante, detrás y entre.", "Sé describir un paisaje local."],
    explain=[
        "Un croquis es un dibujo simple de un lugar visto desde arriba. No necesita ser perfecto, pero sí claro: usa cuadros para los lugares y flechas para los caminos. Se parece a un mapa pequeño y hecho a mano.",
        "Un croquis comentado lleva frases escritas al lado. Cada frase dice dónde está un lugar con palabras de ubicación: «La panadería está a la izquierda de la calle», «La plaza está entre la escuela y la biblioteca». Los comentarios ayudan a quien lo lee.",
        "Para leer un croquis, parte de un lugar que conozcas y muévete: «Desde la escuela, la biblioteca está a la izquierda». Un buen croquis tiene títulos, un norte (una N con una flecha) y pocos detalles.",
    ],
    vocab=[("croquis", "dibujo simple de un lugar visto desde arriba"), ("comentario", "frase que explica algo del dibujo"), ("referencia", "lugar conocido que sirve para guiarse"), ("flecha", "signo que muestra por dónde ir"), ("norte (N)", "marca que indica hacia dónde queda el norte")],
    worked=[
        W("Leer un croquis", "Croquis (3 filas, de izquierda a derecha). Fila de arriba: Biblioteca, Plaza, Escuela. Fila del medio: Panadería, Calle, Consultorio. Fila de abajo: Casa de Ana, Árbol, Cancha. ¿Qué lugar está entre la Biblioteca y la Escuela?",
          ["Miro la fila de arriba de izquierda a derecha.", "La Biblioteca está primero y la Escuela al final.", "En el medio está la Plaza."], "La Plaza"),
        W("Escribir un comentario", "Con el mismo croquis, ¿cómo comento dónde está el Consultorio?",
          ["Busco una cosa de referencia: la Calle.", "El Consultorio está a la derecha de la Calle.", "Escribo la frase con la referencia."], "El Consultorio está a la derecha de la Calle"),
    ],
    mistakes=[
        M("Dibujar el croquis de frente, como una foto.", "Un croquis se ve desde arriba.", "Dibuja cuadros y caminos como si miraras desde un techo alto."),
        M("Escribir comentarios sin referencia, como «está allá».", "No se entiende dónde.", "Di «a la derecha de la Calle» o «entre la Biblioteca y la Escuela»."),
    ],
    tiers=tiers(
        [ex("Croquis de tres filas: arriba Biblioteca, Plaza, Escuela; en medio Panadería, Calle, Consultorio; abajo Casa de Ana, Árbol, Cancha. ¿Qué lugar está en el centro del croquis?", "La Calle", "Está en el medio de la fila del medio."),
         ex("En el mismo croquis, ¿qué lugar está a la izquierda de la Plaza?", "La Biblioteca", "Es el primer lugar de la fila de arriba."),
         ex("En el mismo croquis, ¿qué lugar está a la derecha del Árbol?", "La Cancha", "En la fila de abajo, la Cancha viene después del Árbol.")],
        [ex("¿Un croquis se dibuja de frente o visto desde arriba?", "Visto desde arriba", "Se parece a un mapa pequeño."),
         ex("¿Qué es un comentario en un croquis?", "Una frase que explica dónde está un lugar", "Ayuda a leer el dibujo."),
         ex("¿Qué marca indica hacia dónde queda el norte?", "Una N con una flecha", "Así se orientan los mapas.")],
        [ex("Con el croquis de la Plaza y la Calle: ¿qué lugar está debajo de la Plaza, en la fila del medio?", "La Calle", "La Calle está en la columna del centro, bajo la Plaza."),
         ex("Con el mismo croquis: ¿qué lugar está encima de la Casa de Ana?", "La Panadería", "Está en la misma columna, arriba."),
         ex("Con el mismo croquis: Ana sale de su casa y va hacia arriba dos lugares. ¿Dónde llega?", "A la Biblioteca", "Sube desde la Casa de Ana a la Panadería y luego a la Biblioteca.")],
        [ex("Laura escribió «La Escuela queda a la izquierda de la Plaza». Según el croquis, ¿qué error cometió?", "La Escuela está a la derecha de la Plaza", "En la fila de arriba la Escuela viene después de la Plaza."),
         ex("Joaquín dice que la Cancha está entre el Árbol y la Casa de Ana. ¿Es cierto?", "No; el Árbol está entre ellas", "En la fila de abajo el orden es Casa de Ana, Árbol, Cancha.")],
        [ex("Escribe un comentario para la Panadería con una referencia del croquis.", "Por ejemplo: la Panadería está a la izquierda de la Calle", "Dice dónde está y respecto de qué."),
         ex("Escribe un comentario para la Cancha con una referencia del croquis.", "Por ejemplo: la Cancha está a la derecha del Árbol", "Dice dónde está y respecto de qué.")],
    ),
    context=[ex("Un niño nuevo debe llegar de la Escuela a la Cancha usando el croquis de arriba. Dice «bajo dos filas y estoy ahí». ¿Llegó bien a la Cancha?", "Sí; desde la Escuela, dos filas hacia abajo, queda la Cancha", "Bajó desde la fila de arriba hasta la fila de abajo, en la columna derecha.")],
    selfcheck=[ex("¿Desde dónde se ve un croquis?", "Desde arriba", "Así se muestran los lugares y caminos."), ex("En el croquis, ¿qué lugar está arriba de la Calle?", "La Plaza", "Está encima de la Calle."), ex("¿Qué debe llevar un buen comentario?", "Una referencia", "Dice a la derecha de qué o entre qué.")],
    open_task=task("Haz un croquis comentado de este lugar: una manzana con la Escuela arriba a la izquierda, la Plaza arriba a la derecha, la Calle en el medio, un Quiosco abajo a la izquierda y una Pileta abajo a la derecha. Usa cuadros, pon una N en una esquina y escribe tres comentarios con las palabras: izquierda, derecha y entre.", "Dibujé cuadros: Escuela y Plaza arriba, Calle en el medio, Quiosco y Pileta abajo. Comentarios: La Escuela está a la izquierda de la Plaza. La Pileta está a la derecha del Quiosco. La Calle está entre las filas de arriba y de abajo.", ["dibujo visto desde arriba", "cinco lugares bien ubicados", "tres comentarios con referencia", "tiene la N"], ["croquis", "tres frases"], ["dibujar de frente", "comentarios sin referencia"], "Pide a otra persona seguir las frases para ver si puede ubicar cada lugar sin mirar el dibujo."),
    reinforce="Dibuja un croquis de tu pieza con cuatro objetos y escribe dos comentarios.",
    extend="Agrega al croquis un cuarto comentario que use la palabra «detrás» o «delante» con una referencia.",
)

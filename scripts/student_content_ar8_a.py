"""Cuaderno del estudiante de 8.º básico Artes Visuales: AR08 OA 01 (crear trabajos visuales sobre la relación entre personas, naturaleza y medioambiente)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR08 OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- Clase 1
lesson(
    OA1, 1,
    "Hojas, lápiz de mina, lápices de colores y restos limpios de papel de diario o de revista. Los tres referentes están descritos en esta clase; no necesitas buscarlos.",
    "Aprenderé a observar una obra sobre personas, naturaleza y medioambiente, a distinguir copiar de reinterpretar y a tomar una decisión visual propia. Sirve para crear sin repetir lo que otra persona ya hizo.",
    ["Sé registrar en una bitácora detalles que se ven, una pregunta y una posibilidad.", "Sé que una obra comunica una intención con color, forma, material y composición."],
    [
        "Un referente es una obra, imagen o práctica que observo para aprender de ella. Cuando el tema es la relación entre personas, naturaleza y medioambiente, me fijo en cómo la muestra: cuidado, uso, convivencia, daño o cambio. El medioambiente es el conjunto de elementos naturales y humanos que rodean a los seres vivos, como el agua, el aire, el suelo y las ciudades.",
        "Copiar es repetir las formas, los colores y la composición de otra obra. Reinterpretar es tomar un recurso del referente, por ejemplo la escala exagerada, el material o el punto de vista, y cambiar lo demás para decir algo mío. La escala es el tamaño de un elemento comparado con los otros. Siempre anoto de dónde viene el referente: esa es su procedencia.",
        "Una obra muestra un solo punto de vista. Un mural sobre un río no representa por sí solo cómo toda una comunidad se relaciona con la naturaleza: es lo que su autor o autora decidió mostrar. Tampoco basta repetir símbolos ambientales muy usados, como el planeta con manos; pregunto qué significan en mi obra. Termino cada observación con dos detalles, una pregunta y una posibilidad propia.",
    ],
    [("referente", "obra, imagen o práctica que se observa para aprender de ella"), ("reinterpretar", "tomar un recurso de un referente y cambiar lo demás para decir algo propio"), ("escala", "tamaño de un elemento comparado con los otros de la obra"), ("medioambiente", "conjunto de elementos naturales y humanos que rodean a los seres vivos"), ("procedencia", "lugar o autoría de donde viene un referente")],
    [
        w("Copia o reinterpretación", "Referente de ejemplo: un dibujo con tiza en una vereda, que muestra una raíz gigante saliendo de una alcantarilla. Paula dibuja con tiza en su vereda una raíz gigante que sale de una alcantarilla. Quique toma la idea de «usar el suelo de la calle como soporte» y dibuja con tiza unas ramas que nacen de un poste. ¿Quién copia y quién reinterpreta?", ["Paula repite la figura, el objeto y el lugar: no cambia ninguna decisión.", "Quique conserva solo un recurso, el suelo de la calle como soporte.", "Quique cambia la figura y el objeto del que nace."], "Paula copia; Quique reinterpreta"),
        w("Registro de bitácora", "Referente de ejemplo: una pintura de un pescador visto desde arriba, con la red formando un círculo que ocupa casi todo el cuadro. Registra dos detalles, una pregunta y una posibilidad.", ["Detalle 1: el pescador se ve desde arriba.", "Detalle 2: la red forma un círculo que ocupa casi todo el cuadro.", "Pregunta: ¿por qué el autor eligió verlo desde arriba?", "Posibilidad: dibujar desde arriba a una persona que riega, con la manguera formando un círculo."], "Dos detalles (vista desde arriba, red en círculo), una pregunta sobre el punto de vista y una posibilidad propia que toma el recurso sin copiar la escena"),
    ],
    [
        m("Cambiar solo el tamaño o el color del referente y creer que la obra ya es propia.", "La composición y la idea siguen siendo las de otra persona.", "Cambia al menos una decisión de fondo: el objeto, el material, el punto de vista o el mensaje."),
        m("Afirmar que un mural muestra cómo toda una comunidad se relaciona con la naturaleza.", "Una obra solo muestra lo que su autor o autora decidió mostrar.", "Habla de lo que se ve en esa obra y de su procedencia, sin hablar por toda la comunidad."),
    ],
    [
        ex("El mural de ejemplo muestra a un niño que riega una planta más alta que un edificio. Un compañero dibuja ese mismo niño con la misma planta, en los mismos colores, pero en una hoja más pequeña. ¿Copia o reinterpreta?", "Copia", "Solo cambia el tamaño de la hoja; las formas, los colores y la composición siguen iguales."),
        ex("En Artes Visuales, ¿cómo se llama la obra o imagen que observas para aprender de ella antes de crear la tuya?", "Referente", "Es el punto de partida que se observa sin repetirlo."),
        ex("Observaste una serie de ejemplo: cuatro fotos de la misma quebrada, tomadas desde el mismo punto en distintas estaciones. ¿Cuál es una posibilidad expresiva propia a partir de ella? A. «Dibujaré mi patio desde la misma ventana en tres momentos del día» B. «Pintaré la quebrada igual que en las fotos».", "A", "Toma el recurso del mismo punto de vista y lo aplica a un lugar propio; la otra opción repite el motivo."),
    ],
    [
        ex("Un afiche de ejemplo usa hojas secas pegadas para formar una mano. ¿Qué recurso de ese referente puedes reinterpretar? A. Usar un material natural para formar una figura B. Pegar hojas secas en forma de mano sobre fondo gris.", "A", "Es un recurso que se puede aplicar a otra figura; la otra opción es la obra repetida."),
        ex("Una estudiante escribe: «Este mural muestra cómo toda la comunidad cuida la naturaleza». ¿Qué problema tiene su frase?", "Generaliza a toda la comunidad a partir de una sola obra", "Una obra solo muestra lo que su autor decidió mostrar."),
        ex("Para una obra sobre el agua, ¿cuál propuesta reinterpreta en vez de repetir un símbolo muy usado? A. Dibujar el planeta sostenido por dos manos, como en tantos afiches B. Dibujar el recorrido que hace el agua desde la llave de tu casa hasta el desagüe.", "B", "Parte de una observación propia y no de un símbolo repetido."),
    ],
    [
        ex("Del mural del niño y la planta gigante tomas el recurso de la escala exagerada. ¿Qué decisión lo reinterpreta? A. Dibujar una abeja enorme junto a una casa pequeña B. Dibujar otro niño regando una planta enorme.", "A", "Conserva el recurso de la desproporción, pero cambia el tema y los elementos."),
        ex("Miras un mural de ejemplo: un niño riega una planta más alta que un edificio, y todo está pintado en verdes y amarillos. Tres anotaciones: 1) «Es bonito». 2) «La planta mide más que el edificio». 3) «Los colores son verdes y amarillos». ¿Cuántas son detalles que se pueden comprobar mirando?", "2", "La 2 y la 3 se comprueban mirando; «bonito» es una opinión."),
        ex("Una serie de ejemplo muestra cuatro fotos de la misma quebrada tomadas desde el mismo punto. Quieres tomar ese recurso del punto fijo. ¿Qué acción lo aplica? A. Dibujar la ventana de tu casa en la mañana y en la tarde desde el mismo lugar B. Dibujar cuatro paisajes distintos desde cuatro lugares.", "A", "Mantiene el punto fijo y cambia el momento, como hacen las fotos."),
    ],
    [
        ex("El afiche de ejemplo muestra una mano hecha de hojas secas que sostiene una botella aplastada. Pía copia: usa hojas, mano y botella. Tomás anota: «Me interesa que la figura esté hecha del mismo material que se quiere cuidar; yo armaré un pez con restos de papel reciclado». ¿Quién reinterpreta y qué recurso conservó?", "Tomás; conservó la relación entre el material y el tema", "Toma un recurso y cambia figura y objeto; Pía repite los elementos."),
        ex("Una compañera dice: «Mi obra es propia porque cambié el fondo gris por azul, pero todo lo demás es igual al afiche». ¿Alcanza con cambiar el fondo?", "No", "Cambia un detalle, pero la figura y la composición siguen siendo las del afiche."),
    ],
    [
        ex("Para una obra sobre el aire de tu ciudad eliges un punto de partida. ¿Cuál nace de una observación propia? A. Un planeta con manos B. La ventana de tu pieza con un trozo de cielo dibujado cada día en un tono distinto C. Una nube con cara triste.", "B", "Registra un dato observado por ti; las otras dos son símbolos repetidos."),
        ex("Dos reinterpretaciones de un río contaminado pintado en grises. X) Pintar otro río contaminado en grises, más pequeño. Y) Pintar el mismo punto del río hoy, con tus colores, anotando que es una sola vista y no toda su historia. ¿Cuál cumple los dos cuidados: no copiar y no generalizar?", "Y", "Cambia colores y momento, y reconoce que una vista no muestra toda la historia; X repite la obra."),
    ],
    ex("En tu liceo piden una obra propia sobre el cuidado de una plaza. Tienes de referente un mural de ejemplo en que un niño riega una planta gigante. ¿Qué plan reinterpreta y respeta la procedencia? A. Dibujar el mural completo y firmarlo como propio B. Tomar la escala exagerada, dibujar un banco de la plaza cubierto por una hoja enorme y anotar de dónde viene ese recurso.", "B", "Reinterpreta con tema propio y declara de dónde viene el recurso."),
    [
        ex("En Artes Visuales, ¿qué es reinterpretar un referente?", "Tomar un recurso y cambiar el resto para decir algo propio", "Así la obra conserva una enseñanza sin repetir al autor."),
        ex("Verdadero o falso: un mural sobre un río muestra cómo toda una comunidad se relaciona con la naturaleza.", "Falso", "Solo muestra lo que su autor decidió mostrar."),
        ex("Además de dos detalles, ¿qué dos cosas termina de registrar tu observación?", "Una pregunta y una posibilidad propia", "Eso pide la bitácora de observación."),
    ],
    task(
        "Elige UN referente de ejemplo. A) Mural: un niño riega una planta más alta que un edificio, en verdes y amarillos. B) Serie de cuatro fotografías de la misma quebrada, tomadas desde el mismo punto en distintas estaciones. C) Afiche: una mano hecha de hojas secas sostiene una botella plástica aplastada sobre fondo gris. En tu bitácora anota dos detalles, una pregunta y la procedencia del referente. Luego haz dos bocetos pequeños que reinterpreten recursos distintos, elige uno y dibújalo con una decisión que no esté en el referente.",
        "Elegí la A. Detalles: la planta es más alta que el edificio; los colores son verdes y amarillos. Pregunta: ¿por qué el niño es tan pequeño? Procedencia: mural de ejemplo de esta clase. Boceto 1: escala exagerada con una abeja enorme. Boceto 2: material natural para formar una figura. Elijo el 1 y agrego un sillón diminuto bajo la abeja.",
        ["registra dos detalles, una pregunta y la procedencia", "hace dos bocetos que toman recursos distintos", "elige uno y agrega una decisión propia", "no copia las formas ni los colores del referente"],
        ["bitácora de observación", "dos bocetos pequeños", "dibujo elegido con decisión propia"],
        ["repetir el referente con otro tamaño o color", "generalizar a toda una comunidad"],
        "Pregunta qué recurso tomó del referente y qué decisión del dibujo final ya no está en él.",
    ),
    "Mira durante un minuto una planta o un árbol cerca de tu casa y di en voz alta un recurso visual que podrías tomar de él, sin copiarlo.",
    "Elige un símbolo ambiental muy repetido y explica con dos frases qué dibujo propio lo reemplazaría y por qué comunica más.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Hojas, lápiz de mina y lápices de colores. Las tres fichas de obras están escritas en esta clase; no necesitas buscarlas.",
    "Aprenderé a investigar el contexto, el material y el propósito de una obra sobre personas, naturaleza y medioambiente, y a separar datos de inferencias. Sirve para decidir qué puedo tomar de una obra y qué no.",
    ["Sé que un referente se reinterpreta y no se copia.", "Sé separar lo que se ve de lo que opino."],
    [
        "Para entender una obra investigo tres cosas: su contexto, su material y su propósito. El contexto es la situación en que se hizo: lugar, momento, quién la hizo y para quién. El material es con qué se hizo. El propósito es para qué se hizo: informar, invitar a cuidar, recordar, denunciar o embellecer un lugar.",
        "Los tres datos se relacionan. Una escultura hecha con tapas plásticas recolectadas habla de los residuos con el mismo material del que trata. Un mural en un muro exterior busca que lo vea todo el barrio, no solo quien entra a un museo. Cuando una ficha no dice algo, no lo invento: lo marco como pendiente y busco una fuente, como la ficha del museo, el relato de su autora o un libro.",
        "Distingo los datos, que la ficha afirma, de las inferencias, que yo deduzco a partir de ellos. «Fue pintado por estudiantes y vecinos» es un dato; «por eso el barrio lo cuida» es una inferencia. Con el contexto, el material y el propósito decido qué recurso puedo reinterpretar en mi obra y cuál no calza con lo que quiero comunicar.",
    ],
    [("contexto", "situación en que se hizo una obra: lugar, momento, autoría y público"), ("propósito", "para qué se hizo una obra"), ("dato", "información que la ficha o la fuente afirma"), ("inferencia", "idea que yo deduzco a partir de los datos"), ("fuente", "lugar de donde sale una información, como una ficha o el relato de su autor")],
    [
        w("Leer una ficha", "Ficha de ejemplo: «Escultura hecha con tapas plásticas recolectadas por un colegio, instalada en una plaza durante un mes, para mostrar cuánto plástico se junta». Señala contexto, material y propósito.", ["Contexto: una plaza, durante un mes, hecha por un colegio.", "Material: tapas plásticas recolectadas.", "Propósito: mostrar cuánto plástico se junta."], "Contexto: plaza y colegio; material: tapas recolectadas; propósito: mostrar la cantidad de plástico"),
        w("Dato o inferencia", "La ficha del mural dice: «Pintado por jóvenes del sector en un puente peatonal para invitar a no botar basura al río». Una compañera escribe: «Por eso el río ya no tiene basura». ¿Qué es su frase?", ["La ficha no dice qué pasó con el río después.", "La frase deduce un resultado que no aparece."], "Es una inferencia sin respaldo; el dato es solo que lo pintaron para invitar a no botar basura"),
    ],
    [
        m("Escribir como dato algo que la ficha no dice.", "Se mezcla lo que yo imagino con lo que realmente se sabe de la obra.", "Marca esa idea como inferencia o como dato pendiente y busca una fuente."),
        m("Copiar el material de una obra sin preguntarse para qué se eligió.", "El material puede ser parte del mensaje y no sirve en otro tema.", "Pregunta qué relación hay entre el material, el tema y el propósito."),
    ],
    [
        ex("Ficha: «Escultura hecha con tapas plásticas recolectadas por un colegio, instalada en una plaza durante un mes». ¿Cuál es su material?", "Tapas plásticas recolectadas", "La ficha nombra el material con que está hecha."),
        ex("En el análisis de una obra, ¿qué se llama propósito?", "Para qué se hizo la obra", "Es la razón por la que su autor la creó: informar, invitar o recordar."),
        ex("Ficha: «Fotografía en blanco y negro de un bosque talado, expuesta en un centro cultural». ¿Cuál es un dato de contexto? A. Está expuesta en un centro cultural B. Es una fotografía en blanco y negro.", "A", "Dice dónde se muestra la obra; el blanco y negro habla de su imagen."),
    ],
    [
        ex("Ficha: «Mural pintado en el muro exterior de una escuela rural por estudiantes y vecinos para una campaña de cuidado del agua». ¿Cuál afirmación es un dato y no una inferencia? A. Lo pintaron estudiantes y vecinos B. Por eso todo el pueblo cuida el agua.", "A", "La ficha lo afirma; la otra frase deduce un resultado que no aparece."),
        ex("Una escultura de tapas plásticas muestra cuánto plástico junta un colegio en un mes. ¿Qué relación hay entre su material y su propósito? A. El material forma parte del mensaje, porque es el residuo del que trata B. El material solo sirve para que la escultura pese poco.", "A", "El residuo real vuelve visible el problema; la otra opción inventa una razón que la ficha no da."),
        ex("La ficha no dice cuánto tiempo estuvo instalada otra escultura. ¿Qué haces? A. Anoto que ese dato falta y busco una fuente B. Escribo un número que me parece posible.", "A", "Un dato que falta se busca; no se inventa."),
    ],
    [
        ex("La ficha de un mural dice: «Pintado en el muro exterior de una escuela rural, por estudiantes y vecinos, para una campaña de cuidado del agua». Tres frases sobre él: 1) «Fue pintado en un muro exterior». 2) «Seguramente costó mucho dinero». 3) «Su propósito es una campaña de cuidado del agua». Según la ficha, ¿cuántas son datos?", "2", "La 1 y la 3 aparecen en la ficha; la 2 es una suposición."),
        ex("Quieres una obra sobre residuos para tu plaza. La ficha de la escultura dice: «Tapas plásticas recolectadas por un colegio, instalada en una plaza durante un mes». ¿Qué dato de su contexto te sirve para decidir dónde mostrar tu obra? A. Que se instaló en un espacio público abierto, una plaza B. Que usa tapas de un color específico, porque la ficha lo nombra.", "A", "La ficha informa el lugar; no dice nada sobre un color específico."),
        ex("Una obra está en un muro de calle y otra dentro de un edificio cerrado. ¿Cuál puede ver alguien que solo camina por la calle? A. La del muro de calle B. La del edificio cerrado.", "A", "Un muro exterior se ve desde la vereda; un espacio cerrado exige entrar."),
    ],
    [
        ex("La escultura de tapas tiene como propósito mostrar cuánto plástico se junta. La fotografía del bosque talado busca invitar a mirar el cambio de un paisaje. ¿Cuál de las dos usa un material del mismo tema que trata?", "La escultura de tapas", "Muestra residuos plásticos hechos de plástico; la fotografía solo retrata el paisaje."),
        ex("Un compañero dice: «El mural se pintó para ganar un premio». La ficha solo dice que fue para una campaña de cuidado del agua. ¿Qué es su afirmación?", "Una inferencia sin respaldo", "La ficha no menciona ningún premio."),
    ],
    [
        ex("Planificas una obra con restos de cartón. Dos propósitos: X) mostrar cuánto cartón se bota en tu casa en una semana, Y) invitar a mirar un humedal. ¿Cuál se relaciona mejor con el cartón reutilizado?", "X", "El material residual habla del consumo, tema del propósito X."),
        ex("Ficha: «Instalación con ramas caídas, en un parque, creada por vecinos». ¿Cuál afirmación es una inferencia? A. Está en un parque B. Probablemente usaron ramas porque las encontraron en el mismo parque.", "B", "La ficha no dice por qué eligieron ramas; es una deducción."),
    ],
    ex("Tu curso elige un referente para una exposición sobre el cuidado del río. La ficha dice: «Mural de ejemplo en un puente peatonal, pintado por jóvenes del sector con pintura de exteriores, para invitar a no botar basura al río». ¿Qué información de contexto usas para decidir dónde poner tu obra? A. Que está en un puente peatonal, un lugar por donde se pasa a pie B. Que usa pintura de exteriores.", "A", "El lugar de la obra muestra a qué público puede llegar; la pintura no decide dónde ponerla."),
    [
        ex("¿Qué tres cosas se investigan de una obra en esta clase?", "Contexto, material y propósito", "Juntas explican qué es la obra y por qué está hecha así."),
        ex("Verdadero o falso: si la ficha no dice un dato, puedo escribirlo como si fuera seguro.", "Falso", "Un dato que falta se busca o se marca como pendiente."),
        ex("En Artes Visuales, ¿qué es una inferencia?", "Una idea que deduzco a partir de los datos", "No aparece escrita en la fuente."),
    ],
    task(
        "Elige UNA ficha. A) Mural de ejemplo en el muro exterior de una escuela rural, pintado por estudiantes y vecinos para una campaña de cuidado del agua. B) Escultura de ejemplo con tapas plásticas recolectadas por un colegio, instalada en una plaza durante un mes. C) Fotografía de ejemplo de un bosque talado, en blanco y negro, expuesta en un centro cultural para invitar a mirar el cambio de un paisaje. Haz una tabla con contexto, material y propósito, marca una inferencia tuya con una pregunta para investigarla y anota qué recurso tomarías para una obra propia.",
        "Elegí la B. Contexto: plaza, un mes, colegio. Material: tapas plásticas recolectadas. Propósito: mostrar la cantidad de plástico. Inferencia: tal vez muchos vecinos la vieron; pregunta: ¿cuánta gente pasa por esa plaza? Recurso que tomaría: usar el residuo real como material de mi obra sobre el agua.",
        ["completa contexto, material y propósito con datos de la ficha", "marca una inferencia distinta de los datos", "propone una pregunta para investigar", "elige un recurso para una obra propia"],
        ["tabla de tres columnas", "inferencia con pregunta", "recurso elegido"],
        ["escribir como dato algo que la ficha no dice", "olvidar relacionar el material con el propósito"],
        "Señala un dato y una inferencia de la tabla y pregunta qué fuente confirmaría la inferencia.",
    ),
    "Mira un objeto hecho de material reutilizado en tu casa y di en voz alta para qué se usa y por qué ese material sirve para eso.",
    "Escribe dos propósitos distintos para una obra hecha con restos de cartón y explica cómo cambiaría la elección del material en cada uno.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hojas, lápiz de mina, lápices de colores, restos limpios de papel de diario y cola fría o cinta de papel (o dibuja en vez de pegar). Las pruebas que se piden están descritas en esta clase.",
    "Aprenderé a explorar procedimientos como el frottage, el collage y el dibujo de observación, y a ver cómo el encuadre, la escala, el color y la composición cambian el efecto. Sirve para decidir con evidencia antes de hacer la obra final.",
    ["Sé distinguir copiar de reinterpretar.", "Sé separar el contexto, el material y el propósito de una obra."],
    [
        "Un procedimiento es la manera de trabajar un material. El frottage consiste en poner una hoja sobre una superficie con textura, como una corteza o una hoja de planta con relieve, y frotar encima con el lápiz acostado para pasar su relieve al papel. El collage es pegar trozos de papeles u otros materiales para componer una imagen. El dibujo de observación consiste en dibujar lo que veo ante mis ojos, no una imagen ya hecha.",
        "Cada decisión visual cambia el efecto. El encuadre es la parte de la escena que muestro y a qué distancia: un primer plano muy cercano de una hoja destaca su detalle, y un plano general con un árbol diminuto en la ciudad puede dar sensación de escasez. La escala, el contraste y el color también hablan: los colores cálidos, como el naranja, avanzan; los fríos, como el azul y el violeta, se alejan o calman.",
        "Para saber qué decisión produjo qué efecto, hago pruebas pequeñas y cambio una sola variable a la vez: solo el color, solo la ubicación o solo el tamaño. Si cambio tres cosas juntas, no sé cuál causó el cambio. Después comparo las pruebas con mi intención y elijo con evidencia, no por costumbre.",
    ],
    [("frottage", "técnica de frotar con lápiz sobre una superficie con relieve para pasar su textura al papel"), ("collage", "técnica de pegar trozos de materiales para componer una imagen"), ("encuadre", "parte de la escena que se muestra y a qué distancia"), ("variable", "decisión visual que se puede cambiar, como el color, el tamaño o la ubicación"), ("contraste", "diferencia marcada entre dos elementos, como un color vivo sobre gris")],
    [
        w("Una sola variable", "Quieres mostrar que una persona se siente pequeña ante un bosque. Prueba 1: persona de 4 cm bajo árboles de 4 cm. Prueba 2: la misma persona de 4 cm bajo árboles de 20 cm. ¿Qué variable cambia y cuál prueba sirve?", ["La persona, los colores y el fondo son iguales en las dos pruebas.", "Solo cambia el tamaño de los árboles.", "Los árboles mucho más altos que la persona dan sensación de pequeñez."], "Cambia la escala de los árboles; sirve la prueba 2"),
        w("Elegir un color de fondo", "Quieres un fondo que dé sensación de calor seco para un campo sin lluvia. Dudas entre un fondo azul y uno naranja. ¿Cuál eliges?", ["El azul es un color frío que calma o refresca.", "El naranja es un color cálido que se asocia al calor."], "El fondo naranja"),
    ],
    [
        m("Cambiar el color, el tamaño y la ubicación a la vez en una nueva prueba.", "No se sabe cuál cambio produjo el efecto.", "Cambia una sola variable por prueba y anota qué cambió."),
        m("Elegir una prueba porque «se ve más linda» sin compararla con la intención.", "La belleza no dice si la obra comunica lo que querías.", "Compara cada prueba con tu intención y elige la que mejor la logra."),
    ],
    [
        ex("Pones una hoja de papel sobre una corteza y la frotas con el lápiz acostado para pasar su relieve. ¿Cómo se llama esta técnica?", "Frottage", "Se pasa la textura de una superficie al papel frotando."),
        ex("Quieres que se vean con detalle las nervaduras de una hoja. ¿Qué encuadre eliges: primer plano o plano general?", "Primer plano", "Acercarse muestra los detalles pequeños."),
        ex("¿Cuál grupo está formado solo por colores fríos? A. Azul y violeta B. Naranja y rojo.", "A", "Azul y violeta se asocian a lo frío; naranja y rojo son cálidos."),
    ],
    [
        ex("En un dibujo, un árbol ocupa una décima parte de una plaza gris. ¿Qué efecto puede dar su tamaño pequeño? A. Sensación de poca presencia o escasez B. Sensación de abundancia.", "A", "Un elemento diminuto frente a un entorno grande parece escaso."),
        ex("Probaste dos versiones: en la primera la hoja está al centro y en la segunda en una esquina con mucho espacio vacío. ¿Qué variable cambiaste?", "La ubicación (composición)", "Cambió el lugar de la hoja en la página."),
        ex("¿Por qué conviene cambiar una sola variable a la vez al comparar pruebas? A. Porque así sé cuál cambio produjo el efecto B. Porque se gasta menos papel.", "A", "Si cambian varias cosas, no se sabe cuál causa el cambio."),
    ],
    [
        arith("En un collage usarás 12 trozos de papel con el doble de trozos verdes que de grises. ¿Cuántos trozos verdes necesitas?", "12*2//3", "Se divide en 3 partes: 2 verdes por cada 1 gris."),
        ex("Quieres que quien mire sienta cercanía con una semilla que germina. ¿Qué encuadre usas? A. Primer plano muy cerca de la semilla B. Plano general lejano con la semilla casi invisible.", "A", "Acercar el encuadre da cercanía; alejarlo la esconde."),
        ex("Haces un frottage de una superficie rugosa. ¿Cómo usas el lápiz: acostado o con la punta bien afilada?", "Acostado", "La mina acostada marca la textura en una franja; la punta solo hace líneas finas y puede romper el papel."),
    ],
    [
        ex("Tu intención es mostrar un árbol que casi desaparece en la ciudad. Prueba 1: un árbol de 10 cm entre edificios de 12 cm. Prueba 2: un árbol de 2 cm entre los mismos edificios. ¿Cuál la logra mejor?", "La prueba 2", "El árbol muy pequeño frente a los edificios da la idea de que casi desaparece; en la prueba 1 tiene casi la misma presencia que ellos."),
        ex("Un compañero pintó una ciudad gris con una sola flor roja en primer plano y quiere mostrar que la naturaleza resiste. ¿Qué decisión ayuda más a ese mensaje? A. El contraste entre el rojo y los grises B. Pintar la flor del mismo gris.", "A", "El color vivo destaca sobre el gris y la hace visible."),
    ],
    [
        ex("Quieres mostrar que el agua desaparece de un campo. Propuesta X: una línea azul que se adelgaza de izquierda a derecha sobre fondo café. Propuesta Y: una línea azul gruesa y constante sobre fondo azul. ¿Cuál comunica mejor la intención?", "X", "La línea que se adelgaza muestra pérdida; Y no cambia ni se distingue."),
        ex("Tu árbol de verde oscuro se confunde con el fondo, también verde oscuro. ¿Qué cambio de una sola variable lo soluciona? A. Cambiar el fondo a un tono claro B. Cambiar el tamaño de la hoja de papel.", "A", "El contraste de valor entre árbol y fondo hace que se distinga."),
    ],
    ex("Tienes cartón, diario, hojas secas y témpera. Quieres mostrar cercanía entre un niño y un árbol de tu plaza. ¿Qué decisión de composición la expresa mejor? A. El niño y el árbol casi tocándose por sus bordes B. El niño en una esquina y el árbol en la opuesta con espacio vacío entre ambos.", "A", "La cercanía en la página sugiere cercanía en la relación."),
    [
        ex("En Artes Visuales, ¿qué es el encuadre?", "La parte de la escena que muestro y a qué distancia", "Define qué se ve y cuánto detalle aparece."),
        ex("Verdadero o falso: cambiar tres variables a la vez ayuda a saber cuál produjo el efecto.", "Falso", "Solo con una variable cambiada se puede relacionar el efecto con una decisión."),
        ex("¿Cuál de estos colores es frío: rojo, amarillo o azul?", "Azul", "El rojo y el amarillo son cálidos; el azul se asocia a lo frío."),
    ],
    task(
        "Hoy pruebas dos variantes de un mismo tema: una hoja de árbol sola en un patio. Elige UNA variable para cambiar: A) el encuadre (primer plano o plano general), B) el color del fondo (cálido o frío), C) el tamaño de la hoja del árbol dentro del dibujo (muy grande o muy pequeña). Haz dos pruebas pequeñas con papel, lápiz o collage de diario, cambiando solo esa variable. Escribe qué efecto produjo cada una y cuál elegirías para mostrar que la hoja es frágil.",
        "Elegí la C. Prueba 1: hoja del árbol muy grande, que ocupa casi todo el papel. Prueba 2: hoja del árbol muy pequeña, en el centro del papel. En la 2 la hoja se ve frágil, porque el espacio vacío la vuelve diminuta. Elijo la 2.",
        ["cambia una sola variable entre las dos pruebas", "describe el efecto de cada prueba", "elige una según la intención dada", "las pruebas son distintas entre sí"],
        ["dos pruebas pequeñas", "texto con el efecto y la elección"],
        ["cambiar varias variables a la vez", "elegir por gusto y no por la intención"],
        "Pregunta cuál fue la variable que cambió y qué efecto concreto tuvo en la idea de fragilidad.",
    ),
    "Pon una hoja sobre una superficie con relieve de tu casa, como la tapa de un cuaderno rugoso, y frótala con un lápiz acostado para ver su textura.",
    "Explica en tres frases cómo cambiarías el encuadre de tu prueba elegida para que el efecto fuera el contrario.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hojas, lápiz de mina, lápices de colores, restos de papel de diario y cola fría o cinta de papel. Si no tienes cola, puedes dibujar en vez de pegar.",
    "Aprenderé a pasar de una intención a una obra propia sobre personas, naturaleza y medioambiente con bocetos, una versión final, un título y una ficha. Sirve para crear una respuesta visual que se pueda explicar.",
    ["Sé hacer pruebas cambiando una variable a la vez.", "Sé que una obra declara la procedencia de sus referentes."],
    [
        "Para crear una respuesta propia sigo cinco pasos. Primero escribo mi intención en una frase: qué quiero mostrar, con qué recurso y qué efecto busco. Segundo, hago dos o tres bocetos, que son dibujos rápidos para probar ideas. Tercero, elijo uno y explico por qué sirve a mi intención. Cuarto, hago la versión final. Quinto, escribo un título y una ficha con materiales y procedencia del referente.",
        "Una buena intención es específica. «Quiero hacer algo bonito con hojas» no dice qué comunicar. En cambio, «quiero mostrar que una grieta del pavimento se vuelve un camino de hojas, con hojas pegadas en línea, para que se sienta que la naturaleza avanza» dice el qué, el cómo y el efecto. Un título puede ayudar a la idea: «Lo que crece entre el cemento» dice más que «Naturaleza».",
        "Mi obra es propia cuando la composición y el mensaje son decisiones mías, aunque haya tomado un recurso de otro referente. En la ficha lo declaro: «recurso de escala tomado del mural de ejemplo». Eso es honesto y no le quita valor a mi obra. Uso materiales reutilizados limpios, como diario o cartón, y evito objetos con filo o vidrio.",
    ],
    [("intención", "frase que dice qué quiero mostrar, con qué recurso y qué efecto busco"), ("boceto", "dibujo rápido para probar una idea"), ("versión final", "obra terminada que se elige entre los bocetos"), ("ficha", "texto breve con título, materiales y procedencia de los referentes"), ("autoría", "decisiones propias que hacen que una obra sea de quien la creó")],
    [
        w("Mejorar una intención", "Mejora esta intención: «Quiero dibujar un río bonito».", ["No dice qué comunicar ni con qué recurso.", "Agrego un qué: un río que se angosta al pasar por un puente.", "Agrego un cómo: una línea azul que se adelgaza.", "Agrego un efecto: que se sienta que al agua le cuesta pasar."], "«Quiero mostrar un río que se angosta bajo un puente, con una línea azul que se adelgaza, para que se sienta que al agua le cuesta pasar»"),
        w("Elegir un boceto", "Intención: mostrar que el agua de una llave se pierde gota a gota. Boceto 1: una llave con gotas que forman un charco grande en el suelo. Boceto 2: una llave cerrada, sin gotas. ¿Cuál eliges?", ["El boceto 2 no muestra pérdida de agua: no responde a la intención.", "El boceto 1 muestra gotas y un charco que crece."], "Elijo el boceto 1, porque muestra las gotas que se pierden y el charco"),
    ],
    [
        m("Saltarse los bocetos y hacer la versión final con la primera idea.", "No se compara ninguna alternativa ni se descubre un recurso mejor.", "Haz al menos dos bocetos distintos y compáralos con tu intención."),
        m("No declarar el recurso que se tomó de un referente.", "Parece que todo es propio y se pierde la procedencia.", "Anota en la ficha qué recurso tomaste y de qué referente."),
    ],
    [
        ex("En el proceso de creación de esta clase, ¿qué paso va justo antes de hacer la versión final?", "Elegir un boceto y explicar por qué sirve a la intención", "Primero se compara y se decide; después se hace la obra final."),
        ex("Una intención dice: «Quiero hacer algo bonito con hojas». ¿Qué le falta? A. Decir qué quiere comunicar B. Usar más hojas.", "A", "No dice qué comunicar ni qué efecto busca."),
        ex("La ficha de una obra dice: «Título: Raíces de mi calle. Materiales: cartón y hojas secas». ¿Qué parte falta?", "La procedencia del referente", "La ficha lleva título, materiales y referente."),
    ],
    [
        ex("¿Cuál intención dice el qué, el cómo y el efecto? A. «Quiero mostrar una grieta convertida en camino de hojas, con hojas pegadas en línea, para que se sienta que la naturaleza avanza» B. «Quiero hacer un collage de naturaleza».", "A", "Dice qué muestra, con qué recurso y qué efecto busca."),
        ex("Boceto 1 repite el referente con otros colores. Boceto 2 usa el recurso de escala con un tema propio. Si buscas autoría, ¿cuál desarrollas?", "El boceto 2", "Reinterpreta el recurso en vez de repetir la obra."),
        ex("Tu obra usa diario, hojas secas del patio y cola fría. ¿Cuál de esos materiales es un material reutilizado? A. El diario B. La cola fría.", "A", "El diario ya tuvo un uso anterior; la cola es un producto nuevo."),
    ],
    [
        arith("Haces 3 bocetos pequeños en una hoja de 24 cm de ancho, repartida en 3 partes iguales. ¿Cuántos centímetros de ancho tiene cada boceto?", "24//3", "El ancho de la hoja se reparte en partes iguales."),
        ex("Para una obra que muestra una planta que crece entre baldosas, ¿qué título anuncia mejor la idea? A. «Naturaleza» B. «Lo que crece entre las baldosas».", "B", "Es específico; el otro título no dice nada de la idea."),
        ex("Un compañero quiere escribir «Hecho solo por mí», pero tomó el recurso de la escala de un mural de ejemplo. ¿Qué debe agregar a su ficha? A. Que tomó el recurso de escala de ese mural B. Nada, porque la idea es suya.", "A", "La ficha declara la procedencia del recurso."),
    ],
    [
        ex("Intención: mostrar que el pasto crece entre cemento. Boceto 1: un gran cuadrado de cemento con una mancha verde en una grieta. Boceto 2: un césped completo sin cemento. ¿Cuál responde a la intención?", "El boceto 1", "Muestra el cemento y el pasto que crece, como pide la intención."),
        ex("Una estudiante dice que su obra es propia porque la hizo ella, pero usó la misma composición y el mismo símbolo, un planeta con manos, de un afiche. ¿Qué le falta para tener una respuesta propia?", "Tomar decisiones propias de composición o de símbolo", "La autoría nace de decisiones propias, no solo de quién la dibuja."),
    ],
    [
        arith("Tu versión final cabe en una hoja de 30 cm de ancho, con un margen de 2 cm por cada lado. ¿Cuántos centímetros de ancho útil quedan?", "30-2-2", "Se resta el margen de los dos lados."),
        ex("Dos títulos para una obra que muestra una planta que crece entre baldosas: X) «Planta» Y) «Entre baldosas, igual crece». ¿Cuál se relaciona más con la idea de resistencia?", "Y", "Dice que la planta crece pese al obstáculo."),
    ],
    ex("Te piden para el diario mural una obra propia sobre cuidar el entorno de tu escuela, con un afiche de ejemplo de una mano hecha de hojas como referente. ¿Cuál ficha está mejor armada? A. «Título: Mi patio. Materiales: hojas secas y diario. Referente: afiche de la mano de hojas, recurso de material natural. Intención: mostrar que el patio puede ser un lugar de cuidado» B. «Título: Mi obra».", "A", "Reúne título, materiales, procedencia e intención."),
    [
        ex("¿Cuáles son los cinco pasos para crear la respuesta propia, en orden, desde el primero?", "Intención, bocetos, elegir un boceto, versión final, título y ficha", "Ese es el orden de trabajo de la clase."),
        ex("Verdadero o falso: basta con cambiar el color del referente para tener una obra propia.", "Falso", "La composición y la idea deben ser decisiones propias."),
        ex("¿Qué tres cosas dice una intención específica?", "Qué muestra, con qué recurso y qué efecto busca", "Así guía las decisiones de la obra."),
    ],
    task(
        "Elige UN tema. A) Una planta que crece en una grieta de la vereda. B) Un río que cruza una ciudad. C) Un patio escolar con un solo árbol. Escribe tu intención en una frase, haz tres bocetos pequeños con distintos encuadres, elige uno y justifícalo, haz la versión final con papel, lápices o collage de diario, y arma una ficha con título, materiales y el recurso que tomaste de algún referente de las clases anteriores.",
        "Tema C. Intención: mostrar que un solo árbol sostiene todo un patio, con un árbol grande en primer plano y niños pequeños a su sombra, para que se sienta protección. Elijo el boceto 2. Título: «Un árbol para todos». Materiales: diario y lápices. Recurso tomado: escala exagerada del mural de ejemplo.",
        ["escribe una intención específica", "hace tres bocetos distintos", "justifica la elección con la intención", "completa título, materiales y procedencia del recurso"],
        ["intención escrita", "tres bocetos", "versión final", "ficha de la obra"],
        ["intención vaga como «algo bonito»", "no declarar el referente"],
        "Señala qué decisión de la obra no está en ningún referente y pregunta cómo ayuda a la intención.",
    ),
    "Cuenta a una persona de tu casa tu intención en una sola frase, sin mostrarle el dibujo, y mira si entiende qué quieres mostrar.",
    "Escribe una segunda ficha para la misma obra como si la presentaras a personas que no conocen tu escuela, y di qué datos cambiarías.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Tu obra o boceto de la clase anterior, hojas y lápiz. Si no lo tienes, usa uno de los dos dibujos descritos en esta clase.",
    "Aprenderé a comparar la intención de mi obra con el efecto que produce en quien la mira, usando sus respuestas, y a decidir un cambio con evidencia. Sirve para mejorar una obra sin quedarme con mi primera impresión.",
    ["Sé escribir una intención específica.", "Sé hacer pruebas cambiando una sola variable."],
    [
        "La intención es lo que yo quiero comunicar; el efecto es lo que realmente percibe quien mira. Pueden coincidir o no. Para comprobarlo, muestro la obra sin explicarla y hago tres preguntas: qué ves, qué sientes y qué crees que quiere decir. Anoto las respuestas tal como las dicen y las comparo con mi intención.",
        "Si el efecto no coincide, no culpo a quien mira: reviso qué decisión visual lo produjo. Por ejemplo, si quería mostrar abundancia de agua y la gente ve «un charco pequeño», quizá la mancha azul era demasiado chica. Cambio una sola decisión y vuelvo a mostrar la obra a las mismas personas. Una respuesta distinta de la que esperaba no es un error: es información sobre la obra.",
        "También respeto otros puntos de vista. Dos personas pueden sentir cosas distintas por la misma obra, y eso no la invalida. Pregunto qué detalle las llevó a su respuesta y evalúo si ese detalle sirve o estorba a mi intención. Así decido qué cambio hacer y qué conservar, y puedo explicar mi elección con evidencia.",
    ],
    [("intención", "lo que quiero comunicar con la obra"), ("efecto", "lo que realmente percibe o siente quien mira la obra"), ("evidencia", "respuesta o dato que permite comprobar algo"), ("revisión", "cambio que hago a una obra después de contrastarla con su efecto"), ("público", "personas que miran y reaccionan a la obra")],
    [
        w("Contrastar", "Intención: mostrar soledad. Dos personas ven tu dibujo de una banca vacía bajo un árbol sin hojas. Una dice «soledad» y la otra «descanso». ¿Hay coincidencia?", ["Una persona percibió soledad: coincide.", "La otra percibió descanso: es una información distinta.", "Pregunto qué detalle le dio sensación de descanso."], "Coincide en una de dos; reviso qué detalle produjo la sensación de descanso"),
        w("Decidir un cambio", "Intención: advertir que un cerro está muy seco. Efecto: las personas ven «un paisaje tranquilo» porque usaste verdes suaves. ¿Qué cambio de una sola decisión haces?", ["La causa probable es el color de todo el cerro.", "Cambio solo el color: uso cafés y amarillos secos.", "Vuelvo a mostrarlo a las mismas personas."], "Cambiar los verdes por cafés y amarillos secos y volver a consultar a las mismas personas"),
    ],
    [
        m("Explicar la obra antes de que la miren y luego preguntar si se entiende.", "La explicación tapa el efecto real de la imagen.", "Muestra primero la obra y pregunta qué ven y qué sienten."),
        m("Cambiar toda la obra cuando una persona no coincide con la intención.", "No se sabe qué decisión produjo el efecto.", "Cambia una sola decisión y compara con las respuestas anteriores."),
    ],
    [
        ex("Tu intención es transmitir calma. Una persona dice que tu dibujo le parece agitado. ¿Hay diferencia entre intención y efecto?", "Sí", "Querías calma y se percibió agitación."),
        ex("Antes de explicar tu obra a una compañera, ¿qué debes hacer para comprobar su efecto?", "Preguntarle qué ve y qué siente sin explicarle", "Así el efecto no se mezcla con tu explicación."),
        ex("Tu intención: mostrar hojas como un tesoro. Alguien dice que parecen basura. ¿Coinciden la intención y el efecto?", "No", "Percibió lo contrario de lo que querías comunicar."),
    ],
    [
        ex("Mostraste tu río de líneas finas azules a tres personas. Dos dijeron «calma» y una dijo «frío». Tu intención era calma. ¿Cuántas personas percibieron el efecto buscado?", "2", "Solo dos respuestas coinciden con la intención de calma."),
        ex("Un compañero dijo «no me gusta tu obra». ¿Qué pregunta te da más información? A. «¿Qué parte te hizo pensar eso?» B. «¿No te gusta nada?»", "A", "Pide un detalle concreto que se puede revisar."),
        ex("Si el efecto no coincide con la intención, ¿qué revisas primero? A. Qué decisión visual produjo ese efecto B. Cuánto tiempo tardaste en hacerla.", "A", "El efecto nace de las decisiones visuales (tamaño, color, composición), no del tiempo de trabajo."),
    ],
    [
        ex("Intención: mostrar abundancia de agua. Efecto: la gente ve «un charco pequeño». ¿Qué cambio de una sola decisión ayuda? A. Agrandar la mancha azul hasta ocupar casi toda la hoja B. Cambiar solo el título de la obra.", "A", "El tamaño de la mancha es lo que produce la percepción de poca agua."),
        arith("Mostraste dos versiones a 8 personas. En la versión 1, 3 dijeron «cuidado»; en la versión 2, 6 dijeron «cuidado». ¿Cuántas personas más percibieron el efecto buscado en la versión 2?", "6-3", "Se compara la cantidad en cada versión."),
        ex("Intención: la naturaleza resiste en la ciudad. Efecto: la planta se pierde entre grises similares. ¿Qué cambio es coherente? A. Dar a la planta un verde más vivo que los grises B. Pintar toda la obra con el mismo gris.", "A", "El contraste hará visible la planta."),
    ],
    [
        ex("Un compañero dice: «Mi obra no tiene nada que cambiar, aunque todos entendieron algo distinto a lo que quería». ¿Es correcto?", "No", "La diferencia entre intención y efecto indica algo que revisar."),
        ex("Camila siente nostalgia y Rosa siente alegría ante tu obra. Tu intención era nostalgia. ¿Qué haces con la respuesta de Rosa? A. Preguntarle qué detalle la llevó a sentir alegría y evaluar si cambiarlo B. Ignorarla porque no coincide.", "A", "La respuesta distinta es evidencia útil para revisar."),
    ],
    [
        ex("Intención: que se sienta que la naturaleza avanza sobre la ciudad. Versión 1: líneas verdes que suben desde abajo sobre edificios grises; la gente dijo «avanza». Versión 2: puntos verdes repartidos parejos por toda la hoja; la gente dijo «decoración». ¿Qué decisión explica la diferencia?", "Las líneas que suben desde abajo dan sentido de avance", "El recorrido de las líneas crea movimiento; los puntos parejos no."),
        ex("Después de revisar tu obra, ¿cuál es la mejor evidencia de que el cambio funcionó? A. Mostrar la versión nueva a las mismas personas y comparar sus respuestas con las anteriores B. Decir que ahora te gusta más a ti.", "A", "Compara el efecto antes y después en las mismas personas."),
    ],
    ex("Antes de colgar tu obra sobre el reciclaje en el pasillo del colegio, la muestras a tres compañeros. Dicen: «Los colores se ven bien, pero no entendemos qué es la forma del centro». ¿Qué haces? A. Revisar si la forma central comunica tu intención y probar un cambio B. Colgarla igual y agregar un cartel que explique la forma, sin revisar el dibujo.", "A", "La duda de los compañeros es evidencia para revisar esa decisión; un cartel no corrige lo que la imagen no comunica."),
    [
        ex("En Artes Visuales, ¿qué es el efecto de una obra?", "Lo que realmente percibe o siente quien la mira", "Es distinto de la intención, que es lo que el autor quería comunicar."),
        ex("Verdadero o falso: si alguien no entiende tu obra, siempre es culpa suya.", "Falso", "Su respuesta es información sobre las decisiones visuales de la obra."),
        ex("¿Qué tres preguntas haces a quien mira tu obra sin explicarla?", "Qué ve, qué siente y qué cree que quiere decir", "Con esas respuestas puedes comparar el efecto con tu intención."),
    ],
    task(
        "Usa tu obra de la clase anterior. Si no la tienes, usa este dibujo de ejemplo: un árbol pequeño en una esquina de una hoja gris, con la intención «mostrar que la naturaleza resiste». Muéstralo sin explicarlo a dos personas y hazles las tres preguntas: qué ven, qué sienten y qué creen que quiere decir. Anota las respuestas, compáralas con la intención, cambia UNA decisión visual y vuelve a mostrarlo.",
        "Persona 1: ve un árbol solo y siente tristeza; cree que habla de abandono. Persona 2: ve un árbol pequeño y siente ternura. Intención: resistencia. Efecto: no coincide. Cambio (una sola decisión): le agrego un brote nuevo al árbol. Segunda ronda: la persona 1 dice «sigue creciendo».",
        ["anota las respuestas a las tres preguntas sin explicar la obra", "compara efecto e intención", "cambia solo una decisión", "vuelve a mostrar y registra la nueva respuesta"],
        ["tabla de respuestas", "obra o dibujo revisado", "registro de la segunda ronda"],
        ["explicar antes de preguntar", "cambiar muchas cosas a la vez"],
        "Pregunta qué decisión cambió y qué respuesta nueva muestra que el cambio funcionó.",
    ),
    "Muestra durante diez segundos un dibujo tuyo a una persona de tu casa, escóndelo y pídele que diga qué recuerda y qué sintió, sin explicar nada antes.",
    "Compara por escrito dos respuestas distintas de tu público a la misma obra y decide cuál conservarías como evidencia, explicando por qué.",
)

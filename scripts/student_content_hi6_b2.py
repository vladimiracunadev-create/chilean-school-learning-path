"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 14 (desastres naturales y desarrollo de Chile) y OA 15 (organización democrática)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA14, OA15 = "HI06 OA 14", "HI06 OA 15"

# ================================================================ OA 14 · clase 1
lesson(
    OA14, 1,
    "Aprenderé a ubicar en el tiempo y en el espacio algunos desastres naturales de la historia reciente de Chile: sismos, erupciones, sequía y aluviones. Sirve para entender por qué el país se prepara para ellos.",
    ["Sé ubicar el norte, el centro y el sur de Chile.", "Sé ordenar hechos en una línea de tiempo."],
    [
        "Un desastre natural es un fenómeno de la naturaleza que causa gran daño a las personas y a sus bienes. Chile está en el Cinturón de Fuego del Pacífico, donde chocan placas de la corteza terrestre. Por eso hay muchos sismos, que son movimientos bruscos del suelo, y muchos volcanes. Un tsunami es una serie de olas gigantes que suele producirse por un sismo bajo el mar.",
        "Algunos hechos de la historia reciente: el sismo de Valdivia, en el sur, en 1960, el de mayor magnitud medido en el mundo (9,5); la erupción del volcán Chaitén, en el sur, en 2008; el sismo y tsunami de 2010 en la zona centro-sur (8,8); el sismo de Iquique, en el norte, en 2014 (8,2); y en 2015 el aluvión de Atacama, en el norte, y la erupción del volcán Calbuco, en el sur. Desde alrededor de 2010 la zona central vive una sequía, que es la falta de lluvia durante muchos años.",
        "Un aluvión es un flujo rápido de agua con barro y piedras que baja de los cerros después de lluvias fuertes. Para ubicar un desastre decimos cuándo ocurrió, o sea el año, y dónde, o sea la zona de Chile. Con los años podemos calcular cuánto tiempo pasó entre un hecho y otro.",
    ],
    [("sismo", "movimiento brusco del suelo"), ("tsunami", "serie de olas gigantes, casi siempre producidas por un sismo bajo el mar"), ("erupción", "salida de lava, cenizas y gases por un volcán"), ("sequía", "falta de lluvia durante mucho tiempo"), ("aluvión", "flujo de agua con barro y piedras que baja de los cerros")],
    [
        ("Ubicar un hecho", "El sismo de Iquique ocurrió en 2014. ¿Cuándo y en qué zona de Chile?", ["El año es 2014.", "Iquique está en el norte.", "Respondo con el año y la zona."], "En 2014, en el norte"),
        ("Calcular el tiempo entre hechos", "Un sismo fue en 2010 y otro en 2014. ¿Cuántos años pasaron entre ellos?", ["Resto los años.", "2014 menos 2010.", "Son 4 años."], "4 años"),
    ],
    [
        ("Creer que los desastres naturales solo ocurren en una zona de Chile.", "Hubo sismos, erupciones, sequías y aluviones en el norte, el centro y el sur.", "Ubica cada hecho con su año y su zona."),
        ("Confundir un sismo con un tsunami.", "El sismo es el movimiento del suelo y el tsunami son olas que suelen venir después.", "Pregunta si habla del suelo o del mar."),
    ],
    [
        ("¿Qué ocurrió antes: el sismo de 1960 o el de 2010?", "El de 1960", "1960 es un año anterior a 2010."),
        ("El sismo de 2014 afectó la zona de Iquique. ¿Esa zona queda en el norte o en el sur de Chile?", "En el norte", "Iquique está en el norte del país."),
        ("Un volcán que hace erupción, ¿es un caso de volcanismo o de sequía?", "Volcanismo", "La sequía es falta de lluvia, no salida de lava."),
    ],
    [
        ("¿Por qué en Chile hay tantos sismos y volcanes?", "Porque está en una zona donde chocan placas de la corteza terrestre", "Ese choque produce los sismos y los volcanes."),
        ("¿Qué diferencia hay entre un sismo y un tsunami?", "El sismo es un movimiento del suelo y el tsunami es una serie de olas gigantes", "Así se definieron en la clase."),
        ("Una sequía, ¿es falta de lluvia durante mucho tiempo o un temblor fuerte?", "Falta de lluvia durante mucho tiempo", "Así se definió en el vocabulario."),
    ],
    [
        arith("Entre el sismo de Valdivia (1960) y el sismo de 2010, ¿cuántos años pasaron?", "2010-1960", "Se resta el año menor al año mayor.", " años"),
        ("Ordena por año, del más antiguo al más reciente: A) aluvión de Atacama (2015), B) erupción del Chaitén (2008), C) sismo de Valdivia (1960).", "C, B, A", "1960 es el año menor y 2015 el mayor."),
        ("De estos tres sismos, ¿cuál ocurrió más al norte: Valdivia 1960, centro-sur 2010 o Iquique 2014?", "Iquique 2014", "Iquique está en el norte y los otros dos en el sur o centro-sur."),
    ],
    [
        ("Pía dice: «Los desastres naturales solo ocurren en el sur de Chile». Con los hechos de la clase, ¿qué error tiene?", "Hubo hechos en el norte, como el sismo de 2014 y el aluvión de Atacama", "Los hechos de la clase abarcan varias zonas."),
        ("Un compañero cuenta que en 2015 bajó por los cerros de Atacama agua con barro y piedras. ¿Fue un sismo o un aluvión?", "Un aluvión", "Es un flujo de agua con barro y piedras, no un movimiento del suelo."),
    ],
    [
        arith("Entre la erupción del Chaitén (2008) y la del Calbuco (2015), ¿cuántos años pasaron?", "2015-2008", "Se resta el año anterior al posterior.", " años"),
        ("Ordena de norte a sur: A) erupción del Chaitén, B) sismo de Iquique 2014, C) sequía de la zona central.", "B, C, A", "Iquique está en el norte, la zona central en el centro y Chaitén en el sur."),
    ],
    [("Un diario escolar hará una línea de tiempo con tres hechos: sismo de Valdivia (1960), erupción del Chaitén (2008) y sismo de Iquique (2014). ¿Cuál queda en el medio?", "La erupción del Chaitén", "2008 está entre 1960 y 2014.")],
    [("En Historia: ¿qué es un aluvión?", "Un flujo de agua con barro y piedras que baja de los cerros", "Es la definición de la clase."), ("¿Por qué Chile tiene muchos sismos?", "Porque está donde chocan placas de la corteza terrestre", "Ese choque mueve el suelo."), ("¿Qué es una sequía?", "Falta de lluvia durante mucho tiempo", "Es la definición de la clase.")],
    (
        "Elige uno de estos tres hechos y escribe una ficha con año, zona de Chile y tipo de desastre. Hecho a) sismo de Valdivia 1960; hecho b) erupción del Chaitén 2008; hecho c) aluvión de Atacama 2015. Luego calcula cuántos años pasaron hasta el año 2025.",
        "Hecho c: aluvión; 2015; norte de Chile; 10 años hasta 2025.",
        ["incluye año, zona y tipo de desastre", "calcula bien los años", "usa un vocabulario de la clase"],
        ["ficha escrita con un cálculo"],
        ["confundir el tipo de desastre", "restar mal los años"],
        "Muestra tu ficha a una persona de tu casa y pídele que compruebe tu resta.",
    ),
    "Pregunta a una persona de tu casa si recuerda algún sismo o desastre natural y anota el año.",
    "Dibuja una línea de tiempo con tres desastres naturales de esta clase.",
)

# ================================================================ OA 14 · clase 2
lesson(
    OA14, 2,
    "Aprenderé a leer fuentes sobre desastres naturales, como informes, datos científicos, noticias y relatos, y a preguntar quién las hizo. Sirve para saber qué ocurrió sin dejarse llevar por rumores.",
    ["Sé ubicar algunos desastres naturales de Chile en el tiempo y el espacio.", "Sé que una fuente tiene una procedencia."],
    [
        "Sobre un desastre natural hay muchas fuentes. El Servicio Sismológico Nacional, de la Universidad de Chile, mide y registra los sismos. El organismo nacional de emergencias (antes ONEMI, hoy SENAPRED) entrega informes sobre los daños y la ayuda. Los diarios cuentan lo que pasa día a día. Los relatos de testigos cuentan lo que vivió una persona.",
        "La procedencia nos dice quién hizo la fuente, cuándo y para qué. Los datos científicos se miden con instrumentos. Un titular puede exagerar para llamar la atención. Las primeras cifras que se publican suelen corregirse cuando llega más información, por eso conviene mirar la fecha de la fuente.",
        "Al leer, separamos lo que la fuente dice, lo que interpretamos y lo que no permite saber. Una fotografía de una casa caída muestra cómo quedó esa casa, pero no dice cuántas casas se dañaron en toda la región. Un relato de un vecino cuenta su barrio, no todo el país. Para entender un desastre, juntamos varias fuentes.",
    ],
    [("magnitud", "número que mide la fuerza de un sismo"), ("informe oficial", "documento de una institución del Estado con datos y decisiones"), ("testigo", "persona que vio o vivió un hecho"), ("titular", "frase grande que encabeza una noticia"), ("rumor", "cosa que se dice sin que nadie la haya comprobado")],
    [
        ("Elegir la fuente", "Quieres saber qué magnitud tuvo un sismo. ¿Conviene un instrumento científico o el rumor de un vecino?", ["La magnitud se mide con instrumentos.", "Un rumor no se ha comprobado.", "Elijo el registro científico."], "El registro científico"),
        ("Comparar magnitudes", "Tabla: sismo A, magnitud 7,4; sismo B, magnitud 6,9. ¿Cuál fue mayor?", ["Comparo 7,4 con 6,9.", "7,4 es mayor.", "El sismo A tuvo mayor magnitud."], "El sismo A"),
    ],
    [
        ("Creer que la primera cifra de daños siempre es la final.", "Las cifras se corrigen cuando llega más información.", "Revisa la fecha de la fuente y busca la más reciente."),
        ("Usar el relato de un vecino para hablar de todo el país.", "Un testigo cuenta lo que vivió él.", "Agrega otras fuentes."),
    ],
    [
        ("El Servicio Sismológico Nacional registra sismos. ¿Entrega datos científicos o publicidad?", "Datos científicos", "Su función es medir y registrar."),
        ("Un testigo cuenta lo que vivió. ¿Describe la experiencia de una persona o la de todo el país?", "La experiencia de una persona", "Un relato muestra una vivencia."),
        ("«Fue un sismo horrible», ¿es un dato o una opinión?", "Una opinión", "«Horrible» no se mide con instrumentos."),
    ],
    [
        ("¿Por qué las primeras cifras de daños pueden cambiar?", "Porque se corrigen cuando llega más información", "Al comienzo faltan datos."),
        ("¿Por qué sirve comparar un informe oficial con un relato de testigo?", "Uno entrega datos generales y el otro muestra cómo se vivió", "Cada fuente aporta una parte."),
        ("Una fotografía de una casa caída, ¿muestra todo el desastre?", "No, solo lo que se ve en ese lugar", "Una imagen muestra una parte del hecho."),
    ],
    [
        ("Tabla: Valdivia 1960, 9,5; Maule 2010, 8,8; Iquique 2014, 8,2. ¿Qué sismo tuvo la mayor magnitud?", "Valdivia 1960", "9,5 es la cifra mayor."),
        ("En la misma tabla (9,5; 8,8; 8,2), ¿cuál sismo tuvo la menor magnitud?", "Iquique 2014", "8,2 es la cifra menor."),
        ("Un titular dice: «Catástrofe en todo el país». Un informe de ejemplo indica daños en 3 de las 346 comunas de Chile. ¿Cuál fuente es más precisa sobre cuántas comunas se dañaron?", "El informe", "Entrega una cifra concreta y comprobable."),
    ],
    [
        ("Pablo lee el relato de una vecina que dice que se cortó la luz en su calle y concluye: «Toda la ciudad quedó sin luz». ¿Qué límite tiene su conclusión?", "El relato solo describe su calle", "Un relato no muestra toda la ciudad."),
        ("Una foto muestra un puente caído en 2010. Ana dice: «Todos los puentes de Chile cayeron». ¿Qué error comete?", "Generaliza con una sola foto", "Una foto muestra un solo lugar."),
    ],
    [
        ("Ordena los pasos para usar una fuente: A) decidir qué se puede concluir, B) revisar quién la hizo, cuándo y para qué, C) anotar los datos que entrega.", "B, C, A", "Primero la procedencia, luego el contenido y al final la conclusión."),
        ("Una noticia publicada el día del sismo dice «Hay 10 casas dañadas». Un informe publicado un mes después dice «Hay 120 casas dañadas». ¿Qué cifra es más confiable para saber el total de daños?", "La del informe posterior", "Tiene más información y es más reciente."),
    ],
    [("Un niño quiere saber cómo vivieron las familias un aluvión. Puede leer una tabla de datos o el relato de una vecina. ¿Qué fuente le muestra mejor lo que vivió una persona?", "El relato de la vecina", "Cuenta una experiencia concreta.")],
    [("En Historia: ¿qué es un rumor?", "Algo que se dice sin que nadie lo haya comprobado", "Es la definición de la clase."), ("¿Quién mide los sismos en Chile?", "El Servicio Sismológico Nacional", "Es la institución que los registra."), ("¿Se deben usar varias fuentes para entender un desastre?", "Sí", "Cada una muestra solo una parte.")],
    (
        "Lee estas dos fuentes inventadas para practicar. Fuente 1 (informe de una municipalidad): «Tras la lluvia fuerte, 20 viviendas quedaron con barro». Fuente 2 (relato de un vecino): «Fue terrible, el agua se llevó mi huerto». Escribe lo que dice cada una, una conclusión que NO se puede sacar de ellas y una pregunta de procedencia para cada una.",
        "Fuente 1: 20 viviendas con barro. Fuente 2: perdió su huerto. No se puede decir cuántas viviendas se dañaron en toda la región. Preguntas: ¿cuándo se hizo el informe? ¿quién es el vecino?",
        ["resume cada fuente", "incluye una conclusión que no se puede sacar", "formula una pregunta de procedencia por fuente"],
        ["cuatro frases escritas"],
        ["inventar cifras", "mezclar lo que dice cada fuente"],
        "Muestra tus frases a una persona de tu casa y pídele que compruebe que cada dato aparece en la fuente.",
    ),
    "Pregunta a una persona de tu casa dónde se informa cuando hay un sismo y anota la respuesta.",
    "Escribe qué otra fuente usarías para saber más sobre un aluvión.",
)

# ================================================================ OA 14 · clase 3
lesson(
    OA14, 3,
    "Aprenderé a relacionar la causa de un desastre natural con sus consecuencias en el desarrollo de Chile y con las acciones de los actores. Sirve para entender por qué el país tiene normas de construcción y planes de emergencia.",
    ["Sé ubicar y leer fuentes sobre desastres naturales.", "Sé que una causa es una razón y una consecuencia es lo que pasa después."],
    [
        "La causa de los sismos y volcanes en Chile es el choque de placas de la corteza terrestre. La causa de una sequía es la falta de lluvia durante años. La de un aluvión puede ser una lluvia muy fuerte en un lugar donde casi nunca llueve. Los desastres naturales ocurren por la naturaleza, pero el daño también depende de cómo y dónde se construye y de cuánto se preparan las personas.",
        "Las consecuencias son varias. Un sismo fuerte puede dañar viviendas, caminos, puentes, escuelas y puertos. Reconstruir cuesta tiempo y dinero y puede frenar un tiempo el desarrollo de una región. Pero también obliga a cambiar: en Chile las normas de construcción antisísmica son exigentes, hay sistemas de alerta de tsunami, vías de evacuación y simulacros. Ante una sequía se construyen embalses y se reparte agua en camiones aljibe.",
        "Los actores son quienes participan: las familias, las municipalidades, el organismo nacional de emergencias, Bomberos, la Armada, los científicos, las empresas y los voluntarios. Un buen análisis incluye la causa, los actores, la acción, las consecuencias a corto plazo, como la falta de agua o luz, y las consecuencias a largo plazo, como nuevas normas.",
    ],
    [("norma antisísmica", "regla que exige construir de modo que los edificios resistan sismos"), ("reconstrucción", "arreglar o volver a construir lo que se dañó"), ("simulacro", "ensayo de cómo actuar frente a una emergencia"), ("camión aljibe", "camión que lleva agua a lugares donde falta"), ("evacuación", "salir de un lugar peligroso hacia otro seguro")],
    [
        ("Armar la cadena", "Una sequía de varios años deja un valle sin agua para los cultivos. Una cooperativa construye un embalse. Nombra causa, actor y consecuencia.", ["Causa: falta de lluvia durante años.", "Actor: la cooperativa.", "Consecuencia: se guarda agua para los cultivos."], "Causa: falta de lluvia; actor: cooperativa; consecuencia: agua guardada"),
        ("Una consecuencia a largo plazo", "Tras un sismo fuerte, el país exige construir los edificios con normas antisísmicas. ¿Es una consecuencia a corto o a largo plazo?", ["Una norma se aplica durante muchos años.", "No termina cuando termina la emergencia.", "Es de largo plazo."], "A largo plazo"),
    ],
    [
        ("Creer que el daño de un sismo depende solo de su fuerza.", "También depende de cómo y dónde se construye.", "Mira la causa y también la preparación."),
        ("Nombrar a un solo actor, como el gobierno.", "También participan familias, Bomberos, municipalidades y voluntarios.", "Haz una lista de todos los actores."),
    ],
    [
        ("La causa de los sismos en Chile, ¿es el choque de placas o la falta de lluvia?", "El choque de placas", "La falta de lluvia causa sequías."),
        ("Bomberos y la municipalidad, ¿son actores o consecuencias de un desastre?", "Actores", "Son quienes participan en la respuesta."),
        ("Una norma antisísmica, ¿busca evitar daños o aumentarlos?", "Evitar daños", "Obliga a construir más resistente."),
    ],
    [
        ("¿Por qué un desastre puede frenar el desarrollo de una región por un tiempo?", "Porque hay que gastar tiempo y dinero en reconstruir", "Esos recursos se podrían usar en otras cosas."),
        ("¿Por qué las familias participan en simulacros?", "Para saber cómo actuar y evacuar con rapidez", "Preparar a las personas reduce el daño."),
        ("¿Por qué un aluvión puede ocurrir en un desierto?", "Porque una lluvia muy fuerte cae sobre un suelo seco que absorbe poca agua", "El agua que no se absorbe corre por la superficie."),
    ],
    [
        ("Después de un aluvión, el único camino a un pueblo queda cortado. ¿Qué dificultad aparece: el pueblo queda aislado o aumenta el turismo?", "El pueblo queda aislado", "Sin camino no llegan alimentos ni ayuda."),
        ("Una zona de sequía recibe agua en camiones aljibe. ¿Qué problema temporal busca resolver?", "La falta de agua para beber y cocinar", "El camión lleva agua donde no hay."),
        arith("En un plan se reconstruirán 120 viviendas en 4 años, al mismo ritmo cada año. ¿Cuántas viviendas se reconstruyen por año?", "120//4", "Se reparten 120 entre 4 años.", " viviendas"),
    ],
    [
        ("Rosa dice: «Después de un sismo no cambia nada». Con lo aprendido, ¿qué error comete?", "Los sismos llevan a nuevas normas, planes y simulacros", "Los desastres obligan a prepararse mejor."),
        ("Un edificio muy alto tiene normas antisísmicas y otro sin ellas está a su lado. Con el mismo sismo, ¿cuál es más probable que sufra menos daño?", "El que tiene normas antisísmicas", "Fue construido para resistir los movimientos."),
    ],
    [
        ("Ordena la cadena: A) se aprueban nuevas normas de construcción, B) un sismo daña muchos edificios, C) se estudia qué falló.", "B, C, A", "Primero el hecho, luego el análisis y por último las normas."),
        ("Una ciudad costera dañada por un tsunami decide marcar rutas de evacuación con señales hacia lugares altos. ¿Cuál es la causa de esa decisión?", "El peligro de un nuevo tsunami", "Se busca proteger a las personas de otra ola."),
    ],
    [("Una escuela de una zona de sismos hace simulacros cada semestre. ¿Qué actor organiza el simulacro: la escuela o los volcanes?", "La escuela", "Los volcanes no participan; las personas de la escuela sí.")],
    [("¿Qué es una norma antisísmica?", "Una regla para construir edificios que resistan sismos", "Es la definición de la clase."), ("¿Qué causa los sismos y volcanes de Chile?", "El choque de placas", "Es la causa natural."), ("¿Qué es una evacuación?", "Salir de un lugar peligroso hacia otro seguro", "Es la definición de la clase.")],
    (
        "Elige un caso y escribe causa, dos actores, una consecuencia a corto plazo y una a largo plazo. Caso a) un sismo daña escuelas en el centro del país; caso b) una sequía seca los pozos de un pueblo; caso c) una erupción cubre de ceniza una ciudad del sur.",
        "Caso b: causa: poca lluvia; actores: familias y municipalidad; corto plazo: camiones aljibe; largo plazo: nuevos pozos y uso cuidadoso del agua.",
        ["nombra la causa natural", "incluye al menos dos actores", "distingue corto y largo plazo"],
        ["cinco frases escritas"],
        ["mezclar causa con consecuencia", "olvidar el largo plazo"],
        "Lee tus frases a una persona de tu casa y pídele que diga cuál es la causa y cuál la consecuencia.",
    ),
    "Escribe dos cosas que hay que hacer en tu casa si ocurre un sismo, según las indicaciones de tu escuela.",
    "Escribe una pregunta que le harías a un científico sobre los sismos.",
)

# ================================================================ OA 14 · clase 4
lesson(
    OA14, 4,
    "Aprenderé a comparar cómo afectan los desastres naturales al norte, al centro y al sur de Chile y a reconocer perspectivas distintas. Sirve para ver que cada territorio enfrenta riesgos y respuestas propias.",
    ["Sé relacionar causas y consecuencias de los desastres.", "Sé usar criterios para comparar."],
    [
        "Comparar territorios es ver en qué se parecen y en qué cambian al enfrentar los desastres. Usamos criterios iguales: qué desastre ocurrió, qué daño principal causó y qué respuesta hubo. En el norte hubo el sismo de Iquique en 2014 y el aluvión de Atacama en 2015. En el centro hubo el sismo de 2010 y hay una sequía prolongada. En el sur hubo el sismo de Valdivia en 1960 y las erupciones del Chaitén en 2008 y del Calbuco en 2015.",
        "Los riesgos se repiten, pero no son iguales en todos los lugares. Por ejemplo, la sequía afecta más a la agricultura de la zona central; los volcanes afectan a las zonas cercanas del sur; los sismos pueden ocurrir en todo el país. También cambia la respuesta: en el norte se necesitan rutas de evacuación en la costa; en el centro, embalses y ahorro de agua; en el sur, planes de evacuación cerca de los volcanes.",
        "Una perspectiva es la mirada de una persona según su situación. Un agricultor mira la sequía por su cosecha, una autoridad por la seguridad de todos y un científico por los datos. Comparar perspectivas ayuda a entender el mismo desastre desde varios lados sin decir que una mirada es la única válida.",
    ],
    [("territorio", "lugar con sus paisajes, recursos y personas"), ("riesgo", "posibilidad de que ocurra un daño"), ("criterio", "regla igual para comparar dos cosas"), ("perspectiva", "mirada de una persona según su situación"), ("plan de evacuación", "plan para salir con rapidez hacia un lugar seguro")],
    [
        ("Comparar con un criterio", "Zona norte: sismo 2014 y aluvión 2015. Zona sur: sismo de Valdivia 1960 y erupciones de 2008 y 2015. Compara el criterio «tipo de desastre».", ["En el norte: sismo y aluvión.", "En el sur: sismo y erupciones volcánicas.", "Ambos tuvieron sismos, pero solo el sur tuvo erupciones."], "Ambos tuvieron sismos; el sur también tuvo erupciones"),
        ("Dos perspectivas", "Un agricultor del centro y un científico miran la sequía. ¿Qué mira cada uno?", ["El agricultor mira cuánta agua tienen sus cultivos.", "El científico mira los datos de lluvia.", "Son perspectivas distintas del mismo hecho."], "El agricultor, sus cultivos; el científico, los datos"),
    ],
    [
        ("Decir que un territorio sufre más que otro sin criterios.", "Cada territorio tiene riesgos distintos.", "Compara con criterios iguales."),
        ("Creer que solo hay una perspectiva válida.", "Cada persona ve según su situación.", "Escucha al menos dos miradas."),
    ],
    [
        ("Los volcanes que hicieron erupción en 2008 y 2015, ¿están en el norte o en el sur?", "En el sur", "El Chaitén y el Calbuco están en el sur de Chile."),
        ("La sequía prolongada de las últimas décadas, ¿afecta especialmente a la zona central o a la Antártica?", "A la zona central", "Allí se concentra la agricultura que depende de la lluvia."),
        ("Un criterio de comparación, ¿es una regla igual para ambos lugares o una opinión?", "Una regla igual para ambos lugares", "Así se compara lo mismo."),
    ],
    [
        ("¿Por qué una zona con volcanes tiene planes de evacuación diferentes a una zona con sequía?", "Porque los riesgos y daños son distintos", "El plan depende del desastre posible."),
        ("¿Por qué un agricultor y una autoridad pueden mirar distinto una sequía?", "Porque tienen necesidades y responsabilidades distintas", "Eso es tener perspectivas distintas."),
        ("¿Por qué los sismos exigen preparación en todo el país?", "Porque pueden ocurrir en cualquier zona", "Chile está en una zona de placas que chocan."),
    ],
    [
        ("Tabla: norte, aluvión 2015 (agua con barro); sur, erupción Calbuco 2015 (ceniza). ¿Qué desastre de la tabla tiene que ver con las lluvias fuertes?", "El aluvión", "El agua con barro baja por lluvias intensas."),
        ("Con la misma tabla: ¿qué desastre produce ceniza?", "La erupción del Calbuco", "Los volcanes expulsan ceniza al hacer erupción."),
        ("Tabla: Zona A, sequía, respuesta embalses; Zona B, tsunami, respuesta rutas de evacuación. ¿Cuál zona necesita señalizar rutas hacia lugares altos?", "La zona B", "El tsunami exige evacuar hacia lugares altos."),
    ],
    [
        ("Marta dice: «El sur no necesita prepararse para sismos porque tiene volcanes». ¿Qué error comete?", "En el sur también ocurren sismos, como el de Valdivia en 1960", "Los volcanes no reemplazan la preparación para sismos."),
        ("Una autoridad dice: «Hay que evacuar la costa». Un pescador dice: «Mi bote está en el puerto». ¿Son perspectivas iguales o distintas?", "Distintas", "Una mira la seguridad y el otro su trabajo."),
    ],
    [
        ("Ordena de norte a sur los desastres: A) erupción del Calbuco, B) sismo de Iquique, C) sequía de la zona central.", "B, C, A", "Iquique en el norte, zona central en el centro y Calbuco en el sur."),
        arith("Entre el sismo de Iquique (2014) y el aluvión de Atacama (2015), ¿cuántos años pasaron?", "2015-2014", "Se resta el año anterior al posterior.", " año"),
    ],
    [("En un pueblo del centro hay sequía y un vecino propone ahorrar agua en las casas. Otro propone construir un embalse. ¿Qué actor puede hacer la primera propuesta sin ayuda de grandes obras: las familias o el Estado?", "Las familias", "Ahorrar agua en casa depende de las familias; un embalse necesita obras mayores.")],
    [("¿Qué es una perspectiva?", "La mirada de una persona según su situación", "Es la definición de la clase."), ("¿Qué zona sufre más la sequía prolongada?", "La zona central", "La agricultura depende de la lluvia."), ("¿Qué sirve para comparar dos territorios?", "Usar los mismos criterios", "Así se compara lo mismo.")],
    (
        "Completa esta tabla con una frase por casilla: columnas norte / centro / sur; filas desastre ocurrido, daño principal y respuesta. Puedes usar esta información: norte, sismo y aluvión, daños en viviendas y caminos, rutas de evacuación; centro, sequía, falta de agua para cultivos, embalses; sur, erupciones, ceniza sobre ciudades, planes de evacuación. Luego escribe una semejanza y una diferencia.",
        "Semejanza: en las tres zonas hay riesgos y respuestas. Diferencia: en el centro el problema es la falta de agua y en el sur la ceniza.",
        ["completa las tres columnas", "escribe una semejanza y una diferencia", "usa los mismos criterios en cada zona"],
        ["tabla de 3 por 3 y dos frases"],
        ["comparar con criterios distintos", "decir que una zona es la peor"],
        "Pide a una persona de tu casa que lea tu tabla y diga si la información es clara.",
    ),
    "Escribe un riesgo natural que existe en tu comuna y qué haces para prepararte.",
    "Escribe una pregunta para entrevistar a una autoridad sobre cómo se prepara tu región.",
)

# ================================================================ OA 15 · clase 1
lesson(
    OA15, 1,
    "Aprenderé a ubicar los tres poderes del Estado y los cargos de elección popular de Chile, y cuánto dura cada uno. Sirve para saber quién toma decisiones en el país y en mi comuna.",
    ["Sé que Chile es una república y que las personas votan.", "Sé que la comuna tiene una municipalidad."],
    [
        "En Chile el poder del Estado se divide en tres para que no quede en una sola persona. El Poder Ejecutivo lo encabeza el Presidente de la República y gobierna y administra el país. El Poder Legislativo es el Congreso Nacional, formado por la Cámara de Diputadas y Diputados y el Senado, y hace las leyes. El Poder Judicial son los tribunales, que aplican las leyes y resuelven los conflictos. Este reparto se llama división de poderes.",
        "Algunos cargos se eligen por voto de las personas, y por eso se llaman cargos de elección popular: los concejales y el alcalde, que trabajan en la comuna; los diputados y los senadores, que forman el Congreso; y el Presidente. El Presidente, el alcalde, los concejales y los diputados duran 4 años. Los senadores duran 8 años.",
        "Para ubicar estas instituciones pensamos en el espacio y el tiempo. La municipalidad está en cada comuna; el Congreso funciona en la ciudad de Valparaíso; el Presidente trabaja en el Palacio de La Moneda, en Santiago. Y cada cargo tiene una fecha en que termina su período, o sea el tiempo que dura en el cargo.",
    ],
    [("división de poderes", "reparto del poder del Estado en Ejecutivo, Legislativo y Judicial"), ("cargo de elección popular", "cargo que se llena con el voto de las personas"), ("concejal", "persona elegida para trabajar junto al alcalde en una comuna"), ("período", "tiempo que una persona dura en un cargo"), ("ley", "regla que debe cumplir toda la sociedad")],
    [
        ("Clasificar una función", "Una institución hace las leyes del país. ¿Qué poder del Estado es?", ["Hacer leyes es crear reglas.", "Esa función es del Congreso.", "Es el Poder Legislativo."], "Poder Legislativo"),
        ("Calcular el fin de un período", "Una alcaldesa de ejemplo asumió en 2024. Su período dura 4 años. ¿En qué año termina?", ["Sumo 4 años a 2024.", "2024 más 4 es 2028."], "En 2028"),
    ],
    [
        ("Pensar que el Presidente hace todas las leyes.", "Las leyes las hace el Congreso, aunque el Presidente puede proponer proyectos.", "Separa quién gobierna (Ejecutivo) de quién hace las leyes (Legislativo)."),
        ("Creer que los jueces se eligen por voto popular.", "Los jueces no se eligen por voto; trabajan en el Poder Judicial.", "Recuerda los cargos de elección popular: concejales, alcalde, diputados, senadores y Presidente."),
    ],
    [
        ("¿Quién gobierna y administra el país: el Presidente o los tribunales?", "El Presidente", "Encabeza el Poder Ejecutivo."),
        ("¿Dónde trabaja el alcalde: en la municipalidad o en el Senado?", "En la municipalidad", "El alcalde dirige la comuna."),
        ("¿Quiénes aplican las leyes y resuelven conflictos: los tribunales o los diputados?", "Los tribunales", "Son el Poder Judicial."),
    ],
    [
        ("¿Por qué el poder del Estado se divide en tres?", "Para que no quede en una sola persona", "Así se evita el abuso de poder."),
        ("¿Qué significa «cargo de elección popular»?", "Un cargo que se llena con el voto de las personas", "Así se definió en el vocabulario."),
        ("¿Cuál es la diferencia entre el Poder Ejecutivo y el Legislativo?", "El Ejecutivo gobierna y el Legislativo hace las leyes", "Cada poder tiene una función distinta."),
    ],
    [
        ("Un senador de ejemplo asumió en 2022. Su período dura 8 años. ¿En qué año termina?", "En 2030", "2022 más 8 es 2030.", "2022+8"),
        ("Tres cargos: concejal, juez, senador. ¿Cuál NO se elige por voto popular?", "Juez", "Los jueces no se eligen por voto popular."),
        ("En una tabla de ejemplo: cargo, Presidente, 4 años; senador, 8 años. ¿Cuántos años más dura un senador que el Presidente?", "4", "8 menos 4 es 4.", "8-4"),
    ],
    [
        ("Luis dice: «El alcalde es del Poder Judicial porque resuelve problemas». ¿Qué error comete?", "El alcalde dirige la comuna, no es parte del Poder Judicial", "Resolver problemas no basta para ser juez."),
        ("Una ley dice que todos deben usar casco al andar en bicicleta. ¿Qué poder la hizo: el Legislativo o el Judicial?", "El Legislativo", "Hacer leyes es su función."),
    ],
    [
        ("Ordena de la comuna al país los cargos: A) Presidente, B) alcalde, C) diputado.", "B, C, A", "El alcalde es de la comuna, el diputado de su distrito y el Presidente de todo el país."),
        ("Una diputada de ejemplo asumió en 2022 y una concejala de ejemplo asumió en 2024. Ambos cargos duran 4 años. ¿Cuál de los dos períodos termina antes?", "El de la diputada", "Termina en 2026, antes que el de la concejala, que termina en 2028."),
    ],
    [("En la comuna de Lagos de Ejemplo hay un problema de basura en la plaza. ¿A quién le corresponde decidir primero sobre la limpieza de la plaza: al alcalde o al Presidente?", "Al alcalde", "La plaza es un asunto de la comuna.")],
    [("En Historia: ¿cuáles son los tres poderes del Estado?", "Ejecutivo, Legislativo y Judicial", "Es la división de poderes."), ("¿Cuánto dura un senador en su cargo?", "8 años", "Su período es más largo que el de otros cargos."), ("¿Qué es un cargo de elección popular?", "Un cargo que se llena con el voto de las personas", "Es la definición de la clase.")],
    (
        "Completa este cuadro con los cargos de elección popular: cargo, dónde trabaja (comuna, Congreso o La Moneda), cuánto dura. Cargos: concejal, alcalde, diputado, senador, Presidente. Luego escribe, solo para diputado, senador y Presidente, qué poder del Estado integran.",
        "Alcalde: municipalidad, 4 años. Senador: Congreso, 8 años, Poder Legislativo. Presidente: La Moneda, 4 años, Poder Ejecutivo.",
        ["completa los cinco cargos", "usa 4 u 8 años según el cargo", "relaciona cada cargo con su lugar de trabajo"],
        ["cuadro de cinco filas"],
        ["poner a los jueces como cargo electo", "confundir los años"],
        "Pide a una persona de tu casa que te pregunte por un cargo y respóndele sin mirar el cuadro.",
    ),
    "Escribe un cargo de elección popular que conozcas y qué hace.",
    "Escribe una pregunta que le harías a un concejal de tu comuna.",
)

# ================================================================ OA 15 · clase 2
lesson(
    OA15, 2,
    "Aprenderé a leer fuentes sobre la democracia: resultados de elecciones, textos de la Constitución y propaganda, y a preguntar quién las hizo. Sirve para distinguir información oficial de propaganda.",
    ["Sé cuáles son los poderes del Estado y los cargos de elección popular.", "Sé que una fuente tiene una procedencia."],
    [
        "Para entender cómo funciona la democracia usamos fuentes. El Servicio Electoral (Servel) organiza las elecciones y entrega los resultados oficiales. La Constitución, que es la ley más importante, dice cómo se organiza el Estado. Los diarios cuentan lo que ocurre. Los afiches de propaganda los hacen los candidatos para convencer.",
        "Preguntamos por la procedencia: quién hizo la fuente, cuándo y para qué. Un resultado oficial cuenta los votos. Un afiche dice «Vota por mí, soy el mejor» y es una opinión del candidato, no un dato. Un titular puede resaltar solo una parte. Por eso comparamos varias fuentes antes de concluir.",
        "En una elección gana quien obtiene más votos, y para saberlo se cuentan los votos. Con una tabla podemos calcular el total de votos y la diferencia entre candidatos. Pero una tabla de un solo lugar no nos dice qué pasó en todo el país.",
    ],
    [("Servel", "organismo que organiza las elecciones y entrega los resultados oficiales"), ("Constitución", "ley más importante del país, que organiza el Estado"), ("propaganda", "mensaje que busca convencer a las personas"), ("candidato", "persona que se presenta para ser elegida"), ("voto", "forma en que una persona elige a quien la representará")],
    [
        ("Leer una tabla de votos", "Elección de alcalde, comuna de ejemplo: Ana, 4.200 votos; Beto, 3.100 votos; Carla, 2.700 votos. ¿Quién obtuvo más votos?", ["Comparo los tres números.", "4.200 es el mayor.", "Ana obtuvo más votos."], "Ana"),
        ("Distinguir dato y opinión", "Afiche: «Pedro es el mejor candidato». ¿Es un dato o una opinión?", ["«El mejor» no se mide con un número.", "Lo dice el propio candidato.", "Es una opinión."], "Una opinión"),
    ],
    [
        ("Creer que lo que dice un afiche es un dato comprobado.", "El afiche lo hace el candidato para convencer.", "Pregunta quién lo hizo y para qué."),
        ("Pensar que una tabla de una comuna muestra el resultado de todo el país.", "La tabla describe solo esa comuna.", "Di solo lo que muestra la tabla."),
    ],
    [
        ("¿Quién organiza las elecciones y entrega resultados oficiales: el Servel o un candidato?", "El Servel", "Es el organismo encargado."),
        ("La Constitución, ¿es la ley más importante del país o un afiche?", "La ley más importante del país", "Organiza el Estado."),
        ("Un afiche de propaganda, ¿busca informar con datos o convencer?", "Convencer", "Lo hace el candidato para obtener votos."),
    ],
    [
        ("¿Por qué conviene preguntar quién hizo un afiche?", "Porque un candidato lo hace para convencer", "Su propósito es obtener votos."),
        ("¿Por qué no basta una tabla de una comuna para decir quién ganó en todo el país?", "Porque solo muestra esa comuna", "Faltan los resultados de los demás lugares."),
        ("¿Para qué sirve comparar varias fuentes sobre una elección?", "Para comprobar que la información coincide", "Así se evitan errores o exageraciones."),
    ],
    [
        arith("Con la tabla de otra comuna de ejemplo: Dora, 5.000 votos; Enzo, 3.800 votos. ¿Cuántos votos más obtuvo Dora?", "5000-3800", "Se resta los votos de Enzo a los de Dora.", " votos"),
        arith("Tabla de ejemplo: Fabián, 1.500 votos; Gaby, 2.500 votos; Hugo, 1.000 votos. ¿Cuántos votos se emitieron en total?", "1500+2500+1000", "Se suman los votos de los tres candidatos.", " votos"),
        ("Un afiche dice «Mi propuesta: más árboles en la plaza». ¿Es una propuesta o un resultado de la elección?", "Una propuesta", "Dice qué haría, no cuántos votos obtuvo."),
    ],
    [
        ("Ema ve un afiche con la frase «Todos me apoyan» y concluye: «Entonces ganó». ¿Qué error comete?", "Un afiche no prueba cuántos votos obtuvo", "Los resultados oficiales muestran quién ganó."),
        ("Un diario dice «Elección reñida» y la tabla de ejemplo muestra 5.001 votos contra 4.999. ¿Qué dato respalda el titular?", "La diferencia es de solo 2 votos", "5.001 menos 4.999 son 2."),
    ],
    [
        ("Ordena los pasos para analizar una fuente electoral: A) calcular o concluir, B) leer quién la hizo, C) revisar los datos.", "B, C, A", "Primero la procedencia, luego los datos y al final la conclusión."),
        ("Resultados de ejemplo de una comuna: Ida, 40 % de los votos; Juan, 35 %; Kira, 25 %. ¿Qué porcentaje suman los tres?", "100 %", "40 más 35 más 25 es 100.", "40+35+25"),
    ],
    [("Un vecino lee que Raúl tuvo 6.300 votos en la elección de alcalde de su comuna y comenta: «Eso significa que ganó en el país». ¿Qué falta para afirmar eso?", "Resultados de todo el país", "Una comuna no representa a todo el país.")],
    [("En Historia: ¿qué es el Servel?", "El organismo que organiza las elecciones y entrega resultados oficiales", "Es la definición de la clase."), ("¿Qué es propaganda?", "Un mensaje que busca convencer", "Es la definición de la clase."), ("¿Qué es la Constitución?", "La ley más importante del país", "Organiza el Estado.")],
    (
        "Lee este afiche inventado: «Vota por Marcela. Plaza segura, iluminación y más áreas verdes. Tu comuna merece lo mejor». Escribe qué propone, qué es una opinión y qué dato se necesitaría para saber si cumplirá. Luego inventa una pregunta de procedencia.",
        "Propone seguridad, iluminación y áreas verdes. Opinión: «Tu comuna merece lo mejor». Dato: cuántas plazas tienen iluminación hoy. Pregunta: ¿quién pagó el afiche?",
        ["distingue propuesta de opinión", "señala un dato necesario", "formula una pregunta de procedencia"],
        ["cuatro frases escritas"],
        ["confundir opinión con propuesta", "no pedir un dato"],
        "Pide a una persona de tu casa que subraye en tu texto cuál frase es opinión.",
    ),
    "Mira un afiche de propaganda o aviso y escribe qué propone y a quién busca convencer.",
    "Escribe una pregunta para un candidato que permita comprobar su propuesta.",
)

# ================================================================ OA 15 · clase 3
lesson(
    OA15, 3,
    "Aprenderé a relacionar las causas y consecuencias de dividir el poder, de elegir autoridades y de participar. Sirve para entender por qué una democracia necesita ciudadanos que se informen y voten.",
    ["Sé cuáles son los tres poderes y los cargos electos.", "Sé leer fuentes electorales."],
    [
        "La causa de dividir el poder es evitar que una sola persona o grupo tenga demasiada fuerza. La consecuencia es que los poderes se controlan entre sí: el Congreso hace las leyes, el Presidente las promulga y los tribunales las aplican. Si una autoridad comete una falta, otro poder puede revisarla.",
        "Así nace una ley: un proyecto de ley lo pueden presentar el Presidente o los parlamentarios, o sea los diputados y senadores. Se discute en la Cámara de Diputadas y Diputados y en el Senado. Si ambas cámaras lo aprueban, el Presidente lo promulga, o sea lo firma y lo hace oficial, y empieza a regir. Cada paso es una oportunidad de revisar y mejorar la propuesta.",
        "La participación ciudadana también tiene consecuencias. Cuando muchas personas votan, las autoridades representan mejor a la sociedad. Cuando pocas votan, las decisiones las toma un grupo pequeño. Participar no es solo votar: también sirve organizarse en una junta de vecinos, en el centro de estudiantes o enviar una propuesta a la municipalidad.",
    ],
    [("promulgar", "firmar una ley para que empiece a regir"), ("proyecto de ley", "propuesta de ley que se discute antes de aprobarse"), ("parlamentario", "diputado o senador"), ("participación ciudadana", "acciones de las personas para influir en las decisiones de su comunidad"), ("representar", "hablar y decidir en nombre de otras personas")],
    [
        ("Seguir una ley", "Un proyecto de ley fue aprobado por la Cámara de Diputadas y Diputados y por el Senado. ¿Quién lo promulga?", ["Ya fue aprobado por ambas cámaras.", "El último paso es firmarlo.", "Lo promulga el Presidente."], "El Presidente"),
        ("Causa y consecuencia", "Si el Congreso aprobara una ley que contradice la Constitución, un tribunal puede revisarla. ¿Qué logra la división de poderes en este caso?", ["Hay poderes distintos.", "Uno puede revisar al otro.", "Se evita el abuso."], "Que un poder pueda revisar al otro y se evite el abuso"),
    ],
    [
        ("Creer que votar es la única forma de participar.", "También se participa en juntas de vecinos, centros de estudiantes y propuestas a la municipalidad.", "Piensa en todas las formas de involucrarse."),
        ("Pensar que una ley nace solo por decisión del Presidente.", "La discuten el Congreso y el Presidente la promulga.", "Sigue todos los pasos."),
    ],
    [
        ("¿Quién promulga una ley: el Presidente o un alcalde?", "El Presidente", "Firma la ley aprobada por el Congreso."),
        ("¿Quiénes son los parlamentarios: los diputados y senadores o los jueces?", "Los diputados y senadores", "Forman el Congreso."),
        ("Participar en el centro de estudiantes, ¿es un ejemplo de participación ciudadana?", "Sí", "Es organizarse para influir en decisiones de la comunidad."),
    ],
    [
        ("¿Por qué conviene que los poderes se controlen entre sí?", "Para evitar que una persona o grupo tenga demasiado poder", "Así se previene el abuso."),
        ("¿Por qué una ley se discute en dos cámaras?", "Para revisarla más de una vez y mejorarla", "Cada cámara puede cambiarla."),
        ("¿Qué pasa si pocas personas participan en una elección?", "Decide un grupo pequeño y las autoridades representan peor a la sociedad", "La participación amplia da más legitimidad."),
    ],
    [
        ("Ordena los pasos de una ley: A) el Presidente la promulga, B) se presenta un proyecto, C) ambas cámaras la aprueban.", "B, C, A", "Primero el proyecto, luego la aprobación y al final la promulgación."),
        ("Vecinos de una población envían una carta a la municipalidad pidiendo un semáforo. ¿Es un ejemplo de participación ciudadana o de promulgar una ley?", "De participación ciudadana", "Es una acción de las personas para influir en una decisión."),
        arith("En una comuna de ejemplo votaron 6.000 de las 10.000 personas con derecho a voto. ¿Cuántas personas no votaron?", "10000-6000", "Se resta los votantes al total.", " personas"),
    ],
    [
        ("Teo dice: «Si el Presidente quiere una ley, la puede hacer solo». ¿Qué error comete?", "La ley debe discutirse y aprobarse en el Congreso", "El Presidente la promulga, pero no la crea solo."),
        ("Una comuna de ejemplo tiene 10.000 personas con derecho a voto. En la elección A votaron 8.000 y en la B votaron 3.000. ¿En cuál elección representa mejor la decisión de la comunidad?", "En la A", "Participó una proporción mayor de personas."),
    ],
    [
        ("Ordena la cadena: A) se eligen autoridades que representan a todos, B) muchas personas votan, C) las personas se informan sobre los candidatos.", "C, B, A", "Primero se informan, luego votan y de eso resulta la representación."),
        ("Un alcalde de ejemplo propone cerrar una calle y los vecinos reúnen firmas para oponerse. ¿Qué forma de participación usan?", "Reunir firmas", "Es una acción ciudadana para influir en una decisión."),
    ],
    [("En una escuela se elige centro de estudiantes. El 90 % de los cursos participa y se discuten propuestas. ¿Esa elección es un ejemplo de participación amplia o escasa?", "Amplia", "Casi todos los cursos participan.")],
    [("¿Qué significa promulgar?", "Firmar una ley para que empiece a regir", "Es la definición de la clase."), ("¿Para qué se divide el poder?", "Para evitar que una persona o grupo tenga demasiado poder", "Es la causa de la división."), ("Además de votar, ¿qué otra forma de participar existe?", "Organizarse en una junta de vecinos o centro de estudiantes", "Hay varias formas de participar.")],
    (
        "Elige uno de estos casos y escribe la cadena de causas y consecuencias con al menos dos actores. Caso a) un proyecto de ley sobre cuidado de plazas; caso b) una elección de centro de estudiantes con poca participación; caso c) los vecinos piden un semáforo a la municipalidad.",
        "Caso c: causa: cruce peligroso; actores: vecinos, municipalidad; consecuencia: se instala el semáforo y mejora la seguridad.",
        ["nombra la causa", "menciona al menos dos actores", "explica la consecuencia"],
        ["cadena escrita en tres partes"],
        ["omitir actores", "no explicar la consecuencia"],
        "Lee tu cadena a una persona de tu casa y pídele que diga qué actor tiene el papel más importante.",
    ),
    "Escribe una forma de participar que podrías hacer hoy en tu curso o en tu barrio.",
    "Escribe una pregunta sobre cómo se hace una ley que quisieras responder.",
)

# ================================================================ OA 15 · clase 4
lesson(
    OA15, 4,
    "Aprenderé a comparar a quién representa cada cargo de elección popular y a reconocer perspectivas distintas ante un mismo problema. Sirve para saber a quién acudir según el tipo de problema.",
    ["Sé qué cargos son de elección popular.", "Sé que una perspectiva es la mirada de una persona."],
    [
        "Cada cargo de elección popular representa a un territorio distinto. El alcalde y los concejales representan a la comuna. Los diputados representan a un distrito, que agrupa varias comunas. Los senadores representan a una región. El Presidente representa a todo el país. Por eso un problema pequeño de un barrio suele corresponder a la municipalidad, y una ley para todo el país, al Congreso.",
        "Para comparar usamos criterios iguales: a quién representa, qué función cumple y qué tipo de problemas atiende. El alcalde administra la comuna, los concejales revisan y aprueban decisiones locales, los parlamentarios hacen leyes y el Presidente gobierna el país. Todos deben respetar la Constitución.",
        "También hay perspectivas distintas. Un vecino quiere que arreglen su calle. Un comerciante quiere más seguridad. Un estudiante quiere más áreas verdes. Una autoridad debe escuchar a todos y decidir pensando en el bien común. Comparar perspectivas no significa que una sea mejor; significa entender qué necesita cada persona.",
    ],
    [("distrito", "grupo de comunas que elige a sus diputados"), ("región", "gran división territorial de Chile; tiene 16"), ("representación", "hecho de que una persona hable por otras"), ("bien común", "condiciones que ayudan a todos a vivir bien"), ("perspectiva", "mirada de una persona según su situación")],
    [
        ("Elegir a quién acudir", "Un vecino quiere que reparen un pozo en la calle de su barrio. ¿A quién acude primero: al alcalde o al Presidente?", ["El pozo está en una calle de la comuna.", "La comuna la administra el alcalde.", "Acude al alcalde."], "Al alcalde"),
        ("Comparar a quién representan", "Un diputado y un senador. ¿Quién representa a una región completa?", ["Los diputados representan un distrito.", "Los senadores representan una región.", "Es el senador."], "El senador"),
    ],
    [
        ("Pensar que el Presidente decide todos los problemas de un barrio.", "Los asuntos de la comuna corresponden al alcalde y a los concejales.", "Pregunta qué territorio afecta el problema."),
        ("Creer que una perspectiva es la única válida.", "Cada persona ve el problema según su situación.", "Escucha varias miradas."),
    ],
    [
        ("¿A quién representa el Presidente: a una comuna o a todo el país?", "A todo el país", "Gobierna la nación completa."),
        ("¿Quién representa a la comuna: el alcalde o el senador?", "El alcalde", "Dirige la comuna."),
        ("¿Quiénes hacen las leyes: los concejales o el Congreso?", "El Congreso", "Los concejales trabajan en la comuna."),
    ],
    [
        ("¿Por qué hay cargos que representan territorios distintos?", "Porque los problemas son de distinto tamaño: barrio, comuna, región o país", "Cada nivel atiende lo que le corresponde."),
        ("¿Por qué una autoridad debe escuchar varias perspectivas?", "Porque las personas tienen necesidades distintas", "Decidir pensando en el bien común exige escuchar a todos."),
        ("¿Qué significa «bien común»?", "Condiciones que ayudan a todos a vivir bien", "Así se definió en el vocabulario."),
    ],
    [
        ("Un problema: no hay luz en una plaza de la comuna. ¿Quién tiene la función principal de resolverlo: el concejo municipal o el Senado?", "El concejo municipal", "Es un asunto local."),
        ("Un problema: una nueva ley sobre cuidado del agua para todo el país. ¿Quiénes la discuten: los concejales o los parlamentarios?", "Los parlamentarios", "Son quienes hacen las leyes."),
        ("Un vecino quiere más iluminación y un comerciante quiere más estacionamientos. ¿Son perspectivas iguales o distintas?", "Distintas", "Cada uno prioriza su necesidad."),
    ],
    [
        ("Rosa dice: «Los senadores representan solo mi comuna». ¿Qué error comete?", "Los senadores representan a una región completa", "Su territorio es mayor que una comuna."),
        ("Dos vecinos: uno pide más árboles y otro pide más estacionamientos en la misma plaza. ¿Qué debería hacer una autoridad según el bien común?", "Escuchar a ambos y buscar una solución que beneficie a la comunidad", "El bien común toma en cuenta a todos."),
    ],
    [
        ("Ordena de menor a mayor territorio: A) región, B) comuna, C) país.", "B, A, C", "La comuna está dentro de la región y esta dentro del país."),
        ("Tres problemas: A) arreglar una calle, B) cambiar una ley nacional, C) decidir sobre un hospital regional. ¿Cuál corresponde principalmente a los parlamentarios?", "B", "Cambiar una ley nacional lo hace el Congreso."),
    ],
    [("En una comuna de ejemplo hay tres opiniones sobre una plaza: una vecina quiere juegos para niños, un adulto mayor quiere bancas y un joven quiere una cancha. ¿Qué criterio común permite compararlas?", "Qué necesita cada persona de la plaza", "Todas hablan de usos distintos del mismo espacio.")],
    [("¿A quién representan los senadores?", "A una región", "Es el territorio que representan."), ("¿Qué es el bien común?", "Condiciones que ayudan a todos a vivir bien", "Es la definición de la clase."), ("¿Quién representa a una comuna?", "El alcalde", "Dirige la municipalidad.")],
    (
        "Completa esta tabla de cargos con una frase por casilla: concejal, alcalde, diputado, senador, Presidente; columnas: territorio que representa y ejemplo de problema que atiende. Luego elige una de estas dos situaciones y explica a quién acudirías: a) falta alumbrado en tu calle; b) se necesita una ley para proteger los glaciares del país.",
        "Situación a: acudo al alcalde o al concejo municipal porque es un asunto de la comuna.",
        ["relaciona cada cargo con su territorio", "da un problema adecuado para cada cargo", "justifica a quién acudir"],
        ["tabla de cinco filas y una justificación"],
        ["confundir diputado con senador", "elegir al Presidente para un problema de barrio"],
        "Pregunta a una persona de tu casa si sabe cómo se llama el alcalde de tu comuna y anótalo.",
    ),
    "Escribe un problema de tu barrio y a qué cargo le corresponde atenderlo.",
    "Escribe una pregunta que le harías a un diputado de tu distrito.",
)

# ================================================================ OA 15 · clase 5
lesson(
    OA15, 5,
    "Aprenderé a argumentar con evidencia por qué es importante la participación ciudadana en una democracia. Sirve para defender una idea con datos y razones.",
    ["Sé qué cargos se eligen y a quién representan.", "Sé separar dato, opinión y conclusión."],
    [
        "Argumentar es defender una idea con evidencia y razones. Un argumento tiene tres partes: una afirmación, que es lo que sostengo; una evidencia, que es un dato que la apoya; y una razón, que explica por qué ese dato apoya la afirmación. También decimos qué límite tiene la evidencia.",
        "Veamos un ejemplo con una comuna inventada. Afirmación: «Participar es importante». Evidencia: en una votación en que solo participó el 20 % de las personas, las propuestas ganadoras beneficiaron a un grupo pequeño. Razón: si participan pocas personas, se escucha a pocas. Límite: es un solo caso y no sabemos qué pasó en otras comunas.",
        "En Chile, las personas mayores de 18 años deben votar en las elecciones. Pero la participación va más allá del voto. Se participa al informarse, al organizarse en una junta de vecinos, al presentar una propuesta en el municipio o al elegir un centro de estudiantes. Las democracias funcionan mejor cuando muchas personas participan de manera informada.",
    ],
    [("argumento", "idea defendida con evidencia y razones"), ("evidencia", "dato o fuente que apoya una afirmación"), ("participación", "acciones de las personas para influir en las decisiones de la comunidad"), ("junta de vecinos", "organización de vecinos de un barrio"), ("límite", "lo que la evidencia no permite saber")],
    [
        ("Identificar la evidencia", "Frase: «Participar es útil, porque en la comuna X, con 70 % de votantes, se escucharon propuestas de varios barrios». ¿Cuál es la evidencia?", ["La afirmación es que participar es útil.", "El dato es el 70 % de votantes y las propuestas de varios barrios.", "Esa es la evidencia."], "El 70 % de votantes y las propuestas de varios barrios"),
        ("Reconocer un límite", "Un dato de una sola comuna muestra que votaron 7 de cada 10 personas. ¿Qué no permite saber?", ["Es una sola comuna.", "No habla de otras.", "No permite afirmar lo mismo de todo el país."], "Cómo participan otras comunas"),
    ],
    [
        ("Dar una opinión sin ningún dato que la apoye.", "Una opinión sin evidencia no se puede comprobar.", "Agrega un dato o una fuente."),
        ("Generalizar con el resultado de una sola comuna.", "Una comuna no representa a todo el país.", "Reconoce el límite de tu evidencia."),
    ],
    [
        ("Una afirmación, ¿es lo que alguien sostiene o el dato que lo apoya?", "Lo que alguien sostiene", "El dato que apoya es la evidencia."),
        ("«En esa elección votó el 20 % de las personas», ¿puede ser evidencia?", "Sí", "Es un dato que se puede comprobar."),
        ("Organizarse en una junta de vecinos, ¿es una forma de participación?", "Sí", "Los vecinos se organizan para influir en decisiones."),
    ],
    [
        ("¿Por qué un argumento necesita evidencia?", "Para que se pueda comprobar y convencer", "Sin datos queda como una simple opinión."),
        ("¿Por qué es importante decir los límites de la evidencia?", "Para no afirmar más de lo que muestra el dato", "Así se evita generalizar demasiado."),
        ("¿Por qué la participación va más allá de votar?", "Porque se puede influir también informándose y organizándose", "Hay otras formas de involucrarse."),
    ],
    [
        ("Afirmación: «Informarse antes de votar mejora la elección». ¿Qué evidencia sirve: «las personas conocen las propuestas de cada candidato» o «el candidato usa un afiche grande»?", "Las personas conocen las propuestas de cada candidato", "Conocer las propuestas ayuda a elegir con fundamento."),
        arith("En una comuna de ejemplo, de 5.000 personas con derecho a voto, votaron 3.500. ¿Cuántas no votaron?", "5000-3500", "Se resta los votantes al total.", " personas"),
        ("Afirmación: «En la junta de vecinos se resuelven problemas del barrio». ¿Qué evidencia sirve: «los vecinos pidieron un semáforo y la municipalidad lo instaló» o «la junta tiene una sede de color verde»?", "Los vecinos pidieron un semáforo y la municipalidad lo instaló", "Muestra un problema resuelto por organización vecinal."),
    ],
    [
        ("Eva escribe: «Votar no sirve porque no me gusta ninguno». ¿Qué le falta a su argumento?", "Evidencia y razones que sustenten la idea", "Un gusto personal no demuestra que votar no sirva."),
        ("Luis dice: «En mi comuna casi nadie votó, así que en todo Chile pasa igual». ¿Qué límite no respeta?", "Una comuna no representa a todo el país", "Generaliza más allá de la evidencia."),
    ],
    [
        ("Ordena un argumento: A) razón, B) afirmación, C) evidencia.", "B, C, A", "Primero se afirma, luego se da el dato y al final se explica."),
        ("Elecciones de ejemplo en dos cursos: curso A, 28 de 30 estudiantes votaron; curso B, 12 de 30. Afirmación: «En el curso A la directiva representa mejor al grupo». ¿Qué dato apoya más esa afirmación?", "Que votaron 28 de 30 estudiantes", "Participó una proporción mayor del curso."),
    ],
    [("Un niño dice: «Es importante participar porque así las autoridades escuchan a más personas». ¿Cuál es la razón de su argumento?", "Que así las autoridades escuchan a más personas", "Explica por qué participar es importante.")],
    [("¿Qué partes tiene un buen argumento?", "Afirmación, evidencia y razón", "Así se enseñó en la clase."), ("¿Qué es la evidencia?", "Un dato o fuente que apoya una afirmación", "Es la definición del vocabulario."), ("¿Votar es la única forma de participar?", "No", "También se participa informándose y organizándose.")],
    (
        "Elige una de estas afirmaciones y escribe un argumento con evidencia, razón y límite. Afirmación a) «Participar en el centro de estudiantes ayuda a mejorar la escuela». Afirmación b) «Informarse antes de votar es una responsabilidad». Puedes usar estos datos inventados: en la escuela X, el centro de estudiantes organizó una campaña de reciclaje y se recolectaron 300 kilos; en la comuna Y, 8 de cada 10 personas que se informaron antes de votar dijeron conocer las propuestas.",
        "Afirmación a: participar ayuda. Evidencia: 300 kilos recolectados. Razón: los estudiantes organizados lograron resultados. Límite: es una sola escuela.",
        ["incluye afirmación y evidencia", "explica la razón", "reconoce un límite"],
        ["cuatro frases escritas"],
        ["no usar los datos entregados", "no reconocer el límite"],
        "Lee tu argumento a una persona de tu casa y pídele que diga si la evidencia convence.",
    ),
    "Escribe una forma de participar que te gustaría probar y por qué.",
    "Escribe qué dato necesitarías para saber si la participación en tu comuna es alta.",
)

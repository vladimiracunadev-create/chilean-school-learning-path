"""Cuaderno del estudiante de 1.º medio Artes Visuales: AR1M OA 01 (proyectos visuales sobre arquitectura, espacio público y diseño urbano)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR1M OA 01"


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
    "Hojas, lápiz de mina y lápices de colores. La ficha de la Plaza Los Aromos (de ejemplo) está escrita en esta clase; no necesitas buscar ni fotografiar nada.",
    "Aprenderé a leer un espacio público como si fuera una obra: veo su contexto, su lenguaje visual y su propósito. Sirve para proponer cambios en un lugar sin inventar a ciegas.",
    ["Sé que una obra se puede reinterpretar y no solo copiar, y que debo anotar su procedencia.", "Sé separar lo que se ve de lo que opino."],
    [
        "Un espacio público es un lugar de uso abierto a todas las personas, como una plaza, una vereda, un paradero o un parque. Para leerlo miro tres cosas. El contexto es lo que lo rodea y cómo se usa: el barrio, el clima, quiénes pasan por ahí. El lenguaje visual son sus formas, materiales, escala, color y ritmo. El propósito es para qué fue pensado y para quién.",
        "Las tres cosas se conectan. Una banca circular alrededor de un árbol no es solo una forma bonita: hace que las personas se sienten mirándose y se junten, y el árbol les da sombra. La escala es el tamaño de un elemento comparado con el cuerpo humano o con los otros elementos. Una escalera grande impone, una banca baja invita a quedarse. Por eso observo con la pregunta «¿qué efecto produce esta decisión?».",
        "Observar no es opinar. «La plaza es fea» es una opinión; «el piso es de adoquines con juntas abiertas y no hay sombra en la zona de juegos» es un rasgo que cualquiera puede comprobar mirando. Mi registro de observación lleva dos rasgos visuales, una relación con el contexto y una pregunta. También cuido a las personas: si fotografío un lugar, no muestro rostros ni difundo imágenes sin permiso.",
    ],
    [("espacio público", "lugar de uso abierto a todas las personas, como una plaza o un paradero"), ("contexto", "lo que rodea a un lugar y la forma en que se usa"), ("lenguaje visual", "formas, materiales, escala, color y ritmo con que se ve algo"), ("propósito", "para qué y para quién fue pensado un espacio"), ("escala", "tamaño de un elemento comparado con el cuerpo humano o con los otros elementos")],
    [
        w("Leer una ficha", "Ficha de ejemplo, Plaza Los Aromos: banca circular de hormigón alrededor de un árbol; piso de adoquines con juntas abiertas; zona de juegos sin sombra; entrada norte con rampa y entrada sur con escalera; queda junto a una escuela y un consultorio. Separa contexto, lenguaje visual y un propósito probable.", ["Contexto: está junto a una escuela y un consultorio.", "Lenguaje visual: banca circular de hormigón, piso de adoquines, rampa y escalera.", "Propósito probable: un lugar de encuentro y espera para estudiantes y pacientes, con acceso para quien no puede subir peldaños."], "Contexto: escuela y consultorio; lenguaje visual: banca circular, adoquines, rampa; propósito probable: encuentro y espera con acceso para todos"),
        w("Efecto de una decisión", "En la misma plaza, ¿qué efecto produce la banca circular alrededor del árbol?", ["Rasgo: la banca rodea el árbol en círculo.", "Efecto: las personas quedan frente a frente y en la sombra del árbol.", "Relación con el propósito: favorece el encuentro."], "Favorece que las personas se junten y conversen a la sombra"),
    ],
    [
        m("Registrar «la plaza es fea» o «es peligrosa» y creer que eso es observar.", "Una opinión no se puede comprobar mirando el lugar.", "Anota rasgos visibles, por ejemplo «no hay luminarias en el sector sur», y deja la opinión para después."),
        m("Mirar solo las formas y no el contexto.", "La misma forma sirve distinto junto a una escuela que junto a una carretera.", "Pregunta siempre quién usa el lugar y con qué fin antes de decidir qué cambiar."),
    ],
    [
        ex("En Arquitectura y diseño urbano, ¿qué es el lenguaje visual de un espacio? A. Sus formas, materiales, escala y ritmo con que se ve B. El nombre de la calle y el año en que se hizo C. Lo que opinan los vecinos sobre él.", "A", "El lenguaje visual describe cómo se ve el espacio; las otras opciones son datos externos u opiniones."),
        ex("Plaza Los Aromos tiene entrada norte con rampa y entrada sur con escalera. ¿Por cuál entrada puede ingresar una persona en silla de ruedas?", "Por la norte", "La rampa permite avanzar sin peldaños; la escalera lo impide."),
        ex("La ficha dice que la plaza queda junto a una escuela y un consultorio. ¿Ese dato es de contexto o de lenguaje visual?", "De contexto", "Habla de lo que rodea a la plaza, no de sus formas ni materiales."),
    ],
    [
        ex("La banca circular de la plaza rodea un árbol. ¿Qué propósito se relaciona mejor con esa forma? A. Que las personas se sienten mirándose y se junten B. Que las personas pasen rápido sin detenerse.", "A", "El círculo pone a las personas frente a frente; no está pensado para el paso rápido."),
        ex("Rasgos de la ficha: 1) banca de hormigón, 2) piso de adoquines, 3) árbol de copa ancha, 4) rampa. ¿Cuántos nombran un material de construcción?", "2", "Hormigón y adoquines son materiales; el árbol es vegetación y la rampa es una forma."),
        ex("¿Cuál es una relación con el contexto bien escrita? A. La zona de juegos queda junto a una escuela, por eso la usan niños y niñas B. La banca es de hormigón.", "A", "Conecta un rasgo del lugar con su entorno; la otra frase solo describe un material."),
    ],
    [
        ex("Esquina de ejemplo: paradero con techo bajo, sin banca, tres personas esperando de pie al sol, edificio de cuatro pisos al lado. Anotaciones: 1) «El techo es bajo». 2) «Es horrible». 3) «No hay banca». 4) «Hay tres personas de pie al sol». ¿Cuántas son rasgos que se comprueban mirando?", "3", "La 1, la 3 y la 4 se ven; «horrible» es una opinión."),
        ex("Un registro dice: «La plaza es peligrosa». ¿Cuál lo convierte en observación? A. «No hay luminarias en el sector sur» B. «La plaza es muy peligrosa y fea».", "A", "Nombra un rasgo visible que se puede comprobar; la otra frase repite la opinión."),
        arith("Recorrido de ejemplo por el borde de una plaza rectangular: 40 m por un lado largo, 25 m por uno corto, 40 m por el otro lado largo y 25 m por el otro lado corto. ¿Cuántos metros mide el recorrido completo?", "40 + 25 + 40 + 25", "Se suman los cuatro lados del borde.", " m"),
    ],
    [
        ex("Dos plazas de ejemplo. En la primera, todas las bancas miran hacia la calle. En la segunda, cuatro bancas miran hacia un centro común. ¿Cuál favorece mejor que grupos distintos conversen entre sí?", "La segunda", "Las bancas enfrentadas dejan a las personas cara a cara; las que miran a la calle las separan."),
        ex("Una zona de juegos infantiles no tiene sombra y la plaza está junto a una escuela. ¿Qué decisión visual responde al contexto? A. Plantar un árbol de copa ancha junto a los juegos B. Pintar las bancas de rojo.", "A", "La sombra resuelve el problema del sol; el color rojo no cambia la falta de sombra."),
    ],
    [
        ex("Conteo de ejemplo en la plaza durante una hora: pasaron 60 personas; 24 se sentaron, 15 jugaron y el resto solo cruzó. ¿Cuántas solo cruzaron?", "21", "Se restan las que se sentaron y las que jugaron del total: 60 − 24 − 15 = 21.", "60-24-15"),
        ex("Con el mismo conteo (60 personas: 24 sentadas, 15 jugando, 21 cruzando), ¿qué afirmación está respaldada? A. La mayoría se quedó en la plaza porque 39 de 60 se sentaron o jugaron B. Más de la mitad solo cruzó.", "A", "24 + 15 = 39, que supera la mitad de 60; las 21 que cruzaron son menos de la mitad."),
    ],
    ex("El centro de tu liceo quiere mejorar el paradero de la esquina. Tu observación de ejemplo dice: «techo bajo, sin banca, tres personas de pie al sol, edificio de cuatro pisos al lado». ¿Qué relación con el contexto sostiene que hace falta una banca con sombra? A. Hay personas esperando de pie al sol, y esperar de pie cansa a quien tiene mayor edad B. El edificio de cuatro pisos es más alto que el techo.", "A", "Conecta el uso real del paradero con una necesidad; la altura del edificio no justifica una banca."),
    [
        ex("En esta clase, ¿qué tres cosas se miran de un espacio público?", "Contexto, lenguaje visual y propósito", "Juntas explican cómo es el lugar y para qué sirve."),
        ex("Verdadero o falso: «el parque es horrible» es un rasgo visual que se comprueba mirando.", "Falso", "Es una opinión; un rasgo sería «no hay basureros en el parque»."),
        ex("¿Qué cuatro cosas lleva tu registro de observación?", "Dos rasgos visuales, una relación con el contexto y una pregunta", "Así queda una evidencia comprobable y una duda para investigar."),
    ],
    task(
        "Elige UN espacio de ejemplo. A) Paradero: techo bajo, sin banca, tres personas de pie al sol, edificio de cuatro pisos al lado. B) Plaza Los Aromos: banca circular de hormigón alrededor de un árbol, piso de adoquines, zona de juegos sin sombra, rampa al norte y escalera al sur. C) Vereda de un colegio: ancho de 1,5 m, un poste en el centro, cuarenta estudiantes saliendo a la misma hora. Haz un dibujo en planta (vista desde arriba) y anota dos rasgos visuales, una relación con el contexto y una pregunta para investigar.",
        "Elegí la A. Rasgos: el techo es bajo; no hay banca. Relación con el contexto: tres personas esperan de pie al sol, entonces hace falta sombra y asiento. Pregunta: ¿cuánto tiempo espera cada persona? Dibujé el paradero desde arriba con el techo, la calle y las tres personas.",
        ["anota dos rasgos que se comprueban mirando", "relaciona un rasgo con el contexto", "formula una pregunta para investigar", "dibuja el espacio desde arriba sin mostrar rostros"],
        ["dibujo en planta", "registro con dos rasgos, una relación y una pregunta"],
        ["escribir opiniones como si fueran rasgos", "olvidar el contexto"],
        "Pregunta qué rasgo de su registro se puede comprobar mirando y cuál de sus frases es una opinión.",
    ),
    "Mira por un minuto la vereda o el patio más cercano y di en voz alta dos rasgos visibles y una pregunta sobre cómo se usa.",
    "Elige un lugar que conozcas y explica con tres frases cómo cambiaría su propósito si cambiara su escala o su material.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Hojas, lápiz de mina y lápices de colores. Los materiales y referentes están descritos en esta clase; no necesitas buscarlos. Para la prueba práctica sirven cartón y papel limpios.",
    "Aprenderé a explorar materiales y referentes de la arquitectura y el diseño urbano y a elegir un material según lo que quiero que el espacio comunique. Sirve para que mis decisiones tengan una razón.",
    ["Sé leer un espacio con contexto, lenguaje visual y propósito.", "Sé que un referente se reinterpreta y se cita con su procedencia."],
    [
        "La materialidad es el conjunto de materiales con que se construye algo y lo que ellos comunican. El hormigón es resistente y duradero, pero retiene el calor y se ve pesado. La madera es cálida al tacto, pero necesita mantención contra la lluvia. El ladrillo da textura y ritmo con su repetición. Los adoquines con juntas abiertas dejan pasar el agua al suelo, lo que se llama permeabilidad. El vidrio deja ver el interior y da sensación de apertura.",
        "Elegir un material es elegir un efecto y un costo de uso. Una banca de metal al sol quema en verano; una de madera es más amable, pero se desgasta. Por eso comparo materiales con criterios: durabilidad, temperatura, mantención y cómo se ve. Un referente es un espacio u obra que observo para aprender de él. No lo copio: tomo un recurso, como el ritmo de ladrillos, y lo adapto a mi lugar.",
        "Para probar sin gastar uso materiales reutilizables limpios: cartón, tapas, envases y papel. Con ellos hago una muestra pequeña y observo cómo se ve cada textura. Siempre anoto la procedencia de un referente: quién lo hizo, dónde está y qué datos sé con certeza. Si mi referente es una fotografía, solo uso imágenes mías o autorizadas y sin rostros de personas.",
    ],
    [("materialidad", "materiales con que se hace algo y lo que comunican"), ("permeabilidad", "capacidad de un material de dejar pasar el agua"), ("durabilidad", "capacidad de un material de resistir el uso y el tiempo"), ("mantención", "cuidados y reparaciones que necesita un material para seguir en buen estado"), ("referente", "espacio u obra que se observa para aprender de él")],
    [
        w("Elegir un material para una banca", "Una plaza de ejemplo es muy soleada y llueve poco, pero se usa todo el día. Tienes dos bancas: una de metal sin pintura y otra de madera tratada. ¿Cuál conviene y por qué?", ["Criterio de temperatura: el metal sin pintura se calienta mucho al sol.", "Criterio de mantención: la madera tratada necesita cuidado, pero la lluvia es poca.", "Decisión: la madera tratada, porque en el sol es más amable de usar."], "La banca de madera tratada, porque no quema al sol y la poca lluvia reduce su mantención"),
        w("Tomar un recurso de un referente", "Referente de ejemplo: un muro de ladrillos donde algunos ladrillos sobresalen y forman un patrón que da sombra. Tomas el recurso del relieve que da sombra. ¿Cómo lo reinterpretas con cartón?", ["Recurso del referente: relieve que crea sombras.", "Cambio propio: usar tiras de cartón pegadas sobre una base, con otro patrón.", "Procedencia: anoto que el recurso viene del muro de ejemplo."], "Tiras de cartón en relieve con un patrón propio, citando el muro de ejemplo"),
    ],
    [
        m("Elegir el material solo por su color o por cómo se ve en foto.", "Se olvida cuánto se calienta, cuánto dura y qué mantención necesita.", "Compara al menos dos criterios de uso antes de decidir."),
        m("Copiar el referente completo cambiando solo el material.", "La composición y la idea siguen siendo de otra persona.", "Toma un recurso del referente y cambia además la forma, el lugar o el propósito."),
    ],
    [
        ex("En Arquitectura y diseño urbano, ¿qué es la permeabilidad de un piso? A. Que deja pasar el agua hacia el suelo B. Que resiste mucho peso C. Que tiene un color claro.", "A", "Un piso permeable permite que la lluvia se filtre; no se refiere a resistencia ni a color."),
        ex("Un material se calienta mucho al sol y quema al tocarlo en verano. ¿Qué criterio de uso está en riesgo?", "La temperatura", "Un material que quema no es cómodo para sentarse en verano."),
        ex("Un muro de ladrillos repite el mismo ladrillo muchas veces. ¿Qué efecto visual produce la repetición?", "Ritmo", "Repetir un elemento a intervalos regulares crea ritmo visual."),
    ],
    [
        ex("Una calle de ejemplo se inunda cuando llueve porque el piso es continuo y no deja pasar el agua. ¿Qué cambio de materialidad ayudaría? A. Poner adoquines con juntas abiertas que dejen pasar el agua B. Pintar el piso de un color más claro.", "A", "Las juntas abiertas filtran el agua; el color no cambia su permeabilidad."),
        ex("Compara dos bancas para una plaza muy lluviosa: madera sin tratar (se pudre con la humedad) y hormigón (resiste la lluvia). ¿Cuál tiene menos riesgo de deteriorarse por la lluvia?", "La de hormigón", "El hormigón resiste la humedad; la madera sin tratar se pudre."),
        ex("Quieres una fachada con ritmo y sombra usando restos de cartón. ¿Qué haces? A. Pego tiras de cartón en relieve repitiendo un patrón B. Pinto el cartón de un solo color liso.", "A", "El relieve repetido crea ritmo y sombra; el color liso no hace ninguna de las dos cosas."),
    ],
    [
        arith("Para una muestra de ejemplo cortas tiras de cartón de 2 cm de ancho. Si la muestra mide 24 cm de ancho y las tiras van pegadas una junto a otra, ¿cuántas tiras necesitas?", "24 // 2", "Se divide el ancho total entre el ancho de cada tira.", " tiras"),
        ex("Un compañero dice: «Mi referente es esta foto de internet con personas conocidas y la usaré sin pedir permiso». ¿Qué cuidado falta? A. Usar solo imágenes propias o autorizadas y sin rostros B. Cambiarle el nombre al archivo.", "A", "Cambiar el nombre del archivo no resuelve el permiso; hay que usar imágenes propias o autorizadas."),
        arith("Un muro de ejemplo de 3 m de alto se cubre con hileras de ladrillos de 15 cm de alto cada una. ¿Cuántas hileras lleva? (3 m = 300 cm)", "300 // 15", "Se divide la altura total entre la altura de cada hilera.", " hileras"),
    ],
    [
        ex("En un patio con sol directo todo el verano comparas una banca de hormigón oscuro y una de madera clara. Quieres sentarte a las 15:00 sin quemarte. ¿Qué criterio decide la elección: temperatura, ritmo o escala?", "Temperatura", "Lo que importa es cuánto se calienta el asiento al sol; el ritmo y la escala no cambian eso."),
        ex("Un muro de ejemplo combina ladrillo (textura) y vidrio (apertura). ¿Cuál es la sensación que aporta el vidrio?", "Apertura, porque deja ver el interior", "El vidrio es transparente y permite ver a través de él."),
    ],
    [
        ex("Una banca de metal de ejemplo se calienta mucho al sol del patio. ¿Qué cambio mejora su temperatura sin cambiar el material? A. Pintarla de un color claro y ponerle sombra B. Pintarla de negro.", "A", "Un color claro y la sombra absorben y reciben menos calor; el negro absorbe más."),
        arith("Para una muestra tienes 38 tapas limpias y cada patrón de ejemplo usa 6 tapas. ¿Cuántos patrones completos puedes armar?", "38 // 6", "Se divide el total de tapas entre las que usa cada patrón y se cuentan solo los completos.", " patrones"),
    ],
    ex("Tu curso arma una muestra de materiales para un proyecto de paradero. Tienes 3 materiales de ejemplo con sus notas: hormigón (dura mucho y casi no pide mantención; retiene calor, pero a la sombra no quema), madera tratada (cálida, pide mantención) y metal pintado (liviano, se calienta al sol). Necesitas un asiento que no queme y casi no requiera cuidados. ¿Cuál eliges y por qué? A. Hormigón, porque dura mucho aunque retenga calor, y se puede sombrear con un techo B. Metal pintado, porque pesa poco.", "A", "Con un techo que dé sombra, el hormigón cumple en durabilidad y casi no necesita mantención; el peso liviano no responde a ninguna necesidad."),
    [
        ex("¿Qué criterios se comparan al elegir un material para el espacio público?", "Durabilidad, temperatura, mantención y cómo se ve", "Juntos muestran el efecto y el costo de uso del material."),
        ex("Verdadero o falso: al tomar un recurso de un referente puedo copiar todo si anoto el nombre.", "Falso", "Se toma un recurso y se cambia el resto; anotar el nombre no basta."),
        ex("En esta clase, ¿qué datos se anotan de la procedencia de un referente?", "Quién lo hizo, dónde está y qué se sabe con certeza", "Eso permite citarlo y distinguir dato de suposición."),
    ],
    task(
        "Elige UN problema de ejemplo. A) Una banca de plaza que quema al sol en verano. B) Una calle que se inunda con la lluvia porque el piso no deja pasar el agua. C) Un muro liso y gris que nadie mira. Con trozos de cartón, papel y tapas limpias haz dos muestras pequeñas de materialidades distintas para resolverlo, compara ambas con dos criterios (por ejemplo temperatura y mantención) y elige una. Anota un referente de ejemplo del que tomaste un recurso y de dónde viene.",
        "Elegí el problema C. Muestra 1: tiras de cartón en relieve; muestra 2: tapas pegadas formando un patrón. Criterios: textura y sombra. Elegí la 1 porque el relieve proyecta más sombra. Referente: muro de ladrillos de ejemplo de esta clase, de donde tomé el relieve que da sombra.",
        ["hace dos muestras con materialidades distintas", "compara con dos criterios", "elige una y explica por qué", "anota el referente y su procedencia"],
        ["dos muestras", "comparación con dos criterios", "referente citado"],
        ["elegir por color y no por uso", "copiar el referente completo"],
        "Pregunta qué criterio decidió su elección y qué recurso del referente conservó sin copiarlo.",
    ),
    "Toca dos objetos distintos de tu casa y di cuál usarías para una banca de plaza y por qué, según su temperatura y durabilidad.",
    "Investiga con una persona de tu casa qué material de tu barrio se deteriora más con la lluvia o el sol y explica por qué.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hojas cuadriculadas o lisas, regla, lápiz de mina y lápices de colores. Los planos y datos están escritos en esta clase; no necesitas buscarlos.",
    "Aprenderé a probar decisiones visuales con planos, vistas y escalas, y a comparar dos propuestas con un criterio. Sirve para decidir antes de construir una maqueta o proponer un cambio real.",
    ["Sé elegir un material según su uso.", "Sé que un espacio se lee por contexto, lenguaje visual y propósito."],
    [
        "Un arquitecto o diseñador no decide a ojo: prueba. Una planta es el dibujo de un lugar visto desde arriba, como un mapa. Una elevación es el dibujo visto de frente. Con la planta veo cómo se distribuyen y circulan las personas; con la elevación veo alturas y sombras. La escala dice cuánto se reduce el dibujo: en una escala 1:50, 1 cm del dibujo representa 50 cm de la realidad.",
        "Para usar la escala multiplico o divido. Si una banca real mide 200 cm y el plano está a escala 1:50, dibujo 200 ÷ 50 = 4 cm. Si en el plano mido 6 cm, la realidad es 6 × 50 = 300 cm. Así puedo comprobar si una idea cabe: por ejemplo, si un pasillo debe medir al menos 120 cm de ancho para que pasen dos personas lado a lado, calculo cuántos centímetros dibujar.",
        "Probar significa hacer dos versiones y compararlas con un criterio claro, por ejemplo circulación (si se puede avanzar sin chocar), sombra o visibilidad. La versión A y la B se dibujan con la misma escala para que la comparación sea justa. Elijo una según mi propósito, no por gusto, y anoto qué cambiaría en una segunda versión. Una revisión útil dice qué ajusto, no solo «mejorar».",
    ],
    [("planta", "dibujo de un lugar visto desde arriba"), ("elevación", "dibujo de un lugar o un objeto visto de frente"), ("escala", "relación entre el tamaño del dibujo y el tamaño real"), ("circulación", "forma en que las personas se desplazan por un espacio"), ("criterio", "regla que se usa para comparar y decidir")],
    [
        w("Dibujar a escala", "Una banca de ejemplo mide 200 cm de largo y 50 cm de ancho. Dibújala en una planta a escala 1:50. ¿Cuántos centímetros mide el dibujo?", ["Largo: 200 ÷ 50 = 4 cm.", "Ancho: 50 ÷ 50 = 1 cm.", "El dibujo es un rectángulo de 4 cm por 1 cm."], "Rectángulo de 4 cm de largo y 1 cm de ancho"),
        w("Comparar dos pruebas", "Dos plantas de un patio, ambas a escala 1:50. En la A, las bancas están en el centro y el pasillo libre mide 2 cm en el plano. En la B, las bancas van junto al muro y el pasillo libre mide 6 cm. Criterio: circulación. ¿Cuál conviene y cuánto mide el pasillo B en la realidad?", ["Pasillo A: 2 × 50 = 100 cm; pasillo B: 6 × 50 = 300 cm.", "Con el criterio de circulación, un pasillo más ancho permite pasar mejor.", "Elijo la B."], "La B, con un pasillo real de 300 cm"),
    ],
    [
        m("Dibujar las medidas reales en el plano sin aplicar la escala.", "El dibujo no cabe en la hoja y no se parece a la proporción del lugar.", "Divide cada medida real por el número de la escala antes de dibujar."),
        m("Elegir una de las dos pruebas por gusto, sin criterio.", "No se puede explicar ni defender la decisión.", "Compara A y B con un criterio escrito, como circulación o sombra, y decide con eso."),
    ],
    [
        ex("En Arquitectura y diseño urbano, ¿cómo se llama el dibujo de un lugar visto desde arriba? A. Planta B. Elevación C. Escala.", "A", "La planta muestra la distribución vista desde arriba; la elevación es la vista de frente."),
        ex("¿Qué significa que un plano esté a escala 1:100?", "1 cm del plano representa 100 cm de la realidad", "La escala indica cuántas veces se reduce el tamaño real."),
        arith("Un plano está a escala 1:20 y una puerta dibujada mide 10 cm. ¿Cuántos centímetros mide la puerta real?", "10 * 20", "Se multiplica la medida del dibujo por el número de la escala.", " cm"),
    ],
    [
        arith("Un pasillo real mide 240 cm de ancho. En un plano a escala 1:40, ¿cuántos centímetros debes dibujar?", "240 // 40", "Se divide la medida real entre el número de la escala.", " cm"),
        ex("Dos plantas a la misma escala del mismo patio. En la primera hay 2 caminos libres y en la segunda hay 4 caminos libres. Con el criterio de circulación, ¿cuál se recorre mejor?", "La segunda", "Tener más caminos libres permite avanzar con menos choques."),
        ex("Para comparar dos propuestas de plaza con justicia, ¿qué debes mantener igual? A. La escala y el criterio B. El color de los lápices.", "A", "Con distinta escala o criterio las propuestas no se pueden comparar; el color no afecta la comparación."),
    ],
    [
        arith("En el plano de una plaza a escala 1:50, un camino dibujado mide 18 cm de largo. ¿Cuántos metros mide el camino real? (100 cm = 1 m)", "18 * 50 // 100", "Primero se pasa a centímetros reales y luego a metros.", " m"),
        ex("Un pasillo debe medir al menos 120 cm para que pasen dos personas lado a lado. En un plano a escala 1:50, tu pasillo dibujado mide 2 cm. ¿Cumple? A. No, porque 2 × 50 = 100 cm y es menos de 120 B. Sí, porque 2 cm es un número pequeño.", "A", "Se convierte a medida real: 100 cm no alcanza para el mínimo de 120 cm."),
        ex("Para estudiar la sombra de un edificio de ejemplo necesitas ver su altura. ¿Qué dibujo usas? A. Una elevación B. Una planta.", "A", "La elevación muestra alturas porque es una vista de frente; la planta no las muestra."),
    ],
    [
        ex("La versión A de un patio deja un solo acceso a la zona de juegos y la B deja dos. Tu criterio es que no se formen filas largas a la hora del recreo. ¿Cuál eliges y por qué?", "La B, porque dos accesos reparten mejor a las personas", "Con dos entradas, las filas se dividen y se acortan."),
        ex("Un compañero elige la versión A «porque me gusta más». ¿Qué le falta a su decisión?", "Un criterio para compararla con la versión B", "Sin criterio, la decisión no se puede justificar ni revisar."),
    ],
    [
        arith("En una prueba de maqueta a escala 1:50 quieres una rampa de 400 cm de largo real. ¿Cuántos centímetros mide la rampa en la maqueta?", "400 // 50", "Se divide el largo real entre el número de la escala.", " cm"),
        ex("Dos propuestas para una esquina de ejemplo con el criterio «dar sombra durante la espera». A) Un techo de 4 m² sobre la banca. B) Un techo de 1 m² sobre la banca. ¿Cuál cumple mejor el criterio si hay 6 personas esperando?", "A", "Un techo más amplio cubre a más personas; 1 m² no alcanza para 6 personas."),
    ],
    ex("Tu liceo quiere ubicar cuatro bancas en un patio rectangular de 10 m de largo por 6 m de ancho. A escala 1:100, ¿cuántos centímetros de largo debe medir el rectángulo dibujado? A. 10 cm B. 100 cm.", "A", "10 m son 1.000 cm y 1.000 ÷ 100 = 10 cm; 100 cm no cabría en una hoja."),
    [
        ex("Para dibujar a escala 1:50, ¿qué operación haces con la medida real? A. Dividirla entre 50 B. Multiplicarla por 50.", "A", "Se divide entre 50 para reducirla; multiplicar sirve para pasar del dibujo a la realidad."),
        ex("¿Qué debe tener una comparación de dos pruebas para ser justa?", "La misma escala y un criterio claro", "Así se comparan cosas equivalentes."),
        ex("Verdadero o falso: una elevación sirve para ver cómo se distribuyen las personas desde arriba.", "Falso", "Eso lo muestra la planta; la elevación muestra alturas."),
    ],
    task(
        "Elige UN lugar de ejemplo. A) Un paradero: 3 m de largo por 1,5 m de ancho, con una banca de 2 m. B) Un rincón de patio de 4 m por 3 m donde caben tres bancas de 1,5 m. C) Una vereda de 12 m de largo por 2 m de ancho con un árbol a los 6 m. Elige una escala (1:50 o 1:100), dibuja dos plantas distintas del lugar con esa misma escala, compara A y B con UN criterio (circulación, sombra o visibilidad) y decide. Anota qué ajustarías en una segunda versión.",
        "Elegí el lugar A con escala 1:50. Paradero de 6 cm por 3 cm, banca de 4 cm. Planta 1: banca al fondo, pasillo libre de 2 cm. Planta 2: banca al costado, pasillo libre de 3 cm. Criterio: circulación. Elijo la 2. En una segunda versión ensancharía un poco más la entrada.",
        ["usa la misma escala en las dos plantas", "calcula las medidas del dibujo con la escala", "compara con un criterio nombrado", "decide y propone un ajuste"],
        ["dos plantas a escala", "cálculos de medidas", "decisión con criterio y ajuste"],
        ["no aplicar la escala", "elegir por gusto sin criterio"],
        "Pregunta cómo calculó una medida del dibujo y qué criterio decidió entre las dos plantas.",
    ),
    "Mide con pasos o con una regla el ancho de un pasillo de tu casa y di qué medida dibujarías a escala 1:50.",
    "Elige un criterio nuevo (por ejemplo, visibilidad) y explica cómo cambiarías una de tus dos plantas para cumplirlo mejor.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hojas, lápiz de mina, lápices de colores, regla y restos limpios de cartón y papel. Los tres sitios de ejemplo están descritos en esta clase; no necesitas visitarlos.",
    "Aprenderé a desarrollar una propuesta propia para mejorar un espacio: parto de un problema, defino un propósito y tomo decisiones de forma, material y acceso. Sirve para que mi proyecto responda a necesidades reales.",
    ["Sé dibujar una planta a escala y comparar dos pruebas con un criterio.", "Sé elegir un material por durabilidad, temperatura y mantención."],
    [
        "Una propuesta propia comienza con un problema observable, por ejemplo «no hay dónde sentarse a la sombra». De ahí sale un propósito: para qué y para quién será mi intervención. Luego tomo tres tipos de decisiones: de forma (cómo se ve y se distribuye), de materialidad (con qué se hace) y de acceso (quién puede usarlo y cómo). Cada decisión debe poder justificarse con el problema.",
        "El acceso universal significa que el espacio pueda ser usado por la mayor cantidad posible de personas, incluidas quienes usan silla de ruedas, bastón, coche o tienen dificultad para ver. Una rampa suave, un piso sin desniveles y señales con buen contraste ayudan. La pendiente de una rampa se calcula dividiendo la altura que sube entre el largo del recorrido. En un ejemplo, subir 30 cm en 360 cm de largo da una pendiente de 1 en 12.",
        "Mi propuesta se expresa en una maqueta o un plano con una leyenda: qué es cada cosa y a qué escala está. Después reviso con una pauta: ¿resuelve el problema?, ¿se puede construir con los materiales indicados?, ¿pensé en quién la usa? Dejo anotado qué cambiaría en una versión siguiente. La propuesta es mía solo si cada decisión importante tiene una razón mía y no un copiado de un referente.",
    ],
    [("propuesta", "idea de intervención con un problema, un propósito y decisiones justificadas"), ("acceso universal", "diseño que permite usar un espacio a la mayor cantidad posible de personas"), ("pendiente", "cuánto sube una superficie en relación con su largo"), ("leyenda", "lista que explica qué significa cada símbolo o color de un plano"), ("intervención", "acción de cambiar o mejorar un lugar")],
    [
        w("Del problema a la decisión", "Problema de ejemplo: en una vereda estrecha de colegio, cuarenta estudiantes salen al mismo tiempo y el poste del centro bloquea el paso. Propón una decisión de forma, una de materialidad y una de acceso.", ["Forma: ensanchar la vereda en un tramo curvo que rodee el poste.", "Materialidad: piso antideslizante, con textura distinta en el borde para marcar el límite.", "Acceso: tramo sin desniveles para quien usa silla de ruedas o coche."], "Tramo ensanchado alrededor del poste, piso antideslizante con borde texturado y sin desniveles"),
        w("Calcular una pendiente", "Una rampa de ejemplo debe subir 30 cm. Se propone un recorrido de 360 cm de largo. ¿Cuántas veces cabe la altura en el largo?", ["Largo ÷ altura = 360 ÷ 30.", "360 ÷ 30 = 12.", "La pendiente es de 1 en 12: sube 1 por cada 12 de largo."], "Pendiente de 1 en 12"),
    ],
    [
        m("Proponer una forma llamativa sin partir de un problema observable.", "La obra se ve bien pero no resuelve nada ni se justifica.", "Escribe primero el problema y el propósito, y después elige la forma."),
        m("Pensar el acceso solo para personas que pueden subir escalones.", "Deja fuera a quienes usan silla de ruedas, coche o bastón.", "Comprueba si todo el recorrido se puede hacer sin escalones y con piso parejo."),
    ],
    [
        ex("En una propuesta de espacio público, ¿qué es el acceso universal? A. Que la mayor cantidad posible de personas pueda usar el espacio B. Que el espacio sea gratis para todos.", "A", "Se refiere a la posibilidad de uso por distintas personas; el costo es otro asunto."),
        ex("¿Cuál es el primer paso de una propuesta propia: partir del problema observable o elegir la forma que se ve más bonita?", "Partir del problema observable", "Las demás decisiones deben poder justificarse con ese problema."),
        ex("En un plano, ¿para qué sirve la leyenda?", "Para explicar qué significa cada símbolo o color", "Sin leyenda quien lee el plano no sabe qué representa cada cosa."),
    ],
    [
        arith("Una rampa de ejemplo debe subir 20 cm y tiene un largo de 240 cm. ¿Cuántas veces cabe la altura en el largo (1 en cuántos)?", "240 // 20", "Se divide el largo entre la altura que sube.", ""),
        ex("Un sitio de ejemplo tiene un solo acceso con tres escalones. ¿Qué decisión mejora más el acceso universal? A. Agregar una rampa suave junto a los escalones B. Pintar los escalones de un color vivo.", "A", "La rampa elimina el obstáculo para sillas de ruedas y coches; el color solo ayuda a verlos."),
        ex("Un compañero propone una plaza con piso de grava suelta. ¿Qué dificultad de acceso puede causar?", "Dificulta el paso de sillas de ruedas y coches", "La grava suelta es inestable y las ruedas se hunden."),
    ],
    [
        ex("Problema de ejemplo: un sitio vacío entre dos casas se usa como basural y nadie lo cuida. Propuestas: 1) un cerco alto para impedir el paso, 2) una huerta comunitaria con bancas y un letrero con horario. ¿Cuál responde mejor al propósito «volver a usar el sitio entre vecinos»?", "La 2", "La huerta y las bancas invitan a usar y cuidar el sitio; el cerco lo deja cerrado y sin uso."),
        ex("En tu propuesta el problema es «no hay sombra para esperar». ¿Qué decisión se justifica con ese problema? A. Un techo con una banca debajo B. Una pintura de colores en el piso.", "A", "El techo resuelve la sombra; la pintura no cambia nada del problema."),
        ex("Una persona dice: «Mi propuesta es propia porque copié la forma de un referente pero con otro color». ¿Es suficiente?", "No", "Cambiar solo el color deja la idea de otra persona; cada decisión importante debe tener una razón propia."),
    ],
    [
        arith("Un tramo de vereda ensanchada de ejemplo mide 5 m de largo por 3 m de ancho. ¿Cuántos metros cuadrados cubre?", "5 * 3", "El área de un rectángulo es largo por ancho.", " m²"),
        ex("Una propuesta debe hacerse con 6 tiras de madera, 4 tapas y cartón. Tu maqueta lleva 8 tiras. ¿Qué haces? A. Reduzco el diseño a 6 tiras o cambio el material de dos B. Dejo las 8 y compro más sin decir nada.", "A", "La propuesta debe poder construirse con los materiales indicados; hay que ajustarla."),
    ],
    [
        ex("Dos rampas de ejemplo suben lo mismo, 24 cm. La X tiene 288 cm de largo y la Y tiene 192 cm de largo. ¿Cuál es más suave?", "La X", "Su largo es 288 ÷ 24 = 12 veces la altura, y el de Y es 192 ÷ 24 = 8 veces; más largo para la misma altura da menos pendiente."),
        arith("Una rampa de ejemplo con pendiente de 1 en 12 debe subir 18 cm. ¿Cuántos centímetros de largo necesita?", "18 * 12", "El largo es la altura multiplicada por 12.", " cm"),
    ],
    ex("Un liceo de ejemplo quiere una zona de espera para el transporte escolar: 30 estudiantes a la vez, patio sin sombra, un escalón de 15 cm en la entrada. Elige la propuesta que responde mejor. A. Techo para todos, banca larga y una rampa en el escalón B. Una escultura grande en la entrada para decorar.", "A", "Resuelve sombra, asiento y acceso, que son los problemas observados; la escultura no responde a ninguno."),
    [
        ex("¿Qué tres tipos de decisiones se toman en una propuesta propia?", "De forma, de materialidad y de acceso", "Cada una debe justificarse con el problema."),
        ex("Verdadero o falso: la pendiente de una rampa se calcula dividiendo la altura entre el largo del recorrido.", "Verdadero", "Compara cuánto sube con cuánto avanza."),
        ex("¿Qué tres preguntas se hacen al revisar una propuesta?", "Si resuelve el problema, si se puede construir y si pensó en quién la usa", "Esa pauta permite decidir qué cambiar."),
    ],
    task(
        "Elige UN problema de ejemplo. A) Una esquina con paradero sin techo ni banca y un escalón de 15 cm en la vereda. B) Un sitio vacío entre dos casas usado como basural. C) Un patio de liceo donde 30 estudiantes esperan al sol. Escribe el problema, el propósito (para qué y para quién) y tres decisiones: una de forma, una de materialidad y una de acceso. Dibuja una planta con leyenda, indica la escala y escribe qué cambiarías en una segunda versión.",
        "Elegí el problema A. Propósito: que quienes esperan el bus estén protegidos y puedan subir a la vereda sin ayuda. Forma: techo curvo sobre la banca. Materialidad: madera tratada para la banca porque no quema al sol. Acceso: rampa de 15 cm de alto y 180 cm de largo. Dibujé la planta a escala 1:50 con leyenda. En una segunda versión probaría un techo más largo.",
        ["parte de un problema observable", "define propósito, forma, materialidad y acceso", "dibuja planta con leyenda y escala", "propone un ajuste para una segunda versión"],
        ["texto con problema y propósito", "planta con leyenda y escala"],
        ["elegir la forma antes del problema", "olvidar el acceso"],
        "Pregunta qué problema resuelve cada decisión y quién podría quedar fuera de su propuesta.",
    ),
    "Recorre con la vista una vereda o escalera de tu barrio y di en voz alta una decisión que mejoraría su acceso para alguien con coche de bebé.",
    "Calcula la pendiente de una rampa de ejemplo que sube 15 cm en 180 cm y explica si es más suave o más empinada que una de 1 en 10.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hojas y lápiz. Las dos propuestas y la pauta están escritas en esta clase; no necesitas buscar nada. Si fotografías un lugar, hazlo sin rostros y con permiso.",
    "Aprenderé a contrastar propuestas de espacio público con criterios y a cuidar el consentimiento, el crédito y el espacio cuando muestro un trabajo. Sirve para defender mi decisión y para difundirla con respeto.",
    ["Sé desarrollar una propuesta con problema, propósito y decisiones de forma, material y acceso.", "Sé comparar dos pruebas con la misma escala y un criterio."],
    [
        "Contrastar es poner dos propuestas frente a frente y compararlas con los mismos criterios. En diseño urbano uso cuatro: uso (si responde a una necesidad real), acceso (quién puede utilizarlo), memoria (si respeta lo que el lugar significa para quienes lo habitan) e impacto (qué efecto tiene en el ambiente y en el barrio). Puedo darles puntaje de 0 a 3 y sumar, pero lo importante es justificar cada puntaje con algo observable.",
        "Una buena justificación usa el esquema «dato, criterio, conclusión»: la propuesta tiene tal rasgo, ese rasgo cumple tal criterio y por eso la valoro así. Evito frases como «me gusta más». También reviso mi propia propuesta con la misma pauta y acepto lo que falta. Autoría significa que las decisiones son mías; si tomé un recurso de un referente, lo declaro.",
        "Al difundir un trabajo o fotografiar un espacio cuido tres cosas. Consentimiento: pido permiso para mostrar fotos de personas o de obras ajenas y no muestro rostros. Crédito: anoto quién hizo cada obra o referente. Cuidado del espacio: no pinto ni pego nada sobre un lugar sin autorización de quien lo administra. Difundir sin consentimiento, sin crédito o dañando el lugar quita valor al trabajo y puede perjudicar a otras personas.",
    ],
    [("contrastar", "comparar dos o más propuestas con los mismos criterios"), ("memoria", "lo que un lugar significa para las personas que lo habitan y lo recuerdan"), ("impacto", "efecto de una propuesta sobre el ambiente y el barrio"), ("consentimiento", "permiso de una persona o institución para mostrar su imagen, obra o lugar"), ("crédito", "anotar quién es el autor o la autora de una obra o referente")],
    [
        w("Puntuar con criterios", "Propuesta A: techo y banca en un paradero, con rampa, pensada para quienes esperan el bus; no considera nada del uso anterior del lugar. Propuesta B: un mural en la pared del paradero; no cambia el acceso ni la sombra. Puntúa de 0 a 3 uso, acceso, memoria e impacto de la A.", ["Uso: responde a la necesidad de esperar protegido, 3.", "Acceso: tiene rampa, 3.", "Memoria: no considera el uso anterior, 1.", "Impacto: mejora la espera, pero no considera el ambiente, 2."], "A obtiene 3 + 3 + 1 + 2 = 9 puntos"),
        w("Cuidar la difusión", "Quieres publicar una foto de tu maqueta junto al muro de la escuela, donde aparece un compañero de espaldas y un mural de un artista del barrio. ¿Qué haces antes de publicar?", ["Pides permiso al compañero o recortas la imagen para que no aparezca.", "Anotas el nombre de quien pintó el mural, si lo conoces.", "Confirmas que no pintaste ni pegaste nada en el muro sin autorización."], "Pedir consentimiento o recortar al compañero, dar crédito al artista y no intervenir el muro sin permiso"),
    ],
    [
        m("Elegir la propuesta ganadora solo porque «se ve mejor».", "No se puede comprobar ni explicar con evidencia.", "Usa los cuatro criterios y justifica cada puntaje con un rasgo observable."),
        m("Publicar una foto con el mural de otra persona y sin anotar quién lo hizo.", "Se pierde el crédito de su autor o autora y se usa su obra sin permiso.", "Pide consentimiento cuando corresponda y anota el crédito."),
    ],
    [
        ex("Los cuatro criterios para contrastar propuestas en esta clase son uso, acceso, memoria e... ¿cuál falta?", "Impacto", "Impacto es el efecto sobre el ambiente y el barrio."),
        ex("Un criterio pregunta si una propuesta respeta lo que el lugar significa para quienes lo habitan. ¿Cuál es? A. Memoria B. Acceso.", "A", "La memoria se refiere al significado del lugar; el acceso, a quién puede usarlo."),
        ex("En Artes Visuales, ¿qué es el crédito de una obra?", "Anotar quién es su autor o autora", "Reconoce la autoría de quien la hizo."),
    ],
    [
        arith("Una propuesta recibe estos puntajes de 0 a 3: uso 2, acceso 3, memoria 1, impacto 2. ¿Cuál es el total?", "2 + 3 + 1 + 2", "Se suman los cuatro puntajes de los criterios.", " puntos"),
        ex("Una propuesta tiene rampa, piso parejo y señales con buen contraste. ¿Qué criterio sostiene mejor esos rasgos? A. Acceso B. Memoria.", "A", "Los tres rasgos permiten que más personas usen el lugar."),
        ex("Quieres mostrar una fotografía de una obra ajena en tu exposición. ¿Qué haces primero? A. Pedir permiso y anotar el crédito B. Cambiarle el título.", "A", "El permiso y el crédito respetan la autoría; cambiar el título no."),
    ],
    [
        ex("Propuesta A: banca y techo con rampa, puntajes uso 3, acceso 2, memoria 1 e impacto 2. Propuesta B: mural sin cambios de acceso, puntajes uso 1, acceso 0, memoria 3 e impacto 1. ¿Cuál tiene mayor total y cuánto es?", "A, con 8 puntos", "A suma 3 + 2 + 1 + 2 = 8; B suma 1 + 0 + 3 + 1 = 5."),
        ex("En el ejemplo anterior, ¿qué puede hacer la propuesta A para mejorar su criterio más bajo?", "Incluir algo que respete la memoria del lugar, como conservar el árbol antiguo", "Su puntaje más bajo es memoria; conservar un elemento significativo la sube."),
        ex("Una compañera dice: «Mi propuesta es la mejor porque tiene más color». ¿Qué frase la corrige mejor? A. «Tiene más puntaje en uso y acceso, porque incluye banca y rampa» B. «Todas las propuestas son igual de buenas».", "A", "Justifica con criterios y rasgos observables; la otra frase evita comparar."),
    ],
    [
        ex("Para sacar una foto de tu maqueta junto a un muro pintado por un vecino, ¿cuál es la secuencia correcta? A. Pido permiso, tomo la foto sin rostros y anoto el crédito del mural B. Publico la foto y avisaré después si alguien reclama.", "A", "El consentimiento y el crédito se resuelven antes de difundir, no después."),
        ex("Decides pintar el borde del paradero con tu diseño. ¿Qué falta para poder hacerlo? A. La autorización de quien administra el lugar B. Un color que combine.", "A", "No se interviene un espacio sin permiso; el color es un asunto posterior."),
    ],
    [
        ex("Dos propuestas empatan en 10 puntos. La primera tiene acceso 1 y la segunda tiene acceso 3. El paradero lo usa a diario una persona mayor con bastón. ¿Cuál eliges?", "La segunda", "Con el mismo total, pesa más el criterio que afecta a la persona que usa el lugar: su acceso."),
        ex("Una propuesta recibe uso 3, acceso 0, memoria 3 e impacto 3, con total 9. ¿Qué criterio debes revisar primero?", "El acceso", "Un 0 significa que algunas personas no pueden usar el lugar, aunque el total parezca alto."),
    ],
    ex("Tu curso expone dos propuestas para una plaza de ejemplo. Puntajes (de 0 a 3): la propuesta del grupo 1 tiene uso 3, acceso 2, memoria 2 e impacto 3; la del grupo 2 tiene uso 2, acceso 3, memoria 3 e impacto 3. ¿Cuál tiene la mayor suma y por cuántos puntos supera a la otra?", "El grupo 2, por 1 punto", "El grupo 1 suma 3 + 2 + 2 + 3 = 10 y el grupo 2 suma 2 + 3 + 3 + 3 = 11."),
    [
        ex("¿Qué esquema ayuda a justificar un puntaje?", "Dato, criterio y conclusión", "Une un rasgo observable con un criterio y con la decisión."),
        ex("Verdadero o falso: puedo pintar un muro de la escuela si mi diseño es bueno, aunque nadie lo autorice.", "Falso", "Siempre se necesita autorización de quien administra el lugar."),
        ex("¿Qué tres cosas se cuidan al difundir un trabajo?", "Consentimiento, crédito y cuidado del espacio", "Respetan a las personas, a los autores y al lugar."),
    ],
    task(
        "Compara estas dos propuestas de ejemplo para un paradero. Propuesta 1: techo curvo con banca, rampa y piso parejo; usa madera tratada; no considera el árbol antiguo del lugar. Propuesta 2: mural colorido en la pared, sin techo ni banca, que recuerda a los vecinos del barrio. Puntúa de 0 a 3 uso, acceso, memoria e impacto de cada una y justifica cada puntaje con «dato, criterio, conclusión». Elige una, di qué le agregarías de la otra y redacta cómo difundirías el resultado cuidando el consentimiento, el crédito y el espacio.",
        "Propuesta 1: uso 3 (hay techo y banca), acceso 3 (rampa y piso parejo), memoria 1 (no considera el árbol antiguo), impacto 2. Total 9. Propuesta 2: uso 1, acceso 0, memoria 3, impacto 1. Total 5. Elijo la 1 y le agregaría un mural de la 2 en la pared. Para difundirlo pediría permiso para fotos, anotaría el crédito del mural y no pintaría sin autorización del administrador del paradero.",
        ["puntúa los cuatro criterios en ambas propuestas", "justifica cada puntaje con dato, criterio y conclusión", "elige una y propone un elemento de la otra", "describe cómo cuidará consentimiento, crédito y espacio"],
        ["tabla de puntajes", "justificaciones escritas", "plan de difusión cuidadoso"],
        ["decidir por gusto", "difundir sin consentimiento ni crédito"],
        "Pregunta qué dato sostiene su puntaje más alto y qué permiso pediría antes de mostrar el trabajo.",
    ),
    "Cuenta a una persona de tu casa cuáles son los cuatro criterios para comparar propuestas de espacio público.",
    "Redacta tres frases con la estructura «dato, criterio, conclusión» sobre una plaza o paradero que conozcas.",
)

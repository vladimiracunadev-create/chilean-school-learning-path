"""Cuaderno del estudiante de 1.º medio Artes Visuales: AR1M OA 04 (juicio crítico en contexto) y AR1M OA 05 (crítica fundamentada de trabajos propios y de pares)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA4 = "AR1M OA 04"
OA5 = "AR1M OA 05"


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


# ======================================================================= OA 04
# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Hojas, lápiz de mina y lápices de colores. Las dos obras de ejemplo (una pintura de calle y una fotografía de feria) están descritas en esta clase; no necesitas buscar imágenes.",
    "Aprenderé a describir una obra, a distinguir mi gusto de un juicio crítico y a considerar las condiciones en que su creador la hizo. Sirve para opinar sobre arte con argumentos y sin ser injusto.",
    ["Sé separar un dato observable de una opinión.", "Sé que una obra se lee por su contexto, su lenguaje visual y su propósito."],
    [
        "Un juicio crítico es una valoración de una obra que se apoya en razones y no solo en el gusto. «Me encanta» o «no me gusta» son gustos personales: valen como reacción, pero no se pueden comprobar. Un juicio crítico recorre cuatro pasos. Describir: decir qué veo, sin opinar. Analizar: explicar cómo están usados los recursos, como el color o la composición. Interpretar: proponer qué podría significar. Juzgar: decidir qué tan lograda está la obra y por qué.",
        "Para juzgar con justicia considero las condiciones contextuales del creador: la época y el lugar en que trabajó, los recursos que tenía, su formación, su propósito y su público. No es justo criticar una fotografía de rollo en blanco y negro diciendo «es mala porque no tiene color»: la técnica de la cámara y el propósito de documentar explican esa decisión. Conocer las condiciones no obliga a que me guste la obra, pero me da razones más justas.",
        "Una frase de análisis conecta un rasgo con un efecto: «las pinceladas visibles dan sensación de movimiento». Una interpretación usa verbos de posibilidad: «sugiere», «podría significar». Si algo no consta en la ficha, lo marco como inferencia mía. Respeto siempre a la persona que hizo la obra: critico lo que veo en el trabajo, no a quien lo hizo.",
    ],
    [("juicio crítico", "valoración de una obra apoyada en razones y no solo en el gusto"), ("describir", "decir qué se ve sin opinar"), ("analizar", "explicar cómo los recursos de la obra producen un efecto"), ("interpretar", "proponer qué podría significar la obra"), ("condiciones contextuales", "época, lugar, recursos, formación, propósito y público de quien creó la obra"), ("saturado", "color muy intenso y puro, sin mezcla de gris")],
    [
        w("Gusto o juicio", "Dos frases sobre una pintura de ejemplo de una calle al atardecer: F1 «Me encanta, es lo más bonito que vi». F2 «Los colores saturados llevan la mirada hacia la calle, que es lo que la autora quería mostrar». ¿Cuál es un juicio crítico?", ["F1 solo expresa gusto y no da razones.", "F2 conecta un rasgo (colores saturados) con un efecto y con el propósito."], "F2 es el juicio crítico; F1 es un gusto"),
        w("Condiciones del creador", "Ficha de ejemplo: fotografía en blanco y negro de una feria, tomada con una cámara de rollo, sin edición, para documentar. Un compañero dice: «Es mala porque no tiene color». ¿Qué olvida?", ["La cámara de rollo en blanco y negro limita el color.", "El propósito era documentar, no mostrar color."], "Olvida la técnica de la cámara y el propósito de documentar"),
    ],
    [
        m("Decir «es mala porque no me gusta».", "El gusto no es una razón que otra persona pueda comprobar.", "Conecta un rasgo con un efecto y con el propósito de la obra."),
        m("Juzgar una obra de otra época con los recursos de hoy.", "El creador no tenía esos recursos y la comparación es injusta.", "Pregunta qué recursos y condiciones tenía quien la hizo."),
    ],
    [
        ex("¿Cuál de estas frases es de gusto personal? A. «Me encanta este cuadro» B. «El contraste entre figuras oscuras y fondo claro destaca a las personas».", "A", "Expresa una reacción; la otra frase explica un recurso y su efecto."),
        ex("En un juicio crítico, ¿qué significa describir?", "Decir qué se ve sin opinar", "Es el primer paso: se observa antes de valorar."),
        ex("Ficha: «La artista pintó durante un invierno largo con los materiales que tenía en casa». ¿Es una condición contextual del creador o un rasgo de lenguaje visual?", "Una condición contextual", "Habla de cuándo y con qué recursos trabajó."),
    ],
    [
        ex("Los cuatro pasos de un juicio crítico son describir, analizar, interpretar y juzgar. ¿Qué paso viene justo después de analizar?", "Interpretar", "Primero se explica cómo funcionan los recursos y luego se propone qué significan."),
        ex("Frase: «Las pinceladas visibles dan sensación de movimiento». ¿Qué paso del juicio es? A. Analizar B. Describir.", "A", "Conecta un rasgo con un efecto; solo describir sería nombrar las pinceladas."),
        ex("Una persona dice que un grabado impreso con una sola tinta negra «es malo porque no tiene colores». ¿Qué olvida? A. Que una sola tinta se explica por la técnica de la matriz y por el propósito de mostrar contraste B. Que debería tener un marco.", "A", "Las condiciones y la técnica del creador explican la decisión de no usar colores."),
    ],
    [
        arith("La pintura de ejemplo mide 40 cm de largo por 30 cm de alto. ¿Cuántos centímetros cuadrados tiene su superficie?", "40 * 30", "El área de un rectángulo es largo por alto.", " cm²"),
        ex("Anotaciones sobre la pintura: 1) «Muestra una calle al atardecer». 2) «Me gusta mucho». 3) «Las pinceladas se ven». 4) «Las figuras no tienen rostro». ¿Cuántas son descripciones observables?", "3", "La 1, la 3 y la 4 se comprueban mirando; la 2 es gusto."),
        ex("¿Cuál es una interpretación? A. «Las figuras sin rostro sugieren que la calle es de todos» B. «Hay figuras sin rostro».", "A", "Propone un significado con un verbo de posibilidad; la otra frase solo describe."),
    ],
    [
        ex("Dos juicios sobre una pintura de una feria con figuras oscuras sobre un fondo claro. J1: «Es buena porque me gusta». J2: «Es eficaz: el contraste entre figuras oscuras y fondo claro destaca a las personas, que eran el tema que se quería mostrar». ¿Cuál es un juicio crítico?", "J2", "Da una razón, un rasgo y el propósito; J1 solo expresa gusto."),
        ex("¿Por qué importa saber que la artista pintó en casa, en invierno, con materiales que tenía? A. Explica por qué eligió un formato pequeño y pocos materiales B. Demuestra que la obra es mala.", "A", "Las condiciones del creador explican decisiones; no son una prueba de calidad."),
    ],
    [
        arith("En la pintura de 1.200 cm², el cielo ocupa 480 cm². ¿Cuántos centímetros cuadrados ocupa el resto de la pintura?", "1200 - 480", "Se resta la parte del cielo del total.", " cm²"),
        ex("Un compañero dice: «Esta fotografía es mejor que la pintura porque es más real». ¿Qué problema tiene? A. Compara dos obras con propósitos distintos usando un solo criterio, el realismo B. Que no mencionó el marco.", "A", "Cada obra se juzga con criterios pertinentes a su propósito."),
    ],
    ex("Debes escribir un texto para la muestra del liceo sobre la pintura de la calle al atardecer. ¿Con qué empiezas? A. Con describir lo que se ve B. Con «Me gusta mucho».", "A", "Primero se describe lo observable; el gusto no es un paso del juicio."),
    [
        ex("¿Cuáles son los cuatro pasos de un juicio crítico?", "Describir, analizar, interpretar y juzgar", "Van de lo observable a la valoración."),
        ex("Verdadero o falso: conocer las condiciones del creador obliga a que la obra me guste.", "Falso", "Solo da razones más justas para valorarla."),
        ex("¿Qué se critica en una obra: la persona que la hizo o lo que se ve en el trabajo?", "Lo que se ve en el trabajo", "El juicio es sobre la obra, con respeto a quien la creó."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Pintura de 40 por 30 cm de una calle al atardecer: colores muy saturados, figuras sin rostro, pinceladas visibles; la autora pintó en casa durante un invierno largo con los materiales que tenía. B) Fotografía en blanco y negro de una feria, tomada con cámara de rollo y sin edición, para documentar. C) Escultura de ejemplo de 50 cm, hecha con tapas plásticas recolectadas, para hablar de residuos. Escribe una descripción (qué veo), un análisis (un rasgo y su efecto), una interpretación con un verbo de posibilidad y un juicio con una razón. Anota una condición del creador que cambie cómo la juzgas.",
        "Elegí la A. Descripción: calle al atardecer, figuras sin rostro, pinceladas visibles. Análisis: los colores saturados llevan la mirada a la calle. Interpretación: las figuras sin rostro podrían sugerir que la calle es de todos. Juicio: es eficaz porque el color concentra la mirada en lo que quiere mostrar. Condición: pintó en casa con lo que tenía, y eso explica el formato pequeño.",
        ["describe sin opinar", "analiza conectando un rasgo con un efecto", "interpreta con un verbo de posibilidad", "juzga con una razón y nombra una condición del creador"],
        ["texto de cuatro partes", "condición del creador anotada"],
        ["decir solo «me gusta»", "juzgar con criterios impertinentes"],
        "Pregunta cuál de sus frases es descripción y cuál juicio, y qué condición del creador usó.",
    ),
    "Mira una imagen que tengas a mano (un afiche, una caja o un calendario) y di en voz alta una descripción, un análisis y un juicio con razón.",
    "Explica en tres frases por qué dos personas pueden valorar distinto una misma obra y aun así ambas pueden estar bien argumentadas.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Hojas, lápiz de mina y lápices de colores. Las fichas de dos obras de ejemplo (un mural de puerto y un grabado de taller) están escritas en esta clase; no necesitas buscar nada.",
    "Aprenderé a comparar dos obras de contextos distintos usando una ficha de referente y a elegir criterios estéticos pertinentes. Sirve para juzgar cada obra según lo que quiere lograr.",
    ["Sé describir, analizar, interpretar y juzgar una obra.", "Sé que las condiciones del creador explican algunas decisiones."],
    [
        "Un referente es una obra que observo para aprender de ella, y su ficha anota autoría, lugar, medio, recursos, propósito y procedencia. Con dos fichas puedo comparar. Ficha del mural de ejemplo: pintado por una artista y vecinos en el muro de un puerto, con pintura para exteriores, para invitar a cuidar la costa, visto desde lejos y a la intemperie. Ficha del grabado de ejemplo: hecho por un grabador en un taller con prensa, edición de 15 copias, 20 cm de alto, para exponer en una galería, visto de cerca.",
        "Los criterios estéticos son las razones con que valoro el aspecto y el efecto de una obra. Los más usados son la composición (cómo se ordena), el color, la técnica (cómo se hizo), la originalidad, la expresividad (cuánto transmite) y la coherencia entre forma y propósito. Un criterio es pertinente si calza con lo que la obra quiere lograr. Para el mural, la legibilidad a distancia es pertinente; para el grabado, el detalle fino lo es. Pedirle detalle fino a un mural de puerto sería impertinente.",
        "Comparar es mirar ambas obras con los mismos criterios y mostrar diferencias. Por ejemplo: composición, el mural usa planos grandes y el grabado muchas líneas finas; técnica, el mural resiste la intemperie y el grabado se imprime en serie. Las diferencias se explican por el contexto: lugar, recursos y público. Si una ficha no dice algo, no lo supongo. Anoto la procedencia del referente y lo que sé con certeza.",
    ],
    [("ficha de referente", "registro de autoría, lugar, medio, recursos, propósito y procedencia de una obra"), ("criterio estético", "razón con que se valora el aspecto y el efecto de una obra"), ("pertinente", "que calza con lo que la obra quiere lograr"), ("legibilidad", "facilidad con que se entiende una imagen desde donde se mira"), ("intemperie", "exposición a la lluvia, el sol y el viento al aire libre")],
    [
        w("Elegir criterios pertinentes", "Mural de puerto de ejemplo: planos grandes, pintura para exteriores, visto desde lejos, para invitar a cuidar la costa. ¿Cuál criterio es pertinente: la legibilidad a distancia o el detalle fino?", ["El mural se ve desde lejos.", "La legibilidad a distancia importa para que se entienda el mensaje.", "El detalle fino no se vería desde lejos."], "La legibilidad a distancia"),
        w("Comparar con un mismo criterio", "Criterio: técnica. Mural de puerto: pintura para exteriores, resiste lluvia y sol. Grabado de taller: se imprime en serie, 15 copias. ¿Qué diferencia hay?", ["El mural es una pieza única hecha para resistir el clima.", "El grabado es una obra repetible hecha para verse en interior.", "La técnica responde a lo que cada obra necesita."], "El mural resiste la intemperie en una sola pieza y el grabado se repite en serie para interior"),
    ],
    [
        m("Pedir a un mural lo mismo que a un grabado pequeño.", "Cada obra tiene un propósito y una distancia de lectura distintos.", "Elige criterios que calcen con el propósito y con dónde se ve la obra."),
        m("Suponer datos de una obra que su ficha no entrega.", "Se mezcla lo que sé con lo que imagino.", "Marca el dato como pendiente o como inferencia."),
    ],
    [
        ex("¿Qué es un criterio estético pertinente? A. El que calza con lo que la obra quiere lograr B. El que prefiere quien critica.", "A", "La pertinencia depende de la obra, no del gusto de quien critica."),
        ex("El mural de puerto se ve desde lejos. ¿Cuál es la distancia de lectura de esa obra: de cerca o de lejos?", "De lejos", "Está en un muro exterior grande."),
        ex("Ficha del grabado de ejemplo: «edición de 15 copias, 20 cm de alto, en galería». ¿Dónde se ve: en interior o a la intemperie?", "En interior", "Se muestra en una galería."),
    ],
    [
        ex("Para el grabado de taller, ¿qué criterio es pertinente? A. El detalle fino de las líneas B. Que se lea desde 30 metros.", "A", "Se ve de cerca, así que el detalle importa; la lectura a gran distancia no es su caso."),
        ex("Con el criterio de composición, ¿cuál es una diferencia correcta entre las dos obras? A. El mural ordena planos grandes y el grabado, muchas líneas finas B. El grabado ordena planos grandes y el mural, muchas líneas finas.", "A", "Los planos grandes se leen a distancia y calzan con el mural; las líneas finas, con el grabado que se mira de cerca."),
        ex("Ficha del mural: «pintado por una artista y vecinos». ¿Qué dato de contexto aporta? A. Que fue hecho con participación de la comunidad B. Que la pintura es de mala calidad.", "A", "La autoría colectiva es una condición del creador; la ficha no dice nada sobre la calidad de la pintura."),
    ],
    [
        ex("Un compañero dice: «El mural es peor porque no tiene líneas tan finas como el grabado». ¿Qué falla en su juicio?", "Usa un criterio impertinente: el detalle fino no es lo que un mural de lejos busca", "Los criterios deben calzar con el propósito y la distancia de lectura."),
        ex("Criterio: coherencia entre forma y propósito. Mural: invitar a cuidar la costa con planos grandes. ¿Es coherente? A. Sí, porque planos grandes se entienden desde lejos B. No, porque falta un marco.", "A", "La forma sirve al propósito de llegar a quienes pasan lejos."),
        arith("El grabado tiene una edición de 15 copias y 4 se vendieron. ¿Cuántas copias quedan?", "15 - 4", "Se restan las vendidas del total.", " copias"),
    ],
    [
        ex("La ficha del mural no dice cuántas personas participaron. Un compañero escribe «participaron 30 personas». ¿Qué debe hacer? A. Marcarlo como dato pendiente B. Dejarlo escrito porque es posible.", "A", "Un dato que no consta se marca como pendiente."),
        ex("Quieres comparar con un solo criterio. ¿Cuál sirve a ambas obras? A. Coherencia entre forma y propósito B. Cantidad de líneas finas.", "A", "Se puede aplicar a las dos; la cantidad de líneas finas solo calza con el grabado."),
    ],
    [
        arith("El mural mide 6 m de largo por 3 m de alto. ¿Cuántos metros cuadrados cubre?", "6 * 3", "El área es largo por alto.", " m²"),
        ex("Un mural mide 18 m² y un grabado mide 20 cm por 15 cm. ¿Qué comparación es justa? A. Comparar cómo cada uno usa la composición para su propósito B. Decir que el mural es mejor porque es más grande.", "A", "El tamaño no es un criterio de calidad; la composición sí se puede comparar."),
    ],
    ex("Debes escribir para la muestra del liceo un comentario que compare el mural de puerto y el grabado de taller. ¿Qué enfoque es más justo? A. Elegir un criterio pertinente a ambos y explicar las diferencias por su contexto B. Decir cuál me gusta más sin razones.", "A", "El criterio común y el contexto dan razones comprobables."),
    [
        ex("¿Qué datos lleva una ficha de referente?", "Autoría, lugar, medio, recursos, propósito y procedencia", "Permite comparar con datos."),
        ex("Verdadero o falso: un criterio es pertinente si calza con lo que la obra quiere lograr.", "Verdadero", "Esa es la definición de pertinencia."),
        ex("¿Qué haces si una ficha no dice un dato?", "Lo marco como pendiente o como inferencia", "No se inventa lo que no consta."),
    ],
    task(
        "Compara las dos obras de ejemplo. Mural de puerto: pintado por una artista y vecinos en un muro exterior de 6 por 3 m, pintura para exteriores, planos grandes, para invitar a cuidar la costa. Grabado de taller: 20 cm de alto, edición de 15 copias, líneas finas, para exponer en una galería. Completa una ficha de cada una, elige dos criterios pertinentes para ambas, compara con ellos y explica cada diferencia con el contexto. Anota un dato que la ficha no entrega y cómo lo investigarías.",
        "Criterios: composición y coherencia entre forma y propósito. Composición: el mural usa planos grandes; el grabado, líneas finas. Coherencia: los planos grandes sirven para invitar desde lejos; las líneas finas, para mirar de cerca en una galería. Diferencias explicadas por el lugar y la distancia. Dato pendiente: cuántas personas participaron en el mural; lo preguntaría a quien administra el muro.",
        ["completa una ficha para cada obra", "elige criterios pertinentes", "explica diferencias con el contexto", "marca un dato pendiente"],
        ["dos fichas", "comparación con dos criterios", "dato pendiente"],
        ["usar un criterio impertinente", "inventar datos"],
        "Pregunta por qué los criterios que eligió son pertinentes para ambas obras.",
    ),
    "Cuenta a una persona de tu casa por qué no se debe juzgar un mural y un grabado pequeño con el mismo detalle fino.",
    "Elige un tercer criterio estético y explica con dos frases si es pertinente para el mural y para el grabado.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Hojas y lápiz. Los juicios de ejemplo y las obras están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a probar un juicio crítico con la estructura «afirmación, evidencia, criterio» y a descartar razones débiles. Sirve para que mis juicios resistan una objeción.",
    ["Sé elegir criterios estéticos pertinentes.", "Sé describir, analizar, interpretar y juzgar."],
    [
        "Un juicio crítico se puede probar. Su estructura básica tiene tres partes: la afirmación, que es lo que sostengo; la evidencia, que es el rasgo de la obra que lo respalda; y el criterio, que es la razón que une una cosa con la otra. Ejemplo: afirmación «la composición es equilibrada»; evidencia «hay una figura grande a la izquierda y tres pequeñas a la derecha»; criterio «el peso visual de la figura grande se compensa con varias pequeñas».",
        "Para probar mi juicio pregunto: ¿la evidencia está realmente en la obra?, ¿el criterio es pertinente?, ¿qué diría una persona que piensa distinto? Esa objeción posible se llama contraargumento. Un buen juicio lo reconoce y responde: «alguien podría decir que la figura grande domina; sin embargo, su color claro la hace menos pesada». Si no puedo responder, ajusto mi afirmación para que sea más precisa.",
        "Hay razones débiles que debo descartar. «Es famosa» o «la hizo alguien joven» no son razones estéticas. «Es realista» sirve solo si el propósito era parecerse a la realidad. Tampoco debo generalizar: de una obra no puedo concluir cómo es toda una época. Una afirmación fuerte con una sola evidencia se debilita; con dos o tres evidencias se sostiene mejor.",
    ],
    [("afirmación", "lo que se sostiene sobre una obra"), ("evidencia", "rasgo observable de la obra que respalda la afirmación"), ("contraargumento", "objeción que podría plantear alguien que piensa distinto"), ("peso visual", "fuerza con que un elemento atrae la mirada"), ("generalizar", "concluir sobre todo un conjunto a partir de un solo caso")],
    [
        w("Armar un juicio", "Obra de ejemplo: una figura grande clara a la izquierda y tres figuras pequeñas oscuras a la derecha. Arma un juicio sobre el equilibrio con afirmación, evidencia y criterio.", ["Afirmación: la composición está equilibrada.", "Evidencia: una figura grande a la izquierda y tres pequeñas a la derecha.", "Criterio: el peso de la grande se compensa con varias pequeñas."], "Afirmación: equilibrada; evidencia: una grande y tres pequeñas; criterio: se compensa el peso visual"),
        w("Responder una objeción", "Alguien objeta: «La figura grande domina toda la obra». Responde usando un rasgo de la obra.", ["Reconozco que la figura es grande.", "Su color es claro y las tres pequeñas son oscuras, que atraen la mirada.", "Respondo con ese rasgo."], "La figura es grande, pero las tres pequeñas oscuras atraen la mirada y equilibran el peso"),
    ],
    [
        m("Apoyar un juicio en «es famosa» o «la hizo alguien joven».", "Esas razones no hablan del aspecto ni del efecto de la obra.", "Usa evidencia visible y un criterio estético."),
        m("Concluir cómo es toda una época a partir de una sola obra.", "Una obra no representa a todas las demás.", "Limita la afirmación a la obra que observaste."),
    ],
    [
        ex("¿Cuáles son las tres partes de un juicio probado? A. Afirmación, evidencia y criterio B. Título, autor y año.", "A", "Esas tres partes forman la estructura que se puede comprobar."),
        ex("En una fotografía de una calle, «el único farol encendido está en el centro y el resto está oscuro». ¿Es la afirmación o la evidencia de un juicio sobre dónde se fija la mirada?", "La evidencia", "Es un rasgo observable que respalda la afirmación."),
        ex("En Artes: ¿Qué es un contraargumento?", "Una objeción que podría plantear alguien que piensa distinto", "Se anticipa para fortalecer el juicio."),
    ],
    [
        ex("¿Cuál es una razón estética? A. «Los colores fríos del fondo hacen resaltar la figura roja» B. «El artista es muy conocido».", "A", "Habla del aspecto y efecto; la fama no."),
        ex("Una afirmación se apoya en una sola evidencia. ¿Qué haces para sostenerla mejor? A. Buscar dos o tres evidencias más B. Hacerla más enfática.", "A", "Más evidencias hacen más fuerte un juicio; el énfasis no."),
        ex("Un compañero dice: «Esta obra muestra cómo era todo el siglo». ¿Qué error comete?", "Generaliza a todo el siglo a partir de una obra", "Una obra no representa todo un periodo."),
    ],
    [
        ex("Afirmación: «El color guía la mirada». Evidencia: «el único objeto rojo está en el centro». Criterio: ¿cuál une ambos? A. Un color único en un fondo apagado atrae la mirada B. El rojo es un color bonito.", "A", "Relaciona el rasgo con el efecto; el segundo es un gusto."),
        arith("Un juicio tiene 1 evidencia en la primera versión y se refuerza hasta tener 3. ¿Cuántas evidencias se agregaron?", "3 - 1", "Se resta la cantidad inicial de la final.", " evidencias"),
        ex("«Es realista». ¿Cuándo es un criterio pertinente? A. Cuando el propósito de la obra era parecerse a la realidad B. Siempre, en cualquier obra.", "A", "Un criterio solo vale si calza con el propósito."),
    ],
    [
        ex("Alguien objeta: «La obra está desordenada». Tu afirmación era «está equilibrada». ¿Qué respuesta usa evidencia? A. «Hay dos grupos de figuras, uno a cada lado del centro, de pesos parecidos» B. «Para mí está ordenada».", "A", "Responde con un rasgo comprobable; la otra opción repite el gusto."),
        ex("Tu juicio dice que una obra es «la mejor de todas». ¿Qué problema tiene? A. No es comprobable y exagera sin evidencia B. Es muy corto.", "A", "Una afirmación absoluta sin evidencia no se puede sostener."),
    ],
    [
        ex("Tu afirmación es «el rojo guía la mirada». Quieres reforzarla con una segunda evidencia observable. ¿Cuál sirve? A. «El fondo es gris y apagado alrededor del rojo» B. «El rojo es el color favorito de mi familia».", "A", "Es un rasgo visible de la obra; la preferencia de una familia no está en la obra."),
        ex("Dos juicios sobre la misma obra: J1 usa una evidencia y un criterio pertinente; J2 usa tres evidencias, un criterio pertinente y responde un contraargumento. ¿Cuál se sostiene mejor?", "J2", "Tiene más evidencias y anticipa la objeción."),
    ],
    ex("En la muestra del liceo alguien dice de una pintura de ejemplo: «Está mal porque es famosa y yo no la entiendo». Tu respuesta justa es... A. «Dime qué rasgo ves y por qué no logra su propósito» B. «Tienes razón, entonces es mala».", "A", "Pide evidencia y criterio; fama y falta de comprensión no son razones estéticas."),
    [
        ex("¿Qué tres partes tiene un juicio que se puede probar?", "Afirmación, evidencia y criterio", "Juntas permiten comprobarlo."),
        ex("Verdadero o falso: «es famosa» es una razón estética.", "Falso", "No habla del aspecto ni del efecto de la obra."),
        ex("¿Qué se hace con un contraargumento?", "Se reconoce y se responde con un rasgo de la obra", "Fortalece el juicio."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Pintura con una figura grande clara a la izquierda y tres figuras pequeñas oscuras a la derecha. B) Fotografía en blanco y negro de una calle con un solo farol encendido en el centro. C) Afiche con una palabra grande en rojo sobre un fondo gris. Escribe un juicio con afirmación, evidencia y criterio. Escribe un contraargumento posible y respóndelo. Marca una razón débil que NO usarías y por qué.",
        "Elegí la B. Afirmación: el farol guía la mirada. Evidencia: es la única luz y está en el centro. Criterio: una luz única en un fondo oscuro atrae la atención. Contraargumento: la calle vacía podría distraer; respuesta: el farol es la parte más clara y la mirada vuelve a él. Razón débil: «es una foto antigua», porque no habla de cómo se ve.",
        ["escribe afirmación, evidencia y criterio", "plantea un contraargumento y lo responde", "descarta una razón débil con justificación", "usa solo rasgos visibles"],
        ["juicio de tres partes", "contraargumento con respuesta"],
        ["apoyarse en la fama", "generalizar desde una obra"],
        "Pregunta cuál es la evidencia de su juicio y cómo respondió la objeción.",
    ),
    "Cuenta a una persona de tu casa qué diferencia hay entre una razón estética y decir que algo es famoso.",
    "Escribe un juicio de tres partes sobre una imagen de tu casa y un contraargumento posible.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Hojas y lápiz. La ficha de la obra de ejemplo y la pauta de cinco partes están escritas en esta clase; no necesitas buscar nada.",
    "Aprenderé a escribir un juicio crítico completo de una obra en contexto, con cinco partes y una pauta para revisarlo. Sirve para presentar una valoración clara, justa y fundamentada.",
    ["Sé armar un juicio con afirmación, evidencia y criterio.", "Sé considerar las condiciones del creador."],
    [
        "Un juicio crítico completo tiene cinco partes. 1) Ficha: título de ejemplo, autoría, medio y condiciones del creador. 2) Descripción: qué se ve. 3) Análisis: cómo los recursos producen efectos, con criterios pertinentes. 4) Interpretación: qué podría significar, con verbos de posibilidad. 5) Juicio: una afirmación con evidencia, el criterio, una objeción posible y una conclusión sobre qué tan lograda está la obra y qué se podría mejorar.",
        "Escribir con orden ayuda a que sea claro. Uso frases cortas, conectores como «porque», «por ejemplo» y «sin embargo», y un máximo de palabras, por ejemplo 150. Reviso con una pauta de 0 a 2 puntos por parte: 0 si falta, 1 si está incompleta, 2 si está completa y justificada. Con cinco partes, el máximo es 10. Una conclusión justa reconoce lo logrado y lo que podría cambiar, sin burlarse.",
        "Mi texto es una opinión fundamentada, no un hecho absoluto. Por eso uso «a mi juicio» o «según los criterios elegidos». Anoto la fuente de la ficha. Si la obra trata un tema sensible, como el dolor de una comunidad, la trato con respeto y cuido de no ridiculizar a nadie. Si alguien usa el juicio para burlarse de una persona, aviso a un adulto de confianza.",
    ],
    [("ficha", "registro breve de título, autoría, medio y condiciones del creador"), ("conector", "palabra que une ideas, como «porque» o «sin embargo»"), ("pauta de revisión", "lista de partes con puntaje para revisar un texto"), ("conclusión", "cierre que resume el juicio y propone qué se podría mejorar"), ("fundamentar", "apoyar una afirmación con evidencia y criterio")],
    [
        w("Revisar con la pauta", "Un texto sobre una pintura de ejemplo tiene ficha completa, descripción completa, análisis con un rasgo y un efecto, interpretación ausente y juicio con evidencia pero sin criterio. Puntúa de 0 a 2 las cinco partes.", ["Ficha: 2.", "Descripción: 2.", "Análisis: 2.", "Interpretación: ausente, 0.", "Juicio: sin criterio, incompleto, 1."], "2 + 2 + 2 + 0 + 1 = 7 de 10"),
        w("Conclusión justa", "Obra de ejemplo: afiche con una palabra roja sobre fondo gris. Redacta una conclusión que reconozca lo logrado y lo mejorable.", ["Lo logrado: el rojo sobre gris atrae la mirada.", "Lo mejorable: el tamaño de la palabra podría aumentar para leerse a distancia.", "Uso «a mi juicio»."], "A mi juicio, el rojo sobre el gris atrae la mirada; podría mejorar leyéndose desde más lejos si la palabra fuera más grande"),
    ],
    [
        m("Escribir solo una opinión corta («es buena») como si fuera un juicio completo.", "Falta describir, analizar, interpretar y justificar.", "Recorre las cinco partes con la pauta."),
        m("Burlarse de la obra o de quien la hizo.", "Un juicio crítico valora la obra con respeto.", "Critica rasgos de la obra y propone mejoras."),
    ],
    [
        ex("¿Cuántas partes tiene un juicio crítico completo en esta clase?", "5", "Ficha, descripción, análisis, interpretación y juicio."),
        ex("En la pauta de revisión, ¿cuántos puntos recibe una parte que falta? A. 0 B. 1.", "A", "Falta total vale 0; incompleta vale 1."),
        ex("¿Qué palabra es un conector que une una razón con una afirmación? A. «Porque» B. «Hoy».", "A", "«Porque» introduce la razón de una afirmación."),
    ],
    [
        arith("Un texto recibe 2, 2, 1, 1 y 2 puntos en las cinco partes. ¿Cuánto suma de 10?", "2 + 2 + 1 + 1 + 2", "Se suman los cinco puntajes.", " puntos"),
        ex("Un texto dice: «La pintura tiene colores saturados que concentran la mirada en la calle». ¿A qué parte pertenece? A. Análisis B. Ficha.", "A", "Conecta un rasgo con un efecto."),
        ex("Un texto escribe: «Las figuras sin rostro podrían sugerir que la calle es de todos». ¿Qué parte es?", "Interpretación", "Propone un significado con un verbo de posibilidad."),
    ],
    [
        ex("Un texto tiene ficha 2, descripción 1, análisis 2, interpretación 1 y juicio 0. ¿Qué parte debe escribir primero de nuevo para mejorar más?", "El juicio", "Falta por completo y vale 0."),
        arith("Tu texto debe tener un máximo de 150 palabras y llevas 112. ¿Cuántas palabras puedes agregar?", "150 - 112", "Se resta lo escrito del máximo.", " palabras"),
        ex("Quieres cerrar tu texto sobre un afiche con una conclusión justa. ¿Cuál es mejor? A. «A mi juicio, el rojo atrae la mirada; podría mejorar si la palabra fuera más grande» B. «Es un afiche malo y quien lo hizo no sabe».", "A", "Reconoce lo logrado y propone un cambio; la otra frase ataca a la persona."),
    ],
    [
        ex("Un compañero afirma: «Mi juicio es un hecho absoluto». ¿Qué corrección le haces? A. Que es una opinión fundamentada y conviene decir «a mi juicio» B. Que debería escribirlo más grande.", "A", "El juicio depende de los criterios elegidos."),
        ex("Un texto trata una pintura sobre el dolor de una comunidad. ¿Cuál es el enfoque correcto? A. Valorar con respeto sin ridiculizar a nadie B. Hacer chistes para que sea ameno.", "A", "El tema es sensible y se trata con respeto."),
    ],
    [
        ex("Alguien usa tu juicio escrito para burlarse de la persona que hizo la obra. ¿Qué haces? A. Aviso a una persona adulta de confianza B. Lo ignoro y no digo nada.", "A", "Las burlas se informan a un adulto; no se guardan en silencio."),
        arith("En un texto de 150 palabras, la ficha usa 20, la descripción 30, el análisis 40 y la interpretación 25. ¿Cuántas palabras le quedan al juicio?", "150 - 20 - 30 - 40 - 25", "Se restan del máximo las palabras ya usadas.", " palabras"),
    ],
    ex("En la muestra del liceo te piden que escribas un juicio crítico sobre el afiche de la palabra roja sobre fondo gris. Tienes un máximo de 150 palabras. ¿Qué estructura usas? A. Ficha, descripción, análisis, interpretación y juicio B. Solo «Me gusta, es rojo».", "A", "La estructura de cinco partes permite un juicio completo."),
    [
        ex("¿Qué cinco partes tiene un juicio crítico completo?", "Ficha, descripción, análisis, interpretación y juicio", "Cada parte cumple una función distinta."),
        ex("Verdadero o falso: una conclusión justa solo señala lo malo de la obra.", "Falso", "Reconoce lo logrado y propone qué mejorar."),
        ex("¿Qué haces si alguien usa un juicio para burlarse de otra persona?", "Aviso a una persona adulta de confianza", "Las burlas no se guardan en silencio."),
    ],
    task(
        "Escribe un juicio crítico completo de UNA obra de ejemplo con un máximo de 150 palabras. A) Afiche: una palabra grande en rojo sobre fondo gris, hecho por estudiantes con témpera para un pasillo. B) Pintura de 40 por 30 cm de una calle al atardecer, colores saturados, figuras sin rostro; la autora pintó en casa. C) Escultura de 50 cm con tapas plásticas recolectadas, para hablar de residuos. Usa las cinco partes: ficha, descripción, análisis, interpretación y juicio con afirmación, evidencia, criterio y una conclusión justa. Revisa tu texto con la pauta de 0 a 2 por parte y escribe tu puntaje total.",
        "Elegí el afiche. Ficha: afiche de estudiantes, témpera, para un pasillo. Descripción: una palabra grande en rojo sobre fondo gris. Análisis: el rojo contrasta con el gris y atrae la mirada. Interpretación: podría sugerir urgencia. Juicio: a mi juicio, cumple su propósito porque se lee de lejos; podría mejorar si el tamaño aumentara. Puntaje con la pauta: 2 + 2 + 2 + 2 + 2 = 10.",
        ["incluye las cinco partes", "usa afirmación, evidencia y criterio", "cierra con una conclusión justa", "se revisa con la pauta y no supera 150 palabras"],
        ["texto de cinco partes", "puntaje de la pauta"],
        ["escribir solo una opinión", "burlarse de la obra"],
        "Pregunta qué parte fue más difícil de escribir y qué evidencia sostiene su juicio.",
    ),
    "Cuenta a una persona de tu casa las cinco partes de un juicio crítico y cuál te parece más difícil.",
    "Reescribe la conclusión de tu texto con otro conector y compara cuál se entiende mejor.",
)

# ======================================================================= OA 05
# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Hojas, lápiz de mina y lápices de colores. El trabajo de ejemplo de una compañera ficticia está descrito en esta clase; no necesitas mostrar trabajos reales de nadie.",
    "Aprenderé a mirar un trabajo visual, propio o de un par, con cuatro criterios: contexto, materialidad, lenguaje visual y propósito expresivo. Sirve para dar y recibir críticas útiles y respetuosas.",
    ["Sé describir, analizar, interpretar y juzgar una obra.", "Sé que una razón estética se apoya en evidencia."],
    [
        "Para criticar un trabajo visual, propio o de un compañero o compañera, uso cuatro criterios. El contexto es dónde, cuándo y en qué condiciones se hizo. La materialidad son los materiales y cómo se usaron. El lenguaje visual son las formas, el color y la composición. El propósito expresivo es lo que la persona quiso comunicar o provocar. Un buen juicio los relaciona: ¿el material y el lenguaje visual sirven al propósito?",
        "Trabajo de ejemplo de una compañera ficticia, Camila: afiche de 30 por 40 cm, collage de papel de diario y témpera, tema: reciclaje en el barrio, hecho en dos tardes en casa. Con los cuatro criterios puedo decir: contexto, hecho en casa en poco tiempo; materialidad, papel de diario reciclado, coherente con el tema; lenguaje visual, un círculo central rodeado de franjas; propósito, invitar a reciclar. Cada punto se apoya en un dato de la ficha.",
        "La crítica tiene reglas de respeto. Hablo del trabajo, no de la persona: «el texto es pequeño», no «Camila escribe mal». Empiezo con lo que funciona, señalo con evidencia lo que podría cambiar y ofrezco una sugerencia concreta. Si es mi propio trabajo, aplico los mismos criterios con la misma honestidad. Si una crítica se vuelve burla o ataque, aviso a una persona adulta de confianza.",
    ],
    [("contexto", "dónde, cuándo y en qué condiciones se hizo un trabajo"), ("materialidad", "materiales de un trabajo y cómo se usaron"), ("lenguaje visual", "formas, color y composición con que se ve un trabajo"), ("propósito expresivo", "lo que la persona quiso comunicar o provocar"), ("sugerencia concreta", "propuesta específica de cambio que se puede aplicar")],
    [
        w("Aplicar los cuatro criterios", "Afiche de ejemplo de Camila (ficticia): 30 por 40 cm, collage de papel de diario y témpera, tema reciclaje, hecho en dos tardes en casa, un círculo central con franjas alrededor. Asigna cada dato a un criterio.", ["Hecho en dos tardes en casa: contexto.", "Papel de diario y témpera: materialidad.", "Círculo central con franjas: lenguaje visual.", "Tema reciclaje: propósito expresivo."], "Contexto: dos tardes en casa; materialidad: papel de diario y témpera; lenguaje visual: círculo con franjas; propósito: reciclaje"),
        w("Hablar del trabajo", "Quieres decir que el texto del afiche es pequeño. ¿Cuál formulación es respetuosa: «Camila escribe mal» o «el texto es pequeño para leerse desde dos metros»?", ["La primera critica a la persona.", "La segunda describe el trabajo con una condición medible."], "«El texto es pequeño para leerse desde dos metros»"),
    ],
    [
        m("Criticar a la persona («eres mala para esto») en vez del trabajo.", "Ataca a quien lo hizo y no da información útil.", "Habla de un rasgo del trabajo con evidencia."),
        m("Mirar solo el lenguaje visual y olvidar el propósito.", "No se sabe si el trabajo logra lo que quería.", "Relaciona siempre forma y material con el propósito."),
    ],
    [
        ex("¿Cuál criterio describe «hecho en dos tardes en casa»? A. Contexto B. Materialidad.", "A", "Habla de cuándo y dónde se hizo."),
        ex("¿Qué criterio se refiere al papel de diario y la témpera?", "La materialidad", "Nombra los materiales del trabajo."),
        ex("¿Cuál formulación habla del trabajo y no de la persona? A. «El texto es pequeño» B. «Ella escribe mal».", "A", "La primera describe un rasgo; la segunda ataca a la persona."),
    ],
    [
        ex("El afiche usa un círculo central con franjas. ¿Qué criterio es? A. Lenguaje visual B. Propósito expresivo.", "A", "Es un rasgo de forma y composición."),
        ex("El propósito del afiche es invitar a reciclar. ¿Qué criterio mide si el papel de diario ayuda a ese propósito?", "La relación entre materialidad y propósito", "El material reciclado es coherente con un tema de reciclaje."),
        ex("¿Con qué empieza una crítica respetuosa? A. Con lo que funciona B. Con lo que está mal.", "A", "Reconocer lo logrado ayuda a recibir mejor las sugerencias."),
    ],
    [
        arith("El afiche mide 30 cm por 40 cm. ¿Cuántos centímetros cuadrados tiene?", "30 * 40", "El área es largo por alto.", " cm²"),
        arith("Camila hizo el afiche en 2 tardes de 3 horas cada una. ¿Cuántas horas dedicó en total?", "2 * 3", "Se multiplican las tardes por las horas de cada una.", " horas"),
        ex("Una sugerencia concreta para el texto pequeño es... A. «Aumentar las letras a 5 cm de alto» B. «Mejorar el texto».", "A", "Indica qué cambiar y cuánto; «mejorar» no."),
    ],
    [
        ex("Un compañero dice: «Tu afiche es feo porque no me gusta el rojo». ¿Qué le falta a su crítica?", "Un criterio, una evidencia y hablar del trabajo", "El gusto no es un criterio ni una evidencia."),
        ex("En un trabajo propio, ¿puedes aplicar los mismos cuatro criterios? A. Sí, con la misma honestidad B. No, porque nadie critica lo suyo.", "A", "Los criterios sirven para cualquier trabajo, incluido el propio."),
    ],
    [
        ex("Un afiche de reciclaje usa papel nuevo brillante comprado. ¿Qué criterio muestra una posible falta de coherencia con el tema?", "La materialidad", "El material no coincide con el tema de reciclaje."),
        arith("Una pauta tiene 4 criterios y cada uno vale hasta 3 puntos. ¿Cuál es el máximo total?", "4 * 3", "Se multiplica el número de criterios por el puntaje máximo de cada uno.", " puntos"),
    ],
    ex("En el taller del liceo, un compañero te muestra su afiche y te pide una crítica. ¿Con qué frase empiezas? A. «Los colores contrastan y se ve de lejos; el texto podría ser más grande» B. «Está mal hecho».", "A", "Reconoce lo logrado, señala un rasgo con evidencia y sugiere un cambio."),
    [
        ex("¿Cuáles son los cuatro criterios de esta clase?", "Contexto, materialidad, lenguaje visual y propósito expresivo", "Permiten mirar el trabajo completo."),
        ex("Verdadero o falso: una buena crítica habla de la persona que hizo el trabajo.", "Falso", "Habla del trabajo, con respeto."),
        ex("¿Qué haces si una crítica se vuelve una burla?", "Aviso a una persona adulta de confianza", "No se guarda en silencio."),
    ],
    task(
        "Elige UN trabajo de ejemplo. A) Afiche de 30 por 40 cm de Camila (ficticia): collage de papel de diario y témpera, tema reciclaje, hecho en dos tardes en casa, círculo central con franjas. B) Dibujo de 21 por 30 cm de Tomás (ficticio): lápices de colores, tema el cerro de su barrio, hecho en el recreo, cerro al centro y cielo con rayas. C) Tu propio trabajo, con un dibujo breve de ejemplo que hagas hoy. Completa una tabla de los cuatro criterios con un dato en cada uno, escribe una fortaleza con evidencia, una sugerencia concreta y revisa que hables del trabajo y no de la persona.",
        "Elegí el afiche de Camila. Contexto: dos tardes en casa. Materialidad: papel de diario, coherente con reciclaje. Lenguaje visual: círculo central con franjas. Propósito: invitar a reciclar. Fortaleza: el papel de diario refuerza el tema. Sugerencia: aumentar el texto a 5 cm de alto para leerse desde dos metros. Revisé que todas las frases hablen del afiche.",
        ["completa los cuatro criterios con datos", "escribe una fortaleza con evidencia", "propone una sugerencia concreta", "habla del trabajo y no de la persona"],
        ["tabla de cuatro criterios", "fortaleza y sugerencia"],
        ["criticar a la persona", "olvidar el propósito"],
        "Pregunta qué dato sostiene su fortaleza y qué cambio exacto sugiere.",
    ),
    "Cuenta a una persona de tu casa los cuatro criterios para mirar un trabajo visual y cómo empezarías una crítica.",
    "Escribe una crítica de tres frases de un objeto con diseño de tu casa usando dos de los cuatro criterios.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Hojas y lápiz. Los dos trabajos de ejemplo de pares ficticios y la fórmula de retroalimentación están escritos en esta clase; no necesitas mostrar trabajos reales.",
    "Aprenderé a dar retroalimentación con la fórmula «pregunta, fortaleza, sugerencia», a analizar la materialidad de un trabajo y a separar mi preferencia de un criterio. Sirve para ayudar a mejorar sin herir.",
    ["Sé usar los cuatro criterios: contexto, materialidad, lenguaje visual y propósito.", "Sé hablar del trabajo y no de la persona."],
    [
        "La retroalimentación es una respuesta que ayuda a mejorar un trabajo. La fórmula «pregunta, fortaleza, sugerencia» ordena lo que digo. Primero hago una pregunta honesta para entender: «¿qué querías mostrar con el color azul?». Después digo una fortaleza con evidencia: «el azul destaca porque todo lo demás es gris». Finalmente doy una sugerencia concreta: «prueba pegar el título más arriba para que se lea antes». Así la persona sabe qué conservar y qué cambiar.",
        "La materialidad merece atención especial. Me pregunto si el material sirve al propósito, si se ve cuidado y si podría ser más sustentable. Trabajo de ejemplo 1, de Ignacio (ficticio): retrato en lápiz grafito, 21 por 30 cm, en el cuaderno, para mostrar emociones. Trabajo de ejemplo 2, de Valentina (ficticia): maqueta de una plaza en cartón reciclado, pegamento y témpera, 30 por 30 cm, para proponer un espacio de encuentro. El grafito permite matices suaves; el cartón da volumen a la maqueta.",
        "Distingo preferencia de criterio. «No me gustan las maquetas» es una preferencia; «las piezas de la maqueta no están firmes y se mueven» es un criterio de oficio con evidencia. Mi crítica no debe imponer mi estilo: ayudo a que el trabajo se acerque más a lo que su autor o autora quería. Si recibo una crítica dura, no respondo con enojo: pregunto qué dato la respalda y decido qué usar.",
    ],
    [("retroalimentación", "respuesta que ayuda a mejorar un trabajo"), ("fortaleza", "rasgo del trabajo que funciona y se puede apoyar con evidencia"), ("preferencia", "gusto personal que no se puede comprobar en el trabajo"), ("oficio", "cuidado y destreza en el uso de la técnica y los materiales"), ("matiz", "variación suave de un tono o de la intensidad de una línea")],
    [
        w("Dar retroalimentación", "Trabajo de Valentina (ficticia): maqueta de una plaza en cartón reciclado y témpera, 30 por 30 cm, para proponer un espacio de encuentro; las piezas se mueven un poco. Escribe pregunta, fortaleza y sugerencia.", ["Pregunta: ¿qué actividad pensaste para el centro de la plaza?", "Fortaleza: el cartón reciclado es coherente con una propuesta sustentable.", "Sugerencia: pegar las piezas con engrudo sobre una base más firme."], "Pregunta sobre el centro, fortaleza en el material reciclado y sugerencia de reforzar las uniones"),
        w("Preferencia o criterio", "Un compañero dice: «No me gustan las maquetas». ¿Es una preferencia o un criterio?", ["No dice nada que se pueda comprobar en el trabajo.", "Expresa solo un gusto."], "Es una preferencia"),
    ],
    [
        m("Dar solo la sugerencia, sin entender qué quería lograr la persona.", "La crítica puede ir en contra de su propósito.", "Haz primero una pregunta honesta para entender la intención."),
        m("Imponer mi estilo al decir cómo debería hacerse.", "El trabajo es de otra persona y tiene su propio propósito.", "Sugiere cambios que acerquen el trabajo a lo que quería comunicar."),
    ],
    [
        ex("¿Qué tres partes tiene la fórmula de retroalimentación de esta clase?", "Pregunta, fortaleza y sugerencia", "Ordena lo que se dice."),
        ex("«Las piezas de la maqueta se mueven». ¿Es una preferencia o un criterio de oficio?", "Un criterio de oficio", "Describe un rasgo comprobable del cuidado de las uniones."),
        ex("¿Qué tipo de matices permite el lápiz grafito? A. Variaciones suaves de tono B. Colores brillantes.", "A", "El grafito da grises de distinta intensidad."),
    ],
    [
        ex("¿Cuál es una pregunta honesta para entender? A. «¿Qué querías mostrar con el azul?» B. «¿Por qué hiciste eso tan raro?».", "A", "La primera busca entender; la segunda juzga."),
        ex("«El azul destaca porque todo lo demás es gris». ¿Qué parte de la fórmula es?", "Fortaleza", "Dice qué funciona y da evidencia."),
        ex("«Prueba pegar el título más arriba para que se lea antes». ¿Qué parte es? A. Sugerencia B. Pregunta.", "A", "Propone un cambio concreto."),
    ],
    [
        ex("El cartón reciclado de la maqueta, ¿cómo se relaciona con una propuesta de espacio de encuentro sustentable?", "Es coherente porque reutiliza un material", "El material refuerza el propósito."),
        arith("La maqueta de Valentina mide 30 cm por 30 cm. ¿Cuántos centímetros cuadrados ocupa su base?", "30 * 30", "El área de un cuadrado es lado por lado.", " cm²"),
        ex("Un compañero dice: «No me gusta el cartón». ¿Qué le pides? A. Una razón comprobable sobre el trabajo B. Que lo cambie por otro.", "A", "Hay que distinguir preferencia de criterio."),
    ],
    [
        ex("Ignacio recibe esta crítica: «Tu retrato está mal». ¿Qué le falta para ser útil?", "Un rasgo, una evidencia y una sugerencia", "La frase no dice qué cambiar ni por qué."),
        ex("Recibes una crítica dura sobre tu trabajo. ¿Qué haces? A. Pregunto qué dato la respalda y decido qué usar B. Respondo con enojo.", "A", "Preguntar permite aprovechar lo útil."),
        ex("Quieres criticar un retrato en grafito. ¿Cuál es una sugerencia que respeta su propósito de mostrar emociones? A. «Marca más la sombra bajo los ojos para reforzar la tristeza» B. «Haz mejor el retrato».", "A", "Concreta qué cambiar y lo relaciona con el propósito."),
    ],
    [
        ex("Un compañero critica tu maqueta: «No sirve porque no es de madera». ¿Qué problema tiene su crítica? A. Impone su gusto de material sin relación con el propósito B. Falta mencionar el color.", "A", "El propósito era un espacio sustentable y el cartón reciclado lo apoya."),
        ex("Dos críticas a la misma maqueta. C1: «Se nota que no te esforzaste». C2: «Las piezas se mueven; prueba pegarlas con engrudo sobre una base firme». ¿Cuál sigue la fórmula y habla del trabajo? A. C2 B. C1.", "A", "C2 señala un rasgo del trabajo y da una sugerencia concreta; C1 juzga a la persona."),
    ],
    ex("En el taller, un compañero te muestra su maqueta de cartón y no se entiende qué quiere mostrar. ¿Qué haces primero? A. Le pregunto qué quiere mostrar con ella B. Le digo cómo lo haría yo.", "A", "La pregunta permite entender el propósito antes de criticar."),
    [
        ex("¿Qué se hace primero en la fórmula de retroalimentación?", "Una pregunta honesta", "Sirve para entender la intención."),
        ex("Verdadero o falso: «no me gustan las maquetas» es un criterio comprobable.", "Falso", "Es una preferencia."),
        ex("Si una crítica se vuelve ataque a la persona, ¿qué haces?", "Aviso a una persona adulta de confianza", "No se guarda en silencio."),
    ],
    task(
        "Elige UN trabajo de ejemplo. A) Retrato en grafito de Ignacio (ficticio), 21 por 30 cm, para mostrar emociones. B) Maqueta de plaza de Valentina (ficticia), cartón reciclado y témpera, 30 por 30 cm, con piezas que se mueven. C) Tu propio trabajo: haz ahora un boceto breve de un objeto de tu casa. Escribe una retroalimentación con pregunta, fortaleza (con evidencia) y sugerencia concreta, y marca una preferencia tuya que NO usarías en la crítica. Revisa que no hables de la persona.",
        "Elegí la maqueta de Valentina. Pregunta: ¿qué actividad pensaste para el centro de la plaza? Fortaleza: el cartón reciclado es coherente con una propuesta sustentable. Sugerencia: pegar las piezas con engrudo sobre una base más firme. Preferencia que no usaría: «me gustan más las plazas con árboles». Todas las frases hablan de la maqueta.",
        ["incluye pregunta, fortaleza y sugerencia", "apoya la fortaleza con evidencia", "separa preferencia de criterio", "habla del trabajo y no de la persona"],
        ["retroalimentación escrita", "preferencia marcada"],
        ["imponer el propio estilo", "criticar a la persona"],
        "Pregunta cuál es su preferencia y cuál su criterio, y cómo los distinguió.",
    ),
    "Cuenta a una persona de tu casa la fórmula «pregunta, fortaleza, sugerencia» con un ejemplo de un objeto cercano.",
    "Escribe una retroalimentación a un trabajo tuyo antiguo con la fórmula completa.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Hojas, lápiz de mina, lápices de colores y regla. Los datos de las críticas y los trabajos de ejemplo están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a probar un cambio en mi trabajo a partir de una crítica, a priorizar sugerencias y a comparar antes y después. Sirve para mejorar sin rehacer todo.",
    ["Sé dar retroalimentación con pregunta, fortaleza y sugerencia.", "Sé separar preferencia de criterio."],
    [
        "Una crítica sirve cuando cambio algo y compruebo qué pasó. Primero ordeno las sugerencias que recibí. Elijo una que sea concreta, que acerque el trabajo a mi propósito y que pueda hacer con el tiempo y los materiales que tengo. Después hago una versión corta, a veces en un boceto pequeño, cambiando solo esa cosa. Comparar antes y después con los mismos criterios me muestra si el cambio funcionó.",
        "Para priorizar uso dos preguntas: ¿cuánto mejora el propósito? y ¿cuánto esfuerzo requiere? Si le doy puntos de 1 a 3 a cada una, una sugerencia con impacto 3 y esfuerzo 1 conviene mucho. Ejemplo con datos de ejemplo: S1, aumentar el texto del afiche (impacto 3, esfuerzo 1); S2, rehacer todo el fondo (impacto 2, esfuerzo 3); S3, cambiar el marco (impacto 1, esfuerzo 1). El orden sensato es S1, luego S3 y S2 si sobra tiempo.",
        "No toda crítica debo seguirla. Si una sugerencia va contra mi propósito, la agradezco y explico por qué no la uso. Conservo la versión anterior para poder volver. Cuando comparo, escribo el cambio, el criterio usado y el resultado: «cambié el tamaño del texto de 2 cm a 5 cm; criterio: legibilidad a dos metros; resultado: se lee mejor». Así mi proceso queda documentado y mi autoría clara.",
    ],
    [("priorizar", "ordenar lo que se va a hacer según su importancia"), ("impacto", "cuánto mejora una sugerencia el propósito del trabajo"), ("esfuerzo", "tiempo y materiales que requiere hacer un cambio"), ("versión anterior", "copia del trabajo antes del cambio"), ("documentar el proceso", "anotar qué se cambió, con qué criterio y qué resultó")],
    [
        w("Priorizar sugerencias", "Datos de ejemplo del afiche: S1 aumentar el texto (impacto 3, esfuerzo 1); S2 rehacer el fondo (impacto 2, esfuerzo 3); S3 cambiar el marco (impacto 1, esfuerzo 1). Ordena de más a menos conveniente.", ["S1 tiene el mayor impacto y el menor esfuerzo.", "S3 cuesta poco, pero aporta poco.", "S2 aporta algo y cuesta mucho."], "S1, luego S3 y por último S2"),
        w("Documentar un cambio", "Cambiaste el texto de 2 cm a 5 cm de alto para leerse desde dos metros, y ahora se lee bien. Escribe el registro.", ["Cambio: texto de 2 cm a 5 cm.", "Criterio: legibilidad a dos metros.", "Resultado: se lee mejor."], "Cambié el texto de 2 cm a 5 cm; criterio: legibilidad a dos metros; resultado: se lee mejor"),
    ],
    [
        m("Cambiar todo el trabajo después de una sola crítica.", "Se pierde lo que funcionaba y no se sabe qué ayudó.", "Elige una sugerencia concreta, cambia solo eso y compara."),
        m("Seguir una crítica que contradice mi propósito para no discutir.", "El trabajo deja de comunicar lo que quería.", "Agradece, explica por qué no la usas y conserva tu propósito."),
    ],
    [
        ex("Antes de cambiar mi trabajo, ¿qué debo guardar? A. La versión anterior B. Solo la nueva.", "A", "Con la versión anterior puedo volver y comparar."),
        ex("Una sugerencia tiene impacto 3 y esfuerzo 1. ¿Conviene hacerla?", "Sí", "Mejora mucho el propósito con poco esfuerzo."),
        ex("Al probar un cambio, ¿cuántas cosas conviene cambiar a la vez? A. Una B. Todas.", "A", "Con una sola cosa sabes qué produjo el efecto."),
    ],
    [
        ex("Sugerencias de ejemplo para un dibujo: S1 impacto 3 y esfuerzo 2; S2 impacto 1 y esfuerzo 3. ¿Cuál haces primero?", "S1", "Tiene el mayor impacto y el menor esfuerzo."),
        arith("Tienes 3 sugerencias y pruebas 1 por vez, cada prueba toma 20 minutos. ¿Cuántos minutos necesitas para probarlas todas?", "3 * 20", "Se multiplica la cantidad de pruebas por la duración de cada una.", " minutos"),
        ex("Una sugerencia pide cambiar el tema de tu trabajo, que es un propósito tuyo. ¿Qué haces? A. Agradezco y explico por qué no la uso B. La aplico para evitar discusiones.", "A", "Cambiar el tema va contra tu propósito."),
    ],
    [
        ex("En el registro «cambié el fondo gris por uno amarillo; criterio: contraste con el texto; resultado: se lee mejor desde el pasillo», ¿cuál es el criterio?", "El contraste con el texto", "Es la razón con que se evaluó el cambio."),
        arith("El título de un afiche pasó de 3 cm a 7 cm de alto. ¿Cuántos centímetros aumentó?", "7 - 3", "Se resta la altura inicial de la final.", " cm"),
        ex("Comparas antes y después con un criterio. El después se lee a 3 metros y el antes a 1 metro. Tu criterio es legibilidad. ¿Qué concluyes? A. El cambio funcionó B. No se puede saber.", "A", "Con el mismo criterio, el después es mejor."),
    ],
    [
        ex("Un compañero cambió el fondo, el texto y el marco a la vez y dice que ahora «se ve mejor». ¿Qué problema hay en su prueba?", "No sabe qué cambio produjo la mejora", "Cambió tres cosas a la vez."),
        ex("Datos de ejemplo: S4 impacto 3 esfuerzo 2; S5 impacto 1 esfuerzo 3; S6 impacto 2 esfuerzo 1. ¿Cuál es la peor inversión de tiempo si solo tienes una tarde? A. S5 B. S4.", "A", "S5 cuesta mucho y aporta poco; S4 y S6 aportan más con menos esfuerzo."),
    ],
    [
        arith("Una sugerencia tiene impacto 3 y esfuerzo 2; otra, impacto 1 y esfuerzo 3. Si restas el esfuerzo del impacto, ¿cuál es el resultado de la primera?", "3 - 2", "Impacto menos esfuerzo da una medida simple de conveniencia.", ""),
        ex("Con esa resta, la primera sugerencia (impacto 3, esfuerzo 2) da 1 y la segunda (impacto 1, esfuerzo 3) da −2. ¿Cuál es más conveniente?", "La primera", "Su resultado es 1 y el de la segunda es −2."),
    ],
    ex("Tu compañera te sugiere dos cambios para tu afiche: aumentar el texto (impacto 3, esfuerzo 1) y cambiar el tema por uno que a ella le gusta más (impacto 0 en tu propósito, esfuerzo 3). ¿Qué haces? A. Aplico el primero y agradezco el segundo explicando mi propósito B. Aplico los dos.", "A", "El segundo no mejora tu propósito y cuesta mucho."),
    [
        ex("¿Qué dos preguntas se usan para priorizar sugerencias?", "Cuánto mejora el propósito y cuánto esfuerzo requiere", "Ayudan a ordenar los cambios."),
        ex("Verdadero o falso: debo seguir todas las críticas que recibo.", "Falso", "Solo las que ayudan a mi propósito."),
        ex("¿Qué tres datos se anotan al documentar un cambio?", "El cambio, el criterio y el resultado", "Así el proceso queda claro."),
    ],
    task(
        "Elige UNA situación de ejemplo. A) Un afiche con texto de 2 cm de alto y tres sugerencias: S1 aumentar el texto (impacto 3, esfuerzo 1), S2 rehacer el fondo (impacto 2, esfuerzo 3), S3 cambiar el marco (impacto 1, esfuerzo 1). B) Un retrato en grafito con dos sugerencias: S1 marcar más la sombra de los ojos (impacto 3, esfuerzo 1), S2 cambiar de papel (impacto 1, esfuerzo 3). C) Un trabajo tuyo con una sugerencia que tú elijas. Prioriza, elige una sugerencia, haz un boceto con ese único cambio y escribe el registro «cambio, criterio y resultado». Anota una sugerencia que no seguirías y por qué.",
        "Elegí la situación A. Prioricé S1, S3 y S2. Elegí S1 y dibujé el afiche con el texto de 5 cm. Registro: cambié el texto de 2 cm a 5 cm; criterio: legibilidad a dos metros; resultado: se lee mejor. No seguiría cambiar el tema, porque va contra mi propósito de invitar a reciclar.",
        ["prioriza con impacto y esfuerzo", "cambia una sola cosa", "documenta cambio, criterio y resultado", "explica una sugerencia que no seguiría"],
        ["orden de sugerencias", "boceto con el cambio", "registro del cambio"],
        ["cambiar todo a la vez", "seguir una crítica contraria al propósito"],
        "Pregunta por qué eligió esa sugerencia y cómo comprobó el resultado.",
    ),
    "Cuenta a una persona de tu casa por qué conviene cambiar una sola cosa por vez al probar una crítica.",
    "Elige una sugerencia que hayas recibido alguna vez y evalúala con impacto y esfuerzo del 1 al 3.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Hojas y lápiz. Los dos trabajos de ejemplo y la pauta de puntaje están escritos en esta clase; no necesitas mostrar trabajos reales ni nombres de personas.",
    "Aprenderé a escribir un informe crítico de un trabajo propio y de un trabajo de un par, con los cuatro criterios, evidencia y un plan de mejora. Sirve para cerrar un proyecto con una mirada honesta y respetuosa.",
    ["Sé dar retroalimentación con la fórmula y priorizar sugerencias.", "Sé documentar un cambio con criterio y resultado."],
    [
        "Un informe crítico reúne en un solo texto la mirada sobre un trabajo propio y sobre el de un par. Tiene seis partes: 1) ficha del trabajo; 2) contexto; 3) materialidad; 4) lenguaje visual; 5) propósito expresivo y qué tan logrado está; 6) plan de mejora con una o dos acciones. Cada parte lleva un dato observable y una razón. Uso la misma pauta para ambos trabajos para que la mirada sea justa.",
        "Puntúo cada criterio de 0 a 3: 0 no se observa; 1 se observa poco; 2 se observa bien; 3 se observa muy bien y está justificado. Con cuatro criterios el máximo es 12. El puntaje es una ayuda, no el juicio completo: lo importante es la razón que lo sostiene. Si mi propio trabajo recibe un puntaje menor que el del par, lo reconozco sin enojo. Si el par recibe menos, lo digo con respeto y propongo una mejora concreta.",
        "En un informe cuido la privacidad: uso nombres ficticios o iniciales si el par no autoriza su nombre, no incluyo rostros ni datos personales y pido permiso para mostrar su trabajo. Doy crédito a referentes y materiales. Al final escribo qué aprendí y qué haré distinto en el próximo trabajo. Si la crítica se vuelve ataque, aviso a una persona adulta de confianza y guardo evidencia.",
    ],
    [("informe crítico", "texto que reúne la mirada crítica sobre uno o más trabajos"), ("pauta de puntaje", "lista de criterios con puntaje de 0 a 3"), ("plan de mejora", "una o dos acciones concretas para mejorar un trabajo"), ("privacidad", "derecho a que los datos personales no se muestren sin permiso"), ("crédito", "anotar quién hizo cada obra o aportó un material o referente")],
    [
        w("Puntuar con la pauta", "Trabajo de un par (ficticio): maqueta de plaza en cartón reciclado y témpera. Contexto: hecha en casa en tres tardes, 2. Materialidad: cartón reciclado coherente con el tema, pero piezas flojas, 2. Lenguaje visual: formas claras y colores contrastados, 3. Propósito: se entiende que es una plaza de encuentro, 3. ¿Cuál es el total?", ["Se suman los cuatro puntajes.", "2 + 2 + 3 + 3 = 10 de 12."], "10 de 12"),
        w("Plan de mejora", "En la maqueta las piezas se mueven. Escribe un plan de mejora con una acción concreta.", ["Problema: piezas flojas.", "Acción: pegar las piezas con engrudo sobre una base de cartón doble.", "Resultado esperado: la maqueta se mantiene firme."], "Pegar las piezas con engrudo sobre una base de cartón doble"),
    ],
    [
        m("Usar pautas distintas para el trabajo propio y para el del par.", "La comparación deja de ser justa.", "Aplica los mismos cuatro criterios y la misma escala."),
        m("Incluir el nombre completo o una foto del par sin permiso.", "Se vulnera su privacidad.", "Usa un nombre ficticio o iniciales y pide autorización."),
    ],
    [
        ex("¿Cuántos criterios se puntúan en el informe crítico de esta clase?", "4", "Contexto, materialidad, lenguaje visual y propósito."),
        ex("En la pauta, ¿qué significa un 0? A. No se observa el criterio B. Se observa muy bien.", "A", "0 es la ausencia; 3 es lo máximo."),
        ex("¿Qué incluye el plan de mejora? A. Una o dos acciones concretas B. Una lista de todo lo que está mal.", "A", "El plan propone cambios posibles."),
    ],
    [
        arith("Un trabajo recibe 3, 2, 1 y 2 en los cuatro criterios. ¿Cuánto suma?", "3 + 2 + 1 + 2", "Se suman los cuatro puntajes.", " puntos"),
        ex("«Hecha en casa en tres tardes con cartón reciclado». ¿Qué criterio apoya mejor este dato? A. Contexto B. Lenguaje visual.", "A", "Dice dónde y cuánto tiempo se trabajó."),
        ex("Quieres mostrar el trabajo de un compañero en tu informe. ¿Qué haces primero? A. Pedirle permiso B. Usar su nombre completo.", "A", "El permiso se pide antes."),
    ],
    [
        arith("Tu trabajo suma 9 y el de tu par suma 11, ambos de 12. ¿Cuántos puntos de diferencia hay?", "11 - 9", "Se resta el menor del mayor.", " puntos"),
        ex("El puntaje de tu propio trabajo es menor que el de tu par. ¿Cuál es una respuesta honesta? A. Reconozco lo que falta y planeo una mejora B. Cambio los puntajes para no quedar atrás.", "A", "La honestidad es parte del criterio."),
        ex("Tu par recibe 1 en materialidad porque las piezas están sueltas. ¿Qué sugerencia concreta le das? A. «Pega las piezas con engrudo sobre una base firme» B. «Hazlo mejor».", "A", "Indica qué hacer."),
    ],
    [
        ex("Un informe da a un trabajo 3 en lenguaje visual sin ninguna razón. ¿Qué le falta? A. Un dato observable que lo justifique B. Un número más alto.", "A", "El puntaje se sostiene con evidencia."),
        ex("Un par se burla del trabajo de otra persona en el informe. ¿Qué debes hacer? A. Avisar a una persona adulta de confianza y guardar evidencia B. Reírme y no decir nada.", "A", "Las burlas se informan a un adulto."),
    ],
    [
        arith("Dos trabajos, cada uno con 4 criterios de 0 a 3. ¿Cuál es el máximo total entre ambos?", "2 * 4 * 3", "Son dos trabajos, cuatro criterios y 3 puntos como máximo.", " puntos"),
        ex("En tu informe pones solo iniciales para tu par porque no autorizó su nombre. ¿Qué principio respetas?", "La privacidad", "Se evita mostrar datos personales sin permiso."),
    ],
    ex("Debes entregar un informe crítico de tu maqueta y la de un compañero. Tu maqueta suma contexto 2, materialidad 3, lenguaje visual 2 y propósito 3; la del compañero suma 3, 2, 3 y 2. ¿Cuántos puntos tiene cada una?", "10 cada una", "La tuya suma 2 + 3 + 2 + 3 = 10 y la de tu compañero 3 + 2 + 3 + 2 = 10."),
    [
        ex("¿Qué seis partes tiene el informe crítico?", "Ficha, contexto, materialidad, lenguaje visual, propósito y plan de mejora", "Cada parte lleva dato y razón."),
        ex("Verdadero o falso: el puntaje reemplaza la razón que lo sostiene.", "Falso", "La razón es lo más importante."),
        ex("¿Qué se debe pedir antes de mostrar el trabajo de un par?", "Su permiso", "Respeta su privacidad y autoría."),
    ],
    task(
        "Escribe un informe crítico de DOS trabajos de ejemplo. Trabajo propio (ejemplo): afiche de 30 por 40 cm, papel de diario y témpera, tema reciclaje, hecho en dos tardes en casa, con texto de 2 cm de alto. Trabajo de un par (ejemplo): maqueta de plaza de 30 por 30 cm, cartón reciclado y témpera, hecha en tres tardes, con piezas que se mueven. Para cada uno completa los cuatro criterios con un dato y un puntaje de 0 a 3, suma el total y escribe un plan de mejora de una o dos acciones. Usa nombres ficticios o iniciales y cierra con lo que harías distinto en el próximo trabajo.",
        "Afiche: contexto 2, materialidad 3 (papel de diario coherente con reciclaje), lenguaje visual 2, propósito 2: total 9. Plan: aumentar el texto a 5 cm. Maqueta del compañero J.: contexto 3, materialidad 2 (piezas flojas), lenguaje visual 3, propósito 3: total 11. Plan: pegar con engrudo. Lo que haré distinto: hacer una prueba de legibilidad antes de terminar.",
        ["usa los cuatro criterios en ambos trabajos", "puntúa y justifica con un dato", "escribe un plan de mejora concreto", "protege la privacidad del par"],
        ["informe de dos trabajos", "tabla de puntajes", "plan de mejora"],
        ["usar pautas distintas", "mostrar datos personales"],
        "Pregunta qué dato sostiene su puntaje más alto y qué acción de mejora es la más urgente.",
    ),
    "Cuenta a una persona de tu casa las seis partes de un informe crítico y cuál te parece más importante.",
    "Reescribe el plan de mejora de tu informe con otra acción y compara cuál es más fácil de hacer.",
)

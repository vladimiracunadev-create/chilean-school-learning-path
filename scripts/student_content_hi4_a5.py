"""Material del estudiante de 4.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (recursos renovables y no renovables), OA 08 (paisajes de América) y OA 09 (recursos de América y desarrollo sostenible)."""
from __future__ import annotations

from student_lessons import arith, ex, register
from student_content_hi4_a import task

OA7 = "HI04 OA 07"
OA8 = "HI04 OA 08"
OA9 = "HI04 OA 09"

# ================================================================ OA 07 · RECURSOS
# ---------------------------------------------------------------- clase 1
R1 = ("Ficha 1: Un recurso natural es algo que la naturaleza ofrece y las personas usan. Hay recursos renovables, que se renuevan con el tiempo si se usan con cuidado, como el agua, el viento, el sol, los bosques y los peces. "
      "Hay recursos no renovables, que no se renuevan en el tiempo humano porque se formaron en millones de años, como el petróleo, el carbón y los minerales. "
      "En Chile, el cobre, un mineral, se extrae sobre todo en el norte, por ejemplo en la región de Antofagasta. Los bosques se encuentran sobre todo en el centro y el sur. "
      "El sol es muy intenso en el desierto del norte. El mar de la costa entrega peces.")
register(
    OA7, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de Chile ayuda, pero no es necesario.",
    use="Aprenderé qué es un recurso natural, dónde hay algunos recursos en Chile y cómo se dividen en renovables y no renovables. Sirve para entender por qué hay que cuidarlos.",
    prior=["Sé ubicar el norte, centro y sur de Chile.", "Sé que la naturaleza nos da agua, aire y alimentos."],
    explain=[
        "Un recurso natural es algo que la naturaleza ofrece y que las personas usan: el agua, el aire, los bosques, los minerales o el sol. Todo lo que usamos viene, de una u otra forma, de un recurso natural. Los recursos naturales no están repartidos por igual: cada lugar tiene algunos y le faltan otros.",
        "Los recursos renovables se renuevan con el tiempo si los usamos con cuidado. Son el agua, el viento, el sol, los bosques y los peces. Los recursos no renovables no se renuevan en el tiempo humano, porque se formaron durante millones de años. Son el petróleo, el carbón y los minerales, como el cobre.",
        "En Chile hay ejemplos de ambos. El cobre se extrae sobre todo en el norte, por ejemplo en la región de Antofagasta. Los bosques están sobre todo en el centro y el sur. El sol es muy intenso en el desierto del norte, y el mar de la costa entrega peces. Para saber dónde está cada recurso, usamos mapas y fuentes confiables.",
    ],
    vocab=[("recurso natural", "algo que la naturaleza ofrece y las personas usan"), ("renovable", "que se renueva con el tiempo si se usa con cuidado"), ("no renovable", "que no se renueva en el tiempo humano"), ("mineral", "sustancia que se extrae de la tierra, como el cobre"), ("extraer", "sacar un recurso de la tierra")],
    worked=[
        {"title": "Clasificar un recurso", "problem": f"{R1} ¿El petróleo es renovable o no renovable?", "steps": ["Busco el petróleo en la ficha.", "Está entre los recursos que se formaron en millones de años."], "answer": "No renovable"},
        {"title": "Ubicar un recurso", "problem": f"{R1} ¿Dónde se extrae sobre todo el cobre en Chile?", "steps": ["Busco la palabra cobre.", "Dice que sobre todo en el norte, por ejemplo en Antofagasta."], "answer": "En el norte de Chile"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los recursos están en todas partes.", "why": "No se piensa en la distribución.", "fix": "Cada lugar tiene algunos recursos y no otros."},
        {"wrong": "Decir que renovable significa «que nunca se acaba».", "why": "Se olvida el cuidado.", "fix": "Renovable significa que se renueva si lo usamos con cuidado."},
    ],
    tiers={
        "recovery": [
            ex(f"{R1} ¿Qué es un recurso natural?", "algo que la naturaleza ofrece y las personas usan", "La ficha lo define."),
            ex(f"{R1} ¿El agua es un recurso renovable o no renovable?", "renovable", "La ficha la lista entre los renovables."),
            ex(f"{R1} ¿El carbón es renovable o no renovable?", "no renovable", "La ficha lo lista entre los no renovables."),
        ],
        "understand": [
            ex(f"{R1} ¿Por qué el petróleo es no renovable?", "porque se formó en millones de años", "No se renueva en el tiempo humano."),
            ex(f"{R1} ¿Qué recurso se encuentra sobre todo en el centro y sur de Chile?", "los bosques", "La ficha lo indica."),
            ex(f"{R1} ¿Qué recurso muy intenso hay en el desierto del norte de Chile?", "el sol", "La ficha lo indica."),
        ],
        "apply": [
            ex(f"{R1} Clasifica como «renovable» o «no renovable»: el viento.", "renovable", "El viento se renueva."),
            ex(f"{R1} Clasifica como «renovable» o «no renovable»: el cobre.", "no renovable", "Es un mineral que se formó en millones de años."),
            ex(f"{R1} Una empresa quiere instalar paneles solares en el desierto del norte. ¿Qué recurso aprovecha?", "el sol", "El sol es muy intenso allí."),
        ],
        "reason": [
            ex(f"{R1} Tomás dice: «El cobre es renovable porque hay mucho en el norte». ¿Qué error tiene?", "Hay mucho, pero no se renueva en el tiempo humano", "Renovable depende de si se renueva, no de cuánto hay."),
            ex(f"{R1} Ana dice: «Todos los recursos están en todas las regiones de Chile». ¿Qué dato de la ficha la corrige?", "El cobre está sobre todo en el norte y los bosques en el centro y sur", "Los recursos no se reparten por igual."),
        ],
        "challenge": [
            ex(f"{R1} Clasifica cada recurso como «renovable» o «no renovable»: a) peces; b) carbón; c) sol; d) cobre.", "a: renovable; b: no renovable; c: renovable; d: no renovable", "Los peces y el sol se renuevan; el carbón y el cobre no."),
            ex(f"{R1} Un compañero ubica los bosques en el extremo norte desértico. ¿Qué parte del país le indicarías?", "el centro y el sur", "Allí están sobre todo los bosques."),
        ],
    },
    context=[ex("Una familia pasea por la costa de Chile y compra pescado en una caleta. ¿Qué recurso natural usó y de qué tipo es?", "los peces; renovable", "Los peces se renuevan si se pesca con cuidado.")],
    selfcheck=[
        ex("En Historia: ¿Qué es un recurso renovable?", "uno que se renueva con el tiempo si se usa con cuidado", "Es la definición de la ficha."),
        ex("En Historia: ¿Qué es un recurso no renovable?", "uno que no se renueva en el tiempo humano", "Se formó en millones de años."),
        ex("¿Dónde se extrae sobre todo el cobre en Chile?", "en el norte", "La ficha lo indica."),
    ],
    open_task=task(
        f"Dibuja un mapa muy simple de Chile como una franja vertical. Marca el norte con un cobre (escribe «cobre»), el centro y el sur con bosques (escribe «bosques») y la costa con un pez (escribe «peces»). Al lado, escribe una lista con dos recursos renovables y dos no renovables de la ficha. {R1}",
        "Franja con cobre arriba, bosques al sur, peces en la costa. Renovables: sol y agua. No renovables: petróleo y carbón.",
        ["tres recursos ubicados", "dos renovables", "dos no renovables"], ["mapa", "dos listas"], ["poner los bosques en el desierto", "clasificar mal el cobre"],
        "Pregunta cuál de los recursos del mapa usa su familia. Es una conversación abierta."),
    reinforce="Explica con tus palabras la diferencia entre renovable y no renovable con un ejemplo de cada uno.",
    extend="Escribe cinco objetos de tu sala y de qué recurso natural vienen.",
)

# ---------------------------------------------------------------- clase 2
R2 = ("Ficha 2: Cuatro afirmaciones sobre recursos. (A) Etiqueta de un cuaderno: «Papel de bosques con manejo; por cada árbol cortado se plantan nuevos árboles». "
      "(B) Folleto de una empresa: «El petróleo nunca se acabará». No dice quién lo escribió ni de dónde saca los datos. "
      "(C) Informe de una institución científica, con fecha y autor: «El petróleo se formó durante millones de años y las reservas son limitadas». "
      "(D) Cartel de un museo, con fecha: «El agua del planeta circula en un ciclo, pero el agua dulce utilizable es poca y se puede contaminar».")
register(
    OA7, 2,
    materials="Lápiz y papel. Las afirmaciones están escritas en cada ejercicio.",
    use="Aprenderé a revisar las fuentes que hablan de recursos naturales y a distinguir las que tienen respaldo. Sirve para saber cuándo creer una afirmación.",
    prior=["Sé qué es un recurso renovable y no renovable.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Sobre los recursos naturales circulan muchas afirmaciones: en etiquetas, folletos, informes y carteles. Antes de creerlas, preguntamos quién las dijo, cuándo, con qué datos y para qué. Una afirmación con autor, fecha y datos es más confiable que una que solo repite una frase sin decir de dónde sale.",
        "El folleto de la empresa dice que el petróleo nunca se acabará, pero no indica autor ni datos. En cambio, el informe de la institución científica explica que se formó durante millones de años y que las reservas son limitadas. Eso concuerda con lo que sabemos de los recursos no renovables.",
        "Otra pista es el interés de quien habla. Una empresa que vende petróleo puede querer decir que nunca se acabará. Eso no significa que mienta siempre, pero debemos revisar. La etiqueta del cuaderno nos dice que el papel viene de bosques con manejo, es decir, que se cortan y se plantan árboles. Es un uso de un recurso renovable, que requiere cuidado.",
    ],
    vocab=[("etiqueta", "papel pegado a un producto que informa de él"), ("reserva", "cantidad de un recurso que queda por usar"), ("limitado", "que tiene un máximo y puede acabarse"), ("manejo", "forma planificada de usar un recurso"), ("interés", "lo que alguien quiere lograr")],
    worked=[
        {"title": "Evaluar una afirmación", "problem": f"{R2} ¿Es confiable la afirmación B?", "steps": ["Reviso si dice quién la escribió y de dónde saca los datos.", "No dice ninguna de las dos cosas."], "answer": "No, porque no dice quién la escribió ni de dónde saca los datos"},
        {"title": "Contrastar", "problem": f"{R2} ¿Qué dice C que contradice a B?", "steps": ["B dice que el petróleo nunca se acabará.", "C dice que se formó durante millones de años y que las reservas son limitadas."], "answer": "Que las reservas de petróleo son limitadas"},
    ],
    mistakes=[
        {"wrong": "Creer una afirmación solo porque está en un folleto bonito.", "why": "No se revisa quién la dijo.", "fix": "Revisa autor, fecha, datos e interés."},
        {"wrong": "Pensar que todo lo que dice una empresa es falso.", "why": "Se generaliza.", "fix": "Revisa cada afirmación con datos y compara con otras fuentes."},
    ],
    tiers={
        "recovery": [
            ex(f"{R2} ¿Qué afirmación no dice quién la escribió?", "la afirmación B", "Es el folleto de la empresa."),
            ex(f"{R2} ¿Qué afirmación tiene fecha y autor?", "la afirmación C", "Es el informe de la institución científica."),
            ex(f"{R2} ¿De dónde viene el papel del cuaderno de la etiqueta A?", "de bosques con manejo", "La etiqueta lo dice."),
        ],
        "understand": [
            ex(f"{R2} ¿Qué significa que las reservas sean limitadas?", "que tienen un máximo y pueden acabarse", "La palabra limitado indica un máximo."),
            ex(f"{R2} ¿Qué dice D del agua dulce utilizable?", "que es poca y se puede contaminar", "El cartel lo dice."),
            ex(f"{R2} ¿Qué hace el manejo del bosque de la etiqueta A?", "planta nuevos árboles por cada árbol cortado", "Así el bosque se renueva."),
        ],
        "apply": [
            ex(f"{R2} Quieres saber si el petróleo se puede acabar. ¿Qué afirmación usas, B o C?", "C", "Tiene autor, fecha y datos."),
            ex(f"{R2} La afirmación A habla de un recurso. ¿Es renovable o no renovable?", "renovable", "Los bosques se renuevan si se cuidan."),
            ex(f"{R2} La afirmación C habla de un recurso. ¿Es renovable o no renovable?", "no renovable", "El petróleo se formó en millones de años."),
        ],
        "reason": [
            ex(f"{R2} Luis dice: «El folleto B es confiable porque lo hizo una empresa grande». ¿Qué error tiene?", "El tamaño de la empresa no reemplaza a los datos, autor y fecha", "Una fuente se evalúa por su procedencia."),
            ex(f"{R2} Ema dice: «Si el bosque se renueva, se puede cortar todo sin cuidado». ¿Qué dice la etiqueta A?", "Que se plantan nuevos árboles por cada árbol cortado; hay un manejo", "Renovable no significa sin límite."),
        ],
        "challenge": [
            ex(f"{R2} Ordena de más a menos confiable: B, C y D.", "C y D, luego B", "C y D tienen fecha y datos; B no."),
            ex(f"{R2} ¿Por qué una empresa petrolera podría querer decir que el petróleo nunca se acabará?", "porque le conviene seguir vendiéndolo", "Es un interés de quien habla."),
        ],
    },
    context=[ex("Un anuncio en la calle dice: «La energía de este producto es infinita». No tiene autor ni datos. ¿Qué dos preguntas le harías?", "¿Quién lo dice? ¿Con qué datos?", "Son preguntas de procedencia y de evidencia.")],
    selfcheck=[
        ex("¿Qué debemos revisar en una afirmación sobre recursos?", "quién la dijo, cuándo y con qué datos", "Permite ver si es confiable."),
        ex("¿Qué dice el informe C sobre el petróleo?", "que se formó durante millones de años y que sus reservas son limitadas", "Es la afirmación C."),
        ex("¿Qué es el manejo de un bosque?", "una forma planificada de usarlo, plantando árboles nuevos", "Ayuda a que el bosque se renueve."),
    ],
    open_task=task(
        f"Haz una tabla con las afirmaciones A, B, C y D y las columnas: «¿tiene autor o institución?», «¿tiene fecha?», «¿dice de dónde saca los datos?». Completa con sí o no. Al final escribe cuál usarías para un trabajo escolar y por qué. {R2}",
        "A: no se indica autor, sí explica el manejo. B: no, no, no. C: sí, sí, sí. D: no se indica autor, sí fecha, sí explica. Usaría C porque tiene autor, fecha y datos.",
        ["cuatro filas", "decisión justificada"], ["tabla", "una frase"], ["usar B sin explicar", "dejar columnas vacías"],
        "Pregunta qué haría si solo tuviera B. La respuesta esperada es buscar una segunda fuente."),
    reinforce="Nombra tres preguntas que harías a un folleto antes de creerle.",
    extend="Busca una etiqueta de un producto de tu casa y anota qué recurso natural menciona.",
)

# ---------------------------------------------------------------- clase 3
R3 = ("Ficha 3: Recursos en objetos cotidianos. (1) Lápiz: madera de un árbol y grafito, un mineral. (2) Cuaderno: papel hecho de árboles. (3) Botella de plástico: se fabrica a partir del petróleo. "
      "(4) Cable eléctrico: contiene cobre, un metal. (5) Olla de aluminio: el aluminio es un metal que se obtiene de un mineral. (6) Pan: se hace con trigo, que crece con agua y suelo. "
      "(7) Bicicleta: el acero se hace con hierro, un metal que se obtiene de un mineral. Los bosques y los cultivos son renovables si se cuidan. Los metales y el petróleo son no renovables.")
register(
    OA7, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Puedes mirar un lápiz o un cuaderno de tu mochila para pensar.",
    use="Aprenderé a reconocer los recursos naturales que hay dentro de objetos de todos los días y a decir si son renovables o no. Sirve para entender de dónde viene lo que usamos.",
    prior=["Sé qué es un recurso renovable y no renovable.", "Sé que los objetos se fabrican con materiales."],
    explain=[
        "Los objetos que usamos cada día están hechos con recursos naturales. Un lápiz tiene madera de un árbol, un recurso renovable si el bosque se cuida, y grafito, un mineral no renovable. Un cuaderno tiene papel, hecho de árboles. Una botella de plástico se fabrica a partir del petróleo, un recurso no renovable.",
        "Los metales también vienen de recursos naturales. Un cable eléctrico contiene cobre. Una olla de aluminio usa aluminio, que se obtiene de un mineral. Una bicicleta tiene acero, que se hace con hierro, también de un mineral. Los metales y el petróleo son no renovables. El pan viene del trigo, un cultivo renovable que necesita agua y suelo.",
        "Un mismo objeto puede tener recursos de distinto tipo. El lápiz combina uno renovable y otro no renovable. Por eso, al decidir si cuidar un objeto, conviene pensar de qué recursos está hecho. Si un objeto tiene recursos no renovables, es más importante reutilizarlo o reciclarlo para que su material no se pierda.",
    ],
    vocab=[("grafito", "mineral con el que se hace la mina del lápiz"), ("aluminio", "metal que se obtiene de un mineral"), ("acero", "metal hecho con hierro"), ("reciclar", "volver a usar un material para hacer algo nuevo"), ("reutilizar", "volver a usar un objeto sin destruirlo")],
    worked=[
        {"title": "Reconocer los recursos de un objeto", "problem": f"{R3} ¿De qué recursos está hecho un lápiz?", "steps": ["Busco el lápiz en la ficha.", "Tiene madera y grafito."], "answer": "Madera de un árbol y grafito, un mineral"},
        {"title": "Clasificar", "problem": f"{R3} El cable eléctrico contiene cobre. ¿Ese recurso es renovable?", "steps": ["El cobre es un metal que se extrae de la tierra.", "Los metales son no renovables."], "answer": "No, es no renovable"},
    ],
    mistakes=[
        {"wrong": "Decir que el plástico viene de los árboles.", "why": "Se confunde con el papel.", "fix": "El plástico de la botella viene del petróleo."},
        {"wrong": "Decir que un objeto tiene un solo recurso.", "why": "No se analiza cada parte.", "fix": "Revisa todas las partes: el lápiz tiene madera y grafito."},
    ],
    tiers={
        "recovery": [
            ex(f"{R3} ¿De qué recurso viene el plástico de una botella?", "del petróleo", "La ficha lo indica."),
            ex(f"{R3} ¿De qué recurso viene el papel del cuaderno?", "de los árboles", "La ficha lo indica."),
            ex(f"{R3} ¿Qué metal tiene un cable eléctrico?", "cobre", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{R3} ¿Qué metal se usa para hacer acero?", "hierro", "La ficha lo dice."),
            ex(f"{R3} ¿Qué recursos necesita el trigo para crecer?", "agua y suelo", "La ficha lo dice."),
            ex(f"{R3} ¿Por qué el lápiz combina recursos de dos tipos?", "porque la madera es renovable y el grafito es no renovable", "Tiene una parte de cada tipo."),
        ],
        "apply": [
            ex(f"{R3} Clasifica como «renovable» o «no renovable»: la madera de un bosque bien cuidado.", "renovable", "Los bosques son renovables si se cuidan."),
            ex(f"{R3} Clasifica como «renovable» o «no renovable»: el aluminio de una olla.", "no renovable", "Es un metal que se obtiene de un mineral."),
            ex(f"{R3} Clasifica como «renovable» o «no renovable»: el trigo del pan.", "renovable", "Es un cultivo que se vuelve a sembrar."),
        ],
        "reason": [
            ex(f"{R3} Tomás dice: «Una botella de plástico está hecha con un recurso renovable». ¿Qué error tiene?", "El plástico viene del petróleo, que es no renovable", "La ficha lo dice."),
            ex(f"{R3} Ana dice: «Es más importante reciclar una olla de aluminio que un cuaderno de papel de bosque cuidado». ¿Qué razón tiene?", "El aluminio viene de un mineral no renovable", "Conviene cuidar más lo que no se renueva."),
        ],
        "challenge": [
            ex(f"{R3} Clasifica los recursos como «renovable» o «no renovable»: a) madera del lápiz; b) grafito; c) petróleo de la botella; d) trigo.", "a: renovable; b: no renovable; c: no renovable; d: renovable", "Los recursos vegetales se renuevan; los minerales y el petróleo no."),
            ex(f"{R3} Una bicicleta tiene acero de hierro. ¿Qué es mejor para cuidar el recurso: botarla o repararla y reutilizarla?", "repararla y reutilizarla", "Así se aprovecha el metal sin gastar más."),
        ],
    },
    context=[ex("En tu mochila hay un lápiz, un cuaderno de papel y una botella plástica. Según la ficha, ¿cuántos de esos tres objetos tienen algún recurso no renovable?", "2", "El lápiz tiene grafito y la botella viene del petróleo; el cuaderno es solo papel.")],
    selfcheck=[
        ex("¿Qué recurso se usa para fabricar plástico?", "el petróleo", "Es un recurso no renovable."),
        ex("¿El aluminio de una olla es un recurso renovable o no renovable?", "no renovable", "Es un metal que se obtiene de un mineral."),
        ex("En Historia: ¿Qué significa reciclar?", "volver a usar un material para hacer algo nuevo", "Evita perder el recurso."),
    ],
    open_task=task(
        f"Dibuja tres objetos de la ficha (por ejemplo, un lápiz, una botella y un cuaderno) y al lado de cada uno escribe de qué recurso natural viene y si es renovable o no. {R3}",
        "Lápiz: madera (renovable) y grafito (no renovable). Botella: petróleo (no renovable). Cuaderno: árboles (renovable).",
        ["tres objetos", "recurso de cada uno", "clasificación correcta"], ["tres dibujos con rótulos"], ["decir que el plástico es de árboles", "clasificar todo como renovable"],
        "Pregunta qué objeto de los que dibujó se podría reutilizar."),
    reinforce="Elige un objeto de tu casa y di de qué recursos está hecho.",
    extend="Escribe una forma de reutilizar una botella de plástico sin riesgos, como guardar lápices.",
)

# ---------------------------------------------------------------- clase 4
R4 = ("Ficha 4: Tres casos de uso de recursos. CASO 1: en un bosque se cortan 100 árboles al año y se plantan 100. CASO 2: en otro bosque se cortan 150 árboles al año y se plantan 100. "
      "CASO 3: una reserva de petróleo de 120 unidades se usa a razón de 20 unidades por año. Medidas para cuidar los recursos: reducir el uso, reutilizar los objetos y reciclar los materiales. "
      "Dos miradas sobre el caso 2: una empresa quiere cortar 150 árboles para producir más papel; una comunidad vecina quiere cuidar el bosque porque le da agua y sombra.")
register(
    OA7, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a comparar formas de usar los recursos y a distinguir cuáles los cuidan y cuáles los agotan. Sirve para decidir cómo usar los recursos con responsabilidad.",
    prior=["Sé qué es un recurso renovable y no renovable.", "Sé que una perspectiva es un punto de vista."],
    explain=[
        "Un recurso renovable se renueva solo si lo usamos con cuidado. Si cortamos más árboles de los que plantamos, el bosque se reduce y puede acabarse. En el caso 1, se cortan 100 y se plantan 100: el bosque se mantiene. En el caso 2, se cortan 150 y se plantan 100: cada año faltan 50 árboles, y el bosque disminuye.",
        "Los recursos no renovables, como el petróleo, tienen una reserva limitada. Si una reserva tiene 120 unidades y se usan 20 por año, dura 6 años. No se renueva, así que usar menos hoy permite que dure más. Para cuidar los recursos se puede reducir el consumo, reutilizar los objetos y reciclar los materiales.",
        "Las personas pueden tener perspectivas distintas. Una empresa quiere producir más papel; una comunidad quiere cuidar el bosque porque le da agua y sombra. Para decidir, hay que mirar quién gana, quién pierde y qué pasa en el futuro. Cuidar los recursos significa pensar también en quienes vivirán después.",
    ],
    vocab=[("agotar", "gastar un recurso hasta que se acabe"), ("reducir", "usar menos"), ("reutilizar", "volver a usar un objeto"), ("reciclar", "convertir un material usado en uno nuevo"), ("perspectiva", "punto de vista de una persona o grupo")],
    worked=[
        {"title": "Calcular un déficit", "problem": f"{R4} En el caso 2, ¿cuántos árboles faltan cada año?", "steps": ["Se cortan 150 y se plantan 100.", "Resto: 150 − 100 = 50."], "answer": "50 árboles"},
        {"title": "Calcular una duración", "problem": f"{R4} ¿Cuántos años dura la reserva del caso 3?", "steps": ["Hay 120 unidades y se usan 20 por año.", "Divido: 120 ÷ 20 = 6."], "answer": "6 años"},
    ],
    mistakes=[
        {"wrong": "Pensar que un recurso renovable no se puede agotar.", "why": "Se olvida que depende de cómo se use.", "fix": "Si se usa más rápido de lo que se renueva, se agota."},
        {"wrong": "Pensar que usar menos un recurso no renovable no cambia nada.", "why": "No se calcula la duración.", "fix": "Usar menos hace que la reserva dure más años."},
    ],
    tiers={
        "recovery": [
            ex(f"{R4} En el caso 1, ¿se cortan y se plantan la misma cantidad de árboles?", "Sí", "Se cortan 100 y se plantan 100."),
            ex(f"{R4} ¿Qué tres medidas para cuidar los recursos nombra la ficha?", "reducir, reutilizar y reciclar", "Son las medidas de la ficha."),
            ex(f"{R4} ¿Cuántas unidades tiene la reserva de petróleo del caso 3?", "120", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{R4} ¿Por qué el bosque del caso 2 disminuye?", "porque se cortan más árboles de los que se plantan", "Se cortan 150 y se plantan 100."),
            ex(f"{R4} ¿Qué quiere la comunidad con el bosque?", "cuidarlo porque le da agua y sombra", "La ficha lo dice."),
            ex(f"{R4} ¿Qué quiere la empresa con el bosque del caso 2?", "cortar 150 árboles para producir más papel", "La ficha lo dice."),
        ],
        "apply": [
            arith(f"{R4} En el caso 2, ¿cuántos árboles faltan cada año?", "150-100", "Se resta lo plantado de lo cortado.", " árboles"),
            arith(f"{R4} ¿Cuántos años dura la reserva de petróleo si se usan 20 unidades por año?", "120//20", "Se divide la reserva por el uso anual.", " años"),
            arith(f"{R4} Si el uso bajara a 10 unidades por año, ¿cuántos años duraría la reserva de 120 unidades?", "120//10", "Con menos uso, la reserva dura más.", " años"),
        ],
        "reason": [
            ex(f"{R4} Luis dice: «El caso 2 está bien porque los árboles son renovables». ¿Qué error tiene?", "Se cortan más de los que se plantan, así que el bosque disminuye", "Renovable depende del cuidado."),
            ex(f"{R4} Ema dice: «Si usamos menos petróleo, igual se acaba». ¿Tiene razón y qué cambia?", "Sí, pero dura más años", "Usar menos alarga la duración."),
        ],
        "challenge": [
            ex(f"{R4} ¿Cuál es el caso que cuida mejor el bosque: el 1 o el 2?", "el caso 1", "Se plantan tantos árboles como se cortan."),
            ex(f"{R4} Elige la decisión que da papel a la empresa y mantiene el bosque de la comunidad. A) Cortar 150 árboles y plantar 100. B) Cortar 100 árboles y plantar 100.", "B", "Así hay papel y el bosque se mantiene, como en el caso 1."),
        ],
    },
    context=[arith("Una escuela tiene 120 hojas de papel para 6 meses. Si usa la misma cantidad cada mes, ¿cuántas hojas usa al mes?", "120//6", "Se reparte el total entre los meses.", " hojas")],
    selfcheck=[
        ex("¿Cuáles son tres formas de cuidar los recursos?", "reducir, reutilizar y reciclar", "Son medidas de cuidado."),
        ex("¿Cuándo se agota un recurso renovable?", "cuando se usa más rápido de lo que se renueva", "Por eso hay que cuidarlo."),
        ex("¿Qué pasa con una reserva si se usa menos cada año?", "dura más años", "El gasto es menor."),
    ],
    open_task=task(
        f"Escribe una tabla con los casos 1, 2 y 3 y dos columnas: «qué pasa con el recurso» y «qué medida lo cuidaría». Completa con los datos de la ficha. Al final escribe una frase para la empresa y otra para la comunidad del caso 2. {R4}",
        "Caso 1: el bosque se mantiene; seguir plantando. Caso 2: faltan 50 árboles al año; cortar menos. Caso 3: dura 6 años; usar menos. Empresa: puede producir sin agotar el bosque. Comunidad: seguirá teniendo agua y sombra.",
        ["tres casos completos", "dos frases"], ["tabla", "dos frases"], ["decir que todos los casos son iguales", "no mencionar el déficit del caso 2"],
        "Pregunta qué cambia si los árboles plantados son 150. La respuesta esperada es que el bosque se mantiene."),
    reinforce="Explica a alguien cómo calcular cuántos años dura una reserva.",
    extend="Escribe dos acciones de tu casa para reducir el consumo de papel o agua.",
)

# ================================================================ OA 08 · PAISAJES DE AMÉRICA
# ---------------------------------------------------------------- clase 1
S1 = ("Ficha 1: América es un continente que se extiende de norte a sur. Al oeste está el océano Pacífico y al este, el océano Atlántico. Se divide en tres partes: América del Norte (Canadá, Estados Unidos, México), América Central (Guatemala, Costa Rica, Panamá, entre otros) y América del Sur (Brasil, Argentina, Chile, Perú, entre otros). "
      "El mar Caribe tiene muchas islas, como Cuba. La cordillera de los Andes recorre América del Sur de norte a sur. Las Montañas Rocosas están en América del Norte. Chile y Perú tienen costa en el océano Pacífico; Brasil y Argentina tienen costa en el Atlántico. Chile está entre la cordillera de los Andes y el océano Pacífico.")
register(
    OA8, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de América ayuda, pero no es necesario.",
    use="Aprenderé a ubicar el continente americano, sus partes, océanos y algunos países. Sirve para describir paisajes con un lugar claro.",
    prior=["Sé qué es un continente.", "Sé ubicar el norte, el sur, el este y el oeste."],
    explain=[
        "América es un continente que se extiende de norte a sur. Al oeste tiene el océano Pacífico y al este el océano Atlántico. Para estudiarla, se divide en tres partes: América del Norte, América Central y América del Sur. Cada parte tiene varios países.",
        "En América del Norte están Canadá, Estados Unidos y México. En América Central están países como Guatemala, Costa Rica y Panamá. En América del Sur están, entre otros, Brasil, Argentina, Chile y Perú. Además, el mar Caribe, al este de América Central, tiene muchas islas, como Cuba. Chile y Perú tienen costa en el Pacífico; Brasil y Argentina, en el Atlántico; y Chile queda entre los Andes y el Pacífico.",
        "Dos grandes cordilleras recorren el continente: la cordillera de los Andes, en América del Sur, y las Montañas Rocosas, en América del Norte. Para ubicar un paisaje conviene decir en qué parte de América está, qué país es y si está cerca de un océano o de una cordillera.",
    ],
    vocab=[("continente", "gran masa de tierra, como América"), ("océano", "gran extensión de agua salada"), ("cordillera", "cadena de montañas"), ("país", "territorio con un gobierno propio"), ("isla", "tierra rodeada de agua por todos lados")],
    worked=[
        {"title": "Ubicar un país", "problem": f"{S1} ¿En qué parte de América está Chile?", "steps": ["Busco Chile en las listas.", "Está en América del Sur."], "answer": "En América del Sur"},
        {"title": "Ubicar un océano", "problem": f"{S1} ¿Qué océano está al oeste de América?", "steps": ["Busco la palabra oeste.", "Es el océano Pacífico."], "answer": "El océano Pacífico"},
    ],
    mistakes=[
        {"wrong": "Decir que México está en América del Sur.", "why": "Se confunde con países latinoamericanos.", "fix": "Según la ficha, México está en América del Norte."},
        {"wrong": "Confundir el Pacífico con el Atlántico.", "why": "Se olvida su posición.", "fix": "El Pacífico está al oeste y el Atlántico, al este."},
    ],
    tiers={
        "recovery": [
            ex(f"{S1} ¿Qué océano está al este de América?", "el océano Atlántico", "La ficha lo indica."),
            ex(f"{S1} ¿Cuántas partes tiene América según la ficha?", "tres", "América del Norte, Central y del Sur."),
            ex(f"{S1} ¿Qué cordillera recorre América del Sur?", "la cordillera de los Andes", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{S1} ¿En qué parte de América está Canadá?", "en América del Norte", "La ficha lo indica."),
            ex(f"{S1} ¿Qué parte de América tiene a Guatemala, Costa Rica y Panamá?", "América Central", "La ficha lo indica."),
            ex(f"{S1} ¿Dónde están las Montañas Rocosas?", "en América del Norte", "La ficha lo indica."),
        ],
        "apply": [
            ex(f"{S1} Quieres ubicar Brasil. ¿Buscas en América del Norte o en América del Sur?", "en América del Sur", "La ficha lo lista ahí."),
            ex(f"{S1} Quieres ubicar Cuba. ¿En qué mar de la ficha hay muchas islas, como Cuba?", "el mar Caribe", "La ficha lo indica."),
            ex(f"{S1} Un viajero va de Chile a Perú. ¿Cambia de parte de América?", "No", "Ambos están en América del Sur."),
        ],
        "reason": [
            ex(f"{S1} Tomás dice: «El océano Pacífico está al este de América». ¿Qué dato de la ficha lo corrige?", "Al oeste está el Pacífico y al este el Atlántico", "La ficha ubica los océanos."),
            ex(f"{S1} Ana dice: «Los Andes están en América del Norte». ¿Qué dice la ficha?", "Que recorren América del Sur", "Las Montañas Rocosas son las de América del Norte."),
        ],
        "challenge": [
            ex(f"{S1} Clasifica cada lugar en América del Norte, Central o del Sur: a) México; b) Panamá; c) Argentina.", "a: América del Norte; b: América Central; c: América del Sur", "Así aparecen en las listas de la ficha."),
            ex(f"{S1} Elige la frase que ubica bien a Chile. A) Chile está en América del Norte, junto al Atlántico. B) Chile está en América del Sur, entre los Andes y el océano Pacífico.", "B", "Se ubica con ayuda de la cordillera y el océano, según la ficha."),
        ],
    },
    context=[ex("Un amigo te muestra un mapa y dice: «Este país está al oeste y toca el Pacífico». Si es sudamericano, ¿qué dos países de la ficha podrían ser?", "Chile o Perú", "Ambos son de América del Sur y tocan el Pacífico.")],
    selfcheck=[
        ex("¿Qué océano está al oeste de América?", "el Pacífico", "La ficha lo indica."),
        ex("¿Qué tres partes tiene América?", "América del Norte, América Central y América del Sur", "Son las que nombra la ficha."),
        ex("¿Dónde están las Montañas Rocosas?", "en América del Norte", "Es la cordillera del norte."),
    ],
    open_task=task(
        f"Dibuja un mapa muy simple de América: una forma alargada con una cintura angosta en el medio. Escribe «Pacífico» a la izquierda y «Atlántico» a la derecha. Rotula las tres partes: América del Norte, América Central y América del Sur. Marca con un punto Chile y con otro México. {S1}",
        "Forma alargada con tres partes rotuladas, océanos a cada lado, Chile en el sur y México en el norte.",
        ["océanos bien ubicados", "tres partes rotuladas", "dos países ubicados"], ["mapa simple"], ["cambiar de lado los océanos", "poner México en el sur"],
        "Pregunta por qué el Pacífico queda a la izquierda. La respuesta esperada es que está al oeste."),
    reinforce="Nombra tres países de cada parte de América.",
    extend="Escribe cómo irías de Chile a Canadá: por qué partes de América pasarías.",
)

# ---------------------------------------------------------------- clase 2
S2 = ("Ficha 2: Tres fuentes sobre paisajes de América. (A) Fotografía de una selva, con pie de foto «Selva amazónica, Brasil, 2021». (B) Tabla de práctica con datos inventados para ejercitar, no son cifras reales: "
      "Lugar Uno, 3.000 milímetros de lluvia al año; Lugar Dos, 100 milímetros; Lugar Tres, 800 milímetros. (C) Texto sin autor ni fecha que dice que «toda América es calurosa». "
      "Los milímetros de lluvia indican cuánta agua cae: más milímetros significa más lluvia.")
register(
    OA8, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a leer fotografías, tablas y textos para describir paisajes de América, y a revisar si son confiables.",
    prior=["Sé que una fuente tiene procedencia.", "Sé leer una tabla con números."],
    explain=[
        "Para describir un paisaje usamos fuentes: fotografías, mapas, tablas de datos y textos. Una fotografía con pie de foto que dice dónde y cuándo se tomó nos entrega un buen dato. Una tabla con números nos ayuda a comparar, por ejemplo cuánto llueve en cada lugar.",
        "La lluvia se mide en milímetros. Más milímetros significa que cae más agua. En la tabla de práctica, el Lugar Uno recibe 3.000 milímetros al año, el Lugar Dos, 100 y el Lugar Tres, 800. Podemos decir que el Lugar Uno es muy lluvioso y el Lugar Dos es muy seco. Atención: los datos de la tabla son inventados para practicar y no son cifras reales de ningún lugar.",
        "Un texto sin autor ni fecha que dice que toda América es calurosa es poco confiable. Además, es falso: en América hay selvas calurosas, desiertos secos y zonas muy frías. Siempre conviene revisar quién lo dijo, cuándo y con qué datos, y compararlo con otras fuentes.",
    ],
    vocab=[("pie de foto", "texto que explica una fotografía"), ("milímetro de lluvia", "unidad que mide cuánta agua cae"), ("selva", "bosque tropical muy lluvioso y de plantas altas"), ("generalizar", "decir que algo es igual en todas partes"), ("confiable", "que merece que le creamos")],
    worked=[
        {"title": "Leer una tabla", "problem": f"{S2} ¿Qué lugar de la tabla es el más lluvioso?", "steps": ["Comparo 3.000, 100 y 800.", "El mayor es 3.000, el Lugar Uno."], "answer": "El Lugar Uno"},
        {"title": "Evaluar un texto", "problem": f"{S2} ¿Es confiable la fuente C?", "steps": ["Reviso si tiene autor y fecha.", "No tiene ninguno, y generaliza."], "answer": "No, no tiene autor ni fecha y generaliza demasiado"},
    ],
    mistakes=[
        {"wrong": "Creer que toda América tiene el mismo clima.", "why": "Se generaliza.", "fix": "América tiene climas muy distintos."},
        {"wrong": "Usar los datos de práctica como si fueran reales.", "why": "No se lee el aviso.", "fix": "Lee la aclaración: son datos inventados."},
    ],
    tiers={
        "recovery": [
            ex(f"{S2} ¿Qué lugar de la tabla tiene 100 milímetros de lluvia?", "el Lugar Dos", "La tabla lo indica."),
            ex(f"{S2} ¿Dónde se tomó la fotografía A?", "en la selva amazónica, Brasil", "El pie de foto lo dice."),
            ex(f"{S2} ¿Qué fuente no tiene autor ni fecha?", "la fuente C", "Es el texto que generaliza."),
        ],
        "understand": [
            ex(f"{S2} ¿Qué indica una cifra más alta de milímetros?", "más lluvia", "Los milímetros miden cuánta agua cae."),
            ex(f"{S2} ¿Por qué no podemos usar la tabla B para afirmar nada real?", "porque sus datos son inventados", "La ficha lo avisa."),
            ex(f"{S2} ¿Por qué la afirmación «toda América es calurosa» generaliza?", "porque dice que todo el continente es igual", "América tiene climas distintos."),
        ],
        "apply": [
            arith(f"{S2} ¿Cuántos milímetros más llueve en el Lugar Uno que en el Lugar Tres, según la tabla de práctica?", "3000-800", "Se resta la lluvia menor de la mayor.", " milímetros"),
            arith(f"{S2} ¿Cuántos milímetros más llueve en el Lugar Tres que en el Lugar Dos?", "800-100", "Se resta la lluvia menor de la mayor.", " milímetros"),
            ex(f"{S2} ¿Qué lugar de la tabla describirías como seco: el Uno o el Dos?", "el Dos", "Tiene solo 100 milímetros de lluvia."),
        ],
        "reason": [
            ex(f"{S2} Luis dice: «El Lugar Dos está en el Amazonas». ¿Por qué no hay evidencia?", "La tabla no dice dónde están los lugares y es de práctica", "No ubica los lugares."),
            ex(f"{S2} Ema dice: «La fotografía A prueba que en todo Brasil hay selva». ¿Qué error tiene?", "Una foto muestra un lugar, no todo un país", "Es una generalización."),
        ],
        "challenge": [
            ex(f"{S2} Ordena los lugares de más a menos lluviosos.", "Uno, Tres y Dos", "3.000, 800 y 100."),
            ex(f"{S2} ¿Cuál fuente te sirve más para describir cómo se ve una selva: la A, la B o la C?", "la A", "Es una fotografía con lugar y año."),
        ],
    },
    context=[ex("Un video sin título ni fecha dice que en América no hay lugares fríos. ¿Qué dos preguntas le harías antes de usarlo?", "¿Quién lo hizo? ¿Qué datos usa?", "Son las preguntas de procedencia y evidencia.")],
    selfcheck=[
        ex("¿Qué miden los milímetros de lluvia?", "cuánta agua cae", "Más milímetros, más lluvia."),
        ex("¿Qué fuente de la ficha es una fotografía?", "la fuente A", "Es la selva amazónica."),
        ex("¿Por qué conviene revisar autor y fecha de un texto?", "porque ayuda a saber si es confiable", "Es parte de la procedencia."),
    ],
    open_task=task(
        f"Haz una tabla de tres filas con los lugares Uno, Dos y Tres. Escribe sus milímetros de lluvia y una palabra para describirlos: «muy lluvioso», «seco» o «con lluvia moderada». Agrega una frase que diga por qué esta tabla no sirve para afirmar nada real. {S2}",
        "Uno: 3.000, muy lluvioso. Dos: 100, seco. Tres: 800, lluvia moderada. Los datos son inventados.",
        ["tres filas", "descripciones coherentes", "aclaración de datos inventados"], ["tabla", "una frase"], ["usar los datos como reales", "describir al revés"],
        "Pregunta qué diferencia hay entre un lugar con 3.000 y uno con 100 milímetros."),
    reinforce="Cuenta cómo se lee una tabla de lluvia.",
    extend="Averigua en un atlas dónde llueve más en América del Sur y anota la fuente.",
)

# ---------------------------------------------------------------- clase 3
S3 = ("Ficha 3: Paisajes de América. SELVA AMAZÓNICA: bosque tropical muy lluvioso y cálido, recorrido por el río Amazonas, en Sudamérica. DESIERTO DE ATACAMA: en el norte de Chile, uno de los más secos del mundo. "
      "PAMPA: llanura extensa, con pocos árboles, en Argentina y países vecinos. PATAGONIA: región fría y ventosa en el sur de Argentina y de Chile. MONTAÑAS ROCOSAS: cordillera de América del Norte. "
      "CARIBE: islas cálidas y con playas. NORTE DE CANADÁ: clima muy frío. Vocabulario geográfico: llanura es terreno plano; cordillera es una cadena de montañas; desierto es un lugar con muy poca lluvia; río es una corriente de agua; costa es el borde entre la tierra y el mar.")
register(
    OA8, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a describir paisajes de América con clima, ríos y vocabulario geográfico. Sirve para contar cómo es un lugar usando palabras precisas.",
    prior=["Sé ubicar el continente americano.", "Sé leer una tabla de lluvias."],
    explain=[
        "Un paisaje se describe con palabras precisas. El vocabulario geográfico ayuda: una llanura es un terreno plano; una cordillera es una cadena de montañas; un desierto es un lugar con muy poca lluvia; un río es una corriente de agua; la costa es el borde entre la tierra y el mar. El clima describe si hace calor o frío y si llueve mucho o poco.",
        "En América hay paisajes muy distintos. La selva amazónica es calurosa y muy lluviosa, y la recorre el río Amazonas. El desierto de Atacama, en el norte de Chile, es uno de los lugares más secos del mundo. La pampa es una llanura con pocos árboles. La Patagonia es fría y ventosa. En el norte de Canadá hace mucho frío.",
        "Para describir un paisaje conviene decir dónde está, cómo es el clima y qué relieve y agua tiene. Por ejemplo: «La selva amazónica está en Sudamérica, es cálida y lluviosa, y tiene un río muy grande». Así comparamos y evitamos decir que todo es igual en todas partes.",
    ],
    vocab=[("llanura", "terreno plano"), ("cordillera", "cadena de montañas"), ("desierto", "lugar con muy poca lluvia"), ("clima", "estado del tiempo que se repite en un lugar durante muchos años"), ("relieve", "formas de la superficie de la Tierra, como montañas o llanuras")],
    worked=[
        {"title": "Describir un paisaje", "problem": f"{S3} Describe la selva amazónica con tres datos.", "steps": ["Busco su clima: cálido y muy lluvioso.", "Busco su río y su lugar: río Amazonas, en Sudamérica."], "answer": "Es cálida, muy lluviosa y está recorrida por el río Amazonas, en Sudamérica"},
        {"title": "Usar vocabulario", "problem": f"{S3} ¿Qué palabra describe un terreno plano y extenso como la pampa?", "steps": ["Busco la definición de terreno plano.", "Es llanura."], "answer": "Llanura"},
    ],
    mistakes=[
        {"wrong": "Decir que el desierto de Atacama es lluvioso.", "why": "Se confunde con la selva.", "fix": "Un desierto tiene muy poca lluvia."},
        {"wrong": "Decir que la Patagonia es cálida.", "why": "Se piensa en el Caribe.", "fix": "La Patagonia es fría y ventosa."},
    ],
    tiers={
        "recovery": [
            ex(f"{S3} ¿Qué paisaje está en el norte de Chile y es muy seco?", "el desierto de Atacama", "La ficha lo indica."),
            ex(f"{S3} ¿Qué río recorre la selva amazónica?", "el Amazonas", "La ficha lo indica."),
            ex(f"{S3} ¿Qué es una llanura?", "un terreno plano", "La ficha lo define."),
        ],
        "understand": [
            ex(f"{S3} ¿Cómo es el clima de la selva amazónica?", "cálido y muy lluvioso", "La ficha lo dice."),
            ex(f"{S3} ¿Cómo es la Patagonia?", "fría y ventosa", "La ficha lo dice."),
            ex(f"{S3} ¿Qué paisaje tiene islas cálidas y con playas?", "el Caribe", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{S3} Un paisaje es una llanura extensa con pocos árboles en Argentina. ¿Cuál es?", "la pampa", "La ficha lo define así."),
            ex(f"{S3} Un paisaje es una cadena de montañas en América del Norte. ¿Cuál es?", "las Montañas Rocosas", "La ficha lo dice."),
            ex(f"{S3} Un lugar tiene muy poca lluvia y está en Chile. ¿Qué vocabulario geográfico le corresponde?", "desierto", "Un desierto tiene muy poca lluvia."),
        ],
        "reason": [
            ex(f"{S3} Tomás dice: «En toda América hace calor». ¿Qué dato de la ficha lo corrige?", "En el norte de Canadá hace mucho frío y en la Patagonia hace frío", "Hay climas distintos."),
            ex(f"{S3} Ana dice: «La selva amazónica y el desierto de Atacama son iguales». ¿Qué diferencia de clima hay?", "La selva es lluviosa y el desierto es muy seco", "El clima es opuesto."),
        ],
        "challenge": [
            ex(f"{S3} Clasifica cada palabra como «relieve» o «agua»: a) cordillera; b) río; c) llanura; d) costa y mar.", "a: relieve; b: agua; c: relieve; d: agua", "Cordillera y llanura son formas de la tierra; río y mar son agua."),
            ex(f"{S3} Elige la mejor descripción de la Patagonia. A) Está en el norte de Chile y es muy seca. B) Está en el sur de Argentina y de Chile, y es fría y ventosa.", "B", "B incluye lugar y clima según la ficha."),
        ],
    },
    context=[ex("Un turista dice: «Quiero un paisaje cálido con playas». ¿Qué lugar de la ficha le recomiendas?", "el Caribe", "Tiene islas cálidas y con playas.")],
    selfcheck=[
        ex("¿Qué es un desierto?", "un lugar con muy poca lluvia", "Se define por su baja lluvia."),
        ex("¿Qué es una cordillera?", "una cadena de montañas", "Es parte del relieve."),
        ex("¿Qué paisaje es frío y ventoso?", "la Patagonia", "La ficha lo indica."),
    ],
    open_task=task(
        f"Elige uno de los paisajes de la ficha y haz un dibujo con un rótulo de clima, uno de relieve y uno de agua (si hay). Escribe una descripción de tres frases usando al menos tres palabras del vocabulario geográfico. {S3}",
        "Selva amazónica: rótulos clima cálido y lluvioso, relieve llano y río Amazonas. Descripción de tres frases.",
        ["dibujo con tres rótulos", "tres frases", "vocabulario geográfico usado"], ["dibujo", "tres frases"], ["mezclar rasgos de dos paisajes", "describir sin decir dónde está"],
        "Pregunta qué palabra del vocabulario fue más útil."),
    reinforce="Describe en voz alta un paisaje de tu región con clima, relieve y agua.",
    extend="Compara un paisaje de la ficha con uno de tu región en dos frases.",
)

# ---------------------------------------------------------------- clase 4
S4 = ("Ficha 4: Idiomas, países y ciudades de América. En la mayoría de los países de América Central y del Sur y en México se habla español; en Brasil, portugués; en Estados Unidos, inglés; en Canadá, inglés y francés; en Haití, francés y criollo. "
      "También se hablan lenguas indígenas, como el quechua, el náhuatl y las lenguas mayas. Grandes ciudades: Ciudad de México (México), São Paulo (Brasil), Nueva York (Estados Unidos) y Buenos Aires (Argentina). Las cuatro tienen millones de habitantes. "
      "Dos paisajes: la selva amazónica, con ciudades más pequeñas y mucha naturaleza; y una gran ciudad, con edificios, calles y muchas personas. Dos miradas: un turista valora la selva por su naturaleza; una familia indígena que vive allí la valora por su alimento y su hogar.")
register(
    OA8, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a comparar paisajes de América considerando idiomas, países y grandes ciudades, y a notar que un mismo paisaje se valora distinto según quién lo mira.",
    prior=["Sé describir un paisaje con clima y relieve.", "Sé qué es una perspectiva."],
    explain=[
        "En América se hablan muchos idiomas. En la mayoría de los países de América Central y del Sur y en México se habla español. En Brasil se habla portugués. En Estados Unidos se habla inglés, en Canadá inglés y francés, y en Haití francés y criollo. También se hablan lenguas indígenas, como el quechua, el náhuatl y las lenguas mayas.",
        "También hay grandes ciudades, como Ciudad de México, en México; São Paulo, en Brasil; Nueva York, en Estados Unidos; y Buenos Aires, en Argentina. Las cuatro tienen millones de habitantes. Son lugares con muchos edificios, calles y personas, muy distintos de la selva amazónica, que tiene mucha naturaleza y ciudades más pequeñas. Comparar un paisaje natural con una ciudad ayuda a ver cómo las personas usan y modifican el espacio.",
        "Un mismo paisaje se mira desde perspectivas distintas. Un turista puede valorar la selva por su naturaleza. Una familia indígena que vive allí la valora por su alimento y su hogar. Ninguna mirada es falsa, pero cada una destaca algo diferente. Al comparar, conviene decir qué criterio usamos: idioma, clima, población o ciudad.",
    ],
    vocab=[("idioma", "lengua que habla un grupo de personas"), ("población", "conjunto de personas que viven en un lugar"), ("gran ciudad", "ciudad con muchos habitantes y edificios"), ("criollo", "lengua que surge de la mezcla de otras, como la que se habla en Haití"), ("comparar", "mirar en qué se parecen y se diferencian dos cosas")],
    worked=[
        {"title": "Comparar por idioma", "problem": f"{S4} ¿Qué idioma se habla en Brasil y cuál en la mayoría de los países de América Central y del Sur?", "steps": ["Busco Brasil: portugués.", "Busco la mayoría: español."], "answer": "En Brasil, portugués; en la mayoría de los otros, español"},
        {"title": "Comparar paisajes", "problem": f"{S4} Compara la selva amazónica con una gran ciudad en un rasgo.", "steps": ["La selva tiene mucha naturaleza y ciudades más pequeñas.", "La gran ciudad tiene edificios, calles y muchas personas."], "answer": "La selva tiene mucha naturaleza; la gran ciudad tiene muchos edificios y personas"},
    ],
    mistakes=[
        {"wrong": "Decir que en toda América se habla español.", "why": "Se generaliza.", "fix": "Hay portugués, inglés, francés y lenguas indígenas."},
        {"wrong": "Decir que la perspectiva del turista es la única correcta.", "why": "No se piensa en quien vive allí.", "fix": "Una familia indígena puede valorar el paisaje de otra manera."},
    ],
    tiers={
        "recovery": [
            ex(f"{S4} ¿Qué idioma se habla en Brasil?", "portugués", "La ficha lo indica."),
            ex(f"{S4} ¿Qué idioma se habla en Estados Unidos?", "inglés", "La ficha lo indica."),
            ex(f"{S4} ¿Qué dos idiomas se hablan en Canadá?", "inglés y francés", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{S4} ¿Qué lenguas indígenas nombra la ficha?", "quechua, náhuatl y lenguas mayas", "Son las tres que aparecen."),
            ex(f"{S4} ¿Qué cuatro grandes ciudades nombra la ficha?", "Ciudad de México, São Paulo, Nueva York y Buenos Aires", "Son las que aparecen en la ficha."),
            ex(f"{S4} ¿Qué valora una familia indígena de la selva?", "su alimento y su hogar", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{S4} ¿En qué país está São Paulo y qué idioma se habla allí?", "en Brasil; portugués", "La ficha indica el país y el idioma de Brasil."),
            ex(f"{S4} ¿En cuál de estas ciudades se habla español como idioma principal: Nueva York o Buenos Aires?", "Buenos Aires", "Argentina está en América del Sur, donde se habla sobre todo español; Nueva York está en Estados Unidos."),
            ex(f"{S4} ¿En cuántos de estos países se habla inglés, según la ficha: Brasil, Estados Unidos, Canadá y Haití?", "2", "Se habla inglés en Estados Unidos y en Canadá."),
        ],
        "reason": [
            ex(f"{S4} Tomás dice: «En toda América se habla español». ¿Qué dato de la ficha lo corrige?", "En Brasil se habla portugués y en Estados Unidos inglés", "Hay otros idiomas."),
            ex(f"{S4} Ana dice: «La selva solo sirve para pasear». ¿Qué mirada de la ficha la completa?", "Una familia indígena la valora por su alimento y su hogar", "Para algunas personas es su lugar de vida."),
        ],
        "challenge": [
            ex(f"{S4} ¿Qué dato de población entrega la ficha sobre Ciudad de México, São Paulo, Nueva York y Buenos Aires?", "que las cuatro tienen millones de habitantes", "La ficha lo dice."),
            ex(f"{S4} Elige la afirmación mejor sostenida. A) Todas las ciudades de América son iguales. B) Hay selvas, desiertos y grandes ciudades, con paisajes e idiomas muy distintos.", "B", "B respeta la diversidad."),
        ],
    },
    context=[ex("Un viajero va de Buenos Aires a São Paulo y nota que cambia el idioma. ¿Qué idioma esperaba y cuál encuentra?", "esperaba español y encuentra portugués", "Argentina y Brasil tienen idiomas distintos según la ficha.")],
    selfcheck=[
        ex("¿Qué idioma se habla en la mayoría de América Central y del Sur?", "español", "La ficha lo indica."),
        ex("¿Qué es una gran ciudad?", "una ciudad con muchos habitantes y edificios", "Es la definición de la ficha."),
        ex("¿Por qué un mismo paisaje se mira distinto según quién lo ve?", "porque cada persona tiene su perspectiva", "Cada una valora cosas distintas."),
    ],
    open_task=task(
        f"Haz una tabla de dos columnas: «selva amazónica» y «gran ciudad». Escribe en cada una tres rasgos usando la ficha (paisaje, personas, idioma si corresponde). Después escribe una frase con la mirada de un turista y otra con la de una familia indígena sobre la selva. {S4}",
        "Selva: mucha naturaleza, ciudades más pequeñas, idioma portugués si es Brasil. Gran ciudad: edificios, calles, muchas personas. Turista: valora la naturaleza. Familia: valora el alimento y el hogar.",
        ["dos columnas", "tres rasgos cada una", "dos miradas"], ["tabla", "dos frases"], ["inventar datos", "olvidar una mirada"],
        "Pregunta cuál paisaje le gustaría visitar y por qué."),
    reinforce="Nombra cuatro idiomas que se hablan en América y en qué país.",
    extend="Averigua qué idiomas se hablan en tu curso y compáralos con los de la ficha.",
)

# ================================================================ OA 09 · RECURSOS DE AMÉRICA
# ---------------------------------------------------------------- clase 1
T1 = ("Ficha 1: Principales recursos de América y países donde son importantes. PETRÓLEO: Venezuela, México, Estados Unidos, Canadá y Brasil. COBRE: Chile y Perú. LITIO: Chile, Argentina y Bolivia. PLATA: México y Perú. "
      "GAS NATURAL: Bolivia, entre otros. MADERA Y BOSQUES: Brasil y Canadá. PESCA: Perú y Chile. SOYA: Brasil, Argentina y Estados Unidos. CAFÉ: Brasil y Colombia. AGUA DULCE: río Amazonas y Grandes Lagos de Estados Unidos y Canadá.")
register(
    OA9, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de América ayuda, pero no es necesario.",
    use="Aprenderé a reconocer y ubicar algunos de los principales recursos naturales de América. Sirve para entender dónde hay cada recurso y por qué algunos países dependen de él.",
    prior=["Sé qué es un recurso renovable y no renovable.", "Sé ubicar países de América."],
    explain=[
        "América tiene muchos recursos naturales, pero no están repartidos por igual. Algunos países tienen mucho petróleo, como Venezuela, México, Estados Unidos, Canadá y Brasil. El cobre es un recurso muy importante en Chile y Perú. El litio, un mineral que se usa en baterías, se encuentra en Chile, Argentina y Bolivia.",
        "Otros recursos son la plata en México y Perú, el gas natural en Bolivia, la madera y los bosques en Brasil y Canadá, y la pesca en Perú y Chile. También hay recursos agrícolas: la soya en Brasil, Argentina y Estados Unidos, y el café en Brasil y Colombia. El agua dulce está en el río Amazonas y en los Grandes Lagos de Estados Unidos y Canadá.",
        "Para ubicar un recurso, buscamos el mineral, el cultivo o el agua en el mapa y miramos el país. Esto no significa que ese sea el único país que lo tiene, sino uno de los más importantes. Un país con un recurso importante puede vender ese recurso a otros países, y eso influye en su economía.",
    ],
    vocab=[("petróleo", "recurso no renovable usado para combustible y plástico"), ("litio", "mineral usado en baterías"), ("soya", "cultivo cuyos granos son alimento"), ("agua dulce", "agua sin sal, que usamos para beber y regar"), ("economía", "forma en que un país produce y vende cosas")],
    worked=[
        {"title": "Ubicar un recurso", "problem": f"{T1} ¿En qué dos países es importante el cobre?", "steps": ["Busco la palabra cobre.", "Dice Chile y Perú."], "answer": "Chile y Perú"},
        {"title": "Ubicar un país", "problem": f"{T1} ¿Qué recursos de la ficha son importantes en Perú?", "steps": ["Busco Perú en las listas.", "Aparece en cobre, plata y pesca."], "answer": "Cobre, plata y pesca"},
    ],
    mistakes=[
        {"wrong": "Decir que solo Chile tiene cobre.", "why": "Se piensa en el país propio.", "fix": "También Perú lo tiene entre los más importantes."},
        {"wrong": "Decir que el petróleo solo está en un país.", "why": "Se generaliza.", "fix": "La ficha nombra varios países."},
    ],
    tiers={
        "recovery": [
            ex(f"{T1} ¿En qué dos países es importante el cobre?", "Chile y Perú", "La ficha lo indica."),
            ex(f"{T1} ¿Qué recurso se usa en baterías y está en Chile, Argentina y Bolivia?", "el litio", "La ficha lo indica."),
            ex(f"{T1} ¿En qué países es importante el café?", "Brasil y Colombia", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{T1} ¿Qué país de la ficha tiene gas natural?", "Bolivia", "La ficha lo indica."),
            ex(f"{T1} ¿Qué dos países tienen plata?", "México y Perú", "La ficha lo indica."),
            ex(f"{T1} ¿Dónde están los Grandes Lagos?", "entre Estados Unidos y Canadá", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{T1} Un país tiene petróleo, soya y madera. ¿Qué país de la ficha cumple con los tres?", "Brasil", "Brasil aparece en petróleo, madera y soya."),
            ex(f"{T1} ¿Qué recurso comparten Chile y Perú en la ficha, además del cobre?", "la pesca", "Ambos aparecen en pesca."),
            arith(f"{T1} La ficha nombra cinco países con petróleo y dos con cobre. ¿Cuántos países son entre ambos recursos, sin contar los repetidos?", "5+2", "No hay países que aparezcan en ambos listados.", " países"),
        ],
        "reason": [
            ex(f"{T1} Tomás dice: «Solo Chile tiene cobre». ¿Qué dato de la ficha lo corrige?", "También Perú es importante en cobre", "Hay más de un país."),
            ex(f"{T1} Ana dice: «Si un país no aparece en la ficha, no tiene recursos». ¿Qué error tiene?", "La ficha nombra solo algunos países importantes, no todos", "No es una lista completa."),
        ],
        "challenge": [
            ex(f"{T1} Clasifica cada recurso como «mineral», «de cultivo» o «de agua»: a) litio; b) café; c) Grandes Lagos.", "a: mineral; b: de cultivo; c: de agua", "El litio se extrae de la tierra, el café se cultiva y los lagos son agua."),
            ex(f"{T1} ¿Qué país de la ficha aparece en litio y en cobre?", "Chile", "Está en ambas listas."),
        ],
    },
    context=[ex("Una persona dice que Bolivia es importante en gas natural y litio. ¿Qué recurso de esos dos aparece también en Chile y Argentina?", "el litio", "La ficha nombra a los tres países en litio.")],
    selfcheck=[
        ex("¿Qué recurso se usa en baterías?", "el litio", "Es un mineral."),
        ex("¿En qué países es importante la pesca?", "Perú y Chile", "La ficha lo indica."),
        ex("¿Por qué no se reparten los recursos por igual?", "porque cada lugar tiene algunos y no otros", "Depende de la naturaleza de cada territorio."),
    ],
    open_task=task(
        f"Dibuja un mapa muy simple de América y marca con un símbolo cada recurso en uno de sus países: un círculo para el petróleo en México, un triángulo para el cobre en Chile y un cuadrado para el litio en Argentina. Haz una leyenda que explique cada símbolo. {T1}",
        "Mapa con tres símbolos y una leyenda: círculo petróleo, triángulo cobre, cuadrado litio.",
        ["tres recursos ubicados", "leyenda completa"], ["mapa", "leyenda"], ["poner el recurso en un país equivocado", "olvidar la leyenda"],
        "Pregunta qué recurso de su mapa es renovable y cuál no."),
    reinforce="Nombra tres recursos de América y un país para cada uno.",
    extend="Averigua qué recurso importante hay en tu región de Chile.",
)

# ---------------------------------------------------------------- clase 2
T2 = ("Ficha 2: Mapa de práctica con leyenda. Leyenda: triángulo = cobre; círculo = petróleo; cuadrado = litio; rombo = café. El mapa fue hecho por una institución científica, con título «Recursos de América» y año 2022. "
      "Ubicación en el mapa de práctica: triángulos en Chile y Perú; círculos en Venezuela, México y Canadá; cuadrados en Chile, Argentina y Bolivia; rombos en Brasil y Colombia. "
      "Otro mapa sin título, autor ni leyenda muestra solo manchas de colores.")
register(
    OA9, 2,
    materials="Lápiz y papel. El mapa de práctica está descrito en cada ejercicio.",
    use="Aprenderé a leer una leyenda y a evaluar si un mapa de recursos es confiable. Sirve para localizar recursos con un mapa bien hecho.",
    prior=["Sé qué es una leyenda.", "Sé ubicar los recursos de América."],
    explain=[
        "Un mapa de recursos usa símbolos para mostrar dónde hay cada recurso. La leyenda explica qué significa cada símbolo. En nuestro mapa de práctica, un triángulo es cobre, un círculo es petróleo, un cuadrado es litio y un rombo es café. Sin leyenda no sabemos qué significa cada símbolo.",
        "También revisamos la procedencia del mapa. El mapa de práctica fue hecho por una institución científica, tiene título «Recursos de América» y año 2022. Eso lo hace más confiable que otro mapa sin título, autor ni leyenda, que solo muestra manchas de colores. Un mapa confiable dice quién lo hizo, cuándo y qué representa.",
        "Para leer el mapa, miramos cada símbolo y lo buscamos en la leyenda, y luego vemos en qué país está. En el mapa de práctica hay triángulos en Chile y Perú, círculos en Venezuela, México y Canadá, cuadrados en Chile, Argentina y Bolivia, y rombos en Brasil y Colombia.",
    ],
    vocab=[("leyenda", "explicación de los símbolos de un mapa"), ("símbolo", "dibujo simple que representa algo"), ("título", "nombre que dice de qué trata el mapa"), ("institución", "organización que hace o publica un mapa"), ("procedencia", "quién hizo la fuente, cuándo y para qué")],
    worked=[
        {"title": "Leer la leyenda", "problem": f"{T2} ¿Qué recurso representa el cuadrado?", "steps": ["Busco el cuadrado en la leyenda.", "Dice litio."], "answer": "Litio"},
        {"title": "Leer el mapa", "problem": f"{T2} ¿En qué países hay triángulos?", "steps": ["Los triángulos son cobre.", "Están en Chile y Perú."], "answer": "Chile y Perú"},
    ],
    mistakes=[
        {"wrong": "Interpretar un símbolo sin mirar la leyenda.", "why": "Se supone su significado.", "fix": "Busca siempre el símbolo en la leyenda."},
        {"wrong": "Usar un mapa sin título, autor ni leyenda.", "why": "No se revisa su procedencia.", "fix": "Prefiere mapas con título, autor, año y leyenda."},
    ],
    tiers={
        "recovery": [
            ex(f"{T2} ¿Qué recurso representa el círculo?", "el petróleo", "La leyenda lo dice."),
            ex(f"{T2} ¿Qué recurso representa el rombo?", "el café", "La leyenda lo dice."),
            ex(f"{T2} ¿Qué título tiene el mapa?", "Recursos de América", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{T2} ¿Para qué sirve la leyenda?", "para explicar qué significa cada símbolo", "Sin ella no se entiende el mapa."),
            ex(f"{T2} ¿Por qué el mapa con título y año es más confiable que el de manchas?", "porque dice quién lo hizo, cuándo y qué representa", "Esos datos permiten comprobarlo."),
            ex(f"{T2} ¿En cuántos países hay círculos de petróleo en el mapa de práctica?", "3", "Hay círculos en Venezuela, México y Canadá."),
        ],
        "apply": [
            ex(f"{T2} ¿Qué recurso representan los símbolos en Brasil y Colombia?", "el café", "Los rombos están ahí."),
            ex(f"{T2} ¿En qué país aparecen un triángulo y un cuadrado?", "Chile", "Chile tiene cobre y litio."),
            arith(f"{T2} El mapa tiene cuadrados en tres países y rombos en dos. ¿Cuántos símbolos de litio y café hay entre ambos?", "3+2", "Se suman los países de cada símbolo.", " símbolos"),
        ],
        "reason": [
            ex(f"{T2} Luis dice: «El mapa de manchas es igual de confiable». ¿Qué error tiene?", "No tiene título, autor ni leyenda", "No permite comprobar su procedencia."),
            ex(f"{T2} Ema dice: «Si Brasil solo tiene rombos, no tiene otros recursos». ¿Qué error tiene?", "El mapa de práctica no muestra todos los recursos", "Solo representa cuatro recursos."),
        ],
        "challenge": [
            ex(f"{T2} ¿Qué dos recursos aparecen en Chile según el mapa de práctica?", "cobre y litio", "Tiene triángulo y cuadrado."),
            ex(f"{T2} Un compañero lee un círculo en Canadá como cobre. ¿Cómo lo corriges?", "El círculo es petróleo, según la leyenda", "La leyenda dice que el círculo es petróleo."),
        ],
    },
    context=[ex("En un diario ves un mapa sin leyenda con triángulos rojos. ¿Qué harías antes de decir qué recurso representan?", "buscar una leyenda o una explicación del mapa", "Sin leyenda no se sabe qué significan.")],
    selfcheck=[
        ex("En Historia: ¿Qué es una leyenda?", "la explicación de los símbolos de un mapa", "Dice qué significa cada símbolo."),
        ex("¿Qué recurso es el triángulo en el mapa de práctica?", "el cobre", "La leyenda lo dice."),
        ex("¿Qué hace más confiable a un mapa?", "tener título, autor, año y leyenda", "Así se puede comprobar."),
    ],
    open_task=task(
        f"Dibuja una leyenda con los cuatro símbolos de la ficha y su significado. Después dibuja un mapa muy simple de Sudamérica y marca con los símbolos correctos Chile (cobre y litio), Brasil (café) y Venezuela (petróleo). {T2}",
        "Leyenda con triángulo cobre, círculo petróleo, cuadrado litio y rombo café. Mapa con Chile triángulo y cuadrado, Brasil rombo, Venezuela círculo.",
        ["leyenda completa", "tres países marcados con los símbolos correctos"], ["leyenda", "mapa"], ["usar un símbolo para dos recursos", "olvidar un país"],
        "Pregunta qué símbolo usó para cada recurso y por qué."),
    reinforce="Explica a alguien cómo leer un mapa con leyenda.",
    extend="Diseña tus propios símbolos para tres recursos y haz una leyenda.",
)

# ---------------------------------------------------------------- clase 3
T3 = ("Ficha 3: Usos de algunos recursos de América. COBRE: se usa en cables eléctricos y tuberías. PETRÓLEO: se usa como combustible y para fabricar plástico. LITIO: se usa en baterías de teléfonos y de algunos vehículos. "
      "MADERA: se usa para papel, muebles y construcción. AGUA DULCE: se usa para beber, regar cultivos y producir electricidad. CAFÉ y SOYA: son alimentos que muchos países venden a otros. "
      "Un país vende un recurso a otros países: esto se llama exportar.")
register(
    OA9, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé para qué se usan los recursos de América y cómo se relacionan con la vida diaria. Sirve para entender por qué son valiosos y por qué hay que cuidarlos.",
    prior=["Sé ubicar recursos de América.", "Sé qué es un recurso renovable y no renovable."],
    explain=[
        "Los recursos tienen usos concretos. El cobre se usa en cables eléctricos y tuberías. El petróleo se usa como combustible y para fabricar plástico. El litio se usa en baterías de teléfonos y de algunos vehículos. La madera sirve para papel, muebles y construcción. El agua dulce sirve para beber, regar cultivos y producir electricidad.",
        "El café y la soya son alimentos que muchos países venden a otros. Cuando un país vende un recurso a otros países, decimos que lo exporta. Para algunos países, exportar recursos es una parte importante de su economía. Por eso es importante cuidar los recursos: si se acaban, esa economía se ve afectada.",
        "Algunos recursos son renovables, como el agua dulce y la madera de bosques cuidados, y otros son no renovables, como el cobre, el petróleo y el litio. Los usos de hoy influyen en lo que habrá mañana. Por eso hablamos de desarrollo sostenible: usar los recursos de modo que también queden para el futuro.",
    ],
    vocab=[("exportar", "vender un recurso o producto a otros países"), ("combustible", "sustancia que se quema para dar energía"), ("batería", "aparato que guarda energía eléctrica"), ("desarrollo sostenible", "usar los recursos hoy sin impedir que los usen las próximas generaciones"), ("tubería", "tubo por donde pasa el agua u otros líquidos")],
    worked=[
        {"title": "Relacionar recurso y uso", "problem": f"{T3} ¿Para qué se usa el litio?", "steps": ["Busco la palabra litio.", "Se usa en baterías."], "answer": "En baterías de teléfonos y de algunos vehículos"},
        {"title": "Clasificar", "problem": f"{T3} ¿El cobre es renovable o no renovable?", "steps": ["El cobre es un mineral.", "Los minerales son no renovables."], "answer": "No renovable"},
    ],
    mistakes=[
        {"wrong": "Decir que el petróleo solo sirve como combustible.", "why": "Se olvida el plástico.", "fix": "También se usa para fabricar plástico."},
        {"wrong": "Decir que exportar es comprar.", "why": "Se confunde con importar.", "fix": "Exportar es vender a otros países."},
    ],
    tiers={
        "recovery": [
            ex(f"{T3} ¿Para qué se usa el cobre?", "en cables eléctricos y tuberías", "La ficha lo indica."),
            ex(f"{T3} ¿Para qué se usa el petróleo?", "como combustible y para fabricar plástico", "La ficha lo indica."),
            ex(f"{T3} ¿Qué significa exportar?", "vender un recurso a otros países", "La ficha lo define."),
        ],
        "understand": [
            ex(f"{T3} ¿Qué recurso sirve para hacer papel y muebles?", "la madera", "La ficha lo indica."),
            ex(f"{T3} ¿Para qué se usa el agua dulce?", "para beber, regar cultivos y producir electricidad", "La ficha lo indica."),
            ex(f"{T3} ¿Qué es el desarrollo sostenible?", "usar los recursos hoy sin impedir que los usen las próximas generaciones", "La ficha lo explica."),
        ],
        "apply": [
            ex(f"{T3} Un teléfono usa una batería. ¿Qué recurso de la ficha contiene?", "litio", "El litio se usa en baterías."),
            ex(f"{T3} Una casa necesita cables eléctricos. ¿Qué recurso necesita?", "cobre", "El cobre se usa en cables."),
            ex(f"{T3} Un país vende café a otros países. ¿Qué hace con el café?", "lo exporta", "Vender a otros países es exportar."),
        ],
        "reason": [
            ex(f"{T3} Tomás dice: «Si el cobre se acaba, no pasa nada con la economía de los países que lo venden». ¿Qué error tiene?", "Para algunos países exportar recursos es una parte importante de su economía", "La ficha lo indica."),
            ex(f"{T3} Ana dice: «La madera es no renovable». ¿Qué decir si el bosque se cuida?", "Que es renovable, porque los bosques cuidados se renuevan", "Depende del cuidado."),
        ],
        "challenge": [
            ex(f"{T3} Clasifica cada recurso como «renovable» o «no renovable»: a) agua dulce; b) petróleo; c) madera de bosques cuidados; d) litio.", "a: renovable; b: no renovable; c: renovable; d: no renovable", "El agua y la madera cuidada se renuevan; el petróleo y el litio no."),
            ex(f"{T3} Elige la frase correcta. A) Exportar recursos no tiene relación con cuidarlos. B) Si el recurso se acaba, quienes dependen de exportarlo pierden ingresos.", "B", "B relaciona exportar con cuidar."),
        ],
    },
    context=[ex("Un auto eléctrico usa baterías. ¿Qué recurso mineral se necesita para fabricar esas baterías?", "litio", "La ficha lo indica.")],
    selfcheck=[
        ex("¿Qué recurso se usa para fabricar plástico?", "el petróleo", "Además de combustible."),
        ex("¿Qué es exportar?", "vender a otros países", "Es lo contrario de comprar a otros países."),
        ex("¿Qué recurso sirve para hacer baterías?", "el litio", "Se usa en teléfonos y vehículos."),
    ],
    open_task=task(
        f"Haz una tabla con tres columnas: «recurso», «para qué se usa» y «¿renovable o no?». Completa cuatro filas con recursos de la ficha. Después escribe una frase que explique por qué cuidar el recurso que elijas. {T3}",
        "Cobre: cables y tuberías; no renovable. Madera: papel y muebles; renovable. Litio: baterías; no renovable. Agua dulce: beber y regar; renovable.",
        ["cuatro filas completas", "clasificación correcta", "una razón para cuidar"], ["tabla", "una frase"], ["clasificar mal el litio", "olvidar un uso"],
        "Pregunta qué recurso de la tabla usa más su familia."),
    reinforce="Nombra tres recursos y para qué sirve cada uno.",
    extend="Averigua qué usos tiene el cobre además de los de la ficha.",
)

# ---------------------------------------------------------------- clase 4
T4 = ("Ficha 4: Caso de práctica. Un pueblo de América tiene un bosque grande. (A) Una empresa quiere cortar todo el bosque para vender madera rápido. (B) La comunidad quiere conservar el bosque porque le da agua limpia, leña y alimentos. "
      "(C) La autoridad propone cortar solo una parte cada año y plantar árboles nuevos para reemplazarla. Desarrollo sostenible significa usar los recursos para vivir hoy sin impedir que las próximas generaciones los usen. "
      "Cuidar los recursos puede significar reducir, reutilizar y reciclar, proteger zonas y plantar árboles. Si de un bosque de 400 árboles se cortan 40 al año y se plantan 40, el bosque se mantiene.")
register(
    OA9, 4,
    materials="Lápiz y papel. El caso está escrito en cada ejercicio.",
    use="Aprenderé a comparar decisiones sobre el uso de un recurso y a elegir la que cuida el recurso y también atiende las necesidades de hoy. Sirve para participar en decisiones de tu comunidad.",
    prior=["Sé qué es un recurso renovable y no renovable.", "Sé que las personas tienen perspectivas distintas."],
    explain=[
        "Una decisión sobre un recurso afecta a muchas personas. En nuestro caso hay tres posturas. La empresa quiere cortar todo el bosque para vender madera rápido. La comunidad quiere conservarlo porque le da agua limpia, leña y alimentos. La autoridad propone cortar solo una parte cada año y plantar árboles nuevos.",
        "El desarrollo sostenible es usar los recursos para vivir hoy sin impedir que las próximas generaciones los usen. Para decidir, comparamos: ¿qué gana cada grupo?, ¿qué pierde?, ¿qué pasa en el futuro? Si se corta todo el bosque, la empresa gana hoy, pero la comunidad pierde su agua y su leña, y no queda bosque para después.",
        "La propuesta de la autoridad se parece más al desarrollo sostenible: se usa una parte del bosque y se plantan árboles nuevos. Por ejemplo, si de un bosque de 400 árboles se cortan 40 al año y se plantan 40, el bosque se mantiene. Cada decisión tiene ventajas y costos, y por eso es importante escuchar a todas las partes.",
    ],
    vocab=[("desarrollo sostenible", "usar los recursos hoy sin impedir que los usen las próximas generaciones"), ("conservar", "mantener algo en buen estado"), ("generación", "grupo de personas que nacen en una misma época"), ("postura", "opinión o posición de una persona o grupo"), ("reemplazar", "poner algo nuevo en el lugar de lo que se sacó")],
    worked=[
        {"title": "Elegir lo sostenible", "problem": f"{T4} ¿Qué propuesta se parece más al desarrollo sostenible?", "steps": ["La A corta todo el bosque.", "La C corta una parte y planta árboles nuevos."], "answer": "La propuesta C de la autoridad"},
        {"title": "Calcular el equilibrio", "problem": f"{T4} Si se cortan 40 árboles y se plantan 40, ¿cuántos árboles se pierden en total por año?", "steps": ["Resto lo cortado menos lo plantado.", "40 − 40 = 0."], "answer": "0 árboles"},
    ],
    mistakes=[
        {"wrong": "Pensar que cuidar un recurso es no usarlo nunca.", "why": "Se confunde cuidar con prohibir.", "fix": "Cuidar es usarlo de modo que también quede para el futuro."},
        {"wrong": "Pensar que solo importa la opinión de la empresa.", "why": "No se escucha a la comunidad.", "fix": "Hay que escuchar a todas las partes."},
    ],
    tiers={
        "recovery": [
            ex(f"{T4} ¿Qué quiere la empresa?", "cortar todo el bosque para vender madera rápido", "La ficha lo dice."),
            ex(f"{T4} ¿Qué quiere la comunidad?", "conservar el bosque", "La ficha lo dice."),
            ex(f"{T4} ¿Qué propone la autoridad?", "cortar una parte cada año y plantar árboles nuevos", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{T4} ¿Qué recursos le da el bosque a la comunidad?", "agua limpia, leña y alimentos", "La ficha los nombra."),
            ex(f"{T4} ¿Qué es el desarrollo sostenible?", "usar los recursos hoy sin impedir que los usen las próximas generaciones", "La ficha lo define."),
            ex(f"{T4} ¿Qué pierde la comunidad si se corta todo el bosque?", "su agua, su leña y sus alimentos", "El bosque se los da."),
        ],
        "apply": [
            arith(f"{T4} Si de un bosque de 400 árboles se cortan 40 y se plantan 40, ¿cuántos árboles quedan al final del año?", "400-40+40", "Se resta lo cortado y se suma lo plantado.", " árboles"),
            arith(f"{T4} Si se cortan 40 árboles y solo se plantan 10, ¿cuántos árboles quedan de un bosque de 400?", "400-40+10", "Se resta lo cortado y se suma lo plantado.", " árboles"),
            ex(f"{T4} ¿Qué propuesta usa el bosque y a la vez lo cuida: la A o la C?", "la C", "Corta una parte y planta árboles nuevos."),
        ],
        "reason": [
            ex(f"{T4} Luis dice: «Cortar todo el bosque es sostenible porque la empresa gana dinero». ¿Qué error tiene?", "No deja bosque para el futuro y la comunidad pierde sus recursos", "Sostenible significa pensar también en el mañana."),
            ex(f"{T4} Ema dice: «Cuidar un recurso es no usarlo nunca». ¿Qué dice la ficha del desarrollo sostenible?", "Que se usan los recursos hoy sin impedir que los usen las próximas generaciones", "Cuidar es usar con equilibrio, no solo prohibir."),
        ],
        "challenge": [
            ex(f"{T4} ¿Qué ventaja tiene la propuesta C que la A no tiene: vender madera más rápido o que el bosque se mantiene para el futuro?", "que el bosque se mantiene para el futuro", "La A vende más rápido, pero deja sin bosque; la C lo mantiene."),
            ex(f"{T4} Elige la mejor decisión. A) Cortar todo el bosque. B) Cortar una parte cada año, plantar árboles nuevos y escuchar a la comunidad.", "B", "B cuida el recurso y atiende varias necesidades."),
        ],
    },
    context=[ex("Un pueblo costero pesca peces todo el año y nota que cada año hay menos. ¿Qué medida es más sostenible: A) pescar aún más para ganar lo mismo, o B) pescar menos y dejar descansar zonas?", "B", "Así los peces se renuevan y el recurso queda para el futuro.")],
    selfcheck=[
        ex("¿Qué es el desarrollo sostenible?", "usar los recursos hoy sin impedir que los usen las próximas generaciones", "Piensa en el futuro."),
        ex("¿Qué propuesta del caso cuida mejor el bosque?", "la C de la autoridad", "Planta árboles nuevos."),
        ex("¿Por qué conviene escuchar a todas las partes?", "porque cada una tiene necesidades y miradas distintas", "Ayuda a decidir mejor."),
    ],
    open_task=task(
        f"Escribe una carta corta de una niña o niño del pueblo a la autoridad. En la carta debe haber una petición clara, dos razones sacadas de la ficha y una medida concreta para cuidar el bosque. {T4}",
        "Estimada autoridad: le pido que apoye cortar solo una parte del bosque cada año y plantar árboles nuevos. Así la comunidad seguirá teniendo agua limpia y leña. Además, el bosque quedará para las próximas generaciones.",
        ["una petición", "dos razones de la ficha", "una medida concreta"], ["carta corta"], ["pedir cortar todo", "no dar razones"],
        "Pide que lea la carta y que diga qué parte es la petición y cuáles son las razones."),
    reinforce="Explica con tus palabras qué es desarrollo sostenible con un ejemplo de tu barrio.",
    extend="Escribe dos acciones de tu familia o curso para cuidar un recurso natural.",
)

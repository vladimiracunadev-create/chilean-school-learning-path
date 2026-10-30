"""Cuaderno del estudiante, 1.º básico Ciencias Naturales: OA 05 (plantas y animales de Chile y su cuidado) y OA 06 (sentidos y prevención de riesgos)."""
from __future__ import annotations

from student_content_cn_a import task
from student_lessons import arith, ex, register

OA5, OA6 = "CN01 OA 05", "CN01 OA 06"

# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Este cuaderno con la ficha de seis seres vivos de Chile (tamaño aproximado, cubierta o forma y lugar donde viven), lápiz y colores.",
    use="Aprenderé a reconocer plantas y animales de Chile y a describirlos con datos. Sirve para conocer lo que hay cerca de nosotros y cuidarlo.",
    prior=["Sé la ficha de naturalista.", "Sé que cada ser vivo tiene un hábitat."],
    explain=[
        "En Chile viven plantas y animales muy distintos porque el país es largo y tiene desierto, bosque, cordillera y mar. Algunos viven solo aquí o casi solo aquí, y por eso son parte de lo que nos hace únicos.",
        "Hoy conocemos seis. El copihue es una flor roja del bosque del sur. La araucaria es un árbol que puede llegar a medir unos 40 m. El cóndor es un ave de la cordillera con alas de unos 3 m de punta a punta. El pudú es un ciervo muy pequeño de unos 40 cm. El guanaco mide unos 110 cm. La ranita de Darwin mide unos 3 cm.",
        "Para describir un ser vivo de Chile usa datos que puedas observar: tamaño, cubierta o forma, y dónde vive. Así puedes compararlo con otro sin confundirte.",
    ],
    vocab=[("biodiversidad", "variedad de plantas y animales que hay en un lugar"), ("copihue", "flor roja del bosque del sur de Chile"), ("araucaria", "árbol alto de la cordillera del sur de Chile"), ("pudú", "ciervo muy pequeño del bosque del sur"), ("cóndor", "ave grande de la cordillera")],
    worked=[
        {"title": "Leer una ficha", "problem": "Pudú: unos 40 cm, pelo café, bosque del sur de Chile. Guanaco: unos 110 cm, pelo café claro, cordillera. ¿Cuál es más alto?", "steps": ["Comparo 40 con 110.", "110 es mayor que 40.", "El guanaco es más alto."], "answer": "El guanaco; unos 70 cm más alto"},
        {"title": "Unir ser vivo y lugar", "problem": "Copihue, cóndor y ranita de Darwin. Lugares: bosque del sur, cordillera, desierto. ¿Dónde vive el cóndor?", "steps": ["El cóndor es un ave grande.", "Sus alas lo llevan sobre la cordillera."], "answer": "El cóndor vive en la cordillera"},
    ],
    mistakes=[
        {"wrong": "Decir que el cóndor es un animal pequeño porque vuela.", "why": "Se mezcla volar con ser pequeño.", "fix": "Mira el dato: sus alas miden unos 3 m de punta a punta."},
        {"wrong": "Pensar que todas las plantas de Chile son iguales a las de otros países.", "why": "No se conoce la variedad del país.", "fix": "Observa datos: el copihue y la araucaria crecen en el sur de Chile y en zonas cercanas, y no en todos los países."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál de estos seres vivos de Chile es una flor roja: el copihue o la araucaria?", "El copihue", "El copihue tiene flores rojas."),
            ex("¿Cuál es un ave grande de la cordillera: el cóndor o el pudú?", "El cóndor", "El pudú es un ciervo."),
            ex("¿Qué animal chileno mide unos 3 cm: la ranita de Darwin o el guanaco?", "La ranita de Darwin", "El guanaco mide unos 110 cm."),
        ],
        "understand": [
            ex("¿Qué es la biodiversidad?", "La variedad de plantas y animales que hay en un lugar", "Incluye muchos tipos de seres vivos."),
            ex("¿Por qué hay seres vivos tan distintos en Chile?", "Porque tiene desierto, bosque, cordillera y mar", "Cada lugar da condiciones distintas."),
            ex("¿Qué datos usamos para describir un ser vivo de Chile?", "Tamaño, cubierta o forma y lugar donde vive", "Son datos observables."),
        ],
        "apply": [
            arith("El guanaco mide unos 110 cm y el pudú unos 40 cm. ¿Cuántos centímetros más alto es el guanaco?", "110-40", "Se resta la medida del pudú a la del guanaco.", " cm"),
            arith("Una araucaria adulta puede medir 40 m (dato de ejemplo) y una araucaria joven mide 5 m. ¿Cuántos metros más mide la adulta?", "40-5", "Se resta la medida pequeña a la grande.", " m"),
            ex("Ficha: unos 3 cm, vive en el bosque húmedo del sur. ¿Qué animal chileno es?", "La ranita de Darwin", "Es el único de la lista con ese tamaño."),
        ],
        "reason": [
            ex("Ema dice que el pudú y el guanaco son iguales porque los dos son café. ¿Qué dato muestra que no son iguales?", "Su tamaño: 40 cm y 110 cm", "La medida es distinta."),
            ex("Un niño dice que el cóndor no es de Chile porque lo vio en un dibujo de otro país. ¿Qué respondes?", "Que el cóndor vive en la cordillera de Chile", "Se observa en la cordillera chilena."),
        ],
        "challenge": [
            ex("Escribe un ser vivo de Chile y dos datos de él.", "Por ejemplo el copihue: flor roja y bosque del sur", "Dos datos observables."),
            ex("En una cordillera ves 2 cóndores y 5 guanacos. ¿Cuántos animales ves?", "7", "Dos más cinco son siete."),
        ],
    },
    context=[ex("Imagina que un guía del parque dice que en el bosque del sur hay 3 copihues florecidos, 2 pudúes y 4 ranitas de Darwin en un sendero. ¿Cuántos seres vivos de la lista hay en total?", "9", "Tres más dos más cuatro son nueve.")],
    selfcheck=[ex("¿El cóndor vive en la cordillera o en el mar?", "En la cordillera", "Es un ave de cerros altos."), ex("¿El copihue es un animal o una planta?", "Una planta", "Es una flor."), ex("¿Qué animal es el más pequeño de la clase?", "La ranita de Darwin", "Mide unos 3 cm.")],
    open_task=task("Escribe una ficha para dos de estos seres vivos de Chile con los datos dados: cóndor (ave, alas de unos 3 m, cordillera), pudú (ciervo, unos 40 cm, bosque del sur), copihue (flor roja, bosque del sur). Dibuja uno.", "Ficha del pudú: ciervo de unos 40 cm, vive en el bosque del sur. Ficha del cóndor: ave con alas de unos 3 m, vive en la cordillera.", ["escribe tres datos por ficha", "usa números con unidad", "dibuja uno"], ["dos fichas", "dibujo"], ["escribir opiniones", "olvidar la unidad"], "Reconoce los datos y pide usar la unidad en cada medida."),
    reinforce="Pregunta a alguien de tu casa qué planta o animal de Chile conoce y descríbelo.",
    extend="Compara dos animales de Chile con sus tamaños.",
)

register(
    OA5, 2,
    materials="Este cuaderno con una tabla de comparación de dos animales y dos plantas de Chile, lápiz y colores.",
    use="Aprenderé a comparar plantas y animales de Chile con una tabla. Sirve para ver en qué se parecen y en qué se diferencian.",
    prior=["Sé reconocer algunos seres vivos de Chile.", "Sé comparar medidas."],
    explain=[
        "Comparar es mirar dos cosas y decir en qué se parecen y en qué son distintas. Se hace con una tabla: en cada fila se pone un dato, como tamaño, color o lugar donde vive, y en cada columna un ser vivo.",
        "Ejemplo: el guanaco mide unos 110 cm y vive en la cordillera. El pudú mide unos 40 cm y vive en el bosque del sur. Son parecidos porque los dos tienen pelo, y distintos porque no miden lo mismo ni viven en el mismo lugar.",
        "Para plantas pasa lo mismo. La araucaria puede medir unos 40 m y tiene hojas duras y puntiagudas. El copihue es una enredadera de flores rojas. Una buena comparación dice una semejanza y una diferencia con datos.",
    ],
    vocab=[("comparar", "mirar dos cosas y ver en qué se parecen y en qué se diferencian"), ("semejanza", "algo que se parece"), ("diferencia", "algo que no es igual"), ("tabla", "cuadro con filas y columnas para ordenar datos"), ("enredadera", "planta que sube enrollándose en otra cosa")],
    worked=[
        {"title": "Comparar dos animales", "problem": "Guanaco: unos 110 cm, pelo, cordillera. Pudú: unos 40 cm, pelo, bosque del sur. Escribe una semejanza y una diferencia.", "steps": ["Los dos tienen pelo: semejanza.", "110 cm y 40 cm son distintos: diferencia.", "Viven en lugares distintos: diferencia."], "answer": "Semejanza: tienen pelo. Diferencia: el guanaco mide 70 cm más"},
        {"title": "Comparar dos plantas", "problem": "Araucaria: árbol de unos 40 m. Copihue: enredadera con flores rojas. ¿Cuál es un árbol?", "steps": ["Un árbol es alto y se sostiene solo.", "La enredadera necesita apoyo."], "answer": "La araucaria es un árbol"},
    ],
    mistakes=[
        {"wrong": "Escribir solo diferencias.", "why": "Se piensa que comparar es buscar lo distinto.", "fix": "Escribe también una semejanza."},
        {"wrong": "Decir «es más lindo» como diferencia.", "why": "Es una opinión.", "fix": "Usa datos de la tabla, como tamaño o lugar."},
    ],
    tiers={
        "recovery": [
            ex("Tabla: guanaco 110 cm, pudú 40 cm. ¿Cuál es más pequeño?", "El pudú", "40 es menor que 110."),
            ex("Tabla: el guanaco vive en la cordillera y el pudú en el bosque. ¿Viven en el mismo lugar?", "No", "Los lugares son distintos."),
            ex("Tabla: ambos tienen pelo. ¿Es una semejanza o una diferencia?", "Una semejanza", "Tienen lo mismo."),
        ],
        "understand": [
            ex("¿Qué es una semejanza?", "Algo que se parece entre dos cosas", "Es lo mismo en ambos."),
            ex("¿Qué es una diferencia?", "Algo que no es igual entre dos cosas", "Cambia entre uno y otro."),
            ex("¿Qué va en las filas de una tabla de comparación?", "Un dato, como tamaño o lugar", "Cada fila trae un dato."),
        ],
        "apply": [
            arith("El guanaco mide 110 cm y el pudú 40 cm. ¿Cuál es la diferencia de tamaño en centímetros?", "110-40", "Se resta el tamaño menor al mayor.", " cm"),
            ex("Tabla de ejemplo: araucaria adulta de 40 m y araucaria joven de 5 m. ¿Cuántos metros más alta es la adulta?", "35 m", "Cuarenta menos cinco son treinta y cinco."),
            ex("Cóndor: vuela, plumas. Guanaco: camina, pelo. Escribe una diferencia.", "El cóndor vuela y el guanaco camina", "Se mueven de manera distinta."),
        ],
        "reason": [
            ex("Beto dice que el cóndor y el guanaco son parecidos porque los dos viven en la cordillera. ¿Es suficiente para decir que son iguales?", "No", "Es solo una semejanza; se distinguen en cubierta y forma de moverse."),
            ex("¿Por qué una comparación con una semejanza y una diferencia es mejor que una con solo una?", "Porque muestra qué es igual y qué cambia", "Da una visión completa."),
        ],
        "challenge": [
            ex("Compara la araucaria y el copihue con un dato de semejanza.", "Por ejemplo los dos son plantas de Chile", "Ambos son plantas del sur."),
            ex("Hay 3 animales con pelo y 2 con plumas. ¿Cuántos animales hay?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("Un cartel del parque dice que el pudú mide unos 40 cm y la ranita de Darwin unos 3 cm. ¿Cuántos centímetros más mide el pudú?", "37 cm", "Cuarenta menos tres son treinta y siete.")],
    selfcheck=[ex("¿Qué se pone en una tabla de comparación?", "Datos", "Se ordenan los datos."), ex("Si dos animales no miden lo mismo, ¿eso es una semejanza o una diferencia?", "Una diferencia", "El tamaño cambia entre los dos."), ex("¿Cuál es una planta: la araucaria o el pudú?", "La araucaria", "El pudú es un animal.")],
    open_task=task("Completa esta tabla de comparación con los datos y escribe una semejanza y una diferencia. Guanaco: unos 110 cm, pelo, camina, cordillera. Cóndor: alas de unos 3 m, plumas, vuela, cordillera.", "Semejanza: los dos viven en la cordillera. Diferencia: el guanaco camina y tiene pelo; el cóndor vuela y tiene plumas.", ["completa la tabla", "escribe una semejanza con dato", "escribe una diferencia con dato"], ["tabla", "dos frases"], ["escribir opiniones", "dar solo diferencias"], "Reconoce la semejanza y pide un segundo dato de diferencia."),
    reinforce="Compara dos plantas de un parque con una tabla de dos columnas.",
    extend="Compara tres seres vivos y busca una semejanza que tengan los tres.",
)

register(
    OA5, 3,
    materials="Este cuaderno con tarjetas de cuatro amenazas (basura, incendios, tala de árboles y mascotas sueltas) y de lo que necesitan los seres vivos, lápiz y colores.",
    use="Aprenderé qué necesitan las plantas y animales de Chile y qué los pone en peligro. Sirve para decidir cómo cuidarlos.",
    prior=["Sé que cada ser vivo necesita agua, alimento y aire.", "Sé que el hábitat les da lo que necesitan."],
    explain=[
        "Las plantas y los animales de Chile necesitan su hábitat limpio, agua, alimento y refugio. Si el hábitat cambia mucho, algunos seres vivos quedan en peligro. Un ser vivo está en peligro cuando quedan pocos y puede desaparecer.",
        "Hay amenazas, que son cosas que hacen daño. La basura puede enfermar a los animales. Los incendios queman bosques y refugios. La tala de árboles saca el hogar de aves y pequeños animales. Las mascotas sueltas pueden asustar o cazar animales silvestres.",
        "Los niños también pueden ayudar. Puedes botar la basura en su lugar, no arrancar plantas, no hacer fuego y no molestar a los animales silvestres. Estas medidas se llaman medidas de cuidado.",
    ],
    vocab=[("amenaza", "cosa que hace daño a un ser vivo"), ("en peligro", "quedan pocos y podrían desaparecer"), ("medida de cuidado", "acción que protege a un ser vivo"), ("tala", "cortar árboles"), ("silvestre", "que vive libre en la naturaleza")],
    worked=[
        {"title": "Unir amenaza y daño", "problem": "Basura en un sendero. ¿A qué animal puede hacer daño y cómo?", "steps": ["Un animal puede comer un plástico.", "El plástico no se digiere.", "Se enferma."], "answer": "Puede enfermar a un animal que lo come"},
        {"title": "Elegir una medida de cuidado", "problem": "Una familia hace un picnic en el bosque y le sobra basura. ¿Qué medida de cuidado sirve?", "steps": ["Si la deja, hace daño.", "Si la guarda en una bolsa, no hace daño.", "La lleva a un basurero."], "answer": "Llevarse la basura en una bolsa y botarla en el basurero"},
    ],
    mistakes=[
        {"wrong": "Pensar que cuidar es llevarse un animal silvestre a la casa.", "why": "Se confunde cuidar con tener.", "fix": "Cuidar es dejarlo en su hábitat y proteger el lugar."},
        {"wrong": "Pensar que una planta pequeña da lo mismo si la arrancan.", "why": "No se ve que cada planta es parte del hábitat.", "fix": "No arranques plantas; sirven de alimento y refugio."},
    ],
    tiers={
        "recovery": [
            ex("¿Es la basura en el bosque una amenaza o una medida de cuidado?", "Una amenaza", "Hace daño a animales y plantas."),
            ex("¿Es llevar la basura a un basurero una amenaza o una medida de cuidado?", "Una medida de cuidado", "Protege el hábitat."),
            ex("¿Un ser vivo en peligro tiene muchos o pocos individuos?", "Pocos", "Quedan pocos y podría desaparecer."),
        ],
        "understand": [
            ex("¿Qué es una amenaza para un ser vivo?", "Algo que le hace daño", "Pone en riesgo su vida."),
            ex("¿Qué hacen los incendios con los refugios?", "Los queman", "Destruyen el hogar de los animales."),
            ex("¿Qué es una medida de cuidado?", "Una acción que protege a un ser vivo", "Evita que se dañe."),
        ],
        "apply": [
            ex("Tarjetas: basura, incendio, tala, mascota suelta. ¿Cuántas amenazas hay?", "4", "Las cuatro hacen daño."),
            ex("Un niño ve una flor y quiere arrancarla. ¿Qué medida de cuidado puede usar?", "Mirarla y dejarla en su lugar", "Así no se le hace daño."),
            arith("En un sendero ves 3 envases tirados y, con un adulto, recoges 2. ¿Cuántos envases quedan por recoger?", "3-2", "Se restan los que ya recogiste.", " envase"),
        ],
        "reason": [
            ex("Sofía dice que un fuego pequeño en el bosque no es peligroso. ¿Qué respondes con una razón?", "Es peligroso porque el fuego puede crecer y quemar el hogar de los animales", "El fuego se propaga rápido."),
            ex("¿Por qué una mascota suelta puede hacer daño a un animal silvestre?", "Porque lo puede asustar o cazar", "Los silvestres no están acostumbrados a ellas."),
        ],
        "challenge": [
            ex("Escribe una amenaza para el cóndor y una medida de cuidado.", "Por ejemplo basura; no tirar basura", "La medida evita el daño."),
            ex("Hay 4 medidas de cuidado en un afiche y 2 amenazas. ¿Cuántas cosas hay en el afiche?", "6", "Cuatro más dos son seis."),
        ],
    },
    context=[ex("En un paseo, un grupo de 3 niños recoge 2 bolsas de basura cada uno en un sendero, con un adulto. ¿Cuántas bolsas recogen entre todos?", "6", "Dos más dos más dos son seis bolsas.")],
    selfcheck=[ex("¿Qué es una amenaza?", "Algo que hace daño", "Pone en riesgo."), ex("¿Se debe arrancar una planta silvestre?", "No", "Sirve de alimento y refugio."), ex("¿Qué puede hacer el fuego en un bosque?", "Quemar el hogar de los animales", "Destruye sus refugios.")],
    open_task=task("Mira la situación: una familia va a un cerro con perro, comida y fósforos. Escribe tres cosas que pueden hacer daño al lugar y tres medidas de cuidado. Dibuja una.", "Daños: dejar basura, soltar al perro, hacer fuego. Medidas: llevarse la basura, mantener al perro con correa, no hacer fuego.", ["escribe tres amenazas", "escribe tres medidas", "une cada medida con su amenaza"], ["tabla de dos columnas", "dibujo"], ["escribir medidas que no cuidan", "no unir cada una"], "Reconoce las medidas y pide unir cada una con su amenaza."),
    reinforce="Con un adulto, recoge y bota en su lugar tres papeles que veas en el suelo. No toques vidrios ni nada que pinche.",
    extend="Explica por qué un ser vivo en peligro necesita que se cuide su hábitat.",
)

register(
    OA5, 4,
    materials="Este cuaderno con tres lugares de Chile (un humedal, un bosque y una cordillera) y sus datos, una pauta para un plan de cuidado, lápiz y colores.",
    use="Aprenderé a armar un plan de cuidado con acciones claras. Sirve para proteger plantas y animales de un lugar.",
    prior=["Sé qué es una amenaza y una medida de cuidado.", "Sé comparar plantas y animales."],
    explain=[
        "Un plan de cuidado dice qué se va a hacer, quién lo hace y cuándo. Por ejemplo: «Poner un basurero. Lo ponen los vecinos. Se limpia cada viernes». Así la idea se puede cumplir.",
        "Elige un lugar y mira qué lo amenaza. Si el lugar es un humedal con aves, la basura y el ruido las asustan. Si es un bosque, el fuego es el mayor riesgo. Si es una cordillera, el pisoteo puede dañar las plantas pequeñas.",
        "Un buen plan tiene medidas simples: botar la basura en su lugar, no hacer fuego, no arrancar plantas, no molestar a los animales y avisar a un adulto si ves un daño. Después se revisa si ayudó.",
    ],
    vocab=[("plan", "lista de acciones para lograr algo"), ("humedal", "lugar con agua poco profunda donde viven aves"), ("pisoteo", "dañar plantas al pisarlas"), ("quién", "persona que hace la acción"), ("cuándo", "momento en que se hace la acción")],
    worked=[
        {"title": "Armar un plan simple", "problem": "Una laguna con patos y basura en la orilla. Arma un plan con qué, quién y cuándo.", "steps": ["Qué: recoger la basura.", "Quién: los niños con un adulto.", "Cuándo: cada sábado."], "answer": "Recoger la basura, con un adulto, cada sábado"},
        {"title": "Revisar si el plan sirve", "problem": "Antes había 10 envases por semana. Con el plan hay 3. ¿Funcionó?", "steps": ["10 menos 3 son 7.", "Hay 7 envases menos."], "answer": "Sí, hay 7 envases menos por semana"},
    ],
    mistakes=[
        {"wrong": "Escribir un plan sin decir quién lo hace.", "why": "Se piensa que se hará solo.", "fix": "Escribe quién y cuándo."},
        {"wrong": "Proponer medidas que no se pueden cumplir, como «sacar todos los autos».", "why": "No se piensa en lo que se puede hacer.", "fix": "Elige acciones pequeñas que tú puedes hacer."},
    ],
    tiers={
        "recovery": [
            ex("En un plan, ¿qué dice la palabra «quién»?", "Quién hace la acción", "Nombra a la persona."),
            ex("En un plan, ¿qué dice la palabra «cuándo»?", "En qué momento se hace", "Indica el tiempo."),
            ex("¿Es «botar la basura en su lugar» una medida simple de cuidado?", "Sí", "Se puede hacer cada día."),
        ],
        "understand": [
            ex("¿Qué es un plan de cuidado?", "Una lista de acciones para proteger un lugar", "Dice qué, quién y cuándo."),
            ex("¿Por qué un plan debe ser posible de cumplir?", "Para que las acciones se hagan de verdad", "Una idea imposible no ayuda."),
            ex("¿Para qué se revisa un plan después?", "Para ver si ayudó", "Se compara antes y después."),
        ],
        "apply": [
            arith("Antes del plan había 12 envases por semana. Después, 4. ¿Cuántos envases menos hay?", "12-4", "Se resta lo que queda a lo que había.", " envases"),
            ex("Lugar: bosque. Amenaza: fuego. ¿Qué medida eliges: no hacer fuego o plantar flores?", "No hacer fuego", "Evita el daño del fuego."),
            ex("Completa: Qué: poner un basurero. Quién: los vecinos. Cuándo: ¿?. Escribe un momento posible.", "Por ejemplo cada viernes", "Un momento regular que se pueda cumplir."),
        ],
        "reason": [
            ex("Un plan dice «Cuidar el lugar». ¿Qué falta para que sea un plan?", "Decir qué, quién y cuándo", "Una acción concreta se puede cumplir."),
            ex("Después del plan, la basura bajó de 12 a 4 envases. Ana dice «no sirvió». ¿Qué respondes con datos?", "Sí sirvió: hay 8 envases menos", "Doce menos cuatro son ocho."),
        ],
        "challenge": [
            ex("Escribe un plan de tres acciones para una plaza con palomas.", "Por ejemplo botar basura, no asustar a las palomas y avisar si ves un daño", "Son acciones posibles."),
            ex("En un plan hay 3 acciones de los niños y 2 de los adultos. ¿Cuántas acciones tiene el plan?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("Un humedal tiene 15 patos y los niños quieren que no los asusten. Si pegan 3 carteles en un sendero y 3 en otro, ¿cuántos carteles pegan?", "6", "Tres más tres son seis carteles.")],
    selfcheck=[ex("¿Qué tres preguntas responde un plan?", "Qué, quién y cuándo", "Son las tres partes."), ex("¿Se puede cuidar un lugar sin hacer nada?", "No", "Hay que actuar."), ex("¿Qué se hace al revisar un plan?", "Ver si ayudó", "Se compara antes y después.")],
    open_task=task("Elige uno de estos lugares y arma un plan de tres acciones con qué, quién y cuándo: A) un humedal con aves y basura; B) un bosque con riesgo de fuego; C) una cordillera con plantas pisadas. Dibuja el lugar con un cartel de cuidado.", "Lugar A. Qué: recoger basura. Quién: niños con un adulto. Cuándo: cada sábado. Qué: pegar un cartel. Quién: el curso. Cuándo: este mes. Qué: no gritar. Quién: todos. Cuándo: siempre.", ["elige un lugar", "escribe tres acciones", "dice qué, quién y cuándo"], ["plan de tres filas", "dibujo con cartel"], ["acciones imposibles", "olvidar quién o cuándo"], "Reconoce el plan y pide completar quién y cuándo en cada acción."),
    reinforce="Haz un cartel con un mensaje de cuidado para tu calle.",
    extend="Imagina cómo medirías si tu plan sirvió después de un mes.",
)

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Este cuaderno con una tabla de cinco sentidos (órgano y qué percibe), lápiz y colores.",
    use="Aprenderé qué son los cinco sentidos y dónde están los órganos que los usan. Sirve para entender cómo conocemos lo que nos rodea.",
    prior=["Sé nombrar partes del cuerpo como ojos, orejas y nariz.", "Sé que mi cuerpo siente."],
    explain=[
        "Tienes cinco sentidos. Con los ojos ves: es la vista. Con las orejas oyes: es el oído. Con la nariz hueles: es el olfato. Con la lengua pruebas: es el gusto. Con la piel sientes: es el tacto.",
        "Cada sentido tiene un órgano, que es una parte del cuerpo que hace un trabajo. Los ojos, las orejas, la nariz, la lengua y la piel están en lugares distintos del cuerpo. La piel está en todo el cuerpo.",
        "Los sentidos mandan información al cerebro. Así sabes si algo está caliente, si suena fuerte o si huele rico. Usar los sentidos es una forma de observar.",
    ],
    vocab=[("vista", "sentido que usa los ojos para ver"), ("oído", "sentido que usa las orejas para oír"), ("olfato", "sentido que usa la nariz para oler"), ("gusto", "sentido que usa la lengua para probar"), ("tacto", "sentido que usa la piel para sentir")],
    worked=[
        {"title": "Unir sentido y órgano", "problem": "Unir: ver, oír, oler, probar, sentir. Órganos: ojos, orejas, nariz, lengua, piel.", "steps": ["Ver: ojos.", "Oír: orejas.", "Oler: nariz.", "Probar: lengua.", "Sentir: piel."], "answer": "Ver-ojos, oír-orejas, oler-nariz, probar-lengua, sentir-piel"},
        {"title": "Elegir el sentido", "problem": "Sientes que la taza está caliente. ¿Qué sentido usas?", "steps": ["Tocas la taza.", "La piel de la mano siente el calor."], "answer": "El tacto"},
    ],
    mistakes=[
        {"wrong": "Decir que el sentido del tacto está solo en las manos.", "why": "Se piensa que sentir es solo tocar con los dedos.", "fix": "La piel de todo el cuerpo siente."},
        {"wrong": "Confundir oído con orejas.", "why": "Se mezcla el sentido con el órgano.", "fix": "El oído es el sentido y las orejas son el órgano que se usa."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué órgano usas para ver?", "Los ojos", "Con ellos ves."),
            ex("¿Qué órgano usas para oír?", "Las orejas", "Con ellas oyes."),
            ex("¿Qué órgano usas para oler?", "La nariz", "Con ella hueles."),
        ],
        "understand": [
            ex("¿Cuántos sentidos tienes?", "Cinco", "Vista, oído, olfato, gusto y tacto."),
            ex("¿Qué es un órgano?", "Una parte del cuerpo que hace un trabajo", "Cada sentido tiene uno."),
            ex("¿Dónde está el órgano del tacto?", "En la piel de todo el cuerpo", "La piel cubre el cuerpo entero."),
        ],
        "apply": [
            ex("Pruebas una naranja y es ácida. ¿Qué sentido usas?", "El gusto", "La lengua prueba el sabor."),
            ex("Suena una campana. ¿Qué sentido usas?", "El oído", "Las orejas oyen los sonidos."),
            ex("Hueles pan recién hecho. ¿Qué sentido usas?", "El olfato", "La nariz huele."),
        ],
        "reason": [
            ex("Bruno dice que ve los sonidos. ¿Qué sentido usa para un sonido y cuál no?", "Usa el oído, no la vista", "Los sonidos se oyen."),
            ex("Si te vendas los ojos, ¿qué sentidos siguen funcionando?", "Oído, olfato, gusto y tacto", "Solo la vista queda tapada."),
        ],
        "challenge": [
            ex("Escribe una cosa que puedes sentir con la piel y una que puedes oír.", "Por ejemplo el viento y una campana", "Cada una usa un sentido."),
            ex("Cuentas 5 sentidos y 5 órganos distintos. ¿Cuántas cosas son entre sentidos y órganos?", "10", "Cinco más cinco son diez."),
        ],
    },
    context=[ex("En la cocina hueles las galletas, tocas el plato tibio, ves el color dorado y oyes el horno. ¿Cuántos sentidos usaste?", "4", "Olfato, tacto, vista y oído.")],
    selfcheck=[ex("¿Qué sentido usa los ojos?", "La vista", "Con los ojos se ve."), ex("¿Qué sentido usa la lengua?", "El gusto", "Con la lengua se prueba."), ex("¿Qué sentido usa la piel?", "El tacto", "Con la piel se siente.")],
    open_task=task("Mira estas cinco situaciones y escribe qué sentido usas: 1) oyes un perro ladrar; 2) hueles una flor; 3) ves un arcoíris; 4) sientes el agua fría de la llave; 5) pruebas un trozo de pan. Dibuja el órgano de dos.", "1 oído, 2 olfato, 3 vista, 4 tacto, 5 gusto. Dibujo: una oreja y un ojo.", ["une cada situación con su sentido", "nombra el órgano de dos", "dibuja dos órganos"], ["lista", "dibujos"], ["confundir olfato con gusto", "olvidar el tacto"], "Reconoce los cinco sentidos y pide nombrar el órgano."),
    reinforce="Cierra los ojos y nombra tres sonidos que oyes en tu casa.",
    extend="Explica qué sentido te ayuda más cuando cruzas una calle.",
)

register(
    OA6, 2,
    materials="Este cuaderno con una tabla de seis objetos de la casa y cinco preguntas sobre qué sentido sirve, lápiz y colores. En casa: una venda o un pañuelo y objetos seguros como una cuchara, un algodón y una manzana.",
    use="Aprenderé qué información da cada sentido: colores, sonidos, olores, sabores y cómo se sienten las cosas. Sirve para describir objetos con palabras exactas.",
    prior=["Sé nombrar los cinco sentidos.", "Sé que cada sentido tiene un órgano."],
    explain=[
        "Cada sentido nos da información distinta. La vista nos dice colores, formas y tamaños. El oído nos dice si un sonido es fuerte o suave. El olfato nos dice olores como dulce o fuerte.",
        "El gusto nos dice si algo es dulce, salado, ácido o amargo. El tacto nos dice si algo es liso o áspero, frío o caliente, blando o duro. Para describir bien un objeto usamos varios sentidos.",
        "Un juego sirve para practicar: con los ojos vendados, un amigo te da una cuchara, un algodón o una manzana. Con el tacto dices si es liso, blando o duro. Por seguridad, nunca pruebes algo sin que un adulto lo sepa.",
    ],
    vocab=[("áspero", "que no es liso al tocarlo"), ("liso", "que es parejo al tocarlo"), ("fuerte", "que suena muy alto o huele mucho"), ("dulce", "sabor como el azúcar"), ("ácido", "sabor como el limón")],
    worked=[
        {"title": "Sentido e información", "problem": "El limón es amarillo, huele fuerte y sabe ácido. ¿Qué información da cada sentido?", "steps": ["Vista: amarillo.", "Olfato: huele fuerte.", "Gusto: ácido."], "answer": "Vista amarillo, olfato fuerte y gusto ácido"},
        {"title": "Usar el tacto", "problem": "Con los ojos vendados tocas un algodón, una cuchara y una piedra. El algodón es blando, la cuchara fría y la piedra dura. ¿Qué sentido usaste y qué información diste?", "steps": ["Usaste el tacto.", "Dijiste blando, frío y duro."], "answer": "El tacto; blando, frío y duro"},
    ],
    mistakes=[
        {"wrong": "Decir «huele rico» sin explicar cómo es el olor.", "why": "Se usa una palabra muy general.", "fix": "Di si es dulce, fuerte o suave."},
        {"wrong": "Probar objetos desconocidos para saber cómo son.", "why": "Se piensa que probar siempre es seguro.", "fix": "Solo prueba alimentos que un adulto te dio."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué información da la vista: colores o sabores?", "Colores", "Los ojos ven colores."),
            ex("¿Qué información da el gusto: dulce o liso?", "Dulce", "El sabor lo da el gusto."),
            ex("¿Qué información da el tacto: áspero o amarillo?", "Áspero", "La textura la da el tacto."),
        ],
        "understand": [
            ex("¿Qué sabores conoces según esta clase?", "Dulce, salado, ácido y amargo", "Son los cuatro sabores de la clase."),
            ex("¿Qué sentido te dice si un sonido es fuerte o suave?", "El oído", "Las orejas oyen sonidos."),
            ex("¿Por qué conviene usar varios sentidos para describir un objeto?", "Porque cada sentido da información distinta", "Con varios se describe mejor."),
        ],
        "apply": [
            ex("Un algodón se siente blando y suave. ¿Qué sentido te lo dice?", "El tacto", "La piel siente la textura."),
            ex("Una manzana es roja, cruje y sabe dulce. ¿Cuántos sentidos usaste?", "3", "Vista, oído y gusto."),
            arith("Pruebas 4 alimentos dulces y 3 ácidos que un adulto te dio. ¿Cuántos alimentos probaste?", "4+3", "Se suman los alimentos.", " alimentos"),
        ],
        "reason": [
            ex("Lila dice que sabe si una sopa está caliente con el gusto. ¿Con qué sentido se nota primero el calor?", "Con el tacto", "La piel siente el calor; por eso conviene acercar la mano al plato antes de probar."),
            ex("Si tienes la nariz tapada, ¿qué sentido se te hace más difícil?", "El olfato", "No pasa el olor."),
        ],
        "challenge": [
            ex("Escribe tres palabras para describir una piedra con el tacto.", "Por ejemplo dura, áspera y fría", "Son datos del tacto."),
            ex("Una caja tiene 3 objetos blandos y 2 duros. ¿Cuántos objetos hay?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("En la feria hueles frutillas, ves su color rojo y las tocas con la mano. ¿Qué tres sentidos usaste?", "Olfato, vista y tacto", "Oler, ver y tocar.")],
    selfcheck=[ex("¿Qué sabores conoces?", "Dulce, salado, ácido y amargo", "Son los de la clase."), ex("¿Qué sentido dice si algo es liso o áspero?", "El tacto", "La textura se siente con la piel."), ex("¿Se debe probar un objeto desconocido?", "No", "Puede ser peligroso.")],
    open_task=task("Describe con tres sentidos esta lista de objetos: un limón, un algodón y una campana. Para el limón usa vista, olfato y gusto; para el algodón tacto; para la campana oído. Escribe una palabra por sentido y nombra el órgano.", "Limón: vista amarillo (ojos), olfato fuerte (nariz), gusto ácido (lengua). Algodón: tacto blando (piel). Campana: oído sonido fuerte (orejas).", ["usa una palabra por sentido", "nombra el órgano", "respeta la lista"], ["tabla", "dibujo"], ["usar una palabra general como «lindo»", "proponer probar objetos desconocidos"], "Reconoce la información de cada sentido y pide una palabra más específica."),
    reinforce="Con los ojos tapados, toca tres objetos seguros de tu casa y di cómo son.",
    extend="Explica por qué la sopa hirviendo se debe probar con cuidado.",
)

register(
    OA6, 3,
    materials="Este cuaderno con la tabla de un experimento (comer con la nariz tapada, datos de ejemplo), lápiz y colores. En casa: trozos pequeños de manzana y pera, y un adulto que ayude. Si alguien es alérgico a una fruta, no la pruebes. Come sentado.",
    use="Aprenderé que los sentidos trabajan juntos. Sirve para entender por qué la comida sabe distinto cuando estás resfriado.",
    prior=["Sé qué información da cada sentido.", "Sé leer una tabla con números."],
    explain=[
        "Los sentidos no trabajan solos. Cuando comes una manzana, la ves, la hueles, la tocas, oyes el crujido y la pruebas. El cerebro junta toda la información y te dice que es una manzana.",
        "Si un sentido falla, los otros ayudan. Cuando tienes la nariz tapada por un resfrío, la comida parece tener menos sabor porque el olfato no ayuda al gusto. En el experimento de hoy, 6 niños probaron un trozo de manzana o de pera con la nariz tapada y con la nariz destapada.",
        "Datos de ejemplo: con la nariz destapada, los 6 niños dijeron bien cuál era; con la nariz tapada, solo 2 de 6 acertaron. La diferencia nos muestra que el olfato ayuda al gusto.",
    ],
    vocab=[("experimento", "prueba que se hace para aprender algo"), ("destapada", "sin nada que impida el paso del aire"), ("acertar", "decir la respuesta correcta"), ("cerebro", "órgano que junta la información de los sentidos"), ("resfrío", "enfermedad que tapa la nariz")],
    worked=[
        {"title": "Leer los datos", "problem": "Con la nariz destapada acertaron 6 de 6 niños. Con la nariz tapada acertaron 2 de 6. ¿En cuál situación acertaron más?", "steps": ["Comparo 6 con 2.", "6 es mayor que 2.", "Acertaron más con la nariz destapada."], "answer": "Con la nariz destapada acertaron más; 4 niños más"},
        {"title": "Explicar el resultado", "problem": "¿Por qué les costó más cuando la nariz estaba tapada?", "steps": ["El olfato no recibió olor.", "El gusto no tuvo ayuda.", "Costó reconocer el sabor."], "answer": "Porque el olfato ayuda al gusto"},
    ],
    mistakes=[
        {"wrong": "Decir que el gusto trabaja solo.", "why": "No se ve que el olor ayuda al sabor.", "fix": "Piensa que el olfato y el gusto trabajan juntos."},
        {"wrong": "Sacar una conclusión con una sola persona.", "why": "Un solo caso puede ser casualidad.", "fix": "Mira los datos de varias personas, como los 6 niños."},
    ],
    tiers={
        "recovery": [
            ex("Con la nariz destapada acertaron 6 niños. ¿Todos o algunos?", "Todos", "Eran 6 niños."),
            arith("Con la nariz tapada acertaron 2 niños de 6. ¿Cuántos no acertaron?", "6-2", "Se resta los que acertaron del total.", " niños"),
            ex("¿Qué órgano junta la información de los sentidos?", "El cerebro", "Él decide qué es lo que sentimos."),
        ],
        "understand": [
            ex("¿Por qué la comida sabe menos con un resfrío?", "Porque el olfato no ayuda al gusto", "La nariz está tapada."),
            ex("¿Qué sentidos usas al comer una manzana que cruje?", "Vista, olfato, tacto, oído y gusto", "Todos los sentidos participan."),
            ex("¿Para qué sirve un experimento?", "Para aprender algo con una prueba", "Se comparan resultados."),
        ],
        "apply": [
            arith("Con la nariz destapada acertaron 6 y con la nariz tapada acertaron 2. ¿Cuántos más acertaron con la nariz destapada?", "6-2", "Se resta lo menor a lo mayor.", " niños"),
            ex("En otro grupo: nariz destapada 5 de 5 y nariz tapada 1 de 5. ¿El resultado es parecido al primero?", "Sí", "También acertaron más con la nariz destapada."),
            arith("Prueban una manzana 4 niños y una pera 3 niños. ¿Cuántos niños probaron en total?", "4+3", "Se suman los niños de cada fruta.", " niños"),
        ],
        "reason": [
            ex("Si un solo niño acertó con la nariz tapada, ¿se puede decir que el olfato no importa?", "No", "Un solo caso no alcanza; los datos del grupo muestran que acertaron menos."),
            ex("¿Qué conclusión sale de los datos 6 de 6 y 2 de 6?", "El olfato ayuda al gusto", "Con nariz tapada acertaron menos."),
        ],
        "challenge": [
            ex("Escribe otro caso en que dos sentidos trabajan juntos.", "Por ejemplo vista y oído al ver una tormenta", "El rayo se ve y el trueno se oye."),
            ex("En una mesa hay 2 niños con la nariz tapada y 3 con la nariz destapada. ¿Cuántos niños hay?", "5", "Dos más tres son cinco."),
        ],
    },
    context=[ex("Marta está resfriada y su sopa le parece sin sabor. Su papá, que no está resfriado, dice que está rica. ¿Qué sentido ayuda a su papá?", "El olfato", "Con la nariz libre siente el olor de la sopa.")],
    selfcheck=[ex("¿Los sentidos trabajan solos o juntos?", "Juntos", "El cerebro junta la información."), ex("¿Qué sentido ayuda al gusto?", "El olfato", "El olor ayuda a reconocer sabores."), ex("¿Cuántos niños acertaron con la nariz destapada?", "6", "Acertaron todos los niños.")],
    open_task=task("Con estos datos de otro grupo escribe una conclusión: 5 niños probaron la misma fruta, una pera, dos veces: con la nariz destapada acertaron 5 y con la nariz tapada acertaron 1 (datos de ejemplo). Cita los números y explica por qué.", "Con la nariz destapada acertaron 5 de 5 y con la nariz tapada solo 1 de 5. El olfato ayuda al gusto.", ["cita los dos números", "compara", "explica con el olfato"], ["frase con números", "dibujo"], ["no usar los números", "concluir sin comparar"], "Reconoce la comparación y pide citar los dos números."),
    reinforce="Con ayuda de un adulto, pruébense dos alimentos con la nariz tapada y destapada.",
    extend="Explica por qué se come mejor cuando el plato huele rico.",
)

register(
    OA6, 4,
    materials="Este cuaderno con seis situaciones de riesgo para los sentidos y cinco medidas de protección, lápiz y colores.",
    use="Aprenderé a proteger mis sentidos y a evitar riesgos al explorar. Sirve para cuidar mis ojos, oídos, nariz, lengua y piel.",
    prior=["Sé qué información da cada sentido.", "Sé que los sentidos trabajan juntos."],
    explain=[
        "Los sentidos se pueden dañar. Mirar directo al Sol daña los ojos. Un ruido muy fuerte o un volumen muy alto daña los oídos. Meter objetos pequeños en las orejas o la nariz es peligroso. Tocar algo muy caliente quema la piel.",
        "Hay medidas de protección. Usa sombrero, lentes de sol y protector solar cuando haya mucha luz. Baja el volumen de los audífonos. No te metas nada en las orejas ni en la nariz. Lava tus manos antes de tocarte los ojos. Pide ayuda a un adulto con ollas y estufas.",
        "Antes de explorar algo desconocido, pregunta a un adulto. No pruebes plantas, productos de limpieza ni medicamentos. Ante una situación de riesgo, aléjate y avisa a un adulto.",
    ],
    vocab=[("riesgo", "posibilidad de que algo haga daño"), ("protección", "cuidado para evitar un daño"), ("volumen", "qué tan fuerte suena"), ("quemadura", "daño en la piel por algo muy caliente"), ("avisar", "decir a un adulto lo que pasa")],
    worked=[
        {"title": "Unir riesgo y medida", "problem": "Riesgo: hay mucho Sol a mediodía. ¿Qué medida de protección eliges?", "steps": ["El Sol fuerte daña los ojos y la piel.", "Un sombrero y lentes de sol protegen."], "answer": "Usar sombrero y lentes de sol, y no mirar el Sol"},
        {"title": "Decidir qué hacer", "problem": "Ves a tu hermano menor con una cuenta pequeña cerca de su nariz. ¿Qué haces?", "steps": ["Es un riesgo.", "No intentes sacarla tú.", "Avisa a un adulto de inmediato."], "answer": "Avisar a un adulto"},
    ],
    mistakes=[
        {"wrong": "Pensar que si no duele, no hace daño.", "why": "Algunos daños ocurren poco a poco.", "fix": "Cuida tus oídos y ojos aunque no duela."},
        {"wrong": "Probar algo para saber qué es.", "why": "Se piensa que probar siempre es seguro.", "fix": "No pruebes nada desconocido; pregunta a un adulto."},
    ],
    tiers={
        "recovery": [
            ex("¿Se puede mirar directo al Sol?", "No", "Daña los ojos."),
            ex("¿Es buena idea bajar el volumen de los audífonos?", "Sí", "Protege los oídos."),
            ex("¿Es seguro meterse un objeto pequeño en la oreja?", "No", "Puede dañar el oído."),
        ],
        "understand": [
            ex("¿Qué es un riesgo?", "La posibilidad de que algo haga daño", "Hay que evitarlo."),
            ex("¿Qué dos cosas protegen los ojos del Sol?", "Sombrero y lentes de sol", "Dan sombra y filtran la luz."),
            ex("¿Qué haces ante un riesgo que no puedes resolver?", "Aviso a un adulto", "Un adulto sabe cómo actuar."),
        ],
        "apply": [
            ex("Riesgo: un volumen muy alto. ¿Qué sentido se daña?", "El oído", "Se dañan las orejas."),
            ex("Riesgo: una olla caliente. ¿Qué sentido se daña?", "El tacto", "La piel se quema."),
            arith("En un paseo hay 3 niños con sombrero y 2 sin sombrero. ¿Cuántos niños hay?", "3+2", "Se suman los niños con y sin sombrero.", " niños"),
        ],
        "reason": [
            ex("Pablo dice que puede probar una flor del jardín para saber a qué sabe. ¿Qué le dices y por qué?", "Que no, porque podría hacerle daño", "Una planta desconocida puede ser peligrosa."),
            ex("Ana usa audífonos con el volumen al máximo porque le gusta. ¿Qué riesgo corre?", "Dañarse los oídos", "El ruido fuerte los daña."),
        ],
        "challenge": [
            ex("Escribe una medida de protección para cada sentido: vista, oído y tacto.", "Por ejemplo lentes de sol, bajar el volumen y no tocar algo caliente y pedir ayuda a un adulto", "Cada una evita un daño."),
            ex("Una familia tiene 4 pares de lentes de sol y 3 sombreros. ¿Cuántos objetos de protección hay?", "7", "Cuatro más tres son siete."),
        ],
    },
    context=[ex("Un niño se queda 2 horas en la playa al mediodía sin sombrero ni lentes. ¿Qué dos partes del cuerpo hay que proteger del Sol?", "Los ojos y la piel", "El Sol daña ojos y piel.")],
    selfcheck=[ex("¿Qué se usa para proteger los ojos del Sol?", "Lentes de sol", "Filtran la luz."), ex("¿Qué haces ante un riesgo?", "Aviso a un adulto", "Es la primera medida."), ex("¿Qué órgano se daña con ruidos muy fuertes?", "Las orejas", "Allí está el oído.")],
    open_task=task("Mira estas tres situaciones y escribe el riesgo, el sentido que se podría dañar y una medida de protección. 1) Un niño mira un eclipse sin protección. 2) Un grupo escucha música con el volumen al máximo. 3) Una niña toca una plancha encendida.", "1) Riesgo: daño en los ojos; sentido: vista; medida: no mirar el Sol. 2) Riesgo: daño en los oídos; oído; bajar el volumen. 3) Riesgo: quemadura; tacto; no tocarla y avisar a un adulto.", ["nombra el riesgo", "nombra el sentido", "propone una medida"], ["tabla de tres filas", "dibujo"], ["no nombrar el sentido", "medidas poco seguras"], "Reconoce el riesgo y pide una medida clara para cada situación."),
    reinforce="Haz un cartel con una regla para cuidar tus ojos.",
    extend="Explica por qué se debe avisar a un adulto cuando hay un riesgo.",
)

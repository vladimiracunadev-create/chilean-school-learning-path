"""Cuaderno del estudiante, 2.º básico Historia, Geografía y Ciencias Sociales: OA 09 (patrimonio natural) y OA 10 (pueblos originarios en el mapa)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA9, OA10 = "HI02 OA 09", "HI02 OA 10"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Este cuaderno y un lápiz. Todos los casos están escritos en los ejercicios.",
    use="Aprenderé por qué algunos lugares, plantas y animales de la naturaleza son un patrimonio natural. Sirve para entender por qué la gente los cuida.",
    prior=["Sé que hay paisajes, plantas y animales en mi país.", "Sé que cuidar es proteger algo para que no se dañe."],
    explain=[
        "El patrimonio natural son los lugares, las plantas y los animales de la naturaleza que una comunidad valora y quiere cuidar. Pueden ser un bosque, un lago, un desierto, una playa o un animal único. Se heredan de quienes vivieron antes y se dejan a quienes vienen después.",
        "No se elige solo porque algo sea bonito. También importa que dé agua, que sea hogar de animales que casi no quedan, que sea único en el mundo o que tenga valor para las personas que viven cerca. Un humedal puede verse simple, pero es hogar de muchas aves.",
        "El patrimonio natural necesita cuidado de las personas. La naturaleza existe sola, pero se puede dañar con basura, fuego o caza. Por eso hay normas, y por eso la gente ayuda: no tirar basura, no sacar plantas y avisar a un adulto si algo se daña.",
    ],
    vocab=[("patrimonio natural", "naturaleza valiosa que cuidamos para todos"), ("paisaje", "lo que se ve al mirar un lugar"), ("conservación", "cuidar algo para que no se pierda"), ("humedal", "lugar con agua poco profunda donde viven aves"), ("heredar", "recibir algo de quienes vivieron antes")],
    worked=[
        W("Elegir por varias razones", "El humedal de un pueblo no es muy bonito, pero allí duermen cientos de aves y el agua de lluvia se guarda en él. ¿Puede ser patrimonio natural?",
          ["Miro qué da el lugar: hogar para aves y agua guardada.", "No me quedo solo con lo bonito.", "Hay razones importantes para cuidarlo."], "Sí; da hogar a aves y guarda agua, aunque no sea muy bonito"),
        W("Qué es natural", "Un cartel dice: «Valle con cóndores y río limpio». Otro dice: «Plaza con fuente de cemento». ¿Cuál habla de patrimonio natural?",
          ["Natural es lo que existe en la naturaleza sin ser construido.", "Los cóndores y el río son naturales.", "La fuente de cemento la hicieron personas."], "El primer cartel"),
    ],
    mistakes=[
        M("Decir que un lugar es patrimonio solo porque es bonito.", "Se ignoran otras razones, como dar agua o ser hogar de animales.", "Piensa también en qué da el lugar y a quiénes sirve."),
        M("Creer que la naturaleza no necesita cuidado de las personas.", "Se olvida que la basura y el fuego la pueden dañar.", "Las personas ayudan con normas y buenos hábitos."),
    ],
    tiers=tiers(
        [ex("El patrimonio natural, ¿es naturaleza que cuidamos o una casa que se construyó?", "Naturaleza que cuidamos", "El patrimonio natural viene de la naturaleza, no de una construcción."),
         ex("¿Cuál es natural: un lago o un puente de fierro?", "Un lago", "El lago existe en la naturaleza; el puente lo construyeron personas."),
         ex("¿Para qué cuidamos el patrimonio natural: para que se pierda o para que siga existiendo?", "Para que siga existiendo", "Conservar es cuidar para que no se pierda.")],
        [ex("Di dos razones, distintas de ser bonito, para cuidar un humedal con aves.", "Da hogar a aves y guarda agua", "El texto explica que las aves viven allí y que el agua se guarda."),
         ex("¿Por qué se dice que el patrimonio natural se hereda?", "Porque lo recibimos de quienes vivieron antes y lo dejamos a quienes vienen", "Heredar es recibir y pasar a otros."),
         ex("Un bosque tiene árboles que casi no quedan. ¿Es buena razón para cuidarlo? Responde sí o no y explica.", "Sí; protege árboles que podrían perderse", "Cuidar sirve para que algo poco común no desaparezca.")],
        [ex("Lugar A: desierto con flores raras que solo crecen allí. Lugar B: terreno vacío con basura. ¿Cuál sería patrimonio natural?", "El lugar A", "Tiene flores únicas que vale la pena cuidar."),
         ex("Ana vio una laguna donde viven muchas aves. ¿Qué norma de cuidado le sugieres: no tirar basura o gritar fuerte?", "No tirar basura", "La basura puede dañar el agua y a las aves."),
         ex("Hay tres opciones: una playa con aves marinas, un estacionamiento y una tienda. ¿Cuál es naturaleza?", "La playa con aves marinas", "El estacionamiento y la tienda los construyeron personas.")],
        [ex("Tomás dijo: «Esta quebrada es fea, así que no vale cuidarla». Si da agua a muchos animales, ¿tiene razón?", "No; por ser útil para los animales vale cuidarla", "El valor no depende solo de la belleza."),
         ex("Sofía dijo: «La naturaleza no necesita a nadie». ¿Qué le responderías con un ejemplo?", "Necesita cuidado: la basura o el fuego pueden dañarla", "Las personas pueden dañar o proteger un lugar natural.")],
        [ex("Un pueblo debe elegir entre cuidar un humedal con aves y llenarlo de tierra para una cancha. Escribe una razón para cuidarlo.", "Es hogar de aves y guarda agua", "Se usa lo que el humedal da a la naturaleza y a las personas."),
         ex("De cóndor, carretera y río, ¿cuáles son naturaleza y cuál lo hicieron personas?", "Cóndor y río son naturaleza; la carretera la hicieron personas", "El cóndor y el río existen sin que alguien los construya; la carretera sí se construye.")],
    ),
    context=[ex("Un grupo de niños de una escuela cerca de un lago quiere cuidarlo. Piensan en recoger basura, no pisar el nido de aves y avisar a un adulto si ven fuego. ¿Eso cuida el patrimonio natural? Explica.", "Sí; protege a las aves y al lago", "Cada acción evita un daño al lago o a los animales.")],
    selfcheck=[ex("Escribe con tus palabras qué es el patrimonio natural.", "Naturaleza valiosa que cuidamos para todos", "Es naturaleza que valoramos y conservamos."), ex("Nombra un paisaje que sea patrimonio natural.", "Por ejemplo, un lago, un bosque o un desierto", "Cualquier paisaje natural valorado sirve."), ex("¿Se elige patrimonio solo por belleza? Responde sí o no.", "No", "También importan el agua, los animales y las personas.")],
    open_task=task("Elige uno de estos lugares: humedal con aves, bosque de árboles antiguos o playa con lobos marinos. Dibújalo y escribe dos razones para cuidarlo y una acción tuya para ayudar. Ejemplo de acción: no dejar basura.", "Dibujé un humedal con aves. Hay que cuidarlo porque es hogar de aves y guarda agua. Yo no dejaré basura.", ["elige un lugar de la lista", "da dos razones distintas de la belleza", "escribe una acción concreta"], ["dibujo", "dos razones", "una acción"], ["decir solo «es lindo»", "no escribir ninguna acción"], "Lee tus razones a un adulto y pide que te diga cuál es la más fuerte."),
    reinforce="Mira por la ventana o recuerda un paseo y nombra algo natural de ese lugar.",
    extend="Escribe una norma sencilla para cuidar un lugar natural que conozcas.",
)

register(
    OA9, 2,
    materials="Este cuaderno y un lápiz. Las fichas de especies están escritas en los ejercicios.",
    use="Aprenderé a relacionar plantas y animales de Chile con el ambiente donde viven. Sirve para entender por qué cada especie necesita su lugar.",
    prior=["Sé qué es patrimonio natural.", "Sé que las plantas y los animales viven en lugares distintos."],
    explain=[
        "La flora son las plantas de un lugar y la fauna son sus animales. Cada especie vive en un ambiente que le da alimento, agua y refugio. Si el ambiente se daña, la planta o el animal pierde su hogar.",
        "En Chile hay muchos ambientes. La araucaria crece en bosques de montaña del sur. El flamenco chileno vive en lagunas saladas del norte. El huemul habita montañas y bosques fríos del sur. El pingüino de Humboldt vive en costas e islas rocosas. El cóndor vuela en la cordillera de los Andes. El copihue crece en bosques húmedos del centro-sur.",
        "Cuando decimos que una especie es característica de un lugar, queremos decir que allí se la encuentra y que ayuda a reconocerlo. No usamos plantas o animales solo como adorno. Los miramos para entender cómo viven y qué necesitan para seguir allí.",
    ],
    vocab=[("flora", "las plantas de un lugar"), ("fauna", "los animales de un lugar"), ("ambiente", "el lugar con su agua, clima y alimento"), ("característica", "que ayuda a reconocer un lugar"), ("especie", "tipo de planta o animal")],
    worked=[
        W("Animal y ambiente", "Un ave rosada con patas largas come en una laguna salada del norte. ¿Qué especie es?",
          ["Pienso en el ambiente: laguna salada del norte.", "El ave que vive allí es el flamenco chileno.", "Revisa que sea rosada y de patas largas."], "El flamenco chileno"),
        W("Planta y ambiente", "Un árbol de piñones crece en bosques de montaña del sur de Chile. ¿Cómo se llama?",
          ["Busco la planta del bosque de montaña del sur.", "El árbol que da piñones y vive allí es la araucaria."], "La araucaria"),
    ],
    mistakes=[
        M("Poner un pingüino en un bosque de montaña.", "No se mira dónde vive la especie.", "El pingüino de Humboldt vive en costas e islas rocosas."),
        M("Creer que una especie está solo para decorar un lugar.", "Se olvida que necesita alimento, agua y refugio.", "Pregunta qué necesita esa especie para vivir."),
    ],
    tiers=tiers(
        [ex("¿La flora son plantas o animales?", "Plantas", "La flora son las plantas; la fauna son los animales."),
         ex("¿El huemul es flora o fauna?", "Fauna", "El huemul es un animal."),
         ex("¿La araucaria es flora o fauna?", "Flora", "La araucaria es un árbol.")],
        [ex("¿Qué necesita una especie del ambiente donde vive? Nombra dos cosas.", "Alimento, agua o refugio", "Esas son las necesidades que cubre el ambiente."),
         ex("¿Dónde vive el flamenco chileno: en una laguna salada del norte o en el bosque del sur?", "En una laguna salada del norte", "Allí encuentra su alimento."),
         ex("¿Qué animal vuela en la cordillera de los Andes: el cóndor o el pingüino?", "El cóndor", "El pingüino de Humboldt vive en la costa.")],
        [ex("Lugar: costa rocosa del norte con islas. ¿Qué ave de la lista vive allí: pingüino de Humboldt, cóndor o flamenco?", "El pingüino de Humboldt", "Vive en costas e islas rocosas."),
         ex("Lugar: bosque húmedo del centro-sur con una flor roja en forma de campana. ¿Cuál es la planta: araucaria o copihue?", "El copihue", "El copihue es una flor de bosques húmedos del centro-sur."),
         ex("Lugar: montaña fría con bosques y animales parecidos a ciervos. ¿Qué especie: huemul o flamenco?", "El huemul", "El huemul habita montañas y bosques fríos del sur.")],
        [ex("Rosa dice: «Pondré flamencos en el bosque porque se verá bonito». ¿Qué error hay?", "El flamenco vive en lagunas saladas del norte, no en un bosque", "Una especie necesita su propio ambiente."),
         ex("Si secan una laguna del norte, ¿qué pasa con los flamencos que comen allí?", "Pierden su alimento y su hogar", "El ambiente les daba alimento y refugio.")],
        [ex("Une cada especie con su ambiente: cóndor, flamenco, pingüino de Humboldt. Ambientes: cordillera, costa rocosa, laguna salada.", "Cóndor con cordillera, flamenco con laguna salada, pingüino con costa rocosa", "Cada una vive donde encuentra lo que necesita."),
         ex("Una familia dice que la araucaria se ve linda en un patio de la playa. ¿Qué dato necesitan saber antes?", "La araucaria crece en bosques de montaña del sur", "Primero se piensa en el ambiente que necesita la planta.")],
    ),
    context=[ex("En una excursión, Ema ve un ave rosada de patas largas en una laguna salada. Dice que es un pingüino. ¿Qué le dirías?", "Es un flamenco; el pingüino vive en la costa", "El ambiente y la forma indican que es un flamenco.")],
    selfcheck=[ex("¿Qué animal es característico de los bosques fríos del sur: huemul o pingüino?", "El huemul", "Vive en montañas y bosques fríos del sur."), ex("¿El copihue es flora o fauna?", "Flora", "Es una planta con flor."), ex("¿Qué necesita una especie para vivir en un lugar?", "Alimento, agua y refugio", "El ambiente debe ofrecer esas cosas.")],
    open_task=task("Elige una especie: araucaria, flamenco chileno o pingüino de Humboldt. Dibuja la especie en su ambiente y escribe tres datos: cómo se llama, dónde vive y qué necesita del lugar.", "Elegí el flamenco chileno. Vive en lagunas saladas del norte y necesita agua con alimento para comer.", ["nombra la especie", "dice dónde vive", "dice qué necesita"], ["dibujo", "tres datos"], ["poner la especie en un ambiente equivocado", "usar la especie solo como adorno"], "Pregunta a un adulto si el ambiente dibujado puede darle alimento, agua y refugio a la especie."),
    reinforce="Nombra un animal y una planta que veas cerca de tu casa y di dónde viven.",
    extend="Escribe una frase que explique qué pasaría con un animal si su ambiente se llena de basura.",
)

register(
    OA9, 3,
    materials="Este cuaderno y un lápiz. La ficha del parque y la lista de normas están escritas en los ejercicios.",
    use="Aprenderé qué es un parque nacional, qué protege y qué normas se cumplen al visitarlo. Sirve para saber cómo cuidar un lugar natural cuando lo visito.",
    prior=["Sé que hay paisajes, plantas y animales valiosos.", "Sé que cuidar necesita normas."],
    explain=[
        "Un parque nacional es una gran área de naturaleza que el Estado protege. En ella se cuidan los paisajes, las plantas y los animales. En Chile, la Corporación Nacional Forestal, llamada CONAF, administra muchos parques nacionales.",
        "Hay ejemplos en todo el país. El Parque Nacional Lauca está en el norte y protege altiplano, lagos y animales como vicuñas. El Parque Nacional La Campana está en la zona central. El Parque Nacional Conguillío protege bosques de araucarias. El Parque Nacional Torres del Paine está en el extremo sur.",
        "Para visitarlo hay normas. Se camina por los senderos marcados. No se sacan plantas ni piedras. No se alimenta a los animales. Se lleva de vuelta la basura. No se hace fuego fuera de los lugares permitidos. Cada norma evita un daño concreto.",
    ],
    vocab=[("parque nacional", "área de naturaleza protegida por el Estado"), ("sendero", "camino marcado para caminar"), ("norma", "regla que ayuda a cuidar"), ("CONAF", "institución que administra parques nacionales"), ("proteger", "cuidar para que no haya daño")],
    worked=[
        W("Para qué sirve una norma", "En un parque hay un cartel: «No alimente a los animales». ¿Qué daño evita?",
          ["Pienso qué pasa si un animal come comida de personas.", "Puede enfermarse o acostumbrarse a pedir comida.", "La norma evita ese daño."], "Evita que los animales se enfermen o dejen de buscar su alimento"),
        W("Qué protege un parque", "El Parque Nacional Conguillío protege bosques de araucarias. ¿Qué cuida: una flora o una fauna?",
          ["La araucaria es un árbol.", "Los árboles son flora.", "El parque cuida bosques de flora."], "Cuida flora: los bosques de araucarias"),
    ],
    mistakes=[
        M("Pensar que en un parque nacional se puede sacar flores como recuerdo.", "No se piensa en el daño a la planta.", "Se miran y se fotografían, pero no se sacan."),
        M("Salirse del sendero para ir más rápido.", "Se pisa la vegetación y se asusta a los animales.", "Siempre se camina por el sendero marcado."),
    ],
    tiers=tiers(
        [ex("Un parque nacional, ¿es un lugar protegido o un lugar para construir casas?", "Un lugar protegido", "El Estado protege su naturaleza."),
         ex("¿Qué institución administra muchos parques nacionales de Chile: CONAF o la panadería?", "CONAF", "Es la Corporación Nacional Forestal."),
         ex("¿Por dónde se camina en un parque: por el sendero o entre las plantas?", "Por el sendero", "El sendero evita pisar plantas.")],
        [ex("¿Qué protege el Parque Nacional Conguillío?", "Bosques de araucarias", "Es el árbol que se menciona en el texto."),
         ex("Menciona dos normas para visitar un parque nacional.", "No sacar plantas y llevarse la basura", "Son normas que cuidan a la naturaleza."),
         ex("¿Para qué sirve la norma de no hacer fuego fuera de los lugares permitidos?", "Para evitar incendios", "El fuego puede quemar bosques y animales.")],
        [ex("Carlos ve un zorro y le quiere dar un sándwich. ¿Cumple la norma?", "No; no se alimenta a los animales", "La norma pide no alimentarlos."),
         ex("Un letrero dice: «Lleve de vuelta su basura». Bia tiene una botella vacía. ¿Qué hace con ella?", "La guarda en su mochila y se la lleva", "Así el parque queda limpio."),
         ex("Una familia visita el Parque Nacional Torres del Paine, en el extremo sur. ¿Está en el norte o en el sur de Chile?", "En el sur", "El texto dice que está en el extremo sur.")],
        [ex("Lola dice: «Llevaré una planta pequeña a mi casa». ¿Por qué no debe?", "Las plantas del parque no se sacan porque son parte del patrimonio", "La norma protege la flora."),
         ex("Pedro dice: «Si todos pisan fuera del sendero no pasa nada». ¿Qué le responderías?", "Entre todos dañarían las plantas", "Muchas pisadas fuera del sendero aplastan plantas.")],
        [ex("Elige la norma que NO ayuda a cuidar: A) llevar la basura, B) quedarse en el sendero, C) gritar para ver si responden los animales.", "C", "Gritar asusta a los animales."),
         ex("Dos parques: Lauca (altiplano, vicuñas) y Conguillío (araucarias). ¿Cuál protege un bosque?", "Conguillío", "Lauca protege altiplano y lagos; Conguillío protege bosques de araucaria.")],
    ),
    context=[ex("Mamá y Nico llegan a un parque nacional. Ven un cartel con tres normas: no sacar plantas, no hacer fuego, ir por el sendero. A Nico le gusta una flor. ¿Qué norma debe recordar?", "No sacar plantas", "La flor es parte de lo que el parque protege.")],
    selfcheck=[ex("En Historia: ¿Qué es un parque nacional?", "Un área de naturaleza protegida por el Estado", "Es un lugar que se cuida para todos."), ex("Nombra un parque nacional de Chile.", "Lauca, La Campana, Conguillío o Torres del Paine", "Son ejemplos del texto."), ex("Escribe una norma de visita.", "Por ejemplo, ir por el sendero o llevar la basura", "Cada norma evita un daño.")],
    open_task=task("Imagina que visitas el Parque Nacional Conguillío con bosques de araucarias. Escribe tres normas que cumplirías y qué daño evita cada una. Puedes usar: ir por el sendero, no sacar plantas, llevar la basura, no hacer fuego.", "Iría por el sendero para no pisar plantas. Llevaría mi basura para no ensuciar. No haría fuego para no quemar el bosque.", ["escribe tres normas", "dice el daño que evita cada norma", "usa palabras claras"], ["lista de tres normas con su razón"], ["escribir normas sin razón", "mezclar el parque con una plaza"], "Muestra la lista a un adulto y explica con tus palabras por qué existe cada norma."),
    reinforce="Nombra una norma que cumplas en un lugar natural cuando lo visitas.",
    extend="Dibuja un cartel de un parque con una norma y su dibujo.",
)

register(
    OA9, 4,
    materials="Este cuaderno y un lápiz. Las fichas de ejemplo están escritas en los ejercicios.",
    use="Aprenderé a presentar un ejemplo de patrimonio natural cercano con tres datos: dónde está, qué lo hace especial y cómo se cuida. Sirve para explicar a otros por qué vale la pena protegerlo.",
    prior=["Sé qué es patrimonio natural.", "Sé que hay parques nacionales y normas."],
    explain=[
        "Cada región de Chile tiene patrimonio natural. Puede ser un parque nacional, un humedal, una playa, un cerro o un bosque. Para presentarlo bien, necesitas tres datos: la ubicación, el rasgo especial y el cuidado.",
        "La ubicación dice dónde está: región, zona norte, centro o sur, y qué hay cerca. El rasgo especial dice qué lo hace valioso: una planta, un animal o un paisaje. El cuidado dice cómo se protege y qué podemos hacer las personas.",
        "Una buena presentación es corta y clara. Por ejemplo: «El Parque Nacional Lauca está en el norte, en el altiplano. Allí viven vicuñas y hay un lago. Se cuida con guardaparques y normas de visita». No hace falta decir todo, pero sí lo que se pide.",
        "Tú también puedes presentar un lugar natural de tu región. Si no lo conoces, pide ayuda a un adulto o a tu profesora: te pueden decir cuál es y dónde está. Revisa que sea un lugar natural y no uno construido.",
    ],
    vocab=[("región", "parte grande en que se divide el país"), ("ubicación", "dónde queda un lugar"), ("rasgo", "algo especial que lo hace distinto"), ("guardaparque", "persona que cuida un parque"), ("presentar", "contar algo de manera ordenada")],
    worked=[
        W("Armar la ficha", "Datos: Parque Nacional Torres del Paine, extremo sur, montañas y lagos, normas de visita. ¿Cuál es la ubicación, el rasgo y el cuidado?",
          ["La ubicación es el extremo sur de Chile.", "El rasgo son las montañas y los lagos.", "El cuidado son las normas de visita."], "Ubicación: extremo sur; rasgo: montañas y lagos; cuidado: normas de visita"),
        W("Completar una presentación", "Completa: «El Parque Nacional Lauca está en el ____ de Chile. Allí viven ____. Se cuida con ____». Opciones: vicuñas, norte, guardaparques y normas.",
          ["Lauca está en el norte.", "Allí viven vicuñas.", "Se cuida con guardaparques y normas."], "Norte, vicuñas, guardaparques y normas"),
    ],
    mistakes=[
        M("Decir solo «es lindo» sin ubicación ni cuidado.", "Falta información importante.", "Escribe los tres datos: ubicación, rasgo y cuidado."),
        M("Inventar un dato sobre el lugar.", "Se confunde lo que se sabe con lo que se imagina.", "Usa solo datos de la ficha o que un adulto te confirme."),
    ],
    tiers=tiers(
        [ex("Para presentar un lugar natural, ¿cuántos datos se piden: ubicación, rasgo y cuidado?", "Tres", "Se piden esos tres datos."),
         ex("¿Qué dato dice dónde queda un lugar: ubicación o cuidado?", "Ubicación", "La ubicación indica el lugar."),
         ex("¿Qué dato dice cómo se protege el lugar: rasgo o cuidado?", "Cuidado", "El cuidado dice cómo se protege.")],
        [ex("Ficha: Parque Nacional La Campana, zona central, palmas chilenas. ¿Cuál es el rasgo especial?", "Las palmas chilenas", "El rasgo es lo que lo hace valioso."),
         ex("Ficha: Parque Nacional Conguillío, bosques de araucarias, sur. ¿Cuál es la ubicación?", "En el sur", "El texto dice sur."),
         ex("¿Por qué no basta decir «es lindo»?", "No dice dónde está ni cómo se cuida", "Una presentación necesita tres datos.")],
        [ex("Datos mezclados: «guardaparques», «montañas y lagos», «extremo sur». Pon cada dato en ubicación, rasgo o cuidado.", "Ubicación: extremo sur; rasgo: montañas y lagos; cuidado: guardaparques", "Cada dato responde a una pregunta distinta."),
         ex("Ficha: Parque Nacional Lauca, norte, vicuñas, normas de visita. Escribe una oración de presentación.", "El Parque Nacional Lauca está en el norte, allí viven vicuñas y se cuida con normas de visita", "Se usan los tres datos."),
         ex("Una presentación dice solo: «El Parque Nacional Conguillío tiene bosques de araucarias». ¿Qué dos datos faltan?", "La ubicación y el cuidado", "Solo se entregó el rasgo; faltan dónde está y cómo se cuida.")],
        [ex("Pablo dijo que La Campana está en el extremo sur. Según la ficha de La Campana, ¿qué error hay?", "Está en la zona central", "La ubicación correcta es zona central."),
         ex("Elena presentó: «Hay animales raros, es bonito». ¿Qué le pedirías agregar?", "Dónde está y cómo se cuida", "Faltan ubicación y cuidado.")],
        [ex("Escribe una presentación de tres frases del Parque Nacional Torres del Paine usando: extremo sur, montañas y lagos, normas de visita.", "Está en el extremo sur. Tiene montañas y lagos. Se cuida con normas de visita", "Cada frase lleva uno de los tres datos."),
         ex("Compara Lauca (norte, vicuñas) y Conguillío (sur, araucarias). ¿En qué se diferencian?", "En la ubicación y en el rasgo", "Uno está en el norte con vicuñas; el otro en el sur con araucarias.")],
    ),
    context=[ex("Una escuela hace una exposición. Dani debe presentar el Parque Nacional La Campana: zona central, palmas chilenas, normas de visita. ¿Qué debe decir sobre el cuidado?", "Que se cuida con normas de visita", "Ese es el dato de cuidado de la ficha.")],
    selfcheck=[ex("¿Qué tres datos lleva una presentación de un lugar natural?", "Ubicación, rasgo y cuidado", "Son los tres datos pedidos."), ex("¿Qué dice el rasgo?", "Lo que hace especial al lugar", "El rasgo muestra por qué es valioso."), ex("Nombra un lugar de patrimonio natural de Chile.", "Lauca, La Campana, Conguillío o Torres del Paine", "Son ejemplos de la clase.")],
    open_task=task("Elige una ficha y escribe tu presentación con tres frases. Ficha A: Parque Nacional Lauca, norte, vicuñas, normas de visita. Ficha B: Parque Nacional Conguillío, sur, araucarias, normas de visita. Después escribe una acción tuya para cuidar la naturaleza.", "Elegí la ficha B. El Parque Nacional Conguillío está en el sur. Tiene bosques de araucarias. Se cuida con normas de visita. Yo no dejaré basura.", ["escribe ubicación, rasgo y cuidado", "usa solo datos de la ficha", "agrega una acción propia"], ["tres frases", "una acción"], ["inventar un dato", "olvidar el cuidado"], "Lee tu presentación a alguien y pregunta si entendió dónde está, qué tiene y cómo se cuida."),
    reinforce="Cuenta a un adulto un lugar natural que conozcas con tres datos: dónde está, qué tiene y cómo se cuida.",
    extend="Dibuja un afiche del parque que elegiste con una norma de visita.",
)

# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="Este cuaderno y un lápiz. Los mapas están escritos en palabras dentro de cada ejercicio.",
    use="Aprenderé a leer un mapa: su título, la orientación y la leyenda. Sirve para ubicar bien un lugar antes de decir algo sobre él.",
    prior=["Sé que el norte se dibuja arriba en un mapa.", "Sé que los símbolos representan cosas."],
    explain=[
        "Un mapa es un dibujo de un lugar visto desde arriba. No es el lugar real, sino una representación. Por eso tiene que ayudar a entender. Antes de ubicar algo, hay tres cosas que se leen primero.",
        "Primero está el título, que dice de qué trata el mapa. Segundo está la orientación, que muestra dónde queda el norte, el sur, el este y el oeste. Tercero está la leyenda, que explica con qué colores o símbolos se dibujó cada cosa. Sin leyenda no sabes qué significa un círculo rojo.",
        "También hay una escala, que dice cuánto se achicó la realidad para caber en el papel. Si lees primero el título, la orientación y la leyenda, no te equivocas al decir dónde queda un lugar o qué zona representa.",
    ],
    vocab=[("mapa", "dibujo de un lugar visto desde arriba"), ("título", "dice de qué trata el mapa"), ("orientación", "muestra dónde queda el norte"), ("leyenda", "explica los símbolos del mapa"), ("escala", "dice cuánto se achicó la realidad")],
    worked=[
        W("Qué es la leyenda", "Un mapa tiene un círculo rojo y una flecha azul. La leyenda dice: círculo rojo = escuela, flecha azul = río. ¿Qué representa el círculo rojo?",
          ["Busco el círculo rojo en la leyenda.", "La leyenda dice que es una escuela."], "Una escuela"),
        W("Leer antes de ubicar", "Un mapa se titula «Zonas norte, centro y sur de Chile». El norte está arriba. ¿Dónde se dibuja la zona sur?",
          ["Leo el título: habla de zonas de Chile.", "Miro la orientación: el norte está arriba.", "La zona sur queda abajo."], "Abajo"),
    ],
    mistakes=[
        M("Ubicar algo sin leer el título ni la leyenda.", "Se puede entender mal qué representa el dibujo.", "Lee siempre título, orientación y leyenda primero."),
        M("Pensar que el mapa es el lugar real.", "Un mapa es un dibujo que representa.", "Úsalo como guía, sabiendo que está achicado."),
    ],
    tiers=tiers(
        [ex("¿Qué parte del mapa dice de qué trata: el título o la leyenda?", "El título", "El título nombra el tema del mapa."),
         ex("¿Qué parte explica los símbolos: la leyenda o el título?", "La leyenda", "La leyenda dice qué significa cada símbolo."),
         ex("¿Qué muestra dónde queda el norte: la orientación o la escala?", "La orientación", "La orientación indica el norte.")],
        [ex("Escribe en orden las tres cosas que se leen antes de ubicar algo en un mapa.", "Título, orientación y leyenda", "Son las tres partes que explicó la clase."),
         ex("¿Qué significa que el mapa sea una representación?", "Que es un dibujo que muestra un lugar real", "No es el lugar mismo."),
         ex("¿Para qué sirve la escala?", "Para saber cuánto se achicó la realidad", "Dice qué tan reducido está el dibujo.")],
        [ex("Mapa «Frutas del huerto de Ema». Leyenda: círculo rojo = manzano, triángulo verde = peral. Aparecen dos círculos rojos y un triángulo verde. ¿Cuántos manzanos hay?", "2", "Cada círculo rojo es un manzano."),
         ex("En el mismo mapa, ¿cuántos perales hay?", "1", "El triángulo verde es un peral y hay uno."),
         ex("Mapa con el norte arriba. Un pueblo está dibujado abajo de un río. ¿Está al norte o al sur del río?", "Al sur", "Abajo es el sur cuando el norte está arriba.")],
        [ex("Lalo dijo que un cuadrado azul era un lago sin leer la leyenda. La leyenda dice cuadrado azul = escuela. ¿Qué error cometió?", "No leyó la leyenda; el cuadrado es una escuela", "La leyenda decide qué representa el símbolo."),
         ex("Dani dibujó un mapa sin título. ¿Qué problema tiene?", "Nadie sabe de qué trata el mapa", "El título dice el tema.")],
        [ex("Mapa: «Zonas de Chile». Norte arriba. Zona A arriba, zona B al medio, zona C abajo. ¿Cuál es el norte, el centro y el sur?", "A es el norte, B el centro y C el sur", "El norte se dibuja arriba y el sur abajo."),
         ex("Mapa sin leyenda: un triángulo amarillo. ¿Se puede saber qué significa? Explica.", "No; falta la leyenda", "Sin leyenda no se explica el símbolo.")],
    ),
    context=[ex("Marta recibe un mapa del patio de su escuela. El título dice «Juegos del patio». La leyenda dice: estrella = columpio, cuadrado = resbalín. Ve dos estrellas. ¿Qué hay dos veces en el patio?", "Columpios", "Cada estrella representa un columpio.")],
    selfcheck=[ex("¿Qué es un mapa?", "Un dibujo de un lugar visto desde arriba", "Representa un lugar real."), ex("¿Qué dice la leyenda?", "Qué significan los símbolos", "Sin ella no se entienden los dibujos."), ex("¿Dónde se dibuja el sur si el norte va arriba?", "Abajo", "Son lados opuestos.")],
    open_task=task("Dibuja un mapa de tu sala o de tu pieza visto desde arriba. Debe tener título, una N para el norte con una flecha y una leyenda con dos símbolos (por ejemplo, círculo = mesa, cuadrado = cama).", "Mi mapa se llama «Mi pieza». Puse una N arriba. Leyenda: círculo = mesa, cuadrado = cama.", ["tiene título", "marca el norte", "tiene leyenda con dos símbolos"], ["dibujo con título, N y leyenda"], ["olvidar la leyenda", "usar símbolos sin explicarlos"], "Pide a un adulto que lea tu mapa y diga si entiende cada símbolo con tu leyenda."),
    reinforce="Mira un mapa en casa o en un libro y busca su título, su orientación y su leyenda.",
    extend="Agrega un tercer símbolo a tu mapa y explícalo en la leyenda.",
)

register(
    OA10, 2,
    materials="Este cuaderno y un lápiz. El mapa de zonas está descrito en palabras.",
    use="Aprenderé a ubicar en la zona norte de Chile a cuatro pueblos originarios: aimara, atacameño o licanantay, diaguita y chango. También ubicaré el pueblo rapa nui, que vive en una isla. Sirve para saber dónde han vivido y cómo se leen sus lugares en un mapa.",
    prior=["Sé leer título, orientación y leyenda de un mapa.", "Sé que Chile tiene zonas norte, centro y sur."],
    explain=[
        "Un pueblo originario es un pueblo que ya vivía en estas tierras antes de que llegaran los españoles. Sus territorios son los lugares donde vivieron y viven. En el mapa de Chile se pueden ubicar por zonas: norte, centro y sur.",
        "En la zona norte vivieron varios pueblos. Los aimara habitaron el altiplano y los valles cercanos, en el extremo norte, cerca de la cordillera. Los atacameños, también llamados licanantay, vivieron en oasis y salares, cerca de San Pedro de Atacama. Los diaguitas vivieron en los valles de las regiones de Atacama y de Coquimbo. Los chango vivieron a lo largo de la costa del norte, pescando y recogiendo mariscos; en el mapa son una franja angosta junto al mar.",
        "Un pueblo no vive en el continente: el pueblo rapa nui vive en la isla Rapa Nui, también llamada Isla de Pascua. Está en el océano Pacífico, muy lejos de la costa de Chile, y en un mapa se dibuja como una isla aparte, al oeste.",
        "Los territorios no eran fronteras rígidas como las de hoy. Los pueblos se movían y se relacionaban. Por eso en el mapa se dibujan como zonas, no como líneas exactas. Hoy muchas personas de estos pueblos viven en el norte, en Rapa Nui y también en otras ciudades de Chile.",
    ],
    vocab=[("pueblo originario", "pueblo que ya vivía aquí antes de la llegada de los españoles"), ("altiplano", "zona alta y plana en la cordillera"), ("oasis", "lugar con agua en el desierto"), ("valle", "tierra baja entre cerros por donde pasa un río"), ("territorio", "zona donde vive un pueblo"), ("rapa nui", "pueblo originario de la isla de Pascua, en el océano Pacífico")],
    worked=[
        W("Un pueblo por su ambiente", "Un pueblo vivió en oasis y salares del desierto, cerca de San Pedro de Atacama. ¿Cuál es?",
          ["Pienso en oasis y salares del norte.", "San Pedro de Atacama está en esa zona.", "Los atacameños o licanantay vivieron allí."], "Los atacameños o licanantay"),
        W("Leer una zona", "En un mapa con norte arriba, los diaguitas se dibujan en una zona al norte del centro, con valles. ¿En qué zona de Chile se ubican?",
          ["El norte está arriba.", "Los valles de los diaguitas están en el norte de Chile."], "En la zona norte"),
    ],
    mistakes=[
        M("Decir que todos los pueblos del norte vivían en el mar.", "Se mezclan los ambientes.", "El altiplano, los oasis y los valles son lugares distintos."),
        M("Dibujar el territorio de un pueblo con una línea exacta.", "Los pueblos se movían y no había fronteras fijas.", "Dibuja una zona aproximada."),
    ],
    tiers=tiers(
        [ex("¿Los aimara, atacameños y diaguitas vivieron en la zona norte, centro o sur?", "Norte", "La clase ubica a estos pueblos en el norte."),
         ex("¿Qué pueblo vivió en el altiplano del extremo norte?", "Los aimara", "El altiplano es su ambiente."),
         ex("¿Qué pueblo vivió en los valles de Atacama y de Coquimbo?", "Los diaguitas", "Esos valles son su zona.")],
        [ex("¿Qué es un oasis?", "Un lugar con agua en el desierto", "Allí hay agua y se puede vivir."),
         ex("¿Dónde está la isla Rapa Nui: en el océano Pacífico o en el altiplano?", "En el océano Pacífico", "Es una isla lejos de la costa, por eso se dibuja aparte."),
         ex("¿Por qué el territorio de un pueblo no se dibuja con una línea exacta?", "Porque se movían y no había fronteras rígidas", "Los territorios eran zonas aproximadas.")],
        [ex("Mapa con norte arriba. Zona 1 en el extremo norte, altiplano. Zona 2 en el norte, oasis y salares. Zona 3 más al sur, valles. ¿Qué número corresponde a los diaguitas?", "La zona 3", "Los diaguitas están en valles más al sur de las otras dos zonas."),
         ex("En el mismo mapa, ¿qué zona corresponde a los aimara?", "La zona 1", "Los aimara habitan el extremo norte, en el altiplano."),
         ex("En el mismo mapa hay una zona 4: una franja angosta junto al mar, en la costa del norte. ¿Qué pueblo corresponde?", "Los chango", "Los chango vivieron en la costa del norte, pescando y recogiendo mariscos.")],
        [ex("Gael dibuja a los aimara en una región de lluvia al sur. ¿Qué error cometió?", "Los aimara habitan el extremo norte, no el sur", "Los ubicó en la zona equivocada."),
         ex("Ema dice que los diaguitas viven en el altiplano del extremo norte. ¿Es correcto?", "No; vivieron en valles de Atacama y de Coquimbo", "El altiplano es de los aimara.")],
        [ex("Ordena de norte a sur: diaguitas, aimara, atacameños.", "Aimara, atacameños, diaguitas", "Se ordena de más al norte a menos al norte."),
         ex("Un niño de una comunidad aimara vive hoy en una ciudad grande. ¿Deja de pertenecer a su pueblo? Explica.", "No; muchas personas de pueblos originarios viven en ciudades", "Pertenecer a un pueblo no depende de dónde se vive.")],
    ),
    context=[ex("En una exposición hay tres tarjetas: «Altiplano», «Oasis y salares» y «Valles de Atacama y Coquimbo». Une cada tarjeta con aimara, atacameño o diaguita.", "Altiplano con aimara, oasis y salares con atacameño, valles con diaguita", "Cada ambiente corresponde a un pueblo.")],
    selfcheck=[ex("Nombra cuatro pueblos originarios del norte de esta clase.", "Aimara, atacameño o licanantay, diaguita y chango", "Son los que se estudiaron; atacameño también se dice licanantay."), ex("¿Qué pueblo vivió en valles de Coquimbo?", "Diaguita", "Allí están sus valles."), ex("¿Dónde se ubican en un mapa con norte arriba?", "Arriba, en la zona norte", "El norte se dibuja arriba.")],
    open_task=task("Dibuja un esquema simple de Chile como una columna vertical. Marca N arriba y S abajo. En la parte alta escribe «Aimara», «Atacameño o licanantay» y «Diaguita» en el orden de norte a sur y haz una zona aproximada para cada uno; dibuja «Chango» como una franja junto al mar y «Rapa Nui» como una isla aparte, a la izquierda. Aclara en una nota: «Cada comunidad cuenta su propia historia; yo solo ubico zonas».", "La columna tiene N arriba y S abajo. Escribí Aimara arriba, Atacameño o licanantay abajo y Diaguita más abajo en el norte. Dibujé a los chango junto al mar y Rapa Nui como isla aparte. Nota: cada comunidad cuenta su propia historia.", ["marca N y S", "ubica los tres pueblos en orden", "dibuja chango junto al mar y Rapa Nui como isla", "usa zonas, no líneas exactas"], ["esquema", "nota de respeto"], ["dibujar fronteras exactas", "mezclar el orden"], "Pide a un adulto que compruebe que el orden va de más norte a menos norte."),
    reinforce="Di en voz alta los nombres de los pueblos del norte y la zona de cada uno.",
    extend="Con ayuda de un adulto, busca un libro o sitio oficial y lee un dato más sobre uno de estos pueblos.",
)

register(
    OA10, 3,
    materials="Este cuaderno y un lápiz. El mapa de zonas está descrito en palabras.",
    use="Aprenderé a ubicar a los picunche, a los mapuche y a los huilliche en el centro, el centro-sur y el sur de Chile, y a entender que sus territorios son amplios y cambiaron. Sirve para ubicar sin usar fronteras rígidas.",
    prior=["Sé ubicar pueblos del norte.", "Sé que hay zonas norte, centro y sur."],
    explain=[
        "Los picunche vivieron en los valles de la zona central de Chile, entre los ríos que bajan de la cordillera. La palabra picunche viene del mapuzugun y se entiende como «gente del norte». Los mapuche habitaron la zona centro-sur, desde el río Biobío hacia el sur, y su nombre quiere decir «gente de la tierra». Los huilliche son parte de la familia mapuche y vivieron más al sur, desde la zona de Valdivia hasta la isla de Chiloé. Su nombre quiere decir «gente del sur».",
        "El territorio mapuche es amplio. Incluye valles, la costa, los bosques y la cordillera. No todos vivían igual: unos estaban en la costa, otros en los valles y otros cerca de la cordillera. Se movían para visitar a otros y para buscar recursos.",
        "Hoy muchas personas mapuche viven en el sur y también en ciudades como Santiago. Por eso no se debe ubicar a un pueblo solo donde hoy viven más personas ni dibujar una línea fija. En un mapa se muestra una zona amplia y aproximada.",
    ],
    vocab=[("picunche", "pueblo originario del valle central"), ("mapuche", "pueblo originario del centro-sur, «gente de la tierra»"), ("zona amplia", "lugar grande sin límites exactos"), ("movilidad", "capacidad de moverse de un lugar a otro"), ("mapuzugun", "la lengua del pueblo mapuche"), ("huilliche", "pueblo mapuche del sur, «gente del sur»")],
    worked=[
        W("Ubicar por zona", "Un pueblo vivió en los valles de la zona central. Su nombre significa «gente del norte». ¿Cuál es?",
          ["Pienso en la zona central y en los valles.", "El nombre habla de «gente del norte».", "Ese pueblo es el picunche."], "Los picunche"),
        W("Una zona amplia", "Un mapa dibuja a los mapuche solo en un punto del sur. ¿Qué falta para que sea correcto?",
          ["Los mapuche habitaron una zona amplia centro-sur.", "Debe dibujarse una zona grande, no un punto."], "Dibujar una zona amplia desde el Biobío hacia el sur"),
    ],
    mistakes=[
        M("Poner a los mapuche solo donde hoy hay más personas.", "El territorio fue más amplio y hoy también viven en otras ciudades.", "Dibuja una zona amplia y aproximada."),
        M("Creer que todos los mapuche vivían igual en todas partes.", "Había costa, valle y cordillera.", "Cada lugar daba distintos recursos."),
    ],
    tiers=tiers(
        [ex("¿Los picunche vivieron en la zona central o en el extremo sur?", "En la zona central", "Vivían en valles del centro."),
         ex("¿Los mapuche habitaron la zona centro-sur o el desierto del norte?", "La zona centro-sur", "Su territorio parte desde el Biobío hacia el sur."),
         ex("¿Qué lengua habla el pueblo mapuche: mapuzugun o aimara?", "Mapuzugun", "Mapuzugun es la lengua del pueblo mapuche.")],
        [ex("¿Qué significa mapuche, según la clase?", "Gente de la tierra", "Mapu es tierra y che es gente."),
         ex("¿Cómo se entiende la palabra picunche?", "Gente del norte", "Así se explica en el texto."),
         ex("¿Por qué se dibuja una zona amplia y no una línea?", "Porque el territorio era amplio y los pueblos se movían", "No había fronteras rígidas.")],
        [ex("Mapa con norte arriba. Zona 1 en el centro del país, valles. Zona 2 más abajo, desde el Biobío hacia el sur. ¿Qué zona es de los picunche?", "La zona 1", "Los picunche vivían en el valle central."),
         ex("En el mismo mapa, ¿cuál zona es de los mapuche?", "La zona 2", "Su territorio parte desde el Biobío hacia el sur."),
         ex("Una comunidad mapuche vivía cerca de la cordillera y otra cerca de la costa. ¿Vivían en el mismo ambiente?", "No; la costa y la cordillera son ambientes distintos", "Su territorio incluía varios ambientes.")],
        [ex("Lucas dice que los mapuche solo viven en el sur hoy y no en otros lugares. ¿Qué le dirías?", "Hoy también viven en ciudades como Santiago", "Muchas personas mapuche viven en otras zonas."),
         ex("Ana dibujó a los picunche en el extremo sur. ¿Qué error hay?", "Vivieron en el valle central", "Su zona es la central.")],
        [ex("Ordena de norte a sur: huilliche, mapuche, picunche.", "Picunche, mapuche, huilliche", "Los picunche viven en el centro, los mapuche desde el Biobío y los huilliche más al sur, hasta Chiloé."),
         ex("¿Qué significa huilliche y en qué parte de Chile vivieron?", "Gente del sur; desde la zona de Valdivia hasta la isla de Chiloé", "Su nombre dice que están más al sur que los mapuche del Biobío.")],
    ),
    context=[ex("En una sala hay un mapa con una línea gruesa que separa el territorio mapuche del resto. Una niña dice que esa línea no es correcta. ¿Por qué podría tener razón?", "Porque los territorios eran zonas amplias y no tenían fronteras rígidas", "Los pueblos se movían y se relacionaban.")],
    selfcheck=[ex("¿En qué zona vivieron los picunche?", "En la zona central", "Vivían en los valles del centro."), ex("¿Qué pueblo mapuche vivió más al sur, hasta Chiloé?", "Los huilliche", "Su nombre significa gente del sur."), ex("¿Por qué no se usan líneas rígidas?", "Porque eran zonas amplias", "Los pueblos se movían.")],
    open_task=task("Dibuja Chile como una columna con N arriba. Marca con sombreado suave una zona central para los picunche, una zona más abajo, amplia, para los mapuche y otra más abajo para los huilliche. Escribe en una nota: «La forma tradicional de contar su historia la enseñan sus comunidades y educadores tradicionales».", "Dibujé una columna con N arriba, zona central para picunche, zona amplia centro-sur para mapuche y huilliche más abajo, hasta Chiloé. Escribí la nota de respeto.", ["usa zonas amplias", "ubica en orden de norte a sur", "escribe la nota de respeto"], ["esquema", "nota"], ["usar líneas rígidas", "olvidar la nota"], "Pide a un adulto que mire si usaste zonas amplias."),
    reinforce="Di en voz alta qué significan mapuche y huilliche y dónde está la zona de cada uno.",
    extend="Con un adulto, busca en un mapa oficial las regiones del centro y del centro-sur de Chile.",
)

register(
    OA10, 4,
    materials="Este cuaderno y un lápiz. El mapa del extremo sur está descrito en palabras.",
    use="Aprenderé a ubicar en el sur y en los territorios australes a los chono, kawésqar, yagán y selk'nam. Sirve para saber cómo la geografía de canales e islas se relaciona con cada pueblo.",
    prior=["Sé ubicar pueblos del norte y del centro.", "Sé que los territorios eran zonas amplias."],
    explain=[
        "El sur de Chile tiene muchos canales, islas y fiordos. Allí vivieron pueblos que conocían muy bien el mar y los bosques. Los chono navegaron por canales entre la isla de Chiloé y el sur de Aysén. Los kawésqar vivieron en los canales de la Patagonia occidental, y los yagán en los canales del extremo sur, hacia el cabo de Hornos.",
        "Los selk'nam vivieron en la Isla Grande de Tierra del Fuego, donde hay estepa y bosque. Fueron cazadores que seguían a los guanacos. Es importante saber que hoy hay descendientes de los pueblos kawésqar, yagán y selk'nam, y que cada comunidad cuenta su historia.",
        "En un mapa, estos pueblos se dibujan en la parte de abajo de la columna de Chile, en zonas amplias. Para ubicarlos, mira primero si hay canales, islas o estepa. Así sabes cuál pueblo va en cada lugar.",
    ],
    vocab=[("canal", "paso angosto de mar entre islas"), ("fiordo", "entrada larga y profunda del mar entre cerros"), ("australe", "del extremo sur"), ("estepa", "terreno plano con pasto y pocos árboles"), ("descendiente", "persona que viene de un pueblo anterior")],
    worked=[
        W("Pueblo y ambiente", "Un pueblo vivió en la Isla Grande de Tierra del Fuego, en la estepa, siguiendo a los guanacos. ¿Cuál fue?",
          ["Pienso en estepa y guanacos.", "La isla es Tierra del Fuego.", "Los selk'nam vivieron allí."], "Los selk'nam"),
        W("De norte a sur", "Hay tres pueblos: kawésqar, chono y yagán. ¿Quién vivió más al sur?",
          ["Los chono están cerca de Chiloé.", "Los kawésqar están en la Patagonia.", "Los yagán están en el extremo sur."], "Los yagán"),
    ],
    mistakes=[
        M("Decir que todos los pueblos del sur eran cazadores de la estepa.", "Algunos vivían en canales y navegaban.", "Mira si el ambiente es canal o estepa."),
        M("Creer que estos pueblos ya no existen hoy.", "Hay descendientes y comunidades.", "Cada comunidad cuenta su propia historia."),
    ],
    tiers=tiers(
        [ex("¿Los chono, kawésqar, yagán y selk'nam vivieron en el norte o en el sur?", "En el sur", "La clase los ubica en el sur y en los territorios australes."),
         ex("¿Qué pueblo vivió en la Isla Grande de Tierra del Fuego?", "Los selk'nam", "Ese es su territorio."),
         ex("¿Los canales son pasos de mar o de tierra?", "De mar", "Un canal es un paso angosto de mar.")],
        [ex("¿Qué es un fiordo?", "Una entrada larga y profunda del mar entre cerros", "Se forma en lugares con montañas cerca del mar."),
         ex("¿Qué ambiente tiene la estepa?", "Terreno plano con pasto y pocos árboles", "Así se describe en la clase."),
         ex("¿Por qué se dice que hay descendientes de estos pueblos?", "Porque hoy hay personas que vienen de ellos", "Los pueblos continúan en sus descendientes.")],
        [ex("Mapa con norte arriba. En la columna de Chile, de arriba hacia abajo, hay cuatro zonas: A cerca de Chiloé, B canales de la Patagonia occidental, C canales del extremo sur, D isla grande al este. ¿Qué pueblo corresponde a la zona A?", "Los chono", "Navegaron entre Chiloé y el sur de Aysén."),
         ex("En el mismo mapa, ¿qué pueblo corresponde a la zona B?", "Los kawésqar", "Habitaron los canales de la Patagonia occidental."),
         ex("En el mismo mapa, ¿qué pueblo corresponde a la zona D, la isla grande?", "Los selk'nam", "Vivieron en la Isla Grande de Tierra del Fuego.")],
        [ex("Javi dice que los yagán vivieron en el desierto. ¿Qué error cometió?", "Vivieron en los canales del extremo sur", "El desierto es del norte."),
         ex("Sara cree que los selk'nam navegaban canales como los kawésqar. Según la clase, ¿cómo vivían los selk'nam?", "En la estepa, siguiendo a los guanacos", "Eran cazadores de la isla grande.")],
        [ex("Ordena de norte a sur: yagán, chono, kawésqar.", "Chono, kawésqar, yagán", "Chiloé queda al norte, luego la Patagonia occidental y después el extremo sur."),
         ex("¿Cuáles tres pueblos del sur navegaban por canales?", "Chono, kawésqar y yagán", "Los selk'nam, en cambio, vivían en la estepa de la isla grande.")],
    ),
    context=[ex("Una profesora muestra un mapa con cuatro zonas coloreadas del sur de Chile y pide a los niños ponerles nombre: chono, kawésqar, yagán y selk'nam. Ema pone «selk'nam» en la zona de canales cerca de Chiloé. ¿Está bien?", "No; esa zona es de los chono", "Los selk'nam vivieron en la isla grande.")],
    selfcheck=[ex("Nombra los cuatro pueblos del sur de esta clase.", "Chono, kawésqar, yagán y selk'nam", "Son los que se estudiaron."), ex("¿Qué ambiente tiene el territorio kawésqar?", "Canales", "Vivían en los canales de la Patagonia occidental."), ex("¿Hay descendientes hoy de estos pueblos?", "Sí, hay descendientes y comunidades", "Los pueblos continúan.")],
    open_task=task("Dibuja la parte sur de Chile como una columna con canales e islas. Escribe cuatro rótulos en orden de norte a sur: chono, kawésqar, yagán y una isla grande al este para selk'nam. Escribe una nota: «Las comunidades cuentan su historia; yo solo ubico zonas».", "Dibujé la columna con canales e islas. Puse chono arriba, kawésqar, yagán y la isla de los selk'nam. Escribí la nota.", ["usa los cuatro pueblos", "ordena de norte a sur", "escribe la nota de respeto"], ["esquema con cuatro rótulos", "nota"], ["mezclar el orden", "usar líneas rígidas"], "Pide a un adulto que revise que la isla grande sea de los selk'nam."),
    reinforce="Nombra un pueblo del sur y el ambiente donde vivió.",
    extend="Con un adulto, mira un mapa oficial y busca el cabo de Hornos y la Isla Grande de Tierra del Fuego.",
)

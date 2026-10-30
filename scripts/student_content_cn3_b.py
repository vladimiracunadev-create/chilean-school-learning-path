"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 08 (fuentes de luz) y OA 09 (propagación, reflexión y colores de la luz)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA8, OA9 = "CN03 OA 08", "CN03 OA 09"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 08
register(
    OA8, 1,
    materials="Una pieza o un clóset que se pueda dejar oscuro, una linterna, un espejo de mano, un trozo de papel aluminio y un peluche. Nunca mires directo a la linterna ni al Sol.",
    use="Aprenderé a distinguir si un objeto emite luz propia o solo refleja la luz de otro. Sirve para no confundir algo que brilla con algo que de verdad produce luz.",
    prior=["Sé que necesitamos luz para ver los objetos.", "Sé que el Sol alumbra de día."],
    explain=[
        "Una fuente de luz es un objeto que emite luz, es decir, que produce su propia luz. El Sol, una ampolleta encendida y una linterna encendida son fuentes de luz. Se ven aunque no haya otra luz cerca.",
        "Otros objetos solo reflejan la luz. Reflejar es hacer rebotar la luz que llega desde otra fuente. Un espejo, el papel aluminio y la Luna brillan porque les llega luz y la devuelven. No producen luz propia.",
        "Hay una prueba muy simple: la oscuridad. Si dejo un objeto en una pieza sin ninguna luz y aun así lo veo, emite luz. Si deja de verse, solo reflejaba. Por eso no todo lo que brilla es una fuente de luz.",
    ],
    vocab=[("fuente de luz", "objeto que produce luz"), ("emitir", "producir y enviar luz propia"), ("reflejar", "hacer rebotar la luz que llega de otra fuente"), ("oscuridad", "lugar donde no hay luz"), ("brillar", "verse con mucha luz; puede ser luz propia o luz reflejada")],
    worked=[
        {"title": "La linterna y el espejo", "problem": "En una pieza oscura hay una linterna encendida y un espejo. ¿Cuál emite luz y cuál solo refleja?", "steps": ["Veo la linterna aunque nada la alumbre desde afuera: tiene luz propia.", "Veo el espejo solo si la luz de la linterna le llega.", "Si apago la linterna, el espejo deja de verse."], "answer": "La linterna emite luz; el espejo solo refleja"},
        {"title": "La Luna brilla", "problem": "La Luna se ve brillante de noche. ¿Es una fuente de luz?", "steps": ["Pregunto de dónde viene su luz.", "Su luz es la del Sol, que rebota en ella.", "Rebotar es reflejar, no emitir."], "answer": "No; la Luna refleja la luz del Sol"},
    ],
    mistakes=[
        {"wrong": "Decir «el espejo es una fuente de luz porque brilla».", "why": "Se confunde brillar con producir luz.", "fix": "Haz la prueba de la oscuridad: si sin luz externa no se ve, solo refleja."},
        {"wrong": "Pensar que la Luna produce su propia luz.", "why": "Se ve luminosa de noche y parece una lámpara.", "fix": "Recuerda que la Luna refleja la luz del Sol."},
    ],
    tiers={
        "recovery": [
            ex("El Sol, ¿emite luz propia o solo refleja la luz de otro objeto?", "Emite luz propia", "El Sol produce su propia luz, por eso es una fuente."),
            ex("Un espejo está en una pieza completamente oscura, sin ninguna otra luz. ¿Produce luz propia?", "No", "El espejo solo refleja la luz que le llega; sin luz no se ve."),
            ex("Completa con «emite» o «refleja»: una ampolleta encendida ___ luz propia.", "emite", "Una ampolleta encendida produce luz, no la rebota."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre emitir luz y reflejar luz?", "Emitir es producir luz propia y reflejar es hacer rebotar la luz de otra fuente", "Emitir crea luz; reflejar solo la devuelve."),
            ex("La Luna brilla de noche. ¿Es una fuente de luz?", "No, refleja la luz del Sol", "La luz que vemos en la Luna viene del Sol."),
            ex("Una cinta reflectante de una mochila brilla cuando la alumbra la luz de un auto y en oscuridad total no se ve. ¿Emite o refleja luz?", "Refleja", "Si necesita luz de otra fuente para verse, solo la refleja."),
        ],
        "apply": [
            ex("Clasifica en «emite» o «refleja»: linterna encendida, hoja blanca, ampolleta encendida, espejo.", "Emiten: linterna encendida y ampolleta encendida. Reflejan: hoja blanca y espejo", "Los dos primeros producen luz y los otros dos solo la devuelven."),
            ex("Una pieza está completamente oscura y en ella hay una linterna encendida y un espejo. ¿Cuál de los dos se ve por su propia luz?", "La linterna", "La linterna emite luz propia; el espejo necesita luz de otra fuente."),
            ex("Marcos dice que los adornos brillantes de sus zapatillas son fuentes de luz. En una pieza sin ninguna luz, ¿brillarían?", "No", "Solo reflejan la luz; sin luz que les llegue no se ven."),
        ],
        "reason": [
            ex("Sofía dice: «Todo lo que brilla es una fuente de luz». ¿Cuál de estos ejemplos prueba que se equivoca: el Sol, la Luna o una ampolleta encendida?", "La Luna", "La Luna brilla, pero solo refleja la luz del Sol."),
            ex("En un clóset sin ninguna luz hay un espejo y un peluche. ¿Cuál de los dos se ve?", "Ninguno", "Los dos solo reflejan luz; sin luz no se ve ninguno."),
        ],
        "challenge": [
            ex("Una luciérnaga brilla de noche en un campo sin luces. ¿Es una fuente de luz? Usa la prueba de la oscuridad.", "Sí, porque se ve en la oscuridad y produce luz propia", "Un objeto que se ve en la oscuridad total emite luz."),
            ex("Quieres saber si una pulsera brillante emite o solo refleja luz. ¿Qué haces y qué resultado muestra que solo refleja?", "La dejo en una pieza completamente oscura y, si deja de verse, solo refleja", "Si sin luz externa se deja de ver, no producía luz propia."),
        ],
    },
    context=[ex("Camino a casa, Tomás ve tres cosas: la Luna llena, un semáforo en verde y una señal de tránsito que brilla cuando la alumbra un auto. ¿Cuál de las tres emite luz propia?", "El semáforo", "La Luna y la señal solo reflejan; el semáforo produce su luz.")],
    selfcheck=[
        ex("¿Qué hace una fuente de luz?", "Emite luz propia", "Fuente de luz es lo que produce luz."),
        ex("¿Una cosa que solo refleja luz es una fuente de luz?", "No", "Solo devuelve la luz que recibe."),
        ex("¿Qué prueba te sirve para saber si algo emite luz?", "La oscuridad", "Si se ve sin luz externa, emite luz."),
    ],
    open_task=task(
        "Si puedes, oscurece un clóset o una pieza. Pon dentro una linterna, un espejo, papel aluminio y un peluche, y anota qué ves con la linterna apagada y con la linterna encendida. Si no puedes, usa esta tabla: con la linterna apagada no se ve ningún objeto; con la linterna encendida se ven la linterna y, alumbrados por ella, el espejo, el papel aluminio y el peluche. Escribe cuál objeto emite luz y cuáles solo reflejan, con una frase de prueba.",
        "Emite luz solo la linterna: con ella apagada no se ve nada, y encendida alumbra a los demás. El espejo, el aluminio y el peluche solo reflejan la luz de la linterna.",
        ["identifica la linterna como única fuente", "nombra los objetos que solo reflejan", "usa la oscuridad como prueba"],
        ["tabla con lo observado", "frase con la conclusión", "dibujo de la pieza oscura"],
        ["decir que el espejo emite luz porque brilla", "no mencionar la prueba de la oscuridad"],
        "Reconoce la prueba bien hecha y pide que explique por qué el papel aluminio brilla sin ser una fuente.",
    ),
    reinforce="Mira en tu casa tres objetos que brillan. Para cada uno escribe si crees que emite o solo refleja y qué prueba harías.",
    extend="Averigua con una persona de tu casa por qué la Luna cambia de forma, y cuenta si la Luna produce su luz.",
)

register(
    OA8, 2,
    materials="Papel y lápiz para completar una tabla con dos criterios. Las fuentes se dan escritas en esta clase y no necesitas usar fuego ni conectar nada.",
    use="Aprenderé a clasificar fuentes de luz con dos preguntas claras. Sirve para ordenar muchas fuentes sin equivocarme.",
    prior=["Sé que una fuente de luz emite luz propia.", "Sé que la Luna y el espejo solo reflejan."],
    explain=[
        "Para clasificar una fuente de luz uso dos criterios. Primer criterio: ¿emite luz propia? Si no, no es una fuente. Segundo criterio: ¿existe sola en la naturaleza o la hicieron las personas?",
        "Una fuente natural de luz existe sin que las personas la fabriquen: el Sol, las estrellas, los relámpagos y las luciérnagas. Una fuente artificial es hecha por las personas: la ampolleta, la linterna, la pantalla de un televisor y la llama de una vela.",
        "El fuego puede ser de los dos tipos. Un incendio de bosque provocado por un rayo es natural. La llama de una vela, encendida por una persona, es artificial. Para clasificar miro quién la produjo. Cuidado: el fuego solo se usa con una persona adulta.",
    ],
    vocab=[("natural", "que existe en la naturaleza sin que las personas lo fabriquen"), ("artificial", "hecho por las personas"), ("criterio", "regla o pregunta que uso para clasificar"), ("relámpago", "chispa muy grande de luz que aparece en una tormenta"), ("estrella", "astro que emite luz propia, como el Sol")],
    worked=[
        {"title": "Clasificar el Sol", "problem": "Clasifica el Sol con los dos criterios.", "steps": ["¿Emite luz propia? Sí.", "¿Existe sola en la naturaleza? Sí.", "Entonces cumple los dos criterios de fuente natural."], "answer": "Fuente natural de luz"},
        {"title": "Clasificar una linterna", "problem": "Clasifica una linterna encendida.", "steps": ["¿Emite luz propia? Sí.", "¿La hicieron las personas? Sí, la fabrican personas.", "Por eso es artificial."], "answer": "Fuente artificial de luz"},
    ],
    mistakes=[
        {"wrong": "Clasificar el fuego siempre como natural.", "why": "Se piensa que el fuego es natural por ser una llama.", "fix": "Pregunta quién lo produjo: un rayo lo hace natural; una persona que enciende una vela lo hace artificial."},
        {"wrong": "Decir que la Luna es una fuente natural de luz.", "why": "Se usa solo el criterio «está en la naturaleza».", "fix": "Primero pregunta si emite luz propia; la Luna solo refleja, por eso no es una fuente."},
    ],
    tiers={
        "recovery": [
            ex("¿Una ampolleta encendida es una fuente natural o artificial?", "Artificial", "Las personas fabrican las ampolletas."),
            ex("¿Un relámpago es una fuente natural o artificial?", "Natural", "Aparece en las tormentas sin que lo fabriquen las personas."),
            ex("Completa: la primera pregunta para clasificar una fuente de luz es si ___ luz propia.", "emite", "Solo una fuente emite luz propia."),
        ],
        "understand": [
            ex("¿Qué quiere decir que una fuente es artificial?", "Que la hicieron las personas", "Artificial es lo fabricado por las personas."),
            ex("¿Por qué una luciérnaga es una fuente natural?", "Porque emite luz propia y no la fabricó una persona", "Cumple los dos criterios: emite luz y existe en la naturaleza."),
            ex("La llama de una vela puede ser artificial. ¿Qué dato lo muestra?", "Que una persona la enciende", "Una persona produce la llama con la vela."),
        ],
        "apply": [
            ex("Clasifica en natural o artificial: el Sol, la pantalla de un televisor, las estrellas, una linterna.", "Naturales: el Sol y las estrellas. Artificiales: la pantalla de un televisor y la linterna", "El Sol y las estrellas existen solos; los otros los fabrican personas."),
            ex("Un rayo incendia un árbol en el cerro y se forma una llama. ¿Esa llama es una fuente natural o artificial?", "Natural", "El rayo la causó sin intervención de una persona."),
            ex("Una persona adulta enciende una fogata en un lugar autorizado. ¿La luz de la fogata es natural o artificial?", "Artificial", "Una persona la encendió."),
        ],
        "reason": [
            ex("Daniela dice que un espejo es una fuente artificial porque lo fabrican personas. ¿Qué criterio olvidó?", "Que una fuente debe emitir luz propia", "El espejo solo refleja, así que no es una fuente."),
            ex("Dos amigos discuten: uno dice que la Luna es una fuente natural y el otro que no es fuente. ¿Quién tiene razón?", "El que dice que no es fuente", "La Luna no emite luz propia, solo refleja la del Sol."),
        ],
        "challenge": [
            ex("Si no sabes si algo es fuente de luz, ¿qué dos preguntas haces y en qué orden?", "Primero si emite luz propia y después si es natural o artificial", "Si no emite luz propia, no hay que clasificarlo como fuente."),
            ex("En una playa de noche se ven una estrella, un faro encendido y el reflejo de la Luna en el agua. ¿Cuáles son fuentes de luz y cuál es natural y cuál artificial?", "Son fuentes la estrella (natural) y el faro (artificial); el reflejo de la Luna no es fuente", "Solo emiten luz la estrella y el faro; el reflejo es luz rebotada."),
        ],
    },
    context=[ex("En una tormenta de noche, Valentina ve un relámpago, la lámpara de su velador encendida y las estrellas entre las nubes. ¿Cuántas de las tres son fuentes naturales?", "Dos: el relámpago y las estrellas", "La lámpara es artificial; las otras dos existen en la naturaleza.")],
    selfcheck=[
        ex("¿Una fuente artificial la hace la naturaleza o las personas?", "Las personas", "Artificial es lo hecho por las personas."),
        ex("¿Las estrellas son fuentes naturales de luz?", "Sí", "Emiten luz propia y existen sin que las fabriquen."),
        ex("¿Qué se pregunta primero al clasificar: si emite luz propia o si es natural?", "Si emite luz propia", "Primero hay que saber si es una fuente."),
    ],
    open_task=task(
        "Copia y completa esta tabla marcando natural o artificial: Sol, ampolleta, relámpago, linterna, luciérnaga, pantalla de televisor. Luego escribe una frase que explique con los dos criterios por qué el Sol es natural y la linterna artificial. Si puedes, agrega dos fuentes más que veas en tu casa.",
        "Naturales: Sol, relámpago, luciérnaga. Artificiales: ampolleta, linterna, pantalla de televisor. El Sol emite luz propia y existe solo; la linterna emite luz propia pero la fabrican personas.",
        ["clasifica las seis fuentes sin error", "usa los dos criterios en la frase", "agrega fuentes que sí emiten luz propia"],
        ["tabla completada", "frase con los dos criterios", "lista de dos fuentes de casa"],
        ["marcar la Luna o un espejo como fuente", "usar un solo criterio"],
        "Valora la tabla y pide que revise si las fuentes agregadas realmente emiten luz propia.",
    ),
    reinforce="Haz dos columnas, «natural» y «artificial», y escribe tres fuentes en cada una. Pídele a alguien de tu casa que las revise.",
    extend="Mira por una ventana de noche y anota cuántas fuentes artificiales de luz ves desde ahí.",
)

register(
    OA8, 3,
    materials="Papel y lápiz. Las comparaciones se hacen con las situaciones escritas en el cuaderno y con lo que recuerdas de tu casa. No toques ampolletas encendidas.",
    use="Aprenderé en qué se parecen y en qué se diferencian las fuentes naturales y las artificiales. Sirve para decidir qué luz conviene en cada situación.",
    prior=["Sé clasificar fuentes de luz en naturales y artificiales.", "Sé que emitir es producir luz propia."],
    explain=[
        "Las fuentes naturales y las artificiales se parecen en algo importante: todas emiten luz propia. Se diferencian en quién las produce y en cómo las usamos.",
        "Una fuente natural, como el Sol, no la podemos encender ni apagar. El Sol alumbra de día y de noche no se ve. Una fuente artificial, como una ampolleta o una linterna, se enciende y se apaga cuando la persona quiere, y funciona de noche con electricidad o con pilas.",
        "Muchas fuentes también dan calor. El Sol calienta la Tierra y una ampolleta encendida se calienta. Por eso nunca se toca una ampolleta que lleva rato encendida. Las dos clases de fuente son útiles: el Sol nos da luz gratis, y las artificiales nos ayudan cuando no hay Sol.",
    ],
    vocab=[("comparar", "buscar en qué se parecen y en qué se diferencian dos cosas"), ("encender", "hacer que algo empiece a dar luz"), ("pila", "pieza que guarda energía y hace funcionar una linterna"), ("electricidad", "energía que llega por el enchufe y hace funcionar una ampolleta"), ("calor", "energía que hace que algo se sienta caliente")],
    worked=[
        {"title": "Sol y ampolleta", "problem": "Compara el Sol y una ampolleta: ¿qué tienen en común y qué las diferencia?", "steps": ["En común: las dos emiten luz propia.", "El Sol es natural y no se enciende ni se apaga.", "La ampolleta es artificial y se enciende con un interruptor."], "answer": "Las dos emiten luz propia; el Sol es natural y la ampolleta se enciende y apaga"},
        {"title": "Luz en un corte de luz", "problem": "En la noche hay un corte de luz. ¿Sirve el Sol o una linterna con pilas?", "steps": ["De noche el Sol no alumbra.", "La linterna funciona con pilas, sin enchufe.", "Entonces conviene la linterna."], "answer": "Una linterna con pilas"},
    ],
    mistakes=[
        {"wrong": "Decir que las fuentes artificiales no son fuentes de verdad.", "why": "Se piensa que solo la luz natural es luz propia.", "fix": "Ambas emiten luz propia; solo cambia quién las produce."},
        {"wrong": "Pensar que el Sol se apaga de noche.", "why": "No lo vemos y parece que dejó de alumbrar.", "fix": "El Sol sigue emitiendo luz; de noche nuestro lado de la Tierra mira hacia otra dirección."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué tienen en común el Sol y una ampolleta?", "Las dos emiten luz propia", "Ambas son fuentes de luz."),
            ex("¿Cuál se puede encender y apagar cuando una persona quiere: el Sol o una linterna?", "Una linterna", "Las artificiales se encienden con un interruptor."),
            ex("Completa: una ampolleta funciona con ___ del enchufe.", "electricidad", "La ampolleta de una casa necesita electricidad."),
        ],
        "understand": [
            ex("¿Por qué no podemos apagar el Sol como apagamos una ampolleta?", "Porque es una fuente natural que no producimos nosotros", "Las personas no controlan el Sol."),
            ex("¿Cuál es una diferencia entre una fuente natural y una artificial?", "La natural existe sola y la artificial la hacen las personas", "La diferencia es quién la produce."),
            ex("¿Por qué no se toca una ampolleta que lleva horas encendida?", "Porque está caliente", "Las ampolletas encendidas se calientan y pueden quemar."),
        ],
        "apply": [
            ex("Es de noche y quieres leer en tu pieza. ¿Qué fuente usas: el Sol, una lámpara de velador o una estrella?", "Una lámpara de velador", "Es artificial y se enciende cuando la necesitas."),
            ex("Pablo va de campamento y no hay enchufes. ¿Qué fuente artificial puede llevar para alumbrar de noche?", "Una linterna con pilas", "Funciona sin enchufe."),
            ex("Una tienda de campaña verde queda alumbrada de día sin encender nada. ¿Qué fuente natural la alumbra?", "El Sol", "De día el Sol es la fuente natural que alumbra."),
        ],
        "reason": [
            ex("Un compañero dice: «Las fuentes naturales son mejores porque dan luz siempre». ¿Es cierto que el Sol alumbra siempre un mismo lugar de la Tierra?", "No", "De noche el Sol no alumbra ese lugar."),
            ex("Una pieza está sin ventanas. Aunque sea de día afuera, ¿qué fuente conviene usar adentro y por qué?", "Una artificial, porque el Sol no llega adentro", "Sin ventanas no entra la luz del Sol."),
        ],
        "challenge": [
            ex("En un parque de noche, los faroles son útiles porque dan luz cuando no hay Sol. ¿Los faroles son fuentes naturales o artificiales?", "Artificiales", "Las personas los fabrican y los encienden cuando falta el Sol."),
            ex("¿Qué fuente necesita pilas o electricidad para funcionar: el Sol o una linterna?", "Una linterna", "El Sol no necesita pilas ni enchufe; la linterna sí."),
        ],
    },
    context=[ex("Un barco pequeño navega de noche cerca de la costa y ve un faro que se enciende y apaga con una secuencia. ¿El faro es una fuente natural o artificial y para qué sirve?", "Es artificial y sirve para avisar dónde está la costa", "Lo hicieron personas y su luz guía a los barcos.")],
    selfcheck=[
        ex("¿Qué tienen en común todas las fuentes de luz?", "Emiten luz propia", "Eso las hace fuentes."),
        ex("¿Una fuente artificial se puede encender y apagar?", "Sí", "Las personas la controlan."),
        ex("¿Quién produce una fuente natural de luz?", "La naturaleza", "No la fabrican las personas."),
    ],
    open_task=task(
        "Completa esta tabla de comparación para el Sol y para una linterna: ¿emite luz propia?, ¿quién la produce?, ¿se puede encender y apagar?, ¿funciona de noche? Después escribe dos frases: una sobre en qué se parecen y otra sobre en qué se diferencian.",
        "Sol: sí emite luz, la produce la naturaleza, no se enciende ni apaga, de noche no alumbra mi lugar. Linterna: sí emite luz, la fabrican personas, se enciende y se apaga, funciona de noche. Se parecen en que emiten luz propia; se diferencian en quién las produce.",
        ["completa las cuatro filas sin error", "escribe una semejanza correcta", "escribe una diferencia correcta"],
        ["tabla completa", "dos frases de comparación"],
        ["decir que el Sol se apaga de noche", "confundir semejanza con diferencia"],
        "Pide que lea en voz alta su semejanza y explique con un ejemplo de su casa.",
    ),
    reinforce="Haz un dibujo dividido en dos mitades: a la izquierda una fuente natural y a la derecha una artificial. Escribe una diferencia debajo.",
    extend="Pregunta en tu casa cuántas ampolletas hay y cuáles se usan más de noche.",
)

register(
    OA8, 4,
    materials="Papel y lápiz. Las situaciones están escritas en el cuaderno. Si tienes una linterna con pilas, puedes usarla con ayuda de una persona adulta; no uses fuego.",
    use="Aprenderé para qué usamos las fuentes de luz y cómo usarlas con seguridad. Sirve para cuidarme a mí y a mi casa.",
    prior=["Sé qué es una fuente natural y una artificial.", "Sé que algunas fuentes dan calor."],
    explain=[
        "Usamos la luz para ver de noche, para estudiar, para avisar y para cuidarnos. Los semáforos usan luz para ordenar el tránsito, los faros guían a los barcos y las linternas sirven cuando se corta la luz.",
        "Las fuentes de luz también tienen riesgos. Nunca se debe mirar el Sol directamente, porque daña los ojos. Una ampolleta encendida se calienta y no se toca. No se debe poner el dedo en un enchufe. El fuego, como el de una vela o un fósforo, lo maneja solo una persona adulta.",
        "También cuidamos la energía. Si apagamos las luces que no usamos, gastamos menos electricidad. Una ampolleta LED gasta menos electricidad que una ampolleta antigua y alumbra bien. En un corte de luz es más seguro usar una linterna que una vela, porque la linterna no tiene llama.",
    ],
    vocab=[("seguridad", "cuidarse para evitar accidentes"), ("riesgo", "posibilidad de que algo cause daño"), ("ahorrar", "gastar menos de algo"), ("LED", "tipo de ampolleta que usa poca electricidad"), ("corte de luz", "momento en que se va la electricidad de la casa")],
    worked=[
        {"title": "Una ampolleta recién apagada", "problem": "Una ampolleta estuvo encendida mucho rato y la apagan hace un minuto. ¿La puedes tocar?", "steps": ["Una ampolleta encendida se calienta.", "Apagarla no la enfría al instante.", "Puede seguir caliente y quemar."], "answer": "No, hay que esperar a que se enfríe"},
        {"title": "Luz en un corte de luz", "problem": "Se corta la luz de noche. Tienes una linterna y una vela. ¿Qué es más seguro?", "steps": ["La vela tiene una llama que puede iniciar un incendio.", "La linterna no tiene llama.", "Elijo la linterna."], "answer": "La linterna"},
    ],
    mistakes=[
        {"wrong": "Mirar el Sol un momento para ver cómo es.", "why": "Se cree que un instante no hace daño.", "fix": "No mires nunca el Sol directamente; puede dañar tus ojos aunque sea poco tiempo."},
        {"wrong": "Dejar las luces encendidas aunque nadie las use.", "why": "Se piensa que la luz no cuesta nada.", "fix": "Apaga las luces al salir de una pieza para ahorrar electricidad."},
    ],
    tiers={
        "recovery": [
            ex("¿Se debe mirar directamente al Sol?", "No", "Puede dañar los ojos."),
            ex("¿Quién puede manejar una vela encendida: un niño solo o una persona adulta?", "Una persona adulta", "El fuego puede causar quemaduras o incendios."),
            ex("Completa: al salir de una pieza, ___ la luz para ahorrar electricidad.", "apago", "Apagar la luz evita gastar electricidad."),
        ],
        "understand": [
            ex("¿Para qué sirve la luz de un semáforo?", "Para ordenar el tránsito", "Los colores indican cuándo avanzar o detenerse."),
            ex("¿Por qué una linterna es más segura que una vela en un corte de luz?", "Porque no tiene llama", "Sin llama no hay riesgo de incendio."),
            ex("¿Por qué conviene una ampolleta LED?", "Porque gasta menos electricidad", "Alumbra gastando menos energía."),
        ],
        "apply": [
            ex("Salvador sale de su pieza y deja la luz y la lámpara encendidas. ¿Qué acción de seguridad y ahorro debería hacer?", "Apagar las luces", "Así evita gastar electricidad."),
            ex("Ana quiere cambiar una ampolleta que acaba de apagarse y está caliente. ¿Qué hace primero?", "Espera a que se enfríe y pide ayuda a una persona adulta", "La ampolleta caliente puede quemar."),
            ex("Un niño ve un puntero láser en una tienda y quiere apuntar a los ojos de su amigo. ¿Está bien?", "No", "La luz fuerte puede dañar los ojos."),
        ],
        "reason": [
            ex("Pedro dice: «Está bien mirar el Sol si uso lentes oscuros comunes». ¿Es una regla segura?", "No", "Los lentes comunes no protegen para mirar el Sol directamente; no se mira el Sol."),
            ex("Dos casas tienen el mismo número de ampolletas. En una las apagan al salir y en la otra no. ¿Cuál gasta menos electricidad?", "La que las apaga al salir", "Una ampolleta apagada no consume electricidad."),
        ],
        "challenge": [
            ex("Una regla dice «no tocar ampolletas encendidas» y otra dice «no mirar el Sol directamente». ¿Cuál de las dos evita una quemadura?", "No tocar ampolletas encendidas", "La ampolleta encendida está caliente; mirar el Sol daña los ojos, no quema la mano."),
            ex("Durante un corte de luz de noche, ¿qué objeto conviene tener a mano en casa y por qué?", "Una linterna con pilas, porque da luz sin llama", "Sirve sin electricidad y es más segura que el fuego."),
        ],
    },
    context=[ex("Mientras Isidora hace su tarea de noche, el computador de su casa se apaga por un corte de luz. En el cajón hay una linterna con pilas y una caja de fósforos. ¿Qué toma y qué hace con los fósforos?", "Toma la linterna y deja los fósforos para una persona adulta", "Los fósforos producen fuego y solo los usa un adulto.")],
    selfcheck=[
        ex("¿Qué fuente de luz no se debe mirar directamente?", "El Sol", "Mirarlo daña los ojos."),
        ex("¿Una ampolleta recién apagada puede estar caliente?", "Sí", "Tarda en enfriarse."),
        ex("¿Apagar las luces que no uso ayuda a ahorrar electricidad?", "Sí", "Se gasta menos energía."),
    ],
    open_task=task(
        "Haz un afiche de seguridad con tres reglas para usar la luz en casa. Usa estas ideas si lo necesitas: no mirar el Sol, no tocar ampolletas encendidas, apagar luces que no uso, el fuego solo con personas adultas, usar linterna en un corte de luz. Dibuja una escena para cada regla.",
        "Regla 1: No miro el Sol directamente (dibujo de un niño que mira hacia abajo en el patio). Regla 2: No toco una ampolleta encendida. Regla 3: Apago la luz al salir.",
        ["escribe tres reglas distintas y seguras", "cada regla tiene un dibujo claro", "incluye al menos una de ahorro o de seguridad con calor"],
        ["afiche terminado", "tres dibujos con reglas"],
        ["incluir una regla insegura como «mirar el Sol con lentes»", "repetir la misma regla tres veces"],
        "Valora el afiche y pide que explique oralmente por qué cada regla evita un daño.",
    ),
    reinforce="Revisa tu pieza y anota qué luces se podrían apagar cuando no estás.",
    extend="Averigua con una persona de tu casa cuál es la regla de seguridad más importante con las ampolletas y los enchufes.",
)

# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Una linterna, tres tarjetas de cartulina con un orificio hecho por una persona adulta con perforadora de oficina, tres trozos de plasticina para pararlas, una pared clara y una pieza que puedas oscurecer. No mires al haz de la linterna.",
    use="Aprenderé que la luz viaja en línea recta. Sirve para entender por qué las sombras tienen la forma de los objetos.",
    prior=["Sé que una fuente de luz emite luz.", "Sé que una línea recta no se dobla."],
    explain=[
        "La luz viaja en línea recta. El camino que sigue la luz se llama trayectoria, y una línea fina de luz se llama rayo. Dibujamos un rayo como una línea recta con una flecha.",
        "Puedo comprobarlo con tres tarjetas, cada una con un orificio. Las pongo en fila, una detrás de otra, con los orificios a la misma altura. Si la linterna ilumina el primer orificio, la luz pasa por los tres y forma un punto en la pared.",
        "Si muevo la tarjeta del medio hacia un lado, la luz ya no pasa. Eso muestra que la luz no se dobla para pasar por el orificio. También explica las sombras: como la luz va recta y un objeto la tapa, detrás queda un espacio sin luz con la forma del objeto.",
    ],
    vocab=[("rayo de luz", "línea de luz que viaja recta"), ("trayectoria", "camino que sigue algo al moverse"), ("línea recta", "línea sin curvas"), ("sombra", "zona oscura que queda detrás de un objeto que tapa la luz"), ("orificio", "agujero pequeño")],
    worked=[
        {"title": "Tres tarjetas alineadas", "problem": "Tres tarjetas con orificios están en fila y alineadas. La luz de una linterna entra por el primer orificio. ¿Qué se ve en la pared?", "steps": ["Los orificios están a la misma altura y en línea recta.", "La luz viaja recta y pasa por los tres.", "Aparece un punto de luz en la pared."], "answer": "Un punto de luz en la pared"},
        {"title": "Tarjeta del medio movida", "problem": "Ahora la tarjeta del medio se mueve 2 cm a un lado. ¿Llega luz a la pared?", "steps": ["El orificio del medio ya no está en la misma línea.", "La luz no se dobla para pasar.", "La tarjeta tapa el rayo."], "answer": "No llega luz a la pared; la luz viaja recta"},
    ],
    mistakes=[
        {"wrong": "Pensar que la luz da vueltas para pasar por un orificio desalineado.", "why": "Se cree que la luz puede doblarse cuando lo necesita.", "fix": "Si los orificios no están en línea recta, la luz no pasa."},
        {"wrong": "Dibujar el rayo de luz como una línea curva.", "why": "No se recuerda que la luz va recta.", "fix": "Dibuja siempre los rayos como líneas rectas con flecha."},
    ],
    tiers={
        "recovery": [
            ex("¿La luz viaja en línea recta o en curvas?", "En línea recta", "La luz no se dobla al viajar en el aire."),
            ex("¿Cómo se llama una línea fina de luz que viaja recta?", "Rayo", "Rayo de luz es una línea de luz."),
            ex("Completa: el camino que sigue la luz se llama ___.", "trayectoria", "Trayectoria es el camino de un movimiento."),
        ],
        "understand": [
            ex("¿Qué muestra el experimento de las tres tarjetas con orificios?", "Que la luz viaja en línea recta", "Solo pasa cuando los orificios están en línea recta."),
            ex("¿Por qué se forma una sombra detrás de un objeto?", "Porque el objeto tapa la luz que viaja recta", "Detrás del objeto no llega luz."),
            ex("¿Cómo se dibuja un rayo de luz?", "Como una línea recta con una flecha", "La flecha muestra hacia dónde va y la línea recta, que no se dobla."),
        ],
        "apply": [
            ex("Tres tarjetas alineadas tienen orificios a 10 cm de altura. Una cuarta tarjeta se pone al final con su orificio a 14 cm. ¿Pasa la luz por la cuarta?", "No", "Su orificio no está en la misma línea que los otros."),
            ex("Una linterna alumbra a un osito de peluche delante de una pared. ¿Qué forma tiene la sombra: de osito o de círculo?", "De osito", "La luz recta queda tapada por el contorno del peluche."),
            ex("Un rayo sale de una linterna hacia la pared. Se pone un libro delante de la luz. ¿Llega el rayo a la pared?", "No", "El libro tapa el rayo."),
        ],
        "reason": [
            ex("Beatriz dice: «La luz da una curva para pasar por el orificio movido». Según el experimento, ¿tiene razón?", "No", "Al mover el orificio la luz deja de pasar, por lo tanto no se dobla."),
            ex("La sombra de una silla en la pared tiene el contorno de la silla. ¿Qué característica de la luz lo explica: que viaja recta o que se separa en colores?", "Que viaja recta", "Si la luz se curvara, la sombra no tendría el contorno de la silla."),
        ],
        "challenge": [
            ex("Quieres que la luz de una linterna llegue a la pared pasando por un tubo de cartón. ¿El tubo debe estar recto o doblado?", "Recto", "La luz solo pasa si el tubo está alineado."),
            ex("Con tres tarjetas alineadas la luz pasa. Quieres que deje de pasar sin tapar ningún orificio. ¿Qué haces con la tarjeta del medio: la corres hacia un lado o la dejas igual?", "La corro hacia un lado", "Al desalinear los orificios se bloquea el rayo recto."),
        ],
    },
    context=[ex("En una pieza oscura, un niño ve que por un pequeño hueco de la persiana entra un rayo de luz y llega al piso en un punto. ¿Cómo es el camino de ese rayo desde la ventana hasta el piso?", "En línea recta", "La luz viaja recta desde el hueco hasta el piso.")],
    selfcheck=[
        ex("¿Qué forma tiene la trayectoria de la luz?", "Recta", "La luz no se dobla."),
        ex("¿Qué pasa si los tres orificios no están alineados?", "La luz no pasa", "El rayo recto choca con una tarjeta."),
        ex("¿Por qué una sombra tiene la forma del objeto?", "Porque el objeto tapa la luz recta", "Detrás no llega luz."),
    ],
    open_task=task(
        "Si puedes, arma tres tarjetas con orificio en fila y alúmbralas con una linterna en una pieza oscura: primero alineadas y luego con la del medio movida. Anota qué viste. Si no puedes, usa estos datos: alineadas, aparece un punto de luz en la pared; con la del medio 2 cm a un lado, no aparece ningún punto. Dibuja los dos casos con rayos y escribe tu conclusión.",
        "Alineadas, el rayo es recto y pasa. Movida, el rayo choca y no pasa. Conclusión: la luz viaja en línea recta.",
        ["dibuja los rayos como líneas rectas", "relaciona el resultado con la luz recta", "escribe una conclusión corta"],
        ["dos dibujos", "tabla de resultados", "frase de conclusión"],
        ["dibujar rayos curvos", "concluir que la luz se dobla"],
        "Valora la conclusión y pregunta qué pasaría si usara cuatro tarjetas alineadas.",
    ),
    reinforce="Haz sombras de tus manos con una linterna en la pared y dibuja cómo cambia la forma cuando acercas o alejas la mano.",
    extend="Mira cómo entra la luz por una ventana al amanecer y dibuja el rayo como una línea recta.",
)

register(
    OA9, 2,
    materials="Una linterna, una hoja de papel de cocina o papel vegetal, un trozo de cartón, una bolsa de plástico transparente y un libro. Una pared clara en una pieza oscura. No mires al haz de la linterna.",
    use="Aprenderé a comparar qué materiales dejan pasar la luz. Sirve para elegir materiales para ventanas, cortinas y paraguas.",
    prior=["Sé que la luz viaja en línea recta.", "Sé que una sombra aparece cuando algo tapa la luz."],
    explain=[
        "Los materiales se comportan distinto con la luz. Un material transparente deja pasar casi toda la luz y se ve claro lo que hay detrás. Ejemplos: el agua limpia y una bolsa de plástico transparente.",
        "Un material translúcido deja pasar una parte de la luz, pero no se ve claro lo que hay detrás. El papel vegetal es un ejemplo. Un material opaco no deja pasar la luz y forma una sombra bien oscura. Ejemplos: el cartón y la madera.",
        "Para investigarlo, pongo cada material delante de la linterna y miro la pared. Si la pared se ilumina fuerte, es transparente. Si se ilumina un poco, es translúcido. Si no se ilumina, es opaco. Siempre pruebo un material a la vez para comparar bien.",
    ],
    vocab=[("transparente", "deja pasar la luz y permite ver claro lo que hay detrás"), ("translúcido", "deja pasar parte de la luz, pero no se ve claro lo que hay detrás"), ("opaco", "no deja pasar la luz"), ("material", "de qué está hecho un objeto"), ("variable", "lo que cambio en un experimento, como el material")],
    worked=[
        {"title": "Cuatro materiales", "problem": "Con una linterna se prueba un cartón, papel vegetal, una bolsa transparente y un libro. El cartón y el libro no iluminan la pared; el papel ilumina un poco; la bolsa ilumina fuerte. Clasifícalos.", "steps": ["Cartón y libro: no dejan pasar luz.", "Papel vegetal: deja pasar un poco.", "Bolsa: deja pasar casi toda."], "answer": "Opacos: cartón y libro; translúcido: papel vegetal; transparente: bolsa"},
        {"title": "Cortinas", "problem": "Quieres que una pieza quede casi a oscuras para dormir. ¿Qué cortina eliges: de tela fina que deja ver la luz, de plástico transparente o de tela gruesa que no deja pasar luz?", "steps": ["Quiero que pase muy poca luz.", "El material opaco no deja pasar la luz.", "La tela gruesa es la más opaca."], "answer": "La tela gruesa, porque es opaca"},
    ],
    mistakes=[
        {"wrong": "Decir que el papel vegetal es opaco porque no se ve a través de él.", "why": "Se usa solo si se ve claro o no, sin mirar si pasa luz.", "fix": "Si deja pasar un poco de luz aunque no se vea claro, es translúcido."},
        {"wrong": "Pensar que un material opaco no tiene sombra.", "why": "Se cree que sombra es lo mismo que luz débil.", "fix": "El material opaco tapa la luz y forma la sombra más oscura."},
    ],
    tiers={
        "recovery": [
            ex("¿Un material opaco deja pasar la luz?", "No", "Opaco es lo que no deja pasar la luz."),
            ex("Pones un vidrio de ventana limpio entre tus ojos y un árbol. ¿Ves claro el árbol?", "Sí", "El vidrio limpio es transparente y deja pasar casi toda la luz."),
            ex("Completa: el papel vegetal deja pasar un poco de luz; es ___.", "translúcido", "Translúcido deja pasar parte de la luz."),
        ],
        "understand": [
            ex("¿Cuál es la diferencia entre translúcido y opaco?", "Translúcido deja pasar parte de la luz y opaco no deja pasar luz", "Una diferencia es cuánta luz pasa."),
            ex("¿Por qué el cartón forma una sombra oscura?", "Porque es opaco y tapa la luz", "No deja pasar la luz."),
            ex("¿Qué observas en la pared si pones un material transparente delante de la linterna?", "Se ilumina casi como sin material", "Pasa casi toda la luz."),
        ],
        "apply": [
            ex("Clasifica: agua limpia en un frasco de plástico transparente, una tabla de madera, papel vegetal. Responde en orden como transparente, opaco o translúcido.", "Transparente, opaco, translúcido", "El agua deja pasar la luz, la madera la tapa y el papel deja pasar parte."),
            ex("Pones un libro delante de la linterna y la pared queda sin luz. ¿Qué tipo de material es el libro?", "Opaco", "No deja pasar la luz."),
            ex("Quieres una ventana por la que se vea el patio. ¿Eliges material transparente, translúcido u opaco?", "Transparente", "Solo el transparente deja ver claro."),
        ],
        "reason": [
            ex("Los vidrios del baño dejan pasar luz, pero desde afuera no se ve quién está adentro. ¿Son transparentes o translúcidos?", "Translúcidos", "Dejan pasar luz sin que se vea claro."),
            ex("Mauro prueba un material y la pared queda un poco iluminada. Dice que es opaco. ¿Tiene razón?", "No", "Si deja pasar un poco de luz, es translúcido."),
        ],
        "challenge": [
            ex("Un paraguas debe tapar el Sol. ¿Debería ser de un material opaco o transparente?", "Opaco", "El opaco impide el paso de la luz."),
            ex("Para comparar cuánta luz deja pasar cada material, ¿qué debes mantener igual en cada prueba?", "La linterna y la distancia a la pared", "Así solo cambia el material."),
        ],
    },
    context=[ex("En un invernadero, el techo debe dejar pasar luz del Sol a las plantas y dejar ver hacia afuera. ¿Qué tipo de material conviene?", "Transparente", "Deja pasar casi toda la luz.")],
    selfcheck=[
        ex("¿Qué es un material opaco?", "El que no deja pasar la luz", "Opaco bloquea toda la luz."),
        ex("¿Un material translúcido deja pasar luz?", "Sí, una parte", "Pasa un poco de luz."),
        ex("¿Un material transparente deja ver claro lo que hay detrás?", "Sí", "Deja pasar casi toda la luz."),
    ],
    open_task=task(
        "Si puedes, prueba con una linterna delante de cada uno: cartón, papel vegetal o de cocina, bolsa transparente y un libro. Anota en una tabla si la pared se ilumina mucho, poco o nada. Si no puedes, usa estos datos: cartón, nada; papel de cocina, poco; bolsa transparente, mucho; libro, nada. Clasifica cada uno y escribe cuál serviría para una cortina de dormitorio.",
        "Cartón y libro: opacos. Papel de cocina: translúcido. Bolsa: transparente. Para dormir sirve el cartón o una tela opaca.",
        ["clasifica los cuatro materiales", "usa mucho, poco o nada como evidencia", "elige un material opaco para la cortina"],
        ["tabla con resultados", "frase de elección"],
        ["clasificar el papel de cocina como opaco", "no basar la clasificación en lo observado"],
        "Pide que explique en voz alta cómo decidió cada clasificación.",
    ),
    reinforce="Mira a través de tres materiales de tu casa y escribe si ves claro, borroso o nada.",
    extend="Cuenta a alguien de tu casa por qué un vidrio de baño deja pasar luz sin dejar ver claro.",
)

register(
    OA9, 3,
    materials="Una linterna, un espejo de mano, papel aluminio liso, el mismo papel aluminio arrugado, una pared clara y una pieza oscura. Nunca apuntes la luz reflejada a los ojos de nadie ni uses un espejo con el Sol.",
    use="Aprenderé que la luz rebota en las superficies y cómo cambia al rebotar. Sirve para entender los espejos y los reflectantes.",
    prior=["Sé que la luz viaja en línea recta.", "Sé que reflejar es hacer rebotar la luz."],
    explain=[
        "La reflexión de la luz ocurre cuando un rayo llega a una superficie y rebota. Si la superficie es lisa y brillante, como un espejo, el rayo sale en una sola dirección y se forma una imagen clara.",
        "El rayo que llega a un espejo inclinado hacia un lado sale inclinado hacia el otro lado. Si muevo el espejo, cambia el lugar de la pared donde llega la luz. Por eso un espejo sirve para enviar la luz a otro sitio.",
        "Una superficie arrugada, como el papel aluminio arrugado, también refleja la luz. Pero sus pliegues la mandan en muchas direcciones y no se ve una imagen clara. Por seguridad, la luz reflejada nunca se apunta a los ojos, y jamás se usa un espejo para reflejar el Sol.",
    ],
    vocab=[("reflexión", "cuando la luz rebota al llegar a una superficie"), ("superficie lisa", "superficie plana, sin arrugas ni bultos"), ("imagen", "lo que se ve reflejado en un espejo"), ("rebotar", "volver hacia atrás después de chocar"), ("pliegue", "arruga de una hoja o tela")],
    worked=[
        {"title": "Linterna y espejo", "problem": "Una linterna alumbra un espejo y la luz llega a un punto de la pared. Mueves el espejo un poco. ¿Qué pasa con el punto?", "steps": ["El espejo refleja el rayo.", "Al cambiar la inclinación del espejo cambia la dirección del rayo.", "El punto se mueve."], "answer": "El punto de luz cambia de lugar en la pared"},
        {"title": "Aluminio liso y arrugado", "problem": "En un papel aluminio liso se ve una imagen clara y en el arrugado no. ¿Por qué?", "steps": ["Los dos reflejan la luz.", "El liso manda la luz en una dirección.", "El arrugado la manda en muchas direcciones."], "answer": "El arrugado refleja en muchas direcciones y no forma imagen clara"},
    ],
    mistakes=[
        {"wrong": "Decir que el aluminio arrugado no refleja la luz.", "why": "No se forma imagen clara y parece que no refleja.", "fix": "Sí refleja, pero la luz sale en muchas direcciones."},
        {"wrong": "Usar un espejo para enviar la luz del Sol a los ojos de un amigo.", "why": "Se cree que es un juego inocente.", "fix": "Nunca apuntes luz reflejada a los ojos; puede encandilar y dañar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué le pasa a la luz cuando llega a un espejo?", "Rebota", "La luz se refleja."),
            ex("¿Una superficie lisa y brillante refleja la luz en una sola dirección?", "Sí", "Por eso forma una imagen clara."),
            ex("Completa: cuando la luz rebota en una superficie se llama ___.", "reflexión", "Reflexión es el rebote de la luz."),
        ],
        "understand": [
            ex("¿Por qué un espejo forma una imagen clara?", "Porque es liso y refleja la luz en una sola dirección", "Los rayos salen ordenados."),
            ex("¿Por qué el papel aluminio arrugado no forma una imagen clara?", "Porque los pliegues mandan la luz en muchas direcciones", "Los rayos salen desordenados."),
            ex("Si mueves un espejo que refleja la luz de una linterna, ¿qué cambia?", "El lugar donde llega la luz reflejada", "La dirección del rayo cambia con la inclinación."),
        ],
        "apply": [
            ex("Quieres que la luz de una linterna llegue al rincón derecho de una pieza oscura. ¿Qué haces con un espejo?", "Lo inclino hasta que la luz reflejada llegue al rincón", "Cambiando la inclinación cambio la dirección."),
            ex("Un rayo de linterna llega a un espejo y sale en otra dirección. ¿Cómo se llama a esto: reflexión o separación en colores?", "Reflexión", "El rayo rebotó en el espejo."),
            ex("Te ves clara en una bandeja metálica pulida y borrosa en otra muy rayada. ¿Cuál tiene la superficie más lisa?", "La pulida", "La superficie lisa refleja en una sola dirección y forma imagen clara."),
        ],
        "reason": [
            ex("Un papel blanco también refleja luz, pero no se ve tu cara en él. ¿Por qué?", "Porque su superficie no es lisa y refleja la luz en muchas direcciones", "Solo las superficies lisas forman imagen."),
            ex("Joaquín quiere jugar con un espejo y el Sol para molestar a un compañero. ¿Qué regla de seguridad rompe?", "No dirigir la luz reflejada a los ojos de nadie", "Puede dañar los ojos."),
        ],
        "challenge": [
            ex("Los ciclistas usan reflectantes en la ropa. ¿Por qué se ven de noche cuando un auto los ilumina?", "Porque reflejan la luz de los faros", "Devuelven la luz hacia el conductor."),
            ex("¿Cómo comprobarías que un espejo cambia la dirección de la luz?", "Muevo el espejo y veo que se mueve el punto de luz reflejado", "Si cambia el punto, cambió la dirección del rayo."),
        ],
    },
    context=[ex("Camila se mira en el espejo del baño y ve su cara clara. Luego mira el piso de cemento rugoso y no ve su cara. ¿Cuál superficie refleja la luz en una sola dirección?", "El espejo", "Su superficie es lisa.")],
    selfcheck=[
        ex("¿Qué es la reflexión de la luz?", "Que la luz rebota en una superficie", "Reflexión es rebote."),
        ex("¿Qué superficie forma imagen clara: lisa o arrugada?", "Lisa", "Refleja en una sola dirección."),
        ex("¿Se puede apuntar la luz reflejada a los ojos de alguien?", "No", "Puede dañar la vista."),
    ],
    open_task=task(
        "Si puedes, alumbra con una linterna en una pieza oscura un espejo y mueve el espejo para llevar el punto de luz a tres lugares de la pared. Prueba luego papel aluminio liso y arrugado. Si no puedes, usa estos datos: el espejo manda la luz a un punto pequeño; el aluminio liso manda un punto casi igual; el arrugado reparte la luz en manchas. Dibuja los rayos y escribe una conclusión.",
        "En el espejo el rayo rebota y forma un punto. En el aluminio arrugado el rayo se reparte en varias manchas. Conclusión: las superficies lisas reflejan en una dirección.",
        ["dibuja rayos rectos que rebotan", "compara liso y arrugado con datos", "escribe una conclusión"],
        ["dibujo de rayos", "tabla de resultados", "frase de conclusión"],
        ["afirmar que el arrugado no refleja", "no dibujar la dirección del rebote"],
        "Pide que explique por qué el punto se mueve cuando mueve el espejo.",
    ),
    reinforce="Mírate en una cuchara por el lado que se curva hacia adentro y por el otro, y anota cómo cambia lo que ves.",
    extend="Cuenta cuántos objetos reflectantes ves en la calle en tu camino al colegio.",
)

register(
    OA9, 4,
    materials="Un rociador de agua o una manguera con chorro fino, un día de Sol y un lugar al aire libre; opcionalmente un CD o DVD viejo y una ventana con luz del día. Siempre con el Sol a tu espalda y sin mirarlo.",
    use="Aprenderé que la luz blanca se puede separar en colores. Sirve para explicar el arcoíris.",
    prior=["Sé que la luz viaja recta y que se refleja.", "Sé que existen distintos colores."],
    explain=[
        "La luz blanca del Sol parece sin color, pero en realidad está formada por muchos colores mezclados. Cuando se separan, aparece el espectro de colores. Los colores pasan de uno a otro sin cortes, pero se acostumbra nombrar siete: rojo, anaranjado, amarillo, verde, azul, añil y violeta.",
        "El arcoíris se produce cuando la luz del Sol atraviesa gotas de agua de la lluvia o del rocío. Las gotas separan la luz en colores. Para verlo hay que tener el Sol a la espalda y las gotas de agua enfrente. En un arcoíris, el rojo queda en el borde de arriba y el violeta en el de abajo.",
        "Puedo repetirlo en casa. Con el Sol a mi espalda, rocío agua en gotas finas frente a mí. También puedo mirar un CD con la luz de una ventana. Nunca miro al Sol ni dirijo su luz a los ojos. Solo miro los colores que aparecen en las gotas o en el CD.",
    ],
    vocab=[("espectro", "conjunto de colores en que se separa la luz blanca"), ("arcoíris", "arco de colores que se forma con Sol y gotas de agua"), ("gota", "porción pequeña de agua en forma de esfera"), ("mezclado", "unido a otras cosas"), ("separar", "dividir algo en sus partes")],
    worked=[
        {"title": "Dónde pararse para ver un arcoíris", "problem": "Llueve frente a ti y el Sol brilla detrás de ti. ¿Podrás ver un arcoíris?", "steps": ["El Sol debe estar a mi espalda.", "Las gotas de lluvia deben estar frente a mí.", "Se cumplen las dos condiciones."], "answer": "Sí, puedes ver un arcoíris"},
        {"title": "Contar los colores", "problem": "¿Cuántos colores tiene el espectro que se nombra en este cuaderno?", "steps": ["Los nombro: rojo, anaranjado, amarillo, verde, azul, añil, violeta.", "Cuento uno por uno.", "Son siete."], "answer": "7 colores"},
    ],
    mistakes=[
        {"wrong": "Pensar que el arcoíris es un objeto que está en un lugar fijo.", "why": "Se ve como una cosa concreta en el cielo.", "fix": "Se forma con el Sol y las gotas, y depende de dónde esté la persona."},
        {"wrong": "Mirar al Sol para encontrar el arcoíris.", "why": "Se piensa que hay que mirar donde está la luz.", "fix": "Mira hacia las gotas con el Sol a tu espalda; nunca mires al Sol."},
    ],
    tiers={
        "recovery": [
            ex("¿La luz blanca del Sol está formada por muchos colores?", "Sí", "Se puede separar en un espectro."),
            ex("Para ver un arcoíris se necesitan gotas de agua y otra cosa. ¿Qué fuente de luz es?", "El Sol", "La luz del Sol se separa en colores en las gotas."),
            ex("Completa: el conjunto de colores en que se separa la luz se llama ___.", "espectro", "Espectro es el conjunto de colores."),
        ],
        "understand": [
            ex("¿Cómo se forma un arcoíris?", "La luz del Sol atraviesa gotas de agua y se separa en colores", "Las gotas hacen que se vean los colores."),
            ex("¿Dónde debe estar el Sol cuando quieres ver un arcoíris?", "A tu espalda", "Para mirar las gotas con la luz que llega por detrás."),
            ex("¿Por qué no hay que mirar al Sol?", "Porque daña los ojos", "El Sol es muy fuerte."),
        ],
        "apply": [
            arith("El espectro que nombramos tiene 7 colores. Ya pintaste rojo, anaranjado y amarillo. ¿Cuántos colores te faltan por pintar?", "7-3", "De los 7 colores ya pintaste 3.", " colores"),
            ex("En el espectro hay estos colores: rojo, anaranjado, amarillo, verde, azul, añil, violeta. ¿Cuál queda después del azul?", "Añil", "El orden es rojo, anaranjado, amarillo, verde, azul, añil, violeta."),
            ex("Un niño rocía agua fina con el Sol detrás de él y ve colores. ¿Qué hizo la luz del Sol al pasar por las gotas?", "Se separó en colores", "Las gotas descompusieron la luz blanca."),
        ],
        "reason": [
            ex("Aldo mira una lluvia fina con el Sol a su espalda. Carla mira la misma lluvia con el Sol de frente. ¿Quién puede ver el arcoíris sin mirar al Sol?", "Aldo", "Mira las gotas con el Sol a su espalda."),
            ex("Sandra dice que el arcoíris existe aunque no haya Sol. ¿Es cierto?", "No", "Sin la luz del Sol no se separa la luz en colores."),
        ],
        "challenge": [
            ex("En un CD sostenido junto a una ventana ves bandas de colores. ¿Qué conclusión puedes sacar sobre la luz blanca?", "Que está formada por colores que se pueden separar", "El CD separa la luz blanca de la ventana."),
            ex("En un arcoíris, ¿el rojo está en el borde de arriba o en el de abajo?", "En el borde de arriba", "El rojo queda arriba y el violeta abajo."),
        ],
    },
    context=[ex("Después de llover, sale el Sol y Matías ve un arcoíris. ¿Qué dos cosas hay en el cielo que permiten verlo?", "El Sol y las gotas de agua", "La luz solar se separa al pasar por las gotas.")],
    selfcheck=[
        ex("¿Cuántos colores nombra el espectro de este cuaderno?", "7", "Rojo, anaranjado, amarillo, verde, azul, añil y violeta."),
        ex("¿Qué separa la luz del Sol en el arcoíris?", "Las gotas de agua", "La luz cambia al pasar por ellas."),
        ex("¿Se puede mirar el Sol para buscar el arcoíris?", "No", "Daña los ojos."),
    ],
    open_task=task(
        "Dibuja un arcoíris con sus siete colores en orden, con el rojo arriba. Luego dibuja una escena que muestre dónde están el Sol, las gotas de agua y la persona que lo mira. Si puedes, rocía agua fina con el Sol a tu espalda y anota los colores que ves.",
        "Mi arcoíris tiene rojo arriba y violeta abajo. En mi escena el Sol está detrás de la niña y las gotas están delante.",
        ["coloca los siete colores en orden", "ubica el Sol detrás de la persona", "señala las gotas de agua"],
        ["dibujo del arcoíris", "dibujo de la escena", "frase explicativa"],
        ["poner al Sol delante de la persona mirándolo", "olvidar las gotas de agua"],
        "Valora el orden de los colores y pregunta qué pasaría sin gotas de agua.",
    ),
    reinforce="Escribe los siete colores en orden y repítelos hasta decirlos sin mirar.",
    extend="Pregunta en tu casa si alguien recuerda haber visto un arcoíris y cómo estaba el cielo.",
)

register(
    OA9, 5,
    materials="Lápiz y papel. Los datos de cada situación están escritos en el cuaderno. Si quieres repetir un experimento, usa una linterna y objetos de tu casa sin mirar el haz.",
    use="Aprenderé a escribir una explicación sobre la luz apoyándome en datos. Sirve para que mis conclusiones tengan pruebas.",
    prior=["Sé que la luz viaja recta, se refleja y se separa en colores.", "Sé clasificar materiales como opacos, translúcidos y transparentes."],
    explain=[
        "Una explicación científica tiene tres partes: una afirmación, una evidencia y una razón. La afirmación dice lo que concluyo. La evidencia son los datos que observé. La razón explica por qué esos datos apoyan mi afirmación.",
        "Por ejemplo: «La luz viaja en línea recta» es la afirmación. La evidencia es que con las tarjetas alineadas la luz pasó y con una movida no pasó. La razón es que, si la luz pudiera doblarse, habría pasado también por la tarjeta movida.",
        "Una buena explicación usa datos del experimento, no solo opiniones. Además, debo decir qué se mantuvo igual en las pruebas, como la linterna y la distancia. Así sé que el cambio se debe al material, a la posición o a la superficie que cambié.",
    ],
    vocab=[("afirmación", "lo que concluyo después de investigar"), ("evidencia", "datos u observaciones que apoyan una afirmación"), ("razón", "explicación de por qué la evidencia apoya la afirmación"), ("dato", "información que se anota al observar o medir"), ("conclusión", "lo que se aprende de los datos")],
    worked=[
        {"title": "Explicar con datos", "problem": "Datos: cartón, la pared queda sin luz; papel vegetal, queda un poco de luz; bolsa transparente, queda mucha luz. Escribe una afirmación con evidencia.", "steps": ["Afirmación: los materiales dejan pasar distinta cantidad de luz.", "Evidencia: cartón nada, papel poco, bolsa mucha.", "Razón: la cantidad de luz que llega a la pared depende del material."], "answer": "Los materiales dejan pasar distinta cantidad de luz, según el material"},
        {"title": "Elegir la afirmación que sí apoyan los datos", "problem": "Datos: el espejo manda la luz a un punto; el aluminio arrugado la reparte en manchas. ¿Qué afirmación apoyan: «las superficies lisas reflejan en una dirección» o «el aluminio no refleja»?", "steps": ["Miro la evidencia: el arrugado sí manda luz.", "La primera afirmación coincide con el espejo.", "La segunda contradice los datos."], "answer": "Las superficies lisas reflejan en una dirección"},
    ],
    mistakes=[
        {"wrong": "Dar una conclusión sin ningún dato.", "why": "Se cree que basta con opinar.", "fix": "Cita la medición u observación que apoya la conclusión."},
        {"wrong": "Concluir algo que los datos no muestran.", "why": "Se generaliza más de lo observado.", "fix": "Di solo lo que los datos permiten afirmar."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llaman los datos que apoyan una afirmación?", "Evidencia", "Evidencia son los datos u observaciones."),
            ex("¿Qué dice la afirmación de una explicación científica?", "Lo que concluyo", "La afirmación resume la conclusión."),
            ex("Completa: la ___ explica por qué la evidencia apoya la afirmación.", "razón", "La razón conecta la evidencia con la afirmación."),
        ],
        "understand": [
            ex("¿Por qué una explicación necesita evidencia?", "Para mostrar que la conclusión viene de los datos", "Sin datos solo hay una opinión."),
            ex("Datos: tarjetas alineadas, pasa la luz; tarjeta movida, no pasa. ¿Qué afirmación apoyan?", "La luz viaja en línea recta", "Solo pasa si hay una línea recta."),
            ex("¿Por qué hay que mantener igual la linterna y la distancia en todas las pruebas?", "Para que el cambio se deba solo a lo que se modificó", "Si cambian varias cosas no se sabe cuál causó el resultado."),
        ],
        "apply": [
            ex("Datos: espejo plano, un punto claro en la pared; aluminio arrugado, tres manchas pequeñas. ¿Qué afirmación apoyan: «las superficies lisas y arrugadas reflejan la luz de forma distinta» o «el aluminio arrugado no refleja»?", "Las superficies lisas y arrugadas reflejan la luz de forma distinta", "El aluminio arrugado sí mandó luz, pero repartida en manchas."),
            ex("Datos de tres vasos: A deja ver claro la mano detrás; B deja ver una mancha borrosa; C no deja ver nada. ¿Qué vaso es translúcido?", "B", "Deja pasar luz pero no deja ver claro."),
            ex("Datos: se rocía agua con el Sol a la espalda y se ven colores; sin Sol no se ven. ¿Qué afirmación apoyan?", "Se necesita luz del Sol y gotas de agua para ver colores", "Sin el Sol no hubo colores."),
        ],
        "reason": [
            ex("Dos niños prueban si una hoja deja pasar luz. Uno usa una linterna a 10 cm y el otro otra linterna a 1 m. ¿Se puede comparar bien sus resultados?", "No", "Cambiaron la fuente y la distancia."),
            ex("Un niño dice que todos los materiales de plástico son transparentes porque probó uno. ¿Es suficiente un solo dato?", "No", "Un solo caso no prueba una afirmación general."),
        ],
        "challenge": [
            ex("Un estudiante escribe: «La luz viaja recta porque sí». Mejora su explicación: ¿qué evidencia del experimento de las tarjetas puede agregar?", "Con tres tarjetas alineadas la luz pasó y con una movida no", "Esa evidencia muestra que la luz no se dobla."),
            ex("Datos: papel vegetal deja pasar un poco de luz, cartón nada. Un compañero dice que el papel vegetal es opaco. Responde con evidencia.", "No, porque deja pasar un poco de luz", "Opaco es lo que no deja pasar nada de luz."),
        ],
    },
    context=[ex("Para decidir qué material usar en una lámpara de papel que dé luz suave, Rosa probó papel de cocina (pasa poca luz), cartón (no pasa) y plástico transparente (pasa casi toda). ¿Cuál elige y qué evidencia usa?", "El papel de cocina, porque deja pasar poca luz", "Es translúcido y suaviza la luz.")],
    selfcheck=[
        ex("¿Qué tres partes tiene una explicación científica?", "Afirmación, evidencia y razón", "Cada parte cumple un papel."),
        ex("¿Una conclusión puede basarse solo en una opinión?", "No", "Necesita datos que la apoyen."),
        ex("¿Qué debe mantenerse igual en las pruebas para comparar justo?", "Las condiciones que no cambié", "Así solo cambia lo que quiero estudiar."),
    ],
    open_task=task(
        "Usa estos datos de un experimento: luz de linterna, cartón: 0 de 10 de luz en la pared; papel de cocina: 4 de 10; bolsa transparente: 9 de 10. Escribe una explicación con afirmación, evidencia y razón, y di qué se mantuvo igual.",
        "Afirmación: el material cambia cuánta luz pasa. Evidencia: cartón 0, papel de cocina 4, bolsa 9. Razón: el cartón es opaco, el papel translúcido y la bolsa transparente. Se mantuvo igual la linterna y la distancia.",
        ["escribe afirmación, evidencia y razón", "cita al menos dos datos", "nombra algo que se mantuvo igual"],
        ["explicación escrita", "tabla copiada"],
        ["concluir sin citar datos", "olvidar lo que se mantuvo igual"],
        "Pide que lea su explicación y cambie una palabra por otra más precisa del vocabulario.",
    ),
    reinforce="Elige un experimento de la luz de esta unidad y explícalo en voz alta con afirmación, evidencia y razón.",
    extend="Anota en un cuaderno una duda sobre la luz que no se pudo resolver con los datos y cómo la investigarías.",
)

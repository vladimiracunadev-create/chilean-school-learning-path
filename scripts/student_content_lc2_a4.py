"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 12 (eventos socioculturales y ceremoniales: convenciones, momentos y espacios) y
OA 13 (valores sociocomunitarios: reciprocidad, respeto y ayuda mutua).

Criterio de autoría: las invitaciones, las comunidades y las personas de los casos son inventadas. Nunca se
describe, se simula ni se pide reproducir una ceremonia; solo se enseña a reconocer momentos, espacios y
convenciones de convivencia. No se nombra ningún evento ceremonial real ni su fecha; el único evento real es el feriado nacional Día Nacional
de los Pueblos Indígenas (cerca del 21 de junio). Las palabras «ayni» y «minga» se presentan «según fuentes
publicadas» y quedan marcadas para revisión por especialista y por la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12, OA13 = "LC02 OA 12", "LC02 OA 13"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No simular ceremonias."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


INVITA = "Invitación inventada: «Fiesta de la cosecha de Valle Alto. Cuándo: un sábado de otoño. Dónde: la plaza del pueblo. Cómo participar: llegar con una comida para compartir, saludar a los mayores, guardar silencio durante el canto de apertura y pedir permiso antes de sacar fotos.»"

# ============================================================ OA 12 · Eventos socioculturales y ceremoniales
L(
    OA12, 1,
    materials="Lápiz y hojas. La invitación y los ejemplos están escritos aquí; son inventados salvo los señalados como fuentes publicadas.",
    use="Aprenderé qué es un evento sociocultural y uno ceremonial, y que cada uno tiene su momento, su espacio y sus reglas. Sirve para saber cómo comportarse si te invitan.",
    prior=["Sé qué es una comunidad.", "Sé que una ficha tiene una fuente."],
    explain=[
        "Un evento sociocultural es un encuentro de una comunidad, como una fiesta, una feria o una reunión de familias. Un evento ceremonial es una ceremonia que tiene un sentido especial para el pueblo. Algunos eventos son abiertos a todos y otros solo son para quienes la comunidad invita.",
        "Todo evento tiene un momento, un espacio y convenciones. El momento es cuándo ocurre, por ejemplo un mes del año. El espacio es dónde se hace, como una plaza o un lugar de la comunidad. Las convenciones son las reglas de comportamiento: cómo saludar, cuándo callar y qué se puede fotografiar.",
        "Cada pueblo y cada comunidad tiene sus propios eventos, con sus propios momentos, espacios y reglas. Cuáles son, cuándo se hacen y cómo se participa lo dicen el educador tradicional y la comunidad. Nosotros no los adivinamos ni los inventamos. Por eso aquí usamos eventos inventados para practicar.",
    ],
    vocab=[("evento sociocultural", "encuentro de una comunidad, como una fiesta o una feria"), ("evento ceremonial", "ceremonia con un sentido especial para un pueblo"), ("momento", "cuándo ocurre un evento"), ("espacio", "dónde ocurre un evento"), ("convención", "regla de comportamiento que todos respetan")],
    worked=[
        W("Leer una invitación", INVITA + " ¿Cuándo y dónde es?", ["Busco el cuándo: un sábado de otoño.", "Busco el dónde: la plaza del pueblo.", "Escribo las dos respuestas."], "Un sábado de otoño en la plaza del pueblo."),
        W("Encontrar una convención", INVITA + " Nombra una regla de comportamiento.", ["Una convención es una regla.", "Leo: guardar silencio durante el canto de apertura.", "Esa es una convención."], "Guardar silencio durante el canto de apertura"),
    ],
    mistakes=[
        M("Pensar que todos los eventos son abiertos a todos.", "Algunos son solo para quienes la comunidad invita.", "Pregunta si puedes ir y acepta la respuesta."),
        M("Llegar a un evento sin saber las reglas.", "Puedes faltar al respeto sin querer.", "Pregunta cómo participar antes de ir."),
    ],
    R=[
        ex("Una fiesta de la comunidad es un evento sociocultural. ¿Verdadero o falso?", "Verdadero", "Es un encuentro de la comunidad."),
        ex("El momento de un evento es cuándo ocurre. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ex("El espacio de un evento es dónde se hace. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("Verdadero o falso: todos los eventos son abiertos a todos.", "Falso", "Algunos son solo para quienes la comunidad invita."),
        ex("¿Qué es una convención? A) Una regla de comportamiento B) Un tipo de comida", "A", "Es una regla que todos respetan."),
        ex(INVITA + " ¿En qué estación es la fiesta? A) Otoño B) Verano", "A", "La invitación dice que es un sábado de otoño."),
    ],
    A=[
        ex(INVITA + " ¿Qué debes llevar para participar?", "Una comida para compartir", "La invitación lo pide."),
        ex(INVITA + " Une dato y tipo. 1) un sábado de otoño 2) la plaza del pueblo 3) guardar silencio. a) espacio b) convención c) momento", "1-c, 2-a, 3-b", "Cada dato responde cuándo, dónde y cómo."),
        ex("Invitación inventada de Bahía Clara: «Feria del mar. Cuándo: un domingo de verano. Dónde: la playa. Cómo participar: llegar temprano y no tocar los botes sin permiso». Une dato y tipo. 1) un domingo de verano 2) la playa 3) no tocar los botes sin permiso. a) espacio b) convención c) momento", "1-c, 2-a, 3-b", "Cada dato responde cuándo, dónde y cómo."),
    ],
    Z=[
        ex("Pedro dice: «Si me invitan a un evento no necesito saber las reglas». ¿Qué le dirías?", "Que debe preguntar cómo participar", "Las convenciones cuidan el respeto."),
        ex("Ema dice que todos los eventos de todos los pueblos son iguales y se hacen en las mismas fechas. ¿Qué le responderías?", "Que cada pueblo y cada comunidad tiene sus propios eventos y fechas", "Esos datos los dice cada comunidad."),
    ],
    D=[
        ex("Una invitación dice «Ceremonia solo para la comunidad». ¿Puedes ir sin que te inviten? Responde Sí o No.", "No", "Es solo para quienes la comunidad invita."),
        ex("Dos invitaciones: una pide silencio al inicio y otra pide cantar fuerte. ¿Debes seguir las mismas reglas en las dos? Responde Sí o No.", "No", "Cada evento tiene sus propias convenciones."),
    ],
    context=[ex("Tu curso recibe la invitación de Valle Alto. Lía quiere sacar fotos de todo apenas llegue. ¿Qué debe hacer primero? A) Pedir permiso B) Sacar fotos igual", "A", "La invitación pide permiso antes de sacar fotos.")],
    selfcheck=[ex("Nombra las tres partes que tiene todo evento.", "Momento, espacio y convenciones", "Son las tres ideas de la clase."), ex("¿Qué haces si no sabes cómo participar?", "Pregunto", "Preguntar evita faltar al respeto."), ex("Verdadero o falso: algunos eventos son solo para quienes invita la comunidad.", "Verdadero", "Hay eventos abiertos y otros restringidos.")],
    task=T("Lee la invitación inventada de Valle Alto que está en esta clase. Haz una tabla con tres columnas: cuándo, dónde y reglas. Escribe los datos que da la invitación. Luego escribe una pregunta que le harías a la comunidad para participar con respeto. No dibujes ceremonias ni símbolos sagrados.",
           "Cuándo: un sábado de otoño. Dónde: la plaza del pueblo. Reglas: llevar comida, saludar, guardar silencio, pedir permiso para fotos. Pregunta: ¿cómo debemos saludar a los mayores?",
           ["completa las tres columnas", "usa solo datos de la invitación", "formula una pregunta respetuosa"], ["tabla", "pregunta"], ["inventar reglas", "dibujar ceremonias"],
           "Verificar los datos con la invitación."),
    reinforce="Subraya en la invitación el momento, el espacio y una regla con tres colores.",
    extend="Escribe una pregunta sobre un evento de tu zona para el educador tradicional.",
)

L(
    OA12, 2,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé por qué los eventos tienen reglas y cómo cada una cuida a las personas y a la comunidad. Sirve para saber qué hacer cuando te invitan.",
    prior=["Sé que todo evento tiene momento, espacio y convenciones.", "Sé que algunos eventos son restringidos."],
    explain=[
        "Las convenciones de un evento cuidan el respeto. Saludar a los mayores muestra reconocimiento. Guardar silencio en ciertos momentos permite escuchar. Llevar comida para compartir expresa reciprocidad. Pedir permiso antes de sacar fotos respeta la privacidad.",
        "Algunos eventos tienen un espacio especial. Ese espacio puede tener normas: dónde sentarse, por dónde entrar o qué no tocar. Si no sabes, esperas y observas. Preguntar antes siempre es mejor que equivocarse.",
        "Algunos momentos de un evento no se fotografían ni se graban. La comunidad decide qué se puede compartir. Después del evento tampoco se publica nada sin permiso. Y es importante agradecer a quienes te recibieron.",
    ],
    vocab=[("reconocimiento", "valorar a una persona por su lugar y su saber"), ("privacidad", "lo que cada persona o comunidad decide no mostrar"), ("norma", "regla que se debe cumplir"), ("observar", "mirar con atención antes de actuar"), ("agradecer", "mostrar que valoras lo recibido")],
    worked=[
        W("Por qué existe la regla", "Una regla pide guardar silencio durante el canto de apertura. ¿Para qué sirve?", ["Callar permite escuchar.", "Así se respeta a quienes cantan.", "Sirve para escuchar y respetar."], "Para escuchar y respetar a quienes cantan"),
        W("Qué hacer si no sé", "Llegas a un espacio de práctica y no sabes dónde sentarte. ¿Qué haces: te sientas en cualquier parte o esperas y observas?", ["No conozco la norma del lugar.", "Esperar y observar evita equivocarme.", "Puedo preguntar con voz baja."], "Espero, observo y pregunto"),
    ],
    mistakes=[
        M("Sentarse en el primer lugar libre sin preguntar.", "Puede ser un lugar reservado.", "Espera que te indiquen."),
        M("Publicar fotos del evento sin permiso.", "La comunidad decide qué se muestra.", "Pregunta antes y acepta la respuesta."),
    ],
    R=[
        ex("Saludar a los mayores es una forma de respeto. ¿Verdadero o falso?", "Verdadero", "Saludar muestra reconocimiento."),
        ex("Si no sabes dónde sentarte, ¿esperas o te sientas en cualquier lugar?", "Espero", "Así evitas equivocarte."),
        ex("Llevar comida para compartir expresa reciprocidad. ¿Verdadero o falso?", "Verdadero", "Compartir es devolver."),
    ],
    C=[
        ex("¿Para qué sirve guardar silencio? A) Para escuchar B) Para dormir", "A", "El silencio permite escuchar."),
        ex("Verdadero o falso: después de un evento se pueden publicar todas las fotos sin permiso.", "Falso", "La comunidad decide qué se publica."),
        ex("¿Qué haces después de que te recibieron? A) Agradezco B) Me voy sin decir nada", "A", "Agradecer es una forma de respeto."),
    ],
    A=[
        ex("Une regla y razón. 1) guardar silencio 2) saludar a los mayores 3) pedir permiso para fotos. a) respetar la privacidad b) escuchar c) reconocer a los mayores", "1-b, 2-c, 3-a", "Cada regla cuida un valor."),
        ex(INVITA + " ¿Cuántas reglas de comportamiento nombra la invitación (llevar comida, saludar, silencio y fotos)?", "4", "Se cuentan las cuatro."),
        ex("Marca solo lo respetuoso en un evento: a) saludar b) gritar c) esperar indicaciones d) tocar objetos sin preguntar.", "a y c", "Saludar y esperar son respetuosos."),
    ],
    Z=[
        ex("Tomás dice: «Las reglas de los eventos no sirven». ¿Qué le responderías?", "Que cuidan el respeto y el sentido del evento", "Cada regla protege algo importante."),
        ex("Lía quiere grabar un canto sin preguntar porque «es lindo». ¿Qué error comete?", "No pidió permiso", "Hay momentos que no se graban."),
    ],
    D=[
        ex("Un evento tiene tres reglas: silencio, saludo y no fotos. Un niño rompe una. ¿Cuántas reglas siguen vigentes para los demás?", "3", "Las tres reglas siguen valiendo."),
        ex("Una comunidad pide que no se publique un video de su evento. Un visitante lo sube igual. ¿Qué principio rompió?", "El respeto a la decisión de la comunidad", "La comunidad decide qué se comparte."),
    ],
    context=[ex("En la fiesta de Valle Alto, Mateo se sienta en un banco que parece libre. Una abuela le dice que es para los mayores. ¿Qué hace Mateo? A) Se cambia y agradece B) Se queda sentado", "A", "Respeta la indicación.")],
    selfcheck=[ex("Escribe dos reglas de un evento.", "Saludar y pedir permiso para fotos", "Son ejemplos de la clase."), ex("¿Qué haces si no sabes una regla?", "Observo y pregunto", "Así evitas equivocarte."), ex("Verdadero o falso: la comunidad decide qué se puede fotografiar.", "Verdadero", "Es parte de su privacidad.")],
    task=T("Crea una guía de visita de una página para un evento inventado de Valle Alto. Escribe cinco reglas con su razón, por ejemplo guardar silencio para escuchar. Dibuja un cartel con la regla más importante. No dibujes ceremonias ni símbolos sagrados.",
           "1. Saludar a los mayores: reconocimiento. 2. Guardar silencio: escuchar. 3. Llevar comida: compartir. 4. Pedir permiso para fotos: respeto. 5. Agradecer al final. Cartel: «Pedimos permiso».",
           ["escribe cinco reglas", "da la razón de cada una", "no dibuja ceremonias"], ["guía", "cartel"], ["reglas sin razón", "dibujar ceremonias"],
           "Revisar que cada regla tenga su razón."),
    reinforce="Elige dos reglas y explica a un adulto por qué existen.",
    extend="Escribe una regla más que cuide la privacidad de una comunidad.",
)

L(
    OA12, 3,
    materials="Lápiz y hojas. Los calendarios son simples y están escritos aquí.",
    use="Aprenderé que los eventos de los pueblos originarios siguen celebrándose hoy y que se organizan en el año. Sirve para reconocer su presente y ubicarlos en el calendario.",
    prior=["Sé los meses del año.", "Sé que hay eventos con reglas."],
    explain=[
        "Los eventos de los pueblos originarios no son solo del pasado. Se celebran hoy y participan niños, jóvenes y mayores. Algunos han cambiado en la forma de organizarse, pero siguen reuniendo a las comunidades.",
        "Los eventos se ubican en el calendario. Cada comunidad dice cuándo hace los suyos. En este cuaderno usamos un calendario inventado de Valle Alto: la feria de verano en enero y la fiesta de la cosecha en abril. Un evento nacional que sí conocemos es el Día Nacional de los Pueblos Indígenas, cerca del 21 de junio, cuando empieza el invierno en Chile.",
        "Para conocerlos con respeto, usamos fuentes de hoy: educadores tradicionales, comunidades, sitios oficiales y libros nuevos. Recordamos que cada comunidad vive el evento a su manera. Y no confundimos un evento con otro ni con una fiesta de otro tipo.",
    ],
    vocab=[("calendario", "organización de los días y meses del año"), ("celebrar", "hacer una fiesta o ceremonia por algo importante"), ("presente", "lo que ocurre hoy"), ("organizar", "preparar algo entre varias personas"), ("reunir", "juntar a las personas")],
    worked=[
        W("Ubicar en el calendario", "Enero es el mes 1 y abril es el mes 4. En el calendario inventado de Valle Alto, ¿cuántos meses pasan entre la feria de verano (enero) y la fiesta de la cosecha (abril)?", ["Resto 4 − 1.", "4 − 1 = 3.", "Pasan 3 meses."], "3 meses"),
        W("Seguir celebrándose", "Caso inventado: «La fiesta de Valle Alto se hace cada otoño, y hoy los jóvenes ayudan a organizarla». ¿Es una fiesta del pasado o del presente?", ["Dice cada otoño y hoy.", "Los jóvenes ayudan ahora.", "Es del presente."], "Del presente"),
    ],
    mistakes=[
        M("Pensar que los eventos de los pueblos originarios ya no se celebran.", "Se celebran hoy con la participación de personas actuales.", "Busca fuentes de hoy."),
        M("Confundir fechas de eventos distintos.", "Cada evento tiene su momento.", "Anota la fecha con su fuente."),
    ],
    R=[
        ex("En el calendario inventado de Valle Alto, la feria de verano es en enero. ¿Verdadero o falso?", "Verdadero", "Es el dato de la clase."),
        ex("El Día Nacional de los Pueblos Indígenas es cerca del 21 de junio. ¿Verdadero o falso?", "Verdadero", "Es el dato de la clase."),
        ex("Los eventos de los pueblos originarios se celebran hoy. ¿Verdadero o falso?", "Verdadero", "Participan personas actuales."),
    ],
    C=[
        ex("Verdadero o falso: los eventos de los pueblos originarios son solo del pasado.", "Falso", "Se celebran hoy."),
        ex("¿Qué estación empieza en Chile cerca del 21 de junio? A) Invierno B) Verano", "A", "En el hemisferio sur junio es de invierno."),
        ex("Para conocer un evento con respeto, ¿qué usas? A) Fuentes de hoy B) Suposiciones", "A", "Las fuentes dan datos claros."),
    ],
    A=[
        arith("Si enero es el mes 1 y abril el mes 4, ¿cuántos meses hay entre enero y abril?", "4-1", "Se restan los números de los meses.", " meses"),
        ex("Ordena de primero a último en el año: fiesta de la cosecha (abril), feria de verano (enero), Día Nacional de los Pueblos Indígenas (cerca del 21 de junio). ¿Cuál es el primero?", "La feria de verano", "Enero viene antes que abril y que junio."),
        ex("Une evento y momento. 1) feria de verano de Valle Alto 2) fiesta de la cosecha de Valle Alto 3) Día Nacional de los Pueblos Indígenas. a) cerca del 21 de junio b) abril c) enero", "1-c, 2-b, 3-a", "Cada evento tiene su momento."),
    ],
    Z=[
        ex("Rosa dice: «Todos los eventos de los pueblos originarios son en el mismo mes». ¿Qué le responderías?", "Que cada comunidad dice cuándo hace los suyos; en el calendario de Valle Alto hay uno en enero y otro en abril", "Los eventos tienen momentos distintos."),
        ex("Pedro dice: «Esa fiesta ya no se hace». Ana muestra un afiche de este año. ¿Quién tiene razón?", "Ana", "El afiche de este año muestra que se hace hoy."),
    ],
    D=[
        arith("Un calendario de práctica marca 2 eventos en junio y 1 en enero. ¿Cuántos eventos hay en total?", "2+1", "Se suman los eventos de los dos meses.", " eventos"),
        ex("Una escuela organiza un acto por el Día Nacional de los Pueblos Indígenas. ¿Qué fuente de hoy puede usar? A) Un educador tradicional B) Una película de dibujos", "A", "El educador es una fuente actual y confiable."),
    ],
    context=[ex("El curso arma el calendario inventado de Valle Alto. Lía pone la fiesta de la cosecha en junio. ¿Está bien?", "No, es en abril", "El calendario de la clase dice que es en abril.")],
    selfcheck=[ex("Nombra dos eventos del calendario de Valle Alto y su mes.", "Feria de verano en enero y fiesta de la cosecha en abril", "Son los datos de la clase."), ex("¿Por qué decimos que los eventos son del presente?", "Porque se celebran hoy", "Participan personas actuales."), ex("Verdadero o falso: todas las comunidades viven los eventos igual.", "Falso", "Cada comunidad lo vive a su manera.")],
    task=T("Dibuja un calendario de práctica con los meses de enero a junio. Marca en enero la feria de verano de Valle Alto, en abril la fiesta de la cosecha y cerca del 21 de junio el Día Nacional de los Pueblos Indígenas. Escribe cuántos meses hay entre enero y abril. No dibujes ceremonias ni símbolos sagrados.",
           "Calendario de enero a junio. Enero: feria de verano. Abril: fiesta de la cosecha. Junio: Día Nacional de los Pueblos Indígenas. Hay 3 meses entre enero y abril.",
           ["ubica bien los eventos", "calcula los meses", "no dibuja ceremonias"], ["calendario", "número"], ["ubicar mal los eventos", "dibujar ceremonias"],
           "Verificar con los datos de la clase."),
    reinforce="Escribe los meses de enero a junio en orden.",
    extend="Escribe una pregunta sobre un evento de tu zona para el educador tradicional.",
)

L(
    OA12, 4,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé cómo participar de forma respetuosa en un evento o aprender de él sin simularlo. Sirve para valorar las ceremonias y no usarlas como espectáculo.",
    prior=["Sé que los eventos tienen convenciones.", "Sé que algunos son restringidos."],
    explain=[
        "Las ceremonias tienen un sentido especial para sus comunidades. Por eso no las simulamos en clase ni las convertimos en juego o en espectáculo. Si queremos aprender, escuchamos a una persona de la comunidad que nos cuente lo que ella quiera compartir.",
        "Podemos participar de otras formas respetuosas. Podemos leer una invitación, escribir una carta de agradecimiento, hacer preguntas de respeto y cuidar el lugar. También podemos organizar un encuentro de escuela donde una persona invitada cuente lo que decide y los niños escuchen.",
        "Si no nos invitan a un evento, no vamos. Si nos invitan, seguimos las reglas, no fotografiamos sin permiso y agradecemos. Si algo no se entiende, preguntamos después con respeto. Y recordamos que hay momentos que no se cuentan a quienes no son parte de la comunidad.",
    ],
    vocab=[("simular", "hacer como si fuera algo que no es"), ("espectáculo", "algo que se muestra para que otros miren"), ("invitar", "pedir a alguien que participe"), ("agradecimiento", "palabras o gestos para dar las gracias"), ("restringido", "que solo es para quienes la comunidad decide")],
    worked=[
        W("Qué hacer en vez de simular", "Tu curso quiere conocer una ceremonia. ¿Qué es mejor? a) simularla en el patio b) invitar a una persona de la comunidad para que cuente lo que quiera.", ["Simular no es respetuoso.", "Invitar a una persona y escucharla sí lo es.", "Elijo la segunda."], "b"),
        W("Después de la invitación", "Fuiste a una fiesta de Valle Alto con una invitación. ¿Qué haces al terminar? a) agradecer b) publicar todas las fotos c) irte sin saludar.", ["Agradecer cierra el encuentro con respeto.", "Publicar fotos sin permiso no corresponde.", "Elijo agradecer."], "a"),
    ],
    mistakes=[
        M("Hacer una ceremonia en el patio de la escuela.", "No es un juego y puede ofender.", "Invita a una persona de la comunidad a contar lo que quiera."),
        M("Ir a un evento sin invitación porque «es público».", "Algunos eventos son restringidos.", "Pregunta si puedes ir."),
    ],
    R=[
        ex("¿Se deben simular ceremonias en clase? Responde Sí o No.", "No", "No son un juego."),
        ex("Si te invitan, sigues las reglas del evento. ¿Verdadero o falso?", "Verdadero", "Es parte del respeto."),
        ex("Agradecer después de un evento es una forma de respeto. ¿Verdadero o falso?", "Verdadero", "Valora a quienes te recibieron."),
    ],
    C=[
        ex("Verdadero o falso: puedes ir a cualquier evento aunque no te inviten.", "Falso", "Algunos eventos son restringidos."),
        ex("¿Qué es mejor para aprender de una ceremonia? A) Escuchar a una persona de la comunidad B) Imitarla", "A", "Escuchar respeta el sentido de la ceremonia."),
        ex("Si te piden no grabar, ¿qué haces? A) No grabo B) Grabo en secreto", "A", "Respetas lo que piden."),
    ],
    A=[
        ex("Marca las acciones respetuosas: a) escribir una carta de agradecimiento b) simular una ceremonia c) pedir permiso d) invitar a una persona de la comunidad.", "a, c y d", "Esas acciones respetan; simular no."),
        ex("Ordena: 1) agradezco 2) recibo la invitación 3) voy y sigo las reglas. Escribe el orden.", "2, 3, 1", "Primero la invitación, luego voy y al final agradezco."),
        ex("Un niño dice «hagamos la ceremonia con disfraces». ¿Qué alternativa le propones? A) Invitar a un educador tradicional B) Comprar disfraces", "A", "Una persona de la comunidad puede compartir lo que quiera."),
    ],
    Z=[
        ex("Lía dice que simular una ceremonia es una forma de aprender. ¿Qué le responderías?", "Que mejor escuche a una persona de la comunidad", "Simularla puede ofender."),
        ex("Pedro cree que si el evento es en una plaza, todos pueden ir. ¿Qué debería hacer primero?", "Preguntar si es abierto", "Algunos eventos son restringidos aunque estén en un lugar público."),
    ],
    D=[
        ex("Una escuela hace un acto con una persona invitada que cuenta lo que quiere. Los niños escuchan, agradecen y no graban. ¿Cuántas acciones respetuosas hay (invitar, escuchar, agradecer, no grabar)?", "4", "Se cuentan las cuatro."),
        ex("Un visitante graba una ceremonia aunque lo prohibieron. ¿Qué debe hacer después? A) Borrarlo y pedir disculpas B) Publicarlo", "A", "Repara su error."),
    ],
    context=[ex("El curso quiere hacer una feria cultural. Ema propone una «ceremonia» con velas para representar a un pueblo. ¿Qué le dices? A) Mejor invitar a una persona de la comunidad B) Está bien, es solo un juego", "A", "Una persona de la comunidad puede compartir lo que decida.")],
    selfcheck=[ex("Escribe dos acciones respetuosas ante un evento ceremonial.", "Pedir permiso y agradecer", "Son ejemplos de respeto."), ex("¿Por qué no se simulan las ceremonias?", "Porque tienen un sentido especial", "No son un juego."), ex("Verdadero o falso: puedes grabar si nadie te ve.", "Falso", "Hay que pedir permiso siempre.")],
    task=T("Escribe una carta de agradecimiento a una persona inventada, doña Rosa, que visitó tu escuela para contar lo que ella quiso sobre un evento de su comunidad. Incluye tres frases: agradecer, decir qué aprendiste y prometer cuidar lo que te contó. Dibuja una tarjeta con un paisaje de tu invención, sin símbolos sagrados.",
           "Querida doña Rosa: gracias por visitarnos. Aprendí que los eventos tienen reglas de respeto. Prometo cuidar lo que nos contó y no grabarlo sin permiso.",
           ["escribe tres frases", "no pide ni simula ceremonias", "promete cuidar lo contado"], ["carta", "tarjeta"], ["simular ceremonias", "no agradecer"],
           "Valorar el agradecimiento y verificar que no contenga detalles inventados."),
    reinforce="Escribe tres frases de agradecimiento para una visita.",
    extend="Escribe una pregunta que no invada la intimidad de una comunidad.",
)

# ============================================================ OA 13 · Valores sociocomunitarios
L(
    OA13, 1,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé a reconocer valores como la reciprocidad, el respeto y la ayuda mutua en acciones de la familia y la comunidad. Sirve para ver cómo se convive bien.",
    prior=["Sé qué es una familia y una comunidad.", "Sé que una fuente dice quién cuenta."],
    explain=[
        "Los valores sociocomunitarios son ideas que guían cómo convivimos en la familia y en la comunidad. Tres de ellos son la reciprocidad, el respeto y la ayuda mutua. Se reconocen mirando lo que las personas hacen.",
        "La reciprocidad es dar y recibir. El respeto es tratar con cuidado a las personas, a los mayores y a la naturaleza. La ayuda mutua es ayudarse entre varios. Por ejemplo, si un vecino ayuda a otro a cargar leña, y después el otro lo ayuda a él, hay ayuda mutua.",
        "Los valores no se dicen solo con palabras. Se ven en las acciones. Cada comunidad tiene su forma de vivirlos. En este cuaderno usamos casos inventados para aprender a reconocerlos, y las formas tradicionales las enseña el educador tradicional.",
    ],
    vocab=[("valor", "idea que guía cómo convivimos"), ("reciprocidad", "dar y recibir entre personas"), ("respeto", "tratar con cuidado a personas y a la naturaleza"), ("ayuda mutua", "ayudarse entre varios"), ("convivir", "vivir juntos con buen trato")],
    worked=[
        W("Reconocer un valor", "Caso inventado: «Doña Rosa lleva pan a su vecina enferma. Después la vecina le regala verduras de su huerta». ¿Qué valor aparece?", ["Una persona da, la otra también da.", "Se devuelve algo recibido.", "Eso es reciprocidad."], "Reciprocidad"),
        W("Otro valor", "Caso inventado: «Un niño saluda a su abuelo antes de empezar a conversar». ¿Qué valor aparece?", ["Saludar con cuidado es tratar bien.", "Escuchar a los mayores también.", "Es respeto."], "Respeto"),
    ],
    mistakes=[
        M("Pensar que los valores solo se dicen con palabras.", "Se ven en lo que las personas hacen.", "Mira las acciones de las personas."),
        M("Confundir reciprocidad con ayuda mutua.", "La reciprocidad es dar y recibir; la ayuda mutua es ayudar entre varios.", "Pregunta si es dar y recibir o ayudar entre varios."),
    ],
    R=[
        ex("Dar y recibir es reciprocidad. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
        ex("Tratar con cuidado a los mayores es respeto. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
        ex("Ayudarse entre varios es ayuda mutua. ¿Verdadero o falso?", "Verdadero", "Es su definición."),
    ],
    C=[
        ex("¿Qué valor muestra quien saluda con cariño a un mayor? A) Respeto B) Competencia", "A", "Saludar con cuidado es respeto."),
        ex("Verdadero o falso: los valores se ven en las acciones.", "Verdadero", "Se reconocen mirando lo que se hace."),
        ex("Dos vecinos se ayudan a cosechar y luego cosechan juntos. ¿Qué valor es? A) Ayuda mutua B) Competencia", "A", "Se ayudan entre varios."),
    ],
    A=[
        ex("Une acción y valor. 1) regalar verduras a quien te dio pan 2) saludar a un abuelo 3) construir juntos un puente. a) respeto b) ayuda mutua c) reciprocidad", "1-c, 2-a, 3-b", "Cada acción muestra un valor distinto."),
        ex("Caso inventado: «Cuatro familias limpian juntas un canal». ¿Qué valor aparece?", "Ayuda mutua", "Se ayudan entre varias familias."),
        ex("Caso inventado: «Un niño espera su turno para hablar». ¿Qué valor aparece?", "Respeto", "Esperar el turno es tratar con cuidado."),
    ],
    Z=[
        ex("Pedro dice: «Ayudar solo sirve si me dan algo a cambio». ¿Qué le falta entender a su idea?", "Que ayudar también es cuidar a otros", "Se ayuda también para cuidar y convivir bien."),
        ex("Ema dice: «La reciprocidad es igual a la ayuda mutua». ¿En qué se diferencian?", "La reciprocidad es dar y recibir; la ayuda mutua es ayudar entre varios", "Cada una tiene su sentido."),
    ],
    D=[
        ex("Caso inventado: «Una familia cosecha, comparte con vecinos y luego recibe ayuda para su techo». ¿Qué dos valores aparecen?", "Reciprocidad y ayuda mutua", "Dan y reciben, y se ayudan entre varios."),
        ex("Un niño ve a un compañero tirar basura al río y lo corrige con calma. ¿Qué valor muestra?", "Respeto por la naturaleza", "Cuida el río."),
    ],
    context=[ex("En tu cuaderno, Lía escribe: «Mi abuela cuida a mi hermano; mi mamá cuida a mi abuela». ¿Qué valor aparece principalmente? A) Reciprocidad B) Competencia", "A", "Se devuelve el cuidado recibido.")],
    selfcheck=[ex("Nombra tres valores de esta clase.", "Reciprocidad, respeto y ayuda mutua", "Son los tres de la explicación."), ex("¿Cómo reconocemos un valor?", "Mirando las acciones", "Se ve en lo que se hace."), ex("Verdadero o falso: la ayuda mutua es ayudarse entre varios.", "Verdadero", "Es la definición.")],
    task=T("Lee tres casos inventados: A) «Doña Rosa lleva pan a una vecina y la vecina le regala verduras». B) «Un niño saluda a su abuelo antes de conversar». C) «Cuatro familias limpian juntas un canal». Escribe qué valor aparece en cada caso y haz un dibujo del caso que más te guste.",
           "A: reciprocidad. B: respeto. C: ayuda mutua. Dibujo: cuatro familias limpiando un canal.",
           ["identifica los tres valores", "relaciona cada valor con la acción", "dibuja un caso"], ["tres respuestas", "dibujo"], ["confundir valores", "no dibujar"],
           "Pedir que explique cómo vio el valor en cada acción."),
    reinforce="Escribe una acción de tu familia que muestre cada valor.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo se vive un valor en su comunidad.",
)

L(
    OA13, 2,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé cómo la reciprocidad, el respeto y la ayuda mutua se viven en la familia, la escuela y la comunidad, y qué palabras usan algunos pueblos. Sirve para ver que se practican en lugares distintos.",
    prior=["Sé qué son la reciprocidad, el respeto y la ayuda mutua.", "Sé que se ven en las acciones."],
    explain=[
        "Estos valores se viven en muchos lugares. En la familia, los mayores cuidan a los niños y después los niños ayudan a los mayores. En la escuela, compartimos útiles y esperamos turnos. En la comunidad, los vecinos se ayudan en las fiestas y en los trabajos grandes.",
        "Según fuentes publicadas, en el mundo andino se habla de ayni, que es ayudar hoy a alguien para recibir ayuda mañana. Y en Chile se usa la palabra minga para un trabajo en que muchas personas ayudan a una familia. Su uso varía según el lugar y cada comunidad las vive a su manera.",
        "Los valores también cuidan la naturaleza. Se respeta el agua, el cerro y los animales. Y se agradece lo que se recibe. Vivir los valores en lugares distintos no significa que todas las comunidades lo hagan igual: por eso preguntamos, escuchamos y no suponemos.",
    ],
    vocab=[("ayni", "palabra andina que, según fuentes publicadas, significa ayudar hoy para recibir ayuda mañana"), ("minga", "trabajo en que muchas personas ayudan a una familia"), ("turno", "momento que le toca a cada persona"), ("vecino", "persona que vive cerca"), ("escuchar", "poner atención a lo que dice otro")],
    worked=[
        W("Valores en lugares distintos", "Une el lugar con el valor. Familia: los mayores cuidan a los niños. Escuela: se espera el turno. Comunidad: los vecinos ayudan a levantar un techo. ¿Qué valor aparece en la comunidad?", ["Los vecinos ayudan entre varios.", "Eso es ayuda mutua.", "Lo escribo."], "Ayuda mutua"),
        W("Qué significa ayni", "Según fuentes publicadas, ayni es ayudar hoy a alguien para recibir ayuda mañana. ¿Qué valor muestra?", ["Hoy doy ayuda.", "Mañana recibo ayuda.", "Es reciprocidad."], "Reciprocidad"),
    ],
    mistakes=[
        M("Pensar que todas las comunidades viven los valores igual.", "Cada comunidad tiene su forma.", "Pregunta cómo lo hace cada una."),
        M("Usar palabras de una lengua sin saber su significado.", "Puedes decir algo falso.", "Usa solo las palabras que una fuente confiable te explica."),
    ],
    R=[
        ex("Esperar el turno es una forma de respeto. ¿Verdadero o falso?", "Verdadero", "Trata bien a los demás."),
        ex("Según fuentes publicadas, ayni es ayudar hoy para recibir ayuda mañana. ¿Qué valor muestra: reciprocidad o competencia?", "Reciprocidad", "Se da y se recibe."),
        ex("Una minga es un trabajo en que muchos ayudan. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("Verdadero o falso: todas las comunidades viven los valores exactamente igual.", "Falso", "Cada una tiene su forma."),
        ex("¿Dónde se pueden vivir los valores? A) En la familia, la escuela y la comunidad B) Solo en la escuela", "A", "Se viven en muchos lugares."),
        ex("En una minga, ¿cuántas personas ayudan a una familia? A) Muchas B) Una sola", "A", "Es un trabajo colectivo."),
    ],
    A=[
        ex("Une lugar y acción. 1) familia 2) escuela 3) comunidad. a) vecinos ayudan a levantar un techo b) los mayores cuidan a los niños c) se espera el turno", "1-b, 2-c, 3-a", "Cada acción ocurre en ese lugar."),
        ex("Caso inventado: «Esta semana ayudo a mi vecino a cosechar y la próxima él me ayuda». ¿Qué valor aparece?", "Reciprocidad", "Se da y se recibe ayuda."),
        arith("En una minga de práctica participan 5 familias con 4 personas cada una. ¿Cuántas personas hay en total?", "5*4", "Se multiplica el número de familias por las personas de cada una.", " personas"),
    ],
    Z=[
        ex("Tomás dice: «Si todos se ayudan, nadie necesita pedir permiso». ¿Qué falta?", "Respeto al ayudar", "Ayudar también necesita permiso y cuidado."),
        ex("Lía dice que sabe lo que significa una palabra de una lengua indígena porque «suena parecido». ¿Qué debe hacer?", "Preguntar a una fuente confiable", "Un sonido parecido no da el significado."),
    ],
    D=[
        arith("En una minga de práctica, 12 personas llegan temprano y 8 más llegan después. ¿Cuántas personas ayudan en total?", "12+8", "Se suman los dos grupos.", " personas"),
        ex("Dos comunidades inventadas viven la ayuda mutua de formas distintas: una con mingas y otra con turnos de trabajo. ¿Alguna lo hace mal? Responde Sí o No.", "No", "Cada una tiene su forma."),
    ],
    context=[ex("En la escuela, Ema comparte sus lápices con Mateo y Mateo le comparte su merienda. ¿Qué valor aparece? A) Reciprocidad B) Competencia", "A", "Cada uno da y recibe algo.")],
    selfcheck=[ex("Escribe un lugar donde se viven los valores.", "La familia, la escuela o la comunidad", "Se viven en todos."), ex("¿Qué significa minga?", "Un trabajo en que muchas personas ayudan", "Es un trabajo colectivo."), ex("Verdadero o falso: los valores cuidan también la naturaleza.", "Verdadero", "Se respeta el agua, los cerros y los animales.")],
    task=T("Haz una tabla con tres lugares: familia, escuela y comunidad. En cada uno escribe una acción de ayuda mutua, una de respeto y una de reciprocidad. Puedes usar ideas de la clase. Dibuja la acción que más te guste. No escribas datos personales.",
           "Familia: ayudo a mi mamá a ordenar (ayuda mutua); saludo a mi abuela (respeto); cuido a mi abuela como ella me cuidó (reciprocidad). Escuela: comparto lápices; espero mi turno; devuelvo un favor.",
           ["completa las tres filas", "incluye los tres valores", "no escribe datos personales"], ["tabla", "dibujo"], ["confundir valores", "escribir datos personales"],
           "Revisar que cada acción corresponda a su valor."),
    reinforce="Elige un valor y escribe tres acciones que lo muestren.",
    extend="Escribe una pregunta sobre una minga o un trabajo en conjunto para un educador tradicional.",
)

L(
    OA13, 3,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé que los valores de la comunidad siguen vivos hoy y que los practican personas actuales. Sirve para mostrar que están presentes en la vida diaria.",
    prior=["Sé qué son los valores sociocomunitarios.", "Sé que se viven en lugares distintos."],
    explain=[
        "Los valores no son solo cosa del pasado. Hoy los practican abuelos, madres, padres, niños y jóvenes. Se ven cuando un vecino ayuda a otro, cuando se comparten alimentos, cuando se escucha a los mayores y cuando se cuida la naturaleza.",
        "Las formas de vivir los valores pueden cambiar. Por ejemplo, en una comunidad inventada, antes se avisaba a los vecinos de una minga caminando. Hoy se puede avisar por teléfono. Lo importante es que el valor continúe: la ayuda mutua sigue, aunque cambie el medio para avisar.",
        "Los valores se aprenden en la casa, en la escuela y en la comunidad. Cada persona puede practicarlos desde pequeña. Si los cuidamos, la convivencia mejora para todos. Y reconocemos que quienes los enseñan son personas de hoy.",
    ],
    vocab=[("continuar", "seguir existiendo"), ("cambiar", "volverse distinto"), ("medio", "forma de hacer algo, como un teléfono o una carta"), ("convivencia", "vivir juntos con respeto"), ("practicar", "hacer algo una y otra vez para aprender")],
    worked=[
        W("Qué cambió y qué continúa", "Caso inventado: «Antes se avisaba de una minga caminando, hoy se avisa por teléfono, pero todos siguen ayudando». ¿Qué cambió y qué continúa?", ["Cambió la forma de avisar.", "Continúa la ayuda de todos.", "Escribo cada cosa en su columna."], "Cambió el aviso; continúa la ayuda mutua."),
        W("Persona actual", "Una niña dice que su tío invita a los vecinos a una minga. ¿Esa persona es del pasado o de hoy?", ["Lo hace ahora.", "Es una persona actual.", "Los valores se practican hoy."], "De hoy"),
    ],
    mistakes=[
        M("Pensar que los valores de la comunidad ya no se practican.", "Muchas personas los viven hoy.", "Observa lo que las personas hacen ahora."),
        M("Creer que si cambia el medio, el valor desapareció.", "El valor continúa aunque cambie la forma.", "Pregunta qué sigue igual."),
    ],
    R=[
        ex("Los valores de la comunidad se practican hoy. ¿Verdadero o falso?", "Verdadero", "Los practican personas actuales."),
        ex("Avisar por teléfono en vez de caminar es un cambio. ¿Verdadero o falso?", "Verdadero", "Cambió el medio."),
        ex("¿La ayuda mutua continúa si se avisa por teléfono? Responde Sí o No.", "Sí", "El valor sigue aunque cambie el medio."),
    ],
    C=[
        ex("Verdadero o falso: si cambia el medio, desaparece el valor.", "Falso", "El valor continúa."),
        ex("¿Dónde se aprenden los valores? A) En la casa, la escuela y la comunidad B) Solo en un libro", "A", "Se aprenden viviéndolos."),
        ex("Una niña ayuda a su vecina a cargar bolsas. ¿Esto pasa en el pasado o hoy?", "Hoy", "Lo hace ahora."),
    ],
    A=[
        ex("Clasifica como CAMBIÓ o CONTINÚA: a) avisar por teléfono b) ayudar entre vecinos c) invitar con un mensaje.", "a cambió, b continúa, c cambió", "Solo el medio cambia."),
        ex("Une persona y acción actual. 1) un niño 2) una abuela 3) un vecino. a) enseña a escuchar b) ayuda a cargar leña c) comparte su merienda", "1-c, 2-a, 3-b", "Cada uno practica un valor hoy."),
        ex("Marca solo lo que cuida la convivencia: a) esperar turno b) empujar c) compartir d) gritar.", "a y c", "Esperar y compartir cuidan la convivencia."),
    ],
    Z=[
        ex("Rosa dice: «Los valores comunitarios son del pasado». ¿Qué prueba puedes dar?", "Hoy los vecinos se ayudan y comparten", "Las personas actuales los practican."),
        ex("Pedro dice que avisar por teléfono hace que la minga ya no sea una minga. ¿Qué le dirías?", "Que sigue siendo ayuda mutua aunque cambie el aviso", "El valor continúa."),
    ],
    D=[
        arith("Una escuela de práctica tiene 3 cursos y cada curso trae 10 libros para compartir con otros. ¿Cuántos libros hay para compartir?", "3*10", "Se multiplica cursos por libros de cada curso.", " libros"),
        ex("Una comunidad usa un grupo de mensajes para organizar una ayuda. ¿Qué valor continúa?", "La ayuda mutua", "Las personas siguen ayudándose."),
    ],
    context=[ex("Tu curso organiza una ayuda para limpiar la plaza. Julia avisa por mensaje. ¿Qué continúa de la minga? A) Ayudarse entre muchos B) Avisar caminando", "A", "El valor continúa, aunque cambie el medio.")],
    selfcheck=[ex("Escribe una acción que muestre un valor hoy.", "Ayudar a un vecino o compartir", "Son acciones actuales."), ex("¿Qué continúa si cambia el medio de avisar?", "El valor", "Se sigue ayudando."), ex("Verdadero o falso: los niños no practican valores.", "Falso", "Los niños también los practican.")],
    task=T("Escribe una carta corta a un vecino inventado, don Luis, para invitarlo a una ayuda de práctica en la plaza. Incluye el día (un sábado), la hora (10:00 de la mañana), qué se hará (limpiar y plantar flores) y cómo agradecerás su ayuda. Dibuja la plaza limpia y con flores. No escribas direcciones reales.",
           "Estimado don Luis: lo invito el sábado a las 10:00 a limpiar y plantar flores en la plaza. Después compartiremos una merienda para agradecerle.",
           ["incluye día, hora y qué se hará", "propone agradecer", "usa un trato respetuoso"], ["carta", "dibujo"], ["olvidar el agradecimiento", "usar direcciones reales"],
           "Revisar que la invitación tenga todos los datos y sea respetuosa."),
    reinforce="Escribe tres acciones actuales de ayuda en tu escuela.",
    extend="Escribe una pregunta para una persona mayor sobre cómo se ayudaban antes los vecinos.",
)

L(
    OA13, 4,
    materials="Lápiz y hojas. Los casos son inventados.",
    use="Aprenderé a proponer acciones de reciprocidad, respeto y ayuda mutua que cuiden a las personas y a la naturaleza. Sirve para llevar los valores a la vida diaria.",
    prior=["Sé qué son los tres valores.", "Sé que continúan hoy."],
    explain=[
        "Cuidar los valores significa ponerlos en práctica. Una acción de reciprocidad puede ser devolver un favor. Una acción de respeto puede ser escuchar sin interrumpir. Una acción de ayuda mutua puede ser trabajar con otros para lograr algo para todos.",
        "También cuidamos con la palabra. Cumplir lo que prometemos es parte del respeto. Si decimos que vamos a ayudar, ayudamos. Si decimos que vamos a guardar un secreto o no publicar una historia, lo cumplimos. La palabra dada vale.",
        "Un buen compromiso es claro, posible y se puede revisar. Por ejemplo: «Esta semana ayudaré a mi vecina dos veces». Después de la semana, revisamos si lo hicimos. Así los valores se vuelven hábitos de la vida diaria.",
    ],
    vocab=[("compromiso", "lo que prometo hacer"), ("cumplir", "hacer lo que se prometió"), ("hábito", "algo que se hace seguido"), ("revisar", "mirar si algo se hizo"), ("palabra dada", "lo que una persona promete")],
    worked=[
        W("Un buen compromiso", "¿Cuál es un compromiso claro y posible? a) «Ayudaré a todos siempre» b) «Esta semana ayudaré a mi vecina dos veces».", ["Un buen compromiso es claro.", "También se puede revisar.", "El segundo cumple eso."], "b"),
        W("Revisar", "Prometiste ayudar dos veces a tu vecina. Ayudaste una vez. ¿Qué te falta hacer?", ["Prometí 2 y hice 1.", "2 − 1 = 1.", "Falta una vez."], "Una vez"),
    ],
    mistakes=[
        M("Prometer cosas muy grandes que no se pueden cumplir.", "Si no se cumple, se pierde la confianza.", "Elige un compromiso claro y posible."),
        M("Olvidar revisar si cumpliste.", "Sin revisar, no mejoras.", "Revisa al final de la semana."),
    ],
    R=[
        ex("Cumplir lo que prometimos es parte del respeto. ¿Verdadero o falso?", "Verdadero", "La palabra dada vale."),
        ex("Un buen compromiso es claro y posible. ¿Verdadero o falso?", "Verdadero", "Es la idea de la clase."),
        ex("Revisar un compromiso es mirar si lo cumpliste. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
    ],
    C=[
        ex("¿Cuál compromiso es mejor? A) Ayudar a todos para siempre B) Ayudar a mi vecina dos veces esta semana", "B", "Es claro y se puede revisar."),
        ex("Verdadero o falso: se puede prometer cualquier cosa sin pensar si se podrá cumplir.", "Falso", "Un compromiso debe ser posible."),
        ex("Si prometes no publicar una historia, ¿qué haces? A) Cumplo B) Publico igual", "A", "La palabra dada se cumple."),
    ],
    A=[
        ex("Ordena: 1) reviso si cumplí 2) hago mi compromiso 3) lo escribo. Escribe el orden.", "3, 2, 1", "Primero lo escribo, luego lo hago y al final reviso."),
        arith("Prometiste ayudar 3 veces a tu vecina esta semana. Ayudaste 2. ¿Cuántas veces te falta?", "3-2", "Se resta lo hecho a lo prometido.", " vez"),
        ex("Marca los compromisos claros: a) saludar a mi abuela cada día b) ser el mejor del mundo c) llevar mi basura de vuelta en la excursión d) hacerlo todo.", "a y c", "Son claros y posibles."),
    ],
    Z=[
        ex("Ema promete ayudar «todo el año» a todos sus vecinos. ¿Qué problema tiene su compromiso?", "Es demasiado grande y difícil de revisar", "No se puede cumplir ni revisar fácilmente."),
        ex("Tomás dice que no necesita cumplir si nadie lo ve. ¿Qué valor le falta?", "Respeto y palabra dada", "Cumplir es importante aunque nadie vea."),
    ],
    D=[
        ex("Una niña promete 2 acciones de respeto, 2 de ayuda y 1 de reciprocidad. ¿Cuántas acciones prometió en total?", "5", "2 + 2 + 1 = 5."),
        ex("Un curso se compromete a cuidar la plaza una vez al mes durante 4 meses. ¿Cuántas veces la cuidará?", "4", "Una por mes durante 4 meses."),
    ],
    context=[ex("Tu curso hace una lista de compromisos para la semana. Julia escribe «Seré mejor persona». Su profesora le pide que sea más clara. ¿Qué podría escribir? A) «Saludaré a mis vecinos cada día» B) «Seré mejor»", "A", "Es una acción concreta que se puede revisar.")],
    selfcheck=[ex("¿Qué debe tener un buen compromiso?", "Ser claro, posible y revisable", "Son las tres características de la clase."), ex("¿Qué haces con la palabra dada?", "La cumplo", "Es parte del respeto."), ex("Verdadero o falso: revisar sirve para mejorar.", "Verdadero", "Muestra qué falta hacer.")],
    task=T("Escribe una tarjeta con tres compromisos para esta semana: uno de reciprocidad, uno de respeto y uno de ayuda mutua. Deben ser claros y posibles. Dibuja un recuadro para marcar cuando los cumplas. No escribas nombres de personas reales.",
           "Reciprocidad: devolveré un favor a mi compañero. Respeto: saludaré a mi abuelo cada día. Ayuda mutua: limpiaré la sala con mis compañeros el viernes. Recuadro para marcar.",
           ["escribe tres compromisos", "cada uno es claro y posible", "incluye un recuadro de revisión"], ["tarjeta", "recuadro"], ["compromisos vagos", "olvidar la revisión"],
           "Revisar que cada compromiso pueda verificarse."),
    reinforce="Elige un compromiso y escribe cómo sabrás si lo cumpliste.",
    extend="Escribe un compromiso de curso que ayude a toda la sala.",
)

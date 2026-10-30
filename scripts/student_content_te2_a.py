"""Cuaderno del estudiante, 2.º básico Tecnología: OA 01 (diseño de objetos) y OA 02 (tareas, materiales, herramientas)."""
from __future__ import annotations

from student_lessons import ex, register

OA1, OA2 = "TE02 OA 01", "TE02 OA 02"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [ex(*i) for i in R], "understand": [ex(*i) for i in C], "apply": [ex(*i) for i in A], "reason": [ex(*i) for i in Z], "challenge": [ex(*i) for i in D]},
        context=[ex(*ctx)], selfcheck=[ex(*i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01
reg(
    OA1, 1,
    materials="Una hoja, un lápiz y los casos escritos en este cuaderno. No necesitas nada más.",
    use="Aprenderé a decir quién usará un objeto, qué necesita y en qué lugar lo usará, antes de dibujar. Sirve para que mi diseño ayude de verdad.",
    prior=["Sé que un objeto tecnológico se hace para ayudar a alguien.", "Sé que un criterio es algo que el objeto debe cumplir."],
    explain=[
        "Diseñar es pensar un objeto antes de hacerlo. Lo primero es la necesidad: lo que una persona quiere lograr. La persona que usará el objeto es el usuario. Todavía no dibujes el objeto.",
        "También importa el contexto, que es el lugar y la situación donde se usará. Un objeto para llevar tres libros en el bus no es igual a uno para usar en la casa. Cambia el lugar y cambia lo que el objeto necesita.",
        "Además hay restricciones, que son límites. Por ejemplo: debe caber en una mochila, o pesar poco. Escribe usuario, necesidad, contexto y una restricción. Con eso tu boceto tendrá un rumbo claro.",
    ],
    vocab=[("necesidad", "lo que una persona quiere lograr"), ("usuario", "quien usará el objeto"), ("contexto", "el lugar y la situación de uso"), ("restricción", "un límite que el diseño debe respetar"), ("diseñar", "pensar y dibujar un objeto antes de hacerlo")],
    worked=[
        ("Ordenar los datos de un caso", "Mía camina al colegio con tres libros en los brazos y se le caen. ¿Cuál es el usuario, la necesidad y el contexto?", ["Quien usará el objeto es Mía: es la usuaria.", "Lo que necesita es llevar tres libros sin que caigan.", "El contexto es el camino al colegio."], "Usuaria: Mía. Necesidad: llevar tres libros sin que caigan. Contexto: el camino al colegio"),
        ("Agregar una restricción", "Para Mía, escribe una restricción para el objeto que llevará los libros.", ["Mía también lleva una mochila.", "El objeto no puede ser muy pesado para sus brazos.", "Escribo el límite con un dato comprobable."], "Debe pesar menos que sus tres libros juntos"),
    ],
    mistakes=[
        ("Empezar diciendo «haré una caja» sin decir para quién.", "La solución se elige antes de entender la necesidad.", "Escribe primero usuario, necesidad y contexto; la solución viene después."),
        ("Escribir como necesidad «quiero un asa».", "El asa es una solución, no una necesidad.", "Escribe qué se quiere lograr: «llevar libros sin que caigan»."),
    ],
    R=[
        ("Rita lleva su colación al patio y se le cae. ¿Quién es la usuaria: Rita o el patio?", "Rita", "La usuaria es la persona que usará el objeto."),
        ("Toño no encuentra sus lápices en la mochila. ¿Su necesidad es encontrar sus lápices o pintar una pared?", "Encontrar sus lápices", "La necesidad es lo que él quiere lograr."),
        ("Un objeto se usará en la cocina de una casa. ¿La cocina es el usuario o el contexto?", "El contexto", "El contexto es el lugar donde se usa."),
    ],
    C=[
        ("¿Qué es una restricción en un diseño? Responde con tus palabras.", "Un límite que el diseño debe respetar", "Una restricción limita el tamaño, peso u otro rasgo."),
        ("Dos frases: A «llevar tres libros sin que caigan» y B «una caja con asa». ¿Cuál es una necesidad?", "A", "A dice lo que se quiere lograr; B ya es una solución."),
        ("Un diseño para usar en el bus y otro para usar en la casa. ¿Pueden necesitar cosas distintas? Responde sí o no.", "Sí", "El contexto cambia lo que el objeto necesita."),
    ],
    A=[
        ("Caso: Dani necesita guardar 4 lápices sobre su mesa de estudio. Escribe usuario, necesidad y contexto en ese orden.", "Usuario: Dani. Necesidad: guardar 4 lápices. Contexto: su mesa de estudio", "Lleva los tres datos que da el caso."),
        ("Caso: una abuela quiere regar una planta de la ventana sin caerse del banquito. ¿Cuál es el contexto?", "La ventana de la casa donde está la planta", "Es el lugar de uso."),
        ("Una mochila mide 30 cm de ancho. El objeto debe caber dentro. ¿Sirve como restricción «ancho menor que 30 cm» o «que sea lindo»?", "Ancho menor que 30 cm", "Se puede medir y comprobar."),
    ],
    Z=[
        ("Lalo dice: «Mi necesidad es una caja azul». ¿Es una necesidad o una solución? Explica en pocas palabras.", "Es una solución", "Una caja azul no dice qué quiere lograr."),
        ("Un niño dibujó un objeto, pero no sabe quién lo usará. ¿Le conviene dibujar más o decidir primero el usuario? Responde con una frase.", "Decidir primero el usuario", "Sin usuario, el boceto no tiene rumbo."),
    ],
    D=[
        ("Caso: Ema lleva su botella de agua y su cuaderno al colegio y la botella moja el cuaderno. Escribe necesidad y una restricción comprobable.", "Necesidad: que la botella no moje el cuaderno; restricción: por ejemplo, debe caber en la mochila", "Pide una necesidad y un límite medible."),
        ("Un diseño para llevar tres libros dice «contexto: el bus». ¿Qué restricción nueva aparece por ir de pie? Escribe una.", "Debe poder sujetarse con una mano, por ejemplo", "En el bus se va de pie y con una mano libre."),
    ],
    ctx=("Cami vive lejos y lleva en la mano tres cuadernos y una colación. Se le cae todo al subir la escalera de la micro. Escribe usuario, necesidad, contexto y una restricción.", "Usuaria: Cami. Necesidad: llevar cuadernos y colación sin que caigan. Contexto: la escalera de la micro. Restricción: debe dejar una mano libre", "Cubre los cuatro datos con el caso."),
    sc=[
        ("¿Qué se escribe primero: la solución o la necesidad?", "La necesidad", "Sin necesidad no sabes qué diseñar."),
        ("«Debe pesar poco» y «debe pesar menos que 1 kilo». ¿Cuál se puede comprobar mejor?", "Debe pesar menos que 1 kilo", "Tiene un número que se puede medir."),
        ("¿El contexto es el lugar de uso o el nombre del objeto?", "El lugar de uso", "Contexto es lugar y situación."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: Nico lleva 3 libros por la calle y se le caen. Caso 2: Sol quiere sostener su dibujo en la pared sin romperlo. Escribe usuario, necesidad, contexto y una restricción. Después haz un boceto a mano alzada de una idea.",
        "Caso 1: Usuario Nico. Necesidad: llevar 3 libros sin que caigan. Contexto: la calle. Restricción: debe pesar poco. Boceto: una bolsa de cartón con asa.",
        ["dice el usuario", "dice la necesidad sin nombrar la solución", "dice el contexto", "escribe una restricción comprobable", "hace un boceto"],
        ["ficha con los cuatro datos", "boceto a mano alzada"],
        ["escribe una solución como necesidad", "restricción que no se puede comprobar"],
        "Pregunta: «¿esto es lo que Nico quiere lograr o ya es un objeto?». Si es un objeto, ayúdale a decir qué quiere lograr.",
    ),
    reinforce="Mira un objeto de tu casa y di quién lo usa, qué necesita y dónde se usa.",
    extend="Piensa en un problema de tu sala de clases y escribe usuario, necesidad, contexto y una restricción.",
)

reg(
    OA1, 2,
    materials="Hojas, lápiz y los casos de este cuaderno. Sirve cualquier papel de reúso limpio.",
    use="Aprenderé a dibujar tres ideas distintas para un mismo problema. Sirve para comparar y no quedarme con la primera idea.",
    prior=["Sé decir usuario, necesidad y contexto.", "Sé que un boceto es un dibujo rápido."],
    explain=[
        "Un mismo problema puede tener muchas soluciones. Por eso conviene hacer tres bocetos distintos antes de elegir. Un boceto es un dibujo rápido a mano alzada, sin regla y sin pintar.",
        "Dos ideas son distintas cuando cambia cómo funcionan o cómo se usan, no solo el color. Para sostener un dibujo en la pared hay ideas distintas: un marco de cartón, un gancho de papel doblado o una tira con pegamento. Son tres formas de resolver lo mismo.",
        "Los diseños también se pueden unir con otras asignaturas. En Ciencias, una planta necesita luz y agua: puedes diseñar un soporte que la deje junto a la ventana. Dibuja rápido, no borres y escribe una palabra bajo cada idea.",
    ],
    vocab=[("boceto", "dibujo rápido a mano alzada"), ("idea distinta", "una solución que funciona de otra forma"), ("a mano alzada", "dibujar sin regla"), ("comparar", "mirar qué tienen igual y qué tienen distinto")],
    worked=[
        ("Reconocer ideas distintas", "Para colgar un dibujo: A una tira de cartón con pegamento, B otra tira de cartón pero roja, C un gancho de papel doblado. ¿Qué dos ideas son distintas?", ["A y B se usan igual: solo cambia el color.", "C funciona de otra forma: se dobla y se engancha.", "Entonces A y C son ideas distintas."], "A y C son distintas; B solo cambia el color"),
        ("Idea desde otra asignatura", "En Ciencias, una planta necesita luz. Escribe una idea de soporte para dejarla junto a la ventana.", ["Pienso qué necesita la planta: luz.", "Imagino una repisa pequeña pegada junto al vidrio.", "Anoto el nombre bajo el boceto: repisa."], "Repisa pequeña junto a la ventana"),
    ],
    mistakes=[
        ("Dibujar tres veces la misma caja con distinto color.", "Cambiar solo el color no crea una idea nueva.", "Cambia la forma o la manera de usarla."),
        ("Borrar un boceto porque no se ve bonito.", "Un boceto es para pensar, no para exhibir.", "Déjalo y anota qué te sirve de él."),
    ],
    R=[
        ("Un boceto es un dibujo rápido a mano alzada. ¿Se hace con regla o sin regla?", "Sin regla", "A mano alzada significa sin regla."),
        ("Quieres tres ideas para guardar lápices. ¿Haces un dibujo o tres?", "Tres", "Conviene comparar varias ideas."),
        ("Ana dibujó un vaso y otro vaso igual, pero rojo. ¿Son ideas distintas?", "No", "Solo cambió el color."),
    ],
    C=[
        ("¿Por qué conviene hacer varios bocetos antes de elegir? Responde con una frase.", "Para comparar y elegir la mejor", "Con varias ideas se decide mejor."),
        ("Ideas para sujetar un papel: A pinza de ropa, B imán chico, C cinta de papel. ¿Cuántas ideas distintas hay?", "3", "Cada una funciona de otra manera."),
        ("Si un boceto sale chueco, ¿se bota o se guarda para pensar?", "Se guarda", "Los bocetos sirven para pensar."),
    ],
    A=[
        ("Necesidad: que un cuaderno no se moje en la mochila. Escribe dos ideas que funcionen distinto.", "Por ejemplo: una caja de plástico con tapa y una funda impermeable", "Dos ideas con funcionamiento diferente."),
        ("Problema: una planta debe recibir luz. ¿Qué conviene incluir en el soporte: quedar junto a la ventana o quedar en un armario cerrado?", "Quedar junto a la ventana", "La planta necesita luz."),
        ("Marcos dibujó: una repisa, un gancho y una repisa más grande. ¿Cuántas ideas distintas dibujó?", "2", "La repisa grande sigue siendo repisa."),
    ],
    Z=[
        ("Tato dice: «Mi primera idea es la mejor, no dibujaré más». ¿Tiene razón? Explica brevemente.", "No, porque no comparó con otras ideas", "Sin comparar no sabe si es la mejor."),
        ("Dos ideas para llevar una botella: A funda con asa, B funda sin asa. ¿Cuál probablemente deja la mano más libre?", "A, con asa", "El asa permite colgar la funda del brazo."),
    ],
    D=[
        ("Necesidad: que un libro grande no se doble al guardarlo. Dibuja con palabras tres ideas muy distintas y di cuál mejora el apoyo.", "Por ejemplo: carpeta rígida, repisa y caja; cualquiera con justificación", "Tres ideas distintas y una razón."),
        ("Sol hizo tres bocetos y todos usan cartón pegado. ¿Qué cambio haría una idea realmente distinta?", "Usar otra forma de sostener, como doblar o colgar", "Hay que cambiar el modo de funcionar."),
    ],
    ctx=("Lía quiere sostener una hoja de dibujo en la pared sin hacer agujeros. Escribe tres ideas distintas con una palabra cada una y marca cuál te parece mejor.", "Cinta de papel; marco de cartón; gancho de cartulina. La mejor: cinta de papel, porque se saca sin romper la hoja", "Tres ideas diferentes y una elección."),
    sc=[
        ("¿Cuántos bocetos conviene hacer antes de elegir?", "Tres", "Tres permiten comparar."),
        ("¿Cambiar solo el color crea una idea nueva?", "No", "Debe cambiar el funcionamiento."),
        ("¿Un boceto se hace con regla?", "No", "Se hace a mano alzada."),
    ],
    open_task=(
        "Escoge un problema. Problema 1: guardar 5 lápices sobre una mesa. Problema 2: sostener una planta pequeña junto a una ventana. Haz tres bocetos a mano alzada con ideas distintas y escribe una palabra bajo cada uno. Subraya el que te parezca mejor.",
        "Problema 1: boceto 1 vaso de cartón; boceto 2 tira con ranuras; boceto 3 caja con tapa. Subrayo la caja con tapa.",
        ["hace tres bocetos", "las ideas funcionan de manera distinta", "escribe una palabra bajo cada una", "subraya una elección"],
        ["tres bocetos con nombres"],
        ["tres dibujos iguales con distinto color", "no elegir ninguno"],
        "Pregunta: «¿en qué se diferencian estas dos ideas?». Si solo cambia el color, pide otra forma de resolverlo.",
    ),
    reinforce="Dibuja dos ideas diferentes para colgar una mochila en tu casa.",
    extend="Elige un tema de Ciencias que conozcas y diseña dos ideas para ayudarlo, por ejemplo cuidar una planta.",
)

reg(
    OA1, 3,
    materials="Una hoja, un lápiz, una regla si tienes, y las figuras de este cuaderno.",
    use="Aprenderé a dibujar un objeto con vistas, partes con nombre y medidas. Sirve para que otra persona entienda cómo hacerlo.",
    prior=["Sé hacer un boceto a mano alzada.", "Sé medir en centímetros con una regla."],
    explain=[
        "Un buen dibujo de diseño se entiende sin que lo expliques. Para eso lleva etiquetas, que son nombres escritos con una línea hasta cada parte. También lleva medidas con su unidad, por ejemplo 15 cm.",
        "Un objeto se puede mirar desde distintos lados. La vista de frente muestra lo que ves de frente. La vista de lado muestra su grosor. La vista de arriba muestra cómo se ve desde arriba. Con dos vistas se entiende mejor que con una.",
        "Imagina un vaso de cartón para lápices. De frente se ve un rectángulo de 10 cm de alto. De arriba se ve un círculo. Dibuja cada vista, pon las etiquetas y anota las medidas con su unidad.",
    ],
    vocab=[("etiqueta", "nombre escrito para señalar una parte"), ("vista de frente", "cómo se ve el objeto mirado de frente"), ("vista de lado", "cómo se ve desde un costado"), ("vista de arriba", "cómo se ve mirado desde arriba"), ("medida", "número con su unidad, como 10 cm")],
    worked=[
        ("Elegir la vista", "Un vaso de cartón para lápices mide 10 cm de alto. ¿Qué vista muestra mejor la altura: la de frente o la de arriba?", ["La altura se ve mirando de frente.", "Desde arriba solo se ve el borde redondo.", "Entonces conviene la vista de frente."], "La vista de frente"),
        ("Escribir una medida", "El vaso mide 10 centímetros de alto. Escribe la medida como se pone en un dibujo.", ["Escribo el número 10.", "Agrego la unidad: cm.", "Pongo una línea que va de arriba a abajo del vaso."], "10 cm"),
    ],
    mistakes=[
        ("Escribir una medida sin unidad: «10».", "No se sabe si son centímetros, metros u otra cosa.", "Escribe siempre el número con su unidad: 10 cm."),
        ("Dibujar partes sin nombre.", "Otra persona no sabe qué es cada parte.", "Pon una etiqueta con una línea a cada parte."),
    ],
    R=[
        ("Una etiqueta sirve para nombrar una parte. ¿Se escribe cerca de la parte o en otra hoja?", "Cerca de la parte", "Así se sabe a qué parte se refiere."),
        ("Una medida debe llevar número y unidad. ¿«12 cm» está completa o incompleta?", "Completa", "Tiene número y unidad."),
        ("¿Qué vista muestra un objeto mirado desde arriba?", "La vista de arriba", "Se llama así."),
    ],
    C=[
        ("¿Para qué sirven las etiquetas en un dibujo de diseño?", "Para nombrar las partes", "Así otra persona entiende cada parte."),
        ("Una caja mide 8 cm de alto. ¿Qué vista muestra mejor ese dato: frente o arriba?", "Frente", "La altura se ve de frente."),
        ("¿Por qué dibujar dos vistas ayuda más que una?", "Porque muestra más lados del objeto", "Se entiende mejor la forma."),
    ],
    A=[
        ("Escribe la medida de una regla de 15 centímetros como se pone en un dibujo.", "15 cm", "Número y unidad."),
        ("Dibujas una bolsa con asa. ¿Qué dos etiquetas pondrías: asa y cuerpo, o sol y nube?", "Asa y cuerpo", "Son las partes del objeto."),
        ("Una caja de 12 cm de largo y 5 cm de alto. ¿Qué medida va en la vista de frente si miras el largo: 12 cm o 5 cm?", "12 cm", "El largo se ve de frente en la vista horizontal."),
    ],
    Z=[
        ("Una compañera dibujó un soporte con la medida «20». ¿Qué le falta? Responde con una palabra.", "La unidad", "Sin unidad el número no basta."),
        ("Un dibujo tiene vista de frente con la forma de un rectángulo y vista de arriba con un círculo. ¿Puede ser un vaso o una caja cuadrada?", "Un vaso", "Un círculo arriba indica forma redonda."),
    ],
    D=[
        ("Dibuja con palabras un soporte para lápices: di dos vistas, dos etiquetas y una medida con unidad.", "Por ejemplo: frente y arriba; etiquetas base y pared; 10 cm", "Pide dos vistas, dos etiquetas y una medida."),
        ("Un objeto de 6 cm de ancho debe caber en una mochila de 30 cm. ¿Caben 4 objetos en fila? Responde sí o no y di cuánto ocupan.", "Sí, ocupan 24 cm", "4 veces 6 es 24, y 24 es menor que 30."),
    ],
    ctx=("Lía hizo un portalápices con 10 cm de alto y base redonda de 7 cm de ancho. Dibuja con palabras la vista de frente con sus etiquetas y medidas.", "Vista de frente: rectángulo con alto 10 cm y ancho 7 cm; etiquetas: cuerpo y base", "Incluye etiquetas y medidas con unidad."),
    sc=[
        ("¿Qué lleva una medida completa?", "Número y unidad", "Sin unidad no está completa."),
        ("¿Qué vista muestra la altura?", "La vista de frente", "La altura se ve de frente."),
        ("¿Para qué sirven las etiquetas?", "Para nombrar partes", "Explican el dibujo."),
    ],
    open_task=(
        "Escoge un objeto: un portalápices de 10 cm de alto, o una repisa de 20 cm de largo. Dibuja la vista de frente y la vista de arriba. Pon al menos dos etiquetas y dos medidas con unidad.",
        "Portalápices: dibujé el frente (rectángulo) y arriba (círculo). Etiquetas: cuerpo y base. Medidas: 10 cm de alto y 7 cm de ancho.",
        ["dibuja dos vistas", "pone 2 etiquetas", "pone 2 medidas con unidad"],
        ["hoja con dos vistas etiquetadas"],
        ["medidas sin unidad", "partes sin nombre"],
        "Pregunta: «si otra persona ve tu dibujo, ¿sabe qué es cada parte?». Revisa que cada medida diga cm.",
    ),
    reinforce="Mide con una regla un objeto pequeño de tu casa y escribe sus medidas con unidad.",
    extend="Dibuja la vista de lado de tu objeto y compárala con la de frente.",
)

reg(
    OA1, 4,
    materials="Papel o cartón reutilizado limpio, cinta de papel y tijeras de punta redonda con un adulto cerca.",
    use="Aprenderé a hacer un modelo concreto de papel o cartón para ver tamaño y forma antes de construir el objeto final. Sirve para detectar errores a bajo costo.",
    prior=["Sé hacer vistas con medidas.", "Sé usar tijeras escolares con cuidado."],
    explain=[
        "Un modelo es una versión simple del objeto, hecha con papel o cartón. Sirve para pensar con las manos. Con el modelo ves si el tamaño sirve y si las partes encajan, antes de usar el material definitivo.",
        "Un modelo no tiene que ser bonito ni durable. Puede ser de papel doblado o cartón con cinta de papel. Se hace rápido y se puede cambiar. Si algo no sirve, lo corriges en el modelo, no en el objeto final.",
        "Por ejemplo, haces un modelo de una caja para 4 lápices. Pruebas con lápices de verdad y ves que no caben. Entonces cambias la medida en el modelo y anotas el nuevo tamaño. Un error en el modelo ahorra material y tiempo.",
    ],
    vocab=[("modelo", "versión simple del objeto hecha para probar"), ("prototipo", "primer objeto hecho para probar una idea"), ("encajar", "calzar una parte en otra"), ("corregir", "cambiar algo para que funcione mejor")],
    worked=[
        ("Detectar un error con el modelo", "Hiciste un modelo de papel de una caja de 4 cm de ancho para 4 lápices. Cada lápiz tiene 1 cm de grosor, uno al lado de otro. ¿Caben?", ["Cuatro lápices de 1 cm ocupan 4 cm.", "La caja mide 4 cm, justo.", "Conviene dejar un poco más: 5 cm."], "Cabe justo; mejor hacerla de 5 cm"),
        ("Qué cambiar", "El modelo de una repisa se inclina hacia adelante. ¿Qué corriges en el modelo y no en el objeto final?", ["Veo que se inclina.", "Pruebo con una base más ancha en el modelo.", "Anoto que la base ancha lo arregló."], "Se corrige primero la base en el modelo"),
    ],
    mistakes=[
        ("Construir el objeto final sin hacer antes un modelo.", "Un error costaría material y tiempo.", "Haz un modelo de papel y corrige primero ahí."),
        ("Pensar que el modelo debe quedar perfecto.", "Es solo para probar.", "Hazlo rápido y con materiales simples."),
    ],
    R=[
        ("Un modelo es una versión simple del objeto. ¿Se hace antes o después del objeto final?", "Antes", "Sirve para probar antes de construir."),
        ("¿De qué material puede ser un modelo: papel o diamante?", "Papel", "Un modelo usa materiales simples y baratos."),
        ("Si el modelo de una caja no calza con el objeto, ¿lo corriges en el modelo o lo botas todo?", "Lo corriges en el modelo", "Para eso sirve el modelo."),
    ],
    C=[
        ("¿Por qué conviene probar con un modelo antes de usar el material final?", "Para detectar errores sin gastar material", "Un error en el modelo cuesta menos."),
        ("¿Un modelo tiene que quedar bonito y durable? Responde sí o no.", "No", "Es solo para probar."),
        ("¿Qué se puede ver con un modelo: el tamaño o el sabor?", "El tamaño", "El modelo permite ver tamaño y forma."),
    ],
    A=[
        ("Quieres una caja para 3 gomas de 4 cm de ancho en fila. ¿Qué ancho mínimo tiene que tener el modelo?", "12 cm", "3 veces 4 es 12."),
        ("El modelo de una repisa se cae hacia adelante. ¿Qué parte probarías cambiar en el modelo: la base o el color?", "La base", "Una base más ancha o pesada da estabilidad."),
        ("Tu modelo mide 20 cm y la mochila mide 18 cm de ancho. ¿Cabe? Responde sí o no.", "No", "20 cm es mayor que 18 cm."),
    ],
    Z=[
        ("Un compañero dice: «Mi modelo falló, no sirve». ¿Qué le dices: que lo bote o que anote qué falló? Explica en una frase.", "Que anote qué falló", "El fallo da información para mejorar."),
        ("Dos modelos: uno de cartón en 5 minutos y otro de madera en un día. ¿Cuál conviene para probar una idea nueva?", "El de cartón", "Es más rápido y barato de cambiar."),
    ],
    D=[
        ("Quieres un soporte para un cuaderno de 22 cm de largo. Tu modelo mide 20 cm. ¿Cuántos centímetros más debe tener y por qué?", "Al menos 2 cm más", "22 menos 20 es 2, y el cuaderno debe caber."),
        ("Haces un modelo de papel y el objeto final pesa más. Escribe una razón por la que el modelo puede fallar distinto.", "El papel es más liviano que el material final", "El peso cambia la estabilidad."),
    ],
    ctx=("Pía quiere una caja para guardar 6 fichas, cada una de 2 cm de ancho, en fila. Hace un modelo de papel de 10 cm de ancho. ¿Caben las fichas? ¿Cuánto falta?", "No caben: 6 por 2 es 12 cm y el modelo mide 10 cm; faltan 2 cm, hay que agrandarlo a 12 cm", "Calcula el ancho necesario y compara."),
    sc=[
        ("¿Un modelo se hace antes o después del objeto final?", "Antes", "Sirve para probar."),
        ("¿Dónde corriges un error: en el modelo o en el objeto final?", "En el modelo", "Así no gastas el material final."),
        ("¿El modelo puede ser de papel o cartón?", "Sí", "Son materiales simples."),
    ],
    open_task=(
        "Haz un modelo de papel o cartón de una caja para guardar 4 lápices. Mide el ancho de tus lápices y prueba. Escribe si cabe, qué cambiaste y cuál es la medida final con unidad.",
        "Hice un modelo de papel de 6 cm. Con 4 lápices no cabían. Lo cambié a 7 cm. Medida final: 7 cm.",
        ["hace un modelo", "prueba con objetos reales", "anota qué cambió", "escribe una medida con unidad"],
        ["modelo de papel", "nota con la medida final"],
        ["no probar con objetos reales", "medida sin unidad"],
        "Pregunta: «¿qué aprendiste con tu modelo que no sabías antes?». Si no cambió nada, pide que pruebe con otro objeto.",
    ),
    reinforce="Haz un modelo de papel de una cajita que quepa un borrador.",
    extend="Haz un modelo de la misma caja con otra forma y compara cuál guarda mejor.",
)

reg(
    OA1, 5,
    materials="Hoja, lápiz y la tabla de este cuaderno. No necesitas materiales especiales.",
    use="Aprenderé a elegir la mejor idea comparando criterios en una tabla. Sirve para decidir con razones y no solo por gusto.",
    prior=["Sé hacer tres ideas distintas.", "Sé que un criterio es algo que se puede comprobar."],
    explain=[
        "Después de hacer varias ideas toca elegir. Para elegir bien usa criterios que se puedan comprobar. Por ejemplo: cabe en la mochila, pesa poco, se arma en menos de 10 minutos.",
        "Una tabla de decisión ayuda. En cada fila va una idea y en cada columna un criterio. Marcas con un visto si la idea cumple y con una equis si no cumple. Después cuentas los vistos.",
        "La idea con más vistos suele ser la mejor, pero revisa con calma. Si dos ideas empatan, un criterio importante puede decidir. Y la razón para elegir debe ser un criterio, no que «se ve más lindo».",
    ],
    vocab=[("criterio", "algo comprobable que el objeto debe cumplir"), ("tabla de decisión", "tabla para comparar ideas con criterios"), ("empatar", "tener el mismo número de vistos"), ("decisión", "elegir una opción con razones")],
    worked=[
        ("Contar vistos", "Dos ideas y tres criterios. Idea A cumple 2 criterios. Idea B cumple 3. ¿Cuál se elige?", ["A tiene 2 vistos.", "B tiene 3 vistos.", "B cumple más criterios."], "Se elige la idea B"),
        ("Desempate", "Dos ideas con 2 vistos cada una. El criterio más importante es «cabe en la mochila». A lo cumple y B no. ¿Cuál se elige?", ["Hay empate en total.", "Miro el criterio más importante.", "A cumple ese criterio."], "Se elige la idea A"),
    ],
    mistakes=[
        ("Elegir la idea porque «se ve más linda».", "No es un criterio comprobable.", "Elige por los criterios de la tabla."),
        ("Contar los vistos y no mirar los criterios importantes.", "A veces un criterio pesa más.", "Revisa también cuál criterio es esencial."),
    ],
    R=[
        ("Una idea cumple 3 criterios y otra cumple 1. ¿Cuál cumple más?", "La de 3", "3 es más que 1."),
        ("En la tabla, un visto significa que la idea cumple. ¿Una equis significa cumple o no cumple?", "No cumple", "La equis marca que no cumple."),
        ("¿«Se ve más lindo» es un criterio comprobable? Responde sí o no.", "No", "No se puede medir."),
    ],
    C=[
        ("¿Para qué sirve una tabla de decisión?", "Para comparar ideas con criterios", "Ordena la comparación."),
        ("Si hay empate, ¿qué ayuda a decidir: el criterio más importante o tirar una moneda?", "El criterio más importante", "La decisión debe tener razones."),
        ("¿Cuál es un criterio comprobable: «pesa menos de 500 g» o «es simpático»?", "Pesa menos de 500 g", "Se puede medir con una balanza."),
    ],
    A=[
        ("Idea A: cumple «cabe en la mochila» y «pesa poco», pero no «se arma rápido». Idea B: cumple solo «se arma rápido». ¿Cuántos vistos tiene A?", "2", "Cumple dos criterios."),
        ("Tres criterios y tres ideas. A tiene 1 visto, B tiene 3, C tiene 2. ¿Qué idea eliges?", "B", "Tiene más vistos."),
        ("Criterios: cabe en 20 cm, pesa menos de 1 kg. Idea con 25 cm de largo y 500 g. ¿Cumple «cabe en 20 cm»?", "No", "25 cm es mayor que 20 cm."),
    ],
    Z=[
        ("Dos ideas empatan en vistos. Una es «se arma en 5 minutos» y otra es «es más bonita». ¿Con cuál criterio puedes justificar mejor?", "Se arma en 5 minutos", "Es comprobable con un reloj."),
        ("Una compañera eligió la idea con menos vistos. ¿Qué pregunta le haces para entender su razón?", "¿Qué criterio importante cumple esa idea?", "Un criterio esencial podría pesar más."),
    ],
    D=[
        ("Idea A: cumple 3 de 4 criterios. Idea B: cumple 3 de 4, pero no cumple «es seguro para un niño». ¿Cuál eliges y por qué?", "A, porque B no cumple el criterio de seguridad", "La seguridad es esencial."),
        ("Escribe tres criterios comprobables para un soporte de lápices.", "Por ejemplo: sostiene 5 lápices; no se cae al empujarlo suave; mide menos de 15 cm de alto", "Tres criterios que se pueden probar."),
    ],
    ctx=("Rita compara dos soportes de papel para lápices. Criterios: sostiene 3 lápices, mide menos de 12 cm, se arma en 10 minutos. Idea 1 cumple los tres. Idea 2 cumple solo uno. ¿Cuál elige y qué escribe como razón?", "Elige la idea 1, porque cumple los tres criterios", "La razón es la cantidad de criterios cumplidos."),
    sc=[
        ("¿Se elige por criterios o por gusto?", "Por criterios", "Los criterios dan razones."),
        ("¿La equis marca que cumple o que no cumple?", "Que no cumple", "Es el signo de no cumplir."),
        ("¿Qué idea eliges si A tiene 2 vistos y B tiene 3?", "B", "Tiene más vistos que A."),
    ],
    open_task=(
        "Usa estas tres ideas para sujetar un dibujo en la pared: A marco de cartón, B tira con cinta de papel, C gancho de papel doblado. Criterios: no rompe el dibujo, se saca fácil, usa menos de 2 materiales. Haz una tabla, marca vistos y equis, y elige con una razón.",
        "A: no rompe sí, se saca fácil no, menos de 2 materiales no. B: sí, sí, sí. C: sí, no, sí. Elijo B porque cumple los tres.",
        ["hace una tabla con ideas y criterios", "marca cumple o no cumple", "cuenta", "elige con una razón"],
        ["tabla de decisión", "frase con la elección y la razón"],
        ["elegir por gusto", "no contar los vistos"],
        "Pregunta: «¿qué criterio te hizo elegir?». Si dice «porque es lindo», pídele que use un criterio de la tabla.",
    ),
    reinforce="Compara dos mochilas de tu casa con dos criterios y elige una.",
    extend="Inventa un criterio nuevo y repite la comparación de las tres ideas.",
)

# ------------------------------------------------------------------ OA 02
reg(
    OA2, 1,
    materials="Una hoja y un lápiz. Los objetos de ejemplo están descritos en este cuaderno.",
    use="Aprenderé a decir qué resultado quiero y qué acciones hacen falta para lograrlo. Sirve para trabajar con orden.",
    prior=["Sé que un objeto se construye con pasos.", "Sé que un diseño tiene criterios."],
    explain=[
        "Antes de construir, escribe el resultado que quieres. El resultado es cómo debe quedar el objeto terminado. Por ejemplo: una caja de cartón de 10 cm de alto que guarda 5 lápices.",
        "Para llegar al resultado se hacen acciones. Una acción es algo que haces con las manos, como medir, cortar, doblar o pegar. Cada acción empieza con un verbo: medir, cortar, doblar, pegar.",
        "Escribe las acciones en frases cortas. Si el resultado es la caja, algunas acciones son: medir el cartón, cortar el cartón, doblar los lados, pegar con cinta. Así sabes qué hacer sin olvidar nada.",
    ],
    vocab=[("resultado", "cómo debe quedar el objeto terminado"), ("acción", "algo que haces, como cortar o pegar"), ("verbo", "palabra que dice lo que se hace"), ("objeto terminado", "el objeto listo para usar")],
    worked=[
        ("Escribir el resultado", "Quieres un portalápices de cartón de 10 cm de alto. Escribe el resultado.", ["Digo qué objeto es: portalápices.", "Agrego el material: cartón.", "Agrego una medida con unidad: 10 cm de alto."], "Un portalápices de cartón de 10 cm de alto"),
        ("Encontrar las acciones", "¿Qué acciones hacen falta para el portalápices? Escribe tres.", ["Primero se mide el cartón.", "Luego se corta.", "Después se dobla y se pega."], "Medir, cortar, doblar y pegar el cartón"),
    ],
    mistakes=[
        ("Escribir como acción «un pegamento».", "Pegamento es un material, no una acción.", "Escribe una acción con verbo: «pegar los lados»."),
        ("Escribir solo «la caja» como resultado.", "No dice cómo debe quedar.", "Agrega medidas y para qué sirve."),
    ],
    R=[
        ("«Cortar» y «pegar», ¿son acciones o materiales?", "Acciones", "Son cosas que se hacen."),
        ("El resultado es cómo queda el objeto al final. ¿Se escribe antes o después de construir?", "Antes", "Guía el trabajo."),
        ("«Doblar» es un verbo. ¿Es una acción? Responde sí o no.", "Sí", "Dice qué se hace."),
    ],
    C=[
        ("¿Qué es el resultado de un trabajo?", "Cómo debe quedar el objeto terminado", "Es el objetivo final."),
        ("¿Qué palabra al comienzo de una frase nos dice que es una acción?", "Un verbo", "Los verbos dicen lo que se hace."),
        ("Una caja que guarda 5 lápices y mide 10 cm de alto, ¿es un resultado o una acción?", "Un resultado", "Describe el objeto terminado."),
    ],
    A=[
        ("Escribe el resultado de este caso: una repisa de cartón que sostiene 3 libros livianos.", "Una repisa de cartón que sostiene 3 libros livianos", "Indica objeto, material y qué logra."),
        ("Para un marcador de página de papel, ¿cuál es una acción: «cortar una tira» o «tijera»?", "Cortar una tira", "Tiene verbo y es algo que se hace."),
        ("Resultado: un sobre de papel. Elige las dos acciones necesarias: doblar el papel, mojar el piso, pegar los bordes.", "Doblar el papel y pegar los bordes", "Son las que construyen el sobre."),
    ],
    Z=[
        ("Un compañero escribió: «Resultado: cortar cartón». ¿Es resultado o acción? Explica.", "Es una acción", "Cortar es algo que se hace; no dice cómo queda."),
        ("Para la caja, dos niños proponen acciones: Ana «medir, cortar, pegar» y Beto «pegar, cortar, medir». ¿Quién tiene un orden más lógico?", "Ana", "Primero se mide, luego se corta, al final se pega."),
    ],
    D=[
        ("Escribe el resultado y cuatro acciones para hacer un portalápices de cartón de 8 cm de alto.", "Resultado: portalápices de cartón de 8 cm. Acciones: medir, cortar, doblar, pegar", "Cada acción lleva verbo."),
        ("Un resultado dice «una caja». ¿Qué dos datos agregarías para que sea más claro?", "El material y una medida, por ejemplo", "Un resultado claro se puede comprobar."),
    ],
    ctx=("Tato quiere hacer una bolsita de papel para guardar 3 tarjetas. Escribe el resultado y cuatro acciones con verbo.", "Resultado: bolsita de papel de 10 cm para 3 tarjetas. Acciones: medir, cortar, doblar, pegar", "Resultado claro y acciones con verbo."),
    sc=[
        ("¿El resultado dice cómo queda el objeto?", "Sí", "Es el objeto terminado."),
        ("¿«Pegar» es acción o material?", "Acción", "Es algo que se hace."),
        ("¿Cada acción empieza con un verbo?", "Sí", "El verbo dice lo que haces."),
    ],
    open_task=(
        "Escoge un objeto: una caja de cartón de 10 cm de alto, un marcador de página de papel o una bolsita de papel. Escribe el resultado con una medida y cuatro acciones, cada una con verbo.",
        "Objeto: marcador de papel. Resultado: tira de papel de 15 cm de largo. Acciones: medir 15 cm, cortar la tira, doblar la punta, decorar con lápiz.",
        ["escribe un resultado con medida", "escribe cuatro acciones", "cada acción tiene verbo"],
        ["ficha con resultado y acciones"],
        ["poner materiales como acciones", "resultado sin medidas"],
        "Pregunta: «¿esa palabra dice qué haces o qué usas?». Si dice qué usa, es material.",
    ),
    reinforce="Escribe el resultado y tres acciones para hacer un avión de papel.",
    extend="Compara tu lista de acciones con la de un compañero y busca una que falte.",
)

reg(
    OA2, 2,
    materials="Una hoja y lápiz. Los materiales y herramientas se describen en este cuaderno.",
    use="Aprenderé a separar los materiales de las herramientas. Sirve para saber qué reunir antes de construir.",
    prior=["Sé decir el resultado y las acciones.", "Conozco tijeras, regla y pegamento."],
    explain=[
        "Un material es lo que forma parte del objeto y queda en él: papel, cartón, cinta, fibras como lana o hilo, o plástico limpio. Una herramienta es lo que usas para trabajar y que luego guardas: regla, tijeras, lápiz.",
        "Una buena pregunta es: ¿queda en el objeto o lo guardo al final? Si queda en el objeto, es material. Si lo guardas, es herramienta. El pegamento queda pegado: es material. Las tijeras se guardan: son herramienta.",
        "Cada herramienta ayuda a una acción. La regla ayuda a medir, las tijeras a cortar, el lápiz a marcar. Antes de empezar, escribe dos listas: una de materiales y otra de herramientas. Así no se te olvida nada. Las tijeras escolares se usan con un adulto cerca y sin apuntar a nadie.",
    ],
    vocab=[("material", "lo que queda en el objeto terminado"), ("herramienta", "lo que se usa para trabajar y se guarda"), ("fibra", "hilo o lana delgada"), ("lista", "palabras ordenadas una bajo otra")],
    worked=[
        ("Clasificar", "Para una caja: cartón, regla, cinta, tijeras. ¿Cuáles son materiales y cuáles herramientas?", ["El cartón queda en la caja: material.", "La cinta queda pegada: material.", "La regla y las tijeras se guardan: herramientas."], "Materiales: cartón y cinta. Herramientas: regla y tijeras"),
        ("Herramienta y acción", "¿Qué herramienta ayuda a la acción «medir»?", ["Medir es saber cuánto mide algo.", "Una regla muestra los centímetros.", "Elijo la regla."], "La regla"),
    ],
    mistakes=[
        ("Poner el pegamento en la lista de herramientas.", "El pegamento queda en el objeto.", "Pregúntate: ¿queda en el objeto? Entonces es material."),
        ("Decir que las tijeras son material.", "Las tijeras se guardan al terminar.", "Son herramienta."),
    ],
    R=[
        ("La regla se guarda al terminar. ¿Es material o herramienta?", "Herramienta", "No queda en el objeto."),
        ("El cartón queda en la caja. ¿Es material o herramienta?", "Material", "Forma parte del objeto."),
        ("El hilo es una fibra. ¿Es material o herramienta si queda en el objeto?", "Material", "Queda en el objeto."),
    ],
    C=[
        ("¿Qué pregunta ayuda a distinguir un material de una herramienta?", "¿Queda en el objeto o se guarda al final?", "Esa pregunta separa ambos."),
        ("¿La lana es un material de tipo fibra o una herramienta?", "Un material de tipo fibra", "Queda en el objeto."),
        ("¿Qué herramienta ayuda a la acción «cortar»: las tijeras o la regla?", "Las tijeras", "Cortan el papel."),
    ],
    A=[
        ("Lista: papel, lápiz, tijeras, cinta de papel. Escribe cuáles son materiales.", "Papel y cinta de papel", "Se quedan en el objeto."),
        ("Lista: botella de plástico limpia, lana, regla. ¿Cuántas herramientas hay?", "1", "Solo la regla es herramienta."),
        ("Para marcar una línea recta de 10 cm, ¿qué usas: regla y lápiz o cinta y lana?", "Regla y lápiz", "Son herramientas de medir y marcar."),
    ],
    Z=[
        ("Un niño puso «cinta» en herramientas. ¿Por qué es un error? Responde brevemente.", "Porque la cinta queda en el objeto", "Lo que queda es material."),
        ("¿Las tijeras pasan a ser material de la caja que cortas con ellas? Responde sí o no y di por qué.", "No, porque se guarda", "Se guarda: es una herramienta."),
    ],
    D=[
        ("Para un barco de papel y botella de plástico limpia, escribe una lista de materiales y una de herramientas.", "Materiales: papel, botella de plástico limpia, cinta. Herramientas: tijeras, regla", "Separa lo que queda de lo que se guarda."),
        ("Una fibra, un papel, un plástico y un cartón. ¿Son todos materiales o hay herramientas? Responde.", "Todos son materiales", "Quedan en el objeto."),
    ],
    ctx=("Cami hará un sobre con papel, pegamento en barra, regla y tijeras escolares. Haz las listas de materiales y de herramientas.", "Materiales: papel y pegamento en barra. Herramientas: regla y tijeras", "Pegamento queda; regla y tijeras se guardan."),
    sc=[
        ("¿Queda en el objeto: material o herramienta?", "Material", "Eso define al material."),
        ("¿La regla es herramienta?", "Sí", "Se guarda al terminar el trabajo."),
        ("¿Un hilo es material?", "Sí", "Es una fibra que queda en el objeto."),
    ],
    open_task=(
        "Escoge un objeto: un llavero de lana, una caja de cartón o un barco de botella de plástico limpia. Escribe dos listas: materiales y herramientas. En cada lista pon al menos tres elementos y anota qué acción ayuda cada herramienta.",
        "Llavero de lana. Materiales: lana, cartón, cinta. Herramientas: tijeras escolares (cortar), regla (medir), lápiz (marcar).",
        ["hace dos listas", "pone al menos tres elementos en cada una", "asocia cada herramienta a una acción"],
        ["dos listas", "frase con herramienta y acción"],
        ["mezclar materiales y herramientas"],
        "Pregunta: «¿queda en el objeto?». Revisa cada ítem con esa pregunta.",
    ),
    reinforce="Mira tu estuche y separa lo que sería material y lo que sería herramienta.",
    extend="Elige un objeto y piensa un material nuevo que lo mejore.",
)

reg(
    OA2, 3,
    materials="Hojas y tarjetas de papel con los pasos. Puedes escribir cada paso en un trozo de papel.",
    use="Aprenderé a ordenar los pasos de una tarea y saber cuál depende de otro. Sirve para no cometer errores de orden.",
    prior=["Sé separar materiales y herramientas.", "Sé escribir acciones con verbo."],
    explain=[
        "Los pasos de un trabajo tienen un orden. Algunos no se pueden hacer antes que otros. Esa relación se llama dependencia: un paso depende de otro cuando necesita que el otro ya esté hecho.",
        "Por ejemplo, no puedes cortar una tira antes de medirla, porque cortar depende de medir. Tampoco puedes pegar dos partes antes de cortarlas. En cambio, preparar la regla y el lápiz puede hacerse al comienzo, sin esperar.",
        "Para ordenar, pregúntate: ¿qué debo tener hecho antes de este paso? Escribe cada paso en una tarjeta y muévelas hasta que el orden tenga sentido. Numera los pasos del 1 en adelante.",
    ],
    vocab=[("orden", "cuál paso va primero, segundo y así"), ("dependencia", "un paso necesita que otro esté hecho"), ("primero", "lo que se hace al comienzo"), ("después", "lo que se hace luego")],
    worked=[
        ("Ordenar pasos", "Pasos para un marcador: cortar la tira, medir 15 cm, decorar. Ordénalos.", ["Para cortar necesito saber cuánto.", "Primero se mide.", "Luego se corta y al final se decora."], "1 medir, 2 cortar, 3 decorar"),
        ("Encontrar la dependencia", "¿Qué paso depende de «cortar dos partes»: pegar las partes o buscar la regla?", ["Para pegar necesito que las partes existan.", "Buscar la regla no depende de cortar.", "Pegar depende de cortar."], "Pegar las partes depende de cortar"),
    ],
    mistakes=[
        ("Pegar antes de cortar.", "Aún no existen las partes que se pegan.", "Revisa qué paso necesita que otro esté hecho."),
        ("Ordenar por orden de gusto.", "El orden depende de la tarea, no del gusto.", "Pregunta: ¿qué debo tener antes?"),
    ],
    R=[
        ("Medir o cortar: ¿cuál va primero en una tira de papel?", "Medir", "Se mide antes de cortar."),
        ("Pegar o cortar: ¿cuál va primero si hay que unir dos partes?", "Cortar", "Antes de pegar las partes deben existir."),
        ("Un paso que necesita que otro esté hecho tiene una...", "Dependencia", "Así se llama esa relación."),
    ],
    C=[
        ("¿Qué pregunta ayuda a ordenar pasos?", "¿Qué debo tener hecho antes?", "Muestra la dependencia."),
        ("¿Se puede doblar una caja antes de cortar el cartón? Responde sí o no.", "No", "Doblar depende de cortar."),
        ("¿Qué paso puede hacerse al comienzo sin esperar a otro: reunir la regla o pegar los lados?", "Reunir la regla", "No depende de ningún paso."),
    ],
    A=[
        ("Ordena: pegar los lados, medir el cartón, cortar el cartón. Escribe el orden con números.", "1 medir, 2 cortar, 3 pegar", "Cada paso depende del anterior."),
        ("Pasos: elegir material, dibujar el boceto, construir. Escribe cuál va último.", "Construir", "Se construye con material y boceto listos."),
        ("En un barco de papel: A doblar el papel, B conseguir el papel. ¿Cuál es primero?", "B, conseguir el papel", "Sin papel no se puede doblar."),
    ],
    Z=[
        ("Dos niñas ordenan: Lía «cortar, medir, pegar» y Pía «medir, cortar, pegar». ¿Cuál orden es correcto y por qué?", "El de Pía, porque se mide antes de cortar", "Cortar depende de medir."),
        ("Un niño pinta una caja y la dobla enseguida con la pintura mojada. ¿Está bien o mal? Explica en una frase.", "Mal, porque la pintura debe secar antes de doblar", "La pintura mojada mancha y se corre."),
    ],
    D=[
        ("Ordena seis pasos: pegar partes, medir, reunir materiales, cortar, decorar la caja ya armada, probar. Escribe el orden con números.", "1 reunir materiales, 2 medir, 3 cortar, 4 pegar partes, 5 decorar, 6 probar", "Cada paso depende del anterior."),
        ("En la lista anterior, ¿qué paso puede hacerse al mismo tiempo que «medir»? Responde con una frase.", "Preparar la regla y el lápiz, por ejemplo", "No depende de otros."),
    ],
    ctx=("Mía arma una caja. Tiene estas tarjetas: pegar, doblar, medir, cortar. Ordénalas y di qué paso depende de cuál.", "Medir, cortar, doblar, pegar. Cortar depende de medir; doblar depende de cortar; pegar depende de doblar", "Cada paso necesita el anterior."),
    sc=[
        ("¿Medir va antes o después de cortar?", "Antes", "Para cortar bien hay que saber cuánto."),
        ("¿Una dependencia significa que un paso necesita a otro?", "Sí", "Es la definición."),
        ("¿Pegar va antes de cortar si pegas dos partes?", "No", "Antes hay que cortarlas."),
    ],
    open_task=(
        "Ordena estos pasos para hacer un sobre: pegar los bordes, doblar el papel, medir el papel, cortar el papel. Numera del 1 al 4 y escribe qué paso depende de cuál.",
        "1 medir, 2 cortar, 3 doblar, 4 pegar bordes. Cortar depende de medir; doblar depende de cortar; pegar depende de doblar.",
        ["ordena los cuatro pasos", "usa números", "explica al menos dos dependencias"],
        ["pasos numerados", "frases con dependencias"],
        ["ordenar por gusto", "invertir medir y cortar"],
        "Pregunta: «¿puedes hacer este paso si el anterior no está hecho?». Si puede, revisa si es una dependencia real.",
    ),
    reinforce="Ordena los pasos para lavarte los dientes y di cuál depende de cuál.",
    extend="Busca un paso de un trabajo que pueda hacerse al mismo tiempo que otro.",
)

reg(
    OA2, 4,
    materials="Una hoja y un lápiz. Puedes copiar la tabla del cuaderno.",
    use="Aprenderé a juntar acciones, materiales y herramientas en un plan de trabajo. Sirve para trabajar sin olvidar nada.",
    prior=["Sé ordenar pasos.", "Sé separar materiales y herramientas."],
    explain=[
        "Un plan de trabajo reúne todo lo que aprendiste. Tiene el resultado, los pasos en orden, los materiales y las herramientas. También puede decir quién hace cada paso si trabajan en equipo.",
        "Una forma útil es una tabla con tres columnas: paso, material y herramienta. En cada fila va una acción, lo que se usa y lo que ayuda. Por ejemplo: medir el cartón, cartón, regla.",
        "Antes de empezar, revisa el plan con una pregunta: ¿tengo todo lo que dice? Si algo falta, no empieces. Durante el trabajo marca los pasos que ya hiciste. Un plan claro permite que otra persona trabaje con él.",
    ],
    vocab=[("plan de trabajo", "lista ordenada de pasos con materiales y herramientas"), ("columna", "lista vertical de una tabla"), ("fila", "lista horizontal de una tabla"), ("revisar", "mirar con cuidado antes de empezar")],
    worked=[
        ("Completar una fila", "Paso: cortar la tira. Material: papel. ¿Qué herramienta anotas?", ["Cortar se hace con tijeras.", "Las tijeras se guardan: son herramienta.", "Anoto tijeras escolares."], "Tijeras escolares"),
        ("Revisar el plan", "El plan dice que usarás regla, papel y tijeras. En tu mesa hay papel y regla. ¿Puedes empezar?", ["Comparo la lista con lo que tengo.", "Faltan las tijeras.", "Debo conseguirlas antes."], "No, faltan las tijeras"),
    ],
    mistakes=[
        ("Empezar a trabajar sin revisar si tienes todo.", "Te detienes a medio camino.", "Revisa el plan contra tus materiales y herramientas."),
        ("Dejar columnas vacías en la tabla.", "El plan queda incompleto.", "Cada paso lleva material y herramienta, o una raya si no usa."),
    ],
    R=[
        ("Un plan de trabajo tiene pasos, materiales y herramientas. ¿Falta algo si no tiene los pasos?", "Sí", "Los pasos son lo principal."),
        ("En la tabla, ¿la palabra «fila» es una línea horizontal o vertical?", "Horizontal", "La fila va de lado a lado."),
        ("Antes de empezar, ¿revisas que tienes todo o empiezas de inmediato?", "Revisas que tienes todo", "Así no te detienes."),
    ],
    C=[
        ("¿Qué tres cosas reúne un plan de trabajo?", "Pasos, materiales y herramientas", "Es el resumen de la tarea."),
        ("¿Para qué sirve revisar el plan antes de empezar?", "Para saber si tienes todo", "Evita detenerte a mitad."),
        ("¿Se anota el paso y su herramienta en la misma fila?", "Sí", "Así queda ordenado."),
    ],
    A=[
        ("Paso: medir 15 cm. Material: papel. ¿Qué herramienta va en la fila: regla o cinta?", "Regla", "La regla mide centímetros."),
        ("Plan para una caja: cartón, cinta, tijeras, regla. En tu mesa hay cartón, regla y cinta. ¿Qué te falta?", "Tijeras", "No están en la mesa."),
        ("Completa la fila: Paso 2, cortar el cartón. Herramienta: ___. Elige entre tijeras escolares y lápiz.", "Tijeras escolares", "Cortan el cartón."),
    ],
    Z=[
        ("Un plan no dice quién hace cada paso y el equipo discute. ¿Qué podrían agregar a la tabla?", "Una columna con el nombre de quién hace cada paso", "Así cada uno sabe su tarea."),
        ("Un compañero dice: «No necesito el plan, me acuerdo». ¿Qué ventaja tiene escribirlo? Responde en una frase.", "Otra persona puede seguirlo y no se olvida nada", "Un plan escrito se comparte."),
    ],
    D=[
        ("Escribe un plan de 4 filas para hacer un marcador de papel: paso, material y herramienta en cada fila.", "Medir (papel, regla); cortar (papel, tijeras); doblar (papel, ninguna); decorar (papel, lápices de color)", "Cuatro filas completas."),
        ("Un plan dice 6 pasos. Ya hiciste 4. ¿Cuántos faltan?", "2", "6 menos 4 es 2."),
    ],
    ctx=("Tomás y Eli hacen un sobre. Plan: 1 medir (papel, regla), 2 cortar (papel, tijeras), 3 doblar (papel), 4 pegar (pegamento en barra). Tienen papel, regla y pegamento. ¿Qué les falta y desde qué paso?", "Les faltan las tijeras; no pueden pasar del paso 2", "Cortar requiere tijeras."),
    sc=[
        ("¿Un plan de trabajo tiene pasos en orden?", "Sí", "Es su parte principal."),
        ("¿Se revisa el plan antes o después de empezar?", "Antes", "Para no quedarse sin algo."),
        ("¿La herramienta de medir 15 cm es la regla?", "Sí", "La regla mide centímetros."),
    ],
    open_task=(
        "Haz un plan de trabajo en una tabla de cuatro filas para uno de estos objetos: una bolsita de papel o un marcador de página. Columnas: paso, material, herramienta. Revisa el plan con tus cosas y anota si te falta algo.",
        "Marcador: 1 medir 15 cm (papel, regla); 2 cortar (papel, tijeras escolares); 3 doblar la punta (papel, ninguna); 4 decorar la punta (papel, lápices de color). Me faltan los lápices de color.",
        ["tabla con cuatro pasos en orden", "cada fila con material y herramienta", "revisa y anota lo que falta"],
        ["tabla del plan", "nota de revisión"],
        ["pasos desordenados", "columnas vacías"],
        "Pregunta: «¿puede otra persona hacer el objeto solo con tu plan?». Si no, falta algún dato.",
    ),
    reinforce="Escribe un plan de tres pasos para armar un barco de papel: paso, material y herramienta.",
    extend="Agrega una columna «quién» y reparte el plan entre dos personas.",
)

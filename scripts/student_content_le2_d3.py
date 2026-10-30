"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 28 (vocabulario en lo oral), OA 29 (juego de roles) y OA 30 (recitación)."""
from __future__ import annotations

from student_lessons import ex, register

OA28, OA29, OA30 = "LE02 OA 28", "LE02 OA 29", "LE02 OA 30"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 28
reg(
    OA28, 1,
    "Este cuaderno, lápiz y una hoja. Un adulto que lea el texto en voz alta.",
    "Aprenderé a explicar una palabra nueva usando la situación del texto donde apareció. Sirve para entender y recordar palabras nuevas.",
    ["Sé escuchar un texto breve.", "Sé que las palabras tienen significado."],
    [
        "Cuando escuchamos o leemos un texto, a veces aparece una palabra que no conocemos. El contexto es lo que dicen las frases de alrededor. Esas frases son pistas. Con ellas podemos adivinar qué significa la palabra nueva.",
        "Lee esto: «Mateo caminó con sigilo por el pasillo para no despertar a su hermana». La palabra nueva es sigilo. La pista es «para no despertar». Entonces sigilo es hacer algo sin ruido. Luego puedo usar la palabra: «Mi gato se acerca con sigilo».",
        "Para explicar una palabra nueva a otra persona, hago tres pasos: digo la palabra, cuento en qué situación apareció y digo qué significa con mis palabras. Así la palabra queda unida a una escena que recuerdo, y no a una definición que se olvida.",
    ],
    [("vocabulario", "las palabras que conocemos"), ("contexto", "las frases que rodean una palabra"), ("pista", "señal que ayuda a entender"), ("sigilo", "manera de hacer algo sin ruido"), ("significado", "lo que quiere decir una palabra")],
    [
        ("Usar el contexto", "Texto: «Mateo caminó con sigilo para no despertar a su hermana». ¿Qué significa sigilo?", ["Busco la palabra nueva.", "Leo la pista: para no despertar.", "Concluyo."], "Sigilo es hacer algo sin ruido."),
        ("Explicar a otra persona", "Debes explicar la palabra «diminuta» del texto: «Mateo llevaba una linterna diminuta, casi del tamaño de su dedo». ¿Qué dices?", ["Digo la palabra.", "Cuento la situación.", "Digo el significado."], "Diminuta es muy pequeña, como la linterna de Mateo, casi del tamaño de un dedo."),
    ],
    [("Decir una definición sin relacionarla con el texto.", "Se memoriza sin situación.", "Cuenta dónde apareció la palabra."), ("Inventar un significado sin mirar las pistas.", "Se adivina sin leer.", "Busca las frases de alrededor.")],
    [
        E("«Caminó con sigilo para no despertar a su hermana». ¿Sigilo es con ruido o sin ruido?", "Sin ruido", "La pista es no despertar."),
        E("«Una linterna diminuta, del tamaño de un dedo». ¿Diminuta es muy grande o muy pequeña?", "Muy pequeña", "El tamaño de un dedo es pequeño."),
        E("Para entender una palabra nueva, ¿leo las frases de alrededor o las ignoro?", "Leo las frases de alrededor", "Esas frases dan pistas."),
    ],
    [
        E("En Lenguaje: ¿Qué es el contexto?", "Las frases que rodean una palabra", "Ayudan a entenderla."),
        E("¿Por qué conviene unir una palabra a una situación?", "Para recordarla mejor", "Una escena se recuerda más."),
        E("¿Qué tres pasos uso para explicar una palabra?", "Digo la palabra, la situación y su significado", "Así la explico bien."),
    ],
    [
        E("Texto: «Ana se quedó inmóvil cuando vio la abeja. No movió ni un dedo». ¿Qué significa inmóvil?", "Sin moverse", "El texto dice que no movió ni un dedo."),
        E("Texto: «El perro estaba ansioso. Daba vueltas y miraba la puerta esperando a su dueño». ¿Qué significa ansioso?", "Con muchas ganas de que algo pase", "Da vueltas esperando."),
        E("Escribe la palabra «sigilo» en una frase propia.", "Por ejemplo: El gato se acercó con sigilo", "Usa la palabra con su significado."),
    ],
    [
        E("Rita dice: «Sigilo es correr rápido». Según el texto de Mateo, ¿tiene razón?", "No", "Mateo no hacía ruido para no despertar."),
        E("Tito explica «diminuta» así: «Es como la linterna de Mateo, muy chica». ¿Usó el texto?", "Sí", "Nombra la linterna del texto."),
    ],
    [
        E("Texto: «El gigante tenía una voz atronadora. Cuando hablaba, temblaban los vasos». Con las pistas, ¿atronadora quiere decir muy fuerte o muy suave?", "Muy fuerte", "Si tiemblan los vasos, es una voz fuerte."),
        E("Elige la mejor explicación de «ansioso»: a) «Es feliz.» b) «Es cuando esperas con muchas ganas, como el perro que mira la puerta.»", "b", "La b usa la situación del texto."),
    ],
    [E("Texto: «Mi abuela hace pan con mucho esmero: mide la harina, la mezcla despacio y vigila el horno». Explica con tus palabras qué significa esmero, usando una pista del texto.", "Esmero es poner mucho cuidado; la pista es que mide, mezcla despacio y vigila", "Une significado y pista.")],
    [
        E("¿Una pista del texto puede ayudarme a entender una palabra?", "Sí", "El contexto la explica."),
        E("¿Debo inventar un significado sin leer?", "No", "Hay que usar pistas."),
        E("¿Puedo usar la palabra nueva en una frase mía?", "Sí", "Así la practico."),
    ],
    ("Explica una palabra del texto. Escucha o lee: «Teo recibió una noticia que lo dejó atónito. Abrió la boca, abrió los ojos y no pudo decir nada». Con un adulto, haz tres pasos: 1) di la palabra atónito, 2) cuenta qué le pasó a Teo, 3) di qué significa con tus palabras. Luego crea tu propia frase con atónito.",
     "Atónito. A Teo le dieron una noticia y abrió la boca y los ojos sin decir nada. Atónito es estar muy sorprendido. Mi frase: Me quedé atónito cuando vi el arcoíris doble.",
     ["dice la palabra", "usa la pista del texto", "da el significado con sus palabras y crea su frase"], ["explicación oral o escrita", "frase propia"], ["inventar sin pistas", "no usar el texto"],
     "Si inventa, pide que señale la pista del texto que lo hizo pensar eso."),
    "Cuenta a alguien de tu casa una palabra nueva que aprendiste hoy.",
    "Busca la pista de una palabra nueva en un cuento que conozcas y explícala.",
)

reg(
    OA28, 2,
    "Este cuaderno, lápiz y una hoja. Un adulto que escuche tus frases.",
    "Aprenderé a probar una palabra nueva en una frase propia y a aceptar que alguien la reformule. Sirve para usar mejor las palabras nuevas al hablar.",
    ["Sé explicar una palabra con el contexto.", "Sé escuchar a otra persona."],
    [
        "Una palabra nueva se aprende mejor si la uso. Ensayar oralmente es decir la palabra en voz alta en una frase mía. Por ejemplo, con «sigilo»: «El ratón salió con sigilo de su cueva». La frase debe tener sentido con el significado de la palabra.",
        "A veces mi frase sale un poco rara. Si digo «Comí sigilo», no tiene sentido. Entonces alguien puede ayudarme reformulando: «¿Quisiste decir que te acercaste con sigilo?». Reformular es decir lo mismo de otra manera, ayudando sin interrumpir ni burlarse.",
        "Cuando me reformulan, escucho y pruebo de nuevo. No me enojo: me están ayudando a aprender. Y cuando ayudo a otra persona, espero a que termine su idea antes de corregir. Así la persona no pierde la confianza para hablar.",
    ],
    [("ensayar", "practicar antes de usar"), ("frase propia", "frase que invento yo"), ("reformular", "decir lo mismo de otra manera"), ("sentido", "que tiene lógica y se entiende"), ("interrumpir", "cortar a alguien mientras habla")],
    [
        ("Frase con sentido", "Usa la palabra «diminuto». ¿Qué frase armas?", ["Pienso: diminuto es muy pequeño.", "Busco algo muy pequeño.", "Armo la frase."], "La hormiga es diminuta."),
        ("Aceptar una reformulación", "Dijiste: «Mi mochila es diminuta de pesada». Un compañero te dice: «¿Quisiste decir que es muy pesada?». ¿Qué haces?", ["Escucho.", "Veo que diminuta no combina con pesada.", "Pruebo de nuevo."], "Mi mochila es muy pesada. La hormiga es diminuta."),
    ],
    [("Poner la palabra en una frase sin sentido.", "Se usa solo por usarla.", "Revisa si encaja con el significado."), ("Enojarse cuando me corrigen.", "Se siente vergüenza.", "Escucha y prueba de nuevo.")],
    [
        E("«La hormiga es diminuta». ¿Tiene sentido?", "Sí", "La hormiga es muy pequeña."),
        E("«El elefante es diminuto». ¿Tiene sentido?", "No", "Un elefante es grande."),
        E("Si alguien reformula mi frase, ¿escucho o me enojo?", "Escucho", "Me ayuda a aprender."),
    ],
    [
        E("¿Qué es reformular?", "Decir lo mismo de otra manera", "Se mantiene la idea."),
        E("¿Por qué conviene ensayar la palabra en voz alta?", "Para aprender a usarla", "Se usa mejor lo que se practica."),
        E("¿Qué hago al ayudar a alguien con su frase?", "Espero a que termine y luego ayudo", "No lo interrumpo."),
    ],
    [
        E("Usa la palabra «sigilo» en una frase con sentido.", "Por ejemplo: El gato entró con sigilo a la cocina", "El significado es hacer algo sin ruido."),
        E("Usa la palabra «ansioso» en una frase con sentido.", "Por ejemplo: Estaba ansioso esperando mi cumpleaños", "Ansioso es esperar con muchas ganas."),
        E("Reformula esta frase para que tenga sentido: «Comí sigilo».", "Por ejemplo: Caminé con sigilo", "Se usa sigilo como manera de actuar."),
    ],
    [
        E("Pablo dice: «La montaña es diminuta». Ema le dice: «¿Quisiste decir enorme?». ¿Su reformulación ayuda?", "Sí", "Corrige el sentido sin burlarse."),
        E("Luis se ríe de la frase de Ana: «Tengo un perro sigiloso que ladra». Luis la interrumpió. ¿Ayudó?", "No", "Interrumpió y se burló."),
    ],
    [
        E("Elige la frase con sentido: a) «La pulga es diminuta.» b) «La ballena es diminuta.»", "a", "La pulga es muy pequeña."),
        E("Beto dice: «Estoy atónito de comer». ¿Cómo lo ayudarías a reformular? a) «¿Quisiste decir que estás atónito por una sorpresa?» b) «Eso no existe.»", "a", "Ayuda a corregir sin ofender."),
    ],
    [E("Eva dice: «Me quedé inmóvil de contenta bailando». Reformula su idea con la palabra «inmóvil» y con sentido.", "Por ejemplo: Me quedé inmóvil cuando vi una araña", "Inmóvil es no moverse.")],
    [
        E("¿Una frase propia con la palabra nueva me ayuda a aprenderla?", "Sí", "La práctica ayuda."),
        E("¿Puedo ayudar a un compañero sin burlarme?", "Sí", "Reformular es ayudar."),
        E("¿La frase tiene que tener sentido?", "Sí", "Debe concordar con el significado."),
    ],
    ("Ensaya palabras nuevas. Palabras: sigilo (sin ruido), diminuto (muy pequeño), ansioso (con muchas ganas de que algo pase). Di una frase propia con cada una a un adulto. Si una frase no tiene sentido, el adulto te la reformula. Escucha y vuelve a decirla bien. Anota cuál palabra te costó más.",
     "El gato entró con sigilo. La semilla es diminuta. Estoy ansioso por el fin de semana. Me costó más ansioso, pero ya lo entendí.",
     ["dice una frase con cada palabra", "las frases tienen sentido", "acepta la reformulación"], ["frases dichas a un adulto", "nota de la palabra más difícil"], ["frases sin sentido", "molestarse con la ayuda"],
     "Si la frase no tiene sentido, pide que explique con sus palabras qué significa la palabra y que vuelva a intentar."),
    "Dile a alguien de tu casa una frase con una palabra nueva.",
    "Reformula una frase de un compañero ayudando sin interrumpir.",
)

reg(
    OA28, 3,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a comparar palabras parecidas y a elegir la más precisa antes de hablar. Sirve para decir exactamente lo que quiero.",
    ["Sé usar palabras nuevas en frases.", "Sé qué es un significado."],
    [
        "Hay palabras que se parecen pero no significan exactamente lo mismo. «Caminar» y «arrastrarse» son acciones distintas. «Grande», «enorme» y «gigante» hablan del tamaño, pero «gigante» es mucho más que «grande». Elegir bien las palabras hace que me entiendan mejor.",
        "Para elegir la palabra precisa, comparo. Primero pienso qué quiero decir. Luego miro las opciones y veo cuál muestra mejor la idea. Por ejemplo, si mi amiga está muy feliz, «contenta» sirve, pero «radiante» muestra que su alegría se nota mucho.",
        "No siempre la palabra más difícil es la mejor. La mejor es la que dice lo que quiero y que mi audiencia entiende. Si uso «gigante» para un lápiz común, no es preciso. Por eso comparo antes de hablar y me pregunto: ¿esta palabra dice lo que quiero decir?",
    ],
    [("precisión", "decir exactamente lo que quiero"), ("sinónimo", "palabra con significado parecido a otra"), ("comparar", "mirar en qué se parecen y en qué se diferencian"), ("enorme", "muy grande"), ("radiante", "que se ve muy feliz y luminoso")],
    [
        ("Elegir entre dos palabras", "Quieres decir que el dinosaurio era muy muy grande. ¿Usas «grande» o «enorme»?", ["Pienso cuánto es el tamaño.", "Comparo las dos palabras.", "Elijo la que muestra más."], "Enorme."),
        ("Cuidar la precisión", "Dices «es gigante» de tu lápiz común. ¿Es preciso?", ["Veo el tamaño real del lápiz.", "Gigante es mucho más grande.", "Busco otra palabra."], "No; mejor decir: es un lápiz normal."),
    ],
    [("Usar la palabra más difícil siempre.", "Se cree que suena mejor.", "Elige la que mejor dice tu idea."), ("Usar la misma palabra para todo.", "Se conoce poco vocabulario.", "Compara palabras y elige la más precisa.")],
    [
        E("¿Qué es más grande: «grande» o «enorme»?", "Enorme", "Enorme indica un tamaño mayor."),
        E("Para un lápiz común, ¿es preciso decir «gigante»?", "No", "Un lápiz común no es gigante."),
        E("¿Antes de hablar, comparo mis palabras o digo cualquiera?", "Comparo mis palabras", "Así elijo la mejor."),
    ],
    [
        E("¿Qué es un sinónimo?", "Una palabra con significado parecido", "Dice algo semejante."),
        E("¿Por qué comparar palabras parecidas?", "Para elegir la que mejor dice mi idea", "No todas significan igual."),
        E("¿La palabra más difícil siempre es la mejor?", "No", "La mejor es la que dice lo que quiero."),
    ],
    [
        E("Elige la palabra más precisa para una caja muy muy chica: a) «pequeña» b) «diminuta».", "b", "Diminuta es más pequeña que pequeña."),
        E("Elige para alguien muy feliz: a) «contento» b) «radiante».", "b", "Radiante muestra una felicidad que se nota."),
        E("Escribe una palabra más precisa que «bonita» para una canción que suena suave y tranquila.", "Por ejemplo: relajante", "Dice cómo suena, no solo que gusta."),
    ],
    [
        E("Ana dice: «El perro se arrastró bajo la reja». Pedro dice: «El perro caminó bajo la reja». Si el perro iba pegado al suelo, ¿cuál es más precisa?", "La de Ana", "Arrastrarse es ir pegado al suelo."),
        E("Mateo dijo que la hormiga es «enorme». ¿Fue preciso?", "No", "La hormiga es muy pequeña."),
    ],
    [
        E("Elige la palabra más precisa para completar: «Dormí un rato corto, una _____». a) siesta b) noche", "a", "Siesta es un sueño corto."),
        E("Ordena de menor a mayor tamaño: a) enorme, b) pequeño, c) grande.", "b, c, a", "Pequeño es menos que grande y enorme es más."),
    ],
    [E("Quieres contar que tu abuelo guarda un botón muy muy chico. Escribe dos palabras que podrías usar, y elige la más precisa.", "Por ejemplo: chica y diminuta; la más precisa es diminuta", "Compara dos opciones.")],
    [
        E("¿Dos palabras parecidas significan siempre lo mismo?", "No", "Pueden tener matices."),
        E("¿Debo pensar qué quiero decir antes de elegir?", "Sí", "La idea guía la palabra."),
        E("¿Puedo usar «gigante» para algo pequeño?", "No", "No es preciso."),
    ],
    ("Elige la palabra precisa. Para cada situación, escoge la palabra y explica por qué: 1) un perro que camina pegado al suelo, ¿camina o se arrastra? 2) un niño muy feliz, ¿contento o radiante? 3) una hormiga, ¿diminuta o enorme? Di tus tres elecciones a un adulto y explica una.",
     "1) Se arrastra, porque va pegado al suelo. 2) Radiante, porque se nota que está muy feliz. 3) Diminuta, porque es muy pequeña. Expliqué la 3: las hormigas no son enormes.",
     ["elige la palabra pertinente", "compara dos opciones", "explica una elección"], ["tres elecciones", "explicación oral"], ["elegir una palabra por ser difícil", "no explicar"],
     "Si elige mal, pide que piense qué quiere mostrar y compare con la otra palabra."),
    "Busca tres palabras para decir «grande» y ordénalas de menor a mayor.",
    "Elige palabras precisas para describir un día de lluvia.",
)

reg(
    OA28, 4,
    "Este cuaderno, lápiz y una hoja. Un adulto como compañero de conversación.",
    "Aprenderé a usar palabras nuevas dentro de una conversación para aportar al tema. Sirve para hablar con más variedad sin forzar las palabras.",
    ["Sé elegir palabras precisas.", "Sé mantener el tema."],
    [
        "Las palabras nuevas se aprenden mejor cuando las usamos conversando. Pero no debemos meterlas a la fuerza. Una palabra se integra bien cuando ayuda a decir una idea del tema. Si hablamos de un cuento sobre un ratón, «sigilo» puede ayudar a contar cómo se mueve.",
        "Para integrar, escucho primero lo que dicen. Luego pienso si una palabra nueva encaja y la uso en mi aporte. Por ejemplo: Tema: el ratón del cuento. Compañero: «El ratón salió de la cueva». Yo: «Sí, y salió con sigilo para que el gato no lo oyera».",
        "Si la palabra no encaja, no la uso. Es mejor una frase sencilla y clara. Y si alguien usa mal una palabra, no lo interrumpo para corregirlo: espero a que termine, y después, si hace falta, lo ayudo con amabilidad.",
    ],
    [("integrar", "poner una palabra dentro de una conversación"), ("aporte", "idea que agrego al tema"), ("forzar", "usar algo aunque no encaje"), ("encajar", "quedar bien en un lugar"), ("amable", "que trata bien a los demás")],
    [
        ("Integrar una palabra", "Tema: el ratón del cuento. Tu compañero dice: «El ratón salió de la cueva». Usa «sigilo» en tu aporte.", ["Retomo lo que dijo.", "Pienso cómo salió el ratón.", "Uso sigilo."], "Sí, y salió con sigilo para que el gato no lo oyera."),
        ("No forzar", "Tema: el almuerzo. ¿Conviene decir «sigilo» aquí?", ["Veo el tema.", "Pienso si la palabra encaja.", "Decido que no."], "No; no encaja con el almuerzo, mejor otra palabra."),
    ],
    [("Meter la palabra nueva aunque no tenga relación.", "Se quiere mostrar que se aprendió.", "Úsala solo si ayuda al tema."), ("Interrumpir para corregir a otro.", "Se quiere ayudar rápido.", "Espera a que termine y ayuda con amabilidad.")],
    [
        E("Tema: un gato que se acerca a un pájaro sin hacer ruido. ¿Encaja «sigilo» o «almuerzo»?", "Sigilo", "Describe un movimiento sin ruido."),
        E("Tema: el cumpleaños. ¿Encaja «atónito» si hubo una sorpresa o no encaja?", "Encaja", "Atónito es muy sorprendido."),
        E("Si alguien usa mal una palabra, ¿lo interrumpo o espero que termine?", "Espero que termine", "Así no lo interrumpo."),
    ],
    [
        E("¿Qué significa integrar una palabra?", "Usarla dentro de una conversación", "Debe ayudar al tema."),
        E("¿Por qué no debo forzar una palabra?", "Porque confunde si no encaja", "La conversación pierde claridad."),
        E("¿Cómo ayudo a alguien que usó mal una palabra?", "Con amabilidad, después de que termine", "Respeta su idea."),
    ],
    [
        E("Tema: una mascota que espera a su dueño. Usa la palabra «ansioso» en un aporte.", "Por ejemplo: El perro estaba ansioso esperando a su dueño", "Ansioso encaja con la espera."),
        E("Tema: un pez muy pequeño en una pecera. Usa la palabra «diminuto».", "Por ejemplo: El pez es diminuto", "Se refiere a algo muy pequeño."),
        E("Tema: la lluvia en la ventana. ¿Cuál palabra encajaría mejor: «radiante» o «gotear»? Explica con una frase.", "Gotear; el agua gotea por la ventana", "Describe la lluvia."),
    ],
    [
        E("Pedro habla de su perro y de la nada dice «atónito». Nadie entiende. ¿Integró bien la palabra?", "No", "No encaja con el tema."),
        E("Ema dice: «El pájaro se posó con sigilo». Sus compañeros asienten. ¿Integró bien la palabra?", "Sí", "Encaja con el movimiento del pájaro."),
    ],
    [
        E("Conversación: Ana: «El zorro se acercó a las gallinas». Luis: «Sí, y se acercó con sigilo». Beto: «Sí, y sigilo es mi comida favorita». ¿Quién integró mal?", "Beto", "Su frase no encaja."),
        E("Un niño dijo «muy sigilo» y otro lo interrumpió. ¿Qué habría sido mejor?", "Esperar a que terminara y ayudar con amabilidad", "Respeta su idea y su confianza."),
    ],
    [E("Tema de conversación: un cuento de un ratón que sale de noche a buscar queso. Escribe un aporte que use dos de estas palabras: sigilo, diminuto, ansioso.", "Por ejemplo: El ratón diminuto salió con sigilo a buscar queso", "Usa dos palabras con sentido.")],
    [
        E("¿Una palabra nueva debe ayudar al tema?", "Sí", "Debe encajar con el tema."),
        E("¿Puedo corregir a un compañero a mitad de su frase?", "No", "Es mejor esperar su turno."),
        E("¿Una frase sencilla y clara es mejor que una frase forzada?", "Sí", "Se entiende mejor."),
    ],
    ("Conversa con un adulto 2 minutos sobre «un cuento de un ratón que sale de noche». Intenta usar al menos dos palabras: sigilo, diminuto, ansioso, atónito. Úsalas solo cuando encajen. Si el adulto reformula una frase tuya, escucha. Anota qué palabras usaste y si encajaron.",
     "Adulto: El ratón salió de noche. Yo: Sí, y salió con sigilo. Adulto: Era muy pequeño. Yo: Sí, un ratón diminuto, y estaba ansioso por el queso. Usé sigilo, diminuto y ansioso. Todas encajaron.",
     ["usa al menos dos palabras nuevas", "las palabras encajan con el tema", "acepta una reformulación"], ["conversación con un adulto", "anotación de palabras usadas"], ["forzar las palabras", "interrumpir"],
     "Si fuerza una palabra, pregunta si ayuda a contar algo del tema."),
    "Usa una palabra nueva en la mesa cuando conversen.",
    "Ayuda a un compañero a usar una palabra nueva sin interrumpir.",
)

reg(
    OA28, 5,
    "Este cuaderno, lápiz y una hoja. Un adulto como oyente.",
    "Aprenderé a explicar qué hizo más clara una intervención por el uso de una palabra nueva. Sirve para evaluar cómo hablo y mejorar.",
    ["Sé integrar palabras nuevas.", "Sé que una palabra precisa ayuda."],
    [
        "Cuando usamos una palabra nueva, podemos revisar su efecto: ¿ayudó a que la idea se entendiera mejor? Evaluar el efecto es comparar dos formas de decir lo mismo. Por ejemplo: «El gato fue hasta el pájaro» y «El gato se acercó con sigilo al pájaro». La segunda muestra cómo se movió.",
        "Para evaluar hago tres preguntas: ¿la palabra encajó en la idea?, ¿mi compañero entendió mejor?, ¿puedo explicar por qué? Digo, por ejemplo: «La palabra sigilo hizo más clara la intervención porque mostró que el gato no hacía ruido».",
        "Si la palabra no ayudó, también aprendo. Puedo decir: «Usé una palabra que confundió; la próxima vez elegiré otra más sencilla». Evaluar no es decir «salió mal», sino explicar qué cambiaría. Así mejoro cada vez que hablo.",
    ],
    [("efecto", "lo que logra algo en quien escucha"), ("evaluar", "revisar si algo salió bien"), ("claridad", "cuando algo se entiende bien"), ("comparar", "mirar dos cosas para ver diferencias"), ("mejorar", "hacer algo mejor")],
    [
        ("Comparar dos versiones", "Versión A: «El gato fue hasta el pájaro». Versión B: «El gato se acercó con sigilo al pájaro». ¿Cuál se entiende mejor cómo se movió?", ["Leo las dos.", "Busco la diferencia.", "Digo cuál muestra más."], "La B, porque dice que no hacía ruido."),
        ("Evaluar y mejorar", "Dijiste «El ratón es radiante» para un ratón triste. Un compañero no entendió. ¿Qué dices?", ["Reviso si la palabra encaja.", "Veo que no encajó.", "Propongo otra."], "Radiante no encajó porque el ratón estaba triste; mejor diría que está triste."),
    ],
    [("Decir «salió bien» sin explicar por qué.", "Falta una razón.", "Explica qué hizo más clara la intervención."), ("Pensar que una palabra difícil siempre mejora.", "No se mira el efecto.", "Revisa si el compañero entendió mejor.")],
    [
        E("¿Qué se evalúa en esta clase: el efecto de la palabra o el color de la ropa?", "El efecto de la palabra", "Revisamos cómo ayudó."),
        E("«Se acercó con sigilo» ¿muestra más cómo se movió que «fue hasta»?", "Sí", "Sigilo explica que no hacía ruido."),
        E("Si una palabra confundió, ¿lo reconozco o digo que fue perfecta?", "Lo reconozco", "Así puedo mejorar."),
    ],
    [
        E("¿Qué es evaluar el efecto?", "Revisar si la palabra ayudó a entender", "Se compara qué cambió."),
        E("¿Qué pregunta hago para evaluar?", "¿La palabra encajó y se entendió mejor?", "Mide el efecto."),
        E("Si la palabra no ayudó, ¿qué hago?", "Explico qué cambiaría", "Aprendo para la próxima."),
    ],
    [
        E("Compara: A «Ana está contenta» y B «Ana está radiante». ¿Cuál muestra más felicidad?", "B", "Radiante expresa mayor alegría."),
        E("Escribe por qué «sigilo» hizo más clara esta frase: «El gato se acercó con sigilo».", "Porque muestra que se acercó sin ruido", "Explica el efecto de la palabra."),
        E("Escribe una mejora para esta frase: «Estoy muy mucho contento».", "Por ejemplo: Estoy radiante", "Usa una palabra más precisa."),
    ],
    [
        E("Dani dijo «Me gustó mi intervención» y no explicó nada. Eva dijo «Mi palabra diminuto mostró que la caja era muy chica». ¿Quién evaluó mejor?", "Eva", "Explicó el efecto de la palabra."),
        E("Pepe usó «atónito» para hablar de una sopa y nadie entendió. ¿Qué evaluación es correcta: «La palabra no encajó» o «Mi intervención fue perfecta»?", "La palabra no encajó", "Evaluar es ser honesto."),
    ],
    [
        E("Dos intervenciones. A: «Entré a la casa con sigilo porque todos dormían». B: «Entré a la casa porque sí». ¿Cuál queda más clara y por qué?", "A; porque explica cómo entró y por qué", "Tiene una palabra que aporta."),
        E("Después de hablar, Tito dice: «Usé ansioso y mi compañera entendió que esperaba con muchas ganas». ¿Evaluó el efecto?", "Sí", "Dice qué entendió su compañera."),
    ],
    [E("Escucha esta intervención: «Fui al parque y vi un perro diminuto que corría. Estaba ansioso porque su dueño se alejaba». Escribe cuál de las dos palabras aportó más claridad y por qué.", "Por ejemplo: Ansioso, porque mostró lo que sentía el perro", "Evalúa el efecto de una palabra.")],
    [
        E("¿Puedo explicar por qué una palabra ayudó?", "Sí", "Es evaluar el efecto."),
        E("¿Mejorar es reconocer qué no salió bien?", "Sí", "Ayuda a aprender."),
        E("¿Una palabra difícil siempre mejora una frase?", "No", "Solo si encaja."),
    ],
    ("Evalúa el efecto. Di a un adulto una intervención de 3 frases sobre un animal, usando una palabra nueva (sigilo, diminuto, ansioso o atónito). Luego pregúntale si entendió mejor con esa palabra. Responde por escrito o en voz alta: 1) ¿qué palabra usaste? 2) ¿ayudó a que se entendiera mejor? 3) ¿por qué? 4) ¿qué cambiarías?",
     "Dije: Un gato diminuto salió de la caja. Caminó con sigilo. Su dueño estaba atónito. Usé diminuto. Ayudó porque mostró su tamaño. Cambiaría atónito por sorprendido porque mi mamá no lo entendió.",
     ["nombra la palabra y su efecto", "explica por qué ayudó o no", "propone un cambio"], ["intervención oral", "evaluación escrita u oral"], ["decir solo «bien» sin razón", "no proponer cambio"],
     "Si no explica, pregunta qué entendió el adulto gracias a la palabra."),
    "Compara dos frases tuyas, con y sin una palabra nueva, y di cuál queda más clara.",
    "Escribe una mini guía de tres preguntas para evaluar una intervención.",
)

# ================================================================ OA 29
reg(
    OA29, 1,
    "Este cuaderno, lápiz y una hoja. Un adulto o un muñeco como compañero.",
    "Aprenderé a construir un personaje: qué sabe, qué quiere y qué puede hacer. Sirve para jugar a los roles con ideas y sin confundirme.",
    ["Sé jugar a «hacer como si».", "Sé que un personaje tiene un rol."],
    [
        "Un rol es el papel que representamos en un juego, como panadero, guardaparque o capitana de un barco. Para construir un rol, pensamos en tres cosas: qué sabe el personaje, qué quiere y qué puede hacer. Con eso, el personaje tiene una forma de hablar y de actuar.",
        "Por ejemplo, la guardaparque Lila sabe los nombres de las aves. Quiere que los visitantes cuiden el bosque. Puede mostrar caminos y explicar reglas. Cuando la represento, hablo con voz clara y digo cosas como «Por favor, no lleven basura».",
        "Un personaje también tiene límites: no puede hacer cosas imposibles en el juego. Una guardaparque no puede volar. En situaciones ficticias y seguras jugamos con ganas, pero siempre con respeto. No nos burlamos de las personas ni de sus trabajos.",
    ],
    [("rol", "papel que represento en un juego"), ("personaje", "alguien que invento o represento"), ("saber", "lo que el personaje conoce"), ("querer", "lo que el personaje desea lograr"), ("poder", "lo que el personaje puede hacer")],
    [
        ("Armar un rol", "Eres el panadero Mario. ¿Qué sabe, qué quiere y qué puede hacer?", ["Pienso en su trabajo.", "Elijo qué sabe.", "Elijo qué quiere y qué puede."], "Sabe hacer pan, quiere que le guste a los clientes, puede amasar y vender."),
        ("Hablar como el rol", "Eres la guardaparque Lila. ¿Qué dices a unos visitantes?", ["Recuerdo lo que quiere.", "Hablo con voz clara.", "Digo una regla amable."], "Bienvenidos. Por favor, no lleven basura."),
    ],
    [("Hacer que el personaje sepa todo.", "Se olvida que cada rol sabe cosas distintas.", "Elige lo que sabe ese rol."), ("Burlarse del personaje.", "Se cree que da risa.", "Juega con respeto.")],
    [
        E("El panadero Mario, ¿sabe hacer pan o sabe manejar un barco?", "Sabe hacer pan", "Es su trabajo."),
        E("Lila, la guardaparque, quiere cuidar el bosque. ¿Eso es lo que sabe o lo que quiere?", "Lo que quiere", "Quiere es lo que desea lograr."),
        E("Una guardaparque, ¿puede volar en el juego o no?", "No", "Tiene límites reales."),
    ],
    [
        E("¿Qué es un rol?", "El papel que represento en un juego", "Hago como si fuera ese personaje."),
        E("¿Qué tres cosas pienso para construir un rol?", "Qué sabe, qué quiere y qué puede hacer", "Dan forma al personaje."),
        E("¿Por qué no me burlo de los roles?", "Porque se juega con respeto", "Todos los trabajos importan."),
    ],
    [
        E("Eres la capitana Rosa. Escribe qué sabe, qué quiere y qué puede hacer.", "Por ejemplo: Sabe navegar; quiere llegar a salvo; puede dirigir la tripulación", "Tiene las tres partes."),
        E("Eres el cartero Beto. Escribe una frase con la que te presentas.", "Por ejemplo: Buenos días, soy Beto y traigo su carta", "Habla como el rol."),
        E("Eres una doctora. Escribe qué quieres lograr en el juego.", "Por ejemplo: Quiero ayudar a mi paciente", "Es lo que desea el personaje."),
    ],
    [
        E("Nico representa a un bombero. Dice: «Yo vuelo con alas». ¿Es lo que puede hacer un bombero?", "No", "Un bombero no vuela."),
        E("Rosa se burla del cartero que representa Luis. ¿Está jugando con respeto?", "No", "Se burla de él."),
    ],
    [
        E("Elige la mejor ficha para una bibliotecaria: a) sabe de libros, quiere que los cuiden, puede prestarlos. b) sabe nadar, quiere volar, puede cantar.", "a", "La a encaja con el rol."),
        E("En una escena, el panadero Mario dice: «Hoy no tengo harina». ¿Qué no podrá hacer Mario?", "Pan", "Sin harina no se amasa pan."),
    ],
    [E("Vas a jugar a la guardaparque Lila con un adulto. Escribe cómo usarías lo que Lila sabe, quiere y puede hacer en una escena de visitantes.", "Lila sabe los nombres de las aves y los dice; quiere que cuiden el bosque y pide no dejar basura; puede mostrar el camino", "Une las tres partes.")],
    [
        E("¿Todos los roles saben lo mismo?", "No", "Cada rol sabe cosas distintas."),
        E("¿Es seguro jugar situaciones ficticias con respeto?", "Sí", "No hay peligro."),
        E("¿El personaje tiene límites?", "Sí", "No hace cosas imposibles."),
    ],
    ("Construye un rol. Elige uno: panadero, guardaparque, cartera o bibliotecaria. Escribe tres cosas: qué sabe, qué quiere y qué puede hacer. Luego representa tu rol con un adulto durante un minuto, diciendo al menos dos frases propias de ese rol. Juega con respeto.",
     "Rol: bibliotecaria. Sabe dónde está cada libro. Quiere que los niños cuiden los libros. Puede prestarlos y recomendar. Dije: Bienvenido a la biblioteca. Este cuento es muy bueno. Por favor, cuídalo.",
     ["escribe qué sabe, quiere y puede", "habla como el rol", "juega con respeto"], ["ficha escrita", "representación ante un adulto"], ["roles sin ficha", "burla"],
     "Si el rol sabe todo, pregunta qué cosas no sabría una persona con ese trabajo."),
    "Describe a un familiar su trabajo diciendo qué sabe, qué quiere y qué puede hacer.",
    "Crea la ficha de un rol imaginario en un lugar seguro, como un faro.",
)

reg(
    OA29, 2,
    "Este cuaderno, lápiz y una hoja. Un adulto o un muñeco como compañero.",
    "Aprenderé a responder a lo que dice otro personaje en un diálogo. Sirve para que la escena avance y para escuchar de verdad.",
    ["Sé construir un rol.", "Sé esperar mi turno."],
    [
        "En un diálogo de roles, los personajes se responden. No se trata de decir mis frases ensayadas, sino de reaccionar a lo que oí. Si el cliente dice «Quiero pan», el panadero responde «¿Cuánto desea?». Cada respuesta se relaciona con lo anterior.",
        "Una situación es el problema o la escena donde estamos. Por ejemplo: un cliente llega a la panadería y ya no queda pan integral. La situación nos da qué decir. El panadero puede ofrecer otro pan, y el cliente decide.",
        "Para responder bien, hago tres cosas: escucho la frase, pienso qué diría mi personaje y respondo manteniendo mi rol. Si no entiendo algo, hago una pregunta. Así el diálogo se construye entre los dos y nadie queda hablando solo.",
    ],
    [("diálogo", "conversación entre personajes"), ("situación", "escena o problema donde están los personajes"), ("responder", "decir algo relacionado con lo que oí"), ("reaccionar", "actuar según lo que ocurre"), ("mantener el rol", "seguir siendo ese personaje")],
    [
        ("Responder en el rol", "Cliente: «Quiero pan integral». Panadero: ¿qué puede responder si no queda?", ["Escucho.", "Pienso qué haría un panadero.", "Ofrezco una solución."], "Lo siento, hoy no queda integral. Tengo marraqueta fresca."),
        ("Preguntar si no entiendo", "Capitana: «Icen la vela del medio». No sabes cuál es. ¿Qué dices como marinero?", ["Mantengo el rol.", "Hago una pregunta.", "Espero la respuesta."], "Capitana, ¿cuál es la vela del medio, la azul o la blanca?"),
    ],
    [("Decir mi frase sin escuchar.", "Se piensa solo en el guion propio.", "Responde a lo que oíste."), ("Salirme del rol sin avisar.", "Se olvida el personaje.", "Mantén tu rol hasta el fin de la escena.")],
    [
        E("Cliente: «Quiero pan». El panadero responde «¿Cuánto desea?». ¿Se relaciona con lo anterior?", "Sí", "Pregunta por lo que pidió."),
        E("Cliente: «Quiero pan». El panadero responde «Hoy llueve». ¿Responde bien?", "No", "No se relaciona con la petición."),
        E("En un diálogo, ¿respondo a lo que oí o solo digo mi frase ensayada?", "Respondo a lo que oí", "Dialogar es reaccionar."),
    ],
    [
        E("¿Qué es una situación en un juego de roles?", "La escena o problema donde están los personajes", "Da el contexto del diálogo."),
        E("¿Por qué hago una pregunta si no entiendo?", "Para seguir el diálogo sin perderme", "Me ayuda a responder bien."),
        E("¿Qué significa mantener el rol?", "Seguir siendo ese personaje", "No salirme del juego."),
    ],
    [
        E("Eres la doctora. El paciente dice: «Me duele la garganta». Escribe tu respuesta.", "Por ejemplo: Voy a revisarla. ¿Desde cuándo le duele?", "Reacciona a lo dicho."),
        E("Eres el cliente. El panadero dice: «Hoy no queda integral». Escribe tu respuesta.", "Por ejemplo: Entonces llevaré una marraqueta", "Responde con una decisión."),
        E("Eres el marinero. La capitana dice: «¡Hay tormenta!». Escribe tu respuesta.", "Por ejemplo: ¡Entendido, capitana! ¿Bajamos las velas?", "Reacciona y pregunta."),
    ],
    [
        E("Dos niños juegan a la tienda. Uno dice: «Quiero manzanas». El otro dice sus frases ensayadas: «Hoy las peras están baratas». ¿Dialogó bien?", "No", "No respondió a lo pedido."),
        E("Tina, que es bibliotecaria, escucha: «¿Tiene cuentos de dragones?». Responde: «Sí, en el segundo estante». ¿Mantuvo el rol?", "Sí", "Habló como bibliotecaria."),
    ],
    [
        E("Ordena el diálogo: a) Aquí tiene, gracias. b) Hola, quiero dos panes. c) Buenos días, ¿qué desea? d) Son dos panes, por favor.", "c, b, d, a", "Saludo, pedido, confirmación y entrega."),
        E("Situación: el cliente pide un pan que se acabó. El panadero sigue diciendo «Aquí está», sin tenerlo. ¿Cuál es el error?", "No respondió a la situación", "Ignoró que no quedaba pan."),
    ],
    [E("Situación: eres la guardaparque Lila y un visitante dice: «¿Puedo dar de comer a los pájaros?». Escribe tu respuesta manteniendo el rol y cuidando el bosque.", "Por ejemplo: No, por favor. La comida de personas les hace mal. Mejor mirarlos desde lejos", "Responde al visitante cuidando el rol.")],
    [
        E("¿Los personajes se responden entre ellos?", "Sí", "Así hay diálogo."),
        E("¿Puedo preguntar si no entiendo algo?", "Sí", "Ayuda a continuar."),
        E("¿Está bien hablar sin escuchar?", "No", "Hay que reaccionar."),
    ],
    ("Dialoga en una situación. Con un adulto, representen esta escena: «Un cliente llega a la panadería y pide pan integral, pero ya no queda». Una persona es el panadero y la otra el cliente. Hagan al menos 4 intercambios, respondiendo cada uno a lo que dijo el otro. Luego cambien los roles.",
     "Cliente: Buenos días, quiero pan integral. Panadero: Lo siento, hoy no queda. Cliente: ¿Y qué otro pan tiene? Panadero: Tengo marraqueta fresca. Cliente: La llevo, gracias. Panadero: Que le vaya bien.",
     ["responde a lo que dice el otro", "mantiene el rol", "completa cuatro intercambios"], ["escena con un adulto"], ["frases sin relación", "salirse del rol"],
     "Si no responde a lo dicho, repite lo último que dijo su compañero y pídele que responda a eso."),
    "Juega a la tienda con alguien de tu casa durante dos minutos.",
    "Crea una escena de diálogo con un problema y su solución.",
)

reg(
    OA29, 3,
    "Este cuaderno, lápiz y una hoja. Un adulto o un muñeco como compañero.",
    "Aprenderé a ponerme en el lugar de otro personaje sin burlarme. Sirve para entender cómo piensa o se siente otra persona.",
    ["Sé representar un rol.", "Sé dialogar en una situación."],
    [
        "Cambiar de rol es representar a otro personaje de la misma situación. Si antes fui cliente, ahora soy panadero. Así descubro cómo ve la escena la otra persona. Esto se llama probar otra perspectiva, que es la manera de mirar algo desde el lugar de otro.",
        "Para cambiar de rol sin burlarme, pienso: ¿qué siente este personaje?, ¿qué quiere?, ¿qué necesita? Por ejemplo, un cliente puede estar apurado y el panadero, ocupado. Los dos tienen razones. Jugar es entenderlos, no reírse de ellos.",
        "Una burla es imitar para hacer reír de alguien, y duele. Una perspectiva es imitar para comprender, y ayuda. Nunca representamos de forma exagerada a personas por su aspecto, su voz o su origen. Si algo ofende, paramos y cambiamos el juego.",
    ],
    [("perspectiva", "forma de ver algo desde el lugar de otro"), ("cambiar de rol", "representar a otro personaje"), ("burla", "imitar para reírse de alguien"), ("comprender", "entender por qué alguien siente o piensa algo"), ("respeto", "tratar bien a los demás")],
    [
        ("Probar otra perspectiva", "Antes fuiste el cliente apurado. Ahora eres el panadero con muchos pedidos. ¿Qué sientes?", ["Pienso en su trabajo.", "Pienso en su necesidad.", "Digo qué siente."], "Siente apuro y cansancio por tantos pedidos, y quiere atender bien."),
        ("Detectar una burla", "Un niño imita la forma de hablar de un compañero para hacer reír a los demás. ¿Es perspectiva o burla?", ["Veo que se ríe de alguien.", "Duele a esa persona.", "Concluyo."], "Es burla; hay que parar y cambiar el juego."),
    ],
    [("Exagerar a un personaje para que den risa.", "Se cree que así es más gracioso.", "Muestra sus sentimientos con respeto."), ("Seguir si alguien se siente mal.", "Se piensa que es parte del juego.", "Para y cambia el juego.")],
    [
        E("Cambiar de rol, ¿es representar a otro personaje o dejar de jugar?", "Representar a otro personaje", "Vemos la escena desde otro lugar."),
        E("Imitar para comprender, ¿ayuda o duele?", "Ayuda", "Busca entender al otro."),
        E("Imitar para reírse de alguien, ¿es burla o perspectiva?", "Burla", "Hiere a la persona."),
    ],
    [
        E("En Lenguaje: ¿Qué es una perspectiva?", "La forma de ver algo desde el lugar de otro", "Es ponerse en su lugar."),
        E("¿Por qué paro el juego si alguien se siente mal?", "Porque jugar es para disfrutar todos", "Nadie debe sufrir."),
        E("¿Qué pregunto cuando cambio de rol?", "Qué siente, qué quiere y qué necesita", "Ayudan a comprender."),
    ],
    [
        E("Antes fuiste la doctora y ahora eres el paciente con dolor de oído. Escribe qué sientes.", "Por ejemplo: Siento dolor y preocupación; quiero que me revisen", "Muestra la perspectiva del paciente."),
        E("Eres el cliente que no encuentra pan integral. Escribe una frase con respeto.", "Por ejemplo: Entiendo, entonces llevaré otro pan, gracias", "Es amable y comprende."),
        E("Eres el cartero que no encuentra una dirección. Escribe qué sientes y qué haces.", "Por ejemplo: Me siento confundido; pregunto a un vecino", "Muestra sentimiento y acción."),
    ],
    [
        E("Mario hace de panadero ocupado y suspira porque hay mucha fila. Luis se ríe de él. ¿Cuál de los dos probó la perspectiva?", "Mario", "Mario mostró cómo se siente el personaje."),
        E("Ema representa a una persona mayor caminando lento y todos se ríen de cómo habla. ¿Fue respetuoso?", "No", "Se burló de una persona mayor."),
    ],
    [
        E("Elige la mejor forma de representar a un cliente enojado: a) gritando y tirando cosas, b) hablando firme y diciendo qué necesita.", "b", "Muestra enojo sin dañar."),
        E("Si en el juego sientes que alguien exagera un rasgo de una persona real, ¿qué haces?", "Paro y cambio el juego", "Para evitar que alguien se sienta mal."),
    ],
    [E("En la escena de la panadería, ahora eres el panadero. El cliente está apurado y tú tienes muchos pedidos. Escribe lo que dices para ayudarlo con respeto.", "Por ejemplo: Entiendo que tiene apuro. Le atiendo en un momento", "Muestra empatía hacia el cliente.")],
    [
        E("¿Probar otra perspectiva ayuda a entender?", "Sí", "Se piensa como el otro."),
        E("¿Puedo burlarme de cómo habla alguien?", "No", "Es una burla."),
        E("¿Puedo cambiar de rol varias veces?", "Sí", "Así veo la escena de varios lados."),
    ],
    ("Cambia de rol con respeto. Con un adulto, representen la escena de la panadería dos veces: primero tú eres el cliente apurado y luego tú eres el panadero. Después di qué sintió cada personaje y qué comprendiste. No exageres a nadie para hacer reír.",
     "Como cliente estaba apurado y quería rápido mi pan. Como panadero tenía muchos pedidos y me costaba atender rápido. Comprendí que los dos tenían razones.",
     ["representa dos roles", "dice qué sintió cada personaje", "no se burla"], ["dos escenas", "comentario final"], ["exagerar para burlarse", "no decir qué comprendió"],
     "Si exagera, recuerda que el objetivo es comprender, no hacer reír."),
    "Pregunta a alguien de tu casa cómo se siente en su trabajo y escúchalo.",
    "Escribe qué diría un personaje de cuento distinto al protagonista.",
)

reg(
    OA29, 4,
    "Este cuaderno, lápiz y una hoja. Uno o dos compañeros de juego (adultos o hermanos).",
    "Aprenderé a crear una escena en equipo: acordar cómo empieza, qué dificultad aparece y cómo termina. Sirve para trabajar juntos y que todos decidan.",
    ["Sé dialogar en una situación.", "Sé cambiar de rol con respeto."],
    [
        "Una escena en equipo tiene tres partes. El inicio presenta dónde están y qué quieren los personajes. La dificultad es el problema que aparece. El cierre es cómo se resuelve. Antes de actuar, el equipo acuerda estas tres partes en pocas frases.",
        "Por ejemplo: Inicio: tres amigos acampan en el patio. Dificultad: se cae la carpa por el viento. Cierre: la levantan entre todos y se sientan a cantar. Cada uno propone una idea y el equipo elige o une las ideas. Todos tienen un rol. Cuando el equipo escucha mi idea me siento valorado, y cuando yo valoro la idea de otro, él también se siente valorado.",
        "Para que todos decidan, usamos turnos: cada persona propone una cosa antes de que alguien hable por segunda vez. Si una persona decide por todos, la escena no es de equipo. Escuchamos, decimos «sí, y…» o proponemos cambios con respeto.",
    ],
    [("equipo", "grupo que trabaja junto"), ("inicio", "cómo comienza la escena"), ("dificultad", "problema que aparece"), ("cierre", "cómo termina la escena"), ("acuerdo", "decisión que toma el equipo entre todos")],
    [
        ("Acordar inicio, dificultad y cierre", "Tres amigos quieren acampar. ¿Qué acuerdan para su escena?", ["Piensan el inicio.", "Piensan la dificultad.", "Piensan el cierre."], "Inicio: acampan; dificultad: el viento tira la carpa; cierre: la levantan juntos."),
        ("Tomar decisiones entre todos", "Un niño decide todo y no deja hablar a los demás. ¿Qué hace el equipo?", ["Reconocen que es un problema.", "Proponen turnos.", "Escuchan a cada uno."], "Hacen turnos para que cada uno proponga antes de decidir."),
    ],
    [("Dejar que decida solo el que habla más.", "Se cree que es más rápido.", "Haz turnos y escucha a todos."), ("Actuar sin acordar antes.", "Se quiere empezar rápido.", "Acuerden inicio, dificultad y cierre.")],
    [
        E("En una escena, ¿el inicio es cómo comienza o cómo termina?", "Cómo comienza", "Es el primer momento."),
        E("La dificultad es un problema que aparece. ¿Sí o no?", "Sí", "Mueve la escena."),
        E("¿Deciden todos o solo uno en una escena de equipo?", "Deciden todos", "Es un trabajo en equipo."),
    ],
    [
        E("¿Cuáles son las tres partes de una escena?", "Inicio, dificultad y cierre", "Estructuran lo que ocurre."),
        E("¿Por qué se hacen turnos para proponer?", "Para que todos opinen", "Nadie decide solo."),
        E("En Lenguaje: ¿Qué es un acuerdo?", "Una decisión del equipo entre todos", "Se llega escuchando."),
    ],
    [
        E("Inventa un inicio para una escena en la playa.", "Por ejemplo: Tres amigos llegan a la playa con un balde", "Presenta personajes y lugar."),
        E("Inventa una dificultad para esa escena en la playa.", "Por ejemplo: Una ola se lleva el balde", "Es un problema."),
        E("Inventa un cierre para esa escena en la playa.", "Por ejemplo: Entre todos recuperan el balde y arman un castillo", "Resuelve el problema."),
    ],
    [
        E("Un equipo propone: Inicio, tres niños arman un puesto de jugos. Dificultad, no hay vasos. Cierre, usan frascos limpios. ¿Tiene las tres partes?", "Sí", "Hay inicio, dificultad y cierre."),
        E("Ana propone, Luis acepta con «sí, y…» y Rita agrega otra idea. ¿Es trabajo en equipo?", "Sí", "Los tres aportan."),
    ],
    [
        E("Una escena empieza con «Cuatro amigos juegan» y termina con «Todos se van a casa». Falta una parte. ¿Cuál?", "La dificultad", "Falta el problema."),
        E("En un grupo, dos personas proponen cosas distintas. ¿Qué es mejor: a) elegir solo la de uno, b) unir o votar con respeto?", "b", "Así todos participan."),
    ],
    [E("Eres parte de un equipo de tres que representa una escena en un zoológico. Escribe el inicio, una dificultad y el cierre, y cómo repartirían los roles para que todos hablen.", "Inicio: visitan el zoológico; dificultad: se pierde un niño; cierre: lo encuentran con la guardaparque; roles: niño, guardaparque, familiar", "Tiene las tres partes y roles para todos.")],
    [
        E("¿Una escena necesita una dificultad?", "Sí", "Da movimiento a la historia."),
        E("Si el equipo escucha la idea de cada uno, ¿cada persona se siente valorada?", "Sí", "Ser escuchado ayuda a confiar en uno mismo."),
        E("¿Primero actúo y luego acordamos?", "No", "Primero se acuerda."),
    ],
    ("Crea en equipo. Con dos personas más (o con un adulto y un muñeco), preparen una escena de un minuto. Primero acuerden en voz alta: inicio, dificultad y cierre. Cada uno debe proponer algo antes de decidir. Luego represéntenla. Anota quién propuso qué.",
     "Inicio: tres amigos acampan en el patio. Dificultad: el viento tira la carpa. Cierre: la levantan entre todos y cantan. Yo propuse la dificultad, Ema el inicio y papá el cierre.",
     ["acuerdan inicio, dificultad y cierre", "todos proponen", "representan la escena"], ["escena ensayada", "nota de quién propuso qué"], ["decide uno solo", "faltan partes"],
     "Si decide uno solo, pidan turnos y que cada uno proponga una parte."),
    "Cuenta una escena corta con inicio, problema y final a alguien de tu casa.",
    "Reescribe el cierre de tu escena para que sea distinto, acordado por el equipo.",
)

# ================================================================ OA 30
reg(
    OA30, 1,
    "Este cuaderno, lápiz y una hoja. Un adulto que lea en voz alta y marque el ritmo con palmas.",
    "Aprenderé a reconocer el ritmo, las repeticiones y los sonidos de un poema antes de memorizarlo. Sirve para recitar mejor y con más gusto.",
    ["Sé repetir una rima corta.", "Sé escuchar con atención."],
    [
        "Un poema o una rima suena como una música hecha con palabras. Si lo escuchamos con atención, notamos el ritmo, es decir, los golpes de voz que se repiten. Podemos marcarlo con palmas. También notamos las pausas, que son pequeños silencios entre las frases.",
        "Mira este poema: «Gota a gota, gota a gota, / baila el agua en mi ventana; / salta, salta, cae y rota, / ya se asoma la mañana». Las palabras «gota» y «rota» riman, y también «ventana» y «mañana». Rimar es terminar con sonidos parecidos. Además, se repite «gota a gota».",
        "Antes de memorizar, escuchamos tres cosas: qué se repite, dónde hay pausas y qué palabras riman. Eso ayuda a recordar, porque la repetición y la rima funcionan como pistas. Después lo decimos con las palmas, despacio, y disfrutamos cómo suena.",
    ],
    [("ritmo", "golpes de voz que se repiten"), ("rima", "sonido parecido al final de las palabras"), ("repetición", "cuando algo se dice varias veces"), ("pausa", "pequeño silencio"), ("verso", "cada línea de un poema")],
    [
        ("Encontrar las rimas", "Poema: «Gota a gota, gota a gota, / baila el agua en mi ventana; / salta, salta, cae y rota, / ya se asoma la mañana». ¿Qué palabras riman?", ["Miro el final de cada verso.", "Comparo los sonidos.", "Las junto."], "Gota con rota, y ventana con mañana."),
        ("Encontrar la repetición", "En el mismo poema, ¿qué se repite al comienzo?", ["Leo el primer verso.", "Busco palabras iguales.", "Cuento cuántas veces."], "Se repite «gota a gota» dos veces."),
    ],
    [("Memorizar sin escuchar cómo suena.", "Se piensa que solo hay que aprender las palabras.", "Primero escucha el ritmo, las pausas y las rimas."), ("Decirlo muy rápido.", "Se quiere terminar pronto.", "Marca el ritmo con palmas despacio.")],
    [
        E("¿Rima «ventana» con «mañana» o con «gota»?", "Con mañana", "Terminan con sonido parecido."),
        E("En «Gota a gota, gota a gota», ¿qué palabra se repite?", "Gota", "Aparece varias veces."),
        E("¿Cuántos versos tiene el poema de la lluvia: 4 o 6?", "4", "Hay cuatro líneas."),
    ],
    [
        E("En Lenguaje: ¿Qué es el ritmo?", "Los golpes de voz que se repiten", "Dan música a las palabras."),
        E("¿Para qué sirven las pausas?", "Para respirar y marcar las frases", "Ordenan el poema."),
        E("¿Por qué ayuda la rima a recordar?", "Porque funciona como una pista de sonido", "Se recuerda el eco."),
    ],
    [
        E("Rima: «sol - ______». Elige entre «luz» y «farol».", "farol", "Termina con -ol."),
        E("Rima: «luna - ______». Elige entre «cuna» y «mesa».", "cuna", "Termina con -una."),
        E("Escribe dos palabras que rimen con «casa».", "Por ejemplo: masa y taza", "Terminan con sonido parecido (-asa)."),
    ],
    [
        E("Verso 1 «Pasa el viento por mi puerta», verso 2 «y despierta toda la huerta». ¿Qué palabras riman?", "Puerta y huerta", "Ambas terminan en -uerta."),
        E("Dani dice que «gota» rima con «ventana». ¿Tiene razón?", "No", "Los sonidos finales son distintos."),
    ],
    [
        E("Poema: «Un patito, dos patitos, / tres patitos al pasar; / nadan juntos y chiquitos / por el agua del lugar». ¿Qué palabras riman?", "Patitos con chiquitos, y pasar con lugar", "Hay dos pares de rimas."),
        E("En los dos primeros versos de ese poema, ¿cuántas veces aparece la palabra «patitos»?", "2", "Aparece en «dos patitos» y «tres patitos»."),
    ],
    [E("Poema: «Gota a gota, gota a gota, / baila el agua en mi ventana; / salta, salta, cae y rota, / ya se asoma la mañana». Di el poema con palmas en cada «gota» y señala dónde harías una pausa.", "Palmas en gota; pausas al final de cada verso", "Marca ritmo y pausas.")],
    [
        E("¿Rimar es terminar con sonidos parecidos?", "Sí", "Así se define la rima."),
        E("¿La repetición ayuda a memorizar?", "Sí", "Es una pista."),
        E("¿Debo escuchar antes de memorizar?", "Sí", "Así entiendo el ritmo."),
    ],
    ("Escucha y marca el ritmo. Con un adulto, di el poema de la lluvia tres veces. 1) La primera, solo escucha. 2) La segunda, marca con palmas la palabra «gota». 3) La tercera, di el poema con una pausa al final de cada verso. Luego anota dos rimas y una repetición que encontraste.",
     "Rimas: gota y rota; ventana y mañana. Repetición: gota a gota. Marqué el ritmo con palmas y paré al final de cada verso.",
     ["marca el ritmo con palmas", "encuentra dos rimas y una repetición", "usa pausas"], ["práctica con un adulto", "nota escrita"], ["decirlo muy rápido", "no encontrar las rimas"],
     "Si va rápido, repite con palmas lentas y cuenta hasta dos en cada pausa."),
    "Escucha una canción de cuna de tu casa y cuenta cuántas veces se repite una palabra.",
    "Inventa dos versos que rimen sobre el viento.",
)

reg(
    OA30, 2,
    "Este cuaderno, lápiz y una hoja. Un adulto para escuchar.",
    "Aprenderé a pronunciar un trabalenguas con claridad, empezando despacio. Sirve para mejorar mi pronunciación y disfrutar los juegos de palabras.",
    ["Sé reconocer ritmo y rimas.", "Sé hablar con voz clara."],
    [
        "Un trabalenguas es un juego de palabras difíciles de decir rápido, porque tienen sonidos parecidos. Por ejemplo: «Pablito pinta pelotas pequeñas para papá». Se repite mucho el sonido p. Por eso es difícil y por eso es divertido.",
        "La articulación es mover bien la boca, la lengua y los labios para decir cada sonido. Si hablo muy rápido, las palabras se enredan. La clave es empezar despacio, decir cada palabra con claridad y subir la velocidad un poco, solo si no me equivoco.",
        "Equivocarse en un trabalenguas es normal y es parte del juego. Si me trabo, respiro, vuelvo a empezar despacio y sigo. La confianza no es no cometer errores: es volver a intentarlo con calma. Puedo practicar solo, en pareja o con quien quiera.",
    ],
    [("trabalenguas", "juego de palabras difíciles de pronunciar"), ("articulación", "mover bien labios y lengua para decir los sonidos"), ("claridad", "que se entiende cada palabra"), ("velocidad", "qué tan rápido hablo"), ("intentar", "probar otra vez")],
    [
        ("Decirlo despacio", "Trabalenguas: «Pablito pinta pelotas pequeñas para papá». ¿Cómo lo practicas?", ["Lo digo palabra por palabra.", "Digo bien la p.", "Subo la velocidad poco a poco."], "Lo digo despacio, marcando cada p, y luego un poco más rápido."),
        ("Volver a empezar", "Te trabaste a mitad del trabalenguas. ¿Qué haces?", ["Respiro.", "No me enojo.", "Empiezo de nuevo despacio."], "Respiro y empiezo de nuevo despacio."),
    ],
    [("Decirlo lo más rápido posible.", "Se cree que lo importante es la velocidad.", "Primero claridad y después velocidad."), ("Enojarse al equivocarse.", "Se cree que errar es fracasar.", "Respira y vuelve a empezar.")],
    [
        E("Para decir un trabalenguas, ¿empiezo despacio o muy rápido?", "Despacio", "Así se pronuncia bien."),
        E("Si me equivoco, ¿vuelvo a empezar o dejo de jugar?", "Vuelvo a empezar", "Seguir intentando da confianza."),
        E("En «Pablito pinta pelotas pequeñas para papá», ¿qué sonido se repite: p o m?", "p", "Muchas palabras empiezan con p."),
    ],
    [
        E("¿Qué es la articulación?", "Mover bien labios y lengua al hablar", "Ayuda a decir cada sonido."),
        E("¿Por qué no debo ir demasiado rápido?", "Porque se enredan las palabras", "Se pierde la claridad."),
        E("¿Equivocarse en un trabalenguas es malo?", "No, es parte del juego", "Se aprende intentando."),
    ],
    [
        E("Cuenta cuántas palabras del trabalenguas «Pablito pinta pelotas pequeñas para papá» empiezan con p.", "6", "Pablito, pinta, pelotas, pequeñas, para y papá empiezan con p."),
        E("Trabalenguas: «Rosa rompe ricas rosquillas rojas». ¿Qué sonido se repite al comienzo?", "r", "Todas las palabras empiezan con r."),
        E("Escribe en qué orden practicarías: a) decirlo rápido, b) decirlo despacio, c) repetirlo con calma.", "b, c, a", "Primero claridad, luego velocidad."),
    ],
    [
        E("Ema dice el trabalenguas muy rápido y nadie la entiende. Luis lo dice a velocidad media y claro. ¿Quién lo hizo mejor?", "Luis", "Se entiende cada palabra."),
        E("Tito se equivocó dos veces y siguió intentando. ¿Mostró confianza?", "Sí", "Persistió con calma."),
    ],
    [
        E("Trabalenguas: «Rosa rompe ricas rosquillas rojas». ¿Cuántas palabras tiene?", "5", "Son Rosa, rompe, ricas, rosquillas y rojas."),
        E("Elige la mejor estrategia si una palabra te cuesta: a) saltarla, b) repetirla despacio varias veces y luego dentro del trabalenguas.", "b", "Practicar la parte difícil ayuda."),
    ],
    [E("Tienes que practicar este trabalenguas: «Pablito pinta pelotas pequeñas para papá». Escribe los tres pasos que seguirás para decirlo bien.", "Despacio, palabra por palabra; con claridad en la p; subir un poco la velocidad", "Describe una práctica ordenada.")],
    [
        E("¿Puedo practicar un trabalenguas con un compañero?", "Sí", "Se puede jugar en pareja."),
        E("¿Es mejor claridad que velocidad?", "Sí", "Se entiende más."),
        E("¿Una equivocación significa que no sirvo?", "No", "Aprendemos al intentar de nuevo."),
    ],
    ("Practica un trabalenguas sin correr. Di tres veces: «Pablito pinta pelotas pequeñas para papá». 1) La primera, muy despacio, marcando cada p. 2) La segunda, a velocidad normal. 3) La tercera, un poco más rápido, pero sin equivocarte. Si te trabas, respira y empieza de nuevo. Luego cuéntale a un adulto cuál fue más clara.",
     "La primera la dije despacio y se entendió todo. La segunda, normal, también. En la tercera me trabé, pero respiré y empecé de nuevo. La más clara fue la segunda.",
     ["empieza despacio", "mantiene la claridad", "vuelve a intentar con calma si se equivoca"], ["práctica ante un adulto", "comentario sobre la versión más clara"], ["ir demasiado rápido", "rendirse"],
     "Si se enoja, recuerda que equivocarse es parte del juego y repite despacio."),
    "Enseña un trabalenguas a alguien de tu casa.",
    "Inventa un trabalenguas de siete palabras con el sonido t.",
)

reg(
    OA30, 3,
    "Este cuaderno, lápiz y una hoja. Un adulto para escuchar.",
    "Aprenderé a cambiar la voz y el gesto según lo que dice el poema o la adivinanza. Sirve para que quien escucha entienda y sienta lo que quiero comunicar.",
    ["Sé recitar con claridad.", "Sé que la voz muestra emociones."],
    [
        "La entonación es cómo sube y baja la voz al decir algo. Una pregunta de sí o no, como «¿Vienes?», sube la voz al final; una exclamación suena más fuerte y marcada. También usamos la expresión, que es lo que muestran la cara y el cuerpo. Con ambas, el poema cobra vida y quien escucha entiende lo que sentimos.",
        "Veamos una adivinanza: «Tengo alas y no soy pájaro, / vuelo bajito en la tarde, / cargo polen en mis patas / y hago miel muy dulce. ¿Qué soy?». Digo los primeros versos con misterio, voz suave. Al final subo la voz para la pregunta. La respuesta es la abeja.",
        "Para decidir cómo decir un texto, pregunto: ¿qué dice?, ¿cómo se siente?, ¿qué voz y qué gesto le quedan? Un verso alegre va con voz alegre y sonrisa. Uno de misterio, con voz baja y mirada atenta. Los gestos deben ser suaves y sin exagerar.",
    ],
    [("entonación", "subida y bajada de la voz al hablar"), ("expresión", "lo que muestran la cara y el cuerpo"), ("adivinanza", "texto que pide descubrir una respuesta"), ("misterio", "algo que despierta curiosidad"), ("exclamación", "frase que muestra una emoción fuerte")],
    [
        ("Elegir la voz", "Verso: «¡Qué alegría, llegó mi abuela!». ¿Qué voz y qué gesto eliges?", ["Leo el verso.", "Siento alegría.", "Elijo voz alegre."], "Voz alegre y fuerte, con sonrisa."),
        ("Entonar una pregunta", "En la adivinanza, el último verso es «¿Qué soy?». ¿Cómo lo dices?", ["Es pregunta.", "Subo un poco la voz al final.", "Miro al público."], "Subo un poco la voz al final, para invitar al público a responder."),
    ],
    [("Decir todo con la misma voz.", "No se piensa en el sentido.", "Cambia la voz según lo que dice."), ("Exagerar los gestos.", "Se cree que más gesto es mejor.", "Usa gestos suaves que combinen con el texto.")],
    [
        E("En «¿Vienes?», una pregunta de sí o no, ¿la voz sube o baja al final?", "Sube", "Así se reconoce esa pregunta."),
        E("Un verso de misterio, ¿va con voz baja o con voz de grito?", "Voz baja", "Eso da suspenso."),
        E("«¡Qué alegría!», ¿se dice con voz triste o alegre?", "Alegre", "Combina con el sentido."),
    ],
    [
        E("¿Qué es la entonación?", "Cómo sube y baja la voz", "Muestra el sentido."),
        E("¿Por qué cambio la voz según el texto?", "Para que se entienda lo que siento", "La voz transmite emociones."),
        E("¿Qué debo cuidar con los gestos?", "Que sean suaves y combinen con el texto", "No deben exagerar."),
    ],
    [
        E("Adivinanza: «Tengo alas y no soy pájaro, vuelo bajito en la tarde, cargo polen en mis patas y hago miel muy dulce». ¿Cuál es la respuesta?", "La abeja", "La miel y el polen lo indican."),
        E("Verso: «Silencio, que el bosque duerme». ¿Qué voz usas?", "Voz baja y suave", "Combina con el sueño."),
        E("Verso: «¡Ganamos el partido!». ¿Qué gesto usas?", "Brazos arriba y sonrisa", "Eso muestra una celebración."),
    ],
    [
        E("Tati dice «Estoy muy triste» con voz saltarina y sonrisa. ¿Combina con el verso?", "No", "La voz no coincide con lo que dice."),
        E("Lalo dice la adivinanza con voz de misterio. Al preguntar «¿Qué soy?», sube la voz. ¿Entonó bien?", "Sí", "Combina con el sentido."),
    ],
    [
        E("Verso A: «¡Corre, corre, que ya llega!». Verso B: «Dormir, dormir, que ya es de noche». ¿Cuál se dice con ritmo rápido y cuál con ritmo lento?", "A rápido, B lento", "Cada ritmo combina con el sentido."),
        E("Escoge cómo decir «La luna se esconde tras la nube» para dar misterio: a) con gritos, b) con voz suave y pausa.", "b", "La pausa y la voz suave dan misterio."),
    ],
    [E("Adivinanza: «Tengo hojas y no soy libro, tengo tronco y no soy gato; vivo quieto en el jardín y doy sombra en verano». Escribe cómo la dirías: qué voz, qué pausa y qué gesto, y cuál es la respuesta.", "Voz suave y juguetona, una pausa antes de la pregunta, gesto de abrir los brazos; respuesta: el árbol", "Une voz, pausa, gesto y respuesta.")],
    [
        E("¿Puedo cambiar de voz para un verso triste?", "Sí", "La voz muestra emociones."),
        E("¿Los gestos deben ser muy grandes?", "No", "Deben ser suaves."),
        E("¿Una pregunta suena igual que una exclamación?", "No", "Cambia la entonación."),
    ],
    ("Entona para comunicar. Con un adulto, di estos tres versos con distinta voz y gesto: 1) «¡Qué alegría, llegó mi abuela!», 2) «Silencio, que el bosque duerme», 3) «¿Quién se comió mi manzana?». Luego pide al adulto que adivine qué sentías en cada uno. Si acierta, tu voz y gesto fueron claros.",
     "1) Voz alegre y fuerte, sonrisa y brazos abiertos. 2) Voz baja, dedo en los labios. 3) Voz que sube un poco al final, cejas arriba. Mi mamá adivinó los tres.",
     ["cambia la voz según el verso", "usa gestos suaves", "el adulto reconoce las emociones"], ["práctica con un adulto"], ["decir todo igual", "exagerar los gestos"],
     "Si todo suena igual, pregunta cómo se siente el verso y cómo lo diría una persona en esa situación."),
    "Dile «buenos días» de tres formas distintas a alguien de tu casa.",
    "Elige un poema que conozcas y márcalo con voces distintas para cada verso.",
)

reg(
    OA30, 4,
    "Este cuaderno, lápiz y una hoja. Un adulto o más personas como audiencia.",
    "Aprenderé a recitar para una audiencia, solo, en pareja o en coro, y a evaluar mi claridad. Sirve para ganar confianza y disfrutar compartiendo un texto.",
    ["Sé escuchar el ritmo.", "Sé articular y entonar."],
    [
        "Recitar para una audiencia es decir un poema, una rima, una canción, un trabalenguas o una adivinanza ante otras personas. Podemos hacerlo de tres formas: solos, en pareja (cada uno dice un verso) o en coro (todos juntos). Cada uno elige la forma con la que se sienta mejor.",
        "Antes de recitar respiro, miro a la audiencia y empiezo con calma. Mientras recito, cuido el volumen, la claridad, la entonación y los gestos. Si me equivoco, respiro y sigo: no pasa nada. La confianza no se mide por no tener errores, sino por seguir con ganas.",
        "Después de recitar, evaluamos con criterios simples: ¿se oyó?, ¿se entendió?, ¿se notó el ritmo y la emoción? Podemos hacernos una pregunta: ¿qué hice bien y qué mejoraré? Si alguien prefiere no recitar solo, puede hacerlo en pareja o coro. Todas las formas valen.",
    ],
    [("audiencia", "personas que escuchan"), ("coro", "varias personas que recitan juntas"), ("pareja", "dos personas que recitan por turnos"), ("confianza", "seguridad en lo que puedo hacer"), ("criterio", "regla para evaluar algo")],
    [
        ("Elegir cómo recitar", "Te da nervios recitar solo. ¿Qué opciones tienes?", ["Pienso en mis opciones.", "Puedo hacerlo en pareja.", "O en coro."], "En pareja, diciendo un verso cada uno, o en coro, todos juntos."),
        ("Evaluar con criterios", "Recitaste el poema de la lluvia. ¿Qué criterios usas para evaluarte?", ["Pienso en el volumen.", "Pienso en la claridad.", "Pienso en el ritmo."], "Se oyó, se entendió y se notó el ritmo."),
    ],
    [("Creer que la confianza es no equivocarse.", "Se piensa que el que se equivoca no tiene confianza.", "La confianza es seguir con ganas."), ("Obligar a todos a recitar solos.", "Se piensa que solo hay una forma.", "Ofrece pareja o coro.")],
    [
        E("Si no quiero recitar solo, ¿puedo hacerlo en pareja o en coro?", "Sí", "Todas las formas valen."),
        E("Si me equivoco al recitar, ¿respiro y sigo o me voy corriendo?", "Respiro y sigo", "Seguir muestra confianza."),
        E("¿Un coro recita con una persona o con varias?", "Con varias", "Todas hablan juntas."),
    ],
    [
        E("¿Qué son los criterios de evaluación?", "Reglas simples para revisar cómo salió algo", "Ayudan a mejorar."),
        E("¿Por qué la confianza no es no equivocarse?", "Porque es seguir intentando con ganas", "Los errores son parte del aprendizaje."),
        E("¿Qué hago antes de recitar?", "Respiro y miro a la audiencia", "Empiezo con calma."),
    ],
    [
        E("Poema: «Gota a gota, gota a gota, / baila el agua en mi ventana». Dos niños lo recitan: uno dice el primer verso y el otro el segundo. ¿Qué forma de recitar usaron?", "En pareja", "Cada uno dice un verso."),
        E("Escribe tres criterios para evaluar una recitación.", "Se oyó, se entendió, se notó el ritmo o la emoción", "Son criterios observables."),
        E("Escribe una frase para decirte después de recitar: una cosa que hiciste bien.", "Por ejemplo: Hablé claro y miré a la audiencia", "Reconoce un logro."),
    ],
    [
        E("Rosa recitó sin equivocarse pero muy bajito. Pedro se trabó una vez, siguió y se oyó fuerte. ¿Quién cumplió mejor el criterio «se oyó»?", "Pedro", "Se oyó fuerte, aunque se trabó una vez."),
        E("Mateo no quiere recitar solo. Ana le propone hacerlo juntos. ¿Es una buena idea?", "Sí", "En pareja se siente más seguro."),
    ],
    [
        E("Adivinanza: «Soy redonda, estoy en el cielo, de noche te alumbro y de día me escondo». Un niño la dice mirando a su público y subiendo la voz al preguntar. ¿Entonó bien la pregunta?", "Sí", "Al subir la voz marca la pregunta."),
        E("Dos criterios: a) «Se oyó» y b) «Era largo». ¿Cuál es mejor para evaluar la recitación?", "a", "Se refiere a cómo se dijo."),
    ],
    [E("Tu curso recitará el poema de la lluvia. Una compañera tiene mucha vergüenza. Escribe dos formas de ayudarla a participar sin obligarla a recitar sola.", "Hacerlo en pareja y en coro", "Ofrece alternativas respetuosas.")],
    [
        E("¿Puedo elegir cómo recitar?", "Sí", "Solo, pareja o coro."),
        E("¿Evaluar es decir lo que hice bien y lo que mejoraré?", "Sí", "Ayuda a crecer."),
        E("¿Equivocarse es un fracaso?", "No", "Es parte de aprender."),
    ],
    ("Recita para una audiencia. Elige el poema de la lluvia, el trabalenguas de Pablito o una canción o ronda que conozcas. Recítalo ante dos o tres personas de tu casa: solo, en pareja o en coro, como prefieras. Respira, mira al público, cuida volumen, claridad y ritmo. Después pide que digan: ¿se oyó?, ¿se entendió?, ¿se notó el ritmo? Anota una cosa que hiciste bien y una que mejorarás.",
     "Recité en pareja con mi hermana. Se oyó y se entendió. Hice bien el ritmo con las palmas. Mejoraré la mirada, porque miré el piso.",
     ["recita con la forma elegida", "cuida volumen, claridad y ritmo", "evalúa una cosa que hizo bien y una que mejorará"], ["recitación ante audiencia", "evaluación con tres criterios"], ["obligar a recitar solo", "pensar que errores son fracasos"],
     "Si tiene mucha vergüenza, ofrece pareja o coro y ensayen juntos."),
    "Recita para una persona de tu casa una rima corta que te guste.",
    "Prepara un coro de tres personas y reparte versos distintos a cada una.",
)

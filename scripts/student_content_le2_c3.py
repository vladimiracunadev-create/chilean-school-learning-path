"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 20 (género, número y concordancia) y OA 21 (ortografía y puntuación)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA20, OA21 = "LE02 OA 20", "LE02 OA 21"
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


# ================================================================ OA 20 · clase 1
reg(
    OA20, 1,
    "Las palabras de este cuaderno, lápiz y hoja. Tarjetas de papel si quieres armar plurales.",
    "Aprenderé a distinguir singular y plural y a formar el plural de las palabras. Sirve para decir y escribir cuántas cosas hay.",
    ["Sé reconocer sustantivos.", "Sé contar hasta 20."],
    [
        "El número de una palabra dice si hablamos de uno o de más de uno. Si es uno, está en singular: «una casa». Si es más de uno, está en plural: «dos casas». El plural se marca con las terminaciones -s o -es.",
        "Hay tres reglas fáciles. Si la palabra termina en vocal, agregas -s: casa, casas. Si termina en consonante, agregas -es: flor, flores; papel, papeles. Si termina en z, cambias la z por c y agregas -es: lápiz, lápices; pez, peces.",
        "Cuando una palabra cambia a plural, las palabras que la acompañan también cambian: «el pez veloz» pasa a «los peces veloces». Por eso es bueno revisar todo el grupo de palabras.",
    ],
    [("singular", "una sola persona, animal o cosa"), ("plural", "más de una persona, animal o cosa"), ("terminación", "letras con que termina una palabra"), ("vocal", "a, e, i, o, u"), ("consonante", "letra que no es vocal")],
    [
        ("Plural de una palabra con vocal final", "Escribe el plural de «casa».", ["«Casa» termina en la vocal a.", "Agrego -s."], "Casas."),
        ("Plural de una palabra con z final", "Escribe el plural de «lápiz».", ["«Lápiz» termina en z.", "Cambio la z por c.", "Agrego -es."], "Lápices."),
    ],
    [("Poner -s a una palabra que termina en consonante: «flors».", "Se usa la misma regla para todo.", "Si termina en consonante, agrega -es: flores."), ("Dejar la z en el plural: «lápizes».", "No se cambia la letra.", "Cambia z por c: lápices.")],
    [
        E("¿Cuál es el plural de «casa»?", "casas", "Termina en vocal, así que se agrega -s."),
        E("¿«Gatos» está en singular o en plural?", "Plural", "Habla de más de uno."),
        E("¿Cuál es el plural de «flor»?", "flores", "Termina en consonante; se agrega -es."),
    ],
    [
        E("Una palabra termina en vocal. ¿Agrego -s o -es?", "-s", "Después de vocal se agrega -s."),
        E("¿Qué cambia en «lápiz» cuando pasa a plural?", "La z cambia por c y se agrega -es", "El plural es lápices."),
        E("«Una mesa» nombra ¿uno o más de uno?", "Uno", "El artículo «una» y el singular indican uno."),
    ],
    [
        E("Escribe el plural de «papel».", "papeles", "Termina en consonante; se agrega -es."),
        E("Escribe el plural de «pez».", "peces", "La z cambia por c y se agrega -es."),
        E("Escribe el singular de «luces».", "luz", "El plural de luz es luces."),
    ],
    [
        E("Tomás escribió «flors». ¿Cuál es el error?", "Flor termina en consonante y el plural lleva -es: flores", "La regla correcta es agregar -es."),
        E("Mara dice que el plural de «lápiz» es «lápizes». Corrige y explica.", "Lápices, porque la z cambia por c", "Antes de e se escribe c y no z."),
    ],
    [
        E("Escribe en plural «el pez veloz».", "los peces veloces", "Cambian el artículo, el sustantivo y el adjetivo."),
        arith("Tienes 1 lápiz y te regalan 4 lápices más. ¿Cuántos lápices tienes?", "1+4", "Se suman los que tienes y los regalados."),
    ],
    [E("En un cartel dice: «Hay un papel y dos ___ en la mesa». Completa con el plural de «papel».", "papeles", "Termina en l y el plural lleva -es.")],
    [
        E("¿Qué letra cambio cuando una palabra termina en z?", "La z se cambia por c", "Así se escribe el plural."),
        E("¿«Peces» es singular o plural?", "Plural", "Habla de más de un pez."),
        E("¿Cuántas terminaciones de plural aprendiste hoy: -s y -es?", "Dos", "Son -s y -es."),
    ],
    ("Escribe el plural de estas ocho palabras y di la regla que usaste en cada una: mesa, flor, lápiz, perro, papel, luz, niña, reloj. Pista: «reloj» termina en consonante y su plural es «relojes».",
     "mesas (vocal, -s), flores (consonante, -es), lápices (z→c, -es), perros (vocal, -s), papeles (consonante, -es), luces (z→c, -es), niñas (vocal, -s), relojes (consonante, -es).",
     ["forma bien los ocho plurales", "usa la regla correcta", "cambia z por c cuando corresponde"], ["lista con el plural y la regla de cada palabra"], ["escribir «lápizes»", "poner -s a palabras terminadas en consonante"],
     "Si falla un plural, pregunta: «¿Con qué letra termina la palabra?»."),
    "Busca en tu cuarto cinco cosas en singular y di su plural en voz alta.",
    "Escribe cinco plurales de palabras que terminen en z.",
)

# ================================================================ OA 20 · clase 2
reg(
    OA20, 2,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé que las palabras de un grupo deben coincidir en género y número. Sirve para escribir sin errores de concordancia.",
    ["Sé reconocer artículos, sustantivos y adjetivos.", "Sé formar el plural."],
    [
        "El género dice si una palabra es masculina o femenina: «el niño» es masculino y «la niña» es femenino. El número dice si es singular o plural. Cuando las palabras de un grupo tienen el mismo género y número, decimos que concuerdan.",
        "Mira estos grupos: «el niño alto», «la niña alta», «los niños altos» y «las niñas altas». El artículo, el sustantivo y el adjetivo cambian juntos. No se dice «la niña alto» ni «los niño altos».",
        "Algunos adjetivos no cambian de género, como «grande» o «veloz»: «el perro grande» y «la perra grande». Pero sí cambian de número: «los perros grandes». Para revisar, lee el grupo completo y comprueba que todas las palabras digan lo mismo.",
    ],
    [("género", "ser masculino o femenino"), ("masculino", "como «el niño»"), ("femenino", "como «la niña»"), ("concordar", "coincidir en género y número"), ("grupo nominal", "artículo, sustantivo y adjetivo juntos")],
    [
        ("Hacer concordar un adjetivo", "Completa: «la casa ___» (blanco o blanca).", ["«Casa» es femenino y singular.", "El adjetivo debe ser femenino y singular."], "La casa blanca."),
        ("Hacer concordar en plural", "Completa: «los gatos ___» (negro o negros).", ["«Gatos» es masculino y plural.", "El adjetivo debe ser plural."], "Los gatos negros."),
    ],
    [("Escribir «la niña alto».", "El adjetivo no se cambia al femenino.", "Cambia el adjetivo: la niña alta."), ("Poner solo el sustantivo en plural: «los niño».", "Se olvida revisar el artículo y el adjetivo.", "Pon todas las palabras en plural: los niños.")],
    [
        E("Completa: «la casa ___». Opciones: blanco o blanca.", "blanca", "Casa es femenino."),
        E("Completa: «los gatos ___». Opciones: negro o negros.", "negros", "Gatos es plural."),
        E("¿Cuántas palabras de «las niñas altas» están en plural?", "3", "Las, niñas y altas están en plural."),
    ],
    [
        E("¿Qué significa concordar?", "Coincidir en género y número", "Las palabras dicen lo mismo."),
        E("¿Cuál concuerda: «el casa blanca» o «la casa blanca»?", "la casa blanca", "Casa es femenino y singular."),
        E("¿Cambia «grande» de masculino a femenino en «el perro grande» y «la perra grande»?", "No", "Grande se escribe igual para los dos."),
    ],
    [
        E("Completa: «las flores ___». Opciones: rojo, roja o rojas.", "rojas", "Flores es femenino plural."),
        E("Completa: «un perro ___». Opciones: pequeño o pequeña.", "pequeño", "Perro es masculino singular."),
        E("Corrige: «el gata negro».", "la gata negra", "Gata es femenino."),
    ],
    [
        E("Explica por qué «los niño» está mal.", "Porque «los» es plural y «niño» está en singular", "El plural debe estar en todas las palabras."),
        E("Pedro escribió «la mesa nuevo». ¿Qué ocurrió?", "Mesa es femenino y nuevo es masculino; es «la mesa nueva»", "El adjetivo no concuerda en género."),
    ],
    [
        E("Escribe en plural «el zapato negro».", "los zapatos negros", "Cambian artículo, sustantivo y adjetivo."),
        arith("Una oración tiene 4 grupos nominales y 3 concuerdan. ¿Cuántos tienen error?", "4-3", "Se resta los correctos del total."),
    ],
    [E("En un aviso dice: «Se vende unas bicicleta rojo». Corrígelo sin cambiar el verbo «vende».", "Se vende una bicicleta roja.", "Concuerdan una, bicicleta y roja.")],
    [
        E("¿Qué hago para revisar la concordancia?", "Leo todo el grupo de palabras", "Veo si todas dicen lo mismo."),
        E("¿«Niñas» es masculino o femenino?", "Femenino", "Termina en -a y habla de niñas."),
        E("¿Un artículo masculino puede acompañar a un sustantivo femenino?", "No", "Deben coincidir en género y número."),
    ],
    ("Corrige la concordancia de estos cinco grupos y escribe cada uno bien (hay más de una forma correcta si todas las palabras concuerdan). 1) las niño altos. 2) un casa grandes. 3) los flores rojo. 4) la perro negra. 5) unas gatos pequeña.",
     "1) los niños altos (o las niñas altas). 2) una casa grande (o unas casas grandes). 3) las flores rojas. 4) el perro negro (o la perra negra). 5) unos gatos pequeños (o unas gatas pequeñas). Hay más de una forma correcta si todas las palabras concuerdan.",
     ["corrige artículo, sustantivo y adjetivo", "usa el mismo género y número", "escribe los cinco grupos"], ["hoja con cinco grupos corregidos"], ["corregir solo una palabra", "mezclar singular y plural"],
     "Pide que lea cada grupo y diga si suena bien; luego que señale cuál palabra no coincide."),
    "Di en voz alta tres grupos nominales que concuerden con objetos de tu casa.",
    "Escribe un grupo nominal en las cuatro formas: masculino y femenino, singular y plural.",
)

# ================================================================ OA 20 · clase 3
reg(
    OA20, 3,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé a usar el género correcto con las personas y a escribir sin estereotipos. Sirve para tratar a todas las personas con respeto.",
    ["Sé que hay palabras masculinas y femeninas.", "Sé hacer concordar el artículo con el sustantivo."],
    [
        "Cuando hablamos de personas, el género de las palabras depende de quién es la persona. Si es hombre, decimos «el profesor» o «el cocinero». Si es mujer, decimos «la profesora» o «la cocinera». Algunas palabras no cambian, como «artista» o «deportista»: solo cambia el artículo, como en «el artista» y «la artista».",
        "Un estereotipo es una idea fija sobre cómo deben ser las personas. Por ejemplo, creer que «solo las mujeres cocinan» o «solo los hombres son bomberos». Eso no es verdad. Cualquier persona puede tener cualquier trabajo o jugar cualquier juego.",
        "Al escribir, usamos el género que corresponde a la persona de la que hablamos, sin imponer ideas sobre lo que puede hacer. Así tratamos a todos con respeto.",
    ],
    [("estereotipo", "idea fija sobre cómo deben ser las personas"), ("respeto", "tratar bien a los demás"), ("profesora", "mujer que enseña"), ("deportista", "persona que practica un deporte"), ("oficio", "trabajo de una persona")],
    [
        ("Elegir el género según la persona", "Una mujer enseña a los niños de la escuela. ¿Cómo la llamamos: el profesor o la profesora?", ["Veo que es una mujer.", "El artículo y el sustantivo deben ser femeninos."], "La profesora."),
        ("Escribir sin estereotipos", "Reescribe sin estereotipos: «Las mamás cocinan y los papás trabajan».", ["Pienso: ¿solo ellas cocinan y solo ellos trabajan? No es así.", "Escribo una oración que incluya a todos."], "Las mamás y los papás cocinan y trabajan."),
    ],
    [("Pensar que un trabajo es solo de hombres o solo de mujeres.", "Se repiten ideas antiguas.", "Recuerda que cualquier persona puede hacer cualquier trabajo."), ("Usar el género del trabajo y no el de la persona.", "Se mira el oficio y no a la persona.", "Usa el género de la persona de quien hablas.")],
    [
        E("Una mujer enseña a los niños. ¿Cómo se dice: el profesor o la profesora?", "la profesora", "Es una mujer."),
        E("Un hombre cocina en un restaurante. ¿Cómo se dice: el cocinero o la cocinera?", "el cocinero", "Es un hombre."),
        E("Una mujer que cura a los enfermos, ¿es el médico o la médica?", "la médica", "Se usa el femenino."),
    ],
    [
        E("¿Pueden las mujeres ser bomberas y los hombres cocineros?", "Sí", "Cualquier persona puede tener cualquier oficio."),
        E("¿Qué decide si uso «el» o «la» con una persona?", "Si la persona es hombre o mujer", "El género sigue a la persona."),
        E("En «el deportista» y «la deportista», ¿cambia la palabra deportista?", "No, solo cambia el artículo", "Deportista sirve para ambos."),
    ],
    [
        E("Completa: «___ doctora atendió al niño». Opciones: El o La.", "La", "Doctora es femenino."),
        E("Mi papá trabaja en una cocina. Completa: «Mi papá es ___». Opciones: cocinero o cocinera.", "cocinero", "Mi papá es hombre."),
        E("Completa: «___ artista pintó un mural». La artista es una mujer. Opciones: El o La.", "La", "Artista es mujer."),
    ],
    [
        E("Un texto dice: «Los niños juegan fútbol y las niñas cocinan». ¿Por qué es un estereotipo?", "Porque supone que solo algunos pueden jugar y otras cocinar", "Todos pueden hacer ambas cosas."),
        E("Pedro dice que solo los hombres pueden ser bomberos. ¿Es correcto?", "No, porque también hay mujeres bomberas", "Cualquier persona puede serlo."),
    ],
    [
        E("Reescribe sin estereotipo: «Las niñas juegan con muñecas y los niños con autos». Escribe una versión posible.", "Ejemplo: Las niñas y los niños juegan con muñecas y autos.", "Se incluye a todos."),
        E("Escribe en femenino: «el profesor simpático».", "la profesora simpática", "Cambian artículo, sustantivo y adjetivo."),
    ],
    [E("Tu profesora anuncia: «Mañana vendrá un bombero a hablar con nosotros». Llega una mujer. ¿Cómo dices que llegó?", "Llegó la bombera", "Se usa el femenino para una mujer.")],
    [
        E("¿Un estereotipo es una idea que siempre es verdad?", "No", "Es una idea fija que no es cierta."),
        E("Si hablo de una niña, ¿uso «el» o «la»?", "La", "Niña es femenino."),
        E("¿Puedo decir «el artista» para un hombre y «la artista» para una mujer?", "Sí", "Artista no cambia de forma."),
    ],
    ("Completa y reescribe estas oraciones con el género correcto y sin estereotipos. 1) Rosa, que trabaja en una cocina, es ___ (cocinero o cocinera). 2) Mi hermano, que cura enfermos, es ___ (médico o médica). 3) Reescribe: «Los hombres arreglan autos y las mujeres cuidan niños».",
     "1) cocinera. 2) médico. 3) Los hombres y las mujeres arreglan autos y cuidan niños.",
     ["usa el género correcto", "no repite estereotipos", "reescribe la tercera oración incluyendo a todos"], ["tres respuestas escritas"], ["decir «cocinero» para Rosa", "mantener el estereotipo"],
     "Pregunta: «¿Quién puede hacer ese trabajo?». Recuerda que todos pueden."),
    "Escribe dos oraciones sobre personas de tu familia con su oficio y el género correcto.",
    "Haz una lista de diez oficios con su forma masculina y femenina, cuando cambian.",
)

# ================================================================ OA 20 · clase 4
reg(
    OA20, 4,
    "Los textos con errores de este cuaderno, un lápiz de color y hoja.",
    "Aprenderé a encontrar y corregir errores de concordancia en un texto. Sirve para mejorar mis escritos antes de publicarlos.",
    ["Sé formar el plural.", "Sé hacer concordar género y número."],
    [
        "Editar la concordancia es leer un texto y corregir las palabras que no coinciden. Para hacerlo, lee cada oración. Busca el sustantivo y mira el artículo y el adjetivo que lo acompañan.",
        "Sigue estos pasos. Uno: encuentra el sustantivo. Dos: revisa si el artículo y el adjetivo tienen su mismo género y número. Tres: corrige lo que no coincida. Cuatro: relee la oración corregida.",
        "Por ejemplo, en «Los gato duermen», el sustantivo es «gato». «Los» está en plural, pero «gato» no. Se corrige: «Los gatos duermen». También el verbo debe coincidir con quien hace la acción. Si son varios, el verbo va en plural: «los gatos duermen», «mi amiga y yo cantamos».",
    ],
    [("editar", "mejorar un texto corrigiendo detalles"), ("concordancia", "que las palabras coincidan en género y número"), ("subrayar", "marcar con una línea"), ("corregir", "cambiar para que quede bien"), ("verbo", "palabra que dice qué hace alguien")],
    [
        ("Corregir una oración", "Edita: «Los gato duermen».", ["Subrayo «gato».", "«Los» es plural; «gato» está en singular.", "Cambio a «gatos»."], "Los gatos duermen."),
        ("Corregir género y número", "Edita: «Las flor amarillo huelen bien».", ["El sustantivo es «flor».", "Con «las» debe ser plural: flores.", "Amarillo debe ser femenino plural: amarillas."], "Las flores amarillas huelen bien."),
    ],
    [("Corregir una sola palabra.", "Se piensa que el error es uno solo.", "Revisa todas las palabras del grupo."), ("No releer después de corregir.", "Se cree que ya está bien.", "Lee la oración corregida en voz alta.")],
    [
        E("En «Los gato duermen», ¿cuál palabra tiene el error?", "gato", "Debe estar en plural."),
        E("Corrige «el niña».", "la niña", "Niña es femenino."),
        E("En «Las flor huelen bien», ¿qué falta en «flor»?", "La terminación de plural -es", "Debe ser flores."),
    ],
    [
        E("Ordena los pasos: A) corregir, B) encontrar el sustantivo, C) revisar artículo y adjetivo, D) releer.", "B, C, A, D", "Primero el sustantivo, luego revisar, corregir y releer."),
        E("¿Por qué conviene releer el texto corregido?", "Para comprobar que todo concuerda", "Así veo si quedó algún error."),
        E("En «El profesora lee», sin cambiar la palabra «profesora», ¿qué artículo hay que corregir?", "El, debe ser la", "Profesora es femenino."),
    ],
    [
        E("Edita: «La niña pequeño juega».", "La niña pequeña juega.", "El adjetivo debe ser femenino."),
        E("Edita: «Los pájaro vuelan alto».", "Los pájaros vuelan alto.", "Pájaro debe estar en plural."),
        E("Edita: «Mis amigas es simpático».", "Mis amigas son simpáticas.", "Todo debe estar en femenino plural."),
    ],
    [
        E("Un niño corrigió «los gato negro» y escribió «los gatos negro». ¿Qué le falta?", "Poner el adjetivo en plural: los gatos negros", "Debe revisar todas las palabras."),
        E("¿Por qué un error de concordancia puede confundir al lector?", "Porque no queda claro de cuántos o de quiénes se habla", "El número y género dan información."),
    ],
    [
        E("Edita, dejando la palabra «niño» (en plural): «Las niño alto juegan en el parque».", "Los niños altos juegan en el parque.", "Se ajusta todo el grupo."),
        arith("Un texto tiene 6 errores de concordancia. Corriges 4. ¿Cuántos errores quedan?", "6-4", "Se restan los corregidos."),
    ],
    [E("En una nota de la escuela dice: «Los alumno nuevos traerá su lápices». Edítala.", "Los alumnos nuevos traerán sus lápices.", "Todo coincide en plural.")],
    [
        E("¿Qué palabra busco primero al editar la concordancia?", "El sustantivo", "Las demás palabras se ajustan a él."),
        E("¿Subrayar ayuda a encontrar errores?", "Sí", "Marca lo que debo revisar."),
        E("¿El verbo también debe coincidir con quien hace la acción?", "Sí", "Debe estar en el mismo número."),
    ],
    ("Edita este texto subrayando los errores y escribiéndolo corregido. Texto: «Los niñas juegan en el parques. Las perro grande corre rápido. Mi amiga y yo cantan una canciones bonito». Hay más de una forma correcta.",
     "Las niñas juegan en el parque (o en los parques). Los perros grandes corren rápido (o: La perra grande corre rápido). Mi amiga y yo cantamos una canción bonita (o unas canciones bonitas).",
     ["subraya los errores", "corrige artículo, sustantivo y adjetivo", "relee el texto corregido"], ["texto original subrayado y versión final"], ["corregir solo una palabra por grupo", "no cambiar el verbo"],
     "Pide que lea cada oración corregida en voz alta y diga qué cambió y por qué."),
    "Busca en un cuaderno tuyo una oración con una concordancia y revísala.",
    "Inventa tres oraciones con errores de concordancia, intercámbialas con alguien y corrígelas.",
)

# ================================================================ OA 21 · clase 1
reg(
    OA21, 1,
    "Las palabras de este cuaderno, lápiz y hoja. Tarjetas de papel si quieres armar palabras.",
    "Aprenderé a escribir bien las sílabas ce, ci, que y qui. Sirve para que otros lean mis palabras sin dificultad.",
    ["Sé que algunas letras suenan igual.", "Sé separar palabras en sílabas."],
    [
        "La letra c suena como la s cuando va antes de e o i: cena, cine, cebra, cielo. En cambio, el sonido de la k antes de e o i se escribe qu: queso, quince, esquina, parque. En «que» y «qui» la u no se pronuncia.",
        "Con a, o, u la c suena como k: casa, color, cuchara. Pero antes de e, i necesitamos qu para ese sonido: que, qui. Compara «cena» (suena s) con «queso» (suena k).",
        "Para escribir bien, di la palabra despacio y escucha el sonido. Si suena como s antes de e o i, quizás va con c; si suena como k antes de e o i, va con qu. Si dudas, consulta un diccionario.",
    ],
    [("ce, ci", "sílabas en que la c suena como s"), ("que, qui", "sílabas en que qu suena como k y la u no suena"), ("sílaba", "parte de una palabra que se dice de una vez"), ("diccionario", "libro que muestra cómo se escriben las palabras"), ("sonido", "lo que oímos al decir una letra")],
    [
        ("Elegir entre ce y que", "Completa: ___so (alimento hecho con leche).", ["Digo la palabra: ___so.", "El sonido es k antes de e.", "Se escribe «que»."], "Queso."),
        ("Elegir entre ci y qui", "Completa: ___ne (donde vemos películas).", ["Digo la palabra: ___ne.", "El sonido es s antes de i.", "Se escribe «ci»."], "Cine."),
    ],
    [("Escribir «kerer» o «sine».", "Se escribe como suena sin pensar en las reglas.", "Antes de e o i, usa qu para el sonido k y c para el sonido s."), ("Pronunciar la u en «que» y «qui».", "Se cree que la u suena.", "En que y qui la u no se pronuncia, solo acompaña.")],
    [
        E("Completa: ___so (alimento hecho con leche). Opciones: ce o que.", "que", "Se escribe «queso»."),
        E("Completa: ___ne (donde vemos películas). Opciones: ci o qui.", "ci", "Se escribe «cine»."),
        E("¿Suena la u en «queso»?", "No", "En «que» la u no se pronuncia."),
    ],
    [
        E("¿Qué letras forman el sonido k antes de e o i: c o qu?", "qu", "Así se escribe: que, qui."),
        E("¿Cuál está bien escrita: «cielo» o «sielo»?", "cielo", "Con el sonido s antes de i se usa c."),
        E("En «quince», ¿suena la u?", "No", "En «qui» la u no se pronuncia."),
    ],
    [
        E("Completa: ___bolla (se usa en la ensalada). Opciones: ce o que.", "ce", "Se escribe «cebolla»."),
        E("Completa: ___nco (el número que sigue al cuatro). Opciones: ci o qui.", "ci", "Se escribe «cinco»."),
        E("Completa: es___na (donde se juntan dos calles). Opciones: qui o ci.", "qui", "Se escribe «esquina»."),
    ],
    [
        E("Pedro escribió «sena» para la comida de la noche. ¿Cómo se escribe bien?", "cena", "El sonido s antes de e se escribe con c."),
        E("En «quiero» y «cuero», ¿en cuál suena la u?", "cuero", "En «cuero» se pronuncia la u; en «quiero» no."),
    ],
    [
        E("Une las sílabas es + qui + na y escribe la palabra.", "esquina", "La unión forma esquina."),
        E("¿Cuántas palabras con que, qui o ce hay en «Quiero queso en la cena»?", "3", "Quiero, queso y cena."),
    ],
    [E("En tu lista de compras aparece «keso» y «sebolla». Escríbelas bien.", "queso y cebolla", "Se escriben con qu y con c.")],
    [
        E("¿Cuál se escribe con c: «cena» o «kena»?", "cena", "El sonido s antes de e se escribe c."),
        E("¿Cómo se escribe correctamente el sonido k en «parque»?", "Con qu", "Antes de e se usa qu."),
        E("¿Qué hago si dudo cómo se escribe una palabra?", "Consulto un diccionario", "Allí aparece bien escrita."),
    ],
    ("Completa las seis palabras con ce, ci, que o qui y luego escribe una oración con tres de ellas. Palabras: 1) ___rca (lugar próximo). 2) ___so (alimento hecho con leche). 3) ___nturón (cinta para sujetar el pantalón). 4) pa___te (caja pequeña que se envía por correo). 5) ___rer (desear algo). 6) ___ncuenta (el número 50).",
     "cerca, queso, cinturón, paquete, querer, cincuenta. Oración: Quiero queso para la cena.",
     ["completa seis palabras bien", "usa c y qu correctamente", "escribe una oración con tres palabras"], ["lista de palabras y una oración"], ["escribir «k» en lugar de «qu»", "no pronunciar la palabra antes de elegir"],
     "Si se equivoca, pide que diga la palabra despacio y encuentre el sonido."),
    "Busca en un libro cinco palabras con que o qui y cópialas.",
    "Escribe diez palabras con ce, ci, que o qui en dos columnas.",
)

# ================================================================ OA 21 · clase 2
reg(
    OA21, 2,
    "Las palabras de este cuaderno, lápiz y hoja.",
    "Aprenderé a escribir bien ge, gi, gue, gui, güe y güi. Sirve para no confundirme con las letras g y u.",
    ["Sé que la letra g puede sonar de dos formas.", "Sé leer y escribir sílabas."],
    [
        "La letra g suena fuerte, como la j, cuando va antes de e o i: gente, girasol, gigante, gelatina. Pero a veces suena suave: gato, gota, gusano. Para que suene suave antes de e o i, se escribe una u: guerra, guiso, guitarra. Esa u no suena.",
        "Cuando la u sí debe sonar, se le pone dos puntitos encima. Esos dos puntitos se llaman diéresis. Así se escribe: pingüino, cigüeña, vergüenza. Compara «guiso» (la u no suena) con «pingüino» (la u sí suena).",
        "Hay palabras con j que suenan igual que ge o gi, como jirafa y jefe. No hay regla simple: hay que aprenderlas. Si dudas, usa el diccionario.",
    ],
    [("ge, gi", "sílabas en que la g suena como j"), ("gue, gui", "sílabas en que la g suena suave y la u no suena"), ("güe, güi", "sílabas en que la u sí suena"), ("diéresis", "los dos puntitos sobre la ü"), ("suave", "con sonido débil, no fuerte")],
    [
        ("Elegir entre gi y gui", "Completa: ___tarra (instrumento con seis cuerdas).", ["Digo la palabra: _tarra.", "La g suena suave y la u no suena.", "Se escribe «gui»."], "Guitarra."),
        ("Elegir entre gui y güi", "Completa: pin___no (ave que vive en el hielo y no vuela).", ["Digo la palabra: pin_no.", "Aquí la u sí suena.", "Se escribe con diéresis: «güi»."], "Pingüino."),
    ],
    [("Escribir «pinguino» sin diéresis.", "Se olvida que la u suena.", "Pon los dos puntitos para que la u suene: pingüino."), ("Poner diéresis a «guitarra».", "Se mezcla con las palabras donde la u suena.", "Si la u no suena, no lleva diéresis.")],
    [
        E("¿Cuál se escribe con ge: gente o jente?", "gente", "Se escribe con g."),
        E("Completa: ___tarra (instrumento con seis cuerdas). Opciones: gi o gui.", "gui", "Se escribe «guitarra»."),
        E("Completa: pin___no (ave que vive en el hielo). Opciones: gui o güi.", "güi", "Se escribe «pingüino»."),
    ],
    [
        E("¿Suena la u en «guitarra»?", "No", "En gui la u no suena."),
        E("¿Cómo se llaman los dos puntitos sobre la u en «pingüino»?", "Diéresis", "Indican que la u debe sonar."),
        E("¿Cuál lleva diéresis: «guerra» o «vergüenza»?", "vergüenza", "Allí la u debe sonar."),
    ],
    [
        E("Completa: ___gante (muy grande). Opciones: ge o gi.", "gi", "Se escribe «gigante»."),
        E("Completa: ci___ña (ave de patas largas). Opciones: gue o güe.", "güe", "Se escribe «cigüeña»."),
        E("Completa: ___rra (lucha entre países). Opciones: gue o güe.", "gue", "Se escribe «guerra»."),
    ],
    [
        E("Beto escribió «pinguino». ¿Qué falta?", "La diéresis sobre la u: pingüino", "En esa palabra la u sí suena."),
        E("¿Por qué «guiso» no lleva diéresis?", "Porque la u no suena", "Solo se usa diéresis si la u suena."),
    ],
    [
        E("Corrige: «El pinguino tiene verguenza».", "El pingüino tiene vergüenza.", "En ambas palabras la u suena."),
        E("¿Cuántas palabras llevan diéresis en «La cigüeña y el pingüino sienten vergüenza»?", "3", "Cigüeña, pingüino y vergüenza."),
    ],
    [E("En el zoológico hay un cartel que dice «Zona de pinguinos». Escribe bien la palabra.", "Zona de pingüinos", "Hay que poner diéresis para que la u suene.")],
    [
        E("¿La g suena fuerte antes de e y de i?", "Sí", "Suena como la j."),
        E("¿En «gigante» la g suena fuerte o suave?", "Fuerte", "Suena como la j."),
        E("Para que la g suene suave antes de e o i, ¿qué letra agrego?", "La u", "Así se escribe gue o gui."),
    ],
    ("Completa las cinco palabras con ge, gi, gue, gui, güe o güi y escribe una oración con dos de ellas. Palabras: 1) ___rra (lucha entre países). 2) ___so (comida que se cocina en una olla). 3) ci___ña (ave de patas largas). 4) ___latina (postre que tiembla). 5) pin___no (ave que vive en el hielo).",
     "guerra, guiso, cigüeña, gelatina, pingüino. Oración: El pingüino comió gelatina.",
     ["completa cinco palabras bien", "distingue gue/gui de güe/güi", "escribe una oración correcta"], ["lista y oración"], ["olvidar la diéresis", "confundir ge con gue"],
     "Si duda entre gui y güi, pregunta: «¿Se escucha la u cuando la digo?»."),
    "Busca en un libro tres palabras con ge o gi y cópialas.",
    "Escribe diez palabras con g y j que suenen igual y revisa su escritura en el diccionario.",
)

# ================================================================ OA 21 · clase 3
reg(
    OA21, 3,
    "Las palabras de este cuaderno, lápiz y hoja.",
    "Aprenderé a escribir bien r y rr. Sirve para no cambiar el significado de las palabras.",
    ["Sé que la r tiene dos sonidos.", "Conozco palabras como perro y pero."],
    [
        "La r puede sonar suave, como en «pera», o fuerte, como en «perro». El sonido fuerte se escribe de dos formas. Al comienzo de una palabra se escribe con una r: rana, ropa. Entre vocales se escribe con dos rr: perro, carro, cerro.",
        "También suena fuerte después de n, l o s. En ese caso se escribe una sola r: Enrique, honrado, alrededor, Israel. Si pones dos rr entre vocales, el sonido es fuerte, y si pones una, es suave. Esto cambia el significado: «pero» no es lo mismo que «perro», ni «cero» es lo mismo que «cerro».",
        "Para escribir bien, di la palabra despacio. Pregunta: ¿suena fuerte? ¿Dónde está? Si está al inicio o después de n, l o s, va una r. Si está entre vocales, va rr.",
    ],
    [("r suave", "sonido de la r en «pera»"), ("r fuerte", "sonido de la r en «perro»"), ("rr", "dos erres que suenan fuerte entre vocales"), ("vocal", "a, e, i, o, u"), ("significado", "lo que quiere decir una palabra")],
    [
        ("Escribir r fuerte al inicio", "Completa: ___ana (animal verde que salta y vive cerca del agua).", ["La palabra comienza con sonido fuerte.", "Al comienzo se usa una sola r."], "Rana."),
        ("Escribir rr entre vocales", "Completa: pe___o (animal que ladra).", ["El sonido fuerte está entre dos vocales.", "Entre vocales se escribe rr."], "Perro."),
    ],
    [("Escribir «rrana» al inicio de una palabra.", "Se cree que el sonido fuerte siempre lleva rr.", "Al inicio se usa una sola r."), ("Escribir «caro» cuando quiero decir «carro».", "No se escucha la diferencia de sonido.", "Di la palabra: si suena fuerte entre vocales, usa rr.")],
    [
        E("Completa: ___ana (animal verde que salta). Opciones: r o rr.", "r", "Al comienzo se usa una sola r."),
        E("Completa: pe___o (animal que ladra). Opciones: r o rr.", "rr", "Entre vocales con sonido fuerte se usa rr."),
        E("¿Con una r o dos rr se escribe «ropa»?", "Con una r", "Está al inicio."),
    ],
    [
        E("¿Qué diferencia hay entre «pero» y «perro»?", "«Pero» es una palabra de unión y «perro» es un animal", "La r suave o fuerte cambia el significado."),
        E("Entre vocales y con sonido fuerte, ¿se escribe r o rr?", "rr", "Se usa rr para el sonido fuerte."),
        E("En «Enrique», ¿se escribe r o rr después de la n?", "r", "Después de n se usa una sola r."),
    ],
    [
        E("Completa: ca___o (vehículo con ruedas). Opciones: r o rr.", "rr", "Se escribe «carro»."),
        E("Completa: hon___ado (persona que actúa con verdad). Opciones: r o rr.", "r", "Después de n va una r."),
        E("Completa: al___ededor (en torno a algo). Opciones: r o rr.", "r", "Después de l va una r."),
    ],
    [
        E("Tomás escribió «rrana». ¿Cuál es el error?", "Al comienzo de palabra se usa una sola r", "El sonido fuerte al inicio es con r."),
        E("Ana dice que «cero» y «cerro» se escriben igual. ¿Tiene razón?", "No, «cero» es un número y «cerro» es un monte", "La rr cambia el significado."),
    ],
    [
        E("Completa con pero o perro: «Mi ___ es pequeño, ___ es veloz».", "perro, pero", "Primero el animal y luego la palabra de unión."),
        E("¿Cuántas palabras con rr hay en «El perro subió al cerro y empujó el carro»?", "3", "Perro, cerro y carro."),
    ],
    [E("Rotulas el dibujo de un animal de cuatro patas que ladra. ¿Escribes «pero» o «perro»?", "perro", "El animal se escribe con rr.")],
    [
        E("¿«Rosa» se escribe con r o con rr?", "Con r", "Está al inicio."),
        E("¿«Barro» se escribe con r o con rr?", "Con rr", "Entre vocales suena fuerte."),
        E("En «Israel», ¿se escribe r o rr después de la s?", "r", "Después de s va una sola r."),
    ],
    ("Completa las seis palabras con r o rr y escribe una oración con dos de ellas. Palabras: 1) ___opa (lo que nos ponemos). 2) pe___o (animal que ladra). 3) ___eloj (marca la hora). 4) co___al (lugar cercado para animales). 5) en___edo (lío o confusión). 6) hon___a (respeto por una persona).",
     "ropa, perro, reloj, corral, enredo, honra. Oración: Mi perro rompió la ropa.",
     ["completa seis palabras", "usa r o rr según corresponda", "escribe una oración correcta"], ["lista y oración"], ["usar rr al inicio", "usar r entre vocales para el sonido fuerte"],
     "Pide que diga cada palabra despacio y diga si la r está al inicio, entre vocales o después de n."),
    "Escribe tres palabras con rr y tres con r fuerte al inicio.",
    "Busca cinco pares de palabras que cambian de significado con r y rr.",
)

# ================================================================ OA 21 · clase 4
reg(
    OA21, 4,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé cuándo se usa mayúscula: al empezar una oración y en nombres propios. Sirve para que el lector reconozca el inicio y los nombres.",
    ["Sé qué es una oración.", "Sé la diferencia entre mayúscula y minúscula."],
    [
        "Usamos mayúscula en dos casos. El primero es la primera letra de una oración: «Hoy fui al parque». El segundo es la primera letra de los nombres propios: los nombres de personas, mascotas y lugares, como Camila, Luna, Chile o Valparaíso.",
        "Los nombres que no son propios van con minúscula: «niño», «perro», «ciudad». En «Mi perro Bruno vive en Temuco», solo Mi, Bruno y Temuco llevan mayúscula. Los días de la semana y los meses también van con minúscula: lunes, marzo.",
        "Para revisar, mira cada palabra y pregunta: ¿empieza una oración? ¿Es el nombre de alguien o de un lugar en particular? Si la respuesta es sí, va con mayúscula.",
    ],
    [("nombre propio", "nombre de una persona, mascota o lugar en particular"), ("mayúscula", "letra grande"), ("minúscula", "letra pequeña"), ("mascota", "animal que vive con una familia"), ("lugar", "sitio donde algo está")],
    [
        ("Corregir un nombre de lugar", "Corrige: «vivo en valparaíso».", ["La oración empieza con mayúscula: Vivo.", "Valparaíso es un lugar en particular, va con mayúscula."], "Vivo en Valparaíso."),
        ("Corregir varios nombres", "Corrige: «mi amiga paula vive en chile».", ["Mi empieza la oración.", "Paula es un nombre de persona.", "Chile es un nombre de país."], "Mi amiga Paula vive en Chile."),
    ],
    [("Escribir «hoy es Lunes».", "Se cree que los días son nombres propios.", "Los días y los meses van con minúscula: lunes."), ("Escribir «mi Perro Bruno».", "Se pone mayúscula a palabras comunes.", "Solo el nombre propio va con mayúscula: mi perro Bruno.")],
    [
        E("¿El nombre «camila» empieza con mayúscula o minúscula?", "Mayúscula", "Es un nombre de persona."),
        E("¿«Chile» lleva mayúscula?", "Sí", "Es el nombre de un país."),
        E("Corrige «mi gato se llama tomás».", "Mi gato se llama Tomás.", "Empieza la oración y el nombre es propio."),
    ],
    [
        E("¿En qué dos casos usamos mayúscula?", "Al empezar una oración y en nombres propios", "Son los dos usos."),
        E("En «Mi perro Bruno», ¿lleva mayúscula «perro»?", "No", "Perro es un nombre común; Bruno es propio."),
        E("En Lenguaje: ¿Qué es un nombre propio?", "El nombre de alguien o de un lugar en particular", "Nombra algo único."),
    ],
    [
        E("Corrige: «vivo en valparaíso».", "Vivo en Valparaíso.", "Inicio de oración y lugar."),
        E("Corrige: «mi amiga paula vive en chile».", "Mi amiga Paula vive en Chile.", "Inicio, persona y país."),
        E("¿Cuántas mayúsculas hay en «Mi tío Pedro viajó a Arica. Vio el mar»?", "4", "Mi, Pedro, Arica y Vio."),
    ],
    [
        E("Eva escribió «Hoy es Lunes». ¿Es correcto?", "No, los días van con minúscula: lunes", "Los días no son nombres propios."),
        E("Pedro escribió «Mi Perro se llama luna». ¿Qué errores tiene?", "Perro va con minúscula y Luna con mayúscula", "Luna es el nombre propio de la mascota."),
    ],
    [
        E("Escribe con mayúsculas donde corresponda: «el domingo fui con mi prima sofía a santiago».", "El domingo fui con mi prima Sofía a Santiago.", "Inicio, persona y lugar."),
        arith("Escribes 5 oraciones y en ellas hay 2 nombres propios, sin contar las palabras que inician oración. ¿Cuántas mayúsculas necesitas en total?", "5+2", "Una por cada inicio y una por cada nombre propio."),
    ],
    [E("En un sobre escribes: «para mi tía rosa, de valdivia». Escríbelo bien.", "Para mi tía Rosa, de Valdivia", "Inicio de oración, persona y ciudad.")],
    [
        E("¿«Marzo» lleva mayúscula en medio de una oración?", "No", "Los meses van con minúscula."),
        E("¿El nombre de mi mascota lleva mayúscula?", "Sí", "Es un nombre propio."),
        E("¿La palabra «ciudad» lleva mayúscula?", "No", "Es un nombre común."),
    ],
    ("Reescribe este texto con las mayúsculas correctas. Texto: «el sábado mi hermano tomás y yo fuimos a la playa de viña del mar. mi perro luna nos acompañó. en marzo volveremos». Luego encierra con un círculo los nombres propios (Viña del Mar es un solo nombre: lleva mayúscula en Viña y en Mar).",
     "El sábado mi hermano Tomás y yo fuimos a la playa de Viña del Mar. Mi perro Luna nos acompañó. En marzo volveremos. Nombres propios: Tomás, Viña del Mar, Luna.",
     ["usa mayúscula al inicio de cada oración", "escribe mayúscula en los nombres propios", "deja «marzo» y «sábado» con minúscula"], ["texto reescrito con círculos"], ["poner mayúscula a «sábado» o «marzo»", "olvidar «Luna»"],
     "Pregunta: «¿Es el nombre de alguien o de un lugar en particular?»."),
    "Escribe los nombres de cinco personas de tu familia con su mayúscula.",
    "Haz una lista de diez nombres propios (personas, mascotas y lugares) con mayúscula.",
)

# ================================================================ OA 21 · clase 5
reg(
    OA21, 5,
    "Los textos de este cuaderno, lápiz y hoja.",
    "Aprenderé a poner el punto al final de cada oración para separar las ideas de un texto. Sirve para que el lector entienda dónde termina cada idea.",
    ["Sé usar mayúsculas al inicio de una oración.", "Sé qué es una oración."],
    [
        "El punto va al final de cada oración. Nos avisa que una idea terminó. Después del punto empieza una idea nueva con mayúscula. Sin puntos, las ideas se mezclan y el texto cuesta entender.",
        "A veces unimos muchas ideas con la palabra «y»: «Fui al parque y me caí y lloré y mi mamá me ayudó». Es mejor separar con puntos: «Fui al parque. Me caí. Lloré. Mi mamá me ayudó». Ahora cada idea se lee clara.",
        "No pongas punto en medio de una idea: «Mi. gato come» es un error. Cada oración debe quedar completa antes del punto. Para revisar, lee en voz alta y detente cada vez que termina una idea.",
    ],
    [("punto", "signo que termina una oración"), ("idea", "lo que pienso y quiero decir"), ("separar", "poner aparte"), ("completo", "que tiene todo lo necesario"), ("texto", "conjunto de oraciones que dicen algo")],
    [
        ("Separar ideas con puntos", "Escribe con puntos y mayúsculas: «me desperté desayuné fui a la escuela».", ["Encuentro tres ideas.", "Pongo punto después de cada una.", "Cada idea nueva empieza con mayúscula."], "Me desperté. Desayuné. Fui a la escuela."),
        ("Mejorar un texto con muchas «y»", "Mejora: «Fui al parque y me caí y lloré y mi mamá me ayudó».", ["Separo cada idea.", "Pongo punto al final de cada una."], "Fui al parque. Me caí. Lloré. Mi mamá me ayudó."),
    ],
    [("Poner punto en medio de una idea.", "No se mira si la oración está completa.", "El punto va cuando la idea termina."), ("Unir todo con «y».", "Se escribe como se habla.", "Separa las ideas con puntos.")],
    [
        E("¿Cuántas ideas hay en «Me desperté. Desayuné. Fui a la escuela»?", "3", "Hay tres oraciones."),
        E("¿Qué signo va al final de «Hoy llueve»?", "Punto", "Cierra la oración."),
        E("¿Con qué letra empieza la oración que sigue a un punto?", "Mayúscula", "Una idea nueva empieza con letra grande."),
    ],
    [
        E("¿Por qué ayuda el punto a quien lee?", "Porque sabe cuándo termina una idea", "El punto marca el final."),
        E("«Fui al parque y me caí y lloré y mi mamá me ayudó» tiene muchas «y». ¿Cómo se mejora?", "Separando las ideas con puntos", "Cada idea queda clara."),
        E("¿Cuál tiene el punto bien puesto: «Mi papá. cocina rico.» o «Mi papá cocina rico.»?", "Mi papá cocina rico.", "El punto va al final de la idea."),
    ],
    [
        E("Pon puntos y mayúsculas: «mi gato duerme mucho ronronea cuando lo acaricio».", "Mi gato duerme mucho. Ronronea cuando lo acaricio.", "Hay dos ideas."),
        E("Agrega los puntos: «Hoy salimos temprano Fuimos al museo Vimos fósiles».", "Hoy salimos temprano. Fuimos al museo. Vimos fósiles.", "Hay tres ideas."),
        E("¿Cuántos puntos necesita «Llegué a casa Me lavé las manos Comí»?", "3", "Uno por cada idea, incluyendo el final."),
    ],
    [
        E("Un niño escribe «Mi. gato. come.». ¿Cuál es el error?", "Pone punto después de cada palabra y no al final de la idea", "El punto va cuando termina la oración completa."),
        E("Ana dice que no hace falta el punto final del texto. ¿Qué le dices?", "Sí hace falta, porque cierra la última idea", "Todo texto termina con punto."),
    ],
    [
        E("Separa en dos oraciones: «El sábado fuimos al cerro hacía mucho viento».", "El sábado fuimos al cerro. Hacía mucho viento.", "Son dos ideas."),
        arith("Un texto tiene 6 ideas y ya pusiste 4 puntos. ¿Cuántos puntos faltan?", "6-4", "Cada idea necesita su punto."),
    ],
    [E("Escribes un mensaje: «mamá ya llegué a la escuela estoy bien». Escríbelo con mayúsculas, una coma después de «Mamá» y puntos.", "Mamá, ya llegué a la escuela. Estoy bien.", "Son dos ideas separadas por punto.")],
    [
        E("¿Qué signo cierra una idea?", "El punto", "Indica que la idea terminó."),
        E("¿Pongo punto en medio de una oración que aún no termina?", "No", "La idea aún sigue."),
        E("Después del punto, ¿qué letra va?", "Mayúscula", "La idea nueva empieza con mayúscula."),
    ],
    ("Arregla este texto con puntos y mayúsculas, separando cada idea. Texto: «el sábado fui a la casa de mi abuela ella cocinó empanadas yo la ayudé a amasar después comimos juntos fue un día muy lindo».",
     "El sábado fui a la casa de mi abuela. Ella cocinó empanadas. Yo la ayudé a amasar. Después comimos juntos. Fue un día muy lindo.",
     ["separa las cinco ideas", "pone punto al final de cada una", "usa mayúscula después de cada punto"], ["texto reescrito"], ["dejar dos ideas pegadas", "olvidar el punto final"],
     "Pide que lea en voz alta y haga una pausa en cada punto; si no hay pausa, falta un punto."),
    "Escribe tres oraciones sobre tu día y pon el punto en cada una.",
    "Escribe un texto de seis oraciones y pídele a alguien que cuente cuántos puntos usaste.",
)

# ================================================================ OA 21 · clase 6
reg(
    OA21, 6,
    "Las oraciones de este cuaderno, lápiz y hoja.",
    "Aprenderé a escribir preguntas y exclamaciones con dos signos, uno al inicio y otro al final. Sirve para que el lector sepa cuándo preguntas o cuándo muestras una emoción.",
    ["Sé qué es una pregunta.", "Sé qué es una exclamación."],
    [
        "En español las preguntas llevan dos signos: uno al principio (¿) y otro al final (?). Por ejemplo: «¿Cómo te llamas?». Las exclamaciones también llevan dos signos: uno al principio (¡) y otro al final (!). Por ejemplo: «¡Qué día tan lindo!».",
        "Usamos la pregunta para pedir información. Usamos la exclamación para mostrar una emoción, como alegría, sorpresa o miedo. El signo de apertura va antes de la primera palabra de la pregunta o la exclamación. El de cierre va después de la última.",
        "No olvides ninguno de los dos signos. Si escribes solo uno, el lector no sabe dónde empieza o termina. Y después del signo de cierre no se escribe punto.",
    ],
    [("pregunta", "oración con que pedimos información"), ("exclamación", "oración con que mostramos una emoción"), ("signo de apertura", "el que va al inicio: ¿ o ¡"), ("signo de cierre", "el que va al final: ? o !"), ("emoción", "lo que siento, como alegría o sorpresa")],
    [
        ("Escribir una pregunta", "Pon los signos: «Dónde está mi mochila».", ["Es una pregunta.", "Abro con ¿ antes de «Dónde».", "Cierro con ? al final."], "¿Dónde está mi mochila?"),
        ("Escribir una exclamación", "Pon los signos: «Qué día tan lindo».", ["Muestra alegría.", "Abro con ¡ antes de «Qué».", "Cierro con ! al final."], "¡Qué día tan lindo!"),
    ],
    [("Escribir solo el signo de cierre.", "Se escribe como en otros idiomas.", "En español se escribe también el de apertura."), ("Poner punto después del signo de cierre.", "Se cree que toda oración termina con punto.", "El signo de cierre ya termina la oración.")],
    [
        E("¿Cuántos signos lleva una pregunta: uno o dos?", "Dos", "Uno de apertura y otro de cierre."),
        E("¿Qué signo abre una pregunta: ¿ o ¡?", "¿", "El de pregunta es ¿."),
        E("¿Qué signos usas para mostrar sorpresa o alegría: ¡! o ¿?", "¡!", "Son los signos de exclamación."),
    ],
    [
        E("¿Cuál está bien: «Cómo te llamas?» o «¿Cómo te llamas?»?", "¿Cómo te llamas?", "Lleva signo de apertura y de cierre."),
        E("¿Qué muestra una exclamación?", "Una emoción", "Alegría, sorpresa o miedo."),
        E("¿Dónde va el signo de apertura: antes de la primera palabra o después de la última?", "Antes de la primera palabra", "Abre la pregunta o la exclamación."),
    ],
    [
        E("Pon los signos: «Qué rico huele el pan».", "¡Qué rico huele el pan!", "Muestra una emoción de alegría."),
        E("Pon los signos: «Cuándo es tu cumpleaños».", "¿Cuándo es tu cumpleaños?", "Pide una información."),
        E("Pon los signos: «Cuántos años tienes».", "¿Cuántos años tienes?", "Pide una información."),
    ],
    [
        E("Rosa escribió «¿Qué hora es.». ¿Cuál es el error?", "Falta el signo de cierre ? y sobra el punto", "La pregunta se cierra con ?."),
        E("Escribe con signos: a) «Qué susto me diste» (emoción) b) «Qué hora es» (pregunta).", "a) ¡Qué susto me diste! b) ¿Qué hora es?", "La primera muestra emoción y la segunda pide información."),
    ],
    [
        E("Arregla en tres oraciones (un saludo con emoción, una pregunta y una exclamación): «hola cómo estás qué bueno verte».", "¡Hola! ¿Cómo estás? ¡Qué bueno verte!", "Saludo, pregunta y exclamación."),
        arith("Una pregunta usa 2 signos. Escribes 3 preguntas. ¿Cuántos signos usas en total?", "3*2", "Cada pregunta lleva dos signos."),
    ],
    [E("Llegas a casa y quieres saber si hay pan. Escribe la pregunta en una nota con los signos correctos.", "¿Hay pan?", "Es una pregunta y lleva dos signos.")],
    [
        E("¿Una pregunta lleva punto después del signo de cierre?", "No", "El signo de cierre ya termina."),
        E("¿Cómo se llama el signo ¡?", "Signo de apertura de exclamación", "Abre la exclamación."),
        E("¿Qué pasa si falta uno de los dos signos?", "El lector no sabe dónde empieza o termina", "Por eso van los dos."),
    ],
    ("Escribe estas cinco oraciones con los signos correctos. 1) cómo estás. 2) qué miedo. 3) cuántos lápices tienes. 4) qué rico está el pan. 5) dónde vive tu abuela. Después marca cuáles son preguntas y cuáles exclamaciones.",
     "1) ¿Cómo estás? (pregunta). 2) ¡Qué miedo! (exclamación). 3) ¿Cuántos lápices tienes? (pregunta). 4) ¡Qué rico está el pan! (exclamación). 5) ¿Dónde vive tu abuela? (pregunta).",
     ["usa los dos signos en cada oración", "distingue pregunta de exclamación", "escribe mayúscula al inicio"], ["cinco oraciones con signos"], ["olvidar el signo de apertura", "poner punto después del signo"],
     "Pide que diga qué siente o qué quiere saber en cada oración para elegir los signos."),
    "Escribe una pregunta y una exclamación sobre tu día.",
    "Escribe un diálogo de seis líneas entre dos personas con preguntas y exclamaciones.",
)

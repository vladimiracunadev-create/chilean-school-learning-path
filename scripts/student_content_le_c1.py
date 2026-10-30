"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 19 (palabras desconocidas) y OA 20 (experiencia teatral)."""
from __future__ import annotations

from student_lessons import ex, register

OA19, OA20 = "LE01 OA 19", "LE01 OA 20"
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


# ================================================================ OA 19
reg(
    OA19, 1,
    "Las frases de este cuaderno, un lápiz y una hoja. Un adulto puede leer las frases en voz alta; no se necesitan otros materiales.",
    "Aprenderé a darme cuenta de cuándo no entiendo una palabra y a decirlo sin vergüenza. Sirve para entender mejor lo que leo y lo que escucho.",
    ["Sé leer o escuchar frases cortas.", "Sé que cada palabra tiene un significado."],
    [
        "A veces leemos o escuchamos una palabra que no conocemos. Eso le pasa a todas las personas, también a los adultos. Esa palabra se llama palabra desconocida. Lo importante es darse cuenta y detenerse, en vez de seguir de largo.",
        "Para notarla, hazte esta pregunta mientras lees: ¿entendí todo lo que dice? Si una parte queda confusa, busca cuál es la palabra que te frena. Por ejemplo, en «El gato caminó sigiloso por el pasillo», quizás no sabes cómo caminó el gato. La palabra que te frena es «sigiloso».",
        "Decir «no sé qué significa esta palabra» no es una falla. Es una buena estrategia, porque es el primer paso para averiguar su significado. Después podrás buscar pistas, preguntar o consultar un diccionario.",
    ],
    [("palabra desconocida", "una palabra que no sé qué significa"), ("significado", "lo que quiere decir una palabra"), ("detenerme", "parar un momento para pensar"), ("estrategia", "una forma de resolver algo"), ("preguntar", "pedir ayuda para saber algo")],
    [
        ("Encontrar la palabra que frena", "Lee: «El gato caminó sigiloso por el pasillo. Nadie lo escuchó.» ¿Qué palabra podría ser desconocida?", ["Leo la frase completa.", "Me pregunto qué parte no entiendo: no sé cómo caminó el gato.", "La palabra que me frena es «sigiloso»."], "La palabra desconocida es «sigiloso»."),
        ("Decirlo en voz alta", "Pedro escuchó «El vecino es muy generoso» y no sabe qué significa «generoso». ¿Qué puede decir?", ["Se detiene en la palabra.", "Lo dice con calma, sin vergüenza."], "Puede decir: «No sé qué significa generoso»."),
    ],
    [("Seguir leyendo como si nada.", "Da vergüenza decir que no se entiende.", "Detente y marca la palabra que te frena."), ("Pensar que solo los niños no saben palabras.", "Nadie conoce todas las palabras.", "Recuerda que preguntar es de personas curiosas.")],
    [
        E("En «El oso dormía en una cueva umbría», no sé qué es «umbría». ¿Qué palabra me detiene?", "umbría", "Es la palabra cuyo significado no conozco."),
        E("Ana no entendió «precioso» en una frase. ¿Qué debe hacer primero: seguir sin pensar o detenerse en esa palabra?", "Detenerse en esa palabra", "Notar la palabra es el primer paso para averiguar su significado."),
        E("¿Es una falla decir «no sé qué significa esta palabra»?", "No, es una buena estrategia", "Preguntar ayuda a comprender mejor."),
    ],
    [
        E("¿Qué es una palabra desconocida?", "Una palabra que no sé qué significa", "Es una palabra que aún no conozco."),
        E("¿Por qué conviene notar que no entiendo una palabra?", "Porque si no la entiendo, puedo no comprender el mensaje", "Una palabra clave sin entender deja la idea incompleta."),
        E("¿Cuál muestra que me detuve en una palabra: «Seguí leyendo igual» o «Paré y dije: esta no la entiendo»?", "Paré y dije: esta no la entiendo", "Detenerse es notar el problema."),
    ],
    [
        E("Dime la palabra más difícil y menos usada entre «tío», «llegó», «exhausto» y «correr».", "exhausto", "Las otras tres son palabras muy comunes."),
        E("Escribe la frase que diría Pedro para pedir ayuda con la palabra «cristalino».", "Por ejemplo: ¿Qué significa «cristalino»?", "La frase nombra la palabra y pide su significado."),
        E("Escribe una palabra que puede ser nueva en «El zorro avanzó con cautela entre los arbustos».", "cautela o arbustos", "Ambas son poco comunes para un niño de 6 años."),
    ],
    [
        E("Luis leyó «El mago tenía una capa raída» y dijo «ya entendí todo», pero no entendió «raída». ¿Qué le puede pasar?", "Puede imaginar mal cómo era la capa", "Sin saber «raída» no sabe si la capa era nueva o vieja."),
        E("Eva se detiene en «raída» y Mía la salta. ¿Quién usa una mejor estrategia?", "Eva", "Eva nota la palabra y puede averiguarla."),
    ],
    [
        E("Una frase tiene 6 palabras y no entiendes 1. ¿Cuántas sí entiendes?", "5", "Entiendes casi todas; solo debes averiguar una palabra."),
        E("Lee: «La profesora estaba complacida con el trabajo.» ¿Qué palabra tiene más probabilidad de ser desconocida: «profesora» o «complacida»?", "complacida", "«Profesora» es muy común en la escuela."),
    ],
    [E("La profesora dice: «Hoy haremos una actividad colaborativa». Tomás no sabe qué significa «colaborativa». ¿Qué puede hacer?", "Levantar la mano y preguntar qué significa «colaborativa»", "Preguntar en el momento ayuda a seguir la clase.")],
    [
        E("Si no entiendo una palabra, ¿pienso que soy malo para leer?", "No", "A todas las personas les pasa."),
        E("En «El río era muy caudaloso», ¿cuál podría ser la palabra desconocida?", "caudaloso", "Es la menos común de la frase."),
        E("¿Qué hago primero cuando noto una palabra que no conozco?", "Me detengo y la marco", "Notarla permite averiguarla después."),
    ],
    ("Lee estas tres frases. Para cada una, escribe la palabra que podrías no conocer y la frase que dirías para pedir ayuda. Frase 1: «El pirata encontró un cofre oculto en la arena.» Frase 2: «La profesora estaba complacida con el trabajo.» Frase 3: «El río era muy caudaloso en primavera.»",
     "Frase 1: oculto. Pido ayuda: ¿Qué significa «oculto»? Frase 2: complacida. ¿Qué significa «complacida»? Frase 3: caudaloso. ¿Qué significa «caudaloso»?",
     ["escribe una palabra para cada frase", "escribe una pregunta que nombra la palabra", "no se avergüenza de preguntar"], ["hoja con tres palabras y tres preguntas"], ["escribir una frase entera en vez de la palabra", "preguntas que no nombran la palabra"],
     "Si la palabra elegida es común, di: «Buena idea; ahora busca otra que sí sea difícil» y pide que la lea de nuevo."),
    "Lee en voz alta «El gato caminó sigiloso» a un adulto y dile qué palabra te frena.",
    "Escucha una conversación de adultos y anota una palabra que no conozcas.",
)

reg(
    OA19, 2,
    "Los textos de este cuaderno, lápiz y hoja. Un adulto lee en voz alta las frases si lo necesitas.",
    "Aprenderé a usar las otras palabras de la frase como pistas para adivinar qué significa una palabra nueva. Sirve para entender sin esperar ayuda.",
    ["Sé detectar una palabra que no conozco.", "Sé leer o escuchar frases de dos oraciones."],
    [
        "Las palabras de una frase se ayudan unas a otras. Cuando no conoces una palabra, mira las que están antes y después. Esas palabras se llaman contexto y entregan pistas. Con ellas puedes formar una idea de lo que significa. Esa idea es «mi idea» y después hay que comprobarla.",
        "Mira este ejemplo: «El perro estaba famélico: no había comido en todo el día y se comió su plato rapidito». Si no sabes «famélico», las pistas son «no había comido en todo el día» y «se comió su plato rapidito». Entonces famélico debe significar con mucha hambre.",
        "Tu idea puede estar equivocada, por eso después hay que comprobarla. Pero buscar pistas es una buena manera de empezar. Primero marca la palabra, luego busca dos pistas y por último di: «Creo que significa…».",
    ],
    [("contexto", "las palabras que rodean a otra palabra"), ("pista", "una señal que ayuda a descubrir algo"), ("mi idea", "lo que creo que significa, antes de comprobar"), ("famélico", "con mucha hambre"), ("comprobar", "revisar si mi idea es correcta")],
    [
        ("Encontrar dos pistas", "«Mi abuelo es muy longevo: ya tiene 95 años y ha vivido mucho.» ¿Qué creo que significa «longevo»?", ["Marco «longevo».", "Pista 1: tiene 95 años. Pista 2: ha vivido mucho.", "Mi idea: longevo es una persona que vive muchos años."], "Longevo significa que vive muchos años."),
        ("Pistas que apuntan a lo frío", "«La sopa estaba gélida; Ana sintió mucho frío al tomarla y la dejó.» ¿Qué creo que significa «gélida»?", ["Marco «gélida».", "Pista 1: sintió mucho frío. Pista 2: dejó la sopa.", "Mi idea: gélida es muy fría."], "Gélida significa muy fría."),
    ],
    [("Adivinar sin mirar las otras palabras.", "Se piensa que la palabra sola dice todo.", "Lee la frase completa y busca dos pistas."), ("Quedarse con la primera idea sin revisar.", "La primera idea puede no encajar.", "Prueba si tu idea tiene sentido en la frase.")],
    [
        E("«El perro estaba famélico: no había comido en todo el día.» ¿Qué pista dice que tenía hambre?", "No había comido en todo el día", "No comer explica el hambre."),
        E("En «La sopa estaba gélida; Ana sintió mucho frío», ¿cuál es una pista de «gélida»?", "Ana sintió mucho frío", "El frío se relaciona con una sopa fría."),
        E("Las palabras que rodean a otra palabra, ¿cómo se llaman?", "Contexto", "Rodean y ayudan a entender."),
    ],
    [
        E("¿Qué es «mi idea» sobre el significado de una palabra?", "Lo que creo que significa una palabra antes de comprobarlo", "Todavía hay que revisarla."),
        E("¿Para qué sirven las pistas del contexto?", "Para adivinar qué significa una palabra nueva", "Las palabras vecinas ayudan a comprender."),
        E("¿Cuántas pistas conviene buscar antes de decir mi idea?", "Dos o más", "Con varias pistas la idea es más segura."),
    ],
    [
        E("«Mi hermano es muy veloz: llega primero a todas las carreras.» ¿Qué creo que significa «veloz»?", "Muy rápido", "Llegar primero en carreras indica rapidez."),
        E("«El lago estaba sereno: no había olas ni viento.» ¿Qué creo que significa «sereno»?", "Tranquilo", "Sin olas ni viento todo está en calma."),
        E("«La caja era liviana; Rosa la levantó con un solo dedo.» ¿Qué creo que significa «liviana»?", "Que pesa poco", "Se levanta con un solo dedo."),
    ],
    [
        E("«El niño estaba exhausto: corrió una hora y se tiró al suelo respirando fuerte.» Marca las dos pistas.", "Corrió una hora; se tiró al suelo respirando fuerte", "Ambas indican mucho cansancio."),
        E("Beto dice que «exhausto» significa muy contento. ¿Encaja con las pistas de la frase anterior?", "No, porque las pistas dicen cansancio", "Correr una hora y respirar fuerte no muestran alegría."),
    ],
    [
        E("«Julia usó una linterna porque la bodega era muy lóbrega: no entraba ni un rayo de luz.» ¿Qué crees que significa «lóbrega»?", "Muy oscura", "No entra luz y se necesita linterna."),
        E("Elige la mejor idea para «El erizo es tímido: se esconde cuando alguien lo mira». Opciones: a) miedoso y callado, b) muy grande.", "a", "Esconderse indica vergüenza o miedo."),
    ],
    [E("Un cartel dice: «Cuidado, el piso está resbaloso porque lo acaban de encerar». Un niño no sabe «encerar». ¿Qué pista puede usar?", "La palabra «piso» y que está resbaloso", "Encerar tiene que ver con dejar el piso brillante y liso.")],
    [
        E("Si una palabra no la sé, ¿qué miro primero?", "Las palabras de alrededor", "Dan pistas del significado."),
        E("«El oso es fornido: tiene brazos grandes y mucha fuerza.» ¿Qué significa «fornido»?", "Fuerte", "Brazos grandes y fuerza son las pistas."),
        E("¿Mi idea siempre es correcta?", "No, hay que comprobarla", "Puede encajar o no en la frase."),
    ],
    ("Lee estas frases. Para cada una, escribe la palabra desconocida, dos pistas y qué crees que significa. Frase 1: «El abuelo estaba afónico: casi no le salía la voz y hablaba muy bajito.» Frase 2: «La torre era altísima y muy esbelta, delgada y larga como un lápiz.» Frase 3: «El payaso hizo una mueca graciosa y todos soltaron una carcajada.»",
     "Frase 1: afónico. Pistas: casi no le salía la voz; hablaba bajito. Creo que significa sin voz. Frase 2: esbelta. Pistas: delgada; larga como un lápiz. Creo que significa delgada y alta. Frase 3: carcajada. Pistas: todos soltaron; payaso gracioso. Creo que es una risa fuerte.",
     ["marca una palabra por frase", "escribe dos pistas distintas", "dice «creo que significa»"], ["hoja con tres columnas: palabra, pistas, idea"], ["dar una sola pista", "usar la palabra para explicarse a sí misma"],
     "Pide que busque otra pista en la frase y que la use para mejorar su idea."),
    "Escribe una frase propia con pistas para la palabra «veloz».",
    "Inventa una frase con pistas para la palabra «lóbrego» y pide a alguien que adivine.",
)

reg(
    OA19, 3,
    "El mini glosario de este cuaderno, lápiz y hoja. No se necesita diccionario real, pero si hay uno infantil en casa se puede usar.",
    "Aprenderé a elegir a quién o dónde preguntar cuando las pistas no bastan. Sirve para averiguar el significado de una palabra con seguridad.",
    ["Sé usar pistas del contexto.", "Sé el orden de las letras del abecedario."],
    [
        "A veces las pistas no alcanzan. Entonces puedes preguntar a una persona, como tu profesora, tu mamá, tu papá o un compañero, o consultar un diccionario. Un diccionario es un libro con palabras ordenadas como el abecedario, y al lado de cada una explica qué significa.",
        "Para preguntar bien, nombra la palabra y di en qué frase la oíste. Por ejemplo: «¿Qué significa tímido en la frase El erizo es tímido?». Así la otra persona te responde mejor. Dar las gracias después es parte de una buena pregunta.",
        "Para buscar en un diccionario, fíjate en la primera letra de la palabra. Las palabras con a van antes que las con b, y las con b antes que las con c. Ese orden se llama orden alfabético. Si hay muchas palabras con la misma letra, mira la segunda letra.",
    ],
    [("diccionario", "libro que explica el significado de las palabras"), ("glosario", "lista corta de palabras con su significado"), ("orden alfabético", "orden como el abecedario: a, b, c…"), ("consultar", "buscar información en un libro o preguntar a alguien"), ("fuente", "persona o libro donde encuentro información")],
    [
        ("Preguntar con una buena pregunta", "Ana no sabe «tímido» en la frase «El erizo es tímido». ¿Cómo puede preguntar?", ["Nombra la palabra.", "Dice en qué frase la oyó.", "Pide el significado con amabilidad."], "¿Qué significa «tímido» en la frase «El erizo es tímido»?"),
        ("Buscar en orden", "Dentro de un glosario con las palabras bote, árbol, casa y dedo, ¿cuál va primero?", ["Miro la primera letra de cada una: b, a, c, d.", "En el abecedario la a va primero."], "Árbol"),
    ],
    [("Buscar sin mirar el orden del abecedario.", "Se hojea al azar.", "Comienza con la primera letra de la palabra."), ("Preguntar solo «¿qué es eso?».", "Quien responde no sabe cuál palabra.", "Nombra la palabra y di la frase.")],
    [
        E("¿Qué letra va primero en el abecedario: b o c?", "b", "La b está antes que la c."),
        E("Ana oyó «tímido». ¿Qué dice para preguntar mejor: «¿Qué es eso?» o «¿Qué significa tímido?»", "¿Qué significa tímido?", "Nombra la palabra concreta."),
        E("¿Cuántas palabras hay en el glosario: sol, luna, mar?", "3", "Hay una palabra en cada nombre."),
    ],
    [
        E("¿Qué es un diccionario?", "Un libro que explica el significado de las palabras", "Tiene las palabras ordenadas y su explicación."),
        E("¿Por qué conviene decir la frase donde oí la palabra?", "Porque ayuda a quien me responde", "El significado puede cambiar según la frase."),
        E("Menciona una persona a quien puedo preguntar en el curso por una palabra.", "Por ejemplo: la profesora o un compañero", "Ambos pueden ayudarme."),
    ],
    [
        E("Ordena según el abecedario: dado, gato, ave, foco.", "ave, dado, foco, gato", "a, d, f, g es el orden."),
        E("En el glosario aparece: «mullido: blando y suave». ¿Qué significa mullido?", "Blando y suave", "Es lo que dice la definición."),
        E("¿Con qué letra empiezo a buscar «ágil» en un diccionario?", "a", "La primera letra de «ágil» es la a."),
    ],
    [
        E("Mini glosario: «sigiloso: que no hace ruido»; «ágil: que se mueve con rapidez y facilidad». Pedro leyó «El gato sigiloso saltó» y no sabe «sigiloso». ¿Qué significa?", "Que no hace ruido", "Se busca la palabra en el glosario."),
        E("Mini glosario: «tenaz: que no se rinde»; «torpe: que se mueve con poca habilidad». La frase dice «Rosa fue tenaz y no se rindió». ¿Qué palabra buscó?", "tenaz", "Es la palabra que explica «no se rindió»."),
    ],
    [
        E("Una niña no encuentra «bote» entre árbol, casa y dedo. ¿Por qué no está en la lista?", "Porque la lista no incluye esa palabra", "Esa lista tiene árbol, casa y dedo."),
        E("¿Qué debo hacer si no hay ni diccionario ni adulto cerca? Opciones: a) preguntar a un compañero, b) dejar de leer para siempre.", "a", "Una persona puede ayudar."),
    ],
    [E("En el recreo, Luz escucha «Qué inmenso es el patio» y no sabe «inmenso». ¿Cómo pregunta con cortesía a su profesora?", "Por ejemplo: Profesora, ¿qué significa inmenso en Qué inmenso es el patio?", "Nombra la palabra y la frase, con cortesía.")],
    [
        E("¿Qué es un glosario?", "Una lista corta de palabras con su significado", "Se parece a un diccionario más pequeño."),
        E("¿Qué palabra va primero en el diccionario: perro o gato?", "gato", "La g va antes que la p."),
        E("Después de recibir ayuda, ¿qué digo?", "Gracias", "Agradecer es parte de una buena pregunta."),
    ],
    ("Usa este mini glosario: «tenaz: que no se rinde»; «cauteloso: que avanza con cuidado»; «diminuto: muy pequeño». Escribe dos preguntas distintas, una para «diminuto» y otra para «cauteloso», nombrando la palabra y diciendo la frase donde la oíste, y responde cada una con el glosario. Frases: «El caracol es diminuto» y «El gato fue cauteloso en el techo».",
     "Pregunta 1: ¿Qué significa diminuto en El caracol es diminuto? Respuesta: muy pequeño. Pregunta 2: ¿Qué significa cauteloso en El gato fue cauteloso en el techo? Respuesta: que avanza con cuidado.",
     ["nombra la palabra", "dice la frase", "responde con la definición del glosario"], ["dos preguntas con sus respuestas"], ["preguntar «qué es esto»", "copiar la definición equivocada"],
     "Haz que repita la pregunta y la compare con la del ejemplo; si le falta la frase, pídele que la agregue."),
    "Ordena en tu hoja estas palabras en orden alfabético: mesa, árbol, zapato, dedo.",
    "Averigua con un adulto el significado de una palabra nueva de tu casa y escribe qué fuente usaste.",
)

reg(
    OA19, 4,
    "La ficha de palabras de este cuaderno, hoja, lápiz y colores. Se pueden escribir tarjetas con papel recortado.",
    "Aprenderé a comprobar si mi idea de una palabra funciona y a guardarla en una tarjeta. Sirve para recordarla y usarla después.",
    ["Sé buscar pistas.", "Sé preguntar o consultar el significado."],
    [
        "Cuando ya tienes una idea del significado, hay que comprobarla. Una manera sencilla es cambiar la palabra desconocida por el significado y releer la frase. Si la frase sigue teniendo sentido, tu idea funciona. Si suena extraña, vuelve a buscar pistas.",
        "Por ejemplo, en «El gato caminó sigiloso», cambio sigiloso por sin hacer ruido y queda «El gato caminó sin hacer ruido». Tiene sentido, entonces la idea es correcta. Si hubiera puesto «haciendo mucho ruido», no cuadraría con «Nadie lo escuchó».",
        "Después de comprobar, guarda la palabra en una tarjeta con la palabra, su significado y una frase tuya. Léela dos o tres días seguidos y úsala cuando hables. Así deja de ser desconocida y pasa a ser una palabra que ya sabes.",
    ],
    [("comprobar", "revisar si mi idea funciona"), ("reemplazar", "cambiar una palabra por otra"), ("tarjeta de palabra", "papel con la palabra, su significado y una frase"), ("usar", "decir o escribir la palabra cuando hace falta"), ("tiene sentido", "la frase se entiende bien")],
    [
        ("Reemplazar para comprobar", "Frase: «La mochila es liviana.» Mi idea: liviana significa «que pesa poco». ¿Funciona?", ["Reemplazo: «La mochila pesa poco».", "Releo la frase.", "Tiene sentido."], "Sí, la idea funciona."),
        ("Una idea que no funciona", "Frase: «La sopa estaba gélida y Ana sintió frío.» Mi idea: gélida significa caliente. ¿Funciona?", ["Reemplazo: «La sopa estaba caliente y Ana sintió frío».", "No concuerda con el frío.", "Debo buscar otra pista."], "No funciona; gélida debe ser muy fría."),
    ],
    [("Guardar la palabra sin comprobar.", "Se cree que la primera idea es segura.", "Cambia la palabra por el significado y relee."), ("Escribir solo la palabra en la tarjeta.", "Más tarde no se recuerda el significado.", "Agrega significado y una frase propia.")],
    [
        E("En «El perro estaba famélico», reemplazo famélico por «con mucha hambre». ¿La frase tiene sentido?", "Sí", "Un perro puede tener mucha hambre."),
        E("Reemplazo «sereno» por «tranquilo» en «El lago estaba sereno». ¿Tiene sentido?", "Sí", "Un lago puede estar tranquilo."),
        E("¿Cuántas partes lleva una tarjeta de palabra: palabra, significado y frase?", "3", "Son tres partes."),
    ],
    [
        E("¿Qué hago para comprobar mi idea?", "Cambio la palabra por el significado y releo la frase", "Así veo si la frase sigue teniendo sentido."),
        E("¿Qué hago si la frase no tiene sentido al reemplazar?", "Busco nuevas pistas o pregunto", "Mi idea de significado puede estar equivocada."),
        E("¿Por qué conviene escribir una frase propia en la tarjeta?", "Para recordar cómo se usa la palabra", "Una frase muestra el uso real."),
    ],
    [
        E("Reemplaza: «La torre era esbelta» con «delgada y alta». Escribe cómo queda.", "La torre era delgada y alta", "Se cambia una palabra por su significado."),
        E("Escribe una tarjeta para «veloz»: palabra, significado y una frase.", "Por ejemplo: veloz, muy rápido; El tren es veloz.", "Lleva las tres partes."),
        E("Una tarjeta dice: «cautela: cuidado para no tener problemas». Completa la frase: «El gato caminó con ___ por el techo».", "cautela", "Caminar con cuidado cuadra con el significado."),
    ],
    [
        E("Mía cree que «raída» significa nueva. En «La capa raída tenía agujeros», ¿funciona su idea?", "No", "Una capa con agujeros no es nueva."),
        E("Beto dice que «inmenso» es pequeño. En «El océano es inmenso, no se ve la orilla», ¿acertó?", "No, inmenso significa muy grande", "No ver la orilla indica tamaño enorme."),
    ],
    [
        E("¿Qué significa «obediente» si Sol dice: «Mi perro es obediente: siempre hace lo que le pido»? Escribe una tarjeta con tu idea.", "Por ejemplo: obediente, que hace caso; Mi perro es obediente.", "La pista es «hace lo que le pido»."),
        E("Carla escribió una tarjeta con solo la palabra «cautela». ¿Qué le falta?", "El significado y una frase", "Sin esos datos no recuerda qué significa."),
    ],
    [E("Tomás aprendió «generoso». Su abuela le pidió que usara la palabra en una frase. ¿Qué frase puede decir?", "Por ejemplo: Mi tío es generoso porque comparte su almuerzo.", "Usar la palabra en una frase muestra que la entiende.")],
    [
        E("¿Cuáles son las tres partes de una tarjeta de palabra?", "Palabra, significado y frase", "Son sus tres partes."),
        E("Si mi idea no calza en la frase, ¿la guardo igual?", "No", "Primero debo corregirla."),
        E("¿Cuántas veces conviene leer la tarjeta: una sola vez o varios días?", "Varios días", "Repasar ayuda a recordar."),
    ],
    ("Escribe una tarjeta de palabra para cada palabra: «diminuto» (muy pequeño), «cauteloso» (que avanza con cuidado) y «tenaz» (que no se rinde). Cada tarjeta lleva la palabra, su significado y una frase tuya; comprueba reemplazando la palabra por el significado y releyendo.",
     "diminuto: muy pequeño. Frase: El caracol es diminuto. Compruebo: El caracol es muy pequeño. cauteloso: que avanza con cuidado. Frase: El gato es cauteloso. Compruebo: El gato avanza con cuidado. tenaz: que no se rinde. Frase: Rosa fue tenaz. Compruebo: Rosa no se rindió.",
     ["tres tarjetas con palabra, significado y frase", "comprueba reemplazando", "la frase tiene sentido"], ["tres tarjetas escritas"], ["frase que no usa la palabra", "significado equivocado"],
     "Si la frase no tiene sentido, pide que reemplace la palabra por el significado y vuelva a leer."),
    "Usa una de tus tarjetas en una conversación de hoy y cuenta cuándo la dijiste.",
    "Haz un mini glosario de cinco palabras nuevas con dibujo para cada una.",
)

# ================================================================ OA 20
reg(
    OA20, 1,
    "Las pautas de este cuaderno, lápiz y hoja. Para practicar se puede usar una silla del hogar como butaca imaginaria.",
    "Aprenderé cómo ser un buen público en una obra de teatro. Sirve para disfrutar la obra y respetar a los actores.",
    ["Sé que en el teatro las personas representan una historia.", "Sé escuchar en silencio por un rato."],
    [
        "El teatro es un arte en el que personas llamadas actores representan una historia frente a otras personas, que son el público. Los actores están en el escenario y el público mira desde las butacas, que son los asientos. Para que todos disfruten, el público también tiene tareas importantes.",
        "El buen público llega a tiempo, apaga o guarda el celular, escucha en silencio y mira con atención. Si algo es gracioso, puede reír; si la historia es triste, puede quedarse callado. Al final, aplaude para agradecer el trabajo de los actores.",
        "Hay cosas que no se hacen durante la obra: hablar fuerte, correr, gritar, comer haciendo ruido o pararse sin necesidad. Los actores te escuchan y se distraen. Si necesitas decir algo muy importante, hazlo en voz baja a un adulto.",
    ],
    [("teatro", "arte donde actores representan una historia"), ("actor", "persona que representa un personaje"), ("público", "personas que miran la obra"), ("escenario", "lugar donde actúan los actores"), ("aplaudir", "juntar las manos para agradecer")],
    [
        ("Una acción del buen público", "Durante la obra, Ana mira el escenario y escucha sin hablar. ¿Es un buen público?", ["Mira al escenario.", "Escucha sin molestar.", "Eso ayuda a que todos disfruten."], "Sí, Ana es un buen público."),
        ("Una acción que molesta", "Durante la obra, Beto habla fuerte con su amigo. ¿Qué debe hacer?", ["Los actores y los otros niños no escuchan.", "Beto debe quedarse en silencio.", "Si necesita decir algo, lo dice muy bajito al adulto."], "Beto debe callar o hablar bajito al adulto."),
    ],
    [("Hablar con el compañero mientras actúan.", "Se cree que no pasa nada.", "Espera al final para comentar."), ("No aplaudir al final.", "No se sabe que el aplauso agradece.", "Aplaude cuando la obra termina.")],
    [
        E("¿Dónde actúan los actores: en el escenario o en la butaca?", "En el escenario", "La butaca es donde se sienta el público."),
        E("Durante la obra, ¿hablo fuerte con mi compañero?", "No", "Se distrae a los actores y a los demás."),
        E("Al final de la obra, ¿qué hace el público?", "Aplaude", "Agradece el trabajo de los actores."),
    ],
    [
        E("¿Quiénes forman el público?", "Las personas que miran la obra", "No actúan; miran y escuchan."),
        E("¿Por qué se guarda el celular durante la obra?", "Para no hacer ruido ni distraer", "Las luces y los sonidos molestan."),
        E("¿Para qué sirve el aplauso?", "Para agradecer a los actores", "Muestra que valoramos su trabajo."),
    ],
    [
        E("Escribe dos cosas que haces para ser un buen público.", "Por ejemplo: escucho en silencio y miro atentamente.", "Ambas ayudan a todos a disfrutar."),
        E("¿Cómo se llama el asiento donde se sienta una persona del público en el teatro?", "Butaca", "Es el asiento de la sala."),
        E("Escribe una frase para decirle a un compañero que está hablando durante la obra, con respeto.", "Por ejemplo: Hablemos al final, por favor.", "Pide silencio con cortesía."),
    ],
    [
        E("Luz dice: «Si la obra no me gusta, me paro y salgo corriendo». ¿Es lo mejor?", "No", "Se interrumpe a los actores; puede esperar y decirlo al final."),
        E("Mateo se ríe en una parte graciosa de la obra. ¿Es adecuado?", "Sí", "Reír cuando algo es gracioso es parte del teatro."),
    ],
    [
        E("Ordena estas acciones para ir al teatro: a) aplaudo, b) llego a tiempo, c) escucho en silencio. Escribe las letras en orden.", "b, c, a", "Primero llego, después escucho y al final aplaudo."),
        E("En una obra sobre un oso triste, un niño grita «¡Chao!». ¿Qué problema crea?", "Rompe el silencio y distrae a los actores", "Un grito corta la historia."),
    ],
    [E("Vas a ver una obra con tu curso. Dos amigos conversan durante la función. ¿Qué haces tú?", "Miro la obra y les hago una seña de silencio", "Cuidar el silencio ayuda a todos.")],
    [
        E("¿Qué hago con mi celular durante una obra?", "Lo guardo o lo apago", "Evita ruidos y luces."),
        E("¿Qué hace el actor en el escenario?", "Representa un personaje", "Eso es actuar."),
        E("¿Puedo reír si algo es gracioso en la obra?", "Sí", "Reír con respeto es parte de ser público."),
    ],
    ("Lee esta pauta de buen público y dibuja o escribe tres acciones: 1) llegar a tiempo, 2) escuchar en silencio, 3) aplaudir al final. Luego practica con un adulto en casa: cuando el adulto cuente una historia de tres frases, tú escuchas sin hablar y aplaudes al terminar.",
     "Dibujé: 1) un niño llegando con reloj; 2) un niño con el dedo en la boca en silencio; 3) manos aplaudiendo. Practiqué con mi mamá: escuché sin hablar y aplaudí.",
     ["tres acciones del buen público", "practica escuchando en silencio", "aplaude al final"], ["dibujo o escrito de tres acciones", "adulto observa el silencio"], ["hablar mientras el adulto cuenta", "no aplaudir"],
     "Si habló, repite la práctica con una historia más corta y pide que cuente cuántas veces se acordó de callar."),
    "Dibuja una butaca y escribe una frase que diga cómo te sentarás en el teatro.",
    "Inventa una regla más para un buen público y explica por qué ayuda.",
)

reg(
    OA20, 2,
    "El libreto breve de este cuaderno, un espacio libre en casa y objetos cotidianos como un cojín o una bufanda.",
    "Aprenderé a mostrar cómo es un personaje usando el cuerpo y la voz. Sirve para actuar y para entender mejor los cuentos.",
    ["Sé que un personaje es quien participa en una historia.", "Sé hablar fuerte y bajito."],
    [
        "Cuando un actor representa a un personaje, no solo dice sus palabras. También usa el cuerpo, la cara y la voz para mostrar cómo es. Un gigante camina con pasos grandes y lentos, y habla con voz grave. Un ratón camina con pasitos rápidos y habla con voz aguda.",
        "El cuerpo cuenta cómo se siente el personaje. Si está feliz, sonríe y se mueve liviano. Si está enojado, aprieta las manos y junta las cejas (se dice «frunce el ceño»). Si tiene miedo, se encoge y mira para todos lados. La voz también cambia: fuerte, suave, rápida o lenta.",
        "Para construir un personaje, piensa tres cosas: quién es, cómo se mueve y cómo habla. Después ensaya frente a un adulto y pregúntale: ¿se nota que soy un gigante? Si no se nota, cambia el tamaño de los pasos o la voz. El libreto es el texto con lo que dice cada personaje.",
    ],
    [("personaje", "quien vive la historia"), ("gesto", "movimiento de la cara o las manos"), ("voz grave", "voz baja y gruesa"), ("voz aguda", "voz alta y delgada"), ("ensayar", "practicar antes de actuar")],
    [
        ("Un gigante", "¿Cómo se mueve y habla un gigante que llega a un pueblo?", ["Pasos grandes y lentos.", "Brazos extendidos.", "Voz grave y fuerte."], "Se mueve con pasos grandes y habla con voz grave."),
        ("Un ratón asustado", "¿Cómo se mueve y habla un ratón asustado?", ["Pasitos rápidos y cuerpo encogido.", "Mira para todos lados.", "Voz aguda y suave."], "Se mueve con pasitos y habla con voz aguda y suave."),
    ],
    [("Actuar solo con las palabras.", "Se cree que basta con decir el texto.", "Agrega gestos, pasos y voz."), ("Usar la misma voz para todos los personajes.", "No se piensa cómo es cada uno.", "Cambia la voz según el personaje.")],
    [
        E("Un gigante camina: ¿con pasos grandes o pasitos cortos?", "Pasos grandes", "El gigante es muy alto."),
        E("Un ratón habla: ¿voz grave o voz aguda?", "Voz aguda", "Los ratones son pequeños y su voz es delgada."),
        E("Un personaje con miedo, ¿se estira o se encoge?", "Se encoge", "Con miedo el cuerpo se hace pequeño."),
    ],
    [
        E("¿Qué parte del cuerpo ayuda a mostrar el enojo: el ceño fruncido o los brazos relajados?", "El ceño fruncido", "La cara muestra el enojo."),
        E("¿Por qué un actor cambia la voz?", "Para mostrar cómo es el personaje", "La voz comunica quién es."),
        E("En Lenguaje, ¿qué es ensayar?", "Practicar antes de actuar", "Ensayar mejora la actuación."),
    ],
    [
        E("Libreto: Gigante: «¡Hola, pueblo!». Escribe cómo caminarías y hablarías para este gigante.", "Por ejemplo: pasos grandes y voz grave", "Cuerpo y voz muestran su tamaño."),
        E("Libreto: Ratón: «¡Cuidado con el gato!». Escribe cómo moverías las manos y la voz.", "Por ejemplo: manos temblorosas y voz aguda rápida", "Muestran susto y pequeño tamaño."),
        E("Libreto: Reina: «Pasen todos al salón». Describe un gesto y una voz para una reina elegante.", "Por ejemplo: espalda recta, paso lento y voz clara", "Muestran que la reina es elegante."),
    ],
    [
        E("Dos niñas actúan de abuelito: Ana camina rápido con voz de bebé. Luz camina lento con la espalda curva y voz temblorosa. ¿Quién muestra mejor al abuelito?", "Luz", "Camina lento y encorvado, como una persona mayor."),
        E("Beto hace de león y habla en susurro con pasitos de ratón. ¿Se nota que es león?", "No", "El león suele mostrarse fuerte y de voz grave."),
    ],
    [
        E("¿Cuántos personajes hay en el libreto: Gigante, Ratón y Reina?", "3", "Se cuentan Gigante, Ratón y Reina."),
        E("Libreto: Ratón: «No me comas, por favor». ¿Qué voz es mejor: fuerte y grave o baja y rápida?", "Baja y rápida", "El ratón está asustado."),
    ],
    [E("En la obra escolar te toca ser un pájaro que acaba de despertar. ¿Qué puedes hacer con el cuerpo y la voz?", "Por ejemplo: mover los brazos como alas y hacer un sonido suave", "Cuerpo y voz muestran el personaje.")],
    [
        E("¿Qué tres cosas pienso al construir un personaje?", "Quién es, cómo se mueve y cómo habla", "Son las claves para actuar."),
        E("Un personaje enojado, ¿sonríe o frunce el ceño?", "Frunce el ceño", "Es un gesto de enojo."),
        E("Un personaje que duerme, ¿habla fuerte o respira lento?", "Respira lento", "Un cuerpo dormido está tranquilo."),
    ],
    ("Escoge uno de estos personajes: gigante, ratón, reina o pájaro. Frente a un adulto, di tu frase con cuerpo y voz. Frases: Gigante: «¡Hola, pueblo!». Ratón: «¡Cuidado con el gato!». Reina: «Pasen todos al salón». Pájaro: «¡Ya amaneció!». Pide al adulto que diga cómo se mueve y habla tu personaje.",
     "Fui ratón: caminé con pasitos, encogí el cuerpo y dije «¡Cuidado con el gato!» con voz aguda y rápida. Mi mamá dijo: se nota que eres un ratón asustado.",
     ["usa el cuerpo", "usa la voz", "el adulto reconoce el personaje"], ["adulto observa y dice qué personaje fue"], ["decir la frase sin moverse", "usar la voz normal"],
     "Muestra una nueva forma de caminar y repite hasta que el adulto reconozca el personaje."),
    "Repite la actuación frente a un espejo y mira qué haces con las manos.",
    "Representa el mismo personaje enojado y luego contento; explica qué cambia.",
)

reg(
    OA20, 3,
    "El texto breve de la escena, objetos del hogar (silla, tela, cojín) y espacio libre. Las ideas están escritas en el cuaderno.",
    "Aprenderé que el teatro usa espacio, objetos y sonidos para contar. Sirve para crear escenas sin necesidad de muchos materiales.",
    ["Sé representar un personaje con cuerpo y voz.", "Sé reconocer sonidos del hogar."],
    [
        "En el teatro, el escenario no es solo un piso: puede ser un bosque, una casa o la luna. Los actores usan objetos, llamados utilería, para ayudar a contar la historia. Una silla puede ser un trono, y una tela azul puede ser un río.",
        "También se usan sonidos. Golpear suavemente una mesa puede imitar pasos; una cuchara contra una taza puede ser una campana. Los sonidos ayudan al público a imaginar lo que no se ve. Si el sonido es muy fuerte, se tapan las voces, por eso se cuida el volumen.",
        "Para planear una escena, escribe tres cosas: dónde pasa, qué objetos usan y qué sonidos hay. Por ejemplo: pasa en un bosque, usan una tela verde y un palo, y se escucha el viento con la voz.",
    ],
    [("escenario", "lugar donde pasa la escena"), ("utilería", "objetos que usan los actores"), ("sonido", "lo que se escucha en la obra"), ("imaginar", "ver con la mente lo que no está"), ("volumen", "qué tan fuerte o suave suena algo")],
    [
        ("Convertir un objeto", "En la escena, una tela azul se extiende en el piso. ¿Qué puede ser?", ["La tela es larga y azul.", "El azul parece agua.", "Puede ser un río."], "La tela puede ser un río."),
        ("Elegir un sonido", "Para mostrar pasos en un bosque, ¿qué sonido sirve: golpes suaves en una mesa o un grito?", ["Los pasos suenan toc, toc.", "El grito asusta y no parece paso.", "Los golpes suaves imitan pasos."], "Golpes suaves en una mesa."),
    ],
    [("Creer que el teatro necesita objetos caros.", "No se imagina con lo que hay.", "Usa objetos del hogar de otra manera."), ("Poner sonidos muy fuertes.", "No se escuchan las voces.", "Cuida el volumen para que se oigan los actores.")],
    [
        E("Una silla puede representar un trono. ¿Verdadero o falso?", "Verdadero", "En teatro los objetos pueden representar otras cosas."),
        E("La utilería, ¿son los objetos o las luces de la sala?", "Los objetos que usan los actores", "Utilería significa objetos de la escena."),
        E("Golpear suavemente una mesa, ¿puede imitar pasos?", "Sí", "El sonido recuerda unos pasos."),
    ],
    [
        E("¿Para qué sirven los sonidos en una obra?", "Para ayudar al público a imaginar lo que no se ve", "El sonido completa la historia."),
        E("¿Por qué se cuida el volumen de un sonido?", "Para que se oigan las voces de los actores", "Un sonido muy fuerte tapa el diálogo."),
        E("¿Qué tres cosas escribo para planear una escena?", "Dónde pasa, qué objetos hay y qué sonidos hay", "Esas ideas organizan la escena."),
    ],
    [
        E("Escena: «Una niña cruza un río». Tienes una tela azul. ¿Cómo la usarías?", "La extendería en el piso para que la niña pase por encima", "La tela representa el río."),
        E("Escena: «Una tormenta». Tienes una bandeja de plástico. ¿Qué sonido harías?", "Golpearía la bandeja suavemente con los dedos como lluvia", "Los golpecitos imitan gotas."),
        E("Escena: «Una cueva oscura». Tienes una manta. Escribe cómo la usarías.", "Me cubro con la manta para formar una cueva", "La manta cubre y simula oscuridad."),
    ],
    [
        E("Mía usa una silla como si fuera un auto. ¿Se entiende?", "Sí, si dice o muestra que maneja", "El público puede imaginarlo."),
        E("En un bosque, Luis hace sonar una campana muy fuerte todo el rato. ¿Ayuda a la escena?", "No, porque tapa las voces", "El volumen alto molesta."),
    ],
    [
        E("Escena: bosque. Objetos: tela verde y palo. Sonido: viento con la voz. ¿Cuántos elementos hay en total (objetos + sonido)?", "3", "Tela, palo y viento suman tres."),
        E("Ana planea la escena de una playa. Escribe un objeto y un sonido.", "Por ejemplo: toalla azul y sonido de olas con la boca", "Ambos cuentan el lugar."),
    ],
    [E("Vas a presentar una escena de una cocina con un cuaderno, una cuchara y una taza. Escribe cómo usas la cuchara.", "Por ejemplo: la golpeo suave contra la taza como campana", "La cuchara se vuelve sonido.")],
    [
        E("¿Dónde pasa una escena con árboles y pájaros?", "En un bosque", "Los árboles y pájaros sugieren bosque."),
        E("¿Qué sonido imita la lluvia: golpes suaves rápidos con los dedos o un grito?", "Golpes suaves rápidos con los dedos", "Se parecen a gotas."),
        E("¿La utilería debe ser cara?", "No", "Con objetos simples se puede imaginar."),
    ],
    ("Planea esta escena con un adulto: «Un niño busca su balón en una cueva». Escribe: 1) dónde pasa, 2) dos objetos del hogar que usarás (por ejemplo, manta, linterna de papel, cojín, silla) y 3) dos sonidos (por ejemplo, pasos con golpes suaves, eco con la voz). Luego represéntala con tu adulto como público.",
     "1) En una cueva. 2) Objetos: una manta como techo y un cojín como piedra. 3) Sonidos: pasos con golpes suaves y eco de mi voz diciendo ¡Balón! Mi adulto entendió que era una cueva.",
     ["dice dónde ocurre", "usa dos objetos", "usa dos sonidos"], ["hoja con lugar, objetos y sonidos", "adulto observa la escena"], ["sonidos demasiado fuertes", "objetos sin explicar"],
     "Si el adulto no entiende el lugar, agrega un sonido que lo muestre."),
    "Convierte un objeto de tu casa en otro (una cuchara en micrófono) y muestra cómo.",
    "Cambia el lugar de la escena (de cueva a playa) y cambia un objeto y un sonido.",
)

reg(
    OA20, 4,
    "La mini obra breve de este cuaderno, lápiz y hoja. No se necesitan otros materiales.",
    "Aprenderé a conversar sobre una obra de teatro para contar qué entendí y qué opino. Sirve para pensar en la historia y escuchar a otros.",
    ["Sé qué es un personaje.", "Sé contar qué pasó en una historia."],
    [
        "Después de ver una obra, conversamos sobre ella. Podemos contar qué pasó, quiénes eran los personajes y qué sentimos. También podemos decir qué nos gustó y por qué. Dar una razón con «porque» hace que la opinión se entienda mejor.",
        "Una conversación tiene turnos: habla una persona y las demás escuchan. Si no entendiste algo, puedes preguntar. Si estás de acuerdo, puedes decir «yo también lo vi así». Si piensas diferente, puedes decir «yo pienso otra cosa» con respeto.",
        "Para recordar la obra, responde tres preguntas: ¿quiénes eran? ¿qué problema tuvieron? ¿cómo terminó? Con esas respuestas ya puedes contar la obra en pocas frases.",
    ],
    [("opinión", "lo que pienso o siento sobre algo"), ("porque", "palabra que da la razón"), ("problema", "lo que complica la historia"), ("final", "cómo termina la historia"), ("turno", "momento para hablar")],
    [
        ("Contar la obra", "Mini obra «El conejo y la zanahoria»: Un conejo tenía hambre. Una zanahoria estaba muy alta en un árbol. El conejo pidió ayuda a un pájaro y juntos la bajaron. ¿Quiénes eran, cuál fue el problema y cómo terminó?", ["Personajes: conejo y pájaro.", "Problema: la zanahoria estaba muy alta.", "Final: la bajaron juntos."], "Personajes: conejo y pájaro; problema: zanahoria alta; final: la bajaron juntos."),
        ("Dar una opinión con razón", "Opino sobre «El conejo y la zanahoria». ¿Qué puedo decir?", ["Digo qué me gustó.", "Agrego «porque».", "La razón viene de la obra."], "Me gustó porque el conejo pidió ayuda y la obtuvo."),
    ],
    [("Decir solo «me gustó» sin razón.", "Se cree que basta.", "Agrega «porque» y la razón."), ("Interrumpir al que habla.", "Hay apuro por opinar.", "Espera tu turno.")],
    [
        E("Mini obra: «Un conejo tenía hambre. La zanahoria estaba en un árbol alto. Un pájaro lo ayudó.» ¿Quién ayudó al conejo?", "Un pájaro", "El texto lo dice."),
        E("En la misma obra, ¿qué problema tenía el conejo?", "Tenía hambre y la zanahoria estaba alta", "Eso complica la historia."),
        E("Al hablar de una obra, ¿digo qué me gustó y por qué?", "Sí", "Dar razones aclara la opinión."),
    ],
    [
        E("¿Qué palabra uso para dar una razón?", "Porque", "Porque une la opinión con su razón."),
        E("¿Qué es el final de una obra?", "Cómo termina la historia", "Es la última parte."),
        E("Si no entendí una parte de la obra, ¿qué hago?", "Pregunto con respeto", "Preguntar ayuda a comprender."),
    ],
    [
        E("Obra: «Una niña perdió su gorro en el mercado. Un vendedor la ayudó a buscarlo y lo hallaron bajo una caja.» ¿Cómo terminó?", "Hallaron el gorro bajo una caja", "El texto dice dónde lo encontraron."),
        E("Escribe una frase de opinión con «porque» sobre la obra del gorro.", "Por ejemplo: Me gustó porque el vendedor ayudó a la niña.", "Lleva opinión y razón."),
        E("Mini obra: «Un gato y un perro peleaban por un hueso. Un niño partió el hueso en dos.» ¿Cuántas partes quedaron?", "2", "Partir en dos da dos partes."),
    ],
    [
        E("Beto dice: «No me gustó». Ana dice: «No me gustó porque era muy ruidosa». ¿Quién dio una razón?", "Ana", "Ana usó «porque» en su frase."),
        E("En la obra del conejo, ¿es verdad que el conejo resolvió solo el problema?", "No, un pájaro lo ayudó", "El texto lo dice."),
    ],
    [
        E("Una niña dice «el conejo no quiso la ayuda de nadie». El texto cuenta que pidió ayuda al pájaro y juntos bajaron la zanahoria. ¿La opinión coincide?", "No", "El conejo pidió ayuda y trabajó junto al pájaro."),
        E("Escribe una pregunta que podrías hacer al pájaro de la obra.", "Por ejemplo: ¿Por qué quisiste ayudar al conejo?", "Una pregunta abierta invita a pensar."),
    ],
    [E("Después de una función, tu amigo dice: «La obra de las abejas fue aburrida». Tú pensaste que fue buena. ¿Cómo puedes decirlo con respeto?", "Por ejemplo: Yo pienso otra cosa: me gustó porque las abejas cantaban", "Es una opinión distinta con razón.")],
    [
        E("¿Qué pregunto para recordar la obra?", "Quiénes eran, qué problema hubo y cómo terminó", "Son tres preguntas clave."),
        E("¿Dejo que otros hablen en su turno?", "Sí", "Así todos se escuchan."),
        E("Frase de opinión: «Me gustó el gato porque era ___». Completa con una razón posible.", "Por ejemplo: valiente", "La razón explica la opinión."),
    ],
    ("Lee la obra y conversa con un adulto. Obra «El gato y el hueso»: Un gato y un perro peleaban por un hueso. Un niño partió el hueso en dos y los dos comieron contentos. Responde en voz alta: quiénes eran, cuál era el problema, cómo terminó y qué te gustó, con «porque».",
     "Eran un gato, un perro y un niño. El problema era que peleaban por un hueso. Terminó cuando el niño lo partió en dos. Me gustó porque el niño solucionó el problema sin pelear.",
     ["responde las tres preguntas", "da una opinión con «porque»", "escucha al adulto"], ["adulto escucha y anota si usó «porque»"], ["decir solo «me gustó»", "interrumpir"],
     "Si falta «porque», pregunta: ¿por qué? y repite la frase con la razón."),
    "Cuenta en tres frases una obra o cuento que viste y di qué opinas.",
    "Escribe una pregunta para un personaje y respóndela tú como si fueras él.",
)

reg(
    OA20, 5,
    "La obra breve de este cuaderno, hoja, lápiz y objetos del hogar. El adulto puede ser el público.",
    "Aprenderé a cambiar una parte de una obra e inventar otra posibilidad. Sirve para usar mi creatividad y entender que una historia puede contarse de otra forma.",
    ["Sé contar una obra con inicio, problema y final.", "Sé actuar con cuerpo y voz."],
    [
        "Una obra puede cambiar si cambiamos una parte. Si el final es otro, la historia queda distinta. A eso se le llama recrear: inventar una versión nueva usando lo que ya sabemos de la obra. Los actores y los autores lo hacen mucho.",
        "Para recrear, escoge una sola cosa que cambiar: el final, el lugar o un personaje. Por ejemplo, en la obra del conejo y la zanahoria, el pájaro podría no querer ayudar. ¿Cómo cambia la obra? El conejo tendría que buscar otra solución. Después escribe en tres frases cómo queda.",
        "Antes de actuar la nueva versión, practica con tu cuerpo y tu voz. Pide a un adulto que sea el público. Al terminar, cuéntale qué cambiaste y por qué.",
    ],
    [("recrear", "inventar una versión nueva de una historia"), ("cambiar", "hacer algo distinto"), ("versión", "forma de contar una historia"), ("final", "cómo termina"), ("posibilidad", "algo que podría pasar")],
    [
        ("Cambiar el final", "Obra original: «Un conejo tenía hambre. Un pájaro bajó la zanahoria y comieron juntos.» Cambia el final: el pájaro no está. ¿Qué podría hacer el conejo?", ["Cambio una parte: el pájaro no está.", "Pienso una solución: el conejo busca una escalera.", "Escribo el nuevo final."], "El conejo busca una escalera y baja la zanahoria."),
        ("Cambiar el lugar", "Misma obra, pero ocurre en la playa. ¿Qué cambia?", ["La zanahoria cuelga de una palmera.", "El pájaro es una gaviota.", "Los sonidos son olas."], "La zanahoria está en una palmera y ayuda una gaviota."),
    ],
    [("Cambiar todo a la vez.", "Se pierde el hilo de la historia.", "Cambia una sola parte."), ("No decir qué se cambió.", "El público no sabe qué es nuevo.", "Cuéntalo al terminar.")],
    [
        E("Si cambio el final de una obra, ¿cambia la historia?", "Sí", "Un final distinto cambia lo que pasa al terminar."),
        E("Obra: el pájaro no está. ¿Quién resuelve el problema del conejo?", "El conejo", "Sin ayuda, el conejo debe actuar."),
        E("¿Cuántas cosas cambio al recrear: una o todas?", "Una", "Se recomienda cambiar una parte."),
    ],
    [
        E("¿Qué significa recrear una obra?", "Inventar una versión nueva usando la obra original", "Se parte de algo conocido."),
        E("¿Por qué conviene decir qué cambié?", "Para que el público entienda la nueva versión", "Sin explicar, puede confundirse."),
        E("Menciona dos partes de una obra que puedo cambiar.", "Por ejemplo: el final y el lugar", "Son partes que se pueden modificar."),
    ],
    [
        E("Obra: «Una niña va a la plaza y juega con un perro.» Cambia el lugar a una playa. Escribe cómo queda.", "Por ejemplo: Una niña va a la playa y juega con un perro.", "Se cambia solo el lugar."),
        E("Obra: «Un oso duerme en su cueva.» Cambia al personaje por un conejo. Escribe cómo queda.", "Un conejo duerme en su cueva", "Se cambia el personaje."),
        E("Obra original: el ratón gana la carrera. Escribe un final distinto.", "Por ejemplo: el ratón y la tortuga llegan juntos", "El final es nuevo."),
    ],
    [
        E("Beto cambia el lugar, los personajes y el final de una vez. ¿Es fácil de seguir?", "No", "Hay que cambiar una cosa a la vez."),
        E("Carla recrea la obra y dice «Cambié el final». ¿Hizo bien en decirlo?", "Sí", "Explicar lo nuevo ayuda al público."),
    ],
    [
        E("Obra original: «Un niño pierde su globo; lo busca y lo encuentra en un árbol». ¿Cuál final es igual al original: a) lo encuentra en un árbol, b) se lo lleva el viento?", "a", "El final original dice que lo encuentra en un árbol."),
        E("¿Cuántas frases tiene tu nueva versión si escribes 1 por inicio, 1 por problema y 1 por final?", "3", "Son tres frases."),
    ],
    [E("Tu curso hará una obra sobre un pez que no encuentra su casa. Propón un final nuevo.", "Por ejemplo: el pez encuentra una casa nueva con un amigo", "Es una posibilidad nueva coherente con la historia.")],
    [
        E("Al recrear, ¿parto de una historia conocida?", "Sí", "Se transforma lo que ya existe."),
        E("¿Un final nuevo tiene que tener sentido con el principio?", "Sí", "Si no, la historia queda desordenada."),
        E("Después de actuar la nueva versión, ¿qué cuento al público?", "Qué parte cambié", "Eso aclara la novedad."),
    ],
    ("Obra original «El pez que busca su casa»: Un pez salió a nadar y se perdió. Un cangrejo lo vio y le mostró el camino de vuelta. Cambia una parte: el cangrejo no está. Escribe en tres frases cómo sigue la historia y actúala con un adulto de público. Al final cuéntale qué cambiaste.",
     "Un pez salió a nadar y se perdió. Una tortuga lo vio y lo llevó a casa. Cambié al cangrejo por una tortuga. Actué nadando con los brazos.",
     ["cambia una parte", "escribe tres frases", "cuenta qué cambió"], ["hoja con tres frases", "adulto observa la actuación"], ["cambiar todo", "no explicar el cambio"],
     "Pide que diga cuál fue la parte cambiada y por qué la cambió."),
    "Cambia el final del cuento que más te gusta y cuéntalo en tres frases.",
    "Escribe y actúa tres finales distintos para la misma obra y di cuál te gusta más.",
)

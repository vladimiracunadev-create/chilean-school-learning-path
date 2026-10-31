"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 30 (incorporar vocabulario nuevo en las intervenciones orales)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA30 = "LE06 OA 30"
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


# ================================================================ OA 30 · clase 1
T_NAT = ("«El naturalista caminó de manera sigilosa por el sendero. Era un hombre meticuloso: anotaba cada detalle de lo que veía. "
         "Aquella tarde descubrió un vestigio de un antiguo refugio, apenas unas piedras ordenadas en círculo. "
         "Las marcas del suelo fueron efímeras: la lluvia las borró en minutos.»")
reg(
    OA30, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: un diccionario y una persona de tu casa que lea los textos en voz alta.",
    "Aprenderé a encontrar palabras nuevas en un texto leído o escuchado y a deducir su significado usando las pistas del contexto. Sirve para ampliar mi vocabulario y poder usar esas palabras después al hablar.",
    ["Sé que las palabras tienen significado.", "Sé leer un texto breve y comprender de qué trata."],
    [
        "Cuando leemos o escuchamos un texto, a veces aparecen palabras que no conocemos. En lugar de ignorarlas, podemos deducir su significado con las pistas del contexto, que son las palabras y frases que rodean a la palabra nueva. Por ejemplo, en «Era un hombre meticuloso: anotaba cada detalle», la frase que sigue a los dos puntos explica que meticuloso es alguien cuidadoso con los detalles.",
        "Las pistas pueden ser una explicación después de dos puntos, un ejemplo, un sinónimo cercano o un contraste. En «Las marcas fueron efímeras: la lluvia las borró en minutos», la pista es la explicación: duraron poco tiempo. En «No era numeroso, sino escaso», el contraste con «numeroso» muestra que escaso significa poco. Cuando una pista no basta, se confirma con un diccionario.",
        "Para que una palabra nueva se vuelva tuya, conviene anotarla con su significado y una oración propia. Después, se usa al hablar. Una estrategia es: 1) subrayar la palabra, 2) leer la frase completa, 3) buscar la pista, 4) proponer un significado, 5) comprobarlo. Con esta rutina, ampliarás tu vocabulario sin interrumpir la lectura.",
    ],
    [("vocabulario", "conjunto de palabras que conocemos y usamos"), ("contexto", "palabras y frases que rodean a una palabra"), ("pista", "dato del texto que ayuda a entender algo"), ("deducir", "descubrir algo a partir de pistas"), ("diccionario", "libro o recurso con el significado de las palabras")],
    [
        ("Deducir por explicación", "«Era un hombre meticuloso: anotaba cada detalle de lo que veía.» ¿Qué significa meticuloso?", ["Busco la pista después de los dos puntos.", "Anota cada detalle: se fija en lo pequeño.", "Propongo: cuidadoso con los detalles."], "Cuidadoso con los detalles."),
        ("Deducir por contraste", "«El agua no era abundante, sino escasa.» ¿Qué significa escasa?", ["Veo el contraste «no… sino».", "Abundante significa mucho.", "Escasa es lo contrario: poca."], "Poca, que no alcanza."),
    ],
    [("Saltarse la palabra nueva.", "Se cree que no importa si se entiende lo demás.", "Subraya la palabra y busca la pista en la frase."), ("Inventar un significado sin pistas.", "Se adivina sin mirar el texto.", "Apoya tu idea en una pista y luego comprueba con el diccionario.")],
    [
        E("«El gato avanzó sigiloso hacia el pájaro, sin que sus patas hicieran ruido.» ¿Qué significa sigiloso: que actúa sin hacer ruido o que actúa con mucho ruido?", "Que actúa sin hacer ruido", "La pista dice que sus patas no hacían ruido."),
        E(f"{T_NAT} ¿Qué frase ayuda a entender «efímeras»: «la lluvia las borró en minutos» o «por el sendero»?", "La lluvia las borró en minutos", "Explica que duraron muy poco."),
        E(f"{T_NAT} Según la pista, ¿qué significa «efímeras»: de poca duración o permanentes?", "De poca duración", "Se borraron en pocos minutos."),
    ],
    [
        E(f"{T_NAT} En «un vestigio de un antiguo refugio, apenas unas piedras ordenadas», ¿qué significa vestigio: señal o resto de algo que existió, o un refugio nuevo?", "Señal o resto de algo que existió", "Solo quedaban algunas piedras de un refugio antiguo."),
        E("«El niño es cauteloso: antes de cruzar la calle mira a ambos lados». ¿Qué significa cauteloso: que actúa con precaución o que actúa sin pensar?", "Que actúa con precaución", "Mirar a ambos lados antes de cruzar muestra cuidado."),
        E("«Marta es afable: saluda con una sonrisa y trata bien a todos». ¿Qué significa afable: amable en el trato o apurada?", "Amable en el trato", "La explicación habla de buen trato."),
    ],
    [
        E("Ordena los pasos de la rutina: a) buscar la pista en la frase b) subrayar la palabra c) comprobar con el diccionario d) proponer un significado. Escribe las letras.", "b, a, d, c", "Se subraya, se busca la pista, se propone y se comprueba."),
        E("«Perseveró: aunque falló tres veces, no se rindió». ¿Qué significa perseveró: siguió intentando o abandonó?", "Siguió intentando", "La explicación dice que no se rindió."),
        E("En «Las provisiones eran escasas, pocas para tantas familias», ¿qué pista ayuda a entender «escasas»: «pocas para tantas familias» o «las provisiones»?", "Pocas para tantas familias", "Es la explicación del significado."),
    ],
    [
        E("Un estudiante dice: «Si no entiendo una palabra, tengo que parar de leer». ¿Es siempre necesario? Responde sí o no.", "No", "Primero se busca la pista del contexto y se sigue leyendo."),
        E("«El camino fue sinuoso: giraba y giraba entre los cerros.» ¿Qué significa sinuoso: con muchas curvas o recto?", "Con muchas curvas", "La explicación dice que giraba y giraba."),
    ],
    [
        E("Mientras escuchas un cuento, oyes: «El guardián era intrépido: nunca temía a la oscuridad». Sin el diccionario, ¿qué deduces de intrépido: que no tiene miedo o que es lento?", "Que no tiene miedo", "La explicación dice que nunca temía."),
        E("Palabra desconocida: «ávido». Texto: «Leía ávido, sin pausa, un libro tras otro». ¿Qué deducirías: con mucho deseo de leer o con desgano?", "Con mucho deseo de leer", "Leía sin pausa y uno tras otro."),
    ],
    [E("En una conferencia escolar escuchas: «La ruta fue extenuante: al final, todos estaban agotados». Quieres anotar la palabra con su significado. ¿Cuál anotas: a) extenuante: muy cansador b) extenuante: muy divertido?", "a", "La pista dice que quedaron agotados.")],
    [
        E("¿Cómo se llama lo que rodea a una palabra y ayuda a entenderla?", "Contexto", "Aporta las pistas."),
        E("¿Sirve el diccionario para comprobar un significado? Responde sí o no.", "Sí", "Confirma la deducción."),
        E("¿Hay que usar las palabras nuevas al hablar? Responde sí o no.", "Sí", "Así pasan a formar parte de mi vocabulario."),
    ],
    ("Lee este fragmento (o pide a alguien que te lo lea en voz alta): «El explorador era perspicaz: se daba cuenta de lo que otros pasaban por alto. Ante una duda, actuaba con cautela, midiendo cada paso. Su mapa era una reliquia: lo había heredado de su abuelo y lo guardaba como un tesoro». Para «perspicaz», «cautela» y «reliquia», escribe la pista del texto, tu significado propuesto y una oración propia con cada palabra.",
     "Perspicaz: pista «se daba cuenta de lo que otros pasaban por alto»; significa muy atento y que entiende rápido. Oración: «Mi hermana es perspicaz y descubrió el truco».",
     ["señala una pista del texto para cada palabra", "propone un significado razonable", "escribe una oración propia correcta"], ["tres filas: pista, significado y oración"], ["inventar sin pistas", "oración con la palabra mal usada"],
     "Si la oración no se entiende, cámbiala por otra situación en que la palabra tenga sentido."),
    "Escribe una oración con la palabra «meticuloso» y otra con «efímero».",
    "Escucha un noticiero o lee una nota y anota una palabra nueva con la pista que te ayudó.",
)

# ================================================================ OA 30 · clase 2
reg(
    OA30, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar con las palabras nuevas.",
    "Aprenderé a precisar el significado de palabras nuevas usando prefijos, sufijos, familias de palabras, sinónimos y antónimos. Sirve para entender mejor lo que escucho y elegir mejor lo que voy a decir.",
    ["Sé deducir el significado de una palabra por el contexto.", "Sé qué es un sinónimo."],
    [
        "Muchas palabras se forman juntando partes con significado. Un prefijo va al comienzo: «re-» significa otra vez (releer), «pre-» significa antes (prever), «in-» o «im-» indican negación (imposible), «des-» indica lo contrario (desorden). Un sufijo va al final: «-ble» indica que se puede (lavable), «-oso» indica que tiene mucho de algo (cuidadoso), «-dad» indica cualidad (bondad). Si reconoces las partes, puedes deducir el significado.",
        "Por ejemplo, «impredecible» se forma con «im-» (no), «pre-» (antes), «decir» y «-ble» (se puede): significa que no se puede predecir. Del mismo modo, «inolvidable» es lo que no se puede olvidar. Las palabras que comparten una raíz forman una familia de palabras: «cuidar», «cuidado», «cuidadoso» y «descuidado» comparten «cuid-».",
        "También precisamos con sinónimos (palabras de significado parecido) y antónimos (palabras de significado contrario). «Escaso» es sinónimo de «poco» y antónimo de «abundante». Pero ojo: los sinónimos rara vez significan exactamente lo mismo; cambian el matiz o el registro. Por eso conviene comprobar que la palabra elegida encaje en la frase.",
    ],
    [("prefijo", "parte que se agrega al comienzo de una palabra"), ("sufijo", "parte que se agrega al final de una palabra"), ("familia de palabras", "palabras que comparten una misma raíz"), ("antónimo", "palabra de significado contrario"), ("matiz", "pequeña diferencia de significado")],
    [
        ("Analizar con partes", "¿Qué significa «reconstruir» si «re-» significa otra vez y «construir» significa levantar algo?", ["Separo las partes: re- + construir.", "Re- significa otra vez.", "Reconstruir es construir de nuevo."], "Construir de nuevo."),
        ("Sinónimo y antónimo", "Para la palabra «escaso», di un sinónimo y un antónimo.", ["Sinónimo: significa parecido, como «poco».", "Antónimo: lo contrario, como «abundante».", "Compruebo en una frase."], "Sinónimo: poco. Antónimo: abundante."),
    ],
    [("Creer que todo prefijo «in-» significa «no».", "Hay palabras como «inicio» que no lo usan así.", "Comprueba que la palabra base exista: «in-» + «seguro» = «inseguro»."), ("Cambiar una palabra por un sinónimo sin revisar si encaja.", "Se piensa que significan exactamente lo mismo.", "Relee la frase para ver si el matiz sirve.")],
    [
        E("¿Qué significa el prefijo «re-» en «releer»: otra vez o antes?", "Otra vez", "Releer es leer de nuevo."),
        E("¿Qué significa el sufijo «-ble» en «lavable»: que se puede o que ya está hecho?", "Que se puede", "Lavable es lo que se puede lavar."),
        E("¿Cuál es un antónimo de «abundante»: escaso o numeroso?", "Escaso", "Significa lo contrario."),
    ],
    [
        E("¿Qué significa «desorden» si «des-» indica lo contrario de «orden»: falta de orden o mucho orden?", "Falta de orden", "Des- niega o invierte la palabra base."),
        E("¿Cuál palabra pertenece a la familia de «cuidar»: cuidadoso o ciudad?", "Cuidadoso", "Comparte la raíz «cuid-»."),
        E("«Imposible» se forma con im- (no) y «posible». ¿Qué significa: que no se puede o que se puede mucho?", "Que no se puede", "Im- indica negación."),
    ],
    [
        E("Descompón «inolvidable»: in- + olvidar + -ble. ¿Qué significa: que no se puede olvidar o que se olvida rápido?", "Que no se puede olvidar", "Suma negación y posibilidad."),
        E("¿Cuál palabra es un sinónimo de «afable»: amable o ruidoso?", "Amable", "Afable significa amable en el trato."),
        E("Ordena de más a menos cantidad: a) escaso b) abundante c) suficiente. Escribe las letras.", "b, c, a", "Abundante es mucho, suficiente alcanza y escaso es poco."),
    ],
    [
        E("Un estudiante dice: «Los sinónimos significan exactamente lo mismo». ¿Es correcto? Responde sí o no.", "No", "Suelen diferir en matiz o registro."),
        E("«Predecible» se forma con «pre-» (antes), «decir» y «-ble» (que se puede): ¿qué significa: que se puede anticipar o que no se puede anticipar?", "Que se puede anticipar", "Suma antes y posibilidad; lo contrario es «impredecible»."),
    ],
    [
        E("Quieres decir que algo «no se puede romper». ¿Qué palabra formas con «in-» + «romper» + «-ble»: irrompible o rompible? Elige la que significa «que no se puede romper».", "Irrompible", "In- (que se transforma en ir- antes de r) niega la posibilidad."),
        E("En «El cuidadoso carpintero revisó cada medida», ¿qué sufijo da a «cuidadoso» el sentido de «lleno de cuidado»: -oso o -dad?", "-oso", "-oso indica que tiene mucho de algo."),
    ],
    [E("En una exposición quieres decir que una tarea «no se puede hacer». Tienes dos opciones: «imposible» e «inalcanzable». ¿Cuál es más cercana a «no se puede hacer»: imposible o inalcanzable?", "Imposible", "Imposible significa que no se puede; inalcanzable habla de algo que no se puede alcanzar.")],
    [
        E("¿Cómo se llama la parte que va al final de una palabra, como «-oso»?", "Sufijo", "Va al final."),
        E("¿Un antónimo tiene significado contrario? Responde sí o no.", "Sí", "Por ejemplo, abundante y escaso."),
        E("¿Dos palabras de la misma raíz forman una familia de palabras? Responde sí o no.", "Sí", "Comparten una raíz."),
    ],
    ("Analiza estas cuatro palabras separando las partes y escribe su significado: «predecir», «incomprensible», «reutilizable» y «cuidadoso». Para cada una, escribe una oración propia. Después anota un sinónimo y un antónimo de «afable» o de «escaso».",
     "Reutilizable = re- (otra vez) + utilizar + -ble (que se puede): se puede usar otra vez. Oración: «Mi botella es reutilizable». Antónimo de escaso: abundante.",
     ["separa correctamente las partes", "explica el significado", "escribe oraciones correctas", "anota un sinónimo y un antónimo"], ["cuatro análisis y oraciones"], ["inventar significados", "confundir sinónimo y antónimo"],
     "Si no puedes separar la palabra, busca su raíz: ¿qué otra palabra se parece?"),
    "Forma dos palabras con el prefijo «des-» y explica qué significan.",
    "Busca en un texto tres palabras con prefijo o sufijo y descompónlas.",
)

# ================================================================ OA 30 · clase 3
reg(
    OA30, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para probar las frases en voz alta.",
    "Aprenderé a elegir la palabra más pertinente para cada situación, según su significado, su matiz y el registro. Sirve para incorporar el vocabulario nuevo de forma adecuada y no forzada.",
    ["Sé deducir y precisar el significado de palabras nuevas.", "Sé que existen sinónimos con matices distintos."],
    [
        "Incorporar de manera pertinente una palabra nueva significa usarla cuando corresponde: que su significado encaje con lo que quieres decir, que combine con las otras palabras de la frase y que sea adecuada a la situación. No basta con conocer una palabra: hay que saber cuándo usarla. Una palabra puede ser correcta en el diccionario y estar mal usada en una frase.",
        "Los sinónimos muestran bien esta idea. «Caminar», «deambular», «marchar» y «merodear» se relacionan con avanzar a pie, pero cada uno tiene un matiz. Deambular es caminar sin rumbo fijo. Marchar es caminar con paso firme y ordenado. Merodear es andar cerca de un lugar con intención dudosa. «Los soldados deambulaban en fila» suena raro; «los soldados marchaban en fila» es pertinente.",
        "También importa el registro. En una exposición formal es mejor «afable» que «buena onda»; en una conversación con amigos puede ser al revés. Y hay palabras con carga positiva o negativa: «ahorrador» suena positivo y «tacaño» suena negativo, aunque ambos se refieren a quien gasta poco. Para elegir, pregúntate: ¿qué significa?, ¿qué matiz tiene?, ¿a quién se lo digo?",
    ],
    [("pertinente", "adecuado a lo que se quiere decir"), ("matiz", "pequeña diferencia de significado o intención"), ("registro", "forma de hablar según la situación"), ("deambular", "caminar sin rumbo fijo"), ("marchar", "caminar con paso firme y ordenado")],
    [
        ("Elegir entre sinónimos", "«Los soldados ______ en fila hacia el cuartel». Opciones: marchaban / deambulaban.", ["Marchar es caminar con paso firme y ordenado.", "Deambular es caminar sin rumbo.", "La frase habla de soldados en fila."], "Marchaban."),
        ("Elegir según el matiz", "Quieres decir algo positivo de un amigo que gasta con cuidado. ¿Dices «ahorrador» o «tacaño»?", ["Ambas hablan de gastar poco.", "«Tacaño» suena negativo.", "«Ahorrador» suena positivo."], "Ahorrador."),
    ],
    [("Usar una palabra solo porque suena elegante.", "Se piensa que impresiona.", "Úsala solo si encaja con lo que quieres decir."), ("Pensar que los sinónimos son intercambiables.", "No se miran los matices.", "Relee la frase y pregúntate si el matiz calza.")],
    [
        E("«El niño ______ por el parque sin saber adónde ir». Opciones: marchaba / deambulaba.", "deambulaba", "No tiene rumbo fijo."),
        E("«Los estudiantes ______ al ritmo de la banda en el desfile». Opciones: marchaban / merodeaban.", "marchaban", "Caminan con paso firme y ordenado."),
        E("¿Cuál es más pertinente para describir a una persona amable en una exposición formal: afable o buena onda?", "Afable", "Es más formal."),
    ],
    [
        E("«El gato ______ cerca de la cocina esperando que se descuidaran». Opciones: merodeaba / marchaba.", "merodeaba", "Anda cerca de un lugar con intención dudosa."),
        E("Quieres elogiar a un compañero que cuida lo que gasta. ¿Qué palabra elige: ahorrador o tacaño?", "Ahorrador", "Tiene sentido positivo."),
        E("«La ciudad estaba en silencio y la gente era escasa en las calles». ¿Qué significa escasa en esa frase: poca o numerosa?", "Poca", "Se describe un lugar casi vacío."),
    ],
    [
        E("Elige la frase pertinente: a) «El profesor, afable, saludó a todos con una sonrisa.» b) «El profesor, sigiloso, saludó a todos con una sonrisa.»", "a", "Sigiloso no encaja con saludar abiertamente."),
        E("¿Cuál palabra es más precisa para «un trabajo hecho con mucho cuidado de los detalles»: meticuloso o rápido?", "Meticuloso", "Significa cuidadoso con los detalles."),
        E("¿Cuál frase es más formal: a) «El vecino es buena onda.» b) «El vecino es afable.»", "b", "Evita la expresión coloquial."),
    ],
    [
        E("Un estudiante dice: «Si una palabra es bonita, siempre sirve». ¿Es correcto? Responde sí o no.", "No", "Debe encajar con el significado y la situación."),
        E("«La reunión fue efímera» y «la reunión fue interminable». ¿Cuál significa que duró poco: la primera o la segunda?", "La primera", "Efímera es de corta duración."),
    ],
    [
        E("Completa con la palabra pertinente: «Marta, ______ al principio, probó con cuidado el platillo nuevo». Opciones: cautelosa / ruidosa.", "cautelosa", "Probar con cuidado es actuar con precaución."),
        E("Completa con la palabra pertinente: «El detective, ______, siguió al sospechoso sin hacer ruido». Opciones: sigiloso / afable.", "sigiloso", "Actúa en silencio para no ser descubierto."),
    ],
    [E("En una exposición ante la directora quieres describir a un vecino que ayuda a todos y trata bien a la gente. ¿Qué frase es mejor: a) «Mi vecino es afable y colabora con la comunidad.» b) «Mi vecino es súper buena onda.»", "a", "Es más formal y precisa.")],
    [
        E("¿Cómo se llama el uso adecuado de una palabra a lo que se quiere decir?", "Uso pertinente", "Encaja con significado y situación."),
        E("¿Los sinónimos son siempre intercambiables? Responde sí o no.", "No", "Pueden tener otro matiz."),
        E("¿Importa el registro al elegir una palabra? Responde sí o no.", "Sí", "Debe ser adecuada a la situación."),
    ],
    ("Lee estas tres frases y elige la palabra pertinente de cada par, escribiendo una breve razón: 1) «La profesora fue (afable / sigilosa) con los visitantes». 2) «Los bomberos (marchaban / merodeaban) en fila hacia el desfile». 3) «El clima de la mañana fue (efímero / meticuloso) y pronto cambió». Después, escribe una frase propia con una palabra nueva que hayas aprendido esta semana.",
     "1) afable, porque trata bien. 2) marchaban, porque van en fila. 3) efímero, porque duró poco. Frase propia: «Mi abuela fue meticulosa al ordenar sus fotos».",
     ["elige la palabra correcta en cada par", "da una razón", "su frase propia usa bien la palabra"], ["tres elecciones con razón y una frase propia"], ["elegir por sonido", "usar la palabra sin que calce"],
     "Si dudas, reemplaza la palabra por su significado y comprueba que la frase siga teniendo sentido."),
    "Escribe una frase pertinente con «deambular» y otra con «marchar».",
    "Busca dos sinónimos de «grande» y explica cuándo usarías cada uno.",
)

# ================================================================ OA 30 · clase 4
reg(
    OA30, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para comparar frases.",
    "Aprenderé a comparar distintos usos de una palabra y a distinguir cuándo está bien o mal empleada, incluyendo palabras con más de un significado. Sirve para no usar vocabulario nuevo de forma forzada y para entender mejor lo que escucho.",
    ["Sé elegir palabras pertinentes.", "Sé deducir significados por el contexto."],
    [
        "Algunas palabras tienen más de un significado: son polisémicas. «Hoja» puede ser la hoja de un árbol o una hoja de papel. «Banco» puede ser un asiento largo, un lugar donde se guarda dinero o un grupo de peces. «Copa» puede ser un vaso con pie o la parte alta de un árbol. El contexto nos dice cuál significado corresponde: «La copa del árbol da sombra» se refiere a la parte alta.",
        "Comparar usos de una palabra nueva nos ayuda a saber si está bien empleada. Imagina que alguien dice: «El niño cauteloso corrió sin mirar a ningún lado». Hay una contradicción: cauteloso significa que actúa con precaución, y correr sin mirar es lo contrario. En cambio, «El niño cauteloso miró a ambos lados antes de cruzar» es un uso pertinente.",
        "Al escuchar a otras personas, podemos aprender de sus usos, pero también detectar errores. Para revisar, hacemos tres preguntas: ¿el significado de la palabra encaja con la frase?, ¿combina con las demás palabras?, ¿hay contradicciones? Si la respuesta es no, buscamos otra palabra o reformulamos.",
    ],
    [("polisemia", "cuando una palabra tiene varios significados"), ("contradicción", "cuando dos ideas no pueden ser ciertas a la vez"), ("empleo", "uso de una palabra en una frase"), ("reformular", "decir de otra manera"), ("uso forzado", "uso que no encaja con la situación")],
    [
        ("Elegir el significado", "«Dejé el bolso en el banco de la plaza». ¿Qué significado de «banco» corresponde: asiento largo o lugar donde se guarda dinero?", ["Miro el contexto: en la plaza.", "En una plaza hay asientos.", "Es el asiento largo."], "Asiento largo."),
        ("Detectar un mal uso", "«La niña meticulosa pintó sin cuidado y con prisa». ¿Hay un mal uso de «meticulosa»?", ["Meticulosa significa cuidadosa con los detalles.", "La frase dice que pintó sin cuidado.", "Hay contradicción."], "Sí, porque contradice el significado de meticulosa."),
    ],
    [("Usar una palabra nueva sin comprobar que encaja.", "Se piensa que basta conocerla.", "Relee la frase y revisa contradicciones."), ("Creer que una palabra tiene un solo significado.", "No se mira el contexto.", "Pregunta qué significado calza en cada frase.")],
    [
        E("«La hoja del árbol cayó en otoño». ¿«Hoja» es parte de una planta o de un cuaderno?", "Parte de una planta", "El contexto menciona un árbol."),
        E("«La copa del árbol da sombra». ¿«Copa» es un vaso o la parte alta del árbol?", "La parte alta del árbol", "El contexto menciona sombra y árbol."),
        E("«Nadamos entre un banco de peces». ¿«Banco» es un asiento o un grupo de peces?", "Un grupo de peces", "El contexto menciona peces."),
    ],
    [
        E("¿Qué frase usa bien «cauteloso»: a) «El ciclista cauteloso frenó al ver la esquina.» b) «El ciclista cauteloso pasó la esquina a toda velocidad sin mirar.»", "a", "La b) contradice la idea de actuar con precaución."),
        E("¿Cuál frase usa bien «efímero»: a) «La burbuja de jabón fue efímera, explotó en segundos.» b) «La montaña era efímera, llevaba millones de años allí.»", "a", "Efímero significa de corta duración."),
        E("«Guardé mis ahorros en el banco». ¿«Banco» es un asiento o una institución para guardar dinero?", "Una institución para guardar dinero", "El contexto menciona ahorros."),
    ],
    [
        E("¿Cuál frase se contradice con «meticuloso»: a) «El meticuloso carpintero midió cada tabla.» b) «El meticuloso carpintero cortó tablas sin medir.»", "b", "Meticuloso implica cuidar los detalles y medir."),
        E("«El comerciante afable gritó y trató mal a sus clientes.» ¿Hay contradicción con «afable»? Responde sí o no.", "Sí", "Afable significa amable en el trato."),
        E("Elige la frase que reformula bien «El hombre sigiloso pisó fuerte»: a) «El hombre sigiloso caminó sin hacer ruido.» b) «El hombre sigiloso gritó su nombre.»", "a", "Reformula sin contradecir el significado."),
    ],
    [
        E("Un estudiante dice: «Mientras más palabras difíciles use, mejor hablo». ¿Es correcto? Responde sí o no.", "No", "Importa usarlas bien, no cuántas se usan."),
        E("En «La hoja del cuaderno está arrugada», ¿«hoja» se refiere a una planta? Responde sí o no.", "No", "El contexto es un cuaderno."),
    ],
    [
        E("Un compañero dice: «El naturalista fue sigiloso y por eso espantó a todos los pájaros con sus gritos». ¿Cómo corriges: a) cambias «sigiloso» por «ruidoso» b) mantienes todo igual?", "a", "Sigiloso y gritos se contradicen."),
        E("Tres usos de «escaso»: 1) «El agua escasea en el desierto.» 2) «Hubo escasa lluvia este año.» 3) «Hay una escasa multitud de cien mil personas.» ¿Cuál es el uso forzado?", "El 3", "Cien mil personas no son pocas."),
    ],
    [E("En un trabajo en grupo, un compañero dice: «El documento fue efímero porque se leyó varias veces durante años». ¿Qué le aconsejas: a) cambiar «efímero» por «duradero» b) dejar la frase?", "a", "Si se leyó durante años, no duró poco.")],
    [
        E("¿Cómo se llama una palabra con varios significados?", "Polisémica", "Cambia de sentido según el contexto."),
        E("¿Hay que revisar que no haya contradicciones al usar una palabra nueva? Responde sí o no.", "Sí", "Así se evita un uso forzado."),
        E("¿El contexto ayuda a elegir el significado de una palabra? Responde sí o no.", "Sí", "Las palabras alrededor dan pistas."),
    ],
    ("Lee estas cuatro frases y marca cuáles usan bien la palabra y cuáles mal; reescribe las incorrectas: 1) «El jardinero meticuloso podó las rosas sin mirar.» 2) «La nieve fue efímera: al mediodía ya se había derretido.» 3) «La directora, afable, retó duramente a los visitantes.» 4) «El zorro sigiloso se acercó al gallinero sin hacer ruido».",
     "1) Mal: meticuloso y sin mirar se contradicen; «podó cada rosa con cuidado». 2) Bien. 3) Mal: afable y retó duramente; «saludó amablemente». 4) Bien.",
     ["identifica bien las cuatro frases", "reescribe las incorrectas sin contradicción", "explica la razón"], ["cuatro valoraciones y dos reescrituras"], ["no ver la contradicción", "reescribir sin cambiar el problema"],
     "Si dudas, reemplaza la palabra por su definición y relee."),
    "Escribe dos frases con «hoja»: una sobre un árbol y otra sobre un cuaderno.",
    "Busca una palabra con dos significados y escribe una frase para cada uno.",
)

# ================================================================ OA 30 · clase 5
T_PUEBLO = ("Texto que lee una persona adulta: «Cuando llegó el invierno, las provisiones del pueblo eran escasas. Marta, la panadera, era afable con todos y repartió el pan sin pedir nada. "
            "Los vecinos, cautelosos al principio, aceptaron y pronto compartieron lo poco que tenían. Esa primavera, aunque la nieve fue efímera, la ayuda entre vecinos perseveró.»")
reg(
    OA30, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer el texto en voz alta y escuchar tu intervención.",
    "Aprenderé a producir una intervención oral que incorpore tres palabras nuevas tomadas de un texto escuchado, de manera pertinente. Sirve para convertir el vocabulario nuevo en parte de mi forma de hablar.",
    ["Sé deducir significados y elegir palabras pertinentes.", "Sé hablar de un tema con introducción, desarrollo y cierre."],
    [
        "Un texto escuchado o leído es una fuente de vocabulario nuevo. Para incorporarlo al hablar, sigue cuatro pasos. Primero, escucha o lee con atención y anota las palabras que no conocías, con su significado. Segundo, elige tres palabras que sirvan para el tema de tu intervención. Tercero, escribe oraciones donde cada palabra encaje con lo que quieres decir. Cuarto, ensaya en voz alta hasta que las uses con naturalidad.",
        "Una intervención oral breve puede responder a una pregunta como «¿Qué piensas de la actitud de Marta?». Se compone de una opinión, una razón y un cierre. Dentro de esas partes, aparecen las palabras nuevas: «Pienso que Marta fue afable porque repartió el pan sin pedir nada. Aunque las provisiones eran escasas, los vecinos compartieron». Observa que cada palabra encaja y se entiende sin explicarla.",
        "Para revisarla, usa una lista: ¿usé tres palabras nuevas?, ¿las usé con el significado correcto?, ¿encajan con el registro?, ¿no hay contradicciones?, ¿se entiende sin leer? Si algo falla, cambia la palabra o la frase. El objetivo no es llenar la intervención de palabras raras, sino usarlas donde ayudan a decir algo con más precisión.",
    ],
    [("intervención oral", "participación breve al hablar en una clase o conversación"), ("incorporar", "agregar algo como parte propia"), ("naturalidad", "forma de hablar sin que suene forzada"), ("ensayar", "practicar antes de hablar"), ("registro", "forma de hablar según la situación")],
    [
        ("Armar una intervención", f"{T_PUEBLO} Responde en una oración: ¿qué piensas de Marta? Usa «afable».", ["Escribo mi opinión.", "Agrego una razón del texto.", "Incluyo la palabra «afable» de forma pertinente."], "«Pienso que Marta fue afable, porque repartió el pan sin pedir nada»."),
        ("Revisar con la lista", "Revisa: «Marta fue cautelosa y gritó a todos». ¿Qué falla de la lista?", ["Cautelosa significa cuidadosa.", "Gritó a todos no encaja.", "Hay contradicción."], "Hay una contradicción: cautelosa y gritó a todos no calzan."),
    ],
    [("Meter palabras nuevas en frases donde no calzan.", "Se busca mostrar vocabulario.", "Usa una palabra solo si encaja con tu idea."), ("Leer la intervención sin ensayarla.", "Se piensa que basta escribirla.", "Ensáyala en voz alta hasta que suene natural.")],
    [
        E(f"{T_PUEBLO} ¿Qué palabra del texto describe a Marta: afable o cautelosa?", "Afable", "El texto dice que era afable con todos."),
        E(f"{T_PUEBLO} ¿Qué palabra describe a los vecinos al principio: afables o cautelosos?", "Cautelosos", "El texto dice que fueron cautelosos al principio."),
        E(f"{T_PUEBLO} ¿Qué significa «escasas» en «las provisiones eran escasas»: pocas o muchas?", "Pocas", "El texto dice que compartieron lo poco que tenían."),
    ],
    [
        E(f"{T_PUEBLO} ¿Cuál es una frase pertinente con «escasas»: a) «Las provisiones eran escasas, por eso compartieron lo poco que tenían.» b) «Las provisiones eran escasas porque había demasiadas.»", "a", "La b) contradice el significado."),
        E(f"{T_PUEBLO} ¿Cuál de estas palabras viene del texto: perseveró o vestigio?", "Perseveró", "Se usa al final: la ayuda entre vecinos perseveró."),
        E("¿Cuál es el orden correcto para incorporar vocabulario nuevo: a) escribir oraciones b) anotar palabras con su significado c) ensayar en voz alta d) elegir tres palabras? Escribe las letras.", "b, d, a, c", "Anota, elige, escribe y ensaya."),
    ],
    [
        E(f"{T_PUEBLO} Una opinión con palabra del texto: «Los vecinos fueron ______ al principio, pero aceptaron el pan». Opciones: cautelosos / efímeros.", "cautelosos", "Describe una actitud de precaución."),
        E(f"{T_PUEBLO} ¿Qué dos palabras del texto usarías para decir que algo duró poco y que se siguió ayudando? Opciones: a) efímera y perseveró b) afable y escasas", "a", "Efímera es de corta duración y perseveró es seguir adelante."),
        E(f"{T_PUEBLO} ¿Cuántas de estas cuatro palabras aparecen en el texto: afable, escasas, vestigio y perseveró?", "3", "Aparecen afable, escasas y perseveró; vestigio no está en este texto."),
    ],
    [
        E("Un estudiante dice: «Si uso muchas palabras nuevas, mi intervención será mejor aunque no se entienda». ¿Es correcto? Responde sí o no.", "No", "Debe usarlas con pertinencia para que se entienda."),
        E("Revisión: «La nieve fue efímera y duró todo el invierno». ¿Qué falla: el uso de «efímera» o el uso de «nieve»?", "El uso de «efímera»", "Si duró todo el invierno no fue de corta duración."),
    ],
    [
        E(f"{T_PUEBLO} ¿Qué intervención usa mejor tres palabras nuevas: a) «Marta, afable, repartió pan cuando las provisiones eran escasas; los vecinos, cautelosos al inicio, aceptaron.» b) «Marta era afable, afable, afable.»", "a", "Usa tres palabras distintas con sentido."),
        E("Tu intervención usó tres palabras nuevas: afable, escasas y perseveró. Si te piden revisar, ¿qué falta comprobar: que cada una encaje en su frase o que sean largas?", "Que cada una encaje en su frase", "El criterio es la pertinencia."),
    ],
    [E("Después de escuchar el texto de Marta, tu profesor pide una intervención de 20 segundos con dos palabras nuevas. ¿Cuál intervención sirve: a) «Creo que los vecinos fueron cautelosos al principio, pero luego fueron generosos y su ayuda perseveró.» b) «Marta hizo pan.»", "a", "Usa dos palabras nuevas con sentido.")],
    [
        E("¿Cuántas palabras nuevas se piden en la actividad de hoy?", "Tres", "Son tres, según la consigna."),
        E("¿Hay que ensayar la intervención en voz alta? Responde sí o no.", "Sí", "Así suena natural."),
        E("¿Conviene usar la palabra aunque no encaje? Responde sí o no.", "No", "Debe ser pertinente."),
    ],
    ("Escucha o lee el texto de Marta (pide a alguien que lo lea): «Cuando llegó el invierno, las provisiones del pueblo eran escasas. Marta, la panadera, era afable con todos y repartió el pan sin pedir nada. Los vecinos, cautelosos al principio, aceptaron y pronto compartieron lo poco que tenían. Esa primavera, aunque la nieve fue efímera, la ayuda entre vecinos perseveró». Elige tres palabras nuevas (afable, cautelosos, escasas, efímera, perseveró), prepara una intervención de 30 segundos que responda «¿Qué opinas de lo que hizo Marta?» y ensáyala en voz alta frente a una persona de tu casa.",
     "«Creo que Marta fue afable y generosa. Aunque las provisiones eran escasas, repartió el pan, y los vecinos, cautelosos al principio, terminaron ayudándose».",
     ["usa tres palabras nuevas del texto", "las palabras encajan con el significado", "da una opinión con una razón", "se entiende sin leer"], ["intervención de 30 segundos y lista revisada"], ["palabras que no calzan", "leer sin ensayar"],
     "Si una palabra no calza, reemplázala por otra del texto que sí encaje."),
    "Escribe una intervención de dos oraciones con «escasas» y «perseveró».",
    "Lee un texto breve en casa, anota dos palabras nuevas y úsalas en una conversación esta semana.",
)

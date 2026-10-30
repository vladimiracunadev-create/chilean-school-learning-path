"""Student material for 3.º básico Inglés, EN03 OA 10 (sonidos /w/, /th/, /s/-/z/ con chants, rimas y diálogos) y OA 11 (interacción breve en clase).

Todo el inglés es original, muy breve y con pista en español. No hay audio externo: una persona de la casa lee en voz alta
y el cuaderno describe la posición de la boca. No se exige acento; se busca que se entienda.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA10, OA11 = "EN03 OA 10", "EN03 OA 11"


def E(rows):
    return [ex(q, a, w) for q, a, w in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 10
lesson(
    OA10, 1,
    "Las palabras y el chant escritos en cada ejercicio, un espejo pequeño si tienes (o tu reflejo en una ventana) y una persona de tu casa para repetir contigo.",
    "Aprenderé a reconocer y decir el sonido /w/ de palabras como water y window, y a repetirlo en un chant muy corto. Sirve para que otras personas te entiendan al hablar inglés.",
    ["Sé que las palabras tienen sonidos.", "Sé decir hello y thank you."],
    [
        "Un sonido (sound) no es lo mismo que una letra. Escribimos el sonido entre barras, por ejemplo /w/. El sonido /w/ está al comienzo de water (agua), window (ventana), we (nosotros), week (semana), wet (mojado) y wind (viento). También suena /w/ al comienzo de one (uno), aunque se escribe con o.",
        "Para decir /w/, mira tu posición de boca (mouth position): redondea los labios como para decir «u» o para soplar una vela, y ábrelos rápido hacia la vocal siguiente. Los dientes no tocan los labios. Tu voz (voice) está encendida: si pones la mano en el cuello, sientes una vibración (vibration).",
        "Muchas personas dicen water como «guater» o we como «gui». Con práctica, se corrige: primero redondea los labios, luego abre. Mira tu cara en un espejo o en una ventana. Después repite el chant: «Water, water, we like water. Wet wind, wet window.» (Nos gusta el agua. Viento mojado, ventana mojada.) Lo importante es que se entienda; no se exige un acento perfecto.",
    ],
    [("sound", "sonido"), ("/w/", "sonido que empieza water"), ("mouth position", "posición de la boca"), ("voice", "voz"), ("vibration", "vibración"), ("chant", "canto rítmico corto")],
    [
        ("Encontrar /w/", "Palabras: window, sun, book. ¿Cuál empieza con /w/?", ["Digo cada palabra en voz alta.", "En window redondeo los labios al comienzo.", "En sun y book no."], "window"),
        ("Decir /w/ bien", "Quieres decir water. ¿Qué haces con los labios antes de abrirlos?", ["Redondeo los labios como para decir «u».", "Los abro rápido hacia la vocal.", "Digo water."], "Redondeo los labios y los abro rápido."),
    ],
    [
        ("Decir /w/ como «g», por ejemplo «guater».", "Se imita el sonido del español.", "Redondea los labios y ábrelos rápido: wa-ter."),
        ("Pensar que one empieza con /o/ porque se escribe con o.", "Se confunde la letra con el sonido.", "One suena como /w/ al comienzo: wun."),
    ],
    [
        ("¿Cómo se dice «agua» en inglés?", "water", "Water empieza con el sonido /w/."),
        ("¿Qué significa «window»?", "Ventana", "Window es la ventana de una casa."),
        ("¿Qué significa «wet»?", "Mojado", "Wet empieza con /w/."),
    ],
    [
        ("¿Qué haces con los labios para decir /w/?", "Los redondeo y luego los abro", "Esa es la posición de boca de /w/."),
        ("¿Entre qué signos se escribe un sonido, como /w/?", "Entre barras", "Las barras muestran que se habla de un sonido y no de una letra."),
        ("¿Cuál palabra empieza con /w/? (a) one (b) cat", "a", "One suena wun, aunque se escribe con o."),
    ],
    [
        ("Palabras: tree, week, ball. Escribe la que empieza con /w/.", "week", "Week es semana y empieza con /w/."),
        ("Palabras: dog, wind, book. Escribe la que empieza con /w/.", "wind", "Wind es viento y empieza con /w/."),
        ("Completa con una palabra con /w/: «The ___ is wet.» (la ventana)", "window", "Window lleva /w/ al comienzo."),
    ],
    [
        ("Ana dice «guater» por water. ¿Qué parte del sonido debe cambiar?", "Debe redondear los labios para /w/", "No es una g; es un sonido de labios."),
        ("Pablo dice que one no tiene sonido /w/ porque no tiene la letra w. ¿Tiene razón?", "No, one empieza con el sonido /w/", "El sonido no depende solo de la letra."),
    ],
    [
        ("Palabras: window, water, tree, wet, sun, we, hat. ¿Cuántas empiezan con /w/?", "4", "Son window, water, wet y we."),
        ("Chant: «Water, water, we like water.» ¿Cuántas veces aparece la palabra water?", "3", "Aparece al comienzo, otra vez y al final."),
    ],
    [("En una canción de curso dicen «Wet wind, wet window». Tu compañero la dice con el comienzo de «g». ¿Qué le dices en español que haga con los labios?", "Que los redondee y los abra rápido", "Así sale el sonido /w/.")],
    [
        ("¿Qué siente tu mano en el cuello cuando dices /w/?", "Vibración", "La voz está encendida con /w/."),
        ("¿Cómo se dice «viento» en inglés?", "wind", "Wind empieza con /w/."),
        ("¿Es necesario tener un acento perfecto?", "No", "Lo importante es que se entienda."),
    ],
    task("Con una persona de tu casa, lee este chant despacio y luego a ritmo con palmadas: «Water, water, we like water. Wet wind, wet window.» Mira tus labios en un espejo o en una ventana. Marca con lápiz cada palabra que empiece con /w/ y cuéntalas. Luego di otro chant corto con tres de estas palabras: week, one, wind.", "Las palabras con /w/ son water (tres veces), we, wet (dos veces), wind y window: ocho en total. Mi chant: «One week, one wind, one week!»", ["marca las palabras con /w/", "redondea los labios al decir /w/", "lee el chant con ritmo", "crea otro chant con palabras con /w/"], ["el chant con palabras marcadas", "nota de la persona que escuchó"], ["decir guater", "pensar que one no tiene /w/"], "No corrijas el acento. Pide repetir la palabra y celebra el sonido de labios."),
    "Di diez veces seguidas water con los labios redondos, mirándote en un espejo.",
    "Dibuja tres palabras con /w/ (water, window, wind) y escribe el nombre en inglés.",
)

lesson(
    OA10, 2,
    "Las palabras y el chant escritos en cada ejercicio, un espejo pequeño si tienes y una persona de tu casa. Nada de morder la lengua: solo apoyarla suave.",
    "Aprenderé a producir con cuidado los dos sonidos de la letra combinada th (como en three y this) y a distinguirlos. Sirve para decir palabras como thank you y three de forma que se entiendan.",
    ["Sé que /w/ es un sonido.", "Sé decir thank you de forma aproximada."],
    [
        "En inglés hay un sonido que no existe en el español: /th/. Se escribe con las letras t y h juntas. Para decirlo, apoya la punta de la lengua suavemente entre los dientes (tongue between the teeth), sin morder, y deja salir el aire. Se oye en three (tres), thank (gracias), think (pensar), thumb (pulgar) y mouth (boca).",
        "Hay dos formas de /th/. La primera es sin voz: sale solo aire, sin vibración en el cuello, como en three y thank. La segunda es con voz: la garganta vibra, como en this (esto), that (eso), the (el, la), they (ellos). Para comprobarlo, pon la mano en el cuello: si vibra, es con voz. Cuando digas th, la lengua no debe quedar detrás de los dientes ni convertirse en una t.",
        "Cuidado con tres confusiones: three no es tree (árbol), think no es sink (hundirse) y thank no es sank (se hundió). Si la lengua se queda detrás de los dientes, el sonido cambia y se entiende otra palabra. Repite lento, con la lengua suave.",
    ],
    [("/th/", "sonido de three y this"), ("tongue", "lengua"), ("teeth", "dientes"), ("three", "tres"), ("this", "esto"), ("thank", "agradecer")],
    [
        ("Distinguir three y tree", "Escuchas «three» y «tree». ¿Cuál lleva /th/?", ["Escribo las dos palabras.", "Three tiene th al comienzo.", "En tree la lengua no toca los dientes."], "three"),
        ("Con voz o sin voz", "Pones la mano en el cuello. Con thank no vibra; con this sí. ¿Cuál es con voz?", ["Digo thank: no vibra.", "Digo this: vibra.", "La que vibra es con voz."], "this"),
    ],
    [
        ("Decir tree por three.", "La lengua queda detrás de los dientes y se dice t.", "Apoya la lengua suave entre los dientes y deja salir el aire."),
        ("Morder la lengua con fuerza para decir th.", "Se piensa que hay que apretar.", "Apoya la lengua con suavidad, sin morder."),
    ],
    [
        ("¿Cómo se dice «tres» en inglés?", "three", "Three lleva el sonido /th/."),
        ("¿Cómo se dice «gracias» con la forma de dos palabras?", "thank you", "Thank lleva /th/."),
        ("¿Qué significa «this»?", "Esto", "Se usa para señalar algo cercano."),
    ],
    [
        ("¿Dónde pones la lengua para decir /th/?", "Entre los dientes, suavemente", "Así sale el sonido sin morder."),
        ("¿Es th lo mismo que t?", "No", "Th pone la lengua entre los dientes y t no."),
        ("Pones la mano en el cuello y vibra al decir this. ¿Es th con voz o sin voz?", "Con voz", "La garganta vibra con this."),
    ],
    [
        ("Palabras: tree, three, sun. Escribe la que lleva /th/ al comienzo.", "three", "Three lleva th."),
        ("Palabras: sink, think, cat. Escribe la que lleva /th/ al comienzo.", "think", "Think es pensar y lleva th."),
        ("Palabras: sank, thank, bus. Escribe la que lleva /th/ al comienzo.", "thank", "Thank es agradecer y lleva th."),
    ],
    [
        ("Lola dice «tree» por «three». ¿Qué palabra se entiende en inglés?", "Árbol", "Tree significa árbol, no tres."),
        ("Paula muerde fuerte la lengua para decir th. ¿Qué le recomiendas?", "Apoyarla suave, sin morder", "El sonido sale con aire y lengua suave."),
    ],
    [
        ("Palabras: this, that, thumb, they, three. Escribe cuántas llevan th con voz (vibran).", "3", "This, that y they llevan th con voz."),
        ("Palabras: thumb, three, thank, this. Escribe cuántas llevan th sin voz.", "3", "Thumb, three y thank llevan th sin voz."),
    ],
    [("Le dices a un amigo de otro país «tree books» cuando querías decir tres libros. ¿Qué palabra debes cambiar para decir three?", "tree por three", "La lengua debe ir entre los dientes en th.")],
    [
        ("¿Cómo se dice «pulgar» en inglés?", "thumb", "Thumb lleva th sin voz."),
        ("¿Cómo se llama el sonido que se escribe con th?", "/th/", "Es un sonido propio del inglés."),
        ("¿Qué compruebas con la mano en el cuello?", "Si hay vibración", "Con voz vibra; sin voz no."),
    ],
    task("Con una persona de tu casa, mira una ventana o un espejo y di despacio: «three, thank you, think, thumb» y luego «this, that, they». Apoya la lengua suave entre los dientes. Pon la mano en el cuello en cada grupo y di si vibró (con voz) o no (sin voz). Después di los pares: three/tree, think/sink, thank/sank, y pide que te digan cuál palabra dijiste.", "En three, thank you, think y thumb no vibra. En this, that y they vibra. Distingo three de tree.", ["apoya la lengua suave entre los dientes", "dice los dos grupos de palabras", "dice si vibra o no", "distingue los tres pares"], ["nota de la persona que escuchó los pares"], ["decir tree por three", "morder la lengua con fuerza"], "No corrijas el acento: pide que repita la palabra con la lengua suave y celebra los avances."),
    "Di tres veces seguidas «thank you» frente a un espejo, con la lengua suave entre los dientes.",
    "Escribe tres palabras con th sin voz y tres con voz que hayas aprendido hoy.",
)

lesson(
    OA10, 3,
    "Las palabras escritas en cada ejercicio y una persona de tu casa. Usa tu mano en el cuello para sentir la vibración.",
    "Aprenderé a distinguir y decir los sonidos /s/ y /z/ con las palabras de la clase. Sirve para no confundir pares como sip y zip, o bus y buzz.",
    ["Sé que los sonidos se pueden sentir con la mano en el cuello.", "Sé decir /w/ y /th/."],
    [
        "El sonido /s/ es el de sun (sol), sit (sentarse), sip (tomar un sorbo), bus (bus) e ice (hielo). El sonido /z/ es el de zoo (zoológico), zebra (cebra), zip (cierre), zero (cero), buzz (zumbido) y eyes (ojos). La posición de la boca es casi la misma, pero hay una diferencia: /s/ es sin voz y /z/ es con voz (voice).",
        "Para comprobarlo, pon la mano en el cuello. Con /s/ no sientes vibración (vibration), como un viento suave. Con /z/ sientes una vibración, como una abeja pequeña. En inglés, la letra z se dice /z/, como en zoo. La letra s puede decirse /s/, como en sun, o /z/, como en is (es) y nose (nariz).",
        "Esto importa porque cambia el significado: sip no es zip, y bus no es buzz. Practica los pares: sip/zip, bus/buzz, Sue/zoo. Escucha la diferencia con la mano en el cuello y repite despacio. Recuerda: no se exige un acento perfecto, sino que se entienda qué palabra dijiste.",
    ],
    [("/s/", "sonido sin voz, como sun"), ("/z/", "sonido con voz, como zoo"), ("voice", "voz"), ("vibration", "vibración"), ("sip / zip", "tomar un sorbo / cierre"), ("bus / buzz", "bus / zumbido")],
    [
        ("Con voz o sin voz", "Dices sun y zoo con la mano en el cuello. ¿Cuál vibra?", ["Digo sun: no vibra.", "Digo zoo: vibra.", "La que vibra es zoo."], "zoo (/z/)"),
        ("Elegir un par", "Escuchas «zip». Opciones: sip / zip. ¿Cuál es con voz al comienzo?", ["Zip empieza con z.", "La z suena /z/.", "Ese sonido vibra."], "zip"),
    ],
    [
        ("Decir zoo con /s/ al comienzo.", "En español no suena la z como /z/.", "Pon la mano en el cuello y busca la vibración."),
        ("Pensar que la letra s siempre suena /s/.", "Se olvida que is suena /z/.", "La letra s puede ser /s/ o /z/; escúchalo en cada palabra."),
    ],
    [
        ("¿Cómo se dice «sol» en inglés?", "sun", "Sun empieza con /s/."),
        ("¿Cómo se dice «cebra» en inglés?", "zebra", "Zebra empieza con /z/."),
        ("¿Qué significa «buzz»?", "Zumbido", "Es el sonido de una abeja."),
    ],
    [
        ("¿Cuál sonido es con voz? (a) /s/ (b) /z/", "b", "El sonido /z/ hace vibrar el cuello."),
        ("¿Qué sientes con la mano en el cuello al decir /s/?", "Nada de vibración", "El sonido /s/ es sin voz."),
        ("¿Qué sonido tiene la letra z en zoo?", "/z/", "La z de zoo suena /z/."),
    ],
    [
        ("Palabras: sit, zip, sun. Escribe la que empieza con /z/.", "zip", "Zip empieza con z y suena /z/."),
        ("Palabras: bus, buzz. Escribe la que termina con /z/ (zumbido).", "buzz", "Buzz termina con z, que suena /z/."),
        ("Palabras: zoo, Sue, zebra. Escribe cuántas empiezan con /z/.", "2", "Zoo y zebra empiezan con /z/."),
    ],
    [
        ("Ana dice «sip» cuando quería decir «zip» (cierre). ¿Cambia el significado?", "Sí, es otra palabra", "Sip y zip son palabras distintas."),
        ("Leo pregunta si is suena /s/ porque lleva s. ¿Qué sonido tiene is?", "/z/", "En is la s suena /z/."),
    ],
    [
        ("Pares: sip/zip, bus/buzz, Sue/zoo. En cuántos pares el segundo tiene /z/ (con voz)?", "3", "Zip, buzz y zoo tienen /z/."),
        ("Palabras: sun, zero, is, ice. Escribe cuántas tienen /z/.", "2", "Zero e is tienen /z/."),
    ],
    [("En el zoológico, un niño dice «The zebra is in the soo». Quería decir «zoo». ¿Qué sonido debe cambiar al comienzo de zoo?", "/s/ por /z/", "Zoo empieza con /z/, con voz.")],
    [
        ("¿Cómo se dice «cero» en inglés?", "zero", "Zero empieza con /z/."),
        ("¿Qué palabra lleva /s/ al comienzo: zoo o sun?", "sun", "Sun empieza con /s/."),
        ("¿Para qué sirve la mano en el cuello?", "Para sentir si hay vibración", "Con voz vibra; sin voz, no."),
    ],
    task("Con una persona de tu casa, pon la mano en el cuello y di despacio: sun, sit, bus, ice y luego zoo, zip, zebra, buzz, eyes. Anota si vibra o no. Después di los pares sip/zip, bus/buzz y Sue/zoo y pide que te digan cuál de los dos dijiste, con los ojos cerrados.", "En sun, sit, bus e ice no vibra (/s/). En zoo, zip, zebra, buzz y eyes vibra (/z/). Distingo los tres pares.", ["siente la vibración en /z/", "dice los dos grupos de palabras", "dice los tres pares", "la persona acierta el par"], ["nota de la persona que escuchó los pares"], ["decir zoo con /s/", "pensar que la letra s siempre es /s/"], "No corrijas el acento. Repite el par más difícil con él o ella y celebra los aciertos."),
    "Imita una abeja diciendo «zzz» y siente la vibración en el cuello. Luego di «sss» y siente la diferencia.",
    "Dibuja un zoo con una zebra y una abeja (buzz), y escribe el nombre de cada animal en inglés.",
)

lesson(
    OA10, 4,
    "El chant escrito en esta clase, palmadas o golpes suaves en una mesa y una persona de tu casa.",
    "Aprenderé a decir un chant corto con ritmo usando los sonidos /w/, /th/, /s/ y /z/, y a crear mi propia estrofa. Sirve para practicar los sonidos jugando.",
    ["Sé decir /w/, /th/, /s/ y /z/ en palabras sueltas.", "Sé seguir un ritmo con palmadas."],
    [
        "Un chant es un canto rítmico y corto que se dice con palmadas. Ayuda a practicar sonidos porque repites las mismas palabras con ritmo. Este chant es original: «Water, water, we like water. / Three thin thumbs say thank you. / Sit in the sun, sip, sip, sip. / Zip, zip, zoo, zoo, zebra.» (thin significa delgado; say significa dicen; sit in the sun significa siéntate al sol.)",
        "Cada línea practica un sonido: la primera lleva /w/, la segunda /th/, la tercera /s/ y la cuarta /z/. Primero lee el chant sin ritmo. Luego marca el ritmo con una palmada por cada palabra importante. Por último, di el chant más rápido. Si te equivocas, no importa: respira y empieza de nuevo.",
        "Una rima (rhyme) es cuando dos palabras terminan con el mismo sonido, como sun y fun (diversión), o bee y three. Los chants y las rimas ayudan a recordar sonidos. Para crear tu estrofa, cambia una palabra por otra que tenga el mismo sonido. Por ejemplo, puedes cambiar «water» por «wind»: «Wind, wind, we like wind». Mira el sonido, no solo la letra. Una estrofa nueva debe mantener el mismo sonido para que el chant siga practicando lo mismo.",
    ],
    [("chant", "canto rítmico corto"), ("rhythm", "ritmo"), ("clap", "dar palmadas"), ("thin", "delgado"), ("say", "decir"), ("sit", "sentarse")],
    [
        ("Encontrar el sonido de una línea", "Línea: «Three thin thumbs say thank you.» ¿Qué sonido practica?", ["Leo las palabras: three, thin, thumbs, thank.", "Todas llevan th.", "El sonido es /th/."], "/th/"),
        ("Cambiar una palabra", "Línea: «Water, water, we like water.» Quieres cambiar water por otra palabra con /w/. ¿Qué palabra sirve?", ["Busco una palabra que empiece con /w/.", "Wind empieza con /w/.", "La cambio."], "wind"),
    ],
    [
        ("Cambiar una palabra por otra que no tenga el mismo sonido.", "Se mira la letra y no el sonido.", "Escucha el sonido de la palabra nueva."),
        ("Decir el chant muy rápido desde el comienzo.", "Se pierde el ritmo y los sonidos.", "Empieza despacio y sube la velocidad."),
    ],
    [
        ("¿Qué es un «chant»?", "Un canto rítmico corto", "Se dice con ritmo y palmadas."),
        ("¿Qué significa «clap»?", "Dar palmadas", "Se usa para marcar el ritmo."),
        ("¿Qué significa «thin»?", "Delgado", "Aparece en el chant de th."),
    ],
    [
        ("¿Qué sonido practica «Zip, zip, zoo, zoo, zebra»?", "/z/", "Todas empiezan con z."),
        ("¿Qué sonido practica «Sit in the sun, sip, sip, sip»?", "/s/", "Sit, sun y sip empiezan con /s/."),
        ("¿Qué haces para marcar el ritmo del chant?", "Doy una palmada por cada palabra importante", "El ritmo ayuda a recordar los sonidos."),
    ],
    [
        ("Completa con una palabra con /w/: «Wet wind, wet ___.» (ventana)", "window", "Window lleva /w/ al comienzo."),
        ("Completa con una palabra con /th/: «Three thin ___.» (pulgares)", "thumbs", "Thumbs lleva th."),
        ("Completa con una palabra con /z/: «Zip, zip, zoo, ___.» (cebra)", "zebra", "Zebra lleva /z/."),
    ],
    [
        ("Un niño cambia «water» por «sun» en la línea de /w/. ¿Mantiene el mismo sonido? Responde sí o no.", "No", "Sun empieza con /s/, no con /w/."),
        ("Una niña cambia «zip» por «zero» en la línea de /z/. ¿Mantiene el mismo sonido? Responde sí o no.", "Sí", "Zero empieza con /z/."),
    ],
    [
        ("Línea: «Sip, sip, sip, sun, sit.» Escribe cuántas palabras hay.", "5", "Son sip, sip, sip, sun y sit."),
        ("Estrofa nueva: «Wind, wind, we like wind.» ¿Qué palabra cambió respecto de «Water, water, we like water»? Escribe la nueva.", "wind", "Se cambió water por wind."),
    ],
    [("En la feria de ciencias, tu grupo dice un chant con la palabra bee (abeja) y el sonido /z/. Elige la palabra que debe aparecer: (a) buzz (b) bus", "a", "Buzz termina con /z/ y es el zumbido de la abeja.")],
    [
        ("¿Qué palabra rima con sun? (a) fun (b) zoo", "a", "Sun y fun terminan con el mismo sonido."),
        ("¿Se necesita un acento perfecto para decir un chant?", "No", "Se busca que se entienda."),
        ("Si te equivocas en el chant, ¿qué haces?", "Respiro y empiezo de nuevo", "Equivocarse es normal."),
    ],
    task("Di con una persona de tu casa este chant con palmadas: «Water, water, we like water. / Three thin thumbs say thank you. / Sit in the sun, sip, sip, sip. / Zip, zip, zoo, zoo, zebra.» Escribe cuál sonido practica cada línea. Luego crea una estrofa nueva que cambie una palabra de la primera línea por otra con /w/ (por ejemplo wind o window) y dila con ritmo.", "Línea 1: /w/. Línea 2: /th/. Línea 3: /s/. Línea 4: /z/. Mi estrofa: «Window, window, we like window.»", ["dice el chant con ritmo", "identifica el sonido de cada línea", "crea una estrofa con /w/", "se entiende al decirla"], ["la estrofa escrita", "nota de la persona que escuchó"], ["cambiar por una palabra sin /w/", "decirlo muy rápido al comienzo"], "No corrijas el acento. Repite el chant juntos y celebra el ritmo."),
    "Di el chant en voz baja con el ritmo de tus palmadas.",
    "Escribe una estrofa de cuatro palabras para el sonido /th/, por ejemplo «Think, thank, thumb, three».",
)

lesson(
    OA10, 5,
    "El diálogo escrito en esta clase y una persona de tu casa para leer los dos personajes por turnos.",
    "Aprenderé a decir un diálogo muy breve de manera que se entienda, con los sonidos /w/, /th/ y /z/ de la clase. Sirve para hablar con calma y claridad.",
    ["Sé decir los sonidos /w/, /th/, /s/ y /z/.", "Sé leer un diálogo con dos personajes."],
    [
        "Un diálogo (dialogue) es una conversación entre dos personas. Este diálogo es original y muy corto: «A: Hello! Is this your bag? B: Yes, it is. Thank you! A: You're welcome.» (¡Hola! ¿Esta es tu mochila? Sí, lo es. ¡Gracias! De nada.) «You're welcome» significa de nada; es la respuesta que enseñamos aquí, aunque en inglés hay otras formas de decirlo, como «No problem». En este diálogo aparecen /th/ (this, thank), /z/ (is) y /w/ (welcome).",
        "Para que se entienda, habla despacio, separa bien las palabras y repite si hace falta. Que sea inteligible (intelligible) quiere decir que la otra persona puede entender el mensaje. No necesitas un acento perfecto. Si alguien no entiende, puedes repetir más lento o decir «Sorry?» (¿perdón?).",
        "Practica en tres pasos. Primero, lee el diálogo con tu pareja, línea por línea. Segundo, marca con lápiz las palabras con /w/, /th/ y /z/ y practícalas solas. Tercero, di el diálogo completo, cambiando de personaje. Si te equivocas, puedes decir «Sorry» y empezar otra vez.",
    ],
    [("dialogue", "diálogo, conversación"), ("intelligible", "que se puede entender"), ("You're welcome", "de nada"), ("Sorry?", "¿perdón?, ¿cómo?"), ("Is this your bag?", "¿esta es tu mochila?"), ("Yes, it is", "sí, lo es")],
    [
        ("Encontrar los sonidos", "Diálogo: «A: Hello! Is this your bag? B: Yes, it is. Thank you!» ¿Qué sonido tiene thank?", ["Miro la palabra thank.", "Empieza con th.", "El sonido es /th/ sin voz."], "/th/"),
        ("Hablar para que se entienda", "Tu compañero no entiende «Is this your bag?». ¿Qué haces?", ["Repito más lento.", "Separo las palabras.", "Uso gestos si hace falta."], "Repito más lento y separo las palabras."),
    ],
    [
        ("Hablar muy rápido para sonar «más inglés».", "Se confunde rapidez con claridad.", "Habla lento y claro."),
        ("Quedarse callado cuando alguien no entiende.", "Se piensa que no hay solución.", "Repite más lento o di «Sorry?»."),
    ],
    [
        ("¿Qué significa «You're welcome»?", "De nada", "Se responde a thank you."),
        ("¿Qué significa «dialogue»?", "Diálogo, conversación", "Dos personas hablan por turnos."),
        ("¿Qué quiere decir que un mensaje sea «intelligible»?", "Que se puede entender", "Es lo que más importa al hablar."),
    ],
    [
        ("En «Thank you», ¿qué sonido tiene la primera palabra al comienzo?", "/th/", "Thank empieza con th."),
        ("En «Is this your bag?», ¿qué sonido tiene la palabra is al final?", "/z/", "La s de is suena /z/."),
        ("¿Quién responde «You're welcome»? Escribe A o B.", "A", "A dice You're welcome después de Thank you."),
    ],
    [
        ("Completa: «A: Hello! ___ this your bag?» (es)", "Is", "Is va antes de this."),
        ("Completa: «B: Yes, it ___.» (es)", "is", "Yes, it is es la respuesta corta."),
        ("Completa: «A: You're ___.» (de nada)", "welcome", "You're welcome es de nada."),
    ],
    [
        ("Sofía dice «Tank you» en vez de «Thank you». ¿Qué cambia al decir tank?", "La lengua queda detrás de los dientes y se dice t", "En th la lengua va entre los dientes."),
        ("Un niño dice el diálogo gritando muy rápido y nadie lo entiende. ¿Qué cambias?", "Hablar más lento y claro", "Lo importante es que se entienda."),
    ],
    [
        ("Ordena las tres líneas del diálogo con letras A, B, A: (1) Yes, it is. Thank you! (2) You're welcome. (3) Hello! Is this your bag? Escribe los números en orden.", "3, 1, 2", "Primero se saluda, luego se responde y por último se dice de nada."),
        ("Diálogo: «A: Is this your bag? B: Yes, it is.» Cambia bag por book (libro). Escribe la pregunta de A en inglés.", "Is this your book?", "Se cambia solo la palabra bag por book."),
    ],
    [("Un compañero nuevo encuentra tu mochila en el patio y te la devuelve. Él pregunta «Is this your bag?». Responde en inglés con tres palabras: sí, lo es.", "Yes, it is", "Es la respuesta corta a la pregunta.")],
    [
        ("¿Qué dices si no entiendes algo?", "Sorry?", "Sorry? pide que repitan."),
        ("¿Cómo respondes a «Thank you»?", "You're welcome", "Es la respuesta educada."),
        ("¿Cómo se dice «gracias» en inglés?", "Thank you", "Lleva /th/ al comienzo."),
    ],
    task("Con una persona de tu casa, lee este diálogo por turnos: «A: Hello! Is this your bag? / B: Yes, it is. Thank you! / A: You're welcome.» Hablen despacio. Marcan con lápiz las palabras con /th/, /z/ y /w/. Luego cambian de personaje y lo repiten. Al final, cambien bag por book y dígalo de nuevo.", "Marco this, thank (th), is (z) y welcome (w). Digo el diálogo y luego con book.", ["lee su turno con claridad", "marca los sonidos pedidos", "cambia de personaje", "cambia bag por book y se entiende"], ["el diálogo con marcas", "nota de la persona que lo escuchó"], ["hablar muy rápido", "decir tank por thank"], "Pregunta si se entendió cada línea y celebra la claridad más que el acento."),
    "Di el diálogo en voz baja a un peluche o a una mascota y luego di el otro personaje.",
    "Escribe en español tres consejos para que un mensaje en inglés se entienda mejor.",
)

# ================================================================ OA 11
lesson(
    OA11, 1,
    "Las frases y diálogos escritos en cada ejercicio, un lápiz, una goma y una regla reales si los tienes, y una persona de tu casa para hacer el diálogo.",
    "Aprenderé a pedir y dar objetos de la sala con frases como «Can I have a pencil, please?». Sirve para participar en clase en inglés con frases muy usadas.",
    ["Sé decir hello y thank you.", "Sé nombres de objetos de la sala: pencil, book."],
    [
        "En la sala de clases se piden cosas con una pregunta corta. Se dice «Can I have a pencil, please?» (¿puedo tener un lápiz, por favor?). «Please» significa por favor y se usa para ser amable. Puedes cambiar pencil por otro objeto: eraser (goma), ruler (regla), book (libro). Antes de una palabra que empieza con vocal, como eraser, se usa an (an eraser); antes de pencil, ruler o book se usa a.",
        "Quien tiene el objeto responde: «Sure» (claro) o «Yes» (sí), y lo entrega diciendo «Here you are» (aquí tienes). Quien recibe responde «Thank you» (gracias) y el otro dice «You're welcome» (de nada). Si no tiene el objeto, puede decir «Sorry» (lo siento).",
        "También se puede pedir ayuda: «Can you help me, please?» (¿puedes ayudarme, por favor?). Usa gestos y objetos para que se entienda: muestra el lápiz o señala el objeto. Las frases no tienen que ser largas. Lo importante es pedir, responder y agradecer por turnos.",
    ],
    [("Can I have...?", "¿puedo tener...?"), ("please", "por favor"), ("Here you are", "aquí tienes"), ("Sure", "claro"), ("eraser", "goma de borrar"), ("ruler", "regla")],
    [
        ("Pedir un objeto", "Quieres una goma de borrar. ¿Qué dices a tu compañero?", ["Uso Can I have.", "Digo eraser.", "Agrego please."], "Can I have an eraser, please?"),
        ("Responder y agradecer", "Tu compañero dice «Can I have a ruler, please?». Tú le das la regla. ¿Qué dices, y qué responde él?", ["Digo Here you are.", "Él dice Thank you.", "Yo respondo You're welcome."], "Here you are. / Thank you. / You're welcome."),
    ],
    [
        ("Pedir sin decir please.", "Se olvida la palabra amable.", "Agrega please al final."),
        ("Decir «Give me a pencil».", "Se traduce directo del español y suena mandón.", "Usa Can I have...?"),
    ],
    [
        ("¿Qué significa «please»?", "Por favor", "Es una palabra amable."),
        ("¿Qué significa «Here you are»?", "Aquí tienes", "Se dice al entregar algo."),
        ("¿Cómo se dice «regla» en inglés?", "ruler", "Es el objeto para medir."),
    ],
    [
        ("¿Qué pregunta usas para pedir un lápiz?", "Can I have a pencil, please?", "Es la pregunta amable para pedir."),
        ("¿Qué respondes cuando te dan un objeto?", "Thank you", "Se agradece al recibir."),
        ("Te dicen «Thank you». ¿Qué respondes?", "You're welcome", "Significa de nada."),
    ],
    [
        ("Completa: «Can I ___ a ruler, please?» (tener)", "have", "Have significa tener."),
        ("Completa: «___ you are.» (aquí tienes; escribe la primera palabra)", "Here", "Here you are es aquí tienes."),
        ("Completa: «Can I have a pencil, ___?» (por favor)", "please", "Please es por favor."),
    ],
    [
        ("Un niño dice «Give me a pencil». ¿Cómo lo dices más amable en inglés?", "Can I have a pencil, please?", "La pregunta con please es amable."),
        ("Tu compañera te pide una goma y tú no tienes. ¿Qué respondes? (a) «Sorry.» (b) «You're welcome.»", "a", "Sorry significa lo siento y se usa si no puedes dar algo."),
    ],
    [
        ("Ordena el diálogo con números: (1) Thank you. (2) Can I have a pencil, please? (3) Here you are. (4) You're welcome. Escribe los números en orden.", "2, 3, 1, 4", "Primero se pide, luego se entrega, se agradece y se responde."),
        ("Cambia pencil por ruler en «Can I have a pencil, please?» y escribe la pregunta completa.", "Can I have a ruler, please?", "Se cambia solo el objeto."),
    ],
    [("En clase de arte necesitas una regla y tu compañero tiene dos. Elige lo que le dices en inglés: (a) «Can I have a ruler, please?» (b) «Here you are.»", "a", "Es la pregunta para pedir el objeto.")],
    [
        ("¿Cómo se dice «goma de borrar» en inglés?", "eraser", "Es el objeto para borrar."),
        ("¿Qué significa «Can you help me, please?»", "¿Puedes ayudarme, por favor?", "Es una petición de ayuda."),
        ("¿Qué palabra muestra amabilidad al pedir?", "please", "Please es por favor."),
    ],
    task("Con una persona de tu casa, hagan este diálogo tres veces, cambiando el objeto cada vez: pencil, eraser, ruler. Tú pides: «Can I have a pencil, please?» La otra persona responde «Sure. Here you are.» Tú dices «Thank you.» Ella dice «You're welcome.» Usa un objeto real o un dibujo en un papel. Después cambien de rol.", "«Can I have an eraser, please?» «Sure. Here you are.» «Thank you.» «You're welcome.»", ["pide con Can I have...", "dice please", "agradece", "responde You're welcome al cambiar de rol"], ["nota de la persona que hizo el diálogo con él o ella"], ["olvidar please", "decir Give me"], "Muestra el objeto cuando falte la palabra y celebra que use frases amables."),
    "Di Can I have a pencil, please? mirando un lápiz de tu casa.",
    "Escribe un diálogo de tres líneas para pedir una goma y entregarla.",
)

lesson(
    OA11, 2,
    "Las fichas de personajes escritas en cada ejercicio, lápiz y una persona de tu casa. Los personajes son inventados.",
    "Aprenderé a presentar a una persona inventada con frases como «This is Lola. She is eight. She is from Peru.» Sirve para hablar de otra persona y dar solo información segura.",
    ["Sé decir My name is... y I'm...", "Sé que she es ella y he es él."],
    [
        "Para presentar a otra persona, usa «This is...» (esta es / este es). Si es una niña, sigue con she (ella): «This is Lola. She is eight.» Si es un niño, sigue con he (él): «This is Tom. He is nine.» En inglés se dice «She is eight» o «He is nine» para decir la edad (ella tiene ocho, él tiene nueve).",
        "Para decir de dónde es: «She is from Peru» (ella es de Perú). Para decir lo que le gusta, agrega una s al verbo like: «She likes music» (le gusta la música), «He likes soccer» (le gusta el fútbol). Esa s solo se usa con he y she. Con I se dice «I like». Para hablar de ti puedes decir «I'm Lola. I'm eight.» (I'm es la forma corta de I am: yo soy; yo tengo ocho años). En este cuaderno usamos «soccer» para el fútbol, que es la palabra de Estados Unidos; en Inglaterra y en otros países se dice «football».",
        "Estos personajes son inventados, por eso no importa compartir sus datos. Cuando hables de personas reales, no digas dirección, teléfono ni colegio. Una buena presentación es clara y corta: nombre, edad, país y un gusto. Termina con «Thank you» para cerrar.",
    ],
    [("This is...", "esta es... / este es..."), ("She is / He is", "ella es / él es"), ("from", "de, de origen"), ("She likes...", "a ella le gusta..."), ("He likes...", "a él le gusta..."), ("soccer", "fútbol")],
    [
        ("Presentar a una niña", "Ficha: Lola, 8 años, de Perú, le gusta la música. Preséntala con cuatro frases.", ["Uso This is para el nombre.", "Para la edad y el país uso She is.", "Para el gusto uso She likes."], "This is Lola. She is eight. She is from Peru. She likes music."),
        ("Presentar a un niño", "Ficha: Tom, 9 años, de México, le gusta el fútbol. Preséntalo con cuatro frases.", ["Uso This is Tom.", "Uso He is para la edad y el país.", "Uso He likes para el gusto."], "This is Tom. He is nine. He is from Mexico. He likes soccer."),
    ],
    [
        ("Decir «She like music» sin la s.", "Se olvida la s con she.", "Con she y he se agrega s: likes."),
        ("Decir «This is Tom. She is nine.»", "Se confunde he con she.", "Tom es un niño, así que va He is."),
    ],
    [
        ("¿Qué significa «This is Lola»?", "Esta es Lola", "This is presenta a alguien."),
        ("¿Qué pronombre usas para un niño, he o she?", "he", "He es él."),
        ("¿Qué significa «She is from Peru»?", "Ella es de Perú", "From indica el origen."),
    ],
    [
        ("¿Qué datos de una persona real no compartes con desconocidos?", "Dirección, teléfono y colegio", "Son datos privados."),
        ("¿Cuándo se agrega la s a like?", "Con he y she", "Se dice likes con he y she."),
        ("¿Por qué se pueden compartir todos los datos de los personajes de esta clase?", "Porque son inventados", "No son personas reales."),
    ],
    [
        ("Completa: «This ___ Lola.» (es)", "is", "This is presenta a alguien."),
        ("Completa: «He ___ nine.» (él tiene nueve años)", "is", "Con he se usa is: He is nine."),
        ("Completa: «She ___ music.» (le gusta)", "likes", "Con she se usa likes."),
    ],
    [
        ("Marta dice «This is Tom. She is nine.» ¿Qué palabra cambia?", "She por He", "Tom es un niño."),
        ("Leo dice «This is Lola. She like music.» ¿Qué falta?", "La s en likes", "Con she se dice likes."),
    ],
    [
        ("Ficha: Sara, 7 años, de España, le gusta el arte. Escribe la primera frase para presentarla.", "This is Sara.", "Se usa This is y el nombre."),
        ("Ficha: Pablo, 9 años. Escribe la frase que dice su edad (nueve).", "He is nine.", "Pablo es un niño, así que va He is."),
    ],
    [("Eres el presentador de un club de lectura. Presentas al personaje inventado Tom, de México. Escribe la frase que dice de dónde es.", "He is from Mexico.", "Tom es un niño; se usa He is from.")],
    [
        ("¿Cómo se dice «fútbol» (en esta clase) en inglés?", "soccer", "Es la palabra que usamos aquí."),
        ("¿Qué significa «He likes soccer»?", "A él le gusta el fútbol", "Likes lleva s con he."),
        ("¿Qué significa «I'm eight»?", "Tengo ocho años", "I'm es I am; sirve para hablar de mí."),
    ],
    task("Presenta en voz alta a estos dos personajes inventados a una persona de tu casa. Ficha 1: Lola, 8 años, de Perú, le gusta la música. Ficha 2: Tom, 9 años, de México, le gusta el fútbol (soccer). Usa «This is...», «She is...» o «He is...», «from» y «likes». Termina con «Thank you.» Si quieres, dibuja a cada personaje.", "«This is Lola. She is eight. She is from Peru. She likes music. Thank you.»", ["presenta a los dos personajes", "usa she y he correctamente", "dice from y likes", "termina con Thank you"], ["el dibujo", "nota de la persona que escuchó"], ["decir She like", "confundir he con she"], "Valora cada dato dicho y repite con él o ella la frase que le costó."),
    "Di en voz alta cuatro frases para presentar a un personaje inventado de un libro o dibujo que conozcas.",
    "Escribe en inglés dos frases para presentar a un personaje inventado de una película, sin datos reales.",
)

lesson(
    OA11, 3,
    "Las frases escritas en cada ejercicio y una persona de tu casa para el diálogo. Puedes usar un cuaderno con dibujos.",
    "Aprenderé a preguntar cómo se dice una palabra en inglés y a pedir que repitan, con frases como «How do you say...?». Sirve para participar en clase cuando me falta una palabra.",
    ["Sé decir Can I have...? y Thank you.", "Sé que book es libro y door es puerta."],
    [
        "A todos nos falta una palabra a veces. Por eso hay frases para pedir ayuda. Para saber cómo se dice una palabra, pregunta: «How do you say \"puerta\" in English?» (¿cómo se dice «puerta» en inglés?). La otra persona responde: «It's \"door\"» (es «door»).",
        "Si no sabes qué significa una palabra, pregunta: «What does \"door\" mean?» (¿qué significa «door»?). Si no oíste bien, pide: «Can you repeat, please?» (¿puedes repetir, por favor?). Y si no entiendes, puedes decir: «I don't understand» (no entiendo). Si no sabes algo, dices: «I don't know» (no sé).",
        "Estas frases son útiles y son parte de hablar un idioma nuevo. Pedir ayuda no es un error: es una estrategia. También puedes ayudarte señalando un objeto, haciendo un gesto o mostrando un dibujo. Cuando recibas la palabra, repítela y agradece: «Thank you!».",
    ],
    [("How do you say...?", "¿cómo se dice...?"), ("What does... mean?", "¿qué significa...?"), ("Can you repeat, please?", "¿puedes repetir, por favor?"), ("I don't understand", "no entiendo"), ("I don't know", "no sé"), ("door", "puerta")],
    [
        ("Pedir una palabra", "No sabes cómo se dice «mesa» en inglés. ¿Qué preguntas?", ["Uso How do you say.", "Escribo la palabra en español: mesa.", "Agrego in English."], "How do you say \"mesa\" in English?"),
        ("Pedir que repitan", "No oíste una palabra de la profesora. ¿Qué dices?", ["Uso Can you repeat.", "Agrego please.", "Digo la frase completa."], "Can you repeat, please?"),
    ],
    [
        ("Quedarse callado cuando falta una palabra.", "Se piensa que hay que saber todo.", "Pregunta con How do you say...?"),
        ("Decir solo «What?» para pedir que repitan.", "Suena brusco en inglés.", "Di Can you repeat, please?"),
    ],
    [
        ("¿Qué significa «How do you say...?»", "¿Cómo se dice...?", "Se usa cuando falta una palabra."),
        ("¿Qué significa «I don't understand»?", "No entiendo", "Don't significa no."),
        ("¿Qué significa «door»?", "Puerta", "Es la palabra inglesa para puerta."),
    ],
    [
        ("¿Qué preguntas si quieres saber el significado de «door»?", "What does \"door\" mean?", "Esa pregunta pide el significado."),
        ("¿Qué dices si no oíste bien?", "Can you repeat, please?", "Pide repetir con amabilidad."),
        ("¿Pedir ayuda es un error?", "No", "Es una estrategia para hablar un idioma nuevo."),
    ],
    [
        ("Completa: «How do you ___ \"libro\" in English?» (decir)", "say", "Say es decir."),
        ("Completa: «It's ___.» (la respuesta a cómo se dice «puerta»)", "door", "Door es puerta."),
        ("Completa: «I don't ___.» (entiendo)", "understand", "Understand es entender."),
    ],
    [
        ("Un niño dice solo «What?» para pedir que repitan. ¿Qué frase más amable usas?", "Can you repeat, please?", "La frase con please es más amable."),
        ("Tu compañera pregunta «How do you say \"silla\" in English?». Tú sabes que es chair. ¿Qué respondes?", "It's \"chair\"", "It's seguido de la palabra responde la pregunta."),
    ],
    [
        ("Diálogo: «A: How do you say \"ventana\" in English? B: It's \"window\".» ¿Qué palabra en inglés recibió A?", "window", "B respondió It's window."),
        ("Ordena la conversación con números: (1) It's \"door\". (2) Thank you! (3) How do you say \"puerta\" in English? Escribe los números en orden.", "3, 1, 2", "Primero se pregunta, luego se responde y por último se agradece."),
    ],
    [("En una clase de ciencias la profesora dice una palabra que no entiendes. Elige lo que dices: (a) «Can you repeat, please?» (b) «Thank you!»", "a", "Es la frase para pedir que repitan.")],
    [
        ("¿Cómo se dice «¿puedes repetir, por favor?» en inglés?", "Can you repeat, please?", "Es la frase para pedir repetición."),
        ("¿Qué significa «I don't know»?", "No sé", "Se usa cuando no sabes la respuesta."),
        ("Cuando recibes la palabra, ¿qué haces?", "La repito y agradezco", "Repetir ayuda a recordar y agradecer es amable."),
    ],
    task("Con una persona de tu casa, haz este diálogo con tres objetos de la casa o de otra asignatura (por ejemplo, una puerta, una mesa, una silla o una figura de Matemática como un círculo, circle). Señala cada objeto y pregunta: «How do you say \"puerta\" in English?» Tu pareja responde «It's \"door\"» (o «table», «chair»). Si no oyes, pide: «Can you repeat, please?» Repite la palabra y di «Thank you!».", "«How do you say \"mesa\" in English?» «It's \"table\".» «Table. Thank you!»", ["usa How do you say...?", "pide repetición con Can you repeat, please?", "repite la palabra recibida", "agradece"], ["nota de la persona que lo escuchó"], ["quedarse callado", "decir solo What?"], "Celebra que pidió ayuda y repite la palabra con él o ella."),
    "Señala tres objetos de tu casa y pregunta en inglés cómo se dicen.",
    "Escribe un mini diálogo de tres líneas para pedir y recibir una palabra.",
)

lesson(
    OA11, 4,
    "Las fichas escritas en cada ejercicio, lápiz y una hoja para dibujar. Una persona de tu casa para escuchar.",
    "Aprenderé a hacer una presentación muy corta de un animal con una imagen de apoyo, usando «This is...», «It is...» e «It can...». Sirve para exponer frente a otros con ayuda de una imagen.",
    ["Sé decir This is... y She is/He is...", "Sé algunos colores y animales."],
    [
        "Una presentación (presentation) es hablar de un tema con una imagen que ayuda. Una presentación breve tiene cuatro partes: saludo, tema, datos y cierre. Ejemplo con una imagen de una abeja: «Hello! This is a bee. It is small. It is yellow and black. It can fly. Thank you!» (¡Hola! Esta es una abeja. Es pequeña. Es amarilla y negra. Puede volar. ¡Gracias!)",
        "Para el tema usa «This is a...» (esto es un/una...). Para describir usa «It is...» seguido de una característica: small (pequeño), big (grande), yellow (amarillo), black (negro). Para decir lo que puede hacer usa «It can...»: fly (volar), swim (nadar), run (correr). Antes de bee o dog se usa «a»: a bee, a dog. También puedes presentar algo de otra asignatura. En Matemática: «This is a circle. It is red.» (círculo; rojo). Otras figuras son square (cuadrado) y triangle (triángulo).",
        "Usa la imagen: señala la parte de la que hablas, mira a quienes te escuchan y habla despacio. Si olvidas una palabra, mira la imagen o di «Sorry» y empieza otra vez. Una presentación muy breve tiene tres o cuatro datos. Tu profesora o profesor te ayudará con la palabra que falte.",
    ],
    [("presentation", "presentación"), ("This is a...", "esto es un/una..."), ("It is...", "es..."), ("It can...", "puede..."), ("fly", "volar"), ("small", "pequeño")],
    [
        ("Armar una presentación", "Imagen: [una abeja amarilla y negra volando]. Datos: abeja, pequeña, amarilla y negra, vuela. ¿Qué dices en cuatro frases?", ["Saludo y tema: Hello! This is a bee.", "Describo: It is small. It is yellow and black.", "Digo lo que puede hacer: It can fly."], "Hello! This is a bee. It is small. It is yellow and black. It can fly."),
        ("Usar la imagen", "Estás en la presentación y olvidas la palabra bee. La imagen muestra la abeja. ¿Qué haces?", ["Miro la imagen.", "Reconozco el dibujo.", "Digo la palabra y sigo."], "Miro la imagen, recuerdo bee y sigo."),
    ],
    [
        ("Hablar sin mirar a nadie y sin usar la imagen.", "Se piensa que la imagen es solo decoración.", "Señala la imagen y mira a quienes te escuchan."),
        ("Decir «It can to fly».", "Se agrega to por traducción.", "Después de can va el verbo solo: It can fly."),
    ],
    [
        ("¿Qué significa «This is a bee»?", "Esta es una abeja", "This is presenta el tema."),
        ("¿Qué significa «It can fly»?", "Puede volar", "Can es poder."),
        ("¿Cómo se dice «pequeño» en inglés?", "small", "Es lo contrario de big."),
    ],
    [
        ("¿Cuáles son las cuatro partes de una presentación breve?", "Saludo, tema, datos y cierre", "Así queda ordenada."),
        ("¿Para qué sirve la imagen en una presentación?", "Para ayudar a hablar y a que se entienda", "La imagen da apoyo a quien expone."),
        ("¿Qué haces si olvidas una palabra?", "Miro la imagen o empiezo otra vez", "Hay estrategias para continuar."),
    ],
    [
        ("Completa: «This ___ a bee.» (es)", "is", "This is presenta el tema."),
        ("Completa: «It ___ fly.» (puede)", "can", "Can significa poder."),
        ("Completa: «It is ___ and black.» (amarillo)", "yellow", "Yellow es amarillo."),
    ],
    [
        ("Un niño dice «It can to fly». ¿Qué palabra sobra?", "to", "Después de can va el verbo solo."),
        ("Una niña empieza su presentación con «Thank you!». ¿Qué parte falta al comienzo?", "El saludo, Hello", "Thank you es el cierre."),
    ],
    [
        ("Ficha: [una tortuga verde que nada]. Datos: tortuga (turtle), verde (green), nada (swim). Escribe la frase que dice qué puede hacer.", "It can swim.", "Se usa It can y el verbo solo."),
        ("En Matemática: ficha [un cuadrado azul]. Completa: «This is a ___. It is blue.» (cuadrado)", "square", "Square es cuadrado."),
    ],
    [("Hoy te toca exponer sobre un animal en ciencias, con una imagen de un loro verde que puede volar (parrot es loro). Escribe la frase de saludo y tema en inglés: Hello, este es un loro.", "Hello! This is a parrot.", "Se saluda y se presenta el tema con This is a.")],
    [
        ("¿Cómo se dice «presentación» en inglés?", "presentation", "Es la palabra para exponer."),
        ("¿Qué frase cierra una presentación?", "Thank you!", "Es una forma amable de terminar."),
        ("¿Qué significa «It is yellow»?", "Es amarillo", "It is describe un color."),
    ],
    task("Con la ficha «bee», prepara y di tu presentación a una persona de tu casa: Hello! This is a bee. It is small. It is yellow and black. It can fly. Thank you! Dibuja la abeja para usarla como apoyo y señálala mientras hablas. Después haz otra presentación con una ficha nueva: «a turtle: green, can swim». Por último, en Matemática, presenta un círculo rojo (circle, red). Escribe antes los datos en inglés.", "«Hello! This is a turtle. It is green. It can swim. Thank you!» / «Hello! This is a circle. It is red. Thank you!»", ["usa saludo, tema, datos y cierre", "usa this is, it is, it can", "usa la imagen o el dibujo", "habla despacio y mira a quien escucha"], ["el dibujo de apoyo", "nota de la persona que escuchó"], ["decir It can to", "no usar la imagen"], "Pregunta qué dato le gustó y celebra el cierre y la voz clara."),
    "Presenta un animal que te guste a un peluche, con las cuatro partes.",
    "Dibuja otro animal y escribe tres frases en inglés con This is, It is e It can.",
)

lesson(
    OA11, 5,
    "Las fichas y preguntas escritas en cada ejercicio, lápiz y una persona de tu casa que haga las preguntas.",
    "Aprenderé a responder preguntas que me hacen después de mi presentación, con respuestas cortas como «Yes, it is» o «No, it isn't». Sirve para adaptarme a lo que preguntan.",
    ["Sé hacer una presentación con This is..., It is... e It can...", "Sé responder con Yes y No."],
    [
        "Después de una presentación, el público puede hacer una pregunta de seguimiento (follow-up question). Por ejemplo, si presentaste una abeja: «Is it big?» (¿es grande?). Respondes con una respuesta corta: «No, it isn't. It is small» (no, no lo es. Es pequeña). Si la respuesta es sí, dices «Yes, it is».",
        "Hay tres tipos de preguntas. Con is: «Is it big?» → «Yes, it is» o «No, it isn't». Con can: «Can it fly?» → «Yes, it can» o «No, it can't» (no puede). Con color: «What color is it?» (¿de qué color es?) → «It's yellow and black» (es amarilla y negra). «It's» es una forma corta de «it is» y «isn't» es una forma corta de «is not».",
        "Para responder bien, escucha la primera palabra de la pregunta (Is, Can o What color) y elige la respuesta que corresponde. Si no entiendes, pide: «Can you repeat, please?». Si no sabes, puedes decir «I don't know». No necesitas hablar mucho; basta una respuesta corta y clara.",
    ],
    [("follow-up question", "pregunta de seguimiento"), ("Is it big?", "¿es grande?"), ("Yes, it is", "sí, lo es"), ("No, it isn't", "no, no lo es"), ("Yes, it can / No, it can't", "sí puede / no puede"), ("What color is it?", "¿de qué color es?")],
    [
        ("Responder con is", "Presentaste una abeja pequeña. Te preguntan «Is it big?». ¿Qué respondes?", ["La abeja es pequeña.", "La respuesta es no.", "Uso No, it isn't."], "No, it isn't. It is small."),
        ("Responder con can", "Te preguntan «Can it swim?» sobre la abeja, que no nada. ¿Qué respondes?", ["La pregunta usa Can.", "La abeja no nada.", "Uso No, it can't."], "No, it can't."),
    ],
    [
        ("Responder «Yes, it can» a una pregunta con is.", "Se mezcla la respuesta con la pregunta.", "Escucha la primera palabra: Is → it is; Can → it can."),
        ("Quedarse callado si no entiende.", "Se piensa que hay que saber todo.", "Pide: Can you repeat, please?"),
    ],
    [
        ("¿Qué significa «Is it big?»", "¿Es grande?", "Pregunta por una característica."),
        ("¿Qué significa «No, it isn't»?", "No, no lo es", "Isn't es is not."),
        ("¿Qué significa «No, it can't»?", "No, no puede", "Can't es no puede."),
    ],
    [
        ("Te preguntan «Is it yellow?» sobre una abeja amarilla. ¿Qué respondes?", "Yes, it is", "Is it se responde con it is."),
        ("Te preguntan «Can it fly?» sobre una abeja. ¿Qué respondes?", "Yes, it can", "Can it se responde con it can."),
        ("Te preguntan «What color is it?» sobre una abeja amarilla y negra. ¿Qué respondes?", "It's yellow and black", "La pregunta pide el color."),
    ],
    [
        ("Completa: «Is it big?» «No, it ___.» (no lo es)", "isn't", "Isn't es la forma corta de is not."),
        ("Completa: «Can it swim?» «No, it ___.» (no puede)", "can't", "Can't es la forma corta de can not."),
        ("Completa: «What color is it?» «It's ___.» (verde)", "green", "Green es verde."),
    ],
    [
        ("Alguien pregunta «Can it fly?» sobre un perro y respondes «Yes, it is». ¿Qué cambias?", "Debe ser No, it can't", "Un perro no vuela y la respuesta usa can."),
        ("Te preguntan «Is it small?» sobre una abeja. Respondes «Yes, it can». ¿Qué palabra corriges?", "can por is", "La pregunta usa is, así que la respuesta usa is."),
    ],
    [
        ("Ficha: [una tortuga verde que nada, pero no vuela]. Pregunta: «Can it fly?» Escribe la respuesta corta.", "No, it can't.", "La tortuga no vuela; la pregunta usa can."),
        ("Ficha: [una tortuga verde]. Pregunta: «Is it green?» Escribe la respuesta corta.", "Yes, it is.", "La tortuga es verde y la pregunta usa is."),
    ],
    [("Presentas un loro verde que puede volar. Un compañero pregunta «Is it green?». Responde en inglés con tres palabras.", "Yes, it is", "El loro es verde; la pregunta usa is.")],
    [
        ("¿Qué dices para pedir con amabilidad que repitan?", "Can you repeat, please?", "Se pide repetir con amabilidad."),
        ("¿Qué palabra de la pregunta te dice cómo responder?", "La primera palabra", "Is, Can o What color indican qué responder."),
        ("¿Qué significa «follow-up question»?", "Pregunta de seguimiento", "Es una pregunta después de la presentación."),
    ],
    task("Presenta un animal con tu ficha («This is a turtle. It is small. It is green. It can swim.»). Una persona de tu casa te hace tres preguntas: «Is it big?», «Can it fly?» y «What color is it?» Responde con respuestas cortas: «No, it isn't» (o «Yes, it is»), «No, it can't» y «It's green». Si no entiendes, pide «Can you repeat, please?». Luego cambien de rol.", "«Is it big?» «No, it isn't.» «Can it fly?» «No, it can't.» «What color is it?» «It's green.»", ["responde con is, can y color", "usa respuestas cortas", "pide repetición si no entiende", "cambia de rol"], ["nota de la persona que hizo las preguntas"], ["mezclar is y can", "quedarse callado"], "Celebra la respuesta corta y ayuda a identificar la primera palabra de cada pregunta."),
    "Haz tres preguntas con Is it, Can it y What color a un peluche y respóndelas tú.",
    "Escribe tres preguntas de seguimiento y sus respuestas cortas para un animal que elijas.",
)

"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 22 (obras literarias escuchadas) y OA 23 (comprensión de textos orales)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA22, OA23 = "LE02 OA 22", "LE02 OA 23"
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


# ================================================================ OA 22 · clase 1
reg(
    OA22, 1,
    "El cuento de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja para dibujar o anotar.",
    "Aprenderé a prepararme para escuchar una historia: mirar el título, pensar de qué trata y escuchar con atención. Sirve para disfrutar y comprender mejor las obras.",
    ["Sé escuchar a un adulto que lee.", "Sé qué es un título."],
    [
        "Antes de escuchar un cuento, un poema o una fábula, conviene prepararse. Siéntate cómodo y haz silencio. Mira el título y, si hay, la ilustración. Con esas pistas piensa de qué podría tratar la historia. Eso se llama anticipar.",
        "Anticipar es imaginar una posibilidad, no adivinar el final. Si la historia dice algo distinto, no pasa nada: cambias tu idea. Por ejemplo, el título «El zorro y la luna del estanque» te hace pensar en un zorro que mira la luna en el agua. Escucha para comprobar si es así.",
        "Mientras escuchas, pon atención en los personajes, en qué pasa y en cómo suena la voz. Al terminar, vuelve a tu idea del comienzo y mira si coincidió o cambió.",
        "Hay dos clases de cuentos. Los cuentos folclóricos se han contado en voz alta por mucho tiempo, de persona en persona, y no se sabe quién los inventó. Suelen empezar con «Había una vez», a menudo repiten algo y terminan con una fórmula como «Colorín colorado, este cuento se ha acabado». Los cuentos de autor los escribió una persona que sabemos quién es. El cuento del zorro de este cuaderno es nuevo: está escrito para este cuaderno al estilo de los cuentos folclóricos.",
    ],
    [("anticipar", "pensar de qué puede tratar una historia antes de escucharla"), ("título", "el nombre de una obra"), ("posibilidad", "algo que puede pasar"), ("personaje", "quien actúa en una historia"), ("comprobar", "revisar si lo que pensé era cierto"), ("cuento folclórico", "cuento que se contó de boca en boca y cuyo autor no se conoce"), ("cuento de autor", "cuento que escribió una persona que se conoce")],
    [
        ("Anticipar con el título", "El título es «El zorro y la luna del estanque». ¿De qué podría tratar?", ["Miro el título: aparecen un zorro, la luna y un estanque.", "Pienso: quizás el zorro ve la luna en el agua.", "Es una posibilidad que comprobaré."], "Podría tratar de un zorro que ve la luna reflejada en un estanque."),
        ("Comprobar después de escuchar", "El cuento dice: «Había una vez un zorro muy goloso. Una noche vio la luna en el agua de un estanque. "
         "¡Qué queso redondo!, pensó. Metió la pata para sacarlo y la luna se rompió en mil ondas. Lo intentó otra vez, y otra, y otra, pero siempre pasaba lo mismo. Cuando el agua quedó quieta, la luna volvió a aparecer. El zorro comprendió que era un reflejo. Colorín colorado, este cuento se ha acabado». ¿Coincidió la anticipación?",
         ["Mi idea: el zorro ve la luna en el agua.", "El cuento dice que vio la luna en el agua de un estanque.", "Además, pensó que era un queso. Y empieza con «Había una vez», como muchos cuentos folclóricos."], "Sí coincidió; además aprendí que el zorro creyó que era un queso."),
    ],
    [("Pensar que mi idea del comienzo debe ser igual al cuento.", "Se cree que anticipar es acertar.", "Una anticipación es una posibilidad; si el cuento cambia, cambio mi idea."), ("Hablar mientras alguien lee.", "Se quiere decir lo que se piensa.", "Espera al final para conversar.")],
    [
        E("¿Qué significa anticipar?", "Pensar de qué puede tratar la historia antes de escucharla", "Se usan pistas como el título."),
        E("¿Cuál es un comienzo típico de un cuento folclórico: «Había una vez…» o «Hoy a las ocho…»?", "Había una vez…", "Muchos cuentos folclóricos empiezan así."),
        E("En el título «El zorro y la luna del estanque», ¿qué animal aparece?", "El zorro", "Está nombrado en el título."),
    ],
    [
        E("Un niño dice: «Creo que habla de un zorro que ve la luna». ¿Anticipó o resumió?", "Anticipó", "Todavía no escuchó la historia."),
        E("Si la historia dice algo distinto de lo que pensé, ¿debo cambiar mi idea?", "Sí", "Una anticipación es solo una posibilidad."),
        E("En un cuento folclórico, ¿se sabe quién lo inventó?", "No", "Pasó de persona en persona por mucho tiempo."),
    ],
    [
        E("El título es «La tortuga que quería volar». ¿Qué personaje aparece?", "La tortuga", "Está en el título."),
        E("Con ese título, ¿qué posibilidad encaja: a) la tortuga intenta volar o b) la tortuga hace una torta?", "a", "El título habla de querer volar."),
        E("Ordena: A) escuchar la historia, B) pensar de qué trata, C) mirar el título.", "C, B, A", "Primero miro, luego pienso y después escucho."),
    ],
    [
        E("Luis dice: «Ya sé el final, no escucho». ¿Está bien?", "No, porque lo que pensó puede cambiar y debe escuchar hasta el final", "Anticipar no es saber el final."),
        E("Un libro dice en su tapa: «Cuento escrito por Elena Rojas». ¿Es un cuento folclórico o un cuento de autor?", "Un cuento de autor", "Se sabe quién lo escribió."),
    ],
    [
        E("En el cuento del zorro, ¿qué creyó el zorro que era la luna del agua?", "Un queso redondo", "El texto dice «¡Qué queso redondo!»."),
        arith("El zorro intentó sacar la luna 1 vez y después lo intentó otras 3 veces (otra vez, y otra, y otra). ¿Cuántos intentos hizo en total?", "1+3", "Se suma el primer intento a los que siguieron."),
    ],
    [E("Tu abuela te contará un cuento llamado «El pájaro que perdió su canto». Empieza con «Había una vez». ¿Qué pregunta puedes hacerte antes de escuchar?", "¿Qué le pasó al pájaro? o ¿Cómo recuperará su canto?", "Las preguntas surgen del título.")],
    [
        E("¿Qué hago al terminar la historia con mi anticipación?", "Reviso si coincidió o cambió", "Así compruebo mi idea."),
        E("¿Una anticipación es una posibilidad o una verdad segura?", "Una posibilidad", "Puede cambiar al escuchar."),
        E("¿Qué miro además del título para anticipar?", "La ilustración", "También da pistas."),
    ],
    ("Anticipa con estos tres títulos y escribe una oración para cada uno: 1) «El oso que no podía dormir». 2) «La niña y el río cantor». 3) «El gato del faro». Luego un adulto lee este mini cuento y compara con tu anticipación del título 1: «Un oso quería dormir su siesta, pero el viento movía las ramas y hacía ruido. El oso se fue a una cueva y por fin durmió».",
     "1) El oso intenta dormir y algo se lo impide. 2) Una niña descubre que el río suena como una canción. 3) Un gato vive en un faro y quizá vea los barcos. Comparación: sí coincidió, el oso no podía dormir por el ruido del viento.",
     ["escribe una anticipación para cada título", "usa el título como pista", "compara con lo escuchado"], ["hoja con tres anticipaciones y una comparación"], ["decir cómo termina la historia", "no basarse en el título"],
     "Pregunta: «¿Qué palabra del título te dio la pista?». Aclara que puede equivocarse sin problema."),
    "Antes de que tu familia te cuente un cuento, dime de qué crees que tratará por el título.",
    "Inventa un título de cuento y pide a alguien que anticipe de qué trata.",
)

# ================================================================ OA 22 · clase 2
reg(
    OA22, 2,
    "El cuento de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a seguir el hilo de una historia: reconocer qué pasa primero, después y al final. Sirve para comprender cuentos y recordarlos.",
    ["Sé anticipar a partir del título.", "Sé qué son los personajes."],
    [
        "Una historia se cuenta en partes. Cada parte donde ocurre algo se llama episodio. Seguir el hilo es entender cómo un episodio lleva al siguiente. Para eso escucha las palabras de orden, como primero, después, al final.",
        "Escucha este cuento. «Tomasa, la tortuga, quiso ir a la feria del pueblo. Primero cruzó el río apoyándose en un tronco. Después subió la loma muy despacio. Al llegar, la feria ya había terminado, pero un niño le regaló una manzana. Tomasa volvió a casa contenta». Hay tres episodios: cruzar el río, subir la loma y llegar a la feria.",
        "Para recordar la historia, di qué hizo el personaje en cada parte. Así no pierdes el hilo y puedes contarla a otra persona. El cuento de Tomasa es un cuento de autor: alguien lo escribió, no pasó de boca en boca como los cuentos folclóricos.",
    ],
    [("episodio", "parte de una historia donde pasa algo"), ("hilo", "orden en que ocurren las cosas"), ("primero, después, al final", "palabras que muestran el orden"), ("personaje", "quien actúa en la historia"), ("resumir", "contar lo más importante en pocas palabras")],
    [
        ("Ordenar los episodios", "En el cuento de Tomasa, ¿qué hizo primero y qué hizo después?", ["Busco la palabra «primero»: cruzó el río.", "Busco «después»: subió la loma."], "Primero cruzó el río y después subió la loma."),
        ("Resumir", "Cuenta el cuento de Tomasa en una oración.", ["Digo quién es: Tomasa, la tortuga.", "Digo qué pasó: fue a la feria, cruzó el río y subió la loma.", "Digo cómo terminó: un niño le regaló una manzana."], "Tomasa fue a la feria, cruzó el río y subió la loma; llegó tarde, pero un niño le regaló una manzana."),
    ],
    [("Contar los hechos desordenados.", "No se escuchan las palabras de orden.", "Busca primero, después y al final."), ("Olvidar el final.", "Se pierde atención al terminar.", "Escucha hasta la última oración.")],
    [
        E("En el cuento, ¿quién quiso ir a la feria?", "Tomasa, la tortuga", "El cuento empieza con ella."),
        E("¿Qué cruzó primero Tomasa?", "El río", "Dice «Primero cruzó el río»."),
        E("¿Qué le regaló el niño a Tomasa?", "Una manzana", "Aparece en el final del cuento."),
    ],
    [
        E("¿Qué es un episodio?", "Una parte de la historia donde pasa algo", "Cada episodio cuenta un hecho."),
        E("¿Qué hizo Tomasa después de cruzar el río?", "Subió la loma", "El cuento dice «Después subió la loma»."),
        E("¿Cuántos lugares recorre Tomasa antes de llegar a la feria: el río y la loma?", "2", "El río y la loma."),
    ],
    [
        E("Ordena: A) volvió a casa contenta, B) cruzó el río, C) subió la loma.", "B, C, A", "Es el orden del cuento."),
        E("El cuento de Tomasa lo escribió una persona para este cuaderno. ¿Es un cuento folclórico o un cuento de autor?", "Un cuento de autor", "Tiene una persona que lo escribió."),
        E("¿Cómo se sintió Tomasa al final?", "Contenta", "El cuento dice que volvió contenta."),
    ],
    [
        E("La feria terminó, pero Tomasa volvió contenta. ¿Por qué?", "Porque un niño le regaló una manzana", "El regalo la alegró."),
        E("Pedro dice que Tomasa subió la loma antes de cruzar el río. ¿Tiene razón?", "No, porque primero cruzó el río", "Es el orden del cuento."),
    ],
    [
        E("Resume el cuento en una oración con las palabras fue, cruzó, subió y manzana.", "Tomasa fue a la feria, cruzó el río, subió la loma y recibió una manzana.", "El resumen incluye los hechos principales."),
        arith("Tomasa tiene 3 episodios en su camino. Ya contaste 2. ¿Cuántos faltan?", "3-2", "Se resta lo contado del total."),
    ],
    [E("Alguien te cuenta: «Primero preparó la masa, después hizo bolitas y al final las horneó». ¿Qué hizo después de preparar la masa?", "Hizo bolitas", "La palabra «después» lo indica.")],
    [
        E("¿Qué palabras me ayudan a ordenar los hechos?", "Primero, después y al final", "Marcan el orden."),
        E("¿Un resumen cuenta todos los detalles o lo más importante?", "Lo más importante", "Resumir es contar en pocas palabras."),
        E("¿Qué debo hacer para no perder el hilo?", "Escuchar con atención y decir qué pasó en cada parte", "Así sigo los episodios."),
    ],
    ("Un adulto te lee este cuento: «Pablo encontró un pajarito en el patio. Primero lo miró sin tocarlo. Después le dejó agua y migas de pan. Al final, el pajarito ya no estaba, y Pablo sonrió porque había volado». Escribe los tres episodios en orden y un resumen de una oración.",
     "1) Pablo miró al pajarito sin tocarlo. 2) Le dejó agua y migas. 3) Al final el pajarito había volado. Resumen: Pablo cuidó a un pajarito hasta que pudo volar.",
     ["escribe los tres episodios en orden", "usa primero, después y al final", "resume en una oración"], ["hoja con tres episodios y un resumen"], ["cambiar el orden", "no escribir el final"],
     "Pide que cuente el cuento a otra persona usando primero, después y al final."),
    "Cuéntale a alguien lo que hiciste hoy con primero, después y al final.",
    "Escucha un cuento largo y escribe sus episodios principales en una lista.",
)

# ================================================================ OA 22 · clase 3
reg(
    OA22, 3,
    "El poema de este cuaderno, que un adulto lee despacio. Lápiz, hoja y colores si quieres dibujar.",
    "Aprenderé a imaginar imágenes cuando escucho un poema. Sirve para disfrutar cómo la voz y las palabras muestran lo que se siente.",
    ["Sé escuchar con atención.", "Sé qué es un poema."],
    [
        "Un poema se escucha con la voz de quien lo lee. La voz puede ser suave, lenta o alegre. Esa voz nos ayuda a imaginar lo que dice. Cierra los ojos y deja que las palabras te muestren imágenes.",
        "En un poema, el poeta usa comparaciones: dice que algo es como otra cosa. Escucha este poema. «Gotas pequeñas / tocan la ventana, / como dedos de plata / que piden entrar. / El techo canta, / la calle se lava / y la tarde huele / a tierra y a pan». Aquí las gotas son como dedos de plata, y el techo suena como si cantara.",
        "Al escuchar, pregúntate qué imágenes ves, qué sonidos oyes y qué sientes. No hay una única respuesta, pero tu idea debe apoyarse en las palabras del poema.",
    ],
    [("poema", "texto escrito en versos, que muestra sentimientos o imágenes"), ("verso", "cada línea de un poema"), ("imagen", "lo que veo en mi mente"), ("comparación", "decir que algo se parece a otra cosa"), ("voz", "forma en que se dice un texto en voz alta")],
    [
        ("Entender una comparación", "En el poema, ¿qué quiere decir «como dedos de plata que piden entrar»?", ["El poeta compara las gotas con dedos.", "La plata brilla, como las gotas.", "Las gotas golpean la ventana como dedos que piden entrar."], "Las gotas brillan y golpean la ventana como si fueran dedos."),
        ("Entender «el techo canta»", "¿Por qué el poeta dice «el techo canta»?", ["La lluvia cae sobre el techo.", "Hace un sonido parecido a una música."], "Porque la lluvia suena en el techo, como un canto."),
    ],
    [("Pensar que el poeta habla de dedos de verdad.", "Se lee todo de forma literal.", "Piensa que es una comparación: las gotas parecen dedos."), ("Leer el poema muy rápido.", "Se quiere terminar pronto.", "Léelo despacio para imaginar las imágenes.")],
    [
        E("En el poema, ¿qué toca la ventana?", "Las gotas pequeñas", "El poema comienza con «Gotas pequeñas tocan la ventana»."),
        E("Según el poema, ¿qué canta?", "El techo", "El poema dice «El techo canta»."),
        E("Según el poema, ¿a qué huele la tarde?", "A tierra y a pan", "Son los dos olores que dice el poema."),
    ],
    [
        E("¿Qué imagen hay en «dedos de plata»?", "Las gotas parecen dedos brillantes", "Es una comparación."),
        E("En «la tarde huele a tierra y a pan», ¿qué sentido se usa?", "El olfato", "Se habla de olores."),
        E("¿Por qué el poeta dice «el techo canta»?", "Porque la lluvia suena sobre el techo", "El sonido recuerda una canción."),
    ],
    [
        E("Para leer «Gotas pequeñas tocan la ventana», ¿conviene hablar despacio y suave o gritando?", "Despacio y suave", "La lluvia suave pide voz suave."),
        E("¿Con qué compara las gotas el poeta?", "Con dedos de plata", "Lo dice en el tercer verso."),
        E("Según el poema, ¿qué hace la calle?", "Se lava", "Dice «la calle se lava»."),
    ],
    [
        E("Ana dice que el techo no puede cantar de verdad. ¿Por qué lo dice el poema?", "Para mostrar con una imagen el sonido de la lluvia", "El poeta usa imágenes, no palabras literales."),
        E("¿El poema transmite tranquilidad o miedo?", "Tranquilidad", "Las gotas son pequeñas y la tarde huele a pan."),
    ],
    [
        E("¿Cuál es una comparación: a) «El sol es una naranja grande» o b) «El sol sale a las ocho»?", "a", "Dice que el sol se parece a una naranja."),
        arith("El poema tiene 8 versos y ya escuchaste 3. ¿Cuántos versos faltan?", "8-3", "Se resta lo escuchado del total."),
    ],
    [E("Escuchas llover en tu casa. ¿Cuál frase muestra mejor un sonido suave: a) «La lluvia susurra en la ventana» o b) «La lluvia compra pan»?", "a", "Susurrar es hacer un sonido suave.")],
    [
        E("¿Cada línea de un poema se llama verso o párrafo?", "Verso", "Un poema se escribe en versos."),
        E("¿Mi imagen del poema debe apoyarse en las palabras del texto?", "Sí", "Así es una interpretación con base."),
        E("¿Dos personas pueden imaginar cosas distintas con el mismo poema?", "Sí", "Cada persona imagina a su manera."),
    ],
    ("Escucha este poema: «La luna redonda / se asoma al ventanal, / como una moneda blanca / que nadie puede gastar. / Los grillos cantan bajito / y la noche aprende a soñar». Dibuja la imagen que viste en tu mente y escribe: 1) con qué compara el poeta la luna, 2) qué sonido aparece, 3) cómo te sentiste.",
     "1) La compara con una moneda blanca. 2) Los grillos cantan bajito. 3) Me sentí tranquilo, como en una noche de silencio.",
     ["dice la comparación", "nombra el sonido", "explica lo que sintió"], ["dibujo y tres respuestas"], ["decir una comparación que no está en el poema", "no apoyarse en el texto"],
     "Pide que muestre en el poema las palabras que respaldan su respuesta."),
    "Pídele a un adulto que lea un poema corto y cuéntale qué imagen viste.",
    "Escribe dos versos con una comparación sobre la lluvia, el sol o la luna.",
)

# ================================================================ OA 22 · clase 4
reg(
    OA22, 4,
    "La fábula de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a conversar sobre una fábula: contar lo que entendí y dar mi opinión con una razón. Sirve para compartir ideas y escuchar otras.",
    ["Sé seguir los hechos de una historia.", "Sé qué es una opinión."],
    [
        "Después de escuchar una obra, podemos conversar. Conversar es hablar por turnos, escuchar a los demás y dar nuestra opinión con una razón. Una fábula es un cuento breve con animales que actúan como personas y deja una enseñanza llamada moraleja.",
        "Escucha esta fábula. «En una granja, la gallina pidió ayuda para llevar semillas al granero. El gallo dijo: no puedo, estoy ocupado cantando. La oveja dijo que estaba cansada. La gallina y el pato llevaron las semillas solos. Llegó el invierno y el gallo tuvo hambre. La gallina le dio un puñado de semillas y le dijo: la próxima vez ayúdanos». La moraleja es: quien ayuda hoy recibe ayuda mañana.",
        "Para opinar, usa «Creo que… porque…». Por ejemplo: «Creo que el gallo actuó mal porque no ayudó a sus compañeros». Escucha también a los demás y responde con respeto.",
    ],
    [("fábula", "cuento breve con animales que deja una enseñanza"), ("moraleja", "enseñanza que deja una fábula"), ("opinión", "lo que pienso sobre algo"), ("razón", "el motivo por el que pienso algo"), ("turno", "momento en que me toca hablar")],
    [
        ("Dar una opinión con razón", "¿Qué opinas del gallo? Usa «Creo que… porque…».", ["Pienso: el gallo no ayudó.", "Escribo mi opinión.", "Agrego la razón con «porque»."], "Creo que el gallo actuó mal porque no ayudó a sus compañeros."),
        ("Responder a otra opinión", "Marta dice: «La gallina fue muy amable». Estás de acuerdo. ¿Cómo respondes?", ["Digo que estoy de acuerdo con ella.", "Doy una razón."], "Estoy de acuerdo con Marta porque la gallina le dio semillas aunque él no ayudó."),
    ],
    [("Decir «no me gustó» sin razón.", "No se piensa por qué.", "Agrega «porque» y un motivo."), ("Hablar todos a la vez.", "Se quiere opinar rápido.", "Espera tu turno y escucha.")],
    [
        E("En la fábula, ¿quién pidió ayuda para llevar las semillas?", "La gallina", "El texto lo dice al inicio."),
        E("¿Qué dijo el gallo para no ayudar?", "Que estaba ocupado cantando", "Es lo que dice el texto."),
        E("¿Qué es una moraleja?", "La enseñanza que deja una fábula", "Dice qué podemos aprender."),
    ],
    [
        E("La moraleja es: «Quien ayuda hoy recibe ayuda mañana». ¿Qué enseña?", "A ayudar a los demás", "La enseñanza habla de ayuda."),
        E("Para conversar, ¿se habla por turnos o todos a la vez?", "Por turnos", "Así todos pueden escuchar."),
        E("¿Qué hizo la gallina cuando el gallo tuvo hambre?", "Le dio un puñado de semillas", "El texto lo dice."),
    ],
    [
        E("Completa: «Creo que el gallo actuó mal ___ no ayudó». Opciones: porque o pero.", "porque", "Anuncia la razón."),
        E("Ana opina que la gallina fue amable. ¿Qué razón la apoya: a) «Le dio semillas aunque él no ayudó» o b) «Es de color café»?", "a", "La razón se relaciona con la acción."),
        E("Marta dijo algo y estás de acuerdo. ¿Qué dices: «Estoy de acuerdo con Marta porque…» o «No te escucho»?", "Estoy de acuerdo con Marta porque…", "Es una respuesta respetuosa con razón."),
    ],
    [
        E("El gallo dice que cantar era más importante que ayudar. ¿La moraleja está de acuerdo con él?", "No, porque dice que quien ayuda recibe ayuda", "La moraleja valora ayudar."),
        E("Luis dice «no me gustó» sin más. ¿Qué le falta?", "Una razón con «porque»", "Una opinión necesita razón."),
    ],
    [
        E("¿Cuál opinión tiene razón: a) «Me gustó porque aprendí a ayudar» o b) «Me gustó»?", "a", "La a explica por qué."),
        arith("En la fábula aparecen 4 animales y 2 no ayudaron. ¿Cuántos ayudaron?", "4-2", "Se resta los que no ayudaron."),
    ],
    [E("Tu compañera dice que la gallina debió dejar sin semillas al gallo, pero tú crees que hizo bien. ¿Cómo respondes con respeto?", "Yo pienso distinto porque la gallina le dio semillas y le pidió ayudar la próxima vez", "Se explica el desacuerdo con calma.")],
    [
        E("Al terminar de escuchar, ¿qué hago antes de opinar?", "Pienso en lo que escuché", "Mi opinión debe basarse en la obra."),
        E("¿Es respetuoso interrumpir a quien habla?", "No", "Se espera el turno."),
        E("¿Una opinión puede ser distinta a la de mi compañero?", "Sí", "Cada persona puede opinar distinto."),
    ],
    ("Escucha esta fábula: «Un pato nadaba feliz y se burló de una tortuga lenta. La tortuga no dijo nada y siguió su camino. Cuando el pato cayó en una zanja, la tortuga le tendió una rama y lo ayudó a salir. El pato aprendió a no burlarse». Escribe: 1) tu opinión sobre el pato con «Creo que… porque…», 2) una moraleja posible.",
     "1) Creo que el pato actuó mal porque se burló de la tortuga. 2) Moraleja: No te burles de los demás, porque quizás te ayuden mañana.",
     ["usa «Creo que… porque…»", "da una razón", "propone una moraleja relacionada"], ["hoja con opinión y moraleja"], ["no dar razón", "moraleja que no se relaciona con la fábula"],
     "Pide que muestre qué parte del texto apoya su razón."),
    "Cuéntale a alguien de tu casa una fábula que conozcas y su moraleja.",
    "Inventa una moraleja para el cuento de Tomasa, la tortuga, y explica por qué.",
)

# ================================================================ OA 22 · clase 5
reg(
    OA22, 5,
    "La leyenda de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a volver a un pasaje de la obra para comprobar lo que recuerdo. Sirve para responder con evidencia y no con dudas.",
    ["Sé seguir los hechos de una historia.", "Sé opinar con razón."],
    [
        "A veces no recordamos bien un detalle de lo que escuchamos. En esos casos podemos volver a escuchar el pasaje, que es la parte de la obra donde aparece ese dato. Así comprobamos con el texto y no solo con la memoria.",
        "Escucha esta leyenda, inventada para este cuaderno. «Dicen que hace mucho tiempo un cerro grande se quedó dormido. Por eso el sol no podía salir y las mañanas llegaban tarde al pueblo. Los niños le cantaron una canción suave hasta que el cerro se movió un poquito. Desde entonces el sol sale un rato después de que cantan los gallos». Una leyenda explica con imaginación por qué algo es como es.",
        "Para volver a un pasaje, pregunta qué quieres saber y busca la parte donde se dice. Por ejemplo, para saber cómo despertaron al cerro, vuelves a la parte de los niños. Luego responde con las palabras del texto.",
    ],
    [("pasaje", "parte de una obra"), ("leyenda", "relato que explica con imaginación el origen de algo"), ("comprobar", "revisar si algo es cierto"), ("evidencia", "frase del texto que muestra que algo es cierto"), ("explícito", "dicho claramente en el texto")],
    [
        ("Encontrar el pasaje", "¿Qué hicieron los niños para despertar al cerro?", ["Busco la parte donde aparecen los niños.", "Allí dice: «Los niños le cantaron una canción suave»."], "Le cantaron una canción suave."),
        ("Comprobar una duda", "Eva cree que los niños gritaron al cerro. ¿Cómo lo compruebas?", ["Vuelvo a la parte de los niños.", "El texto dice «cantaron una canción suave»."], "No gritaron; el texto dice que le cantaron una canción suave."),
    ],
    [("Contestar sin volver al texto cuando no recuerdo.", "Se prefiere inventar para ir rápido.", "Pide que se relea el pasaje y responde con lo que dice."), ("Responder con lo que me imagino.", "Se mezcla lo que dice el texto con lo propio.", "Marca la frase del texto que apoya tu respuesta.")],
    [
        E("¿Qué hizo el cerro hace mucho tiempo?", "Se quedó dormido", "Es lo que dice la leyenda."),
        E("¿Qué hicieron los niños?", "Le cantaron una canción suave", "Aparece en la leyenda."),
        E("¿Quién se movió un poquito?", "El cerro", "Después de la canción se movió."),
    ],
    [
        E("¿Qué es volver a un pasaje?", "Escuchar de nuevo la parte donde aparece un dato", "Sirve para comprobar."),
        E("Para saber cómo despertaron al cerro, ¿qué parte vuelvo a escuchar: el principio o la parte de los niños?", "La parte de los niños", "Allí está el dato."),
        E("¿Una leyenda explica con imaginación o cuenta algo que ocurrió hoy?", "Explica con imaginación", "Cuenta cómo algo llegó a ser como es."),
    ],
    [
        E("Busca la frase que explica por qué las mañanas llegaban tarde.", "El sol no podía salir porque el cerro dormía", "El texto lo explica en la segunda oración."),
        E("Según el final, ¿cuándo sale el sol?", "Un rato después de que cantan los gallos", "Lo dice la última oración."),
        E("¿Cómo era la canción de los niños?", "Suave", "El texto dice «una canción suave»."),
    ],
    [
        E("Eva dice que los niños gritaron al cerro. ¿Cómo lo compruebas?", "Vuelvo al pasaje: dice que cantaron una canción suave", "El texto no habla de gritar."),
        E("¿Por qué cuenta la leyenda que el cerro estaba dormido?", "Para explicar con imaginación por qué el sol sale un rato después", "Es la explicación que da la leyenda."),
    ],
    [
        E("Marca V o F: 1) El cerro estaba despierto. 2) Los niños cantaron. 3) El sol sale antes de que canten los gallos.", "1 F, 2 V, 3 F", "Se comprueba con el texto."),
        arith("La leyenda tiene 4 oraciones y ya releíste 1. ¿Cuántas te faltan?", "4-1", "Se resta lo releído del total."),
    ],
    [E("Tu abuelo te cuenta algo y quieres comprobar un dato. ¿Qué haces?", "Le pido que repita esa parte", "Así compruebo el dato con lo que dijo.")],
    [
        E("¿Responder con el texto es más seguro que responder de memoria?", "Sí", "El texto muestra lo que realmente dice."),
        E("Si no encuentro el dato, ¿qué hago?", "Releo o escucho otra vez", "Así busco la parte correcta."),
        E("¿Una leyenda de este cuaderno es un hecho real o una historia imaginada?", "Una historia imaginada", "Fue inventada para este cuaderno."),
    ],
    ("Escucha esta leyenda inventada para este cuaderno: «Cuentan que había una laguna tan tímida que se escondía de la lluvia. Las nubes le hacían cosquillas hasta que la laguna se reía y se llenaba de ondas. Por eso, cuando llueve, el agua de la laguna se mueve». Responde volviendo al pasaje: 1) ¿Cómo era la laguna? 2) ¿Qué hacían las nubes? 3) ¿Qué ocurre cuando llueve? Escribe la frase que usaste en cada caso.",
     "1) Tímida: «una laguna tan tímida». 2) Le hacían cosquillas: «Las nubes le hacían cosquillas». 3) El agua se mueve: «cuando llueve, el agua de la laguna se mueve».",
     ["responde las tres preguntas", "señala la frase del texto", "no agrega datos inventados"], ["hoja con tres respuestas y tres frases"], ["responder de memoria", "inventar datos"],
     "Pide que lea en voz alta la frase que usó para cada respuesta."),
    "Pídele a un adulto que lea una leyenda y vuelve a preguntar un dato.",
    "Inventa una leyenda de tres oraciones que explique algo, como por qué sale la luna.",
)

# ================================================================ OA 23 · clase 1
reg(
    OA23, 1,
    "Los textos orales de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a escuchar con un propósito: saber para qué escucho. Sirve para poner atención a lo que realmente necesito.",
    ["Sé escuchar a otras personas.", "Sé qué es un propósito."],
    [
        "Escuchamos con distintos propósitos. A veces escuchamos para aprender datos, como en una explicación. Otras veces para hacer algo, como en las instrucciones. Y otras veces para disfrutar, como en un relato.",
        "Mira estos ejemplos. Explicación: «Las abejas hacen miel con el néctar de las flores. Lo llevan a la colmena y lo guardan en celdas». Instrucciones: «Para plantar un poroto, pon algodón en un vaso, luego el poroto y después un poco de agua». Anécdota: «Ayer se me perdió mi sombrero y lo encontré en el patio».",
        "Antes de escuchar, pregúntate para qué lo haces. Si es para aprender, fíjate en los datos. Si son instrucciones, presta atención al orden de los pasos. Si es un relato, imagina lo que ocurre.",
    ],
    [("propósito", "lo que quiero lograr al escuchar"), ("explicación", "texto que da datos para aprender algo"), ("instrucciones", "pasos para hacer algo"), ("anécdota", "relato breve de algo que le pasó a alguien"), ("dato", "información concreta")],
    [
        ("Reconocer el propósito", "Escuchas: «Las abejas hacen miel con el néctar de las flores». ¿Para qué escuchas?", ["El texto da una información.", "Escucho para aprender un dato."], "Para aprender un dato."),
        ("Reconocer instrucciones", "Escuchas: «Para plantar un poroto, pon algodón en un vaso». ¿Qué tipo de texto es?", ["Dice cómo se hace algo.", "Tiene pasos."], "Son instrucciones."),
    ],
    [("Escuchar todo igual, sin saber para qué.", "No se piensa antes de escuchar.", "Pregunta antes: ¿para qué escucho?"), ("Jugar mientras escucho instrucciones.", "Se distrae la atención.", "Escucha con calma y sin otras actividades.")],
    [
        E("Si escucho cómo se hace una torta, ¿para qué escucho?", "Para seguir los pasos", "Son instrucciones que dicen cómo hacerlo."),
        E("Al escuchar un cuento, ¿escucho para disfrutar o para aprender pasos?", "Para disfrutar", "Los cuentos se escuchan para disfrutar."),
        E("En Lenguaje: ¿Qué es el propósito al escuchar?", "Para qué escucho", "Es lo que quiero lograr."),
    ],
    [
        E("«Las abejas hacen miel con el néctar de las flores. Lo llevan a la colmena.» ¿Es una explicación o un relato?", "Una explicación", "Entrega datos para aprender."),
        E("En una explicación, ¿busco información o un final sorpresa?", "Información", "Se escucha para aprender."),
        E("En unas instrucciones, ¿a qué presto más atención?", "Al orden de los pasos", "El orden importa para hacerlas bien."),
    ],
    [
        E("Escuchas: «Para plantar un poroto, primero pon algodón en un vaso». ¿Cuál es el propósito del texto?", "Dar instrucciones", "Dice cómo hacer algo."),
        E("¿Qué haces al escuchar una explicación?", "Miro a quien habla y pienso en los datos importantes", "Así recuerdo la información."),
        E("Escuchas: «Las abejas llevan el néctar a la colmena». ¿Qué dato aprendes?", "Que las abejas llevan el néctar a la colmena", "Es la información que da el texto."),
    ],
    [
        E("Ana escucha instrucciones jugando con su lápiz. ¿Qué puede pasarle?", "Puede olvidar un paso", "Se distrae y pierde atención."),
        E("«Ayer se me perdió mi sombrero y lo encontré en el patio.» ¿Cuál es el propósito?", "Contar una anécdota", "Narra algo que le pasó a alguien."),
    ],
    [
        E("Une: A explicación, B instrucciones, C relato con 1) aprender datos, 2) seguir pasos, 3) disfrutar una historia.", "A1, B2, C3", "Cada texto tiene su propósito."),
        arith("El texto de las abejas tiene 2 oraciones. Si ya escuchaste 1, ¿cuántas faltan?", "2-1", "Se resta lo escuchado."),
    ],
    [E("Tu mamá te dice: «Sal, camina dos cuadras y gira a la derecha». ¿Para qué escuchas?", "Para seguir las instrucciones y llegar sin perderme", "Son pasos para llegar.")],
    [
        E("¿Qué hago antes de escuchar un texto nuevo?", "Pienso para qué voy a escuchar", "Eso guía mi atención."),
        E("¿Todos los textos orales sirven para lo mismo?", "No", "Cada uno tiene su propósito."),
        E("¿Para qué escucho un cuento: para aprender pasos o para disfrutar?", "Para disfrutar", "Es un relato."),
    ],
    ("Un adulto te lee tres textos. Texto 1: «Los delfines respiran aire por un orificio en la cabeza». Texto 2: «Primero lava tus manos, luego seca bien con una toalla». Texto 3: «El domingo mi gato se subió al techo y bajó con un pajarito de juguete». Escribe el propósito de cada uno (aprender, seguir pasos o disfrutar) y una razón.",
     "Texto 1: aprender, porque da un dato sobre los delfines. Texto 2: seguir pasos, porque dice cómo lavarse las manos. Texto 3: disfrutar, porque cuenta algo que le pasó al gato.",
     ["identifica el propósito de cada texto", "da una razón", "usa los datos del texto"], ["hoja con tres propósitos y razones"], ["confundir explicación con relato", "no dar razón"],
     "Pregunta: «¿Qué te dice el texto: un dato, pasos o una historia?»."),
    "Pídele a un adulto que te diga cómo prepara algo y dime cuál era el propósito.",
    "Escucha un programa corto y di si era para informar, instruir o entretener.",
)

# ================================================================ OA 23 · clase 2
reg(
    OA23, 2,
    "Los textos orales de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a conectar lo que escucho con mis experiencias, sin salirme del tema. Sirve para entender mejor y recordar.",
    ["Sé para qué escucho un texto.", "Sé contar algo que viví."],
    [
        "Cuando escuchamos algo, a veces recordamos algo que vivimos. Eso se llama conectar con nuestra experiencia. Conectar ayuda a entender mejor, porque relacionamos lo nuevo con lo que ya sabemos.",
        "Escucha este texto. «Mi abuelo tiene una huerta. Planta tomates y lechugas. Cada mañana los riega con una regadera». Si dices «Yo también riego las plantas de mi casa», estás conectando con el tema. Si dices «Ayer vi una película de piratas», te desvías, porque no se relaciona con la huerta.",
        "Una buena conexión es breve, se relaciona con lo escuchado y después vuelve al tema. Así todos pueden seguir escuchando.",
    ],
    [("conectar", "relacionar lo que escucho con algo que viví"), ("experiencia", "algo que me pasó o que hice"), ("huerta", "terreno donde se plantan verduras"), ("desviarse", "salirse del tema"), ("tema", "de qué trata un texto")],
    [
        ("Hacer una conexión", "Escuchas: «Mi abuelo tiene una huerta». ¿Qué conexión puedes decir?", ["Pienso en algo que viví sobre plantas o huertas.", "Digo una frase breve y relacionada."], "Mi tía también tiene una huerta y cosecha zapallos."),
        ("Reconocer una desviación", "Alguien dice: «Hoy comí pizza» después de escuchar sobre la huerta. ¿Se conecta?", ["La huerta es de verduras.", "La pizza no se relaciona."], "No se conecta; se desvió del tema."),
    ],
    [("Contar una historia muy larga que no tiene que ver.", "Se quiere hablar de lo que me gusta.", "Haz una conexión breve y vuelve al tema."), ("No decir nada por miedo a equivocarse.", "Se cree que no hay respuestas correctas.", "Conecta con una experiencia simple.")],
    [
        E("Según el texto, ¿qué planta el abuelo?", "Tomates y lechugas", "El texto lo dice."),
        E("Según el texto, ¿con qué los riega?", "Con una regadera", "Es lo que dice el texto."),
        E("«Yo también riego las plantas de mi casa.» ¿Se relaciona con el texto de la huerta?", "Sí", "Habla de regar plantas."),
    ],
    [
        E("¿Qué es conectar lo que escucho con mi experiencia?", "Relacionarlo con algo que viví", "Une lo nuevo con lo que ya sé."),
        E("¿Cuál se relaciona con la huerta: a) «En mi casa mi mamá siembra albahaca» o b) «Ayer vi una película de piratas»?", "a", "La albahaca es una planta."),
        E("¿Para qué sirve conectar?", "Para entender mejor y recordar", "Relaciono con lo que conozco."),
    ],
    [
        E("Marta dice: «Mi tía también tiene una huerta y cosecha zapallos». ¿Se conecta con el texto?", "Sí", "Habla de una huerta."),
        E("Pedro dice: «Mi perro se llama Rex». ¿Se conecta con el texto de la huerta?", "No", "Es otro tema."),
        E("Después de contar tu experiencia, ¿qué frase vuelve al tema: a) «Y por eso me gusta que el abuelo riegue sus tomates» o b) «Y además mi perro es grande»?", "a", "La a regresa a lo que se escuchó."),
    ],
    [
        E("Luis habla de su cumpleaños mientras escucha sobre la huerta. ¿Qué problema hay?", "Se desvía del tema", "No se relaciona con lo escuchado."),
        E("Una conexión debe ser breve. ¿Por qué?", "Para que todos puedan seguir escuchando", "Una conexión larga interrumpe."),
    ],
    [
        E("¿Cuál es conexión y cuál se desvía? 1) «Mi mamá riega las flores del balcón» 2) «Hoy comí pizza».", "1 conexión, 2 se desvía", "Solo la primera se relaciona con regar plantas."),
        arith("El texto tiene 3 oraciones y conectas 1 con tu experiencia. ¿Cuántas quedan sin conectar?", "3-1", "Se resta la que conectaste."),
    ],
    [E("La profesora lee sobre una huerta y pregunta quién ha visto una. Tú viste la huerta de tu vecina, que tiene lechugas. ¿Qué dices?", "Yo vi la huerta de mi vecina y tiene lechugas", "Es una conexión breve y relacionada.")],
    [
        E("¿Una buena conexión se relaciona con el tema?", "Sí", "Si no, es una desviación."),
        E("¿Debo volver al tema después de conectar?", "Sí", "Así sigo aprendiendo del texto."),
        E("¿Mi experiencia es parte de lo que entiendo del texto?", "Sí", "Ayuda a comprender."),
    ],
    ("Escucha este texto: «Mi tía tiene un gallinero. Cada mañana junta los huevos y le da maíz a las gallinas. Las gallinas ponen más huevos cuando están tranquilas». Escribe dos cosas. Primero una conexión con tu experiencia relacionada con el texto. Segundo, una frase que sería una desviación.",
     "Conexión: En mi casa tenemos una gallina y le doy maíz. Desviación: Ayer fui a la playa con mi primo.",
     ["la conexión se relaciona con el texto", "es breve y clara", "la desviación no se relaciona con el texto"], ["hoja con dos frases"], ["contar algo que no se relaciona", "escribir una conexión demasiado larga"],
     "Pregunta: «¿Qué parte del texto te hizo recordar eso?»."),
    "Cuéntale a un adulto algo que te recordó un texto que escuchaste.",
    "Escucha una noticia breve y escribe una conexión con tu experiencia.",
)

# ================================================================ OA 23 · clase 3
reg(
    OA23, 3,
    "Los textos orales de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a hacer preguntas para obtener información que falta o para aclarar dudas. Sirve para entender bien un aviso o una explicación.",
    ["Sé escuchar con atención.", "Sé que las preguntas llevan ¿?."],
    [
        "Cuando algo no queda claro, podemos preguntar. Preguntar es pedir información. Las preguntas comienzan con palabras como qué, quién, cuándo, dónde, cómo y por qué. Cada una pide un dato distinto: «dónde» pide un lugar y «cuándo» pide un momento.",
        "Escucha este aviso. «El sábado iremos al museo. Saldremos temprano en el bus del colegio. Lleven colación». El aviso dice el lugar, el día y lo que hay que llevar. No dice la hora exacta. Entonces puedes preguntar: «¿A qué hora saldremos?».",
        "Para preguntar bien, levanta la mano, espera tu turno y di «disculpe» o «por favor». Si no oíste bien, puedes decir: «¿Puede repetir?». Preguntar muestra que quieres entender.",
    ],
    [("pregunta", "oración que pide información"), ("aclarar", "dejar algo claro"), ("duda", "cuando no estoy seguro de algo"), ("información", "datos que sirven para saber algo"), ("repetir", "decir otra vez")],
    [
        ("Encontrar el dato que falta", "El aviso dice: «El sábado iremos al museo. Saldremos temprano en el bus del colegio. Lleven colación». ¿Qué dato falta?", ["Busco lugar: museo.", "Busco día: sábado.", "Busco hora: solo dice temprano, falta la hora exacta."], "Falta la hora exacta de salida."),
        ("Hacer la pregunta", "Haz una pregunta para saber la hora.", ["Uso la palabra «a qué hora».", "Pongo los dos signos."], "¿A qué hora saldremos?"),
    ],
    [("Preguntar algo que ya se dijo.", "No se escuchó con atención.", "Escucha primero y pregunta solo lo que falta."), ("Hablar sin pedir la palabra.", "Se quiere preguntar rápido.", "Levanta la mano y espera tu turno.")],
    [
        E("¿Qué palabra uso para preguntar por un lugar: dónde o quién?", "Dónde", "Pide un lugar."),
        E("¿Qué palabra uso para preguntar por una persona: quién o cuándo?", "Quién", "Pide una persona."),
        E("Si no entendí algo, ¿pregunto o me quedo callado?", "Pregunto", "Preguntar ayuda a entender."),
    ],
    [
        E("Del aviso del museo, ¿qué dato no dice exactamente: la hora de salida o el lugar?", "La hora de salida", "Solo dice «temprano»."),
        E("¿Para qué sirve preguntar para aclarar?", "Para entender lo que no quedó claro", "Aclara las dudas que tengo."),
        E("¿Cuál pregunta aclara: «¿A qué hora salimos?» o «Me gusta el museo»?", "¿A qué hora salimos?", "Pide el dato que falta."),
    ],
    [
        E("¿Cuál pregunta sirve para saber la hora: a) «¿A qué hora saldremos?» o b) «Saldremos»?", "a", "La a pregunta por la hora."),
        E("¿Qué pregunta sirve para saber qué colación traer: «¿Qué debo traer de colación?» o «Yo traigo pan»?", "¿Qué debo traer de colación?", "Pide el dato."),
        E("El aviso dice que irán al museo. ¿Hace falta preguntar adónde van?", "No, porque ya lo dijo", "El lugar ya está dicho."),
    ],
    [
        E("Rosa pregunta «¿Adónde vamos?», pero el aviso ya dijo museo. ¿Qué pudo hacer?", "Escuchar con atención o pedir que repitan", "Había un dato que ya se dijo."),
        E("¿Por qué decir «disculpe» antes de preguntar?", "Para pedir la palabra con respeto", "Es una forma amable de hablar."),
    ],
    [
        E("¿Cuáles de estas empiezan una pregunta: dónde, hoy, cuándo, mesa?", "dónde y cuándo", "Son palabras interrogativas."),
        arith("Necesitas 4 datos para el paseo (lugar, hora, transporte y qué llevar) y te dieron 3. ¿Cuántos faltan?", "4-3", "Se resta lo que te dijeron."),
    ],
    [E("La profesora dice: «Mañana visitaremos una granja». No dijo a qué hora. ¿Qué preguntas?", "¿A qué hora salimos?", "Es el dato que falta.")],
    [
        E("¿Cuál palabra pide un momento: cuándo o dónde?", "Cuándo", "Pide cuándo ocurre algo."),
        E("¿Qué hago antes de preguntar en clase?", "Levanto la mano", "Así respeto el turno."),
        E("¿Una pregunta lleva dos signos?", "Sí", "Uno de apertura y otro de cierre."),
    ],
    ("Escucha este aviso: «La biblioteca abrirá una función de cuentos. Será en la sala azul. Los niños deben ir con un adulto». Escribe tres preguntas para obtener información que falta o aclarar una duda (por ejemplo, sobre el día, la hora y qué cuentos se leerán).",
     "¿Qué día será la función? ¿A qué hora empieza? ¿Qué cuentos se leerán?",
     ["escribe tres preguntas con signos", "pide datos que faltan", "usa palabras interrogativas"], ["hoja con tres preguntas"], ["preguntar lo que ya dijo el aviso", "olvidar los signos"],
     "Pregunta: «¿Esa información ya estaba en el aviso?»."),
    "Haz una pregunta a un adulto para aclarar algo que no entendiste.",
    "Escucha una noticia breve y escribe tres preguntas sobre lo que no dijo.",
)

# ================================================================ OA 23 · clase 4
reg(
    OA23, 4,
    "Los textos orales de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a diferenciar lo que un texto dice claramente de lo que debo pensar con pistas. Sirve para comprender más allá de las palabras.",
    ["Sé responder preguntas sobre un texto.", "Sé buscar pistas."],
    [
        "La información explícita es la que el texto dice claramente. La información implícita es la que no está dicha, pero podemos pensar usando pistas y lo que ya sabemos. Esa idea que formamos se llama inferencia.",
        "Escucha este texto. «Martina llegó a casa con el paraguas mojado y las botas llenas de barro. Dejó las botas junto a la puerta y se sacó el abrigo». Explícito: el paraguas estaba mojado y las botas tenían barro. El texto no dice que llovió, pero con las pistas podemos inferirlo.",
        "Para inferir, junta dos pistas del texto y lo que sabes del mundo. Pregúntate: ¿qué pudo haber pasado? Si no hay pistas, no puedes afirmar nada. Las inferencias deben apoyarse en lo que se escuchó.",
    ],
    [("explícito", "dicho claramente"), ("implícito", "no dicho, pero se puede pensar"), ("inferencia", "idea que formo con pistas del texto"), ("pista", "señal que ayuda a pensar"), ("afirmar", "decir que algo es cierto")],
    [
        ("Buscar información explícita", "¿Qué estaba mojado, según el texto de Martina?", ["Busco la frase donde se dice.", "Dice «el paraguas mojado»."], "El paraguas."),
        ("Hacer una inferencia", "El texto no dice que llovió. ¿Puedes inferirlo?", ["Pista 1: paraguas mojado.", "Pista 2: botas con barro.", "Sé que cuando llueve el paraguas se moja y el suelo se llena de barro."], "Sí, se puede inferir que había llovido."),
    ],
    [("Decir como si fuera un hecho algo que no hay pistas.", "Se inventa sin apoyarse en el texto.", "Comprueba que tengas al menos dos pistas."), ("Pensar que lo que no está escrito no se puede saber.", "Se confunde decir con inferir.", "Usa las pistas para pensar más allá.")],
    [
        E("¿Qué estaba mojado, según el texto?", "El paraguas", "Está dicho en el texto."),
        E("¿Con qué estaban llenas las botas de Martina?", "Con barro", "El texto dice «las botas llenas de barro»."),
        E("¿Qué hizo Martina con el abrigo?", "Se lo sacó", "El texto lo dice."),
    ],
    [
        E("La información explícita, ¿se dice en el texto o se piensa?", "Se dice en el texto", "Está escrita o dicha."),
        E("¿Qué es una inferencia?", "Una idea que formo con pistas del texto", "No está dicha, pero se apoya en pistas."),
        E("El texto no dice «llovió». ¿Se puede inferir con las pistas «paraguas mojado» y «botas con barro»?", "Sí", "Las pistas indican lluvia."),
    ],
    [
        E("«Martina se sacó el abrigo.» ¿Es información explícita o inferencia?", "Explícita", "El texto lo dice."),
        E("«Afuera había llovido.» ¿Es información explícita o inferencia?", "Inferencia", "El texto no lo dice, se piensa con pistas."),
        E("¿Qué pista ayuda a pensar que llovió: el paraguas mojado o el abrigo?", "El paraguas mojado", "Un paraguas se moja con la lluvia."),
    ],
    [
        E("Tomás dice que Martina estaba contenta. ¿Hay pistas en el texto para afirmarlo?", "No, no hay pistas", "El texto no habla de cómo se sentía."),
        E("¿Por qué una inferencia debe apoyarse en pistas?", "Para no inventar", "Así tiene base en el texto."),
    ],
    [
        E("Marca E (explícita) o I (inferencia): 1) Las botas tenían barro. 2) Había caminado por una calle mojada. 3) Se sacó el abrigo.", "1 E, 2 I, 3 E", "1 y 3 están en el texto; 2 se piensa."),
        arith("Hay 3 hechos dichos en el texto y 1 que se infiere. ¿Cuántos datos hay en total?", "3+1", "Se suman los dichos y el inferido."),
    ],
    [E("Escuchas: «Pedro llegó con el pelo seco y la chaqueta puesta; en la mano traía un helado a medio comer». ¿Qué se dice explícitamente?", "Que tenía el pelo seco, la chaqueta puesta y un helado a medio comer", "Son hechos que el texto dice.")],
    [
        E("¿Dos pistas son mejores que una para inferir?", "Sí", "Dan más apoyo."),
        E("¿Una inferencia siempre está escrita en el texto?", "No", "Se forma con pistas."),
        E("Si no hay pistas, ¿puedo afirmar una inferencia?", "No", "Eso sería inventar datos."),
    ],
    ("Escucha: «Camila abrió su mochila y vio que su cuaderno estaba mojado. La botella de agua estaba sin tapa. Camila suspiró y buscó una toalla». Escribe una información explícita y una inferencia, con dos pistas que la apoyen.",
     "Explícita: El cuaderno estaba mojado. Inferencia: Se derramó el agua de la botella. Pistas: la botella estaba sin tapa y el cuaderno mojado.",
     ["escribe una información explícita", "propone una inferencia razonable", "da dos pistas"], ["hoja con información explícita, inferencia y pistas"], ["inventar sin pistas", "decir lo mismo en ambas"],
     "Pregunta: «¿Qué dos pistas del texto te hicieron pensar eso?»."),
    "Escucha una conversación de adultos y dime algo que se pueda inferir.",
    "Escribe un texto corto de dos oraciones con pistas para que otra persona infiera algo.",
)

# ================================================================ OA 23 · clase 5
reg(
    OA23, 5,
    "Las instrucciones de este cuaderno, que un adulto lee en voz alta. Una hoja de papel y lápiz.",
    "Aprenderé a escuchar instrucciones, recordar el orden de los pasos y hacerlos bien. Sirve para realizar tareas sin equivocarme.",
    ["Sé seguir pasos.", "Sé las palabras primero, después y por último."],
    [
        "Las instrucciones dicen paso a paso cómo hacer algo. Para seguirlas, escucha con atención y en silencio. Presta atención a las palabras de orden: primero, luego, después y por último. Recuerda cuántos pasos son.",
        "Escucha estas instrucciones. «Toma una hoja. Primero, dóblala por la mitad. Después, dibuja una estrella en una de las mitades. Por último, escribe tu nombre en la otra mitad». Después de tomar la hoja, son tres pasos. Si cambias el orden, el resultado es distinto.",
        "Si no entiendes un paso, pide que lo repitan. Cuando termines, revisa si hiciste todos los pasos en el orden dicho.",
    ],
    [("instrucciones", "pasos que dicen cómo hacer algo"), ("paso", "una parte de las instrucciones"), ("orden", "primero, después, por último"), ("revisar", "mirar si hice todo bien"), ("mitad", "una de las dos partes iguales")],
    [
        ("Seguir el orden", "En las instrucciones, ¿qué haces primero?", ["Busco «primero».", "Dice: dóblala por la mitad."], "Doblar la hoja por la mitad."),
        ("Contar los pasos", "¿Cuántos pasos tienen las instrucciones: doblar, dibujar y escribir?", ["Cuento cada acción.", "Doblar, dibujar, escribir."], "Tres pasos."),
    ],
    [("Hacer los pasos en otro orden.", "No se escuchan las palabras de orden.", "Escucha primero, después y por último."), ("Seguir adelante sin entender un paso.", "Da vergüenza preguntar.", "Pide que lo repitan.")],
    [
        E("¿Qué haces primero: doblar la hoja o dibujar la estrella?", "Doblar la hoja", "Es el primer paso."),
        E("¿Dónde dibujas la estrella?", "En una de las mitades", "El texto lo dice."),
        E("¿Qué escribes al final?", "Tu nombre", "Es el último paso."),
    ],
    [
        E("¿Qué palabra indica el último paso: primero o por último?", "Por último", "Marca el final."),
        E("¿Para qué escucho las instrucciones hasta el final?", "Para no saltarme pasos", "Cada paso importa."),
        E("«Pon un vaso en la mesa. Mete tres lápices. Saca uno.» ¿Cuántos pasos tiene?", "3", "Poner, meter y sacar."),
    ],
    [
        arith("Pones tres lápices en un vaso y sacas uno. ¿Cuántos lápices quedan?", "3-1", "Se resta el que sacaste."),
        E("Ordena: 1) dibujar la estrella, 2) doblar la hoja, 3) escribir tu nombre.", "2, 1, 3", "Doblo, dibujo y escribo."),
        E("¿Dónde escribes tu nombre?", "En la otra mitad", "Es lo que indica el texto."),
    ],
    [
        E("Pía dibujó la estrella antes de doblar la hoja. ¿Qué pasó?", "No siguió el orden", "El primer paso era doblar."),
        E("Si no entiendo un paso, ¿qué hago?", "Pido que lo repitan", "Así no me equivoco."),
    ],
    [
        arith("Escuchas: «Toma 5 fichas, pon 2 en una caja y 1 en otra». ¿Cuántas fichas quedan fuera de las cajas?", "5-2-1", "Se restan las fichas puestas en las cajas."),
        E("Después de doblar la hoja por la mitad, ¿cuántas mitades tiene?", "2", "Una mitad y otra."),
    ],
    [E("Mamá dice: «Lava la lechuga, sécala y luego ponla en el plato». ¿Qué haces después de lavarla?", "La seco", "El orden es lavar, secar y poner.")],
    [
        E("¿Qué palabras me ayudan a recordar el orden?", "Primero, después y por último", "Son palabras de orden."),
        E("Al terminar, ¿qué reviso?", "Si hice todos los pasos en el orden", "Así compruebo mi trabajo."),
        E("¿Puedo cambiar el orden de los pasos sin problema?", "No", "El orden cambia el resultado."),
    ],
    ("Un adulto lee: «Toma una hoja. Primero, dóblala por la mitad. Después, dibuja una estrella en una de las mitades. Por último, escribe tu nombre en la otra mitad». Hazlo en una hoja. Luego escribe cuántos pasos tuvo (sin contar «Toma una hoja») y qué quedó en cada mitad.",
     "Fueron tres pasos. En una mitad hay una estrella y en la otra mitad está mi nombre.",
     ["sigue los pasos en orden", "dice cuántos pasos fueron", "describe cada mitad"], ["hoja doblada con estrella y nombre y una respuesta escrita"], ["cambiar el orden", "no escribir el nombre"],
     "Pide que cuente en voz alta los pasos que hizo sin mirar el texto."),
    "Pídele a un adulto instrucciones para algo simple y síguelas.",
    "Escribe unas instrucciones de tres pasos para que otra persona las siga.",
)

# ================================================================ OA 23 · clase 6
reg(
    OA23, 6,
    "El relato de este cuaderno, que un adulto lee en voz alta. Lápiz y hoja.",
    "Aprenderé a opinar sobre lo que escucho y a dar una razón. Sirve para expresar lo que pienso con respeto.",
    ["Sé que una opinión es lo que pienso.", "Sé usar «porque»."],
    [
        "Después de escuchar un relato, podemos opinar. Una opinión es lo que pensamos sobre algo que escuchamos. No es lo mismo que un hecho. Un hecho se puede comprobar en el relato; una opinión es lo que pensamos de ese hecho.",
        "Escucha este relato. «El otro día fui a la plaza con mi hermano. Encontramos una billetera con dinero. La llevamos al guardia de la plaza, y el dueño vino a buscarla. Nos dio las gracias». Hecho: llevaron la billetera al guardia. Opinión: «Hicieron bien porque el dinero no era suyo».",
        "Para opinar bien, di lo que piensas y por qué. Usa «Creo que… porque…». Escucha también las opiniones de otros. Puedes pensar distinto, pero con respeto.",
    ],
    [("hecho", "algo que ocurrió y se puede comprobar"), ("opinión", "lo que pienso sobre algo"), ("razón", "motivo de mi opinión"), ("respetar", "tratar bien a otros aunque piensen distinto"), ("guardia", "persona que cuida un lugar")],
    [
        ("Distinguir hecho y opinión", "¿«Llevaron la billetera al guardia» es un hecho o una opinión?", ["Puedo comprobarlo en el relato.", "El relato lo dice."], "Es un hecho."),
        ("Dar una opinión con razón", "Opina sobre lo que hicieron los hermanos.", ["Digo qué pienso: hicieron bien.", "Agrego la razón con «porque»."], "Creo que hicieron bien porque el dinero no era de ellos."),
    ],
    [("Decir una opinión como si fuera un hecho.", "Se mezclan las dos cosas.", "Pregunta: ¿se puede comprobar en el relato?"), ("Burlarse de una opinión distinta.", "Se piensa que solo una persona tiene razón.", "Escucha y responde con respeto.")],
    [
        E("¿Qué encontraron los hermanos?", "Una billetera con dinero", "Lo dice el relato."),
        E("¿A quién la llevaron?", "Al guardia de la plaza", "Es la persona que menciona el relato."),
        E("¿Qué hizo el dueño al recibir la billetera?", "Les dio las gracias", "Es el final del relato."),
    ],
    [
        E("En Lenguaje: ¿Qué es una opinión?", "Lo que pienso sobre algo", "Es mi idea sobre lo que escuché."),
        E("¿Cuál es una opinión: «Encontraron una billetera» o «Hicieron bien»?", "Hicieron bien", "Es una valoración, no un hecho."),
        E("¿Qué palabra uso para dar la razón de mi opinión?", "Porque", "Introduce el motivo."),
    ],
    [
        E("Completa: «Creo que hicieron bien ___ la billetera no era suya». Opciones: porque o aunque.", "porque", "Introduce la razón."),
        E("Beto opina: «El final me gustó porque el dueño recuperó su billetera». ¿Cuál es su razón?", "El dueño recuperó su billetera", "Va después de «porque»."),
        E("¿Cuál opinión tiene razón: a) «Fue un buen gesto porque ayudaron a otra persona» o b) «Fue un buen gesto»?", "a", "La a explica por qué."),
    ],
    [
        E("Un niño dice: «Hicieron mal porque eran dos». ¿Esa razón apoya su opinión?", "No, porque ser dos no tiene relación", "La razón debe estar relacionada con los hechos."),
        E("¿Puedo opinar distinto a mi compañero con respeto?", "Sí", "Cada persona puede pensar distinto."),
    ],
    [
        E("Marca H (hecho) u O (opinión): 1) Llevaron la billetera al guardia. 2) Fueron muy honestos. 3) El dueño dio las gracias.", "1 H, 2 O, 3 H", "Honestos es una valoración; los otros hechos se comprueban."),
        arith("En el relato hay 4 personas: el narrador, su hermano, el guardia y el dueño. Dos son hermanos. ¿Cuántas no son los hermanos?", "4-2", "Se resta a los hermanos."),
    ],
    [E("Tu amigo dice que los hermanos debieron quedarse con el dinero. Tú no estás de acuerdo. ¿Cómo respondes con respeto?", "Yo pienso distinto, porque el dinero era de otra persona", "Se dice la opinión con una razón y sin ofender.")],
    [
        E("¿Un hecho se puede comprobar en el relato?", "Sí", "Está dicho en el texto."),
        E("¿Una opinión es siempre un hecho?", "No", "Es lo que pienso sobre algo."),
        E("¿Qué debo hacer cuando mi compañero opina distinto?", "Escuchar con respeto", "Podemos pensar distinto sin pelear."),
    ],
    ("Escucha este relato: «Ayer, mi vecina Elena regaló flores de su jardín a los vecinos. Algunos dieron las gracias y otros no dijeron nada. Elena sonrió igual». Escribe 1) un hecho del relato, 2) tu opinión sobre lo que hizo Elena, con una razón, 3) una frase para responder con respeto a alguien que piense distinto.",
     "1) Elena regaló flores a los vecinos. 2) Creo que Elena fue generosa porque compartió sus flores. 3) Yo pienso distinto, pero respeto tu opinión porque cada uno puede pensar distinto.",
     ["escribe un hecho comprobable", "da una opinión con razón", "responde con respeto"], ["hoja con tres respuestas"], ["dar una opinión sin razón", "burlarse de otra opinión"],
     "Pregunta: «¿Se puede comprobar en el relato o es lo que piensas?»."),
    "Dile a un adulto tu opinión sobre un cuento que escuchaste y explica por qué.",
    "Compara tu opinión con la de alguien de tu casa sobre el mismo relato y escribe en qué se parecen.",
)

"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 26 (apreciar obras de teatro, películas o representaciones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA26 = "LE06 OA 26"
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


# Sinopsis originales usadas en la clase 1
S_TREN = ("Obra de teatro «El último tren del pueblo»: la empresa quiere cerrar la estación de un pueblo pequeño. "
          "Doña Rita, la jefa de estación, y Nico, un niño que vende periódicos, juntan firmas para impedirlo. "
          "El alcalde dice que mantener el tren es muy caro. Al final, los vecinos viajan y envían encomiendas durante una semana y el cierre se posterga.")
S_LLAVES = ("Película «Las llaves de Ema»: Ema pierde las llaves de su casa el día en que su familia viaja. "
            "Recorre el barrio preguntando a los vecinos, pero cada uno le da una pista distinta. "
            "Descubre que las dejó en la panadería, donde el panadero las guardó. Termina conociendo a todos sus vecinos.")

# ================================================================ OA 26 · clase 1
reg(
    OA26, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar la sinopsis de la actividad abierta.",
    "Aprenderé a discutir los aspectos relevantes de la historia de una obra de teatro o una película: personajes, conflicto, desenlace y tema. Sirve para opinar con razones y no solo decir «me gustó» o «no me gustó».",
    ["Sé que las historias tienen inicio, desarrollo y final.", "Sé dar una opinión y una razón."],
    [
        "Cuando apreciamos una obra de teatro o una película, no solo la miramos: la pensamos y la discutimos. Para eso conviene fijarse en cuatro aspectos de la historia. Los personajes son quienes actúan. El conflicto es el problema que mueve la historia. El desenlace es la forma en que ese problema se resuelve o termina. El tema es la idea de fondo que la obra deja pensando, por ejemplo la amistad o la unión de una comunidad.",
        "Una buena discusión se apoya en la historia. Decir «la obra es buena porque sí» no ayuda a nadie. En cambio, «me gustó el desenlace, porque los vecinos lograron postergar el cierre juntos» da una razón que otros pueden comprobar o rebatir. Por eso, al discutir, siempre nombramos la parte de la historia que respalda lo que decimos.",
        "Para encontrar el tema, pregúntate qué hace que el problema se resuelva o no se resuelva. Si lo resuelve el trabajo en equipo, el tema se relaciona con la cooperación. El tema no es lo que pasa en la historia (eso es el argumento), sino lo que esa historia nos hace pensar sobre la vida.",
    ],
    [("personaje", "quien actúa en la historia"), ("conflicto", "problema central que mueve la historia"), ("desenlace", "parte final, donde el problema se resuelve o termina"), ("tema", "idea de fondo que deja pensando la obra"), ("argumento", "lo que ocurre en la historia, hecho por hecho")],
    [
        ("Separar conflicto y desenlace", "Película «La bicicleta azul»: Lola quiere correr una carrera, pero su bicicleta está rota. Su vecino Aldo la ayuda a repararla y ella llega tarde. Igual pedalea hasta el final, llega última y los demás la aplauden. ¿Cuál es el conflicto y cuál el desenlace?", ["Busco el problema que mueve la historia: la bicicleta rota y la carrera.", "Busco cómo termina: llega última pero la aplauden.", "Separo cada aspecto con su parte del texto."], "Conflicto: la bicicleta rota antes de la carrera. Desenlace: llega última, pero la aplauden."),
        ("Proponer el tema con una razón", "En «La bicicleta azul», ¿qué tema se puede proponer y con qué razón?", ["Miro qué resuelve el problema: la ayuda del vecino y la perseverancia de Lola.", "Pienso en una idea de fondo: ayudar y no rendirse.", "Justifico con una parte de la historia."], "Tema: la perseverancia y la ayuda entre vecinos, porque Lola llega a la meta gracias a la ayuda de Aldo y a que no se rinde."),
    ],
    [("Decir «la obra es buena porque sí».", "Se cree que una opinión no necesita razones.", "Agrega una razón tomada de la historia: «Me gustó el desenlace porque…»."), ("Confundir el tema con el argumento.", "Se cuenta lo que pasa en lugar de la idea de fondo.", "Pregúntate qué idea deja la historia, no solo qué ocurre.")],
    [
        E(f"{S_TREN} ¿Qué personaje vende periódicos?", "Nico", "El texto dice que Nico es el niño que vende periódicos."),
        E(f"{S_TREN} ¿Cuál es el conflicto: a) la empresa quiere cerrar la estación b) Nico pierde su trabajo c) el alcalde se va del pueblo?", "a", "El problema que mueve la historia es el cierre de la estación."),
        E(f"{S_TREN} ¿Cómo termina la historia: a) el cierre se posterga b) el tren se destruye c) Nico se va del pueblo?", "a", "El texto dice que el cierre se posterga al final."),
    ],
    [
        E(f"{S_LLAVES} ¿Cuál es el conflicto de la película?", "Ema pierde las llaves de su casa", "El problema que mueve la historia es la pérdida de las llaves."),
        E(f"{S_LLAVES} ¿Quién había guardado las llaves?", "El panadero", "Lo dice el texto: las guardó en la panadería."),
        E(f"{S_LLAVES} ¿Qué idea de fondo se relaciona mejor con la película: a) los vecinos pueden ayudarse y conocerse b) conviene viajar siempre solo c) hay que desconfiar de los panaderos?", "a", "Ema resuelve el problema gracias a sus vecinos y termina conociéndolos."),
    ],
    [
        E(f"{S_TREN} ¿Qué razón del texto apoya la opinión «el alcalde es un obstáculo para Rita y Nico»: a) dice que mantener el tren es muy caro b) vende encomiendas c) viaja en tren?", "a", "Su argumento va contra lo que quieren Rita y Nico."),
        E(f"{S_TREN} Ordena los hechos: a) los vecinos viajan y envían encomiendas b) la empresa quiere cerrar la estación c) Rita y Nico juntan firmas. Escribe las letras.", "b, c, a", "Primero el problema, luego el intento de solución y al final el resultado."),
        E(f"{S_LLAVES} Cuando Ema recorre el barrio preguntando por las pistas, ¿en qué parte de la historia está: inicio, desarrollo o desenlace?", "Desarrollo", "Es el intento de resolver el problema, no su presentación ni su final."),
    ],
    [
        E(f"Sobre «El último tren del pueblo», Pía dice: «El tema es la unión de los vecinos». Tomás dice: «El tema es que los niños venden periódicos». ¿Quién identifica mejor el tema? Responde Pía o Tomás.", "Pía", "El problema se resuelve porque los vecinos actúan juntos; vender periódicos es solo un detalle."),
        E("Un estudiante dice: «La obra es buena porque sí». ¿Qué le falta para discutir bien: a) una razón sacada de la historia b) una voz más fuerte c) más personajes?", "a", "Una discusión se apoya en partes de la historia que otros pueden comprobar."),
    ],
    [
        E(f"{S_LLAVES} ¿Cuál es la mejor pregunta para discutir la película: a) ¿Por qué cada vecino da a Ema una pista distinta y qué muestra eso? b) ¿Ema tiene llaves? c) ¿La película es larga?", "a", "Invita a razonar sobre la historia y no se responde con un dato."),
        E(f"{S_TREN} Si nadie hubiera actuado y la estación se hubiera cerrado, ¿seguiría siendo el tema la unión de los vecinos? Responde sí o no.", "No", "El tema surge de que el problema se resuelve gracias a la acción conjunta."),
    ],
    [E("Tu curso vio «El último tren del pueblo» y la profesora pide discutir el desenlace. ¿Qué intervención participa mejor: a) «Me gustó que el cierre se postergara, porque los vecinos lo lograron juntos.» b) «Me gustó porque estaba buena.»", "a", "Da una razón sacada del desenlace de la historia.")],
    [
        E("En una obra o película, ¿cómo se llama el problema central que mueve la historia?", "Conflicto", "Es el problema alrededor del cual ocurre todo lo demás."),
        E("¿Cómo se llama la parte que muestra cómo se resuelve el problema?", "Desenlace", "Cierra la historia."),
        E("¿Una opinión sobre una obra necesita una razón tomada de la historia? Responde sí o no.", "Sí", "Así los demás pueden comprobar o rebatir lo que dices."),
    ],
    ("Lee esta sinopsis: «Obra «El faro de Juana»: el pueblo de pescadores no tiene luz en su faro y los botes no pueden volver de noche. Juana, una niña, propone encender linternas en cada casa de la costa. Algunos vecinos no creen que sirva, pero al final todas las casas se iluminan y los botes regresan.» Conversa con una persona de tu casa o escribe: 1) conflicto, 2) desenlace, 3) un posible tema, 4) tu opinión con una razón tomada de la historia.",
     "Conflicto: el faro sin luz. Desenlace: los botes regresan. Tema: la colaboración. Opinión: me gustó el final porque la idea de Juana funcionó gracias a todos.",
     ["identifica el conflicto correctamente", "identifica el desenlace", "propone un tema que no es solo el argumento", "da una opinión con una razón de la historia"], ["cuatro respuestas escritas o dichas"], ["contar la historia sin separar los aspectos", "opinar sin razón"],
     "Si tu tema solo cuenta lo que pasa, pregúntate: ¿qué idea deja la historia sobre la vida?"),
    "Escribe un conflicto, un desenlace y un tema para una historia breve inventada por ti sobre un parque que se quiere cerrar.",
    "Piensa en una película que hayas visto y escribe su conflicto, su desenlace y su tema en tres frases.",
)

# ================================================================ OA 26 · clase 2
reg(
    OA26, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer las frases con distintos tonos.",
    "Aprenderé a describir cómo un actor usa su voz (volumen, tono, ritmo y pausas) para expresar emociones. Sirve para apreciar cómo una misma frase puede sentirse alegre, triste, enojada o asustada.",
    ["Sé reconocer emociones básicas.", "Sé que una frase puede decirse de distintas maneras."],
    [
        "En el teatro y en el cine, los actores comunican emociones con la voz. Los elementos de la voz que más cambian son cuatro. El volumen es qué tan fuerte o suave se habla. El tono es qué tan agudo o grave suena la voz. El ritmo es qué tan rápido o lento se dice. Las pausas son silencios breves entre palabras.",
        "Cada emoción suele tener su combinación. La alegría suele sonar aguda, rápida y con volumen medio o alto. La tristeza, lenta, suave y grave. El enojo, con volumen fuerte, ritmo firme y palabras marcadas. El miedo, con voz temblorosa, entrecortada, a veces en susurro. Son pistas frecuentes, no reglas fijas: un actor puede romperlas para sorprender, pero siempre lo hace por una razón.",
        "Para apreciar la voz de un actor, describe lo que oyes con estos cuatro elementos y conecta con la emoción que expresa. Por ejemplo: «dice ‘¡Ganamos!’ con voz aguda y rápida, por eso se nota la alegría». La descripción más útil nombra el elemento de la voz y la emoción que ayuda a expresar.",
    ],
    [("volumen", "qué tan fuerte o suave se habla"), ("tono", "qué tan aguda o grave suena la voz"), ("ritmo", "qué tan rápido o lento se habla"), ("pausa", "silencio breve entre palabras"), ("entrecortada", "dicha con cortes, sin fluir")],
    [
        ("Unir voz y emoción", "En una obra, la actriz dice «No quiero que te vayas» muy despacio, con voz suave y baja, haciendo pausas. ¿Qué emoción expresa?", ["Describo su voz: lenta, suave y con pausas.", "Esa combinación suele mostrar tristeza.", "Conecto la voz con la emoción."], "Tristeza, porque habla lento, suave y con pausas."),
        ("Elegir la voz para una emoción", "Un actor debe decir «¡Cuidado, viene el perro!» con miedo. ¿Qué voz conviene: a) susurro rápido y entrecortado b) voz lenta y grave de sueño?", ["El miedo se expresa con voz tensa y entrecortada.", "El susurro rápido y entrecortado lo muestra.", "Elijo la que calza con la emoción."], "a) susurro rápido y entrecortado."),
    ],
    [("Describir solo «habla fuerte» sin decir qué emoción expresa.", "Se nombra el sonido, pero no su efecto.", "Une el elemento de la voz con la emoción: «volumen fuerte, enojo»."), ("Creer que toda voz fuerte es enojo.", "Se piensa que hay una sola regla.", "Mira el contexto: un grito de gol es alegría.")],
    [
        E("Un actor dice «Qué bien, aprobé» con voz aguda y rápida. ¿Qué emoción expresa: alegría o tristeza?", "Alegría", "La voz aguda y rápida suele mostrar entusiasmo."),
        E("En la voz, ¿cómo se llama qué tan fuerte o suave se habla: volumen, ritmo o pausa?", "Volumen", "Mide la fuerza con que sale el sonido."),
        E("Una actriz habla lento, con voz suave y baja, y hace pausas. ¿Qué emoción se parece más: tristeza o enojo?", "Tristeza", "La lentitud y la suavidad suelen mostrar pena."),
    ],
    [
        E("Un personaje dice «¡Sal de mi cuarto!» con volumen fuerte y palabras muy marcadas. ¿Qué emoción expresa: enojo o sorpresa?", "Enojo", "El volumen fuerte y la firmeza marcan el enojo."),
        E("Para mostrar miedo en la frase «¿Quién anda ahí?», ¿qué voz conviene: a) susurro entrecortado b) voz alegre y rápida c) grito de victoria?", "a", "El miedo se expresa con voz tensa y entrecortada."),
        E("Una actriz hace una pausa larga antes de decir «Ganó el otro equipo». ¿Para qué sirve la pausa: a) mostrar que le cuesta decirlo b) mostrar que se quedó dormida?", "a", "La pausa puede marcar emoción o dificultad antes de una noticia."),
    ],
    [
        E("Describe con un elemento de la voz cuál de estas frases corresponde a la alegría: a) «Hablaba muy lento y bajito» b) «Hablaba rápido y con voz aguda, riendo». Responde a o b.", "b", "La rapidez y la voz aguda suelen acompañar la alegría."),
        E("Ordena de menor a mayor volumen: a) un grito b) un susurro c) una conversación normal. Escribe las letras.", "b, c, a", "Del más suave al más fuerte: susurro, conversación y grito."),
        E("Un actor dice «Estoy tranquilo» con voz temblorosa y entrecortada. ¿Qué emoción deja ver realmente su voz: calma o nervios?", "Nervios", "La voz entrecortada y temblorosa revela nerviosismo."),
    ],
    [
        E("Una actriz dice «Gracias por todo» con voz baja, lenta y sin mirar. Otra actriz dice la misma frase con voz aguda y sonriendo. ¿Qué diferencia comunica la voz: a) la primera suena a despedida triste y la segunda a gratitud alegre b) no hay ninguna diferencia?", "a", "El mismo texto cambia según el volumen, el tono y el ritmo."),
        E("Si un actor grita de alegría al ganar un premio, ¿se cumple que toda voz fuerte es enojo? Responde sí o no.", "No", "Hay que mirar el contexto: gritar también puede mostrar entusiasmo."),
    ],
    [
        E("Describe correctamente cómo se oye este fragmento: «Dice ‘te lo juro’ en un susurro, muy rápido y con pausas cortas». ¿Qué emoción expresa mejor: a) miedo o urgencia b) aburrimiento?", "a", "El susurro rápido y entrecortado transmite miedo o urgencia."),
        E("Un actor dice «Hoy ganamos» con volumen alto, voz aguda y ritmo rápido. ¿Qué elemento de su voz ayuda más a mostrar entusiasmo: el tono agudo o el silencio?", "El tono agudo", "La voz aguda y vivaz muestra energía alegre."),
    ],
    [E("En la función de curso, tu compañero Mateo debe decir «¡Lo logramos!» con alegría. Le propones: a) voz aguda, rápida y fuerte b) voz grave, lenta y suave. ¿Cuál le recomiendas?", "a", "Esa combinación de voz transmite entusiasmo.")],
    [
        E("¿Cómo se llaman los silencios breves entre palabras?", "Pausas", "Marcan emoción, suspenso o énfasis."),
        E("¿Qué elemento de la voz mide qué tan rápido se habla: ritmo o tono?", "Ritmo", "El ritmo es la velocidad."),
        E("¿La voz de un actor expresa emociones? Responde sí o no.", "Sí", "Lo hace con el volumen, el tono, el ritmo y las pausas."),
    ],
    ("Lee en voz alta la frase «No sé qué hacer» de cuatro formas: 1) con tristeza, 2) con miedo, 3) con enojo, 4) con alegría sorprendida. Para cada una, anota cómo cambiaste volumen, tono y ritmo (por ejemplo: «más lento y suave»). Si puedes, pide a una persona de tu casa que adivine la emoción de cada versión.",
     "Tristeza: más lento, suave y grave, con una pausa antes de «hacer».",
     ["lee la frase cuatro veces con emociones distintas", "anota al menos dos cambios de la voz por emoción", "los cambios son coherentes con la emoción"], ["cuatro anotaciones breves"], ["describir solo con «más fuerte» o «más bajo»", "usar la misma voz en todas"],
     "Si la persona no adivinó, exagera un poco más el cambio de ritmo o de pausas."),
    "Elige otra frase corta, como «Mira lo que encontré», y anota cómo suena con sorpresa y con desconfianza.",
    "Escucha un diálogo en una película o serie con una persona de tu casa y describe con volumen, tono y ritmo cómo habla un personaje enojado.",
)

# ================================================================ OA 26 · clase 3
reg(
    OA26, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: un espejo o una persona de tu casa para ensayar gestos.",
    "Aprenderé a describir cómo la gestualidad de un actor (rostro, manos, postura, mirada y movimiento) expresa emociones. Sirve para apreciar lo que un personaje siente aunque no lo diga con palabras.",
    ["Sé describir cómo se usa la voz para expresar emociones.", "Sé reconocer emociones básicas."],
    [
        "La gestualidad es todo lo que el cuerpo del actor comunica sin hablar: la expresión del rostro, la mirada, las manos, la postura y los movimientos. En el teatro, donde el público está lejos, los gestos suelen ser amplios para que se vean. En el cine, la cámara se acerca y un pequeño gesto, como una ceja levantada, ya dice mucho.",
        "Cada emoción tiene gestos frecuentes. La tristeza suele mostrarse con hombros caídos, mirada al suelo y pasos lentos. El enojo, con ceño fruncido, puños apretados y cuerpo tenso. La alegría, con sonrisa amplia, saltos o brazos abiertos. El miedo, con cuerpo encogido, manos temblorosas y pasos hacia atrás. Estas son pistas, y el contexto ayuda a decidir.",
        "A veces el gesto y la voz no coinciden a propósito. Si un personaje dice «estoy bien» pero mira al suelo con los hombros caídos, el público entiende que está triste y quiere ocultarlo. Para apreciar una actuación, describe el gesto concreto que ves y di qué emoción te hace pensar.",
    ],
    [("gestualidad", "lo que el cuerpo comunica sin palabras"), ("postura", "manera de colocar el cuerpo"), ("ceño fruncido", "cejas juntas, gesto de enojo o preocupación"), ("mirada", "hacia dónde y cómo mira una persona"), ("contradicción", "cuando dos cosas no coinciden, como gesto y palabra")],
    [
        ("Leer un gesto", "Un personaje camina con hombros caídos, la mirada en el suelo y pasos lentos. ¿Qué emoción comunica?", ["Observo postura, mirada y pasos.", "Hombros caídos, mirada baja y lentitud suelen mostrar tristeza.", "Uno los gestos y concluyo."], "Tristeza."),
        ("Detectar contradicción", "Un personaje dice «Estoy feliz de que te vayas» pero aprieta los puños y mira hacia otro lado. ¿Qué comunica el gesto?", ["Comparo lo que dice con lo que hace.", "Puños apretados y mirada evasiva muestran molestia.", "El gesto contradice la frase."], "Que en realidad está molesto o dolido, aunque diga lo contrario."),
    ],
    [("Hablar solo de la cara.", "Se olvida que el cuerpo entero actúa.", "Revisa también postura, manos, mirada y movimiento."), ("Decir «se ve raro» sin describir el gesto.", "Es una impresión sin evidencia.", "Nombra el gesto exacto: «aprieta los puños».")],
    [
        E("Una actriz abre los brazos, salta y sonríe ampliamente. ¿Qué emoción comunica: alegría o miedo?", "Alegría", "Los saltos, los brazos abiertos y la sonrisa suelen mostrar alegría."),
        E("Un personaje retrocede con el cuerpo encogido y las manos temblando. ¿Qué siente: miedo o enojo?", "Miedo", "Retroceder y temblar son gestos típicos de miedo."),
        E("Un personaje frunce el ceño y aprieta los puños. ¿Qué emoción comunica: enojo o tristeza?", "Enojo", "El ceño fruncido y los puños apretados muestran tensión y enojo."),
    ],
    [
        E("En una obra, una niña baja la cabeza, se encorva y arrastra los pies. ¿Qué otro gesto confirma esa tristeza: a) caminar con la mirada en el suelo b) saltar sonriendo c) levantar los brazos?", "a", "Caminar con la mirada en el suelo se suma a la cabeza baja y los pies arrastrados."),
        E("En el teatro, ¿por qué los gestos suelen ser amplios: a) para que el público lejano los vea b) para no hablar?", "a", "El público está lejos y necesita ver bien el gesto."),
        E("Una actriz levanta una ceja y entrecierra los ojos mirando a otro personaje. ¿Qué comunica: desconfianza o felicidad?", "Desconfianza", "Ceja alzada y ojos entrecerrados muestran duda."),
    ],
    [
        E("Un personaje dice «Estoy bien», pero tiene los hombros caídos y los ojos hacia el suelo. ¿Qué indica el gesto: a) que está triste y lo oculta b) que realmente está feliz?", "a", "El gesto contradice la palabra y muestra lo que siente."),
        E("Ordena de menor a mayor tensión del cuerpo: a) puños apretados y pasos firmes b) cuerpo relajado c) hombros algo tensos. Escribe las letras.", "b, c, a", "Del cuerpo relajado al muy tenso."),
        E("En el cine, la cámara se acerca a la cara de un actor que tiembla apenas el labio. ¿Qué ventaja da este plano cercano: a) se ve un gesto pequeño b) se oyen mejor los efectos?", "a", "La cámara cerca permite ver gestos pequeños."),
    ],
    [
        E("Dos actores dicen «Me voy». El primero camina lento, con la cabeza gacha. El segundo sale rápido, cerrando la puerta con fuerza. ¿Qué diferencia de emoción comunican los gestos: tristeza frente a enojo? Responde sí o no.", "Sí", "Cabeza gacha y lentitud sugieren pena; fuerza al cerrar sugiere enojo."),
        E("Un estudiante dice: «Se ve raro». ¿Qué le falta para apreciar bien: a) nombrar el gesto exacto que ve b) hablar más fuerte?", "a", "La apreciación se apoya en gestos concretos observables."),
    ],
    [
        E("Un personaje abre un regalo, se tapa la boca con las manos, abre mucho los ojos y da un salto. ¿Qué emoción es más probable: sorpresa alegre o aburrimiento?", "Sorpresa alegre", "Taparse la boca, ojos grandes y un salto muestran sorpresa positiva."),
        E("Un actor camina en puntas de pie, mira hacia atrás y se encoge cada vez que cruje el piso. ¿Qué intención del personaje comunica: pasar sin ser visto o llamar la atención?", "Pasar sin ser visto", "Caminar en puntas y mirar hacia atrás muestra sigilo."),
    ],
    [E("En tu función de curso, tu compañero Tomás debe mostrar vergüenza al ser llamado al frente, sin hablar. ¿Qué gestos le sugieres: a) mirar al suelo, encoger los hombros y sonreír tímido b) saltar con los brazos abiertos?", "a", "Esos gestos muestran timidez y vergüenza.")],
    [
        E("¿Cómo se llama lo que el cuerpo comunica sin palabras?", "Gestualidad", "Incluye rostro, manos, postura, mirada y movimiento."),
        E("¿Hombros caídos y mirada baja muestran más tristeza o alegría?", "Tristeza", "Es un gesto frecuente de pena."),
        E("Si el gesto contradice lo que dice el personaje, ¿qué comunica el gesto? Responde lo que siente o lo que dice.", "Lo que siente", "El gesto revela la emoción real."),
    ],
    ("Describe cómo mostrarías sin palabras estas tres situaciones, con al menos tres gestos cada una (rostro, manos, postura, mirada o movimiento): 1) esperas un resultado importante, estás nervioso; 2) te dan una noticia muy buena; 3) te dan una mala noticia pero intentas disimular. Si puedes, ensaya frente a un espejo o a una persona de tu casa.",
     "1) Muerdo mis uñas, miro la puerta y camino de un lado a otro.",
     ["usa al menos tres gestos por situación", "los gestos son coherentes con la emoción", "en la tercera se nota el intento de disimular"], ["tres descripciones escritas o ensayadas"], ["describir solo la cara", "usar el mismo gesto para dos emociones"],
     "Si dos situaciones se parecen, cambia el ritmo del movimiento: ¿más rápido, más lento, más tenso?"),
    "Escribe un personaje que dice «Qué bueno» pero con gestos de que no le gusta nada. Describe los gestos.",
    "Observa un recreo y anota tres gestos distintos de personas y qué emoción te parecen mostrar.",
)

# ================================================================ OA 26 · clase 4
reg(
    OA26, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una linterna y una persona de tu casa para probar el efecto de la luz.",
    "Aprenderé a identificar los recursos que usan las obras para provocar un efecto en la audiencia: efectos de sonido, música, iluminación, vestuario y escenografía. Sirve para explicar por qué una escena nos da miedo, tranquilidad o alegría.",
    ["Sé que los actores usan voz y gestos para expresar emociones.", "Sé describir qué siento al ver una escena."],
    [
        "Además de los actores, las obras usan recursos que buscan provocar un efecto en el público. Los efectos de sonido son ruidos como una puerta que cruje, una lluvia o un trueno. La música acompaña la escena y cambia el ánimo. La iluminación usa luz fuerte, tenue, de colores o focos que destacan a un personaje. El vestuario y la escenografía, es decir, la ropa y los objetos del escenario, también aportan.",
        "Cada recurso se elige por un efecto. Una música lenta y grave puede crear suspenso. Una luz azul tenue puede dar sensación de noche o frío. Un foco que ilumina solo a un personaje dirige la atención hacia él. Un redoble de tambor antes de un anuncio genera expectativa. Para apreciar la obra, identifica el recurso y di qué efecto provoca en ti.",
        "Cuando analices, evita decir solo «se oyó música». Di qué tipo de música y qué efecto tiene: «música lenta y grave crea suspenso». Si un recurso no cambia lo que sentimos, tal vez no cumple su función; y si cambia mucho el ánimo, probablemente fue una buena decisión del equipo de la obra.",
    ],
    [("efecto de sonido", "ruido que se agrega para dar realismo o emoción"), ("iluminación", "uso de la luz en el escenario"), ("suspenso", "tensión de esperar algo que no sabemos"), ("escenografía", "objetos y fondos del escenario"), ("expectativa", "espera de que algo ocurra")],
    [
        ("Recurso y efecto", "En una escena, se apagan las luces, suena un crujido lento y una música grave y baja. ¿Qué efecto busca provocar en la audiencia?", ["Identifico los recursos: apagón, crujido y música grave.", "Juntos hacen esperar algo malo que no se ve.", "El efecto es suspenso o miedo."], "Suspenso o miedo."),
        ("Elegir el recurso", "Quieres que el público sienta alegría en la escena de una fiesta. ¿Qué recursos eliges: a) música rápida y luces cálidas y brillantes b) música lenta y luz azul tenue?", ["La alegría se asocia con energía.", "La música rápida y la luz brillante dan esa sensación.", "Elijo la que calza con el efecto."], "a) música rápida y luces cálidas y brillantes."),
    ],
    [("Decir solo «había música» sin decir qué efecto tiene.", "Se nombra el recurso, pero no su función.", "Añade el tipo de música y el efecto: «lenta y grave, crea suspenso»."), ("Creer que más sonidos siempre es mejor.", "Se piensa que el exceso impresiona.", "Un recurso funciona si ayuda al efecto, no por cantidad.")],
    [
        E("Antes de que aparezca el villano suena un redoble de tambor que sube cada vez más fuerte. ¿Qué efecto busca: expectativa o aburrimiento?", "Expectativa", "El sonido creciente hace esperar lo que viene."),
        E("En una obra, un foco ilumina solo a una niña y el resto del escenario queda a oscuras. ¿Qué logra la luz: dirigir la atención hacia ella o esconder el escenario?", "Dirigir la atención hacia ella", "El foco señala al personaje importante."),
        E("Un trueno suena justo cuando entra el fantasma. ¿Qué tipo de recurso es el trueno: efecto de sonido o vestuario?", "Efecto de sonido", "Es un ruido agregado a la escena."),
    ],
    [
        E("Una luz azul tenue y música suave acompañan una escena nocturna. ¿Qué sensación da: calma o prisa?", "Calma", "La luz tenue y la música suave son tranquilizadoras."),
        E("¿Qué recurso conviene para que el público sienta que llueve: a) efecto de sonido de lluvia b) vestuario de verano c) música de fiesta?", "a", "El sonido de lluvia reproduce lo que se quiere mostrar."),
        E("Los actores usan abrigos gruesos y bufandas, y el fondo muestra nieve pintada. ¿Qué dos recursos son: vestuario y escenografía o música e iluminación?", "Vestuario y escenografía", "Los abrigos son vestuario y el fondo pintado es escenografía."),
    ],
    [
        E("Ordena según cuánta tensión crea la escena: a) crujido, apagón y música grave b) música tranquila y luz clara c) luz tenue y silencio. Escribe de menos a más tensión.", "b, c, a", "La suma de apagón, crujido y música grave crea más tensión que lo demás."),
        E("Una escena muestra un funeral con música alegre y luces de colores. ¿Qué efecto produce probablemente: confusión o consuelo?", "Confusión", "La música y las luces contradicen la situación triste."),
        E("En una película se corta la música justo antes de un salto del personaje. ¿Qué efecto crea el silencio súbito: a) sorpresa o tensión b) risa fuerte?", "a", "El silencio repentino deja al público a la espera."),
    ],
    [
        E("Un estudiante dice: «La escena da miedo porque hay música». ¿Qué le falta a su apreciación: a) decir qué tipo de música y cómo afecta b) decir que le gusta?", "a", "Una buena apreciación nombra la característica del recurso y su efecto."),
        E("En un teatro hay pocos recursos y el público se sigue emocionando gracias a los actores. ¿Es verdad que el efecto depende siempre de más recursos? Responde sí o no.", "No", "Puede lograrse con pocos recursos si se usan bien."),
    ],
    [
        E("Un director quiere que el público sienta que la escena ocurre en un día caluroso. ¿Qué iluminación elige: a) luz amarilla intensa b) luz azul tenue?", "a", "La luz amarilla intensa sugiere calor."),
        E("Si en una escena de tristeza suena una música lenta con pocos instrumentos y la luz baja lentamente, ¿qué efecto se busca: tristeza suave o entusiasmo?", "Tristeza suave", "La música lenta y la luz baja profundizan la tristeza."),
    ],
    [E("Tu curso prepara una escena donde un personaje entra a una casa vacía de noche. Tienes tres recursos para elegir: a) puerta que cruje, luz tenue y silencio b) risas y música de fiesta c) luz brillante y aplausos. ¿Cuál crea suspenso?", "a", "Crujido, poca luz y silencio generan tensión.")],
    [
        E("¿Cómo se llaman los ruidos agregados a una escena, como un trueno o una puerta?", "Efectos de sonido", "Dan realismo y emoción."),
        E("¿Un foco que ilumina a un solo personaje dirige o aleja la atención del público?", "Dirige", "La luz señala lo importante."),
        E("¿Un recurso se elige para provocar un efecto en la audiencia? Responde sí o no.", "Sí", "Por eso hay que describir qué efecto busca."),
    ],
    ("Lee esta escena: «Un niño entra de noche a la cocina para tomar agua. Todo está a oscuras. Escucha un goteo lento. De pronto, un ruido metálico en la despensa. El niño se queda inmóvil». Propone un recurso de sonido, uno de iluminación y uno de música para que el público sienta suspenso y explica en una frase el efecto de cada uno.",
     "Sonido: goteo lento. Iluminación: luz muy tenue. Música: un tono grave sostenido. Todos crean tensión.",
     ["propone un recurso de sonido, uno de luz y uno de música", "cada recurso es coherente con el suspenso", "explica el efecto de cada uno"], ["tres recursos con su efecto, por escrito"], ["nombrar el recurso sin el efecto", "elegir recursos alegres para una escena de miedo"],
     "Si un recurso no calza, pregúntate: ¿esto hace que el público espere, se asuste o se relaje?"),
    "Escribe qué recursos usarías en una escena de reconciliación entre dos amigos.",
    "Fíjate en la música de la escena de una película que veas esta semana y anota qué sentías al oírla.",
)

# ================================================================ OA 26 · clase 5
reg(
    OA26, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para comparar versiones leídas en voz alta.",
    "Aprenderé a comparar dos interpretaciones de una misma escena y a decidir cuál se ajusta mejor a la historia usando evidencia. Sirve para entender que una obra puede interpretarse de distintas maneras, pero no todas calzan igual con lo que ocurre.",
    ["Sé describir voz, gestos y recursos de una escena.", "Sé dar una opinión con una razón."],
    [
        "Una interpretación es la manera como un actor o un director decide mostrar un personaje o una escena. Dos actores pueden decir la misma frase de modos muy distintos, y ambos pueden ser válidos. Comparar interpretaciones significa describir en qué se parecen y en qué se diferencian en voz, gestos y recursos, y qué emoción o idea transmite cada una.",
        "Para decidir cuál se ajusta mejor, hay que volver a la historia. ¿Qué sabemos del personaje? ¿Qué le acaba de pasar? Una interpretación calza mejor si es coherente con ese contexto. Por ejemplo, si un personaje acaba de perder algo muy querido, una voz alegre sería extraña, salvo que la obra explique que oculta su pena.",
        "Al comparar, usa expresiones como «en cambio», «a diferencia de» o «ambas». Y siempre apoya tu preferencia con evidencia: «Prefiero la versión B porque su voz baja y su mirada al suelo calzan con la tristeza del personaje». Preferir una versión no significa que la otra esté mal, sino que calza menos con el contexto.",
    ],
    [("interpretación", "manera de mostrar un personaje o escena"), ("contexto", "lo que ocurre antes y alrededor de una escena"), ("coherente", "que calza con el resto y no se contradice"), ("a diferencia de", "expresión para marcar una diferencia"), ("evidencia", "detalle observable que respalda una opinión")],
    [
        ("Comparar dos versiones", "Contexto: Lucas acaba de enterarse de que su mejor amigo se mudará. Dice «Qué bien por él». Versión A: voz baja, mirada al suelo, pausa antes de hablar. Versión B: voz aguda, rápida, sonriendo ampliamente. ¿Qué versión calza mejor con el contexto?", ["Leo el contexto: noticia triste para Lucas.", "Comparo: A muestra pena; B, alegría total.", "A calza mejor porque su gesto y voz son coherentes con la pérdida."], "La versión A."),
        ("Qué comparten dos versiones", "En las dos versiones de la escena de Lucas, ¿qué tienen en común?", ["Busco lo que no cambia.", "Ambas dicen la misma frase «Qué bien por él».", "Lo que cambia es la forma de decirla."], "Ambas dicen el mismo texto: «Qué bien por él»."),
    ],
    [("Decir «la versión B es mala» sin razón.", "Se juzga sin comparar con el contexto.", "Explica en qué no calza: «su voz alegre no calza con la noticia triste»."), ("Pensar que solo existe una interpretación correcta.", "Se confunde interpretación con dato.", "Acepta varias, pero evalúa cuál calza mejor con el contexto.")],
    [
        E("Dos actores dicen la misma frase «Lo siento». ¿Se trata de la misma interpretación o de interpretaciones distintas si cambian voz y gestos?", "Interpretaciones distintas", "La interpretación incluye cómo se dice, no solo qué se dice."),
        E("En la expresión «a diferencia de», ¿qué se marca: una semejanza o una diferencia?", "Una diferencia", "Esa expresión contrasta dos cosas."),
        E("Para decidir qué interpretación calza mejor, ¿qué hay que mirar: el contexto de la historia o el color del telón?", "El contexto de la historia", "Allí se ve qué siente y vive el personaje."),
    ],
    [
        E("Contexto: Ana acaba de ganar el campeonato. Dice «Lo logramos». Versión A: voz aguda, brazos arriba, sonrisa. Versión B: voz plana, mirada baja. ¿Cuál calza mejor con el contexto: A o B?", "A", "La alegría de ganar es coherente con la voz aguda y los brazos arriba."),
        E("En las versiones de Ana, ¿qué texto repiten las dos: «Lo logramos» o «Lo siento»?", "Lo logramos", "Es la frase que dicen ambas versiones."),
        E("¿Qué conector sirve para decir que dos versiones coinciden: «a diferencia de» o «ambas»?", "Ambas", "«Ambas» reúne lo que comparten."),
    ],
    [
        E("Contexto: un personaje acaba de descubrir que le mintieron. Dice «Gracias por contarme la verdad». Versión A: voz cálida y sonrisa. Versión B: voz fría, brazos cruzados, mirada firme. ¿Cuál calza mejor y por qué? Responde con la letra.", "B", "El enojo contenido calza con la reacción ante una mentira."),
        E("Ordena una comparación: a) A diferencia de A, la versión B mira de frente. b) Ambas versiones dicen la misma frase. c) Por eso prefiero la versión B. Escribe las letras en un orden lógico.", "b, a, c", "Primero lo común, luego la diferencia y por último la conclusión."),
        E("Dos actores interpretan a un abuelo: uno cansado y lento, otro ágil y bromista. Si la obra dice que el abuelo es muy enérgico, ¿cuál calza mejor?", "El ágil y bromista", "Es coherente con lo que dice la obra del personaje."),
    ],
    [
        E("Un estudiante dice: «La versión A es mejor porque sí». ¿Qué le falta para comparar bien: a) citar un detalle de la voz o los gestos y el contexto b) más fuerza en la voz?", "a", "Comparar bien exige evidencia observable y su relación con el contexto."),
        E("Si dos interpretaciones son distintas, ¿una de ellas siempre está equivocada? Responde sí o no.", "No", "Varias interpretaciones pueden ser válidas, aunque calcen distinto."),
    ],
    [
        E("Contexto: una niña oculta que tiene miedo a hablar en público. Dice «Estoy tranquila». Versión A: voz firme, manos quietas. Versión B: voz temblorosa y manos sudando. ¿Cuál deja ver mejor el miedo que se oculta?", "B", "La voz temblorosa contradice la frase y muestra lo que siente."),
        E("En esa escena, ¿qué ventaja tiene la versión A si la obra quiere mostrar que el personaje logra disimular: a) muestra control b) muestra enojo?", "a", "La voz firme sugiere que disimula con éxito."),
    ],
    [E("En el taller de teatro, dos compañeros muestran la frase «Me voy ahora». Camila la dice despacio, con la mirada baja; Joaquín la dice fuerte, de frente. La escena cuenta que el personaje se va porque lo trataron injustamente y siente rabia. ¿Cuál interpretación calza mejor: la de Camila o la de Joaquín?", "La de Joaquín", "Su fuerza y su mirada de frente calzan con la rabia por el trato injusto.")],
    [
        E("¿Qué es comparar interpretaciones: mirar sus semejanzas y diferencias o elegir la más famosa?", "Mirar sus semejanzas y diferencias", "Se describen y se contrastan con evidencia."),
        E("¿Hay que volver al contexto para decidir qué interpretación calza mejor? Responde sí o no.", "Sí", "El contexto muestra qué siente el personaje."),
        E("¿Cuál palabra introduce una semejanza: «ambas» o «a diferencia de»?", "Ambas", "Reúne lo que comparten."),
    ],
    ("Lee esta escena y compara dos versiones. Contexto: Sofía recibe de su hermano un regalo que le encanta y dice «No tenías que molestarte». Versión A: voz suave, ojos brillantes y abrazo. Versión B: voz seca, brazos cruzados y mirada esquiva. Escribe una comparación de tres a cuatro líneas con «ambas» y «a diferencia de», y concluye cuál calza mejor y por qué.",
     "Ambas versiones dicen la misma frase. A diferencia de B, la versión A muestra cariño con un abrazo. Prefiero A porque el contexto es de un regalo que le encanta.",
     ["usa «ambas» y «a diferencia de»", "menciona al menos dos detalles de voz o gestos", "concluye con una razón basada en el contexto"], ["comparación escrita de tres a cuatro líneas"], ["decir «una es mala» sin razón", "no volver al contexto"],
     "Si tu conclusión no usa el contexto, agrega: «Porque en la historia el personaje…»."),
    "Escribe dos formas de decir «Buenos días» para dos personajes distintos y explica qué las diferencia.",
    "Dile a una persona de tu casa una frase con dos interpretaciones diferentes y pídele que describa qué cambió.",
)

# ================================================================ OA 26 · clase 6
reg(
    OA26, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer tu apreciación en voz alta.",
    "Aprenderé a escribir y revisar una apreciación breve de una obra, pensando en quién la leerá o escuchará. Sirve para compartir mi opinión de una obra con razones claras y con evidencia de la historia, los actores y los recursos.",
    ["Sé discutir la historia de una obra.", "Sé describir voz, gestos y recursos con su efecto."],
    [
        "Una apreciación es un texto breve en que expresas tu opinión sobre una obra apoyándote en evidencia. Una buena apreciación tiene cuatro partes. Primero presenta la obra con su título y una idea de la historia. Luego comenta un aspecto de la actuación, como voz o gestos, con un ejemplo. Después explica un recurso (sonido, música, luz) y su efecto. Al final da tu opinión con una razón.",
        "Revisar para una audiencia significa pensar en quién lo leerá. Si tus lectores no vieron la obra, debes explicar un poco la historia, pero sin contar todo el final. Usa un lenguaje claro y evita frases como «estuvo bueno» sin una razón. Elimina las repeticiones y verifica que cada afirmación tenga evidencia: ¿qué escena, voz o recurso muestra lo que dices?",
        "Un buen método de revisión es leer tu texto como si fueras otra persona y preguntarte: ¿se entiende?, ¿qué evidencia tiene cada opinión?, ¿explico el efecto de cada recurso?, ¿cuento demasiado del final? Marca lo que falte y mejóralo antes de entregar.",
    ],
    [("apreciación", "texto breve con opinión sobre una obra, apoyada en evidencia"), ("audiencia", "personas que leerán o escucharán"), ("evidencia", "detalle de la obra que respalda lo que dices"), ("revisar", "leer con atención para mejorar un texto"), ("final", "parte donde termina la historia; conviene no contarlo todo")],
    [
        ("Detectar la parte que falta", "Borrador: «La obra «El faro de Juana» me gustó mucho. La música daba suspenso en la escena de la tormenta. Los actores estuvieron muy bien». ¿Qué falta?", ["Reviso las cuatro partes: obra e historia, actuación con ejemplo, recurso con efecto, opinión con razón.", "La actuación solo dice «muy bien» sin ejemplo.", "También falta la razón de la opinión."], "Falta una idea de la historia, un ejemplo concreto de actuación (la voz o los gestos) y una razón para la opinión."),
        ("Mejorar una frase", "Mejora la frase «Estuvo bueno». ¿Cuál versión es mejor: a) «Me gustó cuando Juana, con voz firme, convenció a los vecinos.» b) «Estuvo muy bueno.»", ["Busco la que incluya una escena, un recurso o un detalle.", "La a) nombra una escena y la voz de la actriz.", "Tiene evidencia."], "a)"),
    ],
    [("Contar todo el final de la obra.", "Se piensa que contar más es explicar mejor.", "Cuenta lo necesario y deja el final sin revelar."), ("Escribir solo adjetivos como «lindo» o «fome».", "No se justifica la opinión.", "Agrega la escena o el detalle que sostiene el adjetivo.")],
    [
        E("Una apreciación comienza presentando la obra con su título. ¿Esta parte va al principio o al final?", "Al principio", "Primero se presenta la obra."),
        E("En una apreciación, ¿qué se comenta de la actuación: la voz y los gestos o el precio de la entrada?", "La voz y los gestos", "Son aspectos de la interpretación de los actores."),
        E("¿Para quién revisamos una apreciación: para la audiencia que la leerá o solo para nosotros?", "Para la audiencia que la leerá", "Debe entenderse para quien no vio la obra."),
    ],
    [
        E("Frase: «Los actores estuvieron muy bien». ¿Qué le falta: a) un ejemplo concreto de voz o gesto b) más adjetivos?", "a", "Sin un ejemplo, la opinión no tiene evidencia."),
        E("¿Cuál frase explica un recurso con su efecto: a) «La música lenta y grave creó suspenso en la tormenta.» b) «Había música.»", "a", "Nombra el tipo de música y el efecto."),
        E("Si los lectores no vieron la obra, ¿qué debes incluir: una pequeña idea de la historia o ninguna información?", "Una pequeña idea de la historia", "Así entienden de qué obra hablas."),
    ],
    [
        E("Ordena las partes de una apreciación: a) opinión con una razón b) presentar la obra c) comentar la actuación d) explicar un recurso con su efecto. Escribe las letras.", "b, c, d, a", "Se parte con la obra, luego actuación y recurso, y se cierra con la opinión."),
        E("Revisa: «Fui a ver una obra. Estuvo bueno. Me gustó mucho». ¿Qué problema principal tiene: no tiene evidencia o es demasiado larga?", "No tiene evidencia", "Solo dice gustos, sin escenas, voces o recursos."),
        E("Un texto dice: «Al final, Juana descubre que el culpable era el alcalde y todos lo celebran». Si el lector no vio la obra, ¿qué problema tiene: revela el final o no menciona el título? Elige el principal.", "Revela el final", "Cuenta el desenlace completo."),
    ],
    [
        E("Dos estudiantes escriben su opinión final. Marta: «Recomiendo la obra porque la música y la luz hacen sentir miedo en la tormenta». Raúl: «Recomiendo la obra porque sí». ¿Cuál apreciación está mejor justificada?", "Marta", "Da una razón con recursos y su efecto."),
        E("Si en el borrador falta explicar el efecto de la luz, ¿qué agregas: una frase con el efecto de la luz o un adjetivo más?", "Una frase con el efecto de la luz", "Se completa la parte que falta."),
    ],
    [
        E("Mejora la frase para una audiencia que no vio la película: «La parte de Ema fue buena». ¿Cuál es mejor: a) «Me gustó cuando Ema pregunta a los vecinos con voz insegura, porque se nota su nerviosismo.» b) «Ema fue buena.»", "a", "La a) da escena, voz y razón."),
        E("En una revisión, ¿qué debe hacerse con una opinión sin evidencia: borrarla siempre o apoyarla con un detalle?", "Apoyarla con un detalle", "Lo ideal es mejorar la opinión con evidencia."),
    ],
    [E("Tu curso recibirá apreciaciones de la obra de teatro de un curso menor. Cada texto debe tener al menos una razón con evidencia. ¿Cuál cumple: a) «Me gustó porque las luces rojas hicieron sentir la tensión del duelo.» b) «Me gustó porque era entretenida.»", "a", "La a) menciona un recurso y su efecto.")],
    [
        E("¿Cuál es la última parte de una apreciación: la opinión con una razón o el título?", "La opinión con una razón", "Cierra la apreciación."),
        E("¿Cuenta todo el final de la obra una buena apreciación? Responde sí o no.", "No", "Se evita arruinar la sorpresa a quien no la vio."),
        E("¿Se debe revisar un texto antes de entregarlo? Responde sí o no.", "Sí", "Revisar permite completar lo que falta."),
    ],
    ("Lee este borrador: «La obra «Un día en el mercado» fue entretenida. Los actores hablaban fuerte. Me gustó». Reescríbelo en cuatro frases agregando: 1) una idea de la historia (inventa una breve y sencilla), 2) un ejemplo de voz o gesto, 3) un recurso con su efecto, 4) una opinión con razón. Luego revisa que sirva para un lector que no vio la obra.",
     "«Un día en el mercado» cuenta cómo un niño ayuda a una vendedora. La actriz hablaba rápido y con gestos amplios, y mostraba prisa. Los sonidos de voces y monedas hacían sentir el bullicio. Me gustó porque se sentía como un mercado real.",
     ["tiene las cuatro partes", "incluye evidencia concreta", "no cuenta todo el final", "se entiende para quien no vio la obra"], ["texto de cuatro frases"], ["frases sin evidencia", "contar el final"],
     "Marca cada frase con una palabra: HISTORIA, ACTUACIÓN, RECURSO u OPINIÓN. Si falta una, agrégala."),
    "Reescribe esta frase para que tenga evidencia: «El teatro de ayer fue lindo».",
    "Escribe una apreciación de tres frases sobre una escena de una película que hayas visto.",
)

"""Cuaderno del estudiante, 3.º básico Lenguaje y Comunicación: OA 25 (experiencia y lenguaje teatral) y OA 26 (conversación grupal)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA25, OA26 = "LE03 OA 25", "LE03 OA 26"
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


# ================================================================ OA 25 · clase 1
reg(
    OA25, 1,
    "Este cuaderno, lápiz y una hoja. Si puedes, una obra en vivo o grabada con una persona de tu casa; si no, usa el afiche y las escenas escritas aquí.",
    "Aprenderé a prepararme como público: leer un afiche, acordar cómo cuidar la función y llevar una pregunta para observar. Sirve para disfrutar una obra y entender mejor lo que pasa en el escenario.",
    ["Sé que una obra la cuentan personas con su voz y su cuerpo.", "Sé leer títulos, días y horas."],
    [
        "Ver una obra de teatro es distinto de ver una película, porque los actores están ahí, en vivo, y nos ven y nos escuchan. El teatro es un género: una forma de contar historias para que personas las representen ante un público. El público es el grupo de personas que mira y escucha la función. Antes de ir, leemos el afiche, que dice el título, el lugar, el día, la hora y a veces cuánto dura.",
        "Un buen público cuida la función con acuerdos: llegar unos minutos antes, apagar el celular, no hablar mientras los actores hablan, reír cuando algo es gracioso y aplaudir al final. Los acuerdos sirven para que todos disfruten; no sirven para quedarse sin sentir nada.",
        "También ayuda llevar una pregunta para observar, por ejemplo: ¿qué problema tiene el personaje? o ¿cómo muestra su alegría con el cuerpo? Una pregunta así nos hace mirar la escena entera y no solo el decorado, que es lo que hay pintado o armado en el escenario.",
    ],
    [("obra", "historia que se cuenta en el teatro"), ("función", "cada vez que se presenta una obra"), ("público", "personas que miran y escuchan la función"), ("afiche", "cartel que dice título, lugar, día y hora"), ("decorado", "objetos y telones que forman el lugar de la escena")],
    [
        ("Leer un afiche", "Afiche: «La señora Pelusa y el viento. Teatro Municipal. Sábado, 17:00. Duración: 50 minutos». ¿A qué hora termina la función?", ["Empieza a las 17:00.", "Dura 50 minutos: 17:00 más 50 minutos.", "Cincuenta minutos después de las 17:00 son las 17:50."], "Termina a las 17:50."),
        ("Elegir una pregunta para observar", "Dos preguntas: «¿Cuántas sillas hay en el escenario?» y «¿Qué problema tiene el personaje principal?». ¿Cuál ayuda más a entender la obra?", ["Pienso para qué sirve cada pregunta.", "Contar sillas no explica la historia.", "El problema del personaje mueve la historia."], "«¿Qué problema tiene el personaje principal?»."),
    ],
    [("Creer que el buen público debe quedarse inmóvil y callado todo el rato.", "Se confunde cuidar la función con no sentir nada.", "Reír, mirar con atención y aplaudir también cuidan la función."), ("Decir que una obra fue buena solo porque tenía un decorado bonito.", "El decorado ayuda, pero no es la obra completa.", "Fíjate también en personajes, voz, gestos y problema de la historia.")],
    [
        E("Afiche: «El zorro y la luna. Sala Norte. Domingo, 11:30». ¿A qué hora empieza la función?", "A las 11:30", "La hora está escrita en el afiche."),
        E("¿Quiénes son el público: las personas que actúan o las personas que miran y escuchan?", "Las personas que miran y escuchan", "El público es quien ve la función."),
        E("Antes de la función apagas el celular. ¿Ese acuerdo ayuda o molesta a los demás?", "Ayuda", "Sin luz ni ruido, todos se concentran."),
    ],
    [
        E("¿Por qué reír cuando algo es gracioso no rompe un acuerdo de público?", "Porque es parte de disfrutar y no impide oír", "Una risa breve no molesta la función."),
        E("Elige la mejor pregunta para observar: a) ¿Cuánto costó la entrada? b) ¿Cómo muestra el personaje que está nervioso?", "b", "La b te hace mirar su voz y su cuerpo."),
        E("La obra «El zorro y la luna» se presenta una vez el viernes y una vez el sábado. ¿Cuántas funciones hay en total?", "Dos", "Cada vez que se presenta es una función."),
    ],
    [
        arith("La función dura 45 minutos y el intermedio, 10 minutos. ¿Cuántos minutos son en total?", "45+10", "Se suman los dos tiempos.", " minutos"),
        arith("En el Teatro del Cerro cada entrada cuesta $2.000. Van tres personas. ¿Cuánto pagan en total?", "2000+2000+2000", "Se suma el precio de cada entrada.", " pesos"),
        E("Ordena los pasos: a) aplaudir al final, b) leer el afiche, c) apagar el celular y mirar la función. Escribe las letras en orden.", "b, c, a", "Primero te informas, luego miras y al final aplaudes."),
    ],
    [
        E("Ema dice: «Voy a mirar solo el decorado». Leo dice: «Voy a observar el problema del personaje y cómo lo muestra». ¿Quién se prepara mejor para entender la obra?", "Leo", "Su pregunta busca el conflicto y los gestos, no solo el decorado."),
        E("Un niño se ríe cuando el personaje se tropieza y toda la sala ríe también. ¿Rompió un acuerdo de público?", "No", "Reír con gracia y sin gritar es parte de disfrutar."),
    ],
    [
        E("Dos amigos se paran y tapan la vista de quienes están atrás. ¿Qué acuerdo ayuda a que todos vean: a) quedarse sentados b) pararse para ver mejor?", "a", "Si todos se sientan, todos ven el escenario."),
        E("Un niño pequeño pregunta en voz alta qué está pasando. ¿Cuál acuerdo cuida a todos: a) hablar durante toda la obra b) susurrar solo si necesita ayuda y comentar en el intermedio?", "b", "Atiende al niño sin impedir que los demás oigan."),
    ],
    [E("Tu curso verá «El zorro y la luna». Una compañera propone observar «cuánto mide el escenario». Otra propone observar «cómo muestra el zorro su miedo». ¿Cuál propuesta ayuda más a entender la historia?", "La segunda", "El miedo del zorro es parte del problema de la obra.")],
    [
        E("¿Dónde leo a qué hora empieza una función?", "En el afiche", "El afiche trae título, lugar, día y hora."),
        E("¿Un acuerdo de público cuida a todos o solo a quien lo propone?", "A todos", "Se acuerda para que todos disfruten."),
        E("¿Sirve llevar una pregunta para observar la obra?", "Sí", "Orienta la mirada hacia lo importante de la escena."),
    ],
    ("Prepara tu visita al teatro. Lee este afiche: «El último globo. Sala Sur. Sábado, 16:00. Duración: 40 minutos». Escribe o cuenta: 1) a qué hora termina la función, 2) tres acuerdos de público, 3) una pregunta para observar, que puedes escoger de esta lista: «¿Qué problema tiene el personaje?», «¿Cómo muestra su emoción con el cuerpo?», «¿Qué hace cuando está solo?». Si no puedes asistir a una función, aplica tu pregunta a una escena que te cuente una persona de tu casa.",
     "1) Termina a las 16:40. 2) Llegar antes, apagar el celular, reír y aplaudir sin molestar. 3) Pregunta: ¿Cómo muestra su emoción con el cuerpo?",
     ["calcula bien la hora de término", "escribe tres acuerdos que cuidan la función", "elige una pregunta para observar"], ["hoja con respuestas o explicación oral a una persona de tu casa"], ["acuerdos que prohíben reír o moverse del todo", "contar mal los minutos"],
     "Si un acuerdo te deja sin disfrutar, pregunta si ayuda a todos y cámbialo por otro."),
    "Lee otro afiche que te escriba una persona de tu casa y di título, lugar, día y hora.",
    "Escribe tu propio afiche para una obra imaginaria con título, lugar, día, hora y duración.",
)

# ================================================================ OA 25 · clase 2
reg(
    OA25, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que lea las escenas con distintas voces.",
    "Aprenderé a observar cómo el cuerpo, la voz y el espacio muestran lo que siente y quiere un personaje. Sirve para entender mejor una obra y para actuar con más claridad.",
    ["Sé qué es un personaje.", "Sé que una obra se cuenta con voz y cuerpo."],
    [
        "En el teatro las palabras no son lo único que importa. La voz cambia en volumen (fuerte o bajito), en ritmo (rápido o lento) y en tono (alegre, serio, asustado). El cuerpo habla con la postura, la mirada y los gestos. El espacio es el lugar del escenario donde se mueve cada personaje.",
        "Una pista sola no siempre alcanza. Si un personaje habla bajito, puede estar triste, pero también puede estar contando un secreto. Por eso juntamos varias pistas: cómo habla, qué hace con el cuerpo y dónde está. Cuando las pistas coinciden, podemos explicar con más seguridad lo que sucede.",
        "Para observar bien usamos una frase en dos partes: nombramos la pista y decimos qué muestra. Por ejemplo: «Habló bajito y miró al suelo, por eso parecía tímido». Así explicamos cómo se cuenta la escena, no solo qué ocurre.",
    ],
    [("volumen", "qué tan fuerte o bajito suena la voz"), ("tono", "manera de decir algo: alegre, serio, asustado"), ("postura", "forma de colocar el cuerpo"), ("mirada", "hacia dónde y cómo mira el personaje"), ("desplazamiento", "movimiento del personaje por el escenario")],
    [
        ("Juntar pistas", "Escena: Mateo entra a pasos rápidos, habla fuerte y agita los brazos: «¡Se nos acaba el tiempo!». ¿Qué siente o quiere Mateo?", ["Voz: fuerte.", "Cuerpo: pasos rápidos y brazos agitados.", "Las tres pistas muestran prisa."], "Tiene prisa y quiere apurar a los demás."),
        ("Una pista no basta", "Escena: Ana y Bruno se sientan en lados opuestos del escenario y no se miran. ¿Qué pista de espacio hay y qué dudas deja?", ["El espacio los separa: están lejos.", "Pueden estar enojados o ser tímidos.", "Necesito otra pista, como la voz o lo que dicen."], "Están lejos uno del otro; hace falta otra pista para saber por qué."),
    ],
    [("Decir «estaba triste» sin dar ninguna pista.", "No se sabe de dónde sale la idea.", "Di la pista: «Habló bajito y miró al suelo, por eso parecía triste»."), ("Fijarse solo en las palabras que dice el personaje.", "La voz, el cuerpo y el espacio también cuentan la historia.", "Mira cómo lo dice y qué hace mientras lo dice.")],
    [
        E("Un personaje habla muy fuerte y rápido. ¿Parece apurado o tranquilo?", "Apurado", "Voz fuerte y rápida suele mostrar prisa."),
        E("Un personaje baja la cabeza y cruza los brazos. ¿Eso es voz, gesto o espacio?", "Gesto", "Es un movimiento del cuerpo."),
        E("Dos personajes que estaban lejos ahora están uno junto al otro. ¿Qué cambió: el espacio o el volumen?", "El espacio", "Cambió dónde están en el escenario."),
    ],
    [
        E("¿Qué significa «tono» de la voz?", "La manera de decir algo, como alegre o serio", "El tono muestra la emoción al hablar."),
        E("¿Por qué conviene juntar varias pistas y no usar una sola?", "Porque una pista sola puede tener más de un significado", "Varias pistas que coinciden dan más seguridad."),
        E("Elige la pista de postura: a) «habla lento» b) «se encorva y se mira los pies» c) «se aleja hacia la puerta».", "b", "La postura es cómo coloca el cuerpo."),
    ],
    [
        E("Escena: «Lola entra corriendo y grita: ¡Perdí mi gorro!». Nombra una pista de voz y una de cuerpo.", "Voz: grita; cuerpo: entra corriendo", "Ambas están escritas en la escena."),
        E("Escena: «Tomás se acerca a Lola, se agacha y le dice con voz suave: Te ayudo a buscar». ¿Qué muestra el desplazamiento de Tomás?", "Que quiere acompañarla y ayudarla", "Se acerca y se agacha a su lado."),
        E("Escena: «Sofía habla bajito, lento, y abraza su mochila». ¿Qué emoción muestran juntas las pistas: a) alegría b) tristeza o cansancio?", "b", "Voz baja, ritmo lento y abrazo coinciden."),
    ],
    [
        E("Ana dice: «El dragón estaba triste». Luis dice: «El dragón caminaba lento y miraba al suelo, por eso parecía triste». ¿Quién explicó con pistas?", "Luis", "Luis nombra lo que hizo el dragón."),
        E("Un actor dice «estoy feliz» con voz muy baja y cara seria. ¿Las pistas coinciden con sus palabras?", "No", "Feliz suele verse con voz y cara alegres."),
    ],
    [
        E("Escena: «A se aleja de B hacia el fondo. B queda de pie, quieto, con los brazos caídos». ¿Cuál es la pista de espacio y cuál la de cuerpo?", "Espacio: A se aleja; cuerpo: B con los brazos caídos", "El espacio es el movimiento por el escenario; el cuerpo, la postura."),
        E("Elige la mejor frase para explicar una escena: a) «Pasó algo triste.» b) «Habló bajito y se sentó lejos, por eso parecía triste.»", "b", "La b nombra pistas concretas."),
    ],
    [E("Escena: «Pedro entra gritando: ¡Llegué tarde! Se agarra la cabeza y corre hasta el centro. Mira a María, que está sentada, y dice bajito: Perdón». ¿Cómo cambia la voz de Pedro?", "Pasa de gritar a hablar bajito", "Primero grita y luego dice bajito el perdón.")],
    [
        E("¿Un gesto es un movimiento del cuerpo?", "Sí", "Se hace con la cara, las manos o el cuerpo."),
        E("¿Solo importan las palabras en el teatro?", "No", "También cuentan la voz, el cuerpo y el espacio."),
        E("Si digo cómo se siente un personaje, ¿debo dar una pista?", "Sí", "La pista explica de dónde saqué la idea."),
    ],
    ("Observa y explica una escena. Lee esta escena en voz alta o pide que te la lean: «Sofía entra caminando lento. Se sienta en una silla, abraza su mochila y dice bajito: Hoy no quiero jugar. Diego se acerca, se agacha a su lado y le dice con voz suave: Si quieres, nos sentamos juntos». Escribe qué crees que siente cada personaje y una pista de voz, de cuerpo o de espacio que lo muestra.",
     "Sofía parece triste: camina lento, abraza su mochila y habla bajito. Diego quiere acompañarla: se acerca, se agacha y habla suave.",
     ["dice qué siente cada personaje", "da una pista por personaje", "explica con «porque» o «por eso»"], ["respuesta escrita u oral con pistas"], ["resumir sin dar pistas", "inventar datos que la escena no dice"],
     "Si solo resume, pregunta: ¿cómo hablaba Sofía? ¿Qué hizo Diego con su cuerpo?"),
    "Pide a alguien de tu casa que diga «hola» de tres maneras y explica qué sientes en cada una.",
    "Cambia la voz y el espacio de la escena de Sofía para que parezca alegre y explica qué cambiaste.",
)

# ================================================================ OA 25 · clase 3
reg(
    OA25, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: cinco papelitos para ordenar las acciones.",
    "Aprenderé a reconstruir una escena: decir quiénes son los personajes, cuál es el conflicto y qué acciones ocurren en orden. Sirve para recordar una obra y contarla sin perder lo importante.",
    ["Sé reconocer personajes y sus acciones.", "Sé usar primero, luego y al final."],
    [
        "Una escena es una parte de una obra donde los personajes hacen cosas y se dicen cosas. Lo que hacen son las acciones. Lo que se dicen es el diálogo. Para reconstruir una escena, ordenamos las acciones con palabras como primero, luego, después y al final.",
        "En casi toda escena hay un conflicto, que es el problema que los personajes quieren resolver. Por ejemplo: dos amigos quieren usar a la vez el único balón. El conflicto mueve la historia. Puede resolverse con un acuerdo, con una ayuda, o puede quedar abierto. La forma en que termina el conflicto se llama desenlace.",
        "Para contar una escena, nombramos a los personajes, decimos el conflicto y relatamos las acciones importantes en orden. No hace falta repetir todo el diálogo. Es mejor decir quién quería qué, qué problema apareció y cómo terminó.",
    ],
    [("escena", "parte de una obra donde pasa algo"), ("acción", "lo que hace un personaje"), ("diálogo", "lo que dicen los personajes"), ("conflicto", "problema que los personajes deben resolver"), ("desenlace", "cómo termina el conflicto")],
    [
        ("Encontrar el conflicto", "Escena «El único balón»: Julia y Max quieren jugar con el único balón del patio. Julia lo toma. Max lo tira de un lado. Después proponen turnos de cinco minutos y juegan. ¿Cuál es el conflicto?", ["Busco qué quieren los personajes.", "Ambos quieren el único balón.", "Ese problema es el conflicto."], "Los dos quieren usar el único balón a la vez."),
        ("Ordenar acciones", "En «El único balón», ordena: a) acuerdan turnos, b) Julia toma el balón, c) juegan. ¿Cuál es el orden?", ["Primero Julia toma el balón.", "Luego acuerdan turnos.", "Al final juegan."], "b, a, c."),
    ],
    [("Contar la escena repitiendo cada palabra del diálogo.", "Se pierde lo importante.", "Resume: personajes, conflicto, acciones y final."), ("Decir que el conflicto es un personaje o un lugar.", "El conflicto es un problema, no un objeto.", "Pregunta: ¿qué problema deben resolver?")],
    [
        E("¿Qué son las acciones de una escena?", "Lo que hacen los personajes", "Acción viene de actuar o hacer."),
        E("¿Qué es el diálogo?", "Lo que dicen los personajes", "Es la conversación entre ellos."),
        E("Escena: «Dos niños quieren el mismo columpio». ¿Cuál es el conflicto?", "Los dos quieren el mismo columpio", "Es el problema que deben resolver."),
    ],
    [
        E("¿Por qué el conflicto es importante en una escena?", "Porque mueve la historia", "Sin problema, los personajes no tendrían qué resolver."),
        E("Ordena con primero, luego y al final: a) Rita pide ayuda, b) Rita tropieza con una caja, c) Tomás la ayuda a levantarse.", "b, a, c", "El tropiezo ocurre antes de pedir ayuda."),
        E("Elige el desenlace de «El único balón» según la escena de arriba: a) pelean y no juegan b) acuerdan turnos y juegan.", "b", "Así termina la escena escrita."),
    ],
    [
        E("Escena: «Leo no encuentra su lápiz. Pregunta a Marta, que lo vio en el suelo. Leo lo recoge y agradece». ¿Cuál es el conflicto?", "Leo no encuentra su lápiz", "Es el problema con el que empieza la escena."),
        E("En esa escena, ¿qué acción resuelve el problema: a) Marta le avisa dónde está b) Leo agradece?", "a", "Marta le dice dónde está el lápiz."),
        E("Escena: «Una abuela quiere cruzar la calle y el semáforo está en rojo. Un niño la acompaña y esperan juntos». Escribe quién es cada personaje y el conflicto.", "Personajes: la abuela y el niño; conflicto: ella quiere cruzar y el semáforo está en rojo", "Se leen en la escena."),
    ],
    [
        E("Ana cuenta: «Hay un niño, una niña, un balón, conflicto y final». Bea cuenta: «Julia y Max querían el único balón, pelearon y luego acordaron turnos». ¿Quién reconstruyó mejor la escena?", "Bea", "Cuenta quién quería qué, el problema y cómo terminó."),
        E("Escena: «Nina y Dani hacen un cartel. Nina quiere pintarlo de azul y Dani de rojo. Deciden pintar el fondo azul y las letras rojas». ¿El conflicto se resolvió?", "Sí", "Llegaron a un acuerdo que usa los dos colores."),
    ],
    [
        E("Escena: «Una niña quiere regar la planta. Otro niño ya la regó. Ella se enoja, él le explica y deciden mirar si la tierra está húmeda». ¿Qué acción de la escena evita regarla otra vez?", "Mirar si la tierra está húmeda", "Comprueban antes de volver a regar."),
        E("Ordena el final: a) la niña se enoja b) él le explica c) revisan la tierra. ¿Qué letra va primera?", "a", "La escena parte con su enojo."),
    ],
    [E("Escena: «Mia y Sol quieren sentarse junto a la ventana en el bus. Mia llegó primero, pero Sol tenía mareo. Mia le ofrece el asiento». ¿Cuál es el conflicto y cómo se resuelve? Escribe en una frase cada cosa.", "Conflicto: las dos quieren el asiento junto a la ventana; se resuelve cuando Mia se lo ofrece a Sol", "Ambos datos están en la escena.")],
    [
        E("¿El conflicto es un problema?", "Sí", "Es lo que los personajes deben resolver."),
        E("¿Puedo contar una escena sin repetir todo el diálogo?", "Sí", "Basta con decir lo importante."),
        E("¿El desenlace es cómo termina el conflicto?", "Sí", "Cierra la escena."),
    ],
    ("Reconstruye una escena. Lee: «Camila y Joaquín deben entregar un trabajo en pareja. Camila quiere escribir primero y Joaquín quiere dibujar primero. Se enojan y se quedan callados. Después Camila propone que cada uno haga la parte que más le guste y que se revisen entre los dos. Joaquín acepta y terminan juntos». Escribe o cuenta: personajes, conflicto, tres acciones en orden y cómo terminó.",
     "Personajes: Camila y Joaquín. Conflicto: cada uno quiere empezar con algo distinto. Primero se enojan; luego Camila propone repartirse y revisar; al final Joaquín acepta y terminan.",
     ["nombra personajes", "dice el conflicto con claridad", "ordena tres acciones y dice el final"], ["relato escrito u oral de la escena"], ["contar sin conflicto", "desordenar las acciones"],
     "Si falta el conflicto, pregunta qué quería cada uno."),
    "Cuenta a una persona de tu casa una escena de un cuento que conozcas, con personajes, conflicto y final.",
    "Cambia el final de la escena de Camila y Joaquín y explica si el conflicto se resuelve o queda abierto.",
)

# ================================================================ OA 25 · clase 4
reg(
    OA25, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los diálogos.",
    "Aprenderé a mirar una escena desde otro rol: el de otro personaje o el de quien trabaja en una obra. Sirve para entender qué quiere cada uno y para ampliar mi forma de expresarme.",
    ["Sé reconocer personajes y conflicto.", "Sé que el cuerpo y la voz muestran emociones."],
    [
        "Una misma escena se ve distinta según quién la mira. Si cambiamos de rol, cambia lo que vemos. El rol de un personaje es lo que ese personaje quiere y siente. Preguntarnos «¿qué quiere este personaje y qué siente?» nos ayuda a comprender también a quienes piensan distinto de nosotros.",
        "En una obra también hay roles de trabajo. El actor o la actriz interpreta a un personaje. El director o la directora guía los ensayos y decide cómo se mueven los actores. El dramaturgo o la dramaturga escribe el texto de la obra. El público mira y escucha.",
        "Para explorar una escena desde otro rol, usamos esta frase: «Si yo fuera el personaje, querría… porque…». No cambiamos los hechos de la escena: solo miramos lo mismo desde otro lugar y buscamos pistas del texto que justifiquen lo que decimos.",
    ],
    [("rol", "papel que tiene alguien en una escena o en una obra"), ("actor o actriz", "persona que interpreta a un personaje"), ("director o directora", "persona que guía los ensayos de la obra"), ("dramaturgo o dramaturga", "persona que escribe el texto de la obra"), ("punto de vista", "lugar desde donde alguien mira la situación")],
    [
        ("Cambiar de personaje", "Escena: «Tomás se sienta solo en el recreo. Lucía lo ve, se acerca y le dice: ¿Quieres jugar con nosotras?». Desde el rol de Tomás, ¿qué podría sentir cuando Lucía se acerca?", ["Tomás estaba solo.", "Alguien lo invita.", "Puede sentir alivio o alegría, y la pista es que lo invitan."], "Podría sentir alivio o alegría porque lo invitaron."),
        ("Reconocer un rol de trabajo", "En el ensayo, alguien dice a los actores: «Entra por la derecha y habla más fuerte». ¿Qué rol tiene?", ["Da indicaciones sobre cómo moverse.", "No interpreta un personaje.", "Guía el ensayo."], "Director o directora."),
    ],
    [("Cambiar los hechos de la escena al cambiar de rol.", "Al cambiar de rol cambia la mirada, no lo que ocurrió.", "Mantén los hechos y cambia solo lo que el personaje siente o quiere."), ("Pensar que el actor es el mismo que el personaje.", "El actor interpreta a un personaje, pero es otra persona.", "Di: el actor interpreta, el personaje vive la historia.")],
    [
        E("Quien interpreta a un personaje en la obra es: a) el actor o la actriz b) el director o la directora.", "a", "Interpretar es parte del trabajo de actuar."),
        E("Quien escribe el texto de la obra es: a) el dramaturgo o la dramaturga b) el público.", "a", "Dramaturgo viene de escribir obras."),
        E("Escena: «Un niño pierde su gorro». Desde su rol, ¿qué podría sentir: preocupación o aburrimiento?", "Preocupación", "Perder algo suele preocupar."),
    ],
    [
        E("¿Por qué sirve mirar una escena desde otro personaje?", "Para entender qué quiere y siente ese personaje", "Así comprendemos otras formas de ver lo que pasa."),
        E("¿Cambiar de rol cambia los hechos de la escena?", "No", "Solo cambia desde dónde miramos."),
        E("¿Quién guía los ensayos: el director o el público?", "El director", "El público solo mira la función."),
    ],
    [
        E("Escena: «Rosa dice: ¡Se acabaron las galletas! Y Paz responde: Yo me comí la última». Desde el rol de Rosa, ¿qué podría sentir: sorpresa o calma total?", "Sorpresa", "Se enteró de que ya no hay galletas."),
        E("Completa con una pista: «Si yo fuera Tomás, querría jugar porque…». Escribe la razón que da la escena de arriba.", "Porque estaba solo", "En la escena, Tomás estaba solo en el recreo."),
        E("Un actor dice: «Mi personaje es muy valiente». ¿Quién es valiente: el actor o el personaje?", "El personaje", "Es una cualidad del papel que interpreta."),
    ],
    [
        E("Escena: «Un abuelo cuenta un cuento y su nieta lo interrumpe tres veces. El abuelo respira y dice: Esperemos a que termine esta parte». Desde el rol del abuelo, ¿qué quiere: a) terminar el cuento b) que se vaya?", "a", "Pide esperar para terminar el relato."),
        E("Ana cuenta la escena desde el rol de Lucía y escribe: «Tomás no estaba solo en el recreo». En la escena original Tomás estaba solo. ¿Respetó los hechos?", "No", "Al cambiar de rol no se cambian los hechos."),
    ],
    [
        E("En la escena de Tomás y Lucía, escribe una pista de que Lucía quiere incluir a Tomás.", "Le dice: ¿Quieres jugar con nosotras?", "La pregunta es una invitación."),
        E("Un grupo prepara una escena. Camilo cambia el texto escrito de la obra. ¿Qué rol hace: dramaturgo o público?", "Dramaturgo", "Escribe o modifica el texto."),
    ],
    [E("Escena: «Ema y su hermano mayor esperan el bus. Ema quiere hablar, pero su hermano mira el celular. Ella se calla y se queda mirando la calle». Desde el rol de Ema, ¿qué podría sentir: a) ganas de conversar b) mucha alegría por el silencio? Elige la que tiene una pista en la escena.", "a", "La escena dice que quería hablar.")],
    [
        E("¿Un actor es lo mismo que su personaje?", "No", "El actor interpreta; el personaje es parte de la historia."),
        E("¿Puedo cambiar los hechos al mirar desde otro rol?", "No", "Solo cambia la mirada."),
        E("¿Sirve preguntar «qué quiere este personaje»?", "Sí", "Ayuda a comprender sus acciones."),
    ],
    ("Explora una escena desde otro rol. Lee: «Mateo se cae en el patio y se hace un raspón en la rodilla. Ana, que estaba jugando a la cuerda, deja de jugar y le pregunta si puede ayudarlo. Mateo, avergonzado, dice que está bien. Ana se queda a su lado un momento más». Escribe o cuenta: 1) qué quiere y siente Ana, 2) qué quiere y siente Mateo, usando la frase «Si yo fuera…, querría… porque…» y una pista de la escena.",
     "Si yo fuera Ana, querría ayudar porque dejó de jugar para preguntarle. Si yo fuera Mateo, querría que no me vean porque se avergonzó y dijo que estaba bien.",
     ["usa la frase con «porque»", "da una pista de la escena para cada personaje", "no cambia los hechos"], ["texto breve u explicación oral"], ["inventar hechos nuevos", "no explicar con pistas"],
     "Si no hay pista, pregunta: ¿qué dijo o hizo para que pienses eso?"),
    "Cuenta a alguien de tu casa un recreo desde el punto de vista de otra persona que estuvo ahí.",
    "Escribe la misma escena desde el rol de un compañero que la mira desde lejos y explica qué siente.",
)

# ================================================================ OA 25 · clase 5
reg(
    OA25, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: dos personas de tu casa para leer los diálogos en voz alta.",
    "Aprenderé a crear una respuesta teatral breve: una escena corta con personajes, conflicto, diálogo y acotaciones. Sirve para expresar lo que sentí o pensé de una obra y para desarrollar mi creatividad.",
    ["Sé reconocer personajes y conflicto.", "Sé observar voz, cuerpo y espacio."],
    [
        "Después de ver o escuchar una obra, podemos responder creando una escena nuestra. Una respuesta teatral breve puede continuar la historia, mostrar un final distinto o contar lo que pensó otro personaje. Para que funcione, necesita personajes, un conflicto y un final posible.",
        "En un texto teatral, el nombre del personaje se escribe antes de lo que dice. Entre paréntesis van las acotaciones, que indican cómo se dice o se hace algo. Por ejemplo: LUCÍA (suave, agachándose): ¿Te ayudo? La acotación no se dice en voz alta: guía a quien actúa.",
        "Una buena respuesta es breve y clara: de cuatro a seis intervenciones. Mostramos lo que sienten los personajes con lo que dicen y con las acotaciones, sin explicarlo todo. Al terminar, revisamos si el conflicto se entiende y si el final es posible.",
    ],
    [("acotación", "indicación entre paréntesis sobre cómo decir o hacer algo"), ("intervención", "lo que dice un personaje cada vez que habla"), ("continuar", "seguir una historia después de su final"), ("final alternativo", "otra forma posible de terminar una historia"), ("creatividad", "capacidad de inventar algo nuevo")],
    [
        ("Reconocer la acotación", "Texto: «NICO (mirando al suelo): No quise romper tu dibujo». ¿Qué es lo que va entre paréntesis y para qué sirve?", ["Está entre paréntesis.", "Dice cómo está Nico al hablar.", "Guía al actor y no se dice en voz alta."], "Es la acotación; indica cómo habla o qué hace Nico."),
        ("Completar una intervención", "Escena: Nico rompió sin querer el dibujo de Pía. Escribe una intervención de Pía que muestre que se siente triste pero escucha.", ["Pienso qué siente Pía.", "Agrego una acotación.", "Escribo una frase con ese ánimo."], "PÍA (bajito): Me dolió, pero quiero escucharte."),
    ],
    [("Escribir las acotaciones como si fueran parte del diálogo que se dice.", "Las acotaciones son indicaciones, no palabras del personaje.", "Ponlas entre paréntesis y no las leas en voz alta."), ("Crear una escena sin conflicto, solo con saludos.", "Sin problema, no hay historia que avanzar.", "Agrega algo que los personajes quieran y que les cueste lograr.")],
    [
        E("En un texto teatral, ¿el nombre del personaje se escribe antes o después de lo que dice?", "Antes", "Así se sabe quién habla."),
        E("¿Qué indica una acotación: cómo decir o hacer algo, o el título de la obra?", "Cómo decir o hacer algo", "Guía a quien actúa."),
        E("¿Una acotación se dice en voz alta?", "No", "Solo orienta a quien actúa."),
    ],
    [
        E("¿Para qué sirve crear un final alternativo?", "Para imaginar otra manera de terminar la historia", "Muestra creatividad y comprensión del conflicto."),
        E("Texto: «ANA (sonriendo y aplaudiendo): ¡Ganaste!». ¿Qué emoción indica la acotación?", "Alegría", "Sonreír y aplaudir muestran alegría."),
        E("¿Cuántas intervenciones tiene este texto? «LEO: Hola. MIA: Hola. LEO: ¿Jugamos? MIA: Sí.»", "Cuatro", "Cada vez que habla un personaje cuenta una."),
    ],
    [
        E("Ordena para escribir una respuesta teatral: a) revisar el final b) pensar personajes y conflicto c) escribir las intervenciones. Escribe las letras.", "b, c, a", "Se planifica, se escribe y se revisa."),
        E("Agrega una acotación a esta frase para que se note que Rosa tiene miedo: «ROSA: ¿Quién está ahí?».", "ROSA (temblando): ¿Quién está ahí?", "Temblar es un gesto de miedo."),
        E("Escribe quién habla en: «TOMÁS (sonriendo): Gracias por esperarme».", "Tomás", "Su nombre va antes de los dos puntos."),
    ],
    [
        E("Ema escribe una escena que solo dice: «Hola», «Hola», «Chao», «Chao». Ana escribe una donde dos niños discuten por un turno y lo resuelven. ¿Cuál tiene conflicto?", "La de Ana", "Hay un problema que resolver."),
        E("En una escena, PÍA (llorando): Estoy bien. ¿Las palabras y la acotación coinciden?", "No", "Dice que está bien, pero llora."),
    ],
    [
        E("Final de «El único balón»: Julia y Max juegan juntos en un solo equipo con el mismo balón. ¿Es un final alternativo posible del conflicto, sí o no?", "Sí", "Resuelve el problema de otra manera que puede ocurrir."),
        E("¿Cuál final es posible para «dos niños quieren el mismo columpio»: a) uno se turna con el otro b) el columpio se convierte en nave espacial real?", "a", "Es un final que pasa en la vida real."),
    ],
    [E("Una obra termina cuando Lola devuelve un libro a la biblioteca con retraso. ¿Cuál continuación sería la mejor respuesta teatral: a) Lola habla con la bibliotecaria y acuerdan una forma de devolver a tiempo la próxima vez; b) aparece un dragón y nadie habla?", "a", "Resuelve el problema con diálogo posible.")],
    [
        E("¿Una respuesta teatral necesita conflicto?", "Sí", "Sin problema, no hay historia."),
        E("¿Las acotaciones van entre paréntesis?", "Sí", "Así se distinguen del diálogo."),
        E("¿Mi final puede ser distinto del de la obra original?", "Sí", "Un final alternativo es una respuesta creativa."),
    ],
    ("Crea tu respuesta teatral. Lee la situación: «Un niño llamado Beto devuelve a una compañera, Gaby, el cuaderno que le prestó. El cuaderno tiene una hoja arrugada». Escribe una escena de cuatro a seis intervenciones con nombres de personajes, un conflicto y al menos dos acotaciones. Termina con un final posible. Puedes leerla en voz alta con una persona de tu casa.",
     "BETO (nervioso): Gaby, tu cuaderno tiene una hoja arrugada. GABY (mirando la hoja): Me da pena, pero lo importante es que me lo devolviste. BETO (aliviado): Puedo alisarla con cuidado. GABY (sonriendo): Gracias por avisarme.",
     ["tiene de cuatro a seis intervenciones", "muestra un conflicto", "usa al menos dos acotaciones", "termina con un final posible"], ["escena escrita o leída en voz alta"], ["escena sin conflicto", "acotaciones mezcladas con el diálogo"],
     "Si falta el conflicto, pregunta qué problema tienen Beto y Gaby."),
    "Reescribe una de las escenas de esta unidad con un final distinto de una línea.",
    "Crea una escena de seis intervenciones sobre cómo compartir un material del curso.",
)

# ================================================================ OA 26 · clase 1
reg(
    OA26, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar el texto.",
    "Aprenderé a preparar una idea u opinión con una razón antes de participar en una conversación de grupo. Sirve para que los demás entiendan lo que pienso y para que la conversación avance.",
    ["Sé decir lo que pienso.", "Sé esperar mi turno para hablar."],
    [
        "Una conversación de grupo funciona mejor cuando cada persona trae una idea preparada. Una idea es lo que pienso sobre un tema. Una opinión es lo que pienso o siento, y puede ser distinta de la de otra persona. Para que los demás me entiendan, la acompaño con una razón o un dato del texto que escuchamos.",
        "Una forma sencilla de preparar la idea es: «Pienso que…, porque…». Por ejemplo: «Pienso que el niño hizo bien en ayudar, porque el texto dice que la señora llevaba mucho peso». La razón muestra que escuché o leí con atención y permite que otros contesten.",
        "Antes de hablar conviene pensar en tres cosas: qué quiero decir, qué razón tengo y si mi idea se relaciona con el tema. Una idea sin razón, como «porque sí» o «me gusta», es difícil de conversar. Si el texto no dice algo, puedo decir «yo creo» para mostrar que es mi opinión.",
    ],
    [("idea", "lo que pienso sobre un tema"), ("opinión", "lo que pienso o siento y puede ser distinto de lo que piensan otros"), ("razón", "motivo que explica por qué pienso algo"), ("tema", "asunto del que se conversa"), ("turno", "momento en que me toca hablar")],
    [
        ("Armar una idea con razón", "Texto: «Dani vio que a su compañera se le cayeron los lápices. Los recogió y se los entregó sin decir nada». Prepara una idea: ¿fue amable? Usa «Pienso que…, porque…».", ["Decido qué pienso: sí fue amable.", "Busco el dato: recogió los lápices.", "Armo la frase con «porque»."], "Pienso que Dani fue amable, porque recogió los lápices y se los entregó."),
        ("Distinguir idea con y sin razón", "Dos intervenciones sobre el mismo texto: A) «Dani es bueno.» B) «Dani es bueno, porque ayudó sin que se lo pidieran.» ¿Cuál tiene razón?", ["Busco la palabra «porque».", "B explica el motivo.", "A solo afirma."], "La B."),
    ],
    [("Decir una opinión sin ninguna razón: «Me gusta porque sí».", "Los demás no saben qué te hizo pensar eso.", "Agrega un dato del texto: «Porque el texto dice que…»."), ("Hablar de algo que no tiene relación con el texto.", "La conversación se aleja del tema.", "Revisa antes si tu idea responde a lo que se conversa.")],
    [
        E("Completa: «Pienso que el niño fue amable, ___ recogió los lápices». ¿Qué palabra falta: porque o aunque?", "Porque", "Introduce la razón."),
        E("¿Una opinión es lo que yo pienso o lo que dice el diccionario?", "Lo que yo pienso", "Puede ser distinta de la de otra persona."),
        E("¿Cuál tiene razón: «Es lindo.» o «Es lindo porque tiene muchos colores.»?", "La segunda", "Explica el motivo con un dato."),
    ],
    [
        E("En Lenguaje: ¿Para qué sirve dar una razón?", "Para que los demás entiendan por qué pienso así", "La razón sostiene la idea."),
        E("Texto: «Una niña regó el huerto aunque llovía». Idea: «Se preocupó por el huerto». ¿Cuál puede ser su razón: a) regó aunque llovía b) le gusta el helado?", "a", "Es un dato del texto relacionado con la idea."),
        E("Si el texto no dice algo y yo lo pienso, ¿qué puedo decir al comenzar: «yo creo» o «el texto dice»?", "Yo creo", "Marca que es mi opinión."),
    ],
    [
        E("Texto: «Pablo guardó su merienda y la compartió con un compañero que había olvidado la suya». Arma una idea con «porque»: ¿fue generoso?", "Pienso que Pablo fue generoso, porque compartió su merienda", "Idea más dato del texto."),
        E("Ordena para preparar una idea: a) pensar la razón b) escuchar el texto c) decir mi idea con «porque». Escribe las letras.", "b, a, c", "Primero escucho, luego pienso, al final hablo."),
        E("Una compañera opina: «El texto es entretenido». ¿Cuál puede ser su razón: a) porque pasan cosas inesperadas b) porque hoy es lunes?", "a", "La razón debe relacionarse con el texto."),
    ],
    [
        E("Sara dice: «Me gustó el cuento, porque sí». Teo dice: «Me gustó el cuento, porque la niña no se rindió». ¿Quién ayuda más a conversar?", "Teo", "Su razón da algo de qué hablar."),
        E("Texto: «Dani recogió los lápices de su compañera y se los entregó». Rita dice: «Dani fue amable, porque recogió los lápices». Teo dice: «Dani fue amable, porque tiene el pelo corto». ¿Qué razón sale del texto: la de Rita o la de Teo?", "La de Rita", "La de Teo no se relaciona con lo que hizo Dani."),
    ],
    [
        E("Texto: «Luis llegó tarde porque ayudó a un vecino que cargaba bolsas». Dos opiniones: a) «Luis hizo mal, porque llegó tarde.» b) «Luis hizo bien, porque ayudó a alguien que lo necesitaba.» ¿Ambas tienen razón del texto?", "Sí", "Cada una usa un dato distinto del texto."),
        E("Sobre Luis, ¿cuál tiene idea y razón: a) «Luis es puntual.» b) «Pienso que Luis fue solidario, porque ayudó a un vecino.»", "b", "La b une una idea con un motivo del texto."),
    ],
    [E("Tu grupo conversa sobre el texto de Dani. Ana dice: «Dani no habla mucho». Bea dice: «Dani fue amable, porque recogió los lápices». ¿Qué intervención se relaciona con la pregunta «¿Fue amable?»", "La de Bea", "Responde al tema y da una razón.")],
    [
        E("¿Una opinión puede ser distinta de la de otro?", "Sí", "Cada persona piensa con sus propias razones."),
        E("¿Qué palabra introduce una razón: porque o también?", "Porque", "Anuncia el motivo."),
        E("¿Mi idea debe relacionarse con el tema?", "Sí", "Así la conversación avanza."),
    ],
    ("Prepara tu idea para conversar. Lee este texto: «En el recreo, Maite vio que un compañero nuevo, Hugo, comía solo. Le dijo: Si quieres, juega con nosotros. Hugo sonrió y fue con ella». Prepara en tu hoja o cuéntale a una persona de tu casa: una idea con la forma «Pienso que…, porque…» sobre lo que hizo Maite, y una pregunta para el grupo. Puedes elegir entre «¿Qué sintió Hugo?» o «¿Qué más podría hacer Maite?».",
     "Pienso que Maite fue acogedora, porque invitó a Hugo a jugar. Pregunta: ¿Qué sintió Hugo?",
     ["dice una idea clara", "da una razón del texto", "propone una pregunta para el grupo"], ["hoja con idea y pregunta o explicación oral"], ["opinión sin razón", "razón que no sale del texto"],
     "Si falta la razón, pregunta: ¿qué dice el texto que te hizo pensar eso?"),
    "Cuenta a alguien de tu casa una opinión con «Pienso que…, porque…» sobre un cuento que conozcas.",
    "Prepara dos ideas distintas con razón sobre el texto de Maite y compáralas.",
)

# ================================================================ OA 26 · clase 2
reg(
    OA26, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar por turnos.",
    "Aprenderé a mantener el foco de una conversación de grupo: hablar del tema y respetar los turnos. Sirve para que todos entiendan de qué se habla y puedan participar.",
    ["Sé decir una idea con una razón.", "Sé esperar mi turno."],
    [
        "El foco de una conversación es el tema del que estamos hablando. Mantener el foco significa que lo que decimos se relaciona con ese tema. Si el tema es «cómo cuidar el huerto del curso», no corresponde contar lo que vimos en la tele ayer.",
        "Para mantener el foco, antes de hablar me pregunto: «¿Esto responde a lo que estamos conversando?». Si me desvío sin querer, puedo decir: «Perdón, volvamos al tema». También puedo conectar mi idea con la anterior: «Sobre lo que dijo Eli, yo agrego…».",
        "Respetar los turnos también cuida el foco. Cuando alguien habla, escucho hasta que termine. Levanto la mano o espero una pausa. Así nadie se queda sin hablar y las ideas no se mezclan. Quien guía la conversación puede ayudar diciendo quién sigue.",
    ],
    [("foco", "tema central de la conversación"), ("desvío", "decir algo que no se relaciona con el tema"), ("turno", "momento en que me toca hablar"), ("interrumpir", "hablar mientras otra persona todavía habla"), ("moderador o moderadora", "persona que ayuda a cuidar turnos y tema")],
    [
        ("Reconocer lo que mantiene el foco", "Tema: «Cómo cuidar el huerto del curso». Intervenciones: a) «Podemos regar por la mañana.» b) «Ayer vi un partido.» ¿Cuál mantiene el foco?", ["Busco la relación con el huerto.", "Regar es cuidar el huerto.", "El partido no se relaciona."], "La a."),
        ("Volver al tema", "Tema: «Cómo cuidar el huerto del curso». Alguien cuenta que su perro se escapó. ¿Qué puedes decir para volver al tema?", ["Reconozco que el comentario se desvió.", "Uso una frase amable.", "Regreso al huerto."], "«Gracias por contarlo. Volvamos al huerto: ¿quién riega los lunes?»"),
    ],
    [("Hablar de lo que te importa aunque no se relacione con el tema.", "La conversación se desordena.", "Espera otro momento o relaciónalo con el tema."), ("Interrumpir porque tienes una idea muy buena.", "La otra persona pierde su turno.", "Anota tu idea y espera tu turno.")],
    [
        E("Tema: «Cuidar la sala». ¿Qué mantiene el foco: «Podemos ordenar los materiales» o «Mi primo vive en el sur»?", "Podemos ordenar los materiales", "Ordenar es cuidar la sala."),
        E("¿Qué es el foco de una conversación?", "El tema de que se habla", "Todo lo que decimos se relaciona con él."),
        E("Alguien habla. ¿Qué hago: escucho hasta que termine o hablo al mismo tiempo?", "Escucho hasta que termine", "Así se respeta su turno."),
    ],
    [
        E("¿Por qué conviene preguntarse «¿Esto responde al tema?» antes de hablar?", "Para no desviarse", "Ayuda a mantener el foco."),
        E("¿Cuál es una forma amable de volver al tema: «Eso no importa» o «Gracias, volvamos al tema»?", "Gracias, volvamos al tema", "Es amable y devuelve la conversación al foco."),
        E("¿Qué hace la persona que modera: cuida turnos y tema o decide todas las ideas?", "Cuida turnos y tema", "No decide las ideas; ayuda a ordenar."),
    ],
    [
        E("Tema: «Reglas para el recreo». Marca la intervención que mantiene el foco: a) «Propongo no correr en la escalera.» b) «Mi cumpleaños es en abril.»", "a", "Es una regla para el recreo."),
        E("Tema: «Reciclar en el curso». Carla dice que le gusta la pizza. ¿Qué frase vuelve al tema sin ofender: a) «Eso no importa, cállate.» b) «Gracias, Carla. Volvamos a cómo reciclar en el curso.»", "b", "Reconoce el aporte y regresa al foco."),
        E("En un grupo, Iván levanta la mano mientras Sara habla. ¿Qué hace bien Iván?", "Espera su turno", "Pide hablar sin interrumpir."),
    ],
    [
        E("Tema: «Cuidar el huerto». Eli dice: «Podemos poner un cartel». Dani dice: «Sobre el cartel, podría decir que no pisen las plantas». ¿Dani mantiene el foco?", "Sí", "Se apoya en lo que dijo Eli y habla del huerto."),
        E("Tema: «Cuidar el huerto». Rita dice: «Siempre me gustó el color verde» y no lo relaciona con el huerto. ¿Su idea mantiene el foco?", "No", "No responde al tema por sí sola."),
    ],
    [
        E("Tema: «Una fiesta de fin de año en el curso». Ordena para participar bien: a) hablar de la fiesta b) esperar mi turno c) pensar si mi idea responde al tema. Escribe las letras.", "c, b, a", "Pienso, espero y hablo."),
        E("Dos compañeros hablan a la vez. ¿Cuál es el mejor acuerdo: a) hablar más fuerte b) hablar uno a la vez por turnos?", "b", "Los turnos cuidan que todos se oigan."),
    ],
    [E("Tema: «Cómo cuidar los libros de la sala». Cuatro intervenciones: a) «Forrarlos con papel.» b) «El domingo vi una película.» c) «No dejarlos abiertos al revés.» d) «Mi hermano tiene un patinete». ¿Cuántas mantienen el foco?", "Dos", "Solo a y c hablan de cuidar libros.")],
    [
        E("¿Mantener el foco es hablar del tema?", "Sí", "Lo que digo se relaciona con el tema."),
        E("¿Interrumpir ayuda a conversar?", "No", "Quita el turno a quien habla."),
        E("¿Puedo conectar mi idea con la anterior?", "Sí", "Ayuda a que la conversación avance."),
    ],
    ("Conversa por turnos y con foco. El tema es «Cómo cuidar las plantas del patio». Escribe o cuenta una idea tuya que mantenga el foco, una frase para volver al tema si alguien se desvía y una forma de pedir tu turno. Frases posibles para el turno: «Levanto la mano» o «Espero una pausa y digo: ¿puedo agregar algo?».",
     "Idea: regarlas por la mañana. Para volver al tema: «Gracias, volvamos a las plantas». Turno: levanto la mano.",
     ["su idea se relaciona con el tema", "propone una frase amable para volver al tema", "describe cómo pedir el turno"], ["hoja con tres respuestas o conversación breve con alguien de tu casa"], ["idea fuera del tema", "volver al tema con una frase descortés"],
     "Si la idea se desvía, pregunta cómo se relaciona con las plantas."),
    "Conversa con una persona de tu casa sobre un tema por cinco turnos cada uno, cuidando que todo se relacione con él.",
    "Cuenta qué harías si dos compañeros se desvían del tema al mismo tiempo.",
)

# ================================================================ OA 26 · clase 3
reg(
    OA26, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar preguntas.",
    "Aprenderé a preguntar para aclarar dudas y a mostrar interés por lo que dicen los demás. Sirve para entender mejor y para que quien habla se sienta escuchado.",
    ["Sé mantener el foco de una conversación.", "Sé esperar mi turno."],
    [
        "Una pregunta para aclarar sirve para entender mejor lo que alguien dijo. No es una pregunta para criticar ni para decir que la otra persona se equivocó. Empieza con frases como «¿Qué quieres decir con…?», «¿Puedes dar un ejemplo?» o «¿Me lo explicas otra vez?».",
        "Preguntamos cuando no entendemos una palabra, cuando falta un dato o cuando queremos saber más sobre lo que contó una persona. Así mostramos interés. También mostramos interés con gestos: mirar a quien habla, asentir con la cabeza y no hacer otra cosa mientras escuchamos.",
        "La pregunta debe ser clara y respetuosa. Una pregunta dicha con burla o enojo, como «¿Cómo puedes decir eso?», no aclara, solo molesta. Con voz tranquila y mirando a la persona, una pregunta como «¿Puedes contarme más?» ayuda a que la conversación avance.",
    ],
    [("aclarar", "hacer que algo se entienda mejor"), ("pregunta", "frase con la que pedimos información"), ("ejemplo", "caso que ayuda a entender una idea"), ("interés", "ganas de saber y atención hacia lo que dicen"), ("respetuoso", "que trata bien a la otra persona")],
    [
        ("Elegir la pregunta que aclara", "Tomás dice: «Mi tía hace una cosa rara con las plantas». ¿Qué pregunta aclara: «¿Qué cosa hace con las plantas?» o «¿Para qué cuentas eso?».", ["Busco una pregunta que pida información.", "La primera pide más datos.", "La segunda suena a crítica."], "«¿Qué cosa hace con las plantas?»."),
        ("Pedir un ejemplo", "Lía dice: «Hay que ser solidario». No entiendes la palabra. ¿Cómo pides ayuda?", ["Uso una frase amable.", "Pido un ejemplo.", "Pregunto sin criticar."], "«¿Puedes dar un ejemplo de ser solidario?»."),
    ],
    [("Preguntar con burla o enojo: «¿Cómo puedes decir eso?».", "No aclara; hace sentir mal a quien habla.", "Pregunta con curiosidad: «¿Me explicas por qué piensas eso?»."), ("Hacer una pregunta que ya fue respondida porque no escuchaste.", "Muestra falta de atención.", "Escucha primero hasta el final y pregunta lo que falte.")],
    [
        E("¿Una pregunta para aclarar sirve para entender mejor o para criticar?", "Para entender mejor", "Su meta es comprender."),
        E("¿Cuál es una pregunta para aclarar: «¿Qué quieres decir con ‘abono’?» o «¡Eso está mal!»?", "¿Qué quieres decir con ‘abono’?", "Pide el significado de la palabra."),
        E("¿Mirar a quien habla muestra interés?", "Sí", "Muestra atención y respeto."),
    ],
    [
        E("Marcos dice: «El cuento pasa en una aldea». No sabes qué es una aldea. ¿Qué preguntas?", "¿Qué es una aldea?", "Pide la definición de la palabra."),
        E("¿Por qué «¿Cómo puedes decir eso?», dicho con enojo, no es una buena pregunta para aclarar?", "Porque ofende y no pide información", "No ayuda a comprender y lastima."),
        E("Elige la mejor opción para mostrar interés: a) mirar el celular b) mirar a quien habla y asentir.", "b", "Así demuestras que escuchas."),
    ],
    [
        E("Ana dice: «Fui al lugar donde viven los patos». Para aclarar qué lugar es, ¿qué preguntas: a) ¿Cómo se llama ese lugar? b) ¿Y a mí qué me importa?", "a", "Pide el dato que falta sin criticar."),
        E("Beto dice: «Mi hermano cuida un animal». Elige la pregunta que aclara más: a) ¿Qué animal cuida? b) ¿Para qué hablas de eso?", "a", "La a pide un dato concreto."),
        E("Un compañero cuenta algo largo y no entiendes la parte final. ¿Qué frase usas: «¿Me lo explicas otra vez?» o «No te entiendo nada»?", "¿Me lo explicas otra vez?", "Es amable y pide ayuda."),
    ],
    [
        E("Sofía dice: «Prefiero el verano». Ema pregunta: «¿Por qué es mejor que el invierno?» Pedro pregunta: «¿Qué es lo que más te gusta del verano?». ¿Cuál pregunta busca aclarar sin comparar ni criticar?", "La de Pedro", "Pide más información de su opinión."),
        E("Luis dijo que su abuelo vive lejos. Pregunta aclaratoria: «¿Dónde vive?» o «¿Y tu papá?»", "¿Dónde vive?", "Aclara lo que contó Luis; la otra pregunta supone algo sobre su familia."),
    ],
    [
        E("Elena dice: «En mi casa hacemos pan». Escribe una pregunta que muestre interés sin suponer quién lo hace.", "¿Cómo hacen el pan?", "Pide información sin suponer quién cocina."),
        E("Un compañero contó que su perro es muy tranquilo. ¿Qué pregunta muestra interés: a) ¿Cómo se llama y qué le gusta hacer? b) ¡Qué aburrido!", "a", "Pide información con respeto."),
    ],
    [E("En una conversación, Carla dijo que su tía le enseñó a tejer. Tu pregunta puede ser «¿Cómo te enseñó?» o «Eso no sirve». ¿Cuál escoges para aclarar y mostrar interés?", "¿Cómo te enseñó?", "Pide detalles y valora lo contado.")],
    [
        E("¿Preguntar para aclarar es lo mismo que criticar?", "No", "Aclarar busca entender."),
        E("¿Puedo pedir un ejemplo?", "Sí", "Un ejemplo ayuda a comprender."),
        E("¿Debo escuchar hasta el final antes de preguntar?", "Sí", "Evita repetir preguntas ya respondidas."),
    ],
    ("Practica preguntas que aclaran. Lee lo que dijo Nico en una conversación: «Voy a un lugar con muchos árboles y una cosa grande que da sombra. Allí siempre hay un animal que canta». Escribe tres preguntas para aclarar (una sobre el lugar, una sobre el animal y otra para pedir un ejemplo) y una frase para mostrar interés. Pide a una persona de tu casa que responda con detalles inventados.",
     "¿Qué lugar es? ¿Qué animal canta? ¿Puedes dar un ejemplo de lo que da sombra? Me interesa lo que cuentas.",
     ["escribe tres preguntas claras", "las preguntas piden información y no critican", "incluye una frase de interés"], ["hoja con preguntas o conversación breve"], ["preguntas que ofenden", "preguntas ya contestadas en lo dicho"],
     "Si una pregunta suena a crítica, cámbiala por «¿Puedes contarme más?»."),
    "Haz tres preguntas para aclarar a alguien de tu casa sobre un cuento que te cuente.",
    "Escribe cinco frases para empezar preguntas que aclaran y úsalas con alguien.",
)

# ================================================================ OA 26 · clase 4
reg(
    OA26, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar.",
    "Aprenderé a construir sobre lo que dijeron otros: agregar ideas, mostrar acuerdo y demostrar empatía. Sirve para que la conversación crezca y para que las personas se sientan comprendidas.",
    ["Sé mantener el foco.", "Sé preguntar para aclarar."],
    [
        "Construir sobre lo dicho significa usar la idea de otra persona para avanzar. Podemos agregar algo con «Además…», estar de acuerdo con «Coincido con Ana porque…», o ampliar con «Eso me hace pensar en…». Así la conversación no es una lista de ideas sueltas, sino una conversación conectada.",
        "La empatía es entender cómo se siente otra persona y mostrar que nos importa. Si alguien cuenta algo difícil, podemos decir «Entiendo que te hayas sentido así» o «Debe haber sido incómodo». No hace falta dar consejos ni contar lo nuestro enseguida. Primero escuchamos y reconocemos lo que siente.",
        "Es importante no usar la empatía para quitarle importancia a lo que siente la otra persona. Frases como «No es para tanto» o «Exageras» no ayudan. Con una frase de empatía, una mirada atenta y un tono tranquilo, mostramos que escuchamos de verdad.",
    ],
    [("construir", "usar una idea de otro para avanzar"), ("acuerdo", "estar de acuerdo con una idea"), ("empatía", "entender cómo se siente otra persona"), ("conector", "palabra que une ideas, como además o por eso"), ("reconocer", "decir que sé lo que le pasa a otra persona")],
    [
        ("Agregar a lo que dijo otro", "Ana dice: «Podemos plantar lechugas en el huerto». Quieres agregar que se necesita agua. Escribe cómo conectar tu idea.", ["Uso la idea de Ana.", "Empiezo con «Además» o «Sobre lo que dijo Ana».", "Agrego lo del agua."], "«Sobre lo que dijo Ana, además se necesita agua para las lechugas.»"),
        ("Responder con empatía", "Teo cuenta: «Hoy me fue mal en el partido y me dio vergüenza». ¿Qué respuesta muestra empatía?", ["Reconozco lo que siente Teo.", "No le quito importancia.", "Escojo una frase amable."], "«Entiendo que hayas sentido vergüenza.»"),
    ],
    [("Responder a un problema con «No es para tanto».", "Le quita importancia a lo que siente la persona.", "Di: «Entiendo cómo te sientes» y escucha."), ("Repetir exactamente lo que dijo otro.", "No suma nada nuevo.", "Agrega un dato, ejemplo o razón propia.")],
    [
        E("Para agregar una idea, ¿puedo usar «Además…» o «Nunca»?", "Además", "Añade algo a lo anterior."),
        E("En Lenguaje: ¿Qué es la empatía?", "Entender cómo se siente otra persona", "Significa ponerse en su lugar."),
        E("Teo dijo que tiene vergüenza. ¿Qué respuesta es empática: «Entiendo cómo te sientes» o «No es para tanto»?", "Entiendo cómo te sientes", "Reconoce lo que siente sin restarle importancia."),
    ],
    [
        E("¿Por qué construir sobre lo dicho ayuda a conversar?", "Porque las ideas se conectan y avanzan", "La conversación no queda en ideas sueltas."),
        E("Ana propuso plantar lechugas. Bea dice: «Coincido con Ana porque son fáciles de cuidar». ¿Bea muestra acuerdo?", "Sí", "Usa «coincido» y da una razón."),
        E("¿Cuál frase muestra empatía: «Debe haber sido incómodo» o «Cuenta otra cosa»?", "Debe haber sido incómodo", "Reconoce lo difícil de la situación."),
    ],
    [
        E("Sara dice: «Hay que reciclar el papel». Escribe una frase que construya sobre su idea con «Además».", "Además, podemos usar las hojas por los dos lados", "Suma una idea relacionada."),
        E("Dani cuenta: «Se me perdió mi libro favorito y estoy triste». Elige una respuesta con empatía: a) «Entiendo que estés triste; era tu libro favorito.» b) «Compra otro y listo.»", "a", "Reconoce lo que siente."),
        E("Luis dice: «Yo también pienso que sí». Falta algo. ¿Qué debería agregar para construir sobre lo dicho: una razón o un chiste?", "Una razón", "La razón suma a la conversación."),
    ],
    [
        E("Ana dice: «Hay que cuidar el patio». Eli dice: «Yo también». Ben dice: «Yo también pienso eso porque así habrá sombra para todos». ¿Quién construyó mejor sobre la idea?", "Ben", "Suma una razón nueva."),
        E("Mia cuenta que se siente nerviosa por exponer. Lía responde: «No pasa nada, es fácil». Pía responde: «Entiendo que estés nerviosa, ¿qué te preocupa?». ¿Quién mostró más empatía?", "Pía", "Reconoce lo que siente y pregunta."),
    ],
    [
        E("Un amigo cuenta que su mascota está enferma. ¿Qué respuesta mezcla empatía y ayuda: «Entiendo que estés preocupado; ¿quieres contarme más?» o «Seguro se mejora»?", "Entiendo que estés preocupado; ¿quieres contarme más?", "Reconoce lo que siente y abre la conversación."),
        E("Ordena los pasos para responder con empatía: a) hacer una pregunta amable b) escuchar sin interrumpir c) decir cómo creo que se siente. Escribe las letras.", "b, c, a", "Primero escucho, luego reconozco y después pregunto."),
    ],
    [E("En el grupo Tomás dijo que quiere hacer un mural. Ema dijo que podría ser del mar. Carla quiere agregar que se pinten peces. ¿Qué frase construye mejor: «Además del mar de Ema, podemos pintar peces» o «Yo quiero otra cosa»?", "Además del mar de Ema, podemos pintar peces", "Une su idea con la de Ema.")],
    [
        E("¿Puedo mostrar acuerdo y dar una razón?", "Sí", "Así mi aporte suma."),
        E("¿Empatía es entender lo que siente otra persona?", "Sí", "Es ponerse en su lugar."),
        E("¿«No es para tanto» muestra empatía?", "No", "Le quita importancia a lo que siente."),
    ],
    ("Construye sobre lo dicho y responde con empatía. Lee: «Pía dice: Propongo hacer un mural del barrio. Hugo dice: Yo también quiero, pero me da vergüenza pintar porque no sé dibujar». Escribe: 1) una frase que construya sobre la idea de Pía con «Además», 2) una respuesta empática para Hugo, 3) una pregunta amable para el grupo.",
     "1) Además, podemos dividir el mural en partes pequeñas. 2) Entiendo que sientas vergüenza. 3) ¿Qué parte del mural le gustaría pintar a cada uno?",
     ["construye sobre la idea de Pía", "responde a Hugo sin restarle importancia", "formula una pregunta amable"], ["hoja con tres frases o conversación breve"], ["responder con «no pasa nada»", "no relacionar con la idea de Pía"],
     "Si la respuesta resta importancia, cámbiala por «Entiendo que…»."),
    "Cuenta a una persona de tu casa una situación del colegio y pídele que responda con empatía.",
    "Escribe tres frases de empatía distintas para tres situaciones del recreo.",
)

# ================================================================ OA 26 · clase 5
reg(
    OA26, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: dos personas de tu casa para conversar con respeto.",
    "Aprenderé a decir que pienso distinto sin descalificar a la otra persona. Sirve para conversar en grupo aunque no estemos de acuerdo, sin burlas ni insultos.",
    ["Sé dar mi opinión con una razón.", "Sé preguntar para aclarar."],
    [
        "En una conversación no siempre pensamos igual. Un desacuerdo es cuando dos personas tienen opiniones distintas. Eso es normal y puede ser útil, porque nos ayuda a conocer otras razones. Lo importante es discrepar con respeto, es decir, decir lo que pienso sin tratar mal a la otra persona.",
        "Una forma respetuosa de discrepar es: «Yo pienso distinto, porque…». Primero reconozco lo que dijo la otra persona: «Entiendo tu idea, pero yo pienso que…». Hablo de la idea, no de la persona. Descalificar es decir que alguien o algo es tonto, malo o inútil: «Eso es una tontera» es una descalificación.",
        "Si alguien se burla o dice algo que lastima, puedo decir con calma: «Prefiero que no hables así». Si sigue, aviso a una persona adulta. En un desacuerdo, cada uno puede explicar sus razones y pensar si quiere cambiar de opinión. A veces nos quedamos en desacuerdo y también está bien.",
    ],
    [("desacuerdo", "cuando dos personas piensan distinto"), ("discrepar", "decir que pienso distinto"), ("descalificar", "tratar mal a una persona o a su idea con palabras como tonto o inútil"), ("burla", "reírse de alguien para hacerle daño"), ("respeto", "tratar bien a los demás aunque piensen distinto")],
    [
        ("Discrepar con respeto", "Ema dice: «Para el mural, lo mejor es pintar un bosque». Tú prefieres pintar el mar. ¿Cómo lo dices con respeto?", ["Reconozco su idea.", "Digo que pienso distinto.", "Agrego mi razón."], "«Entiendo tu idea, pero yo pienso distinto: el mar tiene muchos colores.»"),
        ("Reconocer una descalificación", "Alguien dice: «Tu idea es una tontera». ¿Qué palabra descalifica?", ["Busco una palabra que ofende.", "«Tontera» trata mal la idea.", "No aporta razones."], "«Tontera»."),
    ],
    [("Responder a una idea con «Eso es tonto».", "Descalifica y puede hacer sentir mal a alguien.", "Di: «Pienso distinto porque…»."), ("Enojarse porque alguien piensa distinto.", "Pensar distinto es normal.", "Escucha sus razones y explica las tuyas.")],
    [
        E("Dos personas piensan distinto sobre el mural. ¿Eso es un desacuerdo o un acuerdo?", "Un desacuerdo", "Hay opiniones distintas."),
        E("¿Es respetuoso decir «Pienso distinto porque…»?", "Sí", "Es una forma de discrepar con razón."),
        E("¿Cuál descalifica: «Eso es inútil» o «Yo pienso distinto»?", "Eso es inútil", "Trata mal la idea o a la persona."),
    ],
    [
        E("¿Por qué conviene reconocer la idea de otro antes de discrepar?", "Porque muestra que lo escuché y lo respeto", "Baja la tensión y facilita la conversación."),
        E("¿Un desacuerdo es malo siempre?", "No", "Puede ayudar a conocer otras razones."),
        E("Si alguien se burla, ¿qué puedo decir con calma: «Prefiero que no hables así» o «Tú eres peor»?", "Prefiero que no hables así", "Dice lo que quiero sin atacar."),
    ],
    [
        E("Teo dice: «Prefiero un huerto de flores». Tú prefieres uno de verduras. Escribe una frase respetuosa para discrepar.", "Entiendo tu idea, pero yo pienso distinto: las verduras se pueden comer", "Reconoce, discrepa y da razón."),
        E("Marca la respuesta respetuosa: a) «Tu idea es mala.» b) «No estoy de acuerdo porque creo que no alcanzará el espacio.»", "b", "Habla de la idea y da una razón."),
        E("Ana se ríe de la propuesta de Luis y dice: «¡Qué idea más ridícula!». ¿Eso es una burla o una discrepancia respetuosa?", "Una burla", "Se ríe de la idea para hacer sentir mal a Luis."),
    ],
    [
        E("Sara dice: «Esa idea no sirve para nada». Pía dice: «No lo veo igual: creo que no resultará porque falta tiempo». ¿Quién discrepa con respeto?", "Pía", "No descalifica y explica."),
        E("Después de escuchar razones, Hugo cambia de opinión. ¿Hizo algo malo?", "No", "Cambiar de opinión con razones es parte de conversar."),
    ],
    [
        E("Un compañero dice: «Mi idea es mejor porque yo soy el mayor». Pedro responde: «Entiendo, pero la edad no explica por qué tu idea es mejor». ¿Pedro descalifica?", "No", "Habla de la razón y no ataca a la persona."),
        E("En un desacuerdo, ¿es válido terminar diciendo «Cada uno piensa distinto y está bien»?", "Sí", "A veces no se llega a un acuerdo y eso es posible."),
    ],
    [E("Tu grupo debe elegir entre un mural del mar o un mural del bosque. Julián dice «el bosque es lo mejor». Tú prefieres el mar. ¿Cuál es la mejor respuesta: «Entiendo que te guste el bosque, pero prefiero el mar porque tiene muchos colores» o «Qué aburrido el bosque»?", "Entiendo que te guste el bosque, pero prefiero el mar porque tiene muchos colores", "Discrepa con respeto y razón.")],
    [
        E("¿Pensar distinto es normal?", "Sí", "Cada persona tiene sus razones."),
        E("¿Puedo burlarme de una idea?", "No", "La burla lastima y no aporta."),
        E("¿Hablar de la idea y no de la persona es respetuoso?", "Sí", "Así se evita descalificar."),
    ],
    ("Discrepa con respeto. Lee: «Lía dice: Para el cumpleaños del curso hagamos solo música. Matías dice: Yo prefiero que también haya juegos». Escribe: 1) una respuesta de Matías que reconozca la idea de Lía y diga que piensa distinto, 2) una forma de decir «prefiero que no hables así» si alguien se burla, 3) una propuesta para llegar a un acuerdo.",
     "1) Entiendo tu idea, pero yo pienso distinto: también podría haber juegos para quienes no quieren bailar. 2) Prefiero que no hables así. 3) Podemos hacer media hora de música y media hora de juegos.",
     ["reconoce la idea del otro", "discrepa sin descalificar", "propone un acuerdo"], ["hoja con tres respuestas o conversación breve"], ["usar palabras que ofenden", "no dar razón"],
     "Si aparece una palabra que ofende, pregunta cómo se diría sin atacar."),
    "Conversa con una persona de tu casa sobre un tema donde piensen distinto, usando «Yo pienso distinto, porque…».",
    "Escribe tres frases para discrepar con respeto en tres situaciones del colegio.",
)

# ================================================================ OA 26 · clase 6
reg(
    OA26, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar el cierre.",
    "Aprenderé a cerrar una conversación de grupo: resumir los acuerdos, nombrar los desacuerdos y dejar preguntas abiertas. Sirve para que todos sepan qué se decidió y qué queda por pensar.",
    ["Sé mantener el foco.", "Sé discrepar con respeto."],
    [
        "Cuando una conversación de grupo termina, conviene cerrar. Cerrar significa recordar lo que se acordó, lo que sigue en desacuerdo y lo que todavía no sabemos. Así nadie se queda con dudas. Un acuerdo es una decisión que el grupo aceptó. Un desacuerdo pendiente es una idea en la que todavía pensamos distinto.",
        "Una pregunta abierta es una pregunta que no se responde con sí o no y que invita a seguir pensando. Por ejemplo: «¿Cómo podemos cuidar el huerto en vacaciones?». Una pregunta abierta deja el tema vivo para otra conversación. Se diferencia de una pregunta cerrada, como «¿Regamos hoy?».",
        "Para cerrar usamos una estructura: «Acordamos que…», «Seguimos pensando distinto en…», «Nos queda la pregunta…». También agradecemos a quienes participaron y confirmamos que todos pudieron hablar. Cerrar con respeto es la última forma de cuidar la conversación.",
    ],
    [("cerrar", "terminar una conversación recordando lo importante"), ("acuerdo", "decisión que el grupo aceptó"), ("desacuerdo pendiente", "tema en el que aún se piensa distinto"), ("pregunta abierta", "pregunta que invita a pensar y no se responde con sí o no"), ("resumen", "texto breve con las ideas principales")],
    [
        ("Armar un cierre", "El grupo acordó regar los lunes y miércoles. No se acordó quién compra las semillas. Armen un cierre con la estructura «Acordamos…, Seguimos pensando… y Nos queda la pregunta…».", ["Escribo el acuerdo.", "Escribo el desacuerdo pendiente.", "Formulo una pregunta abierta."], "Acordamos regar lunes y miércoles. Seguimos pensando quién compra las semillas. Nos queda la pregunta: ¿cómo podemos conseguir semillas para todos?"),
        ("Distinguir pregunta abierta", "¿Cuál es abierta: «¿Regamos hoy?» o «¿Cómo cuidamos el huerto en vacaciones?».", ["Veo si se responde con sí o no.", "La primera sí.", "La segunda invita a pensar."], "«¿Cómo cuidamos el huerto en vacaciones?»."),
    ],
    [("Terminar la conversación sin decir qué se acordó.", "Algunos no saben qué se decidió.", "Recuerda en voz alta: «Acordamos que…»."), ("Hacer solo preguntas de sí o no al final.", "No invitan a seguir pensando.", "Pregunta con «cómo» o «por qué».")],
    [
        E("¿Un acuerdo es una decisión que el grupo aceptó?", "Sí", "Todos lo aprobaron."),
        E("¿Cuál es una pregunta abierta: «¿Cómo ayudamos al huerto?» o «¿Regamos hoy?»", "¿Cómo ayudamos al huerto?", "Invita a pensar y no se responde con sí o no."),
        E("¿Para qué se cierra una conversación?", "Para recordar lo acordado y lo que queda", "Ayuda a que todos sepan qué sigue."),
    ],
    [
        E("¿Qué es un desacuerdo pendiente?", "Una idea en la que aún se piensa distinto", "Quedó sin resolver."),
        E("«Acordamos que habrá turnos para regar.» ¿Es un acuerdo o una pregunta?", "Un acuerdo", "Es una decisión del grupo."),
        E("¿Qué hace mejor un cierre: «Chao, nos vemos» o «Acordamos que…, nos queda la pregunta…»?", "Acordamos que…, nos queda la pregunta…", "Resume y deja ideas para después."),
    ],
    [
        E("El grupo decidió limpiar la sala el viernes pero no sabe qué materiales usar. Escribe el acuerdo con «Acordamos que».", "Acordamos que limpiaremos la sala el viernes", "Es la decisión tomada."),
        E("Con la misma conversación, escribe el desacuerdo pendiente.", "Seguimos pensando qué materiales usar", "Todavía no se decidió."),
        E("Con la misma conversación, escribe una pregunta abierta.", "¿Qué materiales podríamos usar para limpiar la sala?", "Invita a pensar sin responder sí o no."),
    ],
    [
        E("Ana cierra: «Terminamos, vámonos». Luis cierra: «Acordamos que habrá turnos; nos queda la pregunta de cómo avisar». ¿Quién cierra mejor?", "Luis", "Resume el acuerdo y deja una pregunta."),
        E("Una pregunta como «¿Está bien?» ¿ayuda a cerrar con ideas nuevas?", "No", "Se responde con sí o no y no invita a pensar."),
    ],
    [
        E("Una compañera casi no habló. ¿Qué puede hacer quien cierra: preguntarle si quiere agregar algo o terminar sin preguntar?", "Preguntarle si quiere agregar algo", "Así todos tienen oportunidad de participar."),
        E("En un cierre falta la pregunta abierta. Elige la adecuada: a) ¿Qué otras formas hay de cuidar los libros? b) ¿Los cuidamos?", "a", "Invita a pensar en distintas formas."),
    ],
    [E("Tu grupo acordó forrar los libros, pero no decidió quién los forra. ¿Cuál es el desacuerdo pendiente: a) forrar los libros b) quién los forra?", "b", "Es lo que aún no se decidió.")],
    [
        E("¿Cerrar una conversación es parte de conversar bien?", "Sí", "Ayuda a recordar lo acordado."),
        E("¿Puedo dejar una pregunta abierta?", "Sí", "Invita a seguir pensando."),
        E("¿Debo dar las gracias al terminar?", "Sí", "Reconoce la participación de todos."),
    ],
    ("Cierra una conversación. El grupo habló de «Cómo cuidar los materiales del curso». Se acordó guardar los lápices en una caja. No se acordó quién cuida la caja. Escribe o di en voz alta un cierre con: 1) «Acordamos que…», 2) «Seguimos pensando en…», 3) «Nos queda la pregunta…» y una frase de agradecimiento.",
     "Acordamos que guardaremos los lápices en una caja. Seguimos pensando quién cuida la caja. Nos queda la pregunta: ¿cómo podemos turnarnos para cuidarla? Gracias a todos por participar.",
     ["recuerda el acuerdo", "dice qué queda pendiente", "formula una pregunta abierta", "agradece"], ["hoja con el cierre o cierre oral"], ["omitir el desacuerdo pendiente", "pregunta cerrada"],
     "Si la pregunta se responde con sí o no, pide cambiarla por «cómo» o «por qué»."),
    "Practica el cierre con una persona de tu casa sobre un tema que hayan conversado.",
    "Escribe tres preguntas abiertas distintas para cerrar una conversación sobre el recreo.",
)

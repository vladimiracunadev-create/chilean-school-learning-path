"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 24 (teatro infantil) y OA 25 (conversaciones grupales)."""
from __future__ import annotations

from student_lessons import ex, register

OA24, OA25 = "LE02 OA 24", "LE02 OA 25"
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


# ================================================================ OA 24
reg(
    OA24, 1,
    "Este cuaderno, lápiz y una hoja. Si puedes, una obra en vivo o grabada con un adulto; si no, usa el afiche y la escena escritos aquí.",
    "Aprenderé a prepararme para ver una obra de teatro y a poner acuerdos de público que cuidan la función. Sirve para disfrutar la obra y no molestar a nadie.",
    ["Sé que un cuento tiene personajes.", "Sé esperar mi turno para hablar."],
    [
        "Una obra de teatro es una historia que personas cuentan con su voz y su cuerpo frente a un público. El público es el grupo que mira y escucha. Antes de la función, leemos el afiche: dice el título, el lugar y la hora.",
        "El público también ayuda a que la obra salga bien. Por eso hacemos acuerdos: llegar a tiempo, apagar el celular, mirar y escuchar con atención. Reír cuando algo es gracioso y aplaudir al final también está bien, porque los actores nos ven y se alegran.",
        "Un buen acuerdo cuida a todos. Una regla que nos obliga a quedarnos como estatuas, sin reír ni respirar fuerte, no ayuda a disfrutar. Antes de ver una obra, también podemos pensar qué esperamos ver, usando el título y el afiche como pistas.",
    ],
    [("obra", "historia que se cuenta en el teatro"), ("público", "personas que miran y escuchan la obra"), ("escenario", "lugar donde actúan los actores"), ("función", "cada vez que se presenta una obra"), ("acuerdo", "regla que decidimos entre todos")],
    [
        ("Leer el afiche", "Afiche: «El dragón con hipo. Sala Azul. Sábado a las 16:00». ¿Qué obra veremos y cuándo?", ["Busco el título.", "Busco el día y la hora.", "Los junto en una frase."], "Veremos «El dragón con hipo» el sábado a las 16:00."),
        ("Elegir un buen acuerdo", "Dos propuestas: «Apagar el celular» y «No mover ni un dedo». ¿Cuál cuida la función?", ["Pienso si la regla ayuda a todos.", "Veo que apagar el celular evita ruidos.", "Veo que no mover ni un dedo no deja disfrutar."], "Apagar el celular."),
    ],
    [("Creer que el público debe quedarse inmóvil y callado todo el tiempo.", "Se confunde cuidar la función con no sentir nada.", "Puedes reír, mirar y aplaudir sin molestar."), ("Pensar que solo importa el final de la historia.", "Se olvida que la obra se disfruta desde el comienzo.", "Mira también la voz, los gestos y el escenario.")],
    [
        E("Antes de una obra, ¿es mejor llegar con tiempo o cuando ya empezó?", "Llegar con tiempo", "Así encuentras tu lugar sin molestar."),
        E("Afiche: «Función: domingo a las 11:00». ¿A qué hora empieza?", "A las 11:00", "La hora está escrita en el afiche."),
        E("Durante la obra, ¿el público mira y escucha, o habla fuerte con el vecino?", "Mira y escucha", "Hablar fuerte molesta a los demás."),
    ],
    [
        E("¿Qué es el público?", "Las personas que miran y escuchan la obra", "El público es quien ve la función."),
        E("Acuerdo: «Reír cuando algo es gracioso». ¿Cuida la función o la daña?", "La cuida", "Reír no molesta y muestra que disfrutas."),
        E("¿Por qué se pide apagar el celular?", "Porque su luz y su sonido distraen", "Los demás no podrían concentrarse."),
    ],
    [
        E("Afiche: «Los tres patitos. Teatro del Parque. Viernes 17:00». Escribe el título y el lugar.", "Los tres patitos; Teatro del Parque", "Son los datos del título y del lugar."),
        E("Clasifica cada acuerdo como «cuida» o «no cuida»: a) aplaudir al final, b) contar el final en voz alta, c) apagar el celular.", "a cuida, b no cuida, c cuida", "Contar el final arruina la sorpresa de los demás."),
        E("El título es «El dragón con hipo». ¿Qué personaje esperas ver?", "Un dragón", "El título nombra al dragón."),
    ],
    [
        E("Regla A: «No hablar mientras los actores hablan». Regla B: «No moverse ni respirar fuerte en toda la función». ¿Cuál es razonable?", "La regla A", "La B no se puede cumplir y no cuida a nadie."),
        E("Tomás se rió cuando el dragón tuvo hipo, igual que toda la sala. ¿Rompió un acuerdo?", "No", "Reír con gracia es parte de disfrutar la obra."),
    ],
    [
        E("Una compañera dice: «En el teatro hay que quedarse como estatua». ¿Tiene razón?", "No", "Se puede reír y aplaudir sin molestar."),
        E("Ordena: a) aplaudir al final, b) sentarse y apagar el celular, c) ver la obra.", "b, c, a", "Primero te preparas, luego miras y al final aplaudes."),
    ],
    [E("Tu curso verá una obra de títeres. Se proponen dos acuerdos: «Apagamos el celular» y «Nadie puede mover ni un dedo». ¿Cuál eliges?", "Apagamos el celular", "Cuida la función sin quitar el disfrute.")],
    [
        E("¿Dónde leo la hora de una función?", "En el afiche", "El afiche trae título, lugar y hora."),
        E("¿Aplaudir al final es parte de ser buen público?", "Sí", "Muestra respeto a quienes actuaron."),
        E("¿Un acuerdo de público cuida a todos o solo a uno?", "A todos", "Se hace entre todos para todos."),
    ],
    ("Prepara tus acuerdos de público. Lee este afiche: «Obra: La luna que perdió su luz. Lugar: Sala Verde. Hora: 15:30». Escribe tres acuerdos para ver la obra: uno sobre el celular, uno sobre escuchar y uno sobre reír o aplaudir. Escribe también qué esperas ver, usando el título como pista. Hazlo en tu hoja o cuéntaselo a un adulto.",
     "1) Apagar el celular. 2) Escuchar sin hablar encima de los actores. 3) Reír si algo es gracioso y aplaudir al final. Espero ver una luna triste que busca su luz, por el título.",
     ["escribe tres acuerdos que cuidan la función", "ninguno exige quedarse inmóvil", "usa el título del afiche como pista"], ["hoja con los acuerdos", "explicación oral a un adulto"], ["acuerdos que prohíben reír o moverse del todo", "no usar el título como pista"],
     "Si un acuerdo prohíbe reír, pregunta si la regla ayuda a disfrutar y propone otra."),
    "Lee otro afiche inventado por un adulto y di título, lugar y hora.",
    "Escribe un afiche para una obra imaginaria con título, lugar y hora.",
)

reg(
    OA24, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: un adulto que lea la escena en voz alta con distintas voces.",
    "Aprenderé a notar cómo la voz, el gesto y el espacio muestran lo que siente un personaje. Sirve para entender mejor una obra y para actuar con más claridad.",
    ["Sé qué es un personaje.", "Sé que una obra se cuenta con voz y cuerpo."],
    [
        "En el teatro no solo importan las palabras. La voz cambia: puede ser fuerte, bajita, rápida o lenta. El gesto es lo que hace la cara o el cuerpo, como encoger los hombros o sonreír. El espacio es dónde está cada personaje en el escenario, cerca o lejos de otro.",
        "Cuando un personaje habla rápido y fuerte, a menudo está apurado o enojado. Si habla bajito y se sienta en el suelo, puede estar triste o cansado. Si se acerca a otro y habla suave, quiere ayudar o consolar. Esas pistas nos cuentan la escena sin que nadie las explique.",
        "Para observar bien, hacemos una pregunta: ¿qué hizo el personaje y qué pude sentir por eso? Nombramos la pista (voz, gesto o espacio) y decimos qué muestra. Así no solo contamos lo que pasó, también explicamos cómo se contó.",
    ],
    [("voz", "sonido que usa el personaje al hablar"), ("gesto", "movimiento de la cara o del cuerpo"), ("espacio", "lugar del escenario donde está cada personaje"), ("pista", "señal que ayuda a entender algo"), ("escena", "parte corta de una obra")],
    [
        ("Pista de voz", "Lola entra corriendo y grita: «¡Perdí mi gorro!». ¿Qué pista de voz hay y qué muestra?", ["La voz es fuerte y rápida.", "Entra corriendo.", "Pienso qué siente alguien así."], "Voz fuerte y rápida: está preocupada y apurada."),
        ("Pista de espacio", "Tomás camina hacia Lola y se queda a su lado. ¿Qué muestra el espacio?", ["Tomás se acerca.", "Se queda junto a ella.", "Eso indica cuidado."], "Se acerca para acompañarla y ayudarla."),
    ],
    [("Contar solo qué pasó.", "Se olvida mirar cómo lo mostraron.", "Agrega una pista de voz, gesto o espacio."), ("Decir «estaba triste» sin dar una pista.", "No se explica de dónde sale la idea.", "Di: «Habló bajito, por eso parecía triste».")],
    [
        E("Un personaje habla muy fuerte y rápido. ¿Parece apurado o tranquilo?", "Apurado", "La voz fuerte y rápida muestra apuro."),
        E("Un personaje se sienta en el suelo y baja la cabeza. ¿Qué parte muestra eso: voz, gesto o espacio?", "El gesto", "La cabeza baja es un movimiento del cuerpo."),
        E("Dos personajes se paran muy lejos uno del otro. ¿Qué cambió: el espacio o la voz?", "El espacio", "Cambió dónde están en el escenario."),
    ],
    [
        E("En Lenguaje: ¿Qué es un gesto?", "Un movimiento de la cara o del cuerpo", "Muestra lo que siente el personaje."),
        E("¿Por qué es útil notar la voz del personaje?", "Porque muestra cómo se siente", "La voz cambia con la emoción."),
        E("Si un personaje habla bajito y lento, ¿puede estar cansado?", "Sí", "Esa voz suele mostrar cansancio o tristeza."),
    ],
    [
        E("Escena: «Lola grita: ¡Perdí mi gorro!». ¿Qué emoción muestra la voz?", "Preocupación o apuro", "Gritar rápido muestra que algo la inquieta."),
        E("Escena: «Tomás levanta la mano y dice con voz suave: Yo te ayudo». ¿Qué pista de voz hay?", "Voz suave", "Está escrita en la escena."),
        E("Escena: «Lola se sienta en el suelo y habla bajito: Ya no quiero buscar». Escribe una pista y lo que muestra.", "Habla bajito; muestra tristeza o cansancio", "La voz baja indica cómo se siente."),
    ],
    [
        E("Ana dice: «En la escena, el dragón estaba triste». Luis dice: «Estaba triste porque caminaba lento y miraba al suelo». ¿Quién dio una pista?", "Luis", "Luis explica con el gesto y el movimiento."),
        E("Un actor dice «estoy muy feliz» con voz muy baja y cara seria. ¿La voz y el gesto combinan con lo que dice?", "No", "Feliz suele mostrarse con voz y cara alegres."),
    ],
    [
        E("En una escena, A se aleja de B y B se queda quieto con los brazos caídos. ¿Qué pistas de espacio y de gesto hay?", "Espacio: A se aleja; gesto: B con brazos caídos", "Una es dónde se mueven y otra es el cuerpo."),
        E("Elige la mejor frase para explicar una escena: a) «Pasó algo triste.» b) «Ella habló bajito y se sentó, por eso parecía triste.»", "b", "La b cita pistas concretas."),
    ],
    [E("Mira esta escena: «Pedro entra gritando: ¡Llegué tarde! Se agarra la cabeza y corre hasta el centro. Mira a María, que está sentada, y dice bajito: Perdón». Nombra una pista de voz y una de gesto.", "Voz: grita al entrar y luego dice bajito; gesto: se agarra la cabeza", "Las pistas están en la escena escrita.")],
    [
        E("¿Un gesto es un movimiento?", "Sí", "Se hace con la cara o el cuerpo."),
        E("¿Solo importa lo que dicen las palabras en el teatro?", "No", "También importan la voz, el gesto y el espacio."),
        E("Si digo «estaba triste», ¿debo dar una pista?", "Sí", "La pista explica de dónde saqué la idea."),
    ],
    ("Observa y explica una escena. Lee esta escena en voz alta o pídele a un adulto que la lea: «Sofía entra caminando lento. Se sienta en una silla, abraza su mochila y dice bajito: Hoy no quiero jugar. Diego se acerca, se agacha a su lado y le dice con voz suave: Si quieres, nos sentamos juntos». Escribe qué siente cada personaje y una pista de voz, de gesto o de espacio que lo muestra.",
     "Sofía está triste: camina lento, abraza su mochila y habla bajito. Diego quiere ayudarla: se acerca, se agacha a su lado y habla suave.",
     ["dice qué siente cada personaje", "da una pista de voz, gesto o espacio por personaje", "no solo cuenta lo que pasó"], ["respuesta escrita u oral con pistas"], ["resumir sin dar pistas", "inventar datos que la escena no tiene"],
     "Si solo resume, pregunta: ¿cómo hablaba Sofía? ¿Qué hizo Diego con su cuerpo?"),
    "Mira a alguien de tu casa decir «hola» con tres voces distintas y di qué siente en cada una.",
    "Cambia la voz y el espacio de la escena de Sofía para que parezca alegre, y explica qué cambiaste.",
)

reg(
    OA24, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: 5 papelitos para ordenar las acciones.",
    "Aprenderé a ordenar lo que pasa en una escena y a explicar cuál es el conflicto. Sirve para recordar una obra y contarla sin perder lo importante.",
    ["Sé reconocer personajes y sus acciones.", "Sé ordenar una historia con primero, luego y al final."],
    [
        "Una escena tiene personajes que hacen cosas. Esas cosas son las acciones. Para reconstruir una escena, las ordenamos: primero, luego, después y al final. Así recordamos la secuencia sin confundirnos.",
        "En casi todas las escenas hay un conflicto. El conflicto es el problema que los personajes deben resolver. Por ejemplo: una niña quiere el único globo rojo y su amigo también lo quiere. Ese problema mueve la escena, y al final se resuelve o queda abierto.",
        "Para contar una escena, nombra a los personajes, di el conflicto y cuenta las acciones en orden. No hace falta repetir todas las palabras. Es mejor decir lo importante: quién, qué quería, qué problema tuvo y cómo terminó.",
    ],
    [("acción", "lo que hace un personaje"), ("conflicto", "problema que los personajes deben resolver"), ("secuencia", "orden en que pasan las cosas"), ("reconstruir", "volver a armar algo en orden"), ("desenlace", "cómo termina la escena")],
    [
        ("Ordenar acciones", "Acciones desordenadas: a) Rita comparte el globo, b) Rita y Beto quieren el globo rojo, c) Beto propone turnarse. ¿En qué orden pasó?", ["Busco el problema primero.", "Luego busco la idea para resolverlo.", "Termino con el resultado."], "b, c, a."),
        ("Decir el conflicto", "Rita y Beto quieren el único globo rojo. ¿Cuál es el conflicto?", ["Veo quiénes participan.", "Veo qué quiere cada uno.", "Digo el problema."], "Los dos quieren el único globo rojo."),
    ],
    [("Contar todo palabra por palabra.", "Se cree que hay que repetir todo.", "Cuenta quién, qué problema y cómo termina."), ("Confundir el conflicto con el final.", "Se mezcla el problema con la solución.", "Primero di el problema y después cómo se resolvió.")],
    [
        E("Rita guarda el globo en su mochila. ¿Eso es una acción o un conflicto?", "Una acción", "Es algo que hace el personaje."),
        E("Dos niños quieren el mismo columpio. ¿Ese es el conflicto o el desenlace?", "El conflicto", "Es el problema que deben resolver."),
        E("En una secuencia, ¿qué va primero: el problema o la solución?", "El problema", "Primero aparece el problema y luego se resuelve."),
    ],
    [
        E("¿Qué es un conflicto en una escena?", "El problema que deben resolver los personajes", "Mueve la historia hacia adelante."),
        E("¿Para qué sirve ordenar las acciones?", "Para contar la escena sin confundirse", "La secuencia muestra qué pasó antes y después."),
        E("¿Qué es el desenlace?", "Cómo termina la escena", "Es el final del conflicto."),
    ],
    [
        E("Ordena: a) Lía le presta la pelota, b) Mario pierde su pelota, c) Mario juega feliz. ¿En qué orden?", "b, a, c", "Primero pierde, luego recibe ayuda, al final juega."),
        E("Escena: «Tina no puede abrir la puerta. Pide ayuda a Juan. Juan empuja y la puerta se abre». ¿Cuál es el conflicto?", "Tina no puede abrir la puerta", "Ese es el problema inicial."),
        E("En la escena anterior, ¿cuál es el desenlace?", "La puerta se abre", "Es como termina el problema."),
    ],
    [
        E("Eva cuenta una escena: «Ella entró, dijo hola, se sentó, y luego…». Eva no dijo el problema. ¿Qué falta en su relato?", "El conflicto", "Sin el problema, no se entiende la escena."),
        E("Escena: «Ana y Pía quieren el mismo libro. Deciden leerlo juntas». ¿El conflicto se resolvió?", "Sí", "Encontraron una forma de compartir."),
    ],
    [
        E("Escena A: «Un niño no encuentra su abrigo y busca por todo el escenario hasta que lo halla bajo una silla». Escena B: «Dos amigos pelean por un juguete y no se ponen de acuerdo». ¿Cuál termina sin resolverse?", "La B", "En la B no se dice que lo resolvieron."),
        E("Ordena la secuencia: a) Rosa pide ayuda, b) Rosa se cae con su bolso, c) un vecino la ayuda a levantarse, d) Rosa agradece.", "b, a, c, d", "Cada acción lleva a la siguiente."),
    ],
    [E("Cuenta en una frase esta escena: «Lalo quiere subir a un árbol pero tiene miedo. Su prima Eli le dice que sube con él, paso a paso. Suben los dos y se ríen». Di quién, el conflicto y el final.", "Lalo tiene miedo de subir al árbol; Eli lo acompaña y suben juntos", "Incluye personaje, conflicto y final.")],
    [
        E("¿Una acción es lo que hace un personaje?", "Sí", "Acción es algo que se hace."),
        E("¿El conflicto es siempre un final feliz?", "No", "Es el problema, no el final."),
        E("¿Primero se cuenta el desenlace o el problema?", "El problema", "El orden ayuda a entender."),
    ],
    ("Reconstruye una escena con tus palabras. Lee: «Camila lleva una caja muy grande y no puede pasar por la puerta. Tomás ve que la caja se atora. Los dos giran la caja de lado y logran pasar. Se ríen y cierran la puerta». Escribe cuatro acciones en orden y di cuál es el conflicto y cómo se resolvió.",
     "1) Camila lleva la caja. 2) La caja se atora. 3) Tomás la ayuda y giran la caja. 4) Pasan y se ríen. Conflicto: la caja no pasaba por la puerta. Se resolvió girando la caja de lado.",
     ["ordena al menos cuatro acciones", "nombra el conflicto", "explica cómo se resolvió"], ["lista escrita u oral en orden"], ["mezclar el orden", "no decir el problema"],
     "Si desordena, pide que use primero, luego, después y al final."),
    "Cuenta una escena corta de una película o cuento que conozcas con inicio, problema y final.",
    "Cambia el desenlace de la escena de Camila y explica qué otra solución habría.",
)

reg(
    OA24, 4,
    "Este cuaderno, lápiz y espacio libre en casa. Se necesita un adulto o un muñeco como compañero de juego.",
    "Aprenderé a mostrar una misma acción de distintas maneras con la voz y el cuerpo. Sirve para actuar con más imaginación y para entender mejor a un personaje.",
    ["Sé que la voz y el gesto muestran emociones.", "Sé moverme con cuidado en un espacio libre."],
    [
        "En el teatro, una misma acción se puede mostrar de muchas formas. Caminar puede ser caminar contento, cansado o con miedo. Lo que cambia es el ritmo, el tamaño del movimiento, la voz y la cara. A eso lo llamamos explorar de manera expresiva.",
        "Para explorar, haz una prueba con tu cuerpo. Primero camina normal. Luego camina más lento, con la cabeza baja y hombros caídos: se ve cansado. Después camina con pasos grandes, cabeza arriba y una sonrisa: se ve contento. Fíjate qué cambió y qué se entiende.",
        "Explorar también es probar y elegir. No hay una sola forma correcta, pero sí una que cuenta mejor la escena. Si el personaje busca un tesoro con miedo, los pasos pequeños y la mirada atenta lo muestran bien. Siempre actúa con cuidado, sin empujar ni golpear.",
    ],
    [("expresivo", "que muestra lo que siente un personaje"), ("ritmo", "qué tan rápido o lento algo se mueve"), ("explorar", "probar distintas formas"), ("movimiento", "cambio de lugar o de posición del cuerpo"), ("elegir", "decidir cuál opción se queda")],
    [
        ("Cambiar el ritmo", "El personaje camina con mucho sueño. ¿Qué ritmo y gesto eliges?", ["Pienso cómo se mueve alguien con sueño.", "Elijo pasos lentos.", "Agrego bostezo y hombros caídos."], "Pasos lentos, hombros caídos y un bostezo."),
        ("Cambiar el tamaño del movimiento", "El personaje tiene miedo de hacer ruido. ¿Cómo mueves tu cuerpo?", ["Pienso en alguien que no quiere que lo oigan.", "Hago pasos pequeños.", "Miro alrededor despacio."], "Pasos pequeños, de puntillas y mirando alrededor."),
    ],
    [("Hacer siempre el mismo movimiento.", "Se cree que solo hay una forma.", "Prueba tres formas y elige la mejor."), ("Actuar muy fuerte y chocar con otros.", "Se olvida cuidar el espacio.", "Mueve tu cuerpo sin tocar a nadie.")],
    [
        E("Caminar con pasos grandes, cabeza arriba y sonrisa, ¿muestra alegría o cansancio?", "Alegría", "Los pasos grandes y la sonrisa son alegres."),
        E("Pasos muy lentos y hombros caídos, ¿muestran energía o cansancio?", "Cansancio", "El ritmo lento y los hombros caídos indican cansancio."),
        E("Al explorar un movimiento, ¿pruebo una forma o varias?", "Varias", "Explorar es probar distintas formas."),
    ],
    [
        E("¿Qué cambia cuando camino contento y cuando camino con miedo?", "El ritmo, el tamaño del paso, la voz y la cara", "Esos elementos muestran la emoción."),
        E("¿Por qué no existe una única forma de caminar en el teatro?", "Porque depende de cómo se siente el personaje", "La emoción cambia el movimiento."),
        E("¿Qué debo cuidar al actuar con un compañero?", "No empujar ni golpear", "El juego debe ser seguro."),
    ],
    [
        E("Escribe cómo mostrarías con el cuerpo a alguien que lleva una bolsa muy pesada.", "Pasos lentos, cuerpo inclinado y brazos tensos", "Así se ve el peso."),
        E("Un personaje está muy enojado y camina. Elige: a) pasos suaves y sonrisa, b) pasos fuertes y cara seria.", "b", "Los pasos fuertes y la cara seria muestran enojo."),
        E("Un personaje descubre un regalo. Escribe un gesto de la cara y uno de las manos.", "Cara: ojos abiertos y sonrisa; manos: aplauden o se levantan", "Son gestos que muestran sorpresa y alegría."),
    ],
    [
        E("Dos niños muestran miedo. Nico se agacha y mira por los lados. Eli corre y grita fuerte. ¿Quién muestra más cuidado para no hacer ruido?", "Nico", "Eli hace mucho ruido corriendo y gritando."),
        E("María prueba tres formas de abrir una puerta imaginaria: despacio, de golpe y con cuidado. ¿Probó sola una forma o exploró varias?", "Exploró varias", "Probó tres formas distintas."),
    ],
    [
        E("La acción es «subir una escalera». ¿Cómo la mostrarías si el personaje está muy cansado? Elige: a) saltando de dos en dos, b) paso a paso, agarrándose del pasamanos.", "b", "El paso lento muestra cansancio."),
        E("Escena: un niño busca a su gato en la oscuridad. Elige el movimiento más claro: a) correr riendo, b) caminar despacio con las manos adelante.", "b", "Mostrar que no se ve bien en la oscuridad."),
    ],
    [E("Mira esta acción: «abrir una caja que no sabes qué tiene». Escribe dos formas distintas de mostrarla con el cuerpo, una con curiosidad y otra con miedo.", "Curiosidad: la abro rápido y me asomo; miedo: la abro de a poco, con los ojos casi cerrados", "Cada forma muestra una emoción diferente.")],
    [
        E("¿Explorar es probar distintas formas de hacer algo?", "Sí", "Se compara cuál cuenta mejor."),
        E("¿Un movimiento puede cambiar si cambia la emoción?", "Sí", "La emoción cambia el cuerpo."),
        E("¿Debo empujar a mi compañero para actuar mejor?", "No", "Se actúa con cuidado."),
    ],
    ("Explora una acción con tu cuerpo. La acción es «tomar un vaso de agua». Haz tres versiones con un adulto como público: 1) con mucha sed, 2) con mucho cuidado porque el vaso está lleno, 3) con enojo. Pídele que adivine la emoción y anota cuál fue más clara y por qué.",
     "Con mucha sed tomé el vaso rápido y bebí de un trago. Con cuidado lo agarré con las dos manos y caminé lento. Con enojo lo puse de golpe en la mesa. La más clara fue la del cuidado, porque mis pasos lentos se notaron.",
     ["prueba tres versiones distintas", "cambia ritmo, tamaño o gesto", "explica cuál fue más clara"], ["demostración ante un adulto", "nota escrita u oral"], ["repetir el mismo movimiento", "actuar sin cuidar el espacio"],
     "Si repite lo mismo, pregunta qué parte del cuerpo cambiaría: pasos, manos o cara."),
    "Camina por tu pieza como si estuvieras contento, enojado y dormido, y di qué cambió.",
    "Elige una acción cotidiana y muéstrala con cuatro emociones diferentes.",
)

reg(
    OA24, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: un adulto con quien conversar.",
    "Aprenderé a dar mi opinión sobre una decisión de la obra, usando pruebas. Sirve para conversar como público y para explicar por qué algo me gustó o no.",
    ["Sé que la voz, el gesto y el espacio cuentan cosas.", "Sé decir mi opinión con respeto."],
    [
        "Cuando termina una obra, el público conversa. Una opinión dice qué pienso, pero se vuelve fuerte cuando la apoyo con una evidencia, es decir, algo que vi o escuché en la obra. Por ejemplo: «Me gustó cuando el lobo habló bajito, porque dio más misterio».",
        "Los actores y directores toman decisiones: qué voz usar, dónde pararse, qué gesto hacer. Como público, podemos opinar sobre una decisión. Para hacerlo, seguimos tres pasos: digo qué decisión miré, digo qué pienso y doy una razón con evidencia.",
        "También escuchamos las opiniones de otros. Dos personas pueden pensar distinto y las dos pueden tener razón, si explican con lo que vieron. Decir «no me gustó» sin razón no ayuda. Decir «no me gustó porque no escuché la voz» sí ayuda.",
    ],
    [("opinión", "lo que pienso sobre algo"), ("evidencia", "algo que vi o escuché que apoya mi opinión"), ("decisión escénica", "elección que hacen los actores al representar"), ("razón", "motivo de lo que pienso"), ("respetar", "escuchar sin burlarse")],
    [
        ("Opinión con evidencia", "En una obra, el lobo habló bajito y caminó despacio. A ti te dio misterio. ¿Cómo lo dices?", ["Digo qué decisión miré.", "Digo qué pienso.", "Doy la razón con evidencia."], "Me gustó que el lobo hablara bajito porque dio misterio."),
        ("Opinión sin evidencia", "Un compañero dice: «Fue aburrida». ¿Cómo lo ayudas a mejorar su opinión?", ["Le pregunto qué parte vio.", "Le pido una razón.", "Le ayudo a decirlo con evidencia."], "«Me aburrí cuando la escena fue muy larga y nadie se movió»."),
    ],
    [("Decir solo «me gustó» o «no me gustó».", "Falta la razón.", "Agrega «porque…» con algo que viste."), ("Criticar a las personas, no la decisión.", "Se confunde opinar con burlarse.", "Habla de la voz, del gesto o del espacio, no de cómo es la persona.")],
    [
        E("Opinión: «La voz del dragón me dio miedo porque era muy grave». ¿Incluye una razón?", "Sí", "Dice por qué lo pensó."),
        E("«Me gustó» solo, ¿es una opinión con razón o sin razón?", "Sin razón", "No dice por qué."),
        E("¿Una evidencia es algo que vi o algo que imagino sin haber visto?", "Algo que vi o escuché", "Debe venir de la obra."),
    ],
    [
        E("¿Para qué sirve dar una razón en una opinión?", "Para que otros entiendan por qué lo pienso", "La razón apoya la idea."),
        E("Dos personas piensan distinto sobre una escena y las dos explican con lo que vieron. ¿Pueden tener razón?", "Sí", "Cada una apoya su idea con evidencia."),
        E("¿Opinar sobre una decisión escénica es hablar de la voz, el gesto o el espacio?", "Sí", "Esas son decisiones de la obra."),
    ],
    [
        E("Completa: «Me gustó que el hada ______ porque ______». Escribe una idea con una decisión y una razón. Ejemplo de decisión: volar con los brazos abiertos.", "Por ejemplo: volara con los brazos abiertos; se veía libre", "Une decisión y razón."),
        E("En una obra, el rey entró lento y habló fuerte. Escribe una opinión con razón sobre cómo se vio.", "Por ejemplo: Se vio importante porque entró lento y habló fuerte", "Usa evidencia de la escena."),
        E("Cambia esta opinión sin razón: «No me gustó el final». Agrega una razón posible.", "Por ejemplo: No me gustó porque terminó muy rápido", "Agrega la causa."),
    ],
    [
        E("Sara: «Me gustó porque la niña habló bajito y se acercó al perro». Pepe: «Me gustó porque sí». ¿Quién dio mejor evidencia?", "Sara", "Sara cuenta lo que vio."),
        E("Mateo dice: «El actor era feo». ¿Habla de una decisión de la obra o de la persona?", "De la persona", "No opina sobre voz, gesto o espacio."),
    ],
    [
        E("Opinión A: «El final fue triste porque la niña bajó la cabeza y no habló». Opinión B: «El final fue triste». ¿Cuál se apoya más en evidencia?", "La A", "La A cuenta qué hizo la niña."),
        E("Escoge la opinión respetuosa y con razón: a) «No me gustó, qué tontos», b) «No me gustó porque hablaron muy bajito y no los escuché».", "b", "La b explica sin ofender."),
    ],
    [E("Después de ver una obra, un amigo dice que le gustó la escena del bosque. Tú viste que los actores usaron una luz verde y hablaron en susurros. Escribe una opinión sobre esa decisión con una razón.", "Por ejemplo: Me gustó la luz verde y los susurros porque dieron misterio", "Une decisión, opinión y razón.")],
    [
        E("¿Una buena opinión lleva una razón?", "Sí", "La razón explica la idea."),
        E("¿Puedo opinar de lo que vi sin burlarme de las personas?", "Sí", "Se puede opinar con respeto."),
        E("¿Debo usar algo que vi o escuché como evidencia?", "Sí", "La evidencia viene de la obra."),
    ],
    ("Conversa como público. Piensa en una obra, película o función de títeres que hayas visto. Si no recuerdas ninguna, usa esta: «En una obra, un oso entra lento, habla con voz grave y se sienta solo en un banco. Después una niña se acerca y le ofrece pan». Escribe o di tres cosas: una decisión que miraste, tu opinión y una razón con evidencia. Escucha también una opinión de otra persona.",
     "Decisión: el oso entra lento. Opinión: me pareció triste. Razón: porque se sienta solo y habla con voz grave. Mi hermana dijo que le pareció tierno porque la niña le ofrece pan.",
     ["nombra una decisión de la obra", "da una opinión con una razón basada en lo visto", "escucha una opinión distinta con respeto"], ["opinión escrita u oral", "comentario sobre otra opinión"], ["decir solo «me gustó»", "criticar a la persona"],
     "Si dice solo «me gustó», pregunta qué vio u oyó que se lo hizo pensar."),
    "Cuenta a alguien de tu casa qué parte de una obra o película te gustó más y por qué.",
    "Compara dos decisiones de una misma escena y di cuál contó mejor la historia, con evidencia.",
)

# ================================================================ OA 25
reg(
    OA25, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: un adulto con quien conversar.",
    "Aprenderé a aportar ideas que tienen relación con el tema de la conversación. Sirve para que todos se entiendan y la conversación no se pierda.",
    ["Sé esperar mi turno.", "Sé escuchar a quien habla."],
    [
        "En una conversación, el tema es de lo que estamos hablando. Si el tema es «mascotas», lo que digo debe tener relación con mascotas. El tema puede venir de un texto que leímos o escuchamos en clases, o de algo que nos interesa. A esto le llamamos mantener el foco. Cuando mi idea se sale del tema, los demás se confunden.",
        "Para aportar, escucho lo que dijo la persona anterior y busco una relación. Puedo agregar algo parecido, hacer una pregunta o dar un ejemplo. Por ejemplo, si alguien dice «mi perro come pan», yo puedo decir «mi gato come pescado» porque sigo hablando de lo que comen las mascotas.",
        "Si quiero cambiar de tema, puedo decirlo con cortesía: «¿Podemos hablar ahora de…?». Así todos saben que cambiamos. Un turno es mi momento de hablar. Respetar los turnos es esperar a que termine el que habla, sin interrumpir.",
    ],
    [("tema", "de qué se está hablando"), ("foco", "mantener la atención en el tema"), ("turno", "momento en que me toca hablar"), ("aportar", "agregar una idea al tema"), ("relacionar", "unir mi idea con la de otro")],
    [
        ("Aportar al tema", "Tema: mascotas. Luis dice: «Mi perro come pan». ¿Qué aporte tiene relación?", ["Veo el tema: mascotas.", "Pienso en algo parecido.", "Lo digo después de escuchar."], "Mi gato come pescado."),
        ("Detectar que se salió del tema", "Tema: el recreo. Ana dice: «Jugamos a la pelota». Beto dice: «Ayer vi una película de dinosaurios». ¿Beto sigue el tema?", ["Reviso el tema: el recreo.", "Veo que Beto habla de una película.", "Concluyo que no hay relación."], "No, Beto se salió del tema."),
    ],
    [("Hablar de lo que quiero, sin escuchar.", "Se piensa solo en la propia idea.", "Escucha y relaciona tu idea con la anterior."), ("Interrumpir para no olvidar mi idea.", "Se tiene miedo de olvidarla.", "Guárdala en tu cabeza y espera tu turno.")],
    [
        E("Tema: frutas. Alguien dice «me gustan las manzanas». ¿Qué aporte es del tema: «a mí las peras» o «mi bicicleta es roja»?", "A mí las peras", "Las peras son frutas."),
        E("Tema: el parque. ¿Qué frase sigue el tema: «Hay columpios nuevos» o «Hoy hay prueba»?", "Hay columpios nuevos", "Los columpios están en el parque."),
        E("Para respetar el turno, ¿espero a que termine el otro o hablo al mismo tiempo?", "Espero a que termine", "Así todos pueden escuchar."),
    ],
    [
        E("¿Qué es el tema de una conversación?", "De qué se está hablando", "Es lo que une las ideas."),
        E("¿Por qué conviene escuchar antes de hablar?", "Para relacionar mi idea con la del otro", "Así mi aporte sigue el tema."),
        E("¿Qué hago si quiero cambiar de tema?", "Lo pido con cortesía", "Así todos saben que cambiamos."),
    ],
    [
        E("Tema: los juegos del patio. Luisa dice: «Me gusta la cuerda». Escribe un aporte que siga el tema.", "Por ejemplo: A mí me gusta el luche", "Habla de otro juego del patio."),
        E("Tema: el verano. Pedro dice: «Fui a la playa». Escribe una pregunta que siga el tema.", "Por ejemplo: ¿Qué hiciste en la playa?", "Pregunta sobre lo que dijo."),
        E("En clases escucharon el cuento «Los tres cerditos». Tema: el cuento. Marta dice: «El cerdito de ladrillos fue el más cuidadoso». Escribe una idea relacionada con el cuento.", "Por ejemplo: A mí me gustó que el lobo no pudo entrar a la casa de ladrillos", "Sigue hablando del cuento."),
    ],
    [
        E("Tema: los animales del campo. Diego dice: «Las vacas dan leche». Sofía: «Mi abuela tiene un campo». Julia: «Las gallinas ponen huevos». ¿Quién siguió mejor el tema?", "Julia", "Julia habla de animales."),
        E("Tema: el cumpleaños. Lola habla de la torta. Tito interrumpe para contar un chiste. ¿Respetó el turno?", "No", "Interrumpió a Lola."),
    ],
    [
        E("Conversación: Ana: «Mi libro favorito es de piratas». Beto: «Mi libro favorito es de piratas también». Carlos: «Hoy me duele un diente». ¿Cuál de los tres aportes se sale del tema?", "El de Carlos", "No habla de libros."),
        E("Tema: la escuela. Nina quiere hablar de su mascota. ¿Qué frase cortés puede usar? a) «¡Hablemos de mi perro!» b) «¿Podemos hablar de mi perro ahora?»", "b", "La b pide el cambio con cortesía."),
    ],
    [E("Tema: nuestro juguete favorito. Rosa dice: «Me gusta mi muñeca porque tiene vestido azul». Escribe un aporte que se relacione con lo que dijo.", "Por ejemplo: A mí me gusta mi auto porque tiene luces", "Habla del juguete favorito y se une a lo dicho.")],
    [
        E("¿Mantener el foco es hablar del tema?", "Sí", "El foco es el tema de la conversación."),
        E("¿Debo escuchar a la persona antes de hablar?", "Sí", "Así relaciono mi idea."),
        E("¿Está bien interrumpir si tengo una idea?", "No", "Se espera el turno."),
    ],
    ("Conversa con un adulto 2 minutos sobre el tema «un lugar que me gusta». Cada uno habla por turnos y debe aportar una idea relacionada con lo que dijo el otro. Antes de hablar, escucha. Anota o recuerda dos aportes tuyos que se relacionaron con el tema.",
     "Tema: un lugar que me gusta. Adulto: La plaza, porque hay árboles. Yo: A mí me gusta la plaza porque hay un columpio. Adulto: ¿Y con quién vas? Yo: Con mi hermano. Mis dos aportes se relacionaron con la plaza.",
     ["aporta ideas relacionadas con el tema", "espera su turno", "escucha antes de responder"], ["adulto comenta si se mantuvo el foco", "dos aportes recordados o anotados"], ["salirse del tema", "interrumpir"],
     "Si se sale del tema, pregunta de qué hablaba la otra persona y ayúdale a unir su idea."),
    "Conversa en la mesa sobre un tema que elija tu familia y cuida el foco.",
    "Ayuda a mantener el foco en una conversación de tres personas y avisa con cortesía si se aleja.",
)

reg(
    OA25, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: un adulto con quien conversar.",
    "Aprenderé a decir lo que pienso y a dar una razón. Sirve para que los demás entiendan mis ideas y para respetar que otros piensen distinto.",
    ["Sé mantener el tema.", "Sé esperar mi turno."],
    [
        "Una opinión es lo que pienso o siento sobre algo, como «me gusta el verano». Una razón explica por qué lo pienso, como «porque puedo ir a la playa». Cuando agrego «porque…» mi opinión se entiende mejor.",
        "Para dar una opinión, uso frases como «yo pienso que…» o «a mí me parece que…». Después digo «porque…» y escribo una razón. Por ejemplo: «Yo pienso que leer es entretenido porque descubro historias». Así los demás saben qué pienso y por qué.",
        "No todas las personas piensan igual. Si alguien piensa distinto, no es una falta de respeto: es otra opinión con otra razón. Puedo decir «yo pienso distinto porque…». Mientras hablamos sin burlarnos, la conversación sigue siendo respetuosa.",
    ],
    [("opinión", "lo que pienso sobre algo"), ("razón", "motivo por el que lo pienso"), ("porque", "palabra que une la opinión con la razón"), ("desacuerdo", "cuando pienso distinto de otro"), ("respetuoso", "que no se burla ni ofende")],
    [
        ("Opinión con razón", "¿Te gusta jugar al aire libre? Da tu opinión con razón.", ["Digo «yo pienso que…»", "Uso «porque…»", "Escribo una razón verdadera."], "Yo pienso que es entretenido jugar al aire libre porque puedo correr."),
        ("Opinión distinta, con respeto", "Tu amigo dice: «El invierno es lo mejor porque llueve». A ti no te gusta. ¿Cómo respondes?", ["No me burlo.", "Digo que pienso distinto.", "Doy mi razón."], "Yo pienso distinto, porque con la lluvia no puedo salir a jugar."),
    ],
    [("Decir solo «me gusta» o «no me gusta».", "Falta la razón.", "Agrega «porque…»"), ("Reírse de una opinión distinta.", "Se cree que pensar distinto es un error.", "Escucha y responde con respeto.")],
    [
        E("«Me gusta el helado porque está frío.» ¿La frase tiene razón?", "Sí", "Después de porque está la razón."),
        E("«Me gusta el helado.» ¿Tiene razón?", "No", "No dice por qué."),
        E("¿Qué palabra une opinión y razón: «porque» o «también»?", "Porque", "Indica el motivo de lo que pienso."),
    ],
    [
        E("En Lenguaje: ¿Qué es una opinión?", "Lo que pienso sobre algo", "Es una idea personal."),
        E("¿Por qué agrego una razón a mi opinión?", "Para que los demás entiendan mi idea", "La razón la explica."),
        E("Si otra persona piensa distinto, ¿pasa algo malo?", "No", "Es otra opinión con otra razón."),
    ],
    [
        E("Completa: «Yo pienso que los gatos son lindos porque _____». Escribe una razón.", "Por ejemplo: son suaves", "La razón explica la opinión."),
        E("Tu amigo dice «Me gusta el verano porque hay sol». Tú piensas distinto. Escribe cómo respondes.", "Por ejemplo: Yo pienso distinto, porque con tanto sol me da calor", "Dice desacuerdo con razón."),
        E("Escribe una opinión con razón sobre tu fruta favorita.", "Por ejemplo: Me gusta la sandía porque es jugosa", "Une opinión y razón."),
    ],
    [
        E("Leo dice: «El recreo es lo mejor, porque puedo jugar». Ema dice: «El recreo es lo mejor». ¿Quién explicó mejor?", "Leo", "Leo agregó una razón."),
        E("Mati dice «Pienso distinto, porque…» y escucha. Pepe se ríe de la opinión de Mati. ¿Quién fue respetuoso?", "Mati", "Mati no se burló."),
    ],
    [
        E("Opinión: «Me gusta el parque porque el lunes tengo prueba». ¿La razón explica por qué le gusta el parque?", "No", "La prueba del lunes no tiene relación con el parque."),
        E("Ordena las partes para formar una opinión con razón: a) porque puedo ver amigos, b) Yo pienso que ir a la escuela es bueno.", "b, a", "Primero la opinión y luego la razón."),
    ],
    [E("En clase preguntan: «¿Prefieres leer o dibujar?». Escribe tu respuesta con una opinión y una razón.", "Por ejemplo: Prefiero dibujar porque puedo inventar personajes", "Une opinión y razón con porque.")],
    [
        E("¿Cuando opino debo decir una razón?", "Sí", "Así me entienden mejor."),
        E("¿Puedo pensar distinto que mi amigo?", "Sí", "Cada uno tiene su opinión."),
        E("¿Está bien burlarse de una opinión?", "No", "Se debe respetar."),
    ],
    ("Opina con razón. Responde en tu hoja o en voz alta a tres preguntas: 1) ¿Prefieres el día o la noche? 2) ¿Te gusta más jugar solo o acompañado? 3) ¿Cuál es tu juego favorito? Cada respuesta debe tener «yo pienso que…» y «porque…». Luego pídele a un adulto su opinión y respóndele con respeto si piensan distinto.",
     "1) Yo pienso que el día es mejor porque hay luz para jugar. 2) Yo pienso que es mejor acompañado porque me río más. 3) Mi juego favorito es el luche porque salto.",
     ["responde tres preguntas", "cada respuesta tiene opinión y razón", "responde con respeto a una opinión distinta"], ["respuestas escritas u orales", "adulto escucha"], ["no dar razón", "burlarse"],
     "Si falta razón, pregunta «¿por qué piensas eso?» y pide que lo diga con porque."),
    "Di tu opinión sobre la comida de hoy y por qué.",
    "Escucha dos opiniones distintas sobre el mismo tema y explica en qué razones se diferencian.",
)

reg(
    OA25, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: un adulto que te cuente algo para hacerle preguntas.",
    "Aprenderé a hacer preguntas que ayudan a comprender lo que otra persona dijo. Sirve para aclarar dudas y para que el que habla se sienta escuchado.",
    ["Sé mantener el tema.", "Sé dar una opinión con razón."],
    [
        "Cuando no entendemos algo, hacemos una pregunta. Una pregunta de aclaración nos ayuda a entender mejor. Por ejemplo, si alguien dice «fui a un lugar grande», podemos preguntar: «¿Cómo era ese lugar?». Así completamos la idea.",
        "Hay palabras para empezar preguntas: ¿qué?, ¿quién?, ¿dónde?, ¿cuándo?, ¿cómo? y ¿por qué? Una buena pregunta se relaciona con lo que se dijo. No es una pregunta para llevarse la conversación a otro lado ni para molestar.",
        "También podemos pedir que repitan con otras palabras: «¿Puedes explicarlo de nuevo?». Después de escuchar la respuesta, podemos decir «gracias, ahora entendí». Preguntar con respeto muestra interés y ayuda a todos a aprender.",
    ],
    [("pregunta", "frase con la que pido información"), ("aclarar", "hacer más claro algo"), ("duda", "cuando no entiendo bien"), ("interés", "ganas de saber más"), ("repetir", "decir otra vez")],
    [
        ("Hacer una pregunta de aclaración", "Marta dice: «Fui a un lugar muy grande». No sabes qué lugar era. ¿Qué preguntas?", ["Escucho qué falta.", "Elijo una palabra para preguntar.", "Hago la pregunta."], "¿Qué lugar era?"),
        ("Pedir que repitan", "El profesor dice algo muy rápido y no lo entendiste. ¿Qué dices?", ["No me quedo callado.", "Pido con cortesía.", "Espero la respuesta."], "¿Puede repetirlo, por favor?"),
    ],
    [("Preguntar algo que no tiene relación.", "Se quiere cambiar de tema.", "Pregunta sobre lo que dijo la persona."), ("Quedarme con la duda.", "Se siente vergüenza.", "Preguntar ayuda a todos.")],
    [
        E("Alguien dice: «Tengo un perro». ¿Qué pregunta ayuda: «¿Cómo se llama?» o «¿Cuánto es 5 + 5?»", "¿Cómo se llama?", "Se relaciona con lo que dijo."),
        E("¿Con qué palabra preguntas por un lugar: dónde o quién?", "Dónde", "Dónde se usa para lugares."),
        E("Si no entendí algo, ¿pregunto o me quedo con la duda?", "Pregunto", "Preguntar ayuda a entender."),
    ],
    [
        E("¿Para qué sirve una pregunta de aclaración?", "Para entender mejor lo que dijo otra persona", "Completa la información."),
        E("¿Qué debe tener una buena pregunta?", "Relación con lo que se dijo", "Sigue el tema de la conversación."),
        E("¿Por qué es respetuoso preguntar con interés?", "Porque muestra que escucho", "El que habla se siente escuchado."),
    ],
    [
        E("Eva dice: «Ayer vi algo hermoso». Escribe una pregunta para entender más.", "Por ejemplo: ¿Qué viste?", "Pide información que falta."),
        E("Tomás dice: «Mi hermana vive lejos». Escribe una pregunta con dónde.", "Por ejemplo: ¿Dónde vive tu hermana?", "Usa la palabra pedida."),
        E("Rita dice: «Hice un dibujo». Escribe una pregunta con cómo.", "Por ejemplo: ¿Cómo es tu dibujo?", "Usa la palabra pedida."),
    ],
    [
        E("Lalo dice: «Fui al cumpleaños de Pepe». Ana pregunta: «¿Qué comimos ayer en la escuela?». ¿La pregunta de Ana aclara lo que dijo Lalo?", "No", "No tiene relación con lo que dijo Lalo."),
        E("Sofi dice: «Me gusta mi tía». Mario pregunta: «¿Por qué te gusta?». ¿La pregunta ayuda a comprender?", "Sí", "Pide la razón de lo que dijo Sofi."),
    ],
    [
        E("Dani dice: «Compré una cosa rica». Tres preguntas: a) «¿Qué compraste?» b) «¿Tienes sed?» c) «¿Dónde vives?». ¿Cuál aclara?", "a", "La a pide el dato que falta."),
        E("Ordena para formar una pregunta cortés: a) por favor, b) ¿Puedes repetir eso, c) ?", "b, a, c", "Se arma ¿Puedes repetir eso por favor?"),
    ],
    [E("Una compañera cuenta: «El sábado fui a un lugar con muchos animales». Escribe dos preguntas que ayuden a entender mejor su relato.", "Por ejemplo: ¿Qué animales viste? ¿Con quién fuiste?", "Cada pregunta busca un dato nuevo.")],
    [
        E("¿Preguntar es una forma de interesarse?", "Sí", "Muestra que escucho."),
        E("¿Cualquier pregunta aclara lo dicho?", "No", "Debe relacionarse con lo dicho."),
        E("¿Puedo pedir que repitan lo que no entendí?", "Sí", "Es una forma cortés de aclarar."),
    ],
    ("Haz preguntas de aclaración. Un adulto te contará esto en dos frases: «El domingo fuimos a un lugar nuevo. Había algo que no conocía». Escucha y haz cuatro preguntas que usen qué, dónde, cómo o por qué. Después di qué entendiste mejor con las respuestas.",
     "¿Qué lugar era? ¿Dónde está? ¿Cómo era ese lugar? ¿Por qué no lo conocías? Entendí que era un parque nuevo con una torre.",
     ["hace cuatro preguntas que aclaran", "las preguntas se relacionan con lo dicho", "escucha las respuestas"], ["preguntas dichas o escritas", "explicación de lo que entendió"], ["preguntas sin relación", "interrumpir al que habla"],
     "Si la pregunta no se relaciona, pide que mire qué dato falta en lo que dijo el adulto."),
    "Haz una pregunta de aclaración a alguien de tu casa sobre algo que contó.",
    "Haz preguntas a dos personas distintas sobre el mismo tema y compara qué aprendiste.",
)

reg(
    OA25, 4,
    "Este cuaderno, lápiz y una hoja. Un adulto que cuente una anécdota breve.",
    "Aprenderé a mostrar que escucho, retomando lo que dijo otra persona antes de responder. Sirve para que el otro sienta que le prestamos atención.",
    ["Sé esperar mi turno.", "Sé hacer una pregunta para aclarar."],
    [
        "Escuchar bien no es solo estar callado. Escuchar de forma visible es mostrar con el cuerpo y con las palabras que presto atención. Miro a quien habla, no hago otra cosa y, si es cómodo, asiento con la cabeza. Si mirar a los ojos me incomoda, puedo mirar su cara o lo que muestra y escuchar con atención.",
        "Antes de responder, puedo retomar lo que dijo la otra persona. Retomar es repetir con mis palabras una parte de lo que escuché. Por ejemplo: «Dijiste que tu perro se perdió y lo encontraron». Después agrego mi respuesta: «¡Qué alegría que apareció!».",
        "Retomar ayuda a comprobar si entendí. Si me equivoco, la otra persona puede corregirme. Para empezar puedo decir «Entendí que…» o «Dijiste que…». Con esa frase muestro interés y evito malentendidos.",
    ],
    [("retomar", "repetir con mis palabras lo que escuché"), ("atención", "ganas de escuchar con cuidado"), ("mirar", "dirigir los ojos hacia quien habla"), ("malentendido", "cuando entendemos algo distinto"), ("comprobar", "verificar si algo es correcto")],
    [
        ("Retomar y responder", "Luz dice: «Mi gato se escondió y lo encontré bajo la cama». ¿Cómo retomas y respondes?", ["Retomo con «dijiste que…»", "Repito lo importante.", "Respondo con mi reacción."], "Dijiste que tu gato se escondió y lo encontraste bajo la cama. ¡Qué bueno que apareció!"),
        ("Mostrar que escucho con el cuerpo", "Un compañero te cuenta algo importante. ¿Qué haces con el cuerpo?", ["Lo miro.", "Dejo mi lápiz.", "Asiento con la cabeza."], "Lo miro, dejo mi lápiz y asiento con la cabeza."),
    ],
    [("Responder algo que no tiene que ver.", "No se escuchó lo dicho.", "Retoma una parte antes de responder."), ("Mirar el celular mientras otro habla.", "Se distrae.", "Mira a quien habla.")],
    [
        E("Para escuchar bien, ¿miro a quien habla o miro por la ventana?", "Miro a quien habla", "Así muestro atención."),
        E("¿Qué frase retoma: «Dijiste que fuiste al parque» o «Hoy estoy cansado»?", "Dijiste que fuiste al parque", "Repite lo que el otro dijo."),
        E("¿Retomar es repetir con mis palabras o inventar algo?", "Repetir con mis palabras", "Muestro que entendí."),
    ],
    [
        E("¿Por qué retomar antes de responder?", "Para mostrar que escuché y comprobar que entendí", "Ayuda a evitar malentendidos."),
        E("Si me equivoco al retomar, ¿qué puede pasar?", "La otra persona me corrige", "Así aclaramos el malentendido."),
        E("¿Escuchar es solo estar callado?", "No", "También se mira y se muestra atención."),
    ],
    [
        E("Pablo dice: «Mi abuelo me enseñó a andar en bicicleta». Escribe cómo retomas con «Dijiste que…».", "Dijiste que tu abuelo te enseñó a andar en bicicleta", "Repite lo central."),
        E("Rosa dice: «Hoy aprendí a nadar». Escribe una respuesta que retome y reaccione.", "Por ejemplo: Entendí que hoy aprendiste a nadar. ¡Qué bien!", "Retoma y responde."),
        E("Un compañero cuenta algo triste. Escribe dos acciones de tu cuerpo para mostrar atención.", "Por ejemplo: lo miro y no hablo mientras cuenta", "Son signos de escucha."),
    ],
    [
        E("Ema dice: «Perdí mi lápiz». Luis responde: «Mi mamá cocina rico». ¿Luis retomó lo que dijo Ema?", "No", "Su respuesta no tiene relación."),
        E("Sol dice: «Mi hermano cumple ocho años». Gaby: «Dijiste que tu hermano cumple ocho años, ¡felicidades!». ¿Gaby escuchó de forma visible?", "Sí", "Retomó lo dicho antes de responder."),
    ],
    [
        E("Mateo cuenta que su perro se llama Rocky. Tomás retoma: «Dijiste que tu gato se llama Rocky». ¿Tomás retomó bien?", "No", "Cambió perro por gato."),
        E("Elige la mejor forma de empezar a responder: a) «Yo ya sé eso», b) «Entendí que…».", "b", "Retomar muestra interés."),
    ],
    [E("Tu compañera Pía dice: «Me caí en el recreo, pero un amigo me ayudó a levantarme». Escribe una respuesta que primero retome y luego reaccione.", "Por ejemplo: Dijiste que te caíste y un amigo te ayudó. Qué bueno que tuviste ayuda", "Retoma y reacciona.")],
    [
        E("¿Mirar a quien habla muestra atención?", "Sí", "Es una forma de escuchar."),
        E("¿«Dijiste que…» sirve para retomar?", "Sí", "Repite lo que el otro dijo."),
        E("¿Puedo responder sin escuchar?", "No", "Se debe escuchar primero."),
    ],
    ("Escucha de forma visible. Un adulto te contará: «El otro día fui a un mercado. Compré tomates y vi un loro que decía hola». Mírale mientras habla. Cuando termine, retoma con «Dijiste que…» y responde con una reacción. Luego cambien de rol: cuéntale tú algo breve y mira cómo te escucha.",
     "Dijiste que fuiste a un mercado, compraste tomates y viste un loro que decía hola. ¡Qué simpático!",
     ["mira a quien habla", "retoma lo importante", "reacciona con respeto"], ["adulto observa la escucha", "respuesta dicha o escrita"], ["no mirar", "responder sin retomar"],
     "Si no retoma, pide que repita una parte de lo que oyó."),
    "Retoma una frase de alguien de tu casa y responde.",
    "Retoma lo dicho por dos personas distintas antes de dar tu opinión.",
)

reg(
    OA25, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: un adulto con quien practicar.",
    "Aprenderé a reconocer cómo se siente otra persona sin suponer y a preguntar con cuidado. Sirve para ser empático y para tratar bien a los demás.",
    ["Sé que las personas tienen emociones.", "Sé hacer preguntas de aclaración."],
    [
        "Empatía es entender cómo se siente otra persona y ponerse en su lugar. Para reconocer una emoción, miramos la cara, escuchamos la voz y pensamos en lo que pasó. Alguien puede estar contento, triste, enojado, asustado o avergonzado.",
        "Pero no podemos estar seguros solo mirando. Por eso no suponemos: preguntamos con cuidado. En vez de decir «estás enojado», podemos decir «¿Cómo te sientes?» o «Parece que estás triste, ¿es así?». La otra persona nos cuenta y no nos equivocamos.",
        "Después de escuchar, respondemos con amabilidad. Podemos decir «Entiendo que te sientas así» o «¿Quieres que te ayude?». Si la persona no quiere hablar, respetamos su decisión. La empatía no obliga a nadie a contar lo que no quiere.",
    ],
    [("empatía", "entender cómo se siente otro"), ("emoción", "lo que siente una persona, como alegría o miedo"), ("suponer", "creer algo sin preguntar"), ("perspectiva", "forma en que otra persona ve algo"), ("respetar", "aceptar lo que el otro decide")],
    [
        ("Preguntar sin suponer", "Un compañero mira el suelo y no juega. ¿Qué le preguntas?", ["Noto que está callado.", "No digo «estás triste» como si fuera seguro.", "Pregunto con cuidado."], "¿Cómo te sientes? ¿Quieres contarme?"),
        ("Responder con empatía", "Ana dice: «Estoy nerviosa por la prueba». ¿Cómo respondes?", ["Retomo lo que dijo.", "Reconozco su emoción.", "Ofrezco ayuda."], "Entiendo que estés nerviosa. ¿Quieres que repasemos juntas?"),
    ],
    [("Decir «seguro estás triste» sin preguntar.", "Se supone lo que siente.", "Pregunta: ¿cómo te sientes?"), ("Insistir cuando no quiere hablar.", "Se olvida respetar.", "Dile que estás cerca si quiere contar.")],
    [
        E("Un niño llora. ¿Qué emoción podría sentir: tristeza o risa?", "Tristeza", "Llorar suele mostrar pena, pero igual conviene preguntar."),
        E("Para no suponer, ¿pregunto «¿cómo te sientes?» o digo «seguro estás enojado»?", "Pregunto cómo se siente", "Así no supongo."),
        E("Si alguien no quiere hablar, ¿insisto o lo respeto?", "Lo respeto", "Cada uno decide si cuenta."),
    ],
    [
        E("En Lenguaje: ¿Qué es la empatía?", "Entender cómo se siente otro", "Es ponerse en su lugar."),
        E("¿Por qué no debo suponer lo que siente alguien?", "Porque puedo equivocarme", "Solo la persona sabe cómo se siente."),
        E("¿Qué puedo ofrecer después de escuchar?", "Ayuda o compañía", "Así muestro cuidado."),
    ],
    [
        E("Tomás tiene la cara roja y los puños cerrados. Escribe una pregunta cuidadosa para él.", "Por ejemplo: ¿Cómo te sientes?", "Pregunta y no supone."),
        E("Luz dice: «Me da vergüenza hablar en público». Escribe una respuesta empática.", "Por ejemplo: Entiendo que te dé vergüenza. ¿Quieres que practiquemos juntas?", "Reconoce la emoción y ofrece ayuda."),
        E("Un compañero se cayó y se ríe, pero tiene los ojos rojos. Escribe cómo preguntarías sin suponer.", "Por ejemplo: ¿Te dolió? ¿Cómo estás?", "Pregunta y no afirma."),
    ],
    [
        E("Ema ve a Pepe callado y dice: «Seguro estás celoso». Pepe responde: «No, solo estoy cansado». ¿Qué hizo mal Ema?", "Supuso sin preguntar", "Se equivocó por suponer."),
        E("Rosa le pregunta a Nico: «¿Quieres contarme qué pasó?». Nico dice que no. Rosa responde: «Está bien, aquí estoy». ¿Fue respetuosa?", "Sí", "Respetó su decisión."),
    ],
    [
        E("Dos compañeros reciben la misma noticia: tendrán una prueba. Uno sonríe y otro se muerde las uñas. ¿Deben sentir lo mismo?", "No", "Cada persona puede sentirse distinto."),
        E("Elige la mejor frase: a) «No llores, no es para tanto.» b) «Veo que estás triste. ¿Quieres contarme?»", "b", "La b reconoce la emoción y pregunta."),
    ],
    [E("Una compañera llega al curso, se sienta lejos del grupo y mira al suelo. Escribe qué le dices para saber cómo está, sin suponer.", "Por ejemplo: Hola, ¿cómo estás? Si quieres, puedes sentarte con nosotros", "Pregunta sin afirmar y ofrece compañía.")],
    [
        E("¿Puedo saber lo que siente alguien solo mirando?", "No", "Podría equivocarme al suponer."),
        E("¿Preguntar con cuidado es una forma de empatía?", "Sí", "Muestra interés por el otro."),
        E("¿Debo obligar a alguien a contarme cómo se siente?", "No", "Debo respetar su decisión."),
    ],
    ("Practica la empatía con un adulto. Lee esta situación: «Camilo perdió su juguete favorito en el parque. Está sentado, callado, con la mirada baja». Escribe o di tres cosas: 1) una pista que ves, 2) una pregunta que le harías sin suponer, 3) una frase para acompañarlo. Respeta si Camilo no quiere hablar.",
     "1) Está callado y mira hacia abajo. 2) ¿Cómo te sientes, Camilo? 3) Entiendo que estés triste por tu juguete. ¿Quieres que lo busquemos juntos?",
     ["nombra una pista concreta", "pregunta sin suponer", "ofrece ayuda o compañía"], ["respuesta escrita u oral con las tres partes"], ["afirmar sin preguntar", "insistir si no quiere hablar"],
     "Si supone, pídele que cambie la afirmación por una pregunta con cómo."),
    "Pregunta a alguien de tu casa cómo se sintió hoy y escucha con atención.",
    "Escribe una conversación breve entre dos amigos donde uno reconoce cómo se siente el otro sin suponer.",
)

reg(
    OA25, 6,
    "Este cuaderno, lápiz y una hoja. Un adulto como compañero de conversación.",
    "Aprenderé a mantener un diálogo breve con tema, turnos y cierre, usando todo lo aprendido. Sirve para participar bien en conversaciones del curso y de la casa.",
    ["Sé aportar al tema.", "Sé dar una opinión con razón.", "Sé hacer preguntas y retomar lo dicho."],
    [
        "Una buena conversación junta varias habilidades. Primero elegimos un tema. Luego hablamos por turnos: uno dice una idea, el otro la retoma, pregunta o agrega su opinión con una razón. Todos mantienen el foco para no perderse.",
        "Mientras conversamos, escuchamos de forma visible: miramos a la persona, retomamos lo que dijo y preguntamos si tenemos dudas. Si alguien piensa distinto, lo escuchamos con respeto. Si alguien se siente mal, reconocemos su emoción sin suponer.",
        "Al terminar, hacemos un cierre. Un cierre es una frase para terminar bien, como «Gracias por conversar» o «Hoy aprendí que…». Con el cierre, todos saben que la conversación acabó y se van contentos.",
    ],
    [("diálogo", "conversación entre dos o más personas"), ("cierre", "forma de terminar una conversación"), ("foco", "mantener el tema"), ("turno", "momento en que me toca hablar"), ("participar", "tomar parte en algo")],
    [
        ("Armar un diálogo breve", "Tema: la lluvia. A dice: «Me gusta la lluvia porque huele a tierra mojada». ¿Cómo responde B retomando y dando su opinión?", ["B retoma lo que dijo A.", "B da su opinión con razón.", "B hace una pregunta."], "Dijiste que huele a tierra mojada. A mí me gusta porque puedo saltar en charcos. ¿Y tú saltas?"),
        ("Hacer un cierre", "Después de hablar de la lluvia, quieres terminar. ¿Qué dices?", ["Resumo lo que aprendí.", "Agradezco.", "Me despido."], "Gracias por conversar. Hoy aprendí que a ti también te gusta la lluvia."),
    ],
    [("Hablar solo yo.", "No se respetan los turnos.", "Escucha, retoma y pregunta."), ("Terminar de golpe sin cerrar.", "Se olvida el cierre.", "Di gracias o resume lo conversado.")],
    [
        E("En un diálogo, ¿hablan por turnos o al mismo tiempo?", "Por turnos", "Así se escucha a todos."),
        E("Un cierre sirve para: ¿empezar o terminar bien la conversación?", "Terminar bien", "Indica que se acabó."),
        E("¿Qué frase es un cierre: «Gracias por conversar» o «Ahora hablemos de otra cosa»?", "Gracias por conversar", "Termina la conversación con cortesía."),
    ],
    [
        E("¿Qué debo mantener durante toda la conversación?", "El foco o tema", "Evita que nos perdamos."),
        E("¿Por qué retomo lo que dijo el otro antes de opinar?", "Para mostrar que escuché", "Así el otro se siente escuchado."),
        E("¿Qué hago si alguien piensa distinto?", "Lo escucho con respeto", "Cada uno puede opinar."),
    ],
    [
        E("Tema: los juegos. Tú dices: «Me gusta el luche». Escribe lo que dice tu compañero retomando y sumando su opinión.", "Por ejemplo: Dijiste que te gusta el luche. A mí me gusta la pelota porque corro", "Retoma y opina."),
        E("Escribe una pregunta para seguir la conversación sobre mascotas, luego de que alguien dijo «Tengo un conejo».", "Por ejemplo: ¿Cómo se llama tu conejo?", "Pide más información."),
        E("Escribe un cierre breve para una conversación sobre vacaciones.", "Por ejemplo: Gracias por contarme sobre tus vacaciones", "Agradece y termina."),
    ],
    [
        E("Dos niños conversan: A habla 5 minutos sin parar. B nunca habla. ¿Respetan los turnos?", "No", "B no tuvo su turno."),
        E("Ana: «Me gusta el invierno porque tomo chocolate». Beto: «¿Qué tipo de chocolate?». ¿Beto mantuvo el foco?", "Sí", "Preguntó sobre lo que dijo Ana."),
    ],
    [
        E("En un diálogo, el cierre «Hoy aprendí que a mi amigo también le gusta pintar» menciona: a) lo conversado, b) un tema nuevo sin relación.", "a", "Resume lo que se habló."),
        E("Ordena una conversación: a) Hasta luego, b) Hola, ¿hablamos de mascotas?, c) A mí me gustan los gatos.", "b, c, a", "Se parte, se conversa y se cierra."),
    ],
    [E("Sandra y Tomi hablan del recreo. Sandra dice: «Me gusta jugar al luche». Escribe una continuación de tres turnos, empezando por Tomi, con una pregunta, una opinión con razón y un cierre.", "Tomi: ¿Con quién juegas? Sandra: Con Ema, porque salta rápido. Tomi: Gracias por contarme.", "Incluye pregunta, opinión y cierre.")],
    [
        E("¿Una conversación necesita un tema?", "Sí", "El tema guía lo que se dice."),
        E("¿Cerrar la conversación es de buena educación?", "Sí", "Así muestra respeto."),
        E("¿Puedo conversar sin escuchar?", "No", "Escuchar es parte de conversar."),
    ],
    ("Sostén una conversación de 3 minutos con un adulto sobre «mi comida favorita». Debes: 1) hablar por turnos, 2) retomar al menos una idea suya, 3) dar tu opinión con razón, 4) hacer una pregunta, 5) cerrar con una frase. Después anota qué parte te resultó más fácil.",
     "Tema: mi comida favorita. Yo: Mi comida favorita son los porotos porque son calientitos. Adulto: Dijiste que son calientitos, ¿con qué los comes? Yo: Con arroz. ¿Y la tuya? Cierre: Gracias por contarme. Me costó más hacer una pregunta.",
     ["mantiene el tema", "respeta turnos", "retoma, pregunta, opina y cierra"], ["adulto cuenta cuántas habilidades usó", "nota de lo más fácil"], ["salirse del tema", "olvidar el cierre"],
     "Si olvida el cierre, ensayen una frase final juntos."),
    "Conversa con alguien de tu casa sobre qué hizo en el día, con turnos y cierre.",
    "Conversa con dos personas a la vez cuidando que los tres tengan turno.",
)

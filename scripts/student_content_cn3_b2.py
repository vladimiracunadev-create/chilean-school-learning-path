"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 10 (propagación y cualidades del sonido) y OA 11 (componentes y escala del Sistema Solar)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA10, OA11 = "CN03 OA 10", "CN03 OA 11"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="Una regla de plástico o madera, una mesa, una liga (elástico) y una caja de zapatos sin tapa, un tazón de plástico, plástico de cocina para taparlo y unos granos de arroz. Nada de vidrio.",
    use="Aprenderé que todo sonido nace de una vibración. Sirve para entender cómo suenan una guitarra, una voz o un tambor.",
    prior=["Sé que oímos con los oídos.", "Sé que una cosa se mueve cuando la empujo."],
    explain=[
        "Un sonido se produce cuando algo vibra. Vibrar es moverse muy rápido hacia un lado y hacia el otro, muchas veces seguidas. Una cuerda de guitarra suena porque vibra, y un tambor suena porque su superficie vibra.",
        "Puedo comprobarlo. Si apoyo una regla en el borde de la mesa, la sujeto con una mano y con la otra tiro del extremo y lo suelto, la regla vibra y suena. Si la sujeto con la mano para que deje de vibrar, el sonido se detiene. Cuando hablo, también puedo sentir con los dedos mi garganta vibrar.",
        "Las vibraciones llegan a mi oído y mi cerebro las entiende como sonido. Si algo no vibra, no suena. Por eso un objeto quieto no produce sonido. Un sonido muy fuerte puede dañar el oído, así que no grito cerca de las orejas de otras personas.",
    ],
    vocab=[("vibración", "movimiento muy rápido de ida y vuelta"), ("sonido", "lo que oímos cuando algo vibra"), ("fuente sonora", "objeto que produce sonido"), ("garganta", "parte del cuello por donde pasa el aire al hablar"), ("oído", "órgano con el que escuchamos")],
    worked=[
        {"title": "La regla en la mesa", "problem": "Una regla sobresale de la mesa. La tiras del extremo y la sueltas. ¿Por qué suena?", "steps": ["Al soltarla, el extremo se mueve de arriba hacia abajo muy rápido.", "Ese movimiento rápido es una vibración.", "La vibración produce el sonido."], "answer": "Suena porque la regla vibra"},
        {"title": "Detener el sonido", "problem": "Una liga estirada suena al tirar de ella. Si pones el dedo sobre la liga, ¿qué pasa con el sonido?", "steps": ["El dedo impide que la liga se mueva.", "Sin vibración no hay sonido.", "El sonido se detiene."], "answer": "El sonido se detiene porque la liga deja de vibrar"},
    ],
    mistakes=[
        {"wrong": "Pensar que los objetos suenan solos, sin moverse.", "why": "No se alcanza a ver el movimiento rápido.", "fix": "Todo objeto que suena vibra; puedes sentirlo con la mano o ver que salta un grano de arroz."},
        {"wrong": "Decir que el sonido es algo que se queda dentro del objeto.", "why": "Se confunde el sonido con el objeto que lo produce.", "fix": "El sonido sale de la vibración y se mueve por el aire hasta el oído."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué ocurre en un objeto cuando produce sonido?", "Vibra", "El sonido nace de una vibración."),
            ex("Si pones el dedo sobre una liga que suena, ¿se detiene el sonido?", "Sí", "El dedo impide que vibre."),
            ex("Completa: un movimiento muy rápido de ida y vuelta se llama ___.", "vibración", "Esa es la definición de vibración."),
        ],
        "understand": [
            ex("¿Por qué suena una cuerda de guitarra?", "Porque vibra", "La vibración produce el sonido."),
            ex("Apoyas los dedos en tu garganta mientras dices «aaa» y sientes un cosquilleo. ¿Qué es lo que sientes?", "La vibración de la garganta", "Al hablar, la garganta vibra."),
            ex("¿Un objeto totalmente quieto puede producir sonido?", "No", "Sin vibración no hay sonido."),
        ],
        "apply": [
            ex("Pones granos de arroz sobre plástico estirado en un tazón y golpeas con una cuchara una olla de metal cerca. Los granos saltan. ¿Qué muestra eso?", "Que el plástico vibra por el sonido", "El movimiento de los granos muestra la vibración."),
            ex("Una regla suena al tirar de su extremo. ¿Qué haces para que deje de sonar?", "La sujeto con la mano para que no vibre", "Si no vibra, no suena."),
            ex("Una campana suena al golpearla. Si la agarras fuerte con las dos manos, el sonido se apaga. ¿Qué detuviste?", "La vibración de la campana", "Sin vibración no hay sonido."),
        ],
        "reason": [
            ex("Rosario dice: «La liga suena aunque no se mueva». Tú ves que la liga se ve desenfocada al sonar. ¿Qué evidencia la contradice?", "Que se ve desenfocada porque vibra", "Se ve borrosa porque se mueve muy rápido."),
            ex("Dos reglas iguales sobresalen igual de la mesa. A una la dejas libre y a otra la sujetas fuerte con la mano. ¿Cuál puede sonar?", "La que está libre", "Solo puede sonar la que vibra."),
        ],
        "challenge": [
            ex("Pones los dedos en tu garganta. ¿Cuándo sientes cosquilleo: cuando dices «aaa» o cuando te quedas en silencio?", "Cuando dices «aaa»", "Al producir la voz la garganta vibra; en silencio no vibra."),
            ex("Quieres ver que el parche de un tambor vibra al golpearlo. ¿Qué te sirve poner encima: granos de arroz o una piedra grande?", "Granos de arroz", "Los granos livianos saltan y muestran la vibración; una piedra grande no se mueve."),
        ],
    },
    context=[ex("Andrés toca una guitarra y pone la mano sobre las cuerdas. El sonido se apaga de golpe. ¿Qué explica eso?", "Que la mano detuvo la vibración de las cuerdas", "Sin vibración el sonido termina.")],
    selfcheck=[
        ex("¿De dónde nace un sonido?", "De una vibración", "Algo que vibra produce sonido."),
        ex("¿Qué pasa con el sonido si detengo la vibración?", "Se detiene", "No hay vibración, no hay sonido."),
        ex("¿Qué se mueve en la garganta cuando hablo?", "Vibra", "La voz nace de una vibración."),
    ],
    open_task=task(
        "Si puedes, haz sonar una regla en el borde de la mesa y una liga estirada sobre una caja sin tapa. Anota qué sientes con los dedos y qué pasa si detienes el movimiento. Si no puedes, usa estos datos: regla libre, suena y se ve borrosa; regla sujetada, no suena. Dibuja la regla en cada caso y escribe tu conclusión sobre la vibración y el sonido.",
        "La regla libre vibra y suena. La regla sujetada no vibra y no suena. Conclusión: el sonido se produce cuando algo vibra.",
        ["relaciona vibración y sonido", "describe lo que pasa cuando se detiene la vibración", "dibuja los dos casos"],
        ["dibujos con rótulos", "registro de lo observado", "frase de conclusión"],
        ["decir que el sonido existe sin vibración", "olvidar describir qué pasa al detener la regla"],
        "Reconoce lo observado y pregunta cómo podría ver la vibración de una cuerda con algo liviano encima.",
    ),
    reinforce="Toca tu garganta mientras tarareas una canción corta y cuenta qué sientes.",
    extend="Busca tres objetos de tu casa que suenen y escribe cuál parte de cada uno vibra.",
)

register(
    OA10, 2,
    materials="Un reloj de pulsera o un temporizador de cocina que haga «tic», cinta métrica o pasos, y tres o cuatro personas de la casa. Un lugar tranquilo y amplio.",
    use="Aprenderé que el sonido viaja en todas las direcciones y se debilita con la distancia. Sirve para entender por qué oímos a alguien aunque no lo veamos.",
    prior=["Sé que el sonido nace de una vibración.", "Sé medir una distancia en pasos o metros."],
    explain=[
        "Cuando algo vibra, el sonido sale hacia todos lados: adelante, atrás, a los lados, arriba y abajo. Por eso puedo oír a una persona que habla en otra pieza, aunque no esté mirando hacia mí.",
        "El sonido necesita un medio para viajar. Medio es la materia por donde pasa el sonido, como el aire, el agua o una pared. En el aire, las vibraciones van pasando de un trozo de aire al siguiente hasta llegar al oído. En el espacio no hay aire y por eso no se oye ningún sonido.",
        "Cuanto más lejos estoy de la fuente, más débil oigo el sonido, porque la vibración se reparte por todos lados. Si me alejo del reloj que hace «tic», dejo de oírlo a cierta distancia. Si dos personas están a la misma distancia, oyen igual de fuerte, estén donde estén.",
    ],
    vocab=[("medio", "materia por donde viaja el sonido, como el aire o el agua"), ("dirección", "hacia dónde va algo"), ("distancia", "cuánto separa dos lugares"), ("débil", "poco fuerte"), ("fuente sonora", "lo que produce el sonido")],
    worked=[
        {"title": "Oír en varias direcciones", "problem": "Un temporizador hace «tic» en el centro de una pieza. Cuatro personas están a 2 m: una adelante, una atrás y dos a los lados. ¿Quiénes lo oyen?", "steps": ["El sonido sale hacia todos lados.", "Todos están a la misma distancia.", "Todos lo oyen igual de fuerte."], "answer": "Las cuatro personas lo oyen"},
        {"title": "Alejarse de la fuente", "problem": "Un reloj se oye bien a 1 m y casi no se oye a 5 m. ¿Por qué?", "steps": ["El sonido se reparte por todos lados.", "Al alejarme, llega menos al oído.", "Se oye más débil."], "answer": "Porque a más distancia el sonido llega más débil"},
    ],
    mistakes=[
        {"wrong": "Pensar que el sonido solo va en línea recta hacia un oído.", "why": "Se confunde con la luz, que viaja recta.", "fix": "El sonido sale por todos lados; por eso se oye aunque no estés al frente."},
        {"wrong": "Creer que en el espacio se pueden oír las explosiones.", "why": "Se ha visto en películas.", "fix": "En el espacio no hay aire, así que el sonido no puede viajar."},
    ],
    tiers={
        "recovery": [
            ex("¿El sonido viaja en una sola dirección o en todas las direcciones?", "En todas las direcciones", "Sale hacia todos lados desde la fuente."),
            ex("Si te alejas de un reloj que hace tic, ¿lo oyes más fuerte o más débil?", "Más débil", "Mientras más lejos, más débil llega."),
            ex("Completa: el sonido necesita un ___ para viajar, como el aire.", "medio", "El medio es la materia por donde viaja."),
        ],
        "understand": [
            ex("¿Por qué puedes oír a alguien que habla desde la pieza de al lado?", "Porque el sonido viaja en todas las direcciones", "No hace falta mirar a la fuente."),
            ex("¿Qué es un medio para el sonido?", "La materia por donde viaja el sonido", "Puede ser el aire, el agua o un sólido."),
            ex("¿Por qué en el espacio no se oyen sonidos?", "Porque no hay aire", "Sin medio el sonido no viaja."),
        ],
        "apply": [
            ex("Hay tres niños a 2 m, 4 m y 8 m de una campana. ¿Cuál oye el sonido más débil?", "El que está a 8 m", "Es el más lejano."),
            ex("Una persona ríe en el centro de un patio y hay cuatro personas a su alrededor a igual distancia. ¿Cuántas la oyen?", "Las cuatro", "El sonido va en todas las direcciones."),
            ex("Sofía oye a su hermano que habla en la pieza de al lado. Entre los dos hay aire. ¿El sonido viaja por el aire o por el vacío?", "Por el aire", "El aire es el medio que lleva las vibraciones."),
        ],
        "reason": [
            ex("Gabriel dice: «No te oigo porque no me miras». Según lo que sabes del sonido, ¿es correcta su razón?", "No", "El sonido viaja en todas las direcciones; mirar no es necesario."),
            ex("Dos personas oyen el mismo timbre. Una está a 3 m y la otra a 15 m. ¿Cuál lo oye más fuerte y por qué?", "La que está a 3 m, porque está más cerca", "A más distancia llega más débil."),
        ],
        "challenge": [
            ex("Un astronauta golpea una herramienta fuera de su nave, en el espacio vacío. ¿Puede otro astronauta oír ese golpe por el espacio vacío? ¿Por qué?", "No, porque no hay aire", "Sin medio no viaja el sonido."),
            ex("Para comprobar con un reloj que el sonido va en varias direcciones, ¿dónde ubicas a las personas: todas al mismo lado del reloj o en distintos lados, a igual distancia?", "En distintos lados, a igual distancia", "Si todas lo oyen desde lados distintos, el sonido va hacia todos lados."),
        ],
    },
    context=[ex("En una fiesta, el cantante está en el centro de un salón y Sara, a un lado, y Pedro, al fondo, lo oyen. ¿Qué puede decir Sara sobre cómo viaja el sonido?", "Que llega en todas las direcciones", "Ambos lo oyen estando en distintos lados.")],
    selfcheck=[
        ex("¿Por dónde sale el sonido de una fuente sonora?", "Por todos lados", "Viaja en todas las direcciones."),
        ex("¿Se oye más débil el sonido cuando me alejo?", "Sí", "Se reparte y llega con menos fuerza."),
        ex("¿Qué necesita el sonido para viajar?", "Un medio", "Como aire, agua o sólidos."),
    ],
    open_task=task(
        "Si puedes, pon un temporizador o reloj con tic en el centro de una pieza. Pide a tres personas que se ubiquen a 2 m en tres lados distintos y anota si lo oyen. Luego aléjate de a 1 m y anota la distancia a la que dejas de oírlo. Si no puedes, usa estos datos: a 2 m lo oyen la persona de adelante, la de atrás y la del lado; a 6 m ya no lo oye nadie. Dibuja la fuente con flechas hacia todos lados y escribe tu conclusión.",
        "El tic se oye en todos los lados a 2 m y deja de oírse a 6 m. Conclusión: el sonido viaja en todas las direcciones y se debilita con la distancia.",
        ["dibuja flechas hacia todos lados", "menciona la distancia", "concluye sobre direcciones y debilitamiento"],
        ["dibujo con flechas", "tabla de distancias", "frase de conclusión"],
        ["dibujar solo una flecha", "no mencionar que se debilita"],
        "Valora la tabla y pide que explique qué cambiaría si el pasillo fuera muy largo.",
    ),
    reinforce="Habla en voz baja a alguien de tu casa colocándote en distintos lados de una pieza y anota desde dónde te oye.",
    extend="Pregunta a alguien qué sonidos oye desde su pieza que vienen de otros lugares de la casa.",
)

register(
    OA10, 3,
    materials="Una mesa de madera, un reloj que haga tic (o dos cucharas para golpear suave), dos vasos de plástico, un trozo de hilo o pitilla de 3 m y un lápiz para hacer un agujero en el fondo (con ayuda de una persona adulta).",
    use="Aprenderé que el sonido viaja por materiales distintos y que en los sólidos suele oírse más fuerte. Sirve para entender los teléfonos de vasos y por qué se oye a través de una pared.",
    prior=["Sé que el sonido necesita un medio.", "Sé que se debilita con la distancia."],
    explain=[
        "El sonido puede viajar por gases, como el aire, por líquidos, como el agua, y por sólidos, como la madera o el metal. Cada material puede ser un medio.",
        "Los sólidos y los líquidos suelen llevar el sonido mejor que el aire. Si pongo la oreja sobre una mesa de madera y golpeo suavemente el otro extremo con un dedo, oigo el golpe más fuerte que si lo escucho a través del aire.",
        "Con dos vasos de plástico unidos por un hilo tenso hago un teléfono de vasos. La voz hace vibrar el fondo de un vaso, la vibración viaja por el hilo y hace vibrar el otro vaso. Si el hilo está flojo, la vibración no pasa bien y no se oye. Otros materiales, como la tela gruesa, dejan pasar poco sonido.",
    ],
    vocab=[("sólido", "material con forma propia, como la madera"), ("líquido", "material que fluye, como el agua"), ("gas", "material como el aire"), ("tenso", "estirado, sin quedar flojo"), ("transmitir", "hacer pasar algo de un lugar a otro")],
    worked=[
        {"title": "Teléfono de vasos", "problem": "Dos vasos unidos por un hilo bien tenso. Hablas en uno y tu amiga escucha en el otro. ¿Qué lleva el sonido de un vaso al otro?", "steps": ["Tu voz hace vibrar el fondo del vaso.", "La vibración viaja por el hilo.", "El otro vaso vibra y se oye."], "answer": "El hilo tenso lleva la vibración"},
        {"title": "Oreja en la mesa", "problem": "Golpeas suavemente un extremo de una mesa y apoyas la oreja en el otro. ¿Se oye más fuerte con la oreja en la mesa o sin tocarla?", "steps": ["La madera es un sólido y lleva la vibración.", "La oreja pegada recibe la vibración directo.", "Se oye más fuerte."], "answer": "Con la oreja apoyada en la mesa"},
    ],
    mistakes=[
        {"wrong": "Decir que el sonido solo viaja por el aire.", "why": "Casi siempre oímos sonidos que llegan por el aire.", "fix": "También viaja por líquidos y sólidos, y a veces se oye mejor."},
        {"wrong": "Pensar que un hilo flojo lleva igual de bien el sonido.", "why": "No se recuerda que la vibración necesita un hilo estirado.", "fix": "Para que el hilo transmita la vibración, debe estar tenso."},
    ],
    tiers={
        "recovery": [
            ex("¿Por qué materiales puede viajar el sonido: gases, líquidos y sólidos, o solo gases?", "Gases, líquidos y sólidos", "Todos pueden ser un medio."),
            ex("En un teléfono de vasos, ¿el hilo debe estar tenso o flojo?", "Tenso", "Un hilo tenso transmite la vibración."),
            ex("Completa: la madera es un material ___ por el que viaja el sonido.", "sólido", "La madera es un sólido."),
        ],
        "understand": [
            ex("¿Cómo llega la voz de un vaso al otro en un teléfono de vasos?", "Como vibración que viaja por el hilo", "El hilo transmite la vibración."),
            ex("¿Por qué se oye más fuerte un golpe si apoyas la oreja en una mesa de madera?", "Porque el sólido lleva bien la vibración", "La mesa transmite el golpe a tu oído."),
            ex("El agua es un líquido. ¿Puede el sonido viajar por el agua?", "Sí", "Los líquidos también transmiten el sonido."),
        ],
        "apply": [
            ex("Clasifica el medio en gas, líquido o sólido: aire, agua, metal.", "Gas, líquido, sólido", "El aire es gas, el agua es líquido y el metal es sólido."),
            ex("Oyes a un vecino que golpea una muralla de su casa. ¿Qué medio sólido llevó el sonido hasta ti?", "La muralla", "Las paredes transmiten la vibración."),
            ex("Un niño usa un teléfono de vasos con un hilo muy flojo y no se oye nada. ¿Qué debe hacer para que funcione?", "Estirar el hilo", "Así la vibración puede pasar."),
        ],
        "reason": [
            ex("Un niño dice que no puede oír a su amigo que golpea la mesa porque está lejos. Pone la oreja en la mesa y lo oye. ¿Qué explica eso?", "La mesa de madera transmitió el sonido", "El sólido lleva la vibración."),
            ex("Dos teléfonos de vasos: A con hilo tenso y B con el hilo enrollado y flojo. ¿En cuál se escucha mejor y por qué?", "En A, porque el hilo está tenso", "La vibración viaja bien por un hilo estirado."),
        ],
        "challenge": [
            ex("Una pared gruesa deja pasar poco sonido, pero un golpe en una cañería de metal se oye en toda la casa. ¿Qué dato apoya que los sólidos transmiten el sonido?", "El golpe en el metal se oye en toda la casa", "El metal lleva muy bien la vibración."),
            ex("Golpeas suave un extremo de una mesa. Para comprobar que la mesa lleva el sonido, ¿dónde pones la oreja: apoyada en el otro extremo de la mesa o lejos de la mesa?", "Apoyada en el otro extremo de la mesa", "Si se oye bien con la oreja apoyada, la mesa lleva el sonido."),
        ],
    },
    context=[ex("Lucía apoya la oreja en el piso de madera de su casa y oye pasos de alguien que camina en la pieza vecina. ¿Qué medio sólido llevó el sonido hasta su oído?", "El piso de madera", "La madera es un sólido que transmite la vibración de los pasos.")],
    selfcheck=[
        ex("¿El sonido puede viajar por un sólido?", "Sí", "Por ejemplo por la madera."),
        ex("¿Qué pasa si el hilo de un teléfono de vasos queda flojo?", "No transmite bien el sonido", "Necesita estar tenso."),
        ex("¿Por qué materiales viaja el sonido?", "Sólidos, líquidos y gases", "Todos son medios."),
    ],
    open_task=task(
        "Si puedes, haz un teléfono de vasos con un hilo de 3 m: pide a una persona adulta que haga un agujero en el fondo de cada vaso de plástico. Prueba con el hilo tenso y flojo. Si no puedes, usa estos datos: hilo tenso, se oye bien; hilo flojo, no se oye. Escribe qué materiales actúan como medio y por qué el hilo debe estar tenso.",
        "El hilo, que es un sólido, lleva la vibración. Debe estar tenso porque si está flojo la vibración no pasa. Conclusión: el sonido viaja por los sólidos.",
        ["nombra el hilo como medio sólido", "explica por qué debe estar tenso", "usa los datos de hilo tenso y flojo"],
        ["registro con dos pruebas", "dibujo del teléfono", "frase de conclusión"],
        ["decir que la voz viaja por el hilo como si fuera un tubo", "no comparar el hilo tenso y flojo"],
        "Valora el uso del vocabulario y pide que dibuje el recorrido de la vibración.",
    ),
    reinforce="Apoya la oreja en una mesa y golpea suave con un dedo. Compara con oírlo sin apoyar la oreja.",
    extend="Averigua con una persona de tu casa qué sonidos de la calle oyes desde tu pieza y qué pared los deja pasar menos.",
)

register(
    OA10, 4,
    materials="Un temporizador o reloj con tic, una caja de zapatos con tapa, una toalla o polera gruesa y cinta métrica. Un pasillo o una pieza vacía. No uses sonidos fuertes.",
    use="Aprenderé que el sonido puede reflejarse (rebotar) o absorberse. Sirve para entender el eco y por qué las salas con alfombras suenan distinto.",
    prior=["Sé que el sonido viaja en todas las direcciones.", "Sé que viaja por distintos materiales."],
    explain=[
        "Cuando el sonido llega a una superficie, puede reflejarse, es decir, rebotar, o absorberse, es decir, quedar atrapado en el material y debilitarse. Las superficies duras y lisas, como un muro o un piso de cerámica, reflejan mucho sonido.",
        "El eco se produce cuando el sonido rebota en una superficie dura y grande y vuelve a mis oídos un poquito después. Para oírlo, la superficie debe estar muy lejos, a muchos metros. En una sala pequeña el sonido rebota tan rápido que no se separa del original, y solo lo siento como un sonido que dura más.",
        "Los materiales blandos y esponjosos, como las cortinas gruesas, las alfombras y las telas, absorben el sonido. Por eso una pieza con alfombra y cortinas tiene menos eco y se oye más apagada. Si pongo un temporizador dentro de una caja con toalla, lo oigo menos que si la caja está vacía.",
    ],
    vocab=[("reflejar el sonido", "hacer que el sonido rebote"), ("absorber", "quedarse con el sonido y debilitarlo"), ("eco", "sonido que rebota y se oye un poco después"), ("blando", "que se hunde al apretarlo, como una toalla"), ("duro", "que no se hunde, como un muro")],
    worked=[
        {"title": "Caja con toalla", "problem": "Un temporizador se oye hasta 8 m sin caja, hasta 5 m dentro de una caja vacía y hasta 2 m dentro de una caja con toalla. ¿Qué material absorbe más sonido?", "steps": ["Comparo hasta dónde se oye en cada caso.", "Con toalla se oye solo hasta 2 m, el menor alcance.", "Entonces la toalla absorbe más."], "answer": "La toalla absorbe más sonido"},
        {"title": "Eco en una cancha", "problem": "Gritas frente a un muro grande de una cancha, lejos de ti, y oyes tu voz de vuelta. ¿Qué pasó con el sonido?", "steps": ["El muro es duro y grande.", "El sonido rebotó en él.", "Volvió a tus oídos un momento después."], "answer": "Se reflejó en el muro y produjo eco"},
    ],
    mistakes=[
        {"wrong": "Pensar que el eco existe en cualquier pieza pequeña.", "why": "Se piensa que todo rebote es eco.", "fix": "El eco se oye separado cuando la superficie está lejos; en una pieza pequeña el rebote se mezcla con el sonido original."},
        {"wrong": "Decir que las alfombras reflejan mucho el sonido.", "why": "Se confunde reflejar con absorber.", "fix": "Los materiales blandos absorben el sonido; los duros lo reflejan."},
    ],
    tiers={
        "recovery": [
            ex("¿Un muro duro refleja o absorbe más el sonido?", "Refleja", "Las superficies duras hacen rebotar el sonido."),
            ex("¿Una toalla gruesa absorbe sonido?", "Sí", "Los materiales blandos absorben."),
            ex("Completa: el sonido que rebota y vuelve a mi oído se llama ___.", "eco", "El eco es el sonido que rebota."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre reflejar y absorber el sonido?", "Reflejar es rebotarlo y absorber es debilitarlo dentro del material", "Una superficie devuelve el sonido y la otra lo atrapa."),
            ex("¿Por qué una pieza con alfombra y cortinas tiene menos eco?", "Porque esos materiales blandos absorben el sonido", "Absorben en vez de rebotar."),
            ex("¿Por qué en un cerro con una pared de roca lejos puedes oír el eco?", "Porque la roca refleja el sonido", "La superficie dura y lejana lo devuelve."),
        ],
        "apply": [
            arith("Un reloj se oye hasta 9 m sin nada, hasta 6 m dentro de una caja vacía y hasta 3 m dentro de una caja con ropa gruesa. ¿Cuántos metros menos se oye con la ropa gruesa que sin nada?", "9-3", "La ropa gruesa absorbe sonido y reduce hasta dónde se oye.", " m"),
            ex("Una sala tiene piso de cerámica, paredes lisas y sin cortinas. ¿Esperas mucho o poco eco?", "Mucho eco", "Las superficies duras y lisas reflejan el sonido."),
            ex("Quieres que una pieza de música tenga menos eco. ¿Pones alfombra y cortinas gruesas o más baldosas lisas?", "Alfombra y cortinas gruesas", "Los materiales blandos absorben el sonido; las baldosas lisas lo reflejan."),
        ],
        "reason": [
            ex("Un compañero dice que si grita en su pieza pequeña no hay eco porque no hay rebote. ¿Cuál es el error?", "Sí hay rebote, pero está muy cerca y se mezcla con la voz", "El sonido rebota en las paredes de la pieza."),
            ex("En el experimento de la caja, un niño usó una toalla en una prueba y otra caja con un pañuelo delgado en otra. ¿Qué debió mantener igual para comparar justo?", "El mismo temporizador, la misma caja y la misma distancia", "Así solo cambia el material."),
        ],
        "challenge": [
            ex("Una biblioteca tiene alfombra y cortinas gruesas. ¿Por qué es útil para que haya silencio?", "Porque absorben el sonido y evitan el eco", "Los materiales blandos absorben."),
            ex("Para saber cuál de dos telas absorbe más el sonido de un reloj, ¿qué mides: hasta qué distancia se oye el reloj envuelto en cada tela o el color de cada tela?", "Hasta qué distancia se oye el reloj envuelto en cada tela", "La tela con menor alcance absorbe más."),
        ],
    },
    context=[ex("Camilo canta en el baño con paredes de cerámica y su voz suena fuerte y larga. En el dormitorio con alfombra y cortinas suena apagada. ¿Por qué cambia su voz?", "En el baño las paredes duras reflejan el sonido y en el dormitorio lo absorben", "Las superficies duras reflejan y las blandas absorben.")],
    selfcheck=[
        ex("¿Qué materiales absorben el sonido?", "Los blandos", "Como telas y alfombras."),
        ex("¿Qué es el eco?", "Sonido que rebota y se oye después", "Es una reflexión del sonido."),
        ex("¿Una pared dura y lisa refleja el sonido?", "Sí", "Lo hace rebotar."),
    ],
    open_task=task(
        "Si puedes, mide hasta qué distancia se oye un temporizador sin caja, dentro de una caja vacía y dentro de una caja con una toalla. Si no puedes, usa estos datos: sin caja 8 m; caja vacía 5 m; caja con toalla 2 m. Haz una tabla, ordena de menos a más absorbente y escribe una conclusión.",
        "Sin caja 8 m, caja vacía 5 m, caja con toalla 2 m. La toalla absorbe más. Conclusión: los materiales blandos absorben el sonido.",
        ["ordena correctamente de menos a más absorbente", "usa los números de la tabla", "concluye sobre materiales blandos"],
        ["tabla con distancias", "orden escrito", "frase de conclusión"],
        ["decir que entre más lejos se oye más absorbe", "no mencionar la toalla"],
        "Valora la tabla y pregunta qué ocurriría con una tela más gruesa.",
    ),
    reinforce="Ve a un pasillo y a una pieza con alfombra y aplaude una vez en cada lugar. Anota en cuál suena más largo.",
    extend="Pregunta en tu casa en qué pieza el sonido se oye más fuerte y por qué creen que ocurre.",
)

register(
    OA10, 5,
    materials="Una regla de plástico o madera de 30 cm, una mesa, tres ligas de distinto grosor, una caja de zapatos sin tapa. No uses sonidos fuertes ni cerca de los oídos de otras personas.",
    use="Aprenderé a distinguir tono e intensidad del sonido. Sirve para describir si un sonido es grave o agudo y si es fuerte o débil.",
    prior=["Sé que el sonido nace de una vibración.", "Sé que el sonido se debilita con la distancia."],
    explain=[
        "El tono es qué tan grave o agudo es un sonido. Un tono grave es bajo, como el de una voz profunda. Un tono agudo es alto, como el de un silbido. El tono depende de qué tan rápido vibra el objeto: si vibra rápido, el tono es agudo; si vibra lento, es grave.",
        "La intensidad es qué tan fuerte o débil se oye un sonido. Depende de cuánto se mueve el objeto al vibrar. Si golpeo una cuerda suave, vibra poco y suena débil. Si la golpeo fuerte, vibra mucho y suena fuerte. La intensidad no cambia el tono.",
        "Con una regla en el borde de una mesa puedo probarlo: cuanto más corta es la parte que sobresale, más rápido vibra y más agudo suena. Si tiro del extremo más fuerte, suena más fuerte, pero con el mismo tono. Cuido mis oídos: no uso sonidos muy fuertes ni audífonos con mucho volumen.",
    ],
    vocab=[("tono", "qué tan grave o agudo es un sonido"), ("grave", "sonido bajo, como una voz profunda"), ("agudo", "sonido alto, como un silbido"), ("intensidad", "qué tan fuerte o débil se oye un sonido"), ("volumen", "nivel de fuerza con que se oye un aparato de música")],
    worked=[
        {"title": "La regla corta y larga", "problem": "Una regla sobresale 10 cm de la mesa y suena. Luego sobresale 25 cm y suena. ¿En cuál el tono es más agudo?", "steps": ["La parte corta vibra más rápido.", "Vibrar rápido da un tono agudo.", "La de 10 cm es más aguda."], "answer": "La regla que sobresale 10 cm"},
        {"title": "Golpear más fuerte", "problem": "Un tambor suena débil con un golpe suave y fuerte con un golpe fuerte. ¿Qué cambió: el tono o la intensidad?", "steps": ["El golpe fuerte hace vibrar más el parche.", "Suena más fuerte, no más agudo.", "Cambió la intensidad."], "answer": "La intensidad"},
    ],
    mistakes=[
        {"wrong": "Confundir un sonido agudo con un sonido fuerte.", "why": "Ambos pueden parecer «altos» al decirlo.", "fix": "Agudo y grave hablan del tono; fuerte y débil hablan de la intensidad."},
        {"wrong": "Pensar que subir el volumen hace el tono más agudo.", "why": "Se cree que más fuerte es más alto de tono.", "fix": "Subir el volumen cambia la intensidad, no el tono."},
    ],
    tiers={
        "recovery": [
            ex("Un silbido, ¿es un sonido grave o agudo?", "Agudo", "Es un tono alto."),
            ex("Una voz muy profunda, ¿tiene un tono grave o agudo?", "Grave", "Es un tono bajo."),
            ex("Completa: qué tan fuerte o débil se oye un sonido se llama ___.", "intensidad", "Intensidad habla de lo fuerte del sonido."),
        ],
        "understand": [
            ex("¿De qué depende el tono de un sonido?", "De qué tan rápido vibra el objeto", "Más rápido, tono más agudo."),
            ex("¿De qué depende la intensidad de un sonido?", "De cuánto se mueve el objeto al vibrar", "Más movimiento, más fuerte."),
            ex("¿Es lo mismo un sonido agudo que un sonido fuerte?", "No", "Agudo es tono y fuerte es intensidad."),
        ],
        "apply": [
            ex("Una regla sobresale 10 cm, otra de las mismas características sobresale 15 cm y otra 25 cm. ¿Cuál suena más grave?", "La de 25 cm", "A más largo, vibra más lento y es más grave."),
            ex("Tocas una cuerda suave y luego fuerte. ¿Qué suena más fuerte?", "La golpeada fuerte", "Vibra más y tiene mayor intensidad."),
            ex("En una guitarra la cuerda delgada suena más aguda que la gruesa. ¿Cuál vibra más rápido?", "La delgada", "Vibrar más rápido da el tono más agudo."),
        ],
        "reason": [
            ex("Marta dice: «Si subo el volumen, el sonido se hace más agudo». ¿Tiene razón?", "No", "Subir el volumen solo cambia la intensidad."),
            ex("Una campana grande suena grave y una campana chica suena aguda. ¿Cuál vibra más lento?", "La grande", "El tono grave viene de vibraciones lentas."),
        ],
        "challenge": [
            ex("Un niño quiere que una regla suene más aguda sin golpearla más fuerte. ¿Qué cambia?", "Deja sobresalir menos regla de la mesa", "Una parte más corta vibra más rápido."),
            ex("Un niño usa audífonos con el volumen al máximo durante horas. ¿Es una forma segura de cuidar sus oídos?", "No", "Los sonidos muy fuertes y prolongados pueden dañar el oído."),
        ],
    },
    context=[ex("Nicolás escucha un trueno lejano que suena grave y débil, y una alarma cercana que suena aguda y fuerte. ¿Cuál tiene el tono más agudo?", "La alarma", "Es la que suena aguda; el trueno suena grave.")],
    selfcheck=[
        ex("¿Qué es el tono?", "Qué tan grave o agudo es un sonido", "El tono habla de lo grave o agudo."),
        ex("¿Qué es la intensidad?", "Qué tan fuerte o débil se oye un sonido", "Es la fuerza con que se oye."),
        ex("¿Una vibración rápida da un tono agudo o grave?", "Agudo", "A más rápido, más agudo."),
    ],
    open_task=task(
        "Si puedes, haz sonar una regla en el borde de una mesa dejando 10 cm, 15 cm y 25 cm fuera. Escucha el tono y anota cuál es más agudo. Luego tira de la regla suave y fuerte y anota la intensidad. Si no puedes, usa estos datos: 10 cm tono muy agudo; 15 cm tono medio; 25 cm tono grave; tirón suave suena débil; tirón fuerte suena fuerte. Escribe una conclusión sobre tono e intensidad.",
        "A menos regla afuera, más agudo. Un tirón más fuerte hace sonar más fuerte pero no cambia el tono. Conclusión: el tono depende de la rapidez de la vibración y la intensidad de cuánto se mueve.",
        ["ordena los tonos de más agudo a más grave", "separa tono de intensidad", "escribe una conclusión"],
        ["tabla con los tonos", "registro de intensidad", "frase de conclusión"],
        ["confundir agudo con fuerte", "decir que el tirón fuerte cambia el tono"],
        "Reconoce la tabla y pide que dé un ejemplo de su casa de sonido grave y uno agudo.",
    ),
    reinforce="Haz sonar con la boca un sonido agudo y uno grave y luego uno fuerte y uno débil. Nombra cada uno.",
    extend="Escucha en tu casa tres sonidos y anota si cada uno es grave o agudo, fuerte o débil.",
)

# ---------------------------------------------------------------- OA 11
register(
    OA11, 1,
    materials="Papel y lápiz. Si puedes, una persona de tu casa te ayuda a mirar un dibujo del Sistema Solar en un libro. No mires al Sol directamente.",
    use="Aprenderé a distinguir el Sol, los planetas, las lunas, los cometas y los asteroides. Sirve para ubicar cada cuerpo del Sistema Solar.",
    prior=["Sé que el Sol es una fuente de luz.", "Sé que la Luna refleja la luz del Sol."],
    explain=[
        "El Sistema Solar está formado por el Sol y todos los cuerpos que giran a su alrededor. El Sol es una estrella: emite luz y calor propios y está en el centro. Los demás cuerpos giran en caminos llamados órbitas.",
        "Los planetas son cuerpos grandes y redondos que giran alrededor del Sol. Son ocho: Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano y Neptuno. No emiten luz propia: brillan porque reflejan la luz del Sol. Las lunas giran alrededor de un planeta; la Tierra tiene una, la Luna.",
        "Los asteroides son trozos de roca que giran alrededor del Sol; hay muchos entre Marte y Júpiter. Los cometas son cuerpos de hielo, polvo y roca; cuando se acercan al Sol les sale una cola. Hay que ser preciso: el Sol es una estrella, no un planeta, y la Luna es una luna, no un planeta.",
    ],
    vocab=[("Sistema Solar", "el Sol y los cuerpos que giran a su alrededor"), ("estrella", "astro que emite luz y calor propios"), ("planeta", "cuerpo grande y redondo que gira alrededor del Sol"), ("luna", "cuerpo que gira alrededor de un planeta"), ("órbita", "camino que sigue un cuerpo al girar alrededor de otro")],
    worked=[
        {"title": "Distinguir Sol y planeta", "problem": "¿Qué diferencia hay entre el Sol y la Tierra?", "steps": ["El Sol emite luz propia: es una estrella.", "La Tierra gira alrededor del Sol y no emite luz propia: es un planeta.", "El Sol está en el centro."], "answer": "El Sol es una estrella que emite luz; la Tierra es un planeta que gira a su alrededor"},
        {"title": "Una luna", "problem": "Un cuerpo gira alrededor de Marte. ¿Cómo se llama?", "steps": ["Gira alrededor de un planeta.", "Eso es una luna."], "answer": "Una luna"},
    ],
    mistakes=[
        {"wrong": "Decir que la Luna es un planeta.", "why": "Se ve grande en el cielo.", "fix": "Una luna gira alrededor de un planeta; la Luna gira alrededor de la Tierra."},
        {"wrong": "Decir que el Sol es un planeta.", "why": "Se ve grande y redondo.", "fix": "El Sol es una estrella porque emite luz propia."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es el Sol: una estrella o un planeta?", "Una estrella", "Emite luz y calor propios."),
            ex("¿Cuántos planetas tiene el Sistema Solar?", "8", "Son ocho: de Mercurio a Neptuno."),
            ex("Completa: un cuerpo que gira alrededor de un planeta se llama ___.", "luna", "Luna es el cuerpo que gira alrededor de un planeta."),
        ],
        "understand": [
            ex("¿Qué es un cometa?", "Un cuerpo de hielo, polvo y roca que tiene cola cerca del Sol", "La cola aparece cuando se acerca al Sol."),
            ex("¿Qué es un asteroide?", "Un trozo de roca que gira alrededor del Sol", "Hay muchos entre Marte y Júpiter."),
            ex("¿Por qué los planetas brillan si no tienen luz propia?", "Porque reflejan la luz del Sol", "Rebotan la luz que reciben."),
        ],
        "apply": [
            ex("Clasifica como estrella, planeta o luna: Sol, Tierra, Luna.", "Estrella, planeta, luna", "El Sol emite luz; la Tierra gira alrededor del Sol; la Luna gira alrededor de la Tierra."),
            ex("Nombra el planeta que sigue después de Marte en el orden Mercurio, Venus, Tierra, Marte...", "Júpiter", "El quinto planeta es Júpiter."),
            ex("Un cuerpo de hielo y roca que crece con una cola brillante al acercarse al Sol. ¿Es un cometa o un asteroide?", "Un cometa", "La cola con hielo y polvo es de un cometa."),
        ],
        "reason": [
            ex("Pablo dice que la Luna es un planeta porque es redonda. ¿Qué dato lo corrige?", "La Luna gira alrededor de la Tierra y no del Sol", "Por eso es una luna."),
            ex("Una compañera dice: «Venus es una estrella porque brilla mucho en la noche». ¿Tiene razón?", "No", "Venus es un planeta; brilla porque refleja la luz del Sol."),
        ],
        "challenge": [
            ex("¿Cuántos planetas hay entre la Tierra y el Sol?", "2", "Mercurio y Venus están más cerca del Sol que la Tierra."),
            arith("La Tierra es el tercer planeta desde el Sol. ¿Cuántos planetas están más lejos del Sol que la Tierra?", "8-3", "De los 8 planetas se descuentan los 3 primeros: Mercurio, Venus y Tierra.", " planetas"),
        ],
    },
    context=[ex("Mirando de noche, Ignacia ve un punto brillante y una luz grande y redonda con manchas. Una persona de su casa le dice que una es un planeta y la otra la Luna. ¿Cuál gira alrededor de la Tierra?", "La Luna", "Es el cuerpo que gira alrededor de nuestro planeta.")],
    selfcheck=[
        ex("¿Qué cuerpo está en el centro del Sistema Solar?", "El Sol", "Todos los demás giran a su alrededor."),
        ex("¿La Tierra es un planeta o una luna?", "Un planeta", "Gira alrededor del Sol."),
        ex("¿Qué es una órbita?", "El camino que sigue un cuerpo al girar alrededor de otro", "Es la trayectoria."),
    ],
    open_task=task(
        "Dibuja el Sistema Solar con el Sol en el centro y los ocho planetas alrededor, y rotula cada uno. Agrega una luna al lado de la Tierra, un cometa con cola y un asteroide. No necesitas respetar tamaños; escríbelo en una nota. Si no sabes el orden, usa esta lista: Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno.",
        "El Sol está al centro. Siguen Mercurio, Venus, Tierra con su Luna, Marte, Júpiter, Saturno, Urano y Neptuno. Dibujé un cometa con la cola y un asteroide entre Marte y Júpiter.",
        ["rotula los ocho planetas en orden", "agrega Sol, luna, cometa y asteroide", "nota que los tamaños no están a escala"],
        ["dibujo rotulado", "nota sobre los tamaños"],
        ["poner la Tierra en el centro", "olvidar rotular algún cuerpo"],
        "Valora el orden y pide que explique con sus palabras qué es un asteroide.",
    ),
    reinforce="Recita en voz alta el orden de los ocho planetas, desde el más cercano al Sol hasta el más lejano.",
    extend="Averigua con una persona de tu casa cuál es el planeta que más le gusta y por qué.",
)

register(
    OA11, 2,
    materials="Papel, lápiz, una regla y objetos pequeños de tu casa para comparar tamaños (una arveja o garbanzo, una pelota de tenis, una pelota grande). Usa la tabla escrita en el cuaderno.",
    use="Aprenderé a comparar los tamaños del Sol, los planetas y la Luna con un modelo a escala. Sirve para imaginar lo grande que es el Sol.",
    prior=["Sé que el Sol es una estrella y los planetas giran a su alrededor.", "Sé medir en centímetros."],
    explain=[
        "Un modelo a escala reduce los tamaños reales siempre en la misma proporción. Imagino que la Tierra mide 1 cm de ancho. Con esa escala, Júpiter mide unos 11 cm, Saturno unos 9 cm, Urano y Neptuno unos 4 cm cada uno, y el Sol unos 109 cm, más de un metro.",
        "Los planetas más pequeños son menores que la Tierra. Mercurio y Marte miden menos de 1 cm en este modelo. Venus es casi igual que la Tierra. La Luna es más chica: mide cerca de una cuarta parte de la Tierra.",
        "El Sol es enormemente más grande que los planetas. Con esta escala, en el ancho del Sol caben unas 109 Tierras en fila. Por eso decimos que el Sol es mucho más grande, y que Júpiter es el planeta más grande y Mercurio el más pequeño de los ocho.",
    ],
    vocab=[("escala", "relación que mantiene la misma proporción entre el modelo y lo real"), ("modelo", "representación de algo real, más fácil de ver"), ("diámetro", "ancho de una esfera medido por el centro"), ("proporción", "relación entre dos tamaños"), ("comparar", "buscar cuánto más grande o más chico es algo")],
    worked=[
        {"title": "Júpiter y la Tierra", "problem": "En el modelo, la Tierra mide 1 cm y Júpiter 11 cm. ¿Cuántos cm mide Júpiter más que la Tierra?", "steps": ["Júpiter: 11 cm.", "Tierra: 1 cm.", "Resto 11 − 1."], "answer": "10 cm más"},
        {"title": "Quién es mayor", "problem": "En el modelo, Saturno mide 9 cm y Neptuno 4 cm. ¿Cuál es más grande?", "steps": ["Comparo 9 y 4.", "9 es mayor que 4."], "answer": "Saturno"},
    ],
    mistakes=[
        {"wrong": "Pensar que todos los planetas son casi del tamaño de la Tierra.", "why": "En los dibujos suelen verse parecidos.", "fix": "Júpiter es unas 11 veces más ancho que la Tierra, y Mercurio es más chico."},
        {"wrong": "Pensar que el Sol es del mismo tamaño que un planeta grande como Júpiter.", "why": "Se ve parecido en dibujos.", "fix": "El Sol es unas 10 veces más ancho que Júpiter."},
    ],
    tiers={
        "recovery": [
            ex("En el modelo, ¿qué es más grande: el Sol o Júpiter?", "El Sol", "El Sol mide 109 cm y Júpiter 11 cm."),
            ex("¿Cuál es el planeta más grande del Sistema Solar?", "Júpiter", "Es el de mayor diámetro."),
            ex("Completa: en el modelo con la Tierra de 1 cm, Venus mide casi lo mismo que la ___.", "Tierra", "Venus tiene casi el mismo tamaño que la Tierra."),
        ],
        "understand": [
            ex("¿Qué es un modelo a escala?", "Una representación que mantiene la misma proporción con lo real", "Reduce todo igual para poder comparar."),
            ex("¿Por qué en un dibujo del Sistema Solar los tamaños no son reales?", "Porque no cabría en una hoja si se respetara la escala", "El Sol y los planetas son muy distintos en tamaño."),
            ex("¿Cuántas Tierras caben en una fila a lo ancho del Sol, aproximadamente?", "Unas 109", "El Sol mide unos 109 cm si la Tierra mide 1 cm."),
        ],
        "apply": [
            arith("En el modelo, el Sol mide 109 cm y Júpiter 11 cm. ¿Cuántos cm más mide el Sol que Júpiter?", "109-11", "Se resta el tamaño menor del mayor.", " cm"),
            arith("En el modelo, Saturno mide 9 cm y Urano 4 cm. Si pones los dos en fila, ¿cuántos cm miden juntos?", "9+4", "Se suman los dos anchos.", " cm"),
            ex("En el modelo, Saturno mide 9 cm, Neptuno 4 cm y la Tierra 1 cm. Ordénalos del más grande al más pequeño.", "Saturno, Neptuno, Tierra", "9 > 4 > 1."),
        ],
        "reason": [
            ex("Diego dice que la Luna es más grande que la Tierra. Con el modelo, ¿qué respondes?", "La Luna es más pequeña, como una cuarta parte de la Tierra", "En el modelo mide mucho menos de 1 cm."),
            ex("Lucía dice que Júpiter y la Tierra son casi iguales porque en un dibujo se ven parecidos. ¿Qué dato con la escala la corrige?", "Júpiter mide 11 cm y la Tierra 1 cm", "Júpiter es unas 11 veces más ancho."),
        ],
        "challenge": [
            arith("En el modelo, los cuatro planetas grandes miden 11, 9, 4 y 4 cm. Puestos en fila, ¿cuántos cm le faltan a esa fila para igualar al Sol, que mide 109 cm?", "109-11-9-4-4", "Se restan los cuatro anchos a los 109 cm del Sol.", " cm"),
            ex("La fila de los cuatro planetas grandes mide 28 cm y el Sol mide 109 cm. ¿El Sol es más ancho que esos cuatro planetas puestos en fila?", "Sí", "109 cm es mucho más que 28 cm."),
        ],
    },
    context=[ex("Para una feria de ciencias, Marta usa una pelota de 1 cm para la Tierra. ¿Qué tamaño debe tener aproximadamente el Sol y por qué le cuesta ponerlo en una mesa chica?", "Unos 109 cm; es más grande que la mesa chica", "El Sol mide más de un metro en el modelo.")],
    selfcheck=[
        ex("¿Cuál es el planeta más grande?", "Júpiter", "Su diámetro es el mayor."),
        ex("¿El Sol es más grande o más pequeño que Júpiter?", "Más grande", "Mide unos 109 cm contra 11 cm."),
        ex("¿Qué significa «a escala»?", "Que guarda la misma proporción", "Todo se reduce igual."),
    ],
    open_task=task(
        "Usa esta tabla de un modelo con la Tierra de 1 cm: Sol 109 cm, Júpiter 11 cm, Saturno 9 cm, Urano 4 cm, Neptuno 4 cm, Tierra 1 cm. Dibuja círculos con estos tamaños, o márcalos con una regla en una cartulina, y escribe tres comparaciones usando las palabras «más grande que», «más pequeño que» o «casi igual». Si no puedes dibujar el Sol completo, di cómo lo representarías.",
        "Júpiter es más grande que la Tierra. Neptuno es casi igual que Urano. El Sol es mucho más grande que Júpiter.",
        ["usa los números de la tabla", "escribe tres comparaciones correctas", "explica cómo representar el Sol si no cabe"],
        ["dibujo o tabla", "tres comparaciones escritas"],
        ["dibujar los planetas del mismo tamaño", "olvidar que el Sol es mucho mayor"],
        "Pide que lea una comparación en voz alta y que mida con la regla uno de sus círculos.",
    ),
    reinforce="Ordena de mayor a menor Sol, Júpiter, Saturno, Tierra usando la tabla, y dilo en voz alta.",
    extend="Averigua en un libro por qué Mercurio es el planeta más pequeño y cuenta lo que descubras.",
)

register(
    OA11, 3,
    materials="Un pasillo, patio o cancha donde puedas dar hasta 30 pasos en línea, tiza o papelitos para marcar y la tabla del cuaderno. Anda caminando con cuidado y sin correr.",
    use="Aprenderé a ordenar los planetas según su distancia al Sol con un modelo a escala. Sirve para entender lo lejos que están los cuerpos del Sistema Solar.",
    prior=["Sé el orden de los ocho planetas.", "Sé comparar números hasta 100."],
    explain=[
        "Los planetas están a distintas distancias del Sol. Mercurio es el más cercano y Neptuno el más lejano. La distancia de la Tierra al Sol es de unos 150 millones de kilómetros.",
        "Para imaginar las distancias hago un modelo con pasos. Pongo al Sol en un extremo y a la Tierra a 1 paso. Con la misma escala, Júpiter queda a unos 5 pasos, Saturno a unos 10, Urano a unos 20 y Neptuno a unos 30. Mercurio y Venus quedan a menos de 1 paso, y Marte entre 1 y 2 pasos. Son valores aproximados.",
        "Esto muestra que las distancias entre los planetas son enormes y que no están repartidos parejo: los cuatro primeros planetas están cerca del Sol y los cuatro últimos están muy lejos entre sí. La luz del Sol tarda unos 8 minutos en llegar a la Tierra, y unas 4 horas en llegar a Neptuno.",
    ],
    vocab=[("distancia", "cuánto separa dos cuerpos"), ("aproximado", "casi exacto, pero no con todos los detalles"), ("cercano", "que está cerca"), ("lejano", "que está lejos"), ("millón", "mil veces mil; 1.000.000")],
    worked=[
        {"title": "Neptuno y Júpiter", "problem": "En el modelo, Neptuno está a 30 pasos del Sol y Júpiter a 5 pasos. ¿Cuántos pasos hay entre ellos?", "steps": ["Neptuno: 30 pasos.", "Júpiter: 5 pasos.", "30 − 5 = 25."], "answer": "25 pasos"},
        {"title": "Cuál está más cerca", "problem": "Entre Marte y Saturno, ¿cuál está más cerca del Sol?", "steps": ["En el orden, Marte viene antes que Saturno.", "Está más cerca del Sol."], "answer": "Marte"},
    ],
    mistakes=[
        {"wrong": "Pensar que los planetas están a la misma distancia unos de otros.", "why": "En los dibujos se ven repartidos parejo.", "fix": "Las distancias aumentan mucho hacia afuera; entre Saturno y Neptuno hay mucho más espacio que entre Mercurio y Venus."},
        {"wrong": "Creer que Venus está más lejos del Sol que la Tierra.", "why": "Se olvida el orden de los planetas.", "fix": "El orden desde el Sol es Mercurio, Venus, Tierra: Venus está más cerca."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es el planeta más cercano al Sol?", "Mercurio", "Es el primero en el orden."),
            ex("¿Cuál es el planeta más lejano del Sol?", "Neptuno", "Es el octavo."),
            ex("Completa: la Tierra está a 1 paso del Sol en el modelo; Júpiter está más ___.", "lejos", "Está a unos 5 pasos."),
        ],
        "understand": [
            ex("¿Por qué se usa un modelo con pasos para las distancias?", "Porque las distancias reales son demasiado grandes para verlas", "El modelo las reduce a una escala que se puede caminar."),
            ex("En el modelo, ¿los planetas están a distancias parejas entre sí?", "No", "Las distancias crecen mucho hacia afuera."),
            ex("¿Cuánto tarda la luz del Sol en llegar a la Tierra?", "Unos 8 minutos", "Es un tiempo aproximado muy corto comparado con la distancia."),
        ],
        "apply": [
            arith("En el modelo, Saturno está a 10 pasos y Júpiter a 5. ¿Cuántos pasos hay entre ellos?", "10-5", "Se resta la distancia menor a la mayor.", " pasos"),
            arith("Neptuno está a 30 pasos del Sol y Urano a 20. ¿Cuántos pasos hay entre ellos?", "30-20", "Se restan las distancias.", " pasos"),
            ex("Ordena del más cercano al más lejano del Sol: Júpiter, Venus, Neptuno.", "Venus, Júpiter, Neptuno", "Ese es el orden de distancia al Sol."),
        ],
        "reason": [
            ex("Un compañero dice que Marte está más lejos del Sol que Júpiter. Con el modelo, ¿tiene razón?", "No", "Marte está entre 1 y 2 pasos y Júpiter a unos 5."),
            ex("En el modelo, ¿la Tierra queda a más o a menos de 2 pasos del Sol?", "A menos de 2 pasos", "La Tierra está a 1 paso."),
        ],
        "challenge": [
            ex("Neptuno está mucho más lejos del Sol que la Tierra. ¿Recibe más o menos luz y calor del Sol que la Tierra?", "Menos", "A más distancia del Sol llega menos luz y calor."),
            arith("Un modelo pone a Neptuno a 30 pasos del Sol y otro grupo lo pone a 15 pasos por error. ¿Cuántos pasos se equivocaron?", "30-15", "Se restan los dos números de pasos.", " pasos"),
        ],
    },
    context=[ex("Isabel camina por un pasillo con 30 pasos y marca a Neptuno en el último. Pone a la Tierra en el paso 1. ¿Dónde debería poner a Júpiter: cerca del paso 5 o del paso 25?", "Cerca del paso 5", "Júpiter está a unos 5 pasos del Sol.")],
    selfcheck=[
        ex("¿Qué planeta está más cerca del Sol?", "Mercurio", "Es el primero."),
        ex("¿Qué planeta está más lejos del Sol?", "Neptuno", "Es el octavo."),
        ex("En el modelo, ¿la Tierra está a cuántos pasos del Sol?", "1 paso", "Es la unidad del modelo."),
    ],
    open_task=task(
        "Con un papel largo o en un pasillo, marca el Sol y los planetas con esta tabla de pasos aproximados: Mercurio y Venus menos de 1, Tierra 1, Marte entre 1 y 2, Júpiter 5, Saturno 10, Urano 20, Neptuno 30. Si no puedes caminar, dibuja una línea con una escala: cada centímetro es un paso. Escribe cuál planeta quedó más lejos y cuál más cerca del Sol.",
        "Marqué el Sol en 0 y Neptuno a 30. El más cercano es Mercurio y el más lejano Neptuno.",
        ["marca en orden correcto los ocho planetas", "usa la tabla de pasos", "nombra el más cercano y el más lejano"],
        ["línea o recorrido marcado", "frase con cercano y lejano"],
        ["poner a Venus más lejos que la Tierra", "repartir los planetas a igual distancia"],
        "Valora la línea y pide que explique por qué los últimos planetas quedan tan separados.",
    ),
    reinforce="Camina los 30 pasos del modelo diciendo el nombre de cada planeta cuando llegues a su marca.",
    extend="Pregunta en casa cuánto tiempo cree la gente que tardaría un auto en llegar al Sol y compara con la idea de que la luz tarda 8 minutos.",
)

register(
    OA11, 4,
    materials="Papel, lápices de colores y la tabla de apariencia del cuaderno. Opcional: un libro o una pantalla con fotos del Sistema Solar con ayuda de una persona adulta. Nunca mires directamente al Sol.",
    use="Aprenderé cómo se ven algunos cuerpos del Sistema Solar y por qué los dibujos no muestran los tamaños y distancias reales. Sirve para leer mejor imágenes de ciencia.",
    prior=["Sé distinguir estrellas, planetas, lunas, cometas y asteroides.", "Sé que los modelos tienen escala."],
    explain=[
        "Cada cuerpo tiene una apariencia propia. El Sol es una esfera muy brillante. Marte se ve rojizo porque su suelo tiene hierro oxidado. Júpiter tiene bandas de nubes y una gran mancha. Saturno tiene anillos de hielo y roca. La Luna es gris con cráteres, que son huecos redondos. Los cometas muestran una cola brillante, y los asteroides son rocas de formas irregulares.",
        "La cola de un cometa se forma cuando se acerca al Sol y el hielo se calienta. La cola siempre apunta en dirección contraria al Sol. Cuando el cometa se aleja, la cola desaparece.",
        "Los dibujos tienen límites. Si dibujo el Sistema Solar en una hoja, no puedo respetar a la vez los tamaños y las distancias: los planetas se verían como puntos casi invisibles o los dibujaría mucho más cerca de lo real. Además, algunas fotos tienen colores ajustados. Por eso un dibujo del Sistema Solar es una representación, no una copia exacta.",
    ],
    vocab=[("cráter", "hueco redondo en la superficie de un cuerpo"), ("anillo", "banda delgada de hielo y roca que rodea a un planeta"), ("cola", "chorro de gas y polvo de un cometa"), ("representación", "dibujo o modelo que muestra algo real"), ("límite", "lo que un modelo no puede mostrar bien")],
    worked=[
        {"title": "Reconocer por su apariencia", "problem": "Un planeta tiene anillos grandes que lo rodean. ¿Cuál es?", "steps": ["Los anillos más visibles son de Saturno.", "Júpiter, Urano y Neptuno tienen anillos finos, pero los de Saturno son los más claros."], "answer": "Saturno"},
        {"title": "Límite de un dibujo", "problem": "En un dibujo, la Tierra y el Sol tienen casi el mismo tamaño. ¿Qué límite tiene ese dibujo?", "steps": ["El Sol es unas 109 veces más ancho que la Tierra.", "El dibujo no respeta la escala.", "Muestra el orden, pero no los tamaños reales."], "answer": "No respeta la escala de tamaños"},
    ],
    mistakes=[
        {"wrong": "Pensar que la cola de un cometa va hacia atrás por donde va el cometa.", "why": "Se imagina como la estela de un avión.", "fix": "La cola apunta siempre lejos del Sol."},
        {"wrong": "Creer que las fotos del espacio muestran siempre los colores exactos que verías.", "why": "Se piensa que son fotos comunes.", "fix": "Algunas imágenes tienen colores ajustados para ver mejor los detalles."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué cuerpo se ve rojizo en el cielo: Marte o Júpiter?", "Marte", "Su suelo tiene hierro oxidado."),
            ex("¿Qué planeta tiene anillos muy visibles?", "Saturno", "Sus anillos se ven claramente."),
            ex("Completa: la Luna tiene huecos redondos llamados ___.", "cráteres", "Son huecos redondos en su superficie."),
        ],
        "understand": [
            ex("¿Por qué un cometa tiene cola?", "Porque al acercarse al Sol su hielo se calienta y suelta gas y polvo", "La cola aparece por el calor del Sol."),
            ex("¿Hacia dónde apunta la cola de un cometa?", "Lejos del Sol", "Siempre apunta en dirección contraria al Sol."),
            ex("¿Por qué Marte se ve rojizo?", "Porque su suelo tiene hierro oxidado", "El óxido le da el color rojizo."),
        ],
        "apply": [
            ex("Un cuerpo es gris y tiene muchos huecos redondos. ¿Es la Luna o Júpiter?", "La Luna", "Los cráteres son de la Luna."),
            ex("Un cuerpo es una roca de forma irregular, sin atmósfera ni cola. ¿Es un asteroide o un cometa?", "Un asteroide", "Los asteroides son rocas irregulares sin cola."),
            ex("Un dibujo muestra todos los planetas del mismo tamaño y pegados. ¿Qué dos cosas no respeta?", "Los tamaños y las distancias", "Los planetas tienen tamaños y distancias muy distintos."),
        ],
        "reason": [
            ex("Ana dice que un dibujo de la Tierra y el Sol del mismo tamaño muestra el tamaño real. ¿Qué respondes?", "Es una representación, no respeta la escala", "El Sol es mucho más grande."),
            ex("Un cometa se aleja del Sol y su cola se hace pequeña. ¿Por qué?", "Porque con menos calor suelta menos gas y polvo", "La cola se debe al calor del Sol."),
        ],
        "challenge": [
            ex("¿Por qué no se puede hacer un dibujo en una hoja que muestre a la vez los tamaños y las distancias reales?", "Porque los planetas serían puntos casi invisibles o las distancias no cabrían", "Las distancias son enormes comparadas con los tamaños."),
            ex("Un cuerpo muestra bandas de nubes y una gran mancha. ¿Es Júpiter o la Luna?", "Júpiter", "Las bandas de nubes y la gran mancha son de Júpiter; la Luna tiene cráteres."),
        ],
    },
    context=[ex("En una foto, Pedro ve un cuerpo con cola brillante cerca del Sol. La cola apunta hacia la derecha y el Sol está a la izquierda del cometa. ¿Está bien dibujada la cola?", "Sí, porque apunta lejos del Sol", "La cola siempre se aleja del Sol.")],
    selfcheck=[
        ex("¿Qué planeta es famoso por sus anillos?", "Saturno", "Sus anillos son los más visibles."),
        ex("¿Qué tiene la Luna en su superficie?", "Cráteres", "Son huecos redondos."),
        ex("¿Un dibujo del Sistema Solar puede mostrar los tamaños y distancias reales?", "No", "Tendría que ser enorme."),
    ],
    open_task=task(
        "Completa esta tabla con una palabra de apariencia para cada cuerpo: Sol, Marte, Júpiter, Saturno, Luna, cometa, asteroide. Usa estas pistas: muy brillante, rojizo, bandas de nubes, anillos, cráteres, cola, roca irregular. Luego escribe un límite que tiene tu dibujo del Sistema Solar.",
        "Sol: muy brillante. Marte: rojizo. Júpiter: bandas. Saturno: anillos. Luna: cráteres. Cometa: cola. Asteroide: roca irregular. Mi dibujo no muestra los tamaños reales.",
        ["relaciona cada cuerpo con su apariencia", "usa las pistas dadas", "escribe un límite del dibujo"],
        ["tabla completa", "frase del límite"],
        ["intercambiar pistas", "no escribir ningún límite"],
        "Valora la tabla y pide que explique una pista con una frase.",
    ),
    reinforce="Elige un cuerpo del Sistema Solar y describe cómo se ve sin decir su nombre. Pide que adivinen cuál es.",
    extend="Busca con una persona adulta una foto de Saturno y cuenta qué detalles de su apariencia notas.",
)

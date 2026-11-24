"""Ciencias Naturales EPJA Básica N2, módulo 3 (parte 1): OAD-09, observar y describir procesos energéticos del entorno (manifestaciones, transformaciones, fuentes y recursos energéticos en Chile). Todo en papel; las observaciones y los datos son inventados y rotulados «de ejemplo»; no se hacen experimentos."""
from __future__ import annotations

from hc_common import make_build


MATERIALS = ("Papel, lápiz y goma. Todas las observaciones, tablas y datos están escritos en cada ejercicio y son de ejemplo, inventados para este cuaderno. "
             "No se ejecuta ningún experimento ni se manipula electricidad de la red, fuego ni sustancias: solo se leen y se analizan descripciones. "
             "Si algo te cuesta leer, pide apoyo a quien te acompañe.")
build = make_build(MATERIALS)

O = "EPJA-CNAT-NB2-OAD-09"
PRIOR = ["Ya uso aparatos, cocinas, estufas y luz en mi vida diaria y noto sus efectos.", "Sé leer tablas sencillas y sumar y restar números pequeños."]

# ============================================================ clase 1
F = ("Ficha 1 (observación de ejemplo en una cocina). Un hervidor eléctrico calienta agua y al final silba. Una ampolleta ilumina la mesa. "
     "Un ventilador mueve el aire. Una persona bate una masa con una cuchara.")
build(
    O, 1, F,
    use="Hoy observo lo que pasa a mi alrededor y reconozco dónde hay energía, por los cambios que produce.",
    prior=PRIOR,
    explain=[
        "La energía no se ve ni se toca, pero se nota por lo que hace. Cuando algo se calienta, se mueve, se ilumina o suena, hay energía actuando. Tú ya la notas cada día: la estufa que calienta, la ampolleta que alumbra, la radio que suena.",
        "Observar es mirar con atención usando los sentidos: la vista, el oído, el tacto y el olfato. Describir es contar con palabras claras qué se observó, sin mezclar lo que se ve con lo que uno opina. Por ejemplo: «El hervidor calienta el agua y silba».",
        "Un proceso energético es una situación en la que la energía produce cambios. Para describirlo conviene anotar qué aparato o cuerpo participa, qué efecto produce (calor, luz, sonido, movimiento) y en qué momento ocurre.",
    ],
    vocab=[("energía", "lo que permite que algo cambie: se mueva, se caliente, ilumine o suene"), ("observar", "mirar con atención usando los sentidos"), ("proceso energético", "situación en que la energía produce cambios"), ("efecto", "cambio que se nota")],
    worked=[
        ("Describir con la ficha", F, ["Busco qué aparato participa en cada caso: hervidor, ampolleta, ventilador, persona.", "Anoto el efecto de cada uno: calienta y silba, ilumina, mueve el aire, mueve la masa."], "Hay cuatro procesos energéticos: calor y sonido, luz, movimiento del aire y movimiento de la masa"),
        ("Separar observación y opinión", "Una persona anota: «La estufa calienta la pieza y huele a polvo. Qué estufa más fea.»", ["«Calienta la pieza» y «huele a polvo» se perciben con los sentidos.", "«Qué estufa más fea» es una opinión, no una observación."], "Las observaciones son «calienta la pieza» y «huele a polvo»"),
    ],
    mistakes=[("Decir que no hay energía porque no se ve.", "La energía se reconoce por sus efectos, no porque se vea.", "Pregúntate qué cambio produce: calor, luz, sonido o movimiento."),
              ("Mezclar opinión con observación: «el hervidor es muy ruidoso y molesto».", "«Molesto» es lo que siente quien observa; no se puede comprobar igual para todos.", "Describe lo medible o visible: «el hervidor silba al hervir».")],
    T=[
        ("abc", "{F} ¿Qué cambio produce el hervidor sobre el agua?", "La calienta", "La ilumina", "La mueve como el viento", "El agua sube de temperatura; la luz la da la ampolleta y el aire lo mueve el ventilador."),
        ("ab", "Para este cuaderno, ¿qué es la energía?", "Lo que permite que algo cambie, se mueva, se caliente, ilumine o suene", "Un objeto que se guarda dentro de los enchufes", "La energía no es un objeto: se reconoce por los cambios que produce."),
        ("=", "{F} De los cuatro elementos de la ficha (hervidor, ampolleta, ventilador y persona con cuchara), ¿cuántos NO son aparatos eléctricos?", "4-3", "Hay cuatro elementos y tres son aparatos eléctricos, así que queda uno que no lo es.", " elemento"),
        ("abc", "Una radio encendida suena. ¿Qué manifestación de la energía percibes con el oído?", "Sonido", "Luz", "Calor", "El oído percibe el sonido; la luz se ve y el calor se siente en la piel."),
        ("ab", "Una persona dice: «Si no veo la energía, no existe». ¿Qué respuesta es correcta?", "La energía se reconoce por sus efectos: luz, calor, movimiento o sonido", "Solo existe cuando se puede tocar con la mano", "Aunque la energía no se vea, sus efectos sí se pueden observar y describir."),
        ("abc", "{F} Cuando la persona bate la masa, ¿qué manifestación de la energía aparece?", "Movimiento de la cuchara y de la masa", "Luz de la ampolleta", "Calor del hervidor", "Batir es mover, por eso la manifestación es el movimiento."),
        ("abc", "Se anotan estos aparatos: estufa (calienta), parlante (suena), linterna (alumbra), batidora (mueve). ¿Cuál se usa para producir luz?", "La linterna", "El parlante", "La estufa", "La linterna alumbra; el parlante suena y la estufa calienta."),
        ("abc", "Un secador de pelo de ejemplo mueve aire y lo calienta. ¿Qué dos efectos de la energía aparecen?", "Movimiento y calor", "Luz y sonido", "Solo luz", "El aire en movimiento es movimiento y el aire tibio es calor."),
        ("=", "En una pieza hay 2 ampolletas encendidas y 1 televisor encendido, todos eléctricos. ¿Cuántos aparatos están usando energía eléctrica?", "2+1", "Se suman las dos ampolletas y el televisor, porque los tres están encendidos.", " aparatos"),
        ("ab", "Ana anota «el hervidor está caliente y silba». Luis anota «el hervidor es lindo». ¿Quién describe un proceso energético?", "Ana, porque nombra calor y sonido", "Luis, porque da su opinión", "Calor y sonido son efectos de la energía; «lindo» no describe ningún cambio."),
        ("abc", "Un grupo dice: «Al apagar la estufa, la energía desaparece sin dejar rastro». ¿Qué observación lo contradice mejor?", "La pieza sigue tibia un rato, porque el calor pasó al aire y a los objetos", "La estufa pesa más", "El enchufe cambia de color", "Que la pieza siga tibia muestra que la energía térmica pasó a otros cuerpos."),
        ("abc", "Observación: «Al encender un ventilador, un papel liviano se mueve y el motor queda tibio». ¿Qué dos manifestaciones hay?", "Movimiento y calor", "Luz y sonido", "Electricidad y luz", "El papel se mueve (movimiento) y el motor se entibia (calor)."),
        ("ab", "Quieres describir bien un proceso energético. ¿Qué anotación sirve más?", "El aparato, el efecto que produce y cuánto tiempo dura", "Solo el nombre del aparato", "Una descripción completa nombra quién participa, qué efecto produce y cuándo."),
    ],
    ctx=("abc", "En una sala de espera hay una estufa encendida, una radio con música y una lámpara. Una vecina te pide que anotes tres observaciones. ¿Cuál lista es correcta?", "La estufa calienta, la radio suena y la lámpara ilumina", "La estufa suena, la radio ilumina y la lámpara calienta", "La estufa es fea, la radio es vieja y la lámpara es cara", "La primera lista une cada aparato con su efecto real; la tercera solo da opiniones."),
    sc=[("En Ciencias: ¿cómo se reconoce la energía?", "Por los cambios que produce: calor, luz, sonido o movimiento", "La energía no se ve, pero sus efectos sí se observan."),
        ("¿Qué diferencia hay entre observar y opinar?", "Observar es describir lo que se percibe; opinar es dar un juicio personal", "Una observación se puede comprobar; una opinión depende de quien la dice."),
        ("¿Qué datos conviene anotar de un proceso energético?", "El aparato, el efecto y el momento", "Con esos tres datos otra persona puede entender lo observado.")],
    op=("Elige una de estas tres escenas de ejemplo y descríbela en cuatro líneas: (a) un secador de ropa eléctrico que gira y calienta, (b) una cocina a gas encendida que calienta una olla, (c) una radio que suena en una feria. Anota qué aparato participa, qué efectos se notan y en qué momento. Separa lo que observas de lo que opinas.",
        "Escena (c): La radio suena durante la feria (sonido). Se nota porque la gente conversa más alto. Opinión: la música es agradable.",
        ["nombra el aparato", "anota al menos un efecto de la energía", "separa observación y opinión"],
        ["cuatro líneas escritas en el cuaderno"],
        ["anotar solo opiniones", "no decir qué efecto se nota"],
        "Pregunta: «¿Qué cambio se nota y cómo lo sabes?» y «¿esto lo podría ver cualquier persona o es tu opinión?»."),
    reinforce="Mira tres aparatos de tu casa y escribe qué efecto de la energía produce cada uno.",
    extend="Escribe dos observaciones de procesos energéticos que ocurren fuera de casa, por ejemplo en la calle o en una plaza.",
)

# ============================================================ clase 2
F = ("Ficha 2 (tabla de ejemplo). Objeto | Qué se le entrega | Qué se nota. "
     "Ampolleta | electricidad | luz y un poco de calor. Parlante | electricidad | sonido. Cocina a gas | gas | calor. "
     "Bicicleta | fuerza de las piernas | movimiento. Pila de linterna | sustancias guardadas en su interior | electricidad.")
build(
    O, 2, F,
    use="Hoy aprendo los nombres de las manifestaciones de la energía y tres de sus propiedades.",
    prior=PRIOR + ["Reconozco que la energía se nota por sus efectos."],
    explain=[
        "La energía se manifiesta de distintas formas. La energía luminosa es la luz; la térmica es el calor; la sonora es el sonido; la eléctrica es la que circula por cables y pilas; y la de movimiento es la que tiene un cuerpo que se desplaza. La energía química está guardada en los alimentos, la leña, los combustibles y las pilas.",
        "La energía tiene propiedades que ayudan a describirla. Se transfiere: pasa de un cuerpo a otro, como el calor de una olla a tus manos. Se transforma: cambia de una forma a otra, como la eléctrica que en una ampolleta pasa a luz y calor.",
        "Una tercera propiedad es que, al transformarse, no desaparece: pasa a otra forma o a otros cuerpos, aunque a veces ya no sea útil, como el calor que se escapa al aire. Con estos nombres puedes describir con precisión lo que observas.",
    ],
    vocab=[("energía luminosa", "luz"), ("energía térmica", "calor"), ("energía sonora", "sonido"), ("energía eléctrica", "la que circula por cables y pilas"), ("energía química", "la guardada en alimentos, leña, combustibles y pilas"), ("transferir", "pasar de un cuerpo a otro")],
    worked=[
        ("Nombrar la manifestación", F, ["Miro la fila del parlante: se nota sonido.", "El sonido se llama energía sonora."], "El parlante produce energía sonora a partir de electricidad"),
        ("Transferencia", "Una persona sostiene una taza con té caliente y siente que las manos se le entibian.", ["El té está más caliente que las manos.", "El calor pasa del té a las manos."], "Hubo transferencia de energía térmica de la taza a las manos"),
    ],
    mistakes=[("Llamar «energía eléctrica» a todo lo que se enchufa.", "Lo que se enchufa recibe energía eléctrica, pero produce otra manifestación: luz, calor o sonido.", "Distingue lo que entra al aparato de lo que se nota que sale."),
              ("Creer que si el calor se escapa al aire, la energía se acabó.", "La energía térmica pasó al aire; no desapareció, aunque ya no sirva para lo que se quería.", "Sigue el camino de la energía: ¿a qué cuerpo pasó?")],
    T=[
        ("abc", "{F} ¿Qué manifestación de la energía se nota en la cocina a gas?", "Calor, o energía térmica", "Sonido, o energía sonora", "Luz, o energía luminosa", "La tabla dice que la cocina a gas produce calor, y el calor es energía térmica."),
        ("ab", "¿Qué nombre recibe el calor como manifestación de la energía?", "Energía térmica", "Energía luminosa", "El calor corresponde a la energía térmica; la luminosa es la luz."),
        ("abc", "{F} ¿Qué se nota en la bicicleta?", "Movimiento", "Luz", "Sonido de radio", "La tabla dice que la bicicleta produce movimiento."),
        ("abc", "¿Dónde está guardada la energía química?", "En los alimentos, la leña y las pilas", "En el sonido de una radio", "En la luz de una ventana", "Los alimentos, la leña y las pilas guardan energía química hasta que se usan."),
        ("ab", "{F} ¿Qué aparato de la tabla recibe gas?", "La cocina", "La ampolleta", "Según la tabla, la cocina a gas es el objeto al que se entrega gas."),
        ("abc", "Un cable lleva energía a una lámpara. ¿Qué manifestación circula por el cable?", "Energía eléctrica", "Energía sonora", "Energía de movimiento", "La que circula por cables y pilas es la energía eléctrica."),
        ("abc", "{F} ¿En cuál de los objetos de la tabla se nota más de una manifestación?", "En la ampolleta, que da luz y calor", "En el parlante", "En la bicicleta", "Solo la ampolleta muestra dos efectos en la tabla: luz y calor."),
        ("ab", "Un termo con agua caliente se deja en una mesa fría y después de un rato el agua se enfría. ¿Qué ocurrió?", "Se transfirió energía térmica del agua al aire y a la mesa", "La energía térmica dejó de existir", "El calor pasó de lo más caliente a lo más frío y no desapareció."),
        ("=", "Una pila de ejemplo entrega energía durante 4 horas por día. ¿Cuántas horas entrega en 3 días?", "4*3", "Se repiten 4 horas durante 3 días, así que se multiplica.", " horas"),
        ("abc", "Una lámpara transforma energía eléctrica en luz. ¿Qué propiedad de la energía se muestra?", "Se transforma", "Se acaba", "Se vuelve sonido", "Pasar de eléctrica a luz es un cambio de forma, es decir, una transformación."),
        ("abc", "{F} Una persona dice que la pila de linterna «no tiene energía hasta que se enchufa». ¿Qué corrección es correcta?", "La pila guarda energía química y la entrega como eléctrica", "La pila solo es de plástico", "La pila produce sonido", "Según la tabla la pila guarda sustancias en su interior, que es energía química."),
        ("abc", "Observas que una olla caliente entibia la mesa donde se apoya. ¿Cuál afirmación es correcta?", "La energía térmica se transfirió de la olla a la mesa", "La mesa produjo energía térmica de la nada", "La olla perdió energía y no fue a ninguna parte", "El calor pasa de lo caliente a lo frío: de la olla a la mesa."),
        ("ab", "Un radio portátil funciona con pilas y suena. ¿Qué cadena de formas es correcta?", "Química en la pila, eléctrica en el circuito y sonora en el parlante", "Sonora en la pila, luminosa en el circuito y química en el parlante", "La pila guarda energía química y el parlante entrega sonido."),
    ],
    ctx=("abc", "En una feria venden velas eléctricas de ejemplo con pilas. Una persona pregunta de qué forma es la energía que hace brillar la vela. ¿Qué respondes?", "Es energía luminosa que viene de energía química guardada en las pilas", "Es energía sonora que sale de la pila", "Es energía de movimiento de la vela", "Brillar es luz, y la pila entrega la energía que tenía guardada."),
    sc=[("En Ciencias: ¿qué es la energía térmica?", "El calor", "La energía térmica es la manifestación que sentimos como calor."),
        ("¿Qué significa que la energía se transfiere?", "Pasa de un cuerpo a otro", "Como el calor que pasa de una olla a las manos."),
        ("¿Dónde está guardada la energía química?", "En alimentos, leña, combustibles y pilas", "Estos materiales almacenan energía que se libera al usarlos.")],
    op=("Elige tres objetos de una cocina de ejemplo (por ejemplo: refrigerador, tetera eléctrica y lámpara). Para cada uno escribe qué se le entrega y qué manifestación de la energía se nota. Después escribe una frase con la palabra «transferir».",
        "Lámpara: se le entrega electricidad y se nota luz. Frase: el calor se transfiere de la olla a la mesa.",
        ["los tres objetos tienen entrada y salida", "usa los nombres de las manifestaciones", "la frase usa «transferir» correctamente"],
        ["una tabla de tres filas y una frase"],
        ["escribir solo la entrada sin la salida", "usar «transferir» para algo que no pasa de un cuerpo a otro"],
        "Pregunta: «¿Qué entra y qué sale?» y «¿de qué cuerpo a qué cuerpo pasa?»."),
    reinforce="Haz una lista de cinco cosas de tu casa y escribe qué forma de energía se nota en cada una.",
    extend="Explica con tus palabras por qué el calor de una taza no «desaparece» cuando se enfría el té.",
)

# ============================================================ clase 3
F = ("Ficha 3 (cadenas de ejemplo). Ampolleta de filamento: entra electricidad; sale luz y mucho calor. "
     "Licuadora: entra electricidad; sale movimiento de las aspas, sonido y calor. "
     "Persona que camina: entran alimentos (energía química); sale movimiento y calor del cuerpo. "
     "Panel solar: entra luz del Sol; sale electricidad.")
build(
    O, 3, F,
    use="Hoy sigo, paso a paso, cómo la energía cambia de forma en un aparato y cuánta se aprovecha.",
    prior=PRIOR + ["Conozco los nombres de las manifestaciones de la energía."],
    explain=[
        "Para describir una transformación de energía sigue tres pasos. Paso 1: ¿qué energía entra? Paso 2: ¿qué energía útil sale, o sea la que buscamos? Paso 3: ¿qué otra sale sin que la busquemos, como el calor que se escapa?",
        "Casi siempre, al transformarse, una parte de la energía sale como calor que no sirve para lo que queríamos. Por eso una ampolleta antigua se calienta mucho: su energía útil es la luz, pero parte importante sale como calor.",
        "También los seres vivos transforman energía: el cuerpo toma energía química de los alimentos y la convierte en movimiento y en calor corporal. Y un panel solar transforma luz del Sol en electricidad.",
    ],
    vocab=[("transformación", "cambio de una forma de energía a otra"), ("energía útil", "la que buscamos al usar un aparato"), ("energía perdida", "la que sale sin que la busquemos, casi siempre calor"), ("entrada y salida", "lo que se entrega al aparato y lo que se obtiene")],
    worked=[
        ("Los tres pasos", F, ["Elijo la licuadora. Entrada: electricidad.", "Energía útil: movimiento de las aspas.", "Salen además sonido y calor, que no buscamos."], "Electricidad pasa a movimiento (útil), sonido y calor"),
        ("Un dato de ejemplo", "De cada 10 unidades de energía eléctrica que recibe una ampolleta de filamento de ejemplo, 1 sale como luz y el resto como calor.", ["Total que entra: 10.", "Luz: 1. Calor: 10 menos 1."], "9 unidades salen como calor"),
    ],
    mistakes=[("Decir que la energía eléctrica «se gasta» y se acaba al usar un aparato.", "La energía se transforma; lo que parece gasto es que se convierte en formas que ya no usamos.", "Sigue la cadena: ¿en qué formas salió?"),
              ("Anotar solo la energía útil y olvidar el calor.", "Casi todas las transformaciones sueltan algo de calor.", "Agrega siempre el paso 3: lo que sale sin buscarlo.")],
    T=[
        ("abc", "{F} ¿Qué energía entra a la licuadora?", "Eléctrica", "Luminosa", "Química", "La ficha dice que a la licuadora entra electricidad."),
        ("ab", "{F} ¿Cuál es la energía útil de la ampolleta de filamento?", "La luz", "El calor", "La ampolleta se usa para alumbrar, así que su energía útil es la luz."),
        ("=", "{F} ¿Cuántas formas de energía salen de la licuadora (movimiento, sonido y calor)?", "1+1+1", "Se cuenta cada manifestación que la ficha nombra como salida.", " formas"),
        ("abc", "{F} ¿Qué energía transforma el panel solar?", "Luz del Sol en electricidad", "Electricidad en luz", "Sonido en calor", "Según la ficha, entra luz del Sol y sale electricidad."),
        ("ab", "Una ampolleta de ejemplo recibe 20 unidades de energía eléctrica y entrega 4 como luz. ¿Cómo se llama el resto?", "Energía perdida, casi toda en forma de calor", "Energía útil", "Lo que no sale como luz se escapa como calor y no es lo que buscamos."),
        ("=", "Una ampolleta de ejemplo recibe 20 unidades de energía eléctrica y entrega 4 como luz. ¿Cuántas unidades salen como calor?", "20-4", "Se resta la energía útil del total que entra.", " unidades"),
        ("abc", "{F} Una persona camina. ¿Cuál es la entrada de energía?", "Los alimentos, con su energía química", "El sonido de los pasos", "La luz de la calle", "El cuerpo usa la energía química de lo que come."),
        ("abc", "Un secador de pelo de ejemplo recibe electricidad y entrega aire en movimiento y calor. ¿Cuál es su energía útil?", "Calor y movimiento del aire, para secar", "Solo sonido", "Solo luz", "Se usa para secar con aire tibio; el sonido es lo que sale sin buscarlo."),
        ("ab", "Una linterna de pilas funciona 10 minutos y la pila queda tibia. ¿Qué explica la pila tibia?", "Parte de la energía salió como calor", "La pila produjo luz extra", "Una parte de toda transformación sale como calor, como indica el paso 3."),
        ("abc", "{F} Se compara una ampolleta de filamento con otra moderna de ejemplo que se calienta menos. ¿Cuál afirmación es razonable?", "La moderna convierte más energía eléctrica en luz y pierde menos como calor", "La moderna produce más calor que luz", "Las dos pierden exactamente lo mismo", "Si se calienta menos, pierde menos energía como calor y aprovecha más."),
        ("=", "Un panel solar de ejemplo recibe 50 unidades de luz y entrega 10 unidades de electricidad. ¿Cuántas unidades no se convirtieron en electricidad?", "50-10", "Las unidades que no se aprovechan son la diferencia entre lo que entra y lo útil.", " unidades"),
        ("abc", "Alguien afirma: «Cuando uso la licuadora, la energía eléctrica se acaba y no queda nada». ¿Qué observación lo contradice?", "El motor queda tibio y la licuadora suena: la energía pasó a calor y sonido", "La licuadora tiene botón", "El cable es largo", "Calor y sonido son formas en que salió parte de la energía."),
        ("ab", "Para describir bien un aparato, ¿qué orden de pasos conviene?", "Energía que entra, energía útil que sale y energía que se pierde", "Color del aparato, precio y marca", "El orden entrada, útil y pérdida describe toda la transformación."),
    ],
    ctx=("abc", "En un taller comunitario comparan dos estufas de ejemplo. Ambas reciben la misma electricidad, pero una calienta mucho la pieza y la otra solo la tibia, y se nota que su cable se calienta bastante. ¿Qué conviene concluir?", "La segunda pierde más energía como calor fuera de la pieza", "La segunda produce más luz", "Las dos son iguales sin importar lo observado", "Si el cable se calienta mucho, parte de la energía salió como calor sin servir en la pieza."),
    sc=[("En esta clase: ¿qué es la energía útil de un aparato?", "La que buscamos al usar un aparato", "Es la parte de la transformación que sirve para nuestro objetivo."),
        ("En Ciencias: ¿qué suele salir además de la energía útil?", "Calor", "Casi toda transformación suelta algo de energía térmica."),
        ("¿Qué energía transforma el cuerpo al caminar?", "La química de los alimentos", "El cuerpo usa energía química para moverse y mantenerse tibio.")],
    op=("Elige un aparato de esta lista de ejemplo: radio de pilas, plancha eléctrica o cargador de celular. Escribe la energía que entra, la energía útil que sale y la que se pierde. Haz un esquema con flechas y explícalo en voz alta a otra persona.",
        "Radio de pilas: entra energía química guardada en la pila, sale sonido (útil) y calor (se pierde).",
        ["indica la entrada", "indica la salida útil", "indica la energía que se pierde"],
        ["un esquema con flechas y tres rótulos"],
        ["omitir la energía perdida", "poner la flecha al revés"],
        "Pregunta: «¿Qué buscabas al usar el aparato y qué más salió?»."),
    reinforce="Elige otro aparato de tu casa y completa los tres pasos: entra, sale útil y se pierde.",
    extend="Explica por qué a veces un aparato que funciona mucho rato se siente tibio al tocarlo.",
)

# ============================================================ clase 4
F = ("Ficha 4 (lista de ejemplo de fuentes de energía). Sol; viento; agua de los ríos en movimiento; carbón; petróleo; gas natural. "
     "Dato general: el carbón, el petróleo y el gas natural se formaron durante millones de años a partir de restos de seres vivos.")
build(
    O, 4, F,
    use="Hoy practico clasificando fuentes de energía y explicando por qué unas se renuevan y otras no.",
    prior=PRIOR + ["Conozco las formas de la energía y sus transformaciones."],
    explain=[
        "Una fuente de energía es un recurso del que obtenemos energía para usarla. El Sol, el viento y el agua de los ríos son fuentes renovables: se reponen de forma natural o no se acaban cuando las usamos, al menos en la escala de la vida humana.",
        "El carbón, el petróleo y el gas natural son combustibles fósiles. Se formaron durante millones de años y, al usarlos, se consumen mucho más rápido de lo que se forman. Por eso se llaman fuentes no renovables.",
        "Elegir una fuente implica pensar en el ambiente. Quemar combustibles fósiles libera gases que contaminan el aire y aumentan el efecto invernadero; las fuentes renovables suelen tener menos impacto, aunque también necesitan espacio y cuidado.",
    ],
    vocab=[("fuente de energía", "recurso del que se obtiene energía"), ("renovable", "se repone o no se agota al usarla"), ("no renovable", "se consume más rápido de lo que se forma"), ("combustible fósil", "carbón, petróleo o gas natural, formados en millones de años")],
    worked=[
        ("Clasificar", F, ["Pregunto de cada fuente: ¿se repone o se acaba?", "El Sol, el viento y el agua en movimiento se reponen; el carbón, el petróleo y el gas no."], "Renovables: Sol, viento y agua. No renovables: carbón, petróleo y gas natural"),
        ("Dar una razón", "Una persona dice que el petróleo es no renovable. Se le pide justificarlo con la ficha.", ["La ficha dice que se formó durante millones de años.", "Se usa mucho más rápido de lo que se forma."], "Es no renovable porque se consume más rápido de lo que se forma"),
    ],
    mistakes=[("Decir que una fuente es renovable porque «hay mucha».", "Lo que importa es si se repone al ritmo con que se usa, no cuánta hay hoy.", "Pregunta: ¿se repone de forma natural en poco tiempo?"),
              ("Pensar que las fuentes renovables no tienen ningún impacto.", "También ocupan terreno o cambian el paisaje, aunque suelen contaminar menos.", "Compara impactos en vez de decir «ninguno».")],
    T=[
        ("abc", "{F} ¿Cuál de estas fuentes es renovable?", "El viento", "El carbón", "El petróleo", "El viento se repone de forma natural; el carbón y el petróleo se agotan."),
        ("ab", "{F} ¿Cuál de estas fuentes es un combustible fósil?", "El gas natural", "El Sol", "La ficha indica que el gas natural se formó durante millones de años."),
        ("=", "{F} La lista nombra tres fuentes renovables y tres no renovables. ¿Cuántas fuentes tiene la lista en total?", "3+3", "Se suman las fuentes renovables y las no renovables nombradas.", " fuentes"),
        ("abc", "¿Qué significa que una fuente sea no renovable?", "Se consume más rápido de lo que se forma", "Se renueva todos los días", "No se puede usar", "No renovable indica que el ritmo de uso supera al ritmo de formación."),
        ("ab", "El agua de un río en movimiento mueve una turbina. ¿Qué tipo de fuente se usa?", "Renovable", "No renovable", "El agua en movimiento se repone con el ciclo del agua."),
        ("abc", "¿Qué libera principalmente la quema de combustibles fósiles?", "Gases que contaminan el aire y aumentan el efecto invernadero", "Solo agua limpia", "Más petróleo", "La quema libera gases como dióxido de carbono que alteran el aire."),
        ("abc", "{F} Un grupo propone usar «solo fuentes que se formaron en millones de años». ¿Qué tipo de fuentes escogió?", "No renovables", "Renovables", "Solo el Sol", "Esas fuentes son los combustibles fósiles de la lista."),
        ("ab", "Una persona dice: «Las fuentes renovables no tienen ningún impacto». ¿Qué respuesta es mejor?", "Suelen tener menos impacto, pero también ocupan espacio o cambian el paisaje", "Tiene razón, no tienen impacto", "Un impacto menor no es lo mismo que ninguno."),
        ("=", "Un barrio de ejemplo tiene 12 luminarias, y 5 funcionan con energía del Sol y el resto con otra fuente. ¿Cuántas funcionan con otra fuente?", "12-5", "Se resta al total las luminarias que usan el Sol.", " luminarias"),
        ("abc", "Un pueblo de ejemplo usa un generador de viento y nota que solo funciona cuando sopla. ¿Qué limitación muestra?", "Depende de que haya viento", "El viento se acaba para siempre", "Produce petróleo", "Una renovable puede depender del clima o del momento."),
        ("abc", "Dos vecinos discuten cuál recurso se renueva en poco tiempo: la leña de un bosque que se replanta o el petróleo. ¿Quién tiene razón?", "Quien dice que el bosque replantado se repone en décadas y el petróleo en millones de años", "Quien dice que ambos tardan igual", "Quien dice que el petróleo se repone al instante", "Replantar repone un bosque en décadas; el petróleo tarda millones de años."),
        ("abc", "{F} Para cuidar el ambiente, ¿cuál decisión es más coherente con la información de la ficha?", "Combinar fuentes renovables y usar menos energía", "Quemar solo carbón", "Usar petróleo sin límites", "Disminuir el consumo y apoyarse en renovables reduce el impacto."),
        ("ab", "¿Cuál afirmación es correcta sobre el Sol como fuente?", "Su energía llega cada día y no se agota al usarla en la escala humana", "Solo sirve de noche", "Cada día llega luz solar, aunque cambia con el clima y el momento."),
    ],
    ctx=("abc", "En una reunión de vecinos se propone instalar un calefón con paneles que usan el Sol, en vez de uno que funciona con gas natural. Una persona pregunta qué diferencia hay entre ambas fuentes. ¿Qué respondes?", "El Sol es renovable y el gas natural es un combustible fósil no renovable", "Las dos son renovables", "Las dos son no renovables", "El Sol se repone cada día; el gas natural se formó en millones de años."),
    sc=[("En Ciencias: ¿qué es una fuente renovable?", "Una que se repone o no se agota al usarla", "Renovable quiere decir que se renueva de forma natural."),
        ("¿Qué son los combustibles fósiles?", "Carbón, petróleo y gas natural", "Se formaron durante millones de años a partir de restos de seres vivos."),
        ("¿Por qué conviene pensar en el ambiente al elegir una fuente?", "Porque cada fuente produce un impacto distinto", "Así se compara lo que cada una cambia en el aire, el agua y el paisaje.")],
    op=("Con esta lista de ejemplo de fuentes (Sol, viento, carbón, petróleo, agua de río, gas natural), haz una tabla de dos columnas: «renovable» y «no renovable». Agrega una razón corta para cada fuente y una frase sobre el impacto ambiental de una de ellas.",
        "Renovable: Sol, porque llega cada día. No renovable: carbón, porque se formó en millones de años. Impacto: el carbón libera gases al quemarse.",
        ["clasifica las seis fuentes", "da una razón por fuente", "menciona un impacto ambiental"],
        ["una tabla de dos columnas y una frase"],
        ["clasificar según «cuánto hay»", "olvidar la razón"],
        "Pregunta: «¿Se repone al ritmo con que se usa?»."),
    reinforce="Haz una lista de tres actividades de tu semana que usan energía y di de qué fuente podría venir.",
    extend="Explica por qué ahorrar energía ayuda aunque se use una fuente renovable.",
)

# ============================================================ clase 5
F = ("Ficha 5 (localidades de ejemplo, inventadas). Pampa Clara: zona desértica del norte con muchos días despejados. "
     "Valle Los Sauces: tiene un río con una caída de agua constante. Costa Brava: viento fuerte casi todo el año. Bosque Sur: abundante leña. "
     "Tabla de ejemplo, electricidad de una comuna: hidroeléctrica 40 %, solar 25 %, eólica 15 %, carbón 20 %.")
build(
    O, 5, F,
    use="Hoy conozco recursos energéticos de Chile y propongo cuál conviene a cada zona, cuidando el ambiente.",
    prior=PRIOR + ["Sé clasificar fuentes renovables y no renovables."],
    explain=[
        "En Chile se usan varias fuentes de energía. Hay centrales hidroeléctricas, que aprovechan el agua de los ríos; plantas solares, sobre todo en el norte, donde hay muchos días despejados; parques eólicos que usan el viento; y centrales termoeléctricas que queman carbón, gas o petróleo. En el sur, mucha gente calefacciona con leña.",
        "Una parte importante de los combustibles fósiles que se usan en el país se importa. Esto significa que no todas las zonas tienen los mismos recursos: cada una aprovecha mejor lo que tiene cerca, como el sol en el desierto o el agua en un valle con río.",
        "La mezcla de fuentes cambia con los años. Para cifras actuales conviene revisar información oficial reciente. Aquí usamos datos de ejemplo para practicar: sumar porcentajes, comparar y proponer medidas que cuiden el aire, el agua y los bosques.",
    ],
    vocab=[("hidroeléctrica", "central que usa la caída del agua para producir electricidad"), ("termoeléctrica", "central que quema combustible para producir electricidad"), ("parque eólico", "conjunto de aerogeneradores que usan el viento"), ("recurso energético", "fuente de energía disponible en un lugar")],
    worked=[
        ("Elegir según el lugar", F, ["Pampa Clara tiene muchos días despejados.", "Eso favorece la energía del Sol."], "A Pampa Clara le conviene energía solar"),
        ("Leer la tabla", "La tabla de ejemplo dice: hidroeléctrica 40 %, solar 25 %, eólica 15 %, carbón 20 %. ¿Qué porcentaje es renovable?", ["Renovables: hidroeléctrica, solar y eólica.", "Se suman 40 más 25 más 15."], "80 % es renovable"),
    ],
    mistakes=[("Elegir la misma fuente para todas las zonas.", "Cada lugar tiene un clima y recursos distintos.", "Mira primero qué recurso abunda en la zona."),
              ("Dar cifras como si fueran las oficiales de hoy.", "Los datos de este cuaderno son de ejemplo y la mezcla cambia con los años.", "Rotula los datos y consulta fuentes oficiales para las cifras vigentes.")],
    T=[
        ("abc", "{F} ¿Qué recurso aprovecha mejor Costa Brava?", "El viento", "La leña", "El agua de una caída", "La ficha dice que allí sopla fuerte casi todo el año."),
        ("ab", "{F} ¿Qué localidad tiene un río con una caída de agua constante?", "Valle Los Sauces", "Pampa Clara", "La ficha asocia el río con caída de agua a Valle Los Sauces."),
        ("=", "{F} En la tabla, ¿qué porcentaje de la electricidad viene del carbón y de la solar juntos?", "20+25", "Se suman los porcentajes de las dos fuentes nombradas.", " %"),
        ("abc", "¿Qué tipo de central usa la caída del agua?", "Hidroeléctrica", "Termoeléctrica", "Eólica", "Hidro se refiere al agua, y su caída mueve la turbina."),
        ("ab", "¿Qué hace una central termoeléctrica?", "Quema combustible para producir electricidad", "Usa solo el Sol", "Termo se asocia al calor que se obtiene al quemar combustible."),
        ("abc", "{F} Bosque Sur tiene abundante leña. ¿Qué cuidado ambiental conviene tener?", "Replantar para que el bosque se reponga y cuidar el humo", "Cortar sin replantar", "Quemar la mayor cantidad posible", "La leña solo es sostenible si el bosque se repone y se evita el humo excesivo."),
        ("=", "{F} ¿Qué porcentaje de la electricidad de la comuna de ejemplo NO es renovable?", "100-(40+25+15)", "Se restan de 100 las tres fuentes renovables de la tabla.", " %"),
        ("abc", "{F} ¿Qué fuente de la tabla es no renovable?", "El carbón", "La eólica", "La hidroeléctrica", "El carbón es un combustible fósil."),
        ("ab", "Una comuna sin sol ni viento fuertes pero con un río con desnivel, ¿qué fuente probablemente aprovecha?", "Hidroeléctrica", "Solar", "El río con desnivel permite mover una turbina."),
        ("abc", "{F} Se quiere reducir el carbón de la tabla del 20 % al 10 % reemplazándolo por solar. ¿Cuánto quedaría la solar?", "35 %", "30 %", "45 %", "Si el carbón baja 10 puntos y los suma la solar, pasa de 25 a 35."),
        ("abc", "Una persona dice que la mezcla de fuentes de Chile es la de esta tabla de ejemplo. ¿Qué corrección es correcta?", "Son datos de ejemplo: las cifras reales se consultan en información oficial vigente", "La tabla es oficial de hoy", "La mezcla nunca cambia", "La tabla es un ejemplo y la mezcla cambia con los años."),
        ("abc", "{F} Pampa Clara propone usar paneles solares y además ahorrar luz. ¿Cuál es la razón más sólida?", "El sol abunda, y ahorrar reduce la energía que se necesita", "Porque el sol es gratis y no tiene ninguna desventaja", "Porque el desierto no necesita energía", "Aprovechar el recurso local y bajar el consumo cuida el ambiente."),
        ("ab", "¿Por qué no todas las zonas usan la misma fuente?", "Porque cada zona tiene recursos distintos, como sol, viento o ríos", "Porque la energía es distinta en cada casa", "La disponibilidad de recursos cambia según la geografía y el clima."),
    ],
    ctx=("abc", "En el consejo vecinal de una zona costera de ejemplo con viento constante se propone estudiar energía eólica. Una vecina pregunta si sirve en todo el país. ¿Qué respondes?", "Sirve donde hay viento suficiente; cada zona debe estudiar su recurso", "Sirve igual en todas partes", "No sirve en ninguna parte", "Un parque eólico depende de contar con viento regular."),
    sc=[("En Ciencias: ¿qué es una central hidroeléctrica?", "La que usa la caída del agua para producir electricidad", "Hidro se refiere al agua, y su caída mueve las turbinas."),
        ("¿Qué fuente conviene en una zona desértica con muchos días despejados?", "La solar", "Allí abunda la luz del Sol."),
        ("¿Por qué las cifras de la tabla de este cuaderno no son oficiales?", "Son datos de ejemplo para practicar", "Las cifras vigentes se consultan en información oficial.")],
    op=("Con la ficha de las cuatro localidades, escribe qué recurso aprovecharías en cada una, una ventaja y un cuidado ambiental. Presenta tus propuestas en una tabla y explica una de ellas a otra persona.",
        "Valle Los Sauces: hidroeléctrica. Ventaja: el agua cae siempre. Cuidado: respetar el caudal del río.",
        ["relaciona cada localidad con su recurso", "da una ventaja y un cuidado", "usa datos de la ficha"],
        ["una tabla de cuatro filas"],
        ["proponer lo mismo para todas", "no mencionar cuidado ambiental"],
        "Pregunta: «¿Qué dato de la ficha apoya tu elección?»."),
    reinforce="Elige una zona de Chile que conozcas y piensa qué recurso energético tiene cerca.",
    extend="Escribe tres preguntas que harías a una fuente oficial para conocer la mezcla de energía de tu región.",
)

# ============================================================ clase 6
F = ("Ficha 6 (cuenta de electricidad de ejemplo, datos inventados). Consumo del mes: 180 kWh. Consumo del mes anterior: 210 kWh. "
     "Un kilowatt-hora (kWh) es la energía que usa un aparato de 1 kilowatt (kW) funcionando durante 1 hora. "
     "Aparato de ejemplo: estufa eléctrica de 2 kW.")
build(
    O, 6, F,
    use="Hoy reviso lo aprendido: leo un consumo de energía de ejemplo, comparo y decido medidas para cuidar el ambiente.",
    prior=PRIOR + ["Conozco formas de energía, transformaciones y fuentes."],
    explain=[
        "Para revisar lo aprendido, junta tres ideas: la energía se nota por sus efectos, se transforma y se transfiere, y se obtiene de fuentes renovables y no renovables. Con eso puedes leer una cuenta de electricidad y entender qué mide.",
        "La electricidad que usamos se mide en kilowatt-hora (kWh). Un kWh es la energía que consume un aparato de 1 kilowatt (kW) funcionando durante 1 hora. Si el aparato es de 2 kW y funciona 3 horas, consume 2 por 3, es decir, 6 kWh.",
        "Comparar el consumo de dos meses permite saber si subió o bajó. Reducir el consumo ayuda al ambiente: se necesita producir menos energía. Algunas medidas son apagar lo que no se usa, desenchufar cargadores y elegir aparatos eficientes.",
    ],
    vocab=[("kilowatt-hora (kWh)", "unidad con que se mide la energía eléctrica consumida"), ("consumo", "cantidad de energía que se usa"), ("aparato eficiente", "el que aprovecha más energía y pierde menos como calor"), ("medida de ahorro", "acción para usar menos energía")],
    worked=[
        ("Comparar dos meses", F, ["Mes anterior: 210 kWh. Este mes: 180 kWh.", "Resto 210 menos 180."], "El consumo bajó 30 kWh"),
        ("Consumo de un aparato", "Una estufa eléctrica de ejemplo de 2 kW se usa 4 horas.", ["Se multiplican los kW por las horas.", "2 por 4."], "Consumió 8 kWh"),
    ],
    mistakes=[("Confundir kW con kWh.", "El kW indica la potencia del aparato; el kWh es la energía consumida en un tiempo.", "Multiplica kW por horas para obtener kWh."),
              ("Decir que el consumo bajó cuando el número de la cuenta aumentó.", "Un número mayor significa más consumo.", "Compara dos valores del mismo tipo antes de concluir.")],
    T=[
        ("abc", "{F} ¿Cuál fue el consumo de este mes?", "180 kWh", "210 kWh", "30 kWh", "La ficha indica 180 kWh para este mes."),
        ("ab", "¿Qué mide el kilowatt-hora?", "La energía eléctrica consumida", "La temperatura de la pieza", "El kWh es la unidad de energía eléctrica que aparece en las cuentas."),
        ("=", "{F} ¿Cuánto bajó el consumo entre el mes anterior y este mes?", "210-180", "Se resta el consumo de este mes al del mes anterior.", " kWh"),
        ("abc", "{F} ¿Qué mide 1 kWh según la ficha?", "Un aparato de 1 kW funcionando 1 hora", "Un aparato de 1 hora sin electricidad", "Un aparato de 1 kg", "Un kWh es la energía que consume 1 kW durante 1 hora."),
        ("=", "{F} Una estufa eléctrica de 2 kW funciona 3 horas. ¿Cuántos kWh consume?", "2*3", "Se multiplican la potencia en kW por las horas de uso.", " kWh"),
        ("ab", "¿Cuál medida ahorra electricidad?", "Apagar las luces de las piezas vacías", "Dejar el televisor encendido sin mirarlo", "Apagar lo que no se usa reduce los kWh consumidos."),
        ("=", "{F} Si el mes siguiente el consumo bajara 20 kWh respecto de este mes, ¿cuánto sería?", "180-20", "Se resta el ahorro al consumo de este mes.", " kWh"),
        ("abc", "{F} Una persona dice: «Gasté 210 kWh este mes». ¿Qué corrección es correcta?", "Gastó 180 kWh este mes; 210 era del mes anterior", "Está correcto", "Gastó 30 kWh este mes", "Los 210 kWh corresponden al mes anterior según la ficha."),
        ("ab", "¿Por qué ahorrar energía ayuda al ambiente?", "Porque se necesita producir menos energía", "Porque la energía deja de existir", "Menos consumo exige menos producción y menos impacto."),
        ("=", "Una estufa de 2 kW se usa 2 horas por día. ¿Cuántos kWh consume en 5 días?", "2*2*5", "Se multiplican potencia, horas diarias y días.", " kWh"),
        ("abc", "Se comparan dos aparatos de ejemplo que dan igual luz: A consume 10 unidades de energía eléctrica y B consume 4. ¿Cuál es más eficiente?", "B, porque necesita menos energía para la misma luz", "A, porque consume más", "Son iguales", "Con la misma luz, el que usa menos energía pierde menos como calor."),
        ("abc", "{F} Una persona dice que la estufa eléctrica de la ficha pierde toda su energía al enfriarse. ¿Qué corrección aplica?", "El calor pasa al aire y a los objetos: la energía se transfiere", "La energía se destruye", "La estufa produce frío", "La energía térmica se transfiere al ambiente, no desaparece."),
        ("ab", "Para el informe final de este módulo, ¿qué conclusión es mejor?", "El consumo bajó 30 kWh, probablemente por apagar aparatos que no se usaban", "El consumo bajó porque sí", "Una conclusión debe apoyarse en datos y proponer una explicación posible."),
    ],
    ctx=("abc", "En una cuenta de ejemplo aparece «consumo: 150 kWh» y la persona no sabe qué significa. ¿Cómo se lo explicas?", "Es la energía eléctrica usada en el mes, medida en kilowatt-hora", "Es la temperatura de la casa", "Es el peso de los aparatos", "El kWh mide la energía eléctrica consumida."),
    sc=[("¿Cómo se calcula el consumo de un aparato en kWh?", "Potencia en kW por horas de uso", "Por ejemplo, 2 kW durante 3 horas son 6 kWh."),
        ("En Ciencias: ¿qué es un aparato eficiente?", "El que aprovecha más energía y pierde menos como calor", "Eficiente significa que el aparato desperdicia menos energía como calor."),
        ("¿Para qué sirve comparar dos meses de consumo?", "Para saber si el consumo subió o bajó", "Así se evalúa si las medidas de ahorro funcionan.")],
    op=("Con la cuenta de ejemplo de la ficha, escribe: cuánto cambió el consumo, dos medidas de ahorro que podrían explicarlo y una frase final que une la energía, la fuente y el cuidado del ambiente.",
        "El consumo bajó 30 kWh. Medidas: apagar luces y desenchufar cargadores. Frase: ahorrar electricidad reduce la energía que se debe producir.",
        ["calcula bien la diferencia", "propone dos medidas", "relaciona con el ambiente"],
        ["un párrafo corto de tres líneas"],
        ["confundir kW con kWh", "no justificar las medidas"],
        "Pregunta: «¿Qué dato de la cuenta apoya tu conclusión?»."),
    reinforce="Anota durante una semana cuántas horas usas un aparato y calcula su consumo con una potencia de ejemplo.",
    extend="Explica con un ejemplo por qué un aparato eficiente cuida el ambiente aunque dé la misma luz o calor.",
)

"""Lenguaje y Comunicación EPJA Nivel 2 (5.º y 6.º), módulo 3: OAD-09, relacionar elementos verbales y no verbales en un texto audiovisual.
Los guiones son inventados y se leen en papel: no hay audio ni video reales (la voz, el tono y los gestos se describen por escrito)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los guiones, fichas y datos están escritos en cada ejercicio y son inventados para este cuaderno: "
    "no necesitas video, audio ni internet. Cuando la clase habla de un video, usa el guion escrito: lo que se ve, la voz y los gestos "
    "se describen entre paréntesis. Si quieres, pide a otra persona que lo lea en voz alta con el tono indicado. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)

build = make_build(MATERIALS)

O = "EPJA-LECO-NB2-OAD-09"

F1 = ("Video de ejemplo «Tu turno en la municipalidad» (datos inventados). IMAGEN: una persona mira una pantalla que dice «Turno 42». "
      "VOZ (tono suave, ritmo lento): «Cuando vea su número en la pantalla, avance al módulo 3.» TEXTO EN PANTALLA: «Módulo 3». "
      "GESTO: la funcionaria sonríe y señala hacia la derecha.")
F2 = ("Video de ejemplo con una misma frase dicha de dos maneras (datos inventados). Versión A: la voz dice «Ya llegó el bus» con tono alegre, "
      "volumen medio y ritmo animado; la persona sonríe y levanta la mano. Versión B: la voz dice «Ya llegó el bus» con tono cansado, "
      "volumen bajo y ritmo lento; la persona suspira y mira el reloj.")
F3 = ("Video de ejemplo «Ahorrar agua en casa» (datos inventados). IMAGEN 1: una llave que gotea. VOZ (tono serio, ritmo lento): "
      "«Una llave que gotea desperdicia agua todos los días.» TEXTO EN PANTALLA: «Revise sus llaves». IMAGEN 2: una persona aprieta la llave "
      "hasta que deja de gotear y sonríe. VOZ (tono alegre, ritmo más rápido): «Un arreglo simple evita el desperdicio.»")
F4 = ("Aviso de ejemplo «Reunión de vecinos» (datos inventados). IMAGEN: una sala con sillas en círculo; un vecino levanta la mano. "
      "VOZ (tono cordial, volumen medio): «Los esperamos el sábado para decidir juntos.» TEXTO EN PANTALLA: «Sábado, sede vecinal». "
      "GESTO: una vecina hace señas de bienvenida con la mano.")
F5 = ("Video de ejemplo «Revisar el extintor» para un lugar de trabajo (datos inventados). IMAGEN: un extintor con una etiqueta verde; "
      "una persona lo señala. VOZ (tono serio, volumen alto, ritmo lento): «Revise que la aguja esté en la zona verde.» "
      "TEXTO EN PANTALLA: «Aguja en zona verde = listo». GESTO: la persona hace el signo de aprobación con el pulgar.")
F6 = ("Video de ejemplo «Mensaje de la directiva» (datos inventados). VOZ (tono tembloroso, volumen bajo, ritmo rápido): «Todo está bajo control.» "
      "IMAGEN: la persona que habla mira hacia atrás varias veces y aprieta los puños. TEXTO EN PANTALLA: «Sin novedades».")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy distingo qué comunican las palabras y qué comunica todo lo demás en un video o aviso de pantalla.",
    prior=["Veo avisos en pantallas, videos o noticias en la vida diaria.", "Puedo decir de qué trata un mensaje.", "Leo frases cortas, con apoyo si lo necesito."],
    explain=[
        "Un texto audiovisual es un mensaje que usa imagen y sonido a la vez: un video, la pantalla de turnos de un consultorio, un aviso del metro o una noticia de televisión. Ya los conoces: los entiendes todos los días sin pensar en cómo están hechos.",
        "Los elementos verbales son las palabras, dichas en voz alta o escritas en pantalla. Los elementos no verbales son todo lo que comunica sin palabras: la imagen, los gestos, el tono y el volumen de la voz, el ritmo, los colores y la música.",
        "Relacionar ambos significa preguntarse cómo se ayudan: a veces repiten lo mismo, a veces agregan algo y a veces dicen cosas distintas. Entender esa relación te permite comprender mejor y no quedarte solo con las palabras.",
    ],
    vocab=[("texto audiovisual", "mensaje que combina imagen y sonido, como un video"), ("elemento verbal", "las palabras, dichas o escritas"), ("elemento no verbal", "lo que comunica sin palabras: imagen, gesto, tono"), ("guion", "texto que describe lo que se ve y lo que se dice")],
    worked=[
        ("Separar lo verbal de lo no verbal", "Aviso de ejemplo: IMAGEN: una ventanilla con una fila. VOZ (tono amable): «Las personas mayores pasan primero.» TEXTO EN PANTALLA: «Atención preferente». GESTO: el funcionario invita con la mano a pasar.", ["Verbal: la frase de la voz y el texto «Atención preferente».", "No verbal: la ventanilla con la fila, el tono amable y el gesto de invitar a pasar.", "Compruebo: ¿es una palabra? Es verbal. ¿Es una imagen o un gesto? Es no verbal."], "Verbal: la frase y «Atención preferente». No verbal: ventanilla, tono y gesto"),
        ("Un aviso del metro", "Un aviso de ejemplo del metro: la voz dice «Cuidado, cierre de puertas» con volumen alto y ritmo rápido, mientras parpadea una luz roja.", ["Las palabras son «Cuidado, cierre de puertas».", "El volumen alto, el ritmo rápido y la luz roja no son palabras.", "Todo junto comunica urgencia."], "Verbal: las palabras. No verbal: volumen, ritmo y luz roja; juntos comunican urgencia"),
    ],
    mistakes=[("Pensar que «verbal» es solo lo que se dice en voz alta.", "El texto escrito en pantalla también son palabras, aunque nadie las pronuncie.", "Pregunta: ¿son palabras, dichas o escritas? Entonces es verbal."),
              ("Creer que solo importan las palabras.", "El tono, el gesto y la imagen cambian lo que entendemos.", "Mira y escucha todo antes de decir qué comunica el mensaje.")],
    T=[
        ("ab", "¿Qué es un texto audiovisual?", "Un mensaje que combina imagen y sonido, como un video", "Un texto que solo se escribe en papel", "Audiovisual significa que se ve y se oye; un texto solo de papel no tiene sonido ni imagen en movimiento."),
        ("abc", "{F} ¿Cuál es un elemento verbal de este video?", "«Cuando vea su número en la pantalla, avance al módulo 3.»", "La funcionaria que sonríe", "El gesto de señalar hacia la derecha", "La frase de la voz está hecha de palabras; la sonrisa y el gesto comunican sin palabras."),
        ("{F} El texto en pantalla «Módulo 3», ¿es verbal o no verbal? Responde con una palabra.", "verbal", "Son palabras escritas, aunque nadie las diga en voz alta."),
        ("abc", "{F} ¿Qué se pide hacer cuando aparezca el número en la pantalla?", "Avanzar al módulo 3", "Sacar otro turno", "Esperar fuera del edificio", "La voz lo dice directamente: «avance al módulo 3»."),
        ("ab", "{F} ¿Cuál es un elemento no verbal?", "La funcionaria señala hacia la derecha", "El texto «Módulo 3»", "Señalar es un gesto y no usa palabras; el texto en pantalla son palabras escritas."),
        ("abc", "{F} ¿Qué aporta el gesto de señalar que la voz no dice?", "Hacia dónde queda el módulo", "El número del turno", "El nombre de la funcionaria", "La voz nombra el módulo, pero solo el gesto indica la dirección."),
        ("ab", "{F} La voz dice «módulo 3» y el texto en pantalla también. ¿Qué relación hay?", "Se repiten: el texto refuerza lo que dice la voz", "Se contradicen", "Los dos dicen lo mismo, así que uno apoya al otro y no hay contradicción."),
        ("Un video muestra una flecha roja que apunta a una puerta. ¿La flecha es verbal o no verbal? Responde con una palabra.", "no verbal", "Es una imagen; no está hecha de palabras."),
        ("abc", "La voz dice «Salida» mientras la imagen muestra una flecha verde. ¿Qué par es correcto?", "«Salida» es verbal y la flecha es no verbal", "Las dos son verbales", "Las dos son no verbales", "«Salida» es una palabra; la flecha es una imagen sin palabras."),
        ("abc", "En un aviso de un consultorio, la voz dice «Silencio, por favor» en voz baja mientras la imagen muestra a una persona con el dedo sobre los labios. ¿Qué elementos son no verbales?", "El volumen bajo y el gesto del dedo sobre los labios", "Solo las palabras «Silencio, por favor»", "Solo el nombre del consultorio", "El volumen y el gesto no son palabras y refuerzan el pedido de silencio."),
        ("ab", "Un aviso de la tele muestra una cara de sorpresa mientras la voz dice «La cuenta de luz bajó». ¿Qué comunica la cara?", "Que la noticia no se esperaba", "Que se cortó la luz", "La cara muestra sorpresa, es decir, algo inesperado; no habla de un corte de luz."),
        ("abc", "{F} Si se quitara el sonido y quedaran solo imagen y texto, ¿qué ocurriría?", "Se entendería que hay que ir al módulo 3, pero se perdería la indicación de esperar a ver el número", "Se entendería exactamente lo mismo, sin perder nada", "No se entendería nada", "El texto sigue indicando el módulo, pero la condición «cuando vea su número» solo la dice la voz."),
        ("ab", "Ana dice que en un video solo importan las palabras. Luis dice que palabras, imagen y gestos juntos dan el mensaje. ¿Quién tiene razón?", "Luis, porque todos los elementos comunican", "Ana, porque las palabras son lo único que significa", "En un texto audiovisual la imagen, el tono y los gestos agregan o cambian el significado."),
    ],
    ctx=("abc", "En la sala de espera de un consultorio, la pantalla muestra «Turno 18» en letras verdes que parpadean, y suena un timbre corto. Una persona dice: «Me llamaron». ¿Qué elementos no verbales le permitieron entenderlo?", "El timbre y las letras que parpadean", "Solo la palabra «Turno»", "El nombre del consultorio", "El timbre y el parpadeo llaman la atención sin palabras; junto con el número, avisan que le toca."),
    sc=[("En Lenguaje: ¿qué son los elementos verbales de un video?", "Las palabras, dichas o escritas", "Incluye la voz y el texto en pantalla porque ambos usan palabras."),
        ("¿Cuál de estas cosas es no verbal: el tono de la voz o el texto en pantalla?", "El tono de la voz", "El tono no es una palabra: es cómo suena la voz."),
        ("¿Para qué sirve relacionar lo verbal con lo no verbal?", "Para entender mejor el mensaje completo", "Palabras e imágenes se refuerzan, se completan o se contradicen, y eso cambia el sentido.")],
    op=("Imagina este aviso de ejemplo: «IMAGEN: una persona sostiene un paraguas bajo la lluvia. VOZ (tono tranquilo): «Hoy lleve paraguas.» TEXTO EN PANTALLA: «Lluvia por la tarde».» Escribe una lista de dos columnas: elementos verbales y elementos no verbales. Luego cuéntaselo a otra persona.",
        "Verbal: «Hoy lleve paraguas» y «Lluvia por la tarde». No verbal: la persona con paraguas, la lluvia y el tono tranquilo.",
        ["clasifica las palabras como verbales", "clasifica imagen y tono como no verbales", "usa al menos dos elementos en cada columna"],
        ["una tabla de dos columnas en el cuaderno"],
        ["poner el texto en pantalla en la columna no verbal", "dejar una columna sin completar"],
        "Pregunta: «¿Esto son palabras o es otra cosa que comunica?»."),
    reinforce="Mira un aviso en una pantalla de tu barrio y anota una cosa verbal y una no verbal.",
    extend="Explica con un ejemplo por qué la misma frase puede entenderse distinto si cambia el gesto de quien la dice.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo las palabras para hablar de la voz y los gestos: tono, volumen, inflexión, ritmo y gesto.",
    prior=["Sé separar lo verbal de lo no verbal.", "Puedo comparar dos situaciones parecidas.", "Conozco palabras como «rápido» y «lento»."],
    explain=[
        "La voz comunica más que las palabras. El tono es cómo suena la voz: alegre, serio, enojado, cansado. El volumen es la fuerza de la voz: alto o bajo. El ritmo es la rapidez al hablar y las pausas que se hacen.",
        "La inflexión es el cambio de la voz hacia arriba o hacia abajo, por ejemplo cuando sube al final de una pregunta. Los gestos son movimientos de la cara o del cuerpo: sonreír, levantar la mano, suspirar.",
        "También importa el registro, que es el modo de hablar según la situación. El registro formal es cuidado y respetuoso («Estimado vecino»); el informal es cercano («Hola, vecino»). Elegir el registro adecuado depende de con quién hablamos. Además, un sinónimo es una palabra de significado parecido a otra y un antónimo, una de significado contrario.",
    ],
    vocab=[("tono", "cómo suena la voz: alegre, serio, cansado"), ("volumen", "fuerza de la voz, alto o bajo"), ("inflexión", "subida o bajada de la voz al hablar"), ("ritmo", "rapidez y pausas al hablar"), ("registro", "modo de hablar según la situación: formal o informal"), ("sinónimo", "palabra de significado parecido"), ("antónimo", "palabra de significado contrario")],
    worked=[
        ("Misma frase, distinta versión", "Video de ejemplo con la frase «Gracias por venir». Versión C: tono cálido, volumen medio, ritmo calmado; la persona sonríe y da la mano. Versión D: tono frío, volumen bajo, ritmo rápido; la persona mira el celular.", ["Las palabras son iguales en C y en D.", "Cambia el tono (cálido/frío), el volumen, el ritmo y el gesto.", "Por eso C comunica un agradecimiento sincero y D, desinterés."], "Las palabras no cambian; cambian tono, volumen, ritmo y gesto, y con ellos el mensaje"),
        ("Registro formal e informal", "Dos saludos de ejemplo para avisar de una reunión: «Estimados vecinos: les informo que la reunión será el sábado» y «Hola, vecinos, les aviso que el sábado nos juntamos».", ["El primero usa «estimados» y «les informo»: cuidado y respetuoso.", "El segundo usa «hola» y «nos juntamos»: cercano."], "El primero es formal; el segundo, informal"),
    ],
    mistakes=[("Confundir volumen con ritmo.", "El volumen es la fuerza de la voz; el ritmo es la rapidez y las pausas.", "Pregunta: ¿habla más fuerte (volumen) o más rápido (ritmo)?"),
              ("Creer que el registro formal es «hablar difícil».", "El registro formal es respetuoso y claro, no complicado.", "Usa frases simples y saludos cuidados.")],
    T=[
        ("ab", "{F} ¿Qué cambia entre la versión A y la B?", "El tono, el volumen, el ritmo y el gesto; las palabras son las mismas", "Todas las palabras", "La frase «Ya llegó el bus» se repite igual en las dos versiones."),
        ("¿Qué describe «alegre» o «cansado»: el tono o el gesto? Responde con una palabra.", "tono", "Alegre y cansado dicen cómo suena la voz."),
        ("abc", "¿Qué es el volumen?", "La fuerza con que suena la voz, alta o baja", "La rapidez con que se habla", "El estado de ánimo de la voz", "El volumen mide la fuerza de la voz; la rapidez es el ritmo y el ánimo es el tono."),
        ("abc", "{F} En la versión B, ¿qué significa «ritmo lento»?", "Se habla despacio y con pausas", "Se habla muy fuerte", "Se usa un saludo formal", "Ritmo es la rapidez y las pausas; lento es lo contrario de rápido."),
        ("ab", "{F} En la versión B, ¿cuál es un gesto?", "Mirar el reloj", "El volumen bajo", "Mirar el reloj es un movimiento del cuerpo; el volumen es una característica de la voz."),
        ("¿Cómo se llama el cambio de la voz hacia arriba al final de una pregunta? Responde con una palabra.", "inflexión", "La inflexión es la subida o bajada de la voz mientras se habla."),
        ("abc", "Un sinónimo de «veloz» es:", "rápido", "lento", "ruidoso", "Veloz y rápido significan casi lo mismo; lento es lo contrario."),
        ("ab", "Un antónimo de «pausado» es:", "apresurado", "tranquilo", "Pausado es lento y tranquilo; apresurado es lo contrario."),
        ("abc", "{F} ¿Qué versión comunica que la persona esperó mucho?", "La B", "La A", "Las dos por igual", "En B el tono cansado, el suspiro y el reloj sugieren una espera larga; en A la persona celebra."),
        ("ab", "En una carta a la municipalidad, ¿qué saludo corresponde?", "Estimados señores:", "Hola, qué tal, po", "La municipalidad es una institución, así que se usa un registro formal."),
        ("abc", "Un aviso dice «Calma» con voz tensa, volumen alto y ritmo rápido. ¿Qué contradicción hay?", "La palabra pide calma, pero el tono y el ritmo transmiten urgencia", "No hay contradicción, porque la palabra dice calma", "Las palabras y el volumen dicen lo mismo", "Lo verbal pide tranquilidad, pero lo no verbal comunica tensión: dicen cosas opuestas."),
        ("ab", "Un vecino dice: «Si la frase es la misma, el mensaje es el mismo». ¿Es correcto?", "No: tono, ritmo y gestos cambian lo que se entiende", "Sí: solo cuentan las palabras", "Como muestran las versiones A y B, la misma frase puede sonar a alegría o a cansancio."),
        ("abc", "{F} Si en la versión A el volumen fuera muy bajo y la persona mirara al suelo, ¿qué pasaría con el mensaje?", "Sonaría menos alegre, aunque las palabras sean iguales", "Seguiría igual de alegre", "Dejaría de tener palabras", "El volumen bajo y la mirada al suelo restan alegría: lo no verbal modifica el sentido."),
    ],
    ctx=("abc", "Un altavoz del barrio dice, con voz rápida y volumen muy alto: «Reunión mañana, no falte». ¿Qué puede entender quien lo oye?", "Que la reunión es importante y urgente", "Que la reunión se canceló", "Que no importa si va o no", "El volumen alto y el ritmo rápido refuerzan «no falte»: comunican urgencia."),
    sc=[("¿Qué es el ritmo en una voz?", "La rapidez al hablar y las pausas", "El ritmo no mide la fuerza ni el ánimo, sino la velocidad."),
        ("En Lenguaje: ¿qué es la inflexión?", "El cambio de la voz hacia arriba o hacia abajo", "Por ejemplo, sube al final de una pregunta."),
        ("¿Qué registro usa «Estimado vecino»?", "El formal", "Es un saludo cuidado y respetuoso.")],
    op=("Lee esta frase de ejemplo: «Necesito que vengas». Escribe dos versiones: en una la persona dice la frase con tono amable y en la otra con tono molesto. Para cada una anota el volumen, el ritmo y un gesto. Si puedes, léelas en voz alta.",
        "Versión 1: tono amable, volumen medio, ritmo calmado, sonríe. Versión 2: tono molesto, volumen alto, ritmo rápido, frunce el ceño.",
        ["describe tono, volumen y ritmo en cada versión", "incluye un gesto distinto en cada una", "muestra que las palabras son las mismas"],
        ["dos versiones escritas con sus rasgos"],
        ["cambiar las palabras de la frase", "usar la misma descripción en las dos versiones"],
        "Pregunta: «¿Qué cambió: las palabras o la forma de decirlas?»."),
    reinforce="Di una misma frase de tres maneras distintas y nota cómo cambia lo que se entiende.",
    extend="Escribe un saludo formal y otro informal para invitar a una reunión de vecinos.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy sigo cuatro pasos para relacionar lo que dicen las palabras con lo que comunican la imagen y el tono.",
    prior=["Sé qué es lo verbal y lo no verbal.", "Conozco tono, volumen, ritmo y gesto.", "Puedo describir lo que veo en una imagen."],
    explain=[
        "Para relacionar lo verbal con lo no verbal conviene un método. Paso 1: lee o escucha las palabras. Paso 2: observa lo no verbal: imagen, gestos, tono, volumen y ritmo. Paso 3: pregúntate cómo se relacionan. Paso 4: di qué idea comunica el texto completo.",
        "En el paso 3 hay tres posibilidades. Se refuerzan cuando repiten lo mismo. Se complementan cuando una parte agrega algo que la otra no dice. Se contradicen cuando dicen cosas opuestas; ahí conviene desconfiar y mirar con más cuidado.",
        "Este método sirve para videos, noticias y avisos. Con la práctica se hace rápido: es la misma atención que ya pones cuando alguien dice «estoy bien» con la cara triste.",
    ],
    vocab=[("reforzar", "repetir lo mismo para dar más fuerza"), ("complementar", "agregar algo que faltaba"), ("contradecir", "decir lo contrario"), ("desperdicio", "gastar algo sin necesidad")],
    worked=[
        ("Los cuatro pasos", "Video de ejemplo «Apagar la luz». IMAGEN 1: una pieza vacía con la luz prendida. VOZ (tono serio): «Una luz prendida sin necesidad gasta electricidad.» TEXTO EN PANTALLA: «Apague al salir». IMAGEN 2: una persona apaga el interruptor y sale. VOZ (tono alegre): «Un gesto simple ahorra energía.»", ["Paso 1: la voz habla de una luz prendida sin necesidad y de un gesto simple.", "Paso 2: la imagen muestra la pieza vacía y luego a alguien apagando; el tono pasa de serio a alegre.", "Paso 3: imagen y voz se refuerzan; el texto «Apague al salir» complementa, porque agrega la acción pedida.", "Paso 4: el video dice que dejar la luz prendida gasta electricidad y que apagarla es simple."], "Idea: apagar la luz al salir ahorra electricidad"),
        ("Una contradicción", "Video de ejemplo: la voz dice «Todo salió perfecto» con tono apagado, y la persona se toma la cabeza con las manos.", ["Paso 1: las palabras dicen perfecto.", "Paso 2: el tono apagado y el gesto de las manos en la cabeza muestran preocupación.", "Paso 3: se contradicen."], "Se contradicen: conviene dudar de las palabras y mirar el tono y el gesto"),
    ],
    mistakes=[("Quedarse solo con las palabras y saltarse el paso 2.", "Lo no verbal puede cambiar o contradecir lo que dicen las palabras.", "Antes de concluir, describe imagen, tono y gesto."),
              ("Decir «se refuerzan» siempre.", "A veces una parte agrega algo (complementa) o dice algo opuesto (contradice).", "Pregunta: ¿repite, agrega o dice lo contrario?")],
    T=[
        ("abc", "¿Qué se hace en el paso 1 del método?", "Leer o escuchar las palabras", "Decidir la idea final", "Mirar solo los gestos", "El método parte por las palabras y después observa lo no verbal."),
        ("ab", "{F} ¿Cuál es la frase de la voz que acompaña la imagen 1?", "«Una llave que gotea desperdicia agua todos los días.»", "«Un arreglo simple evita el desperdicio.»", "La primera frase se dice con la llave goteando; la segunda acompaña el arreglo de la imagen 2."),
        ("Cuando la imagen y las palabras dicen lo mismo, se _____ (refuerzan o contradicen). Responde con una palabra.", "refuerzan", "Repetir la misma idea con dos recursos le da más fuerza al mensaje."),
        ("abc", "{F} ¿Qué relación hay entre el texto «Revise sus llaves» y la voz?", "El texto complementa: agrega la acción que se pide", "El texto contradice a la voz", "No tienen ninguna relación", "La voz cuenta el problema y el texto agrega qué hacer: complementa."),
        ("ab", "{F} ¿Qué cambia en la voz entre la primera y la segunda frase?", "Pasa de un tono serio a uno alegre y el ritmo se acelera", "Pasa de un tono alegre a uno serio", "Primero se presenta el problema con seriedad y luego la solución con alegría."),
        ("abc", "{F} ¿Qué comunica ese cambio de tono?", "Primero se presenta un problema y luego una solución positiva", "Que el video ya terminó", "Que habla otra persona distinta", "El tono serio acompaña el problema y el alegre, la solución."),
        ("ab", "La voz dice «Estoy feliz» con tono molesto y la persona frunce el ceño. ¿Qué relación hay?", "Se contradicen", "Se refuerzan", "Las palabras dicen feliz, pero el tono y el gesto muestran enojo: dicen cosas opuestas."),
        ("abc", "¿Cuál es el orden correcto de los pasos?", "Leer palabras, observar lo no verbal, relacionar, decir la idea", "Decir la idea, leer palabras, observar, relacionar", "Observar, decir la idea, leer, relacionar", "Primero se reúne la información y al final se concluye."),
        ("ab", "{F} ¿Cuál es la idea que comunica el video completo?", "Revisar y arreglar las llaves evita desperdiciar agua", "Las llaves son de metal", "Todas las partes del video apuntan a cuidar el agua revisando y arreglando las llaves."),
        ("abc", "{F} Si el segundo texto en pantalla dijera «Es muy difícil arreglarla» mientras la imagen muestra un arreglo simple y sonriente, ¿qué ocurriría?", "Texto e imagen se contradirían", "Se reforzarían", "Nada cambiaría, porque el texto no cuenta", "El texto diría que es difícil y la imagen mostraría que es simple: son opuestos."),
        ("ab", "¿Por qué conviene observar lo no verbal antes de concluir?", "Porque puede reforzar, completar o contradecir las palabras", "Porque las palabras no significan nada", "Sin mirar la imagen y el tono se puede perder o malentender parte del mensaje."),
        ("abc", "Una voz dice, rápido y bajito: «Este producto no tiene riesgos», y en pantalla aparece en letra muy pequeña «Lea las condiciones». ¿Qué conviene concluir?", "Que conviene leer las condiciones, porque lo no verbal resta atención a algo importante", "Que no hace falta leer nada más", "Que el producto es de mala calidad", "La rapidez, el volumen bajo y la letra chica hacen pasar por alto la condición: hay que revisarla."),
        ("abc", "Tres personas analizan el video de las llaves. ¿Cuál análisis es el mejor?", "Dice qué muestra la imagen, qué dice la voz y cómo se relacionan para comunicar que hay que revisar las llaves", "Copia solo lo que dice la voz", "Dice que el video es lindo", "El mejor análisis une palabras, imagen y relación; copiar o opinar sin fundamento no basta."),
    ],
    ctx=("abc", "En una reunión de vecinos proyectan un video sobre el cuidado de las plazas: la voz dice «Cuidemos juntos nuestra plaza» y en la imagen aparecen vecinos botando basura al suelo. ¿Qué relación hay entre voz e imagen?", "Se contradicen", "Se refuerzan", "Se complementan", "Lo que se dice (cuidar) y lo que se ve (ensuciar) son opuestos."),
    sc=[("En Lenguaje: ¿qué significa que dos elementos «se complementan»?", "Que uno agrega algo que el otro no dice", "Complementar es agregar, no repetir ni contradecir."),
        ("¿Qué paso del método viene después de observar lo no verbal?", "Relacionar lo verbal con lo no verbal", "Primero se reúne la información y luego se relaciona."),
        ("¿Qué conviene hacer si palabras y gestos se contradicen?", "Mirar con más cuidado y dudar del mensaje", "La contradicción avisa que algo no coincide.")],
    op=("Aplica los cuatro pasos a este aviso de ejemplo: «IMAGEN: una persona tapa una olla. VOZ (tono tranquilo): «Tape las ollas para ahorrar gas.» TEXTO EN PANTALLA: «Menos tiempo, menos gas».» Escribe qué hiciste en cada paso y la idea final.",
        "Paso 1: tapar ollas ahorra gas. Paso 2: imagen de una olla tapada, tono tranquilo. Paso 3: se refuerzan; el texto complementa. Paso 4: tapar ollas ahorra gas.",
        ["escribe los cuatro pasos", "dice si se refuerzan, complementan o contradicen", "termina con una idea completa"],
        ["cuatro líneas escritas, una por paso"],
        ["saltarse el paso 2", "escribir la idea sin relacionar nada"],
        "Pregunta: «¿Qué dice la imagen que no dice la voz?»."),
    reinforce="Elige un aviso de pantalla que veas hoy y dile a alguien si imagen y palabras se refuerzan o se contradicen.",
    extend="Escribe un ejemplo propio de texto donde las palabras y los gestos se contradigan y explica cómo lo notaste.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: completo una tabla de análisis y aprendo a citar un video.",
    prior=["Conozco los cuatro pasos para relacionar lo verbal y lo no verbal.", "Sé qué es el registro formal e informal.", "Entiendo qué es un sinónimo."],
    explain=[
        "Practicar con apoyo significa que alguien te da una pista. Una pista útil es una tabla con cuatro columnas: escena, elemento verbal, elemento no verbal y relación. Si completas las cuatro, ya analizaste el texto.",
        "Cuando uses un video como fuente, conviene citarlo: decir de dónde viene la información. Una forma sencilla es escribir quién lo hizo, el título entre comillas, qué tipo de texto es y el año. Así otras personas pueden encontrarlo.",
        "Para comprender un mensaje oral ayudan tres estrategias: anticipar el tema con el título, tomar nota de las palabras clave y volver a escuchar lo que no entendiste. Si una palabra es nueva, usa el contexto para deducir su sentido y pregunta si hace falta.",
    ],
    vocab=[("citar", "decir de dónde viene la información"), ("fuente", "lugar o persona de donde sale un dato"), ("sede", "lugar donde se reúne una organización"), ("cordial", "amable y respetuoso"), ("palabra clave", "palabra que resume la idea central")],
    worked=[
        ("Completar la tabla", "Aviso de ejemplo «Taller de costura». IMAGEN: mesas con máquinas de coser. VOZ (tono animado): «¡Venga a aprender a coser!» TEXTO EN PANTALLA: «Martes y jueves, 18 h». GESTO: una instructora muestra una tela.", ["Escena: aviso de un taller.", "Verbal: «¡Venga a aprender a coser!» y «Martes y jueves, 18 h».", "No verbal: mesas con máquinas, tono animado y la instructora que muestra una tela.", "Relación: se complementan: el texto agrega los días y la hora que la voz no dice."], "Voz e imagen se refuerzan y el texto complementa con los días y la hora"),
        ("Citar el aviso", "Junta de Vecinos Los Aromos (de ejemplo), «Reunión de vecinos», aviso en video, 2024 (año de ejemplo).", ["Quién lo hizo: Junta de Vecinos Los Aromos.", "Título entre comillas: «Reunión de vecinos».", "Tipo de texto y año: aviso en video, 2024."], "Una cita completa dice quién, título, tipo de texto y año"),
    ],
    mistakes=[("Citar solo con «un video que vi».", "No dice quién lo hizo ni cómo encontrarlo.", "Escribe quién, título, tipo de texto y año."),
              ("Saltarse una palabra nueva sin deducir qué significa.", "El contexto da pistas y deja comprender mejor.", "Lee la frase completa, deduce el sentido y pregunta si sigue la duda.")],
    T=[
        ("ab", "{F} ¿Cuál es la frase que dice la voz?", "«Los esperamos el sábado para decidir juntos.»", "«Sábado, sede vecinal»", "La segunda frase es el texto escrito en pantalla; la voz dice la invitación completa."),
        ("abc", "{F} ¿Qué día se convoca a la reunión?", "El sábado", "El domingo", "El viernes", "Tanto la voz como el texto en pantalla dicen sábado."),
        ("ab", "{F} ¿Qué elemento no verbal muestra que la reunión es participativa?", "El vecino que levanta la mano", "La hora de la reunión", "Levantar la mano es pedir la palabra; la hora no es un gesto ni muestra participación."),
        ("abc", "{F} ¿Qué relación hay entre la voz que dice «sábado» y el texto «Sábado, sede vecinal»?", "El texto complementa: agrega el lugar", "Se contradicen", "No tienen relación", "La voz da el día y el texto repite el día y agrega dónde."),
        ("ab", "{F} ¿Qué comunican el tono cordial y las señas de bienvenida?", "Una invitación amable", "Una orden obligatoria", "El tono cordial y las señas muestran cercanía, no exigencia."),
        ("abc", "¿Qué cita sencilla del aviso incluye todos los datos?", "Junta de Vecinos Los Aromos (de ejemplo), «Reunión de vecinos», aviso en video, 2024 (año de ejemplo)", "«Reunión de vecinos»", "Un aviso que vi", "La primera dice quién, título, tipo de texto y año; las otras no permiten encontrar la fuente."),
        ("¿Qué dato falta en la cita «Junta de Vecinos Los Aromos, aviso en video, 2024»? Responde con una palabra.", "título", "Falta el nombre del aviso entre comillas."),
        ("ab", "Antes de ver un video, ¿qué estrategia ayuda a comprender mejor?", "Anticipar el tema a partir del título", "Tapar la imagen y no mirar", "El título da una pista del tema y prepara la atención."),
        ("abc", "Alguien no entendió la palabra «sede» al ver el aviso. ¿Qué estrategia usa mejor?", "Releer la frase «Sábado, sede vecinal», deducir que es un lugar de reunión y preguntar si duda", "Ignorar la palabra", "Cambiar de aviso", "Usar el contexto y preguntar permite comprender sin perder el hilo."),
        ("ab", "Un antónimo de «cordial» es:", "hostil", "amable", "Cordial es amable; hostil es lo contrario, desagradable o agresivo."),
        ("abc", "{F} Si la vecina cruzara los brazos con gesto serio mientras la voz dice «Los esperamos», ¿qué ocurriría?", "Gesto y palabras se contradirían", "Se reforzarían", "Quedaría igual de claro", "Cruzar los brazos con seriedad no es una bienvenida: va en contra de lo dicho."),
        ("ab", "¿Qué análisis es más completo?", "Verbal: invitación al sábado; no verbal: sillas en círculo y gestos amables; relación: se refuerzan", "Es un aviso bonito", "Un análisis completo nombra lo verbal, lo no verbal y su relación."),
        ("abc", "Para reforzar que la reunión es abierta a todos, ¿qué imagen mantiene la coherencia con las palabras?", "Varias personas distintas entrando y saludando", "Una sala vacía", "Una puerta cerrada con candado", "Una imagen de personas entrando coincide con la invitación; las otras la contradicen."),
    ],
    ctx=("abc", "Una persona quiere compartir en una reunión información de un video de la junta de vecinos de ejemplo. ¿Cuál es la mejor forma de mencionar la fuente?", "«Según el aviso en video “Reunión de vecinos”, de la Junta de Vecinos Los Aromos (de ejemplo), 2024»", "«Dicen que habrá reunión»", "«Vi algo por ahí»", "La primera señala quién lo dijo, cuál es el título y el año; las otras no."),
    sc=[("¿Qué cuatro datos tiene una cita sencilla?", "Quién, título, tipo de texto y año", "Con esos datos otra persona encuentra la fuente."),
        ("¿Qué columnas tiene la tabla de análisis?", "Escena, verbal, no verbal y relación", "Reúnen lo que se dice, lo que se ve y cómo se unen."),
        ("En Lenguaje: ¿qué estrategia ayuda a entender una palabra nueva?", "Usar el contexto y preguntar", "Las palabras de alrededor dan pistas.")],
    op=("Completa una tabla de cuatro columnas (escena, verbal, no verbal, relación) con este aviso de ejemplo: «IMAGEN: una feria con puestos de verduras. VOZ (tono animado, ritmo rápido): «¡Este sábado, feria en la plaza!» TEXTO EN PANTALLA: «Plaza central, 9 a 13 h».» Escribe también una cita de ejemplo del aviso: Junta de Vecinos Los Aromos (de ejemplo), «Feria en la plaza», aviso en video, 2024.",
        "Escena: aviso de feria. Verbal: «Este sábado, feria» y «Plaza central, 9 a 13 h». No verbal: feria con puestos, tono animado. Relación: se refuerzan.",
        ["completa las cuatro columnas", "dice si se refuerzan, complementan o contradicen", "escribe la cita con quién, título, tipo y año"],
        ["una tabla y una cita en el cuaderno"],
        ["dejar la columna de relación vacía", "citar sin título"],
        "Pregunta: «¿Qué agrega el texto escrito que no dice la voz?»."),
    reinforce="Completa la tabla con un aviso que veas hoy y pide a otra persona que opine.",
    extend="Escribe cómo citarías un video que tú mismo has visto, usando quién, título, tipo y año.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a un video de un lugar de trabajo y a un aviso de la comunidad.",
    prior=["Sé completar la tabla de análisis.", "Distingo reforzar, complementar y contradecir.", "Sé citar una fuente de forma sencilla."],
    explain=[
        "En un lugar de trabajo o en la comunidad, los videos y avisos se ven a veces sin sonido, con ruido o desde lejos. Por eso un buen mensaje audiovisual no depende de un solo elemento: si falta el audio, el texto y la imagen deben comunicar lo esencial.",
        "Al analizar, pregúntate qué parte del mensaje llega por las palabras y qué parte llega por la imagen, el color o el gesto. Un color como el verde, junto con la frase «zona verde», refuerza la indicación y ayuda a quien lee con dificultad.",
        "También conviene preguntar para quién está hecho el mensaje. El registro, el tono y el volumen deben ser adecuados a ese público: una indicación de seguridad se dice con seriedad y claridad, no en broma.",
    ],
    vocab=[("indicación", "instrucción que dice qué hacer"), ("público", "personas a las que va dirigido un mensaje"), ("esencial", "lo más importante, lo que no puede faltar"), ("seguridad", "conjunto de cuidados para evitar accidentes")],
    worked=[
        ("Analizar un video de trabajo", "Video de ejemplo «Orden en la bodega». IMAGEN: una bodega con una línea amarilla en el piso. VOZ (tono firme, volumen alto): «Mantenga libre la línea amarilla.» TEXTO EN PANTALLA: «Línea amarilla = paso libre». GESTO: la persona hace una señal de alto con la mano.", ["Verbal: «Mantenga libre la línea amarilla» y «Línea amarilla = paso libre».", "No verbal: línea amarilla, tono firme, volumen alto y señal de alto con la mano.", "Relación: todo se refuerza: la indicación, el color y el gesto dicen que el paso debe quedar libre."], "Palabras, color y gesto se refuerzan: la línea amarilla debe quedar libre"),
        ("Sin sonido", "Un aviso de ejemplo se proyecta sin sonido: IMAGEN: un camión de basura; TEXTO: «Retiro de basura: lunes y jueves».", ["Sin voz se pierde el tono.", "Pero el texto dice lo esencial: qué se retira y qué días.", "El camión refuerza la idea de retiro de basura."], "El texto y el camión comunican lo esencial aunque no haya sonido"),
    ],
    mistakes=[("Creer que si falta el sonido el mensaje se pierde por completo.", "Un buen mensaje apoya lo esencial en texto e imagen.", "Revisa qué parte llega sin audio."),
              ("Analizar el aviso sin pensar a quién va dirigido.", "El mismo mensaje se dice distinto para públicos distintos.", "Pregunta siempre: ¿para quién es?")],
    T=[
        ("ab", "{F} ¿Qué indicación da la voz?", "Revisar que la aguja esté en la zona verde", "Cambiar el extintor cada día", "La voz dice «Revise que la aguja esté en la zona verde»; no menciona cambios diarios."),
        ("abc", "{F} ¿El signo de aprobación con el pulgar es verbal o no verbal?", "No verbal", "Verbal", "Las dos cosas", "Es un gesto: comunica sin palabras."),
        ("abc", "{F} ¿Qué comunican el tono serio y el volumen alto?", "Que la indicación es importante", "Que es un chiste", "Que no hay que hacer nada", "Un tono serio y fuerte dan peso a una indicación de seguridad."),
        ("{F} ¿De qué color es la etiqueta del extintor del video? Responde con una palabra.", "verde", "La imagen indica una etiqueta verde, igual que la zona verde de la aguja."),
        ("ab", "{F} ¿Qué relación hay entre el texto «Aguja en zona verde = listo» y el gesto del pulgar?", "Se refuerzan: los dos dicen que está bien", "Se contradicen", "Ambos comunican aprobación: el texto con palabras y el pulgar con un gesto."),
        ("abc", "{F} Una persona ve el video sin sonido. ¿Qué parte del mensaje le llega igual?", "Que la aguja debe estar en la zona verde, por el texto y la imagen", "Nada del mensaje", "Solo el tono serio de la voz", "El texto en pantalla y la imagen repiten lo esencial sin necesidad de audio."),
        ("ab", "En la reunión se ve un aviso sin sonido: texto «Cambio de horario: ahora a las 19 h» y un reloj con dos horas. ¿Qué se entiende?", "Que el horario cambió y la hora nueva es a las 19 h", "Que la reunión se suspendió", "El texto dice el cambio y la hora; el reloj lo refuerza."),
        ("abc", "¿Qué mensaje comunica mejor una indicación de seguridad a un público amplio?", "Letras grandes, voz clara y una imagen que coincide con lo que se dice", "Letras diminutas y música fuerte", "Una voz muy rápida sin texto", "La claridad y la coherencia entre elementos ayudan a que más personas entiendan."),
        ("ab", "¿Cómo se llama el grupo de personas a quienes va dirigido un aviso?", "El público", "La fuente", "El público es a quien va dirigido el mensaje; la fuente es de dónde sale la información."),
        ("abc", "{F} Si la voz dijera en tono de broma «Revise la aguja, si quiere», ¿qué sucedería?", "El tono bromista restaría seriedad a una indicación de seguridad", "Quedaría más clara", "No cambiaría nada", "El tono debe ser adecuado al contenido; una broma debilita una indicación importante."),
        ("ab", "Un aviso de ejemplo para vecinos dice con voz fuerte y rápida «¡Corte de agua mañana!» y el texto en pantalla, con letra pequeña, «de 9 a 13 h». ¿Qué mejoraría la claridad?", "Escribir el horario en letra grande", "Hablar aún más rápido", "El horario es un dato esencial: debe verse fácil, no en letra pequeña."),
        ("abc", "{F} ¿Cuál análisis es más completo?", "Verbal: indicación y texto; no verbal: color, gesto y tono; relación: se refuerzan para decir que verde es listo", "Es un video claro", "La persona es amable", "El primero incluye lo verbal, lo no verbal y su relación; los otros solo opinan."),
        ("ab", "Si el texto dijera «Aguja en zona roja = listo» mientras la imagen muestra una etiqueta verde, ¿qué pasaría?", "Habría contradicción entre texto e imagen", "Se reforzarían", "Rojo y verde son colores distintos: el texto y la imagen dirían cosas opuestas."),
    ],
    ctx=("abc", "En un lugar de trabajo pasan un video sin sonido. La imagen muestra un casco amarillo; el texto dice «Use casco en esta zona». ¿Qué elementos refuerzan el mensaje?", "La imagen del casco y el texto que lo nombra", "Solo el color amarillo", "El silencio del video", "Imagen y texto dicen lo mismo con recursos distintos: se refuerzan."),
    sc=[("¿Qué debe llegar aunque falte el audio?", "Lo esencial, por texto e imagen", "Si se pierde el audio, el mensaje no debe desaparecer."),
        ("En Lenguaje: ¿qué es el público de un mensaje?", "Las personas a quienes va dirigido", "Saber el público ayuda a elegir registro y tono."),
        ("¿Qué tono conviene en una indicación de seguridad?", "Serio y claro", "El tono debe ser adecuado al contenido.")],
    op=("Analiza este aviso de ejemplo: «IMAGEN: un contenedor azul con botellas de plástico. VOZ (tono amable, ritmo calmado): «Deposite aquí solo botellas limpias.» TEXTO EN PANTALLA: «Plástico limpio, contenedor azul».» Escribe lo verbal, lo no verbal, la relación y cómo se entendería sin sonido. Cita el aviso: Junta de Vecinos Los Aromos (de ejemplo), «Reciclar en el barrio», aviso en video, 2024.",
        "Verbal: «Deposite aquí solo botellas limpias» y el texto en pantalla. No verbal: contenedor azul, botellas, tono amable. Relación: se refuerzan. Sin sonido: el texto y el contenedor bastan.",
        ["separa lo verbal y lo no verbal", "explica la relación", "dice qué se entiende sin sonido", "incluye la cita"],
        ["un análisis escrito de cuatro partes"],
        ["analizar sin mencionar la relación", "citar sin título"],
        "Pregunta: «¿Qué parte del mensaje sobrevive sin audio?»."),
    reinforce="Mira un aviso de un lugar público sin sonido y anota qué mensaje llega.",
    extend="Explica por qué es útil que un aviso de seguridad se entienda con la imagen y el texto, aunque no haya audio.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado, detecto una contradicción y decido qué quiero repasar.",
    prior=["Conozco los cuatro pasos del método.", "Sé usar la tabla de análisis.", "Sé citar una fuente de forma sencilla."],
    explain=[
        "En este cierre repasamos lo importante. Un texto audiovisual comunica con palabras y con elementos no verbales: imagen, gestos, tono, volumen y ritmo. Para entenderlo, observamos ambos y preguntamos si se refuerzan, se complementan o se contradicen.",
        "Cuando se contradicen, no hay que aceptar sin más lo que dicen las palabras. Un tono tembloroso o una mirada nerviosa pueden indicar que algo no coincide. Aun así, no conviene adivinar: describe lo que ves y lo que oyes, y busca más información en una fuente confiable.",
        "Para decidir qué repasar, revisa tu lista: ¿distingo lo verbal de lo no verbal?, ¿nombro tono, volumen y ritmo?, ¿relaciono los elementos?, ¿cito la fuente? Anota lo que ya dominas y lo que quieres practicar de nuevo.",
    ],
    vocab=[("contradicción", "cuando dos cosas dicen lo contrario"), ("fuente confiable", "fuente que dice quién habla y puede comprobarse"), ("repasar", "volver a estudiar algo"), ("describir", "decir cómo es algo sin opinar")],
    worked=[
        ("Detectar la contradicción", "Video de ejemplo: VOZ (tono apagado): «Estamos felices con los resultados.» IMAGEN: la persona mira el suelo y se toma el rostro con la mano. TEXTO EN PANTALLA: «Resultados del año».", ["Lo verbal: «Estamos felices con los resultados» y «Resultados del año».", "Lo no verbal: tono apagado, mirada al suelo y mano en el rostro.", "Se contradicen: las palabras dicen alegría y el tono y los gestos muestran decaimiento."], "Se contradicen: las palabras celebran, pero el tono y los gestos muestran decaimiento"),
        ("Describir sin adivinar", "Con el mismo video: ¿qué se puede decir sin inventar?", ["Se puede decir que la persona habla con tono apagado y mira el suelo.", "No se puede afirmar por qué lo hace: el video no lo dice.", "Conviene buscar más información en una fuente confiable."], "Describe lo observado y no adivines las causas"),
    ],
    mistakes=[("Concluir qué le pasa a la persona sin tener datos.", "Los gestos dan pistas, no certezas.", "Describe lo que ves y busca más información."),
              ("Creer que repasar es repetir todo.", "Es más útil repasar lo que cuesta.", "Marca tus dos puntos más débiles y practica con ellos.")],
    T=[
        ("ab", "{F} ¿Cuál es la frase dicha por la voz?", "«Todo está bajo control.»", "«Sin novedades»", "La voz dice «Todo está bajo control»; «Sin novedades» aparece escrito en pantalla."),
        ("abc", "{F} ¿Qué tono tiene la voz?", "Tembloroso", "Alegre", "Enojado", "La descripción del video dice que la voz tiene un tono tembloroso."),
        ("{F} ¿«Sin novedades» es un elemento verbal o no verbal? Responde con una palabra.", "verbal", "Es texto escrito en pantalla, es decir, palabras."),
        ("abc", "{F} ¿Qué gesto muestra nerviosismo?", "Mirar hacia atrás y apretar los puños", "Decir «Sin novedades»", "Hablar en un video", "Mirar hacia atrás y apretar los puños son movimientos del cuerpo; lo otro son palabras."),
        ("ab", "{F} ¿Qué relación hay entre las palabras y lo no verbal?", "Se contradicen", "Se refuerzan", "Las palabras tranquilizan, pero el tono y los gestos muestran preocupación."),
        ("abc", "{F} ¿Qué es lo más prudente concluir?", "Que lo que se ve y se oye no coincide con las palabras, y conviene buscar más información", "Que la persona miente seguro", "Que no hay nada que comprobar", "Hay indicios de contradicción, pero no certeza: se verifica en una fuente confiable."),
        ("ab", "Para describir sin adivinar, ¿qué frase sirve?", "«La persona habla con tono tembloroso y mira hacia atrás»", "«La persona está asustada porque le pasó algo»", "La primera describe lo que se ve; la segunda inventa una causa."),
        ("abc", "¿Qué conviene hacer ante un mensaje que se contradice?", "Buscar más información en una fuente confiable", "Aceptar solo las palabras", "Ignorar el video", "Verificar con otra fuente permite comprobar lo que el video no aclara."),
        ("ab", "¿Cuál es una fuente más confiable?", "Un aviso que dice qué institución lo emitió", "Una publicación sin autor", "Quien firma un mensaje se hace responsable y lo dicho puede comprobarse."),
        ("ab", "Un sinónimo de «prudente» es:", "cuidadoso", "apresurado", "Prudente es quien actúa con cuidado; apresurado es lo contrario."),
        ("abc", "{F} ¿Qué cambio haría coherente el video?", "Que el tono fuera firme y la persona estuviera tranquila", "Que el tono fuera más tembloroso", "Que la persona mirara más hacia atrás", "Si palabras, tono y gestos transmiten calma, el mensaje es coherente."),
        ("ab", "Una persona dice que repasar es repetir todo el cuaderno. ¿Es lo más útil?", "No: conviene repasar lo que más cuesta", "Sí: siempre hay que repetir todo", "Concentrarse en los puntos débiles aprovecha mejor el tiempo."),
        ("abc", "¿Cuál análisis final es el mejor?", "Verbal: tranquiliza; no verbal: nerviosismo; relación: se contradicen; conclusión: hay que verificar", "El video es corto", "Todo está bajo control", "El mejor análisis une lo verbal, lo no verbal, la relación y una conclusión prudente."),
    ],
    ctx=("abc", "Alguien reenvía un mensaje en video: la persona dice con tono seguro «Este remedio cura todo», pero evita mirar a cámara y el texto en pantalla, en letra mínima, dice «No reemplaza una consulta». ¿Qué conviene hacer?", "Notar la contradicción y consultar a un profesional de salud o a una fuente oficial", "Creer solo la frase fuerte", "Compartirlo de inmediato", "Palabras y letra pequeña no coinciden; en temas de salud se consulta a profesionales."),
    sc=[("En Lenguaje: ¿qué es una contradicción en un mensaje?", "Cuando lo verbal y lo no verbal dicen cosas opuestas", "Detectarla ayuda a no aceptar sin pensar."),
        ("¿Qué datos tiene una cita sencilla?", "Quién, título, tipo de texto y año", "Con esos cuatro datos otra persona puede encontrar la fuente."),
        ("¿Qué hago para decidir qué repasar?", "Reviso mi lista y marco lo que me cuesta", "Una lista de comprobación muestra qué reforzar.")],
    op=("Haz tu lista de comprobación: escribe «sí» o «a veces» ante cada pregunta: ¿distingo lo verbal de lo no verbal?, ¿nombro tono, volumen y ritmo?, ¿digo si se refuerzan, complementan o contradicen?, ¿cito la fuente? Luego analiza este video de ejemplo: «VOZ (tono firme): «La feria abre a las 9.» TEXTO EN PANTALLA: «Feria: 9 a 13 h».» y escribe qué quieres repasar.",
        "Lista con cuatro respuestas. Análisis: verbal y texto coinciden; el tono firme refuerza; se refuerzan. Repasar: citar la fuente.",
        ["responde las cuatro preguntas", "analiza el video con los tres pasos", "elige al menos un punto para repasar"],
        ["una lista y un análisis en el cuaderno"],
        ["responder «sí» a todo sin revisar", "no elegir qué repasar"],
        "Pregunta: «¿Qué te costó más y cómo lo vas a practicar?»."),
    reinforce="Elige el punto que más te costó y analiza un aviso nuevo usando solo ese punto.",
    extend="Explica a otra persona, con un ejemplo, cómo se relacionan las palabras con el gesto y el tono.",
)

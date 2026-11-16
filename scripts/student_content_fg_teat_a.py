"""Teatro 3.º y 4.º medio FG: OAC-01 (cuerpo, gesto y voz en juegos dramáticos e improvisaciones), clases 1 a 4. Escenas inventadas; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O1 = "FG-TEAT-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (juego de ejemplo, inventado). Una persona espera en un paradero y dice la frase «ya casi es la hora». "
     "Versión 1: de pie, hombros caídos, mira el suelo, habla bajo y lento. "
     "Versión 2: de pie, pecho abierto, mira al frente, habla fuerte y rápido, da pasos cortos. "
     "Versión 3: sentada en el suelo, mira el reloj de reojo, voz aguda y con pausas largas.")
build(
    O1, 1, F,
    use="Aprenderé a distinguir los recursos del cuerpo (postura, gesto, mirada, nivel, desplazamiento) y de la voz (volumen, tono, ritmo, pausa) y a explorarlos en un juego dramático cambiando una variable a la vez.",
    prior=["Distingo una descripción de una opinión.", "Sé trabajar en un espacio despejado respetando el espacio de otras personas.", "Sé que un mismo texto puede decirse de muchas maneras."],
    explain=[
        "En teatro, el cuerpo comunica con la postura (cómo se para o se sienta), el gesto (un movimiento expresivo del rostro, las manos o el cuerpo), la mirada, el nivel (la altura del cuerpo: alto, medio o bajo) y el desplazamiento (cómo y por dónde se mueve). La voz comunica con el volumen (fuerte o suave), el tono (agudo o grave), el ritmo (rápido o lento) y la pausa (un silencio con intención). Todos estos recursos se pueden observar y describir.",
        "Explorar es probar de manera ordenada. Se dice la misma frase y se cambia solo una variable, por ejemplo el ritmo, para comparar qué efecto produce. Si se cambian cuatro cosas a la vez, no se sabe cuál produjo el efecto. Después de cada prueba se anota qué se hizo y qué se percibió, separando lo que se observa (voz baja, mirada al suelo) de lo que se interpreta (parece cansancio).",
        "Todo ejercicio corporal se hace con seguridad: espacio despejado, cada persona en su zona, sin tocarse, sin caídas ni saltos peligrosos y sin forzar la voz. Si hay dolor, mareo o incomodidad, se detiene el ejercicio y se avisa a una persona adulta.",
    ],
    vocab=[("postura", "forma en que el cuerpo se sostiene"), ("gesto", "movimiento expresivo del rostro, las manos o el cuerpo"), ("nivel", "altura del cuerpo en el espacio: alto, medio o bajo"), ("tono", "qué tan agudo o grave suena la voz"), ("ritmo", "rapidez con que se dicen las palabras"), ("pausa", "silencio con intención dentro de lo que se dice"), ("variable", "elemento que se cambia a propósito para comparar su efecto")],
    worked=[
        ("Describir sin interpretar", "Un compañero mira al suelo, habla bajo y encoge los hombros al decir «bueno, está bien». Escribe una descripción y una interpretación por separado.", ["Descripción: mira al suelo, voz baja y hombros encogidos; son rasgos que cualquiera puede comprobar.", "Interpretación: podría estar resignado o inseguro; es una lectura posible, no un hecho."], "Descripción con rasgos observables; interpretación rotulada como posible"),
        ("Cambiar una variable", "Quieres saber si el ritmo cambia el sentido de la frase «voy a pensarlo». ¿Cómo lo pruebas?", ["Dices la frase dos veces con la misma postura, la misma mirada y el mismo volumen.", "Solo cambias el ritmo: una vez lento y otra rápido, y anotas el efecto de cada una."], "Se cambia solo el ritmo y se anota el efecto"),
    ],
    mistakes=[("Describir con «actúa raro» o «lo hace mal».", "Son impresiones que otra persona no puede comprobar mirando.", "Cámbialas por rasgos: «habla bajo, mira al suelo y no mueve las manos»."),
              ("Cambiar postura, voz y mirada a la vez y concluir cuál funcionó.", "Con varios cambios juntos no se sabe qué produjo el efecto.", "Cambia una sola variable por prueba y compara.")],
    T=[
        ('abc', '¿Cuál es un ejemplo de gesto?', 'Levantar las cejas y abrir la boca al oír una noticia', 'Decir una frase con el volumen más alto para que se escuche desde el fondo', 'Ubicarse en el extremo derecho del espacio', 'El gesto es un movimiento expresivo del rostro o del cuerpo; el volumen es de la voz y la ubicación es del espacio.'),
        ('abc', '{F} ¿En qué versión se usa el nivel bajo?', 'Versión 3', 'Versión 1', 'Versión 2', 'Solo en la 3 la persona está sentada en el suelo, y el nivel bajo es tener el cuerpo cerca del suelo.'),
        ('abc', '¿Qué es el tono de la voz?', 'Qué tan aguda o grave suena', 'Qué tan fuerte suena', 'Qué tan rápido se habla', 'El tono es la altura del sonido; la fuerza es el volumen y la rapidez es el ritmo.'),
        ('abc', '{F} ¿Qué conjunto de rasgos de la versión 1 permite proponer que el personaje está cansado?', 'Hombros caídos, mirada al suelo y voz baja y lenta', 'Pecho abierto, mirada al frente, pasos cortos y voz fuerte y rápida', 'Nivel bajo, reloj de reojo y pausas largas', 'La interpretación de cansancio se apoya en rasgos de la versión 1; los otros conjuntos son de las versiones 2 y 3.'),
        ('abc', 'Una pausa con intención dentro de una frase sirve para', 'dar tiempo a que una idea o emoción se note antes de seguir', 'subir el volumen sin esfuerzo y hablar más fuerte hacia el final de la frase', 'esconder que se olvidó el texto', 'Una pausa elegida marca lo que viene o lo que acaba de decirse; no es un descuido.'),
        ('abc', 'Dos intérpretes dicen «ya llegué»: una sonríe y levanta los brazos, el otro frunce el ceño y mira al piso. ¿Qué cambió?', 'El gesto, y con él lo que se percibe de la situación', 'El texto, porque las palabras son distintas', 'Nada, porque la frase es la misma', 'Con el mismo texto, el gesto y la mirada cambian el sentido que recibe el público.'),
        ('=', 'Un calentamiento vocal tiene 3 ejercicios de 4 minutos cada uno y una pausa de 2 minutos al final. ¿Cuántos minutos dura?', '3*4+2', 'Se multiplican los ejercicios por sus minutos y se suma la pausa final.', ' minutos'),
        ('abc', '{F} Quieres que la espera se perciba impaciente sin gritar. ¿Qué combinación eliges?', 'Pasos cortos, mirada al reloj y ritmo de habla rápido', 'Nivel bajo, mirada al suelo, voz lenta y pausas largas entre cada palabra', 'Cuerpo quieto, voz grave y pausas muy largas', 'La impaciencia se muestra con movimiento corto, atención al reloj y ritmo acelerado, sin subir el volumen.'),
        ('abc', 'Para un ejercicio de gesto en parejas, ¿cuál es una variante segura?', 'Cada persona usa su propia zona y se comunica solo con la mirada y los gestos, sin tocarse', 'Una persona empuja suave a la otra para marcar el conflicto', 'Una persona se deja caer al suelo para mostrar sorpresa', 'En un ejercicio seguro no hay contacto ni caídas; la expresión se logra con mirada y gesto.'),
        ('abc', 'Ana dice: «El personaje es un enojón». Bruno dice: «Habla fuerte, aprieta los puños y camina rápido». ¿Quién separa lo observable de lo interpretado?', 'Bruno, porque describe rasgos que se pueden comprobar', 'Ana, porque nombra con precisión la emoción del personaje en una sola palabra', 'Ninguno, pues ambos usan la misma información', 'Bruno cita rasgos comprobables; Ana entrega directamente una interpretación sin mostrar de dónde sale.'),
        ('abc', 'Una compañera propone decir la misma frase con tres tonos (grave, medio y agudo) y anotar qué cambia. ¿Qué principio de exploración cumple?', 'Cambiar una sola variable y comparar el efecto', 'Repetir la frase muchas veces igual para memorizarla mejor', 'Elegir de entrada el tono correcto', 'Mantiene todo igual salvo el tono, así el efecto se atribuye a ese cambio.'),
        ('=', 'Una frase de 24 palabras se dice a 2 palabras por segundo y se le agregan 3 pausas de 2 segundos. ¿Cuántos segundos dura?', '24//2+3*2', 'Primero se calcula el tiempo de las palabras y luego se suma el de las pausas.', ' segundos'),
        ('abc', '{F} Quieres comunicar que el personaje oculta algo. ¿Qué prueba permite saber si funciona la mirada?', 'Bajar la mirada solo cuando entra otra persona, con el resto igual', 'Cambiar mirada, voz y postura al mismo tiempo', 'Repetir la versión 2 tres veces sin cambios', 'Con un solo cambio se puede atribuir el efecto a la mirada.'),
    ],
    ctx=('=', 'Veinte estudiantes forman equipos de 5. Cada equipo muestra 3 gestos de 40 segundos cada uno, y los equipos pasan uno tras otro. ¿Cuántos minutos suma la ronda entera?', '20//5*3*40//60', 'Se calcula la cantidad de equipos, los segundos totales y se pasa a minutos.', ' minutos'),
    sc=[
        ("En Teatro: ¿qué es el nivel en el uso del cuerpo?", "La altura del cuerpo en el espacio: alto, medio o bajo", "El nivel dice qué tan cerca del suelo o alto está el cuerpo."),
        ("¿Qué se debe hacer ante un mareo o una incomodidad durante un ejercicio corporal?", "Detener el ejercicio y avisar a una persona adulta", "La seguridad va primero y no se sigue con una molestia."),
        ("¿Qué se anota después de cada prueba de exploración?", "Qué se hizo y qué efecto se percibió, separando lo observado de lo interpretado", "Así se comparan pruebas sin mezclar hechos con opiniones."),
    ],
    op=("Escoge una frase de ejemplo: «ya casi es la hora» o «no esperaba verte aquí». Dila tres veces cambiando solo una variable (por ejemplo el ritmo). Escribe, por cada prueba, qué variable cambiaste, una descripción de lo que se observa y una interpretación rotulada como posible.",
        "Frase «no esperaba verte aquí»; variable: pausa. Prueba 1 sin pausa: voz continua, sonó casual. Prueba 2 con pausa antes de «verte»: silencio y mirada baja; interpretación posible: sorpresa o duda.",
        ["cambia una sola variable por prueba", "separa descripción de interpretación", "usa términos de cuerpo o voz de la clase"],
        ["hoja con tres pruebas registradas"],
        ["cambiar varias variables a la vez", "escribir solo opiniones como «quedó bien»"],
        "Pregunta: «¿qué cambió entre la prueba 1 y la 2?». Si nombra más de una cosa, pídele repetir cambiando solo una."),
    reinforce="Elige una frase corta y dila en casa con tres ritmos distintos, sin contacto ni objetos, anotando qué cambia.",
    extend="Explica por qué una pausa puede comunicar más que una palabra y da una situación inventada donde ocurra.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (situación de ejemplo, inventada). Quién: una persona que atiende un kiosco en una plaza. Qué quiere: cerrar a la hora para llegar a un ensayo. "
     "Dónde: el kiosco, a las siete de la tarde. Obstáculo: llega alguien que necesita ayuda para encontrar una dirección justo cuando va a cerrar.")
build(
    O1, 2, F,
    use="Aprenderé a construir una situación dramática breve con personaje, objetivo, espacio y obstáculo, y a mostrar lo que el personaje quiere con acciones del cuerpo y la voz en vez de explicarlo con palabras.",
    prior=["Distingo recursos del cuerpo y de la voz.", "Sé cambiar una variable por vez.", "Sé trabajar con respeto en parejas y grupos."],
    explain=[
        "Una situación dramática tiene cuatro elementos básicos: quién (el personaje), qué quiere (su objetivo), dónde y cuándo ocurre (el espacio y el tiempo) y qué se lo dificulta (el obstáculo). Cuando el objetivo choca con el obstáculo aparece el conflicto, que es lo que mueve la escena. Sin conflicto, la escena queda como una descripción: pasa el tiempo, pero nada cambia.",
        "El personaje se muestra con acciones. Una acción es algo que el personaje hace para conseguir su objetivo: apurarse, convencer, esquivar, pedir. En vez de decir «tengo prisa», el cuerpo puede mirar el reloj, guardar objetos rápido y cortar las frases. Esto es mostrar, y casi siempre comunica más que explicar.",
        "En los juegos dramáticos se usan objetos imaginarios y ejercicios como el espejo (dos personas frente a frente, a un brazo de distancia, imitando movimientos lentos sin tocarse) o la estatua (quedarse quieto en una imagen). Se evita todo contacto y cualquier subida o caída. Un personaje es una construcción para la escena: no es la identidad de quien actúa, y el ejercicio puede detenerse si alguien se incomoda.",
    ],
    vocab=[("personaje", "figura que se construye para una escena"), ("objetivo", "lo que el personaje quiere conseguir"), ("obstáculo", "lo que complica que consiga su objetivo"), ("conflicto", "choque entre el objetivo y el obstáculo que mueve la escena"), ("acción", "algo que el personaje hace para lograr su objetivo"), ("espacio", "lugar donde ocurre la escena")],
    worked=[
        ("Armar una situación", "Quieres una escena sobre una persona que debe entregar un paquete antes de las cinco y se queda sin batería en su teléfono. Identifica los cuatro elementos.", ["Quién: una persona repartidora. Qué quiere: entregar antes de las cinco.", "Dónde: una calle del barrio, a media tarde. Obstáculo: el teléfono sin batería y no sabe la dirección exacta."], "Personaje, objetivo, lugar/tiempo y obstáculo completos"),
        ("Mostrar en vez de decir", "El personaje está nervioso porque espera un resultado. Propón dos acciones para mostrarlo sin decirlo.", ["Elijo acciones que se vean: revisar varias veces el bolsillo y acomodarse la ropa sin necesidad.", "Agrego una voz que se corta en medio de la frase."], "Revisar el bolsillo, acomodarse la ropa y cortar las frases"),
    ],
    mistakes=[("Hacer que los personajes se cuenten lo que sienten («estoy muy nervioso»).", "Explicar quita fuerza; el público entiende más por lo que se ve que por lo que se anuncia.", "Convierte cada emoción en una acción visible."),
              ("Armar una escena sin obstáculo, donde todo sale bien de inmediato.", "Sin obstáculo no hay conflicto y la escena no se mueve.", "Agrega algo que complique el objetivo.")],
    T=[
        ('abc', '¿Qué es el objetivo de un personaje?', 'Lo que quiere conseguir en la escena', 'El lugar donde ocurre la escena', 'La emoción que quiere provocar en el público', 'El objetivo es lo que el personaje desea; el lugar es el espacio y la emoción del público es el propósito.'),
        ('abc', '{F} ¿Cuál es el obstáculo de esta situación?', 'Llega alguien que pide ayuda justo antes de cerrar', 'El kiosco está en una plaza y la escena ocurre a las siete de la tarde', 'La persona atiende el kiosco', 'El obstáculo es lo que dificulta el objetivo de cerrar a tiempo; el lugar y el oficio no lo dificultan.'),
        ('abc', 'En el juego del espejo en parejas, ¿cómo se hace con seguridad?', 'Frente a frente, a un brazo de distancia, imitando movimientos lentos sin tocarse', 'Tomados de la mano para sentir mejor el movimiento', 'Moviéndose rápido y girando para que sea más difícil imitar', 'La distancia sin contacto y el ritmo lento evitan choques y caídas.'),
        ('abc', 'Una escena donde nadie quiere nada ni nada se complica queda como', 'una descripción en la que no cambia nada para los personajes', 'una escena con un conflicto muy fuerte que cambia a todos los personajes', 'una improvisación sin espacio', 'Sin objetivo ni obstáculo no hay conflicto que mueva la escena.'),
        ('abc', '{F} Para mostrar que el personaje tiene prisa sin decirlo, el cuerpo puede', 'mirar el reloj, guardar objetos rápido y cortar las frases', 'sentarse en el nivel bajo y mirar la plaza', 'repetir en voz alta «tengo prisa»', 'Las acciones visibles muestran la prisa; decir la frase es explicar.'),
        ('abc', 'Un personaje quiere silencio para estudiar y otro quiere poner música en el mismo lugar. ¿Qué se genera?', 'Un conflicto entre objetivos opuestos', 'Una descripción detallada del lugar donde ocurre la escena', 'Un cambio de personaje', 'Dos objetivos incompatibles en el mismo espacio producen conflicto.'),
        ('=', 'Cinco equipos preparan cada uno 2 situaciones de 90 segundos. ¿Cuántos minutos suman todas las situaciones?', '5*2*90//60', 'Se multiplican equipos, situaciones y segundos, y se pasa a minutos.', ' minutos'),
        ('abc', 'Un grupo escribe: «Una vecina quiere terminar su tarea antes de que oscurezca; llega su hermano a contarle algo muy largo». ¿Qué elemento de la situación falta?', 'El espacio donde ocurre la escena', 'El objetivo, porque no se sabe qué quiere hacer la vecina', 'El obstáculo', 'Se nombran un objetivo (terminar la tarea) y un obstáculo (el hermano), pero no el lugar.'),
        ('abc', '¿Qué objeto imaginario es seguro y claro para el público?', 'Sostener con las dos manos una taza imaginaria y beber despacio', 'Subirse a una mesa o a una silla para mostrar que se está en un lugar alto', 'Correr hacia atrás para mostrar que se llega tarde', 'El objeto imaginario sostenido con calma no exige subir ni moverse de forma peligrosa.'),
        ('abc', 'Un estudiante dice «mi personaje está feliz» y su compañera pregunta «¿qué quiere y qué se lo impide?». ¿Por qué es útil esa pregunta?', 'Porque el objetivo y el obstáculo dan acciones que se pueden mostrar', 'Porque la felicidad no puede actuarse', 'Porque un personaje no debe tener emociones', 'Una emoción sola no dice qué hacer; el objetivo y el obstáculo generan acciones.'),
        ('abc', '{F} Un grupo cambia el obstáculo: ahora llega alguien a comprar mientras el personaje quiere cerrar. ¿Qué pasa con el conflicto?', 'Cambia: el personaje debe decidir si atiende o cierra', 'Desaparece, porque atender a un cliente no es un obstáculo sino parte del trabajo', 'No cambia, pues el personaje sigue en el kiosco', 'El nuevo obstáculo obliga a elegir entre dos acciones y cambia el conflicto.'),
        ('=', 'Un taller de 45 minutos dedica 10 al calentamiento y 5 a explicar las reglas; el resto se reparte en 6 escenas del mismo largo. ¿Cuántos minutos dura cada escena?', '(45-10-5)//6', 'Se resta lo ya usado al total y se divide el resto en partes iguales.', ' minutos'),
        ('abc', 'Versión 1: el personaje logra su objetivo de inmediato. Versión 2: intenta dos acciones distintas porque la primera falla. ¿Cuál muestra más conflicto?', 'La versión 2, porque la acción cambia ante el obstáculo', 'La versión 1, porque el personaje consigue lo que quiere sin dificultades', 'Ambas, ya que tienen el mismo objetivo', 'El conflicto se nota cuando algo resiste y el personaje debe cambiar su acción.'),
    ],
    ctx=('=', 'Un equipo tiene 20 minutos de ensayo: 5 los usa para acordar quién, qué quiere, dónde y qué obstáculo, y el resto lo reparte en 3 ensayos iguales. ¿Cuántos minutos dura cada ensayo?', '(20-5)//3', 'Se descuentan los minutos de acuerdo y se divide el resto en tres.', ' minutos'),
    sc=[
        ("En Teatro: ¿qué es un obstáculo?", "Lo que complica que el personaje consiga su objetivo", "El obstáculo es la parte que genera el conflicto."),
        ("¿Qué elementos básicos tiene una situación dramática?", "Quién, qué quiere, dónde y cuándo, y qué se lo dificulta", "Son los cuatro elementos que enseña la clase."),
        ("Si durante un juego dramático alguien se siente incómodo, ¿qué se hace?", "Se detiene el juego y se avisa a una persona adulta", "Cualquier persona puede detener un ejercicio por seguridad."),
    ],
    op=("Escoge un lugar de ejemplo: una biblioteca, una parada de buses o una cocina. Escribe quién es el personaje, qué quiere, dónde y cuándo está y qué obstáculo aparece. Agrega tres acciones (no frases) que muestren lo que quiere. Sin contacto físico ni objetos peligrosos.",
        "Parada de buses: una estudiante que quiere llegar a una prueba; el bus no pasa; acciones: mira el camino cada pocos segundos, camina en círculos cortos y revisa su mochila.",
        ["incluye los cuatro elementos", "el obstáculo genera conflicto", "las acciones se pueden ver", "no hay contacto ni riesgo"],
        ["ficha con la situación y tres acciones"],
        ["escribir frases en vez de acciones", "no incluir obstáculo"],
        "Pregunta: «¿esa acción se ve o se tiene que decir?». Si se tiene que decir, pídele convertirla en algo visible."),
    reinforce="Observa a distancia prudente una situación cotidiana (sin identificar a nadie) y anota quién, qué quería y qué le complicaba.",
    extend="Explica por qué mostrar una emoción con acciones suele comunicar más que decirla y da un ejemplo propio.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (improvisación de ejemplo, tema neutro). Dos personas esperan un bus que se demora. La persona uno dice: «Parece que hoy pasará más tarde». "
     "Respuesta uno de la persona dos: «No, el bus siempre llega a la hora». Respuesta dos: «Sí, y por eso traje un libro para compartir». Respuesta tres: «¿Viste lo que pasó en el partido?».")
build(
    O1, 3, F,
    use="Aprenderé reglas básicas de la improvisación (aceptar la propuesta, escuchar, no bloquear), a ensayar probando una variable y a registrar decisión, prueba y efecto, tanto en trabajo individual como grupal.",
    prior=["Sé armar una situación con objetivo y obstáculo.", "Sé cambiar una variable por vez.", "Sé respetar turnos y el espacio de otras personas."],
    explain=[
        "Improvisar es crear una escena en el momento, sin texto escrito, a partir de una situación dada. Funciona con tres reglas. Primero, aceptar la propuesta: lo que dice o hace la otra persona se toma como cierto dentro de la escena. Segundo, construir sobre ella («sí, y…»), agregando algo nuevo. Tercero, escuchar, porque lo que dice el otro da información para tu siguiente acción. Bloquear, es decir, rechazar o anular la propuesta del otro, detiene la escena.",
        "En una improvisación individual decides todo tú; en una grupal debes ajustar tu propuesta a lo que hacen los demás y cuidar que todos tengan turno. Cuando alguien domina, el grupo acuerda turnos breves. Los temas son neutros y cotidianos (esperar un bus, buscar un asiento); se evitan peleas reales, secretos personales y temas que incomoden.",
        "Después de improvisar se ensaya con orden. Se escribe la decisión (qué se quiso hacer), la prueba (qué se hizo, cambiando una sola variable) y el efecto (qué se observó). Si aparece un tema que incomoda o una situación de riesgo, se detiene el ejercicio y se avisa a una persona adulta.",
    ],
    vocab=[("improvisación", "escena creada en el momento, sin texto escrito"), ("aceptar", "tomar como cierto en la escena lo que propone otra persona"), ("bloquear", "rechazar o anular la propuesta del otro y detener la escena"), ("escucha", "atención a lo que dice y hace la otra persona"), ("registro de ensayo", "anotación de decisión, prueba y efecto")],
    worked=[
        ("Reconocer un bloqueo", "Una persona dice: «Parece que hoy llueve fuerte». Otra responde: «No, está despejado». ¿Qué pasó?", ["La segunda persona rechazó lo que la primera propuso como cierto.", "Eso detiene la escena porque no hay nada sobre qué construir."], "Bloqueó la propuesta"),
        ("Registrar un ensayo", "En una improvisación probaste hablar más bajo en la segunda mitad. Escribe el registro.", ["Decisión: mostrar que el personaje confía un secreto.", "Prueba: bajar el volumen solo en la segunda mitad. Efecto: la frase sonó más cercana y el público se inclinó."], "Decisión, prueba y efecto anotados"),
    ],
    mistakes=[("Responder con otro tema para evitar la propuesta del compañero.", "Cambiar de tema es una forma de bloquear y la escena pierde dirección.", "Acepta lo propuesto y agrega un dato nuevo."),
              ("Querer ganar la escena dominando la conversación.", "La improvisación grupal necesita turnos y escucha.", "Termina tu idea, escucha la siguiente y construye sobre ella.")],
    T=[
        ('abc', '¿Qué significa aceptar la propuesta en una improvisación?', 'Tomar como cierto en la escena lo que dijo o hizo la otra persona', 'Repetir exactamente sus palabras', 'Estar de acuerdo con todo lo que la otra persona opina fuera de la escena', 'Aceptar es una regla de la escena: lo propuesto pasa a ser real dentro de ella.'),
        ('abc', '{F} ¿Qué respuesta de la persona dos construye sobre la propuesta?', 'La respuesta dos', 'La respuesta uno', 'La respuesta tres', 'La dos acepta que el bus se demora y agrega un dato nuevo; la uno la niega y la tres cambia de tema.'),
        ('abc', 'Si en una improvisación aparece un tema que te incomoda, ¿qué haces?', 'Detienes el ejercicio y avisas a una persona adulta', 'Sigues con la escena para no cortar el trabajo del grupo ni arruinarlo', 'Esperas al final sin decir nada', 'La incomodidad es motivo suficiente para detener; la escena no vale más que el bienestar.'),
        ('abc', '¿Por qué escuchar es parte de improvisar?', 'Porque lo que dice la otra persona da información para tu siguiente acción', 'Porque así se sabe cuándo conviene dejar de participar en la escena', 'Porque permite memorizar el texto de la otra persona para repetirlo', 'Sin texto escrito, lo que dice el otro es el material con que se continúa.'),
        ('abc', 'En un ensayo, una variable es', 'un elemento que se cambia a propósito para comparar su efecto', 'un error de pronunciación que se debe corregir antes de repetir la prueba', 'el texto que se memoriza', 'La variable es lo único que se modifica para ver qué efecto produce.'),
        ('abc', '¿Cuál es un tema adecuado para improvisar en el aula?', 'Dos personas buscan dónde sentarse en una sala llena', 'Una pelea real entre dos compañeros', 'Un secreto personal de alguien del curso que todos conocen y quieren mostrar', 'El tema neutro permite crear sin exponer a nadie ni reabrir conflictos reales.'),
        ('=', 'En una ronda cada pareja actúa 2 minutos y comenta 1 minuto. Hay 7 parejas. ¿Cuántos minutos dura la ronda?', '7*(2+1)', 'Cada pareja usa 3 minutos en total y se multiplica por las 7 parejas.', ' minutos'),
        ('abc', '{F} La persona dos quiere mostrar impaciencia sin bloquear. ¿Qué respuesta sirve?', 'Sí, y ya llevo media hora mirando el reloj', 'No, ese bus siempre pasa a su hora y no se demora nunca', 'Mejor me voy y ya', 'Acepta que el bus se demora y agrega impaciencia; las otras niegan o cortan la escena.'),
        ('abc', '¿Cuál anotación de ensayo está completa?', 'Cambié solo el volumen a más bajo y la frase sonó como un secreto', 'Probé varias cosas distintas durante el ensayo y al final quedó mejor', 'Cambié todo en la escena y el resultado fue distinto al del inicio', 'Nombra la variable que cambió y el efecto observado; las otras son vagas.'),
        ('abc', 'En una improvisación grupal una persona habla siempre sin escuchar. ¿Qué ajuste propone el grupo?', 'Acordar turnos breves y que cada quien termine su idea antes de agregar la suya', 'Pedirle que no participe en las próximas rondas hasta que aprenda a escuchar al resto', 'Dejar que domine para terminar rápido', 'Los turnos resuelven el problema sin excluir a nadie.'),
        ('abc', '¿Qué diferencia hay entre improvisar solo y en grupo?', 'En grupo hay que ajustar la propia propuesta a lo que hacen los demás', 'En grupo no hace falta escuchar', 'En solitario se necesita siempre un texto escrito', 'La improvisación grupal depende de la escucha y del ajuste mutuo; la individual no.'),
        ('=', 'Un grupo improvisa 5 escenas de 3 minutos cada una y comenta 4 veces durante 2 minutos entre ellas. ¿Cuántos minutos dura todo?', '5*3+4*2', 'Se suman los minutos de las escenas y los de los comentarios intermedios.', ' minutos'),
        ('abc', 'Un grupo cambió solo la entrada del personaje (lenta o rápida); otro cambió entrada, voz y objetos a la vez. ¿Cuál puede decir qué produjo el efecto?', 'El primero, porque cambió una sola variable', 'El segundo, porque probó más cosas', 'Ninguno, pues no hay forma de saberlo', 'Con un único cambio se atribuye el efecto a esa variable.'),
    ],
    ctx=('=', 'En un curso de 12 estudiantes se improvisa en parejas, una pareja a la vez, y cada una dura 3 minutos. ¿Cuántos minutos tardan todas las parejas?', '12//2*3', 'Se calculan las parejas y se multiplican por la duración de cada una.', ' minutos'),
    sc=[
        ("En Teatro: ¿qué significa «sí, y…» en improvisación?", "Aceptar la propuesta y agregar algo nuevo", "Así la escena avanza sobre lo ya propuesto."),
        ("¿Qué es bloquear en una improvisación?", "Rechazar o anular la propuesta del otro y detener la escena", "El bloqueo corta lo que la otra persona había construido."),
        ("¿Qué se escribe en un registro de ensayo?", "La decisión, la prueba y el efecto observado", "Sirve para decidir qué conservar o cambiar."),
    ],
    op=("Escoge un tema neutro: esperar el turno en una oficina, buscar un asiento en un bus o armar una mesa para un cumpleaños. Escribe tres líneas de diálogo para una improvisación en que la persona dos acepta y construye sobre la propuesta de la uno. Luego anota una decisión, una prueba (una sola variable) y un efecto posible.",
        "Tema: buscar un asiento. Uno: «Creo que ese puesto está libre». Dos: «Sí, y al lado hay otro para tu amiga». Uno: «Entonces guardemos ambos». Registro: decisión, mostrar cooperación; prueba, hablar más suave; efecto, la escena se sintió más amable.",
        ["la persona dos acepta y construye", "no hay bloqueos", "el registro tiene decisión, prueba y efecto", "el tema es neutro"],
        ["diálogo de tres líneas y registro de ensayo"],
        ["responder con un bloqueo", "cambiar varias variables en la prueba"],
        "Pregunta: «¿la respuesta niega lo dicho o suma algo?». Si niega, pídele reescribirla con «sí, y…»."),
    reinforce="Con una persona de tu casa, improvisa dos minutos sobre un tema neutro aplicando «sí, y…» y comenta qué te costó.",
    extend="Explica por qué bloquear perjudica a toda la escena, no solo a quien fue bloqueado.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (situación de ejemplo, inventada). La misma frase: «Tengo una noticia para todos». "
     "Contexto 1: una sala pequeña, 8 personas sentadas a 3 metros. Contexto 2: un patio, 60 personas de pie a 15 metros. "
     "Propósito del grupo: que la noticia se perciba como una sorpresa alegre.")
build(
    O1, 4, F,
    use="Aprenderé a ajustar el cuerpo y la voz al propósito de la escena y al contexto (tamaño del espacio, distancia del público), proyectando sin gritar y cuidando la voz.",
    prior=["Distingo recursos del cuerpo y de la voz.", "Sé armar una situación con objetivo y obstáculo.", "Sé improvisar aceptando la propuesta de otra persona."],
    explain=[
        "El propósito de una escena es lo que el grupo quiere comunicar o provocar en el público: informar, emocionar, hacer reír, hacer pensar. Es distinto del objetivo del personaje, que es lo que el personaje quiere dentro de la historia. Por ejemplo, el personaje quiere cerrar el kiosco (objetivo) y el grupo quiere mostrar cómo la prisa vuelve injustas a las personas (propósito).",
        "El contexto también cambia lo que conviene hacer. En una sala pequeña, con el público cerca, bastan gestos pequeños y detallados y una voz natural. En un patio, con el público lejos, los gestos deben ser más amplios y la voz necesita proyección. Proyectar es hacer llegar la voz lejos apoyándola en la respiración y articulando con claridad, sin gritar. Articular es pronunciar con precisión las sílabas para que las palabras se entiendan.",
        "Cuidar la voz es parte del trabajo: tomar agua, hacer pausas y no forzar. Si hay dolor o ronquera, se detiene el ensayo y se avisa a una persona adulta. Cada decisión se evalúa por si sirve al propósito en ese contexto, no por si «se ve bien» en general.",
    ],
    vocab=[("propósito", "lo que el grupo quiere comunicar o provocar en el público"), ("contexto", "circunstancias del lugar y del público en que se presenta"), ("proyectar", "hacer llegar la voz lejos con apoyo de la respiración, sin gritar"), ("articular", "pronunciar con precisión para que se entienda cada palabra"), ("amplitud", "tamaño de un gesto o movimiento")],
    worked=[
        ("Distinguir propósito y objetivo", "Una escena muestra a un personaje que quiere llegar primero a la fila. El grupo quiere que el público se pregunte si vale la pena apurarse siempre. ¿Cuál es el objetivo y cuál el propósito?", ["Lo que el personaje quiere en la historia es llegar primero: objetivo.", "Lo que el grupo quiere provocar en el público es la reflexión: propósito."], "Objetivo: llegar primero; propósito: hacer pensar"),
        ("Ajustar al contexto", "Una escena de gestos pequeños se presentará en un gimnasio con el público a 20 metros. ¿Qué ajustes conviene probar?", ["Los gestos deben ser más amplios para verse a distancia.", "La voz necesita proyección y articulación, sin gritar."], "Gestos más amplios y voz proyectada y articulada"),
    ],
    mistakes=[("Gritar para que se oiga en un espacio grande.", "Forzar la voz la daña y no mejora la comprensión; lo que ayuda es el apoyo de la respiración y la articulación.", "Respira, apoya la voz y articula con claridad."),
              ("Usar el mismo tamaño de gesto en cualquier espacio.", "El gesto pequeño no se ve a distancia y el gigante resulta exagerado de cerca.", "Ajusta la amplitud a la distancia del público.")],
    T=[
        ('abc', '¿Qué es proyectar la voz?', 'Hacerla llegar lejos apoyándola en la respiración y articulando, sin gritar', 'Gritar lo más fuerte posible para que se escuche hasta el último puesto de la sala sin importar cómo suene', 'Hablar más rápido para ocupar menos tiempo', 'Proyectar usa respiración y claridad; gritar daña la voz y no asegura que se entienda.'),
        ('abc', '{F} ¿En cuál contexto conviene un gesto más amplio?', 'En el contexto 2, el patio con el público a 15 metros', 'En el contexto 1, la sala pequeña', 'En ambos por igual, porque la amplitud no depende de la distancia del público', 'A mayor distancia, el gesto debe ser más amplio para verse.'),
        ('abc', '¿Qué es el propósito de una escena?', 'Lo que el grupo quiere comunicar o provocar en el público', 'Lo que el personaje quiere conseguir', 'La duración de la escena', 'El propósito es del grupo hacia el público; el objetivo es del personaje.'),
        ('abc', '¿Para qué sirve articular bien?', 'Para que las palabras se entiendan aunque no se grite', 'Para hablar siempre más lento y marcar cada palabra aunque se pierda el ritmo', 'Para subir el tono de la voz', 'La articulación hace claras las sílabas y permite que la voz llegue comprensible.'),
        ('abc', 'El personaje quiere cerrar el kiosco; el grupo quiere mostrar cómo la prisa vuelve injustas a las personas. ¿Cuál es el propósito?', 'Mostrar cómo la prisa vuelve injustas a las personas', 'Cerrar el kiosco a tiempo para llegar a un ensayo', 'Que el público aprenda a ordenar mejor una plaza', 'Es lo que el grupo busca comunicar al público; lo otro pertenece a la historia.'),
        ('abc', 'En una sala pequeña con el público muy cerca, conviene', 'gestos pequeños y detallados y una voz natural', 'gestos enormes y voz muy fuerte para que el público lo note de inmediato', 'mantener una postura rígida y sin voz', 'La cercanía permite apreciar el detalle sin exagerar.'),
        ('=', 'Un trabalenguas se repite 5 veces; cada repetición dura 20 segundos y entre ellas hay 4 descansos de 10 segundos. ¿Cuántos segundos dura el ejercicio?', '5*20+4*10', 'Se suman las repeticiones y los descansos que hay entre ellas.', ' segundos'),
        ('abc', '{F} Para el contexto 2, ¿qué ajuste de voz es adecuado?', 'Más apoyo en la respiración, articulación clara y ritmo algo más lento', 'Gritar toda la frase y acelerar el ritmo para que no se note el cansancio', 'Hablar igual que en la sala pequeña', 'La distancia exige proyección y claridad; gritar o no ajustar no resuelve la comprensión.'),
        ('abc', 'En un ensayo largo, ¿cuál es una medida de cuidado de la voz?', 'Tomar agua, hacer pausas y parar si hay dolor, avisando a una persona adulta', 'Seguir hablando fuerte aunque duela, hasta terminar el ensayo completo', 'Susurrar con esfuerzo durante todo el ensayo, sin descansar nunca la voz', 'Forzar la voz con dolor puede dañarla; la pausa y el aviso son lo seguro.'),
        ('abc', 'Un grupo quiere hacer reír con una escena de torpeza, pero actúa con gestos mínimos y voz monótona. ¿Qué conviene revisar?', 'Gestos más amplios y ritmo variado que muestren la torpeza', 'Cambiar el propósito, porque reír con torpeza es demasiado difícil de lograr', 'Nada: el gesto mínimo siempre es mejor', 'Los recursos deben servir al propósito; la torpeza cómica necesita cuerpo y ritmo visibles.'),
        ('abc', '{F} Otro grupo presenta en el patio con gestos y voz de sala pequeña. ¿Cómo se explica que el público del fondo no entienda?', 'No ajustó amplitud ni proyección al contexto', 'El propósito de la escena era demasiado alegre', 'La frase tenía pocas palabras', 'El problema está en la adaptación al contexto; la frase y el propósito no impiden entender.'),
        ('=', 'Una sala tiene 6 filas de 8 sillas. Si asisten 36 personas, ¿cuántas sillas quedan vacías?', '6*8-36', 'Se calculan las sillas totales y se resta el público presente.', ' sillas'),
        ('abc', 'Un grupo planea presentar primero en la sala pequeña y luego en el patio. ¿Cuál plan adapta bien la escena?', 'Probar en el patio gestos más amplios y más proyección, manteniendo el propósito', 'Repetir la escena idéntica en el patio porque ya funcionó muy bien en la sala pequeña', 'Cambiar el propósito para que sea más fácil', 'Se ajustan los recursos al contexto y se conserva lo que el grupo quiere comunicar.'),
    ],
    ctx=('ab', 'Una escena con propósito de emocionar se presentará a un público de 60 personas en un patio. ¿Qué conviene hacer primero?', 'Ensayar en un espacio de tamaño parecido para ajustar amplitud y proyección', 'Ensayar solo en la sala de clases porque es más cómoda', 'Un espacio del tamaño del real permite probar si los recursos llegan al público.'),
    sc=[
        ("En Teatro: ¿qué diferencia hay entre propósito y objetivo?", "El propósito es del grupo hacia el público; el objetivo es del personaje en la historia", "Son niveles distintos: el grupo comunica y el personaje desea."),
        ("¿Qué es articular?", "Pronunciar con precisión cada sílaba para que se entienda", "La articulación mejora la comprensión sin gritar."),
        ("Si sientes dolor al forzar la voz en un ensayo, ¿qué haces?", "Detengo el ensayo, descanso y aviso a una persona adulta", "El dolor es señal de parar, no de seguir."),
    ],
    op=("Escoge una frase de ejemplo: «Tengo una noticia para todos» u «hoy nos toca cambiar de sala». Escribe un propósito para la escena y, para dos contextos (sala pequeña y patio), qué harías con la amplitud del gesto, la proyección y la articulación. Termina con una medida de cuidado de la voz.",
        "Frase «hoy nos toca cambiar de sala»; propósito: generar curiosidad. Sala: gestos pequeños y voz natural. Patio: gestos amplios, respiración y articulación clara. Cuidado: tomar agua y parar si hay dolor, avisando a una persona adulta.",
        ["propósito claro", "ajustes distintos para cada contexto", "incluye proyección y articulación", "incluye cuidado de la voz"],
        ["ficha con propósito y ajustes"],
        ["decir «gritar más» en el patio", "confundir propósito con objetivo del personaje"],
        "Pregunta: «¿qué haces distinto en el patio que en la sala y por qué?». Debe nombrar amplitud y proyección."),
    reinforce="Di una frase corta con volumen natural y luego con apoyo de respiración y articulación, sin gritar, y anota qué cambia.",
    extend="Explica cómo cambiarías una misma escena para presentarla en una sala pequeña y en un espacio abierto sin cambiar su propósito.",
)

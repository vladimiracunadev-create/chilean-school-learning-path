"""Cuaderno del estudiante de 2.º medio Artes Visuales: AR2M OA 03 (video, multimedia y creación contemporánea)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR2M OA 03"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Hojas y lápiz. Las fichas de los videos de ejemplo están escritas en la clase: no necesitas ver ni grabar nada. Si más adelante grabas, usa el teléfono con permiso de una persona adulta.",
    "Aprenderé a observar un video o una pieza multimedia mirando su contexto, su lenguaje visual (planos, ritmo, sonido) y su propósito. Sirve para decidir cómo contar una idea en imágenes en movimiento.",
    ["Sé separar contexto, lenguaje visual y propósito.", "Sé que una opinión no es lo mismo que un rasgo que se ve."],
    [
        "El video es una sucesión de imágenes en movimiento, casi siempre con sonido. La multimedia combina varios medios en una misma pieza: imagen, texto, sonido y animación. Son medios contemporáneos porque hoy se hacen y se ven con teléfonos, computadores y pantallas. Para observarlos uso las mismas tres preguntas: dónde se ve (contexto), cómo está hecho (lenguaje visual) y qué busca provocar (propósito).",
        "El lenguaje visual del video tiene herramientas propias. El plano es lo que muestra el encuadre. El plano general muestra el lugar completo; el plano medio muestra a una persona de la cintura hacia arriba; el primer plano muestra un rostro o un objeto muy de cerca. El ritmo es la velocidad con que cambian los planos: muchos cortes cortos dan ritmo rápido y pocos planos largos dan ritmo lento. El sonido también comunica: música, voz, ruido ambiente o silencio.",
        "El contexto de exhibición cambia la lectura. Un video visto en la pantalla pequeña de un teléfono necesita imágenes simples y letras grandes; en una proyección en la sala se pueden usar detalles. Describo primero lo que veo y oigo, interpreto con «podría sugerir» y juzgo con un criterio. Si el video muestra personas, recuerdo que grabar y mostrar a alguien exige su permiso.",
    ],
    [("plano", "lo que muestra el encuadre de la imagen"), ("primer plano", "plano muy cercano de un rostro o un objeto"), ("ritmo", "velocidad con que cambian los planos"), ("multimedia", "pieza que combina imagen, texto, sonido o animación"), ("contexto de exhibición", "lugar y pantalla donde se ve la pieza")],
    [
        w("Leer una ficha de video", "Video de ejemplo «Lluvia en el Paradero», 40 s, hecho para verse en el teléfono: 6 planos. Plano 1, general del paradero, 8 s. Plano 2, medio de una persona esperando, 6 s. Plano 3, primer plano de manos con un paraguas, 5 s. Planos 4, 5 y 6 duran 7, 8 y 6 s. Sonido: lluvia suave y un silencio final de 2 s. ¿Qué duración tienen los tres planos que faltan sumados y qué propósito probable tiene?", ["Planos 4, 5 y 6: 7 + 8 + 6 = 21 s.", "Comprobación: 8 + 6 + 5 + 21 = 40 s.", "Propósito probable: mostrar la espera y el cansancio del viaje diario."], "21 s; mostrar la espera del viaje diario"),
        w("Efecto del ritmo", "Un video de ejemplo de 30 s tiene 3 planos. Otro de 30 s tiene 10 planos. ¿Cuál tiene ritmo más rápido?", ["Plano promedio del primero: 30 ÷ 3 = 10 s.", "Plano promedio del segundo: 30 ÷ 10 = 3 s.", "Planos más cortos significan cortes más frecuentes."], "El de 10 planos, porque sus planos son más cortos"),
    ],
    [
        m("Decir «el video es aburrido» y creer que eso es observar.", "Es una opinión, no un rasgo que se compruebe.", "Escribe rasgos como «tiene tres planos largos y solo sonido de lluvia» y luego juzga con un criterio."),
        m("Mirar solo la imagen y olvidar el sonido y el lugar donde se ve.", "El sonido y la pantalla cambian lo que el video comunica.", "Anota los tres: imagen, sonido y contexto de exhibición."),
    ],
    [
        ex("En Artes Visuales, ¿qué es un plano? A. Lo que muestra el encuadre de la imagen B. La música del video.", "A", "Plano es el encuadre; la música es sonido."),
        ex("¿Qué plano muestra un rostro o un objeto muy de cerca? A. Primer plano B. Plano general.", "A", "El primer plano acerca la cámara al detalle."),
        ex("La multimedia combina… A. Varios medios, como imagen, texto y sonido B. Solo fotografías sin sonido.", "A", "Multimedia significa varios medios en una pieza."),
    ],
    [
        ex("Un video muestra todo un patio con muchas personas. ¿Qué plano usa? A. Plano general B. Primer plano.", "A", "Muestra el lugar completo."),
        ex("Un video se verá en la pantalla pequeña de un teléfono. ¿Qué decisión conviene? A. Letras grandes e imágenes simples B. Letras muy pequeñas con muchos detalles.", "A", "En pantallas pequeñas se pierde el detalle."),
        ex("Dato de un video de ejemplo: «se oye lluvia suave y luego hay 2 s de silencio». ¿Es dato de imagen o de sonido?", "De sonido", "Describe lo que se oye, no lo que se ve."),
    ],
    [
        ex("¿Qué muestra un plano medio? A. A una persona de la cintura hacia arriba B. El lugar completo con todas las personas.", "A", "El plano medio acerca la cámara a la persona; el plano general muestra el lugar."),
        ex("Un video de ejemplo cambia de plano cada 2 s. Otro cambia cada 10 s. ¿Cuál tiene ritmo más lento? A. El de 10 s B. El de 2 s.", "A", "Planos más largos significan menos cortes."),
        ex("¿Cuál frase es una interpretación? A. «El silencio final podría sugerir cansancio» B. «El silencio final dura 2 s».", "A", "La primera propone un significado; la segunda describe."),
    ],
    [
        ex("Un video de ejemplo sobre el ruido en un barrio no tiene sonido. ¿Qué pierde? A. Una herramienta clave para mostrar su tema B. Su duración.", "A", "El sonido es parte del lenguaje del video y aquí sería central."),
        ex("Un compañero dice: «el video es lento porque no me gusta». ¿Cuál es un criterio comprobable? A. Cada plano dura más de 8 s B. A mí me aburre.", "A", "Se puede medir la duración de los planos."),
    ],
    [
        ex("Un video de ejemplo se proyectará en una sala con 30 estudiantes. ¿Qué cambia respecto del teléfono? A. Se pueden usar más detalles B. Se debe hacer más pequeño.", "A", "Una pantalla grande permite imágenes más detalladas."),
        ex("Dos videos de ejemplo tratan del mismo patio. U dura 30 s con 3 planos y solo música; V dura 30 s con 12 planos y ruido de pasos. Quieres mostrar el bullicio del recreo. ¿Cuál conviene? A. V B. U.", "A", "Más cortes y ruido ambiente transmiten movimiento y bullicio."),
    ],
    ex("Quieres grabar a tus primos jugando en una plaza para un proyecto escolar. ¿Qué haces antes de mostrar el video? A. Pedir permiso a ellos y a una persona adulta B. Subirlo sin avisar.", "A", "Toda persona grabada debe saber y aceptar cómo se mostrará."),
    [
        ex("¿Cuáles son las tres cosas que se observan de un video?", "Contexto, lenguaje visual y propósito", "Juntas dicen dónde se ve, cómo está hecho y para qué."),
        ex("Verdadero o falso: el silencio puede ser una decisión de sonido.", "Verdadero", "Una pausa también comunica."),
        ex("¿Qué es ritmo en un video?", "La velocidad con que cambian los planos", "Cortes frecuentes dan ritmo rápido."),
    ],
    task(
        "Elige UN video de ejemplo. A) «Pasos de Lunes»: 36 s, plano general de un pasillo, primer plano de zapatillas y plano medio de dos estudiantes, sonido de pasos y una voz que cuenta; se verá en una sala. B) «Hojas»: 30 s, un solo plano fijo de un árbol, sin voz, con sonido de viento; se verá en el teléfono. C) «Mensaje»: 40 s, imágenes de letras en movimiento con música suave; se verá en una pantalla de un hall. Escribe una ficha con contexto, dos rasgos de lenguaje visual o sonido y un propósito; agrega una interpretación con «podría» y un juicio apoyado en un criterio.",
        "Elegí B. Contexto: teléfono. Rasgos: un solo plano fijo de 30 s; sonido de viento sin voz. Propósito: invitar a observar con calma. Interpretación: el plano fijo podría sugerir paciencia. Juicio: funciona en teléfono porque la imagen es simple y no hay detalles pequeños.",
        ["separa contexto, lenguaje y propósito", "usa términos como plano, ritmo o sonido", "escribe una interpretación con «podría»", "apoya el juicio en un criterio comprobable"],
        ["ficha de observación", "interpretación y juicio con criterio"],
        ["decir solo si le gusta o no", "olvidar el sonido o la pantalla"],
        "Pregunta qué rasgo del video respalda el juicio y si dependió del lugar donde se vería.",
    ),
    "Mira un video corto de tu teléfono sin sonido y anota cuántos planos distintos alcanzas a contar.",
    "Explica con tres frases cómo cambia un video si se ve en un teléfono o proyectado en una sala.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Hojas, lápiz y, si tienes, un teléfono para hacer fotos de objetos sobre una mesa. Los referentes son fichas de ejemplo inventadas; no necesitas buscar videos.",
    "Aprenderé a explorar los materiales y las técnicas de un video o de una pieza multimedia: cámara, luz, plano, ángulo y animación fotograma a fotograma. Sirve para elegir con razones cómo producir mi pieza.",
    ["Sé reconocer planos, ritmo y sonido.", "Sé que un referente se transforma y no se copia."],
    [
        "Los materiales del video no son solo la cámara. Importan la luz (natural es la más simple), el espacio, el sonido y el tiempo de grabación. El teléfono sirve como cámara si se apoya sobre libros para que no tiemble. La luz de una ventana, de lado, da volumen a los objetos; si la ventana queda detrás del objeto (contraluz), el objeto se ve oscuro y sin detalles.",
        "El ángulo es la altura de la cámara respecto de lo que se graba. Un ángulo desde arriba (picado) hace ver pequeño al objeto; desde abajo (contrapicado) lo hace ver grande. La animación fotograma a fotograma consiste en sacar muchas fotos de un objeto moviéndolo un poco entre cada una y mostrarlas rápido. Si muestro 10 fotos por segundo (cifra de ejemplo; cada proyecto elige la suya), un video de 4 s necesita 40 fotos.",
        "Un referente es un video que sirve de inspiración. Lo analizo en tres puntos: qué plano usa, qué sonido usa y qué decisión tomó el autor. Luego tomo una idea y la transformo con mi tema. Si uso música o imágenes de otras personas, necesito su permiso o debo elegir material libre; lo más simple es crear mi propio sonido con la voz, palmadas o ruidos de objetos.",
    ],
    [("ángulo", "altura de la cámara respecto de lo que se graba"), ("picado", "ángulo desde arriba que hace ver pequeño al sujeto"), ("contrapicado", "ángulo desde abajo que hace ver grande al sujeto"), ("fotograma", "cada imagen fija que forma un video"), ("animación fotograma a fotograma", "técnica que mueve un objeto un poco entre fotos")],
    [
        w("Calcular fotogramas", "Quieres una animación de ejemplo de 6 s mostrando 10 fotos por segundo. ¿Cuántas fotos debes sacar?", ["Fotos por segundo: 10.", "Duración: 6 s.", "Multiplico: 10 × 6 = 60 fotos."], "60 fotos"),
        w("Elegir un ángulo", "Una ficha de referente dice: «para mostrar una torre de latas poderosa, la cámara está en el piso mirando hacia arriba». ¿Qué ángulo es y qué efecto busca?", ["La cámara está abajo, mirando hacia arriba.", "Ese ángulo se llama contrapicado.", "Efecto: hace ver la torre grande e imponente."], "Contrapicado; hace ver la torre grande"),
    ],
    [
        m("Poner la ventana detrás del objeto porque «ahí hay luz».", "El sujeto queda oscuro y sin detalles.", "Coloca la ventana al costado del objeto, no detrás."),
        m("Usar la canción de otra persona sin permiso porque «es solo un trabajo escolar».", "La música tiene autor y derechos.", "Crea tu propio sonido o pide autorización."),
    ],
    [
        ex("¿Qué es un fotograma? A. Una imagen fija de un video B. Un tipo de música.", "A", "El video está formado por muchos fotogramas."),
        ex("Un ángulo desde arriba que hace ver pequeño al objeto se llama… A. Picado B. Contrapicado.", "A", "Picado significa cámara arriba mirando hacia abajo."),
        ex("¿Dónde conviene poner la ventana para iluminar un objeto? A. A un costado del objeto B. Detrás del objeto.", "A", "La luz lateral muestra volumen y detalles."),
    ],
    [
        ex("¿Qué técnica mueve un objeto un poco entre foto y foto? A. Animación fotograma a fotograma B. Plano general.", "A", "Esa técnica crea la ilusión de movimiento."),
        ex("Para que el teléfono no tiemble al grabar conviene… A. Apoyarlo sobre libros o una superficie firme B. Sostenerlo con una mano en el aire.", "A", "Una base firme estabiliza la imagen."),
        ex("Si quieres que una persona se vea grande e imponente, ¿qué ángulo usas? A. Contrapicado B. Picado.", "A", "Mirar hacia arriba agranda al sujeto."),
    ],
    [
        arith("Una animación de ejemplo dura 8 s y muestra 12 fotos por segundo. ¿Cuántas fotos necesita?", "8 * 12", "Se multiplica la duración por las fotos por segundo.", " fotos"),
        ex("Ya sacaste 36 de 50 fotos y al verlas seguidas el objeto da saltos bruscos. ¿Qué ajuste conviene? A. Moverlo menos entre una foto y la siguiente B. Mostrar menos fotos por segundo.", "A", "Los saltos vienen de mover demasiado entre fotos; con movimientos pequeños se ve continuo."),
        ex("Quieres sonido propio para tu video sobre un patio. ¿Qué es mejor? A. Grabar tus palmadas y pasos B. Copiar una canción popular entera.", "A", "El sonido propio no depende de derechos ajenos."),
    ],
    [
        ex("Un referente de ejemplo tiene un solo plano largo y música lenta. Tu tema es una carrera de relevos. ¿Qué decisión propia transforma el referente? A. Usar planos cortos y sonido rápido B. Copiar el plano largo y la música lenta.", "A", "El tema pide energía; cambiar el ritmo muestra autoría."),
        ex("Dos versiones de la misma escena, una con luz de ventana de lado y otra con la ventana detrás. ¿Cuál muestra mejor los detalles del objeto? A. La de ventana al lado B. La de ventana detrás.", "A", "La luz lateral ilumina el objeto de frente."),
    ],
    [
        ex("Un compañero quiere grabar sobre un puente alto para una toma contrapicada. ¿Qué respondes? A. Mejor tomar desde el suelo en un lugar seguro y con una persona adulta cerca B. Que se asome para que se vea más impactante.", "A", "El riesgo de caída hace inaceptable la propuesta; el efecto se logra desde el suelo."),
        ex("Una amiga dice que su animación necesita 15 fotos por segundo y quiere 3 s. Otra dice que 40 fotos bastan. ¿Quién tiene razón? Responde: la primera o la segunda.", "La primera", "15 × 3 = 45 fotos; 40 no alcanzan."),
    ],
    ex("Para el cumpleaños de un amigo grabas un saludo con cuatro personas. ¿Qué haces con la luz si el espacio es una sala con ventana? A. Pones la ventana a un costado de las personas B. Las pones con la ventana detrás de ellas.", "A", "Así se ven los rostros y se evita el contraluz."),
    [
        ex("Verdadero o falso: un fotograma es una imagen fija.", "Verdadero", "El video es una sucesión de fotogramas."),
        ex("¿Qué ángulo hace ver pequeño al objeto?", "Picado", "La cámara arriba mira hacia abajo."),
        ex("¿Qué haces si quieres usar una canción de otra persona?", "Pedir permiso o elegir otro sonido", "La música tiene autor y derechos."),
    ],
    task(
        "Planifica la exploración de un video corto. Opciones de tema: A) la espera en un paradero; B) un objeto de tu casa que se «transforma»; C) un sonido del barrio. Para el tema que elijas, decide: qué tipo de plano usarás, el ángulo, dónde estará la luz, el sonido que crearás tú y cuántas fotos necesitarías si hicieras una animación de 5 s a 10 fotos por segundo. Indica qué idea tomas de un referente de ejemplo y cómo la transformas.",
        "Elegí B, un lápiz que se transforma en torre. Plano: primer plano. Ángulo: contrapicado para verlo grande. Luz: ventana al lado. Sonido propio: golpes suaves con la palma. Fotos: 10 × 5 = 50. Referente: un plano largo con música lenta; yo lo cambio por cortes rápidos y sonido de golpes.",
        ["elige plano, ángulo y luz con una razón", "crea sonido propio", "calcula bien las fotos", "transforma una idea del referente"],
        ["plan con plano, ángulo, luz y sonido", "cálculo de fotos"],
        ["copiar el referente", "usar música ajena"],
        "Pregunta por qué eligió ese ángulo y si el sonido es de su autoría.",
    ),
    "Apoya tu teléfono en libros y compara dos fotos de un objeto, una con la ventana al costado y otra con la ventana detrás del objeto.",
    "Escribe tres frases que expliquen cuándo conviene un ángulo contrapicado.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Hojas, lápiz, reloj o temporizador del teléfono. Los datos de las pruebas están escritos en la clase. Para probar, graba pruebas cortas de 10 segundos en un lugar seguro de tu casa.",
    "Aprenderé a probar decisiones de encuadre, duración, ritmo y sonido en un video corto. Sirve para elegir cómo contar mi idea antes de producir la versión final.",
    ["Sé reconocer plano, ritmo, ángulo y fotograma.", "Sé calcular fotos y duración."],
    [
        "Probar es comparar dos versiones cambiando una sola cosa. Puedo comparar un plano general con un primer plano, un corte cada 3 s con un corte cada 8 s, o una pieza con sonido y otra con silencio. Anoto el resultado en una frase: qué cambié, qué efecto vi u oí y qué decido. Si cambio muchas cosas a la vez, no sé cuál produjo el efecto.",
        "La composición del encuadre se puede probar con la regla de los tercios: imagino la imagen dividida en tres columnas y tres filas. Poner el objeto principal sobre una de las líneas, y no siempre en el centro, suele dar una imagen más viva. Es una guía y no una obligación: se puede romper con intención. También pruebo la duración: un plano de 3 s se lee como un vistazo; uno de 10 s invita a contemplar.",
        "La edición es ordenar y cortar los planos. Una pieza de 30 s con 6 planos tiene en promedio 5 s por plano. Si el tema es una carrera, conviene un ritmo rápido; si es calma, uno lento. Pruebo con 10 segundos, comparo y elijo según mi propósito. En este cuaderno no se enseña un programa en particular, porque eso depende del taller y del docente.",
    ],
    [("edición", "ordenar y cortar los planos de un video"), ("regla de los tercios", "guía que divide la imagen en tres columnas y tres filas"), ("composición", "forma de ordenar los elementos dentro del encuadre"), ("corte", "paso de un plano a otro"), ("prueba", "versión corta para comparar decisiones")],
    [
        w("Calcular el ritmo", "Una pieza de ejemplo dura 30 s y tiene 6 planos de igual duración. Otra dura 30 s y tiene 15 planos de igual duración. ¿Cuánto dura un plano en cada una?", ["Primera: 30 ÷ 6 = 5 s.", "Segunda: 30 ÷ 15 = 2 s.", "La segunda tiene ritmo más rápido."], "5 s en la primera y 2 s en la segunda"),
        w("Elegir según el propósito", "Propósito de ejemplo: mostrar la calma de una tarde en una plaza. Opciones: X con cortes cada 2 s y música rápida; Y con planos de 8 s y sonido de viento. ¿Cuál eliges?", ["Propósito: calma.", "Y tiene planos largos y sonido suave.", "Elijo Y."], "Y, porque su ritmo lento transmite calma"),
    ],
    [
        m("Cambiar plano, sonido y duración a la vez en la misma prueba.", "No se sabe cuál cambio produjo el efecto.", "Cambia una sola cosa por prueba."),
        m("Poner siempre el objeto en el centro del encuadre sin probar otra opción.", "Es una decisión que no se comparó.", "Prueba el objeto sobre una línea de los tercios y compara."),
    ],
    [
        ex("¿Qué es la edición de un video? A. Ordenar y cortar los planos B. Cambiar la marca del teléfono.", "A", "Edición es dar orden y ritmo a los planos."),
        ex("Un video con cortes muy frecuentes tiene ritmo… A. Rápido B. Lento.", "A", "Muchos cortes aceleran el ritmo."),
        ex("¿Cuántas cosas conviene cambiar entre una prueba y otra?", "Una", "Así se sabe qué produjo el efecto."),
    ],
    [
        ex("Con la regla de los tercios, ¿dónde se puede poner el objeto principal? A. Sobre una de las líneas B. Siempre exactamente en el centro.", "A", "Las líneas de los tercios dan un punto fuerte a la imagen."),
        ex("Un plano de 3 s se lee como… A. Un vistazo B. Una contemplación larga.", "A", "Un plano corto no da tiempo para detenerse."),
        ex("Si quieres transmitir calma, ¿qué ritmo eliges? A. Lento B. Muy rápido.", "A", "Los planos largos dan sensación de calma."),
    ],
    [
        ex("Dos pruebas de 10 s: una tiene 2 planos de 5 s y la otra 5 planos de 2 s. ¿Cuál tiene ritmo más rápido? A. La de 5 planos de 2 s B. La de 2 planos de 5 s.", "A", "Planos más cortos significan cortes más frecuentes."),
        arith("Un video de ejemplo tiene 4 planos de 6 s y 3 planos de 4 s. ¿Cuántos segundos dura?", "4 * 6 + 3 * 4", "Se multiplica cada grupo y se suman los totales.", " s"),
        ex("Quieres mostrar una carrera de relevos de forma emocionante. ¿Qué prueba esperas que funcione mejor? A. Cortes cada 2 s con sonido de pasos rápidos B. Un plano de 20 s sin sonido.", "A", "El ritmo rápido transmite la energía de una carrera."),
    ],
    [
        ex("Una compañera probó un plano general y un primer plano, pero también cambió la música entre ambas. ¿Puede concluir qué plano funciona mejor? Responde sí o no.", "No", "Cambió dos cosas a la vez."),
        ex("Un video de ejemplo debe terminar en 36 s, tiene 5 planos de 6 s y falta un último plano. ¿Cuánto debe durar? A. 6 s B. 12 s.", "A", "5 × 6 = 30 s y 36 − 30 = 6 s."),
    ],
    [
        ex("Tu prueba de 10 s muestra que el objeto se pierde en una esquina. ¿Qué decisión tomas? A. Moverlo a una línea de los tercios y repetir la prueba B. Dejarlo igual.", "A", "Recomponer el encuadre y volver a probar es parte del proceso."),
        ex("Dos planos de ejemplo de 4 s: en el primero el objeto está justo al centro; en el segundo, sobre una línea de los tercios. Buscas una imagen más viva según la guía. ¿Cuál eliges? A. El segundo B. El primero.", "A", "La guía de los tercios propone ubicar el punto de interés sobre una línea."),
    ],
    ex("Estás probando dos versiones de un saludo grabado en tu casa. Una tiene voz y otra silencio con subtítulos. Tu familiar escucha poco. ¿Qué versión conviene? A. La de subtítulos B. La de voz, porque es más natural.", "A", "El texto permite entender el mensaje sin oírlo."),
    [
        ex("¿Qué se hace tras cada prueba?", "Anotar qué se cambió, el efecto y la decisión", "Así queda evidencia del proceso."),
        ex("Verdadero o falso: la regla de los tercios es una obligación.", "Falso", "Es una guía que se puede romper con intención."),
        ex("Un plano de 10 s invita a…", "Contemplar", "La duración larga da tiempo para detenerse."),
    ],
    task(
        "Planifica dos pruebas de 10 s para un propósito a elegir: A) transmitir calma en una plaza; B) transmitir energía en una carrera; C) mostrar curiosidad ante un objeto pequeño. Para cada prueba escribe cuántos planos tendría, cuánto dura cada uno, qué sonido y qué UNA cosa cambias entre la prueba 1 y la 2. Indica con qué criterio elegirás.",
        "Elegí C. Prueba 1: 2 planos de 5 s, primer plano del objeto y plano medio de la mano; sonido de pasos suaves. Prueba 2: 5 planos de 2 s, mismo sonido; cambié solo la duración de los planos. Criterio: cuál transmite más curiosidad por el objeto. Elegiré la que haga querer mirar de cerca.",
        ["cambia una sola cosa entre pruebas", "calcula bien la duración de los planos", "elige con un criterio ligado al propósito", "registra el resultado"],
        ["plan de dos pruebas", "criterio de elección"],
        ["cambiar varias cosas a la vez", "no justificar la elección"],
        "Pregunta qué cambió entre una prueba y otra y qué efecto esperaba.",
    ),
    "Graba en tu teléfono dos clips de 5 s de un mismo objeto, uno desde arriba y otro desde el costado, y compara el efecto.",
    "Explica en tres frases por qué conviene cambiar una sola cosa por prueba.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Hojas cuadriculadas o en blanco, regla y lápiz. Los temas y los datos están escritos en la clase. Si grabas, hazlo con permiso de una persona adulta, en un lugar seguro y con consentimiento de quien aparezca.",
    "Aprenderé a desarrollar una propuesta propia de video corto o pieza multimedia con tema, guion gráfico, tabla de planos, sonido y cuidado de permisos. Sirve para planificar antes de grabar.",
    ["Sé elegir plano, ángulo, luz y ritmo.", "Sé probar una decisión cambiando una sola cosa."],
    [
        "Un guion gráfico (en inglés storyboard) es una historieta simple que dibuja cada plano en un recuadro, con una nota de lo que se ve, el sonido y la duración. Sirve para que otra persona entienda mi idea sin verla grabada. Cada recuadro debe indicar el tipo de plano, qué ocurre y cuánto dura. Con la suma de las duraciones calculo el largo total del video.",
        "Parto de un desafío creativo, por ejemplo «un video de 40 segundos que muestre cómo se usa un espacio de la sala». Elijo qué contaré, para quién y en qué pantalla se verá. Luego dibujo el guion gráfico, la tabla de planos y escribo qué sonido haré yo mismo. El video debe poder hacerse con objetos cotidianos y sin programas especiales; si se usa un programa de edición, lo enseña el docente.",
        "Cuido tres cosas éticas. Primero, el consentimiento: solo grabo a personas que aceptan y sé quién verá el video. Segundo, la autoría: el guion y las imágenes son míos, y si tomo algo de otra persona, la nombro. Tercero, la seguridad: grabo en lugares conocidos, sin subirme a nada alto y sin caminar por la calle mirando la pantalla. Si algo me incomoda, se lo cuento a una persona adulta de confianza.",
    ],
    [("guion gráfico", "historieta de recuadros que planifica cada plano del video"), ("tabla de planos", "lista con tipo de plano, qué ocurre y duración"), ("consentimiento", "permiso de una persona para ser grabada y mostrada"), ("duración total", "suma de la duración de todos los planos"), ("autoría", "decisiones y creación propias del autor")],
    [
        w("Armar una tabla de planos", "Video de ejemplo sobre la hora de recreo, 36 s: plano 1 general del patio, 8 s; plano 2 medio de dos estudiantes conversando, 7 s; plano 3 primer plano de una pelota, 6 s; plano 4 general del patio vacío, 9 s. ¿Cuánto falta para 36 s?", ["Suma: 8 + 7 + 6 + 9 = 30 s.", "Faltan: 36 − 30 = 6 s.", "Puedo agregar un plano 5 de 6 s."], "Faltan 6 s"),
        w("Cuidar el consentimiento", "Quieres grabar a una compañera en el plano medio. ¿Qué haces antes de grabar y de mostrar?", ["Le explico para qué es el video y quién lo verá.", "Ella decide si acepta y puede decir que no.", "Si no acepta, uso un objeto o una silueta."], "Pedir su permiso e informarle quién verá el video"),
    ],
    [
        m("Grabar primero y planificar después.", "Se pierde tiempo y se repiten tomas.", "Dibuja el guion gráfico y la tabla de planos antes de grabar."),
        m("Mostrar el video de una persona sin avisarle.", "Toda persona tiene derecho a decidir sobre su imagen.", "Pide permiso y explica dónde se verá."),
    ],
    [
        ex("¿Qué es un guion gráfico? A. Una historieta de recuadros que planifica los planos B. Un tipo de cámara.", "A", "Dibuja cada plano antes de grabar."),
        ex("¿Qué debe decir cada recuadro del guion? A. Tipo de plano, qué ocurre y duración B. Solo el título del video.", "A", "Así otra persona entiende la idea."),
        ex("Antes de grabar a una compañera, ¿qué necesitas? A. Su consentimiento B. Que ella no se entere.", "A", "Hay que pedir permiso."),
    ],
    [
        ex("Un video de ejemplo debe durar 40 s. ¿Qué parte del guion te ayuda a saber cuánto dura? A. La suma de la duración de los planos B. El color de la portada.", "A", "La duración total es la suma de cada plano."),
        ex("Quieres grabar un plano contrapicado desde el suelo de tu patio. ¿Es una decisión segura? A. Sí, si el lugar es conocido y sin riesgos B. Sí, aunque sea sobre una ventana alta.", "A", "No se graba en lugares con riesgo de caída."),
        ex("¿Cuál es una buena idea para el sonido de tu video? A. Grabar tus propias palmadas o pasos B. Usar una canción conocida completa.", "A", "El sonido propio resguarda la autoría."),
    ],
    [
        arith("Tu video planificado tiene 5 planos de 6 s y 2 planos de 5 s. ¿Cuántos segundos dura?", "5 * 6 + 2 * 5", "Se calcula cada grupo y se suman.", " s"),
        ex("Recuadro de ejemplo del guion: «Primer plano de unas manos que atan un cordón; se oyen golpecitos suaves». ¿Qué dato obligatorio falta? A. La duración en segundos B. El nombre del curso.", "A", "Cada recuadro debe indicar tipo de plano, qué ocurre y cuánto dura; sin la duración no se puede sumar el total."),
        ex("Desafío: un video de 30 s que muestre cómo se usa la sala de estudio. ¿Qué plano usarías para mostrar la sala completa? A. Plano general B. Primer plano de un lápiz.", "A", "El plano general muestra el espacio entero."),
    ],
    [
        ex("Un compañero propone usar un fragmento de un video de otra persona sin avisar «porque está en internet». ¿Qué respondes? A. Que debe pedir permiso o nombrar la autoría, o mejor, hacer su propio material B. Que no importa si es corto.", "A", "Estar en internet no quita el derecho del autor."),
        ex("Tu tabla suma 52 s y el límite es 45 s. ¿Qué ajuste conviene? A. Acortar uno o dos planos B. Agregar más planos.", "A", "Hay que bajar la duración total."),
    ],
    [
        ex("Un familiar te pide que grabes un video en el techo de la casa para tener «una toma desde arriba». ¿Qué respondes? A. No, busco otro lugar seguro y con una persona adulta cerca B. Sí, con cuidado.", "A", "Un techo es un lugar peligroso."),
        ex("Un guion tiene cuatro planos de 9 s y el límite es 45 s. ¿Cabe un quinto plano de 8 s? Responde sí o no.", "Sí", "4 × 9 = 36 s; 36 + 8 = 44 s, que es menos de 45 s."),
    ],
    ex("Una amiga no quiere aparecer en tu video. ¿Qué haces? A. Respetarlo y usar manos, objetos o siluetas B. Convencerla hasta que acepte.", "A", "Su decisión debe respetarse sin presión."),
    [
        ex("¿Qué tres datos pones en cada recuadro del guion gráfico?", "Tipo de plano, qué ocurre y duración", "Permiten planificar y calcular el total."),
        ex("Verdadero o falso: grabar a una persona sin avisar es aceptable si el video es corto.", "Falso", "Siempre se necesita consentimiento."),
        ex("Si te incomoda algo durante la grabación, ¿qué haces?", "Se lo cuento a una persona adulta de confianza", "Así se cuida la seguridad."),
    ],
    task(
        "Diseña la propuesta de un video corto de entre 30 y 45 s. Elige UN tema: A) un rincón de tu casa a distintas horas; B) la preparación de una merienda sencilla sin uso de fuego ni cuchillos; C) el recorrido de un objeto por una mesa. Escribe un guion gráfico en palabras con al menos cinco planos (tipo de plano, qué ocurre y duración en segundos), suma la duración total, indica el sonido que harás tú y cómo cuidas el consentimiento y la seguridad.",
        "Elegí C. Planos: 1) general de la mesa, 6 s; 2) primer plano del objeto, 5 s; 3) plano medio de la mano que lo mueve, 7 s; 4) contrapicado desde la mesa, 6 s; 5) general final, 8 s. Total: 6 + 5 + 7 + 6 + 8 = 32 s. Sonido: golpes suaves que hago con los dedos. Consentimiento: solo aparece mi mano. Seguridad: grabo en mi mesa con luz de ventana.",
        ["tiene al menos cinco planos con duración", "suma bien la duración total", "propone sonido propio", "cuida el consentimiento y la seguridad"],
        ["guion gráfico en palabras", "suma de duraciones y nota de cuidados"],
        ["no planificar la duración", "olvidar el consentimiento"],
        "Pregunta cómo se calculó la duración y qué decisión del guion es propia.",
    ),
    "Dibuja cuatro recuadros de un guion gráfico para un video de 20 s sobre tu desayuno.",
    "Escribe dos frases que expliquen por qué es importante pedir consentimiento para grabar a una persona.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Hojas y lápiz. La pauta, los puntajes y las piezas de ejemplo están escritos en la clase.",
    "Aprenderé a contrastar un video o una pieza multimedia con criterios de propósito, lenguaje visual, ritmo, sonido y ética. Sirve para decidir qué conservar y qué cambiar en la versión final.",
    ["Sé armar un guion gráfico con tabla de planos.", "Sé probar decisiones cambiando una cosa a la vez."],
    [
        "Contrastar es comparar la pieza con criterios claros. En esta clase uso cinco, cada uno de 0 a 2 puntos: propósito (se entiende qué quiere provocar), lenguaje visual (planos y ángulos coherentes con la idea), ritmo (duración y cortes adecuados), sonido (aporta y es propio o autorizado) y cuidado ético (hay consentimiento y seguridad). El máximo es 10 puntos.",
        "Cada puntaje se apoya en evidencia: el guion gráfico, la tabla de duraciones, la nota de permisos y las pruebas de 10 segundos. Además reviso la accesibilidad, es decir, que más personas puedan entender la pieza. Los subtítulos ayudan a quien no oye bien o ve el video sin sonido, y un texto con buen contraste (claro sobre fondo oscuro, o al revés) se lee mejor.",
        "Después propongo un ajuste concreto para el criterio más bajo, como acortar los planos para acelerar el ritmo. No evalúo a la persona sino a la pieza. En este nivel, el uso de un programa de edición y la exhibición en pantallas especiales dependen del taller y del docente; aquí practico la planificación y el análisis.",
    ],
    [("accesibilidad", "facilidad con que más personas pueden entender una pieza"), ("subtítulos", "texto escrito de lo que se dice o se oye"), ("contraste", "diferencia clara entre el color del texto y el del fondo"), ("coherencia", "acuerdo entre las decisiones visuales y el propósito"), ("ajuste", "cambio concreto para mejorar la versión")],
    [
        w("Aplicar la pauta", "Pauta de 5 criterios de 0 a 2 puntos. Video de ejemplo «Hora del Recreo»: propósito 2, lenguaje visual 1, ritmo 2, sonido 1, cuidado ético 2. ¿Cuál es el total y cuál criterio conviene ajustar?", ["Suma: 2 + 1 + 2 + 1 + 2 = 8 puntos.", "Los puntajes más bajos son lenguaje visual y sonido, con 1.", "Elijo uno, por ejemplo el sonido."], "8 de 10; ajustar sonido o lenguaje visual"),
        w("Mejorar la accesibilidad", "El video «Hora del Recreo» se verá en un hall con ruido. ¿Qué agregas para que todos entiendan?", ["Dato: en un hall con ruido el sonido se pierde.", "Solución: subtítulos con texto de buen contraste.", "Así se entiende sin oír."], "Subtítulos con buen contraste"),
    ],
    [
        m("Dar el máximo sin mostrar evidencia.", "Sin evidencia el puntaje es una opinión.", "Cita la tabla de planos, la nota de permisos o la prueba."),
        m("Olvidar los subtítulos cuando el video se verá en un lugar ruidoso.", "No todas las personas podrán oír el sonido.", "Agrega texto con buen contraste."),
    ],
    [
        ex("¿Qué evidencia respalda el criterio de cuidado ético? A. La nota de permisos de las personas que aparecen B. La duración de los planos.", "A", "Los permisos muestran el consentimiento; la duración corresponde al ritmo."),
        ex("¿Qué criterio revisa que haya consentimiento y seguridad? A. Cuidado ético B. Ritmo.", "A", "Se refiere al respeto a personas y al riesgo."),
        ex("¿Para qué sirven los subtítulos? A. Para que más personas entiendan la pieza B. Para cambiar el ritmo.", "A", "Mejoran la accesibilidad."),
    ],
    [
        ex("Un video de ejemplo cumple su propósito, pero usa una canción de otra persona sin permiso. ¿Qué criterio baja? A. Sonido B. Lenguaje visual.", "A", "El sonido no es propio ni autorizado."),
        ex("Un texto gris claro sobre fondo blanco, ¿cómo es su contraste? A. Débil, se lee mal B. Fuerte, se lee bien.", "A", "Hay poca diferencia entre ambos colores."),
        ex("¿Qué evidencia respalda el criterio de ritmo? A. La tabla con la duración de los planos B. Una opinión sobre el título.", "A", "Es un dato comprobable."),
    ],
    [
        arith("Un video de ejemplo obtiene 2, 2, 1, 1 y 2 puntos en los cinco criterios. ¿Cuál es el total?", "2 + 2 + 1 + 1 + 2", "Se suman los cinco puntajes.", " puntos"),
        ex("Un video tiene 0 en lenguaje visual porque solo usa primeros planos de objetos, y su propósito es mostrar un patio completo. ¿Qué ajuste conviene? A. Agregar un plano general del patio B. Quitar el sonido.", "A", "El plano general muestra el lugar completo, que es lo que pide el propósito."),
        ex("El criterio de ritmo sacó 0 porque los planos duran 20 s en un video que quiere ser energético. ¿Qué ajuste conviene? A. Acortar los planos y agregar cortes B. Alargar aún más los planos.", "A", "El ritmo rápido responde a la energía."),
    ],
    [
        ex("Dos videos de ejemplo suman 8 puntos. P tiene 2 en cuidado ético y 0 en sonido; Q tiene 0 en cuidado ético y 2 en sonido. ¿Cuál es más urgente de corregir antes de mostrarse? A. Q, por no cuidar la ética B. P, por el sonido.", "A", "Sin consentimiento o seguridad no debe mostrarse, aunque el sonido sea bueno."),
        ex("Un compañero dice: «mi video saca 10 porque yo lo hice». ¿Qué le falta? A. Evidencia de cada criterio B. Más cortes.", "A", "Los puntajes se apoyan en evidencia, no en quién lo hizo."),
    ],
    [
        ex("Vas a mostrar tu video a tus vecinos y aparece una niña pequeña en dos planos. ¿Qué haces antes? A. Pedir permiso a una persona adulta responsable de ella B. Mostrarlo igual, porque es solo un instante.", "A", "El permiso es necesario aunque aparezca poco."),
        ex("Un grupo se puso 2 en cuidado ético sin haberle preguntado a una persona que aparece en un plano. ¿Qué corrige? A. Pide su permiso y deja el puntaje en 0 hasta tenerlo B. Mantiene el 2.", "A", "Sin consentimiento no se cumple el criterio."),
    ],
    ex("Tu video suma 6 de 10 y el criterio más bajo es ritmo. ¿Qué ajuste propones? A. Acortar los planos más largos B. Agregar una canción.", "A", "El ritmo depende de la duración y los cortes."),
    [
        ex("Nombra los cinco criterios de la pauta.", "Propósito, lenguaje visual, ritmo, sonido y cuidado ético", "Son los cinco criterios de la clase."),
        ex("Verdadero o falso: un puntaje alto sin evidencia es suficiente.", "Falso", "Cada puntaje necesita evidencia."),
        ex("¿Qué se evalúa con la pauta?", "La pieza, no a la persona", "La evaluación orienta la mejora."),
    ],
    task(
        "Evalúa UNA pieza con la pauta de cinco criterios (0 a 2). A) «Pasos de Lunes»: 36 s, 6 planos de 6 s, voz propia, nadie reconocible, se verá en un pasillo ruidoso sin subtítulos. B) «Hojas»: 30 s, un solo plano fijo, viento grabado por la autora, sin personas. C) Tu propio guion de la clase anterior. Escribe un puntaje y una evidencia por criterio, suma el total, propone un ajuste para el criterio más bajo y di si agregarías subtítulos.",
        "Evalué la A. Propósito 2: se entiende que muestra el inicio de la semana. Lenguaje visual 2: planos variados. Ritmo 2: seis planos de 6 s. Sonido 1: la voz es propia, pero en un pasillo ruidoso se perdería. Cuidado ético 2: nadie reconocible. Total 9 de 10. Ajuste para el criterio más bajo: agregar subtítulos con letras claras sobre fondo oscuro.",
        ["asigna puntaje y evidencia a cada criterio", "suma bien el total", "propone un ajuste o subtítulos con razón", "evalúa la pieza y no a la persona"],
        ["pauta con puntajes y evidencias", "ajuste o mejora de accesibilidad"],
        ["puntaje sin evidencia", "olvidar la accesibilidad"],
        "Pregunta qué evidencia respalda cada puntaje y si el ajuste cambia de verdad el criterio más bajo.",
    ),
    "Revisa un video corto de tu casa con sonido apagado y anota si se entiende; luego decide si necesitaría subtítulos.",
    "Escribe cuatro frases con puntaje y evidencia para una pieza de ejemplo.",
)

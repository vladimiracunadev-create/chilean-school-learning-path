"""Cuaderno del estudiante de 7.º básico Artes Visuales: AR07 OA 03 (crear a partir de la imaginación con medios digitales contemporáneos: fotografía y edición de imágenes)."""
from __future__ import annotations

from student_content_ar7_a import lesson, m, task, w
from student_lessons import arith, ex

OA3 = "AR07 OA 03"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Una hoja, lápiz y un marco de cartón con un hueco rectangular (visor). Si tienes teléfono o cámara, úsalo con permiso de una persona adulta; si no, basta el visor. Las escenas están descritas aquí.",
    "Aprenderé a leer una fotografía: qué muestra su encuadre, cómo se ordena una secuencia y a quién va dirigida (audiencia). Sirve para tomar decisiones antes de fotografiar.",
    ["Sé que una imagen comunica con decisiones visuales.", "Sé escribir una intención con qué, cómo y por qué."],
    [
        "El encuadre es lo que decido dejar dentro del borde de la imagen y lo que dejo fuera. Cambiar el encuadre cambia el mensaje. Un plano general muestra el lugar completo y a las personas pequeñas. Un plano medio muestra a una persona de la cintura hacia arriba. Un primer plano muestra una parte, como un rostro o un objeto, muy cerca, y deja ver detalle y emoción. Un plano detalle muestra una parte pequeña, como una mano o un zapato.",
        "El ángulo es desde dónde se mira. Un ángulo picado es desde arriba hacia abajo y hace ver pequeño al sujeto. Un ángulo contrapicado es desde abajo hacia arriba y lo hace ver grande y fuerte. Un ángulo a nivel está a la altura de los ojos y se siente natural. Una secuencia es un grupo de imágenes ordenadas que se leen una tras otra, como un cuento sin palabras. El orden cambia el sentido: la misma imagen de una puerta cerrada no significa lo mismo antes o después de una imagen de alguien esperando.",
        "La audiencia es la persona o el grupo que mirará las imágenes. Pensar en ella ayuda a decidir qué mostrar y cómo. Una imagen para niños pequeños necesita formas claras y pocos detalles; una para el curso puede ser más compleja. Al analizar una fotografía me pregunto: ¿qué plano y ángulo usa?, ¿qué deja fuera?, ¿qué orden tiene la secuencia?, ¿para quién parece hecha? Anoto lo que veo antes de interpretar.",
    ],
    [("encuadre", "lo que queda dentro del borde de la imagen"), ("plano", "qué tan cerca o lejos se muestra el sujeto"), ("ángulo", "desde dónde se mira el sujeto"), ("secuencia", "imágenes ordenadas que se leen una tras otra"), ("audiencia", "personas que mirarán la obra")],
    [
        w("Leer el plano y el ángulo", "Una foto de ejemplo muestra a un niño de la cintura hacia arriba, de pie sobre una roca, tomada desde abajo; se ve grande contra el cielo. ¿Qué plano y ángulo son, y qué efecto producen?", ["La cámara está abajo y mira hacia arriba: ángulo contrapicado.", "Se ve de la cintura hacia arriba: plano medio.", "Efecto: se ve fuerte y grande."], "Plano medio con ángulo contrapicado: el niño se ve grande y fuerte"),
        w("Cambiar el orden", "Tienes dos imágenes: (1) un paraguas abierto y (2) una calle mojada. Si las ordenas 1-2 se lee «llegó la lluvia y mojó la calle». ¿Cómo se lee si las ordenas 2-1?", ["Primero se ve la calle mojada.", "Después el paraguas abierto.", "Sugiere que la lluvia ya pasó y alguien se protege."], "Se lee como «la calle ya estaba mojada y alguien se protege»"),
    ],
    [
        m("Pensar que la foto muestra todo lo que había frente a la cámara.", "El encuadre deja fuera lo que no está dentro del borde.", "Pregunta qué hay fuera del encuadre y por qué se dejó fuera."),
        m("Cambiar el orden de las imágenes sin pensar que cambia el sentido.", "La misma imagen significa distinto según lo que viene antes y después.", "Prueba dos órdenes y lee cómo cambia."),
    ],
    [
        ex("Una foto muestra una hoja de árbol muy de cerca, con sus nervaduras. ¿Es plano general o plano detalle?", "Plano detalle", "Muestra una parte pequeña muy de cerca."),
        ex("Un ángulo desde arriba hacia abajo se llama: A. picado B. contrapicado.", "A", "Picado es mirar desde arriba."),
        ex("La audiencia de una obra son: A. las personas que la mirarán B. los materiales que se usaron.", "A", "La audiencia es quien mira la obra."),
    ],
    [
        ex("Una foto de un patio muestra todo el patio, con las personas muy pequeñas. ¿Qué plano es?", "Plano general", "Muestra el lugar completo y a las personas pequeñas."),
        ex("Quieres que un gato se vea grande y poderoso. ¿Desde dónde fotografías: desde arriba o desde abajo?", "Desde abajo", "El ángulo contrapicado hace ver grande al sujeto."),
        ex("Dos fotos: en la primera se ve un niño con un helado; en la segunda, un helado derretido en el suelo. Si las ordenas 1-2, ¿qué cuenta la secuencia? A. Que el helado pasó de la mano del niño al suelo B. Que el helado pasó del suelo a la mano del niño.", "A", "El orden 1-2 muestra el helado primero en la mano y luego en el suelo."),
    ],
    [
        ex("Quieres mostrar la soledad de una persona en una plaza enorme. ¿Qué plano usas: general o primer plano?", "General", "El plano general deja a la persona pequeña dentro de un espacio grande."),
        ex("Quieres mostrar la emoción en el rostro de alguien. ¿Qué plano usas: primer plano o plano general?", "Primer plano", "Se acerca al rostro y se ve la emoción."),
        arith("Una secuencia tiene 3 imágenes de plano general, 2 de plano medio y 1 de primer plano. ¿Cuántas imágenes tiene la secuencia?", "3+2+1", "Se suman todas las imágenes."),
    ],
    [
        ex("Un compañero dice que su foto «muestra todo el parque». Su foto solo incluye una banca vacía y un árbol, tomada muy de cerca. ¿Es correcto? A. No, el encuadre deja fuera casi todo el parque B. Sí, siempre se ve todo.", "A", "El encuadre muestra solo lo que queda dentro del borde."),
        ex("Una foto para niños de 5 años y otra para adultos. La primera tiene 3 objetos grandes y colores simples. La segunda tiene 20 objetos pequeños. ¿Cuál se ajusta mejor a niños pequeños?", "La primera", "Pocos objetos grandes son más fáciles de leer para esa audiencia."),
    ],
    [
        ex("Mira el orden: 1) una niña con una linterna en un pasillo oscuro, 2) una puerta entreabierta con luz, 3) la niña sonriendo. ¿Qué sentimiento recorre la secuencia: de miedo a alivio o de alegría a pena?", "De miedo a alivio", "La oscuridad inicial se resuelve con la luz y la sonrisa."),
        ex("Quieres que una torre de bloques se vea pequeña frente a un gigante de juguete. ¿Desde qué ángulo fotografías la torre: picado o contrapicado?", "Picado", "Mirarla desde arriba la hace ver pequeña."),
    ],
    ex("Decide el plano para una imagen sobre «el cansancio de las manos de una panadera»: A. plano detalle de las manos enharinadas B. plano general de una panadería llena de gente. Elige el que dirige la mirada a lo que quieres mostrar.", "A", "El plano detalle centra la atención en las manos."),
    [
        ex("En Artes Visuales, ¿qué es el encuadre?", "Lo que queda dentro del borde de la imagen", "Define qué se ve y qué no."),
        ex("Verdadero o falso: una foto muestra todo lo que había frente a la cámara.", "Falso", "El encuadre deja fuera parte del lugar."),
        ex("¿Qué ángulo hace ver grande al sujeto?", "Contrapicado", "Se mira desde abajo hacia arriba."),
    ],
    task(
        "Elige UNA escena escrita. A) Un niño sobre una roca, un cielo grande y un perro a sus pies. B) Un patio con ropa colgada y un gato dormido en el suelo. C) Una mano que sostiene una taza humeante junto a una ventana con lluvia. Con tu visor de cartón o una cámara, haz tres encuadres distintos de un lugar parecido de tu casa (general, medio y detalle) y anota qué mensaje cambia en cada uno. Escribe para qué audiencia es.",
        "Elegí la C. Hice un encuadre general de la ventana con la lluvia, uno medio de la taza en la mesa y un detalle del vapor. En el general se siente el día frío; en el detalle, el calor. Audiencia: compañeros del curso, porque quiero mostrar el contraste de afuera y adentro.",
        ["hace tres encuadres con planos distintos", "anota qué cambia en cada uno", "escribe la audiencia", "no incluye a personas sin permiso"],
        ["tres encuadres o dibujos de encuadre", "nota del mensaje de cada uno"],
        ["usar el mismo plano tres veces", "no pensar en la audiencia"],
        "Destaca la diferencia de mensaje entre dos planos y pregunta qué dejó fuera del encuadre.",
    ),
    "Mira un objeto por el hueco de tu visor, acércalo y aléjalo, y di qué cambia en lo que ves.",
    "Describe en cuatro líneas la misma escena con tres planos distintos y explica cuál cuenta más de la persona.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Un objeto cotidiano limpio (por ejemplo una taza o una planta), una linterna o una ventana con luz, una hoja blanca y el visor de cartón. Si tienes teléfono o cámara, úsalo con permiso de una persona adulta. No hace falta fotografiar a personas.",
    "Aprenderé a explorar la luz, el punto de vista y la composición para crear una imagen imaginada con un objeto. Sirve para tomar decisiones antes de editar.",
    ["Sé elegir plano y ángulo.", "Sé que una prueba pequeña permite comparar."],
    [
        "La fotografía es escribir con luz: sin luz no hay imagen. La luz que viene de adelante ilumina todo y aplana las formas. La luz lateral, que llega de un costado, crea sombras y muestra volumen y textura. El contraluz, con la luz detrás del objeto, lo convierte en una silueta oscura con un borde brillante. Cambiar de ventana o mover una linterna cambia la imagen sin cambiar el objeto.",
        "La composición es cómo se ordenan los elementos dentro del encuadre. Una manera fácil es dividir mentalmente la imagen en tres partes a lo ancho y a lo alto y poner el objeto principal en una de las líneas en vez de en el centro exacto: se llama regla de los tercios. También puedo usar el espacio vacío para dar calma o llenar la imagen para dar tensión. El punto de vista cambia lo que se ve, como mirar un objeto de frente, desde arriba o muy de cerca.",
        "Una fotografía de imaginación no copia la realidad: construye una escena inventada. Por ejemplo, puedo poner una planta pequeña junto a un auto de juguete grande para crear un «mundo gigante». Pruebo tres opciones y escojo la que mejor muestra mi idea. Una buena exploración incluye al menos tres tomas (una toma es cada foto o dibujo de prueba) con luz, punto de vista o composición distintos. Si no tengo cámara, dibujo el encuadre en una hoja con las sombras y las luces.",
    ],
    [("luz lateral", "luz que llega de un costado y marca volumen y textura"), ("contraluz", "luz detrás del objeto que lo vuelve silueta"), ("composición", "orden de los elementos dentro del encuadre"), ("regla de los tercios", "poner lo principal en una línea que divide la imagen en tres partes"), ("silueta", "forma oscura que se ve contra la luz")],
    [
        w("Elegir la luz", "Fotografías una taza con una cuchara. Quieres mostrar la textura de la cerámica rugosa. ¿Qué luz usas: frontal o lateral?", ["La frontal aplana la superficie.", "La lateral crea pequeñas sombras en cada relieve.", "Las sombras muestran textura."], "La luz lateral"),
        w("Componer con tercios", "Quieres fotografiar una planta pequeña con un fondo vacío para dar calma. ¿Dónde pones la planta?", ["En el centro exacto da una imagen estática.", "En una línea de tercios y con espacio vacío al lado da calma.", "Dejo el espacio vacío al lado hacia donde mira o se inclina la planta."], "En un tercio, con espacio vacío al lado"),
    ],
    [
        m("Poner siempre el objeto en el centro exacto sin probar otros lugares.", "A veces se ve estático o poco interesante.", "Prueba tercios y espacio vacío y compara."),
        m("Hacer una sola toma y quedarse con ella.", "No se sabe si había una opción mejor.", "Haz al menos tres tomas con una variable distinta."),
    ],
    [
        ex("Luz que viene de un costado y crea sombras que muestran el volumen: ¿frontal, lateral o contraluz?", "Lateral", "Una luz que llega de un costado marca el relieve."),
        ex("Un objeto oscuro con borde brillante porque la luz está detrás se llama: A. silueta B. primer plano.", "A", "El contraluz vuelve al objeto una forma oscura."),
        ex("¿Cuántas tomas distintas incluye al menos una buena exploración?", "Tres", "Permite comparar luz, punto de vista o composición."),
    ],
    [
        ex("Quieres mostrar la forma de una planta como silueta oscura contra la luz de una ventana. ¿Dónde debe estar la ventana respecto de la planta: detrás de la planta o detrás de ti?", "Detrás de la planta", "La luz queda detrás de la planta y la vuelve silueta."),
        ex("Una foto con luz frontal aplana el objeto. ¿Qué cambias para mostrar mejor su textura? A. Mover la luz hacia un costado B. Hacerla más brillante de frente.", "A", "La luz lateral produce sombras que muestran relieve."),
        ex("Tu objeto está en el centro exacto y la imagen se ve estática. ¿Qué pruebas? A. Moverlo a una línea de tercios y dejar espacio vacío B. Taparlo completamente.", "A", "Un cambio de composición da más vida a la imagen."),
    ],
    [
        ex("Para crear un «mundo gigante» fotografías una hoja de lechuga junto a un auto de juguete. Quieres que la hoja parezca un árbol. ¿Cómo la fotografías: muy de cerca y desde abajo o de lejos y desde arriba?", "Muy de cerca y desde abajo", "El ángulo contrapicado y la cercanía la hacen ver enorme."),
        ex("Quieres que una imagen se sienta tensa y llena. ¿Qué composición usas: objetos muy juntos cubriendo casi todo el encuadre o un solo objeto pequeño en un espacio vacío?", "Objetos muy juntos cubriendo casi todo el encuadre", "Llenar el encuadre da sensación de tensión."),
        arith("Haces 3 tomas con luz lateral y 2 tomas con contraluz. ¿Cuántas tomas hiciste?", "3+2", "Se suman las tomas de ambas luces."),
    ],
    [
        ex("Dos compañeros fotografían la misma taza. Uno la pone de frente a la luz de la ventana y otro con la ventana detrás. ¿Quién obtiene una silueta?", "El que la pone con la ventana detrás", "Con la luz detrás, la taza se ve como silueta."),
        ex("Un estudiante quiere mostrar «soledad» y pone la planta en el centro rodeada de muchas macetas. ¿Qué cambias? A. Dejarla sola, en un tercio, con espacio vacío B. Agregar más macetas.", "A", "El espacio vacío y la planta sola transmiten soledad."),
    ],
    [
        ex("Para un mundo imaginado fotografías una pila de monedas y quieres que parezca una torre enorme. ¿Qué punto de vista usas: a la altura de la mesa, mirando hacia arriba, o desde arriba, mirando hacia abajo?", "A la altura de la mesa, mirando hacia arriba", "Desde abajo la pila se ve alta y grande; desde arriba se vería como un círculo."),
        ex("Quieres que una cuchara parezca un puente sobre un río imaginario. ¿Qué haces: fotografiarla muy de cerca con el borde cruzando el encuadre o muy de lejos?", "Muy de cerca con el borde cruzando el encuadre", "La cercanía la hace ver enorme."),
    ],
    ex("Para una fotografía de imaginación tienes una taza, una cuchara y una hoja de papel azul. Quieres hacer una escena de «barco en el mar». ¿Qué decisión de composición sirve más? A. Poner la cuchara de lado como barco sobre el papel azul con espacio vacío arriba B. Tapar toda la imagen con la taza.", "A", "El papel azul funciona de mar y el espacio vacío da sensación de horizonte."),
    [
        ex("¿Qué luz crea una silueta?", "El contraluz", "La luz detrás oscurece el frente del objeto."),
        ex("Verdadero o falso: el objeto principal siempre debe estar en el centro.", "Falso", "Se pueden usar tercios u otras composiciones."),
        ex("¿Qué se hace si no tienes cámara?", "Dibujar el encuadre con luces y sombras", "Sirve para practicar las mismas decisiones."),
    ],
    task(
        "Elige UN objeto. A) Una taza limpia. B) Una planta pequeña. C) Una cuchara y un papel azul. Haz tres tomas o tres dibujos de encuadre variando una cosa: luz (frontal, lateral, contraluz), punto de vista o composición. Anota qué cambió y qué efecto produjo. Si usas cámara, no fotografíes a personas ni lugares privados ajenos.",
        "Elegí la B. Toma 1: planta con luz frontal, se ve plana. Toma 2: luz lateral, se ven las nervaduras. Toma 3: contraluz, silueta oscura con borde brillante. Cambié solo la luz. Elijo la 3 porque muestra la forma como una sombra misteriosa.",
        ["hace tres tomas o dibujos variando una cosa", "anota qué cambió y su efecto", "elige una y explica", "no incluye personas"],
        ["tres tomas o dibujos", "nota del efecto de cada cambio"],
        ["variar muchas cosas a la vez", "elegir sin explicar"],
        "Destaca la variable cambiada y pregunta cómo se sentiría con otra luz.",
    ),
    "Mueve una linterna alrededor de un objeto en una pieza oscura y di cómo cambia su sombra.",
    "Describe cómo harías una escena imaginada de «ciudad en miniatura» con objetos de tu casa, indicando luz y encuadre.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Seis rectángulos de papel del mismo tamaño (viñetas), lápiz y lápices de colores. Puedes usar fotos tomadas con permiso o dibujar cada encuadre. Las historias de partida están escritas aquí.",
    "Aprenderé a contar una historia con imágenes ordenadas (narración visual) usando inicio, cambio y cierre. Sirve para planificar una secuencia de fotografías o imágenes digitales.",
    ["Sé elegir plano, ángulo y luz.", "Sé que el orden de las imágenes cambia el sentido."],
    [
        "Una narración visual cuenta una historia con imágenes, con poca o ninguna palabra. Se planifica en un guion gráfico (storyboard), que es una serie de recuadros con el dibujo rápido de cada imagen y una nota. Una historia sencilla tiene tres partes: un inicio, que presenta el lugar y al personaje; un cambio, donde pasa algo que mueve la historia; y un cierre, que muestra cómo termina o qué quedó distinto.",
        "Cada imagen debe aportar algo nuevo. Si dos imágenes son iguales, la historia no avanza. Puedo variar el plano: un plano general al inicio para ubicar el lugar, un primer plano en el cambio para mostrar la emoción y un plano detalle al final para dejar una huella. El ritmo es la velocidad con que cambian las imágenes: muchas imágenes cortas se sienten rápidas y pocas imágenes con mucho detalle se sienten lentas.",
        "Los personajes pueden ser objetos: una hoja que viaja, un zapato que espera. Así no necesito fotografiar a nadie. Para comprobar mi secuencia se la muestro a otra persona sin explicar y le pregunto qué entendió. Si cuenta otra historia, reviso el orden o falta una imagen. La narración se puede hacer en fotos, dibujos o en una aplicación de edición, pero el plan en papel siempre ayuda.",
    ],
    [("narración visual", "historia contada con imágenes ordenadas"), ("guion gráfico", "serie de recuadros que planifica una secuencia (storyboard)"), ("inicio", "parte que presenta el lugar y al personaje"), ("cierre", "parte que muestra cómo termina la historia"), ("ritmo", "velocidad con que cambian las imágenes")],
    [
        w("Planificar tres partes", "Cuentas la historia de un zapato que espera en una puerta. Ordena las tres partes con imágenes.", ["Inicio: plano general de una puerta con un zapato solo.", "Cambio: primer plano de unas pisadas que se acercan.", "Cierre: plano detalle del zapato con su par."], "Inicio: puerta con zapato solo; cambio: pisadas que llegan; cierre: el par completo"),
        w("Corregir una secuencia repetida", "Tu secuencia tiene cuatro imágenes casi iguales de una hoja en el suelo. ¿Qué cambias?", ["Si todas son iguales, la historia no avanza.", "Cambio el plano y el momento de cada imagen.", "Agrego un cambio: el viento la mueve."], "Variar el plano y mostrar un cambio (el viento mueve la hoja)"),
    ],
    [
        m("Hacer varias imágenes casi iguales y esperar que cuenten algo.", "Sin cambios, la historia no avanza.", "Cada imagen debe mostrar algo nuevo."),
        m("Planificar solo la primera imagen y decidir el resto sobre la marcha.", "La historia pierde el cierre y el orden.", "Dibuja un storyboard con inicio, cambio y cierre antes de hacerla."),
    ],
    [
        ex("¿Qué tres partes tiene una historia sencilla?", "Inicio, cambio y cierre", "Presentan, mueven y terminan la historia."),
        ex("Un guion gráfico es: A. una serie de recuadros con dibujos rápidos que planifican la secuencia B. un texto largo sin imágenes.", "A", "El storyboard se hace con dibujos y notas."),
        ex("Tres imágenes casi idénticas seguidas, ¿hacen avanzar la historia?", "No", "Si no muestran algo nuevo, la historia no avanza."),
    ],
    [
        ex("Una historia de un globo: 1) globo atado a una silla, 2) el hilo suelto, 3) globo en el cielo. ¿En cuál imagen ocurre el cambio?", "En la 2", "El hilo suelto es lo que mueve la historia."),
        ex("Quieres que la secuencia se sienta rápida. ¿Cuál usas: muchas imágenes cortas o pocas imágenes con mucho detalle?", "Muchas imágenes cortas", "Cambiar seguido da ritmo rápido."),
        ex("Para el inicio de tu historia, ¿qué plano ayuda a ubicar el lugar: plano general o plano detalle?", "Plano general", "Muestra el lugar completo."),
    ],
    [
        arith("Tu storyboard tiene 2 imágenes de inicio, 3 de cambio y 1 de cierre. ¿Cuántos recuadros tiene?", "2+3+1", "Se suman todas las partes."),
        ex("Tienes seis recuadros y quieres contar «una semilla que crece». ¿Qué orden es correcto? A. semilla en tierra, brote pequeño, planta con hojas B. planta con hojas, semilla en tierra, brote pequeño.", "A", "La A respeta el orden de crecimiento."),
        ex("En tu historia de un perro que espera, quieres un cierre emotivo. ¿Qué plano usas al final: primer plano de la cara del perro al ver llegar a alguien o plano general de una calle vacía?", "Primer plano de la cara del perro al ver llegar a alguien", "El primer plano muestra la emoción del reencuentro."),
    ],
    [
        ex("Muestras tu secuencia de un barco de papel a una persona y cuenta otra historia. ¿Qué haces? A. Revisar el orden y ver si falta una imagen B. Decirle que está equivocada.", "A", "Si el mensaje no se entiende, hay que revisar la secuencia."),
        ex("Un compañero afirma que si sus seis imágenes son tomas del mismo objeto sin cambios, ya contó una historia. ¿Qué falta?", "Un cambio entre las imágenes", "Sin cambio no hay historia."),
    ],
    [
        ex("Cuentas la historia «un paraguas que se rompe con el viento». Si el cambio ocurre en la imagen 3 de 5, ¿cuántas imágenes quedan después del cambio?", "2", "De 5 imágenes, el cambio es la 3.ª; quedan 5 − 3 = 2."),
        ex("Dos storyboards cuentan «un amanecer». El primero tiene 6 viñetas con el cielo cada vez más claro. El segundo tiene 6 viñetas con el mismo cielo gris. ¿Cuál cuenta mejor el amanecer?", "El primero", "Muestra un cambio de luz entre viñetas."),
    ],
    ex("Tienes que contar con un objeto «una taza que espera». Elige la mejor secuencia de tres imágenes. A. taza vacía sola, mano que sirve, taza llena humeante B. taza llena, taza vacía, mano que sirve.", "A", "La A tiene inicio, cambio y cierre; la B desordena la historia."),
    [
        ex("En Artes Visuales, ¿qué es el ritmo en una secuencia?", "La velocidad con que cambian las imágenes", "Muchas imágenes cortas son rápidas; pocas con detalle son lentas."),
        ex("Verdadero o falso: los personajes de la historia pueden ser objetos.", "Verdadero", "Una hoja o un zapato pueden ser el personaje."),
        ex("¿Qué haces con tu secuencia antes de hacerla?", "La planificas en un storyboard", "Así se ordenan inicio, cambio y cierre."),
    ],
    task(
        "Elige UNA historia. A) Un zapato que espera en una puerta. B) Una hoja que viaja por una vereda. C) Una taza que espera a ser llenada. Haz un storyboard de seis recuadros con inicio, cambio y cierre; en cada uno anota el plano (general, medio, primer plano o detalle). Muéstralo a otra persona sin explicar y anota qué entendió.",
        "Elegí la B. 1: plano general de una vereda con una hoja (inicio). 2: primer plano de la hoja. 3: viento, la hoja se mueve (cambio). 4: plano medio de la hoja en el aire. 5: la hoja cae en un charco. 6: plano detalle de las ondas del charco (cierre). Mi hermana entendió que la hoja viajó hasta el charco.",
        ["storyboard de seis recuadros", "inicio, cambio y cierre claros", "planos variados", "anota lo que entendió otra persona"],
        ["storyboard de seis recuadros", "nota de la prueba con otra persona"],
        ["imágenes repetidas", "no probar con otra persona"],
        "Destaca la imagen del cambio y pregunta qué efecto tendría cambiar el orden de dos viñetas.",
    ),
    "Cuenta con tres objetos de tu casa una historia corta, moviéndolos como si fueran imágenes.",
    "Reordena tu storyboard de dos maneras distintas y explica cómo cambia la historia.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Tus imágenes de la clase anterior (fotos con permiso o dibujos), papel y lápiz. Si usas una aplicación gratuita de edición, hazlo con ayuda de una persona adulta. También se puede simular la edición con dibujos y notas.",
    "Aprenderé a editar imágenes con ajustes simples (recorte, brillo, contraste, saturación, blanco y negro) respetando la autoría y la privacidad. Sirve para mejorar mi obra sin engañar ni dañar a nadie.",
    ["Sé armar una secuencia con inicio, cambio y cierre.", "Sé que la autoría es mía cuando tomo mis propias decisiones."],
    [
        "Editar es cambiar una imagen después de tomarla. Los ajustes básicos son: recortar, que cambia el encuadre; el brillo, que aclara u oscurece toda la imagen; el contraste, que aumenta o baja la diferencia entre claros y oscuros; la saturación, que hace los colores más intensos o más apagados; y el blanco y negro, que quita el color. Cada ajuste cambia la emoción: más contraste da dramatismo y menos saturación da una sensación apagada o antigua.",
        "Editar no significa engañar. Si cambio una imagen para mostrar una idea imaginada está bien, y lo digo en la ficha. Pero no debo alterar la foto de una persona para burlarme de ella ni mezclar imágenes para hacer creer algo falso. Respeto la autoría: uso solo imágenes que yo hice o que tengo permiso para usar, y siempre cito de dónde vienen. Una imagen de otra persona no es mía solo porque la encontré.",
        "La privacidad también importa. No uso rostros de otras personas, nombres, direcciones ni lugares que permitan ubicar a alguien, y quito datos que la imagen pueda traer, como la ubicación. Pido permiso por escrito o en persona antes de usar la imagen de alguien que aparece y, si es menor de edad, también a su familia. Si tengo dudas, uso objetos, paisajes sin datos personales o dibujos. Edito siempre una copia y guardo el original sin cambios.",
    ],
    [("edición", "cambios que se hacen a una imagen después de tomarla"), ("contraste", "diferencia entre las zonas claras y oscuras"), ("saturación", "intensidad de los colores"), ("privacidad", "derecho a que no se muestren datos o imágenes propias sin permiso"), ("copia", "versión que se edita para conservar el original intacto")],
    [
        w("Elegir el ajuste", "Una foto de ejemplo de un patio se ve apagada y gris. Quieres que los colores se vean vivos. ¿Qué ajustas?", ["Los colores apagados indican poca saturación.", "Subo la saturación.", "Dejo el contraste igual para no cambiar el resto."], "Subir la saturación"),
        w("Decidir si se puede usar", "Un compañero te envía una foto en que sale la cara de su hermana pequeña, que no sabe que la usarás. ¿La usas?", ["La imagen muestra un rostro.", "Hay que tener permiso de la persona y, si es menor, de su familia.", "Es mejor usar un dibujo o un objeto."], "No, hasta tener el permiso; usa un objeto o un dibujo"),
    ],
    [
        m("Editar la imagen original y guardar encima.", "Si el cambio no gusta, no se puede volver atrás.", "Guarda el original y edita una copia."),
        m("Usar una foto que encontraste en internet como si fuera tuya.", "No es tu autoría y puede no tener permiso de uso.", "Usa imágenes tuyas o con permiso, y cita la fuente."),
    ],
    [
        ex("Un ajuste que quita el color de una imagen se llama: A. blanco y negro B. saturación alta.", "A", "El blanco y negro elimina el color."),
        ex("Ajuste que aumenta la diferencia entre claros y oscuros: ¿brillo o contraste?", "Contraste", "Brillo aclara todo; contraste marca la diferencia."),
        ex("¿Qué se edita siempre: el original o una copia?", "Una copia", "Así se conserva el original sin cambios."),
    ],
    [
        ex("Una foto de tu planta se ve demasiado oscura. ¿Qué ajuste necesitas: subir el brillo o bajar la saturación?", "Subir el brillo", "El brillo aclara toda la imagen."),
        ex("Quieres que una foto de un día de lluvia se vea dramática. ¿Qué ajustas? A. Subir el contraste y bajar la saturación B. Subir mucho el brillo y la saturación.", "A", "El contraste alto y los colores apagados dan dramatismo."),
        ex("Una foto muestra una dirección escrita en un letrero visible. ¿Qué haces antes de mostrarla en el curso? A. Recortar para dejarla fuera del encuadre B. Mostrarla igual.", "A", "La dirección es un dato que permite ubicar un lugar."),
    ],
    [
        ex("Quieres recortar una foto de un árbol para que quede solo la copa. ¿Qué ajuste usas: recorte o contraste?", "Recorte", "El recorte cambia el encuadre."),
        ex("Descargas la foto de un paisaje que sacó otra persona y la usas sin decir nada. ¿Qué principio no respetaste? A. La autoría, porque no es tu imagen ni citaste su origen B. La privacidad, porque el paisaje puede mostrar un lugar.", "A", "La imagen no es tuya y no citaste su origen."),
        arith("Tienes 8 fotos y editas 3 con blanco y negro y 2 con más saturación. ¿Cuántas fotos quedan sin editar?", "8-3-2", "Se restan las editadas del total."),
    ],
    [
        ex("Un compañero edita una foto de un curso para que parezca que un estudiante hizo algo que no hizo. ¿Qué principio rompe? A. No engañar ni dañar B. Recortar la foto.", "A", "Alterar una imagen para engañar daña a la persona."),
        ex("Una estudiante dice: «Mi foto está editada y se ve distinta a la realidad, pero lo anoto en la ficha como imagen imaginada». ¿Es correcto?", "Sí", "Editar para una idea imaginada es válido si se dice."),
    ],
    [
        ex("Una foto de tu prima muestra su cara y su uniforme con el nombre del colegio. Quieres usarla en tu obra. ¿Cuál es la decisión más cuidadosa? A. Pedir permiso y quitar el nombre del colegio B. Subirla tal cual.", "A", "Se pide permiso y se eliminan datos que permiten ubicarla."),
        ex("Quieres mostrar un paisaje que sacaste en un viaje. La foto trae datos de ubicación exacta. ¿Qué haces antes de compartirla en el curso?", "Quitar los datos de ubicación", "La ubicación exacta puede revelar dónde vives o estuviste."),
    ],
    ex("Tu foto de una taza se ve apagada. Opción A: subir saturación y contraste en una copia. Opción B: borrar la original y editar sobre ella. ¿Cuál es la mejor práctica?", "A", "Se conserva el original y la edición mejora la copia."),
    [
        ex("¿Qué hace la saturación?", "Cambia la intensidad de los colores", "Puede hacerlos más vivos o más apagados."),
        ex("Verdadero o falso: puedo usar la foto de otra persona si la encontré.", "Falso", "Necesito permiso y debo citar de dónde viene."),
        ex("¿Qué datos se quitan antes de mostrar una imagen?", "Los que permiten ubicar a una persona", "Protegen la privacidad."),
    ],
    task(
        "Elige UNA situación. A) Una foto de un patio que se ve gris y apagada. B) Una foto de un letrero de calle con un nombre de pasaje visible. C) Una foto de un gato dormido, muy oscura. Para cada una escribe qué ajuste harías (recorte, brillo, contraste, saturación o blanco y negro), por qué y qué dato o riesgo revisarías antes de mostrarla. Si tienes una foto tuya sin personas, edita una copia y compara.",
        "Elegí la C. Ajuste: subir el brillo para ver al gato y bajar un poco el contraste para que no se pierda el pelaje. Riesgo: el fondo muestra un número de casa en la pared. Lo recorto antes de mostrarla. Guardé el original y edité la copia.",
        ["elige ajustes con una razón", "revisa un dato de privacidad", "trabaja sobre una copia", "no usa imágenes ajenas sin permiso"],
        ["descripción de los ajustes", "nota de privacidad"],
        ["editar el original", "mostrar datos que ubican a alguien"],
        "Destaca el ajuste mejor justificado y pregunta qué riesgo de privacidad revisó.",
    ),
    "Mira una foto de tu casa (sin personas) y di qué dato tendrías que quitar antes de mostrarla a otras personas.",
    "Escribe dos reglas que seguirías para respetar la autoría y dos para la privacidad cuando editas imágenes.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Tu secuencia terminada (fotos con permiso o dibujos), papel, lápiz y una hoja para la ficha. Se puede presentar impresa, en pantalla con una persona adulta o en una pared de la sala.",
    "Aprenderé a presentar mi obra digital en un circuito protegido, es decir, con una audiencia cerrada y sin exponer datos. Sirve para compartir mi trabajo de forma segura y respetuosa.",
    ["Sé editar con respeto a la autoría y la privacidad.", "Sé que la audiencia influye en lo que muestro."],
    [
        "Un circuito protegido es un espacio cerrado donde solo ve mi obra un grupo conocido y autorizado: mi curso, mi familia o una exposición en la sala. No es una red abierta donde cualquier persona puede verla, copiarla o guardarla. Antes de presentar decido en qué circuito lo haré y a quién va dirigida mi obra.",
        "Para presentar con cuidado reviso una lista: ¿tengo permiso de todas las personas que aparecen?, ¿quité nombres, direcciones, uniformes y ubicaciones?, ¿mis imágenes son mías o citadas?, ¿pensé en cómo se sentirá quien las vea? También agrego una ficha con título, intención y técnica, y declaro si la imagen es editada o imaginada. Si alguien dice que algo lo incomoda, retiro esa parte sin discutir.",
        "La presentación también se diseña: el orden de las imágenes, el tamaño, el lugar y el tiempo para mirar. Puedo imprimir mi secuencia en hojas y colgarla en fila, o mostrarla en una pantalla sin conexión. Después pido comentarios con un criterio, por ejemplo «¿se entendió la historia?» y anoto qué cambiaría. Si en algún momento algo de lo que veo en línea me incomoda o me preocupa, aviso a una persona adulta de confianza.",
    ],
    [("circuito protegido", "espacio cerrado donde solo ve la obra un grupo autorizado"), ("permiso", "autorización de una persona para usar su imagen"), ("ficha", "texto corto que acompaña la obra con título, intención y técnica"), ("dato personal", "dato que permite identificar o ubicar a alguien"), ("editada", "imagen cambiada después de tomarla, que debe declararse")],
    [
        w("Elegir el circuito", "Tienes una secuencia de tu gato. ¿Dónde la presentas: en la sala con tu curso o en una red abierta donde cualquiera puede verla?", ["La sala es un grupo conocido.", "La red abierta permite que cualquiera copie y guarde.", "El circuito protegido es el curso."], "En la sala con tu curso"),
        w("Revisar antes de presentar", "Tu foto muestra una bicicleta apoyada en una reja con el número de la casa visible. ¿Qué haces?", ["El número de casa es un dato que ubica un lugar.", "Recorto o tapo el número.", "Presento solo cuando no queden datos."], "Recortar o tapar el número de la casa antes de presentar"),
    ],
    [
        m("Pensar que si se la envío a un amigo ya es privada.", "Los archivos pueden copiarse y reenviarse fuera del grupo.", "Elige un circuito cerrado y controlado y pide permiso."),
        m("Mostrar imágenes con nombres, uniformes o lugares reconocibles.", "Pone en riesgo la privacidad de las personas.", "Revisa y quita datos que permitan ubicar a alguien."),
    ],
    [
        ex("En Artes Visuales, ¿qué es un circuito protegido?", "Un espacio cerrado donde solo ve la obra un grupo autorizado", "Limita quién puede ver, copiar o guardar la obra."),
        ex("Tu curso en la sala, ¿es un circuito protegido?: A. Sí, es un grupo conocido y autorizado B. No, cualquiera puede entrar.", "A", "El curso es un grupo cerrado y conocido."),
        ex("Si alguien dice que una imagen lo incomoda, ¿la retiras o discutes?", "La retiras", "Se respeta a la persona y se corrige sin discutir."),
    ],
    [
        ex("Tu foto muestra un uniforme con el nombre del colegio. Antes de presentar, ¿qué haces? A. Recortar o tapar el nombre B. Dejarlo para que se sepa de dónde es.", "A", "El nombre del colegio ayuda a ubicar a alguien."),
        ex("Una imagen que editaste para crear un mundo imaginario, ¿se declara como editada en la ficha?", "Sí", "Se declara para no engañar."),
        ex("¿Qué datos incluye una ficha? A. Título, intención y técnica B. Dirección de tu casa y teléfono.", "A", "La dirección y el teléfono son datos personales."),
    ],
    [
        arith("Imprimes 6 imágenes en hojas y las cuelgas en 2 filas iguales. ¿Cuántas imágenes hay por fila?", "6/2", "Se reparten por igual en dos filas."),
        ex("Quieres presentar con la secuencia en orden: inicio, cambio y cierre. En una pared cuelgas de izquierda a derecha: cierre, inicio, cambio. ¿Está bien el orden?", "No", "El orden de lectura de izquierda a derecha debe ser inicio, cambio y cierre."),
        ex("Una estudiante quiere que su obra la vea todo el curso. ¿Qué lista revisa antes? A. Permisos, datos personales, autoría y ficha B. Solo el color de las imágenes.", "A", "La lista protege a las personas y a la autora."),
    ],
    [
        ex("Un compañero dice que su obra está en un circuito protegido porque la mandó a «solo unos pocos amigos». ¿Es suficiente?", "No", "Los archivos pueden reenviarse; se necesita un circuito controlado y permisos."),
        ex("Dos estudiantes presentan su secuencia. La primera dice «es una imagen imaginada y editada». El segundo no dice nada aunque la editó para engañar. ¿Quién cumple mejor con ser honesto con su audiencia?", "La primera", "Declarar la edición evita engañar a quien mira."),
    ],
    [
        ex("Presentas a tu familia, en una pantalla sin conexión a internet, una secuencia con tu amigo Pedro. Alguien pide una copia para subirla a una red abierta. ¿Qué haces? A. Decir que primero necesitas el permiso de Pedro y decidir tú qué compartes B. Dársela de inmediato.", "A", "Compartir en una red abierta exige permiso de quien aparece y decisión de la autora."),
        ex("Algo que viste en una pantalla te hizo sentir mal. ¿Qué haces? A. Aviso a una persona adulta de confianza B. Lo guardo en secreto.", "A", "Contarlo a una persona adulta de confianza protege tu bienestar."),
    ],
    ex("Preparas una exposición en la sala. Tienes 6 imágenes: dos con rostros sin permiso, dos de objetos y dos de paisajes sin datos. ¿Cuántas puedes presentar sin cambios? Elige: A. 4 B. 6.", "A", "Los 2 rostros sin permiso no se muestran: 6 − 2 = 4."),
    [
        ex("¿Qué se pide antes de usar el rostro de alguien?", "Permiso", "La imagen de una persona no se usa sin autorización."),
        ex("Verdadero o falso: declarar que una imagen es editada es opcional.", "Falso", "Se declara para no engañar."),
        ex("¿Qué haces si una imagen en línea te preocupa?", "Aviso a una persona adulta de confianza", "Es el paso más seguro."),
    ],
    task(
        "Elige UNA presentación. A) Una secuencia de seis imágenes de un objeto, impresa y colgada en la sala. B) Una secuencia de dibujos que se muestra a tu familia en una pantalla sin conexión a internet. C) Una ficha y tres imágenes en un panel del curso. Escribe: el circuito, a quién va dirigida, una lista de revisión de cuatro puntos (permisos, datos personales, autoría, declaración de edición) y la ficha con título, intención y técnica.",
        "Elegí la A. Circuito: la sala con mi curso. Audiencia: compañeros. Revisión: sin personas, sin nombres, imágenes mías y declaradas como editadas. Ficha: «La hoja que viaja». Intención: mostrar cómo el viento cambia el camino de una hoja. Técnica: fotografía de imaginación con edición simple.",
        ["elige un circuito protegido", "escribe la audiencia", "completa la lista de cuatro puntos", "redacta una ficha completa"],
        ["lista de revisión", "ficha"],
        ["usar una red abierta", "no declarar la edición"],
        "Destaca el punto de la lista más cuidado y pregunta qué cambiaría si la audiencia fuera distinta.",
    ),
    "Cuenta a una persona de tu casa a quién le mostrarías tu obra y a quién no, y por qué.",
    "Escribe un comentario respetuoso que darías a la obra de un compañero usando un criterio (por ejemplo, orden de la secuencia).",
)

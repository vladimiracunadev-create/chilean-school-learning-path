"""Música 3.º y 4.º medio FG: OAC-03 (interpretación de repertorios y estilos). Estilos, rutinas y arreglos de ejemplo, inventados; sin audio real."""
from __future__ import annotations

from fg_musi_common import build

O3 = "FG-MUSI-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (tres estilos de ejemplo, inventados, para interpretar). Estilo 1: frases largas y ligadas (legato), volumen suave que sube y baja, 65 pulsos por minuto. "
     "Estilo 2: sonidos cortos y cortados (staccato), acentos en los pulsos 2 y 4 de cada compás de 4/4, 100 pulsos por minuto. "
     "Estilo 3: pulso parejo y rápido a 140 pulsos por minuto, golpes de igual fuerza, voz hablada con ritmo marcado.")
build(
    O3, 1, F,
    use="Aprenderé a reconocer los elementos característicos de un estilo que importan al interpretar (articulación, acentos, fraseo, dinámica, tempo) y a relacionarlos con el propósito expresivo de una pieza.",
    prior=["Describo tempo, dinámica y timbre.", "Sé qué es un compás de 4/4.", "Distingo un rasgo audible de una opinión."],
    explain=[
        "Interpretar es hacer sonar una obra, propia o de otras personas, tomando decisiones sobre cómo tocarla o cantarla. Cada estilo tiene elementos característicos que se notan al interpretar: la articulación (qué tan unidos o separados suenan los sonidos: legato es ligado, staccato es cortado), los acentos (qué pulsos suenan más fuerte), el fraseo (cómo se agrupan los sonidos en frases con inicio y final), la dinámica (el volumen) y el tempo.",
        "Un acento cambia el carácter del ritmo. En un compás de 4/4, acentuar los pulsos 1 y 3 da una sensación distinta a acentuar el 2 y el 4. Por eso, al interpretar repertorio de otro estilo no basta con tocar las notas correctas: hay que respetar sus rasgos característicos. Al mismo tiempo, el propósito expresivo (qué quiero transmitir) puede orientar decisiones dentro del estilo.",
        "El repertorio personal es la música que cada persona elige o crea para interpretar; el repertorio de otros músicos es el que ellos crearon o hicieron conocido. En ambos casos conviene escuchar con atención, anotar los rasgos y practicar uno por uno.",
    ],
    vocab=[("articulación", "forma de unir o separar los sonidos al tocar o cantar"), ("legato", "articulación en que los sonidos se unen sin cortes"), ("staccato", "articulación en que los sonidos se tocan cortos y separados"), ("acento", "sonido o pulso que se hace sonar más fuerte"), ("fraseo", "manera de agrupar los sonidos en frases"), ("repertorio", "conjunto de obras que una persona o grupo puede interpretar")],
    worked=[
        ("Reconocer un acento", "En un patrón de 4/4 los pulsos 2 y 4 suenan más fuertes que el 1 y el 3. ¿Qué estás identificando?", ["Se comparan la fuerza de los pulsos.", "Los pulsos que suenan más fuerte llevan acento.", "El patrón tiene acentos en el 2 y el 4."], "Los acentos del patrón, en los pulsos 2 y 4"),
        ("Elegir articulación", "Quieres interpretar una frase tranquila y continua. ¿Qué articulación te sirve y por qué?", ["Una frase continua pide unir los sonidos.", "El legato une los sonidos sin cortes.", "Staccato los separaría y daría sensación de salto."], "Legato, porque une los sonidos"),
    ],
    mistakes=[("Pensar que interpretar bien es tocar todas las notas correctas.", "También cuentan articulación, acentos, fraseo y dinámica propios del estilo.", "Revisa esos elementos además de las notas."),
              ("Cambiar los acentos del patrón porque «suena igual».", "Mover los acentos cambia el carácter del ritmo.", "Practica el acento original contando en voz baja.")],
    T=[
        ('abc', '{F} ¿Qué estilo usa sonidos cortos y cortados?', 'El estilo 2, que usa staccato y sonidos separados', 'El estilo 1, que usa legato', 'El estilo 3, de voz hablada', 'El staccato separa los sonidos; el legato los une.'),
        ('abc', '{F} ¿En qué pulsos están los acentos del estilo 2?', '2 y 4', '1 y 3', '1 y 4', 'La ficha indica acentos en los pulsos 2 y 4.'),
        ('ab', 'La articulación se refiere a', 'cómo se unen o separan los sonidos', 'cuánto dura la pieza completa', 'La articulación es la forma de unir o separar los sonidos al interpretar.'),
        ('abc', '{F} ¿Qué estilo tiene el tempo más lento?', 'El estilo 1, con 65 pulsos por minuto, el menor de los tres', 'El estilo 2, con 100 pulsos por minuto', 'El estilo 3, con 140 pulsos por minuto', '65 es el menor de los tres tempos.'),
        ('abc', '{F} Quieres interpretar una frase larga y continua de forma tranquila. ¿Qué estilo te sirve de modelo?', 'El estilo 1, por su legato y su volumen suave', 'El estilo 2, por sus sonidos cortos', 'El estilo 3, por su pulso rápido y parejo', 'Legato y volumen suave favorecen la continuidad tranquila.'),
        ('abc', '{F} En el estilo 3 todos los golpes tienen igual fuerza. ¿Qué rasgo falta respecto del estilo 2?', 'Acentos en pulsos específicos', 'Un pulso estable', 'Un tempo rápido', 'El estilo 2 acentúa el 2 y el 4; el estilo 3 los iguala.'),
        ('abc', 'Una estudiante toca todas las notas bien pero en vez de ligar corta cada sonido. ¿Qué elemento del estilo no respetó?', 'La articulación: cambió sonidos ligados por cortados', 'El título, porque la pieza cambió de nombre', 'El tempo, porque la pieza se tocó más rápido', 'Cambió legato por cortes, o sea la articulación.'),
        ('abc', '{F} ¿Cuántos acentos hay en 3 compases de 4/4 del estilo 2?', '6', '3', '12', 'Cada compás tiene 2 acentos y 3 × 2 = 6.'),
        ('abc', 'Un grupo quiere interpretar una canción de otro músico. ¿Cuál es el primer paso razonable?', 'Escuchar y anotar los rasgos característicos del estilo', 'Cambiar el estilo para que sea suyo', 'Aprender solo la letra sin escuchar nada', 'Anotar rasgos permite respetar el estilo al interpretar.'),
        ('abc', '{F} El propósito de una pieza es «sorprender». ¿Qué decisión de dinámica es coherente?', 'Pasar de un volumen muy suave a un acento fuerte e inesperado', 'Mantener el mismo volumen todo el tiempo', 'Tocar todo en legato sin cambios', 'Un contraste de volumen genera sorpresa.'),
        ('abc', 'Dos compañeros discuten: uno dice que el repertorio personal vale menos que el de otros músicos. ¿Qué respuesta es mejor?', 'Ambos se interpretan con criterio; lo importante es respetar sus rasgos y su propósito', 'Sí, porque lo conocido siempre es superior', 'No, porque lo personal no necesita practicarse', 'El valor de una interpretación está en las decisiones, no en el origen de la obra.'),
        ('abc', '{F} Si una misma frase pasa del estilo 2 al estilo 1, ¿cómo cambia su articulación?', 'Pasa de cortada (staccato) a ligada (legato), con volumen más suave', 'Pasa de ligada a cortada', 'No cambia: solo cambia el tempo', 'El estilo 1 usa legato y el 2 usa staccato.'),
        ('=', '{F} Un pasaje del estilo 3 dura 28 pulsos. ¿Cuántos compases de 4/4 son?', '28//4', 'Se divide el total de pulsos por los 4 pulsos de cada compás.', ' compases'),
    ],
    ctx=('abc', 'Un grupo escolar quiere interpretar una pieza de otro estilo, pero la toca con los acentos corridos «porque queda más fácil». ¿Qué conviene decirles?', 'Que practiquen con el acento original, contando en voz baja los pulsos', 'Que el acento no importa si las notas son correctas', 'Que cambien de pieza si algo es difícil', 'El acento es un rasgo característico; se practica, no se elimina.'),
    sc=[
        ('¿Qué es el legato?', 'Unir los sonidos sin cortes', 'Los sonidos se tocan ligados, sin separaciones.'),
        ('¿Qué es un acento?', 'Un pulso o sonido que se hace sonar más fuerte', 'Marca los pulsos con más fuerza dentro del compás.'),
        ('abc', 'Interpretar bien un estilo implica', 'respetar articulación, acentos, fraseo y dinámica', 'tocar solo las notas correctas', 'tocar lo más fuerte posible', 'El estilo se expresa más allá de las notas.'),
    ],
    op=("Con la {F} elige uno de los tres estilos y escribe cuatro instrucciones para interpretar una frase: articulación, acentos (en qué pulsos), dinámica y tempo, y un propósito expresivo que cuadre con ellas.",
        "Estilo 2. Articulación: staccato. Acentos: pulsos 2 y 4. Dinámica: media. Tempo: 100 pulsos por minuto. Propósito: dar sensación de alegría ligera.",
        ["cuatro instrucciones", "coherentes con el estilo", "propósito"], ["pauta de interpretación"], ["mezclar rasgos de estilos distintos", "no indicar los pulsos"],
        "Reconoce las instrucciones y pide revisar que cada una cuadre con el mismo estilo."),
    reinforce="Elige una canción que te guste y anota su articulación, sus acentos y su tempo.",
    extend="Compara dos canciones del mismo tempo y explica cómo se diferencian en articulación y acentos.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (rutina de ensayo de ejemplo de 20 minutos, para voz o instrumento). Calentamiento: 5 minutos de respiración y notas suaves. Pasaje difícil: 8 minutos a tempo lento. "
     "Pieza completa: 5 minutos. Pausa para descansar y beber agua: 2 minutos. Reglas: postura erguida y relajada; no forzar la voz ni gritar; volumen moderado; si algo duele, se detiene y se avisa a una persona adulta.")
build(
    O3, 2, F,
    use="Aprenderé a organizar el trabajo técnico (postura, respiración, afinación, calentamiento, volumen seguro y descanso) para interpretar con coherencia con lo que quiero expresar, sin dañar la voz ni los oídos.",
    prior=["Reconozco articulación, acentos y dinámica.", "Sé que el volumen alto daña los oídos.", "Distingo ensayo de presentación."],
    explain=[
        "El trabajo técnico es el que prepara al cuerpo y al oído para interpretar con control. Incluye la postura (erguida y relajada), la respiración (lenta y profunda, sin elevar los hombros), la afinación (que las notas suenen en su altura correcta) y el control del pulso. Una buena técnica no es un fin en sí misma: sirve a lo que se quiere expresar. Por ejemplo, controlar el aire permite sostener una nota larga y suave si el propósito es calma.",
        "Un ensayo eficaz tiene calentamiento, trabajo de lo difícil, pieza completa y descanso. Se comienza suave y se sube la exigencia de a poco. La voz no se fuerza: gritar o seguir con dolor puede dañarla. Con instrumentos, se evita el volumen alto y se hacen pausas para cuidar los oídos. Si algo duele, se detiene el ensayo y se avisa a una persona adulta de confianza.",
        "Conviene anotar qué practicaste, cuánto tiempo y qué mejoró. Eso ayuda a decidir qué trabajar la próxima vez.",
    ],
    vocab=[("técnica", "conjunto de habilidades para tocar o cantar con control"), ("afinación", "que las notas suenen en la altura correcta"), ("calentamiento", "ejercicios suaves antes de ensayar"), ("postura", "forma de colocar el cuerpo al tocar o cantar"), ("respiración", "manejo del aire que sostiene la voz o el soplo")],
    worked=[
        ("Sumar el tiempo de ensayo", "Una rutina tiene 4 minutos de calentamiento, 7 de pasaje difícil y 6 de pieza completa. ¿Cuánto dura sin pausas?", ["Calentamiento: 4.", "Pasaje difícil: 7.", "Pieza completa: 6. Total: 4 + 7 + 6 = 17."], "17 minutos"),
        ("Relacionar técnica y propósito", "Una estudiante quiere cantar una frase calmada y se queda sin aire a la mitad. ¿Qué parte técnica debe trabajar?", ["El propósito pide una nota larga y suave.", "Eso depende del control de la respiración.", "Debe practicar respiraciones lentas y sostener el aire de a poco."], "La respiración"),
    ],
    mistakes=[("Ensayar siempre a máximo volumen para «sonar con ganas».", "Daña los oídos y oculta errores de afinación y pulso.", "Ensaya a volumen moderado y sube solo si el pasaje lo necesita."),
              ("Saltarse el calentamiento por falta de tiempo.", "Aumenta el riesgo de tensión y de errores.", "Reduce el pasaje difícil, no el calentamiento.")],
    T=[
        ('=', '{F} ¿Cuántos minutos de trabajo hay en la rutina sin contar la pausa?', '5+8+5', 'Se suman calentamiento, pasaje difícil y pieza completa.', ' minutos'),
        ('abc', '{F} ¿Cuánto dura la rutina completa, con la pausa?', '20 minutos', '18 minutos', '25 minutos', 'Los cuatro bloques suman 5 + 8 + 5 + 2 = 20 minutos.'),
        ('abc', '{F} ¿Por qué el calentamiento va primero?', 'Prepara al cuerpo y se sube la exigencia de a poco', 'Porque es la parte más difícil de la pieza', 'Porque así se evita usar la respiración', 'Se empieza suave para evitar tensión.'),
        ('abc', '¿Qué significa afinación?', 'Que las notas suenen en su altura correcta', 'Que la pieza dure lo mismo en cada ensayo', 'Que el volumen sea el mismo', 'La afinación es la altura correcta del sonido.'),
        ('abc', 'Una estudiante siente dolor en la garganta al cantar. ¿Qué debe hacer?', 'Detenerse y avisar a una persona adulta de confianza', 'Cantar más fuerte para aflojar la garganta', 'Seguir y no decir nada hasta terminar', 'El dolor es una señal para parar y pedir ayuda.'),
        ('abc', '{F} La pieza completa de la rutina se repite 3 veces seguidas, de 5 minutos cada vez. ¿Cuántos minutos son?', '15', '8', '10', '5 minutos por 3 repeticiones son 15 minutos.'),
        ('abc', '{F} ¿Qué regla de la ficha protege la voz?', 'No forzarla ni gritar, y parar si hay dolor', 'Practicar sin pausas', 'Usar el volumen máximo', 'La ficha indica no forzar la voz.'),
        ('abc', 'Un guitarrista ensaya con amplificador al máximo «para sentir la fuerza». ¿Qué conviene decirle?', 'Que baje el volumen para cuidar sus oídos y oír mejor sus errores', 'Que suba aún más para no oír a los demás', 'Que no ensaye nunca con amplificador', 'El volumen alto daña la audición y oculta errores.'),
        ('abc', '{F} Si solo tienes 15 minutos, ¿qué decisión protege mejor el cuerpo?', 'Acortar el pasaje difícil y mantener el calentamiento y la pausa', 'Eliminar el calentamiento porque no es necesario', 'Eliminar la pausa para que dure más la pieza', 'El calentamiento y la pausa protegen el cuerpo; se ajusta el trabajo más largo.'),
        ('abc', 'Una cantante domina la afinación pero su interpretación suena sin emoción. ¿Qué falta?', 'Relacionar la técnica con lo que quiere expresar', 'Más volumen y velocidad', 'Cambiar de repertorio', 'La técnica debe servir al propósito expresivo.'),
        ('abc', '{F} El tiempo total del pasaje difícil en tres ensayos seguidos de 8 minutos es', '24 minutos', '16 minutos', '32 minutos', '8 minutos por 3 ensayos son 24 minutos.'),
        ('abc', '¿Cuál es una postura adecuada para cantar o tocar?', 'Erguida y relajada, sin elevar los hombros', 'Encorvada, para apoyarse en la silla', 'Rígida, con los hombros muy altos', 'La postura erguida y relajada facilita respirar y evita tensión.'),
        ('abc', '{F} ¿Para qué sirve anotar qué se practicó y qué mejoró?', 'Para decidir qué trabajar en la próxima sesión', 'Para saber quién practicó más tiempo', 'Para no repetir la misma pieza nunca más', 'El registro orienta el trabajo siguiente.'),
    ],
    ctx=('abc', 'Un coro escolar tiene 24 minutos de ensayo. Quiere calentamiento de 6 minutos, 12 de repertorio y una pausa. ¿Cuánto puede durar la pausa?', '6 minutos', '8 minutos', '4 minutos', '24 − 6 − 12 = 6 minutos.'),
    sc=[
        ('¿Para qué sirve el calentamiento?', 'Para preparar el cuerpo antes de ensayar', 'Evita tensión y errores por empezar con mucha exigencia.'),
        ('¿Qué hacer si algo duele al ensayar?', 'Detenerse y avisar a una persona adulta', 'El dolor es una señal para parar y pedir ayuda.'),
        ('abc', 'La técnica se trabaja para', 'servir a lo que se quiere expresar', 'competir con otros grupos', 'tocar más fuerte', 'La técnica es un medio para el propósito expresivo.'),
    ],
    op=("Con la {F} diseña una rutina de ensayo de 25 minutos para un pasaje que quieras mejorar: bloques con tiempos que sumen 25, una regla de cuidado de la voz o los oídos y el propósito expresivo que orienta el trabajo.",
        "Calentamiento 5, pasaje difícil a tempo lento 10, pieza completa 7, pausa 3 = 25. Regla: volumen moderado y detenerme si algo duele. Propósito: que la frase final suene calmada.",
        ["tiempos que suman 25", "regla de cuidado", "propósito expresivo"], ["rutina por bloques"], ["tiempos que no suman", "olvidar cuidado auditivo"],
        "Reconoce la rutina y pide comprobar la suma de minutos."),
    reinforce="Escribe una rutina de ensayo de 15 minutos con tres bloques y comprueba que suma 15.",
    extend="Prueba tres respiraciones lentas y cuenta cuántos pulsos puedes sostener una nota suave; anota el resultado.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (plan de estudio de ejemplo para un pasaje difícil de 4 compases en 4/4, o sea 16 pulsos). Etapa 1: separar y repetir el compás 3, que es el más difícil, a 60 pulsos por minuto. "
     "Etapa 2: unir los compases 2 y 3 a 60. Etapa 3: tocar los 4 compases a 60. Etapa 4: subir a 70, luego a 80, solo si las notas salen parejas dos veces seguidas. "
     "Criterio de calidad: pulso estable y afinación correcta antes de subir el tempo.")
build(
    O3, 3, F,
    use="Aprenderé a ensayar un pasaje difícil con un plan técnico: dividirlo, empezar lento, subir el tempo de a poco con un criterio de calidad y comprobar si mejora la expresión.",
    prior=["Calculo duraciones con pulsos por minuto.", "Cuido voz y oídos al ensayar.", "Sé qué es una rutina de ensayo."],
    explain=[
        "Un pasaje difícil se aprende mejor dividiéndolo. Primero se aísla el compás más difícil, se repite despacio y se comprueba que salga con pulso estable y afinación correcta. Después se une con el compás anterior, y recién entonces se toma el pasaje completo. A esto se le llama estudio por partes. Repetir a toda velocidad un pasaje que sale mal solo fija el error.",
        "El tempo se sube de a poco: por ejemplo de 60 a 70 y luego a 80 pulsos por minuto, solo cuando el pasaje sale parejo dos veces seguidas al tempo actual. Para calcular cuánto dura un pasaje se usa: segundos = pulsos × 60 ÷ pulsos por minuto. Cuatro compases de 4/4 son 16 pulsos; a 60 pulsos por minuto duran 16 segundos.",
        "La técnica está al servicio de la expresión. Cuando el pasaje ya sale con seguridad, se agregan las decisiones expresivas: dinámica, articulación y fraseo. Si al subir el tempo se pierde la calidad, se vuelve al tempo anterior sin culpa.",
    ],
    vocab=[("estudio por partes", "trabajar un pasaje dividiéndolo en secciones pequeñas"), ("tempo lento", "pulsos más espaciados, para controlar cada nota"), ("pulso estable", "pulsos que se mantienen parejos, sin acelerar ni frenar"), ("criterio de calidad", "condición que debe cumplirse antes de pasar a la etapa siguiente"), ("fijar un error", "repetir un error hasta aprenderlo mal")],
    worked=[
        ("Calcular una duración", "Un pasaje de 8 pulsos va a 120 pulsos por minuto. ¿Cuántos segundos dura?", ["8 × 60 = 480.", "480 ÷ 120 = 4."], "4 segundos"),
        ("Decidir si subir el tempo", "Un estudiante toca el pasaje a 60 con una nota desafinada una de dos veces. ¿Sube a 70?", ["El criterio pide que salga parejo dos veces seguidas.", "No se cumplió.", "Debe repetir a 60 antes de subir."], "No, repite a 60 hasta que salga parejo dos veces seguidas"),
    ],
    mistakes=[("Practicar el pasaje difícil a tempo rápido «para acostumbrarse».", "Se fijan los errores y se pierde el control del pulso.", "Empieza lento y sube de a poco."),
              ("Subir el tempo por tiempo transcurrido, no por calidad.", "El avance debe depender del criterio, no del reloj.", "Sube solo si sale parejo dos veces seguidas.")],
    T=[
        ('=', '{F} Los 4 compases son 16 pulsos a 60 pulsos por minuto. ¿Cuántos segundos duran?', '16*60//60', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto.', ' segundos'),
        ('abc', '{F} ¿Qué compás se aísla primero?', 'El compás 3, por ser el más difícil', 'El compás 1, por ser el primero', 'Los cuatro compases juntos', 'El plan comienza con el compás más difícil.'),
        ('abc', '{F} ¿Qué se debe cumplir antes de subir de 60 a 70?', 'Que el pasaje salga parejo dos veces seguidas', 'Que haya pasado una hora de ensayo', 'Que el público ya lo haya escuchado', 'El criterio de calidad decide el avance.'),
        ('=', '{F} A 80 pulsos por minuto, ¿cuántos segundos duran 16 pulsos?', '16*60//80', 'Se multiplican 16 pulsos por 60 y se divide por 80.', ' segundos'),
        ('abc', 'Un estudiante toca un pasaje rápido, con errores, siete veces seguidas. ¿Qué riesgo corre?', 'Fijar los errores, es decir, aprender mal el pasaje', 'Aprender el pulso con más rapidez', 'Mejorar la afinación sin esfuerzo', 'Repetir mal a velocidad alta consolida el error.'),
        ('abc', '{F} ¿Cuál es el orden correcto de las etapas?', 'Aislar, unir dos compases, tocar los cuatro y subir el tempo', 'Subir el tempo, tocar los cuatro y aislar', 'Tocar los cuatro a tempo máximo y luego dividir', 'Se avanza de lo pequeño a lo grande y del tempo lento al rápido.'),
        ('abc', '{F} El estudiante llegó a 70 y las notas dejaron de salir parejas. ¿Qué hace?', 'Vuelve a 60 y trabaja ahí hasta que salga parejo otra vez', 'Sigue subiendo a 80 para acostumbrarse', 'Cambia el pasaje por uno fácil', 'Volver al tempo anterior recupera el control.'),
        ('abc', 'Una cantante domina un pasaje lento pero suena rígida. ¿Qué paso sigue?', 'Agregar decisiones expresivas como dinámica y fraseo', 'Cantar todo más fuerte', 'Dejar de practicar el pasaje', 'Una vez seguro, el pasaje se trabaja expresivamente.'),
        ('abc', '{F} ¿Cuántos pulsos tienen los compases 2 y 3 juntos?', '8', '4', '16', 'Cada compás tiene 4 pulsos y 2 × 4 = 8.'),
        ('abc', '{F} El criterio de calidad incluye', 'pulso estable y afinación correcta antes de subir el tempo', 'tempo máximo y volumen alto', 'repetir cuatro veces en cualquier orden', 'La ficha define esos dos rasgos como condición.'),
        ('abc', 'Un grupo cree que «mientras más rápido toquen, más técnica tienen». ¿Qué respuesta corresponde?', 'La velocidad sola no mide la técnica; importan el control y la calidad', 'Es correcto, la velocidad define la técnica', 'No importa porque la técnica no se mide', 'La técnica es control, no solo rapidez.'),
        ('abc', '{F} Si tocas el pasaje de 16 pulsos a 60 y a 80, ¿en cuántos segundos se diferencian?', '4 segundos, porque 16 pulsos a 60 duran 16 y a 80 duran 12', '16 segundos', '2 segundos', 'A 60 dura 16 s y a 80 dura 12 s; la diferencia es 4.'),
        ('abc', 'Antes de subir el tempo, ¿qué registro conviene hacer?', 'Anotar el tempo logrado y el error que aún aparece', 'Anotar solo el nombre de la pieza', 'No anotar nada para no perder tiempo', 'El registro permite avanzar con evidencia.'),
    ],
    ctx=('abc', 'Un guitarrista toca un pasaje de 12 pulsos a 60 y quiere pasar a 80. A 60 sale parejo una vez y falla la segunda. ¿Qué decide?', 'Seguir a 60 hasta que salga parejo dos veces seguidas', 'Subir a 80 porque ya salió una vez bien', 'Parar y no ensayar más ese pasaje', 'Aún no cumple el criterio de dos veces seguidas.'),
    sc=[
        ('¿Cuántos segundos duran 24 pulsos a 60 pulsos por minuto?', '24', 'A 60 pulsos por minuto cada pulso dura un segundo.'),
        ('¿Qué es el estudio por partes?', 'Trabajar el pasaje dividido en secciones pequeñas', 'Aísla lo difícil antes de unirlo.'),
        ('abc', 'Subir el tempo debe depender de', 'la calidad con que sale el pasaje en el tempo actual', 'el tiempo que pasó en el reloj', 'la opinión de quien no escuchó', 'El avance se decide con un criterio de calidad.'),
    ],
    op=("Con la {F} como modelo, diseña un plan de estudio para un pasaje difícil de 3 compases de 4/4 (12 pulsos): tres etapas, un tempo inicial, un criterio de calidad para subir y cuánto dura el pasaje al tempo inicial.",
        "Etapa 1: compás 2 solo. Etapa 2: compases 1 y 2. Etapa 3: los tres compases. Tempo inicial: 60. Criterio: sale parejo dos veces seguidas. Duración: 12 × 60 ÷ 60 = 12 segundos.",
        ["tres etapas", "criterio de calidad", "duración calculada"], ["plan de estudio"], ["subir el tempo sin criterio", "calcular mal la duración"],
        "Reconoce el plan y pide verificar la duración del pasaje."),
    reinforce="Calcula cuánto dura un pasaje de 16 pulsos a 50 y a 100 pulsos por minuto.",
    extend="Aplica el plan de tres etapas a una frase de una canción conocida y anota qué tempo alcanzaste.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (arreglo de ejemplo para un trío, 8 compases de 4/4). Intérprete A: melodía en los compases 1 a 8. Intérprete B: acompañamiento con notas largas, entra en el compás 3. Intérprete C: percusión suave de objetos, entra en el compás 5. "
     "Antes de empezar, quien dirige cuenta en voz baja «1, 2, 3, 4» para dar el tempo (80 pulsos por minuto). En el compás 8 las tres personas terminan juntas y reducen el volumen. Regla: volumen moderado; todas escuchan a las demás.")
build(
    O3, 4, F,
    use="Aprenderé a interpretar en conjunto: coordinar entradas y finales, equilibrar los roles de melodía, acompañamiento y ritmo, y escuchar a las demás personas para sonar como un solo grupo.",
    prior=["Practico un pasaje con plan técnico.", "Cuento compases y pulsos.", "Sé mantener un pulso estable."],
    explain=[
        "Interpretar en conjunto exige coordinar a varias personas. Cada una cumple un rol: la melodía lleva la idea principal, el acompañamiento sostiene la armonía con notas o acordes, y la percusión o el ritmo marca el pulso. Un buen conjunto equilibra los volúmenes para que la melodía se oiga y nadie quede tapado. Para eso, además de tocar bien, hay que escuchar a las demás personas durante toda la pieza.",
        "Antes de empezar se da una cuenta previa en voz baja (por ejemplo «1, 2, 3, 4») que fija el tempo y avisa cuándo entrar. Cada entrada se prepara contando los compases de silencio: si un intérprete entra en el compás 3, debe esperar 2 compases. Los finales también se acuerdan: quien dirige o marca con un gesto suave el momento de terminar juntos.",
        "Si el grupo no suena junto, se revisa una cosa por vez: el pulso, las entradas, el equilibrio de volumen o el final. Se ensaya en volumen moderado para cuidar los oídos.",
    ],
    vocab=[("conjunto", "grupo de personas que interpretan juntas"), ("rol", "función que cumple cada intérprete: melodía, acompañamiento o ritmo"), ("cuenta previa", "conteo en voz baja que fija el tempo antes de empezar"), ("entrada", "momento en que una persona empieza a tocar o cantar"), ("equilibrio", "volumen adecuado de cada rol para que se oiga la melodía")],
    worked=[
        ("Contar compases de espera", "En un arreglo, el intérprete B entra en el compás 5. ¿Cuántos compases espera?", ["Antes del compás 5 están los compases 1, 2, 3 y 4.", "Espera 5 − 1 = 4 compases."], "4 compases"),
        ("Elegir un ajuste de equilibrio", "En el ensayo no se oye la melodía porque el acompañamiento suena muy fuerte. ¿Qué ajuste conviene?", ["No se sube el volumen de todo.", "Se baja el acompañamiento.", "Se vuelve a escuchar."], "Bajar el acompañamiento y volver a escuchar"),
    ],
    mistakes=[("Escuchar solo la propia parte.", "Se pierde la sincronía y no se nota que se tapa a las demás personas.", "Alterna la atención entre tu parte y el conjunto."),
              ("Empezar sin cuenta previa «porque todos saben el tempo».", "Cada persona entra con un tempo ligeramente distinto.", "Da siempre una cuenta previa antes de empezar.")],
    T=[
        ('=', '{F} ¿Cuántos compases espera el intérprete B antes de entrar?', '3-1', 'B entra en el compás 3, así que espera los compases 1 y 2.', ' compases'),
        ('=', '{F} ¿Cuántos compases toca la percusión (C) hasta el final?', '8-5+1', 'C toca desde el compás 5 hasta el 8, ambos incluidos.', ' compases'),
        ('abc', '{F} ¿Qué rol cumple el intérprete A?', 'Melodía, que lleva la idea principal', 'Acompañamiento, que sostiene la armonía', 'Percusión, que marca el pulso', 'A lleva la idea principal en todos los compases.'),
        ('abc', '{F} ¿Para qué se da la cuenta previa?', 'Para fijar el tempo común y avisar cuándo empezar', 'Para cambiar el tempo durante la pieza', 'Para que la melodía suene fuerte', 'La cuenta previa da el tempo común.'),
        ('abc', '{F} ¿Qué ocurre en el compás 8?', 'Las tres personas terminan juntas y reducen el volumen', 'La percusión sigue sola', 'La melodía se repite', 'La ficha indica un final conjunto con volumen menor.'),
        ('abc', '{F} En el compás 6 suenan tres roles a la vez. ¿Qué rol conviene que se oiga más?', 'La melodía, porque lleva la idea principal', 'La percusión, porque marca el pulso', 'El acompañamiento, porque sostiene la armonía', 'La melodía lleva la idea principal; los otros la sostienen.'),
        ('abc', 'En un ensayo, A y B no terminan juntos. ¿Qué corresponde acordar?', 'Quién marca el final y con qué gesto lo harán todas las personas', 'Que A toque más fuerte para llegar primero', 'Que B no termine nunca', 'Un final conjunto se acuerda con una señal clara.'),
        ('abc', '{F} El intérprete C se adelanta y entra en el compás 4. ¿Qué error comete?', 'No cuenta bien los compases de espera antes de su entrada', 'Toca con articulación incorrecta', 'Usa un objeto fuerte', 'Debía esperar hasta el compás 5.'),
        ('abc', 'Un percusionista no escucha a los demás y sube su volumen. ¿Qué conviene?', 'Escuchar al conjunto y ajustar su volumen para equilibrar', 'Tocar aún más fuerte para marcar el pulso', 'Dejar de tocar hasta el final del ensayo', 'El equilibrio depende de escuchar a las demás personas.'),
        ('abc', '{F} Si el tempo es 80 pulsos por minuto, ¿cuántos segundos dura la cuenta previa de 4 pulsos?', '3 segundos', '4 segundos', '2 segundos', '4 × 60 ÷ 80 = 3 segundos.'),
        ('abc', '{F} Si el trío ensaya el arreglo completo 3 veces, ¿cuántos compases toca en total la melodía?', '24', '8', '16', '3 veces por 8 compases son 24 compases.'),
        ('abc', 'El grupo no suena junto. ¿Cuál es una buena forma de revisar?', 'Revisar una cosa por vez: pulso, entradas, equilibrio y final', 'Cambiar todo a la vez', 'Culpar a quien tocó más fuerte', 'Revisar de a una cosa permite encontrar la causa.'),
        ('abc', '{F} Una estudiante dice que su parte, el acompañamiento, no importa porque no es la melodía. ¿Qué respuesta es mejor?', 'Importa: sostiene la melodía y el conjunto la necesita', 'Tiene razón, el acompañamiento no se nota', 'Puede dejar de tocar y nadie lo notará', 'Cada rol aporta al resultado del conjunto.'),
    ],
    ctx=('abc', 'Un grupo escolar toca un arreglo de 8 compases a 80 pulsos por minuto. Los tres entran juntos en el compás 1 aunque la ficha indica entradas distintas, y la melodía se tapa. ¿Qué ajuste corresponde?', 'Hacer entrar a B en el compás 3 y a C en el 5, como indica el arreglo', 'Subir el volumen de la melodía y dejar las entradas', 'Cambiar el arreglo para que todos toquen igual', 'Las entradas escalonadas dan espacio a la melodía.'),
    sc=[
        ('¿Para qué sirve la cuenta previa?', 'Para fijar el tempo y avisar cuándo entrar', 'Da el tempo común a todo el grupo.'),
        ('Si alguien entra en el compás 6, ¿cuántos compases de espera tiene?', '5', 'Espera los compases 1 a 5.'),
        ('abc', 'En un conjunto, la melodía debe', 'oírse con claridad sobre el resto sin tapar a nadie', 'sonar siempre lo más fuerte posible', 'quedar oculta por el acompañamiento', 'El equilibrio permite oír la idea principal.'),
    ],
    op=("Con la {F} como modelo, escribe un arreglo para un trío de 6 compases: qué rol toca cada persona, en qué compás entra cada una, cómo dan la cuenta previa y cómo terminan juntas, y una regla de volumen.",
        "A melodía compases 1-6; B acompañamiento desde el compás 2; C percusión desde el compás 4. Cuenta previa «1, 2, 3, 4» en voz baja. Final: todas reducen el volumen en el compás 6 al ver la señal de A. Volumen moderado.",
        ["roles definidos", "entradas por compás", "cuenta previa y final"], ["arreglo escrito"], ["entradas confusas", "sin regla de volumen"],
        "Reconoce el arreglo y pide revisar cuántos compases espera cada persona."),
    reinforce="Entra en un compás de 4/4 con una compañera después de una cuenta previa y anota si empezaron juntas.",
    extend="Escribe dos finales posibles para un arreglo y explica en qué cambia el efecto.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (pauta de autoevaluación de ejemplo para una grabación a volumen moderado). Cada criterio se puntúa de 1 (falta trabajar) a 3 (logrado): pulso estable, afinación, articulación del estilo, dinámica expresiva. "
     "Resultados de una interpretación de ejemplo: pulso estable 2, afinación 3, articulación 1, dinámica 2. Propósito expresivo: transmitir calma. Meta de la próxima sesión: mejorar el criterio con menor puntaje.")
build(
    O3, 5, F,
    use="Aprenderé a registrar una interpretación con una pauta de criterios, detectar qué trabajo técnico falta y ajustarlo en la próxima sesión, de modo coherente con el propósito expresivo.",
    prior=["Estudio un pasaje por partes.", "Interpreto en conjunto.", "Separo evidencia de opinión."],
    explain=[
        "Registrar una interpretación permite escucharte desde afuera. Puede hacerse con una grabación a volumen moderado, una pauta escrita o ambas. Una pauta de autoevaluación define criterios claros: pulso estable, afinación, articulación propia del estilo y dinámica expresiva. Cada criterio se puntúa con una escala simple, por ejemplo de 1 a 3, y se anota una evidencia: el compás o instante donde se oye.",
        "Con los puntajes se decide qué ajustar. Se prioriza el criterio más bajo, o el que más afecte el propósito expresivo. Por ejemplo, si el propósito es transmitir calma y la articulación es cortada, ese criterio es una prioridad aunque otro puntaje también sea bajo. Se fija una meta pequeña y medible para la próxima sesión, como «tocar los compases 3 y 4 con legato dos veces seguidas».",
        "Autoevaluarse con honestidad no es juzgarse con dureza: es describir lo que se oye. Un puntaje alto no significa perfección, sino que el criterio se cumple con claridad en ese momento.",
    ],
    vocab=[("pauta de autoevaluación", "lista de criterios para revisar la propia interpretación"), ("criterio", "aspecto concreto que se revisa"), ("evidencia", "instante o compás donde se oye el criterio"), ("meta medible", "objetivo pequeño que se puede comprobar"), ("puntaje", "número que indica cuánto se cumple un criterio")],
    worked=[
        ("Sumar la pauta", "Un estudiante obtiene 3, 2, 2 y 1 en cuatro criterios. ¿Cuántos puntos suma de un máximo de 12?", ["3 + 2 + 2 + 1 = 8.", "El máximo es 4 × 3 = 12."], "8 de 12 puntos"),
        ("Elegir la prioridad", "Un estudiante tiene afinación 3, pulso 1 y dinámica 2. ¿Qué prioriza?", ["El menor puntaje es el pulso, con 1.", "El pulso afecta a todo el pasaje."], "El pulso"),
    ],
    mistakes=[("Escribir «lo hice bien» sin un criterio.", "No se sabe qué conservar ni qué ajustar.", "Puntúa cada criterio y cita el compás."),
              ("Fijar metas gigantes como «tocar perfecto».", "No se pueden comprobar.", "Elige una meta pequeña y medible para la próxima sesión.")],
    T=[
        ('=', '{F} ¿Cuántos puntos suma la interpretación de ejemplo?', '2+3+1+2', 'Se suman los cuatro puntajes de la ficha.', ' puntos'),
        ('abc', '{F} ¿Cuál es el máximo posible de la pauta?', '12 puntos, por 4 criterios de 3 puntos', '9 puntos, por 3 criterios de 3 puntos', '16 puntos, por 4 criterios de 4 puntos', 'Cuatro criterios por 3 puntos cada uno dan 12.'),
        ('abc', '{F} ¿Qué criterio tiene el puntaje más bajo?', 'La articulación, con puntaje 1', 'La afinación', 'El pulso estable', 'La articulación tiene 1; los otros tienen 3 y 2.'),
        ('abc', '{F} Con el propósito de transmitir calma, ¿por qué conviene priorizar la articulación?', 'Porque tiene el menor puntaje y la calma pide sonidos ligados', 'Porque es el criterio más fácil de subir', 'Porque la afinación no importa', 'Un estilo ligado ayuda a la calma; la articulación está en 1.'),
        ('abc', 'Una buena meta medible es', 'tocar los compases 3 y 4 con legato dos veces seguidas', 'tocar la pieza de manera perfecta en la próxima sesión', 'tocar mejor que ayer en la próxima sesión', 'La primera se puede comprobar con claridad.'),
        ('abc', '{F} Si el puntaje de pulso sube de 2 a 3 en la próxima sesión, ¿cuántos puntos suma ahora la pauta (los demás igual)?', '9', '8', '10', 'Antes eran 8 y sube 1 punto.'),
        ('abc', 'Alguien anota: «afinación 2: se desafina en el compás 5». ¿Qué tiene de bueno esta anotación?', 'Incluye un puntaje y una evidencia', 'Solo expresa una opinión', 'No dice dónde está el problema', 'Cita el compás donde se oye la desafinación.'),
        ('abc', '{F} Una estudiante dice que 3 en afinación significa que no necesita practicar más. ¿Qué es más preciso?', 'Significa que el criterio se cumple con claridad, pero hay otros por trabajar', 'Es correcto, no necesita practicar nada', 'Significa que debe dejar la afinación para siempre', 'Un puntaje alto en un criterio no cubre el resto.'),
        ('abc', '¿Por qué grabar a volumen moderado?', 'Cuida los oídos y permite oír mejor los detalles', 'Hace que la grabación dure menos', 'Evita que el teléfono se llene de archivos', 'El volumen alto daña la audición y distorsiona los detalles.'),
        ('abc', '{F} ¿Qué meta es coherente con la pauta de ejemplo?', 'Tocar con legato los dos primeros compases dos veces seguidas', 'Tocar más fuerte para que se oiga mejor', 'Cambiar de pieza para evitar la articulación', 'Atiende el criterio más bajo y es medible.'),
        ('abc', 'Un estudiante se pone 3 en todo sin escuchar su grabación. ¿Qué falla?', 'La autoevaluación no se apoya en evidencia', 'La escala debería llegar hasta 5', 'Debía grabar más fuerte', 'Sin escuchar la grabación no existe ninguna evidencia.'),
        ('=', '{F} ¿Cuántos puntos le faltan a la interpretación de ejemplo para llegar al máximo de la pauta?', '12-8', 'El máximo es 12 y la interpretación de ejemplo suma 8.', ' puntos'),
        ('abc', 'Para decidir qué ajustar primero, un criterio importante es', 'cuánto afecta al propósito expresivo', 'cuál es el más fácil de contar', 'cuál usó otro grupo', 'El ajuste debe servir a lo que se quiere expresar.'),
    ],
    ctx=('abc', 'Después de grabarse, una estudiante obtiene pulso 3, afinación 2, articulación 2 y dinámica 1, y quiere transmitir sorpresa. ¿Qué prioriza?', 'La dinámica, para trabajar los contrastes de volumen', 'El pulso, porque tiene 3', 'Ninguno, porque ya está lista', 'La dinámica tiene el menor puntaje y los contrastes apoyan la sorpresa.'),
    sc=[
        ('¿Cuántos puntos suman 3, 3, 2 y 1?', '9', 'Al sumar 3 + 3 + 2 + 1 el resultado es 9.'),
        ('En Música: ¿Qué es una meta medible?', 'Un objetivo pequeño que se puede comprobar', 'Permite saber con claridad si la meta se cumplió.'),
        ('abc', 'Una pauta de autoevaluación sirve para', 'revisar la propia interpretación con criterios claros', 'comparar quién es mejor que quién', 'reemplazar el ensayo', 'Describe lo que se oye y orienta el trabajo.'),
    ],
    op=("Con la {F} como modelo, evalúa una interpretación tuya o de ejemplo con los cuatro criterios (puntaje de 1 a 3 y un compás de evidencia), suma los puntos, elige el criterio prioritario y escribe una meta medible.",
        "Pulso 2 (compás 4 se apura), afinación 3, articulación 2, dinámica 1 (volumen igual todo el tiempo). Suma: 8. Prioridad: dinámica. Meta: hacer crecer el volumen del compás 5 al 8 dos veces seguidas.",
        ["puntajes con evidencia", "suma correcta", "meta medible"], ["pauta completa"], ["no citar evidencia", "meta no medible"],
        "Reconoce la pauta y pide ubicar un compás exacto para cada puntaje."),
    reinforce="Puntúa tres criterios de una canción que cantes y anota una evidencia para cada uno.",
    extend="Compara dos pautas de ensayos distintos y explica qué criterio mejoró más.",
)

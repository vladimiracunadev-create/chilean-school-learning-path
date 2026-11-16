"""Música 3.º y 4.º medio FG: OAC-01 (experimentación con estilos contemporáneos y recursos de producción). Piezas y patrones de ejemplo, inventados; sin audio real."""
from __future__ import annotations

from fg_musi_common import build

O1 = "FG-MUSI-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (tres piezas de ejemplo, inventadas). Pieza A: batería, bajo eléctrico y guitarra con sonido sucio (distorsión); 140 pulsos por minuto; estrofa y estribillo que se repiten; la voz grita en el estribillo. "
     "Pieza B: golpes hechos con una máquina de ritmos y un sintetizador; 120 pulsos por minuto; un patrón de 4 pulsos que se repite sin cambios; no hay voz. "
     "Pieza C: guitarra de cuerdas de nailon y una voz suave; 70 pulsos por minuto; tres estrofas; no hay batería.")
build(
    O1, 1, F,
    use="Aprenderé a reconocer los rasgos audibles que caracterizan a un estilo musical contemporáneo (tempo, timbres, textura, forma y función) y a no confundir un estilo con una sola característica.",
    prior=["Describo pulso, melodía, timbre, textura y forma.", "Distingo un rasgo audible de una opinión.", "Sé que una misma música puede cumplir varias funciones."],
    explain=[
        "Un estilo musical es un conjunto de rasgos que se repiten en muchas obras y que permiten reconocerlas como parientes: el tempo (pulsos por minuto), los timbres que se usan, la textura (cuántas capas suenan a la vez), la forma (cómo se ordenan las partes) y la función (para qué se hace: bailar, escuchar, acompañar una imagen). Un solo rasgo no define un estilo: una pieza rápida no es automáticamente de un estilo en particular.",
        "En la música contemporánea los estilos se mezclan con facilidad. Una fusión toma rasgos de dos o más estilos, por ejemplo el patrón de una máquina de ritmos con una melodía cantada que se parece a una canción tradicional. Para reconocer un estilo conviene escuchar varias veces y anotar rasgos que se puedan comprobar, sin dejarse llevar solo por el nombre que alguien le dio.",
        "Reconocer rasgos es el paso previo a experimentar: antes de cambiar o combinar recursos, hay que saber qué aporta cada uno. Anota siempre el rasgo, el instante donde se oye y el efecto que produce, y deja tu opinión aparte, rotulada como opinión.",
    ],
    vocab=[("estilo", "conjunto de rasgos musicales que se repiten en muchas obras"), ("pulsos por minuto", "medida del tempo: cuántos pulsos suenan en un minuto"), ("fusión", "mezcla de rasgos de dos o más estilos"), ("distorsión", "efecto que vuelve áspero y sucio el sonido de un instrumento eléctrico"), ("sintetizador", "instrumento electrónico que crea sonidos con circuitos o programas"), ("función", "para qué se usa una música")],
    worked=[
        ("Reconocer rasgos en una pieza", "Pieza de ejemplo: bombo y caja marcan un pulso de 100 por minuto, una guitarra repite cuatro notas y una voz habla con ritmo rápido sobre ese fondo. Anota tres rasgos audibles.", ["Tempo: 100 pulsos por minuto, se comprueba contando.", "Timbres: bombo, caja, guitarra y voz hablada.", "Textura: la guitarra repite un patrón y la voz va encima."], "Tempo de 100 ppm; timbres de percusión, guitarra y voz hablada; fondo repetido con voz encima"),
        ("Distinguir un rasgo de un estilo", "Una compañera afirma: «Todo lo que suena a 140 pulsos por minuto es del mismo estilo». ¿Es correcto?", ["Un tempo es un solo rasgo.", "Piezas de estilos muy distintos pueden compartir el mismo tempo.", "Para hablar de estilo hay que mirar tempo, timbres, textura, forma y función juntos."], "No: un solo rasgo no define un estilo"),
    ],
    mistakes=[("Decir que una pieza es de un estilo solo porque es rápida.", "El tempo es uno de varios rasgos y lo comparten estilos muy distintos.", "Revisa al menos tres rasgos antes de concluir."),
              ("Describir con «suena moderna» o «suena rara».", "Son impresiones que otra persona no puede comprobar escuchando.", "Cambia la impresión por un rasgo: «hay un sintetizador y no hay voz».")],
    T=[
        ('abc', '{F} ¿Qué pieza no tiene batería ni instrumentos eléctricos y es la más lenta?', 'Pieza C, que tiene cuerdas de nailon y va a 70 pulsos por minuto', 'Pieza B, porque no tiene voz', 'Pieza A, porque tiene estribillo', 'La C es la única con cuerdas de nailon y voz suave, y su tempo es el menor de las tres.'),
        ('abc', '¿Cuál de estas frases es un rasgo audible?', 'Solo suena una voz cantando, sin ningún otro instrumento que la acompañe', 'Es la música de moda entre estudiantes', 'Fue creada hace pocos años en una ciudad grande', 'Solo la primera se puede comprobar escuchando; las otras son contexto o popularidad.'),
        ('ab', 'Una música que mezcla el patrón de una máquina de ritmos con una melodía de tradición oral es un ejemplo de', 'una fusión de dos estilos', 'una estrofa', 'Una fusión toma rasgos de más de un estilo; una estrofa es solo una parte de la forma de una canción.'),
        ('abc', '{F} ¿Qué pieza combina estrofas y estribillo con una voz que grita?', 'Pieza A', 'Pieza B', 'Pieza C', 'Solo la A tiene estribillo y voz gritada; la B no tiene voz y la C canta suave.'),
        ('=', '{F} La pieza A va a 140 pulsos por minuto y la C a 70. ¿Cuántas veces más rápido es el tempo de A que el de C?', '140//70', 'Se divide el tempo mayor por el menor para comparar cuántas veces cabe.', ' veces'),
        ('abc', '{F} ¿Qué rasgo de la pieza B se relaciona con su función probable de música para bailar?', 'Su patrón de 4 pulsos que se repite sin cambios y es fácil de seguir', 'La ausencia de voz humana', 'El tempo de 120 pulsos por minuto por ser el mayor', 'Un patrón estable y repetido facilita seguir el pulso con el cuerpo; el tempo de B no es el mayor (A tiene 140).'),
        ('abc', 'Dos piezas van a 120 pulsos por minuto. ¿Qué se puede concluir?', 'Que su tempo es igual, pero aún no se sabe si comparten el mismo estilo o los mismos timbres', 'Que son del mismo estilo porque el tempo define el estilo', 'Que suenan igual porque el tempo es lo único que se oye', 'El tempo es un rasgo; faltan timbres, textura, forma y función para hablar de estilo.'),
        ('abc', 'Una estudiante dice: «La pieza es de ese estilo porque me suena parecida». ¿Qué le falta?', 'Citar rasgos audibles que otra persona pueda comprobar al escuchar la pieza', 'Una opinión más fuerte sobre la pieza', 'Compararla solo con una canción que ya conoce', 'Una impresión de parecido no es evidencia; los rasgos sí.'),
        ('abc', '{F} Una banda quiere un sonido entre B y C: ritmo de máquina con voz suave. ¿Qué rasgo de cada pieza toma?', 'La base repetida de B para el ritmo y la voz suave de C para cantar', 'La distorsión de A y la ausencia de voz de B', 'El estribillo de A y los 70 pulsos por minuto de C', 'Toma de B su base rítmica y de C su voz; así mezcla dos estilos.'),
        ('abc', 'Una pieza usa guitarra eléctrica con distorsión a 80 pulsos por minuto. Alguien dice que es del mismo estilo que otra a 80 con guitarra de nailon. ¿Qué error comete?', 'Basa el estilo en un solo rasgo, el tempo, y deja de lado los timbres', 'Cuenta mal los pulsos de cada pieza', 'Confunde guitarra con voz', 'Los timbres difieren mucho, así que igualar el tempo no basta.'),
        ('abc', '{F} Para describir la textura de la pieza A conviene decir:', 'Varias capas suenan a la vez: batería, bajo, guitarra y voz', 'Suena una sola capa, como una voz sin acompañamiento', 'Es una pieza larga con muchas partes diferentes', 'La textura cuenta las capas simultáneas; en A son cuatro.'),
        ('abc', '¿Qué orden conviene seguir para reconocer un estilo?', 'Escuchar, anotar rasgos que se puedan comprobar y recién después clasificar', 'Elegir la etiqueta primero y buscar rasgos', 'Preguntar el nombre del estilo y no escuchar', 'La clasificación debe apoyarse en rasgos anotados, no al revés.'),
        ('abc', '{F} ¿Qué dos rasgos describe la frase «tres estrofas y sin batería» de la pieza C?', 'La forma (las estrofas) y los timbres (sin batería)', 'El tempo y la función de la pieza', 'La textura y el tempo de la pieza', 'Las estrofas describen la forma y la falta de batería describe los timbres.'),
    ],
    ctx=('abc', 'En un taller escolar proponen una fusión. Una pieza de ejemplo tiene patrón de máquina de ritmos y la otra, guitarra y voz en tres estrofas. ¿Qué primera decisión es la más razonable?', 'Anotar qué aporta cada rasgo de las dos piezas antes de decidir cómo mezclarlos', 'Mezclar todo a la vez para ver qué sale', 'Copiar la pieza más famosa y cambiarle el título', 'Primero hay que saber qué aporta cada recurso; mezclar sin criterio no es experimentar.'),
    sc=[
        ('¿Qué es un estilo musical?', 'Un conjunto de rasgos que se repiten en muchas obras', 'Un estilo se reconoce por varios rasgos que se repiten.'),
        ('En Música: ¿Qué es una fusión?', 'La mezcla de rasgos de dos o más estilos', 'Toma y combina elementos de más de un estilo distinto.'),
        ('abc', '¿Cuál es un rasgo audible?', 'Hay un patrón de 4 pulsos que se repite', 'Me parece moderna', 'Es famosa entre jóvenes', 'Solo el patrón repetido se puede comprobar escuchando.'),
    ],
    op=("Con la {F} escribe una ficha para la pieza que elijas: tres rasgos audibles, una función probable y una frase que diga por qué un solo rasgo no basta para nombrar su estilo.",
        "Pieza C: guitarra de nailon y voz suave; tres estrofas; 70 pulsos por minuto. Función probable: acompañar un momento tranquilo. Un solo rasgo no basta porque otras piezas lentas pueden tener timbres y formas distintas.",
        ["tres rasgos comprobables", "función probable", "razona sobre un solo rasgo"], ["ficha breve"], ["usar impresiones como rasgos", "decidir el estilo por el tempo"],
        "Reconoce la ficha y pide cambiar cada impresión por un rasgo."),
    reinforce="Elige una canción de tu lista y anota tres rasgos audibles en líneas separadas de tu opinión.",
    extend="Busca dos canciones con el mismo tempo y muestra con tres rasgos que son de estilos distintos.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (proyecto de ejemplo de un grupo de 4 estudiantes). Recursos disponibles: sus voces; una cajonera de plástico y dos tapas de olla de metal sin filo como objetos sonoros; una guitarra; un teclado con sonidos de piano, cuerdas y bajo; "
     "un teléfono para grabar; un programa de edición con eco, reverberación (efecto de sala grande) y control de volumen. Regla del grupo: el volumen se mantiene bajo para cuidar los oídos.")
build(
    O1, 2, F,
    use="Aprenderé a explorar recursos de producción musical (voz, objetos sonoros, instrumentos y tecnologías) y a elegir cuál conviene según el efecto que quiero lograr y la seguridad del grupo.",
    prior=["Reconozco rasgos de estilos contemporáneos.", "Sé que cada timbre tiene un carácter propio.", "Sé que el volumen alto daña los oídos."],
    explain=[
        "Un recurso de producción es todo lo que se usa para hacer sonar y dar forma a una música. Hay cuatro familias: la voz (cantada, hablada, susurrada), los objetos sonoros (cosas cotidianas que se golpean, frotan o sacuden de forma segura), los instrumentos musicales y las tecnologías (grabar, editar, repetir un fragmento en bucle, añadir efectos como eco o reverberación, y ajustar el volumen de cada capa en la mezcla).",
        "Explorar significa probar un recurso, escuchar el efecto y anotarlo antes de decidir. Un objeto sonoro puede aportar un timbre nuevo, pero hay que revisar que sea seguro: sin bordes filosos, sin piezas pequeñas que se suelten y sin golpes fuertes. Una tecnología tampoco arregla una idea débil: un efecto aplicado a todo vuelve la mezcla confusa.",
        "Al grabar y mezclar, el volumen se mantiene moderado. Si necesitas subirlo para que se oiga una capa, mejor baja otra. Anota qué recurso usaste, con qué fin y qué cambió al oírlo.",
    ],
    vocab=[("recurso de producción", "voz, objeto, instrumento o tecnología usada para hacer música"), ("objeto sonoro", "objeto cotidiano que se usa para producir sonidos de forma segura"), ("bucle", "fragmento grabado que se repite una y otra vez"), ("reverberación", "efecto que da la impresión de un espacio grande, con eco que se apaga"), ("mezcla", "ajuste del volumen y la ubicación de cada capa de sonido")],
    worked=[
        ("Elegir un recurso según el efecto", "El grupo quiere un sonido seco y corto que marque cada pulso. ¿Qué recurso de la ficha conviene probar y por qué?", ["Hay que buscar un sonido de ataque rápido y poca duración.", "La cajonera golpeada suena seca y corta.", "La reverberación alargaría el sonido, lo contrario de lo buscado."], "La cajonera, porque su golpe es seco y corto; no usar reverberación"),
        ("Detectar un problema de mezcla", "En la grabación de ejemplo, la voz casi no se oye porque la guitarra y el teclado suenan muy fuertes. ¿Cuál es la mejor decisión?", ["No conviene subir todo el volumen: puede dañar los oídos.", "Se baja el volumen de guitarra y teclado para dejar espacio a la voz.", "Luego se vuelve a escuchar para comprobar."], "Bajar guitarra y teclado y volver a escuchar"),
    ],
    mistakes=[("Subir el volumen general para que se oiga todo.", "Daña los oídos y no corrige el desequilibrio entre capas.", "Baja las capas que tapan y escucha otra vez."),
              ("Aplicar eco o reverberación a todas las pistas.", "Se pierde claridad y todo suena igual.", "Elige una o dos pistas donde el efecto tenga una razón.")],
    T=[
        ('abc', '{F} ¿Cuál de estos recursos es un objeto sonoro?', 'Las tapas de olla de metal sin filo', 'El teclado con sonido de cuerdas', 'El programa de edición', 'Un objeto sonoro es una cosa cotidiana usada de forma segura para hacer sonar.'),
        ('abc', '¿Qué hace la reverberación?', 'Da la impresión de un espacio grande, con un eco que se apaga', 'Acelera el pulso de toda la pieza', 'Cambia la voz por la de un instrumento', 'Es un efecto de sala; no modifica el tempo ni cambia las voces.'),
        ('ab', '{F} Si una capa no se oye, la mejor decisión es', 'bajar el volumen de las capas que la tapan', 'subir el volumen de todo', 'Subir todo el volumen daña los oídos y no corrige el equilibrio.'),
        ('abc', '{F} El grupo quiere un fondo continuo y suave. ¿Qué recurso del teclado le sirve?', 'El sonido de cuerdas tocando notas largas y sostenidas', 'Un golpe seco en la cajonera repetido', 'Las tapas de olla chocando con fuerza', 'Las notas largas de cuerdas dan continuidad; los golpes secos son cortos.'),
        ('abc', 'Un estudiante propone usar un frasco de vidrio como objeto sonoro. ¿Qué respuesta es la más adecuada?', 'Descartarlo y elegir un objeto de plástico o madera sin bordes filosos', 'Usarlo, pero golpearlo muy despacio', 'Usarlo con las manos protegidas por un trapo', 'El vidrio puede romperse y cortar; hay alternativas seguras, así que no se arriesga.'),
        ('abc', '{F} El grupo graba una vez la cajonera y repite ese fragmento sin parar. ¿Qué técnica usó?', 'Un bucle, que repite un fragmento grabado', 'Una fusión de estilos', 'Una reverberación', 'Repetir un fragmento grabado se llama bucle.'),
        ('abc', 'Un grupo aplica eco a todas las pistas y la mezcla se ve confusa. ¿Qué conviene hacer?', 'Dejar el eco solo en una o dos pistas con una razón clara', 'Agregar más eco para que el efecto se note más', 'Quitar todas las pistas y partir con la voz sola', 'Menos efectos, con intención, devuelven la claridad.'),
        ('abc', '{F} ¿Qué decisión explica mejor el uso de la voz susurrada en una estrofa?', 'Crea cercanía y contrasta con un estribillo más fuerte', 'Es obligatoria en toda música contemporánea', 'Sirve para tapar la guitarra', 'Un susurro cambia el timbre y puede contrastar con otra parte.'),
        ('abc', 'Para explorar un recurso nuevo, ¿qué orden es el más útil?', 'Probarlo, escuchar el efecto y anotarlo antes de decidir', 'Decidir su uso antes de probarlo', 'Usarlo en toda la pieza y anotar si falla', 'Explorar es probar, escuchar y registrar antes de decidir.'),
        ('abc', '{F} La regla del grupo es mantener el volumen bajo. ¿Qué objetivo cumple?', 'Cuidar la audición de todas las personas del equipo mientras graban', 'Evitar que se escuche la voz', 'Reducir el número de instrumentos', 'El volumen bajo protege la audición.'),
        ('abc', 'Una compañera dice que la tecnología es mejor que los objetos sonoros. ¿Qué respuesta es más acertada?', 'Cada recurso aporta algo distinto; se elige según el efecto buscado', 'Sí, porque lo digital siempre suena más profesional', 'No, porque la tecnología arruina cualquier sonido natural', 'Ninguna familia de recursos es mejor en general; depende del propósito.'),
        ('abc', '{F} El grupo quiere sonar «como una sala grande». ¿Qué recurso tecnológico elige?', 'La reverberación, que imita un espacio amplio', 'Un cambio de tempo a 200 pulsos por minuto', 'Duplicar el volumen de la voz', 'La reverberación imita el sonido de un espacio amplio.'),
        ('abc', 'Antes de decidir un efecto, ¿qué dato conviene anotar?', 'El recurso, su fin y lo que cambió al oírlo', 'Solo el nombre del programa usado', 'La opinión de quien no escuchó la prueba', 'La bitácora debe reunir recurso, intención y efecto.'),
    ],
    ctx=('abc', 'Un grupo escolar prepara un fragmento de 8 pulsos con la cajonera, la voz y un bucle. En el ensayo la voz se pierde. ¿Qué decisión es la más razonable?', 'Bajar el volumen de la cajonera y del bucle, y volver a probar', 'Subir todo el volumen hasta oírla', 'Quitar la voz porque cuesta mezclarla', 'Se equilibran las capas sin subir el volumen general.'),
    sc=[
        ('¿Qué es un bucle?', 'Un fragmento grabado que se repite', 'Se repite en forma continua para formar una base sonora.'),
        ('Nombra las cuatro familias de recursos de producción de la clase.', 'Voz, objetos sonoros, instrumentos y tecnologías', 'Son las cuatro familias de recursos que explica esta clase.'),
        ('abc', '¿Qué conviene hacer cuando una pista tapa a otra?', 'Bajar la que tapa y volver a escuchar', 'Subir el volumen de todas las pistas', 'Aplicarles más reverberación', 'Se corrige el equilibrio entre capas sin dañar los oídos.'),
    ],
    op=("Con la {F} arma un plan de sonido para una pieza de 8 pulsos: elige un recurso para el pulso, uno para el fondo y uno para el efecto final, y explica en una frase por qué cada uno.",
        "Pulso: cajonera, porque su golpe es seco. Fondo: teclado con cuerdas, porque las notas largas dan continuidad. Final: reverberación, porque alarga el cierre. Volumen bajo en todo.",
        ["tres recursos elegidos", "justificación breve", "volumen seguro"], ["plan de sonido"], ["usar un recurso sin razón", "olvidar el volumen seguro"],
        "Reconoce el plan y pide explicar el efecto que espera en cada elección."),
    reinforce="Haz una lista de cinco objetos seguros de tu casa y describe cómo suena cada uno, sin golpear fuerte.",
    extend="Compara en dos frases cómo cambia una melodía cuando se canta con la voz sola y cuando se acompaña con un bucle.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (prueba de ejemplo). Un grupo escribe un patrón de 8 pulsos: «X . X X . X . .» donde X es un golpe y el punto es silencio. "
     "Versión 1: 120 pulsos por minuto, golpes con caja de madera. Versión 2: mismo patrón, 80 pulsos por minuto, golpes con tapa de olla de metal sin filo. "
     "Solo cambió el tempo y el timbre; el patrón es idéntico.")
build(
    O1, 3, F,
    use="Aprenderé a ensayar una decisión musical: cambiar una sola variable, comparar versiones y explicar el efecto, en vez de imitar un estilo sin decidir nada.",
    prior=["Reconozco rasgos de estilos y recursos de producción.", "Cuento pulsos en un patrón.", "Sé anotar un patrón con X y puntos."],
    explain=[
        "Experimentar no es imitar ni hacer cambios al azar. Una decisión musical se ensaya cambiando una variable a la vez (el tempo, el timbre, el orden de los golpes, un efecto) y manteniendo el resto igual. Así, si la música cambia, sabes cuál fue la causa. Se anotan dos versiones, se escuchan, y se describe el efecto con rasgos comprobables.",
        "Un patrón de 8 pulsos se lee contando: cada posición es un pulso, X es un golpe y el punto es silencio. El patrón «X . X X . X . .» tiene cuatro golpes en ocho pulsos. Si el tempo es 120 pulsos por minuto, cada minuto tiene 120 pulsos; 8 pulsos duran 8 × 60 ÷ 120 = 4 segundos.",
        "Imitar sin decidir es copiar rasgos de un estilo sin preguntarse qué efecto buscas. Decidir es elegir un cambio, probarlo, compararlo con la versión anterior y quedarte con lo que sirve a tu intención. También es válido conservar la versión original si el cambio no mejora.",
    ],
    vocab=[("variable", "aspecto de la música que se puede cambiar: tempo, timbre, orden de los golpes, efecto"), ("versión", "prueba completa de una idea musical, para compararla con otra"), ("patrón", "secuencia de golpes y silencios que se repite"), ("silencio", "pulso en que no suena nada, marcado con un punto"), ("decisión musical", "elección de un cambio con una intención y un efecto comprobado")],
    worked=[
        ("Contar un patrón", "Cuenta los golpes y los silencios del patrón «X X . X . . X .».", ["Posiciones: 1 X, 2 X, 3 punto, 4 X, 5 punto, 6 punto, 7 X, 8 punto.", "Golpes: posiciones 1, 2, 4 y 7 = 4 golpes.", "Silencios: 3, 5, 6 y 8 = 4 silencios."], "4 golpes y 4 silencios"),
        ("Calcular una duración", "A 60 pulsos por minuto suena un pulso por segundo. ¿Cuánto duran 8 pulsos?", ["Un pulso por segundo.", "8 pulsos × 1 segundo = 8 segundos."], "8 segundos"),
    ],
    mistakes=[("Cambiar tempo, timbre y orden de golpes a la vez y concluir que «quedó mejor».", "No se sabe cuál cambio produjo el efecto.", "Cambia una variable por prueba y compara."),
              ("Contar los silencios como si no ocuparan tiempo.", "Cada punto es un pulso que dura lo mismo que un golpe.", "Cuenta todas las posiciones, con X o con punto.")],
    T=[
        ('=', '{F} ¿Cuántos golpes (X) tiene el patrón de 8 pulsos?', '4', 'Se cuentan las X en las ocho posiciones; los puntos son silencios.', ' golpes'),
        ('abc', '{F} ¿Qué variable cambia entre la versión 1 y la 2, además del tempo?', 'El timbre: caja de madera en la versión 1 y tapa de metal en la 2', 'El orden de los golpes', 'La cantidad de pulsos del patrón', 'El patrón es idéntico; cambian la caja de madera por la tapa de metal.'),
        ('ab', '¿Qué significa un punto en un patrón rítmico escrito con X y puntos?', 'Un pulso en que no suena nada', 'Un golpe muy suave', 'El punto es un silencio que ocupa el mismo tiempo que un golpe.'),
        ('=', '{F} A 120 pulsos por minuto, ¿cuántos segundos dura el patrón de 8 pulsos?', '8*60//120', 'Se multiplican los pulsos por 60 segundos y se divide por los pulsos por minuto.', ' segundos'),
        ('=', '{F} A 80 pulsos por minuto, ¿cuántos segundos duran 4 repeticiones del patrón de 8 pulsos? (32 pulsos en total)', '32*60//80', 'Son 32 pulsos; se multiplican por 60 y se divide por 80.', ' segundos'),
        ('abc', '{F} ¿Por qué es útil cambiar solo una variable entre versiones?', 'Porque así se sabe con certeza qué cambio produjo el efecto que se oye', 'Porque en música está prohibido cambiar varias', 'Porque así se termina más rápido la prueba', 'Con un solo cambio la causa del efecto es clara.'),
        ('abc', 'Un grupo copia el sonido de un estilo famoso sin preguntarse qué efecto busca. ¿Cómo se llama ese error?', 'Imitar un estilo sin decidir un efecto propio', 'Fusionar con criterio', 'Mezclar con equilibrio', 'Copiar sin una intención es imitar sin decidir.'),
        ('abc', '{F} La versión 2 suena más pesada y calmada. ¿Cuál es una explicación apoyada en la ficha?', 'El tempo es menor y el timbre es de metal', 'El patrón de golpes es distinto', 'Se agregaron más golpes en el pulso 8', 'Solo cambiaron tempo y timbre; el patrón es idéntico.'),
        ('abc', 'Un grupo cambia el timbre y el orden de golpes y dice que el timbre mejoró la música. ¿Qué falla en su razonamiento?', 'No puede separar el efecto del timbre del efecto del orden', 'No tiene derecho a opinar sin partitura', 'Confunde el silencio con un pulso', 'Al cambiar dos variables a la vez no se sabe cuál causó el efecto.'),
        ('abc', '{F} Quieren probar un patrón nuevo: «X X . . X . X .». ¿Cuántos silencios tiene?', '4', '3', '5', 'Posiciones 3, 4, 6 y 8 son silencios: 4.'),
        ('abc', '{F} ¿Qué prueba es una buena decisión si quieren saber si la caja de madera suena más clara que la tapa?', 'Tocar el mismo patrón al mismo tempo con cada una y comparar', 'Tocar con la caja un patrón y con la tapa otro más rápido', 'Escuchar solo la caja varias veces seguidas', 'Se iguala todo menos el timbre para aislar el efecto.'),
        ('abc', 'Después de probar, el grupo prefiere la versión original. ¿Qué conclusión es válida?', 'Conservar la original es una decisión legítima si el cambio no sirve a la intención', 'La prueba fracasó, así que no hubo aprendizaje', 'Hay que cambiar algo igual porque experimentar obliga a cambiar', 'Experimentar incluye descartar cambios que no mejoran.'),
        ('abc', 'Para registrar una prueba, ¿qué anotación es suficiente?', 'Variable cambiada, versión A y B, y efecto oído', 'Solo «me gustó más la B»', 'Solo el nombre del estilo imitado', 'La anotación debe permitir repetir la prueba y ver el efecto.'),
    ],
    ctx=('abc', 'Un grupo tiene el patrón «X . X X . X . .» y quiere un final más tenso. Prueban lo mismo a 120 y a 160 pulsos por minuto. ¿Qué variable están ensayando?', 'El tempo: la rapidez del pulso, que pasa de 120 a 160 por minuto', 'El timbre de los instrumentos', 'El orden de los golpes', 'Solo cambia la rapidez del pulso; el patrón y el timbre se mantienen iguales.'),
    sc=[
        ('¿Cuántas variables conviene cambiar por prueba?', 'Una', 'Así se puede identificar la causa del efecto oído.'),
        ('¿Qué es «imitar sin decidir»?', 'Copiar rasgos de un estilo sin elegir un efecto propio', 'Le faltan una intención propia y una comparación de versiones.'),
        ('abc', '¿Cuántos segundos duran 4 pulsos a 60 pulsos por minuto?', '4 segundos, porque a 60 pulsos por minuto cada pulso dura 1 segundo', '60 segundos, porque es un minuto', '15 segundos, porque divide 60 entre 4', 'A 60 pulsos por minuto cada pulso dura 1 segundo, así que 4 pulsos duran 4.'),
    ],
    op=("Con la {F} escribe un patrón nuevo de 8 pulsos con X y puntos, elige una sola variable para cambiar entre dos versiones y anota en tres líneas: la variable, qué esperas oír y qué cuenta como evidencia.",
        "Patrón: «X . X . X X . .» (4 golpes). Variable: tempo, 100 y 140 pulsos por minuto. Espero que 140 suene más enérgico. Evidencia: comparar la sensación de energía y el tiempo que dura el patrón.",
        ["patrón de 8 pulsos", "una sola variable", "evidencia anotada"], ["dos versiones comparadas"], ["cambiar varias variables", "contar mal los pulsos"],
        "Reconoce el patrón y pide aclarar qué se mantiene igual en ambas versiones."),
    reinforce="Escribe tres patrones de 8 pulsos con 3, 4 y 5 golpes, y cuenta los silencios de cada uno.",
    extend="Prepara una prueba de dos versiones que cambie solo el timbre y anota qué rasgo esperas que cambie.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (idea de fusión de ejemplo). Estilo 1: un ritmo marcado de 4 pulsos con golpes en los pulsos 1 y 3 (patrón «X . X .»). "
     "Estilo 2: una melodía cantada de 4 frases de 4 pulsos cada una, que sube en la frase 2 y baja en la frase 4. "
     "Propósito de la fusión: música para abrir un acto escolar, de unos 32 pulsos, con ambiente de bienvenida. Recursos: dos voces, la cajonera, un teclado y un bucle.")
build(
    O1, 4, F,
    use="Aprenderé a crear y analizar una fusión breve de dos estilos con recursos de producción: elegir qué toma de cada estilo, ordenar las partes y justificar las decisiones con evidencia audible.",
    prior=["Reconozco rasgos de estilos.", "Exploro recursos de producción y los cuido.", "Ensayo cambiando una variable por prueba."],
    explain=[
        "Crear una fusión comienza con un propósito: ¿para qué es esta música? Con él se decide qué rasgo se toma de cada estilo. Por ejemplo, de un estilo se toma la base rítmica, que sostiene el pulso, y del otro la melodía cantada, que lleva la idea. Luego se ordenan las partes (forma) y se elige quién toca cada capa para que no se tapen.",
        "Una forma sencilla de fusión de 32 pulsos es: introducción de 8 pulsos con solo el ritmo, parte A de 16 pulsos con ritmo y melodía, y cierre de 8 pulsos con el bucle que se apaga. Para comprobarla se suman las partes: 8 + 16 + 8 = 32. Si sobran o faltan pulsos, hay que ajustar.",
        "Para analizar la fusión se usan conceptos de la disciplina: qué rasgo viene de cada estilo, qué efecto produce y si respeta el propósito. Una fusión lograda no solo mezcla: cada rasgo cumple una función. Reconoce también los límites: qué no pudiste probar o qué quedó confuso.",
    ],
    vocab=[("base rítmica", "capa de percusión o bajo que sostiene el pulso"), ("introducción", "parte inicial que prepara lo que viene"), ("propósito", "intención con que se crea la música"), ("cierre", "parte final que concluye la pieza"), ("función de un rasgo", "para qué sirve ese rasgo dentro de la pieza")],
    worked=[
        ("Armar la forma", "Quieren 32 pulsos: introducción de 8 pulsos y cierre de 8 pulsos. ¿Cuántos pulsos tiene la parte central?", ["Total: 32 pulsos.", "Introducción y cierre: 8 + 8 = 16 pulsos.", "Parte central: 32 − 16 = 16 pulsos."], "16 pulsos"),
        ("Justificar una decisión", "¿Por qué conviene que el ritmo de golpes en 1 y 3 sea la base de la fusión de la ficha?", ["Es estable y fácil de seguir.", "Deja espacio para que la melodía de cuatro frases se escuche.", "Ayuda a que el público sienta el pulso de bienvenida."], "Sostiene el pulso y deja lugar a la melodía"),
    ],
    mistakes=[("Poner todos los recursos a sonar desde el primer pulso.", "Las capas se tapan y se pierde el contraste.", "Entra de a poco: primero el ritmo, luego la melodía."),
              ("Defender la fusión solo con «quedó bien».", "No se pueden comprobar ni el rasgo ni el efecto.", "Cita qué viene de cada estilo y qué efecto produce.")],
    T=[
        ('=', '{F} La fusión dura 32 pulsos con introducción de 8, parte A de 16 y cierre. ¿Cuántos pulsos tiene el cierre?', '32-8-16', 'Se restan introducción y parte A del total de pulsos.', ' pulsos'),
        ('abc', '{F} ¿Qué rasgo toma la fusión del estilo 1?', 'La base rítmica con golpes en los pulsos 1 y 3', 'La melodía de cuatro frases', 'El uso de la voz sola sin ritmo', 'El patrón «X . X .» pertenece al estilo 1.'),
        ('abc', '¿Qué se decide primero al crear una fusión?', 'El propósito: para qué se va a usar esa música', 'El número de instrumentos que habrá', 'El título que tendrá en una plataforma', 'El propósito orienta qué rasgos tomar.'),
        ('=', '{F} En el patrón «X . X .», ¿cuántos golpes hay en 4 repeticiones seguidas?', '2*4', 'Cada repetición tiene 2 golpes y se repite 4 veces.', ' golpes'),
        ('abc', '{F} ¿En qué pulso de una repetición del patrón de 4 pulsos suena el segundo golpe?', 'En el pulso 3 de cada repetición', 'En el pulso 2 de cada repetición', 'En el pulso 4', 'El patrón «X . X .» tiene golpes en las posiciones 1 y 3.'),
        ('abc', '{F} ¿Qué parte de la forma es más razonable para el bucle que se apaga?', 'El cierre, porque un bucle que se apaga termina', 'La introducción, porque prepara lo que viene', 'La frase 2 de la melodía, que sube en la mitad', 'Un bucle que se apaga sirve para terminar la pieza.'),
        ('abc', '{F} La melodía cantada tiene 4 frases de 4 pulsos. ¿Cuántos pulsos ocupa toda la melodía?', '16', '8', '32', 'Son 4 frases por 4 pulsos cada una: 16 pulsos, lo que cabe en la parte A.'),
        ('abc', 'Un grupo escribe: «Tomamos la base rítmica del estilo 1 porque sostiene el pulso y deja espacio a la melodía». ¿Qué tiene esa frase?', 'Un rasgo, de qué estilo viene y para qué sirve', 'Solo una opinión sobre la fusión', 'Solo un dato histórico', 'Indica qué rasgo, de dónde viene y para qué sirve.'),
        ('abc', '{F} En la parte A suenan juntos ritmo, melodía y bucle, y no se oye la voz. ¿Qué decisión de mezcla es mejor?', 'Bajar el volumen del bucle y el ritmo para dejar la voz', 'Subir el volumen de todo para que la voz se note', 'Quitar la melodía porque es la capa más débil', 'Se equilibran las capas sin subir el volumen general.'),
        ('abc', '{F} Una compañera propone gritar el estribillo y subir mucho el volumen. ¿Con qué dato de la ficha se comprueba si esa idea sirve?', 'Con el propósito: dar la bienvenida en un acto escolar', 'Con que la melodía sube en la frase 2', 'Con que la cajonera suena en los pulsos 1 y 3', 'Toda decisión se compara con el propósito; una música de bienvenida pide un ambiente acogedor y un volumen moderado.'),
        ('abc', '¿Qué es una función de un rasgo dentro de una pieza?', 'Lo que ese rasgo aporta, es decir, para qué sirve dentro de la pieza', 'La fecha en que se creó el rasgo', 'El volumen con que se toca el rasgo', 'La función explica la utilidad del rasgo.'),
        ('abc', '{F} Si la parte central pasara a 12 pulsos y se mantiene la introducción de 8, ¿cuántos pulsos debe tener el cierre para llegar a 32?', '12', '8', '16', '32 − 8 − 12 = 12.'),
        ('abc', 'Para reconocer un límite de la fusión, ¿qué frase sirve?', 'No alcanzamos a probar un segundo timbre para el bucle', 'La fusión quedó perfecta y no cambiaría nada', 'A nadie le gustó, así que fracasó', 'Un límite es lo que falta probar o resolver, dicho con claridad.'),
    ],
    ctx=('abc', 'Un grupo debe presentar una fusión de 32 pulsos en un acto, pero la forma que ensayó suma 40 pulsos. ¿Qué ajuste es el más sensato?', 'Acortar partes hasta que la forma sume 32 pulsos, por ejemplo el cierre', 'Subir el volumen para compensar', 'Repetir toda la pieza dos veces seguidas', 'La forma debe sumar los pulsos previstos.'),
    sc=[
        ('¿Qué es la base rítmica?', 'La capa de percusión o bajo que sostiene el pulso', 'Es la capa que mantiene el pulso estable para las demás.'),
        ('Si una introducción tiene 8 pulsos y un cierre 8, ¿cuántos pulsos quedan para la parte central en una pieza de 32?', '16', 'Al restar 8 y 8 de 32 quedan 16 pulsos.'),
        ('abc', '¿Qué hace que una fusión sea lograda?', 'Cada rasgo tomado cumple una función', 'Tiene la mayor cantidad de estilos mezclados', 'Suena muy fuerte', 'Un rasgo que no cumple una función no aporta a la pieza.'),
    ],
    op=("Con la {F} crea la forma de una fusión de 32 pulsos con tres partes, anota los pulsos de cada una (deben sumar 32) y justifica en una frase qué rasgo de cada estilo usas y para qué.",
        "Introducción 8 pulsos (solo ritmo), parte A 16 (ritmo y melodía), cierre 8 (bucle que se apaga). 8 + 16 + 8 = 32. Del estilo 1 uso el ritmo para sostener el pulso; del estilo 2, la melodía para llevar la idea.",
        ["tres partes que suman 32", "rasgo de cada estilo", "función"], ["forma y justificación"], ["pulsos que no suman", "no explicar la función"],
        "Reconoce la forma y pide comprobar la suma de los pulsos."),
    reinforce="Escribe una forma de 24 pulsos con tres partes distintas y comprueba que suman 24.",
    extend="Elige dos canciones muy distintas que conozcas y propone qué rasgo de cada una usarías en una fusión y para qué.",
)

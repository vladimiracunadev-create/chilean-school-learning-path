"""Lengua y Literatura EPJA Media Nivel 1, módulo 4 (parte 4): OAD-16, analizar los puntos de vista de un texto audiovisual (imagen, texto y sonido) y comunicar conclusiones oralmente. Todo el material audiovisual es inventado y se entrega DESCRITO en tablas escritas: no hay audio ni video."""
from __future__ import annotations

from epja_leli_nm1_d_common import build

O = "EPJA-LELI-NM1-OAD-16"

F1 = ("Aviso audiovisual (inventado y descrito por escrito), «Panadería del pasaje», 3 escenas. "
      "Escena 1: Imagen: plano general de una calle con luz de amanecer. Texto en pantalla: «Cada mañana». Sonido: guitarra suave. "
      "Escena 2: Imagen: primer plano de unas manos amasando. Voz en off: «Hecho a mano». Sonido: el sonido de la masa al golpear la mesa. "
      "Escena 3: Imagen: una familia riendo alrededor de una mesa con pan. Texto en pantalla: «Pan para todos». Sonido: risas y la música sube.")

F2 = ("Reportaje (inventado y descrito por escrito), «Cierra la feria de la plaza», 3 escenas. "
      "Escena 1: Imagen: plano general de la feria vacía, con sillas apiladas. Texto en pantalla: «Cierra la feria de la plaza». Sonido: viento y música lenta. "
      "Escena 2: Imagen: primer plano de una vendedora con los ojos húmedos. Voz en off: «Cuarenta familias pierden su sustento». Sonido: silencio y luego un violín. "
      "Escena 3: Imagen: plano general de un edificio municipal cerrado con rejas. Texto en pantalla: «Sin respuestas». Sonido: un golpe seco. "
      "Datos de apoyo: un plano general muestra el lugar completo; un primer plano muestra de cerca un rostro u objeto; la voz en off se oye sin que se vea a quien habla.")

F3 = ("Campaña de seguridad (inventada y descrita por escrito), «En esta obra, primero la seguridad», 3 escenas. "
      "Escena 1: Imagen: plano general de una obra de construcción donde los trabajadores no llevan casco. Voz en off: «En esta empresa, la seguridad es lo primero». Sonido: música alegre. "
      "Escena 2: Imagen: primer plano de un casco colgado de un clavo. Texto en pantalla: «Usa tu casco». Sonido: golpes de martillo. "
      "Escena 3: Imagen: un trabajador con casco sonriendo. Texto en pantalla: «Cuídate». Sonido: la música sube. "
      "Pasos del análisis: 1) leer la tabla escena por escena; 2) anotar imagen, texto y sonido; 3) preguntar qué sugiere cada uno; 4) ver si se refuerzan o se contradicen; 5) formular el punto de vista.")

F4 = ("Reportaje A (inventado y descrito por escrito), canal municipal, «Avanzan las obras», 2 escenas. "
      "Escena 1: Imagen: plano general de máquinas trabajando bajo un cielo despejado. Voz en off: «Avanzan las obras que mejorarán el barrio». Sonido: marcha alegre. "
      "Escena 2: Imagen: plano de una maqueta con la avenida terminada. Texto en pantalla: «Listo en seis meses». Sonido: aplausos. "
      "Reportaje B (inventado y descrito por escrito), canal de los comerciantes, «Ventas a la baja», 2 escenas. "
      "Escena 1: Imagen: primer plano de un local con mercadería sin vender. Voz en off: «Comerciantes aseguran que las ventas bajaron». Sonido: ruido de tráfico. "
      "Escena 2: Imagen: plano general de una avenida con zanjas y poco público. Texto en pantalla: «Cuándo termina». Sonido: silencio. "
      "Dato de apoyo: ambos reportajes hablan de las mismas obras en la misma avenida.")

F5 = ("Video (inventado y descrito por escrito), «Reciclar en el edificio», 3 escenas. "
      "Escena 1: Imagen: primer plano de un contenedor de basura desbordado. Voz en off: «Cada semana, más residuos». Sonido: moscas. "
      "Escena 2: Imagen: plano general de vecinos separando botellas y cartones en el patio. Texto en pantalla: «Juntos sí se puede». Sonido: música animada. "
      "Escena 3: Imagen: un letrero con las instrucciones para separar. Texto en pantalla: «Botellas, cartones y latas». Sonido: silencio. "
      "Exposición A (inventada): «El video muestra residuos y vecinos que reciclan. Me gustó. Fin». "
      "Exposición B (inventada): «El video quiere que los vecinos reciclen. Lo hace con una imagen de basura desbordada y la frase “más residuos”, y con vecinos reunidos y música animada. Pienso que muestra bien el problema, pero no explica cómo se retira lo reciclado. Por eso necesito más información antes de apoyarlo del todo». "
      "Exposición C (inventada): «Todos deberían reciclar, es obvio. Los que no reciclan son flojos».")

F6 = ("Noticia (inventada y descrita por escrito), «Nuevo horario de buses», 3 escenas. "
      "Escena 1: Imagen: primer plano de una persona esperando bajo la lluvia. Voz en off: «Nuevo horario de buses: más esperas». Sonido: lluvia y música triste. "
      "Escena 2: Imagen: plano general de un bus lleno. Texto en pantalla: «Pasajeros molestos». Sonido: bocinas. "
      "Escena 3: Imagen: entrevista a una pasajera que dice: «Antes pasaba cada diez minutos, ahora cada veinte». Texto en pantalla: «Pasajera, caso de ejemplo». Sonido: ruido de calle. "
      "Nota: la noticia no muestra la versión de la empresa de buses.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya veo a diario, avisos, noticias y videos del celular, para reconocer que imagen, texto y sonido comunican juntos.",
    prior=["Veo avisos y noticias en televisión o en el celular.", "Sé que la música cambia cómo me siento.", "Puedo decir qué mensaje me dejó un aviso."],
    explain=[
        "Tú ya conoces los textos audiovisuales: un aviso, una noticia, un video. Un texto audiovisual comunica con tres cosas a la vez: la imagen (lo que se ve), el texto (las palabras escritas o dichas) y el sonido (música, ruidos, voces, silencio).",
        "Cada parte aporta algo. La imagen muestra, el texto explica o nombra y el sonido crea un ambiente. Si quitas el sonido de un aviso, cambia lo que sientes, aunque veas las mismas imágenes. Por eso hay que mirar las tres partes juntas.",
        "Todo texto audiovisual tiene un punto de vista: es la mirada desde la que alguien cuenta algo. Quien lo hace elige qué mostrar, qué decir y qué música poner. Hoy aprendemos a leer esas elecciones en una tabla escrita, porque aquí no hay video ni audio.",
    ],
    vocab=[("texto audiovisual", "mensaje que combina imagen, texto y sonido"), ("escena", "parte de un video donde ocurre una situación"), ("voz en off", "voz que se oye sin que se vea a quien habla"), ("punto de vista", "mirada desde la que alguien cuenta algo")],
    worked=[
        ("Separar imagen, texto y sonido", "Escena 2 del aviso: manos amasando; voz «Hecho a mano»; sonido de la masa al golpear la mesa.", ["Imagen: primer plano de manos amasando.", "Texto: voz en off que dice «Hecho a mano».", "Sonido: golpes de la masa."], "Imagen muestra el trabajo, texto lo nombra y sonido lo hace cercano"),
        ("Descubrir el punto de vista", "Aviso: amanecer, manos, familia riendo, «Pan para todos».", ["Elige mostrar lo cálido y familiar.", "No muestra precios ni comparaciones."], "La panadería se muestra como cálida y familiar"),
    ],
    mistakes=[("Mirar solo las imágenes y olvidar el sonido.", "El sonido también crea sentido: música, silencio o ruidos.", "Anota siempre imagen, texto y sonido de cada escena."),
              ("Creer que un aviso «solo muestra la realidad».", "Quien lo hace elige qué mostrar y qué no.", "Pregunta: «¿qué eligieron mostrar y qué dejaron fuera?».")],
    T=[
        ("abc", "{F} ¿Qué muestra la imagen de la escena 2?", "Un primer plano de unas manos amasando", "Una calle con luz de amanecer", "Una familia riendo", "La tabla indica un primer plano de manos amasando."),
        ("{F} ¿Cuántas escenas tiene el aviso? Escribe el número.", "3", "La tabla del texto describe tres escenas numeradas."),
        ("abc", "{F} ¿Qué texto aparece en pantalla en la escena 3?", "«Pan para todos»", "«Hecho a mano»", "«Cada mañana»", "La escena 3 muestra la frase «Pan para todos»."),
        ("abc", "{F} ¿Qué sonido acompaña la escena 1?", "Guitarra suave", "Risas", "Golpes de martillo", "La tabla de la escena 1 anota guitarra suave."),
        ("abc", "{F} ¿Qué sensación crea la luz de amanecer con la guitarra suave?", "Calma y calidez", "Peligro", "Prisa", "La luz suave y la música tranquila crean un ambiente cálido."),
        ("ab", "{F} ¿Qué quiere sugerir la imagen de la familia riendo con el pan?", "Que el pan se comparte y se disfruta en familia", "Que el pan es el más barato", "Muestra un momento familiar y no entrega ningún dato de precio."),
        ("abc", "En Lengua y Literatura: ¿qué es un texto audiovisual?", "Un mensaje que combina imagen, texto y sonido", "Un texto solo con palabras", "Un dibujo sin sonido", "Combina tres formas de comunicar a la vez."),
        ("abc", "{F} ¿Qué frase da una información concreta sobre cómo se hace el pan?", "«Hecho a mano»", "«Cada mañana»", "«Pan para todos»", "La voz en off señala cómo se elabora el pan."),
        ("{F} ¿El aviso informa el precio del pan? Responde sí o no.", "no", "Las tres escenas no mencionan ningún precio."),
        ("abc", "{F} ¿Cuál es el punto de vista del aviso?", "La panadería se muestra como cálida y familiar", "El pan es más caro que en otras partes", "La panadería tiene problemas", "Elige mostrar escenas de familia, manos y amanecer."),
        ("ab", "{F} Un vecino dice: «El aviso demuestra que este pan es mejor que los otros». ¿Tiene razón?", "No: el aviso muestra sensaciones y no compara con otros panes", "Sí: aparece una familia feliz", "Ninguna escena compara este pan con otro producto."),
        ("abc", "{F} Si se apaga el sonido del aviso, ¿qué cambia?", "Se pierden la música y el sonido de la masa, que crean el ambiente", "Se pierden las imágenes", "Se pierde el texto escrito", "El sonido aporta emoción que no está en la imagen."),
        ("abc", "¿En cuál de estos lugares ves un texto audiovisual?", "En un noticiero de televisión", "En un cuaderno de cuentas", "En una boleta de compra", "El noticiero combina imágenes, voz y música."),
    ],
    ctx=("abc", "Ves un aviso de un banco de barrio con música emotiva y una familia sonriente, sin nombrar costos. Quieres decidir si te conviene. ¿Qué haces?", "Reconozco que muestra sentimientos y pido la información concreta", "Confío porque la música es linda", "Lo comparto sin leer", "Un aviso emotivo no entrega datos concretos que se puedan comparar."),
    sc=[("En Lengua y Literatura: ¿qué tres partes tiene un texto audiovisual?", "Imagen, texto y sonido", "Se analizan juntas para entender el mensaje."),
        ("¿Qué es el punto de vista de un video?", "La mirada desde la que se cuenta algo", "Es lo que quien lo hace elige mostrar."),
        ("¿Qué aporta el sonido?", "Crea un ambiente y una emoción", "Música y ruidos cambian cómo sentimos lo que vemos.")],
    op=("Elige UNA escena del aviso de la ficha y escribe en tu cuaderno tres líneas: qué muestra la imagen, qué dice el texto y qué sonido hay. Después escribe una oración que diga qué te hace sentir o pensar esa combinación. {F}",
        "Escena 3: imagen, una familia riendo con pan; texto, «Pan para todos»; sonido, risas y música que sube. Me hace sentir alegría y compañía, como si el pan fuera para compartir.",
        ["usa los tres elementos de la escena", "los datos corresponden a la ficha", "dice qué sugiere"],
        ["tres líneas y una oración"],
        ["inventar datos que no están en la tabla", "no mencionar el sonido"],
        "Pregunta: «¿Qué cambiaría si faltara el sonido?»."),
    reinforce="Recuerda un aviso que hayas visto hoy y anota qué imagen, qué texto y qué sonido tenía.",
    extend="Describe en tres líneas una escena para un aviso de una feria de tu barrio: imagen, texto y sonido.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo el vocabulario para analizar un texto audiovisual: plano, voz en off, música, silencio, punto de vista y postura.",
    prior=["Reconozco imagen, texto y sonido en un aviso.", "Sé qué es un punto de vista.", "Leo una tabla de escenas."],
    explain=[
        "Para describir lo que se ve hay palabras precisas. Un plano general muestra el lugar completo. Un primer plano muestra de cerca un rostro o un objeto y llama la atención sobre un detalle. El encuadre es lo que queda dentro de la imagen y lo que queda fuera.",
        "Para el sonido también hay palabras. La música marca un ambiente: lenta es melancólica, alegre es festiva. Un efecto sonoro es un ruido añadido, como un golpe. El silencio también comunica: puede crear tensión o dar importancia a lo que viene. La voz en off es la voz que se oye sin que se vea a quien habla.",
        "Con esas palabras puedes decir cuál es el punto de vista: a favor, en contra o neutro respecto de un hecho. Además puedes formular tu postura, que es lo que tú piensas, apoyada en lo que viste, leíste y escuchaste, y no solo en lo que te hace sentir.",
    ],
    vocab=[("plano general", "imagen que muestra el lugar completo"), ("primer plano", "imagen que muestra de cerca un rostro u objeto"), ("efecto sonoro", "ruido añadido para crear una sensación"), ("postura", "lo que tú piensas sobre un tema, apoyado en razones")],
    worked=[
        ("Nombrar un plano", "Escena 2: primer plano de una vendedora con los ojos húmedos.", ["Muestra de cerca un rostro.", "Hace que miremos su emoción."], "Primer plano que destaca la emoción"),
        ("Interpretar el sonido", "Escena 3: un golpe seco al ver el edificio con rejas.", ["Es un efecto sonoro.", "Da sensación de cierre y de rechazo."], "El golpe seco refuerza la idea de que no hay respuestas"),
    ],
    mistakes=[("Decir «música triste» sin relacionarla con lo que se muestra.", "La música sola no explica el punto de vista.", "Di qué idea refuerza la música en esa escena."),
              ("Confundir el punto de vista con mi postura.", "El punto de vista es de quien hizo el video; la postura es mía.", "Primero describe la mirada del video y luego tu opinión.")],
    T=[
        ("abc", "{F} ¿Qué tipo de plano es el de la escena 1?", "Plano general", "Primer plano", "Voz en off", "Muestra la feria completa y vacía."),
        ("abc", "{F} ¿Qué tipo de plano es el de la vendedora con los ojos húmedos?", "Primer plano", "Plano general", "Efecto sonoro", "La imagen muestra de cerca su rostro, no el lugar."),
        ("{F} ¿Cuántas familias pierden su sustento según la voz en off? Escribe el número.", "40", "La voz en off dice «cuarenta familias» en la escena 2."),
        ("ab", "{F} ¿Qué efecto crea el silencio y luego el violín en la escena 2?", "Aumenta la emoción de lo que se dice", "Informa un dato nuevo", "El silencio y la música crean emoción pero no agregan datos."),
        ("abc", "{F} ¿Qué efecto sonoro aparece en la escena 3?", "Un golpe seco", "Aplausos", "Risas", "La tabla anota un golpe seco."),
        ("abc", "{F} ¿Qué idea refuerza el golpe seco con el edificio cerrado?", "Que no hay respuestas ni salida", "Que la feria es alegre", "Que el edificio es nuevo", "El sonido seco se combina con las rejas y el texto «Sin respuestas»."),
        ("abc", "En Lengua y Literatura: ¿qué es la voz en off?", "Una voz que se oye sin que se vea a quien habla", "Una canción", "Una letra en pantalla", "No muestra al hablante en la imagen."),
        ("abc", "{F} ¿Cuál es el punto de vista del reportaje?", "A favor de los feriantes", "A favor del municipio", "Neutro, sin ninguna opinión", "Muestra su emoción, la pérdida y un edificio cerrado."),
        ("ab", "{F} ¿Qué escena muestra un lugar completo y no un detalle?", "La escena 1, un plano general", "La escena 2, un primer plano", "El plano general muestra la feria entera."),
        ("abc", "{F} ¿Qué falta en el reportaje para conocer otras miradas?", "La versión del municipio", "Más música", "Otro violín", "Solo se muestra un lado de la situación."),
        ("abc", "En Lengua y Literatura: ¿cuál es la diferencia entre el punto de vista del video y mi postura?", "El punto de vista es de quien hizo el video; la postura es mía", "No hay diferencia", "La postura es de quien lo hizo", "Primero se describe su mirada y después se formula la propia."),
        ("ab", "{F} Un vecino dice: «La música lenta prueba que el reportaje es verdadero». ¿Es correcto?", "No: la música crea ambiente y no prueba datos", "Sí: la música no engaña", "Solo los datos comprobables prueban algo."),
        ("abc", "{F} ¿Qué dato se puede comprobar en el reportaje?", "Que cuarenta familias pierden su sustento, cifra que puede verificarse con otra fuente", "Que el violín es triste", "Que la música es lenta", "Una cifra puede verificarse con otra fuente; la música es una emoción."),
    ],
    ctx=("abc", "En una reunión vecinal ponen un video sobre la feria con música triste y primeros planos de personas llorando. Se te pide opinar. ¿Qué haces?", "Separo lo que muestra el video de lo que siento y pido más información", "Opino solo según la música", "Me niego a opinar", "Primero se describen los recursos y luego se opina con razones."),
    sc=[("En Lengua y Literatura: ¿qué es un primer plano?", "Una imagen de cerca de un rostro u objeto", "El primer plano destaca un detalle de lo que se muestra."),
        ("¿Qué comunica el silencio?", "Puede crear tensión o dar importancia a lo que viene", "El silencio no es ausencia de sentido: también comunica."),
        ("¿Qué es mi postura?", "Lo que yo pienso, apoyado en razones", "Se apoya en lo que vi, leí y escuché.")],
    op=("Haz en tu cuaderno una tabla con las tres escenas de la ficha y tres columnas (tipo de plano, qué sonido, qué sugiere). Después escribe una oración con el punto de vista del reportaje. {F}",
        "Escena 1: plano general; viento y música lenta; sugiere abandono. Escena 2: primer plano; silencio y violín; sugiere pena. Escena 3: plano general; golpe seco; sugiere rechazo. Punto de vista: a favor de los feriantes.",
        ["tabla con tres escenas completas", "usa el vocabulario de la clase", "formula el punto de vista"],
        ["una tabla y una oración"],
        ["no distinguir planos", "decir un punto de vista sin datos"],
        "Pregunta: «¿Qué dato de la tabla apoya tu respuesta?»."),
    reinforce="Describe una escena de una noticia que hayas visto usando las palabras plano, sonido y voz en off.",
    extend="Escribe dos oraciones que expliquen cómo cambiaría el sentido de la escena 2 si el sonido fuera una marcha alegre.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo paso a paso cómo analizar una campaña con una tabla: qué dicen la imagen, el texto y el sonido, y si coinciden.",
    prior=["Describo planos y sonidos.", "Reconozco el punto de vista de un video.", "Leo una tabla escena por escena."],
    explain=[
        "El análisis tiene cinco pasos. Paso 1: lee la tabla escena por escena. Paso 2: anota imagen, texto y sonido. Paso 3: pregunta qué sugiere cada uno. Paso 4: mira si se refuerzan o se contradicen. Paso 5: formula el punto de vista y tu postura.",
        "Imagen, texto y sonido pueden reforzarse: todo apunta a la misma idea. O pueden contradecirse: la voz dice una cosa y la imagen muestra otra. Cuando se contradicen, es una señal para dudar y preguntar quién lo hizo y para qué.",
        "Tu postura debe apoyarse en datos de la tabla. Por ejemplo: «El mensaje dice seguridad, pero la imagen muestra trabajadores sin casco, por eso no confío del todo». Así separas lo que el video dice de lo que realmente muestra.",
    ],
    vocab=[("reforzarse", "decir lo mismo para dar más fuerza a una idea"), ("contradecirse", "decir cosas opuestas"), ("campaña", "serie de mensajes que buscan un cambio de conducta"), ("coherencia", "acuerdo entre lo que se dice y lo que se muestra")],
    worked=[
        ("Anotar y relacionar", "Escena 1: obra sin cascos; voz «la seguridad es lo primero»; música alegre.", ["Imagen: trabajadores sin casco.", "Voz: seguridad primero.", "Imagen y voz no coinciden."], "Imagen y voz se contradicen"),
        ("Apoyar una postura", "Escena 3: trabajador con casco sonriendo; «Cuídate».", ["Aquí imagen y texto coinciden.", "Pero la escena 1 mostraba lo contrario."], "La campaña es incoherente: dice una cosa en una escena y muestra otra en la primera"),
    ],
    mistakes=[("Creer que si la voz lo dice, es cierto.", "Hay que comprobar si la imagen lo confirma.", "Compara voz e imagen escena por escena."),
              ("Anotar solo lo que coincide.", "Las contradicciones son lo más importante de ver.", "Busca también lo que no se refuerza.")],
    T=[
        ("abc", "{F} ¿Qué muestra la imagen de la escena 1?", "Una obra donde los trabajadores no llevan casco", "Un casco colgado de un clavo", "Un trabajador sonriendo con casco", "La tabla indica que los trabajadores no llevan casco."),
        ("abc", "{F} ¿Qué dice la voz en off de la escena 1?", "«En esta empresa, la seguridad es lo primero»", "«Usa tu casco»", "«Cuídate»", "La voz afirma que la seguridad es lo primero."),
        ("{F} ¿Cuántas escenas tiene la campaña? Escribe el número.", "3", "La tabla del texto describe tres escenas numeradas."),
        ("abc", "{F} ¿Qué pasa entre la imagen y la voz en la escena 1?", "Se contradicen", "Se refuerzan", "No tienen relación", "La voz habla de seguridad y la imagen muestra trabajadores sin casco."),
        ("ab", "{F} ¿Qué efecto puede tener la música alegre en la escena 1?", "Quitar seriedad a un tema de seguridad", "Aumentar la preocupación por el casco", "Una música festiva suaviza un tema que requiere atención."),
        ("abc", "{F} ¿Qué escena muestra imagen y texto que se refuerzan?", "La escena 3, con casco y «Cuídate»", "La escena 1", "Ninguna", "En la escena 3 el trabajador con casco coincide con el mensaje."),
        ("abc", "{F} ¿Qué sugiere el primer plano del casco colgado de un clavo en la escena 2?", "Que el casco existe pero no se está usando", "Que el casco es nuevo", "Que no hay obra", "El casco colgado muestra un objeto sin uso."),
        ("abc", "{F} ¿Qué puedes concluir sobre la coherencia de la campaña?", "Es incoherente: dice una cosa en la voz y muestra otra en la imagen", "Es totalmente coherente", "No tiene mensaje", "La escena 1 contradice el mensaje."),
        ("ab", "{F} ¿Cuál es el paso que viene después de anotar imagen, texto y sonido?", "Preguntar qué sugiere cada uno", "Escribir la postura final sin pensar", "Primero se interpreta lo anotado y luego se formula la postura."),
        ("abc", "{F} ¿Cuál es una postura apoyada en la tabla?", "No confío del todo, porque la imagen de la escena 1 contradice el mensaje", "Es la mejor campaña porque la música es alegre", "Las campañas siempre mienten", "La postura usa un dato de la tabla."),
        ("abc", "En Lengua y Literatura: ¿qué significa que imagen y texto se refuercen?", "Que dicen lo mismo y dan más fuerza a la idea", "Que dicen cosas opuestas", "Que no se relacionan", "Reforzarse es apoyar la misma idea."),
        ("ab", "{F} Un compañero dice: «La campaña no hace falta porque dice que la seguridad es lo primero». ¿Es una buena conclusión?", "No: lo que dice no coincide con lo que muestra", "Sí: la voz lo afirma", "Hay que mirar la imagen, y la escena 1 muestra lo contrario de lo que dice la voz."),
        ("abc", "{F} ¿Qué haces si encuentras una contradicción entre imagen y texto?", "Dudo del mensaje y busco otra fuente", "Creo la voz sin revisar", "Borro la imagen", "Una contradicción es señal para verificar."),
    ],
    ctx=("abc", "En una charla ven una campaña sobre «cuidado de las personas» donde se ve a personas trabajando sin protección. ¿Qué observación sirve?", "Que el mensaje y la imagen se contradicen", "Que la música es bonita", "Que el video es largo", "Anotar la contradicción ayuda a evaluar el mensaje."),
    sc=[("¿Cuántos pasos tiene el análisis de hoy?", "Cinco", "Leer, anotar, interpretar, relacionar y formular punto de vista."),
        ("En Lengua y Literatura: ¿qué es la coherencia en un video?", "Que lo que se dice coincide con lo que se muestra", "Es el acuerdo entre imagen, texto y sonido."),
        ("¿Qué hago si imagen y voz se contradicen?", "Dudo y verifico", "La contradicción es una señal de alerta.")],
    op=("Haz en tu cuaderno una tabla con las tres escenas (imagen, texto, sonido, ¿se refuerzan o se contradicen?). Escribe después tu postura sobre la campaña en tres oraciones, con dos datos de la tabla. {F}",
        "Escena 1: obra sin cascos; seguridad primero; música alegre; se contradicen. Escena 2: casco colgado; usa tu casco; golpes; el casco no se usa. Escena 3: trabajador con casco; cuídate; música; se refuerzan. Postura: no confío del todo, porque en la escena 1 se ve lo contrario de lo que dice la voz. Necesitaría ver cómo es la obra real.",
        ["tabla con las tres escenas", "identifica una contradicción", "postura con dos datos"],
        ["una tabla y tres oraciones"],
        ["no mencionar el sonido", "postura sin datos"],
        "Pregunta: «¿Qué escena te hizo dudar y por qué?»."),
    reinforce="Observa un afiche de tu barrio y anota si lo que dice coincide con lo que muestra.",
    extend="Reescribe la escena 1 de modo que imagen, voz y sonido se refuercen.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: comparo dos reportajes del mismo hecho y veo cómo cada uno elige mostrar y callar cosas.",
    prior=["Sé separar imagen, texto y sonido.", "Reconozco si se refuerzan o se contradicen.", "Sé qué es un punto de vista."],
    explain=[
        "Dos reportajes sobre el mismo hecho pueden mostrar cosas muy distintas. Cada uno elige qué imagen usar, qué decir y qué música poner. También elige qué dejar fuera. Lo que se omite también construye un punto de vista. Mostrar solo un lado de un hecho es un sesgo.",
        "Para comparar, haz una tabla con dos columnas, una por reportaje, y filas para imagen, texto, sonido y lo que no muestra. Luego mira qué comparten y en qué se diferencian. Comparar ayuda a ver que ninguna versión muestra todo.",
        "Para formular tu postura, no basta con elegir un reportaje. Puedes decir que ambos muestran una parte, señalar qué dato falta y qué harías para averiguarlo. Ese paso te ayuda a conversar con respeto con quienes piensan distinto.",
    ],
    vocab=[("omitir", "dejar algo fuera de lo que se cuenta"), ("versión", "forma en que alguien cuenta un hecho"), ("sesgo", "inclinación a mostrar un solo lado"), ("comparar", "mirar dos cosas para ver qué comparten y qué cambia")],
    worked=[
        ("Comparar las imágenes", "A: máquinas bajo un cielo despejado. B: local con mercadería sin vender.", ["A muestra el avance.", "B muestra el efecto en los comerciantes.", "Cada una elige un lado."], "Cada reportaje elige mostrar una parte"),
        ("Detectar lo que se omite", "A no muestra a los comerciantes; B no muestra la maqueta ni el plazo.", ["A omite el efecto en las ventas.", "B omite el plan y el plazo de término."], "Cada versión omite lo que no favorece su mirada"),
    ],
    mistakes=[("Elegir un reportaje como «el verdadero».", "Cada uno muestra una parte del hecho.", "Di qué muestra cada uno y qué falta."),
              ("Pensar que lo que no se muestra no importa.", "Lo omitido también construye el punto de vista.", "Anota lo que cada versión deja fuera.")],
    T=[
        ("abc", "{F} ¿Qué sonido usa el Reportaje A en la escena 1?", "Una marcha alegre", "Ruido de tráfico", "Silencio", "La tabla anota una marcha alegre."),
        ("abc", "{F} ¿Qué texto aparece en pantalla en la escena 2 del Reportaje B?", "«Cuándo termina»", "«Listo en seis meses»", "«Avanzan las obras»", "La escena 2 de B muestra «Cuándo termina»."),
        ("{F} ¿En cuántos meses dice el Reportaje A que estará listo? Escribe el número.", "6", "El texto en pantalla dice «Listo en seis meses»."),
        ("abc", "{F} ¿Cuál es el punto de vista del Reportaje A?", "Favorable a las obras", "Contrario a las obras", "Sin ninguna opinión", "Muestra avance, aplausos y un cielo despejado."),
        ("abc", "{F} ¿Cuál es el punto de vista del Reportaje B?", "Muestra el perjuicio a los comerciantes", "Celebra el avance de las obras", "Es neutro y muestra todo", "Muestra mercadería sin vender y zanjas con poco público."),
        ("ab", "{F} ¿Qué omite el Reportaje A?", "El efecto en las ventas de los comerciantes", "El avance de las máquinas", "No muestra a los comerciantes ni el efecto de las obras en su negocio."),
        ("ab", "{F} ¿Qué omite el Reportaje B?", "El plan de la avenida terminada y su plazo", "La mercadería sin vender", "No muestra la maqueta ni el plazo de término."),
        ("abc", "{F} ¿Qué tienen en común ambos reportajes?", "Hablan de las mismas obras en la misma avenida", "Usan la misma música", "Entrevistan a las mismas personas", "El dato de apoyo dice que tratan el mismo hecho."),
        ("abc", "{F} ¿Qué efecto crea el silencio de la escena 2 del Reportaje B?", "Da peso a la pregunta «Cuándo termina»", "Anuncia buenas noticias", "Cambia la avenida", "Sin sonido, la pregunta queda más presente."),
        ("abc", "{F} Una vecina dice: «El A es el verdadero porque tiene música alegre». ¿Qué le respondes?", "Que cada reportaje muestra una parte y la música no prueba nada", "Que tiene razón", "Que el B es el único válido", "La música crea ambiente, no verdad."),
        ("abc", "{F} ¿Qué puedes hacer para formular una postura equilibrada?", "Decir qué muestra cada uno, qué falta y cómo averiguarlo", "Elegir el reportaje con más escenas", "No opinar nunca", "Una postura equilibrada reconoce lo que cada uno muestra y omite."),
        ("ab", "{F} ¿Qué diferencia hay en la forma de usar la imagen?", "A usa planos amplios del avance; B usa un primer plano de un local", "Ambos usan el mismo plano", "A usa planos generales y maqueta; B parte con un primer plano de la mercadería."),
        ("abc", "{F} ¿Qué dato podría confirmar o refutar la versión de B?", "Un registro de ventas del local de antes y durante las obras", "La marcha alegre de A", "El cielo despejado", "Un dato comprobable permite verificar el efecto en las ventas."),
    ],
    ctx=("abc", "En una reunión de vecinos pasan los dos reportajes. Algunos dicen que A es el correcto y otros que B. ¿Qué propones?", "Comparar qué muestra y qué omite cada uno y buscar datos", "Votar cuál suena mejor", "Cancelar la reunión", "Comparar y buscar datos permite una conversación respetuosa."),
    sc=[("En Lengua y Literatura: ¿qué es omitir?", "Dejar algo fuera de lo que se cuenta", "Lo omitido también construye el punto de vista."),
        ("¿Por qué comparo dos reportajes del mismo hecho?", "Porque cada uno muestra una parte", "Comparar muestra lo que cada versión elige."),
        ("¿Qué hago para tener una postura equilibrada?", "Decir qué muestra cada uno y qué falta", "Así reconozco las dos miradas y lo que cada una omite.")],
    op=("Haz una tabla de dos columnas (Reportaje A y B) y cuatro filas (imagen, texto, sonido, qué omite). Después escribe tu postura en tres oraciones, con un dato de cada reportaje y una pregunta que harías para averiguar más. {F}",
        "A: máquinas, «Avanzan las obras», marcha alegre, omite a los comerciantes. B: local con mercadería, «Ventas a la baja», tráfico y silencio, omite el plazo. Postura: ambos muestran una parte. A dice que estará listo en seis meses; B dice que bajaron las ventas. Preguntaría cuánto bajaron las ventas y qué apoyo habrá.",
        ["tabla de 2 columnas y 4 filas", "usa un dato de cada reportaje", "formula una pregunta"],
        ["una tabla y tres oraciones"],
        ["elegir uno como «verdadero» sin datos", "no decir qué se omite"],
        "Pregunta: «¿Qué dato falta para decidir?»."),
    reinforce="Cuenta en dos versiones, una a favor y otra en contra, un hecho pequeño de tu barrio y anota qué omite cada una.",
    extend="Escribe cinco preguntas que le harías al canal que hizo el Reportaje A y cinco al del Reportaje B.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido: preparo y comunico oralmente mis conclusiones sobre un video, con orden, razones y respeto.",
    prior=["Sé analizar imagen, texto y sonido.", "Sé formular una postura con datos.", "Sé que puedo preparar lo que voy a decir."],
    explain=[
        "Comunicar oralmente tus conclusiones tiene una estructura. Primero dices qué viste y de qué trata. Luego explicas cómo se usan la imagen, el texto y el sonido. Después das tu postura con una razón. Por último, cierras con una pregunta o una propuesta. En dos minutos alcanzas.",
        "Una buena exposición oral se reconoce por cuatro criterios: orden (se entiende el hilo), claridad (voz y ritmo que se escuchan), evidencia (datos de la tabla) y respeto (no se juzga a las personas). Puedes apoyarte en una tarjeta con tus ideas, pero no leas todo.",
        "En una junta de vecinos o en una reunión, tu postura puede ayudar a decidir. Por eso conviene separar los datos de tu opinión, reconocer lo que no sabes y escuchar a quien piensa distinto. Una exposición respetuosa invita a conversar, no a ganar.",
    ],
    vocab=[("exposición oral", "presentación hablada de lo que pensaste y por qué"), ("estructura", "orden de las partes de una exposición"), ("evidencia", "dato que apoya lo que dices"), ("tarjeta de apoyo", "papel con las ideas principales para recordar")],
    worked=[
        ("Armar la exposición", "Video: «Reciclar en el edificio».", ["Qué vi: un video para que vecinos separen residuos.", "Cómo lo hace: imagen de basura desbordada, vecinos reunidos y música animada.", "Mi postura: muestra el problema, pero falta explicar el retiro.", "Cierre: pregunto a la administración cómo se retira."], "Exposición completa en cuatro partes"),
        ("Evaluar con criterios", "Exposición B: dice qué quiere el video, cómo lo hace, su postura y un cierre.", ["Orden: sí.", "Evidencia: cita imagen y texto.", "Respeto: no juzga a personas."], "Cumple los criterios"),
    ],
    mistakes=[("Leer una hoja entera sin mirar al público.", "Se pierde claridad y contacto con quien escucha.", "Usa una tarjeta con ideas y habla con tus palabras."),
              ("Juzgar a las personas en vez de analizar el video.", "Es una falta de respeto y no usa evidencia.", "Habla de lo que el video muestra y de tu razón.")],
    T=[
        ("abc", "{F} ¿Qué muestra la imagen de la escena 1 del video?", "Un contenedor de basura desbordado", "Vecinos reciclando", "Un letrero con instrucciones", "La tabla indica un primer plano del contenedor desbordado."),
        ("abc", "{F} ¿Qué sonido hay en la escena 2?", "Música animada", "Moscas", "Silencio", "La escena 2 lleva música animada."),
        ("{F} ¿Cuántas escenas tiene el video? Escribe el número.", "3", "La tabla del texto describe tres escenas numeradas."),
        ("abc", "{F} ¿Cuál de las exposiciones es la mejor?", "La B, porque explica los recursos, da una postura y razones", "La A, porque es corta", "La C, porque es firme", "La B cumple los criterios de orden, evidencia y respeto."),
        ("abc", "{F} ¿Qué le falta a la Exposición A?", "Explicar cómo usa el video imagen, texto y sonido", "Más risas", "Un título", "Solo dice «Me gustó» sin análisis ni razones."),
        ("abc", "{F} ¿Qué problema tiene la Exposición C?", "Juzga a las personas y no usa datos del video", "Es demasiado larga", "Cita demasiadas imágenes", "Dice «flojos» y no se apoya en evidencia."),
        ("ab", "{F} ¿Qué dato de la tabla usa la Exposición B para fundamentar su postura?", "La imagen del contenedor desbordado y la frase «más residuos»", "El color del contenedor", "Usa una imagen y un texto del video como evidencia."),
        ("abc", "En Lengua y Literatura: ¿cuál es el orden de una buena exposición oral?", "Qué vi, cómo lo dice, mi postura y un cierre", "Mi postura, qué vi y cómo lo dice", "Solo el cierre", "Esa secuencia permite seguir el hilo."),
        ("abc", "¿Cuál de estos es un criterio de una buena exposición oral?", "Respeto: no se juzga a las personas", "Hablar siempre más fuerte", "Usar la mayor cantidad de palabras difíciles", "El respeto es uno de los cuatro criterios."),
        ("abc", "¿Para qué sirve una tarjeta de apoyo?", "Para recordar las ideas principales sin leerlo todo", "Para leer toda la exposición", "Para reemplazar lo que dices por una lectura", "Ayuda a hablar con tus palabras."),
        ("ab", "{F} Después de la postura de la Exposición B, ¿qué pregunta de cierre sirve?", "¿Cómo se retira lo que se separa?", "¿Cuántos vecinos hay?", "La pregunta surge de lo que el video no explica."),
        ("abc", "{F} ¿Qué haces si alguien no está de acuerdo con tu postura?", "Escucho sus razones y las comparo con mis datos", "Insisto sin escuchar", "Cambio de tema", "El respeto exige escuchar y comparar razones."),
        ("abc", "{F} ¿Cuál es una forma respetuosa de decir que la Exposición C se equivoca?", "Dices que no se apoya en datos del video y propones agregar evidencia", "Dices que quien la hizo es flojo", "Dices que no vale la pena escucharla", "Se critica el texto, no a la persona."),
    ],
    ctx=("abc", "En una junta de vecinos te piden dar tu opinión sobre un video del municipio, en dos minutos. ¿Qué haces?", "Preparo una tarjeta con qué vi, cómo lo dice, mi postura y un cierre", "Improviso sin pensar", "Leo sin mirar a nadie", "Una estructura corta permite comunicar con orden y respeto."),
    sc=[("¿Qué cuatro partes tiene una exposición oral de hoy?", "Qué vi, cómo lo dice, mi postura y un cierre", "Dan orden a lo que se dice."),
        ("En Lengua y Literatura: ¿qué es la evidencia?", "Un dato que apoya lo que digo", "Sin evidencia la postura es solo una opinión."),
        ("¿Qué criterio evita juzgar a las personas?", "El respeto", "Se analiza el video, no a quien piensa distinto.")],
    op=("Prepara una exposición oral de dos minutos sobre el video de la ficha. Escribe en una tarjeta cuatro ideas, una por parte: qué vi, cómo lo dice, mi postura con una razón y un cierre. Si puedes, ensáyala en voz alta. {F}",
        "Qué vi: un video para que los vecinos reciclen. Cómo lo dice: imagen de basura desbordada, vecinos reunidos y música animada. Postura: muestra el problema y la solución, pero no explica el retiro. Cierre: ¿quién retira lo reciclado?",
        ["cuatro partes en orden", "usa datos de la tabla", "razón de la postura", "tono respetuoso"],
        ["una tarjeta con cuatro ideas"],
        ["no usar datos del video", "juzgar a las personas"],
        "Pregunta: «¿Qué dato apoya tu postura?»."),
    reinforce="Cuenta oralmente, en un minuto, una noticia que viste ayer, sin leer.",
    extend="Prepara otra tarjeta con una postura contraria a la tuya y explica con qué razones podría defenderla otra persona.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: analizo una noticia nueva, formulo mi postura con evidencia y decido cómo mejorar mi forma de comunicar.",
    prior=["Sé analizar imagen, texto y sonido.", "Sé que cada versión omite algo.", "Sé armar una exposición oral breve."],
    explain=[
        "Revisar lo logrado es comprobar que usas bien el método. Para cada texto audiovisual, anota imagen, texto y sonido, mira si se refuerzan, detecta lo que se omite, formula tu postura con datos y comunícala con orden y respeto.",
        "Una noticia puede mostrar solo una versión. En la noticia de hoy, la voz dice «más esperas», la imagen muestra a una persona bajo la lluvia y la música es triste, pero no aparece la versión de la empresa. Eso no la hace falsa, pero sí incompleta.",
        "Para cerrar, evalúa tu propio trabajo con una lista de cuatro preguntas. ¿Usé las tres partes? ¿Señalé lo omitido? ¿Mi postura tiene datos? ¿Hablé con respeto? Después elige una cosa para mejorar la próxima vez.",
    ],
    vocab=[("incompleta", "que no muestra todas las partes"), ("autoevaluación", "revisar tu propio trabajo con criterios"), ("dato verificable", "dato que se puede comprobar en otra fuente"), ("emoción", "sentimiento que produce algo, como pena o rabia")],
    worked=[
        ("Separar datos y emoción", "Escena 3: pasajera dice que el bus pasaba cada diez minutos y ahora cada veinte.", ["El dato es el cambio de diez a veinte minutos.", "La música triste de la escena 1 es emoción."], "Dato: frecuencia; emoción: música y lluvia"),
        ("Detectar lo omitido", "La noticia no muestra la versión de la empresa.", ["Falta la razón del cambio de horario.", "Falta una cifra de pasajeros."], "Faltan la versión de la empresa y datos sobre el cambio"),
    ],
    mistakes=[("Usar la emoción como si fuera un dato.", "La música triste no prueba que algo sea cierto.", "Apoya tu postura en datos que se puedan comprobar."),
              ("Quedarse solo con la parte que coincide con lo que uno piensa.", "Eso es un sesgo.", "Busca también lo que no coincide con tu opinión.")],
    T=[
        ("abc", "{F} ¿Qué dato verificable entrega la pasajera?", "Que antes el bus pasaba cada diez minutos y ahora cada veinte", "Que el bus está lleno", "Que llueve", "Es una afirmación concreta que podría comprobarse con otra fuente."),
        ("=", "Si antes un bus pasaba cada 10 minutos, ¿cuántos buses pasaban en 60 minutos?", "60 // 10", "Se divide el tiempo total por el intervalo entre buses."),
        ("=", "Si ahora un bus pasa cada 20 minutos, ¿cuántos buses pasan en 60 minutos?", "60 // 20", "Se divide el tiempo total por el nuevo intervalo."),
        ("abc", "{F} ¿Qué recurso busca crear tristeza en la escena 1?", "La lluvia y la música triste", "El texto «Pasajeros molestos»", "Las bocinas", "La tabla anota lluvia y música triste."),
        ("abc", "{F} ¿Qué texto en pantalla aparece en la escena 2?", "«Pasajeros molestos»", "«Nuevo horario»", "«Más esperas»", "La escena 2 muestra «Pasajeros molestos»."),
        ("abc", "{F} ¿Qué se omite según la nota final?", "La versión de la empresa de buses", "La voz de la pasajera", "El bus lleno", "La nota final de la ficha lo dice de forma expresa."),
        ("ab", "{F} ¿Es falsa la noticia por omitir la versión de la empresa?", "No necesariamente: es incompleta y conviene buscar otra fuente", "Sí: toda omisión es mentira", "Omitir una versión la deja incompleta, pero eso no prueba que sea falsa."),
        ("abc", "{F} ¿Qué parte de la noticia es una emoción y no un dato?", "La música triste con la lluvia", "El cambio de diez a veinte minutos", "El nombre «Pasajera»", "La música crea una sensación, no entrega información."),
        ("abc", "{F} ¿Cuál es una postura bien apoyada?", "Según la pasajera, el intervalo subió de 10 a 20 minutos; falta la versión de la empresa", "La empresa es culpable porque la música es triste", "Nadie debe usar buses", "Usa un dato verificable y reconoce lo que falta."),
        ("abc", "{F} ¿Qué haces para completar la información?", "Busco la versión de la empresa y otro testimonio", "Comparto solo esta noticia", "Me quedo con mi primera impresión", "Contrastar varias versiones completa el cuadro de la situación."),
        ("ab", "Gabriela dice: «Si el video me enoja, es verdad». ¿Qué le respondes?", "Que sentir enojo no prueba que algo sea cierto", "Que tiene razón", "Las emociones no son una prueba de que un dato sea verdadero."),
        ("abc", "En tu autoevaluación, ¿qué pregunta te ayuda a reconocer un sesgo?", "¿Busqué también lo que no coincide con lo que pienso?", "¿Cuánto duró el video?", "¿Cuántas escenas tenía?", "El sesgo aparece cuando solo se mira un lado."),
        ("abc", "{F} ¿Qué recurso del sonido incluye la escena 3?", "Ruido de calle", "Música alegre", "Aplausos", "La tabla anota ruido de calle."),
    ],
    ctx=("abc", "Ves en las redes un video con música dramática que dice que cierran un consultorio del barrio, sin mostrar de dónde sale el dato. ¿Qué haces?", "Busco un aviso oficial o hablo con quien puede confirmarlo", "Lo comparto de inmediato", "Lo borro y no pienso más", "Un dato sin fuente debe verificarse antes de difundirse."),
    sc=[("En Lengua y Literatura: ¿qué es una postura bien apoyada?", "La que usa datos verificables y reconoce lo que falta", "Los datos la sostienen y la honestidad la hace más sólida."),
        ("¿Una música triste prueba que algo es cierto?", "No", "La música crea una emoción y no una prueba."),
        ("¿Qué cuatro preguntas hago al evaluarme?", "Tres partes, lo omitido, datos y respeto", "Son los cuatro criterios de revisión.")],
    op=("Analiza la noticia de la ficha en un texto de cinco oraciones: qué dicen imagen, texto y sonido; qué dato verificable hay; qué se omite; tu postura con un dato; y qué mejorarás de tu forma de comunicar. {F}",
        "En la noticia, la imagen muestra a una persona bajo la lluvia, la voz dice «más esperas» y la música es triste. El dato verificable es que el bus pasaba cada diez minutos y ahora cada veinte. Se omite la versión de la empresa. Mi postura es que el cambio parece afectar a los pasajeros, pero falta otra fuente. Mejoraré nombrando lo que falta.",
        ["usa imagen, texto y sonido", "señala un dato y una omisión", "postura con dato", "dice qué mejorará"],
        ["cinco oraciones escritas"],
        ["usar la emoción como dato", "no señalar lo omitido"],
        "Pregunta: «¿Qué fuente consultarías para completar la información?»."),
    reinforce="Anota en una tarjeta tus cuatro criterios de revisión y úsalos en la próxima noticia que veas.",
    extend="Explica oralmente a otra persona, en un minuto, la diferencia entre un dato y una emoción en un video.",
)

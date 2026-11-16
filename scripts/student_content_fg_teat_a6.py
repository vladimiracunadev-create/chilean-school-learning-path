"""Teatro 3.º y 4.º medio FG: OAC-04 (propósitos expresivos y contexto de obras teatrales), clases 1 a 3. Obras y textos originales e inventados; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O4 = "FG-TEAT-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (descripción de una puesta de ejemplo, «El último tren de la noche», inventada). Una actriz espera sentada en un banco. Mueve los dedos como si contara monedas. "
     "Habla con la voz muy baja y con pausas largas. Cuando suena un silbido lejano levanta la cabeza de golpe y calla. Al final se pone de pie muy despacio y deja su bolso en el banco.")
build(
    O4, 1, F,
    use="Aprenderé a inferir el propósito expresivo de una obra a partir de criterios estéticos, en especial el uso expresivo del gesto y la voz, apoyando cada inferencia en rasgos que se pueden observar.",
    prior=["Distingo hechos de interpretaciones.", "Sé describir cuerpo, gesto, voz, ritmo y pausa.", "Sé que el propósito es lo que una obra busca comunicar."],
    explain=[
        "El propósito expresivo de una obra es lo que busca comunicar o hacer sentir al público: una idea, una emoción, una pregunta. Rara vez se declara; se infiere. Inferir es sacar una conclusión razonable a partir de pistas. Las pistas son rasgos que se pueden observar: lo que hacen el cuerpo y la voz, el ritmo, el uso del espacio, los objetos, los silencios.",
        "Los criterios estéticos son aspectos de la obra que se observan y analizan para entender cómo comunica: por ejemplo el uso expresivo del gesto y de la voz, los recursos de la puesta en escena, las ideas que plantea y las emociones y sensaciones que genera. Una inferencia sólida cita el rasgo, explica qué efecto produce y propone qué propósito sugiere. Por ejemplo: «las pausas largas y la voz baja crean tensión de espera».",
        "Una obra admite más de una lectura, pero no cualquier lectura. Una inferencia es razonable si otra persona puede comprobar los rasgos que la sostienen. Decir «me aburrí» es una opinión personal, no una inferencia sobre el propósito. Las obras de esta clase son descripciones inventadas; el video o la función real queda para el docente.",
    ],
    vocab=[("propósito expresivo", "lo que una obra busca comunicar o hacer sentir"), ("inferir", "sacar una conclusión razonable a partir de pistas observables"), ("criterio estético", "aspecto de la obra que se observa para entender cómo comunica"), ("rasgo", "característica observable de una puesta en escena"), ("lectura", "interpretación posible de una obra, apoyada en rasgos")],
    worked=[
        ("Inferir con evidencia", "En una escena, un actor mira el reloj cada pocos segundos y responde con frases cortas. ¿Qué propósito puede inferirse?", ["Rasgos: mira el reloj muchas veces y habla en frases cortas.", "Efecto: transmite apuro o impaciencia; el propósito podría ser mostrar la tensión de esperar."], "Mostrar la tensión de la espera, apoyado en esos rasgos"),
        ("Separar opinión e inferencia", "Una espectadora dice: «la obra me pareció lenta». Otra: «las pausas de 10 segundos hacen que la escena parezca detenida». ¿Cuál es una inferencia apoyada en rasgos?", ["La primera es una opinión personal.", "La segunda cita un rasgo comprobable y su efecto."], "La segunda"),
    ],
    mistakes=[("Escribir «el propósito es triste» sin citar nada de la obra.", "No hay rasgos que otra persona pueda comprobar.", "Cita el rasgo, su efecto y luego el propósito."),
              ("Creer que hay una sola lectura correcta que debe adivinarse.", "Las obras permiten varias lecturas razonables, cada una con su evidencia.", "Defiende tu lectura con rasgos observables.")],
    T=[
        ('abc', '¿Qué es el propósito expresivo de una obra?', 'Lo que busca comunicar o hacer sentir al público', 'La cantidad de personas que asisten a verla', 'La historia que cuenta de principio a fin, en orden', 'El propósito es lo que la obra quiere expresar; el argumento es solo la historia que narra.'),
        ('abc', '{F} ¿Cuál es un rasgo del uso expresivo de la voz en esta puesta?', 'La voz muy baja y con pausas largas', 'El banco en que se sienta la actriz durante la escena', 'El silbido lejano que se escucha una vez', 'La voz baja y las pausas son rasgos de uso de la voz; el banco y el silbido son otros recursos.'),
        ('abc', '¿Qué es un criterio estético al analizar una obra?', 'Un aspecto observable, como el gesto, la voz o el uso del espacio', 'Si la obra le gustó o no a quien la analiza', 'Si la obra es famosa o poco conocida entre el público de las redes del colegio y sus alrededores', 'Es un aspecto de la obra que se analiza, no una preferencia personal ni su fama.'),
        ('abc', '{F} Cuando suena el silbido, la actriz levanta la cabeza de golpe y calla. ¿Qué efecto produce?', 'Genera expectativa: sugiere que espera algo o a alguien', 'Muestra que se aburrió de esperar y que pronto se irá de la escena', 'Indica que la obra terminó en ese momento', 'Reaccionar de golpe a un sonido y callar crea expectativa; ella no sale ni termina la obra.'),
        ('abc', '{F} ¿Qué inferencia sobre el propósito se apoya en los rasgos descritos?', 'Mostrar la espera y la expectativa de una persona sola', 'Enseñar los horarios de un servicio de transporte', 'Hacer reír con un malentendido entre dos personas', 'Las pausas, el gesto de contar monedas y el silbido sostienen la idea de espera.'),
        ('abc', '¿Por qué una inferencia debe apoyarse en evidencia?', 'Porque otra persona puede comprobar en la obra lo que la sostiene', 'Porque solo existe una lectura posible de cada obra', 'Porque la evidencia reemplaza lo que sintió cada espectador y evita tener que explicar', 'La evidencia permite discutir con base en lo que se observó.'),
        ('=', 'En una escena de 180 segundos hay 4 pausas largas de 9 segundos cada una. ¿Qué porcentaje de la escena ocupan las pausas?', '4*9*100//180', 'Se suma el tiempo de pausas, se divide en el total y se pasa a porcentaje.', ' %'),
        ('abc', 'Un espectador dice: «Me aburrí, entonces la obra es mala». ¿Qué lo diferencia de una inferencia?', 'Es una opinión personal; la inferencia cita rasgos de la puesta que se pueden comprobar', 'Es una inferencia, porque se basa en lo que él sintió durante la función', 'Es un dato, porque todos los espectadores sienten lo mismo', 'Una opinión expresa una reacción; la inferencia sobre el propósito necesita rasgos.'),
        ('abc', '{F} Para sustentar que la obra expresa espera, ¿qué evidencia sirve más?', 'Las pausas largas, la voz baja y levantar la cabeza al silbido', 'Que la actriz sea joven y use un abrigo oscuro', 'Que el título del programa de mano tenga la palabra «tren» y la actriz esté vestida de viajera', 'La evidencia más sólida está en la actuación y los sonidos, no en datos ajenos a lo que se ve.'),
        ('abc', 'Una persona lee la obra como soledad y otra como esperanza. ¿Pueden ser ambas razonables?', 'Sí, si cada una cita rasgos que la respaldan, porque la obra admite varias lecturas', 'No, porque una obra solo tiene un propósito correcto que se debe adivinar', 'Sí, aunque ninguna cite rasgos, porque cada espectador opina libremente', 'Varias lecturas son razonables cuando cada una tiene evidencia observable.'),
        ('abc', '{F} Imagina que la actriz hablara fuerte y rápido y se moviera por todo el espacio. ¿Cómo cambiaría el propósito percibido?', 'Se acercaría a la urgencia o la ansiedad, y no a la espera tranquila', 'No cambiaría, porque el texto sigue siendo el mismo', 'Se volvería un propósito de humor, sin importar qué más cambie en el resto de la puesta', 'El cambio de voz y movimiento produce otro efecto, que sugiere otro propósito.'),
        ('=', 'Un registro de análisis anota 12 rasgos; 9 son hechos observados y el resto son interpretaciones. ¿Qué porcentaje son hechos?', '9*100//12', 'Se divide el número de hechos entre el total de rasgos anotados.', ' %'),
        ('abc', 'El grupo uno cita tres rasgos y concluye «espera». El grupo dos concluye «terror» sin citar ningún rasgo. ¿Cuál inferencia es más sólida?', 'La del grupo uno, porque se apoya en rasgos comprobables', 'La del grupo dos, porque nombra una emoción más intensa', 'Ambas, porque las dos son lecturas personales y no se pueden comparar', 'La sustentación con rasgos hace comparable una lectura; una emoción sin evidencia no lo es.'),
    ],
    ctx=('ab', 'Ves una escena y quieres inferir su propósito. ¿Qué haces primero?', 'Anotar rasgos observables y después proponer el propósito', 'Leer la opinión de otra persona y repetirla como tuya', 'Primero se observan los rasgos y después se concluye con ellos.'),
    sc=[
        ("En Teatro: ¿qué es inferir el propósito de una obra?", "Sacar una conclusión razonable a partir de rasgos observables", "Una inferencia se sostiene con pistas que otro puede comprobar."),
        ("¿Una opinión como «me aburrí» es una inferencia sobre el propósito?", "No, es una opinión personal", "No cita ningún rasgo de la obra que se pueda comprobar."),
        ("¿Una obra puede tener más de una lectura razonable?", "Sí, si cada una cita rasgos que la respaldan", "Las lecturas se valoran por su evidencia."),
    ],
    op=("Lee la descripción de una puesta de ejemplo: «Un actor ordena una mesa para dos, mira la puerta, acomoda de nuevo los cubiertos de plástico, deja una silla vacía y apaga la luz de a poco». Escribe: tres rasgos observables, el efecto de cada uno y un propósito expresivo que infieras, sin decir 'me gustó' ni 'me aburrió'.",
        "Rasgos: ordena la mesa para dos; mira la puerta varias veces; deja una silla vacía. Efectos: preparación, expectativa, ausencia. Propósito posible: expresar la espera de alguien que no llega.",
        ["tres rasgos observables", "efecto de cada rasgo", "propósito apoyado en esos rasgos", "no usa opiniones personales como evidencia"],
        ["hoja con rasgos, efectos y propósito"],
        ["escribir solo la emoción", "usar opiniones como evidencia"],
        "Pregunta: «¿en qué parte de la puesta se ve eso?». Si no puede señalarla, falta evidencia."),
    reinforce="Observa una escena breve de tu entorno o inventa una y escribe dos rasgos y el propósito que sugieren.",
    extend="Explica por qué dos personas pueden inferir propósitos distintos de la misma obra sin que ninguna se equivoque.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (texto dramático original e inventado, «La caja»). Una oficina vacía, de noche. ELENA ordena papeles. DAVID entra con el abrigo mojado. "
     "DAVID: Vine por mis cosas. ELENA: Ya están en esa caja. (Pausa.) DAVID: ¿No me vas a preguntar nada? ELENA: (sin mirarlo) La caja pesa poco. Mejor así. "
     "(DAVID toma la caja. Antes de salir, deja una llave sobre el escritorio. ELENA mira la llave hasta que la puerta se cierra.)")
build(
    O4, 2, F,
    use="Aprenderé a leer un texto dramático (diálogo, acotaciones, conflicto y objetos) y a inferir su propósito expresivo apoyándome en lo que los personajes dicen, callan y hacen.",
    prior=["Sé inferir con rasgos observables.", "Sé que un personaje tiene objetivo y obstáculo.", "Sé leer acotaciones."],
    explain=[
        "Un texto dramático está escrito para ser representado. Tiene diálogos (lo que dicen los personajes) y acotaciones (indicaciones sobre acciones, gestos, silencios y espacio). Para inferir su propósito conviene leerlo dos veces: primero para entender qué pasa y luego para fijarse en cómo pasa. Lo que se dice importa, pero también lo que se calla, las pausas y lo que hacen los personajes.",
        "Las pistas de un texto son el conflicto (qué enfrenta a los personajes), el subtexto (lo que se quiere decir sin decirlo), los objetos que cobran importancia y el cierre. En «La caja», Elena habla de lo poco que pesa la caja, pero lo que expresa es la distancia entre ella y David; la llave que se deja sobre el escritorio puede marcar el fin de una relación de trabajo. Estos hechos permiten proponer un propósito, como mostrar un adiós contenido.",
        "Un propósito se formula en una oración y se apoya en dos o tres pistas del texto: «El texto muestra cómo se vive un adiós sin palabras de despedida; lo sostienen las pausas, la caja que pesa poco y la llave que se deja». Como todo texto, merece respeto: si es de otra persona, se cita con su nombre y no se copia entero. Los textos de esta clase son originales y cortos.",
    ],
    vocab=[("texto dramático", "texto escrito para ser representado, con diálogos y acotaciones"), ("subtexto", "lo que un personaje quiere decir sin decirlo"), ("objeto con sentido", "objeto al que la escena da importancia"), ("cierre", "final de la escena que deja un efecto"), ("pista", "dato del texto que sostiene una inferencia")],
    worked=[
        ("Leer el subtexto", "En un texto, una madre dice: «Qué bien que te va tan bien en la ciudad» mientras guarda el delantal sin mirar a su hijo. ¿Qué puede estar comunicando?", ["Sus palabras son de alegría, pero no lo mira y guarda el delantal en silencio.", "Puede expresar orgullo mezclado con tristeza por la distancia."], "Un sentimiento mezclado que no dice con palabras"),
        ("Formular un propósito", "Pistas: dos personajes hablan del clima y evitan hablar del tema principal; uno se va dejando su bufanda. Propón un propósito.", ["Pista 1: evitan el tema importante. Pista 2: la bufanda queda como señal de que alguien volverá o dejó algo pendiente.", "Propósito: mostrar cómo se evita una conversación difícil."], "Mostrar cómo se evita una conversación difícil"),
    ],
    mistakes=[("Resumir lo que pasa y creer que eso es el propósito.", "El resumen cuenta la historia, no lo que la obra busca comunicar.", "Pregúntate para qué se cuenta y apóyate en pistas."),
              ("Ignorar las acotaciones y el silencio.", "Allí hay mucha información sobre lo que los personajes sienten.", "Subraya acciones, pausas y objetos al leer.")],
    T=[
        ('abc', '¿Qué es una acotación en un texto dramático?', 'Una indicación sobre acciones, gestos, silencios o espacio', 'Una frase que el público repite al final', 'El título que lleva la obra cuando se publica', 'La acotación orienta la puesta; no es parte del diálogo.'),
        ('abc', '{F} ¿Cuál es el conflicto en «La caja»?', 'Una despedida entre dos personas que no se dicen lo que sienten', 'Una discusión por un robo de dinero ocurrido en la oficina esa misma semana', 'La búsqueda de unos documentos perdidos', 'El texto muestra una despedida contenida; no hay robo ni documentos.'),
        ('abc', '{F} En «La caja», ¿qué objeto cobra un sentido especial al final?', 'La llave que David deja sobre el escritorio', 'El abrigo mojado de David', 'Los papeles que ordena Elena', 'La llave deja un cierre y Elena la mira hasta que se cierra la puerta.'),
        ('abc', '{F} Elena dice: «La caja pesa poco. Mejor así». ¿Qué subtexto es razonable?', 'Habla del peso, pero expresa la distancia que hay ahora entre ambos', 'Quiere que David se lleve algo más pesado para no volver nunca más a buscar nada', 'Pide que David le explique por qué se va', 'La frase habla de la caja, pero dice algo sobre la relación y la despedida.'),
        ('abc', 'Para inferir el propósito de un texto dramático, es mejor', 'leerlo dos veces: primero para entender qué pasa y luego cómo pasa', 'leer solo el final para no confundirse con el resto', 'saltarse las acotaciones y concentrarse en el diálogo', 'La segunda lectura permite fijarse en pausas, objetos y subtexto.'),
        ('abc', '{F} Una compañera resume «La caja»: «David va a buscar sus cosas y se va». ¿Qué falta para hablar del propósito?', 'Explicar qué busca comunicar el texto y apoyarlo en pistas', 'Contar la historia con más detalle, indicando qué ocurre en cada momento de la escena', 'Agregar el nombre del actor que lo interpretará', 'El resumen cuenta la historia; el propósito es lo que esa historia busca expresar.'),
        ('=', 'Un texto dramático tiene 6 líneas de diálogo y 2 acotaciones. ¿Qué porcentaje de las partes son acotaciones?', '2*100//(6+2)', 'Se divide el número de acotaciones entre el total de partes y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué pista sostiene la lectura «un adiós contenido»?', 'Las pausas, la frase sobre la caja y la llave que se deja', 'El abrigo mojado que usa David en la oficina y la hora de la noche', 'Que Elena ordene papeles en una oficina vacía', 'Esas tres pistas muestran que la despedida se vive sin decirlo todo.'),
        ('abc', '{F} Un grupo lee «La caja» y propone: «El propósito es mostrar que los edificios de oficinas son tristes». ¿Qué problema tiene?', 'No hay pistas en el texto que lo sostengan', 'Es una opinión incorrecta que nadie puede sostener', 'Es una idea demasiado larga', 'La inferencia sin pistas del texto no puede comprobarse.'),
        ('abc', 'Una estudiante afirma que el texto no tiene propósito porque «no pasa nada». ¿Qué respuesta es adecuada?', 'Pasa algo en lo que se calla y en lo que se hace con los objetos y las pausas', 'Tiene razón, porque una obra necesita acción para tener propósito', 'Debe agregar más personajes para que pase algo', 'Lo que no se dice también comunica; la acción puede ser mínima.'),
        ('abc', 'Dos lectoras dicen: «el texto muestra una despedida» y «el texto muestra enojo contenido». ¿Cuándo son razonables ambas?', 'Cuando cada una cita pistas del texto que las sostienen', 'Nunca, porque solo una de las dos lecturas puede estar en lo correcto', 'Siempre, aunque no citen pistas', 'Ambas lecturas se aceptan si se apoyan en el texto.'),
        ('=', 'En el cierre de un texto dramático hay 2 acciones escritas y una pausa en el diálogo. Si cada acción dura 6 segundos y la pausa 4, ¿cuántos segundos dura el cierre?', '2*6+4', 'Se suman las acciones y la pausa.', ' segundos'),
        ('abc', '{F} Si en «La caja» la llave se dejara en la mano de Elena y ella dijera «gracias», ¿cambiaría el efecto?', 'Sí, porque el gesto y el diálogo dejarían de ser tan contenidos', 'No, porque la llave sigue estando en la escena', 'No, porque las palabras no influyen en el propósito', 'Un cambio en la acción y el diálogo cambia lo que se comunica.'),
    ],
    ctx=('ab', 'Debes defender tu lectura de un texto. ¿Qué pruebas usas?', 'Pistas del texto, como diálogos, acotaciones y objetos', 'Lo que sientes, sin citar nada del texto', 'Una lectura se defiende citando el texto que la sostiene.'),
    sc=[
        ("En Teatro: ¿qué son los diálogos y las acotaciones?", "Los diálogos son lo que dicen los personajes; las acotaciones, indicaciones de acción, gesto o espacio", "Ambos aportan pistas para inferir el propósito de la obra."),
        ("¿Es lo mismo resumir un texto que inferir su propósito?", "No, el resumen cuenta la historia y el propósito dice qué busca comunicar", "El propósito responde para qué se cuenta."),
        ("¿Qué es el subtexto?", "Lo que un personaje quiere decir sin decirlo", "Se lee en pausas, gestos y lo que se calla."),
    ],
    op=("Lee este texto original: «(Una cocina. NICO prepara dos tazas. SOFÍA entra con una maleta.) NICO: Hice té. SOFÍA: No me voy a quedar. (Pausa.) NICO: Igual lo hice. (SOFÍA deja la maleta junto a la puerta y se sienta.)». Escribe: el conflicto, un objeto con sentido, un subtexto y un propósito expresivo apoyado en dos pistas del texto.",
        "Conflicto: ella llega a irse y él quiere que se quede. Objeto con sentido: las dos tazas. Subtexto de «igual lo hice»: quiero que te quedes. Propósito: mostrar cómo se ofrece cuidado cuando alguien decide irse; pistas: las dos tazas y el gesto de dejar la maleta.",
        ["identifica conflicto y objeto", "formula un subtexto", "propone un propósito", "lo apoya en dos pistas del texto"],
        ["hoja con las respuestas"],
        ["resumir en vez de inferir", "no citar pistas"],
        "Pregunta: «¿qué línea o acción del texto sostiene tu idea?». Debe señalarla."),
    reinforce="Escribe un texto de cuatro líneas con una pausa y un objeto con sentido, y pídele a otra persona que infiera su propósito.",
    extend="Explica por qué lo que un personaje calla puede decir más que lo que dice.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (dos puestas de ejemplo del mismo texto «La caja», inventadas). Puesta 1: luz cálida y baja, un silencio largo antes de la llave, vestuario de colores apagados, sin música. "
     "Puesta 2: luz blanca y fuerte, un reloj que suena durante toda la escena, vestuario de colores intensos, música rápida al final.")
build(
    O4, 3, F,
    use="Aprenderé a reconocer cómo los recursos de la puesta en escena (luz, sonido, vestuario, escenografía y objetos) producen ideas, emociones y sensaciones, y cómo cambian el propósito que infiero de una obra.",
    prior=["Sé inferir el propósito con rasgos y pistas.", "Sé que la puesta en escena reúne espacio, objetos, luz y sonido.", "Sé diferenciar hecho e interpretación."],
    explain=[
        "El mismo texto puede transmitir cosas distintas según cómo se pone en escena. La luz cálida y baja sugiere intimidad o recogimiento; la luz blanca y fuerte puede dar sensación de frialdad o de revisión. El sonido también comunica: un silencio largo crea espera; un reloj que suena todo el tiempo marca presión o urgencia; una música rápida acelera la emoción. El vestuario y los colores sugieren estados de ánimo, y la escenografía y los objetos construyen el lugar.",
        "Para analizarlo se usa la secuencia rasgo, efecto, propósito. Se describe el recurso (la luz es cálida y baja), se explica el efecto que produce (crea un ambiente íntimo y silencioso) y se propone qué propósito refuerza (mostrar una despedida contenida). Un recurso no tiene un significado fijo; depende del conjunto de las decisiones. Una luz cálida puede ser acogedora en una obra y asfixiante en otra.",
        "Al comparar dos puestas del mismo texto, se observan qué cambió y qué efecto tuvo cada cambio. No se trata de decir cuál es mejor en general, sino cuál sirve mejor a cierto propósito. Los efectos de luz y sonido de esta clase son descripciones; si el grupo prueba algo en sala, usa la luz del lugar, volumen moderado y nada que produzca fuego ni calor.",
    ],
    vocab=[("puesta en escena", "conjunto de decisiones de espacio, objetos, luz, sonido y movimiento"), ("ambiente", "sensación general que produce la escena"), ("sensación", "efecto físico o emocional que produce un recurso"), ("escenografía", "construcción o disposición del espacio donde ocurre la escena"), ("recurso", "elemento que se usa para comunicar")],
    worked=[
        ("Rasgo, efecto y propósito", "En una puesta, la luz baja y cálida acompaña una conversación entre dos personas mayores. ¿Qué analizas?", ["Rasgo: luz baja y cálida.", "Efecto: ambiente íntimo y tranquilo. Propósito posible: acercar al público a una conversación afectuosa."], "Rasgo, efecto y propósito encadenados"),
        ("Comparar dos puestas", "En una puesta un reloj suena sin parar; en otra hay silencio. ¿Qué cambia?", ["El reloj marca el paso del tiempo y puede generar presión.", "El silencio abre espacio a la espera y a lo no dicho."], "Cambian el ritmo y la sensación: presión en una y espera en la otra"),
    ],
    mistakes=[("Decir que un recurso «siempre» significa lo mismo, como que el rojo es enojo.", "El efecto depende del conjunto de decisiones y del contexto.", "Explica el efecto en esa puesta, con el resto de los recursos."),
              ("Juzgar una puesta como mejor sin decir para qué propósito.", "Una misma decisión sirve a unos propósitos y a otros no.", "Compara según el propósito que se quiere expresar.")],
    T=[
        ('abc', '¿Qué hace la puesta en escena respecto de un texto dramático?', 'Decide cómo se muestra el texto con espacio, objetos, luz, sonido y movimiento', 'Reemplaza el texto por un resumen más corto que se pueda representar en menos tiempo', 'Cambia su autor para adaptarlo al público', 'La puesta es el modo de mostrar el texto; no lo reemplaza ni cambia su autoría.'),
        ('abc', '{F} ¿Qué recurso de la puesta 2 puede transmitir presión o urgencia?', 'El reloj que suena durante toda la escena', 'La luz cálida y baja', 'El silencio largo antes de la llave', 'El sonido constante de un reloj marca el paso del tiempo; los otros recursos son de la puesta 1.'),
        ('abc', '{F} En la puesta 1, ¿qué efecto produce el silencio largo antes de la llave?', 'Crea espera y deja espacio para lo que no se dice', 'Acelera el ritmo de la escena y deja menos espacio para pensar', 'Muestra que los actores olvidaron el texto', 'El silencio sostenido concentra la atención y crea tensión de espera.'),
        ('abc', 'La secuencia «rasgo, efecto, propósito» sirve para', 'explicar cómo un recurso observable apoya lo que la obra busca comunicar', 'adivinar cuánto durará la función y calcular cuántas personas entrarán a verla', 'calificar a las personas que actúan', 'La secuencia conecta lo que se ve con lo que se infiere.'),
        ('abc', '¿Cuál es un ejemplo de análisis con rasgo, efecto y propósito?', 'La luz baja crea un ambiente íntimo, lo que refuerza una conversación afectuosa', 'La luz baja es muy bonita y me gustó mucho más que la luz fuerte de la otra puesta', 'La luz baja se compra en tiendas especializadas', 'El primero describe el recurso, su efecto y el propósito que apoya.'),
        ('abc', '{F} ¿Qué puesta crea más sensación de revisión o frialdad?', 'La puesta 2, por la luz blanca y fuerte', 'La puesta 1, por el vestuario de colores apagados', 'Ninguna, porque no hay diferencias entre ellas', 'La luz blanca y fuerte sugiere frialdad o revisión; la puesta 1 tiene recogimiento.'),
        ('=', 'Una puesta usa 3 cambios de luz y cada cambio dura 4 segundos. Si se hacen 2 funciones, ¿cuántos segundos de cambios de luz se usan en total?', '3*4*2', 'Se multiplican cambios, segundos y funciones.', ' segundos'),
        ('abc', '{F} ¿Qué propósito refuerza mejor la puesta 1?', 'Mostrar una despedida contenida, íntima y silenciosa', 'Mostrar una carrera contra el tiempo', 'Hacer reír con una confusión de relojes que se descomponen en medio de la escena', 'Luz cálida y baja, silencio y colores apagados sostienen intimidad y contención.'),
        ('abc', 'Alguien afirma: «El color rojo siempre significa enojo en las obras». ¿Qué responderías?', 'El efecto depende del conjunto de decisiones y del contexto de cada puesta', 'Tiene razón, porque el color tiene un solo significado universal', 'El rojo solo se usa para mostrar alegría', 'Ningún recurso tiene un significado fijo en todas las puestas.'),
        ('abc', '{F} Un grupo dice: «La puesta 2 es peor que la 1». ¿Qué le falta a esa afirmación?', 'Indicar para qué propósito resulta peor y con qué rasgos lo sostiene', 'Agregar una nota numérica a cada puesta y sumar los puntos de todos los criterios', 'Decir cuál puesta tuvo más público', 'Juzgar sin propósito ni rasgos no permite comparar con fundamento.'),
        ('abc', 'Un grupo quiere probar en sala una luz que produce calor y una vela para dar clima. ¿Qué corresponde?', 'Descartar el calor y la vela, y usar la luz de la sala con otras decisiones', 'Probarlo un minuto, con mucho cuidado y con un adulto cerca, solo para ver cómo se ve', 'Pedir a una persona del público que lo cuide', 'El fuego y el calor son un riesgo; el clima puede lograrse con recursos seguros.'),
        ('=', 'La música rápida de la puesta 2 dura 40 segundos de una escena de 160 segundos. ¿Qué porcentaje de la escena ocupa?', '40*100//160', 'Se divide el tiempo de música entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Si a la puesta 1 se le agrega el reloj constante de la puesta 2, ¿qué ocurre con el efecto?', 'Se mezcla la espera con la presión del tiempo y cambia el propósito percibido', 'No cambia nada, porque el reloj es un sonido y los sonidos no influyen en el propósito', 'Desaparece la luz cálida y baja', 'Un nuevo recurso modifica el conjunto y el efecto que se percibe.'),
    ],
    ctx=('ab', 'Comparas dos puestas de un mismo texto. ¿Qué corresponde analizar?', 'Qué cambió y qué efecto tuvo cada cambio en el propósito', 'Cuál puesta tiene más objetos, sin mirar su efecto', 'Un cambio de recursos tiene sentido por el efecto que produce.'),
    sc=[
        ("En Teatro: ¿qué es la escenografía?", "La construcción o disposición del espacio donde ocurre la escena", "Ayuda a crear el lugar y el ambiente."),
        ("¿Qué significa analizar con «rasgo, efecto, propósito»?", "Describir el recurso, explicar lo que produce y decir qué propósito apoya", "Conecta lo observado con lo que la obra comunica."),
        ("En una prueba en sala, ¿qué se evita en la luz?", "Fuego y fuentes de calor", "Son un riesgo para las personas y el lugar."),
    ],
    op=("Imagina dos puestas de un mismo texto breve sobre un reencuentro: una con luz cálida y música suave y otra con luz fría y silencio total. Escribe, para cada una, un rasgo, su efecto y el propósito que refuerza, y luego una conclusión sobre cuál sirve mejor al propósito «mostrar un reencuentro tenso».",
        "Puesta 1: luz cálida y música suave; efecto, calma y cercanía; refuerza un reencuentro amable. Puesta 2: luz fría y silencio; efecto, distancia y tensión; refuerza un reencuentro tenso. Para ese propósito sirve mejor la puesta 2.",
        ["rasgo, efecto y propósito en cada puesta", "conclusión según el propósito", "no usa significados fijos", "recursos seguros"],
        ["cuadro comparativo con conclusión"],
        ["decir cuál es mejor sin un propósito", "afirmar significados fijos para un color"],
        "Pregunta: «¿mejor para qué propósito?». Debe nombrar el propósito."),
    reinforce="Elige una escena que conozcas por tu vida (sin identificar a nadie) y describe cómo cambiaría con luz fuerte o luz baja.",
    extend="Explica por qué ningún recurso de la puesta en escena tiene un significado fijo.",
)

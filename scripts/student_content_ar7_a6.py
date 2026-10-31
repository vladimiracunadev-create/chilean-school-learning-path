"""Cuaderno del estudiante de 7.º básico Artes Visuales: AR07 OA 06 (caracterizar y apreciar espacios de difusión de las artes visuales: medios presentes, espacio, montaje y público)."""
from __future__ import annotations

from student_content_ar7_a import lesson, m, task, w
from student_lessons import arith, ex

OA6 = "AR07 OA 06"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA6, 1,
    "Una hoja, lápiz y una tabla de cuatro columnas dibujada por ti. Los espacios que se comparan están descritos en esta clase; no necesitas salir de tu casa.",
    "Aprenderé a caracterizar cuatro espacios donde se difunden las artes visuales: museo, galería, espacio público y plataforma digital. Sirve para decidir dónde y cómo mostrar un trabajo.",
    ["Sé que una obra se interpreta con datos de medio, material y contexto.", "Sé que la audiencia influye en lo que muestro."],
    [
        "Difundir una obra es hacerla llegar a un público. Los espacios de difusión son los lugares, físicos o digitales, donde se muestra. Un museo es una institución que conserva, estudia y exhibe colecciones, muchas veces de valor patrimonial. Una galería es un espacio dedicado a exhibir obras, a menudo de artistas vivos, por temporadas, y a veces las obras se venden. El espacio público es la calle, la plaza o el muro de un barrio, donde la obra está a la vista de cualquier persona que pase.",
        "Una plataforma digital es un sitio web o aplicación donde se publican imágenes y videos que se pueden ver desde cualquier lugar con conexión. Cada espacio permite distintos medios de expresión: el museo y la galería muestran pinturas, esculturas e instalaciones con protección; el espacio público acepta murales, esculturas grandes y acciones; la plataforma digital muestra fotografía, video y arte hecho con computador, pero no reemplaza la presencia de un objeto grande o con textura.",
        "Para caracterizar un espacio me pregunto cuatro cosas: ¿qué medios muestra?, ¿cómo es el lugar (cerrado o abierto, grande o pequeño)?, ¿cómo se montan las obras? y ¿quién es su público (quién llega, cuántas personas, por qué)? Con esas respuestas puedo comparar espacios y elegir el más adecuado para un trabajo. No hay un espacio mejor que otro: depende de lo que quiero mostrar y a quién.",
    ],
    [("difusión", "hacer llegar una obra a un público"), ("museo", "institución que conserva, estudia y exhibe colecciones"), ("galería", "espacio dedicado a exhibir obras, a menudo por temporadas"), ("espacio público", "lugar abierto a todas las personas, como una plaza o un muro"), ("plataforma digital", "sitio web o aplicación donde se publican y se ven imágenes")],
    [
        w("Caracterizar un espacio", "Una escultura de piedra de dos metros se muestra en una plaza abierta. ¿En qué espacio de difusión está y quiénes la ven?", ["Una plaza es un espacio público.", "Cualquier persona que pase la puede ver.", "No necesita entrada ni horario."], "En el espacio público; la ve cualquier persona que pase por la plaza"),
        w("Elegir el espacio", "Tienes una fotografía digital que quieres compartir con personas que viven lejos. ¿Qué espacio sirve más?", ["Una plataforma digital llega a personas conectadas.", "Un museo requiere ir al lugar.", "El espacio público llegaría solo a quien pasa."], "La plataforma digital"),
    ],
    [
        m("Pensar que el museo es el único lugar donde se muestra arte.", "Hay galerías, espacio público y plataformas digitales.", "Compara los cuatro espacios según lo que quieres mostrar."),
        m("Decir que la plataforma digital reemplaza ver una obra grande en persona.", "Una pantalla no muestra el tamaño, el peso ni la textura real.", "Considera qué se pierde al ver una obra en pantalla."),
    ],
    [
        ex("Una calle con un mural en un muro es un espacio: ¿público o de museo?", "Público", "Está abierto a cualquier persona que pase."),
        ex("Un espacio que conserva y exhibe colecciones de valor patrimonial se llama: A. museo B. galería.", "A", "El museo conserva, estudia y exhibe colecciones."),
        ex("Un sitio web donde se publican imágenes y videos es un espacio: ¿físico o digital?", "Digital", "Se ve a través de pantallas y conexión."),
    ],
    [
        ex("¿Qué espacio muestra obras a menudo por temporadas y a veces las vende: museo o galería?", "Galería", "La galería suele hacer exhibiciones temporales."),
        ex("Una persona sin conexión a internet quiere ver una obra. ¿Qué espacio no le sirve? A. plataforma digital B. espacio público", "A", "La plataforma digital necesita conexión."),
        ex("Un mural grande pintado en un muro de barrio llega más fácilmente a: A. cualquier persona que pase B. solo a quien compra una entrada", "A", "El espacio público es abierto y no requiere entrada."),
    ],
    [
        ex("Tienes una escultura de cartón de tres metros. ¿Qué espacio la muestra mejor: una sala amplia de galería o una pantalla de teléfono?", "Una sala amplia de galería", "Una pantalla pierde el tamaño real."),
        ex("Quieres mostrar una fotografía a personas de otra ciudad sin viajar. ¿Qué espacio eliges: plataforma digital o galería de tu barrio?", "Plataforma digital", "Llega a personas lejanas."),
        arith("Un museo tiene 4 salas con 12 obras cada una. ¿Cuántas obras exhibe?", "4*12", "Se multiplican salas por obras."),
    ],
    [
        ex("Un compañero dice: «Mi mural no vale porque está en la calle y no en un museo». ¿Qué le dirías? A. Que el espacio público también es un espacio de difusión válido B. Que solo los museos importan", "A", "Cada espacio tiene sus características y no hay uno mejor."),
        ex("Una obra de arte textil muy delicada, ¿es más adecuado mostrarla en un museo con control de luz o en un muro de calle bajo el sol?", "En un museo con control de luz", "El museo puede proteger los materiales delicados."),
    ],
    [
        ex("Quieres mostrar una instalación de 30 sillas en círculo que se recorre. ¿Qué espacio conviene: una sala amplia de galería o una pantalla de 15 cm?", "Una sala amplia de galería", "Se necesita espacio para recorrerla."),
        ex("Quieres que tu dibujo lo vean muchas personas sin pagar y de paso. ¿Qué eliges? A. Un muro de plaza autorizado B. Una sala cerrada con entrada", "A", "El espacio público llega a quienes pasan sin entrada."),
    ],
    ex("Un video corto sobre una planta que crece en 30 días. ¿Qué espacio difunde mejor ese medio a muchas personas lejanas? A. plataforma digital B. escultura en plaza", "A", "El video se difunde bien en una plataforma digital."),
    [
        ex("En Artes Visuales, ¿qué es difundir una obra?", "Hacerla llegar a un público", "Es mostrarla a otras personas."),
        ex("Verdadero o falso: hay un espacio de difusión mejor que todos los demás.", "Falso", "Depende de lo que se quiere mostrar y a quién."),
        ex("¿Qué cuatro espacios se caracterizan en esta clase?", "Museo, galería, espacio público y plataforma digital", "Son los cuatro que se comparan."),
    ],
    task(
        "Elige UN trabajo para difundir. A) Una escultura de cartón de tres metros. B) Una fotografía digital que quieres mostrar a personas lejanas. C) Un mural pequeño sobre el cuidado del agua. Completa una tabla con los cuatro espacios (museo, galería, espacio público, plataforma digital) y para cada uno anota medios que muestra, cómo es el lugar y quién es el público. Elige el más adecuado y explica por qué.",
        "Elegí la B. Museo: pinturas y esculturas, lugar cerrado, público que visita. Galería: obras de temporada, lugar cerrado, público interesado. Espacio público: murales, abierto, quienes pasan. Plataforma digital: foto y video, sin lugar físico, personas conectadas. Elijo la plataforma digital porque llega a personas lejanas.",
        ["completa la tabla de cuatro espacios", "anota medios, lugar y público", "elige uno con una razón", "no dice que un espacio es siempre mejor"],
        ["tabla completa", "elección con razón"],
        ["decir que solo el museo importa", "elegir sin justificar"],
        "Destaca la razón de la elección y pregunta qué pierde el trabajo en ese espacio.",
    ),
    "Mira un lugar cercano a tu casa donde se podría mostrar una obra y di si es cerrado o abierto y quién lo vería.",
    "Escribe qué espacio elegirías para un video de 30 segundos y qué espacio elegirías para una escultura grande, con una razón para cada uno.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA6, 2,
    "Una hoja, lápiz, regla o cinta de medir de casa y un papel grande para hacer un plano. Los datos de las salas están escritos en esta clase.",
    "Aprenderé a relacionar el espacio, el montaje y la audiencia: cómo la altura, la luz, la distancia y el recorrido cambian lo que el público ve y siente. Sirve para organizar una exhibición.",
    ["Sé caracterizar museo, galería, espacio público y plataforma digital.", "Sé que el lenguaje visual produce efectos."],
    [
        "El montaje es la manera de instalar y ordenar las obras en un espacio. Incluye la altura a la que se cuelgan, la distancia entre ellas, la luz, el recorrido que seguirá el público y los textos. Una guía usada en muchas salas es poner el centro de la obra a unos 1,5 metros del suelo, cerca de la altura de los ojos de un adulto, y dejar espacio entre obras para que cada una se vea sola.",
        "El espacio influye en la lectura. Una obra pequeña en una sala amplia se siente delicada; la misma obra rodeada de muchas otras se pierde. Una luz dirigida destaca; una luz plana permite ver todo. Un recorrido libre invita a explorar; uno guiado cuenta una historia en orden. Pensar en la audiencia también cambia el montaje: para niños pequeños se baja la altura; para personas en silla de ruedas se deja espacio ancho y una altura que puedan ver bien.",
        "Para planificar un montaje hago un plano simple: dibujo la sala desde arriba, marco la entrada y ubico las obras con números. Anoto la altura del centro de cada obra y el recorrido con una flecha. Después me pregunto: ¿qué verá primero el público?, ¿dónde puede detenerse?, ¿se cruzan las personas? y ¿se ven todas las obras sin que una tape a otra? Ajusto lo que no funcione.",
    ],
    [("montaje", "forma de instalar y ordenar las obras en un espacio"), ("recorrido", "camino que sigue el público dentro del espacio"), ("audiencia", "personas que miran la exhibición"), ("plano", "dibujo de la sala vista desde arriba"), ("altura de ojos", "nivel al que mira un adulto, cerca de 1,5 metros")],
    [
        w("Calcular una altura", "Una pintura mide 60 cm de alto y quieres que su centro quede a 150 cm del suelo. ¿A qué altura queda su borde inferior?", ["La mitad de 60 cm es 30 cm.", "El borde inferior queda 30 cm bajo el centro.", "150 menos 30 es 120."], "120 cm del suelo"),
        w("Adaptar a la audiencia", "Tu exhibición es para niños de 5 años. ¿Qué cambias respecto de un montaje para adultos?", ["Los niños miran desde más abajo.", "Bajo la altura de las obras.", "Pongo los textos cerca y grandes."], "Bajar la altura de las obras y poner los textos cerca y grandes"),
    ],
    [
        m("Colgar todas las obras a la misma altura sin pensar en quién las verá.", "No todas las personas ven desde la misma altura.", "Piensa en la audiencia y ajusta la altura y el espacio."),
        m("Juntar muchas obras para «llenar» la pared.", "Las obras se tapan o se pierden unas a otras.", "Deja espacio entre ellas para que cada una se vea sola."),
    ],
    [
        ex("¿Cómo se llama el dibujo de la sala vista desde arriba: plano o recorrido?", "Plano", "Muestra dónde va cada obra."),
        ex("La altura de ojos de un adulto es cerca de: A. 1,5 metros B. 3 metros", "A", "Es el nivel al que se suele mirar una obra."),
        ex("Dejar espacio entre las obras, ¿ayuda a que se vea cada una sola? ¿Sí o no?", "Sí", "Evita que se tapen entre sí."),
    ],
    [
        ex("Una sala tiene luz plana y pareja. ¿Qué permite: ver todo con claridad o destacar una sola obra?", "Ver todo con claridad", "La luz plana ilumina por igual."),
        ex("Una exhibición para niños pequeños. ¿Qué haces con la altura de las obras? A. Bajarlas B. Subirlas", "A", "Los niños miran desde más abajo."),
        ex("Para que una persona en silla de ruedas pueda ver, ¿qué debe tener el recorrido? A. espacio ancho entre obras B. pasillos muy angostos", "A", "Necesita espacio para desplazarse y ver."),
    ],
    [
        arith("Una pintura mide 80 cm de alto y quieres que su centro quede a 150 cm del suelo. ¿A qué altura queda su borde superior?", "150+40", "La mitad de 80 es 40; el borde superior queda 40 cm sobre el centro."),
        arith("Una pared mide 7 m. Quieres colgar 3 obras de 1 m de ancho, con el mismo espacio entre ellas y sin dejar espacio en los extremos. ¿Cuántos metros de espacio queda entre una obra y la siguiente?", "(7-3)/2", "Quedan 4 m libres repartidos en 2 espacios iguales."),
        ex("Quieres que el público conozca primero una obra grande y luego las pequeñas. ¿Qué haces con el recorrido? A. Ubicas la grande a la entrada B. La ubicas al fondo", "A", "El recorrido debe llevar a la grande primero."),
    ],
    [
        ex("Un montaje junta 10 obras en una pared de 2 metros. ¿Qué problema probable tiene?", "Las obras se tapan o se pierden unas a otras", "Hay muy poco espacio entre ellas."),
        ex("Un museo cuelga todo a 2 metros de altura. Una persona de 12 años dice que no ve bien. ¿Qué decisión de montaje falló?", "La altura no consideró a toda la audiencia", "El centro debía estar cerca de la altura de ojos."),
    ],
    [
        ex("Tu exhibición cuenta una historia de la mañana a la noche. ¿Qué tipo de recorrido conviene: guiado en orden o libre sin flechas?", "Guiado en orden", "Una historia necesita un orden de lectura."),
        arith("Tienes 8 obras y las repartes por igual en 2 paredes. ¿Cuántas obras hay por pared?", "8/2", "Se reparten por igual."),
    ],
    ex("Una sala tiene una entrada y una puerta de salida. Colocas las obras 1 a 5 en orden desde la entrada, en el sentido de las agujas del reloj. ¿Qué dibujo ayuda a planificar este recorrido? A. un plano con flechas y números B. una lista sin dibujo", "A", "El plano muestra el orden y el camino."),
    [
        ex("En Artes Visuales, ¿qué es el montaje?", "La forma de instalar y ordenar las obras en un espacio", "Incluye altura, luz, distancia y recorrido."),
        ex("Verdadero o falso: todas las personas ven bien desde la misma altura.", "Falso", "Depende de la edad y de la audiencia."),
        ex("¿Para qué sirve el plano?", "Para planificar dónde va cada obra y el recorrido", "Muestra la sala desde arriba."),
    ],
    task(
        "Elige UNA sala. A) Una sala de 6 m de largo para 4 pinturas de 80 cm de alto. B) Una sala pequeña para niños de 5 años con 5 dibujos. C) Un pasillo de 8 m para una historia en 6 imágenes. Haz un plano desde arriba con la entrada, el orden de las obras con números, flechas de recorrido y la altura del centro de cada obra. Explica una decisión pensando en la audiencia.",
        "Elegí la B. Plano: entrada a la izquierda; cinco dibujos con números del 1 al 5 en la pared del fondo; flecha de recorrido de izquierda a derecha. Altura del centro: 100 cm, porque los niños miran desde más abajo. Textos grandes y cerca de cada dibujo.",
        ["hace un plano con entrada y números", "indica recorrido y altura", "explica una decisión por la audiencia", "deja espacio entre obras"],
        ["plano", "explicación de la decisión"],
        ["colgar a la misma altura para todos", "juntar demasiado las obras"],
        "Destaca la decisión mejor relacionada con la audiencia y pregunta qué cambiaría si el público fuera distinto.",
    ),
    "Mide con una regla o con tus manos la altura de tus ojos y la de una persona mayor de tu casa; di qué cambiaría en un montaje.",
    "Dibuja el plano de tu pieza como si fuera una galería con tres obras y marca el recorrido.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA6, 3,
    "Una hoja y lápiz. Las situaciones de museo y plataforma que se analizan están escritas en esta clase.",
    "Aprenderé qué es la mediación, el acceso y el cuidado en los espacios de difusión. Sirve para que más personas puedan disfrutar una obra y para que la obra se conserve.",
    ["Sé relacionar espacio, montaje y audiencia.", "Sé que una obra puede ser frágil."],
    [
        "La mediación son las acciones que ayudan al público a comprender una obra: las cartelas con datos, las visitas guiadas, los talleres, los folletos y las preguntas que invitan a mirar. Una buena mediación no dice cómo debe sentirse la persona; le da pistas y preguntas para mirar mejor. Los textos deben ser claros, con letra legible y vocabulario simple.",
        "El acceso es la posibilidad real de llegar, entrar y entender. Incluye el costo de la entrada, los horarios, la ubicación, las rampas y los ascensores para personas con movilidad reducida, los textos grandes o en relieve para personas con baja visión y la información en lenguaje claro. Una plataforma digital también necesita acceso: textos descriptivos de las imágenes, que los lectores de pantalla (programas que leen en voz alta) pueden decir, buen contraste y que se pueda usar sin internet muy rápido.",
        "El cuidado, o conservación, protege las obras: se limita la luz fuerte porque puede desteñir papeles y telas, se evita la humedad, se mantiene una distancia y se pide no tocar. Una huella puede dañar una superficie delicada. En el espacio público el cuidado es de toda la comunidad: no rayar ni pegar encima de un mural. Acceso y cuidado se equilibran: se busca que muchas personas lo disfruten sin dañar la obra.",
    ],
    [("mediación", "acciones que ayudan al público a comprender una obra"), ("acceso", "posibilidad real de llegar, entrar y entender un espacio"), ("conservación", "cuidado que protege las obras del daño"), ("cartela", "texto corto junto a la obra con sus datos"), ("baja visión", "dificultad para ver aunque se usen lentes")],
    [
        w("Mejorar el acceso", "Un museo tiene una escalera sin rampa. ¿Qué personas quedan sin acceso y qué se puede hacer?", ["Quedan fuera personas con movilidad reducida o con coches.", "Se puede instalar una rampa o un ascensor.", "Mientras tanto, se ofrece una visita virtual."], "Se pierde el acceso de personas con movilidad reducida; se soluciona con rampa o ascensor"),
        w("Equilibrar acceso y cuidado", "Una pintura en papel se destiñe con la luz. ¿Cómo permites que se vea y se cuide?", ["Reduzco la luz fuerte.", "Pongo un cordón de distancia.", "Ofrezco una copia digital para mirar de cerca."], "Con poca luz, un cordón de distancia y una copia digital para verla de cerca"),
    ],
    [
        m("Pensar que cuidar una obra es prohibir que alguien la vea.", "El cuidado busca que la obra dure para que más personas la disfruten.", "Equilibra acceso y cuidado con distancia, luz moderada y copias para tocar."),
        m("Escribir cartelas con palabras difíciles para que «se vea serio».", "Dificulta el acceso al público.", "Usa un lenguaje claro y letra legible."),
    ],
    [
        ex("Una visita guiada es parte de: A. mediación B. conservación", "A", "Ayuda a comprender la obra."),
        ex("¿Una rampa para quien no puede subir escaleras mejora el acceso o la conservación?", "El acceso", "Permite llegar al espacio."),
        ex("Pedir no tocar la obra protege su: ¿acceso o conservación?", "Conservación", "Evita dañar la superficie."),
    ],
    [
        ex("Una cartela con letra muy chica y palabras difíciles. ¿Qué falla? A. la mediación y el acceso B. la conservación de la obra", "A", "No se entiende ni se lee bien."),
        ex("Un museo cobra una entrada que muchas familias no pueden pagar. ¿Qué dimensión afecta?", "El acceso", "El costo limita quién puede entrar."),
        ex("La luz fuerte puede desteñir papeles y telas. ¿Cuál es una medida de conservación? A. bajar la luz sobre esas obras B. subir la luz sobre esas obras", "A", "La luz fuerte daña los materiales delicados."),
    ],
    [
        ex("Una plataforma digital muestra imágenes sin descripción de texto. ¿A quién deja sin acceso?", "A personas con baja visión que usan lectores de pantalla", "Sin descripción, el lector no puede explicar la imagen."),
        arith("Un museo recibe 40 personas en cada visita guiada y hace 3 visitas al día. ¿Cuántas personas recibe en un día?", "40*3", "Se multiplican las personas por visita por las visitas."),
        ex("Un mural en un barrio aparece con rayas de plumón. ¿Quién tiene la responsabilidad de cuidarlo en un espacio público? A. toda la comunidad B. solo el museo", "A", "El espacio público se cuida entre todas las personas."),
    ],
    [
        ex("Una exposición de dibujos delicados mantiene la luz baja y la entrada es gratuita, con rampa. ¿Equilibra acceso y cuidado?", "Sí", "La luz baja cuida y la rampa con entrada gratuita facilita el acceso."),
        ex("Una exposición es muy cuidada, pero los horarios son solo en la mañana de días de semana y el costo es alto. ¿Qué dimensión es débil?", "El acceso", "Muchas personas no podrían asistir."),
    ],
    [
        ex("Una escuela organiza una exposición con textos grandes, una rampa, un cordón de distancia y luz moderada. ¿Cuántas medidas de acceso y cuidado se mencionan?", "Cuatro", "Son textos grandes, rampa, cordón y luz moderada."),
        ex("Quieres que una persona con baja visión disfrute una escultura. ¿Qué mediación ayuda? A. una réplica que se pueda tocar con permiso B. un cartel pequeño", "A", "Tocar una réplica permite conocer la forma sin dañar el original."),
    ],
    ex("Un museo debe elegir cómo mostrar un textil antiguo muy frágil. ¿Cuál cuida y da acceso? A. vitrina con luz suave y copia digital ampliada B. colgarlo al sol de un patio", "A", "La vitrina protege y la copia digital permite verlo de cerca."),
    [
        ex("En Artes Visuales, ¿qué es la mediación?", "Acciones que ayudan al público a comprender una obra", "Incluye cartelas y visitas."),
        ex("Verdadero o falso: cuidar una obra significa que nadie pueda verla.", "Falso", "Se busca equilibrar cuidado y acceso."),
        ex("¿Qué debe tener un texto de cartela?", "Lenguaje claro y letra legible", "Facilita comprender la obra."),
    ],
    task(
        "Elige UN caso. A) Un museo con una escalera sin rampa que guarda dibujos delicados. B) Una plataforma digital con imágenes de murales sin descripción de texto. C) Una escuela que arma una exposición de pinturas en papel en el patio. Escribe una medida de mediación, una de acceso y una de conservación, y explica cómo las equilibras.",
        "Elegí la C. Mediación: una cartela de dos líneas junto a cada pintura. Acceso: entrada gratuita y una ruta sin escalones. Conservación: ponerlas bajo techo, lejos del sol directo. Equilibrio: están a la vista del curso pero protegidas de la luz.",
        ["escribe una medida de cada tipo", "explica el equilibrio entre acceso y cuidado", "usa lenguaje claro", "no propone prohibir sin alternativa"],
        ["tres medidas escritas", "explicación del equilibrio"],
        ["cuidar impidiendo ver", "dar acceso sin proteger la obra"],
        "Destaca la medida mejor justificada y pregunta qué cambiaría para otro público.",
    ),
    "Escribe en una hoja una cartela de dos líneas para un objeto de tu casa, con lenguaje claro y letra grande.",
    "Escribe una medida de acceso para una plataforma digital y una para una calle con un mural.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA6, 4,
    "Una hoja, lápiz y lápices de colores. Los trabajos y las audiencias de partida están descritos en esta clase.",
    "Aprenderé a diseñar una difusión pertinente para un trabajo: elegir espacio, montaje, mediación, acceso y cuidado según el medio y la audiencia. Sirve para mostrar mi obra de forma adecuada.",
    ["Sé caracterizar espacios de difusión.", "Sé relacionar montaje, audiencia, acceso y cuidado."],
    [
        "Una difusión pertinente es la que se ajusta al trabajo y a su público. Parte de tres preguntas: ¿qué medio de expresión tiene mi trabajo y qué necesita?, ¿a quién quiero llegar? y ¿qué espacio y qué montaje permiten que se entienda mejor? No es lo mismo difundir una pintura frágil que un mural, ni un video que una escultura de cartón. El medio y el material fijan lo que se puede hacer.",
        "Con eso diseño un plan simple de seis partes: espacio elegido, montaje (altura, distancia, recorrido), mediación (cartela o pregunta), acceso (horario, costo, textos claros), cuidado (luz, distancia, no tocar) y evaluación (cómo sabré si funcionó). Por ejemplo, para una serie de dibujos en papel para el curso: la sala de clases, a la altura de ojos, con una cartela de tres líneas, entrada libre, lejos del sol y una pregunta de opinión al final.",
        "Un plan se revisa con la audiencia: pido a alguien que recorra mi montaje y anote qué entendió, qué no vio y qué le costó. Con esos datos ajusto. Un buen plan es simple, realista con los materiales y el tiempo disponibles, y respeta la autoría y la privacidad: no muestro datos personales ni imágenes de personas sin permiso.",
    ],
    [("pertinente", "adecuado al trabajo y a su público"), ("plan de difusión", "organización de espacio, montaje, mediación, acceso, cuidado y evaluación"), ("evaluación", "forma de comprobar si el plan funcionó"), ("medio y material", "tipo de obra y de qué está hecha"), ("público objetivo", "personas a las que quiero llegar")],
    [
        w("Armar el plan", "Tienes tres dibujos en papel, delicados, para tu curso. Diseña los seis puntos del plan.", ["Espacio: la sala de clases.", "Montaje: a la altura de ojos, con espacio entre dibujos.", "Mediación: cartela de tres líneas.", "Acceso: entrada libre en recreo.", "Cuidado: lejos del sol y sin tocar.", "Evaluación: preguntar qué entendieron."], "Sala de clases, altura de ojos, cartela, entrada libre, lejos del sol y una pregunta final"),
        w("Detectar un plan poco pertinente", "Un compañero quiere colgar su papel delicado en la reja de la calle, bajo el sol, para que todos lo vean. ¿Qué falla?", ["El sol desteñirá el papel.", "La lluvia lo dañará.", "Hay que cambiar el espacio o el material."], "Falla el cuidado: el sol y la lluvia dañan el papel; conviene un lugar bajo techo o una copia"),
    ],
    [
        m("Elegir el espacio más grande o más famoso sin pensar en el trabajo.", "El mejor espacio es el que se ajusta al medio y a la audiencia.", "Parte de las preguntas sobre el trabajo y el público."),
        m("Armar el plan sin pensar en cómo comprobar si funcionó.", "No se sabe si el público entendió.", "Incluye una evaluación simple, como una pregunta al final."),
    ],
    [
        ex("¿Cuántas partes tiene el plan de difusión de esta clase?", "Seis", "Son espacio, montaje, mediación, acceso, cuidado y evaluación."),
        ex("Una difusión pertinente se ajusta al trabajo y a su: A. público B. precio", "A", "Pertinente es adecuado al trabajo y a su audiencia."),
        ex("La evaluación del plan sirve para: A. comprobar si el público entendió B. aumentar el costo", "A", "Muestra si el plan funcionó."),
    ],
    [
        ex("Una pintura delicada en papel, ¿conviene mostrarla bajo techo o a la intemperie?", "Bajo techo", "El sol y la lluvia la dañarían."),
        ex("Un mural enorme sobre un muro autorizado de barrio, ¿qué espacio le corresponde: espacio público o galería?", "Espacio público", "Es una obra grande hecha para el muro."),
        ex("Un video corto para personas conectadas lejos. ¿Qué espacio lo muestra mejor: plataforma digital o plaza?", "Plataforma digital", "Llega a personas lejanas con conexión."),
    ],
    [
        ex("Tu plan dice «cartela con tres líneas». ¿A qué parte del plan pertenece? A. mediación B. cuidado", "A", "La cartela ayuda a comprender."),
        arith("Cuelgas 6 dibujos en 2 filas iguales. ¿Cuántos dibujos hay por fila?", "6/2", "Se reparten por igual."),
        ex("Quieres que una persona con baja visión pueda apreciar tu exposición. ¿Qué agregas al plan? A. textos grandes y una descripción oral B. un cartel más pequeño", "A", "Los textos grandes y la descripción facilitan el acceso."),
    ],
    [
        ex("Dos planes para mostrar una serie de fotografías impresas. El primero las cuelga en una pared al sol; el segundo las pone en una pared interior con luz suave. ¿Cuál cuida mejor las fotos?", "El segundo", "La luz suave protege el papel."),
        ex("Un estudiante quiere subir la imagen de un compañero a una red abierta sin pedirle permiso. ¿Qué principio no respeta?", "La privacidad y la autoría", "Se necesita permiso de la persona que aparece."),
    ],
    [
        ex("Tu trabajo es una escultura de cartón de dos metros. ¿Qué espacio y montaje escoges? A. sala amplia o patio techado con espacio para rodearla B. una vitrina pequeña", "A", "Una escultura grande necesita espacio para recorrerla."),
        arith("Tu plan de difusión tiene 6 partes y ya escribiste 4. ¿Cuántas partes te faltan?", "6-4", "Se resta lo escrito del total."),
    ],
    ex("Quieres mostrar tres pinturas de formato mediano a niños de 8 años. ¿Qué decisión de montaje es pertinente? A. colgarlas bajas y con cartelas con preguntas B. colgarlas muy altas con texto difícil", "A", "La altura baja y las preguntas se ajustan al público infantil."),
    [
        ex("En Artes Visuales, ¿qué es una difusión pertinente?", "La que se ajusta al trabajo y a su público", "Considera medio, material y audiencia."),
        ex("Verdadero o falso: el mejor espacio es siempre el museo.", "Falso", "Depende del trabajo y la audiencia."),
        ex("¿Qué se hace para comprobar si el plan funcionó?", "Evaluar con una pregunta o una observación", "Así se puede ajustar el plan."),
    ],
    task(
        "Elige UN trabajo. A) Tres dibujos en papel delicado para tu curso. B) Un video corto de 30 segundos para personas de otra ciudad. C) Una escultura de cartón de dos metros para la comunidad del colegio. Completa los seis puntos del plan (espacio, montaje, mediación, acceso, cuidado, evaluación) con decisiones concretas y una razón para el espacio elegido.",
        "Elegí la C. Espacio: patio techado. Montaje: la escultura al centro, con espacio para rodearla. Mediación: una cartela con título y una pregunta. Acceso: horario en recreo, entrada libre y una ruta sin escalones. Cuidado: lejos de la lluvia y con un cordón a un metro. Evaluación: preguntar a tres personas qué les llamó la atención. Razón: el patio techado tiene espacio y la protege.",
        ["completa los seis puntos del plan", "elige el espacio con razón", "considera audiencia y cuidado", "respeta autoría y privacidad"],
        ["plan de seis puntos", "razón del espacio"],
        ["elegir el espacio sin pensar en el trabajo", "olvidar la evaluación"],
        "Destaca la decisión mejor relacionada con el medio y pregunta qué cambiaría con otra audiencia.",
    ),
    "Cuenta a una persona de tu casa dónde mostrarías una obra tuya y por qué ese lugar es el adecuado.",
    "Escribe un segundo plan para el mismo trabajo pero con otra audiencia y explica qué cambia.",
)

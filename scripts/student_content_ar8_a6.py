"""Cuaderno del estudiante de 8.º básico Artes Visuales: AR08 OA 06 (comparar y valorar espacios de difusión de las artes visuales y su aporte a la comunidad)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA6 = "AR08 OA 06"


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
    OA6, 1,
    "Hojas, lápiz y, si los tienes, trozos de cartón para tarjetas. Los tres espacios de ejemplo están descritos en esta clase; no necesitas buscarlos.",
    "Aprenderé a describir un espacio de difusión de las artes visuales con cinco criterios: medios de expresión, espacio, montaje, público y aporte a la comunidad. Sirve para compararlos con orden y tomar ideas para mi propia exposición sin copiar.",
    ["Sé que un referente se reinterpreta y no se copia.", "Sé separar lo que se ve de lo que opino."],
    [
        "Un espacio de difusión es un lugar, físico o virtual, donde las obras se muestran al público. Hay museos, galerías, centros culturales, muros y plazas, ferias y galerías en línea. Cada uno presenta las obras de manera distinta y llega a públicos distintos.",
        "Para compararlos uso cinco criterios. Los medios de expresión presentes son los tipos de obra que se muestran, como pintura, escultura, fotografía, video o instalación. El espacio es cómo es el lugar. El montaje es cómo se disponen las obras. El público son las personas que lo visitan. El aporte a la comunidad es el beneficio que deja a las personas de su entorno, como acceso a la cultura, encuentro o aprendizaje.",
        "Observo sin copiar: de un espacio puedo tomar un recurso, como poner una etiqueta junto a cada obra, y usarlo en mi propio espacio con cambios. Describo primero lo que veo, sin decir cuál es mejor. Y no generalizo: un espacio de ejemplo no representa a todos los museos ni a todas las galerías.",
    ],
    [("espacio de difusión", "lugar, físico o virtual, donde las obras se muestran al público"), ("montaje", "manera de disponer las obras en un espacio"), ("público", "personas que visitan o ven un espacio"), ("aporte a la comunidad", "beneficio que un espacio deja a las personas de su entorno"), ("virtual", "que existe en una pantalla y no en un lugar físico")],
    [
        w("Describir un espacio", "Sala de museo de ejemplo: pinturas y esculturas, sala cerrada con iluminación, obras a la altura de la vista con una etiqueta al lado, entrada con horario y visitas de cursos escolares. Descríbela con los cinco criterios.", ["Medios de expresión: pintura y escultura.", "Espacio: sala cerrada con iluminación.", "Montaje: obras a la altura de la vista con etiqueta al lado.", "Público: visitantes con horario, entre ellos cursos escolares.", "Aporte a la comunidad: pendiente; la descripción no lo dice."], "Cuatro criterios descritos y el aporte a la comunidad pendiente"),
        w("Copia o reinterpretación", "Del museo de ejemplo se toma el recurso de la etiqueta junto a cada obra. Ana arma en su casa una sala idéntica a la del museo de ejemplo. Bruno pone tarjetas con título y materiales junto a sus dibujos en un pasillo. ¿Quién copia y quién reinterpreta?", ["Ana repite todo el espacio.", "Bruno toma solo el recurso de la etiqueta y lo adapta a su espacio."], "Ana copia; Bruno reinterpreta"),
    ],
    [
        m("Pensar que un espacio de ejemplo muestra cómo son todos los museos o todas las galerías.", "Cada espacio tiene sus propias decisiones y público.", "Habla solo del espacio descrito."),
        m("Decir cuál espacio es mejor antes de describirlos con los criterios.", "La opinión viene sin evidencia.", "Describe primero con los cinco criterios y luego valora."),
    ],
    [
        ex("¿Qué es un espacio de difusión? A. Un lugar, físico o virtual, donde las obras se muestran al público B. Un taller donde se pintan las obras.", "A", "Su función es mostrar las obras a las personas."),
        ex("Una galería en línea, ¿es un espacio físico o virtual?", "Virtual", "Existe en una pantalla y no en un lugar físico."),
        ex("El criterio que se refiere a las personas que visitan un espacio, ¿cuál es?", "El público", "Habla de quiénes lo visitan."),
    ],
    [
        ex("Un mural en un muro exterior de una plaza no tiene horario de visita. ¿Qué ventaja tiene para el público? A. Lo ve cualquier persona que pasa B. Solo lo ven quienes pagan entrada.", "A", "Un muro exterior sin horario está a la vista de quien pasa."),
        ex("En el muro exterior de la plaza no hay etiquetas y el mural ocupa toda la pared. ¿Qué criterio describe eso?", "El montaje", "Dice cómo se disponen las obras."),
        ex("Una compañera dice que la sala del museo de ejemplo muestra cómo son todos los museos. ¿Qué error comete?", "Generaliza a todos los museos desde un solo espacio", "Un espacio solo muestra sus propias decisiones."),
    ],
    [
        arith("La sala del museo de ejemplo muestra 12 pinturas y 5 esculturas. ¿Cuántas obras muestra en total?", "12+5", "Se suman las obras de los dos tipos."),
        ex("Une cada dato con su criterio. a) «Hay pinturas y esculturas». b) «Es una sala cerrada con iluminación». c) «La visitan cursos escolares». Criterios: 1 medios de expresión, 2 espacio, 3 público. Escribe cada letra con su número.", "a-1, b-2, c-3", "Cada dato responde a un criterio distinto."),
        ex("Quieres tomar el recurso de pintar con otras personas, del mural de la plaza. ¿Qué plan lo reinterpreta? A. Invitar a dos compañeros a pintar contigo un panel de cartón con un tema propio y citar el mural B. Pintar en tu pared el mismo mural de ejemplo.", "A", "Adapta el recurso con tema propio y reconoce su origen."),
    ],
    [
        ex("El muro exterior de la plaza y una galería en línea de fotografías y videos: ¿cuál puede ser vista por alguien que no sale de su casa, si tiene conexión?", "La galería en línea", "Es un espacio virtual accesible desde cualquier lugar con conexión."),
        ex("Un muro de plaza no tiene etiquetas y la sala del museo sí. ¿Cuál tiene un montaje con etiqueta junto a cada obra?", "La sala del museo", "La descripción del muro no menciona etiquetas."),
    ],
    [
        ex("El mural de la plaza lo pintaron vecinos y jóvenes del sector. ¿Qué aporte a la comunidad muestra ese dato? A. La participación de los vecinos en su espacio B. Un horario de visitas.", "A", "Los vecinos participaron en su propio espacio."),
        ex("La ficha dice que la galería en línea se ve desde cualquier lugar. ¿Qué dato falta para valorar su aporte a la comunidad?", "Si las personas de la comunidad tienen conexión para verla", "Verse desde cualquier lugar no asegura que todos tengan acceso."),
    ],
    ex("Tu curso hará una exposición en el pasillo y tiene de referente la sala del museo de ejemplo. ¿Qué plan reinterpreta y cita? A. Poner obras a la altura de la vista, una etiqueta junto a cada una y anotar que la idea viene del museo de ejemplo B. Copiar toda la sala del museo.", "A", "Toma un recurso, lo adapta y lo cita."),
    [
        ex("¿Cuáles son los cinco criterios para describir un espacio de difusión?", "Medios de expresión, espacio, montaje, público y aporte a la comunidad", "Son los criterios de la clase."),
        ex("Verdadero o falso: un espacio de ejemplo muestra cómo son todos los museos.", "Falso", "Cada espacio tiene sus propias decisiones."),
        ex("¿Qué es el montaje?", "La manera de disponer las obras en un espacio", "Incluye altura, orden y etiquetas."),
    ],
    task(
        "Elige UN espacio de ejemplo. A) Sala de museo: pinturas y esculturas, sala cerrada con iluminación, obras a la altura de la vista con etiqueta, entrada con horario, visitas escolares. B) Muro exterior de una plaza: mural pintado por vecinos y jóvenes, sin horario, sin etiquetas, lo ve quien pasa. C) Galería en línea: fotografías y videos de estudiantes, se ve desde cualquier lugar con conexión, con un texto breve junto a cada obra. Haz una tabla con los cinco criterios (marca «pendiente» lo que no se dice) y dibuja un boceto de tu propio espacio que reinterprete un recurso, citando de dónde viene.",
        "Elegí la B. Medios: pintura mural. Espacio: muro exterior. Montaje: sin etiquetas. Público: quien pasa, sin horario. Aporte: participación de vecinos y jóvenes. Boceto: un pasillo con mis dibujos pintados sobre cartón pegados en la pared y una tarjeta con el nombre de cada uno. Recurso tomado: pintar con otras personas, del mural de ejemplo.",
        ["completa los cinco criterios con datos de la descripción", "marca como pendiente lo que no se dice", "hace un boceto que reinterpreta un recurso", "cita la procedencia del recurso"],
        ["tabla de cinco criterios", "boceto", "fuente citada"],
        ["opinar sin describir", "copiar el espacio completo"],
        "Pregunta qué criterio quedó pendiente y qué recurso tomó para su boceto.",
    ),
    "Mira una pared de tu casa y di en voz alta qué obras pondrías, a qué altura y cómo las ordenarías.",
    "Elige un espacio de ejemplo y escribe tres frases sobre qué público puede quedar fuera de él.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA6, 2,
    "Hojas y lápiz. Las tres fichas de espacios están escritas en esta clase.",
    "Aprenderé a investigar el público, el acceso y el aporte a la comunidad de un espacio de difusión, y a separar datos de inferencias. Sirve para comparar espacios con respaldo y decidir dónde exponer.",
    ["Sé los cinco criterios de descripción.", "Sé separar datos de inferencias."],
    [
        "Para investigar un espacio de difusión me pregunto: ¿quién lo organiza?, ¿para qué existe?, ¿quiénes lo visitan?, ¿qué obras muestra? y ¿qué tan fácil es llegar? El acceso depende de varias cosas: el horario, el costo, la ubicación y, en un espacio virtual, la conexión a internet. Una entrada liberada es una entrada que no se paga. Un espacio con entrada liberada y talleres presenciales facilita que los vecinos participen.",
        "El aporte a la comunidad se apoya en evidencia: talleres para vecinos, entrada liberada, exposiciones de personas del barrio, encuentros. No basta decir «aporta mucho»; digo qué hace el espacio y para quién. Un espacio puede aportar mucho a un grupo y poco a otro: una galería en línea sirve a quien tiene conexión, pero deja fuera a quien no la tiene.",
        "Separo datos de inferencias. «El centro tiene talleres para vecinos» es un dato de la ficha; «los vecinos aprenden mucho» es una inferencia que nadie escribió. Si falta información, como cuántas personas asisten, la marco como pendiente y busco una fuente, por ejemplo a quienes organizan el espacio. Así mi comparación se puede comprobar.",
    ],
    [("acceso", "facilidad con que las personas pueden llegar a un espacio o usarlo"), ("entrada liberada", "entrada que no se paga"), ("conexión", "acceso a internet"), ("organizar", "preparar y hacerse cargo de un espacio o una actividad"), ("evidencia", "dato que respalda una afirmación")],
    [
        w("Leer una ficha", "Ficha de ejemplo: «Centro cultural barrial que abre de martes a sábado, 6 horas cada día, con entrada liberada, exposiciones de dibujo y fotografía y talleres para vecinos». Señala medios de expresión, acceso y aporte.", ["Medios: dibujo y fotografía.", "Acceso: de martes a sábado, 6 horas diarias, entrada liberada.", "Aporte: talleres para vecinos y entrada que no se paga."], "Medios: dibujo y fotografía; acceso: 5 días, 6 horas, entrada liberada; aporte: talleres para vecinos"),
        w("Horas por semana", "El centro abre de martes a sábado, 6 horas cada día. ¿Cuántas horas abre en una semana?", ["De martes a sábado hay 5 días.", "Multiplico 5 por 6."], "30 horas"),
    ],
    [
        m("Decir que un espacio «aporta mucho» sin decir qué hace ni para quién.", "No hay evidencia que se pueda comprobar.", "Nombra qué ofrece el espacio y a qué personas llega."),
        m("Pensar que un espacio virtual llega a toda la comunidad.", "Quien no tiene conexión queda fuera.", "Revisa quiénes pueden acceder."),
    ],
    [
        ex("El centro cultural abre de martes a sábado. ¿Cuántos días a la semana abre?", "5", "Martes, miércoles, jueves, viernes y sábado."),
        ex("¿Qué significa «entrada liberada»? A. Que no se paga entrada B. Que se paga una entrada mayor.", "A", "Liberada es sin costo."),
        ex("Para ver una galería en línea, ¿qué necesita una persona además de un aparato?", "Conexión a internet", "Es un espacio virtual."),
    ],
    [
        ex("¿Cuál afirmación es un dato de la ficha del centro? A. El centro tiene talleres para vecinos B. Los vecinos aprenden mucho en los talleres.", "A", "La ficha afirma los talleres, no el aprendizaje."),
        ex("Una feria al aire libre tiene puestos de pintura, grabado y artesanía. ¿Qué criterio describe eso? A. Los medios de expresión presentes B. El aporte a la comunidad.", "A", "Dice qué tipos de obra se muestran."),
        ex("¿Qué aporte a la comunidad tiene el centro cultural? A. Talleres y entrada liberada, que facilitan que los vecinos participen B. Que tenga paredes blancas.", "A", "Son acciones que permiten participar."),
    ],
    [
        arith("Otro centro cultural de ejemplo abre de lunes a viernes, 8 horas cada día. ¿Cuántas horas abre por semana?", "5*8", "Se multiplican los días por las horas."),
        arith("Una feria de ejemplo se arma el primer domingo de cada mes. ¿Cuántas veces se arma en 3 años?", "12*3", "Hay 12 meses por año."),
        arith("Un liceo de ejemplo sube a su galería en línea 15 fotografías y 9 videos. ¿Cuántas obras muestra?", "15+9", "Se suman las fotografías y los videos."),
    ],
    [
        ex("Para vecinos sin internet, ¿cuál es más accesible: el centro cultural con entrada liberada o la galería en línea?", "El centro cultural", "La galería exige conexión."),
        ex("Un compañero dice «la feria llega a más gente que el centro cultural» sin dar ningún dato. ¿Qué es su afirmación?", "Una inferencia sin respaldo", "No hay evidencia que la sostenga."),
    ],
    [
        ex("La ficha del centro no dice cuántos vecinos asisten. ¿Qué haces?", "Lo marco como pendiente y lo pregunto a quienes organizan el centro", "Un dato que falta se busca; no se inventa."),
        arith("Un grupo de 4 personas visitaría un espacio de ejemplo con entrada de $2.000 por persona. ¿Cuántos pesos pagaría en total?", "4*2000", "Se multiplica el valor de la entrada por las personas."),
    ],
    ex("Tu curso quiere invitar a vecinos que no tienen conexión a internet. ¿Qué espacio conviene? A. Un centro cultural barrial con entrada liberada B. Una galería en línea.", "A", "Es presencial y no exige conexión."),
    [
        ex("¿Qué es una entrada liberada?", "Una entrada que no se paga", "Facilita el acceso."),
        ex("Verdadero o falso: una galería en línea llega a toda la comunidad.", "Falso", "Quien no tiene conexión queda fuera."),
        ex("¿Qué debes hacer con un dato que falta en la ficha?", "Marcarlo como pendiente y buscar una fuente", "No se inventa."),
    ],
    task(
        "Elige UNA ficha. A) Centro cultural barrial que abre de martes a sábado, 6 horas diarias, entrada liberada, exposiciones de dibujo y fotografía y talleres para vecinos. B) Feria de arte al aire libre, el primer domingo de cada mes en una plaza, con puestos de pintura, grabado y artesanía y entrada liberada. C) Galería en línea de fotografías y videos de estudiantes de un liceo, accesible desde cualquier lugar con conexión. Haz una tabla con medios de expresión, espacio, montaje, público y aporte, marca lo pendiente, anota una inferencia con una pregunta para investigarla y di a quién llega y a quién deja fuera.",
        "Elegí la C. Medios: fotografía y video. Espacio: virtual. Montaje: pendiente. Público: quien tenga conexión. Aporte: muestra el trabajo de estudiantes. Inferencia: tal vez la ven familias lejanas; pregunta: ¿cuántas personas la visitan? Llega a quien tiene conexión y deja fuera a quien no la tiene.",
        ["completa la tabla con datos de la ficha", "marca lo pendiente", "formula una pregunta de investigación", "dice a quién llega y a quién deja fuera"],
        ["tabla de cinco criterios", "inferencia con pregunta", "público incluido y excluido"],
        ["escribir como dato algo que la ficha no dice", "suponer que llega a toda la comunidad"],
        "Señala un dato y una inferencia de la tabla y pregunta qué fuente confirmaría la inferencia.",
    ),
    "Pregunta a una persona de tu casa qué espacio cultural conoce y anota cómo llegó a él y si cuesta entrar.",
    "Escribe dos preguntas de investigación sobre el público de un espacio y di dónde buscarías cada respuesta.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA6, 3,
    "Hojas, lápiz, regla y cartón para tarjetas. Las medidas que se usan están en los enunciados.",
    "Aprenderé a tomar decisiones de montaje, como la altura, la separación, el orden y la cartela, y a calcular el reparto de obras en una pared. Sirve para mostrar obras de manera clara y accesible.",
    ["Sé los cinco criterios para describir un espacio de difusión.", "Sé dibujar un plano en planta con escala."],
    [
        "El montaje es el conjunto de decisiones que ordenan las obras en un espacio. Una referencia habitual es poner el centro de las obras a unos 150 cm del suelo, cerca de la altura de los ojos de muchas personas; es solo una referencia: si el público son niños o personas en silla de ruedas, conviene bajar un poco el centro de las obras y las cartelas. Las obras iguales con separaciones parejas crean orden y ritmo, y se miran una por una. Agrupar obras por tema o por medio ayuda a entenderlas. La obra principal se puede destacar al centro o con más espacio alrededor.",
        "La cartela es la etiqueta junto a cada obra con título, autoría y materiales. Su letra debe ser legible y estar a una altura cómoda. La iluminación debe evitar reflejos sobre superficies brillantes: una luz de frente sobre un vidrio produce reflejo, y una luz de lado lo reduce. El recorrido debe dejar un camino libre y amplio, para que cualquier persona, incluso con silla de ruedas, pueda circular sin chocar con obras.",
        "Para repartir las obras en una pared calculo: largo de la pared menos el ancho de todas las obras, dividido por el número de espacios iguales. Con n obras hay n + 1 espacios, contando los bordes. Hago un plano en planta o una vista de frente en papel, pruebo y ajusto antes de montar. Siempre uso materiales seguros y no clavo ni perforo paredes sin permiso.",
    ],
    [("cartela", "etiqueta junto a una obra con título, autoría y materiales"), ("separación", "espacio entre una obra y otra"), ("reflejo", "brillo de una luz sobre una superficie que dificulta ver la obra"), ("recorrido", "camino que sigue el público dentro del espacio"), ("jerarquía", "orden de importancia que se da a las obras al montarlas")],
    [
        w("Repartir en una pared", "Una pared mide 500 cm. Colgarás 3 obras de 60 cm de ancho, con espacios iguales entre ellas y en los bordes. ¿Cuántos centímetros mide cada espacio?", ["Tres obras ocupan 3 por 60, es decir, 180 cm.", "Sobran 500 menos 180, o sea 320 cm.", "Con 3 obras hay 4 espacios: 320 dividido por 4."], "80 cm"),
        w("Altura de la obra", "Una obra de 40 cm de alto debe quedar con su centro a 150 cm del suelo. ¿A qué altura queda su borde inferior?", ["La mitad de 40 es 20.", "Resto 20 a 150."], "130 cm"),
    ],
    [
        m("Poner las obras muy arriba o muy abajo según el espacio que queda.", "Se dificulta verlas y leer las cartelas.", "Usa la altura de referencia y ajusta la pared, no la altura de la mirada."),
        m("Dejar el camino lleno de obras que sobresalen.", "Alguien puede chocar y se limita el acceso.", "Deja un camino libre y amplio."),
    ],
    [
        ex("¿Qué datos lleva una cartela?", "Título, autoría y materiales", "Es la etiqueta junto a cada obra."),
        ex("Agrupar obras por tema, ¿es una decisión de montaje o de público?", "De montaje", "Decide cómo se ordenan las obras."),
        ex("Una luz de frente sobre una superficie brillante produce un efecto molesto. ¿Cómo se llama?", "Reflejo", "Dificulta ver la obra."),
    ],
    [
        ex("Obras iguales con separaciones parejas, ¿qué crean? A. Orden y ritmo B. Desorden.", "A", "La separación pareja ordena la mirada."),
        ex("Quieres destacar una obra principal. ¿Qué decisión usas? A. Ponerla al centro con más espacio alrededor B. Esconderla entre otras.", "A", "El espacio alrededor le da jerarquía."),
        ex("Un camino angosto tiene obras que sobresalen. ¿Qué riesgo hay? A. Alguien puede chocar con ellas B. Se ven mejor.", "A", "Un camino libre y amplio evita choques."),
    ],
    [
        arith("Una pared de 600 cm tendrá 4 obras de 50 cm de ancho, con espacios iguales entre ellas y en los bordes. ¿Cuántos centímetros mide cada espacio?", "(600-4*50)//5", "Con 4 obras hay 5 espacios; se reparte lo que sobra."),
        arith("Una pared de 400 cm tendrá 3 obras de 60 cm de ancho, con espacios iguales entre ellas y en los bordes. ¿Cuántos centímetros mide cada espacio?", "(400-3*60)//4", "Con 3 obras hay 4 espacios."),
        arith("Una obra de 30 cm de alto debe quedar con su centro a 150 cm del suelo. ¿A qué altura queda su borde inferior?", "150-30//2", "Se resta al centro la mitad del alto."),
    ],
    [
        ex("Montaje X: obras pegadas sin espacio entre ellas. Montaje Y: separación pareja de 20 cm. Quieres que cada obra se mire por separado. ¿Cuál eliges?", "Y", "El espacio separa cada obra."),
        ex("Una obra con superficie brillante muestra reflejo por una luz de frente. ¿Qué cambio de una variable ayuda? A. Mover la luz a un lado de la obra B. Mover la obra más abajo.", "A", "La luz de lado reduce el reflejo."),
    ],
    [
        ex("Para que lo disfruten personas en silla de ruedas y personas de baja estatura, ¿qué decisión ayuda? A. Camino libre y amplio y cartelas legibles, a una altura que se pueda leer sentado o de pie B. Obras muy altas y cartelas pequeñas.", "A", "Mejora el acceso físico y visual."),
        ex("Cambias una cartela de letra pequeña por una de letra grande. ¿Qué mejora?", "La legibilidad", "Se lee con más facilidad."),
    ],
    arith("Un pasillo tiene una pared de 320 cm donde colgarás 3 obras de 40 cm de ancho, con espacios iguales entre ellas y en los bordes. ¿Cuántos centímetros mide cada espacio?", "(320-3*40)//4", "Con 3 obras hay 4 espacios; se reparte lo que sobra."),
    [
        ex("Con n obras en una pared, ¿cuántos espacios hay contando los bordes?", "n + 1", "Hay un espacio antes de la primera y uno después de cada obra."),
        ex("Verdadero o falso: una luz de frente sobre un vidrio reduce el reflejo.", "Falso", "Lo aumenta; una luz de lado lo reduce."),
        ex("¿A qué altura aproximada se pone el centro de las obras como referencia?", "A unos 150 cm del suelo", "Es cerca de la altura de los ojos de muchas personas."),
    ],
    task(
        "Elige UNA pared. A) 500 cm de largo, para 3 obras de 60 cm. B) 480 cm de largo, para 4 obras de 40 cm. C) 360 cm de largo, para 2 obras de 60 cm. Calcula el espacio entre obras (iguales, bordes incluidos), dibuja la pared de frente con las obras y las medidas, ubica el centro de las obras a unos 150 cm del suelo, escribe una cartela por obra con título, autoría y materiales, y deja un camino libre. No perfores ni claves paredes: usa una pared dibujada en papel.",
        "Elegí la A. Obras: 3 × 60 = 180 cm; sobran 320 cm; 4 espacios de 80 cm. Dibujé la pared con cada obra y las medidas. Centro a 150 cm. Cartela de cada una: título, autoría y materiales. Dejé libre el camino frente a la pared.",
        ["calcula el espacio con n + 1 espacios iguales", "dibuja la pared con medidas", "ubica el centro de las obras a la altura de referencia", "escribe cartelas completas y deja un camino libre"],
        ["cálculo", "dibujo de frente con medidas", "cartelas"],
        ["olvidar contar los espacios de los bordes", "dejar obras que sobresalen en el camino"],
        "Pregunta cómo calculó el espacio entre obras y qué decisión tomó para el recorrido.",
    ),
    "Mide una pared de tu casa y calcula dónde irían tres obras iguales de 30 cm con espacios iguales.",
    "Explica por qué un montaje que funciona para una pared de 500 cm no sirve igual para una de 300 cm y qué cambiarías.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA6, 4,
    "Hojas, lápiz, regla y cartón para tarjetas. Los dos espacios que compararás están descritos en esta clase.",
    "Aprenderé a comparar dos espacios de difusión con los cinco criterios, a valorarlos con una razón y a diseñar una exposición propia en un espacio que beneficie a una comunidad. Sirve para decidir dónde y cómo mostrar un trabajo.",
    ["Sé investigar acceso, público y aporte de un espacio.", "Sé calcular el reparto de obras en una pared."],
    [
        "Comparar y valorar espacios de difusión significa mirar dos espacios con los mismos cinco criterios y luego decir cuál conviene más para un propósito, con una razón. Por ejemplo, para un público que no tiene internet, un centro cultural presencial con entrada liberada conviene más que una galería en línea, porque llega a quienes la galería deja fuera. Una valoración sin razón, como «es mejor porque sí», no sirve.",
        "Para diseñar una exposición propia sigo seis pasos. Elijo un espacio y un público. Decido qué medios de expresión mostraré. Dibujo el plano de montaje con medidas. Pienso qué aporte quiero dejar a esas personas: acceso, encuentro o aprendizaje. Escribo una invitación con qué, dónde, cuándo y para quién, y las cartelas. Finalmente, pregunto a algunos asistentes qué les dejó la exposición.",
        "Soy honesto con los resultados: si cuatro de cinco asistentes dicen que aprendieron algo, hablo de esas cinco personas, no de toda la comunidad. Y valoro cada espacio según su propósito, no según cuál es más moderno o más antiguo. Un espacio pequeño y cercano puede aportar más a un barrio que uno grande y lejano.",
    ],
    [("valorar", "decir qué conviene más o es más logrado, con una razón"), ("invitación", "mensaje que dice qué, dónde, cuándo y para quién es una exposición"), ("asistente", "persona que va a ver una exposición"), ("propósito", "para qué se hace una exposición"), ("comparar", "mirar dos espacios con los mismos criterios")],
    [
        w("Valorar con razón", "Quieres exponer 10 fotografías para estudiantes de tu liceo. Comparas el pasillo del liceo y una galería en línea. ¿Cuál conviene y por qué?", ["Los estudiantes pasan por el pasillo todos los días.", "La galería en línea exige entrar a una página.", "El público ya está en el pasillo."], "El pasillo del liceo, porque es presencial y llega a quienes ya pasan por ahí cada día"),
        w("Repartir dibujos", "Quieres repartir 12 dibujos en 3 paredes por igual. ¿Cuántos dibujos van en cada pared?", ["Los dibujos se reparten en partes iguales.", "Divido 12 entre 3."], "4 dibujos"),
    ],
    [
        m("Elegir un espacio solo porque parece más moderno.", "Puede no llegar al público que quieres.", "Elige según el propósito y el público."),
        m("Decir que la exposición aportó a toda la comunidad por lo que dijeron unos pocos asistentes.", "Pocas respuestas no representan a todos.", "Habla de las personas consultadas."),
    ],
    [
        ex("¿Cuántos criterios se usan para comparar espacios de difusión en esta clase?", "Cinco", "Medios, espacio, montaje, público y aporte."),
        ex("¿Qué dice una invitación?", "Qué, dónde, cuándo y para quién es la exposición", "Con esos datos la gente sabe a qué ir."),
        ex("Para valorar un espacio, ¿qué necesitas además de describirlo? A. Una razón basada en los criterios B. Su fecha de inauguración.", "A", "Sin razón no se puede comprobar."),
    ],
    [
        ex("¿Cuál valoración tiene una razón? A. «El centro cultural aporta más a vecinos sin internet porque tiene entrada liberada y talleres presenciales» B. «El centro es mejor porque sí».", "A", "Da un motivo basado en el público y el acceso."),
        ex("Quieres que vecinos de un mismo edificio vean 12 dibujos sin salir lejos. ¿Dónde conviene exponer? A. En el hall del edificio B. En una galería en línea.", "A", "Está cerca y no exige conexión."),
        ex("¿Cuál invitación tiene los datos necesarios? A. «Exposición de dibujos, el sábado a las 11:00, en el hall del edificio, con entrada liberada» B. «Vengan».", "A", "Dice qué, cuándo, dónde y el costo."),
    ],
    [
        arith("Repartes 20 dibujos en 4 paredes por igual. ¿Cuántos dibujos hay en cada pared?", "20//4", "Se divide el total entre las paredes."),
        arith("Invitaste a 20 vecinos y asistieron 14. ¿Cuántos no asistieron?", "20-14", "Se resta los que asistieron del total invitado."),
        ex("Une cada dato con su criterio. a) «Es el hall de un edificio». b) «Hay dibujos y fotografías». c) «Lo visitan vecinos del edificio». Criterios: 1 medios de expresión, 2 espacio, 3 público. Escribe cada letra con su número.", "a-2, b-1, c-3", "Cada dato responde a un criterio distinto."),
    ],
    [
        ex("Quieres que vecinos del edificio que no tienen conexión a internet vean la exposición. Opción X: galería en línea que llega a personas lejanas pero exige conexión. Opción Y: hall del edificio. ¿Cuál conviene?", "Y", "Llega a quienes no tienen conexión."),
        ex("Valoración X: «El museo es mejor que el muro porque es más serio». Valoración Y: «El muro llega a más gente que pasa porque no tiene horario; el museo permite ver con calma gracias a las etiquetas». ¿Cuál usa criterios?", "Y", "Compara público y montaje."),
    ],
    [
        arith("Cada fila de la exposición lleva 6 dibujos de 40 cm de ancho. El hall mide 480 cm de ancho. ¿Cuántos centímetros de pared quedan libres en una fila para los espacios?", "480-6*40", "Se resta el ancho de los dibujos al ancho del hall."),
        ex("Preguntas a 5 asistentes qué les dejó la exposición y 4 responden algo concreto. ¿Qué conclusión es válida? A. Para esas 5 personas hubo un aporte B. La exposición aportó a toda la comunidad.", "A", "Cinco respuestas no representan a todos."),
    ],
    ex("Tu curso compara un centro cultural barrial y una galería en línea para exponer a vecinos que no tienen internet. ¿Cuál comparación está mejor argumentada? A. «El centro es más adecuado porque su entrada es liberada y presencial, y la galería exige conexión» B. «La galería, porque es moderna».", "A", "Usa público y acceso como razones."),
    [
        ex("¿Qué debe tener una valoración de un espacio?", "Una razón basada en los criterios", "Así se puede comprobar."),
        ex("Verdadero o falso: un espacio más moderno aporta siempre más a la comunidad.", "Falso", "El aporte depende del propósito y del público."),
        ex("¿Qué cuatro datos lleva una invitación?", "Qué, dónde, cuándo y para quién", "Permiten saber a qué ir."),
    ],
    task(
        "Elige UN caso. A) Exponer 12 dibujos para vecinos de tu edificio que no tienen conexión a internet. B) Exponer 10 fotografías del barrio para estudiantes de tu liceo. C) Exponer 8 trabajos de arte reciclado en una feria de barrio. Compara dos espacios posibles con los cinco criterios, valora cuál conviene con una razón, dibuja el plano de montaje con medidas (una pared de papel basta) y escribe la invitación con qué, dónde, cuándo y para quién, y una cartela. No perfores ni claves paredes.",
        "Elegí el caso A. Comparé el hall del edificio y una galería en línea. Valoración: el hall conviene porque es presencial y llega a quienes no usan internet. Plano: pared de 480 cm, 12 dibujos de 40 cm en 2 filas de 6, 240 cm libres por fila. Invitación: «Exposición de dibujos, el sábado a las 11:00, en el hall del edificio, entrada liberada, para todos los vecinos».",
        ["compara dos espacios con los cinco criterios", "valora con una razón", "dibuja el plano con medidas", "escribe invitación y cartela con los datos necesarios"],
        ["tabla comparativa", "plano", "invitación y cartela"],
        ["elegir por lo moderno", "generalizar a toda la comunidad"],
        "Pregunta qué criterio decidió su elección y cómo lo comprobaría con los asistentes.",
    ),
    "Cuéntale a una persona de tu casa dónde mostrarías un trabajo tuyo y por qué ese lugar llega a quien quieres.",
    "Escribe una segunda valoración para el mismo caso con un público distinto y explica qué cambia.",
)

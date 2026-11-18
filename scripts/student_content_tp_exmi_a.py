"""Explotación Minera TP 3.º y 4.º medio: OAE-01 (planos y mapas), OAE-02 (fortificación: solo conceptos y documentos) y OAE-03 (ventilación secundaria y drenaje: solo conceptos y cálculos de planilla). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_exmi_common import AVISO, EMER, build

O1 = "TP-EXMI-3y4-OAE-01"
O2 = "TP-EXMI-3y4-OAE-02"
O3 = "TP-EXMI-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La faena ficticia «Mina Demo Quebrada Seca» explota cobre a cielo abierto y tiene un sector subterráneo pequeño. Su mapa de ubicación muestra el rajo, la planta, los caminos, un punto de reunión de emergencia y una zona de tronadura con acceso restringido. "
     "Peligros anotados: caída de rocas desde los taludes, tránsito de camiones de gran tamaño, polvo y desorientación en el sector subterráneo. Dotación de ejemplo por turno: 40 personas en el rajo, 15 en la planta y 5 en el sector subterráneo. "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad (de 1 a 5) × gravedad (de 1 a 5). Caída de rocas: probabilidad 3 y gravedad 5. Polvo: probabilidad 5 y gravedad 2.")
build(
    O1, 1, F,
    use="Aprenderé para qué sirven los planos y mapas de una faena minera, qué peligros y riesgos hay que tener presentes al leerlos y por qué leer un mapa no habilita para entrar a una zona restringida.",
    prior=["Sé leer una tabla sencilla.", "Sé multiplicar y dividir números enteros.", "Sé que una empresa se rige por reglas escritas."],
    explain=[
        "Una faena minera es el lugar de trabajo donde se extrae y se trata el mineral; en una mina a cielo abierto, la excavación se llama rajo. Se representa en planos y mapas: un mapa de ubicación muestra dónde están las áreas, los caminos, los puntos de reunión y las zonas restringidas; un plano muestra con más detalle una parte, como una labor o un nivel. Todo plano usa simbología, que son signos y colores explicados en una leyenda. Una zona de exclusión es un área con acceso prohibido o restringido por su riesgo, y un punto de reunión es el lugar señalado donde el personal se junta en una emergencia.",
        "Un peligro es una fuente que puede causar daño, y el riesgo es la posibilidad de que ese daño ocurra. En la matriz de ejemplo el puntaje de riesgo se calcula como probabilidad por gravedad, y se atiende primero el puntaje mayor. La autoridad minera fiscaliza que la faena cumpla la norma vigente de seguridad, y la empresa debe mantener planos y señales al día.",
        f"Leer un mapa ayuda a prevenir, pero no habilita a nadie para entrar a una zona restringida ni a trabajar en ella: eso exige formación, autorización y permiso. {EMER} {AVISO}",
    ],
    vocab=[("faena minera", "lugar donde se extrae y se trata el mineral"), ("mapa de ubicación", "dibujo que muestra dónde están las áreas, los caminos y los puntos de seguridad de la faena"), ("simbología", "signos y colores de un plano, explicados en la leyenda"), ("zona de exclusión", "área con acceso prohibido o restringido por su riesgo"), ("punto de reunión", "lugar señalado donde el personal se junta en una emergencia"), ("peligro", "fuente que puede causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("puntaje de riesgo", "probabilidad multiplicada por gravedad, según la matriz")],
    worked=[
        ("Peligro y riesgo", "En un taller de mantención de ejemplo, un charco de aceite cubre parte del pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el aceite en el piso, porque puede causar daño.", "El riesgo es que alguien resbale y caiga."], "Peligro: el aceite en el piso; riesgo: que alguien resbale y caiga"),
        ("Puntaje de riesgo", "En otra matriz de ejemplo, el tránsito de camionetas en un cruce de caminos tiene probabilidad 2 y gravedad 4. ¿Qué puntaje de riesgo resulta?", ["Se multiplica la probabilidad por la gravedad.", "2 por 4 son 8."], "8 puntos"),
    ],
    mistakes=[("Creer que quien leyó el mapa ya puede entrar a cualquier zona de la faena.", "Entrar a una zona restringida exige formación, autorización y permiso, no solo conocer el mapa.", "Usa el mapa para saber dónde no entrar y pide autorización para lo demás."),
              ("Llamar riesgo a la fuente del daño, como la caída de rocas.", "La fuente del daño es el peligro; el riesgo es la posibilidad de que ocurra el daño.", "Pregúntate: ¿esto es la fuente o es la posibilidad de daño?")],
    T=[
        ("abc", "En Explotación Minera: ¿para qué sirve un mapa de ubicación de una faena?", "Para saber dónde están las áreas, los caminos, los puntos de reunión y las zonas restringidas", "Para calcular cuántas toneladas de mineral hay en cada área", "Para autorizar a una persona a trabajar en una zona de riesgo", "El mapa de ubicación orienta; no calcula producción ni entrega autorizaciones."),
        ("abc", "En Explotación Minera: ¿qué es la simbología de un plano?", "El conjunto de signos y colores que representan elementos e indicaciones, explicados en la leyenda", "La lista de personas que pueden usar el plano", "El nombre de la empresa que lo dibujó", "Los símbolos solo se entienden con la leyenda, que explica cada signo."),
        ("abc", "En Explotación Minera: ¿qué es una zona de exclusión?", "Un área donde el acceso está prohibido o restringido por su riesgo", "Un área donde se guardan los planos de la faena", "Un área abierta a todo el personal sin permiso", "Una zona de exclusión limita el acceso justamente por el riesgo que tiene."),
        ("=", "{F} ¿Cuántas personas trabajan por turno en total en la faena de la ficha?", "40+15+5", "Se suman las personas del rajo, de la planta y del sector subterráneo.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «caída de rocas desde los taludes»?", "Que una roca golpee a una persona y la lesione", "Que el rajo tenga taludes", "Que se necesiten más camiones en el rajo", "El riesgo es el daño posible; tener taludes es solo la situación que lo origina."),
        ("abc", "{F} ¿Para qué sirve el punto de reunión que muestra el mapa?", "Para que el personal se junte allí en una emergencia y se pueda contar a todos", "Para guardar las herramientas del turno", "Para esperar el inicio de la jornada", "El punto de reunión permite saber si todas las personas están a salvo."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la caída de rocas?", "3*5", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál debe atenderse primero, la caída de rocas o el polvo?", "La caída de rocas, porque su puntaje 15 supera al 10 del polvo", "El polvo, porque tiene la mayor probabilidad (5)", "Ambos por igual, porque los dos están anotados", "Se prioriza el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Una persona sin autorización quiere pasar por la zona de tronadura restringida para acortar camino. ¿Qué corresponde?", "No ingresar, usar el camino señalado y avisar a un responsable si necesita pasar", "Pasar si lleva casco y chaleco reflectante", "Entrar si no ve a nadie en la zona", "Una zona restringida no se cruza sin autorización, aunque se use protección."),
        ("abc", "{F} ¿Por qué conviene que el mapa marque a la vez el punto de reunión y la zona restringida?", "Porque muestra dónde reunirse y dónde no entrar, y así se puede actuar rápido en una emergencia", "Porque el mapa reemplaza al plan de emergencia de la empresa", "Porque la ley exige que el mapa tenga solo dos símbolos", "El mapa orienta, pero no sustituye el plan de emergencia que la empresa debe tener."),
        ("abc", "{F} Un compañero dice: «leí el mapa de la faena, así que ya puedo entrar solo al sector subterráneo». ¿Qué es correcto?", "Leer el mapa no lo habilita: necesita formación, autorización y cumplir la norma vigente", "Puede entrar si lleva casco y linterna", "Puede entrar si ya conoce el camino de memoria", "Ni el equipo de protección ni conocer el camino reemplazan la autorización."),
        ("=", "{F} Para un simulacro, el personal del rajo y de la planta de un turno se reparte en grupos de 5 personas. ¿Cuántos grupos se forman?", "(40+15)//5", "Se suma el personal de las dos áreas y se divide entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, una persona te cuenta que de la entrada de un sector subterráneo sale humo y que hay personas adentro. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar con un mapa a buscar a las personas", "Esperar a ver si el humo se disipa antes de avisar", "Intervenir sin formación puede sumar otra víctima; lo que corresponde es avisar."),
    ],
    ctx=("abc", "El jefe de un contratista de ejemplo te dice: «Toma este mapa y entra tú al sector subterráneo a revisar, el mapa te lo explica todo». ¿Qué respondes?", "Que no, porque entrar exige formación, autorización y norma vigente, y que consultarás a un adulto responsable", "Que sí, porque con el mapa basta", "Que sí, pero solo hasta la primera galería", "Leer un mapa no habilita para entrar a un sector subterráneo."),
    sc=[
        ("En Explotación Minera: ¿qué es un peligro?", "Una fuente que puede causar daño, como la caída de rocas", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En Explotación Minera: ¿para qué sirve un punto de reunión?", "Para que el personal se junte en una emergencia y se cuente a todos", "El punto de reunión permite comprobar que nadie quedó atrás."),
        ("¿Cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("Mapa ficticio de la faena «Mina Demo Cerro Claro»: tiene un camino principal, una bodega, un punto de reunión y una zona restringida junto al botadero (lugar donde se deposita la roca sin valor). Escribe (a) qué información útil entrega ese mapa para una emergencia, (b) por qué la zona restringida debe estar marcada y quién debe autorizar la entrada, (c) un peligro y su riesgo asociado en esa faena, (d) por qué leer el mapa no te habilita para trabajar.",
        "(a) Dónde está el punto de reunión y cuál es el camino para llegar. (b) Porque tiene un riesgo que limita el acceso; la entrada la autoriza el responsable de la faena. (c) Peligro: el tránsito de camiones por el camino principal; riesgo: que un camión atropelle a una persona. (d) Porque trabajar ahí exige formación, autorización, norma vigente y permiso.",
        ["explica la utilidad del mapa en una emergencia", "justifica la zona restringida", "distingue peligro y riesgo", "aclara que el mapa no habilita"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que el mapa autoriza el ingreso", "no nombrar quién autoriza"],
        "Pregunta: «¿quién puede autorizarte a entrar y qué necesitas tú?». Si no responde, pídele que relea el último párrafo de la explicación."),
    reinforce="Inventa una matriz de dos peligros de una faena con probabilidad y gravedad, calcula los puntajes y di cuál se atiende primero.",
    extend="Explica con un ejemplo por qué un mapa desactualizado puede ser peligroso.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Cuadro de rotulación de un plano de la faena ficticia «Mina Demo Quebrada Seca»: Título: plano de planta del nivel de cota 1.200 m. Escala: 1:2.000. Revisión: C. Fecha: 15 de marzo de ejemplo. Elaboró: topografía. Revisó: planificación. Aprobó: la jefatura de la faena. Estado: vigente. "
     "Leyenda: línea azul continua = ruta de evacuación; triángulo amarillo = advertencia; círculo rojo con barra = prohibición; cuadrado verde = punto de reunión; línea punteada = labor proyectada, aún no construida. El norte está hacia arriba del plano.")
build(
    O1, 2, F,
    use="Aprenderé los tipos de plano de una mina, las partes de un plano (escala, leyenda, cuadro de rotulación, norte y cota) y qué rol cumple cada persona que lo elabora, revisa y aprueba.",
    prior=["Sé qué es un mapa de ubicación y para qué sirve.", "Sé convertir centímetros en metros.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un plano de planta muestra una labor o un terreno visto desde arriba. Una sección o perfil es un corte vertical que muestra alturas y profundidades. La cota es la altura de un punto respecto de un nivel de referencia, y un nivel es un piso de trabajo de la mina que se identifica por su cota. La escala relaciona el plano con la realidad: en 1:2.000, 1 cm del plano representa 2.000 cm, es decir, 20 m en terreno.",
        "El cuadro de rotulación es el recuadro del plano que indica su título, escala, revisión, fecha, quién lo elaboró, revisó y aprobó, y su estado. Solo se debe usar la revisión vigente: una revisión antigua puede mostrar labores que ya cambiaron. La leyenda explica los símbolos. En general, el rojo se usa para prohibiciones, el amarillo para advertencias, el azul para obligaciones y el verde para evacuación y seguridad, pero la leyenda de cada plano manda.",
        f"Los roles se reparten: topografía elabora, planificación revisa y la jefatura de la faena aprueba. Leer un plano no habilita para intervenir una labor. {EMER} {AVISO}",
    ],
    vocab=[("plano de planta", "dibujo de una labor o terreno visto desde arriba"), ("sección o perfil", "corte vertical que muestra alturas y profundidades"), ("cota", "altura de un punto respecto de un nivel de referencia"), ("escala", "relación entre una medida del plano y la medida real"), ("cuadro de rotulación", "recuadro con título, escala, revisión, fecha y firmas del plano"), ("leyenda", "explicación de los símbolos del plano"), ("revisión vigente", "versión del plano que está en uso"), ("labor proyectada", "labor dibujada que todavía no está construida")],
    worked=[
        ("Escala de un plano", "El plano de un botadero de ejemplo está a escala 1:500 y dos puntos están a 8 cm. ¿Cuántos metros hay entre ellos en terreno?", ["1 cm del plano representa 500 cm, es decir, 5 m.", "8 cm por 5 m son 40 m."], "40 metros"),
        ("Leer un símbolo", "El plano de una bodega de ejemplo muestra un triángulo amarillo junto a un cruce de pasillos. ¿Qué indica y qué hace quien lo lee?", ["Por convención, el amarillo es advertencia, y se confirma en la leyenda.", "Quien lo lee extrema la atención en ese cruce y respeta la indicación."], "Advertencia en el cruce: se extrema la atención"),
    ],
    mistakes=[("Usar un plano sin revisar la fecha ni la revisión porque «el dibujo es el mismo».", "Una revisión antigua puede mostrar labores o rutas que ya cambiaron.", "Confirma en el cuadro de rotulación que el estado sea vigente."),
              ("Medir en el plano y dar la distancia en centímetros como si fuera la distancia real.", "La distancia real se obtiene aplicando la escala.", "Convierte siempre la medida del plano usando la escala.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué muestra un plano de planta?", "Una labor o terreno visto desde arriba", "Un corte vertical que muestra la profundidad", "La lista de materiales de la obra", "La planta es la vista desde arriba; el corte vertical es la sección."),
        ("abc", "En Explotación Minera: ¿qué es una sección o perfil de una mina?", "Un corte vertical que muestra alturas y profundidades", "Una vista desde arriba de la faena", "Una tabla con los símbolos del plano", "La sección corta el terreno en vertical; la vista desde arriba es la planta."),
        ("abc", "En Explotación Minera: ¿qué es la escala de un plano?", "La relación entre una medida en el plano y la medida real", "El tamaño del papel en que se imprime", "La cantidad de revisiones que tiene", "La escala permite convertir lo dibujado en distancias reales."),
        ("abc", "{F} ¿Qué significa la escala 1:2.000 del plano?", "1 cm del plano representa 2.000 cm en terreno", "1 cm del plano representa 200 cm en terreno", "2.000 cm del plano representan 1 cm en terreno", "En 1:2.000 cada unidad del plano equivale a 2.000 unidades reales."),
        ("abc", "{F} ¿Quién aprobó el plano?", "La jefatura de la faena", "Topografía", "Planificación", "Topografía elaboró, planificación revisó y la jefatura aprobó."),
        ("abc", "{F} Según la leyenda, ¿qué representa la línea punteada?", "Una labor proyectada, aún no construida", "Una ruta de evacuación", "Un camino cerrado por seguridad", "La ruta de evacuación es azul continua; la punteada indica lo proyectado."),
        ("=", "{F} Dos puntos del plano están separados 6 cm. ¿Cuántos metros hay entre ellos en terreno?", "6*2000//100", "Se multiplican los centímetros por 2.000 y se pasan a metros dividiendo entre 100.", " m"),
        ("abc", "{F} Una persona debe llegar al punto de reunión desde un taller. ¿Qué línea del plano debe seguir?", "La línea azul continua de la ruta de evacuación", "La línea punteada de la labor proyectada", "El triángulo amarillo de advertencia", "La ruta de evacuación está marcada en azul continuo según la leyenda."),
        ("=", "{F} Una ruta de evacuación mide 14 cm en el plano y se recorre a 2 metros por segundo (valor de ejemplo). ¿Cuántos segundos tarda?", "14*2000//100//2", "Se convierten los centímetros del plano a metros y se divide entre la rapidez.", " s"),
        ("abc", "Un jefe de turno de ejemplo tiene dos copias de un plano de planta: la revisión B, de hace un año, y la revisión D, vigente. ¿Cuál debe usar y por qué?", "La revisión D, porque es la vigente y las antiguas pueden mostrar labores que cambiaron", "La B, porque ya la conoce", "Cualquiera, porque el dibujo del terreno es el mismo", "El estado vigente del cuadro de rotulación indica la versión que se usa."),
        ("abc", "{F} ¿Por qué un plano debe indicar su escala?", "Porque sin escala no se pueden convertir las medidas del plano en distancias reales", "Porque la escala indica quién lo dibujó", "Porque la escala muestra si el plano está vigente", "La escala es lo que permite pasar de centímetros del plano a metros de terreno."),
        ("=", "{F} Una galería proyectada mide 9 cm en el plano. ¿Cuántos metros tendrá en terreno cuando se construya?", "9*20", "Cada centímetro del plano vale 20 metros reales con esta escala.", " m"),
        ("abc", "Durante una visita de ejemplo, una persona te dice que ve que una galería se está derrumbando con alguien adentro. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para medir con el plano qué tan grande es el derrumbe", "Esperar a que termine para informar", "Acercarse sin formación pone en riesgo a más personas; avisar es lo correcto."),
    ],
    ctx=("abc", "Un supervisor de ejemplo te muestra una hoja de plano sin fecha, sin revisión y sin firma de aprobación, y te pide ubicar en ella una ruta de evacuación. ¿Qué haces?", "Pedir el plano vigente con su cuadro de rotulación completo antes de usarlo", "Usarlo igual, porque se ve claro", "Usarlo y anotar tú la fecha de hoy", "Sin cuadro de rotulación no se sabe si el plano está vigente ni quién lo aprobó."),
    sc=[
        ("En Explotación Minera: ¿qué indica la escala 1:500?", "Que 1 cm del plano representa 5 m reales", "1 cm por 500 son 500 cm, es decir, 5 m."),
        ("¿Qué datos entrega el cuadro de rotulación?", "Título, escala, revisión, fecha, firmas y estado", "Es la ficha de identificación del plano."),
        ("En Explotación Minera: ¿qué es una cota?", "La altura de un punto respecto de un nivel de referencia", "La cota ubica los puntos en altura."),
    ],
    op=("Cuadro de rotulación ficticio de la faena «Mina Demo Cerro Claro»: plano de planta, escala 1:1.000, revisión A, sin fecha, elaborado por topografía, sin firma de revisión ni de aprobación, estado «borrador». Escribe (a) cuáles datos faltan, (b) si ese plano se puede usar para tomar decisiones y por qué, (c) cuántos metros reales representan 7 cm del plano, (d) qué rol tiene quien aprueba un plano.",
        "(a) Faltan la fecha, la firma de revisión y la de aprobación, y el estado vigente. (b) No: es un borrador y no se sabe si es la versión en uso. (c) 7 cm por 10 m son 70 m. (d) Aprobar significa dejar constancia de que el plano es correcto y de que se puede usar; lo hace la jefatura de la faena.",
        ["detecta los datos faltantes", "decide con criterio sobre el uso del plano", "convierte la medida con la escala", "describe el rol de quien aprueba"],
        ["hoja con las cuatro respuestas"],
        ["usar un plano en borrador", "no convertir la medida con la escala", "confundir quien revisa con quien aprueba"],
        "Pregunta: «¿cómo sabes que este plano está vigente?». Si no responde, pídele que relea la parte sobre el cuadro de rotulación."),
    reinforce="Dibuja en tu cuaderno un cuadro de rotulación con ocho datos y rellénalo con valores inventados.",
    extend="Explica con un ejemplo por qué un plano de planta y una sección se usan juntos.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Plano de planta simplificado de un sector subterráneo de la faena ficticia «Mina Demo Lomas Bajas», escala 1:1.000. Puntos: Taller (T), Cruce 1 (C1), Cruce 2 (C2), Cámara de refugio (R) y Salida a superficie (S). "
     "Tramos medidos en el plano: T–C1 = 3 cm; C1–S = 12 cm; C1–C2 = 5 cm; C2–R = 4 cm; C2–S = 8 cm. Leyenda: línea azul = ruta de evacuación hacia la salida. Anotación del plano: «el tramo C1–S está bloqueado por trabajos y marcado con prohibición». "
     "La cámara de refugio es un lugar señalado donde esperar solo si no se puede salir, y su uso lo indica el plan de emergencia de la empresa.")
build(
    O1, 3, F,
    use="Aprenderé a analizar en papel un caso de evacuación: leer un plano de labores, seguir una ruta permitida, calcular distancias y tiempos con la escala y respetar las prohibiciones marcadas.",
    prior=["Sé usar la escala de un plano.", "Sé sumar y multiplicar números enteros.", "Sé que una prohibición en un plano debe respetarse."],
    explain=[
        "Una galería es una labor casi horizontal de una mina subterránea; un cruce es el punto donde se encuentran dos o más galerías; una cámara de refugio es un lugar señalado donde esperar si no se puede salir. Una ruta de evacuación es el camino señalado que lleva a la salida o a un punto seguro, y el plan de emergencia de la empresa dice cómo se usa cada elemento.",
        "Para analizar un caso, primero se identifican los puntos y los tramos del plano; luego se descartan los tramos bloqueados o marcados con prohibición; después se comparan las rutas que quedan sumando las distancias que se obtienen aplicando la escala. Una ruta más corta no es mejor si pasa por un tramo prohibido. El tiempo de evacuación se estima dividiendo la distancia en metros entre la rapidez, que aquí es un valor de ejemplo.",
        f"Este análisis es solo de papel: moverse por una mina subterránea exige formación, autorización y personal de rescate preparado. {EMER} {AVISO}",
    ],
    vocab=[("galería", "labor casi horizontal de una mina subterránea"), ("cruce", "punto donde se encuentran dos o más galerías"), ("cámara de refugio", "lugar señalado donde esperar solo si no se puede salir"), ("ruta de evacuación", "camino señalado que lleva a la salida o a un punto seguro"), ("tramo", "parte de una ruta entre dos puntos"), ("tramo bloqueado", "tramo que no se puede usar por trabajos o por riesgo")],
    worked=[
        ("Comparar dos rutas", "En un plano de ejemplo a escala 1:500, la ruta X mide 11 cm y la ruta Y mide 9 cm, y ninguna está bloqueada. ¿Cuál es más corta y cuántos metros mide?", ["Cada centímetro del plano vale 5 m.", "La ruta Y mide 9 por 5, es decir, 45 m, y es menor que 11 por 5, que son 55 m."], "La ruta Y, de 45 m"),
        ("Respetar un bloqueo", "En el plano de una galería de ejemplo, la ruta más corta pasa por un tramo marcado con prohibición. Hay otra ruta más larga sin marcas. ¿Cuál se usa?", ["Un tramo con prohibición no se usa aunque sea más corto.", "La ruta más larga es la permitida."], "La ruta más larga, sin tramos prohibidos"),
    ],
    mistakes=[("Elegir siempre la ruta más corta sin mirar las marcas de prohibición.", "Un tramo bloqueado no se puede usar, aunque ahorre metros.", "Descarta primero los tramos bloqueados y luego compara."),
              ("Medir en el plano y no convertir los centímetros en metros antes de calcular el tiempo.", "La rapidez se da en metros por segundo; las distancias deben estar en metros.", "Aplica la escala antes de dividir entre la rapidez.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una ruta de evacuación?", "El camino señalado que lleva de forma segura a la salida o a un punto seguro", "El camino más corto entre dos puntos cualquiera de la faena", "El camino que usan los camiones para llevar el mineral", "La ruta de evacuación está señalada y debe llevar a un lugar seguro."),
        ("abc", "En Explotación Minera: ¿qué es un cruce en el plano de una mina subterránea?", "Un punto donde se encuentran dos o más galerías", "Una salida directa a superficie", "Un lugar donde se guardan equipos", "Un cruce une galerías; la salida a superficie es otro elemento del plano."),
        ("abc", "En Explotación Minera: ¿qué es una galería?", "Una labor casi horizontal de una mina subterránea", "Una labor vertical que une dos niveles", "Un escalón de una mina a cielo abierto", "La galería es horizontal o casi; la vertical que une niveles es otra labor."),
        ("=", "{F} ¿Cuántos metros representa en terreno el tramo C2–R?", "4*10", "Con escala 1:1.000, cada centímetro del plano vale 10 metros.", " m"),
        ("abc", "{F} ¿Qué tramo del plano está bloqueado?", "C1–S", "C1–C2", "C2–S", "La anotación del plano dice que el tramo C1–S está bloqueado y prohibido."),
        ("abc", "{F} ¿Para qué sirve la cámara de refugio de la ficha?", "Para esperar solo si no se puede salir, según el plan de emergencia", "Para ser una segunda salida a superficie", "Para guardar los equipos del taller", "El refugio no es una salida: es un lugar de espera señalado."),
        ("=", "{F} ¿Cuántos metros mide la ruta T–C1–C2–S?", "(3+5+8)*10", "Se suman los tramos en centímetros y se convierte con la escala.", " m"),
        ("abc", "{F} Con el tramo C1–S bloqueado, ¿qué ruta debe seguirse desde el taller hasta la salida?", "T–C1–C2–S", "T–C1–S", "T–C1–C2–R", "La ruta permitida que llega a la salida es la que pasa por C2."),
        ("=", "{F} ¿Cuántos metros más larga es la ruta T–C1–C2–S que la T–C1–S?", "(3+5+8)*10-(3+12)*10", "Se restan las distancias de las dos rutas en metros.", " m"),
        ("abc", "{F} Un trabajador propone usar el tramo C1–S «aunque esté bloqueado, porque es el más corto». ¿Qué corresponde?", "Respetar la prohibición y usar la ruta alternativa señalada", "Usarlo si va rápido", "Usarlo si nadie lo ve", "Un tramo bloqueado y prohibido no se usa, aunque sea el más corto."),
        ("abc", "{F} ¿Qué dato del plano es indispensable para estimar cuánto tarda una evacuación?", "La escala, para convertir centímetros del plano en metros reales", "La fecha de impresión del plano", "El nombre de quien lo dibujó", "Sin escala no se conoce la distancia real que hay que recorrer."),
        ("=", "{F} Una persona evacúa por la ruta permitida a 2 metros por segundo (valor de ejemplo). ¿Cuántos segundos tarda desde el taller hasta la salida?", "(3+5+8)*10//2", "Se calcula la distancia real de la ruta permitida y se divide entre la rapidez.", " s"),
        ("abc", "Un compañero te cuenta que de la entrada de un sector subterráneo sale humo y que hay personas adentro. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar con el plano a buscar a las personas", "Esperar a ver si el humo se pasa antes de avisar", "Entrar sin formación puede sumar otra víctima; lo correcto es avisar."),
    ],
    ctx=("abc", "En una charla de ejemplo, un instructor muestra un plano en que una galería tiene dos salidas: una de 6 cm, marcada con prohibición por trabajos, y otra de 9 cm, sin marcas, con escala 1:1.000. Un participante dice que usaría la de 6 cm «porque son 30 m menos». ¿Qué respondes?", "Que no se usa un tramo prohibido: se toma la de 9 cm, que mide 90 m y es la permitida", "Que sí, porque la distancia corta es lo más importante", "Que sí, si lleva linterna", "El criterio es la prohibición marcada; solo después se comparan distancias."),
    sc=[
        ("En Explotación Minera: ¿qué es una cámara de refugio?", "Un lugar señalado donde esperar solo si no se puede salir", "El refugio no reemplaza a la salida."),
        ("¿Qué se hace primero al analizar rutas de evacuación en un plano?", "Descartar los tramos bloqueados o prohibidos", "Después se comparan las rutas que quedan."),
        ("¿Cómo se pasa de centímetros del plano a metros reales?", "Aplicando la escala del plano", "La escala dice cuántos metros vale cada centímetro."),
    ],
    op=("Plano ficticio de la faena «Mina Demo Cerro Claro», escala 1:500: Bodega (B), Cruce (X), Salida (S) y Punto de reunión exterior (P). Tramos: B–X = 4 cm; X–S = 10 cm; X–P = 6 cm. El tramo X–S está marcado con prohibición por trabajos, pero X–P lleva al punto de reunión exterior. Escribe (a) cuántos metros reales mide B–X–P, (b) cuál ruta sigue una persona que sale de la bodega y por qué, (c) cuántos segundos tarda a 2 metros por segundo, (d) qué hace si ve humo en el tramo B–X y no puede avanzar.",
        "(a) (4 + 6) × 5 = 50 m. (b) B–X–P, porque X–S está prohibido. (c) 50 ÷ 2 = 25 s. (d) No sigue ni se acerca a la zona de riesgo, avisa a un adulto responsable y a emergencias según el plan de emergencia.",
        ["calcula la distancia con la escala", "elige la ruta respetando la prohibición", "estima el tiempo", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["usar el tramo prohibido", "no convertir con la escala", "intentar pasar por una zona con humo"],
        "Pregunta: «¿qué tramo descartas primero y por qué?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Dibuja una red de cuatro puntos con distancias en centímetros, bloquea un tramo y calcula la ruta permitida.",
    extend="Explica con un ejemplo por qué la ruta más corta no siempre es la mejor ruta de evacuación.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (plano de ejemplo, inventado). Plano del rajo de la faena ficticia «Mina Demo Cordillera», escala 1:5.000 (1 cm del plano = 50 m reales). Las curvas de nivel se dibujan cada 10 m de altura. Una rampa une el nivel de cota 2.400 m con el de cota 2.340 m y mide 12 cm en el plano (distancia horizontal). "
     "Alrededor del punto marcado «T» hay una zona de exclusión de tronadura de 4 cm de radio en el plano (valor ficticio, sin relación con distancias reales). Distancias medidas en el plano desde T: garita de control = 3 cm; oficina = 6 cm; taller = 9 cm. Límite de pendiente de rampa de la empresa (valor de ejemplo): 12 %.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico a un plano: calcular desniveles, pendientes de rampa y distancias reales, y comprobar si una instalación queda dentro de una zona de exclusión marcada en un plano.",
    prior=["Sé usar la escala de un plano.", "Sé calcular un porcentaje sencillo.", "Sé qué es la cota de un punto."],
    explain=[
        "Las curvas de nivel son líneas del plano que unen puntos de la misma cota; la equidistancia es la diferencia de altura entre dos curvas seguidas, por ejemplo 10 m. El desnivel entre dos puntos es la resta de sus cotas. La pendiente de una rampa se expresa en porcentaje: es el desnivel dividido entre la distancia horizontal, multiplicado por 100. Una pendiente de 10 % significa que se sube o se baja 10 m por cada 100 m horizontales.",
        "Para usar estos datos se mide en el plano, se pasa a metros con la escala y se compara con el límite que fija la empresa o la norma vigente. Una zona de exclusión de tronadura se dibuja como un círculo con su radio; una instalación cuya distancia al centro es menor que el radio queda dentro y no debe ocupar esa zona durante la tronadura. Los radios reales los fija el responsable autorizado según la norma vigente; aquí son valores de ejemplo.",
        f"Este cuaderno no enseña a diseñar ni ejecutar tronaduras: solo a leer lo que un plano indica. {EMER} {AVISO}",
    ],
    vocab=[("curva de nivel", "línea que une puntos de la misma cota"), ("equidistancia", "diferencia de altura entre dos curvas de nivel seguidas"), ("desnivel", "diferencia de cota entre dos puntos"), ("pendiente", "desnivel dividido entre la distancia horizontal, en porcentaje"), ("rampa", "camino inclinado que une dos niveles"), ("radio", "distancia desde el centro de un círculo hasta su borde")],
    worked=[
        ("Pendiente de un camino", "Un camino de acarreo de ejemplo baja 24 m a lo largo de 400 m horizontales. ¿Qué pendiente tiene?", ["El desnivel es 24 m y la distancia horizontal es 400 m.", "24 por 100 dividido entre 400 es 6 %."], "6 %"),
        ("Zona de exclusión", "En otro plano de ejemplo, escala 1:2.000, una zona de exclusión tiene radio de 5 cm y un contenedor de oficinas está a 4 cm del centro. ¿Está dentro?", ["El radio es 5 cm y la distancia es 4 cm.", "4 cm es menor que 5 cm."], "Sí, el contenedor está dentro de la zona"),
    ],
    mistakes=[("Calcular la pendiente dividiendo el desnivel entre la medida del plano sin pasarla a metros.", "Desnivel y distancia deben estar en las mismas unidades.", "Convierte los centímetros del plano a metros con la escala y luego divide."),
              ("Creer que una instalación está fuera de la zona de exclusión porque está cerca del borde.", "Si la distancia al centro es menor que el radio, está dentro.", "Compara la distancia con el radio en las mismas unidades.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una curva de nivel?", "Una línea que une puntos del terreno de la misma cota", "Una línea que marca la ruta más corta de un camino", "Una línea que separa dos propiedades mineras", "Las curvas de nivel representan la altura del terreno en el plano."),
        ("abc", "En Explotación Minera: ¿qué es el desnivel entre dos puntos?", "La diferencia de cota entre ellos", "La distancia horizontal entre ellos", "La suma de sus cotas", "El desnivel es una diferencia de altura, no una distancia horizontal."),
        ("abc", "En Explotación Minera: ¿cómo se calcula la pendiente de una rampa en porcentaje?", "Desnivel dividido entre distancia horizontal, por 100", "Distancia horizontal dividida entre desnivel, por 100", "Suma de las cotas dividida entre dos", "La pendiente compara cuánto sube o baja la rampa con lo que avanza en horizontal."),
        ("=", "{F} ¿Cuántos metros reales mide la distancia horizontal de la rampa?", "12*50", "Se multiplican los centímetros del plano por los 50 metros que vale cada uno.", " m"),
        ("=", "{F} ¿Cuántos metros es el desnivel de la rampa entre las dos cotas?", "2400-2340", "Se resta la cota menor a la mayor.", " m"),
        ("=", "{F} Con la equidistancia de 10 m, ¿cuántos intervalos entre curvas de nivel hay entre las dos cotas de la rampa?", "(2400-2340)//10", "Se divide el desnivel entre la equidistancia de las curvas.", " intervalos"),
        ("=", "{F} ¿Qué pendiente en porcentaje tiene la rampa?", "60*100//(12*50)", "Se divide el desnivel entre la distancia horizontal y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos metros reales tiene de radio la zona de exclusión?", "4*50", "Se multiplica el radio del plano por los metros que vale cada centímetro.", " m"),
        ("abc", "{F} ¿Qué instalaciones quedan dentro de la zona de exclusión?", "Solo la garita de control", "La garita de control y la oficina", "La oficina y el taller", "Solo la garita está a menos de 4 cm de T; la oficina y el taller están más lejos."),
        ("abc", "{F} ¿Cumple la rampa el límite de pendiente de la empresa?", "Sí, porque su pendiente de 10 % es menor que el límite de 12 %", "No, porque 10 % es distinto de 12 %", "No, porque la rampa mide más de 100 m", "Cumple si su pendiente no supera el límite de ejemplo."),
        ("abc", "{F} ¿Qué corresponde respecto de la garita de control, que está dentro de la zona de exclusión?", "Que quede sin personas dentro de la zona durante la tronadura, según lo que ordene el responsable autorizado", "Que la garita se mueva sola con la tronadura", "Que nadie la tome en cuenta porque los planos no marcan garitas", "Una instalación dentro de la zona de exclusión no debe tener personas durante la tronadura."),
        ("=", "{F} Se proyecta otra rampa que bajará 30 m con una pendiente de 10 %. ¿Cuántos metros horizontales recorre esa rampa?", "30*100//10", "La distancia horizontal es el desnivel por 100 dividido entre la pendiente.", " m"),
        ("abc", "Un caminante de ejemplo ve, desde el borde del rajo, que se desprende un bloque de roca cerca de un compañero. ¿Qué corresponde según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse al borde para ayudar al compañero", "Medir en el plano la distancia hasta el compañero", "Acercarse puede provocar otro desprendimiento; corresponde avisar."),
    ],
    ctx=("abc", "En un plano de ejemplo a escala 1:2.000, una bodega está a 7 cm del centro de una zona de exclusión de 6 cm de radio. Un compañero dice que «está tan cerca del borde que hay que contarla como dentro». ¿Qué respondes?", "Que 7 cm es mayor que 6 cm, así que la bodega queda fuera de la zona dibujada, y que cualquier duda se consulta al responsable autorizado", "Que está dentro porque está cerca del borde", "Que está dentro porque la zona es solo un dibujo", "La distancia mayor que el radio indica que está fuera; la cercanía al borde no cambia la comparación."),
    sc=[
        ("En Explotación Minera: ¿qué dos datos se necesitan para calcular una pendiente?", "El desnivel y la distancia horizontal", "La pendiente compara cuánto sube la rampa con lo que avanza."),
        ("¿Qué indica una distancia menor que el radio de una zona de exclusión?", "Que el punto está dentro de la zona", "Menor que el radio significa más cerca del centro."),
        ("¿Qué se debe hacer con las medidas del plano antes de calcular?", "Pasarlas a metros con la escala", "Todos los datos deben estar en las mismas unidades."),
    ],
    op=("Plano ficticio del rajo «Mina Demo Cerro Claro», escala 1:2.000 (1 cm = 20 m). Una rampa une la cota 1.800 m con la cota 1.784 m y mide 8 cm en el plano. La zona de exclusión de ejemplo tiene 3 cm de radio y el comedor está a 5 cm del centro. Escribe (a) el desnivel y la distancia horizontal real, (b) la pendiente en porcentaje, (c) si el comedor está dentro o fuera de la zona, (d) qué harías si el comedor estuviera dentro.",
        "(a) Desnivel 16 m; distancia horizontal 8 × 20 = 160 m. (b) 16 × 100 ÷ 160 = 10 %. (c) Fuera, porque 5 cm es mayor que 3 cm. (d) Avisar al responsable para que ordene sacar a las personas de esa instalación durante la tronadura, sin decidirlo uno mismo.",
        ["calcula el desnivel y la distancia real", "calcula la pendiente", "compara con el radio", "deriva la decisión al responsable"],
        ["hoja con las cuatro respuestas"],
        ["no convertir con la escala", "dividir al revés el desnivel y la distancia", "decidir solo sobre la tronadura"],
        "Pregunta: «¿qué dos números dividiste y en qué unidad estaban?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una rampa con dos cotas y una distancia en el plano a otra escala, y calcula su pendiente.",
    extend="Explica con un ejemplo por qué una pendiente muy alta puede ser un peligro para el tránsito de vehículos.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (documentos de ejemplo, inventados). Dos planos de planta del mismo sector de la faena ficticia «Mina Demo Piedra Azul», ambos a escala 1:1.000. Plano P-1: revisión B, fecha 10 de enero de ejemplo; tiene título, escala, norte y fecha, pero no tiene leyenda ni firma de aprobación y su estado es «reemplazado». Su ruta de evacuación mide 17 cm hasta la salida antigua. "
     "Plano P-2: revisión D, fecha 2 de agosto de ejemplo; tiene título, escala, leyenda, fecha y firma de aprobación, pero no tiene norte; su estado es «vigente». Su ruta de evacuación mide 21 cm hasta una salida nueva. "
     "Lista de verificación de calidad de un plano (de ejemplo): 1 título; 2 escala; 3 leyenda; 4 norte; 5 revisión y fecha; 6 firma de aprobación; 7 estado vigente.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos planos del mismo sector, verificar su calidad con una lista de verificación y decidir cuál usar y qué observaciones registrar.",
    prior=["Sé qué partes tiene un plano.", "Sé usar la escala.", "Sé qué es una revisión vigente."],
    explain=[
        "Verificar la calidad de un plano es comprobar que cumple una lista de ítems antes de usarlo: título, escala, leyenda, norte, revisión y fecha, firma de aprobación y estado vigente. Cada ítem que falta es una observación, que se anota y se informa a quien elaboró el plano para que lo corrija. Un plano con muchas observaciones o con estado «reemplazado» no se usa para decidir.",
        "Al comparar dos alternativas, no basta con mirar cuál ruta es más corta: primero se descarta el plano que no está vigente, y luego se evalúa la ruta del plano que sí lo está. Una salida nueva que aparece solo en el plano vigente indica que las labores cambiaron, y el personal debe ser informado según el plan de la empresa.",
        f"Tampoco corresponde corregir a mano un plano oficial ni dibujar sobre él: las correcciones las hace quien lo elabora y las aprueba la jefatura. {EMER} {AVISO}",
    ],
    vocab=[("lista de verificación", "lista de ítems que se comprueban uno a uno"), ("observación", "ítem que falta o está mal y se anota para corregirlo"), ("estado reemplazado", "plano que ya no está en uso porque hay una versión nueva"), ("estado vigente", "plano que está en uso"), ("alternativa", "una de las opciones que se comparan")],
    worked=[
        ("Contar cumplimientos", "Un plano de ejemplo de un botadero cumple 5 de los 7 ítems de la lista de verificación. ¿Cuántas observaciones tiene?", ["Cada ítem que no se cumple es una observación.", "7 menos 5 son 2."], "2 observaciones"),
        ("Elegir un plano", "De dos planos de ejemplo de una bodega, uno está vigente pero le falta el norte y el otro está reemplazado y completo. ¿Cuál se usa?", ["El estado vigente es lo primero que se exige.", "Al vigente se le anota la observación del norte."], "El vigente, con la observación anotada"),
    ],
    mistakes=[("Elegir el plano que tiene la ruta más corta sin mirar su estado.", "Un plano reemplazado puede mostrar salidas que ya no existen.", "Primero se confirma que el estado sea vigente."),
              ("Corregir a mano una observación sobre el plano oficial.", "Las correcciones las hace quien elabora el plano y las aprueba la jefatura.", "Anota la observación e informa a quien corresponde.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una lista de verificación de un plano?", "Una lista de ítems que se comprueban uno a uno antes de usar el plano", "Una lista de las personas que deben firmar el plano", "Una lista de las labores que se construirán", "La lista de verificación sirve para comprobar si el plano cumple lo mínimo."),
        ("abc", "En Explotación Minera: ¿qué significa que un plano tenga estado «reemplazado»?", "Que ya no está en uso porque hay una versión nueva", "Que está listo para aprobarse", "Que es el plano más reciente", "Un plano reemplazado ya fue sustituido por otro y no debe usarse."),
        ("abc", "En Explotación Minera: ¿qué es una observación en la verificación de un plano?", "Un ítem que falta o está mal y se anota para corregirlo", "Una opinión personal sobre el diseño de la mina", "El resultado final aprobado del plano", "Las observaciones son los ítems incumplidos que se informan."),
        ("=", "{F} ¿Cuántos metros mide en terreno la ruta de evacuación del plano P-1?", "17*10", "Con escala 1:1.000, cada centímetro del plano vale 10 metros.", " m"),
        ("=", "{F} ¿Cuántos ítems de la lista de verificación cumple el plano P-2?", "7-1", "El plano P-2 cumple todos los ítems salvo el norte.", " ítems"),
        ("abc", "{F} ¿Qué observación tiene el plano P-2?", "No tiene norte", "No tiene leyenda", "No tiene firma de aprobación", "El plano P-2 tiene leyenda y firma, pero no norte."),
        ("=", "{F} ¿Cuántas observaciones tiene el plano P-1?", "7-4", "P-1 cumple cuatro ítems de la lista y las observaciones son los ítems restantes.", " observaciones"),
        ("abc", "{F} ¿Cuál plano debe usar la jefatura para organizar una evacuación y por qué?", "El P-2, porque es el vigente aunque le falte el norte", "El P-1, porque tiene la ruta más corta", "El P-1, porque está fechado antes", "El estado vigente es el primer criterio para usar un plano."),
        ("=", "{F} ¿Cuántos metros más larga es la ruta del plano P-2 que la del P-1?", "(21-17)*10", "Se restan los centímetros de las dos rutas y se convierte con la escala.", " m"),
        ("abc", "{F} ¿Por qué la ruta de P-2 llega a una salida distinta?", "Porque las labores cambiaron y existe una salida nueva que solo aparece en el plano vigente", "Porque el plano P-2 tiene un error de dibujo", "Porque el plano P-1 usa otra escala", "Una salida nueva solo en el plano vigente indica que las labores cambiaron."),
        ("abc", "{F} Un supervisor sugiere dibujar con lápiz el norte en el plano P-2 para completarlo. ¿Qué corresponde?", "Anotar la observación e informar a quien elaboró el plano para que lo corrija", "Dibujar el norte con lápiz, porque es un dato obvio", "Descartar el plano P-2 y usar el P-1", "Un plano oficial lo corrige quien lo elabora y lo aprueba la jefatura."),
        ("=", "{F} Una persona evacúa por la ruta del plano P-2 a 3 metros por segundo (valor de ejemplo). ¿Cuántos segundos tarda?", "21*10//3", "Se convierte la distancia a metros y se divide entre la rapidez.", " s"),
        ("abc", "Mientras revisas un plano de ejemplo, un compañero te cuenta que en esa zona acaba de ocurrir un desprendimiento de rocas con personas atrapadas. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Ir a la zona con el plano para ubicar el punto exacto", "Seguir revisando el plano y avisar al terminar", "La emergencia se avisa de inmediato; acercarse sin formación pone en riesgo a más personas."),
    ],
    ctx=("abc", "Te entregan dos planos de ejemplo de una zona de acopio: el A, completo y firmado, con estado «reemplazado», y el B, firmado pero sin leyenda, con estado «vigente». Un colega dice que usará el A porque está completo. ¿Qué respondes?", "Que se usa el B, que es el vigente, y que la falta de leyenda se anota como observación para corregirla", "Que se usa el A, porque lo completo pesa más que el estado", "Que se usan ambos mezclados y se elige el que convenga", "El estado vigente es indispensable; la falta de leyenda se informa."),
    sc=[
        ("En Explotación Minera: ¿qué se hace con un ítem que falta en un plano?", "Se anota como observación y se informa a quien lo elaboró", "Las correcciones las hace quien elabora el plano."),
        ("¿Qué se revisa primero al comparar dos planos del mismo sector?", "Que estén vigentes", "Un plano reemplazado no sirve para decidir."),
        ("¿Quién corrige un plano oficial?", "Quien lo elabora, con aprobación de la jefatura", "No se corrige a mano sobre el plano oficial."),
    ],
    op=("Dos planos ficticios del mismo sector de la faena «Mina Demo Cerro Claro», escala 1:500. Plano X: revisión A, estado «reemplazado», completo, ruta de 20 cm. Plano Y: revisión C, estado «vigente», sin firma de aprobación, ruta de 24 cm. Escribe (a) cuál plano usarías y por qué, (b) qué observación anotarías, (c) cuántos metros mide la ruta del plano que elegiste, (d) a quién informarías la observación.",
        "(a) El Y, porque es el vigente. (b) Que no tiene la firma de aprobación. (c) 24 × 5 = 120 m. (d) A quien elaboró el plano y a la jefatura que debe aprobarlo.",
        ["elige el plano vigente", "anota la observación correcta", "calcula la distancia real", "identifica a quién informar"],
        ["hoja con las cuatro respuestas"],
        ["elegir el plano por la ruta más corta", "olvidar la conversión con la escala", "corregir el plano a mano"],
        "Pregunta: «¿qué mira primero un jefe de turno al elegir entre dos planos?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Dibuja una lista de verificación de siete ítems, inventa un plano que cumple cuatro y anota sus tres observaciones.",
    extend="Explica con un ejemplo por qué el estado del plano pesa más que lo completo que esté.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (caso de ejemplo, inventado). La faena subterránea ficticia «Mina Demo Río Hondo» tiene una galería principal de 200 m. Su matriz de peligros anota: caída de rocas desde el techo (probabilidad 4 y gravedad 5), filtración de agua que debilita la roca (probabilidad 5 y gravedad 3), tránsito de equipos pesados (probabilidad 3 y gravedad 4) y ruido (probabilidad 5 y gravedad 1). "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. El proyecto de fortificación de ejemplo indica pernos de anclaje y malla en toda la galería. Personal de ejemplo en un turno: 6 personas en inspección, 9 en mantención y 3 en prevención de riesgos.")
build(
    O2, 1, F,
    use="Aprenderé qué es la fortificación de una mina, por qué se necesita, qué peligros la hacen necesaria y por qué solo personal autorizado la instala y la mantiene.",
    prior=["Sé qué es un peligro y qué es un riesgo.", "Sé calcular un puntaje multiplicando dos números.", "Sé que las tareas de riesgo las hacen personas autorizadas."],
    explain=[
        "El macizo rocoso es la roca en su lugar natural, con sus grietas y capas. Cuando se abre una labor, la roca que rodea el espacio puede aflojarse y desprenderse. La fortificación, también llamada sostenimiento, es el conjunto de elementos que se colocan para dar soporte a la roca y evitar su caída: los pernos de anclaje son barras de acero que se fijan en la roca, la malla es una red de acero que retiene trozos pequeños y el hormigón proyectado es una capa de hormigón aplicada sobre la roca. También se fortifican los taludes de una mina a cielo abierto, que son las paredes inclinadas del rajo.",
        "El proyecto minero indica qué fortificación lleva cada zona, según las estructuras geológicas y el método de explotación. La fortificación no elimina todo el peligro: la roca cambia con el tiempo, con el agua y con las vibraciones, por eso se inspecciona y se mantiene. En la matriz de ejemplo, el puntaje de riesgo es probabilidad por gravedad y se atiende primero el mayor.",
        f"Instalar y mantener fortificación exige formación, equipos certificados, permiso de trabajo y personal autorizado; este cuaderno no enseña a hacerlo. La autoridad minera fiscaliza que se cumpla la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("macizo rocoso", "roca en su lugar natural, con sus grietas y capas"), ("fortificación", "conjunto de elementos que dan soporte a la roca de una labor; también se llama sostenimiento"), ("perno de anclaje", "barra de acero que se fija en la roca"), ("malla", "red de acero que retiene trozos pequeños de roca"), ("hormigón proyectado", "capa de hormigón aplicada sobre la roca"), ("talud", "pared inclinada de una mina a cielo abierto")],
    worked=[
        ("Puntaje de riesgo", "En la matriz de ejemplo de una bodega de repuestos, el peligro «puerta sin señal» tiene probabilidad 2 y gravedad 3. ¿Qué puntaje resulta?", ["Se multiplica la probabilidad por la gravedad.", "2 por 3 son 6."], "6 puntos"),
        ("Peligro y riesgo en un talud", "En el talud de un camino de ejemplo se ve una grieta nueva. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la grieta nueva, porque el talud puede desprenderse.", "El riesgo es que se desprenda roca y golpee a una persona o a un vehículo."], "Peligro: la grieta; riesgo: que se desprenda roca y cause daño"),
    ],
    mistakes=[("Creer que una galería fortificada ya no necesita inspecciones.", "La roca cambia con el tiempo, el agua y las vibraciones.", "La fortificación se inspecciona y se mantiene de forma periódica."),
              ("Creer que quien entiende para qué sirve un perno ya puede instalarlo.", "Instalar fortificación exige formación, equipos certificados, permiso y autorización.", "Aprende el concepto aquí y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es la fortificación de una labor?", "El conjunto de elementos que dan soporte a la roca para evitar que se desprenda", "El conjunto de rejas que impiden la entrada de personas ajenas a la faena", "El proceso de separar el mineral de la roca sin valor", "La fortificación sostiene la roca; no es un cierre de acceso ni un proceso de separación."),
        ("abc", "En Explotación Minera: ¿qué es el macizo rocoso?", "La roca en su lugar natural, con sus grietas y capas", "El mineral ya extraído y apilado", "El conjunto de máquinas de una faena", "El macizo es la roca antes de ser extraída."),
        ("abc", "En Explotación Minera: ¿para qué sirve la malla de una fortificación?", "Para retener trozos pequeños de roca que podrían desprenderse", "Para unir dos galerías entre sí", "Para medir la humedad de la roca", "La malla es una red de acero que contiene los pedazos sueltos."),
        ("=", "{F} ¿Cuántas personas hay en total en el turno de la ficha?", "6+9+3", "Se suman las personas de inspección, mantención y prevención.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «caída de rocas desde el techo»?", "Que una roca golpee a una persona o a un equipo", "Que la galería sea muy larga", "Que se necesite más malla", "El riesgo es el daño posible, no una característica de la galería."),
        ("abc", "{F} ¿Por qué la ficha indica «filtración de agua» como un peligro para la fortificación?", "Porque el agua puede debilitar la roca y hacer que se desprenda", "Porque el agua hace que los pernos sean más livianos", "Porque el agua obliga a trabajar solo de noche", "El agua puede aflojar la roca y reducir la estabilidad."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la caída de rocas desde el techo?", "4*5", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el tránsito de equipos pesados?", "3*4", "Se multiplican la probabilidad y la gravedad de ese peligro.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál de los cuatro peligros se debe atender primero?", "La caída de rocas, porque tiene el puntaje mayor (20)", "La filtración de agua, porque su probabilidad es la más alta", "El ruido, porque ocurre casi siempre", "Se atiende primero el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Un joven en práctica dice: «ya sé para qué sirven los pernos, así que puedo ayudar a instalarlos». ¿Qué es correcto?", "Saber para qué sirven no lo habilita: la instalación exige formación, permiso y personal autorizado", "Puede ayudar si usa casco y guantes", "Puede ayudar si un compañero lo guía desde lejos", "El equipo de protección no reemplaza la formación ni la autorización."),
        ("abc", "{F} ¿Por qué una galería con pernos y malla igual debe inspeccionarse?", "Porque la roca puede cambiar con el tiempo, con el agua y con las vibraciones", "Porque los pernos se disuelven con la humedad", "Porque la malla se mueve sola de lugar", "La fortificación reduce el peligro, pero la roca sigue cambiando."),
        ("=", "{F} Para un simulacro, el personal de inspección y de mantención se reparte en grupos de 5 personas. ¿Cuántos grupos se forman?", "(6+9)//5", "Se suma el personal de las dos áreas y se divide entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, ves que cae polvo y pequeñas rocas del techo de una galería donde hay personas trabajando. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a avisar a las personas con tu propia linterna", "Esperar a ver si se detiene antes de avisar", "Entrar a una zona con caída de rocas sin formación pone en riesgo a otra persona."),
    ],
    ctx=("abc", "Un amigo de ejemplo que trabaja en una faena te dice: «Ven, te muestro cómo se colocan los pernos en el techo, es fácil». ¿Qué respondes?", "Que no, porque hacerlo exige formación, equipos certificados, permiso y autorización, y que consultarás a un adulto responsable", "Que sí, pero solo un perno", "Que sí, si se hace sin que nadie lo vea", "Instalar fortificación no es una tarea para quien no está autorizado."),
    sc=[
        ("En Explotación Minera: ¿qué es un perno de anclaje?", "Una barra de acero que se fija en la roca para darle soporte", "Los pernos forman parte de los elementos de fortificación."),
        ("En Explotación Minera: ¿qué es un talud?", "La pared inclinada de una mina a cielo abierto", "Los taludes del rajo también se fortifican con elementos de soporte."),
        ("¿Cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("La faena ficticia «Mina Demo Cerro Claro» tiene una galería de acceso de 60 m en la que el techo muestra, en un tramo de 10 m, roca muy fracturada y manchas de humedad. Escribe (a) cuál es el peligro y cuál el riesgo, (b) un elemento de fortificación que podría proponer un proyecto para ese tramo, (c) por qué ese elemento necesitaría inspección periódica, (d) quién instala y quién no.",
        "(a) Peligro: la roca fracturada y húmeda del techo; riesgo: que se desprenda y golpee a una persona o a un equipo. (b) Malla con pernos de anclaje, según lo indique el proyecto. (c) Porque la roca cambia con el tiempo, el agua y las vibraciones. (d) Lo instala personal formado y autorizado con permiso de trabajo; un estudiante o una persona sin autorización no.",
        ["distingue peligro y riesgo", "nombra un elemento de fortificación", "justifica la inspección periódica", "aclara quién instala"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que la fortificación elimina el peligro para siempre", "no aclarar que lo instala personal autorizado"],
        "Pregunta: «¿qué puede cambiar en la roca aunque esté fortificada?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una matriz de tres peligros de una galería con probabilidad y gravedad, calcula los puntajes y ordénalos de mayor a menor.",
    extend="Explica con un ejemplo por qué el agua puede ser un peligro para la estabilidad de una galería.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (documentos de ejemplo, inventados). Extracto del proyecto de fortificación de la «Galería Norte», de 120 m, de la faena ficticia «Mina Demo Piedra Azul». Tramo A (0 a 50 m): roca firme con pocas diaclasas; pernos de anclaje y malla. Tramo B (50 a 90 m): cruza una falla; pernos, malla y hormigón proyectado. Tramo C (90 a 120 m): roca muy fracturada; marcos de acero. "
     "Una diaclasa o junta es una fractura de la roca sin desplazamiento; una falla es una fractura con desplazamiento de los bloques. Documentos del proyecto: plano de fortificación, informe geomecánico, registro de inspección y permiso de trabajo. "
     "Roles: el geomecánico estudia la roca y recomienda el tipo de fortificación; el supervisor organiza el trabajo; el personal autorizado de fortificación ejecuta; el prevencionista vela por la seguridad.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos de estructura geológica y fortificación, los documentos de un proyecto de fortificación y el rol de cada persona que participa.",
    prior=["Sé qué es la fortificación y para qué sirve.", "Sé leer un cuadro con tramos y distancias.", "Sé qué es un permiso de trabajo."],
    explain=[
        "Las estructuras geológicas son las fracturas y capas del macizo rocoso. Una diaclasa o junta es una fractura sin desplazamiento; una falla es una fractura en que los bloques se desplazaron; la estratificación es la disposición de la roca en capas; el contacto es el límite entre dos tipos de roca. Los lugares con muchas estructuras suelen necesitar más fortificación, por eso el proyecto la fija por tramos.",
        "Los documentos de un proyecto de fortificación son: el plano de fortificación, que muestra qué elemento va en cada tramo; el informe geomecánico, que explica cómo está la roca; el registro de inspección, que anota lo observado en cada visita; y el permiso de trabajo, que autoriza una tarea de riesgo a personal definido. Un documento sin fecha ni firma no sirve para decidir.",
        f"Cada rol tiene su límite: el geomecánico recomienda, el supervisor organiza, el personal autorizado ejecuta y el prevencionista vela por la seguridad. Nadie puede cambiar el tipo de fortificación por su cuenta. {EMER} {AVISO}",
    ],
    vocab=[("estructura geológica", "fractura o capa del macizo rocoso"), ("diaclasa", "fractura de la roca sin desplazamiento; también se llama junta"), ("falla", "fractura de la roca con desplazamiento de los bloques"), ("estratificación", "disposición de la roca en capas"), ("informe geomecánico", "documento que explica el estado de la roca y recomienda la fortificación"), ("registro de inspección", "documento donde se anota lo observado en cada visita"), ("marco de acero", "estructura de acero que sostiene una labor")],
    worked=[
        ("Largo de un tramo", "En el proyecto de otra galería de ejemplo, el tramo X va de 20 a 75 m. ¿Cuántos metros mide?", ["Se resta el punto inicial al final.", "75 menos 20 son 55 m."], "55 metros"),
        ("Rol de una persona", "En una faena de ejemplo, quien estudia la roca y recomienda qué fortificación necesita una zona es el geomecánico. ¿Puede el supervisor cambiar esa recomendación por su cuenta?", ["El supervisor organiza el trabajo, pero no define el tipo de fortificación.", "Un cambio debe pasar por quien la recomendó y quedar documentado."], "No, el cambio debe consultarse y documentarse"),
    ],
    mistakes=[("Creer que cualquier fractura de la roca es una falla.", "Una falla tiene desplazamiento de los bloques; una diaclasa no.", "Pregúntate si los bloques se desplazaron."),
              ("Creer que el supervisor puede cambiar el tipo de fortificación si le parece más cómodo.", "El tipo lo recomienda el geomecánico y lo fija el proyecto.", "Cualquier cambio se consulta y se documenta.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una falla geológica?", "Una fractura de la roca con desplazamiento de los bloques", "Una fractura de la roca sin desplazamiento", "Una capa de roca más dura que las demás", "La falla se distingue por el desplazamiento de los bloques."),
        ("abc", "En Explotación Minera: ¿qué es una diaclasa?", "Una fractura de la roca sin desplazamiento", "Una fractura con desplazamiento de los bloques", "Un perno que se fija en la roca", "La diaclasa o junta es una fractura sin desplazamiento."),
        ("abc", "En Explotación Minera: ¿qué documento anota lo observado en cada visita de inspección?", "El registro de inspección", "El plano de fortificación", "El informe geomecánico", "El registro deja constancia de lo observado en cada visita."),
        ("=", "{F} ¿Cuántos metros mide el tramo B de la galería?", "90-50", "Se resta el punto inicial al final del tramo.", " m"),
        ("abc", "{F} ¿Qué fortificación indica el proyecto para el tramo C?", "Marcos de acero", "Pernos y malla", "Hormigón proyectado solamente", "El tramo C, de roca muy fracturada, lleva marcos de acero."),
        ("abc", "{F} ¿Por qué el tramo B lleva hormigón proyectado además de pernos y malla?", "Porque cruza una falla y necesita más soporte", "Porque está más cerca de la entrada", "Porque el tramo A ya tiene malla", "El proyecto refuerza la fortificación donde hay una estructura como una falla."),
        ("=", "{F} ¿Cuántos metros de la galería tienen pernos de anclaje y malla (tramos A y B)?", "(50-0)+(90-50)", "Se suman los largos de los dos tramos que llevan esos elementos.", " m"),
        ("abc", "{F} ¿Quién recomienda el tipo de fortificación según los roles de la ficha?", "El geomecánico", "El supervisor", "El prevencionista", "El geomecánico estudia la roca y recomienda; el supervisor organiza."),
        ("abc", "{F} ¿Qué documento muestra qué elemento va en cada tramo?", "El plano de fortificación", "El permiso de trabajo", "El registro de inspección", "El plano ubica los elementos; el permiso autoriza a quién y cuándo."),
        ("abc", "{F} Un supervisor propone usar solo malla en el tramo B para ahorrar tiempo. ¿Qué corresponde?", "No hacerlo por su cuenta: el cambio se consulta con quien recomendó la fortificación y se documenta", "Hacerlo si el grupo está de acuerdo", "Hacerlo si el tramo parece estable", "El tipo de fortificación lo fija el proyecto, no la comodidad del equipo."),
        ("abc", "{F} ¿Por qué un registro de inspección sin fecha ni firma no sirve para decidir?", "Porque no se sabe cuándo se hizo ni quién se responsabiliza de lo anotado", "Porque los registros solo valen si son muy extensos", "Porque la fecha es un adorno del documento", "Un registro necesita fecha y firma para ser confiable."),
        ("=", "{F} El proyecto de ejemplo indica un marco de acero por cada 6 m de largo del tramo C. ¿Cuántos marcos hacen falta en el tramo C?", "(120-90)//6", "Se divide el largo del tramo entre la separación de los marcos.", " marcos"),
        ("abc", "Una persona te cuenta que en una galería de ejemplo se está desprendiendo roca del techo y que un trabajador quedó atrapado. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a levantar las rocas para liberarlo", "Esperar a que llegue el geomecánico antes de avisar", "Entrar sin formación puede provocar otro desprendimiento."),
    ],
    ctx=("abc", "Una compañera de práctica te muestra el informe geomecánico de otra galería de ejemplo y dice: «ya leí el informe, así que puedo cambiar el tipo de fortificación en el tramo dudoso». ¿Qué respondes?", "Que no: el cambio lo recomienda el geomecánico y lo fija el proyecto, y tú consultas a un adulto responsable", "Que sí, porque el informe da permiso", "Que sí, si se anota después en el registro", "Un informe se lee y se consulta; no autoriza a modificar el proyecto."),
    sc=[
        ("En Explotación Minera: ¿qué diferencia una falla de una diaclasa?", "La falla tiene desplazamiento de los bloques", "La diaclasa es una fractura sin desplazamiento."),
        ("En Explotación Minera: ¿qué hace el geomecánico?", "Estudia la roca y recomienda el tipo de fortificación", "Recomienda; no ejecuta ni autoriza trabajos de riesgo."),
        ("¿Para qué sirve el permiso de trabajo?", "Para autorizar una tarea de riesgo a personal definido", "El permiso nombra quién, qué y cuándo."),
    ],
    op=("Proyecto ficticio de la «Galería Sur» de la faena «Mina Demo Cerro Claro», de 80 m: tramo 1 de 0 a 30 m (roca firme, pernos y malla) y tramo 2 de 30 a 80 m (cruza una falla, pernos, malla y hormigón proyectado). Escribe (a) el largo de cada tramo, (b) por qué el tramo 2 lleva más elementos, (c) qué documento usarías para saber qué elemento va en cada tramo, (d) quién decide un cambio y quién no.",
        "(a) Tramo 1: 30 m; tramo 2: 50 m. (b) Porque cruza una falla y necesita más soporte. (c) El plano de fortificación. (d) Lo recomienda el geomecánico y lo fija el proyecto; el supervisor o el trabajador no cambian el tipo por su cuenta.",
        ["calcula el largo de los tramos", "relaciona la estructura con el refuerzo", "elige el documento correcto", "asigna los roles"],
        ["hoja con las cuatro respuestas"],
        ["confundir falla con diaclasa", "elegir el permiso de trabajo en vez del plano", "creer que el supervisor decide el tipo de fortificación"],
        "Pregunta: «¿quién recomienda y quién organiza?». Si no responde, pídele que relea el tercer párrafo de la explicación."),
    reinforce="Inventa un proyecto de 100 m con tres tramos y asigna a cada uno un elemento de fortificación y una razón.",
    extend="Explica con un ejemplo por qué los documentos de un proyecto deben tener fecha y firma.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (caso de ejemplo, inventado). Registro de inspección de la «Galería Poniente» de la faena ficticia «Mina Demo Lomas Bajas», con 8 puntos revisados por personal autorizado. P1: sin novedad. P2: placa de un perno doblada. P3: sin novedad. P4: malla con una rotura pequeña. P5: grieta nueva en el hormigón proyectado con filtración de agua. P6: sin novedad. P7: trozo de roca caído al piso, sin personas cerca. P8: sin novedad. "
     "Clasificación de ejemplo: «sin novedad»; «observación», que se informa a la jefatura para programar su corrección por personal autorizado; «hallazgo crítico», que se informa de inmediato, se señaliza y se restringe la zona según el plan de la empresa.")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel el registro de una inspección de fortificación: clasificar hallazgos, contar y calcular porcentajes, y decidir a quién se informa cada cosa.",
    prior=["Sé qué es un registro de inspección.", "Sé calcular un porcentaje sencillo.", "Sé qué es un hallazgo."],
    explain=[
        "Un hallazgo es lo que una inspección encuentra. En la clasificación de ejemplo, los hallazgos se agrupan en tres: «sin novedad» cuando todo está en orden, «observación» cuando hay un daño menor que se debe corregir y «hallazgo crítico» cuando hay una señal de que la roca puede desprenderse, como una grieta nueva con filtración o una caída de roca. Cada categoría tiene una respuesta distinta.",
        "Una observación se informa a la jefatura para programar la corrección. Un hallazgo crítico se informa de inmediato, se señaliza y se restringe el acceso según el plan de la empresa; quien no es personal autorizado no se acerca a mirar ni a corregir. Un porcentaje de puntos sin novedad es los puntos sin novedad por 100 dividido entre los puntos revisados.",
        f"Analizar el registro en papel permite entender cómo se decide, pero no habilita para inspeccionar ni reparar fortificación. {EMER} {AVISO}",
    ],
    vocab=[("hallazgo", "lo que una inspección encuentra"), ("observación", "daño menor que se informa para programar su corrección"), ("hallazgo crítico", "señal de que la roca puede desprenderse y que exige aviso inmediato y restricción de la zona"), ("sin novedad", "punto revisado en que todo está en orden"), ("señalizar", "marcar una zona con avisos para que nadie entre")],
    worked=[
        ("Clasificar un hallazgo", "En una inspección de ejemplo de un talud, se anota una malla con una abolladura pequeña y sin rotura. ¿Cómo se clasifica?", ["Es un daño menor, no una señal de desprendimiento.", "Se clasifica como observación y se informa a la jefatura."], "Observación"),
        ("Porcentaje de puntos", "En otra inspección de ejemplo de 10 puntos, 7 están sin novedad. ¿Qué porcentaje es?", ["Se multiplican por 100 los puntos sin novedad y se divide entre los revisados.", "7 por 100 dividido entre 10 es 70."], "70 %"),
    ],
    mistakes=[("Clasificar una grieta nueva con filtración como observación porque «no se ha caído nada».", "Es una señal de que la roca puede desprenderse y se trata como hallazgo crítico.", "Ante una señal de desprendimiento se informa de inmediato y se restringe la zona."),
              ("Creer que quien encuentra un hallazgo crítico debe acercarse a repararlo.", "La reparación la hace personal autorizado; los demás se alejan y avisan.", "No te acerques a la zona de riesgo: avisa a un adulto responsable.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un hallazgo crítico en una inspección de fortificación?", "Una señal de que la roca puede desprenderse y que exige aviso inmediato", "Un daño menor que se corrige en la próxima mantención", "Un punto revisado en que todo está en orden", "Lo crítico es lo que indica un posible desprendimiento."),
        ("abc", "En Explotación Minera: ¿qué es una observación en un registro de inspección?", "Un daño menor que se informa para programar su corrección", "Una opinión personal del inspector sobre la galería", "Un permiso de trabajo vencido", "La observación es un daño menor, no una emergencia."),
        ("abc", "En Explotación Minera: ¿qué significa señalizar una zona?", "Marcarla con avisos para que nadie entre", "Dibujarla en el plano de la faena", "Rellenarla con hormigón", "Señalizar es avisar con carteles o barreras para impedir el acceso."),
        ("=", "{F} ¿Cuántos puntos quedaron sin novedad?", "4", "Los puntos P1, P3, P6 y P8 están en orden.", " puntos"),
        ("abc", "{F} ¿Cómo se clasifica la placa doblada del punto P2?", "Observación", "Hallazgo crítico", "Sin novedad", "Es un daño menor en un elemento, no una señal de desprendimiento."),
        ("abc", "{F} ¿Qué puntos son hallazgos críticos?", "P5 y P7", "P2 y P4", "P5 y P8", "La grieta nueva con filtración y la roca caída son las señales de desprendimiento."),
        ("=", "{F} ¿Qué porcentaje de los puntos revisados quedó sin novedad?", "4*100//8", "Se multiplican por 100 los puntos sin novedad y se divide entre los revisados.", " %"),
        ("=", "{F} ¿Cuántos puntos son observaciones o hallazgos críticos en total?", "8-4", "Se restan los puntos sin novedad al total revisado.", " puntos"),
        ("abc", "{F} ¿A quién y cuándo se informa el hallazgo del punto P5?", "A la jefatura de inmediato, con señalización de la zona", "A la jefatura en la próxima reunión mensual", "A nadie, porque el hormigón proyectado ya cubre la grieta", "Un hallazgo crítico se informa de inmediato y se restringe la zona."),
        ("abc", "{F} Un joven en práctica ve el registro y propone pasar a mirar de cerca la grieta del punto P5. ¿Qué corresponde?", "No acercarse a la zona de riesgo y avisar a un adulto responsable", "Acercarse con una linterna para describirla mejor", "Acercarse solo unos minutos", "Acercarse a una grieta con señales de desprendimiento es peligroso."),
        ("abc", "{F} ¿Por qué el punto P7, aunque no haya personas cerca, es un hallazgo crítico?", "Porque la roca caída indica que puede seguir desprendiéndose", "Porque cualquier roca en el piso es crítica", "Porque no había nadie que la viera", "Que no haya personas cerca no elimina la señal de desprendimiento."),
        ("=", "{F} En la inspección siguiente se revisan 20 puntos y 15 quedan sin novedad. ¿Qué porcentaje queda sin novedad?", "15*100//20", "Se multiplican por 100 los puntos sin novedad y se divide entre los revisados.", " %"),
        ("abc", "Una persona te cuenta que, cerca de una galería de ejemplo, se escuchan golpes de roca que cae y hay trabajadores adentro. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a ver qué ocurre para informar con detalle", "Esperar a que cese el ruido antes de avisar", "Avisar de inmediato; entrar sin formación pone en riesgo a más personas."),
    ],
    ctx=("abc", "Un inspector de ejemplo anota en su registro: «grieta nueva con filtración en el techo, sin novedad por ahora». Su colega nota la contradicción. ¿Qué corresponde?", "Corregir la clasificación a hallazgo crítico, informar de inmediato y restringir la zona", "Dejarlo así, porque no se ha caído nada", "Borrar la anotación para no alarmar", "Una grieta con filtración es una señal de desprendimiento, no un punto sin novedad."),
    sc=[
        ("En Explotación Minera: ¿qué se hace ante un hallazgo crítico?", "Se informa de inmediato y se restringe la zona", "Lo crítico no espera a la próxima revisión."),
        ("¿Cómo se calcula el porcentaje de puntos sin novedad?", "Puntos sin novedad por 100, divididos entre los revisados", "El porcentaje compara los puntos en orden con el total."),
        ("¿Quién corrige una observación?", "Personal autorizado, programado por la jefatura", "Quien no tiene autorización no repara fortificación."),
    ],
    op=("Registro ficticio de la faena «Mina Demo Cerro Claro»: 10 puntos revisados en una galería. Resultados: 6 sin novedad, 3 observaciones (una placa de perno doblada y dos roturas pequeñas de malla) y 1 hallazgo crítico (roca caída al piso). Escribe (a) el porcentaje de puntos sin novedad, (b) qué se hace con las observaciones, (c) qué se hace con el hallazgo crítico, (d) qué debe hacer una persona sin autorización que ve la roca caída.",
        "(a) 6 × 100 ÷ 10 = 60 %. (b) Se informan a la jefatura para programar la corrección por personal autorizado. (c) Se informa de inmediato, se señaliza y se restringe la zona según el plan de la empresa. (d) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula el porcentaje", "describe la respuesta a una observación", "describe la respuesta a un hallazgo crítico", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["tratar como observación una roca caída", "creer que la persona sin autorización puede reparar", "dividir entre un número distinto de 10"],
        "Pregunta: «¿qué diferencia hay entre informar de inmediato y programar una corrección?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un registro de 5 puntos con una observación y un hallazgo crítico, y escribe qué harías con cada uno.",
    extend="Explica con un ejemplo por qué es importante registrar también los puntos sin novedad.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (planilla de ejemplo, inventada). Proyecto de fortificación de un tramo de 60 m de galería de la faena ficticia «Mina Demo Río Hondo». Regla del proyecto de ejemplo: una fila de pernos cada 2 m de largo, con 5 pernos por fila. Malla: cubre el techo y las paredes, con 18 m² por cada metro de largo de galería; cada rollo de malla cubre 90 m². "
     "Hormigón proyectado: se aplica en 120 m² del tramo, con un espesor de 5 cm; volumen en m³ = área en m² × espesor en cm ÷ 100. Precio de ejemplo de un perno: $15.000. Existencias de pernos en bodega: 120.")
build(
    O2, 4, F,
    use="Aprenderé a calcular en una planilla las cantidades y los costos de un proyecto de fortificación: filas y pernos, rollos de malla, volumen de hormigón y diferencias con las existencias.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé calcular un área y un volumen sencillos.", "Sé leer una regla de un proyecto."],
    explain=[
        "Una planilla de cantidades traduce las reglas del proyecto en números. Si hay una fila de pernos cada 2 m en un tramo de 60 m, el número de filas es el largo dividido entre la separación; los pernos totales son las filas por los pernos de cada fila. Una existencia es lo que hay guardado en bodega, y el faltante es la diferencia entre lo necesario y lo que hay.",
        "La malla se calcula con su cobertura: si cada metro de galería necesita 18 m² y el tramo mide 60 m, el área total es 18 por 60, y los rollos se obtienen dividiendo el área entre lo que cubre cada rollo. El volumen de hormigón es el área por el espesor en centímetros dividido entre 100, lo que da metros cúbicos. El costo es la cantidad por el precio unitario.",
        f"Estos cálculos son de planilla: los números del proyecto real los fija el proyecto y la norma vigente, y nadie los cambia por su cuenta. {EMER} {AVISO}",
    ],
    vocab=[("planilla de cantidades", "tabla que traduce las reglas del proyecto en cantidades y costos"), ("existencia", "cantidad de un material guardada en bodega"), ("faltante", "cantidad necesaria que supera lo que hay en bodega"), ("cobertura", "área que cubre una unidad de material"), ("espesor", "grosor de una capa"), ("volumen", "espacio que ocupa un material, en metros cúbicos")],
    worked=[
        ("Filas de elementos", "En un talud de ejemplo se coloca una fila de anclajes cada 3 m a lo largo de 45 m. ¿Cuántas filas hay?", ["Se divide el largo entre la separación.", "45 dividido entre 3 son 15 filas."], "15 filas"),
        ("Volumen de una capa", "Una capa de hormigón proyectado de ejemplo cubre 80 m² con 10 cm de espesor. ¿Qué volumen es?", ["Volumen = área × espesor en cm ÷ 100.", "80 por 10 son 800, y 800 dividido entre 100 son 8 m³."], "8 m³"),
    ],
    mistakes=[("Multiplicar los metros de largo por los pernos por fila sin pasar por las filas.", "Los pernos son las filas por los pernos de cada fila; las filas salen del largo dividido entre la separación.", "Calcula primero las filas y después los pernos."),
              ("Olvidar convertir el espesor de centímetros a metros al calcular el volumen.", "La fórmula del proyecto ya incluye dividir entre 100.", "Aplica la fórmula completa: área por espesor en cm, dividido entre 100.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una existencia en una planilla de bodega?", "La cantidad de un material que está guardada en la bodega", "La cantidad de un material que falta comprar", "El precio de un material", "La existencia es lo que hay; lo que falta es el faltante."),
        ("abc", "En Explotación Minera: ¿qué es un faltante?", "La cantidad necesaria que supera lo que hay en bodega", "La cantidad de material sobrante", "El precio total de una compra", "El faltante es la diferencia entre lo necesario y lo disponible."),
        ("abc", "En Explotación Minera: ¿qué es el espesor de una capa de hormigón proyectado?", "El grosor de la capa", "El largo del tramo cubierto", "El peso de un metro cúbico de hormigón", "El espesor es el grosor, no el largo ni el peso."),
        ("=", "{F} ¿Cuántas filas de pernos tiene el tramo de la ficha?", "60//2", "Se divide el largo del tramo entre la separación de las filas.", " filas"),
        ("=", "{F} ¿Cuántos pernos necesita el tramo en total?", "(60//2)*5", "Se multiplican las filas por los pernos de cada fila.", " pernos"),
        ("=", "{F} ¿Cuántos metros cuadrados de malla necesita el tramo completo?", "18*60", "Se multiplica el área por metro de largo por los metros del tramo.", " m²"),
        ("=", "{F} ¿Cuántos rollos de malla se necesitan?", "18*60//90", "Se divide el área total entre lo que cubre cada rollo.", " rollos"),
        ("=", "{F} ¿Cuántos metros cúbicos de hormigón proyectado necesita el tramo?", "120*5//100", "Se multiplica el área por el espesor en cm y se divide entre 100.", " m³"),
        ("=", "{F} ¿Cuánto cuestan en total los pernos que necesita el tramo?", "(60//2)*5*15000", "Se multiplican los pernos necesarios por el precio de uno.", " pesos"),
        ("=", "{F} ¿Cuántos pernos faltan comprar, si hay 120 en bodega?", "(60//2)*5-120", "Se resta la existencia a los pernos que se necesitan.", " pernos"),
        ("abc", "{F} Un bodeguero dice: «tengo 120 pernos, así que alcanzan para el tramo». ¿Qué corresponde?", "Revisar que se necesitan 150, por lo que hay un faltante que se debe informar y pedir", "Instalar los 120 y dejar el resto sin fortificar", "Usar pernos de otro tamaño para completar", "El proyecto fija las cantidades; el faltante se informa y se pide, no se cambia."),
        ("=", "{F} Si el espesor del hormigón proyectado del proyecto subiera a 10 cm en los mismos 120 m², ¿cuántos m³ serían?", "120*10//100", "Se aplica la misma fórmula con el nuevo espesor.", " m³"),
        ("abc", "Un joven en práctica quiere usar la planilla para decidir por su cuenta cuántos pernos colocar en una galería real. ¿Qué es correcto?", "No puede: las cantidades las fija el proyecto, y la ejecución es de personal autorizado", "Puede si el cálculo le da exacto", "Puede si anota el resultado en un cuaderno", "La planilla de este cuaderno es un ejercicio de papel, no un proyecto real."),
    ],
    ctx=("abc", "Un asistente de ejemplo calcula para un tramo de 30 m con filas cada 2 m y 4 pernos por fila, y escribe «30 × 4 = 120 pernos». ¿Qué respondes?", "Que primero se calculan las filas, 30 dividido entre 2 son 15, y luego los pernos, 15 por 4 son 60", "Que está correcto, porque 30 por 4 son 120", "Que faltan sumar los pernos de las paredes", "Los pernos son las filas por los pernos de cada fila; el largo no se multiplica directamente."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el número de filas de pernos?", "Largo del tramo dividido entre la separación de las filas", "Cada fila ocupa una separación del tramo."),
        ("¿Cómo se calcula el volumen de hormigón proyectado?", "Área por espesor en centímetros, dividido entre 100", "El resultado queda en metros cúbicos."),
        ("En Explotación Minera: ¿qué es un faltante?", "Lo necesario que supera la existencia", "Se informa y se pide la diferencia."),
    ],
    op=("Planilla ficticia de la faena «Mina Demo Cerro Claro»: tramo de 40 m, una fila de pernos cada 2 m con 6 pernos por fila, malla de 18 m² por metro de largo, rollos de 90 m² y precio de ejemplo de $12.000 por perno. En bodega hay 100 pernos. Escribe (a) las filas y los pernos totales, (b) los rollos de malla, (c) si falta algún perno y cuántos, (d) el costo de ejemplo de los pernos necesarios.",
        "(a) 40 ÷ 2 = 20 filas y 20 × 6 = 120 pernos. (b) 18 × 40 = 720 m², y 720 ÷ 90 = 8 rollos. (c) Faltan 20 pernos, porque 120 − 100 = 20. (d) 120 × 12.000 = $1.440.000.",
        ["calcula filas y pernos", "calcula los rollos de malla", "calcula el faltante", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar el largo por los pernos por fila", "olvidar dividir el área entre lo que cubre un rollo", "no restar la existencia"],
        "Pregunta: «¿qué calculaste antes de los pernos totales?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un tramo de 50 m con una fila cada 5 m y 4 pernos por fila, y calcula los pernos y su costo.",
    extend="Explica con un ejemplo por qué un faltante se informa y no se cubre con material distinto.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 10 (documentos de ejemplo, inventados). Dos ofertas para suministrar 40 rollos de malla para la faena ficticia «Mina Demo Lomas Bajas». Oferta 1: $190.000 por rollo, con certificado de calidad exigido por el proyecto, entrega en 10 días. Oferta 2: $160.000 por rollo, sin certificado de calidad, entrega en 3 días. "
     "Regla de la empresa de ejemplo: no se compra material de fortificación que no tenga el certificado exigido por el proyecto. "
     "Además, dos registros de inspección de ejemplo con cinco datos obligatorios (fecha, ubicación, descripción del hallazgo, nombre del inspector, firma). Registro R-1 tiene los cinco datos. Registro R-2 tiene fecha, ubicación y descripción, pero no nombre ni firma.")
build(
    O2, 5, F,
    use="Aprenderé a comparar alternativas de compra y de registro en un proyecto de fortificación y a verificar su calidad con las exigencias del proyecto y de la empresa.",
    prior=["Sé calcular costos multiplicando.", "Sé qué es un registro de inspección.", "Sé qué es una regla de la empresa."],
    explain=[
        "Comparar alternativas es mirar varios criterios, no solo el precio. Un certificado de calidad es el documento que demuestra que un material cumple lo que exige el proyecto; sin él, el material no puede usarse en fortificación, aunque sea más barato o llegue antes. Un criterio obligatorio decide primero: la alternativa que no lo cumple queda descartada, y recién entre las que sí lo cumplen se compara el precio y el plazo.",
        "Verificar la calidad de un registro es comprobar que tenga todos los datos obligatorios: sin fecha, no se sabe cuándo se hizo; sin nombre ni firma, no se sabe quién responde. Un registro incompleto se devuelve a quien lo hizo para que lo complete; no se completa por otra persona ni se inventan los datos que faltan.",
        f"Los costos se calculan multiplicando el precio por la cantidad, y la diferencia entre dos ofertas se obtiene restando los totales. {EMER} {AVISO}",
    ],
    vocab=[("certificado de calidad", "documento que demuestra que un material cumple lo que exige el proyecto"), ("criterio obligatorio", "condición que una alternativa debe cumplir para poder ser elegida"), ("oferta", "propuesta de un proveedor con precio y plazo"), ("proveedor", "empresa o persona que vende un material"), ("registro incompleto", "registro al que le faltan datos obligatorios")],
    worked=[
        ("Costo de una compra", "Una oferta de ejemplo de pernos cuesta $8.000 por unidad y se necesitan 90. ¿Cuánto cuesta en total?", ["Se multiplica el precio por la cantidad.", "8.000 por 90 son 720.000."], "$720.000"),
        ("Descartar por criterio obligatorio", "De dos ofertas de ejemplo de cemento, una es más barata y no trae certificado, y la otra trae certificado y cuesta más. El proyecto exige certificado. ¿Cuál se elige?", ["El certificado es un criterio obligatorio.", "La oferta sin certificado queda descartada."], "La que trae certificado"),
    ],
    mistakes=[("Elegir la oferta más barata aunque no cumpla una exigencia del proyecto.", "Un criterio obligatorio decide antes que el precio.", "Primero descarta las ofertas que no cumplen y luego compara el precio."),
              ("Completar tú los datos que faltan en un registro ajeno.", "Un registro lo completa y firma quien lo hizo; los datos inventados lo vuelven poco confiable.", "Devuelve el registro a su autor para que lo complete.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué demuestra un certificado de calidad de un material?", "Que el material cumple lo que exige el proyecto", "Que el material es el más barato", "Que el proveedor es el más cercano", "El certificado respalda la calidad, no el precio ni la cercanía."),
        ("abc", "En Explotación Minera: ¿qué es un criterio obligatorio al comparar ofertas?", "Una condición que la oferta debe cumplir para poder ser elegida", "El criterio que prefiere la mayoría del equipo", "El precio más bajo de todas las ofertas", "Un criterio obligatorio descarta las ofertas que no lo cumplen."),
        ("abc", "En Explotación Minera: ¿qué es un registro incompleto?", "Un registro al que le faltan datos obligatorios", "Un registro que tiene demasiados datos", "Un registro escrito con otra letra", "Lo incompleto es lo que no tiene todos los datos obligatorios."),
        ("=", "{F} ¿Cuánto cuestan en total los 40 rollos de la oferta 1?", "190000*40", "Se multiplica el precio de un rollo por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan en total los 40 rollos de la oferta 2?", "160000*40", "Se multiplica el precio de un rollo por la cantidad.", " pesos"),
        ("abc", "{F} ¿Qué oferta cumple el criterio obligatorio de la empresa?", "La oferta 1, porque trae el certificado de calidad", "La oferta 2, porque entrega más rápido", "Ninguna, porque las dos tienen precio", "La regla de la empresa exige el certificado, que solo trae la oferta 1."),
        ("=", "{F} ¿Cuántos pesos más cuesta la oferta 1 que la oferta 2 por los 40 rollos?", "190000*40-160000*40", "Se restan los totales de las dos ofertas.", " pesos"),
        ("=", "{F} ¿Cuántos días más tarda la oferta 1 que la oferta 2 en entregar?", "10-3", "Se restan los días de entrega de las dos ofertas.", " días"),
        ("abc", "{F} ¿Cuál oferta se debe elegir y por qué?", "La oferta 1, porque la oferta 2 no cumple el criterio obligatorio aunque sea más barata", "La oferta 2, porque ahorra dinero y tiempo", "Cualquiera, porque el material es el mismo", "El criterio obligatorio decide antes que el precio y el plazo."),
        ("abc", "{F} Un jefe propone comprar la oferta 2 «y pedir el certificado después, cuando llegue». ¿Qué corresponde?", "Rechazar la propuesta, porque la empresa no compra material de fortificación sin certificado", "Aceptar si el proveedor promete enviarlo", "Aceptar si el material se ve en buen estado", "La regla exige el certificado al comprar, no después."),
        ("abc", "{F} ¿Por qué el registro R-2 no está completo?", "Porque no tiene el nombre del inspector ni la firma", "Porque no tiene fecha", "Porque no describe el hallazgo", "R-2 tiene fecha, ubicación y descripción, pero le faltan el nombre y la firma."),
        ("=", "{F} ¿Cuántos de los cinco datos obligatorios tiene el registro R-2?", "5-2", "Se restan los dos datos que le faltan a los cinco obligatorios.", " datos"),
        ("abc", "{F} ¿Qué corresponde hacer con el registro R-2?", "Devolverlo a quien lo hizo para que lo complete y lo firme", "Completarlo con el nombre del jefe de turno", "Usarlo igual porque describe el hallazgo", "El registro lo completa y firma quien lo hizo."),
    ],
    ctx=("abc", "Una bodeguera de ejemplo recibe 30 rollos de malla de una oferta sin certificado de calidad y dice: «están en perfecto estado, los guardo y se usan». ¿Qué corresponde?", "Informar a la jefatura que no hay certificado y no usar el material hasta que se regularice", "Usarlos igual porque se ven bien", "Cambiar la etiqueta para que parezcan certificados", "Sin certificado exigido por el proyecto, el material no se usa en fortificación."),
    sc=[
        ("En Explotación Minera: ¿qué se compara primero entre ofertas?", "El cumplimiento de los criterios obligatorios", "Lo que no cumple queda descartado antes de comparar el precio."),
        ("En Explotación Minera: ¿cómo se calcula el costo total de comprar pernos o mallas?", "Precio unitario por cantidad", "La multiplicación del precio por la cantidad da el total."),
        ("¿Qué se hace con un registro al que le falta la firma?", "Se devuelve a su autor para que lo complete", "No lo completa otra persona ni se inventan datos."),
    ],
    op=("Dos ofertas ficticias para la faena «Mina Demo Cerro Claro»: 50 pernos. Oferta A: $9.000 por perno, certificado de calidad incluido, entrega en 8 días. Oferta B: $7.000 por perno, sin certificado, entrega en 2 días. La empresa exige certificado. Escribe (a) el costo total de cada oferta, (b) cuál eliges y por qué, (c) cuántos pesos pagas de más respecto de la otra y qué compras con ello, (d) qué harías si el proveedor B promete mandar el certificado después.",
        "(a) A: 9.000 × 50 = $450.000; B: 7.000 × 50 = $350.000. (b) La A, porque cumple el criterio obligatorio del certificado. (c) Pagas $100.000 más y compras la garantía de calidad que exige la empresa. (d) No aceptar: la regla exige el certificado al comprar.",
        ["calcula los costos", "aplica el criterio obligatorio", "interpreta la diferencia de costo", "mantiene la regla de la empresa"],
        ["hoja con las cuatro respuestas"],
        ["elegir la más barata", "no restar bien los totales", "aceptar el certificado después"],
        "Pregunta: «¿qué oferta queda descartada antes de comparar precios?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos ofertas de malla con certificado distinto y decide cuál se elige explicando el criterio.",
    extend="Explica con un ejemplo por qué una oferta más barata puede salir más cara si el material no sirve.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 11 (caso de ejemplo, inventado). En la faena subterránea ficticia «Mina Demo Cañada Larga», una frente de avance (el extremo donde la galería avanza) queda a 300 m de la ventilación principal y recibe aire por un ducto con un ventilador secundario. Una bomba saca el agua que se junta en un sumidero. "
     "Peligros anotados: aire contaminado en la frente si el ventilador se detiene (probabilidad 3 y gravedad 5), agua acumulada en el piso (probabilidad 4 y gravedad 3), electricidad cerca del agua (probabilidad 2 y gravedad 4) y ruido del ventilador (probabilidad 5 y gravedad 2). "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. Personal de ejemplo en un turno: 4 personas en ventilación, 7 en mantención eléctrica y mecánica y 3 en prevención de riesgos.")
build(
    O3, 1, F,
    use="Aprenderé qué son la ventilación secundaria y el drenaje de una mina, qué peligros tienen y por qué solo personal autorizado instala y mantiene estos equipos.",
    prior=["Sé qué es un peligro y qué es un riesgo.", "Sé calcular un puntaje multiplicando dos números.", "Sé que las tareas de riesgo las hacen personas autorizadas."],
    explain=[
        "En una mina subterránea el aire se renueva con ventilación. La ventilación principal mueve el aire por las galerías grandes; la ventilación secundaria lleva aire a lugares donde no llega por sí solo, como una frente de avance, usando un ventilador y un ducto, que es el tubo que conduce el aire. Sin aire renovado se acumulan polvo, calor y gases y puede faltar oxígeno. El drenaje es el conjunto de canales, sumideros, bombas y tuberías que recogen y sacan el agua de la mina, tanto subterránea como a cielo abierto.",
        "Los peligros de estos sistemas son el aire contaminado si falla el ventilador, el agua acumulada en el piso, el contacto entre electricidad y agua y el ruido. En la matriz de ejemplo, el puntaje de riesgo es probabilidad por gravedad y se atiende primero el mayor. La autoridad minera fiscaliza que se cumpla la norma vigente sobre ventilación y seguridad.",
        f"Instalar, conectar y mantener ventiladores y bombas exige formación, personal eléctrico y mecánico autorizado y permiso de trabajo; este cuaderno no enseña a hacerlo. {EMER} {AVISO}",
    ],
    vocab=[("ventilación secundaria", "sistema de ventilador y ducto que lleva aire a lugares sin circulación propia, como una frente de avance"), ("ducto", "tubo que conduce el aire"), ("frente de avance", "extremo de una galería donde se sigue avanzando"), ("drenaje", "conjunto de canales, sumideros, bombas y tuberías que sacan el agua de la mina"), ("sumidero", "pozo donde se junta el agua para ser bombeada"), ("bomba", "equipo que mueve el agua por una tubería")],
    worked=[
        ("Puntaje de riesgo", "En la matriz de ejemplo de una sala de bombas, el piso resbaloso tiene probabilidad 3 y gravedad 3. ¿Qué puntaje de riesgo resulta?", ["Se multiplica la probabilidad por la gravedad.", "3 por 3 son 9."], "9 puntos"),
        ("Peligro y riesgo", "Un ducto de ventilación de ejemplo tiene una rotura que deja escapar aire. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el ducto roto, porque llega menos aire a la frente.", "El riesgo es que se acumulen gases o polvo donde trabaja la gente."], "Peligro: el ducto roto; riesgo: que se acumulen gases o polvo"),
    ],
    mistakes=[("Creer que quien sabe para qué sirve un ventilador ya puede conectarlo o moverlo.", "Conectar y mover equipos exige personal autorizado, formación y permiso de trabajo.", "Aprende el concepto aquí y deja la tarea a personal autorizado."),
              ("Pensar que el agua acumulada es solo una molestia y no un peligro.", "El agua puede debilitar el piso, ocultar desniveles y combinarse con la electricidad.", "Reconoce el agua como peligro y avisa para que se atienda.")],
    T=[
        ("abc", "En Explotación Minera: ¿para qué sirve la ventilación secundaria?", "Para llevar aire a lugares donde no llega por sí solo, como una frente de avance", "Para llevar el mineral desde la frente hasta la planta", "Para sacar el agua que se junta en el piso", "La ventilación secundaria renueva el aire; el agua se saca con el drenaje."),
        ("abc", "En Explotación Minera: ¿qué es el drenaje de una mina?", "El conjunto de canales, sumideros, bombas y tuberías que sacan el agua", "El conjunto de ductos que llevan aire a la frente", "El sistema que lleva el mineral a la planta", "El drenaje recoge y saca el agua; el aire va por ductos."),
        ("abc", "En Explotación Minera: ¿qué es un ducto de ventilación?", "Un tubo que conduce el aire hasta un lugar de trabajo", "Un canal que recoge el agua de la galería", "Un cable que da energía al ventilador", "El ducto conduce aire; el agua va por canales y tuberías."),
        ("=", "{F} ¿Cuántas personas hay en total en el turno de la ficha?", "4+7+3", "Se suman las personas de ventilación, mantención y prevención.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «aire contaminado si el ventilador se detiene»?", "Que las personas de la frente respiren aire con gases o con poco oxígeno", "Que el ventilador necesite mantención", "Que el ducto sea muy largo", "El riesgo es el daño posible a las personas, no una característica del equipo."),
        ("abc", "{F} ¿Por qué se necesita un ventilador secundario en la frente de la ficha?", "Porque está a 300 m de la ventilación principal y el aire no llega por sí solo", "Porque la frente produce más mineral que las otras zonas", "Porque el ventilador reemplaza al drenaje", "La ventilación secundaria alimenta lugares alejados de la principal."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el aire contaminado si el ventilador se detiene?", "3*5", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la electricidad cerca del agua?", "2*4", "Se multiplican la probabilidad y la gravedad de ese peligro.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál de los cuatro peligros debe atenderse primero?", "El aire contaminado, porque tiene el mayor puntaje (15)", "El ruido, porque tiene la mayor probabilidad (5)", "El agua acumulada, porque tiene el segundo mayor puntaje", "Se atiende primero el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Un trabajador sin autorización eléctrica ve que el cable del ventilador se desconectó y quiere volver a conectarlo. ¿Qué corresponde?", "No hacerlo y avisar a la jefatura para que lo haga personal eléctrico autorizado", "Hacerlo con guantes de goma", "Hacerlo rápido para que no se acumule aire malo", "Los guantes no reemplazan la autorización; la tarea es de personal autorizado."),
        ("abc", "{F} ¿Por qué se considera peligrosa la combinación de agua y electricidad?", "Porque el agua conduce la corriente y un equipo energizado puede causar una descarga", "Porque el agua enfría los cables y los deja inservibles", "Porque la electricidad evapora el agua del sumidero", "El agua facilita el paso de la corriente a las personas."),
        ("=", "{F} Para un simulacro, todo el personal del turno se reparte en grupos de 7 personas. ¿Cuántos grupos se forman?", "(4+7+3)//7", "Se suma el personal de las tres áreas y se divide entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, ves que una frente está sin ventilador y te cuentan que dos personas que estaban ahí no responden. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar corriendo a sacarlas", "Encender tú el ventilador y esperar", "Entrar a una zona sin aire seguro pone en riesgo a otra persona."),
    ],
    ctx=("abc", "Un contratista de ejemplo te dice: «Ayúdame a mover este ventilador y a conectarlo, es fácil, solo hay que enchufarlo». ¿Qué respondes?", "Que no, porque mover y conectar equipos exige formación, personal autorizado y permiso, y que consultarás a un adulto responsable", "Que sí, si lo haces con otra persona", "Que sí, si el ventilador es pequeño", "Instalar o conectar equipos no es una tarea para quien no está autorizado."),
    sc=[
        ("En Explotación Minera: ¿qué es una frente de avance?", "El extremo de una galería donde se sigue avanzando", "En ese lugar el aire no llega por sí solo."),
        ("En Explotación Minera: ¿qué es un sumidero?", "Un pozo donde se junta el agua para ser bombeada", "El sumidero concentra el agua antes de sacarla."),
        ("¿Cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("La faena ficticia «Mina Demo Cerro Claro» tiene una galería nueva de 150 m con una frente donde trabajan 5 personas y un sumidero con una bomba cerca de la entrada. Escribe (a) un peligro y su riesgo asociado en la ventilación, (b) un peligro y su riesgo asociado en el drenaje, (c) quién debe conectar y mantener el ventilador y la bomba, (d) qué haces si ves que el ventilador se detuvo y alguien está en la frente.",
        "(a) Peligro: que el ventilador se detenga; riesgo: que se acumulen gases o falte oxígeno en la frente. (b) Peligro: agua acumulada en el piso cerca de equipos eléctricos; riesgo: una descarga eléctrica o una caída. (c) Personal eléctrico y mecánico autorizado, con permiso de trabajo. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["identifica un peligro y un riesgo de ventilación", "identifica un peligro y un riesgo de drenaje", "asigna la tarea a personal autorizado", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que cualquier trabajador puede conectar equipos", "intentar entrar a la frente"],
        "Pregunta: «¿qué le podría pasar a una persona si falla el ventilador?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una matriz de tres peligros de un sistema de drenaje con probabilidad y gravedad, y calcula los puntajes.",
    extend="Explica con un ejemplo por qué una frente alejada necesita ventilación secundaria.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 12 (documentos de ejemplo, inventados). Diagrama de ventilación de la «Mina Demo Piedra Azul»: el ventilador secundario V1 impulsa aire por un ducto de 150 m, armado en tramos de 30 m cada uno, hasta la frente F1. Caudal nominal de V1: 12 m³/s (valor de ejemplo); el caudal es el volumen de aire que pasa por segundo. "
     "Diagrama de drenaje: el sumidero S1 envía el agua con la bomba B1 por una tubería de 200 m, armada en tramos de 8 m cada uno, hasta una cuneta (canal) en superficie. "
     "Documentos: diagrama del sistema, instrucción técnica del fabricante (de ejemplo), pauta de verificación, registro de mantención y permiso de trabajo. Roles: el responsable de ventilación vigila el sistema; el electricista autorizado hace las tareas eléctricas; el mecánico autorizado, las mecánicas; el supervisor organiza; el prevencionista vela por la seguridad.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario de los diagramas de ventilación y drenaje, los documentos que acompañan a estos equipos y el rol de cada persona.",
    prior=["Sé qué son la ventilación secundaria y el drenaje.", "Sé leer un diagrama sencillo.", "Sé qué es un permiso de trabajo."],
    explain=[
        "Un diagrama es un dibujo esquemático que muestra cómo se conectan las partes de un sistema, sin importar la escala. El diagrama de ventilación muestra el ventilador, el ducto y la frente a la que llega el aire; el de drenaje muestra el sumidero, la bomba, la tubería y el canal por donde sale el agua. El caudal es el volumen que pasa por segundo, por ejemplo metros cúbicos de aire por segundo o litros de agua por segundo.",
        "Los documentos acompañan al equipo durante su vida: la instrucción técnica del fabricante dice cómo debe usarse y mantenerse y nadie la reemplaza por su costumbre; la pauta de verificación es una lista que se completa al revisar el sistema; el registro de mantención deja constancia de lo hecho, y el permiso de trabajo autoriza una tarea de riesgo a personal definido.",
        f"Cada rol tiene su límite: el responsable de ventilación vigila, los especialistas autorizados ejecutan y el supervisor organiza. Nadie reemplaza a otro en una tarea de riesgo. {EMER} {AVISO}",
    ],
    vocab=[("diagrama", "dibujo esquemático que muestra cómo se conectan las partes de un sistema"), ("caudal", "volumen de aire o de agua que pasa por segundo"), ("cuneta", "canal que lleva el agua"), ("instrucción técnica del fabricante", "documento que dice cómo usar y mantener un equipo"), ("pauta de verificación", "lista que se completa al revisar un sistema"), ("registro de mantención", "documento que deja constancia de lo hecho en un equipo")],
    worked=[
        ("Contar tramos", "En una tubería de ejemplo de 120 m armada en tramos de 6 m, ¿cuántos tramos hay?", ["Se divide el largo total entre el largo de cada tramo.", "120 dividido entre 6 son 20 tramos."], "20 tramos"),
        ("Leer un documento", "Una bomba de ejemplo tiene una instrucción técnica del fabricante que fija una mantención periódica a cargo de personal autorizado. Un supervisor dice que «esta vez se puede saltar». ¿Qué corresponde?", ["La instrucción del fabricante no se reemplaza por la costumbre ni por la prisa.", "Se cumple lo que dice la instrucción y se avisa al responsable."], "Se cumple la instrucción del fabricante"),
    ],
    mistakes=[("Creer que el diagrama muestra las distancias exactas, como un plano a escala.", "Un diagrama es esquemático: muestra conexiones, y las distancias están anotadas aparte.", "Lee las medidas anotadas en el diagrama y no las que parecen en el dibujo."),
              ("Creer que el supervisor puede hacer las tareas eléctricas si tiene prisa.", "Las tareas eléctricas son del electricista autorizado.", "Cada tarea la hace quien tiene la autorización correspondiente.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un diagrama de ventilación?", "Un dibujo esquemático que muestra cómo se conectan el ventilador, el ducto y la frente", "Un plano a escala de toda la mina", "Una lista de las personas que trabajan en la frente", "El diagrama muestra conexiones; no es un plano a escala."),
        ("abc", "En Explotación Minera: ¿qué es el caudal de un ventilador?", "El volumen de aire que mueve por segundo", "La potencia eléctrica que consume", "El largo del ducto que alimenta", "El caudal mide el volumen por unidad de tiempo."),
        ("abc", "En Explotación Minera: ¿qué es una pauta de verificación?", "Una lista que se completa al revisar un sistema", "El permiso para entrar a la frente", "El plano de la galería", "La pauta ordena la revisión ítem por ítem."),
        ("=", "{F} ¿Cuántos tramos de ducto tiene el sistema de ventilación?", "150//30", "Se divide el largo del ducto entre el largo de cada tramo.", " tramos"),
        ("=", "{F} ¿Cuántos tramos de tubería tiene el sistema de drenaje?", "200//8", "Se divide el largo de la tubería entre el largo de cada tramo.", " tramos"),
        ("abc", "{F} ¿Qué recoge el agua de la mina antes de que la bomba B1 la envíe a superficie?", "El sumidero S1", "La cuneta", "El ducto", "El sumidero junta el agua y la bomba la envía por la tubería."),
        ("abc", "{F} ¿Qué documento deja constancia de lo hecho en el ventilador después de una mantención?", "El registro de mantención", "La pauta de verificación", "El diagrama del sistema", "El registro documenta lo realizado; la pauta es la lista de revisión."),
        ("abc", "{F} ¿Quién hace las tareas eléctricas del sistema de ventilación?", "El electricista autorizado", "El supervisor", "El prevencionista", "Las tareas eléctricas son de personal eléctrico autorizado."),
        ("abc", "{F} ¿Qué documento autoriza una tarea de riesgo a personal definido?", "El permiso de trabajo", "El diagrama del sistema", "El registro de mantención", "El permiso nombra quién, qué y cuándo puede hacer la tarea."),
        ("abc", "{F} Un supervisor con prisa propone no seguir la instrucción técnica del fabricante porque «siempre se hizo así». ¿Qué corresponde?", "Seguir la instrucción del fabricante y avisar al responsable si hay dudas", "Hacerlo a su manera si el equipo ya es antiguo", "Hacerlo a su manera si trabaja con cuidado", "La instrucción del fabricante no se reemplaza por la costumbre."),
        ("abc", "{F} ¿Por qué el diagrama de ventilación anota el largo del ducto aunque sea esquemático?", "Porque el dibujo no está a escala y las medidas se leen en lo anotado", "Porque el ducto se mide con una regla en el dibujo", "Porque el largo del ducto cambia con el caudal", "Las medidas de un diagrama están anotadas porque el dibujo no está a escala."),
        ("=", "{F} Un segundo ventilador de ejemplo entregaría 8 m³/s. ¿Cuántos m³ de aire entregan juntos V1 y ese ventilador en un segundo?", "12+8", "Se suman los caudales de los dos ventiladores.", " m³"),
        ("abc", "Un compañero te cuenta que una bomba de ejemplo se sobrecalentó y sale humo del tablero eléctrico cerca del sumidero. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a desconectar el tablero", "Echar agua sobre el tablero", "Un tablero con humo puede causar una descarga o un incendio."),
    ],
    ctx=("abc", "En una charla de ejemplo, un participante dice que el diagrama de drenaje de su faena «ya se sabe de memoria» y que puede hacer la mantención de la bomba sin pauta ni permiso. ¿Qué respondes?", "Que no: la mantención se hace con la pauta, la instrucción del fabricante y un permiso, por personal autorizado", "Que sí, si la bomba es pequeña", "Que sí, porque la memoria es suficiente", "Una mantención exige documentos y personal autorizado, no memoria."),
    sc=[
        ("En Explotación Minera: ¿qué es el caudal?", "El volumen de aire o de agua que pasa por segundo", "Se mide en unidades como m³/s o L/s."),
        ("En Explotación Minera: ¿para qué sirve la instrucción técnica del fabricante?", "Para saber cómo usar y mantener un equipo", "Es la referencia que nadie reemplaza por la costumbre."),
        ("¿Qué muestra un diagrama de drenaje?", "Cómo se conectan el sumidero, la bomba, la tubería y el canal", "El diagrama muestra las conexiones del sistema."),
    ],
    op=("Diagrama ficticio de la faena «Mina Demo Cerro Claro»: el ventilador V2 envía aire por un ducto de 90 m, en tramos de 30 m, hasta una frente; el sumidero S2 envía el agua con la bomba B2 por una tubería de 160 m, en tramos de 8 m, hasta una cuneta. Escribe (a) cuántos tramos de ducto y de tubería hay, (b) qué documento usarías para registrar una mantención, (c) quién hace las tareas eléctricas, (d) qué haces si ves humo saliendo del tablero de la bomba.",
        "(a) 90 ÷ 30 = 3 tramos de ducto y 160 ÷ 8 = 20 tramos de tubería. (b) El registro de mantención. (c) El electricista autorizado. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula los tramos", "elige el documento correcto", "asigna la tarea eléctrica a quien corresponde", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["confundir la pauta con el registro", "pasar por alto la división de tramos", "intentar apagar el tablero"],
        "Pregunta: «¿qué documento anota lo hecho y cuál lista lo que hay que revisar?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Dibuja un diagrama sencillo de un sistema de drenaje con cuatro elementos y rotula cada uno.",
    extend="Explica con un ejemplo por qué las medidas de un diagrama esquemático están escritas aparte.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 13 (caso de ejemplo, inventado). Informe de turno de la Frente 4 Norte de la faena ficticia «Mina Demo Lomas Bajas». El ventilador V2 tiene un caudal de salida de 12 m³/s. El ducto, de 200 m, pierde por fugas el 25 % de ese caudal (valor medido en una revisión anterior, de ejemplo). El caudal requerido en la frente según la planilla es 10 m³/s. "
     "Registro del turno: a las 07:00 el ventilador está en marcha; a las 11:30 se anota «ruido anormal en el ventilador»; a las 11:45 se anota «ducto con una abertura visible a 60 m del ventilador». "
     "Pauta de decisión de ejemplo: si el caudal que llega a la frente es menor que el requerido, se informa de inmediato al responsable de ventilación y no ingresa personal nuevo a la frente hasta que él lo autorice.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel un caso de ventilación: calcular el caudal que llega a la frente, compararlo con el requerido, leer un registro de turno y decidir a quién se informa.",
    prior=["Sé qué es el caudal.", "Sé calcular un porcentaje de un número.", "Sé qué es una frente de avance."],
    explain=[
        "Un ducto de ventilación no entrega a la frente todo el aire que sale del ventilador, porque parte se pierde por fugas, es decir, por aberturas y uniones mal selladas. Si se pierde un 25 %, llega el 75 % del caudal. El caudal que llega es el caudal de salida multiplicado por 75 y dividido entre 100. El caudal requerido es el mínimo que la planilla exige para esa frente; si llega menos, la ventilación es insuficiente.",
        "Un registro de turno es un documento donde se anotan, con la hora, las cosas notables. Una abertura en el ducto o un ruido anormal en el ventilador son señales de falla, y se informan de inmediato al responsable de ventilación. El responsable decide qué hacer; el personal no autorizado no repara ni mueve el equipo.",
        f"Este análisis es de papel: ni tú ni este cuaderno pueden decidir sobre una ventilación real. {EMER} {AVISO}",
    ],
    vocab=[("fuga", "pérdida de aire por una abertura o una unión mal sellada"), ("caudal requerido", "mínimo de aire que la planilla exige para una frente"), ("ventilación insuficiente", "situación en que llega menos aire que el requerido"), ("registro de turno", "documento donde se anotan, con la hora, las cosas notables del turno"), ("señal de falla", "dato que indica que un equipo no funciona bien")],
    worked=[
        ("Caudal que llega", "Un ventilador de ejemplo entrega 20 m³/s y el ducto pierde el 10 %. ¿Cuánto llega a la frente?", ["Si se pierde el 10 %, llega el 90 %.", "20 por 90 dividido entre 100 son 18 m³/s."], "18 m³/s"),
        ("Comparar con lo requerido", "Una frente de ejemplo requiere 15 m³/s y llegan 18 m³/s. ¿La ventilación es suficiente?", ["Se compara el caudal que llega con el requerido.", "18 es mayor que 15."], "Sí, es suficiente"),
    ],
    mistakes=[("Creer que llega a la frente todo el caudal que entrega el ventilador.", "Parte se pierde por fugas en el ducto.", "Resta la pérdida antes de comparar con lo requerido."),
              ("Pensar que un ruido anormal del ventilador es solo una molestia.", "Es una señal de falla y se informa de inmediato.", "Anota el ruido con la hora y avisa al responsable.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es una fuga en un ducto de ventilación?", "Una pérdida de aire por una abertura o una unión mal sellada", "Una caída del ventilador", "Un aumento del caudal requerido", "La fuga hace que llegue menos aire del que salió."),
        ("abc", "En Explotación Minera: ¿qué significa que la ventilación de una frente sea insuficiente?", "Que llega menos aire que el requerido", "Que el ventilador es muy ruidoso", "Que el ducto es demasiado corto", "Insuficiente compara lo que llega con lo que se necesita."),
        ("abc", "En Explotación Minera: ¿qué es una señal de falla en un equipo?", "Un dato que indica que no funciona bien, como un ruido anormal", "Un cartel que prohíbe usarlo", "El nombre de quien lo instaló", "La señal de falla es un indicio que debe informarse."),
        ("=", "{F} ¿Cuántos metros cúbicos por segundo llegan a la frente con la pérdida del 25 %?", "12*75//100", "Llega el 75 % del caudal: se multiplica por 75 y se divide entre 100.", " m³/s"),
        ("=", "{F} ¿Cuántos m³/s se pierden por fugas en el ducto?", "12-12*75//100", "Se resta el caudal que llega al caudal de salida.", " m³/s"),
        ("abc", "{F} ¿A qué hora se anotó la primera señal de falla?", "A las 11:30", "A las 07:00", "A las 11:45", "La primera señal es el ruido anormal anotado a las 11:30."),
        ("=", "{F} ¿Cuántos m³/s faltan para llegar al caudal requerido?", "10-12*75//100", "Se resta el caudal que llega al requerido.", " m³/s"),
        ("abc", "{F} ¿Es suficiente la ventilación de la frente?", "No, porque llegan 9 m³/s y se requieren 10", "Sí, porque el ventilador entrega 12 m³/s", "Sí, porque 9 es cercano a 10", "Se compara el caudal que llega con el requerido, no el de salida."),
        ("abc", "{F} Según la pauta de decisión de ejemplo, ¿qué se hace?", "Informar de inmediato al responsable de ventilación y no ingresar personal nuevo hasta que él lo autorice", "Seguir trabajando y anotarlo al final del turno", "Aumentar el caudal requerido para que parezca suficiente", "La pauta ordena avisar de inmediato y restringir el ingreso."),
        ("abc", "{F} Un joven en práctica propone sellar la abertura del ducto con cinta para solucionarlo. ¿Qué corresponde?", "No hacerlo: avisar al responsable para que lo repare personal autorizado", "Hacerlo si usa una cinta resistente", "Hacerlo rápido para no perder aire", "La reparación de un sistema de ventilación es de personal autorizado."),
        ("abc", "{F} ¿Por qué se anotan la hora y la descripción de cada señal de falla en el registro?", "Porque permiten saber cuándo ocurrió y quién debe actuar", "Porque el registro es más largo si tiene más datos", "Porque la hora cambia el caudal requerido", "El registro con hora permite seguir lo ocurrido y asignar responsabilidades."),
        ("=", "{F} Si se reemplazara el ventilador por otro de 16 m³/s y la pérdida siguiera en 25 %, ¿cuántos m³/s llegarían a la frente?", "16*75//100", "Llegaría el 75 % del nuevo caudal de salida.", " m³/s"),
        ("abc", "Una persona te cuenta que de una frente de ejemplo sale un olor extraño y que hay trabajadores que no responden por radio. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Ir a la frente a ver qué pasa", "Esperar a que el olor pase", "Acercarse a una atmósfera dudosa sin formación es muy peligroso."),
    ],
    ctx=("abc", "Un supervisor de ejemplo lee el informe de la ficha y dice: «el ventilador entrega 12 y se requieren 10, así que estamos bien». ¿Qué respondes?", "Que por las fugas llegan solo 9 m³/s, menos de los 10 requeridos, y que se debe informar de inmediato al responsable", "Que tiene razón, porque 12 es mayor que 10", "Que se puede esperar al próximo turno", "El caudal que cuenta es el que llega a la frente, no el que sale del ventilador."),
    sc=[
        ("En Explotación Minera: ¿qué caudal se compara con el requerido?", "El que llega a la frente", "El caudal de salida no considera las fugas."),
        ("¿Cómo se calcula el caudal que llega si se pierde un 25 %?", "Se multiplica el caudal por 75 y se divide entre 100", "Llega el 75 % del caudal."),
        ("En Explotación Minera: ¿a quién se informa una señal de falla de la ventilación?", "Al responsable de ventilación, de inmediato", "Él decide qué hacer y quién interviene."),
    ],
    op=("Informe ficticio de turno de la faena «Mina Demo Cerro Claro»: el ventilador V3 entrega 20 m³/s, el ducto pierde el 20 % por fugas y la frente requiere 18 m³/s. A las 14:10 se anota un ruido anormal. Escribe (a) cuántos m³/s llegan a la frente, (b) si la ventilación es suficiente y por qué, (c) a quién informas y qué anotas en el registro, (d) qué haces si alguien te dice que entres a la frente a revisarla.",
        "(a) 20 × 80 ÷ 100 = 16 m³/s. (b) No, porque 16 es menos de 18. (c) Al responsable de ventilación, de inmediato; se anota la hora (14:10) y la descripción del ruido. (d) No entro, no me acerco a la zona de riesgo y aviso a un adulto responsable y a emergencias si hay peligro.",
        ["calcula el caudal que llega", "compara con el requerido", "identifica a quién informar y qué anotar", "aplica la conducta de seguridad"],
        ["hoja con las cuatro respuestas"],
        ["comparar el caudal de salida con el requerido", "no anotar la hora", "entrar a revisar la frente"],
        "Pregunta: «¿qué porcentaje del caudal llega si se pierde el 20 %?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un ventilador de 30 m³/s con una pérdida del 20 %, calcula lo que llega y compáralo con un requerimiento de 25 m³/s.",
    extend="Explica con un ejemplo por qué es importante anotar la hora de una señal de falla.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 14 (planilla de ejemplo, inventada). Frente de la faena ficticia «Mina Demo Río Hondo». Regla de ejemplo para el caudal de aire requerido: 3 m³ por minuto por cada persona y 60 m³ por minuto por cada equipo diésel. La frente tiene 8 personas y 2 equipos diésel. El ventilador entrega 180 m³ por minuto y el ducto pierde el 20 % por fugas. "
     "Criterio de ejemplo: la ventilación cumple si el caudal que llega es igual o mayor que el requerido. "
     "Drenaje: el sumidero tiene capacidad de 30.000 litros; entra agua a 5 litros por segundo y la bomba saca 25 litros por segundo. 1 m³ equivale a 1.000 litros.")
build(
    O3, 4, F,
    use="Aprenderé a calcular en una planilla el caudal de aire requerido según personas y equipos, a compararlo con el que llega y a estimar el tiempo de vaciado de un sumidero.",
    prior=["Sé qué es el caudal.", "Sé calcular el porcentaje de un número.", "Sé convertir litros en metros cúbicos."],
    explain=[
        "El caudal requerido de una frente se calcula sumando lo que necesita cada persona y cada equipo diésel, según la regla del proyecto: personas por su aire por persona, más equipos por su aire por equipo. El caudal que llega es el caudal del ventilador menos las fugas. La ventilación cumple si lo que llega es igual o mayor que lo requerido; si no, se informa al responsable de ventilación.",
        "En el drenaje, el caudal neto es lo que la bomba saca menos lo que entra. El tiempo para vaciar un sumidero se obtiene dividiendo el volumen entre el caudal neto; si el volumen está en litros, se divide entre litros por segundo y resulta en segundos. Para pasar segundos a minutos se divide entre 60, y 1 m³ son 1.000 litros.",
        f"Los valores de esta planilla son de ejemplo: los reales los fija el proyecto y la norma vigente. Nadie puede cambiarlos por su cuenta. {EMER} {AVISO}",
    ],
    vocab=[("caudal requerido", "mínimo de aire que la regla del proyecto exige para una frente"), ("equipo diésel", "máquina con motor diésel, que consume aire"), ("caudal neto", "caudal que saca la bomba menos el caudal que entra"), ("capacidad del sumidero", "volumen máximo de agua que cabe en el sumidero"), ("litro", "unidad de volumen; 1.000 litros son 1 m³")],
    worked=[
        ("Caudal requerido", "En una frente de ejemplo hay 6 personas y 1 equipo diésel, con la regla de 3 m³/min por persona y 50 m³/min por equipo. ¿Cuánto aire se requiere?", ["Personas: 6 por 3 son 18; equipo: 1 por 50 son 50.", "18 más 50 son 68 m³/min."], "68 m³/min"),
        ("Tiempo de vaciado", "Un sumidero de ejemplo tiene 12.000 litros, entra agua a 2 L/s y la bomba saca 12 L/s. ¿Cuántos segundos tarda en vaciarse?", ["El caudal neto es 12 menos 2, es decir, 10 L/s.", "12.000 dividido entre 10 son 1.200 s."], "1.200 segundos"),
    ],
    mistakes=[("Sumar personas y equipos sin multiplicar por lo que requiere cada uno.", "Cada persona y cada equipo necesitan su propio caudal.", "Multiplica cada cantidad por su regla y luego suma."),
              ("Dividir el volumen del sumidero entre el caudal de la bomba sin restar el agua que entra.", "Mientras la bomba saca agua, sigue entrando agua.", "Usa el caudal neto, que es la salida menos la entrada.")],
    T=[
        ("abc", "En Explotación Minera: ¿cómo se calcula el caudal de aire requerido de una frente según la regla de ejemplo?", "Se suma el aire de las personas y el de los equipos diésel", "Se usa solo el aire que necesitan las personas", "Se divide el caudal del ventilador entre dos", "El caudal requerido considera personas y equipos."),
        ("abc", "En Explotación Minera: ¿qué es el caudal neto de una bomba en un sumidero?", "Lo que saca la bomba menos lo que entra de agua", "La suma de lo que saca y lo que entra", "La capacidad total del sumidero", "El caudal neto es el que realmente reduce el nivel del agua."),
        ("abc", "En Explotación Minera: ¿qué relación hay entre litros y metros cúbicos?", "1 m³ equivale a 1.000 litros", "1 m³ equivale a 100 litros", "1 litro equivale a 1.000 m³", "Mil litros llenan un metro cúbico."),
        ("=", "{F} ¿Cuántos m³ por minuto requieren las 8 personas de la frente?", "8*3", "Se multiplican las personas por el aire que necesita cada una.", " m³/min"),
        ("=", "{F} ¿Cuántos m³ por minuto requieren los 2 equipos diésel?", "2*60", "Se multiplican los equipos por el aire que necesita cada uno.", " m³/min"),
        ("=", "{F} ¿Cuántos m³ por minuto de aire se requieren en total en la frente?", "8*3+2*60", "Se suman el aire de las personas y el de los equipos.", " m³/min"),
        ("=", "{F} ¿Cuántos m³ por minuto llegan a la frente después de las fugas del 20 %?", "180*80//100", "Llega el 80 % del caudal del ventilador.", " m³/min"),
        ("abc", "{F} ¿Cumple la ventilación de la frente?", "Sí, porque lo que llega es igual al requerido", "No, porque el ventilador entrega más de lo requerido", "No, porque hay fugas", "El criterio dice que cumple si lo que llega es igual o mayor que lo requerido."),
        ("abc", "{F} Se suma una persona más a la frente. ¿Cumple la ventilación?", "No, porque el requerido sube a 147 y llegan 144", "Sí, porque una persona consume poco aire", "Sí, porque el ventilador sigue entregando 180", "Con 9 personas se requieren 27 más 120, es decir, 147, y llegan 144."),
        ("abc", "{F} Un jefe de turno propone agregar a la persona de todos modos «porque falta muy poco». ¿Qué corresponde?", "No hacerlo y informar al responsable de ventilación, porque el criterio no se cumple", "Hacerlo si el turno es corto", "Hacerlo si la persona es experimentada", "El criterio es obligatorio; la decisión es del responsable."),
        ("=", "{F} ¿Cuántos litros por segundo es el caudal neto de la bomba?", "25-5", "Se resta el agua que entra a lo que saca la bomba.", " L/s"),
        ("=", "{F} Si el sumidero está lleno, ¿cuántos minutos tarda la bomba en vaciarlo?", "30000//(25-5)//60", "Se divide el volumen entre el caudal neto y se pasan los segundos a minutos.", " min"),
        ("abc", "Una persona te cuenta que un sumidero de ejemplo se desbordó y que el agua llegó hasta un tablero eléctrico. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a cortar la electricidad tú mismo", "Intentar achicar el agua con baldes", "Agua y electricidad juntas causan descargas; solo personal autorizado interviene."),
    ],
    ctx=("abc", "Un asistente de ejemplo dice que un sumidero de 36.000 litros se vacía en 1.440 segundos con una bomba de 25 L/s, sin considerar una entrada de 5 L/s. ¿Qué respondes?", "Que debe usar el caudal neto de 20 L/s y que se vacía en 1.800 segundos", "Que está correcto, porque 36.000 dividido entre 25 son 1.440", "Que se vacía en 900 segundos porque hay que dividir entre 40", "Mientras la bomba saca agua sigue entrando agua, por eso se usa el caudal neto."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el caudal neto de una bomba?", "Lo que saca la bomba menos lo que entra", "Lo que entra de agua reduce el efecto de la bomba."),
        ("¿Cuántos litros hay en 1 m³?", "1.000 litros", "Un metro cúbico equivale a mil litros."),
        ("En Explotación Minera: ¿cuándo cumple la ventilación de una frente?", "Cuando el caudal que llega es igual o mayor que el requerido", "El criterio es obligatorio y se compara con lo que llega."),
    ],
    op=("Planilla ficticia de la faena «Mina Demo Cerro Claro»: una frente tiene 10 personas y 1 equipo diésel, con la regla de 3 m³/min por persona y 60 m³/min por equipo. El ventilador entrega 120 m³/min y el ducto pierde el 20 % por fugas. Un sumidero de 18.000 litros recibe 4 L/s y la bomba saca 22 L/s. Escribe (a) el caudal requerido, (b) el caudal que llega y si cumple, (c) el tiempo para vaciar el sumidero lleno, (d) a quién informas si la ventilación no cumple.",
        "(a) 10 × 3 + 1 × 60 = 90 m³/min. (b) 120 × 80 ÷ 100 = 96 m³/min; cumple, porque 96 es mayor que 90. (c) Caudal neto 22 − 4 = 18 L/s; 18.000 ÷ 18 = 1.000 s, es decir, unos 16 minutos y 40 segundos. (d) Al responsable de ventilación, de inmediato.",
        ["calcula el caudal requerido", "calcula lo que llega y compara", "calcula el tiempo con el caudal neto", "identifica a quién informar"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las fugas", "no restar el agua que entra", "no multiplicar cada cantidad por su regla"],
        "Pregunta: «¿qué dato restaste en el drenaje y por qué?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una frente con 12 personas y 2 equipos, define una regla de aire y calcula el caudal requerido.",
    extend="Explica con un ejemplo por qué el caudal neto de una bomba es menor que su caudal de salida cuando entra agua.",
)

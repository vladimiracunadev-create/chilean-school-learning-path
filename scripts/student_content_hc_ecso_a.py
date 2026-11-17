"""Economía y sociedad (electivo HC, 3.º y 4.º medio): OAC-01 (la economía como ciencia social) y OAC-02 (toma de decisiones), clases 1 a 5 de cada uno. Casos, cifras y fuentes de ejemplo, ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel o cuaderno y, si quieres, una calculadora simple. No se necesita computador ni internet: cada caso, tabla y dato está escrito en el enunciado. "
             "Las familias, empresas, comunas y cifras son ficticias o «de ejemplo» y sirven para practicar el razonamiento económico, no para aprender datos reales. "
             "Este cuaderno no entrega asesoría financiera ni recomienda inversiones: presenta modelos y posturas con sus argumentos, y tu tarea es analizarlos y evaluarlos, no adivinar cuál es «la correcta». "
             "Cuando un ejercicio toque dinero de una familia, los montos están en pesos chilenos.")
build = make_build(MATERIALS)

O1 = "HI-ECSO-3y4-OAC-01"
O2 = "HI-ECSO-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso de ejemplo, ficticio). La familia Rojas dispone de $60.000 libres este mes. Tiene tres opciones: un taller de inglés para la hija, $40.000; el arreglo de la bicicleta de trabajo del padre, $35.000; "
     "una salida familiar, $30.000. Con ese dinero no alcanza para todo. La familia ordena sus preferencias así: primero el taller, segundo la bicicleta, tercero la salida.")
build(
    O1, 1, F,
    use="Aprenderé qué estudia la economía, por qué la escasez obliga a elegir y cómo identificar el costo de oportunidad y a los agentes que deciden: familias, sector privado y Estado.",
    prior=["Sé sumar y restar cantidades de dinero.", "Sé que elegir una cosa a veces significa dejar otra.", "Conozco la diferencia entre una familia, una empresa y un organismo del Estado."],
    explain=[
        "La economía es la ciencia social que estudia cómo las personas, las empresas y el Estado toman decisiones para enfrentar la escasez. La escasez significa que los recursos (dinero, tiempo, trabajo, materias primas) son limitados, mientras que las necesidades y los deseos de las personas son muchos y siempre pueden crecer. Por eso toda sociedad debe elegir.",
        "Quienes toman decisiones económicas se llaman agentes económicos. Los principales son las familias, que deciden cómo gastar o ahorrar su ingreso; el sector privado, es decir, las empresas, que deciden qué producir y a qué precio; y el Estado, que decide cómo usar los impuestos y qué servicios y reglas ofrece. Los tres comparten un problema: no pueden tenerlo todo.",
        "Elegir implica renunciar. El costo de oportunidad de una decisión es lo mejor a lo que se renuncia al tomarla. No es lo mismo que el precio pagado: si con el mismo dinero podías hacer dos cosas y eliges una, el costo de oportunidad es la otra, la que habrías elegido en segundo lugar. Reconocerlo permite decidir sabiendo qué se pierde.",
    ],
    vocab=[("economía", "ciencia social que estudia cómo se decide para enfrentar la escasez"), ("escasez", "recursos limitados frente a necesidades y deseos ilimitados"), ("agente económico", "quien toma decisiones económicas: familia, empresa o Estado"), ("costo de oportunidad", "lo mejor a lo que se renuncia al elegir"), ("recurso", "medio limitado que sirve para producir o satisfacer necesidades"), ("sector privado", "las empresas y negocios que no pertenecen al Estado")],
    worked=[
        ("Hallar el costo de oportunidad", "Tomás tiene $15.000 y puede comprar un libro de $12.000 o ir al cine por $9.000. Prefiere primero el libro y luego el cine. Elige el libro. ¿Cuál es su costo de oportunidad?",
         ["Comprueba si puede hacer ambas cosas: 12.000 + 9.000 suman 21.000, más de lo que tiene, así que debe elegir una.", "La mejor alternativa a la que renuncia es la que prefería en segundo lugar: el cine."],
         "Ir al cine"),
        ("Identificar agente y escasez", "Una panadería privada tiene un solo horno y esa mañana puede hornear pan amasado o pasteles, no ambos. Decide hornear pan amasado. ¿Qué agente decide, qué es escaso y qué cuesta la decisión?",
         ["Es una empresa, por lo tanto el agente es el sector privado.", "Lo escaso es el tiempo del horno esa mañana, y el costo de oportunidad son los pasteles que no se hornean."],
         "Sector privado; escasea el horno; el costo de oportunidad son los pasteles"),
    ],
    mistakes=[("Creer que el costo de oportunidad es el precio que se paga.", "Se mira solo el dinero y se olvida lo que se deja de hacer.", "Pregunta qué mejor alternativa se pierde al elegir."),
              ("Pensar que solo las familias pobres enfrentan escasez.", "Se confunde escasez con pobreza.", "Todo agente, incluso un país rico, tiene recursos limitados y debe elegir.")],
    T=[
        ("abc", "{F} ¿Por qué la familia Rojas debe elegir?", "Porque el dinero disponible es limitado frente a lo que quiere hacer", "Porque las tres opciones cuestan exactamente lo mismo", "Porque ninguna de las opciones le conviene", "La escasez aparece cuando el dinero no alcanza para todas las opciones deseadas."),
        ("=", "{F} ¿Cuánto dinero (en pesos) le sobra a la familia si paga solo el taller de inglés?", "60000-40000", "Se resta el precio del taller al dinero disponible."),
        ("abc", "En Economía y sociedad: ¿qué es la escasez?", "Que los recursos son limitados frente a necesidades y deseos ilimitados", "Que un producto desaparece de las tiendas", "Que una familia no tiene ingresos", "La escasez es una relación entre recursos limitados y deseos ilimitados, no una falta total ni pobreza."),
        ("abc", "{F} ¿Cuántas de las tres actividades puede pagar la familia con sus $60.000?", "Solo una", "Dos", "Las tres", "Cualquier pareja de opciones suma al menos 65.000, que es más que el dinero disponible."),
        ("En Economía y sociedad: ¿qué es el costo de oportunidad?", "Lo mejor a lo que se renuncia al elegir una opción", "Es la mejor alternativa perdida, no el dinero que se paga."),
        ("abc", "Una empresa de transporte decide comprar un bus nuevo en vez de ampliar su bodega. ¿Qué agente económico toma esa decisión?", "El sector privado", "La familia", "El Estado", "Una empresa pertenece al sector privado, que decide qué producir y cómo invertir."),
        ("{F} Si la familia elige el taller de inglés, ¿cuál es su costo de oportunidad?", "Arreglar la bicicleta de trabajo", "Es la opción que ocupaba el segundo lugar en sus preferencias, y la que pierde al elegir el taller."),
        ("{F} Si la familia elige la salida familiar, ¿cuál es su costo de oportunidad?", "El taller de inglés", "Renuncia a la opción que más prefería, que es la mejor alternativa perdida."),
        ("abc", "Un municipio dispone de recursos para una sola obra: una ciclovía o una sala cuna. Construye la sala cuna. ¿Cuál es el costo de oportunidad?", "Los beneficios de la ciclovía que no se construye", "El dinero gastado en la sala cuna", "Los beneficios de la sala cuna", "El costo de oportunidad es lo que se pierde de la alternativa no elegida, no lo que cuesta la obra elegida."),
        ("{F} Un vecino dice: «El costo de oportunidad del taller es $40.000». ¿Es correcto?", "No: es la bicicleta a la que se renuncia, y $40.000 es el precio pagado", "El costo de oportunidad nombra la alternativa perdida, mientras el dinero pagado es solo el precio."),
        ("abc", "Ana afirma que en un país muy rico no habría escasez. ¿Qué respondería la economía?", "Habría escasez igual, porque los recursos seguirían siendo limitados frente a los deseos", "Ana tiene razón, porque un país rico puede producir todo", "Ana tiene razón, porque la escasez solo afecta a los hogares y no a un país", "La escasez es universal: aun con muchos recursos, los deseos de la sociedad pueden crecer más."),
        ("{F} Un descuento deja el arreglo de la bicicleta en $25.000. ¿Qué dos actividades de la ficha podría pagar ahora la familia juntas?", "El arreglo de la bicicleta y la salida familiar", "25.000 más 30.000 suman 55.000 y cabe en 60.000, mientras las otras parejas suman 65.000 y 70.000."),
        ("abc", "Un gobierno afirma que puede ampliar un servicio sin renunciar a nada. ¿Por qué pediría un economista revisar esa afirmación?", "Porque los recursos son limitados y todo uso tiene un costo de oportunidad", "Porque ampliar un servicio reduce los costos de los demás servicios", "Porque el costo de oportunidad solo existe en las familias", "Si los recursos son limitados, usarlos en algo implica dejar de usarlos en otra cosa."),
    ],
    ctx=("abc", "El centro de estudiantes de un liceo tiene $90.000 para la semana de aniversario. Puede pagar un festival que cuesta $90.000 o dos talleres que cuestan $45.000 cada uno. Eligen los talleres. ¿Cuál es el costo de oportunidad?", "El festival al que renuncian", "Los $90.000 que gastan", "Cada uno de los dos talleres", "Al elegir los talleres, lo mejor que dejan de hacer es el festival."),
    sc=[
        ("En Economía y sociedad: ¿qué estudia la economía?", "Cómo personas, empresas y Estado deciden para enfrentar la escasez", "Es una ciencia social centrada en las decisiones ante recursos limitados."),
        ("Nombra los tres agentes económicos que presenta la explicación.", "Familias, sector privado (empresas) y Estado", "Son quienes toman las decisiones económicas principales."),
        ("¿Por qué elegir implica un costo de oportunidad?", "Porque al usar los recursos limitados en una opción se renuncia a la mejor alternativa", "Todo recurso usado en una cosa deja de estar disponible para otra."),
    ],
    op=("Elige uno de estos dos casos y analízalo. Caso 1 (hogar): Camila tiene $50.000 libres. Puede comprar zapatillas deportivas por $45.000, pagar un curso de fotografía por $30.000 o ahorrar todo; prefiere las zapatillas, luego el curso. "
        "Caso 2 (Estado): un municipio de ejemplo tiene recursos para una sola obra, una plaza con juegos o un consultorio ampliado. "
        "Escribe qué agente decide, qué es escaso, las opciones, qué elegirías tú y por qué, y cuál sería el costo de oportunidad de tu elección.",
        "Caso 1. Decide una familia o persona; escasea el dinero ($50.000). Si compra las zapatillas, no alcanza el curso (45.000 + 30.000 suman 75.000). Costo de oportunidad: el curso de fotografía.",
        ["identifica el agente económico", "nombra el recurso escaso", "señala el costo de oportunidad como la mejor alternativa perdida", "justifica la elección con una razón"],
        ["texto breve con agente, escasez, opciones, elección y costo de oportunidad"],
        ["confundir el costo de oportunidad con el precio", "nombrar como costo de oportunidad todas las opciones perdidas", "no justificar la elección"],
        "Pregunta: «¿a qué opción renuncias exactamente?». Si cita el precio, pídele que nombre la alternativa."),
    reinforce="Escribe tres decisiones que tomaste esta semana y, para cada una, la alternativa a la que renunciaste (tu costo de oportunidad).",
    extend="Compara cómo se expresa la escasez en una familia, en una panadería y en un municipio: ¿qué es escaso en cada uno y qué decisiones debe tomar?",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (caso de ejemplo, ficticio). Un grupo de investigación de ejemplo quiere saber si bajar el precio de los pasajes de un bus escolar aumenta el número de estudiantes que lo usan. "
     "Supuesto del modelo: «Todo lo demás permanece igual (frecuencia de buses, clima, horario de clases)». Dato de ejemplo: con pasaje de $600 viajan 400 estudiantes por día; con pasaje de $500 viajan 440 por día. "
     "Dato de la experiencia de una comuna de ejemplo: al bajar el pasaje, también se agregó un bus, y los viajeros subieron a 480.")
build(
    O1, 2, F,
    use="Aprenderé cómo trabaja la economía como ciencia: construye modelos con supuestos, contrasta con datos y experiencias, y reconoce los límites de lo que concluye.",
    prior=["Sé qué es la escasez y el costo de oportunidad.", "Sé leer datos simples de una tabla.", "Distingo un dato de una opinión."],
    explain=[
        "La economía usa un método científico: observa una situación, formula una explicación, la contrasta con datos y la corrige si los datos no la respaldan. Como no puede encerrar a la sociedad en un laboratorio, trabaja con modelos, que son versiones simplificadas de la realidad que dejan fuera detalles para ver una relación importante, y con experiencias económicas, es decir, casos reales de políticas o mercados que sirven como evidencia.",
        "Todo modelo parte de supuestos, que son condiciones que se aceptan para poder razonar. Un supuesto muy usado es ceteris paribus, expresión latina que significa «todo lo demás constante»: se analiza el efecto de un solo factor, imaginando que los demás no cambian. Los supuestos permiten ordenar el pensamiento, pero si la realidad se aleja mucho de ellos, las conclusiones del modelo pierden fuerza.",
        "Una hipótesis es una afirmación que se puede contrastar con datos, por ejemplo: «si baja el precio, sube la cantidad demandada». Los datos pueden apoyarla o contradecirla, y una experiencia real rara vez cumple todos los supuestos. Por eso un economista no declara «demostrado» un resultado con un solo caso: busca varios, revisa qué otros factores cambiaron y explica sus límites.",
    ],
    vocab=[("modelo económico", "versión simplificada de la realidad para ver una relación"), ("supuesto", "condición que se acepta para poder razonar"), ("ceteris paribus", "todo lo demás constante"), ("hipótesis", "afirmación que se puede contrastar con datos"), ("experiencia económica", "caso real de mercado o de política que sirve como evidencia"), ("contrastar", "comparar una explicación con los datos para ver si los respaldan")],
    worked=[
        ("Reconocer un supuesto", "Un modelo de ejemplo dice: «Si sube el precio de las manzanas, se compran menos manzanas, suponiendo que el ingreso de las personas no cambia». ¿Cuál es el supuesto?",
         ["Busca la condición que se mantiene fija para aislar el efecto del precio.", "Es el ingreso de las personas, que se supone constante."],
         "Que el ingreso de las personas no cambia"),
        ("Contrastar una hipótesis", "Hipótesis de ejemplo: «si baja el precio de una entrada al teatro, más personas asisten». Datos de ejemplo: con entrada de $4.000 asisten 120 personas; con $3.000, 150. ¿Los datos apoyan la hipótesis?",
         ["Compara los dos casos: bajó el precio de 4.000 a 3.000 y la asistencia pasó de 120 a 150.", "La asistencia subió, lo que concuerda con la hipótesis, aunque son solo dos observaciones y otros factores podrían influir."],
         "Sí la apoyan, con la salvedad de que son pocos datos"),
    ],
    mistakes=[("Pensar que un modelo falla porque es más simple que la realidad.", "Se confunde simplificar con equivocarse.", "Un modelo se simplifica a propósito; se evalúa por si explica bien lo que quiere explicar."),
              ("Dar por demostrada una hipótesis con un solo caso.", "Se ignora que otros factores pudieron cambiar.", "Busca más casos y revisa qué otras cosas variaron.")],
    T=[
        ("abc", "{F} ¿Qué supuesto declara el modelo?", "Que todo lo demás permanece igual", "Que los estudiantes no necesitan viajar", "Que los estudiantes deciden sin considerar el precio", "El modelo fija la frecuencia, el clima y el horario para aislar el efecto del precio."),
        ("abc", "En Economía y sociedad: ¿qué es un modelo económico?", "Una versión simplificada de la realidad para estudiar una relación", "Una copia exacta de un mercado real", "Una predicción que se cumple en todos los casos", "Un modelo omite detalles a propósito para destacar una relación, y no copia la realidad."),
        ("=", "{F} Según el dato del modelo, ¿cuántos estudiantes más por día viajan al bajar el pasaje de $600 a $500?", "440-400", "Se restan los viajeros del pasaje de $600 a los del pasaje de $500."),
        ("abc", "¿Qué significa ceteris paribus?", "Todo lo demás constante", "Todo lo demás cambia a la vez", "Solo importa el precio", "Es la expresión que indica que se analiza un factor mientras los otros se mantienen fijos."),
        ("En Economía y sociedad: ¿qué es una hipótesis?", "Una afirmación que se puede contrastar con datos", "Se diferencia de una opinión porque los datos pueden apoyarla o contradecirla."),
        ("abc", "{F} ¿Qué parte de la ficha corresponde a una experiencia económica de una comuna?", "El dato de la comuna de ejemplo donde también se agregó un bus", "El supuesto de que todo lo demás se mantiene igual", "El cálculo con el pasaje de $500", "Una experiencia económica es un caso real, y la comuna aplicó una política concreta."),
        ("{F} En la experiencia de la comuna subieron los viajeros a 480. ¿Se cumple allí el supuesto «todo lo demás igual»?", "No, porque además de bajar el pasaje se agregó un bus", "El bus extra cambia otro factor, de modo que el supuesto del modelo no se mantuvo."),
        ("abc", "{F} Un asesor dice: «Los 480 viajeros prueban que bajar el pasaje por sí solo sube la demanda». ¿Qué falla en ese razonamiento?", "Se cambió también la frecuencia, y no se sabe cuánto aportó cada cambio", "Los datos son demasiado pocos para tener cualquier valor", "Los 480 viajeros son menos que los 440 del modelo", "Dos factores cambiaron a la vez, así que el efecto del pasaje queda mezclado con el del bus."),
        ("abc", "Un modelo supone que todas las personas tienen el mismo ingreso. Una economista compara con un barrio donde los ingresos son muy distintos. ¿Qué conclusión es razonable?", "Los resultados del modelo deben usarse con cautela en ese barrio", "El modelo debe descartarse de inmediato", "El modelo sirve igual de bien, porque un modelo siempre es exacto", "Cuando la realidad se aleja del supuesto, la conclusión pierde fuerza, pero no se vuelve inútil sin más."),
        ("{F} Con el dato de $600 y $500, un estudiante calcula que cada $100 de rebaja suma 40 viajeros por día y proyecta que con pasaje $0 viajarían 640. ¿Qué advertencia metodológica harías?", "Extrapola con solo dos puntos y supone un efecto igual en todo rango, lo cual no está comprobado", "Con solo dos observaciones no se puede asumir que la relación siga igual fuera del rango observado."),
        ("abc", "¿Qué debe hacer un economista que obtiene un resultado distinto al que su modelo preveía?", "Revisar sus supuestos y buscar otras explicaciones o más datos", "Ocultar el dato que no calza", "Cambiar los datos para que calcen con el modelo", "El método científico exige ajustar la explicación cuando los datos no la respaldan."),
        ("abc", "{F} Si quisieras reforzar la hipótesis sobre el pasaje, ¿qué evidencia sería más útil?", "Casos de otras comunas donde solo bajó el pasaje y no cambió nada más", "Una opinión de un vecino sobre si le gusta el bus", "Un dato de la misma comuna donde ya se había agregado un bus", "Casos que cumplan mejor el supuesto aislan el efecto del precio."),
        ("¿Por qué un modelo con supuestos poco realistas puede ser igualmente útil?", "Porque ayuda a ver una relación clave, siempre que se declaren sus límites", "Un modelo no pretende reproducir todo, sino aclarar una relación, con sus límites explícitos."),
    ],
    ctx=("abc", "Una feria libre de ejemplo baja el arriendo del puesto de $20.000 a $15.000 por día para atraer más comerciantes. Al mismo tiempo, llegan tres buses de turistas a la feria. Si el número de comerciantes sube, ¿qué puede concluir un economista?", "Que no puede atribuir el aumento solo al arriendo, porque también cambió la llegada de turistas", "Que el arriendo bajo explica todo el aumento", "Que los turistas no influyen en los comerciantes", "Con dos factores cambiando a la vez no se aísla el efecto del arriendo."),
    sc=[
        ("En Economía y sociedad: ¿qué es un supuesto?", "Una condición que se acepta para poder razonar", "Permite aislar una relación aunque simplifique la realidad."),
        ("¿Para qué sirve contrastar una hipótesis con datos?", "Para ver si los datos la respaldan o la contradicen", "El método científico exige comparar la explicación con evidencia."),
        ("¿Por qué una sola experiencia no basta para dar algo por demostrado?", "Porque otros factores pudieron cambiar y el caso puede no repetirse", "Se necesitan varios casos y revisar qué más varió."),
    ],
    op=("Analiza esta hipótesis de ejemplo: «si sube el precio de las bebidas azucaradas en un kiosco escolar, los estudiantes compran menos». "
        "Datos de ejemplo: con precio $1.200 se vendían 90 bebidas por semana; con $1.500, 70. En esa misma semana, además, el kiosco agregó una oferta de jugos naturales. "
        "Escribe: (1) el supuesto del modelo; (2) si los datos apoyan la hipótesis; (3) qué otro factor cambió; (4) qué dato adicional pedirías.",
        "(1) Que lo demás se mantiene igual. (2) La venta bajó de 90 a 70, lo que apoya la hipótesis. (3) La oferta de jugos pudo reducir la compra de bebidas. (4) Ventas de otro kiosco que subió el precio sin agregar jugos.",
        ["declara el supuesto ceteris paribus", "compara los datos con la hipótesis", "identifica el factor que contamina la evidencia", "pide un dato adicional pertinente"],
        ["texto de cuatro respuestas numeradas"],
        ["afirmar que los datos demuestran la hipótesis sin salvedad", "no notar la oferta de jugos", "pedir un dato que repite la misma evidencia"],
        "Pregunta: «¿qué cambió además del precio?». Si no lo ve, pídele que relea los datos de la semana."),
    reinforce="Escribe una hipótesis económica sobre tu entorno (por ejemplo, el precio de una entrada o de un pasaje) y el supuesto que declararías.",
    extend="Explica por qué los experimentos de laboratorio, comunes en física, son más difíciles en economía, y qué papel cumplen las experiencias reales.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (casos de ejemplo, ficticios). Caso 1: Valentina elige entre trabajar 5 horas extra en una tienda, por las que le pagan $20.000 en total, o estudiar esas 5 horas para una prueba. Se decide por estudiar. "
     "Caso 2: Un pastelero considera hacer una torta más por la tarde: el costo adicional (ingredientes y gas) es $8.000 y la vendería en $12.000. "
     "Caso 3: Un municipio de ejemplo sube de $500 a $1.000 la tarifa de estacionamiento en el centro. Al mes siguiente hay menos autos estacionados.")
build(
    O1, 3, F,
    use="Aprenderé cuatro principios básicos de la economía (disyuntivas, costo de oportunidad, decisiones al margen e incentivos) y los usaré para explicar decisiones cotidianas.",
    prior=["Sé qué es la escasez y el costo de oportunidad.", "Sé qué es un modelo y un supuesto.", "Sé restar cantidades de dinero."],
    explain=[
        "La economía se apoya en algunos principios fundamentales. El primero: las personas enfrentan disyuntivas, es decir, situaciones en que obtener algo exige renunciar a otra cosa. El segundo: el costo de algo es lo que se entrega a cambio, y eso incluye el costo de oportunidad, que a veces no es dinero sino tiempo.",
        "El tercer principio: las personas racionales piensan al margen. Decidir al margen es comparar el beneficio y el costo adicional de hacer un poquito más, no el total. Un pastelero no pregunta si le conviene la pastelería en general, sino si le conviene hacer una torta más. El cuarto principio: las personas responden a incentivos, que son premios o castigos que cambian lo atractiva que resulta una acción.",
        "Estos principios no dicen qué es justo ni qué debería hacerse: describen cómo suelen funcionar las decisiones. Sirven para formular hipótesis y explicar casos. Como todo principio de un modelo, tienen límites: las personas no siempre calculan con precisión ni cuentan con toda la información, algo que se verá al estudiar economía del comportamiento.",
    ],
    vocab=[("disyuntiva", "situación en que obtener algo exige renunciar a otra cosa"), ("decidir al margen", "comparar beneficio y costo de hacer un poco más"), ("incentivo", "premio o castigo que cambia qué tan atractiva es una acción"), ("beneficio adicional", "lo que se gana por una unidad más"), ("costo adicional", "lo que cuesta una unidad más"), ("principio económico", "idea básica que ayuda a explicar decisiones")],
    worked=[
        ("Aplicar el principio al margen", "Una heladería de ejemplo puede preparar una tanda más de helados: costaría $15.000 y se vendería por $18.000. ¿Le conviene?",
         ["Compara el beneficio adicional (18.000) con el costo adicional (15.000).", "El beneficio supera al costo en 3.000, así que conviene hacerla."],
         "Sí, porque gana 3.000 más de lo que cuesta"),
        ("Reconocer un incentivo", "Una empresa de ejemplo ofrece un bono de $30.000 a quienes lleguen puntuales todo el mes. ¿Qué principio ilustra y qué efecto se espera?",
         ["El bono es un premio que cambia lo atractivo de llegar a la hora.", "Se espera que más personas lleguen puntuales."],
         "Incentivos: se espera mayor puntualidad"),
    ],
    mistakes=[("Decidir mirando el total y no lo adicional.", "Se olvida que lo relevante es qué cambia con una unidad más.", "Compara el costo y el beneficio de la próxima unidad."),
              ("Creer que un incentivo siempre es dinero.", "Se confunde incentivo con pago.", "Un incentivo puede ser tiempo, reconocimiento, comodidad o una sanción.")],
    T=[
        ("abc", "{F} ¿Qué principio muestra el Caso 1 de Valentina?", "Las personas enfrentan disyuntivas: estudiar implica renunciar al pago", "Las personas deciden sin comparar alternativas", "El pago no tiene costo de oportunidad", "Obtener algo (preparación para la prueba) exige renunciar a otra cosa (el pago)."),
        ("=", "{F} En el Caso 2, ¿cuánto más es el beneficio adicional que el costo adicional de la torta? (en pesos)", "12000-8000", "Se resta el costo adicional al beneficio adicional."),
        ("abc", "En Economía y sociedad: ¿qué significa decidir al margen?", "Comparar el costo y el beneficio de una unidad adicional", "Decidir sin pensar en nada", "Comparar solo el costo total", "El análisis marginal se centra en el cambio que produce hacer un poco más."),
        ("{F} En el Caso 1, ¿cuál es el costo de oportunidad de estudiar esas cinco horas?", "Los $20.000 que habría ganado trabajando", "Es la mejor alternativa a la que renuncia al elegir estudiar."),
        ("abc", "{F} ¿Qué efecto indica el Caso 3 sobre el incentivo de estacionar?", "Al subir la tarifa, estacionar es menos atractivo y baja el número de autos", "La tarifa más alta atrae más autos", "La tarifa no influye en la decisión", "Una tarifa más cara es un incentivo negativo para estacionar."),
        ("ab", "{F} En el Caso 2, ¿conviene al pastelero hacer la torta adicional?", "Sí, porque el beneficio adicional supera al costo adicional", "No, porque el costo no es cero", "Gana 4.000 más de lo que cuesta, así que la torta adicional es rentable."),
        ("abc", "Un restaurante de ejemplo ofrece menú gratis el día del cumpleaños a quien reserve con una semana de anticipación. ¿Qué principio ilustra?", "Las personas responden a incentivos", "Las personas no responden a premios", "Los restaurantes no toman decisiones al margen", "El menú gratis es un premio que cambia el atractivo de reservar con anticipación."),
        ("abc", "Una joven tiene una tarde libre. Puede trabajar en cuidar niños por $15.000 o ir a un paseo con amigos. Va al paseo. ¿Qué es lo correcto afirmar?", "Pagó con el costo de oportunidad de $15.000 en tiempo y dinero no ganado", "Al paseo no le cuesta nada porque es gratis", "Gastó $15.000 en el paseo", "Aunque el paseo no cueste dinero, renunciar al trabajo tiene un costo de oportunidad."),
        ("{F} Un vecino dice: «Con la tarifa más alta nadie estacionará en el centro». ¿Qué precisión harías usando lo aprendido?", "Los incentivos cambian cuántos estacionan, pero no hacen que nadie lo haga necesariamente", "El caso solo señala que hay menos autos, no que no haya ninguno."),
        ("abc", "{F} Una pastelera de ejemplo piensa hacer una torta adicional por la tarde: pagaría $10.000 en ingredientes y horas extra y la vendería en $12.000. Según el principio de decidir al margen, ¿qué conviene?", "Hacerla, porque el beneficio adicional (12.000) supera su costo adicional (10.000)", "No hacerla, porque 10.000 es mucho dinero", "No hacerla, porque debe comparar con el costo total de toda la pastelería", "Lo relevante es comparar lo adicional, y 12.000 es mayor que 10.000."),
        ("abc", "{F} ¿Qué diferencia hay entre los principios que ilustran el Caso 2 y el Caso 3?", "El pastelero decide al margen y el municipio usa un incentivo", "Los dos aplican exactamente el mismo principio", "Ninguno aplica un principio económico", "El Caso 2 compara costo y beneficio adicional, mientras el Caso 3 cambia una conducta por una tarifa."),
        ("abc", "Un estudiante dice: «Los principios de la economía describen cómo debería actuar siempre la gente». ¿Qué corrección corresponde?", "Describen cómo suelen funcionar las decisiones, sin decir qué es justo", "Son órdenes legales que todos deben cumplir", "Son reglas que deben aplicarse en todas las decisiones", "Los principios sirven para explicar y formular hipótesis, no para ordenar conductas."),
        ("Una empresa de ejemplo premia con $10.000 a quien proponga una mejora, pero descubre que muchos proponen ideas sin valor para cobrar el premio. ¿Qué enseña esto sobre los incentivos?", "Que los incentivos cambian conductas, y a veces de maneras no previstas", "Las personas responden al premio, y un diseño pobre puede producir efectos no buscados."),
    ],
    ctx=("abc", "Un liceo de ejemplo quiere que los estudiantes lleguen antes a clases. Puede (1) dar un punto en la nota de convivencia a quien llegue puntual o (2) agregar una hora de clases extra para todos si hay atrasos. ¿Cuál es un incentivo positivo?", "El punto en la nota por llegar puntual", "La hora de clases extra por atrasos", "Ninguno es un incentivo", "Un punto en la nota es un premio que hace más atractiva la puntualidad."),
    sc=[
        ("¿Cuáles son los cuatro principios que presenta la explicación?", "Disyuntivas, costo de oportunidad, decisión al margen e incentivos", "Son las ideas básicas que ayudan a explicar decisiones."),
        ("En Economía y sociedad: ¿qué es un incentivo?", "Un premio o castigo que cambia qué tan atractiva es una acción", "No tiene que ser dinero: puede ser tiempo, reconocimiento o una sanción."),
        ("¿Por qué conviene hacer una unidad más cuando el beneficio adicional supera al costo adicional?", "Porque la decisión aumenta la ganancia neta", "Al margen, si se gana más de lo que cuesta, la unidad aporta."),
    ],
    op=("Elige una de estas dos situaciones de ejemplo y explícala con los principios. Situación 1: un taller de ropa decide hacer 10 poleras más por $60.000 de costo adicional y las vendería por $75.000. "
        "Situación 2: un cine de barrio ofrece entrada a mitad de precio los martes. Indica qué principios operan, calcula lo que puedas con los datos y escribe una conclusión de dos oraciones.",
        "Situación 1. Principio: decidir al margen. Beneficio adicional 75.000 menos costo adicional 60.000 son 15.000, así que conviene hacer las 10 poleras.",
        ["nombra al menos un principio pertinente", "usa los datos para calcular o argumentar", "escribe una conclusión coherente con el cálculo"],
        ["texto breve con principios, cálculo y conclusión"],
        ["comparar el costo total con el beneficio de una sola unidad", "olvidar el costo de oportunidad", "dar una conclusión que contradice el cálculo"],
        "Pregunta: «¿qué cambia si haces una unidad más?». Si habla del total, pídele que mire solo lo adicional."),
    reinforce="Escribe un ejemplo de tu vida de cada uno de los cuatro principios (disyuntiva, costo de oportunidad, decisión al margen, incentivo).",
    extend="Busca una norma o regla de tu liceo que funcione como incentivo y explica a quién y qué conducta busca cambiar.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (afirmaciones de ejemplo). Afirmación 1: «En el último año, el precio de una docena de huevos en el almacén de ejemplo pasó de $3.200 a $3.600.» "
     "Afirmación 2: «El Estado debería fijar un precio máximo para los huevos.» "
     "Afirmación 3: «Si el precio de los huevos sube, las personas compran menos huevos.» "
     "Afirmación 4: «Es injusto que las familias de menores ingresos gasten una parte mayor de su sueldo en alimentos.»")
build(
    O1, 4, F,
    use="Aprenderé a distinguir el análisis positivo (lo que es, se contrasta con datos) del normativo (lo que debería ser, depende de valores) y a explicar cómo se relacionan en la economía.",
    prior=["Sé qué es una hipótesis.", "Distingo un hecho de una opinión.", "Sé qué es un modelo económico."],
    explain=[
        "El análisis positivo describe cómo funciona la economía: es decir, trata de lo que es. Sus afirmaciones se pueden contrastar con datos, y pueden resultar verdaderas o falsas. «El precio subió de 3.200 a 3.600» es una afirmación positiva, porque se puede comprobar con una boleta o una estadística.",
        "El análisis normativo opina sobre cómo debería ser la economía: trata de lo que debería ser. Sus afirmaciones dependen de valores, como la justicia, la libertad o la eficiencia, y no se resuelven solo con datos. «El Estado debería fijar un precio máximo» es normativa, porque requiere decidir qué se valora más y a quién se protege.",
        "Ambos análisis se necesitan. Para decidir bien una política hacen falta datos y modelos (lo positivo) y también una discusión sobre los valores (lo normativo). Una afirmación normativa puede apoyarse en hechos, pero los hechos solos no la demuestran. Distinguir los dos tipos ayuda a no discutir como si fueran hechos cosas que son valoraciones, ni al revés.",
    ],
    vocab=[("análisis positivo", "describe lo que es y se contrasta con datos"), ("análisis normativo", "opina sobre lo que debería ser y depende de valores"), ("afirmación positiva", "enunciado que puede ser verdadero o falso según datos"), ("afirmación normativa", "enunciado que expresa un juicio de valor"), ("juicio de valor", "opinión sobre lo bueno, lo justo o lo deseable"), ("política económica", "decisión del Estado para influir en la economía")],
    worked=[
        ("Clasificar una afirmación", "«La cantidad de pan que se vende cae cuando el precio sube.» ¿Es positiva o normativa?",
         ["Pregunta si se puede contrastar con datos de ventas y precios.", "Sí se puede, y puede resultar verdadera o falsa."],
         "Positiva"),
        ("Separar hechos y valores", "«El desempleo bajó, así que el gobierno hizo bien las cosas.» ¿Qué parte es positiva y cuál normativa?",
         ["«El desempleo bajó» se puede comprobar con datos: es positiva.", "«El gobierno hizo bien las cosas» es un juicio de valor: es normativa."],
         "Primera parte positiva, segunda normativa"),
    ],
    mistakes=[("Pensar que normativo significa «falso» o «sin valor».", "Se confunde juicio de valor con error.", "Una afirmación normativa no es verdadera ni falsa según datos, pero se puede discutir con argumentos."),
              ("Creer que un dato basta para zanjar una afirmación normativa.", "Se olvida que dependen de valores.", "Usa los datos para informar la discusión, y debate los valores aparte.")],
    T=[
        ("abc", "{F} ¿Cuál de las afirmaciones es una afirmación positiva?", "La Afirmación 1, sobre el precio de la docena de huevos", "La Afirmación 2, sobre fijar un precio máximo", "La Afirmación 4, sobre lo injusto", "Se puede comprobar con datos si el precio pasó de 3.200 a 3.600."),
        ("abc", "{F} ¿Por qué la Afirmación 2 es normativa?", "Dice lo que el Estado debería hacer y depende de valores", "Porque contiene números", "Porque habla de huevos", "El verbo «debería» expresa un juicio sobre lo deseable, no un hecho verificable."),
        ("=", "{F} ¿Cuántos pesos subió la docena de huevos según la Afirmación 1?", "3600-3200", "Se resta el precio anterior al precio nuevo."),
        ("abc", "En Economía y sociedad: ¿qué describe el análisis positivo?", "Lo que es, y se contrasta con datos", "Lo que debería ser, según valores", "Lo que es justo para todos", "El análisis positivo describe hechos y relaciones que pueden verificarse."),
        ("abc", "{F} La Afirmación 3 dice que si sube el precio se compra menos. ¿Qué tipo de afirmación es?", "Positiva, porque se puede contrastar con datos de compras", "Normativa, porque habla de personas", "Ninguna, porque no tiene números", "Se puede comprobar con datos si la cantidad comprada cae cuando sube el precio."),
        ("ab", "¿Qué tipo de análisis es «las tarifas de la locomoción deberían ser más bajas»?", "Normativo", "Positivo", "La frase usa «deberían», que expresa un juicio de valor sobre lo deseable."),
        ("{F} La Afirmación 4 menciona justicia. ¿Qué valor expresa y de qué tipo es el enunciado?", "Justicia; es normativo", "El término «injusto» expresa un valor y no puede resolverse solo con datos."),
        ("abc", "«El desempleo bajó, así que la política fue buena». ¿Qué conviene separar para analizar este enunciado?", "El hecho (el desempleo bajó) y el juicio (la política fue buena)", "Nada, porque ambas partes son hechos", "Nada, porque ambas partes son opiniones", "La primera parte es contrastable y la segunda depende de valores."),
        ("abc", "{F} Una economista afirma: «Un precio máximo para los huevos generaría escasez de huevos en el almacén». ¿Qué tipo de afirmación es?", "Positiva, porque predice un efecto que se puede contrastar", "Normativa, porque habla de una política", "Ni positiva ni normativa", "Aunque trate de una política, predice un efecto que puede verificarse con datos."),
        ("{F} Con la Afirmación 2, explica cómo podrían aportar datos a una discusión normativa.", "Mostrando qué efectos tendría el precio máximo, aunque decidir si debe aplicarse depende de valores", "Los datos informan los efectos, pero la decisión final exige ponderar valores como justicia o eficiencia."),
        ("abc", "Dos personas discuten: una dice «el pan subió» y otra «el pan debería ser gratis». ¿Qué tipo de desacuerdo hay?", "Uno puede resolverse con datos y el otro depende de valores", "Los dos pueden resolverse con datos", "Los dos dependen solo de valores", "El primero es verificable y el segundo expresa un juicio sobre lo deseable."),
        ("abc", "{F} Si un dato mostrara que el precio de los huevos no subió, ¿qué afirmación quedaría falsa?", "La Afirmación 1", "La Afirmación 2", "La Afirmación 4", "Solo una afirmación positiva como la 1 puede resultar falsa por los datos."),
        ("Un político dice: «Los datos prueban que debemos subir los impuestos». ¿Qué falla en esa frase?", "Los datos pueden informar efectos, pero «debemos» es normativo y no lo demuestran solos", "Un juicio normativo no se prueba solo con datos."),
    ],
    ctx=("abc", "En un debate de ejemplo sobre el transporte, una estudiante dice: «El pasaje subió 10% el año pasado». Otro responde: «Debería haber pasaje gratis para estudiantes». Una tercera dice: «Si el pasaje sube, viaja menos gente». ¿Cuántas afirmaciones son positivas?", "Dos", "Una", "Tres", "La primera y la tercera se pueden contrastar con datos, y la segunda expresa un deber."),
    sc=[
        ("En Economía y sociedad: ¿qué es un análisis normativo?", "Una opinión sobre cómo debería ser la economía, según valores", "Se basa en juicios sobre lo justo, lo deseable o lo eficiente."),
        ("¿Qué palabra suele indicar una afirmación normativa?", "Debería", "Señala un juicio de valor sobre lo deseable."),
        ("¿Por qué una buena decisión de política necesita ambos análisis?", "Porque los datos informan los efectos y los valores orientan qué se prefiere", "Sin datos se decide a ciegas y sin valores no hay criterio."),
    ],
    op=("Lee estas cuatro frases de ejemplo sobre una política de ejemplo: (1) «Con el subsidio al transporte escolar, 300 estudiantes más llegan al liceo cada día.» (2) «El subsidio es una inversión justa en el futuro.» "
        "(3) «Si se retira el subsidio, el gasto en pasajes de las familias sube.» (4) «El Estado debería subsidiar solo a los hogares de menores ingresos.» Clasifica cada una como positiva o normativa, explica tu criterio y escribe un párrafo de cuatro líneas sobre qué datos y qué valores usarías para decidir.",
        "(1) Positiva: se puede contrastar con datos. (2) Normativa: usa «justa». (3) Positiva: predice un efecto verificable. (4) Normativa: usa «debería». Datos: costo del subsidio y quiénes lo reciben; valores: justicia y eficiencia.",
        ["clasifica correctamente las cuatro frases", "explica el criterio con las palabras «contrastable» o «juicio de valor»", "separa datos y valores en el párrafo final"],
        ["clasificación con criterio y párrafo breve"],
        ["clasificar por la presencia de números y no por el tipo de enunciado", "tomar partido sin argumentos", "mezclar hechos y valores en una sola frase"],
        "Pregunta: «¿esto se podría verificar con una estadística?». Si dice que sí, es positivo."),
    reinforce="Escribe dos afirmaciones positivas y dos normativas sobre el precio de un producto que conozcas.",
    extend="Elige una noticia de economía y subraya, con dos colores, lo que es positivo y lo que es normativo.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (caso de ejemplo, ficticio). El municipio de Lomas del Sur dispone de $60.000.000 para mejorar el barrio. Tiene dos proyectos: Proyecto Luz, que instala luminarias en 20 calles y cuesta $40.000.000; "
     "Proyecto Plaza, que construye una plaza con juegos y cuesta $35.000.000. El concejo de ejemplo debate. Postura 1: «Conviene la luminaria, porque reduce el riesgo en la noche». Postura 2: «Conviene la plaza, porque se usa por todas las edades». "
     "Un estudio de ejemplo indica que en las calles con luminarias nuevas hubo menos asaltos reportados, y que la plaza sería usada por unas 500 personas a la semana.")
build(
    O1, 5, F,
    use="Aprenderé a evaluar alternativas aplicando lo estudiado: escasez, costo de oportunidad, análisis positivo y normativo, para decidir con razones y reconocer sus límites.",
    prior=["Sé qué es el costo de oportunidad.", "Distingo afirmaciones positivas y normativas.", "Sé qué es un modelo y su supuesto."],
    explain=[
        "Evaluar alternativas consiste en comparar las opciones disponibles según criterios claros. Un criterio es una característica que permite juzgar si una opción es buena, como el costo, la cantidad de personas beneficiadas, el tiempo que demora o el efecto en el largo plazo. Sin criterios explícitos, la comparación se vuelve solo una preferencia.",
        "Una buena evaluación económica sigue pasos: identificar el problema y el recurso escaso, listar las alternativas viables, estimar costos y beneficios de cada una (con datos o supuestos declarados), nombrar el costo de oportunidad de elegir cada una, separar lo positivo de lo normativo y, finalmente, decidir justificando qué valores se priorizan. Esa decisión debe quedar abierta a la crítica.",
        "También hay que reconocer los límites: los datos pueden ser incompletos, los supuestos pueden no cumplirse y personas con valores distintos pueden elegir distinto aun con los mismos datos. Por eso un análisis económico serio presenta las posturas con sus argumentos, indica qué evidencia falta y evita presentar como «única respuesta» lo que depende también de valores.",
    ],
    vocab=[("criterio", "característica que permite juzgar una opción"), ("alternativa viable", "opción posible con los recursos disponibles"), ("beneficiarios", "personas que reciben el efecto de una decisión"), ("largo plazo", "efectos que se ven después de mucho tiempo"), ("evaluar", "comparar opciones con criterios y razones"), ("postura", "posición que alguien defiende con argumentos")],
    worked=[
        ("Comprobar una alternativa viable", "Un colegio de ejemplo tiene $8.000.000. ¿Es viable un laboratorio de $5.000.000 y una cancha de $4.500.000 al mismo tiempo?",
         ["Suma los costos: 5.000.000 más 4.500.000 dan 9.500.000.", "Como 9.500.000 es más que 8.000.000, no pueden hacerse las dos."],
         "No es viable hacer ambas: hay que elegir"),
        ("Separar criterios y valores", "Postura de ejemplo: «Conviene el laboratorio porque lo usan más estudiantes». ¿Qué criterio usa y qué valor supone?",
         ["Criterio: cantidad de estudiantes beneficiados.", "Valor: que conviene beneficiar a la mayor cantidad posible."],
         "Criterio: beneficiarios; valor: llegar a más personas"),
    ],
    mistakes=[("Elegir la alternativa «más barata» sin mirar a quiénes beneficia.", "Se usa un solo criterio y se ignoran otros.", "Compara con varios criterios y declara cuál priorizas."),
              ("Presentar una decisión que depende de valores como si fuera un hecho.", "Se olvida la parte normativa.", "Indica qué valor orienta tu elección y qué otros valores darían otra decisión.")],
    T=[
        ("abc", "{F} ¿Pueden hacerse ambos proyectos con los recursos disponibles?", "No, porque suman más de los $60.000.000", "Sí, porque cada uno cuesta menos que el total", "Sí, porque el Estado puede gastar el mismo dinero dos veces", "Los dos juntos cuestan 75.000.000, más que el presupuesto."),
        ("=", "{F} ¿Cuántos pesos costarían los dos proyectos juntos?", "40000000+35000000", "Se suman los costos de las dos obras."),
        ("abc", "En Economía y sociedad: ¿qué es un criterio de evaluación?", "Una característica que permite juzgar si una opción es buena", "Una orden que impone el Estado", "Un resultado que ya se conoce", "Los criterios, como el costo o los beneficiarios, permiten comparar alternativas de modo explícito."),
        ("abc", "{F} ¿Qué criterio usa la Postura 2 para preferir la plaza?", "La variedad de personas que la usarían", "El costo menor de la obra", "La reducción del riesgo nocturno", "Argumenta que la plaza se usa por todas las edades."),
        ("{F} Si el municipio elige la plaza, ¿cuál es el costo de oportunidad?", "Los beneficios del Proyecto Luz", "Es la alternativa a la que se renuncia al elegir la plaza."),
        ("ab", "{F} ¿Qué tipo de afirmación es «en las calles con luminarias nuevas hubo menos asaltos reportados»?", "Positiva, porque se puede contrastar con datos", "Normativa, porque habla de seguridad", "Es un dato del estudio de ejemplo que puede comprobarse con reportes."),
        ("{F} Calcula cuánto dinero sobraría del presupuesto si se elige el Proyecto Luz.", "20.000.000", "Del presupuesto de 60.000.000 se resta el costo de 40.000.000."),
        ("abc", "{F} Un concejal propone elegir la alternativa más barata. ¿Qué proyecto elegiría con ese único criterio?", "El Proyecto Plaza", "El Proyecto Luz", "Ninguno", "La plaza cuesta 35.000.000 y la luminaria 40.000.000."),
        ("abc", "{F} ¿Qué dato adicional ayudaría a decidir mejor entre ambos proyectos?", "Cuántas personas se benefician con las luminarias en comparación con las 500 de la plaza", "La opinión personal de cada concejal sobre los proyectos", "El costo de otros proyectos que el municipio ya terminó", "Comparar beneficiarios con la misma medida permite evaluar bajo el mismo criterio."),
        ("{F} Imagina que dos concejales aceptan los mismos datos, pero uno elige la luminaria y otro la plaza. ¿Cómo puede explicarse?", "Porque priorizan valores distintos, como seguridad o uso por todas las edades", "Los datos no resuelven por sí solos la parte normativa de la decisión."),
        ("abc", "{F} La Postura 1 dice «Conviene la luminaria». ¿Qué le falta para ser una evaluación completa?", "Comparar costos, beneficiarios y costo de oportunidad con la otra opción", "Cambiar el nombre del proyecto", "Eliminar los números", "Una postura sólida usa criterios explícitos y considera lo que se pierde."),
        ("abc", "{F} Un asesor dice: «Los datos demuestran que la luminaria es lo correcto». ¿Qué objeción es más pertinente?", "El dato informa un efecto, pero decidir qué priorizar depende de valores", "El dato es falso porque viene de un estudio", "Hubo menos asaltos, así que la plaza no tiene ningún beneficio", "Elegir entre proyectos incluye juicios de valor que los datos no zanjan."),
        ("Nombra dos límites que debería declarar un análisis como el de la ficha.", "Datos incompletos (por ejemplo, un estudio de pocas calles) y supuestos que podrían no cumplirse", "Un análisis serio dice qué evidencia falta y qué supuestos usa."),
    ],
    ctx=("abc", "Un centro de estudiantes de ejemplo tiene $120.000 y evalúa dos propuestas: una biblioteca de intercambio de libros ($70.000) o un torneo deportivo ($90.000). Quiere beneficiar a la mayor cantidad de estudiantes: la biblioteca llegaría a 300 y el torneo a 180. Con ese criterio, ¿qué conviene?", "La biblioteca, porque beneficia a más estudiantes", "El torneo, porque cuesta más", "Ninguna, porque no alcanzan los $120.000", "El criterio es la cantidad de beneficiarios, y 300 es mayor que 180."),
    sc=[
        ("¿Qué pasos sigue una buena evaluación económica?", "Identificar el problema, listar alternativas, estimar costos y beneficios, nombrar el costo de oportunidad, separar valores y decidir", "Son los pasos de comparación con criterios explícitos."),
        ("¿Por qué personas con los mismos datos pueden elegir distinto?", "Porque priorizan valores distintos", "La parte normativa de una decisión depende de lo que cada persona valora."),
        ("Nombra un límite que debe declarar un análisis económico.", "Datos incompletos o supuestos que podrían no cumplirse", "Declararlo evita presentar una opinión como respuesta única."),
    ],
    op=("Elige uno de estos casos de ejemplo y evalúa las alternativas. Caso 1: una familia tiene $100.000 y puede (a) pagar un curso de computación de $80.000 para el hijo o (b) arreglar el techo, que cuesta $90.000. "
        "Caso 2: un centro de salud de ejemplo tiene recursos para (a) contratar una nutricionista o (b) comprar camillas nuevas. Define al menos dos criterios, compara las alternativas, nombra el costo de oportunidad de tu elección, "
        "separa lo que es dato de lo que es valor y declara un límite de tu análisis.",
        "Caso 1. Criterios: urgencia y efecto futuro. El techo es urgente porque protege la vivienda; el curso mejora oportunidades. Si elige el techo, pierde el curso. Dato: ambos suman 170.000, más de lo disponible. Valor: priorizar seguridad. Límite: no sé el estado real del techo.",
        ["define al menos dos criterios", "compara con ellos las dos alternativas", "nombra el costo de oportunidad", "distingue datos y valores", "declara un límite"],
        ["texto de cinco partes con criterios, comparación, costo de oportunidad, valores y límite"],
        ["usar un solo criterio", "no nombrar lo que se pierde", "presentar un valor como si fuera un dato"],
        "Pregunta: «¿qué dejarías de lograr con tu elección?». Si no lo nombra, pídele revisar el costo de oportunidad."),
    reinforce="Elige una decisión pendiente de tu casa o liceo y escribe dos alternativas, dos criterios y cuál elegirías con su costo de oportunidad.",
    extend="Compara por escrito cómo evaluaría un mismo proyecto una persona que prioriza la eficiencia y otra que prioriza la equidad, sin decir cuál es la correcta.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 6 (casos de ejemplo, ficticios). Caso 1: un municipio cobra una multa de $5.000 por dejar escombros en la vía pública; llevarlos a un punto autorizado cuesta $4.000. "
     "Caso 2: una pastelería regala un café a quien traiga su propia taza. "
     "Caso 3: un liceo da puntos para la salida de fin de año a los cursos que reciclen más botellas, y se descubre que algunos cursos traen botellas desde sus casas, de otros hogares, sin reciclar nada nuevo.")
build(
    O2, 1, F,
    use="Aprenderé cómo los economistas estudian los incentivos: qué son, cómo hacen cambiar las decisiones de los agentes y por qué a veces generan efectos no buscados.",
    prior=["Sé qué es la escasez y el costo de oportunidad.", "Sé que las personas responden a incentivos.", "Sé restar cantidades de dinero."],
    explain=[
        "Un incentivo es un estímulo que hace más o menos atractiva una acción al cambiar sus costos o beneficios. Los economistas parten de la hipótesis de que los agentes responden a incentivos: si una acción se vuelve más cara o menos beneficiosa, tienden a hacerla menos; si se vuelve más barata o beneficiosa, tienden a hacerla más. Esa hipótesis se contrasta con datos.",
        "Hay incentivos positivos, que premian o abaratan una acción (descuentos, bonos, puntos), e incentivos negativos, que la penalizan o encarecen (multas, impuestos, tarifas). Pueden ser monetarios o no monetarios, como el reconocimiento, la comodidad o el tiempo ahorrado. Los incentivos son una herramienta de las empresas y del Estado para orientar conductas sin obligar directamente.",
        "Los incentivos pueden tener consecuencias no buscadas, a veces llamadas incentivos perversos: un premio mal diseñado puede llevar a cumplir la meta sin cumplir el propósito. Por eso, al estudiar un incentivo conviene preguntar qué conducta busca cambiar, a quién afecta, qué costo o beneficio cambia exactamente y qué podrían hacer los agentes para aprovecharlo sin lograr el objetivo.",
    ],
    vocab=[("incentivo positivo", "estímulo que premia o abarata una acción"), ("incentivo negativo", "estímulo que penaliza o encarece una acción"), ("incentivo perverso", "incentivo que produce un efecto contrario al buscado"), ("multa", "sanción en dinero por incumplir una norma"), ("conducta", "forma de actuar de una persona o empresa"), ("diseño de un incentivo", "forma en que se define qué se premia o penaliza")],
    worked=[
        ("Clasificar un incentivo", "Un gimnasio de ejemplo cobra $2.000 menos de mensualidad a quienes paguen antes del día 5. ¿Qué incentivo es y qué conducta busca?",
         ["El descuento abarata la acción de pagar a tiempo: es un incentivo positivo.", "La conducta que busca cambiar es el pago anticipado."],
         "Incentivo positivo; busca el pago puntual"),
        ("Detectar un efecto no buscado", "Una empresa de ejemplo paga a sus vendedores solo por la cantidad de llamadas hechas. Los vendedores empiezan a hacer llamadas muy cortas. ¿Qué pasó?",
         ["Se premió la cantidad de llamadas, no la calidad o las ventas.", "Los vendedores cumplen la meta sin cumplir el propósito: es un incentivo perverso."],
         "Un incentivo perverso: premia llamadas, no ventas"),
    ],
    mistakes=[("Creer que un incentivo es siempre un premio.", "Se olvidan multas, impuestos y tarifas.", "También hay incentivos negativos que encarecen una acción."),
              ("Suponer que todo incentivo funciona como se espera.", "Se ignora cómo los agentes pueden aprovecharlo.", "Antes de aplicarlo, pregunta cómo podrían cumplir la meta sin lograr el propósito.")],
    T=[
        ("abc", "{F} ¿Qué tipo de incentivo es la multa del Caso 1?", "Un incentivo negativo", "Un incentivo positivo", "Un incentivo no monetario", "La multa penaliza la conducta de dejar escombros."),
        ("abc", "{F} ¿Qué tipo de incentivo es el café regalado del Caso 2?", "Un incentivo positivo", "Un incentivo negativo", "Una multa", "Regalar un café premia la conducta de traer la taza."),
        ("=", "{F} Caso 1: si fuera seguro que te multan, ¿cuántos pesos menos pagas llevando los escombros al punto autorizado que pagando la multa?", "5000-4000", "Se resta el costo de cumplir al monto de la multa."),
        ("abc", "En Economía y sociedad: ¿qué es un incentivo?", "Un estímulo que cambia lo atractiva que resulta una acción", "Una obligación impuesta por ley", "Un dato estadístico", "El incentivo modifica costos o beneficios, no obliga directamente."),
        ("En Economía y sociedad: ¿qué es un incentivo perverso?", "Uno que produce un efecto contrario o distinto al buscado", "Es un incentivo mal diseñado que se cumple sin lograr el propósito."),
        ("abc", "{F} En el Caso 3, ¿por qué el premio por reciclar falla?", "Porque se premió la cantidad de botellas, no el reciclaje nuevo", "Porque el premio era demasiado pequeño", "Porque el premio se dio solo a un curso", "Los cursos cumplen la meta con botellas traídas sin reciclar nada nuevo."),
        ("{F} En el Caso 1, ¿qué conducta busca cambiar la multa y cómo afecta la decisión de quien tiene escombros?", "Que se lleven a un punto autorizado; la multa encarece dejarlos en la calle", "Al subir el costo de la conducta no deseada, se espera que menos personas la hagan."),
        ("abc", "{F} Si la multa del Caso 1 bajara a $1.000 y llevar los escombros sigue costando $4.000, ¿qué conducta resultaría más conveniente en dinero?", "Pagar la multa", "Llevar los escombros al punto autorizado", "Ninguna cuesta nada", "La multa de 1.000 es menor que el costo de 4.000, así que el incentivo se debilita."),
        ("abc", "Una comuna de ejemplo instala un cobro por bolsa de basura para que las familias generen menos residuos. Algunas familias empiezan a dejar bolsas en sitios eriazos. ¿Qué enseña esto?", "Que un incentivo puede generar conductas evasivas no buscadas", "Que los incentivos solo funcionan con castigos", "Que las familias no responden a precios", "Los agentes pueden evitar el costo sin cambiar la conducta que se quería cambiar."),
        ("{F} En el Caso 3, ¿qué debería medirse para premiar de verdad el reciclaje?", "El reciclaje adicional generado en el liceo y no la cantidad de botellas entregadas", "Hay que medir lo que realmente se busca, que es reciclaje nuevo y no botellas traídas de afuera."),
        ("abc", "{F} Un concejal dice: «Con el café gratis, la pastelería perderá plata y el incentivo es mala idea». ¿Qué evaluación es más completa?", "Hay que comparar el costo del café regalado con el ahorro y la fidelidad que genera", "Un incentivo se justifica solo si es gratis", "La pastelería no puede tomar decisiones", "El incentivo se evalúa comparando su costo con los beneficios que produce."),
        ("abc", "{F} ¿Qué tienen en común el Caso 1 y el Caso 2?", "Ambos cambian los costos o beneficios de una conducta sin obligar directamente", "Ambos son multas", "Ambos son regalos", "Ambos influyen en la decisión modificando lo que cuesta o gana el agente."),
        ("Una empresa premia con $20.000 a quien no falte en el mes. Muchos trabajadores van enfermos al trabajo. ¿Qué principio muestra esta consecuencia?", "El incentivo premia la asistencia, no la salud ni el desempeño, y produce un efecto no buscado", "El premio sirve para cumplir la meta formal, aunque dañe el propósito de fondo."),
    ],
    ctx=("abc", "Un edificio de ejemplo cobra $3.000 por cada hora de uso del salón de eventos después de las 22:00, para reducir el ruido. Una familia calcula que arrendar un salón externo cuesta $2.000 por hora. ¿Qué es probable que haga esa familia?", "Usar el salón externo, porque le resulta más barato", "Usar el salón del edificio, porque es más caro", "Pagar el cobro del edificio, porque es una obligación", "El cobro alto desplaza la conducta hacia la alternativa más barata."),
    sc=[
        ("¿Cuál es la diferencia entre un incentivo positivo y uno negativo?", "El positivo premia o abarata una acción y el negativo la penaliza o encarece", "Cambian el costo o beneficio de la acción en sentidos opuestos."),
        ("¿Qué es un incentivo perverso?", "Uno que produce un efecto distinto o contrario al que se buscaba", "Cumple la meta sin lograr el propósito."),
        ("¿Es siempre monetario un incentivo?", "No: también puede ser reconocimiento, comodidad o tiempo", "Los incentivos no monetarios también cambian las decisiones."),
    ],
    op=("Diseña un incentivo para este problema de ejemplo: en el patio de un liceo, muchos estudiantes dejan los envases en el suelo. Puedes elegir (a) un incentivo positivo, (b) uno negativo o (c) uno combinado. "
        "Escribe qué conducta buscas cambiar, el incentivo, a quién afecta, cómo podrían aprovecharlo sin lograr el objetivo y cómo lo corregirías.",
        "(a) Un punto para el curso por cada semana en que el patio quede limpio según la revisión del inspector. Afecta a todos los cursos. Podrían esconder basura; por eso se revisa también el baño y la sala.",
        ["define la conducta que se quiere cambiar", "describe un incentivo claro", "anticipa una forma de aprovecharlo sin cumplir el propósito", "propone una corrección"],
        ["texto con conducta, incentivo, riesgo y corrección"],
        ["premiar la medida equivocada", "no anticipar ninguna evasión", "proponer un incentivo que cuesta más que el beneficio"],
        "Pregunta: «¿cómo podría alguien cumplir la meta sin cumplir el propósito?». Si no lo imagina, dale el ejemplo de las botellas."),
    reinforce="Escribe dos incentivos positivos y dos negativos que existan en tu barrio o liceo.",
    extend="Busca un incentivo que haya tenido un efecto no buscado (en tu entorno o en una noticia) y explica qué debería haberse medido.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 7 (datos de ejemplo, ficticios). Panadería «Doña Rosa» decide cuántas hornadas hacer en una mañana. Cada hornada adicional tiene este costo adicional (ingredientes y energía) y este ingreso adicional por ventas: "
     "1.ª hornada: costo $20.000, ingreso $50.000. 2.ª hornada: costo $25.000, ingreso $45.000. 3.ª hornada: costo $30.000, ingreso $35.000. 4.ª hornada: costo $35.000, ingreso $30.000.")
build(
    O2, 2, F,
    use="Aprenderé qué son el costo marginal y el beneficio marginal y cómo los agentes deciden cuánto hacer comparando lo adicional, no el total.",
    prior=["Sé decidir al margen de manera intuitiva.", "Sé sumar y restar cantidades de dinero.", "Sé leer una tabla con varias filas."],
    explain=[
        "El costo marginal es lo que cuesta producir o consumir una unidad adicional. El beneficio marginal es lo que se gana con esa unidad adicional. «Marginal» siempre se refiere al cambio que produce una unidad más, y no al total acumulado. Si el beneficio marginal es mayor que el costo marginal, esa unidad aporta ganancia neta; si es menor, la unidad deja pérdida.",
        "La regla de decisión de los economistas es seguir aumentando la cantidad mientras el beneficio marginal sea mayor o igual que el costo marginal, y detenerse cuando el costo marginal pasa a superar al beneficio marginal. En una tabla se revisa fila por fila: se calcula el beneficio neto de cada unidad adicional (beneficio marginal menos costo marginal) y se hace mientras sea positivo.",
        "Esta regla no vale solo para empresas. Una persona que estudia decide cuántas horas más dedicar a una materia: cada hora adicional rinde menos que la anterior, mientras su costo de oportunidad se mantiene o crece. Pero ojo con un error frecuente: los costos ya pagados que no se pueden recuperar no deben contarse en la decisión sobre la próxima unidad.",
    ],
    vocab=[("costo marginal", "costo de producir o consumir una unidad adicional"), ("beneficio marginal", "beneficio de una unidad adicional"), ("beneficio neto marginal", "beneficio marginal menos costo marginal"), ("unidad adicional", "una más sobre lo que ya se tiene"), ("rendimiento decreciente", "cada unidad adicional aporta menos que la anterior"), ("costo hundido", "gasto ya hecho que no se puede recuperar")],
    worked=[
        ("Decidir hasta dónde producir", "Un kiosco de ejemplo evalúa vender una cuarta caja de galletas: su costo marginal es $6.000 y su beneficio marginal es $5.000. ¿Le conviene?",
         ["Compara beneficio y costo marginal: 5.000 contra 6.000.", "El beneficio marginal es menor, así que la caja deja una pérdida de 1.000."],
         "No le conviene vender esa caja adicional"),
        ("Usar una tabla", "Un taller de costura de ejemplo: 1.ª tanda de poleras, costo marginal $10.000 y beneficio $18.000; 2.ª tanda, costo $14.000 y beneficio $16.000; 3.ª tanda, costo $18.000 y beneficio $15.000. ¿Cuántas tandas conviene?",
         ["1.ª tanda: 18.000 menos 10.000 dejan 8.000 de ganancia. 2.ª: 16.000 menos 14.000 dejan 2.000.", "3.ª tanda: 15.000 menos 18.000 dejan una pérdida de 3.000, así que se detiene en la segunda."],
         "Dos tandas"),
    ],
    mistakes=[("Comparar el costo total con el beneficio total y no lo adicional.", "Se pierde de vista que lo relevante es cada unidad extra.", "Calcula el beneficio neto de cada unidad adicional."),
              ("Contar un gasto ya pagado y no recuperable al decidir la siguiente unidad.", "Se confunde un costo hundido con un costo marginal.", "Solo cuentan los costos y beneficios que cambian con la decisión.")],
    T=[
        ("abc", "{F} ¿Cuál es el costo marginal de la 2.ª hornada?", "$25.000", "$45.000", "$20.000", "La tabla indica $25.000 como costo adicional de la segunda hornada."),
        ("=", "{F} ¿Cuánto es el beneficio neto (en pesos) de la 1.ª hornada?", "50000-20000", "Se resta el costo marginal al beneficio marginal."),
        ("abc", "En Economía y sociedad: ¿qué es el costo marginal?", "El costo de producir una unidad adicional", "El costo total de toda la producción", "El costo de la primera unidad solamente", "«Marginal» se refiere al cambio por una unidad más."),
        ("=", "{F} ¿Cuánto es el beneficio neto (en pesos) de la 2.ª hornada?", "45000-25000", "Se resta el costo marginal de la 2.ª hornada a su ingreso."),
        ("abc", "{F} ¿Cuál es el beneficio neto de la 3.ª hornada?", "$5.000", "$35.000", "-$5.000", "Son 35.000 de ingreso menos 30.000 de costo."),
        ("=", "{F} ¿Cuántos pesos se pierde con la 4.ª hornada? Responde con el número de la diferencia entre su costo y su ingreso.", "35000-30000", "El costo supera al ingreso en esa diferencia."),
        ("{F} ¿Cuántas hornadas conviene hacer?", "Tres", "Hasta la 3.ª el beneficio marginal supera al costo marginal, y en la 4.ª no."),
        ("abc", "{F} ¿Por qué no conviene hacer la 4.ª hornada?", "Porque su costo marginal supera a su beneficio marginal", "Porque es la última de la tabla", "Porque su ingreso es menor que el de la 1.ª hornada", "El costo de 35.000 es mayor que el ingreso de 30.000."),
        ("=", "{F} ¿Cuántos pesos de ganancia total dejan las tres primeras hornadas juntas?", "30000+20000+5000", "Se suman los beneficios netos de las tres primeras hornadas."),
        ("abc", "{F} La panadera dice: «Ya pagué $90.000 en el horno nuevo, así que debo hacer la 4.ª hornada para recuperarlo». ¿Qué falla en este razonamiento?", "El gasto del horno ya está pagado y no cambia con la 4.ª hornada, que deja pérdida", "El horno debería haberse pagado antes", "La 4.ª hornada deja ganancia", "Un costo hundido no debe contarse al decidir la próxima unidad."),
        ("{F} Los precios de los ingredientes suben y la 3.ª hornada pasa a costar $40.000, con el mismo ingreso. ¿Cuántas hornadas conviene hacer ahora?", "Dos", "El costo de la 3.ª supera su ingreso de 35.000, así que se detiene en la 2.ª."),
        ("abc", "Un estudiante dice que, como estudiar le ha costado mucho esfuerzo, debe seguir estudiando toda la noche aunque ya no aprenda nada. ¿Qué principio ignora?", "Que solo importa el beneficio y costo de la siguiente hora", "Que el estudio no tiene beneficios", "Que el esfuerzo pasado debe borrarse", "Debe comparar lo que gana con una hora más con lo que cuesta, y no con lo ya gastado."),
        ("abc", "{F} Si la panadera pudiera vender la 4.ª hornada a un mayorista que paga $45.000 en total (con el mismo costo de $35.000), ¿qué conviene?", "Hacerla, porque el beneficio marginal sube a 45.000 y supera al costo", "No hacerla, porque la tabla no la incluye", "No hacerla, porque el costo es alto", "Al cambiar el beneficio marginal, la decisión también cambia."),
    ],
    ctx=("abc", "Un joven de ejemplo reparte volantes. Cada hora adicional le rinde menos: la 1.ª hora le reporta $6.000 de pago, la 2.ª $5.000, la 3.ª $3.000 y la 4.ª $1.500. Cada hora adicional le cuesta, en tiempo que podría usar para estudiar, el equivalente a $2.500. ¿Cuántas horas conviene trabajar?", "Tres horas", "Dos horas", "Cuatro horas", "En la 3.ª, 3.000 supera 2.500; en la 4.ª, 1.500 es menor que 2.500."),
    sc=[
        ("En Economía y sociedad: ¿qué es el beneficio marginal?", "El beneficio de una unidad adicional", "Se refiere al cambio por una unidad más."),
        ("¿Cuándo conviene seguir aumentando la cantidad?", "Mientras el beneficio marginal sea mayor o igual que el costo marginal", "La unidad adicional aporta o no resta ganancia."),
        ("¿Qué es un costo hundido y por qué no se cuenta?", "Un gasto ya pagado que no se recupera, y no cambia con la decisión siguiente", "Solo cuentan los costos y beneficios que cambian con la decisión."),
    ],
    op=("Resuelve uno de estos casos de ejemplo. Caso 1: un puesto de limonada vende por vasos y por cada vaso adicional tiene estos datos: 1.er vaso, costo $200 y beneficio $800; 2.º, costo $300 y beneficio $700; 3.º, costo $400 y beneficio $500; 4.º, costo $500 y beneficio $400; 5.º, costo $600 y beneficio $300. "
        "Caso 2: tú decides cuántas horas estudiar para una prueba, con rendimiento decreciente. Para el caso 1, calcula el beneficio neto de cada vaso, di cuántos conviene y por qué. Para el caso 2, inventa datos coherentes para cuatro horas y aplica la misma regla.",
        "Caso 1. Beneficios netos: 600, 400, 100, -100 y -300. Conviene 3 vasos, porque el 4.º ya deja pérdida.",
        ["calcula el beneficio neto de cada unidad", "aplica la regla de detenerse cuando el costo supera al beneficio", "justifica con la comparación marginal"],
        ["tabla o lista con beneficios netos y una conclusión"],
        ["comparar totales y no marginales", "olvidar descartar las unidades con pérdida", "incluir un costo hundido en la decisión"],
        "Pregunta: «¿en qué unidad el costo pasa a ser mayor que el beneficio?». Si no la ubica, pídele que escriba la resta de cada fila."),
    reinforce="Con la tabla de «Doña Rosa», calcula la ganancia total si hiciera dos hornadas y la ganancia total si hiciera cuatro, y compara.",
    extend="Explica por qué una persona puede decidir no comerse un último trozo de torta aunque la torta esté rica: ¿qué cambia en el beneficio marginal?",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 8 (casos de ejemplo, ficticios). Caso A (costo para terceros): una curtiembre de ejemplo produce un lote de cuero. Costo privado: $60.000. Beneficio privado (lo que gana por venderlo): $100.000. "
     "Además, sus residuos dañan el río y limpiar el daño costaría $70.000 a los vecinos. "
     "Caso B (beneficio para terceros): un vecino planta un árbol en la acera. Su costo es $30.000 y su beneficio privado (sombra en su casa) es $10.000; los vecinos del pasaje obtienen en conjunto un beneficio de $40.000 por la sombra y la belleza.")
build(
    O2, 3, F,
    use="Aprenderé a distinguir costos y beneficios privados de los sociales, y a usar esa diferencia para entender por qué una decisión conveniente para un agente puede no serlo para la sociedad.",
    prior=["Sé calcular costos y beneficios marginales.", "Sé qué es un incentivo.", "Sé sumar y restar cantidades de dinero."],
    explain=[
        "Un costo privado es el que paga quien toma la decisión, y un beneficio privado es el que recibe él mismo. Pero una decisión puede afectar a otras personas que no participaron en ella: a esos efectos se les llama externalidades. Una externalidad negativa impone un costo a terceros, y una externalidad positiva les da un beneficio.",
        "Para evaluar una decisión desde el punto de vista de toda la sociedad se usan el costo social y el beneficio social. El costo social es el costo privado más el costo que se traspasa a terceros. El beneficio social es el beneficio privado más el beneficio que reciben terceros. Una actividad conviene a la sociedad cuando su beneficio social supera a su costo social.",
        "La diferencia entre lo privado y lo social explica por qué un mercado, por sí solo, puede producir demasiado de lo que genera daños a terceros y demasiado poco de lo que les da beneficios. Reconocerlo no resuelve qué política aplicar: eso es una discusión posterior, con posturas distintas sobre impuestos, normas o subsidios.",
    ],
    vocab=[("costo privado", "costo que paga quien decide"), ("beneficio privado", "beneficio que recibe quien decide"), ("externalidad", "efecto de una decisión sobre terceros que no participaron"), ("costo social", "costo privado más el costo para terceros"), ("beneficio social", "beneficio privado más el beneficio para terceros"), ("tercero", "persona afectada que no participó de la decisión")],
    worked=[
        ("Calcular el costo social", "Una fábrica de ejemplo produce un lote con costo privado de $40.000 y causa un daño a vecinos que cuesta $15.000. ¿Cuál es el costo social?",
         ["El costo social es el costo privado más el costo para terceros.", "Suma 40.000 y 15.000."],
         "$55.000"),
        ("Comparar lo privado y lo social", "Un taller de ejemplo ganaría $50.000 con un trabajo que tiene costo privado de $30.000 y genera ruido que cuesta $35.000 a los vecinos. ¿Conviene al taller? ¿Conviene a la sociedad?",
         ["Para el taller: 50.000 menos 30.000 dejan 20.000 de ganancia, así que le conviene.", "Para la sociedad: el costo social es 30.000 más 35.000 igual a 65.000, mayor que el beneficio de 50.000, así que no conviene."],
         "Conviene al taller, pero no a la sociedad"),
    ],
    mistakes=[("Sumar el daño a terceros al beneficio y no al costo.", "Se confunde la dirección del efecto.", "El daño a terceros aumenta el costo social."),
              ("Creer que si una actividad es rentable para la empresa también lo es para la sociedad.", "Se omite lo que pagan los terceros.", "Compara siempre el beneficio social con el costo social.")],
    T=[
        ("=", "{F} Caso A: ¿cuál es el costo social del lote en pesos?", "60000+70000", "Se suma el costo privado y el costo para los vecinos."),
        ("=", "{F} Caso A: ¿cuánto gana la curtiembre en pesos, considerando solo costo y beneficio privados?", "100000-60000", "Se resta el costo privado al beneficio privado."),
        ("abc", "En Economía y sociedad: ¿qué es una externalidad?", "Un efecto de una decisión sobre terceros que no participaron", "Un impuesto que paga una empresa", "Un precio fijado por el Estado", "Las externalidades son efectos sobre terceros, positivos o negativos."),
        ("abc", "{F} Caso A: ¿cuál es la externalidad y de qué tipo?", "El daño al río que pagan los vecinos; es negativa", "El beneficio de la curtiembre; es positiva", "El costo del lote; es negativa", "El daño recae en terceros y les impone un costo."),
        ("abc", "{F} Caso B: ¿qué tipo de externalidad genera el árbol?", "Positiva, porque da un beneficio a terceros", "Negativa, porque cuesta $30.000", "Ninguna, porque el vecino lo paga", "Los vecinos reciben un beneficio sin participar en la decisión."),
        ("=", "{F} Caso B: ¿cuál es el beneficio social del árbol en pesos?", "10000+40000", "Se suman el beneficio privado y el beneficio de los vecinos."),
        ("abc", "{F} Caso A: ¿conviene el lote a la sociedad?", "No, porque el costo social supera al beneficio", "Sí, porque la curtiembre gana", "Sí, porque el daño es de otros", "El beneficio es 100.000 y el costo social es 130.000."),
        ("abc", "{F} Caso B: ¿conviene el árbol a la sociedad?", "Sí, porque el beneficio social supera al costo", "No, porque al vecino le cuesta más de lo que gana", "No, porque los vecinos no pagaron", "El beneficio social de 50.000 supera el costo de 30.000."),
        ("abc", "{F} Caso B: ¿plantaría el vecino el árbol si decide solo con su costo y beneficio privados?", "No, porque pierde 20.000 en términos privados", "Sí, porque el árbol es gratis", "Sí, porque gana 40.000", "Su beneficio privado es 10.000 y su costo es 30.000."),
        ("{F} Explica con la diferencia entre lo privado y lo social por qué la curtiembre hace el lote aunque no convenga a la sociedad.", "Porque ella no paga el daño a los vecinos, que recae en terceros", "Decide con su costo privado y no incluye el costo traspasado."),
        ("abc", "{F} Una concejala dice: «Si el árbol beneficia tanto a los vecinos, el Estado debería pagarlo». ¿Qué tipo de enunciado es?", "Normativo, porque dice lo que debería hacerse", "Positivo, porque tiene números", "Ni positivo ni normativo", "El verbo «debería» expresa un juicio sobre qué política aplicar."),
        ("abc", "{F} En el Caso A, el costo de limpiar el río baja de $70.000 a $50.000 por una nueva técnica. ¿Qué pasa con la conveniencia social del lote?", "El costo social pasa a 110.000 y supera el beneficio de 100.000, aunque por menos", "Ahora conviene a la sociedad", "Nada cambia en el costo social", "Con 60.000 más 50.000 el costo social es 110.000, todavía mayor que 100.000."),
        ("Una estudiante dice: «Si es rentable para la empresa, es bueno para el país». ¿Qué contraejemplo de esta clase muestra que no siempre es así?", "El Caso A: gana la curtiembre, pero el costo social supera al beneficio", "Una actividad rentable puede imponer costos a terceros que superen su beneficio."),
    ],
    ctx=("abc", "Una escuela de ejemplo organiza un festival con música alta. El festival le deja $200.000 de ganancia y le cuesta $80.000. Los vecinos pierden en conjunto el equivalente a $150.000 por el ruido. ¿Qué conclusión sobre el festival es correcta?", "Ganancia privada de 120.000, pero costo social mayor que el beneficio, porque 80.000 más 150.000 superan 200.000", "Conviene a la sociedad porque la escuela gana", "No tiene externalidades", "El costo social es 230.000, que supera al beneficio de 200.000."),
    sc=[
        ("En Economía y sociedad: ¿cómo se calcula el costo social?", "Costo privado más costo para terceros", "Incluye lo que paga quien decide y lo que se traspasa a otros."),
        ("¿Qué diferencia hay entre una externalidad positiva y una negativa?", "La positiva da un beneficio a terceros y la negativa les impone un costo", "Ambas afectan a quienes no participaron en la decisión."),
        ("¿Cuándo conviene una actividad a la sociedad?", "Cuando su beneficio social supera a su costo social", "Se compara el efecto total, no solo el privado."),
    ],
    op=("Elige uno de estos casos de ejemplo y calcula. Caso 1: un camión de reparto genera ganancias privadas de $90.000 por día, con un costo privado de $50.000, y el ruido y el humo producen un costo de $60.000 para los vecinos. "
        "Caso 2: una peluquería gratuita para adultos mayores la organiza un grupo de jóvenes: les cuesta $25.000, sin beneficio propio, y los adultos mayores obtienen un beneficio de $45.000. "
        "Calcula costo social y beneficio social, indica si la actividad conviene a la sociedad, y escribe una frase que distinga lo positivo (el cálculo) de lo normativo (qué debería hacer el Estado).",
        "Caso 1. Costo social: 50.000 más 60.000 igual 110.000. Beneficio: 90.000. No conviene a la sociedad. Positivo: el cálculo; normativo: «el Estado debería gravar el humo» sería un juicio sobre la política.",
        ["calcula el costo social o el beneficio social correctamente", "compara ambos y concluye", "distingue una afirmación positiva de una normativa"],
        ["cálculo con conclusión y una frase que separa lo positivo de lo normativo"],
        ["sumar el daño a terceros al beneficio", "concluir solo con el cálculo privado", "decir qué política aplicar sin presentarla como un juicio"],
        "Pregunta: «¿quién paga cada costo?». Si olvida al tercero, pídele que lo marque en el enunciado."),
    reinforce="Describe una externalidad positiva y una negativa que veas en tu barrio, y señala quiénes son los terceros en cada una.",
    extend="Explica por qué dos personas pueden estar de acuerdo con el cálculo del costo social y desacuerdan en cómo debería actuar el Estado.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 9 (experimento de ejemplo, ficticio). En un liceo de ejemplo se ofrecen dos formularios de ahorro voluntario de $2.000 al mes. Formulario 1: «Marca la casilla si quieres ahorrar $2.000 al mes.» "
     "Formulario 2: «Ahorrarás $2.000 al mes, salvo que marques la casilla para no hacerlo.» Resultados de ejemplo: con el Formulario 1 ahorran 30 de 100 estudiantes; con el Formulario 2, 80 de 100. "
     "Otros casos de ejemplo: una tienda muestra un reloj a $200.000 junto a otro de $100.000, y el segundo parece barato. Un estudiante que no necesita el dinero ahora prefiere recibir $5.000 hoy antes que $6.000 en un mes.")
build(
    O2, 4, F,
    use="Aprenderé cómo la economía del comportamiento complementa el modelo clásico: qué sesgos influyen en las decisiones reales y cómo el diseño de las opciones, o «empujón», puede mejorarlas sin prohibir nada.",
    prior=["Sé que las personas responden a incentivos.", "Sé decidir al margen con costos y beneficios.", "Sé que los modelos simplifican la realidad."],
    explain=[
        "El modelo clásico supone agentes que comparan costos y beneficios con cuidado y consistencia. La economía del comportamiento incorpora lo que muestra la psicología: las personas usan atajos mentales, se distraen y sufren sesgos, que son desviaciones sistemáticas respecto del cálculo cuidadoso. Investigadores como Daniel Kahneman y Richard Thaler contribuyeron a este enfoque, y ambos recibieron el premio Nobel de Economía.",
        "Algunos sesgos conocidos: el sesgo del presente (preferir una recompensa inmediata aunque sea menor que una mayor y futura), la aversión a las pérdidas (una pérdida duele más que lo que alegra una ganancia igual), el anclaje (el primer número que se ve influye en cuánto parece caro o barato), el encuadre (la misma información decide distinto según cómo se presente) y el sesgo de statu quo o de la opción por defecto (tendencia a dejar todo como está). También influye lo que hacen los demás: saber que la mayoría de los vecinos cumple una conducta (una norma social) empuja a imitarla.",
        "Un empujón (en inglés, nudge) es un cambio en la forma de presentar las opciones que orienta una decisión sin prohibir nada ni cambiar mucho los incentivos económicos. Cambiar la opción por defecto es un ejemplo. Los empujones plantean preguntas éticas: ¿quién decide qué es lo mejor para otros?, ¿se informa a las personas?, ¿pueden elegir otra cosa fácilmente? Hay posturas a favor y en contra, y la evidencia varía según el caso.",
    ],
    vocab=[("economía del comportamiento", "enfoque que integra la psicología al estudio de las decisiones económicas"), ("sesgo", "desviación sistemática respecto de un juicio cuidadoso"), ("sesgo del presente", "preferir lo inmediato aunque sea menor"), ("aversión a las pérdidas", "sentir una pérdida más fuerte que una ganancia igual"), ("anclaje", "influencia del primer número que se ve"), ("empujón (nudge)", "cambio en cómo se presentan las opciones sin prohibir nada")],
    worked=[
        ("Reconocer un sesgo", "Una persona de ejemplo prefiere recibir $10.000 mañana antes que $12.000 en una semana, aunque sabe que no necesita el dinero ya. ¿Qué sesgo se observa?",
         ["Prefiere lo inmediato aunque lo futuro sea mayor.", "Eso corresponde al sesgo del presente."],
         "Sesgo del presente"),
        ("Interpretar un empujón", "Una cafetería de ejemplo pone la fruta a la altura de los ojos y los dulces al fondo. Compran más fruta, y nadie tiene prohibido comprar dulces. ¿Qué es esto?",
         ["No hay prohibiciones ni cambios de precio.", "Se cambió la forma de presentar las opciones: es un empujón."],
         "Un empujón (nudge)"),
    ],
    mistakes=[("Creer que la economía del comportamiento reemplaza todo el modelo clásico.", "Se confunde complemento con sustitución.", "El enfoque agrega evidencia psicológica y mantiene ideas como los incentivos."),
              ("Pensar que un empujón es lo mismo que una prohibición.", "Se ignora que las personas pueden elegir otra cosa.", "El empujón orienta sin prohibir y mantiene la libertad de elección.")],
    T=[
        ("abc", "{F} ¿Qué cambió entre el Formulario 1 y el Formulario 2?", "La opción por defecto", "El monto ahorrado", "La edad de los estudiantes", "El monto era $2.000 en ambos, y solo cambió quién debe marcar la casilla."),
        ("=", "{F} ¿Cuántos estudiantes más (de cada 100) ahorran con el Formulario 2 que con el Formulario 1?", "80-30", "Se restan los ahorradores de un formulario a los del otro."),
        ("abc", "En Economía y sociedad: ¿qué es un sesgo?", "Una desviación sistemática respecto de un juicio cuidadoso", "Un error de cálculo al azar", "Un impuesto sobre el ahorro", "Los sesgos son desviaciones que se repiten de manera predecible."),
        ("abc", "{F} ¿Qué sesgo explica la diferencia en los resultados de los dos formularios?", "El sesgo de la opción por defecto o de statu quo", "El sesgo del presente", "El anclaje con un número alto", "Muchos dejan la opción que viene marcada y no hacen el esfuerzo de cambiarla."),
        ("abc", "{F} ¿Qué sesgo ilustra el reloj de $200.000 junto al de $100.000?", "El anclaje", "La aversión a las pérdidas", "El sesgo del presente", "El primer precio alto hace que el segundo parezca barato."),
        ("ab", "{F} El estudiante que prefiere $5.000 hoy antes que $6.000 en un mes, ¿qué sesgo muestra?", "El sesgo del presente", "El anclaje", "Prefiere lo inmediato aunque lo futuro sea mayor."),
        ("{F} ¿Por qué el Formulario 2 es un empujón y no una prohibición?", "Porque nadie está obligado a ahorrar: pueden marcar la casilla para no hacerlo", "Se mantiene la libertad de elección y solo cambia la opción por defecto."),
        ("abc", "Una estudiante dice que perder una entrada de $5.000 que ya compró le duele mucho más que lo que le alegraría ganar una entrada de $5.000. ¿Qué sesgo describe?", "La aversión a las pérdidas", "El anclaje", "El sesgo de statu quo", "Siente la pérdida más intensamente que una ganancia igual."),
        ("abc", "Dos locales cobran lo mismo en total. El local A marca $10.000 y avisa «recargo de $1.000 si paga con tarjeta»; el local B marca $11.000 y avisa «descuento de $1.000 si paga en efectivo». Más clientes se molestan con el local A. ¿Qué sesgo hay?", "El encuadre", "El anclaje", "El sesgo del presente", "La misma información decide distinto según cómo se presenta."),
        ("{F} El modelo clásico predeciría que ambos formularios dan el mismo resultado si el beneficio del ahorro es el mismo. ¿Qué muestran los datos y qué corrección aporta la economía del comportamiento?", "Muestran resultados muy distintos; las personas no solo calculan, también son influidas por cómo se presenta la opción", "La forma de presentar la opción afecta la decisión, algo que el modelo clásico no preveía."),
        ("abc", "{F} Un crítico dice: «Poner el ahorro como opción por defecto no respeta la autonomía de los estudiantes». ¿Qué respuesta usa el argumento contrario?", "Cualquiera puede desmarcar la casilla, así que la libertad de elección se mantiene", "Ahorrar es obligatorio por ley, así que no hay elección", "Como el ahorro siempre es bueno, no importa cómo se presente", "Los defensores de los empujones destacan que se puede elegir otra cosa fácilmente."),
        ("abc", "{F} ¿Qué dato adicional ayudaría a evaluar si el Formulario 2 realmente beneficia a los estudiantes?", "Cuántos desmarcaron después y si el ahorro les hizo falta ese mes", "El número de formularios impresos por el liceo", "El promedio de notas del curso", "Hay que revisar si el efecto es bueno para quienes ahorran y no solo si aumenta el ahorro."),
        ("Un compañero dice: «Los sesgos prueban que las personas son irracionales y que el modelo clásico no sirve». ¿Qué matiz harías?", "Los sesgos corrigen y complementan el modelo; no lo descartan por completo", "El enfoque agrega psicología y mantiene ideas como incentivos y costo de oportunidad."),
    ],
    ctx=("abc", "Una empresa de ejemplo inscribe automáticamente a sus trabajadores en un plan de ahorro, y pueden salir cuando quieran con un solo trámite. Casi todos permanecen. ¿Cuál es una pregunta ética pertinente sobre este empujón?", "¿Se informó claramente a los trabajadores y pueden salir fácilmente?", "¿Cuánto dinero ganó la empresa el año pasado?", "¿Por qué ningún trabajador debería ahorrar?", "La evaluación ética pide transparencia y facilidad para elegir otra cosa."),
    sc=[
        ("En Economía y sociedad: ¿qué es un empujón (nudge)?", "Un cambio en cómo se presentan las opciones que orienta sin prohibir", "Mantiene la libertad de elegir otra cosa."),
        ("Nombra dos sesgos estudiados en la clase.", "Sesgo del presente y aversión a las pérdidas (también anclaje, encuadre y statu quo)", "Son desviaciones sistemáticas de las decisiones reales."),
        ("¿La economía del comportamiento reemplaza al modelo clásico?", "No: lo complementa con evidencia psicológica", "Sigue usando ideas como incentivos y costo de oportunidad."),
    ],
    op=("Analiza este caso de ejemplo: el municipio de Lomas del Sur quiere que más hogares separen el reciclaje. Propone tres medidas: (1) enviar a cada hogar un mensaje que diga «el 80% de tus vecinos ya separa», dato de ejemplo; (2) entregar contenedores de colores en la puerta de cada casa; (3) cobrar $2.000 a quienes no separen. "
        "Clasifica cada medida (empujón o incentivo económico), nombra el sesgo o la influencia en que se apoya (si hay alguna), escribe un argumento a favor y uno en contra de cada una.",
        "(1) Empujón: apela a lo que hacen los demás (norma social). A favor: es barato y sin prohibir. En contra: puede ser engañoso si el dato no fuera real. (2) Empujón: facilita la acción. (3) Incentivo negativo: cobro.",
        ["clasifica correctamente las tres medidas", "relaciona al menos una con un sesgo", "da un argumento a favor y uno en contra por medida"],
        ["tabla de tres filas con clasificación, sesgo y dos argumentos"],
        ["confundir empujón con multa", "dar solo argumentos a favor", "tomar partido sin argumentos"],
        "Pregunta: «¿esta medida prohíbe algo o cambia el precio?». Si cambia el precio, es un incentivo económico."),
    reinforce="Escribe un ejemplo de tu vida de anclaje y otro de opción por defecto (por ejemplo, ajustes de un teléfono).",
    extend="Compara las razones de quienes defienden y quienes critican los empujones, sin decidir cuál postura es la correcta.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 10 (caso de ejemplo, ficticio). Una empresa de agua de ejemplo quiere reducir el consumo de agua de los hogares en verano. Tres opciones, con resultados estimados de ejemplo: "
     "Opción 1, subir el precio del metro cúbico: baja el consumo un 8%, pero pesa más en el presupuesto de los hogares de menores ingresos. "
     "Opción 2, enviar a cada hogar una carta que compara su consumo con el de sus vecinos: baja el consumo un 4%, con costo bajo y sin cambiar el precio. "
     "Opción 3, prohibir el riego en ciertas horas: baja el consumo un 6%, pero exige fiscalizar y multar.")
build(
    O2, 5, F,
    use="Aprenderé a evaluar críticamente cómo los economistas estudian las decisiones: comparar enfoques (incentivos, costos marginales y sociales, comportamiento), reconocer sus límites y justificar una elección.",
    prior=["Sé qué son incentivos y costos marginales.", "Distingo costos privados y sociales.", "Conozco algunos sesgos y qué es un empujón."],
    explain=[
        "Los economistas disponen de varias herramientas para estudiar decisiones: los incentivos, que cambian costos y beneficios; el análisis marginal, que compara lo adicional; la distinción entre costo privado y social, que incorpora a terceros; y la economía del comportamiento, que incorpora sesgos y el diseño de las opciones. Ninguna herramienta es perfecta, y cada una responde mejor a ciertas preguntas.",
        "Analizar críticamente significa preguntar de cada enfoque qué supone, qué evidencia tiene, qué deja afuera y a quién favorece o perjudica. Por ejemplo, un incentivo de precio es efectivo, pero puede ser regresivo, es decir, pesar más en quienes tienen menos ingresos; un empujón es barato y respeta la libertad de elección, pero su efecto puede ser pequeño o no repetirse en otros contextos.",
        "Al evaluar una política conviene usar criterios explícitos, como la efectividad (cuánto cambia la conducta), el costo, la equidad (a quién afecta más), la libertad de elección y la facilidad de aplicarla. Los datos permiten comparar efectividad y costo, pero priorizar la equidad o la libertad es una decisión de valores. Una conclusión sólida lo declara y muestra qué evidencia falta.",
    ],
    vocab=[("efectividad", "cuánto logra cambiar la conducta buscada"), ("regresivo", "que pesa más en quienes tienen menos ingresos"), ("equidad", "trato justo según las necesidades y circunstancias"), ("fiscalizar", "controlar que se cumpla una norma"), ("criterio de evaluación", "característica con la que se compara una opción"), ("replicabilidad", "posibilidad de repetir un resultado en otro contexto")],
    worked=[
        ("Comparar con un criterio", "Dos programas de ejemplo para reducir el uso del auto: el A baja el uso en 10% y cuesta $5.000.000, el B lo baja en 6% y cuesta $1.000.000. ¿Cuál es más efectivo y cuál más barato?",
         ["Efectividad: A baja 10%, B baja 6%, así que A es más efectivo.", "Costo: B cuesta menos."],
         "A es más efectivo; B es más barato"),
        ("Reconocer un límite", "Un estudio de ejemplo hecho en un solo barrio muestra que una carta comparativa redujo el consumo de agua. ¿Qué límite tiene su conclusión?",
         ["El resultado se obtuvo en un solo barrio.", "No se sabe si se repite en otros contextos."],
         "Replicabilidad: puede no repetirse en otros barrios"),
    ],
    mistakes=[("Elegir la opción más efectiva sin mirar a quiénes afecta más.", "Se ignora la equidad.", "Compara varios criterios y declara cuál priorizas."),
              ("Creer que un enfoque, como el de los empujones o el de los incentivos, es siempre superior.", "Se generaliza desde algunos casos.", "Cada enfoque responde mejor a ciertas preguntas y tiene límites.")],
    T=[
        ("abc", "{F} ¿Qué opción es la más efectiva para reducir el consumo?", "La Opción 1, que baja un 8%", "La Opción 2, que baja un 4%", "La Opción 3, que baja un 6%", "El mayor porcentaje de reducción corresponde a la subida de precio."),
        ("=", "{F} ¿Cuántos puntos porcentuales más reduce la Opción 1 que la Opción 2? (Es la diferencia entre los dos porcentajes.)", "8-4", "Se restan los porcentajes de reducción."),
        ("abc", "{F} ¿Qué opción es un empujón?", "La Opción 2, la carta comparativa", "La Opción 1, la subida de precio", "La Opción 3, la prohibición", "Cambia la forma de presentar información sin prohibir ni subir el precio."),
        ("abc", "En Economía y sociedad: ¿qué significa que un incentivo de precio sea regresivo?", "Que pesa más en quienes tienen menos ingresos", "Que reduce los precios", "Que solo afecta a las empresas", "Regresivo se refiere al peso relativo sobre el presupuesto de cada hogar."),
        ("abc", "{F} ¿Qué opción exige más fiscalización?", "La Opción 3", "La Opción 2", "La Opción 1", "Prohibir el riego requiere controlar y multar a quienes incumplan."),
        ("abc", "{F} ¿Qué opción tiene un costo bajo y no cambia el precio?", "La Opción 2", "La Opción 1", "La Opción 3", "La carta comparativa es barata y mantiene el precio igual."),
        ("{F} Si el criterio principal es la efectividad, ¿qué opción elegirías y qué problema podría tener?", "La Opción 1; puede pesar más en los hogares de menores ingresos", "Mejora la efectividad pero tiene un costo en equidad."),
        ("{F} Si el criterio principal es la libertad de elección, ¿qué opción tiene menos restricciones?", "La Opción 2, porque no prohíbe ni cambia el precio", "Es una información que cada hogar puede ignorar, a diferencia de la prohibición."),
        ("abc", "{F} Un asesor dice: «La opción comparativa es la mejor porque cuesta poco». ¿Qué objeción es válida?", "Reduce solo el 4% y sus efectos pueden no repetirse en otros barrios", "Costar poco no importa en una evaluación", "No tiene ninguna objeción", "Un costo bajo no basta si la efectividad es limitada y hay dudas de replicabilidad."),
        ("{F} Alguien propone combinar la Opción 1 y la Opción 2. ¿Qué ventaja y qué riesgo tendría?", "Podría sumar efectos, pero mantiene el peso del precio en hogares de menores ingresos", "Combinar herramientas puede aumentar la efectividad, aunque no resuelve por sí solo el problema de equidad."),
        ("abc", "{F} Si un hogar de bajos ingresos y otro de altos ingresos pagan el mismo aumento de precio, ¿qué hogar siente un efecto relativo mayor en su presupuesto?", "El de bajos ingresos, porque el aumento es una parte mayor de su ingreso", "El de altos ingresos", "Ninguno de los dos siente el aumento", "Un mismo monto representa mayor proporción cuando el ingreso es menor."),
        ("abc", "{F} ¿Qué parte de la decisión entre las tres opciones depende de valores y no solo de datos?", "Cuánto priorizar la equidad o la libertad frente a la efectividad", "Calcular los porcentajes de reducción", "Leer los resultados estimados", "Los datos comparan efectividad y costo, pero priorizar la equidad o la libertad es un juicio."),
        ("¿Por qué una conclusión sólida sobre estas opciones debe declarar qué evidencia falta?", "Porque los resultados son estimaciones y podrían no cumplirse en otros contextos", "Reconocer los límites evita presentar como cierto lo que es incierto."),
    ],
    ctx=("abc", "Un liceo de ejemplo quiere que los estudiantes lleguen a tiempo. Prueba un descuento de $1.000 en el almuerzo para quien llegue puntual (en un curso) y un mensaje que dice «tu curso es el que más llega puntual» (en otro). El primero mejora la puntualidad en 10 puntos porcentuales y el segundo en 6, en un mes. ¿Qué conclusión es más prudente?", "Que el descuento fue más efectivo en estos dos cursos, pero falta saber el costo y si se repite", "Que los mensajes solo funcionan en liceos", "Que los dos resultados son idénticos", "Dos cursos y un mes no bastan para generalizar, y el descuento tiene un costo."),
    sc=[
        ("¿Qué preguntas se hacen al analizar críticamente un enfoque?", "Qué supone, qué evidencia tiene, qué deja afuera y a quién afecta", "Evalúa los límites del enfoque y a quiénes afecta."),
        ("En Economía y sociedad: ¿qué es la equidad?", "Un trato justo según las necesidades y circunstancias", "Es un criterio de valores usado para evaluar políticas."),
        ("¿Por qué un empujón puede no ser suficiente?", "Porque su efecto puede ser pequeño o no repetirse en otros contextos", "Su baja intensidad y su replicabilidad limitada son dos límites."),
    ],
    op=("Elige uno de estos problemas de ejemplo y evalúa dos alternativas. Problema 1: reducir los atrasos a primera hora en un liceo. Problema 2: aumentar el uso de bicicletas en un barrio. "
        "Para cada alternativa, define al menos tres criterios (por ejemplo, efectividad, costo, equidad), escribe un dato inventado y rotulado «de ejemplo» para cada criterio, "
        "elige una opción, declara qué valor priorizaste y señala un límite de tu análisis.",
        "Problema 2. Alternativa A: ciclovía (efectividad alta de ejemplo, costo alto). Alternativa B: campaña de información (efectividad baja de ejemplo, costo bajo). Elijo la A priorizando la seguridad. Límite: dato de ejemplo.",
        ["define al menos tres criterios", "usa datos rotulados como de ejemplo", "justifica la elección con un valor", "declara un límite"],
        ["tabla comparativa y párrafo de conclusión"],
        ["usar un solo criterio", "presentar los datos inventados como reales", "no declarar ningún límite"],
        "Pregunta: «¿qué valor te llevó a esa elección?». Si dice que los datos, pídele que busque el valor detrás."),
    reinforce="Elige una política que hayas visto en tu comuna y escribe qué enfoque usa (incentivo, regla o empujón) y un límite.",
    extend="Escribe un diálogo breve entre dos personas que aceptan los mismos datos de la Ficha 10 pero eligen opciones distintas por sus valores.",
)

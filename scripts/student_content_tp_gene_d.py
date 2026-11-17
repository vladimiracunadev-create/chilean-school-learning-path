"""Objetivos genéricos TP 3.º y 4.º medio, módulo D: OAG-10 (emprender y gestión financiera básica), OAG-11 (prevención de riesgos y enfermedades ocupacionales, elementos de protección personal) y OAG-12 (decisiones financieras: ahorro previsional, seguros, endeudamiento e inversión).
Todo en papel: empresas, personas, montos, tasas y cuotas inventados y rotulados «de ejemplo». OAG-11 es solo conceptual (sin procedimientos operativos) y OAG-12 no es asesoría financiera ni recomienda productos o instituciones."""
from __future__ import annotations

from tp_gene_common import build

G10 = "TP-GENE-3y4-OAG-10"
G11 = "TP-GENE-3y4-OAG-11"
G12 = "TP-GENE-3y4-OAG-12"
LIM = " Este cuaderno trabaja en papel, con casos de ejemplo: no reemplaza a tu profesor, a tu jefatura ni a la norma vigente."
AVISO = " Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente (por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar."
FIN = " Este cuaderno explica conceptos con cifras de ejemplo: no es asesoría financiera ni recomienda productos o instituciones. Antes de decidir, infórmate en fuentes oficiales y conversa con una persona adulta de confianza."

# ============================================================ OAG-10, clase 1
F = ("Ficha 37 (idea de negocio de ejemplo; personas inventadas). Valentina y Diego, estudiantes de un liceo técnico ficticio, notan que en 3 oficinas cercanas, de 20 trabajadores cada una, no hay dónde comprar colaciones saludables a la hora de almuerzo. "
     "Idea: vender colaciones saludables por encargo, a $2.500 cada una (precio de ejemplo). Un kiosco cercano vende colaciones a $3.000, con poca variedad. Antes de invertir preguntarán a una muestra de 15 trabajadores si comprarían: 9 dijeron que sí.")
build(
    G10, 1, F,
    use="Aprenderé qué es emprender, cómo detectar una necesidad, definir clientes y propuesta de valor, y validar una idea antes de invertir.",
    prior=["Sé calcular cuántos por cada 100.", "Sé multiplicar y restar.", "Conozco qué es un cliente y un precio."],
    explain=[
        "Emprender es detectar una necesidad o una oportunidad y crear una solución, un producto o un servicio, asumiendo ciertos riesgos. Puede ser un proyecto propio o una iniciativa dentro de un lugar de trabajo, como una mejora que ahorra tiempo o dinero. Los elementos básicos de una idea son la necesidad que resuelve, los clientes a quienes se dirige, la propuesta de valor (lo que ofrece y en qué se diferencia de la competencia) y el precio.",
        "Antes de invertir dinero y tiempo, se valida la idea: se pregunta a posibles clientes, se prueba a pequeña escala y se analiza la competencia. Así se reduce el riesgo de equivocarse. Un emprendedor necesita responsabilidad, perseverancia, capacidad de aprender de los errores y respeto por las normas. Para vender, según el rubro, existen normas y permisos que se deben cumplir; se consultan en las instituciones competentes, según la norma vigente.",
        "Los datos de esta ficha son de ejemplo. Este cuaderno no te habilita para iniciar un negocio ni reemplaza la asesoría de instituciones de apoyo al emprendimiento." + LIM,
    ],
    vocab=[("emprender", "detectar una necesidad u oportunidad y crear una solución asumiendo riesgos"), ("necesidad", "problema o carencia que una idea busca resolver"), ("cliente", "persona o empresa que compra el producto o servicio"), ("propuesta de valor", "lo que ofrece una idea y en qué se diferencia de la competencia"), ("validar", "comprobar con posibles clientes que la idea responde a una necesidad real"), ("competencia", "otros que ofrecen algo parecido a los mismos clientes")],
    worked=[
        ("Identificar la necesidad", "Un liceo de ejemplo no tiene dónde dejar las bicicletas de los estudiantes. Alguien propone un estacionamiento supervisado. ¿Cuál es la necesidad?", ["Es el problema que se quiere resolver.", "Falta de un lugar seguro para las bicicletas."], "Falta de un lugar seguro para dejar las bicicletas"),
        ("Calcular clientes potenciales", "En un barrio de ejemplo hay 4 locales con 15 trabajadores cada uno. ¿Cuántos clientes potenciales hay?", ["Se multiplican los locales por los trabajadores.", "4 × 15 = 60."], "60 clientes potenciales"),
    ],
    mistakes=[("Invertir dinero porque «a mí me encantaría comprar eso».", "El gusto personal no representa a los clientes y se puede perder lo invertido.", "Pregunta a posibles clientes y prueba a pequeña escala."),
              ("Decir «no tengo competencia» porque no conoces a nadie que venda lo mismo.", "Siempre hay alternativas que los clientes usan hoy para resolver su necesidad.", "Investiga qué hacen hoy los clientes y cuánto pagan.")],
    T=[
        ("abc", "En emprendimiento: ¿qué es emprender?", "Detectar una necesidad u oportunidad y crear una solución asumiendo riesgos", "Pedir un préstamo para comprar cosas", "Trabajar siempre sin jefatura", "Emprender es crear una solución a una necesidad; no es solo endeudarse ni trabajar sin jefe."),
        ("abc", "{F} ¿Cuál es la necesidad que detectan Valentina y Diego?", "No hay dónde comprar colaciones saludables cerca de las oficinas", "Que los estudiantes no tienen tiempo", "Que el kiosco no tiene clientes", "La ficha dice que cerca de las oficinas no hay colaciones saludables."),
        ("abc", "{F} ¿Quiénes son los clientes de la idea?", "Los trabajadores de las tres oficinas cercanas", "Los dueños del kiosco", "Los estudiantes del liceo", "La necesidad la sienten los trabajadores de las oficinas."),
        ("=", "{F} ¿Cuántos clientes potenciales hay en las tres oficinas?", "3*20", "Se multiplican las oficinas por los trabajadores de cada una.", " clientes"),
        ("abc", "{F} ¿Qué ventaja ofrece la idea frente al kiosco?", "Colaciones saludables a menor precio", "Una colación más cara con más variedad", "Una colación sin ingredientes", "La idea cobra $2.500 frente a los $3.000 del kiosco y ofrece variedad saludable."),
        ("=", "{F} ¿Cuántos pesos más barata es cada colación respecto del kiosco?", "3000-2500", "Al precio del kiosco se le resta el precio de la idea.", " pesos"),
        ("=", "{F} De los 15 trabajadores consultados, 9 dijeron que sí comprarían. ¿Cuántos de cada 100 comprarían?", "9*100//15", "Se multiplica por 100 y se divide entre los consultados.", " de cada 100"),
        ("=", "{F} Si solo 1 de cada 5 clientes potenciales comprara una colación al día, ¿cuántos pesos venderían en un día?", "(60//5)*2500", "Se calculan los compradores y se multiplican por el precio.", " pesos"),
        ("abc", "¿Por qué conviene preguntar a posibles clientes antes de invertir?", "Para validar si la idea responde a una necesidad real y reducir el riesgo", "Para que se enteren de la idea y la copien", "Porque preguntar es obligatorio por ley", "Preguntar antes de invertir ayuda a no perder dinero en una idea sin demanda."),
        ("abc", "{F} Diego dice: «Como a mí me encantaría comprar estas colaciones, no hace falta preguntar a nadie». ¿Qué problema tiene?", "Su gusto no representa a los clientes, por lo que hay que validar con ellos", "Ninguno: lo que le gusta a un socio le gusta a todos", "Preguntar quita tiempo", "Validar con clientes evita que el gusto personal reemplace a la demanda real."),
        ("abc", "Una trabajadora de una empresa de ejemplo propone reordenar la bodega para ahorrar tiempo de búsqueda. ¿Qué tipo de iniciativa es?", "Un emprendimiento dentro del lugar de trabajo: una mejora útil", "No es emprender, porque no genera una empresa nueva", "Una falta, porque no es su función", "Proponer una mejora útil es una forma de emprender dentro de la empresa."),
        ("abc", "{F} Valentina propone vender de inmediato 100 colaciones diarias sin probar antes. ¿Qué observación corresponde?", "Conviene empezar pequeño y ajustar con la demanda real", "Está bien: cuanto más rápido, mejor", "No debería vender nada nunca", "Probar a pequeña escala reduce el riesgo de perder lo invertido."),
        ("=", "{F} Si los 9 trabajadores interesados compran una colación cada uno en un día, ¿cuántos pesos ingresan?", "9*2500", "Se multiplican los compradores por el precio de una colación.", " pesos"),
    ],
    ctx=("abc", "{F} Para vender alimentos, Diego pregunta qué permisos hacen falta. ¿Qué respuesta es más adecuada?", "Consultar a las instituciones competentes sobre las normas y los permisos vigentes antes de vender", "Vender y preguntar después", "Pedir a un amigo que «sabe»", "Los permisos dependen de la norma vigente y se consultan en fuentes oficiales."),
    sc=[
        ("En emprendimiento: ¿qué es la propuesta de valor?", "Lo que ofrece la idea y cómo se diferencia", "Explica por qué el cliente preferiría esta opción."),
        ("¿Para qué se valida una idea?", "Para comprobar que responde a una necesidad real", "Reduce el riesgo antes de invertir."),
        ("¿Quién puede emprender?", "Cualquier persona, también dentro de su trabajo", "Mejorar el trabajo también es emprender."),
    ],
    op=("Caso de ejemplo. En una población ficticia no hay un lugar donde reparar bicicletas cerca de un liceo con 300 estudiantes, de los cuales 60 vienen en bicicleta. Marcela y Tomás piensan ofrecer una pequeña revisión de frenos y neumáticos los viernes, a $5.000 (precio de ejemplo). Consultaron a 20 estudiantes con bicicleta y 8 dijeron que sí lo usarían. "
        "Escribe: (1) la necesidad, (2) los clientes y cuántos clientes potenciales hay, (3) cuántos de cada 100 dijeron que sí, (4) una propuesta de valor, (5) un permiso o norma que consultarías.",
        "(1) Falta de un lugar cercano para revisar bicicletas. (2) Estudiantes que vienen en bicicleta: 60. (3) 8 × 100 ÷ 20 = 40 de cada 100. (4) Revisión rápida, cerca del liceo y a bajo precio. (5) Consultaría con la dirección del liceo y con las instituciones competentes qué normas y permisos corresponden; no haría trabajos para los que no estoy capacitado.",
        ["identifica la necesidad", "calcula clientes y proporciones", "formula una propuesta de valor", "menciona consultar normas"],
        ["hoja con cinco respuestas"],
        ["no validar la idea", "no calcular la proporción", "ignorar normas"],
        "Pregunta: «¿qué harías si solo 2 de 20 dijeran que sí?». Debe plantear revisar la idea, el precio o los clientes antes de invertir."),
    reinforce="Escribe una necesidad que observes en tu liceo o barrio y una idea para resolverla.",
    extend="Explica con un ejemplo por qué una mejora dentro de una empresa también es una forma de emprender.",
)

# ============================================================ OAG-10, clase 2
F = ("Ficha 38 (negocio de ejemplo: venta de colaciones por encargo; cifras inventadas). Cada colación cuesta $1.500 en ingredientes y envase (costo variable por unidad) y se vende a $2.500. "
     "Costos fijos del mes: arriendo de un espacio $90.000 y transporte $30.000. Utilidad = ingresos − costos variables − costos fijos. Punto de equilibrio = costos fijos ÷ margen por unidad.")
build(
    G10, 2, F,
    use="Aprenderé a calcular ingresos, costos fijos y variables, margen, utilidad y punto de equilibrio de un negocio pequeño.",
    prior=["Sé multiplicar, restar y dividir.", "Conozco qué es un precio.", "Conozco la idea de emprender."],
    explain=[
        "Los ingresos son el dinero que entra por vender: precio por unidades vendidas. Los costos son el dinero que se gasta para producir y vender. Los costos variables cambian con lo que se produce, como los ingredientes y los envases. Los costos fijos se pagan aunque no se venda nada, como el arriendo. La utilidad es lo que queda después de restar todos los costos a los ingresos.",
        "El margen por unidad es el precio menos el costo variable de esa unidad; es lo que cada venta aporta para pagar los costos fijos y generar utilidad. El punto de equilibrio es la cantidad de unidades que hay que vender para cubrir justo todos los costos, sin ganar ni perder: se calcula dividiendo los costos fijos entre el margen por unidad. Desde esa cantidad, cada venta adicional deja utilidad.",
        "Confundir ingresos con utilidad es un error frecuente: lo que entra no es lo que se gana. Registrar los datos con orden permite tomar buenas decisiones." + LIM,
    ],
    vocab=[("ingreso", "dinero que entra por las ventas"), ("costo variable", "costo que cambia según lo que se produce"), ("costo fijo", "costo que se paga aunque no se venda"), ("margen por unidad", "precio menos costo variable de una unidad"), ("utilidad", "ingresos menos todos los costos"), ("punto de equilibrio", "ventas con las que no se gana ni se pierde")],
    worked=[
        ("Calcular el margen", "Un producto de ejemplo se vende a $900 y su costo variable es $600. ¿Cuál es el margen por unidad?", ["Margen = precio − costo variable.", "900 − 600 = 300."], "$300 por unidad"),
        ("Punto de equilibrio", "Un negocio de ejemplo tiene costos fijos de $60.000 y un margen de $300 por unidad. ¿Cuál es su punto de equilibrio?", ["Se dividen los costos fijos entre el margen.", "60.000 ÷ 300 = 200."], "200 unidades"),
    ],
    mistakes=[("Decir «vendí 100 colaciones y gané 250.000 pesos».", "Esos son ingresos; falta restar los costos variables y fijos para saber la utilidad.", "Calcula la utilidad: ingresos menos todos los costos."),
              ("No considerar el arriendo ni el transporte porque «no cambian».", "Los costos fijos también hay que pagarlos, aunque no se venda.", "Incluye los costos fijos en el cálculo de la utilidad.")],
    T=[
        ("abc", "En gestión de un negocio: ¿qué es un costo fijo?", "Un costo que se paga aunque no se venda nada", "Un costo que cambia con cada producto vendido", "El dinero que entra por las ventas", "El costo fijo no depende de las ventas, como el arriendo."),
        ("abc", "{F} ¿Cuál de estos es un costo fijo?", "El arriendo del espacio", "Los ingredientes de cada colación", "El envase de cada colación", "El arriendo se paga igual aunque no se venda ninguna colación."),
        ("abc", "{F} ¿Cuál de estos es un costo variable?", "Los ingredientes y el envase de cada colación", "El arriendo", "El transporte mensual", "Los ingredientes dependen de cuántas colaciones se preparan."),
        ("=", "{F} ¿Cuánto suman los costos fijos del mes?", "90000+30000", "Se suman el arriendo y el transporte.", " pesos"),
        ("=", "{F} ¿Cuál es el margen por colación?", "2500-1500", "Al precio de venta se le resta el costo variable por unidad.", " pesos"),
        ("=", "{F} Si se venden 150 colaciones, ¿cuánto suman los ingresos?", "150*2500", "Se multiplica el precio por las unidades vendidas.", " pesos"),
        ("=", "{F} Si se venden 150 colaciones, ¿cuánto suman los costos variables?", "150*1500", "Se multiplica el costo variable por unidad por las unidades.", " pesos"),
        ("=", "{F} ¿Cuál es la utilidad del mes si se venden 150 colaciones?", "150*2500-150*1500-(90000+30000)", "Se restan los costos variables y los fijos a los ingresos.", " pesos"),
        ("=", "{F} ¿Cuántas colaciones hay que vender para llegar al punto de equilibrio?", "(90000+30000)//(2500-1500)", "Se dividen los costos fijos entre el margen por colación.", " colaciones"),
        ("abc", "{F} Un socio dice: «Vendimos 100 colaciones, así que ganamos 250.000». ¿Qué error comete?", "Confunde ingresos con utilidad: no resta los costos variables ni los fijos", "Ninguno: lo que entra es lo que se gana", "Cuenta de más las colaciones", "Los 250.000 son ingresos; para la utilidad faltan los costos."),
        ("abc", "{F} Si el precio bajara a $2.000 sin cambiar los costos, ¿qué ocurre con el margen y el punto de equilibrio?", "El margen baja a $500 y el punto de equilibrio sube", "El margen sube y el punto de equilibrio baja", "No cambian", "Con menor precio queda menos para pagar costos fijos, por lo que se necesita vender más."),
        ("abc", "{F} En el mes se vendieron solo 90 colaciones. ¿Qué ocurre?", "Hay pérdida, porque no se alcanza el punto de equilibrio", "Hay utilidad, porque algo se vendió", "El resultado es exactamente cero", "Con 90 colaciones el margen total no alcanza a pagar los costos fijos de $120.000."),
        ("=", "{F} Con 90 colaciones vendidas, ¿cuántas faltan para llegar al punto de equilibrio?", "(90000+30000)//(2500-1500)-90", "Al punto de equilibrio se le restan las colaciones vendidas.", " colaciones"),
    ],
    ctx=("abc", "{F} El mes siguiente esperan vender 130 colaciones. Los socios quieren saber si habrá utilidad antes de comprar los ingredientes. ¿Qué hacen?", "Calculan el margen total (130 × 1.000) y lo comparan con los costos fijos de $120.000", "Compran todo y esperan a ver qué pasa", "Suben el precio sin calcular", "130 × 1.000 = 130.000, que supera los costos fijos en $10.000; calcular antes ayuda a decidir."),
    sc=[
        ("En un negocio de ejemplo: ¿cómo se calcula la utilidad?", "Ingresos menos todos los costos", "La utilidad es lo que queda después de pagar los costos."),
        ("¿Qué es el punto de equilibrio?", "Las ventas con las que no se gana ni se pierde", "Cubre justo todos los costos, sin ganar ni perder."),
        ("¿Qué costos se pagan aunque no se venda?", "Los costos fijos", "Son independientes del volumen de ventas."),
    ],
    op=("Caso de ejemplo. Un taller ficticio de bolsos de tela vende cada bolso a $8.000. El costo de la tela e hilos por bolso es de $3.000. Costos fijos del mes: arriendo $60.000 y luz $15.000. "
        "Escribe: (1) el margen por bolso, (2) los costos fijos del mes, (3) el punto de equilibrio, (4) la utilidad si se venden 30 bolsos, (5) qué harías si solo vendes 10 bolsos.",
        "(1) 8.000 − 3.000 = 5.000. (2) 60.000 + 15.000 = 75.000. (3) 75.000 ÷ 5.000 = 15 bolsos. (4) 30 × 5.000 − 75.000 = 75.000 pesos. (5) Con 10 bolsos hay pérdida (50.000 de margen total frente a 75.000 de costos fijos); revisaría el precio, los costos o cómo vender más.",
        ["calcula el margen", "suma los costos fijos", "calcula el punto de equilibrio", "calcula la utilidad", "analiza el caso de pocas ventas"],
        ["hoja con cinco respuestas"],
        ["confundir ingresos con utilidad", "olvidar los costos fijos", "dividir mal"],
        "Pregunta: «¿qué pasa con el equilibrio si el arriendo sube a $90.000?». Debe calcular 105.000 ÷ 5.000 = 21 bolsos."),
    reinforce="Inventa un producto con precio, costo variable y costos fijos y calcula su punto de equilibrio.",
    extend="Explica con un ejemplo por qué un negocio con muchas ventas puede igualmente perder dinero.",
)

# ============================================================ OAG-10, clase 3
F = ("Ficha 39 (registro de cuatro semanas de un negocio de ejemplo). Saldo inicial: $50.000. Semana 1: ingresos $150.000 y egresos $120.000. Semana 2: ingresos $180.000 y egresos $140.000. "
     "Semana 3: ingresos $120.000 y egresos $150.000. Semana 4: ingresos $200.000 y egresos $130.000. Saldo al final de la semana = saldo anterior + ingresos − egresos.")
build(
    G10, 3, F,
    use="Aprenderé a llevar un flujo de caja simple, a separar el dinero personal del del negocio y a entender el capital de trabajo.",
    prior=["Conozco ingresos, costos y utilidad.", "Sé sumar y restar cifras grandes.", "Conozco qué es un presupuesto."],
    explain=[
        "El flujo de caja es el registro del dinero que entra (ingresos) y sale (egresos) de un negocio en un período, y del saldo que queda. Se calcula así: saldo anterior más ingresos menos egresos. Si el saldo baja o llega a cero, el negocio puede quedarse sin dinero para pagar, aunque en el papel tenga utilidad. Por eso conviene llevar el registro con orden y mirar cómo evoluciona el saldo semana a semana.",
        "El capital de trabajo es el dinero necesario para operar entre el momento en que se paga (por ejemplo, a proveedores) y el momento en que se cobra a los clientes. Conviene separar el dinero personal del dinero del negocio, para saber realmente si el negocio funciona, y guardar una pequeña reserva para imprevistos. Las ventas deben respaldarse con los documentos que exige la norma vigente, como boletas o facturas; para informarte sobre las obligaciones tributarias, consulta al Servicio de Impuestos Internos.",
        "Los registros honestos permiten tomar decisiones; los registros alterados llevan a decisiones equivocadas." + LIM,
    ],
    vocab=[("flujo de caja", "registro del dinero que entra y sale de un negocio y del saldo que queda"), ("egreso", "dinero que sale del negocio"), ("saldo", "dinero que queda después de sumar ingresos y restar egresos"), ("capital de trabajo", "dinero necesario para operar entre pagar y cobrar"), ("reserva", "dinero que se guarda para imprevistos"), ("documento de venta", "boleta o factura que respalda una venta")],
    worked=[
        ("Calcular un saldo", "Un negocio de ejemplo parte con $30.000, tiene ingresos de $90.000 y egresos de $70.000. ¿Cuál es el saldo final?", ["Saldo = inicial + ingresos − egresos.", "30.000 + 90.000 − 70.000 = 50.000."], "$50.000"),
        ("Separar dinero", "Una vendedora de ejemplo paga su arriendo personal con el dinero de la caja del negocio. ¿Qué problema genera?", ["Mezcla el dinero personal con el del negocio.", "No se sabe cuánto gana realmente el negocio."], "No se puede saber si el negocio funciona"),
    ],
    mistakes=[("Gastar el dinero de la caja del negocio en gastos personales.", "No se sabe cuánto gana el negocio y puede faltar dinero para pagar a proveedores.", "Retira un monto definido para ti y anótalo como egreso."),
              ("Mirar solo las ventas y no el saldo.", "Se puede vender mucho y quedarse sin dinero si los pagos llegan antes que los cobros.", "Lleva un flujo de caja y revisa el saldo con frecuencia.")],
    T=[
        ("abc", "En gestión financiera: ¿qué es el flujo de caja?", "El registro de lo que entra y sale de dinero y del saldo que queda", "El total de ventas del año", "La lista de clientes del negocio", "El flujo de caja registra ingresos, egresos y saldo."),
        ("abc", "{F} ¿En qué semana los egresos fueron mayores que los ingresos?", "En la semana 3", "En la semana 1", "En la semana 4", "En la semana 3 entraron $120.000 y salieron $150.000."),
        ("=", "{F} ¿Cuál es el saldo al final de la semana 1?", "50000+150000-120000", "Al saldo inicial se le suman los ingresos y se restan los egresos.", " pesos"),
        ("=", "{F} Partiendo del saldo de la semana 1, ¿cuál es el saldo al final de la semana 2?", "(50000+150000-120000)+180000-140000", "Al saldo de la semana 1 se suman los ingresos y se restan los egresos.", " pesos"),
        ("=", "{F} Al final de la semana 3, ¿cuál es el saldo?", "(50000+150000-120000)+180000-140000+120000-150000", "Se encadenan los saldos de las semanas anteriores con los datos de la semana 3.", " pesos"),
        ("=", "{F} ¿Cuál es el saldo al final de la semana 4?", "(50000+150000-120000)+180000-140000+120000-150000+200000-130000", "Se encadenan los saldos de las cuatro semanas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos sumaron los ingresos de las cuatro semanas?", "150000+180000+120000+200000", "Se suman los ingresos de cada semana.", " pesos"),
        ("=", "{F} ¿Cuántos pesos sumaron los egresos de las cuatro semanas?", "120000+140000+150000+130000", "Se suman los egresos de cada semana.", " pesos"),
        ("abc", "¿Por qué conviene separar el dinero personal del dinero del negocio?", "Para saber si el negocio realmente funciona y no quedarse sin dinero para pagar", "Para pagar menos a los proveedores", "Para poder gastar la caja del negocio sin llevar registro", "Mezclar dineros impide medir las ganancias reales."),
        ("abc", "{F} En la semana 3 el saldo bajó. Un socio dice: «No importa, el resto de las semanas fue bueno». ¿Qué respuesta es correcta?", "Importa: si se repite, el saldo podría agotarse; hay que revisar egresos e ingresos", "Tiene razón: una semana mala no se analiza", "Hay que ocultar esa semana en el registro", "Los números de una semana pueden mostrar un problema que conviene corregir a tiempo."),
        ("abc", "Un negocio vende a clientes que pagan a 30 días, pero debe pagar hoy a sus proveedores. ¿Qué necesita para operar?", "Capital de trabajo para cubrir el tiempo entre pagar y cobrar", "Vender menos", "Dejar de pagar a los proveedores", "El capital de trabajo cubre el desfase entre pagos y cobros."),
        ("abc", "Un cliente pide no recibir boleta a cambio de un descuento. ¿Qué corresponde?", "Emitir el documento de venta según la norma vigente y consultar al Servicio de Impuestos Internos si hay dudas", "Aceptar porque se vende más rápido", "Entregar boleta solo si el cliente la exige", "Las ventas deben respaldarse con los documentos que exige la norma vigente."),
        ("=", "{F} Si en la semana 3 los egresos hubieran sido $120.000 en vez de $150.000, ¿cuál habría sido el saldo al final de esa semana?", "(50000+150000-120000)+180000-140000+120000-120000", "Se cambia el egreso de la semana 3 y se recalcula el saldo acumulado.", " pesos"),
    ],
    ctx=("abc", "{F} Al comenzar la semana 5, el negocio debe pagar $200.000 a un proveedor y tiene un saldo de $160.000. ¿Qué hace el dueño?", "Revisa las cuentas por cobrar, negocia un plazo o ajusta los pagos antes de que falte dinero", "Paga y espera que lleguen ingresos", "Retira dinero personal sin registrar", "Anticipar un faltante permite negociar o reordenar pagos a tiempo."),
    sc=[
        ("En gestión financiera: ¿cómo se calcula el saldo?", "Saldo anterior más ingresos menos egresos", "Así se ve cuánto dinero queda disponible."),
        ("¿Para qué sirve una reserva para imprevistos?", "Para cubrir gastos inesperados", "Evita quedarse sin dinero ante una emergencia."),
        ("¿Dónde te informas de obligaciones tributarias?", "En el Servicio de Impuestos Internos", "Es la institución que informa sobre tributación."),
    ],
    op=("Caso de ejemplo. Una pastelería ficticia empieza el mes con $80.000. Semana 1: ingresos $200.000, egresos $170.000. Semana 2: ingresos $150.000, egresos $190.000. Semana 3: ingresos $230.000, egresos $160.000. "
        "Escribe: (1) el saldo al final de cada semana, (2) en qué semana el saldo bajó, (3) una razón para separar el dinero personal del del negocio, (4) una medida para evitar quedarse sin dinero.",
        "(1) Semana 1: 80.000 + 200.000 − 170.000 = 110.000. Semana 2: 110.000 + 150.000 − 190.000 = 70.000. Semana 3: 70.000 + 230.000 − 160.000 = 140.000. (2) En la semana 2. (3) Para saber cuánto gana realmente el negocio. (4) Llevar una reserva y revisar el saldo cada semana.",
        ["encadena bien los saldos", "identifica la semana en que bajó", "explica la separación de dineros", "propone una medida"],
        ["hoja con cuatro respuestas"],
        ["no encadenar los saldos", "mezclar el dinero personal", "no proponer medida"],
        "Pregunta: «¿qué harías en la semana 3 si el saldo fuera menor a lo necesario para pagar al proveedor?». Debe plantear reordenar pagos y negociar plazos."),
    reinforce="Inventa un flujo de caja de tres semanas con saldo inicial y calcula el saldo de cada una.",
    extend="Explica por qué un negocio con utilidad puede quedarse sin dinero en caja.",
)

# ============================================================ OAG-10, clase 4
F = ("Ficha 40 (dos proyectos de ejemplo para un negocio pequeño; cifras inventadas). Proyecto A: inversión inicial $300.000; utilidad mensual esperada $60.000; riesgo: depende de un solo cliente. "
     "Proyecto B: inversión inicial $200.000; utilidad mensual esperada $25.000; riesgo: necesita permisos que tardan en llegar. Tiempo de recuperación = inversión ÷ utilidad mensual. Una persona de ejemplo dispone de $250.000 ahorrados.")
build(
    G10, 4, F,
    use="Aprenderé a evaluar la viabilidad de un proyecto con datos de inversión, recuperación y riesgos, y a armar un plan de acción simple.",
    prior=["Conozco utilidad y punto de equilibrio.", "Sé dividir y multiplicar.", "Conozco el flujo de caja."],
    explain=[
        "Evaluar la viabilidad de un proyecto es analizar si es posible y conviene llevarlo a cabo. Se revisan varios aspectos: el económico (si deja utilidad y cuánto tarda en recuperarse la inversión), el técnico (si se cuenta con los conocimientos y recursos), el legal (si cumple las normas y permisos) y el social y ambiental (qué efecto tiene en otras personas y en el entorno). La inversión inicial es el dinero que hay que poner antes de empezar a vender.",
        "El tiempo de recuperación se calcula dividiendo la inversión inicial entre la utilidad mensual: indica en cuántos meses se recupera lo invertido. Sirve para comparar, pero no es lo único: también importan los riesgos y si se cuenta con el dinero. Un plan de acción reúne los pasos, los responsables y las fechas para llevar el proyecto a la práctica. Conviene pedir orientación a instituciones de apoyo al emprendimiento y actuar con honestidad con clientes y proveedores.",
        "Las cifras de la ficha son de ejemplo; este cuaderno no recomienda iniciar negocios ni endeudarse." + LIM,
    ],
    vocab=[("viabilidad", "posibilidad real de llevar a cabo un proyecto con buenos resultados"), ("inversión inicial", "dinero que hay que poner antes de empezar a vender"), ("tiempo de recuperación", "meses que tarda la utilidad en cubrir la inversión"), ("riesgo", "posibilidad de que algo salga mal"), ("plan de acción", "pasos, responsables y fechas para ejecutar un proyecto"), ("permiso", "autorización necesaria para realizar una actividad")],
    worked=[
        ("Tiempo de recuperación", "Un proyecto de ejemplo requiere una inversión de $120.000 y deja $20.000 de utilidad al mes. ¿En cuántos meses se recupera?", ["Se divide la inversión entre la utilidad mensual.", "120.000 ÷ 20.000 = 6."], "6 meses"),
        ("Revisar la viabilidad legal", "Un proyecto de ejemplo vende alimentos preparados. ¿Qué aspecto debe consultar antes de empezar?", ["Algunos rubros requieren permisos.", "Debe consultar las normas y permisos vigentes."], "Las normas y los permisos vigentes del rubro"),
    ],
    mistakes=[("Elegir un proyecto solo porque «se recupera más rápido».", "Pueden faltar dinero, permisos o clientes, y el riesgo puede ser alto.", "Compara también inversión, riesgos y normas."),
              ("Empezar el proyecto sin permisos «y ver qué pasa».", "Puede ser sancionado y perder lo invertido.", "Consulta los permisos antes de invertir.")],
    T=[
        ("abc", "En evaluación de proyectos: ¿qué es la viabilidad?", "La posibilidad real de llevar a cabo un proyecto con buenos resultados", "El nombre del proyecto", "El número de clientes de la competencia", "La viabilidad analiza si el proyecto es posible y conviene hacerlo."),
        ("=", "{F} ¿En cuántos meses se recupera la inversión del proyecto A?", "300000//60000", "Se divide la inversión entre la utilidad mensual.", " meses"),
        ("=", "{F} ¿En cuántos meses se recupera la inversión del proyecto B?", "200000//25000", "Se divide la inversión entre la utilidad mensual.", " meses"),
        ("=", "{F} ¿Cuánta utilidad se obtiene en 12 meses con el proyecto A?", "60000*12", "Se multiplica la utilidad mensual por los 12 meses.", " pesos"),
        ("=", "{F} ¿Cuánta utilidad se obtiene en 12 meses con el proyecto B?", "25000*12", "Se multiplica la utilidad mensual por los 12 meses.", " pesos"),
        ("abc", "{F} ¿Qué proyecto cabe en el ahorro disponible sin necesitar más dinero?", "El proyecto B", "El proyecto A", "Ambos", "El proyecto A pide $300.000 y la persona tiene $250.000; el B pide $200.000."),
        ("=", "{F} ¿Cuántos pesos le faltan a la persona para financiar el proyecto A?", "300000-250000", "A la inversión requerida se le resta el ahorro disponible.", " pesos"),
        ("=", "{F} En 12 meses, ¿cuál es la ganancia neta del proyecto A, es decir, la utilidad menos la inversión?", "60000*12-300000", "A la utilidad de 12 meses se le resta la inversión inicial.", " pesos"),
        ("abc", "{F} ¿Cuál es el principal riesgo del proyecto A?", "Depende de un solo cliente", "Necesita permisos que tardan", "No deja utilidad", "La ficha indica que el riesgo de A es depender de un solo cliente."),
        ("abc", "{F} Un amigo dice: «Elige A, porque se recupera antes». ¿Qué falta considerar?", "Si se cuenta con el dinero, el riesgo de depender de un cliente y si se cumplen las normas", "Nada: el tiempo de recuperación es lo único importante", "El color del logo", "Una buena decisión considera financiamiento, riesgos y normas, además del tiempo de recuperación."),
        ("abc", "¿Qué es un plan de acción?", "Los pasos, los responsables y las fechas para llevar a cabo el proyecto", "Una lista de ideas sin orden", "El nombre del equipo", "El plan de acción organiza quién hace qué y cuándo."),
        ("abc", "{F} Para el proyecto B, ¿qué es lo más adecuado respecto de los permisos?", "Iniciar los trámites cuanto antes y planificar sin invertir todo antes de obtenerlos", "Comenzar a vender sin permisos", "Esperar a que alguien los pida", "Los permisos son una condición del proyecto y conviene gestionarlos antes de la inversión grande."),
        ("=", "{F} Si el proyecto B se retrasa 3 meses por los permisos antes de dar utilidad, ¿en cuántos meses desde que se invierte se recupera la inversión?", "200000//25000+3", "Se suma el retraso al tiempo normal de recuperación.", " meses"),
    ],
    ctx=("abc", "{F} La persona de ejemplo duda entre A y B. Un familiar le ofrece prestarle lo que falta para A. ¿Qué es lo más prudente?", "Analizar bien el riesgo y la capacidad de devolver lo prestado antes de decidir, y consultar fuentes oficiales", "Aceptar de inmediato porque A se recupera antes", "Descartar B sin analizarlo", "Endeudarse sin analizar riesgo y capacidad de pago puede llevar a problemas mayores."),
    sc=[
        ("En proyectos de ejemplo: ¿cómo se calcula el tiempo de recuperación?", "Inversión dividida entre la utilidad mensual", "Indica en cuántos meses se recupera lo invertido."),
        ("¿Qué aspectos se revisan en la viabilidad?", "Económico, técnico, legal y social", "Así se analiza el proyecto en forma completa."),
        ("¿Para qué sirve un plan de acción?", "Para saber quién hace qué y cuándo", "Ordena la ejecución del proyecto con responsables y fechas."),
    ],
    op=("Caso de ejemplo. Un grupo de estudiantes de un liceo ficticio evalúa dos proyectos. Proyecto 1: lavado de autos con inversión de $150.000 y utilidad de $30.000 al mes; riesgo: depende del clima. Proyecto 2: venta de artesanías con inversión de $90.000 y utilidad de $15.000 al mes; riesgo: ventas solo en fines de semana. Dispone de $120.000. "
        "Escribe: (1) el tiempo de recuperación de cada uno, (2) cuál cabe en el ahorro, (3) un riesgo y una forma de reducirlo, (4) un plan de acción de tres pasos con responsables y fechas inventadas.",
        "(1) Proyecto 1: 150.000 ÷ 30.000 = 5 meses; proyecto 2: 90.000 ÷ 15.000 = 6 meses. (2) Solo el proyecto 2. (3) Riesgo: ventas solo en fines de semana; reducirlo participando en ferias o vendiendo por encargo. (4) Paso 1: cotizar materiales (Ana, semana 1); paso 2: consultar normas y permisos (Beto, semana 2); paso 3: primera venta de prueba (todos, semana 3).",
        ["calcula la recuperación", "compara con el ahorro", "identifica y reduce un riesgo", "arma un plan con responsables y fechas"],
        ["hoja con cuatro respuestas"],
        ["ignorar el ahorro disponible", "plan sin responsables", "no considerar riesgos"],
        "Pregunta: «¿qué pasaría si las ventas son la mitad de lo esperado?». Debe recalcular la utilidad y el tiempo de recuperación."),
    reinforce="Inventa dos ideas de proyecto con inversión y utilidad mensual y calcula cuál se recupera antes.",
    extend="Explica por qué un proyecto que se recupera rápido puede no ser la mejor decisión.",
)

# ============================================================ OAG-11, clase 1
F = ("Ficha 41 (cinco situaciones de ejemplo en lugares de trabajo ficticios). 1) En una cocina, el piso del pasillo está mojado y no hay aviso. 2) En una oficina, una persona trabaja 8 horas sentada con la pantalla muy baja y empieza a sentir dolor de cuello. "
     "3) En una bodega, las cajas están apiladas hasta el techo y la pila se inclina. 4) En un taller, hay un cable pelado a la vista en una zona de paso. 5) En una obra, un trabajador circula sin casco en una zona donde se advierte la caída de objetos.")
build(
    G11, 1, F,
    use="Aprenderé los conceptos básicos de la prevención de riesgos: peligro, riesgo, accidente, incidente y enfermedad ocupacional, y a reconocer condiciones y acciones inseguras en el entorno.",
    prior=["Sé observar un entorno de trabajo.", "Sé calcular cuántos por cada 100.", "Sé que la seguridad es responsabilidad de todos."],
    explain=[
        "Un peligro es cualquier fuente con potencial de causar daño, como un piso mojado o un cable pelado. El riesgo es la posibilidad de que ese peligro cause daño, considerando qué tan probable es y qué tan grave podría ser. Un accidente es un hecho inesperado que causa lesión a una persona; un incidente es un hecho que pudo causar daño pero no lo causó. Una enfermedad ocupacional es un daño a la salud que aparece por la exposición prolongada a factores del trabajo, como una mala postura o el ruido intenso.",
        "Las condiciones inseguras son características del entorno que pueden causar daño, como el piso mojado sin aviso. Las acciones inseguras son conductas de las personas que aumentan el riesgo, como circular sin el elemento de protección exigido. Los factores de riesgo pueden ser de seguridad (caídas, golpes, electricidad), físicos (ruido, temperatura), químicos, biológicos, ergonómicos (posturas, cargas) y psicosociales (estrés, trato). La prevención consiste en actuar antes de que ocurra el daño: observar, reportar y corregir.",
        "Evaluar las condiciones del entorno es una tarea compartida: la empresa organiza y capacita; cada trabajador cumple las normas y avisa de lo que observa. Las normas vigentes y las entidades fiscalizadoras de cada sector definen las reglas." + AVISO + LIM,
    ],
    vocab=[("peligro", "fuente con potencial de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño, según su probabilidad y gravedad"), ("accidente", "hecho inesperado que causa lesión a una persona"), ("incidente", "hecho que pudo causar daño pero no lo causó"), ("enfermedad ocupacional", "daño a la salud causado por la exposición prolongada a factores del trabajo"), ("condición insegura", "característica del entorno que puede causar daño"), ("acción insegura", "conducta de una persona que aumenta el riesgo")],
    worked=[
        ("Distinguir peligro y riesgo", "Un pasillo de ejemplo tiene el piso mojado. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el piso mojado.", "El riesgo es la posibilidad de que alguien resbale y se lesione."], "Peligro: piso mojado; riesgo: resbalar y lesionarse"),
        ("Cálculo de incidentes por accidente", "Una empresa de ejemplo registró 9 incidentes y 3 accidentes. ¿Cuántos incidentes hubo por cada accidente?", ["Se divide el número de incidentes entre el de accidentes.", "9 ÷ 3 = 3."], "3 incidentes por accidente"),
    ],
    mistakes=[("Pensar «nunca ha pasado nada, entonces no hay riesgo».", "El peligro existe aunque aún no haya causado daño; solo faltó la ocasión.", "Revisa los peligros y corrígelos antes de que ocurra un accidente."),
              ("Ignorar un incidente porque «nadie se lastimó».", "Es una advertencia que muestra que algo puede salir mal.", "Repórtalo para que se corrija la causa.")],
    T=[
        ("abc", "En prevención de riesgos: ¿qué es un riesgo?", "La posibilidad de que un peligro cause daño, según su probabilidad y gravedad", "Cualquier cosa que existe en el lugar de trabajo", "Un accidente que ya ocurrió", "El riesgo se refiere a la posibilidad de daño; el accidente es el daño ocurrido."),
        ("abc", "{F} ¿Qué tipo de situación es la 1, el piso mojado sin aviso?", "Una condición insegura del entorno", "Una acción insegura de una persona", "Una enfermedad ocupacional", "El piso mojado sin aviso es una característica del entorno."),
        ("abc", "{F} ¿Qué situación muestra una acción insegura de una persona?", "La 5: circular sin casco en una zona con caída de objetos", "La 1: piso mojado sin aviso", "La 3: cajas apiladas hasta el techo", "En la 5 es la conducta del trabajador la que aumenta el riesgo."),
        ("abc", "{F} ¿Qué situación puede dar origen a una enfermedad ocupacional si se mantiene en el tiempo?", "La 2: trabajar 8 horas con mala postura", "La 4: cable pelado", "La 5: circular sin casco", "La exposición prolongada a una mala postura puede dañar la salud."),
        ("abc", "¿Qué es un incidente?", "Un hecho que pudo causar daño pero no lo causó", "Un hecho que causa una lesión grave", "Una enfermedad que aparece con los años", "El incidente es un cuasi accidente: advierte que algo puede salir mal."),
        ("=", "Una empresa de ejemplo registró en un trimestre 12 incidentes y 3 accidentes. ¿Cuántos incidentes hubo por cada accidente?", "12//3", "Se divide el número de incidentes entre el de accidentes.", " incidentes"),
        ("abc", "{F} ¿Qué factor de riesgo representa el cable pelado de la situación 4?", "Un factor de seguridad de tipo eléctrico", "Un factor psicosocial", "Un factor biológico", "El cable expuesto puede causar un daño eléctrico, es decir, un riesgo de seguridad."),
        ("abc", "{F} Ves la situación 1 en tu lugar de trabajo. ¿Qué haces?", "Avisas de inmediato a quien corresponde y no usas ese tramo hasta que se corrija", "Pasas rápido para no demorar", "Esperas a que alguien se caiga", "Avisar y evitar el tramo protege a las personas hasta que se corrija."),
        ("=", "En una oficina de ejemplo trabajan 25 personas y 10 reportan dolor de cuello. ¿Cuántas de cada 100 reportan el dolor?", "10*100//25", "Se multiplica por 100 y se divide entre las personas de la oficina.", " de cada 100"),
        ("abc", "Un trabajador dice: «Hace años que no pasa nada, así que no hay riesgo». ¿Qué respuesta es correcta?", "El riesgo es una posibilidad: que no haya ocurrido no significa que el peligro no exista", "Tiene razón, el riesgo se mide por lo que ya pasó", "El riesgo solo existe con una lesión", "El riesgo es la posibilidad de daño, no solo un daño ya ocurrido."),
        ("abc", "¿Quién es responsable de la prevención en un lugar de trabajo?", "Todos: la empresa organiza y capacita, y cada trabajador cumple las normas y avisa", "Solo el trabajador que se lesiona", "Solo la jefatura", "La prevención es una tarea compartida entre la empresa y las personas."),
        ("abc", "{F} Un compañero propone reparar el cable pelado él mismo con cinta, porque sabe algo de electricidad. ¿Qué corresponde?", "No intervenir: avisar al responsable para que lo repare personal autorizado", "Hacerlo rápido para evitar accidentes", "Taparlo con cartón y seguir trabajando", "Las instalaciones eléctricas solo las intervienen personas autorizadas."),
        ("=", "Tras aplicar medidas de orden, los incidentes de una bodega de ejemplo bajaron de 15 a 9. ¿Cuántos por cada 100 bajaron?", "(15-9)*100//15", "Se calcula la baja, se multiplica por 100 y se divide entre los incidentes iniciales.", " por cada 100"),
    ],
    ctx=("abc", "{F} Una estudiante en práctica nota en la bodega la situación 3, con cajas inclinadas. Su tutor está ocupado. ¿Qué hace?", "Se aleja del lugar, avisa a su tutor o a la persona responsable y espera que lo corrijan quienes están autorizados", "Intenta enderezar la pila ella sola", "Sigue trabajando junto a la pila para no interrumpir", "Alejarse y avisar protege a las personas y deja la corrección a quienes corresponde."),
    sc=[
        ("En prevención de riesgos: ¿qué es un peligro?", "Una fuente con potencial de causar daño", "El peligro existe aunque aún no haya causado daño."),
        ("¿Qué haces si ves una condición insegura?", "Aviso a quien corresponde", "Avisar permite corregirla antes de un accidente."),
        ("¿Qué es una enfermedad ocupacional?", "Un daño a la salud por exposición prolongada en el trabajo", "Aparece con el tiempo, por ejemplo por la postura o el ruido."),
    ],
    op=("Caso de ejemplo. En una pastelería ficticia se observa: una bandeja pesada en un estante alto sin aviso; un piso con aceite derramado sin señal; una trabajadora que pasa 7 horas de pie en un mesón demasiado bajo y refiere dolor de espalda; y un compañero que usa el celular mientras camina por el pasillo de cajas. "
        "Escribe: (1) cuál es el peligro y cuál el riesgo en cada situación, (2) cuáles son condiciones inseguras y cuáles acciones inseguras, (3) cuál puede originar una enfermedad ocupacional, (4) a quién avisarías y qué NO harías por tu cuenta.",
        "(1) Bandeja alta: peligro la bandeja, riesgo de caída y golpe. Aceite: peligro el piso resbaladizo, riesgo de caída. Mesón bajo: peligro la postura, riesgo de dolor de espalda. Celular al caminar: peligro la distracción, riesgo de tropiezo. (2) Condiciones inseguras: bandeja, aceite y mesón. Acción insegura: celular al caminar. (3) El mesón bajo, por la postura prolongada. (4) Avisaría a la jefatura o al responsable de prevención; no limpiaría ni retiraría sustancias o cargas sin estar autorizado y capacitado.",
        ["distingue peligro y riesgo", "clasifica condiciones y acciones inseguras", "reconoce la enfermedad ocupacional", "avisa y evita intervenir sin autorización"],
        ["hoja con cuatro respuestas"],
        ["confundir peligro y riesgo", "intervenir por cuenta propia", "no avisar"],
        "Pregunta: «¿qué pasaría si nadie avisa del aceite?». Debe mencionar que alguien podría resbalar y lesionarse."),
    reinforce="Observa tu liceo o tu casa y escribe dos condiciones inseguras y dos acciones inseguras que viste, sin tocar ni arreglar nada peligroso.",
    extend="Explica con un ejemplo por qué un incidente sin lesión es una advertencia que no debe ignorarse.",
)

# ============================================================ OAG-11, clase 2
F = ("Ficha 42 (cinco medidas de ejemplo para reducir un mismo riesgo: el ruido intenso en un taller ficticio). A) Eliminar la tarea ruidosa, comprando la pieza ya terminada. B) Sustituir la máquina por un equipo menos ruidoso. "
     "C) Instalar una cubierta que encierra la fuente de ruido (control de ingeniería). D) Rotar al personal, limitar las horas de exposición, capacitar y señalizar (control administrativo). E) Entregar protectores auditivos (elemento de protección personal, EPP). "
     "Jerarquía de controles: eliminación, sustitución, controles de ingeniería, controles administrativos y, como último recurso, EPP.")
build(
    G11, 2, F,
    use="Aprenderé la jerarquía de controles para reducir un riesgo y qué son los elementos de protección personal (EPP), sus características y su uso responsable.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé multiplicar y restar.", "Sé que la seguridad es responsabilidad de todos."],
    explain=[
        "Para reducir un riesgo se aplican medidas ordenadas de la más efectiva a la menos efectiva. Primero se intenta eliminar el peligro; si no se puede, se sustituye por algo menos peligroso; luego se usan controles de ingeniería, que aíslan o encierran el peligro; después, controles administrativos, como rotación de personal, procedimientos, capacitación y señalización; y como último recurso, los elementos de protección personal (EPP). Esta secuencia se llama jerarquía de controles.",
        "Los EPP son equipos que protegen a la persona, como casco, lentes, protectores auditivos, guantes o calzado de seguridad. No eliminan el peligro: solo protegen si se usan bien. Deben ser adecuados al riesgo, de la talla correcta, estar en buen estado, cumplir la norma vigente y usarse con capacitación. Quién los entrega, cómo se reponen y cuáles se exigen se define por la norma vigente y la empresa; consúltalo. Si un EPP molesta o no calza, se avisa para revisar la talla o el modelo, sin dejar de usarlo.",
        "Un EPP no reemplaza las otras medidas: se usa junto con ellas, no en lugar de ellas." + AVISO + LIM,
    ],
    vocab=[("jerarquía de controles", "orden de medidas de la más efectiva a la menos efectiva para reducir un riesgo"), ("eliminación", "quitar el peligro por completo"), ("sustitución", "reemplazar algo peligroso por algo menos peligroso"), ("control de ingeniería", "medida que aísla o encierra el peligro"), ("control administrativo", "medida de organización, como turnos, capacitación y señalización"), ("EPP", "elemento de protección personal: equipo que protege a la persona"), ("capacitación", "formación para realizar una tarea de forma segura")],
    worked=[
        ("Clasificar una medida", "Una empresa de ejemplo instala una barrera fija que impide acercarse a una zona peligrosa. ¿Qué tipo de medida es?", ["La barrera aísla el peligro.", "Es un control de ingeniería."], "Control de ingeniería"),
        ("Calcular exposición", "Una persona de ejemplo estaba expuesta a un riesgo 6 horas al día y, con rotación, queda en 2 horas. ¿Cuántas horas menos al día?", ["Se resta la nueva exposición a la anterior.", "6 − 2 = 4."], "4 horas menos"),
    ],
    mistakes=[("Entregar solo EPP y no hacer nada más.", "El EPP es la medida menos efectiva; el peligro sigue existiendo.", "Considera primero eliminar, sustituir o aislar el peligro."),
              ("Usar un EPP roto o de otra talla «porque es lo que hay».", "No protege bien y puede dar una falsa sensación de seguridad.", "Avisa para cambiarlo por uno adecuado y en buen estado.")],
    T=[
        ("abc", "En prevención de riesgos: ¿qué es la jerarquía de controles?", "Un orden de medidas, de las más efectivas a las menos efectivas, para reducir un riesgo", "Un listado de las personas que mandan en la empresa", "El orden en que se entregan los EPP", "La jerarquía ordena las medidas según su efectividad para controlar un riesgo."),
        ("abc", "{F} ¿Cuál es la medida más efectiva de la ficha?", "La A: eliminar la tarea ruidosa", "La E: entregar protectores auditivos", "La D: rotar al personal", "Eliminar el peligro es la medida de mayor efectividad."),
        ("abc", "{F} ¿Cuál es el último recurso en la jerarquía?", "La E: el EPP", "La A: la eliminación", "La C: el control de ingeniería", "El EPP protege a la persona, pero deja el peligro en su lugar."),
        ("abc", "{F} ¿Qué tipo de medida es la C?", "Un control de ingeniería", "Un control administrativo", "Un EPP", "La cubierta aísla la fuente de ruido, lo que corresponde a ingeniería."),
        ("abc", "{F} ¿Qué tipo de medida es la D?", "Un control administrativo", "Una sustitución", "Un control de ingeniería", "Rotar al personal, capacitar y señalizar son medidas de organización."),
        ("abc", "¿Por qué el EPP es el último recurso?", "Porque no elimina el peligro: solo protege si se usa bien", "Porque es muy caro para la empresa", "Porque es opcional para los trabajadores", "El peligro sigue presente, y el EPP depende del uso correcto."),
        ("=", "Una persona de ejemplo estaba expuesta a un ruido intenso 8 horas al día. Con rotación, queda en 2 horas al día. ¿Cuántas horas menos de exposición tiene a la semana, de 5 días?", "(8-2)*5", "Se calcula la reducción diaria y se multiplica por los cinco días.", " horas"),
        ("=", "Una empresa de ejemplo cambia los protectores de sus 25 trabajadores cada 3 meses, a razón de un par por persona. ¿Cuántos pares necesita al año?", "25*(12//3)", "Se calcula cuántos cambios hay al año y se multiplican por los trabajadores.", " pares"),
        ("abc", "¿Qué característica debe tener un EPP?", "Ser adecuado al riesgo, de la talla correcta y estar en buen estado", "Ser el más económico", "Verse bien aunque no calce", "Un EPP solo protege si es adecuado, calza y está en buen estado."),
        ("abc", "{F} La empresa solo entrega protectores auditivos (E) y no hace nada más. ¿Qué observación corresponde?", "Es la medida menos efectiva; conviene considerar eliminar, sustituir o aislar la fuente de ruido", "Está bien, porque con los protectores el ruido desaparece", "Es mejor retirar los protectores", "El ruido sigue existiendo; las medidas superiores en la jerarquía son más efectivas."),
        ("abc", "Un trabajador de una obra de ejemplo no usa el casco porque le aprieta. ¿Qué corresponde?", "Avisar a su jefatura para revisar la talla o el modelo, y no trabajar sin él mientras tanto", "Dejar de usarlo porque molesta", "Usarlo suelto para que no apriete", "Si un EPP no calza, se avisa para cambiarlo, pero no se prescinde de él."),
        ("abc", "Unos protectores de ejemplo se comparten entre varios trabajadores sin limpieza ni revisión. ¿Qué observación corresponde?", "Los EPP se usan según las instrucciones de limpieza y revisión, y se evita compartirlos si no corresponde", "Compartir EPP ahorra dinero y siempre es seguro", "Revisar un EPP es innecesario", "El estado e higiene de un EPP afectan su protección y la salud de quien lo usa."),
        ("=", "Un casco de ejemplo se usa durante 24 meses y se revisa cada 6 meses. ¿Cuántas revisiones se hacen en ese tiempo?", "24//6", "Se divide el período de uso entre el intervalo de revisión.", " revisiones"),
    ],
    ctx=("abc", "{F} El jefe del taller dice que como ya entregó protectores no hace falta mejorar nada más. Un trabajador propone buscar una máquina menos ruidosa. ¿Qué es lo más acertado?", "Evaluar la sustitución de la máquina, porque es una medida más efectiva que solo entregar EPP", "Descartar la idea porque es costosa", "Dejar solo los protectores", "La sustitución está más arriba en la jerarquía y reduce el ruido en su origen."),
    sc=[
        ("En prevención de riesgos: ¿qué medida es la más efectiva?", "Eliminar el peligro", "Si el peligro no existe, no hay riesgo."),
        ("¿Qué es un control administrativo?", "Una medida de organización, como turnos y capacitación", "Cambia la forma de trabajar y no el peligro."),
        ("¿Qué haces si tu EPP no calza?", "Aviso para cambiarlo", "Un EPP que no calza no protege bien."),
    ],
    op=("Caso de ejemplo. En una panadería ficticia hay riesgo por superficie caliente en un mesón de trabajo (solo concepto). La jefa propone cuatro ideas: (1) usar una cubierta que aísle la zona, (2) rotar al personal, (3) entregar guantes y capacitar, (4) reemplazar la superficie por una que no se caliente tanto. "
        "Escribe: (1) qué tipo de medida es cada idea, (2) en qué orden de efectividad las pondrías, (3) qué características debe tener el EPP y (4) qué NO harías sin instructor ni autorización.",
        "(1) 1: control de ingeniería; 2: control administrativo; 3: EPP junto con capacitación; 4: sustitución. (2) 4 (sustitución), 1 (ingeniería), 2 (administrativo), 3 (EPP). (3) Adecuado al riesgo, de la talla correcta, en buen estado, con capacitación y según la norma vigente. (4) No manipularía equipos ni superficies calientes sin instructor, capacitación ni autorización.",
        ["clasifica las medidas", "las ordena por efectividad", "describe características del EPP", "reconoce lo que no hay que hacer sin autorización"],
        ["hoja con cuatro respuestas"],
        ["poner el EPP como primera medida", "olvidar la capacitación", "proponer manipular equipos sin autorización"],
        "Pregunta: «¿qué pasaría si solo se usan guantes?». Debe decir que el peligro sigue y que los guantes no bastan."),
    reinforce="Elige un riesgo de tu especialidad y propone una medida para cada nivel de la jerarquía, sin describir procedimientos.",
    extend="Explica con un ejemplo por qué eliminar un peligro es mejor que protegerse de él.",
)

# ============================================================ OAG-11, clase 3
F = ("Ficha 43 (señales y matriz de ejemplo). Señales: círculo con borde rojo y una barra = prohibición; círculo azul = obligación; triángulo amarillo = advertencia de peligro; rectángulo verde = emergencia o salvamento (salidas, primeros auxilios); color rojo = equipos contra incendio. "
     "Matriz de ejemplo: nivel de riesgo = probabilidad (1 baja, 2 media, 3 alta) × consecuencia (1 leve, 2 seria, 3 grave). Niveles de ejemplo: 1 a 2 = bajo; 3 a 4 = medio; 6 a 9 = alto. "
     "Situaciones: S1, piso mojado en un pasillo (probabilidad 3, consecuencia 1); S2, cajas altas inestables (probabilidad 2, consecuencia 3); S3, un tomacorriente flojo (probabilidad 1, consecuencia 2).")
build(
    G11, 3, F,
    use="Aprenderé a leer señales de seguridad y etiquetas, y a usar una matriz simple de riesgo para decidir qué situación atender primero.",
    prior=["Conozco peligro, riesgo y jerarquía de controles.", "Sé multiplicar enteros.", "Sé leer un cuadro con niveles."],
    explain=[
        "La señalética de seguridad comunica riesgos y reglas con formas y colores. Las señales de prohibición tienen un círculo con borde rojo y una barra; las de obligación, un círculo azul; las de advertencia, un triángulo amarillo; las de emergencia o salvamento, un rectángulo verde; y el rojo también identifica los equipos contra incendio. Para que cumpla su función, una señal debe ser visible, entendible y estar en buen estado. Las normas vigentes de cada sector definen cuáles se usan.",
        "Los productos con riesgo traen etiquetas y pictogramas de advertencia, y una hoja de datos de seguridad con información sobre su manejo. Se leen antes de usar el producto; si algo no se entiende, se pregunta a la jefatura o al instructor. Para priorizar riesgos se puede usar una matriz simple: se multiplica la probabilidad por la consecuencia para obtener un nivel, y se atiende primero lo que tiene nivel alto. El nivel orienta la prioridad, pero igual se corrige todo riesgo que se detecte.",
        "Los valores de la matriz de esta ficha son de ejemplo; cada empresa define los suyos según la norma vigente." + AVISO + LIM,
    ],
    vocab=[("señalética", "conjunto de señales que comunican riesgos y reglas con formas y colores"), ("prohibición", "señal que indica lo que no se debe hacer"), ("obligación", "señal que indica lo que se debe hacer o usar"), ("pictograma", "dibujo que comunica una advertencia"), ("hoja de datos de seguridad", "documento con información sobre un producto y cómo manejarlo con seguridad"), ("matriz de riesgo", "cuadro que multiplica probabilidad por consecuencia para priorizar")],
    worked=[
        ("Leer una señal", "Una señal de ejemplo es un círculo azul con el dibujo de un casco. ¿Qué indica?", ["El círculo azul es una obligación.", "Indica que se debe usar el casco."], "Obligación de usar casco"),
        ("Calcular un nivel", "Una situación de ejemplo tiene probabilidad 3 y consecuencia 2. ¿Qué nivel de riesgo tiene?", ["Se multiplican probabilidad y consecuencia.", "3 × 2 = 6, que es nivel alto en la matriz de ejemplo."], "Nivel 6, alto"),
    ],
    mistakes=[("Quitar un cartel de advertencia porque «afea» el lugar.", "Sin la señal, las personas no conocen el peligro y pueden accidentarse.", "Mantén las señales visibles y en buen estado."),
              ("Ignorar un pictograma que no se conoce.", "Puede advertir de un peligro importante.", "Pregunta a la jefatura o al instructor y lee la hoja de datos de seguridad.")],
    T=[
        ("abc", "{F} ¿Qué indica un círculo azul?", "Una obligación", "Una prohibición", "Una advertencia", "El círculo azul se usa en señales de obligación, como usar un equipo de protección."),
        ("abc", "{F} ¿Qué indica un círculo con borde rojo y una barra?", "Una prohibición", "Una obligación", "Una emergencia", "El borde rojo con barra señala algo que no se debe hacer."),
        ("abc", "{F} ¿Qué indica un triángulo amarillo?", "Una advertencia de peligro", "Una prohibición", "Una salida de emergencia", "El triángulo amarillo advierte de un peligro."),
        ("abc", "{F} ¿Qué señal usarías para indicar una salida de emergencia?", "Un rectángulo verde", "Un círculo azul", "Un triángulo amarillo", "El verde se usa para emergencia y salvamento."),
        ("=", "{F} ¿Qué nivel de riesgo tiene S1, el piso mojado?", "3*1", "Se multiplican la probabilidad y la consecuencia de S1.", " (nivel)"),
        ("=", "{F} ¿Qué nivel de riesgo tiene S2, las cajas altas inestables?", "2*3", "Se multiplican la probabilidad y la consecuencia de S2.", " (nivel)"),
        ("=", "{F} ¿Qué nivel de riesgo tiene S3, el tomacorriente flojo?", "1*2", "Se multiplican la probabilidad y la consecuencia de S3.", " (nivel)"),
        ("abc", "{F} Según la matriz, ¿qué situación se debe atender primero?", "S2, porque tiene nivel alto", "S1, porque es la más probable", "S3, porque es la más fácil", "El mayor nivel de la matriz es el de S2."),
        ("abc", "En la etiqueta de un producto de ejemplo aparece un pictograma que no conoces. ¿Qué haces antes de usarlo?", "Pregunto a la jefatura o al instructor y reviso la hoja de datos de seguridad", "Lo uso igual, porque nadie lo ha reclamado", "Lo guardo sin leer nada más", "Un pictograma desconocido se consulta antes de usar el producto."),
        ("abc", "{F} Un jefe dice: «S1 es nivel medio, no hace falta corregirla». ¿Qué respuesta es correcta?", "El nivel orienta la prioridad, pero igual se corrige con una medida simple, como señalizar y avisar", "Tiene razón: los riesgos medios no se corrigen", "Hay que corregir solo los riesgos bajos", "Todo riesgo detectado se corrige; el nivel solo indica el orden de atención."),
        ("abc", "¿Qué condiciones debe cumplir una señal de seguridad?", "Ser visible, entendible y estar en buen estado", "Verse bonita, aunque no se entienda", "Estar escondida para no molestar", "Una señal cumple su función solo si las personas la ven y la comprenden."),
        ("abc", "{F} Un compañero quiere sacar un cartel de prohibición porque «afea» la bodega. ¿Qué corresponde?", "No quitarlo y explicar que protege a las personas", "Sacarlo para mejorar el aspecto", "Cambiarlo por un cartel sin dibujo", "La señal comunica un riesgo y su retiro deja a las personas sin información."),
        ("=", "{F} Si con una medida la probabilidad de S2 baja de 2 a 1, ¿cuántos puntos baja su nivel?", "2*3-1*3", "Se calcula el nivel antes y después de la medida y se restan.", " puntos"),
    ],
    ctx=("abc", "{F} En una bodega de ejemplo se detectan S1, S2 y S3. Solo hay tiempo para atender una antes del turno de la tarde. ¿Cuál se atiende y qué se hace con las demás?", "Se atiende S2 por su nivel alto y se señalizan y avisan las otras dos para corregirlas después", "Se atiende S3 y se ignoran las otras", "No se atiende ninguna, porque no hay tiempo", "El nivel alto se atiende primero; las demás se señalizan y se programan."),
    sc=[
        ("En señalética de ejemplo: ¿qué significa un triángulo amarillo?", "Advertencia de peligro", "El amarillo y el triángulo advierten de peligros."),
        ("¿Cómo se calcula el nivel en una matriz simple?", "Probabilidad por consecuencia", "El producto de ambos da el nivel de riesgo."),
        ("¿Qué haces si un pictograma no lo conoces?", "Pregunto antes de usar el producto", "Un símbolo desconocido no se supone, se consulta."),
    ],
    op=("Caso de ejemplo. En un taller ficticio de confección se observan tres situaciones: (A) una alfombra suelta en la entrada (probabilidad 3, consecuencia 2); (B) una estantería sin fijar con cajas pesadas arriba (probabilidad 2, consecuencia 3); (C) una puerta de emergencia bloqueada por cajas (probabilidad 1, consecuencia 3). Matriz de ejemplo: 1 a 2 bajo, 3 a 4 medio, 6 a 9 alto. "
        "Escribe: (1) el nivel de cada situación, (2) el orden en que las atenderías, (3) una señal que usarías en cada una y su color, (4) qué NO harías por tu cuenta.",
        "(1) A: 3 × 2 = 6, alto. B: 2 × 3 = 6, alto. C: 1 × 3 = 3, medio. (2) A y B primero (empatan en nivel alto; se avisa y se atienden a la vez según los responsables), luego C. (3) A: triángulo amarillo de advertencia; B: círculo azul si hay una obligación o triángulo amarillo de advertencia; C: señal verde de salida de emergencia visible y despejada. (4) No movería muebles pesados ni cargas sin estar autorizado y capacitado; avisaría a la jefatura.",
        ["calcula los niveles", "ordena según la matriz", "elige señales", "reconoce lo que no se hace sin autorización"],
        ["hoja con cuatro respuestas"],
        ["no multiplicar bien", "ignorar la puerta de emergencia", "mover cargas pesadas sin autorización"],
        "Pregunta: «¿qué haces si no tienes tiempo para atender las tres?». Debe decir que señaliza, avisa y deja programadas las correcciones según el nivel."),
    reinforce="Dibuja las cuatro señales (prohibición, obligación, advertencia y emergencia) con su forma y color y escribe un ejemplo de cada una.",
    extend="Explica por qué una matriz de riesgo ayuda a priorizar, pero no reemplaza el criterio ni la norma vigente.",
)

# ============================================================ OAG-11, clase 4
F = ("Ficha 44 (registro de incidentes y accidentes de una bodega ficticia, cuatro trimestres; cifras inventadas). Trimestre 1: 10 incidentes y 2 accidentes con lesión leve. Trimestre 2: 8 incidentes y 1 accidente. Trimestre 3: 5 incidentes y 0 accidentes. Trimestre 4: 4 incidentes y 0 accidentes. "
     "Causas más repetidas (de ejemplo): pasillos con cajas en el suelo, 11 casos; falta de señalización, 6 casos; uso incorrecto de elementos de protección, 4 casos. Medidas aplicadas desde el trimestre 2: orden y limpieza diaria, señalización de pasillos y capacitación del personal.")
build(
    G11, 4, F,
    use="Aprenderé a analizar un registro de incidentes con datos, a proponer medidas según la jerarquía de controles y a conocer los deberes y derechos en seguridad.",
    prior=["Conozco peligro, riesgo, EPP y señales.", "Sé calcular cuántos por cada 100.", "Sé sumar y restar."],
    explain=[
        "El registro de incidentes y accidentes sirve para aprender: muestra cuántos ocurrieron, dónde, por qué y si las medidas funcionan. Se analiza con tres pasos: contar los eventos, buscar las causas que más se repiten y comprobar si bajaron después de aplicar medidas. Luego se propone un plan de acción con medidas de la jerarquía de controles, responsables y fechas.",
        "Los trabajadores tienen deberes en seguridad: cumplir las normas, usar los EPP, participar en las capacitaciones y avisar de las condiciones inseguras, los incidentes y los accidentes, incluso los leves. Según la norma vigente, algunas empresas deben tener un comité paritario u otras instancias de prevención; consulta a tu jefatura o a la entidad fiscalizadora de tu sector qué corresponde a tu empresa. Las cifras de esta ficha son de ejemplo y no representan datos reales de accidentes.",
        "La seguridad también incluye cuidar la salud física y mental: pausas, buena postura y buen trato previenen enfermedades ocupacionales." + AVISO + LIM,
    ],
    vocab=[("registro de incidentes", "documento donde se anotan los incidentes y accidentes"), ("causa repetida", "causa que aparece en muchos casos"), ("plan de acción", "medidas, responsables y fechas para corregir una situación"), ("tendencia", "forma en que cambian los datos con el tiempo"), ("comité paritario", "instancia con representantes de la empresa y de los trabajadores para promover la prevención"), ("reporte", "aviso por escrito de un incidente o una condición insegura")],
    worked=[
        ("Contar eventos", "Una bodega de ejemplo registró 6 incidentes en un trimestre y 4 en el siguiente. ¿Cuántos suman?", ["Se suman los dos trimestres.", "6 + 4 = 10."], "10 incidentes"),
        ("Medir la baja", "Los incidentes de una empresa de ejemplo bajaron de 20 a 15. ¿Cuántos por cada 100 bajaron?", ["La baja es 20 − 15 = 5.", "5 × 100 ÷ 20 = 25."], "25 por cada 100"),
    ],
    mistakes=[("No informar un golpe leve para no «ensuciar» el registro.", "Se pierde la oportunidad de atender a la persona y de corregir la causa.", "Informa siempre, aunque sea leve."),
              ("Dejar de registrar porque «ya bajaron los incidentes».", "Sin registro no se sabe si los resultados se mantienen.", "Sigue registrando para detectar si vuelven a subir.")],
    T=[
        ("=", "{F} ¿Cuántos incidentes se registraron en total en los cuatro trimestres?", "10+8+5+4", "Se suman los incidentes de los cuatro trimestres.", " incidentes"),
        ("=", "{F} ¿Cuántos accidentes se registraron en total?", "2+1+0+0", "Se suman los accidentes de los cuatro trimestres.", " accidentes"),
        ("abc", "{F} ¿Cuál es la causa que más se repitió?", "Pasillos con cajas en el suelo", "Falta de señalización", "Uso incorrecto de elementos de protección", "La ficha indica 11 casos de pasillos con cajas en el suelo, la cifra más alta."),
        ("=", "{F} ¿Cuántos incidentes menos hubo en el trimestre 4 que en el trimestre 1?", "10-4", "Al número del trimestre 1 se le resta el del trimestre 4.", " incidentes"),
        ("=", "{F} ¿Cuántos incidentes por cada 100 bajaron entre el trimestre 1 y el trimestre 4?", "(10-4)*100//10", "Se calcula la baja, se multiplica por 100 y se divide entre los del trimestre 1.", " por cada 100"),
        ("abc", "{F} ¿Qué tipo de medidas se aplicaron desde el trimestre 2?", "Controles administrativos y de orden, que son menos efectivas que eliminar el peligro", "Eliminación total de todos los peligros", "Solo elementos de protección personal", "Orden, señalización y capacitación son medidas administrativas."),
        ("=", "{F} ¿Cuántos casos de causas se contaron en total?", "11+6+4", "Se suman los casos de las tres causas más repetidas.", " casos"),
        ("abc", "{F} ¿Qué medida adicional sería más efectiva para los pasillos con cajas en el suelo?", "Rediseñar el almacenamiento para que cada caja tenga su lugar y no queden cajas en el suelo", "Pedir al personal que tenga más cuidado", "Colocar solo un cartel", "Eliminar la causa en el origen es más efectivo que depender del cuidado de las personas."),
        ("=", "{F} ¿Cuántos incidentes sumaron los dos últimos trimestres?", "5+4", "Se suman los incidentes del trimestre 3 y del trimestre 4.", " incidentes"),
        ("abc", "{F} Un jefe dice: «Ya bajaron los incidentes, dejemos de registrar». ¿Qué respuesta es correcta?", "Registrar permite mantener los resultados y detectar si vuelven a subir", "Tiene razón: registrar ya no sirve", "El registro solo sirve cuando hay accidentes graves", "Los datos permiten comprobar que las mejoras se sostienen."),
        ("abc", "Un trabajador se golpea levemente la mano y no lo informa. ¿Qué corresponde?", "Informar siempre, para atenderlo y corregir la causa", "Callar, porque fue leve", "Informar solo si le duele varios días", "Los hechos leves también se reportan porque advierten de riesgos."),
        ("abc", "{F} Un trabajador ve cajas en el suelo del pasillo. ¿Qué hace?", "Avisa y, si está dentro de sus funciones y sin riesgo, ayuda a ordenar", "Pasa por encima para no demorar", "Las deja porque otro las ordenará", "Avisar y ayudar dentro de lo permitido es parte del deber de prevención."),
        ("=", "{F} Si la meta es que los incidentes de un trimestre sean una cuarta parte de los del trimestre 2, ¿cuántos incidentes serían?", "8//4", "Se divide entre 4 los incidentes del trimestre 2.", " incidentes"),
    ],
    ctx=("abc", "{F} En el trimestre 5 sube a 7 el número de incidentes y una trabajadora nota que el orden diario dejó de hacerse. ¿Qué propone?", "Retomar el orden diario con responsables y fechas, y revisar el registro para confirmar la causa", "Culpar a una persona y sancionarla", "Dejar de contar incidentes", "Un plan con responsables y registro permite corregir sin culpar a una persona."),
    sc=[
        ("En prevención de riesgos: ¿para qué sirve el registro de incidentes?", "Para aprender de lo ocurrido y corregir causas", "Muestra qué pasa, dónde y por qué."),
        ("¿Qué haces ante un incidente leve?", "Lo informo igual", "Los hechos leves advierten de riesgos mayores."),
        ("¿Quién fiscaliza las normas de seguridad de tu sector?", "La entidad fiscalizadora correspondiente", "Cada sector tiene su entidad y su norma vigente."),
    ],
    op=("Caso de ejemplo. Un restaurante ficticio registra: Mes 1, 8 incidentes y 1 accidente; Mes 2, 6 incidentes y 1 accidente; Mes 3, 4 incidentes y 0 accidentes. Causas repetidas: pisos mojados sin aviso (9 casos), mesones desordenados (5 casos), falta de capacitación de personal nuevo (3 casos). Medidas aplicadas desde el mes 2: señal de piso mojado y capacitación a los nuevos. "
        "Escribe: (1) el total de incidentes, (2) cuántos por cada 100 bajaron entre el mes 1 y el mes 3, (3) la causa más repetida, (4) una medida superior en la jerarquía para esa causa y un responsable, (5) por qué se informa también un incidente leve.",
        "(1) 8 + 6 + 4 = 18. (2) (8 − 4) × 100 ÷ 8 = 50 por cada 100. (3) Pisos mojados sin aviso. (4) Rediseñar el flujo para evitar derrames en pasillos o agregar un tapete; responsable: encargado de sala, con fecha de ejemplo. (5) Porque advierte de un riesgo y permite corregirlo antes de un accidente.",
        ["suma los incidentes", "calcula la baja", "identifica la causa", "propone una medida y un responsable", "explica por qué se reportan los incidentes leves"],
        ["hoja con cinco respuestas"],
        ["no sumar bien", "proponer solo carteles", "culpar a una persona"],
        "Pregunta: «¿qué harías si el piso mojado se debe a una gotera?». Debe decir que avisa a mantención o a quien corresponda y no repara por su cuenta."),
    reinforce="Escribe tres datos de un registro de incidentes de ejemplo y una medida por cada nivel de la jerarquía.",
    extend="Explica con un ejemplo por qué un plan de acción necesita responsables y fechas.",
)

# ============================================================ OAG-12, clase 1
F = ("Ficha 45 (presupuesto mensual de ejemplo de Camila, auxiliar de bodega en una empresa ficticia). Ingresos: $450.000. Gastos fijos: arriendo de una pieza $150.000, transporte $45.000, cuenta del celular $15.000. "
     "Gastos variables: alimentación $110.000, ocio $40.000, ropa $20.000. Meta de ahorro de ejemplo: juntar $240.000 para un fondo de emergencia. Cuenta de ahorro de ejemplo: paga 1 de cada 100 pesos por mes sobre el saldo (tasa de ejemplo).")
build(
    G12, 1, F,
    use="Aprenderé a armar un presupuesto, a distinguir gastos fijos y variables, y a calcular cuánto y en cuánto tiempo se puede ahorrar para una meta.",
    prior=["Sé sumar, restar y multiplicar cifras grandes.", "Sé calcular cuántos por cada 100.", "Conozco el flujo de caja de un negocio."],
    explain=[
        "El presupuesto es el plan de ingresos y gastos de un período. Los ingresos son el dinero que se recibe. Los gastos fijos se repiten cada mes con un valor casi igual, como el arriendo o el transporte; los gastos variables cambian, como la alimentación, el ocio o la ropa. Lo que queda después de restar los gastos a los ingresos es lo que se puede ahorrar. Ahorrar es guardar parte del dinero para usarlo en el futuro.",
        "Conviene fijar metas de ahorro con un monto y un plazo, y un fondo de emergencia para imprevistos, como una enfermedad o la pérdida de un trabajo. Una buena práctica es apartar primero la cantidad que se quiere ahorrar y luego gastar el resto, porque «lo que sobre» muchas veces no sobra. El interés es el dinero que una institución paga por guardar tus ahorros; la tasa de interés es el porcentaje que se paga. En el interés simple, el interés se calcula siempre sobre el mismo monto: interés = monto × tasa × tiempo.",
        "Distinguir entre necesidades y deseos ayuda a decidir en qué gastar y en qué no." + FIN + LIM,
    ],
    vocab=[("presupuesto", "plan de ingresos y gastos de un período"), ("gasto fijo", "gasto que se repite cada mes con un valor casi igual"), ("gasto variable", "gasto que cambia de un mes a otro"), ("ahorro", "parte del dinero que se guarda para el futuro"), ("fondo de emergencia", "ahorro reservado para imprevistos"), ("interés", "dinero que paga o cobra una institución por el uso del dinero"), ("tasa de interés", "porcentaje con que se calcula el interés")],
    worked=[
        ("Calcular el ahorro posible", "Una persona de ejemplo gana $300.000 y gasta $240.000. ¿Cuánto puede ahorrar al mes?", ["Se restan los gastos a los ingresos.", "300.000 − 240.000 = 60.000."], "$60.000"),
        ("Calcular un interés simple", "Una cuenta de ejemplo paga 2 de cada 100 pesos al año. ¿Cuánto interés da un ahorro de $50.000 en un año?", ["Se calcula 2 de cada 100 sobre 50.000.", "50.000 × 2 ÷ 100 = 1.000."], "$1.000"),
    ],
    mistakes=[("Pensar «ahorraré lo que sobre a fin de mes».", "Rara vez sobra algo si no se aparta primero.", "Aparta el monto de ahorro apenas recibes el ingreso."),
              ("Usar el fondo de emergencia para un gusto que se puede postergar.", "Cuando llegue una emergencia no habrá con qué enfrentarla.", "Define metas distintas para deseos y para emergencias.")],
    T=[
        ("abc", "En finanzas personales: ¿qué es ahorrar?", "Guardar parte del dinero para usarlo en el futuro", "Gastar todo el dinero en lo que se necesita", "Pedir dinero prestado para comprar", "Ahorrar es apartar dinero hoy para necesidades o metas futuras."),
        ("=", "{F} ¿Cuánto suman los gastos fijos de Camila?", "150000+45000+15000", "Se suman el arriendo, el transporte y el celular.", " pesos"),
        ("=", "{F} ¿Cuánto suman los gastos variables de Camila?", "110000+40000+20000", "Se suman la alimentación, el ocio y la ropa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos puede ahorrar Camila al mes, después de todos los gastos?", "450000-(150000+45000+15000)-(110000+40000+20000)", "Se restan los gastos fijos y variables a los ingresos.", " pesos"),
        ("abc", "{F} ¿Cuál es un gasto variable de Camila?", "El ocio", "El arriendo", "El transporte", "El ocio cambia de mes a mes; el arriendo y el transporte se repiten."),
        ("=", "{F} Si Camila reduce el ocio en $10.000, ¿en cuántos meses reúne la meta de $240.000?", "240000//(450000-(150000+45000+15000)-(110000+40000+20000)+10000)", "Se calcula el nuevo ahorro mensual y se divide la meta entre ese monto.", " meses"),
        ("=", "{F} Si deposita $70.000 en la cuenta de ahorro, ¿cuánto interés gana en un mes con la tasa de ejemplo?", "70000*1//100", "Se calcula 1 de cada 100 sobre el monto depositado.", " pesos"),
        ("=", "{F} Si ahorra $70.000 al mes durante 6 meses, ¿cuánto junta sin contar intereses?", "70000*6", "Se multiplica el ahorro mensual por los meses.", " pesos"),
        ("abc", "¿Para qué sirve un fondo de emergencia?", "Para enfrentar imprevistos sin endeudarse", "Para comprar cosas que están de oferta", "Para pagar las vacaciones todos los años", "El fondo de emergencia se reserva para eventos inesperados."),
        ("abc", "{F} Camila gasta todo y piensa ahorrar «lo que sobre». ¿Qué problema tiene esa idea?", "Rara vez sobra algo; conviene apartar primero un monto fijo", "Ninguno, porque siempre sobra algo", "Que le dará intereses negativos", "Si no se aparta primero, el ahorro depende de lo que quede, que suele ser poco."),
        ("abc", "{F} Una amiga le propone usar el dinero de la meta de emergencia para un viaje. ¿Qué conviene?", "Distinguir entre emergencia y deseo y fijar una meta distinta para el viaje", "Usar el fondo, porque un viaje es importante", "Dejar de ahorrar", "El fondo de emergencia debe protegerse para su propósito."),
        ("abc", "Un joven recibe un ingreso extra por un trabajo temporal. ¿Cuál es una decisión financiera prudente?", "Definir cuánto ahorrar y cuánto gastar antes de gastar", "Gastar todo de inmediato en lo que quiera", "Prestarlo a cualquiera que lo pida", "Planificar el uso del ingreso extra ayuda a lograr metas."),
        ("=", "{F} Si el ahorro mensual de $70.000 se mantiene todo el año, ¿cuánto junta Camila en 12 meses sin contar intereses?", "70000*12", "Se multiplica el ahorro mensual por los 12 meses.", " pesos"),
    ],
    ctx=("abc", "{F} Camila quiere comprar un celular nuevo de $240.000, aunque el actual funciona. ¿Cómo decide mejor?", "Revisa su presupuesto, distingue entre necesidad y deseo, y fija una meta de ahorro con plazo", "Se endeuda de inmediato sin mirar su presupuesto", "Usa el fondo de emergencia sin avisar a nadie", "Planificar y distinguir necesidad de deseo evita decisiones apuradas."),
    sc=[
        ("En finanzas personales: ¿qué es un gasto fijo?", "Uno que se repite cada mes con valor casi igual", "Permite planificar mejor el presupuesto de cada mes."),
        ("¿Cómo se calcula el ahorro posible?", "Ingresos menos gastos", "Lo que queda es lo que se puede ahorrar."),
        ("¿Qué es el interés?", "Dinero que se paga o se cobra por usar dinero", "Se calcula aplicando una tasa sobre el monto."),
    ],
    op=("Caso de ejemplo. Julián, ayudante de cocina en un casino ficticio, gana $400.000 al mes. Gastos fijos: arriendo $130.000 y transporte $40.000. Gastos variables: alimentación $90.000, ocio $50.000 y ropa $30.000. Quiere juntar $180.000 para sus estudios. "
        "Escribe: (1) sus gastos totales, (2) cuánto puede ahorrar al mes, (3) en cuántos meses junta la meta, (4) una decisión de gasto variable que cambiaría y cómo afectaría el plazo.",
        "(1) 130.000 + 40.000 + 90.000 + 50.000 + 30.000 = 340.000. (2) 400.000 − 340.000 = 60.000. (3) 180.000 ÷ 60.000 = 3 meses. (4) Si reduce el ocio en $30.000 (de $50.000 a $20.000), ahorra 90.000 al mes y junta la meta en 2 meses.",
        ["suma los gastos", "calcula el ahorro", "calcula los meses", "propone un ajuste y ve su efecto"],
        ["hoja con cuatro respuestas"],
        ["no sumar todos los gastos", "ignorar la meta", "proponer endeudarse"],
        "Pregunta: «¿qué pasa si el arriendo sube $20.000?». Debe notar que el ahorro baja a 40.000 y la meta tarda más."),
    reinforce="Haz un presupuesto de ejemplo con tres gastos fijos y tres variables y calcula cuánto se podría ahorrar.",
    extend="Explica por qué conviene apartar el ahorro primero y no esperar a ver qué sobra.",
)

# ============================================================ OAG-12, clase 2
F = ("Ficha 46 (conceptos con cifras de ejemplo; no son datos reales). Un trabajador de ejemplo gana $500.000 al mes. Cotización previsional de ejemplo: 10 de cada 100 pesos de su sueldo se destinan a su cuenta de ahorro para la pensión (el porcentaje real lo fija la norma vigente). "
     "Seguro de ejemplo contra robo para un taller: prima mensual $12.000; cobertura máxima $2.000.000; deducible $100.000 (la persona asegurada paga los primeros $100.000 de cada siniestro); exclusión: daños por mala conservación.")
build(
    G12, 2, F,
    use="Aprenderé qué es el ahorro previsional y cómo funcionan los seguros: prima, cobertura, deducible, siniestro y exclusiones, con cifras de ejemplo.",
    prior=["Conozco el presupuesto y el ahorro.", "Sé calcular partes de un total.", "Sé qué es un riesgo."],
    explain=[
        "El ahorro previsional es el dinero que se guarda durante la vida laboral para financiar la pensión cuando una persona deja de trabajar. Se forma con la cotización, que es una parte del sueldo que se destina a ese fin según la norma vigente. También existe el ahorro previsional voluntario, que la persona decide aportar además de lo obligatorio. Entender cuánto se ahorra y cómo se administra ayuda a planificar el futuro; las reglas y los porcentajes reales se consultan en fuentes oficiales.",
        "Un seguro es un contrato en que una persona o empresa paga una prima para que una aseguradora cubra, en parte o en todo, una pérdida si ocurre un siniestro (el hecho cubierto). La cobertura es lo que el seguro paga y hasta qué monto; el deducible es la parte que paga la persona asegurada en cada siniestro; las exclusiones son los casos que el seguro no cubre. Un seguro transfiere el riesgo de una pérdida grande a cambio de un pago menor y regular. Antes de contratar uno se lee la póliza completa y se consultan las dudas.",
        "En general, un seguro no es una inversión ni un ahorro: la prima no se recupera si no hay siniestro." + FIN + LIM,
    ],
    vocab=[("ahorro previsional", "dinero que se guarda durante la vida laboral para financiar la pensión"), ("cotización", "parte del sueldo que se destina al ahorro para la pensión, según la norma vigente"), ("pensión", "ingreso periódico que se recibe al dejar de trabajar"), ("seguro", "contrato que cubre una pérdida si ocurre un hecho previsto"), ("prima", "pago que se hace por un seguro"), ("cobertura", "lo que el seguro paga y hasta qué monto"), ("deducible", "parte de la pérdida que paga la persona asegurada")],
    worked=[
        ("Calcular una cotización de ejemplo", "Con una tasa de ejemplo de 10 de cada 100, un sueldo de $300.000 genera una cotización de ¿cuánto?", ["Se calcula 10 de cada 100 de 300.000.", "300.000 × 10 ÷ 100 = 30.000."], "$30.000"),
        ("Calcular lo que paga el seguro", "Un siniestro de ejemplo de $400.000 con un deducible de $50.000 y una cobertura que lo permite. ¿Cuánto paga la aseguradora?", ["Se resta el deducible a la pérdida.", "400.000 − 50.000 = 350.000."], "$350.000"),
    ],
    mistakes=[("Contratar un seguro sin leer la póliza.", "Puede tener exclusiones o un deducible que no se esperaban.", "Lee la póliza completa y pregunta las dudas por escrito."),
              ("Creer que el seguro es un ahorro que se recupera.", "La prima se paga por la cobertura, aunque no ocurra un siniestro.", "Distingue entre ahorro, seguro e inversión.")],
    T=[
        ("abc", "En previsión social: ¿qué es la cotización?", "Una parte del sueldo que se destina al ahorro para la pensión, según la norma vigente", "El sueldo completo que se recibe en el mes", "Un bono que entrega la empresa", "La cotización destina una parte del sueldo a la pensión."),
        ("=", "{F} ¿Cuántos pesos al mes se destinan a la cuenta de ahorro para la pensión, con la cotización de ejemplo?", "500000*10//100", "Se calcula 10 de cada 100 sobre el sueldo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se destinan en un año, con esa cotización de ejemplo?", "500000*10//100*12", "Se multiplica la cotización mensual por los 12 meses.", " pesos"),
        ("abc", "{F} ¿Qué es la prima del seguro?", "El pago que se hace por tener el seguro, aquí $12.000 al mes", "El monto máximo que paga el seguro", "La parte de la pérdida que paga la persona asegurada", "La prima es el precio periódico del seguro."),
        ("abc", "{F} ¿Qué es el deducible?", "La parte de cada siniestro que paga la persona asegurada, aquí $100.000", "El pago mensual del seguro", "El hecho cubierto, como un robo", "El deducible es la parte que asume el asegurado."),
        ("=", "{F} ¿Cuántos pesos paga el taller por la prima en un año?", "12000*12", "Se multiplica la prima mensual por 12 meses.", " pesos"),
        ("=", "{F} Hay un robo (siniestro) que causa una pérdida de $800.000. ¿Cuánto paga la aseguradora, considerando el deducible?", "800000-100000", "A la pérdida se le resta el deducible.", " pesos"),
        ("abc", "{F} Una pérdida del taller se debe a que unas máquinas se oxidaron por mala conservación. ¿Qué ocurre con el seguro?", "No la cubre, porque es una exclusión de la póliza", "La cubre completa", "La cubre con otro deducible", "La póliza dice que la mala conservación está excluida."),
        ("=", "{F} Un siniestro de $1.500.000 ocurre dentro de lo cubierto. ¿Cuánto paga la aseguradora, si la cobertura máxima lo permite?", "1500000-100000", "Se resta el deducible a la pérdida, siempre que no pase la cobertura máxima.", " pesos"),
        ("abc", "{F} Un taller no contrata seguro porque «nunca le ha pasado nada». ¿Qué observación corresponde?", "El seguro transfiere el riesgo de una pérdida grande a cambio de una prima pequeña; hay que evaluar ese riesgo", "No hay riesgo mientras no haya ocurrido", "El seguro siempre conviene", "La decisión depende del riesgo, de la prima y de la capacidad de asumir una pérdida."),
        ("abc", "¿Qué conviene hacer antes de contratar un seguro?", "Leer la póliza completa: cobertura, deducible, exclusiones y prima, y consultar las dudas", "Firmar rápido para no perder la oferta", "Contratar el que recomiende la primera persona que ofrezca", "Entender las condiciones evita sorpresas en el momento del siniestro."),
        ("abc", "{F} Un empleador dice a un trabajador que «no importa» que se cotice. ¿Qué respuesta es adecuada?", "La cotización forma parte de su ahorro para la pensión; las obligaciones se consultan en fuentes oficiales", "Tiene razón: la pensión llega igual", "Solo importa si el trabajador es mayor", "Las obligaciones previsionales se rigen por la norma vigente, no por la opinión de una persona."),
        ("=", "{F} Si el taller paga la prima durante 5 años sin siniestros, ¿cuánto habrá pagado en total?", "12000*12*5", "Se multiplica la prima anual por los años.", " pesos"),
    ],
    ctx=("abc", "{F} Dos socios discuten: uno quiere cancelar el seguro «para ahorrar» y el otro quiere mantenerlo. ¿Cómo deciden mejor?", "Comparan el costo de la prima con el tamaño de la pérdida posible y con lo que pueden asumir", "Lo deciden por sorteo", "Cancelan sin leer la póliza", "Una decisión informada compara costo, riesgo y capacidad de asumir la pérdida."),
    sc=[
        ("En seguros de ejemplo: ¿qué es la prima?", "El pago por tener el seguro", "Se paga aunque no ocurra un siniestro."),
        ("¿Qué es el deducible?", "La parte que paga la persona asegurada", "Se descuenta de lo que paga el seguro."),
        ("¿Dónde consultas las reglas de la cotización?", "En fuentes oficiales y la norma vigente", "Los porcentajes reales los fija la norma."),
    ],
    op=("Caso de ejemplo. Una peluquería ficticia contrata un seguro con prima de $9.000 al mes, cobertura máxima de $1.000.000 y deducible de $80.000. Excluye daños por uso indebido. Ocurre un robo con pérdida de $600.000. Un empleado de la peluquería gana $400.000 y su cotización de ejemplo es de 10 de cada 100. "
        "Escribe: (1) la prima anual, (2) cuánto paga la aseguradora por el robo, (3) cuánto paga la peluquería, (4) la cotización mensual de ejemplo del empleado, (5) por qué conviene leer la póliza.",
        "(1) 9.000 × 12 = 108.000. (2) 600.000 − 80.000 = 520.000. (3) 80.000. (4) 400.000 × 10 ÷ 100 = 40.000. (5) Para conocer la cobertura, el deducible y las exclusiones antes de contratar.",
        ["calcula la prima anual", "calcula lo que paga el seguro", "calcula el deducible", "calcula la cotización de ejemplo", "explica por qué leer la póliza"],
        ["hoja con cinco respuestas"],
        ["olvidar el deducible", "confundir prima con cobertura", "ignorar las exclusiones"],
        "Pregunta: «¿qué pasaría si la pérdida fuera de $1.500.000?». Debe decir que la cobertura máxima es de $1.000.000, así que el seguro no paga todo."),
    reinforce="Explica con tus palabras la diferencia entre prima, cobertura, deducible y exclusión, con un ejemplo inventado.",
    extend="Explica por qué un seguro no es lo mismo que un ahorro.",
)

# ============================================================ OAG-12, clase 3
F = ("Ficha 47 (dos créditos de ejemplo; tasas y montos inventados). Crédito A: monto $600.000 en 6 cuotas mensuales; interés total de ejemplo $60.000. Crédito B: monto $600.000 en 12 cuotas mensuales; interés total de ejemplo $132.000. "
     "Cuota = (monto + interés total) ÷ número de cuotas. El CAE (costo anual equivalente) es un indicador que expresa el costo total de un crédito en un año, para poder comparar créditos; en esta ficha no se calcula. Ingreso mensual de la persona de ejemplo: $450.000.")
build(
    G12, 3, F,
    use="Aprenderé qué es el endeudamiento, cómo se calculan las cuotas con datos de ejemplo, qué es el CAE y cuáles son los riesgos y oportunidades de un crédito.",
    prior=["Conozco el interés y la tasa.", "Sé dividir y sumar cifras grandes.", "Conozco el presupuesto."],
    explain=[
        "Un crédito es dinero que se pide prestado y se devuelve en cuotas, pagando además un interés. El monto es la cantidad prestada; el plazo, el tiempo para pagar; la tasa de interés, el porcentaje que se cobra por el préstamo; y la cuota, el pago periódico. En el ejemplo de esta clase, cuota = (monto + interés total) ÷ número de cuotas. El costo total del crédito es lo que se paga en total: monto más intereses y otros cobros.",
        "Para comparar créditos no basta mirar la cuota: una cuota baja puede significar un plazo largo y más intereses. El CAE (costo anual equivalente) resume el costo total de un crédito en un año y sirve para compararlos. También se pregunta por otros costos, como seguros asociados, y por las condiciones de pago anticipado. La carga financiera es la parte del ingreso que se va en cuotas; si es alta, hay riesgo de sobreendeudamiento. La mora es el atraso en el pago, que puede generar cobros extra y afectar el historial de la persona.",
        "El crédito puede ser una oportunidad, por ejemplo para financiar estudios o una herramienta de trabajo, si se tiene capacidad de pago. Siempre se lee el contrato completo antes de firmar." + FIN + LIM,
    ],
    vocab=[("crédito", "dinero prestado que se devuelve en cuotas con interés"), ("cuota", "pago periódico de un crédito"), ("plazo", "tiempo para pagar un crédito"), ("CAE", "costo anual equivalente: indicador del costo total de un crédito en un año"), ("carga financiera", "parte del ingreso que se destina a pagar cuotas"), ("mora", "atraso en el pago de una cuota"), ("sobreendeudamiento", "deber más de lo que se puede pagar con los ingresos")],
    worked=[
        ("Calcular una cuota", "Un crédito de ejemplo de $300.000 tiene un interés total de $30.000 y se paga en 5 cuotas. ¿Cuál es la cuota?", ["Se suma el interés al monto.", "(300.000 + 30.000) ÷ 5 = 66.000."], "$66.000"),
        ("Costo total", "Con el mismo crédito, ¿cuánto se paga en total?", ["Se suma el monto y el interés.", "300.000 + 30.000 = 330.000."], "$330.000"),
    ],
    mistakes=[("Elegir el crédito solo porque tiene la cuota más baja.", "La cuota baja suele significar más plazo y más intereses totales.", "Compara el costo total o el CAE, además de la cuota."),
              ("Firmar un contrato de crédito sin leerlo completo.", "Puede incluir costos adicionales o cláusulas que no se conocían.", "Lee el contrato, pregunta lo que no entiendas y pide el CAE.")],
    T=[
        ("abc", "En finanzas personales: ¿qué es un crédito?", "Dinero prestado que se devuelve en cuotas con interés", "Dinero regalado por una institución", "Un ahorro que se retira al final del año", "Un crédito se devuelve con intereses, a diferencia de un regalo o un ahorro."),
        ("=", "{F} ¿Cuál es la cuota mensual del crédito A?", "(600000+60000)//6", "Se suman monto e interés y se divide entre el número de cuotas.", " pesos"),
        ("=", "{F} ¿Cuál es la cuota mensual del crédito B?", "(600000+132000)//12", "Se suman monto e interés y se divide entre el número de cuotas.", " pesos"),
        ("=", "{F} ¿Cuánto se paga en total con el crédito A?", "600000+60000", "Se suman el monto y el interés total.", " pesos"),
        ("=", "{F} ¿Cuánto se paga en total con el crédito B?", "600000+132000", "Se suman el monto y el interés total.", " pesos"),
        ("abc", "{F} ¿Cuál crédito tiene la cuota mensual menor?", "El crédito B", "El crédito A", "Tienen la misma cuota", "El crédito B reparte el pago en más cuotas y por eso cada cuota es menor."),
        ("abc", "{F} ¿Cuál crédito cuesta menos en total?", "El crédito A", "El crédito B", "Cuestan lo mismo", "El crédito A paga menos intereses en total."),
        ("=", "{F} Si se toma el crédito A, ¿cuánto del ingreso mensual de $450.000 queda después de pagar la cuota?", "450000-(600000+60000)//6", "Al ingreso se le resta la cuota mensual del crédito A.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más en intereses cuesta el crédito B en comparación con el A?", "132000-60000", "A los intereses de B se le restan los de A.", " pesos"),
        ("abc", "{F} Un vendedor dice: «Elija el crédito B, su cuota es más baja». ¿Qué falta considerar?", "El costo total o el CAE: la cuota baja implica más intereses en total", "Nada: la cuota es lo único que importa", "El color del contrato", "La cuota baja se logra con más plazo y más intereses totales."),
        ("abc", "¿Qué es la mora?", "El atraso en el pago de una cuota", "El pago anticipado de todo el crédito", "La tasa de interés del crédito", "La mora es pagar tarde, lo que puede generar cobros extra."),
        ("abc", "Una persona tiene dos cuotas de crédito y está pensando en pedir un tercer crédito para pagar gastos del mes. ¿Qué riesgo debe considerar?", "El sobreendeudamiento: las cuotas pueden consumir gran parte de su ingreso", "Ninguno, porque más crédito siempre ayuda", "Que el banco no le entregue nada", "Acumular cuotas reduce la capacidad de pago y aumenta el riesgo de mora."),
        ("=", "{F} Si se tomaran ambos créditos al mismo tiempo, ¿cuánto del ingreso de $450.000 quedaría después de pagar las dos cuotas?", "450000-(600000+60000)//6-(600000+132000)//12", "Al ingreso se le restan las dos cuotas mensuales.", " pesos"),
    ],
    ctx=("abc", "{F} Una persona necesita $600.000 para comprar herramientas de trabajo y duda entre A y B. ¿Cómo decide mejor?", "Compara el costo total o el CAE, revisa cuánto le queda del ingreso cada mes y lee el contrato", "Elige el que tenga la publicidad más llamativa", "Elige el que le recomiende la primera persona que ofrezca", "Una decisión informada considera costo total, capacidad de pago y condiciones del contrato."),
    sc=[
        ("En créditos de ejemplo: ¿cómo se calcula la cuota?", "Monto más interés, dividido en el número de cuotas", "Reparte el total a pagar en pagos iguales."),
        ("¿Qué indica el CAE?", "El costo total anual de un crédito", "Sirve para comparar créditos de distinto plazo."),
        ("¿Qué haces antes de firmar un crédito?", "Leo el contrato completo", "Así conozco los costos y las condiciones antes de aceptar."),
    ],
    op=("Caso de ejemplo. Matías, trabajador de una ferretería ficticia que gana $500.000 al mes, evalúa dos créditos de ejemplo para comprar un computador: Crédito 1: monto $400.000, interés total $40.000, 4 cuotas. Crédito 2: monto $400.000, interés total $80.000, 8 cuotas. "
        "Escribe: (1) la cuota de cada crédito, (2) el costo total de cada uno, (3) cuál cuesta menos en total, (4) cuánto del ingreso queda después de la cuota en cada caso, (5) una pregunta que harías antes de firmar.",
        "(1) Crédito 1: (400.000 + 40.000) ÷ 4 = 110.000. Crédito 2: (400.000 + 80.000) ÷ 8 = 60.000. (2) 440.000 y 480.000. (3) El crédito 1. (4) 390.000 y 440.000. (5) «¿Cuál es el CAE y qué costos adicionales o seguros incluye?».",
        ["calcula las cuotas", "calcula el costo total", "compara con criterio", "calcula el ingreso restante", "formula una pregunta pertinente"],
        ["hoja con cinco respuestas"],
        ["mirar solo la cuota", "olvidar el costo total", "no leer el contrato"],
        "Pregunta: «¿qué harías si más adelante no puedes pagar una cuota?». Debe decir que avisa a la institución cuanto antes y pregunta por alternativas, en lugar de callar."),
    reinforce="Inventa un crédito con monto, interés total y número de cuotas y calcula la cuota y el costo total.",
    extend="Explica por qué la cuota más baja no siempre significa el crédito más barato.",
)

# ============================================================ OAG-12, clase 4
F = ("Ficha 48 (opciones de ejemplo; no se recomiendan productos ni instituciones). Opción X: depósito a plazo fijo de ejemplo; $100.000 por 1 año; devuelve $103.000 (interés de ejemplo: 3 de cada 100); riesgo bajo; si se retira antes del plazo se pierde parte del interés. "
     "Opción Y: instrumento de riesgo de ejemplo; $100.000 por 1 año; si va bien devuelve $130.000 y si va mal devuelve $80.000; sin garantía. Oferta Z: «Doble su dinero en un mes, 100 % asegurado».")
build(
    G12, 4, F,
    use="Aprenderé qué es invertir, cómo se relacionan riesgo, rentabilidad, liquidez y plazo, y cómo reconocer ofertas engañosas, con cifras de ejemplo.",
    prior=["Conozco el ahorro, el interés y el crédito.", "Sé calcular partes de un total.", "Sé reconocer mensajes engañosos."],
    explain=[
        "Invertir es destinar dinero con la expectativa de obtener una ganancia en el futuro, asumiendo un riesgo. La rentabilidad es la ganancia que da una inversión respecto de lo invertido. El riesgo es la posibilidad de ganar menos de lo esperado o de perder parte del dinero. En general, a mayor ganancia posible, mayor riesgo. La liquidez es qué tan rápido se puede recuperar el dinero sin perder valor, y el plazo es el tiempo que se compromete el dinero.",
        "Diversificar es repartir el dinero en distintas opciones para no depender de una sola. Antes de decidir se define el objetivo, cuánto tiempo se puede dejar el dinero, cuánto riesgo se puede soportar y si podría necesitarse pronto. Las ofertas que prometen ganancias muy altas y 100 % aseguradas en poco tiempo son señales de estafa. Antes de entregar dinero, se verifica la oferta en organismos oficiales y se conversa con una persona adulta de confianza o con un profesional.",
        "Este cuaderno no recomienda inversiones ni instituciones: solo explica conceptos para que tomes decisiones informadas." + FIN + LIM,
    ],
    vocab=[("inversión", "destinar dinero esperando una ganancia futura, asumiendo un riesgo"), ("rentabilidad", "ganancia de una inversión respecto de lo invertido"), ("riesgo", "posibilidad de ganar menos de lo esperado o de perder dinero"), ("liquidez", "qué tan rápido se puede recuperar el dinero sin perder valor"), ("plazo", "tiempo que se compromete el dinero"), ("diversificar", "repartir el dinero en distintas opciones"), ("estafa", "engaño para quitar dinero a una persona")],
    worked=[
        ("Calcular una ganancia", "Una opción de ejemplo devuelve $108.000 por $100.000 invertidos. ¿Cuál es la ganancia?", ["Se resta lo invertido a lo recibido.", "108.000 − 100.000 = 8.000."], "$8.000"),
        ("Reconocer una señal de estafa", "Un mensaje de ejemplo dice: «Gane el triple en una semana, sin riesgo». ¿Qué señal de alerta tiene?", ["Promete una ganancia muy alta en poco tiempo.", "Dice que no hay riesgo."], "Promete ganancias muy altas y seguras en poco tiempo"),
    ],
    mistakes=[("Poner todo el dinero en la opción que promete más ganancia.", "Si sale mal, se pierde mucho y no hay con qué enfrentarlo.", "Considera el riesgo, el plazo y la necesidad de tener dinero disponible."),
              ("Entregar dinero por una oferta que «solo dura hoy» sin verificarla.", "La presión es una táctica de estafa.", "Verifica en organismos oficiales y consulta con un adulto de confianza.")],
    T=[
        ("abc", "En inversiones: ¿qué es la rentabilidad?", "La ganancia de una inversión respecto de lo invertido", "El dinero que se guarda en casa", "La cuota que se paga por un crédito", "La rentabilidad mide cuánto se gana en relación con lo invertido."),
        ("=", "{F} ¿Cuánto se gana con la opción X en un año?", "103000-100000", "A lo que se recibe se le resta lo invertido.", " pesos"),
        ("=", "{F} ¿Cuánto se gana con la opción Y si va bien?", "130000-100000", "A lo que se recibe se le resta lo invertido.", " pesos"),
        ("=", "{F} ¿Cuánto se pierde con la opción Y si va mal?", "100000-80000", "A lo invertido se le resta lo que se recibe.", " pesos"),
        ("abc", "{F} ¿Qué opción tiene mayor riesgo?", "La opción Y", "La opción X", "Las dos tienen el mismo riesgo", "En Y se puede perder parte del dinero y no hay garantía."),
        ("abc", "¿Qué es la liquidez?", "Qué tan rápido se puede recuperar el dinero sin perder valor", "La ganancia que da la inversión", "El número de cuotas de un crédito", "La liquidez habla de rapidez y pérdida al recuperar el dinero."),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre el mejor y el peor resultado de la opción Y?", "130000-80000", "Al mejor resultado se le resta el peor resultado.", " pesos"),
        ("abc", "{F} ¿Qué señales de alerta tiene la oferta Z?", "Promete duplicar el dinero en un mes y dice que es 100 % asegurado", "Pide pocos datos", "Ofrece un contrato por escrito", "Una ganancia enorme y segura en poco tiempo es una señal típica de estafa."),
        ("abc", "¿Qué haces antes de entregar dinero a una oferta de inversión?", "Verifico en organismos oficiales y consulto con una persona adulta de confianza o con un profesional", "Transfiero rápido para no perder el cupo", "Entrego mis claves para que operen por mí", "Verificar y consultar reduce el riesgo de caer en una estafa."),
        ("abc", "{F} Un amigo dice: «Pon todo en Y, porque puedes ganar $30.000». ¿Qué falta considerar?", "También podría perder $20.000, y si necesitas el dinero pronto el riesgo importa", "Nada: solo importa el mejor resultado", "Que el amigo no entiende", "Una decisión informada considera los resultados posibles, no solo el mejor."),
        ("abc", "¿Por qué no conviene poner todo el dinero en una sola opción?", "Porque diversificar reparte el riesgo", "Porque está prohibido", "Porque así se gana menos siempre", "Repartir el dinero reduce el efecto de que una opción salga mal."),
        ("abc", "{F} Una persona necesita el dinero dentro de 3 meses para pagar una matrícula. ¿Qué criterios son clave?", "La liquidez y el plazo: no puede arriesgarse a perder ni dejar el dinero inmovilizado un año", "Solo la rentabilidad máxima", "Ninguno: puede decidir sin pensar", "Con una necesidad cercana, la liquidez y el plazo pesan más que la ganancia posible."),
        ("=", "{F} Si alguien invierte $50.000 en X y $50.000 en Y, y Y sale mal, ¿cuánto recibe en total al final del año?", "50000*103//100+50000*80//100", "Se calcula lo que devuelve cada opción y se suman.", " pesos"),
    ],
    ctx=("abc", "{F} Un conocido le ofrece a una joven de 18 años la oferta Z y le dice que debe decidir hoy. ¿Qué hace ella?", "No transfiere nada, verifica la oferta en organismos oficiales y consulta con una persona adulta de confianza", "Transfiere una parte pequeña para probar", "Le entrega sus claves para ganar tiempo", "La presión y la promesa de ganancia segura son señales de estafa; verificar y consultar protege."),
    sc=[
        ("En inversiones de ejemplo: ¿qué relación hay entre ganancia posible y riesgo?", "A mayor ganancia posible, mayor riesgo", "Las altas ganancias suelen venir con riesgos altos."),
        ("¿Qué es diversificar?", "Repartir el dinero en distintas opciones", "Reduce el efecto de que una opción salga mal."),
        ("¿Qué haces ante una oferta que promete ganancias seguras?", "Desconfío y verifico", "Una ganancia alta y segura es una señal de estafa."),
    ],
    op=("Caso de ejemplo. Rosa, de 19 años, dispone de $200.000 de ahorro (cifra de ejemplo). Opción 1: depósito de ejemplo a un año que devuelve $206.000, riesgo bajo, con penalización si se retira antes. Opción 2: instrumento de riesgo de ejemplo que devuelve $260.000 si va bien y $160.000 si va mal. Una oferta por mensajería le dice: «Triplique su dinero en 15 días, garantizado». "
        "Escribe: (1) la ganancia de la opción 1, (2) la ganancia y la pérdida posibles de la opción 2, (3) tres señales de alerta de la oferta por mensajería, (4) qué criterios considerarías para decidir y a quién consultarías.",
        "(1) 206.000 − 200.000 = 6.000. (2) Ganancia: 60.000; pérdida: 40.000. (3) Promete triplicar en 15 días, dice «garantizado» y llega por mensajería sin verificación. (4) Objetivo, plazo, riesgo que puede soportar y liquidez; consultaría a una persona adulta de confianza o a un profesional y verificaría en organismos oficiales.",
        ["calcula la ganancia y la pérdida", "reconoce señales de alerta", "nombra criterios de decisión", "indica a quién consultar"],
        ["hoja con cuatro respuestas"],
        ["decidir solo por la ganancia", "ignorar la oferta engañosa", "no consultar"],
        "Pregunta: «¿qué pasaría si Rosa necesita el dinero en 2 meses?». Debe decir que la liquidez y el plazo serían más importantes que la ganancia."),
    reinforce="Escribe cuatro preguntas que harías antes de entregar dinero a una oferta de inversión.",
    extend="Explica por qué una oferta que promete ganancias muy altas y seguras es una señal de alerta.",
)

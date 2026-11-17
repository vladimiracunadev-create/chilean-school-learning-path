"""Contabilidad TP 3.º y 4.º medio: OAE-05 (comunicar información contable básica), OAE-06 (organizar el lugar de trabajo) y OAE-07 (atender a clientes internos y externos). Casos, cifras y empresas inventados."""
from __future__ import annotations

from tp_cont_common import build

O5 = "TP-CONT-3y4-OAE-05"
O6 = "TP-CONT-3y4-OAE-06"
O7 = "TP-CONT-3y4-OAE-07"

# ============================================================ OAE-05, clase 1
F = ("Ficha 18 (solicitudes de ejemplo en «Taller Rayén»). La dueña pide saber cuánto se vendió y cuánto se gastó en el mes; el jefe de bodega pide el valor de las existencias; "
     "la jefa de ventas pide cuánto deben los clientes. Datos del mes (de ejemplo): ventas $5.000.000; gastos $3.800.000; existencias $2.400.000; clientes por cobrar $1.500.000.")
build(
    O5, 1, F,
    use="Aprenderé para qué sirven los informes contables internos, qué elementos deben llevar y qué información conviene o no compartir.",
    prior=["Sé qué son ventas, gastos y existencias.", "Sé calcular el resultado de un período.", "Sé qué es información confidencial."],
    explain=[
        "Un informe interno presenta información contable a personas de la propia empresa, como la dueña o las jefaturas, para que tomen decisiones. Cada persona necesita cifras distintas: la dueña, el resultado; bodega, las existencias; ventas, lo que deben los clientes. Por eso lo primero es preguntar qué decisión se quiere tomar y elegir solo las cifras que sirven.",
        "Un buen informe lleva siempre un título, el período al que se refiere, la unidad (por ejemplo, pesos), la fuente de las cifras, las cifras clave y una conclusión breve en lenguaje claro. Debe ser oportuno, es decir, llegar a tiempo para decidir, y fiel: las cifras no se cambian para que se vean mejor.",
        "Algunos datos, como los sueldos de cada persona o las deudas con proveedores, son confidenciales. Se entregan solo a quien los necesita para su función y con autorización de la jefatura. Si alguien pide más información de la necesaria, se pregunta para qué la quiere y se consulta antes de entregarla.",
    ],
    vocab=[("informe interno", "documento para personas de la propia empresa que decide con cifras"), ("período", "tramo de tiempo informado"), ("unidad", "forma de medir las cifras, como pesos"), ("fuente", "origen de las cifras"), ("conclusión", "frase breve que resume lo que muestran las cifras"), ("oportuno", "que llega a tiempo para decidir"), ("fiel", "que muestra las cifras tal como son")],
    worked=[
        ("Elegir el dato", "Un dueño de ejemplo quiere saber si le alcanza el dinero disponible para pagar a sus proveedores este mes. ¿Qué cifras debe mostrar el informe?", ["La pregunta compara dinero disponible con deudas.", "Se muestran caja y banco frente a las deudas con proveedores."], "Caja y banco y deudas con proveedores"),
        ("Completar el informe", "Un informe de ejemplo dice «Ventas 2.000.000». ¿Qué le falta?", ["No indica el período ni la unidad ni la fuente.", "Falta título, período, unidad, fuente y conclusión."], "Título, período, unidad, fuente y conclusión"),
    ],
    mistakes=[("Entregar todo el libro mayor cuando la dueña pidió «cuánto ganamos».", "La información se vuelve difícil de usar y se exponen datos que no se necesitan.", "Pregunta qué decisión quiere tomar y entrega las cifras que la apoyan."),
              ("Cambiar una cifra para que el informe se vea mejor.", "El informe deja de ser fiel y engaña a quien decide.", "Presenta las cifras reales y comenta su causa si corresponde.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es un informe interno?", "Un documento que presenta información a personas de la propia empresa para decidir", "Un documento que se entrega a clientes para cobrar una venta", "Un documento tributario que se emite por cada venta", "El informe interno apoya decisiones de la propia empresa; la factura o boleta son documentos tributarios."),
        ("abc", "¿Qué elementos debe llevar siempre un informe?", "Título, período, unidad, fuente de las cifras, cifras clave y conclusión", "Solo las cifras, sin explicación", "Solo la conclusión, sin cifras", "Sin estos elementos el informe puede malinterpretarse o no poder comprobarse."),
        ("ab", "{F} ¿Qué informe necesita la dueña?", "Las ventas y los gastos del mes, y su resultado", "El saldo de lo que deben los clientes", "La dueña pidió saber cuánto se vendió y cuánto se gastó."),
        ("=", "{F} ¿Cuántos pesos es el resultado del mes (ventas menos gastos)?", "5000000-3800000", "El resultado es ventas menos gastos.", " pesos"),
        ("abc", "{F} ¿Qué cifra necesita el jefe de bodega?", "El valor de las existencias: $2.400.000", "El total de ventas: $5.000.000", "El saldo que deben los clientes: $1.500.000", "Bodega maneja mercaderías, es decir, las existencias."),
        ("abc", "{F} ¿Qué cifra necesita la jefa de ventas?", "Lo que deben los clientes: $1.500.000", "El valor de las existencias: $2.400.000", "Los gastos del mes: $3.800.000", "Ventas pidió saber cuánto deben los clientes, que son las cuentas por cobrar."),
        ("=", "{F} ¿Qué porcentaje de las ventas representan los gastos?", "3800000*100//5000000", "Se divide el gasto por las ventas y se multiplica por 100.", " %"),
        ("abc", "¿Por qué no se entregan a la jefa de ventas los sueldos de cada persona del personal?", "Porque no los necesita para su decisión y es información reservada", "Porque las cifras son muy grandes", "Porque los sueldos no son parte de la contabilidad", "La confidencialidad limita la información a quien la necesita para su función."),
        ("abc", "Un informe dice «Resultado 900.000» sin período ni unidad. ¿Qué problema tiene?", "No se sabe a qué mes ni a qué moneda o unidad se refiere", "Ninguno, porque la cifra está bien escrita", "Es demasiado corto para leerse", "Sin período y unidad, la cifra puede malinterpretarse."),
        ("abc", "¿Qué significa que un informe sea oportuno?", "Que llega a tiempo para tomar la decisión", "Que contiene todas las cifras posibles", "Que es muy extenso", "La oportunidad se mide por la utilidad en el momento de decidir."),
        ("=", "{F} ¿Qué porcentaje de las ventas representan las cuentas por cobrar?", "1500000*100//5000000", "Se divide lo que deben los clientes por las ventas del mes.", " %"),
        ("abc", "La dueña pide «todo sobre la empresa». ¿Qué haces primero?", "Preguntar qué decisión quiere tomar para elegir las cifras", "Entregar todos los registros del año", "Esperar al cierre anual", "Entender la decisión permite mostrar solo lo útil."),
        ("abc", "Un compañero cambia $1.200.000 por $1.500.000 en el informe «para que se vea mejor». ¿Qué corresponde?", "Presentar las cifras reales y avisar al contador del cambio", "Dejarlo así porque a la dueña le gustará", "Cambiar otras cifras para disimular la diferencia", "Un informe debe ser fiel; cambiar cifras es falsear la información."),
    ],
    ctx=("abc", "El jefe de otra área pide a la asistente el detalle de las deudas con proveedores «por curiosidad». ¿Qué responde?", "Que consultará con la jefatura qué información corresponde compartir", "Que se lo entrega ahora porque es de la misma empresa", "Que se lo mande por mensaje a su teléfono personal", "Ser de la misma empresa no basta: se comparte lo que la función requiere y con autorización."),
    sc=[
        ("En Contabilidad: ¿qué se pregunta antes de preparar un informe?", "Qué decisión quiere tomar quien lo pidió", "Esa decisión determina qué cifras se muestran."),
        ("¿Qué elementos básicos lleva un informe interno?", "Título, período, unidad, fuente, cifras clave y conclusión", "Con ellos el informe se entiende y se puede comprobar."),
        ("¿Qué haces si alguien pide información reservada sin necesitarla?", "Consulto a la jefatura antes de entregarla", "La confidencialidad exige autorización y necesidad."),
    ],
    op=("Prepara un informe interno de ejemplo para la dueña de una panadería con estos datos del mes de junio: ventas $3.000.000; gastos $2.100.000; clientes por cobrar $400.000. Escribe un título, el período, la unidad, la fuente, el resultado, el porcentaje de gastos sobre ventas y una conclusión de dos líneas; señala qué dato no mostrarías a todo el personal.",
        "Título: Resultado del mes de junio. Período: junio. Unidad: pesos. Fuente: registros contables de junio (de ejemplo). Resultado: 3.000.000 − 2.100.000 = 900.000. Gastos sobre ventas: 70 %. Conclusión: en junio las ventas cubrieron los gastos y quedó un resultado de $900.000. No mostraría a todo el personal las deudas con proveedores ni los sueldos individuales.",
        ["incluye título, período, unidad, fuente y conclusión", "calcula resultado y porcentaje", "señala un dato confidencial"],
        ["hoja con el informe de una página"],
        ["omitir el período", "no calcular el porcentaje", "mostrar datos reservados a todos"],
        "Pregunta: «¿para quién es este informe y qué decisión apoya?». Si no puede decirlo, repasa la selección de cifras."),
    reinforce="Escribe tres decisiones distintas que podrían tomar una dueña, un jefe de bodega y una jefa de ventas con información contable.",
    extend="Explica con un ejemplo inventado qué puede pasar si un informe llega tarde a quien debe decidir.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 19 (glosario y datos de ejemplo). Estado de resultados = ingresos − costos − gastos; margen bruto = ventas − costo de ventas; flujo de caja = entradas − salidas de dinero del período; "
     "presupuesto = cifra planificada. «Taller Rayén» en abril (de ejemplo): ventas $3.000.000; costo de ventas $1.800.000; gastos de administración y ventas $900.000; "
     "entradas de dinero $2.700.000; salidas de dinero $2.500.000.")
build(
    O5, 2, F,
    use="Aprenderé qué muestra cada informe básico (estado de situación, de resultados, flujo de caja, presupuesto) y cómo elegir la forma de presentarlo.",
    prior=["Sé la ecuación patrimonial.", "Sé qué son ventas, costos y gastos.", "Sé leer tablas y gráficos simples."],
    explain=[
        "Cada informe responde una pregunta. El estado de situación muestra activos, pasivos y patrimonio a una fecha. El estado de resultados muestra ingresos, costos y gastos de un período y su resultado. El flujo de caja muestra el dinero que entró y salió en un período. El presupuesto es una cifra planificada que se compara con lo real.",
        "El margen bruto es lo que queda de las ventas después de restar el costo de ventas. El resultado es el margen bruto menos los gastos. El resultado y el flujo de caja pueden ser distintos: una venta a crédito aumenta el resultado, pero el dinero entra después; un gasto pagado más tarde reduce el resultado ahora y la caja después.",
        "La forma de presentar también importa. Una tabla sirve para ver cifras exactas; un gráfico de barras sirve para comparar valores entre períodos o entre presupuesto y real. Siempre se rotulan los ejes, el período y la unidad. Lo importante se destaca en una conclusión escrita en lenguaje claro.",
    ],
    vocab=[("estado de situación", "informe de activos, pasivos y patrimonio a una fecha"), ("estado de resultados", "informe de ingresos, costos y gastos de un período"), ("margen bruto", "ventas menos costo de ventas"), ("flujo de caja", "dinero que entra menos dinero que sale"), ("presupuesto", "cifra planificada para comparar con lo real"), ("gráfico de barras", "gráfico que compara valores con barras")],
    worked=[
        ("Calcular un resultado", "Una tienda de ejemplo tiene ventas por $1.000.000, costo de ventas por $600.000 y gastos por $250.000. ¿Cuál es el resultado?", ["Margen bruto = 1.000.000 − 600.000 = 400.000.", "Resultado = 400.000 − 250.000 = 150.000."], "$150.000"),
        ("Calcular un flujo", "Una tienda de ejemplo recibió $900.000 y pagó $700.000 en el mes. ¿Cuál es el flujo de caja?", ["Se restan las salidas a las entradas.", "900.000 − 700.000 = 200.000."], "$200.000"),
    ],
    mistakes=[("Creer que si hay resultado positivo hay dinero en caja.", "El resultado incluye ventas por cobrar y gastos por pagar; la caja es otra cosa.", "Mira el flujo de caja para saber el dinero disponible."),
              ("Mostrar un gráfico sin título ni unidad.", "El lector no sabe qué mide ni en qué período.", "Rotula título, ejes, período y unidad.")],
    T=[
        ("abc", "En Contabilidad: ¿qué muestra el estado de resultados?", "Los ingresos, costos y gastos de un período y su resultado", "Los activos, pasivos y patrimonio a una fecha", "Las entradas y salidas de dinero solamente", "El estado de resultados mide el desempeño de un período."),
        ("abc", "¿Qué muestra el estado de situación?", "Los activos, pasivos y patrimonio a una fecha", "Las ventas y los gastos del mes", "El dinero planificado", "La situación se mide en una fecha, no en un período."),
        ("ab", "¿Qué muestra el flujo de caja?", "El dinero que entró y salió en un período", "Los activos y pasivos a una fecha", "El flujo de caja solo cuenta movimientos de dinero."),
        ("=", "{F} ¿Cuántos pesos es el margen bruto de abril?", "3000000-1800000", "El margen bruto es ventas menos costo de ventas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el resultado de abril?", "3000000-1800000-900000", "El resultado es el margen bruto menos los gastos.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el flujo de caja de abril?", "2700000-2500000", "El flujo es lo que entró menos lo que salió.", " pesos"),
        ("abc", "{F} ¿Por qué el resultado y el flujo de caja de abril son distintos?", "Porque el resultado incluye ventas y gastos aunque no se hayan cobrado o pagado, y el flujo solo cuenta dinero", "Porque uno de los dos tiene un error de cálculo", "Porque el flujo no cuenta las ventas", "Los dos miden cosas distintas: desempeño y dinero."),
        ("abc", "En Contabilidad: ¿qué es un presupuesto?", "Una cifra planificada que se compara con lo real", "Una cifra que se calcula al final del período", "Un documento que respalda una compra", "El presupuesto se fija antes para comparar después."),
        ("=", "Un presupuesto de gastos de ejemplo es $850.000 y el gasto real fue $900.000. ¿Cuántos pesos se gastaron sobre el presupuesto?", "900000-850000", "Se resta el presupuesto al valor real.", " pesos"),
        ("abc", "Se quieren comparar las ventas de cuatro meses seguidos. ¿Qué presentación sirve más?", "Un gráfico de barras con un mes por barra", "Un párrafo largo con las cifras", "Una lista de documentos archivados", "Las barras permiten comparar valores de varios períodos de un vistazo."),
        ("abc", "¿Qué informe muestra mejor si podrá pagar a sus proveedores con el dinero que tendrá este mes?", "El flujo de caja", "El estado de resultados", "El presupuesto de gastos", "El flujo informa el dinero disponible, que es lo que sirve para pagar."),
        ("=", "{F} ¿Qué porcentaje de las ventas es el margen bruto?", "1200000*100//3000000", "Se divide el margen bruto por las ventas y se multiplica por 100.", " %"),
        ("abc", "Un informe muestra un resultado positivo y concluye «tenemos dinero en caja para todo». ¿Qué error comete?", "Confunde el resultado del período con el dinero disponible", "No suma los gastos", "Usa mal el presupuesto", "El resultado no equivale al dinero que hay en caja."),
    ],
    ctx=("abc", "La jefa pide mostrar a la dueña cuánto se vendió en cada uno de los últimos cinco meses. ¿Qué eliges?", "Un gráfico de barras con título, período y unidad, y una conclusión escrita", "Un gráfico sin título para que sea más limpio", "Una lista larga de facturas", "Un gráfico de barras rotulado permite comparar los meses y entender el mensaje."),
    sc=[
        ("En Contabilidad: ¿cómo se calcula el margen bruto?", "Ventas menos costo de ventas", "El margen bruto es lo que queda antes de restar los gastos."),
        ("¿Qué informe muestra el dinero que entró y salió?", "El flujo de caja", "El flujo de caja solo registra movimientos de dinero."),
        ("¿Qué se rotula siempre en un gráfico?", "Título, período, unidad y ejes", "Sin rótulos el lector no entiende qué mide."),
    ],
    op=("Una tienda de ejemplo tuvo en julio: ventas $2.500.000; costo de ventas $1.500.000; gastos $600.000; entradas de dinero $2.000.000; salidas de dinero $2.100.000. Calcula el margen bruto, el resultado y el flujo de caja, y explica en tres líneas por qué pueden tener signos distintos.",
        "Margen bruto: 1.000.000. Resultado: 1.000.000 − 600.000 = 400.000. Flujo de caja: 2.000.000 − 2.100.000 = −100.000. Explicación: el resultado es positivo porque considera todas las ventas del mes, pero entró menos dinero del que salió porque parte de las ventas se cobrará después.",
        ["calcula margen bruto, resultado y flujo", "distingue desempeño de dinero disponible", "explica la diferencia con claridad"],
        ["hoja con los cálculos y la explicación"],
        ["confundir resultado con caja", "restar al revés el flujo", "no explicar la diferencia"],
        "Pregunta: «¿por qué el resultado es positivo y el flujo negativo?». Si no menciona las ventas por cobrar, repasa la diferencia."),
    reinforce="Escribe en una frase qué pregunta responde cada informe: situación, resultados, flujo y presupuesto.",
    extend="Explica con un ejemplo inventado cómo una venta a crédito cambia el resultado de un mes pero no su flujo de caja.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 20 (estado de resultados de ejemplo de «Taller Rayén», mayo). Ventas $4.200.000; costo de ventas $2.520.000; gastos: arriendo $300.000, sueldos $500.000, luz y agua $80.000, publicidad $120.000. "
     "El informe es para la dueña, de una página, con título, período, unidad, fuente y conclusión.")
build(
    O5, 3, F,
    use="Aprenderé a armar un estado de resultados sencillo y a escribir una conclusión fiel y comprensible.",
    prior=["Sé calcular margen bruto y resultado.", "Sé qué elementos lleva un informe.", "Sé calcular porcentajes exactos."],
    explain=[
        "Un estado de resultados sencillo se arma en este orden: ventas, costo de ventas, margen bruto, gastos (cada uno con su nombre y un total) y resultado. Cada línea lleva su cifra en pesos. El título dice qué es y de qué período, por ejemplo «Estado de resultados de mayo, en pesos».",
        "Después se redacta una conclusión breve y fiel: una o dos frases que digan el resultado y qué lo explica, sin exagerar ni esconder datos. También se declaran los límites: corresponde a un solo mes, no muestra el dinero en caja y los datos son los registrados hasta esa fecha.",
        "Cuando el informe circula entre varias personas, se muestra el total de cuentas sensibles, como sueldos, y no el detalle por persona. La fuente (los registros contables del período) se anota para que cualquiera pueda comprobar las cifras.",
    ],
    vocab=[("total de gastos", "suma de todas las cuentas de gasto del período"), ("conclusión fiel", "frase que dice lo que muestran las cifras, sin exagerar"), ("cuenta sensible", "cuenta con información reservada"), ("límite", "lo que el informe no puede mostrar")],
    worked=[
        ("Armar un estado", "Una tienda de ejemplo tuvo ventas por $2.000.000, costo de ventas por $1.200.000 y gastos por $500.000. ¿Cómo queda el estado de resultados?", ["Ventas 2.000.000; costo de ventas 1.200.000; margen bruto 800.000.", "Gastos 500.000; resultado 300.000."], "Margen bruto $800.000; resultado $300.000"),
        ("Redactar una conclusión", "Con el resultado de $300.000 anterior, redacta una conclusión fiel de una línea.", ["Debe decir el resultado y su relación con las ventas.", "No debe afirmar que hay dinero en caja."], "En el período las ventas cubrieron costos y gastos, con un resultado de $300.000"),
    ],
    mistakes=[("Escribir «ganamos $680.000 en caja» cuando es un resultado.", "El resultado no equivale a dinero disponible.", "Escribe «el resultado del período fue $680.000»."),
              ("Mostrar sueldos por persona en un informe que verán muchas personas.", "Se expone información reservada.", "Muestra el total de sueldos y guarda el detalle para quien corresponda.")],
    T=[
        ("=", "{F} ¿Cuántos pesos es el margen bruto?", "4200000-2520000", "El margen bruto es ventas menos costo de ventas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suman los gastos?", "300000+500000+80000+120000", "Se suman las cuatro cuentas de gasto.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el resultado de mayo?", "4200000-2520000-(300000+500000+80000+120000)", "El resultado es margen bruto menos total de gastos.", " pesos"),
        ("abc", "{F} ¿Qué título corresponde al informe?", "Estado de resultados de mayo, en pesos (cifras de ejemplo)", "Informe", "Cuentas del taller", "El título debe decir qué informe es, el período y la unidad."),
        ("=", "{F} ¿Qué porcentaje de las ventas es el costo de ventas?", "2520000*100//4200000", "Se divide el costo de ventas por las ventas y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cuál es el mayor gasto del mes?", "Sueldos, con $500.000", "Arriendo, con $300.000", "Publicidad, con $120.000", "Entre las cuentas de gastos, la mayor cifra es la de sueldos."),
        ("abc", "{F} ¿Qué conclusión es fiel con los datos?", "En mayo el resultado fue de $680.000, porque las ventas cubrieron costos y gastos", "En mayo hay $680.000 disponibles en caja", "En mayo el taller perdió dinero", "La conclusión fiel habla de resultado, no de dinero en caja, y coincide con los cálculos."),
        ("=", "{F} Si la publicidad se redujera a la mitad, ¿cuál sería el resultado de mayo con las demás cifras iguales?", "4200000-2520000-(300000+500000+80000+60000)", "Se recalcula el total de gastos con la publicidad reducida.", " pesos"),
        ("abc", "{F} ¿Qué fuente indicarías al pie del informe?", "Los registros contables de mayo (libro diario y mayor)", "Lo que recuerdo del mes", "El informe de otra empresa", "La fuente debe permitir comprobar las cifras."),
        ("abc", "El informe lo recibirán todas las jefaturas. ¿Cómo muestras los sueldos?", "Con el total de sueldos, sin el detalle por persona", "Con el nombre y el sueldo de cada persona", "No los incluyes aunque el resultado quede mal calculado", "El total basta para el resultado y protege la información personal."),
        ("abc", "¿Cuál es el orden correcto de un estado de resultados sencillo?", "Ventas, costo de ventas, margen bruto, gastos y resultado", "Resultado, gastos, ventas, costo de ventas", "Gastos, resultado, ventas, margen bruto", "El orden va de lo que ingresa a lo que queda después de restar costos y gastos."),
        ("=", "{F} Si las ventas hubieran sido $4.500.000 con el mismo costo de ventas y los mismos gastos, ¿cuántos pesos sería el resultado?", "4500000-2520000-1000000", "Se mantiene el costo de ventas y el total de gastos; cambian las ventas.", " pesos"),
        ("abc", "{F} ¿Qué límite debe declarar el informe?", "Corresponde a un solo mes y no muestra el dinero disponible en caja", "Ninguno, porque las cifras están completas", "Que mayo fue un mes especial", "Un estado de resultados no informa la caja ni una tendencia."),
    ],
    ctx=("abc", "La dueña mira el informe y pregunta: «¿tengo $680.000 en la caja?». ¿Qué respondes?", "No necesariamente: ese es el resultado del mes; el dinero disponible lo muestra el flujo de caja", "Sí, siempre", "No sé, y no puedo revisarlo", "El resultado y la caja miden cosas distintas."),
    sc=[
        ("En Contabilidad: ¿cuál es el orden de un estado de resultados sencillo?", "Ventas, costo de ventas, margen bruto, gastos y resultado", "Va de los ingresos a lo que queda al final."),
        ("¿Qué debe declarar una conclusión fiel?", "El resultado y su explicación, sin exagerar", "Así la lectura corresponde a las cifras."),
        ("¿Qué se hace con cuentas sensibles en informes amplios?", "Se muestra el total, no el detalle personal", "Se protege la información reservada de las personas."),
    ],
    op=("Arma el estado de resultados de ejemplo de una tienda en junio con estos datos: ventas $3.600.000; costo de ventas $2.160.000; arriendo $250.000; sueldos $400.000; luz y agua $90.000; publicidad $60.000. Escribe un título, el margen bruto, el total de gastos, el resultado, una conclusión de dos líneas y un límite.",
        "Título: Estado de resultados de junio, en pesos (cifras de ejemplo). Margen bruto: 1.440.000. Gastos: 800.000. Resultado: 640.000. Conclusión: en junio las ventas cubrieron el costo de ventas y los gastos, con un resultado de $640.000. Límite: corresponde a un solo mes y no muestra el dinero en caja.",
        ["ordena bien el estado", "calcula margen, gastos y resultado", "redacta conclusión y límite fieles"],
        ["hoja con el estado y la conclusión"],
        ["mezclar resultado y caja", "no totalizar los gastos", "no declarar límites"],
        "Pregunta: «¿qué le dirías a quien confunda resultado y caja?». Si no distingue, repasa el flujo de caja."),
    reinforce="Recalcula el resultado de la ficha si los sueldos subieran $50.000 y las ventas se mantuvieran.",
    extend="Explica por qué conviene mostrar el total de sueldos y no el detalle por persona en un informe que verán varias áreas.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 21 (presupuesto y real de ejemplo, abril, «Taller Rayén»). Ventas: presupuesto $3.000.000; real $3.300.000. Gastos: presupuesto $1.000.000; real $1.150.000. "
     "Variación = real − presupuesto. Resultado = ventas − gastos. El informe es para las jefaturas.")
build(
    O5, 4, F,
    use="Aprenderé a comparar lo real con lo presupuestado, elegir cómo presentarlo y redactar un resumen fiel con sus límites.",
    prior=["Sé calcular variaciones y porcentajes.", "Sé armar un estado de resultados sencillo.", "Sé elegir entre tabla y gráfico."],
    explain=[
        "Comparar lo real con el presupuesto permite saber si se cumplió lo planificado. La variación es el valor real menos el presupuestado y se expresa también como porcentaje del presupuesto: variación × 100 ÷ presupuesto. Se calcula para cada cifra y para el resultado.",
        "Un buen resumen para jefaturas es breve, usa números y verbos claros y termina en una acción o una pregunta. Por ejemplo: «En marzo (de ejemplo) las ventas quedaron 4 % sobre el presupuesto y los gastos 12 % sobre el presupuesto. Se revisarán los gastos». Para comparar presupuesto y real por cuenta sirve un gráfico de barras agrupadas, con dos barras por cuenta.",
        "Un criterio ético básico es presentar la información completa aunque no guste. Si alguien pide ocultar una variación desfavorable, se presenta igual y se avisa al contador. Se declaran los límites: la comparación no explica por qué cambiaron las cifras y corresponde a un solo mes.",
    ],
    vocab=[("variación", "valor real menos valor presupuestado"), ("variación porcentual", "variación dividida por el presupuesto y multiplicada por 100"), ("gráfico de barras agrupadas", "gráfico con dos barras por cuenta para comparar"), ("resumen ejecutivo", "texto breve que resume lo importante para decidir"), ("favorable", "que mejora el resultado respecto del presupuesto")],
    worked=[
        ("Calcular una variación", "Una tienda de ejemplo presupuestó ventas por $800.000 y vendió $880.000. ¿Cuál es la variación y su porcentaje?", ["Variación = 880.000 − 800.000 = 80.000.", "80.000 × 100 ÷ 800.000 = 10."], "$80.000, es decir, 10 %"),
        ("Redactar el resumen", "Con esa variación y gastos 5 % sobre el presupuesto, redacta una línea de resumen.", ["Se dicen las dos variaciones y el sentido del resultado.", "Se agrega una acción: revisar el detalle de gastos."], "Ventas 10 % sobre el presupuesto y gastos 5 % sobre el presupuesto; se revisarán los gastos"),
    ],
    mistakes=[("Calcular el porcentaje sobre el valor real.", "La variación porcentual se mide sobre el presupuesto.", "Divide la variación por el presupuesto."),
              ("Quitar la variación de gastos del resumen porque «se ve mal».", "El informe deja de ser fiel y las jefaturas deciden con información incompleta.", "Presenta toda la información y avisa al contador de la petición.")],
    T=[
        ("=", "{F} ¿Cuántos pesos fue la variación de las ventas?", "3300000-3000000", "La variación es el valor real menos el presupuesto.", " pesos"),
        ("=", "{F} ¿Cuántos pesos fue la variación de los gastos?", "1150000-1000000", "La variación es el valor real menos el presupuesto.", " pesos"),
        ("=", "{F} ¿En qué porcentaje superaron las ventas al presupuesto?", "300000*100//3000000", "Se divide la variación por el presupuesto y se multiplica por 100.", " %"),
        ("=", "{F} ¿En qué porcentaje superaron los gastos al presupuesto?", "150000*100//1000000", "Se divide la variación de gastos por su presupuesto.", " %"),
        ("=", "{F} ¿Cuántos pesos fue el resultado presupuestado?", "3000000-1000000", "El resultado es ventas menos gastos.", " pesos"),
        ("=", "{F} ¿Cuántos pesos fue el resultado real?", "3300000-1150000", "Se restan los gastos reales a las ventas reales.", " pesos"),
        ("abc", "{F} ¿Qué lectura describe mejor los datos?", "Las ventas superaron el presupuesto en 10 % y los gastos en 15 %; el resultado real fue $150.000 mayor", "Las ventas y los gastos estuvieron bajo el presupuesto", "El resultado real fue menor que el presupuestado", "Los porcentajes calculados y la resta de resultados muestran un resultado real mayor en $150.000."),
        ("abc", "{F} Para comparar presupuesto y real de ventas y gastos, ¿qué gráfico sirve?", "Barras agrupadas, con dos barras por cuenta", "Un gráfico circular con un solo valor", "Una línea con un único punto", "Las barras agrupadas ponen lado a lado lo presupuestado y lo real."),
        ("abc", "{F} ¿Cuál resumen es mejor para las jefaturas?", "En abril las ventas superaron el presupuesto en 10 % y los gastos en 15 %; el resultado fue $150.000 mayor. Se revisarán los gastos", "Abril estuvo muy bien", "Los gastos son un desastre", "El resumen útil lleva cifras, interpretación y una acción, sin adjetivos exagerados."),
        ("abc", "¿Por qué el resumen debe mostrar la variación y no solo el valor real?", "Porque la variación muestra si se cumplió lo planificado", "Porque es más corto", "Porque el presupuesto no importa", "Sin comparar con el presupuesto no se sabe si el valor real es bueno o malo."),
        ("abc", "{F} Un jefe pide ocultar la variación de gastos porque «se ve mal». ¿Qué corresponde?", "Presentar toda la información y avisar al contador de la petición", "Ocultarla para evitar problemas", "Cambiar el presupuesto para que coincida", "Un informe debe ser fiel; no se oculta ni se cambia información."),
        ("=", "{F} Si en mayo el gasto real fuera $1.250.000 con presupuesto de $1.000.000, ¿en qué porcentaje superaría al presupuesto?", "250000*100//1000000", "Se divide la variación por el presupuesto.", " %"),
        ("abc", "{F} ¿Qué límite debe declarar quien presenta la comparación?", "Solo compara un mes y no explica por qué subieron los gastos", "Ninguno, porque las cifras son exactas", "Que el presupuesto siempre es incorrecto", "Para explicar causas hay que revisar el detalle y más períodos."),
    ],
    ctx=("abc", "La contadora debe presentar la comparación a las jefaturas en tres minutos. ¿Qué es lo más adecuado?", "Un gráfico de barras agrupadas y un resumen de dos líneas con una acción", "Leer todos los asientos del mes", "Entregar solo el resultado real sin comparar", "Se prioriza lo que ayuda a decidir: comparación, interpretación y acción."),
    sc=[
        ("En Contabilidad: ¿cómo se calcula la variación porcentual contra presupuesto?", "Variación × 100 ÷ presupuesto", "Se mide sobre la cifra planificada."),
        ("¿Qué lleva un buen resumen para jefaturas?", "Cifras, interpretación y una acción", "Así sirve para decidir rápido y sin confusiones."),
        ("¿Qué haces si te piden ocultar una variación desfavorable?", "La presento y aviso al contador", "El informe debe ser completo y fiel."),
    ],
    op=("Una empresa de ejemplo presupuestó ventas por $2.000.000 y gastos por $1.200.000 en agosto; lo real fue ventas $2.100.000 y gastos $1.380.000. Calcula variaciones, porcentajes y resultados presupuestado y real, y escribe un resumen de dos líneas para las jefaturas con una acción y un límite.",
        "Ventas: +100.000 (5 %). Gastos: +180.000 (15 %). Resultado presupuestado: 800.000; real: 720.000 (80.000 menos). Resumen: en agosto las ventas superaron el presupuesto en 5 % y los gastos en 15 %, por lo que el resultado fue $80.000 menor; se revisarán los gastos. Límite: es un solo mes y no explica las causas.",
        ["calcula variaciones y porcentajes", "compara los resultados", "redacta resumen con acción y límite"],
        ["hoja con cálculos y resumen"],
        ["calcular el porcentaje sobre el real", "ocultar lo desfavorable", "no incluir acción"],
        "Pregunta: «¿qué acción propones?». Si no la incluye, pídele una acción concreta."),
    reinforce="Inventa un presupuesto y un valor real para tres cuentas y calcula las variaciones.",
    extend="Explica con un ejemplo inventado por qué una variación favorable en ventas puede no ser buena noticia si los gastos suben más.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 22 (puesto de trabajo de ejemplo, inventado). Una oficina contable tiene: 12 carpetas sueltas sobre un escritorio; un cajón de archivador abierto que sobresale al pasillo; "
     "cables sueltos en el piso; documentos con RUT de clientes a la vista; una silla sin regular y la pantalla del computador muy baja. "
     "Pausas de ejemplo en la jornada: 2 pausas de 15 minutos.")
build(
    O6, 1, F,
    use="Aprenderé por qué un puesto de trabajo ordenado, seguro y cómodo protege a las personas y a la información, y qué riesgos hay en una oficina contable.",
    prior=["Sé que los documentos tienen datos reservados.", "Sé qué es un riesgo.", "Sé sumar y multiplicar."],
    explain=[
        "Organizar y ordenar el lugar de trabajo significa que cada cosa tenga su lugar, que el espacio sea seguro y que el puesto sea cómodo. Un puesto desordenado produce tropiezos, pérdida de documentos y errores. En una oficina contable los riesgos más comunes son tropezar con cables o cajones abiertos, mantener malas posturas y dejar a la vista documentos con datos personales.",
        "La ergonomía adapta el puesto a la persona para cuidar su salud y comodidad: silla regulada, pantalla a la altura de los ojos y pausas breves y regulares. La frecuencia de las pausas la define el empleador o la persona de prevención de riesgos. Si aparece dolor persistente se avisa a una persona adulta responsable de la empresa y se consulta a un profesional de la salud; este cuaderno no entrega diagnósticos.",
        "El orden también protege la información. Una política de escritorio limpio consiste en guardar bajo llave los documentos reservados cuando uno se retira. Las salidas de emergencia y los pasillos siempre se mantienen despejados. Los plazos para conservar documentos son los que fija la norma vigente: antes de eliminar un documento se consulta a la jefatura o al contador.",
    ],
    vocab=[("ergonomía", "adaptar el puesto de trabajo a la persona para cuidar su salud"), ("pausa", "descanso breve durante la jornada"), ("escritorio limpio", "guardar bajo llave los documentos reservados al retirarse"), ("riesgo", "posibilidad de que algo cause daño"), ("prevención", "acciones para evitar un daño antes de que ocurra"), ("despejado", "libre de objetos que estorben")],
    worked=[
        ("Detectar un riesgo", "En una oficina de ejemplo hay una caja en el pasillo frente a la salida de emergencia. ¿Cuál es el riesgo y qué se hace?", ["La caja puede bloquear la salida y provocar tropiezos.", "Se avisa al encargado o se despeja si es seguro y liviano, y se deja el pasillo libre."], "Riesgo de bloqueo y tropiezo; se despeja y se avisa"),
        ("Cuidar la información", "Una asistente de ejemplo se retira y deja sobre el escritorio una lista de clientes con sus RUT. ¿Qué corresponde?", ["La lista contiene datos personales.", "Se guarda bajo llave antes de retirarse."], "Guardarla bajo llave"),
    ],
    mistakes=[("Dejar un cajón abierto «solo un momento» sobre el pasillo.", "Puede causar un tropiezo o un golpe aunque sea un momento.", "Cierra el cajón apenas termines de usarlo."),
              ("Pensar que las pausas hacen perder tiempo.", "Trabajar sin pausas aumenta errores y molestias.", "Haz las pausas que indique tu empleador o la persona de prevención.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es la ergonomía en una oficina?", "Adaptar el puesto de trabajo a la persona para cuidar su salud y comodidad", "Hacer el trabajo más rápido sin importar la comodidad", "Decorar la oficina", "La ergonomía busca que el puesto proteja a la persona."),
        ("abc", "{F} ¿Qué riesgo produce el cajón abierto que sobresale al pasillo?", "Tropiezo o golpe", "Pérdida de datos por un virus", "Mala postura de la espalda", "El cajón que sobresale al pasillo puede golpear o hacer tropezar."),
        ("ab", "{F} ¿Qué corresponde hacer con los cables sueltos en el piso?", "Ordenarlos y dejarlos fuera de la zona de paso", "Dejarlos y caminar con cuidado", "Los cables en la zona de paso son un riesgo de caída; se ordenan."),
        ("abc", "{F} ¿Qué riesgo tiene dejar a la vista documentos con RUT de clientes?", "Exponer datos personales a quien no los necesita", "Que se arrugue el papel", "Que se acaben las carpetas", "Los datos personales deben protegerse y mostrarse solo a quien los necesita."),
        ("abc", "{F} Con la silla sin regular y la pantalla muy baja, ¿qué riesgo se produce?", "Mala postura y molestias en cuello y espalda", "Pérdida de documentos", "Corte de la luz", "Una mala postura mantenida puede causar molestias."),
        ("=", "{F} Si las 12 carpetas sueltas se ordenan en cajas de 4 carpetas, ¿cuántas cajas se necesitan?", "12//4", "Se divide el total de carpetas por las que caben en una caja.", " cajas"),
        ("abc", "¿Qué recomienda la ergonomía para trabajo prolongado frente a una pantalla?", "Hacer pausas breves y cambiar de postura, según lo que indique el empleador o prevención", "Trabajar sin parar para terminar antes", "Hacer pausas solo al final de la jornada", "Las pausas regulares ayudan a cuidar la salud y la atención."),
        ("=", "{F} En una jornada de ejemplo con 2 pausas de 15 minutos, ¿cuántos minutos de pausa hay en total?", "2*15", "Se multiplica la cantidad de pausas por su duración.", " minutos"),
        ("abc", "¿Qué es la política de escritorio limpio?", "Guardar bajo llave los documentos reservados al retirarse", "No usar el escritorio para trabajar", "Botar todos los papeles al final del día", "Su objetivo es proteger la información reservada."),
        ("abc", "¿Por qué se guardan bajo llave los documentos reservados?", "Para que personas que no corresponde no vean datos personales o financieros", "Para que el papel se arrugue menos", "Para no necesitar copia de seguridad", "La llave limita el acceso a quien tiene autorización."),
        ("abc", "Ves cajas que bloquean una salida de emergencia. ¿Qué corresponde?", "Avisar de inmediato a la jefatura o a quien se encarga de prevención", "Esperar a que alguien más lo note", "Cubrir la salida con un cartel", "Una salida bloqueada es un riesgo grave y se informa de inmediato."),
        ("=", "{F} Si cada una de las 12 carpetas tiene 25 hojas, ¿cuántas hojas hay en total?", "12*25", "Se multiplica el número de carpetas por las hojas de cada una.", " hojas"),
        ("abc", "{F} Si debes ordenar solo una cosa primero, ¿cuál corresponde?", "El cajón abierto en el pasillo y los cables, porque pueden causar una caída ahora", "Cambiar el color de las carpetas", "Etiquetar todas las carpetas antes que nada", "Se priorizan los riesgos que pueden causar daño inmediato a las personas."),
    ],
    ctx=("abc", "Una compañera se queja de dolor persistente de espalda y te pregunta qué enfermedad tiene. ¿Qué respondes?", "Que no puedo diagnosticar y que avise a una persona adulta responsable de la empresa y consulte a un profesional de la salud", "Que seguro es una hernia y que tome un medicamento", "Que se aguante porque falta poco para el cierre", "Un cuaderno de contabilidad no da diagnósticos: se deriva a quien corresponde."),
    sc=[
        ("En Contabilidad: ¿qué es un escritorio limpio?", "Guardar bajo llave los documentos reservados al retirarse", "Protege la información de personas no autorizadas."),
        ("¿Qué riesgo tienen los cables sueltos en el piso?", "Tropiezos y caídas", "Los cables en la zona de paso pueden hacer caer a alguien."),
        ("¿Qué haces ante un dolor persistente en el trabajo?", "Aviso a una persona adulta responsable y consulto a un profesional de la salud", "No se diagnostica por cuenta propia."),
    ],
    op=("Observa este puesto de ejemplo: un cajón abierto sobre el pasillo, tres cables sueltos en el piso, una lista de clientes con RUT sobre el escritorio al irse la persona y una silla sin regular. Para cada caso escribe el riesgo y la acción, y ordena las cuatro acciones de más urgente a menos urgente con una razón.",
        "Cajón: riesgo de golpe o tropiezo; cerrarlo. Cables: riesgo de caída; fijarlos fuera de la zona de paso. Lista: exposición de datos personales; guardarla bajo llave. Silla: mala postura; regularla. Orden de urgencia: cajón y cables (riesgo inmediato de caída), lista (información reservada), silla (molestias a mediano plazo).",
        ["identifica el riesgo de cada caso", "propone una acción para cada uno", "prioriza con una razón"],
        ["hoja con cuatro riesgos, cuatro acciones y el orden"],
        ["no priorizar", "olvidar los datos personales", "dar un diagnóstico médico"],
        "Pregunta: «¿qué riesgo corriges primero y por qué?». Si no justifica por el daño inmediato, repasa la priorización."),
    reinforce="Haz una lista de cinco cosas que ordenarías en un puesto de trabajo de ejemplo para evitar tropiezos.",
    extend="Explica con un ejemplo inventado cómo un puesto desordenado puede provocar un error contable.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 23 (lista de documentos de ejemplo). Facturas recibidas, tal como llegaron: N.º 118, 120, 119, 121. Carpetas de clientes con las letras: A, M, C. "
     "Boletas de venta del 3 al 9 de mayo (ambos días incluidos). Método de las 5S: clasificar (separar lo necesario), ordenar (un lugar para cada cosa), limpiar, estandarizar (reglas iguales para todos) y mantener el hábito.")
build(
    O6, 2, F,
    use="Aprenderé criterios de archivo (cronológico, alfabético, correlativo), el método de las 5S y buenas prácticas para respaldar documentos.",
    prior=["Sé qué es un número correlativo.", "Sé el orden alfabético.", "Sé dividir y contar días."],
    explain=[
        "Archivar es guardar documentos de modo que se puedan encontrar rápido. Los criterios más usados son: cronológico (por fecha), alfabético (por nombre, de la A a la Z), correlativo (por número creciente, como facturas 1, 2, 3) y por tema. Se elige el criterio según cómo se busca el documento y se aplica igual para todos, para que cualquiera lo encuentre.",
        "El método de las 5S ayuda a mantener el orden: clasificar (separar lo que se necesita de lo que sobra), ordenar (un lugar para cada cosa), limpiar, estandarizar (fijar reglas iguales para todos) y mantener el hábito. Las cajas y carpetas se rotulan con el tipo de documento, el período y el rango de números, por ejemplo «Facturas, mayo, N.º 100 al 140».",
        "Los documentos digitales requieren copia de seguridad: una copia guardada en otro lugar, para poder recuperarlos si se pierden o se dañan. Las claves son personales y no se escriben a la vista ni se comparten. El plazo que se conserva cada documento lo fija la norma vigente; no se elimina nada sin consultar a la jefatura o al contador.",
    ],
    vocab=[("archivar", "guardar documentos para encontrarlos rápido"), ("correlativo", "ordenado por número creciente"), ("cronológico", "ordenado por fecha"), ("alfabético", "ordenado de la A a la Z"), ("5S", "método de orden: clasificar, ordenar, limpiar, estandarizar y mantener"), ("copia de seguridad", "copia guardada aparte para recuperar la información"), ("rotular", "escribir una etiqueta que dice qué contiene")],
    worked=[
        ("Ordenar facturas", "Se recibieron las facturas N.º 31, 33, 32 y 34. ¿Cómo quedan en orden correlativo creciente?", ["Se ordenan de menor a mayor número.", "31, 32, 33 y 34."], "31, 32, 33, 34"),
        ("Rotular una caja", "Una caja de ejemplo guarda comprobantes de egreso de junio, del N.º 60 al N.º 95. ¿Qué rótulo le pones?", ["Se anotan tipo de documento, período y rango.", "Se escribe «Comprobantes de egreso, junio, N.º 60 al 95»."], "Comprobantes de egreso, junio, N.º 60 al 95"),
    ],
    mistakes=[("Rotular una caja como «Varios».", "Nadie sabe qué contiene sin abrirla.", "Escribe tipo, período y rango de números."),
              ("Guardar la copia de seguridad en el mismo lugar que el original.", "Si ese lugar se daña, se pierden ambos.", "Guarda la copia en otro lugar seguro.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es un archivo correlativo?", "Uno ordenado por número creciente", "Uno ordenado de la A a la Z", "Uno ordenado por color de carpeta", "Correlativo significa seguir la numeración en orden creciente."),
        ("abc", "¿Qué es un archivo alfabético?", "Uno ordenado de la A a la Z por nombre", "Uno ordenado por fecha de llegada", "Uno ordenado por tamaño", "El criterio alfabético usa el nombre."),
        ("ab", "¿Qué es un archivo cronológico?", "Uno ordenado por fecha", "Uno ordenado por tema", "Cronológico significa seguir el orden del tiempo."),
        ("abc", "{F} ¿Cuál es el orden correlativo creciente de las facturas recibidas?", "118, 119, 120, 121", "118, 120, 119, 121", "121, 120, 119, 118", "El orden creciente va de menor a mayor número."),
        ("abc", "{F} ¿Cuál es el orden alfabético de las carpetas A, M y C?", "A, C, M", "A, M, C", "C, A, M", "En el abecedario la C viene antes que la M."),
        ("=", "{F} ¿Cuántos días de boletas hay del 3 al 9 de mayo, ambos incluidos?", "9-3+1", "Se cuentan ambos extremos, por eso se suma uno.", " días"),
        ("abc", "En el método de las 5S, ¿qué significa clasificar?", "Separar lo necesario de lo que sobra", "Ordenar por color", "Limpiar el escritorio", "Clasificar es decidir qué se queda y qué se retira."),
        ("abc", "En las 5S, ¿qué significa estandarizar?", "Fijar reglas iguales para todos para mantener el orden", "Comprar muebles iguales", "Limpiar todos los días", "Estandarizar es acordar reglas comunes para todas las personas."),
        ("abc", "¿Para qué sirve una copia de seguridad de documentos digitales?", "Para recuperarlos si se pierden o se dañan", "Para que dos personas los modifiquen a la vez", "Para que ocupen menos espacio", "La copia permite restaurar la información."),
        ("abc", "¿Por qué no basta guardar la copia de seguridad en el mismo lugar que el original?", "Porque si ese lugar se daña se pierden ambos", "Porque la copia siempre es peor que el original", "Porque ocupa más espacio", "El respaldo debe estar separado del original para cumplir su función."),
        ("=", "Una caja de archivo guarda 150 documentos y hay 600 documentos. ¿Cuántas cajas se necesitan?", "600//150", "Se divide el total de documentos por los que caben en cada caja.", " cajas"),
        ("abc", "¿Cuánto tiempo se debe conservar un documento contable?", "El plazo que fija la norma vigente; antes de eliminar se consulta a la jefatura o al contador", "Un año, siempre", "Hasta que falte espacio", "El plazo no lo decide cada persona sino la norma vigente."),
        ("abc", "Una asistente escribe su clave en un papel pegado al monitor. ¿Qué corresponde?", "Cambiarla y guardarla de forma privada, sin compartirla", "Dejarla porque nadie la verá", "Compartirla con una compañera para emergencias", "Las claves son personales y no se dejan a la vista."),
    ],
    ctx=("abc", "Una caja de documentos dice «Cosas de mayo». Una persona nueva debe encontrar una factura N.º 125. ¿Cómo se evita este problema?", "Rotulando cajas con tipo de documento, período y rango de números", "Pidiéndole que abra todas las cajas", "Cambiando la factura de lugar sin avisar", "Un rótulo claro permite ubicar documentos sin abrir cada caja."),
    sc=[
        ("En Contabilidad: ¿qué es un archivo correlativo?", "Uno ordenado por número creciente", "Es el criterio típico para facturas y comprobantes."),
        ("¿Qué datos lleva el rótulo de una caja?", "Tipo de documento, período y rango de números", "Así se encuentra el contenido sin abrirla."),
        ("¿Dónde se guarda la copia de seguridad de los comprobantes contables?", "En otro lugar seguro, separado del original", "Así se recupera la información si el original se daña."),
    ],
    op=("Ordena estas boletas de ejemplo en orden correlativo creciente: N.º 205, 202, 204, 201, 203. Luego escribe el rótulo de la caja que las guarda para el mes de agosto y explica en dos líneas cómo evitarías que alguien guarde la copia de seguridad en el mismo lugar del original.",
        "Orden: 201, 202, 203, 204, 205. Rótulo: «Boletas de venta, agosto, N.º 201 al 205». Copia de seguridad: la guardo en otro lugar seguro y separado, para que si el lugar del original se daña, se pueda recuperar la información.",
        ["ordena correctamente el correlativo", "rotula con tipo, período y rango", "explica el lugar del respaldo"],
        ["hoja con la lista ordenada, el rótulo y la explicación"],
        ["ordenar al revés", "rotular con «varios»", "dejar el respaldo junto al original"],
        "Pregunta: «¿qué le falta al rótulo para que otra persona encuentre el documento?». Si no menciona el rango, revisa el rótulo."),
    reinforce="Escribe los cinco pasos de las 5S con un ejemplo de tu casa para cada uno.",
    extend="Explica con un ejemplo inventado qué pasa si un archivo no sigue ningún criterio.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 24 (caso de ejemplo). En una oficina contable hay 240 documentos del mes mezclados: facturas (80), boletas (120) y comprobantes (40). Cada caja de archivo guarda 40 documentos. "
     "Hoy encontrar un documento toma en promedio 6 minutos; con el archivo ordenado se espera que tome 2 minutos (cifras de ejemplo). Se buscan 15 documentos al día. Las boletas del mes (mayo) están numeradas del N.º 1 al N.º 120.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de desorden documental: contar, calcular tiempos y proponer un plan de archivo.",
    prior=["Sé los criterios de archivo.", "Sé el método 5S.", "Sé multiplicar y dividir exactamente."],
    explain=[
        "Para mejorar un puesto de trabajo se parte midiendo. En un caso de desorden se cuentan los documentos, se agrupan por tipo (facturas, boletas, comprobantes), se calcula cuántas cajas se necesitan y se estima el tiempo que se pierde buscando. Las cifras permiten comparar la situación actual con la que se espera después de ordenar.",
        "Un plan de archivo básico define: el criterio (por tipo y luego por número correlativo), las cajas y su rótulo, el lugar donde se guardan y quién se encarga. Las cajas con datos personales se guardan con llave y acceso restringido. Al mover cajas se anota la nueva ubicación y se informa a quienes las usan.",
        "Los tiempos de este caso son cifras de ejemplo: en la realidad se miden en la propia oficina. Lo importante es el método: contar, calcular, decidir y volver a medir. El ahorro de tiempo se usa para registrar y revisar a tiempo, no para acumular más trabajo sin pausas.",
    ],
    vocab=[("plan de archivo", "criterio, cajas, rótulos, lugar y responsable del archivo"), ("rango", "números desde el primero hasta el último de un grupo"), ("tiempo de búsqueda", "minutos que toma encontrar un documento"), ("ahorro", "diferencia entre el tiempo de antes y el de después"), ("acceso restringido", "permitido solo a quienes lo necesitan")],
    worked=[
        ("Contar cajas", "Una oficina de ejemplo tiene 150 comprobantes y cada caja guarda 50. ¿Cuántas cajas necesita?", ["Se divide el total por lo que cabe en una caja.", "150 ÷ 50 = 3."], "3 cajas"),
        ("Calcular el ahorro", "En una oficina de ejemplo se buscan 10 documentos al día; antes tomaba 8 minutos cada uno y ahora 3. ¿Cuántos minutos se ahorran por día?", ["Antes: 10 × 8 = 80 minutos. Ahora: 10 × 3 = 30 minutos.", "El ahorro es 80 − 30 = 50 minutos."], "50 minutos por día"),
    ],
    mistakes=[("Calcular las cajas sin separar los tipos de documento.", "Se mezclan facturas, boletas y comprobantes y se pierde el orden.", "Agrupa por tipo y luego calcula las cajas de cada uno."),
              ("Mover las cajas sin anotar su nueva ubicación.", "Otras personas no las encontrarán.", "Anota la nueva ubicación e informa a quienes las usan.")],
    T=[
        ("=", "{F} ¿Cuántos documentos hay en total?", "80+120+40", "Se suman los tres tipos de documento.", " documentos"),
        ("=", "{F} ¿Cuántas cajas se necesitan en total?", "240//40", "Se divide el total de documentos por los que caben en cada caja.", " cajas"),
        ("=", "{F} ¿Cuántas cajas se necesitan solo para las boletas?", "120//40", "Se divide la cantidad de boletas por los que caben en cada caja.", " cajas"),
        ("abc", "{F} ¿Cuál es el mejor criterio para archivar estos documentos?", "Separar por tipo y luego ordenar por número correlativo", "Dejarlos todos mezclados por fecha de llegada", "Ordenarlos por el tamaño del papel", "Por tipo y correlativo se encuentra cada documento sin revisar todo."),
        ("=", "{F} ¿Cuántos minutos se pierden hoy buscando 15 documentos al día?", "15*6", "Se multiplica la cantidad de búsquedas por el tiempo de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos tomaría buscar 15 documentos con el archivo ordenado?", "15*2", "Se multiplica la cantidad de búsquedas por el tiempo esperado.", " minutos"),
        ("=", "{F} ¿Cuántos minutos se ahorrarían por día?", "15*6-15*2", "Se resta el tiempo esperado al tiempo actual.", " minutos"),
        ("abc", "{F} En las 5S, ¿qué paso corresponde a separar lo necesario de lo que sobra antes de ordenar?", "Clasificar", "Limpiar", "Estandarizar", "Clasificar es el primer paso y define qué se queda."),
        ("abc", "{F} ¿Qué rótulo es el mejor para la primera caja de boletas del mes?", "Boletas de venta, mayo, N.º 1 al 40", "Varios", "Cosas del mes", "El rótulo con tipo, período y rango permite ubicar los documentos."),
        ("abc", "¿Por qué rotular con el rango de números?", "Permite ubicar un documento sin abrir la caja y notar si falta alguno", "Hace que la caja se vea más bonita", "Permite que cualquiera cambie su contenido", "El rango da una referencia clara y facilita detectar faltantes."),
        ("abc", "{F} Algunas cajas contienen datos personales de clientes. ¿Dónde se guardan?", "En un lugar con llave y acceso restringido", "En el pasillo, para que estén a mano", "Sobre un escritorio abierto", "Los datos personales se protegen con acceso restringido."),
        ("=", "{F} En 20 días de trabajo, ¿cuántos minutos se ahorrarían con el archivo ordenado?", "20*(15*6-15*2)", "Se multiplica el ahorro diario por los días de trabajo.", " minutos"),
        ("abc", "Al cambiar las cajas a otro estante, ¿qué corresponde hacer?", "Anotar la nueva ubicación e informar a quienes las usan", "No avisar para que nadie las toque", "Esperar a que alguien pregunte dónde están", "Sin información sobre la nueva ubicación, los documentos se pierden."),
    ],
    ctx=("abc", "Tu jefa te pregunta si vale la pena ordenar el archivo. ¿Qué respuesta se apoya en datos?", "Hoy se pierden 90 minutos al día buscando y con orden serían 30: se ahorran 60 minutos por día", "No sé, pero se ve más lindo", "Vale la pena porque a mí me gusta el orden", "Una decisión se apoya en cifras medidas y comparadas."),
    sc=[
        ("En Contabilidad: ¿qué se mide primero para mejorar un puesto?", "Cuántos documentos hay y cuánto tiempo toma encontrarlos", "Las cifras permiten comparar antes y después."),
        ("¿Qué incluye un plan de archivo?", "Criterio, cajas, rótulos, lugar y responsable", "Así queda claro cómo se ordena y quién lo mantiene."),
        ("¿Qué se hace al mover cajas?", "Se anota la nueva ubicación y se informa a quienes las usan", "Otras personas deben poder encontrarlas sin tener que preguntar."),
    ],
    op=("Una oficina de ejemplo tiene 300 documentos: 100 facturas, 150 boletas y 50 comprobantes. Cada caja guarda 50. Los comprobantes de septiembre están numerados del N.º 1 al N.º 50. Calcula las cajas por tipo y en total, el tiempo ahorrado por día si se buscan 12 documentos y la búsqueda pasa de 5 a 2 minutos, y escribe un rótulo para la caja de comprobantes del mes de septiembre.",
        "Cajas: facturas 2, boletas 3, comprobantes 1; total 6. Tiempo antes: 12 × 5 = 60; después: 12 × 2 = 24; ahorro: 36 minutos por día. Rótulo: «Comprobantes, septiembre, N.º 1 al 50».",
        ["calcula cajas por tipo y total", "calcula el ahorro de tiempo", "escribe un rótulo completo"],
        ["hoja con los cálculos y el rótulo"],
        ["mezclar los tipos", "calcular el ahorro con una resta incorrecta", "rotular sin rango"],
        "Pregunta: «¿cómo calculaste el ahorro?». Si no compara antes y después, repasa la resta."),
    reinforce="Inventa una oficina con 180 documentos y cajas de 30 y calcula cuántas cajas necesita.",
    extend="Explica por qué el ahorro de tiempo se usa también para revisar los registros y no solo para hacer más trabajo.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 25 (lista de verificación de ejemplo para una oficina contable). Ítems: 1) pasillo despejado; 2) cables fuera de la zona de paso; 3) documentos reservados bajo llave al retirarse; "
     "4) silla y pantalla regulados; 5) pausas breves realizadas; 6) copia de seguridad hecha; 7) carpetas rotuladas. Revisión de ejemplo: cumple los ítems 1, 2, 4 y 7; no cumple los ítems 3, 5 y 6. "
     "Tiempo de corrección (de ejemplo): ítem 3, 1 hora; ítem 5, 2 horas; ítem 6, 3 horas.")
build(
    O6, 4, F,
    use="Aprenderé a usar una lista de verificación y a armar un plan de mejora para mantener un lugar de trabajo ordenado, seguro y confidencial.",
    prior=["Sé los riesgos de una oficina.", "Sé los criterios de archivo.", "Sé qué es la confidencialidad."],
    explain=[
        "Una lista de verificación es una lista de puntos que se revisan uno a uno: cada ítem se marca como «cumple» o «no cumple». Sirve para detectar problemas antes de que ocurran y para repetir la revisión cada cierto tiempo. Es una ayuda para avisar y corregir; no reemplaza a la persona de prevención ni a la norma vigente.",
        "Con los ítems que no cumplen se arma un plan de mejora. Cada acción tiene un responsable, un plazo y una forma de comprobar que se hizo. Se prioriza por el riesgo: primero lo que puede causar daño inmediato a personas, luego lo que expone información y después el orden general. El hábito se sostiene repitiendo la revisión.",
        "Hay normas de ética que acompañan al orden: los documentos con datos personales no se sacan de la oficina ni se fotografían con teléfonos personales sin autorización, y no se comparte información de la empresa con quien no corresponde. Si algo no está claro, se consulta a la jefatura antes de actuar.",
    ],
    vocab=[("lista de verificación", "lista de puntos que se revisan como «cumple» o «no cumple»"), ("plan de mejora", "acciones con responsable, plazo y comprobación"), ("responsable", "persona a cargo de una acción"), ("plazo", "fecha límite de una acción"), ("sostener", "mantener el hábito con revisiones repetidas")],
    worked=[
        ("Contar lo pendiente", "En una revisión de ejemplo de 8 ítems se cumplen 5. ¿Cuántos ítems quedan pendientes?", ["Se restan los cumplidos al total.", "8 − 5 = 3."], "3 ítems"),
        ("Armar una acción", "Para el ítem «copia de seguridad hecha» que no cumple, ¿qué acción de mejora completa se escribe?", ["Debe tener responsable, plazo y comprobación.", "Por ejemplo: hacer la copia el viernes, a cargo de la auxiliar; se comprueba abriendo la copia."], "Acción con responsable, plazo y comprobación"),
    ],
    mistakes=[("Marcar «cumple» sin mirar el puesto de trabajo.", "La revisión pierde valor y los riesgos siguen.", "Revisa con la vista cada ítem antes de marcarlo."),
              ("Llevarse documentos con RUT de clientes a casa «para adelantar».", "Se exponen datos personales fuera de la oficina.", "Consulta la política de la empresa y no saques documentos sin autorización.")],
    T=[
        ("=", "{F} ¿Cuántos ítems no cumple la revisión?", "7-4", "Se restan los ítems que cumple al total de ítems.", " ítems"),
        ("=", "{F} ¿Cuántas horas se necesitan en total para corregir los tres ítems pendientes?", "1+2+3", "Se suman las horas de cada ítem pendiente.", " horas"),
        ("abc", "{F} ¿Qué ítem no cumplido protege los datos personales que podrían quedar a la vista?", "El ítem 3, documentos reservados bajo llave", "El ítem 6, copia de seguridad", "El ítem 1, pasillo despejado", "El ítem 3 protege la información reservada al retirarse."),
        ("abc", "{F} ¿Qué ítem no cumplido ayuda a prevenir fatiga por trabajo prolongado?", "El ítem 5, pausas breves", "El ítem 7, carpetas rotuladas", "El ítem 2, cables fuera de la zona de paso", "Las pausas son la medida que previene la fatiga."),
        ("abc", "{F} ¿Qué ítem no cumplido permite recuperar los datos si se pierde el original?", "El ítem 6, copia de seguridad", "El ítem 4, silla y pantalla regulados", "El ítem 1, pasillo despejado", "La copia de seguridad es lo que permite restaurar información."),
        ("abc", "¿Por qué conviene repetir la revisión cada cierto tiempo?", "Porque el orden se pierde si no se mantiene", "Porque la lista cambia sola", "Para cambiar los ítems cada vez", "Sostener el hábito exige revisar de nuevo."),
        ("abc", "¿Quién decide eliminar documentos antiguos?", "La jefatura o el contador, según la norma vigente de conservación", "Cualquiera que necesite espacio", "Una visita que pase por la oficina", "Eliminar documentos exige autorización y respetar los plazos vigentes."),
        ("=", "Un estante tiene 4 repisas y en cada una caben 5 cajas. Se quieren guardar 24 cajas. ¿Cuántas cajas no tienen lugar?", "24-4*5", "Se resta la capacidad del estante al total de cajas.", " cajas"),
        ("abc", "Un jefe pide llevar a casa documentos con RUT de clientes «para adelantar trabajo». ¿Qué corresponde?", "Consultar la política de la empresa y no sacar documentos sin autorización", "Llevarlos y devolverlos al día siguiente", "Fotografiarlos con el teléfono personal", "Los datos personales no salen de la oficina sin autorización."),
        ("abc", "Un compañero no hace pausas «para terminar antes». ¿Qué le explicas?", "Que las pausas cuidan la salud y la atención, y trabajar sin ellas aumenta errores y molestias", "Que las pausas no son parte del trabajo", "Que las pausas se hacen solo si sobra tiempo", "Las pausas forman parte del trabajo seguro."),
        ("abc", "Una compañera tiene dolor persistente en la espalda por trabajar muchas horas sentada. ¿Qué corresponde?", "Avisar a una persona adulta responsable de la empresa y consultar a un profesional de la salud", "Diagnosticarla y recomendarle un medicamento", "Decirle que lo ignore", "Un cuaderno no da diagnósticos: se deriva a quien corresponde."),
        ("abc", "¿Qué debe tener cada acción de un plan de mejora?", "Un responsable, un plazo y una forma de comprobar que se hizo", "Solo un título", "Solo el costo", "Con estos tres datos se puede dar seguimiento."),
        ("abc", "¿Qué límite tiene una lista de verificación?", "No reemplaza a la persona de prevención ni a la norma vigente", "Garantiza que no habrá accidentes", "Reemplaza cualquier revisión de la jefatura", "La lista ayuda a detectar y avisar, pero no sustituye a quienes tienen esa función."),
    ],
    ctx=("abc", "La jefa te pide marcar «cumple» en todos los ítems sin revisar, porque viene una visita. ¿Qué haces?", "Reviso los ítems de verdad, marco lo que cumple y aviso de lo pendiente", "Marco todo «cumple» para evitar problemas", "No hago la revisión", "Una revisión solo sirve si refleja la realidad."),
    sc=[
        ("En Contabilidad: ¿qué es una lista de verificación?", "Una lista de puntos que se revisan como cumple o no cumple", "Ayuda a detectar problemas de forma ordenada."),
        ("¿Qué priorizas primero en un plan de mejora?", "Lo que puede causar daño inmediato a personas", "El riesgo inmediato va antes que el orden general."),
        ("¿Se sacan documentos con datos personales de la oficina?", "No, salvo con autorización de la jefatura", "Los datos personales deben resguardarse y no salir sin autorización."),
    ],
    op=("Haz una lista de verificación de ejemplo con seis ítems para un puesto de trabajo contable y marca cuáles cumple y cuáles no (inventa la revisión). Para cada ítem pendiente escribe una acción con responsable, plazo y comprobación, y ordénalas por prioridad con una razón.",
        "Ítems: pasillo despejado (cumple); cables ordenados (cumple); documentos reservados bajo llave (no cumple); copia de seguridad hecha (no cumple); pausas breves realizadas (cumple); carpetas rotuladas (cumple). Acción 1: guardar documentos reservados bajo llave hoy, a cargo de la auxiliar; se comprueba al cerrar. Acción 2: hacer la copia el viernes, a cargo del contador; se comprueba abriéndola. Prioridad: primero los documentos reservados porque exponen datos personales.",
        ["lista de seis ítems con revisión", "acciones con responsable, plazo y comprobación", "prioridad justificada"],
        ["hoja con la lista, las acciones y la prioridad"],
        ["dar un diagnóstico médico", "no incluir plazo o responsable", "no justificar la prioridad"],
        "Pregunta: «¿cómo sabrías que la acción se cumplió?». Si no hay comprobación, pídele una forma concreta."),
    reinforce="Escribe una lista de verificación de cuatro ítems para el escritorio de tu casa donde estudias.",
    extend="Explica con un ejemplo inventado por qué una lista de verificación no reemplaza a un profesional de prevención.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 26 (situaciones de atención de ejemplo en «Papelería Los Aromos SpA»). (1) La jefa de ventas pide al área contable el saldo de un cliente. (2) Un cliente llama preguntando por una factura. "
     "(3) Un proveedor pregunta cuándo se le pagará. (4) Una persona desconocida pide ver la lista de clientes. Cliente interno: persona o área de la misma empresa que usa tu trabajo. "
     "Cliente externo: persona o empresa de afuera de la empresa.")
build(
    O7, 1, F,
    use="Aprenderé quiénes son los clientes internos y externos de un área contable, cómo atenderlos con respeto y cómo proteger la información.",
    prior=["Sé qué es información confidencial.", "Sé qué es un cliente y un proveedor.", "Sé qué es un dato personal."],
    explain=[
        "Atender a clientes es responder a las personas que necesitan algo de tu trabajo. Un cliente interno es una persona o un área de la misma empresa, como ventas o bodega, que usa la información contable. Un cliente externo es alguien de afuera: clientes que compran, proveedores a quienes se les paga, el banco o una persona que consulta.",
        "La buena atención se apoya en cinco actitudes: saludar e identificarse, escuchar sin interrumpir, hablar con claridad y respeto, responder con datos comprobados y cumplir los plazos que se prometen. Si no sabes la respuesta, dices que lo vas a averiguar y comprometes un plazo, o derivas a quien corresponde; no inventas una respuesta.",
        "La información de un cliente es confidencial. No se entrega información de otro cliente ni datos personales (teléfono, dirección, correo) a quien no está autorizado. Si alguien levanta la voz o amenaza, mantienes la calma y avisas de inmediato a la jefatura o a una persona adulta responsable; no confrontas. Los protocolos de cada empresa se siguen según lo que indique la jefatura.",
    ],
    vocab=[("cliente interno", "persona o área de la misma empresa que usa tu trabajo"), ("cliente externo", "persona o empresa de afuera que necesita algo de la empresa"), ("derivar", "pasar una consulta a quien corresponde y avisar a quien consultó"), ("plazo", "tiempo comprometido para responder"), ("empatía", "intentar entender lo que siente la otra persona"), ("autorizado", "con permiso para recibir cierta información")],
    worked=[
        ("Clasificar al cliente", "El jefe de bodega de una empresa de ejemplo pide a contabilidad el valor de las existencias. ¿Es cliente interno o externo?", ["Pertenece a la misma empresa.", "Usa el trabajo del área contable: es cliente interno."], "Cliente interno"),
        ("Responder cuando no sabes", "Un cliente de ejemplo pregunta algo que no sabes. ¿Qué respondes?", ["No inventas.", "Dices que lo averiguarás, anotas el dato de contacto autorizado y comprometes un plazo, o derivas a quien sabe."], "Que lo averiguas y comprometes un plazo, o derivas"),
    ],
    mistakes=[("Responder de memoria una cifra que no recuerdas bien.", "Se entrega información incorrecta y se pierde la confianza.", "Revisa el registro antes de responder o compromete un plazo."),
              ("Entregar el teléfono de otro cliente a quien lo pide por amabilidad.", "Los datos personales no se comparten sin autorización.", "Ofrece tomar el mensaje o derivar a la jefatura.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es un cliente interno?", "Una persona o área de la misma empresa que usa tu trabajo", "Una persona que compra a la empresa", "Un proveedor al que se le paga", "Interno significa dentro de la empresa, como el área de ventas."),
        ("abc", "¿Qué es un cliente externo?", "Una persona o empresa de afuera que necesita algo de la empresa", "Otra área de la misma oficina", "Un compañero de trabajo", "Externo significa fuera de la empresa."),
        ("ab", "{F} La situación (1), la jefa de ventas pide el saldo de un cliente, ¿qué tipo de cliente es?", "Cliente interno", "Cliente externo", "La jefa de ventas trabaja en la misma empresa."),
        ("abc", "{F} En la situación (3), ¿qué tipo de cliente es el proveedor?", "Cliente externo", "Cliente interno", "Un trabajador de la empresa", "El proveedor está fuera de la empresa."),
        ("abc", "{F} En la situación (4), una persona desconocida pide la lista de clientes. ¿Qué corresponde?", "No entregarla y consultar a la jefatura", "Entregarla completa", "Entregar solo la mitad", "La lista de clientes es confidencial y solo se entrega a quien está autorizado."),
        ("abc", "¿Cuál es la primera acción al atender a una persona?", "Saludar e identificarse", "Pedirle sus datos personales de inmediato", "Responder sin escucharla", "Un saludo claro abre una atención respetuosa."),
        ("=", "{F} Cada consulta toma en promedio 5 minutos (cifra de ejemplo). ¿Cuántos minutos toman 18 consultas internas y 12 externas?", "(18+12)*5", "Se suma la cantidad de consultas y se multiplica por los minutos de cada una.", " minutos"),
        ("abc", "¿Por qué no se entrega a un cliente información de otro cliente?", "Porque es información confidencial y puede incluir datos personales", "Porque la información de otros clientes es pública", "Porque solo le importa al banco", "La información de cada cliente se protege."),
        ("abc", "¿Por qué atender bien a un cliente interno es parte del trabajo contable?", "Porque su trabajo depende de recibir información correcta y a tiempo", "Porque solo los clientes externos importan", "Porque nunca pide nada importante", "Los clientes internos usan la información para decidir."),
        ("abc", "Un cliente molesto levanta la voz por teléfono. ¿Qué haces?", "Mantener la calma, escuchar y registrar el reclamo", "Responder también en voz alta", "Cortar la llamada sin avisar", "La calma y la escucha bajan la tensión y permiten resolver."),
        ("abc", "Un cliente te hace una pregunta que no sabes responder. ¿Qué corresponde?", "Decir que lo averiguarás y comprometer un plazo, o derivar a quien sabe", "Inventar una respuesta que suene bien", "Decir que no es tu problema", "Mejor reconocer que no sabes y comprometer una respuesta que improvisar."),
        ("=", "En una semana de ejemplo se comprometió responder 30 consultas dentro del plazo y se respondieron 27 a tiempo. ¿Qué porcentaje se respondió a tiempo?", "27*100//30", "Se divide lo respondido a tiempo por el total y se multiplica por 100.", " %"),
        ("abc", "Un cliente externo pide el correo personal del dueño de la empresa. ¿Qué corresponde?", "Ofrecer tomar el mensaje y derivarlo, sin entregar datos personales", "Entregar el correo para ser amable", "Entregar el teléfono para ser más rápido", "Los datos personales del dueño tampoco se entregan sin autorización."),
    ],
    ctx=("abc", "Una persona que dice ser «amiga del dueño» pide por teléfono el saldo que debe un cliente. No la conoces. ¿Qué haces?", "Le explico que no puedo entregar esa información y derivo a la jefatura", "Se lo digo porque suena amable", "Le pido que lo anote para que no se le olvide", "La información de un cliente solo se entrega a quien está autorizado."),
    sc=[
        ("En Contabilidad: ¿qué es un cliente interno?", "Una persona o área de la misma empresa que usa tu trabajo", "Interno quiere decir que pertenece a la empresa."),
        ("¿Qué haces si no sabes la respuesta a una consulta?", "Digo que lo averiguaré y comprometo un plazo, o derivo", "No se inventan respuestas: se averigua y se compromete un plazo."),
        ("¿Qué haces si alguien levanta la voz o amenaza?", "Mantengo la calma y aviso a la jefatura o a una persona adulta responsable", "No se confronta; se pide ayuda a quien corresponde."),
    ],
    op=("Clasifica estas cuatro personas de una empresa de ejemplo como cliente interno o externo y escribe una frase de respuesta amable para cada una: (a) la jefa de bodega pide el costo de una mercadería; (b) un proveedor pregunta la fecha de pago de una factura; (c) un cliente llama molesto por un cobro; (d) una persona desconocida pide la lista de clientes.",
        "(a) Interna: «Le envío el costo hoy, revisado en el registro». (b) Externo: «Reviso la factura y le confirmo la fecha de pago con el contador». (c) Externo: «Entiendo su molestia; anoto su reclamo y lo reviso con los documentos». (d) Externa: «No puedo entregar esa información; consulto a la jefatura».",
        ["clasifica correctamente a cada persona", "usa un tono respetuoso", "protege la información en el caso (d)"],
        ["tabla con cuatro personas, su clasificación y su respuesta"],
        ["entregar la lista de clientes", "inventar una respuesta", "no clasificar a la persona"],
        "Pregunta: «¿por qué no entregas la lista?». Si no habla de confidencialidad, repasa las reglas de información."),
    reinforce="Escribe tres frases amables para saludar y despedir a una persona que consulta por una factura.",
    extend="Explica con un ejemplo inventado por qué la buena atención interna mejora la atención a clientes externos.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 27 (registro de atenciones de ejemplo). R1: un cliente pregunta cuánto debe (consulta). R2: un cliente dice que se le cobró dos veces una factura (reclamo). "
     "R3: un cliente pide copia de una factura (solicitud). R4: un proveedor pregunta la fecha de pago (consulta). Protocolo de ejemplo: saludar, escuchar, registrar, resolver o derivar y cerrar confirmando.")
build(
    O7, 2, F,
    use="Aprenderé a distinguir consultas, reclamos y solicitudes, a seguir un protocolo de atención y a usar el registro y el estado de cuenta.",
    prior=["Sé quién es un cliente interno y uno externo.", "Sé qué es una factura y un pago.", "Sé sumar y restar importes."],
    explain=[
        "Las personas se comunican con el área contable por tres motivos. Una consulta es una pregunta que se responde con datos. Un reclamo es una molestia por algo que la persona cree incorrecto, como un cobro doble. Una solicitud es un pedido de algo concreto, como la copia de una factura. Distinguirlas ayuda a decidir qué se hace y a quién se deriva.",
        "El protocolo de atención tiene cinco pasos: saludar, escuchar, registrar, resolver o derivar y cerrar confirmando. El registro de atención lleva la fecha, quién consulta, el motivo, la respuesta o derivación y el plazo comprometido. Un estado de cuenta es la lista de las facturas y pagos de un cliente con su saldo; sirve para responder con datos.",
        "Las comunicaciones de cobranza son respetuosas: recuerdan la factura, su monto y su vencimiento, ofrecen aclarar dudas y no amenazan ni exponen a la persona. Si un cliente pide que no se le llame más, se respeta y se consulta a la jefatura qué otro canal usar. No se comparten datos del cliente con terceros.",
    ],
    vocab=[("consulta", "pregunta que se responde con datos"), ("reclamo", "molestia por algo que la persona cree incorrecto"), ("solicitud", "pedido de algo concreto"), ("registro de atención", "anotación de fecha, motivo, respuesta y plazo"), ("estado de cuenta", "lista de facturas y pagos de un cliente con su saldo"), ("cobranza", "gestión para que se pague lo adeudado")],
    worked=[
        ("Clasificar el motivo", "Un cliente de ejemplo dice: «me llegó una factura que ya había pagado». ¿Es consulta, reclamo o solicitud?", ["Expresa una molestia por un cobro que cree incorrecto.", "Es un reclamo."], "Reclamo"),
        ("Calcular un saldo", "Un cliente de ejemplo tiene facturas por $70.000 y $30.000 y pagó $40.000. ¿Cuánto debe?", ["Facturas: 70.000 + 30.000 = 100.000.", "Saldo: 100.000 − 40.000 = 60.000."], "$60.000"),
    ],
    mistakes=[("Tratar un reclamo como si fuera una simple consulta.", "La persona queda sin respuesta a su molestia y el problema continúa.", "Registra el reclamo, revisa los documentos y responde con un plazo."),
              ("Enviar un mensaje de cobranza con amenazas.", "No es respetuoso y puede afectar a la persona y a la empresa.", "Escribe un recordatorio claro y cortés.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es una consulta?", "Una pregunta que se responde con datos", "Una molestia por un cobro incorrecto", "Un pedido de copia de un documento", "La consulta pide información; el reclamo expresa molestia y la solicitud pide algo concreto."),
        ("abc", "¿Qué es un reclamo?", "Una molestia por algo que la persona cree incorrecto", "Una pregunta sobre un horario", "Un pedido de un documento", "El reclamo expresa disconformidad con algo que la persona cree incorrecto."),
        ("ab", "{F} R3, el cliente pide copia de una factura. ¿Qué tipo de atención es?", "Una solicitud", "Un reclamo", "Pide algo concreto, por eso es una solicitud."),
        ("abc", "{F} R2, el cliente dice que se le cobró dos veces una factura. ¿Qué tipo de atención es?", "Un reclamo", "Una consulta", "Una solicitud", "Expresa molestia por un cobro que cree incorrecto."),
        ("abc", "{F} ¿Cuál es el orden del protocolo de atención?", "Saludar, escuchar, registrar, resolver o derivar y cerrar confirmando", "Registrar, cerrar, saludar, escuchar y resolver", "Resolver, saludar, cerrar, registrar y escuchar", "Se parte por saludar y escuchar y se termina confirmando con la persona."),
        ("abc", "{F} R2, el reclamo por cobro doble. ¿A quién se deriva para revisar las facturas?", "Al contador o a la persona responsable de revisar las facturas", "A otro cliente", "Al proveedor", "Quien revisa los documentos es quien puede resolver el reclamo."),
        ("abc", "¿Qué debe llevar un registro de atención?", "Fecha, quién consulta, motivo, respuesta o derivación y plazo", "Solo el nombre", "Solo la respuesta", "Con estos datos se puede dar seguimiento."),
        ("=", "Un cliente de ejemplo tiene facturas por $120.000, $80.000 y $50.000 y pagó $100.000. ¿Cuántos pesos debe?", "120000+80000+50000-100000", "Se suman las facturas y se resta lo pagado.", " pesos"),
        ("abc", "¿Qué es un estado de cuenta?", "La lista de facturas y pagos de un cliente con su saldo", "El informe de gastos de la empresa", "Una factura nueva", "Muestra qué se facturó, qué se pagó y qué queda."),
        ("abc", "¿Cuál de estos mensajes de cobranza es adecuado?", "«Le recordamos que la factura N.º 215 por $120.000 venció el 5 de mayo. Si ya la pagó, por favor avísenos para actualizar el registro»", "«Pague ya o publicaremos su nombre en la oficina»", "«Su deuda es una vergüenza»", "El mensaje respetuoso informa y ofrece aclarar, sin amenazar ni exponer."),
        ("=", "En un mes de ejemplo se registraron 40 atenciones y 6 fueron reclamos. ¿Qué porcentaje fueron reclamos?", "6*100//40", "Se divide el número de reclamos por el total y se multiplica por 100.", " %"),
        ("abc", "Un cliente pide que no se le llame más. ¿Qué corresponde?", "Respetar su solicitud, registrarla y consultar a la jefatura qué canal usar", "Seguir llamándolo por si cambia de idea", "Borrar sus datos sin avisar a nadie", "La preferencia de la persona se respeta y se informa a la jefatura."),
        ("abc", "{F} R4, un proveedor pregunta la fecha de pago. ¿Qué respuesta es adecuada si no tienes el dato?", "«Reviso la factura y le confirmo hoy; si corresponde, consulto con el contador»", "«Pagaremos mañana» sin saberlo", "«No sé y no me interesa»", "No se prometen fechas que no se conocen."),
    ],
    ctx=("abc", "Un cliente llama enojado porque cree que se le cobró una factura dos veces. Aún no revisas nada. ¿Qué haces?", "Escucho, registro el reclamo, reviso los documentos y respondo con un plazo", "Le digo que se equivoca", "Le prometo que ya se arregló", "Primero se revisa con documentos y se responde con datos comprobables."),
    sc=[
        ("En Contabilidad: ¿qué es un reclamo?", "Una molestia por algo que la persona cree incorrecto", "Se atiende registrándolo y revisando los documentos."),
        ("¿Cuáles son los pasos del protocolo de atención?", "Saludar, escuchar, registrar, resolver o derivar y cerrar confirmando", "Ese orden asegura una atención completa."),
        ("¿Cómo debe ser un mensaje de cobranza?", "Respetuoso, claro y sin amenazas", "Informa la factura y ofrece aclarar dudas."),
    ],
    op=("Un cliente de ejemplo tiene tres facturas: $90.000, $60.000 y $40.000, y pagó $70.000. Calcula su saldo, escribe un mensaje de cobranza respetuoso de tres líneas (sin amenazas) con una factura de ejemplo N.º 410 por $90.000 vencida, y completa un registro de atención con fecha de ejemplo, motivo y plazo.",
        "Saldo: 190.000 − 70.000 = 120.000. Mensaje: «Estimado cliente: le recordamos que la factura N.º 410 por $90.000 está vencida. Si ya la pagó, por favor avísenos para actualizar el registro. Quedamos atentos a cualquier duda». Registro: fecha de ejemplo; motivo: cobranza; respuesta: mensaje enviado; plazo: 5 días.",
        ["calcula el saldo correctamente", "redacta un mensaje respetuoso", "completa el registro con motivo y plazo"],
        ["hoja con el saldo, el mensaje y el registro"],
        ["amenazar al cliente", "no restar el pago", "dejar el registro sin plazo"],
        "Pregunta: «¿qué haría el cliente si lee tu mensaje?». Si siente presión, pide reescribirlo con más cortesía."),
    reinforce="Escribe una consulta, un reclamo y una solicitud distintos que podría hacer un cliente a una empresa.",
    extend="Explica con un ejemplo inventado por qué un registro de atención ayuda a quien continúa el caso al día siguiente.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 28 (caso de ejemplo). «Colegio Los Alerces» (cliente de ejemplo) llama y dice que pagó la factura N.º 450 de $99.000 el 12 de mayo y que se le sigue cobrando. "
     "Registro de «Papelería Los Aromos SpA»: factura N.º 450 por $99.000, emitida el 2 de mayo; pago de $99.000 recibido el 12 de mayo (comprobante de ingreso N.º 77); "
     "factura N.º 451 por $99.000, emitida el 20 de mayo, sin pagar. Un aviso de cobranza enviado el 25 de mayo menciona por error la factura N.º 450.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un reclamo con los documentos, a identificar la causa y a responder con datos y respeto.",
    prior=["Sé qué es un reclamo y el protocolo de atención.", "Sé calcular saldos.", "Sé qué respalda un pago."],
    explain=[
        "Un reclamo se analiza en cuatro pasos: escuchar y registrar los datos que da el cliente (factura, monto, fecha), revisar los documentos y registros que lo comprueban, identificar la causa del problema y responder con datos y un plazo. No se discute con la persona ni se responde de memoria.",
        "En el caso, el registro muestra que la factura N.º 450 está pagada el 12 de mayo y que lo pendiente es la N.º 451. El aviso de cobranza mencionó por error la N.º 450. La causa es una confusión de la empresa, no del cliente. La respuesta reconoce la confusión, indica qué está pagado y qué está pendiente y se compromete a corregir el aviso.",
        "Después de responder se cierra confirmando con el cliente lo acordado, se deja constancia en el registro y se avisa a la jefatura del error para evitar que se repita. Si el cliente pide enviar datos a otro correo, se verifica antes su identidad y su autorización.",
    ],
    vocab=[("causa", "origen del problema"), ("comprobante de ingreso", "constancia interna de un cobro recibido"), ("aviso de cobranza", "mensaje que recuerda un pago pendiente"), ("verificar la identidad", "comprobar que quien pide es quien dice ser"), ("constancia", "anotación que deja registro de lo ocurrido")],
    worked=[
        ("Revisar con documentos", "Un cliente de ejemplo dice que pagó la factura N.º 20 de $50.000. El registro muestra un pago de $50.000 con comprobante N.º 5. ¿Qué concluyes?", ["El pago está registrado con su comprobante.", "La factura N.º 20 figura pagada."], "La factura N.º 20 está pagada"),
        ("Redactar la respuesta", "Con ese resultado, escribe una respuesta breve al cliente.", ["Se reconoce la molestia.", "Se informa lo comprobado y se compromete a corregir el aviso."], "Revisamos su caso: la factura N.º 20 figura pagada (comprobante N.º 5); corregiremos el aviso y lamentamos la confusión"),
    ],
    mistakes=[("Responder «usted se equivoca» antes de revisar.", "Se discute sin datos y se pierde la confianza.", "Escucha, revisa los documentos y responde con lo comprobado."),
              ("Enviar el estado de cuenta a otro correo sin verificar.", "Se pueden entregar datos a una persona no autorizada.", "Verifica identidad y autorización antes de enviar.")],
    T=[
        ("abc", "{F} ¿Qué tipo de atención es la llamada del colegio?", "Un reclamo", "Una solicitud", "Una consulta de horario", "El colegio expresa molestia por un cobro que cree incorrecto."),
        ("abc", "{F} ¿Cuál es el primer paso con este reclamo?", "Escuchar y registrar factura, monto y fecha que da el cliente", "Decirle que se equivoca", "Cortar y llamar después", "Primero se escucha y se registra la información que da el cliente."),
        ("=", "{F} ¿Cuántos pesos suman en total las facturas N.º 450 y N.º 451?", "99000+99000", "Se suman los montos de ambas facturas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos debe realmente el colegio, considerando el pago recibido?", "99000+99000-99000", "Se restan los pagos recibidos al total facturado.", " pesos"),
        ("abc", "{F} ¿Qué documento del registro respalda el pago de la factura N.º 450?", "El comprobante de ingreso N.º 77, del 12 de mayo", "El aviso de cobranza del 25 de mayo", "La factura N.º 451", "El comprobante de ingreso prueba que se recibió el pago."),
        ("abc", "{F} ¿Cuál es la causa probable de la confusión?", "El aviso de cobranza mencionó por error la factura N.º 450, que ya estaba pagada", "El colegio no pagó la factura N.º 450", "La factura N.º 450 no existe", "El registro indica un error en el aviso de cobranza, no un pago faltante."),
        ("abc", "{F} ¿Qué respuesta es adecuada para el colegio?", "«Revisamos su caso: la factura N.º 450 figura pagada el 12 de mayo (comprobante 77); lo pendiente es la N.º 451 por $99.000. Lamentamos la confusión del aviso»", "«Usted se equivoca, debe pagar»", "«Ignore el aviso y no pague nada»", "La respuesta debe informar con datos qué está pagado y qué pendiente, y reconocer el error."),
        ("abc", "{F} ¿Qué se hace con el aviso erróneo?", "Informar a la jefatura para corregir el aviso y dejar constancia", "No hacer nada", "Enviar otro aviso igual", "El error se corrige y se deja constancia para evitar que se repita."),
        ("=", "{F} ¿Cuántos días pasaron desde la emisión de la factura N.º 451 (20 de mayo) hasta el aviso (25 de mayo)?", "25-20", "Se resta la fecha de emisión a la fecha del aviso.", " días"),
        ("abc", "¿Por qué se verifica con documentos antes de responder?", "Para responder con datos comprobables y no de memoria", "Para hacer esperar al cliente", "Para demostrar quién tiene la razón", "Responder con documentos da confianza y evita errores."),
        ("abc", "Un cliente pide enviar el estado de cuenta a un correo distinto del registrado. ¿Qué corresponde?", "Verificar su identidad y autorización antes de enviarlo", "Enviarlo de inmediato", "Negarse sin dar explicación", "Los datos solo se entregan a quien está autorizado."),
        ("=", "{F} Si el colegio pagara la factura N.º 451 y tuviera una nota de crédito por $9.000 por una devolución, ¿cuántos pesos pagaría?", "99000-9000", "La nota de crédito reduce el monto a pagar.", " pesos"),
        ("abc", "¿Cuál es un buen cierre de la atención?", "Confirmar con el cliente lo acordado y el plazo, y registrar la atención", "Colgar sin despedirse", "Prometer algo sin anotarlo", "El cierre confirma lo acordado y deja constancia."),
    ],
    ctx=("abc", "Tu jefa te dice que respondas al colegio «que se equivoca», aunque el registro muestra el pago. ¿Qué haces?", "Le muestro el comprobante a la jefa y propongo responder con los datos del registro", "Obedezco y le digo al cliente que se equivoca", "No respondo al cliente", "Responder con datos comprobados protege a la empresa y a la persona."),
    sc=[
        ("En Contabilidad: ¿qué se hace primero ante un reclamo?", "Escuchar y registrar los datos que da el cliente", "Así se tiene el dato que luego se revisa."),
        ("¿Con qué se responde un reclamo?", "Con datos comprobados en los documentos", "La respuesta debe poder demostrarse con un documento o registro."),
        ("¿Qué se hace después de responder?", "Confirmar lo acordado y dejar constancia", "El registro permite dar seguimiento al caso al día siguiente."),
    ],
    op=("Un cliente de ejemplo llama diciendo que no recibió la mercadería de la factura N.º 612 por $75.000. El registro muestra la guía de despacho N.º 88 con recepción firmada el 4 de junio. Escribe los cuatro pasos del análisis, una respuesta de tres líneas con respeto y qué derivarías al contador.",
        "Pasos: escuchar y registrar; revisar la guía N.º 88 firmada; identificar que hay una recepción firmada; responder con un plazo. Respuesta: «Revisamos su caso: la guía N.º 88 figura recibida y firmada el 4 de junio. Si desea, revisamos juntos quién la recibió. Le confirmo en 2 días». Derivar al contador la verificación de la firma y la factura.",
        ["sigue los cuatro pasos", "responde con datos y respeto", "deriva lo que corresponde"],
        ["hoja con pasos, respuesta y derivación"],
        ["acusar al cliente", "no usar la guía", "prometer algo sin comprobar"],
        "Pregunta: «¿qué dato apoya tu respuesta?». Si no nombra la guía, repasa el uso de documentos."),
    reinforce="Escribe tres frases cordiales para responder un reclamo usando datos de un documento.",
    extend="Explica con un ejemplo inventado cómo corregir un aviso erróneo evita nuevos reclamos.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 29 (cola de atención de ejemplo, una mañana). S1: un proveedor pide la fecha de pago de una factura de $200.000, emitida con crédito a 30 días y vencida hace 10 días. "
     "S2: la jefa de ventas pide con urgencia el saldo de un cliente para una reunión a las 11:00. S3: un cliente pide copia de la factura N.º 520. "
     "S4: una persona desconocida llama pidiendo los datos de contacto de otro cliente. Reglas: priorizar por urgencia y plazo; verificar identidad antes de entregar datos; derivar lo que no te corresponde.")
build(
    O7, 4, F,
    use="Aprenderé a priorizar atenciones, verificar identidad, derivar lo que no me corresponde y mantener un trato respetuoso aun en situaciones difíciles.",
    prior=["Sé el protocolo de atención.", "Sé qué es información confidencial.", "Sé calcular tiempos y porcentajes."],
    explain=[
        "Cuando hay varias solicitudes a la vez se prioriza por urgencia y plazo: primero lo que tiene una hora límite cercana o que afecta a otras personas. Cada solicitud se registra y se contesta; las que no te corresponden se derivan a quien sabe, avisando a la persona que consultó.",
        "Antes de entregar datos a alguien se verifica su identidad y su autorización. Una persona desconocida que pide datos de contacto de un cliente no los recibe: se le ofrece tomar el mensaje y derivar a la jefatura. Nunca se prometen fechas ni resultados que no dependan de ti: se dice que se consultará y se compromete un plazo para responder.",
        "Si una persona insulta o amenaza, mantienes la calma, no respondes con agresión y avisas a la jefatura o a una persona adulta responsable; si hay riesgo, pides ayuda de inmediato. Después se deja constancia de lo ocurrido. Este ejercicio es práctica en papel y el protocolo real lo define cada empresa.",
    ],
    vocab=[("priorizar", "decidir qué se atiende primero"), ("urgencia", "necesidad de responder pronto por una hora límite"), ("verificar identidad", "comprobar que quien pide es quien dice ser"), ("derivar", "pasar la solicitud a quien corresponde"), ("compromiso", "promesa de hacer algo en cierto plazo")],
    worked=[
        ("Priorizar", "Una mañana de ejemplo tiene tres solicitudes: copia de una factura sin plazo, saldo de un cliente para una reunión en 30 minutos y una consulta general. ¿Cuál va primero?", ["Se mira la urgencia: la reunión en 30 minutos es la más próxima.", "Esa solicitud va primero."], "El saldo para la reunión"),
        ("No prometer lo que no dependes", "Un proveedor de ejemplo pide la fecha exacta de pago, pero la decide el contador. ¿Qué respondes?", ["No inventas ni prometes una fecha.", "Dices que consultarás con el contador y le confirmarás hoy."], "Que consultas con el contador y confirmas hoy"),
    ],
    mistakes=[("Atender primero lo más fácil aunque otra solicitud tenga una hora límite.", "Se incumple un plazo importante.", "Prioriza por urgencia y plazo."),
              ("Dar el teléfono de otro cliente a una persona desconocida «por amabilidad».", "Se entregan datos personales sin autorización.", "Ofrece tomar el mensaje y deriva a la jefatura.")],
    T=[
        ("abc", "{F} ¿Cuál solicitud se atiende primero por urgencia?", "S2, porque la reunión es a las 11:00", "S3, porque es la más fácil", "S1, porque el monto es mayor", "S2 tiene una hora límite próxima; las otras no."),
        ("abc", "{F} En S4, ¿qué corresponde?", "No entregar los datos y ofrecer tomar el mensaje o derivar a la jefatura", "Entregarlos porque pide con amabilidad", "Entregar solo el teléfono", "Los datos personales no se entregan a una persona desconocida."),
        ("abc", "{F} En S3, ¿qué se verifica antes de enviar la copia de la factura?", "Que quien la pide sea el cliente o esté autorizado", "Que la copia esté en color", "Que sea lunes", "La copia contiene datos del cliente y solo se entrega a quien corresponde."),
        ("=", "{F} En S1, ¿cuántos días pasaron desde la emisión de la factura hasta hoy (30 días de crédito más 10 días de atraso)?", "30+10", "Se suman los días de crédito y los días vencidos.", " días"),
        ("abc", "{F} En S1, ¿qué respuesta es adecuada?", "«Reviso la factura y le confirmo hoy la fecha; consulto con el contador»", "«Le pagamos mañana» sin saberlo", "«No sé y no es mi tema»", "No se prometen fechas que no dependen de ti."),
        ("abc", "¿Qué pasa si prometes algo que no depende de ti?", "Puedes incumplir y perder la confianza de la persona", "Nada, porque las promesas no importan", "La persona siempre lo olvida", "Prometer sin poder cumplir daña la confianza."),
        ("=", "{F} La mañana dura 4 horas y cada una de las 4 solicitudes toma 20 minutos. ¿Cuántos minutos libres quedan?", "4*60-4*20", "Se restan los minutos de atención al total de minutos de la mañana.", " minutos"),
        ("abc", "¿Qué significa derivar?", "Pasar la solicitud a quien corresponde y avisar a quien consultó", "No responder", "Rechazar la solicitud sin explicar", "Derivar es una forma de resolver con la persona correcta."),
        ("abc", "¿Por qué se verifica la identidad antes de entregar datos?", "Para no entregar información a quien no corresponde", "Para retrasar la atención", "Porque es una costumbre sin motivo", "La verificación protege la confidencialidad de los datos de los clientes."),
        ("abc", "Un compañero da a la persona desconocida el teléfono de un cliente «por amabilidad». ¿Qué error comete?", "Entregó datos personales sin verificar ni tener autorización", "Fue puntual", "Registró mal la hora", "Los datos personales se entregan solo con autorización."),
        ("abc", "Un cliente insulta a quien lo atiende. ¿Qué corresponde?", "Mantener la calma, avisar a la jefatura y dejar constancia", "Insultar también", "Guardar silencio y no avisar a nadie", "Se responde con calma y se pide ayuda a quien corresponde."),
        ("=", "En una semana de ejemplo, 17 de 20 solicitudes se respondieron dentro del plazo. ¿Qué porcentaje fue?", "17*100//20", "Se divide lo respondido a tiempo por el total y se multiplica por 100.", " %"),
        ("abc", "¿Qué límite tiene este cuaderno respecto de la atención real?", "Es práctica en papel; el protocolo real lo define cada empresa", "Reemplaza el protocolo de la empresa", "Autoriza a entregar datos sin permiso", "El cuaderno ayuda a practicar, pero no sustituye las reglas de cada empresa."),
    ],
    ctx=("abc", "Dos solicitudes llegan a la vez: un cliente sin plazo pide una copia de factura y la jefa de ventas pide un saldo para una reunión en 15 minutos. ¿Qué haces?", "Atiendo primero a la jefa y aviso al cliente que enviaré su copia más tarde, con un plazo", "Atiendo primero al cliente y dejo a la jefa esperando", "Atiendo a ambas sin orden", "Se prioriza por urgencia y se informa un plazo a quien espera."),
    sc=[
        ("En Contabilidad: ¿cómo se prioriza una cola de solicitudes?", "Por urgencia y plazo", "Se atiende primero lo que tiene hora límite cercana."),
        ("¿Qué se hace antes de entregar datos a alguien?", "Verificar su identidad y su autorización", "Así se protege la información de los clientes."),
        ("¿Qué haces si no te corresponde resolver algo?", "Lo derivo a quien corresponde y aviso a quien consultó", "La persona debe saber quién resolverá su caso."),
    ],
    op=("Ordena por prioridad estas cuatro solicitudes de una mañana de ejemplo y escribe una frase de respuesta para cada una: (a) copia de una factura sin urgencia; (b) la jefa de ventas pide un saldo para una reunión en 20 minutos; (c) un proveedor pide la fecha de pago, que decide el contador; (d) una persona desconocida pide datos de un cliente.",
        "Orden: (b) por la hora límite, (c) porque un proveedor espera una respuesta, (a) y (d) al final (en (d) no se entrega nada). Respuestas: (b) «Te lo envío ahora, revisado». (c) «Consulto con el contador y le confirmo hoy». (a) «Le envío la copia hoy después de verificar quién la pide». (d) «No puedo entregar esa información; consulto a la jefatura».",
        ["prioriza por urgencia", "no promete lo que no depende de ella o él", "protege los datos de la persona desconocida"],
        ["hoja con el orden y cuatro respuestas"],
        ["entregar datos a la persona desconocida", "prometer una fecha de pago", "no priorizar"],
        "Pregunta: «¿por qué esa primera?». Si no menciona la hora límite, repasa la priorización."),
    reinforce="Escribe dos frases para decir con amabilidad que no puedes entregar cierta información.",
    extend="Explica con un ejemplo inventado por qué es mejor derivar bien que responder rápido pero mal.",
)

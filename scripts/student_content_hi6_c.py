"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 23 (proyectos de aporte con plan y presupuesto)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI06 OA 23"
MAT = "Lápiz y papel. Los casos, los planes y los precios están escritos en cada ejercicio; no necesitas internet ni comprar nada."

# ---------------------------------------------------------------- Clase 1
build(
    OA, 1, "",
    use="Aprenderé a ubicar un proyecto de aporte: qué necesidad atiende, dónde, cuándo y para quiénes. Sirve para elegir un proyecto realista antes de hacer el plan y el presupuesto.",
    prior=["Sé que ayudar a otras personas es una forma de participar.", "Sé leer fechas y calcular cuántos días hay entre dos fechas.", "Sé que un problema tiene causas, actores y consecuencias."],
    explain=[
        "Un proyecto es un conjunto de acciones ordenadas para lograr un objetivo en un plazo. En esta clase hablamos de proyectos de aporte: acciones concretas para ayudar. Un voluntariado es un trabajo que una persona hace por decisión propia, sin recibir pago, para ayudar a otros. La ayuda social es el apoyo a personas que lo necesitan, por ejemplo con abrigo, alimentos o compañía.",
        "Antes de actuar hay que ubicar el proyecto. Me pregunto: ¿qué necesidad hay?, ¿en qué lugar?, ¿cuándo se hará? y ¿para quiénes? También decido el ámbito, o sea, hasta dónde llega el aporte. En la escuela, el aporte queda dentro del colegio. En la comunidad, llega al barrio o a la comuna, con vecinos e instituciones cercanas. En la sociedad, llega a personas del país o de lugares lejanos.",
        "Un buen proyecto debe ser realista: se puede lograr con el tiempo, las personas y el dinero que hay. Prometer ayudar a todo el país en una semana no es realista. El orden de trabajo es: detectar la necesidad, fijar un objetivo, hacer el plan, calcular el presupuesto, realizar las actividades y evaluar los resultados.",
    ],
    vocab=[("proyecto", "conjunto de acciones ordenadas para lograr un objetivo en un plazo"), ("voluntariado", "trabajo que se hace por decisión propia, sin pago, para ayudar"), ("ayuda social", "apoyo a personas que lo necesitan"), ("ámbito", "hasta dónde llega un aporte: escuela, comunidad o sociedad"), ("realista", "que se puede lograr con el tiempo, las personas y el dinero disponibles")],
    worked=[
        ("Ubicar un proyecto", "Un curso quiere pintar el mural del patio de su colegio durante las dos primeras semanas de noviembre. ¿Cuál es el ámbito y cuál es el lugar?",
         ["Pregunto hasta dónde llega el aporte: solo al colegio.", "El ámbito es la escuela.", "El lugar es el patio del colegio."], "Ámbito: escuela; lugar: el patio del colegio"),
        ("Revisar si es realista", "Un grupo de 5 voluntarios quiere repartir ropa a un país entero en 4 días. ¿Es un proyecto realista?",
         ["Miro el tiempo: 4 días.", "Miro las personas: solo 5.", "El alcance es demasiado grande para ese tiempo y esas personas."], "No es realista"),
    ],
    mistakes=[
        ("Elegir un proyecto enorme para impresionar.", "Si no alcanza el tiempo ni el dinero, el proyecto no se termina.", "Reduce el alcance hasta que sea posible con lo que tienes."),
        ("Empezar a comprar o a repartir antes de ubicar la necesidad.", "Se puede ayudar en algo que no era lo más urgente.", "Primero pregunta qué necesidad hay, dónde, cuándo y para quiénes."),
    ],
    T=[
        ("¿Qué es un voluntariado?", "Un trabajo que una persona hace por decisión propia, sin pago, para ayudar", "Se distingue de un trabajo pagado."),
        ("Un curso pinta el mural del patio de su colegio. ¿El ámbito es escuela, comunidad o sociedad?", "Escuela", "El aporte queda dentro del colegio."),
        ("Un curso junta abrigos para un hogar de ancianos del barrio. ¿El ámbito es escuela, comunidad o sociedad?", "Comunidad", "El aporte llega a personas del barrio."),
        ("¿Qué diferencia hay entre el plan y el presupuesto de un proyecto?", "El plan ordena actividades, responsables y fechas; el presupuesto calcula el dinero", "Uno organiza el trabajo y el otro el dinero."),
        ("¿Por qué un proyecto debe decir dónde y cuándo se hará?", "Para poder organizar las acciones y que todos sepan el lugar y el plazo", "Sin lugar y plazo no se puede coordinar."),
        ("¿Qué es la ayuda social?", "El apoyo a personas que lo necesitan, como abrigo, alimentos o compañía", "Responde a una necesidad concreta."),
        ("En «Taller de lectura para niños de un jardín infantil, los martes de octubre, en la sede vecinal», ¿cuál es el lugar del proyecto?", "La sede vecinal", "Es donde se hará la actividad."),
        ("=", "Un proyecto empieza el día 3 y termina el día 24 del mismo mes. ¿Cuántos días hay entre el día 3 y el día 24?", "24-3", "Se resta la fecha de inicio a la de término."),
        ("Un curso reúne útiles escolares para niños de varias regiones del país afectadas por inundaciones. ¿El ámbito es escuela, comunidad o sociedad?", "Sociedad", "El aporte llega a personas de lugares lejanos."),
        ("Ana propone ayudar a todo el mundo en una semana con $5.000. ¿Qué defecto principal tiene su proyecto?", "No es realista para el tiempo y el dinero", "El alcance es mayor que los recursos."),
        ("Un proyecto dice: «El curso limpiará la plaza del barrio San Pedro». Ya indica quiénes y dónde. ¿Qué dato de ubicación le falta?", "Cuándo, o sea la fecha o el plazo", "Faltan fecha o plazo."),
        ("Ordena las etapas: A) hacer el plan, B) detectar la necesidad, C) calcular el presupuesto, D) realizar las actividades.", "B, A, C, D", "Primero la necesidad, luego plan, presupuesto y acción."),
        ("=", "Un curso quiere dar 2 paquetes de útiles a cada uno de los 45 niños de un jardín. Cada una de las 30 familias del curso aporta 1 paquete. ¿Cuántos paquetes faltan?", "2*45-30", "Se necesitan 90 paquetes y hay 30."),
    ],
    ctx=("En tu colegio hay 12 sillas rotas en la biblioteca. Un grupo propone arreglarlas con ayuda de 4 voluntarios durante 2 semanas. Para ubicar el proyecto, ¿cuál es la necesidad?", "Las 12 sillas rotas de la biblioteca", "Es el problema que el proyecto quiere resolver."),
    sc=[("En Historia: ¿qué es un proyecto de aporte realista?", "El que se puede lograr con el tiempo, las personas y el dinero disponibles", "Es la idea central de la clase."),
        ("¿Cuáles son los tres ámbitos de un aporte?", "Escuela, comunidad y sociedad", "Dicen hasta dónde llega la ayuda."),
        ("¿Qué cuatro preguntas ubican un proyecto?", "Qué necesidad, dónde, cuándo y para quiénes", "Permiten delimitar el proyecto.")],
    op=("Lee estas tres necesidades. A) Juntar 5.000 libros para la biblioteca del curso en 2 semanas con 3 voluntarios. B) Construir una plaza completa en un mes con $20.000. C) Pintar 3 bancas del patio en 10 días con 6 voluntarios. Escoge la más realista y escribe: necesidad, ámbito, lugar, plazo y quiénes participan. Explica con una frase por qué es realista y descarta una de las otras con su motivo.",
        "Elijo C. Necesidad: bancas sin pintura. Ámbito: escuela. Lugar: patio del colegio. Plazo: 10 días. Participan 6 voluntarios. Es realista porque 3 bancas se pintan con 6 personas en 10 días. Descarto B porque una plaza completa no se hace con $20.000.",
        ["identifica necesidad, ámbito, lugar, plazo y participantes", "elige una opción realista", "justifica con tiempo, personas o dinero"], ["ficha de ubicación y una justificación de realismo"], ["elegir el proyecto más grande", "olvidar el plazo"], "Muestra tu ficha a una persona de tu casa y pídele que encuentre el plazo."),
    reinforce="Mira tu barrio y escribe una necesidad pequeña que un grupo de voluntarios podría atender en dos semanas.",
    extend="Escribe un proyecto que sea de ámbito comunidad y otro de ámbito sociedad, con un lugar para cada uno.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
build(
    OA, 2, "",
    use="Aprenderé a revisar de dónde viene la información que uso para planificar: precios, encuestas e informes. Sirve para armar un presupuesto con datos confiables.",
    prior=["Sé ubicar un proyecto: necesidad, lugar, plazo y quiénes.", "Sé que una fuente tiene procedencia: quién la hizo, cuándo y para qué.", "Sé multiplicar y restar con números de varias cifras."],
    explain=[
        "Para hacer un plan y un presupuesto necesito datos. Los consigo de fuentes. Una cotización es un papel o mensaje donde un negocio dice cuánto cuesta algo. Una encuesta es hacer las mismas preguntas a un grupo de personas para saber qué piensan o necesitan. Un informe es un documento de una institución que presenta datos, como el número de niños de una escuela.",
        "No toda fuente sirve. Reviso su procedencia: ¿quién la hizo?, ¿cuándo? y ¿para qué? Un precio sin fecha puede estar vencido, porque los precios cambian. Un mensaje sin nombre no se puede comprobar. Una encuesta que pregunta solo a los amigos no representa a todo el grupo. Una información de otro lugar o de hace muchos años puede no servir hoy.",
        "Para decidir bien pido al menos dos cotizaciones con nombre del negocio y fecha. Las comparo y uso la más confiable. Anoto en el presupuesto de dónde sacó cada dato, para que otra persona pueda revisarlo. Si los datos se contradicen, vuelvo a preguntar antes de decidir.",
    ],
    vocab=[("cotización", "documento o mensaje donde un negocio informa cuánto cuesta algo"), ("encuesta", "las mismas preguntas hechas a un grupo para conocer su opinión o necesidad"), ("informe", "documento de una institución que presenta datos"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("vigente", "que todavía vale, que no está vencido")],
    worked=[
        ("Elegir la fuente de precio", "Cotización A: Librería A, 5 de octubre, 12 cuadernos a $1.200 cada uno. Cotización B: mensaje sin nombre ni fecha, 12 cuadernos por $10.800. ¿Cuál usas para el presupuesto?",
         ["Reviso quién y cuándo en cada una.", "La A tiene nombre y fecha.", "La B no se puede comprobar."], "La cotización A, porque tiene nombre y fecha"),
        ("Leer una encuesta", "Se preguntó a 30 estudiantes qué juntar: 15 dijeron abrigos, 10 libros y 5 alimentos. ¿Cuál es la opción más votada?",
         ["Comparo los votos.", "15 es mayor que 10 y que 5."], "Abrigos"),
    ],
    mistakes=[
        ("Usar un precio sin fecha ni nombre del negocio.", "No se puede saber si está vencido ni comprobar quién lo dio.", "Pide una cotización con nombre y fecha."),
        ("Encuestar solo a las personas más cercanas.", "El resultado no representa a todo el grupo.", "Pregunta a todo el grupo o a una muestra variada."),
    ],
    T=[
        ("¿Qué es una cotización?", "Un documento o mensaje donde un negocio dice cuánto cuesta algo", "Es la fuente de un precio."),
        ("¿Qué es una encuesta?", "Hacer las mismas preguntas a un grupo para conocer lo que piensa o necesita", "Recoge información de varias personas."),
        ("¿Cuáles son las tres preguntas de procedencia de una fuente?", "Quién la hizo, cuándo y para qué", "Permiten juzgar si la fuente sirve."),
        ("¿Por qué un precio sin fecha puede ser una mala fuente?", "Porque los precios cambian y puede estar vencido", "No se sabe si sigue vigente."),
        ("¿Por qué conviene pedir al menos dos cotizaciones?", "Para compararlas y elegir la más confiable o conveniente", "Una sola no permite comparar."),
        ("¿Por qué una encuesta hecha solo a los amigos no representa al grupo?", "Porque deja fuera a otras personas que piensan distinto", "La muestra es parcial."),
        ("=", "La Librería A cotiza, con fecha del 5 de octubre, 15 cuadernos a $1.300 cada uno. ¿Cuánto cuesta el total?", "15*1300", "Se multiplica el precio por la cantidad.", ""),
        ("Elige la mejor fuente para un precio: A) mensaje sin nombre, B) cotización con nombre del negocio y fecha.", "B", "Tiene procedencia clara."),
        ("=", "En una encuesta a 40 estudiantes, 22 prefirieron juntar alimentos. ¿Cuántos estudiantes prefirieron otra cosa?", "40-22", "Se resta de los 40 los que votaron alimentos."),
        ("Cotización C (Papelería C, 2 de octubre): 10 pliegos a $900 cada uno. Cotización D (sin nombre ni fecha): 10 pliegos a $700 cada uno. Para el presupuesto, ¿cuál usas y por qué?", "La C, porque tiene nombre y fecha", "Se puede comprobar; la D no."),
        ("Una compañera dice: «A todos les gusta juntar juguetes, lo leí en un afiche de hace 12 años en otra comuna». ¿Qué problema de procedencia tiene?", "Es muy antigua y de otro lugar", "No habla de este grupo hoy."),
        ("Ordena los pasos para un precio confiable: A) pedir dos cotizaciones, B) anotar nombre del negocio y fecha de cada una, C) compararlas, D) poner el precio elegido en el presupuesto.", "A, B, C, D", "Primero se obtienen, luego se registran, se comparan y se usan."),
        ("=", "Dos cotizaciones con fecha, del mismo cuaderno y por 18 unidades: la del negocio A suma $21.600 y la del negocio B suma $19.800. ¿Cuánto se ahorra eligiendo B?", "21600-19800", "Se resta el precio menor al mayor."),
    ],
    ctx=("Tu curso necesita comprar 8 cartulinas para un afiche solidario. Tienes un mensaje sin firma que dice «cuestan $500» y una lista de precios fechada de una papelería del barrio que dice $650 cada una. ¿Qué precio usas?", "$650, de la lista fechada", "Tiene procedencia clara."),
    sc=[("En Historia: ¿qué es una cotización?", "Un documento donde un negocio informa cuánto cuesta algo", "Es una fuente de precios."),
        ("¿Qué preguntas se hacen para revisar la procedencia?", "Quién, cuándo y para qué", "Permiten juzgar la fuente."),
        ("¿Por qué anotar en el presupuesto de dónde viene cada dato?", "Para que otros puedan comprobarlo", "La transparencia permite revisar.")],
    op=("Lee estas dos cotizaciones. Cotización 1: Papelería Norte, 8 de octubre, 10 resmas de hojas a $4.200 cada una. Cotización 2: mensaje sin nombre ni fecha, 10 resmas a $3.500 cada una. Calcula el total de cada una, decide cuál usarías para un presupuesto y explica tu decisión con las preguntas de procedencia.",
        "Total 1: 10 x 4.200 = 42.000. Total 2: 10 x 3.500 = 35.000. Uso la 1 porque dice quién (Papelería Norte) y cuándo (8 de octubre). La 2 es más barata, pero no se puede comprobar.",
        ["calcula los dos totales", "decide cuál usar", "explica con quién y cuándo"], ["dos cálculos y una justificación"], ["elegir solo por precio", "no usar la fecha"], "Pide a una persona de tu casa que revise tus cálculos de multiplicación."),
    reinforce="En tu casa, mira la etiqueta de un producto con precio y anota si trae nombre del negocio y fecha.",
    extend="Escribe tres preguntas para una encuesta breve sobre qué aporte necesita tu curso.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
PLAN = "Plan «Abrigo para el hogar»: objetivo, juntar 20 mantas. Actividad 1, pedir mantas en el barrio (responsable Ema, semana 1). Actividad 2, lavar y doblar (responsable Tomás, semana 2). Actividad 3, entregar las mantas (responsable la profesora y 5 voluntarios, semana 3)."
build(
    OA, 3, "",
    use="Aprenderé a armar un plan con responsables y fechas, y un presupuesto con ingresos y gastos. Sirve para que un proyecto de ayuda se pueda realizar de verdad.",
    prior=["Sé ubicar un proyecto y revisar la procedencia de los precios.", "Sé sumar, restar y multiplicar con números hasta decenas de miles.", "Sé identificar causas y consecuencias de un problema."],
    explain=[
        "Un plan ordena el trabajo. Tiene un objetivo, que es lo que se quiere lograr, y una lista de actividades. Cada actividad lleva un responsable, que es la persona que se encarga de ella, y una fecha. Algunas actividades dependen de otras: no puedo entregar mantas antes de juntarlas. Por eso las ordeno en el tiempo.",
        "Un presupuesto calcula el dinero del proyecto. Tiene dos partes. Los ingresos son el dinero que entra, por ejemplo aportes de las familias o la venta de galletas caseras. Los gastos son el dinero que sale, por ejemplo comprar bolsas o detergente. El saldo es la diferencia: ingresos menos gastos. Si el saldo es cero o positivo, alcanza. Si es negativo, falta dinero.",
        "También pienso en actores, causas y consecuencias. Los actores son quienes participan: el curso, las familias, el hogar que recibe la ayuda. La causa de este proyecto es que hay pocas mantas en invierno. La consecuencia esperada es que las personas duerman abrigadas. Si nadie actúa, la causa sigue y el problema continúa.",
    ],
    vocab=[("objetivo", "lo que se quiere lograr con el proyecto"), ("responsable", "persona que se encarga de una actividad"), ("ingreso", "dinero que entra al proyecto"), ("gasto", "dinero que sale del proyecto"), ("saldo", "ingresos menos gastos")],
    worked=[
        ("Leer un plan", PLAN + " ¿Quién es el responsable de lavar y doblar, y en qué semana?",
         ["Busco la actividad lavar y doblar.", "Tomás es el responsable.", "Se hace en la semana 2."], "Tomás, en la semana 2"),
        ("Calcular un saldo", "Ingresos: $9.000 de aportes de familias. Gastos: $4.000 en detergente y $2.500 en bolsas. ¿Cuál es el saldo?",
         ["Sumo los gastos: 4.000 + 2.500 = 6.500.", "Resto de los ingresos: 9.000 - 6.500."], "$2.500 de saldo"),
    ],
    mistakes=[
        ("Escribir actividades sin responsable ni fecha.", "Nadie sabe quién las hace ni cuándo.", "Asigna un responsable y una fecha a cada actividad."),
        ("Mezclar ingresos y gastos en una misma suma.", "El saldo se calcula restando los gastos de los ingresos.", "Suma por separado ingresos y gastos, y luego resta."),
    ],
    T=[
        ("En un plan, ¿qué es un responsable?", "La persona que se encarga de una actividad", "Cada actividad necesita alguien a cargo."),
        ("Un presupuesto tiene dos partes. ¿Cuáles son?", "Ingresos y gastos", "Uno es lo que entra y el otro lo que sale."),
        ("Un curso cobra $500 de entrada a una función para juntar fondos. ¿Esos $500 son un ingreso o un gasto?", "Un ingreso", "Es dinero que entra."),
        ("¿Por qué cada actividad del plan debe tener un responsable?", "Para que alguien se encargue y no quede sin hacerse", "Evita que la tarea se pierda."),
        ("¿Qué es el saldo de un presupuesto?", "La diferencia entre ingresos y gastos", "Se calcula restando."),
        ("¿Por qué un proyecto de ayuda debe pensar en las consecuencias?", "Para saber qué mejora se espera y qué riesgos hay", "Permite evaluar si vale la pena."),
        (PLAN + " ¿Qué actividad se hace en la semana 3?", "Entregar las mantas", "Aparece con la semana 3 en el plan."),
        ("=", "Ingresos: $10.000 de aportes de las familias y $5.500 por vender galletas caseras. Gastos: $4.800 en lana y $3.200 en bolsas. ¿Cuál es el saldo en pesos?", "10000+5500-4800-3200", "Se suman ingresos y se restan los gastos."),
        ("«El invierno es frío y el hogar tiene pocas mantas.» ¿Esa frase es una causa o una consecuencia del proyecto?", "Una causa", "Es el problema que origina la acción."),
        ("Si la actividad «pedir mantas en el barrio» no se hace en la semana 1, ¿qué actividad no puede hacerse en la semana 2?", "Lavar y doblar las mantas", "No se pueden lavar mantas que no se han juntado."),
        (PLAN + " Si nadie consigue un vehículo para llevar las mantas al hogar, ¿qué actividad del plan no se puede realizar?", "Entregar las mantas", "La entrega depende de poder trasladarlas; hay que resolverlo antes de la semana 3."),
        ("=", "Ingresos: $12.000. Gastos: $5.500 en lana, $4.200 en tela y $3.800 en bolsas. ¿Cuánto dinero falta?", "5500+4200+3800-12000", "Los gastos superan los ingresos."),
        ("Ordena de causa a consecuencia: A) los residentes duermen abrigados, B) se juntan y entregan 20 mantas, C) el hogar tiene pocas mantas en invierno.", "C, B, A", "Problema, acción y resultado."),
    ],
    ctx=("Tu curso organiza una once solidaria. Hay tres tareas: pedir permiso en el colegio, preparar el pan y avisar a las familias. Tres estudiantes, Luz, Iván y Bruno, se reparten una tarea cada uno. ¿Qué dos datos faltan en el plan para que esté completo?", "Las fechas y el objetivo", "Un plan completo tiene objetivo, actividades, responsables y fechas."),
    sc=[("En Historia: ¿qué es un presupuesto?", "El cálculo de ingresos y gastos de un proyecto", "Ordena el dinero del proyecto."),
        ("¿Cómo se calcula el saldo?", "Ingresos menos gastos", "Dice si alcanza el dinero."),
        ("¿Qué debe llevar cada actividad de un plan?", "Un responsable y una fecha", "Así se puede coordinar.")],
    op=("Un curso de 6.º organiza una colecta de alimentos para una sede vecinal. Escribe un plan con objetivo y tres actividades, cada una con un responsable (usa los nombres Ema, Tomás y Luz) y una semana. Luego completa un presupuesto con estos datos: ingresos, $8.000 de aportes y $4.000 por venta de galletas; gastos, $3.500 en cajas y $2.000 en afiches. Calcula el saldo.",
        "Objetivo: juntar 100 alimentos. Actividad 1: avisar en el barrio (Ema, semana 1). Actividad 2: recibir y ordenar (Tomás, semana 2). Actividad 3: entregar (Luz, semana 3). Ingresos 12.000; gastos 5.500; saldo 6.500.",
        ["objetivo claro", "tres actividades con responsable y semana", "ingresos, gastos y saldo calculados"], ["un plan y un presupuesto con saldo"], ["olvidar una fecha", "sumar los gastos con los ingresos"], "Pide a una persona de tu casa que lea tu plan y encuentre los responsables."),
    reinforce="Haz una lista de tres actividades para una tarea de tu casa y asigna un responsable a cada una.",
    extend="Explica con tus palabras por qué un proyecto con saldo negativo necesita cambios.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
build(
    OA, 4, "",
    use="Aprenderé a comparar perspectivas y territorios al planificar un proyecto, y a ajustar el presupuesto cuando no alcanza. Sirve para adaptar la ayuda a quienes la necesitan.",
    prior=["Sé hacer un plan con responsables y fechas.", "Sé calcular ingresos, gastos y saldo.", "Sé que cada persona mira un tema desde su perspectiva."],
    explain=[
        "Un mismo proyecto puede verse distinto según quién lo mira. Una perspectiva es la manera de ver un tema según lo que se necesita o se teme. Un adulto mayor puede pedir talleres en la mañana y un estudiante puede preferir la tarde. Para planificar bien escucho a las personas que recibirán la ayuda y busco soluciones que consideren a varias perspectivas.",
        "Los territorios también cambian las necesidades. En un pueblo del desierto del norte llueve muy poco y el agua es escasa. En una zona lluviosa del sur hay mucha lluvia y las casas pueden necesitar techos y canaletas en buen estado. Un proyecto que sirvió en un lugar puede no servir en otro. Antes de copiarlo reviso qué necesita ese territorio.",
        "A veces el presupuesto no alcanza. Entonces no abandono el proyecto: lo ajusto. Ajustar es cambiar gastos o ingresos para que el saldo no sea negativo. Primero fijo las prioridades, que son lo más importante para cumplir el objetivo. Quito o reduzco lo que no es esencial y busco nuevos ingresos si es necesario.",
    ],
    vocab=[("perspectiva", "manera de ver un tema según lo que se necesita o se teme"), ("territorio", "espacio con rasgos propios, como clima y recursos"), ("prioridad", "lo más importante para cumplir el objetivo"), ("ajustar", "cambiar gastos o ingresos para que el dinero alcance"), ("esencial", "que no puede faltar para cumplir el objetivo")],
    worked=[
        ("Ajustar un presupuesto", "Ingresos: $15.000. Gastos: $8.500 en pan, $6.000 en jugos y $4.500 en globos de decoración. El objetivo es dar una once a adultos mayores. ¿Qué gasto conviene quitar primero?",
         ["Veo qué es esencial: pan y jugos.", "Los globos no son esenciales.", "Quitarlos baja los gastos."], "Los globos de decoración"),
        ("Considerar dos perspectivas", "Adultos mayores piden taller en la mañana. Estudiantes solo pueden en la tarde. ¿Qué solución considera a ambos?",
         ["Busco una solución intermedia.", "Hacer el taller algunos días en la mañana y otros en la tarde."], "Taller dos días en la mañana y dos en la tarde"),
    ],
    mistakes=[
        ("Copiar un proyecto de otro lugar sin revisar las necesidades locales.", "Los territorios tienen climas, recursos y personas distintas.", "Pregunta qué necesita la comunidad donde actuarás."),
        ("Abandonar el proyecto cuando el dinero no alcanza.", "Se puede ajustar quitando gastos no esenciales o buscando ingresos.", "Fija prioridades y ajusta el presupuesto."),
    ],
    T=[
        ("En un proyecto, ¿qué es una perspectiva?", "La manera de ver el tema según lo que se necesita o se teme", "Cambia de persona en persona."),
        ("¿Qué significa ajustar un presupuesto?", "Cambiar gastos o ingresos para que el dinero alcance", "El saldo debe quedar sin números negativos."),
        ("¿Qué es una prioridad en un proyecto?", "Lo más importante para cumplir el objetivo", "Se financia primero."),
        ("¿Por qué un pueblo del desierto del norte y una zona lluviosa del sur pueden necesitar proyectos distintos?", "Porque su clima y sus recursos son distintos", "El territorio cambia las necesidades."),
        ("¿Por qué conviene escuchar a quienes recibirán la ayuda?", "Para saber qué necesitan en realidad", "Evita ayudar en algo que no era necesario."),
        ("Si el presupuesto no alcanza, ¿qué se puede hacer en vez de abandonar el proyecto?", "Ajustarlo quitando gastos no esenciales o buscando ingresos", "Hay soluciones antes de renunciar."),
        ("=", "Ingresos: $18.000. Gastos: $9.000 en pan, $7.000 en jugos y $5.000 en afiches. ¿Cuánto dinero falta?", "9000+7000+5000-18000", "Los gastos suman $21.000."),
        ("Faltan $4.000 en un presupuesto. ¿Qué ajuste lo resuelve: A) quitar un gasto no esencial de $4.800, B) subir un gasto en $2.000?", "A", "Quitar $4.800 cubre los $4.000 faltantes."),
        ("Una campaña para ahorrar agua, ¿responde mejor a un pueblo del desierto del norte o a una zona lluviosa del sur?", "A un pueblo del desierto del norte", "Allí el agua es escasa."),
        ("Adultos mayores piden talleres en la mañana y estudiantes solo pueden en la tarde. ¿Qué solución considera ambas perspectivas: A) solo mañana, B) dos días en la mañana y dos en la tarde?", "B", "Atiende a ambos grupos."),
        ("Valentina dice: «Como el proyecto funcionó en mi barrio, funcionará igual en cualquier lugar». ¿Qué debe revisar?", "Si el otro lugar tiene las mismas necesidades y recursos", "Los territorios son distintos."),
        ("=", "En la comunidad A, el proyecto cuesta $1.500 por persona y en la comunidad B, $2.000 por persona. Ambas atienden a 20 personas. ¿Cuántos pesos más cuesta en total en la B?", "(2000-1500)*20", "Se calcula la diferencia por persona y se multiplica por 20."),
        ("Un proyecto de once tiene tres gastos: pan, globos y afiches. El objetivo es dar once a 20 adultos mayores. ¿Cuál gasto es esencial?", "El pan", "Sin pan no se puede dar la once."),
    ],
    ctx=("Dos juntas de vecinos quieren el mismo proyecto de biblioteca móvil. Una está en una ciudad con calles cercanas y otra en un pueblo rural con casas muy distantes. ¿Qué debe comparar el equipo antes de repetir el proyecto?", "Las distancias y los recursos de cada territorio", "El territorio cambia el costo y la forma de hacerlo."),
    sc=[("En Historia: ¿qué es ajustar un presupuesto?", "Cambiar gastos o ingresos para que el dinero alcance", "Evita un saldo negativo."),
        ("¿Qué es una prioridad?", "Lo más importante para cumplir el objetivo", "Se financia primero."),
        ("¿Por qué un proyecto no se copia sin revisar el lugar?", "Porque cada territorio tiene necesidades distintas", "El contexto cambia la solución.")],
    op=("Un curso tiene $20.000 para una once solidaria. Gastos pensados: pan $9.000, jugos $7.000, globos $3.000 y afiches $4.000. Calcula el total y cuánto falta. Luego propón un ajuste que cumpla el objetivo (dar once a 25 personas) y explica en una frase qué perspectiva de quienes reciben la ayuda cuidaste.",
        "Total: 23.000; faltan 3.000. Quito los globos ($3.000). Así el total es 20.000 y alcanza. Cuidé la perspectiva de quienes reciben: lo esencial es el pan y los jugos, no la decoración.",
        ["calcula total y faltante", "ajusta quitando algo no esencial", "explica qué perspectiva cuidó"], ["un cálculo, un ajuste y una justificación"], ["quitar el pan", "no revisar el nuevo total"], "Pide a una persona de tu casa que compruebe que tu nuevo total no pasa de $20.000."),
    reinforce="Anota tres gastos de una fiesta y decide cuál es el menos esencial.",
    extend="Compara un proyecto para una zona lluviosa y uno para una zona seca y explica una diferencia.",
    materials=MAT,
)

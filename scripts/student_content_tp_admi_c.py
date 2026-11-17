"""Administración 3.º medio TP: OAE-05 (organizar y ordenar el lugar de trabajo) y OAE-06 (equipos y herramientas tecnológicas con uso eficiente). Empresas, personas y cifras inventadas; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, listas, registros de consumo y casos están escritos en cada ejercicio: las oficinas y las personas son inventadas y las cifras son «de ejemplo», "
             "así que no necesitas equipos, programas ni internet. No uses documentos ni datos reales de tu liceo, de tu familia o de una empresa de práctica. "
             "Este cuaderno enseña criterios y cálculos básicos en papel; las normas de prevención de riesgos, de conservación de documentos y de seguridad eléctrica se consultan en la norma vigente y con tu docente de la especialidad. "
             "Nunca abras ni repares equipos eléctricos: ante una falla, avisa al soporte técnico. Cuida tu postura y haz pausas cortas cada 45 minutos.")

build = make_build(MATERIALS)

O5 = "TP-ADMI-3-OAE-05"
O6 = "TP-ADMI-3-OAE-06"

# ============================================================ OAE-05, clase 1
F = ("Ficha 19 (puesto de trabajo de ejemplo, inventado) de la oficina «Contadores Los Álamos». Sobre el escritorio hay 14 carpetas sin rótulo y una pila de papeles. Hay una caja de resmas de papel en el pasillo. "
     "Un alargador con cables cruza el suelo hacia una impresora. Unos sobres con sueldos de ejemplo quedaron a la vista sobre una silla. El primer cajón del archivador está trabado por exceso de papeles. "
     "Tiempo de búsqueda de ejemplo de un documento: 6 minutos.")
build(
    O5, 1, F,
    use="Aprenderé por qué el orden del lugar de trabajo importa para encontrar la información, cuidar la seguridad y proteger los datos reservados, y conoceré el método de las 5S.",
    prior=["Sé qué es un documento de respaldo.", "Sé que hay datos reservados.", "Sé calcular minutos."],
    explain=[
        "Organizar el lugar de trabajo es disponer los documentos, objetos y equipos de modo que se puedan recuperar rápido y sin riesgo. Un lugar ordenado ahorra tiempo de búsqueda, evita pérdidas de documentos y previene accidentes, como tropezar con cables o con una caja en el pasillo. También protege la información reservada, que no debe quedar a la vista de cualquiera.",
        "El método de las 5S es una guía conocida para ordenar: clasificar (separar lo necesario de lo que sobra), ordenar (un lugar para cada cosa y cada cosa en su lugar), limpiar (mantener el puesto aseado), estandarizar (usar las mismas reglas todos los días) y mantener la disciplina (cumplirlas siempre). Es un método de orden y no una norma legal.",
        "Las normas de prevención de riesgos y de conservación de documentos se consultan en la norma vigente y las políticas de la empresa. En el lugar de trabajo se despejan los pasillos y las salidas, se guardan los cables fuera del paso y se reportan los riesgos a la jefatura. Quien ordena no elimina documentos por su cuenta: consulta primero qué se conserva y por cuánto tiempo.",
    ],
    vocab=[("recuperar", "encontrar y sacar un documento u objeto cuando se necesita"), ("5S", "método de orden: clasificar, ordenar, limpiar, estandarizar y mantener disciplina"), ("rótulo", "etiqueta que dice qué contiene una carpeta"), ("riesgo", "posibilidad de que ocurra un daño"), ("reservado", "que no debe verse ni difundirse sin autorización"), ("pasillo despejado", "paso libre de objetos")],
    worked=[
        ("Aplicar «clasificar»", "En un escritorio de ejemplo hay una factura vigente, una revista antigua y un folleto de otra empresa. Con la regla «clasificar», ¿qué se hace?", ["Se separa lo necesario de lo que sobra.", "La factura vigente se conserva; revista y folleto se retiran si nadie los necesita."], "Se conserva la factura y se retira lo que sobra"),
        ("Detectar un riesgo", "En una oficina ficticia hay una caja a mitad de un pasillo por el que pasa gente. ¿Qué riesgo hay y qué se hace?", ["Alguien puede tropezar con la caja.", "Se mueve la caja a un lugar de almacenamiento y se despeja el pasillo."], "Riesgo de tropiezo; despejar el pasillo"),
    ],
    mistakes=[("Botar documentos antiguos para «ordenar» sin consultar.", "Algunos deben conservarse por obligación o por su valor de respaldo.", "Consulta a la jefatura y a la norma vigente qué se conserva y por cuánto tiempo."),
              ("Dejar los cables cruzando el paso porque «es solo un rato».", "Aumenta el riesgo de tropiezos y de dañar el equipo.", "Guarda los cables fuera de la zona de paso.")],
    T=[
        ("abc", "En Administración: ¿para qué se organiza el lugar de trabajo?", "Para encontrar rápido la información y trabajar sin riesgos", "Para que el escritorio se vea vacío al terminar", "Para evitar que otras personas trabajen cerca", "El orden sirve para recuperar con rapidez y prevenir accidentes."),
        ("abc", "{F} ¿Qué riesgo representa la caja de resmas en el pasillo?", "Tropiezo o bloqueo del paso", "Pérdida de documentos digitales", "Exceso de luz", "Un objeto en el pasillo puede causar tropiezos y bloquear una salida."),
        ("abc", "{F} ¿Qué dato está en riesgo por los sobres a la vista sobre la silla?", "La confidencialidad de la información de sueldos", "La temperatura de la oficina", "La velocidad de la impresora", "Los sobres con sueldos son información reservada que no debe verse."),
        ("abc", "En el método de las 5S, ¿qué significa «clasificar»?", "Separar lo necesario de lo que sobra", "Pintar las paredes", "Archivar todo sin revisar", "Clasificar es la primera S: decidir qué se necesita y qué no."),
        ("abc", "En el método de las 5S, ¿qué significa «estandarizar»?", "Usar las mismas reglas de orden todos los días", "Comprar muebles iguales", "Eliminar las reglas", "Estandarizar fija reglas comunes para que el orden se mantenga."),
        ("abc", "{F} ¿Qué problema muestran las 14 carpetas sin rótulo?", "No se sabe qué contiene cada una y se pierde tiempo buscando", "Hay demasiados rótulos", "Las carpetas son de otro color", "Sin rótulo hay que abrir cada carpeta para saber su contenido."),
        ("=", "{F} Si se hacen 10 búsquedas al día y cada una toma 6 minutos, ¿cuántos minutos se gastan buscando al día?", "10*6", "Minutos al día = búsquedas × minutos por búsqueda.", " minutos"),
                ("=", "{F} Con 15 búsquedas al día de 6 minutos cada una, ¿cuántos minutos se gastan buscando en una semana de 5 días?", "15*6*5", "Minutos semanales = búsquedas × minutos × días.", " minutos"),
        ("abc", "{F} Una persona propone botar todos los papeles de la pila del escritorio para ordenar rápido. ¿Qué corresponde?", "Revisar cuáles se conservan y consultar a la jefatura antes de eliminar", "Botarlos, porque la pila molesta", "Llevarlos a casa", "Eliminar documentos sin revisión puede perder respaldos obligatorios."),
        ("abc", "{F} ¿Qué medida de prevención se adopta con el alargador de cables?", "Guardar los cables fuera de la zona de paso", "Cruzarlos más cerca de la puerta", "Taparlos con papeles", "Los cables fuera del paso evitan tropiezos y daños."),
        ("abc", "El primer cajón del archivador se traba por exceso de papeles. ¿Qué es lo más adecuado?", "Retirar lo que ya no se necesita siguiendo la regla de conservación y reorganizar el cajón", "Empujar más papeles para ordenarlos", "Dejarlo trabado y usar el segundo cajón", "El exceso se corrige clasificando y reorganizando con las reglas de conservación."),
        ("abc", "Un compañero dice que ordenar es una pérdida de tiempo porque «yo sé dónde está todo». ¿Qué respuesta es más adecuada?", "El orden también sirve a otras personas que necesitan encontrar lo mismo", "Tiene razón, el orden solo es para quien lo hace", "El orden es solo una decoración", "Un puesto ordenado permite que otros encuentren la información cuando falta quien lo usa."),
        ("abc", "{F} ¿Cuál es el primer paso razonable para ordenar el puesto de la ficha?", "Clasificar: separar lo necesario de lo que sobra y de lo reservado", "Comprar muebles nuevos", "Mover el escritorio", "El método parte por clasificar antes de ordenar y limpiar."),
    ],
    ctx=("abc", "Al término de su turno, una asistente deja el escritorio con los documentos de clientes en una caja bajo llave y los cables recogidos. ¿Qué cumple?", "Orden, seguridad y reserva de la información", "Una orden para botar papeles", "Un cambio de domicilio de la oficina", "Guardar documentos reservados y despejar el puesto cumple orden y seguridad."),
    sc=[
        ("En Administración: ¿qué son las 5S?", "Un método de orden: clasificar, ordenar, limpiar, estandarizar y mantener disciplina", "Es una guía práctica para mantener el orden."),
        ("¿Qué haces antes de eliminar un documento?", "Consulto qué se conserva y por cuánto tiempo", "Hay obligaciones de conservación que se consultan."),
        ("¿Dónde quedan los documentos reservados al terminar el día?", "Guardados en un lugar cerrado", "Así no quedan a la vista de cualquier persona."),
    ],
    op=("Con la Ficha 19, escribe una lista de seis acciones de orden para el puesto, cada una con la «S» del método que aplica, y una frase sobre qué documento consultarías con la jefatura antes de eliminarlo.\n{F}",
        "1) Retirar lo que sobra de la pila (clasificar). 2) Rotular las 14 carpetas y guardarlas por tema (ordenar). 3) Sacar la caja del pasillo y recoger los cables (ordenar y seguridad). 4) Guardar los sobres de sueldos bajo llave (reserva). 5) Limpiar el escritorio al terminar el día (limpiar). 6) Acordar reglas comunes con el equipo (estandarizar). Consultaría antes de eliminar los documentos antiguos del cajón trabado.",
        ["usa las cinco S de forma correcta", "incluye seguridad y reserva", "menciona consultar antes de eliminar"],
        ["lista de seis acciones con su S y una frase"],
        ["botar documentos sin consultar", "olvidar la reserva de los sobres", "dejar los cables en el paso"],
        "Revisa que cada acción tenga su S. Si falta la reserva de los sobres, pregunta quién podría verlos."),
    reinforce="Ordena en papel el contenido de un estuche ficticio con cinco objetos usando las tres primeras S.",
    extend="Explica con un ejemplo inventado cómo el desorden de una persona puede afectar el trabajo de otra.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 20 (sistemas y reglas de ejemplo, inventados) de «Contadores Los Álamos». Sistemas de archivo: alfabético (por apellido), numérico (por número de documento), cronológico (por fecha) y por materia (por tema). "
     "Reglas: rotular cada carpeta con nombre, tema y año; registrar en una hoja de control cada documento que sale (quién, fecha de salida, fecha de devolución); separar el archivo activo (se usa seguido) del archivo pasivo (se guarda por obligación o consulta ocasional). "
     "Los plazos de conservación se consultan en la norma vigente y en la política de la empresa. Roles: encargada de archivo, usuarios y jefatura.")
build(
    O5, 2, F,
    use="Aprenderé los sistemas de archivo, el rotulado, la hoja de control de salida y los roles que permiten disponer y recuperar la información a tiempo.",
    prior=["Sé qué es organizar el puesto de trabajo.", "Conozco las 5S.", "Sé ordenar por orden alfabético y por número."],
    explain=[
        "Un sistema de archivo es la regla con que se ordenan los documentos para encontrarlos rápido. El sistema alfabético ordena por apellido o nombre; el numérico, por el número del documento; el cronológico, por fecha; y el de materia, por tema. Se elige según cómo se busca: si se pide por cliente conviene el alfabético; si se pide por número de factura, el numérico.",
        "Cada carpeta debe llevar un rótulo con nombre, tema y año. Si un documento sale del archivo, se anota en una hoja de control quién lo retira, la fecha de salida y la fecha de devolución, para saber dónde está. El archivo activo guarda lo que se usa seguido y está más a mano; el archivo pasivo guarda lo que solo se conserva por obligación o para consultas ocasionales. Los plazos de conservación no se fijan por opinión: se consultan en la norma vigente.",
        "Los roles ordenan la responsabilidad. La encargada de archivo mantiene el sistema y la hoja de control; los usuarios retiran y devuelven documentos y los mantienen completos; la jefatura autoriza el acceso a documentos reservados. Cada persona devuelve el documento a su lugar y no lo presta a quien no está autorizado.",
    ],
    vocab=[("sistema de archivo", "regla con que se ordenan los documentos"), ("alfabético", "ordenado por apellido o nombre"), ("cronológico", "ordenado por fecha"), ("archivo activo", "documentos de uso frecuente"), ("archivo pasivo", "documentos que se guardan por obligación o consulta ocasional"), ("hoja de control", "registro de salida y devolución de documentos")],
    worked=[
        ("Elegir un sistema", "En una oficina ficticia siempre se pregunta por una carpeta diciendo el apellido del cliente. ¿Qué sistema conviene?", ["Se busca por apellido.", "Eso es el sistema alfabético."], "Alfabético"),
        ("Activo o pasivo", "Una factura del año en curso se consulta casi todos los días. ¿Archivo activo o pasivo?", ["Se usa con frecuencia.", "Eso corresponde al archivo activo."], "Archivo activo"),
    ],
    mistakes=[("Retirar una carpeta sin anotar en la hoja de control.", "Nadie sabrá dónde está si se necesita.", "Anota quién la retira, la fecha de salida y la de devolución."),
              ("Decidir por cuenta propia cuánto tiempo se conserva un documento.", "Los plazos de conservación se fijan por norma.", "Consulta la norma vigente y la política de la empresa.")],
    T=[
        ("abc", "En Administración: ¿qué es un sistema de archivo?", "La regla con que se ordenan los documentos para encontrarlos", "El mueble donde se guardan los documentos", "El color de las carpetas", "Un sistema de archivo es el criterio de orden; el mueble es otra cosa."),
        ("abc", "{F} ¿Qué sistema de la ficha ordena por fecha?", "El cronológico", "El alfabético", "El numérico", "Cronológico significa que los documentos van ordenados por su fecha."),
        ("abc", "{F} ¿Qué datos anota la hoja de control cuando un documento sale?", "Quién lo retira, la fecha de salida y la fecha de devolución", "Solo el color de la carpeta", "El sueldo del encargado", "La hoja de control registra esos tres datos."),
        ("abc", "{F} ¿Qué rol mantiene el sistema de archivo y la hoja de control?", "La encargada de archivo", "Cualquier cliente", "El proveedor de papel", "La ficha asigna a la encargada de archivo el mantenimiento del sistema."),
        ("abc", "Piden con frecuencia la factura 4.512. ¿Qué sistema facilita encontrarla?", "El numérico, por número de documento", "El alfabético por apellido del cliente", "El cronológico por mes", "Para búsquedas por número, el sistema numérico es el más directo."),
        ("abc", "¿Qué es el archivo pasivo?", "Documentos que se guardan por obligación o consulta ocasional", "Documentos que se usan todos los días", "Documentos que se botan", "El archivo pasivo conserva lo que no se usa seguido pero debe guardarse."),
        ("=", "{F} Una carpeta salió el día 12 y debía devolverse el día 19. ¿Cuántos días de préstamo tiene?", "19-12", "Días de préstamo = fecha de devolución − fecha de salida.", " días"),
        ("=", "En un archivo de ejemplo hay 6 cajones y cada uno guarda 9 carpetas. ¿Cuántas carpetas hay en total?", "6*9", "Total = cajones × carpetas por cajón.", " carpetas"),
        ("abc", "{F} Una carpeta no tiene rótulo. ¿Qué datos debería llevar?", "Nombre, tema y año", "Solo la fecha de compra del mueble", "El nombre de la encargada", "Según la regla de la ficha, el rótulo lleva nombre, tema y año."),
        ("abc", "Un usuario pide un documento reservado de sueldos. ¿Qué corresponde?", "Consultar si está autorizado por la jefatura antes de entregarlo", "Entregarlo, porque es usuario del archivo", "Prestarlo sin anotar nada", "El acceso a documentos reservados lo autoriza la jefatura."),
        ("abc", "Un compañero dice que el plazo de conservación de un documento es «de 3 años porque sí». ¿Qué respondes?", "Que se confirma en la norma vigente y la política de la empresa", "Que está bien, porque lo dijo un compañero", "Que se bote el documento antes", "Los plazos de conservación se fijan por norma, no por opinión."),
        ("abc", "{F} Para ordenar las carpetas de clientes que se piden por nombre de empresa, ¿qué sistema conviene?", "El alfabético", "El cronológico", "El de materia", "Si la búsqueda es por nombre, se ordena alfabéticamente."),
        ("abc", "Un documento fue devuelto con dos hojas faltantes. ¿Qué hace la encargada?", "Registra la observación, informa a la jefatura y busca las hojas", "Lo archiva sin decir nada", "Lo bota", "Un documento incompleto se informa y se investiga."),
    ],
    ctx=("abc", "Una oficina decide archivar los contratos por año de firma y, dentro de cada año, por apellido. ¿Qué combina?", "Un sistema cronológico y uno alfabético", "Un sistema numérico y uno de materia", "Ninguno", "Se usa primero la fecha y después el apellido, combinando dos sistemas."),
    sc=[
        ("En Administración: ¿qué diferencia hay entre archivo activo y pasivo?", "El activo se usa seguido; el pasivo se guarda por obligación o consulta ocasional", "La diferencia es la frecuencia de uso."),
        ("¿Para qué sirve la hoja de control?", "Para saber quién tiene un documento y cuándo debe devolverlo", "Evita que los documentos se pierdan."),
        ("¿Quién autoriza el acceso a documentos reservados?", "La jefatura", "Los usuarios no pueden autorizarse solos."),
    ],
    op=("Con la Ficha 20, elige un sistema de archivo para estos tres casos y justifica en una línea cada elección: (1) carpetas de clientes buscadas por nombre; (2) facturas buscadas por su número; (3) informes buscados por mes. Después escribe cómo registrarías la salida de una carpeta.\n{F}",
        "(1) Alfabético: se busca por nombre. (2) Numérico: se busca por número de factura. (3) Cronológico: se busca por fecha. Registro de salida: anotar en la hoja de control quién retira la carpeta, la fecha de salida (día 12) y la de devolución (día 19).",
        ["elige el sistema correcto en cada caso", "justifica con la forma de búsqueda", "describe el registro de salida"],
        ["tres líneas de elección y una de registro"],
        ["confundir cronológico con numérico", "no justificar", "omitir la fecha de devolución"],
        "Compara con la forma de búsqueda de cada caso. Si no justifica, pide que diga cómo se busca."),
    reinforce="Ordena en papel una lista de seis apellidos inventados y de cinco números de factura inventados.",
    extend="Explica con un ejemplo inventado qué problema produce un sistema de archivo mal elegido.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 21 (carpetas de ejemplo, inventadas) de «Contadores Los Álamos», mezcladas sobre un escritorio. Apellidos de clientes ficticios: Pérez, Araya, Soto, Contreras, Bravo, Díaz, Muñoz. "
     "Números de factura de ejemplo: 245, 118, 391, 12, 207. Consultas del último mes de ejemplo: Soto 3 veces; Araya 18 veces; Díaz 1 vez; Pérez 9 veces. "
     "El archivador tiene 4 cajones: A es el más cómodo de alcanzar, y D el más difícil.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de desorden en papel: ordenar con un sistema de archivo y ubicar lo que más se consulta en el lugar más accesible.",
    prior=["Conozco los sistemas de archivo.", "Sé ordenar alfabética y numéricamente.", "Sé qué es archivo activo."],
    explain=[
        "Para ordenar un conjunto de carpetas se elige primero el sistema según cómo se buscan. Si se buscan por apellido, se ordenan alfabéticamente: la letra A va antes que la B y así hasta la Z. Si se buscan por número de factura, se ordenan de menor a mayor. Cuando dos apellidos empiezan con la misma letra, se compara la letra siguiente.",
        "Además del orden, importa la ubicación. Lo que se consulta más se pone en el lugar más fácil de alcanzar y lo que casi no se usa va en un lugar más alejado o en archivo pasivo. Se usa la frecuencia de consulta para decidir: más consultas, más cerca. Esto ahorra tiempo y esfuerzo.",
        "El análisis termina con una propuesta concreta: qué sistema se aplica, en qué orden quedan los elementos y dónde se ubica cada grupo. La propuesta se anota y se comunica a quienes usan el archivo, para que todos usen las mismas reglas.",
    ],
    vocab=[("orden alfabético", "orden de las palabras según el abecedario"), ("orden creciente", "de menor a mayor"), ("frecuencia de consulta", "cuántas veces se usa algo en un período"), ("accesible", "fácil de alcanzar"), ("propuesta", "solución que se presenta para aprobar"), ("regla común", "norma que todos usan igual")],
    worked=[
        ("Orden alfabético", "Ordena estos apellidos ficticios: Mora, Alvarez, Lagos. ¿Cuál queda primero?", ["Se compara la primera letra: A, L, M.", "La A va antes."], "Alvarez"),
        ("Orden numérico", "Ordena de menor a mayor: 73, 8, 140, 21. ¿Cuál queda último?", ["De menor a mayor: 8, 21, 73, 140.", "El último es el mayor."], "140"),
    ],
    mistakes=[("Ordenar los números de factura como si fueran palabras: 118, 12, 207...", "Como texto el 12 queda después del 118, lo que no coincide con el orden numérico.", "Ordena los números por su valor, de menor a mayor."),
              ("Poner arriba lo que casi no se usa porque «es lo más importante».", "Se pierde tiempo alcanzando lo que se usa mucho.", "Ubica lo que más se consulta en el lugar más accesible.")],
    T=[
        ("abc", "En Administración: ¿qué criterio ordena las carpetas de clientes que se buscan por apellido?", "El orden alfabético", "El orden por tamaño de carpeta", "El orden por color", "Si se busca por apellido, conviene ordenar alfabéticamente."),
        ("abc", "{F} Ordenando alfabéticamente los apellidos de la ficha, ¿cuál queda primero?", "Araya", "Bravo", "Pérez", "Araya empieza con A y queda antes que los demás."),
        ("abc", "{F} Ordenando alfabéticamente los apellidos de la ficha, ¿cuál queda último?", "Soto", "Pérez", "Muñoz", "Soto empieza con S, que viene después de P y M en el abecedario."),
        ("abc", "{F} Ordenando alfabéticamente los apellidos de la ficha, ¿cuál queda en tercer lugar?", "Contreras", "Bravo", "Díaz", "El orden es Araya, Bravo, Contreras, Díaz, Muñoz, Pérez, Soto."),
        ("abc", "{F} Ordenando los números de factura de menor a mayor, ¿cuál queda segundo?", "118", "12", "207", "El orden es 12, 118, 207, 245, 391."),
        ("abc", "{F} Ordenando los números de factura de menor a mayor, ¿cuál queda último?", "391", "245", "12", "391 es el número mayor de la lista."),
        ("=", "{F} ¿Cuántas consultas suman en total las cuatro carpetas con consultas registradas?", "3+18+1+9", "Se suman las consultas de Soto, Araya, Díaz y Pérez.", " consultas"),
        ("abc", "{F} ¿Qué carpeta conviene ubicar en el cajón A, el más cómodo?", "Araya, que se consultó 18 veces", "Díaz, que se consultó 1 vez", "Soto, que se consultó 3 veces", "Lo más consultado debe estar más a mano."),
        ("abc", "{F} ¿Qué carpeta conviene ubicar en el cajón D o en archivo pasivo?", "Díaz, que se consultó solo 1 vez", "Araya, que se consultó 18 veces", "Pérez, que se consultó 9 veces", "Lo que casi no se consulta puede ir en el lugar menos cómodo."),
        ("=", "{F} Araya se consultó 18 veces y cada vez se pierden 3 minutos extra si está en un cajón difícil. ¿Cuántos minutos se pierden en el mes?", "18*3", "Minutos perdidos = consultas × minutos extra por consulta.", " minutos"),
        ("abc", "Dos apellidos de ejemplo: «Soto» y «Sosa». ¿Cuál va primero alfabéticamente?", "Sosa, porque la tercera letra «s» va antes que la «t»", "Soto, porque es más corto", "Soto, porque la «t» va antes que la «s»", "Empatan en «So» y se compara la tercera letra: «s» antecede a «t»."),
        ("abc", "{F} Un compañero propone ordenar los números de factura como si fueran palabras, cifra por cifra. ¿Qué problema tiene?", "El 12 queda después del 118 aunque es menor; hay que ordenar por valor", "Ninguno, queda igual", "Los números mayores quedan antes que los menores", "Como texto, «118» antecede a «12»; el orden numérico usa el valor."),
        ("abc", "{F} Terminado el orden, ¿qué debe hacer la persona que ordenó?", "Anotar la regla usada y avisar al equipo para que todos la usen", "Guardar el secreto del orden", "Cambiar el orden cada día", "Las reglas comunes sostienen el orden en el tiempo."),
    ],
    ctx=("abc", "Una asistente recibe otra carpeta de Araya con documentos nuevos. ¿Dónde debe archivarla?", "Junto a las demás carpetas de Araya, en el lugar de mayor acceso", "Al final del cajón D", "En el pasillo mientras tanto", "Los documentos de un mismo cliente se agrupan, y los más consultados van a mano."),
    sc=[
        ("En Administración: ¿cómo se ordena de menor a mayor?", "Comenzando por el valor más pequeño", "El orden creciente va del menor al mayor."),
        ("¿Dónde se ubica lo que más se consulta?", "En el lugar más accesible", "Así se ahorra tiempo y esfuerzo."),
        ("¿Cómo se comparan dos apellidos que empiezan igual?", "Con la letra siguiente", "Se avanza letra por letra hasta que difieran."),
    ],
    op=("Con la Ficha 21, escribe la propuesta de orden: la lista de apellidos en orden alfabético, la lista de facturas de menor a mayor, y en qué cajón (A, B, C o D) pondrías las carpetas de Araya, Pérez, Soto y Díaz con una razón para cada una.\n{F}",
        "Apellidos: Araya, Bravo, Contreras, Díaz, Muñoz, Pérez, Soto. Facturas: 12, 118, 207, 245, 391. Araya en A (18 consultas); Pérez en B (9); Soto en C (3); Díaz en D (1). Regla: lo más consultado, más a mano.",
        ["ordena bien ambas listas", "asigna cajones según las consultas", "da una razón por carpeta"],
        ["dos listas ordenadas y cuatro razones"],
        ["orden alfabético equivocado", "ubicar lo menos usado en A", "no dar razones"],
        "Revisa ambas listas contra la ficha. Si un cajón no coincide con las consultas, pide revisar."),
    reinforce="Ordena en papel ocho apellidos que inventes y asigna dos cajones según una frecuencia que también inventes.",
    extend="Explica con un ejemplo inventado cuándo conviene cambiar la ubicación de una carpeta.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 22 (datos de ejemplo, inventados) de «Contadores Los Álamos». Un archivador tiene 4 cajones (A, B, C y D); en cada cajón caben 8 carpetas; cada carpeta contiene hasta 25 documentos. Se deben archivar 600 documentos. "
     "Las carpetas se numeran desde la 1 y se reparten en orden: carpetas 1 a 8 en el cajón A, 9 a 16 en el B, 17 a 24 en el C, y así. Código de ubicación de ejemplo: letra del cajón y puesto dentro del cajón, por ejemplo A-03. "
     "Búsqueda: antes de ordenar tomaba 6 minutos por documento; después de ordenar toma 2 minutos. Se hacen 15 búsquedas al día y se trabaja 5 días a la semana.")
build(
    O5, 4, F,
    use="Aprenderé a calcular la capacidad de un archivo, a asignar códigos de ubicación y a estimar el tiempo que se ahorra al ordenar.",
    prior=["Conozco los sistemas de archivo.", "Sé multiplicar y dividir.", "Sé qué es una frecuencia de consulta."],
    explain=[
        "La capacidad de un archivo se calcula multiplicando: cajones × carpetas por cajón × documentos por carpeta. Para saber cuántas carpetas hacen falta, se divide el total de documentos entre los documentos por carpeta; si no es exacto, se aproxima hacia arriba, porque no se puede usar una carpeta incompleta. Se compara la capacidad con lo que se debe archivar para decidir si alcanza.",
        "Un código de ubicación permite recuperar un documento sin buscarlo carpeta por carpeta. En el ejemplo, la letra indica el cajón y el número indica el puesto dentro del cajón. Para asignarlo se calcula en qué cajón cae la carpeta: si cada cajón guarda 8 carpetas, la carpeta 9 es la primera del cajón B, es decir B-01.",
        "El beneficio del orden se estima midiendo tiempos. Tiempo ahorrado por búsqueda = tiempo antes − tiempo después. Se multiplica por el número de búsquedas del día, de la semana o del mes. Es una estimación con datos de ejemplo: el tiempo real se mide en la oficina con un registro.",
    ],
    vocab=[("capacidad", "cantidad máxima que cabe"), ("código de ubicación", "clave que indica dónde está una carpeta"), ("tiempo ahorrado", "tiempo antes menos tiempo después"), ("aproximar hacia arriba", "subir al número entero siguiente cuando sobra"), ("estimación", "cálculo aproximado con datos de ejemplo"), ("puesto", "lugar de una carpeta dentro de un cajón")],
    worked=[
        ("Capacidad", "Un mueble de ejemplo tiene 3 cajones, 6 carpetas por cajón y 20 documentos por carpeta. ¿Cuántos documentos caben?", ["3 × 6 = 18 carpetas.", "18 × 20 = 360 documentos."], "360 documentos"),
        ("Código", "En el mismo mueble ficticio, cada cajón guarda 6 carpetas. ¿Qué código tiene la carpeta 8 (cajones A, B, C)?", ["Las carpetas 1 a 6 van en A y 7 a 12 en B.", "La 8 es la segunda del cajón B."], "B-02"),
    ],
    mistakes=[("Con 604 documentos, usar solo 24 carpetas y dejar fuera los 4 documentos que sobran.", "Esos 4 documentos necesitan una carpeta más, aunque quede casi vacía.", "Aproxima hacia arriba al número entero siguiente."),
              ("Calcular el tiempo ahorrado con el tiempo de después menos el de antes.", "Da un valor negativo que no tiene sentido como ahorro.", "Resta antes − después.")],
    T=[
        ("abc", "En Administración: ¿cómo se calcula la capacidad de un archivador?", "Cajones por carpetas por cajón por documentos por carpeta", "Cajones más carpetas más documentos", "Cajones menos documentos", "La capacidad se obtiene multiplicando las cantidades de cada nivel."),
        ("=", "{F} ¿Cuántas carpetas caben en el archivador?", "4*8", "Carpetas = cajones × carpetas por cajón.", " carpetas"),
        ("=", "{F} ¿Cuántos documentos caben en total en el archivador?", "4*8*25", "Capacidad = cajones × carpetas por cajón × documentos por carpeta.", " documentos"),
        ("=", "{F} ¿Cuántas carpetas de 25 documentos se necesitan para archivar los 600 documentos?", "600//25", "Carpetas necesarias = documentos ÷ documentos por carpeta.", " carpetas"),
        ("abc", "{F} ¿Alcanza el archivador para los 600 documentos?", "Sí, porque caben 800 documentos", "No, porque caben 500 documentos", "No se puede saber", "La capacidad de 800 documentos supera a los 600 que se archivarán."),
        ("=", "{F} ¿Cuántos documentos quedan de espacio libre después de archivar los 600?", "4*8*25-600", "Espacio libre = capacidad − documentos archivados.", " documentos"),
        ("abc", "{F} ¿Qué código de ubicación tiene la carpeta 11?", "B-03", "A-11", "C-03", "Las carpetas 9 a 16 van en el cajón B y la 11 es la tercera: B-03."),
        ("abc", "{F} ¿Qué código tiene la carpeta 17?", "C-01", "B-09", "A-17", "La carpeta 17 es la primera del cajón C."),
        ("=", "{F} ¿Cuántos minutos se ahorran por búsqueda después de ordenar?", "6-2", "Ahorro = tiempo antes − tiempo después.", " minutos"),
        ("=", "{F} ¿Cuántos minutos se ahorran al día con 15 búsquedas?", "(6-2)*15", "Ahorro diario = ahorro por búsqueda × búsquedas.", " minutos"),
        ("=", "{F} ¿Cuántas horas se ahorran en la semana de 5 días?", "(6-2)*15*5//60", "Se pasa de minutos a horas dividiendo por 60.", " horas"),
        ("abc", "{F} Un compañero dice que el ahorro semanal calculado es un dato exacto del futuro. ¿Qué respondes?", "Es una estimación con datos de ejemplo; hay que medir los tiempos reales", "Tiene razón, es exacto", "Es una mentira", "Con tiempos de ejemplo el cálculo es una estimación que se confirma midiendo."),
        ("abc", "{F} Se llegan a archivar 650 documentos en vez de 600. ¿Cuántas carpetas se necesitarían?", "26, porque 650 ÷ 25 = 26", "25, porque 650 se aproxima hacia abajo", "27", "650 ÷ 25 da exactamente 26 carpetas."),
    ],
    ctx=("abc", "Una jefatura pregunta si vale la pena ordenar el archivo. ¿Qué datos de la ficha respaldan una respuesta?", "El ahorro de 4 minutos por búsqueda, que suma 5 horas por semana con los datos de ejemplo", "El color de las carpetas", "El nombre del archivador", "El tiempo ahorrado se estima con los datos de búsqueda de la ficha."),
    sc=[
        ("En Administración: ¿qué se hace si el número de carpetas no es exacto?", "Se aproxima hacia arriba", "No se puede usar media carpeta."),
        ("¿Cómo se calcula el tiempo ahorrado por búsqueda?", "Tiempo antes menos tiempo después", "Así el ahorro resulta un valor positivo y comprensible."),
        ("¿Qué indica un código de ubicación como B-03?", "El cajón B y el puesto 3 dentro del cajón", "El código permite ir directo a la carpeta."),
    ],
    op=("Con la Ficha 22, escribe una hoja de cálculo en papel con: capacidad, carpetas necesarias, espacio libre, código de la carpeta 20, ahorro diario y semanal de tiempo. Agrega una frase sobre cómo medirías el tiempo real.\n{F}",
        "Capacidad: 800 documentos. Carpetas necesarias: 24. Espacio libre: 200 documentos. La carpeta 20 queda en el cajón C, puesto 4: C-04. Ahorro diario: 60 minutos. Ahorro semanal: 300 minutos, es decir 5 horas. Mediría los tiempos reales anotando durante una semana cuánto toma cada búsqueda.",
        ["calcula capacidad y carpetas", "asigna el código", "calcula el ahorro", "reconoce que es estimación"],
        ["hoja con seis cálculos y una frase"],
        ["no aproximar hacia arriba", "código equivocado", "presentar la estimación como exacta"],
        "Rehace los seis cálculos. Si el código no coincide, pide dividir de nuevo las carpetas por cajón."),
    reinforce="Calcula la capacidad de un mueble ficticio de 5 cajones con 7 carpetas por cajón y 30 documentos por carpeta.",
    extend="Explica con un ejemplo inventado cómo cambiaría el código si cada cajón guardara 10 carpetas.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 23 (estación de trabajo de ejemplo, inventada) de «Contadores Los Álamos». Equipos: computador de escritorio con pantalla, impresora de oficina, escáner, teléfono y calculadora. "
     "Prácticas observadas en un día de ejemplo: el computador y la pantalla quedan encendidos toda la noche; los borradores se imprimen por una sola cara; la clave se anota en un papel pegado al monitor; "
     "la silla está baja y la pantalla muy arriba; la persona no hace pausas en 4 horas seguidas.")
build(
    O6, 1, F,
    use="Aprenderé qué equipos y herramientas usa la gestión administrativa, qué cuidados de seguridad, ergonomía y uso eficiente de energía, materiales e insumos corresponden, y cuándo pedir ayuda al soporte técnico.",
    prior=["Sé qué es un documento.", "Conozco equipos de oficina.", "Sé que las claves son personales."],
    explain=[
        "Los equipos y herramientas tecnológicas de la gestión administrativa son los computadores, impresoras, escáneres, teléfonos y los programas de oficina que se usan para registrar, comunicar y archivar información. Usarlos bien significa hacerlo con eficiencia: gastar la energía, los materiales y los insumos que realmente se necesitan, como apagar el equipo al terminar y no imprimir lo que no hace falta.",
        "El uso seguro tiene tres cuidados. Primero, seguridad de la información: la clave es personal, no se comparte ni se anota a la vista, y la pantalla se bloquea al alejarse. Segundo, ergonomía: pantalla a la altura de los ojos, espalda apoyada, pies en el suelo y pausas cortas cada 45 minutos para descansar la vista y el cuerpo. Tercero, seguridad eléctrica: nunca se abre un equipo ni se repara por cuenta propia; ante una falla, se desconecta de forma segura si es posible y se avisa al soporte técnico.",
        "Cada equipo tiene un manual de uso y la empresa tiene políticas sobre su uso. Estas reglas se consultan antes de usar un equipo nuevo o de cambiar una práctica. Las normas de seguridad eléctrica y de prevención de riesgos son parte de la norma vigente.",
    ],
    vocab=[("equipo", "aparato que se usa para trabajar, como un computador"), ("eficiencia", "lograr el trabajo gastando solo lo necesario"), ("ergonomía", "adaptar el puesto al cuerpo para evitar dolores y cansancio"), ("pausa", "descanso breve durante el trabajo"), ("soporte técnico", "persona o área que revisa y repara equipos"), ("manual de uso", "documento que explica cómo usar un equipo")],
    worked=[
        ("Ahorrar energía", "Una persona de ejemplo deja la pantalla encendida durante el almuerzo de una hora. ¿Qué práctica eficiente corresponde?", ["La pantalla gasta energía aunque nadie la mire.", "Se apaga o se activa el modo de ahorro al alejarse."], "Apagar o activar el modo ahorro"),
        ("Pedir ayuda", "La impresora de una oficina ficticia huele a quemado. ¿Qué se hace?", ["No se abre ni se repara.", "Se aparta si es seguro, se desconecta si es posible sin riesgo y se avisa al soporte técnico."], "Avisar al soporte técnico sin abrir el equipo"),
    ],
    mistakes=[("Anotar la clave en un papel pegado al monitor.", "Cualquiera podría usarla y ocultar sus acciones bajo tu nombre.", "Memoriza la clave o usa el método autorizado por la empresa."),
              ("Abrir una impresora que falla para «arreglarla rápido».", "Hay riesgos eléctricos y se pueden dañar piezas.", "Avisa al soporte técnico.")],
    T=[
        ("abc", "En Administración: ¿qué significa usar un equipo con eficiencia?", "Gastar solo la energía, los materiales y los insumos necesarios", "Usarlo sin pausas para trabajar más rápido", "Comprar el equipo más caro", "La eficiencia busca el mismo resultado con menos gasto de recursos."),
        ("abc", "{F} ¿Qué práctica de la ficha desperdicia energía?", "Dejar el computador y la pantalla encendidos toda la noche", "Usar la calculadora", "Escribir una carta", "Un equipo encendido sin uso consume energía sin beneficio."),
        ("abc", "{F} ¿Qué práctica de la ficha desperdicia materiales?", "Imprimir los borradores por una sola cara", "Usar el teléfono", "Guardar archivos", "Los borradores por una cara usan el doble de hojas necesarias."),
        ("abc", "{F} ¿Qué falla de seguridad de la información aparece en la ficha?", "La clave anotada en un papel pegado al monitor", "El uso de la calculadora", "El teléfono sobre el escritorio", "Una clave a la vista permite que otras personas la usen."),
        ("abc", "{F} ¿Qué problema de ergonomía muestra la ficha?", "Silla baja y pantalla muy arriba, sin pausas en 4 horas", "La impresora es demasiado pequeña", "El escritorio es claro", "La postura incorrecta y la falta de pausas cansan y pueden causar dolores."),
        ("abc", "¿Cada cuánto se recomienda hacer una pausa corta frente al computador, según este cuaderno?", "Cada 45 minutos", "Cada 4 horas", "Una vez al día", "El cuaderno recomienda pausas cortas cada 45 minutos para descansar."),
                ("=", "{F} Si cada pausa dura 5 minutos y la persona hace 6 pausas en la jornada, ¿cuántos minutos de pausa suma?", "6*5", "Minutos de pausa = pausas × minutos de cada pausa.", " minutos"),
                ("=", "¿A cuántas resmas de 500 hojas equivalen 3.000 hojas de borradores impresas en un mes?", "3000//500", "Resmas = hojas ÷ hojas por resma.", " resmas"),
        ("=", "Se imprimen 40 páginas de borradores por ambas caras en vez de una sola. ¿Cuántas hojas se usan?", "40//2", "Por ambas caras caben dos páginas en cada hoja.", " hojas"),
        ("abc", "Una impresora se detiene y muestra una luz roja parpadeante. ¿Qué corresponde?", "Revisar el manual de uso y avisar al soporte técnico si persiste", "Abrirla y desarmarla", "Golpearla para que funcione", "Se consulta el manual y se pide ayuda; no se manipulan piezas internas."),
        ("abc", "Una persona se aleja de su computador para ir a una reunión de 20 minutos. ¿Qué es lo más adecuado?", "Bloquear la pantalla para proteger la información", "Dejar la pantalla abierta con los datos de clientes", "Compartir la clave con un compañero para que vigile", "Bloquear la pantalla evita que otras personas vean o usen la información."),
        ("abc", "Un compañero pide la clave de otra persona «solo por hoy». ¿Qué respuesta corresponde?", "Negarse, porque la clave es personal; el acceso se solicita a la jefatura o al soporte", "Entregarla si es de confianza", "Entregarla si lo pide por favor", "Compartir claves rompe la trazabilidad y la seguridad de la información."),
        ("abc", "{F} ¿Qué cambio de ergonomía propondrías primero?", "Subir la silla y bajar la pantalla a la altura de los ojos", "Mover el escritorio al pasillo", "Poner la pantalla en el suelo", "El ajuste de la silla y de la pantalla mejora la postura."),
    ],
    ctx=("abc", "Una asistente se da cuenta de que lleva tres horas seguidas frente al computador y le duelen los ojos. ¿Qué hace?", "Hace una pausa corta, mira a lo lejos y vuelve a su puesto con la postura corregida", "Sigue trabajando para no atrasarse", "Sube el brillo de la pantalla al máximo", "La pausa descansa la vista y el cuerpo; no se debe forzar la jornada."),
    sc=[
        ("En Administración: ¿por qué la clave es personal?", "Porque identifica quién hizo cada acción y protege la información", "Una clave compartida deja de identificar a la persona."),
        ("¿Qué haces ante una falla eléctrica de un equipo?", "No lo abro y aviso al soporte técnico", "Reparar un equipo energizado es riesgoso."),
        ("¿Qué pausa recomienda el cuaderno?", "Una pausa corta cada 45 minutos", "Así se descansa la vista y el cuerpo."),
    ],
    op=("Con la Ficha 23, escribe una lista de cinco mejoras para la estación de trabajo: una de energía, una de materiales, una de seguridad de la información, una de ergonomía y una para pedir ayuda al soporte técnico, cada una con una razón.\n{F}",
        "Energía: apagar el computador y la pantalla al terminar la jornada, porque gastan energía sin uso. Materiales: imprimir borradores por ambas caras, porque se usa la mitad de las hojas. Información: memorizar la clave y bloquear la pantalla al alejarse. Ergonomía: ajustar silla y pantalla y hacer una pausa cada 45 minutos. Soporte: avisar si la impresora falla, sin abrirla.",
        ["cubre las cinco categorías", "da una razón por mejora", "no propone abrir equipos"],
        ["lista de cinco mejoras con razón"],
        ["abrir o reparar equipos", "dejar la clave visible", "omitir las pausas"],
        "Revisa que cada categoría tenga una mejora y una razón. Si propone abrir un equipo, pide cambiarlo por avisar al soporte."),
    reinforce="Anota en tu cuaderno tres hábitos de uso eficiente de energía y tres de papel para una oficina ficticia.",
    extend="Explica con un ejemplo inventado cómo una mala postura prolongada puede afectar el trabajo.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 24 (glosario y documentos de ejemplo, inventados) de «Contadores Los Álamos». Hardware: partes físicas del equipo (pantalla, teclado, impresora). Software: programas (procesador de texto, planilla de cálculo, correo electrónico). "
     "Procesador de texto: para escribir documentos. Planilla de cálculo: para tablas y cálculos. Respaldo: copia de seguridad guardada en otro lugar. Manual de uso: explica cómo usar un equipo. "
     "Hoja de mantención: registro de las revisiones hechas por el soporte técnico. Registro de consumo: anota papel, tóner y energía usados. Roles: usuario (usa el equipo), soporte técnico (revisa y repara), jefatura (autoriza compras y fija políticas).")
build(
    O6, 2, F,
    use="Aprenderé los conceptos de hardware y software, las herramientas de oficina más usadas y los documentos y roles que ordenan su uso.",
    prior=["Sé qué equipos hay en una oficina.", "Sé usar eficiencia y ergonomía.", "Sé que la información es reservada."],
    explain=[
        "El hardware es la parte física de un equipo, como la pantalla, el teclado o la impresora. El software son los programas que le dicen al equipo qué hacer. Entre los programas de oficina están el procesador de texto, que sirve para escribir documentos, la planilla de cálculo, para ordenar datos en tablas y hacer cálculos, y el correo electrónico, para enviar y recibir mensajes.",
        "Algunos documentos acompañan el uso de los equipos. El manual de uso explica cómo usarlos de forma correcta y segura. La hoja de mantención registra las revisiones que hace el soporte técnico. El registro de consumo anota cuánto papel, tóner y energía se usan, y sirve para detectar gastos innecesarios. El respaldo es una copia de seguridad de los archivos importantes, guardada en otro lugar, para no perder información si un equipo falla.",
        "Los roles se distinguen: el usuario usa el equipo siguiendo las reglas; el soporte técnico revisa y repara; la jefatura autoriza compras y define las políticas de uso. El usuario no instala programas por su cuenta y no copia información de la empresa a dispositivos personales sin autorización.",
    ],
    vocab=[("hardware", "partes físicas de un equipo"), ("software", "programas de un equipo"), ("planilla de cálculo", "programa para tablas y cálculos"), ("respaldo", "copia de seguridad guardada en otro lugar"), ("hoja de mantención", "registro de revisiones del soporte técnico"), ("registro de consumo", "anotación de papel, tóner y energía usados")],
    worked=[
        ("Hardware o software", "Clasifica estas dos cosas de una oficina ficticia: la impresora y el programa de correo electrónico.", ["La impresora es una parte física.", "El correo electrónico es un programa."], "Impresora: hardware; correo electrónico: software"),
        ("Elegir la herramienta", "Se necesita sumar los gastos de un mes en una tabla de 30 filas. ¿Qué programa conviene?", ["Hay una tabla con cálculos.", "Eso lo hace la planilla de cálculo."], "La planilla de cálculo"),
    ],
    mistakes=[("Guardar los archivos importantes solo en un computador, sin respaldo.", "Si el equipo falla, la información se pierde.", "Haz el respaldo en otro lugar autorizado."),
              ("Instalar un programa descargado sin consultar.", "Puede traer fallas o ser inseguro.", "Pide la instalación al soporte técnico con autorización de la jefatura.")],
    T=[
        ("abc", "En Administración: ¿qué es el software?", "Los programas que indican al equipo qué hacer", "Las partes físicas del equipo", "El mueble del computador", "El software son los programas; las partes físicas son el hardware."),
        ("abc", "{F} ¿Cuál de estos elementos es hardware?", "La impresora", "El procesador de texto", "La planilla de cálculo", "La impresora es una parte física del equipo."),
        ("abc", "{F} ¿Qué programa conviene para escribir una carta formal?", "El procesador de texto", "La planilla de cálculo", "El respaldo", "El procesador de texto sirve para escribir documentos."),
        ("abc", "{F} ¿Qué programa conviene para sumar una tabla de gastos?", "La planilla de cálculo", "El procesador de texto", "El correo electrónico", "La planilla de cálculo ordena datos en tablas y hace cálculos."),
        ("abc", "{F} ¿Qué documento registra las revisiones que hace el soporte técnico?", "La hoja de mantención", "El registro de consumo", "El manual de uso", "La hoja de mantención anota las revisiones del soporte."),
        ("abc", "{F} ¿Qué documento permite detectar un gasto excesivo de papel?", "El registro de consumo", "El manual de uso", "La hoja de mantención", "El registro de consumo anota cuánto papel se usa."),
        ("abc", "¿Qué es un respaldo?", "Una copia de seguridad guardada en otro lugar", "El archivo original sin copias", "Un programa para escribir", "El respaldo protege contra la pérdida de información."),
        ("=", "En el registro de consumo de ejemplo se anotan 12 resmas en enero y 9 en febrero. ¿Cuántas resmas se usaron en los dos meses?", "12+9", "Se suman los consumos mensuales.", " resmas"),
        ("=", "El mismo registro de ejemplo muestra 12 resmas en enero y 9 en febrero. ¿Cuántas resmas menos se usaron en febrero?", "12-9", "Diferencia = consumo de enero − consumo de febrero.", " resmas"),
        ("abc", "Una persona quiere instalar un programa descargado de internet. ¿Qué corresponde?", "Pedir autorización a la jefatura y solicitar la instalación al soporte técnico", "Instalarlo ella misma sin avisar", "Pedir a un compañero que lo instale", "Los programas se instalan con autorización y por el soporte técnico."),
        ("abc", "Un usuario copia la planilla de sueldos a su dispositivo personal «para adelantar trabajo». ¿Qué falla?", "Saca información reservada de la empresa sin autorización", "Nada, porque es información suya", "Falta cambiar el nombre del archivo", "Copiar datos reservados a dispositivos personales los expone."),
        ("abc", "{F} ¿Quién autoriza la compra de un equipo nuevo?", "La jefatura", "El usuario", "El soporte técnico solo", "Según la ficha, la jefatura autoriza compras y fija políticas."),
        ("abc", "{F} El computador no enciende y huele a quemado. ¿Quién debe revisarlo?", "El soporte técnico", "El usuario, abriéndolo", "Un compañero que sabe de electricidad", "El soporte técnico revisa y repara; el usuario no abre el equipo."),
    ],
    ctx=("abc", "Una asistente prepara un informe con tablas y gráficos de gastos mensuales. ¿Qué herramienta usa para ordenar los números?", "Una planilla de cálculo", "El correo electrónico", "Un respaldo", "La planilla de cálculo organiza y calcula datos en tablas."),
    sc=[
        ("En Administración: ¿qué diferencia hay entre hardware y software?", "El hardware es la parte física; el software, los programas", "Uno se toca y el otro es el conjunto de programas."),
        ("¿Para qué sirve un respaldo?", "Para no perder información si el equipo falla", "La copia queda en otro lugar."),
        ("¿Quién repara un equipo que falla?", "El soporte técnico", "El usuario no manipula las partes internas."),
    ],
    op=("Con la Ficha 24, arma una tabla de tres columnas: Herramienta, Para qué sirve, Cuidado al usarla, con estas cinco filas: procesador de texto, planilla de cálculo, correo electrónico, impresora y respaldo.\n{F}",
        "Procesador de texto: escribir documentos; cuidado: guardar el archivo y no incluir datos reservados sin necesidad. Planilla de cálculo: tablas y cálculos; revisar las fórmulas. Correo electrónico: enviar mensajes; revisar destinatario y adjuntos. Impresora: imprimir lo necesario, por ambas caras; no abrirla si falla. Respaldo: copia de seguridad; guardarla en otro lugar autorizado.",
        ["describe bien cada herramienta", "propone un cuidado concreto", "no incluye abrir equipos"],
        ["tabla de cinco filas y tres columnas"],
        ["confundir hardware y software", "no mencionar cuidados", "omitir el respaldo"],
        "Revisa que cada fila tenga un uso correcto. Si falta el cuidado, pide agregarlo."),
    reinforce="Clasifica en papel diez elementos de una oficina en hardware o software.",
    extend="Explica con un ejemplo inventado qué pasaría si una oficina no hiciera nunca un respaldo.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 25 (registro de consumo de ejemplo, inventado) de «Contadores Los Álamos» en un mes de 20 días de trabajo. Papel: 20 resmas de 500 hojas cada una. Tóner: 3 cartuchos. "
     "Energía: hay 4 computadores de 100 W cada uno; todos funcionan 8 horas al día; 2 de ellos quedan además encendidos 16 horas más cada día sin uso. Tarifa de ejemplo: $200 por kWh (1 kWh equivale a 1.000 Wh). "
     "Se estima que el 60 % del papel impreso corresponde a documentos internos que podrían imprimirse por ambas caras.")
build(
    O6, 3, F,
    use="Aprenderé a leer un registro de consumo, a calcular energía y papel gastados con datos de ejemplo y a detectar dónde se puede ahorrar.",
    prior=["Sé multiplicar y dividir.", "Sé qué es un registro de consumo.", "Sé qué es eficiencia."],
    explain=[
        "El consumo de energía de un equipo se calcula como potencia × tiempo. La potencia se mide en watts (W) y el resultado en watt-hora (Wh). Como el Wh es una unidad pequeña, se usa el kilowatt-hora (kWh): 1 kWh son 1.000 Wh. Por ejemplo, 100 W durante 10 horas son 1.000 Wh, es decir, 1 kWh. El costo de la energía se calcula multiplicando los kWh por la tarifa; aquí se usa una tarifa de ejemplo.",
        "El consumo de papel se mide en hojas: una resma tiene 500 hojas. Imprimir por ambas caras usa la mitad de hojas para el mismo número de páginas. Para saber cuánto se ahorra, se calcula qué parte del papel se puede imprimir por ambas caras y se divide por 2.",
        "Leer el registro de consumo permite hallar ahorros: equipos encendidos sin uso, impresión innecesaria o tóner gastado en borradores. La medida de ahorro se propone a la jefatura con su efecto estimado, y se confirma midiendo el mes siguiente.",
    ],
    vocab=[("potencia", "energía que usa un equipo por unidad de tiempo, medida en watts"), ("watt-hora (Wh)", "unidad de energía: watts por horas"), ("kilowatt-hora (kWh)", "1.000 Wh"), ("tarifa", "precio de una unidad de energía"), ("resma", "paquete de 500 hojas"), ("ahorro", "lo que se deja de gastar")],
    worked=[
        ("Energía", "Un equipo de ejemplo de 200 W funciona 5 horas. ¿Cuántos Wh y cuántos kWh consume?", ["200 × 5 = 1.000 Wh.", "1.000 Wh = 1 kWh."], "1.000 Wh, o 1 kWh"),
        ("Papel", "Una oficina de ejemplo usa 4 resmas al mes. ¿Cuántas hojas son?", ["Cada resma tiene 500 hojas.", "4 × 500 = 2.000."], "2.000 hojas"),
    ],
    mistakes=[("Olvidar convertir Wh a kWh antes de aplicar la tarifa.", "La tarifa es por kWh; el costo resulta mil veces más alto.", "Divide los Wh entre 1.000 para obtener los kWh."),
              ("Calcular el ahorro de papel sobre todas las hojas, y no solo las que pueden imprimirse por ambas caras.", "Se exagera el ahorro.", "Aplica el ahorro solo a la parte que corresponde.")],
    T=[
        ("abc", "En Administración: ¿cómo se calcula el consumo de energía de un equipo?", "Potencia por tiempo", "Potencia más tiempo", "Tiempo dividido por potencia", "El consumo se obtiene multiplicando la potencia por las horas de uso."),
        ("abc", "¿Cuántos Wh tiene 1 kWh?", "1.000", "100", "10", "Un kilowatt-hora equivale a 1.000 watt-hora."),
        ("=", "{F} ¿Cuántos Wh consume un computador de 100 W durante las 8 horas diarias?", "100*8", "Wh = potencia × horas.", " Wh"),
        ("=", "{F} ¿Cuántas hojas se usaron en el mes (20 resmas de 500 hojas cada una)?", "20*500", "Hojas = resmas × hojas por resma.", " hojas"),
        ("=", "{F} ¿Cuántos Wh consume en total en el mes un computador de 100 W que funciona 8 horas al día durante 20 días?", "100*8*20", "Wh del mes = potencia × horas al día × días.", " Wh"),
        ("=", "{F} Cada uno de los 2 computadores queda encendido 16 horas más al día sin uso. ¿Cuántos kWh se gastan en total en el mes por esas horas extra?", "2*100*16*20//1000", "Se multiplican equipos, watts, horas extra y días, y se divide por 1.000.", " kWh"),
        ("=", "{F} ¿Cuántos pesos cuesta esa energía gastada sin uso, con la tarifa de ejemplo?", "2*100*16*20//1000*200", "Costo = kWh × tarifa de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuántas hojas del mes corresponden a documentos internos que podrían imprimirse por ambas caras (60 %)?", "20*500*60//100", "Parte = total de hojas × 60 ÷ 100.", " hojas"),
        ("=", "{F} Si esas hojas se imprimieran por ambas caras, ¿cuántas hojas se ahorrarían?", "20*500*60//100//2", "Por ambas caras se usa la mitad; se ahorra la otra mitad.", " hojas"),
        ("abc", "{F} ¿Qué práctica ahorra más energía según la ficha?", "Apagar los 2 computadores cuando no se usan", "Imprimir por ambas caras", "Cambiar el color de la pantalla", "Las 16 horas extra son el consumo evitable más grande de la ficha."),
        ("abc", "{F} Un colega dice que apagar los computadores ahorrará exactamente lo calculado todos los meses. ¿Qué respondes?", "Es una estimación con datos de ejemplo; se confirma midiendo el mes siguiente", "Es un valor exacto garantizado", "No hay ahorro posible", "El cálculo usa datos de ejemplo y debe verificarse con el registro real."),
        ("abc", "El registro de consumo muestra más tóner de lo normal. ¿Qué se investiga primero?", "Si se imprimen borradores o documentos que no se necesitan", "Si cambió el color de la oficina", "El nombre de quien llena el registro", "El tóner se gasta al imprimir, por eso se revisa qué se imprime."),
        ("abc", "Se decide apagar los equipos sin uso y el soporte pide que se haga con el procedimiento del manual. ¿Por qué?", "Para no dañar el equipo ni perder archivos sin guardar", "Para gastar más energía", "Para que el equipo se encienda solo", "El manual indica la forma segura de apagar para proteger equipo y archivos."),
    ],
    ctx=("abc", "La jefatura pregunta cuánto costaría al mes dejar los 2 computadores encendidos fuera de horario. ¿Qué cifra de la ficha responde?", "La energía de las 16 horas extra, calculada con la tarifa de ejemplo", "El costo de las 20 resmas", "El número de cartuchos", "El costo de energía gastada sin uso se calcula con las horas extra y la tarifa."),
    sc=[
        ("En Administración: ¿cuántos Wh son 1 kWh?", "1.000 Wh", "Un kilowatt-hora equivale a mil watt-hora de energía."),
        ("¿Cómo se calcula el costo de la energía?", "kWh multiplicados por la tarifa", "La tarifa se aplica a los kWh."),
        ("¿Por qué el ahorro calculado es una estimación?", "Porque usa datos de ejemplo y debe confirmarse", "El ahorro real se mide después."),
    ],
    op=("Con la Ficha 25, escribe un informe de seis líneas: energía mensual de un computador en kWh, kWh gastados sin uso en el mes, su costo, hojas que podrían ahorrarse por impresión por ambas caras, una propuesta y el supuesto de tu estimación.\n{F}",
        "Un computador gasta 16 kWh al mes. Sin uso se gastan 64 kWh, que cuestan $12.800 con la tarifa de ejemplo. Podrían ahorrarse 3.000 hojas imprimiendo por ambas caras los documentos internos. Propuesta: apagar los equipos fuera de horario e imprimir por ambas caras. Supuesto: el uso del mes siguiente será similar.",
        ["calcula la energía correctamente", "convierte Wh a kWh", "calcula el ahorro de hojas", "declara un supuesto"],
        ["informe de seis líneas con cifras"],
        ["olvidar dividir por 1.000", "ahorro de papel sobre todas las hojas", "no declarar supuestos"],
        "Rehace los cálculos con la ficha. Si no convierte a kWh, pídelo."),
    reinforce="Calcula en papel la energía en kWh de un equipo de 300 W que funciona 10 horas.",
    extend="Explica con un ejemplo inventado cómo cambiarías el registro de consumo para detectar mejor los gastos innecesarios.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 26 (alternativas de ejemplo, inventadas) para «Contadores Los Álamos». Se debe elegir entre dos impresoras ficticias. Impresora 1: precio $80.000, consumo de 500 W cuando imprime. Impresora 2: precio $112.000, consumo de 300 W cuando imprime. "
     "Uso estimado: 2 horas diarias de impresión durante 20 días al mes. Tarifa de ejemplo: $200 por kWh (1 kWh = 1.000 Wh). Criterios de la jefatura: costo total a 24 meses, impresión por ambas caras disponible en las dos, y seguridad (clave para retirar documentos reservados) disponible solo en la impresora 2.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico y económico para elegir entre dos equipos considerando energía, materiales, seguridad y costo total.",
    prior=["Sé calcular kWh y costo de energía.", "Sé que la información reservada se protege.", "Sé comparar alternativas."],
    explain=[
        "Elegir un equipo no es mirar solo el precio de compra. El costo total en un período es el precio más el costo de energía de ese período, más otros costos como insumos. Se calcula la energía mensual (potencia × horas × días ÷ 1.000), se multiplica por la tarifa y por los meses. La alternativa con menor costo total es más económica, siempre que cumpla los criterios obligatorios.",
        "Los criterios obligatorios son condiciones que el equipo debe cumplir sí o sí; por ejemplo, proteger los documentos reservados con clave de retiro. Una alternativa que no los cumple se descarta aunque sea más barata. Después se compara el costo entre las que cumplen. También se anotan los límites de la estimación: los consumos reales pueden variar.",
        "La decisión es de la jefatura. Quien analiza entrega la comparación con los cálculos a la vista, una recomendación y los supuestos. Todas las cifras de este cuaderno son de ejemplo; en un caso real se usan las del fabricante y las de la tarifa de la empresa, y se aplican las normas de seguridad vigentes.",
    ],
    vocab=[("costo total", "precio más costo de uso en un período"), ("criterio obligatorio", "condición que toda alternativa debe cumplir"), ("consumo mensual", "energía usada en un mes"), ("tarifa", "precio de un kWh"), ("recomendación", "propuesta que se entrega a quien decide"), ("supuesto", "dato no confirmado que se declara")],
    worked=[
        ("Energía mensual", "Un equipo de ejemplo de 400 W imprime 3 horas al día durante 20 días. ¿Cuántos kWh gasta al mes?", ["400 × 3 × 20 = 24.000 Wh.", "24.000 ÷ 1.000 = 24 kWh."], "24 kWh"),
        ("Descartar", "Una alternativa de ejemplo es más barata pero no tiene clave de retiro y es un criterio obligatorio. ¿Se elige?", ["No cumple un criterio obligatorio.", "Se descarta aunque sea más barata."], "No, se descarta"),
    ],
    mistakes=[("Elegir el equipo de menor precio sin calcular el consumo.", "A largo plazo puede salir más caro.", "Calcula el costo total en el período."),
              ("Elegir el equipo que no cumple un criterio obligatorio porque es más barato.", "Puede dejar información reservada expuesta.", "Descarta primero lo que no cumple y compara después.")],
    T=[
        ("abc", "En Administración: ¿qué incluye el costo total de un equipo en un período?", "El precio de compra más el costo de energía y otros costos de uso", "Solo el precio de compra", "El color y la marca", "El costo total suma lo que se paga al comprar y al usar."),
        ("=", "{F} ¿Cuántos kWh gasta al mes la impresora 1?", "500*2*20//1000", "kWh = potencia × horas × días ÷ 1.000.", " kWh"),
        ("=", "{F} ¿Cuántos kWh gasta al mes la impresora 2?", "300*2*20//1000", "kWh = potencia × horas × días ÷ 1.000.", " kWh"),
        ("=", "{F} ¿Cuántos pesos cuesta al mes la energía de la impresora 1?", "500*2*20//1000*200", "Costo mensual = kWh × tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta al mes la energía de la impresora 2?", "300*2*20//1000*200", "Costo mensual = kWh × tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta a 24 meses la energía de la impresora 1?", "500*2*20//1000*200*24", "Se multiplica el costo mensual por 24 meses.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta a 24 meses la energía de la impresora 2?", "300*2*20//1000*200*24", "Se multiplica el costo mensual por 24 meses.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total a 24 meses (precio más energía) de la impresora 1?", "80000+500*2*20//1000*200*24", "Costo total = precio + energía de 24 meses.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total a 24 meses (precio más energía) de la impresora 2?", "112000+300*2*20//1000*200*24", "Costo total = precio + energía de 24 meses.", " pesos"),
                ("=", "{F} ¿Cuántos pesos de diferencia hay entre el costo total a 24 meses de la impresora 1 y el de la impresora 2?", "(80000+500*2*20//1000*200*24)-(112000+300*2*20//1000*200*24)", "Se resta el costo total menor al mayor.", " pesos"),
        ("abc", "{F} Considerando solo el costo total a 24 meses, ¿qué impresora sale más barata?", "La impresora 2, por $6.400 de diferencia", "La impresora 1, porque su precio de compra es menor", "Cuestan exactamente lo mismo", "El menor consumo de la impresora 2 compensa su mayor precio en 24 meses."),
        ("abc", "{F} La jefatura exige clave para retirar documentos reservados. ¿Qué impresora cumple ese criterio obligatorio?", "La impresora 2", "La impresora 1", "Ninguna", "La ficha dice que la clave de retiro está disponible solo en la impresora 2."),
        ("abc", "{F} Con el criterio obligatorio de seguridad, ¿qué impresora se recomienda?", "La impresora 2, porque la 1 no cumple la seguridad aunque cueste menos", "La impresora 1, porque cuesta menos", "Ninguna, porque son iguales", "Un criterio obligatorio se cumple antes de comparar costos."),
    ],
    ctx=("abc", "La jefatura pregunta cuántos meses se tardaría en recuperar la mayor inversión de la impresora 2 por su menor consumo de energía. ¿Qué dato de la ficha usarías?", "La diferencia de precio y el ahorro mensual de energía de la impresora 2", "El color de las impresoras", "El nombre de la tienda", "El tiempo de recuperación se calcula con la diferencia de precio y el ahorro mensual."),
    sc=[
        ("En Administración: ¿cómo se calcula el consumo mensual en kWh?", "Potencia por horas por días, dividido por 1.000", "Se pasa de Wh a kWh dividiendo por mil."),
        ("¿Qué se hace con una alternativa que no cumple un criterio obligatorio?", "Se descarta", "Los criterios obligatorios se cumplen antes de comparar costos."),
        ("¿Qué entrega quien analiza a la jefatura?", "La comparación con cálculos, una recomendación y los supuestos", "La jefatura decide con esa información."),
    ],
    op=("Con la Ficha 26, escribe una recomendación de cinco líneas: energía mensual y costo a 24 meses de cada impresora, cuál cumple el criterio obligatorio, cuál recomiendas y un supuesto de tu estimación.\n{F}",
        "Impresora 1: 20 kWh al mes; costo total a 24 meses $176.000. Impresora 2: 12 kWh al mes; costo total a 24 meses $169.600. Solo la impresora 2 cumple el criterio obligatorio de clave de retiro. Recomiendo la impresora 2. Supuesto: el uso será de 2 horas diarias durante 20 días al mes.",
        ["calcula energía y costos de ambas", "aplica el criterio obligatorio", "recomienda con razón", "declara un supuesto"],
        ["recomendación de cinco líneas con cálculos"],
        ["ignorar la seguridad", "no convertir a kWh", "no declarar supuestos"],
        "Rehace las cuentas con la ficha. Si recomienda la 1 sin ver seguridad, pide revisar los criterios."),
    reinforce="Compara en papel dos equipos de ejemplo por precio y consumo mensual con una tarifa que inventes.",
    extend="Explica con un ejemplo inventado por qué un equipo más barato puede salir más caro a largo plazo.",
)

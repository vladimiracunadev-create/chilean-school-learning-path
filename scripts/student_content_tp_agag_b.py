"""Agropecuaria TP 4.º medio, mención Agricultura: OAM-03 (post cosecha), OAM-04 (acopio, clasificación y guarda) y OAM-05 (mantenimiento de maquinaria). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agag_common import AVISO, EMER, build

O3 = "TP-AGAG-4-OAM-03"
O4 = "TP-AGAG-4-OAM-04"
O5 = "TP-AGAG-4-OAM-05"

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Huerto Demo» recibe manzanas cosechadas en un galpón de embalaje con una cámara de frío. "
     "Peligros anotados: la cámara de frío (temperatura muy baja y una puerta que puede cerrarse con alguien dentro), cajas apiladas en altura, una transpaleta (carro para mover pallets) que circula entre las personas, piso mojado, agua con producto desinfectante y fruta descartada acumulada en el patio, que atrae moscas y roedores.")
build(
    O3, 1, F,
    use="Aprenderé qué es la post cosecha, por qué la cadena de frío y la higiene cuidan la calidad del fruto y del predio, y cuáles son los peligros del galpón de embalaje.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La post cosecha son las prácticas que se hacen después de cosechar para que el fruto llegue en buen estado al cliente: recibirlo, seleccionarlo, enfriarlo, embalarlo y almacenarlo. La cadena de frío es mantener el fruto a baja temperatura desde la cosecha hasta el cliente, porque el calor acelera su maduración y su pudrición. También hay prácticas dirigidas al predio: retirar los descartes, mantener limpio el galpón y manejar los residuos, para cuidar la sustentabilidad del predio y evitar plagas.",
        "El galpón tiene peligros. Una cámara de frío puede dejar atrapada a una persona; las cajas apiladas pueden caer; una transpaleta puede atropellar; el piso mojado hace resbalar; y los productos de desinfección pueden dañar la piel y los ojos. La jerarquía de controles ordena las medidas: eliminar el peligro, sustituirlo, cambiar el lugar o el equipo (ingeniería), dar reglas y capacitación (administrativo) y, al final, el equipo de protección personal (EPP).",
        f"Una puerta de cámara con apertura desde adentro es un control de ingeniería; una regla de no entrar solo es administrativa. Estas tareas las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("post cosecha", "prácticas que se hacen después de cosechar para conservar la calidad"), ("cadena de frío", "mantener el fruto a baja temperatura desde la cosecha hasta el cliente"), ("embalaje", "acondicionar el fruto en cajas para su transporte"), ("transpaleta", "carro para mover pallets"), ("pallet", "plataforma de madera sobre la que se apilan cajas"), ("descarte", "fruta que no sirve y se retira"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Cadena de frío", "Un fruto de ejemplo se deja varias horas al sol antes de entrar a la cámara. ¿Qué principio de la post cosecha se pierde?", ["El frío frena la maduración y la pudrición.", "Al dejarlo al sol se corta la cadena de frío."], "La cadena de frío"),
        ("Clasificar un control", "Un galpón de ejemplo coloca una baranda fija en el borde de la rampa de descarga. ¿Qué tipo de control es?", ["La baranda cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que la fruta puede esperar en el patio, porque «igual va a la cámara».", "El calor acelera su pudrición.", "La fruta entra a frío en el menor tiempo posible."),
              ("Creer que entrar a una cámara de frío «solo un momento» es seguro.", "La puerta puede cerrarse y el frío es peligroso.", "Se entra con autorización y con la manilla interior operativa.")],
    T=[
        ("abc", "En la post cosecha: ¿qué es la cadena de frío?", "Mantener el fruto a baja temperatura desde la cosecha hasta el cliente", "Guardar el fruto en una caja sin tapa", "Cosechar solo de noche", "La cadena de frío es mantener la baja temperatura, no un horario de cosecha."),
        ("abc", "En la post cosecha: ¿qué es un descarte?", "La fruta que no sirve y se retira", "La fruta de mejor calidad", "Una caja vacía", "El descarte es fruta que se retira de la línea."),
        ("abc", "En la post cosecha: ¿qué es un pallet?", "Una plataforma de madera sobre la que se apilan cajas", "Una cámara de frío", "Un producto para desinfectar", "El pallet es la plataforma donde se apilan cajas."),
        ("=", "{F} Un pallet de ejemplo lleva 48 cajas. ¿Cuántas cajas hay en 6 pallets?", "48*6", "Se multiplican las cajas de cada pallet por el número de pallets.", " cajas"),
        ("abc", "{F} Una manilla interior que abre la puerta de la cámara desde adentro es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien entra", "La manilla es una parte del equipo y funciona aunque nadie se acuerde de otra cosa."),
        ("abc", "{F} Una regla que dice «nadie entra solo a la cámara» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la cámara", "De sustitución, porque cambia el frío", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la fruta descartada acumulada en el patio?", "Que atraiga moscas y roedores que contaminen el predio", "La fruta misma en el suelo", "Que ocupe poco espacio", "El riesgo es la posibilidad de daño; la fruta acumulada es el peligro."),
        ("abc", "{F} Una estudiante dice: «puedo conducir la transpaleta entre las personas porque va lenta». ¿Qué respuesta es correcta?", "Es incorrecto: manejar equipos exige formación y autorización", "Es correcto, si usa casco", "Es correcto, si toca la bocina", "La velocidad o la bocina no reemplazan la autorización."),
        ("abc", "{F} En una visita, una persona queda encerrada en la cámara de frío. ¿Qué corresponde según las reglas generales?", "No quedarte en la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a buscarla sin avisar", "Cerrar la puerta para que no salga el frío", "Entrar sin formación puede dejar a otra persona atrapada."),
        ("abc", "En la post cosecha: ¿por qué el calor daña el fruto cosechado?", "Porque acelera su maduración y su pudrición", "Porque lo vuelve más duro", "Porque le quita el color", "El calor acelera los procesos de maduración y pudrición."),
        ("abc", "{F} Se propone solo entregar guantes para la desinfección del galpón. ¿Qué medida es más efectiva?", "Cambiar el producto por uno menos dañino y almacenarlo cerrado", "Entregar un segundo par de guantes", "Pedir que nadie lo toque", "Sustituir el producto actúa sobre el peligro."),
        ("=", "{F} El galpón recibe 2.400 cajas y las deja en pallets de 48 cajas. ¿Cuántos pallets se necesitan?", "2400//48", "Se dividen las cajas totales entre las cajas de cada pallet.", " pallets"),
        ("abc", "En la post cosecha: ¿por qué es importante retirar los descartes del predio?", "Para evitar plagas y contaminación", "Para que haya más espacio en el patio solamente", "Para que la fruta sea más grande", "Los descartes atraen plagas y deterioran la higiene del predio."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por manejar la transpaleta en su galpón «porque ya viste cómo se hace». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si va lenta", "Que sí, si el piso está seco", "Haber visto el concepto no habilita para operar equipos."),
    sc=[
        ("En la post cosecha: ¿qué se hace con la fruta cosechada para frenar su maduración?", "Se enfría rápidamente", "El frío frena la maduración y la pudrición."),
        ("En el galpón de embalaje: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En la post cosecha: ¿qué es el embalaje?", "Acondicionar el fruto en cajas para su transporte", "El embalaje prepara el fruto para el traslado."),
    ],
    op=("El «Huerto Demo 2» anota una tarea de ejemplo: guardar cajas de fruta en una cámara de frío cuya puerta solo abre desde afuera, con el piso mojado y a media tarde. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien encerrado.",
        "(a) Peligro: una puerta que no abre desde adentro; riesgo: que una persona quede encerrada en el frío y se dañe. (b) Una regla de no entrar solo y avisar siempre. (c) Una manilla interior que abra la puerta desde adentro. (d) No entro, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "avisa y no entra"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer entrar sin avisar", "proponer solo EPP"],
        "Pregunta: «¿qué control permite salir aunque nadie esté afuera?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe tres peligros de un galpón de embalaje de fruta y el riesgo de cada uno.",
    extend="Explica con un ejemplo por qué la cadena de frío se corta si la fruta espera al sol.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (registro de recepción de ejemplo, inventado). Lote L-05, cuartel 2 del «Huerto Demo». 480 cajas recibidas. Muestra de 50 frutas: 4 con golpes, 2 con pudrición y 44 sin defecto. "
     "Temperatura de recepción de la fruta: 18 grados; temperatura objetivo de la cámara de ejemplo: 2 grados. La cosecha terminó a las 10 horas y la fruta entró a la cámara a las 15 horas; tiempo máximo de ejemplo entre cosecha y cámara: 6 horas. Documentos: el registro de recepción, el registro de temperaturas y la guía de despacho.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de calidad del fruto (calibre, color, firmeza, defectos), trazabilidad por lote, y los documentos y roles de la post cosecha.",
    prior=["Sé qué es la post cosecha y la cadena de frío.", "Sé calcular porcentajes enteros.", "Sé restar enteros."],
    explain=[
        "La calidad de un fruto se evalúa con varios atributos: el calibre (tamaño), el color, la firmeza (qué tan duro está) y los defectos, como golpes o pudrición. La selección retira los frutos con defectos y la clasificación separa los buenos por calibre o calidad. Un lote es un grupo de fruta de igual cuartel y fecha de cosecha, y la trazabilidad permite saber de dónde viene cada caja.",
        "Los documentos guardan la evidencia: el registro de recepción anota cuántas cajas llegaron y cómo estaban; el registro de temperaturas muestra si se mantuvo el frío; la guía de despacho acompaña a la fruta cuando sale del predio. El jefe de packing organiza el trabajo, el controlador de calidad revisa muestras y el operario de línea ejecuta la selección. Un dato fuera de lo permitido se registra tal cual y se informa.",
        f"Una muestra es un grupo pequeño que representa al lote. El porcentaje de defectos de la muestra estima el del lote. {EMER} {AVISO}",
    ],
    vocab=[("calibre", "tamaño del fruto"), ("firmeza", "qué tan duro está el fruto"), ("selección", "retiro de los frutos con defectos"), ("clasificación", "separación de los frutos buenos por calibre o calidad"), ("lote", "grupo de fruta del mismo cuartel y día de cosecha"), ("registro de temperaturas", "documento con las temperaturas medidas"), ("guía de despacho", "documento que acompaña a la fruta al salir del predio")],
    worked=[
        ("Porcentaje de defectos", "En una muestra de ejemplo de 20 frutas hay 3 con defectos. ¿Qué porcentaje es?", ["3 de 20 equivale a 15 de 100.", "15 %."], "15 %"),
        ("Tiempo hasta el frío", "Una fruta de ejemplo se cosechó a las 9 y entró a la cámara a las 13. ¿Cuántas horas pasaron?", ["Se resta la hora de cosecha a la de entrada.", "13 menos 9."], "4 horas"),
    ],
    mistakes=[("Confundir selección con clasificación.", "La selección retira lo defectuoso; la clasificación separa lo bueno por categorías.", "Primero se selecciona y luego se clasifica."),
              ("Corregir una temperatura en el registro para que cumpla el objetivo.", "Un registro alterado oculta un problema.", "Se anota la temperatura real y se informa.")],
    T=[
        ("abc", "En la post cosecha: ¿qué es la firmeza de un fruto?", "Qué tan duro está el fruto", "El color del fruto", "El tamaño del fruto", "La firmeza mide la dureza del fruto."),
        ("abc", "En la post cosecha: ¿qué es la clasificación del fruto?", "La separación de los frutos buenos por calibre o calidad", "El retiro de los frutos con defectos", "El pesaje de las cajas", "La clasificación separa por categorías; retirar defectos es selección."),
        ("abc", "En la post cosecha: ¿para qué sirve la guía de despacho?", "Para acompañar a la fruta cuando sale del predio", "Para registrar la temperatura de la cámara", "Para medir la firmeza del fruto", "La guía de despacho acompaña el traslado."),
        ("=", "{F} ¿Cuántas frutas de la muestra no tienen defectos?", "50-4-2", "Se restan los frutos con golpes y con pudrición al total de la muestra.", " frutas"),
        ("=", "{F} ¿Qué porcentaje de la muestra tiene algún defecto?", "(4+2)*100//50", "Se suman los frutos con defectos y se calcula su porcentaje sobre la muestra.", " %"),
        ("=", "{F} ¿Cuántas horas pasaron entre el fin de la cosecha y la entrada a la cámara?", "15-10", "Se resta la hora de cosecha a la hora de entrada a la cámara.", " horas"),
        ("abc", "{F} ¿Se cumplió el tiempo máximo entre cosecha y cámara?", "Sí, porque pasaron 5 horas y el máximo es 6", "No, porque pasaron más de 6 horas", "No se puede saber sin medir la firmeza", "5 horas es menor que el máximo de 6."),
        ("abc", "{F} ¿Qué documento muestra si se mantuvo el frío durante el almacenamiento?", "El registro de temperaturas", "La guía de despacho", "El registro de recepción", "Las temperaturas se anotan en el registro de temperaturas."),
        ("=", "{F} ¿Cuántos grados de diferencia hay entre la temperatura de recepción y la temperatura objetivo de la cámara?", "18-2", "Se resta la temperatura objetivo a la temperatura de recepción.", " grados"),
        ("abc", "{F} Un operario dice: «la muestra tiene 12 % de defectos, así que todo el lote está perfecto». ¿Qué respuesta es correcta?", "Es incorrecto: 12 % indica que hay defectos que se retiran y la muestra solo estima el lote", "Es correcto, porque 12 es bajo", "Es correcto, si la muestra es pequeña", "La muestra estima el lote y los defectos deben retirarse."),
        ("abc", "{F} El controlador de calidad quiere anotar 2 grados en la temperatura de recepción en vez de 18, «para que cumpla». ¿Qué corresponde?", "Rechazarlo: se anota la temperatura real y se informa", "Aceptarlo, porque el objetivo es lo importante", "Aceptarlo, si el lote ya está en la cámara", "Alterar el dato oculta el problema."),
        ("abc", "{F} Una persona se resbala en el piso mojado junto a la línea de embalaje y no se levanta. ¿Qué corresponde?", "No moverla, avisar a un adulto responsable y a emergencias", "Levantarla rápido", "Esperar a ver si se levanta sola", "Moverla puede agravar una lesión que no se ve a simple vista."),
        ("abc", "En la post cosecha: ¿por qué es importante la trazabilidad por lote?", "Porque permite saber de dónde viene cada caja si hay un problema", "Porque aumenta el calibre", "Porque reemplaza la selección", "La trazabilidad ayuda a encontrar el origen de un problema."),
    ],
    ctx=("abc", "Un conocido te pide que firmes como «controlador de calidad» un registro de fruta que no revisaste. ¿Qué respondes?", "Que no, porque firmar sin revisar falsea el registro, y que lo consultarás con un adulto responsable", "Que sí, si confías en él", "Que sí, solo esta vez", "Una firma certifica una revisión que debe haber ocurrido."),
    sc=[
        ("En la post cosecha: ¿cómo se calcula el porcentaje de defectos de una muestra?", "Frutas con defecto entre frutas de la muestra, por 100", "El porcentaje relaciona los defectos con el tamaño de la muestra."),
        ("En el galpón de embalaje: ¿qué documento anota cuántas cajas llegaron y su estado?", "El registro de recepción", "El registro de recepción guarda lo que llegó."),
        ("En la post cosecha: ¿qué rol revisa muestras de calidad?", "El controlador de calidad", "El controlador de calidad revisa la fruta con criterios definidos."),
    ],
    op=("Registro de ejemplo del «Huerto Demo 3»: lote L-11, 600 cajas; muestra de 40 frutas con 3 golpeadas y 1 podrida; cosecha terminada a las 9 horas y fruta ingresada a la cámara a las 17 horas; máximo de ejemplo de 6 horas. Escribe (a) el porcentaje de defectos de la muestra, (b) las horas entre cosecha y cámara, (c) si cumple el máximo, (d) qué haces con el dato que no cumple.",
        "(a) (3 + 1) × 100 ÷ 40 = 10 %. (b) 17 − 9 = 8 horas. (c) No cumple, porque 8 es mayor que 6. (d) Se anota el dato real y se informa al jefe de packing y al asesor.",
        ["calcula el porcentaje de defectos", "calcula las horas", "concluye sobre el máximo", "no altera el dato"],
        ["hoja con las cuatro respuestas"],
        ["no sumar golpes y pudrición", "cambiar la hora de entrada"],
        "Pregunta: «¿cuántas frutas tienen algún defecto?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el porcentaje de defectos de una muestra inventada de 25 frutas con 2 golpeadas.",
    extend="Explica con un ejemplo por qué una muestra permite estimar el estado de un lote.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Lote L-09 del «Huerto Demo»: 20 % de la fruta llegó con golpes. Observaciones anotadas: las cajas se llenaron por sobre el borde y se apilaron altas; la fruta se descargó dejándola caer desde la caja; el camino del cuartel tiene baches; la fruta llegó a 20 grados y esperó 7 horas antes de entrar a la cámara; "
     "los descartes se dejaron sin cubrir junto al galpón. Máximo de ejemplo entre cosecha y cámara: 6 horas.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de pérdidas en post cosecha, a relacionar cada observación con una causa y a decidir qué prácticas del fruto y del predio corregir.",
    prior=["Sé qué es la cadena de frío.", "Sé calcular porcentajes enteros.", "Sé leer una ficha con datos."],
    explain=[
        "Para analizar un caso de pérdidas se listan las observaciones y se relaciona cada una con su efecto. Las cajas sobrellenadas aplastan la fruta de abajo; dejar caer la fruta causa golpes; los caminos con baches hacen vibrar y golpear; la espera larga y tibia acelera la pudrición y rompe la cadena de frío; y los descartes sin cubrir atraen plagas y deterioran el predio.",
        "Las causas se ordenan por su efecto y se proponen correcciones conceptuales: respetar el llenado de las cajas, manipular con cuidado, mejorar el camino, enfriar dentro del tiempo máximo y retirar o cubrir los descartes. Una causa no se afirma sin evidencia; si hay duda, se registra y se consulta al asesor. Cada corrección tiene responsable y plazo, y se verifica después con datos.",
        f"Los cambios de procedimiento los define el jefe de packing con el asesor. El trabajo en terreno lo hace personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("causa", "hecho que produce un efecto o problema"), ("efecto", "resultado de una causa"), ("sobrellenado", "llenar la caja por sobre su borde"), ("corrección", "medida que arregla una causa"), ("responsable", "persona a cargo de una corrección"), ("verificar", "comprobar con datos que la corrección funcionó")],
    worked=[
        ("Causa y efecto", "En un galpón de ejemplo se apilan cajas muy altas sobre fruta blanda. ¿Qué efecto es probable?", ["El peso aplasta las cajas de abajo.", "La fruta de abajo se golpea o se aplasta."], "Fruta aplastada en las cajas de abajo"),
        ("Plazo máximo", "Un máximo de ejemplo es 6 horas y una fruta esperó 9. ¿Cuántas horas excedió?", ["Se resta el máximo al tiempo real.", "9 menos 6."], "3 horas"),
    ],
    mistakes=[("Culpar solo al camino sin revisar las otras causas.", "Varias causas pueden sumarse.", "Se listan todas las observaciones y su efecto."),
              ("Dejar los descartes sin cubrir porque «se retiran mañana».", "Atraen plagas y deterioran el predio.", "Se retiran o se cubren el mismo día.")],
    T=[
        ("abc", "En la post cosecha: ¿qué es una causa?", "El hecho que produce un efecto o problema", "El resultado final del problema", "La persona a cargo de una corrección", "La causa produce el efecto; la corrección tiene un responsable."),
        ("abc", "En la post cosecha: ¿qué es verificar una corrección?", "Comprobar con datos que funcionó", "Anotar que se hizo sin revisar", "Repetir el mismo error", "Verificar compara datos antes y después."),
        ("abc", "En la post cosecha: ¿qué es el sobrellenado de una caja?", "Llenarla por sobre su borde", "Dejarla a medias", "Cerrarla con cinta", "El sobrellenado hace que las cajas se aplasten al apilarse."),
        ("abc", "{F} ¿Qué efecto tiene dejar caer la fruta desde la caja?", "Golpes en la fruta", "Mayor calibre", "Menor temperatura", "La caída desde la caja golpea la fruta y la daña."),
        ("abc", "{F} ¿Qué efecto tiene que la fruta espere 7 horas tibia antes de entrar a la cámara?", "Se corta la cadena de frío y se acelera la pudrición", "La fruta se enfría antes", "La fruta aumenta de calibre", "La espera excede el máximo de ejemplo de 6 horas."),
        ("abc", "{F} ¿Qué observación de la ficha puede dañar la fruta durante el traslado del cuartel?", "El camino con baches", "Los descartes sin cubrir", "La fruta a 20 grados", "El camino con baches hace vibrar y golpear la fruta."),
        ("abc", "{F} ¿Qué problema generan los descartes sin cubrir junto al galpón?", "Atraen plagas y deterioran el predio", "Mejoran la cadena de frío", "Suben el calibre", "Los descartes sin cubrir son un foco de plagas."),
        ("=", "{F} ¿Cuántas horas excedió la espera el máximo de ejemplo?", "7-6", "Se resta el máximo permitido al tiempo real de espera.", " hora"),
        ("=", "{F} Si el lote tenía 800 cajas, ¿cuántas cajas se vieron afectadas por golpes?", "800*20//100", "Se calcula el porcentaje de golpes sobre el total de cajas.", " cajas"),
        ("abc", "{F} Una compañera dice: «la única causa es el camino, así que arreglándolo se soluciona todo». ¿Qué respuesta es correcta?", "Es incompleto: hay otras causas, como el sobrellenado, la caída de la fruta y la espera", "Es correcto, porque el camino siempre manda", "Es correcto, si hay baches", "La ficha lista varias causas que se suman."),
        ("abc", "{F} El jefe de packing pide arreglar el camino con una máquina, y una estudiante quiere ayudar conduciéndola. ¿Qué corresponde?", "Rechazarlo: la maquinaria la opera personal capacitado y autorizado", "Aceptarlo, si la máquina es lenta", "Aceptarlo, si es de día", "Operar maquinaria exige formación y autorización."),
        ("abc", "{F} Para corregir la espera tibia, ¿qué medida conceptual conviene analizar?", "Organizar el traslado para que la fruta entre al frío dentro del máximo", "Aumentar el tiempo de espera", "Quitar el registro de temperaturas", "Cumplir el plazo máximo protege la cadena de frío."),
        ("abc", "En la post cosecha: ¿por qué toda corrección debe tener responsable y plazo?", "Para que alguien la ejecute y se pueda verificar a tiempo", "Para que no se pueda medir", "Para evitar escribir el análisis", "Sin responsable y plazo la corrección se olvida."),
    ],
    ctx=("abc", "Un conocido te cuenta que pierde 20 % de su fruta por golpes y te pide que le digas la causa sin ver su galpón. ¿Qué respondes?", "Que hay que observar el proceso y listar las causas posibles con un asesor", "Que es el camino", "Que es la caja", "Sin observar el proceso solo se pueden formular hipótesis."),
    sc=[
        ("En la post cosecha: ¿qué efecto tiene apilar cajas muy altas sobre fruta blanda?", "Aplasta la fruta de abajo", "El peso aplasta las cajas inferiores."),
        ("En el galpón de embalaje: ¿qué se hace con los descartes?", "Se retiran o se cubren el mismo día", "Los descartes sin cubrir atraen plagas."),
        ("En la post cosecha: ¿cómo se verifica que una corrección funcionó?", "Comparando datos antes y después", "La verificación usa datos medibles de antes y después."),
    ],
    op=("Caso de ejemplo del «Huerto Demo 4»: lote L-14 de 500 cajas; 16 % de la fruta con golpes; cajas sobrellenadas; fruta que espera 8 horas antes del frío (máximo de ejemplo 6); descartes en bolsas abiertas junto a la puerta. Escribe (a) cuántas cajas se afectaron, (b) cuántas horas excede la espera, (c) dos causas del caso, (d) una corrección conceptual y quién decide.",
        "(a) 500 × 16 ÷ 100 = 80 cajas. (b) 8 − 6 = 2 horas. (c) Cajas sobrellenadas y espera excesiva antes del frío. (d) Respetar el llenado de las cajas y enfriar dentro de 6 horas; decide el jefe de packing con el asesor.",
        ["calcula las cajas", "calcula el exceso de espera", "cita dos causas", "propone una corrección y quién decide"],
        ["hoja con las cuatro respuestas"],
        ["dividir mal el porcentaje", "citar una causa sin evidencia"],
        "Pregunta: «¿cuántas cajas son el 16 % de 500?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe tres causas posibles de golpes en fruta y una corrección conceptual para cada una.",
    extend="Explica con un ejemplo por qué el cuidado del predio también es parte de la post cosecha.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Huerto Demo» recibió 1.200 cajas de fruta. Clasificación de ejemplo: 40 % categoría extra a $12.000 por caja; 45 % categoría primera a $9.000 por caja; 10 % categoría segunda a $4.000 por caja; 5 % descarte sin valor. "
     "Costo de ejemplo de la post cosecha: $4.000.000 por todas las cajas.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular cajas por categoría, ingreso y margen de la post cosecha, y la merma del lote.",
    prior=["Sé qué es la clasificación y el descarte.", "Sé calcular porcentajes enteros.", "Sé multiplicar y sumar enteros."],
    explain=[
        "Después de clasificar, cada categoría tiene un precio distinto: la fruta de mayor calidad se vende más cara. Para calcular, se obtiene el número de cajas de cada categoría aplicando su porcentaje al total, se multiplica por el precio de cada caja y se suman los ingresos. La merma es la parte del producto que se pierde, como el descarte; su porcentaje se obtiene dividiendo las cajas perdidas entre el total y multiplicando por 100.",
        "El margen es el ingreso total menos el costo de la post cosecha. Conocer la merma ayuda a decidir dónde mejorar: una merma alta pide revisar las causas. También se compara el ingreso por caja recibida, que es el ingreso total dividido entre las cajas totales. Los valores son de ejemplo y las decisiones las toma el asesor.",
        f"Los números no reemplazan el cuidado de la calidad ni la seguridad en el trabajo. {EMER} {AVISO}",
    ],
    vocab=[("categoría", "grupo de calidad en que se clasifica la fruta"), ("merma", "parte del producto que se pierde"), ("ingreso por caja recibida", "ingreso total entre las cajas totales"), ("costo de post cosecha", "gasto total de recibir, seleccionar y guardar la fruta"), ("margen", "ingreso menos costo")],
    worked=[
        ("Cajas por categoría", "Un lote de ejemplo de 200 cajas tiene 30 % en categoría primera. ¿Cuántas cajas son?", ["Se calcula el 30 % de 200.", "30 por 200 entre 100 es 60."], "60 cajas"),
        ("Ingreso de una categoría", "Esas 60 cajas se venden a $8.000 cada una. ¿Cuál es el ingreso?", ["Se multiplican las cajas por el precio.", "60 por 8.000."], "$480.000"),
    ],
    mistakes=[("Calcular el ingreso con el precio de la mejor categoría para todas las cajas.", "Cada categoría tiene su precio.", "Se calcula categoría por categoría y se suma."),
              ("Contar el descarte como parte del ingreso.", "El descarte no tiene valor.", "El descarte se cuenta como merma.")],
    T=[
        ("abc", "En la post cosecha: ¿qué es la merma?", "La parte del producto que se pierde", "El ingreso por caja", "El precio de la categoría extra", "La merma es lo que se pierde."),
        ("abc", "En la post cosecha: ¿por qué se calcula el ingreso por categoría?", "Porque cada categoría tiene un precio distinto", "Porque las cajas pesan distinto", "Porque el costo cambia por caja", "Los precios dependen de la calidad."),
        ("abc", "En la post cosecha: ¿cómo se calcula el margen?", "Ingreso total menos costo de post cosecha", "Ingreso total más costo", "Cajas por precio de la peor categoría", "El margen resta el costo del ingreso."),
        ("=", "{F} ¿Cuántas cajas de categoría extra hay?", "1200*40//100", "Se calcula el porcentaje de la categoría sobre el total de cajas.", " cajas"),
        ("=", "{F} ¿Cuántas cajas de categoría primera hay?", "1200*45//100", "Se calcula el porcentaje de la categoría sobre el total de cajas.", " cajas"),
        ("=", "{F} ¿Cuántas cajas de categoría segunda hay?", "1200*10//100", "Se calcula el porcentaje de la categoría sobre el total de cajas.", " cajas"),
        ("=", "{F} ¿Cuántas cajas son descarte (merma)?", "1200*5//100", "Se calcula el porcentaje de descarte sobre el total.", " cajas"),
        ("=", "{F} ¿Cuál es el ingreso de la categoría extra?", "1200*40//100*12000", "Se multiplican las cajas de la categoría por su precio.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso total de las tres categorías con valor?", "1200*40//100*12000+1200*45//100*9000+1200*10//100*4000", "Se suman los ingresos de las tres categorías.", " pesos"),
        ("=", "{F} ¿Cuál es el margen de la post cosecha?", "1200*40//100*12000+1200*45//100*9000+1200*10//100*4000-4000000", "Se resta el costo de post cosecha al ingreso total.", " pesos"),
        ("abc", "{F} Un encargado dice que las 60 cajas de descarte deben contarse como ingreso «porque algo se venderá». ¿Cuál es el error?", "El descarte no tiene valor y se cuenta como merma", "Ninguno, porque toda caja vale", "El error es dividir entre 100", "La ficha asigna valor cero al descarte."),
        ("abc", "{F} El encargado quiere mover cajas pesadas con una transpaleta sin formación para terminar antes. ¿Qué corresponde?", "Rechazarlo: la transpaleta la opera personal capacitado y autorizado", "Aceptarlo, si va lenta", "Aceptarlo, si es la última caja", "Operar equipos exige formación y autorización."),
        ("abc", "En la post cosecha: ¿por qué una merma alta pide revisar las causas?", "Porque indica pérdidas que se pueden evitar con mejores prácticas", "Porque la merma sube el precio", "Porque la merma es siempre normal", "Una merma alta puede reducirse con mejores prácticas."),
    ],
    ctx=("abc", "Un conocido te pregunta si su post cosecha «es rentable» y te da solo el costo. ¿Qué respondes?", "Que faltan los ingresos por categoría y la merma, y que lo evalúa un asesor", "Que sí, siempre", "Que no, nunca", "Sin ingresos no se puede calcular un margen."),
    sc=[
        ("En la post cosecha: ¿cómo se calcula el número de cajas de una categoría?", "Aplicando su porcentaje al total de cajas", "El porcentaje de la categoría se aplica al total."),
        ("En el galpón de embalaje: ¿qué valor tiene el descarte?", "Ninguno: se cuenta como merma", "El descarte no se vende y por eso no genera ingreso."),
        ("En la post cosecha: ¿qué se resta al ingreso para obtener el margen?", "El costo de la post cosecha", "El margen es lo que queda tras pagar los costos."),
    ],
    op=("Datos de ejemplo del «Huerto Demo 5»: 500 cajas; 50 % categoría extra a $10.000 por caja; 40 % primera a $6.000 por caja; 10 % descarte; costo de post cosecha $2.000.000. Escribe (a) las cajas de cada categoría y el descarte, (b) el ingreso total, (c) el margen, (d) qué haces si el porcentaje de descarte sube a 20 %.",
        "(a) Extra: 250; primera: 200; descarte: 50. (b) 250 × 10.000 + 200 × 6.000 = 2.500.000 + 1.200.000 = $3.700.000. (c) 3.700.000 − 2.000.000 = $1.700.000. (d) Reviso las causas de la merma con el jefe de packing y el asesor.",
        ["calcula las cajas por categoría", "calcula el ingreso", "calcula el margen", "reacciona a una merma alta"],
        ["hoja con las cuatro respuestas"],
        ["usar el mismo precio para todo", "contar el descarte como ingreso"],
        "Pregunta: «¿cuántas cajas es el 50 % de 500?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el ingreso de 80 cajas de categoría primera a $7.000 por caja.",
    extend="Explica con un ejemplo por qué una merma baja mejora el margen.",
)

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Fundo Demo 3» guarda granos de trigo en un silo, papas en una bodega ventilada y hortalizas frescas en una cámara. "
     "Peligros anotados: el silo (el grano puede atrapar a una persona y el polvo puede arder), sacos de 50 kg que se levantan a mano, pallets apilados altos, una transpaleta, roedores que se combaten con productos y humedad que produce hongos.")
build(
    O4, 1, F,
    use="Aprenderé qué son el acopio, la clasificación y la guarda de productos agrícolas, y cuáles son los peligros de un silo, una bodega y una cámara.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El acopio es reunir los productos cosechados en un lugar, como un silo, una bodega o una cámara. La clasificación es separarlos según su calidad o su destino. La guarda es conservarlos en condiciones que cuiden su calidad hasta venderlos. Cada producto tiene características fisiológicas propias: los granos son semillas secas que se guardan por meses; las papas respiran y se guardan semanas o meses; las hortalizas frescas duran pocos días.",
        "Los lugares de guarda tienen peligros. En un silo, el grano puede hundir a quien está encima, y su polvo puede incendiarse; por eso no se entra a un silo. Los sacos pesados dañan la espalda; los pallets altos pueden caer; la transpaleta puede atropellar; los productos contra roedores pueden intoxicar; y la humedad produce hongos que dañan el producto. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar, reglas y, al final, EPP.",
        f"Un silo es un espacio cerrado: no se entra. Las tareas de acopio con equipos las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("acopio", "reunir los productos cosechados en un lugar"), ("clasificación", "separar los productos según su calidad o destino"), ("guarda", "conservar los productos hasta venderlos"), ("silo", "estructura cerrada donde se guardan granos"), ("espacio cerrado", "lugar con poca ventilación donde puede faltar aire"), ("hongo", "microorganismo que daña los productos húmedos"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Elegir el plazo", "Un producto de ejemplo dura solo 3 días. ¿Corresponde a guarda de corto, mediano o largo plazo?", ["Tres días es muy poco tiempo.", "Es guarda de corto plazo."], "Corto plazo"),
        ("Clasificar un control", "Un fundo de ejemplo instala una ventilación fija en la bodega de papas para reducir la humedad. ¿Qué tipo de control es?", ["La ventilación fija cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que entrar al silo a empujar el grano es seguro si se hace rápido.", "El grano puede hundir a la persona en segundos.", "Nadie entra al silo: lo hace personal autorizado con equipos."),
              ("Creer que levantar sacos de 50 kg es seguro «con buena postura».", "El peso excesivo daña la espalda.", "Se usan equipos y se reparte la carga, según la norma vigente.")],
    T=[
        ("abc", "En el acopio: ¿qué es la guarda de un producto?", "Conservarlo en condiciones que cuiden su calidad hasta venderlo", "Separarlo según su calidad", "Reunirlo en un lugar", "La guarda conserva el producto; separar es clasificar y reunir es acopio."),
        ("abc", "En el acopio: ¿qué es un silo?", "Una estructura cerrada donde se guardan granos", "Una cámara con frío para frutas", "Un carro para mover pallets", "El silo es una estructura cerrada para granos."),
        ("abc", "En el acopio: ¿qué es la clasificación de un producto?", "Separarlo según su calidad o destino", "Conservarlo hasta venderlo", "Pesarlo en una balanza", "La clasificación separa por calidad o destino."),
        ("=", "{F} Un saco de ejemplo pesa 50 kg. ¿Cuántos kilos pesan 24 sacos?", "50*24", "Se multiplican los kilos de cada saco por el número de sacos.", " kg"),
        ("abc", "{F} Una reja con candado en la entrada al silo es un control de tipo:", "De ingeniería, porque cambia físicamente el acceso", "Administrativo, porque es una regla", "De EPP, porque protege a quien entra", "La reja es una estructura física que limita el acceso."),
        ("abc", "{F} Una regla que dice «nadie entra al silo sin autorización» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el silo", "De eliminación, porque quita el silo", "Una regla escrita es un control de tipo administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a entrar al silo?", "Que el grano hunda a la persona o falte aire", "El grano mismo", "Que el silo esté vacío", "El riesgo es el daño posible; el grano es el peligro."),
        ("abc", "{F} Una estudiante dice: «puedo entrar al silo a empujar el grano si lo hago rápido». ¿Qué respuesta es correcta?", "Es peligroso: nadie entra al silo, lo hace personal autorizado", "Es correcto, si lleva casco", "Es correcto, si hay otra persona afuera", "El grano puede hundir a la persona en segundos."),
        ("abc", "{F} Una persona queda hundida en el grano de un silo. ¿Qué corresponde según las reglas generales?", "No entrar, avisar a un adulto responsable y a emergencias", "Entrar a sacarla tirando de los brazos", "Mover el grano con una pala", "Entrar puede hundir a otra persona; se avisa a quienes tienen el equipo."),
        ("abc", "En el acopio: ¿por qué la humedad es un problema para la guarda?", "Porque favorece hongos que dañan el producto", "Porque hace más liviano el producto", "Porque evita las plagas", "La humedad favorece hongos que dañan el producto guardado."),
        ("abc", "{F} Se propone solo entregar fajas lumbares para levantar sacos pesados. ¿Qué medida es más efectiva?", "Usar equipos para mover la carga y reducir el peso por saco", "Entregar más fajas", "Pedir que levanten más rápido", "Reducir el esfuerzo manual actúa sobre el peligro."),
        ("=", "{F} Una bodega admite pallets de 24 sacos. ¿Cuántos sacos hay en 8 pallets?", "24*8", "Se multiplican los sacos de cada pallet por el número de pallets.", " sacos"),
        ("abc", "En el acopio: ¿por qué los productos contra roedores deben guardarse cerrados y rotulados?", "Para evitar que se confundan o intoxiquen a personas", "Para que ocupen menos espacio", "Para que sean más baratos", "Un producto tóxico guardado sin control puede dañar."),
    ],
    ctx=("abc", "Un conocido te pide que entres a su silo a «aflojar» el grano porque eres delgado. ¿Qué respondes?", "Que no, porque el silo es un espacio cerrado y peligroso, y que lo consultarás con un adulto responsable", "Que sí, con una cuerda", "Que sí, si es rápido", "Nadie sin formación y equipos entra a un silo."),
    sc=[
        ("En el acopio: ¿qué es el acopio?", "Reunir los productos cosechados en un lugar", "El acopio es la reunión de productos en un lugar."),
        ("En la bodega de granos: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En el acopio: ¿se entra a un silo?", "No, es un espacio cerrado peligroso", "El grano puede hundir y puede faltar aire."),
    ],
    op=("El «Fundo Demo 4» anota una tarea de ejemplo: subir al grano de un silo para nivelarlo con una pala, solo, un día de calor. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien hundido en el grano.",
        "(a) Peligro: grano que puede hundir a la persona; riesgo: que quede atrapada y se asfixie. (b) Una regla de no entrar al silo sin autorización. (c) Una reja con candado y un sistema para nivelar el grano desde afuera. (d) No entro, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no entra y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer entrar a rescatar", "proponer solo EPP"],
        "Pregunta: «¿qué control impide entrar aunque alguien se olvide de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres productos agrícolas inventados y di si su guarda sería de corto, mediano o largo plazo.",
    extend="Explica con un ejemplo por qué un silo es un espacio cerrado.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Bodega del «Fundo Demo 3». Lote T-1: trigo, humedad 12 %, ingresó el día 5. Lote T-2: trigo, humedad 16 %, ingresó el día 8. Lote P-1: papas, ingresó el día 10. "
     "Humedad máxima de ejemplo para guardar trigo a largo plazo: 14 %. Documentos: el registro de ingreso y salida (kárdex), la ficha del lote y el registro de condiciones (temperatura y humedad de la bodega). Regla de salida: primero sale lo que primero entró (FIFO).")
build(
    O4, 2, F,
    use="Aprenderé los conceptos de humedad del grano, plazo de guarda, FIFO y plagas de bodega, y los documentos y roles del acopio.",
    prior=["Sé qué es el acopio, la clasificación y la guarda.", "Sé calcular restas con enteros.", "Sé leer una ficha de datos."],
    explain=[
        "La humedad del grano es el porcentaje de agua que contiene. Un grano muy húmedo se calienta, desarrolla hongos y se echa a perder; por eso para guardarlo mucho tiempo debe estar bajo un máximo. FIFO (primero entra, primero sale) es la regla de salida: sale primero el lote más antiguo, para que ningún producto se quede guardado demasiado tiempo. Las plagas de bodega son insectos y roedores que dañan el producto; se previenen con orden, limpieza y vigilancia.",
        "Los plazos de guarda son de corto plazo (días, para hortalizas frescas), mediano plazo (semanas o meses, como las papas) y largo plazo (meses, como los granos secos). Los documentos son el kárdex, que anota cada ingreso y salida; la ficha del lote, que identifica el producto; y el registro de condiciones, que anota la temperatura y la humedad de la bodega. El bodeguero ejecuta, el jefe de bodega supervisa y el controlador de calidad revisa.",
        f"Un registro de bodega no se altera para que una humedad «cumpla». {EMER} {AVISO}",
    ],
    vocab=[("humedad del grano", "porcentaje de agua que contiene el grano"), ("FIFO", "regla de salida: primero entra, primero sale"), ("kárdex", "registro de cada ingreso y salida de una bodega"), ("plaga de bodega", "insecto o roedor que daña los productos guardados"), ("corto plazo", "guarda de días"), ("largo plazo", "guarda de meses")],
    worked=[
        ("Aplicar FIFO", "Un lote A de ejemplo entró el día 3 y un lote B entró el día 9. ¿Cuál sale primero según FIFO?", ["FIFO saca primero lo más antiguo.", "El lote A entró antes."], "El lote A"),
        ("Comparar con el máximo", "Un grano de ejemplo tiene 15 % de humedad y el máximo es 13 %. ¿Cuántos puntos supera el máximo?", ["Se resta el máximo a la humedad.", "15 menos 13."], "2 puntos"),
    ],
    mistakes=[("Sacar primero el lote que está más cerca de la puerta, aunque sea el más nuevo.", "Rompe el FIFO y deja productos viejos.", "Se saca el más antiguo, aunque cueste más moverlo."),
              ("Mezclar un lote húmedo con uno seco para «bajar» la humedad promedio.", "El grano húmedo puede contaminar al seco.", "Cada lote se guarda por separado y se informa su humedad real.")],
    T=[
        ("abc", "En el acopio: ¿qué es la humedad del grano?", "El porcentaje de agua que contiene", "El peso de cada saco", "La temperatura de la bodega", "La humedad del grano mide el agua que contiene."),
        ("abc", "En el acopio: ¿qué significa FIFO?", "Primero entra, primero sale", "Primero entra, último sale", "Solo sale lo más barato", "FIFO saca primero lo más antiguo."),
        ("abc", "En el acopio: ¿qué es el kárdex?", "El registro de cada ingreso y salida de la bodega", "El registro de la humedad del grano", "El plano de la bodega", "El kárdex anota los movimientos de ingreso y de salida."),
        ("abc", "{F} ¿Cuál lote de trigo puede guardarse a largo plazo según el máximo de ejemplo?", "T-1, con 12 % de humedad", "T-2, con 16 % de humedad", "Ambos", "T-1 está bajo el máximo de 14 % y T-2 lo supera."),
        ("=", "{F} ¿Cuántos puntos de humedad supera el lote T-2 el máximo de ejemplo?", "16-14", "Se resta el máximo a la humedad del lote.", " puntos"),
        ("abc", "{F} Entre T-1 y T-2, ¿cuál sale primero según FIFO?", "T-1, porque entró el día 5", "T-2, porque entró el día 8", "P-1, porque entró el día 10", "T-1 entró antes que T-2, así que sale primero."),
        ("abc", "{F} ¿Qué documento anota cada ingreso y salida de lotes?", "El kárdex", "El registro de condiciones", "La ficha del lote", "El kárdex registra los movimientos de entrada y de salida."),
        ("abc", "{F} ¿Qué rol supervisa el funcionamiento de la bodega?", "El jefe de bodega", "El operador de la transpaleta", "El comprador del trigo", "El jefe de bodega supervisa el funcionamiento de la bodega."),
        ("abc", "{F} Una compañera dice: «mezclemos T-1 con T-2 para que el promedio dé 14 %». ¿Qué respuesta es correcta?", "Es incorrecto: el grano húmedo puede contaminar al seco", "Es correcto, porque el promedio cumple", "Es correcto, si se mezcla bien", "Mezclar daña el lote de menor humedad."),
        ("=", "{F} Si se mezclaran 100 sacos de T-1 con 100 de T-2, ¿cuál sería el promedio de humedad de la mezcla, en puntos?", "(12+16)//2", "Se suman las dos humedades y se divide entre 2.", " %"),
        ("abc", "{F} El bodeguero anota una humedad de 14 % para T-2 en vez de 16 %, «para que cumpla». ¿Qué corresponde?", "Rechazarlo: se anota la humedad real y se informa", "Aceptarlo, si el lote está seco", "Aceptarlo, porque el máximo es 14 %", "Alterar el dato oculta el problema."),
        ("abc", "{F} Una persona se resbala en la bodega y no se mueve. ¿Qué corresponde?", "No moverla, avisar a un adulto responsable y a emergencias", "Levantarla rápido", "Esperar a que despierte", "Moverla puede agravar una lesión que no se ve a simple vista."),
        ("abc", "En el acopio: ¿por qué las papas se guardan a mediano plazo y las hortalizas frescas a corto plazo?", "Porque cada producto tiene una duración distinta", "Porque las hortalizas cuestan más", "Porque las papas son más livianas", "Cada producto tiene su fisiología y su duración."),
    ],
    ctx=("abc", "Un conocido te pide que le «ajustes» la humedad del lote en el registro para que se compre su trigo. ¿Qué respondes?", "Que no, porque se anota el dato real, y que lo consultarás con un adulto responsable", "Que sí, un poco", "Que sí, si el comprador no pregunta", "Alterar el dato engaña al comprador."),
    sc=[
        ("En el acopio: ¿qué lote sale primero con FIFO?", "El más antiguo", "FIFO saca primero el producto que lleva más tiempo guardado."),
        ("En la bodega de granos: ¿qué se hace con un lote por sobre el máximo de humedad?", "Se guarda por separado y se informa", "El lote húmedo puede contaminar al seco."),
        ("En el acopio: ¿qué documento anota los movimientos?", "El kárdex", "El kárdex guarda ingresos y salidas."),
    ],
    op=("Registro de ejemplo del «Fundo Demo 5»: lote M-1, maíz, humedad 13 %, ingresó el día 2; lote M-2, maíz, humedad 17 %, ingresó el día 6; máximo de ejemplo para guarda larga: 14 %. Escribe (a) qué lote puede guardarse a largo plazo, (b) cuántos puntos supera el máximo el otro lote, (c) cuál sale primero según FIFO, (d) qué haces si ves un registro con la humedad cambiada.",
        "(a) M-1. (b) 17 − 14 = 3 puntos. (c) M-1, porque entró primero. (d) No lo corrijo yo: lo informo al jefe de bodega.",
        ["elige el lote correcto", "calcula la diferencia", "aplica FIFO", "informa el cambio"],
        ["hoja con las cuatro respuestas"],
        ["mezclar los lotes", "no aplicar FIFO", "corregir el registro sin avisar"],
        "Pregunta: «¿qué lote tiene humedad bajo el máximo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Aplica FIFO a tres lotes inventados que entraron los días 4, 1 y 7 y escribe el orden de salida.",
    extend="Explica con un ejemplo por qué un lote húmedo puede dañar a uno seco.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Tres lotes del «Fundo Demo 3» con destinos distintos. Lote H: tomates frescos para vender en 3 días, con algunos frutos golpeados. "
     "Lote P: papas para vender en 2 meses, con tierra y sin daños. Lote G: trigo con 11 % de humedad para vender en 8 meses. Condiciones de ejemplo: cámara fría (para corto plazo), bodega ventilada (para mediano plazo) y silo seco (para largo plazo).")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de lotes con destinos distintos y a decidir con dos evidencias dónde se clasifica y se guarda cada uno según su fisiología y su plazo.",
    prior=["Sé qué son corto, mediano y largo plazo.", "Sé qué es FIFO y la humedad del grano.", "Sé leer una ficha con datos."],
    explain=[
        "Para decidir dónde guardar un lote se cruzan tres datos: el producto y su fisiología, el plazo hasta la venta y el estado del lote. Las hortalizas frescas respiran mucho y se echan a perder en pocos días: se guardan en frío y se venden pronto. Las papas respiran menos y se guardan semanas o meses en un lugar fresco y ventilado. Los granos secos respiran muy poco y se guardan meses si están bajo el máximo de humedad.",
        "La clasificación separa los productos dañados de los sanos: los golpeados se retiran o se venden primero, porque se echan a perder antes. Un buen análisis nombra el lote, su plazo, su evidencia y su lugar de guarda, y dice qué cambiaría si cambiara el plazo. La decisión final la toma el jefe de bodega con el asesor.",
        f"Mover productos con equipos, entrar a un silo o a una cámara no es una tarea para quien analiza en papel. {EMER} {AVISO}",
    ],
    vocab=[("fisiología del producto", "cómo funciona el producto después de cosechado, por ejemplo cuánto respira"), ("respiración", "proceso por el que el producto gasta sus reservas y se deteriora"), ("corto plazo", "días"), ("mediano plazo", "semanas o meses"), ("largo plazo", "meses"), ("daño mecánico", "daño por golpes o aplastamiento")],
    worked=[
        ("Elegir el lugar", "Un producto de ejemplo dura solo 2 días y se vende mañana. ¿Dónde conviene guardarlo?", ["Es de corto plazo.", "Corresponde la cámara fría."], "En la cámara fría"),
        ("Producto dañado", "En un lote de ejemplo hay frutos golpeados. ¿Qué se hace con ellos?", ["Los golpeados se echan a perder antes.", "Se retiran o se venden primero."], "Se retiran o se venden primero"),
    ],
    mistakes=[("Guardar todos los productos en el mismo lugar por comodidad.", "Cada producto tiene necesidades distintas.", "Se guarda cada lote según su plazo y su fisiología."),
              ("Mezclar fruta golpeada con fruta sana.", "La fruta golpeada se pudre y contamina.", "Se clasifican y se separan.")],
    T=[
        ("abc", "En el acopio: ¿qué es el daño mecánico en un producto?", "El daño por golpes o aplastamiento", "El daño por falta de riego", "El daño por exceso de luz", "El daño mecánico viene de golpes o aplastamiento."),
        ("abc", "En el acopio: ¿qué es la respiración de un producto cosechado?", "El proceso por el que gasta sus reservas y se deteriora", "El paso del aire por la bodega", "El enfriado del producto", "La respiración gasta reservas y acorta la vida del producto."),
        ("abc", "En el acopio: ¿qué plazo es de semanas o meses?", "Mediano plazo", "Corto plazo", "Largo plazo", "El mediano plazo es de semanas o meses."),
        ("abc", "{F} ¿Dónde conviene guardar el Lote H, de tomates frescos?", "En la cámara fría, por ser de corto plazo", "En el silo seco", "En la bodega ventilada por 2 meses", "Los tomates frescos duran pocos días y necesitan frío."),
        ("abc", "{F} ¿Dónde conviene guardar el Lote P, de papas?", "En la bodega ventilada, por ser de mediano plazo", "En la cámara fría por 8 meses", "En el silo seco", "Las papas se guardan semanas o meses en un lugar fresco y ventilado."),
        ("abc", "{F} ¿Dónde conviene guardar el Lote G, de trigo?", "En el silo seco, por ser de largo plazo y estar bajo el máximo de humedad", "En la cámara fría, por ser trigo", "En la bodega ventilada", "El trigo seco se guarda meses en un silo seco."),
        ("abc", "{F} ¿Qué evidencia respalda la decisión sobre el Lote G?", "Su humedad es de 11 % y se vende en 8 meses", "Tiene frutos golpeados", "Se vende en 3 días", "Un grano seco y un plazo largo piden silo seco."),
        ("=", "{F} Si el Lote H tiene 400 cajas y el 10 % está golpeado, ¿cuántas cajas están golpeadas?", "400*10//100", "Se calcula el porcentaje de golpes sobre el total de cajas.", " cajas"),
        ("abc", "{F} Una compañera dice: «guardemos los tres lotes en la cámara fría, es más simple». ¿Qué respuesta es correcta?", "Es incorrecto: cada lote tiene un plazo y una fisiología distintos", "Es correcto, porque el frío sirve para todo", "Es correcto, si hay espacio", "La cámara no es adecuada para todos."),
        ("abc", "{F} El bodeguero quiere entrar al silo para nivelar el trigo antes de la venta. ¿Qué corresponde?", "Rechazarlo: nadie entra al silo, lo hace personal autorizado con equipos", "Aceptarlo, si es rápido", "Aceptarlo, si lleva casco", "El silo es un espacio cerrado y peligroso."),
        ("=", "{F} Si el Lote P se vende en 2 meses de 30 días, ¿cuántos días estará guardado?", "2*30", "Se multiplican los meses por los días de cada mes.", " días"),
        ("abc", "{F} Si el Lote P se vendiera mañana en vez de en 2 meses, ¿qué cambiaría?", "Pasaría a corto plazo y podría necesitar menos tiempo de guarda", "Pasaría a largo plazo", "No cambiaría nada", "El plazo cambia la decisión de guarda."),
        ("abc", "En el acopio: ¿por qué los frutos golpeados se retiran o se venden primero?", "Porque se echan a perder antes y contaminan a los demás", "Porque son más caros", "Porque no respiran", "El daño mecánico acorta su vida."),
    ],
    ctx=("abc", "Un conocido te pregunta dónde guardar sus papas, sin decir cuándo las venderá. ¿Qué respondes?", "Que depende del plazo hasta la venta y de su estado, y que lo define el jefe de bodega o un asesor", "En el silo seco", "En la cámara fría", "El plazo y el estado cambian la decisión."),
    sc=[
        ("En el acopio: ¿dónde se guardan las hortalizas frescas?", "En frío, por ser de corto plazo", "Las hortalizas frescas duran pocos días."),
        ("En el acopio: ¿qué se hace con los frutos golpeados?", "Se retiran o se venden primero", "Se echan a perder antes que los sanos."),
        ("En la bodega: ¿cuántas evidencias debe citar una decisión técnica?", "Al menos dos", "Dos evidencias hacen verificable la decisión."),
    ],
    op=("Caso de ejemplo del «Fundo Demo 5»: Lote Q, lechugas para vender en 2 días; Lote R, cebollas para vender en 3 meses, sanas y secas; Lote S, maíz con 12 % de humedad para vender en 10 meses. Condiciones: cámara fría, bodega ventilada y silo seco. Escribe (a) el lugar para cada lote, (b) una evidencia para el Lote S, (c) cuántos días son 3 meses de 30 días, (d) quién decide.",
        "(a) Q: cámara fría; R: bodega ventilada; S: silo seco. (b) Tiene 12 % de humedad y se vende en 10 meses. (c) 3 × 30 = 90 días. (d) El jefe de bodega con el asesor.",
        ["elige bien los tres lugares", "cita una evidencia", "calcula los días", "nombra quién decide"],
        ["hoja con las cuatro respuestas"],
        ["guardar todo en el mismo lugar", "no citar evidencia"],
        "Pregunta: «¿cuál es el plazo de cada lote?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Elige entre cámara fría, bodega ventilada y silo seco para tres productos inventados y justifica con el plazo.",
    extend="Explica con un ejemplo por qué el plazo hasta la venta cambia la decisión de guarda.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La bodega del «Fundo Demo 3» mide 10 metros de largo y 5 de ancho, y se apila hasta 4 metros de alto. En la pila caben 25 sacos por cada metro cúbico (dato de ejemplo). "
     "Ingresan 4.000 sacos de papas y se pierde 2 % por mal almacenamiento (dato de ejemplo). Precio de ejemplo: $8.000 por saco. Costo de guarda: $200 por saco por mes.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la capacidad de una bodega, las pérdidas y el costo de guardar un producto por varios meses.",
    prior=["Sé calcular volúmenes de cajas con largo, ancho y alto.", "Sé calcular porcentajes enteros.", "Sé multiplicar y dividir enteros."],
    explain=[
        "El volumen de una bodega es el largo por el ancho por el alto, en metros cúbicos (m³). La capacidad en sacos se obtiene multiplicando el volumen por los sacos que caben en cada m³. Si ingresan más sacos que la capacidad, hay que guardar el resto en otro lugar. La pérdida por mal almacenamiento es un porcentaje de lo guardado y reduce el ingreso.",
        "El costo de guarda es el costo por saco por mes multiplicado por los sacos y por los meses. El ingreso esperado es el precio por los sacos que se venden. El margen es el ingreso menos el costo de guarda. Cuantos más meses se guarda, mayor es el costo, así que hay que comparar si conviene esperar. Los valores son de ejemplo y la decisión final la toma el jefe de bodega con el asesor.",
        f"Apilar sobre el límite de altura es un riesgo de caída; la capacidad se respeta. {EMER} {AVISO}",
    ],
    vocab=[("volumen", "espacio que ocupa un cuerpo, en metros cúbicos"), ("capacidad", "cantidad máxima que cabe en un lugar"), ("pérdida por mal almacenamiento", "producto que se echa a perder por guardarlo mal"), ("costo de guarda", "gasto de guardar un producto cada mes"), ("margen", "ingreso menos costo")],
    worked=[
        ("Volumen", "Una bodega de ejemplo mide 10 m de largo, 5 m de ancho y 3 m de alto. ¿Cuál es su volumen?", ["Se multiplican largo, ancho y alto.", "10 por 5 por 3."], "150 m³"),
        ("Costo de guarda", "Se guardan 100 sacos de ejemplo por 3 meses a $50 por saco por mes. ¿Cuánto cuesta?", ["Se multiplica el costo por los sacos y por los meses.", "50 por 100 por 3."], "$15.000"),
    ],
    mistakes=[("Olvidar la altura de apilado al calcular la capacidad.", "El volumen necesita las tres dimensiones.", "Se multiplican largo, ancho y alto."),
              ("Apilar sobre el límite de altura para que quepan más sacos.", "Aumenta el riesgo de caída.", "Se respeta la capacidad y se usa otro lugar.")],
    T=[
        ("abc", "En el acopio: ¿qué es el volumen de una bodega?", "El espacio que ocupa, en metros cúbicos", "El peso de lo que guarda", "El número de sacos que tiene", "El volumen mide el espacio que ocupa un cuerpo."),
        ("abc", "En el acopio: ¿qué es el costo de guarda?", "El gasto de guardar un producto cada mes", "El precio de venta del producto", "El valor de la bodega", "El costo de guarda se paga mes a mes."),
        ("abc", "En el acopio: ¿qué pasa si ingresa más producto que la capacidad?", "Hay que guardar el resto en otro lugar", "Se apila sobre el límite de altura", "Se bota el producto", "El límite de altura no se supera."),
        ("=", "{F} ¿Cuál es el volumen de la bodega en metros cúbicos?", "10*5*4", "Se multiplican largo, ancho y alto.", " m³"),
        ("=", "{F} ¿Cuántos sacos caben en la bodega?", "10*5*4*25", "Se multiplica el volumen por los sacos que caben en cada metro cúbico.", " sacos"),
        ("=", "{F} Si ingresan 4.000 sacos, ¿cuántos sacos de capacidad quedan libres en la bodega?", "10*5*4*25-4000", "Se resta los sacos que ingresan a la capacidad de la bodega.", " sacos"),
        ("=", "{F} ¿Cuántos sacos se pierden por mal almacenamiento de los 4.000 que ingresan?", "4000*2//100", "Se calcula el porcentaje de pérdida sobre los sacos ingresados.", " sacos"),
        ("=", "{F} ¿Cuántos sacos quedan para vender después de la pérdida?", "4000-4000*2//100", "Se resta la pérdida a los sacos ingresados.", " sacos"),
        ("=", "{F} ¿Cuánto cuesta guardar los sacos que quedan por 3 meses?", "(4000-4000*2//100)*200*3", "Se multiplican los sacos por el costo mensual y por los meses.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso por vender los sacos que quedan?", "(4000-4000*2//100)*8000", "Se multiplican los sacos por el precio de cada saco.", " pesos"),
        ("abc", "{F} Un bodeguero propone apilar un metro más alto «por si llegan más sacos». ¿Qué corresponde?", "Rechazarlo: se respeta el límite de altura y el exceso se guarda en otro lugar", "Aceptarlo, si lo hace con cuidado", "Aceptarlo, si es de día", "Superar la altura máxima aumenta el riesgo de caída."),
        ("abc", "{F} El jefe quiere mover los pallets con una transpaleta que una estudiante nunca ha operado. ¿Qué corresponde?", "Rechazarlo: la transpaleta la opera personal capacitado y autorizado", "Aceptarlo, si va lenta", "Aceptarlo, si hay prisa", "Operar equipos exige formación y autorización."),
        ("abc", "En el acopio: ¿por qué a mayor número de meses de guarda aumenta el costo?", "Porque el costo de guarda se paga cada mes", "Porque el producto pesa más", "Porque el precio baja", "El costo mensual se multiplica por los meses."),
    ],
    ctx=("abc", "Un conocido te pide que le digas si le conviene guardar sus papas 6 meses y te da solo el precio actual. ¿Qué respondes?", "Que faltan el costo de guarda y la pérdida, y que lo evalúa un asesor", "Que sí, siempre", "Que no, nunca", "El costo y las pérdidas entran en el cálculo."),
    sc=[
        ("En el acopio: ¿cómo se calcula el volumen de una bodega?", "Largo por ancho por alto", "El volumen usa las tres dimensiones."),
        ("En la bodega: ¿qué se hace con los sacos que superan la capacidad?", "Se guardan en otro lugar", "No se supera el límite de altura."),
        ("En el acopio: ¿cómo se calcula el costo de guarda?", "Costo mensual por sacos por meses", "El costo se multiplica por los sacos y por los meses."),
    ],
    op=("Datos de ejemplo del «Fundo Demo 6»: bodega de 10 m de largo, 8 de ancho y 3 de alto; caben 10 sacos por m³; ingresan 2.000 sacos; pérdida de 5 %; costo de guarda de $100 por saco por mes por 2 meses. Escribe (a) el volumen, (b) la capacidad en sacos y cuántos sobran, (c) los sacos perdidos, (d) el costo de guardar los sacos que quedan por 2 meses.",
        "(a) 10 × 8 × 3 = 240 m³. (b) 240 × 10 = 2.400 sacos; no sobra ninguno. (c) 2.000 × 5 ÷ 100 = 100 sacos. (d) (2.000 − 100) × 100 × 2 = $380.000.",
        ["calcula el volumen", "calcula la capacidad", "calcula la pérdida", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el alto", "olvidar los meses"],
        "Pregunta: «¿qué tres medidas se multiplican para el volumen?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el volumen de una bodega inventada de 12 m, 5 m y 3 m.",
    extend="Explica con un ejemplo por qué respetar la altura máxima de apilado protege a las personas.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo» de un fundo ficticio atiende un tractor, una pulverizadora y un arado. "
     "Peligros anotados: partes móviles (correas, poleas y ejes), energía almacenada (resortes, presión de aceite hidráulico y batería), combustible y aceites inflamables, superficies calientes del motor y del escape, implementos pesados que pueden caer y mucho ruido.")
build(
    O5, 1, F,
    use="Aprenderé qué es el mantenimiento preventivo y correctivo de la maquinaria, cuáles son los peligros de un taller agrícola y por qué la reparación la hace solo personal autorizado.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El mantenimiento preventivo son las revisiones y cuidados que se hacen según un plan, antes de que ocurra una falla, para evitarla. El mantenimiento correctivo es la reparación que se hace después de una falla. El mantenimiento básico del operador es la inspección visual antes de usar el equipo y el aviso inmediato de cualquier anomalía; no incluye abrir ni reparar. Prevenir cuesta menos que corregir y es más seguro.",
        "Una máquina tiene peligros incluso apagada: partes móviles que pueden arrastrar ropa y manos; energía almacenada, como resortes o aceite a presión, que puede soltarse; combustibles inflamables; superficies calientes; y piezas pesadas que pueden caer. Para trabajar en un equipo, personal autorizado lo deja sin energía y lo señaliza para que nadie lo encienda; a esto se le llama bloqueo y etiquetado. La jerarquía de controles también aplica: eliminar, sustituir, cambiar el lugar o el equipo, reglas y, al final, EPP.",
        f"La reparación y la mantención las hace personal capacitado y autorizado, bajo la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "revisiones y cuidados planificados para evitar fallas"), ("mantenimiento correctivo", "reparación que se hace después de una falla"), ("inspección visual", "revisión con la vista antes de usar el equipo"), ("energía almacenada", "energía que un equipo conserva aunque esté apagado"), ("bloqueo y etiquetado", "dejar un equipo sin energía y señalizar que no se debe encender"), ("anomalía", "algo distinto de lo normal en el funcionamiento")],
    worked=[
        ("Preventivo o correctivo", "Un fundo de ejemplo revisa el nivel de aceite del tractor cada semana, aunque no haya fallas. ¿Es preventivo o correctivo?", ["La revisión se hace antes de cualquier falla.", "Eso es mantenimiento preventivo."], "Preventivo"),
        ("Clasificar un control", "Un taller de ejemplo pone un piso antideslizante y un desagüe junto a la zona donde se lavan los implementos. ¿Qué tipo de control es?", ["El piso cambia físicamente el lugar de trabajo.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que una máquina apagada no tiene peligros.", "Puede tener energía almacenada, piezas calientes o piezas que caen.", "Solo personal autorizado la deja sin energía y la señaliza."),
              ("Creer que el operador puede reparar «una falla pequeña» para ahorrar tiempo.", "Reparar exige formación y autorización.", "El operador informa la anomalía y no repara.")],
    T=[
        ("abc", "En el mantenimiento de maquinaria: ¿qué es el mantenimiento preventivo?", "Las revisiones y cuidados planificados para evitar fallas", "La reparación que se hace después de una falla", "El uso del equipo sin revisión", "El preventivo se hace antes de la falla; la reparación posterior es correctivo."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué es el mantenimiento correctivo?", "La reparación que se hace después de una falla", "Las revisiones planificadas antes de una falla", "La limpieza diaria del taller", "El correctivo ocurre después de la falla."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué es la energía almacenada?", "La energía que un equipo conserva aunque esté apagado", "La energía de la red eléctrica", "La energía de quien lo usa", "Resortes, aceite a presión o baterías conservan energía."),
        ("=", "{F} El taller atiende 3 equipos y cada uno tiene 4 puntos de inspección diaria. ¿Cuántos puntos de inspección hay en total?", "3*4", "Se multiplican los equipos por los puntos de cada uno.", " puntos"),
        ("abc", "{F} Una protección fija sobre las correas del equipo es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "La protección es una parte del equipo y funciona siempre."),
        ("abc", "{F} Una regla que dice «el equipo se bloquea y etiqueta antes de cualquier intervención» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el equipo", "De sustitución, porque cambia al operador", "Una regla escrita es un control de tipo administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al aceite a presión de un equipo apagado?", "Que se libere de golpe y cause lesiones", "El aceite mismo en el estanque", "Que el equipo esté apagado", "El riesgo es la posibilidad de daño; el aceite a presión es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo se revisa un tractor, así que lo reparo yo». ¿Qué respuesta es correcta?", "Es peligroso: la reparación la hace personal capacitado y autorizado", "Es correcto, si apaga el motor", "Es correcto, si usa guantes", "Apagar el motor no elimina la energía almacenada."),
        ("abc", "{F} Durante una visita al taller, el tractor suelta humo y una persona queda atrapada bajo un implemento. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Intentar levantar el implemento tú", "Encender el motor para moverlo", "Acercarse sin formación puede causar otro accidente."),
        ("abc", "En el mantenimiento de maquinaria: ¿por qué prevenir una falla es más seguro que reparar?", "Porque evita intervenir en un equipo averiado y reduce el riesgo", "Porque no necesita planificación", "Porque elimina el combustible", "Prevenir evita trabajar en un equipo en falla."),
        ("abc", "{F} Se propone solo entregar guantes para evitar atrapamientos en las correas. ¿Qué medida es más efectiva?", "Colocar protecciones fijas sobre las partes móviles", "Entregar guantes más gruesos", "Pedir mayor cuidado", "Cubrir las partes móviles actúa sobre el peligro."),
        ("=", "{F} El tractor trabaja 8 horas al día durante 5 días a la semana. ¿Cuántas horas trabaja en una semana?", "8*5", "Se multiplican las horas diarias por los días de trabajo.", " horas"),
        ("abc", "En el mantenimiento de maquinaria: ¿qué hace un operador si nota ruido anormal?", "Avisa de inmediato a su jefe, sin intentar repararlo", "Sigue trabajando sin decir nada", "Lo desarma para revisarlo", "El operador informa; la revisión la hace personal autorizado."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por cambiar piezas del tractor de su fundo «porque ya viste cómo se hace». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si el tractor está apagado", "Que sí, con guantes", "Haber visto el concepto no habilita para intervenir una máquina."),
    sc=[
        ("En el mantenimiento de maquinaria: ¿qué hace el mantenimiento preventivo?", "Evita fallas con revisiones planificadas", "El preventivo se anticipa a la falla."),
        ("En el taller agrícola: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En el mantenimiento de maquinaria: ¿quién repara el equipo?", "Personal capacitado y autorizado", "La reparación exige formación y norma vigente."),
    ],
    op=("El «Taller Demo 2» anota una tarea de ejemplo: cambiar una correa de la pulverizadora con el motor recién apagado, sin bloqueo ni etiqueta, en un taller con piso aceitoso. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien con la mano atrapada en una correa.",
        "(a) Peligro: energía almacenada y partes móviles; riesgo: que el equipo se mueva y atrape la mano. (b) Una regla de bloquear y etiquetar antes de cualquier intervención. (c) Una protección fija sobre la correa. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer apagar el equipo y tocar", "no avisar"],
        "Pregunta: «¿qué control cubre la parte móvil aunque alguien se olvide de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Clasifica como preventivo o correctivo: cambiar un filtro por horas de uso, reparar un neumático reventado y revisar el nivel de aceite.",
    extend="Explica con un ejemplo por qué una máquina apagada puede seguir siendo peligrosa.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (hoja de vida y bitácora de ejemplo, inventadas). Tractor T-1 del «Taller Demo»: el horómetro (contador de horas de uso) marca 1.480 horas. Plan de mantención de ejemplo: una mantención cada 250 horas. La última mantención se hizo a las 1.250 horas. "
     "Bitácora del mes: el operador reportó (1) ruido en un eje, (2) una fuga leve de aceite y (3) una luz del tablero encendida. Documentos: el manual del fabricante, la hoja de vida del equipo, la bitácora y la orden de trabajo.")
build(
    O5, 2, F,
    use="Aprenderé los conceptos de horómetro, plan de mantención, desgaste y repuesto, los documentos de la mantención de maquinaria y los roles del operador, el mecánico y el jefe de taller.",
    prior=["Sé qué es el mantenimiento preventivo y correctivo.", "Sé restar y dividir enteros.", "Sé leer una ficha con datos."],
    explain=[
        "El horómetro es el contador que mide las horas de uso de un equipo. El plan de mantención indica cada cuántas horas se hacen las revisiones; por ejemplo, cada 250 horas. Para saber cuándo toca la siguiente mantención se suma el intervalo a la hora de la última. El desgaste es el deterioro normal por el uso, y un repuesto es la pieza que reemplaza a otra gastada o dañada.",
        "Los documentos son el manual del fabricante, que indica cada cuánto y qué revisar; la hoja de vida, que resume la historia del equipo; la bitácora, donde el operador anota las anomalías; y la orden de trabajo, que dice qué intervención se hará, quién y cuándo. El operador inspecciona y reporta; el mecánico autorizado repara; el jefe de taller programa; y el bodeguero de repuestos entrega las piezas.",
        f"Un registro de mantención no se altera ni se completa con datos inventados. {EMER} {AVISO}",
    ],
    vocab=[("horómetro", "contador que mide las horas de uso de un equipo"), ("plan de mantención", "documento que dice cada cuántas horas se revisa un equipo"), ("desgaste", "deterioro normal por el uso"), ("repuesto", "pieza que reemplaza a otra gastada o dañada"), ("hoja de vida", "documento que resume la historia de un equipo"), ("orden de trabajo", "documento que dice qué intervención se hará, quién y cuándo")],
    worked=[
        ("Próxima mantención", "Un equipo de ejemplo tuvo su última mantención a las 600 horas y se hace cada 200 horas. ¿A qué hora toca la siguiente?", ["Se suma el intervalo a la última mantención.", "600 más 200."], "A las 800 horas"),
        ("Horas restantes", "El horómetro de ese equipo marca 760 horas. ¿Cuántas horas faltan para la mantención?", ["Se resta la lectura actual a la hora de la mantención.", "800 menos 760."], "40 horas"),
    ],
    mistakes=[("Postergar la mantención porque «el equipo todavía funciona».", "Una falla durante el uso es más costosa y peligrosa.", "Se respeta el plan de mantención."),
              ("Anotar una anomalía en la bitácora sin avisar al jefe de taller.", "La anomalía puede ser urgente.", "Se anota y se informa de inmediato.")],
    T=[
        ("abc", "En el mantenimiento de maquinaria: ¿qué mide el horómetro?", "Las horas de uso del equipo", "Los kilos de combustible", "La temperatura del motor", "El horómetro cuenta las horas de uso."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué es un repuesto?", "Una pieza que reemplaza a otra gastada o dañada", "Un documento que describe el equipo", "Una herramienta del operador", "El repuesto es la pieza de reemplazo."),
        ("abc", "En el mantenimiento de maquinaria: ¿para qué sirve la orden de trabajo?", "Para indicar qué intervención se hará, quién y cuándo", "Para medir las horas de uso", "Para describir el diseño del equipo", "La orden dirige la intervención: qué, quién y cuándo."),
        ("=", "{F} ¿A cuántas horas del horómetro toca la siguiente mantención de T-1?", "1250+250", "Se suma el intervalo de mantención a la hora de la última.", " horas"),
        ("=", "{F} ¿Cuántas horas faltan para esa mantención?", "1250+250-1480", "Se resta la lectura actual del horómetro a la hora de la mantención.", " horas"),
        ("=", "{F} ¿Cuántas horas ha trabajado T-1 desde su última mantención?", "1480-1250", "Se resta la hora de la última mantención a la lectura actual.", " horas"),
        ("abc", "{F} ¿Qué documento resume la historia de T-1?", "La hoja de vida", "La orden de trabajo", "La bitácora", "La hoja de vida resume la historia del equipo."),
        ("abc", "{F} ¿Dónde anota el operador el ruido en el eje?", "En la bitácora", "En la hoja de vida", "En el manual del fabricante", "El operador anota las anomalías en la bitácora."),
        ("abc", "{F} ¿Quién debe reparar la fuga de aceite?", "El mecánico autorizado", "El operador que la detectó", "Una estudiante con la ficha", "La reparación la hace personal autorizado."),
        ("abc", "{F} Un operador dice: «la fuga es leve, la limpio y sigo trabajando sin avisar». ¿Qué respuesta es correcta?", "Es incorrecto: se detiene si es seguro, se anota y se informa", "Es correcto, porque es leve", "Es correcto, si limpia bien", "Una fuga puede crecer y debe informarse."),
        ("abc", "{F} El jefe de taller quiere anotar en la hoja de vida que la mantención se hizo a las 1.500 horas, aunque no se hizo. ¿Qué corresponde?", "Rechazarlo: el registro anota solo lo realizado", "Aceptarlo, para cumplir el plan", "Aceptarlo, si se hace mañana", "Anotar lo que no se hizo falsea el registro."),
        ("abc", "{F} Un mecánico está trabajando bajo el tractor sin bloqueo y alguien enciende el motor. ¿Qué corresponde a quien lo ve?", "No acercarte, avisar a un adulto responsable y a emergencias", "Meterte bajo el tractor", "Apagar el motor tú sin saber cómo", "Acercarse sin formación puede causar otro accidente."),
        ("abc", "En el mantenimiento de maquinaria: ¿por qué el manual del fabricante es importante?", "Porque indica cada cuánto y qué revisar en ese equipo", "Porque reemplaza al mecánico", "Porque se puede ignorar si el equipo funciona", "Cada equipo tiene su plan indicado por el fabricante."),
    ],
    ctx=("abc", "Una conocida te pide que cambies las horas del horómetro del tractor «para que parezca que tiene menos uso» al venderlo. ¿Qué respondes?", "Que no, porque es falsear un registro, y que lo consultarás con un adulto responsable", "Que sí, un poco", "Que sí, si no se nota", "Alterar el horómetro engaña a quien compra."),
    sc=[
        ("En el mantenimiento de maquinaria: ¿cómo se calcula la hora de la próxima mantención?", "Hora de la última más el intervalo", "El intervalo se suma a la última mantención."),
        ("En el taller agrícola: ¿qué documento anota las anomalías que reporta el operador?", "La bitácora", "La bitácora guarda los reportes del operador."),
        ("En el mantenimiento de maquinaria: ¿quién programa las mantenciones del taller?", "El jefe de taller", "El jefe de taller organiza el plan."),
    ],
    op=("Ficha de ejemplo del «Taller Demo 3»: pulverizadora P-2, horómetro 880 horas; mantención cada 200 horas; última mantención a las 800 horas. Bitácora: el operador reportó una manguera con una rajadura. Escribe (a) la hora de la próxima mantención, (b) cuántas horas faltan, (c) en qué documento anotó el operador el reporte, (d) quién repara la manguera y qué hace el operador.",
        "(a) 800 + 200 = 1.000 horas. (b) 1.000 − 880 = 120 horas. (c) En la bitácora. (d) El mecánico autorizado repara; el operador detiene el equipo si es seguro y avisa.",
        ["calcula la próxima mantención", "calcula las horas restantes", "nombra el documento", "distingue operador y mecánico"],
        ["hoja con las cuatro respuestas"],
        ["no sumar el intervalo", "reparar por cuenta propia"],
        "Pregunta: «¿a qué hora fue la última mantención?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la próxima mantención de un equipo inventado con última a las 400 horas e intervalo de 150 horas.",
    extend="Explica con un ejemplo por qué la bitácora ayuda a decidir una mantención.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (reportes de ejemplo, inventados). Reportes del operador en el «Taller Demo»: R1, humo oscuro y olor a quemado desde el motor; R2, faltan 30 horas para la mantención programada; "
     "R3, el filtro de aire se ve con polvo acumulado en la inspección visual diaria; R4, el tractor arranca y funciona normal, sin ruidos ni fugas; R5, fuga de combustible bajo el estanque. "
     "Categorías: A, detener el equipo y avisar de inmediato; B, anotar en la bitácora y programar mantención; C, sin acción, funcionamiento normal.")
build(
    O5, 3, F,
    use="Aprenderé a analizar reportes de un operador, a clasificar la urgencia de cada anomalía y a decidir con evidencia quién interviene, sin reparar nada.",
    prior=["Sé qué es el mantenimiento preventivo y correctivo.", "Sé qué es la bitácora.", "Sé leer una lista de datos."],
    explain=[
        "Para analizar un reporte se pregunta cuánta urgencia tiene. Si hay humo, olor a quemado o fuga de combustible, el riesgo de incendio o de lesión es inmediato: el operador detiene el equipo si es seguro y avisa. Si hay un desgaste visible o se acerca una mantención, se anota en la bitácora y se programa. Si todo funciona normal, no se hace nada, pero se sigue la inspección diaria.",
        "Cada reporte se clasifica con una evidencia y se asigna un responsable. El operador informa; el mecánico autorizado diagnostica y repara; el jefe de taller programa; el prevencionista asesora si hay riesgo. Un buen análisis dice la categoría, la evidencia y quién interviene. Nadie repara por cuenta propia ni sigue trabajando con un equipo en riesgo.",
        f"Un combustible que gotea cerca de superficies calientes puede encenderse. {EMER} {AVISO}",
    ],
    vocab=[("urgencia", "qué tan rápido hay que actuar ante una anomalía"), ("diagnóstico", "identificación de la causa de una falla"), ("riesgo de incendio", "posibilidad de que algo se encienda"), ("programar", "fijar fecha y responsable de una tarea"), ("evidencia", "dato del reporte que respalda una decisión")],
    worked=[
        ("Clasificar la urgencia", "Un operador de ejemplo reporta humo blanco y olor a quemado del motor. ¿A qué categoría corresponde?", ["El humo y el olor indican riesgo inmediato.", "Se detiene el equipo y se avisa: categoría A."], "A"),
        ("Clasificar un desgaste", "Un operador de ejemplo reporta que un neumático tiene un desgaste visible y aún no falla. ¿A qué categoría corresponde?", ["No hay riesgo inmediato.", "Se anota y se programa: categoría B."], "B"),
    ],
    mistakes=[("Seguir trabajando con una fuga de combustible «hasta terminar el potrero».", "El combustible que gotea puede encenderse con el calor.", "Se detiene el equipo si es seguro y se avisa de inmediato."),
              ("Ignorar el polvo del filtro porque «el motor anda bien».", "El polvo acumulado desgasta el motor a futuro.", "Se anota y se programa su revisión.")],
    T=[
        ("abc", "En el mantenimiento de maquinaria: ¿qué es la urgencia de una anomalía?", "Qué tan rápido hay que actuar", "Qué tan cara es la reparación", "Quién la detectó", "La urgencia dice la rapidez de la acción."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué es un diagnóstico?", "La identificación de la causa de una falla", "La reparación de la falla", "El aviso al jefe", "El diagnóstico identifica la causa de la falla."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué significa programar una mantención?", "Fijar fecha y responsable de la tarea", "Hacerla de inmediato sin plan", "Ignorarla hasta que falle", "Programar es fijar fecha y responsable."),
        ("abc", "{F} ¿A qué categoría corresponde el reporte R1, humo oscuro y olor a quemado?", "A, detener el equipo y avisar de inmediato", "B, anotar y programar", "C, sin acción", "Humo y olor a quemado indican riesgo inmediato."),
        ("abc", "{F} ¿A qué categoría corresponde el reporte R2, faltan 30 horas para la mantención?", "B, anotar en la bitácora y programar mantención", "A, detener el equipo", "C, sin acción", "Es una mantención prevista, no una emergencia."),
        ("abc", "{F} ¿A qué categoría corresponde el reporte R3, polvo acumulado en el filtro de aire?", "B, anotar en la bitácora y programar su revisión", "A, detener el equipo de inmediato", "C, sin acción", "El polvo es un desgaste que se programa, sin riesgo inmediato."),
        ("abc", "{F} ¿A qué categoría corresponde el reporte R4, funcionamiento normal?", "C, sin acción", "A, detener el equipo", "B, anotar y programar", "Sin ruidos ni fugas, no hay anomalía."),
        ("abc", "{F} ¿A qué categoría corresponde el reporte R5, fuga de combustible?", "A, detener el equipo y avisar de inmediato", "B, anotar y programar", "C, sin acción", "El combustible que gotea puede encenderse con el calor."),
        ("=", "{F} Si el horómetro marca 1.470 horas y faltan 30 horas, ¿a qué hora toca la mantención?", "1470+30", "Se suman las horas restantes a la lectura del horómetro.", " horas"),
        ("abc", "{F} Una estudiante dice: «puedo arreglar la fuga de R5 apretando la manguera con una llave». ¿Qué respuesta es correcta?", "Es peligroso: la reparación la hace personal autorizado", "Es correcto, si aprieta fuerte", "Es correcto, si está el motor apagado", "Intervenir un circuito de combustible exige formación."),
        ("abc", "{F} El operador del reporte R1 quiere seguir trabajando «una hora más». ¿Qué corresponde?", "Rechazarlo: se detiene el equipo si es seguro y se avisa de inmediato", "Aceptarlo, si termina el potrero", "Aceptarlo, si baja la velocidad", "Con humo hay riesgo de incendio."),
        ("abc", "{F} Aparece fuego bajo el tractor y una persona cerca intenta apagarlo con un balde de agua. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable y a emergencias", "Ayudar con más agua", "Quedarse a mirar de cerca", "El agua puede propagar un fuego de combustible; se avisa a quienes pueden actuar."),
        ("abc", "En el mantenimiento de maquinaria: ¿por qué se anota el reporte en la bitácora aunque se resuelva rápido?", "Porque deja historia para detectar fallas repetidas", "Porque aumenta el tiempo de reparación", "Porque la bitácora reemplaza al mecánico", "La bitácora acumula la historia del equipo."),
    ],
    ctx=("abc", "Un conocido te muestra una fotografía de una fuga de combustible en su tractor y te pide que le digas cómo repararla. ¿Qué respondes?", "Que debe detener el equipo y llamar a un mecánico autorizado, y que tú no puedes indicar la reparación", "Que apriete la manguera", "Que lo siga usando con cuidado", "Una fuga de combustible es peligrosa y se deriva a personal autorizado."),
    sc=[
        ("En el mantenimiento de maquinaria: ¿qué se hace ante humo y olor a quemado?", "Se detiene el equipo si es seguro y se avisa", "El riesgo de incendio es inmediato."),
        ("En el taller agrícola: ¿qué se hace con un desgaste visible sin falla?", "Se anota en la bitácora y se programa", "No hay emergencia, pero conviene planificar."),
        ("En el mantenimiento de maquinaria: ¿quién diagnostica y repara?", "El mecánico autorizado", "El diagnóstico y la reparación exigen formación."),
    ],
    op=("Reportes de ejemplo del «Taller Demo 3»: S1, ruido metálico fuerte y vibración del eje; S2, el horómetro marca 980 horas y la mantención programada es a las 1.000 horas; S3, funcionamiento normal; S4, líquido de aceite bajo el motor goteando rápido. Categorías: A, detener y avisar de inmediato; B, anotar y programar; C, sin acción. Escribe (a) la categoría de S1, S2, S3 y S4, (b) cuántas horas faltan para la mantención de S2, (c) una evidencia para S4, (d) quién repara.",
        "(a) S1: A; S2: B; S3: C; S4: A. (b) 1.000 − 980 = 20 horas. (c) El aceite gotea rápido, lo que puede dañar el motor o causar un incendio. (d) El mecánico autorizado.",
        ["clasifica bien los cuatro reportes", "calcula las horas", "cita una evidencia", "nombra al mecánico autorizado"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el ruido metálico como normal", "proponer reparar por cuenta propia"],
        "Pregunta: «¿qué reportes tienen riesgo inmediato?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres reportes inventados: olor a gas, nivel de aceite bajo el mínimo y un equipo que anda normal.",
    extend="Explica con un ejemplo por qué una fuga pequeña se informa igual.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Tractor T-1 del «Taller Demo»: se programan 2.000 horas de trabajo al año. Plan de mantención de ejemplo: cada 250 horas, con un costo de $200.000 por mantención. "
     "Una falla correctiva de ejemplo cuesta $1.200.000 y deja el equipo detenido 20 horas. Año sin plan: 3 fallas correctivas. Año con plan: 1 falla correctiva.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular cuántas mantenciones tiene un plan, su costo, la disponibilidad del equipo y el ahorro de prevenir fallas.",
    prior=["Sé qué es el mantenimiento preventivo y correctivo.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes enteros."],
    explain=[
        "El número de mantenciones preventivas del año es las horas de trabajo divididas por el intervalo de mantención. Su costo es ese número por el costo de cada una. El costo del mantenimiento correctivo es el número de fallas por el costo de cada falla. La disponibilidad es el porcentaje de tiempo en que el equipo está listo para trabajar: se calcula como las horas disponibles divididas por las horas programadas, por 100.",
        "Comparar un año sin plan con uno con plan permite ver si prevenir conviene: se suman los costos de mantenciones y de fallas en cada caso, y se resta. También se mira la disponibilidad, porque una falla detiene el equipo y retrasa las labores. Los valores son de ejemplo, y la decisión final la toman el jefe de taller y el asesor.",
        f"Ahorrar en mantención nunca justifica trabajar con un equipo en riesgo. {EMER} {AVISO}",
    ],
    vocab=[("disponibilidad", "porcentaje del tiempo en que el equipo está listo para trabajar"), ("horas programadas", "horas de trabajo que se planificaron"), ("horas disponibles", "horas programadas menos las horas detenido"), ("costo correctivo", "gasto por las fallas y sus reparaciones"), ("costo preventivo", "gasto por las mantenciones planificadas")],
    worked=[
        ("Número de mantenciones", "Un equipo de ejemplo trabaja 1.000 horas al año con mantención cada 200 horas. ¿Cuántas mantenciones tiene al año?", ["Se divide el trabajo anual entre el intervalo.", "1.000 entre 200."], "5 mantenciones"),
        ("Disponibilidad", "Un equipo de ejemplo tuvo 100 horas programadas y estuvo detenido 10 horas. ¿Cuál fue su disponibilidad?", ["Horas disponibles: 100 menos 10, o sea 90.", "90 de 100 es 90 por ciento."], "90 %"),
    ],
    mistakes=[("Comparar solo el costo de la mantención con el de una falla, sin mirar las horas detenido.", "Una falla también retrasa las labores.", "Se mira además la disponibilidad."),
              ("Posponer mantenciones para ahorrar y trabajar con el equipo en riesgo.", "Aumenta el riesgo de accidente.", "El ahorro no justifica un riesgo para las personas.")],
    T=[
        ("abc", "En el mantenimiento de maquinaria: ¿qué es la disponibilidad de un equipo?", "El porcentaje del tiempo en que está listo para trabajar", "El número de horas de uso", "El precio de las mantenciones", "La disponibilidad relaciona horas disponibles y programadas."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué es el costo correctivo?", "El gasto por las fallas y sus reparaciones", "El gasto por las revisiones planificadas", "El costo del combustible", "El correctivo es el gasto posterior a la falla."),
        ("abc", "En el mantenimiento de maquinaria: ¿qué efecto tiene una falla en las labores?", "Detiene el equipo y retrasa las labores", "Acelera las labores", "No tiene efecto", "Una falla detiene el equipo y retrasa las labores."),
        ("=", "{F} ¿Cuántas mantenciones preventivas tiene T-1 al año?", "2000//250", "Se divide las horas anuales entre el intervalo de mantención.", " mantenciones"),
        ("=", "{F} ¿Cuál es el costo anual de las mantenciones preventivas?", "2000//250*200000", "Se multiplica el número de mantenciones por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de las fallas del año sin plan?", "3*1200000", "Se multiplica el número de fallas por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del año con plan (mantenciones más la falla)?", "2000//250*200000+1*1200000", "Se suman el costo de las mantenciones y el de la falla.", " pesos"),
        ("=", "{F} ¿Cuánto se ahorra en el año con plan respecto del año sin plan?", "3*1200000-(2000//250*200000+1*1200000)", "Se resta el costo con plan al costo sin plan.", " pesos"),
        ("=", "{F} ¿Cuántas horas estuvo detenido T-1 en el año sin plan por sus 3 fallas?", "3*20", "Se multiplican las fallas por las horas detenido en cada una.", " horas"),
        ("=", "{F} ¿Cuál fue la disponibilidad del año sin plan, en porcentaje de las horas programadas?", "(2000-3*20)*100//2000", "Se dividen las horas disponibles entre las programadas y se multiplica por 100.", " %"),
        ("abc", "{F} Un jefe propone saltar la mantención de las 1.250 horas para ahorrar $200.000. ¿Qué corresponde?", "Rechazarlo: el ahorro no justifica el riesgo y puede salir más caro", "Aceptarlo, porque ahorra dinero", "Aceptarlo, si el equipo suena bien", "Saltar mantenciones aumenta el riesgo y el costo correctivo."),
        ("abc", "{F} Una estudiante dice: «ya sé calcular los costos, así que puedo hacer la mantención del tractor yo». ¿Qué respuesta es correcta?", "Es incorrecto: la mantención la hace personal autorizado", "Es correcto, si usa el manual", "Es correcto, si es el cambio de aceite", "Calcular costos no habilita para intervenir una máquina."),
        ("abc", "En el mantenimiento de maquinaria: ¿por qué conviene comparar costos de un año con plan y sin plan?", "Para ver si prevenir fallas conviene económicamente", "Para evitar hacer mantenciones", "Para eliminar el registro", "La comparación muestra el efecto del plan."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene dejar de hacer mantenciones preventivas para ahorrar. ¿Qué respondes?", "Que debe comparar costos de fallas, horas detenido y riesgos con un asesor", "Que sí, que ahorre", "Que no, nunca", "La decisión usa datos de costos, disponibilidad y seguridad."),
    sc=[
        ("En el mantenimiento de maquinaria: ¿cómo se calcula el número de mantenciones al año?", "Horas anuales entre el intervalo", "Se divide el trabajo anual entre las horas de cada intervalo."),
        ("En el taller agrícola: ¿cómo se calcula la disponibilidad?", "Horas disponibles entre horas programadas, por 100", "La disponibilidad es un porcentaje del tiempo programado."),
        ("En el mantenimiento de maquinaria: ¿qué se compara entre un año con plan y uno sin plan?", "Los costos totales y la disponibilidad", "La comparación muestra el efecto de prevenir."),
    ],
    op=("Datos de ejemplo del «Taller Demo 4»: pulverizadora con 600 horas de trabajo al año; mantención cada 150 horas a $100.000 cada una; una falla cuesta $800.000 y detiene 10 horas. Año sin plan: 2 fallas. Año con plan: 0 fallas. Escribe (a) las mantenciones del año con plan, (b) el costo total de cada año, (c) el ahorro de tener plan, (d) quién ejecuta las mantenciones.",
        "(a) 600 ÷ 150 = 4 mantenciones. (b) Con plan: 4 × 100.000 = $400.000; sin plan: 2 × 800.000 = $1.600.000. (c) 1.600.000 − 400.000 = $1.200.000. (d) El mecánico autorizado.",
        ["calcula las mantenciones", "calcula los costos de cada año", "calcula el ahorro", "nombra quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por el intervalo", "ignorar la disponibilidad", "decir que lo ejecuta cualquiera"],
        "Pregunta: «¿entre qué número divides las horas anuales?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la disponibilidad de un equipo inventado con 500 horas programadas y 25 horas detenido.",
    extend="Explica con un ejemplo por qué un plan de mantención protege también a las personas.",
)

"""Telecomunicaciones TP 3.º y 4.º medio: OAE-01 (leer esquemas, proyectos y lenguaje simbólico), OAE-02 (equipos y sistemas de señal: solo conceptos) y OAE-03 (sistemas operativos en una red LAN). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_tele_common import AVISO, build

O1 = "TP-TELE-3y4-OAE-01"
O2 = "TP-TELE-3y4-OAE-02"
O3 = "TP-TELE-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (orden de trabajo de ejemplo, inventada). La empresa ficticia «Redes Austral Ltda.» recibe la orden OT-101: dejar documentado el enlace de datos entre la oficina central y la bodega, "
     "unidas por un recorrido de cable de 60 metros. Documentos entregados: plano de planta, esquema de la red y lista de materiales (cable de red 80 metros, 2 conectores y 1 caja de pared). "
     "Riesgos anotados: el recorrido pasa por una canaleta a 3 metros de altura, cerca de luminarias con energía eléctrica.")
build(
    O1, 1, F,
    use="Aprenderé para qué sirven los esquemas y los proyectos en el trabajo de telecomunicaciones, qué norma y qué riesgos hay que considerar y qué no puedo hacer solo.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar y restar medidas en metros.", "Sé que una empresa entrega órdenes de trabajo."],
    explain=[
        "Las telecomunicaciones llevan voz, imagen y datos de un lugar a otro, por cable o por el aire. Quien trabaja en una red no parte improvisando: parte leyendo documentos. El esquema es un dibujo hecho con símbolos que muestra cómo se conectan los equipos. El plano muestra el lugar físico donde van. La lista de materiales dice qué se necesita y en qué cantidad, y la orden de trabajo dice qué tarea se pide, dónde y en qué condiciones.",
        "El sector se rige por la norma vigente; en Chile, la Subsecretaría de Telecomunicaciones (Subtel) regula este sector. Además, cada tarea tiene riesgos: el riesgo eléctrico, el trabajo en altura y los errores de documentación. Si el documento no coincide con la realidad, no se improvisa: se informa a la jefatura para que se corrija. Todo lo realizado se anota en un registro con fecha, persona y trabajo hecho.",
        f"Las tareas con energía eléctrica, torres, antenas o alturas solo las hace personal autorizado, con instructor, norma vigente y protección. {AVISO}",
    ],
    vocab=[("esquema", "dibujo con símbolos que muestra cómo se conectan los equipos"), ("plano", "dibujo del lugar físico y de dónde va cada cosa"), ("lista de materiales", "documento que dice qué se necesita y en qué cantidad"), ("orden de trabajo", "documento que dice qué tarea se pide, dónde y en qué condiciones"), ("norma vigente", "regla oficial que está en uso hoy"), ("riesgo", "posibilidad de que ocurra un daño"), ("personal autorizado", "personas con la formación y el permiso para una tarea riesgosa")],
    worked=[
        ("Elegir el documento", "Un técnico de ejemplo quiere saber cuántos conectores debe comprar para un enlace. ¿Qué documento consulta?", ["La cantidad de cada material está en un solo documento.", "Ese documento es la lista de materiales."], "La lista de materiales"),
        ("Cable que sobra", "Un enlace de ejemplo tiene un recorrido de 45 metros y se entregan 50 metros de cable. ¿Cuántos metros sobran?", ["Se resta el recorrido al cable entregado.", "50 menos 45."], "5 metros"),
    ],
    mistakes=[("Seguir el esquema aunque no coincida con lo que se ve en el lugar, para no molestar a la jefatura.", "Un documento erróneo lleva a una instalación equivocada y puede crear riesgos.", "Anota la diferencia e informa a la jefatura para corregir el documento."),
              ("Pensar que, por haber leído un cuaderno, ya se puede trabajar a gran altura o con equipos energizados.", "Esas tareas exigen instructor autorizado y norma vigente.", "Aprende los conceptos aquí y practica solo con personal autorizado.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un esquema?", "Un dibujo con símbolos que muestra cómo se conectan los equipos", "Una lista de precios de los equipos", "El contrato de trabajo del técnico", "El esquema usa símbolos para mostrar las conexiones; no es una lista de precios ni un contrato."),
        ("abc", "En Telecomunicaciones: ¿qué es una orden de trabajo?", "El documento que dice qué tarea se pide, dónde y en qué condiciones", "La factura que paga el cliente", "El manual de uso de un equipo", "La orden de trabajo define la tarea pedida; la factura y el manual cumplen otras funciones."),
        ("abc", "¿Qué institución regula el sector de las telecomunicaciones en Chile?", "La Subsecretaría de Telecomunicaciones (Subtel)", "El Servicio de Impuestos Internos", "La Dirección del Trabajo", "Subtel regula el sector; las otras instituciones tienen otras funciones."),
        ("=", "{F} Si la bodega y la oficina están unidas por un recorrido de 60 metros, ¿cuántos metros de cable sobran de los 80 metros entregados?", "80-60", "Se resta el recorrido al cable entregado.", " metros"),
        ("abc", "{F} ¿Qué documento muestra cómo se conectan los equipos de la red?", "El esquema de la red", "La lista de materiales", "La orden de trabajo", "El esquema es el dibujo de las conexiones; la lista dice cantidades y la orden dice la tarea."),
        ("abc", "{F} El recorrido está a 3 metros de altura y cerca de luminarias con energía. ¿Qué corresponde a una persona que solo estudia este cuaderno?", "Dejar esa tarea a personal autorizado con instructor y norma vigente", "Subir con una escalera prestada para avanzar más rápido", "Cortar la energía del edificio sin avisar", "Trabajar en altura o cerca de energía exige personal autorizado; improvisar crea riesgos."),
        ("=", "{F} La empresa repite el mismo trabajo en 5 sucursales idénticas, y cada una necesita los conectores y las cajas de pared de la lista. ¿Cuántas piezas de ese tipo se necesitan en total?", "5*(2+1)", "Cada sucursal usa 2 conectores y 1 caja, y eso se multiplica por 5.", " piezas"),
        ("abc", "{F} El esquema muestra un switch en la bodega, pero en el lugar no hay ninguno. ¿Qué corresponde?", "Informar a la jefatura y pedir que se corrija el documento", "Poner el equipo en otro lugar sin avisar", "Ignorar el esquema y trabajar de memoria", "Cuando un documento no coincide con el lugar se informa y se corrige."),
        ("ab", "¿Una persona que terminó este cuaderno ya puede trabajar en altura?", "No, requiere instructor autorizado y norma vigente", "Sí, porque ya conoce los símbolos", "Conocer símbolos no habilita para una tarea de riesgo; el cuaderno es solo aprendizaje conceptual."),
        ("abc", "Un técnico ve archivos personales de un cliente en un computador mientras revisa su red. ¿Qué corresponde?", "No abrirlos ni copiarlos y limitarse a lo que pide la orden de trabajo", "Copiarlos para guardarlos como respaldo", "Comentarlos con sus compañeros", "Los datos personales no se usan fuera del fin autorizado."),
        ("=", "{F} Se estima 3 horas de documentación por cada enlace y la empresa debe documentar 4 enlaces del mismo tipo. ¿Cuántas horas son en total?", "3*4", "Las horas por enlace se multiplican por los 4 enlaces.", " horas"),
        ("abc", "Al terminar un trabajo, ¿qué debe tener como mínimo el registro?", "Fecha, quién lo hizo y qué se hizo", "Solo el nombre del cliente", "Solo el precio de los materiales", "Un registro útil deja constancia de cuándo, quién y qué."),
        ("abc", "{F} De estos riesgos de la ficha, ¿cuáles dos exigen personal autorizado?", "El trabajo a 3 metros de altura y las luminarias con energía", "Un error de ortografía en la lista y un conector de más", "El color del plano y el tamaño de la hoja", "Solo la altura y la energía eléctrica son riesgos que exigen personal autorizado."),
    ],
    ctx=("abc", "En una oficina de ejemplo, el cliente dice: «mi sobrino sabe de esto, que suba él a la canaleta alta y así ahorramos». Como técnico en formación, ¿qué respondes?", "Explicar que el trabajo en altura lo hace personal autorizado y proponer pedirlo a la empresa", "Aceptar para no discutir con el cliente", "Subir tú mismo porque eres técnico en formación", "Las tareas de altura y energía exigen personal autorizado, norma y protección."),
    sc=[
        ("En Telecomunicaciones: ¿para qué sirve la lista de materiales?", "Para saber qué se necesita y en qué cantidad", "Dice los materiales y sus cantidades."),
        ("¿Qué se hace si el esquema no coincide con el lugar?", "Informar a la jefatura para corregir el documento", "No se improvisa sobre un documento erróneo."),
        ("¿Quién hace las tareas en altura o con energía?", "Personal autorizado, con instructor y norma vigente", "Este cuaderno no habilita para trabajar."),
    ],
    op=("Una escuela de ejemplo pide documentar el cableado entre la sala de computación y la biblioteca (recorrido de 35 metros; se entregan 40 metros de cable y 2 conectores). Escribe (a) los tres documentos que pedirías, (b) cuántos metros sobran, (c) un riesgo que no harías tú y quién lo haría.",
        "(a) Orden de trabajo, esquema de la red y lista de materiales (el plano también sirve). (b) 40 menos 35 son 5 metros. (c) El trabajo en altura o cerca de energía lo haría personal autorizado con instructor y norma vigente.",
        ["nombra tres documentos correctos", "calcula bien los metros que sobran", "reconoce un riesgo y a quién corresponde"],
        ["hoja con los tres documentos, el cálculo y el riesgo"],
        ["decir que ya puede subir a una torre", "restar mal los metros", "olvidar el registro"],
        "Pregunta: «¿qué haces si el esquema no coincide con lo que ves?». Si no responde, pídele que relea la regla de informar y corregir."),
    reinforce="Escribe una lista de materiales de ejemplo para conectar dos computadores con un cable y dos conectores, con sus cantidades.",
    extend="Explica con un ejemplo inventado por qué un registro del trabajo protege al técnico y al cliente.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (leyenda y plano de ejemplo, inventados). Leyenda: R = router; S = switch; P = punto de red en la pared; A = punto de acceso inalámbrico; línea continua = cable de red; "
     "línea de puntos = enlace inalámbrico. El plano está a escala 1:100: 1 cm del plano son 100 cm (1 metro) reales. En el plano, el cable de la sala de reuniones al switch mide 8 cm. "
     "Roles: técnico (ejecuta), proyectista (diseña), supervisor (revisa y autoriza) y cliente (recibe).")
build(
    O1, 2, F,
    use="Aprenderé a leer una leyenda, una escala y los documentos de un proyecto de red, y qué hace cada persona del equipo.",
    prior=["Sé qué es un esquema y una lista de materiales.", "Sé multiplicar por 100.", "Sé convertir centímetros a metros."],
    explain=[
        "El lenguaje simbólico usa símbolos en vez de palabras: un círculo, una línea o una letra representan un equipo o una conexión. La leyenda es la tabla que explica qué significa cada símbolo; sin ella un esquema no se puede leer. Un esquema bien hecho es claro, y el mismo símbolo significa lo mismo en todo el documento.",
        "El plano está dibujado a escala: una razón fija entre lo dibujado y lo real. A escala 1:100, cada centímetro del plano son 100 centímetros reales, es decir, 1 metro. Un proyecto se compone de varios documentos: planos, esquemas, especificaciones técnicas (qué características debe tener cada equipo), lista de materiales y un informe final con lo realmente construido, que se llama plano como quedó construido.",
        "Cada rol responde por algo. El proyectista diseña, el técnico ejecuta lo que dice el documento, el supervisor revisa y autoriza y el cliente recibe y firma. Nadie cambia un documento sin avisar: toda modificación se anota para que el esquema siga siendo la verdad del lugar. " + AVISO,
    ],
    vocab=[("leyenda", "tabla que explica el significado de cada símbolo"), ("símbolo", "dibujo o letra que representa un equipo o una conexión"), ("escala", "razón fija entre la medida del plano y la medida real"), ("especificación técnica", "documento con las características que debe tener un equipo"), ("proyectista", "persona que diseña el proyecto"), ("supervisor", "persona que revisa y autoriza el trabajo")],
    worked=[
        ("Leer la escala", "Plano de ejemplo a escala 1:100. Un pasillo mide 5 cm en el plano. ¿Cuánto mide en la realidad?", ["Cada centímetro del plano son 100 centímetros reales.", "5 por 100 son 500 centímetros, es decir, 5 metros."], "5 metros"),
        ("Leer un símbolo", "Una leyenda de ejemplo dice: T = teléfono; línea doble = cable de voz. En el esquema aparece una línea doble que une T con una central. ¿Qué representa esa línea?", ["La leyenda dice que la línea doble es un cable de voz.", "Une un teléfono con la central."], "Un cable de voz entre el teléfono y la central"),
    ],
    mistakes=[("Suponer que un símbolo significa lo mismo en todos los esquemas y no mirar la leyenda.", "Cada documento puede usar símbolos distintos; la leyenda manda.", "Lee siempre la leyenda antes de interpretar el esquema."),
              ("Medir el plano con la regla y usar esa medida como si fuera la real.", "La medida del plano hay que multiplicarla por la escala.", "Convierte la medida usando la escala indicada.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es una leyenda en un esquema?", "La tabla que explica el significado de los símbolos", "El título del plano", "El nombre de la empresa cliente", "Sin la leyenda no se sabe qué representa cada símbolo."),
        ("abc", "¿Qué significa una escala 1:100 en un plano?", "Que 1 cm del plano son 100 cm reales", "Que el plano mide 100 cm de ancho", "Que hay 100 equipos dibujados", "La escala relaciona la medida del plano con la medida real."),
        ("abc", "¿Qué rol revisa y autoriza el trabajo antes de entregarlo?", "El supervisor", "El proyectista al diseñar", "El cliente al pagar", "El supervisor revisa y autoriza; el proyectista diseña."),
        ("abc", "{F} En la leyenda, ¿qué representa la línea de puntos?", "Un enlace inalámbrico", "Un cable de red", "Un punto de red en la pared", "La leyenda indica que la línea de puntos es un enlace inalámbrico."),
        ("=", "{F} Si el cable de la sala de reuniones al switch mide 8 cm en el plano, ¿cuántos metros mide en la realidad?", "8*100//100", "Cada centímetro del plano son 100 cm reales; se pasa a metros dividiendo por 100.", " metros"),
        ("abc", "{F} ¿Qué letra de la leyenda representa un punto de acceso inalámbrico?", "A", "S", "P", "La leyenda asigna A al punto de acceso inalámbrico; S es el switch y P el punto de red."),
        ("=", "A escala 1:100, un salón mide 12 cm de largo en el plano. ¿Cuántos metros mide en la realidad?", "12*100//100", "Se multiplica por 100 los centímetros del plano y se pasa a metros.", " metros"),
        ("abc", "{F} El técnico nota que el cliente movió el switch a otra pared. ¿Qué debe hacer con el esquema?", "Anotar el cambio para que el esquema refleje el lugar real", "Dejarlo igual porque ya fue aprobado", "Borrar el switch del esquema", "Toda modificación se anota para que el esquema siga siendo la verdad."),
        ("abc", "Un proyecto de ejemplo incluye: planos, esquemas, especificaciones técnicas y lista de materiales. ¿Qué documento dice qué características debe tener un equipo?", "La especificación técnica", "La lista de materiales", "El plano", "La especificación técnica describe las características exigidas a cada equipo."),
        ("abc", "Un esquema de ejemplo usa un círculo con una X, pero no trae leyenda. ¿Qué corresponde?", "Pedir la leyenda antes de interpretar el símbolo", "Suponer que es un teléfono", "Suponer que es una antena", "Sin leyenda no se puede interpretar un símbolo con certeza."),
        ("=", "{F} Un pasillo mide 15 cm en el plano de la ficha. ¿Cuántos metros mide en la realidad?", "15*100//100", "La escala 1:100 convierte cada centímetro del plano en un metro real.", " metros"),
        ("abc", "El técnico termina su trabajo y quiere dar por aprobado él mismo su propio trabajo. ¿Qué rol corresponde que lo revise y autorice?", "El supervisor", "El mismo técnico", "El proyectista de otra empresa", "Nadie aprueba su propio trabajo; lo revisa y autoriza el supervisor."),
        ("abc", "{F} Un plano a escala 1:100 mide 20 cm de ancho. Una persona dice que el edificio mide 20 metros de ancho. ¿Es correcto?", "Sí, porque 20 cm del plano son 20 metros reales", "No, porque son 20 centímetros reales", "No, porque son 200 metros reales", "Con 1:100 cada centímetro es 1 metro, así que 20 cm equivalen a 20 metros."),
    ],
    ctx=("abc", "Un proyectista de ejemplo entrega un esquema sin leyenda y con dos símbolos distintos para el switch. ¿Qué corresponde al técnico?", "Pedir que se agregue la leyenda y se unifique el símbolo antes de trabajar", "Elegir el símbolo que le parezca mejor", "Dibujar un esquema nuevo por su cuenta", "El técnico solicita corrección del documento; no lo reinterpreta."),
    sc=[
        ("En Telecomunicaciones: ¿para qué sirve la leyenda?", "Para saber qué significa cada símbolo", "Define los símbolos de ese documento."),
        ("A escala 1:100, ¿cuántos metros reales son 3 cm del plano?", "3 metros", "Cada centímetro del plano es 1 metro real."),
        ("¿Qué rol diseña el proyecto?", "El proyectista", "El técnico ejecuta y el supervisor revisa."),
    ],
    op=("Un taller de ejemplo tiene un plano a escala 1:100. El cable del router al switch mide 6 cm; del switch a la sala de atención, 9 cm. Escribe (a) los metros reales de cada tramo y el total, (b) qué documento dice las características del switch y (c) quién debe autorizar el trabajo terminado.",
        "(a) 6 cm son 6 metros y 9 cm son 9 metros; el total es 15 metros. (b) La especificación técnica. (c) El supervisor.",
        ["convierte con la escala", "suma los tramos", "nombra el documento y el rol correctos"],
        ["hoja con las conversiones, el total y las dos respuestas"],
        ["no convertir a metros", "olvidar la escala", "decir que el técnico se autoriza a sí mismo"],
        "Pregunta: «¿cuántos metros reales son 4 cm de este plano?». Si no sabe, pídele que use la regla de la escala."),
    reinforce="Dibuja un esquema de ejemplo con un router, un switch y dos computadores, y escribe su leyenda.",
    extend="Explica con un ejemplo inventado qué problema aparece si el plano y el lugar real no coinciden.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Esquema en texto de la «Clínica Veterinaria Pata Azul» (ficticia): Router R1 ── Switch S1. Desde S1 salen cuatro cables: a P1 (recepción), P2 (consulta 1), P3 (consulta 2) y al punto de acceso A1 (sala de espera). "
     "Longitudes de ejemplo de cada cable desde S1: P1 12 m, P2 18 m, P3 25 m, A1 30 m. Lista de materiales entregada: cable 80 m, 4 conectores, 1 switch, 1 router, 1 punto de acceso.")
build(
    O1, 3, F,
    use="Aprenderé a analizar en papel un esquema y su lista de materiales, para comprobar que coinciden y detectar lo que falta.",
    prior=["Sé leer una leyenda y una escala.", "Sé qué es un esquema y una lista de materiales.", "Sé sumar longitudes."],
    explain=[
        "Analizar un caso en papel es comparar documentos entre sí. Del esquema se cuenta cuántos equipos y cuántos cables hay; de la lista de materiales se lee qué se compró. Si el esquema muestra más de lo que trae la lista, falta material. Si la lista trae más que el esquema, sobra, y hay que anotarlo para no comprar de más.",
        "En una red en estrella, todos los equipos se conectan con su propio cable a un equipo central, el switch. Un switch es el equipo que reparte la conexión entre los dispositivos de una red local. Un router conecta esa red local con otra red, como internet. Para saber cuánto cable se necesita se suman los tramos y se agrega una reserva (holgura) para curvas y errores; la cantidad de reserva la define el proyecto.",
        "Toda diferencia se anota en el informe y se informa a la jefatura antes de actuar. El análisis termina con una conclusión escrita que dice qué coincide, qué falta y qué se propone, con los números a la vista para que otra persona pueda comprobarlo. Este análisis es solo de documentos; instalar equipos exige personal autorizado. " + AVISO,
    ],
    vocab=[("red en estrella", "red donde cada equipo se conecta con su propio cable a un equipo central"), ("switch", "equipo que reparte la conexión entre los dispositivos de una red local"), ("router", "equipo que conecta una red local con otra red, como internet"), ("punto de acceso", "equipo que da conexión inalámbrica a la red"), ("holgura", "reserva de cable para curvas y errores"), ("conclusión", "resultado escrito del análisis con sus números")],
    worked=[
        ("Sumar tramos", "Un esquema de ejemplo tiene tres cables desde un switch: 10 m, 15 m y 20 m. ¿Cuánto cable se necesita sin reserva?", ["Se suman los tres tramos.", "10 más 15 más 20."], "45 metros"),
        ("Comparar con la lista", "El esquema de ejemplo muestra 6 puntos de red y la lista trae 5 conectores. ¿Qué pasa?", ["Se compara lo que pide el esquema con lo comprado.", "Faltan 6 menos 5, es decir, 1 conector."], "Falta 1 conector"),
    ],
    mistakes=[("Contar los equipos del esquema pero no comprobar la lista de materiales.", "Se puede comprar de menos y detener el trabajo.", "Compara siempre la cantidad del esquema con la de la lista."),
              ("Dar la cantidad de cable sin sumar los tramos y sin pedir la reserva que define el proyecto.", "El cable justo no deja margen para errores o curvas.", "Suma los tramos y agrega la holgura que indique el proyecto.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué hace un switch?", "Reparte la conexión entre los dispositivos de una red local", "Conecta la red local con internet", "Entrega una cuenta de correo a cada usuario", "El switch reparte la conexión local; el router la une con otra red."),
        ("abc", "¿Qué hace un router?", "Conecta la red local con otra red, como internet", "Reparte la conexión solo entre computadores de una sala", "Almacena los planos del proyecto", "El router comunica redes distintas entre sí, a diferencia del switch."),
        ("abc", "En una red en estrella, ¿cómo se conecta cada equipo?", "Con su propio cable al equipo central", "Todos comparten un único cable en cadena", "Sin cable, solo por radio", "En la estrella cada equipo tiene su propio cable al centro."),
        ("=", "{F} ¿Cuántos metros de cable suman los cuatro tramos desde el switch?", "12+18+25+30", "Se suman las longitudes de los cuatro cables.", " metros"),
        ("abc", "{F} ¿Cuántos conectores pide el esquema si cada cable necesita uno en cada extremo hacia un equipo y se cuentan solo los de los extremos de los cuatro cables?", "8", "4", "6", "Cuatro cables con un conector en cada extremo son 4 por 2, es decir, 8."),
        ("abc", "{F} Hay 4 conectores en la lista. ¿Qué conclusión corresponde si el esquema pide 8?", "Faltan 4 conectores", "Sobran 4 conectores", "La lista está completa", "El esquema pide 8 y la lista trae 4, así que faltan 4."),
        ("=", "{F} El cable entregado es de 80 metros. ¿Cuántos metros faltan para cubrir los cuatro tramos?", "(12+18+25+30)-80", "Se resta el cable entregado al total de los tramos.", " metros"),
        ("abc", "{F} En el esquema, ¿cuántos equipos se conectan directamente al switch?", "4", "5", "3", "Salen cuatro cables: P1, P2, P3 y A1."),
        ("abc", "{F} ¿Qué equipo de la lista da la conexión inalámbrica a la sala de espera?", "El punto de acceso", "El router", "El switch", "El punto de acceso entrega la conexión inalámbrica."),
        ("abc", "Un esquema muestra 5 cables y la lista trae cable para 4 tramos iguales de 10 metros. ¿Cuántos metros faltan?", "10 metros", "5 metros", "No falta cable", "Para 5 tramos de 10 metros hacen falta 50, y hay 40, así que faltan 10."),
        ("=", "{F} Se pide una holgura de ejemplo de 10 metros en total. ¿Cuántos metros de cable se necesitan sumando tramos y holgura?", "12+18+25+30+10", "A la suma de los tramos se agrega la reserva pedida.", " metros"),
        ("abc", "{F} El técnico nota que la lista no trae un cable para el punto A1 y compra uno por su cuenta sin avisar. ¿Qué principio se rompe?", "Toda diferencia se informa a la jefatura antes de actuar", "El switch debe tener más de cuatro cables", "El plano debe estar en color", "Las diferencias entre documentos se informan para decidir con autorización."),
        ("abc", "{F} Una persona concluye: «el cable alcanza porque 80 es mayor que 25». ¿Cuál es su error?", "Comparó con un solo tramo en vez de con la suma de los cuatro", "Sumó los conectores", "Olvidó que el router no lleva cable", "Se debe comparar con el total de tramos, que es 85, y el cable entregado es 80."),
    ],
    ctx=("abc", "El supervisor de ejemplo pregunta: «¿alcanza el material para la clínica?». Tú sumaste 85 metros de tramos y la lista trae 80. ¿Qué respondes?", "Que faltan 5 metros y que propones pedirlos antes de comenzar", "Que alcanza porque falta poco", "Que no sabes y esperas que el cliente lo resuelva", "El análisis entrega números claros y una propuesta."),
    sc=[
        ("En Telecomunicaciones: ¿qué hace el router?", "Conecta la red local con otra red", "El switch solo reparte dentro de la red local."),
        ("¿Qué se suma para saber el cable total?", "Todos los tramos más la holgura", "Los tramos y la reserva del proyecto dan el total."),
        ("¿Qué haces con una diferencia entre esquema y lista?", "La anotas e informas a la jefatura", "No se actúa sobre la red sin autorización del responsable."),
    ],
    op=("Un consultorio de ejemplo tiene un switch conectado a 3 computadores con cables de 7 m, 14 m y 20 m y a una impresora con un cable de 9 m. La lista trae 45 metros de cable y 6 conectores. Escribe (a) el total de metros de tramos, (b) si alcanza el cable y cuánto sobra o falta, (c) cuántos conectores pide el esquema si cada cable lleva uno en cada extremo y si alcanzan.",
        "(a) 7 más 14 más 20 más 9 son 50 metros. (b) No alcanza: faltan 5 metros. (c) 4 cables por 2 extremos son 8 conectores; con 6 faltan 2.",
        ["suma bien los tramos", "compara con la lista y concluye", "calcula los conectores y los compara"],
        ["hoja con las tres sumas y la conclusión"],
        ["comparar con un solo tramo", "olvidar los dos extremos", "comprar sin avisar"],
        "Pregunta: «¿cuántos extremos tiene cada cable?». Si no responde, pídele que dibuje un cable con sus dos puntas."),
    reinforce="Cuenta los cables y los conectores de un esquema de ejemplo con un switch y cinco computadores, y compara con una lista inventada.",
    extend="Explica con un ejemplo inventado por qué se deja una holgura de cable en un proyecto.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). El «Liceo Cumbres» (ficticio) planifica una red en un pasillo con 14 puntos de red. Datos de ejemplo del proyecto: cada punto usa 18 metros de cable en promedio; se agrega una reserva de 10 % (valor de ejemplo del proyecto); "
     "el cable viene en rollos de 305 metros; cada punto lleva 1 caja de pared y 2 conectores; los switches de ejemplo tienen 24 puertos. Referencia de ejemplo: un enlace de cable de cobre no debe superar 100 metros en total (verifica el valor en la norma del proyecto).")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular materiales, verificar límites y justificar la decisión por escrito.",
    prior=["Sé leer una lista de materiales y una escala.", "Sé calcular un porcentaje simple.", "Sé multiplicar y comparar cantidades."],
    explain=[
        "El criterio técnico se aplica con números. Primero se calcula la cubicación: cuánto de cada material hace falta. Para el cable se multiplica el largo promedio por la cantidad de puntos y se agrega la reserva que define el proyecto. Un porcentaje se calcula así: 10 % de una cantidad es esa cantidad dividida por 10. Luego se compara con lo que se vende, como rollos de largo fijo, y se compra la cantidad entera de rollos necesaria.",
        "Después se verifican los límites. Un enlace de cable de cobre tiene un largo máximo que fija la norma del proyecto (aquí, 100 metros de ejemplo); si un tramo lo supera, se busca otra solución, como un segundo switch más cerca. También se verifican las puertas: un switch de 24 puertos admite 24 conexiones, y conviene dejar puertos libres para crecer.",
        "La decisión se escribe con los datos que la respaldan: cálculos, límites revisados y quién autoriza. Si el cálculo exige comprar de más, se explica. El resultado se entrega a la jefatura; la instalación la hace personal autorizado con la norma vigente. " + AVISO,
    ],
    vocab=[("cubicación", "cálculo de la cantidad de cada material que hace falta"), ("reserva", "porcentaje extra de material que fija el proyecto"), ("rollo", "unidad de venta del cable, de largo fijo"), ("largo máximo", "distancia que un enlace no debe superar"), ("puerto", "entrada de un switch para conectar un cable"), ("criterio técnico", "regla basada en datos para decidir")],
    worked=[
        ("Cable con reserva", "Un proyecto de ejemplo tiene 10 puntos de 20 metros cada uno y reserva de 10 %. ¿Cuántos metros de cable se necesitan?", ["Sin reserva: 10 por 20 son 200 metros.", "La reserva es 20 metros; el total es 220 metros."], "220 metros"),
        ("Rollos necesarios", "Se necesitan 400 metros y el rollo trae 305. ¿Cuántos rollos se compran?", ["Un rollo no alcanza porque 305 es menor que 400.", "Con dos rollos hay 610 metros, que alcanzan."], "2 rollos"),
    ],
    mistakes=[("Comprar exactamente el cable sin reserva porque «así sale justo».", "Un error de corte o una curva dejan el cable corto.", "Aplica la reserva que define el proyecto."),
              ("Comprar un rollo parcial: «305 es casi 340».", "Los rollos se venden enteros; si no alcanza, hay que comprar otro rollo.", "Calcula cuántos rollos enteros hacen falta.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la cubicación de materiales?", "El cálculo de la cantidad de cada material que hace falta", "El dibujo del plano a escala", "El permiso de la jefatura para comprar", "La cubicación calcula cantidades; el plano y el permiso son otras cosas."),
        ("abc", "¿Cuánto es el 10 % de 340?", "34", "3,4", "340", "El 10 % de una cantidad es esa cantidad dividida por 10."),
        ("abc", "¿Qué se hace si un enlace de cobre supera el largo máximo del proyecto?", "Buscar otra solución, como acercar un switch", "Instalarlo igual para ahorrar", "Cambiar el máximo en el documento para que calce", "Los límites se respetan; si no se cumplen se busca una alternativa."),
        ("=", "{F} ¿Cuántos metros de cable se necesitan sin la reserva?", "14*18", "Se multiplica el largo promedio por la cantidad de puntos.", " metros"),
        ("=", "{F} ¿Cuántos metros son la reserva del 10 %?", "14*18//10", "La reserva es el 10 % del cable sin reserva.", " metros"),
        ("=", "{F} ¿Cuántos metros de cable se necesitan en total con reserva?", "14*18+14*18//10", "Al cable sin reserva se le suma la reserva del 10 %.", " metros"),
        ("abc", "{F} Se necesitan 277 metros con reserva. ¿Cuántos rollos de 305 metros hay que comprar?", "1 rollo", "2 rollos", "3 rollos", "Un rollo de 305 metros alcanza para 277 metros."),
        ("=", "{F} ¿Cuántas cajas de pared y conectores se necesitan en total para los 14 puntos (sumando las cajas y los conectores)?", "14*(1+2)", "Cada punto lleva 1 caja y 2 conectores; eso se multiplica por 14.", " piezas"),
        ("abc", "{F} Un tramo del proyecto mide 120 metros hasta el último punto. ¿Qué corresponde según la referencia de la ficha?", "No cumple el máximo de 100 metros; hay que buscar otra solución", "Cumple porque 120 es mayor que 100", "No es necesario revisar el tramo", "El tramo supera el máximo de ejemplo y debe resolverse de otra forma."),
        ("=", "{F} Se usarán 14 puertos de un switch. ¿Cuántos puertos quedan libres en un switch de 24 puertos?", "24-14", "Se resta lo usado a los puertos del switch.", " puertos"),
        ("abc", "{F} El proyecto crecerá con 15 puntos más. ¿Basta un solo switch de 24 puertos para 29 puntos?", "No, porque 29 es mayor que 24", "Sí, porque los puertos libres alcanzan para 29", "Sí, porque un switch admite tantos puntos como cables lleguen", "Con 29 conexiones se superan los 24 puertos disponibles."),
        ("abc", "Una persona calcula 14 por 18, obtiene 252 y declara «necesito 252 metros». ¿Qué falta?", "Agregar la reserva del proyecto y revisar los rollos", "Dividir por 14", "Sumar los conectores", "El cálculo sin reserva ni rollos enteros es incompleto."),
        ("abc", "El técnico en formación ve que sobra mucho material en el cálculo y decide no avisar. ¿Qué corresponde?", "Anotarlo y explicarlo en el informe a la jefatura", "Quedarse con el material", "Reducir la cantidad en el documento sin avisar", "Las diferencias se informan y justifican por escrito."),
    ],
    ctx=("abc", "El director de un liceo de ejemplo pregunta si basta un solo rollo de cable para su proyecto de 14 puntos. Tú calculaste 277 metros con reserva. ¿Qué respondes?", "Que sí alcanza un rollo de 305 metros, y que sobran unos 28 metros", "Que no alcanza y hay que comprar dos rollos", "Que no se puede calcular sin ir al lugar", "277 es menor que 305, así que alcanza; la sobra es 305 menos 277, es decir, 28."),
    sc=[
        ("En Telecomunicaciones: ¿qué es la reserva en un cálculo de cable?", "Un porcentaje extra que fija el proyecto", "Cubre las curvas del recorrido y los errores de corte."),
        ("¿Cuántos puertos libres quedan si se usan 10 de 24?", "14", "Se restan los puertos usados a los 24 puertos del switch: 24 menos 10 son 14."),
        ("¿Quién instala una vez aprobado el cálculo?", "Personal autorizado con la norma vigente", "El cuaderno no habilita para instalar."),
    ],
    op=("Una biblioteca de ejemplo necesita 12 puntos de red de 15 metros cada uno, con reserva de 10 % (valor de ejemplo). El cable viene en rollos de 305 metros y los switches tienen 16 puertos. Calcula (a) los metros con reserva, (b) los rollos, (c) si un switch de 16 puertos alcanza para 12 puntos y cuántos puertos quedan libres, y escribe una frase de conclusión para la jefatura.",
        "(a) 12 por 15 son 180 metros; la reserva es 18; el total es 198 metros. (b) 1 rollo, porque 305 alcanza. (c) Sí, quedan 4 puertos libres. Conclusión: con un rollo y un switch de 16 puertos alcanza y quedan 4 puertos para crecer.",
        ["calcula cable y reserva", "decide los rollos y los puertos", "escribe una conclusión con números"],
        ["hoja con los cálculos y la conclusión"],
        ["olvidar la reserva", "comprar rollos parciales", "no revisar los puertos libres"],
        "Pregunta: «¿por qué conviene que sobren puertos?». Si no sabe, pídele que piense en más puntos en el futuro."),
    reinforce="Calcula los metros de cable con reserva de 10 % para 8 puntos de 25 metros cada uno.",
    extend="Explica con un ejemplo inventado qué datos mínimos debe llevar una conclusión técnica para que otra persona la pueda verificar.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (cadena de comunicación de ejemplo, inventada). Una radio comunitaria ficticia, «Radio Los Pinos», describe su cadena en papel: micrófono → mesa de mezcla → transmisor → enlace por el aire → repetidor → "
     "receptor de la escuela → amplificador → parlante. Tipos de señal de ejemplo: voz (en la mesa de mezcla), datos (en el panel de control) e imagen (en una cámara que transmite por cable). Todos los valores son de ejemplo.")
build(
    O2, 1, F,
    use="Aprenderé la cadena de una comunicación (generar, transmitir, repetir, amplificar, recibir, distribuir) y por qué instalar estos equipos exige personal autorizado.",
    prior=["Sé que una señal lleva voz, imagen o datos.", "Sé leer un esquema simple.", "Sé qué es un riesgo."],
    explain=[
        "Un sistema de telecomunicaciones lleva información de un punto a otro. Se divide en etapas: la generación crea la señal (un micrófono convierte voz en señal eléctrica); la transmisión la envía por un cable o por el aire; la repetición la recibe y la reenvía para llegar más lejos; la amplificación la hace más fuerte; la recepción la capta; y la distribución la reparte a varios destinos. La señal puede llevar voz, imagen o datos.",
        "Cada etapa pierde un poco de señal y puede sumar ruido, que son perturbaciones no deseadas. Por eso hay repetidores y amplificadores: para que la señal llegue con calidad. Las especificaciones técnicas del proyecto dicen qué equipo va en cada etapa, y la solicitud de trabajo dice qué se debe instalar y dónde. Las frecuencias y las potencias permitidas en el aire las regula la autoridad, por ejemplo la Subsecretaría de Telecomunicaciones (Subtel), según la norma vigente.",
        f"Instalar estos equipos puede implicar energía eléctrica, antenas, torres y trabajo en altura. {AVISO} Aquí solo se aprende el vocabulario y se leen cadenas en papel, sin pasos de instalación.",
    ],
    vocab=[("generación", "etapa donde se crea la señal"), ("transmisión", "etapa donde la señal se envía por cable o por el aire"), ("repetición", "etapa donde se recibe y se reenvía la señal para llegar más lejos"), ("amplificación", "etapa donde la señal se hace más fuerte"), ("recepción", "etapa donde la señal se capta"), ("distribución", "etapa donde la señal se reparte a varios destinos"), ("ruido", "perturbación no deseada en la señal")],
    worked=[
        ("Nombrar la etapa", "En una cadena de ejemplo, un equipo capta la señal que viene por el aire. ¿En qué etapa está?", ["La etapa que capta la señal es la recepción.", "No la crea ni la reparte, solo la capta."], "Recepción"),
        ("Para qué sirve un repetidor", "Una señal de ejemplo llega muy débil al final de un enlace largo. ¿Qué equipo ayudaría a que llegue más lejos?", ["Un repetidor recibe y reenvía la señal.", "Un amplificador la hace más fuerte."], "Un repetidor o un amplificador"),
    ],
    mistakes=[("Pensar que todo equipo de telecomunicaciones se instala igual de fácil y que basta leer el manual.", "Hay equipos con energía eléctrica, antenas y alturas que exigen personal autorizado.", "Aprende el concepto y deja la práctica para personal autorizado con instructor."),
              ("Confundir amplificación con transmisión.", "Amplificar hace más fuerte la señal; transmitir es enviarla.", "Pregunta en cada etapa: ¿crea, envía, reenvía, refuerza, capta o reparte?")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué hace la etapa de generación?", "Crea la señal, por ejemplo convirtiendo voz en señal eléctrica", "Reparte la señal a varios destinos", "Hace más fuerte la señal", "La generación origina la señal; repartir es distribución y reforzar es amplificación."),
        ("abc", "En Telecomunicaciones: ¿qué es el ruido?", "Una perturbación no deseada que se suma a la señal", "La señal de voz de la radio", "El equipo que repite la señal", "El ruido es lo que no se desea y perjudica la calidad."),
        ("abc", "¿Qué etapa envía la señal por un cable o por el aire?", "La transmisión", "La recepción", "La amplificación", "Transmitir es enviar la señal; recibir es captarla."),
        ("abc", "{F} En la cadena de la radio, ¿qué equipo hace de repetidor?", "El repetidor entre el transmisor y el receptor de la escuela", "El micrófono", "El parlante", "La ficha pone un repetidor que reenvía la señal en el camino."),
        ("abc", "{F} ¿En qué etapa está el micrófono?", "Generación", "Recepción", "Distribución", "El micrófono crea la señal eléctrica a partir de la voz."),
        ("abc", "{F} ¿Qué equipo de la cadena refuerza la señal antes del parlante?", "El amplificador", "El transmisor", "La mesa de mezcla", "El amplificador hace más fuerte la señal antes del parlante."),
        ("=", "{F} La cadena nombra los equipos micrófono, mesa de mezcla, transmisor, repetidor, receptor, amplificador y parlante. ¿Cuántos equipos son?", "1+1+1+1+1+1+1", "Se cuenta cada equipo nombrado en la cadena.", " equipos"),
        ("abc", "{F} ¿Qué tipo de señal lleva la cámara que transmite por cable?", "Imagen", "Voz", "Datos del panel", "La ficha dice que la cámara entrega señal de imagen."),
        ("abc", "{F} Un aficionado propone subir a una torre cercana para instalar el repetidor sin permiso. ¿Qué corresponde?", "Dejar esa tarea a personal autorizado con norma vigente y protección", "Subir si lleva herramientas", "Pedir ayuda a un amigo sin formación", "Trabajo en altura, energía y antenas exigen personal autorizado."),
        ("abc", "Una señal de ejemplo sale del transmisor con buena calidad y llega al receptor con mucho ruido. ¿Qué etapa convendría revisar en el papel?", "El enlace por el aire y si hace falta un repetidor", "El parlante del estudio", "El color del micrófono", "El ruido se suma en el camino de la señal, por lo que se revisa el enlace."),
        ("=", "Un enlace de ejemplo cubre 20 kilómetros con un repetidor a mitad de camino. ¿Cuántos kilómetros hay desde el transmisor hasta el repetidor?", "20//2", "El repetidor está a la mitad, así que se divide el total en dos.", " kilómetros"),
        ("abc", "¿Quién fija las frecuencias y potencias que se pueden usar en el aire?", "La autoridad según la norma vigente, como Subtel", "Cada técnico según su criterio", "El cliente que paga la obra", "El uso del aire está regulado por la autoridad."),
        ("abc", "Una escuela de ejemplo pide transmitir la clase por voz e imagen a otra sala. ¿Qué señales debe contemplar el proyecto?", "Voz e imagen", "Solo datos de un archivo", "Ninguna, porque no hay equipos", "Voz e imagen son los dos tipos de señal pedidos."),
    ],
    ctx=("abc", "Una junta de vecinos de ejemplo quiere instalar una antena en el techo de un edificio y pide ayuda a un estudiante de Telecomunicaciones. ¿Qué responde el estudiante?", "Que puede explicar los conceptos en papel, pero la instalación debe hacerla personal autorizado", "Que él mismo la instala, porque estudió el tema", "Que no sabe nada del tema", "Estudiar conceptos no habilita para trabajar en altura ni con antenas."),
    sc=[
        ("En Telecomunicaciones: ¿qué hace un repetidor?", "Recibe y reenvía la señal para llegar más lejos", "Evita que la señal se pierda en un enlace largo."),
        ("¿Qué etapa capta la señal?", "La recepción", "La recepción es el final del enlace."),
        ("¿Quién hace tareas con antenas y alturas?", "Personal autorizado, con instructor y norma vigente", "El cuaderno no habilita para trabajar."),
    ],
    op=("Una escuela de ejemplo quiere que la voz del director, grabada con un micrófono en la dirección, se escuche en tres salas. Dibuja o escribe una cadena con las seis etapas (generación, transmisión, repetición, amplificación, recepción y distribución) con un equipo de ejemplo en cada una, e indica una tarea del proyecto que no harías sin personal autorizado.",
        "Generación: micrófono. Transmisión: transmisor. Repetición: repetidor. Amplificación: amplificador. Recepción: receptor. Distribución: reparto a los parlantes de las tres salas. Tarea para personal autorizado: instalar antenas o trabajar en altura o con energía eléctrica.",
        ["nombra las seis etapas en orden", "pone un equipo de ejemplo en cada etapa", "reconoce una tarea que exige personal autorizado"],
        ["hoja con la cadena de seis etapas y la tarea"],
        ["confundir amplificar con transmitir", "saltarse una etapa", "decir que él mismo subiría a la antena"],
        "Pregunta: «¿qué hace cada equipo con la señal?». Si no responde, pídele que recorra la cadena de principio a fin."),
    reinforce="Escribe la cadena de un teléfono celular de ejemplo, de quien habla hasta quien escucha, con las etapas que reconoces.",
    extend="Explica con un ejemplo inventado por qué una señal de voz necesita amplificación en un enlace largo.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (hoja de datos de ejemplo, inventada). Equipo «Amplificador AX» (nombre de ejemplo): ganancia 12 dB; pérdida del cable en el tramo 8 dB; "
     "frecuencia de trabajo 100 MHz (de ejemplo). Documentos del proyecto: solicitud de trabajo, especificación técnica, hoja de datos, protocolo de pruebas y acta de entrega. "
     "Roles: instalador, supervisor, ingeniero proyectista y cliente.")
build(
    O2, 2, F,
    use="Aprenderé el vocabulario de señales (frecuencia, ancho de banda, dB), los documentos y los roles del trabajo con equipos de señal.",
    prior=["Sé las etapas de una cadena de comunicación.", "Sé sumar y restar números.", "Sé que una señal puede ser de voz, imagen o datos."],
    explain=[
        "La frecuencia mide cuántas veces por segundo se repite una onda; su unidad es el hercio (Hz). Un kilohercio (kHz) son 1.000 Hz, un megahercio (MHz) son 1.000 kHz y un gigahercio (GHz) son 1.000 MHz. El ancho de banda es el rango de frecuencias que ocupa una señal: a más ancho de banda, más información por segundo.",
        "La ganancia dice cuánto aumenta la señal un amplificador; la atenuación o pérdida dice cuánto se debilita en un cable o en un tramo. Ambas se miden en decibeles (dB) y se pueden sumar y restar: una ganancia de 12 dB y una pérdida de 8 dB dejan una ganancia neta de 12 menos 8, es decir, 4 dB. Una señal puede ser analógica (varía de forma continua) o digital (se representa con valores como 0 y 1).",
        f"La hoja de datos es el documento del fabricante con las características de un equipo; la especificación técnica dice qué se exige en el proyecto. La solicitud de trabajo pide la tarea; el protocolo de pruebas lista las comprobaciones que se hacen antes de entregar. El instalador ejecuta, el supervisor revisa, el ingeniero proyectista diseña y el cliente recibe en el acta de entrega. {AVISO}",
    ],
    vocab=[("hercio (Hz)", "unidad de frecuencia: repeticiones por segundo"), ("megahercio (MHz)", "un millón de hercios"), ("ancho de banda", "rango de frecuencias que ocupa una señal"), ("decibel (dB)", "unidad para ganancia y pérdida de señal, que se suma y se resta"), ("ganancia", "cuánto aumenta la señal un equipo"), ("atenuación", "cuánto se debilita la señal en un tramo"), ("hoja de datos", "documento del fabricante con las características de un equipo")],
    worked=[
        ("Ganancia neta", "Un amplificador de ejemplo da 15 dB y un cable pierde 6 dB. ¿Cuál es la ganancia neta?", ["Se resta la pérdida a la ganancia.", "15 menos 6."], "9 dB"),
        ("Convertir frecuencias", "Una señal de ejemplo tiene 2 MHz. ¿Cuántos kHz son?", ["Un MHz son 1.000 kHz.", "2 por 1.000."], "2.000 kHz"),
    ],
    mistakes=[("Calcular la ganancia neta usando solo la ganancia del amplificador e ignorando la pérdida del cable.", "La señal también se debilita en el cable, y eso se resta.", "Anota ganancias con signo más y pérdidas con signo menos y suma todo."),
              ("Confundir la hoja de datos del fabricante con la especificación técnica del proyecto.", "La hoja dice lo que el equipo puede hacer; la especificación, lo que el proyecto exige.", "Compara la hoja de datos con la especificación para ver si el equipo sirve.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué mide la frecuencia?", "Cuántas veces por segundo se repite una onda", "Cuántos metros mide un cable", "Cuántos equipos tiene la red", "La frecuencia se mide en hercios, que son repeticiones por segundo."),
        ("abc", "En Telecomunicaciones: ¿qué es la atenuación?", "Cuánto se debilita la señal en un tramo", "Cuánto aumenta la señal un amplificador", "El rango de frecuencias de una señal", "La atenuación es una pérdida; la ganancia, un aumento."),
        ("abc", "¿Cuántos Hz son 1 kHz?", "1.000 Hz", "100 Hz", "1.000.000 Hz", "El prefijo kilo significa mil, por eso 1 kHz son 1.000 Hz."),
        ("=", "{F} ¿Cuál es la ganancia neta del tramo, en dB, si se resta la pérdida del cable a la ganancia del amplificador?", "12-8", "La ganancia neta es la ganancia menos la pérdida.", " dB"),
        ("=", "{F} ¿Cuántos kHz son los 100 MHz de la frecuencia de trabajo?", "100*1000", "Un MHz son 1.000 kHz.", " kHz"),
        ("abc", "{F} ¿Qué documento del fabricante trae la ganancia del Amplificador AX?", "La hoja de datos", "El acta de entrega", "La solicitud de trabajo", "La hoja de datos reúne las características del equipo."),
        ("=", "Un tramo de ejemplo tiene dos cables que pierden 5 dB y 7 dB y un amplificador que da 20 dB. ¿Cuál es la ganancia neta del tramo, en dB?", "20-5-7", "Se resta cada pérdida a la ganancia.", " dB"),
        ("abc", "Una señal de ejemplo se representa solo con valores 0 y 1. ¿Cómo se llama?", "Señal digital", "Señal analógica", "Señal de ruido", "La señal con valores como 0 y 1 es digital."),
        ("abc", "{F} El cliente firma una constancia de que recibió el sistema. ¿Qué documento firma?", "El acta de entrega", "La hoja de datos", "El protocolo de pruebas", "El acta de entrega deja constancia de la recepción."),
        ("abc", "{F} El proyecto exige una ganancia neta de al menos 6 dB en el tramo. ¿Cumple el Amplificador AX con el cable de la ficha?", "No, porque la ganancia neta es 4 dB", "Sí, porque su ganancia es 12 dB", "Sí, porque 8 dB es mayor que 6", "Con 12 menos 8 la ganancia neta es 4 dB, que no llega a 6."),
        ("=", "Una señal de ejemplo ocupa de 88 MHz a 92 MHz. ¿Cuántos MHz de ancho de banda ocupa?", "92-88", "El ancho de banda es la diferencia entre la frecuencia mayor y la menor.", " MHz"),
        ("abc", "Un instalador de ejemplo cree que la especificación del proyecto puede cambiarse si el equipo no cumple. ¿Qué corresponde?", "Informar al supervisor y al proyectista para decidir el cambio", "Cambiar la especificación por su cuenta", "Instalar el equipo igual", "Los cambios de especificación los decide quien diseña con autorización."),
        ("abc", "¿Quién diseña el proyecto y fija qué equipo va en cada etapa?", "El ingeniero proyectista", "El instalador", "El cliente al recibir", "El proyectista diseña; el instalador ejecuta."),
    ],
    ctx=("abc", "Un técnico de ejemplo calcula que el amplificador ofrece 4 dB netos, pero el proyecto pide 6 dB. ¿Qué hace en el papel?", "Informar la diferencia y proponer un equipo con más ganancia, a decidir por el proyectista", "Escribir 6 dB en el informe para que cumpla", "Eliminar el cable del esquema", "No se alteran los datos: se informa y se propone."),
    sc=[
        ("En Telecomunicaciones: ¿en qué unidad se miden ganancia y atenuación?", "En decibeles (dB)", "Se suman cuando son ganancias y se restan cuando son pérdidas."),
        ("¿Cuántos MHz son 5.000 kHz?", "5 MHz", "Como 1.000 kHz son 1 MHz, 5.000 kHz son 5 MHz."),
        ("¿Quién recibe y firma el acta de entrega?", "El cliente", "El acta deja constancia de la entrega."),
    ],
    op=("Un tramo de ejemplo tiene un cable de 6 dB de pérdida, un amplificador de 14 dB de ganancia y otro cable de 3 dB de pérdida. El proyecto exige 5 dB netos como mínimo. Calcula la ganancia neta, di si cumple, convierte los 450 MHz de la frecuencia de trabajo a kHz y nombra el documento donde se registra la entrega al cliente.",
        "Ganancia neta: 14 menos 6 menos 3 son 5 dB, así que cumple justo. 450 MHz son 450.000 kHz. La entrega se registra en el acta de entrega.",
        ["calcula la ganancia neta", "convierte MHz a kHz", "nombra el documento"],
        ["hoja con los cálculos y las respuestas"],
        ["sumar las pérdidas", "multiplicar por 100", "confundir la hoja de datos con el acta"],
        "Pregunta: «¿restas o sumas las pérdidas?». Si no responde, pídele que escriba cada valor con su signo."),
    reinforce="Calcula la ganancia neta de un amplificador de 18 dB con un cable que pierde 10 dB.",
    extend="Explica con un ejemplo inventado por qué los dB permiten sumar ganancias y pérdidas en una sola cuenta.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (presupuesto de enlace de ejemplo, inventado). Enlace de una antena de la «Cooperativa Valle Sur» (ficticia) hasta una sala. Nivel de señal al salir del equipo: 10 dBm. "
     "Ganancia de la antena transmisora: +12 dB. Pérdida en el aire (distancia): -90 dB. Ganancia de la antena receptora: +10 dB. Pérdida en cables y conectores del receptor: -4 dB. "
     "El receptor necesita al menos -70 dBm para funcionar bien (sensibilidad de ejemplo). Todos los valores son inventados.")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel un presupuesto de enlace: sumar ganancias y pérdidas en dB para ver si la señal llega con nivel suficiente.",
    prior=["Sé qué son ganancia, atenuación y dB.", "Sé sumar números positivos y negativos.", "Sé las etapas de una cadena de comunicación."],
    explain=[
        "El presupuesto de enlace es la cuenta que sigue el nivel de la señal desde que sale del equipo hasta que llega al receptor. Se parte del nivel de salida en dBm, que es una forma de expresar la potencia en referencia a un milivatio, y se suman las ganancias y se restan las pérdidas, todo en dB. El resultado es el nivel de recepción, también en dBm.",
        "El receptor tiene una sensibilidad: el nivel mínimo con el que funciona bien. Si el nivel de recepción es mayor o igual que la sensibilidad, el enlace llega; si es menor, no. La diferencia entre ambos es el margen. En números negativos, -60 es mayor que -70, porque está más cerca de cero. Un margen positivo ayuda a soportar días de lluvia, obstáculos o equipos envejecidos.",
        f"Este análisis se hace en papel con datos de ejemplo. Elegir potencias y frecuencias reales depende del fabricante, del proyecto y de la autoridad (Subtel, según la norma vigente), y montar antenas exige personal autorizado. {AVISO}",
    ],
    vocab=[("presupuesto de enlace", "cuenta de ganancias y pérdidas desde la salida hasta la recepción"), ("dBm", "forma de expresar potencia en referencia a un milivatio"), ("nivel de recepción", "nivel de señal con que llega la señal al receptor"), ("sensibilidad", "nivel mínimo con que el receptor funciona bien"), ("margen", "diferencia entre el nivel de recepción y la sensibilidad")],
    worked=[
        ("Nivel de recepción", "Un enlace de ejemplo sale con 5 dBm, gana 10 dB, pierde 60 dB y gana 8 dB. ¿Cuál es el nivel de recepción?", ["Se suma 5 más 10 más 8 y se resta 60.", "5 más 10 más 8 son 23; 23 menos 60 son -37."], "-37 dBm"),
        ("Margen", "El nivel de recepción de ejemplo es -37 dBm y la sensibilidad es -60 dBm. ¿Cuál es el margen?", ["El margen es el nivel menos la sensibilidad.", "-37 menos (-60) son 23."], "23 dB"),
    ],
    mistakes=[("Creer que -80 es mayor que -70 porque 80 es mayor que 70.", "En los números negativos, el que está más cerca de cero es mayor.", "Ubica los valores en una recta numérica antes de comparar."),
              ("Sumar la pérdida en el aire como si fuera una ganancia.", "La pérdida resta nivel de señal.", "Escribe cada pérdida con signo menos.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es la sensibilidad de un receptor?", "El nivel mínimo con el que funciona bien", "La distancia máxima de cable", "La potencia del transmisor", "La sensibilidad es el nivel mínimo de señal que el receptor necesita."),
        ("abc", "En Telecomunicaciones: ¿qué calcula el presupuesto de enlace?", "El nivel de señal con que llega al receptor", "El precio total del proyecto", "El número de personas del equipo", "Suma ganancias y resta pérdidas para obtener el nivel de recepción."),
        ("abc", "¿Cuál de estos valores es mayor?", "-60", "-70", "-80", "-60 es el más cercano a cero y, por eso, el mayor."),
        ("=", "{F} ¿Cuál es el nivel de recepción, en dBm?", "10+12-90+10-4", "Se suman las ganancias y se restan las pérdidas a partir del nivel de salida.", " dBm"),
        ("abc", "{F} El receptor necesita al menos -70 dBm. ¿El enlace de la ficha llega con nivel suficiente?", "Sí, porque -62 dBm es mayor que -70 dBm", "No, porque 62 es menor que 70", "No, porque hay pérdida en el aire", "-62 está más cerca de cero que -70, así que supera la sensibilidad."),
        ("=", "{F} ¿Cuál es el margen, en dB, entre el nivel de recepción y la sensibilidad?", "(10+12-90+10-4)+70", "El margen es el nivel de recepción menos la sensibilidad, es decir, -62 más 70.", " dB"),
        ("abc", "Un enlace de ejemplo sale con 0 dBm y gana 20 dB, pierde 100 dB y gana 15 dB. ¿Cuál es el nivel de recepción?", "-65 dBm", "-35 dBm", "135 dBm", "0 más 20 más 15 menos 100 da -65."),
        ("=", "{F} Si la pérdida en el aire sube a 95 dB por una distancia mayor, ¿cuál es el nuevo nivel de recepción?", "10+12-95+10-4", "Se repite la cuenta con la nueva pérdida en el aire.", " dBm"),
        ("abc", "{F} Con la pérdida en el aire de 95 dB, el nivel de recepción es -67 dBm. ¿Cuál es el margen respecto de -70 dBm?", "3 dB", "-3 dB", "137 dB", "-67 menos (-70) es 3, un margen pequeño pero positivo."),
        ("abc", "{F} Una compañera dice: «sumé los 90 dB porque está en la ficha». ¿Cuál es su error?", "Sumó una pérdida en vez de restarla", "Olvidó la ganancia de la antena", "Cambió dBm por kilómetros", "La pérdida en el aire resta nivel de señal."),
        ("=", "Un enlace de ejemplo tiene un nivel de recepción de -58 dBm y una sensibilidad de -75 dBm. ¿Cuál es el margen, en dB?", "-58+75", "El margen es el nivel menos la sensibilidad.", " dB"),
        ("abc", "{F} Se quiere más margen en el enlace de la ficha. ¿Qué alternativa en papel lo mejora sin cambiar la distancia?", "Elegir una antena con más ganancia", "Poner una antena con menos ganancia", "Alargar el cable del receptor", "Más ganancia suma nivel de señal; más cable agrega pérdida."),
        ("abc", "El estudiante de ejemplo propone, para mejorar el margen, montar una antena más alta en una torre sin avisar a nadie. ¿Qué corresponde?", "No hacerlo: el trabajo en altura lo hace personal autorizado con norma vigente", "Subir con ayuda de un amigo", "Hacerlo de noche para que nadie lo vea", "El cuaderno es conceptual; las alturas exigen personal autorizado."),
    ],
    ctx=("abc", "El jefe de proyecto de ejemplo recibe un cálculo que da un margen de -4 dB. ¿Qué indica ese resultado?", "Que el enlace no llega con el nivel necesario y hay que rediseñar en papel", "Que el enlace funciona con mucha holgura", "Que el receptor no existe", "Un margen negativo significa que la señal llega por debajo de la sensibilidad."),
    sc=[
        ("En Telecomunicaciones: ¿qué se obtiene al sumar ganancias y restar pérdidas desde la salida?", "El nivel de recepción", "Es el nivel de señal en el receptor."),
        ("¿Qué es mayor: -50 o -65?", "-50", "Entre los números negativos, el que está más cerca de cero es el mayor."),
        ("¿Quién fija las potencias que se pueden usar en el aire?", "La autoridad según la norma vigente", "Las potencias reales no se inventan."),
    ],
    op=("Un enlace de ejemplo para una escuela rural sale con 8 dBm. Datos: antena transmisora +10 dB, pérdida en el aire -85 dB, antena receptora +9 dB, cables y conectores -5 dB. La sensibilidad del receptor es -72 dBm. Calcula (a) el nivel de recepción, (b) el margen y (c) si el enlace llega, y propón una mejora en papel si el margen es menor que 5 dB.",
        "(a) 8 más 10 menos 85 más 9 menos 5 son -63 dBm. (b) -63 menos (-72) son 9 dB. (c) Llega, y el margen de 9 dB es mayor que 5 dB, por lo que no hace falta mejora; si fuera menor se propondría una antena con más ganancia.",
        ["suma ganancias y resta pérdidas", "calcula el margen", "concluye si llega y propone mejora si corresponde"],
        ["hoja con la cuenta, el margen y la conclusión"],
        ["sumar las pérdidas", "comparar mal los negativos", "no concluir"],
        "Pregunta: «¿por qué -63 es mayor que -72?». Si no sabe, pídele que ubique ambos en una recta numérica."),
    reinforce="Calcula el nivel de recepción de un enlace que sale con 3 dBm, gana 6 dB, pierde 70 dB y gana 6 dB.",
    extend="Explica con un ejemplo inventado por qué conviene dejar un margen positivo en un enlace.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (criterio técnico con datos de ejemplo, inventados). Un edificio ficticio necesita repartir una señal de televisión por cable a 4 oficinas. Nivel de la señal a la entrada del edificio: 0 dBm (valor de ejemplo). "
     "Un divisor de 1 a 4 pierde 7 dB (de ejemplo); cada tramo de cable hacia una oficina pierde 4 dB; un amplificador da 12 dB. Nivel mínimo para cada oficina: -12 dBm.")
build(
    O2, 4, F,
    use="Aprenderé a decidir en papel si una distribución de señal necesita amplificación, calculando niveles con datos de ejemplo.",
    prior=["Sé sumar ganancias y restar pérdidas en dB.", "Sé qué es un nivel mínimo o sensibilidad.", "Sé qué es la distribución de señal."],
    explain=[
        "Distribuir una señal es repartirla a varios destinos. El equipo que la reparte se llama divisor: tiene una entrada y varias salidas, y cada salida recibe menos señal, por lo que el divisor tiene una pérdida (más salidas, más pérdida). El criterio técnico exige calcular el nivel que llega a cada destino y compararlo con el nivel mínimo que necesita.",
        "Para decidir si hace falta un amplificador se hace la cuenta sin él. Si el nivel que llega a cada oficina es menor que el mínimo, se agrega un amplificador y se repite la cuenta. Hay un cuidado más: demasiada señal también puede dañar o deformar la señal de un equipo receptor, así que el nivel no debe superar el máximo que indica la hoja de datos. La decisión se escribe con los datos que la respaldan.",
        f"Todo este trabajo se hace en papel con datos de ejemplo: instalar divisores, cables y amplificadores en un edificio exige personal autorizado y norma vigente, y puede implicar energía eléctrica y alturas. {AVISO}",
    ],
    vocab=[("divisor", "equipo que reparte una señal en varias salidas y le resta nivel a cada una"), ("distribución", "reparto de una señal a varios destinos"), ("nivel mínimo", "nivel con que el destino funciona bien"), ("nivel máximo", "nivel que el equipo no debe superar"), ("criterio técnico", "regla basada en cálculos para decidir")],
    worked=[
        ("Nivel a una oficina", "Una señal de ejemplo entra con 2 dBm, el divisor pierde 6 dB y el cable pierde 3 dB. ¿Cuál es el nivel que llega?", ["Se restan las dos pérdidas al nivel de entrada.", "2 menos 6 menos 3 son -7."], "-7 dBm"),
        ("Decidir si falta amplificador", "El nivel que llega es -7 dBm y el mínimo es -10 dBm. ¿Falta amplificador?", ["-7 está más cerca de cero que -10.", "Entonces supera el mínimo."], "No falta amplificador"),
    ],
    mistakes=[("Calcular solo el cable y olvidar la pérdida del divisor.", "El divisor resta nivel a cada salida.", "Suma todas las pérdidas de la cadena, incluida la del divisor."),
              ("Agregar un amplificador sin revisar el nivel máximo del receptor.", "Un nivel demasiado alto también deforma la señal.", "Compara el resultado con el mínimo y con el máximo de la hoja de datos.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué hace un divisor de señal?", "Reparte una señal en varias salidas y resta nivel a cada una", "Amplifica la señal sin pérdidas", "Convierte la voz en señal eléctrica", "El divisor reparte y, por eso, cada salida recibe menos nivel."),
        ("abc", "¿Qué pasa con la pérdida de un divisor si tiene más salidas?", "Aumenta", "Disminuye", "Desaparece", "Con más salidas, cada una recibe una parte menor de la señal."),
        ("abc", "¿Cuál es un riesgo de dar demasiada señal a un receptor?", "Que se deforme la señal", "Que se gaste menos cable", "Que baje la pérdida del divisor", "Un exceso de nivel puede deformar la señal."),
        ("=", "{F} ¿Cuál es el nivel que llega a una oficina, en dBm, sin amplificador?", "0-7-4", "Se restan la pérdida del divisor y la del cable al nivel de entrada.", " dBm"),
        ("abc", "{F} Sin amplificador llega -11 dBm. ¿Cumple el mínimo de -12 dBm?", "Sí, porque -11 es mayor que -12", "No, porque 11 es menor que 12", "No, porque falta un cable", "-11 está más cerca de cero que -12, así que supera el mínimo."),
        ("abc", "{F} Para una oficina más lejana, el cable pierde 6 dB en vez de 4 dB. ¿Cuál es su nivel sin amplificador?", "-13 dBm", "-11 dBm", "-17 dBm", "0 menos 7 menos 6 da -13."),
        ("abc", "{F} Con -13 dBm y un mínimo de -12 dBm, ¿qué corresponde?", "Agregar un amplificador y repetir la cuenta", "Dejarlo así, porque está cerca", "Quitar el divisor sin avisar", "Se debe cumplir el mínimo; -13 queda por debajo."),
        ("=", "{F} Con el amplificador de 12 dB para la oficina lejana, ¿cuál es el nuevo nivel, en dBm?", "-13+12", "La ganancia se suma al nivel de -13 dBm.", " dBm"),
        ("abc", "{F} La hoja de datos de una televisión de ejemplo dice que su nivel máximo es 2 dBm. ¿Cumple un nivel de -1 dBm?", "Sí, porque -1 es menor que 2", "No, porque -1 es menor que el mínimo", "No, porque es negativo", "-1 está por debajo del máximo de 2 y sobre el mínimo del ejemplo."),
        ("=", "En otro caso de ejemplo la señal entra con 3 dBm, el divisor pierde 10 dB y el cable pierde 5 dB. ¿Cuál es el nivel que llega, en dBm?", "3-10-5", "Se restan las pérdidas al nivel de entrada.", " dBm"),
        ("abc", "Con el último caso de ejemplo (-12 dBm), si el mínimo del receptor es -15 dBm, ¿hace falta un amplificador?", "No, porque -12 supera el mínimo de -15", "Sí, porque -12 es menor que -15", "Sí, porque hay un divisor", "-12 está más cerca de cero que -15."),
        ("abc", "Una persona propone dar una ganancia enorme «para estar seguros». ¿Cuál es el problema?", "Puede superar el nivel máximo y deformar la señal", "Desaparece la pérdida del divisor", "Se reduce el número de oficinas", "El exceso de nivel también es un defecto."),
        ("abc", "{F} El técnico de ejemplo quiere ir al techo del edificio a ajustar el amplificador, «porque es rápido». ¿Qué corresponde?", "Dejar el trabajo en altura a personal autorizado y seguir la norma vigente", "Ir con una escalera y sin avisar", "Pedirle a un vecino que lo haga", "El cuaderno no habilita para trabajar en altura ni con energía."),
    ],
    ctx=("abc", "Una administradora de ejemplo pregunta si basta un divisor para dar señal a 4 oficinas. El cálculo da -11 dBm, mínimo -12 dBm. ¿Qué respondes?", "Que sí alcanza con poco margen y que conviene dejar el cálculo respaldado en un informe", "Que no se puede saber", "Que alcanza porque 11 es mayor que 12", "El resultado cumple el mínimo; se informa con el margen y los datos."),
    sc=[
        ("En Telecomunicaciones: ¿qué se hace primero para decidir si falta un amplificador?", "Calcular el nivel sin amplificador", "La cuenta decide si se cumple el mínimo."),
        ("¿Qué pasa con la señal en un divisor?", "Cada salida recibe menos nivel", "Todo divisor tiene una pérdida que se resta al nivel de cada salida."),
        ("¿Quién instala los equipos del edificio?", "Personal autorizado, con norma vigente", "El cuaderno no habilita para instalar."),
    ],
    op=("Un hospital de ejemplo reparte una señal de entrada de 4 dBm a 2 salas. Un divisor de 1 a 2 pierde 4 dB y cada cable pierde 5 dB; el mínimo de cada sala es -10 dBm y el máximo es 3 dBm. Calcula el nivel que llega, di si cumple el mínimo y el máximo y, si no cumple, propón qué equipo del papel agregarías.",
        "4 menos 4 menos 5 son -5 dBm. Cumple el mínimo (-5 es mayor que -10) y el máximo (-5 es menor que 3). No hace falta amplificador. Si no cumpliera, se agregaría un amplificador y se repetiría la cuenta.",
        ["resta las pérdidas desde la entrada", "compara con mínimo y máximo", "concluye con una propuesta si no cumple"],
        ["hoja con la cuenta y la conclusión"],
        ["olvidar la pérdida del divisor", "comparar mal los negativos", "no revisar el máximo"],
        "Pregunta: «¿qué dos límites debes revisar al final?». Si no responde, pídele que lea la ficha del hospital."),
    reinforce="Calcula el nivel que llega a una sala si entran 1 dBm y el divisor pierde 7 dB y el cable 2 dB.",
    extend="Explica con un ejemplo inventado por qué más salidas en un divisor significan menos nivel por salida.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 9 (oficina de ejemplo, inventada). La empresa ficticia «Contadores del Sur Ltda.» tiene 8 computadores y 1 servidor de archivos en una red local (LAN). "
     "Hay una persona encargada de informática, una gerente y 6 funcionarios. Datos de ejemplo del servidor: nombre SRV-ARCHIVOS, guarda las carpetas de los clientes (datos personales). "
     "Pendiente: instalar un sistema operativo nuevo en 2 computadores. Todo es de ejemplo.")
build(
    O3, 1, F,
    use="Aprenderé qué es un sistema operativo, qué es una red LAN y qué cuidados de calidad y seguridad exige incorporar un equipo a una red.",
    prior=["Sé qué es un computador y una red.", "Sé qué es una cuenta de usuario.", "Sé qué es un dato personal."],
    explain=[
        "Un sistema operativo es el programa principal de un computador: administra sus recursos y permite usar otros programas. Una red LAN (red de área local) conecta computadores y otros equipos cercanos, como los de una oficina. Para que un computador se incorpore a la LAN hay que instalar y configurar bien el sistema operativo: nombre del equipo, cuentas de usuario, dirección de red, actualizaciones y protección.",
        "La calidad y la seguridad se cuidan con reglas: usar solo programas con licencia, mantener el sistema actualizado, crear una cuenta por persona con los permisos mínimos que necesita, tener antivirus y cortafuegos (firewall, un filtro que controla el tráfico) y hacer respaldos. Las contraseñas son personales y secretas: nunca se escriben en un papel pegado ni se comparten, y en estos ejercicios nunca se usan contraseñas reales.",
        "Los equipos de una empresa guardan datos personales de clientes y trabajadores, que se protegen según la norma vigente. Todo cambio se anota en un registro: qué equipo, quién lo hizo, cuándo y con qué autorización. Todo se razona aquí en papel; configurar los equipos de una organización real requiere autorización de su responsable. " + AVISO,
    ],
    vocab=[("sistema operativo", "programa principal que administra el computador y permite usar otros programas"), ("red LAN", "red local que conecta equipos cercanos, como los de una oficina"), ("cuenta de usuario", "identidad personal para entrar a un equipo o a la red"), ("permisos mínimos", "solo los permisos que el trabajo necesita"), ("cortafuegos", "filtro que controla el tráfico que entra y sale"), ("respaldo", "copia de los datos para recuperarlos si algo falla")],
    worked=[
        ("Cuentas y permisos", "En una oficina de ejemplo trabajan 5 personas y cada una necesita su propia cuenta. ¿Cuántas cuentas de usuario hacen falta, sin contar la de administración?", ["Se crea una cuenta por persona.", "5 personas, 5 cuentas."], "5 cuentas"),
        ("Qué dato proteger", "Una carpeta de ejemplo contiene nombres y teléfonos de clientes. ¿Qué tipo de dato es?", ["Identifican personas.", "Son datos personales."], "Datos personales"),
    ],
    mistakes=[("Dar a todos los funcionarios la misma cuenta con todos los permisos para «ahorrar tiempo».", "No se sabe quién hizo cada cambio y se amplía el daño de un error.", "Crea una cuenta por persona con permisos mínimos."),
              ("Dejar una contraseña anotada en un papel pegado en la pantalla.", "Cualquiera que pase puede usarla.", "Guarda las contraseñas en secreto y no las compartas.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un sistema operativo?", "El programa principal que administra el computador", "Un cable para conectar a la red", "Una carpeta con datos de clientes", "El sistema operativo administra los recursos del computador."),
        ("abc", "En Telecomunicaciones: ¿qué es una red LAN?", "Una red local que conecta equipos cercanos", "La red mundial de internet", "Un programa antivirus", "LAN significa red de área local."),
        ("abc", "¿Para qué sirve un cortafuegos?", "Para controlar el tráfico que entra y sale", "Para guardar una copia de los datos", "Para ampliar el espacio del disco", "El cortafuegos filtra el tráfico de red."),
        ("=", "{F} ¿Cuántas personas necesitan cuenta de usuario si son una encargada de informática, una gerente y los 6 funcionarios?", "1+1+6", "Se cuenta una cuenta por persona.", " personas"),
        ("abc", "{F} ¿Qué datos de SRV-ARCHIVOS exigen especial cuidado según la norma vigente?", "Las carpetas de clientes con datos personales", "El nombre SRV-ARCHIVOS", "El número de computadores", "Los datos personales se protegen según la norma vigente."),
        ("abc", "{F} Una funcionaria pide a la encargada de informática que le comparta su contraseña «por si acaso». ¿Qué corresponde?", "No compartirla: las contraseñas son personales y secretas", "Compartirla porque es de confianza", "Escribirla en un papel visible", "Una contraseña compartida impide saber quién hace qué."),
        ("=", "{F} El sistema nuevo se instalará en 2 de los 8 computadores. ¿Cuántos computadores quedan con el sistema antiguo?", "8-2", "Se resta a los computadores los que se actualizan.", " computadores"),
        ("abc", "¿Qué práctica reduce el riesgo de perder datos si falla un disco?", "Hacer respaldos", "Usar la misma contraseña en todo", "Desactivar el cortafuegos", "El respaldo permite recuperar los datos."),
        ("abc", "{F} Antes de instalar el sistema nuevo en los 2 computadores, ¿qué corresponde?", "Pedir autorización a la gerente y respaldar los datos", "Instalar directamente para no perder tiempo", "Borrar las carpetas de clientes", "La autorización y el respaldo son parte de la calidad y la seguridad."),
        ("abc", "Un funcionario descarga un instalador desde un enlace que le llegó por mensaje. ¿Qué corresponde?", "No instalarlo y avisar a la encargada de informática", "Instalarlo porque ya está descargado", "Enviarlo a todos los compañeros", "Un instalador de origen dudoso puede traer programas maliciosos."),
        ("=", "Un registro de ejemplo anota 3 cambios en cada uno de los 4 equipos revisados. ¿Cuántos cambios se anotaron en total?", "3*4", "Se multiplican los cambios por equipo por los equipos revisados.", " cambios"),
        ("abc", "{F} ¿Qué debe anotar la encargada de informática en el registro tras actualizar un equipo?", "Qué equipo, quién lo hizo, cuándo y con qué autorización", "Solo la fecha", "Solo el nombre de la gerente", "Un registro útil permite saber qué pasó y quién autorizó."),
        ("abc", "{F} Una persona propone dar a todo el personal acceso a las carpetas de todos los clientes. ¿Qué principio se rompe?", "El de permisos mínimos", "El de actualizar el sistema", "El de hacer respaldos", "Cada persona accede solo a lo que su trabajo necesita."),
    ],
    ctx=("abc", "La gerente de una oficina de ejemplo pide instalar rápido un sistema operativo en un computador nuevo, sin respaldo ni registro. ¿Qué responde la encargada de informática?", "Explica el riesgo y propone un plan breve con respaldo, autorización y registro", "Acepta sin decir nada", "Se niega sin dar razones", "Se informa el riesgo, se propone una alternativa y se deja constancia."),
    sc=[
        ("En Telecomunicaciones: ¿qué es una red LAN?", "Una red local de equipos cercanos", "Conecta los equipos de un mismo lugar."),
        ("¿Qué permisos recibe cada usuario?", "Los mínimos que su trabajo necesita", "Así se reduce el daño de errores."),
        ("¿Se comparte una contraseña?", "No, es personal y secreta", "Compartirla impide saber quién hizo qué."),
    ],
    op=("Una clínica de ejemplo tiene 5 computadores y 1 servidor en su red local. Hay 1 administrador, 2 recepcionistas, 1 doctora y 1 enfermero. Escribe (a) cuántas cuentas de persona hacen falta, (b) qué cuidado tendrías con las fichas de pacientes y (c) tres reglas de seguridad para un equipo nuevo que se incorpora a la red.",
        "(a) 5 cuentas, una por persona. (b) Las fichas son datos personales sensibles: permisos mínimos, acceso solo del personal autorizado y respaldo. (c) Por ejemplo: sistema actualizado con licencia, antivirus y cortafuegos, y contraseña personal secreta.",
        ["calcula las cuentas", "cuida los datos personales", "nombra tres reglas de seguridad"],
        ["hoja con las tres respuestas"],
        ["compartir cuentas", "dejar sin protección las fichas", "no anotar el cambio"],
        "Pregunta: «¿por qué no una cuenta para todos?». Si no responde, pídele que piense en cómo sabrías quién cometió un error."),
    reinforce="Escribe tres reglas para crear una contraseña personal sin usar datos reales tuyos y sin compartirla.",
    extend="Explica con un ejemplo inventado por qué una red local necesita respaldos.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 10 (ficha de configuración de ejemplo, inventada). Equipo: PC-VENTAS-02 (nombre de ejemplo). Datos de ejemplo de la red de la oficina: dirección de red 192.168.10.0; máscara 255.255.255.0; "
     "puerta de enlace (el router) 192.168.10.1; servidor DNS 192.168.10.2. El equipo PC-VENTAS-02 recibe su dirección por DHCP (automática). Roles: administrador de red, usuario y soporte técnico. "
     "Documentos: inventario de equipos, ficha de configuración y política de seguridad.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario de la configuración de una red: dirección IP, máscara, puerta de enlace, DNS y DHCP, y los documentos y roles que se usan.",
    prior=["Sé qué es una red LAN y un sistema operativo.", "Sé leer una tabla.", "Sé qué es una cuenta de usuario."],
    explain=[
        "Cada equipo de una red tiene una dirección IP: un número, como 192.168.10.25, que lo identifica en la red. La máscara de red (por ejemplo 255.255.255.0) indica qué parte de la dirección corresponde a la red y qué parte al equipo. La puerta de enlace es el equipo, normalmente el router, por donde sale el tráfico hacia otras redes. El DNS traduce nombres, como un sitio web, a direcciones IP. El DHCP es el servicio que entrega direcciones automáticas a los equipos.",
        "Las direcciones que empiezan con 192.168 se usan en redes privadas, dentro de una organización. Dos equipos no pueden tener la misma dirección IP en una misma red, porque se confunde a quién va el tráfico. Una dirección puede ser fija (la fija una persona, útil para servidores) o automática (la entrega el DHCP, útil para equipos de usuarios).",
        "Los documentos del trabajo son el inventario (lista de equipos), la ficha de configuración (los datos de cada equipo) y la política de seguridad (las reglas de la organización). El administrador de red configura y cuida la red, el usuario la usa y el soporte técnico atiende los problemas. Todo cambio se anota en el registro. " + AVISO,
    ],
    vocab=[("dirección IP", "número que identifica un equipo en una red"), ("máscara de red", "número que separa la parte de red de la parte de equipo en la dirección"), ("puerta de enlace", "equipo por donde sale el tráfico hacia otras redes"), ("DNS", "servicio que traduce nombres a direcciones IP"), ("DHCP", "servicio que entrega direcciones automáticas"), ("inventario", "lista de los equipos de la organización"), ("política de seguridad", "reglas de seguridad de la organización")],
    worked=[
        ("Identificar un dato", "Una ficha de ejemplo dice: puerta de enlace 192.168.10.1. ¿Qué equipo suele tener esa dirección?", ["La puerta de enlace es por donde sale el tráfico a otras redes.", "Normalmente es el router."], "El router"),
        ("Dirección repetida", "Dos computadores de una misma red de ejemplo tienen la IP 192.168.10.30. ¿Qué problema hay?", ["Cada dirección debe ser única en la red.", "El tráfico no sabe a cuál de los dos ir."], "Conflicto de direcciones: una IP repetida"),
    ],
    mistakes=[("Poner la misma IP fija en dos equipos «porque son parecidos».", "Una IP repetida produce conflictos y fallas de conexión.", "Asigna una IP distinta a cada equipo o usa DHCP."),
              ("Confundir la puerta de enlace con el servidor DNS.", "La puerta de enlace da salida a otras redes y el DNS traduce nombres.", "Pregunta qué hace cada dato en la ficha.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es una dirección IP?", "Un número que identifica un equipo en una red", "La contraseña de un usuario", "El nombre del fabricante del equipo", "La dirección IP identifica un equipo dentro de una red."),
        ("abc", "En Telecomunicaciones: ¿qué hace el DNS?", "Traduce nombres a direcciones IP", "Entrega direcciones automáticas a los equipos", "Reparte la señal por cable", "El DNS traduce nombres a direcciones; el DHCP entrega direcciones."),
        ("abc", "¿Qué hace el DHCP?", "Entrega direcciones automáticas a los equipos", "Traduce nombres a direcciones", "Respalda los datos", "DHCP asigna direcciones de forma automática."),
        ("abc", "{F} ¿Cuál es la puerta de enlace de la red de ejemplo?", "192.168.10.1", "192.168.10.2", "255.255.255.0", "La ficha dice que la puerta de enlace es 192.168.10.1."),
        ("abc", "{F} ¿Cómo recibe su dirección PC-VENTAS-02?", "Por DHCP, de forma automática", "Fija, puesta por una persona", "No tiene dirección", "La ficha indica que recibe su dirección por DHCP."),
        ("abc", "{F} ¿Qué documento reúne los datos de configuración de un equipo concreto?", "La ficha de configuración", "El inventario", "La política de seguridad", "La ficha de configuración describe un equipo; el inventario lista equipos."),
        ("=", "{F} El inventario anota 8 computadores, 1 servidor, 1 impresora y 1 router. ¿Cuántos equipos son?", "8+1+1+1", "Se suman los equipos del inventario.", " equipos"),
        ("abc", "{F} Dos equipos de la red tienen la IP 192.168.10.50. ¿Qué se debe hacer?", "Cambiar la IP de uno para que sea única", "Dejarlas porque el DNS lo corrige", "Cambiar la máscara a cero", "Cada IP debe ser única en la red."),
        ("abc", "Una dirección 192.168.10.7 con máscara 255.255.255.0 y otra 192.168.20.9 con la misma máscara. ¿Están en la misma red?", "No, porque cambia el tercer número de la dirección", "Sí, porque ambas empiezan con 192", "Sí, porque tienen la misma máscara", "Con esa máscara los tres primeros números definen la red; son distintos."),
        ("abc", "¿Qué rol atiende los problemas de los usuarios con sus equipos?", "El soporte técnico", "El proveedor de internet", "La gerencia", "El soporte técnico atiende las fallas de los usuarios."),
        ("abc", "{F} El administrador quiere que PC-VENTAS-02 tenga siempre la dirección 192.168.10.25. ¿Qué debe hacer?", "Cambiarla a dirección fija o reservarla en el DHCP", "Dejarla por DHCP sin reserva", "Usar la dirección del router", "Con DHCP sin reserva la dirección puede cambiar; una dirección fija o reservada se mantiene."),
        ("abc", "{F} Un usuario de ejemplo pide a soporte cambiar la política de seguridad para no cambiar contraseñas. ¿Qué corresponde?", "Explicar que la política la fija la organización y no se cambia por pedido personal", "Cambiar la política en su computador", "Borrar el documento", "La política es un documento de la organización con reglas para todos."),
        ("abc", "El administrador de red pega la lista de direcciones IP de todos los equipos en un sitio público para «ayudar a otros». ¿Qué corresponde?", "No publicar información interna de la red", "Publicarla si no hay datos de personas", "Enviarla por mensaje a desconocidos", "La información de la red es interna y sirve a quien quiera atacarla."),
    ],
    ctx=("abc", "Un usuario de ejemplo se queja de que no puede entrar a ningún sitio, pero ve los archivos del servidor local. Mirando la ficha, la puerta de enlace está en blanco. ¿Qué dato falta?", "La puerta de enlace, por donde sale el tráfico hacia otras redes", "El nombre del usuario", "La máscara del servidor", "Sin puerta de enlace el equipo no sale de la red local."),
    sc=[
        ("En Telecomunicaciones: ¿qué traduce el DNS?", "Nombres a direcciones IP", "Así se llega a un sitio por su nombre."),
        ("¿Pueden dos equipos tener la misma IP en una red?", "No", "Se produce un conflicto de direcciones."),
        ("¿Qué entrega direcciones automáticas?", "El DHCP", "El DHCP evita tener que asignar a mano cada dirección automática."),
    ],
    op=("Una biblioteca de ejemplo tiene la red 192.168.5.0 con máscara 255.255.255.0 y puerta de enlace 192.168.5.1. Tiene 3 computadores públicos, 1 impresora y 1 servidor. Escribe (a) una tabla con una IP de ejemplo distinta para cada equipo (de 192.168.5.10 en adelante), (b) cuáles dejarías fijas y cuáles por DHCP y (c) un dato de la ficha que no publicarías.",
        "(a) Computador 1: .10; computador 2: .11; computador 3: .12; impresora: .20; servidor: .30. (b) Fijas: servidor e impresora. DHCP: los computadores públicos. (c) No publicaría la lista de direcciones IP internas.",
        ["asigna IP distintas", "decide fijas y automáticas", "nombra un dato interno que no se publica"],
        ["tabla con cinco IP y la decisión"],
        ["repetir una IP", "poner IP fuera de la red", "publicar datos internos"],
        "Pregunta: «¿por qué el servidor debe tener IP fija?». Si no responde, pídele que piense en cómo lo encontrarían los demás equipos."),
    reinforce="Escribe tres direcciones IP de ejemplo distintas para una red 192.168.1.0 y la puerta de enlace en 192.168.1.1.",
    extend="Explica con un ejemplo inventado por qué un servidor suele tener una IP fija.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 11 (caso de ejemplo, inventado). Red de la «Notaría Los Aromos» (ficticia): red 192.168.30.0 con máscara 255.255.255.0 y puerta de enlace 192.168.30.1. "
     "Equipos configurados en papel: PC-A IP 192.168.30.11; PC-B IP 192.168.30.12; PC-C IP 192.168.30.12; PC-D IP 192.168.40.13; PC-E IP 192.168.30.14 con puerta de enlace en blanco. "
     "Además, el PC-B tiene el cortafuegos desactivado y una cuenta compartida por tres personas.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel una configuración de red y a detectar errores de dirección, de seguridad y de cuentas.",
    prior=["Sé qué son la IP, la máscara y la puerta de enlace.", "Sé qué es el cortafuegos.", "Sé qué es una cuenta con permisos mínimos."],
    explain=[
        "Revisar una configuración en papel es comparar cada equipo con las reglas de la red. Primero se verifica que la IP pertenezca a la red (con máscara 255.255.255.0, los tres primeros números deben ser iguales al de la red). Luego, que no esté repetida, y que la puerta de enlace esté puesta y sea la correcta. Un error en cualquiera de estos datos deja al equipo sin comunicarse bien.",
        "Después se revisa la seguridad: el cortafuegos debe estar activo, el sistema actualizado y cada persona debe tener su propia cuenta con permisos mínimos. Una cuenta compartida por varias personas impide saber quién hizo cada cosa. También se verifica que no haya contraseñas escritas a la vista.",
        "El resultado del análisis es una lista de hallazgos: qué está mal, por qué y qué corregir. Los hallazgos se informan al administrador de red y se anotan en el registro; no se corrige nada en una red real sin autorización. Este caso es de papel con datos inventados. " + AVISO,
    ],
    vocab=[("hallazgo", "error o riesgo encontrado al revisar"), ("conflicto de IP", "dos equipos con la misma dirección en una red"), ("misma red", "equipos cuyas direcciones comparten la parte de red"), ("cuenta compartida", "cuenta usada por varias personas, lo que impide saber quién hizo cada cosa")],
    worked=[
        ("IP fuera de la red", "En una red de ejemplo 10.0.1.0 con máscara 255.255.255.0 hay un equipo con IP 10.0.2.9. ¿Está en la red?", ["Con esa máscara los tres primeros números definen la red.", "10.0.2 no es igual a 10.0.1."], "No está en la red"),
        ("Hallazgo de seguridad", "Un equipo de ejemplo tiene el cortafuegos desactivado. ¿Cuál es el hallazgo?", ["El cortafuegos debe estar activo.", "Su desactivación deja el equipo expuesto."], "Cortafuegos desactivado: riesgo de seguridad"),
    ],
    mistakes=[("Revisar solo si la IP «se ve bien» sin comparar con la red.", "Una IP de otra red no se comunica con los demás equipos.", "Compara los tres primeros números con la red."),
              ("Corregir los errores en una red real sin avisar «para ayudar».", "Un cambio sin autorización puede dejar a la organización sin servicio.", "Informa los hallazgos y espera la autorización.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un conflicto de IP?", "Dos equipos con la misma dirección en una red", "Una IP que empieza con 192", "Un equipo sin cables", "Una IP repetida produce fallas de comunicación."),
        ("abc", "¿Por qué es riesgosa una cuenta compartida por varias personas?", "No se puede saber quién hizo cada cosa", "Consume mucha memoria", "Cambia la máscara de red", "La cuenta compartida impide la trazabilidad."),
        ("abc", "En una red 192.168.30.0 con máscara 255.255.255.0, ¿cuál IP pertenece a la red?", "192.168.30.50", "192.168.31.50", "192.169.30.50", "Los tres primeros números deben coincidir con los de la red."),
        ("abc", "{F} ¿Qué equipos de la ficha tienen una IP repetida?", "PC-B y PC-C", "PC-A y PC-B", "PC-D y PC-E", "Ambos equipos tienen la misma dirección, 192.168.30.12, y eso es un conflicto."),
        ("abc", "{F} ¿Qué equipo tiene una IP que no pertenece a la red?", "PC-D", "PC-A", "PC-E", "192.168.40.13 no coincide con los tres primeros números de la red 192.168.30."),
        ("abc", "{F} ¿Qué dato falta en la configuración del PC-E?", "La puerta de enlace", "La máscara", "El nombre de la notaría", "La ficha indica que su puerta de enlace está en blanco."),
        ("=", "{F} De los 5 equipos de la ficha, uno tiene IP fuera de la red, uno no tiene puerta de enlace y dos comparten una IP. ¿Cuántos equipos están sin ningún error de dirección?", "5-1-1-2", "Se restan los equipos con error a los cinco de la lista.", " equipos"),
        ("abc", "{F} ¿Qué hallazgo de seguridad tiene el PC-B además de la IP repetida?", "Cortafuegos desactivado y cuenta compartida", "Tiene demasiada memoria", "Un cable muy largo", "La ficha anota esos dos problemas de seguridad."),
        ("abc", "{F} ¿Qué debe hacer la persona que revisa la configuración con los hallazgos?", "Informarlos al administrador de red y anotarlos", "Cambiarlos en la red real sin avisar", "Guardarlos en silencio", "Se informa y se registra; los cambios los autoriza el responsable."),
        ("=", "{F} Si cada una de las 3 personas que comparten la cuenta del PC-B tuviera su propia cuenta, ¿cuántas cuentas habría en vez de la compartida?", "3", "Se crea una cuenta por persona.", " cuentas"),
        ("abc", "{F} Si se corrige el PC-D a 192.168.30.13, ¿puede comunicarse con el PC-A en la misma red?", "Sí, porque ahora pertenece a la red 192.168.30", "No, porque tiene el número 13", "No, porque falta el DNS", "Con los tres primeros números iguales, los equipos están en la misma red."),
        ("abc", "Una persona anota en un papel pegado al monitor la contraseña de su cuenta. ¿Cuál es el hallazgo?", "La contraseña está a la vista de cualquiera", "Falta una puerta de enlace", "La IP está repetida", "Las contraseñas son secretas y no se dejan a la vista."),
        ("abc", "{F} Se propone dejar al PC-B y al PC-C con la misma IP 192.168.30.12, «para que queden juntos». ¿Qué problema crea?", "Mantiene el conflicto de IP", "Quita la puerta de enlace", "Cambia la máscara", "Dos equipos con la misma IP siguen generando conflicto."),
    ],
    ctx=("abc", "Una notaria de ejemplo pregunta si puede arreglar ella misma la IP repetida entre dos equipos, sin avisar a la encargada de informática. ¿Qué corresponde?", "Avisar a la encargada de informática y esperar la corrección autorizada", "Cambiar las IP al azar", "Apagar toda la red", "Los cambios de red los coordina y autoriza el responsable."),
    sc=[
        ("En Telecomunicaciones: ¿qué es un hallazgo?", "Un error o riesgo encontrado al revisar", "Se informa al responsable y se deja registrado en la bitácora."),
        ("¿Cuándo una IP está en la red 192.168.30.0 con máscara 255.255.255.0?", "Cuando sus tres primeros números son 192.168.30", "Con esa máscara, esos tres números definen a qué red pertenece la dirección."),
        ("¿Qué se hace con los hallazgos de una red real?", "Se informan al responsable antes de corregir", "La corrección la autoriza el responsable."),
    ],
    op=("Una veterinaria de ejemplo tiene la red 192.168.7.0 con máscara 255.255.255.0 y puerta de enlace 192.168.7.1. Equipos: Caja IP 192.168.7.10; Agenda IP 192.168.7.11; Sala IP 192.168.7.11; Bodega IP 192.168.8.12. La Caja no tiene el cortafuegos activo. Escribe una lista de hallazgos (qué está mal y por qué) y la corrección que propondrías al administrador.",
        "Hallazgos: 1) Agenda y Sala repiten la IP 192.168.7.11, lo que causa conflicto. 2) Bodega tiene IP 192.168.8.12, que no pertenece a la red 192.168.7. 3) Caja tiene el cortafuegos desactivado, lo que es un riesgo. Propuesta: asignar una IP distinta a Sala, cambiar la IP de Bodega a una de 192.168.7 y activar el cortafuegos, todo con autorización.",
        ["detecta la IP repetida", "detecta la IP fuera de la red y el cortafuegos", "propone correcciones con autorización"],
        ["lista de tres hallazgos con su corrección"],
        ["no ver la IP repetida", "no comparar con la red", "corregir sin autorización"],
        "Pregunta: «¿qué números de la IP definen la red?». Si no sabe, pídele que compare cada IP con 192.168.7."),
    reinforce="Escribe un hallazgo de ejemplo sobre una cuenta compartida y la corrección que propondrías.",
    extend="Explica con un ejemplo inventado qué problemas causa una puerta de enlace en blanco.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 12 (plan de direccionamiento de ejemplo, inventado). La «Escuela Rural El Roble» (ficticia) planea su red local: red 192.168.50.0 con máscara 255.255.255.0 (254 direcciones útiles para equipos; la .0 es la red y la .255 es la de difusión). "
     "Equipos: 1 router (.1), 1 servidor (.2), 1 impresora (.3), 12 computadores de alumnos y 3 computadores de profesores. Reglas de ejemplo: las direcciones .1 a .20 son fijas; las .100 a .199 las entrega el DHCP.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: planificar direcciones, repartir las fijas y las automáticas y verificar que alcanzan.",
    prior=["Sé qué son la IP, la máscara, la puerta de enlace y el DHCP.", "Sé restar cantidades.", "Sé qué es una dirección fija y una automática."],
    explain=[
        "Un plan de direccionamiento es la lista de qué direcciones se usan para qué. Con la máscara 255.255.255.0, la red tiene 256 direcciones, pero dos están reservadas: la primera (.0) identifica la red y la última (.255) sirve para enviar a todos a la vez (difusión). Por eso quedan 254 direcciones para equipos. Si se necesitan más equipos que direcciones, la red no alcanza y se rediseña.",
        "El plan separa rangos: un rango de direcciones fijas para router, servidor e impresoras, y un rango de direcciones automáticas que entrega el DHCP a computadores y teléfonos. Los rangos no se cruzan. Se deja espacio libre para crecer: un buen plan no usa todas las direcciones, porque mañana habrá más equipos.",
        "La verificación final es contar: cuántos equipos fijos y cuántos automáticos hay, y si caben en sus rangos. El resultado se escribe en la ficha del proyecto y se entrega al administrador de red. Todo es de ejemplo en papel; configurar una red real exige autorización. " + AVISO,
    ],
    vocab=[("plan de direccionamiento", "lista de qué direcciones IP se usan para qué"), ("rango", "conjunto de direcciones seguidas, de una a otra"), ("dirección de difusión", "dirección para enviar a todos los equipos de la red a la vez"), ("direcciones útiles", "direcciones que sí se pueden dar a equipos"), ("crecer", "prever más equipos en el futuro")],
    worked=[
        ("Caben en el rango", "Un rango automático de ejemplo va de .50 a .79, ambos incluidos. ¿Cuántas direcciones tiene?", ["Se resta el inicio al final y se suma 1 porque se incluyen ambos.", "79 menos 50 son 29; más 1 son 30."], "30 direcciones"),
        ("Fijas que faltan", "Una red de ejemplo tiene 4 equipos fijos y reserva 10 direcciones fijas. ¿Cuántas fijas quedan libres?", ["Se resta lo usado a lo reservado.", "10 menos 4."], "6 direcciones"),
    ],
    mistakes=[("Contar los extremos del rango sin sumar 1 (de .100 a .199 son 99).", "Si se incluyen ambos extremos, hay una más que la resta.", "Resta y suma 1: 199 menos 100 más 1 son 100."),
              ("Dejar todas las direcciones ocupadas «para aprovechar la red».", "Sin espacio libre no se pueden agregar equipos.", "Reserva direcciones libres para crecer.")],
    T=[
        ("abc", "En Telecomunicaciones: ¿qué es un plan de direccionamiento?", "La lista de qué direcciones IP se usan para qué", "El dibujo del cableado de una pared", "La clave de la red inalámbrica", "El plan reparte las direcciones de una red."),
        ("abc", "¿Cuántas direcciones útiles para equipos tiene una red con máscara 255.255.255.0?", "254", "256", "255", "De las 256 direcciones, dos están reservadas: la de red y la de difusión."),
        ("abc", "¿Qué entrega el DHCP?", "Direcciones automáticas dentro de su rango", "Direcciones fijas a los servidores", "Contraseñas a los usuarios", "El DHCP asigna las direcciones del rango automático."),
        ("=", "{F} ¿Cuántos computadores hay entre alumnos y profesores?", "12+3", "Se suman los computadores de alumnos y los de profesores.", " computadores"),
        ("=", "{F} ¿Cuántas direcciones tiene el rango fijo de .1 a .20, ambos incluidos?", "20-1+1", "Se resta el inicio al final y se suma 1 porque se incluyen ambos.", " direcciones"),
        ("=", "{F} El router, el servidor y la impresora ocupan 3 direcciones fijas. ¿Cuántas fijas quedan libres en el rango .1 a .20?", "20-3", "Se resta lo usado al total del rango.", " direcciones"),
        ("=", "{F} ¿Cuántas direcciones tiene el rango automático de .100 a .199, ambos incluidos?", "199-100+1", "Se resta el inicio al final y se suma 1.", " direcciones"),
        ("abc", "{F} ¿Los 15 computadores caben en el rango automático?", "Sí, porque hay 100 direcciones para 15 equipos", "No, porque los computadores de profesores van en el rango fijo", "No, porque el DHCP no reparte direcciones", "Con 100 direcciones disponibles sobran para 15 computadores."),
        ("=", "{F} Después de repartir las 15 direcciones automáticas, ¿cuántas del rango automático quedan libres?", "100-15", "Se restan los computadores a las 100 direcciones del rango.", " direcciones"),
        ("abc", "{F} Se agregará una impresora más y se le quiere dar la dirección fija .2. ¿Qué corresponde?", "Elegir una libre, como .4, porque la .2 ya es del servidor", "Usar la .2 porque es más fácil de recordar", "Usar la .1 del router", "Una dirección ocupada no se repite."),
        ("abc", "Un plan de ejemplo pretende dar 300 direcciones a equipos en una red con máscara 255.255.255.0. ¿Qué ocurre?", "No alcanzan, porque la red tiene 254 útiles", "Alcanzan si se usan también la dirección de red y la de difusión", "Alcanzan porque la difusión también se usa", "Con esa máscara solo hay 254 direcciones útiles."),
        ("abc", "{F} ¿Por qué no se asignan todas las direcciones del rango automático?", "Para dejar espacio al crecimiento futuro", "Porque el DHCP funciona mal con rangos llenos", "Porque las direcciones se gastan al usarlas", "Un plan prudente deja direcciones libres para equipos nuevos."),
        ("abc", "{F} Una profesora lleva su notebook personal y pide una IP fija .5 para acceder a las carpetas del servidor. ¿Qué corresponde?", "Pedir autorización al administrador de red según la política de seguridad", "Asignarse la .5 ella misma", "Usar la IP de un compañero", "La política y la autorización del responsable rigen el acceso a la red."),
    ],
    ctx=("abc", "La directora de una escuela de ejemplo quiere sumar 130 notebooks a una red 192.168.50.0 con máscara 255.255.255.0 y rango automático de 100 direcciones. ¿Qué concluye el técnico?", "Que no alcanza el rango y hay que ampliar o rediseñar el plan", "Que alcanza porque el DHCP puede repartir más de las que existen", "Que hay que apagar el DHCP", "130 es mayor que las 100 direcciones del rango; hay que rediseñar."),
    sc=[
        ("En Telecomunicaciones: ¿cuántas direcciones útiles tiene una red con máscara 255.255.255.0?", "254", "Se reservan la de red y la de difusión."),
        ("¿Cuántas direcciones tiene el rango de .10 a .19, ambos incluidos?", "10", "19 menos 10 más 1 son 10."),
        ("¿Para qué se deja espacio libre en el plan?", "Para agregar equipos en el futuro", "Un plan sin espacio no crece."),
    ],
    op=("Una oficina de ejemplo usa la red 192.168.60.0 con máscara 255.255.255.0. Reglas: de .1 a .10 son fijas; de .50 a .149 las entrega el DHCP. Equipos: 1 router, 1 servidor, 2 impresoras y 40 computadores. Calcula (a) cuántas direcciones fijas se usan y cuántas quedan libres, (b) cuántas direcciones tiene el rango automático, (c) cuántas quedan libres tras repartir los computadores y (d) una frase de conclusión para el administrador.",
        "(a) 1 más 1 más 2 son 4 fijas; quedan 10 menos 4, es decir 6 libres. (b) 149 menos 50 más 1 son 100. (c) 100 menos 40 son 60 libres. (d) El plan alcanza y deja 6 fijas y 60 automáticas libres para crecer.",
        ["calcula fijas usadas y libres", "calcula el rango automático y las libres", "concluye con los números"],
        ["hoja con las cuentas y la conclusión"],
        ["olvidar sumar 1 en el rango", "mezclar los rangos", "no concluir"],
        "Pregunta: «¿por qué sumas 1 al calcular el rango?». Si no sabe, pídele que cuente de 50 a 52 con los dedos."),
    reinforce="Calcula cuántas direcciones tiene el rango de .30 a .59, ambos incluidos.",
    extend="Explica con un ejemplo inventado qué problema causa mezclar el rango fijo con el rango automático.",
)

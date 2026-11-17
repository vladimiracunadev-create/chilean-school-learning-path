"""Gráfica TP 3.º y 4.º medio: OAE-04 (regular máquinas de impresión: solo conceptos, documentos y seguridad) y OAE-05 (realizar la impresión: control de calidad, limpieza y cálculos de producción en papel). Sin procedimientos operativos; trabajos, mediciones y costos inventados."""
from __future__ import annotations

from tp_graf_common import build

O4 = "TP-GRAF-3y4-OAE-04"
O5 = "TP-GRAF-3y4-OAE-05"
MAQ = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). Máquinas: una prensa offset de pliego, una máquina flexográfica, una mesa de serigrafía, una guillotina y una plegadora. Reglas del taller (de ejemplo): solo opera una máquina quien está autorizado y capacitado; "
     "las protecciones (resguardos) no se retiran ni se anulan; la persona responsable da el visto bueno antes de partir; se usa protección auditiva donde hay ruido; se mantienen el orden y la limpieza; ante cualquier duda se detiene y se avisa. "
     "Documentos: la orden de trabajo (OT), el manual del fabricante y la hoja de ajuste. Capacitación exigida para operar una máquina nueva: 12 horas, según la regla de ejemplo del taller.")
build(
    O4, 1, F,
    use="Aprenderé qué es regular una máquina de impresión, qué documentos manda a leer, qué peligros hay en términos generales y por qué solo opera quien está autorizado.",
    prior=["Conozco la OT y la hoja de datos de seguridad.", "Sé calcular restas simples.", "Sé qué es un estándar de calidad."],
    explain=[
        "Regular una máquina de impresión significa dejarla ajustada a lo que pide el trabajo: el formato, el sustrato, las tintas y la calidad de la orden de trabajo (OT). Este cuaderno no enseña a hacer esos ajustes: explica qué documentos los guían y qué normas de seguridad los rodean. La hoja de ajuste es el registro donde la persona autorizada anota los valores usados; el manual del fabricante manda cómo se hace cada ajuste.",
        "Las máquinas de impresión tienen peligros generales: partes en movimiento que pueden atrapar o aplastar, ruido, productos químicos y cargas pesadas. Por eso existen los resguardos, que son las protecciones que cubren las partes peligrosas, y que nunca se retiran ni se anulan. La ropa suelta, el cabello largo suelto y las joyas aumentan el riesgo cerca de partes en movimiento.",
        "Solo opera una máquina quien está autorizado y capacitado, y siempre con la norma vigente y elementos de protección. Si algo parece raro, se detiene y se avisa a la persona responsable. También importan la ergonomía y las pausas al trabajar de pie muchas horas." + MAQ,
    ],
    vocab=[("regular una máquina", "dejarla ajustada a lo que pide el trabajo"), ("hoja de ajuste", "registro con los valores usados para dejar lista la máquina"), ("manual del fabricante", "documento que indica cómo usar y ajustar la máquina"), ("resguardo", "protección que cubre una parte peligrosa de la máquina"), ("autorizado", "persona a quien la empresa permitió operar una máquina tras su capacitación"), ("elementos de protección", "ropa y equipos que reducen un riesgo, como la protección auditiva")],
    worked=[
        ("Horas que faltan", "Una persona de ejemplo lleva 8 horas de una capacitación de 12 horas. ¿Cuántas le faltan?", ["Se resta lo hecho al total.", "12 − 8 = 4."], "4 horas"),
        ("Qué documento consultar", "Quieres saber cómo ajustar un componente de una máquina de ejemplo. ¿Qué documento corresponde?", ["El fabricante indica cómo se hace cada ajuste.", "Eso está en el manual del fabricante."], "El manual del fabricante"),
    ],
    mistakes=[("Retirar un resguardo «para ver mejor» cómo funciona la máquina.", "Los resguardos protegen de partes en movimiento; sin ellos aumenta el riesgo de lesiones.", "Nunca retires un resguardo; si hay una duda, avisa a la persona responsable."),
              ("Operar una máquina porque «ya vi cómo se hace».", "Mirar no reemplaza la capacitación ni la autorización de la empresa.", "Opera solo quien está autorizado y capacitado, con instructor.")],
    T=[
        ("abc", "En Gráfica: ¿qué significa regular una máquina de impresión?", "Dejarla ajustada a lo que pide el trabajo", "Comprar una máquina nueva", "Guardar la máquina al terminar el día", "Regular es ajustar la máquina al formato, sustrato y calidad de la OT."),
        ("abc", "En Gráfica: ¿qué es un resguardo?", "Una protección que cubre una parte peligrosa de la máquina", "Un tipo de tinta", "El manual de la máquina", "El resguardo evita el contacto con partes peligrosas y no se retira."),
        ("abc", "{F} ¿Quién puede operar una máquina según las reglas del taller?", "Quien está autorizado y capacitado", "Cualquier persona que haya visto cómo se hace", "Cualquier ayudante que lleve un mes en el taller", "La regla de ejemplo exige autorización y capacitación."),
        ("abc", "{F} ¿Qué documento guía cómo se hace cada ajuste de una máquina?", "El manual del fabricante", "La hoja de datos de un papel", "La factura de la tinta", "El fabricante conoce su máquina y describe cada ajuste en su manual."),
        ("=", "{F} Una persona lleva 5 horas de la capacitación exigida para una máquina nueva. ¿Cuántas horas le faltan?", "12-5", "Al total exigido se le restan las horas ya hechas.", " horas"),
        ("abc", "¿Para qué sirve la hoja de ajuste?", "Para registrar los valores usados para dejar lista la máquina", "Para calcular el precio del trabajo", "Para guardar la firma del cliente", "La hoja de ajuste deja constancia de cómo se preparó la máquina."),
        ("abc", "{F} ¿Qué peligro general tiene el ruido en un taller de impresión?", "Puede dañar la audición si no se usa la protección indicada", "Hace que el papel cambie de color", "Aumenta la velocidad de la máquina", "El ruido prolongado puede dañar la audición; se reduce con protección auditiva y la norma vigente."),
        ("abc", "Alguien con cabello largo suelto se acerca a una máquina en funcionamiento de ejemplo para mirar. ¿Qué corresponde?", "Alejarse y recogerse el cabello, porque las partes en movimiento pueden atrapar", "Acercarse más para ver mejor", "No hacer nada porque el cabello no es un riesgo", "Cerca de partes en movimiento, el cabello suelto puede quedar atrapado."),
        ("abc", "{F} Una compañera propone retirar un resguardo «solo un momento» para mirar. ¿Qué respondes?", "Que los resguardos no se retiran ni se anulan porque protegen de las partes en movimiento", "Que es seguro si la máquina está lenta", "Que se puede si lo hace una persona rápida", "La regla del taller prohíbe retirar resguardos; no hay un «momento» seguro."),
        ("abc", "{F} Un estudiante en práctica quiere partir la máquina de ejemplo porque «ya ha visto cómo se hace». ¿Qué corresponde?", "Pedir capacitación y trabajar solo con instructor autorizado", "Partirla si nadie lo ve", "Partirla si usa guantes", "Mirar no autoriza a operar; se requiere capacitación e instructor."),
        ("abc", "Notas un ruido distinto en la máquina de ejemplo y el jefe no está. ¿Qué haces?", "Me detengo, aviso a una persona responsable y no toco la máquina", "Sigo y espero que se pase", "Pido a un compañero que la repare sin permiso", "Ante una duda se detiene y se avisa; los arreglos los hace personal autorizado."),
        ("abc", "{F} Un compañero autorizado te pide mantener abierto un resguardo «un segundo» mientras él revisa algo. ¿Qué haces?", "Me niego y aviso a la persona responsable, porque los resguardos no se mantienen abiertos ni se anulan", "Lo hago si es solo un segundo", "Lo hago si me presta guantes", "La regla del taller prohíbe anular resguardos aunque lo pida alguien con experiencia."),
        ("=", "{F} El taller tiene 5 máquinas y 3 de ellas son de impresión. ¿Cuántas no son de impresión?", "5-3", "Al total de máquinas se le restan las de impresión.", " máquinas"),
    ],
    ctx=("abc", "Un familiar de ejemplo te ofrece dejarte «practicar» en su máquina de impresión sin instructor ni autorización. ¿Qué respondes?", "Que solo trabajarás con instructor autorizado y la norma vigente, porque este aprendizaje es conceptual", "Que aceptas si no hay nadie más", "Que aceptas si te presta guantes", "Practicar con maquinaria exige autorización, instructor y elementos de protección."),
    sc=[
        ("En Gráfica: ¿qué es un resguardo?", "Una protección que cubre una parte peligrosa", "Evita que las personas toquen partes en movimiento."),
        ("¿Quién puede operar una máquina?", "Quien está autorizado y capacitado", "La empresa autoriza solo a quien tiene capacitación."),
        ("¿Qué haces si algo parece raro en una máquina?", "Me detengo y aviso", "Una duda sin aviso puede terminar en un accidente."),
    ],
    op=("Un taller de ejemplo recibe a un estudiante en visita. Escribe tres reglas de seguridad generales que le explicarías antes de entrar (por ejemplo sobre resguardos, ropa y autorización) y para cada una una razón. "
        "Luego calcula: si el taller exige 12 horas de capacitación y el estudiante lleva 7, cuántas horas le faltan.",
        "Regla 1: no retirar resguardos, porque protegen de partes en movimiento. Regla 2: no usar ropa suelta ni dejar el cabello suelto cerca de las máquinas, porque pueden atraparse. Regla 3: no operar sin autorización ni capacitación, porque se puede lesionar. Faltan 12 − 7 = 5 horas.",
        ["escribe tres reglas generales de seguridad", "da una razón para cada regla", "calcula bien las horas que faltan"],
        ["hoja con tres reglas con su razón y el cálculo"],
        ["escribir pasos para operar la máquina", "no dar razones", "olvidar el cálculo"],
        "Pregunta: «¿por qué el cabello suelto es un riesgo?». Si no sabe, vuelve a las partes en movimiento."),
    reinforce="Dibuja un cartel de ejemplo con tres reglas de seguridad para la entrada de un taller gráfico.",
    extend="Explica por qué ver a otra persona usar una máquina no es lo mismo que estar capacitado para usarla.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (sistemas de impresión, descripción de ejemplo). Tipográfica: formas con relieve que se entintan y presionan el papel. Offset: una plancha plana pasa la imagen a una mantilla de caucho y esta al papel; hay offset de pliego (hojas) y de bobina (rollo continuo de papel). "
     "Flexografía: plancha de relieve flexible y tintas fluidas; se usa en etiquetas, envases y cartón. Serigrafía: la tinta pasa a través de una malla con zonas abiertas, sobre materiales muy variados. Cuerpo de impresión: unidad de una máquina que imprime un color. "
     "Pliego: hoja grande de papel donde se imprime.")
build(
    O4, 2, F,
    use="Aprenderé en qué se diferencian los sistemas de impresión tipográfico, offset, flexográfico y serigráfico, y qué términos de máquina aparecen en una orden de trabajo.",
    prior=["Sé qué es una matriz de impresión.", "Conozco la OT y la hoja de ajuste.", "Sé multiplicar y dividir."],
    explain=[
        "Un sistema de impresión es la manera de pasar la imagen al sustrato. En la impresión tipográfica, las formas tienen relieve, se entintan y presionan el papel. En el offset, la imagen está en una plancha plana, pasa a una mantilla de caucho y de ahí al papel; se llama de pliego cuando imprime hojas y de bobina cuando imprime sobre un rollo continuo de papel.",
        "En la flexografía se usa una plancha de relieve flexible y tintas fluidas, y es común en etiquetas, envases y cartón. En la serigrafía la tinta atraviesa una malla que tiene zonas abiertas y zonas tapadas, y permite imprimir sobre materiales muy variados. Un cuerpo de impresión es la unidad de la máquina que imprime un color: una máquina de 5 cuerpos imprime hasta 5 colores en una sola pasada.",
        "Estos nombres sirven para leer una OT y el manual del fabricante. Describirlos aquí no enseña a ajustar ni a operar las máquinas." + MAQ,
    ],
    vocab=[("sistema de impresión", "manera de pasar la imagen al sustrato"), ("offset", "sistema con plancha plana, mantilla de caucho y papel"), ("flexografía", "sistema con plancha de relieve flexible y tintas fluidas"), ("serigrafía", "sistema en que la tinta atraviesa una malla"), ("cuerpo de impresión", "unidad de la máquina que imprime un color"), ("bobina", "rollo continuo de papel")],
    worked=[
        ("Pasadas necesarias", "Un trabajo de ejemplo es de 4 colores y la máquina tiene 2 cuerpos. ¿Cuántas pasadas se necesitan?", ["Cada cuerpo imprime un color.", "4 ÷ 2 = 2 pasadas."], "2 pasadas"),
        ("Reconocer el sistema", "Una descripción de ejemplo dice: «la tinta atraviesa una malla con zonas abiertas». ¿Qué sistema es?", ["La malla con zonas abiertas es la característica de uno de los sistemas.", "Ese es el sistema serigráfico."], "Serigrafía"),
    ],
    mistakes=[("Decir que el offset imprime directamente de la plancha al papel.", "En el offset la imagen pasa de la plancha a una mantilla de caucho y de ahí al papel.", "Recuerda el camino: plancha, mantilla, papel."),
              ("Creer que todos los sistemas usan una plancha plana.", "La tipográfica y la flexografía usan formas con relieve, y la serigrafía usa una malla.", "Asocia cada sistema con su forma de llevar la imagen.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el offset?", "Un sistema donde la imagen pasa de una plancha plana a una mantilla de caucho y luego al papel", "Un sistema donde la tinta atraviesa una malla", "Un sistema con formas de relieve que presionan el papel", "El offset es indirecto: plancha, mantilla, papel."),
        ("abc", "En Gráfica: ¿qué es la serigrafía?", "Un sistema en que la tinta atraviesa una malla con zonas abiertas", "Un sistema con plancha plana y mantilla", "Un sistema que solo imprime sobre rollos de papel", "La malla con zonas abiertas deja pasar la tinta solo donde va la imagen."),
        ("abc", "En Gráfica: ¿qué es un cuerpo de impresión?", "La unidad de la máquina que imprime un color", "El cuerpo de las personas que operan la máquina", "El tamaño de la letra", "Una máquina de más cuerpos imprime más colores en una pasada."),
        ("abc", "{F} ¿Qué diferencia hay entre offset de pliego y de bobina?", "El de pliego imprime hojas y el de bobina un rollo continuo de papel", "El de pliego usa malla y el de bobina plancha de relieve", "No hay diferencia", "La diferencia está en el sustrato: hojas o rollo continuo."),
        ("=", "{F} Una máquina de ejemplo tiene 6 cuerpos y el trabajo usa 4 colores. ¿Cuántos cuerpos quedan sin usar?", "6-4", "A los cuerpos de la máquina se les restan los colores usados.", " cuerpos"),
        ("abc", "{F} ¿Qué sistema se asocia a etiquetas, envases y cartón?", "La flexografía", "La serigrafía", "La impresión tipográfica", "La ficha asocia la plancha flexible con etiquetas, envases y cartón."),
        ("=", "{F} Un trabajo de 7 colores se imprime en una máquina de 2 cuerpos. ¿Cuántas pasadas necesita?", "(7+2-1)//2", "Con 2 colores por pasada, 3 pasadas cubren 6 colores y falta 1, por eso son 4.", " pasadas"),
        ("abc", "{F} Un trabajo de 4 colores se imprime en una máquina de 4 cuerpos. ¿Cuántas pasadas necesita?", "Una sola pasada", "Cuatro pasadas", "Ninguna", "Cada cuerpo imprime un color, así que 4 cuerpos hacen los 4 colores juntos."),
        ("abc", "{F} Un cliente quiere imprimir carteles sobre un material rígido y poco común. ¿Qué sistema de la ficha puede servir por su variedad de materiales?", "La serigrafía", "El offset de bobina", "La flexografía", "La ficha dice que la serigrafía imprime sobre materiales muy variados."),
        ("abc", "{F} Una compañera dice: «en el offset la plancha toca el papel directamente». ¿Qué corrección corresponde?", "La plancha pasa la imagen a una mantilla de caucho y esta al papel", "Tiene razón, es directo", "La plancha siempre es una malla", "El offset es indirecto: la mantilla interviene entre la plancha y el papel."),
        ("abc", "Alguien dice: «ya sé los sistemas, puedo ajustar la máquina». ¿Qué respondes?", "Conocer los nombres sirve para leer la OT, pero ajustar exige capacitación e instructor", "Tiene razón: con eso basta", "Ajustar solo requiere saber los nombres", "El vocabulario es conceptual; operar máquinas requiere autorización."),
        ("abc", "{F} Una OT dice «4 cuerpos, offset de pliego». ¿Qué información entrega?", "Imprime hojas con 4 colores en una pasada", "Imprime un rollo con 1 color", "Imprime con malla en 4 pasadas", "Se lee: offset de hojas con 4 unidades de color."),
        ("=", "{F} Un taller tiene 3 máquinas de 4 cuerpos cada una. ¿Cuántos colores pueden imprimir a la vez, sumando todas?", "3*4", "Se multiplican las máquinas por los cuerpos de cada una.", " colores"),
    ],
    ctx=("abc", "Un cliente de ejemplo pide 100.000 etiquetas en rollo para frascos y te pregunta qué sistema se usa. Con la ficha, ¿qué le explicas?", "Que la flexografía se usa en etiquetas y envases, y que se confirma con el manual y la OT", "Que se usa serigrafía porque siempre es mejor", "Que ningún sistema sirve", "La ficha asocia la flexografía a etiquetas; la decisión final se confirma con los documentos del trabajo."),
    sc=[
        ("En Gráfica: ¿qué sistema pasa la imagen a una mantilla de caucho?", "El offset", "La mantilla es el paso intermedio entre plancha y papel."),
        ("¿Cuántos colores imprime un cuerpo?", "Uno", "Un cuerpo de impresión es la unidad de un color."),
        ("¿Qué sistema usa una malla?", "La serigrafía", "La tinta atraviesa las zonas abiertas de la malla."),
    ],
    op=("Un taller de ejemplo debe elegir el sistema para cuatro pedidos: (a) 200 carteles sobre plástico rígido; (b) 15.000 cajas de cartón para envases; (c) 3.000 tarjetas en hojas a 2 colores; (d) un diario de 150.000 ejemplares en rollo continuo de papel. "
        "Asigna a cada pedido un sistema de la ficha con una razón y calcula cuántas pasadas necesita el pedido (c) en una máquina de 1 cuerpo.",
        "(a) serigrafía, por imprimir sobre materiales variados; (b) flexografía, por envases y cartón; (c) offset de pliego, por hojas, y necesita 2 pasadas en una máquina de 1 cuerpo (2 ÷ 1); (d) offset de bobina, por rollo continuo de papel.",
        ["asigna un sistema a cada pedido", "da una razón basada en la ficha", "calcula bien las pasadas"],
        ["tabla con pedido, sistema y razón, más el cálculo"],
        ["elegir el mismo sistema para todos", "no dar razón", "confundir pasadas con cuerpos"],
        "Pregunta: «¿en qué se diferencian (a) y (b)?». Si dice que son iguales, repasa las diferencias de sustrato y de sistema."),
    reinforce="Dibuja un esquema simple del recorrido de la imagen en el offset: plancha, mantilla, papel.",
    extend="Explica por qué un taller puede tener máquinas de distintos sistemas y no una sola para todos los trabajos.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (reglas de selección de un taller de ejemplo, inventadas). Tirada alta sobre rollo continuo de papel: offset de bobina. Tirada media sobre hojas: offset de pliego. Etiquetas y envases: flexografía. Tirada corta sobre materiales diversos: serigrafía. Numeración o impresión con relieve en formularios: tipográfica. "
     "Pedidos de ejemplo: P1, 50.000 revistas en rollo continuo de papel; P2, 3.000 etiquetas para envases; P3, 60 carteles sobre plástico rígido; P4, 5.000 afiches en hojas; P5, 2.000 formularios con numeración.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un pedido con reglas de selección y a decidir qué sistema de impresión corresponde, con una razón y un registro.",
    prior=["Conozco los sistemas de impresión.", "Sé leer una OT.", "Sé comparar un pedido con una regla."],
    explain=[
        "Elegir un sistema de impresión es aplicar reglas del taller a los datos del pedido: tirada, sustrato y producto. La tirada es la cantidad que se imprime. El sustrato indica si hay rollo continuo, hojas o materiales especiales, y el producto puede ser una etiqueta, un formulario o un cartel. Cada dato se compara con la regla y se registra la conclusión con su razón.",
        "En esta clase se usan las reglas de la ficha, que son de ejemplo: en un taller real las reglas dependen de sus máquinas, de los costos y de las indicaciones del fabricante. Si un pedido cumple dos reglas o ninguna, no se decide por intuición: se consulta a la persona responsable y se registra lo acordado.",
        "Decidir el sistema es parte de leer la OT; ajustar la máquina que lo imprimirá es tarea de personas autorizadas." + MAQ,
    ],
    vocab=[("tirada", "cantidad de ejemplares que se imprimen"), ("regla de selección", "condición que relaciona el pedido con un sistema de impresión"), ("producto", "lo que se fabrica: etiqueta, formulario, cartel u otro"), ("numeración", "números correlativos impresos en cada ejemplar")],
    worked=[
        ("Aplicar una regla", "Un pedido de ejemplo de 200 bolsas de tela necesita un sistema para materiales diversos y tirada corta. ¿Qué regla de la ficha corresponde?", ["La ficha asigna serigrafía a tirada corta sobre materiales diversos.", "Ese pedido cumple esa condición."], "Serigrafía"),
        ("Contar pedidos", "De 5 pedidos de ejemplo, 2 se imprimen en hojas. ¿Cuántos no se imprimen en hojas?", ["Se resta del total los pedidos en hojas.", "5 − 2 = 3."], "3 pedidos"),
    ],
    mistakes=[("Elegir el sistema por costumbre sin mirar los datos del pedido.", "Cada pedido tiene datos que activan reglas distintas.", "Compara el sustrato, la tirada y el producto con la regla."),
              ("Decidir por cuenta propia cuando el pedido cumple dos reglas a la vez.", "Si dos reglas calzan, la elección corresponde a la persona responsable.", "Consulta y registra lo acordado.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una regla de selección?", "Una condición que relaciona un pedido con un sistema de impresión", "Una regla para medir papel", "Un permiso para operar máquinas", "La regla conecta datos como tirada y sustrato con el sistema que corresponde."),
        ("abc", "{F} ¿Qué sistema corresponde al pedido P1?", "Offset de bobina", "Serigrafía", "Flexografía", "P1 es una tirada alta en rollo continuo de papel."),
        ("abc", "{F} ¿Qué sistema corresponde al pedido P2?", "Flexografía", "Offset de pliego", "Serigrafía", "P2 son etiquetas para envases, que la ficha asocia a flexografía."),
        ("abc", "{F} ¿Qué sistema corresponde al pedido P3?", "Serigrafía", "Offset de bobina", "Tipográfica", "P3 es una tirada corta sobre plástico rígido, un material diverso."),
        ("abc", "{F} ¿Qué sistema corresponde al pedido P4?", "Offset de pliego", "Flexografía", "Serigrafía", "P4 es una tirada media sobre hojas."),
        ("abc", "{F} ¿Qué sistema corresponde al pedido P5?", "Tipográfica", "Offset de pliego", "Flexografía", "P5 requiere numeración en formularios, que la ficha asocia a la impresión tipográfica."),
        ("=", "{F} ¿Cuántos ejemplares suman los pedidos P1, P2 y P4?", "50000+3000+5000", "Se suman las cantidades de los tres pedidos.", " ejemplares"),
        ("=", "{F} P3 pide 60 carteles y P5 pide 2.000 formularios. ¿Cuántos ejemplares suman ambos pedidos?", "60+2000", "Se suman las cantidades de ambos pedidos.", " ejemplares"),
        ("abc", "{F} Un pedido de ejemplo es de 300 calendarios en hojas, tirada media. ¿Qué sistema sugiere la ficha?", "Offset de pliego", "Offset de bobina", "Serigrafía", "Tirada media sobre hojas corresponde a offset de pliego."),
        ("abc", "{F} Un compañero afirma: «P3 también debería ser offset de bobina porque es el más rápido». ¿Qué respondes?", "La regla asigna serigrafía a tiradas cortas sobre materiales diversos como el plástico rígido", "Tiene razón: lo rápido siempre decide", "El plástico rígido no se imprime nunca", "La decisión sigue la regla y los datos del pedido, no la velocidad."),
        ("abc", "{F} Llega un pedido de 500 etiquetas para envases y 2.000 numeradas a la vez en un mismo trabajo. ¿Qué corresponde?", "Consultar a la persona responsable y registrar lo acordado, porque calzan dos reglas", "Elegir el sistema que prefiera el operador", "Descartar el pedido", "Cuando calzan dos reglas, la decisión se consulta y se registra."),
        ("abc", "Un cliente exige imprimir en serigrafía «porque se ve mejor» sin dar datos del producto. ¿Qué haces?", "Pedir los datos del pedido y mostrar qué dice la regla del taller", "Aceptar sin preguntar", "Cambiar la OT por tu cuenta", "Las decisiones se basan en datos del pedido y reglas, no en preferencias sin respaldo."),
        ("=", "{F} Si P1 pide 50.000 revistas y se imprimen 5.000 por hora (valor de ejemplo), ¿cuántas horas dura la tirada?", "50000//5000", "Se divide la tirada por los ejemplares impresos por hora.", " horas"),
    ],
    ctx=("abc", "Una OT de ejemplo pide 1.000 pegatinas sobre vidrio y tu jefa te pregunta qué sistema sugiere la ficha para un material diverso en tirada corta. ¿Qué respondes?", "Serigrafía, según la regla de tirada corta sobre materiales diversos, y que lo confirmará la persona responsable", "Offset de bobina, porque es el más grande", "Ninguno, porque el vidrio no se imprime", "La ficha asigna serigrafía a tirada corta sobre materiales diversos; la confirmación corresponde a quien responde."),
    sc=[
        ("En Gráfica: ¿qué datos del pedido se comparan con la regla?", "Tirada, sustrato y producto", "Esos datos activan la regla que corresponde."),
        ("¿Qué haces si calzan dos reglas?", "Consulto a la persona responsable", "La elección entre dos reglas se acuerda y se registra."),
        ("¿Qué sistema se asocia a tirada alta en rollo?", "Offset de bobina", "La regla de la ficha lo asigna a ese tipo de pedido."),
    ],
    op=("Pedidos de ejemplo: (a) 90.000 folletos en rollo continuo de papel; (b) 150 letreros sobre plástico rígido; (c) 8.000 etiquetas para envases; (d) 4.000 afiches en hojas. Usa las reglas de la ficha. "
        "Asigna un sistema a cada uno con una razón, indica cuál es el pedido de tirada más corta y calcula cuántos ejemplares suman (a) y (c).",
        "(a) offset de bobina por tirada alta en rollo; (b) serigrafía por material diverso en tirada corta; (c) flexografía por etiquetas; (d) offset de pliego por hojas. El de tirada más corta es (b), con 150. Suma de (a) y (c): 90.000 + 8.000 = 98.000.",
        ["asigna bien los sistemas con razón", "identifica el pedido más corto", "suma correctamente las tiradas"],
        ["tabla de cuatro filas con sistema y razón, más la suma"],
        ["usar el mismo sistema para todos", "no justificar", "sumar mal"],
        "Pregunta: «¿qué dato del pedido (b) activa la serigrafía?». Si responde 'es pequeño', pídele que cite el sustrato y la tirada."),
    reinforce="Inventa tres pedidos con datos de tirada y sustrato y asigna a cada uno un sistema con las reglas de la ficha.",
    extend="Explica por qué las reglas de selección de un taller dependen de las máquinas que tiene.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (documentos de ejemplo, inventados). OT: 2.000 pliegos de 50 × 70 cm, papel de 250 g/m², 4 colores, offset de pliego. "
     "Hoja de ajuste preparada por la persona autorizada: formato 50 × 70 cm; papel de 250 g/m²; colores indicados: 3; sistema: offset de pliego. "
     "Tiempos de ejemplo: preparación de la máquina, 90 minutos; velocidad de impresión, 4.000 pliegos por hora.")
build(
    O4, 4, F,
    use="Aprenderé a comparar una hoja de ajuste con la orden de trabajo, detectar diferencias y calcular cuánto pesa la preparación en el tiempo total, sin ajustar ninguna máquina.",
    prior=["Conozco la OT, la hoja de ajuste y los sistemas de impresión.", "Sé calcular tiempos con divisiones.", "Sé qué es una tirada."],
    explain=[
        "La hoja de ajuste es el registro donde la persona autorizada anota los valores con que dejó lista la máquina. Antes de partir, se compara con la OT dato por dato: formato, papel, colores y sistema. Si un dato no coincide, no se arranca y se avisa a la persona responsable, que decide qué documento corregir. Aquí solo se aprende a leer y comparar esos documentos.",
        "El tiempo total de un trabajo es la preparación más la impresión. El tiempo de impresión se calcula dividiendo la tirada por la velocidad en pliegos por hora. En tiradas cortas la preparación pesa mucho en el total, y en tiradas largas se reparte entre muchos pliegos. Estos datos son de ejemplo y los valores reales dependen de la máquina.",
        "Un trabajo se arranca solo cuando OT y hoja de ajuste coinciden y la persona responsable da el visto bueno." + MAQ,
    ],
    vocab=[("coincidir", "ser iguales los datos de dos documentos"), ("visto bueno", "aprobación de la persona responsable para continuar"), ("tiempo de preparación", "tiempo que se usa en dejar lista la máquina antes de imprimir"), ("velocidad", "pliegos que se imprimen por hora")],
    worked=[
        ("Tiempo de impresión", "Una tirada de ejemplo de 6.000 pliegos con velocidad de 3.000 pliegos por hora. ¿Cuántas horas dura?", ["Tiempo = tirada ÷ velocidad.", "6.000 ÷ 3.000 = 2."], "2 horas"),
        ("Comparar dos datos", "La OT de ejemplo dice papel de 150 g/m² y la hoja de ajuste dice 170 g/m². ¿Coinciden?", ["Se comparan 150 y 170.", "Son distintos."], "No coinciden: se avisa antes de partir"),
    ],
    mistakes=[("Arrancar el trabajo con una diferencia entre OT y hoja de ajuste «para ganar tiempo».", "Si el dato equivocado es el de la hoja, se puede perder todo el material.", "Detén y avisa; decide la persona responsable."),
              ("Corregir por cuenta propia el dato de la hoja de ajuste.", "La hoja la prepara y firma la persona autorizada; cambiarla sin registro pierde trazabilidad.", "Informa la diferencia y espera la decisión.")],
    T=[
        ("abc", "En Gráfica: ¿qué se compara con la hoja de ajuste antes de partir?", "La orden de trabajo, dato por dato", "La factura del papel", "El plano de la bodega", "La OT es la fuente que dice qué debe quedar impreso."),
        ("abc", "{F} ¿Cuántos colores pide la OT?", "4 colores", "3 colores", "2 colores", "La OT indica 4 colores; la hoja de ajuste dice 3."),
        ("abc", "{F} ¿Qué dato de la hoja de ajuste no coincide con la OT?", "Los colores", "El formato", "El papel", "Formato, papel y sistema coinciden; los colores son 3 en la hoja y 4 en la OT."),
        ("=", "{F} ¿Cuántos colores faltan en la hoja de ajuste respecto de la OT?", "4-3", "A los colores de la OT se les restan los de la hoja.", " color"),
        ("=", "{F} ¿Cuántos pliegos imprime la máquina en media hora a la velocidad de la ficha?", "4000//2", "La velocidad por hora se divide por dos para obtener media hora.", " pliegos"),
        ("abc", "{F} ¿Qué se hace al descubrir la diferencia?", "No arrancar y avisar a la persona responsable", "Arrancar con 3 colores", "Cambiar la OT sin avisar", "Una diferencia entre documentos se resuelve antes de partir y con la persona responsable."),
        ("=", "{F} ¿Cuántos minutos dura la impresión de los 2.000 pliegos?", "2000*60//4000", "Se calcula cuántos pliegos salen por minuto y se divide la tirada.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma el trabajo entre preparación e impresión?", "90+2000*60//4000", "Se suman los minutos de preparación y de impresión.", " minutos"),
        ("abc", "{F} ¿Qué parte del tiempo total ocupa la preparación?", "Tres cuartos del total: 90 de 120 minutos", "Un cuarto del total", "La mitad exacta del total", "Con 90 de 120 minutos, la preparación ocupa tres cuartos del tiempo."),
        ("abc", "{F} Un compañero dice: «como el trabajo es corto, la preparación casi no cuenta». ¿Qué respondes?", "En tiradas cortas la preparación pesa mucho en el total", "Tiene razón: no cuenta", "La preparación dura lo mismo que la impresión siempre", "Con 90 minutos de preparación y 30 de impresión, la preparación domina el tiempo."),
        ("abc", "La hoja de ajuste de ejemplo dice papel de 200 g/m² y la OT 250 g/m². ¿Qué hace el operador?", "Avisa la diferencia y espera la decisión de la persona responsable", "Prefiere el dato que le parece más probable", "Imprime con el papel que haya", "El papel equivocado afecta la calidad; se consulta antes de partir."),
        ("abc", "{F} Si la hoja de ajuste ya fue firmada por la persona autorizada, ¿puede un estudiante en práctica cambiar el dato de colores?", "No, debe avisar y esperar que la persona autorizada lo corrija", "Sí, si usa lápiz", "Sí, si nadie lo ve", "Solo la persona autorizada modifica y firma la hoja de ajuste."),
        ("=", "{F} Si la velocidad fuera de 5.000 pliegos por hora, ¿cuántos minutos duraría la impresión de los 2.000 pliegos?", "2000*60//5000", "Se multiplica la tirada por 60 minutos y se divide por la velocidad.", " minutos"),
    ],
    ctx=("abc", "Son las 9:55 y el cliente espera su trabajo a las 10:30. Descubres que OT y hoja de ajuste no coinciden en un dato. ¿Qué haces?", "Aviso de inmediato a la persona responsable y explico la diferencia, aunque haya presión por el plazo", "Parto igual para cumplir el plazo", "Cambio el dato en silencio", "La presión del plazo no autoriza a partir con datos que no coinciden."),
    sc=[
        ("En Gráfica: ¿cómo se calcula el tiempo de impresión?", "Tirada dividida por la velocidad", "La velocidad dice cuántos pliegos salen por hora."),
        ("¿Qué haces si OT y hoja de ajuste no coinciden?", "Aviso antes de partir", "El dato equivocado puede perder todo el material."),
        ("¿Quién corrige la hoja de ajuste?", "La persona autorizada que la preparó", "Cambios sin autorización pierden la trazabilidad del trabajo."),
    ],
    op=("Documentos de ejemplo. OT: 3.000 pliegos, 70 × 100 cm, papel de 150 g/m², 2 colores. Hoja de ajuste: 3.000 pliegos, 50 × 70 cm, papel de 150 g/m², 2 colores. Preparación: 60 minutos; velocidad: 3.000 pliegos por hora. "
        "Indica qué datos coinciden y cuáles no, qué harías, y calcula el tiempo total del trabajo en minutos si se corrigiera.",
        "Coinciden la tirada, el papel y los colores. No coincide el formato: la OT dice 70 × 100 cm y la hoja 50 × 70 cm. Avisaría a la persona responsable y esperaría su decisión. Tiempo total: preparación de 60 minutos más impresión de 3.000 ÷ 3.000 = 1 hora = 60 minutos, así que 120 minutos.",
        ["compara dato por dato", "detecta la diferencia de formato y propone avisar", "calcula bien el tiempo total"],
        ["tabla de comparación, la acción y el cálculo"],
        ["no ver la diferencia de formato", "proponer corregir sin avisar", "olvidar sumar la preparación"],
        "Pregunta: «¿cómo sabes que el formato no coincide?». Si no lo explica, pídele que ponga los dos formatos lado a lado."),
    reinforce="Inventa una OT y una hoja de ajuste con una diferencia, y escribe cómo se la comunicarías a la persona responsable.",
    extend="Explica por qué la firma de la persona autorizada en la hoja de ajuste es importante para el registro del trabajo.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (turno de ejemplo, inventado). Trabajo: 8.000 folletos en offset de pliego. Roles: operador de máquina (autorizado), ayudante, encargado de calidad y jefe de turno. "
     "Estándares de ejemplo: una muestra aprobada (OK de impresión) firmada antes de la tirada y una revisión de calidad cada 500 pliegos. Orden y limpieza: los trapos con restos de tinta o solvente se guardan en un contenedor rotulado y cerrado; los derrames se informan a la persona responsable. "
     "Seguridad: resguardos en su lugar, protección auditiva y ropa ajustada. Pauta de ejemplo de pausas para trabajo de pie: 10 minutos cada 2 horas.")
build(
    O5, 1, F,
    use="Aprenderé quiénes participan en la impresión de un producto, qué estándares y normas de seguridad rodean el trabajo y qué cuidados de limpieza, ambiente y ergonomía corresponden.",
    prior=["Conozco la OT, la hoja de ajuste y los resguardos.", "Sé calcular divisiones simples.", "Sé qué es una tirada."],
    explain=[
        "Imprimir un producto es ejecutar la tirada de la orden de trabajo (OT) cumpliendo estándares de calidad y normas de seguridad. Participan varias personas: el operador, que debe estar autorizado y capacitado; el ayudante, el encargado de calidad que revisa lo impreso y el jefe de turno, que decide. El OK de impresión es la muestra aprobada y firmada que sirve de referencia durante toda la tirada.",
        "La calidad se controla a intervalos: cada cierto número de pliegos se retira una muestra y se compara con el OK de impresión. La limpieza y el orden son parte del trabajo: los trapos con restos de tinta o solvente se guardan en un contenedor rotulado y cerrado, y los derrames se informan a la persona responsable; no se echan al desagüe. Los residuos se manejan según la norma vigente.",
        "La seguridad incluye resguardos en su lugar, protección auditiva, ropa ajustada y cabello recogido. La ergonomía incluye pausas regulares y pedir ayuda o medios mecánicos para mover cargas pesadas. Cualquier intervención en una máquina la hacen solo personas autorizadas." + MAQ,
    ],
    vocab=[("OK de impresión", "muestra aprobada y firmada que sirve de referencia durante la tirada"), ("encargado de calidad", "persona que revisa lo impreso y lo compara con el estándar"), ("estándar de calidad", "regla verificable que el producto debe cumplir"), ("derrame", "líquido que se escapa de su envase, como tinta o solvente"), ("ergonomía", "organización del trabajo y del cuerpo para evitar daños")],
    worked=[
        ("Número de revisiones", "Una tirada de ejemplo de 3.000 pliegos con una revisión cada 500. ¿Cuántas revisiones hay?", ["Se divide la tirada por los pliegos entre revisiones.", "3.000 ÷ 500 = 6."], "6 revisiones"),
        ("Dónde guardar un trapo", "Un trapo tiene restos de solvente. ¿Dónde se guarda?", ["No va a la basura común.", "Va a un contenedor rotulado y cerrado para residuos."], "En un contenedor rotulado y cerrado"),
    ],
    mistakes=[("Limpiar con agua y echar los restos de tinta por el desagüe «para terminar rápido».", "La tinta y los solventes contaminan el agua y exigen manejo de residuos según la norma vigente.", "Guarda los restos en el contenedor rotulado y avisa a la persona responsable."),
              ("Sacarse la protección auditiva «un ratito» porque molesta.", "El daño por ruido se acumula aunque cada exposición parezca corta.", "Usa la protección mientras haya ruido y pide una pausa si te molesta.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el OK de impresión?", "La muestra aprobada y firmada que sirve de referencia durante la tirada", "El permiso para entrar al taller", "El recibo de pago del cliente", "Es la referencia con la que se comparan los pliegos."),
        ("abc", "{F} ¿Cada cuántos pliegos hay una revisión de calidad?", "Cada 500 pliegos", "Cada 50 pliegos", "Solo al final", "La ficha fija una revisión cada 500 pliegos."),
        ("abc", "{F} ¿Dónde se guardan los trapos con restos de tinta o solvente?", "En un contenedor rotulado y cerrado", "En la basura común", "En el desagüe", "Son residuos y se manejan según la norma vigente."),
        ("=", "{F} Con la tirada de 8.000 folletos, ¿cuántas revisiones de calidad hay?", "8000//500", "Se divide la tirada por los pliegos entre revisiones.", " revisiones"),
        ("abc", "¿Por qué es necesaria una muestra aprobada antes de la tirada?", "Para tener una referencia con la que comparar los pliegos", "Para decidir el precio final del trabajo", "Para ahorrar tinta únicamente", "La muestra aprobada es el patrón de calidad durante el trabajo."),
        ("abc", "{F} Se derrama un poco de tinta cerca de la máquina. ¿Qué corresponde?", "Avisar a la persona responsable y seguir las indicaciones de la hoja de datos de seguridad", "Taparlo con papel y seguir", "Echarlo al desagüe con agua", "Los derrames se informan y se manejan según la HDS y la norma."),
        ("=", "{F} Un turno de 8 horas sigue la pauta de ejemplo de una pausa de 10 minutos cada 2 horas. ¿Cuántos minutos de pausa suma el turno?", "(8//2)*10", "Se calcula cuántos bloques de 2 horas hay y se multiplican por la pausa.", " minutos"),
        ("abc", "Un ayudante nuevo quiere limpiar una parte de la máquina mientras está funcionando «para ganar tiempo». ¿Qué corresponde?", "No hacerlo: las intervenciones las hacen personas autorizadas con la máquina detenida y según el manual", "Hacerlo con cuidado y rápido", "Hacerlo si el jefe no mira", "Intervenir en una máquina en funcionamiento es un riesgo y exige autorización."),
        ("abc", "¿Qué ropa y presentación corresponden cerca de las máquinas?", "Ropa ajustada, cabello recogido y sin joyas colgantes", "Ropa suelta para estar cómodo", "Bufanda larga para el frío", "Lo suelto puede quedar atrapado por partes en movimiento."),
        ("abc", "{F} Un compañero dice: «no hace falta anotar la revisión, la hice de memoria». ¿Qué respondes?", "Si no queda registrada, no hay respaldo de que se hizo ni de su resultado", "Tiene razón: la memoria basta", "El registro es solo para el cliente", "El registro es la evidencia del control y protege a todo el equipo."),
        ("abc", "Una persona sola quiere mover un paquete de papel muy pesado para ahorrar tiempo. ¿Qué corresponde?", "Pedir ayuda o usar un medio mecánico, según la norma vigente", "Levantarlo con la espalda rápido", "Arrastrarlo por el piso", "Mover cargas pesadas sin ayuda puede lesionar la espalda."),
        ("abc", "{F} El ruido molesta y un compañero se saca la protección auditiva durante la tirada. ¿Qué le dices?", "Que el daño al oído se acumula y que pida una pausa en vez de sacársela", "Que es seguro si es poco rato", "Que los oídos se acostumbran y no se dañan", "El ruido sostenido puede dañar la audición aunque cada rato parezca corto."),
        ("=", "{F} Cada revisión de calidad demora 6 minutos. ¿Cuántos minutos suman las revisiones de toda la tirada?", "(8000//500)*6", "Se multiplican las revisiones por los minutos de cada una.", " minutos"),
    ],
    ctx=("abc", "Ves un charco de solvente en el piso cerca de la máquina y un compañero lo cubre con papel para que no se note. ¿Qué haces?", "Aviso a la persona responsable, señalizo la zona sin pisarla y espero las indicaciones", "Lo seco yo con trapos y sigo trabajando", "Ayudo a taparlo", "Un derrame se informa y se maneja según la hoja de datos de seguridad; taparlo aumenta el riesgo."),
    sc=[
        ("En Gráfica: ¿qué es el OK de impresión?", "La muestra aprobada que sirve de referencia", "Con ella se comparan los pliegos de toda la tirada."),
        ("¿Dónde van los restos de tinta?", "En un contenedor rotulado", "Los residuos no van al desagüe ni a la basura común."),
        ("¿Qué haces si algo no está claro en la máquina?", "Me detengo y aviso", "Las dudas se resuelven con la persona responsable."),
    ],
    op=("En un taller de ejemplo se imprimen 12.000 afiches con una revisión de calidad cada 400 pliegos. Escribe: cuántas revisiones habrá, tres reglas de seguridad u orden que respetarías (resguardos, ropa, residuos u otra) con una razón cada una, "
        "y qué anotarías en el registro si una revisión muestra un problema.",
        "Revisiones: 12.000 ÷ 400 = 30. Reglas: dejar los resguardos en su lugar porque protegen de partes en movimiento; usar ropa ajustada y cabello recogido porque lo suelto se atrapa; guardar los trapos con tinta en un contenedor rotulado porque son residuos. Registro: número de revisión, qué se observó, a quién se avisó y la decisión.",
        ["calcula bien las revisiones", "nombra tres reglas con razón", "describe un registro con hechos y responsable"],
        ["hoja con el cálculo, tres reglas y el registro"],
        ["escribir pasos para operar la máquina", "no dar razones", "registrar sin responsable"],
        "Pregunta: «¿por qué se anota la revisión?». Si responde 'por costumbre', repasa que el registro es la evidencia del control."),
    reinforce="Haz una lista de cinco cuidados de orden, limpieza o salud que debe respetar el equipo de impresión.",
    extend="Explica con un ejemplo inventado por qué el registro de una revisión protege a todo el equipo.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (glosario y defectos de ejemplo, inventados). Arranque: primeros pliegos de la tirada, que se usan para dejar la impresión como el OK. Merma de arranque: pliegos que se pierden en esa etapa. "
     "Planilla de control: hoja donde se anotan las mediciones de cada revisión. Calce: alineación de los colores entre sí. Densidad: medida de cuánta tinta hay en un parche. "
     "Defectos: mancha (tinta donde no debe haber), calce deficiente (colores corridos que dejan bordes con halo) y color desparejo (tono distinto entre pliegos). "
     "Un defecto crítico hace inservible el producto; un defecto menor no afecta su uso.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario del control de calidad durante la impresión: arranque, merma, planilla de control, calce, densidad y tipos de defectos.",
    prior=["Conozco el OK de impresión y las revisiones de calidad.", "Sé qué es una tolerancia.", "Sé calcular porcentajes simples."],
    explain=[
        "El arranque son los primeros pliegos de la tirada, que se imprimen mientras se deja el resultado igual al OK de impresión. Los pliegos perdidos en esa etapa son la merma de arranque, y se pide papel de más para cubrirla. La planilla de control es la hoja donde se anotan las mediciones de cada revisión, con la fecha y el nombre de quien midió.",
        "El calce es la alineación de los colores entre sí: con calce deficiente, los colores quedan corridos y los bordes se ven con un halo. La densidad mide cuánta tinta hay en un parche. Otros defectos son la mancha, que es tinta donde no debe haber, y el color desparejo, que es un tono distinto entre pliegos. Un defecto crítico hace inservible el producto; uno menor no afecta su uso.",
        "Reconocer los defectos permite describirlos con precisión en la planilla y avisar a la persona responsable. Aquí aprendes el vocabulario; ajustar la máquina para corregirlos es tarea de personas autorizadas." + MAQ,
    ],
    vocab=[("arranque", "primeros pliegos de la tirada hasta dejar la impresión como el OK"), ("merma de arranque", "pliegos que se pierden durante el arranque"), ("planilla de control", "hoja donde se anotan las mediciones de cada revisión"), ("calce", "alineación de los colores entre sí"), ("mancha", "tinta donde no debe haber"), ("defecto crítico", "defecto que deja inservible el producto")],
    worked=[
        ("Porcentaje de merma", "En una tirada de ejemplo de 10.000 pliegos se perdieron 200 en el arranque. ¿Qué porcentaje es?", ["Porcentaje = parte × 100 ÷ total.", "200 × 100 ÷ 10.000 = 2."], "2 %"),
        ("Nombrar el defecto", "En un pliego de ejemplo, los colores están corridos y los bordes tienen un halo. ¿Qué defecto es?", ["Los colores no están alineados entre sí.", "Eso es calce deficiente."], "Calce deficiente"),
    ],
    mistakes=[("Llamar «mancha» a cualquier problema de color.", "Cada defecto tiene un nombre y una causa distinta: mancha, calce deficiente o color desparejo.", "Describe qué ves y usa el nombre que corresponde."),
              ("Anotar en la planilla «salió mal» sin más.", "Una anotación sin datos no permite decidir ni repetir el control.", "Escribe qué defecto, en qué pliego y qué medición tienes.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el calce?", "La alineación de los colores entre sí", "El tamaño del papel", "El nombre de una tinta", "Un buen calce deja los colores exactamente superpuestos donde corresponde."),
        ("abc", "En Gráfica: ¿qué es una planilla de control?", "La hoja donde se anotan las mediciones de cada revisión", "Una máquina de corte", "Un tipo de papel", "La planilla es el registro del control durante la tirada."),
        ("abc", "{F} ¿Qué es el arranque?", "Los primeros pliegos de la tirada, mientras se deja la impresión como el OK", "El final de la tirada", "La limpieza del taller", "El arranque ocurre al comienzo y consume parte del papel."),
        ("abc", "{F} Un pliego tiene tinta en un lugar donde no debe haber. ¿Qué defecto es?", "Mancha", "Calce deficiente", "Color desparejo", "La mancha es tinta donde no debe haber."),
        ("abc", "{F} Dos pliegos de la misma tirada tienen tonos distintos. ¿Qué defecto es?", "Color desparejo", "Mancha", "Calce deficiente", "Un tono distinto entre pliegos es color desparejo."),
        ("=", "{F} En una tirada de 8.000 pliegos se perdieron 400 en el arranque. ¿Qué porcentaje es la merma de arranque?", "400*100//8000", "Se multiplica la parte por 100 y se divide por el total.", " %"),
        ("abc", "{F} Un defecto hace que el producto no se pueda entregar. ¿Cómo se clasifica?", "Defecto crítico", "Defecto menor", "No es un defecto", "Un defecto que deja inservible el producto es crítico."),
        ("abc", "{F} Un pequeño punto de tinta en el borde exterior de un folleto que será cortado no afecta el uso. ¿Cómo se clasifica?", "Defecto menor", "Defecto crítico", "Calce deficiente", "Si no afecta el uso del producto, el defecto es menor."),
        ("=", "{F} De 400 pliegos revisados, 12 tienen calce deficiente. ¿Cuántos no tienen ese defecto?", "400-12", "Al total revisado se le restan los pliegos con defecto.", " pliegos"),
        ("abc", "{F} Un compañero anota en la planilla «salió mal». ¿Qué le sugieres?", "Anotar el defecto, el pliego y la medición, porque «salió mal» no permite decidir", "Dejarlo así porque es rápido", "Borrar la anotación", "Una anotación con datos permite decidir y repetir el control."),
        ("abc", "{F} Los bordes de las letras tienen halo de color en toda la tirada. ¿Qué defecto describe mejor la planilla?", "Calce deficiente", "Mancha", "Color desparejo", "El halo en los bordes viene de colores corridos."),
        ("abc", "{F} Un estudiante en visita propone corregir el calce moviendo algo de la máquina. ¿Qué respondes?", "Eso lo hace solo una persona autorizada; yo anoto y aviso", "Que lo haga si le parece fácil", "Que lo haga si usa guantes", "Ajustar una máquina exige autorización y capacitación."),
        ("=", "{F} Si el 2 % de una tirada de 10.000 pliegos se pierde en el arranque, ¿cuántos pliegos son?", "10000*2//100", "El porcentaje se multiplica por el total y se divide por 100.", " pliegos"),
    ],
    ctx=("abc", "En la revisión de una tirada de ejemplo notas que un pliego tiene una pequeña mancha lejos del texto y otro tiene los colores corridos. El encargado pregunta cuál es más grave. ¿Qué respondes?", "Depende de si afecta el uso: describiría ambos con el defecto y su ubicación, y el encargado decide", "Los dos son iguales siempre", "Ninguno importa", "La gravedad se decide con el criterio de defecto crítico o menor y quedando anotada la descripción."),
    sc=[
        ("En Gráfica: ¿qué es la merma de arranque?", "Los pliegos que se pierden en los primeros ajustes", "Se pierden al dejar la impresión como el OK."),
        ("¿Qué defecto deja tinta donde no debe haber?", "La mancha", "El nombre describe exactamente ese problema."),
        ("¿Qué defecto es el color desparejo?", "Un tono distinto entre pliegos", "Se nota al comparar pliegos de la misma tirada."),
    ],
    op=("Una planilla de ejemplo anota estos hallazgos: (a) pliego 300, tinta en el margen blanco; (b) pliego 800, letras con halo de color; (c) pliego 1.200, rojo más oscuro que en el pliego 300. Nombra el defecto de cada uno, clasifica cada uno como crítico o menor con una razón, "
        "y calcula el porcentaje de merma si se perdieron 150 pliegos de una tirada de 5.000 en el arranque.",
        "(a) mancha, menor si no afecta el uso, porque está en el margen; (b) calce deficiente, crítico si dificulta leer; (c) color desparejo, crítico si el cliente exige un color constante. Merma: 150 × 100 ÷ 5.000 = 3 %.",
        ["nombra los tres defectos", "clasifica con una razón", "calcula el porcentaje"],
        ["tabla con defecto, clasificación y razón, más el cálculo"],
        ["llamar mancha a todo", "clasificar sin razón", "calcular el porcentaje al revés"],
        "Pregunta: «¿qué hace crítico a un defecto?». Si responde 'que se ve feo', recuerda que importa si deja inservible el producto."),
    reinforce="Dibuja tres cuadros pequeños y rotula uno con mancha, otro con calce deficiente y otro con color desparejo, describiendo en una frase cómo se vería cada uno.",
    extend="Explica por qué conviene usar los nombres precisos de los defectos al informar a la persona responsable.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (planilla de control de ejemplo, inventada). Estándar: densidad del negro 170 con tolerancia ± 6; calce con tolerancia máxima de 3 décimas de milímetro (los valores de calce de abajo están en décimas de milímetro; los de densidad son unidades de ejemplo). Revisión cada 500 pliegos. "
     "Revisión 1 (pliego 500): negro 171, calce 1. Revisión 2 (pliego 1.000): negro 173, calce 2. Revisión 3 (pliego 1.500): negro 179, calce 2. Revisión 4 (pliego 2.000): negro 172, calce 4. "
     "Si una revisión falla, se separan los pliegos impresos desde la última revisión que cumplía hasta la que falló.")
build(
    O5, 3, F,
    use="Aprenderé a leer una planilla de control, detectar revisiones fuera de tolerancia y decidir qué pliegos se separan y a quién se avisa.",
    prior=["Conozco tolerancia, densidad y calce.", "Sé restar y comparar números.", "Sé leer una tabla."],
    explain=[
        "Una planilla de control reúne las mediciones de cada revisión. En cada una se compara el valor medido con el valor del estándar y su tolerancia. La densidad del negro cumple si la diferencia con 170 es 6 o menos, y el calce cumple si es 3 décimas de milímetro o menos. Una revisión cumple solo si todas sus mediciones cumplen.",
        "Cuando una revisión falla, los pliegos impresos desde la última revisión que cumplía hasta la que falló quedan en duda: se separan y se revisan. La cantidad se calcula restando los números de pliego de las dos revisiones. El operador no corrige por su cuenta: anota, separa si corresponde y avisa a la persona responsable, que autoriza los ajustes.",
        "Las cifras de esta ficha son de ejemplo. Los valores reales los fija el estándar del taller y la norma vigente." + MAQ,
    ],
    vocab=[("planilla de control", "hoja con las mediciones de cada revisión"), ("revisión", "medición de una muestra comparada con el estándar"), ("décima de milímetro", "una décima parte de un milímetro; se usa para medir el calce"), ("separar", "apartar pliegos en duda para revisarlos")],
    worked=[
        ("Revisar un valor", "Una revisión de ejemplo mide densidad 163 con objetivo 170 y tolerancia ± 5. ¿Cumple?", ["La diferencia es 170 − 163 = 7.", "7 es mayor que 5."], "No cumple"),
        ("Pliegos a separar", "La última revisión buena fue en el pliego 600 y la que falló en el 900. ¿Cuántos pliegos quedan en duda?", ["Se resta el pliego de la última revisión buena al de la que falló.", "900 − 600 = 300."], "300 pliegos"),
    ],
    mistakes=[("Seguir imprimiendo sin avisar «porque la próxima revisión seguro sale bien».", "Los pliegos de cada intervalo quedan en duda y el problema puede crecer.", "Anota, separa los pliegos en duda y avisa a la persona responsable."),
              ("Separar solo el pliego que se midió.", "El problema pudo comenzar en cualquier punto desde la última revisión buena.", "Separa todos los pliegos del intervalo.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una revisión en una planilla de control?", "La medición de una muestra comparada con el estándar", "El cambio de turno", "El pago de la tirada", "Cada revisión compara lo medido con el estándar."),
        ("abc", "{F} ¿Cuál es la tolerancia de la densidad del negro en la ficha?", "± 6", "± 3", "± 10", "La ficha fija 170 con tolerancia ± 6."),
        ("=", "{F} ¿Cuál es la diferencia de la densidad del negro en la revisión 3?", "179-170", "Se resta el objetivo al valor medido.", " unidades"),
        ("abc", "{F} ¿Qué revisión falla en densidad del negro?", "La revisión 3", "La revisión 1", "La revisión 2", "En la revisión 3 la diferencia es 9, mayor que 6; en las otras es 1, 3 y 2."),
        ("abc", "{F} ¿Qué revisión falla en calce?", "La revisión 4", "La revisión 3", "La revisión 1", "El calce de la revisión 4 mide 4 décimas, más que la tolerancia de 3."),
        ("=", "{F} Si la revisión 3 falla y la última buena fue la 2, ¿cuántos pliegos se separan?", "1500-1000", "Se resta el pliego de la última revisión buena al de la que falló.", " pliegos"),
        ("=", "{F} Las revisiones 3 y 4 fallan. Desde la última revisión buena (la 2) hasta la 4, ¿cuántos pliegos quedan en duda?", "2000-1000", "Se resta el pliego de la última revisión buena al de la última que falló.", " pliegos"),
        ("abc", "{F} Un compañero dice: «la revisión 3 solo falló por un poco, seguimos». ¿Qué respondes?", "La tolerancia se cumple o no se cumple; hay que anotar, separar y avisar", "Tiene razón: un poco no importa", "Hay que borrar la medición", "Un valor fuera de tolerancia no se considera aceptable aunque la diferencia sea pequeña."),
        ("abc", "¿Qué haces al detectar una revisión fuera de tolerancia?", "Anoto el hecho, separo los pliegos en duda y aviso a la persona responsable", "Imprimo el resto antes de avisar", "Cambio los valores de la planilla", "Registrar, separar y avisar permite decidir con respaldo."),
        ("abc", "{F} ¿Cumple una revisión con negro 168 y calce 2?", "Sí: 168 está a 2 de 170 y 2 es menor que 3", "No: 168 es menor que 170", "No: 2 supera la tolerancia del calce", "Ambos valores están dentro de sus tolerancias."),
        ("abc", "{F} La revisión 2 tiene negro 173 y calce 2. Una compañera dice que falla porque 173 es mayor que 170. ¿Qué respondes?", "Cumple: la diferencia es 3 y la tolerancia es 6", "Falla, porque 173 es mayor que 170", "Falla, porque el calce es 2", "La tolerancia permite diferencias de hasta 6 hacia arriba o abajo."),
        ("abc", "El operador de ejemplo quiere corregir el color por su cuenta apenas ve un valor fuera de tolerancia. ¿Qué corresponde?", "Avisar a la persona responsable, que autoriza los ajustes", "Corregir de inmediato sin avisar", "Esperar a que termine el turno", "Los ajustes los autoriza quien responde del trabajo."),
        ("=", "{F} Si las revisiones cada 500 pliegos llegan hasta el pliego 2.000, ¿cuántas revisiones se hicieron?", "2000//500", "Se divide el último pliego revisado por el intervalo.", " revisiones"),
    ],
    ctx=("abc", "Al final del turno, el jefe te pide la planilla de ejemplo y notas que la revisión 3 no tiene anotada la decisión. ¿Qué haces?", "Le informo que falta registrar la decisión y pregunto qué se decidió para anotarlo con fecha", "Invento una decisión para completar", "Borro la revisión 3", "El registro debe reflejar lo que realmente se decidió, sin inventar."),
    sc=[
        ("En Gráfica: ¿cuándo cumple una revisión?", "Cuando todas sus mediciones cumplen", "Una medición fuera de tolerancia basta para fallar."),
        ("¿Cómo se calcula cuántos pliegos separar?", "Restando los pliegos de las dos revisiones", "El intervalo va desde la última revisión buena hasta la que falló."),
        ("¿Quién autoriza los ajustes?", "La persona responsable", "El operador anota y avisa antes de intervenir."),
    ],
    op=("Planilla de ejemplo. Estándar: densidad del cian 140 con tolerancia ± 5; revisión cada 400 pliegos. Revisión 1 (pliego 400): cian 142. Revisión 2 (pliego 800): cian 146. Revisión 3 (pliego 1.200): cian 148. Revisión 4 (pliego 1.600): cian 141. "
        "Calcula la diferencia de cada revisión, indica cuáles fallan, cuántos pliegos separarías si falla la primera revisión mala y qué anotarías en el registro.",
        "Diferencias: 2, 6, 8, 1. Fallan la revisión 2 (6 > 5) y la 3 (8 > 5). La última revisión buena antes de la primera falla es la 1 (pliego 400), y la primera falla es la 2 (pliego 800): se separan 800 − 400 = 400 pliegos. Registro: «revisión 2, cian 146, fuera de tolerancia; se separan 400 pliegos y se avisa a la persona responsable».",
        ["calcula bien las diferencias", "identifica las revisiones que fallan", "calcula pliegos a separar y escribe un registro"],
        ["tabla de revisiones, el cálculo y el registro"],
        ["usar el pliego equivocado", "no avisar a la persona responsable", "decir que cumple porque está cerca"],
        "Pregunta: «¿por qué la revisión 2 falla si solo difiere en 6?». Si no responde, revisa que la tolerancia es ± 5."),
    reinforce="Inventa una planilla con cuatro revisiones y marca cuáles cumplen con una tolerancia que fijes.",
    extend="Explica por qué se separa un intervalo de pliegos y no solo el pliego medido.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (producción de ejemplo, inventada). Tirada: 10.000 pliegos buenos. Merma de ejemplo: 5 % de la tirada. Velocidad de la máquina: 3.500 pliegos por hora. Preparación (arranque): 90 minutos. "
     "Costo de la máquina: $40.000 por hora (de ejemplo). Costo del papel: $90 por pliego (de ejemplo).")
build(
    O5, 4, F,
    use="Aprenderé a calcular cuántos pliegos hay que imprimir, cuánto dura una tirada y cuánto cuesta, para planificar el trabajo con datos.",
    prior=["Sé calcular porcentajes simples.", "Conozco la merma y la velocidad.", "Sé sumar tiempos y multiplicar costos."],
    explain=[
        "Para planificar una tirada se parte de los pliegos buenos que pide la OT. Como parte del papel se pierde (la merma), hay que imprimir más de los que se entregan: pliegos a imprimir = pliegos buenos + merma. La merma de ejemplo es un porcentaje de la tirada, y el porcentaje de una cantidad se calcula multiplicando por el porcentaje y dividiendo por 100.",
        "El tiempo de impresión es los pliegos a imprimir divididos por la velocidad en pliegos por hora. El tiempo total suma la preparación. El costo de máquina es el tiempo en horas por el costo por hora, y se puede calcular a partir de los minutos. Con el costo total se obtiene el costo por pliego bueno, dividiendo por los pliegos entregados.",
        "Estos cálculos permiten avisar plazos y costos al jefe de turno. Las cifras son de ejemplo: la realidad depende de la máquina, del papel y de los ajustes que hagan las personas autorizadas." + MAQ,
    ],
    vocab=[("pliegos buenos", "pliegos que cumplen y se entregan"), ("pliegos a imprimir", "pliegos buenos más la merma"), ("velocidad", "pliegos que se imprimen por hora"), ("costo por pliego bueno", "costo total dividido por los pliegos entregados")],
    worked=[
        ("Pliegos con merma", "Una tirada de ejemplo de 2.000 pliegos buenos con 10 % de merma. ¿Cuántos pliegos se imprimen?", ["El 10 % de 2.000 es 200.", "2.000 + 200 = 2.200."], "2.200 pliegos"),
        ("Tiempo de impresión", "Se imprimen 4.800 pliegos a 2.400 pliegos por hora. ¿Cuántas horas dura?", ["Tiempo = pliegos ÷ velocidad.", "4.800 ÷ 2.400 = 2."], "2 horas"),
    ],
    mistakes=[("Imprimir solo los pliegos buenos y quedarse corto.", "La merma ocurre siempre y los pliegos buenos no alcanzan.", "Suma la merma antes de planificar."),
              ("Olvidar sumar la preparación al tiempo total.", "La preparación ocupa tiempo de máquina aunque aún no salgan pliegos.", "Suma la preparación al tiempo de impresión.")],
    T=[
        ("abc", "En Gráfica: ¿qué son los pliegos a imprimir?", "Los pliegos buenos más la merma", "Solo los pliegos buenos", "Solo la merma", "Se imprimen más de los que se entregan porque parte se pierde."),
        ("abc", "{F} ¿Cuál es la velocidad de la máquina?", "3.500 pliegos por hora", "9.000 pliegos por hora", "350 pliegos por hora", "La ficha indica 3.500 pliegos por hora."),
        ("=", "{F} ¿Cuántos pliegos son la merma?", "10000*5//100", "El porcentaje se multiplica por la tirada y se divide por 100.", " pliegos"),
        ("=", "{F} ¿Cuántos pliegos hay que imprimir en total?", "10000+10000*5//100", "A los pliegos buenos se les suma la merma.", " pliegos"),
        ("=", "{F} ¿Cuántas horas dura la impresión de todos los pliegos?", "(10000+10000*5//100)//3500", "Se dividen los pliegos a imprimir por la velocidad.", " horas"),
        ("=", "{F} ¿Cuántos minutos dura la impresión?", "(10000+10000*5//100)//3500*60", "Se pasan a minutos las horas de impresión.", " minutos"),
        ("=", "{F} ¿Cuántos minutos dura el trabajo completo, con la preparación?", "90+(10000+10000*5//100)//3500*60", "Se suma la preparación al tiempo de impresión.", " minutos"),
        ("=", "{F} ¿Cuánto cuesta la máquina durante el trabajo completo?", "(90+(10000+10000*5//100)//3500*60)*40000//60", "Se multiplican los minutos por el costo de cada minuto de máquina.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el papel de la merma?", "10000*5//100*90", "Se multiplican los pliegos de merma por el costo de cada pliego.", " pesos"),
        ("abc", "{F} Un compañero dice: «con 10.000 pliegos basta, la merma no es real». ¿Qué respondes?", "La merma ocurre y sin ella faltarían pliegos para entregar los 10.000 buenos", "Tiene razón: no existe", "La merma solo sirve para el costo", "Los pliegos perdidos en pruebas y ajustes deben estar previstos."),
        ("abc", "{F} Un cliente pide el trabajo en 3 horas. Con la preparación y la impresión de la ficha, ¿es posible?", "No: el trabajo dura 270 minutos y 3 horas son 180", "Sí: dura 180 minutos", "Sí: la preparación no cuenta", "El trabajo completo son 90 + 180 = 270 minutos, más que 3 horas."),
        ("abc", "{F} ¿Qué parte del tiempo total ocupa la impresión (sin preparación)?", "Dos tercios: 180 de 270 minutos", "La mitad", "Un cuarto", "180 de 270 minutos equivale a dos tercios."),
        ("=", "{F} ¿Cuánto cuesta en total el papel de todos los pliegos impresos más el tiempo de máquina del trabajo completo?", "(10000+10000*5//100)*90+(90+(10000+10000*5//100)//3500*60)*40000//60", "Se suman el costo del papel impreso y el costo de la máquina durante el trabajo.", " pesos"),
    ],
    ctx=("abc", "El cliente de ejemplo te pregunta por qué cobras 10.500 pliegos si pidió 10.000. ¿Qué le respondes?", "Que parte del papel se pierde en pruebas y ajustes, y que esa merma está prevista en el cálculo", "Que se cobran pliegos de más por costumbre", "Que fue un error que se corregirá", "La merma es una pérdida real y se explica con datos."),
    sc=[
        ("En Gráfica: ¿cómo se calcula el tiempo de impresión?", "Pliegos a imprimir divididos por la velocidad", "La velocidad dice cuántos pliegos salen por hora."),
        ("¿Qué se suma al tiempo de impresión para el total?", "La preparación", "La preparación ocupa tiempo de máquina."),
        ("¿Cómo se calcula el costo por pliego bueno?", "Dividiendo el costo total por los pliegos entregados", "Reparte el costo entre los pliegos que se entregan."),
    ],
    op=("Producción de ejemplo: 6.000 pliegos buenos, merma de 5 %, velocidad de 3.150 pliegos por hora, preparación de 60 minutos y costo de máquina de $30.000 por hora. "
        "Calcula los pliegos a imprimir, la duración de la impresión en minutos, el tiempo total, el costo de la máquina y cuántos pliegos de merma se pierden.",
        "Merma: 6.000 × 5 ÷ 100 = 300. Pliegos a imprimir: 6.300. Impresión: 6.300 ÷ 3.150 = 2 horas = 120 minutos. Total: 60 + 120 = 180 minutos. Costo de máquina: 3 horas × 30.000 = 90.000 pesos. Merma: 300 pliegos.",
        ["calcula bien la merma y los pliegos a imprimir", "calcula tiempos de impresión y total", "calcula el costo de máquina"],
        ["hoja con los cinco cálculos"],
        ["no sumar la merma", "olvidar la preparación", "calcular el costo con los minutos sin pasarlos a horas"],
        "Pregunta: «¿qué suma el tiempo total?». Si responde solo la impresión, repasa el papel de la preparación."),
    reinforce="Inventa una tirada de 4.000 pliegos con merma de 5 % y calcula cuántos pliegos se imprimen.",
    extend="Explica cómo cambiaría el tiempo total si la velocidad subiera a 4.200 pliegos por hora (usa los datos de la ficha).",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (decisión de ejemplo, inventada). Tirada: 10.000 pliegos buenos. En la revisión del pliego 4.000 el color está fuera de tolerancia. Alternativa A: detener y avisar; la parada dura 40 minutos y se pierden 200 pliegos más. "
     "Alternativa B: seguir sin avisar y revisar al final; si el cliente rechaza el color, se pierden los 6.000 pliegos restantes. Costo de la máquina: $30.000 por hora; costo del papel: $90 por pliego (de ejemplo). "
     "Criterio de aceptación del lote: al menos 95 % de pliegos conformes.")
build(
    O5, 5, F,
    use="Aprenderé a comparar alternativas ante un problema de calidad en la impresión, a calcular costos y a verificar si un lote cumple el criterio de aceptación.",
    prior=["Conozco la planilla de control y los defectos.", "Sé calcular porcentajes y costos.", "Sé qué es un criterio de aceptación."],
    explain=[
        "Cuando una revisión muestra un problema, se pueden comparar alternativas con datos: tiempo perdido, papel perdido y riesgo de rechazo. Detener y avisar cuesta tiempo y papel, pero limita el problema. Seguir sin avisar puede parecer más rápido, pero si el cliente rechaza el lote se pierde todo lo impreso después de la falla, además de no tener registro de lo decidido.",
        "El costo de una parada se calcula con los minutos y el costo de la máquina por hora; el costo del papel perdido se calcula con los pliegos perdidos por su precio. Al terminar, se verifica la calidad: el porcentaje de pliegos conformes se compara con el criterio de aceptación. Si no cumple, se informa y se decide con la persona responsable.",
        "Ocultar un problema para cumplir el plazo es una falta ética y puede perjudicar al cliente. La decisión se toma con la persona responsable y queda registrada." + MAQ,
    ],
    vocab=[("alternativa", "una de las opciones entre las que se decide"), ("parada", "tiempo en que la máquina está detenida"), ("rechazo", "decisión del cliente de no recibir un lote"), ("conformes", "pliegos que cumplen los estándares")],
    worked=[
        ("Costo de una parada", "Una parada de ejemplo dura 30 minutos y la máquina cuesta $20.000 por hora. ¿Cuánto cuesta?", ["Media hora cuesta la mitad de una hora.", "20.000 ÷ 2 = 10.000."], "$10.000"),
        ("Verificar un lote", "Un lote de ejemplo tiene 920 pliegos conformes de 1.000 y el criterio es 95 %. ¿Se acepta?", ["920 × 100 ÷ 1.000 = 92.", "92 es menor que 95."], "No, no se acepta"),
    ],
    mistakes=[("Elegir seguir sin avisar para «no perder tiempo».", "El riesgo de perder toda la tirada restante es mucho mayor que la pérdida de la parada.", "Compara los costos y el riesgo antes de decidir."),
              ("Aceptar el lote sin calcular el porcentaje de pliegos conformes.", "El criterio se verifica con un dato, no con la impresión de unos pocos pliegos.", "Calcula el porcentaje y compáralo con el mínimo.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una parada?", "El tiempo en que la máquina está detenida", "Un tipo de defecto de color", "Una orden del cliente", "Una parada consume tiempo de máquina."),
        ("abc", "{F} ¿Qué pasa en la alternativa A?", "Se detiene 40 minutos y se pierden 200 pliegos más", "Se sigue sin avisar", "Se pierden los 6.000 pliegos restantes", "La alternativa A limita el problema a costa de una parada."),
        ("=", "{F} ¿Cuánto cuesta la parada de 40 minutos?", "30000*40//60", "Se multiplica el costo por hora por los minutos y se divide por 60.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el papel de los 200 pliegos que se pierden en la alternativa A?", "200*90", "Se multiplican los pliegos perdidos por su precio.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta en total la alternativa A?", "30000*40//60+200*90", "Se suman el costo de la parada y del papel perdido.", " pesos"),
        ("=", "{F} Si el cliente rechaza el lote en la alternativa B, ¿cuánto cuesta el papel de los 6.000 pliegos restantes?", "6000*90", "Se multiplican los pliegos perdidos por su precio.", " pesos"),
        ("abc", "{F} Si el cliente rechaza el lote, ¿qué alternativa resulta más cara en papel?", "La B, por perder 6.000 pliegos", "La A, por perder 200 pliegos", "Cuestan lo mismo", "Perder 6.000 pliegos cuesta mucho más que perder 200."),
        ("abc", "{F} ¿Por qué la alternativa B es poco responsable aunque parezca más rápida?", "Porque oculta el problema y arriesga perder todo lo que falta imprimir", "Porque usa menos papel siempre", "Porque la máquina funciona más lento", "Seguir sin avisar impide limitar el problema y no deja registro."),
        ("abc", "{F} Un compañero propone la B «para cumplir el plazo». ¿Qué respondes?", "El plazo no justifica ocultar un defecto que puede inutilizar los 6.000 pliegos restantes", "Tiene razón: el plazo es lo más importante", "El defecto no importa", "La calidad y la honestidad con el cliente pesan más que un ahorro de tiempo incierto."),
        ("=", "{F} Al terminar, 9.700 de 10.000 pliegos son conformes. ¿Qué porcentaje es conforme?", "9700*100//10000", "Se multiplican los conformes por 100 y se divide por el total.", " %"),
        ("abc", "{F} Con 9.700 conformes de 10.000, ¿se acepta el lote según el criterio?", "Sí, porque 97 % supera el 95 %", "No, porque hay 300 pliegos no conformes", "No, porque el criterio exige 100 % de pliegos conformes", "El criterio permite hasta 5 % de pliegos no conformes."),
        ("abc", "{F} Si fueran 9.400 conformes de 10.000, ¿qué corresponde?", "Informar que no cumple el 95 % y decidir con la persona responsable", "Aceptarlo igual", "Cambiar el criterio sin avisar", "94 % está bajo el mínimo, así que se informa y se decide con respaldo."),
        ("=", "{F} Por cada 1.000 pliegos, ¿cuántos pueden ser no conformes y aun cumplir el criterio de 95 %?", "1000-950", "Al total se le restan los conformes mínimos exigidos.", " pliegos"),
    ],
    ctx=("abc", "Faltan 20 minutos para la hora de entrega y notas un color fuera de tolerancia. El cliente está esperando. ¿Qué haces?", "Aviso de inmediato a la persona responsable con los datos y propongo detener y revisar", "Entrego sin decir nada", "Cambio los datos de la planilla", "El plazo no justifica entregar con un defecto no informado."),
    sc=[
        ("En Gráfica: ¿qué se compara al decidir entre alternativas?", "Costos, tiempos y riesgos", "Con datos se elige la opción más responsable."),
        ("¿Cómo se verifica un lote al final?", "Comparando el porcentaje conforme con el criterio", "El criterio de aceptación fija el mínimo."),
        ("¿Qué haces si descubres un defecto cerca del plazo?", "Aviso a la persona responsable", "El plazo no justifica ocultar un problema de calidad."),
    ],
    op=("Caso de ejemplo. Tirada de 5.000 pliegos buenos; en el pliego 2.000 el color falla. Alternativa A: detener 30 minutos y perder 100 pliegos más; alternativa B: seguir sin avisar y arriesgar los 3.000 pliegos restantes. Máquina: $24.000 por hora; papel: $60 por pliego. "
        "Calcula el costo de A, el costo del papel que se arriesga en B, escribe cuál recomiendas y por qué, y si al final hay 4.800 conformes de 5.000 con criterio de 95 %, di si se acepta.",
        "A: parada de 30 minutos = 12.000 pesos y 100 pliegos × 60 = 6.000, total 18.000. B arriesga 3.000 × 60 = 180.000 de papel. Recomiendo A porque limita la pérdida, informa a la persona responsable y deja registro. Conformes: 4.800 × 100 ÷ 5.000 = 96 %, mayor que 95: se acepta.",
        ["calcula el costo de A y el riesgo de B", "recomienda A con razones de calidad y registro", "verifica el porcentaje del lote"],
        ["hoja con cuatro cálculos y la recomendación"],
        ["solo comparar tiempo", "ocultar el defecto", "calcular el porcentaje con otro total"],
        "Pregunta: «¿qué pierdes en B si se rechaza?». Si dice 'tiempo', pídele que calcule el papel perdido."),
    reinforce="Escribe dos alternativas que el equipo podría tomar ante un problema de color y una ventaja y un riesgo de cada una.",
    extend="Explica por qué un registro de la decisión protege tanto al taller como al cliente.",
)

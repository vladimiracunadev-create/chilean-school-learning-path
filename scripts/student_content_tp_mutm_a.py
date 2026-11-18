"""Muebles y Terminaciones en Madera (3.º y 4.º medio TP): OAE-01 (medir y acopiar insumos de madera: recepción, registro y calidad) y OAE-02 (leer y utilizar diseños de muebles: planos, despieces, escalas y cotas). Solo conceptos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_mutm_common import AVISO, EMER, build

O1 = "TP-MUTM-3y4-OAE-01"
O2 = "TP-MUTM-3y4-OAE-02"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (bodega de ejemplo, inventada). El taller ficticio «Carpintería Los Boldos» recibe un camión con 8 paquetes: 5 de madera aserrada, 2 de tableros y 1 de piezas remanufacturadas. Cuadrilla de bodega: 4 personas. "
     "Riesgos anotados: caída de pilas mal apoyadas, golpes por manipulación manual de cargas, astillas, polvo de madera al mover los paquetes y tránsito de vehículos en el patio. "
     "Medidas anotadas: piso firme y nivelado, pasillos señalizados entre pilas, guantes, lentes, calzado de seguridad, mascarilla indicada por el responsable, personal autorizado para mover cargas con equipos y registro de recepción firmado por el responsable.")
build(
    O1, 1, F,
    use="Aprenderé qué es acopiar y recibir madera, qué tipos de insumos llegan a un taller de muebles y qué riesgos tiene la bodega.",
    prior=["Sé qué es la jerarquía de controles.", "Sé sumar y restar números pequeños.", "Sé leer una ficha escrita."],
    explain=[
        "Acopiar es guardar los insumos de forma ordenada y segura hasta que se usen; recibir es verificar y registrar lo que llega. En un taller de muebles llegan tres grandes tipos de insumos: madera natural aserrada (tablas y vigas cortadas del tronco), piezas remanufacturadas (elaboradas a partir de madera natural, por ejemplo piezas unidas entre sí) y tableros (productos planos elaborados con madera). Cada tipo se anota en un registro que firma un responsable.",
        "La bodega tiene riesgos propios: pilas que pueden caer, golpes al mover cargas a mano, astillas, polvo de madera y vehículos en movimiento. Según la jerarquía de controles, primero se organiza el espacio (piso firme, pasillos señalizados, pilas estables) y al final se usan los elementos de protección personal (EPP), que nunca reemplazan una buena organización. Mover cargas con equipos lo hace solo personal autorizado; este cuaderno no enseña ese manejo.",
        TAIL,
    ],
    vocab=[("acopio", "almacenamiento ordenado y seguro de los insumos hasta su uso"), ("recepción", "verificación y registro de lo que llega al taller"), ("madera aserrada", "madera natural cortada del tronco en tablas o vigas"), ("pieza remanufacturada", "pieza elaborada a partir de madera natural, por ejemplo unida a otras"), ("tablero", "producto plano elaborado con madera"), ("EPP", "elemento de protección personal, último nivel de la jerarquía de controles")],
    worked=[
        ("Reconocer el documento", "Una bodeguera de ejemplo anota qué paquetes llegaron y los firma el responsable. ¿Cómo se llama ese documento?", ["Lo que se anota al recibir insumos queda en el registro de recepción.", "El responsable lo firma para dejar constancia."], "El registro de recepción"),
        ("Contar paquetes", "Llegan 11 paquetes y 4 son de tableros. ¿Cuántos no son de tableros?", ["Se restan los paquetes de tableros del total.", "11 menos 4 son 7."], "7 paquetes"),
    ],
    mistakes=[("Apilar sin pasillos porque «cabe más».", "Sin pasillos señalizados aumenta el riesgo de golpes y de caída de pilas.", "Se organiza el espacio con pasillos y pilas estables antes de pensar en EPP."),
              ("Creer que los guantes bastan para mover cualquier carga.", "El EPP es el último nivel y no evita esfuerzos ni caídas de pilas.", "Se combinan orden, personal autorizado para equipos y EPP.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es el acopio de insumos?", "El almacenamiento ordenado y seguro hasta que se usen", "El corte de la madera a la medida del mueble", "El barnizado antes de guardar las tablas", "Acopiar es guardar con orden; cortar o barnizar son otras etapas del trabajo."),
        ("abc", "En un taller de muebles, ¿qué es un tablero?", "Un producto plano elaborado con madera", "Una tabla cortada directamente del tronco", "Una herramienta para medir piezas", "El tablero es un producto elaborado; la tabla aserrada sale del tronco."),
        ("=", "{F} ¿Cuántos paquetes no son de madera aserrada?", "8-5", "Se restan los paquetes de madera aserrada del total que llegó.", " paquetes"),
        ("abc", "{F} ¿Cuál de estas medidas de la ficha es un elemento de protección personal?", "El calzado de seguridad", "Los pasillos señalizados", "El piso firme y nivelado", "El calzado lo usa cada persona; los pasillos y el piso organizan el espacio."),
        ("abc", "{F} ¿Qué riesgo de la ficha se relaciona con mover los paquetes a mano?", "Los golpes y esfuerzos por manipulación manual de cargas", "La intoxicación por solventes", "La descarga eléctrica de una máquina", "Mover paquetes a mano causa golpes y sobreesfuerzos; los otros no aparecen en la ficha."),
        ("abc", "{F} ¿Quién firma el registro de recepción según la ficha?", "El responsable", "El conductor del camión", "Cada persona de la cuadrilla", "La ficha indica que firma el responsable, que decide y deja constancia."),
        ("=", "{F} Cada integrante de la cuadrilla recibe guantes, lentes y calzado de seguridad. ¿Cuántas piezas de EPP se entregan?", "4*3", "Se multiplican las 4 personas por las 3 piezas que recibe cada una.", " piezas"),
        ("abc", "{F} Una pila está apoyada en un terreno blando y se inclina. ¿Qué corresponde?", "No acercarse a la pila y avisar al responsable para reorganizarla", "Apoyarse en ella para sostenerla mientras se reorganiza", "Subirse para comprobar si aguanta más peso", "Una pila inclinada puede caer; se evita la zona y se avisa a quien decide."),
        ("abc", "{F} Un paquete llega sin etiqueta y no se sabe si es madera aserrada o remanufacturada. ¿Qué corresponde?", "Anotarlo como observación y consultar al responsable antes de aceptarlo", "Aceptarlo y registrarlo como aserrado por parecerse a los otros", "Descartarlo sin avisar a nadie", "Sin etiqueta no se sabe qué es; se registra y se consulta, no se adivina."),
        ("ab", "{F} Una persona dice: «llevo meses en la bodega, puedo mover cargas con equipos sin autorización». ¿Qué respuesta es correcta?", "No: solo el personal autorizado mueve cargas con equipos", "Sí: la experiencia reemplaza la autorización", "La ficha exige personal autorizado, y la experiencia no reemplaza esa autorización."),
        ("abc", "{F} Un estudiante dice: «el polvo de madera es natural, así que no es un riesgo». ¿Qué respuesta es correcta?", "No: el polvo de madera puede irritar y afectar la respiración, y se controla", "Sí: lo natural nunca daña", "Sí, si se usa mascarilla basta con ignorarlo", "Que sea natural no lo hace inocuo; se controla con orden, ventilación y EPP."),
        ("=", "{F} Cada paquete de madera aserrada trae 30 tablas (dato de ejemplo). ¿Cuántas tablas aserradas llegaron?", "5*30", "Se multiplican los paquetes aserrados por las tablas de cada paquete.", " tablas"),
        ("abc", "{F} El responsable pide anotar los paquetes dañados. ¿Qué datos mínimos lleva el registro?", "Cuántos son, de qué tipo, qué daño tienen y quién lo detectó", "Solo el nombre del conductor", "Solo la hora de llegada del camión", "Un registro útil dice cuántos, de qué tipo, qué daño y quién lo vio."),
    ],
    ctx=("abc", "En una bodega de ejemplo, una pila de tablas cae y una persona queda atrapada. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar levantar la pila entre varios sin avisar", "Esperar a ver si la persona se libera sola", "Mover la pila sin ayuda puede causar otra caída; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es la recepción de insumos?", "Verificar y registrar lo que llega al taller", "Recibir es comprobar y dejar constancia de lo que llegó."),
        ("¿Qué tipos de insumos llegan a un taller de muebles según la clase?", "Madera aserrada, piezas remanufacturadas y tableros", "La clase presenta esos tres grandes tipos de insumos."),
        ("¿Quién puede mover cargas con equipos en la bodega?", "Solo personal autorizado", "Mover cargas con equipos exige autorización y capacitación."),
    ],
    op=("Bodega de ejemplo «Taller Quillay» (ficticio): llegan 9 paquetes, 6 de tableros y 3 de madera aserrada. Cuadrilla de 5 personas, cada una con guantes y calzado de seguridad. Riesgos: caída de pilas, golpes y polvo. Escribe (a) cuántos paquetes no son de tableros, (b) cuántas piezas de EPP se entregan, (c) una medida de organización del espacio y por qué va antes que el EPP, y (d) qué haces si una pila cae sobre alguien.",
        "(a) 9 menos 6 son 3 paquetes. (b) 5×2 son 10 piezas. (c) Pasillos señalizados y pilas estables, porque el EPP es el último nivel y no evita la caída. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula los paquetes que no son de tableros", "calcula las piezas de EPP", "propone una medida de organización con razón", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["decir que el EPP reemplaza el orden", "proponer levantar la pila sin ayuda", "confundir tablero con tabla aserrada"],
        "Pregunta: «¿por qué el orden del espacio va antes que los guantes?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe con tus palabras la diferencia entre madera aserrada, pieza remanufacturada y tablero, con un ejemplo de mueble para cada una.",
    extend="Explica por qué mover cargas con equipos exige personal autorizado aunque la persona tenga experiencia.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Orden de compra «OC-ej 31» del taller ficticio «Carpintería Los Boldos»: 60 tablas de madera aserrada, escuadría de 5 cm por 15 cm, largo de 3 m cada una, y 20 tableros. "
     "Guía de despacho «GD-ej 77» del proveedor ficticio «Proveedor Ejemplo Uno»: 56 tablas de la misma escuadría y largo, y 20 tableros. "
     "Registro de humedad de ejemplo de tres tablas: 19 %, 25 % y 22 %. Criterio de aceptación inventado para esta ficha: humedad máxima de 23 %.")
build(
    O1, 2, F,
    use="Aprenderé qué documentos acompañan la compra y la recepción de madera, qué es la escuadría y cómo se lee un registro de humedad.",
    prior=["Sé qué es el acopio y la recepción.", "Sé multiplicar y restar.", "Sé leer porcentajes simples."],
    explain=[
        "La orden de compra es el documento con que el taller pide los insumos: dice qué, cuánto y con qué medidas. La guía de despacho es el documento que emite el proveedor para indicar lo que realmente envía. Al recibir, se comparan ambos y se anotan las diferencias en el registro de recepción. La escuadría es la medida de la sección de una pieza, es decir, su ancho y su espesor; el largo se anota aparte.",
        "El contenido de humedad es el porcentaje de agua que tiene la madera en relación con su propio peso. Una persona capacitada lo mide con un instrumento y anota el valor; cada proyecto fija un máximo aceptable, que en esta clase es un valor inventado. Quien recibe compara el número con el criterio y decide aceptar o separar la pieza: no la corrige por su cuenta. Los roles son el proveedor, que despacha; el bodeguero, que recibe y registra; y el responsable de calidad, que decide.",
        TAIL,
    ],
    vocab=[("orden de compra", "documento con que el taller pide insumos: qué, cuánto y con qué medidas"), ("guía de despacho", "documento del proveedor que indica lo que realmente envía"), ("escuadría", "medida de la sección de una pieza: ancho y espesor"), ("contenido de humedad", "porcentaje de agua que tiene la madera respecto de su propio peso"), ("criterio de aceptación", "límite fijado por el proyecto para aceptar o rechazar"), ("responsable de calidad", "persona que decide si un insumo se acepta o se separa")],
    worked=[
        ("Comparar documentos", "Una orden de compra de ejemplo pide 90 tablas y la guía de despacho indica 85. ¿Cuántas tablas faltan?", ["Se compara lo pedido con lo despachado.", "90 menos 85 son 5."], "Faltan 5 tablas"),
        ("Leer una humedad", "Con un criterio inventado de máximo 12 %, una tabla registra 15 %. ¿Se acepta?", ["Se compara 15 % con el máximo de 12 %.", "15 % supera el máximo."], "No, se separa y se avisa al responsable de calidad"),
    ],
    mistakes=[("Creer que la guía de despacho y la orden de compra son el mismo documento.", "Una es el pedido del taller y la otra lo que envía el proveedor.", "Se comparan ambas y se anotan las diferencias en el registro."),
              ("Aceptar una pieza con humedad sobre el máximo porque «se ve bien».", "El criterio se aplica con el valor medido, no con la apariencia.", "Se separa la pieza y decide el responsable de calidad.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la orden de compra?", "El documento con que el taller pide los insumos", "El documento que emite el proveedor al despachar", "El registro de humedad de las tablas", "La orden la emite quien compra; la guía de despacho la emite quien vende."),
        ("abc", "¿Qué indica la escuadría de una tabla?", "El ancho y el espesor de su sección", "El largo total de la tabla", "El porcentaje de agua que contiene", "La escuadría describe la sección; el largo y la humedad son otros datos."),
        ("=", "{F} ¿Cuántas tablas faltan según la guía respecto de la orden de compra?", "60-56", "Se resta lo despachado a lo pedido para obtener lo que falta.", " tablas"),
        ("abc", "{F} ¿Qué documento emite el proveedor ficticio?", "La guía de despacho", "La orden de compra", "El registro de humedad", "Quien despacha emite la guía; la orden la emite el taller."),
        ("abc", "{F} ¿Cuál de las tres tablas medidas supera el criterio de aceptación?", "La de 25 %", "La de 19 %", "La de 22 %", "Solo 25 % es mayor que el máximo de 23 %."),
        ("=", "{F} ¿Cuántos centímetros cuadrados tiene la sección de una tabla (ancho por espesor)?", "5*15", "La sección es el producto del espesor por el ancho de la escuadría.", " cm²"),
        ("=", "{F} Según la guía, ¿cuántos metros lineales de tabla se despachan en total (largo de 3 m cada una)?", "56*3", "Se multiplican las tablas despachadas por el largo de cada una.", " m"),
        ("abc", "{F} Los tableros pedidos y despachados coinciden en 20. ¿Qué se anota en el registro de recepción sobre ellos?", "Que coinciden con la orden de compra", "Que faltan 20 tableros", "Que sobran 20 tableros", "Lo pedido y lo despachado son iguales, por lo tanto no hay diferencia."),
        ("abc", "{F} Una tabla mide 21 % de humedad. ¿Qué corresponde?", "Aceptarla porque no supera el máximo inventado de 23 %", "Rechazarla porque 21 es un número alto", "Esperar a que baje antes de registrarla", "Se compara el valor con el criterio: 21 % está bajo el máximo."),
        ("ab", "{F} Una persona dice: «la tabla de 25 % se ve seca, la acepto». ¿Qué respuesta es correcta?", "No: se aplica el criterio con el valor medido y decide el responsable de calidad", "Sí: la apariencia reemplaza el valor medido", "El criterio de la ficha es 23 % como máximo y se aplica con el valor medido."),
        ("abc", "{F} El bodeguero corrige a mano el número de la guía de despacho para que coincida con la orden. ¿Es correcto?", "No: las diferencias se anotan en el registro, no se alteran los documentos", "Sí: así queda ordenado", "Sí, si nadie lo nota", "Alterar un documento oculta la diferencia; se registra y se informa."),
        ("=", "{F} El proveedor reenvía las 4 tablas que faltaban. ¿Cuántas tablas despacha en total entre la guía original y el reenvío?", "56+4", "Al sumar lo ya despachado y las 4 reenviadas se llega a lo pedido.", " tablas"),
        ("abc", "{F} ¿Quién decide si una pieza con humedad dudosa se acepta o se separa?", "El responsable de calidad", "El conductor del camión", "El proveedor desde su oficina", "La decisión la toma el responsable de calidad del taller."),
    ],
    ctx=("abc", "En el taller de ejemplo, la guía de despacho dice 48 tableros y la orden de compra pedía 50. Un compañero propone anotar 50 «para cuadrar». ¿Qué corresponde?", "Anotar 48 en el registro, señalar la diferencia y avisar al responsable", "Anotar 50 y no decir nada", "No registrar nada hasta que lleguen los otros", "El registro debe reflejar lo que llegó y mostrar la diferencia."),
    sc=[
        ("¿Qué es la guía de despacho?", "El documento del proveedor que indica lo que realmente envía", "La guía la emite quien despacha y se compara con la orden."),
        ("En Muebles y Terminaciones en Madera: ¿qué es la escuadría?", "La medida de la sección de la pieza: ancho y espesor", "Describe la sección; el largo se anota aparte."),
        ("¿Qué se hace con una pieza que supera el criterio de humedad?", "Se separa y decide el responsable de calidad", "La pieza no se corrige por cuenta propia."),
    ],
    op=("Taller de ejemplo «Carpintería Ñire» (ficticio). Orden de compra: 80 tablas de 4 cm por 10 cm. Guía de despacho: 74 tablas. Humedades medidas en cuatro tablas: 18 %, 26 %, 20 % y 24 %; criterio inventado: máximo 22 %. Escribe (a) cuántas tablas faltan, (b) cuántas de las cuatro medidas se separan, (c) qué área tiene la sección de una tabla y (d) qué documento se compara con la guía.",
        "(a) 80 menos 74 son 6 tablas. (b) Se separan 2: 26 % y 24 %. (c) 4×10 son 40 cm². (d) La orden de compra.",
        ["calcula las tablas que faltan", "identifica las dos tablas sobre el criterio", "calcula el área de la sección", "nombra la orden de compra"],
        ["hoja con las cuatro respuestas"],
        ["confundir orden de compra con guía de despacho", "aceptar por apariencia", "dividir en vez de multiplicar la sección"],
        "Pregunta: «¿qué valor comparaste con qué criterio?». Si no responde, pídele que relea el vocabulario de contenido de humedad."),
    reinforce="Escribe una lista de tres documentos de la recepción de madera y quién emite cada uno.",
    extend="Explica por qué el registro de recepción no debe alterarse para que coincida con la orden de compra.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de recepción de ejemplo, inventado). Lote 3 del taller ficticio «Carpintería Los Boldos». Según la guía: 40 piezas remanufacturadas y 30 tableros. "
     "Inspección visual por la bodeguera: 5 piezas remanufacturadas con rajaduras y 3 tableros con bordes dañados. Humedad medida en 4 piezas remanufacturadas: 16 %, 21 %, 24 % y 20 %. Criterio de aceptación inventado: humedad máxima de 23 %. "
     "Decisión de ejemplo: las piezas sin defectos y dentro del criterio se aceptan; las demás se separan en una zona marcada y se registran como no conformidad con el nombre de quien las detectó.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de recepción: contar lo aceptado y lo separado, aplicar el criterio de humedad y registrar una no conformidad.",
    prior=["Sé qué documentos acompañan la recepción.", "Sé restar y calcular porcentajes sencillos.", "Sé qué es el criterio de aceptación."],
    explain=[
        "Un caso de recepción se analiza en orden: primero se lee la guía de despacho, luego se anotan los defectos que se ven a simple vista, después se comparan las mediciones con el criterio de aceptación y, por último, se decide qué se acepta y qué se separa. Un defecto de aspecto, como una rajadura o un borde dañado, se registra aunque la humedad esté dentro del criterio.",
        "Una no conformidad es un incumplimiento de lo pedido o del criterio: se describe, se cuenta y se firma por quien la detecta. Lo separado se identifica en una zona marcada para que no se mezcle con lo aceptado; no se descarta en secreto ni se arregla por cuenta propia. Cuando hay muchas piezas, se puede medir una muestra, que es un grupo pequeño elegido del lote, y recordar que el resultado de la muestra no asegura el estado de todas las piezas.",
        TAIL,
    ],
    vocab=[("no conformidad", "incumplimiento de lo pedido o del criterio de aceptación, registrado por escrito"), ("inspección visual", "revisión a simple vista de defectos de aspecto"), ("muestra", "grupo pequeño de piezas del lote que se mide"), ("rajadura", "grieta que se abre en la pieza de madera"), ("zona de separación", "lugar marcado donde se guarda lo no aceptado"), ("lote", "conjunto de piezas recibidas juntas")],
    worked=[
        ("Contar lo aceptable", "Un lote de ejemplo trae 50 piezas y 7 tienen defectos de aspecto. ¿Cuántas quedan sin defectos?", ["Se restan las piezas con defectos del total.", "50 menos 7 son 43."], "43 piezas"),
        ("Aplicar un criterio", "Con un criterio inventado de humedad máxima de 15 %, se miden 13 %, 17 % y 14 %. ¿Cuántas superan el máximo?", ["Solo 17 % es mayor que 15 %.", "Las otras dos están bajo el máximo."], "1 medición"),
    ],
    mistakes=[("Descartar las piezas dañadas sin registrarlas.", "Sin registro no hay constancia ni se puede reclamar al proveedor.", "Se separan en la zona marcada y se anota la no conformidad."),
              ("Creer que si la muestra está bien, todo el lote lo está.", "La muestra es solo un grupo pequeño del lote.", "Se registra que el resultado corresponde a la muestra medida.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una no conformidad en la recepción?", "Un incumplimiento de lo pedido o del criterio, registrado por escrito", "Un acuerdo de precio con el proveedor", "Un tipo de tablero resistente", "La no conformidad es un incumplimiento documentado; no es un acuerdo ni un material."),
        ("abc", "En Muebles y Terminaciones en Madera: ¿Qué es una muestra?", "Un grupo pequeño de piezas del lote que se mide", "Todas las piezas del lote sumadas", "Una pieza que se regala al cliente", "La muestra es solo una parte del lote."),
        ("=", "{F} ¿Cuántas piezas remanufacturadas quedan sin rajaduras?", "40-5", "Se restan las piezas con rajaduras del total despachado.", " piezas"),
        ("=", "{F} ¿Cuántos tableros quedan sin bordes dañados?", "30-3", "Se restan los tableros con bordes dañados de los 30 de la guía.", " tableros"),
        ("abc", "{F} De las cuatro humedades medidas, ¿cuál supera el criterio de aceptación?", "24 %", "21 %", "16 %", "Solo 24 % es mayor que el máximo de 23 %."),
        ("abc", "{F} ¿Dónde se guardan las piezas que no se aceptan?", "En una zona marcada, separadas de lo aceptado", "Mezcladas con las aceptadas para no perder espacio", "Fuera del taller sin registrar", "Se identifican en una zona marcada para que no se confundan."),
        ("=", "{F} ¿Cuántas piezas y tableros se separan en total por defectos de aspecto?", "5+3", "Se suman las piezas con rajaduras y los tableros con bordes dañados.", " unidades"),
        ("abc", "{F} Una pieza remanufacturada sin rajaduras mide 24 % de humedad. ¿Qué corresponde?", "Separarla, porque supera el criterio aunque se vea bien", "Aceptarla, porque no tiene rajaduras", "Aceptarla, porque 24 está cerca de 23", "Pasa el aspecto pero no la humedad; basta incumplir un criterio para separarla."),
        ("abc", "{F} ¿Qué datos lleva el registro de la no conformidad?", "Cuántas piezas, qué defecto, dónde están y quién las detectó", "Solo el nombre del proveedor", "Solo el precio del lote", "Un registro útil dice cuántas, qué defecto, dónde y quién."),
        ("ab", "{F} Un compañero dice: «las 4 piezas medidas están bien, así que las 40 piezas están bien». ¿Qué respuesta es correcta?", "No: una de las cuatro superó el criterio y la muestra no asegura todo el lote", "Sí: cuatro piezas representan siempre todo el lote", "Una de las cuatro piezas medidas da 24 %, sobre el máximo, y la muestra no asegura el lote."),
        ("abc", "{F} Un estudiante propone arreglar por su cuenta las rajaduras para aceptar la pieza. ¿Qué respuesta es correcta?", "No: se registra la no conformidad y decide el responsable de calidad", "Sí: arreglar es parte de recibir", "Sí, si nadie del taller se entera", "Recibir no es reparar: se registra y decide quien corresponde."),
        ("=", "{F} Las piezas aceptadas son las sin rajaduras y dentro del criterio de humedad. Si de las 35 sin rajaduras se separa una más por humedad, ¿cuántas se aceptan?", "35-1", "Se resta la pieza que superó el criterio de las que no tenían rajaduras.", " piezas"),
        ("abc", "{F} ¿Qué rol firma la no conformidad según la ficha?", "Quien detecta el defecto", "El conductor del camión", "El cliente final del mueble", "La ficha indica que se registra con el nombre de quien detectó."),
    ],
    ctx=("abc", "En la bodega de ejemplo aparece un paquete de tableros mojado y con moho visible. Un compañero lo abre y sacude el polvo sin protección. ¿Qué corresponde?", "Avisar al responsable, no manipularlo sin protección y registrar la no conformidad", "Seguir abriendo los demás paquetes sin avisar", "Guardarlo junto a los aceptados para secarlo", "El moho y el polvo son un riesgo para la respiración; se avisa y se separa."),
    sc=[
        ("¿Qué se hace con las piezas con defectos de aspecto?", "Se separan y se registran como no conformidad", "Registrar y separar deja constancia y evita mezclas."),
        ("En Muebles y Terminaciones en Madera: ¿por qué una muestra no asegura todo el lote?", "Porque es solo un grupo pequeño del lote", "Las piezas no medidas pueden estar distintas."),
        ("¿Qué pasa si una pieza se ve bien pero supera el criterio de humedad?", "Se separa", "El criterio se aplica con el valor medido."),
    ],
    op=("Caso de ejemplo «Lote 8» (ficticio): según la guía llegan 60 tableros y 50 piezas remanufacturadas. Defectos de aspecto: 4 tableros con bordes dañados y 6 piezas con rajaduras. Humedades de cuatro piezas: 15 %, 22 %, 25 % y 19 %; criterio inventado: máximo 21 %. Escribe (a) cuántos tableros quedan sin daño, (b) cuántas piezas quedan sin rajaduras, (c) cuántas de las cuatro medidas superan el criterio y (d) qué datos lleva el registro de no conformidad.",
        "(a) 60 menos 4 son 56 tableros. (b) 50 menos 6 son 44 piezas. (c) Dos: 22 % y 25 %. (d) Cuántas piezas, qué defecto, dónde están y quién las detectó.",
        ["calcula tableros sin daño", "calcula piezas sin rajaduras", "identifica las dos humedades sobre el criterio", "enumera los datos del registro"],
        ["hoja con las cuatro respuestas"],
        ["aceptar piezas por apariencia", "olvidar que el criterio es 21 % y no 22 %", "proponer arreglar la pieza"],
        "Pregunta: «¿qué diferencia hay entre un defecto de aspecto y uno de humedad?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe en tres líneas cómo registrarías una no conformidad de ejemplo con cinco piezas dañadas.",
    extend="Explica por qué se anota la no conformidad aunque el proveedor reponga después las piezas dañadas.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Un taller ficticio compra piezas de madera de sección de 10 cm por 5 cm y largo de 300 cm. Un lote tiene 200 piezas. "
     "Conversión dada en esta ficha: 1 dm³ equivale a 1.000 cm³ y 1 m³ equivale a 1.000 dm³. "
     "Ofertas de ejemplo (precios inventados): oferta A, 4 m³ por $720.000; oferta B, 3 m³ por $600.000.")
build(
    O1, 4, F,
    use="Aprenderé a calcular el volumen de piezas de madera con una conversión dada y a comparar el precio por m³ de dos ofertas.",
    prior=["Sé multiplicar números enteros.", "Sé qué es la escuadría.", "Sé leer una tabla de precios."],
    explain=[
        "El volumen de una pieza se obtiene multiplicando su ancho, su espesor y su largo, con las tres medidas en la misma unidad. El resultado se expresa en unidades cúbicas, como cm³ o dm³. Cuando el enunciado entrega una conversión, como 1 dm³ = 1.000 cm³, se divide el número de cm³ por 1.000 para pasar a dm³, y por 1.000 de nuevo para pasar de dm³ a m³.",
        "El precio por m³ permite comparar ofertas de distinto tamaño: se divide el precio total por los m³ que incluye. La oferta más barata por m³ no siempre es la mejor, porque también importan la calidad, la humedad, la entrega y los documentos, pero es un criterio objetivo para empezar. Toda cifra de esta clase es de ejemplo; los valores reales de los productos los fijan el proveedor y la norma vigente.",
        TAIL,
    ],
    vocab=[("volumen", "espacio que ocupa una pieza: ancho por espesor por largo"), ("cm³", "centímetro cúbico, unidad de volumen para piezas pequeñas"), ("dm³", "decímetro cúbico: 1 dm³ equivale a 1.000 cm³"), ("m³", "metro cúbico: 1 m³ equivale a 1.000 dm³"), ("precio por m³", "precio total dividido por los m³ que incluye la oferta"), ("oferta", "propuesta de precio y cantidad de un proveedor")],
    worked=[
        ("Volumen de una pieza", "Una pieza de ejemplo mide 4 cm de espesor, 10 cm de ancho y 100 cm de largo. ¿Cuántos cm³ tiene?", ["Se multiplican las tres medidas.", "4 por 10 por 100 son 4.000."], "4.000 cm³"),
        ("Precio por unidad de volumen", "Una oferta de ejemplo trae 5 m³ por $850.000. ¿Cuánto cuesta cada m³?", ["Se divide el precio por los m³.", "850.000 dividido en 5 es 170.000."], "$170.000 por m³"),
    ],
    mistakes=[("Multiplicar medidas en unidades distintas (cm por m).", "Las tres medidas deben estar en la misma unidad.", "Se convierte todo a cm o todo a m antes de multiplicar."),
              ("Comparar solo el precio total de dos ofertas.", "Una oferta puede traer más madera que la otra.", "Se compara el precio por m³.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué se obtiene al multiplicar ancho, espesor y largo de una pieza?", "Su volumen", "Su escuadría", "Su humedad", "Ancho por espesor por largo da el volumen; la escuadría solo usa ancho y espesor."),
        ("abc", "¿Qué permite comparar el precio por m³?", "Ofertas de distinto tamaño en una misma unidad", "La humedad de dos lotes", "El peso de dos camiones", "El precio por m³ pone las ofertas en la misma base."),
        ("=", "{F} ¿Cuántos cm³ tiene una pieza del lote?", "10*5*300", "Se multiplican ancho, espesor y largo, todos en centímetros.", " cm³"),
        ("=", "{F} ¿Cuántos dm³ tiene una pieza (1 dm³ equivale a 1.000 cm³)?", "15000//1000", "Se divide el volumen en cm³ por 1.000 para pasarlo a dm³.", " dm³"),
        ("=", "{F} ¿Cuántos dm³ tiene el lote completo de 200 piezas?", "200*15", "Se multiplica el volumen de una pieza (15 dm³) por las 200 piezas.", " dm³"),
        ("=", "{F} ¿Cuántos m³ tiene el lote completo (3.000 dm³ en total y 1 m³ equivale a 1.000 dm³)?", "3000//1000", "Se divide el volumen en dm³ por 1.000 para pasarlo a m³.", " m³"),
        ("=", "{F} ¿Cuánto cuesta cada m³ en la oferta A?", "720000//4", "Se divide el precio total de la oferta por los m³ que incluye.", " pesos por m³"),
        ("=", "{F} ¿Cuánto cuesta cada m³ en la oferta B?", "600000//3", "Se divide el precio total de la oferta por sus 3 m³.", " pesos por m³"),
        ("abc", "{F} ¿Qué oferta es más barata por m³?", "La oferta A", "La oferta B", "Ambas cuestan lo mismo por m³", "La oferta A cobra menos por cada m³ que la B."),
        ("abc", "{F} Una persona dice: «la oferta B es más barata porque su precio total es menor». ¿Qué respuesta es correcta?", "No: la B trae menos madera; se compara el precio por m³", "Sí: el menor precio total siempre es mejor", "Sí, porque 3 es menor que 4", "Precio total y cantidad son distintos; se compara por m³."),
        ("abc", "{F} Otra persona dice: «ya sé comparar ofertas, puedo comprar sin revisar la humedad». ¿Qué respuesta es correcta?", "No: además del precio importan la humedad, la entrega y los documentos", "Sí: el precio por m³ decide todo", "Sí, si la oferta es la más barata", "El precio es un criterio, pero la calidad también se verifica."),
        ("=", "{F} Si el taller compra 2 lotes como el de la ficha, ¿cuántos m³ compra?", "2*3", "Se multiplica el volumen de un lote (3 m³) por los 2 lotes.", " m³"),
        ("abc", "{F} Una pieza se midió en metros y otra en centímetros. ¿Qué corresponde antes de multiplicar?", "Convertirlas a la misma unidad", "Multiplicarlas tal cual", "Sumar las medidas en vez de multiplicar", "Multiplicar unidades distintas da un volumen sin sentido."),
    ],
    ctx=("abc", "El responsable pide estimar cuántas piezas de la ficha caben en un camión que carga 6 m³ (dato de ejemplo). Sabiendo que 1 pieza tiene 15 dm³, ¿qué cálculo corresponde?", "Pasar 6 m³ a dm³ y dividir por 15", "Multiplicar 6 por 15 y por 300", "Sumar 6 y 15", "Primero se pasa a la misma unidad (6.000 dm³) y luego se divide entre el volumen de una pieza."),
    sc=[
        ("¿Cómo se calcula el volumen de una pieza?", "Multiplicando ancho, espesor y largo en la misma unidad", "El volumen es el producto de las tres medidas."),
        ("En Muebles y Terminaciones en Madera: ¿para qué sirve el precio por m³?", "Para comparar ofertas de distinto tamaño", "Pone las ofertas en una misma base."),
        ("¿Cuántos dm³ equivalen a 1 m³ según la clase?", "1.000 dm³", "La conversión dada es 1 m³ = 1.000 dm³."),
    ],
    op=("Cálculo de ejemplo «Taller Peumo» (ficticio): piezas de 8 cm de ancho, 4 cm de espesor y 250 cm de largo; un lote de 500 piezas. 1 dm³ equivale a 1.000 cm³ y 1 m³ equivale a 1.000 dm³. Oferta C: 2 m³ por $380.000; oferta D: 5 m³ por $900.000. Escribe (a) el volumen de una pieza en cm³, (b) el volumen del lote en m³, (c) el precio por m³ de cada oferta y (d) cuál oferta es más barata por m³.",
        "(a) 8×4×250 son 8.000 cm³. (b) 8.000 cm³ son 8 dm³; 500×8 son 4.000 dm³, es decir 4 m³. (c) C: 380.000÷2 son 190.000; D: 900.000÷5 son 180.000. (d) La oferta D.",
        ["calcula el volumen de una pieza", "convierte el lote a m³", "calcula ambos precios por m³", "elige la oferta más barata por m³"],
        ["hoja con los cálculos y la elección"],
        ["no convertir las unidades", "comparar solo precios totales", "dividir en vez de multiplicar el lote"],
        "Pregunta: «¿por qué comparas el precio por m³ y no el total?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula el volumen en cm³ de una pieza de ejemplo de 6 cm por 3 cm por 200 cm y pásalo a dm³.",
    extend="Explica qué otros datos, además del precio por m³, miraría un responsable antes de elegir una oferta.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (encargo de ejemplo, inventado). Una clienta ficticia pide un escritorio de 120 cm de ancho, 60 cm de fondo y 75 cm de alto, con 2 cajones y una repisa lateral. "
     "El taller ficticio «Carpintería Los Boldos» anota el encargo en una ficha con el nombre de la clienta (ficticio), una medida de referencia y un croquis a mano alzada. "
     "Riesgos anotados: errores de lectura que llevan a cortar piezas equivocadas, pérdida del plano vigente y datos personales de la clienta a la vista de otras personas. "
     "Medidas anotadas: confirmar por escrito las medidas con la clienta, guardar solo la versión vigente del plano, resguardar los datos personales y hacer pausas al dibujar por tiempos largos.")
build(
    O2, 1, F,
    use="Aprenderé por qué se lee el diseño de un mueble antes de fabricarlo y qué riesgos tiene leerlo mal o descuidar los datos del cliente.",
    prior=["Sé qué son las medidas en centímetros.", "Sé qué es una lista de materiales.", "Sé qué es un dato personal."],
    explain=[
        "El diseño de un mueble es el conjunto de documentos que lo describen antes de fabricarlo: croquis, planos, despiece y especificaciones. Un croquis es un dibujo a mano alzada, con medidas anotadas, para ordenar una idea; un plano es un dibujo con medidas y escala que permite fabricar. Leerlos bien orienta y especifica la demanda del cliente, es decir, lo que el cliente pidió.",
        "Un error de lectura se paga caro: se cortan piezas equivocadas, se pierde material y se pierde tiempo. Por eso se confirma por escrito lo que pidió el cliente, se trabaja con una sola versión vigente del plano y se cuidan los datos personales del cliente: nombre, teléfono y dirección no se muestran a quien no los necesita. Dibujar por periodos largos también cansa la vista y la espalda, por lo que se hacen pausas. En esta clase todo se dibuja y se lee en papel.",
        TAIL,
    ],
    vocab=[("croquis", "dibujo a mano alzada con medidas anotadas para ordenar una idea"), ("plano", "dibujo con medidas y escala que permite fabricar"), ("demanda del cliente", "lo que el cliente pidió: medidas, uso y características"), ("versión vigente", "la última versión aprobada del plano"), ("dato personal", "información que identifica a una persona, como nombre o teléfono"), ("pausa", "descanso breve para cuidar la vista y la espalda")],
    worked=[
        ("Reconocer el documento", "Una persona de ejemplo dibuja a mano alzada una repisa con medidas anotadas para explicar su idea. ¿Qué documento es?", ["Un dibujo a mano alzada con medidas anotadas es un croquis.", "Todavía no tiene escala de fabricación."], "Un croquis"),
        ("Contar piezas", "Una repisa de ejemplo lleva 1 tapa, 2 costados y 3 estantes. ¿Cuántas piezas son?", ["Se suman las piezas de cada tipo.", "1 más 2 más 3 son 6."], "6 piezas"),
    ],
    mistakes=[("Guardar tres versiones del plano sin marcar cuál es la vigente.", "Se puede fabricar con una versión antigua.", "Se identifica la versión vigente y se retiran las anteriores del taller."),
              ("Dejar a la vista el teléfono del cliente en el plano que ve todo el taller.", "El dato personal no lo necesita quien corta o arma.", "Los datos personales quedan en la ficha comercial, no en el plano.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es un croquis?", "Un dibujo a mano alzada con medidas anotadas", "Un plano con escala de fabricación firmado", "Una lista de precios de los tableros", "El croquis ordena una idea; el plano con escala sirve para fabricar."),
        ("abc", "¿Qué significa «demanda del cliente» en el diseño de un mueble?", "Lo que el cliente pidió: medidas, uso y características", "La cantidad de muebles que vende el taller al mes", "El precio de la madera en el mercado", "La demanda del cliente es su pedido específico."),
        ("=", "{F} ¿Cuántos centímetros de ancho tiene el escritorio pedido más la repisa de 30 cm de ancho puesta a su lado?", "120+30", "Se suman el ancho del escritorio y el ancho de la repisa lateral.", " cm"),
        ("abc", "{F} ¿Qué dato de la ficha es un dato personal?", "El nombre de la clienta", "El alto de 75 cm", "El número de cajones", "El nombre identifica a una persona; las medidas no."),
        ("abc", "{F} ¿Qué riesgo de la ficha se evita guardando solo la versión vigente del plano?", "Cortar piezas con una versión antigua", "Sufrir una caída desde altura", "Aspirar polvo de madera", "Una versión antigua puede tener medidas distintas."),
        ("abc", "{F} ¿Dónde deben quedar el teléfono y la dirección de la clienta?", "En la ficha comercial, no en el plano que ve todo el taller", "En el plano, junto a las cotas", "En una nota pegada en la bodega", "El dato personal solo se muestra a quien lo necesita."),
        ("=", "{F} Si el escritorio lleva 2 cajones y cada cajón se arma con 5 piezas (dato de ejemplo), ¿cuántas piezas son de cajones?", "2*5", "Se multiplican los cajones por las piezas de cada uno.", " piezas"),
        ("abc", "{F} Antes de fabricar, ¿qué hace el taller para evitar un malentendido con la clienta?", "Confirmar por escrito las medidas pedidas", "Fabricar rápido para mostrar el resultado", "Cambiar las medidas sin avisar", "Confirmar por escrito deja claro lo que se acordó."),
        ("abc", "{F} Una persona lleva tres horas seguidas dibujando el plano y siente la vista cansada. ¿Qué corresponde?", "Hacer una pausa y descansar la vista y la espalda", "Seguir hasta terminar sin descanso", "Acercar más la cara al papel", "Las pausas cuidan la salud de quien dibuja."),
        ("ab", "{F} Una persona dice: «el plano de ayer sirve igual, aunque haya otro más nuevo». ¿Qué respuesta es correcta?", "No: se usa solo la versión vigente", "Sí: da lo mismo cuál versión se use", "La ficha indica guardar la versión vigente porque las antiguas pueden traer medidas distintas."),
        ("abc", "{F} Una estudiante dice: «leo bien un plano, ya puedo operar las máquinas del taller». ¿Qué respuesta es correcta?", "No: operar máquinas exige instructor autorizado y norma vigente", "Sí: leer planos habilita para operar", "Sí, si usa lentes de seguridad", "Leer un plano no habilita para operar máquinas ni los EPP lo reemplazan."),
        ("=", "{F} El tablero superior tendría 120 cm por 60 cm. ¿Cuántos cm² tiene su cara superior?", "120*60", "El área de un rectángulo es el largo por el ancho.", " cm²"),
        ("abc", "{F} Una clienta pide cambiar el alto de 75 cm a otra medida. ¿Qué corresponde?", "Anotar el cambio por escrito, actualizar el plano y marcar la nueva versión vigente", "Recordar el cambio de memoria", "Cambiar el número en el plano viejo sin avisar", "Todo cambio se registra y se actualiza la versión vigente."),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona se corta una mano con una máquina mientras otra consulta el plano. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Quitar a la persona de la máquina sin que nadie más lo sepa", "Seguir con el trabajo para no perder tiempo", "No se interviene sin autorización en la zona de riesgo; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("¿Para qué sirve leer el diseño de un mueble antes de fabricarlo?", "Para fabricar lo que el cliente pidió y evitar errores", "Una buena lectura evita cortar piezas equivocadas."),
        ("En Muebles y Terminaciones en Madera: ¿qué es la versión vigente de un plano?", "La última versión aprobada", "Es la única que se usa para fabricar."),
        ("¿Cómo se cuidan los datos personales de un cliente?", "No se muestran a quien no los necesita", "Los datos personales se resguardan en la ficha comercial."),
    ],
    op=("Encargo de ejemplo (ficticio): un cliente pide una estantería de 90 cm de ancho, 30 cm de fondo y 180 cm de alto, con 4 estantes. El croquis lleva el nombre y el teléfono del cliente. Escribe (a) una medida que hay que confirmar por escrito con el cliente, (b) por qué el teléfono no debería estar en el plano del taller, (c) cuántos cm² tiene un estante de 90 cm por 30 cm y (d) qué haces si el cliente cambia el alto después de entregado el plano.",
        "(a) Por ejemplo, el alto de 180 cm. (b) Porque quien corta o arma no necesita ese dato personal. (c) 90×30 son 2.700 cm². (d) Anoto el cambio por escrito, actualizo el plano y marco la versión vigente.",
        ["propone una medida a confirmar", "justifica el cuidado del dato personal", "calcula el área del estante", "describe cómo actualizar la versión"],
        ["hoja con las cuatro respuestas"],
        ["dejar datos personales en el plano", "no marcar la versión vigente", "multiplicar mal el área"],
        "Pregunta: «¿quién necesita ver el teléfono del cliente?». Si no responde, pídele que relea el vocabulario de dato personal."),
    reinforce="Escribe la diferencia entre un croquis y un plano con un ejemplo de mueble.",
    extend="Explica por qué es un riesgo tener dos versiones del plano en el taller sin marcar cuál es la vigente.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (plano y despiece de ejemplo, inventados). Rótulo: «Estantería ejemplo E-1», escala 1:5, versión 2 vigente, plano firmado por la diseñadora ficticia. "
     "Cotas dibujadas en el plano (en centímetros, medidas del papel): ancho 18, alto 36, fondo 5. "
     "Despiece de ejemplo: pieza P1, 2 costados, 180 cm por 25 cm por 2 cm, tablero; pieza P2, 4 estantes, 86 cm por 25 cm por 2 cm, tablero; pieza P3, 1 respaldo, 176 cm por 86 cm por 1 cm, tablero delgado. "
     "Cuadro de herrajes: 8 soportes metálicos de estante.")
build(
    O2, 2, F,
    use="Aprenderé a leer las partes de un plano: rótulo, vistas, cotas, escala, despiece y cuadro de herrajes, y quién usa cada documento.",
    prior=["Sé qué es un croquis y un plano.", "Sé multiplicar.", "Sé qué es una lista de piezas."],
    explain=[
        "El rótulo es el recuadro del plano que dice el nombre del mueble, la escala, la versión y quién lo firma. Las vistas muestran el mueble desde distintos lados: la planta, desde arriba; la elevación, de frente; y el corte, que muestra el interior. Las cotas son las medidas escritas sobre el dibujo. La escala dice cuántas veces el dibujo es más pequeño que el objeto real: en una escala 1:20, cada 1 cm del papel representa 20 cm reales.",
        "El despiece es la lista de todas las piezas del mueble, con su nombre, cantidad, medidas y material. El cuadro de herrajes lista las piezas metálicas o auxiliares que no se cortan de madera. Los roles son la diseñadora, que dibuja y firma; el jefe de taller, que lee y programa; y el operario, que recibe instrucciones del jefe. Leer es comparar siempre el plano, el despiece y el cuadro: si no coinciden, no se improvisa, se consulta.",
        TAIL,
    ],
    vocab=[("rótulo", "recuadro del plano con nombre, escala, versión y firma"), ("vista", "dibujo del mueble desde un lado: planta, elevación o corte"), ("cota", "medida escrita sobre el dibujo"), ("escala", "relación entre el dibujo y el objeto real, por ejemplo 1:20"), ("despiece", "lista de piezas con nombre, cantidad, medidas y material"), ("cuadro de herrajes", "lista de piezas metálicas o auxiliares del mueble")],
    worked=[
        ("Leer una escala", "En un plano de ejemplo a escala 1:10, una cota mide 7 cm en el papel. ¿Cuántos centímetros reales representa?", ["La escala 1:10 multiplica por 10.", "7 por 10 son 70."], "70 cm reales"),
        ("Contar con el despiece", "Un despiece de ejemplo dice: 3 tapas, 6 patas. ¿Cuántas piezas hay en total?", ["Se suman las cantidades de cada pieza.", "3 más 6 son 9."], "9 piezas"),
    ],
    mistakes=[("Leer una cota del dibujo como si fuera la medida real.", "Las cotas del papel dependen de la escala.", "Se multiplica por la escala o se lee la medida real escrita."),
              ("Cortar sin comparar plano, despiece y cuadro de herrajes.", "Un error en un documento se descubre al compararlos.", "Si no coinciden, se consulta al jefe de taller o a la diseñadora.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es el despiece de un mueble?", "La lista de piezas con nombre, cantidad, medidas y material", "El dibujo del mueble visto desde arriba", "El precio final del mueble", "El despiece es la lista de piezas; la planta es una vista."),
        ("abc", "¿Qué indica la escala 1:5 de un plano?", "Que cada 1 cm del dibujo representa 5 cm reales", "Que el mueble real mide 5 cm", "Que el plano tiene 5 hojas", "La escala relaciona dibujo y objeto real."),
        ("=", "{F} ¿Cuántos centímetros reales representa la cota de ancho de 18 cm dibujada en el papel?", "18*5", "Con escala 1:5 se multiplica la medida del papel por 5.", " cm"),
        ("=", "{F} ¿Cuántos centímetros reales representa la cota de alto de 36 cm dibujada en el papel?", "36*5", "Con escala 1:5 se multiplica la medida del papel por 5.", " cm"),
        ("abc", "{F} ¿Quién firma el plano según la ficha?", "La diseñadora ficticia", "El operario de la bodega", "El conductor del camión", "El rótulo indica que firma quien diseñó."),
        ("abc", "{F} ¿Qué vista muestra el interior del mueble?", "El corte", "La planta", "La elevación", "El corte muestra el interior; la planta y la elevación muestran el exterior."),
        ("=", "{F} ¿Cuántas piezas de tablero (sin contar herrajes) lleva el despiece?", "2+4+1", "Se suman las cantidades de costados, estantes y respaldo.", " piezas"),
        ("abc", "{F} ¿Dónde se anotan los soportes metálicos de estante?", "En el cuadro de herrajes", "En el despiece de tableros", "En el rótulo", "Los soportes no se cortan de madera; van en el cuadro de herrajes."),
        ("abc", "En otro plano de ejemplo, el despiece dice 4 estantes de 2 soportes cada uno, pero el cuadro de herrajes pide 6 soportes. ¿Qué corresponde?", "Detectar que no coinciden y consultar a la diseñadora", "Elegir el número más conveniente", "Cortar 6 estantes para igualar", "Si los documentos no coinciden no se improvisa: se consulta."),
        ("ab", "{F} Un estudiante dice: «la cota de 36 cm del plano es el alto real». ¿Qué respuesta es correcta?", "No: con escala 1:5 el alto real es 5 veces mayor", "Sí: las cotas siempre son reales", "La ficha indica escala 1:5, de modo que el alto real es cinco veces la cota del papel."),
        ("abc", "{F} Otra persona dice: «ya sé leer el despiece, puedo cortar las piezas yo solo». ¿Qué respuesta es correcta?", "No: cortar exige instructor autorizado, norma vigente y EPP; leer no habilita", "Sí: leer el despiece basta", "Sí, si tiene lentes de seguridad", "Leer un despiece no habilita para operar máquinas."),
        ("=", "{F} Cada estante pide 2 soportes metálicos. ¿Cuántos soportes necesitan los 4 estantes?", "4*2", "Se multiplican los estantes por los soportes de cada uno.", " soportes"),
        ("abc", "{F} ¿Qué versión del plano se usa para fabricar?", "La versión 2, que es la vigente", "Cualquier versión que haya en el taller", "La versión más antigua por ser la original", "Solo se fabrica con la versión vigente que indica el rótulo."),
    ],
    ctx=("abc", "En el taller de ejemplo, un joven ve un aviso de «corte» en el plano y pregunta si se puede probar la máquina de corte sin autorización. ¿Qué respuesta es correcta?", "No: las máquinas las operan solo personas autorizadas y capacitadas", "Sí, si usa lentes y guantes", "Sí, si el plano es de la versión vigente", "La autorización y la capacitación no se reemplazan con EPP ni con planos."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿Qué es una cota?", "Una medida escrita sobre el dibujo", "Las cotas son las medidas del plano."),
        ("En Muebles y Terminaciones en Madera: ¿para qué sirve el cuadro de herrajes?", "Para listar las piezas metálicas o auxiliares del mueble", "Aparte del despiece, indica herrajes que no se cortan de madera."),
        ("¿Qué se hace si el plano y el despiece no coinciden?", "Se consulta, no se improvisa", "Un error en un documento se resuelve con quien diseñó."),
    ],
    op=("Plano de ejemplo «Mesa M-3» (ficticia): escala 1:10; cotas del papel: largo 12 cm y ancho 7 cm. Despiece: 1 tapa, 4 patas, 2 travesaños. Cuadro de herrajes: 12 tornillos de unión. Escribe (a) las medidas reales de largo y ancho de la mesa, (b) cuántas piezas de madera tiene el despiece, (c) dónde aparecen los tornillos y (d) qué haces si el despiece dice 4 patas y el dibujo muestra 6.",
        "(a) 12×10 son 120 cm de largo y 7×10 son 70 cm de ancho. (b) 1+4+2 son 7 piezas. (c) En el cuadro de herrajes. (d) No improviso: consulto al jefe de taller o a la diseñadora.",
        ["calcula las medidas reales con la escala", "suma las piezas del despiece", "indica el cuadro de herrajes", "consulta ante la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["leer la cota del papel como medida real", "contar los tornillos como piezas de madera", "elegir una cantidad sin consultar"],
        "Pregunta: «¿qué hace la escala con las cotas?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe la diferencia entre planta, elevación y corte con una frase para cada vista.",
    extend="Explica qué documentos compararías antes de pasar un mueble a producción.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (caso de lectura de ejemplo, inventado). Plano de la biblioteca «B-4» del taller ficticio «Carpintería Los Boldos», escala 1:10, versión 3 vigente. "
     "Cotas del plano (dibujadas en el papel, en cm): alto total 18; tres tramos verticales marcados dentro del alto total: 6, 6 y 5. Ancho 8; fondo 3. "
     "Despiece de ejemplo: 2 costados, 1 tapa, 1 base, 3 estantes y 1 respaldo; el cuadro de herrajes pide 12 soportes de estante. "
     "Nota del jefe de taller: «los estantes no pueden quedar más anchos que el espacio entre costados».")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de lectura de plano: comprobar que las cotas suman, convertir con la escala y detectar incoherencias.",
    prior=["Sé qué es la escala y el despiece.", "Sé sumar y multiplicar.", "Sé qué es la versión vigente."],
    explain=[
        "Analizar un plano es comprobar que sus datos son coherentes. Una primera revisión es sumar las cotas parciales: los tramos marcados dentro de un alto total deben sumar ese alto. Si no suman, hay un error que se informa a quien diseñó, porque no se decide cuál cota es la correcta. La segunda revisión es convertir las medidas del papel a medidas reales usando la escala.",
        "Una tercera revisión compara el despiece con las vistas: si el despiece dice 3 estantes y el dibujo muestra 4, el documento se devuelve para aclarar. También se comprueba que cada pieza quepa en el espacio disponible: un estante no puede ser más ancho que el espacio entre los costados. Estas comprobaciones se hacen en papel antes de comprar o cortar material, y se dejan anotadas con fecha y nombre en el registro de revisión.",
        TAIL,
    ],
    vocab=[("coherencia", "que los datos del plano no se contradigan entre sí"), ("cota parcial", "cota de un tramo que forma parte de una medida total"), ("cota total", "medida que abarca todos los tramos"), ("registro de revisión", "anotación con fecha y nombre de quien revisó el plano"), ("devolver el documento", "pedir a quien diseñó que aclare o corrija")],
    worked=[
        ("Sumar cotas parciales", "En un plano de ejemplo, un alto total de 10 cm tiene tramos de 4, 3 y 2 cm. ¿Suman el total?", ["Se suman 4, 3 y 2.", "La suma es 9, que no es 10."], "No suman; se informa a quien diseñó"),
        ("Convertir con escala", "Con escala 1:20, una cota de 6 cm en el papel, ¿cuánto mide en la realidad?", ["Se multiplica por 20.", "6 por 20 son 120."], "120 cm"),
    ],
    mistakes=[("Corregir por cuenta propia la cota que no suma.", "No se sabe cuál de las cotas es el error.", "Se anota la incoherencia y se devuelve el plano a quien diseñó."),
              ("Revisar solo una vista y dar por bueno el plano.", "El error puede estar en otra vista o en el despiece.", "Se comparan vistas, despiece y cuadro de herrajes.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué significa que un plano sea coherente?", "Que sus datos no se contradicen entre sí", "Que tiene muchos dibujos", "Que está dibujado a color", "La coherencia es que cotas, vistas y despiece concuerden."),
        ("abc", "¿Qué se hace si las cotas parciales no suman la cota total?", "Se anota la incoherencia y se devuelve el plano a quien diseñó", "Se elige la cota que parezca mejor", "Se corta con la medida más grande", "No se decide por cuenta propia cuál cota es el error."),
        ("=", "{F} ¿Cuánto suman los tres tramos verticales marcados?", "6+6+5", "Se suman las tres cotas parciales del plano.", " cm"),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre el alto total del plano y la suma de los tramos?", "18-17", "Se resta la suma de los tramos al alto total dibujado.", " cm"),
        ("abc", "{F} ¿Qué se concluye al comparar el alto total con la suma de los tramos?", "Hay una incoherencia que se informa a quien diseñó", "El plano está perfecto", "Basta con sumar 1 al último tramo", "Las cotas no concuerdan, por lo que no se puede fabricar."),
        ("=", "{F} Si el alto dibujado es 18 cm y la escala es 1:10, ¿cuántos cm reales mide?", "18*10", "Con escala 1:10 se multiplica la medida del papel por 10.", " cm"),
        ("=", "{F} Según el despiece, ¿cuántas piezas de tablero tiene la biblioteca?", "2+1+1+3+1", "Se suman costados, tapa, base, estantes y respaldo del despiece.", " piezas"),
        ("=", "{F} Cada estante usa 4 soportes de estante. ¿Cuántos soportes necesitan los 3 estantes?", "3*4", "Se multiplican los estantes por los soportes de cada uno.", " soportes"),
        ("abc", "{F} Si el cuadro de herrajes dijera 10 soportes pero el cálculo (3 estantes por 4 soportes) da otra cantidad, ¿qué corresponde?", "Dejar anotada la diferencia y consultar antes de comprar", "Comprar 12 sin revisar", "Comprar la cantidad calculada sin avisar", "Una diferencia entre documentos se consulta antes de comprar."),
        ("abc", "{F} Un estante dibujado mide más que el espacio entre costados. ¿Qué se concluye?", "Hay una incoherencia entre piezas que hay que informar", "El estante queda mejor más ancho", "Se debe cortar el costado", "Una pieza que no cabe en su espacio indica un error de diseño que se informa."),
        ("ab", "{F} Una persona dice: «me quedo con el tramo de 6 y no sumo el resto». ¿Qué respuesta es correcta?", "No: se suman todos los tramos para comprobar el total", "Sí: un solo tramo basta para revisar", "La ficha muestra tres tramos verticales y todos deben sumarse para comprobar el total."),
        ("abc", "{F} Una estudiante dice: «ya detecté un error en el plano, puedo corregirlo y empezar a cortar». ¿Qué respuesta es correcta?", "No: se informa a quien diseñó y cortar exige instructor autorizado y norma vigente", "Sí: detectar el error la habilita a corregirlo", "Sí, si usa EPP completos", "Detectar un error no autoriza a corregirlo ni a operar máquinas."),
        ("abc", "{F} ¿Qué se anota en el registro de revisión?", "Fecha, nombre de quien revisó y las incoherencias encontradas", "Solo la fecha", "Solo el nombre del proveedor de tableros", "El registro deja constancia de quién revisó qué y cuándo."),
    ],
    ctx=("abc", "En el taller de ejemplo, alguien propone saltarse la revisión del plano para ganar tiempo y empezar a trabajar la madera con prisa. ¿Qué respuesta es correcta?", "No: revisar el plano evita errores y accidentes por improvisar", "Sí: la prisa es más importante", "Sí, si el plano se ve ordenado", "Improvisar por prisa aumenta los errores y los riesgos."),
    sc=[
        ("¿Qué se debe sumar para comprobar la cota total?", "Las cotas parciales", "Los tramos deben sumar el total."),
        ("En Muebles y Terminaciones en Madera: ¿qué se hace si el despiece y el dibujo no coinciden?", "Se devuelve el documento para aclarar", "No se improvisa una solución: se devuelve el documento a quien diseñó."),
        ("¿Qué se anota en el registro de revisión?", "Fecha, nombre y las incoherencias", "Deja constancia de quién revisó el plano y qué encontró."),
    ],
    op=("Plano de ejemplo «Armario A-7» (ficticio), escala 1:10: alto total dibujado 20 cm; tramos marcados: 8, 7 y 4 cm. Ancho dibujado 9 cm. Despiece: 2 costados, 1 tapa, 1 base, 2 puertas y 1 respaldo. Escribe (a) cuánto suman los tramos y si coinciden con el total, (b) cuántos cm reales mide el ancho, (c) cuántas piezas lista el despiece y (d) qué haces con la diferencia detectada.",
        "(a) 8+7+4 son 19 y el total es 20: no coinciden. (b) 9×10 son 90 cm. (c) 2+1+1+2+1 son 7 piezas. (d) La anoto y devuelvo el plano a quien diseñó.",
        ["suma las cotas parciales y compara", "convierte el ancho con la escala", "suma las piezas del despiece", "indica devolver el plano"],
        ["hoja con las cuatro respuestas"],
        ["corregir la cota por cuenta propia", "no multiplicar por la escala", "contar solo algunas piezas"],
        "Pregunta: «¿por qué no se corrige la cota solo?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe los pasos de revisión de un plano en una lista de tres puntos, sin incluir ninguna operación de taller.",
    extend="Explica por qué una diferencia de pocos centímetros puede obligar a cambiar el costo de un mueble.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (criterio técnico de ejemplo, inventado). El taller ficticio recibe dos propuestas de diseño para un mueble de entrada. Propuesta 1, escala 1:5: ancho dibujado 20 cm, alto dibujado 24 cm. "
     "Propuesta 2, escala 1:8: ancho dibujado 14 cm, alto dibujado 15 cm. "
     "El cliente (ficticio) exige que el ancho real no pase de 110 cm. Los tableros de ejemplo son de 200 cm por 100 cm. "
     "Registro de versiones del plano: v1 del lunes (reemplazada), v2 del martes (vigente), v3 sin aprobar.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico a dos propuestas de diseño: convertir con la escala, comparar con una exigencia del cliente y registrar la versión.",
    prior=["Sé qué es la escala.", "Sé qué es la versión vigente.", "Sé multiplicar y comparar números."],
    explain=[
        "Una exigencia del cliente se convierte en un criterio técnico: una condición medible que el diseño debe cumplir, por ejemplo, un ancho máximo. Para aplicarla se convierten las medidas del papel a medidas reales usando la escala de cada propuesta, porque dos planos de escalas distintas no se pueden comparar directamente. Después se comparan los resultados con el criterio y se decide qué propuesta lo cumple.",
        "También se revisa que las piezas se puedan obtener de los tableros disponibles: una pieza más larga que el tablero no se puede fabricar de una sola pieza. Finalmente se registra la decisión: qué propuesta se eligió, con qué criterio y cuál es la versión vigente del plano. Una versión sin aprobar no se usa para fabricar, y una versión reemplazada se retira del taller. En esta clase todas las cifras son de ejemplo y se calculan en papel.",
        TAIL,
    ],
    vocab=[("criterio técnico", "condición medible que el diseño debe cumplir"), ("propuesta de diseño", "alternativa de plano que se presenta al cliente"), ("ancho máximo", "límite de ancho que el cliente exige"), ("versión sin aprobar", "plano que aún no firma quien decide"), ("versión reemplazada", "plano antiguo que ya no se usa")],
    worked=[
        ("Aplicar un criterio", "Con escala 1:4, un dibujo de ejemplo mide 25 cm de ancho. El cliente exige 90 cm como máximo. ¿Lo cumple?", ["Se multiplica 25 por 4: son 100 cm.", "100 es mayor que 90."], "No lo cumple"),
        ("Elegir la versión", "Un registro de ejemplo dice: v1 reemplazada, v2 aprobada, v3 sin aprobar. ¿Cuál se usa para fabricar?", ["Se usa la versión aprobada y vigente.", "La v2 está aprobada."], "La v2"),
    ],
    mistakes=[("Comparar directamente las medidas del papel de dos planos de escalas distintas.", "Una misma medida del papel representa distinto tamaño real en cada escala.", "Se convierte cada medida con su escala y luego se compara."),
              ("Usar la versión más nueva aunque no esté aprobada.", "Una versión sin aprobar puede cambiar o descartarse.", "Se fabrica solo con la versión aprobada y vigente.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es un criterio técnico de diseño?", "Una condición medible que el diseño debe cumplir", "Una opinión personal sobre el color", "El nombre del cliente", "El criterio técnico se puede medir y comprobar."),
        ("abc", "¿Por qué se convierte con la escala antes de comparar dos propuestas?", "Porque cada plano tiene una escala distinta", "Porque así los dibujos se ven más grandes", "Porque la escala siempre es 1:1", "Dos escalas distintas no se comparan directamente en el papel."),
        ("=", "{F} ¿Cuánto mide el ancho real de la propuesta 1?", "20*5", "Se multiplica la medida del papel por la escala 5.", " cm"),
        ("=", "{F} ¿Cuánto mide el ancho real de la propuesta 2?", "14*8", "Se multiplica la medida del papel por la escala 8.", " cm"),
        ("abc", "{F} ¿Qué propuesta cumple el ancho máximo exigido por el cliente?", "La propuesta 1", "La propuesta 2", "Ambas por igual", "La propuesta 1 mide 100 cm y la 2 mide 112 cm, que pasa del máximo de 110 cm."),
        ("=", "{F} ¿Cuánto mide el alto real de la propuesta 1?", "24*5", "Se multiplica el alto del papel por la escala 5.", " cm"),
        ("=", "{F} ¿Cuánto mide el alto real de la propuesta 2?", "15*8", "Se multiplica el alto del papel por la escala 8.", " cm"),
        ("abc", "{F} ¿Qué versión del plano se usa para fabricar?", "La v2, que es la vigente", "La v3, por ser la más nueva", "La v1, por ser la original", "Se usa la versión aprobada y vigente; la v3 no está aprobada."),
        ("abc", "{F} Una pieza de la propuesta 1 mide 250 cm de largo. ¿Puede salir de un tablero de 200 cm de largo en una sola pieza?", "No, porque 250 cm es mayor que 200 cm", "Sí, porque los tableros son de 200 cm", "Sí, si se corta de lado", "Una pieza más larga que el tablero no se obtiene en una sola pieza."),
        ("ab", "{F} Una persona dice: «el dibujo 2 es más pequeño en el papel, así que el mueble real es más pequeño». ¿Qué respuesta es correcta?", "No: se compara con las medidas reales convertidas por escala", "Sí: el papel más pequeño siempre es un mueble más pequeño", "La ficha entrega dos escalas distintas, por lo que hay que convertir antes de comparar."),
        ("abc", "{F} Un estudiante dice: «ya sé comparar planos, puedo ajustar el mueble en el taller con las máquinas». ¿Qué respuesta es correcta?", "No: operar máquinas exige instructor autorizado y norma vigente", "Sí: comparar planos habilita para ajustar", "Sí, si trabaja de noche para no molestar", "Saber leer no reemplaza la autorización para operar máquinas."),
        ("=", "{F} Si la propuesta elegida pide 5 tableros de 200 cm por 100 cm, ¿cuántos cm² de tablero son en total?", "5*200*100", "Se multiplica la cantidad por el largo y el ancho de cada tablero.", " cm²"),
        ("abc", "{F} ¿Qué se registra al elegir una propuesta?", "La propuesta elegida, el criterio aplicado y la versión vigente", "Solo el color preferido", "Solo el nombre del dibujante", "La decisión debe quedar trazable en el registro."),
    ],
    ctx=("abc", "El cliente de ejemplo cambia de opinión y pide un ancho máximo menor. El jefe de taller recuerda lo que quedó por teléfono. ¿Qué respuesta es correcta?", "Se registra el cambio por escrito y se actualiza la versión del plano", "Se fabrica según lo que se recuerda", "Se descarta el cambio por ser tarde", "Los cambios se dejan por escrito para evitar errores y reclamos."),
    sc=[
        ("¿Qué se hace antes de comparar dos planos de escalas distintas?", "Se convierten las medidas con la escala de cada uno", "Cada escala cambia el tamaño real."),
        ("En Muebles y Terminaciones en Madera: ¿qué versión del plano se usa para fabricar?", "La aprobada y vigente", "Solo esa versión es válida en el taller."),
        ("¿Qué se registra al elegir una propuesta?", "La propuesta, el criterio y la versión vigente", "Eso asegura trazabilidad de la decisión."),
    ],
    op=("Propuestas de ejemplo (ficticias): Propuesta X, escala 1:6, ancho dibujado 17 cm. Propuesta Y, escala 1:4, ancho dibujado 24 cm. El cliente exige un ancho real máximo de 100 cm. Versiones: v1 reemplazada, v2 vigente, v3 sin aprobar. Escribe (a) el ancho real de cada propuesta, (b) cuál cumple el ancho máximo, (c) qué versión usas para fabricar y (d) qué anotas en el registro de decisión.",
        "(a) X: 17×6 son 102 cm; Y: 24×4 son 96 cm. (b) La propuesta Y. (c) La v2. (d) La propuesta elegida, el criterio y la versión vigente.",
        ["convierte ambos anchos con su escala", "elige la propuesta que cumple", "elige la versión vigente", "describe el registro de decisión"],
        ["hoja con las cuatro respuestas"],
        ["comparar medidas del papel sin convertir", "elegir la v3 por ser la más nueva", "no registrar la decisión"],
        "Pregunta: «¿por qué no se pueden comparar los dibujos en el papel?». Si no responde, pídele que relea la explicación."),
    reinforce="Convierte con una escala 1:12 una cota de 9 cm del papel y escribe el resultado real.",
    extend="Explica qué ventaja tiene dejar por escrito la elección entre dos propuestas de diseño.",
)

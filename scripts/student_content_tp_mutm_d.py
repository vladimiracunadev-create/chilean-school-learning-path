"""Muebles y Terminaciones en Madera (3.º y 4.º medio TP): OAE-07 (estándares de calidad, normas técnicas, prevención de riesgos, higiene, seguridad industrial y medio ambiente: planes de control, inspección de lotes, indicadores y comparación de proveedores) y OAE-08 (instalar en obra: riesgos de obra, documentos, quincallería y planificación, solo conceptos y planillas). Datos de ejemplo."""
from __future__ import annotations

from tp_mutm_common import AVISO, EMER, build

O7 = "TP-MUTM-3y4-OAE-07"
O8 = "TP-MUTM-3y4-OAE-08"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). El taller ficticio «Carpintería Los Boldos» tiene 10 personas. Agentes de riesgo anotados: polvo de madera en el aire y acumulado, ruido de las máquinas y residuos (aserrín, recortes y envases de productos químicos). "
     "Medidas anotadas: sustituir un producto muy peligroso por otro menos peligroso; aspiración de polvo y resguardos en cada máquina; turnos organizados y señalética; protección auditiva y mascarilla indicada por la hoja de datos de seguridad. "
     "Gestión ambiental anotada: aserrín retirado cada semana, envases vacíos guardados para su retiro por un gestor autorizado y madera de origen documentado.")
build(
    O7, 1, F,
    use="Aprenderé qué son la norma técnica, la higiene y la seguridad industrial, y cómo se relacionan la calidad, la prevención de riesgos y el medio ambiente en un taller de muebles.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un EPP.", "Sé qué es un registro."],
    explain=[
        "Una norma técnica es un documento acordado que fija requisitos mínimos para un producto, un proceso o un ensayo; las hay nacionales e internacionales y se indican por su nombre y vigencia, por eso siempre se habla de «la norma vigente». La higiene industrial se preocupa de los agentes del ambiente de trabajo que afectan la salud, como el polvo de madera y el ruido. La seguridad industrial previene accidentes, por ejemplo en máquinas o por incendio. La protección del medio ambiente cuida el aire, el suelo y el agua con una buena gestión de residuos.",
        "La calidad, la seguridad y el medio ambiente van juntas: un taller con polvo acumulado y residuos mal guardados produce peores muebles y más riesgos. Las medidas se ordenan en la jerarquía de controles: eliminar el peligro, sustituirlo por otro menos peligroso, controlarlo en su origen con aspiración o resguardos, organizar el trabajo con turnos y señalética y, al final, usar EPP. Quien fiscaliza el cumplimiento es la entidad fiscalizadora de tu sector, según la norma vigente.",
        TAIL,
    ],
    vocab=[("norma técnica", "documento acordado que fija requisitos mínimos para un producto o proceso"), ("higiene industrial", "control de agentes del ambiente de trabajo que afectan la salud, como polvo y ruido"), ("seguridad industrial", "prevención de accidentes en máquinas, incendios y otras fuentes"), ("control en el origen", "medida que reduce el peligro en la fuente, como la aspiración de polvo"), ("gestor autorizado", "empresa habilitada para retirar y tratar ciertos residuos"), ("origen documentado", "madera cuyo origen está respaldado por documentos")],
    worked=[
        ("Clasificar una medida", "Un taller de ejemplo instala resguardos en una máquina. ¿En qué nivel de la jerarquía de controles está?", ["Un resguardo controla el peligro en su origen.", "No es un EPP ni una organización del trabajo."], "Control en el origen"),
        ("Contar EPP", "En un taller de ejemplo hay 7 personas y cada una recibe 2 piezas de EPP. ¿Cuántas piezas son?", ["Se multiplican las personas por las piezas de cada una.", "7 por 2 son 14."], "14 piezas"),
    ],
    mistakes=[("Creer que la mascarilla elimina el polvo del taller.", "La mascarilla protege a quien la usa pero el polvo sigue en el ambiente.", "Primero se controla el polvo en su origen con aspiración y orden."),
              ("Citar una norma de memoria sin saber si sigue vigente.", "Las normas se actualizan y pueden cambiar.", "Se habla de «la norma vigente» y se consulta la versión actual.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una norma técnica?", "Un documento acordado que fija requisitos mínimos para un producto o proceso", "Una lista de precios de los tableros", "El plano de un mueble específico", "La norma técnica fija requisitos acordados; el plano y la lista de precios son otros documentos."),
        ("abc", "¿De qué se preocupa la higiene industrial?", "De los agentes del ambiente de trabajo que afectan la salud, como el polvo y el ruido", "De evitar que los muebles se rayen", "De calcular el costo de los materiales", "La higiene industrial controla agentes ambientales que dañan la salud."),
        ("abc", "{F} ¿Qué medida de la ficha es un control en el origen?", "La aspiración de polvo en cada máquina", "La protección auditiva", "Los turnos organizados", "La aspiración actúa donde nace el polvo; la protección auditiva es EPP y los turnos son organización."),
        ("abc", "{F} ¿Qué medida de la ficha es un elemento de protección personal?", "La mascarilla indicada por la hoja de datos", "La señalética", "La aspiración de polvo", "La mascarilla la usa cada persona; la señalética organiza y la aspiración es control en el origen."),
        ("abc", "{F} ¿Qué medida de la ficha corresponde a sustitución?", "Reemplazar un producto muy peligroso por otro menos peligroso", "Retirar el aserrín cada semana", "Usar protección auditiva", "Sustituir significa cambiar el producto por otro menos peligroso."),
        ("=", "{F} Cada una de las 10 personas recibe protección auditiva y mascarilla. ¿Cuántas piezas de EPP se entregan?", "10*2", "Se multiplican las personas por las dos piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Qué medida ambiental anota la ficha para los envases vacíos?", "Guardarlos para su retiro por un gestor autorizado", "Botarlos con la basura común", "Quemarlos detrás del taller", "Los envases con restos de productos se retiran por quien está autorizado."),
        ("abc", "{F} Un compañero propone botar el aserrín acumulado en una quebrada cercana. ¿Qué corresponde?", "No: se retira según el plan de residuos, porque el medio ambiente se protege", "Sí: la madera es natural y no daña", "Sí, si se hace de noche", "Los residuos se gestionan según el plan y la norma vigente."),
        ("abc", "{F} ¿Qué entidad fiscaliza el cumplimiento de las normas del sector?", "La entidad fiscalizadora de tu sector, según la norma vigente", "El cliente que compra el mueble", "El proveedor de tableros", "La fiscalización corresponde a una entidad pública competente y no al proveedor."),
        ("ab", "{F} Un estudiante dice: «con mascarilla el polvo del taller ya no es un problema». ¿Qué respuesta es correcta?", "No: el polvo sigue en el ambiente y se controla en su origen", "Sí: la mascarilla elimina el polvo del taller", "La ficha incluye aspiración y mascarilla como medidas distintas."),
        ("abc", "{F} Una estudiante dice: «conozco las medidas del taller, puedo operar las máquinas». ¿Qué respuesta es correcta?", "No: operar máquinas exige instructor autorizado y norma vigente", "Sí: conocer las medidas la habilita", "Sí, si usa mascarilla", "Conocer medidas no habilita para operar máquinas."),
        ("=", "{F} Si el aserrín se retira cada semana, ¿cuántos retiros hay en 8 semanas, si además se retiran los envases cada 2 semanas?", "8+8//2", "Se suman los retiros semanales del aserrín y los retiros de envases cada dos semanas.", " retiros"),
        ("abc", "{F} ¿Qué relación tiene la calidad con el polvo acumulado?", "Un taller con polvo acumulado tiene más riesgos y peores acabados", "Ninguna, son temas separados", "El polvo siempre mejora el acabado", "El polvo acumulado afecta la salud, el riesgo de incendio y la calidad del acabado."),
    ],
    ctx=("abc", "En un taller de ejemplo, el polvo acumulado cerca de un motor eléctrico empieza a arder. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Apagar el fuego con las manos", "Esperar a que se apague solo", "Un conato de incendio se informa a quien corresponde y a emergencias, sin acercarse."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es la higiene industrial?", "El control de agentes del ambiente de trabajo que afectan la salud", "Se ocupa de agentes como el polvo y el ruido."),
        ("¿Qué nivel de la jerarquía de controles va al final?", "El elemento de protección personal", "El EPP protege solo a quien lo usa y no elimina el peligro."),
        ("¿Por qué se habla de «la norma vigente»?", "Porque las normas se actualizan y pueden cambiar", "Se consulta siempre la versión actual."),
    ],
    op=("Taller de ejemplo «Taller Quillay» (ficticio): 6 personas. Agentes: polvo, ruido y residuos. Medidas: aspiración de polvo, protección auditiva y mascarilla, retiro semanal de aserrín y envases entregados a un gestor autorizado. Escribe (a) cuántas piezas de EPP se entregan si cada persona recibe protección auditiva y mascarilla, (b) cuál de las medidas es un control en el origen, (c) qué haces con los envases vacíos y (d) qué haces si el polvo acumulado empieza a arder.",
        "(a) 6×2 son 12 piezas. (b) La aspiración de polvo. (c) Los guardo para su retiro por un gestor autorizado. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula el EPP entregado", "identifica el control en el origen", "propone la gestión de envases", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["decir que la mascarilla elimina el polvo", "botar los envases con la basura común", "intentar apagar el fuego sin autorización"],
        "Pregunta: «¿por qué la aspiración va antes que la mascarilla?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe la diferencia entre higiene industrial y seguridad industrial con un ejemplo de cada una en un taller.",
    extend="Explica por qué un taller necesita un plan de gestión de residuos además de medidas de seguridad para las personas.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (plan de control de calidad de ejemplo, inventado). Puntos de control: P1, recepción de materiales, cada lote; P2, piezas cortadas, muestra de 5 piezas por orden; P3, estructuras armadas, todas; P4, acabado, todas; P5, embalaje, muestra de 3 bultos por envío. "
     "Registros guardados por un tiempo de ejemplo de 12 meses. Roles: controlador de calidad, que inspecciona; jefe de producción, que corrige las causas; prevencionista, que revisa los riesgos; jefe de calidad, que audita el plan.")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario de la gestión de calidad: inspección, muestreo, registro, trazabilidad, acción correctiva y preventiva y auditoría.",
    prior=["Sé qué es una no conformidad.", "Sé qué es un registro.", "Sé multiplicar."],
    explain=[
        "Un plan de control de calidad define en qué puntos del proceso se inspecciona, qué se revisa y con qué frecuencia. La inspección es el examen de un producto para comprobar que cumple lo pedido. El muestreo consiste en inspeccionar solo una parte del lote, la muestra, cuando revisar todo no es posible o necesario. Los resultados quedan en registros, que permiten la trazabilidad: poder seguir la historia de un producto a través de lotes, fechas y responsables.",
        "Cuando aparece un problema se aplica una acción correctiva, que corrige la causa de un problema ya ocurrido para que no se repita. Una acción preventiva, en cambio, actúa antes de que el problema ocurra. La auditoría es una revisión sistemática del plan y de sus registros por una persona que no depende del área auditada. Los roles se reparten entre el controlador, el jefe de producción, el prevencionista y el jefe de calidad, y cada uno firma lo que hace.",
        TAIL,
    ],
    vocab=[("plan de control de calidad", "documento que define puntos de control, qué se revisa y con qué frecuencia"), ("inspección", "examen de un producto para comprobar que cumple lo pedido"), ("muestreo", "inspección de una parte del lote"), ("trazabilidad", "posibilidad de seguir la historia de un producto a través de los registros"), ("acción correctiva", "corrección de la causa de un problema ya ocurrido"), ("acción preventiva", "medida que actúa antes de que ocurra un problema"), ("auditoría", "revisión sistemática del plan y de sus registros")],
    worked=[
        ("Clasificar una acción", "Un taller de ejemplo cambia un procedimiento después de detectar piezas fuera de medida. ¿Qué tipo de acción es?", ["Se actúa sobre un problema que ya ocurrió.", "La corrección de la causa es una acción correctiva."], "Acción correctiva"),
        ("Contar inspecciones", "Un plan de ejemplo inspecciona 4 piezas por orden y se emiten 9 órdenes. ¿Cuántas piezas se inspeccionan?", ["Se multiplican las órdenes por las piezas inspeccionadas en cada una.", "9 por 4 son 36."], "36 piezas"),
    ],
    mistakes=[("Confundir acción correctiva con acción preventiva.", "Una actúa después del problema y la otra antes.", "Se pregunta si el problema ya ocurrió o aún no."),
              ("Creer que si la muestra está bien, todo el lote lo está.", "La muestra es solo una parte del lote.", "Se registra que el resultado corresponde a la muestra inspeccionada.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la trazabilidad?", "La posibilidad de seguir la historia de un producto a través de los registros", "La rapidez con que se fabrica un mueble", "El color de la etiqueta del producto", "La trazabilidad une lotes, fechas y responsables en registros."),
        ("abc", "¿Qué es una acción preventiva?", "Una medida que actúa antes de que ocurra un problema", "La corrección de un defecto ya producido", "Una sanción al operario", "Preventiva significa actuar antes del problema."),
        ("abc", "{F} ¿En qué punto se inspeccionan todas las estructuras armadas?", "P3", "P2", "P5", "La ficha indica que en P3 se controlan todas las estructuras armadas."),
        ("abc", "{F} ¿Qué punto del plan usa una muestra de 3 bultos por envío?", "P5, el embalaje", "P1, la recepción", "P4, el acabado", "La ficha asigna esa muestra al embalaje."),
        ("=", "{F} Si se emiten 12 órdenes y en cada una se inspeccionan 5 piezas cortadas, ¿cuántas piezas se inspeccionan?", "12*5", "Se multiplican las órdenes por las piezas inspeccionadas en cada una.", " piezas"),
        ("=", "{F} Si se envían 7 pedidos y en cada envío se revisan 3 bultos, ¿cuántos bultos se revisan en total?", "7*3", "Se multiplican los envíos por los bultos revisados en cada uno.", " bultos"),
        ("abc", "{F} ¿Quién corrige las causas de un problema según la ficha?", "El jefe de producción", "El controlador de calidad", "El prevencionista", "La ficha asigna la corrección de causas al jefe de producción."),
        ("abc", "{F} ¿Qué rol audita el plan de control?", "El jefe de calidad", "El operador de la máquina", "El proveedor de tableros", "La auditoría la realiza quien no depende del área auditada."),
        ("abc", "{F} Se descubre que varias piezas salen fuera de medida y se cambia la forma de revisarlas para evitar que se repita. ¿Qué tipo de acción es?", "Correctiva", "Preventiva", "Auditoría", "Se corrige la causa de un problema ya ocurrido."),
        ("abc", "{F} Se decide revisar los extintores antes de que se venzan para evitar un problema futuro. ¿Qué tipo de acción es?", "Preventiva", "Correctiva", "Muestreo", "Actúa antes de que el problema ocurra."),
        ("ab", "{F} Un estudiante dice: «los registros solo sirven para archivar y no para rastrear». ¿Qué respuesta es correcta?", "No: los registros permiten la trazabilidad de lotes, fechas y responsables", "Sí: no sirven para nada más", "La explicación indica que los registros permiten seguir la historia de un producto."),
        ("abc", "{F} Una estudiante dice: «sé cómo es el plan, puedo inspeccionar con los instrumentos del taller». ¿Qué respuesta es correcta?", "No: usar instrumentos exige personal capacitado; este cuaderno no habilita", "Sí: conocer el plan basta", "Sí, con lentes de seguridad", "Leer un plan no habilita para trabajar ni para operar equipos."),
        ("=", "{F} Si el plan guarda los registros 12 meses y se revisan los de 3 años, ¿cuántos meses de registros no estarán guardados?", "36-12", "Se restan los meses guardados de los 36 meses revisados.", " meses"),
    ],
    ctx=("abc", "En el taller de ejemplo, durante una auditoría, el controlador de calidad se mueve entre máquinas en funcionamiento sin autorización y casi lo golpea una pieza proyectada. ¿Qué respuesta es correcta?", "Avisar al responsable y no acercarse a las máquinas sin autorización", "Seguir auditando entre las máquinas", "Acercarse más para ver bien", "La auditoría no autoriza a entrar a zonas de riesgo; se avisa al responsable."),
    sc=[
        ("¿Qué es una inspección?", "El examen de un producto para comprobar que cumple lo pedido", "La inspección compara el producto con lo pedido."),
        ("En Muebles y Terminaciones en Madera: ¿qué es el muestreo?", "Inspeccionar una parte del lote", "La muestra es solo una parte del lote."),
        ("En Muebles y Terminaciones en Madera: ¿Qué diferencia hay entre acción correctiva y preventiva?", "La correctiva actúa después del problema y la preventiva antes", "Dependen de si el problema ya ocurrió."),
    ],
    op=("Plan de ejemplo «Taller Ñire» (ficticio): P1, recepción por lote; P2, 4 piezas cortadas por orden; P3, estructuras armadas, todas; P4, acabado, todas. Se emiten 15 órdenes. Un día se detecta que 6 piezas salieron fuera de medida y se modifica la revisión para que no se repita. Escribe (a) cuántas piezas cortadas se inspeccionan, (b) qué tipo de acción es la modificación, (c) qué rol audita el plan y (d) qué sirve para rastrear un lote.",
        "(a) 15×4 son 60 piezas. (b) Acción correctiva. (c) El jefe de calidad. (d) Los registros, que permiten la trazabilidad.",
        ["calcula las piezas inspeccionadas", "clasifica la acción", "nombra al auditor", "nombra los registros"],
        ["hoja con las cuatro respuestas"],
        ["confundir correctiva con preventiva", "olvidar multiplicar por las órdenes", "decir que los registros no sirven para rastrear"],
        "Pregunta: «¿el problema ya ocurrió o aún no?». Si no responde, pídele que relea la diferencia entre acciones."),
    reinforce="Escribe una acción correctiva y una preventiva para un problema de piezas fuera de medida.",
    extend="Explica por qué la persona que audita no debe depender del área auditada.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (inspección de un lote de ejemplo, inventada). Lote de 60 sillas ficticias. Muestra inspeccionada: 12 sillas. Resultados: 6 sin defectos; 3 con una medida fuera de la tolerancia; 1 con una rajadura; 2 con color distinto del de la muestra aprobada. Cada silla defectuosa tiene un solo tipo de defecto. "
     "Criterio de ejemplo: el lote se acepta si en la muestra hay como máximo 2 sillas defectuosas; si hay más, se inspecciona el 100 % del lote. Las sillas defectuosas se separan y se registran.")
build(
    O7, 3, F,
    use="Aprenderé a analizar la inspección de un lote: contar defectos por tipo, calcular el porcentaje en la muestra y aplicar un criterio de aceptación.",
    prior=["Sé qué es el muestreo.", "Sé calcular un porcentaje sencillo.", "Sé qué es una no conformidad."],
    explain=[
        "Al inspeccionar una muestra se cuentan las piezas defectuosas y se clasifican por tipo de defecto: medida fuera de tolerancia, rajadura, color distinto, entre otros. El porcentaje de defectuosas en la muestra se calcula multiplicando las defectuosas por 100 y dividiendo por el tamaño de la muestra. Luego se aplica el criterio de aceptación: si la cantidad de defectuosas supera el máximo permitido, el lote no se acepta con la muestra y se pasa a una inspección del 100 %, que revisa todas las piezas.",
        "Ordenar los tipos de defecto de mayor a menor frecuencia muestra dónde está el problema principal, y ayuda a decidir la acción correctiva. Todo se registra: cuántas piezas, qué defectos y quién inspeccionó. Las piezas defectuosas se separan y no se reparan por cuenta propia: decide el jefe de producción. Estos números son de ejemplo y representan una situación inventada.",
        TAIL,
    ],
    vocab=[("defectuosa", "pieza que no cumple lo pedido"), ("tipo de defecto", "clase de falla, como medida fuera de tolerancia, rajadura o color distinto"), ("inspección al 100 %", "revisión de todas las piezas del lote"), ("frecuencia", "cantidad de veces que ocurre algo"), ("criterio de aceptación", "regla que decide si el lote se acepta")],
    worked=[
        ("Porcentaje en la muestra", "En una muestra de ejemplo de 20 piezas hay 5 defectuosas. ¿Qué porcentaje es?", ["Se multiplica 5 por 100 y se divide por 20.", "500 dividido en 20 son 25."], "25 %"),
        ("Aplicar un criterio", "Con un criterio de ejemplo de máximo 3 defectuosas en la muestra, un lote tiene 4. ¿Qué corresponde?", ["4 supera el máximo de 3.", "Se pasa a inspeccionar todo el lote."], "Inspección al 100 %"),
    ],
    mistakes=[("Aceptar el lote porque «la mitad de la muestra está bien».", "El criterio fija un máximo de defectuosas y no una mitad.", "Se aplica el criterio con el número de defectuosas."),
              ("Reparar por cuenta propia las piezas defectuosas para aceptar el lote.", "Se oculta el problema y no se registra.", "Se separan, se registran y decide el jefe de producción.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una inspección al 100 %?", "La revisión de todas las piezas del lote", "La revisión de una sola pieza elegida al azar", "La revisión del plano antes de cortar", "Al 100 % se revisan todas las piezas, no una muestra."),
        ("abc", "¿Para qué sirve clasificar los defectos por tipo?", "Para ver dónde está el problema principal", "Para contar menos piezas defectuosas", "Para evitar registrar los resultados", "La clasificación muestra qué falla más y orienta la acción correctiva."),
        ("=", "{F} ¿Cuántas sillas defectuosas hay en la muestra?", "3+1+2", "Se suman las sillas con cada tipo de defecto.", " sillas"),
        ("=", "{F} ¿Qué porcentaje de la muestra de 12 sillas es defectuosa (6 sillas)?", "6*100//12", "Se multiplican las defectuosas por 100 y se divide por el tamaño de la muestra.", " %"),
        ("abc", "{F} ¿Qué tipo de defecto es el más frecuente?", "Medida fuera de la tolerancia", "Rajadura", "Color distinto", "Hay 3 sillas con medida fuera de tolerancia, más que de cualquier otro tipo."),
        ("abc", "{F} ¿Qué tipo de defecto es el menos frecuente?", "Rajadura", "Color distinto", "Medida fuera de la tolerancia", "Solo hay 1 silla con rajadura."),
        ("abc", "{F} Con 6 defectuosas y un máximo permitido de 2, ¿qué corresponde hacer?", "Inspeccionar el 100 % del lote", "Aceptar el lote por ser mayoría sin defectos", "Descartar la muestra", "6 supera el máximo de 2, por lo que se revisa todo el lote."),
        ("=", "{F} ¿Cuántas sillas del lote quedan por revisar si se inspecciona el 100 % y ya se revisaron 12?", "60-12", "Se restan las sillas ya revisadas del total del lote.", " sillas"),
        ("=", "{F} ¿Cuántas sillas más defectuosas que el máximo permitido hay en la muestra?", "6-2", "Se restan las defectuosas permitidas de las encontradas.", " sillas"),
        ("abc", "{F} Un compañero propone repintar las 2 sillas de color distinto para que pasen. ¿Qué respuesta es correcta?", "No: se separan y se registran; decide el jefe de producción", "Sí: así se mejora el resultado", "Sí, si usa ventilación", "Reparar por cuenta propia oculta el problema y no queda registrado."),
        ("ab", "{F} Un estudiante dice: «la mitad de la muestra está bien, así que el lote se acepta». ¿Qué respuesta es correcta?", "No: el criterio fija un máximo de 2 defectuosas", "Sí: la mitad sin defectos alcanza", "La ficha dice que el lote se acepta si hay como máximo 2 defectuosas."),
        ("abc", "{F} Una estudiante dice: «ya sé inspeccionar lotes en papel, puedo reparar las sillas con las herramientas del taller». ¿Qué respuesta es correcta?", "No: reparar exige instructor autorizado y norma vigente", "Sí: inspeccionar habilita para reparar", "Sí, si usa lentes", "La inspección en papel no habilita para operar herramientas."),
        ("=", "{F} Si otra muestra de 20 sillas tuviera 4 defectuosas, ¿qué porcentaje sería?", "4*100//20", "Se multiplican las defectuosas por 100 y se divide por el tamaño de la muestra.", " %"),
    ],
    ctx=("abc", "En la inspección de ejemplo, un inspector que mueve una pila de sillas defectuosas siente un tirón fuerte en la espalda y no puede enderezarse. ¿Qué se hace según las reglas generales?", "No seguir levantando, avisar a un adulto responsable y a emergencias", "Seguir moviendo la pila hasta terminar", "Pedirle que levante menos peso sin avisar", "Una lesión se informa a quien corresponde y se pide ayuda de emergencias."),
    sc=[
        ("¿Cómo se calcula el porcentaje de defectuosas de una muestra?", "Defectuosas por 100 dividido en el tamaño de la muestra", "Así la cantidad de defectuosas se expresa como porcentaje de la muestra."),
        ("En Muebles y Terminaciones en Madera: ¿qué pasa si las defectuosas superan el máximo permitido?", "Se inspecciona el 100 % del lote", "El lote no se acepta solo con la muestra."),
        ("¿Para qué se ordenan los defectos de mayor a menor frecuencia?", "Para ver el problema principal", "El ordenamiento muestra dónde conviene actuar primero para mejorar."),
    ],
    op=("Inspección de ejemplo «Taller Peumo» (ficticio): lote de 80 mesas; muestra de 16. Resultados: 10 sin defectos; 3 con medida fuera de tolerancia; 2 con rajaduras; 1 con color distinto. Criterio de ejemplo: máximo 3 defectuosas en la muestra. Escribe (a) cuántas mesas defectuosas hay, (b) qué porcentaje de la muestra es, con la parte entera, (c) qué tipo de defecto es el más frecuente y (d) qué corresponde hacer con el lote.",
        "(a) 3+2+1 son 6 mesas. (b) 6×100÷16 da 37 con resto: 37 %. (c) Medida fuera de tolerancia. (d) Como 6 supera el máximo de 3, se inspecciona el 100 % del lote.",
        ["suma las defectuosas", "calcula el porcentaje con parte entera", "identifica el defecto más frecuente", "decide con el criterio"],
        ["hoja con las cuatro respuestas"],
        ["no aplicar el criterio", "reparar por cuenta propia", "confundir muestra con lote"],
        "Pregunta: «¿qué compara el criterio de aceptación?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula el porcentaje de defectuosas de una muestra de 25 piezas con 5 defectuosas.",
    extend="Explica por qué una inspección al 100 % puede ser más cara pero más segura que una muestra.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (indicadores de calidad de ejemplo, inventada). Registro de 4 semanas del taller ficticio. Piezas producidas y defectuosas por semana: semana 1, 200 y 10; semana 2, 250 y 5; semana 3, 150 y 9; semana 4, 400 y 12. "
     "Meta de ejemplo: una tasa de defectos de como máximo 4 % por semana. Costo de ejemplo de reproceso: $4.000 por pieza defectuosa. Todas las divisiones del enunciado dan resultados exactos.")
build(
    O7, 4, F,
    use="Aprenderé a calcular indicadores de calidad en papel: tasa de defectos por semana, cumplimiento de una meta y costo del reproceso.",
    prior=["Sé calcular porcentajes sencillos.", "Sé qué es una tasa de rechazo.", "Sé leer una tabla."],
    explain=[
        "Un indicador de calidad es un número que resume cómo va el proceso. La tasa de defectos es el porcentaje de piezas defectuosas respecto de las producidas: se multiplican las defectuosas por 100 y se divide por las producidas. Una meta fija el valor máximo aceptable; si la tasa de una semana es igual o menor que la meta, la semana cumple. Los indicadores se miran en el tiempo para ver si mejoran o empeoran.",
        "El reproceso es volver a trabajar una pieza defectuosa para que cumpla; tiene un costo en material, tiempo y desgaste de equipos. Multiplicar las piezas defectuosas por el costo de reproceso da el costo de la mala calidad. Un indicador no repara nada por sí solo: sirve para decidir qué acción correctiva o preventiva tomar y se informa a quien corresponde. Los números de esta clase son de ejemplo y no representan resultados reales.",
        TAIL,
    ],
    vocab=[("indicador de calidad", "número que resume cómo va el proceso"), ("tasa de defectos", "porcentaje de piezas defectuosas respecto de las producidas"), ("meta", "valor máximo o mínimo que se desea alcanzar"), ("reproceso", "trabajo adicional para que una pieza defectuosa cumpla"), ("costo de la mala calidad", "dinero gastado por piezas defectuosas y su reproceso")],
    worked=[
        ("Tasa de defectos", "En una semana de ejemplo se producen 300 piezas y 12 son defectuosas. ¿Qué tasa de defectos hay?", ["Se multiplica 12 por 100 y se divide por 300.", "1.200 dividido en 300 son 4."], "4 %"),
        ("Cumplir una meta", "Con una meta de ejemplo de máximo 5 %, una semana tiene 3 %. ¿Cumple?", ["Se compara 3 con 5.", "3 es menor que 5."], "Sí, cumple"),
    ],
    mistakes=[("Dividir al revés (producidas por defectuosas).", "El porcentaje se calcula sobre el total producido.", "Se multiplican las defectuosas por 100 y se divide por las producidas."),
              ("Mirar solo una semana y sacar conclusiones.", "Una semana puede ser distinta por casualidad.", "Se compara la evolución de varias semanas.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una meta de calidad?", "El valor máximo o mínimo que se desea alcanzar", "El nombre de la última pieza defectuosa", "El total de piezas guardadas en la bodega", "La meta es el valor objetivo del indicador."),
        ("abc", "¿Qué es el reproceso?", "El trabajo adicional para que una pieza defectuosa cumpla", "La compra de más material", "La entrega al cliente", "El reproceso corrige piezas y tiene un costo."),
        ("=", "{F} ¿Cuál es la tasa de defectos de la semana 1 (10 defectuosas de 200)?", "10*100//200", "Se multiplican las defectuosas por 100 y se divide por las producidas.", " %"),
        ("=", "{F} ¿Cuál es la tasa de defectos de la semana 2 (5 defectuosas de 250)?", "5*100//250", "Se multiplican las defectuosas por 100 y se divide por las producidas.", " %"),
        ("=", "{F} ¿Cuál es la tasa de defectos de la semana 3 (9 defectuosas de 150)?", "9*100//150", "Se multiplican las defectuosas por 100 y se divide por las producidas.", " %"),
        ("=", "{F} ¿Cuál es la tasa de defectos de la semana 4 (12 defectuosas de 400)?", "12*100//400", "Se multiplican las defectuosas por 100 y se divide por las producidas.", " %"),
        ("abc", "{F} ¿Qué semanas cumplen la meta de 4 % como máximo?", "Las semanas 2 y 4", "Las semanas 1 y 3", "Solo la semana 3", "Las semanas 2 y 4 tienen 2 % y 3 %, ambas bajo 4 %."),
        ("=", "{F} ¿Cuántas piezas defectuosas hubo en las cuatro semanas?", "10+5+9+12", "Se suman las defectuosas de cada semana.", " piezas"),
        ("=", "{F} ¿Cuánto es el costo de reproceso de las 36 piezas defectuosas?", "36*4000", "Se multiplican las piezas defectuosas por el costo de cada reproceso.", " pesos"),
        ("abc", "{F} ¿En qué semana fue peor la tasa de defectos?", "En la semana 3", "En la semana 1", "En la semana 4", "La semana 3 tuvo 6 %, el valor más alto."),
        ("ab", "{F} Un compañero dice: «la semana 4 tuvo más defectuosas que la 1, así que tuvo peor tasa». ¿Qué respuesta es correcta?", "No: la tasa compara con lo producido, y la semana 4 tuvo 3 % contra 5 % de la semana 1", "Sí: más defectuosas siempre es peor tasa", "La semana 4 produjo 400 piezas y la semana 1 produjo 200, por eso la tasa es menor."),
        ("abc", "{F} Una estudiante dice: «ya sé calcular indicadores, puedo reprocesar las piezas con las máquinas». ¿Qué respuesta es correcta?", "No: reprocesar exige instructor autorizado y norma vigente", "Sí: calcular habilita para reprocesar", "Sí, si usa EPP", "Un cálculo en papel no habilita para operar máquinas."),
        ("abc", "{F} Si la tasa sube dos semanas seguidas, ¿qué corresponde?", "Informar al jefe de producción y analizar la causa", "Ocultar el dato para no preocupar", "Esperar a que mejore sola", "Un indicador que empeora exige analizar y decidir una acción."),
    ],
    ctx=("abc", "En el taller de ejemplo, para bajar la tasa de defectos, un jefe presiona a trabajar más rápido y un operario cansado se acerca a una máquina en movimiento. ¿Qué respuesta es correcta?", "Avisar al responsable: apurar el trabajo aumenta los riesgos y no mejora la calidad", "Seguir porque la meta es lo más importante", "Pedirle más EPP", "La presión por la meta no justifica poner en riesgo a las personas."),
    sc=[
        ("¿Cómo se calcula la tasa de defectos?", "Defectuosas por 100 dividido en las producidas", "Compara las defectuosas con el total producido."),
        ("En Muebles y Terminaciones en Madera: ¿qué significa que una semana cumple la meta?", "Que su tasa es igual o menor que el máximo fijado", "La meta de ejemplo era un máximo."),
        ("¿Qué costo da multiplicar las defectuosas por el costo de reproceso?", "El costo de la mala calidad", "Resume el dinero gastado por los defectos."),
    ],
    op=("Indicadores de ejemplo «Taller Quillay» (ficticio): 3 semanas. Semana A: 100 piezas y 8 defectuosas; semana B: 300 piezas y 9 defectuosas; semana C: 50 piezas y 4 defectuosas. Meta de ejemplo: máximo 5 %. Costo de reproceso de ejemplo: $3.000 por pieza defectuosa. Escribe (a) la tasa de cada semana, (b) cuál cumple la meta, (c) el total de defectuosas y (d) el costo de reproceso total.",
        "(a) A: 8×100÷100 es 8 %; B: 9×100÷300 es 3 %; C: 4×100÷50 es 8 %. (b) Solo la semana B. (c) 8+9+4 son 21 piezas. (d) 21×3.000 son 63.000 pesos.",
        ["calcula las tres tasas", "identifica la semana que cumple", "suma las defectuosas", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "comparar defectuosas sin considerar lo producido", "olvidar el costo de cada pieza"],
        "Pregunta: «¿por qué se compara la tasa y no la cantidad de defectuosas?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula la tasa de defectos de 360 piezas producidas con 18 defectuosas.",
    extend="Explica qué decisiones podría tomar un jefe de calidad al ver que la tasa empeora tres semanas seguidas.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (comparación de proveedores de ejemplo, inventada). Taller ficticio que necesita 100 tableros. Proveedor A: $30.000 por tablero, 6 tableros defectuosos esperados de cada 100, con madera de origen documentado. "
     "Proveedor B: $32.000 por tablero, 2 tableros defectuosos esperados de cada 100, sin origen documentado. "
     "Exigencia del taller (de ejemplo): solo se compra madera de origen documentado. Un tablero defectuoso se pierde y se paga igual.")
build(
    O7, 5, F,
    use="Aprenderé a comparar dos proveedores con criterios de costo, calidad y requisitos ambientales y legales, y a dejar registrada la decisión.",
    prior=["Sé calcular costos totales.", "Sé qué es una tasa de defectos.", "Sé qué es el origen documentado."],
    explain=[
        "Elegir un proveedor no se reduce al precio unitario. Se comparan el costo total, la calidad esperada y el cumplimiento de requisitos. El costo total de una compra suma el precio de los productos y el valor de lo que se pierde por defectos. Los requisitos son condiciones que el taller exige sí o sí, como que la madera tenga origen documentado: un proveedor que no cumple un requisito queda fuera, aunque sea más barato o de mejor calidad.",
        "Verificar la calidad antes de decidir significa pedir documentos y muestras y luego controlar la recepción con un registro. La decisión se escribe: qué opciones se compararon, qué criterios se usaron y quién decidió. Elegir madera de origen documentado también es una medida ambiental: ayuda a evitar la explotación ilegal. Los precios y los porcentajes de esta clase son inventados.",
        TAIL,
    ],
    vocab=[("costo total", "precio de los productos más el valor de lo que se pierde por defectos"), ("requisito", "condición que el taller exige sí o sí"), ("origen documentado", "madera cuyo origen está respaldado por documentos"), ("verificar", "comprobar con documentos o muestras que se cumple lo pedido"), ("criterio de decisión", "razón escrita para elegir una opción")],
    worked=[
        ("Costo de una compra", "Un proveedor de ejemplo vende 10 tableros a $20.000 cada uno. ¿Cuánto cuesta la compra?", ["Se multiplican los tableros por el precio de cada uno.", "10 por 20.000 son 200.000."], "$200.000"),
        ("Requisito primero", "Un proveedor de ejemplo es muy barato pero no cumple un requisito exigido. ¿Se elige?", ["Un requisito exigido se cumple sí o sí.", "El precio no compensa el incumplimiento."], "No, queda fuera"),
    ],
    mistakes=[("Elegir el proveedor más barato sin revisar los requisitos.", "Puede incumplir una exigencia del taller o de la norma vigente.", "Primero se verifican los requisitos y luego se compara el costo."),
              ("Ignorar los defectos esperados al comparar precios.", "Los tableros defectuosos se pagan igual y se pierden.", "Se calcula el costo total incluyendo lo perdido.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es un requisito al elegir un proveedor?", "Una condición que el taller exige sí o sí", "Un descuento por comprar más", "La publicidad del proveedor", "Un requisito es una exigencia obligatoria, no un beneficio."),
        ("abc", "¿Qué significa verificar la calidad de un proveedor?", "Comprobar con documentos y muestras que cumple lo pedido", "Aceptar su palabra sin pruebas", "Comprar siempre al más barato", "Verificar es comprobar con documentos y muestras, no solo confiar."),
        ("=", "{F} ¿Cuánto cuesta la compra de 100 tableros al proveedor A?", "100*30000", "Se multiplican los tableros por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la compra de 100 tableros al proveedor B?", "100*32000", "Se multiplican los tableros por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuánto vale lo perdido por los 6 tableros defectuosos del proveedor A?", "6*30000", "Se multiplican los defectuosos por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuánto vale lo perdido por los 2 tableros defectuosos del proveedor B?", "2*32000", "Se multiplican los defectuosos por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del proveedor A (compra de 3.000.000 más pérdida de 180.000)?", "3000000+180000", "Se suman la compra y lo perdido por defectos.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del proveedor B (compra de 3.200.000 más pérdida de 64.000)?", "3200000+64000", "Se suman la compra y lo perdido por defectos.", " pesos"),
        ("abc", "{F} Por costo total solamente, ¿qué proveedor resulta más barato?", "El proveedor A", "El proveedor B", "Cuestan lo mismo", "A suma $3.180.000 y B suma $3.264.000."),
        ("abc", "{F} ¿Qué proveedor cumple la exigencia de origen documentado?", "El proveedor A", "El proveedor B", "Ninguno", "La ficha indica que A tiene madera de origen documentado y B no."),
        ("ab", "{F} Un compañero dice: «B tiene menos defectos, así que lo elegimos aunque no tenga origen documentado». ¿Qué respuesta es correcta?", "No: el requisito de origen documentado se cumple sí o sí", "Sí: la calidad pesa más que cualquier requisito", "La ficha indica que el taller solo compra madera con origen documentado."),
        ("abc", "{F} Una estudiante dice: «ya elegí proveedor, puedo manejar los tableros con equipos de carga». ¿Qué respuesta es correcta?", "No: mover cargas con equipos exige personal autorizado y norma vigente", "Sí: elegir habilita para manejar equipos", "Sí, con calzado de seguridad", "Elegir proveedor es un trabajo de papel y no habilita para manejar equipos."),
        ("abc", "{F} ¿Qué se registra al decidir entre proveedores?", "Las opciones, los criterios y quién decidió", "Solo el nombre del elegido", "Solo el precio más bajo", "El registro permite revisar la decisión después."),
    ],
    ctx=("abc", "En la bodega de ejemplo, una pila de tableros del proveedor elegido empieza a inclinarse mientras alguien trabaja a su lado. ¿Qué se hace según las reglas generales?", "No acercarse a la pila, avisar a un adulto responsable y a emergencias si hay una persona atrapada", "Sostener la pila con el cuerpo", "Seguir trabajando a su lado", "Una pila inestable es un riesgo; se avisa a quien corresponde."),
    sc=[
        ("¿Qué incluye el costo total de una compra?", "El precio de los productos y lo perdido por defectos", "Los defectos se pagan y se pierden."),
        ("En Muebles y Terminaciones en Madera: ¿qué se hace con un proveedor que no cumple un requisito?", "Queda fuera aunque sea más barato", "Un requisito exigido se cumple sí o sí."),
        ("¿Por qué elegir madera de origen documentado es una medida ambiental?", "Porque ayuda a evitar la explotación ilegal", "El documento respalda la procedencia de la madera."),
    ],
    op=("Comparación de ejemplo «Taller Ñire» (ficticio): se necesitan 50 tableros. Proveedor C: $20.000 por tablero, 4 defectuosos esperados, con origen documentado. Proveedor D: $18.000 por tablero, 5 defectuosos esperados, sin origen documentado. El taller exige origen documentado. Escribe (a) el costo total de C, (b) el costo total de D, (c) qué proveedor eliges y por qué, y (d) qué registras de la decisión.",
        "(a) 50×20.000 son 1.000.000 y 4×20.000 son 80.000: 1.080.000 pesos. (b) 50×18.000 son 900.000 y 5×18.000 son 90.000: 990.000 pesos. (c) Elijo C, porque D no cumple el requisito de origen documentado aunque sea más barato. (d) Las opciones, los criterios y quién decidió.",
        ["calcula el costo total de C", "calcula el costo total de D", "elige por el requisito", "describe el registro"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio sin mirar el requisito", "olvidar la pérdida por defectos", "no registrar la decisión"],
        "Pregunta: «¿qué se mira primero, el precio o el requisito?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula el costo total de 20 tableros de $25.000 con 1 defectuoso que se pierde.",
    extend="Explica por qué un requisito legal o ambiental puede pesar más que el precio.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 6 (obra de ejemplo, inventada). En la obra ficticia «Casa Lomas» se instalan 6 puertas y 4 ventanas de madera. Cuadrilla: 3 personas instaladoras del taller ficticio; en la obra trabajan además 8 personas de otros oficios. "
     "Riesgos anotados: caída de objetos, trabajo en altura en las ventanas del segundo piso, herramientas eléctricas, manipulación de hojas pesadas, vidrios, polvo, cables sueltos y tránsito de otros oficios. "
     "Medidas anotadas: casco y calzado de seguridad, zona delimitada bajo el trabajo en altura, personal autorizado para trabajo en altura, coordinación con el jefe de obra, pisos ordenados y hojas movidas entre dos personas.")
build(
    O8, 1, F,
    use="Aprenderé qué significa instalar muebles, puertas y ventanas en una obra y qué riesgos tiene ese entorno, sin ningún procedimiento de instalación.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un EPP.", "Sé sumar y multiplicar."],
    explain=[
        "Instalar en obra es colocar en su lugar definitivo muebles, puertas, ventanas, molduras y tabiques de madera, incorporando fijaciones y quincallería, según planos y especificaciones técnicas. La quincallería son los herrajes, como bisagras, cerraduras y tiradores; las fijaciones son los elementos que sujetan el mueble o la hoja, como tornillos y pernos. Cómo se instala cada elemento lo enseña un instructor autorizado y está en las instrucciones del fabricante; este cuaderno no las contiene.",
        "Una obra es un entorno compartido con personas de otros oficios, por lo que los riesgos se suman: caída de objetos, trabajo en altura, herramientas eléctricas, cables sueltos, polvo y manipulación de hojas pesadas. La coordinación con el jefe de obra evita que dos cuadrillas trabajen una sobre otra. Solo el personal autorizado trabaja en altura y se delimita la zona bajo ese trabajo. Según la jerarquía de controles, el EPP, como el casco y el calzado, es el último nivel y no reemplaza esas medidas.",
        TAIL,
    ],
    vocab=[("instalar", "colocar en su lugar definitivo un mueble, puerta o ventana"), ("quincallería", "herrajes como bisagras, cerraduras y tiradores"), ("fijación", "elemento que sujeta una pieza, como un tornillo"), ("jefe de obra", "persona que coordina todos los oficios de la obra"), ("zona delimitada", "área marcada donde no se debe pasar por un riesgo"), ("hoja", "parte móvil de una puerta o ventana")],
    worked=[
        ("Contar elementos", "Una obra de ejemplo instala 7 puertas y 3 ventanas. ¿Cuántos elementos son?", ["Se suman puertas y ventanas.", "7 más 3 son 10."], "10 elementos"),
        ("Clasificar un herraje", "Un elemento de ejemplo es una bisagra. ¿Es quincallería o fijación?", ["Las bisagras son herrajes.", "Los herrajes forman la quincallería."], "Quincallería"),
    ],
    mistakes=[("Trabajar bajo otra persona que está en altura porque «es rápido».", "Pueden caer objetos sobre quien está debajo.", "Se respeta la zona delimitada y se coordina con el jefe de obra."),
              ("Creer que el casco permite hacer trabajo en altura sin autorización.", "El EPP es el último nivel y no reemplaza la autorización.", "Solo el personal autorizado trabaja en altura.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la quincallería?", "Los herrajes, como bisagras, cerraduras y tiradores", "Las tablas que forman las puertas", "El adhesivo para las uniones", "La quincallería son los herrajes; las tablas y el adhesivo son otros insumos."),
        ("abc", "¿Qué es una fijación?", "Un elemento que sujeta una pieza, como un tornillo", "Un plano de la obra", "Un tipo de barniz", "La fijación sujeta; el plano y el barniz son otras cosas."),
        ("=", "{F} ¿Cuántos elementos de madera se instalan en total?", "6+4", "Se suman las puertas y las ventanas.", " elementos"),
        ("=", "{F} ¿Cuántas personas hay en total en la obra (cuadrilla y otros oficios)?", "3+8", "Se suman las personas de la cuadrilla y las de otros oficios.", " personas"),
        ("abc", "{F} ¿Qué riesgo de la ficha se debe a las ventanas del segundo piso?", "El trabajo en altura", "El ruido de la bodega", "La intoxicación por solventes", "Las ventanas del segundo piso implican trabajo en altura."),
        ("abc", "{F} ¿Qué medida de la ficha protege a quienes pasan bajo el trabajo en altura?", "La zona delimitada bajo ese trabajo", "El calzado de seguridad", "Los pisos ordenados", "La zona delimitada evita que haya personas donde pueden caer objetos."),
        ("=", "{F} Cada una de las 3 personas de la cuadrilla recibe casco y calzado de seguridad. ¿Cuántas piezas de EPP se entregan?", "3*2", "Se multiplican las personas por las dos piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Con quién se coordina para evitar que dos cuadrillas trabajen una sobre otra?", "Con el jefe de obra", "Con el proveedor de herrajes", "Con el cliente final", "El jefe de obra coordina todos los oficios."),
        ("abc", "{F} Las hojas pesadas se mueven entre dos personas. ¿Qué riesgo busca evitar esa medida?", "Esfuerzos y golpes por manipulación manual de cargas", "El ruido", "El polvo", "Mover una carga entre dos reduce el esfuerzo y los golpes."),
        ("ab", "{F} Un instalador dice: «con casco puedo trabajar en altura sin autorización». ¿Qué respuesta es correcta?", "No: el EPP no reemplaza la autorización para trabajo en altura", "Sí: el casco basta", "La ficha pide personal autorizado para trabajo en altura."),
        ("abc", "{F} Una estudiante dice: «conozco las medidas de la obra, puedo instalar una ventana». ¿Qué respuesta es correcta?", "No: instalar exige instructor autorizado y norma vigente", "Sí: conocer las medidas la habilita", "Sí, con casco y calzado", "Conocer las medidas no habilita para instalar."),
        ("=", "{F} Una hoja pesada se mueve entre 2 de las 3 personas de la cuadrilla. ¿Cuántas personas de la cuadrilla no cargan la hoja?", "3-2", "Se restan las personas que cargan la hoja del total de la cuadrilla.", " persona"),
        ("abc", "{F} ¿Qué hacer si se ve un cable suelto en el pasillo de la obra?", "Avisar al jefe de obra para que se ordene", "Pasar por encima de él con cuidado", "Cortarlo para despejar el paso", "Un cable suelto es riesgo de tropiezo o de descarga; se informa a quien coordina."),
    ],
    ctx=("abc", "En una obra de ejemplo, una persona cae desde una escalera mientras instala una cortina cerca de una ventana. ¿Qué se hace según las reglas generales?", "No mover a la persona, avisar a un adulto responsable y a emergencias", "Levantarla de inmediato", "Ignorar el accidente y continuar", "Ante una caída no se mueve a la persona y se pide ayuda a emergencias."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es instalar en obra?", "Colocar en su lugar definitivo muebles, puertas y ventanas", "Es la etapa final de colocación."),
        ("¿Quién coordina los oficios de la obra?", "El jefe de obra", "Coordina los oficios para evitar cruces peligrosos entre cuadrillas."),
        ("En Muebles y Terminaciones en Madera: ¿Quién puede trabajar en altura?", "Solo personal autorizado", "El trabajo en altura exige autorización."),
    ],
    op=("Obra de ejemplo «Casa Peumo» (ficticia): se instalan 8 puertas y 5 ventanas. La cuadrilla tiene 4 personas y recibe casco y calzado de seguridad. Riesgos: caída de objetos y trabajo en altura. Escribe (a) cuántos elementos se instalan, (b) cuántas piezas de EPP se entregan, (c) qué medida protege a quienes pasan bajo el trabajo en altura y (d) qué haces si alguien cae desde altura.",
        "(a) 8+5 son 13 elementos. (b) 4×2 son 8 piezas. (c) La zona delimitada bajo el trabajo. (d) No muevo a la persona, aviso a un adulto responsable y a emergencias.",
        ["suma los elementos", "calcula el EPP entregado", "propone la zona delimitada", "avisa sin mover a la persona"],
        ["hoja con las cuatro respuestas"],
        ["decir que el EPP reemplaza la autorización", "mover a la persona caída", "confundir quincallería con fijación"],
        "Pregunta: «¿por qué se delimita la zona bajo el trabajo en altura?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe la diferencia entre quincallería y fijaciones con dos ejemplos de cada una.",
    extend="Explica por qué en una obra compartida la coordinación con el jefe de obra es una medida de seguridad.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 7 (planilla de quincallería de ejemplo, inventada). Puerta tipo P1: 3 bisagras, 1 cerradura, 1 tirador y 18 tornillos. Ventana tipo V1: 2 bisagras, 1 manilla y 8 tornillos. "
     "Obra de ejemplo: 6 puertas P1 y 4 ventanas V1. Documentos: plano de instalación (ubicación de cada elemento), especificaciones técnicas (materiales y herrajes), planilla de quincallería y acta de entrega firmada por el cliente. "
     "Roles: instalador autorizado, jefe de obra, inspector técnico que revisa la calidad y cliente que recibe.")
build(
    O8, 2, F,
    use="Aprenderé qué documentos se usan al instalar —plano, especificaciones, planilla de quincallería y acta de entrega— y qué rol cumple cada persona.",
    prior=["Sé qué es la quincallería y una fijación.", "Sé multiplicar y sumar.", "Sé leer una planilla."],
    explain=[
        "El plano de instalación muestra dónde va cada elemento: puerta, ventana, mueble o moldura. Las especificaciones técnicas dicen de qué material es cada elemento y qué herrajes lleva. La planilla de quincallería cuenta cuántos herrajes y fijaciones se necesitan por tipo de elemento y en total. El vano es la abertura de un muro donde va una puerta o ventana; el marco es la estructura fija que la rodea; la hoja es la parte móvil. La holgura es el espacio que queda entre la hoja y el marco.",
        "El acta de entrega es el documento firmado por el cliente que deja constancia de lo instalado y de los pendientes. Los roles se reparten así: el instalador autorizado instala, el jefe de obra coordina, el inspector técnico revisa la calidad y el cliente recibe. Leer los documentos es comparar el plano, las especificaciones y la planilla: si no coinciden, se consulta y no se improvisa. Los números de esta clase son de ejemplo.",
        TAIL,
    ],
    vocab=[("vano", "abertura de un muro donde va una puerta o ventana"), ("marco", "estructura fija que rodea la hoja"), ("holgura", "espacio que queda entre la hoja y el marco"), ("planilla de quincallería", "tabla que cuenta los herrajes y las fijaciones por tipo de elemento"), ("acta de entrega", "documento firmado por el cliente con lo instalado y los pendientes"), ("inspector técnico", "persona que revisa la calidad de la obra")],
    worked=[
        ("Leer la planilla", "Una puerta de ejemplo lleva 2 bisagras y 4 tornillos por bisagra. ¿Cuántos tornillos de bisagras lleva?", ["Se multiplican las bisagras por los tornillos de cada una.", "2 por 4 son 8."], "8 tornillos"),
        ("Reconocer el documento", "Una persona de ejemplo quiere saber dónde va cada ventana en la obra. ¿Qué documento consulta?", ["La ubicación de cada elemento está en el plano de instalación.", "No está en la planilla de quincallería."], "El plano de instalación"),
    ],
    mistakes=[("Confundir el acta de entrega con la planilla de quincallería.", "La planilla cuenta herrajes y el acta deja constancia firmada con el cliente.", "Cada documento se usa para su función."),
              ("Contar los tornillos de una puerta dos veces.", "Se obtienen cantidades distintas y se compra de más.", "Se cuentan los de cada herraje una sola vez.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es el vano?", "La abertura de un muro donde va una puerta o ventana", "La parte móvil de una puerta", "El espacio entre la hoja y el marco", "El vano es la abertura; la hoja es la parte móvil y la holgura es el espacio."),
        ("abc", "En Muebles y Terminaciones en Madera: ¿Qué es el acta de entrega?", "El documento firmado por el cliente con lo instalado y los pendientes", "La planilla que cuenta los herrajes", "El plano de ubicación", "El acta deja constancia firmada de la entrega."),
        ("=", "{F} ¿Cuántas bisagras necesitan las 6 puertas P1?", "6*3", "Se multiplican las puertas por las bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuántas bisagras necesitan las 4 ventanas V1?", "4*2", "Se multiplican las ventanas por las bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuántas bisagras se necesitan en total en la obra?", "6*3+4*2", "Se suman las bisagras de puertas y de ventanas.", " bisagras"),
        ("=", "{F} ¿Cuántos tornillos se necesitan para las 6 puertas P1?", "6*18", "Se multiplican las puertas por los tornillos de cada una.", " tornillos"),
        ("=", "{F} ¿Cuántos tornillos se necesitan en total para puertas y ventanas?", "6*18+4*8", "Se suman los tornillos de puertas y de ventanas.", " tornillos"),
        ("abc", "{F} ¿Qué rol revisa la calidad de lo instalado?", "El inspector técnico", "El instalador", "El cliente que recibe", "Revisar la calidad es función del inspector técnico."),
        ("abc", "{F} ¿Qué documento muestra la ubicación de cada elemento?", "El plano de instalación", "La planilla de quincallería", "El acta de entrega", "La ubicación está en el plano de instalación."),
        ("abc", "{F} ¿Dónde se especifica el material de cada elemento?", "En las especificaciones técnicas", "En el acta de entrega", "En la planilla de quincallería", "Las especificaciones técnicas dicen el material y los herrajes."),
        ("ab", "{F} Un compañero dice: «cuento las cerraduras junto con las bisagras como si fueran el mismo herraje». ¿Qué respuesta es correcta?", "No: se cuentan por separado porque son herrajes distintos", "Sí: son lo mismo", "La planilla separa bisagras, cerraduras y tiradores."),
        ("abc", "{F} Una estudiante dice: «sé leer la planilla, puedo instalar una puerta». ¿Qué respuesta es correcta?", "No: instalar exige instructor autorizado y norma vigente", "Sí: leer la planilla habilita para instalar", "Sí, con casco", "Leer una planilla no habilita para trabajar en obra."),
        ("abc", "{F} ¿Qué herraje lleva la ventana V1 y no la puerta P1?", "Una manilla", "Una cerradura", "Un tirador", "La ventana lleva manilla; la puerta lleva cerradura y tirador."),
    ],
    ctx=("abc", "En una obra de ejemplo, el inspector técnico encuentra que el plano muestra una ventana donde la planilla lista una puerta. ¿Qué respuesta es correcta?", "Anotar la diferencia y consultar antes de instalar", "Elegir la opción más fácil", "Instalar lo que parezca mejor", "Si los documentos no coinciden no se improvisa: se consulta."),
    sc=[
        ("¿Qué es la hoja de una puerta?", "La parte móvil", "Es la que se abre y se cierra."),
        ("En Muebles y Terminaciones en Madera: ¿para qué sirve la planilla de quincallería?", "Para contar los herrajes y fijaciones por tipo de elemento", "Cuenta lo que hay que comprar y llevar."),
        ("¿Qué se hace si el plano y la planilla no coinciden?", "Se consulta, no se improvisa", "Un error en un documento se resuelve con quien lo emitió."),
    ],
    op=("Planilla de ejemplo «Casa Ñire» (ficticia): puerta tipo P2: 3 bisagras y 12 tornillos; ventana tipo V2: 2 bisagras y 6 tornillos. Obra: 5 puertas P2 y 3 ventanas V2. Escribe (a) cuántas bisagras se necesitan en total, (b) cuántos tornillos en total, (c) qué documento dice dónde va cada elemento y (d) qué haces si el plano muestra 4 ventanas y la planilla dice 3.",
        "(a) 5×3+3×2 son 21 bisagras. (b) 5×12+3×6 son 78 tornillos. (c) El plano de instalación. (d) Anoto la diferencia y consulto antes de instalar.",
        ["calcula las bisagras", "calcula los tornillos", "nombra el plano de instalación", "consulta ante la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar ventanas y puertas", "confundir los documentos", "improvisar ante la diferencia"],
        "Pregunta: «¿qué documento muestra la ubicación?». Si no responde, pídele que relea el vocabulario."),
    reinforce="Escribe tres documentos que se usan al instalar y para qué sirve cada uno.",
    extend="Explica qué ventaja tiene el acta de entrega para el cliente y para el taller.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 8 (registro de vanos de ejemplo, inventado). El criterio de ejemplo de holgura total en el ancho (suma de los dos lados) es de 5 a 9 mm, ambos incluidos. "
     "Medidas en milímetros anotadas por el inspector técnico (vano y hoja): P1: vano 900, hoja 892; P2: vano 900, hoja 897; P3: vano 920, hoja 910; P4: vano 850, hoja 843; P5: vano 800, hoja 795. "
     "La holgura se calcula como medida del vano menos medida de la hoja. Lo que no cumple se separa y se informa al jefe de obra.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un registro de vanos y hojas: calcular la holgura, aplicar un criterio de aceptación y decidir qué hacer con lo que no cumple.",
    prior=["Sé qué es un vano y una holgura.", "Sé restar.", "Sé qué es un criterio de aceptación."],
    explain=[
        "Antes de instalar, se compara la medida de cada vano con la de su hoja. La holgura total en el ancho es la medida del vano menos la medida de la hoja; el criterio de aceptación fija una holgura mínima y una máxima. Una holgura menor que la mínima indica que la hoja podría no caber; una mayor que la máxima indica un hueco excesivo. En ambos casos el elemento no se instala por cuenta propia: se informa al jefe de obra.",
        "Esta comparación se hace en papel, con las medidas anotadas por el inspector técnico. Las medidas de esta ficha son inventadas y los criterios reales los fijan las especificaciones del proyecto y la norma vigente. Si más de un elemento incumple, conviene revisar si el error está en los vanos de la obra o en las hojas del taller, y registrar esa información: así se evita repetir el problema en otras obras.",
        TAIL,
    ],
    vocab=[("holgura total", "medida del vano menos la medida de la hoja"), ("holgura mínima", "valor más bajo que acepta el criterio"), ("holgura máxima", "valor más alto que acepta el criterio"), ("inspector técnico", "persona que revisa las medidas y la calidad de la obra"), ("incumple", "no cumple lo pedido")],
    worked=[
        ("Calcular la holgura", "Un vano de ejemplo mide 700 mm y su hoja mide 693 mm. ¿Cuál es la holgura?", ["Se resta la hoja del vano.", "700 menos 693 son 7."], "7 mm"),
        ("Aplicar un criterio", "Con un criterio de ejemplo de 3 a 6 mm, una holgura de 7 mm, ¿se acepta?", ["Se compara 7 con el máximo de 6.", "7 supera el máximo."], "No, se informa al jefe de obra"),
    ],
    mistakes=[("Restar al revés (hoja menos vano).", "Se obtiene una holgura negativa sin sentido.", "Siempre se resta la medida de la hoja de la medida del vano."),
              ("Decidir por cuenta propia cambiar el vano para que la hoja entre.", "No se sabe cuál es el error ni quién lo resuelve.", "Se informa al jefe de obra y se registra la diferencia.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿cómo se calcula la holgura total en el ancho?", "Medida del vano menos medida de la hoja", "Medida de la hoja menos medida del vano", "Suma de las medidas del vano y la hoja", "La holgura es el espacio que queda: vano menos hoja."),
        ("abc", "¿Qué indica una holgura menor que la mínima?", "Que la hoja podría no caber", "Que hay un hueco excesivo", "Que la puerta es muy liviana", "Una holgura menor que la mínima indica que el espacio es insuficiente."),
        ("=", "{F} ¿Cuántos mm de holgura tiene P1?", "900-892", "Se resta la medida de la hoja de la medida del vano.", " mm"),
        ("=", "{F} ¿Cuántos mm de holgura tiene P2?", "900-897", "Se resta la medida de la hoja de la medida del vano.", " mm"),
        ("=", "{F} ¿Cuántos mm de holgura tiene P3?", "920-910", "Se resta la medida de la hoja de la medida del vano.", " mm"),
        ("=", "{F} ¿Cuántos mm de holgura tiene P4?", "850-843", "Se resta la medida de la hoja de la medida del vano.", " mm"),
        ("=", "{F} ¿Cuántos mm de holgura tiene P5?", "800-795", "Se resta la medida de la hoja de la medida del vano.", " mm"),
        ("abc", "{F} ¿Qué elementos quedan fuera del criterio de 5 a 9 mm?", "P2 y P3", "P1 y P4", "P4 y P5", "P2 tiene 3 mm, menos que 5, y P3 tiene 10 mm, más que 9."),
        ("=", "{F} ¿Cuántos elementos cumplen el criterio?", "5-2", "Se restan los elementos fuera del criterio del total registrado.", " elementos"),
        ("abc", "{F} ¿Qué se hace con P3 según la ficha?", "Se separa y se informa al jefe de obra", "Se instala igual porque la diferencia es de 1 mm", "Se corrige por cuenta propia", "Una holgura sobre el máximo se separa y se informa."),
        ("ab", "{F} Un compañero dice: «P5 tiene 5 mm, justo el mínimo, así que se rechaza». ¿Qué respuesta es correcta?", "No: el criterio incluye el valor mínimo y se acepta", "Sí: lo justo se rechaza siempre", "La ficha dice que ambos extremos están incluidos."),
        ("abc", "{F} Una estudiante dice: «ya sé qué elementos cumplen, puedo ajustar el vano con herramientas». ¿Qué respuesta es correcta?", "No: ajustar exige instructor autorizado y norma vigente", "Sí: saber qué cumple habilita para ajustar", "Sí, con EPP", "Una lectura de registros no habilita para trabajar con herramientas."),
        ("abc", "{F} Si la mayoría de los vanos de una obra salen con holgura insuficiente, ¿qué corresponde?", "Informar para revisar si el error está en los vanos o en las hojas", "Corregir cada hoja sin avisar", "Aceptarlos para no atrasar", "Un problema repetido tiene una causa común que debe revisarse."),
    ],
    ctx=("abc", "En la obra de ejemplo, una hoja pesada se resbala y atrapa el pie de un instalador. ¿Qué se hace según las reglas generales?", "No mover la hoja sin ayuda, avisar a un adulto responsable y a emergencias", "Tirar de la hoja con fuerza para liberarlo", "Esperar sin avisar si no hay sangre", "Una lesión por atrapamiento se informa a quien corresponde y a emergencias."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿Cómo se calcula la holgura?", "Vano menos hoja", "Es el espacio que queda entre ambos."),
        ("En Muebles y Terminaciones en Madera: ¿qué se hace con un elemento fuera del criterio?", "Se separa y se informa al jefe de obra", "No se instala por cuenta propia."),
        ("¿Por qué un criterio incluye un mínimo y un máximo?", "Porque una holgura demasiado pequeña o demasiado grande es un problema", "Un espacio muy pequeño o muy grande puede causar fallas."),
    ],
    op=("Registro de ejemplo «Casa Quillay» (ficticia): criterio de ejemplo de holgura total de 4 a 8 mm. Medidas en mm (vano y hoja): Q1: 800 y 794; Q2: 850 y 841; Q3: 900 y 898; Q4: 750 y 744. Escribe (a) la holgura de cada elemento, (b) cuáles cumplen el criterio, (c) cuántos no cumplen y (d) qué haces con los que no cumplen.",
        "(a) Q1: 6; Q2: 9; Q3: 2; Q4: 6. (b) Cumplen Q1 y Q4. (c) No cumplen 2. (d) Los separo y aviso al jefe de obra.",
        ["calcula las cuatro holguras", "identifica los que cumplen", "cuenta los que no cumplen", "informa al jefe de obra"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "no incluir los extremos", "corregir por cuenta propia"],
        "Pregunta: «¿qué se resta de qué?». Si no responde, pídele que relea la definición de holgura."),
    reinforce="Calcula la holgura de un vano de 1.000 mm con una hoja de 992 mm.",
    extend="Explica por qué una holgura demasiado grande también es un problema de calidad.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 9 (planificación de una instalación de ejemplo, inventada). Obra ficticia con 20 puertas. Cada puerta lleva 3 bisagras y cada bisagra 6 tornillos. Merma de ejemplo de 10 % sobre las bisagras. "
     "Los tornillos se venden en cajas de 50. Rendimiento de ejemplo de la cuadrilla: 4 puertas por jornada. Al final se firma el acta de entrega, que lista 60 ítems de revisión; el inspector técnico anota 15 pendientes.")
build(
    O8, 4, F,
    use="Aprenderé a calcular en papel los herrajes y las jornadas de una instalación y a leer un acta de entrega con pendientes.",
    prior=["Sé qué es la quincallería.", "Sé calcular un porcentaje sencillo.", "Sé dividir con resto."],
    explain=[
        "Planificar una instalación en papel combina tres cálculos. Primero, los herrajes: se multiplican las puertas por las bisagras de cada una y se suma la merma, que cubre piezas dañadas o perdidas. Segundo, las fijaciones: se multiplican las bisagras por los tornillos de cada una y se pasa a cajas dividiendo por lo que trae cada caja, redondeando hacia arriba. Tercero, el tiempo: se dividen las puertas por las que la cuadrilla instala por jornada, también redondeando hacia arriba.",
        "El acta de entrega lista los ítems revisados y los pendientes, que son lo que aún no cumple o no está terminado. El porcentaje de pendientes se calcula multiplicando los pendientes por 100 y dividiendo por el total de ítems. Los pendientes se registran con fecha y responsable y se resuelven antes de la entrega definitiva. Todos los números de esta clase son de ejemplo y el trabajo real lo hace personal autorizado.",
        TAIL,
    ],
    vocab=[("merma", "cantidad extra que cubre piezas dañadas o perdidas"), ("caja de fijaciones", "envase que trae una cantidad fija de tornillos"), ("jornada", "día de trabajo"), ("pendiente", "ítem que aún no cumple o no está terminado"), ("entrega definitiva", "momento en que el cliente recibe la obra sin pendientes")],
    worked=[
        ("Herrajes con merma", "Una obra de ejemplo necesita 40 bisagras y la merma es de 10 %. ¿Cuántas se compran?", ["El 10 % de 40 es 4.", "40 más 4 son 44."], "44 bisagras"),
        ("Jornadas", "Una cuadrilla de ejemplo instala 5 elementos por jornada y hay 12. ¿Cuántas jornadas se necesitan?", ["12 dividido en 5 da 2 y sobran 2.", "Se redondea hacia arriba."], "3 jornadas"),
    ],
    mistakes=[("Olvidar la merma al comprar herrajes.", "Una pieza dañada o perdida deja la obra sin herraje.", "Se suma un porcentaje de merma a la cantidad calculada."),
              ("Dar por entregada una obra con pendientes.", "El cliente recibe algo incompleto.", "Los pendientes se registran y se resuelven antes de la entrega definitiva.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es un pendiente en el acta de entrega?", "Un ítem que aún no cumple o no está terminado", "Un ítem aprobado por el cliente", "Una medida de seguridad", "Los pendientes son lo que falta resolver."),
        ("abc", "¿Para qué se suma una merma a los herrajes?", "Para cubrir piezas dañadas o perdidas", "Para pagar menos al proveedor", "Para que la puerta sea más pesada", "La merma evita quedarse sin herrajes."),
        ("=", "{F} ¿Cuántas bisagras se necesitan para las 20 puertas sin merma?", "20*3", "Se multiplican las puertas por las bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuántas bisagras hay que comprar con la merma de 10 % (60 bisagras)?", "60*110//100", "Se calcula el 110 % de las bisagras: el total más la merma de 10 %.", " bisagras"),
        ("=", "{F} ¿Cuántos tornillos se necesitan para 66 bisagras?", "66*6", "Se multiplican las bisagras por los tornillos de cada una.", " tornillos"),
        ("=", "{F} ¿Cuántas cajas de 50 tornillos se necesitan para 396 tornillos, redondeando hacia arriba?", "(396+49)//50", "Se divide 396 en 50 y se redondea hacia arriba porque sobra una parte.", " cajas"),
        ("=", "{F} ¿Cuántas jornadas necesita la cuadrilla para instalar las 20 puertas?", "20//4", "Se dividen las puertas entre las que se instalan por jornada.", " jornadas"),
        ("=", "{F} Si una jornada se pierde por lluvia, ¿cuántas jornadas se necesitan en total?", "20//4+1", "Se suma la jornada perdida a las cinco jornadas planificadas.", " jornadas"),
        ("=", "{F} ¿Qué porcentaje de los 60 ítems del acta son pendientes (15 pendientes)?", "15*100//60", "Se multiplican los pendientes por 100 y se divide por el total de ítems.", " %"),
        ("=", "{F} ¿Cuántos ítems del acta no tienen pendiente?", "60-15", "Se restan los pendientes del total de ítems.", " ítems"),
        ("abc", "{F} ¿Qué se hace con los pendientes del acta?", "Se registran con fecha y responsable y se resuelven antes de la entrega definitiva", "Se ignoran porque son pocos", "Se tachan para que el acta quede limpia", "Los pendientes se resuelven y no se ocultan."),
        ("ab", "{F} Un compañero dice: «compramos exactamente 60 bisagras y no importa la merma». ¿Qué respuesta es correcta?", "No: conviene sumar la merma de 10 % por piezas dañadas o perdidas", "Sí: la merma nunca se usa", "La ficha incluye una merma de ejemplo del 10 %."),
        ("abc", "{F} Una estudiante dice: «ya planifico la instalación, puedo instalar las puertas». ¿Qué respuesta es correcta?", "No: instalar exige instructor autorizado y norma vigente", "Sí: planificar habilita para instalar", "Sí, con casco", "Planificar en papel no habilita para trabajar en obra."),
    ],
    ctx=("abc", "En la obra de ejemplo, para recuperar una jornada perdida, el jefe pide trabajar en altura sin el personal autorizado ni la zona delimitada. ¿Qué respuesta es correcta?", "No: se informa la demora y se mantienen las medidas de seguridad", "Sí: recuperar el plazo es más importante", "Sí, si todos usan casco", "El plazo no justifica saltarse las medidas; se renegocia."),
    sc=[
        ("¿Qué se hace con el resto al calcular cajas de tornillos?", "Se compra una caja más", "Una caja incompleta igual se compra entera."),
        ("En Muebles y Terminaciones en Madera: ¿qué es una merma?", "Una cantidad extra que cubre piezas dañadas o perdidas", "Se suma a la cantidad calculada."),
        ("¿Cuándo se hace la entrega definitiva?", "Cuando se resolvieron los pendientes", "El cliente recibe la obra sin pendientes."),
    ],
    op=("Planificación de ejemplo «Casa Ñire» (ficticia): 15 puertas; 3 bisagras por puerta; 4 tornillos por bisagra; merma de ejemplo de 20 % sobre las bisagras; cajas de 25 tornillos; la cuadrilla instala 3 puertas por jornada. Escribe (a) las bisagras con la merma, (b) los tornillos necesarios para esas bisagras, (c) las cajas necesarias y (d) las jornadas.",
        "(a) 15×3 son 45 bisagras y con 20 % son 54. (b) 54×4 son 216 tornillos. (c) 216÷25 da 8 y sobran 16: 9 cajas. (d) 15÷3 son 5 jornadas.",
        ["calcula las bisagras con merma", "calcula los tornillos", "calcula las cajas con redondeo", "calcula las jornadas"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la merma", "redondear hacia abajo", "olvidar los tornillos por bisagra"],
        "Pregunta: «¿por qué se redondea hacia arriba?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula las cajas de 40 tornillos que se necesitan para 250 tornillos.",
    extend="Explica por qué el acta de entrega protege tanto al cliente como al taller.",
)

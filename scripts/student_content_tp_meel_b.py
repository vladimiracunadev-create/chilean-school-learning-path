"""Mecánica Industrial, mención Mantenimiento Electromecánico, 4.º medio: OAM-04 (reponer o reparar partes y piezas: documentos, criterios y costos) y OAM-05 (puesta en funcionamiento: protocolos, tablas de tolerancia y verificación documental). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meel_common import AVISO, EMER, build

O4 = "TP-MEEL-4-OAM-04"
O5 = "TP-MEEL-4-OAM-05"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Un reductor ficticio R-5, caja que baja la velocidad del giro de un motor, tiene estos componentes: carcasa, eje de entrada, eje de salida, engranajes, dos rodamientos, un sello y aceite. "
     "Lleva 20.000 horas de operación; la vida útil de ejemplo del fabricante para el rodamiento es de 25.000 horas y para el sello, 15.000 horas. Síntomas anotados: fuga de aceite por el sello, ruido en un rodamiento y calentamiento. "
     "Peligros anotados: piezas pesadas, energía almacenada, superficies calientes, aceite derramado y ruido.")
build(
    O4, 1, F,
    use="Aprenderé qué es la vida útil, el desgaste y el deterioro de una pieza, cuándo se repone o se repara según el manual y qué riesgos y residuos tiene esa decisión.",
    prior=["Sé qué es el mantenimiento preventivo y el correctivo.", "Sé qué es energía almacenada.", "Sé restar números enteros."],
    explain=[
        "La vida útil es el tiempo de uso durante el cual una pieza cumple su función según el fabricante. El desgaste es la pérdida gradual de material por roce, y el deterioro es el daño por otras causas, como la corrosión o la fatiga. Cuando una pieza cumplió su vida útil o se desgastó más allá del límite admisible, se repone, es decir, se cambia por otra nueva; si el manual lo permite, a veces se repara, es decir, se recupera su función.",
        "La decisión de reponer o reparar se apoya en el manual del fabricante, en las mediciones y en la bitácora. Intervenir un equipo tiene riesgos: piezas pesadas, energía almacenada, calor, aceite y ruido. Las piezas retiradas, los aceites y los trapos con aceite son residuos que se llevan a los puntos de acopio según la norma vigente; nunca van al desagüe ni a la basura común.",
        f"Este cuaderno no enseña a desarmar ni a reemplazar piezas. {EMER} {AVISO}",
    ],
    vocab=[("vida útil", "tiempo durante el cual una pieza cumple su función según el fabricante"), ("desgaste", "pérdida gradual de material por roce"), ("deterioro", "daño por otras causas, como corrosión o fatiga"), ("reponer", "cambiar una pieza por otra nueva"), ("reparar", "recuperar la función de una pieza sin cambiarla"), ("residuo", "material que se deja de usar y debe gestionarse según la norma")],
    worked=[
        ("Vida útil restante", "Una pieza de ejemplo tiene vida útil de 10.000 horas y lleva 7.000. ¿Cuántas horas de vida útil le quedan?", ["Se resta lo usado a la vida útil.", "10.000 menos 7.000 son 3.000."], "3.000 horas"),
        ("Desgaste o deterioro", "Un eje de ejemplo pierde material por el roce continuo con un casquillo. ¿Es desgaste o deterioro por corrosión?", ["La pérdida gradual por roce es desgaste.", "La corrosión es otro tipo de daño."], "Desgaste"),
    ],
    mistakes=[("Seguir usando una pieza que cumplió su vida útil porque todavía funciona.", "Puede fallar sin aviso y causar un daño mayor.", "Planifica la reposición según el manual y la bitácora."),
              ("Botar el aceite y las piezas con aceite a la basura común.", "Son residuos que requieren gestión.", "Llévalos al punto de acopio según la norma vigente.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la vida útil de una pieza?", "El tiempo de uso durante el cual cumple su función según el fabricante", "El tiempo que tarda en llegar desde la fábrica", "El número de personas que la usan", "La vida útil la fija el fabricante."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el desgaste?", "La pérdida gradual de material por roce", "La rotura repentina de una pieza por un golpe", "El cambio de color de una pieza", "El desgaste ocurre poco a poco por el roce."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué significa reponer una pieza?", "Cambiarla por otra nueva", "Recuperar su función sin cambiarla", "Guardarla en la bodega", "Reponer es sustituir; reparar es recuperar."),
        ("=", "{F} ¿Cuántas horas de vida útil le quedan al rodamiento según el fabricante?", "25000-20000", "Se resta lo usado a la vida útil del rodamiento.", " horas"),
        ("=", "{F} ¿Cuántas horas se pasó el sello de su vida útil?", "20000-15000", "Se resta la vida útil del sello a las horas de operación.", " horas"),
        ("abc", "{F} ¿Cuál de las piezas de la ficha ya superó su vida útil?", "El sello", "El rodamiento", "Ninguna", "El sello tiene vida útil de 15.000 horas y el reductor lleva 20.000."),
        ("=", "{F} Una planta tiene 4 reductores iguales y cada uno requiere cambiar el sello. ¿Cuántos sellos se necesitan?", "4*1", "Cada reductor lleva un sello.", " sellos"),
        ("=", "{F} Cada reductor tiene 2 rodamientos. ¿Cuántos rodamientos requieren 3 reductores iguales?", "3*2", "Se multiplican los reductores por los rodamientos de cada uno.", " rodamientos"),
        ("abc", "{F} El aceite del reductor se retira usado. ¿Qué corresponde con él?", "Almacenarlo en un recipiente rotulado hasta su retiro según la norma vigente", "Verterlo al desagüe", "Mezclarlo con el aceite nuevo", "El aceite usado es un residuo que se gestiona."),
        ("abc", "{F} Un practicante dice: «el sello gotea, pero el reductor sigue andando; lo cambio yo mañana». ¿Qué respuesta es correcta?", "No corresponde: la reposición la planifica y ejecuta personal autorizado con el manual, y la fuga se informa", "Corresponde, porque el cambio es fácil", "Corresponde, si lo hace con el equipo en marcha", "Reemplazar piezas exige autorización, y la fuga debe informarse."),
        ("abc", "En una visita a una planta de ejemplo, una persona queda atrapada entre un reductor y una estructura. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar mover el reductor", "Tirar de la persona para sacarla", "Intervenir sin formación puede agravar la lesión."),
        ("=", "{F} El rodamiento del reductor tiene un costo de ejemplo de $45.000 y el sello, $12.000. ¿Cuánto cuestan ambos repuestos?", "45000+12000", "Se suman los precios de los dos repuestos.", " pesos de ejemplo"),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿cuál es un ejemplo de deterioro y no de desgaste?", "La corrosión de una pieza expuesta a humedad", "La pérdida de material por el roce de un eje", "El uso gradual de un casquillo", "La corrosión es un daño distinto del roce."),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «el sello pasó su vida útil, pero mientras no se rompa seguimos». ¿Qué propones?", "Planificar su reposición según el manual, porque una falla repentina puede dañar el equipo", "Esperar a que se rompa", "Tapar la fuga con un trapo", "La vida útil se respeta para evitar fallas mayores."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuánto vida útil queda si lleva 7.000 de 10.000?", "3.000 horas", "Se resta lo usado a la vida útil."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué es un residuo?", "Material que se deja de usar y debe gestionarse según la norma", "Un residuo no se bota sin gestionarlo según la norma."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién ejecuta la reposición de una pieza?", "Personal autorizado con el manual del fabricante", "Este cuaderno no habilita para intervenir."),
    ],
    op=("Ficha de ejemplo: una bomba ficticia lleva 9.000 horas. Vida útil de ejemplo: sello, 8.000 horas; rodamiento, 12.000 horas. Síntoma: fuga por el sello. Peligros: piezas pesadas, aceite derramado y energía almacenada. Escribe (a) cuántas horas le quedan al rodamiento, (b) cuántas horas se pasó el sello, (c) un control administrativo para la intervención, (d) qué haces con el aceite retirado. No describas cómo se cambia.",
        "(a) 12.000 − 9.000 = 3.000 horas. (b) 9.000 − 8.000 = 1.000 horas. (c) Una orden de trabajo y un permiso, con acceso solo a personal autorizado. (d) Almacenarlo en un recipiente rotulado hasta su retiro, según la norma vigente.",
        ["calcula las horas del rodamiento", "calcula el exceso del sello", "propone un control administrativo", "indica el manejo del aceite"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de restar", "verter el aceite al desagüe", "describir cómo se cambia"],
        "Pregunta: «¿qué se resta a qué?». Si duda, pídele que relea la definición de vida útil."),
    reinforce="Escribe dos piezas con su vida útil inventada y calcula cuánta vida útil queda a un equipo con unas horas de operación inventadas.",
    extend="Explica con un ejemplo por qué una pieza que todavía funciona puede estar fuera de su vida útil.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (extracto de un manual del fabricante, descrito por escrito, de ejemplo e inventado, del reductor ficticio R-5). Despiece: posición 1, tapa (código T-100, 1 unidad); posición 2, sello (código S-210, 1 unidad); posición 3, rodamiento (código R-306, 2 unidades); "
     "posición 4, eje de salida (código E-410, 1 unidad); posición 5, pernos de la tapa (código P-512, 8 unidades). Tabla de reemplazo del fabricante de ejemplo: sello, cambiar a las 15.000 horas; rodamiento, a las 25.000 horas; pernos de la tapa, cada vez que se abra la tapa. "
     "Advertencia del manual: «solo personal autorizado; usar repuestos con el código indicado». Una orden de trabajo registra la pieza, el código, la cantidad, quién la hizo y la fecha.")
build(
    O4, 2, F,
    use="Aprenderé a leer un despiece y una tabla de reemplazo, a usar códigos de repuesto y a conocer los roles y documentos de una reposición.",
    prior=["Sé qué es una orden de trabajo.", "Sé qué es la vida útil.", "Sé multiplicar enteros."],
    explain=[
        "El despiece de un manual muestra las piezas de un equipo separadas, cada una con una posición, un código de repuesto y una cantidad. El código identifica exactamente la pieza que se debe comprar; una pieza con un código distinto no es necesariamente intercambiable. La tabla de reemplazo del fabricante indica cuándo cambiar cada pieza. La solicitud de repuesto pide al almacén las piezas con su código y cantidad.",
        "La orden de trabajo registra la reposición: la pieza, el código, la cantidad, quién la hizo y la fecha; y la hoja de vida del equipo guarda el historial. El planificador programa, el bodeguero entrega los repuestos, el técnico autorizado ejecuta y el supervisor aprueba. Las piezas retiradas se gestionan como residuos según la norma vigente.",
        f"Aquí solo se leen documentos. {EMER} {AVISO}",
    ],
    vocab=[("despiece", "dibujo o lista de las piezas de un equipo por separado"), ("posición", "número que identifica una pieza en el despiece"), ("código de repuesto", "identificador exacto de una pieza comprable"), ("tabla de reemplazo", "lista del fabricante con el momento de cambiar cada pieza"), ("solicitud de repuesto", "documento que pide al almacén piezas con su código y cantidad"), ("bodeguero", "persona que entrega y registra los repuestos")],
    worked=[
        ("Leer un código", "Un despiece de ejemplo dice: «posición 7, filtro, código F-901, 2 unidades». ¿Qué código se pide?", ["Cada pieza tiene su propio código.", "El código es F-901."], "F-901"),
        ("Sumar unidades", "Un despiece de ejemplo anota 2 sellos y 6 pernos. ¿Cuántas piezas suma?", ["Se suman las cantidades.", "2 más 6 son 8."], "8 piezas"),
    ],
    mistakes=[("Comprar un repuesto «parecido» con otro código.", "Puede no ser intercambiable y causar una falla.", "Pide el código indicado por el manual."),
              ("Cambiar una pieza sin registrar la orden de trabajo.", "Se pierde el historial del equipo.", "Toda reposición se registra con pieza, código, cantidad, responsable y fecha.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el código de repuesto?", "El identificador exacto de una pieza comprable", "El número de serie del motor", "La fecha en que se compró la pieza", "El código distingue una pieza de otra."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un despiece?", "Una lista o dibujo de las piezas de un equipo por separado", "El plan anual de mantenimiento", "El certificado de calibración", "El despiece muestra las piezas con sus códigos."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué registra una orden de trabajo de reposición?", "La pieza, el código, la cantidad, quién la hizo y la fecha", "Solo el nombre del técnico", "El precio de venta del equipo", "El registro permite revisar lo hecho."),
        ("abc", "{F} ¿Qué código tiene el rodamiento en el despiece?", "R-306", "S-210", "E-410", "La ficha asigna R-306 al rodamiento."),
        ("=", "{F} ¿Cuántas piezas suma el despiece, contando todas las unidades?", "1+1+2+1+8", "Se suman las cantidades de las cinco posiciones.", " piezas"),
        ("abc", "{F} Según la tabla de reemplazo, ¿cuándo se cambian los pernos de la tapa?", "Cada vez que se abra la tapa", "A las 25.000 horas", "A las 15.000 horas", "La tabla indica cambio con cada apertura de la tapa."),
        ("=", "{F} Una planta tiene 5 reductores iguales y se cambian los pernos de la tapa en todos. ¿Cuántos pernos se necesitan?", "5*8", "Se multiplican los reductores por los pernos de cada uno.", " pernos"),
        ("=", "{F} Se cambian los rodamientos de 3 reductores iguales. ¿Cuántos rodamientos se solicitan?", "3*2", "Se multiplican los reductores por los rodamientos de cada uno.", " rodamientos"),
        ("abc", "{F} Un reductor lleva 14.000 horas. ¿Qué pieza de la tabla de reemplazo está más cerca de su cambio?", "El sello, que se cambia a las 15.000 horas", "El rodamiento, que se cambia a las 25.000 horas", "El eje, que no figura en la tabla", "Al sello le faltan 1.000 horas."),
        ("abc", "{F} El almacén ofrece un rodamiento «equivalente» con otro código. ¿Qué corresponde?", "Consultar al fabricante o al proyectista antes de usarlo, porque podría no ser intercambiable", "Usarlo, porque se parece", "Usarlo, si es más barato", "El manual exige el código indicado."),
        ("abc", "{F} Un técnico dice: «cambié el sello pero no anoté nada, total está cambiado». ¿Qué observación es correcta?", "Debe registrarlo en la orden de trabajo y en la hoja de vida para mantener el historial", "Está bien, porque el cambio ya está hecho", "Está bien, si lo recuerda", "Sin registro no se puede planificar la próxima reposición."),
        ("=", "{F} El código del sello es S-210. Si 4 reductores cambian el sello de a 1, ¿cuántos sellos con ese código hay que solicitar?", "4*1", "Cada reductor usa un sello.", " sellos"),
        ("Un manual de ejemplo anota el código F-901 para un filtro y F-910 para otro. ¿Pueden usarse indistintamente sin consultar?", "No", "Los códigos distintos indican piezas distintas que podrían no ser intercambiables."),
    ],
    ctx=("abc", "El bodeguero de ejemplo entrega un repuesto con un código distinto «porque es el último que queda». ¿Qué propones?", "No usarlo hasta consultar al planificador y al fabricante si es intercambiable", "Usarlo porque es lo que hay", "Limar la pieza hasta que calce", "Un repuesto con otro código puede no calzar ni cumplir."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué identifica exactamente una pieza comprable?", "Su código de repuesto", "El código evita comprar piezas equivocadas."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué hace la solicitud de repuesto?", "Pide al almacén piezas con su código y cantidad", "Organiza la entrega de repuestos desde la bodega."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿dónde se guarda el historial de reposiciones?", "En la hoja de vida del equipo", "El historial permite planificar la próxima reposición."),
    ],
    op=("Ficha de ejemplo: despiece de una bomba ficticia: posición 1, sello, código S-300, 1 unidad; posición 2, rodamiento, código R-410, 2 unidades; posición 3, pernos, código P-520, 6 unidades. Tabla de reemplazo: sello, 6.000 horas; rodamiento, 18.000 horas. Se reponen sello y rodamientos en 4 bombas iguales. Escribe (a) cuántas piezas suma el despiece, (b) cuántos rodamientos se solicitan, (c) qué código pides para el sello, (d) qué registras en la orden de trabajo.",
        "(a) 1 + 2 + 6 = 9 piezas. (b) 4 × 2 = 8 rodamientos. (c) S-300. (d) La pieza, el código, la cantidad, quién la cambió y la fecha.",
        ["suma las piezas", "calcula los rodamientos", "nombra el código", "lista los datos de la orden"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por las bombas", "confundir códigos", "no registrar la orden"],
        "Pregunta: «¿qué código tiene el sello?». Si duda, pídele que relea el despiece."),
    reinforce="Inventa un despiece de tres piezas con código y cantidad y calcula las piezas necesarias para dos equipos.",
    extend="Explica con un ejemplo por qué un repuesto con otro código puede causar una falla.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (informe de medición de ejemplo, inventado; las mediciones las tomó personal autorizado). Eje de salida del reductor R-5: diámetro nuevo 40.000 µm; mínimo admisible según el manual 39.950 µm; medido 39.940 µm. "
     "Rodamiento: juego medido 80 µm; juego máximo admisible 100 µm. Sello: con fuga visible; no es reparable según el manual. Carcasa: sin grietas. Criterio del fabricante de ejemplo: si una medida está fuera del límite admisible, la pieza se repone; "
     "si está dentro, se mantiene en servicio y se reevalúa en la próxima pauta. Costos de ejemplo: eje nuevo, $120.000; reparar el eje (recuperarlo), $50.000, pero el manual no permite reparar un eje bajo el mínimo admisible.")
build(
    O4, 3, F,
    use="Aprenderé a decidir en papel si una pieza se repone, se repara o se mantiene, comparando mediciones con límites admisibles y criterios del manual.",
    prior=["Sé qué es el desgaste y la vida útil.", "Sé comparar un valor con un límite.", "Sé restar números enteros."],
    explain=[
        "El límite admisible es la medida máxima de desgaste que el fabricante permite. Un eje cuyo diámetro baja del mínimo admisible, o un rodamiento cuyo juego supera el máximo, ya no cumple y se repone. Una pieza dentro de los límites se mantiene en servicio y se reevalúa en la próxima pauta. Un sello con fuga que el manual declara no reparable también se repone.",
        "El manual puede prohibir reparar una pieza, aunque la reparación sea más barata. Cuando una pieza no es reparable, el costo de la reparación no se considera. Las mediciones las toma personal autorizado y las decisiones quedan registradas. Las piezas retiradas son residuos que se gestionan según la norma vigente.",
        f"Es un análisis de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("límite admisible", "valor máximo de desgaste que el fabricante permite"), ("mínimo admisible", "diámetro más pequeño que se acepta en un eje"), ("juego", "espacio entre las partes de un rodamiento"), ("reevaluar", "volver a medir y decidir más adelante"), ("no reparable", "pieza que según el manual solo puede reponerse")],
    worked=[
        ("Dentro del límite", "Un eje de ejemplo tiene mínimo admisible de 29.980 µm y mide 29.990 µm. ¿Se repone?", ["29.990 es mayor que 29.980.", "Está dentro del límite y se mantiene."], "No, se mantiene"),
        ("Fuera del límite", "Un rodamiento de ejemplo tiene juego máximo admisible de 60 µm y mide 75 µm. ¿Qué corresponde?", ["75 supera el máximo de 60.", "La pieza se repone."], "Reponerlo"),
    ],
    mistakes=[("Reparar una pieza que el manual declara no reparable porque cuesta menos.", "El manual manda y una reparación no autorizada puede causar una falla.", "Si el manual no permite reparar, se repone."),
              ("Decidir sin comparar la medida con el límite del manual.", "Sin comparación la decisión es una opinión.", "Compara siempre cada medida con su límite.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el límite admisible?", "El valor máximo de desgaste que el fabricante permite", "El valor de la pieza cuando es nueva", "El precio máximo de un repuesto", "El límite admisible marca hasta dónde se acepta el desgaste."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué significa que una pieza sea no reparable?", "Que según el manual solo puede reponerse", "Que cuesta mucho repararla", "Que ya fue reparada una vez", "No reparable significa que el manual no lo permite."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es reevaluar una pieza que está dentro del límite?", "Volver a medirla y decidir en la próxima pauta", "Cambiarla de inmediato", "Ignorarla hasta que falle", "Reevaluar es controlar cómo evoluciona la pieza."),
        ("=", "{F} ¿Cuántos µm bajo el mínimo admisible está el diámetro medido del eje?", "39950-39940", "Se resta el diámetro medido al mínimo admisible.", " µm"),
        ("=", "{F} ¿Cuántos µm de desgaste tiene el eje respecto de su diámetro nuevo?", "40000-39940", "Se resta el diámetro medido al nuevo.", " µm"),
        ("abc", "{F} ¿Qué corresponde con el eje de salida según el criterio del fabricante?", "Reponerlo, porque su diámetro está bajo el mínimo admisible", "Mantenerlo en servicio", "Repararlo, porque cuesta menos", "El diámetro medido es menor que el mínimo admisible."),
        ("abc", "{F} ¿Qué corresponde con el rodamiento?", "Mantenerlo en servicio y reevaluarlo, porque su juego está bajo el máximo admisible", "Reponerlo, porque tiene juego", "Repararlo, porque el juego es positivo", "80 µm es menor que el máximo de 100 µm."),
        ("=", "{F} ¿Cuántos µm le quedan de margen al juego del rodamiento antes de llegar al máximo admisible?", "100-80", "Se resta el juego medido al máximo admisible.", " µm"),
        ("abc", "{F} ¿Qué corresponde con el sello?", "Reponerlo, porque tiene fuga y no es reparable", "Repararlo, porque cuesta menos", "Mantenerlo en servicio, porque la fuga es visible solo a veces", "El manual declara que el sello no es reparable."),
        ("abc", "{F} Un jefe dice: «reparemos el eje por $50.000 en vez de reponerlo por $120.000, ahorramos $70.000». ¿Qué respuesta es correcta?", "No corresponde: el manual no permite reparar un eje bajo el mínimo admisible", "Corresponde, porque ahorra dinero", "Corresponde, si el eje se ve bien", "El criterio del fabricante prevalece sobre el costo."),
        ("abc", "{F} Un practicante propone medir el eje con el reductor en marcha para ahorrar tiempo. ¿Qué respuesta es correcta?", "No corresponde: la medición la hace personal autorizado con el equipo detenido y asegurado", "Corresponde, si lleva guantes", "Corresponde, si el reductor gira despacio", "Medir en un equipo en movimiento es peligroso."),
        ("=", "{F} Se decide reponer el eje y el sello. El sello cuesta $12.000. ¿Cuánto cuestan ambos repuestos?", "120000+12000", "Se suman los precios del eje y del sello.", " pesos de ejemplo"),
        ("Un eje de ejemplo tiene mínimo admisible de 24.970 µm y se mide 24.965 µm. ¿Se repone o se mantiene?", "Se repone", "24.965 es menor que el mínimo de 24.970."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «el eje solo está 10 µm bajo el mínimo, dejémoslo así». ¿Qué propones?", "Reponerlo según el criterio del manual, porque está fuera del límite admisible", "Dejarlo porque la diferencia es pequeña", "Pulirlo para que parezca nuevo", "Un valor fuera del límite no cumple, por pequeña que sea la diferencia."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace con una pieza bajo su mínimo admisible?", "Se repone", "Ya no cumple el límite del fabricante."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué manda sobre el costo al decidir reparar?", "El criterio del manual del fabricante", "Si el manual prohíbe reparar, se repone."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién mide las piezas?", "Personal autorizado", "La medición exige formación y autorización."),
    ],
    op=("Ficha de ejemplo: un eje ficticio de 30.000 µm nuevo tiene mínimo admisible 29.960 µm y se mide 29.955 µm. Un rodamiento tiene juego medido de 40 µm y máximo admisible de 50 µm. El manual no permite reparar el eje. Costo del eje nuevo: $90.000; reparación: $30.000. Escribe (a) cuánto está el eje bajo el mínimo, (b) qué corresponde con el eje y por qué, (c) qué corresponde con el rodamiento, (d) por qué no conviene la reparación del eje.",
        "(a) 29.960 − 29.955 = 5 µm. (b) Reponerlo, porque está bajo el mínimo admisible. (c) Mantenerlo y reevaluarlo en la próxima pauta, porque 40 µm es menor que 50 µm. (d) Porque el manual no permite reparar un eje bajo el mínimo admisible, aunque cueste menos.",
        ["calcula la diferencia", "decide sobre el eje con razón", "decide sobre el rodamiento", "explica el criterio del manual"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "decidir por el costo", "ignorar el límite"],
        "Pregunta: «¿el valor medido está dentro o fuera del límite?». Si duda, pídele que compare ambos números."),
    reinforce="Inventa un límite admisible y una medida y decide si se repone o se mantiene.",
    extend="Explica con un ejemplo por qué el criterio del manual prevalece sobre el costo de la reparación.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (costos y stock de ejemplo, inventados). Planta con 6 reductores iguales. Rodamientos por reductor: 2; precio de ejemplo de un rodamiento: $45.000; vida útil de ejemplo: 25.000 horas; cada reductor opera 5.000 horas al año. "
     "Costo de una parada no programada: $200.000; costo de una parada programada: $40.000. Stock de seguridad de ejemplo: se mantienen en bodega 2 rodamientos de repuesto además de los que se usarán en el año. En bodega hay 5 rodamientos. "
     "Regla de ejemplo del taller: se repara si el costo de reparar es menor o igual a la mitad del costo del repuesto nuevo y el manual lo permite.")
build(
    O4, 4, F,
    use="Aprenderé a calcular cuántos repuestos se necesitan por año, el stock de seguridad, el costo de paradas y a aplicar una regla de reparar o reponer, con datos de ejemplo.",
    prior=["Sé multiplicar, dividir y restar enteros.", "Sé qué es la vida útil.", "Sé comparar costos."],
    explain=[
        "Los repuestos se planifican con la vida útil y las horas de operación. Dividir las horas de vida útil entre las horas de operación al año da cuántos años dura la pieza; los repuestos del año se obtienen multiplicando las piezas por equipo por los equipos y por la fracción de vida que se consume. Con enteros, si una pieza dura 5 años, en un año se cambia un quinto de las piezas.",
        "El stock de seguridad es una cantidad extra en bodega para no detener la planta si una pieza falla antes de lo previsto. Una parada programada cuesta menos que una no programada. La regla de reparar o reponer compara el costo de reparar con el de un repuesto nuevo, siempre que el manual permita reparar.",
        f"Es un cálculo de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("stock de seguridad", "cantidad extra en bodega para evitar detener la planta"), ("parada programada", "detención planificada con anticipación"), ("parada no programada", "detención por una falla inesperada"), ("regla de reparar o reponer", "criterio que compara el costo de reparar con el de un repuesto nuevo"), ("faltante", "cantidad que falta para cubrir la necesidad")],
    worked=[
        ("Años de duración", "Una pieza de ejemplo dura 20.000 horas y el equipo opera 4.000 horas al año. ¿Cuántos años dura?", ["Se divide la vida útil entre las horas por año.", "20.000 dividido en 4.000 son 5."], "5 años"),
        ("Regla de reparar", "Un repuesto nuevo de ejemplo cuesta $80.000 y reparar cuesta $35.000. La regla pide que la reparación cueste la mitad o menos. ¿Se repara?", ["La mitad de 80.000 es 40.000.", "35.000 es menor que 40.000, así que se repara si el manual lo permite."], "Sí, si el manual lo permite"),
    ],
    mistakes=[("Calcular los repuestos sin considerar el stock de seguridad.", "Una falla anticipada puede detener la planta.", "Suma el stock de seguridad a los repuestos del año."),
              ("Aplicar la regla de reparar sin consultar el manual.", "El manual puede prohibir reparar.", "Primero verifica si el manual lo permite.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿para qué sirve el stock de seguridad?", "Para no detener la planta si una pieza falla antes de lo previsto", "Para vender repuestos extra", "Para reducir el costo del repuesto", "Es una reserva extra de repuestos."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una parada no programada?", "Una detención por una falla inesperada", "Una detención planificada con anticipación", "Una parada solo para limpieza", "No programada significa imprevista y sin planificación."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un faltante?", "La cantidad que falta para cubrir la necesidad", "La cantidad que sobra en bodega", "El precio de un repuesto", "El faltante es lo que no alcanza a cubrirse."),
        ("=", "{F} ¿Cuántos años dura un rodamiento, con 25.000 horas de vida útil y 5.000 horas de operación al año?", "25000//5000", "Se divide la vida útil entre las horas por año.", " años"),
        ("=", "{F} ¿Cuántos rodamientos tienen en total los 6 reductores?", "6*2", "Se multiplican los reductores por los rodamientos de cada uno.", " rodamientos"),
        ("=", "{F} ¿Cuántos rodamientos se necesitan para cambiar todos una vez, más el stock de seguridad?", "6*2+2", "Se suman los rodamientos de la planta y el stock de seguridad.", " rodamientos"),
        ("=", "{F} Con 5 rodamientos en bodega, ¿cuántos faltan para cubrir el cambio de todos más el stock de seguridad?", "(6*2+2)-5", "Se resta el inventario a la necesidad total.", " rodamientos"),
        ("=", "{F} ¿Cuánto cuesta comprar los rodamientos faltantes, a $45.000 cada uno?", "9*45000", "Se multiplican los faltantes por el precio de cada rodamiento.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto se ahorra al evitar una parada no programada con una parada programada?", "200000-40000", "Se resta el costo de la programada al de la no programada.", " pesos de ejemplo"),
        ("abc", "{F} Un rodamiento se puede reparar por $20.000 y el manual lo permite. Según la regla de ejemplo, ¿qué corresponde?", "Repararlo, porque 20.000 es menor que la mitad de 45.000", "Reponerlo, porque cuesta menos que el nuevo", "No se puede decidir sin otro dato", "La mitad de 45.000 es 22.500 y 20.000 es menor."),
        ("abc", "{F} Otro rodamiento costaría $30.000 repararlo y el manual lo permite. ¿Qué corresponde con la regla?", "Reponerlo, porque 30.000 supera la mitad de 45.000", "Repararlo, porque cuesta menos que el nuevo", "Mantenerlo sin evaluar", "La reparación debe costar la mitad o menos del repuesto nuevo."),
        ("abc", "{F} Un jefe dice: «apliquemos la regla de reparar a un eje de $120.000 que cuesta $50.000 repararlo». ¿Qué falta verificar?", "Que el manual permita reparar ese eje", "Que el color del eje sea el original", "Que el eje sea más pesado", "La regla solo aplica si el manual lo permite."),
        ("=", "Una pieza de ejemplo dura 12.000 horas y el equipo opera 3.000 horas al año. Una planta tiene 8 equipos iguales con 1 pieza cada uno. ¿Cuántas piezas se cambian en un año si se cambia la cuarta parte de ellas cada año?", "8*3000//12000", "Se multiplican los equipos por las horas por año y se dividen por la vida útil.", " piezas"),
    ],
    ctx=("abc", "El bodeguero de ejemplo dice: «con 5 rodamientos alcanza para todo el año». La planta necesita 12 más el stock de seguridad. ¿Qué respondes?", "Que faltan rodamientos y conviene calcular el faltante antes de comprar", "Que tiene razón", "Que se compre un rodamiento por semana", "Se compara el inventario con la necesidad total."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuántos años dura una pieza de 18.000 horas con 3.000 horas al año?", "6 años", "Se divide la vida útil entre las horas de uso por año."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué parada cuesta menos?", "La parada programada", "Se planifica y evita daños mayores."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se verifica antes de aplicar la regla de reparar?", "Que el manual permita reparar", "El manual puede prohibirlo aunque cueste menos."),
    ],
    op=("Ficha de ejemplo: una planta tiene 4 motores y cada uno usa 2 rodamientos de $30.000. En bodega hay 3. Stock de seguridad: 2. Un rodamiento puede repararse por $12.000 si el manual lo permite; regla: se repara si cuesta la mitad o menos del nuevo. Escribe (a) cuántos rodamientos se necesitan en total con el stock de seguridad, (b) cuántos faltan, (c) cuánto cuesta comprarlos, (d) si conviene reparar uno y por qué.",
        "(a) 4 × 2 + 2 = 10. (b) 10 − 3 = 7. (c) 7 × 30.000 = 210.000 pesos de ejemplo. (d) Sí, si el manual lo permite: la mitad de 30.000 es 15.000 y 12.000 es menor.",
        ["calcula la necesidad", "calcula el faltante", "calcula el costo", "aplica la regla"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el stock", "no restar el inventario", "aplicar la regla sin el manual"],
        "Pregunta: «¿cuántos rodamientos hay que tener y cuántos hay?». Si duda, pídele que arme una pequeña tabla."),
    reinforce="Inventa un equipo con piezas, vida útil y horas por año y calcula cuántos años dura una pieza.",
    extend="Explica con un ejemplo por qué el stock de seguridad evita una parada no programada.",
)

# ============================================================ OAM-04, clase 5
F = ("Ficha 5 (comparación de repuestos y lista de verificación, de ejemplo). Alternativa O: repuesto original del fabricante, $75.000, garantía 12 meses, con certificado y código del manual, vida útil 25.000 horas. "
     "Alternativa Q: repuesto alternativo, $42.000, garantía 3 meses, sin certificado, con otro código, vida útil informada 15.000 horas. Alternativa R: repuesto reacondicionado, $36.000, garantía 6 meses, con certificado, con el código del manual, vida útil 10.000 horas. "
     "Condición obligatoria: tener certificado y el código del manual. Equipo que opera 5.000 horas al año. Lista de verificación posterior: orden de trabajo completa; código coincide; pieza retirada gestionada como residuo; hoja de vida actualizada; mediciones de control registradas.")
build(
    O4, 5, F,
    use="Aprenderé a comparar repuestos con una condición obligatoria y costos por hora, y a verificar con una lista que la reposición quedó bien documentada.",
    prior=["Sé qué es el código de repuesto.", "Sé calcular costo por hora de vida útil.", "Sé qué es una lista de verificación."],
    explain=[
        "Al comparar repuestos, primero se descartan los que no cumplen la condición obligatoria, como tener certificado y el código del manual. Entre los que cumplen se comparan el precio, la garantía y el costo por hora de vida útil, que es el precio dividido por las horas de vida útil. Un repuesto reacondicionado es una pieza usada que se recuperó y se vuelve a ofrecer; su vida útil suele ser menor.",
        "Tras la reposición se verifica la calidad con una lista de verificación: orden de trabajo completa, código coincidente, pieza retirada gestionada como residuo, hoja de vida actualizada y mediciones de control registradas. Una lista con puntos sin cumplir no se firma. El supervisor aprueba y deja constancia.",
        f"Es un análisis de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("repuesto original", "el que fabrica o autoriza el fabricante del equipo"), ("repuesto alternativo", "el que fabrica otra empresa para reemplazar al original"), ("reacondicionado", "pieza usada recuperada y vuelta a ofrecer"), ("condición obligatoria", "requisito que se debe cumplir para considerar la alternativa"), ("costo por hora de vida útil", "precio dividido por las horas de vida útil")],
    worked=[
        ("Costo por hora", "Un repuesto de ejemplo cuesta $30.000 y dura 6.000 horas. ¿Cuánto cuesta por hora de vida útil?", ["Se divide el precio entre las horas.", "30.000 dividido en 6.000 son 5."], "$5 por hora"),
        ("Descartar", "Una condición exige certificado. Una alternativa de ejemplo no lo tiene. ¿Se considera?", ["No cumple la condición.", "Se descarta."], "No, se descarta"),
    ],
    mistakes=[("Elegir el repuesto más barato sin revisar certificado y código.", "No cumple la condición obligatoria y puede fallar.", "Descarta primero las que no cumplen."),
              ("Firmar la lista de verificación sin gestionar la pieza retirada.", "La pieza retirada es un residuo.", "Completa cada punto antes de firmar.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un repuesto reacondicionado?", "Una pieza usada recuperada y vuelta a ofrecer", "Una pieza nueva del fabricante", "Una pieza fabricada para otro equipo", "Reacondicionado significa recuperado después de un uso."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un repuesto original?", "El que fabrica o autoriza el fabricante del equipo", "El más barato del mercado", "El que se fabrica en la planta", "El original tiene respaldo del fabricante."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué hace una lista de verificación posterior a la reposición?", "Comprueba que todo lo documentado esté completo", "Calcula el costo de la pieza", "Reemplaza la orden de trabajo", "Verifica cada punto de la reposición, uno por uno."),
        ("abc", "{F} ¿Qué alternativas cumplen la condición obligatoria?", "O y R", "Q y R", "Solo Q", "O y R tienen certificado y código del manual."),
        ("=", "{F} ¿Cuánto cuesta por hora de vida útil el repuesto original O?", "75000//25000", "Se divide el precio entre las horas, con enteros.", " pesos de ejemplo por hora"),
        ("=", "{F} ¿Cuántos años dura el original O, con 5.000 horas de operación al año?", "25000//5000", "Se divide la vida útil entre las horas por año.", " años"),
        ("=", "{F} ¿Cuántos años dura el reacondicionado R, con 5.000 horas de operación al año?", "10000//5000", "Se divide la vida útil entre las horas por año.", " años"),
        ("=", "{F} Si se usara R durante 10 años, ¿cuántas veces habría que comprarlo, con la duración de R?", "10//2", "Se divide el tiempo total entre los años que dura cada pieza.", " veces"),
        ("=", "{F} Con el costo de R repetido durante 10 años, ¿cuánto se gasta?", "5*36000", "Se multiplica el número de compras por el precio de R.", " pesos de ejemplo"),
        ("=", "{F} Si se usara O durante 10 años, ¿cuánto se gasta, comprándolo cada 5 años?", "2*75000", "Se multiplica el número de compras por el precio de O.", " pesos de ejemplo"),
        ("abc", "{F} Comparando solo los dos que cumplen y el gasto a 10 años, ¿qué resulta?", "O gasta 150.000 y R gasta 180.000, así que O es más conveniente", "R es más conveniente, porque su precio es menor", "Ambos gastan lo mismo", "Con la duración de cada uno, R se compra más veces."),
        ("abc", "{F} Un jefe dice: «Q cuesta menos que O, comprémoslo». ¿Qué respuesta es correcta?", "No corresponde: Q no cumple la condición obligatoria de certificado y código del manual", "Corresponde, porque es más barato", "Corresponde, si la garantía es corta", "La condición obligatoria se aplica antes del precio."),
        ("abc", "{F} Faltó retirar el registro de la pieza vieja como residuo y se pide firmar la lista. ¿Qué corresponde?", "No firmarla hasta gestionar la pieza retirada y completar el punto", "Firmarla porque la pieza nueva ya funciona", "Borrar el punto", "La lista no se firma con puntos incompletos."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece un repuesto muy barato sin certificado. ¿Qué propones?", "No aceptarlo mientras no cumpla la condición obligatoria del certificado y el código", "Aceptarlo para ahorrar", "Aceptarlo si el proveedor es conocido", "Sin certificado no se cumple la condición obligatoria."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace primero al comparar repuestos?", "Descartar los que no cumplen la condición obligatoria", "Después se comparan los costos de las que cumplen."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se obtiene el costo por hora de vida útil?", "Dividiendo el precio entre las horas de vida útil", "Mide el costo de cada hora que dura la pieza."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué pasa con la pieza retirada?", "Se gestiona como residuo según la norma", "Un residuo no se bota sin gestionarlo según la norma."),
    ],
    op=("Ficha de ejemplo: dos repuestos que cumplen la condición obligatoria. X: $50.000, dura 20.000 horas. Z: $35.000, dura 10.000 horas. El equipo opera 5.000 horas al año y se evalúan 20.000 horas. Escribe (a) cuántos años dura cada uno, (b) cuántas compras de cada uno se necesitan en 20.000 horas, (c) cuánto gasta cada uno, (d) cuál conviene y qué compruebas al terminar la reposición.",
        "(a) X: 20.000 ÷ 5.000 = 4 años; Z: 10.000 ÷ 5.000 = 2 años. (b) X: 1 compra; Z: 2 compras. (c) X: 50.000; Z: 2 × 35.000 = 70.000. (d) X, porque gasta menos en las 20.000 horas; al terminar se comprueba la lista de verificación, incluyendo código, residuo y hoja de vida.",
        ["calcula los años", "calcula las compras", "calcula el gasto", "decide y verifica"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo el precio", "olvidar las compras repetidas", "no usar la lista de verificación"],
        "Pregunta: «¿cuántas veces se compra cada uno en el mismo tiempo?». Si duda, pídele que divida las horas totales entre la vida útil."),
    reinforce="Inventa dos repuestos con precio y vida útil y compara cuál gasta menos en un mismo periodo.",
    extend="Explica con un ejemplo por qué un repuesto más barato puede resultar más caro en el tiempo.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Una planta de ejemplo va a poner en funcionamiento una bomba ficticia B-30 tras una reparación. Participan: el jefe de mantenimiento, el técnico autorizado, el operador de la planta, el supervisor de seguridad y el inspector. "
     "Peligros anotados: energía eléctrica, partes giratorias, presión en la tubería, fluido caliente, ruido y personas dentro de la zona de la bomba. Documentos: protocolo de puesta en marcha, tabla de tolerancias del fabricante y permiso de trabajo.")
build(
    O5, 1, F,
    use="Aprenderé qué es la puesta en funcionamiento de un equipo, por qué es una etapa de riesgo, quiénes participan y qué documentos la respaldan.",
    prior=["Sé qué es la energía almacenada.", "Sé qué es un permiso de trabajo.", "Sé qué es una tolerancia."],
    explain=[
        "Poner en funcionamiento un equipo es hacerlo funcionar por primera vez tras una instalación o una reparación y comprobar que cumple lo que pide el fabricante. Es una etapa de riesgo porque las energías se activan: puede haber una conexión mal hecha, una pieza floja o una presión inesperada. Por eso se hace con un protocolo de puesta en marcha, un documento que lista las verificaciones previas, las pruebas, las mediciones y las firmas.",
        "Participan roles definidos: el jefe de mantenimiento coordina, el técnico autorizado ejecuta, el operador conoce el proceso, el supervisor de seguridad vela por las personas y el inspector verifica que todo cumpla. Antes de comenzar, la zona se despeja de personas que no participan y todos conocen el plan y cómo detener el equipo. La SEC fiscaliza lo eléctrico y la tabla de tolerancias fija qué valores se aceptan.",
        f"Este cuaderno no enseña a poner en marcha un equipo; solo conceptos y documentos. {EMER} {AVISO}",
    ],
    vocab=[("puesta en funcionamiento", "hacer funcionar un equipo por primera vez tras instalarlo o repararlo"), ("protocolo de puesta en marcha", "documento con verificaciones previas, pruebas, mediciones y firmas"), ("tabla de tolerancias", "lista de valores aceptados por el fabricante"), ("zona despejada", "área sin personas que no participan"), ("inspector", "persona que verifica que se cumplan los requisitos")],
    worked=[
        ("Elegir el documento", "Una empresa de ejemplo quiere dejar constancia de las pruebas de un equipo recién reparado. ¿Qué documento usa?", ["Las pruebas y las firmas se anotan en un protocolo.", "Es el protocolo de puesta en marcha."], "El protocolo de puesta en marcha"),
        ("Rol", "Una persona de ejemplo vela por que nadie quede cerca del equipo durante la prueba. ¿Qué rol cumple?", ["Su función es proteger a las personas.", "Es el supervisor de seguridad."], "Supervisor de seguridad"),
    ],
    mistakes=[("Hacer la primera puesta en marcha sin avisar a las personas que están cerca.", "Una activación inesperada puede dañarlas.", "Se despeja la zona y se comunica el plan."),
              ("Dar por buena la prueba sin firmar el protocolo.", "Sin registro no hay constancia de las verificaciones.", "Cada prueba se anota y se firma.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es poner en funcionamiento un equipo?", "Hacerlo funcionar por primera vez tras instalarlo o repararlo y comprobar que cumple", "Revisar su pintura exterior", "Cambiar su ubicación en la planta", "Es una etapa de comprobación del funcionamiento."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el protocolo de puesta en marcha?", "Un documento con verificaciones, pruebas, mediciones y firmas", "Un plano del equipo", "Una lista de repuestos", "El protocolo organiza y respalda la puesta en marcha."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una zona despejada?", "Un área sin personas que no participan", "Un área con mucha iluminación", "Un área sin herramientas", "Se despeja para evitar que alguien quede expuesto."),
        ("abc", "{F} ¿Qué rol coordina la puesta en marcha de la bomba?", "El jefe de mantenimiento", "El operador de la planta", "El inspector", "El jefe de mantenimiento coordina a todos los participantes."),
        ("abc", "{F} ¿Cuál de los peligros anotados se asocia a las personas dentro de la zona de la bomba?", "Una activación inesperada que las alcance", "El ruido de la oficina", "El color de la tubería", "Quien está dentro de la zona queda expuesto a las energías activas."),
        ("=", "{F} ¿Cuántos roles participan en la puesta en marcha de la ficha?", "5", "Se cuentan el jefe de mantenimiento, el técnico, el operador, el supervisor y el inspector.", " roles"),
        ("=", "{F} Cada rol firma el protocolo en 2 hojas. ¿Cuántas firmas suma el protocolo?", "5*2", "Se multiplican los roles por las firmas de cada uno.", " firmas"),
        ("=", "{F} Se ponen en marcha 3 bombas iguales con el mismo protocolo de 6 verificaciones. ¿Cuántas verificaciones se registran en total?", "3*6", "Se multiplican las bombas por las verificaciones.", " verificaciones"),
        ("abc", "{F} Un operador propone iniciar la prueba sin avisar «para no asustar a nadie». ¿Qué respuesta es correcta?", "No corresponde: se comunica el plan y se despeja la zona antes de comenzar", "Corresponde, porque es una prueba breve", "Corresponde, si lleva casco", "Una activación sin aviso expone a las personas."),
        ("abc", "{F} Un estudiante dice: «yo puedo hacer la puesta en marcha porque entiendo el protocolo». ¿Qué respuesta es correcta?", "Es falso: la hace personal autorizado con norma vigente, y este cuaderno no habilita para hacerla", "Es cierto, si lo hace con compañeros", "Es cierto, si usa EPP", "Entender el protocolo no autoriza a ejecutarlo."),
        ("abc", "Durante una prueba de ejemplo, una tubería se rompe y proyecta fluido caliente cerca de una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a cerrar una válvula", "Cubrir la fuga con un trapo", "Intervenir sin formación puede causar quemaduras."),
        ("=", "{F} Si cada una de las 5 personas participantes asiste a 2 reuniones previas de 1 hora, ¿cuántas horas-persona de reunión se registran?", "5*2*1", "Se multiplican personas, reuniones y horas.", " horas-persona"),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿quién fiscaliza lo eléctrico de una planta?", "La SEC", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La SEC fiscaliza electricidad y combustibles."),
    ],
    ctx=("abc", "Un jefe de ejemplo dice: «hagamos la prueba ya, después llenamos el protocolo». ¿Qué propones?", "Que el protocolo se complete y se firme durante la puesta en marcha, con la zona despejada", "Aceptarlo para ganar tiempo", "Hacer la prueba sin avisar", "El protocolo es la constancia en el momento de la prueba."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué documento respalda una puesta en marcha?", "El protocolo de puesta en marcha", "Contiene verificaciones, pruebas, mediciones y firmas."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué rol vela por las personas durante la prueba?", "El supervisor de seguridad", "Su función es proteger a las personas."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace con la zona antes de comenzar?", "Se despeja y se comunica el plan", "Evita que alguien quede expuesto a una activación."),
    ],
    op=("Ficha de ejemplo: una planta pondrá en marcha un ventilador ficticio tras repararlo. Participan: jefe de mantenimiento, técnico autorizado, operador y supervisor de seguridad. Peligros: energía eléctrica, partes giratorias y personas cerca. Escribe (a) qué documento respalda la puesta en marcha, (b) qué rol vela por las personas, (c) dos acciones previas para reducir el riesgo, (d) quién ejecuta la puesta en marcha. No describas cómo se arranca el equipo.",
        "(a) El protocolo de puesta en marcha. (b) El supervisor de seguridad. (c) Despejar la zona y comunicar el plan a todos los participantes. (d) El técnico autorizado, con norma vigente.",
        ["nombra el documento", "nombra el rol", "propone dos acciones previas", "indica quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["confundir los roles", "proponer solo EPP", "describir cómo se arranca"],
        "Pregunta: «¿quién cuida a las personas?». Si duda, pídele que relea los roles."),
    reinforce="Escribe cuatro roles de una puesta en marcha y la función de cada uno.",
    extend="Explica con un ejemplo por qué la primera puesta en marcha tiene más riesgo que el funcionamiento rutinario.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (tabla de tolerancias del fabricante, de ejemplo e inventada, para la bomba ficticia B-30). Velocidad de giro nominal: 1.500 vueltas por minuto (rpm), tolerancia ±50 rpm. Presión de descarga nominal: 400 unidades de ejemplo, tolerancia ±20. "
     "Corriente del motor: máximo 11 A. Temperatura del cojinete: máximo 70 °C. Vibración: máximo 5 unidades de ejemplo. Un valor nominal es el valor de diseño; la tolerancia es la diferencia aceptada alrededor del nominal; un máximo es un valor que no se debe superar. "
     "El protocolo exige comparar cada medición con la tabla y firmar cada punto.")
build(
    O5, 2, F,
    use="Aprenderé a leer una tabla de tolerancias del fabricante, a distinguir valor nominal, tolerancia y máximo, y a decidir si una medición cumple.",
    prior=["Sé qué es una tolerancia.", "Sé restar y comparar números.", "Sé qué es un protocolo."],
    explain=[
        "Una tabla de tolerancias del fabricante indica, para cada variable, el valor nominal y su tolerancia, o un valor máximo. El valor nominal es el de diseño; la tolerancia es la diferencia aceptada hacia arriba y hacia abajo. Una medición cumple si queda entre el nominal menos la tolerancia y el nominal más la tolerancia, límites incluidos. Una variable con máximo cumple si no lo supera.",
        "El protocolo exige comparar cada medición con la tabla y firmar cada punto. Una medición fuera de tolerancia es una no conformidad: se informa y se detiene el avance hasta que personal autorizado la corrija. Las mediciones las toma personal autorizado con instrumentos calibrados y se anota el instrumento, la fecha y quién midió.",
        f"Se trabaja con documentos y cálculos; no se mide ni se pone en marcha ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("valor nominal", "valor de diseño de una variable"), ("tolerancia", "diferencia aceptada alrededor del valor nominal"), ("máximo", "valor que una variable no debe superar"), ("rpm", "vueltas por minuto"), ("no conformidad", "medición que no cumple lo pedido")],
    worked=[
        ("Límites de tolerancia", "Una variable de ejemplo tiene nominal 100 y tolerancia ±10. ¿Entre qué valores cumple?", ["El límite inferior es 100 menos 10.", "El superior es 100 más 10."], "Entre 90 y 110"),
        ("Cumplir un máximo", "Un máximo de ejemplo es 8 y se mide 9. ¿Cumple?", ["9 es mayor que 8.", "Supera el máximo."], "No cumple"),
    ],
    mistakes=[("Confundir el nominal con el máximo.", "El nominal es el valor de diseño y puede aceptar variaciones; el máximo es un tope.", "Lee primero el tipo de dato de cada fila."),
              ("Dar por cumplido un valor fuera de tolerancia porque «es muy poco».", "Fuera de tolerancia no cumple.", "Registra la no conformidad.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el valor nominal?", "El valor de diseño de una variable", "El valor máximo que no se debe superar", "El valor medido en la prueba", "El nominal es el valor para el que se diseñó."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la tolerancia en una tabla del fabricante?", "La diferencia aceptada alrededor del valor nominal", "El precio de la pieza", "El valor medido", "La tolerancia fija el rango aceptado."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué significa rpm?", "Vueltas por minuto", "Revisiones por mes", "Repuestos por máquina", "rpm indica cuántas vueltas da un eje en un minuto."),
        ("=", "{F} ¿Cuál es el límite inferior de la velocidad de giro aceptada?", "1500-50", "Se resta la tolerancia al valor nominal.", " rpm"),
        ("=", "{F} ¿Cuál es el límite superior de la presión de descarga aceptada?", "400+20", "Se suma la tolerancia al valor nominal.", " unidades de ejemplo"),
        ("abc", "{F} ¿Qué tipo de dato es la temperatura del cojinete en la tabla?", "Un máximo que no se debe superar", "Un valor nominal con tolerancia", "Un valor medido", "La tabla indica un máximo de 70 °C."),
        ("abc", "{F} Una medición de velocidad da 1.540 rpm. ¿Cumple?", "Sí, porque está entre 1.450 y 1.550", "No, porque no es 1.500", "No, porque supera 1.500", "Cumple porque queda dentro de la tolerancia."),
        ("abc", "{F} Una medición de presión da 425 unidades de ejemplo. ¿Cumple?", "No, porque supera el límite superior de 420", "Sí, porque 425 es cercano a 400", "Sí, porque es menor que 1.500", "El límite superior es 400 más 20, es decir 420."),
        ("abc", "{F} Una medición de corriente da 11 A. ¿Cumple?", "Sí, porque el máximo se cumple si no se supera, y 11 no supera 11", "No, porque es igual al máximo", "No, porque debe ser menor que 10", "Un máximo se cumple mientras no se supere."),
        ("=", "{F} Una medición de vibración da 7 unidades de ejemplo. ¿Cuántas unidades supera el máximo?", "7-5", "Se resta el máximo a la medición.", " unidades"),
        ("abc", "{F} Un practicante dice: «la medición de presión excedió el límite por poco, la anoto como correcta». ¿Qué respuesta es correcta?", "No corresponde: se registra el valor real y la no conformidad, y se informa", "Corresponde, porque es poco", "Corresponde, si lo firma otra persona", "Anotar un valor falso oculta el problema."),
        ("abc", "{F} Un estudiante propone medir la vibración de la bomba en funcionamiento acercando un instrumento. ¿Qué respuesta es correcta?", "No corresponde: la medición la hace personal autorizado con instrumentos calibrados y procedimiento", "Corresponde, si usa guantes", "Corresponde, si la bomba está lenta", "Medir en equipos en marcha es peligroso y exige autorización."),
        ("En un equipo de ejemplo, el nominal es 3.000 con tolerancia ±100. ¿Cumple una medición de 3.100?", "Sí", "3.100 es el límite superior y los límites se incluyen."),
    ],
    ctx=("abc", "Un técnico de ejemplo mide una temperatura de 74 °C y el máximo del fabricante es 70 °C. ¿Qué propones?", "Registrar la medición real, marcar la no conformidad e informar a la jefatura", "Anotar 70 °C", "Esperar a que baje", "El registro debe reflejar la medición real."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuál es el rango de 200 ±15?", "Entre 185 y 215", "Se resta y se suma la tolerancia al nominal."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuándo cumple una variable con máximo?", "Cuando no lo supera", "Un máximo es un tope que no se debe superar."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace con una medición fuera de tolerancia?", "Se registra e informa como no conformidad", "No se altera el valor medido para que cumpla."),
    ],
    op=("Ficha de ejemplo: tabla de un ventilador ficticio. Velocidad nominal: 900 rpm, tolerancia ±30. Corriente máxima: 6 A. Temperatura máxima del cojinete: 65 °C. Mediciones: velocidad 925 rpm; corriente 6 A; temperatura 68 °C. Escribe (a) el rango aceptado de velocidad, (b) si la velocidad cumple, (c) si la corriente cumple, (d) qué haces con la temperatura.",
        "(a) Entre 870 y 930 rpm. (b) Sí, 925 está dentro. (c) Sí, 6 no supera el máximo de 6. (d) Es una no conformidad (68 supera 65): se registra el valor real y se informa a la jefatura.",
        ["calcula el rango", "evalúa la velocidad", "evalúa la corriente", "trata la no conformidad"],
        ["hoja con las cuatro respuestas"],
        ["no incluir los límites", "alterar la temperatura", "no informar"],
        "Pregunta: «¿hay un nominal con tolerancia o un máximo?». Si duda, pídele que relea el tipo de cada fila."),
    reinforce="Inventa un nominal con tolerancia y tres mediciones, y marca cuáles cumplen.",
    extend="Explica con un ejemplo por qué un valor fuera de tolerancia no se corrige en el papel.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (planilla de mediciones de puesta en marcha, de ejemplo, inventada; las mediciones las tomó personal autorizado con instrumentos calibrados). Bomba B-30. Tabla del fabricante de ejemplo: velocidad 1.500 ±50 rpm; presión 400 ±20; corriente máxima 11 A; temperatura del cojinete máxima 70 °C; vibración máxima 5. "
     "Mediciones tras la primera prueba: velocidad 1.485 rpm; presión 430; corriente 9 A; temperatura 66 °C; vibración 4. Observaciones: ruido leve en una unión de la tubería; un instrumento tiene el certificado vencido (el de presión). "
     "Regla del protocolo: si hay alguna medición fuera de tolerancia o con instrumento sin certificado vigente, la bomba no se entrega y se informa al jefe de mantenimiento.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una planilla de mediciones de puesta en marcha, a detectar no conformidades y mediciones dudosas, y a decidir si el equipo se entrega.",
    prior=["Sé leer una tabla de tolerancias.", "Sé qué es un certificado de calibración.", "Sé qué es una no conformidad."],
    explain=[
        "En la planilla de puesta en marcha cada fila compara una medición con la tabla del fabricante y concluye si cumple. Una medición hecha con un instrumento de certificado vencido queda en duda, aunque su valor parezca correcto, y debe repetirse con un instrumento calibrado. Las observaciones, como un ruido, también se anotan, porque pueden indicar un problema aunque las mediciones sean buenas.",
        "La regla del protocolo decide si el equipo se entrega: basta una medición fuera de tolerancia o con instrumento sin certificado vigente para no entregarlo. La decisión se informa al jefe de mantenimiento y se registra. Un equipo no entregado vuelve al personal autorizado para corregir y repetir las pruebas.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("planilla de mediciones", "tabla donde se comparan las mediciones con la tabla del fabricante"), ("medición dudosa", "la que viene de un instrumento sin certificado vigente"), ("observación", "nota sobre algo que se notó, como un ruido"), ("entrega del equipo", "traspaso del equipo a quien lo operará"), ("repetir las pruebas", "volver a medir tras corregir")],
    worked=[
        ("Evaluar una fila", "Una variable de ejemplo tiene nominal 200 ±10 y se mide 215. ¿Cumple?", ["El límite superior es 210.", "215 supera 210."], "No cumple"),
        ("Medición dudosa", "Una medición de ejemplo cumple, pero el instrumento tiene el certificado vencido. ¿Se acepta?", ["El instrumento no es confiable.", "Queda en duda y se repite."], "No, se repite con un instrumento calibrado"),
    ],
    mistakes=[("Entregar el equipo porque «casi todo cumple».", "Basta una no conformidad para no entregarlo.", "Aplica la regla del protocolo."),
              ("Aceptar una medición con instrumento vencido porque el valor es correcto.", "El valor no es confiable.", "Repite con un instrumento calibrado.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una medición dudosa?", "Una medición hecha con un instrumento sin certificado vigente", "Una medición más alta que el nominal", "Una medición tomada por la mañana", "El certificado vencido deja la medición en duda."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿para qué se anotan las observaciones en la planilla?", "Porque pueden indicar un problema aunque las mediciones sean buenas", "Para llenar espacio en la planilla", "Para reemplazar las mediciones", "Un ruido puede avisar de un problema que no mide la tabla."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué ocurre con un equipo que no se entrega?", "Vuelve a personal autorizado para corregir y repetir las pruebas", "Se pone en operación igual", "Se guarda sin informar", "El equipo se corrige antes de la entrega."),
        ("=", "{F} ¿Cuántos rpm se aparta la velocidad medida del nominal?", "1500-1485", "Se resta la medición al nominal.", " rpm"),
        ("abc", "{F} ¿Cumple la velocidad medida?", "Sí, porque está entre 1.450 y 1.550", "No, porque no es 1.500", "No, porque es menor que 1.500", "La tolerancia de la velocidad es ±50 rpm."),
        ("abc", "{F} ¿Cumple la presión medida, de 430?", "No, porque supera el límite superior de 420", "Sí, porque es cercana a 400", "Sí, porque es menor que 1.500", "400 más 20 es 420 y 430 lo supera."),
        ("abc", "{F} ¿Qué pasa con la medición de presión, además de no cumplir?", "Es dudosa, porque su instrumento tiene el certificado vencido", "Es la más confiable de la planilla", "Reemplaza a la de corriente", "La ficha dice que el instrumento de presión tiene el certificado vencido."),
        ("=", "{F} ¿Cuántos A de margen tiene la corriente respecto del máximo?", "11-9", "Se resta la medición al máximo.", " A"),
        ("=", "{F} ¿Cuántos °C de margen tiene la temperatura respecto del máximo?", "70-66", "Se resta la medición al máximo.", " °C"),
        ("abc", "{F} Con la regla del protocolo, ¿se entrega la bomba?", "No, porque hay una medición fuera de tolerancia y un instrumento sin certificado vigente", "Sí, porque la mayoría cumple", "Sí, porque la corriente y la temperatura cumplen", "Basta una de las dos condiciones para no entregarla."),
        ("abc", "{F} Un jefe dice: «anotemos 415 en la presión, que cumple, y entreguemos». ¿Qué respuesta es correcta?", "No corresponde: se registra la medición real, se repite con un instrumento calibrado y no se entrega", "Corresponde, porque ahorra tiempo", "Corresponde, si todos están de acuerdo", "Alterar un valor es falsear el registro."),
        ("abc", "{F} El ruido leve en una unión de la tubería, ¿qué requiere?", "Registrarlo como observación e informarlo al personal autorizado para revisión", "Ignorarlo porque es leve", "Taparlo con un trapo", "Un ruido puede indicar una fuga o un problema en desarrollo."),
        ("En una planilla de ejemplo hay 6 mediciones, 4 cumplen y 2 no. ¿Cuántas no conformidades se registran?", "2", "Las que no cumplen son no conformidades."),
    ],
    ctx=("abc", "El cliente de ejemplo apura la entrega de la bomba, pero hay una medición fuera de tolerancia. ¿Qué propones?", "Informar el estado real, corregir con personal autorizado y repetir las pruebas antes de entregar", "Entregar la bomba igual", "Cambiar el valor medido", "La entrega depende de cumplir la tabla del fabricante."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuántas no conformidades basta para no entregar?", "Una", "Basta una medición fuera de tolerancia."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace con una medición dudosa?", "Se repite con un instrumento calibrado", "El instrumento sin certificado no es confiable."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿se altera un valor para que cumpla?", "No, nunca", "Alterar un valor falsea el registro."),
    ],
    op=("Ficha de ejemplo: tabla de un compresor ficticio: presión 800 ±40; corriente máxima 20 A; temperatura máxima 90 °C. Mediciones: presión 845; corriente 18 A; temperatura 85 °C. El instrumento de la corriente tiene el certificado vigente; el de la presión, vencido. Regla: si hay una medición fuera de tolerancia o con instrumento vencido, no se entrega. Escribe (a) el rango aceptado de presión, (b) si la presión cumple, (c) qué observas del instrumento de presión, (d) si se entrega el compresor y por qué.",
        "(a) Entre 760 y 840. (b) No, 845 supera 840. (c) Tiene el certificado vencido, por lo que la medición es dudosa. (d) No se entrega: hay una medición fuera de tolerancia y un instrumento vencido; se informa al jefe de mantenimiento.",
        ["calcula el rango", "evalúa la presión", "detecta el instrumento vencido", "decide la entrega"],
        ["hoja con las cuatro respuestas"],
        ["incluir mal los límites", "aceptar el instrumento vencido", "entregar el equipo"],
        "Pregunta: «¿qué instrumento tiene el certificado vencido?». Si duda, pídele que relea la ficha."),
    reinforce="Inventa una planilla de cuatro mediciones y decide si el equipo se entrega.",
    extend="Explica con un ejemplo por qué un valor que cumple puede igualmente no ser aceptado.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cálculos de desviación de ejemplo, inventados). Un equipo ficticio tiene velocidad nominal de 1.200 rpm con tolerancia de ±3 % del nominal. Presión nominal de 500 con tolerancia de ±4 %. "
     "Mediciones de cuatro pruebas de la velocidad, en rpm: 1.190; 1.215; 1.250; 1.170. Meta del protocolo: al menos 3 de las 4 pruebas deben cumplir y ninguna debe superar el doble de la tolerancia. Costo de ejemplo de repetir una prueba: $25.000.")
build(
    O5, 4, F,
    use="Aprenderé a calcular tolerancias en porcentaje, a evaluar varias pruebas con una meta y a calcular el costo de repetirlas, con datos de ejemplo.",
    prior=["Sé calcular un porcentaje de números redondos.", "Sé qué es una tolerancia.", "Sé restar y comparar números."],
    explain=[
        "Una tolerancia puede darse en porcentaje del nominal. Para pasarla a unidades se multiplica el nominal por el porcentaje y se divide por 100. Por ejemplo, 3 % de 1.200 es 36. El rango aceptado es el nominal más y menos esa cantidad. La desviación de una medición es la diferencia entre lo medido y el nominal, sin signo.",
        "Con varias pruebas se cuenta cuántas cumplen y se compara con la meta. Una regla adicional, como no superar el doble de la tolerancia, evita aceptar desviaciones grandes aunque la mayoría cumpla. Repetir pruebas tiene un costo, por lo que conviene corregir la causa antes de repetirlas. Todo el cálculo es de papel.",
        f"Los números son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("tolerancia porcentual", "tolerancia dada como porcentaje del nominal"), ("desviación", "diferencia entre lo medido y el nominal, sin signo"), ("rango aceptado", "valores entre el nominal menos y más la tolerancia"), ("meta del protocolo", "mínimo de pruebas que deben cumplir"), ("doble de la tolerancia", "dos veces la tolerancia")],
    worked=[
        ("Tolerancia en unidades", "Un nominal de ejemplo es 800 con tolerancia de ±5 %. ¿Cuánto es la tolerancia en unidades?", ["Se multiplica 800 por 5: 4.000.", "4.000 dividido en 100 son 40."], "±40"),
        ("Desviación", "Un nominal de ejemplo es 800 y se mide 770. ¿Cuál es la desviación?", ["La diferencia es 800 menos 770.", "La desviación es 30."], "30"),
    ],
    mistakes=[("Aplicar el porcentaje a la medición y no al nominal.", "La tolerancia se calcula sobre el nominal.", "Usa siempre el nominal para el porcentaje."),
              ("Ignorar el signo al comparar la desviación con el rango.", "La desviación se compara sin signo con la tolerancia.", "Usa la diferencia sin signo.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la desviación de una medición?", "La diferencia entre lo medido y el nominal, sin signo", "La suma de lo medido y el nominal", "El promedio de varias mediciones", "La desviación mide cuánto se aparta del nominal."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿sobre qué se calcula una tolerancia porcentual?", "Sobre el valor nominal", "Sobre la medición", "Sobre el máximo", "El porcentaje se aplica al nominal."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el rango aceptado?", "Los valores entre el nominal menos y más la tolerancia", "El valor más alto medido", "El nominal solamente", "El rango incluye los límites inferior y superior."),
        ("=", "{F} ¿Cuántas rpm vale la tolerancia de la velocidad, con 3 % del nominal?", "3*1200//100", "Se multiplica el nominal por el porcentaje y se divide por 100.", " rpm"),
        ("=", "{F} ¿Cuál es el límite superior de la velocidad aceptada?", "1200+36", "Se suma la tolerancia al nominal.", " rpm"),
        ("=", "{F} ¿Cuál es el límite inferior de la velocidad aceptada?", "1200-36", "Se resta la tolerancia al nominal.", " rpm"),
        ("abc", "{F} ¿Cuántas de las cuatro pruebas cumplen?", "Tres: 1.190, 1.215 y 1.170", "Dos", "Cuatro", "1.250 supera el límite superior de 1.236; las otras están entre 1.164 y 1.236."),
        ("=", "{F} ¿Cuál es la desviación de la prueba de 1.250 rpm?", "1250-1200", "Se resta el nominal a la medición.", " rpm"),
        ("=", "{F} ¿Cuántas rpm vale el doble de la tolerancia?", "36*2", "Se multiplica la tolerancia por 2.", " rpm"),
        ("abc", "{F} ¿Supera alguna prueba el doble de la tolerancia?", "No, la mayor desviación es 50 y el doble de la tolerancia es 72", "Sí, la de 1.250", "Sí, la de 1.170", "La mayor desviación, 50, es menor que 72."),
        ("abc", "{F} Según la meta, ¿cumple el protocolo?", "Sí: 3 de 4 pruebas cumplen y ninguna supera el doble de la tolerancia", "No, porque una prueba no cumple", "No, porque la meta pide las 4", "La meta pide al menos 3 de 4 y no superar 72."),
        ("abc", "{F} Un jefe dice: «como cumple la meta, no hace falta investigar la prueba de 1.250 rpm». ¿Qué respuesta es adecuada?", "Conviene investigar la causa, porque una prueba fuera de tolerancia puede indicar un problema", "Tiene razón, porque la meta se cumple", "Hay que repetir todas las pruebas sin investigar", "Cumplir la meta no impide que haya un problema."),
        ("=", "{F} Si se repiten las 4 pruebas por $25.000 cada una, ¿cuánto cuesta repetirlas?", "4*25000", "Se multiplica el número de pruebas por el costo de cada una.", " pesos de ejemplo"),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «repitamos las 4 pruebas hasta que todas salgan buenas». ¿Qué propones?", "Investigar primero la causa de la prueba fuera de tolerancia, porque repetir sin corregir es un gasto", "Repetir hasta que salga bien", "Quitar la prueba mala del registro", "Corregir la causa antes de repetir evita costos y riesgos."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuánto es 3 % de 1.200?", "36", "Se multiplica 1.200 por 3 y se divide por 100."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se compara con la meta del protocolo?", "El número de pruebas que cumplen", "La meta fija el mínimo de pruebas que deben cumplir."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿se quita del registro una prueba mala?", "No, nunca", "El registro debe ser completo y fiel."),
    ],
    op=("Ficha de ejemplo: velocidad nominal de 900 rpm con tolerancia de ±2 %. Cuatro pruebas dieron, en rpm: 890; 920; 935; 905. Meta: al menos 3 de 4 pruebas cumplen y ninguna supera el doble de la tolerancia. Costo de repetir una prueba: $15.000. Escribe (a) la tolerancia en rpm, (b) el rango aceptado, (c) cuántas pruebas cumplen y si se cumple la meta, (d) cuánto costaría repetir las pruebas que no cumplen.",
        "(a) 2 × 900 ÷ 100 = 18 rpm. (b) Entre 882 y 918. (c) Cumplen 890 y 905; no cumplen 920 ni 935; solo 2 de 4, así que no se cumple la meta. (d) 2 × 15.000 = 30.000 pesos de ejemplo, si antes se corrige la causa.",
        ["calcula la tolerancia", "calcula el rango", "cuenta y compara con la meta", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["aplicar el porcentaje a la medición", "contar mal las pruebas", "repetir sin investigar"],
        "Pregunta: «¿entre qué valores cumple una prueba?». Si duda, pídele que calcule primero el rango."),
    reinforce="Inventa un nominal con tolerancia porcentual y tres pruebas, y cuenta cuántas cumplen.",
    extend="Explica con un ejemplo por qué la regla del doble de la tolerancia evita aceptar desviaciones grandes.",
)

# ============================================================ OAM-05, clase 5
F = ("Ficha 5 (comparación de dos informes de puesta en marcha y cierre, de ejemplo). Equipo E-1: todas las mediciones cumplen; protocolo firmado en todos los puntos; instrumentos con certificado vigente; capacitación al operador realizada; residuos gestionados; hoja de vida actualizada. "
     "Equipo E-2: todas las mediciones cumplen; falta la firma en 2 puntos; un instrumento tiene el certificado vencido; capacitación pendiente; aceite usado sin gestionar; hoja de vida actualizada. "
     "Lista de cierre de ejemplo: mediciones cumplen; protocolo firmado completo; instrumentos con certificado vigente; capacitación al operador realizada; residuos gestionados; hoja de vida actualizada. Cada punto cumplido suma 1 punto de 6.")
build(
    O5, 5, F,
    use="Aprenderé a comparar dos informes de puesta en marcha con una lista de cierre, a puntuar el cumplimiento y a decidir qué falta antes de entregar.",
    prior=["Sé qué es un protocolo de puesta en marcha.", "Sé qué es una medición dudosa.", "Sé sumar puntos."],
    explain=[
        "Antes de entregar un equipo se verifica una lista de cierre: que las mediciones cumplan, que el protocolo esté completo y firmado, que los instrumentos tengan el certificado vigente, que se haya capacitado al operador, que los residuos estén gestionados y que la hoja de vida esté actualizada. Cada punto cumplido se cuenta, pero el equipo solo se entrega cuando se cumplen todos.",
        "Comparar dos informes permite ver qué falta en cada uno y ordenar las tareas pendientes por riesgo: primero lo que afecta a la seguridad o a la validez de las mediciones, después lo documental. La capacitación al operador reduce errores de uso, y la gestión de residuos cumple la norma vigente. La entrega la aprueba el jefe de mantenimiento.",
        f"El análisis es de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("lista de cierre", "lista de puntos que deben cumplirse antes de entregar el equipo"), ("capacitación al operador", "instrucción a quien usará el equipo sobre su uso seguro"), ("tarea pendiente", "punto de la lista aún no cumplido"), ("residuos gestionados", "residuos llevados al punto de acopio según la norma"), ("entrega aprobada", "traspaso autorizado por el jefe de mantenimiento")],
    worked=[
        ("Puntuar", "Una lista de cierre de ejemplo tiene 6 puntos y un equipo cumple 4. ¿Cuántos puntos pendientes tiene?", ["Se resta lo cumplido al total.", "6 menos 4 son 2."], "2 puntos pendientes"),
        ("Ordenar por riesgo", "Un equipo de ejemplo tiene pendientes: actualizar la hoja de vida y reparar un instrumento con certificado vencido. ¿Cuál se prioriza?", ["El instrumento afecta la validez de las mediciones.", "La hoja de vida es documental."], "Primero el instrumento con certificado vencido"),
    ],
    mistakes=[("Entregar un equipo con puntos pendientes porque «lo documental se llena después».", "La lista exige cumplir todos los puntos.", "Cumple todos antes de entregar."),
              ("Omitir la capacitación al operador.", "El operador puede usar mal el equipo.", "La capacitación es un punto de cierre.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la lista de cierre?", "Una lista de puntos que deben cumplirse antes de entregar el equipo", "Un plano del equipo", "Una lista de repuestos", "La lista de cierre es la última verificación antes de la entrega."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿para qué sirve capacitar al operador?", "Para que use el equipo de manera segura", "Para reemplazar el protocolo", "Para aumentar la velocidad del equipo", "La capacitación reduce errores de uso."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿quién aprueba la entrega del equipo?", "El jefe de mantenimiento", "El operador", "El proveedor de repuestos", "El jefe de mantenimiento autoriza el traspaso."),
        ("=", "{F} ¿Cuántos puntos de la lista de cierre cumple el equipo E-1?", "6", "E-1 cumple todos los puntos de la lista.", " puntos"),
        ("=", "{F} ¿Cuántos puntos de la lista de cierre cumple el equipo E-2?", "2", "Solo las mediciones y la hoja de vida están cumplidas.", " puntos"),
        ("=", "{F} ¿Cuántos puntos pendientes tiene E-2?", "6-2", "Se resta lo cumplido al total.", " puntos"),
        ("abc", "{F} ¿Qué equipo puede entregarse?", "E-1, porque cumple todos los puntos", "E-2, porque sus mediciones cumplen", "Ambos, porque las mediciones cumplen", "La entrega exige todos los puntos."),
        ("abc", "{F} En E-2, ¿qué pendiente afecta la validez de las mediciones?", "El instrumento con certificado vencido", "La capacitación al operador", "La hoja de vida", "Un instrumento vencido deja las mediciones en duda."),
        ("abc", "{F} En E-2, ¿qué pendiente se relaciona con la norma ambiental?", "El aceite usado sin gestionar", "La firma del protocolo", "La capacitación", "El aceite usado es un residuo que se gestiona."),
        ("abc", "{F} Un jefe dice: «E-2 cumple las mediciones, entreguémoslo y completamos después». ¿Qué respuesta es correcta?", "No corresponde: faltan puntos de la lista de cierre, y se entrega al completarlos", "Corresponde, porque las mediciones son lo principal", "Corresponde, si el cliente lo pide", "La lista exige cumplir todo antes de entregar."),
        ("abc", "{F} ¿Qué pendientes de E-2 se priorizan?", "El instrumento vencido y el aceite sin gestionar, y luego las firmas y la capacitación", "Solo las firmas", "Solo la capacitación", "Primero lo que afecta la validez y el ambiente."),
        ("=", "{F} Si E-2 resuelve 3 de sus pendientes, ¿cuántos puntos pendientes le quedan?", "4-3", "Se resta lo resuelto a los pendientes.", " punto"),
        ("Si cada punto pendiente toma 1 jornada de una persona, ¿cuántas jornadas toma cerrar los pendientes de E-2?", "4 jornadas", "E-2 tiene 4 puntos pendientes y cada uno toma 1 jornada."),
    ],
    ctx=("abc", "El cliente de ejemplo quiere el equipo E-2 hoy, aunque faltan firmas y el instrumento está vencido. ¿Qué propones?", "Explicar los pendientes, cerrarlos con personal autorizado y entregar solo con la lista completa", "Entregarlo hoy", "Firmar los puntos sin hacerlos", "No se firma lo que no se verificó."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuántos puntos de la lista deben cumplirse para entregar?", "Todos", "La entrega exige la lista completa."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se prioriza entre los pendientes?", "Lo que afecta la seguridad o la validez de las mediciones", "Después se resuelve lo documental y administrativo."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué aprueba la entrega?", "El jefe de mantenimiento", "Es quien autoriza el traspaso del equipo."),
    ],
    op=("Ficha de ejemplo: equipo E-3: mediciones cumplen; protocolo firmado en 5 de 6 puntos; instrumentos con certificado vigente; capacitación realizada; residuos sin gestionar; hoja de vida actualizada. Lista de cierre de 6 puntos. Escribe (a) cuántos puntos cumple E-3 en total, (b) cuántos pendientes tiene, (c) qué pendientes son, (d) si se entrega y por qué.",
        "(a) Cumple 4: mediciones, instrumentos, capacitación y hoja de vida. (b) 2 pendientes. (c) El protocolo con una firma faltante y los residuos sin gestionar. (d) No se entrega, porque la lista exige cumplir todos los puntos.",
        ["cuenta los puntos cumplidos", "calcula los pendientes", "nombra los pendientes", "decide la entrega"],
        ["hoja con las cuatro respuestas"],
        ["considerar cumplido un protocolo con una firma faltante", "entregar con pendientes", "olvidar los residuos"],
        "Pregunta: «¿el protocolo está completo o le falta una firma?». Si duda, pídele que relea el enunciado."),
    reinforce="Inventa una lista de cierre de cuatro puntos y evalúa dos equipos distintos.",
    extend="Explica con un ejemplo por qué la capacitación al operador forma parte del cierre de una puesta en marcha.",
)

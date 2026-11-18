"""Forestal TP 3.º y 4.º medio: OAE-09 (registro del manejo y la producción forestal en formato digital: planillas descritas por escrito, indicadores de gestión). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O9 = "TP-FORE-3y4-OAE-09"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Forestal Demo» registra la producción en una planilla digital con las columnas: fecha, rodal, labor, volumen (en m³) y responsable. "
     "Registros de producción de tres días seguidos: lunes, 24 m³; martes, 30 m³; miércoles, 18 m³. En otra planilla se anotan datos personales del personal, como nombre y teléfono. "
     "Se hacen 3 labores por día durante 5 días, y cada labor ocupa una fila de la planilla.")
build(
    O9, 1, F,
    use="Aprenderé por qué se registra la producción en forma digital, qué es un formato establecido, qué cuidados exige un registro (datos personales, claves y respaldo) y qué pausas necesita el trabajo frente a una pantalla.",
    prior=["Sé qué es un registro en papel.", "Sé sumar y dividir números enteros.", "Sé qué es un indicador."],
    explain=[
        "Un registro digital es información anotada en un archivo electrónico, como una planilla, con un formato definido. El formato establecido es la estructura fija que dice qué columnas, qué unidades y qué tipo de fecha se usan, y es el mismo para todas las personas, para poder sumar, comparar y controlar la gestión. Un registro útil dice qué se hizo, cuánto, cuándo y quién lo anotó. Un dato mal registrado es peor que uno faltante, porque lleva a decisiones equivocadas con apariencia de verdad.",
        "El registro exige cuidados. Los datos personales, como el nombre o el teléfono, identifican a una persona y se protegen: se registran solo los necesarios y solo los ven quienes deben. Cada persona usa su propia clave y nunca la comparte. El respaldo es una copia de los datos guardada aparte para poder recuperarlos si se pierden. Trabajar frente a una pantalla exige pausas breves periódicas y una postura cómoda para cuidar la vista y el cuerpo.",
        f"En esta clase solo se trabaja con planillas descritas por escrito; no hace falta ningún programa. {EMER} {AVISO}",
    ],
    vocab=[("registro digital", "información anotada en un archivo electrónico con un formato definido"), ("formato establecido", "estructura fija de columnas, unidades y fechas que todos usan"), ("datos personales", "datos que identifican a una persona, como nombre o teléfono"), ("respaldo", "copia de los datos guardada aparte para recuperarlos si se pierden"), ("ergonomía", "cuidado de la postura y de las pausas para evitar molestias en el cuerpo")],
    worked=[
        ("Sumar registros", "Tres registros de producción de ejemplo son 15 m³, 20 m³ y 25 m³. ¿Cuántos m³ suman?", ["Se suman los tres volúmenes.", "15 + 20 + 25 = 60."], "60 m³"),
        ("Qué es un dato personal", "En una planilla de ejemplo hay una columna «teléfono del trabajador». ¿Es un dato personal?", ["Un teléfono identifica a una persona.", "Por eso es un dato personal y se protege."], "Sí, es un dato personal"),
    ],
    mistakes=[("Compartir la clave de la planilla para «ahorrar tiempo».", "Con una clave compartida no se sabe quién anotó o cambió un dato.", "Cada persona usa su propia clave."),
              ("Guardar el respaldo en el mismo equipo que el archivo original.", "Si el equipo falla o se pierde, se pierden ambos.", "El respaldo se guarda en otro lugar.")],
    T=[
        ("abc", "En Forestal: ¿qué es un registro digital de producción?", "Información anotada en un archivo electrónico con un formato definido", "Papel guardado en una caja del taller", "Una fotografía de la faena sin ningún dato", "Un registro digital es un archivo electrónico con un formato; el papel o la foto no lo son."),
        ("abc", "En Forestal: ¿qué es un formato establecido para una planilla?", "La estructura fija de columnas, unidades y fechas que todos usan", "Una planilla distinta que cada persona arma a su manera", "El tamaño de la pantalla del computador", "El formato establecido permite sumar y comparar registros de distintas personas."),
        ("abc", "En Forestal: ¿qué son los datos personales de una planilla?", "Los datos que identifican a una persona, como nombre y teléfono", "Los datos del volumen producido por un rodal", "Los datos de la fecha del registro", "Los datos personales identifican a alguien; el volumen y la fecha no."),
        ("=", "{F} ¿Cuántos m³ suman los tres días registrados?", "24+30+18", "Se suman los volúmenes de los tres días.", " m³"),
        ("=", "{F} ¿Cuál es el promedio diario de producción de los tres días?", "(24+30+18)//3", "Se suman los volúmenes y se dividen entre los 3 días.", " m³"),
        ("abc", "{F} ¿Qué columna de la planilla indica la unidad con que se mide la producción?", "La columna de volumen, que está en m³", "La columna de responsable", "La columna de rodal", "El encabezado de volumen indica que se mide en metros cúbicos."),
        ("abc", "{F} ¿Qué es una copia de seguridad o respaldo?", "Una copia de los datos guardada aparte para recuperarlos si se pierden", "El mismo archivo guardado con otro nombre en el mismo equipo", "Una impresión que se archiva", "El respaldo debe estar separado para servir si el original se pierde."),
        ("abc", "{F} Un compañero propone compartir su clave con todos para ahorrar tiempo. ¿Qué respuesta es correcta?", "No: cada persona usa su propia clave para saber quién anotó cada dato", "Sí, si es una clave larga", "Sí, si todos son del mismo equipo", "Una clave compartida impide saber quién hizo cada cambio."),
        ("abc", "{F} ¿Deben incluirse el nombre y el teléfono del personal en la planilla de producción?", "No: se registran solo los datos necesarios y los personales se protegen", "Sí, porque más datos siempre ayudan", "Sí, para que cualquiera pueda llamar", "La producción no necesita datos personales, y registrarlos sin necesidad aumenta el riesgo."),
        ("abc", "Una persona pasa 4 horas seguidas frente a la pantalla registrando datos. ¿Qué recomendación de ergonomía corresponde?", "Hacer pausas breves periódicas y mantener una postura cómoda", "Seguir sin pausas para terminar antes", "Acercar la pantalla lo más posible a los ojos", "Las pausas y la postura cuidan la vista y el cuerpo."),
        ("abc", "En Forestal: ¿por qué un dato mal registrado puede ser peor que un dato faltante?", "Porque lleva a decisiones equivocadas con apariencia de verdad", "Porque ocupa más espacio en el archivo", "Porque los computadores no aceptan datos mal escritos", "Un dato falso engaña a quien decide; uno faltante se nota y se corrige."),
        ("=", "{F} ¿Cuántas filas tendrá la planilla al cabo de los 5 días?", "3*5", "Se multiplican las labores por día por los días.", " filas"),
        ("abc", "{F} Si el respaldo se guarda en el mismo equipo que el archivo original, ¿por qué es débil?", "Porque si el equipo falla o se pierde, se pierden ambos", "Porque el respaldo se corrompe siempre", "Porque un respaldo no sirve para recuperar datos", "Separar el respaldo del original evita perder todo a la vez."),
    ],
    ctx=("abc", "Un compañero te pide tu clave para «corregir» un dato de producción de ayer. ¿Qué respondes?", "Que no compartes tu clave, y que avisas a un adulto responsable para que se corrija con registro", "Que se la das, si es solo por hoy", "Que se la das, si cambia la clave después", "Una clave compartida impide saber quién cambió el dato."),
    sc=[
        ("En Forestal: ¿qué es un registro digital?", "Información anotada en un archivo electrónico con un formato definido", "El formato permite ordenar y comparar los datos."),
        ("En el trabajo forestal: ¿qué es un dato personal?", "Un dato que identifica a una persona, como nombre o teléfono", "Los datos personales se protegen porque identifican a las personas."),
        ("En el trabajo forestal: ¿para qué sirve un respaldo?", "Para recuperar los datos si se pierden", "El respaldo guarda una copia aparte."),
    ],
    op=("Ficha de ejemplo: una planilla de la empresa ficticia «Forestal Muestra» tiene las columnas fecha, rodal, labor, volumen (m³) y responsable. Registros de cuatro días: 35, 28, 42 y 31 m³. Se hacen 2 labores por día durante 6 días, una fila por labor. Escribe (a) el volumen total y el promedio diario de los cuatro días, (b) cuántas filas tendrá la planilla en los 6 días, (c) un cuidado que corresponde a los datos personales, (d) una recomendación de ergonomía para quien registra.",
        "(a) 35 + 28 + 42 + 31 = 136 m³; 136 ÷ 4 = 34 m³ por día. (b) 2 × 6 = 12 filas. (c) Registrar solo los datos personales necesarios y protegerlos con claves propias. (d) Hacer pausas breves periódicas y mantener una postura cómoda.",
        ["calcula total y promedio", "calcula las filas", "nombra un cuidado de datos personales", "nombra una recomendación de ergonomía"],
        ["hoja con las cuatro respuestas"],
        ["confundir total con promedio", "proponer compartir la clave", "no proteger los datos personales"],
        "Pregunta: «¿qué dato de una persona sobra en una planilla de producción?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una planilla con cinco columnas y dos filas de datos de producción.",
    extend="Explica con un ejemplo por qué cada persona debe usar su propia clave en un registro.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (planilla descrita por escrito, de ejemplo, inventada). Columnas: fecha, rodal (código R-1, R-2…), labor (texto), volumen (número entero en m³), jornadas (número entero). "
     "Fila 1: día 1, R-1, intervención, 40, 2. Fila 2: día 1, R-2, intervención, 60, 3. Fila 3: día 2, R-1, intervención, 35, 2. Fila 4: día 2, R-3, carguío, 50, 1. Fila 5: día 3, R-2, intervención, 45, 2. "
     "Una bitácora de cambios registra cada corrección: fecha, quién la hizo, valor anterior y valor nuevo.")
build(
    O9, 2, F,
    use="Aprenderé los conceptos de una planilla: filas, columnas, tipos de dato, validación, filtro, suma y bitácora de cambios, y cómo leer una planilla descrita por escrito.",
    prior=["Sé qué es un registro y un formato establecido.", "Sé sumar y dividir números enteros.", "Sé qué es una unidad de medida."],
    explain=[
        "Una planilla organiza los datos en filas y columnas. Una fila es un registro completo de un hecho, por ejemplo una labor de un día. Una columna agrupa datos del mismo tipo, como todas las fechas o todos los volúmenes. Cada columna tiene un tipo de dato: fecha, número o texto, y una unidad si corresponde, que se escribe en el encabezado y no dentro de cada celda. Un código de rodal funciona como identificador: debe ser el mismo en todas las filas que se refieren al mismo rodal.",
        "La validación es una regla que impide o avisa datos imposibles o fuera de formato, como un volumen negativo. Un filtro muestra solo las filas que cumplen una condición, y una suma o un promedio calculan sobre una columna. Cuando se corrige un dato, no se borra el valor anterior sin dejar rastro: se anota en una bitácora de cambios con fecha, responsable y los valores antes y después. Así el registro se puede revisar y confiar en él.",
        f"No hace falta ningún programa: la planilla está descrita por escrito. {EMER} {AVISO}",
    ],
    vocab=[("fila", "registro completo de un hecho en una planilla"), ("columna", "conjunto de datos del mismo tipo en una planilla"), ("validación", "regla que impide o avisa datos imposibles o fuera de formato"), ("filtro", "función que muestra solo las filas que cumplen una condición"), ("identificador", "código que identifica de manera única a un elemento, como un rodal"), ("bitácora de cambios", "registro de cada corrección con fecha, responsable y valores antes y después")],
    worked=[
        ("Suma de una columna", "Una columna de volumen de ejemplo tiene 10, 25 y 15. ¿Cuánto suma?", ["Se suman los tres valores de la columna.", "10 + 25 + 15 = 50."], "50 m³"),
        ("Usar un filtro", "En una planilla de ejemplo, un filtro muestra solo las filas con labor «carguío». Hay 2 filas con 20 y 30 m³. ¿Cuánto suman?", ["Solo se consideran las filas filtradas.", "20 + 30 = 50."], "50 m³"),
    ],
    mistakes=[("Escribir la unidad dentro de cada celda numérica, como «40 m³».", "La planilla puede interpretar la celda como texto y no sumarla.", "La unidad va en el encabezado y la celda lleva solo el número."),
              ("Corregir un dato sin dejar rastro de lo que había antes.", "No se puede revisar qué cambió ni quién lo hizo.", "Se anota en la bitácora de cambios.")],
    T=[
        ("abc", "En Forestal: ¿qué es una fila en una planilla de producción?", "Un registro completo de un hecho, como una labor de un día", "El conjunto de datos del mismo tipo", "El nombre del archivo de la planilla", "Una fila agrupa todos los datos de un mismo hecho."),
        ("abc", "En Forestal: ¿qué es una columna en una planilla?", "Un conjunto de datos del mismo tipo, como todos los volúmenes", "Un registro completo de una labor", "El título del informe", "Una columna agrupa datos del mismo campo."),
        ("abc", "En Forestal: ¿qué es la validación de datos de una planilla?", "Una regla que impide o avisa datos imposibles o fuera de formato", "Una revisión de la ortografía del informe", "La copia de seguridad del archivo", "La validación detecta errores al ingresar datos, como un volumen negativo."),
        ("=", "{F} ¿Cuántos m³ suman las filas del rodal R-1?", "40+35", "Se suman los volúmenes de las filas del rodal R-1.", " m³"),
        ("=", "{F} ¿Cuántos m³ suman las filas del rodal R-2?", "60+45", "Se suman los volúmenes de las filas del rodal R-2.", " m³"),
        ("=", "{F} ¿Cuántos m³ suma toda la columna de volumen?", "40+60+35+50+45", "Se suman los volúmenes de las cinco filas.", " m³"),
        ("=", "{F} ¿Cuántas jornadas suma la columna de jornadas?", "2+3+2+1+2", "Se suman las jornadas de las cinco filas.", " jornadas"),
        ("=", "{F} ¿Cuántos m³ por jornada se registraron en promedio en toda la planilla?", "(40+60+35+50+45)//(2+3+2+1+2)", "Se divide el volumen total entre las jornadas totales.", " m³ por jornada"),
        ("abc", "{F} ¿Qué regla de validación es adecuada para la columna de volumen?", "Aceptar solo números enteros mayores que cero", "Aceptar cualquier texto", "Aceptar números negativos", "Un volumen debe ser un número positivo; un texto o un negativo es imposible."),
        ("abc", "{F} Alguien anota un volumen de 4.000 en lugar de 40 en una fila. ¿Qué corresponde?", "Marcarlo como atípico y verificarlo con quien lo anotó", "Borrar la fila sin avisar", "Aceptarlo porque la planilla lo permite", "Un valor muy distinto de los demás se verifica antes de aceptarlo."),
        ("abc", "{F} Se corrige un volumen de 45 a 54 por un error de digitación. ¿Qué debe quedar en la bitácora de cambios?", "La fecha, quién lo hizo y los valores 45 y 54", "Solo el valor nuevo, 54", "Nada, porque es una corrección", "La bitácora conserva el valor anterior y quién lo cambió."),
        ("=", "{F} Si se filtra solo la labor «intervención», ¿cuántos m³ suman las filas filtradas?", "40+60+35+45", "Se suman los volúmenes de las filas que tienen labor intervención.", " m³"),
        ("abc", "{F} Una persona quiere borrar la fila con un dato dudoso para que los totales «cuadren». ¿Qué respuesta es correcta?", "No: se verifica el dato y se corrige dejando constancia, sin borrar para que cuadre", "Sí, si los totales quedan más ordenados", "Sí, si nadie se da cuenta", "Borrar para que cuadre oculta el problema y rompe la trazabilidad."),
    ],
    ctx=("abc", "Un compañero te pide cambiar una fecha de la planilla para que un atraso «no se note», sin dejar registro. ¿Qué respondes?", "Que no, porque los cambios se anotan en la bitácora y no se ocultan, y que avisas a un adulto responsable", "Que sí, si es un cambio pequeño", "Que sí, si lo haces cuando nadie mire", "Cambiar datos sin registro oculta la realidad."),
    sc=[
        ("En Forestal: ¿qué es una columna?", "Un conjunto de datos del mismo tipo", "Cada columna tiene su tipo de dato y su unidad."),
        ("¿Dónde se escribe la unidad de una columna numérica?", "En el encabezado de la columna", "La celda debe llevar solo el número."),
        ("¿Para qué sirve la bitácora de cambios?", "Para dejar constancia de cada corrección con fecha y responsable", "Permite revisar qué cambió y quién lo cambió."),
    ],
    op=("Ficha de ejemplo: planilla con columnas fecha, rodal, labor, volumen (m³), jornadas. Fila 1: día 1, R-4, intervención, 30, 2. Fila 2: día 1, R-5, carguío, 48, 2. Fila 3: día 2, R-4, intervención, 36, 3. Fila 4: día 3, R-5, carguío, 30, 1. Escribe (a) el volumen total, (b) el volumen de las filas con labor «carguío», (c) el rendimiento promedio en m³ por jornada, (d) qué se anota en la bitácora si se corrige el 36 a 38.",
        "(a) 30 + 48 + 36 + 30 = 144 m³. (b) 48 + 30 = 78 m³. (c) 144 ÷ 8 jornadas = 18 m³ por jornada. (d) La fecha, quién lo corrigió y los valores 36 y 38.",
        ["suma bien la columna", "aplica un filtro", "calcula el rendimiento", "describe la bitácora"],
        ["hoja con las cuatro respuestas"],
        ["no filtrar por labor", "olvidar dividir por las jornadas totales", "no dejar constancia de la corrección"],
        "Pregunta: «¿qué filas incluye el filtro de carguío?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una planilla de tres filas y calcula la suma de su columna de volumen.",
    extend="Explica con un ejemplo por qué la unidad se escribe en el encabezado y no en cada celda.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (planilla con errores, descrita por escrito, de ejemplo, inventada). Columnas: fecha (día del mes de ejemplo, que tiene 30 días), rodal (códigos válidos del plan: R-1 a R-4), labor, volumen (número entero en m³, mayor que cero), jornadas (número entero). "
     "Fila 1: día 1, R-1, intervención, 40, 2. Fila 2: día 2, R-2, intervención, -30, 2. Fila 3: día 3, R-3, carguío, «50 m³», 3. Fila 4: día 3, R-9, intervención, 20, 1. "
     "Fila 5: día 45, R-1, carguío, 25, 1. Fila 6: día 4, R-4, intervención, 38, 4. Fila 7: día 5, R-2, intervención, 44, 2. Fila 8: día 5, R-3, carguío, 48, 2.")
build(
    O9, 3, F,
    use="Aprenderé a revisar una planilla en papel: encontrar errores de formato y de contenido, calcular con las filas válidas y corregir dejando constancia.",
    prior=["Sé qué son fila, columna, validación y bitácora.", "Sé calcular porcentajes simples.", "Sé sumar y dividir números enteros."],
    explain=[
        "Revisar una planilla es comparar cada fila con las reglas del formato. Los errores más comunes son un valor imposible, como un volumen negativo o una fecha que no existe; un código que no pertenece al plan, como un rodal inexistente; y una celda con texto en una columna numérica, por ejemplo un número escrito junto a su unidad. Estos errores se encuentran con las reglas de validación y revisando la planilla antes de calcular.",
        "Los totales y los promedios se calculan solo con las filas válidas, y las filas con error se separan y se verifican con quien las anotó. No se borran, no se «arreglan» a ojo ni se inventan valores: se corrige con el dato real, dejando constancia en la bitácora. Un dato atípico, muy distinto de los demás, no es necesariamente un error, pero se verifica. Una planilla revisada y corregida da confianza para decidir.",
        f"El análisis se hace en papel con la planilla descrita. {EMER} {AVISO}",
    ],
    vocab=[("fila válida", "fila que cumple todas las reglas del formato"), ("dato imposible", "valor que no puede existir, como un volumen negativo o una fecha que no existe"), ("código inexistente", "código que no pertenece a la lista de códigos válidos del plan"), ("dato atípico", "valor muy distinto de los demás, que conviene verificar"), ("corrección con constancia", "cambio de un dato anotado en la bitácora con fecha, responsable y valores")],
    worked=[
        ("Detectar un error", "En una planilla de ejemplo con rodales válidos de R-1 a R-3 aparece una fila con rodal R-7. ¿Qué error tiene?", ["R-7 no está entre los códigos válidos.", "Es un código inexistente."], "Código de rodal inexistente"),
        ("Calcular con filas válidas", "Una planilla de ejemplo tiene 4 filas válidas con 10, 20, 30 y 40 m³, y una fila con error. ¿Cuánto suman las válidas?", ["Solo se suman las filas válidas.", "10 + 20 + 30 + 40 = 100."], "100 m³"),
    ],
    mistakes=[("Sumar también las filas con errores, sin revisarlas.", "Los totales quedan distorsionados.", "Calcula con las filas válidas y verifica las demás."),
              ("Corregir un dato dudoso por intuición.", "Un valor supuesto falsea el registro.", "Verifica el dato real con quien lo anotó y deja constancia.")],
    T=[
        ("abc", "En Forestal: ¿por qué escribir «50 m³» en una celda de volumen es un problema?", "Porque mezcla texto con número y la planilla puede no sumarlo", "Porque 50 es un valor demasiado grande", "Porque la unidad nunca debe aparecer en una planilla", "La unidad va en el encabezado; la celda debe contener solo el número."),
        ("abc", "En Forestal: ¿qué es un dato atípico?", "Un valor muy distinto de los demás, que conviene verificar", "Un valor que se repite en todas las filas", "El valor más pequeño de la planilla siempre", "Un dato atípico se aleja del patrón y se verifica antes de aceptarlo o corregirlo."),
        ("abc", "En Forestal: ¿qué es un código de rodal inexistente?", "Un código que no está en la lista de códigos válidos del plan", "Un código escrito en mayúsculas", "Un código que se repite en dos filas", "El código no existe si no pertenece a la lista válida del plan."),
        ("=", "{F} ¿Cuántas filas tienen errores?", "8-4", "Se restan las filas válidas al total de filas.", " filas"),
        ("=", "{F} ¿Qué porcentaje de las filas es válido?", "4*100//8", "Se divide las filas válidas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué fila tiene una fecha imposible?", "La fila 5, con día 45", "La fila 3, con día 3", "La fila 7, con día 5", "El mes de ejemplo tiene 30 días; el día 45 no existe."),
        ("abc", "{F} ¿Qué error tiene la fila 4?", "El rodal R-9 no es un código válido del plan", "La fecha no existe", "El volumen es negativo", "Los códigos válidos son de R-1 a R-4; R-9 no pertenece al plan."),
        ("=", "{F} ¿Cuántos m³ suman las filas válidas, que son las filas 1, 6, 7 y 8?", "40+38+44+48", "Se suman los volúmenes de las cuatro filas válidas.", " m³"),
        ("=", "{F} ¿Cuántas jornadas suman las filas válidas?", "2+4+2+2", "Se suman las jornadas de las cuatro filas válidas.", " jornadas"),
        ("=", "{F} ¿Cuántos m³ por jornada se registraron en las filas válidas?", "(40+38+44+48)//(2+4+2+2)", "Se divide el volumen de las filas válidas entre las jornadas de esas filas.", " m³ por jornada"),
        ("abc", "{F} ¿Qué corresponde hacer con la fila 2, de volumen negativo?", "Verificar el dato con quien lo anotó y corregirlo dejando constancia", "Borrar la fila sin avisar", "Cambiar el signo sin consultar", "Un dato imposible se verifica con su fuente y se corrige con constancia."),
        ("abc", "{F} ¿Qué regla de validación evitaría el error de la fila 5?", "Aceptar solo fechas posibles del mes", "Aceptar solo texto en la columna fecha", "Bloquear la columna de rodal", "Una validación de fecha rechaza días que no existen."),
        ("=", "{F} Si, tras verificar, la fila 2 tiene 30 m³ y la fila 3 tiene 50 m³ (las demás no cambian), ¿cuántos m³ suman esas filas con las válidas?", "40+38+44+48+30+50", "Se suman los volúmenes de las filas válidas y de las dos filas corregidas.", " m³"),
    ],
    ctx=("abc", "Un compañero propone cambiar el día 45 por un día cualquiera para que la planilla «se vea bien» antes de enviarla. ¿Qué corresponde?", "Verificar la fecha real con quien anotó la fila y corregir con constancia, avisando a un adulto responsable si hay presión", "Poner el día 30 sin consultar", "Borrar la fila para que no se note", "Un dato supuesto o borrado falsea el registro."),
    sc=[
        ("En Forestal: ¿qué filas se usan para calcular totales?", "Solo las filas válidas, verificando las demás", "Las filas con error distorsionan el cálculo."),
        ("¿Dónde se escribe la unidad en una columna numérica?", "En el encabezado de la columna", "La celda debe llevar solo el número."),
        ("¿Cómo se corrige un dato dudoso?", "Verificándolo con quien lo anotó y dejando constancia", "No se inventan valores ni se borra para que cuadre."),
    ],
    op=("Ficha de ejemplo: planilla con columnas fecha (el mes de ejemplo tiene 30 días), rodal (válidos R-1 a R-3), volumen (entero mayor que cero) y jornadas. Fila 1: día 2, R-1, 30, 2. Fila 2: día 3, R-5, 20, 1. Fila 3: día 4, R-2, 36, 3. Fila 4: día 33, R-3, 28, 2. Fila 5: día 5, R-3, 44, 2. Fila 6: día 6, R-1, -10, 1. Escribe (a) qué errores tienen las filas 2, 4 y 6, (b) cuántas filas son válidas y qué porcentaje es, (c) el volumen y las jornadas de las filas válidas, (d) qué haces con las filas con error.",
        "(a) Fila 2: rodal inexistente; fila 4: fecha imposible; fila 6: volumen negativo. (b) Hay 3 filas válidas de 6: 50 %. (c) 30 + 36 + 44 = 110 m³ y 2 + 3 + 2 = 7 jornadas. (d) Se verifican con quien las anotó, se corrigen con el dato real y se deja constancia en la bitácora.",
        ["identifica los tres errores", "calcula el porcentaje", "suma solo las filas válidas", "describe la corrección con constancia"],
        ["hoja con las cuatro respuestas"],
        ["sumar las filas con error", "inventar un valor", "borrar sin dejar constancia"],
        "Pregunta: «¿qué regla se rompe en cada fila con error?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe tres filas de una planilla con un error cada una y nombra el error.",
    extend="Explica con un ejemplo por qué un dato atípico se verifica antes de corregirlo.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (indicadores de ejemplo, inventados). Meta del mes: 1.200 m³ en 20 jornadas. Resultado real del mes: 1.080 m³ en 24 jornadas. Costo de una jornada: $150.000 (dato de ejemplo). "
     "Regla de semáforo de ejemplo para el cumplimiento del programa: verde, 95 % o más; amarillo, de 85 % a 94 %; rojo, menos de 85 %.")
build(
    O9, 4, F,
    use="Aprenderé a calcular indicadores de gestión con los datos de una planilla: cumplimiento, rendimiento, desviación y semáforo, y a no maquillar los resultados.",
    prior=["Sé calcular porcentajes simples.", "Sé qué es un registro y una planilla.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un indicador de gestión es un dato calculado que mide el avance frente a una meta. El cumplimiento del programa es el porcentaje de lo programado que se logró: lo real dividido por lo programado, por 100. El rendimiento es lo producido por jornada. La desviación es la diferencia entre lo real y lo programado. Con los indicadores se analiza por qué hubo diferencias y qué medidas tomar.",
        "El semáforo clasifica un indicador en verde, amarillo o rojo según una regla fijada por la empresa. Los resultados se informan tal como son, con la planilla como respaldo. No se ajustan los datos para pasar de color: maquillar un indicador oculta problemas y lleva a malas decisiones. Si una diferencia no se explica, se investiga antes de concluir. Los datos de esta clase son de ejemplo.",
        f"El análisis lo hace la jefatura con los registros; tú practicas los cálculos. {EMER} {AVISO}",
    ],
    vocab=[("indicador de gestión", "dato calculado que mide el avance frente a una meta"), ("cumplimiento del programa", "porcentaje de lo programado que se logró"), ("desviación", "diferencia entre lo real y lo programado"), ("semáforo", "clasificación en verde, amarillo o rojo según una regla"), ("maquillar un indicador", "ajustar los datos para que el resultado se vea mejor sin que lo sea")],
    worked=[
        ("Cumplimiento", "Una meta de ejemplo era 500 m³ y se lograron 450 m³. ¿Cuál es el cumplimiento?", ["450 ÷ 500 son 90 de cada 100.", "El cumplimiento es 90 %."], "90 %"),
        ("Rendimiento", "Se produjeron 360 m³ en 12 jornadas. ¿Cuál es el rendimiento?", ["Se divide lo producido entre las jornadas.", "360 ÷ 12 = 30."], "30 m³ por jornada"),
    ],
    mistakes=[("Ajustar el dato de producción para pasar de amarillo a verde.", "Maquillar un indicador oculta problemas reales.", "Se informa el resultado real y se analizan las causas."),
              ("Mirar solo el cumplimiento y olvidar el rendimiento.", "Se puede cumplir una meta usando más jornadas, lo que sube el costo.", "Revisa varios indicadores a la vez.")],
    T=[
        ("abc", "En Forestal: ¿qué es un indicador de gestión?", "Un dato calculado que mide el avance frente a una meta", "Una opinión del jefe sobre el trabajo", "Una fotografía de la faena", "Un indicador es un dato medible comparado con una meta."),
        ("abc", "En Forestal: ¿qué es el cumplimiento del programa?", "El porcentaje de lo programado que se logró", "El total producido sin compararlo con nada", "El costo de las jornadas del mes", "El cumplimiento compara lo logrado con lo programado."),
        ("abc", "En Forestal: ¿qué es una desviación?", "La diferencia entre lo real y lo programado", "Un error de ortografía en la planilla", "La meta que se fija para el próximo mes", "La desviación mide cuánto se alejó el resultado de lo programado."),
        ("=", "{F} ¿Cuál es el cumplimiento de la producción del mes?", "1080*100//1200", "Se divide lo real entre lo programado y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál era el rendimiento programado, en m³ por jornada?", "1200//20", "Se divide la producción programada entre las jornadas programadas.", " m³ por jornada"),
        ("=", "{F} ¿Cuál fue el rendimiento real, en m³ por jornada?", "1080//24", "Se divide la producción real entre las jornadas reales.", " m³ por jornada"),
        ("=", "{F} ¿Cuántos m³ faltaron respecto de lo programado?", "1200-1080", "Se resta la producción real a la programada.", " m³"),
        ("=", "{F} ¿Cuántas jornadas más se usaron que las programadas?", "24-20", "Se restan las jornadas programadas a las reales.", " jornadas"),
        ("=", "{F} ¿Cuántos pesos más costaron las jornadas reales que las programadas?", "(24-20)*150000", "Se multiplican las jornadas adicionales por el costo de cada una.", " pesos"),
        ("abc", "{F} Según la regla del semáforo, ¿qué color tiene el cumplimiento del mes?", "Amarillo, porque 90 % está entre 85 % y 94 %", "Verde, porque supera el 85 %", "Rojo, porque no llegó al 100 %", "El semáforo usa rangos: 90 % cae en el amarillo."),
        ("=", "{F} ¿En qué porcentaje cayó el rendimiento real respecto del programado?", "(60-45)*100//60", "Se calcula la diferencia entre ambos rendimientos y se divide por el programado.", " %"),
        ("abc", "{F} Alguien propone anotar 1.140 m³ en vez de 1.080 para pasar a verde. ¿Qué respuesta es correcta?", "No: se informa el dato real y se analizan las causas del resultado", "Sí, porque la diferencia es pequeña", "Sí, si el jefe lo autoriza de palabra", "Maquillar el dato oculta los problemas y lleva a malas decisiones."),
        ("=", "{F} ¿Cuántos m³ más se habrían necesitado para llegar al 95 % de cumplimiento?", "1200*95//100-1080", "Se calcula el 95 % de lo programado y se resta lo producido.", " m³"),
    ],
    ctx=("abc", "Alguien te pide enviar la planilla con nombres y teléfonos del personal a una persona externa «para un estudio», sin autorización de la empresa. ¿Qué respondes?", "Que no, porque los datos personales se protegen, y que lo consultarás con un adulto responsable", "Que sí, si el estudio es interesante", "Que sí, si borras solo los teléfonos", "Los datos personales no se entregan sin autorización ni necesidad."),
    sc=[
        ("En Forestal: ¿cómo se calcula el cumplimiento?", "Lo real dividido por lo programado, por 100", "Compara lo logrado con la meta."),
        ("¿Cómo se calcula el rendimiento?", "La producción dividida por las jornadas", "Mide lo producido por cada jornada."),
        ("¿Se puede ajustar un dato para cambiar el color del semáforo?", "No, se informa el dato real", "Maquillar un dato oculta los problemas."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): meta del mes de 800 m³ en 10 jornadas; resultado real de 720 m³ en 12 jornadas; costo de una jornada $100.000. Semáforo: verde, 95 % o más; amarillo, de 85 % a 94 %; rojo, menos de 85 %. Escribe (a) el cumplimiento y su color, (b) el rendimiento programado y el real, (c) cuántos pesos más costaron las jornadas reales, (d) qué haces si el jefe pide anotar 760 m³ para llegar a verde.",
        "(a) 720 ÷ 800 = 90 %, amarillo. (b) Programado: 800 ÷ 10 = 80 m³ por jornada; real: 720 ÷ 12 = 60 m³ por jornada. (c) (12 − 10) × 100.000 = 200.000 pesos. (d) No se ajusta el dato: se informa 720 m³ y se analizan las causas, y se avisa a un adulto responsable si hay presión.",
        ["calcula el cumplimiento y el color", "calcula los dos rendimientos", "calcula el costo adicional", "no maquilla el dato"],
        ["hoja con las cuatro respuestas"],
        ["usar el rango equivocado del semáforo", "dividir mal el rendimiento", "aceptar el ajuste del dato"],
        "Pregunta: «¿qué pasa con las decisiones si el dato es falso?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una meta y un resultado real y calcula el cumplimiento.",
    extend="Explica con un ejemplo por qué cumplir la meta de producción con más jornadas no es necesariamente un buen resultado.",
)

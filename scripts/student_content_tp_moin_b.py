"""Montaje Industrial TP 3.º y 4.º medio: OAE-04 (unir y reparar elementos metálicos: conceptos y documentos), OAE-05 (tratamientos de protección) y OAE-06 (equipos de levante: conceptos y cálculo en papel). Sin procedimientos operativos."""
from __future__ import annotations

from tp_moin_common import AVISO, EMER, build

O4 = "TP-MOIN-3y4-OAE-04"
O5 = "TP-MOIN-3y4-OAE-05"
O6 = "TP-MOIN-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller ficticio «Metal Demo» recibe una orden de trabajo: unir 8 pares de perfiles con soldadura de arco y reparar 3 piezas fisuradas. El taller estima 2 horas de trabajo calificado "
     "por cada unión o reparación (dato de ejemplo). Riesgos anotados en la orden: quemaduras, radiación del arco, humos metálicos, chispas cerca de materiales combustibles, gases a presión, descarga eléctrica y ruido.")
build(
    O4, 1, F,
    use="Aprenderé qué tipos de unión de elementos metálicos existen, qué peligros tienen la soldadura y el corte térmico, cómo se controlan y por qué solo personal calificado puede hacerlos.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un permiso de trabajo.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "Los elementos metálicos de un montaje se unen de dos maneras. En la unión soldada, el calor funde el metal de las piezas, o el de un material de aporte, y al enfriarse quedan unidas. En la unión mecánica se usan pernos, tuercas o remaches, sin fundir las piezas. El corte térmico separa metal con calor. Los procesos se nombran por su técnica: arco manual con electrodo, TIG, MIG, MAG y oxigás. Aquí solo se conocen sus nombres y sus riesgos: ejecutarlos exige calificación.",
        "Los peligros son la radiación luminosa del arco, que daña ojos y piel; los humos metálicos, que dañan los pulmones; las chispas y el calor, que provocan quemaduras e incendios; los gases a presión, que pueden fugarse o explotar; y la descarga eléctrica. Se controlan con la jerarquía de controles: extracción de humos y barreras (ingeniería), permiso de trabajo en caliente y orden en el lugar (administrativos) y careta con filtro, guantes, ropa resistente y protección respiratoria (EPP). Los restos de electrodo, la escoria y los humos son residuos y emisiones que se gestionan por el cuidado del medio ambiente.",
        f"Solo un soldador calificado, con permiso de trabajo y bajo la norma vigente de la entidad fiscalizadora, puede soldar o cortar. {EMER} {AVISO}",
    ],
    vocab=[("unión soldada", "unión en que el calor funde el metal y las piezas quedan unidas al enfriarse"), ("unión mecánica", "unión con pernos, tuercas o remaches, sin fundir las piezas"), ("corte térmico", "separación del metal usando calor"), ("permiso de trabajo en caliente", "documento que autoriza tareas con llama, chispas o calor intenso y fija sus condiciones"), ("radiación del arco", "luz intensa del arco que daña ojos y piel"), ("soldador calificado", "persona con certificado vigente que acredita que puede soldar según un procedimiento")],
    worked=[
        ("Clasificar una unión", "Dos placas de ejemplo se unen con pernos y tuercas. ¿Es una unión soldada o mecánica?", ["Hay pernos y tuercas.", "No se funde el metal: es mecánica."], "Unión mecánica"),
        ("Horas de trabajo", "Una orden de ejemplo tiene 5 uniones de 3 horas cada una. ¿Cuántas horas de trabajo calificado son?", ["Se multiplica la cantidad de uniones por las horas de cada una.", "5 por 3 son 15."], "15 horas"),
    ],
    mistakes=[("Creer que saber qué es una soldadura habilita para soldar.", "Soldar exige calificación, instructor, norma vigente, permiso y EPP.", "Aprende aquí los conceptos y deja la tarea a personal calificado."),
              ("Mirar el arco «solo un momento» sin protección.", "La radiación daña los ojos y la piel aunque la exposición sea corta.", "Quien no trabaja en la soldadura se mantiene fuera de la zona señalizada.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una unión soldada?", "Una unión en que el calor funde el metal y las piezas quedan unidas al enfriarse", "Una unión hecha con pernos y tuercas", "Una unión pegada con una cinta especial", "La soldadura une fundiendo metal; los pernos hacen una unión mecánica."),
        ("abc", "En Montaje Industrial: ¿qué es un permiso de trabajo en caliente?", "Un documento que autoriza tareas con llama, chispas o calor intenso y fija sus condiciones", "Un registro de la temperatura de la pieza", "Un certificado de calibración de un instrumento", "El permiso autoriza y condiciona la tarea; no mide temperaturas ni calibra."),
        ("abc", "En Montaje Industrial: ¿qué peligro de la soldadura de arco daña ojos y piel aunque no se toque la pieza?", "La radiación luminosa del arco", "El ruido de la máquina", "El peso de la pieza", "La luz del arco produce lesiones sin contacto; el ruido y el peso son otros peligros."),
        ("=", "{F} ¿Cuántas horas de trabajo calificado estima el taller para toda la orden, sumando uniones y reparaciones?", "(8+3)*2", "Se suman las 8 uniones y las 3 reparaciones y se multiplican por las horas de cada una.", " horas"),
        ("abc", "{F} ¿Qué riesgo de la orden se previene con una extracción de humos?", "Respirar humos metálicos", "Las quemaduras por contacto", "El ruido de la máquina", "La extracción retira los humos del aire que respira la persona."),
        ("abc", "{F} Una extracción que retira los humos del lugar de trabajo es un control de tipo:", "De ingeniería, porque cambia el lugar de trabajo", "Administrativo, porque es una regla", "De EPP, porque protege a la persona", "Una instalación física que limpia el aire es un control de ingeniería."),
        ("abc", "{F} ¿Qué documento debe existir antes de que personal calificado haga trabajos con chispas?", "Un permiso de trabajo en caliente emitido por la persona responsable", "La firma de un estudiante que mira", "Una fotografía del lugar", "El permiso fija las condiciones y deja un responsable."),
        ("=", "{F} Si la hora de trabajo calificado cuesta $12.000 (valor de ejemplo), ¿cuánto cuesta el trabajo de toda la orden?", "(8+3)*2*12000", "Se multiplican las horas totales de la orden por el valor de cada hora.", " pesos"),
        ("abc", "En un taller de ejemplo hay un cilindro de gas caído y huele a gas. ¿Qué corresponde según las reglas generales?", "Alejarte, avisar a un adulto responsable y a emergencias, y no accionar nada", "Levantarlo rápido para que no se golpee", "Cerrar la puerta y seguir trabajando", "Un posible escape de gas es un riesgo grave; se avisa a quienes pueden actuar."),
        ("abc", "{F} Un compañero dice: «sé qué es la soldadura, así que puedo arreglar la reja de mi casa». ¿Qué respuesta es correcta?", "Es falso: soldar exige calificación, instructor, norma vigente y EPP; este cuaderno no habilita para hacerlo", "Es cierto, si usa careta", "Es cierto, si lo hace al aire libre", "Conocer el concepto no basta; la tarea requiere formación y autorización."),
        ("abc", "En una orden de ejemplo se propone cambiar una unión soldada por una unión con pernos para evitar chispas en una zona con material combustible. ¿A qué nivel de la jerarquía de controles se parece más?", "A uno de los primeros niveles, eliminar o sustituir, porque cambia el proceso peligroso", "A un control administrativo", "Al EPP", "Cambiar el proceso por otro de menor peligro actúa sobre la fuente."),
        ("=", "{F} Con 2 personas calificadas trabajando a la vez, ¿cuántas horas de calendario tarda la orden de la ficha?", "(8+3)*2//2", "Se divide el trabajo total entre las dos personas.", " horas"),
        ("abc", "{F} Un compañero propone retirar la extracción de humos «para ganar espacio» y terminar antes. ¿Qué respuesta es correcta?", "No: quitar un control de ingeniería aumenta el riesgo; se mantienen los controles", "Sí, si todos usan casco", "Sí, si la orden es urgente", "El apuro no justifica retirar un control que protege la salud."),
    ],
    ctx=("abc", "Un vecino de ejemplo te ofrece pagarte por soldar una reja en su patio «porque estudias montaje». ¿Qué respondes?", "Que no, porque soldar exige calificación, norma vigente y EPP, y que se contrate a personal calificado", "Que sí, si trabajas con cuidado", "Que sí, pero solo con tus guantes del colegio", "Estudiar conceptos no te habilita; la tarea es de personal calificado."),
    sc=[
        ("En Montaje Industrial: ¿qué diferencia hay entre una unión soldada y una mecánica?", "La soldada funde el metal; la mecánica usa pernos, tuercas o remaches", "Una une con calor y la otra con piezas de unión."),
        ("¿Qué peligro de la soldadura se controla con una extracción de humos?", "Los humos metálicos que se respiran", "La extracción retira el humo del aire de trabajo."),
        ("¿Quién puede soldar en una obra?", "Personal calificado, con permiso, norma vigente y EPP", "La calificación y el permiso son requisitos antes de soldar."),
    ],
    op=("El taller ficticio «Metal Demo» tiene una orden de ejemplo: 6 uniones soldadas y 2 reparaciones, de 3 horas de trabajo calificado cada una. Riesgos: humos, chispas cerca de cartón y radiación del arco. Escribe (a) las horas totales, (b) un control de ingeniería para los humos, (c) un control administrativo para las chispas cerca del cartón, (d) quién puede hacer el trabajo.",
        "(a) (6 + 2) × 3 = 24 horas. (b) Una extracción de humos del lugar. (c) Un permiso de trabajo en caliente que fije las condiciones y que el cartón se mantenga fuera de la zona. (d) Un soldador calificado, con permiso, norma vigente y EPP; no un estudiante.",
        ["calcula las horas totales", "propone un control de ingeniería", "propone un control administrativo", "indica quién hace el trabajo"],
        ["hoja con las cuatro respuestas"],
        ["sumar solo las uniones", "proponer solo EPP", "decir que un estudiante puede soldar"],
        "Pregunta: «¿qué control actúa sobre el lugar y no sobre la persona?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe tres peligros de la soldadura y el tipo de control (ingeniería, administrativo o EPP) que usarías en cada uno.",
    extend="Explica con un ejemplo por qué un permiso de trabajo en caliente no reemplaza a la calificación del soldador.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (planilla de uniones de ejemplo, inventada). U1: a tope, arco manual, posición plana, soldador con calificación vigente, cordón de 400 mm. U2: en T, MIG, posición horizontal, soldador con calificación vigente, cordón de 600 mm. "
     "U3: en T, arco manual, posición vertical, soldador con la calificación vencida, cordón de 300 mm. U4: traslapada, MAG, posición plana, soldador con calificación vigente, cordón de 500 mm.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de las uniones y soldaduras, qué documentos respaldan el trabajo de unión y qué rol cumple cada persona, y a detectar una irregularidad en una planilla.",
    prior=["Sé qué es una unión soldada y una mecánica.", "Sé qué es un permiso de trabajo.", "Sé sumar números enteros."],
    explain=[
        "Las uniones se describen por la posición de las piezas. En la unión a tope, los bordes de dos piezas quedan enfrentados; en la unión en T, una pieza queda perpendicular a la otra; en la unión traslapada, una pieza queda encima de la otra. El cordón es la línea de soldadura. La posición de la unión puede ser plana, horizontal, vertical o sobre la cabeza, y cada una exige calificación propia. Los procesos se nombran por sus siglas: arco manual, TIG, MIG, MAG y oxigás.",
        "El trabajo se respalda con documentos. La especificación técnica del proyecto fija materiales, tipo de unión y exigencias. El procedimiento de soldadura calificado describe el proceso aprobado, y no se reproduce aquí. El certificado de calificación acredita que el soldador puede trabajar con ese procedimiento y esa posición, y tiene fecha de vigencia. El registro de inspección anota si cada cordón cumple. Una discontinuidad es un defecto del cordón, como un poro (un hueco), una grieta o una socavación (un surco junto al cordón). En los planos, el símbolo de soldadura indica el tipo, el tamaño y la ubicación de la unión; no explica cómo ejecutarla.",
        f"Los roles se reparten: el soldador calificado ejecuta, el inspector de soldadura revisa y registra, el supervisor organiza, el prevencionista vela por la seguridad y el ITO revisa que se cumpla el proyecto. {EMER} {AVISO}",
    ],
    vocab=[("unión a tope", "bordes de dos piezas enfrentados"), ("unión en T", "una pieza perpendicular a la otra"), ("unión traslapada", "una pieza sobre la otra"), ("cordón", "línea de soldadura"), ("discontinuidad", "defecto del cordón, como un poro, una grieta o una socavación"), ("certificado de calificación", "documento que acredita que un soldador puede trabajar con un procedimiento y una posición, con fecha de vigencia"), ("inspector de soldadura", "persona que revisa los cordones y registra si cumplen")],
    worked=[
        ("Leer una fila", "Fila de ejemplo: U9, traslapada, arco manual, plana, soldador calificado. ¿Qué tipo de unión es?", ["Se lee la columna del tipo de unión.", "Dice traslapada."], "Traslapada"),
        ("Sumar cordones", "Tres cordones de ejemplo miden 200, 350 y 150 mm. ¿Cuántos mm suman?", ["Se suman las tres longitudes.", "200 más 350 más 150 son 700."], "700 mm"),
    ],
    mistakes=[("Aceptar el trabajo de un soldador con la calificación vencida porque «lo hace bien».", "Sin calificación vigente no hay respaldo de que cumpla el procedimiento.", "Informa al supervisor o al ITO y no se ejecuta hasta regularizar."),
              ("Creer que el símbolo de soldadura de un plano enseña cómo manejar el equipo.", "El símbolo solo indica tipo, tamaño y ubicación de la unión.", "La técnica se aprende con instructor autorizado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una unión a tope?", "Una unión en que los bordes de dos piezas quedan enfrentados", "Una unión en que una pieza queda encima de la otra", "Una unión en que una pieza queda perpendicular a la otra", "A tope significa bordes enfrentados; encima es traslapada y perpendicular es en T."),
        ("abc", "En Montaje Industrial: ¿qué acredita el certificado de calificación de un soldador?", "Que puede soldar con un procedimiento y una posición, hasta una fecha de vigencia", "Que ha trabajado en muchas obras", "Que su equipo está limpio", "El certificado acredita competencia verificada y vigente, no solo experiencia."),
        ("abc", "En Montaje Industrial: ¿qué es una discontinuidad en un cordón?", "Un defecto del cordón, como un poro, una grieta o una socavación", "El lugar donde comienza el cordón", "La separación entre dos piezas antes de unirlas", "Una discontinuidad es una interrupción o defecto dentro o junto al cordón."),
        ("=", "{F} ¿Cuántos milímetros de cordón suman las cuatro uniones de la planilla?", "400+600+300+500", "Se suman las longitudes de cordón de U1, U2, U3 y U4.", " mm"),
        ("abc", "{F} ¿Qué unión de la planilla está en posición vertical?", "U3", "U1", "U4", "La fila de U3 indica posición vertical; U1 y U4 son planas."),
        ("abc", "{F} ¿Qué uniones se ejecutan en posición plana?", "U1 y U4", "U2 y U3", "Solo U1", "La planilla indica posición plana para U1 y para U4."),
        ("abc", "{F} ¿Qué irregularidad de documentos tiene la planilla?", "U3 está asignada a un soldador con la calificación vencida", "U1 es una unión a tope", "U4 es una unión traslapada", "Una calificación vencida impide ejecutar la unión; los tipos de unión no son irregularidades."),
        ("abc", "{F} ¿Qué corresponde con la unión U3?", "No ejecutarla hasta que la haga personal con calificación vigente, y avisar al supervisor o al ITO", "Ejecutarla igual y regularizar la calificación después", "Cambiar la planilla para que diga «vigente»", "Sin calificación vigente no se ejecuta, y los registros no se alteran."),
        ("=", "{F} Si el plano pide además 3 cordones de 250 mm, ¿cuántos milímetros de cordón hay en total?", "400+600+300+500+3*250", "Se suman los cordones de la planilla y los 3 cordones adicionales.", " mm"),
        ("abc", "¿Quién revisa los cordones terminados y registra si cumplen?", "El inspector de soldadura o de calidad", "El mismo soldador sin dejar registro", "El proveedor del electrodo", "La revisión independiente y registrada es función del inspector."),
        ("abc", "{F} Un compañero dice: «el símbolo de soldadura del plano me enseña cómo manejar el equipo». ¿Qué respuesta es correcta?", "Es falso: el símbolo indica tipo, tamaño y ubicación de la unión; manejar el equipo exige calificación e instrucción", "Es cierto, si el símbolo está en la leyenda", "Es cierto, si la unión es plana", "Un símbolo es información de diseño, no una instrucción de manejo."),
        ("abc", "Un informe de ejemplo anota «poro en el cordón de U2». ¿Qué corresponde con ese hallazgo?", "Registrarlo e informar al inspector o al ITO para decidir si se acepta o se repara por personal calificado", "Taparlo con pintura", "Borrarlo del informe", "Un hallazgo se registra y se decide con criterios; ocultarlo es grave."),
        ("=", "El taller de ejemplo inspecciona 4 uniones por hora. ¿Cuántas horas necesita para 3 planillas iguales a la de la ficha, de 4 uniones cada una?", "3*4//4", "Se calcula el total de uniones y se divide entre las que se inspeccionan por hora.", " horas"),
    ],
    ctx=("abc", "Un ayudante de ejemplo te pide: «anota que el soldador está calificado, su certificado venció ayer pero es lo mismo». ¿Qué respondes?", "Que no se puede anotar eso: sin calificación vigente la unión no se ejecuta y se informa al supervisor o al ITO", "Que sí, porque un día no importa", "Que sí, pero con una nota pequeña", "Un certificado vencido no acredita competencia; alterar el registro es una falta grave."),
    sc=[
        ("En Montaje Industrial: ¿qué es la unión en T?", "Una unión en que una pieza queda perpendicular a la otra", "La forma de la unión recuerda a la letra T."),
        ("¿Qué documento acredita que un soldador puede trabajar con cierto procedimiento?", "El certificado de calificación vigente", "La calificación tiene fecha y se verifica."),
        ("¿Qué es un poro en un cordón?", "Un hueco, que es una discontinuidad", "Es un defecto dentro del cordón."),
    ],
    op=("Ficha de ejemplo: planilla de uniones. V1: a tope, TIG, plana, soldador con calificación vigente, cordón de 200 mm. V2: en T, arco manual, sobre la cabeza, soldador con calificación vigente solo para posición plana, cordón de 350 mm. V3: traslapada, MAG, horizontal, soldador con calificación vigente, cordón de 450 mm. Escribe (a) cuántos mm de cordón suma la planilla, (b) qué unión tiene una irregularidad y por qué, (c) qué harías con ella.",
        "(a) 200 + 350 + 450 = 1.000 mm. (b) V2: la posición sobre la cabeza no coincide con la calificación del soldador, que es solo para plana. (c) No ejecutarla hasta que la haga personal calificado en esa posición, y avisar al supervisor o al ITO.",
        ["suma los cordones", "identifica V2 y la causa", "indica qué hacer sin alterar registros"],
        ["hoja con los tres puntos"],
        ["sumar mal", "decir que V1 tiene la irregularidad", "proponer cambiar la planilla"],
        "Pregunta: «¿qué dato de V2 no coincide?». Si no responde, pídele que relea la regla de que la calificación es por posición."),
    reinforce="Escribe una fila de planilla de ejemplo con tipo de unión, proceso, posición, calificación y longitud del cordón.",
    extend="Explica con un ejemplo por qué la fecha de vigencia de un certificado de calificación es importante.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (informe de inspección visual de ejemplo, inventado). K1: 300 mm, sin hallazgos. K2: 400 mm, poro dentro del límite de la especificación. K3: 600 mm, grieta. K4: 300 mm, socavación dentro del límite de la especificación. K5: 400 mm, sin hallazgos. "
     "Criterio de aceptación de ejemplo: no se acepta ninguna grieta; poros y socavaciones se aceptan si están dentro del límite de la especificación. Tarifa de reparación de ejemplo: $18.000 por cada 100 mm de cordón rechazado.")
build(
    O4, 3, F,
    use="Aprenderé a leer un informe de inspección, a aplicar un criterio de aceptación, a calcular el cordón rechazado y su costo y a seguir el ciclo de una no conformidad.",
    prior=["Sé qué es una discontinuidad.", "Sé qué es una no conformidad.", "Sé calcular un porcentaje simple."],
    explain=[
        "Un cordón se inspecciona por una persona calificada para ver si cumple. La inspección visual revisa el aspecto del cordón. Los ensayos no destructivos revisan el interior o la superficie sin romper la pieza; se nombran por su técnica, como tintas penetrantes, partículas magnéticas, ultrasonido y radiografía, y los hace personal calificado. El criterio de aceptación dice qué defectos se aceptan y cuáles no; la grieta es el más grave y suele no aceptarse.",
        "El ciclo de una no conformidad es: inspección, registro, decisión sobre qué hacer, reparación por personal calificado si corresponde, nueva inspección y cierre. Los cordones aceptados también quedan registrados, porque el registro es la evidencia de que se controló. Para valorar un hallazgo se calcula la longitud rechazada, su porcentaje del total y su costo con la tarifa de ejemplo.",
        f"Este cuaderno no enseña a reparar una soldadura: la reparación la decide el proyecto y la ejecuta personal calificado, con permiso y norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("inspección visual", "revisión del aspecto del cordón por una persona calificada"), ("ensayo no destructivo", "prueba que revisa una soldadura sin romper la pieza"), ("criterio de aceptación", "regla que dice qué defectos se aceptan y cuáles no"), ("grieta", "fisura del cordón o de la pieza, el defecto más grave"), ("socavación", "surco junto al cordón"), ("reinspección", "nueva revisión después de una reparación")],
    worked=[
        ("Porcentaje rechazado", "De 500 mm de cordón inspeccionado de ejemplo, se rechazan 100 mm. ¿Qué porcentaje es?", ["Se divide 100 entre 500 y se multiplica por 100.", "100 por 100 son 10.000, y 10.000 entre 500 son 20."], "20 %"),
        ("Aplicar un criterio", "Con el mismo criterio de la ficha, un cordón de ejemplo tiene un poro dentro del límite. ¿Se acepta?", ["Los poros dentro del límite se aceptan.", "Se acepta y se deja registrado."], "Sí, se acepta y se registra"),
    ],
    mistakes=[("No registrar los cordones aceptados porque «no tienen nada».", "Sin registro no hay evidencia de que se controlaron.", "Anota todos los cordones inspeccionados y su resultado."),
              ("Aceptar una grieta porque «es corta».", "El criterio no acepta grietas, por cortas que sean.", "Registra el rechazo e informa para que decida el proyecto.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una inspección visual de un cordón?", "La revisión de su aspecto por una persona calificada", "La limpieza del cordón con un paño", "El pesaje de la pieza soldada", "La inspección visual revisa el aspecto para detectar defectos."),
        ("abc", "En Montaje Industrial: ¿qué es un criterio de aceptación?", "La regla que dice qué defectos se aceptan y cuáles no", "El permiso para comenzar a soldar", "El precio de la reparación", "El criterio permite decidir de manera objetiva si un cordón sirve."),
        ("abc", "En Montaje Industrial: ¿qué es un ensayo no destructivo?", "Una prueba que revisa la soldadura sin romper la pieza", "Una prueba que rompe la pieza para mirar adentro", "Una prueba que se hace solo con la pieza pintada", "No destructivo significa que la pieza queda sin daño después de la prueba."),
        ("=", "{F} ¿Cuántos milímetros de cordón inspeccionó el informe en total?", "300+400+600+300+400", "Se suman las longitudes de K1 a K5.", " mm"),
        ("abc", "{F} ¿Qué cordón se rechaza según el criterio de aceptación?", "K3, por la grieta", "K2, por el poro", "K4, por la socavación", "Las grietas no se aceptan, y los poros y socavaciones están dentro del límite."),
        ("=", "{F} ¿Qué porcentaje del cordón inspeccionado se rechaza?", "600*100//2000", "Se divide el cordón rechazado entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuánto cuesta reparar el cordón rechazado con la tarifa de la ficha?", "600//100*18000", "Se calcula cuántos tramos de 100 mm hay y se multiplican por la tarifa.", " pesos"),
        ("abc", "{F} ¿Qué corresponde hacer con K2, que tiene un poro dentro del límite?", "Aceptarlo y dejar registrado el resultado", "Rechazarlo igual", "Taparlo para que no se vea", "Un defecto dentro del límite se acepta, pero se registra."),
        ("abc", "{F} ¿Qué debe hacerse después de que personal calificado repare el cordón rechazado?", "Reinspeccionarlo y registrar el resultado", "Pintarlo sin revisar para ahorrar tiempo", "Archivar el informe sin más", "La reparación se verifica con una nueva inspección."),
        ("abc", "{F} Un compañero propone aceptar K3 porque «la grieta es corta». ¿Qué respuesta es correcta?", "No: el criterio no acepta grietas, por cortas que sean", "Sí, si mide menos de 50 mm", "Sí, si se pinta encima", "Un criterio claro evita decisiones por gusto."),
        ("abc", "¿Por qué se registran las inspecciones aunque no haya hallazgos?", "Porque son evidencia de que se controló", "Porque así se rellenan más hojas", "Porque lo pide el proveedor del electrodo", "El registro demuestra el control, incluso cuando todo cumple."),
        ("=", "{F} Si por un criterio más estricto también se rechazara K4, ¿cuántos milímetros de cordón rechazado habría?", "600+300", "Se suman los cordones K3 y K4.", " mm"),
        ("=", "{F} Con ese criterio más estricto, ¿cuánto costaría reparar K3 y K4 con la tarifa de la ficha?", "(600+300)//100*18000", "Se calculan los tramos de 100 mm de los dos cordones y se multiplican por la tarifa.", " pesos"),
    ],
    ctx=("abc", "El jefe de ejemplo quiere ahorrar el costo de reparar K3 y te dice: «anota que la grieta es solo un rayón». ¿Qué respondes?", "Que no se pueden alterar los informes: la grieta se registra como no conformidad y decide el proyecto", "Que sí, para ahorrar dinero", "Que sí, si el rayón no se ve de lejos", "Falsear un informe oculta un defecto grave y puede causar una falla."),
    sc=[
        ("En Montaje Industrial: ¿qué defecto no se acepta en el criterio de la ficha?", "La grieta", "La grieta es el defecto más grave."),
        ("¿Qué se hace después de reparar un cordón?", "Se reinspecciona y se registra el resultado", "Se verifica que la reparación quedó conforme."),
        ("¿Qué porcentaje rechazado se obtiene con 150 mm rechazados de 600 mm?", "25 %", "150 entre 600 por 100 da 25 por ciento."),
    ],
    op=("Informe de ejemplo: L1: 500 mm, sin hallazgos. L2: 300 mm, grieta. L3: 200 mm, poro dentro del límite. Criterio de ejemplo: no se acepta ninguna grieta. Tarifa de reparación de ejemplo: $15.000 por cada 100 mm rechazados. Escribe (a) los mm inspeccionados, (b) qué cordón se rechaza, (c) el porcentaje rechazado, (d) el costo de repararlo.",
        "(a) 500 + 300 + 200 = 1.000 mm. (b) L2, por la grieta. (c) 300 × 100 ÷ 1.000 = 30 %. (d) 300 ÷ 100 × 15.000 = 45.000 pesos.",
        ["suma el total", "identifica el cordón rechazado", "calcula el porcentaje", "calcula el costo"],
        ["hoja con los cuatro cálculos"],
        ["aceptar la grieta", "dividir al revés el porcentaje", "olvidar multiplicar por los tramos de 100 mm"],
        "Pregunta: «¿qué pasa con un defecto que sí está dentro del límite?». Si no responde, pídele que relea la regla del criterio."),
    reinforce="Escribe un criterio de aceptación de ejemplo con dos defectos que se aceptan y uno que no.",
    extend="Explica con un ejemplo por qué los cordones aceptados también quedan en el registro.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (unión mecánica de ejemplo, inventada). Dos placas de 12 mm y 10 mm de espesor se unen con pernos. Cada perno lleva 1 golilla de 3 mm bajo la tuerca y 1 tuerca de 14 mm de altura. "
     "Regla de la planilla de ejemplo: largo mínimo del perno = espesores + golilla + tuerca + 6 mm de sobrante. Hay 5 pernos por conexión y 12 conexiones. Largos de perno disponibles en la bodega: 40 mm, 45 mm y 50 mm. Precio de ejemplo: $350 por perno.")
build(
    O4, 4, F,
    use="Aprenderé el vocabulario de las uniones mecánicas, a calcular en papel el largo mínimo de un perno y la cantidad de pernos, y por qué el apriete y la clase del perno los fija la especificación.",
    prior=["Sé qué es una unión mecánica.", "Sé sumar y multiplicar números enteros.", "Sé qué es una especificación técnica."],
    explain=[
        "Una unión mecánica usa pernos, tuercas y golillas. El perno atraviesa las piezas; la tuerca lo sujeta por el otro extremo; la golilla reparte la presión sobre la pieza. El espesor es el grosor de cada placa. Para elegir un perno en una planilla de papel se calcula el largo mínimo: se suman los espesores de las piezas, de la golilla y de la tuerca, más un sobrante de ejemplo, para que el perno asome fuera de la tuerca.",
        "La especificación técnica fija el diámetro, la clase de resistencia y el apriete de los pernos. La clase viene marcada en el perno, y nunca se mezclan pernos de distintas clases ni se reemplazan por otros «parecidos». El valor del apriete no se entrega en este cuaderno: lo aplica personal autorizado con un instrumento calibrado y queda registrado.",
        f"Las cantidades, los largos y los precios de esta clase son de ejemplo y de planilla. Armar o apretar una unión real exige instructor, norma vigente y EPP. {EMER} {AVISO}",
    ],
    vocab=[("perno", "pieza con cabeza y rosca que atraviesa las piezas a unir"), ("tuerca", "pieza que se enrosca en el perno para sujetarlo"), ("golilla", "arandela que reparte la presión sobre la pieza"), ("espesor", "grosor de una placa"), ("clase de resistencia", "identificación del perno que indica su resistencia, marcada en su cabeza"), ("apriete", "fuerza con que se cierra una unión, fijada por la especificación")],
    worked=[
        ("Largo mínimo", "Una unión de ejemplo tiene placas de 8 mm y 6 mm, una golilla de 2 mm, una tuerca de 10 mm y un sobrante de 5 mm. ¿Cuál es el largo mínimo del perno?", ["Se suman todos los valores.", "8 más 6 más 2 más 10 más 5 son 31 mm."], "31 mm"),
        ("Cantidad de pernos", "Una estructura de ejemplo tiene 7 conexiones de 4 pernos cada una. ¿Cuántos pernos hay?", ["Se multiplican las conexiones por los pernos de cada una.", "7 por 4 son 28."], "28 pernos"),
    ],
    mistakes=[("Usar un perno de otra clase porque «se parece» al especificado.", "La clase indica su resistencia y no es intercambiable.", "Usa solo los pernos de la clase que fija la especificación."),
              ("Elegir un perno más corto que el mínimo porque «igual entra».", "La tuerca no queda con el sobrante exigido.", "Elige un largo disponible igual o mayor que el mínimo.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una unión mecánica?", "Una unión hecha con pernos, tuercas o remaches, sin fundir las piezas", "Una unión hecha con calor que funde las piezas", "Una unión hecha solo con pintura", "La unión mecánica usa piezas de unión; la que funde metal es la soldada."),
        ("abc", "En Montaje Industrial: ¿para qué sirve una golilla?", "Para repartir la presión de la tuerca o de la cabeza sobre la pieza", "Para alargar el perno", "Para darle color al perno", "La golilla reparte la presión y cuida la superficie de la pieza."),
        ("abc", "En Montaje Industrial: ¿qué documento fija el diámetro, la clase y el apriete de los pernos?", "La especificación técnica del proyecto", "La lista de precios del proveedor", "El rótulo de cada lámina", "La especificación define las exigencias; el precio o el rótulo no lo hacen."),
        ("=", "{F} ¿Cuántos milímetros suman los espesores de las dos placas?", "12+10", "Se suman los espesores de las dos placas.", " mm"),
        ("=", "{F} ¿Cuál es el largo mínimo del perno según la regla de la planilla?", "12+10+3+14+6", "Se suman los espesores, la golilla, la tuerca y el sobrante.", " mm"),
        ("abc", "{F} ¿Qué largos disponibles cumplen con el mínimo?", "45 mm y 50 mm", "40 mm y 45 mm", "Solo 50 mm", "El largo debe ser igual o mayor que el mínimo de 45 mm."),
        ("=", "{F} ¿Cuántos pernos hay en total en las 12 conexiones?", "5*12", "Se multiplican los pernos de cada conexión por las conexiones.", " pernos"),
        ("=", "{F} ¿Cuánto cuestan todos los pernos de las 12 conexiones?", "5*12*350", "Se multiplican los pernos totales por el precio de cada uno.", " pesos"),
        ("abc", "{F} Un compañero dice que puede usar el perno de 40 mm porque «igual entra». ¿Qué respuesta es correcta?", "No: queda más corto que el mínimo de 45 mm y no tendría el sobrante exigido", "Sí, porque 40 mm es casi 45 mm", "Sí, si aprieta más la tuerca", "El mínimo de la planilla es una exigencia; apretar más no corrige un perno corto."),
        ("abc", "{F} En la bodega queda un perno de otra clase de resistencia que mide 45 mm. ¿Qué corresponde?", "No usarlo: solo se usan pernos de la clase que fija la especificación", "Usarlo, porque el largo coincide", "Usarlo en la última conexión", "La clase no es intercambiable aunque el largo coincida."),
        ("abc", "¿Por qué este cuaderno no entrega el valor de apriete de los pernos?", "Porque lo fija la especificación y lo aplica personal autorizado con un instrumento calibrado", "Porque el apriete no importa", "Porque es siempre el mismo para cualquier perno", "El apriete depende del proyecto y se verifica con instrumentos calibrados."),
        ("=", "{F} Si se agregara una segunda golilla de 3 mm, ¿cuál sería el nuevo largo mínimo?", "12+10+3+3+14+6", "Se suma la golilla adicional a los espesores y demás valores de la regla.", " mm"),
        ("=", "A las 12 conexiones de 5 pernos de la ficha se agregan 3 conexiones de 4 pernos. ¿Cuántos pernos hay en total?", "5*12+3*4", "Se suman los pernos de las conexiones iniciales y los de las nuevas.", " pernos"),
    ],
    ctx=("abc", "A un compañero de ejemplo se le acabaron los pernos de 45 mm y propone usar uno de 40 mm «que cabe igual». ¿Qué le respondes?", "Que no, porque no cumple el largo mínimo, y que se avise al supervisor para conseguir el perno correcto", "Que sí, si lo aprieta con más fuerza", "Que sí, si pone dos golillas más", "Cambiar el perno por uno más corto debilita la unión; se pide el correcto."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula en la planilla el largo mínimo de un perno?", "Sumando espesores, golilla, tuerca y sobrante", "El perno debe atravesar todo y asomar sobre la tuerca."),
        ("¿Qué documento fija la clase de los pernos?", "La especificación técnica", "La clase se exige en el proyecto y no se cambia por gusto."),
        ("¿Quién aplica el apriete de una unión real?", "Personal autorizado con un instrumento calibrado", "El apriete se hace con instrucción y se registra."),
    ],
    op=("Ficha de ejemplo: placas de 9 mm y 7 mm, golilla de 2 mm, tuerca de 12 mm y sobrante de 5 mm. Hay 6 conexiones de 4 pernos. Largos disponibles: 30, 35 y 40 mm. Precio de ejemplo: $280 por perno. Escribe (a) el largo mínimo, (b) el menor largo disponible que sirve, (c) cuántos pernos y cuánto cuestan, (d) por qué no se usa un perno de otra clase.",
        "(a) 9 + 7 + 2 + 12 + 5 = 35 mm. (b) 35 mm. (c) 6 × 4 = 24 pernos; 24 × 280 = 6.720 pesos. (d) Porque la clase indica la resistencia y la especificación exige una clase determinada.",
        ["calcula el largo mínimo", "elige el largo disponible", "calcula cantidad y costo", "explica por qué importa la clase"],
        ["hoja con los cálculos y la explicación"],
        ["olvidar el sobrante", "elegir 30 mm", "decir que la clase no importa"],
        "Pregunta: «¿qué pasa con un perno más corto que el mínimo?». Si no responde, pídele que relea el cálculo del largo mínimo."),
    reinforce="Calcula el largo mínimo de un perno con placas de 5 mm y 8 mm, golilla de 2 mm, tuerca de 9 mm y sobrante de 4 mm.",
    extend="Explica con un ejemplo por qué los pernos de distintas clases no se mezclan en una misma conexión.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Se compara unir un soporte con una unión soldada en terreno o con una unión pernada, solo como propuesta que se consulta al proyectista. "
     "Matriz de ejemplo con puntajes de 1 a 5 y pesos: seguridad (peso 4), tiempo (peso 3), mantenimiento (peso 2), costo (peso 1). "
     "Unión soldada: seguridad 2, tiempo 2, mantenimiento 1, costo 3. Unión pernada: seguridad 4, tiempo 4, mantenimiento 4, costo 3. "
     "Lista de verificación de calidad de ejemplo: 10 puntos; en una revisión cumplen 8. Regla: si la especificación exige soldadura, el tipo de unión no se cambia sin autorización del proyectista.")
build(
    O4, 5, F,
    use="Aprenderé a comparar una unión soldada con una pernada, a calcular un total con pesos y a verificar la calidad con una lista de verificación sin cambiar el diseño por cuenta propia.",
    prior=["Sé qué es una matriz de decisión.", "Sé qué es una unión soldada y una mecánica.", "Sé calcular un porcentaje simple."],
    explain=[
        "Comparar alternativas ayuda a entender por qué un proyecto elige un tipo de unión. La unión soldada es continua y no se desarma, pero exige calificación, permiso de trabajo en caliente e inspección. La unión pernada se puede desmontar y revisar, y exige pernos de la clase correcta y un apriete verificado. Para comparar se usa una matriz con criterios, puntajes y pesos, y las reglas de seguridad se aplican primero.",
        "La comparación no cambia el diseño. La especificación técnica manda, y cualquier cambio de tipo de unión lo autoriza el proyectista y queda registrado. La calidad se verifica con una lista de verificación: una tabla de puntos que se revisan, cada uno marcado como cumple o no cumple, con fecha y responsable. El porcentaje de cumplimiento es los puntos que cumplen entre el total, por 100, y los puntos que no cumplen quedan como no conformidades.",
        f"Las matrices y listas de esta clase son de papel y con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("lista de verificación", "tabla de puntos que se revisan, marcados como cumple o no cumple"), ("porcentaje de cumplimiento", "puntos que cumplen divididos por el total, por 100"), ("autorización del proyectista", "aprobación escrita de un cambio de diseño"), ("matriz de decisión", "tabla que compara alternativas con criterios, puntajes y pesos"), ("mantenimiento", "revisión y cuidado que necesita una unión durante su vida útil")],
    worked=[
        ("Total de una opción", "Una opción de ejemplo tiene puntajes 4 y 3 en dos criterios de pesos 2 y 5. ¿Cuál es su total?", ["4 por 2 son 8, y 3 por 5 son 15.", "8 más 15 son 23."], "23 puntos"),
        ("Cumplimiento", "En una lista de ejemplo de 20 puntos, cumplen 15. ¿Qué porcentaje de cumplimiento hay?", ["Se divide 15 entre 20 y se multiplica por 100.", "15 por 100 son 1.500, y 1.500 entre 20 son 75."], "75 %"),
    ],
    mistakes=[("Cambiar el tipo de unión porque la matriz da más puntos a otra.", "El diseño lo fija la especificación y solo lo cambia el proyectista.", "Presenta la comparación al proyectista y espera su autorización por escrito."),
              ("Dar por cumplida la lista de verificación con un «ok» general.", "Cada punto debe quedar marcado y con su responsable.", "Marca cada punto por separado y deja fecha y firma.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué ventaja tiene una unión pernada frente a una soldada?", "Se puede desmontar y revisar", "Es siempre más resistente", "No necesita ninguna verificación", "La unión pernada puede desarmarse; eso no la hace siempre más resistente ni la exime de control."),
        ("abc", "En Montaje Industrial: ¿qué es una lista de verificación?", "Una tabla de puntos que se revisan, marcados como cumple o no cumple", "Una lista de precios de pernos", "Un permiso de trabajo", "La lista deja constancia punto por punto del control de calidad."),
        ("abc", "En Montaje Industrial: ¿quién autoriza un cambio del tipo de unión que fija la especificación?", "El proyectista, y queda registrado", "El montajista que ejecuta la unión", "El proveedor de los pernos", "El diseño lo cambia quien lo diseñó, con registro escrito."),
        ("=", "{F} ¿Cuál es el total de la unión soldada en la matriz?", "2*4+2*3+1*2+3*1", "Se suman los puntajes multiplicados por sus pesos.", " puntos"),
        ("=", "{F} ¿Cuál es el total de la unión pernada en la matriz?", "4*4+4*3+4*2+3*1", "Se suman los puntajes multiplicados por sus pesos.", " puntos"),
        ("abc", "{F} Según el total de la matriz, ¿qué unión obtiene más puntos?", "La unión pernada, con 39 frente a 19", "La unión soldada, con 39 frente a 19", "Empatan en 39", "Los totales son 19 para la soldada y 39 para la pernada."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tiene la lista de verificación?", "8*100//10", "Se dividen los puntos que cumplen entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos puntos de la lista quedan como no conformidades?", "10-8", "Se resta lo que cumple al total de puntos.", " puntos"),
        ("abc", "{F} La especificación exige soldadura para ese soporte. Un compañero propone usar pernos porque la matriz da más puntos. ¿Qué corresponde?", "Presentar la comparación al proyectista y no cambiar la unión hasta tener su autorización", "Cambiar a pernos porque la matriz lo muestra", "Mantener la soldadura sin informar a nadie", "La matriz informa, pero no reemplaza la autorización del diseño."),
        ("abc", "{F} Un compañero dice: «la lista cumple 8 de 10, está bien». ¿Qué respuesta es correcta?", "Los 2 puntos que no cumplen son no conformidades que se registran e informan", "Es cierto, 80 % es suficiente siempre", "Los 2 puntos se pueden borrar de la lista", "Cada punto que no cumple se registra y se informa; un porcentaje no los compensa."),
        ("abc", "{F} ¿Qué dato debe tener cada punto de la lista de verificación?", "Su resultado, la fecha y el responsable", "Solo el nombre del proyecto", "Solo la hora de término", "El registro por punto permite trazar quién revisó y cuándo."),
        ("=", "{F} Si el criterio seguridad pasara a peso 5, ¿cuántos puntos sumaría la unión pernada?", "4*5+4*3+4*2+3*1", "Se recalculan los puntajes con el nuevo peso de seguridad.", " puntos"),
        ("abc", "Una revisión de ejemplo muestra una unión soldada con un cordón de menor tamaño que el pedido. ¿Qué corresponde?", "Registrar una no conformidad e informar al inspector o al ITO", "Pintarla para que parezca completa", "Marcar «cumple» por ser solo un poco menor", "El tamaño es una exigencia del proyecto; no cumplirla se registra."),
    ],
    ctx=("abc", "La jefa de ejemplo te pide: «anota 10 de 10 en la lista de verificación para entregar hoy, después se arregla». ¿Qué respondes?", "Que no: se anota lo real, con los 2 puntos que no cumplen, y se informa al ITO", "Que sí, para cumplir la entrega", "Que sí, pero anotando 9 de 10", "Un registro falso quita confianza al control y puede ocultar un riesgo."),
    sc=[
        ("En Montaje Industrial: ¿qué se calcula para obtener el total de una alternativa?", "Los puntajes multiplicados por sus pesos, sumados", "Cada criterio influye según su peso."),
        ("¿Qué pasa con un punto de la lista que no cumple?", "Se registra como no conformidad y se informa", "No se borra ni se compensa con otros puntos."),
        ("¿Quién autoriza cambiar el tipo de unión del proyecto?", "El proyectista", "El diseño solo lo cambia quien lo diseñó."),
    ],
    op=("Ficha de ejemplo: opción X: seguridad 3, tiempo 5, costo 4. Opción Z: seguridad 5, tiempo 3, costo 3. Pesos: seguridad 4, tiempo 2, costo 1. Una lista de verificación de 12 puntos tiene 9 que cumplen. Escribe (a) el total de cada opción, (b) cuál tiene más puntos, (c) el porcentaje de cumplimiento de la lista, (d) qué se hace con los puntos que no cumplen.",
        "(a) X: 3×4 + 5×2 + 4×1 = 12 + 10 + 4 = 26. Z: 5×4 + 3×2 + 3×1 = 20 + 6 + 3 = 29. (b) Z. (c) 9 × 100 ÷ 12 = 75 %. (d) Registrar los 3 puntos como no conformidades e informar al inspector o al ITO.",
        ["calcula los dos totales", "identifica la opción con más puntos", "calcula el porcentaje", "indica qué hacer con los puntos que no cumplen"],
        ["hoja con los cálculos y la decisión"],
        ["multiplicar mal los pesos", "dividir al revés el porcentaje", "borrar los puntos que no cumplen"],
        "Pregunta: «¿qué haces con un punto que no cumple?». Si no responde, pídele que relea el párrafo de no conformidades."),
    reinforce="Inventa una lista de verificación de 5 puntos para una unión pernada y calcula su porcentaje de cumplimiento.",
    extend="Explica con un ejemplo por qué una comparación de alternativas no reemplaza la autorización del proyectista.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller ficticio «Metal Demo» debe proteger 40 vigas de 3 m² de superficie cada una. La etiqueta de un tarro de ejemplo dice: «inflamable; vapores nocivos; mantener alejado del calor y de las chispas; "
     "usar en lugar ventilado; mantener cerrado». La bodega de pinturas del taller no tiene ventilación y queda junto a la zona donde se hacen trabajos con chispas.")
build(
    O5, 1, F,
    use="Aprenderé por qué se protege el acero de la corrosión, qué peligros tienen las pinturas y los anticorrosivos, qué dicen la etiqueta y la hoja de datos de seguridad y cómo se cuidan las personas y el medio ambiente.",
    prior=["Sé qué es la jerarquía de controles.", "Sé calcular la superficie de un rectángulo.", "Sé qué es un residuo."],
    explain=[
        "La corrosión es el deterioro del acero cuando reacciona con la humedad y el oxígeno del aire; debilita las piezas y acorta la vida de una estructura. Para evitarla se protegen las piezas con anticorrosivos y pinturas que forman una barrera, o con otros recubrimientos como el galvanizado, una capa de zinc. Un conjunto de capas especificado por el proyecto se llama sistema de protección.",
        "Estos productos tienen peligros: los solventes son inflamables y sus vapores dañan la salud; el contacto con la piel y los ojos irrita; una bodega sin ventilación acumula vapores. La información de seguridad está en la etiqueta y en la hoja de datos de seguridad (HDS) del producto, que explica sus peligros, su almacenamiento y qué hacer en una emergencia. Los controles son la ventilación (ingeniería), mantener los productos lejos de chispas y llamas (administrativo) y la protección respiratoria, los guantes y los lentes (EPP). Los envases con restos, los trapos con solvente y la pintura sobrante son residuos peligrosos: no van a la basura común ni al desagüe, y se entregan a una gestión autorizada según la norma vigente.",
        f"Este cuaderno no enseña a preparar superficies ni a aplicar productos. {EMER} Ante un derrame o un olor fuerte que cause malestar, aléjate también del lugar y avisa. {AVISO}",
    ],
    vocab=[("corrosión", "deterioro del acero por reacción con la humedad y el oxígeno"), ("anticorrosivo", "producto que protege el acero formando una barrera contra la corrosión"), ("galvanizado", "recubrimiento de zinc sobre el acero"), ("sistema de protección", "conjunto de capas que el proyecto especifica para proteger una pieza"), ("HDS", "hoja de datos de seguridad, que informa peligros, almacenamiento y acciones ante emergencias"), ("inflamable", "que se incendia con facilidad ante calor, chispas o llama"), ("residuo peligroso", "residuo que daña la salud o el ambiente y exige gestión autorizada")],
    worked=[
        ("Reconocer la corrosión", "Una viga de ejemplo guardada a la intemperie muestra manchas rojizas y escamas. ¿Qué proceso ocurre?", ["La humedad y el oxígeno reaccionan con el acero.", "Ese deterioro se llama corrosión."], "Corrosión"),
        ("Calcular una superficie", "Una pieza de ejemplo tiene 5 caras de 2 m² cada una por proteger. ¿Cuántos metros cuadrados son en total?", ["Se multiplican las caras por la superficie de cada una.", "5 por 2 son 10."], "10 m²"),
    ],
    mistakes=[("Guardar productos inflamables junto a una zona con chispas.", "Los vapores pueden incendiarse con una sola chispa.", "Los productos se guardan según la HDS, ventilados y lejos de fuentes de calor."),
              ("Botar al desagüe la pintura sobrante.", "Contamina el agua y es un residuo peligroso.", "Gestiónalo con un proveedor autorizado, según la norma vigente.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la corrosión del acero?", "Su deterioro por reacción con la humedad y el oxígeno", "Su endurecimiento por calor", "Su deformación por una carga", "La corrosión es un cambio químico del acero; el calor o la carga producen otros efectos."),
        ("abc", "En Montaje Industrial: ¿para qué sirve la hoja de datos de seguridad (HDS) de un producto?", "Informa sus peligros, su almacenamiento y qué hacer en una emergencia", "Informa su precio y su color", "Informa cuántos tarros caben en un camión", "La HDS trata de seguridad; el precio y el transporte son otros datos."),
        ("abc", "En Montaje Industrial: ¿qué indica la palabra «inflamable» en la etiqueta de un tarro?", "Que puede incendiarse con calor, chispas o llama", "Que se apaga con agua", "Que es seguro cerca de una soldadura", "Inflamable significa que se incendia con facilidad."),
        ("=", "{F} ¿Cuántos metros cuadrados hay que proteger en total?", "40*3", "Se multiplican las vigas por la superficie de cada una.", " m²"),
        ("abc", "{F} ¿Por qué es riesgosa la ubicación de la bodega de pinturas de la ficha?", "Porque guarda productos inflamables sin ventilación junto a una zona con chispas", "Porque queda lejos de las vigas", "Porque los tarros están cerrados", "Los vapores acumulados y las chispas pueden causar un incendio."),
        ("abc", "{F} Una ventilación que renueva el aire de la bodega es un control de tipo:", "De ingeniería, porque cambia el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a la persona", "Una instalación física que renueva el aire actúa sobre el lugar."),
        ("abc", "{F} ¿Dónde se informa qué hacer ante un derrame del producto?", "En la hoja de datos de seguridad", "En el rótulo de la lámina", "En la lista de piezas", "La HDS describe las acciones ante emergencias del producto."),
        ("=", "{F} Si cada viga requiere 2 horas de trabajo de protección (dato de ejemplo), ¿cuántas horas de trabajo hay para las 40 vigas?", "40*2", "Se multiplican las vigas por las horas de cada una.", " horas"),
        ("abc", "{F} Sobró pintura en un tarro y hay trapos con solvente. ¿Qué corresponde con estos residuos?", "Gestionarlos como residuos peligrosos con un proveedor autorizado, según la norma vigente", "Botarlos a la basura común", "Vaciarlos al desagüe", "Los residuos peligrosos exigen gestión autorizada para no dañar la salud ni el ambiente."),
        ("abc", "{F} Un compañero dice: «si el tarro huele poco, no hace falta ventilar». ¿Qué respuesta es correcta?", "Es falso: los vapores pueden ser nocivos aunque el olor sea leve; se sigue la etiqueta y la HDS", "Es cierto, el olor indica el peligro", "Es cierto si el tarro está cerrado", "El olor no mide el peligro; la información está en la etiqueta y la HDS."),
        ("abc", "Durante una visita de ejemplo a un taller, un tarro se vuelca y una persona se siente mareada por el olor. ¿Qué corresponde según las reglas generales?", "Alejarte de la zona de riesgo, avisar a un adulto responsable y a emergencias", "Limpiar el derrame con las manos", "Echar agua sobre el derrame", "Un derrame de solvente es un riesgo; lo atienden personas capacitadas."),
        ("=", "{F} Si se protegen 8 vigas por día, ¿cuántos días se necesitan para las 40 vigas?", "40//8", "Se divide el total de vigas entre las que se protegen por día.", " días"),
        ("abc", "{F} La jefa propone dejar los tarros en esa bodega «por esta semana» hasta arreglar la ventilación. ¿Qué respuesta es correcta?", "No: mientras no se controle el riesgo, los productos se guardan según la HDS en un lugar adecuado y lejos de las chispas", "Sí, por una semana no pasa nada", "Sí, si se abre la puerta", "Un riesgo de incendio no se posterga; se controla antes de almacenar."),
    ],
    ctx=("abc", "Un amigo de ejemplo te pide ayuda para aplicar un anticorrosivo con solvente en el interior cerrado de su galpón. ¿Qué respondes?", "Que no, porque los vapores en un lugar cerrado son peligrosos y la tarea exige personal capacitado, ventilación, EPP y norma vigente", "Que sí, si abren una ventana pequeña", "Que sí, si usas una mascarilla de papel", "Los vapores acumulados en espacios cerrados son un riesgo grave que este cuaderno no te habilita a manejar."),
    sc=[
        ("En Montaje Industrial: ¿qué es la corrosión?", "El deterioro del acero por humedad y oxígeno", "Es una reacción química que debilita las piezas."),
        ("¿Qué documento explica los peligros y las emergencias de un producto?", "La hoja de datos de seguridad (HDS)", "La HDS reúne la información de seguridad del producto."),
        ("¿Adónde van los envases con restos de pintura?", "A una gestión autorizada de residuos peligrosos", "No pueden ir a la basura común ni al desagüe."),
    ],
    op=("Ficha de ejemplo: el taller «Metal Demo» debe proteger 25 vigas de 4 m² cada una. Una bodega guarda tarros inflamables junto a una zona con chispas y sin ventilación. Escribe (a) los m² por proteger, (b) dos peligros de esa bodega, (c) un control de ingeniería y un control administrativo, (d) qué se hace con los trapos con solvente.",
        "(a) 25 × 4 = 100 m². (b) Productos inflamables cerca de chispas y vapores acumulados por la falta de ventilación. (c) Ingeniería: instalar ventilación en la bodega. Administrativo: mantener los productos lejos de las chispas, según la HDS. (d) Gestionarlos como residuos peligrosos con un proveedor autorizado, según la norma vigente.",
        ["calcula los m²", "nombra dos peligros", "propone los dos controles", "indica la gestión del residuo"],
        ["hoja con las cuatro respuestas"],
        ["proponer solo EPP", "botar los trapos a la basura común", "multiplicar mal los m²"],
        "Pregunta: «¿qué documento te dice cómo guardar el producto?». Si no responde, pídele que relea el párrafo de la HDS."),
    reinforce="Escribe tres datos que debe tener la etiqueta o la HDS de un producto inflamable (por ejemplo, peligro, almacenamiento y emergencia).",
    extend="Explica con un ejemplo por qué proteger el acero de la corrosión también es una decisión de seguridad.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (especificación de pintura de ejemplo, inventada; valores de ejemplo). Sistema de protección para vigas: imprimante anticorrosivo, espesor de película seca (EPS) de 60 µm; capa intermedia, EPS de 80 µm; capa de terminación, EPS de 40 µm. "
     "Hoja técnica de ejemplo: espera de 6 horas entre el imprimante y la capa intermedia, y de 12 horas entre la capa intermedia y la terminación. La viga tiene 2 mm de espesor de acero.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario de un sistema de protección, qué son el espesor de película seca y el micrón, qué documentos usa el oficio y qué rol cumple cada persona.",
    prior=["Sé qué es la corrosión.", "Sé qué es una HDS.", "Sé que 1 m son 1.000 mm."],
    explain=[
        "Un sistema de protección es el conjunto de capas que especifica el proyecto. Suele incluir una capa imprimante anticorrosiva, que protege el acero desde el primer contacto; una o más capas intermedias, que dan espesor y barrera; y una terminación, que da color y resiste el ambiente. Antes de las capas, la especificación pide un grado de limpieza de la superficie, que se indica con un código y se verifica; la forma de lograrlo la enseña un instructor autorizado, no este cuaderno.",
        "El espesor de película seca (EPS) es el grosor de la pintura una vez seca y se mide en micrones (µm); 1 µm es la milésima parte de 1 mm. La hoja técnica del producto indica rendimiento, tiempos de espera entre capas y condiciones ambientales; es distinta de la HDS, que trata de seguridad. Los roles son el aplicador, que ejecuta la tarea con capacitación; el inspector de pintura, que mide y registra; el supervisor; el prevencionista; y el proyectista, que define el sistema.",
        f"Si la especificación de pintura y el plano se contradicen, no se supone: se registra y se consulta al proyectista. {EMER} {AVISO}",
    ],
    vocab=[("sistema de protección", "conjunto de capas que especifica el proyecto"), ("imprimante", "primera capa anticorrosiva sobre el acero"), ("espesor de película seca (EPS)", "grosor de la pintura una vez seca"), ("micrón (µm)", "milésima parte de un milímetro"), ("hoja técnica", "documento del producto con rendimiento, tiempos entre capas y condiciones de uso"), ("inspector de pintura", "persona que mide espesores y registra si cumplen")],
    worked=[
        ("Espesor total", "Un sistema de ejemplo tiene capas de 50, 70 y 30 µm. ¿Cuál es el EPS total especificado?", ["Se suman los espesores de las tres capas.", "50 más 70 más 30 son 150 µm."], "150 µm"),
        ("Pasar a micrones", "Una lámina de ejemplo tiene 3 mm de espesor. ¿Cuántos micrones son?", ["Cada milímetro son 1.000 µm.", "3 por 1.000 son 3.000 µm."], "3.000 µm"),
    ],
    mistakes=[("Confundir la hoja técnica con la HDS.", "La primera trata de cómo usar el producto y la segunda de su seguridad.", "Consulta la hoja técnica para tiempos y rendimientos, y la HDS para peligros y emergencias."),
              ("Compensar una capa delgada con otra más gruesa.", "Cada capa tiene su función y su espesor especificado.", "Registra la diferencia y consulta al inspector o al proyectista.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el espesor de película seca (EPS)?", "El grosor de la pintura una vez seca, medido en micrones", "El grosor del tarro de pintura", "El grosor de la viga de acero", "El EPS se refiere a la capa de pintura seca, no al envase ni a la viga."),
        ("abc", "En Montaje Industrial: ¿qué función cumple la capa imprimante anticorrosiva?", "Proteger el acero desde el primer contacto frenando la corrosión", "Dar el color final", "Reducir el peso de la viga", "El imprimante es la primera barrera contra la corrosión; el color lo da la terminación."),
        ("abc", "En Montaje Industrial: ¿qué es un micrón (µm)?", "La milésima parte de un milímetro", "Mil milímetros", "La centésima parte de un metro", "Un micrón equivale a 0,001 mm, es decir, una milésima de milímetro."),
        ("=", "{F} ¿Cuántos µm de EPS total especifica el sistema de la ficha?", "60+80+40", "Se suman los espesores de las tres capas.", " µm"),
        ("=", "{F} ¿Cuántas horas de espera suman entre las tres capas?", "6+12", "Se suman las dos esperas que fija la hoja técnica.", " horas"),
        ("abc", "{F} ¿Cuál es la capa más gruesa del sistema?", "La intermedia, de 80 µm", "El imprimante, de 60 µm", "La terminación, de 40 µm", "La capa intermedia tiene el mayor espesor de las tres."),
        ("=", "{F} En un punto se mide un EPS total de 175 µm. ¿Cuántos µm le faltan para el total especificado?", "180-175", "Se resta lo medido al total especificado.", " µm"),
        ("abc", "{F} ¿Qué documento informa las esperas entre capas y el rendimiento del producto?", "La hoja técnica del producto", "La HDS", "El rótulo de la lámina", "La hoja técnica trata del uso; la HDS, de la seguridad."),
        ("abc", "{F} ¿Quién mide los espesores y registra si cumplen?", "El inspector de pintura o de calidad", "El mismo aplicador sin dejar registro", "El proveedor del producto en su bodega", "La medición registrada por un inspector da evidencia independiente."),
        ("abc", "{F} Un compañero dice: «la capa intermedia quedó a 70 µm, la compenso con más terminación». ¿Qué respuesta es correcta?", "No: cada capa tiene su espesor especificado; se registra la diferencia y decide el inspector o el proyectista", "Sí, porque el total es lo único que importa", "Sí, si la terminación es de otro color", "Cada capa cumple una función; no se compensan entre sí."),
        ("abc", "{F} El plano y la especificación de pintura se contradicen en el color de terminación. ¿Qué corresponde?", "Registrar la contradicción y consultar al proyectista antes de continuar", "Elegir el color que más guste", "Aplicar los dos colores", "Una contradicción entre documentos la resuelve quien diseñó el proyecto."),
        ("=", "{F} Si se omitiera la capa intermedia, ¿cuántos µm de EPS total quedarían?", "60+40", "Se suman solo el imprimante y la terminación.", " µm"),
        ("=", "{F} ¿Cuántos micrones tiene el espesor de acero de la viga de la ficha?", "2*1000", "Se multiplican los milímetros por 1.000 para pasarlos a micrones.", " µm"),
    ],
    ctx=("abc", "Un jefe de ejemplo pide adelantar la terminación sin esperar el tiempo de la hoja técnica porque «hay apuro». ¿Qué respondes?", "Que los tiempos de la hoja técnica se respetan y que, si hay apuro, se consulta al ITO o al proyectista para replanificar", "Que sí, porque el apuro justifica todo", "Que sí, pero esperando la mitad del tiempo", "Los tiempos de espera protegen la calidad; un apuro se resuelve replanificando."),
    sc=[
        ("En Montaje Industrial: ¿cuántos µm tiene 1 mm?", "1.000 µm", "Un micrón es la milésima parte de un milímetro."),
        ("¿Qué documento informa los tiempos entre capas?", "La hoja técnica del producto", "La hoja técnica indica cómo se usa el producto."),
        ("¿Quién mide y registra los espesores?", "El inspector de pintura", "La medición la hace una persona que registra y no solo el aplicador."),
    ],
    op=("Ficha de ejemplo: sistema de protección con imprimante de 50 µm, intermedia de 90 µm y terminación de 40 µm. Esperas de la hoja técnica: 8 horas y 10 horas. La lámina de acero mide 4 mm de espesor. Escribe (a) el EPS total, (b) las horas de espera totales, (c) el espesor de la lámina en µm, (d) qué documento mirar para conocer los peligros del producto.",
        "(a) 50 + 90 + 40 = 180 µm. (b) 8 + 10 = 18 horas. (c) 4 × 1.000 = 4.000 µm. (d) La hoja de datos de seguridad (HDS).",
        ["suma los espesores", "suma las esperas", "pasa milímetros a micrones", "nombra el documento correcto"],
        ["hoja con las cuatro respuestas"],
        ["confundir HDS con hoja técnica", "multiplicar por 100 en vez de por 1.000", "sumar solo dos capas"],
        "Pregunta: «¿qué documento trae los tiempos entre capas?». Si no responde, pídele que relea la diferencia entre HDS y hoja técnica."),
    reinforce="Inventa un sistema de protección de tres capas con sus espesores en µm y calcula el total.",
    extend="Explica con un ejemplo por qué cada capa de un sistema tiene un espesor y una función distintos.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (registro de control de ejemplo; las lecturas las tomó personal autorizado). EPS total mínimo especificado: 180 µm. Lecturas en 5 puntos de una viga, en orden de punto 1 a punto 5: 185, 192, 178, 181 y 175 µm. "
     "Condición de la hoja técnica de ejemplo: no se aplica el producto si la humedad relativa es de 85 % o más. Registro de humedad relativa del día: a las 9:00, 70 %; a las 12:00, 82 %; a las 15:00, 88 %.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un registro de control de espesores y de condiciones ambientales, a decidir qué puntos cumplen y a tratar las no conformidades sin ocultarlas.",
    prior=["Sé qué es el EPS y el micrón.", "Sé qué es una no conformidad.", "Sé calcular un porcentaje simple."],
    explain=[
        "El control de calidad de una protección mide el EPS con un medidor de espesor, por personal autorizado y con el instrumento calibrado. Cada punto medido debe cumplir el mínimo especificado: un punto que supera el mínimo no compensa a otro que no llega. Los puntos bajo el mínimo se registran como no conformidades y se informan al inspector, que decide con el proyecto qué corresponde.",
        "La hoja técnica fija condiciones ambientales, por ejemplo un máximo de humedad relativa, que es la cantidad de vapor de agua del aire respecto de lo máximo que cabe, expresada en porcentaje. El registro de esas condiciones demuestra que se respetaron. Un registro completo incluye las lecturas, el instrumento y su calibración, las condiciones ambientales, la fecha y quién midió. No se repite una medición hasta que salga un valor mejor: se registran todas.",
        f"La corrección de una no conformidad es una tarea de personal calificado, con permiso y norma vigente, que este cuaderno no enseña. {EMER} {AVISO}",
    ],
    vocab=[("medidor de espesor", "instrumento que mide el espesor de la película seca"), ("humedad relativa", "vapor de agua del aire respecto de lo máximo que cabe, en porcentaje"), ("punto de control", "lugar de la pieza donde se mide el espesor"), ("no conformidad", "resultado que no cumple lo pedido"), ("registro de condiciones ambientales", "anotación de la humedad y otras condiciones durante el trabajo")],
    worked=[
        ("Comparar con el mínimo", "El mínimo de ejemplo es 150 µm y se miden 148, 152 y 150 µm. ¿Qué puntos cumplen?", ["Cumple el que es igual o mayor que 150.", "Cumplen 152 y 150; 148 no cumple."], "Cumplen los puntos de 152 y 150 µm"),
        ("Condición ambiental", "La hoja técnica de ejemplo prohíbe aplicar con humedad de 90 % o más. Hoy hay 86 %. ¿Se puede aplicar?", ["86 es menor que 90.", "La condición se cumple."], "Sí, la condición se cumple"),
    ],
    mistakes=[("Compensar un punto bajo el mínimo con otro que sobra.", "Cada punto debe cumplir por sí mismo.", "Registra cada punto bajo el mínimo como no conformidad."),
              ("Repetir la medición hasta que salga un valor mayor.", "Se ocultan los resultados reales.", "Registra todas las mediciones tomadas y su resultado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la humedad relativa?", "El vapor de agua del aire respecto de lo máximo que cabe, en porcentaje", "La cantidad de agua en un tarro de pintura", "La temperatura del acero", "La humedad relativa se refiere al aire, y la hoja técnica puede fijar un máximo."),
        ("abc", "En Montaje Industrial: ¿por qué se registran las condiciones ambientales durante el trabajo?", "Porque la hoja técnica fija condiciones y el registro demuestra que se respetaron", "Porque así se llena más papel", "Porque lo pide el proveedor de los instrumentos", "El registro es la evidencia de que se cumplieron las condiciones del producto."),
        ("abc", "En Montaje Industrial: ¿qué instrumento mide el espesor de la película seca?", "Un medidor de espesor", "Un manómetro", "Una cinta métrica", "El medidor de espesor está hecho para este control; el manómetro mide presión."),
        ("=", "{F} ¿Cuántos µm le faltan al punto más bajo para llegar al mínimo?", "180-175", "Se resta la lectura más baja al mínimo especificado.", " µm"),
        ("abc", "{F} ¿Qué puntos cumplen el mínimo de 180 µm?", "Los puntos 1, 2 y 4", "Los puntos 1, 2 y 3", "Todos los puntos", "Las lecturas de 185, 192 y 181 cumplen; 178 y 175 no."),
        ("=", "{F} ¿Qué porcentaje de los puntos cumple el mínimo?", "3*100//5", "Se divide lo que cumple entre el total de puntos y se multiplica por 100.", " %"),
        ("abc", "{F} ¿A qué hora del registro no corresponde aplicar según la hoja técnica?", "A las 15:00, con 88 %", "A las 12:00, con 82 %", "A las 9:00, con 70 %", "La condición prohíbe aplicar con 85 % o más, y solo las 15:00 la superan."),
        ("abc", "{F} ¿Qué corresponde con los puntos 3 y 5?", "Registrarlos como no conformidades e informar al inspector para que decida", "Pintar encima sin registrar", "Medir de nuevo hasta que salga un valor mayor", "Los puntos bajo el mínimo se registran e informan; no se repiten hasta obtener otro valor."),
        ("=", "{F} Si se controlan 5 puntos por viga, ¿cuántos puntos se controlan en 12 vigas?", "12*5", "Se multiplican las vigas por los puntos de cada una.", " puntos"),
        ("abc", "{F} Un compañero dice: «el punto 2 mide 192 µm, sobra y compensa los puntos 3 y 5». ¿Qué respuesta es correcta?", "No: cada punto debe cumplir el mínimo y lo que sobra no compensa", "Sí, porque el total de la viga sí cumple", "Sí, si se anota un promedio", "Cada punto es un control independiente."),
        ("abc", "{F} El jefe pide aplicar a las 15:00 porque «solo son 3 puntos sobre el límite». ¿Qué respuesta es correcta?", "No: la condición de la hoja técnica es un límite y se consulta al inspector antes de continuar", "Sí, 3 puntos no importan", "Sí, si se abre una ventana", "Superar un límite de la hoja técnica puede arruinar la capa y debe consultarse."),
        ("=", "{F} Si cada punto bajo el mínimo exige una revisión de 2 horas de personal calificado (dato de ejemplo), ¿cuántas horas de revisión se necesitan?", "2*2", "Se multiplican los puntos bajo el mínimo por las horas de cada revisión.", " horas"),
        ("abc", "{F} ¿Qué debe llevar el registro de este control?", "Las lecturas, el instrumento y su calibración, las condiciones ambientales, la fecha y quién midió", "Solo la palabra «cumple»", "Solo la firma del jefe", "Un registro completo permite repetir y revisar el control."),
    ],
    ctx=("abc", "La supervisora de ejemplo te pide: «anota 180 en los puntos 3 y 5 para cerrar hoy, después se arregla». ¿Qué respondes?", "Que no: se anotan las lecturas reales y se informa al inspector", "Que sí, para cerrar a tiempo", "Que sí, pero solo en el punto 3", "Alterar lecturas oculta un defecto y quita valor al control."),
    sc=[
        ("En Montaje Industrial: ¿qué se hace con un punto bajo el mínimo de EPS?", "Se registra como no conformidad y se informa al inspector", "Un punto bajo el mínimo no se compensa ni se oculta."),
        ("¿Qué mide la humedad relativa?", "El vapor de agua del aire respecto de lo máximo que cabe", "La hoja técnica puede fijar un máximo de humedad."),
        ("¿Se repite una medición hasta obtener un valor mejor?", "No: se registran todas las mediciones tomadas", "Repetir hasta que salga otro valor oculta el resultado real."),
    ],
    op=("Ficha de ejemplo: EPS mínimo de 150 µm. Lecturas en 4 puntos: 155, 148, 160 y 150 µm. Condición de la hoja técnica: no aplicar con humedad relativa de 80 % o más. Humedad del día: 9:00, 72 %; 14:00, 81 %. Escribe (a) qué puntos cumplen, (b) cuántos µm le faltan al punto más bajo, (c) a qué hora no corresponde aplicar, (d) qué harías con el punto que no cumple.",
        "(a) Cumplen 155, 160 y 150 µm; 148 no cumple. (b) 150 − 148 = 2 µm. (c) A las 14:00, con 81 %. (d) Registrarlo como no conformidad e informar al inspector, sin repetir la medición hasta que salga otro valor.",
        ["clasifica los cuatro puntos", "calcula lo que falta", "aplica la condición ambiental", "indica qué hacer con la no conformidad"],
        ["hoja con las cuatro respuestas"],
        ["considerar que 150 no cumple", "aceptar 81 % como menor de 80 %", "proponer repetir la medición hasta que salga otro valor"],
        "Pregunta: «¿cumple un punto que es exactamente igual al mínimo?». Si no responde, pídele que relea el ejemplo de 150 µm."),
    reinforce="Escribe un registro de ejemplo de tres puntos de EPS con un mínimo de 100 µm y marca cuáles cumplen.",
    extend="Explica con un ejemplo por qué se registran todas las mediciones y no solo las que cumplen.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Superficie por proteger: 120 m². Imprimante: rendimiento teórico de 10 m² por litro. Terminación: rendimiento teórico de 5 m² por litro. Pérdida de ejemplo en ambos productos: 20 %. "
     "Rendimiento práctico = rendimiento teórico × (100 − pérdida) ÷ 100. Los productos se venden en tarros de 4 litros: imprimante $18.000 por tarro; terminación $22.000 por tarro.")
build(
    O5, 4, F,
    use="Aprenderé a calcular en papel el rendimiento práctico de un producto de protección, los litros, los tarros y el costo, y a tratar el sobrante como residuo.",
    prior=["Sé qué es el rendimiento.", "Sé calcular un porcentaje simple.", "Sé dividir y multiplicar números enteros."],
    explain=[
        "El rendimiento teórico es la superficie que cubre un litro de producto en condiciones ideales, según la hoja técnica. En la práctica se pierde parte del producto por irregularidades de la superficie, restos en los envases y mermas, así que el rendimiento práctico es menor: se calcula multiplicando el teórico por 100 menos la pérdida, y dividiendo entre 100. Los litros necesarios son la superficie dividida por el rendimiento práctico.",
        "Los productos se venden en envases de un tamaño fijo, por lo que los litros se pasan a tarros y se redondea hacia arriba: si faltan unos litros, se compra un tarro más. Hacia arriba se calcula sumando al número de litros el tamaño del tarro menos 1 y dividiendo por el tamaño del tarro. El costo es los tarros por su precio. Lo que sobra no se bota: se guarda según la HDS o se gestiona como residuo según la norma vigente.",
        f"Este cálculo es de planilla, con valores de ejemplo, y no enseña a preparar ni aplicar productos. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento teórico", "superficie que cubre un litro en condiciones ideales, según la hoja técnica"), ("rendimiento práctico", "superficie que cubre un litro considerando las pérdidas"), ("pérdida", "parte del producto que no llega a cubrir la pieza"), ("tarro", "envase del producto de tamaño fijo"), ("redondear hacia arriba", "pasar al número entero siguiente cuando no se pueden comprar fracciones")],
    worked=[
        ("Rendimiento práctico", "Un producto de ejemplo tiene rendimiento teórico de 12 m² por litro y una pérdida de 25 %. ¿Cuál es su rendimiento práctico?", ["Se multiplica 12 por 75 y se divide entre 100.", "12 por 75 son 900, y 900 entre 100 son 9."], "9 m² por litro"),
        ("Litros y tarros", "Se deben cubrir 90 m² con un producto de rendimiento práctico de 9 m² por litro, en tarros de 4 litros. ¿Cuántos tarros se compran?", ["Litros: 90 entre 9 son 10.", "Con tarros de 4 L: 10 más 3 son 13, y 13 entre 4 son 3 tarros."], "3 tarros"),
    ],
    mistakes=[("Usar el rendimiento teórico como si fuera el real.", "Se compra de menos y el trabajo se detiene.", "Calcula el rendimiento práctico con la pérdida."),
              ("Comprar justo los litros calculados sin redondear a tarros.", "No existen fracciones de tarro y puede faltar producto.", "Redondea hacia arriba a tarros enteros.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el rendimiento teórico de una pintura?", "La superficie que cubre un litro en condiciones ideales, según la hoja técnica", "El precio de un litro", "El tiempo que tarda en secar", "El rendimiento teórico relaciona litros con superficie; precio y secado son otros datos."),
        ("abc", "En Montaje Industrial: ¿por qué el rendimiento práctico es menor que el teórico?", "Porque se pierde producto por irregularidades, restos en los envases y mermas", "Porque el producto se vuelve más caro", "Porque la pintura pesa más al aplicarla", "Las pérdidas reducen la superficie realmente cubierta por litro."),
        ("abc", "En Montaje Industrial: ¿por qué se redondea hacia arriba la cantidad de tarros?", "Porque no se compran fracciones de tarro y faltar producto detendría el trabajo", "Porque así se paga menos", "Porque el redondeo hacia abajo siempre sobra", "Redondear hacia abajo deja el trabajo sin producto."),
        ("=", "{F} ¿Cuál es el rendimiento práctico del imprimante, en m² por litro?", "10*80//100", "Se multiplica el rendimiento teórico por 100 menos la pérdida y se divide entre 100.", " m² por litro"),
        ("=", "{F} ¿Cuántos litros de imprimante se necesitan, con ese rendimiento práctico de 8 m² por litro?", "120//8", "Se divide la superficie entre el rendimiento práctico.", " litros"),
        ("=", "{F} ¿Cuál es el rendimiento práctico de la terminación, en m² por litro?", "5*80//100", "Se multiplica el rendimiento teórico por 100 menos la pérdida y se divide entre 100.", " m² por litro"),
        ("=", "{F} ¿Cuántos litros de terminación se necesitan, con ese rendimiento práctico de 4 m² por litro?", "120//4", "Se divide la superficie entre el rendimiento práctico.", " litros"),
        ("=", "{F} ¿Cuántos tarros de imprimante hay que comprar, si se necesitan 15 litros?", "(15+3)//4", "Se redondea hacia arriba la división de litros entre el tamaño del tarro.", " tarros"),
        ("=", "{F} ¿Cuántos tarros de terminación hay que comprar, si se necesitan 30 litros?", "(30+3)//4", "Se redondea hacia arriba la división de litros entre el tamaño del tarro.", " tarros"),
        ("=", "{F} ¿Cuánto cuestan en total 4 tarros de imprimante y 8 de terminación?", "4*18000+8*22000", "Se multiplican los tarros de cada producto por su precio y se suman.", " pesos"),
        ("abc", "{F} Un compañero compró 3 tarros de imprimante «porque casi alcanza». ¿Qué problema hay?", "Con 12 litros faltan 3 de los 15 necesarios y el trabajo se detendría", "Ninguno, porque 12 es casi 15", "Que 3 tarros cuestan más que 4", "Faltar producto detiene el trabajo y obliga a comprar de apuro."),
        ("=", "{F} Al comprar los 8 tarros de terminación, ¿cuántos litros sobran sobre los 30 necesarios?", "8*4-30", "Se restan los litros necesarios a los litros comprados.", " litros"),
        ("abc", "{F} ¿Qué corresponde con los litros sobrantes?", "Guardarlos cerrados según la HDS o gestionarlos como residuo según la norma vigente", "Vaciarlos al desagüe", "Mezclarlos con otro producto para aprovecharlos", "Un sobrante se guarda de forma segura o se gestiona como residuo; nunca se desecha al ambiente."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «con el rendimiento de la hoja técnica de 10 m² por litro ya sé cuánto comprar, no hace falta pensar en pérdidas». ¿Qué respondes?", "Que la pérdida reduce el rendimiento real y se calcula el rendimiento práctico antes de comprar", "Que tiene razón, porque la hoja técnica nunca se equivoca", "Que compre el doble por si acaso", "El rendimiento de la hoja es ideal; el real depende de las pérdidas."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el rendimiento práctico?", "Rendimiento teórico por (100 menos la pérdida), dividido entre 100", "Se descuenta la pérdida del rendimiento ideal."),
        ("¿Cómo se calculan los litros necesarios?", "Superficie dividida por el rendimiento práctico", "Los litros dependen de cuánto cubre cada litro."),
        ("¿Por qué se redondea hacia arriba a tarros enteros?", "Porque no se compran fracciones y faltar detiene el trabajo", "Los envases son de tamaño fijo."),
    ],
    op=("Ficha de ejemplo: superficie por proteger de 144 m². Un producto tiene rendimiento teórico de 10 m² por litro y una pérdida de 20 %. Se vende en tarros de 5 litros a $20.000 cada uno. Escribe (a) el rendimiento práctico, (b) los litros necesarios (con ese rendimiento práctico), (c) los tarros que se compran, (d) el costo y qué se hace con el sobrante.",
        "(a) 10 × 80 ÷ 100 = 8 m² por litro. (b) 144 ÷ 8 = 18 litros. (c) 18 litros requieren 4 tarros de 5 litros (20 L). (d) 4 × 20.000 = 80.000 pesos; los 2 litros que sobran se guardan según la HDS o se gestiona como residuo.",
        ["calcula el rendimiento práctico", "calcula los litros", "redondea a tarros", "calcula el costo y trata el sobrante"],
        ["hoja con los cuatro cálculos"],
        ["usar el rendimiento teórico", "no redondear hacia arriba", "botar el sobrante"],
        "Pregunta: «¿cuántos litros hay que comprar si faltan 4?». Si no responde, pídele que relea el párrafo del redondeo."),
    reinforce="Calcula en papel el rendimiento práctico de un producto de 6 m² por litro con una pérdida del 10 %.",
    extend="Explica con un ejemplo por qué comprar justo los litros calculados puede detener un trabajo.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (resumen de un plan de izaje de ejemplo, inventado). Carga: una viga de masa 900 kg; los accesorios de izaje suman 60 kg. Lugar: patio de montaje con una línea eléctrica aérea al este y un sector sur de suelo blando. "
     "Peligros anotados: caída de la carga, personas bajo la carga, viento, contacto con la línea eléctrica y vuelco del equipo por suelo blando. Firman el plan el supervisor de izaje, el prevencionista y el jefe de terreno.")
build(
    O6, 1, F,
    use="Aprenderé qué son los equipos de levante y sus accesorios, qué peligros tienen las maniobras, cómo se previenen y por qué solo personal autorizado puede realizarlas.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es una zona de exclusión.", "Sé la diferencia entre masa y peso."],
    explain=[
        "Un equipo de levante es una máquina o dispositivo para elevar y trasladar cargas; algunos ejemplos son la grúa y el polipasto. Los accesorios de izaje son los elementos que unen la carga con el equipo, como las eslingas y los grilletes. Un izaje es una maniobra en que una carga queda suspendida. Aquí solo se estudian los conceptos y los documentos: cómo se amarra, se engancha o se mueve una carga se aprende con un instructor autorizado, nunca con este cuaderno.",
        "Los peligros de un izaje son la caída de la carga, el aplastamiento y el atrapamiento de personas, los golpes por una carga que se balancea, el vuelco del equipo, el viento y el contacto con líneas eléctricas. La regla general más importante es que nadie permanece bajo una carga suspendida. Los controles incluyen el plan de izaje firmado, la zona de exclusión, el equipo y los accesorios con inspección vigente y capacidad rotulada, las señales acordadas y que la maniobra la hagan solo personas autorizadas.",
        f"{EMER} Un estudiante no participa en maniobras de izaje. {AVISO}",
    ],
    vocab=[("equipo de levante", "máquina o dispositivo para elevar y trasladar cargas, como una grúa"), ("accesorio de izaje", "elemento que une la carga con el equipo, como una eslinga o un grillete"), ("izaje", "maniobra en que una carga queda suspendida"), ("plan de izaje", "documento firmado que reúne los datos y los responsables de una maniobra"), ("zona de exclusión", "área donde nadie debe estar durante la maniobra"), ("capacidad rotulada", "límite de carga que indica el fabricante en un rótulo")],
    worked=[
        ("Clasificar un elemento", "Un elemento de ejemplo une la carga con el gancho del equipo. ¿Es equipo de levante o accesorio de izaje?", ["Une la carga con el equipo.", "Eso lo hace un accesorio de izaje."], "Accesorio de izaje"),
        ("Carga total", "Una pieza de ejemplo tiene 700 kg y sus accesorios 40 kg. ¿Cuántos kilogramos son en total?", ["Se suman la pieza y los accesorios.", "700 más 40 son 740."], "740 kg"),
    ],
    mistakes=[("Pensar que una carga liviana permite pasar debajo de ella.", "Cualquier carga suspendida puede lesionar si cae.", "Nadie permanece bajo una carga suspendida, sea cual sea su masa."),
              ("Creer que ver un video de maniobras habilita para ayudar.", "La maniobra exige capacitación presencial, autorización y plan.", "Los estudiantes no participan en maniobras; observan los conceptos en papel.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es un equipo de levante?", "Una máquina o dispositivo para elevar y trasladar cargas, como una grúa", "Una herramienta para medir alturas", "Un andamio para trabajar en altura", "Un equipo de levante mueve cargas; los instrumentos miden y los andamios dan acceso."),
        ("abc", "En Montaje Industrial: ¿qué es un accesorio de izaje?", "Un elemento que une la carga con el equipo, como una eslinga o un grillete", "El casco del operador", "El cartel de la zona de exclusión", "Los accesorios unen carga y equipo; el casco y el cartel son otras medidas."),
        ("abc", "En Montaje Industrial: ¿qué regla general vale para una carga suspendida?", "Nadie debe permanecer bajo ella", "Pueden pasar personas con casco", "Pueden pasar si la carga es liviana", "Una carga suspendida puede caer y lesionar, sin importar el casco ni su masa."),
        ("=", "{F} ¿Cuántos kilogramos suman la viga y los accesorios de izaje?", "900+60", "Se suman la masa de la viga y la de los accesorios.", " kg"),
        ("abc", "{F} ¿Qué peligro de la ficha se relaciona con el sector de suelo blando?", "El vuelco del equipo", "El viento", "La línea eléctrica", "El suelo blando puede ceder bajo el equipo y volcarlo."),
        ("abc", "{F} ¿Por qué se prohíbe permanecer bajo la carga suspendida?", "Porque si la carga cae puede aplastar a quien esté debajo", "Porque la carga proyecta sombra", "Porque se pierde tiempo de trabajo", "El riesgo de caída de la carga es la razón de la prohibición."),
        ("=", "{F} Si 1 kg pesa 10 N en la regla de ejemplo, ¿cuántos newtons pesa la carga total (viga y accesorios)?", "(900+60)*10", "Se suma la masa total y se multiplica por 10.", " N"),
        ("abc", "{F} Hay viento fuerte el día de la maniobra. ¿Qué corresponde según el plan?", "Que las personas responsables evalúen y suspendan la maniobra si corresponde", "Que se haga más rápido para evitar el viento", "Que un estudiante decida si se sigue", "El plan considera el viento, y decide quien tiene la responsabilidad."),
        ("abc", "{F} ¿Quién decide si se inicia el izaje?", "Las personas responsables del plan firmado, no un estudiante ni un ayudante", "Cualquier persona presente", "El proveedor de las piezas", "El inicio lo decide quien firma y responde por el plan."),
        ("abc", "{F} Un compañero dice: «vi un video sobre amarrar cargas, así que puedo ayudar a izar». ¿Qué respuesta es correcta?", "Es falso: la maniobra exige capacitación presencial, autorización y plan; los estudiantes no participan", "Es cierto, si usa casco", "Es cierto, si ayuda solo con cargas pequeñas", "Un video no sustituye la capacitación ni la autorización."),
        ("abc", "Durante una visita de ejemplo, una carga se balancea y atrapa a una persona contra una pared. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a empujar la carga", "Esperar a ver si se suelta sola", "Intervenir sin formación puede causar otra lesión; se avisa a quienes pueden actuar."),
        ("=", "{F} Si el equipo de ejemplo puede levantar 1.500 kg en esa posición, ¿cuántos kg de margen quedan sobre la carga total?", "1500-(900+60)", "Se resta la carga total a la capacidad de ejemplo.", " kg"),
        ("abc", "{F} El jefe de terreno dice que se puede izar sin la firma del prevencionista «porque llegó tarde». ¿Qué respuesta es correcta?", "No: el plan necesita todas las firmas para comenzar", "Sí, si la carga es liviana", "Sí, si se firma al terminar", "Sin todas las firmas, el plan no está aprobado y la maniobra no comienza."),
    ],
    ctx=("abc", "Un proveedor de ejemplo te ofrece subirte a mirar de cerca cómo izan una viga desde el patio. ¿Qué respondes?", "Que no, porque las maniobras tienen zona de exclusión y solo permanecen en ella personas autorizadas", "Que sí, si te quedas un momento", "Que sí, si usas casco y chaleco", "La zona de exclusión impide la presencia de personas ajenas a la maniobra."),
    sc=[
        ("En Montaje Industrial: ¿qué une la carga con el equipo de levante?", "Los accesorios de izaje", "Eslingas y grilletes son ejemplos de accesorios."),
        ("¿Quién puede permanecer bajo una carga suspendida?", "Nadie", "Una carga suspendida puede caer y lesionar a las personas."),
        ("¿Qué documento firmado reúne los responsables de una maniobra?", "El plan de izaje", "Sin plan firmado la maniobra no comienza."),
    ],
    op=("Plan de ejemplo: se iza una pieza de 1.200 kg con accesorios de 80 kg. Peligros anotados: caída de la carga, suelo blando y personas bajo la carga. Escribe (a) la carga total, (b) cuántos newtons pesa con la regla de 1 kg = 10 N, (c) una regla sobre las personas bajo la carga, (d) por qué un estudiante no participa en la maniobra.",
        "(a) 1.200 + 80 = 1.280 kg. (b) 1.280 × 10 = 12.800 N. (c) Nadie permanece bajo una carga suspendida. (d) Porque la maniobra exige capacitación presencial, autorización y plan, y este cuaderno no habilita para ella.",
        ["suma la carga total", "calcula el peso en newtons", "enuncia la regla de las personas", "explica por qué no participa"],
        ["hoja con las cuatro respuestas"],
        ["olvidar los accesorios", "decir que se puede pasar bajo cargas livianas", "creer que un video habilita"],
        "Pregunta: «¿qué incluye la carga total?». Si no responde, pídele que relea el ejemplo de carga total."),
    reinforce="Escribe tres peligros de un izaje y, junto a cada uno, una medida de prevención.",
    extend="Explica con un ejemplo por qué ninguna carga suspendida se considera inofensiva.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (tabla de capacidad de ejemplo de un equipo de levante; valores inventados, no reales). Radio 6 m: 5.000 kg. Radio 10 m: 3.000 kg. Radio 14 m: 1.800 kg. "
     "Accesorios de la caja: eslinga E-1, con rótulo de 2.000 kg y certificado de inspección vigente; grillete G-1, con rótulo de 1.000 kg y certificado de inspección vencido; eslinga E-2, sin rótulo legible.")
build(
    O6, 2, F,
    use="Aprenderé a leer una tabla de capacidad, a reconocer qué accesorios pueden usarse según su rótulo y su certificado, y qué función tiene cada rol en un izaje.",
    prior=["Sé qué es un accesorio de izaje.", "Sé qué es una capacidad rotulada.", "Sé leer una tabla."],
    explain=[
        "La tabla de capacidad de un equipo indica cuánto puede levantar según el radio, que es la distancia horizontal entre el eje del equipo y la carga. A mayor radio, menor capacidad. La carga total que se compara con la tabla incluye la pieza y todos los accesorios. La tabla la entrega el fabricante y no se modifica.",
        "Un accesorio de izaje se considera utilizable solo si tiene un rótulo legible con su capacidad y un certificado de inspección vigente. Si no tiene rótulo legible o su certificado está vencido, se saca de servicio y se avisa al supervisor: nadie escribe un rótulo ni estima una capacidad. Los documentos de un izaje son el plan, la tabla de capacidad, los certificados y el registro de inspecciones. Los roles son el operador autorizado, que maneja el equipo; el señalero, que guía con señales acordadas; el supervisor de izaje, que dirige la maniobra; el prevencionista; y el jefe de terreno.",
        f"Las señales y la manera de usar el equipo se aprenden con un instructor autorizado. {EMER} {AVISO}",
    ],
    vocab=[("radio de trabajo", "distancia horizontal entre el eje del equipo y la carga"), ("tabla de capacidad", "tabla del fabricante que indica cuánto puede levantar el equipo según el radio"), ("certificado de inspección", "documento que acredita que un accesorio fue revisado, con fecha de vigencia"), ("sacar de servicio", "dejar un accesorio sin uso por no cumplir sus requisitos"), ("operador autorizado", "persona habilitada para manejar el equipo de levante"), ("supervisor de izaje", "persona que dirige la maniobra y responde por el plan")],
    worked=[
        ("Leer la tabla", "Una tabla de ejemplo dice: radio 8 m, 4.000 kg; radio 12 m, 2.500 kg. ¿Cuántos kg menos se levantan a 12 m que a 8 m?", ["Se resta la capacidad menor a la mayor.", "4.000 menos 2.500 son 1.500 kg."], "1.500 kg menos"),
        ("Accesorio sin certificado", "Un grillete de ejemplo tiene rótulo legible pero su certificado venció el mes pasado. ¿Puede usarse?", ["Debe tener rótulo legible y certificado vigente.", "El certificado está vencido: se saca de servicio."], "No, se saca de servicio"),
    ],
    mistakes=[("Escribir a mano un rótulo ilegible porque «se ve de 2.000 kg».", "La capacidad la fija el fabricante y la verifica una inspección autorizada.", "Saca el accesorio de servicio y avisa al supervisor."),
              ("Comparar la tabla solo con el peso de la pieza.", "Los accesorios también pesan y forman parte de la carga.", "Suma pieza y accesorios antes de comparar.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el radio de trabajo de un equipo de levante?", "La distancia horizontal entre el eje del equipo y la carga", "La altura a la que sube la carga", "El largo de la pieza que se levanta", "El radio se mide en horizontal desde el eje del equipo hasta la carga."),
        ("abc", "En Montaje Industrial: ¿qué indica la tabla de capacidad de un equipo?", "Cuánto puede levantar según el radio de trabajo", "Cuánto cuesta arrendarlo", "Cuántas horas puede trabajar por día", "La tabla informa capacidades; costo y horas son otros datos."),
        ("abc", "En Montaje Industrial: ¿qué debe tener un accesorio de izaje para poder usarse?", "Un rótulo legible de capacidad y un certificado de inspección vigente", "Un color llamativo", "Pocas horas de uso", "Sin rótulo legible y certificado vigente no se conoce ni se verifica su capacidad."),
        ("abc", "{F} Según la tabla, ¿qué ocurre con la capacidad al aumentar el radio?", "Disminuye", "Aumenta", "No cambia", "La tabla muestra 5.000, 3.000 y 1.800 kg para radios cada vez mayores."),
        ("=", "{F} ¿Cuántos kilogramos menos puede levantar el equipo a 14 m que a 6 m?", "5000-1800", "Se resta la capacidad a 14 m a la capacidad a 6 m.", " kg"),
        ("abc", "{F} ¿Qué accesorio de la caja no puede usarse por tener el certificado vencido?", "El grillete G-1", "La eslinga E-1", "Ninguno", "G-1 tiene el certificado vencido; E-1 lo tiene vigente."),
        ("abc", "{F} ¿Qué corresponde con la eslinga E-2, que no tiene rótulo legible?", "Sacarla de servicio y avisar al supervisor, porque no se conoce su capacidad", "Usarla si parece resistente", "Escribirle el rótulo con un plumón", "Sin rótulo legible no se conoce la capacidad; no se estima ni se inventa."),
        ("=", "{F} ¿Cuántos kilogramos más puede levantar el equipo a 10 m que a 14 m?", "3000-1800", "Se resta la capacidad a 14 m a la capacidad a 10 m.", " kg"),
        ("abc", "{F} Una carga total de 2.500 kg a un radio de 14 m, ¿está dentro de la capacidad de la tabla?", "No: a 14 m la capacidad es de 1.800 kg", "Sí: a 10 m son 3.000 kg", "Sí: 2.500 es menor que 5.000", "Hay que usar la capacidad del radio de trabajo, que a 14 m es 1.800 kg."),
        ("abc", "{F} Un compañero dice que escribirá el rótulo de E-2 «porque se ve de 2.000 kg». ¿Qué respuesta es correcta?", "No: la capacidad la fija el fabricante y la verifica una inspección autorizada; escribir un rótulo es peligroso", "Sí, si usa una letra clara", "Sí, si el accesorio no se ve gastado", "Un rótulo inventado puede llevar a una sobrecarga."),
        ("abc", "En un izaje de ejemplo, ¿quién guía la maniobra con señales acordadas?", "El señalero", "Cualquier persona que vea la carga", "El proveedor de las piezas", "Las señales las da una persona designada, para no confundir al operador."),
        ("abc", "{F} Una carga de 1.700 kg con accesorios de 150 kg se estudia para un radio de 14 m. ¿Está dentro de la tabla?", "No: 1.700 + 150 = 1.850 kg supera los 1.800 kg", "Sí: 1.700 kg es menor que 1.800 kg", "Sí: los accesorios no cuentan en la carga", "Los accesorios forman parte de la carga total que se compara con la tabla."),
        ("=", "{F} Para un radio de 10 m y una carga total de 2.400 kg, ¿cuántos kilogramos de margen quedan?", "3000-2400", "Se resta la carga total a la capacidad a 10 m.", " kg"),
    ],
    ctx=("abc", "Un ayudante de ejemplo propone usar el grillete G-1 «solo por hoy» aunque su certificado esté vencido. ¿Qué respondes?", "Que no: se saca de servicio y se avisa al supervisor", "Que sí, si la carga es liviana", "Que sí, si se anota después", "Un certificado vencido deja al accesorio sin verificación vigente, sin importar la carga."),
    sc=[
        ("En Montaje Industrial: ¿qué sucede con la capacidad al aumentar el radio?", "Disminuye", "A mayor distancia de la carga, el equipo levanta menos."),
        ("¿Qué incluye la carga total que se compara con la tabla?", "La pieza y todos los accesorios", "Los accesorios también pesan y suman a la carga."),
        ("¿Qué se hace con un accesorio sin rótulo legible?", "Se saca de servicio y se avisa al supervisor", "Sin rótulo legible no se conoce su capacidad."),
    ],
    op=("Ficha de ejemplo: tabla de un equipo: radio 5 m, 4.500 kg; radio 9 m, 2.800 kg; radio 13 m, 1.600 kg. Eslinga E-9 con rótulo legible y certificado vigente; grillete G-9 con rótulo legible y certificado vencido. Una pieza de 2.500 kg con accesorios de 100 kg se estudia a 9 m. Escribe (a) la carga total, (b) si está dentro de la tabla a 9 m y cuánto margen queda, (c) qué accesorio no puede usarse y por qué.",
        "(a) 2.500 + 100 = 2.600 kg. (b) Sí, porque 2.600 es menor que 2.800; el margen es 200 kg. (c) El grillete G-9, porque su certificado está vencido: se saca de servicio.",
        ["suma la carga total", "compara con la capacidad y calcula el margen", "identifica el accesorio vencido"],
        ["hoja con los tres puntos"],
        ["olvidar los accesorios", "usar la capacidad de otro radio", "aceptar el accesorio vencido"],
        "Pregunta: «¿qué capacidad se usa si el radio es 9 m?». Si no responde, pídele que relea la regla de la tabla."),
    reinforce="Inventa una tabla de capacidad con tres radios y calcula cuánto baja la capacidad entre el primero y el último.",
    extend="Explica con un ejemplo por qué un rótulo inventado a mano es más peligroso que un accesorio sin usar.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (plan de izaje de ejemplo, borrador, inventado). Pieza P-1: 1.800 kg. Pieza P-2: 2.600 kg. Accesorios de izaje: 120 kg por pieza. Tabla de capacidad del equipo de ejemplo: radio 6 m, 5.000 kg; radio 10 m, 3.000 kg; radio 14 m, 1.800 kg. "
     "Radios previstos: P-1 a 10 m; P-2 a 14 m. Regla de ejemplo para el cálculo en papel: 1 kg pesa 10 N.")
build(
    O6, 3, F,
    use="Aprenderé a calcular la carga total de un izaje en un borrador de plan, a compararla con la capacidad de la tabla, a calcular el margen y el porcentaje de uso y a reconocer cuándo el plan debe replantearse.",
    prior=["Sé leer una tabla de capacidad.", "Sé qué es la carga total.", "Sé calcular un porcentaje simple."],
    explain=[
        "Para revisar un borrador de plan se calcula la carga total de cada pieza, sumando la masa de la pieza y la de los accesorios. Luego se busca en la tabla la capacidad del equipo para el radio previsto y se compara. El margen es la capacidad menos la carga total, y el porcentaje de uso es la carga total por 100 dividida por la capacidad. Si la carga total supera la capacidad, el izaje no se aprueba.",
        "Cuando una pieza supera la capacidad, el plan no se fuerza ni se modifica la tabla. Las personas responsables replantean el plan: estudian otro radio, otro equipo o una división de la pieza aprobada por el proyecto, y vuelven a calcular y a firmar. Todo el cálculo queda en el plan, con fecha y firma. Un cálculo de planilla nunca autoriza por sí solo a mover una carga.",
        f"Las masas, las capacidades y los porcentajes de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("carga total", "suma de la masa de la pieza y de todos los accesorios"), ("margen de capacidad", "diferencia entre la capacidad y la carga total"), ("porcentaje de uso", "carga total por 100 dividida por la capacidad"), ("replantear el plan", "rehacer el plan con otro radio, equipo o división de la pieza, y volver a firmarlo"), ("borrador de plan", "versión del plan aún sin aprobar")],
    worked=[
        ("Margen", "Una pieza de ejemplo tiene carga total de 2.100 kg y la capacidad al radio previsto es 3.500 kg. ¿Cuál es el margen?", ["El margen es la capacidad menos la carga total.", "3.500 menos 2.100 son 1.400 kg."], "1.400 kg"),
        ("Porcentaje de uso", "Una carga total de 1.500 kg y una capacidad de 2.500 kg. ¿Qué porcentaje de la capacidad se usa?", ["Se multiplica 1.500 por 100 y se divide entre 2.500.", "150.000 entre 2.500 son 60."], "60 %"),
    ],
    mistakes=[("Cambiar la capacidad de la tabla para que la pieza «pase».", "La tabla es del fabricante y se basa en pruebas; modificarla es falsear el cálculo.", "Replantea el plan con otro radio, equipo o división aprobada."),
              ("Calcular la carga sin los accesorios.", "Los accesorios pesan y forman parte de lo que levanta el equipo.", "Suma pieza y accesorios antes de comparar.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la carga total de un izaje?", "La suma de la pieza y de todos los accesorios", "Solo la masa de la pieza", "La masa del equipo de levante", "La carga total incluye todo lo que el equipo debe levantar."),
        ("abc", "En Montaje Industrial: ¿con qué se compara la carga total en el plan?", "Con la capacidad de la tabla para el radio previsto", "Con la carga de la pieza más liviana", "Con el peso del operador", "La capacidad del equipo depende del radio y es la referencia."),
        ("abc", "En Montaje Industrial: ¿qué es el margen de capacidad?", "La diferencia entre la capacidad y la carga total", "La suma de la capacidad y la carga", "El radio de trabajo", "El margen muestra cuánto falta para llegar al límite."),
        ("=", "{F} ¿Cuál es la carga total de P-1, con pieza y accesorios?", "1800+120", "Se suman la masa de la pieza y la de los accesorios.", " kg"),
        ("=", "{F} ¿Cuál es la carga total de P-2, con pieza y accesorios?", "2600+120", "Se suman la masa de la pieza y la de los accesorios.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos de margen tiene P-1 al radio previsto de 10 m?", "3000-(1800+120)", "Se resta la carga total de P-1 a la capacidad a 10 m.", " kg"),
        ("abc", "{F} ¿Está P-2 dentro de la capacidad al radio previsto?", "No: 2.720 kg supera los 1.800 kg de capacidad a 14 m", "Sí: 2.720 kg es menor que 3.000 kg", "Sí: a 14 m la capacidad es mayor que a 10 m", "A 14 m la capacidad es 1.800 kg y la carga total la excede."),
        ("=", "{F} ¿Cuántos kilogramos supera P-2 la capacidad a 14 m?", "(2600+120)-1800", "Se resta la capacidad a la carga total de P-2.", " kg"),
        ("=", "{F} ¿Qué porcentaje de la capacidad a 10 m usa la carga total de P-1?", "(1800+120)*100//3000", "Se multiplica la carga total por 100 y se divide entre la capacidad.", " %"),
        ("abc", "{F} Un compañero propone «subir la capacidad a 14 m de 1.800 a 2.800 kg en la tabla para que P-2 pase». ¿Qué respuesta es correcta?", "No: la tabla es del fabricante y no se cambia; el plan debe replantearse por las personas responsables", "Sí, si todos están de acuerdo", "Sí, si se anota con lápiz", "Modificar la tabla es falsear el cálculo y puede causar una caída de carga."),
        ("abc", "{F} ¿Qué pueden estudiar las personas responsables para P-2 a partir de este borrador?", "Otro radio, otro equipo o una división de la pieza aprobada por el proyecto, y rehacer el plan", "Izar igual con más ayudantes", "Izar rápido para que no se note", "Se corrige el plan y se firma de nuevo; no se fuerza la maniobra."),
        ("=", "{F} Si P-2 se estudiara a un radio de 6 m, ¿cuántos kilogramos de margen tendría?", "5000-(2600+120)", "Se resta la carga total de P-2 a la capacidad a 6 m.", " kg"),
        ("=", "{F} ¿Cuántos newtons pesa la carga total de P-1 con la regla de la ficha?", "(1800+120)*10", "Se suma la masa total y se multiplica por 10.", " N"),
    ],
    ctx=("abc", "El jefe de terreno de ejemplo te dice: «el plan de P-2 está casi bien, solo se pasa 920 kg; sigamos y lo ajustamos después». ¿Qué respondes?", "Que un plan que excede la capacidad no se aprueba: se replantea y se firma de nuevo antes de mover la pieza", "Que sí, porque 920 kg es poco", "Que sí, si se avisa al operador", "Una carga sobre la capacidad es un riesgo de caída; no se ajusta durante la maniobra."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el margen de capacidad?", "Capacidad menos carga total", "El margen es lo que falta para el límite."),
        ("¿Qué se hace si la carga total supera la capacidad?", "Se replantea el plan y se firma de nuevo", "Una maniobra que excede la capacidad no se fuerza."),
        ("¿Quién puede modificar la tabla de capacidad?", "Nadie en la obra: es del fabricante", "La tabla se basa en pruebas del fabricante."),
    ],
    op=("Ficha de ejemplo: pieza Q-1 de 2.200 kg con accesorios de 100 kg; capacidad de la tabla al radio previsto de 12 m: 2.500 kg; capacidad a 7 m: 4.000 kg. Escribe (a) la carga total, (b) el margen a 12 m y el porcentaje de uso, (c) qué conclusión saca el plan y si Q-1 se aprobaría a 7 m.",
        "(a) 2.200 + 100 = 2.300 kg. (b) Margen: 2.500 − 2.300 = 200 kg. Uso: 2.300 × 100 ÷ 2.500 = 92 %. (c) A 12 m está dentro de la capacidad con poco margen; a 7 m el margen sería 4.000 − 2.300 = 1.700 kg. Cualquier decisión la toman las personas responsables y se registra en el plan firmado.",
        ["suma la carga total", "calcula margen y porcentaje", "compara con otro radio", "aclara quién decide"],
        ["hoja con los cálculos y la conclusión"],
        ["olvidar los accesorios", "dividir al revés el porcentaje", "decidir la maniobra sin el plan"],
        "Pregunta: «¿qué pasa si el margen fuera negativo?». Si no responde, pídele que relea el párrafo del plan que se replantea."),
    reinforce="Calcula en papel la carga total y el margen de una pieza de 1.400 kg con accesorios de 60 kg y una capacidad de 2.000 kg.",
    extend="Explica con un ejemplo por qué una tabla de capacidad no se modifica en la obra.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (traslado de ejemplo, inventado). Se trasladan 18 piezas de 650 kg cada una en un camión con capacidad de carga rotulada de 4.000 kg (valor de ejemplo). La distancia al sitio de montaje es de 120 km y el camión recorre 60 km por hora en promedio. "
     "Un viaje completo incluye ida, vuelta y 1 hora en total para cargar y descargar (dato de ejemplo).")
build(
    O6, 4, F,
    use="Aprenderé qué es la estiba y el transporte seguro de piezas, a calcular piezas por viaje, viajes y tiempos en una planilla y a reconocer una sobrecarga.",
    prior=["Sé qué es una capacidad rotulada.", "Sé dividir y multiplicar números enteros.", "Sé qué es la carga total."],
    explain=[
        "La estiba es la disposición y sujeción de la carga en un vehículo para transportarla sin que se mueva, se vuelque ni se caiga. Una estiba segura reparte el peso, considera el centro de gravedad, que es el punto donde puede imaginarse concentrado el peso, y respeta la capacidad de carga rotulada del vehículo. Cómo se sujetan las piezas, con qué amarras y con qué nudos, lo enseña un instructor autorizado y lo verifica personal responsable: este cuaderno no entrega esas técnicas.",
        "Una planilla de transporte calcula cuántas piezas caben por viaje sin superar la capacidad (división entera de la capacidad entre la masa de cada pieza), cuántos viajes hacen falta y cuánto tarda cada viaje. Los documentos del traslado son la guía de despacho, el plan de transporte y los permisos necesarios según la norma vigente. Sobrecargar un vehículo es un peligro para el conductor y para las personas en el camino.",
        f"Las cifras son de ejemplo. Cargar, descargar o sujetar piezas es una tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("estiba", "disposición y sujeción de la carga en un vehículo para transportarla"), ("centro de gravedad", "punto donde puede imaginarse concentrado el peso de una carga"), ("capacidad de carga rotulada", "masa máxima de carga que indica el fabricante del vehículo"), ("guía de despacho", "documento que acompaña la carga durante el traslado"), ("sobrecarga", "carga mayor que la capacidad rotulada")],
    worked=[
        ("Piezas por viaje", "Un camión de ejemplo con capacidad de 3.000 kg lleva piezas de 400 kg. ¿Cuántas caben por viaje?", ["Se divide 3.000 entre 400 y se toma la parte entera.", "3.000 entre 400 da 7 y sobra."], "7 piezas"),
        ("Número de viajes", "Hay que llevar 20 piezas y caben 5 por viaje. ¿Cuántos viajes hacen falta?", ["Se divide el total de piezas entre las que caben por viaje.", "20 entre 5 son 4."], "4 viajes"),
    ],
    mistakes=[("Cargar una pieza más porque «se pasa solo un poco».", "Superar la capacidad rotulada es una sobrecarga peligrosa.", "Respeta la capacidad y haz un viaje más si hace falta."),
              ("Creer que un video de amarras habilita para estibar.", "La sujeción de la carga exige capacitación y verificación.", "La estiba la hace y la verifica personal autorizado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la estiba de una carga?", "La disposición y sujeción de la carga en un vehículo para transportarla sin que se mueva", "El cálculo del peso de la carga", "El permiso de circulación del vehículo", "La estiba trata de ubicar y sujetar; el peso y el permiso son otras cosas."),
        ("abc", "En Montaje Industrial: ¿qué es la capacidad de carga rotulada de un camión?", "La masa máxima de carga que indica el fabricante", "La velocidad máxima del camión", "El largo de la tolva", "La capacidad rotulada es el límite de carga del vehículo."),
        ("abc", "En Montaje Industrial: ¿qué es el centro de gravedad de una carga?", "El punto donde puede imaginarse concentrado su peso", "El punto más alto de la carga", "El punto donde se pone el rótulo", "El centro de gravedad resume dónde actúa el peso de la carga."),
        ("=", "{F} ¿Cuántos kilogramos pesan 6 piezas?", "6*650", "Se multiplican las piezas por la masa de cada una.", " kg"),
        ("=", "{F} ¿Cuántas piezas caben por viaje sin superar la capacidad rotulada?", "4000//650", "Se divide la capacidad entre la masa de cada pieza y se toma la parte entera.", " piezas"),
        ("=", "{F} Si por viaje caben 6 piezas, ¿cuántos viajes hacen falta para las 18 piezas?", "18//6", "Se divide el total de piezas entre las que caben por viaje.", " viajes"),
        ("=", "{F} ¿Cuántas horas dura el viaje de ida a 60 km por hora?", "120//60", "Se divide la distancia entre la velocidad.", " horas"),
        ("=", "{F} ¿Cuántas horas dura un viaje completo, con ida, vuelta y 1 hora de carga y descarga?", "120//60*2+1", "Se suman la ida, la vuelta y la hora de carga y descarga.", " horas"),
        ("=", "{F} Si cada viaje completo dura 5 horas, ¿cuántas horas suman los 3 viajes?", "3*5", "Se multiplican los viajes por las horas de cada uno.", " horas"),
        ("abc", "{F} Un conductor propone llevar 7 piezas «porque solo se pasa por 550 kg». ¿Qué respuesta es correcta?", "No: 7 piezas pesan 4.550 kg y superan la capacidad rotulada de 4.000 kg", "Sí, porque 550 kg es poco", "Sí, si se va más despacio", "Superar la capacidad es una sobrecarga, aunque se vaya despacio."),
        ("abc", "{F} Un compañero dice: «hago la estiba con los nudos que vi en un video». ¿Qué respuesta es correcta?", "Es falso: la sujeción exige capacitación, autorización y verificación por personal responsable", "Es cierto, si los nudos se ven firmes", "Es cierto, si el viaje es corto", "Un video no sustituye la capacitación ni la verificación."),
        ("=", "{F} Si el camión llevara 6 piezas, ¿cuántos kilogramos le sobran respecto de la capacidad rotulada?", "4000-6*650", "Se resta la carga de las 6 piezas a la capacidad.", " kg"),
        ("abc", "Durante una visita de ejemplo, una carga se desplaza en un camión y amenaza caer a la vereda con gente. ¿Qué corresponde según las reglas generales?", "Alejarte de la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sostener la carga", "Subirte al camión a acomodarla", "Una carga que se mueve es un peligro; lo atienden personas capacitadas."),
    ],
    ctx=("abc", "Un jefe de ejemplo dice: «cargue 7 piezas hoy para ahorrar un viaje; el camión aguanta». ¿Qué respondes?", "Que 7 piezas superan la capacidad rotulada de 4.000 kg y que se hacen los viajes que correspondan", "Que sí, porque ahorrar un viaje es lo importante", "Que sí, si se maneja con cuidado", "La capacidad rotulada es un límite; ahorrar un viaje no justifica sobrecargar."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calculan las piezas por viaje?", "Dividiendo la capacidad entre la masa de cada pieza y tomando la parte entera", "No se pueden cargar fracciones de pieza."),
        ("¿Qué es una sobrecarga?", "Una carga mayor que la capacidad rotulada", "Superar el límite del fabricante es peligroso."),
        ("¿Quién hace y verifica la sujeción de la carga?", "Personal autorizado y responsable", "La estiba exige capacitación y verificación."),
    ],
    op=("Ficha de ejemplo: 15 piezas de 500 kg; camión de capacidad rotulada de 3.000 kg; distancia de 90 km a 45 km por hora; 1 hora de carga y descarga por viaje completo. Escribe (a) cuántas piezas caben por viaje, (b) cuántos viajes hacen falta, (c) cuántas horas dura un viaje completo, (d) por qué no se carga una pieza más aunque quepa «justo».",
        "(a) 3.000 ÷ 500 = 6 piezas. (b) 15 ÷ 6 = 2 viajes y sobran 3 piezas, así que hacen falta 3 viajes. (c) Ida: 90 ÷ 45 = 2 horas; vuelta, 2 horas; más 1 hora: 5 horas. (d) Porque 7 piezas pesan 3.500 kg y superan los 3.000 kg rotulados: es una sobrecarga.",
        ["calcula las piezas por viaje", "calcula los viajes con redondeo hacia arriba", "calcula el tiempo", "explica la sobrecarga"],
        ["hoja con los cuatro cálculos"],
        ["no redondear los viajes hacia arriba", "olvidar la vuelta", "cargar una pieza más"],
        "Pregunta: «¿qué pasa si sobra una pieza para el último viaje?». Si no responde, pídele que relea el cálculo del número de viajes."),
    reinforce="Calcula en planilla cuántas piezas de 300 kg caben en un camión de 2.000 kg.",
    extend="Explica con un ejemplo por qué una sobrecarga es un peligro también para las personas que no están en la obra.",
)

# FIN

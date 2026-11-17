"""Construcción TP 3.º medio: OAE-07 (muestras y ensayos: documentos y registros), OAE-08 (registros de gestión de obra) y OAE-09 (normas y simbología de seguridad). Solo conceptos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_cons_common import AVISO, EMER, build

O7 = "TP-CONS-3-OAE-07"
O8 = "TP-CONS-3-OAE-08"
O9 = "TP-CONS-3-OAE-09"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Obra «Bodega Pinar» (ficticia): el hormigón llega en 3 camiones de ejemplo, de 8 m³ cada uno. La especificación de ejemplo pide anotar por cada camión 3 datos: "
     "hora de llegada, número de guía y rótulo de la muestra que separa personal capacitado. El laboratorio de ejemplo «Lab Sur» (ficticio) recibe las muestras y entrega un informe. "
     "Riesgos anotados en la obra: polvo de cemento, salpicaduras sobre la piel y los ojos, y levantamiento de cargas pesadas.")
build(
    O7, 1, F,
    use="Aprenderé qué es una muestra, qué papel cumple el laboratorio, qué documentos respaldan el análisis de la calidad y qué riesgos rodean este trabajo.",
    prior=["Sé leer una ficha con datos.", "Sé multiplicar y sumar números enteros.", "Sé que una obra deja registros escritos."],
    explain=[
        "Para saber si un material de obra cumple lo que pide el proyecto, no basta mirarlo: se analiza una muestra, que es una porción representativa separada del material de la obra. La muestra se rotula, es decir, se le pone una identificación escrita (qué es, de dónde viene y cuándo). Un laboratorio analiza muestras y entrega un informe de ensayo: el documento con los resultados. La especificación técnica dice qué se debe cumplir, y el registro de la obra anota qué llegó y qué se muestreó.",
        "Los materiales que se analizan son, por ejemplo, el hormigón, los suelos y otros materiales de la obra. Los riesgos más comunes son el polvo, el contacto del producto con la piel o los ojos y el levantamiento de cargas. La prevención sigue la jerarquía de controles: primero eliminar o reducir el riesgo en su origen, luego usar protecciones colectivas y, al final, los elementos de protección personal (EPP). La toma de muestras y los ensayos los hace personal capacitado y autorizado, según la norma vigente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("muestra", "porción representativa de un material, separada para analizar su calidad"), ("rótulo", "identificación escrita de la muestra: qué es, de dónde viene y cuándo"), ("laboratorio", "lugar que analiza muestras y entrega resultados"), ("informe de ensayo", "documento del laboratorio con los resultados de analizar las muestras"), ("registro", "anotación escrita de lo que ocurre en la obra"), ("jerarquía de controles", "orden para prevenir riesgos: eliminar, proteger en grupo y, al final, proteger a la persona"), ("EPP", "elementos de protección personal")],
    worked=[
        ("Elegir el documento", "Una jefa de obra de ejemplo quiere comprobar qué resultados entregó el laboratorio sobre un suelo de relleno. ¿Qué documento consulta?", ["Los resultados del análisis los entrega el laboratorio.", "El documento donde se escriben es el informe de ensayo."], "El informe de ensayo"),
        ("Contar rótulos", "En una obra de ejemplo llegan 5 camiones y por cada uno se rotula 1 muestra. ¿Cuántos rótulos hay que escribir?", ["Hay 1 rótulo por camión.", "5 camiones por 1 rótulo dan 5."], "5 rótulos"),
    ],
    mistakes=[("Pensar que cualquier trabajador puede tomar la muestra «porque es solo recoger un poco».", "La toma de muestras exige personal capacitado y norma vigente para que el resultado sea válido y seguro.", "Reconoce el concepto y deja la tarea a personal autorizado."),
              ("Mezclar el informe del laboratorio con el registro de la obra como si fueran el mismo documento.", "El laboratorio informa resultados; la obra registra qué llegó y qué se muestreó.", "Archiva ambos y relaciónalos por el rótulo.")],
    T=[
        ("abc", "En Construcción: ¿qué es una muestra de hormigón?", "Una porción representativa del hormigón de la obra, separada para analizar su calidad", "Todo el hormigón de un camión, que se envía al laboratorio", "El informe con los resultados que entrega el laboratorio", "La muestra es solo una porción representativa; el informe es otro documento."),
        ("abc", "En Construcción: ¿qué es un informe de ensayo?", "El documento del laboratorio con los resultados del análisis de las muestras", "El plano que dibuja la ubicación de cada muestra en la planta", "La lista de precios de los materiales de la obra", "El informe contiene resultados; el plano dibuja y la lista de precios indica costos."),
        ("abc", "¿Para qué sirve rotular una muestra?", "Para saber de qué parte de la obra viene y poder relacionar su resultado con ella", "Para que el laboratorio cobre menos por el análisis", "Para que el resultado valga igual aunque no se sepa de dónde viene", "Sin rótulo no se puede relacionar el resultado con la parte de la obra que representa."),
        ("=", "{F} ¿Cuántos m³ de hormigón llegan en total en los 3 camiones?", "3*8", "Se multiplican los camiones por los m³ de cada uno.", " m³"),
        ("abc", "{F} Un camión llegó sin número de guía anotado en el registro. ¿Qué corresponde?", "Dejar constancia de la falta en el registro y avisar al supervisor", "Inventar un número parecido al de otro camión", "Omitir ese camión del registro para no atrasar", "Un dato faltante se declara; inventarlo u omitirlo deja un registro falso o incompleto."),
        ("abc", "{F} ¿Qué riesgos anota la ficha para el trabajo con hormigón?", "Polvo de cemento, salpicaduras sobre piel y ojos, y levantamiento de cargas pesadas", "Solo el ruido de la mezcladora", "Descarga eléctrica y radiación solar", "La ficha anota exactamente el polvo, las salpicaduras y el levantamiento de cargas."),
        ("=", "{F} La especificación pide 3 datos por camión. ¿Cuántos datos se anotan en total para los 3 camiones?", "3*3", "Se multiplican los datos por camión por el número de camiones.", " datos"),
        ("abc", "{F} Un estudiante quiere separar él mismo la muestra «porque es fácil». ¿Qué corresponde?", "No hacerlo: la toma de muestras la realiza personal capacitado y autorizado, según la norma vigente", "Hacerlo si usa guantes", "Hacerlo si el laboratorio se lo permite por teléfono", "Los guantes o un permiso telefónico no reemplazan la capacitación ni la autorización exigidas."),
        ("ab", "{F} Un compañero dice: «con el informe de Lab Sur ya no hace falta el registro de camiones de la obra». ¿Qué respuesta es correcta?", "No: son documentos distintos y se complementan por el rótulo de cada muestra", "Sí: el informe reemplaza todos los registros de la obra", "El informe habla de resultados; el registro de la obra anota lo que llegó y se muestreó."),
        ("abc", "En la bodega de ejemplo cae un estante sobre un trabajador y queda atrapado. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar levantar el estante entre todos de inmediato", "Entrar a sacar al trabajador antes de avisar a alguien", "Acercarse sin ayuda puede provocar otro accidente; se avisa a quien corresponde."),
        ("=", "{F} Lab Sur cobra $15.000 (de ejemplo) por cada informe y se pide un informe por camión. ¿Cuánto cuesta en total?", "3*15000", "Se multiplica el valor de un informe por los tres camiones.", " pesos"),
        ("abc", "{F} Llegan al laboratorio dos muestras con el mismo rótulo «B-2». ¿Qué conclusión es la más prudente?", "No se sabe a qué camión corresponde cada una: hay que informar y aclararlo antes de usar los resultados", "El resultado de cualquiera sirve para ambos camiones", "Se descarta la muestra que se ve peor", "Con rótulos repetidos el resultado no se puede asignar con certeza a una parte de la obra."),
        ("=", "{F} Si se suma un cuarto camión y se pide un informe por camión a $15.000 (de ejemplo) cada uno, ¿cuánto cuestan los informes?", "(3+1)*15000", "Se suman los camiones y se multiplica por el valor de un informe.", " pesos"),
    ],
    ctx=("abc", "Un amigo ofrece pagarle a un estudiante por «sacar unas muestras» de una obra y escribir el resultado sin llevarlas al laboratorio. ¿Qué responde?", "Se niega: los resultados deben salir de un laboratorio y la toma la hace personal autorizado", "Acepta si el pago es bajo", "Acepta, porque ya conoce los documentos", "Un resultado sin laboratorio ni personal autorizado es falso y puede poner en riesgo a las personas."),
    sc=[
        ("En Construcción: ¿qué hace un laboratorio de obra?", "Analiza muestras y entrega un informe de ensayo con los resultados", "El laboratorio informa resultados; no decide por sí solo qué se hace en la obra."),
        ("¿Qué indica el rótulo de una muestra?", "Qué es, de dónde viene y cuándo se tomó", "El rótulo permite relacionar el resultado con la parte de la obra que representa."),
        ("¿Quién toma las muestras de la obra?", "Personal capacitado y autorizado, con norma vigente", "Este cuaderno no habilita para tomar muestras ni hacer ensayos."),
    ],
    op=("Obra de ejemplo «Taller Roble»: llegan 4 camiones de 6 m³ cada uno y por cada camión se rotula 1 muestra. El camión 3 llega sin guía. Escribe (a) cuántos m³ llegan en total, (b) cuántos rótulos hay, (c) qué haces con la guía que falta y a quién informas, (d) un riesgo del trabajo y quién debe tomar las muestras.",
        "(a) 4 por 6 son 24 m³. (b) 4 rótulos. (c) Dejo constancia de la guía faltante en el registro e informo al supervisor; no invento el número. (d) Polvo o levantamiento de cargas; las muestras las toma personal capacitado y autorizado según la norma vigente.",
        ["calcula bien los m³", "cuenta los rótulos", "declara la falta sin inventar", "nombra un riesgo y quién toma las muestras"],
        ["hoja con las cuatro respuestas"],
        ["inventar el número de guía", "decir que puede tomar la muestra", "confundir rótulos con camiones"],
        "Pregunta: «¿qué haces si falta un dato en el registro?». Si no responde, pídele que relea la regla de dejar constancia."),
    reinforce="Escribe tres documentos de este tema (informe de ensayo, registro de obra, especificación) y una frase sobre para qué sirve cada uno.",
    extend="Explica con un ejemplo inventado por qué un resultado sin rótulo claro no sirve para decidir nada en la obra.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (informe de ensayo descrito por escrito, de ejemplo, inventado). Especificación de ejemplo: el hormigón del elemento E-5 debe alcanzar un valor mínimo de 25 unidades de ejemplo (u.e.) "
     "a los 28 días. Informe de «Lab Sur» (ficticio): muestra M1, edad 7 días, valor 18 u.e.; muestra M2, edad 28 días, valor 27 u.e.; muestra M3, edad 28 días, valor 24 u.e. "
     "Regla de lectura de ejemplo: una muestra cumple si su valor obtenido es igual o mayor que el valor especificado, comparado a la edad que fija la especificación.")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario de un informe de ensayo, los roles que intervienen y cómo comparar un valor obtenido con el especificado.",
    prior=["Sé qué es una muestra y un rótulo.", "Sé comparar números enteros.", "Sé que un informe no se altera."],
    explain=[
        "Un informe de ensayo compara lo que se obtuvo con lo que se pidió. El valor especificado es el que fija la especificación técnica; el valor obtenido es el que midió el laboratorio. La edad de la muestra son los días transcurridos desde que se tomó, y la especificación dice a qué edad se compara. Una muestra cumple si su valor obtenido alcanza o supera el especificado a esa edad; si no, no cumple. La trazabilidad es poder seguir el camino de la muestra, desde la obra hasta el resultado, gracias al rótulo y a los registros.",
        "Cada rol tiene su tarea. El laboratorista hace el análisis y firma el informe. El supervisor técnico y el jefe de obra interpretan el informe y deciden los pasos siguientes. El proveedor entrega el material. Nadie corrige un número del informe por su cuenta: si hay un error, se pide al laboratorio una versión corregida y firmada. Un resultado que no cumple no se esconde: se informa de inmediato.",
        f"Esto se lee aquí con valores de ejemplo, sin valores reales. {EMER} {AVISO}",
    ],
    vocab=[("valor especificado", "valor que fija la especificación técnica"), ("valor obtenido", "valor que midió el laboratorio"), ("edad de la muestra", "días transcurridos desde que se tomó"), ("cumple", "el valor obtenido alcanza o supera el especificado a la edad indicada"), ("trazabilidad", "posibilidad de seguir el camino de la muestra hasta su resultado"), ("laboratorista", "persona que hace el análisis y firma el informe"), ("supervisor técnico", "persona que revisa y decide con base en los documentos")],
    worked=[
        ("Aplicar la regla", "Una especificación de ejemplo pide 30 u.e. a los 28 días. El laboratorio informa 33 u.e. a los 28 días. ¿Cumple?", ["Se compara el valor obtenido con el especificado a la edad indicada.", "33 es mayor que 30."], "Sí, cumple"),
        ("Edad distinta", "En otro informe de ejemplo, una muestra de 3 días tiene 10 u.e. y la especificación exige 30 u.e. a los 28 días. ¿Se puede decir que no cumple?", ["La especificación compara a los 28 días.", "Una muestra de 3 días no se compara con ese valor."], "No: aún no se puede concluir porque la edad es distinta"),
    ],
    mistakes=[("Comparar una muestra de pocos días con el valor pedido a los 28 días.", "La especificación fija la edad de comparación.", "Compara solo muestras de la edad que indica la especificación."),
              ("Corregir un valor del informe a mano para que «apruebe».", "Alterar un informe es una falta grave y esconde un problema.", "Informa y pide al laboratorio una versión corregida y firmada.")],
    T=[
        ("abc", "En Construcción: ¿qué es la trazabilidad de una muestra?", "Poder seguir su camino desde la obra hasta el resultado gracias al rótulo y los registros", "La rapidez con que el laboratorio entrega el informe", "El peso de la muestra al llegar al laboratorio", "La trazabilidad es seguir el camino documentado de la muestra, no la rapidez ni el peso."),
        ("abc", "¿Quién interpreta el informe y decide los pasos siguientes en la obra?", "El supervisor técnico junto con el jefe de obra", "El proveedor, que corrige el informe a su favor", "El laboratorista, que decide cómo se corrige la obra", "El laboratorio informa resultados; la decisión en la obra la toman quienes supervisan."),
        ("abc", "En un informe de ensayo, ¿qué es el valor obtenido?", "El valor que midió el laboratorio en la muestra", "El valor que fija la especificación técnica", "El precio que cobra el laboratorio", "El valor obtenido es el medido; el especificado es el que fija el proyecto."),
        ("abc", "{F} ¿Qué muestras se comparan con el valor especificado?", "Las de 28 días, porque la especificación fija esa edad", "Todas, incluida la de 7 días", "Solo la que tiene el valor más bajo", "Se compara a la edad que fija la especificación, que es 28 días."),
        ("=", "{F} ¿Cuántas u.e. sobre el mínimo tiene la muestra M2?", "27-25", "Se resta el valor especificado al valor obtenido de M2.", " u.e."),
        ("abc", "{F} ¿Cumple la muestra M3?", "No: 24 u.e. es menor que las 25 u.e. especificadas", "Sí: 24 es casi 25", "Sí: la regla acepta una diferencia de 1", "La regla pide igual o mayor valor; 24 no alcanza 25 y no se aceptan diferencias."),
        ("ab", "{F} Un jefe dice: «M1 tiene 18, menos que 25: ya sabemos que no cumple». ¿Qué respuesta es correcta?", "Todavía no se concluye: M1 tiene 7 días y la especificación compara a los 28 días", "Sí: cualquier valor bajo 25 incumple", "Para comparar hay que usar la edad que fija la especificación, no cualquier muestra."),
        ("=", "{F} ¿Cuántos días de diferencia de edad hay entre M1 y M2?", "28-7", "Se resta la edad de M1 a la edad de M2.", " días"),
        ("abc", "{F} A un informe de ejemplo le falta la fecha en que se tomó la muestra. ¿Qué corresponde?", "Pedir al laboratorio que lo aclare, porque sin fecha no se comprueba la edad", "Suponer que tiene 28 días", "Usar la fecha de hoy", "Sin fecha de toma no se puede saber la edad, y suponerla puede dar una conclusión falsa."),
        ("abc", "{F} Un encargado quiere cambiar a mano el valor de M3 de 24 a 25 «para que apruebe». ¿Qué corresponde?", "No: alterar un informe es una falta; se informa y se pide al laboratorio una versión corregida", "Hacerlo, porque es solo 1 u.e.", "Hacerlo si el jefe de obra lo pide de palabra", "Un informe no se cambia por pedido verbal; solo el laboratorio corrige y firma."),
        ("abc", "{F} Si el valor especificado subiera a 27 u.e. a los 28 días, ¿cuántas muestras de 28 días cumplirían?", "Una (M2, porque 27 es igual a 27)", "Dos, porque ambas están cerca", "Ninguna, porque el mínimo subió", "Con mínimo 27 cumple M2 (igual a 27) y no M3 (24)."),
        ("=", "En un proyecto de ejemplo, 3 laboratorios entregan 4 informes cada uno. ¿Cuántos informes hay que archivar?", "3*4", "Se multiplica el número de laboratorios por los informes de cada uno.", " informes"),
        ("abc", "Un residente dice: «el informe es del laboratorio, la obra no necesita archivarlo». ¿Qué respuesta es correcta?", "Debe archivarse en el registro de la obra como respaldo de la calidad", "No hace falta, porque el laboratorio lo guarda", "Solo se archiva si no cumple", "El informe respalda la calidad de la obra, cumpla o no, y se archiva con los demás registros."),
    ],
    ctx=("abc", "Un proveedor de ejemplo pide al jefe de obra que «no mencione» que una muestra no cumplió. ¿Qué corresponde?", "Informar el resultado al supervisor y dejarlo registrado", "Guardar silencio si el proveedor es conocido", "Pedirle al laboratorio que cambie el número", "Un resultado que no cumple se informa y se registra; esconderlo pone en riesgo la obra."),
    sc=[
        ("En Construcción: ¿qué es el valor especificado?", "El valor que fija la especificación técnica del proyecto", "Se compara con el valor obtenido para decidir si la muestra cumple."),
        ("¿Cuándo cumple una muestra?", "Cuando su valor obtenido es igual o mayor que el especificado, a la edad indicada", "La regla compara siempre a la edad que fija la especificación."),
        ("¿Se puede corregir un informe a mano?", "No: se pide al laboratorio una versión corregida y firmada", "Alterar un informe oculta problemas y es una falta."),
    ],
    op=("Informe de ejemplo: especificación de 20 u.e. a los 28 días. Muestra A, 28 días, 22 u.e.; muestra B, 28 días, 19 u.e.; muestra C, 7 días, 14 u.e. Escribe (a) qué muestras se comparan con la especificación, (b) cuáles cumplen, (c) qué haces con la que no cumple y a quién informas, (d) por qué no se evalúa C.",
        "(a) A y B, porque tienen 28 días. (b) Cumple A (22 es mayor que 20); B no cumple (19 es menor que 20). (c) Informo el resultado al supervisor técnico y lo dejo registrado; no altero el informe. (d) C tiene 7 días y la especificación compara a los 28 días.",
        ["elige las muestras de la edad correcta", "aplica la regla de cumple", "informa sin alterar el informe", "explica la edad de C"],
        ["hoja con las cuatro respuestas"],
        ["incluir a C en la comparación", "decir que B cumple por estar cerca", "esconder el resultado"],
        "Pregunta: «¿a qué edad se compara?». Si no responde, pídele que relea la edad que fija la especificación."),
    reinforce="Inventa un informe con tres muestras y su especificación; indica cuáles se comparan y cuáles cumplen.",
    extend="Explica por qué la trazabilidad protege a la obra cuando un resultado sale distinto de lo esperado.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (registro de recepción del laboratorio, de ejemplo, inventado). Laboratorio ficticio «Lab Sur», recepción del día 11 del mes de ejemplo. "
     "Fila 1: muestra S1, suelo, rótulo completo, tomada el día 10. Fila 2: muestra S2, suelo, rótulo completo, sin fecha de toma. Fila 3: muestra H1, hormigón, rótulo completo, tomada el día 10. "
     "Fila 4: muestra H2, hormigón, rótulo ilegible, tomada el día 10. Fila 5: muestra A1, agregado, rótulo completo, tomada el día 12. "
     "Criterio de ejemplo: una muestra está completa si trae rótulo legible y una fecha de toma posible; las demás quedan observadas y se informan antes de analizarlas.")
build(
    O7, 3, F,
    use="Analizaré en papel un registro de recepción de muestras, detectaré observaciones y decidiré a quién informar antes de analizar.",
    prior=["Sé qué es un rótulo y un informe de ensayo.", "Sé restar números pequeños.", "Sé que un dato dudoso se informa."],
    explain=[
        "Cuando las muestras llegan al laboratorio se llena un registro de recepción: una lista que anota cada muestra, el material, su rótulo, la fecha de toma y el estado en que llega. Con ese registro se revisa que cada muestra pueda identificarse. Una muestra con rótulo ilegible, sin fecha o con una fecha imposible (por ejemplo, tomada después del día en que se recibió) se llama observada. Una muestra observada no se analiza suponiendo datos: se informa a quien corresponde, que aclara el origen.",
        "Los materiales más comunes son el hormigón, los suelos y los agregados, que son las gravas y arenas que forman parte de una mezcla. Cada uno llega rotulado. El registro de recepción sirve para detectar errores a tiempo, antes de gastar trabajo en un análisis que luego no se podría usar. También se anota quién recibió y la firma, para saber quién respondió por cada muestra.",
        f"El traslado de muestras pesadas también es un riesgo, y se previene primero con medios que evitan el levantamiento manual. {EMER} {AVISO}",
    ],
    vocab=[("registro de recepción", "lista donde se anotan las muestras que llegan y su estado"), ("muestra observada", "muestra con un dato faltante, ilegible o imposible"), ("agregados", "gravas y arenas que forman parte de una mezcla"), ("fecha imposible", "fecha que contradice otros datos, como una toma posterior a la recepción"), ("firma de recepción", "anotación de quién recibió la muestra")],
    worked=[
        ("Detectar la observación", "Un registro de ejemplo trae la muestra X, tomada el día 8 y recibida el día 5. ¿Está completa?", ["La toma no puede ser posterior a la recepción.", "El día 8 viene después del día 5."], "No: tiene una fecha imposible y queda observada"),
        ("Contar completas", "De 6 muestras de ejemplo, 2 llegan sin rótulo legible. ¿Cuántas quedan completas?", ["Las observadas son 2.", "6 menos 2 dan 4."], "4 muestras"),
    ],
    mistakes=[("Analizar una muestra con rótulo ilegible «porque se parece a otra».", "No se sabe a qué parte de la obra pertenece, así que el resultado no sirve.", "Márcala como observada e informa."),
              ("Completar la fecha que falta con la de hoy.", "Se inventa un dato y se cambia la edad de la muestra.", "Pide a quien tomó la muestra que aclare la fecha.")],
    T=[
        ("abc", "En Construcción: ¿qué es un registro de recepción de muestras?", "La lista donde el laboratorio anota las muestras que recibe y en qué estado llegan", "El informe con los resultados del análisis", "El plano con la ubicación de cada muestra", "El registro de recepción anota lo que llega; el informe entrega los resultados."),
        ("abc", "¿Qué es una muestra observada en un registro de recepción?", "Una muestra con un dato faltante, ilegible o imposible", "Una muestra que ya fue analizada", "Una muestra que el proveedor envió gratis", "Observada significa que algún dato no permite identificarla con seguridad."),
        ("abc", "¿Qué se hace con una muestra observada antes de analizarla?", "Informar a quien corresponde para que aclare el dato", "Completar el dato con el más probable", "Analizarla igual y anotar el problema al final", "Analizar suponiendo datos produce resultados que no se pueden usar."),
        ("=", "{F} ¿Cuántas muestras completas hay en el registro?", "5-3", "Hay 5 muestras y 3 de ellas tienen observaciones.", " muestras"),
        ("abc", "{F} ¿Qué observación tiene la muestra S2?", "No trae fecha de toma", "Tiene el rótulo ilegible", "Fue tomada después de la recepción", "La ficha anota que S2 no tiene fecha de toma."),
        ("abc", "{F} ¿Qué problema tiene la muestra A1?", "Su fecha de toma (día 12) es posterior a la recepción (día 11), lo que es imposible", "Es un agregado y no se puede analizar", "Su rótulo está incompleto", "Una muestra no puede haberse tomado después de haber sido recibida."),
        ("ab", "{F} Un asistente dice: «H2 se analiza igual, todo el hormigón es parecido». ¿Qué respuesta es correcta?", "No: con rótulo ilegible no se sabe de qué parte viene; se informa y se aclara", "Sí: el hormigón es igual en toda la obra", "Un resultado solo sirve si se sabe a qué parte de la obra representa la muestra."),
        ("=", "{F} ¿Cuántos días pasaron entre la toma y la recepción de la muestra S1?", "11-10", "Se resta el día de toma al día de recepción.", " día"),
        ("abc", "{F} ¿Cuántas muestras quedan observadas según el criterio de la ficha?", "Tres: S2, H2 y A1", "Dos: S2 y A1", "Una: solo A1", "S2 no tiene fecha, H2 tiene rótulo ilegible y A1 tiene fecha imposible."),
        ("abc", "{F} Un jefe propone escribir para A1 la fecha de toma «10» para cerrar el registro. ¿Qué corresponde?", "No inventar el dato: preguntar a quien tomó la muestra y dejar registro de la aclaración", "Hacerlo, si el 10 es una fecha parecida", "Hacerlo si nadie nota el cambio", "Una fecha supuesta altera la edad de la muestra y falsea el registro."),
        ("=", "{F} Lab Sur cobra $8.000 (de ejemplo) por analizar cada muestra y solo analiza las completas. ¿Cuánto cobra?", "(5-3)*8000", "Se multiplica el valor por las dos muestras completas.", " pesos"),
        ("abc", "En la bodega de muestras hay cajas pesadas. Según la jerarquía de controles, ¿qué medida es la mejor para reducir el riesgo de levantarlas?", "Que la obra disponga un medio de transporte que evite el levantamiento manual", "Dar una faja a cada trabajador y pedir que levante con cuidado", "Pedir que levanten más rápido para pasar menos tiempo expuestos", "Primero se evita el riesgo en su origen; los EPP y la cautela van después."),
        ("abc", "{F} ¿Qué dato permite saber quién respondió por la recepción de cada muestra?", "La firma de recepción", "El color de la caja", "El nombre del material", "La firma deja constancia de quién recibió y respondió por la muestra."),
    ],
    ctx=("abc", "Un laboratorio de ejemplo recibe una muestra sin rótulo y el cliente dice: «es la de la losa, analícela de una vez». ¿Qué corresponde?", "Registrarla como observada y pedir por escrito la identificación antes de analizar", "Analizarla y asumir que es de la losa", "Rotularla con el nombre de la losa y seguir", "Sin identificación escrita no hay trazabilidad, aunque el cliente asegure su origen."),
    sc=[
        ("En Construcción: ¿qué son los agregados?", "Gravas y arenas que forman parte de una mezcla", "Son materiales de obra que también llegan al laboratorio con su rótulo."),
        ("¿Qué es una fecha imposible en el registro?", "Una fecha que contradice otros datos, como una toma posterior a la recepción", "Una muestra no puede tomarse después de haberse recibido."),
        ("¿Se completa un dato faltante con el más probable?", "No: se pide aclararlo a quien corresponde", "Inventar un dato falsea el registro de la obra."),
    ],
    op=("Registro de ejemplo del día 20: fila 1, muestra P1, suelo, rótulo completo, tomada el día 19; fila 2, muestra P2, hormigón, rótulo ilegible, tomada el día 19; fila 3, muestra P3, agregado, rótulo completo, tomada el día 21; fila 4, muestra P4, hormigón, rótulo completo, tomada el día 18. Escribe (a) cuántas muestras quedan observadas, (b) el problema de cada una, (c) a quién informas y qué no haces con sus datos.",
        "(a) Dos: P2 y P3. (b) P2 tiene el rótulo ilegible; P3 tiene fecha de toma (21) posterior a la recepción (20), imposible. (c) Informo al supervisor o a quien tomó las muestras para aclarar; no completo ni supongo datos.",
        ["detecta las dos observadas", "explica cada problema", "informa a quien corresponde", "no inventa datos"],
        ["hoja con las tres respuestas"],
        ["contar P1 o P4 como observadas", "suponer la fecha de P3", "analizar P2 igual"],
        "Pregunta: «¿qué dato no cuadra en P3?». Si no responde, pídele comparar la fecha de toma con la de recepción."),
    reinforce="Escribe tres errores que pueden tener una muestra en el registro de recepción y qué haces con cada uno.",
    extend="Explica por qué detectar una muestra observada al recibirla ahorra tiempo y evita decisiones erradas en la obra.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (criterio de aceptación de ejemplo, inventado). Regla de muestreo de ejemplo: 1 muestra por cada 10 m³ o fracción, contando cada entrega por separado. "
     "Entregas de hormigón de la obra «Galpón Quila» (ficticia): entrega 1, 24 m³; entrega 2, 36 m³. Resultados de ejemplo del lote a los 28 días (u.e.): 26, 28, 24, 30 y 27. "
     "Criterio de aceptación de ejemplo: el lote cumple si el promedio es igual o mayor que 25 u.e. y ninguna muestra queda bajo 22 u.e.")
build(
    O7, 4, F,
    use="Aplicaré criterios de ejemplo para calcular cuántas muestras se piden y decidir si un lote cumple, usando promedios y mínimos en una planilla.",
    prior=["Sé qué es un informe de ensayo.", "Sé sumar, dividir y comparar enteros.", "Sé qué es una muestra observada."],
    explain=[
        "Un lote es el conjunto de material que se evalúa junto. La frecuencia de muestreo es la regla que dice cuántas muestras se piden para cierta cantidad de material; por ejemplo, una por cada cierta cantidad «o fracción», lo que significa que una cantidad sobrante también cuenta como un tramo completo. El criterio de aceptación es la regla que decide si el lote cumple. Estos valores los fija la norma vigente y el proyecto; aquí se usan números de ejemplo.",
        "El promedio se calcula sumando todos los resultados y dividiendo por la cantidad de resultados. Algunos criterios piden dos condiciones a la vez: un promedio mínimo y, además, que ninguna muestra individual quede bajo un límite. Si falla una de las dos, el lote no cumple. La decisión sobre lo que se hace con un lote que no cumple la toma el supervisor técnico, con registro escrito; nadie la toma por cuenta propia.",
        f"Los cálculos se hacen en una planilla, con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("lote", "conjunto de material que se evalúa junto"), ("frecuencia de muestreo", "regla que dice cuántas muestras se piden para una cantidad de material"), ("o fracción", "una cantidad sobrante también cuenta como un tramo completo"), ("criterio de aceptación", "regla que decide si un lote cumple"), ("promedio", "suma de los resultados dividida por la cantidad de resultados"), ("límite individual", "valor bajo el cual ninguna muestra puede quedar")],
    worked=[
        ("Frecuencia con fracción", "Con la regla «1 muestra por cada 10 m³ o fracción», una entrega de ejemplo de 12 m³ tiene 10 m³ y sobran 2 m³. ¿Cuántas muestras se piden?", ["Los 10 m³ piden 1 muestra.", "Los 2 m³ sobrantes cuentan como otro tramo: 1 muestra más."], "2 muestras"),
        ("Promedio", "Tres resultados de ejemplo son 20, 22 y 24 u.e. ¿Cuál es el promedio?", ["Se suman: 20+22+24 = 66.", "Se divide por 3: 22."], "22 u.e."),
    ],
    mistakes=[("Dividir los m³ y redondear hacia abajo (60 m³ ÷ 10 = 6), sin contar cada entrega por separado.", "La regla pide una muestra por cada tramo «o fracción» de cada entrega.", "Calcula cada entrega por separado y suma."),
              ("Decidir que un lote cumple solo porque el promedio llega al mínimo.", "El criterio pide además que ninguna muestra quede bajo el límite individual.", "Revisa las dos condiciones.")],
    T=[
        ("abc", "En Construcción: ¿qué es un lote de hormigón?", "El conjunto de hormigón que se evalúa junto", "Un camión vacío que espera en la obra", "El rótulo que se pone a una muestra", "Un lote es el conjunto de material que se evalúa en conjunto."),
        ("abc", "¿Qué significa «cada 10 m³ o fracción» en una frecuencia de muestreo?", "Que un sobrante menor a 10 m³ también cuenta como un tramo completo", "Que los sobrantes se descartan sin muestrear", "Que se mide solo el tramo más grande", "La palabra «fracción» hace que el sobrante cuente como otro tramo."),
        ("abc", "¿Cómo se calcula el promedio de varios resultados?", "Se suman todos y se divide por la cantidad de resultados", "Se elige el resultado del medio", "Se resta el mayor al menor", "El promedio es la suma dividida por la cantidad de datos."),
        ("=", "{F} Según la regla de muestreo, ¿cuántas muestras se piden para la entrega 1?", "(24+9)//10", "24 m³ tienen 2 tramos de 10 y un sobrante de 4, que cuenta como otro tramo.", " muestras"),
        ("=", "{F} ¿Cuántas muestras se piden para la entrega 2?", "(36+9)//10", "36 m³ tienen 3 tramos de 10 y un sobrante de 6, que cuenta como otro tramo.", " muestras"),
        ("=", "{F} ¿Cuánto suman los cinco resultados de la ficha?", "26+28+24+30+27", "Se suman los cinco valores del lote.", " u.e."),
        ("=", "{F} ¿Cuál es el promedio de los cinco resultados?", "(26+28+24+30+27)//5", "La suma de los cinco resultados se divide por cinco.", " u.e."),
        ("abc", "{F} Según el criterio de la ficha, ¿cumple el lote?", "Sí: el promedio es mayor que 25 y ninguna muestra queda bajo 22", "No: la muestra de 24 está bajo 25", "No: el promedio de 27 es demasiado alto", "El promedio es 27 y el menor valor es 24; ambas condiciones se cumplen."),
        ("ab", "{F} Si la muestra de 24 u.e. fuera 19 u.e. (promedio 26), ¿qué pasa? ", "El lote no cumple, porque una muestra queda bajo 22 u.e. aunque el promedio sea suficiente", "El lote cumple, porque el promedio de 26 supera 25", "El criterio exige las dos condiciones a la vez; basta con que falle una para que no cumpla."),
        ("abc", "{F} Un compañero dice que para los 60 m³ en total bastan 6 muestras (60 ÷ 10). ¿Qué respuesta es correcta?", "Se piden 7: 3 para la entrega 1 y 4 para la entrega 2, porque cada entrega y su fracción se cuentan aparte", "Se piden 6, porque la división es exacta", "Se piden 5, porque basta una por entrega y una más", "La regla cuenta cada entrega por separado y cada sobrante como un tramo."),
        ("=", "{F} Cada muestra cuesta $8.000 (de ejemplo). ¿Cuánto cuestan las muestras de las dos entregas?", "((24+9)//10+(36+9)//10)*8000", "Se suman las muestras de las dos entregas y se multiplican por el valor de una.", " pesos"),
        ("abc", "{F} Si el lote no cumpliera, ¿quién decide qué se hace, según lo aprendido?", "El supervisor técnico, con registro escrito", "El operador de la mezcladora", "Cualquier trabajador que lo detecte", "La decisión la toma quien supervisa y la deja registrada."),
        ("abc", "{F} Un jefe sugiere tomar solo 4 muestras en total «para ahorrar». ¿Qué corresponde?", "No: la cantidad la fija la especificación y se debe cumplir", "Sí, si el promedio sale bien", "Sí, si el proveedor lo acepta", "La frecuencia de muestreo es parte de la especificación y no se reduce por ahorro."),
    ],
    ctx=("abc", "Una supervisora de ejemplo ve que el promedio de un lote cumple, pero una muestra queda bajo el límite individual. ¿Qué debe hacer?", "Declarar que el lote no cumple, registrarlo y dejar la decisión a quien corresponde", "Declarar que cumple, porque el promedio es bueno", "Quitar la muestra baja de la planilla", "El criterio exige ambas condiciones; quitar datos falsea el resultado."),
    sc=[
        ("En Construcción: ¿qué es el criterio de aceptación?", "La regla que decide si un lote cumple", "Sirve para decidir con las mismas condiciones en todos los lotes."),
        ("¿Qué significa «o fracción»?", "Que el sobrante también cuenta como un tramo completo", "Así ningún sobrante queda sin muestrear."),
        ("¿Basta el promedio para aceptar un lote?", "No: también se revisa el límite individual", "Los criterios de ejemplo piden dos condiciones a la vez."),
    ],
    op=("Obra de ejemplo «Muro Alba»: regla de 1 muestra por cada 8 m³ o fracción; entrega única de 20 m³; resultados del lote (u.e.): 21, 23, 25. Criterio de ejemplo: promedio mínimo de 22 y ninguna muestra bajo 20. Escribe (a) cuántas muestras se piden, (b) el promedio, (c) si el lote cumple y por qué, (d) quién decide si no cumpliera.",
        "(a) 20 tiene 2 tramos de 8 y un sobrante de 4: 3 muestras. (b) 21+23+25 son 69; 69 dividido por 3 es 23. (c) Cumple: 23 es mayor que 22 y ninguna queda bajo 20. (d) El supervisor técnico, con registro escrito.",
        ["cuenta la fracción", "calcula el promedio", "aplica las dos condiciones", "nombra quién decide"],
        ["hoja con las cuatro respuestas"],
        ["dividir 20 entre 8 y redondear hacia abajo", "revisar solo el promedio", "decidir por cuenta propia"],
        "Pregunta: «¿qué pasa con el sobrante de 4 m³?». Si no responde, pídele que relea qué significa «o fracción»."),
    reinforce="Inventa una entrega de hormigón de 35 m³ y calcula cuántas muestras se piden con la regla de 1 por cada 10 m³ o fracción.",
    extend="Explica por qué un criterio con promedio y límite individual protege más que uno con solo promedio.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Obra «Casa Alerce» (ficticia). Planilla de stock del día: cemento en sacos: inicio 120, ingresaron 80, salieron 150; clavos en cajas: inicio 30, ingresaron 0, salieron 12. "
     "Horas de equipos (de ejemplo): equipo E1, 6 horas trabajadas; equipo E2, 4 horas trabajadas; la jornada de ejemplo tiene 8 horas. "
     "El formato de la obra pide anotar en cada línea: fecha, material o equipo, cantidad, responsable y firma.")
build(
    O8, 1, F,
    use="Aprenderé para qué se llevan registros de materiales, stock y horas de equipos, y qué riesgos tiene registrar mal o no registrar.",
    prior=["Sé sumar y restar números enteros.", "Sé leer una planilla simple.", "Sé que lo que se anota debe ser verdad."],
    explain=[
        "El control de gestión de una obra consiste en saber cuánto se gasta, cuánto se usa y cuánto queda. Para eso se llevan registros: anotaciones escritas en un formato fijado por la obra. El stock es la cantidad de un material que hay disponible en la bodega. Los ingresos son lo que entra, las salidas son lo que se retira y el saldo es lo que queda. Las horas de equipos son el tiempo que trabajó cada máquina o equipo en la jornada. Cada línea del registro lleva fecha, responsable y firma.",
        "Un buen registro permite detectar pérdidas, pedir materiales a tiempo y cobrar o pagar lo correcto. Un registro falso o incompleto causa compras equivocadas, atrasos y hasta riesgos de seguridad, por ejemplo, si se cree que hay un equipo revisado y no es así. Por eso se registra en el momento, con letra clara y sin borrar: un error se tacha con una línea, se corrige al lado y se firma.",
        f"Esto se aprende aquí en planillas de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("registro", "anotación escrita en un formato fijado por la obra"), ("stock", "cantidad de un material disponible en la bodega"), ("ingreso", "cantidad de material que entra a la bodega"), ("salida", "cantidad de material que se retira de la bodega"), ("saldo", "cantidad que queda después de ingresos y salidas"), ("horas de equipo", "tiempo que trabajó un equipo en la jornada"), ("control de gestión", "seguimiento de lo que se gasta, se usa y queda en la obra")],
    worked=[
        ("Calcular un saldo", "En la bodega de ejemplo hay 50 sacos de yeso, ingresan 20 y salen 30. ¿Cuál es el saldo?", ["Al inicio se suma lo que ingresa: 50+20 = 70.", "Se resta lo que sale: 70-30 = 40."], "40 sacos"),
        ("Corregir un error", "Una persona anota 25 donde debía anotar 52. ¿Cómo corrige el registro?", ["No se borra ni se usa corrector.", "Se tacha con una línea, se escribe 52 al lado y se firma."], "Tacha con una línea, anota el dato correcto y firma"),
    ],
    mistakes=[("Borrar un dato equivocado con corrector para que se vea limpio.", "Un registro con borrones pierde confianza y puede ocultar fraudes.", "Tacha con una línea, anota el dato correcto y firma."),
              ("Anotar al final de la semana lo que pasó cada día.", "Se olvidan cantidades y el registro deja de reflejar la realidad.", "Registra en el momento, cada día.")],
    T=[
        ("abc", "En Construcción: ¿qué es el stock de un material?", "La cantidad de ese material que hay disponible en la bodega", "La cantidad que se compró en toda la obra", "El precio del material por unidad", "El stock es lo que hay disponible; la compra y el precio son otros datos."),
        ("abc", "En una planilla de bodega, ¿qué es el saldo?", "La cantidad que queda después de sumar ingresos y restar salidas", "La cantidad que entró en el día", "La cantidad que se perdió", "El saldo resulta de aplicar ingresos y salidas al inicio."),
        ("abc", "¿Por qué se registra en el momento y con firma?", "Para que el registro refleje lo que realmente ocurrió y se sepa quién respondió", "Para que la planilla se vea más larga", "Para evitar que otras personas lean el registro", "Registrar en el momento y firmar da confianza y deja responsable."),
        ("=", "{F} ¿Cuál es el saldo de cemento en sacos al terminar el día?", "120+80-150", "Al inicio se suma lo que ingresó y se resta lo que salió.", " sacos"),
        ("=", "{F} ¿Cuántas cajas de clavos quedan en la bodega?", "30+0-12", "Al inicio se suma el ingreso (0) y se resta lo que salió.", " cajas"),
        ("=", "{F} ¿Cuántas horas trabajaron entre los dos equipos?", "6+4", "Se suman las horas trabajadas por E1 y E2.", " horas"),
        ("abc", "{F} ¿Qué datos pide el formato de la obra en cada línea?", "Fecha, material o equipo, cantidad, responsable y firma", "Solo la cantidad y el precio", "Fecha y el nombre del proveedor", "El formato de la ficha pide esos cinco datos."),
        ("abc", "{F} Una persona anotó 150 salidas de cemento como 105. ¿Cómo corrige?", "Tacha con una línea, anota 150 al lado y firma", "Borra el 105 con corrector y escribe 150", "Rompe la hoja y reescribe todo sin avisar", "Un error se tacha y se corrige al lado con firma, sin ocultarlo."),
        ("ab", "{F} Un bodeguero dice: «anoto las salidas el viernes, de memoria». ¿Qué respuesta es correcta?", "No: el registro debe hacerse en el momento para que sea fiel", "Sí: da lo mismo cuándo se anote", "Anotar de memoria al final de la semana puede perder cantidades y no refleja la realidad."),
        ("abc", "{F} El equipo E1 aparece con 6 horas, pero un capataz asegura que trabajó 8. ¿Qué corresponde?", "Aclarar con el responsable y corregir el registro dejando constancia", "Dejar 6 y no revisar", "Cambiar a 8 sin preguntar", "Un dato en duda se aclara con quien lo anotó y se corrige dejando constancia."),
        ("=", "{F} ¿Cuántas horas de la jornada de 8 horas no trabajó E2?", "8-4", "Se restan las horas trabajadas a las horas de la jornada.", " horas"),
        ("abc", "Un acopio de material mal ordenado se cae sobre un trabajador de la bodega y lo atrapa. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Mover rápidamente el material sin pedir ayuda", "Esperar a que el trabajador salga por su cuenta", "Acercarse sin ayuda puede causar otro accidente; se avisa a quien corresponde."),
        ("abc", "{F} Si los clavos hubieran salido 40 cajas con un inicio de 30 y sin ingresos, ¿qué muestra la planilla?", "Un error: no pueden salir más cajas de las que había", "Un saldo de 10 cajas", "Un saldo de -10 cajas que es normal", "No se puede retirar más de lo disponible, así que el dato debe revisarse."),
    ],
    ctx=("abc", "Un bodeguero de ejemplo nota que faltan sacos de cemento respecto al registro. ¿Qué hace?", "Registrar la diferencia, informar al jefe de obra y no ajustar la planilla por su cuenta", "Cambiar el registro para que cuadre", "No decir nada para evitar problemas", "Las diferencias se informan y se registran; ajustar sin avisar oculta una pérdida."),
    sc=[
        ("En Construcción: ¿qué es un ingreso en la bodega?", "La cantidad de material que entra a la bodega", "El ingreso se suma al inicio para obtener el saldo."),
        ("¿Cómo se corrige un dato mal anotado?", "Con una línea, el dato correcto al lado y firma", "Así queda a la vista qué se corrigió y quién lo hizo."),
        ("¿Para qué sirve un registro de horas de equipos?", "Para saber cuánto trabajó cada equipo", "Ayuda a controlar el uso y el costo de los equipos."),
    ],
    op=("Bodega de ejemplo «Taller Lenga»: yeso en sacos, inicio 90, ingresaron 40, salieron 70; el equipo E3 trabajó 5 horas de una jornada de 8. Escribe (a) el saldo de yeso, (b) las horas que E3 no trabajó, (c) cómo corriges si anotaste 70 y eran 60 las salidas, (d) por qué se firma cada línea.",
        "(a) 90+40-70 son 60 sacos. (b) 8-5 son 3 horas. (c) Tacho el 70 con una línea, escribo 60 al lado y firmo. (d) Para dejar constancia de quién registró y responde por el dato.",
        ["calcula el saldo", "calcula las horas", "corrige sin borrar", "explica la firma"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar el ingreso", "borrar con corrector", "no mencionar al responsable"],
        "Pregunta: «¿cómo se corrige sin ocultar el error?». Si no responde, pídele que relea la regla de tachar con una línea."),
    reinforce="Inventa una planilla de bodega con inicio, ingresos y salidas de un material y calcula el saldo.",
    extend="Explica con un ejemplo inventado cómo un registro fiel evita una compra de más.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (documentos de obra, de ejemplo, inventados). Obra «Posta Ñire» (ficticia). Orden de compra OC-12: 100 sacos de yeso. Guía de despacho GD-45 del proveedor de ejemplo: llegaron 90 sacos. "
     "Vale de salida de bodega VS-7: se retiran 40 sacos para la partida «cielos». Libro de obra: anotaciones diarias firmadas por el jefe de obra. "
     "Roles: el bodeguero recibe y entrega; el administrativo de obra archiva y cuadra; el jefe de obra autoriza compras y salidas.")
build(
    O8, 2, F,
    use="Aprenderé qué documentos respaldan los registros de una obra (orden de compra, guía, vale de salida y libro de obra) y qué rol cumple cada persona.",
    prior=["Sé qué es un registro y un saldo.", "Sé sumar y restar enteros.", "Sé que cada anotación lleva firma."],
    explain=[
        "Los registros de una obra se apoyan en documentos. La orden de compra es el documento con que la obra pide un material a un proveedor: dice qué y cuánto. La guía de despacho acompaña lo que el proveedor entrega y dice qué y cuánto llegó realmente. El vale de salida de bodega deja constancia de lo que se retira y para qué partida, que es una parte del trabajo con su propio presupuesto. El libro de obra es el cuaderno donde se anotan los hechos diarios de la obra, con fecha y firma.",
        "Conciliar significa comparar documentos para ver si coinciden: por ejemplo, la orden de compra con la guía de despacho. La diferencia entre lo pedido y lo recibido es lo pendiente de entrega. Cada rol tiene su tarea: el bodeguero recibe y entrega, el administrativo de obra archiva y cuadra los documentos y el jefe de obra autoriza compras y salidas. Ningún documento reemplaza a otro, y cuando no coinciden se informa; no se corrige en silencio.",
        f"Los documentos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("orden de compra", "documento con que la obra pide un material a un proveedor"), ("guía de despacho", "documento que acompaña lo que el proveedor entrega"), ("vale de salida", "documento que deja constancia de lo que se retira de la bodega"), ("libro de obra", "cuaderno de hechos diarios de la obra, con fecha y firma"), ("partida", "parte del trabajo de una obra con su propia cantidad y presupuesto"), ("conciliar", "comparar documentos para ver si coinciden"), ("pendiente de entrega", "diferencia entre lo pedido y lo recibido")],
    worked=[
        ("Calcular lo pendiente", "Una orden de ejemplo pide 60 planchas y la guía indica que llegaron 45. ¿Cuántas están pendientes?", ["Se compara lo pedido con lo recibido.", "60 menos 45 son 15."], "15 planchas"),
        ("Elegir el documento", "Una administrativa de ejemplo debe probar qué llegó realmente de un proveedor. ¿Qué documento usa?", ["Lo que llegó lo dice quien despacha.", "Ese documento es la guía de despacho."], "La guía de despacho"),
    ],
    mistakes=[("Archivar solo la orden de compra y botar la guía porque «ya se pidió».", "La guía prueba qué se recibió realmente.", "Archiva todos los documentos y concílialos."),
              ("Retirar material de la bodega sin dejar vale de salida porque «era urgente».", "Sin vale no se sabe a qué partida cargar el material.", "Registra el vale y deja la constancia de la urgencia.")],
    T=[
        ("abc", "En Construcción: ¿qué es una orden de compra?", "El documento con que la obra pide a un proveedor un material y su cantidad", "El documento que acompaña lo que ya se entregó", "El cuaderno de hechos diarios de la obra", "La orden de compra solicita; la guía acompaña la entrega y el libro anota hechos diarios."),
        ("abc", "En documentos de obra: ¿qué es una partida?", "Una parte del trabajo de la obra con su propia cantidad y presupuesto", "Una persona que parte la jornada", "El camión que parte del proveedor", "Una partida es una parte medible y presupuestada del trabajo."),
        ("abc", "¿Qué significa conciliar dos documentos?", "Compararlos para ver si coinciden", "Archivarlos juntos sin leerlos", "Firmarlos aunque no coincidan", "Conciliar es comparar para detectar diferencias."),
        ("=", "{F} ¿Cuántos sacos están pendientes de entrega?", "100-90", "Se resta lo recibido a lo pedido.", " sacos"),
        ("abc", "{F} ¿Qué documento prueba que llegaron 90 sacos?", "La guía de despacho GD-45", "La orden de compra OC-12", "El vale de salida VS-7", "La guía dice qué llegó realmente; la orden dice qué se pidió."),
        ("abc", "{F} ¿Para qué partida se retiran los 40 sacos del vale VS-7?", "Para la partida «cielos»", "Para la partida «fundaciones»", "No lo dice el vale", "El vale de la ficha indica que son para cielos."),
        ("=", "{F} Con 90 sacos recibidos y 40 retirados con el vale, ¿cuántos sacos quedan?", "90-40", "Se restan los sacos retirados a los recibidos.", " sacos"),
        ("ab", "{F} Un auxiliar dice: «como la orden pide 100, anoto 100 sacos recibidos». ¿Qué respuesta es correcta?", "No: se anota lo que dice la guía, 90, y se informa lo pendiente", "Sí: la orden manda sobre la guía", "El registro de recepción refleja lo realmente entregado, no lo pedido."),
        ("abc", "{F} ¿Quién autoriza las salidas de la bodega según la ficha?", "El jefe de obra", "El proveedor", "El administrativo de obra por sí solo", "En la ficha, el jefe de obra autoriza compras y salidas."),
        ("abc", "{F} El bodeguero entrega sacos a un compañero sin vale «porque es urgente». ¿Qué corresponde?", "Registrar el vale de salida de inmediato y dejar la constancia de la urgencia", "No registrar nada, porque ya se entregó", "Registrar el vale una semana después, de memoria", "Sin vale no se sabe a qué partida cargar el material; se registra al tiro."),
        ("=", "{F} Si el proveedor completa la entrega pendiente y se pide una nueva orden por 25 sacos más, ¿cuántos sacos habrá recibido en total la obra sumando los 90 de la guía, los pendientes y los 25 nuevos?", "90+(100-90)+25", "Se suman lo recibido, lo pendiente que llega y la nueva orden.", " sacos"),
        ("abc", "Se derrumba un acopio de planchas en la bodega y una persona queda atrapada. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Retirar las planchas a mano entre varios sin avisar", "Tirar a la persona de los brazos", "Acercarse sin ayuda puede causar otro accidente; se avisa a quien corresponde."),
        ("abc", "{F} Si la guía GD-45 trajera 100 sacos pero llegaran solo 90 al contar, ¿qué corresponde?", "Dejar constancia de la diferencia en la recepción e informar al jefe de obra", "Aceptar los 100 de la guía sin contar", "Anotar 90 y no avisar al proveedor", "Lo recibido se cuenta y las diferencias se informan, no se aceptan en silencio."),
    ],
    ctx=("abc", "Un proveedor de ejemplo entrega menos de lo pedido y propone «arreglarlo» en la guía para que cuadre con la orden. ¿Qué corresponde?", "Rechazar el arreglo, registrar lo realmente recibido e informar al jefe de obra", "Aceptar, para no pelear con el proveedor", "Corregir la orden de compra para que cuadre", "Un documento no se modifica para ocultar una diferencia real."),
    sc=[
        ("En Construcción: ¿qué es el libro de obra?", "El cuaderno de hechos diarios de la obra, con fecha y firma", "Allí se deja constancia de lo que ocurre día a día."),
        ("¿Qué documento prueba lo que realmente llegó?", "La guía de despacho", "La orden de compra solo dice lo que se pidió."),
        ("¿Quién cuadra y archiva los documentos?", "El administrativo de obra", "Cada rol tiene una función en el control de la obra."),
    ],
    op=("Obra de ejemplo «Escuela Maitén»: la orden OC-3 pide 80 planchas; la guía GD-9 indica 70 recibidas; el vale VS-2 retira 30 planchas para la partida «tabiques». Escribe (a) cuántas planchas están pendientes, (b) cuántas quedan en bodega, (c) qué documento prueba lo recibido, (d) qué haces si el proveedor pide que anotes 80.",
        "(a) 80-70 son 10 planchas pendientes. (b) 70-30 son 40 planchas. (c) La guía de despacho GD-9. (d) No lo anoto: registro lo realmente recibido (70), informo al jefe de obra y dejo constancia del pendiente.",
        ["calcula lo pendiente", "calcula el saldo", "nombra el documento correcto", "no altera el registro"],
        ["hoja con las cuatro respuestas"],
        ["usar la orden como recibido", "restar mal", "aceptar anotar 80"],
        "Pregunta: «¿qué documento dice lo realmente recibido?». Si no responde, pídele que relea qué es la guía de despacho."),
    reinforce="Escribe los cuatro documentos de esta clase y, junto a cada uno, la pregunta que responde.",
    extend="Explica con un ejemplo inventado qué problema aparece si la obra no concilia la orden con la guía.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (planilla semanal de bodega, de ejemplo, inventada). Obra «Liceo Lingue» (ficticia), material: sacos de cemento de ejemplo. "
     "Lunes: inicio 100, ingreso 0, salida 20, saldo anotado 80. Martes: ingreso 0, salida 30, saldo anotado 50. Miércoles: ingreso 60 con guía GD-50, salida 25, saldo anotado 85. "
     "Jueves: ingreso 40 sin guía anotada, salida 35, saldo anotado 90. Viernes: ingreso 0, salida 50, saldo anotado 30. "
     "Regla de ejemplo: cada día, saldo = saldo del día anterior + ingreso - salida; un ingreso sin guía queda observado.")
build(
    O8, 3, F,
    use="Analizaré en papel una planilla semanal de bodega para detectar un saldo mal calculado y un ingreso sin respaldo.",
    prior=["Sé qué es un saldo.", "Sé qué es una guía de despacho.", "Sé sumar y restar enteros."],
    explain=[
        "Una planilla semanal registra, día a día, el inicio, los ingresos, las salidas y el saldo de un material. La regla es sencilla: el saldo de un día es el saldo del día anterior más el ingreso, menos la salida. Para revisar una planilla se recalcula cada saldo y se compara con el anotado. Si no coinciden hay un error de cálculo o de anotación. Además, cada ingreso debe tener su guía de despacho; un ingreso sin guía queda observado.",
        "La revisión se hace con calma y en orden, empezando por el primer día. Si se encuentra un error, no se cambia en silencio: se deja constancia de qué se encontró, qué debería decir y quién lo detectó, y se informa al responsable. Corregir el saldo de un día obliga a recalcular los días siguientes, porque cada saldo parte del anterior.",
        f"Los datos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("planilla semanal", "tabla que registra día a día inicio, ingresos, salidas y saldo"), ("saldo anotado", "saldo que aparece escrito en la planilla"), ("saldo recalculado", "saldo que resulta de aplicar la regla"), ("ingreso observado", "ingreso que no tiene guía de despacho anotada"), ("constancia", "anotación escrita de lo detectado")],
    worked=[
        ("Recalcular", "Un saldo anterior de ejemplo es 70, ingresan 10 y salen 25. ¿Cuál es el saldo?", ["Se suma el ingreso: 70+10 = 80.", "Se resta la salida: 80-25 = 55."], "55 sacos"),
        ("Detectar un error", "Un día de ejemplo tiene saldo anterior 60, ingreso 0, salida 15 y saldo anotado 35. ¿Está bien?", ["Se recalcula: 60+0-15 = 45.", "El anotado es 35, distinto de 45."], "No: debería ser 45"),
    ],
    mistakes=[("Revisar solo el último saldo de la semana.", "Un error anterior se arrastra y el último saldo puede estar mal por eso.", "Recalcula día por día desde el inicio."),
              ("Aceptar un ingreso sin guía porque «seguro llegó».", "Sin guía no hay respaldo de lo recibido.", "Marca el ingreso como observado e informa.")],
    T=[
        ("abc", "En Construcción: ¿cómo se calcula el saldo de un día en una planilla de bodega?", "Saldo del día anterior más ingreso, menos salida", "Ingreso menos saldo del día anterior", "Salida más ingreso, sin considerar el día anterior", "El saldo parte del día anterior y se le suma lo que ingresa y se le resta lo que sale."),
        ("abc", "¿Qué es un ingreso observado?", "Un ingreso que no tiene su guía de despacho anotada", "Un ingreso muy grande", "Un ingreso que ocurre un viernes", "Observado significa que le falta el respaldo documental."),
        ("abc", "Si se corrige el saldo de un día, ¿qué pasa con los días siguientes?", "Hay que recalcularlos, porque cada saldo parte del anterior", "No cambian nunca", "Se borran de la planilla", "Cada saldo depende del anterior, así que el cambio se arrastra."),
        ("=", "{F} ¿Cuál es el saldo recalculado del lunes?", "100+0-20", "Se suma el ingreso al inicio y se resta la salida.", " sacos"),
        ("=", "{F} ¿Cuál es el saldo recalculado del miércoles, partiendo del saldo del martes de la ficha?", "50+60-25", "Al saldo del martes se suma el ingreso y se resta la salida.", " sacos"),
        ("abc", "{F} ¿Qué ingreso queda observado en la planilla?", "El del jueves, porque no tiene guía anotada", "El del miércoles, porque es el más grande", "Ninguno, porque todos los saldos cuadran", "La ficha dice que el ingreso del jueves no trae guía."),
        ("=", "{F} ¿Cuántos sacos salieron en total entre lunes y viernes?", "20+30+25+35+50", "Se suman las salidas de los cinco días.", " sacos"),
        ("abc", "{F} ¿Qué pasa con el saldo anotado del viernes (30)?", "Es erróneo: según la regla, el saldo del jueves menos la salida da 40", "Es correcto, porque cuadra con la salida", "Es correcto si se resta primero el ingreso", "90 menos 50 es 40; el 30 anotado no coincide."),
        ("=", "{F} ¿Cuál es el saldo correcto del viernes?", "90+0-50", "Al saldo del jueves se suma el ingreso (0) y se resta la salida.", " sacos"),
        ("ab", "{F} Un supervisor dice: «el viernes tenía 30 anotado, lo dejamos para no complicarnos». ¿Qué respuesta es correcta?", "No: se deja constancia del error y se informa para corregirlo con firma", "Sí: un error de 10 sacos no importa", "Un saldo mal anotado puede ocultar una pérdida o llevar a una compra equivocada."),
        ("abc", "{F} Se verificó que el saldo del jueves era realmente 80 en vez de 90. ¿Qué otro saldo cambia?", "El del viernes, que parte del jueves", "El del lunes", "Ninguno más", "Solo los días posteriores dependen del saldo del jueves."),
        ("abc", "{F} Un auxiliar quiere agregar la guía del jueves de memoria. ¿Qué corresponde?", "Pedir al proveedor o buscar la guía real; no escribir una guía de memoria", "Escribir un número parecido al de la guía del miércoles", "Dejar el espacio en blanco y no avisar", "Una guía inventada falsea el respaldo del ingreso."),
        ("=", "{F} ¿Cuántos sacos de diferencia hay entre el saldo correcto del viernes y el saldo anotado de 30?", "(90+0-50)-30", "Se resta el saldo anotado al saldo correcto.", " sacos"),
    ],
    ctx=("abc", "Una bodeguera de ejemplo descubre que se equivocó en un saldo hace dos días. ¿Qué hace?", "Dejar constancia, corregir con firma y recalcular los saldos siguientes", "Borrar el error sin avisar", "Esperar al final del mes", "Un error se corrige a la vista y se recalcula lo que depende de él."),
    sc=[
        ("En Construcción: ¿qué es un saldo recalculado?", "El que resulta de aplicar la regla al saldo anterior, el ingreso y la salida", "Se compara con el anotado para detectar errores."),
        ("¿Qué se hace con un ingreso sin guía?", "Se marca como observado e informa", "Sin guía el ingreso no tiene respaldo."),
        ("¿Por qué se revisa día por día?", "Porque cada saldo parte del anterior y los errores se arrastran", "Revisar solo el final puede esconder el origen del error."),
    ],
    op=("Planilla de ejemplo: lunes, inicio 40, ingreso 0, salida 10, saldo anotado 30; martes, ingreso 20 con guía GD-1, salida 15, saldo anotado 35; miércoles, ingreso 10 sin guía, salida 5, saldo anotado 45. Escribe (a) el saldo correcto de cada día, (b) qué día tiene un error, (c) qué ingreso queda observado, (d) qué haces con lo encontrado.",
        "(a) Lunes 30; martes 30+20-15 = 35; miércoles 35+10-5 = 40. (b) El miércoles, anotado 45 y debería ser 40. (c) El ingreso del miércoles, sin guía. (d) Dejo constancia, informo al responsable y corrijo con firma recalculando lo que dependa.",
        ["recalcula cada día", "ubica el error", "identifica el ingreso observado", "deja constancia e informa"],
        ["hoja con las cuatro respuestas"],
        ["revisar solo el último día", "aceptar el ingreso sin guía", "corregir en silencio"],
        "Pregunta: «¿qué saldo anterior usas el miércoles?». Si no responde, pídele que relea la regla del saldo."),
    reinforce="Inventa una planilla de tres días para un material y marca un error de saldo para que otro lo encuentre.",
    extend="Explica por qué exigir la guía en cada ingreso protege a la obra de pagos por material que no llegó.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (criterios de gestión de ejemplo, inventados). Obra «Sede Copihue» (ficticia). Consumo diario promedio de cemento: 25 sacos de ejemplo. Plazo de entrega del proveedor de ejemplo: 3 días. "
     "Regla de reposición de ejemplo: se hace un pedido cuando el saldo baja al consumo de los días del plazo más 1 día de margen. Saldo actual: 140 sacos. "
     "Equipo E4 (de ejemplo): costo de $12.000 por hora; presupuesto de la semana: 40 horas; horas trabajadas en la semana: 38.")
build(
    O8, 4, F,
    use="Aplicaré criterios de ejemplo para decidir cuándo reponer un material y para comparar el costo de un equipo con su presupuesto.",
    prior=["Sé qué es una planilla de bodega.", "Sé multiplicar y restar enteros.", "Sé qué son las horas de equipo."],
    explain=[
        "El control de gestión también sirve para anticiparse. El consumo promedio es la cantidad que se usa en un día, en promedio. El plazo de entrega es el tiempo que demora el proveedor en entregar después de un pedido. El punto de reposición es el saldo al que se hace el pedido: debe alcanzar para cubrir los días del plazo más un margen, de modo que el material no se acabe antes de que llegue el nuevo. Aquí se calcula como consumo diario por los días del plazo más el margen.",
        "En los equipos se compara el costo real con el presupuesto. El costo real se obtiene multiplicando las horas trabajadas por el costo por hora. La desviación es la diferencia entre lo presupuestado y lo real: si el costo real es menor, hay ahorro; si es mayor, hay sobrecosto. Los valores son de ejemplo; los reales los fijan el proyecto y los contratos.",
        f"Todo se calcula en planilla. {EMER} {AVISO}",
    ],
    vocab=[("consumo promedio", "cantidad que se usa en un día, en promedio"), ("plazo de entrega", "tiempo que demora el proveedor en entregar después del pedido"), ("punto de reposición", "saldo al que se hace un nuevo pedido"), ("margen", "días extra de reserva que se agregan por seguridad"), ("costo real", "horas trabajadas por costo por hora"), ("desviación", "diferencia entre el presupuesto y el costo real")],
    worked=[
        ("Punto de reposición", "Una obra de ejemplo usa 10 planchas por día, el proveedor tarda 2 días y se deja 1 día de margen. ¿Cuál es el punto de reposición?", ["Los días son 2+1 = 3.", "10 por 3 son 30 planchas."], "30 planchas"),
        ("Desviación", "Un equipo de ejemplo tiene presupuesto de $200.000 y costo real de $180.000. ¿Hay ahorro o sobrecosto?", ["200.000-180.000 = 20.000.", "El real es menor que el presupuestado."], "Ahorro de $20.000"),
    ],
    mistakes=[("Pedir el material cuando ya no queda nada, porque «todavía hay».", "El proveedor demora días y el material se acaba antes de que llegue.", "Pide al llegar al punto de reposición."),
              ("Comparar el costo con el presupuesto sin multiplicar por las horas.", "El costo real depende de las horas trabajadas.", "Multiplica horas por costo por hora y luego compara.")],
    T=[
        ("abc", "En Construcción: ¿qué es el punto de reposición de un material?", "El saldo al que se hace un nuevo pedido", "El saldo con el que se cierra la obra", "El precio máximo que se paga", "El punto de reposición indica cuándo pedir para no quedarse sin material."),
        ("abc", "¿Qué es el plazo de entrega?", "El tiempo que demora el proveedor en entregar después del pedido", "El tiempo que dura la obra", "El plazo para pagar la factura", "El plazo de entrega es la demora del proveedor para entregar."),
        ("abc", "¿Qué significa que haya sobrecosto en un equipo?", "Que el costo real es mayor que el presupuestado", "Que el equipo trabajó menos horas", "Que el costo por hora bajó", "Sobrecosto es gastar más de lo presupuestado."),
        ("=", "{F} ¿Cuántos días se consideran en el cálculo (plazo más margen)?", "3+1", "Se suman los días del plazo y el día de margen.", " días"),
        ("=", "{F} ¿Cuál es el punto de reposición del cemento en sacos?", "25*(3+1)", "Se multiplica el consumo diario por los días del plazo más el margen.", " sacos"),
        ("abc", "{F} Con un saldo actual de 140 sacos, ¿hay que pedir ya?", "No: 140 es mayor que el punto de reposición de 100", "Sí: siempre se pide cuando hay menos de 200", "Sí: 140 es menos que lo que se usa en una semana", "Todavía hay más material que el punto de reposición."),
        ("=", "{F} ¿Cuál es el costo real del equipo E4 en la semana?", "38*12000", "Se multiplican las horas trabajadas por el costo por hora.", " pesos"),
        ("=", "{F} ¿Cuál es el presupuesto del equipo E4 en pesos?", "40*12000", "Se multiplican las horas presupuestadas por el costo por hora.", " pesos"),
        ("abc", "{F} Comparando el costo real con el presupuesto, ¿qué ocurre con E4?", "Hay un ahorro de $24.000", "Hay un sobrecosto de $24.000", "Hay un ahorro de $456.000", "El real es 456.000 y el presupuesto 480.000; la diferencia es 24.000 a favor."),
        ("=", "{F} ¿Después de cuántos días de consumo normal el saldo de 140 baja a 40 sacos?", "(140-40)//25", "Se divide lo que se consume hasta llegar a 40 entre el consumo diario.", " días"),
        ("ab", "{F} Un jefe dice: «pidamos cuando el saldo llegue a 25 sacos, o sea un día de consumo». ¿Qué respuesta es correcta?", "No: el proveedor tarda 3 días y el material se acabaría antes de que llegue", "Sí: con un día de consumo basta", "El punto de reposición debe cubrir al menos el plazo de entrega más un margen."),
        ("abc", "{F} Si el proveedor tardara 5 días en vez de 3 (con el mismo margen), ¿cuál sería el punto de reposición?", "150 sacos", "100 sacos", "125 sacos", "Se usan 5+1 = 6 días por 25 sacos, que son 150."),
        ("abc", "{F} Un compañero propone anotar horas menores en E4 para que se vea ahorro. ¿Qué corresponde?", "Rechazarlo: los registros reflejan lo real, aunque haya sobrecosto", "Aceptarlo, si la diferencia es pequeña", "Aceptarlo, si lo firma otra persona", "Un registro falso oculta un problema y es una falta."),
    ],
    ctx=("abc", "Una jefa de obra de ejemplo revisa la planilla: el saldo de un material está justo en el punto de reposición. ¿Qué decide?", "Hacer el pedido ahora y dejar el registro de la decisión", "Esperar una semana más", "Pedir solo si el proveedor lo ofrece", "Al llegar al punto de reposición se pide, para no quedarse sin material."),
    sc=[
        ("En Construcción: ¿qué es la desviación de un costo?", "La diferencia entre el presupuesto y el costo real", "Muestra si hubo ahorro o sobrecosto."),
        ("¿Cómo se calcula el costo real de un equipo?", "Horas trabajadas por costo por hora", "El costo depende de cuántas horas se trabajó."),
        ("¿Para qué sirve el margen en la reposición?", "Para dar una reserva por si el proveedor se atrasa", "Evita quedarse sin material por pequeñas demoras."),
    ],
    op=("Obra de ejemplo «Taller Boldo»: consumo de 12 planchas por día, plazo de entrega de 4 días y 1 día de margen; saldo actual de 70 planchas. Equipo E5: $9.000 por hora, presupuesto de 30 horas, trabajadas 33. Escribe (a) el punto de reposición, (b) si hay que pedir ya, (c) el costo real de E5, (d) si hay ahorro o sobrecosto y de cuánto.",
        "(a) 12 por (4+1) son 60 planchas. (b) No: 70 es mayor que 60. (c) 33 por 9.000 son 297.000 pesos. (d) El presupuesto es 30 por 9.000 = 270.000; hay sobrecosto de 27.000 pesos.",
        ["calcula el punto de reposición", "decide con la regla", "calcula el costo real", "calcula la desviación"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el margen", "restar mal las horas", "decir ahorro cuando hay sobrecosto"],
        "Pregunta: «¿cuántos días usas en el cálculo?». Si no responde, pídele que relea qué se suma al plazo."),
    reinforce="Inventa un material con consumo diario, plazo y margen, y calcula su punto de reposición.",
    extend="Explica por qué una obra con buenos registros puede anticipar compras y evitar atrasos.",
)

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (faena de ejemplo, inventada). Obra «Edificio Cóndor» (ficticia). Peligros anotados por la prevencionista de ejemplo: caída de personas desde altura, golpe por objetos que caen, ruido, polvo y atrapamiento. "
     "EPP entregados en la obra: casco, lentes, calzado de seguridad, guantes y protector auditivo. Cada trabajador firma un registro cuando recibe sus EPP. "
     "Aspectos ambientales anotados: escombros, polvo y ruido hacia los vecinos. La norma vigente y la entidad fiscalizadora definen lo que se debe cumplir.")
build(
    O9, 1, F,
    use="Aprenderé el vocabulario básico de seguridad y prevención en una obra, la jerarquía de controles y por qué se cuida también el medio ambiente.",
    prior=["Sé leer una ficha con datos.", "Sé contar y sumar enteros.", "Sé que las normas se cumplen aunque nadie mire."],
    explain=[
        "Un peligro es algo que puede causar daño, como un objeto que puede caer. El riesgo es la posibilidad de que ese daño ocurra y su gravedad. Un incidente es un hecho que pudo causar daño y no lo causó; un accidente es un hecho que sí causó daño a una persona. La prevención de riesgos reúne las medidas que evitan accidentes. La jerarquía de controles ordena esas medidas: primero eliminar el peligro, luego reducirlo en su origen o proteger a todo el grupo, y recién al final proteger a cada persona con elementos de protección personal (EPP), como casco, lentes o calzado de seguridad.",
        "La señalética son las señales de seguridad que avisan peligros, obligaciones y salidas. Además de cuidar a las personas, una obra debe cuidar el medio ambiente: los escombros, el polvo y el ruido tienen reglas que fija la norma vigente. La entidad fiscalizadora vigila el cumplimiento, y cada persona de la obra tiene la obligación de conocer las reglas, usar sus EPP y avisar de los peligros que vea.",
        f"Este cuaderno explica conceptos; no te autoriza a trabajar en altura ni con maquinaria. {EMER} {AVISO}",
    ],
    vocab=[("peligro", "algo que puede causar daño"), ("riesgo", "posibilidad de que el daño ocurra y su gravedad"), ("incidente", "hecho que pudo causar daño y no lo causó"), ("accidente", "hecho que causó daño a una persona"), ("jerarquía de controles", "orden de medidas: eliminar, reducir o proteger al grupo y, al final, proteger a la persona"), ("EPP", "elementos de protección personal"), ("señalética", "señales de seguridad que avisan peligros, obligaciones y salidas"), ("escombros", "restos sólidos que deja una obra")],
    worked=[
        ("Peligro o riesgo", "Un piso de ejemplo tiene una abertura sin protección. ¿La abertura es un peligro o un accidente?", ["La abertura puede causar daño, pero aún no lo causó.", "Algo que puede causar daño es un peligro."], "Un peligro"),
        ("Orden de controles", "Una cubierta de ejemplo tiene un objeto que puede caer. Entre eliminar el objeto o dar casco a las personas, ¿qué va primero?", ["La jerarquía parte por eliminar el peligro.", "El casco, un EPP, va al final."], "Eliminar el objeto"),
    ],
    mistakes=[("Creer que con casco y guantes ya no hace falta eliminar peligros.", "Los EPP son la última barrera; no reemplazan eliminar o reducir el peligro.", "Aplica primero la jerarquía y usa EPP como último control."),
              ("Pensar que un incidente sin heridos no hay que informarlo.", "El mismo hecho puede causar daño la próxima vez.", "Informa también los incidentes.")],
    T=[
        ("abc", "En Construcción: ¿qué es un peligro?", "Algo que puede causar daño", "Un daño que ya ocurrió", "Una norma que se cumple", "Peligro es la fuente que puede causar daño; el daño ya ocurrido es el accidente."),
        ("abc", "En Construcción: ¿qué diferencia hay entre un incidente y un accidente?", "El incidente pudo causar daño y no lo causó; el accidente sí causó daño", "El incidente ocurre solo de noche", "El accidente nunca se informa", "El accidente deja daño a una persona; el incidente no, pero se informa igual."),
        ("abc", "En la jerarquía de controles, ¿qué va al final?", "Proteger a cada persona con EPP", "Eliminar el peligro", "Reducir el peligro en su origen", "Los EPP protegen a la persona, pero el peligro sigue existiendo."),
        ("=", "{F} Hay 12 trabajadores y 9 ya firmaron el registro de entrega de EPP. ¿Cuántos faltan por firmar?", "12-9", "Se resta a los trabajadores los que ya firmaron.", " trabajadores"),
        ("abc", "{F} ¿Qué aspectos ambientales anota la ficha?", "Escombros, polvo y ruido hacia los vecinos", "Solo el color de las paredes", "Humo de fábricas lejanas", "La ficha anota exactamente escombros, polvo y ruido."),
        ("abc", "{F} Un trabajador recibe sus EPP pero no firma el registro. ¿Qué corresponde?", "Pedirle que firme para dejar constancia de la entrega", "Dejarlo así, porque ya los tiene", "Firmar por él para ahorrar tiempo", "El registro firmado prueba que la entrega ocurrió y quién la recibió."),
        ("=", "{F} La obra tiene 12 trabajadores y cada uno recibe los EPP de la ficha. ¿Cuántos elementos se entregan en total?", "12*5", "Se multiplican los trabajadores por los EPP de cada uno.", " elementos"),
        ("abc", "{F} Se anota un objeto que puede caer desde un piso. ¿Cuál es la medida más alta de la jerarquía?", "Eliminar o retirar el objeto del lugar donde puede caer", "Dar casco a todo el personal y no tocar el objeto", "Pedir que nadie lo mire", "Primero se elimina el peligro; el casco es el último control."),
        ("ab", "{F} Un compañero dice: «usamos casco, así que no hace falta informar un objeto suelto en altura». ¿Qué respuesta es correcta?", "No: el objeto suelto es un peligro que debe informarse y controlarse en origen", "Sí: con casco ya no hay riesgo", "El casco solo reduce la gravedad del golpe; el peligro sigue existiendo."),
        ("abc", "{F} Una persona cae desde una altura en la faena y queda en el suelo. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Moverla de inmediato para ponerla cómoda", "Subir a ver qué falló antes de avisar", "Acercarse o moverla sin saber puede agravar el daño; se avisa a quien corresponde."),
        ("=", "{F} Si los escombros de un día pesan 3 toneladas (de ejemplo) y se retiran 5 días seguidos con la misma cantidad, ¿cuántas toneladas se retiran?", "3*5", "Se multiplican las toneladas diarias por los días.", " toneladas"),
        ("abc", "{F} ¿Qué dice la ficha sobre quién define lo que se debe cumplir?", "La norma vigente y la entidad fiscalizadora", "El trabajador que lleva más años", "El proveedor de los EPP", "La ficha dice que lo definen la norma vigente y la entidad fiscalizadora."),
        ("abc", "{F} Un vecino reclama por el ruido de la obra. ¿Qué corresponde?", "Informar al jefe de obra para aplicar las medidas ambientales según la norma vigente", "Ignorarlo, porque la obra es temporal", "Pedirle que reclame al proveedor", "El ruido hacia vecinos es un aspecto ambiental que se informa y se controla."),
    ],
    ctx=("abc", "Un trabajador de ejemplo ve un cable tendido en el paso y dice «ya alguien lo verá». ¿Qué corresponde?", "Avisar de inmediato al supervisor para que lo controle", "Pasar por encima con cuidado", "Esperar a que alguien se accidente", "Los peligros se informan; no se asume que otra persona lo hará."),
    sc=[
        ("En Construcción: ¿qué son los EPP?", "Elementos de protección personal, como casco y lentes", "Protegen a la persona, pero van al final de la jerarquía."),
        ("¿Qué se informa además de los accidentes?", "Los incidentes y los peligros que se vean", "Informarlos evita que el daño ocurra la próxima vez."),
        ("¿Quién fiscaliza el cumplimiento de la norma?", "La entidad fiscalizadora", "La norma vigente fija las reglas y la entidad las vigila."),
    ],
    op=("Obra de ejemplo «Bodega Tilo»: peligros anotados: golpe por objetos, ruido y escombros acumulados; EPP entregados a 8 trabajadores: casco, lentes y guantes. Escribe (a) cuántos EPP se entregan en total, (b) qué control va primero para el golpe por objetos, (c) qué aspecto ambiental anotas y (d) qué haces si un trabajador no firmó el registro de EPP.",
        "(a) 8 por 3 son 24 EPP. (b) Eliminar o reducir el peligro en su origen, antes de dar casco. (c) Los escombros acumulados y el ruido. (d) Le pido que firme para dejar constancia.",
        ["calcula los EPP", "aplica la jerarquía", "nombra un aspecto ambiental", "pide la firma"],
        ["hoja con las cuatro respuestas"],
        ["empezar por el EPP", "firmar por el trabajador", "olvidar el aspecto ambiental"],
        "Pregunta: «¿qué va primero en la jerarquía?». Si no responde, pídele que relea el orden de los controles."),
    reinforce="Escribe tres peligros de una obra y, para cada uno, qué medida va primero según la jerarquía.",
    extend="Explica con un ejemplo inventado por qué un EPP no basta para controlar un peligro.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (señales y matriz de ejemplo, inventadas). Señales de la obra «Edificio Cóndor» (ficticia): S1, círculo azul con símbolo de casco; S2, triángulo amarillo con símbolo de golpe; "
     "S3, círculo con borde rojo y una diagonal sobre un cigarrillo; S4, cuadrado verde con símbolo de salida. Matriz de ejemplo (probabilidad de 1 a 4 por consecuencia de 1 a 4): "
     "ruido, probabilidad 3 y consecuencia 1; golpe por objetos, probabilidad 2 y consecuencia 4; polvo, probabilidad 3 y consecuencia 2. "
     "Roles: el trabajador usa sus EPP y avisa; el supervisor controla; el experto en prevención asesora y revisa; el comité de seguridad de ejemplo reúne a representantes de trabajadores y de la empresa.")
build(
    O9, 2, F,
    use="Aprenderé a interpretar señales de seguridad por su forma y color, a leer una matriz de riesgos y a reconocer los roles de la prevención.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé multiplicar enteros pequeños.", "Sé qué es la jerarquía de controles."],
    explain=[
        "Las señales de seguridad se reconocen por su forma y color. Una señal de prohibición es un círculo con borde rojo y una diagonal: indica algo que no se debe hacer. Una señal de obligación es un círculo azul: indica algo que se debe usar o hacer, como el casco. Una señal de advertencia es un triángulo amarillo: avisa un peligro. Una señal de salida o emergencia es verde. Las de equipos contra incendio son rojas. La norma vigente define el detalle de cada una.",
        "La matriz de riesgos es una tabla que ordena los peligros por su nivel de riesgo. En nuestra forma de ejemplo, el nivel de riesgo es la probabilidad (qué tan posible es que ocurra) multiplicada por la consecuencia (qué tan grave sería). Se atiende primero el nivel más alto. Los roles también importan: el trabajador usa sus EPP y avisa; el supervisor controla; el experto en prevención asesora y revisa; el comité de seguridad reúne a representantes del personal y de la empresa.",
        f"Los valores de la matriz son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("señal de prohibición", "círculo con borde rojo y una diagonal; indica lo que no se debe hacer"), ("señal de obligación", "círculo azul; indica lo que se debe usar o hacer"), ("señal de advertencia", "triángulo amarillo; avisa un peligro"), ("señal de salida o emergencia", "señal verde que indica salidas y ayuda"), ("matriz de riesgos", "tabla que ordena los peligros por nivel de riesgo"), ("nivel de riesgo", "probabilidad multiplicada por consecuencia, en el ejemplo"), ("experto en prevención", "persona que asesora y revisa la seguridad de la obra")],
    worked=[
        ("Leer una señal", "Una señal de ejemplo es un triángulo amarillo con el dibujo de una escalera. ¿Es de prohibición, obligación o advertencia?", ["La forma triangular y el color amarillo son de las señales que avisan un peligro.", "Es una señal de advertencia."], "Advertencia"),
        ("Nivel de riesgo", "Un peligro de ejemplo tiene probabilidad 2 y consecuencia 3. ¿Cuál es su nivel de riesgo?", ["Se multiplica probabilidad por consecuencia.", "2 por 3 son 6."], "6"),
    ],
    mistakes=[("Confundir una señal de prohibición con una de obligación porque ambas son redondas.", "Se distinguen por el color: borde rojo con diagonal o círculo azul.", "Mira siempre forma y color juntos."),
              ("Atender primero el peligro más fácil de arreglar.", "La matriz ordena por nivel de riesgo, no por facilidad.", "Atiende primero el nivel más alto.")],
    T=[
        ("abc", "En Construcción: ¿cómo es una señal de prohibición?", "Un círculo con borde rojo y una diagonal", "Un círculo azul con un dibujo", "Un triángulo amarillo", "La prohibición se reconoce por el borde rojo y la diagonal."),
        ("abc", "En Construcción: ¿qué indica una señal de obligación?", "Algo que se debe usar o hacer", "Un peligro cercano", "La salida de emergencia", "La obligación manda usar o hacer algo, por ejemplo el casco."),
        ("abc", "¿Cuál es la función de una matriz de riesgos?", "Ordenar los peligros por su nivel de riesgo para atender primero los más altos", "Registrar el sueldo del personal", "Dibujar los planos de la obra", "La matriz prioriza peligros según su nivel."),
        ("abc", "{F} ¿Qué tipo de señal es la S1?", "Obligación", "Prohibición", "Advertencia", "S1 es un círculo azul, propio de las señales de obligación."),
        ("abc", "{F} ¿Qué indica la señal S3?", "Que no se debe fumar", "Que se debe usar casco", "Que hay salida de emergencia", "S3 tiene borde rojo y diagonal sobre un cigarrillo: prohíbe fumar."),
        ("=", "{F} ¿Cuál es el nivel de riesgo del golpe por objetos?", "2*4", "Se multiplica probabilidad por consecuencia.", " puntos"),
        ("=", "{F} ¿Cuál es el nivel de riesgo del polvo?", "3*2", "Se multiplica probabilidad por consecuencia del polvo.", " puntos"),
        ("abc", "{F} ¿Qué peligro de la matriz se atiende primero?", "El golpe por objetos, porque tiene el nivel más alto", "El ruido, porque su probabilidad es alta", "El polvo, porque es el más frecuente", "El nivel más alto es 8 (golpe por objetos), frente a 3 y 6."),
        ("abc", "{F} Una señal verde de salida está tapada por unos materiales apilados. ¿Qué corresponde?", "Avisar al supervisor para despejarla, porque debe verse siempre", "Dejarla, porque ya se sabe dónde está", "Quitar la señal para que no estorbe", "La señal de emergencia debe verse en todo momento."),
        ("ab", "{F} Un trabajador dice: «la señal S2 es una obligación porque es redonda». ¿Qué respuesta es correcta?", "No: S2 es un triángulo amarillo, de advertencia", "Sí: toda señal redonda es de obligación", "La forma triangular y el color amarillo corresponden a una advertencia."),
        ("abc", "{F} ¿Qué rol revisa y asesora la seguridad de la obra?", "El experto en prevención", "El proveedor", "El visitante", "Según la ficha, el experto en prevención asesora y revisa."),
        ("=", "{F} Si la probabilidad del ruido subiera de 3 a 4 con la misma consecuencia, ¿cuál sería su nivel de riesgo?", "4*1", "Se multiplica la nueva probabilidad por la consecuencia.", " puntos"),
        ("abc", "{F} Un andamio mal ubicado se viene abajo y atrapa a una persona. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar levantar el andamio entre todos", "Acercarse a mirar el daño", "Acercarse o intervenir sin ayuda puede causar otro accidente."),
    ],
    ctx=("abc", "Un visitante de ejemplo entra a una faena donde hay una señal azul de casco y no la sigue. ¿Qué corresponde?", "Avisarle que debe usar el casco y comunicarlo al supervisor", "Dejarlo pasar, porque es solo una visita", "Quitar la señal para evitar conflictos", "Las señales de obligación valen para todas las personas, incluidas las visitas."),
    sc=[
        ("En Construcción: ¿qué indica un triángulo amarillo?", "Una advertencia de peligro", "La forma y el color de advertencia avisan un peligro."),
        ("¿Cómo se obtiene el nivel de riesgo en el ejemplo?", "Probabilidad multiplicada por consecuencia", "El valor más alto se atiende primero."),
        ("¿Quién asesora y revisa la seguridad?", "El experto en prevención", "El supervisor controla y el trabajador avisa."),
    ],
    op=("Matriz de ejemplo de «Taller Ulmo»: ruido, probabilidad 2 y consecuencia 2; objeto que cae, probabilidad 2 y consecuencia 4; polvo, probabilidad 3 y consecuencia 2. Señal Z: círculo azul con símbolo de lentes. Escribe (a) el nivel de riesgo de cada peligro, (b) cuál atiendes primero, (c) qué tipo de señal es Z y qué indica, (d) a quién avisas si una señal está tapada.",
        "(a) Ruido 2 por 2 = 4; objeto que cae 2 por 4 = 8; polvo 3 por 2 = 6. (b) El objeto que cae, porque tiene el nivel más alto (8). (c) Obligación: se deben usar lentes. (d) Al supervisor.",
        ["calcula los tres niveles", "reconoce el empate", "interpreta la señal", "nombra a quién avisa"],
        ["hoja con las cuatro respuestas"],
        ["decir que el ruido va primero", "confundir obligación con prohibición", "tapar la señal"],
        "Pregunta: «¿cuál es el nivel más alto?». Si no responde, pídele que relea cómo se calcula el nivel de riesgo."),
    reinforce="Dibuja en palabras cuatro señales (prohibición, obligación, advertencia y salida) y escribe su forma y color.",
    extend="Explica por qué una matriz de riesgos ayuda a decidir qué atender primero cuando hay varios peligros.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (registro de entrega de EPP y revisión de faena, de ejemplo, inventados). Obra «Liceo Peumo» (ficticia). Registro de entrega de casco, lentes y calzado: "
     "Ana, recibió los tres, firmó; Bruno, recibió casco y lentes, no firmó; Carla, recibió casco y calzado, firmó; Diego, recibió los tres, firmó. "
     "Revisión de la faena del día (de ejemplo): una señal de obligación está caída en el suelo; los escombros están mezclados con envases de pintura vacíos junto a la reja; "
     "una zona de acopio tiene el paso de personas bloqueado. Regla de ejemplo: cada trabajador debe tener los tres EPP y la firma en el registro.")
build(
    O9, 3, F,
    use="Analizaré en papel un registro de entrega de EPP y una revisión de faena para encontrar incumplimientos y decidir a quién informar.",
    prior=["Sé qué son los EPP y la señalética.", "Sé qué es un registro firmado.", "Sé contar con enteros."],
    explain=[
        "Una revisión de faena es un recorrido por la obra para comprobar que se cumplen las reglas de seguridad y ambientales, y se anota en un registro. Cada hallazgo se escribe con qué se vio, dónde y cuándo. Un hallazgo es un incumplimiento cuando algo no cumple una regla: por ejemplo, un EPP que falta, una señal caída, un paso bloqueado o residuos mezclados. Los residuos peligrosos, como envases de productos químicos, se separan de los escombros comunes según la norma vigente.",
        "En el registro de entrega de EPP se revisa que cada persona tenga todos los elementos y la firma. Un hallazgo no se esconde ni se corrige en silencio: se informa al supervisor, que decide la medida y deja constancia. Mientras una situación riesgosa no se corrige, se avisa y se mantiene a las personas lejos de ella. Este análisis se hace en papel; no incluye intervenir ni mover estructuras.",
        f"Los casos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("revisión de faena", "recorrido para comprobar que se cumplen las reglas de la obra"), ("hallazgo", "algo que se observa y se anota en la revisión"), ("incumplimiento", "algo que no cumple una regla"), ("residuo peligroso", "residuo que puede dañar a personas o al ambiente, como envases de productos químicos"), ("constancia", "anotación escrita de lo observado y decidido")],
    worked=[
        ("Revisar un registro", "Un registro de ejemplo debe tener casco y calzado firmados por 5 trabajadores, pero solo 4 firmaron. ¿Cuántas firmas faltan?", ["Se comparan las firmas esperadas con las recibidas.", "5 menos 4 es 1."], "1 firma"),
        ("Clasificar", "En una faena de ejemplo hay una lata vacía de producto químico junto a un montón de ladrillos rotos. ¿Cuál es un residuo peligroso?", ["Los productos químicos pueden dañar.", "La lata se separa de los ladrillos rotos."], "La lata de producto químico"),
    ],
    mistakes=[("Corregir en silencio un hallazgo para que el registro «quede limpio».", "Un hallazgo oculto vuelve a ocurrir.", "Anótalo e informa al supervisor."),
              ("Mezclar todos los residuos porque «igual se botan».", "Los residuos peligrosos exigen manejo distinto según la norma vigente.", "Sepáralos y avisa.")],
    T=[
        ("abc", "En Construcción: ¿qué es una revisión de faena?", "Un recorrido para comprobar que se cumplen las reglas de seguridad y ambientales", "Una reunión para repartir ganancias", "El cobro del arriendo del terreno", "Una revisión busca incumplimientos mediante un recorrido y un registro."),
        ("abc", "En Construcción: ¿qué es un residuo peligroso?", "Un residuo que puede dañar a personas o al ambiente, como un envase de producto químico", "Un residuo muy pesado", "Un residuo que se acumula rápido", "Peligroso se refiere al daño posible, no al peso ni a la rapidez."),
        ("abc", "¿Qué se hace con un hallazgo en una revisión?", "Anotarlo con qué, dónde y cuándo, e informar al supervisor", "Corregirlo en silencio y no anotarlo", "Esperar a que se olvide", "Un hallazgo se anota e informa para que se tome una medida registrada."),
        ("=", "{F} ¿Cuántos trabajadores firmaron el registro de entrega de EPP?", "4-1", "La ficha lista a cuatro trabajadores y solo Bruno no firmó.", " trabajadores"),
        ("abc", "{F} Según la regla, ¿qué incumplimientos tiene el registro de EPP?", "Bruno no recibió calzado ni firmó, y Carla no recibió lentes", "Solo Diego tiene un incumplimiento", "Ninguno, porque todos recibieron algo", "La regla pide los tres EPP y firma; Bruno y Carla no cumplen."),
        ("=", "{F} ¿Cuántos EPP en total se registran entregados?", "3+2+2+3", "Se suman los elementos recibidos por Ana, Bruno, Carla y Diego.", " elementos"),
        ("abc", "{F} ¿Qué hallazgo de la revisión es ambiental?", "Los escombros mezclados con envases de pintura vacíos", "La señal de obligación caída", "El paso bloqueado por el acopio", "La mezcla de residuos peligrosos con escombros es un tema ambiental."),
        ("abc", "{F} ¿Qué hallazgo de la revisión afecta la circulación segura de las personas?", "El paso bloqueado en la zona de acopio", "El envase de pintura en la reja", "El registro de Ana", "Un paso bloqueado impide circular y evacuar con seguridad."),
        ("=", "{F} Si cada trabajador debe tener 3 EPP, ¿cuántos EPP faltan en total para cumplir la regla?", "4*3-(3+2+2+3)", "Se restan los EPP registrados a los que deberían estar.", " elementos"),
        ("ab", "{F} Un supervisor dice: «la señal caída la dejamos, todos saben qué decía». ¿Qué respuesta es correcta?", "No: se anota el hallazgo y la señal se repone para que siga visible", "Sí: la memoria reemplaza la señal", "Una señal caída deja de cumplir su función y debe reponerse según el control del supervisor."),
        ("abc", "{F} Un trabajador sugiere quemar los envases de pintura en un rincón «para despejar». ¿Qué corresponde?", "Rechazarlo y avisar al supervisor para su manejo según la norma vigente", "Aceptar, si lo hacen de noche", "Aceptar, si apagan el fuego después", "Los residuos peligrosos no se queman ni se esconden; se manejan según la norma vigente."),
        ("abc", "Parte de un moldaje se derrumba y atrapa a un trabajador. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Retirar el moldaje a mano entre varios", "Entrar rápido a ayudar", "Acercarse puede causar otro derrumbe; se avisa a quien corresponde."),
        ("abc", "{F} Bruno no firmó el registro y dice que lo hará «después». ¿Qué corresponde?", "Pedirle que firme hoy y dejar constancia de la entrega", "Firmar por él", "Borrar su nombre del registro", "La firma debe ser de la persona que recibió y en el momento de la entrega."),
    ],
    ctx=("abc", "Una practicante de ejemplo encuentra la revisión de la faena con varios incumplimientos y el supervisor le pide «no anotarlos». ¿Qué corresponde?", "Anotar lo que observó y avisar al experto en prevención o a un adulto responsable", "Callarse, porque el supervisor manda", "Borrar la hoja de la revisión", "Los hallazgos se anotan y se informan; esconderlos pone en riesgo a las personas."),
    sc=[
        ("En Construcción: ¿qué es un hallazgo?", "Algo que se observa en una revisión y se anota", "Se anota con qué, dónde y cuándo se vio."),
        ("¿Cómo se manejan los residuos peligrosos?", "Se separan y se manejan según la norma vigente", "No se mezclan con los escombros comunes."),
        ("¿Quién firma la entrega de EPP?", "La persona que los recibe", "La firma deja constancia de la entrega."),
    ],
    op=("Registro de ejemplo de la obra «Taller Coihue»: Elena recibió casco y lentes (firmó); Felipe recibió solo el casco (firmó); Gloria recibió casco y lentes (no firmó). Regla: cada persona debe tener casco y lentes con firma. Revisión: un tacho de residuos peligrosos está sin tapa junto a la entrada. Escribe (a) quiénes incumplen y por qué, (b) cuántos EPP faltan, (c) el hallazgo ambiental y (d) qué haces con lo encontrado.",
        "(a) Felipe, porque no tiene lentes; Gloria, porque no firmó. (b) Falta 1 elemento (los lentes de Felipe). (c) El tacho de residuos peligrosos sin tapa. (d) Anoto los hallazgos e informo al supervisor para que tome medidas y deje constancia.",
        ["detecta los dos incumplimientos", "cuenta los EPP faltantes", "reconoce el hallazgo ambiental", "informa sin ocultar"],
        ["hoja con las cuatro respuestas"],
        ["incluir a Elena", "no contar la firma como incumplimiento", "corregir en silencio"],
        "Pregunta: «¿qué pide la regla a cada persona?». Si no responde, pídele que relea la regla del registro."),
    reinforce="Escribe tres hallazgos que podrías anotar en una revisión de faena y a quién informarías cada uno.",
    extend="Explica por qué anotar un incumplimiento pequeño a tiempo evita que se transforme en un accidente.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (criterios de ejemplo, inventados). Obra «Sede Pehuén» (ficticia). Matriz de riesgos de ejemplo (probabilidad 1 a 4 por consecuencia 1 a 4): "
     "A, polvo, 3 por 2; B, objeto que cae, 2 por 4; C, ruido, 4 por 1; D, atrapamiento, 1 por 4. Regla de ejemplo: nivel 6 o más exige un control antes de iniciar la tarea. "
     "Señalética pedida: 6 señales de obligación, 4 de advertencia y 2 de prohibición, a $4.500 cada una (de ejemplo). Dotación: 20 trabajadores; EPP entregados con firma: 18 trabajadores. "
     "Regla de ejemplo: la entrega con firma debe ser el 100 % de los trabajadores.")
build(
    O9, 4, F,
    use="Aplicaré criterios de ejemplo para priorizar riesgos, presupuestar señalética y calcular el cumplimiento de la entrega de EPP.",
    prior=["Sé qué es una matriz de riesgos.", "Sé multiplicar, sumar y restar enteros.", "Sé qué señal es de obligación, advertencia y prohibición."],
    explain=[
        "Para priorizar se usa el nivel de riesgo: probabilidad por consecuencia. Una regla de la obra puede fijar un umbral, por ejemplo: desde cierto nivel, hay que aplicar un control antes de empezar la tarea. El umbral es el valor desde el cual se exige una acción. Así se decide con un criterio claro y no por impresión. Después de decidir, se elige el control según la jerarquía: primero eliminar o reducir en origen, y los EPP al final.",
        "También se calcula el cumplimiento: cuántos trabajadores cumplen sobre el total. El porcentaje de cumplimiento se obtiene dividiendo los que cumplen entre el total y multiplicando por 100. Y se presupuesta la señalética: la cantidad total de señales se multiplica por el precio de una. Los valores son de ejemplo; en una obra real los fija el proyecto y la norma vigente.",
        f"Todo se resuelve en planilla. {EMER} {AVISO}",
    ],
    vocab=[("umbral", "valor desde el cual se exige una acción"), ("nivel de riesgo", "probabilidad multiplicada por consecuencia, en el ejemplo"), ("control", "medida que reduce o elimina un riesgo"), ("cumplimiento", "proporción de personas o tareas que cumplen una regla"), ("porcentaje", "parte de un total expresada sobre 100"), ("presupuesto de señalética", "costo total de las señales: cantidad por precio")],
    worked=[
        ("Aplicar el umbral", "Un peligro de ejemplo tiene probabilidad 2 y consecuencia 2. Con un umbral de 6, ¿exige control previo?", ["Nivel: 2 por 2 = 4.", "4 es menor que 6."], "No exige control previo"),
        ("Porcentaje", "En una obra de ejemplo 8 de 10 trabajadores tienen todos sus EPP. ¿Qué porcentaje cumple?", ["8 dividido por 10 es 0,8.", "0,8 por 100 es 80."], "80 %"),
    ],
    mistakes=[("Elegir el control con EPP como primera opción porque es lo más barato.", "El EPP es el último control de la jerarquía.", "Revisa primero eliminar o reducir el peligro."),
              ("Dar por cumplido un 90 % cuando la regla pide 100 %.", "La regla exige que todos cumplan.", "Compara con el valor que fija la regla.")],
    T=[
        ("abc", "En Construcción: ¿qué es un umbral de riesgo?", "El valor desde el cual se exige una acción", "El peso máximo de un material", "El horario de término de la jornada", "El umbral fija desde qué nivel hay que actuar."),
        ("abc", "En Construcción: ¿cómo se calcula un porcentaje de cumplimiento?", "Se divide los que cumplen entre el total y se multiplica por 100", "Se suman los que cumplen y los que no", "Se resta el total a los que cumplen", "El porcentaje relaciona a los que cumplen con el total sobre 100."),
        ("abc", "Cuando se elige un control para un riesgo alto, ¿qué se revisa primero?", "Eliminar o reducir el peligro en su origen", "Entregar EPP", "Esperar a que ocurra un incidente", "La jerarquía de controles parte por eliminar o reducir en origen."),
        ("=", "{F} ¿Cuál es el nivel de riesgo del objeto que cae (B)?", "2*4", "Se multiplica probabilidad por consecuencia.", " puntos"),
        ("abc", "{F} ¿Qué peligros exigen un control antes de iniciar la tarea, según el umbral de 6?", "Solo el objeto que cae (B), con nivel 8, y el polvo (A), con nivel 6", "Solo el ruido (C), con nivel 4", "Todos, incluido el atrapamiento (D), con nivel 4", "Se exige control desde 6: A tiene 6 y B tiene 8; C y D tienen 4."),
        ("=", "{F} ¿Cuántas señales se piden en total?", "6+4+2", "Se suman las señales de los tres tipos.", " señales"),
        ("=", "{F} ¿Cuánto cuesta la señalética en total?", "(6+4+2)*4500", "Se multiplica el total de señales por el precio de una.", " pesos"),
        ("=", "{F} ¿Cuántos trabajadores todavía no tienen la entrega con firma?", "20-18", "Se restan los que tienen entrega firmada al total.", " trabajadores"),
        ("abc", "{F} ¿Qué porcentaje de trabajadores tiene la entrega con firma?", "90 %", "18 %", "80 %", "18 dividido por 20 es 0,9, que equivale a 90 sobre 100."),
        ("ab", "{F} Un jefe dice: «90 % es suficiente». ¿Qué respuesta es correcta?", "No: la regla de la obra exige el 100 % de los trabajadores", "Sí: 90 % aprueba", "La regla fija el 100 %, y dos trabajadores sin EPP firmados siguen sin cubrir."),
        ("abc", "{F} Para el objeto que cae (B), ¿cuál control es el más alto en la jerarquía?", "Eliminar o retirar el objeto del lugar donde puede caer", "Entregar casco a todos y dejar el objeto", "Poner una señal de advertencia solamente", "Eliminar es el primer control; la señal y el casco son controles posteriores."),
        ("abc", "{F} Si el precio de una señal subiera a $5.000 (de ejemplo), ¿cuánto costarían las 12 señales?", "$60.000", "$54.000", "$48.000", "12 señales por $5.000 son $60.000."),
        ("abc", "Ante un atrapamiento en una faena de ejemplo, ¿qué debe hacer una persona sin autorización?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a rescatar para ganar tiempo", "Esperar a que se arregle solo", "Intervenir sin autorización puede causar otro accidente; se avisa a quien corresponde."),
    ],
    ctx=("abc", "Un jefe de obra de ejemplo tiene dinero para una sola mejora: más señales o entregar los EPP firmados que faltan. La ficha dice que debe cumplir el 100 % de las entregas. ¿Qué decide primero?", "Completar las entregas firmadas, porque la regla lo exige y protege directamente a las personas", "Comprar más señales aunque falten EPP", "Esperar a la próxima revisión", "Una regla que exige el 100 % se cumple antes de gastar en mejoras opcionales."),
    sc=[
        ("En Construcción: ¿qué hace un umbral de riesgo?", "Fija desde qué nivel hay que aplicar un control", "Permite decidir con un criterio claro."),
        ("¿Cuál es el último control de la jerarquía?", "Los EPP", "Protegen a la persona pero el peligro sigue existiendo."),
        ("¿Qué cálculo da el costo de la señalética?", "Cantidad de señales por el precio de una", "Se multiplica la cantidad total por el precio unitario."),
    ],
    op=("Obra de ejemplo «Gimnasio Mañío»: peligros: P, ruido, 4 por 2; Q, objeto que cae, 3 por 3; R, polvo, 1 por 4. Umbral: nivel 6 o más exige control previo. Se piden 5 señales de obligación y 3 de advertencia a $3.000 cada una. De 25 trabajadores, 20 tienen la entrega de EPP con firma. Escribe (a) el nivel de cada peligro y cuáles exigen control, (b) el costo de las señales, (c) cuántos trabajadores faltan por firmar.",
        "(a) P 8; Q 9; R 4. Exigen control P y Q. (b) 8 señales por 3.000 son 24.000 pesos. (c) 25-20 son 5 trabajadores.",
        ["calcula los tres niveles", "aplica el umbral", "calcula el costo", "calcula los faltantes"],
        ["hoja con las tres respuestas"],
        ["incluir R entre los que exigen control", "sumar mal las señales", "no restar los 20"],
        "Pregunta: «¿desde qué nivel se exige control?». Si no responde, pídele que relea el umbral."),
    reinforce="Inventa una matriz de tres peligros con probabilidad y consecuencia, calcula los niveles y decide cuáles exigen control con un umbral de 6.",
    extend="Explica por qué fijar un umbral numérico ayuda a decidir con el mismo criterio en todas las tareas.",
)

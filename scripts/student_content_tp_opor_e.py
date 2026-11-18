"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-05 (completar y verificar la documentación de recepción y despacho, cero faltas). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O5 = "TP-OPOR-3y4-OAE-05"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La oficina de documentos de «Terminal Demo» recepciona en un día 48 camiones y despacha 30. Cada recepción requiere 3 documentos (guía de recepción, lista de embalaje y registro de ingreso) "
     "y cada despacho requiere 4. Trabajan 6 personas. Observaciones anotadas: una persona comparte su clave de acceso con un compañero «para ir más rápido»; otra revisa documentos en su teléfono mientras camina por el patio entre vehículos; "
     "y se digitó con un error el número de un contenedor.")
build(
    O5, 1, F,
    use="Aprenderé qué es la recepción y el despacho de carga, por qué la documentación debe estar completa y sin errores, y qué riesgos tiene el trabajo documental, incluida la seguridad de la información.",
    prior=["Sé qué es un conocimiento de embarque y una lista de embalaje.", "Sé multiplicar y dividir números enteros.", "Sé qué es una clave de acceso."],
    explain=[
        "La recepción es el proceso en que la carga que llega se recibe, se cuenta y se registra contra sus documentos. El despacho es la entrega de la carga a quien la retira, con sus documentos completos. Los documentos pueden ser digitales, es decir, creados, firmados y guardados en formato electrónico. Cada documento tiene un formato, una estructura fija de campos, y se presenta en una secuencia, un orden correcto. El principio de cero faltas es la meta de que ningún documento salga con errores u omisiones.",
        "Un error documental, como un número de contenedor mal digitado, puede hacer que el documento no coincida con la carga y que el despacho se retrase o se retenga, con costos para el cliente y el terminal. La documentación también lleva datos de personas y de empresas que son confidenciales: la clave de acceso es personal y no se comparte, porque quien firma responde por lo que se hace con su clave. Los archivos digitales se respaldan para poder recuperarlos.",
        f"El trabajo con pantallas exige pausas y buena postura. En el recinto portuario, quien camina entre vehículos no debe mirar el teléfono: es un riesgo de atropello. Las normas de documentación dependen de la norma vigente de la autoridad correspondiente. {EMER} {AVISO}",
    ],
    vocab=[("recepción", "proceso en que la carga que llega se recibe, se cuenta y se registra"), ("despacho", "entrega de la carga a quien la retira, con sus documentos completos"), ("documento digital", "documento creado, firmado y guardado en formato electrónico"), ("formato", "estructura fija de campos de un documento"), ("secuencia", "orden correcto en que se preparan los documentos"), ("cero faltas", "meta de que ningún documento salga con errores u omisiones"), ("confidencialidad", "obligación de no compartir datos que no son públicos"), ("respaldo", "copia de un archivo para poder recuperarlo")],
    worked=[
        ("Contar documentos", "Una oficina de ejemplo prepara 5 documentos por cada despacho y hace 12 despachos. ¿Cuántos documentos prepara?", ["Se multiplican los documentos por cada despacho por los despachos.", "5 por 12 son 60."], "60 documentos"),
        ("Clasificar un riesgo", "Una persona de ejemplo deja su computador con su sesión abierta y se va. ¿Qué riesgo hay?", ["Cualquiera podría usar su sesión y firmar documentos en su nombre.", "Es un riesgo de seguridad de la información."], "Que otra persona use su sesión y firme en su nombre"),
    ],
    mistakes=[("Creer que compartir la clave con un compañero de confianza no tiene consecuencias.", "Quien firma responde por lo hecho con su clave, aunque lo haya hecho otra persona.", "No compartas tu clave y avisa a la jefatura si alguien la pide."),
              ("Creer que un error pequeño en un número no importa.", "Puede hacer que el documento no coincida con la carga y retenga el despacho.", "Verifica cada dato contra el documento original.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la recepción de carga?", "El proceso en que la carga que llega se recibe, se cuenta y se registra contra sus documentos", "El envío de la carga a otro puerto", "El pago de los servicios del puerto", "La recepción registra lo que llega; enviar y pagar son otros procesos."),
        ("abc", "En Operaciones Portuarias: ¿qué es el despacho de carga?", "La entrega de la carga a quien la retira, con sus documentos completos", "La llegada de la carga a la bodega", "La descarga de la nave en el muelle", "El despacho es la salida de la carga hacia quien la retira."),
        ("abc", "En Operaciones Portuarias: ¿qué es un documento digital?", "Un documento creado, firmado y guardado en formato electrónico", "Una copia impresa de un documento escrito a mano", "Un documento que no necesita firma", "Lo digital es el formato electrónico; no exime de firma ni de datos."),
        ("abc", "{F} ¿Qué observación de la ficha corresponde a un riesgo de seguridad de la información?", "Compartir la clave de acceso con un compañero", "Revisar documentos en el teléfono mientras camina", "Contar los camiones recepcionados en el día", "Compartir la clave pone en riesgo la información y la responsabilidad de la firma."),
        ("abc", "{F} ¿Qué riesgo físico tiene revisar documentos en el teléfono mientras se camina entre vehículos?", "La distracción y el atropello por vehículos en movimiento", "Que se llene la memoria del teléfono", "Que se pierdan los documentos digitales", "Mirar el teléfono distrae y expone a ser atropellado."),
        ("abc", "{F} ¿Cuál es la consecuencia probable de digitar mal el número de un contenedor?", "Que el documento no coincida con la carga y el despacho se retrase o se retenga", "Que el contenedor cambie de lugar solo", "Ninguna, porque el número solo es decorativo", "El número identifica la carga; un error genera discrepancias."),
        ("=", "{F} ¿Cuántos documentos requieren las recepciones del día?", "48*3", "Se multiplican los camiones recepcionados por los documentos de cada recepción.", " documentos"),
        ("=", "{F} ¿Cuántos documentos requieren los despachos del día?", "30*4", "Se multiplican los despachos por los documentos de cada uno.", " documentos"),
        ("=", "{F} ¿Cuántos documentos hay que preparar en total en el día?", "48*3+30*4", "Se suman los documentos de las recepciones y los de los despachos.", " documentos"),
        ("abc", "Un compañero te pide tu clave «solo un momento» para firmar un documento. ¿Qué corresponde?", "No compartirla, porque la clave es personal, y avisar a la jefatura", "Compartirla, si es de confianza", "Compartirla y cambiarla después", "La clave es personal; quien firma responde por lo que se hace con ella."),
        ("abc", "En Operaciones Portuarias: ¿por qué conviene respaldar los documentos digitales?", "Porque si un archivo se pierde o se daña se puede recuperar y se puede demostrar lo ocurrido", "Porque el respaldo reemplaza la firma del documento", "Porque los archivos ocupan más espacio sin respaldo", "El respaldo permite recuperar y probar; no reemplaza la firma."),
        ("=", "{F} Si los documentos del día se reparten por igual entre las 6 personas, ¿cuántos documentos revisa cada una?", "(48*3+30*4)//6", "Se calcula el total de documentos y se divide entre las personas.", " documentos"),
        ("abc", "{F} Para reducir el riesgo de error al digitar los números de contenedor, ¿cuál medida es de nivel más efectivo?", "Que el sistema tome el número desde el documento original, sin digitarlo", "Pedir a cada persona que revise con más cuidado", "Poner un cartel que diga «digite sin errores»", "Eliminar la digitación manual quita el peligro de error; el cuidado y el cartel dependen de la persona."),
    ],
    ctx=("abc", "Una persona de la oficina de ejemplo te dice: «déjame tu usuario y clave de práctica para cerrar unos documentos rápido, yo respondo». ¿Qué respondes?", "Que no, porque la clave es personal y quien firma responde por lo que se hace con ella", "Que sí, porque ella responde", "Que sí, solo por hoy", "Compartir la clave rompe la confidencialidad y la responsabilidad de la firma."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es el despacho?", "La entrega de la carga a quien la retira, con documentos completos", "El despacho es la salida de la carga del terminal."),
        ("¿Qué exige el principio de cero faltas?", "Que ningún documento salga con errores u omisiones", "Es la meta de la documentación sin errores."),
        ("¿Qué se hace con la clave de acceso?", "No se comparte con nadie", "La clave es personal y responde por la firma."),
    ],
    op=("Una persona de la oficina de ejemplo revisa documentos en el computador durante todo el turno sin pausas, comparte su clave con un compañero y camina por el patio mirando el teléfono. Escribe (a) un riesgo de seguridad de la información y cómo se evita, (b) un riesgo físico del patio y cómo se evita, (c) una medida para cuidar el cuerpo ante el trabajo con pantalla, (d) por qué una clave no se comparte.",
        "(a) Riesgo: que otra persona firme en su nombre; se evita no compartiendo la clave y avisando a la jefatura. (b) Riesgo: atropello por distracción; se evita no mirando el teléfono al caminar entre vehículos y usando las rutas peatonales. (c) Hacer pausas y mantener una buena postura. (d) Porque quien firma responde por lo hecho con su clave, aunque lo haya hecho otra persona.",
        ["identifica el riesgo de seguridad de la información", "identifica el riesgo físico del patio", "propone pausas y postura", "explica por qué la clave es personal"],
        ["hoja con las cuatro respuestas"],
        ["decir que compartir la clave es aceptable entre amigos", "no mencionar el riesgo de atropello", "no proponer pausas"],
        "Pregunta: «¿quién responde por lo que se firma con una clave?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe tres datos de un documento portuario que son confidenciales y por qué no se comparten.",
    extend="Explica con un ejemplo cómo un error pequeño en un documento puede retrasar un despacho.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (documentos de despacho de ejemplo, inventados). Orden de retiro 77: retira «Importadora Ejemplo» (consignatario) los contenedores C1, C2 y C3. Conocimiento de embarque CE-3001: consignatario «Importadora Ejemplo»; 3 contenedores (C1, C2 y C3); 270 bultos; 8.100 kg. "
     "Guía de despacho 0912: lleva el contenedor C1 (90 bultos, 2.700 kg) en un camión de la empresa «Transportes Demo». En este caso de ejemplo, los campos obligatorios de la guía de despacho son: número de contenedor, bultos, peso, consignatario, empresa de transporte y firma de quien retira. "
     "La guía 0912 no trae la firma de quien retira.")
build(
    O5, 2, F,
    use="Aprenderé qué documentos intervienen en la recepción y el despacho, qué es un campo obligatorio y qué roles participan, y a revisar que un documento esté completo.",
    prior=["Sé qué es un conocimiento de embarque y un consignatario.", "Sé multiplicar y dividir números enteros.", "Sé qué es el despacho."],
    explain=[
        "En el despacho intervienen varios documentos. La factura comercial detalla lo que se vendió y su valor. La lista de embalaje detalla el contenido y el peso de los bultos. El conocimiento de embarque acredita el transporte. La orden de retiro autoriza a un consignatario a retirar la carga. La guía de despacho acompaña a la carga cuando sale en un camión y debe tener todos sus campos obligatorios, los datos que siempre deben estar escritos. Según el tipo de carga pueden exigirse además certificados.",
        "Cada rol cumple una función: el consignatario retira la carga que le corresponde; el transportista la lleva en su camión; el despachador de la oficina prepara y revisa los documentos; el agente de aduanas realiza los trámites con la aduana cuando corresponde. Un documento se da por completo solo si todos sus campos obligatorios están escritos y coinciden con los demás documentos; si falta uno, no se entrega la carga y se informa a quien corresponde.",
        f"Los campos obligatorios de esta clase son de ejemplo; los reales dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("orden de retiro", "documento que autoriza a un consignatario a retirar la carga"), ("guía de despacho", "documento que acompaña a la carga cuando sale en un camión"), ("factura comercial", "documento que detalla lo que se vendió y su valor"), ("campo obligatorio", "dato que siempre debe estar escrito en un documento"), ("transportista", "empresa o persona que lleva la carga en su camión"), ("despachador", "persona de la oficina que prepara y revisa los documentos de salida")],
    worked=[
        ("Revisar un campo", "Una guía de ejemplo tiene número de contenedor, bultos, peso y consignatario, pero no tiene firma. Si la firma es obligatoria, ¿está completa?", ["Se comparan los campos escritos con los obligatorios.", "Falta la firma, que es obligatoria."], "No está completa: falta la firma"),
        ("Peso por bulto", "Un contenedor de ejemplo lleva 50 bultos y 1.500 kg. ¿Cuántos kg pesa en promedio cada bulto?", ["Se divide el peso entre los bultos.", "1.500 dividido en 50 son 30."], "30 kg"),
    ],
    mistakes=[("Entregar la carga porque «la orden de retiro ya la autoriza», aunque la guía esté incompleta.", "Cada documento cumple una función y todos deben estar completos.", "Revisa también la guía antes de entregar."),
              ("Completar a mano un campo que no se conoce.", "Se inventa un dato y se pierde la trazabilidad.", "Si falta un dato, se informa y se pide a quien corresponde.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la orden de retiro?", "El documento que autoriza a un consignatario a retirar la carga", "El documento que acompaña a la carga cuando sale en un camión", "El documento que detalla el valor de lo vendido", "La orden de retiro autoriza; la guía acompaña y la factura detalla el valor."),
        ("abc", "En Operaciones Portuarias: ¿qué es la guía de despacho?", "El documento que acompaña a la carga cuando sale en un camión", "El documento que acredita que el transportista recibió la carga en origen", "La lista de bultos de una nave", "La guía acompaña a la carga en su salida; el conocimiento acredita el transporte."),
        ("abc", "En Operaciones Portuarias: ¿qué es un campo obligatorio de un documento?", "Un dato que siempre debe estar escrito", "Un dato que se puede omitir si el cliente lo pide", "Un dato que solo se escribe a mano", "Un campo obligatorio no se puede dejar en blanco."),
        ("abc", "{F} ¿Qué documento de la ficha autoriza el retiro de los contenedores?", "La orden de retiro", "La guía de despacho", "El conocimiento de embarque", "La orden de retiro es la que autoriza al consignatario."),
        ("abc", "{F} ¿Qué campo obligatorio falta en la guía de despacho de la ficha?", "La firma de quien retira", "El número de contenedor", "La empresa de transporte", "La ficha indica que la guía no trae la firma."),
        ("=", "{F} ¿Cuántos kilogramos pesa en promedio cada bulto del conocimiento de embarque?", "8100//270", "Se divide el peso total entre los bultos.", " kg"),
        ("=", "{F} Después de despachar el contenedor C1, ¿cuántos bultos quedan por despachar?", "270-90", "Se restan a los bultos del conocimiento los de la guía de C1.", " bultos"),
        ("=", "{F} Después de despachar el contenedor C1, ¿cuántos kilogramos quedan por despachar?", "8100-2700", "Se restan a los kilogramos del conocimiento los de la guía de C1.", " kg"),
        ("abc", "{F} ¿Puede darse por completa la guía de despacho 0912?", "No, porque falta un campo obligatorio, la firma de quien retira", "Sí, porque los bultos y el peso coinciden", "Sí, porque el conocimiento la respalda", "Un documento con un campo obligatorio faltante no está completo, aunque otros datos coincidan."),
        ("abc", "En Operaciones Portuarias: ¿por qué debe coincidir el consignatario de la orden de retiro con el del conocimiento?", "Para que la carga se entregue solo a quien tiene derecho a retirarla", "Para que el camión tenga el nombre correcto", "Para que el peso se calcule bien", "El consignatario identifica a quien puede retirar la carga."),
        ("=", "{F} Los contenedores se despachan de a uno, cada 45 minutos. ¿Cuántos minutos toma despachar los tres?", "3*45", "Se multiplica el número de contenedores por el tiempo de cada despacho.", " minutos"),
        ("abc", "{F} Un transportista pide llevarse C2 y C3 sin guías «porque ya tiene la 0912». ¿Qué corresponde?", "No entregar: cada contenedor requiere su guía completa y firmada", "Entregar, porque la orden de retiro lo autoriza", "Entregar, si firma después", "La orden autoriza el retiro, pero cada salida necesita su guía completa."),
        ("abc", "{F} Un despachador completa el campo faltante con una firma que él mismo dibuja «para agilizar». ¿Qué respuesta es correcta?", "Es falso: se falsifica un documento y se debe informar la falta a quien corresponde", "Es cierto: es una forma de agilizar", "Es cierto, si el consignatario no se entera", "Completar un campo con datos falsos es una falta grave."),
    ],
    ctx=("abc", "Un transportista de ejemplo te dice: «ya firmé la guía en mi camión, solo falta que me la des para entregar la carga sin que revises nada más». ¿Qué respondes?", "Que la guía se revisa completa antes de entregar la carga y que, si falta un campo, se informa", "Que se la das, porque ya firmó", "Que se la das y revisas después", "Un documento incompleto no autoriza la entrega de la carga."),
    sc=[
        ("En Operaciones Portuarias: ¿qué documento autoriza el retiro de la carga?", "La orden de retiro", "Autoriza al consignatario a retirar la carga que le corresponde."),
        ("¿Qué es un campo obligatorio?", "Un dato que siempre debe estar escrito", "No se puede dejar en blanco."),
        ("¿Qué se hace si falta un campo obligatorio?", "No se entrega la carga y se informa a quien corresponde", "El documento incompleto no se acepta."),
    ],
    op=("Documentos de ejemplo. Orden de retiro 12: retira «Comercial Demo» los contenedores D1 y D2. Conocimiento de embarque CE-4001: 2 contenedores (D1 y D2), 160 bultos, 4.800 kg. Guía de despacho 0450: contenedor D1, 80 bultos, 2.400 kg, con consignatario y transportista, pero sin firma de quien retira (campo obligatorio). Escribe (a) qué documento autoriza el retiro, (b) cuántos kilogramos pesa en promedio un bulto, (c) qué falta en la guía, (d) cuántos bultos quedan por despachar después de D1.",
        "(a) La orden de retiro. (b) 4.800 ÷ 160 = 30 kg. (c) La firma de quien retira, que es un campo obligatorio; la guía no está completa y se informa. (d) 160 − 80 = 80 bultos.",
        ["identifica la orden de retiro", "calcula el peso promedio", "identifica el campo faltante", "calcula los bultos restantes"],
        ["hoja con las cuatro respuestas"],
        ["dar por completa la guía sin firma", "dividir al revés", "restar mal los bultos"],
        "Pregunta: «¿qué campo obligatorio no está escrito?». Si no responde, pídele que compare los campos de la guía con los obligatorios."),
    reinforce="Inventa una guía con seis campos obligatorios y marca cuál falta en un ejemplo incompleto.",
    extend="Explica con un ejemplo la diferencia entre la orden de retiro y la guía de despacho.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (documentos de ejemplo, inventados). Conocimiento de embarque CE-5120: consignatario «Comercial Ejemplo»; contenedor ABCD 111111 1; 200 bultos; 5.000 kg; precinto 0331. "
     "Lista de embalaje: caja tipo 1, 120 unidades de 20 kg cada una; caja tipo 2, 80 unidades de 35 kg cada una. "
     "Guía de recepción: contenedor ABCD 111111 1; 198 bultos recibidos; precinto verificado 0331; consignatario «Comercial Ejemplos».")
build(
    O5, 3, F,
    use="Aprenderé a verificar un conjunto de documentos comparando sus datos, a detectar discrepancias y a decidir qué se hace con ellas.",
    prior=["Sé qué es un faltante y un campo obligatorio.", "Sé multiplicar y restar números enteros.", "Sé qué es un precinto."],
    explain=[
        "Verificar la documentación es comparar los datos de cada documento con los demás y con la carga real. A esta comparación se le llama verificación cruzada: se revisa que el número de contenedor, el precinto, los bultos, el peso y el nombre del consignatario coincidan en todos los documentos. Una discrepancia es una diferencia entre dos datos que deberían ser iguales. Puede ser un faltante o un sobrante de bultos, una diferencia de peso o un error de transcripción, que es un dato mal copiado, como una letra de más.",
        "Las discrepancias no se corrigen a mano. Se registran por escrito y se informan a quien emitió el documento, que es quien puede corregirlo. Hasta entonces el documento no se aprueba, porque rige el principio de cero faltas. Para el peso de una lista de embalaje se multiplica cada tipo de caja por su peso unitario y se suman los resultados.",
        f"Los datos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("verificación cruzada", "comparar un mismo dato entre varios documentos y con la carga"), ("discrepancia", "diferencia entre dos datos que deberían ser iguales"), ("error de transcripción", "dato mal copiado, como una letra o un número cambiado"), ("faltante", "menos bultos que los declarados"), ("emisor", "quien emitió el documento y puede corregirlo")],
    worked=[
        ("Peso de una lista", "Una lista de ejemplo trae 10 cajas de 30 kg y 20 cajas de 15 kg. ¿Cuántos kg pesa en total?", ["10 por 30 son 300 kg y 20 por 15 son 300 kg.", "300 más 300 son 600."], "600 kg"),
        ("Detectar una discrepancia", "Un conocimiento de ejemplo dice 80 bultos y la guía de recepción dice 78. ¿Qué hay?", ["La guía tiene 2 bultos menos que lo declarado.", "Menos bultos que los declarados es un faltante."], "Un faltante de 2 bultos"),
    ],
    mistakes=[("Corregir a mano una discrepancia para que los documentos cuadren.", "Solo el emisor puede corregir su documento y la diferencia debe quedar registrada.", "Registra la discrepancia e informa al emisor."),
              ("Comparar solo los bultos y olvidar el peso, el precinto y los nombres.", "Un error puede estar en cualquiera de los datos.", "Compara cada dato de la lista de verificación.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es una discrepancia entre documentos?", "Una diferencia entre dos datos que deberían ser iguales", "Una firma que aparece en dos documentos", "Un documento que se entrega dos veces", "La discrepancia es una diferencia entre datos que deben coincidir."),
        ("abc", "En Operaciones Portuarias: ¿qué es una verificación cruzada?", "Comparar un mismo dato entre varios documentos y con la carga", "Firmar un documento dos veces", "Imprimir una copia del documento en otro color", "La verificación cruzada contrasta los datos entre sí."),
        ("abc", "En Operaciones Portuarias: ¿qué es un error de transcripción?", "Un dato mal copiado, como una letra o un número cambiado", "Un documento que no se firmó", "Un documento que llegó tarde", "El error de transcripción ocurre al copiar un dato."),
        ("abc", "{F} ¿Qué datos coinciden entre el conocimiento y la guía de recepción?", "El número de contenedor y el precinto", "Los bultos y el nombre del consignatario", "El peso y los bultos", "El contenedor y el precinto son iguales; los bultos y el nombre difieren."),
        ("=", "{F} ¿Cuántos kilogramos pesa la carga según la lista de embalaje?", "120*20+80*35", "Se multiplica cada tipo de caja por su peso y se suman los resultados.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos más declara la lista de embalaje que el conocimiento de embarque?", "(120*20+80*35)-5000", "Se resta el peso del conocimiento al peso calculado con la lista.", " kg"),
        ("=", "{F} ¿Cuántos bultos faltan según la guía de recepción respecto del conocimiento?", "200-198", "Se restan los bultos recibidos a los declarados.", " bultos"),
        ("abc", "{F} ¿Qué tipo de error es la diferencia de una letra en el nombre del consignatario?", "Un error de transcripción", "Un faltante", "Un sobrante", "Cambiar una letra al copiar un nombre es un error de transcripción."),
        ("=", "{F} ¿Cuántos kilogramos pesan las cajas tipo 2 de la lista?", "80*35", "Se multiplican las unidades de tipo 2 por su peso unitario.", " kg"),
        ("abc", "{F} ¿Puede aceptarse la guía de recepción tal como está?", "No, porque hay discrepancias que deben registrarse e informarse antes de aprobarla", "Sí, porque el precinto coincide", "Sí, porque la diferencia es de solo 2 bultos", "Con discrepancias abiertas no se aprueba, por el principio de cero faltas."),
        ("abc", "En Operaciones Portuarias: ¿quién corrige el peso de un conocimiento de embarque que tiene un error?", "Quien lo emitió, después de ser informado", "El recepcionista, si tiene la lista de embalaje", "El camionero que trae la carga", "Solo el emisor corrige su documento."),
        ("=", "{F} ¿Qué porcentaje de los bultos declarados se recibió?", "198*100//200", "Se divide los bultos recibidos entre los declarados y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cuántas discrepancias hay en total entre los tres documentos?", "3: bultos, peso y nombre del consignatario", "2: solo bultos y peso", "1: solo los bultos", "Los bultos, el peso y el nombre no coinciden; contenedor y precinto sí."),
    ],
    ctx=("abc", "Un compañero de práctica dice: «son solo 2 bultos de diferencia, anota 200 en la guía de recepción y listo». ¿Qué le respondes?", "Que se anota lo contado, el faltante se registra y se informa al emisor", "Que tiene razón, porque la diferencia es pequeña", "Que anotes 200 y después se arregla", "Anotar un dato que no es real oculta un faltante."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el peso de una lista de embalaje?", "Multiplicando cada tipo de caja por su peso y sumando", "Se suman los pesos de todos los tipos de caja."),
        ("¿Qué se hace con una discrepancia?", "Se registra y se informa al emisor", "No se corrige a mano para que cuadre."),
        ("En el puerto: ¿qué es un faltante?", "Menos bultos que los declarados", "Es una diferencia por defecto respecto de lo declarado."),
    ],
    op=("Documentos de ejemplo. Conocimiento CE-6002: 150 bultos; 3.000 kg; precinto 0777. Lista de embalaje: caja tipo 1, 100 unidades de 15 kg; caja tipo 2, 50 unidades de 20 kg. Guía de recepción: 150 bultos; precinto verificado 0771. Escribe (a) el peso de la lista de embalaje, (b) la diferencia de peso con el conocimiento, (c) otra discrepancia que observes, (d) qué se hace con las discrepancias.",
        "(a) 100 × 15 + 50 × 20 = 1.500 + 1.000 = 2.500 kg. (b) 3.000 − 2.500 = 500 kg de diferencia. (c) El precinto: el conocimiento dice 0777 y la guía dice 0771. (d) Se registran por escrito y se informan al emisor; los documentos no se corrigen a mano ni se aprueban hasta resolverlas.",
        ["calcula el peso de la lista", "calcula la diferencia", "detecta la discrepancia del precinto", "indica registrar e informar"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por las unidades", "no revisar el precinto", "corregir a mano"],
        "Pregunta: «¿coinciden los precintos?». Si no responde, pídele que compare los dos números."),
    reinforce="Inventa dos documentos con tres datos iguales y dos distintos, y señala las discrepancias.",
    extend="Explica con un ejemplo por qué es importante informar al emisor y no corregir el documento por cuenta propia.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado). En un turno de «Terminal Demo» se revisaron 120 documentos y 6 tenían errores que se detectaron cuando ya habían salido de la oficina. Cada documento con error requiere 30 minutos de corrección (valor de ejemplo). "
     "La carga asociada a un documento con error queda retenida 2 días y paga $20.000 por día de espera (valor de ejemplo). La meta de la oficina es cero faltas.")
build(
    O5, 4, F,
    use="Aprenderé a calcular la tasa de error, el tiempo y el costo de corregir errores documentales y a decidir si conviene prevenirlos con una revisión previa.",
    prior=["Sé calcular porcentajes sencillos.", "Sé qué es una verificación cruzada.", "Sé qué es el principio de cero faltas."],
    explain=[
        "La tasa de error es el porcentaje de documentos con errores respecto del total revisado. Los documentos sin error son el total menos los que tuvieron errores. Corregir un error cuesta tiempo de personal y, si la carga queda retenida, también cuesta por cada día de espera; a ese gasto por corregir o repetir trabajo se le llama costo de retrabajo. El principio de cero faltas se cumple cuando ningún documento sale con errores; si el error se detecta después de enviado, la meta no se cumplió.",
        "Prevenir un error es más barato que corregirlo, porque evita el retraso, el costo y el riesgo de dejar la carga retenida. Una revisión previa, hecha antes de enviar el documento, toma tiempo pero puede evitar los errores. Para decidir se comparan el tiempo y el costo de prevenir con el tiempo y el costo de corregir. Los errores siempre se registran con honestidad: ocultarlos impide corregir sus causas.",
        f"Todos los datos de tiempo y costo de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("tasa de error", "porcentaje de documentos con errores respecto del total revisado"), ("retrabajo", "trabajo que hay que repetir o corregir por un error"), ("verificación cruzada", "comparar un dato entre varios documentos"), ("revisión previa", "revisión hecha antes de enviar un documento"), ("retención de carga", "carga detenida por un problema documental")],
    worked=[
        ("Tasa de error", "En un turno de ejemplo se revisaron 50 documentos y 5 tenían error. ¿Cuál es la tasa de error?", ["5 de 50 son 10 de cada 100.", "La tasa de error se expresa en porcentaje."], "10 %"),
        ("Costo de retención", "Una carga de ejemplo queda retenida 3 días a $10.000 por día. ¿Cuánto paga?", ["Se multiplican los días por el costo diario.", "3 por 10.000 son 30.000."], "$30.000"),
    ],
    mistakes=[("Calcular la tasa de error dividiendo entre los documentos con error en vez de entre el total.", "La tasa compara los errores con todos los documentos revisados.", "Divide los documentos con error entre el total."),
              ("Creer que se cumple cero faltas si los errores se corrigen después.", "Cero faltas significa que ningún documento sale con errores.", "Revisa antes de enviar.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la tasa de error de un grupo de documentos?", "El porcentaje de documentos con errores respecto del total revisado", "El número de documentos revisados por hora", "El tiempo promedio que demora firmar un documento", "La tasa compara los documentos con error con el total."),
        ("abc", "En Operaciones Portuarias: ¿qué es el retrabajo?", "El trabajo que hay que repetir o corregir por un error", "El trabajo extra que se hace por gusto", "El trabajo de preparar un documento por primera vez", "El retrabajo nace de un error y se suma al costo."),
        ("abc", "En Operaciones Portuarias: ¿qué es una verificación cruzada?", "Comparar un dato entre dos o más documentos distintos", "Firmar un documento con dos firmas", "Revisar solo el primer documento de cada lote", "La verificación cruzada contrasta datos entre documentos."),
        ("=", "{F} ¿Cuántos documentos del turno no tuvieron error?", "120-6", "Se resta al total los documentos con error.", " documentos"),
        ("=", "{F} ¿Qué porcentaje de los documentos tuvo error?", "6*100//120", "Se divide los documentos con error entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas horas de corrección requieren todos los documentos con error?", "6*30//60", "Se multiplican los documentos por los minutos de corrección y se pasan a horas.", " horas"),
        ("=", "{F} ¿Cuántos pesos paga por espera la carga asociada a los documentos con error?", "6*20000*2", "Se multiplican los documentos, el costo por día y los días de retención.", " pesos"),
        ("=", "{F} Si los errores bajan de 6 a 2 por turno, ¿cuántos pesos menos se pagan por espera?", "(6-2)*20000*2", "Se calcula la espera evitada por los 4 documentos que ya no tendrían error.", " pesos"),
        ("abc", "{F} ¿Cumple el turno la meta de cero faltas?", "No, porque 6 documentos tuvieron errores detectados después de salir", "Sí, porque el 95 % de los documentos estuvo correcto", "Sí, porque los errores se corrigieron después", "Cero faltas exige que ningún documento salga con errores."),
        ("abc", "En Operaciones Portuarias: ¿por qué es mejor prevenir un error documental que corregirlo?", "Porque prevenir evita el retraso, el costo y el riesgo de la carga retenida", "Porque corregir siempre es imposible", "Porque prevenir elimina la necesidad de firmar", "Prevenir evita los costos y retrasos que trae el error."),
        ("abc", "{F} Un jefe propone no registrar los errores «para que la tasa se vea mejor». ¿Qué respuesta es correcta?", "Es falso: ocultar errores impide corregir sus causas y es una falta de honestidad", "Es cierto, si baja el número de reclamos", "Es cierto solo en meses de mucho trabajo", "Los errores se registran para poder corregir las causas."),
        ("=", "{F} Una revisión previa de 2 minutos por documento evitaría todos los errores. ¿Cuántas horas más que las de corrección tomaría revisar los 120 documentos?", "120*2//60-6*30//60", "Se calculan las horas de la revisión previa y se restan las de corrección.", " hora"),
        ("abc", "{F} La revisión previa tomaría 1 hora más que corregir, pero evitaría la espera de la carga. ¿Qué conviene?", "La revisión previa, porque evita el costo de espera y los retrasos aunque tome una hora más", "Ninguna, porque toma más horas", "Corregir después, porque toma menos horas", "El costo de espera de la carga es mayor que la hora adicional."),
    ],
    ctx=("abc", "En una práctica de ejemplo, una persona dice: «si un documento tiene error, lo corregimos y no lo anotamos; así nadie nos reclama». ¿Qué respondes?", "Que el error se registra, porque así se descubren y se corrigen sus causas", "Que tiene razón, porque evita reclamos", "Que se anota solo si es grave", "Sin registro no se pueden prevenir los mismos errores."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula la tasa de error?", "Documentos con error entre el total, por 100", "Es un porcentaje respecto del total revisado."),
        ("¿Qué exige cero faltas?", "Que ningún documento salga con errores", "Un error detectado después de enviado incumple la meta."),
        ("¿Por qué conviene prevenir los errores?", "Porque evita el retraso y el costo de corregir", "Corregir cuesta tiempo y puede retener la carga."),
    ],
    op=("En un turno de ejemplo se revisaron 200 documentos y 12 tenían errores detectados cuando ya habían salido. Cada corrección toma 25 minutos. La carga de cada documento con error queda retenida 3 días a $15.000 por día. Escribe (a) qué porcentaje de documentos no tuvo error, (b) cuántas horas de corrección se necesitan en total, (c) cuántos pesos se pagan por la espera, (d) si se cumplió cero faltas y por qué.",
        "(a) Sin error: 200 − 12 = 188; 188 ÷ 200 × 100 = 94 %. (b) 12 × 25 = 300 minutos, que son 5 horas. (c) 12 × 15.000 × 3 = $540.000. (d) No: 12 documentos salieron con errores y cero faltas exige que ninguno salga con errores.",
        ["calcula el porcentaje sin error", "calcula las horas de corrección", "calcula el costo de espera", "concluye que no se cumplió cero faltas"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre los documentos con error", "no pasar minutos a horas", "olvidar multiplicar por los días"],
        "Pregunta: «¿salió algún documento con error?». Si no responde, pídele que relea la definición de cero faltas."),
    reinforce="Inventa un turno con un total de documentos y de errores y calcula la tasa de error.",
    extend="Explica con un ejemplo por qué una revisión previa puede costar menos que corregir después.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Hay que preparar 240 documentos en un día. Alternativa M: una persona digita y revisa sola; hace 40 documentos por hora; el mes pasado tuvo 12 documentos con error de 240. "
     "Alternativa D: una persona digita y otra revisa (doble revisión); entre las dos hacen 30 documentos por hora; el mes pasado tuvo 2 documentos con error de 240. Costo de ejemplo: $6.000 por persona por hora; $8.000 por cada documento con error. "
     "Secuencia de ejemplo de los documentos de un despacho: 1) factura comercial, 2) lista de embalaje, 3) conocimiento de embarque, 4) orden de retiro, 5) guía de despacho.")
build(
    O5, 5, F,
    use="Aprenderé a comparar alternativas de trabajo documental por tiempo, costo y errores, a respetar la secuencia y el formato de los documentos y a aplicar una lista de verificación con cero faltas.",
    prior=["Sé calcular horas, costos y tasas de error.", "Sé qué es una verificación cruzada.", "Sé qué es la secuencia documental."],
    explain=[
        "Para elegir cómo preparar los documentos se comparan alternativas por tiempo, costo y errores. El tiempo es la cantidad de documentos dividida entre el rendimiento por hora. El costo total suma el costo del personal, que es personas por costo por hora por horas, y el costo de los errores, que es la cantidad de documentos con error por el costo de cada uno. Una doble revisión usa a una segunda persona para revisar lo que digitó la primera: tarda más y cuesta más en personal, pero suele reducir los errores.",
        "La secuencia documental es el orden correcto en que se preparan y presentan los documentos: cada uno respalda al siguiente, así que no se altera para adelantar trabajo. Además, cada documento debe respetar su formato, es decir, la estructura fija de campos. Una lista de verificación final comprueba formato, secuencia, campos obligatorios y coincidencia de datos antes de cerrar, con la meta de cero faltas.",
        f"Todos los costos y los rendimientos son de ejemplo. Las exigencias reales dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("doble revisión", "revisión de un documento por una segunda persona distinta de quien lo digitó"), ("secuencia documental", "orden correcto en que se preparan y presentan los documentos"), ("formato", "estructura fija de campos de un documento"), ("costo de personal", "personas por costo por hora por horas"), ("costo de errores", "documentos con error por el costo de cada uno")],
    worked=[
        ("Costo total", "Una alternativa de ejemplo usa 2 personas durante 5 horas a $4.000 por persona por hora y tiene 3 documentos con error a $5.000 cada uno. ¿Cuál es su costo total?", ["El personal cuesta 2 por 4.000 por 5, o sea 40.000.", "Los errores cuestan 3 por 5.000, o sea 15.000. En total, 55.000."], "$55.000"),
        ("Respetar la secuencia", "En una secuencia de ejemplo, el documento 3 respalda al 4. ¿Se puede presentar el 4 antes que el 3?", ["Cada documento respalda al siguiente.", "Si el 4 va antes, queda sin su respaldo."], "No: se respeta la secuencia"),
    ],
    mistakes=[("Elegir la alternativa más rápida sin sumar el costo de sus errores.", "Los errores pueden costar más que el tiempo ahorrado.", "Suma el costo del personal y el costo de los errores."),
              ("Alterar la secuencia de los documentos para adelantar trabajo.", "Cada documento respalda al siguiente y se pueden generar discrepancias.", "Respeta el orden de la secuencia.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la secuencia documental?", "El orden correcto en que se preparan y presentan los documentos", "El número de páginas de un documento", "La hora en que se firma cada documento", "La secuencia es el orden de los documentos."),
        ("abc", "En Operaciones Portuarias: ¿qué es una doble revisión?", "Que una segunda persona revisa lo que digitó la primera", "Que el documento se imprime dos veces", "Que la misma persona lo revisa dos veces seguidas", "La doble revisión incorpora a una segunda persona."),
        ("abc", "En Operaciones Portuarias: ¿qué es el formato de un documento?", "La estructura fija de campos que debe tener", "El tamaño del papel en que se imprime", "El idioma en que se escribe", "El formato fija qué campos tiene el documento."),
        ("=", "{F} ¿Cuántas horas tarda la alternativa M en preparar los 240 documentos?", "240//40", "Se divide el total de documentos entre el rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántas horas tarda la alternativa D?", "240//30", "Se divide el total de documentos entre el rendimiento conjunto por hora.", " horas"),
        ("abc", "{F} ¿Qué documento va primero en la secuencia de ejemplo?", "La factura comercial", "La guía de despacho", "La orden de retiro", "La secuencia empieza por la factura comercial."),
        ("=", "{F} ¿Cuántos pesos cuesta el personal de la alternativa M?", "1*6000*(240//40)", "Se multiplican las personas por el costo por hora y por las horas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan los errores de la alternativa M?", "12*8000", "Se multiplican los documentos con error por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta en total la alternativa D, sumando personal y errores?", "2*6000*(240//30)+2*8000", "Se suman el costo del personal de las dos personas y el de los errores.", " pesos"),
        ("abc", "{F} ¿Qué alternativa conviene si no hay plazo exigido?", "La D, porque cuesta menos en total y tiene menos errores", "La M, porque es más rápida", "Ninguna, porque cuestan lo mismo", "La alternativa D cuesta menos en total que la M."),
        ("abc", "{F} Si el plazo fuera de 7 horas, ¿qué corresponde?", "Solo la M cumple el plazo, aunque con más errores; se informa el riesgo y se refuerza su revisión", "Solo la D cumple el plazo, porque tiene menos errores", "Ninguna cumple el plazo", "La D necesita 8 horas y la M, 6; conviene advertir el mayor riesgo de errores de la M."),
        ("=", "{F} Si el mes siguiente se preparan 480 documentos con la misma tasa de errores de la alternativa M, ¿cuántos documentos con error se esperan?", "480//240*12", "Se calcula cuántas veces se repite el mes de 240 documentos y se multiplica por los errores.", " documentos"),
        ("abc", "{F} Un compañero propone presentar la guía de despacho antes que la orden de retiro «para adelantar». ¿Qué respuesta es correcta?", "Es falso: se respeta la secuencia porque cada documento respalda al siguiente", "Es cierto: el orden no importa", "Es cierto, si el cliente espera", "Alterar el orden puede dejar un documento sin su respaldo."),
    ],
    ctx=("abc", "Al cerrar un lote de ejemplo, un punto de la lista de verificación dice «formato correcto» y nadie lo ha revisado. Alguien dice: «márcalo, seguro está bien». ¿Qué respondes?", "Que primero se revisa el formato y solo entonces se marca el punto", "Que lo marcas, porque seguro está bien", "Que lo marcas y lo revisas la próxima semana", "Marcar sin revisar falsea la lista y puede dejar pasar errores."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el costo total de una alternativa documental?", "Sumando el costo del personal y el costo de los errores", "Ambos costos forman el costo total."),
        ("¿Qué es la doble revisión?", "Que una segunda persona revisa lo que digitó la primera", "Reduce la probabilidad de errores al revisar con otra persona."),
        ("¿Se puede alterar la secuencia de los documentos?", "No, porque cada documento respalda al siguiente", "El orden mantiene la coherencia entre los documentos."),
    ],
    op=("Hay que preparar 180 documentos. Alternativa P: una persona, 30 documentos por hora; el mes pasado tuvo 9 documentos con error de 180. Alternativa Q: dos personas, 20 documentos por hora entre las dos; el mes pasado tuvo 1 documento con error de 180. Costo de ejemplo: $5.000 por persona por hora y $6.000 por cada documento con error. El plazo es de 8 horas. Escribe (a) las horas de cada alternativa, (b) el costo total de P, (c) el costo total de Q, (d) qué alternativa cumple el plazo y qué advertir.",
        "(a) P: 180 ÷ 30 = 6 horas. Q: 180 ÷ 20 = 9 horas. (b) P: 1 × 5.000 × 6 + 9 × 6.000 = 30.000 + 54.000 = $84.000. (c) Q: 2 × 5.000 × 9 + 1 × 6.000 = 90.000 + 6.000 = $96.000. (d) Solo P cumple el plazo de 8 horas, pero tiene más errores; se advierte el riesgo y se refuerza su revisión.",
        ["calcula las horas de cada alternativa", "calcula el costo de P", "calcula el costo de Q", "elige según el plazo y advierte el riesgo de errores"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo de los errores", "olvidar multiplicar por las personas", "no comparar con el plazo"],
        "Pregunta: «¿qué alternativa tarda menos de 8 horas?». Si no responde, pídele que compare sus horas con el plazo."),
    reinforce="Inventa dos alternativas de trabajo documental y calcula sus horas y su costo total.",
    extend="Explica con un ejemplo por qué una alternativa más cara en personal puede salir más barata en total.",
)

"""Administración, mención Recursos Humanos, 4.º medio TP: OAM-01 (llenado y tramitación de contratos, remuneraciones y finiquito) y OAM-02 (cálculo de remuneraciones y finiquitos). Personas, empresas y cifras inventadas; todos los porcentajes y montos son de ejemplo; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, contratos, liquidaciones y finiquitos están escritos en cada ejercicio: las empresas y las personas son inventadas y los montos, los días y los porcentajes son «de ejemplo»: "
             "no son las tasas, los plazos ni los valores reales de la ley. Los derechos y obligaciones laborales, las cotizaciones, los impuestos y los plazos se consultan siempre en el Código del Trabajo y la norma vigente, y con tu docente de la especialidad. "
             "Los datos personales de las trabajadoras y los trabajadores son reservados: en este cuaderno solo se usan nombres ficticios y nunca debes usar datos reales de personas. Este cuaderno no entrega asesoría legal ni laboral personal; ante un caso real se consulta a la Dirección del Trabajo o a un profesional.")

build = make_build(MATERIALS)

O1 = "TP-ADRH-4-OAM-01"
O2 = "TP-ADRH-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 47 (caso ficticio). «Servicios Quillay Ltda.» contrata a Marcela Soto (nombre ficticio) como asistente administrativa. Datos de ejemplo del borrador de contrato: cargo, asistente administrativa; lugar de trabajo, oficina central; "
     "jornada de ejemplo, 40 horas semanales (la jornada máxima la fija la norma vigente); remuneración base de ejemplo, $600.000 mensuales; inicio, 1 de marzo; duración, indefinida. Documentos que acompañan el caso: documento de identificación y certificado de estudios (ficticios).")
build(
    O1, 1, F,
    use="Aprenderé qué es un contrato de trabajo, qué significa llenarlo y tramitarlo, cómo se relaciona con las remuneraciones, el finiquito y la contabilidad, y qué cuidados éticos y de privacidad exige.",
    prior=["Sé qué es una remuneración.", "Sé leer un documento con campos.", "Sé que los datos personales son reservados."],
    explain=[
        "El contrato de trabajo es el acuerdo escrito entre un empleador y una persona trabajadora. Llenarlo es completar con datos correctos lo que debe contener: quiénes son las partes, el cargo, el lugar de trabajo, la remuneración, la jornada, la duración y la fecha de inicio. Tramitarlo es hacer los pasos para dejarlo vigente: revisarlo, firmarlo por ambas partes, entregar una copia y archivarlo con reserva. Qué debe contener y en qué plazos se tramita lo establecen el Código del Trabajo y la norma vigente; aquí no se enseñan plazos ni cifras legales.",
        "El contrato se relaciona con otros documentos. La liquidación de remuneraciones muestra cada mes lo que se paga y se descuenta. El finiquito deja constancia de los pagos cuando la relación laboral termina. Las normas internacionales de contabilidad (NIC) orientan cómo se reconocen y presentan en la contabilidad los pagos al personal, por eso las cifras de estos documentos deben ser exactas.",
        "El trabajo en Recursos Humanos exige ética. Los datos personales se piden solo si tienen relación con el cargo, se guardan con reserva y no se difunden. No se discrimina por motivos personales al contratar. Todo lo acordado debe quedar por escrito, porque un acuerdo solo hablado no protege a ninguna de las partes.",
    ],
    vocab=[("contrato de trabajo", "acuerdo escrito entre empleador y trabajador"), ("empleador", "persona o empresa que contrata"), ("remuneración", "pago por el trabajo realizado"), ("jornada", "tiempo de trabajo pactado"), ("tramitar", "hacer los pasos para dejar un documento vigente"), ("dato personal", "información que identifica a una persona y es reservada")],
    worked=[
        ("Identificar las partes", "Un contrato ficticio dice: «Taller Pino Ltda. contrata a Luis Mora como bodeguero». ¿Quién es el empleador y quién el trabajador?", ["El empleador es quien contrata.", "El trabajador es quien presta el servicio."], "Empleador: Taller Pino Ltda.; trabajador: Luis Mora"),
        ("Dato innecesario", "Al contratar a un bodeguero ficticio, ¿corresponde pedir su religión?", ["No tiene relación con el cargo.", "Se piden solo datos relacionados con el trabajo."], "No corresponde"),
    ],
    mistakes=[("Acordar un aumento solo de palabra y no escribirlo.", "Si hay un conflicto, nada lo respalda.", "Todo lo acordado se deja por escrito y firmado."),
              ("Guardar el contrato en una carpeta abierta del escritorio.", "Cualquier persona podría ver datos personales y la remuneración.", "Guárdalo bajo reserva con acceso solo para personas autorizadas.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es un contrato de trabajo?", "Un acuerdo escrito entre un empleador y una persona trabajadora", "Una lista de precios de la empresa", "Un permiso de circulación", "El contrato deja por escrito las condiciones del trabajo entre las dos partes."),
        ("abc", "{F} ¿Quién es el empleador en la ficha?", "Servicios Quillay Ltda.", "Marcela Soto", "El certificado de estudios", "El empleador es la empresa que contrata."),
        ("abc", "{F} ¿Cuál es la jornada del borrador, según la ficha?", "40 horas semanales de ejemplo", "60 horas semanales", "Sin jornada", "La ficha indica 40 horas semanales como valor de ejemplo."),
        ("=", "{F} Si se pagara solo la remuneración base durante 12 meses, ¿cuántos pesos serían en total?", "600000*12", "Total = remuneración mensual × número de meses.", " pesos"),
        ("=", "{F} Con 4 semanas de 40 horas, ¿cuántas horas de trabajo son al mes (valor de ejemplo)?", "40*4", "Horas al mes = horas semanales × semanas.", " horas"),
        ("abc", "¿Qué dato NO se debe pedir a una persona que postula a un cargo administrativo?", "Su religión o sus creencias personales", "Su experiencia laboral relacionada con el cargo", "Sus estudios relacionados con el cargo", "Los datos sin relación con el cargo pueden discriminar."),
        ("abc", "{F} Un jefe sugiere guardar el certificado de estudios en una carpeta abierta para todos. ¿Qué corresponde?", "Guardarlo bajo reserva, con acceso solo a personas autorizadas", "Dejarlo abierto para ahorrar tiempo", "Enviarlo por una red social", "Los datos personales se guardan con reserva."),
        ("abc", "{F} Un compañero afirma que el plazo para tramitar el contrato es «de 15 días porque lo escuchó». ¿Qué corresponde?", "Consultarlo en el Código del Trabajo y la norma vigente", "Aceptar el dato porque es común", "Preguntar a un amigo", "Los plazos legales se consultan en las fuentes oficiales y no se repiten de oído."),
        ("abc", "{F} ¿Qué se hace antes de firmar si el nombre de la persona está mal escrito en el borrador?", "Corregirlo comparándolo con su documento de identificación", "Firmar igual y corregir después", "Dejarlo así", "Los datos de las partes deben ser exactos desde el inicio."),
        ("abc", "{F} La gerencia promete de palabra un bono que no está en el contrato. ¿Qué corresponde?", "Dejarlo por escrito en el contrato o en un anexo firmado", "Dejarlo solo de palabra", "No mencionarlo nunca", "Lo acordado se escribe para que respalde a ambas partes."),
        ("abc", "{F} ¿Qué relación tiene el contrato con la contabilidad?", "La remuneración acordada es la base para registrar el gasto del personal", "Ninguna", "El contrato reemplaza a la contabilidad", "Las cifras del contrato alimentan los registros contables."),
        ("abc", "Una asistente de RR.HH. comenta en un grupo de mensajes la remuneración de una persona de la empresa. ¿Qué falla?", "Rompe la confidencialidad de un dato personal", "Nada, porque es un comentario", "Falta una firma", "La remuneración y otros datos personales son reservados."),
        ("abc", "{F} Al tramitar el contrato, ¿cuál es un paso razonable después de firmarlo?", "Entregar una copia a la persona trabajadora y archivar el original con reserva", "Destruir el original", "Publicarlo en la oficina", "Cada parte debe tener copia y el archivo se resguarda."),
    ],
    ctx=("abc", "Marcela pregunta si puede ver su contrato firmado. ¿Qué responde la encargada de Recursos Humanos?", "Que le entregará una copia, porque es su documento", "Que es secreto", "Que no existe", "La persona trabajadora recibe una copia de su contrato, según la norma vigente; no es un documento secreto para ella."),
    sc=[
        ("En Recursos Humanos: ¿quiénes firman el contrato?", "Las dos partes: empleador y trabajador", "Ambas partes deben aceptar lo escrito."),
        ("¿Qué datos se piden al contratar?", "Solo los relacionados con el cargo", "Pedir lo demás puede resultar discriminatorio para las personas."),
        ("¿Dónde se consultan los plazos y requisitos legales?", "En el Código del Trabajo y la norma vigente", "No se repiten de oído ni se inventan."),
    ],
    op=("Con la Ficha 47, completa un resumen de contrato de seis líneas con: partes, cargo, lugar, jornada, remuneración base y fecha de inicio. Agrega una frase que diga qué consultarías en el Código del Trabajo y la norma vigente antes de tramitarlo, y cómo guardarías el contrato con reserva.\n{F}",
        "Partes: Servicios Quillay Ltda. y Marcela Soto. Cargo: asistente administrativa. Lugar: oficina central. Jornada: 40 horas semanales de ejemplo. Remuneración base: $600.000 mensuales. Inicio: 1 de marzo. Consultaría en el Código del Trabajo y la norma vigente lo que debe contener el contrato y sus plazos. Lo guardaría bajo reserva con acceso solo a personas autorizadas.",
        ["usa los datos de la ficha", "no inventa plazos ni cifras legales", "menciona reserva de datos"],
        ["resumen de seis líneas y una frase final"],
        ["inventar plazos legales", "dejar el contrato a la vista", "pedir datos innecesarios"],
        "Compara cada dato con la ficha. Si el estudiante inventa un plazo legal, pide cambiarlo por «lo consultaré en la norma vigente»."),
    reinforce="Completa en papel un contrato ficticio de seis líneas con partes, cargo, jornada y remuneración de ejemplo.",
    extend="Explica con un ejemplo inventado por qué un acuerdo solo hablado puede causar conflictos.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 48 (documentos y roles de ejemplo, inventados) de «Servicios Quillay Ltda.». Contrato de trabajo: acuerdo escrito entre empleador y trabajador. Anexo de contrato: documento que modifica algo acordado, como el cargo o la jornada. "
     "Liquidación de remuneraciones: detalle mensual de lo que se paga (haberes), lo que se descuenta y el líquido. Finiquito: documento que deja constancia de los pagos al terminar la relación laboral; se firma con las formalidades que exige la norma vigente. "
     "Remuneración bruta: total de haberes antes de descuentos. Remuneración líquida: lo que recibe la persona después de descuentos. Roles: encargado(a) de Recursos Humanos (llena y tramita), trabajador(a), gerencia (firma por la empresa) y contador(a) (registra en la contabilidad).")
build(
    O1, 2, F,
    use="Aprenderé el significado de los documentos del trabajo (contrato, anexo, liquidación y finiquito), los conceptos de remuneración bruta y líquida, y los roles que participan.",
    prior=["Sé qué es un contrato.", "Sé sumar y restar cifras en pesos.", "Sé que hay datos reservados."],
    explain=[
        "El contrato de trabajo establece las condiciones acordadas. Si algo cambia después, por ejemplo el cargo o la jornada, se deja constancia en un anexo de contrato firmado por las partes. Cada mes se entrega la liquidación de remuneraciones, que detalla los haberes (lo que se paga: sueldo base, bonos, asignaciones), los descuentos y el líquido.",
        "La remuneración bruta es el total de haberes antes de los descuentos. La remuneración líquida es lo que recibe la persona después de los descuentos: líquido = bruto − descuentos. Los descuentos incluyen conceptos previsionales, de salud, impuestos y otros descuentos autorizados; sus reglas están en la norma vigente. Al terminar la relación laboral, el finiquito deja constancia de los pagos pendientes y se firma con las formalidades que exige la norma vigente.",
        "En la tramitación participan varios roles. El encargado de Recursos Humanos llena y tramita los documentos; la gerencia firma por la empresa; la persona trabajadora firma y recibe su copia; el contador registra los pagos según las normas de contabilidad. Cada rol revisa su parte y no cambia lo que no le corresponde.",
    ],
    vocab=[("anexo de contrato", "documento que modifica algo del contrato"), ("liquidación", "detalle mensual de haberes, descuentos y líquido"), ("haberes", "pagos que recibe la persona trabajadora"), ("remuneración bruta", "total de haberes antes de descuentos"), ("remuneración líquida", "lo que recibe tras los descuentos"), ("finiquito", "documento que deja constancia de los pagos al terminar el trabajo")],
    worked=[
        ("Bruto y líquido", "Una liquidación ficticia tiene haberes por $500.000 y descuentos por $90.000. ¿Cuál es el líquido?", ["Líquido = bruto − descuentos.", "500.000 − 90.000 = 410.000."], "$410.000"),
        ("Elegir el documento", "Cambia la jornada de una persona de una empresa ficticia. ¿Qué documento corresponde?", ["Se modifica algo acordado.", "Se usa un anexo de contrato."], "Anexo de contrato"),
    ],
    mistakes=[("Confundir bruto con líquido y pagar el bruto sin descuentos.", "Se paga de más y se incumplen las obligaciones de retención.", "Calcula el líquido restando los descuentos al bruto."),
              ("Modificar el contrato original a mano para cambiar la jornada.", "Pierde validez y genera conflictos.", "Usa un anexo firmado por ambas partes.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es la remuneración líquida?", "Lo que recibe la persona después de los descuentos", "El total antes de descuentos", "Solo los bonos", "El líquido resulta de restar los descuentos al bruto."),
        ("abc", "{F} ¿Qué documento deja constancia de los pagos al terminar la relación laboral?", "El finiquito", "El anexo de contrato", "La liquidación mensual", "El finiquito se firma al término del trabajo."),
        ("abc", "{F} ¿Qué documento modifica algo acordado en el contrato?", "El anexo de contrato", "El finiquito", "La liquidación", "El anexo deja constancia de un cambio firmado por las partes."),
        ("abc", "{F} ¿Qué rol llena y tramita los documentos?", "El encargado o la encargada de Recursos Humanos", "El contador", "La persona trabajadora", "La ficha asigna esa función a RR.HH."),
        ("abc", "{F} ¿Qué rol registra los pagos en la contabilidad?", "El contador o la contadora", "La gerencia", "El trabajador", "La contabilidad la lleva el contador."),
        ("=", "Una liquidación de ejemplo tiene sueldo base $450.000 y un bono de $60.000. ¿Cuántos pesos suman los haberes (bruto)?", "450000+60000", "Bruto = suma de haberes.", " pesos"),
        ("=", "Esa liquidación de ejemplo tiene descuentos por $95.000. ¿Cuántos pesos es el líquido?", "450000+60000-95000", "Líquido = bruto − descuentos.", " pesos"),
        ("=", "Otra liquidación de ejemplo tiene bruto $800.000 y líquido $655.000. ¿Cuántos pesos suman los descuentos?", "800000-655000", "Descuentos = bruto − líquido.", " pesos"),
        ("abc", "{F} Una persona cambia de cargo con la misma jornada. ¿Qué se hace?", "Se firma un anexo de contrato", "Se destruye el contrato", "Se anota con lápiz", "El cambio se documenta con un anexo firmado."),
        ("abc", "{F} Un empleado pide la liquidación del mes. ¿Qué corresponde?", "Entregarla porque detalla lo que recibe y lo que se descuenta", "Negarse porque es reservada para la empresa", "Entregarla a su compañero", "La liquidación es un documento de la persona trabajadora."),
        ("abc", "{F} ¿Quién firma por la empresa?", "La gerencia", "El contador solo", "El cliente", "Según la ficha, la gerencia firma por la empresa."),
        ("abc", "Un encargado corrige con corrector una cifra del contrato firmado. ¿Qué falla?", "Altera un documento firmado; debe hacerse un anexo", "Nada, es una corrección menor", "Falta una cuarta firma", "Un documento firmado no se altera: los cambios se hacen por anexo."),
        ("abc", "{F} Los descuentos de una liquidación se determinan con:", "La norma vigente y lo autorizado por la persona trabajadora", "La opinión del jefe", "Un sorteo", "Las reglas de descuentos están en la norma, no en la voluntad del jefe."),
    ],
    ctx=("abc", "El contador pregunta de dónde saca el dato de lo que se pagó a cada persona en el mes. ¿Qué documento le entrega RR.HH.?", "Las liquidaciones de remuneraciones", "Los anexos de otros años", "Un finiquito de otra empresa", "Las liquidaciones del mes muestran lo pagado a cada persona."),
    sc=[
        ("En Recursos Humanos: ¿cómo se calcula el líquido?", "Bruto menos descuentos", "El líquido es lo que queda tras los descuentos."),
        ("¿Qué documento se usa para modificar un contrato?", "El anexo de contrato", "Deja el cambio firmado por ambas partes."),
        ("¿Quién firma el finiquito?", "Las partes, con las formalidades de la norma vigente", "No se firma de cualquier manera."),
    ],
    op=("Con la Ficha 48, arma una tabla con cuatro filas (contrato, anexo, liquidación, finiquito) y tres columnas: para qué sirve, quién lo llena o firma y qué dato personal contiene. Cierra con una regla de reserva de esos datos.\n{F}",
        "Contrato: acuerdo escrito; lo llena RR.HH. y lo firman las partes; contiene identidad, cargo y remuneración. Anexo: modifica algo acordado; firmado por las partes; contiene el cambio. Liquidación: detalle mensual; la emite RR.HH. y el contador la usa; contiene remuneración y descuentos. Finiquito: constancia de pagos al terminar; se firma con las formalidades de la norma vigente; contiene remuneración y pagos. Regla: guardar bajo reserva con acceso restringido.",
        ["describe bien los cuatro documentos", "asigna roles según la ficha", "incluye una regla de reserva"],
        ["tabla de cuatro filas y una regla"],
        ["confundir anexo con finiquito", "olvidar la reserva", "inventar requisitos legales"],
        "Compara con la ficha. Si inventa requisitos legales, pide cambiarlos por «según la norma vigente»."),
    reinforce="Escribe en papel una liquidación ficticia con tres haberes y dos descuentos, y calcula el líquido.",
    extend="Explica con un ejemplo inventado qué problema produce no entregar copia del contrato a la persona trabajadora.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 49 (documentos de ejemplo con errores, inventados) de «Servicios Quillay Ltda.». Borrador de contrato: «Contrato de trabajo entre Servicios Quillay Ltda. y Marcela Soto. Cargo: asistente. Lugar: oficina central. Jornada: (en blanco). "
     "Remuneración: a convenir. Fecha de inicio: 31 de febrero. Firmas: pendientes.» Liquidación del primer mes: sueldo base $600.000; asignación de ejemplo $40.000; descuentos de ejemplo $120.000. La empresa transfirió $560.000.")
build(
    O1, 3, F,
    use="Aprenderé a analizar documentos laborales con errores en papel: detectar datos faltantes o imposibles, comparar cifras y proponer correcciones sin inventar normas.",
    prior=["Conozco los documentos laborales.", "Sé calcular bruto y líquido.", "Sé que lo acordado se escribe."],
    explain=[
        "Revisar un borrador de contrato es comprobar que cada dato exista, sea posible y no sea ambiguo. Un campo en blanco, como la jornada, deja sin acordar un punto esencial. Una expresión como «a convenir» no fija la remuneración. Una fecha imposible, como un 31 de febrero, es un error de digitación. Antes de firmar se corrigen todos y se confirma con las partes.",
        "Revisar una liquidación es comparar cifras: bruto = haberes; líquido = bruto − descuentos; el monto pagado debe ser igual al líquido. Si el pago no coincide, hay una diferencia que se investiga con los documentos, y se corrige con respaldo y autorización de la jefatura. Nunca se ajusta una cifra sin entender la causa.",
        "Las correcciones se proponen por escrito y quedan registradas. No se cambia el sentido del contrato por cuenta propia: se consulta a quienes lo acordaron. Los plazos y las obligaciones legales se confirman en el Código del Trabajo y la norma vigente.",
    ],
    vocab=[("campo en blanco", "dato sin completar"), ("ambigüedad", "expresión que no fija un dato"), ("dato imposible", "dato que no puede existir, como una fecha inexistente"), ("diferencia", "resta entre lo que debió pagarse y lo que se pagó"), ("corrección", "cambio que arregla un error"), ("respaldo", "documento que prueba una cifra")],
    worked=[
        ("Detectar un error", "Un contrato ficticio dice «Jornada: ___». ¿Qué problema tiene?", ["El campo está en blanco.", "Un punto esencial queda sin acordar."], "Falta la jornada"),
        ("Diferencia de pago", "Una liquidación ficticia tiene líquido $300.000 y se pagó $310.000. ¿Cuál es la diferencia?", ["310.000 − 300.000 = 10.000.", "Se pagó de más."], "$10.000 pagados de más"),
    ],
    mistakes=[("Firmar el contrato con un campo en blanco para completarlo después.", "Otra persona podría completarlo distinto de lo acordado.", "Completa todos los datos antes de firmar."),
              ("Ajustar el monto transferido para que coincida sin investigar.", "Se esconde el error y no se explica la causa.", "Compara con la liquidación y busca la causa.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué problema tiene el campo «Remuneración: a convenir»?", "No fija la remuneración acordada", "Fija una remuneración muy alta", "Es el formato correcto", "«A convenir» deja sin definir un punto esencial."),
        ("abc", "{F} ¿Qué error tiene la fecha de inicio?", "El 31 de febrero no existe", "Está escrita con letra mayúscula", "Es demasiado temprana", "Febrero no tiene 31 días, así que esa fecha no existe."),
        ("abc", "{F} ¿Qué falta en la jornada del borrador?", "El dato: está en blanco", "Nada, está completa", "Una firma", "La jornada es un dato esencial que debe estar escrito."),
        ("=", "{F} ¿Cuántos pesos suman los haberes de la liquidación (sueldo base más asignación)?", "600000+40000", "Bruto = suma de haberes.", " pesos"),
        ("=", "{F} ¿Cuál es el líquido de la liquidación?", "600000+40000-120000", "Líquido = bruto − descuentos.", " pesos"),
        ("=", "{F} ¿Cuál es la diferencia entre lo transferido y el líquido?", "560000-(600000+40000-120000)", "Diferencia = transferido − líquido.", " pesos"),
        ("abc", "{F} ¿Qué indica esa diferencia?", "Se transfirieron $40.000 de más", "Se transfirieron $40.000 de menos", "No hay diferencia", "El monto transferido es mayor que el líquido."),
        ("abc", "{F} El encargado propone ajustar la liquidación a $560.000 para que coincida con la transferencia. ¿Qué respondes?", "Primero hay que investigar la causa con los documentos", "Está bien si coincide", "Se debe borrar la transferencia", "Igualar sin causa oculta el error."),
        ("abc", "{F} ¿Cuántos errores de datos tiene el borrador antes de firmar (campo en blanco, dato ambiguo y fecha imposible)?", "Tres", "Uno", "Cinco", "Hay tres datos que corregir: jornada, remuneración y fecha."),
        ("abc", "{F} El borrador dice solo «Cargo: asistente». ¿Qué mejora corresponde?", "Precisar el cargo como acuerden las partes, por ejemplo «asistente administrativa»", "Dejarlo así porque es corto", "Cambiarlo a gerente", "Un cargo claro evita conflictos sobre las funciones."),
        ("abc", "{F} La gerencia pide firmar hoy aunque la jornada esté en blanco, para «completarla después». ¿Qué es lo más adecuado?", "Completar la jornada antes de firmar", "Firmar y completar con lápiz", "Firmar y no completar", "Un contrato debe estar completo al firmarse."),
        ("abc", "{F} Un compañero dice que «a convenir» significa lo mismo que $600.000. ¿Qué respondes?", "Hay que escribir el monto acordado; «a convenir» no es una cifra", "Es lo mismo", "Depende del día", "Una cifra concreta evita malentendidos entre las dos partes."),
        ("abc", "{F} ¿Dónde se consulta qué otros datos debe llevar un contrato?", "En el Código del Trabajo y la norma vigente", "En un foro de internet", "Con un amigo", "Los requisitos legales se consultan en las fuentes oficiales."),
    ],
    ctx=("abc", "Una asistente revisa el contrato y escribe: «Falta la jornada, la remuneración no tiene cifra y la fecha no existe». ¿Qué hizo bien?", "Describió hechos verificables de cada error", "Dio una opinión sobre la gerencia", "Ocultó los errores", "Describir hechos permite corregir cada dato."),
    sc=[
        ("En Recursos Humanos: ¿qué se hace con un campo en blanco antes de firmar?", "Se completa con el dato acordado", "Un contrato debe estar completo antes de ser firmado."),
        ("¿Qué se hace si el pago no coincide con el líquido?", "Se investiga la causa con los documentos", "No se ajusta sin entender el error."),
        ("¿Dónde se consultan los requisitos legales?", "En el Código del Trabajo y la norma vigente", "No se inventan requisitos: se consultan en la norma."),
    ],
    op=("Con la Ficha 49, escribe un informe de revisión de seis líneas: los tres errores del borrador con su corrección propuesta, el cálculo del líquido y la diferencia con lo transferido, y una acción para resolverla sin ajustar cifras sin causa.\n{F}",
        "Errores: jornada en blanco (completar con la acordada), remuneración «a convenir» (escribir el monto acordado), fecha 31 de febrero (corregir a una fecha real). Líquido: $520.000. Se transfirieron $560.000: hay $40.000 de más. Se investigará la causa con los documentos y se corregirá con respaldo y autorización de la jefatura.",
        ["detecta los tres errores", "calcula líquido y diferencia", "propone investigar la causa"],
        ["informe de seis líneas"],
        ["ajustar cifras sin causa", "inventar plazos legales", "no proponer corrección"],
        "Rehace el cálculo con la ficha. Si ajusta cifras sin causa, pide revisar los documentos."),
    reinforce="Revisa en papel un contrato ficticio de cinco líneas que inventes e identifica un campo en blanco y uno ambiguo.",
    extend="Explica con un ejemplo inventado por qué una diferencia de pago pequeña igual debe investigarse.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 50 (datos de ejemplo, inventados) de «Servicios Quillay Ltda.». Remuneración base de ejemplo: $750.000. Bono de ejemplo: $50.000. Asignación de ejemplo: $30.000. "
     "Descuentos de ejemplo (porcentajes de ejemplo, no son las tasas reales): 10 % de la remuneración base y 8 % de la remuneración base; anticipo de ejemplo ya entregado: $40.000. "
     "Finiquito de ejemplo de otra persona con la misma remuneración base: valor diario de ejemplo = remuneración base ÷ 30; remuneración pendiente: 10 días; feriado proporcional de ejemplo: 6 días al mismo valor diario; pago adicional de ejemplo: $100.000.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar la tramitación con cálculos de ejemplo: bruto, descuentos, líquido y un finiquito con valores de ejemplo, sin usar cifras legales reales.",
    prior=["Sé calcular bruto y líquido.", "Sé calcular porcentajes.", "Sé que las tasas reales están en la norma vigente."],
    explain=[
        "El cálculo de una liquidación sigue un orden: primero los haberes (base + bonos + asignaciones) dan el bruto; después se calculan los descuentos, algunos como porcentaje de una base y otros como montos; por último, líquido = bruto − descuentos − anticipos. Para calcular un porcentaje se multiplica la base por el porcentaje y se divide en 100.",
        "En un finiquito de ejemplo se suman los conceptos pendientes: remuneración de los días trabajados, feriado proporcional y otros pagos que correspondan. El valor diario de ejemplo se obtiene dividiendo la remuneración base entre 30 y se multiplica por los días. Las reglas reales de qué conceptos corresponden y cómo se calculan están en el Código del Trabajo y la norma vigente, y no se deducen de este cuaderno.",
        "Los resultados deben quedar respaldados: cada cifra con su fuente, los documentos firmados y una copia para la persona trabajadora. La revisión de un segundo responsable reduce errores. Los datos personales se mantienen reservados.",
    ],
    vocab=[("haberes", "pagos que recibe la persona"), ("porcentaje de ejemplo", "valor inventado para practicar, no una tasa real"), ("anticipo", "pago adelantado que se descuenta"), ("valor diario", "remuneración base dividida por 30 en este ejemplo"), ("feriado proporcional", "pago por días de descanso pendientes (valor de ejemplo)"), ("segunda revisión", "revisión por otra persona")],
    worked=[
        ("Porcentaje", "Una base ficticia de $400.000 con un descuento de ejemplo del 5 %. ¿Cuánto es el descuento?", ["400.000 × 5 ÷ 100 = 20.000.", "Es un valor de ejemplo."], "$20.000"),
        ("Valor diario", "Una remuneración base ficticia es $600.000. ¿Cuánto es el valor diario de ejemplo (÷ 30)?", ["600.000 ÷ 30 = 20.000.", "Es una regla de ejemplo."], "$20.000"),
    ],
    mistakes=[("Calcular el porcentaje sobre el bruto cuando la ficha dice «sobre la base».", "El resultado cambia y no sigue el criterio acordado.", "Usa la base que indica la ficha."),
              ("Olvidar restar el anticipo al calcular el líquido.", "Se paga de más.", "Resta los descuentos y también los anticipos.")],
    T=[
        ("abc", "En Recursos Humanos: ¿cómo se calcula el 10 % de una base?", "Base por 10 dividido por 100", "Base más 10", "Base dividida por 10 más 100", "El porcentaje se calcula multiplicando por el número y dividiendo en 100."),
        ("=", "{F} ¿Cuántos pesos suman los haberes (base, bono y asignación)?", "750000+50000+30000", "Bruto = suma de haberes.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el primer descuento de ejemplo (10 % de la base)?", "750000*10//100", "Descuento = base × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el segundo descuento de ejemplo (8 % de la base)?", "750000*8//100", "Descuento = base × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suman los dos descuentos?", "750000*10//100+750000*8//100", "Se suman los dos descuentos calculados.", " pesos"),
        ("=", "{F} ¿Cuál es el líquido, descontando los dos porcentajes y el anticipo?", "830000-135000-40000", "Líquido = bruto − descuentos − anticipo.", " pesos"),
        ("=", "{F} ¿Cuánto es el valor diario de ejemplo (base ÷ 30)?", "750000//30", "Valor diario = base ÷ 30.", " pesos"),
        ("=", "{F} ¿Cuánto suma la remuneración pendiente de 10 días?", "750000//30*10", "Pendiente = valor diario × días.", " pesos"),
        ("=", "{F} ¿Cuánto suma el feriado proporcional de ejemplo de 6 días?", "750000//30*6", "Feriado = valor diario × días de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuánto suma el total del finiquito de ejemplo (pendiente, feriado y pago adicional)?", "750000//30*10+750000//30*6+100000", "Se suman los tres conceptos de ejemplo.", " pesos"),
        ("abc", "{F} Un compañero afirma que ese total es lo que corresponde pagar en cualquier finiquito. ¿Qué respondes?", "Es un cálculo de ejemplo; el real sigue el Código del Trabajo y la norma vigente", "Tiene razón, es una regla general", "Se debe pagar siempre el doble", "Los conceptos reales y su cálculo los fija la norma, no el ejemplo."),
        ("abc", "{F} ¿Qué paso reduce errores antes de entregar el cálculo?", "La revisión de otra persona", "Entregarlo sin revisar", "Cambiar cifras al azar", "Una segunda revisión detecta errores de suma."),
        ("abc", "{F} Al entregar el finiquito firmado, ¿qué corresponde con los datos personales?", "Entregar copia a la persona y guardar el original con reserva", "Publicar una copia en la oficina", "Enviarlo a otra empresa", "Los documentos con datos personales se resguardan."),
    ],
    ctx=("abc", "La gerencia pregunta cuánto recibiría la persona del ejemplo. ¿Qué responde un cálculo ordenado?", "$655.000 de líquido con los porcentajes de ejemplo y el anticipo", "$830.000", "$750.000", "El líquido se calcula con descuentos y anticipo, no con el bruto."),
    sc=[
        ("En Recursos Humanos: ¿qué se resta al bruto para obtener el líquido?", "Los descuentos y los anticipos", "El anticipo ya se entregó y se descuenta."),
        ("¿Cómo se calcula el valor diario de ejemplo?", "Base dividida por 30", "Es una regla de ejemplo del cuaderno."),
        ("¿Dónde se confirma qué conceptos corresponden en un finiquito real?", "En el Código del Trabajo y la norma vigente", "Los conceptos reales no se deducen de un ejemplo."),
    ],
    op=("Con la Ficha 50, escribe una hoja de cálculo con: bruto, los dos descuentos, el anticipo, el líquido y el total del finiquito de ejemplo. Termina con una frase que aclare que son cifras de ejemplo y qué normas consultarías en un caso real.\n{F}",
        "Bruto: $830.000. Descuentos de ejemplo: $75.000 y $60.000. Anticipo: $40.000. Líquido: $655.000. Finiquito de ejemplo: $250.000 + $150.000 + $100.000 = $500.000. Son cifras de ejemplo; en un caso real consultaría el Código del Trabajo y la norma vigente.",
        ["calcula bruto, descuentos y líquido", "calcula el finiquito de ejemplo", "aclara que son cifras de ejemplo"],
        ["hoja de cálculo de seis líneas y una frase"],
        ["olvidar el anticipo", "presentar cifras de ejemplo como reales", "no consultar normas"],
        "Rehace los cálculos con la ficha. Si presenta el finiquito como regla general, pide agregar la aclaración."),
    reinforce="Calcula en papel un líquido de ejemplo con base $500.000, un descuento del 5 % y un anticipo de $20.000.",
    extend="Explica con un ejemplo inventado por qué un cálculo de ejemplo no sirve para decidir un pago real.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 51 (planilla de ejemplo, inventada) de «Servicios Quillay Ltda.». Personas ficticias: A. Soto, remuneración base $500.000; B. Araya, remuneración base $650.000; C. Pérez, remuneración base $800.000. "
     "Parámetros de ejemplo (no son las tasas reales): descuento previsional de ejemplo, 10 % de la base; descuento de salud de ejemplo, 8 % de la base; impuesto de ejemplo retenido: A $0, B $10.000, C $30.000.")
build(
    O2, 1, F,
    use="Aprenderé por qué el cálculo de remuneraciones es una obligación con consecuencias para las personas, qué papel tienen las obligaciones previsionales y tributarias y qué cuidados éticos se aplican.",
    prior=["Sé calcular bruto y líquido.", "Sé calcular porcentajes.", "Sé que los datos personales son reservados."],
    explain=[
        "Calcular remuneraciones es determinar, para cada persona y cada período, lo que se debe pagar y lo que se debe descontar, de acuerdo con su contrato, la legislación vigente y las normas de contabilidad (NIC). Un error afecta a la persona (recibe de menos o de más), a la empresa (puede deber diferencias) y a las instituciones a las que se informan o pagan los descuentos.",
        "Las obligaciones previsionales son los descuentos que sirven para pensiones y salud y otros fondos de seguridad social; las obligaciones tributarias incluyen el impuesto que se retiene a algunos ingresos según la norma vigente. El empleador retiene (descuenta) esos montos y los entrega a las instituciones correspondientes en los plazos que fija la norma vigente. Las tasas y plazos reales no se enseñan aquí: se usan porcentajes y montos de ejemplo.",
        "Hay cuidados éticos. Las remuneraciones y descuentos son datos personales reservados; solo las ven quienes los necesitan para su trabajo. No se alteran cálculos para favorecer o perjudicar a una persona. Se guardan los respaldos y se revisan los cálculos antes de pagar.",
    ],
    vocab=[("obligación previsional", "descuento para pensión, salud y seguridad social"), ("obligación tributaria", "impuesto que debe retenerse o pagarse"), ("retener", "descontar un monto para entregarlo a una institución"), ("planilla", "tabla con las remuneraciones de varias personas"), ("período", "mes o tiempo que se calcula"), ("respaldo", "documento que prueba un cálculo")],
    worked=[
        ("Retener", "Una persona ficticia tiene base $400.000 y un descuento de ejemplo del 5 %. ¿Cuánto retiene la empresa?", ["400.000 × 5 ÷ 100 = 20.000.", "Esa suma se entrega a la institución."], "$20.000"),
        ("Dato reservado", "Una asistente ficticia muestra a un colega sin relación el sueldo de otro compañero. ¿Qué falla?", ["El sueldo es un dato personal.", "Solo lo ven quienes lo necesitan para su trabajo."], "Rompe la reserva del dato"),
    ],
    mistakes=[("Calcular las remuneraciones de memoria sin respaldo.", "Los errores se multiplican y no se pueden comprobar.", "Usa la planilla con los documentos de respaldo."),
              ("Comentar los sueldos de la empresa con otras personas.", "Los sueldos son datos personales reservados.", "Comparte solo con quienes lo necesitan para su trabajo.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué significa retener un descuento?", "Descontar un monto para entregarlo a una institución", "Guardar el monto para la empresa", "Perder el documento", "El empleador retiene y entrega lo que corresponde a las instituciones."),
        ("abc", "{F} ¿Qué dato de la ficha es la remuneración base de B. Araya?", "$650.000", "$500.000", "$800.000", "La ficha asigna $650.000 a B. Araya."),
        ("=", "{F} ¿Cuántos pesos suman las remuneraciones base de las tres personas?", "500000+650000+800000", "Total = suma de las tres bases.", " pesos"),
        ("=", "{F} ¿Cuánto es el descuento previsional de ejemplo (10 %) de A. Soto?", "500000*10//100", "Descuento = base × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuánto es el descuento de salud de ejemplo (8 %) de A. Soto?", "500000*8//100", "Descuento = base × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos retiene la empresa en total a B. Araya (previsional, salud e impuesto de ejemplo)?", "650000*10//100+650000*8//100+10000", "Se suman los tres descuentos de ejemplo.", " pesos"),
        ("abc", "{F} Si un error de cálculo hace pagar $20.000 de menos a una persona, ¿quién se ve perjudicado?", "La persona trabajadora, y la empresa puede deber la diferencia", "Nadie", "Solo el banco", "Un error de menos perjudica a la persona y genera una deuda de la empresa."),
        ("abc", "{F} Un colega propone calcular los sueldos «a ojo» para ir más rápido. ¿Qué respondes?", "Se calcula con la planilla y respaldos, y se revisa", "Está bien si el equipo confía", "Sí, siempre que sea la mitad", "Un cálculo sin respaldo no puede comprobarse."),
        ("abc", "Alguien pregunta por la remuneración de un compañero por curiosidad. ¿Qué corresponde?", "No entregarla, porque es un dato personal reservado", "Entregarla si lo pide por favor", "Publicarla", "La remuneración es reservada y solo la ven quienes la necesitan."),
        ("abc", "Un jefe pide bajar el descuento de una persona «de su confianza» para que reciba más. ¿Qué corresponde?", "Rechazarlo: los descuentos se aplican según la norma, no por preferencia", "Aceptarlo si es poco dinero", "Aceptarlo y no avisar", "Alterar un descuento es una falta y no puede hacerse por preferencia."),
        ("abc", "{F} ¿Dónde se consultan las tasas y plazos reales de las cotizaciones?", "En la norma vigente y las instituciones correspondientes", "En este cuaderno de ejemplo", "Con un amigo", "Las tasas reales y los plazos se consultan en fuentes oficiales."),
        ("abc", "{F} Un porcentaje de la ficha es de ejemplo. ¿Qué significa?", "Que sirve para practicar y no es la tasa real", "Que es la tasa real", "Que es obligatorio", "La ficha lo rotula de ejemplo para evitar confusiones."),
        ("abc", "{F} Antes de pagar, ¿qué paso reduce los errores?", "Revisar el cálculo con un segundo responsable", "Pagar sin revisar", "Cambiar cifras al azar", "La segunda revisión detecta errores de suma o de dato."),
    ],
    ctx=("abc", "Una persona nueva en RR.HH. recibe la planilla de remuneraciones del mes. ¿Qué precaución tiene con ella?", "La usa solo para su trabajo y la guarda con acceso restringido", "La deja abierta en la sala de descanso", "La envía a sus amigos", "La planilla tiene datos personales y debe resguardarse."),
    sc=[
        ("En Recursos Humanos: ¿qué es una obligación previsional?", "Un descuento para pensión, salud y seguridad social", "Es una obligación legal que se retiene y se entrega."),
        ("¿Por qué un error de cálculo importa?", "Afecta a la persona, a la empresa y a las instituciones", "Una diferencia genera deudas o pagos de menos."),
        ("¿Se pueden comentar los sueldos con cualquier persona?", "No, son datos personales reservados", "Solo los ven quienes los necesitan para su trabajo."),
    ],
    op=("Con la Ficha 51, escribe un resumen de cinco líneas: la suma de las tres remuneraciones base, los descuentos de ejemplo (previsional y salud) de C. Pérez, qué es retener, y una regla de reserva de los datos de la planilla. Aclara que los porcentajes son de ejemplo.\n{F}",
        "Suma de bases: $1.950.000. Descuentos de ejemplo de C. Pérez: previsional $80.000 y salud $64.000. Retener es descontar un monto para entregarlo a la institución correspondiente. Regla: la planilla se guarda con acceso restringido y solo la ven quienes la necesitan. Los porcentajes son de ejemplo, no tasas reales.",
        ["calcula las cifras", "define retener", "propone una regla de reserva", "aclara que son porcentajes de ejemplo"],
        ["resumen de cinco líneas"],
        ["presentar los porcentajes como reales", "no incluir reserva", "inventar tasas"],
        "Revisa los cálculos. Si presenta porcentajes como reales, pide la aclaración."),
    reinforce="Calcula en papel el 10 % y el 8 % de una base ficticia de $700.000.",
    extend="Explica con un ejemplo inventado cómo un error en un descuento puede afectar a más de una persona.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 52 (conceptos y documentos de ejemplo, inventados) de «Servicios Quillay Ltda.». Haberes imponibles: pagos sobre los cuales se calculan los descuentos previsionales (en el ejemplo: sueldo base y bonos; las horas extra no entran en esa base de ejemplo). Haberes no imponibles: pagos sobre los que no se calculan (en el ejemplo: una asignación de colación). "
     "Horas extraordinarias: horas trabajadas sobre la jornada pactada, que se pagan con un recargo (aquí, un recargo de ejemplo del 50 %). Valor hora de ejemplo = remuneración base ÷ 160. "
     "Libro de remuneraciones: registro mensual de todas las liquidaciones. Registro contable de ejemplo: el gasto en remuneraciones se anota como gasto y lo que aún no se paga como «remuneraciones por pagar» (un pasivo). Roles: encargado(a) de RR.HH., contador(a), gerencia.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos de haberes imponibles y no imponibles, horas extraordinarias, libro de remuneraciones y registro contable básico, con valores de ejemplo.",
    prior=["Sé calcular bruto y líquido.", "Conozco retenciones previsionales y tributarias.", "Sé qué es un pasivo."],
    explain=[
        "Los haberes se clasifican: los imponibles son los pagos sobre los cuales se calculan los descuentos previsionales; los no imponibles no entran en ese cálculo. Esta clasificación y sus límites los fija la norma vigente; aquí se usa una clasificación de ejemplo. Entender la diferencia permite calcular bien la base de los descuentos.",
        "Las horas extraordinarias son las trabajadas sobre la jornada pactada y se pagan con un recargo según la norma vigente; en este cuaderno el recargo es de ejemplo. Para calcularlas se obtiene el valor hora de ejemplo, se le aplica el recargo y se multiplica por las horas. Todas las liquidaciones del mes se resumen en el libro de remuneraciones, que respalda el trabajo de RR.HH. y de la contabilidad.",
        "Las normas contables (NIC) indican que los pagos al personal se reconocen como gasto del período y que lo que aún no se paga queda como una obligación llamada remuneraciones por pagar. En este nivel se entiende la idea: el gasto aumenta y el pasivo aumenta hasta que se paga. Los detalles contables los ve el contador.",
    ],
    vocab=[("haber imponible", "pago sobre el que se calculan descuentos previsionales"), ("haber no imponible", "pago que no entra en ese cálculo"), ("horas extraordinarias", "horas sobre la jornada pactada"), ("recargo", "porcentaje adicional pagado por esas horas"), ("libro de remuneraciones", "registro mensual de todas las liquidaciones"), ("remuneraciones por pagar", "obligación por sueldos aún no pagados")],
    worked=[
        ("Base imponible", "Una persona ficticia tiene sueldo base $500.000, bono $40.000 (imponible) y colación $30.000 (no imponible). ¿Cuánto suman los haberes imponibles?", ["Se suman base y bono.", "500.000 + 40.000 = 540.000."], "$540.000"),
        ("Valor hora", "Con una base ficticia de $480.000 y la regla de ejemplo ÷ 160, ¿cuál es el valor hora?", ["480.000 ÷ 160 = 3.000.", "Es una regla de ejemplo."], "$3.000"),
    ],
    mistakes=[("Calcular el descuento previsional sobre la colación no imponible.", "Se descuenta sobre una base que no corresponde.", "Calcula sobre los haberes imponibles de la clasificación vigente."),
              ("Pagar las horas extra al valor hora normal.", "Se omite el recargo.", "Aplica el recargo antes de multiplicar por las horas.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es un haber imponible?", "Un pago sobre el cual se calculan los descuentos previsionales", "Un pago que nunca se hace", "Un descuento", "Los haberes imponibles forman la base de los descuentos."),
        ("abc", "{F} ¿Qué haber de la ficha es no imponible?", "La asignación de colación", "El sueldo base", "Los bonos", "La ficha clasifica la colación como no imponible."),
        ("abc", "{F} ¿Qué es el libro de remuneraciones?", "Un registro mensual de todas las liquidaciones", "Un contrato de un trabajador", "Una lista de clientes", "El libro resume las liquidaciones del mes."),
        ("=", "{F} Una persona de ejemplo tiene base $640.000. ¿Cuánto es el valor hora de ejemplo (base ÷ 160)?", "640000//160", "Valor hora = base ÷ 160, regla de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuánto vale una hora extra con el recargo de ejemplo del 50 % (valor hora de $4.000)?", "4000+4000*50//100", "Hora extra = valor hora + recargo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suman 6 horas extra a $6.000 cada una?", "6000*6", "Total = valor de la hora extra × horas.", " pesos"),
        ("=", "{F} Una persona tiene base $640.000, bono imponible $60.000 y colación no imponible $30.000. ¿Cuánto suman los haberes imponibles?", "640000+60000", "Imponibles = base + bono.", " pesos"),
        ("=", "{F} Con un descuento previsional de ejemplo del 10 % de los haberes imponibles de $700.000, ¿cuántos pesos se descuentan?", "700000*10//100", "Descuento = base imponible × porcentaje ÷ 100.", " pesos"),
        ("abc", "{F} Un colega calcula el 10 % sobre $730.000 (incluye la colación). ¿Qué falla?", "Usó una base que incluye un haber no imponible", "Nada, es correcto", "Usó un bono", "La colación de la ficha no entra en la base imponible."),
        ("abc", "{F} ¿Qué efecto contable de ejemplo tiene devengar sueldos que aún no se pagan?", "Aumentan el gasto y las remuneraciones por pagar", "Disminuyen el gasto", "No pasa nada", "El gasto se reconoce y queda una obligación hasta el pago."),
        ("abc", "{F} Un compañero asegura que el recargo del 50 % es el real para toda hora extra. ¿Qué respondes?", "Es un recargo de ejemplo; el real se consulta en la norma vigente", "Tiene razón", "El recargo es 100 %", "El cuaderno usa valores de ejemplo, no cifras legales."),
        ("abc", "El libro de remuneraciones del mes suma $3.200.000 pero las liquidaciones suman $3.150.000. ¿Qué corresponde?", "Revisar la diferencia con las liquidaciones antes de cerrar", "Ajustar el libro a la baja", "Ignorarla", "Las cifras deben coincidir; se investiga la diferencia."),
        ("abc", "{F} ¿Quién registra en la contabilidad los sueldos devengados?", "El contador o la contadora", "La gerencia sola", "Un cliente", "El contador lleva los registros contables."),
    ],
    ctx=("abc", "RR.HH. entrega al contador el libro de remuneraciones del mes. ¿Para qué lo usa el contador?", "Para registrar el gasto del personal del mes", "Para contratar personal", "Para fijar sueldos", "El libro respalda el registro contable de remuneraciones."),
    sc=[
        ("En Recursos Humanos: ¿qué diferencia hay entre imponible y no imponible?", "En el imponible se calculan descuentos previsionales; en el no imponible, no", "La clasificación define la base de cálculo."),
        ("¿Cómo se calcula una hora extra de ejemplo?", "Valor hora más el recargo de ejemplo", "Se aplica el recargo antes de multiplicar por las horas."),
        ("¿Qué es «remuneraciones por pagar»?", "Una obligación por sueldos aún no pagados", "Es un pasivo hasta que se paga."),
    ],
    op=("Con la Ficha 52, calcula la liquidación de ejemplo de una persona con base $640.000, bono imponible $60.000, colación no imponible $30.000, 5 horas extra con el recargo de ejemplo y un descuento previsional de ejemplo del 10 % de los imponibles. Escribe haberes imponibles, horas extra, bruto, descuento y líquido.\n{F}",
        "Imponibles: $700.000. Valor hora: $4.000; hora extra con recargo: $6.000; 5 horas = $30.000. Bruto: 640.000 + 60.000 + 30.000 (colación) + 30.000 = $760.000. Descuento previsional de ejemplo: $70.000 (10 % de $700.000). Líquido: $690.000. Son valores de ejemplo.",
        ["clasifica imponibles y no imponibles", "calcula horas extra con recargo", "calcula el descuento sobre la base correcta", "indica que son valores de ejemplo"],
        ["liquidación de ejemplo de cinco cálculos"],
        ["incluir la colación en la base", "olvidar el recargo", "presentar valores como reales"],
        "Rehace los cálculos con la ficha. Si calcula el descuento sobre el bruto, pide usar los imponibles."),
    reinforce="Clasifica en papel cinco pagos ficticios como imponibles o no imponibles según la ficha.",
    extend="Explica con un ejemplo inventado cómo cambia el descuento si se sube un bono imponible.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 53 (liquidación de ejemplo con errores, inventada) de «Servicios Quillay Ltda.», persona ficticia B. Araya. Datos de contrato: base $650.000; bono imponible $50.000; colación no imponible $30.000; 4 horas extra autorizadas. "
     "Valor hora de ejemplo = base ÷ 160; recargo de ejemplo del 50 %. Descuento previsional de ejemplo: 10 % de los haberes imponibles. Descuento de salud de ejemplo: 8 % de los haberes imponibles (en el ejemplo, las horas extra no entran en esa base). "
     "Liquidación emitida: horas extra pagadas a $4.062 cada una (sin recargo, redondeadas), descuento previsional calculado sobre $780.000, descuento de salud calculado sobre $780.000.")
build(
    O2, 3, F,
    use="Aprenderé a analizar una liquidación con errores en papel: recalcular, comparar con lo emitido y proponer la corrección con respaldo, sin usar cifras legales reales.",
    prior=["Conozco haberes imponibles y no imponibles.", "Sé calcular horas extra con recargo.", "Sé comparar un cálculo con otro."],
    explain=[
        "Analizar una liquidación es recalcularla con los datos del contrato y compararla con la emitida. Se verifican en orden: la clasificación de los haberes (imponibles y no imponibles), las horas extra con su recargo, la base de cada descuento, el bruto y el líquido. Cualquier diferencia se anota con su monto y su causa probable.",
        "Cuando hay un error, se calcula la diferencia entre lo que se debió pagar y lo que se pagó. Si se pagó de menos, la empresa debe regularizar con respaldo; si se pagó de más, se informa a la jefatura para decidir cómo corregirlo según la norma vigente. No se corrige una liquidación sin autorización ni sin dejar registro.",
        "El informe de análisis es breve y objetivo: errores detectados, monto de cada uno, efecto en el líquido, corrección propuesta y quién la autoriza. Los datos de la persona se mantienen reservados y el informe lo ven solo quienes deben decidir.",
    ],
    vocab=[("recalcular", "volver a hacer un cálculo con los datos originales"), ("diferencia", "resta entre lo que debió pagarse y lo pagado"), ("causa probable", "explicación más posible, por verificar"), ("regularizar", "corregir un pago con respaldo"), ("base de cálculo", "monto sobre el que se aplica un porcentaje"), ("autorización", "visto bueno de la jefatura")],
    worked=[
        ("Verificar la base", "Una liquidación ficticia calcula el 10 % sobre $800.000, pero los imponibles son $760.000. ¿Está bien?", ["El descuento debe calcularse sobre $760.000.", "Usó una base mayor."], "No: la base es incorrecta"),
        ("Diferencia", "Debía pagarse $520.000 de líquido y se pagó $500.000. ¿Cuál es la diferencia y quién se perjudica?", ["520.000 − 500.000 = 20.000.", "Se pagó de menos a la persona."], "$20.000 de menos; se perjudica la persona"),
    ],
    mistakes=[("Corregir la liquidación en secreto para que nadie vea el error.", "No queda registro y puede repetirse.", "Informa, deja registro y pide autorización."),
              ("Aceptar la liquidación sin recalcularla porque «la hizo el sistema».", "El sistema repite los datos mal ingresados.", "Recalcula con los datos del contrato.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es recalcular una liquidación?", "Volver a hacer el cálculo con los datos del contrato", "Cambiar las cifras al azar", "Imprimirla otra vez", "Recalcular permite compararla con lo emitido."),
        ("=", "{F} ¿Cuánto es el valor hora de ejemplo (base ÷ 160)?", "650000//160", "Valor hora = base ÷ 160, parte entera.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suman los haberes imponibles (base y bono)?", "650000+50000", "Imponibles = base + bono.", " pesos"),
        ("abc", "{F} ¿Sobre qué monto se debe calcular el descuento previsional?", "$700.000, los haberes imponibles", "$730.000, que incluye la colación no imponible", "$650.000, solo la base", "La ficha dice que el descuento se calcula sobre los imponibles."),
        ("abc", "{F} ¿Qué error muestra la liquidación emitida en la base de los descuentos?", "Calculó sobre $780.000 en lugar de los imponibles", "Calculó sobre la base correcta", "No calculó descuentos", "Usó una base mayor que la de los haberes imponibles."),
        ("=", "{F} ¿Cuánto es el descuento previsional correcto (10 % de los imponibles)?", "700000*10//100", "Descuento = imponibles × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuánto es el descuento previsional emitido (10 % de $780.000)?", "780000*10//100", "Descuento emitido con la base errada.", " pesos"),
        ("=", "{F} ¿Cuánto descontó de más la liquidación en previsión?", "780000*10//100-700000*10//100", "Diferencia = descuento emitido − descuento correcto.", " pesos"),
        ("=", "{F} ¿Cuánto es la hora extra correcta con el recargo de ejemplo (valor hora de $4.062 más 50 %)?", "4062+4062*50//100", "Hora extra = valor hora + recargo.", " pesos"),
        ("abc", "{F} ¿Qué error muestra el pago de las horas extra a $4.062?", "No incluyó el recargo de ejemplo", "Pagó con recargo", "Pagó de más", "Pagó el valor hora sin recargo."),
        ("=", "{F} ¿Cuánto se pagó de menos en horas extra por no aplicar el recargo, en las 4 horas?", "(4062+4062*50//100)*4-4062*4", "Diferencia = pago correcto − pago emitido.", " pesos"),
        ("abc", "{F} Un colega propone corregir la liquidación sin avisar. ¿Qué respondes?", "Hay que informar, dejar registro y pedir autorización", "Corregirla en silencio", "No corregirla", "Las correcciones se informan y se autorizan."),
        ("abc", "{F} ¿Quién ve el informe de análisis de la liquidación?", "Solo quienes deben decidir y gestionar la corrección", "Cualquier persona de la empresa", "El público", "Los datos de remuneración son reservados."),
    ],
    ctx=("abc", "La contadora pregunta si el líquido de B. Araya está bien calculado. ¿Qué responde RR.HH. tras el análisis?", "No: hay errores en la base del descuento y en el recargo de las horas extra, que se corregirán con respaldo", "Sí, porque lo hizo el sistema", "No se puede saber", "El análisis encontró dos errores concretos."),
    sc=[
        ("En Recursos Humanos: ¿qué se verifica primero en una liquidación?", "La clasificación de haberes y la base de los descuentos", "Una base errada arrastra los demás cálculos."),
        ("¿Qué se hace al hallar un error?", "Se calcula la diferencia, se informa y se pide autorización", "El error no se corrige en silencio: se informa."),
        ("¿Quién ve el informe de análisis?", "Solo quienes deben decidir", "Los datos de remuneración son reservados."),
    ],
    op=("Con la Ficha 53, escribe un informe de seis líneas: los dos errores de la liquidación, el monto de cada uno, el efecto en el líquido (solo describir), la corrección propuesta y quién la autoriza. Aclara que los porcentajes son de ejemplo.\n{F}",
        "Error 1: descuentos previsional y de salud calculados sobre $780.000 en lugar de $700.000; se descontaron $8.000 y $6.400 de más (cifras de ejemplo). Error 2: horas extra pagadas sin recargo; faltaron $8.124 en las 4 horas (valor de ejemplo). Se propone recalcular con respaldo y regularizar. Autoriza la jefatura. Los porcentajes son de ejemplo.",
        ["detecta los dos errores", "calcula el monto de cada uno", "propone corrección autorizada", "aclara que son cifras de ejemplo"],
        ["informe de seis líneas"],
        ["corregir sin avisar", "no dar el monto", "presentar porcentajes como reales"],
        "Rehace los dos cálculos. Si no menciona autorización, pídela."),
    reinforce="Recalcula en papel una liquidación ficticia de cinco líneas con una base errada y halla la diferencia.",
    extend="Explica con un ejemplo inventado por qué un sistema computacional también puede producir una liquidación incorrecta.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 54 (datos de ejemplo, inventados) de «Servicios Quillay Ltda.». Planilla del mes con tres personas ficticias. Remuneraciones base: A. Soto $500.000; B. Araya $650.000; C. Pérez $800.000. Bonos imponibles: A $0; B $50.000; C $100.000. "
     "Descuento previsional de ejemplo: 10 % de los imponibles; descuento de salud de ejemplo: 8 % de los imponibles. Impuesto de ejemplo retenido: A $0; B $10.000; C $30.000. "
     "Finiquito de ejemplo de la persona D (ficticia) con base $600.000: valor diario de ejemplo = base ÷ 30; remuneración pendiente de 12 días; feriado proporcional de ejemplo de 5 días; indemnización de ejemplo $250.000 (dato dado, no calculado).")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio completo de cálculo con una planilla de ejemplo: líquidos, total retenido a instituciones, costo de la remuneración para la empresa y un finiquito de ejemplo.",
    prior=["Sé calcular descuentos sobre imponibles.", "Sé calcular el valor diario de ejemplo.", "Sé que las cifras son de ejemplo."],
    explain=[
        "Una planilla de remuneraciones se arma persona por persona con el mismo orden: imponibles (base + bonos imponibles), descuento previsional y de salud (porcentaje × imponibles), impuesto retenido, y líquido = bruto − descuentos. Luego se suman las columnas para obtener los totales: total de líquidos, total retenido para instituciones y total de haberes.",
        "El total retenido (previsión, salud e impuesto) se entrega a las instituciones correspondientes en los plazos que fija la norma vigente; aquí no se mencionan plazos. El costo total de las remuneraciones para la empresa se estima de ejemplo como la suma de los haberes brutos del mes. En un caso real se agregan otros aportes del empleador que establece la norma vigente.",
        "En el finiquito de ejemplo se suman los conceptos dados: días trabajados pendientes, feriado proporcional e indemnización de ejemplo. Los conceptos reales y su cálculo se consultan en el Código del Trabajo y la norma vigente. Todo cálculo se respalda y se revisa por una segunda persona.",
    ],
    vocab=[("planilla", "tabla de cálculo de remuneraciones por persona"), ("total retenido", "suma de descuentos que se entregan a instituciones"), ("costo para la empresa", "total de haberes brutos más aportes que fije la norma"), ("indemnización de ejemplo", "monto dado para practicar"), ("remuneración pendiente", "días trabajados aún no pagados"), ("segunda revisión", "control por otra persona")],
    worked=[
        ("Líquido de una persona", "Una persona ficticia: base $400.000, descuentos de ejemplo $60.000, impuesto de ejemplo $0. ¿Cuál es el líquido?", ["Líquido = bruto − descuentos − impuesto.", "400.000 − 60.000 − 0 = 340.000."], "$340.000"),
        ("Remuneración pendiente", "Base ficticia $300.000, valor diario ÷ 30 y 7 días pendientes. ¿Cuánto es?", ["Valor diario = 300.000 ÷ 30 = 10.000.", "10.000 × 7 = 70.000."], "$70.000"),
    ],
    mistakes=[("Sumar el impuesto retenido al líquido.", "El impuesto se resta: es una retención.", "Resta el impuesto al calcular el líquido."),
              ("Dar por definitivo el costo estimado para la empresa.", "En un caso real hay otros aportes del empleador.", "Declara que es una estimación y consulta la norma.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué suma el total retenido?", "Los descuentos previsionales, de salud e impuesto", "Solo los bonos", "Los sueldos líquidos", "El total retenido reúne lo que se descuenta para entregar a instituciones."),
        ("=", "{F} ¿Cuántos pesos son los imponibles de B. Araya (base y bono)?", "650000+50000", "Imponibles = base + bono.", " pesos"),
        ("=", "{F} ¿Cuántos pesos retiene la empresa por previsión (10 %) a B. Araya?", "(650000+50000)*10//100", "Descuento = imponibles × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos retiene la empresa por salud (8 %) a B. Araya?", "(650000+50000)*8//100", "Descuento = imponibles × porcentaje ÷ 100.", " pesos"),
        ("=", "{F} ¿Cuál es el líquido de B. Araya (bruto − previsión − salud − impuesto)?", "700000-70000-56000-10000", "Líquido = bruto − descuentos − impuesto.", " pesos"),
        ("=", "{F} ¿Cuál es el líquido de A. Soto (sin bono y sin impuesto)?", "500000-50000-40000-0", "Líquido = bruto − descuentos − impuesto.", " pesos"),
        ("=", "{F} ¿Cuál es el líquido de C. Pérez (base $800.000, bono $100.000)?", "900000-90000-72000-30000", "Líquido = bruto − descuentos − impuesto.", " pesos"),
        ("=", "{F} ¿Cuánto suman los líquidos de las tres personas?", "(500000-50000-40000-0)+(700000-70000-56000-10000)+(900000-90000-72000-30000)", "Se suman los tres líquidos calculados.", " pesos"),
        ("=", "{F} ¿Cuánto suman los haberes brutos de las tres personas (costo estimado de ejemplo)?", "500000+700000+900000", "Se suman los brutos de A, B y C.", " pesos"),
        ("=", "{F} ¿Cuánto es la remuneración pendiente de 12 días de la persona D (base ÷ 30)?", "600000//30*12", "Pendiente = valor diario × días.", " pesos"),
        ("=", "{F} ¿Cuánto es el feriado proporcional de ejemplo de 5 días de D?", "600000//30*5", "Feriado = valor diario × días de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuánto suma el finiquito de ejemplo de D (pendiente, feriado e indemnización de ejemplo)?", "600000//30*12+600000//30*5+250000", "Se suman los tres conceptos de ejemplo.", " pesos"),
        ("abc", "{F} Un compañero dice que ese finiquito de D es el que corresponde a cualquier persona con base $600.000. ¿Qué respondes?", "Es un ejemplo; el real se calcula según el Código del Trabajo y la norma vigente", "Tiene razón", "Se debe pagar la mitad", "Los conceptos y montos reales dependen de cada caso y de la norma vigente."),
    ],
    ctx=("abc", "La gerencia pregunta cuánto dinero debe transferirse a los trabajadores y cuánto se retuvo para entregar a instituciones. ¿Qué dato necesita de la planilla?", "El total de líquidos y el total retenido", "El promedio de la base", "El nombre de las personas", "Esos dos totales responden ambas preguntas de la gerencia."),
    sc=[
        ("En Recursos Humanos: ¿cómo se calcula el líquido?", "Bruto menos descuentos e impuesto", "La retención se resta al bruto."),
        ("¿Qué se hace con el total retenido?", "Se entrega a las instituciones en los plazos de la norma vigente", "Los plazos reales se consultan en la norma."),
        ("¿Por qué una segunda persona revisa la planilla?", "Para detectar errores de suma o de dato", "Un control cruzado reduce los errores."),
    ],
    op=("Con la Ficha 54, arma la planilla del mes para A, B y C con las columnas Imponibles, Previsión, Salud, Impuesto y Líquido, con los totales de líquidos y de lo retenido. Agrega una frase de reserva de los datos y que las cifras son de ejemplo.\n{F}",
        "A: imponibles $500.000, previsión $50.000, salud $40.000, impuesto $0, líquido $410.000. B: $700.000, $70.000, $56.000, $10.000, líquido $564.000. C: $900.000, $90.000, $72.000, $30.000, líquido $708.000. Total líquidos: $1.682.000. Total retenido: $418.000. Las cifras son de ejemplo y la planilla se guarda con acceso restringido.",
        ["calcula cada fila", "suma los totales", "aclara que son cifras de ejemplo", "menciona la reserva"],
        ["planilla de tres filas con totales"],
        ["sumar el impuesto al líquido", "olvidar los totales", "presentar cifras como reales"],
        "Rehace cada fila. Si el total retenido no coincide, pide sumar previsión, salud e impuesto de las tres."),
    reinforce="Arma en papel una planilla de dos personas ficticias con imponibles, un descuento de ejemplo y el líquido.",
    extend="Explica con un ejemplo inventado por qué un total de planilla mal sumado afecta a todo el mes.",
)

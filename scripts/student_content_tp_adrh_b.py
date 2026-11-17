"""Administración, mención Recursos Humanos, 4.º medio TP: OAM-03 (información sobre bienestar y desarrollo de las personas) y OAM-04 (descripción de cargos, reclutamiento e inducción básica). Personas, empresas y cifras inventadas; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, tablas, avisos y pautas están escritos en cada ejercicio: las empresas y las personas son inventadas (se usan iniciales o nombres ficticios) y las cifras son «de ejemplo», "
             "así que no necesitas programas ni internet. Los datos de las personas trabajadoras y de quienes postulan son datos personales reservados: nunca uses datos reales de personas, ni de tu curso ni de tu familia. "
             "Los derechos y obligaciones laborales, la protección de datos personales y las normas contra la discriminación se consultan en el Código del Trabajo y la norma vigente, y con tu docente de la especialidad. "
             "Este cuaderno no entrega asesoría legal ni psicológica personal: ante una situación real de una persona, se deriva a la jefatura o a quien corresponda según la norma vigente.")

build = make_build(MATERIALS)

O3 = "TP-ADRH-4-OAM-03"
O4 = "TP-ADRH-4-OAM-04"

# ============================================================ OAM-03, clase 1
F = ("Ficha 55 (caso ficticio). «Servicios Quillay Ltda.» (60 personas, valor de ejemplo) debe tomar decisiones sobre capacitación y ascensos. La jefa del área de ventas pide al área de Recursos Humanos: "
     "(a) la lista de quiénes están inscritos en el plan de capacitación; (b) cuántas personas tienen evaluación de desempeño del último período; (c) una lista de posibles candidatos a ascenso del área de ventas. "
     "Un jefe de otra área escribe: «Envíame las fichas completas de todo el equipo, con sus problemas de salud y de familia, por si acaso».")
build(
    O3, 1, F,
    use="Aprenderé qué información de bienestar y desarrollo de las personas se ingresa, se archiva y se presenta, para qué sirve a las jefaturas y qué cuidados de privacidad y ética exige.",
    prior=["Sé que los datos personales son reservados.", "Sé qué es un registro y un archivo.", "Sé leer una tabla simple."],
    explain=[
        "La información sobre bienestar y desarrollo de las personas incluye ascensos (paso a un cargo de nivel superior), promociones (avance de carrera por mérito), transferencias (cambio de área o sede), capacitación (formación para mejorar el trabajo), desempeños y evaluaciones (revisión periódica de cómo se cumplen las funciones). Recursos Humanos la ingresa en registros, la archiva con orden y la presenta a las jefaturas para que tomen decisiones fundadas.",
        "Esos datos son personales y algunos son sensibles, como los de salud o familia. Se aplica el principio de lo necesario: se piden, guardan y entregan solo los datos que se necesitan para la decisión. Una jefatura que decide una capacitación necesita saber quién está inscrito y cuántas horas lleva; no necesita los problemas de salud de nadie. La norma vigente sobre protección de datos personales y el Código del Trabajo fijan las reglas; aquí no se citan artículos.",
        "Cuando se presenta información a una jefatura, se prefiere resumirla: totales, porcentajes y listas con los datos mínimos, sin datos sensibles. Las jefaturas ven solo lo de su área. Cada persona puede conocer qué información suya se guarda según la norma vigente. Una solicitud que parece excesiva se consulta con la jefatura de Recursos Humanos antes de responder.",
    ],
    vocab=[("ascenso", "paso a un cargo de nivel superior"), ("promoción", "avance de carrera por mérito"), ("transferencia", "cambio de área o sede"), ("capacitación", "formación para mejorar el trabajo"), ("evaluación de desempeño", "revisión periódica del cumplimiento de funciones"), ("dato sensible", "dato muy íntimo, como salud o familia")],
    worked=[
        ("Dato necesario", "Un jefe ficticio decide quién va a un curso de planillas de cálculo. ¿Necesita saber la enfermedad de un trabajador?", ["No tiene relación con la decisión.", "Solo necesita sus horas y su evaluación."], "No lo necesita"),
        ("Presentar un resumen", "En lugar de enviar 60 fichas, ¿qué puede enviar RR.HH. a una jefatura sobre capacitación?", ["Un resumen con totales y una lista con datos mínimos.", "Sin datos sensibles."], "Un resumen con totales y datos mínimos"),
    ],
    mistakes=[("Enviar a una jefatura la ficha completa de una persona «por si acaso».", "Entrega datos que la decisión no necesita, algunos sensibles.", "Envía solo los datos necesarios."),
              ("Guardar evaluaciones en una carpeta compartida abierta.", "Cualquiera podría leerlas.", "Guárdalas con acceso solo para quienes deben verlas.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es un ascenso?", "El paso a un cargo de nivel superior", "Un cambio de oficina sin cambio de cargo", "Un curso de capacitación", "El ascenso es subir de nivel; el cambio de sede o área es una transferencia."),
        ("abc", "{F} ¿Qué información pide la jefa de ventas en el punto (a)?", "La lista de personas inscritas en el plan de capacitación", "Sus problemas de salud", "El sueldo de todos", "El punto (a) se refiere a quiénes están en el plan."),
        ("abc", "{F} ¿Qué solicitud de la ficha pide datos que NO son necesarios para decidir?", "Las fichas completas con problemas de salud y de familia", "La lista de inscritos en capacitación", "La cantidad de evaluaciones del período", "Los datos de salud y familia no son necesarios para esas decisiones."),
        ("abc", "{F} ¿Qué corresponde responder a esa solicitud?", "Entregar solo lo necesario y consultar a la jefatura de RR.HH. si hay dudas", "Enviar todas las fichas", "Enviar la ficha de una sola persona", "Se aplica el principio de lo necesario."),
        ("=", "{F} Si 60 personas forman la empresa y 45 están inscritas en el plan de capacitación, ¿cuántas no lo están?", "60-45", "No inscritas = total − inscritas.", " personas"),
        ("=", "{F} De las 60 personas, 48 tienen evaluación del último período. ¿Qué porcentaje es?", "48*100//60", "Porcentaje = personas con evaluación × 100 ÷ total.", " %"),
        ("abc", "¿Qué diferencia hay entre transferencia y ascenso?", "La transferencia cambia de área o sede; el ascenso sube de nivel", "Son lo mismo", "La transferencia es un curso", "Cada concepto describe un movimiento distinto."),
        ("abc", "Un jefe pide el expediente completo de una persona para decidir un curso. ¿Qué se le entrega?", "Solo las horas de capacitación y la evaluación relacionadas con la decisión", "Todo el expediente", "Nada, jamás", "Se entrega lo que sirve a la decisión y nada más."),
        ("abc", "Una asistente de RR.HH. deja las evaluaciones sobre su escritorio al irse. ¿Qué corresponde?", "Guardarlas con llave o bajo acceso restringido", "Dejarlas porque nadie entra", "Llevárselas a casa", "Los documentos con datos personales se resguardan."),
        ("abc", "{F} Una persona pregunta qué información suya se guarda. ¿Qué es lo más adecuado?", "Orientarla según la norma vigente y consultar a la jefatura de RR.HH.", "Negarse siempre", "Mostrarle los datos de otras personas", "Se responde conforme a la norma, sin exponer datos de otros."),
        ("abc", "Un jefe quiere conocer el estado de salud de un trabajador para negarle un ascenso. ¿Qué corresponde?", "Rechazar la solicitud y consultar a la jefatura de RR.HH.", "Entregar el dato", "Entregar parte del dato", "La salud no es un criterio y su uso puede ser discriminatorio."),
        ("abc", "{F} ¿Qué es mejor entregar a la jefa de ventas para decidir un candidato?", "Una tabla con horas de capacitación y resultado de evaluación", "Las fichas completas", "Fotos personales", "Se entrega información útil y mínima."),
        ("abc", "¿Cuál es el objetivo de archivar con orden la información de desarrollo?", "Poder encontrar el dato correcto cuando una jefatura lo necesita", "Acumular papeles", "Ocultar información a la persona", "El archivo ordenado permite responder con exactitud."),
    ],
    ctx=("abc", "Una jefatura pregunta cuántas personas de su área han completado la capacitación obligatoria del año. ¿Qué respuesta de RR.HH. es adecuada?", "Un número y una lista de nombres y horas, sin datos personales adicionales", "Las fichas completas de todo el equipo", "No responder", "Se entrega el dato pedido con los datos mínimos."),
    sc=[
        ("En Recursos Humanos: ¿qué principio guía qué datos se entregan?", "Solo los datos necesarios para la decisión", "Lo demás es innecesario y puede ser riesgoso."),
        ("¿Qué diferencia hay entre ascenso y transferencia?", "El ascenso sube de nivel; la transferencia cambia de área o sede", "Cada concepto describe un movimiento distinto de la persona."),
        ("¿Dónde se guardan las evaluaciones?", "Con acceso restringido a quienes deben verlas", "Las evaluaciones contienen datos personales que se resguardan."),
    ],
    op=("Con la Ficha 55, escribe una respuesta de cinco líneas a la jefa de ventas y otra de dos líneas al jefe que pidió las fichas completas. La primera debe responder (a), (b) y (c) con datos mínimos; la segunda debe explicar por qué no se entregan y qué se ofrece en su lugar.\n{F}",
        "A la jefa: te envío la lista de inscritos en el plan de capacitación con sus horas, el número de personas con evaluación del período (48 de 60) y una tabla de candidatos con horas y evaluación, sin datos sensibles. Al otro jefe: no puedo entregar fichas completas con datos de salud o familia, porque no son necesarios; te ofrezco un resumen de capacitación y evaluación de tu área.",
        ["responde (a), (b) y (c)", "entrega solo datos mínimos", "explica el rechazo de la solicitud excesiva", "ofrece una alternativa"],
        ["dos respuestas, una de cinco líneas y otra de dos"],
        ["entregar datos sensibles", "negarse sin ofrecer alternativa", "no responder (b)"],
        "Revisa que no haya datos de salud o de familia. Si las fichas completas se entregan, pide corregir."),
    reinforce="Escribe en papel cuatro datos de una persona ficticia que SÍ se necesitan para decidir una capacitación y cuatro que NO.",
    extend="Explica con un ejemplo inventado cómo un dato sensible mal usado podría perjudicar a una persona.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 56 (documentos y roles de ejemplo, inventados) de «Servicios Quillay Ltda.». Ficha de personal: datos de la persona, cargo, área, fecha de ingreso y movimientos (se guarda con reserva). Plan de capacitación: lista de cursos del año con horas y personas inscritas. "
     "Registro de asistencia a capacitación: quién asistió y cuántas horas. Evaluación de desempeño: formato con criterios y una nota de 1 a 5 (escala de ejemplo). Registro de movimientos: ascensos, promociones y transferencias con fecha y razón. "
     "Roles: encargado(a) de Recursos Humanos (ingresa y archiva); jefatura de área (usa la información para decidir); trabajador(a) (puede conocer su información, según la norma vigente).")
build(
    O3, 2, F,
    use="Aprenderé los documentos y registros de bienestar y desarrollo (ficha de personal, plan de capacitación, evaluación y registro de movimientos) y los roles de quienes los ingresan y los usan.",
    prior=["Conozco los conceptos de ascenso, promoción y transferencia.", "Sé que los datos se entregan según lo necesario.", "Sé leer una tabla."],
    explain=[
        "Recursos Humanos trabaja con documentos de función clara. La ficha de personal reúne los datos básicos de una persona y su historia en la empresa. El plan de capacitación lista los cursos del año con sus horas y las personas inscritas, y el registro de asistencia anota quién asistió y cuántas horas. La evaluación de desempeño usa criterios definidos y una nota; en este cuaderno la escala es de 1 a 5, de ejemplo.",
        "El registro de movimientos anota los ascensos, promociones y transferencias con su fecha y razón. Sirve para ver la trayectoria de una persona y para evitar decisiones sin respaldo. Todos estos registros se ingresan sin errores, se archivan en orden (por persona o por tipo de documento) y se actualizan cuando algo cambia.",
        "Cada rol tiene su responsabilidad: el encargado de Recursos Humanos ingresa y archiva, y cuida que los datos se resguarden; la jefatura de área usa la información de su equipo para decidir; la persona trabajadora puede conocer su información según la norma vigente. Nadie usa los datos para fines distintos de los que se recogieron.",
    ],
    vocab=[("ficha de personal", "documento con datos básicos e historia de una persona"), ("plan de capacitación", "lista de cursos del año con horas e inscritos"), ("registro de asistencia", "anotación de quién asistió y cuántas horas"), ("escala de evaluación", "rango de notas, aquí de 1 a 5"), ("registro de movimientos", "anotación de ascensos, promociones y transferencias"), ("trayectoria", "historia de cargos y movimientos de una persona")],
    worked=[
        ("Elegir el registro", "Se quiere saber cuántas horas de un curso asistió una persona ficticia. ¿Qué registro se consulta?", ["Se trata de asistencia a capacitación.", "Es el registro de asistencia."], "Registro de asistencia a capacitación"),
        ("Orden de archivo", "Las fichas de 30 personas ficticias se archivan por orden alfabético de apellido. ¿Qué se logra?", ["Se ubica una ficha por apellido.", "Se recupera rápido."], "Ubicar fichas rápidamente"),
    ],
    mistakes=[("Usar la evaluación de desempeño de una persona para fines distintos de los que se recogió, como difundirla en el equipo.", "Se rompe la reserva y se pierde la confianza.", "Úsala solo para las decisiones previstas y con acceso restringido."),
              ("No actualizar el registro de movimientos cuando alguien es transferido.", "La información deja de ser fiel y causa errores en decisiones.", "Registra cada movimiento con fecha y razón.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué reúne la ficha de personal?", "Los datos básicos de la persona, su cargo y su historia en la empresa", "Los precios de la empresa", "La lista de clientes", "La ficha reúne datos de la persona y su trayectoria."),
        ("abc", "{F} ¿Qué documento lista los cursos del año, sus horas y los inscritos?", "El plan de capacitación", "La evaluación de desempeño", "La ficha de personal", "El plan de capacitación organiza los cursos."),
        ("abc", "{F} ¿Qué escala usa la evaluación de desempeño de la ficha?", "Una escala de 1 a 5 de ejemplo", "Una escala de 1 a 100", "Solo «sí» o «no»", "La ficha define una escala de ejemplo de 1 a 5."),
        ("abc", "{F} ¿Qué rol ingresa y archiva los registros?", "El encargado o la encargada de Recursos Humanos", "La jefatura de área", "El cliente", "Según la ficha, ese rol ingresa y archiva."),
        ("abc", "{F} ¿Qué rol usa la información para decidir sobre su equipo?", "La jefatura de área", "El proveedor", "El postulante", "La jefatura usa la información de su equipo."),
        ("abc", "¿Para qué sirve el registro de movimientos?", "Para ver la trayectoria de una persona y respaldar decisiones", "Para anotar las vacaciones de la empresa", "Para registrar compras", "Anota ascensos, promociones y transferencias con fecha y razón."),
        ("=", "En un plan de ejemplo hay 4 cursos de 8 horas, 2 cursos de 12 horas. ¿Cuántas horas suma el plan?", "4*8+2*12", "Horas totales = cursos por horas de cada tipo.", " horas"),
        ("=", "Una persona ficticia asistió a 3 cursos de 8 horas y a 1 de 12 horas. ¿Cuántas horas de capacitación suma?", "3*8+12", "Horas = suma de las horas asistidas.", " horas"),
        ("=", "Un curso de ejemplo de 24 horas se dicta en sesiones de 4 horas. ¿Cuántas sesiones son?", "24//4", "Sesiones = horas totales ÷ horas por sesión.", " sesiones"),
        ("abc", "Un registro de asistencia dice que una persona asistió 10 horas de un curso de 8 horas. ¿Qué corresponde?", "Revisar el dato: no puede asistir más horas que las del curso", "Aceptarlo", "Borrar la persona", "Un dato imposible se revisa con el original."),
        ("abc", "{F} Una jefatura quiere conocer las evaluaciones de otra área. ¿Qué corresponde?", "Solo ve las de su área; las otras requieren autorización", "Puede ver todas", "No puede ver ninguna", "Cada jefatura ve lo de su equipo."),
        ("abc", "{F} Un compañero dice que la ficha de personal puede mostrarse en la sala de descanso. ¿Qué respondes?", "No: es reservada y se guarda con acceso restringido", "Sí, para que todos sepan", "Sí, si es solo un rato", "La ficha de personal tiene datos personales reservados."),
        ("abc", "{F} Una persona trabajadora pide ver su evaluación. ¿Qué es lo más adecuado?", "Orientarla conforme a la norma vigente y consultar con la jefatura de RR.HH.", "Negarse sin explicar", "Mostrarle las de sus compañeros", "La persona puede conocer su información, según la norma."),
    ],
    ctx=("abc", "RR.HH. necesita saber cuántas personas han completado 20 horas de capacitación en el año. ¿Qué registros consulta?", "El registro de asistencia a capacitación", "La lista de clientes", "El libro de compras", "El registro de asistencia anota las horas de cada persona."),
    sc=[
        ("En Recursos Humanos: ¿qué anota el registro de asistencia?", "Quién asistió a la capacitación y cuántas horas", "Es la base para medir el cumplimiento."),
        ("¿Qué escala usa este cuaderno para evaluar?", "Una escala de ejemplo de 1 a 5", "Es solo para practicar, no una norma."),
        ("¿Quién puede conocer su información personal?", "La propia persona, según la norma vigente", "La información es suya y la puede conocer."),
    ],
    op=("Con la Ficha 56, arma un cuadro de cinco filas con Documento, Qué contiene, Quién lo ingresa y Quién lo usa. Incluye ficha de personal, plan de capacitación, registro de asistencia, evaluación de desempeño y registro de movimientos. Agrega una regla de reserva de los datos.\n{F}",
        "Ficha de personal: datos básicos y trayectoria; la ingresa RR.HH.; la usa RR.HH. y la jefatura en lo necesario. Plan de capacitación: cursos, horas e inscritos; RR.HH.; la jefatura. Registro de asistencia: asistentes y horas; RR.HH.; RR.HH. y jefatura. Evaluación: criterios y nota de 1 a 5; la jefatura con RR.HH.; la jefatura de área. Registro de movimientos: ascensos, promociones y transferencias; RR.HH.; la jefatura. Regla: acceso restringido.",
        ["describe bien los cinco documentos", "asigna roles según la ficha", "incluye una regla de reserva"],
        ["cuadro de cinco filas y una regla"],
        ["confundir documentos", "olvidar la reserva", "dar acceso a todos"],
        "Compara con la ficha. Si da acceso a todos, pide corregir con la regla de lo necesario."),
    reinforce="Anota en papel el contenido de una ficha de personal ficticia con seis campos.",
    extend="Explica con un ejemplo inventado qué pasa si no se actualiza el registro de movimientos.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 57 (tabla de ejemplo, inventada) del área de ventas y compras de «Servicios Quillay Ltda.», con personas ficticias identificadas por iniciales. Cada fila: persona, área, evaluación de desempeño (escala de ejemplo de 1 a 5), horas de capacitación del año. "
     "L. R., ventas, 5, 24 horas. M. T., ventas, 4, 30 horas. J. A., ventas, 4, 16 horas. C. S., ventas, 4, 22 horas. R. V., compras, 5, 28 horas. F. B., ventas, 3, 12 horas. "
     "Criterios de ejemplo para considerar a una persona de ventas como candidata a ascenso: evaluación de 4 o más y al menos 20 horas de capacitación en el año. La decisión final la toma la jefatura.")
build(
    O3, 3, F,
    use="Aprenderé a analizar una tabla de desempeño y capacitación en papel, aplicar criterios acordados y presentar a la jefatura una lista fundada sin exponer datos innecesarios.",
    prior=["Conozco los registros de desarrollo.", "Sé leer una tabla con varios criterios.", "Sé que las decisiones son de la jefatura."],
    explain=[
        "Para presentar candidatos a ascenso se aplican criterios acordados por la empresa, iguales para todas las personas. Se revisa cada fila de la tabla y se marca si cumple cada criterio. Solo cumple quien cumple todos. Si una persona no cumple un criterio, no queda en la lista aunque cumpla los demás.",
        "Al presentar el resultado a la jefatura se muestra la lista con los datos mínimos que justifican la decisión (en este caso, evaluación y horas) y se aclara que los criterios son una guía: la decisión final es de la jefatura. No se agregan opiniones personales ni datos sensibles. Se identifica a las personas con los datos mínimos necesarios.",
        "Un buen análisis también revisa que los datos sean confiables: las horas deben coincidir con el registro de asistencia y las evaluaciones con el último período. Si algo no cuadra, se corrige antes de presentar. Los criterios deben ser conocidos por las personas y aplicarse sin discriminación.",
    ],
    vocab=[("criterio", "condición que una persona debe cumplir"), ("candidata o candidato", "persona que cumple los criterios"), ("lista fundada", "lista que explica por qué cada persona está en ella"), ("dato mínimo", "dato imprescindible para la decisión"), ("guía", "ayuda para decidir, no una orden"), ("sin discriminación", "con los mismos criterios para todas las personas")],
    worked=[
        ("Aplicar dos criterios", "Criterios ficticios: evaluación 4 o más y 20 horas o más. Una persona tiene evaluación 5 y 18 horas. ¿Cumple?", ["Cumple la evaluación pero no las horas.", "Debe cumplir ambos."], "No cumple"),
        ("Contar candidatos", "En una tabla ficticia, 3 de 8 personas cumplen ambos criterios. ¿Cuántas no cumplen?", ["8 − 3 = 5.", "Cinco personas no cumplen."], "5 personas"),
    ],
    mistakes=[("Incluir en la lista a quien cumple solo uno de los criterios.", "Los criterios son para todas las personas y deben cumplirse todos.", "Marca cada criterio y selecciona a quien cumple todos."),
              ("Agregar opiniones personales sobre alguien en la lista.", "No son criterios y pueden ser discriminatorios.", "Muestra solo los datos que justifican la decisión.")],
    T=[
        ("abc", "En Recursos Humanos: ¿cómo se aplica un criterio de selección?", "Igual para todas las personas", "Distinto según quién sea", "Solo para quienes caen bien", "Un criterio justo es el mismo para todas las personas."),
        ("abc", "{F} ¿Cuántos criterios de ejemplo se aplican en la ficha?", "Dos: evaluación y horas de capacitación", "Uno: solo la evaluación", "Tres", "La ficha fija evaluación de 4 o más y 20 horas o más."),
        ("abc", "{F} ¿Cumple L. R. los criterios?", "Sí, porque tiene evaluación 5 y 24 horas", "No, porque tiene pocas horas", "No, porque su evaluación es baja", "5 supera el 4 y 24 supera las 20 horas."),
        ("abc", "{F} ¿Cumple J. A. los criterios?", "No, porque sus 16 horas son menos de 20", "Sí, porque su evaluación es 4", "Sí, porque es de ventas", "Cumple la evaluación pero no las horas."),
        ("abc", "{F} ¿Cumple R. V. los criterios para el ascenso de ventas?", "No: es del área de compras, no de ventas", "Sí, porque tiene evaluación 5", "Sí, porque tiene 28 horas", "El criterio es para personas de ventas."),
        ("abc", "{F} ¿Cumple F. B. los criterios?", "No: su evaluación es 3 y tiene 12 horas", "Sí, porque trabaja en ventas", "Sí, porque tiene horas", "No cumple ninguno de los dos criterios."),
        ("=", "{F} Si de las 6 personas de la tabla solo R. V. es del área de compras, ¿cuántas son de ventas?", "6-1", "Ventas = personas de la tabla − las de otra área.", " personas"),
        ("=", "{F} Si cumplen ambos criterios 3 personas de las 5 de ventas, ¿cuántas no cumplen?", "5-3", "No cumplen = personas de ventas − cumplen.", " personas"),
        ("=", "{F} ¿Cuántas horas de capacitación suman las 3 personas candidatas (24, 30 y 22 horas)?", "24+30+22", "Se suman las horas de las candidatas.", " horas"),
        ("abc", "{F} ¿Cuáles son las candidatas y los candidatos?", "L. R., M. T. y C. S.", "L. R., J. A. y R. V.", "M. T., J. A. y F. B.", "Solo ellos tienen evaluación 4 o más y al menos 20 horas en ventas."),
        ("abc", "{F} La jefa pregunta si debe ascender a las tres personas. ¿Qué responde RR.HH.?", "Son candidatas según los criterios; la decisión final es de la jefatura", "Debe ascender a las tres", "No debe ascender a nadie", "Los criterios son una guía y decide la jefatura."),
        ("abc", "{F} Un compañero propone agregar a la lista una nota sobre la vida familiar de una persona. ¿Qué corresponde?", "Rechazarlo: no es un criterio y es un dato sensible", "Aceptarlo", "Aceptarlo si es positivo", "La vida familiar no es un criterio y afecta la privacidad."),
        ("abc", "{F} Las horas de J. A. son 16 según la tabla pero el registro de asistencia dice 20. ¿Qué se hace antes de presentar la lista?", "Revisar el registro y corregir el dato", "Usar el que convenga", "Ignorarlo", "Los datos deben coincidir con el registro."),
    ],
    ctx=("abc", "La jefa de ventas pide una lista con los nombres y la razón de cada candidata. ¿Qué entrega RR.HH.?", "Iniciales o nombres, evaluación y horas, sin datos sensibles", "Las fichas completas", "Una opinión personal sobre cada persona", "Se entregan los datos mínimos que justifican la lista."),
    sc=[
        ("En Recursos Humanos: ¿cuántos criterios debe cumplir una candidata?", "Todos los criterios acordados", "Cumplir uno solo de los criterios no basta."),
        ("¿Quién toma la decisión final de ascender?", "La jefatura", "RR.HH. entrega información; decide la jefatura."),
        ("¿Qué datos se agregan a la lista?", "Solo los que justifican la decisión", "Se evitan datos sensibles y opiniones."),
    ],
    op=("Con la Ficha 57, escribe una lista fundada para la jefa de ventas con las candidatas y los candidatos (iniciales, evaluación y horas), la razón por la que cada persona fuera de la lista no cumple y una frase que diga quién decide. Agrega una verificación de datos que harías antes de enviarla.\n{F}",
        "Candidatas y candidatos: L. R. (5; 24 horas), M. T. (4; 30 horas) y C. S. (4; 22 horas). No cumplen: J. A. (16 horas), F. B. (evaluación 3 y 12 horas); R. V. es del área de compras. La decisión final es de la jefatura. Antes de enviarla verificaría las horas con el registro de asistencia.",
        ["aplica los dos criterios", "explica por qué otros no cumplen", "indica que decide la jefatura", "propone una verificación de datos"],
        ["lista fundada de siete líneas"],
        ["incluir a quien cumple un solo criterio", "datos sensibles", "decidir por la jefatura"],
        "Revisa persona por persona. Si agrega datos sensibles, pide quitarlos."),
    reinforce="Aplica en papel dos criterios de ejemplo a una tabla ficticia de cinco personas y marca quién cumple.",
    extend="Explica con un ejemplo inventado por qué un criterio no debe cambiar según la persona.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 58 (datos de ejemplo, inventados) de «Servicios Quillay Ltda.». Resultados de 10 personas ficticias del área de operaciones. Horas de capacitación del año: 20, 25, 10, 30, 18, 22, 15, 20, 12, 28. "
     "Evaluaciones de desempeño (escala de ejemplo de 1 a 5): 5, 4, 3, 5, 4, 4, 3, 5, 3, 4. Meta de capacitación de ejemplo: al menos 20 horas por persona. Movimientos del año: 1 ascenso, 2 transferencias, 3 promociones. "
     "Cada persona se identifica solo con un número de 1 a 10 en la presentación a la jefatura.")
build(
    O3, 4, F,
    use="Aprenderé a calcular indicadores simples de bienestar y desarrollo (promedios, porcentajes de cumplimiento y movimientos) y a presentarlos a una jefatura sin exponer datos personales.",
    prior=["Sé calcular promedios y porcentajes.", "Conozco los registros de desarrollo.", "Sé que se presentan solo datos mínimos."],
    explain=[
        "Un indicador es una medida simple que resume información para decidir. El promedio de horas de capacitación se calcula sumando las horas y dividiendo entre el número de personas. El porcentaje de cumplimiento de la meta se calcula como personas que cumplen × 100 ÷ personas totales. El promedio de evaluación se calcula igual que el de horas.",
        "Los movimientos del año (ascensos, transferencias y promociones) se cuentan y se presentan en un resumen. Al presentar a una jefatura se usan totales y porcentajes, y las personas se identifican con un número o iniciales; no se muestran datos sensibles ni opiniones. Todo se respalda en los registros.",
        "Un buen resumen incluye: qué se midió, cuál fue el resultado, qué significa en una frase y qué decisión puede apoyar. La jefatura decide qué hacer con la información; RR.HH. no toma decisiones por ella.",
    ],
    vocab=[("indicador", "medida simple que resume información"), ("promedio", "suma de valores dividida por la cantidad"), ("porcentaje de cumplimiento", "personas que cumplen × 100 ÷ total"), ("meta", "valor que se quiere alcanzar"), ("resumen", "presentación breve de resultados"), ("identificar con número", "usar un código en vez del nombre")],
    worked=[
        ("Promedio", "Cuatro personas ficticias tienen 10, 20, 30 y 40 horas de capacitación. ¿Cuál es el promedio?", ["Suma: 100.", "100 ÷ 4 = 25."], "25 horas"),
        ("Cumplimiento", "De 5 personas ficticias, 4 cumplen la meta. ¿Qué porcentaje cumple?", ["4 × 100 ÷ 5 = 80.", "Se expresa en porcentaje."], "80 %"),
    ],
    mistakes=[("Calcular el promedio dividiendo por un número de personas distinto del total.", "El promedio queda mal.", "Divide entre el número real de personas."),
              ("Mostrar los nombres completos en una presentación que solo pide totales.", "Se expone innecesariamente a las personas.", "Usa números o iniciales y totales.")],
    T=[
        ("abc", "En Recursos Humanos: ¿cómo se calcula el promedio de horas?", "Suma de horas dividida por el número de personas", "Horas por personas", "Mayor menos menor", "El promedio reparte el total entre las personas."),
        ("=", "{F} ¿Cuántas horas suman las 10 personas?", "20+25+10+30+18+22+15+20+12+28", "Se suman las horas de las 10 personas.", " horas"),
        ("=", "{F} ¿Cuál es el promedio de horas por persona?", "200//10", "Promedio = suma ÷ cantidad de personas.", " horas"),
        ("abc", "{F} ¿Cuántas personas cumplen la meta de al menos 20 horas?", "6", "5", "7", "Cumplen 20, 25, 30, 22, 20 y 28 horas."),
        ("=", "{F} ¿Qué porcentaje de las 10 personas cumple la meta?", "6*100//10", "Porcentaje = cumplen × 100 ÷ total.", " %"),
        ("=", "{F} ¿Cuántas personas no cumplen la meta?", "10-6", "No cumplen = total − cumplen.", " personas"),
        ("=", "{F} ¿Cuál es la suma de las 10 evaluaciones?", "5+4+3+5+4+4+3+5+3+4", "Se suman las evaluaciones de ejemplo.", " puntos"),
        ("=", "{F} ¿Cuál es el promedio de evaluación?", "40//10", "Promedio = suma ÷ cantidad de personas.", " puntos"),
        ("=", "{F} ¿Cuántos movimientos hubo en el año (ascensos, transferencias y promociones)?", "1+2+3", "Total = suma de los tres tipos de movimiento.", " movimientos"),
        ("abc", "{F} ¿Qué conclusión simple apoya el 60 % de cumplimiento?", "Que 4 de cada 10 personas no alcanzaron la meta y se puede reforzar la capacitación", "Que todos cumplen", "Que nadie cumple", "El 60 % indica que una parte importante no alcanzó la meta."),
        ("abc", "{F} ¿Cómo se identifican las personas en la presentación a la jefatura?", "Con un número de 1 a 10", "Con su nombre completo y su dirección", "Con una foto", "La ficha indica que se identifican solo con un número."),
        ("abc", "{F} La jefatura pide agregar los diagnósticos de salud para «entender mejor». ¿Qué corresponde?", "Rechazarlo: son datos sensibles y no son necesarios", "Agregarlos", "Agregar solo los más graves", "Los datos sensibles no se entregan sin necesidad ni autorización."),
        ("abc", "{F} Un asistente propone presentar solo el 100 % de personas con evaluación de 4 o más, aunque es 70 %. ¿Qué respondes?", "Hay que presentar el dato real; alterarlo es una falta ética", "Es mejor dar un número alto", "Es válido si nadie lo revisa", "Los indicadores deben ser fieles a los registros."),
    ],
    ctx=("abc", "La jefatura de operaciones pregunta cómo le fue a su equipo en capacitación. ¿Qué respuesta resumida entrega RR.HH.?", "Promedio de 20 horas y 60 % de cumplimiento de la meta, con personas identificadas por número", "Todas las fichas personales", "No hay datos", "Se entrega un resumen con totales y sin datos personales."),
    sc=[
        ("En Recursos Humanos: ¿cómo se calcula el porcentaje de cumplimiento?", "Personas que cumplen por cien dividido por el total", "Compara los que cumplen con el total."),
        ("¿Cómo se calcula un promedio?", "Se suman los valores y se divide por la cantidad", "El promedio resume varios datos en uno."),
        ("¿Cómo se presentan las personas en un resumen?", "Con números o iniciales, sin datos innecesarios", "Con ello se protege la privacidad de las personas."),
    ],
    op=("Con la Ficha 58, escribe un resumen de seis líneas para la jefatura: promedio de horas, porcentaje de cumplimiento, promedio de evaluación, movimientos del año, una conclusión y una decisión que podría apoyar. Identifica a las personas solo con números.\n{F}",
        "Promedio de capacitación: 20 horas. Cumplimiento de la meta: 60 % (6 de 10). Evaluación promedio: 4 sobre 5. Movimientos del año: 6 (1 ascenso, 2 transferencias, 3 promociones). Conclusión: cuatro personas (las 3, 5, 9 y 7) no alcanzaron la meta. Decisión que apoya: reforzar la capacitación de esas personas. No se incluyen datos sensibles.",
        ["calcula los indicadores", "identifica a las personas con números", "da una conclusión y una decisión posible", "no incluye datos sensibles"],
        ["resumen de seis líneas"],
        ["alterar un indicador", "mostrar nombres completos", "incluir datos sensibles"],
        "Rehace los cálculos con la ficha. Si el resumen incluye datos sensibles, pide quitarlos."),
    reinforce="Calcula en papel el promedio y el porcentaje de cumplimiento de una lista ficticia de ocho valores.",
    extend="Explica con un ejemplo inventado cómo un indicador puede ayudar a una jefatura a decidir un curso.",
)

# ============================================================ OAM-04, clase 1
F = ("Ficha 59 (caso ficticio). «Servicios Quillay Ltda.» necesita contratar un o una auxiliar administrativo para el área de operaciones. La jefatura del área pide a Recursos Humanos: "
     "(1) escribir la descripción del cargo; (2) publicar un aviso para recibir postulaciones; (3) preparar la bienvenida de la persona contratada. Un borrador de aviso dice: «Se busca joven de buena presencia, sin hijos, para trabajar de lunes a sábado».")
build(
    O4, 1, F,
    use="Aprenderé qué son la descripción de cargos, el reclutamiento y la inducción básica, cómo se relacionan con las necesidades de la empresa y qué cuidados éticos y de privacidad se aplican.",
    prior=["Sé qué es un cargo y una función.", "Sé que los datos personales son reservados.", "Sé qué es un contrato."],
    explain=[
        "La descripción de cargos es el trabajo de escribir, de manera ordenada, qué hace un cargo dentro de la empresa: su nombre, su objetivo, sus funciones, de quién depende y qué requisitos necesita. Sirve para que todos entiendan qué se espera del cargo. El reclutamiento es el proceso de dar a conocer la oferta y recibir postulaciones. La inducción básica es la bienvenida y la orientación inicial de la persona que ingresa.",
        "Estas tareas se hacen de manera sistemática, es decir, siguiendo pasos y formatos definidos por la empresa y por la norma vigente. Los avisos deben ser veraces y no pueden discriminar: no se pide ni se excluye por motivos como edad, apariencia o situación familiar; se piden requisitos relacionados con el cargo. La norma vigente y el Código del Trabajo fijan las reglas contra la discriminación.",
        "Se resguardan los datos de quienes postulan: se usan solo para el proceso y se guardan con reserva. Una persona que postula puede preguntar cómo se tratarán sus datos y se le responde con claridad. Quien tiene dudas consulta a la jefatura de Recursos Humanos.",
    ],
    vocab=[("descripción de cargo", "documento que dice qué hace un cargo"), ("reclutamiento", "proceso de recibir postulaciones"), ("inducción", "bienvenida y orientación inicial de quien ingresa"), ("aviso de empleo", "publicación que invita a postular"), ("requisito", "condición relacionada con el cargo"), ("discriminación", "trato desigual por motivos sin relación con el cargo")],
    worked=[
        ("Requisito válido", "Para un cargo de bodeguero ficticio, ¿es válido pedir experiencia en control de existencias?", ["Está relacionada con el cargo.", "Es un requisito válido."], "Sí, es válido"),
        ("Requisito inválido", "¿Es válido pedir que sea «joven de buena presencia»?", ["No tiene relación con las funciones.", "Puede discriminar."], "No, discrimina"),
    ],
    mistakes=[("Escribir en el aviso que se busca a alguien «sin hijos».", "Es discriminatorio y no se relaciona con las funciones.", "Pide requisitos del cargo, no condiciones personales."),
              ("Guardar los currículos de postulantes en una carpeta abierta para todos.", "Se exponen datos personales.", "Guárdalos con acceso restringido y úsalos solo para el proceso.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es una descripción de cargo?", "Un documento que dice qué hace un cargo y qué requisitos tiene", "La lista de sueldos", "El plano de la oficina", "La descripción de cargo ordena funciones y requisitos."),
        ("abc", "{F} ¿Qué pide la jefatura en el punto (2)?", "Publicar un aviso para recibir postulaciones", "Escribir el contrato", "Despedir a alguien", "El punto (2) es el reclutamiento."),
        ("abc", "{F} ¿Qué es la inducción básica?", "La bienvenida y la orientación inicial de la persona que ingresa", "El pago del primer sueldo", "La evaluación de despido", "La inducción orienta a la persona nueva."),
        ("abc", "{F} ¿Qué frase del borrador de aviso es discriminatoria?", "«Joven de buena presencia, sin hijos»", "«Para trabajar en el área de operaciones»", "«Auxiliar administrativo»", "Edad, apariencia y situación familiar no se relacionan con las funciones."),
        ("abc", "¿Qué tipo de requisito es adecuado en un aviso para un auxiliar administrativo?", "Manejar planillas básicas y buena atención de público", "Tener cierta edad", "Estar soltero", "Un requisito válido se relaciona con las funciones."),
        ("abc", "¿Para qué sirve describir el cargo antes de publicar el aviso?", "Para que el aviso y la selección se basen en lo que realmente hace el cargo", "Para tener más papeles", "Para esconder las funciones", "Un buen aviso parte de una descripción clara."),
        ("=", "En un proceso de ejemplo llegaron 45 postulaciones y 9 cumplen los requisitos mínimos. ¿Cuántas no cumplen?", "45-9", "No cumplen = total − cumplen.", " postulaciones"),
        ("=", "De esas 45 postulaciones de ejemplo, 9 cumplen los requisitos. ¿Qué porcentaje cumple?", "9*100//45", "Porcentaje = cumplen × 100 ÷ total.", " %"),
        ("abc", "{F} Un jefe sugiere dejar el aviso tal como está porque «así se entiende». ¿Qué respondes?", "Hay que reescribirlo con requisitos del cargo, sin discriminar", "Dejarlo", "Agregar más condiciones personales", "El aviso debe respetar la norma y no discriminar."),
        ("abc", "Una persona que postuló pregunta cómo se usarán sus datos. ¿Qué es lo más adecuado?", "Explicarle con claridad que se usan solo para el proceso y se guardan con reserva", "No responderle", "Decirle que se publican", "Quien postula tiene derecho a una respuesta clara."),
        ("abc", "{F} Una compañera de RR.HH. comenta en una conversación abierta quién postuló. ¿Qué falla?", "Rompe la reserva de los datos de las personas postulantes", "Nada, porque son pocos", "Falta una firma", "Los datos de postulantes son reservados."),
        ("abc", "{F} Antes de publicar el aviso, ¿qué debe hacer RR.HH. con la descripción del cargo?", "Revisarla con la jefatura para confirmar que refleja lo que se necesita", "Publicarla sin revisar", "Borrarla", "La jefatura confirma funciones y requisitos."),
        ("abc", "{F} Para un cargo con jornada de lunes a sábado, ¿qué corresponde en el aviso?", "Indicar la jornada tal como se pactará, según la norma vigente", "Ocultar la jornada", "Cambiarla después sin avisar", "Los avisos de empleo deben ser veraces y claros."),
    ],
    ctx=("abc", "RR.HH. recibe 45 currículos de postulantes. ¿Cómo debe guardarlos?", "Con acceso restringido y solo para el proceso", "En un computador abierto a todos", "En una red social", "Los datos de postulantes se resguardan."),
    sc=[
        ("En Recursos Humanos: ¿qué debe cumplir un aviso de empleo?", "Ser veraz y no discriminar", "Pide requisitos relacionados con el cargo."),
        ("¿Para qué sirve la inducción?", "Para orientar a la persona que ingresa", "Facilita su integración y su seguridad."),
        ("¿Qué se hace con los datos de quienes postulan?", "Se usan solo para el proceso y se guardan con reserva", "Los datos de quienes postulan son datos personales."),
    ],
    op=("Con la Ficha 59, reescribe el aviso en cinco líneas sin discriminar: cargo, funciones, requisitos relacionados con el cargo, jornada y cómo postular (inventa un correo ficticio con la forma nombre@ejemplo.cl). Agrega una línea sobre cómo se cuidarán los datos de quienes postulan.\n{F}",
        "Se busca auxiliar administrativo(a). Funciones: apoyar el registro de documentos y la atención de consultas. Requisitos: manejo básico de planillas y buena atención de público. Jornada: según lo pactado en el contrato. Postular a empleos@ejemplo.cl. Los datos se usan solo para el proceso y se guardan con reserva.",
        ["no discrimina", "usa requisitos del cargo", "es veraz sobre la jornada", "cuida los datos de postulantes"],
        ["aviso reescrito de cinco líneas"],
        ["mantener requisitos personales", "ocultar la jornada", "no mencionar los datos"],
        "Compara con la ficha. Si queda algún requisito de edad, apariencia o familia, pide quitarlo."),
    reinforce="Escribe en papel tres requisitos válidos y tres inválidos para un cargo de recepcionista ficticio.",
    extend="Explica con un ejemplo inventado cómo un aviso discriminatorio puede perjudicar a la empresa.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 60 (formatos de ejemplo, inventados) de «Servicios Quillay Ltda.». Descriptor de cargo: nombre del cargo, objetivo, funciones, requisitos, jefatura de la que depende, jornada y lugar. Perfil: conocimientos, habilidades y actitudes relacionados con las funciones. "
     "Aviso de empleo: cargo, funciones, requisitos, jornada, cómo postular y cuidado de datos. Planilla de postulaciones: número, fecha, cargo y si cumple requisitos mínimos (sí o no). Pauta de entrevista: preguntas iguales para todas las personas y puntajes. "
     "Plan de inducción: actividades del primer día y de la primera semana, responsable y tiempo. Roles: encargado(a) de RR.HH., jefatura del área, persona guía (compañero(a) que acompaña a quien ingresa).")
build(
    O4, 2, F,
    use="Aprenderé los documentos del reclutamiento y la inducción (descriptor, perfil, aviso, planilla, pauta y plan de inducción) y el rol de cada persona.",
    prior=["Sé que un aviso no debe discriminar.", "Sé qué es un cargo.", "Sé qué es una función."],
    explain=[
        "El descriptor de cargo reúne el nombre del cargo, su objetivo, sus funciones, los requisitos, de quién depende, la jornada y el lugar. El perfil agrega los conocimientos, habilidades y actitudes relacionados con las funciones. A partir de ellos se escribe el aviso de empleo con información veraz y clara.",
        "En el reclutamiento se usa una planilla de postulaciones para registrar a cada persona que postula y si cumple los requisitos mínimos. Para entrevistar se usa una pauta con preguntas iguales para todas las personas y puntajes definidos de antemano, de modo que la comparación sea justa. Los datos de las personas postulantes son reservados.",
        "La inducción básica usa un plan con actividades del primer día y de la primera semana: bienvenida, presentación del equipo, recorrido, entrega de información de seguridad y de funciones, y una persona guía. Cada rol tiene su responsabilidad: RR.HH. organiza el proceso, la jefatura del área define el cargo y recibe a la persona, y la persona guía acompaña. La seguridad en el trabajo se explica según la norma vigente y quien corresponda.",
    ],
    vocab=[("descriptor de cargo", "documento con nombre, objetivo, funciones y requisitos"), ("perfil", "conocimientos, habilidades y actitudes que pide el cargo"), ("planilla de postulaciones", "registro de quienes postulan"), ("pauta de entrevista", "preguntas iguales para todas las personas, con puntajes"), ("plan de inducción", "actividades de bienvenida y orientación"), ("persona guía", "quien acompaña a la persona que ingresa")],
    worked=[
        ("Elegir el documento", "Se quiere registrar quién postuló y si cumple los requisitos mínimos. ¿Qué documento se usa?", ["Se registran postulantes.", "Es la planilla de postulaciones."], "Planilla de postulaciones"),
        ("Pauta justa", "Una pauta ficticia hace preguntas distintas a cada persona. ¿Es justa?", ["Las preguntas deben ser iguales.", "No es justa."], "No es justa"),
    ],
    mistakes=[("Hacer preguntas distintas a cada persona entrevistada.", "No se puede comparar de forma justa.", "Usa una pauta con preguntas iguales y puntajes definidos."),
              ("Dejar a la persona nueva sola el primer día.", "No conoce al equipo ni las normas de seguridad.", "Usa el plan de inducción y una persona guía.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué reúne un descriptor de cargo?", "Nombre, objetivo, funciones, requisitos, jefatura, jornada y lugar", "Solo el sueldo", "La lista de clientes", "El descriptor ordena la información del cargo."),
        ("abc", "{F} ¿Qué documento tiene preguntas iguales para todas las personas con puntajes?", "La pauta de entrevista", "El aviso de empleo", "El descriptor de cargo", "La pauta permite comparar de forma justa."),
        ("abc", "{F} ¿Qué documento registra a cada persona que postula?", "La planilla de postulaciones", "El plan de inducción", "El perfil", "La planilla registra a las personas postulantes."),
        ("abc", "{F} ¿Qué documento organiza las actividades del primer día de la persona nueva?", "El plan de inducción", "La pauta de entrevista", "El aviso de empleo", "El plan de inducción ordena la bienvenida."),
        ("abc", "{F} ¿Quién acompaña a la persona que ingresa?", "La persona guía", "El postulante rechazado", "El cliente", "Según la ficha, la persona guía acompaña."),
        ("abc", "{F} ¿Qué rol define el cargo y recibe a la persona nueva?", "La jefatura del área", "El proveedor", "La persona guía", "La ficha asigna a la jefatura del área definir el cargo y recibir."),
        ("=", "El plan de inducción de ejemplo del primer día tiene 30 minutos de bienvenida, 45 de recorrido, 60 de seguridad y 45 de funciones. ¿Cuántos minutos suma?", "30+45+60+45", "Minutos totales = suma de las actividades.", " minutos"),
        ("=", "Ese plan de ejemplo suma 180 minutos. ¿Cuántas horas son?", "180//60", "Horas = minutos ÷ 60.", " horas"),
        ("=", "La planilla de ejemplo tiene 30 postulaciones; 12 cumplen los requisitos mínimos. ¿Cuántas no cumplen?", "30-12", "No cumplen = total − cumplen.", " postulaciones"),
        ("abc", "Una pauta de entrevista pregunta por el número de hijos de la persona. ¿Qué corresponde?", "Quitar la pregunta, porque discrimina y no se relaciona con el cargo", "Dejarla", "Hacerla solo a mujeres", "Las preguntas deben estar relacionadas con el cargo."),
        ("abc", "Alguien entrevista a una persona sin pauta y le pregunta lo que se le ocurre. ¿Qué falla?", "No hay una comparación justa entre las personas", "Nada, es más natural", "Falta un chiste", "La pauta asegura el mismo trato a todas."),
        ("abc", "{F} Un currículo con datos de contacto se pierde en una mesa común. ¿Qué es lo más adecuado?", "Avisar a RR.HH. y resguardar los currículos con acceso restringido", "Ignorarlo", "Publicarlo", "Los datos de postulantes son reservados."),
        ("abc", "{F} ¿Qué parte del plan de inducción se refiere a la seguridad?", "Una actividad que explica la información de seguridad, según la norma vigente", "El almuerzo", "La entrega del uniforme", "La seguridad se explica desde el primer día."),
    ],
    ctx=("abc", "Una persona nueva llega mañana. ¿Qué documento prepara RR.HH. para ordenar su primer día?", "El plan de inducción", "La planilla de postulaciones", "El aviso de empleo", "El plan de inducción ordena su bienvenida."),
    sc=[
        ("En Recursos Humanos: ¿para qué sirve la pauta de entrevista?", "Para comparar de forma justa a las personas con las mismas preguntas", "Así se asegura el mismo trato para todas las personas."),
        ("¿Qué incluye el plan de inducción?", "Actividades, responsable y tiempo del primer día y de la primera semana", "El plan organiza la bienvenida de la persona nueva."),
        ("¿Quién acompaña a la persona nueva?", "La persona guía", "Orienta a la persona nueva y resuelve sus dudas iniciales."),
    ],
    op=("Con la Ficha 60, arma un descriptor de cargo de seis líneas para «recepcionista» de una empresa ficticia, con nombre, objetivo, funciones, requisitos, jefatura y jornada. Todos los requisitos deben relacionarse con el cargo.\n{F}",
        "Cargo: recepcionista. Objetivo: atender a las personas que llegan y dirigir sus consultas. Funciones: recibir visitas, registrar llegadas, responder el teléfono. Requisitos: buena atención de público y manejo básico de planillas. Depende de: jefatura de administración. Jornada: según lo pactado en el contrato.",
        ["incluye los seis elementos", "requisitos relacionados con el cargo", "no discrimina"],
        ["descriptor de seis líneas"],
        ["requisitos personales", "omitir funciones", "inventar normas"],
        "Revisa que todos los requisitos sean del cargo. Si hay uno personal, pide quitarlo."),
    reinforce="Escribe en papel tres preguntas válidas para una entrevista de recepcionista ficticio.",
    extend="Explica con un ejemplo inventado cómo una pauta de entrevista evita un trato desigual.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 61 (caso de ejemplo, inventado) de «Servicios Quillay Ltda.». Descriptor de cargo deficiente del puesto «auxiliar de bodega»: «Funciones: ayudar. Requisitos: persona de buen carácter, hombre menor de 30 años, con experiencia. Jornada: según se necesite». "
     "Pauta de entrevista de ejemplo (puntaje máximo por criterio): experiencia relacionada, 40 puntos; conocimientos de control de existencias, 30 puntos; actitud de trabajo en equipo, 30 puntos. "
     "Resultados de tres personas postulantes ficticias identificadas como P1, P2 y P3: P1, experiencia 30, conocimientos 20, actitud 25; P2, experiencia 40, conocimientos 25, actitud 20; P3, experiencia 20, conocimientos 30, actitud 30.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un descriptor deficiente, corregir requisitos y aplicar una pauta de entrevista con puntajes para comparar postulaciones de forma justa y reservada.",
    prior=["Conozco el descriptor, el perfil y la pauta.", "Sé sumar puntajes.", "Sé que no se discrimina."],
    explain=[
        "Analizar un descriptor es verificar que cada parte sea clara, específica y relacionada con el cargo. «Ayudar» no dice qué se hace; «persona de buen carácter» es subjetivo; «hombre menor de 30 años» discrimina por sexo y edad; «según se necesite» no define la jornada. Se corrige reemplazándolos por funciones concretas, requisitos medibles y la jornada que se pactará según la norma vigente.",
        "Al comparar postulantes se usa la pauta con puntajes por criterio, iguales para todas las personas. El puntaje total es la suma de los puntajes de cada criterio. Se ordena de mayor a menor y se informa a la jefatura, que decide. Las diferencias pequeñas pueden no ser significativas; se explica el criterio y se evita basarse en impresiones personales.",
        "El resultado se comunica con cuidado: solo a quienes deben decidir y sin datos personales innecesarios. A las personas postulantes se les responde con respeto y claridad, sin mostrar datos de otras personas.",
    ],
    vocab=[("criterio medible", "requisito que puede verificarse"), ("subjetivo", "que depende de la opinión de cada persona"), ("puntaje total", "suma de los puntajes de los criterios"), ("pauta con puntajes", "formato con criterios y puntos máximos"), ("corregir", "reemplazar una parte deficiente por otra adecuada"), ("comparación justa", "las mismas condiciones para todas las personas")],
    worked=[
        ("Puntaje total", "Una persona ficticia obtiene 30, 20 y 25 puntos en tres criterios. ¿Cuál es su puntaje total?", ["30 + 20 + 25.", "Resulta 75."], "75 puntos"),
        ("Corregir un requisito", "El requisito «de buen carácter» es subjetivo. ¿Cómo se corrige?", ["Se cambia por una conducta observable.", "Por ejemplo, «trabaja en equipo» con ejemplos."], "Cambiarlo por una conducta observable"),
    ],
    mistakes=[("Dejar como requisito «persona de buen carácter».", "Es subjetivo y no se puede comprobar.", "Usa conductas observables y relacionadas con el cargo."),
              ("Elegir según la simpatía personal y no según la pauta.", "Se rompe la comparación justa.", "Usa los puntajes y justifica la decisión.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué problema tiene la función «ayudar»?", "No dice qué se hace en el cargo", "Es demasiado específica", "Es discriminatoria", "Una función debe describir una tarea concreta."),
        ("abc", "{F} ¿Qué requisito del descriptor discrimina?", "«Hombre menor de 30 años»", "«Con experiencia»", "«Persona de buen carácter»", "Sexo y edad no se relacionan con las funciones."),
        ("abc", "{F} ¿Por qué «según se necesite» es un problema en la jornada?", "No define la jornada que se pactará", "Es demasiado exacta", "Es una ley", "La jornada debe ser clara y veraz."),
        ("abc", "{F} ¿Por qué «persona de buen carácter» es un requisito débil?", "Es subjetivo y no se puede comprobar", "Es un requisito legal", "Es medible", "No hay una forma objetiva de verificarlo."),
        ("=", "{F} ¿Cuál es el puntaje total de P1?", "30+20+25", "Total = suma de los puntajes de los tres criterios.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de P2?", "40+25+20", "Total = suma de los puntajes de los tres criterios.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de P3?", "20+30+30", "Total = suma de los puntajes de los tres criterios.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje máximo posible de la pauta?", "40+30+30", "Máximo = suma de los puntos máximos.", " puntos"),
        ("abc", "{F} ¿Quién tiene el puntaje total más alto?", "P2, con 85 puntos", "P1, con 75 puntos", "P3, con 80 puntos", "P2 suma 85, P3 suma 80 y P1 suma 75."),
        ("abc", "{F} ¿Qué corresponde hacer con el resultado?", "Entregarlo a la jefatura con el detalle de la pauta para que decida", "Contratar a P2 sin consultar", "Publicar los puntajes", "RR.HH. informa y la jefatura decide."),
        ("abc", "{F} Un jefe sugiere contratar a P1 «porque cae simpático» aunque tiene menos puntaje. ¿Qué respondes?", "Se debe justificar con la pauta y los criterios; la simpatía no es un criterio", "Está bien, la simpatía importa", "Elige a P3", "La pauta busca decisiones justas y verificables."),
        ("abc", "{F} P3 pregunta por el puntaje de P2. ¿Qué corresponde?", "No entregarlo: es dato de otra persona", "Entregarlo", "Entregar solo la mitad", "Los datos de otras personas son reservados."),
        ("abc", "{F} ¿Cómo se podría reescribir mejor la función «ayudar»?", "«Recibir, registrar y ordenar mercaderías en la bodega»", "«Hacer lo que le pidan»", "«Estar disponible siempre»", "Una función concreta nombra la tarea."),
    ],
    ctx=("abc", "La jefa pregunta por qué se eligió a P2 y no a P3. ¿Qué respuesta fundada entrega RR.HH.?", "P2 obtuvo 85 puntos en la pauta y P3 80, con los mismos criterios", "Porque P2 cae mejor", "Porque lo decidió el azar", "Se fundamenta en los puntajes de una pauta igual para todos."),
    sc=[
        ("En Recursos Humanos: ¿qué es un criterio subjetivo?", "Uno que depende de la opinión de cada persona", "No se puede comprobar con hechos."),
        ("¿Cómo se calcula el puntaje total?", "Sumando los puntajes de cada criterio", "Cada criterio aporta puntos al total de la persona."),
        ("¿Se entregan los puntajes de una persona a otra postulante?", "No, son datos reservados", "Solo se entregan a quien decide."),
    ],
    op=("Con la Ficha 61, reescribe el descriptor del «auxiliar de bodega» en cinco líneas (funciones concretas, requisitos medibles sin discriminar y jornada según lo pactado) y escribe después el orden de las tres personas postulantes con sus puntajes totales y una frase que diga quién decide.\n{F}",
        "Cargo: auxiliar de bodega. Funciones: recibir mercaderías, registrar entradas y ordenar productos. Requisitos: experiencia en bodega y conocimientos básicos de control de existencias. Jornada: según lo pactado en el contrato. Orden: P2, 85; P3, 80; P1, 75. Decide la jefatura con el detalle de la pauta.",
        ["reescribe sin discriminar", "funciones concretas", "calcula los puntajes", "indica quién decide"],
        ["descriptor y orden de postulantes"],
        ["mantener requisitos personales", "cálculo incorrecto de puntajes", "decidir por la jefatura"],
        "Rehace los puntajes. Si queda algún requisito de sexo o edad, pide quitarlo."),
    reinforce="Reescribe en papel dos requisitos subjetivos de un descriptor ficticio en requisitos medibles.",
    extend="Explica con un ejemplo inventado cómo cambiaría el orden si el criterio de experiencia valiera 20 puntos y no 40.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 62 (datos de ejemplo, inventados) de «Servicios Quillay Ltda.». Proceso de reclutamiento de ejemplo para un cargo: llegaron 60 postulaciones; 24 cumplen los requisitos mínimos; se entrevista a 8; se selecciona a 1 persona. "
     "Pauta con puntajes máximos: experiencia, 40; conocimientos, 30; actitud, 30. Postulantes finalistas ficticios: Q1 obtuvo 35, 25 y 20 puntos; Q2, 30, 30 y 30; Q3, 40, 20 y 25. "
     "Plan de inducción de ejemplo del primer día: bienvenida de 30 minutos; presentación del equipo de 30 minutos; recorrido de 45 minutos; información de seguridad de 60 minutos (según la norma vigente y quien corresponda); firma y entrega de documentos de 30 minutos; funciones del cargo de 45 minutos.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar el proceso completo con datos de ejemplo: embudo de postulaciones, puntajes, comparación justa y plan de inducción del primer día con sus tiempos.",
    prior=["Sé calcular porcentajes y puntajes totales.", "Conozco el plan de inducción.", "Sé que la jefatura decide."],
    explain=[
        "Un proceso de reclutamiento se puede mirar como un embudo: llegan muchas postulaciones, algunas cumplen los requisitos mínimos, menos personas pasan a entrevista y solo una se selecciona. Se calcula qué porcentaje pasa de una etapa a la otra para evaluar el proceso. La selección se apoya en la pauta con puntajes iguales para todas las personas.",
        "La comparación justa suma los puntajes de cada finalista y los ordena de mayor a menor. Si dos personas empatan, se usa un criterio de desempate fijado antes del proceso, como el puntaje en el criterio de mayor peso. La jefatura decide y se informa de forma respetuosa a las personas no seleccionadas, sin dar datos de otras.",
        "El plan de inducción asigna tiempo a cada actividad. La suma de los tiempos debe caber en la jornada del primer día, con descansos. La información de seguridad se entrega según la norma vigente y por quien corresponda. Este cuaderno no reemplaza la capacitación de seguridad.",
    ],
    vocab=[("embudo de reclutamiento", "etapas en que se reduce el número de personas"), ("desempate", "criterio fijado antes para resolver empates"), ("finalista", "persona que llega a la última etapa"), ("tasa de paso", "porcentaje que pasa de una etapa a otra"), ("tiempo asignado", "duración de cada actividad"), ("jornada del primer día", "tiempo total de trabajo del primer día")],
    worked=[
        ("Tasa de paso", "De 40 postulaciones ficticias, 10 pasan a entrevista. ¿Qué porcentaje es?", ["10 × 100 ÷ 40 = 25.", "Se expresa en porcentaje."], "25 %"),
        ("Suma de tiempos", "Un plan ficticio tiene actividades de 20, 40 y 30 minutos. ¿Cuánto dura?", ["20 + 40 + 30.", "Resulta 90."], "90 minutos"),
    ],
    mistakes=[("Usar un criterio de desempate inventado después de ver los resultados.", "Parece una decisión arbitraria.", "Define el desempate antes del proceso."),
              ("Programar el primer día con más actividades de las horas disponibles.", "La persona queda agotada y no recibe bien la información.", "Suma los tiempos y deja descansos.")],
    T=[
        ("abc", "En Recursos Humanos: ¿qué es la tasa de paso?", "El porcentaje que pasa de una etapa a la siguiente", "El sueldo inicial", "El horario de entrada", "Mide cuánto del grupo avanza entre etapas."),
        ("=", "{F} ¿Qué porcentaje de las 60 postulaciones cumple los requisitos mínimos (24)?", "24*100//60", "Porcentaje = cumplen × 100 ÷ total.", " %"),
        ("=", "{F} ¿Qué porcentaje de las 24 que cumplen pasa a entrevista (8)?", "8*100//24", "Porcentaje = pasan × 100 ÷ cumplen, parte entera.", " %"),
        ("=", "{F} ¿Cuántas postulaciones no cumplieron los requisitos mínimos?", "60-24", "No cumplen = total − cumplen.", " postulaciones"),
        ("=", "{F} ¿Cuál es el puntaje total de Q1?", "35+25+20", "Total = suma de los tres puntajes.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de Q2?", "30+30+30", "Total = suma de los tres puntajes.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de Q3?", "40+20+25", "Total = suma de los tres puntajes.", " puntos"),
        ("abc", "{F} ¿Quién tiene el puntaje total más alto entre Q1, Q2 y Q3?", "Q2, con 90 puntos", "Q3, con 85 puntos", "Q1, con 80 puntos", "Q2 suma 90, Q3 suma 85 y Q1 suma 80."),
        ("abc", "{F} Dos personas finalistas empatan en 80 puntos. ¿Qué corresponde?", "Aplicar el criterio de desempate definido antes del proceso", "Elegir por simpatía", "Echarlo a la suerte sin avisar", "El desempate se fija antes y se aplica igual a todas."),
        ("=", "{F} ¿Cuántos minutos suman las actividades del plan de inducción del primer día?", "30+30+45+60+30+45", "Minutos totales = suma de las seis actividades.", " minutos"),
        ("=", "{F} ¿Cuántas horas son esos minutos?", "240//60", "Horas = minutos ÷ 60.", " horas"),
        ("abc", "{F} Si la jornada del primer día es de 5 horas con 30 minutos de descanso, ¿cabe el plan de 4 horas?", "Sí: 4 horas más 30 minutos de descanso caben en 5 horas", "No, es mayor que 5 horas", "No se puede saber", "4 horas y media es menos que 5 horas."),
        ("abc", "{F} Una persona no seleccionada pide saber el puntaje de la persona seleccionada. ¿Qué corresponde?", "No entregarlo y explicarle su propio resultado de forma respetuosa", "Entregarlo", "Ignorar el pedido", "Los datos de otras personas son reservados."),
    ],
    ctx=("abc", "La jefatura pregunta cuál fue el resultado del proceso. ¿Qué responde RR.HH. con los puntajes?", "Q2 obtuvo 90 puntos, Q3 85 y Q1 80, con la misma pauta; la decisión es de la jefatura", "Q1 porque fue el primero", "No hay resultado", "La respuesta se apoya en puntajes iguales para todos."),
    sc=[
        ("En Recursos Humanos: ¿cuándo se define el criterio de desempate?", "Antes del proceso", "Así la decisión no parece arbitraria ni improvisada."),
        ("¿Qué se suma para saber si el plan de inducción cabe en el día?", "Los tiempos de todas las actividades", "La suma debe caber en la jornada."),
        ("¿Quién decide a quién contratar?", "La jefatura", "RR.HH. entrega la información fundada y la jefatura decide."),
    ],
    op=("Con la Ficha 62, escribe un informe de seis líneas: embudo (porcentajes de cada etapa), puntajes totales y orden de Q1, Q2 y Q3, el desempate que usarías si dos empataran (definido antes), y el total de minutos del plan de inducción con una frase de seguridad.\n{F}",
        "Embudo: 60 postulaciones, 24 cumplen (40 %), 8 entrevistas (33 % de las que cumplen), 1 seleccionada. Puntajes: Q2, 90; Q3, 85; Q1, 80. Desempate acordado antes: mayor puntaje en experiencia. Plan de inducción: 240 minutos, 4 horas. La seguridad se explica según la norma vigente y por quien corresponda.",
        ["calcula porcentajes del embudo", "suma los puntajes y ordena", "define un desempate previo", "suma los tiempos y menciona seguridad"],
        ["informe de seis líneas"],
        ["inventar un desempate después", "cálculos incorrectos", "no mencionar la seguridad"],
        "Rehace los cálculos. Si el desempate se define después, pide cambiarlo."),
    reinforce="Calcula en papel el porcentaje de paso de tres etapas de un proceso ficticio.",
    extend="Explica con un ejemplo inventado cómo cambiaría el orden si el peso de cada criterio fuera igual.",
)

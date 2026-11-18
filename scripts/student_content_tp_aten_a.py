"""Atención de Enfermería TP 3.º medio (tronco): OAE-01 (cuidados básicos, higiene y confort con trato digno), OAE-02 (medir, controlar y registrar parámetros de salud: lectura de planillas) y OAE-03 (promoción de salud y prevención). Todo en papel: fichas, planillas y personas inventadas y rotuladas «de ejemplo»; sin técnicas clínicas ni procedimientos."""
from __future__ import annotations

from tp_aten_common import LIM, build

O1 = "TP-ATEN-3-OAE-01"
O2 = "TP-ATEN-3-OAE-02"
O3 = "TP-ATEN-3-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (servicio de ejemplo, inventado). Servicio de medicina del «Hospital Ejemplo del Valle», turno de día de 08:00 a 20:00 (12 horas, de las cuales 1 hora es de colación). "
     "Equipo: 1 enfermera, 3 técnicos en enfermería y 1 auxiliar de servicio; el médico pasa visita por la mañana. Hay 18 camas, todas ocupadas. La enfermera reparte los pacientes por igual entre los 3 técnicos y entrega a cada uno, por escrito, las indicaciones de cuidado. "
     "Cada técnico anota el estado de cada paciente a su cargo en una planilla de registro a las 08:00, 11:00, 14:00 y 17:00.")
build(
    O1, 1, F,
    use="Aprenderé quién hace qué en un equipo de salud, qué derechos tiene un paciente, qué riesgos hay en el trabajo de cuidado y por qué todo se registra y se consulta.",
    prior=["Sé leer una ficha con horarios.", "Sé multiplicar y dividir.", "Sé qué es un hospital o un consultorio."],
    explain=[
        "En Atención de Enfermería, el cuidado de una persona lo hace un equipo de salud con funciones distintas. El médico indica tratamientos, la enfermera planifica y supervisa el cuidado, y el técnico en enfermería apoya los cuidados básicos que la enfermera le indica por escrito. Una indicación es una instrucción de un profesional; el técnico no inventa ni cambia cuidados por su cuenta, y ante cualquier duda pregunta antes de actuar.",
        "Todo paciente tiene derechos: a un trato digno, a recibir información comprensible, a que se respete su privacidad y a que sus datos de salud no se comenten con personas ajenas. También puede aceptar o rechazar un cuidado. Los riesgos del trabajo son las infecciones, las caídas, los errores de registro y la filtración de datos. Por eso se registra con hechos, hora y firma, y la planilla es un documento del servicio, no una libreta personal.",
        "Si algo parece urgente, como una caída o un cambio brusco en un paciente, el técnico no decide qué hacer: avisa de inmediato a la enfermera o profesional responsable y a emergencias." + LIM,
    ],
    vocab=[("equipo de salud", "personas con distintas funciones que cuidan juntas a un paciente"), ("técnico en enfermería", "persona que apoya los cuidados básicos bajo las indicaciones y la supervisión de la enfermera"), ("indicación", "instrucción escrita de un profesional sobre el cuidado de un paciente"), ("derechos del paciente", "trato digno, información, privacidad y reserva de sus datos"), ("supervisión", "orientación y control de la enfermera sobre el trabajo del técnico"), ("planilla de registro", "documento del servicio donde se anotan hechos observados con hora y firma")],
    worked=[
        ("Quién resuelve una duda", "Una técnica de ejemplo lee en su indicación un cuidado que no entiende. ¿Qué hace?", ["La indicación la escribió la enfermera y solo ella puede aclararla.", "La técnica no la interpreta a su manera: pregunta antes de actuar."], "Consulta a la enfermera antes de actuar"),
        ("Carga de un turno", "En otra sala de ejemplo hay 20 camas ocupadas y 4 técnicos, y cada uno anota 5 registros por paciente en el turno. ¿Cuántos registros anota cada técnico?", ["20 pacientes entre 4 técnicos son 5 pacientes por técnico.", "5 pacientes × 5 registros = 25."], "25 registros por técnico"),
    ],
    mistakes=[("Cambiar un cuidado porque «el paciente dijo que prefiere otra cosa» sin consultar a la enfermera.", "Las indicaciones las define el profesional; una preferencia se informa, no se resuelve a solas.", "Anota lo que el paciente pidió y avísale a la enfermera."),
              ("Contar en el pasillo cómo está un paciente a quien lo visita un conocido.", "Los datos de salud son confidenciales; solo se informa a quien corresponde según el protocolo.", "Deriva la consulta a la enfermera o al profesional responsable.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es una indicación de cuidado?", "Una instrucción escrita de un profesional sobre el cuidado de un paciente", "Una opinión del técnico sobre lo que cree mejor para el paciente", "La lista de camas ocupadas del servicio", "La indicación la escribe un profesional; las opiniones y las listas de camas son otra cosa."),
        ("abc", "{F} ¿Quién reparte los pacientes entre los técnicos y les entrega las indicaciones?", "La enfermera", "El médico que pasa visita", "La auxiliar de servicio", "La ficha dice que la enfermera reparte y entrega las indicaciones; el médico solo pasa visita."),
        ("abc", "Al comenzar el turno, un técnico ve que a uno de sus pacientes le falta la hoja de indicaciones. ¿Qué corresponde?", "Pedirla a la enfermera antes de actuar", "Usar la hoja de otro paciente que se parezca", "Hacer lo mismo que se hizo en el turno anterior", "Las indicaciones las entrega la enfermera; sin la hoja, el técnico no actúa por suposición."),
        ("=", "{F} ¿Cuántos registros anota en el turno cada técnico, si cada uno tiene a su cargo la misma cantidad de pacientes?", "18//3*4", "Se divide el total de pacientes entre los técnicos y se multiplica por los cuatro horarios de registro.", " registros"),
        ("abc", "Una visita pregunta a un técnico de qué está enferma una paciente de la cama 9. ¿Qué respuesta respeta sus derechos?", "Pedirle que consulte a la enfermera, sin dar datos de la paciente", "Contarle solo el diagnóstico, porque es una visita amable", "Contarle solo si lo pide por segunda vez", "Los datos de salud son confidenciales y los entrega solo quien corresponde según el protocolo."),
        ("abc", "{F} Un técnico nota que un paciente de su lista dejó de responder con claridad y se ve muy decaído. ¿Qué hace?", "Avisa de inmediato a la enfermera o profesional responsable y a emergencias", "Espera al siguiente horario de registro para anotarlo", "Le da algo para beber o un medicamento para que mejore", "Un cambio brusco se avisa al instante; el técnico no decide ni trata por su cuenta."),
        ("=", "{F} Cada técnico trabaja 11 horas efectivas (12 menos 1 de colación). Si reparte su tiempo por igual entre sus pacientes solo para planificar su planilla, ¿cuántos minutos le tocan por paciente?", "(11*60)//(18//3)", "Se pasan las horas efectivas a minutos y se dividen entre los pacientes de cada técnico.", " minutos"),
        ("abc", "{F} Un compañero dice: «Así lo hago yo desde hace años, no necesitas leer la indicación». ¿Qué corresponde?", "Seguir lo que dice la indicación escrita y consultar si hay diferencias", "Hacerlo como el compañero, porque tiene experiencia", "Combinar ambas formas según se vea el paciente", "La referencia de trabajo es la indicación escrita de la enfermera, no la costumbre de otra persona."),
        ("abc", "Un familiar de un paciente de ejemplo pide que el técnico no anote en la planilla que el paciente rechazó un cuidado. ¿Qué corresponde?", "Anotar el hecho tal como ocurrió e informar a la enfermera", "No anotarlo, para no incomodar a la familia", "Anotar que sí lo recibió, para evitar problemas", "El registro debe ser fiel a lo ocurrido; omitir o cambiar datos es una falta."),
        ("abc", "{F} A las 11:00 un técnico no alcanza a ver a uno de sus pacientes. ¿Qué anota en la planilla?", "Que no pudo observarlo a esa hora y lo informa a la enfermera", "El mismo dato de las 08:00, para completar la hora", "Nada, y espera a anotar a las 14:00", "Registrar solo lo observado mantiene la planilla confiable; inventar o copiar datos es un error grave."),
        ("abc", "Un compañero afirma: «El técnico en enfermería puede cambiar un cuidado si el paciente se lo pide con buena razón». ¿Qué corresponde responder?", "Que debe informar la petición a la enfermera, que decide si se cambia la indicación", "Que sí, porque el paciente tiene derechos", "Que sí, mientras lo anote después", "Los derechos del paciente se respetan informando a la enfermera; el cambio de una indicación no lo decide el técnico."),
        ("=", "{F} Si faltara un técnico y los 18 pacientes se repartieran por igual entre los 2 que quedan, ¿cuántos registros tendría que anotar cada uno en el turno?", "18//2*4", "Se calcula cuántos pacientes tendría cada técnico y se multiplica por los cuatro horarios de registro.", " registros"),
        ("abc", "En Atención de Enfermería: ¿para qué sirve registrar con hora y firma?", "Para que otra persona del equipo sepa qué ocurrió, cuándo y quién lo anotó", "Para decidir qué pacientes recibirán más cuidados", "Para dejar una nota personal del técnico", "El registro con hora y firma da trazabilidad: permite saber quién anotó y cuándo."),
    ],
    ctx=("abc", "{F} Mientras anota en la planilla, un técnico oye un golpe y ve a un paciente de la cama 7 en el suelo. ¿Qué hace?", "Avisa de inmediato a la enfermera y pide ayuda de emergencia; no lo mueve por cuenta propia", "Lo levanta enseguida para dejarlo en su cama", "Termina su registro y avisa al final del turno", "Ante una caída solo se avisa de inmediato; mover a la persona puede agravarla y no corresponde al técnico decidirlo."),
    sc=[
        ("En Atención de Enfermería: ¿quién entrega las indicaciones de cuidado al técnico?", "La enfermera", "La enfermera planifica y supervisa; el técnico apoya lo que ella indica."),
        ("¿Qué haces si dudas de una indicación?", "Consulto a la enfermera antes de actuar", "Una duda se aclara con quien escribió la indicación."),
        ("¿Qué haces ante una caída de un paciente?", "Aviso de inmediato a la enfermera y a emergencias", "No decido ni muevo a la persona: pido ayuda de quien corresponde."),
    ],
    op=("Caso de ejemplo: en el turno de la ficha, una técnica ve que la visita de la paciente de la cama 12 pide fotografiar la planilla «para saber cómo está», y la paciente dice que no quiere que su hijo vea sus datos. "
        "Escribe: qué derecho de la paciente está en juego; qué respondería la técnica a la visita; a quién avisaría; y una frase de registro con un hecho observado, sin opinión.",
        "Derecho: privacidad y confidencialidad de sus datos. Respuesta: «La información la entrega la enfermera; ahora no puedo mostrar la planilla». Avisa a la enfermera de lo ocurrido. Registro: «A las 15:00 una visita pidió ver la planilla de la cama 12 y la paciente indicó que no deseaba compartir sus datos».",
        ["nombra el derecho a la privacidad", "no entrega datos y deriva a la enfermera", "el registro describe un hecho, sin opinión"],
        ["hoja con derecho, respuesta, a quién avisa y una frase de registro"],
        ["mostrar la planilla a la visita", "decidir sola qué información entregar", "anotar una opinión sobre la visita en vez de un hecho"],
        "Pregunta: «¿tu frase de registro dice qué pasó o qué piensas de la visita?». Si opina, pídele reescribirla como hecho."),
    reinforce="Escribe tres cosas que hace un técnico en enfermería y tres que solo decide la enfermera o el médico.",
    extend="Explica con un ejemplo inventado por qué un registro fiel protege al paciente y al propio técnico.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (cuidados programados, de ejemplo). Cuatro pacientes de ejemplo de un hospital inventado y su etapa del ciclo vital: cama 1, Rosa, adulta mayor; cama 2, Joaquín, escolar de 8 años, acompañado por su madre; cama 3, Iván, adulto; cama 4, Amanda, lactante de 9 meses, acompañada por su padre. "
     "Cuidados programados por la enfermera para el turno, en cantidad de veces: cama 1, higiene 2 y confort 3; cama 2, higiene 1 y confort 2; cama 3, higiene 2 y confort 2; cama 4, higiene 2 y confort 4. "
     "Las etapas del ciclo vital son lactante, preescolar, escolar, adolescente, adulto y adulto mayor.")
build(
    O1, 2, F,
    use="Aprenderé las etapas del ciclo vital, las necesidades básicas de una persona y cómo se lee una hoja de cuidados programados.",
    prior=["Sé qué hace el técnico y qué hace la enfermera.", "Sé sumar columnas de una tabla.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería, el cuidado cambia según la etapa del ciclo vital: lactante, preescolar, escolar, adolescente, adulto y adulto mayor. Una persona pequeña necesita que un adulto de su familia la acompañe y la calme; una persona mayor necesita que se respete su autonomía, es decir, que haga por sí misma lo que pueda. En todas las etapas existen necesidades básicas: higiene, alimentación, descanso, movilidad, eliminación y confort.",
        "La higiene es la limpieza de la persona y de su entorno; el confort es su bienestar físico y emocional, por ejemplo, un ambiente tranquilo y una posición cómoda. El grado de dependencia indica cuánta ayuda necesita una persona para satisfacer sus necesidades, y lo evalúa la enfermera. Las hojas de cuidados programados dicen cuántas veces y a qué hora se cuida cada necesidad, y el técnico las lee y las cumple según la indicación.",
        "Esta clase solo enseña a nombrar y a leer: cómo se realiza cada cuidado lo enseña un profesional con práctica supervisada." + LIM,
    ],
    vocab=[("ciclo vital", "etapas de la vida de una persona, de lactante a adulto mayor"), ("necesidad básica", "algo que toda persona requiere para estar bien: higiene, alimentación, descanso, movilidad, eliminación y confort"), ("autonomía", "capacidad de decidir y hacer por sí misma lo que puede"), ("grado de dependencia", "cuánta ayuda necesita una persona, evaluada por la enfermera"), ("higiene", "limpieza de la persona y de su entorno"), ("confort", "bienestar físico y emocional de la persona"), ("hoja de cuidados", "documento que dice qué cuidados se programan, cuántas veces y a qué hora")],
    worked=[
        ("Ubicar una etapa", "Una persona de ejemplo tiene 15 años. ¿En qué etapa del ciclo vital está?", ["Las etapas se ordenan de lactante a adulto mayor.", "Quince años corresponden a la adolescencia."], "Adolescente"),
        ("Sumar cuidados", "En otra hoja de ejemplo, un paciente tiene 2 cuidados de higiene y 3 de confort, y otro tiene 1 de higiene y 4 de confort. ¿Cuántos cuidados programados hay en total?", ["Primer paciente: 2 + 3 = 5.", "Segundo paciente: 1 + 4 = 5; total 5 + 5 = 10."], "10 cuidados"),
    ],
    mistakes=[("Tratar a una persona mayor como a un niño y hacerle todo, aunque pueda hacer cosas por sí misma.", "Le quita autonomía y puede disminuir sus capacidades y su dignidad.", "Pregunta qué puede hacer por sí misma y avisa a la enfermera si necesita más ayuda."),
              ("Creer que el confort es solo «que tenga una cama blanda».", "El confort incluye lo físico y lo emocional, como el ruido, la luz y sentirse acompañado.", "Anota qué factores del ambiente ayudan o molestan a la persona e infórmalos a la enfermera.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es una necesidad básica?", "Algo que toda persona requiere para estar bien, como higiene o descanso", "Un examen que pide el médico al ingresar", "Un diagnóstico que anota la enfermera", "Las necesidades básicas son requerimientos de toda persona; los exámenes y los diagnósticos son otra cosa."),
        ("abc", "{F} ¿En qué etapa del ciclo vital está Amanda, de la cama 4?", "Lactante", "Preescolar", "Escolar", "La ficha dice que Amanda tiene 9 meses, edad propia de lactante."),
        ("abc", "{F} ¿Cuántos cuidados de confort tiene programados el paciente de la cama 4?", "4", "2", "3", "En la ficha, la cama 4 tiene confort 4; los otros números pertenecen a otras camas."),
        ("=", "{F} ¿Cuántos cuidados de higiene hay programados entre las cuatro camas?", "2+1+2+2", "Se suman los cuidados de higiene de las cuatro camas.", " cuidados"),
        ("abc", "{F} ¿Qué se debe respetar especialmente al cuidar a Rosa, adulta mayor?", "Su autonomía: que haga por sí misma lo que pueda", "Que todo se haga por ella para que no se esfuerce", "Que decida el técnico si prefiere no consultarle", "La autonomía es un derecho en cualquier etapa; hacerle todo disminuye sus capacidades."),
        ("abc", "{F} ¿Cuál de estas es una necesidad de confort?", "Un ambiente tranquilo y con la luz que la persona prefiere", "Registrar la hora de ingreso", "Reponer el stock de insumos", "El confort es bienestar físico y emocional; registrar y reponer son tareas administrativas."),
        ("=", "{F} ¿Cuántos cuidados programados hay en total en la cama 2, sumando higiene y confort?", "1+2", "Se suman los cuidados de higiene y de confort de esa cama.", " cuidados"),
        ("=", "{F} ¿Cuántos cuidados de confort más que de higiene hay programados en total para las cuatro camas?", "(3+2+2+4)-(2+1+2+2)", "Se suma el confort de todas las camas, se suma la higiene de todas las camas y se restan.", " cuidados"),
        ("abc", "{F} La ficha dice que el padre de Amanda la acompaña. ¿Qué papel cumple su presencia al cuidar a una lactante?", "Ayuda a calmarla y a darle seguridad, y se le trata con respeto", "Reemplaza al técnico en los cuidados", "Es un riesgo que se debe evitar siempre", "En las etapas pequeñas, la compañía de la familia da seguridad y es parte del cuidado."),
        ("abc", "{F} Una técnica dice: «A los escolares y a los adultos mayores se les cuida igual». ¿Qué corresponde responder?", "Que los cuidados se adaptan a la etapa y a las necesidades de cada persona", "Que sí, porque todos los pacientes son iguales", "Que sí, mientras sea en el mismo servicio", "El cuidado se adapta a la etapa del ciclo vital y a lo que cada persona necesita."),
        ("abc", "{F} En la hoja, Iván aparece con 2 cuidados de higiene. Al final del turno solo hay 1 anotado. ¿Qué corresponde?", "Anotar el cuidado pendiente con su motivo e informar a la enfermera", "Anotar los 2 como hechos para completar la hoja", "No anotar nada y dejar que lo vea el siguiente turno", "Un cuidado no realizado se registra como pendiente con su motivo; anotarlo como hecho es falsear el registro."),
        ("=", "{F} La enfermera pide sumar todos los cuidados programados (higiene y confort) de las camas 1 y 3 para organizar su planilla. ¿Cuántos son?", "(2+3)+(2+2)", "Se suman los cuidados de higiene y de confort de las camas 1 y 3.", " cuidados"),
        ("abc", "{F} Una técnica novata quiere cambiar el orden de los cuidados de la cama 2 porque cree que así se cansará menos el paciente. ¿Qué hace?", "Propone el cambio a la enfermera y sigue lo programado mientras tanto", "Lo cambia, porque conoce bien al paciente", "Lo cambia solo si la madre está de acuerdo", "La programación la define la enfermera; el técnico propone y no cambia por su cuenta."),
    ],
    ctx=("abc", "{F} Durante un turno de ejemplo, Rosa dice que prefiere que no le abran la cortina de su cama porque le molesta la luz. La técnica ve que la hoja pide confort 3 veces. ¿Qué hace?", "Anota la preferencia, la informa a la enfermera y cuida el confort respetando lo que Rosa expresó", "Abre la cortina igual, porque la hoja lo exige", "Cierra la cortina y no cuenta nada a nadie", "La preferencia de la persona es parte del confort; se respeta y se informa a quien programa los cuidados."),
    sc=[
        ("En Atención de Enfermería: ¿qué etapa del ciclo vital sigue después de adulto?", "Adulto mayor", "El orden es lactante, preescolar, escolar, adolescente, adulto y adulto mayor."),
        ("¿Qué es el confort?", "El bienestar físico y emocional de la persona", "Incluye el ambiente, la compañía y la comodidad."),
        ("¿Qué haces si un cuidado programado no se pudo hacer?", "Lo anoto como pendiente con el motivo e informo a la enfermera", "No se anota como hecho algo que no se hizo."),
    ],
    op=("Hoja de ejemplo: «cama 5, Camilo, preescolar de 4 años; cama 6, Elena, adulta de 40 años; cama 7, Gaspar, adulto mayor. Cuidados programados en el turno: cama 5, higiene 1 y confort 3; cama 6, higiene 2 y confort 2; cama 7, higiene 2 y confort 4». "
        "Escribe: la etapa de cada paciente; cuántos cuidados programados hay en total; una cosa que respetarías en la autonomía de Gaspar; y qué anotarías si el último cuidado de confort de la cama 7 no se alcanzó a hacer.",
        "Etapas: preescolar, adulta, adulto mayor. Total: (1+3)+(2+2)+(2+4) = 14 cuidados. Autonomía de Gaspar: preguntarle qué puede hacer por sí mismo y no hacérselo todo. Si no se alcanzó: anotar el cuidado como pendiente con el motivo e informar a la enfermera.",
        ["nombra bien las etapas", "suma los cuidados correctamente", "respeta la autonomía", "anota el pendiente con su motivo"],
        ["hoja con tres etapas, un total, una acción de autonomía y una frase de registro"],
        ["anotar como hecho un cuidado no realizado", "decidir cambiar la programación sin consultar", "sumar mal los cuidados"],
        "Pregunta: «¿tu registro dice por qué no se hizo el cuidado?». Si no, pídele agregar el motivo y el aviso a la enfermera."),
    reinforce="Nombra las seis etapas del ciclo vital y escribe una necesidad básica que se vea distinta en un lactante y en un adulto mayor.",
    extend="Explica con un ejemplo inventado la diferencia entre ayudar a una persona y quitarle su autonomía.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (casos breves y pauta de trato digno, de ejemplo). Pauta de cinco criterios: (1) se presenta por su nombre; (2) explica antes de actuar; (3) cuida la privacidad; (4) respeta la decisión de la persona; (5) reserva sus datos. "
     "Caso A: el técnico entra sin golpear, no se presenta, destapa a la paciente sin avisar y sin preguntarle si acepta el cuidado; no comenta datos con nadie. Caso B: el técnico golpea, se presenta, explica, cierra la cortina, respeta lo que la paciente decide y no comenta datos. "
     "Caso C: el técnico se presenta, explica, cuida la privacidad y respeta lo que la paciente decide, pero comenta su estado en el pasillo con una visita de otro paciente. "
     "Caso D: la paciente dice que hoy no quiere el cuidado programado; el técnico se presenta, explica y cuida la privacidad, pero insiste varias veces hasta que ella acepta; no comenta datos. "
     "Cumplimiento de criterios: A 1 de 5, B 5 de 5, C 4 de 5, D 4 de 5.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de trato a un paciente con una pauta de criterios, a reconocer qué derecho se respetó o se vulneró y a decidir a quién avisar.",
    prior=["Conozco los derechos del paciente.", "Sé qué es una indicación.", "Sé calcular porcentajes de números enteros."],
    explain=[
        "Para analizar un caso de trabajo se lee primero la situación y luego se compara con una pauta de criterios. La pauta es una lista de conductas esperadas; se revisa una por una y se marca si se cumplió. Con eso se puede decir qué se hizo bien y qué se debe mejorar sin juzgar a la persona, solo describiendo hechos observables.",
        "Los criterios del trato digno son: presentarse, explicar antes de actuar, cuidar la privacidad, respetar la decisión de la persona y reservar sus datos. Respetar la decisión significa que el paciente puede aceptar o rechazar un cuidado, y el técnico no lo presiona: anota el rechazo con hechos, informa a la enfermera y ella decide cómo seguir. El consentimiento es la aceptación libre de la persona después de recibir información comprensible.",
        "Un caso mal resuelto no se esconde: se informa a la enfermera para corregirlo y mejorar." + LIM,
    ],
    vocab=[("trato digno", "trato respetuoso que reconoce a la persona como sujeto de derechos"), ("pauta de criterios", "lista de conductas esperadas que se revisan una por una"), ("privacidad", "derecho a que su cuerpo y su intimidad se resguarden de la vista de otros"), ("consentimiento", "aceptación libre de la persona luego de recibir información comprensible"), ("rechazo de un cuidado", "decisión de la persona de no aceptar un cuidado propuesto"), ("porcentaje de cumplimiento", "parte de los criterios cumplidos respecto del total, expresada sobre 100")],
    worked=[
        ("Aplicar la pauta a un caso", "Un técnico de ejemplo se presenta, explica lo que hará y deja la puerta abierta de par en par mientras la paciente se cambia. ¿Qué criterio no cumple?", ["Se presentó y explicó, por lo que cumple los criterios 1 y 2.", "Dejar la puerta abierta no cuida la intimidad: no cumple el criterio 3."], "El criterio 3: cuidar la privacidad"),
        ("Calcular el cumplimiento", "En otro caso de ejemplo, un técnico cumple 3 de los 5 criterios de la pauta. ¿Qué porcentaje cumple?", ["Se multiplica 3 por 100 y se divide por 5.", "300 ÷ 5 = 60."], "60 %"),
    ],
    mistakes=[("Insistir con un paciente que rechaza un cuidado «porque es por su bien».", "Presionar le quita su derecho a decidir; el cuidado puede ser necesario, pero eso lo evalúa la enfermera.", "Respeta el rechazo, anótalo con hechos y avisa a la enfermera."),
              ("Comentar el caso de una paciente en el pasillo, aunque sea «solo para desahogarse».", "Cualquier persona que pase puede escuchar y se rompe la confidencialidad.", "Habla del caso solo con la enfermera o el equipo, en un lugar reservado.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es el consentimiento de un paciente?", "La aceptación libre de la persona después de recibir información comprensible", "La firma del técnico en la planilla", "El permiso de la visita para que se haga un cuidado", "El consentimiento es de la propia persona y supone información comprensible."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso A al entrar sin golpear y destapar a la paciente sin avisar?", "El criterio 3: cuidar la privacidad", "El criterio 5: reservar los datos", "Ninguno, porque no habló con nadie", "Destapar sin avisar y entrar sin golpear vulnera la privacidad, que es el criterio 3."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso C?", "El criterio 5: reservar los datos de la persona", "El criterio 1: presentarse", "El criterio 4: respetar la decisión de la persona", "En el caso C comenta el estado de la paciente en el pasillo, lo que rompe la reserva de sus datos."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso D?", "El criterio 4: respetar la decisión de la persona", "El criterio 2: explicar antes de actuar", "El criterio 3: cuidar la privacidad", "Insistir hasta que acepta no respeta que ella puede rechazar el cuidado."),
        ("=", "{F} ¿Cuántos criterios cumplieron en total los casos A, B, C y D?", "1+5+4+4", "Se suman los criterios cumplidos por cada caso.", " criterios"),
        ("=", "{F} Si cada caso se evalúa con 5 criterios, ¿qué porcentaje de los criterios se cumplió entre los cuatro casos?", "(1+5+4+4)*100//(4*5)", "Se suman los criterios cumplidos, se multiplica por 100 y se divide por el total de criterios evaluados.", " %"),
        ("abc", "{F} ¿Qué debe hacer un técnico en la situación del caso D cuando la paciente dice que hoy no quiere el cuidado programado?", "Respetar su decisión, anotar el rechazo con hechos e informar a la enfermera", "Insistir con ayuda de la visita hasta que acepte", "Hacer el cuidado igual y anotar que lo aceptó", "La persona puede rechazar un cuidado y la enfermera evalúa cómo continuar."),
        ("abc", "{F} ¿Cuál es el caso que cumple todos los criterios de la pauta?", "El caso B", "El caso A", "El caso C", "La ficha muestra que solo el caso B cumple 5 de 5 criterios."),
        ("abc", "{F} Un técnico dice que en el caso D «al final ella aceptó, entonces estuvo bien». ¿Qué corresponde responder?", "Que aceptar por insistencia no es un consentimiento libre", "Que sí, porque el resultado fue el esperado", "Que sí, porque el cuidado era una indicación", "Una aceptación lograda con insistencia no es libre, aunque el cuidado estuviera indicado."),
        ("abc", "{F} Al anotar el caso D, un técnico escribe «paciente difícil». ¿Qué corresponde?", "Reescribir con hechos: lo que dijo y lo que ocurrió, sin etiquetas", "Dejarlo así, porque resume lo ocurrido", "Agregar una opinión más completa sobre su carácter", "El registro describe hechos observables; una etiqueta no ayuda y puede dañar a la persona."),
        ("abc", "{F} Una visita pregunta a la técnica del caso C qué tiene la paciente de la cama 3. ¿Qué respuesta respeta los derechos de la paciente?", "Decir que la información la entrega la enfermera y derivar la consulta", "Contarle lo básico, porque ya sabe algo", "Decirle que mire la planilla del servicio", "Solo la persona responsable informa; los datos de la paciente son reservados."),
        ("=", "{F} Después de corregir, el técnico del caso C pasa a cumplir los 5 criterios y el del caso D, 5 de 5. ¿Cuántos criterios más se cumplen entre ambos casos que antes?", "(5+5)-(4+4)", "Se compara el total corregido con el total anterior de los casos C y D.", " criterios"),
        ("abc", "En Atención de Enfermería: ¿para qué sirve una pauta de criterios?", "Para revisar conductas una por una y mejorar sin juzgar a la persona", "Para decidir qué técnico recibirá un castigo", "Para reemplazar la indicación de la enfermera", "La pauta describe conductas observables y orienta la mejora."),
    ],
    ctx=("abc", "{F} Una técnica llega a ayudar a un paciente de ejemplo y nota que él no quiere hablar ni que lo toque nadie hoy. Ya se presentó y le explicó el cuidado indicado. ¿Qué hace?", "Respeta su decisión, anota lo observado y avisa a la enfermera para que evalúe", "Le dice que debe aceptar porque es un derecho de su familia", "Hace el cuidado mientras él mira a otro lado", "El paciente puede rechazar; el rechazo se registra y la enfermera decide cómo seguir."),
    sc=[
        ("En Atención de Enfermería: ¿qué haces si un paciente rechaza un cuidado indicado?", "Respeto su decisión, anoto el hecho y aviso a la enfermera", "El rechazo se registra y lo evalúa la enfermera."),
        ("¿Cuántos criterios tiene la pauta de trato digno de la ficha?", "5", "Presentarse, explicar, privacidad, respetar la decisión y reservar los datos."),
        ("¿Qué debe describir un registro?", "Hechos observables, sin etiquetas", "Los hechos permiten mejorar; las etiquetas dañan."),
    ],
    op=("Caso de ejemplo: un técnico llega a atender a un paciente de la cama 10 que está recién despierto. Entra sin golpear, no se presenta, comienza el cuidado indicado sin preguntar si el paciente acepta (el paciente no lo rechaza) y, al terminar, comenta con otro técnico en el pasillo cómo estaba de ánimo el paciente. "
        "Usa la pauta de la ficha. Escribe: qué criterios no se cumplieron; cuántos de los 5 se cumplieron y qué porcentaje es; qué debería hacer distinto en cada criterio; y a quién avisarías.",
        "No se cumplieron: 1 (no se presentó), 2 (no explicó), 3 (no cuidó la privacidad al entrar sin golpear) y 5 (comentó en el pasillo). Cumplió solo el 4, porque el paciente no rechazó nada: 1 de 5 = 20 %. Distinto: golpear, presentarse, explicar, cuidar la intimidad y comentar solo con la enfermera. Avisaría a la enfermera.",
        ["identifica los criterios incumplidos", "calcula 1 de 5 como 20 %", "propone una conducta distinta por criterio", "avisa a la enfermera"],
        ["hoja con criterios incumplidos, porcentaje, conductas alternativas y a quién avisa"],
        ["no marcar el comentario en el pasillo", "calcular mal el porcentaje", "opinar sobre el técnico en vez de describir hechos"],
        "Pregunta: «¿tu propuesta cambia lo que se hace o solo dice que debería ser más amable?». Si es lo segundo, pídele una conducta concreta."),
    reinforce="Elige un caso de la ficha y reescríbelo para que cumpla los 5 criterios de la pauta, sin cambiar el cuidado indicado.",
    extend="Explica con un ejemplo inventado la diferencia entre respetar una decisión y abandonar a un paciente.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (planilla de cuidados al cierre del turno, de ejemplo). Sala de ejemplo con 8 pacientes a cargo de dos técnicos, 4 pacientes cada uno. La enfermera programó para cada paciente, en el turno, 2 cuidados de higiene y 3 de confort. "
     "Realizados al cierre: Ana (4 pacientes), higiene 7 de 8 y confort 11 de 12; Beto (4 pacientes), higiene 8 de 8 y confort 10 de 12. Regla de la planilla: un cuidado no realizado se anota como pendiente con su motivo y se informa a la enfermera; no se anota como hecho. "
     "Motivos anotados: Ana, 1 higiene pendiente porque la paciente dormía y no quiso despertarla; 1 confort pendiente por traslado al examen. Beto, 2 confort pendientes por falta de tiempo.")
build(
    O1, 4, F,
    use="Aprenderé a calcular el cumplimiento de los cuidados programados de un turno, a leer los pendientes y a decidir qué se informa a la enfermera.",
    prior=["Sé calcular porcentajes de números enteros.", "Sé qué es una indicación.", "Sé leer una planilla."],
    explain=[
        "Al cierre del turno, el equipo revisa cuánto de lo programado se hizo. Para eso se calcula el cumplimiento: los cuidados realizados divididos por los programados, expresados en porcentaje. Si un técnico realizó 18 de 20 cuidados programados, el cumplimiento es 90 %, porque 18 por 100 dividido por 20 da 90. Esta cuenta se hace con los números de la planilla y no con impresiones.",
        "Los cuidados que no se realizaron se llaman pendientes. Se registran con su motivo, por ejemplo «la paciente dormía», y se informan a la enfermera para que decida qué hacer. Anotar un pendiente como hecho es falsear el registro y puede dejar a la persona sin un cuidado necesario. La planilla tampoco sirve para comparar a los técnicos entre sí: sirve para saber qué falta y por qué.",
        "La planilla es de papel y de ejemplo; el cuaderno no enseña cómo se hace ninguno de los cuidados." + LIM,
    ],
    vocab=[("cumplimiento", "cuidados realizados respecto de los programados, en porcentaje"), ("pendiente", "cuidado programado que no se realizó y se anota con su motivo"), ("programado", "indicado por la enfermera para el turno"), ("motivo", "razón concreta por la que no se realizó un cuidado"), ("cierre de turno", "momento en que se revisa y entrega lo hecho y lo pendiente")],
    worked=[
        ("Calcular un cumplimiento", "Una técnica de ejemplo tenía 20 cuidados programados y realizó 15. ¿Qué porcentaje de cumplimiento tuvo?", ["Se multiplican los 15 realizados por 100 y se divide por 20.", "1.500 ÷ 20 = 75."], "75 %"),
        ("Contar los pendientes", "Un técnico de ejemplo tenía 12 cuidados de confort programados y realizó 9. ¿Cuántos quedan pendientes y qué debe anotar?", ["12 − 9 = 3 pendientes.", "Cada pendiente se anota con su motivo y se informa a la enfermera."], "3 pendientes, anotados con motivo e informados a la enfermera"),
    ],
    mistakes=[("Anotar «hecho» en un cuidado que no se alcanzó para que el turno «se vea completo».", "Falsea el registro y deja sin cuidado a la persona sin que nadie lo sepa.", "Anótalo como pendiente con su motivo e infórmalo."),
              ("Informar «muchos pendientes» sin decir cuáles ni por qué.", "La enfermera no puede decidir sin datos concretos.", "Indica cuántos, de qué cuidado, de qué paciente y el motivo.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un cuidado pendiente?", "Un cuidado programado que no se realizó y se anota con su motivo", "Un cuidado que el técnico decidió suprimir", "Un cuidado nuevo que pide el paciente", "Un pendiente fue programado y no se hizo; se registra y se informa."),
        ("abc", "{F} ¿Cuántos cuidados de higiene programó la enfermera para cada paciente en el turno?", "2", "3", "4", "La ficha dice 2 cuidados de higiene por paciente; el 3 corresponde a confort y el 4 a los pacientes de cada técnico."),
        ("abc", "{F} ¿Cómo se debe anotar un cuidado que no se realizó?", "Como pendiente, con su motivo, e informado a la enfermera", "Como realizado, para que no queden vacíos", "No se anota, para no dar explicaciones", "La regla de la planilla pide anotar el pendiente con su motivo e informar a la enfermera."),
        ("=", "{F} ¿Cuántos cuidados programados hay en total en la sala (higiene y confort, 8 pacientes)?", "8*(2+3)", "Se suman los cuidados por paciente y se multiplican por los 8 pacientes.", " cuidados"),
        ("=", "{F} ¿Cuántos cuidados realizaron Ana y Beto entre los dos?", "(7+11)+(8+10)", "Se suman los cuidados de higiene y confort realizados por cada técnico.", " cuidados"),
        ("=", "{F} ¿Qué porcentaje de los cuidados programados de la sala se realizó?", "((7+11)+(8+10))*100//(8*(2+3))", "Se divide lo realizado entre lo programado y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos cuidados de confort quedaron pendientes entre los dos técnicos?", "(12-11)+(12-10)", "Se restan los confort realizados de los programados de cada técnico y se suman.", " pendientes"),
        ("abc", "{F} ¿Cuál es el motivo del pendiente de higiene de Ana?", "La paciente dormía y no quiso despertarla", "Falta de insumos", "Falta de tiempo", "La ficha anota que la paciente dormía; falta de tiempo es el motivo de los pendientes de Beto."),
        ("abc", "{F} Beto dice que sus 2 pendientes de confort «no importan porque eran de poca cosa». ¿Qué corresponde?", "Informarlos igual a la enfermera, que decide si son importantes", "No informarlos, porque eran pocos", "Anotarlos como realizados", "La decisión sobre la importancia de un pendiente es de la enfermera, no del técnico."),
        ("abc", "{F} Para decidir qué técnico trabajó mejor, un compañero propone comparar los porcentajes de Ana y de Beto. ¿Qué corresponde?", "Usar la planilla para saber qué falta y por qué, no para comparar personas", "Comparar, porque el porcentaje más alto es el mejor técnico", "Comparar y publicarlo en el servicio", "La planilla sirve para detectar pendientes y sus causas, no para comparar personas."),
        ("abc", "{F} Al leer los motivos, la enfermera nota que 2 pendientes de Beto son por «falta de tiempo». ¿Qué le corresponde a ella evaluar?", "Si el reparto de pacientes o de tareas necesita ajustes", "Si Beto debe ser reemplazado sin conversar", "Si el paciente debe pagar por el cuidado", "Las causas de los pendientes pueden estar en la organización, que la enfermera revisa."),
        ("=", "{F} Si Beto hubiera realizado todos sus cuidados de confort, ¿cuántos cuidados más habría hecho que los 10 realizados?", "12-10", "Se resta lo realizado de lo programado.", " cuidados"),
        ("abc", "{F} Al cierre del turno, Ana nota que olvidó anotar un cuidado de higiene que sí realizó. ¿Qué corresponde?", "Anotarlo ahora indicando la hora real en que lo hizo y avisar de la corrección", "No anotarlo, porque ya cerró el turno", "Anotarlo con una hora anterior, para que quede en orden", "Un registro tardío se anota con su hora real; cambiar la hora es falsear."),
    ],
    ctx=("abc", "{F} Una técnica nueva se da cuenta, al cierre del turno, de que dejó sin hacer un cuidado programado a un paciente, pero no hubo motivo especial: se le pasó. ¿Qué hace?", "Lo anota como pendiente con el motivo «olvido» y avisa de inmediato a la enfermera", "Lo anota como hecho para no preocupar a nadie", "No lo anota y espera que nadie lo note", "Decir la verdad permite que la enfermera decida a tiempo; ocultarlo puede perjudicar a la persona."),
    sc=[
        ("En Atención de Enfermería: ¿cómo calculas un porcentaje de cumplimiento?", "Realizados × 100 ÷ programados", "El porcentaje compara lo hecho con lo programado."),
        ("¿Qué anotas junto a un pendiente?", "El motivo", "El motivo permite que la enfermera decida."),
        ("¿Cuántos cuidados quedaron pendientes si de 10 programados se hicieron 8?", "2", "Se restan los realizados de los programados: 10 − 8 = 2."),
    ],
    op=("Planilla de ejemplo: «sala con 6 pacientes a cargo de una técnica; programados por paciente, 2 de higiene y 3 de confort; realizados al cierre: higiene 11 de 12 y confort 16 de 18. Motivos: 1 higiene pendiente, paciente en un examen; 2 confort pendientes, uno por falta de tiempo y otro porque el paciente dormía». "
        "Calcula: cuántos cuidados había programados, cuántos se realizaron y qué porcentaje es. Escribe: cuántos pendientes hay y qué informarías a la enfermera, con el motivo de cada uno.",
        "Programados: 6 × (2+3) = 30. Realizados: 11 + 16 = 27. Porcentaje: 27 × 100 ÷ 30 = 90 %. Pendientes: 3 (1 por examen, 1 por falta de tiempo y 1 porque el paciente dormía). Informaría a la enfermera cuántos pendientes hay, de qué cuidado y por qué.",
        ["calcula programados y realizados", "calcula 90 % con la cuenta correcta", "cuenta los pendientes por motivo", "informa a la enfermera"],
        ["hoja con cálculos, el porcentaje y una frase de informe a la enfermera con los pendientes y sus motivos"],
        ["anotar los pendientes como realizados", "calcular mal el porcentaje", "informar sin decir los motivos"],
        "Pregunta: «¿tu informe dice cuántos pendientes hay y por qué?». Si no, pídele agregar ambos datos."),
    reinforce="Con 15 cuidados programados y 12 realizados, calcula el porcentaje de cumplimiento y cuántos quedan pendientes.",
    extend="Explica con un ejemplo inventado por qué la planilla no debe usarse para comparar a dos técnicos entre sí.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (instrumentos de una sala, de ejemplo). En una sala de un servicio inventado hay 1 balanza, 1 tallímetro (para la talla), 6 termómetros, 3 aparatos de presión y 2 oxímetros de pulso (miden la saturación y el pulso). "
     "Cada instrumento lleva una etiqueta con la fecha de su última revisión y la de la próxima; la revisión se repite cada 6 meses. Regla del servicio: un instrumento con la etiqueta vencida no se usa y se avisa a la enfermera.")
build(
    O2, 1, F,
    use="Aprenderé qué es un parámetro de salud, qué instrumento y qué unidad le corresponde, y qué reglas generales protegen la exactitud y la seguridad al registrar.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé leer una ficha.", "Conozco el trabajo del técnico en enfermería."],
    explain=[
        "En Atención de Enfermería, un parámetro de salud es una característica del cuerpo que se mide y se anota, como el peso, la talla, la temperatura, el pulso y la presión arterial. Cada parámetro se mide con un instrumento y se expresa en una unidad: kilogramos para el peso, centímetros para la talla, grados Celsius para la temperatura, latidos por minuto para el pulso y milímetros de mercurio (mmHg) para la presión.",
        "Medir no es interpretar. El técnico registra el valor tal como lo leyó, con su unidad, la hora y su firma, sin redondearlo ni cambiarlo. Si la hoja de la enfermera trae límites de aviso y el valor los sobrepasa, el técnico informa de inmediato a la enfermera; no explica al paciente qué significa. Los instrumentos deben estar limpios y con la revisión periódica al día, porque un instrumento sin revisar puede dar un valor equivocado.",
        "Esta clase no enseña a medir ni cómo se usa cada instrumento: eso lo enseña un profesional con práctica supervisada." + LIM,
    ],
    vocab=[("parámetro de salud", "característica del cuerpo que se mide y se anota, como el peso o la temperatura"), ("instrumento de medición", "aparato con que se obtiene un valor, como la balanza o el termómetro"), ("unidad", "medida en que se expresa un valor, como kg, cm o °C"), ("revisión periódica", "comprobación que se repite cada cierto tiempo para que el instrumento mida bien"), ("límite de aviso", "valor escrito por la enfermera en la hoja que, si se sobrepasa, obliga a avisarle"), ("registro fiel", "anotación que repite el valor leído, sin cambiarlo ni redondearlo")],
    worked=[
        ("Elegir la unidad", "En una planilla de ejemplo se debe anotar la talla de un adulto. ¿En qué unidad se anota?", ["La talla es una longitud.", "En esta planilla se usan centímetros, escritos como cm."], "En centímetros (cm)"),
        ("Contar revisiones de otra sala", "Otra sala de ejemplo tiene 9 instrumentos y cada uno se revisa cada 4 meses. ¿Cuántas revisiones se hacen en un año?", ["Un año tiene 12 meses: 12 ÷ 4 = 3 revisiones por instrumento.", "9 instrumentos × 3 revisiones = 27."], "27 revisiones"),
    ],
    mistakes=[("Anotar «unos 37» cuando el valor no se alcanzó a leer bien.", "Un valor aproximado no es un registro fiel y puede ocultar un dato importante.", "Anota que no se pudo leer bien y avisa a la enfermera."),
              ("Usar un instrumento con la etiqueta vencida «solo por esta vez».", "Puede dar valores equivocados y esos datos se usarían después para decisiones.", "No lo uses, avisa a la enfermera y registra el motivo del control no realizado.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un parámetro de salud?", "Una característica del cuerpo que se mide y se anota, como el peso o la temperatura", "Un diagnóstico que escribe el médico", "Un tratamiento indicado a un paciente", "Un parámetro es algo medible; el diagnóstico y el tratamiento son decisiones del profesional."),
        ("abc", "{F} ¿Para qué sirve la etiqueta de revisión de cada instrumento?", "Para saber cuándo se revisó y cuándo corresponde la próxima revisión", "Para anotar el nombre del último paciente que lo usó", "Para decidir con qué paciente se usa", "La etiqueta indica las fechas de revisión periódica; nada tiene que ver con los pacientes."),
        ("abc", "{F} Un técnico ve que un termómetro tiene la etiqueta vencida. ¿Qué corresponde según la regla del servicio?", "No usarlo y avisar a la enfermera", "Usarlo y anotar en la planilla que podría estar descalibrado", "Usarlo solo con pacientes que no estén graves", "La regla del servicio es no usar el instrumento y avisar; anotar una duda no corrige el riesgo."),
        ("=", "{F} ¿Cuántos instrumentos hay en total en la sala?", "1+1+6+3+2", "Se suman los instrumentos de cada tipo que indica la ficha.", " instrumentos"),
        ("abc", "¿En qué unidad se expresa la temperatura corporal en una planilla de ejemplo?", "En grados Celsius (°C)", "En milímetros de mercurio (mmHg)", "En kilogramos (kg)", "La temperatura se expresa en °C; mmHg corresponde a la presión y kg al peso."),
        ("abc", "{F} Al leer el valor de un paciente, el técnico ve que sobrepasa el límite de aviso escrito en la hoja. ¿Qué hace?", "Avisa de inmediato a la enfermera y registra el valor tal como lo leyó", "Le dice al paciente qué significa su resultado", "Repite la medición varias veces hasta obtener un valor menor", "El técnico no interpreta ni oculta valores: registra con fidelidad e informa a la enfermera."),
        ("=", "{F} Si cada instrumento de la sala se revisa cada 6 meses, ¿cuántas revisiones se hacen en un año entre todos los instrumentos?", "(1+1+6+3+2)*(12//6)", "Se calculan las revisiones por instrumento en el año y se multiplican por el total de instrumentos.", " revisiones"),
        ("abc", "Un paciente de ejemplo pregunta al técnico «¿cómo salió mi presión?». ¿Qué corresponde?", "Decirle que la enfermera o el médico le explicará su resultado", "Explicarle qué significa el valor, porque el técnico lo midió", "No responderle y evitar la conversación", "Interpretar los resultados le corresponde al profesional; se informa con respeto a quién preguntar."),
        ("abc", "{F} Un compañero dice: «Si el termómetro se ve limpio y nuevo, no hace falta mirar su etiqueta». ¿Qué corresponde responder?", "Que la limpieza y la revisión periódica son cosas distintas y la etiqueta siempre se mira", "Que tiene razón, porque un instrumento nuevo no falla", "Que la etiqueta solo importa en los instrumentos grandes", "Un instrumento puede verse limpio y estar sin revisar; la etiqueta es la que indica su estado."),
        ("abc", "El técnico anota en la planilla «temperatura: 37 kg». ¿Qué falla tiene este registro?", "La unidad no corresponde al parámetro", "Falta el nombre del paciente en cada fila", "El valor debería estar redondeado a un número entero", "37 kg es una unidad de peso, no de temperatura; el valor sin la unidad correcta es un registro erróneo."),
        ("abc", "En Atención de Enfermería: ¿por qué los datos de la planilla no se comentan con pacientes ni visitas?", "Porque son datos de salud confidenciales", "Porque solo el médico los entiende", "Porque la planilla es propiedad del técnico", "Los datos de salud son confidenciales y se informan solo a quienes corresponde."),
        ("=", "{F} Hoy se revisaron 5 de los instrumentos de la sala. ¿Cuántos faltan por revisar en este ciclo?", "(1+1+6+3+2)-5", "Se resta lo revisado del total de instrumentos de la sala.", " instrumentos"),
        ("abc", "{F} Un técnico anota «sin cambios» en la planilla sin haber medido a un paciente. ¿Qué corresponde?", "Anotar solo lo medido y, si no se midió, informarlo con el motivo", "Mantener la anotación, porque es probable que no hayan cambios", "Anotar los valores de la hora anterior para completar la fila", "Solo se registran valores realmente medidos; anotar sin medir es falsear el registro."),
    ],
    ctx=("abc", "{F} A las 14:00, un técnico ve que el único aparato de presión de su sector tiene la etiqueta vencida. La enfermera está en otra sala. ¿Qué hace?", "No lo usa, avisa a la enfermera y deja anotado que el control no se pudo realizar y por qué", "Lo usa igual y anota «valor aproximado»", "Pide prestado un aparato de otro servicio sin avisar", "Un control no realizado se registra con su motivo; usar un instrumento no revisado puede dar datos erróneos."),
    sc=[
        ("En Atención de Enfermería: ¿qué haces si un valor sobrepasa el límite de aviso?", "Aviso de inmediato a la enfermera", "El técnico registra e informa; no interpreta."),
        ("¿Qué unidad corresponde al peso?", "Kilogramos (kg)", "El peso se mide en kilogramos en la planilla."),
        ("¿Qué haces con un instrumento de etiqueta vencida?", "No lo uso y aviso a la enfermera", "Un instrumento sin revisión puede dar valores equivocados."),
    ],
    op=("Caso de ejemplo: en una sala hay 8 instrumentos y la etiqueta de 3 está vencida. Un compañero dice que «igual sirven». Escribe: qué harías con los 3 instrumentos; a quién avisarías; qué anotarías en la planilla si no pudieras hacer un control por esa razón; y por qué nunca inventarías un valor. "
        "También calcula cuántos instrumentos están vigentes.",
        "Con los 3 instrumentos vencidos: no usarlos y separarlos como indique la enfermera. Avisaría a la enfermera. Anotaría: «control no realizado a las 10:00: instrumento con revisión vencida; se avisó a la enfermera». Nunca inventaría un valor porque los datos se usan después para decisiones. Vigentes: 8 − 3 = 5.",
        ["no usa los instrumentos vencidos", "avisa a la enfermera", "el registro dice qué no se hizo y por qué", "calcula 5 instrumentos vigentes"],
        ["hoja con acción, aviso, frase de registro y cálculo"],
        ["usar el instrumento igual", "anotar un valor aproximado", "olvidar avisar a la enfermera"],
        "Pregunta: «¿tu frase de registro dice qué pasó y por qué, o solo dice que todo estuvo bien?». Si es lo segundo, pídele reescribirla."),
    reinforce="Escribe tres parámetros de salud, el instrumento con que se miden y la unidad en que se anotan.",
    extend="Explica con un ejemplo inventado por qué un valor «aproximado» en la planilla puede perjudicar a un paciente.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (hoja de control de ejemplo; valores inventados que no sirven como referencia clínica). Paciente de ejemplo, cama 5. Límites de aviso escritos por la enfermera: pulso, avisar si es menor que 62 o mayor que 96 latidos por minuto; presión sistólica, avisar si es menor que 104 o mayor que 138 mmHg. "
     "Registros del día: 08:00, pulso 80 y presión sistólica 120; 12:00, pulso 98 y presión sistólica 118; 16:00, pulso 74 y presión sistólica 142; 20:00, pulso 64 y presión sistólica 112. "
     "Instrumentos: el termómetro mide la temperatura, el aparato de presión mide la presión arterial, el oxímetro mide el pulso y la saturación, la balanza mide el peso.")
build(
    O2, 2, F,
    use="Aprenderé los nombres de los signos vitales y de sus instrumentos, a leer una hoja de control con límites de aviso y quién interpreta y quién registra.",
    prior=["Sé qué es un parámetro de salud.", "Sé qué es un límite de aviso.", "Sé comparar números."],
    explain=[
        "Los signos vitales son parámetros que muestran cómo funciona el cuerpo en un momento: la temperatura, el pulso, la frecuencia respiratoria, la presión arterial y la saturación (cuánto oxígeno lleva la sangre, medido con un oxímetro). La hoja de control o curva de signos vitales es la tabla donde se anotan hora, valor, unidad y firma. La presión arterial tiene dos números: la sistólica y la diastólica.",
        "La enfermera escribe en la hoja los límites de aviso de cada paciente. Leerla es comparar cada registro con sus límites: un valor menor que el límite inferior o mayor que el superior se informa de inmediato a la enfermera. Un valor dentro de los límites igual se registra, y un valor sospechoso, como un número idéntico copiado en todas las horas, también se consulta.",
        "En esta clase los números son inventados y solo sirven para practicar la lectura de una hoja; nunca para decidir sobre una persona." + LIM,
    ],
    vocab=[("signos vitales", "parámetros que muestran cómo funciona el cuerpo: temperatura, pulso, respiración, presión y saturación"), ("hoja de control", "tabla donde se anotan hora, valor, unidad y firma de cada medición"), ("pulso", "número de latidos por minuto"), ("presión arterial", "fuerza de la sangre sobre las arterias, con un número sistólico y otro diastólico"), ("saturación", "cantidad de oxígeno que lleva la sangre, medida con un oxímetro"), ("límite de aviso", "valor escrito por la enfermera que, si se sobrepasa, obliga a avisarle")],
    worked=[
        ("Comparar con un límite", "En una hoja de ejemplo, el límite de aviso del pulso es «mayor que 90». El registro de la tarde es 94. ¿Qué corresponde?", ["94 es mayor que 90, por lo que sobrepasa el límite superior.", "Se registra el valor tal como se leyó y se avisa a la enfermera."], "Registrar 94 y avisar a la enfermera"),
        ("Diferencia entre registros", "En otra hoja de ejemplo, la presión sistólica de la mañana fue 126 y la de la noche, 132. ¿Cuántos mmHg subió?", ["Se resta el valor menor del mayor.", "132 − 126 = 6."], "6 mmHg"),
    ],
    mistakes=[("Pensar que los signos vitales «se interpretan» mirando solo un valor.", "La interpretación la hace un profesional con el conjunto de datos y la historia del paciente.", "Registra con fidelidad e informa a la enfermera lo que sobrepasa el límite de aviso."),
              ("Anotar el mismo valor en todas las horas porque «seguramente no cambia».", "Es un dato inventado, no medido, y pone en riesgo la confianza en la planilla.", "Anota solo lo medido en cada hora; si no se midió, informa el motivo.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la saturación?", "La cantidad de oxígeno que lleva la sangre, medida con un oxímetro", "La cantidad de líquido que toma el paciente en el día", "El peso del paciente en kilogramos", "La saturación mide el oxígeno de la sangre; el líquido y el peso son otros parámetros."),
        ("abc", "{F} ¿Qué instrumento mide la temperatura según la ficha?", "El termómetro", "El oxímetro", "La balanza", "La ficha dice que el termómetro mide la temperatura."),
        ("abc", "{F} ¿Quién escribe los límites de aviso de la hoja?", "La enfermera", "El técnico que mide", "El paciente", "La ficha dice que la enfermera escribe los límites de aviso."),
        ("=", "{F} ¿Cuántos mmHg subió la presión sistólica entre las 12:00 y las 16:00?", "142-118", "Se resta el valor de las 12:00 del valor de las 16:00.", " mmHg"),
        ("abc", "{F} ¿En qué hora del día el pulso sobrepasa el límite superior de aviso?", "A las 12:00", "A las 08:00", "A las 20:00", "A las 12:00 el pulso es 98, mayor que 96; en los otros horarios está dentro de los límites."),
        ("abc", "{F} ¿En qué hora del día la presión sistólica sobrepasa el límite superior de aviso?", "A las 16:00", "A las 12:00", "A las 20:00", "A las 16:00 la sistólica es 142, mayor que 138; las otras están dentro de los límites."),
        ("=", "{F} ¿Cuántos mmHg separan el valor de presión sistólica más alto del más bajo del día?", "142-112", "Se resta el valor menor del valor mayor.", " mmHg"),
        ("=", "{F} ¿Cuál es el promedio de la presión sistólica de los cuatro registros?", "(120+118+142+112)//4", "Se suman los cuatro valores y se dividen entre 4.", " mmHg"),
        ("abc", "{F} A las 12:00, el pulso sobrepasa el límite. ¿Qué hace el técnico?", "Registra 98 y avisa a la enfermera", "Anota 96 para que quede dentro del límite", "Espera al siguiente control para ver si baja", "Se registra el valor real y se avisa; ajustar el dato o esperar oculta información."),
        ("abc", "{F} Un compañero dice: «La presión de las 16:00 es alta, hay que darle algo al paciente para bajarla». ¿Qué corresponde responder?", "Que el técnico solo registra e informa a la enfermera; no decide ni administra nada", "Que sí, porque el valor ya sobrepasó el límite", "Que sí, si lo autoriza un familiar", "Tratar o decidir no le corresponde al técnico; solo registra e informa."),
        ("abc", "{F} A las 20:00 el pulso es 64 y la presión sistólica es 112. ¿Qué corresponde en la hoja?", "Registrar ambos valores, que están dentro de los límites", "No registrarlos, porque no hay nada que avisar", "Anotar «sin cambios» y omitir los números", "Todo valor medido se registra, esté o no dentro de los límites."),
        ("=", "{F} ¿Cuántos latidos por minuto bajó el pulso entre las 12:00 y las 20:00?", "98-64", "Se resta el pulso de las 20:00 del pulso de las 12:00.", " latidos por minuto"),
        ("abc", "La planilla de otra cama de ejemplo muestra pulso 80 a las 08:00, 80 a las 12:00, 80 a las 16:00 y 80 a las 20:00. ¿Qué debe hacer el técnico que revisa la hoja?", "Consultar a la enfermera si se midió realmente en cada hora", "Dejarla así, porque no hay límites sobrepasados", "Borrar tres valores para que se vea natural", "Valores idénticos repetidos pueden indicar datos copiados; se consulta antes de aceptar."),
    ],
    ctx=("abc", "{F} Al revisar el registro de las 16:00, un técnico nota que otra persona escribió 124 donde dice 142 y no hay firma en esa fila. ¿Qué hace?", "No corrige por su cuenta y consulta a quien midió y a la enfermera", "Cambia el valor a 142 porque cree que es el correcto", "Borra la fila para que no quede el error", "Corregir un registro ajeno sin confirmar con quien midió puede introducir otro error."),
    sc=[
        ("En Atención de Enfermería: ¿quién interpreta los signos vitales?", "El profesional (enfermera o médico)", "El técnico mide, registra e informa; el profesional interpreta."),
        ("¿Qué haces con un valor sobre el límite de aviso?", "Lo registro tal como está y aviso a la enfermera", "No se cambia el dato y se informa."),
        ("¿Qué mide el oxímetro?", "El pulso y la saturación", "Es el instrumento que mide ambos parámetros."),
    ],
    op=("Hoja de ejemplo (valores inventados): «Cama 3. Límites de aviso: pulso menor que 60 o mayor que 92; presión sistólica menor que 100 o mayor que 134. Registros: 09:00, pulso 70 y sistólica 130; 13:00, pulso 94 y sistólica 126; 17:00, pulso 68 y sistólica 138». "
        "Escribe: en qué horarios se sobrepasa algún límite y de qué parámetro; qué hace el técnico en cada caso; cuál es la diferencia de pulso entre el mayor y el menor registro; y qué no hace el técnico aunque el valor le preocupe.",
        "Se sobrepasa el pulso a las 13:00 (94 > 92) y la sistólica a las 17:00 (138 > 134). En ambos casos registra el valor real y avisa a la enfermera. Diferencia de pulso: 94 − 68 = 26. El técnico no interpreta, no trata ni da medicamentos y no cambia el dato.",
        ["identifica los horarios y parámetros", "registra y avisa en ambos casos", "calcula 26 de diferencia", "no interpreta ni trata"],
        ["hoja con dos horarios, acciones, un cálculo y una frase sobre lo que no hace"],
        ["cambiar el valor para que entre en el límite", "no avisar a la enfermera", "decidir un tratamiento"],
        "Pregunta: «¿qué haría el técnico si el valor lo preocupa pero está dentro de los límites?». Debe responder que registra y puede consultar a la enfermera."),
    reinforce="Escribe tres signos vitales, su instrumento y su unidad, y explica quién interpreta los valores.",
    extend="Explica con un ejemplo inventado por qué un técnico no debe decir a un paciente «tu presión está bien» o «está mal» al medirla.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (planilla de signos vitales con fallas, de ejemplo; valores inventados). Regla de la planilla: cada fila debe tener hora, parámetro, valor, unidad y firma; un error se corrige con una línea sobre el dato, el valor correcto al lado, la hora y la firma, sin corrector ni borrado. "
     "Fila 1: 08:00, pulso 78 latidos por minuto, firma presente. Fila 2: sin hora, pulso 82 latidos por minuto, firma presente. Fila 3: 12:00, temperatura 37 kg, firma presente. Fila 4: 14:00, presión sistólica 124 mmHg, dato tapado con corrector, firma presente. "
     "Fila 5: 16:00, pulso 80 latidos por minuto, sin firma. Fila 6: 18:00, presión sistólica 118 mmHg, firma presente. Fila 7: 20:00, pulso 76 latidos por minuto, firma presente. Fila 8: 22:00, temperatura 36 °C, firma presente.")
build(
    O2, 3, F,
    use="Aprenderé a revisar un registro y encontrar sus fallas, a saber cómo se corrige un error y a decidir qué informar y a quién.",
    prior=["Conozco los signos vitales y sus unidades.", "Sé qué es un límite de aviso.", "Sé calcular porcentajes de números enteros."],
    explain=[
        "Para analizar un caso con registros se comprueba fila por fila si cumple la regla de la planilla: hora, parámetro, valor, unidad y firma. Un registro incompleto no se puede usar con seguridad: sin hora no se sabe cuándo ocurrió; sin firma, nadie responde por él; con una unidad equivocada, el número puede significar otra cosa. Revisar así es detectar fallas, no buscar culpables.",
        "Un error de registro no se tapa ni se borra. La forma correcta de corregirlo es trazar una línea sobre el dato, escribir el valor correcto al lado, con la hora y la firma de quien corrige, de modo que el dato original siga legible. El corrector, el borrado o el cambio por otra persona sin avisar impiden saber qué ocurrió y pueden alterar la ficha clínica.",
        "Las fallas se informan a la enfermera para que decida; el técnico no completa datos que no midió." + LIM,
    ],
    vocab=[("fila de registro", "línea de la planilla con hora, parámetro, valor, unidad y firma"), ("firma", "marca de la persona que midió y que responde por el registro"), ("corrección de un error", "línea sobre el dato, valor correcto al lado, hora y firma, sin borrar"), ("trazabilidad", "posibilidad de saber quién registró, qué y cuándo"), ("ficha clínica", "documento con la información de salud de una persona"), ("legible", "que se puede leer sin dudas")],
    worked=[
        ("Revisar una fila", "Una fila de ejemplo dice: «10:00, peso 62, firma presente». ¿Qué le falta?", ["La regla pide hora, parámetro, valor, unidad y firma.", "Falta la unidad: kg."], "La unidad (kg)"),
        ("Contar filas correctas", "En otra planilla de ejemplo hay 10 filas y 7 cumplen toda la regla. ¿Qué porcentaje cumple?", ["7 × 100 = 700.", "700 ÷ 10 = 70."], "70 %"),
    ],
    mistakes=[("Tapar con corrector un número mal anotado.", "Se pierde el dato original y no se puede saber si hubo una alteración.", "Traza una línea sobre el error, escribe el valor correcto al lado con hora y firma."),
              ("Completar de memoria la hora que faltaba en una fila ajena.", "El dato lo conoce solo quien midió; completarlo es inventarlo.", "Consulta a quien midió y a la enfermera antes de agregar un dato.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la trazabilidad de un registro?", "Poder saber quién registró qué y cuándo", "El tamaño de la letra de la planilla", "El número de hojas de la ficha", "La trazabilidad permite reconstruir quién anotó cada dato y en qué momento."),
        ("abc", "{F} ¿Qué falla tiene la fila 2?", "No tiene hora", "No tiene firma", "Tiene la unidad equivocada", "En la ficha, la fila 2 dice «sin hora», aunque tiene firma y unidad correcta."),
        ("abc", "{F} ¿Qué falla tiene la fila 3?", "La unidad no corresponde a la temperatura", "No tiene hora", "No tiene firma", "37 kg es una unidad de peso: la temperatura se anota en °C."),
        ("abc", "{F} ¿Qué falla tiene la fila 5?", "No tiene firma", "No tiene valor", "Tiene el dato tapado con corrector", "La ficha indica «sin firma»; el dato de esa fila sí está escrito."),
        ("=", "{F} ¿Cuántas filas cumplen toda la regla de la planilla?", "8-4", "Se restan de las 8 filas las 4 que tienen fallas.", " filas"),
        ("=", "{F} ¿Qué porcentaje de las filas cumple toda la regla?", "(8-4)*100//8", "Se divide la cantidad de filas correctas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} La fila 4 tiene el dato tapado con corrector. ¿Qué corresponde hacer?", "Informar a la enfermera y consultar a quien midió cuál era el valor", "Reemplazar el dato por el que parezca más probable", "Dejarla como está, porque tiene firma", "No se inventa el dato; se consulta a quien midió y se avisa para corregir con trazabilidad."),
        ("abc", "{F} Un técnico midió un pulso de 78 en otro paciente de ejemplo, pero escribió 87 en su planilla. ¿Cómo corrige el error?", "Traza una línea sobre el 87, escribe 78 al lado con hora y firma", "Lo tapa con corrector y escribe 78", "Borra el 87 con goma y escribe 78", "El dato original debe seguir legible; la corrección lleva hora y firma."),
        ("abc", "{F} Otro técnico quiere agregar la hora que falta en la fila 2, «porque seguro fue a las 10:00». ¿Qué corresponde?", "No agregar la hora sin confirmar con quien midió", "Agregarla, porque lo más probable es que sea correcta", "Borrar la fila para evitar problemas", "Una hora supuesta es un dato inventado; se confirma con quien midió."),
        ("abc", "{F} ¿Cuál es el motivo principal para exigir firma en cada fila?", "Que alguien responda por lo registrado", "Que la planilla se vea más ordenada", "Que el paciente sepa quién lo midió", "La firma permite responsabilizar y consultar a quien midió."),
        ("abc", "{F} Una enfermera ve que en las filas 1, 7 y 8 hay datos completos y firmados. ¿Qué significa para el uso de esas filas?", "Que cumplen la regla de la planilla y pueden usarse con más confianza", "Que no hace falta compararlas con nada más", "Que significan que el paciente está sano", "Cumplir la regla de la planilla no dice nada sobre el estado del paciente, solo sobre la calidad del registro."),
        ("=", "{F} ¿Cuántos latidos por minuto separan el pulso de la fila 2 del de la fila 7?", "82-76", "Se restan los valores de pulso de ambas filas.", " latidos por minuto"),
        ("abc", "{F} Al ver las fallas, un técnico dice: «Tiene que ser culpa del turno de la mañana». ¿Qué corresponde?", "Informar las fallas con hechos y dejar que la enfermera revise sin culpar a nadie", "Anotar el nombre del posible culpable en la planilla", "Corregir todas las filas él mismo", "Revisar un registro es detectar fallas con hechos, no buscar culpables."),
    ],
    ctx=("abc", "{F} Al cierre del turno, un técnico se da cuenta de que anotó 36 °C de temperatura en la fila de otro paciente por distracción. Nadie lo ha visto. ¿Qué hace?", "Corrige con una línea, la hora y su firma, y avisa a la enfermera del error", "Lo deja así, porque nadie lo notó", "Borra el dato y espera que nadie pregunte", "Reconocer y corregir con trazabilidad evita que un dato equivocado se use para decidir."),
    sc=[
        ("En Atención de Enfermería: ¿cómo se corrige un error de registro?", "Con una línea sobre el dato, el valor correcto al lado, hora y firma", "Así el dato original sigue legible y hay trazabilidad."),
        ("¿Qué cinco elementos debe tener una fila de la planilla?", "Hora, parámetro, valor, unidad y firma", "Son los que exige la regla de la planilla de ejemplo."),
        ("¿Qué haces si falta la firma en una fila de otro?", "Aviso a la enfermera y consulto a quien midió", "No se completan datos ajenos por suposición."),
    ],
    op=("Planilla de ejemplo con las mismas reglas de la ficha: «Fila A: 09:00, pulso 74 latidos por minuto, firma. Fila B: 10:00, presión sistólica 120, firma. Fila C: 11:00, temperatura 36 °C, sin firma. Fila D: 12:00, pulso 70 latidos por minuto, firma, dato tapado con corrector». "
        "Escribe: qué falla tiene cada fila con falla; cuántas filas cumplen la regla y qué porcentaje es; cómo se corrige un error bien hecho; y a quién avisas.",
        "Fila B: falta la unidad (mmHg). Fila C: sin firma. Fila D: dato tapado con corrector. Cumple solo la fila A: 1 de 4 = 25 %. Corrección: línea sobre el dato, valor correcto al lado, hora y firma. Aviso a la enfermera y consulta a quien midió.",
        ["identifica las tres fallas", "calcula 1 de 4 = 25 %", "describe la corrección con línea, hora y firma", "avisa a la enfermera"],
        ["hoja con fallas, un porcentaje, la forma de corregir y a quién avisa"],
        ["usar corrector", "completar datos que no midió", "no avisar a la enfermera"],
        "Pregunta: «¿tu corrección deja legible el dato original?». Si no, pídele rehacerla."),
    reinforce="Escribe los cinco elementos de una fila y una falla que pueda tener cada uno.",
    extend="Explica con un ejemplo inventado qué pasaría si una planilla con datos tapados se usara para decidir un cuidado.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (control semanal de ejemplo; valores inventados que no sirven como referencia clínica). Paciente de ejemplo, cama 8. Peso registrado cada lunes: semana 1, 64 kg; semana 2, 63 kg; semana 3, 61 kg; semana 4, 60 kg. "
     "Regla de la hoja (de ejemplo): avisar a la enfermera si el peso baja 3 kg o más respecto de la semana 1, o si baja 2 kg o más entre dos semanas seguidas. Talla registrada: 170 cm. "
     "Pulso del mismo día en tres horarios: 08:00, 74; 14:00, 82; 20:00, 78 latidos por minuto; límite de aviso de ejemplo: menor que 58 o mayor que 94.")
build(
    O2, 4, F,
    use="Aprenderé a calcular diferencias, promedios y cambios de una hoja de control con enteros y a aplicar la regla de aviso de la hoja sin interpretar.",
    prior=["Sé restar y dividir números enteros.", "Conozco los límites de aviso.", "Sé leer una tabla."],
    explain=[
        "En la hoja de control se hacen cuentas sencillas con los valores registrados. La diferencia entre dos registros se calcula restando el menor del mayor, por ejemplo 70 − 66 = 4. El promedio se calcula sumando varios valores y dividiéndolos por la cantidad de registros. El cambio entre dos semanas seguidas es la diferencia entre ambos pesos, y se compara con la regla que la enfermera escribió en la hoja.",
        "El técnico aplica la regla de la hoja: si el cambio llega al valor escrito, avisa; si no, solo registra. Calcular no es interpretar: el técnico no dice por qué cambió el peso ni qué conviene hacer. Para cuentas con unidades se verifica que sean iguales, por ejemplo, kilogramos con kilogramos, y se anotan siempre con su unidad.",
        "Los valores son inventados, solo para practicar la lectura de una planilla." + LIM,
    ],
    vocab=[("diferencia", "resultado de restar el valor menor del mayor"), ("promedio", "suma de valores dividida por la cantidad de valores"), ("cambio entre semanas", "diferencia entre los pesos de dos semanas seguidas"), ("regla de la hoja", "criterio escrito por la enfermera que dice cuándo avisar"), ("unidad", "medida con que se anota el valor, como kg o cm")],
    worked=[
        ("Aplicar la regla de la hoja", "Una hoja de ejemplo dice: «avisar si el peso baja 2 kg o más entre dos semanas seguidas». Un paciente de ejemplo pasó de 70 kg a 69 kg. ¿Corresponde avisar?", ["La baja es 70 − 69 = 1 kg.", "1 kg es menor que 2 kg, por lo que la regla no se cumple."], "No corresponde avisar por esa regla; se registra"),
        ("Calcular un promedio", "Tres pulsos de ejemplo de otra hoja son 66, 72 y 78 latidos por minuto. ¿Cuál es el promedio?", ["66 + 72 + 78 = 216.", "216 ÷ 3 = 72."], "72 latidos por minuto"),
    ],
    mistakes=[("Restar kilogramos con centímetros porque «son números».", "Las unidades distintas no se pueden restar entre sí y el resultado no tiene sentido.", "Compara siempre mismas unidades y escribe la unidad del resultado."),
              ("Decirle al paciente «estás bajando de peso, no te preocupes».", "Es una interpretación y un consejo que le corresponde al profesional.", "Registra e informa a la enfermera; no interpretes ante el paciente.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿cómo se calcula la diferencia entre dos pesos registrados?", "Restando el menor del mayor", "Sumándolos y dividiendo por dos", "Multiplicando ambos valores", "La diferencia es el resultado de restar el valor menor del mayor."),
        ("abc", "{F} ¿Cuál es el peso registrado en la semana 3?", "61 kg", "63 kg", "60 kg", "La ficha anota 61 kg en la semana 3; los otros pesos son de las semanas 2 y 4."),
        ("=", "{F} ¿Cuántos kg bajó el peso entre la semana 1 y la semana 4?", "64-60", "Se resta el peso de la semana 4 del de la semana 1.", " kg"),
        ("=", "{F} ¿Cuál es el pulso promedio de los tres horarios?", "(74+82+78)//3", "Se suman los tres pulsos y se dividen entre 3.", " latidos por minuto"),
        ("=", "{F} ¿Cuántos kg bajó el peso entre la semana 2 y la semana 3?", "63-61", "Se resta el peso de la semana 3 del de la semana 2.", " kg"),
        ("abc", "{F} Según la regla de la hoja, ¿qué corresponde por la baja entre la semana 2 y la 3?", "Avisar a la enfermera, porque bajó 2 kg entre dos semanas seguidas", "No avisar, porque 2 kg es poco", "Esperar a la semana 4 para decidir", "La regla dice avisar si baja 2 kg o más entre dos semanas seguidas; aquí bajó 2 kg."),
        ("abc", "{F} Según la regla de la hoja, ¿qué corresponde por la baja entre la semana 1 y la 4?", "Avisar a la enfermera, porque bajó 3 kg o más respecto de la semana 1", "No avisar, porque no bajó 5 kg", "Avisar solo si el paciente lo pide", "La baja total es de 4 kg, que supera el límite de 3 kg de la hoja."),
        ("abc", "{F} ¿Los pulsos de las 08:00, 14:00 y 20:00 sobrepasan el límite de aviso de ejemplo?", "No: los tres están entre 58 y 94", "Sí: el de las 14:00 sobrepasa el límite", "Sí: el de las 08:00 está bajo el límite", "Los tres valores (74, 82 y 78) están dentro de los límites; solo se registran."),
        ("=", "{F} ¿Cuántos latidos por minuto separan el pulso más alto del más bajo del día?", "82-74", "Se resta el pulso más bajo del más alto.", " latidos por minuto"),
        ("abc", "{F} El paciente de la cama 8 pregunta si su baja de peso es mala. ¿Qué responde el técnico?", "Que la enfermera o el médico le explicará su resultado", "Que es normal a su edad", "Que es una señal de que algo grave está pasando", "Interpretar un resultado no le corresponde al técnico; se deriva con respeto al profesional."),
        ("abc", "{F} Un compañero restó 170 cm de talla de 64 kg de peso para ver «cuánto sobra». ¿Qué falla tiene la cuenta?", "Mezcla unidades distintas, por lo que el resultado no tiene sentido", "Falta multiplicar por la edad", "Debería usar solo la talla de la semana 1", "kg y cm son magnitudes distintas y no se pueden restar entre sí."),
        ("=", "{F} Si el peso siguiera bajando 1 kg por semana después de la semana 4, ¿cuántos kg marcaría la hoja en la semana 6?", "60-2", "Se restan 2 kg del peso de la semana 4 (dos semanas más).", " kg"),
        ("abc", "{F} Una técnica anota en la hoja «peso: 60» y deja la casilla de unidad vacía. ¿Qué falla tiene?", "Falta la unidad, por lo que el registro es incompleto", "Debería estar escrito en letras", "Está bien, porque la unidad se sobreentiende", "Sin la unidad no se sabe si 60 son kg u otra medida; el registro debe estar completo."),
    ],
    ctx=("abc", "{F} Al anotar el peso de la semana 4, la técnica calcula la baja respecto de la semana 1 y ve que llega al límite de la regla. Además el paciente dice que últimamente come menos. ¿Qué hace?", "Registra el peso y el comentario del paciente tal como los oyó, y avisa a la enfermera", "Le explica que debe comer más para no seguir bajando", "No anota el comentario porque no es un dato medido", "Registra lo medido y lo dicho por el paciente, y la enfermera decide; el técnico no da consejos clínicos."),
    sc=[
        ("En Atención de Enfermería: ¿cómo se calcula un promedio?", "Se suman los valores y se divide por la cantidad de valores", "Así se obtiene un valor representativo de varios registros."),
        ("¿Qué haces cuando el cambio llega al límite de la hoja?", "Aviso a la enfermera", "La regla de la hoja indica cuándo avisar."),
        ("¿Se pueden restar kg con cm?", "No, porque son unidades distintas", "Solo se comparan valores con la misma unidad."),
    ],
    op=("Hoja de ejemplo (valores inventados): «Cama 12. Peso semanal: 58, 57, 54, 53 kg. Regla de la hoja: avisar si baja 3 kg o más entre dos semanas seguidas, o 4 kg o más respecto de la semana 1. Pulso de las 09:00, 15:00 y 21:00: 70, 76, 82; límite de aviso de ejemplo: mayor que 90». "
        "Calcula: los cambios entre semanas seguidas y la baja desde la semana 1; el promedio de pulso. Escribe: si corresponde avisar por el peso y por qué; si corresponde avisar por el pulso; y una frase de registro sin interpretar.",
        "Cambios: 1, 3, 1; baja total: 58 − 53 = 5. Avisar por el peso: sí, porque entre las semanas 2 y 3 bajó 3 kg y respecto de la semana 1 bajó 5 kg. Pulso promedio: (70+76+82)÷3 = 76; no sobrepasa el límite, solo se registra. Registro: «Peso semana 4: 53 kg; baja total 5 kg; se avisó a la enfermera».",
        ["calcula los cambios y la baja total", "aplica la regla de la hoja", "calcula el promedio 76", "el registro no interpreta"],
        ["hoja con cambios, promedio, decisión de avisar y una frase de registro"],
        ["restar mal", "decidir si es grave o no", "dar consejos al paciente"],
        "Pregunta: «¿tu frase explica por qué bajó el peso o solo cuenta lo medido?». Si lo explica, pídele quitar la interpretación."),
    reinforce="Con los pesos 80, 79 y 76 kg de tres semanas seguidas, calcula la diferencia entre semanas y entre la primera y la tercera.",
    extend="Explica con un ejemplo inventado por qué calcular no es lo mismo que interpretar.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (centro de salud de ejemplo, inventado). En el «Centro de Salud Familiar Ejemplo Norte» la enfermera organiza un taller de alimentación saludable para familias, de 17:00 a 18:30. Se invitó a 40 personas y en la sala caben 36 sentadas. "
     "La enfermera dirige el taller; el técnico en enfermería la apoya con la lista de asistencia y el material. Se prepararon 9 grupos de 4 personas y cada grupo recibe 3 hojas de trabajo. "
     "Regla del centro: la lista de asistencia es reservada y no se toman fotos de las personas sin su autorización por escrito.")
build(
    O3, 1, F,
    use="Aprenderé qué es promover la salud y prevenir enfermedades, qué rol tiene el técnico en una actividad con familias y qué reglas de respeto y reserva debe cumplir.",
    prior=["Sé qué hace el técnico en enfermería.", "Sé calcular horas y minutos.", "Sé dividir en grupos iguales."],
    explain=[
        "En Atención de Enfermería, la promoción de la salud son las acciones para que las personas y las comunidades cuiden y mejoren su salud, por ejemplo aprendiendo hábitos de alimentación saludable. La prevención son las acciones para evitar que una enfermedad aparezca o empeore. Ambas se hacen sobre todo en la atención primaria, que es el primer nivel de atención: consultorios y centros de salud cerca de donde vive la gente.",
        "Estas actividades siguen las orientaciones de las políticas de salud y de la autoridad sanitaria. Por eso las dirige o supervisa un profesional, y el técnico apoya con la organización, la asistencia y el material. El técnico no da consejos clínicos personales ni opina sobre una enfermedad o un tratamiento: si alguien pregunta por su caso, lo deriva con respeto a la enfermera o al profesional del centro.",
        "Los datos de las personas, como la lista de asistencia, son reservados, y las fotos requieren autorización escrita. Si alguien se siente mal durante la actividad, el técnico avisa de inmediato a la enfermera y a emergencias." + LIM,
    ],
    vocab=[("promoción de la salud", "acciones para que las personas cuiden y mejoren su salud"), ("prevención", "acciones para evitar que una enfermedad aparezca o empeore"), ("atención primaria", "primer nivel de atención, en consultorios y centros de salud cercanos"), ("taller educativo", "actividad en grupo para aprender hábitos de salud"), ("lista de asistencia", "registro reservado de las personas que participan"), ("derivar", "enviar una consulta o un caso al profesional que corresponde")],
    worked=[
        ("Qué hace el técnico ante una consulta personal", "En un taller de ejemplo, un asistente pregunta si puede dejar un medicamento que le recetaron. ¿Qué corresponde?", ["Los medicamentos los indica el profesional que los recetó.", "El técnico no opina: deriva la consulta a la enfermera o al profesional del centro."], "Derivar la consulta a la enfermera o al profesional, sin opinar"),
        ("Dividir el tiempo", "Otro taller de ejemplo dura 60 minutos y se divide en 4 bloques iguales. ¿Cuántos minutos dura cada bloque?", ["Se divide la duración total entre los bloques.", "60 ÷ 4 = 15."], "15 minutos"),
    ],
    mistakes=[("Responder «yo que usted dejaría ese medicamento» a un asistente.", "Es un consejo clínico personal y puede perjudicarlo; solo lo da un profesional que conoce su caso.", "Deriva la consulta a la enfermera o al profesional del centro."),
              ("Dejar la lista de asistencia a la vista sobre una mesa del taller.", "Cualquier persona podría leer los datos de las familias.", "Guarda la lista y entrégala solo a quien corresponde.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la promoción de la salud?", "Acciones para que las personas cuiden y mejoren su salud, como aprender hábitos saludables", "El tratamiento de una enfermedad ya diagnosticada", "La toma de exámenes de laboratorio", "La promoción busca que las personas cuiden su salud; tratar o examinar son otras acciones."),
        ("abc", "{F} ¿Quién dirige el taller?", "La enfermera", "El técnico en enfermería", "Una persona de las familias invitadas", "La ficha dice que la enfermera dirige y el técnico la apoya."),
        ("abc", "{F} ¿Qué hace el técnico durante el taller?", "Apoya con la lista de asistencia y el material", "Responde consultas clínicas personales de los asistentes", "Decide los contenidos del taller", "El técnico apoya la organización; los contenidos y la atención clínica son del profesional."),
        ("=", "{F} ¿Cuántas personas invitadas quedan sin cupo sentado?", "40-36", "Se restan los cupos sentados de las personas invitadas.", " personas"),
        ("abc", "{F} Una madre le pide al técnico que mire a su hijo y le diga si tiene sobrepeso. ¿Qué corresponde?", "Derivarla a la enfermera o al profesional del centro, sin evaluar ni opinar", "Mirarlo y darle su opinión de forma amable", "Decirle que lo averigüe por internet", "Evaluar a una persona y dar consejos personales le corresponde a un profesional que conoce su caso."),
        ("=", "{F} ¿Cuántos minutos dura el taller?", "(18*60+30)-(17*60)", "Se restan la hora de inicio de la hora de término, ambas en minutos.", " minutos"),
        ("=", "{F} ¿Cuántas hojas de trabajo hay que preparar para todos los grupos?", "9*3", "Se multiplica la cantidad de grupos por las hojas de cada grupo.", " hojas"),
        ("abc", "{F} Un compañero propone fotografiar a los asistentes para publicar el taller en redes. ¿Qué corresponde según la regla del centro?", "No tomar fotos de las personas sin su autorización por escrito", "Tomarlas, porque es un taller público", "Tomarlas solo de espaldas, sin pedir permiso", "La regla del centro exige autorización escrita para fotografiar a las personas."),
        ("abc", "{F} Una asistente cuenta que es alérgica a un alimento y que en la actividad se ofrecerá una merienda. ¿Qué corresponde?", "Avisar a la enfermera y no ofrecerle ese alimento", "Ofrecérselo en poca cantidad", "Decirle que no es una alergia grave", "Se avisa a la profesional responsable y no se ofrece lo que podría dañar a la persona."),
        ("=", "{F} Si al taller llegaron 27 de las 36 personas que tenían cupo, ¿qué porcentaje de los cupos se ocupó?", "27*100//36", "Se divide la asistencia entre los cupos y se multiplica por 100.", " %"),
        ("abc", "{F} Una participante se desmaya durante el taller. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias", "Le da algo de beber y espera a que despierte", "La levanta y la lleva afuera", "Ante un desmayo no se actúa por cuenta propia: se avisa de inmediato a la enfermera y a emergencias."),
        ("abc", "{F} Un afiche del taller dice: «Quien come mal es porque no le importa su familia». ¿Qué corresponde?", "Proponerle a la enfermera cambiarlo por un mensaje respetuoso y sin culpa", "Colocarlo, porque llama la atención", "Colocarlo solo en la entrada", "Un mensaje que culpa a las personas puede alejarlas; la promoción debe ser respetuosa."),
        ("abc", "En Atención de Enfermería: ¿por qué las actividades de promoción siguen las orientaciones de la autoridad sanitaria?", "Para que el contenido sea correcto y coherente con las políticas de salud", "Para que cada técnico invente su propio taller", "Para evitar que participen las familias", "Las orientaciones aseguran contenidos correctos y comunes en todos los centros."),
    ],
    ctx=("abc", "{F} Al terminar el taller, una familia pide al técnico el teléfono de otra familia que asistió «para conversar de lo que se habló». ¿Qué hace?", "No entrega datos de otras personas y ofrece que la enfermera entregue su contacto a la otra familia, si ella lo autoriza", "Entrega el teléfono, porque es de la comunidad", "Le muestra la lista de asistencia para que lo busque", "Los datos de las personas son reservados; solo se comparten con su autorización."),
    sc=[
        ("En Atención de Enfermería: ¿qué diferencia hay entre promoción y prevención?", "La promoción fortalece la salud; la prevención evita que una enfermedad aparezca o empeore", "Una busca mejorar hábitos y la otra evitar enfermedades."),
        ("¿Qué haces si un asistente te consulta por su caso personal?", "Lo derivo a la enfermera o al profesional", "Los consejos clínicos personales los da quien conoce su caso."),
        ("En Atención de Enfermería: ¿qué haces si alguien se siente mal durante el taller con familias?", "Aviso de inmediato a la enfermera y a emergencias", "No actúo por cuenta propia; pido ayuda a quien corresponde."),
    ],
    op=("Caso de ejemplo: la enfermera te pide apoyar un taller de actividad física para adultos mayores de un club de ejemplo, de 16:00 a 17:00, con 24 invitados, en grupos de 6 personas y con 2 folletos por grupo. "
        "Escribe: cuántos grupos y cuántos folletos hacen falta; dos tareas del técnico antes y durante el taller; qué harías si un asistente te pide un consejo para su dolor de rodilla; y qué harías si alguien dice sentirse mal.",
        "Grupos: 24 ÷ 6 = 4; folletos: 4 × 2 = 8. Antes: ordenar las sillas y el material, preparar la lista de asistencia; durante: apoyar la lista y el material. Dolor de rodilla: derivar a la enfermera, sin dar consejos. Si alguien se siente mal: avisar de inmediato a la enfermera y a emergencias, sin actuar por cuenta propia.",
        ["calcula 4 grupos y 8 folletos", "nombra tareas de apoyo", "deriva la consulta personal", "avisa de inmediato ante un malestar"],
        ["hoja con cálculos, tareas, derivación y aviso"],
        ["dar un consejo para el dolor de rodilla", "actuar por cuenta propia ante el malestar", "calcular mal los grupos"],
        "Pregunta: «¿tu respuesta ante el dolor de rodilla dice qué hace el técnico o qué debería hacer la persona?». Si lo segundo, pídele reescribirla como derivación."),
    reinforce="Escribe tres cosas que hace el técnico en un taller de salud y tres que solo hace la enfermera o el profesional.",
    extend="Explica con un ejemplo inventado por qué un mensaje de salud que culpa a las personas puede alejarlas del centro.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (actividades de un centro de salud de ejemplo, inventado). A: taller de alimentación saludable para familias. B: jornada de vacunación de la comunidad. C: jornada de detección temprana de una enfermedad con un examen. "
     "D: grupo de apoyo para personas que ya viven con una enfermedad crónica, para evitar complicaciones. E: feria saludable con juegos y actividad física al aire libre. "
     "Clasificación del centro: promoción, A y E; prevención primaria, B; prevención secundaria, C; prevención terciaria, D. Asistentes registrados: A 24, B 80, C 36, D 18, E 62.")
build(
    O3, 2, F,
    use="Aprenderé los tipos de prevención, qué son los factores protectores y de riesgo, qué es una alimentación saludable en general y qué documentos se usan en una actividad educativa.",
    prior=["Sé qué es promoción y prevención.", "Sé sumar y comparar números.", "Sé leer una ficha."],
    explain=[
        "La prevención se clasifica en tres niveles. La prevención primaria evita que la enfermedad aparezca, por ejemplo con vacunas. La prevención secundaria busca detectarla pronto, por ejemplo con un examen de detección, para actuar a tiempo. La prevención terciaria busca evitar complicaciones en quien ya vive con una enfermedad. La promoción de la salud es distinta: fortalece hábitos y entornos saludables.",
        "Un factor protector es algo que ayuda a cuidar la salud, como una alimentación variada, el movimiento y el apoyo de la familia. Un factor de riesgo es algo que aumenta la probabilidad de enfermar, como el consumo excesivo de azúcar o el sedentarismo. En general, una alimentación saludable es variada, incluye agua, frutas y verduras y modera la sal, el azúcar y las grasas; las guías precisas las define la autoridad sanitaria.",
        "Los documentos de estas actividades son el afiche, el folleto y el registro de la actividad, con fecha, tema, responsable y asistentes. El registro no incluye datos clínicos de las personas." + LIM,
    ],
    vocab=[("prevención primaria", "evita que la enfermedad aparezca, por ejemplo con vacunas"), ("prevención secundaria", "detecta la enfermedad a tiempo, por ejemplo con un examen de detección"), ("prevención terciaria", "evita complicaciones en quien ya vive con una enfermedad"), ("factor protector", "algo que ayuda a cuidar la salud"), ("factor de riesgo", "algo que aumenta la probabilidad de enfermar"), ("registro de la actividad", "documento con fecha, tema, responsable y asistentes de una actividad educativa")],
    worked=[
        ("Clasificar una actividad", "En un centro de ejemplo se realiza una campaña de vacunación escolar. ¿Qué tipo de prevención es?", ["Las vacunas evitan que la enfermedad aparezca.", "Eso es prevención primaria."], "Prevención primaria"),
        ("Total de asistentes", "En otra jornada de ejemplo asistieron 45 personas el sábado y 38 el domingo. ¿Cuántas asistieron en total?", ["Se suman las asistencias de ambos días.", "45 + 38 = 83."], "83 personas"),
    ],
    mistakes=[("Decir que un examen de detección es prevención primaria porque «previene».", "No evita que la enfermedad aparezca: la detecta a tiempo, y eso es prevención secundaria.", "Pregunta si la acción evita la aparición, detecta a tiempo o evita complicaciones."),
              ("Anotar en el registro de la actividad la enfermedad de cada asistente.", "Son datos clínicos reservados que no corresponden a ese documento.", "Anota solo fecha, tema, responsable y asistencia.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un factor protector?", "Algo que ayuda a cuidar la salud, como una alimentación variada", "Algo que aumenta la probabilidad de enfermar", "Un diagnóstico escrito por el médico", "Un factor protector favorece la salud; el que aumenta la probabilidad de enfermar es de riesgo."),
        ("abc", "{F} ¿Qué tipo de prevención corresponde a la actividad B?", "Prevención primaria", "Prevención secundaria", "Prevención terciaria", "La vacunación evita que la enfermedad aparezca, por lo que es prevención primaria."),
        ("abc", "{F} ¿Qué tipo de prevención corresponde a la actividad C?", "Prevención secundaria", "Prevención primaria", "Promoción de la salud", "La detección temprana con un examen es prevención secundaria."),
        ("abc", "{F} ¿Qué tipo de prevención corresponde a la actividad D?", "Prevención terciaria", "Prevención secundaria", "Prevención primaria", "El grupo busca evitar complicaciones en personas que ya viven con una enfermedad."),
        ("=", "{F} ¿Cuántas personas asistieron en total a las cinco actividades?", "24+80+36+18+62", "Se suman los asistentes de las actividades A, B, C, D y E.", " personas"),
        ("=", "{F} ¿Cuántas personas más asistieron a la actividad B que a la actividad D?", "80-18", "Se resta la asistencia de D de la de B.", " personas"),
        ("=", "{F} ¿Cuántas personas asistieron a las actividades de promoción (A y E)?", "24+62", "Se suman los asistentes de las dos actividades clasificadas como promoción.", " personas"),
        ("abc", "{F} ¿Qué actividad de la ficha es de promoción de la salud?", "La feria saludable con juegos y actividad física", "La jornada de detección temprana con un examen", "El grupo de apoyo para evitar complicaciones", "Una feria saludable fortalece hábitos; la detección y el grupo de apoyo son prevención."),
        ("abc", "¿Cuál de estas es un factor de riesgo?", "El consumo excesivo de azúcar durante largos períodos", "El apoyo de la familia", "Dormir lo suficiente", "El consumo excesivo de azúcar aumenta la probabilidad de enfermar; las otras opciones son protectoras."),
        ("abc", "{F} Un compañero propone anotar en el registro de la actividad D la enfermedad de cada participante. ¿Qué corresponde?", "No anotarlo, porque son datos clínicos reservados", "Anotarlo, porque es una actividad del mismo centro", "Anotarlo solo de quienes lo pidan", "El registro de la actividad lleva fecha, tema, responsable y asistencia, no datos clínicos."),
        ("abc", "En Atención de Enfermería: ¿qué características tiene, en general, una alimentación saludable?", "Es variada, incluye agua, frutas y verduras y modera la sal, el azúcar y las grasas", "Consiste en comer una sola clase de alimento", "Evita todos los alimentos con azúcar siempre", "La alimentación saludable es variada y moderada; las guías precisas las fija la autoridad sanitaria."),
        ("=", "{F} Si cada asistente de la actividad A recibe 2 folletos y se agregan 6 de repuesto, ¿cuántos folletos se preparan?", "24*2+6", "Se multiplican los folletos por asistente y se suman los de repuesto.", " folletos"),
        ("abc", "{F} Una persona que asistió a la actividad C le pide al técnico que le explique el resultado de su examen. ¿Qué corresponde?", "Derivarla a la enfermera o al profesional que le informará su resultado", "Explicarle el resultado, porque asistió a la jornada", "Decirle que no se preocupe, sin ver el resultado", "Interpretar exámenes le corresponde al profesional; el técnico deriva con respeto."),
    ],
    ctx=("abc", "{F} Al preparar el registro de la feria saludable, la enfermera pide anotar la cantidad de asistentes. El técnico contó 62, pero una familia llegó tarde y no firmó la lista. ¿Qué hace?", "Anota los 62 que contó y deja constancia de que una familia no firmó la lista", "Anota solo los que firmaron y no dice nada", "Anota una cifra mayor para que el centro luzca bien", "El registro debe ser fiel a lo ocurrido; se deja constancia de lo que no se pudo registrar."),
    sc=[
        ("En Atención de Enfermería: ¿qué tipo de prevención evita que la enfermedad aparezca?", "La prevención primaria", "Las vacunas son un ejemplo de prevención primaria."),
        ("¿Qué datos lleva el registro de una actividad educativa?", "Fecha, tema, responsable y asistentes", "No lleva datos clínicos de las personas."),
        ("¿Quién interpreta el resultado de un examen?", "El profesional que corresponde", "El técnico no interpreta exámenes: eso lo hace el profesional."),
    ],
    op=("Ficha de ejemplo: «Un centro realiza cuatro actividades: (1) un taller para dormir mejor, (2) un examen de detección en el barrio, (3) una vacunación escolar y (4) un grupo de apoyo para personas con una enfermedad crónica. Asistentes: 18, 30, 54 y 12». "
        "Escribe: qué tipo es cada actividad (promoción, prevención primaria, secundaria o terciaria); cuántas personas asistieron en total; un factor protector y uno de riesgo que podrías nombrar en el taller; y qué anotarías en el registro de la actividad (1).",
        "1: promoción; 2: prevención secundaria; 3: prevención primaria; 4: prevención terciaria. Total: 18+30+54+12 = 114. Factor protector: dormir lo suficiente; de riesgo: dormir muy poco por muchos días. Registro: fecha, tema, responsable (la enfermera) y 18 asistentes, sin datos clínicos.",
        ["clasifica bien las cuatro actividades", "suma 114 personas", "nombra un factor protector y uno de riesgo", "registra solo datos permitidos"],
        ["hoja con una clasificación, un total, dos factores y un registro"],
        ["confundir detección con prevención primaria", "anotar datos clínicos en el registro", "sumar mal"],
        "Pregunta: «¿el examen de detección evita que la enfermedad aparezca o la encuentra a tiempo?». Debe responder que la encuentra a tiempo."),
    reinforce="Escribe una actividad de ejemplo para cada uno de los tres tipos de prevención y una de promoción.",
    extend="Explica con un ejemplo inventado por qué la vacunación y la detección temprana no son la misma clase de prevención.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (pauta de revisión de afiches, de ejemplo). Criterios: (1) mensaje claro y corto; (2) respetuoso, sin culpar; (3) sin diagnósticos ni consejos personales; (4) coherente con las orientaciones de la autoridad sanitaria; (5) incluye a todas las familias y no usa estereotipos. "
     "Afiche A: «Come variado: más verduras y agua, menos azúcar», con una sola imagen de una familia de padre, madre e hijos; cumple los criterios 1, 2, 3 y 4. "
     "Afiche B: «Si eres gordo, estás enfermo», con una imagen de burla; cumple solo el criterio 1. "
     "Afiche C: «Cuidemos juntos nuestra salud: caminemos en comunidad», con imágenes de personas de distintas edades y de una persona en silla de ruedas; cumple los criterios 1, 2, 3, 4 y 5. "
     "Afiche D: «Toma este suplemento y bajarás 5 kilos en una semana», con la marca de un producto de ejemplo; cumple los criterios 1, 2 y 5.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un material de promoción con una pauta de criterios, a reconocer mensajes que culpan o dan consejos personales y a proponer mejoras.",
    prior=["Conozco la promoción de la salud y los tipos de prevención.", "Sé calcular porcentajes de números enteros.", "Conozco los derechos de las personas."],
    explain=[
        "Para analizar un material de promoción, como un afiche, se lee con una pauta de criterios y se marca cuáles cumple. Un buen afiche es claro y corto, respeta a las personas sin culparlas, no da diagnósticos ni consejos personales, se basa en las orientaciones de la autoridad sanitaria y incluye a todas las familias sin estereotipos. Se corrige lo que falla, no se castiga a quien lo hizo.",
        "Un mensaje que culpa o se burla puede avergonzar a las personas y alejarlas del centro de salud. Un mensaje que promete resultados rápidos con un producto no es promoción de la salud, sino publicidad, y no corresponde a un centro de salud. Los estereotipos, como mostrar a un solo tipo de familia, dejan fuera a quienes no se ven reflejados, y la inclusión significa que todos puedan sentirse parte.",
        "El técnico propone mejoras a la enfermera; no decide por sí solo qué se publica." + LIM,
    ],
    vocab=[("pauta de criterios", "lista de condiciones que se revisan una por una"), ("estereotipo", "imagen simplificada que deja fuera la diversidad de las personas"), ("inclusión", "que todas las personas puedan sentirse parte"), ("mensaje de promoción", "texto que invita a cuidar la salud de forma clara y respetuosa"), ("publicidad de un producto", "mensaje que busca vender algo y no promover la salud"), ("mejora", "cambio propuesto para que el material cumpla los criterios")],
    worked=[
        ("Revisar un criterio", "Un afiche de ejemplo dice: «Quien no hace deporte es flojo». ¿Qué criterio incumple?", ["El mensaje juzga y culpa a las personas.", "Incumple el criterio 2: ser respetuoso, sin culpar."], "El criterio 2"),
        ("Calcular el cumplimiento", "Otro afiche de ejemplo cumple 3 de los 5 criterios. ¿Qué porcentaje cumple?", ["3 × 100 = 300.", "300 ÷ 5 = 60."], "60 %"),
    ],
    mistakes=[("Aceptar un afiche que promete «bajar 5 kilos en una semana» porque llama la atención.", "Promete resultados que no se pueden asegurar y vende un producto en vez de promover la salud.", "Propón cambiarlo por un mensaje de hábitos saludables, sin marcas ni promesas."),
              ("Cambiar el afiche y publicarlo sin consultar a la enfermera.", "La decisión sobre los materiales es del profesional responsable.", "Propón la mejora a la enfermera y espera su decisión.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es un estereotipo en un afiche?", "Una imagen simplificada que deja fuera la diversidad de las personas", "Un número que indica cuántas personas asistieron", "El logotipo del centro de salud", "Un estereotipo muestra solo un tipo de persona o de familia y excluye a otros."),
        ("abc", "{F} ¿Qué criterio no cumple el afiche A?", "El criterio 5: incluye a todas las familias y no usa estereotipos", "El criterio 1: mensaje claro y corto", "El criterio 3: sin consejos personales", "El afiche A muestra solo una familia de padre, madre e hijos, lo que deja fuera a otras familias."),
        ("abc", "{F} ¿Cuál es el único criterio que cumple el afiche B?", "El criterio 1: mensaje claro y corto", "El criterio 2: respetuoso, sin culpar", "El criterio 5: incluye a todas las familias", "La ficha dice que el afiche B cumple solo el criterio 1; se burla de las personas y da un diagnóstico."),
        ("=", "{F} ¿Cuántos criterios cumplen en total los cuatro afiches?", "4+1+5+3", "Se suman los criterios cumplidos por cada afiche.", " criterios"),
        ("=", "{F} Si cada afiche se evalúa con 5 criterios, ¿qué porcentaje de los criterios cumplen en total los cuatro afiches?", "(4+1+5+3)*100//(4*5)", "Se suman los criterios cumplidos, se multiplica por 100 y se divide por el total de criterios evaluados.", " %"),
        ("abc", "{F} ¿Cuál es el afiche que cumple todos los criterios?", "El afiche C", "El afiche A", "El afiche D", "Solo el afiche C cumple los 5 criterios de la pauta."),
        ("abc", "{F} ¿Por qué el afiche D no corresponde a un centro de salud?", "Promete un resultado rápido con un producto y es publicidad, no promoción de la salud", "Porque usa colores muy llamativos", "Porque es demasiado largo", "Prometer bajar 5 kilos con un producto vende algo y puede inducir a error; no es promoción."),
        ("abc", "{F} ¿Qué mejora propondría el técnico al afiche A?", "Agregar imágenes de distintos tipos de familias", "Quitar el mensaje sobre verduras y agua", "Agregar una marca de alimentos", "La inclusión se mejora mostrando la diversidad de las familias."),
        ("abc", "{F} El técnico ve el afiche B colgado en la sala de espera. ¿Qué hace?", "Informa a la enfermera que no cumple la pauta y propone retirarlo", "Lo retira y lo bota sin avisar", "Lo deja colgado, porque nadie se ha quejado", "La decisión sobre el material es del profesional responsable; se informa con hechos."),
        ("abc", "{F} Un compañero dice: «El afiche C tiene una persona en silla de ruedas, entonces es mejor que el A solo por eso». ¿Qué corresponde responder?", "Que se evalúan los cinco criterios y el C cumple todos, no solo uno", "Que sí, porque lo que importa es la imagen", "Que no, porque el A tiene más texto", "La pauta evalúa varios criterios; la inclusión es uno de ellos."),
        ("abc", "{F} Una persona de la comunidad dice que el afiche B le dio vergüenza. ¿Qué corresponde hacer?", "Escucharla con respeto, informar a la enfermera y no justificar el afiche", "Decirle que tiene razón en sentirse así", "Decirle que no se ofenda, porque es solo un afiche", "Se escucha y se informa para corregir el material; minimizar el malestar aleja a las personas."),
        ("=", "{F} Si el afiche D se corrigiera para cumplir además el criterio 3, ¿cuántos criterios cumpliría?", "3+1", "Se suma el criterio corregido a los tres que ya cumplía.", " criterios"),
        ("abc", "En Atención de Enfermería: ¿qué debe hacer el técnico si cree que un afiche debe cambiarse?", "Proponer la mejora a la enfermera y esperar su decisión", "Cambiarlo él mismo y avisar después", "Pedir la opinión del público antes de avisar", "La responsable de los materiales es la enfermera; el técnico propone."),
    ],
    ctx=("abc", "{F} La enfermera pide al técnico escribir un afiche sobre hábitos saludables para el centro. El técnico quiere incluir la frase «Si no te cuidas, te mueres». ¿Qué corresponde?", "Proponer una frase positiva y respetuosa, y mostrarla a la enfermera antes de usarla", "Usarla, porque la urgencia convence", "Usarla en letra pequeña", "Un mensaje de miedo y culpa puede alejar a las personas; la enfermera revisa los textos antes de publicarlos."),
    sc=[
        ("En Atención de Enfermería: ¿qué debe hacer un mensaje de promoción?", "Invitar a cuidar la salud de forma clara y respetuosa", "No culpa, no promete y no da consejos clínicos personales."),
        ("En Atención de Enfermería: ¿cuántos criterios tiene la pauta de revisión de afiches de la ficha?", "5", "Claridad, respeto, sin consejos personales, coherencia con la autoridad sanitaria e inclusión."),
        ("¿Quién decide qué material se publica?", "La enfermera o el profesional responsable", "El técnico propone, el profesional decide."),
    ],
    op=("Afiche de ejemplo: «¡Tú eliges! Si no haces ejercicio hoy, mañana será tarde. Compra la bebida energética X, la marca de ejemplo, y verás resultados». La imagen muestra solo a un joven delgado. "
        "Usa los criterios de la ficha. Escribe: qué criterios cumple y cuáles no (cuenta cuántos de 5 cumple); cómo lo mejorarías con una frase nueva; y a quién propondrías el cambio.",
        "Cumple el criterio 1 (es corto). No cumple el 2 (culpa y presiona), el 3 (promete resultados), el 4 (es publicidad de un producto) ni el 5 (solo muestra a un joven delgado): cumple 1 de 5. Frase nueva: «Movernos un poco cada día nos hace bien: caminemos juntos». Propondría el cambio a la enfermera.",
        ["cuenta 1 de 5 criterios cumplidos", "identifica culpa, promesa, publicidad y estereotipo", "propone una frase respetuosa y sin marca", "propone el cambio a la enfermera"],
        ["hoja con criterios, una frase nueva y a quién propone"],
        ["mantener la marca del producto", "decidir cambiar el afiche sin consultar", "olvidar el criterio de inclusión"],
        "Pregunta: «¿tu frase nueva incluye una marca o una promesa?». Si sí, pídele sacarla."),
    reinforce="Elige uno de los afiches de la ficha que no cumpla algún criterio y reescribe su mensaje para que cumpla todos.",
    extend="Explica con un ejemplo inventado por qué mostrar un solo tipo de familia puede dejar fuera a personas de la comunidad.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (registro del trimestre de un centro de salud de ejemplo, inventado). Actividad educativa mensual para familias. Mes 1: invitadas 60 familias, asistieron 36. Mes 2: invitadas 50, asistieron 40. Mes 3: invitadas 90, asistieron 54. "
     "Meta del centro (de ejemplo): que asista al menos el 70 % de las familias invitadas en cada actividad. Material: 1 folleto por cada familia asistente y 10 folletos de repuesto por actividad. "
     "Regla: el registro lleva solo cantidades; los nombres de las familias están en la lista reservada y no se copian al informe.")
build(
    O3, 4, F,
    use="Aprenderé a calcular la cobertura y la asistencia de actividades de promoción, a comparar con una meta y a informar con cantidades sin exponer datos de personas.",
    prior=["Sé calcular porcentajes de números enteros.", "Sé sumar y restar.", "Conozco el registro de una actividad."],
    explain=[
        "La asistencia es cuántas personas o familias llegaron a una actividad. La cobertura es la proporción de las invitadas que asistió, expresada en porcentaje: se multiplica la asistencia por 100 y se divide por las invitadas. Por ejemplo, si asisten 24 de 30 invitadas, la cobertura es 80 %, porque 24 por 100 dividido por 30 da 80. Una meta es un porcentaje que el centro se propone alcanzar.",
        "Al comparar la cobertura con la meta se ve si se cumplió; si no, la enfermera analiza las razones, como el horario o la forma de invitar. El informe lleva solo cantidades y porcentajes, no los nombres de las familias, porque los datos personales son reservados. También se calculan los materiales: un folleto por familia asistente más los de repuesto.",
        "Los datos de esta clase son inventados, para practicar el trabajo con planillas." + LIM,
    ],
    vocab=[("asistencia", "cantidad de personas o familias que llegaron a una actividad"), ("cobertura", "porcentaje de las invitadas que asistió"), ("meta", "porcentaje que el centro se propone alcanzar"), ("invitadas", "familias a las que se convocó a la actividad"), ("material de repuesto", "cantidad extra de folletos para imprevistos")],
    worked=[
        ("Calcular una cobertura", "En una actividad de ejemplo se invitó a 40 familias y asistieron 28. ¿Cuál es la cobertura?", ["Se multiplica la asistencia por 100: 28 × 100 = 2.800.", "2.800 ÷ 40 = 70."], "70 %"),
        ("Calcular el material", "Otra actividad de ejemplo tiene 30 familias asistentes, con 1 folleto por familia y 8 de repuesto. ¿Cuántos folletos se preparan?", ["Se suman las familias asistentes y el repuesto.", "30 + 8 = 38."], "38 folletos"),
    ],
    mistakes=[("Calcular la cobertura dividiendo los asistentes entre los que no asistieron.", "Cambia la base: la cobertura se mide sobre las invitadas, no sobre quienes faltaron.", "Divide siempre entre el total de invitadas."),
              ("Copiar al informe los nombres de las familias que no fueron.", "Son datos personales que no deben salir de la lista reservada.", "Informa solo cantidades y porcentajes.")],
    T=[
        ("abc", "En Atención de Enfermería: ¿qué es la cobertura de una actividad?", "El porcentaje de las invitadas que asistió", "El número de folletos que sobraron", "La cantidad de horas que duró la actividad", "La cobertura compara la asistencia con las invitadas."),
        ("abc", "{F} ¿Qué meta se propuso el centro?", "Que asista al menos el 70 % de las invitadas en cada actividad", "Que asista el 100 % en la primera actividad", "Que asistan al menos 40 familias siempre", "La ficha define la meta como al menos 70 % de las invitadas en cada actividad."),
        ("=", "{F} ¿Cuál fue la cobertura del mes 1?", "36*100//60", "Se multiplica la asistencia por 100 y se divide entre las invitadas.", " %"),
        ("=", "{F} ¿Cuál fue la cobertura del mes 2?", "40*100//50", "Se multiplica la asistencia por 100 y se divide entre las invitadas.", " %"),
        ("=", "{F} ¿Cuál fue la cobertura del mes 3?", "54*100//90", "Se multiplica la asistencia por 100 y se divide entre las invitadas.", " %"),
        ("abc", "{F} ¿En qué meses se alcanzó la meta?", "Solo en el mes 2", "En los meses 1 y 2", "En los tres meses", "Solo el mes 2 tuvo 80 %, superior al 70 %; los meses 1 y 3 tuvieron 60 %."),
        ("=", "{F} ¿Cuántas familias fueron invitadas en total en el trimestre?", "60+50+90", "Se suman las invitadas de los tres meses.", " familias"),
        ("=", "{F} ¿Cuántas familias asistieron en total en el trimestre?", "36+40+54", "Se suman las asistentes de los tres meses.", " familias"),
        ("=", "{F} ¿Cuál fue la cobertura del trimestre completo?", "(36+40+54)*100//(60+50+90)", "Se divide el total de asistentes entre el total de invitadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos folletos se preparan en el mes 3?", "54+10", "Se suma un folleto por familia asistente y los de repuesto.", " folletos"),
        ("abc", "{F} Para el informe, un compañero quiere agregar los nombres de las familias que no asistieron. ¿Qué corresponde?", "No agregarlos: el informe lleva solo cantidades y porcentajes", "Agregarlos, para saber a quién invitar", "Agregarlos solo en el mes 1", "La regla del centro dice que los nombres están en la lista reservada y no se copian al informe."),
        ("abc", "{F} La enfermera quiere saber por qué en los meses 1 y 3 la cobertura fue menor a la meta. ¿Qué corresponde hacer al técnico?", "Informar lo que se observó, como horarios o forma de invitar, sin culpar a las familias", "Decir que las familias no tienen interés", "Anotar que la enfermera invitó mal", "Se aportan hechos para que la enfermera analice; culpar a las familias o al equipo no ayuda."),
        ("=", "{F} Si en el mes 3 hubieran asistido 63 familias de las 90 invitadas, ¿cuál habría sido la cobertura?", "63*100//90", "Se multiplica la asistencia por 100 y se divide entre las invitadas.", " %"),
    ],
    ctx=("abc", "{F} Al cerrar el mes 3, la técnica nota que contó 54 asistentes pero en la lista reservada firmaron 52. ¿Qué hace?", "Informa la diferencia a la enfermera y deja constancia de ambas cifras", "Anota 54 sin avisar, porque es más probable que sea correcta", "Anota 52 sin avisar, para que coincida con la lista", "Las diferencias se informan con ambas cifras para que la enfermera decida cuál se usa."),
    sc=[
        ("En Atención de Enfermería: ¿cómo se calcula la cobertura?", "Asistencia × 100 ÷ invitadas", "Compara cuántas personas asistieron con las que fueron invitadas."),
        ("¿Qué lleva el informe de la actividad?", "Solo cantidades y porcentajes", "Los nombres de las familias son datos reservados."),
        ("¿Qué haces si hay diferencias entre dos cifras de asistencia?", "Informo ambas a la enfermera", "No se elige una cifra sin consultar."),
    ],
    op=("Registro de ejemplo: «Un centro invitó a 80, 60 y 100 familias en tres actividades de promoción; asistieron 48, 45 y 70 respectivamente. Meta: al menos 70 % por actividad. Material: 1 folleto por familia asistente y 5 de repuesto por actividad». "
        "Calcula: la cobertura de cada actividad; en cuáles se cumplió la meta; y cuántos folletos se preparan en total. Escribe una frase de informe a la enfermera, sin datos personales.",
        "Coberturas: 48×100÷80 = 60 %; 45×100÷60 = 75 %; 70×100÷100 = 70 %. Se cumplió la meta en la 2.ª y la 3.ª. Folletos: (48+5)+(45+5)+(70+5) = 178. Informe: «Cobertura de 60 %, 75 % y 70 %; meta cumplida en dos de tres actividades; se prepararon 178 folletos».",
        ["calcula las tres coberturas", "compara con la meta", "calcula 178 folletos", "la frase no incluye datos personales"],
        ["hoja con tres porcentajes, dos actividades que cumplen y una frase de informe"],
        ["dividir entre los que no asistieron", "olvidar el repuesto", "incluir nombres de familias"],
        "Pregunta: «¿tu informe lleva nombres de familias?». Si sí, pídele quitarlos."),
    reinforce="Con 50 familias invitadas y 35 asistentes, calcula la cobertura y los folletos si se reparten 1 por familia y 6 de repuesto.",
    extend="Explica con un ejemplo inventado por qué una cobertura baja se debe analizar sin culpar a las familias.",
)

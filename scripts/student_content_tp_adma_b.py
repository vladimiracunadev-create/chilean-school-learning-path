"""Atención de Enfermería, mención Adulto Mayor (4.º medio TP): OAM-04 (emergencias y accidentes: solo avisar y prevenir), OAM-05 (productos farmacológicos: solo conceptos y lectura de documentos) y OAM-06 (higiene y confort: conceptos y organización). Todo en papel: residencias, personas y familias inventadas y rotuladas «de ejemplo»; sin técnicas clínicas ni procedimientos."""
from __future__ import annotations

from tp_adma_common import LIM, build

O4 = "TP-ADMA-4-OAM-04"
O5 = "TP-ADMA-4-OAM-05"
O6 = "TP-ADMA-4-OAM-06"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (residencia de ejemplo, inventada). La «Residencia Los Aromos de Ejemplo» tiene 30 residentes. Turno de día: 1 enfermera y 4 técnicos. Turno de noche: 1 enfermera y 2 técnicos. "
     "El plan de emergencia, con las vías de evacuación, la zona de seguridad y la cadena de aviso, está publicado en cada pasillo. Se hacen 2 simulacros al año. "
     "La formación en primeros auxilios la da un instructor acreditado, fuera de este cuaderno. Reglas: no ponerse en riesgo, cuidar al resto del grupo, avisar de inmediato a la enfermera y a emergencias, y registrar lo ocurrido.")
build(
    O4, 1, F,
    use="Aprenderé qué es una emergencia y un accidente, qué rol tiene el técnico, qué significa «primeros auxilios» y por qué su aprendizaje exige un instructor acreditado.",
    prior=["Conozco el trabajo del técnico en enfermería.", "Sé dividir y restar números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería (mención Adulto Mayor), una emergencia es una situación que pone en riesgo inmediato la vida o la salud de una persona, como una caída con un golpe fuerte, un atragantamiento, un desmayo, un incendio o un sismo. Un accidente es un hecho inesperado que causa un daño. En ambos casos, lo primero es cuidar la propia seguridad y la del grupo, y avisar de inmediato a la enfermera o profesional responsable y a emergencias.",
        "Los primeros auxilios son la ayuda inicial que dan personas capacitadas mientras llega un profesional. Cómo se realizan lo enseña un instructor acreditado en un curso con práctica supervisada; este cuaderno no enseña ninguna maniobra ni procedimiento. Lo que sí enseña es el rol del técnico: reconocer que algo es una emergencia, avisar, seguir el plan de emergencia, acompañar y registrar después con hechos y hora.",
        "El plan de emergencia, publicado en cada pasillo, indica las vías de evacuación, la zona de seguridad y quién avisa a quién; sus simulacros permiten que todos sepan qué hacer." + LIM,
    ],
    vocab=[("emergencia", "situación que pone en riesgo inmediato la vida o la salud de una persona"), ("accidente", "hecho inesperado que causa un daño"), ("primeros auxilios", "ayuda inicial dada por personas capacitadas hasta que llega un profesional"), ("plan de emergencia", "documento con las vías de evacuación, la zona de seguridad y la cadena de aviso"), ("simulacro", "ensayo del plan de emergencia"), ("cadena de aviso", "orden en que se avisa a quienes deben actuar")],
    worked=[
        ("Reconocer una emergencia", "En el comedor de ejemplo, a una residente se le cae un vaso con agua al piso y nadie se lastima. ¿Es una emergencia?", ["No hay riesgo inmediato para la vida ni la salud de nadie.", "Se avisa al personal de aseo y se señala el lugar, pero no es una emergencia."], "No es una emergencia; se avisa al personal de aseo y se señala el lugar"),
        ("Residentes por persona", "En otra residencia de ejemplo hay 24 residentes y 3 personas del equipo en el turno de noche. ¿Cuántos residentes hay por cada persona del equipo?", ["Se divide el total de residentes entre las personas del equipo.", "24 ÷ 3 = 8."], "8 residentes por persona")],
    mistakes=[("Pensar que «si sé primeros auxilios» puedo actuar por mi cuenta sin avisar.", "Siempre se avisa de inmediato a la enfermera y a emergencias, aunque se tenga formación.", "Avisa primero y actúa solo dentro de lo que indica el protocolo y tu formación acreditada."),
              ("Ponerse en riesgo para ayudar, por ejemplo entrando a una sala con humo.", "Se agrega una víctima más y se complica el rescate por quien corresponde.", "Cuida tu seguridad, avisa y sigue el plan de emergencia.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es una emergencia?", "Una situación que pone en riesgo inmediato la vida o la salud de una persona", "Cualquier cambio de planes en el día", "Un taller que se atrasa", "Una emergencia exige actuar de inmediato y con ayuda."),
        ("abc", "{F} ¿Dónde está publicado el plan de emergencia?", "En cada pasillo", "Solo en la oficina de la enfermera", "En la cocina", "La ficha dice que el plan está publicado en cada pasillo."),
        ("abc", "{F} ¿Quién enseña los primeros auxilios, según la ficha?", "Un instructor acreditado", "El técnico con más años de experiencia", "El familiar de un residente", "La ficha aclara que la formación la da un instructor acreditado."),
        ("=", "{F} ¿Cuántas personas del equipo hay en total durante el turno de día?", "1+4", "Se suman la enfermera y los técnicos del turno de día.", " personas"),
        ("=", "{F} ¿Cuántas personas del equipo hay en total durante el turno de noche?", "1+2", "Se suman la enfermera y los técnicos del turno de noche.", " personas"),
        ("=", "{F} ¿Cuántos residentes hay por cada persona del equipo en el turno de noche?", "30//(1+2)", "Se divide el total de residentes entre las personas del equipo de noche.", " residentes"),
        ("=", "{F} ¿Cuántos residentes más por persona hay de noche que de día?", "30//(1+2)-30//(1+4)", "Se restan los residentes por persona del turno de día de los del turno de noche.", " residentes"),
        ("abc", "{F} Un residente de ejemplo se atraganta en el comedor. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias, y sigue el plan", "Le golpea la espalda de inmediato por cuenta propia", "Le da agua para que pase", "Ante un atragantamiento se avisa de inmediato; no se actúa por cuenta propia."),
        ("abc", "{F} El técnico siente olor a quemado y ve humo en una sala. ¿Qué hace?", "Se aleja del riesgo, avisa de inmediato a la enfermera y a emergencias y sigue el plan de evacuación", "Entra a buscar el origen del humo", "Espera a ver si el humo aumenta", "Se cuida la seguridad propia y del grupo, y se avisa de inmediato."),
        ("abc", "{F} Un compañero dice: «Como hice un curso hace años, puedo manejar sola esta caída». ¿Qué corresponde responder?", "Que se avisa de inmediato a la enfermera y a emergencias, aunque tenga formación", "Que sí, porque tiene experiencia", "Que sí, si lo anota después", "Siempre se avisa; la formación no reemplaza la cadena de aviso."),
        ("abc", "{F} Durante un simulacro, un técnico dice que no hace falta participar «porque es de mentira». ¿Qué corresponde?", "Participar, porque el simulacro prepara para una emergencia real", "No participar, si ya sabe lo que hay que hacer", "Participar solo si lo evalúan", "El simulacro permite practicar el plan y detectar fallas."),
        ("=", "{F} En 3 años, ¿cuántos simulacros habrá hecho la residencia?", "2*3", "Se multiplican los simulacros anuales por los años.", " simulacros"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué debe registrar el técnico después de una emergencia?", "Hechos con hora: qué ocurrió, a quién avisó y cuándo", "Su opinión sobre quién tuvo la culpa", "Un diagnóstico de lo ocurrido", "El registro describe hechos para que el equipo pueda analizar y mejorar."),
    ],
    ctx=("abc", "{F} A las 03:00, un técnico de ejemplo oye un golpe en una pieza y encuentra a una residente en el suelo, consciente, que dice que le duele la cadera. La enfermera está en otra ala. ¿Qué hace?", "Avisa de inmediato a la enfermera y a emergencias, acompaña con calma sin moverla ni darle nada y registra la hora", "La levanta para llevarla a la cama", "Le da un calmante de la bodega", "Mover o tratar a la persona no le corresponde: se avisa de inmediato y se acompaña."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces ante una emergencia?", "Aviso de inmediato a la enfermera y a emergencias", "No actúo por cuenta propia: pido ayuda a quien corresponde."),
        ("¿Quién enseña los primeros auxilios?", "Un instructor acreditado", "Este cuaderno no enseña maniobras: las enseña un instructor."),
        ("¿Qué haces si hay humo?", "Me alejo, aviso de inmediato a la enfermera y a emergencias y sigo el plan de evacuación", "Cuidar la propia seguridad es el primer paso."),
    ],
    op=("Caso de ejemplo: en una residencia de 36 residentes, el turno de noche tiene 1 enfermera y 3 técnicos. A las 22:15, un técnico encuentra a un residente en el suelo del pasillo, consciente, con una herida en la frente. "
        "Escribe: cuántos residentes hay por cada persona del equipo de noche; qué haría el técnico (solo avisar y acompañar); a quién avisaría; y una frase de registro con hora y hechos, sin opiniones.",
        "Residentes por persona: 36 ÷ (1+3) = 9. El técnico no mueve ni trata al residente: avisa de inmediato a la enfermera y a emergencias y lo acompaña con calma. Registro: «22:15, pasillo del ala norte, residente en el suelo, consciente, con una herida en la frente; se avisó a la enfermera y a emergencias a las 22:16».",
        ["calcula 9 residentes por persona", "avisa de inmediato a la enfermera y a emergencias", "no mueve ni trata al residente", "el registro lleva hora y hechos"],
        ["hoja con un cálculo, una conducta, a quién avisa y una frase de registro"],
        ["mover al residente", "curar la herida", "escribir una opinión en el registro"],
        "Pregunta: «¿tu respuesta dice que el técnico cura la herida?». Si sí, pídele reescribirla: solo avisa y acompaña."),
    reinforce="Escribe tres ejemplos de emergencia y qué avisa el técnico en cada una, sin decir qué hace con la persona.",
    extend="Explica con un ejemplo inventado por qué un técnico no debe ponerse en riesgo al ayudar en una emergencia.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (plan de emergencia y registro de incidente de ejemplo). Elementos del plan: vía de evacuación, zona de seguridad y cadena de aviso. Cadena de aviso de ejemplo: quien ve el hecho avisa de inmediato a la enfermera; la enfermera decide el aviso a emergencias o, ante un riesgo inmediato, cualquier persona del equipo puede avisar a emergencias; se avisa luego a la familia por la vía que defina la enfermera. "
     "Registro de incidente, campos: fecha y hora; lugar; persona involucrada; qué se vio (hechos); a quién se avisó y a qué hora; quién llegó y a qué hora; firma. "
     "Eventos de ejemplo y a quién se avisa primero: caída, a la enfermera y a emergencias; atragantamiento, a la enfermera y a emergencias; humo o fuego, a emergencias, a la enfermera y se evacúa según el plan; corte de luz, a la enfermera y a mantención; sismo, se sigue el plan de evacuación y se avisa a la enfermera.")
build(
    O4, 2, F,
    use="Aprenderé los documentos de una emergencia: el plan, la cadena de aviso y el registro de incidente, y a distinguir qué se avisa primero según el evento.",
    prior=["Conozco qué es una emergencia.", "Sé leer una ficha.", "Sé contar elementos."],
    explain=[
        "El plan de emergencia es un documento que dice cómo salir con seguridad y quién hace qué. Sus tres elementos son la vía de evacuación (el camino libre hacia la salida), la zona de seguridad (el lugar donde se reúne el grupo) y la cadena de aviso (quién avisa a quién). Cada establecimiento lo publica y lo practica con simulacros, y todo el equipo debe conocerlo.",
        "El registro de incidente se completa después de un hecho. Sus campos son fecha y hora, lugar, persona involucrada, hechos observados, a quién se avisó y cuándo, quién llegó y cuándo, y firma. Se escribe sin opiniones ni diagnósticos. Según el evento, se avisa a distintas personas: ante una caída o un atragantamiento, a la enfermera y a emergencias; ante un corte de luz, a la enfermera y a mantención; ante un sismo, se sigue el plan de evacuación.",
        "Los documentos de esta clase son de ejemplo; cada establecimiento tiene los suyos." + LIM,
    ],
    vocab=[("plan de emergencia", "documento que dice cómo salir con seguridad y quién hace qué"), ("vía de evacuación", "camino libre hacia la salida"), ("zona de seguridad", "lugar donde se reúne el grupo después de evacuar"), ("cadena de aviso", "orden en que se avisa a quienes deben actuar"), ("registro de incidente", "documento donde se anota lo ocurrido en un hecho inesperado")],
    worked=[
        ("Identificar un elemento del plan", "En un plan de ejemplo se dice «el grupo se reúne en el patio central». ¿Qué elemento del plan es el patio central?", ["Es el lugar donde se reúne el grupo.", "Es la zona de seguridad."], "La zona de seguridad"),
        ("Contar campos", "El registro de ejemplo tiene 8 campos y un técnico completó 6. ¿Cuántos le faltan?", ["Se restan los completados del total.", "8 − 6 = 2."], "2 campos")],
    mistakes=[("Escribir en el registro «la residente se cayó por distraída».", "Es una opinión sobre la persona y no un hecho observado.", "Anota qué se vio: «se encontró a la residente en el suelo junto a la cama»."),
              ("Dejar el campo «a quién se avisó y a qué hora» en blanco «porque se sabe».", "Sin esos datos no se puede revisar si el aviso fue oportuno.", "Completa todos los campos con hora y firma.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la zona de seguridad?", "El lugar donde se reúne el grupo después de evacuar", "El camino hacia la salida", "El lugar donde se guardan los extintores", "La zona de seguridad es el punto de reunión; el camino es la vía de evacuación."),
        ("abc", "{F} ¿Cuántos elementos tiene el plan de emergencia de la ficha?", "Tres", "Dos", "Cuatro", "La ficha enumera vía de evacuación, zona de seguridad y cadena de aviso."),
        ("abc", "{F} ¿A quién avisa primero quien ve una caída?", "A la enfermera y a emergencias", "A la familia", "A mantención", "La ficha indica avisar a la enfermera y a emergencias ante una caída."),
        ("abc", "{F} ¿A quién se avisa ante un corte de luz?", "A la enfermera y a mantención", "A emergencias solamente", "A la familia de cada residente", "La ficha indica avisar a la enfermera y a mantención."),
        ("abc", "{F} ¿Cuántos campos tiene el registro de incidente de la ficha?", "Siete", "Cinco", "Nueve", "La ficha enumera fecha y hora, lugar, persona, qué se vio, aviso, llegada y firma: siete."),
        ("abc", "{F} ¿Cuántos eventos de ejemplo enumera la ficha?", "Cinco", "Tres", "Siete", "La ficha enumera caída, atragantamiento, humo o fuego, corte de luz y sismo."),
        ("abc", "{F} ¿Qué se anota en el campo «qué se vio»?", "Hechos observados, sin opiniones", "La causa que cree el técnico", "Un diagnóstico de la persona", "El registro describe hechos; las causas y los diagnósticos no le corresponden al técnico."),
        ("abc", "{F} ¿Qué hace el técnico ante un sismo, según la ficha?", "Sigue el plan de evacuación y avisa a la enfermera", "Corre a buscar a emergencias", "Se queda quieto sin hacer nada", "La ficha dice que se sigue el plan de evacuación y se avisa a la enfermera."),
        ("abc", "{F} Un técnico escribe en «qué se vio»: «seguramente se tropezó por apurada». ¿Qué corresponde?", "Reescribirlo con hechos: «se encontró a la residente en el suelo junto a la cama»", "Dejarlo, porque explica lo ocurrido", "Agregar más opiniones", "El registro describe hechos y no atribuye causas."),
        ("abc", "{F} Una compañera propone hacer el registro al final de la semana para hacerlo con calma. ¿Qué corresponde?", "Hacerlo cerca del hecho, para anotar los datos con exactitud", "Esperar al fin de semana, porque hay más tiempo", "No hacerlo, si nadie lo pide", "El registro oportuno evita olvidos y errores."),
        ("abc", "{F} Una nueva técnica pregunta dónde está la zona de seguridad. ¿Qué corresponde?", "Mostrársela en el plan publicado y practicar el recorrido en el simulacro", "Decirle que lo averigüe el día de la emergencia", "Decirle que no hace falta, que la enfermera se lo dirá", "Todo el equipo debe conocer el plan antes de una emergencia."),
        ("=", "{F} Si se hacen los 5 eventos de la ficha en un simulacro y cada uno dura 6 minutos, ¿cuántos minutos dura en total?", "5*6", "Se multiplican los eventos por los minutos de cada uno.", " minutos"),
        ("abc", "{F} Tras un incidente, la enfermera pide quién llegó y a qué hora. ¿Dónde está ese dato?", "En el registro de incidente", "En el plan de emergencia", "En la ficha de intereses", "El registro tiene el campo de quién llegó y cuándo."),
    ],
    ctx=("abc", "{F} Al completar el registro de un incidente, la técnica no recuerda a qué hora avisó a la enfermera. ¿Qué hace?", "Anota que no recuerda la hora exacta y lo consulta con la enfermera, sin inventar", "Anota una hora parecida", "Deja el campo en blanco sin avisar", "No se inventan datos: se informa lo que no se recuerda."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cuáles son los tres elementos del plan de emergencia?", "Vía de evacuación, zona de seguridad y cadena de aviso", "Son los elementos que enumera el plan de ejemplo."),
        ("¿Qué se anota en «qué se vio»?", "Hechos observados, sin opiniones", "Las opiniones no corresponden en un registro."),
        ("¿A quién se avisa ante un corte de luz?", "A la enfermera y a mantención", "No es una emergencia que requiera aviso inmediato a emergencias."),
    ],
    op=("Registro de ejemplo: «Fecha 12 de marzo, 15:40; lugar: comedor; persona: un residente de ejemplo; hechos: se observa al residente con tos fuerte y sin poder hablar mientras come; aviso a la enfermera 15:41; aviso a emergencias 15:41; llegada de la enfermera 15:43». "
        "Escribe: cuántos minutos pasaron entre el hecho y la llegada de la enfermera; qué campo falta en el registro de la ficha (de los 7); y una frase de «qué se vio» bien escrita. ¿Qué hizo el técnico además de avisar?",
        "Minutos: 15:43 − 15:40 = 3. Faltan: firma. Frase: «Se observa al residente con tos fuerte y sin poder hablar mientras come». Además de avisar, acompañó sin darle nada ni actuar por su cuenta.",
        ["calcula 3 minutos", "identifica la firma como faltante", "la frase es un hecho", "no describe maniobras"],
        ["hoja con un cálculo, un campo faltante y una frase"],
        ["agregar una causa o un diagnóstico", "olvidar la firma", "describir una maniobra"],
        "Pregunta: «¿tu frase dice qué se vio o por qué ocurrió?». Debe decir qué se vio."),
    reinforce="Escribe los campos de un registro de incidente y una frase de «qué se vio» sobre una caída de ejemplo.",
    extend="Explica con un ejemplo inventado por qué el registro oportuno de un incidente ayuda a mejorar la seguridad.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (casos y pauta de conducta ante emergencias, de ejemplo). Pauta de cinco criterios: (1) mantener la calma y cuidar la propia seguridad; (2) avisar de inmediato a la enfermera y a emergencias; (3) no mover ni dar alimentos ni medicamentos a la persona; (4) cuidar al resto del grupo; (5) registrar con hechos y hora. "
     "Caso A: un técnico encuentra a una residente en el suelo; avisa de inmediato a la enfermera y a emergencias, la acompaña sin moverla ni darle nada, y registra; cumple los cinco. "
     "Caso B: una técnica ve humo en la cocina; entra a buscar el origen, sin avisar primero; cumple los criterios 3, 4 y 5. "
     "Caso C: un residente se atraganta; el técnico avisa de inmediato a la enfermera y a emergencias, le da agua para ayudar y registra; cumple los criterios 1, 2, 4 y 5. "
     "Caso D: durante un sismo, un técnico guía al grupo por la vía de evacuación hasta la zona de seguridad, avisa a la enfermera y anota la hora; cumple los cinco.")
build(
    O4, 3, F,
    use="Aprenderé a analizar casos de emergencia con una pauta, a reconocer qué conducta falló y a decidir qué corrección proponer sin enseñar maniobras.",
    prior=["Conozco el plan de emergencia y el registro de incidente.", "Sé calcular porcentajes de números enteros.", "Conozco la regla de avisar de inmediato."],
    explain=[
        "Analizar un caso de emergencia es compararlo con una pauta de conducta. Los criterios son mantener la calma y cuidar la propia seguridad, avisar de inmediato a la enfermera y a emergencias, no mover ni dar alimentos ni medicamentos a la persona, cuidar al resto del grupo y registrar con hechos y hora. Cada criterio previene un error frecuente.",
        "El error más frecuente es actuar por cuenta propia con buena intención: mover a una persona, darle agua o un remedio, o ponerse en riesgo. Esas acciones pueden agravar el daño. La buena intención no reemplaza el aviso inmediato ni la formación acreditada. Después del hecho, el equipo revisa el caso sin buscar culpables para mejorar el plan.",
        "Esta clase es conceptual: no enseña qué maniobra hacer, sino qué conducta de aviso y de cuidado corresponde." + LIM,
    ],
    vocab=[("pauta de conducta", "lista de acciones esperadas ante un hecho"), ("actuar por cuenta propia", "tomar decisiones o hacer acciones sin avisar ni seguir el protocolo"), ("cuidar al grupo", "proteger al resto de las personas durante una emergencia"), ("análisis del caso", "revisión posterior del hecho para mejorar"), ("buena intención", "deseo de ayudar que no reemplaza el protocolo")],
    worked=[
        ("Aplicar un criterio", "Un técnico de ejemplo da una pastilla a un residente que se siente mal «para que mejore». ¿Qué criterio incumple?", ["Dar medicamentos por cuenta propia incumple el criterio 3.", "Debió avisar de inmediato a la enfermera y a emergencias."], "El criterio 3"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 3 de los 5 criterios. ¿Qué porcentaje es?", ["3 × 100 = 300.", "300 ÷ 5 = 60."], "60 %")],
    mistakes=[("Pensar que dar agua «no hace mal» a una persona que se atraganta.", "Puede empeorar la situación; no corresponde al técnico decidirlo.", "Avisa de inmediato a la enfermera y a emergencias, y no le des nada."),
              ("Quedarse junto a la persona sin avisar «porque no quiero dejarla sola».", "El aviso es lo que permite que llegue ayuda; se puede pedir a otra persona que acompañe.", "Avisa de inmediato y pide ayuda para acompañar.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿por qué la buena intención no reemplaza el aviso inmediato?", "Porque una acción por cuenta propia puede agravar el daño", "Porque el aviso siempre llega demasiado tarde", "Porque la buena intención es una falta", "Actuar sin protocolo puede empeorar la situación."),
        ("abc", "{F} ¿Qué criterio incumple la técnica del caso B?", "El criterio 2: avisar de inmediato a la enfermera y a emergencias", "El criterio 5: registrar", "El criterio 4: cuidar al grupo", "Entró a buscar el origen sin avisar primero."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso C?", "El criterio 3: no dar alimentos ni medicamentos", "El criterio 2: avisar de inmediato", "El criterio 5: registrar", "Dar agua a quien se atraganta es dar algo por cuenta propia."),
        ("abc", "{F} ¿Qué casos cumplen todos los criterios de la pauta?", "Los casos A y D", "Los casos B y C", "Solo el caso A", "La ficha indica que A y D cumplen los cinco criterios."),
        ("=", "{F} ¿Cuántos criterios cumplen en total los cuatro casos?", "5+3+4+5", "Se suman los criterios cumplidos por cada caso.", " criterios"),
        ("=", "{F} ¿Qué porcentaje de los criterios cumplen en total los cuatro casos (cada uno con 5 criterios)?", "(5+3+4+5)*100//(4*5)", "Se multiplica el total cumplido por 100 y se divide entre los criterios evaluados.", " %"),
        ("=", "{F} ¿Cuántos criterios incumplen en total los casos B y C?", "(5-3)+(5-4)", "Se restan los criterios cumplidos de los 5 de cada caso y se suman las fallas.", " criterios"),
        ("abc", "{F} En el caso B, ¿qué debió hacer la técnica al ver humo?", "Alejarse del riesgo, avisar de inmediato a emergencias y a la enfermera y seguir el plan", "Entrar a buscar el origen", "Cerrar la puerta y seguir con su tarea", "Se cuida la propia seguridad y se avisa de inmediato."),
        ("abc", "{F} En el caso A, ¿por qué el técnico no movió a la residente?", "Porque mover a una persona caída puede agravar una lesión que él no puede evaluar", "Porque no tenía fuerza para hacerlo", "Porque era la regla de la residencia, sin razón", "Solo un profesional evalúa si es seguro mover a la persona."),
        ("abc", "{F} Un compañero dice que en el caso D se debió usar el ascensor para ir más rápido. ¿Qué corresponde?", "Seguir la vía de evacuación del plan, sin usar medios no indicados", "Usar el ascensor, porque es más rápido", "Dejar a los más lentos para después", "El plan de evacuación define el recorrido seguro; durante un sismo no se usa un medio no indicado."),
        ("abc", "{F} Al analizar el caso C, la enfermera quiere culpar al técnico. ¿Qué corresponde?", "Analizar qué falló y reforzar la capacitación y el plan, sin buscar culpables", "Sancionar de inmediato", "Ocultar el caso", "El análisis busca mejorar; culpar no ayuda a prevenir."),
        ("=", "{F} Si el técnico del caso C hubiera cumplido también el criterio 3, ¿cuántos criterios habría cumplido?", "4+1", "Se suma el criterio 3 a los cuatro que ya cumplía.", " criterios"),
        ("abc", "{F} Una técnica ve a una residente desmayarse en el pasillo. ¿Qué corresponde?", "Avisar de inmediato a la enfermera y a emergencias, y acompañar sin moverla ni darle nada", "Levantarla y llevarla a su cama", "Darle un caramelo para que reaccione", "Ante un desmayo se avisa de inmediato y no se actúa por cuenta propia."),
    ],
    ctx=("abc", "{F} Durante un corte de luz de noche, un residente con baja visión se levanta y camina por el pasillo oscuro. El técnico lo ve desde lejos. ¿Qué hace?", "Se acerca con una linterna de la residencia, lo acompaña con calma y avisa a la enfermera", "Lo deja caminar solo, porque es autónomo", "Le grita que vuelva rápido", "Se evita el riesgo de caída acompañando con calma y se informa a la enfermera."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿puedo dar agua a quien se atraganta?", "No, aviso de inmediato a la enfermera y a emergencias", "No se da nada por cuenta propia."),
        ("¿Qué haces con una persona caída?", "Aviso de inmediato a la enfermera y a emergencias y la acompaño sin moverla", "Moverla puede agravar una lesión que no sé evaluar."),
        ("¿Cuántos criterios tiene la pauta de la ficha?", "5", "Calma, aviso, no dar ni mover, cuidar al grupo y registrar."),
    ],
    op=("Casos de ejemplo: «A: un residente se marea en el patio; el técnico avisa de inmediato a la enfermera y a emergencias, lo acompaña y registra. B: una residente se cae en el baño; el técnico la levanta de inmediato y la lleva a su cama, y luego avisa a la enfermera y anota lo ocurrido. C: sale humo del tablero eléctrico; el técnico avisa de inmediato a emergencias y a la enfermera, guía al grupo a la zona de seguridad y anota la hora». "
        "Usa la pauta de la ficha. Escribe: qué criterios incumple cada caso; cuántos criterios se cumplen si A cumple 5, B cumple 3 y C cumple 5; y cómo corregirías B.",
        "A cumple todos. B incumple los criterios 2 y 3 (no avisó de inmediato y movió a la persona); cumple 1, 4 y 5. C cumple todos. Total: 5+3+5 = 13 de 15. Corrección de B: avisar de inmediato a la enfermera y a emergencias y acompañar a la residente sin moverla.",
        ["identifica criterios incumplidos en B", "calcula 13 de 15", "propone avisar sin mover", "no enseña maniobras"],
        ["hoja con criterios, un total y una corrección"],
        ["justificar que se mueva a la persona", "sumar mal", "describir una maniobra"],
        "Pregunta: «¿qué debe hacer el técnico en B antes de cualquier otra cosa?». Debe responder avisar de inmediato."),
    reinforce="Escribe las cinco conductas de la pauta con tus palabras y un ejemplo de una conducta que las incumpla.",
    extend="Explica con un ejemplo inventado por qué mover a una persona caída puede ser peligroso.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (registro de incidentes del mes, de ejemplo). Evento 1: hora del hecho 10:00, aviso a las 10:01, llegada de la enfermera a las 10:04. Evento 2: hecho 14:30, aviso 14:34, llegada 14:37. Evento 3: hecho 21:10, aviso 21:11, llegada 21:14. "
     "Evento 4: hecho 03:20, aviso 03:22, llegada 03:27. Evento 5: hecho 16:05, aviso 16:06, llegada 16:12. "
     "Metas del servicio (de ejemplo): aviso dentro de 2 minutos desde el hecho; llegada de la enfermera dentro de 5 minutos desde el aviso. Tipos: caída 2 eventos, atragantamiento 1, desmayo 1, corte de luz 1.")
build(
    O4, 4, F,
    use="Aprenderé a calcular tiempos de aviso y de llegada en un registro de incidentes, a comparar con metas y a informar los resultados para mejorar el plan.",
    prior=["Sé restar horas y minutos.", "Sé calcular porcentajes de números enteros.", "Conozco el registro de incidente."],
    explain=[
        "Un registro de incidentes permite calcular tiempos. El tiempo de aviso es la diferencia entre la hora del hecho y la hora en que se avisó. El tiempo de llegada es la diferencia entre la hora del aviso y la hora en que llegó la enfermera. Con ellos se ve si se cumplen las metas del servicio, que son tiempos máximos de ejemplo. Un resultado fuera de la meta no es un reproche: es una señal para revisar el plan o la cadena de aviso.",
        "También se cuentan los eventos por tipo y se calcula el porcentaje que cumple cada meta, dividiendo los eventos que cumplen entre el total y multiplicando por 100. Estas cuentas se informan a la enfermera con datos exactos y sin identificar a las personas. Si un valor parece raro, por ejemplo una hora imposible, se verifica con quien registró.",
        "Los tiempos de esta clase son inventados y las metas son de ejemplo; las reales las fija el establecimiento." + LIM,
    ],
    vocab=[("tiempo de aviso", "minutos entre el hecho y el aviso a la enfermera"), ("tiempo de llegada", "minutos entre el aviso y la llegada de la enfermera"), ("meta", "tiempo máximo que el servicio se propone cumplir"), ("porcentaje de cumplimiento", "eventos que cumplen la meta por 100 divididos por el total de eventos"), ("señal de mejora", "dato que indica qué revisar del plan")],
    worked=[
        ("Calcular un tiempo de aviso", "Un evento de ejemplo ocurrió a las 09:15 y se avisó a las 09:18. ¿Cuántos minutos pasaron hasta el aviso?", ["Se restan las horas: 09:18 − 09:15.", "Pasaron 3 minutos."], "3 minutos"),
        ("Calcular un porcentaje", "En otro mes de ejemplo, 3 de 4 eventos cumplieron la meta de aviso. ¿Qué porcentaje es?", ["3 × 100 = 300.", "300 ÷ 4 = 75."], "75 %")],
    mistakes=[("Contar el tiempo de llegada desde la hora del hecho.", "La meta de llegada se mide desde el aviso, no desde el hecho.", "Resta la hora del aviso a la hora de llegada."),
              ("Informar un evento con la hora de aviso anterior a la del hecho.", "Es imposible; hay un error de registro que se debe revisar.", "Verifica con quien registró y corrige con trazabilidad.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es el tiempo de aviso?", "Los minutos entre el hecho y el aviso a la enfermera", "Los minutos entre el aviso y la llegada", "La duración de la emergencia", "El tiempo de aviso se mide desde el hecho hasta el aviso."),
        ("=", "{F} ¿Cuántos minutos pasaron del hecho al aviso en el evento 2?", "34-30", "Se restan los minutos de la hora del hecho de los de la hora del aviso.", " minutos"),
        ("=", "{F} ¿Cuántos minutos pasaron del aviso a la llegada en el evento 5?", "12-6", "Se restan los minutos del aviso de los minutos de la llegada.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suman los tiempos de aviso de los cinco eventos?", "1+4+1+2+1", "Se suman los tiempos de aviso de cada evento: 1, 4, 1, 2 y 1 minutos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suman los tiempos de llegada de los cinco eventos?", "3+3+3+5+6", "Se suman los tiempos de llegada de cada evento: 3, 3, 3, 5 y 6 minutos.", " minutos"),
        ("=", "{F} ¿Cuál fue el promedio del tiempo de llegada?", "(3+3+3+5+6)//5", "Se divide la suma de los tiempos de llegada entre los cinco eventos.", " minutos"),
        ("=", "{F} ¿Cuántos eventos cumplieron la meta de aviso (dentro de 2 minutos)?", "5-1", "Solo el evento 2 tardó 4 minutos; se restan de los 5 eventos.", " eventos"),
        ("=", "{F} ¿Qué porcentaje de los eventos cumplió la meta de aviso?", "(5-1)*100//5", "Se multiplican por 100 los eventos que cumplen y se dividen entre el total.", " %"),
        ("=", "{F} ¿Qué porcentaje de los eventos cumplió la meta de llegada (dentro de 5 minutos)?", "(5-1)*100//5", "Solo el evento 5 tardó 6 minutos; se calcula el porcentaje de los que cumplen.", " %"),
        ("abc", "{F} ¿Qué evento no cumplió la meta de aviso?", "El evento 2", "El evento 4", "El evento 5", "El evento 2 tuvo 4 minutos hasta el aviso; el 4 tuvo 2 minutos, que cumple la meta."),
        ("abc", "{F} El evento 5 tardó 6 minutos en llegar la enfermera. ¿Qué corresponde en el análisis?", "Revisar el plan o la cadena de aviso, sin culpar a nadie", "Sancionar a la enfermera", "Ocultar el dato", "Un tiempo fuera de la meta es una señal para mejorar el plan."),
        ("abc", "{F} Un compañero dice: «Con 80 % de cumplimiento ya está todo bien». ¿Qué corresponde responder?", "Que se analizan los eventos fuera de la meta para mejorar, aunque el porcentaje sea alto", "Que sí, porque 80 % es mucho", "Que solo importa el 100 %, y si no, es un fracaso", "Cada evento fuera de la meta es información útil."),
        ("abc", "{F} Al revisar, un técnico ve que el evento 4 aparece con «aviso 03:12», una hora anterior al hecho (03:20). ¿Qué corresponde?", "Verificar con quien registró y con la enfermera, sin cambiar el dato por suposición", "Corregirlo con corrector", "Usar el dato que prefiera", "Un dato dudoso se verifica y se corrige con trazabilidad."),
    ],
    ctx=("abc", "{F} Al preparar el informe del mes, la técnica ve que el evento 2 tuvo un tiempo de aviso de 4 minutos porque la persona que vio el hecho no sabía a quién avisar. ¿Qué hace?", "Informa el hecho con datos a la enfermera y propone repasar la cadena de aviso con todo el equipo", "Anota el nombre de la persona para reprenderla", "Cambia el tiempo a 2 minutos", "Un dato fuera de la meta es una oportunidad de mejora, no un motivo de culpa."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿desde cuándo se mide el tiempo de llegada?", "Desde el aviso", "El tiempo de llegada empieza cuando se avisó."),
        ("¿Qué haces si un tiempo está fuera de la meta?", "Lo informo para revisar el plan, sin culpar", "El dato sirve para mejorar el plan."),
        ("¿Qué porcentaje es 4 de 5 eventos?", "80 %", "4 × 100 ÷ 5 = 80."),
    ],
    op=("Registro de ejemplo: «Evento 1: hecho 08:00, aviso 08:02, llegada 08:05. Evento 2: hecho 12:10, aviso 12:15, llegada 12:19. Evento 3: hecho 19:40, aviso 19:41, llegada 19:45. Evento 4: hecho 23:20, aviso 23:22, llegada 23:30. Metas: aviso dentro de 3 minutos desde el hecho; llegada dentro de 5 minutos desde el aviso». "
        "Calcula: el tiempo de aviso y de llegada de cada evento; cuántos cumplen cada meta y qué porcentaje es; y escribe una frase de informe a la enfermera sin nombres.",
        "Avisos: 2, 5, 1 y 2 minutos; cumplen 3 de 4 = 75 %. Llegadas: 3, 4, 4 y 8 minutos; cumplen 3 de 4 = 75 %. Frase: «De 4 eventos, 3 cumplieron la meta de aviso y 3 la de llegada; se propone revisar los eventos 2 y 4».",
        ["calcula los ocho tiempos", "calcula 75 % en ambas metas", "la frase informa sin nombres", "propone revisar el plan"],
        ["hoja con ocho tiempos, dos porcentajes y una frase de informe"],
        ["medir la llegada desde el hecho", "nombrar personas", "no calcular el porcentaje"],
        "Pregunta: «¿tu frase de informe señala personas o eventos?». Debe señalar eventos."),
    reinforce="Con un hecho a las 11:00, aviso a las 11:03 y llegada a las 11:07, calcula el tiempo de aviso y el de llegada.",
    extend="Explica con un ejemplo inventado por qué un tiempo largo de aviso puede deberse al plan y no a la persona.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (residencia de ejemplo, inventada). En la «Residencia Los Aromos de Ejemplo» viven 30 personas y 18 reciben al menos un medicamento. Los medicamentos los indica el médico en una receta; solo personal autorizado y capacitado, bajo la supervisión de la enfermera y según la norma vigente, los administra. "
     "Se guardan en un lugar con llave y cada entrega se anota en la hoja de medicamentos, con hora y firma. En promedio, cada residente que recibe medicamentos tiene 2 horarios de entrega al día y cada entrega demora 3 minutos de trabajo del personal autorizado. "
     "Regla del servicio: ante un error, una reacción adversa o el rechazo de un medicamento, se avisa de inmediato a la enfermera.")
build(
    O5, 1, F,
    use="Aprenderé quién indica y quién administra los medicamentos, qué significa verificar una indicación y qué debe avisar siempre un técnico en formación.",
    prior=["Conozco los derechos de las personas mayores.", "Sé multiplicar números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería (mención Adulto Mayor), un medicamento es un producto que se usa para tratar, prevenir o aliviar un problema de salud. Solo el médico lo indica, mediante una receta o indicación médica. Solo lo administra el personal autorizado y capacitado, bajo la supervisión de la enfermera y según la norma vigente. Este cuaderno no enseña a administrar ningún medicamento ni lo habilita para hacerlo: es solo aprendizaje conceptual.",
        "Los medicamentos se guardan bajo llave y cada entrega se anota en la hoja de medicamentos con hora y firma. Antes de cada entrega, el personal autorizado verifica cinco puntos: persona correcta, medicamento correcto, cantidad indicada, vía correcta y hora correcta. Los riesgos son los errores de medicación, las reacciones adversas, que son efectos dañinos no esperados, y el rechazo de la persona. En todos esos casos se avisa de inmediato a la enfermera.",
        "La persona mayor tiene derecho a ser informada y a rechazar un medicamento; el rechazo se registra y se informa, sin presionarla ni ocultarle nada." + LIM,
    ],
    vocab=[("medicamento", "producto que se usa para tratar, prevenir o aliviar un problema de salud"), ("receta o indicación médica", "documento donde el médico indica un medicamento"), ("hoja de medicamentos", "documento donde se anota cada entrega con hora y firma"), ("vía de administración", "camino por el que se da un medicamento, como oral o sobre la piel"), ("error de medicación", "equivocación en persona, medicamento, cantidad, vía u hora"), ("reacción adversa", "efecto dañino no esperado después de recibir un medicamento")],
    worked=[
        ("Quién indica", "Una técnica de ejemplo cree que un residente necesita un medicamento para el dolor y se lo comenta a otro compañero. ¿Quién puede indicarlo?", ["Solo el médico indica los medicamentos.", "La técnica avisa a la enfermera de lo que observó, y ella consulta al profesional."], "Solo el médico; la técnica avisa a la enfermera"),
        ("Entregas del día", "En otra residencia de ejemplo, 10 residentes tienen 3 horarios de entrega al día. ¿Cuántas entregas se hacen en el día?", ["Se multiplican los residentes por los horarios.", "10 × 3 = 30."], "30 entregas")],
    mistakes=[("Entregar un medicamento a otro residente «porque son parecidos de nombre».", "Es un error de persona que puede dañar a quien lo recibe.", "No lo hagas: verifica y avisa a la enfermera de la confusión."),
              ("Dejar un medicamento sobre la mesa de un residente «para que se lo tome después».", "Otra persona puede tomarlo o no se sabrá si se tomó.", "Los medicamentos los entrega personal autorizado y se anota la entrega.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿quién indica un medicamento?", "El médico, mediante una receta o indicación", "El técnico en enfermería", "El familiar del residente", "Solo el médico indica medicamentos, y lo hace mediante una receta."),
        ("abc", "{F} ¿Dónde se guardan los medicamentos de la residencia?", "En un lugar con llave", "En la mesa de cada residente", "En un cajón de la sala común", "La ficha dice que se guardan bajo llave."),
        ("abc", "{F} ¿Quién administra los medicamentos?", "El personal autorizado y capacitado, bajo la supervisión de la enfermera", "Cualquier técnico, si el residente se lo pide", "Los familiares durante la visita", "La ficha limita la administración al personal autorizado y supervisado."),
        ("=", "{F} ¿Cuántas entregas de medicamentos se hacen en el día a los 18 residentes?", "18*2", "Se multiplican los residentes por los horarios de entrega.", " entregas"),
        ("=", "{F} ¿Cuántos minutos de trabajo demandan las entregas del día?", "18*2*3", "Se multiplican las entregas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos residentes no reciben ningún medicamento?", "30-18", "Se restan los que reciben medicamentos del total de residentes.", " residentes"),
        ("abc", "{F} Un residente dice al técnico que sintió picazón en la piel después de tomar su medicamento de la mañana. ¿Qué hace?", "Avisa de inmediato a la enfermera y a emergencias, y no le da nada", "Le da algo para la picazón de la bodega", "Le dice que es normal", "Una posible reacción adversa se avisa de inmediato; el técnico no trata por su cuenta."),
        ("abc", "{F} Un residente rechaza su medicamento de la tarde. ¿Qué corresponde?", "Respetar su decisión, no presionarlo, registrar el rechazo y avisar a la enfermera", "Disolverlo en la comida sin que se entere", "Dejarlo en la mesa para que lo tome después", "El rechazo se informa y se registra; nunca se engaña ni se presiona."),
        ("abc", "{F} Un compañero sugiere guardar los medicamentos de un residente en su bolsillo «para entregarlos más rápido». ¿Qué corresponde?", "No hacerlo: los medicamentos se guardan bajo llave y se registran", "Hacerlo, si lo anota después", "Hacerlo, si es solo por unos minutos", "La custodia bajo llave evita extravíos y errores."),
        ("abc", "{F} Un familiar le entrega un frasco de un medicamento al técnico para que se lo dé a su madre. ¿Qué corresponde?", "No recibirlo y derivar al familiar a la enfermera", "Guardarlo en el bolsillo", "Dárselo a la residente de inmediato", "Los medicamentos externos los revisa la enfermera según la indicación."),
        ("=", "{F} Si 4 residentes más empiezan un tratamiento con 2 entregas diarias, ¿cuántas entregas más se hacen en el día?", "4*2", "Se multiplican los residentes nuevos por los horarios de entrega.", " entregas"),
        ("abc", "{F} Un técnico en formación ve que la enfermera prepara una entrega y le pide que mire cómo se hace «para aprender». ¿Qué corresponde?", "Observar con respeto sin intervenir y preguntar después lo que no entiende", "Tomar el medicamento para ayudar a entregarlo", "Entregarlo él mismo cuando la enfermera se distraiga", "Un técnico en formación aprende observando; la entrega la hace el personal autorizado."),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿por qué se anota cada entrega con hora y firma?", "Para saber quién entregó qué y cuándo, y evitar errores", "Para que el médico cobre más", "Para decidir qué técnico trabajó más", "El registro da trazabilidad y evita entregas duplicadas u omitidas."),
    ],
    ctx=("abc", "{F} Un técnico en formación nota que el residente de la cama 3 tiene en su velador un comprimido que no se tomó. No sabe de quién es ni cuándo lo dejaron. ¿Qué hace?", "No lo toca ni se lo da a nadie, y avisa de inmediato a la enfermera", "Se lo da al residente para completar su dosis", "Lo guarda en su bolsillo", "Un medicamento sin origen conocido se informa; no se entrega ni se descarta por cuenta propia."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿quién puede administrar un medicamento?", "El personal autorizado, bajo supervisión de la enfermera", "Este cuaderno no habilita para administrarlos."),
        ("¿Qué haces si un residente rechaza un medicamento?", "Respeto su decisión y aviso a la enfermera", "El rechazo se registra y se informa."),
        ("¿Qué haces ante una posible reacción adversa?", "Aviso de inmediato a la enfermera y a emergencias", "No trato ni decido por mi cuenta."),
    ],
    op=("Caso de ejemplo: en una residencia de 20 personas, 12 reciben medicamentos y tienen 3 horarios de entrega al día, de 2 minutos de trabajo cada uno. A las 14:00, una residente dice que se siente extraña después de su comprimido y se rasca los brazos. "
        "Escribe: cuántas entregas se hacen al día y cuántos minutos suman; qué haría el técnico en formación (solo avisar y acompañar); a quién avisaría; y una frase de registro con hora y hechos, sin diagnóstico.",
        "Entregas: 12 × 3 = 36; minutos: 36 × 2 = 72. El técnico no trata ni da nada: avisa de inmediato a la enfermera y a emergencias y acompaña a la residente con calma. Registro: «14:00, la residente refiere sentirse extraña después de su comprimido y se rasca los brazos; se avisó a la enfermera a las 14:01».",
        ["calcula 36 entregas y 72 minutos", "avisa de inmediato", "no trata ni da medicamentos", "el registro no incluye diagnóstico"],
        ["hoja con dos cálculos, una conducta, a quién avisa y una frase de registro"],
        ["dar algo para la picazón", "escribir un diagnóstico", "esperar para avisar"],
        "Pregunta: «¿tu frase de registro dice qué observaste o qué piensas que tiene la residente?». Si lo segundo, pídele reescribirla."),
    reinforce="Escribe quién indica, quién administra y quién supervisa un medicamento, y qué avisa un técnico en formación.",
    extend="Explica con un ejemplo inventado por qué una persona mayor tiene derecho a rechazar un medicamento y a ser informada.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (hoja de medicamentos de ejemplo, con productos inventados; no contiene cantidades ni dosis). Residente R1: Fármaco Alfa, comprimido, vía oral, cada 12 horas, a las 08:00 y a las 20:00; Crema Gamma, vía sobre la piel, una vez al día, a las 21:00. "
     "Residente R2: Fármaco Beta, gotas, vía oral, cada 8 horas, a las 06:00, 14:00 y 22:00. Residente R3: Fármaco Delta, inyectable, vía intramuscular, una vez al día, a las 10:00; solo lo administra personal autorizado. "
     "Vocabulario: nombre genérico es el de la sustancia; nombre comercial es el de la marca. Cada medicamento tiene fecha de vencimiento y lote impresos.")
build(
    O5, 2, F,
    use="Aprenderé a leer una hoja de medicamentos: nombre, presentación, vía, frecuencia y horario, vencimiento y lote, sin interpretar ni decidir.",
    prior=["Sé quién indica y quién administra medicamentos.", "Sé sumar y restar horas.", "Sé leer una tabla."],
    explain=[
        "La hoja de medicamentos dice, para cada residente, qué medicamento se indicó, en qué presentación, por qué vía, con qué frecuencia y a qué hora. La presentación es la forma del producto: comprimido, gotas, crema o inyectable. La vía es el camino por el que se da: oral (por la boca), sobre la piel (tópica) o intramuscular (con una inyección en un músculo). La frecuencia es cada cuánto se da: «cada 12 horas» son 2 veces al día; «cada 8 horas», 3 veces; y «una vez al día», una.",
        "Cada medicamento tiene un nombre genérico, que es el de la sustancia, y puede tener un nombre comercial, que es el de la marca. También lleva impresas la fecha de vencimiento y el lote. Un medicamento vencido no se usa y se avisa a la enfermera. El técnico no cambia la hora, la vía ni la frecuencia: lee, anota y avisa si algo no coincide.",
        "Esta clase es solo de lectura: no incluye cantidades ni dosis, y no enseña a preparar ni a administrar." + LIM,
    ],
    vocab=[("presentación", "forma del producto: comprimido, gotas, crema o inyectable"), ("vía oral", "por la boca"), ("vía intramuscular", "con una inyección en un músculo, hecha solo por personal autorizado"), ("frecuencia", "cada cuánto tiempo se entrega"), ("nombre genérico", "nombre de la sustancia del medicamento"), ("lote", "número impreso que identifica la producción de un medicamento")],
    worked=[
        ("Leer una frecuencia", "Una indicación de ejemplo dice «cada 6 horas». ¿Cuántas veces al día es?", ["Un día tiene 24 horas.", "24 ÷ 6 = 4 veces al día."], "4 veces al día"),
        ("Leer una hora", "Una hoja de ejemplo dice «cada 12 horas, a las 09:00». ¿A qué hora es la segunda entrega?", ["Se suman 12 horas a las 09:00.", "09:00 + 12 horas = 21:00."], "A las 21:00")],
    mistakes=[("Confundir «cada 12 horas» con «12 veces al día».", "Cada 12 horas son 2 veces al día: la frecuencia es el intervalo, no el número de veces.", "Divide 24 horas entre el intervalo para saber las veces al día."),
              ("Cambiar la hora de una entrega «porque el residente está durmiendo».", "La hora la define la indicación; cambiarla es una decisión del profesional.", "Avisa a la enfermera y ella decide.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la vía de administración?", "El camino por el que se da un medicamento, como la boca o la piel", "La hora en que se da un medicamento", "El nombre de la marca del medicamento", "La vía es el camino de administración; la hora y la marca son otros datos."),
        ("abc", "{F} ¿Cuál es la presentación del Fármaco Beta?", "Gotas", "Comprimido", "Crema", "La ficha indica que el Fármaco Beta es en gotas."),
        ("abc", "{F} ¿Por qué vía se da la Crema Gamma?", "Sobre la piel", "Oral", "Intramuscular", "La ficha dice que la Crema Gamma es sobre la piel."),
        ("=", "{F} ¿Cuántas veces al día se entrega el Fármaco Beta?", "24//8", "Se divide el día de 24 horas entre el intervalo de 8 horas.", " veces"),
        ("=", "{F} ¿Cuántas veces al día se entrega el Fármaco Alfa?", "24//12", "Se divide el día de 24 horas entre el intervalo de 12 horas.", " veces"),
        ("=", "{F} ¿Cuántas entregas por día hay en total entre todas las indicaciones de la hoja?", "2+1+3+1", "Se suman las entregas diarias: Alfa 2, Gamma 1, Beta 3 y Delta 1.", " entregas"),
        ("abc", "{F} ¿A qué hora se hace la segunda entrega del Fármaco Beta?", "A las 14:00", "A las 06:00", "A las 22:00", "La ficha indica las entregas a las 06:00, 14:00 y 22:00; la segunda es a las 14:00."),
        ("=", "{F} ¿Cuántas horas hay entre la primera y la segunda entrega del Fármaco Beta?", "14-6", "Se restan las horas de las dos entregas.", " horas"),
        ("abc", "{F} ¿Quién administra el Fármaco Delta?", "Solo personal autorizado", "Cualquier técnico", "El familiar del residente", "La ficha aclara que lo administra solo personal autorizado."),
        ("abc", "{F} El técnico ve que el frasco del Fármaco Alfa que se va a entregar tiene la fecha de vencimiento de hace un mes. ¿Qué hace?", "No lo entrega y avisa a la enfermera", "Lo entrega, si se ve en buen estado", "Lo entrega en una cantidad menor", "Un medicamento vencido no se usa y se informa."),
        ("abc", "{F} Un compañero dice: «El Fármaco Beta se puede dar a las 15:00 en vez de las 14:00, es solo una hora». ¿Qué corresponde responder?", "Que la hora la define la indicación y cualquier cambio lo decide el profesional", "Que sí, porque es una diferencia pequeña", "Que sí, si el residente prefiere", "No se cambia la hora por cuenta propia; se consulta a la enfermera."),
        ("abc", "{F} Una técnica escribe en la hoja de R2 «gotas, 14:00, listo» sin firma ni la hora real. ¿Qué falla tiene el registro?", "Falta la firma y la hora real de la entrega", "Falta el nombre comercial", "Falta el número de lote de otro medicamento", "Cada entrega se anota con hora real y firma."),
        ("=", "{F} ¿Cuántas horas hay entre la última entrega del Fármaco Beta de un día y la primera del día siguiente?", "24-22+6", "Se calculan las horas que faltan para medianoche y se suman las de la primera entrega del día siguiente.", " horas"),
    ],
    ctx=("abc", "{F} Al preparar la hoja del día, la técnica en formación ve que el nombre «Fármaco Alfa» está escrito con otra letra en la etiqueta del frasco: «Fármaco Alfo». No sabe si es un producto distinto. ¿Qué hace?", "No lo toca y consulta de inmediato a la enfermera", "Lo entrega, porque probablemente es el mismo", "Cambia la etiqueta con un lápiz", "Un nombre distinto puede ser un producto distinto; se consulta antes de cualquier entrega."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cuántas veces al día es «cada 8 horas»?", "3 veces", "24 horas divididas en 8 dan 3 veces al día."),
        ("¿Qué haces con un medicamento vencido?", "No lo uso y aviso a la enfermera", "Un medicamento vencido puede ser peligroso."),
        ("¿Quién cambia una hora de entrega?", "El profesional", "El técnico no cambia horas ni vías."),
    ],
    op=("Hoja de ejemplo: «Residente R4: Fármaco Épsilon, comprimido, vía oral, cada 6 horas, a las 06:00, 12:00, 18:00 y 24:00. Residente R5: Crema Zeta, sobre la piel, cada 12 horas, a las 08:00 y 20:00. Residente R6: Fármaco Eta, gotas, vía oral, una vez al día, a las 09:00». "
        "Escribe: cuántas entregas diarias tiene cada residente y cuántas hay en total; cuántas horas hay entre la primera y la última entrega de R4; y qué harías si el frasco del Fármaco Eta estuviera vencido.",
        "R4: 24 ÷ 6 = 4 entregas; R5: 2; R6: 1. Total: 4+2+1 = 7. Entre la primera y la última entrega de R4 hay 24 − 6 = 18 horas. Con un frasco vencido: no lo toca y avisa a la enfermera.",
        ["calcula 4, 2 y 1 entregas", "suma 7", "calcula 18 horas", "avisa ante el frasco vencido"],
        ["hoja con tres frecuencias, un total, una diferencia de horas y una conducta"],
        ["confundir «cada 6 horas» con 6 veces al día", "usar el frasco vencido", "cambiar la hora"],
        "Pregunta: «¿cada 6 horas son 4 veces o 6 veces al día?». Debe responder 4."),
    reinforce="Escribe la frecuencia diaria de «cada 12 horas», «cada 8 horas» y «cada 6 horas» y una hora posible de cada una.",
    extend="Explica con un ejemplo inventado por qué dos productos con nombres parecidos pueden causar una confusión peligrosa.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (verificación y errores, de ejemplo). Los cinco puntos de verificación: (1) persona correcta; (2) medicamento correcto; (3) cantidad indicada correcta; (4) vía correcta; (5) hora correcta. "
     "Situación A: la etiqueta del frasco dice «Fármaco Alfa» pero la hoja dice «Fármaco Beta»; falla el punto 2. Situación B: el frasco está vencido desde hace una semana. "
     "Situación C: la residente R2 dice que hoy no quiere tomar su medicamento. Situación D: después de recibir su medicamento, un residente presenta manchas en la piel y dificultad para respirar. "
     "Situación E: en la hoja de un residente hay una anotación ilegible en la hora de entrega y no se sabe si se entregó.")
build(
    O5, 3, F,
    use="Aprenderé a analizar situaciones de verificación y de error con la lista de puntos, a reconocer cuál falló y a decidir a quién se avisa y con qué urgencia.",
    prior=["Conozco la hoja de medicamentos y sus datos.", "Conozco el rechazo y la reacción adversa.", "Conozco la regla de avisar de inmediato."],
    explain=[
        "Analizar una situación de medicamentos es revisar qué punto de la verificación falló o qué riesgo apareció. Los cinco puntos son: persona, medicamento, cantidad indicada, vía y hora. Si alguno no coincide, no se entrega y se avisa a la enfermera. Un medicamento vencido o una anotación ilegible también se informan, porque no se puede asegurar la entrega correcta.",
        "Las situaciones se clasifican por urgencia. Una reacción adversa, como manchas en la piel o dificultad para respirar, es urgente: se avisa de inmediato a la enfermera y a emergencias y no se da nada. Un rechazo o un frasco vencido se informan a la enfermera sin demora, pero no son una emergencia. Nunca se «completa» ni se corrige una anotación dudosa por cuenta propia: se consulta a quien la escribió.",
        "Esta clase solo analiza situaciones de papel y no enseña a preparar ni administrar medicamentos." + LIM,
    ],
    vocab=[("verificación", "revisión de los cinco puntos antes de cada entrega"), ("urgencia", "qué tan pronto debe avisarse algo"), ("reacción adversa", "efecto dañino no esperado después de recibir un medicamento"), ("anotación ilegible", "registro que no se puede leer con seguridad"), ("entrega omitida", "entrega programada que no se realizó")],
    worked=[
        ("Identificar el punto fallido", "En una situación de ejemplo, la hoja indica la vía oral y la indicación del frasco dice «uso sobre la piel». ¿Qué punto de la verificación falla?", ["La vía del frasco no coincide con la de la hoja.", "Falla el punto 4: vía correcta."], "El punto 4: vía correcta"),
        ("Clasificar la urgencia", "Un residente de ejemplo dice que su comprimido «se ve de otro color que el de ayer». ¿Es urgente avisar a emergencias?", ["Un posible error de producto no es una emergencia, pero no se entrega.", "Se informa a la enfermera sin demora."], "No: no se entrega y se informa a la enfermera")],
    mistakes=[("Entregar el medicamento «porque es casi igual al de la hoja».", "Un solo punto que no coincide basta para no entregar.", "Si un punto no coincide, no se entrega y se avisa a la enfermera."),
              ("Completar una hora ilegible «con lo que parece».", "Se puede dar o no dar una entrega por error.", "Consulta a quien anotó y a la enfermera antes de cualquier decisión.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿cuántos puntos tiene la verificación de la ficha?", "Cinco", "Tres", "Siete", "La ficha enumera persona, medicamento, cantidad, vía y hora."),
        ("abc", "{F} ¿Qué punto falla en la situación A?", "El punto 2: medicamento correcto", "El punto 1: persona correcta", "El punto 5: hora correcta", "La etiqueta dice Alfa y la hoja Beta: el medicamento no coincide."),
        ("abc", "{F} ¿Qué corresponde en la situación A?", "No entregarlo y avisar a la enfermera", "Entregar el que está en la hoja", "Entregar el del frasco", "Si un punto no coincide no se entrega y se consulta."),
        ("abc", "{F} ¿Qué corresponde en la situación B?", "No usar el frasco vencido y avisar a la enfermera", "Usarlo, si hace falta", "Mezclarlo con otro frasco", "Un medicamento vencido no se usa."),
        ("abc", "{F} ¿Qué corresponde en la situación C?", "Respetar la decisión, registrar el rechazo y avisar a la enfermera", "Insistir hasta que lo tome", "Dárselo escondido en una comida", "El rechazo se respeta, se registra y se informa."),
        ("abc", "{F} ¿Qué corresponde en la situación D?", "Avisar de inmediato a la enfermera y a emergencias, y no dar nada", "Darle un antialérgico de la bodega", "Esperar a ver si se pasa", "Una posible reacción adversa grave es una emergencia."),
        ("abc", "{F} ¿Qué corresponde en la situación E?", "Consultar a quien anotó y a la enfermera antes de decidir", "Suponer que se entregó", "Entregar el medicamento otra vez", "Una entrega dudosa se aclara antes de repetirla o darla por hecha."),
        ("abc", "{F} ¿Cuántas situaciones de la ficha exigen avisar de inmediato a emergencias?", "Una", "Tres", "Cinco", "Solo la situación D, con manchas y dificultad para respirar, exige avisar de inmediato a emergencias."),
        ("abc", "{F} ¿En cuáles situaciones no se entrega el medicamento hasta aclarar el problema?", "En las situaciones A, B y E", "Solo en la situación C", "En todas, incluida la D, en que se da algo para aliviar", "A, B y E impiden la entrega; en C se respeta el rechazo y en D no se da nada."),
        ("abc", "{F} Un compañero dice: «En la situación A da lo mismo, ambos son pastillas». ¿Qué corresponde responder?", "Que un medicamento distinto puede dañar y no se entrega", "Que sí, porque las pastillas son parecidas", "Que sí, si la dosis es pequeña", "La verificación evita errores; dos productos con presentación parecida pueden ser muy diferentes."),
        ("abc", "{F} En la situación D, un familiar que está presente pide que el técnico le dé algo al residente. ¿Qué corresponde?", "Explicar con calma que se avisó a la enfermera y a emergencias y que no se da nada", "Dar lo que pide el familiar", "Pedirle que ayude a dar un medicamento", "El técnico no da nada y comunica con respeto lo que se está haciendo."),
        ("abc", "{F} Después del hecho de la situación D, ¿qué registra el técnico?", "Hora, lo observado, a quién avisó y a qué hora, sin diagnóstico", "Que es una alergia", "Que fue culpa del medicamento", "El registro describe hechos y no diagnostica."),
        ("abc", "{F} La enfermera pide al técnico que explique por qué la hoja de la situación E tiene una anotación ilegible. ¿Qué corresponde?", "Decir con honestidad lo que sabe y proponer escribir con letra clara y con hora", "Culpar a quien escribió", "Decir que no sabe nada", "La explicación honesta y la propuesta de mejora permiten corregir."),
    ],
    ctx=("abc", "{F} Una técnica en formación ve que un compañero está a punto de entregar el medicamento de R2 a otro residente por equivocación. El compañero no la ha visto. ¿Qué hace?", "Detiene la entrega con respeto, le avisa del error y avisa a la enfermera", "Espera a ver si el compañero se da cuenta", "Se lleva el medicamento sin decir nada", "Un error evitable se detiene con respeto y se informa."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces si un punto de la verificación no coincide?", "No se entrega y aviso a la enfermera", "Un punto fallido basta para no entregar."),
        ("¿Qué haces ante manchas en la piel y dificultad para respirar?", "Aviso de inmediato a la enfermera y a emergencias", "Es una posible reacción grave; no doy nada."),
        ("¿Qué haces con una anotación ilegible?", "Consulto a quien la escribió y a la enfermera", "No se completan anotaciones por suposición."),
    ],
    op=("Situaciones de ejemplo: «(1) El nombre del residente en la etiqueta del frasco es distinto al de la hoja. (2) Un residente no quiere tomar sus gotas. (3) Un residente dice que se siente mareado y con la cara hinchada después de su medicamento. (4) La hora de entrega de una anotación aparece borrosa». "
        "Clasifica cada una: qué punto de verificación o qué riesgo es; cuáles son urgentes (aviso inmediato a emergencias) y cuáles se informan a la enfermera sin demora; y escribe una frase de registro para la situación (2).",
        "(1) Punto 1: persona correcta; no se entrega y se avisa a la enfermera. (2) Rechazo: se respeta y se informa a la enfermera. (3) Reacción adversa: urgente; aviso inmediato a la enfermera y a emergencias, sin dar nada. (4) Anotación ilegible: se consulta a quien anotó y a la enfermera. Urgente: solo la 3. Registro de la 2: «09:00, el residente no quiso tomar sus gotas; se registró y se avisó a la enfermera».",
        ["clasifica las cuatro situaciones", "identifica la urgente", "respeta el rechazo", "el registro describe un hecho"],
        ["hoja con cuatro clasificaciones, una urgente y una frase de registro"],
        ["dar algo ante la reacción", "insistir con el rechazo", "suponer el contenido de la anotación borrosa"],
        "Pregunta: «¿cuántas situaciones son urgentes?». Debe responder una."),
    reinforce="Escribe los cinco puntos de verificación y una situación en que fallaría cada uno.",
    extend="Explica con un ejemplo inventado por qué un solo punto que no coincide es suficiente para no entregar un medicamento.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (control de stock y de registro, de ejemplo; sin dosis). Fármaco Alfa de ejemplo: 1 unidad por entrega y 2 entregas al día para cada uno de 5 residentes. Stock: 4 cajas de 30 unidades. Vencimiento de la caja más próxima a vencer: dentro de 10 días. "
     "Registro de una semana (7 días): entregas programadas, 5 residentes × 2 entregas × 7 días; entregas registradas como realizadas, 63; rechazos registrados con motivo, 5; entregas sin registro, 2. "
     "Regla: se avisa a la enfermera cuando el stock alcanza para menos de 5 días, cuando un medicamento vence antes de agotarse y ante cada entrega sin registro.")
build(
    O5, 4, F,
    use="Aprenderé a calcular el consumo y la duración de un stock, a ver si un medicamento vence antes de agotarse y a calcular el cumplimiento del registro, con enteros.",
    prior=["Sé multiplicar y dividir números enteros.", "Conozco la hoja de medicamentos.", "Sé calcular porcentajes de números enteros."],
    explain=[
        "Un stock es la cantidad de unidades disponibles de un medicamento. El consumo diario es la cantidad que se entrega por día: se multiplican las entregas por las unidades de cada entrega. Los días que dura el stock se calculan dividiendo el stock entre el consumo diario. Estas cuentas ayudan a pedir a tiempo, y el pedido lo hace la enfermera o quien la regla indique.",
        "También se compara la duración del stock con la fecha de vencimiento: si el medicamento vence antes de agotarse, la parte que sobra no se usa y se informa. El cumplimiento del registro se calcula con las entregas realizadas sobre las programadas, multiplicadas por 100. Una entrega sin registro es un riesgo, porque se puede repetir o dejar sin dar, y se avisa siempre a la enfermera.",
        "Todos los números son de ejemplo y no incluyen cantidades de principio activo ni dosis." + LIM,
    ],
    vocab=[("stock", "cantidad de unidades disponibles de un medicamento"), ("consumo diario", "unidades que se entregan en un día"), ("vencimiento", "fecha desde la cual el medicamento no debe usarse"), ("entrega programada", "entrega que debía hacerse según la hoja"), ("entrega sin registro", "entrega de la que no queda anotación, y por tanto es un riesgo"), ("cumplimiento del registro", "entregas realizadas sobre programadas, por 100")],
    worked=[
        ("Días de stock", "En otra sala de ejemplo se usan 6 unidades al día y hay 90 en stock. ¿Para cuántos días alcanza?", ["Se divide el stock entre el consumo diario.", "90 ÷ 6 = 15."], "15 días"),
        ("Vence antes de agotarse", "El stock de ejemplo alcanza para 12 días, pero vence en 9 días y se usan 5 unidades al día. ¿Cuántas unidades quedan sin usar al vencer?", ["Alcanza 12 días, pero solo se usa 9: sobran 3 días.", "3 días × 5 unidades = 15."], "15 unidades")],
    mistakes=[("Calcular los días de stock sin considerar el vencimiento.", "Se puede creer que el stock alcanza, cuando una parte vencerá antes de usarse.", "Compara siempre los días de stock con los días que faltan para el vencimiento."),
              ("Considerar «realizada» una entrega sin registro porque «seguro se dio».", "Se puede repetir la entrega o dejarla sin dar.", "Avisa a la enfermera y no se asume nada.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es el consumo diario de un medicamento?", "Las unidades que se entregan en un día", "El precio de la caja", "Las unidades que sobran al final del mes", "El consumo diario es la cantidad que se entrega por día."),
        ("=", "{F} ¿Cuántas unidades se entregan por día entre los 5 residentes?", "5*2*1", "Se multiplican los residentes por las entregas y por las unidades de cada entrega.", " unidades"),
        ("=", "{F} ¿Cuántas unidades hay en el stock?", "4*30", "Se multiplican las cajas por las unidades de cada caja.", " unidades"),
        ("=", "{F} ¿Para cuántos días alcanza el stock?", "4*30//(5*2*1)", "Se divide el stock entre el consumo diario.", " días"),
        ("abc", "{F} ¿Se cumple la regla de avisar cuando el stock alcanza para menos de 5 días?", "No: alcanza para 12 días", "Sí: alcanza para menos de 5 días", "Sí, porque hay solo 4 cajas", "El stock dura 12 días, más que los 5 días de la regla."),
        ("=", "{F} Si la caja próxima a vencer vence en 10 días, ¿cuántos días de stock sobran después del vencimiento?", "4*30//(5*2*1)-10", "Se restan los días hasta el vencimiento de los días que dura el stock.", " días"),
        ("=", "{F} ¿Cuántas unidades quedarían sin usar al vencer, si todo el stock venciera en 10 días?", "(4*30//(5*2*1)-10)*(5*2*1)", "Se multiplican los días que sobran por el consumo diario.", " unidades"),
        ("=", "{F} ¿Cuántas entregas estaban programadas en la semana?", "5*2*7", "Se multiplican los residentes por las entregas y por los días.", " entregas"),
        ("=", "{F} ¿Qué porcentaje de las entregas programadas se registró como realizada?", "63*100//(5*2*7)", "Se multiplican las entregas realizadas por 100 y se dividen entre las programadas.", " %"),
        ("=", "{F} ¿Cuántas entregas programadas quedaron sin explicación (ni realizadas ni rechazos registrados)?", "5*2*7-63-5", "Se restan las realizadas y los rechazos del total programado.", " entregas"),
        ("abc", "{F} ¿Qué corresponde por las 2 entregas sin registro?", "Avisar a la enfermera, que investigará con el equipo", "Anotarlas como realizadas", "Anotarlas como rechazadas", "Una entrega sin registro es un riesgo que se informa."),
        ("abc", "{F} ¿Qué se informa a la enfermera sobre el vencimiento?", "Que parte del stock vencerá antes de agotarse, con los datos calculados", "Que hay que tirar toda la caja", "Que el stock está perfecto", "El cálculo permite que la enfermera decida si se usa, se cambia o se pide menos."),
        ("abc", "{F} Un compañero dice: «Mejor pedir el doble para estar tranquilos». ¿Qué corresponde responder?", "Que el pedido lo decide la enfermera con los datos del consumo y del vencimiento", "Que sí, porque más es mejor", "Que sí, si lo guardamos en la bodega", "Pedir de más puede vencer sin usarse; la decisión es de la enfermera."),
    ],
    ctx=("abc", "{F} Al contar las unidades, la técnica en formación ve que faltan 2 respecto de lo que dice el registro. Nadie más está en la bodega. ¿Qué hace?", "Cuenta de nuevo con la enfermera, informa la diferencia y no la oculta ni la ajusta", "Anota que no faltan, para evitar problemas", "Repone dos de su casa", "Una diferencia se informa con datos, sin ocultarla ni ajustarla."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cómo se calculan los días de un stock?", "Stock ÷ consumo diario", "Así se sabe cuándo avisar para pedir."),
        ("¿Qué haces con una entrega sin registro?", "Aviso a la enfermera", "Una entrega sin registro es un riesgo."),
        ("¿Quién decide el pedido de medicamentos?", "La enfermera o quien la regla indique", "El técnico entrega los datos y no decide el pedido."),
    ],
    op=("Datos de ejemplo: «Fármaco de ejemplo con 1 unidad por entrega y 3 entregas al día para 4 residentes. Stock: 6 cajas de 20 unidades; la caja más próxima vence en 8 días. Registro de 5 días: 60 entregas programadas, 54 realizadas, 4 rechazos con motivo y 2 sin registro». "
        "Calcula: el consumo diario, el stock y para cuántos días alcanza; cuántos días sobran después del vencimiento; el porcentaje de entregas realizadas. Escribe qué avisarías a la enfermera.",
        "Consumo: 4×3×1 = 12 por día. Stock: 6×20 = 120. Alcanza 120 ÷ 12 = 10 días. Sobran 10 − 8 = 2 días (24 unidades). Realizadas: 54×100÷60 = 90 %. Avisaría que parte del stock vence antes de agotarse y que hay 2 entregas sin registro.",
        ["calcula 12, 120 y 10", "calcula 2 días sobrantes", "calcula 90 %", "avisa las entregas sin registro"],
        ["hoja con cuatro cálculos y una frase de aviso"],
        ["ignorar el vencimiento", "anotar las entregas sin registro como realizadas", "calcular mal el porcentaje"],
        "Pregunta: «¿qué haces con las dos entregas sin registro?». Debe responder avisar a la enfermera."),
    reinforce="Con 8 unidades al día y un stock de 120, calcula los días que alcanza y compáralos con un vencimiento en 12 días.",
    extend="Explica con un ejemplo inventado por qué pedir más de lo necesario puede ser un problema.",
)

# ============================================================ OAM-05, clase 5
F = ("Ficha 5 (comparar registros, de ejemplo). Lista de verificación de calidad de una hoja de medicamentos, 8 puntos: (1) fecha; (2) nombre completo de la persona; (3) medicamento; (4) vía; (5) hora programada y hora real; (6) firma de quien entregó; (7) observaciones (rechazo, molestias) con hechos; (8) sin tachaduras ni correctores. "
     "Hoja A: tiene fecha, nombre completo, medicamento, vía, hora programada y hora real, firma y observaciones «rechazó el comprimido a las 20:00»; no tiene tachaduras. Hoja B: solo marcas de visto (✔) sin hora ni firma, sin vía y con un dato corregido con corrector; sí tiene fecha, nombre y medicamento. "
     "Modo manual: 4 minutos por residente; modo digital: 3 minutos por residente más 6 minutos al iniciar y cerrar la sesión; 14 residentes con medicamentos.")
build(
    O5, 5, F,
    use="Aprenderé a comparar dos hojas de registro con una lista de verificación, a ver si un modo de registro conviene más y a proponer mejoras con respeto por la privacidad.",
    prior=["Conozco la hoja de medicamentos, la verificación y el stock.", "Sé sumar puntos y calcular tiempos.", "Sé leer una lista de verificación."],
    explain=[
        "Comparar dos hojas es aplicarles la misma lista de verificación y contar cuántos puntos cumple cada una. Los puntos incluyen la fecha, el nombre completo, el medicamento, la vía, las horas programada y real, la firma de quien entregó, las observaciones con hechos, y la ausencia de tachaduras o correctores. Una hoja con más puntos es más confiable, y la que cumple pocos puede ocultar errores.",
        "Un registro de solo marcas, sin hora ni firma, no permite saber quién entregó ni cuándo. Un dato tapado con corrector impide saber qué decía antes. Cuando una hoja tiene fallas, se informa a la enfermera con hechos, para corregir con trazabilidad y mejorar el formato. También se pueden comparar los modos de registro, manual o digital, por tiempo y por riesgo: el digital deja constancia automática pero exige clave personal y cerrar la sesión.",
        "Ningún modo de registro reemplaza la verificación previa ni la supervisión de la enfermera." + LIM,
    ],
    vocab=[("lista de verificación", "conjunto de puntos que se marcan como cumplidos o no"), ("hora programada", "hora indicada en la hoja"), ("hora real", "hora en que realmente se hizo la entrega"), ("observaciones", "hechos que se anotan fuera de lo programado, como un rechazo"), ("tachadura", "dato tapado o corregido sin trazabilidad"), ("formato de registro", "forma en que está organizada la hoja")],
    worked=[
        ("Contar puntos cumplidos", "Una hoja de ejemplo cumple 6 de los 8 puntos. ¿Cuántos puntos le faltan?", ["8 − 6 = 2.", "Faltan 2 puntos, que se informan a la enfermera."], "2 puntos"),
        ("Comparar tiempos", "En otro servicio de ejemplo, el modo manual toma 5 minutos por residente y hay 10 residentes. ¿Cuántos minutos demora?", ["Se multiplican los minutos por residente por los residentes.", "5 × 10 = 50."], "50 minutos")],
    mistakes=[("Marcar un ✔ en la hoja antes de que la entrega ocurra.", "El registro debe ser posterior y fiel; marcar antes puede ocultar una omisión.", "Anota solo lo que ya ocurrió, con hora real y firma."),
              ("Usar corrector para «dejar la hoja limpia».", "Se pierde el dato original y se pierde trazabilidad.", "Corrige con una línea, el valor correcto, hora y firma.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la hora real de una entrega?", "La hora en que realmente se hizo la entrega", "La hora indicada en la receta", "La hora de apertura de la bodega", "La hora real es la que ocurrió; la programada es la de la hoja."),
        ("abc", "{F} ¿Cuántos puntos de la lista cumple la hoja A?", "Ocho", "Siete", "Seis", "La hoja A tiene todos los datos pedidos y ninguna tachadura: cumple los ocho."),
        ("abc", "{F} ¿Qué puntos incumple la hoja B?", "Los puntos 4, 5, 6, 7 y 8: vía, horas, firma, observaciones y tachaduras", "Solo el punto 1: la fecha", "Solo el punto 2: el nombre", "La ficha dice que la hoja B no tiene vía, horas, firma ni observaciones y tiene un corrector."),
        ("=", "{F} ¿Cuántos puntos cumple la hoja B?", "8-5", "Se restan de los 8 puntos los 5 que incumple.", " puntos"),
        ("=", "{F} ¿Cuántos puntos más cumple la hoja A que la hoja B?", "8-(8-5)", "Se restan los puntos de la hoja B de los ocho de la hoja A.", " puntos"),
        ("abc", "{F} ¿Qué hoja es más confiable?", "La hoja A", "La hoja B", "Ambas por igual", "La hoja A cumple todos los puntos; la B no permite saber quién entregó ni cuándo."),
        ("=", "{F} ¿Cuántos minutos demora el registro manual de los 14 residentes?", "14*4", "Se multiplican los residentes por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos minutos demora el registro digital de los 14 residentes, incluyendo el inicio y el cierre de sesión?", "14*3+6", "Se multiplican los residentes por los minutos y se suman los de inicio y cierre.", " minutos"),
        ("=", "{F} ¿Cuántos minutos menos demora el modo digital que el manual?", "14*4-(14*3+6)", "Se restan los minutos del modo digital de los del manual.", " minutos"),
        ("abc", "{F} Un compañero dice: «El digital es mejor porque es más rápido, no necesitamos más reglas». ¿Qué corresponde responder?", "Que además de ser más rápido, requiere clave personal y cerrar la sesión", "Que tiene razón", "Que el manual es siempre mejor", "El modo digital exige reglas de privacidad igual que el manual."),
        ("abc", "{F} El técnico ve que en la hoja B hay un dato con corrector. ¿Qué corresponde?", "Informar a la enfermera y consultar a quien anotó, sin cambiar el dato por su cuenta", "Cambiar el dato por el que parece", "Dejarlo así", "Se corrige con trazabilidad y consultando a quien anotó."),
        ("abc", "{F} La enfermera propone un nuevo formato que incluya hora real y firma en cada fila. ¿Qué corresponde?", "Apoyar la propuesta y aplicarla desde la próxima hoja", "Rechazarla, porque da más trabajo", "Aplicarla solo a los residentes nuevos", "Los datos de hora real y firma son necesarios para la trazabilidad."),
        ("abc", "{F} En la hoja A figura «rechazó el comprimido a las 20:00». ¿Qué debe hacer el técnico con esa observación?", "Asegurarse de que se informó a la enfermera", "Borrarla para que la hoja se vea mejor", "Cambiarla por «entregado»", "El rechazo se registra y se informa; no se oculta."),
    ],
    ctx=("abc", "{F} Al cerrar el turno, la técnica ve que olvidó firmar tres entregas que sí hizo el personal autorizado ese día. ¿Qué hace?", "Informa a la enfermera para que las firme quien las entregó, con la hora real", "Las firma ella, porque estaba presente", "Las deja sin firma y no dice nada", "Solo firma quien realizó la entrega; se informa para regularizar con trazabilidad."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿para qué sirve una lista de verificación de la hoja?", "Para ver cuántos puntos cumple y qué falta", "Permite comparar la calidad de dos hojas."),
        ("¿Qué haces con un dato tapado con corrector?", "Consulto a quien anotó y aviso a la enfermera", "Se pierde el dato original y la trazabilidad."),
        ("¿Quién firma una entrega?", "Quien la realizó", "La firma indica quién responde por la entrega."),
    ],
    op=("Hojas de ejemplo: «Hoja 1: tiene fecha, nombre, medicamento, vía, hora programada y hora real, firma y observaciones; sin tachaduras. Hoja 2: tiene fecha, nombre y medicamento; solo marcas de visto; sin hora ni firma ni vía; una fila con corrector». Modos: manual, 5 minutos por residente; digital, 4 minutos por residente más 8 al iniciar y cerrar; 12 residentes. "
        "Usa la lista de la ficha. Escribe: cuántos puntos cumple cada hoja; cuál es más confiable y por qué; cuántos minutos toma cada modo; y qué informarías a la enfermera sobre la hoja 2.",
        "Hoja 1: 8 puntos. Hoja 2: cumple fecha, nombre y medicamento (puntos 1, 2 y 3): 3 puntos; fallan 4, 5, 6, 7 y 8. La hoja 1 es más confiable: permite saber quién entregó y cuándo. Manual: 12 × 5 = 60 minutos. Digital: 12 × 4 + 8 = 56 minutos. Informaría las fallas con hechos para corregir con trazabilidad.",
        ["cuenta 8 y 3 puntos", "elige la hoja 1 con razón", "calcula 60 y 56 minutos", "informa a la enfermera con hechos"],
        ["hoja con dos puntajes, una elección, dos cálculos y un informe"],
        ["decir que la hoja 2 es aceptable", "olvidar sumar los minutos de inicio y cierre", "usar corrector"],
        "Pregunta: «¿qué falla de la hoja 2 impide saber quién entregó?». Debe responder la falta de firma."),
    reinforce="Escribe los ocho puntos de la lista con tus palabras y marca cuáles cumple una hoja de solo ✔.",
    extend="Explica con un ejemplo inventado por qué una hoja con firma y hora real ayuda a evitar entregas repetidas.",
)

# ============================================================ OAM-06, clase 1
F = ("Ficha 1 (residencia de larga estadía de ejemplo, inventada). Viven 30 personas mayores: 12 con poca ayuda (autovalentes), 10 con ayuda parcial y 8 con ayuda mayor. Cuatro técnicos trabajan un turno de 8 horas. "
     "Tiempo estimado de trabajo de higiene y confort por residente en el turno (de ejemplo, para planificar): 20 minutos con poca ayuda, 30 con ayuda parcial y 45 con ayuda mayor. "
     "Reglas: golpear antes de entrar, presentarse, explicar lo que se ofrece y respetar la respuesta; cuidar la privacidad; estimular que la persona haga lo que pueda; la técnica ergonómica de cada cuidado la enseña un instructor.")
build(
    O6, 1, F,
    use="Aprenderé qué es el cuidado de higiene y confort en una residencia, qué principios lo guían, cómo se estima la carga de trabajo y qué se avisa siempre.",
    prior=["Conozco los derechos de las personas mayores.", "Sé multiplicar y sumar números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería (mención Adulto Mayor), las necesidades de higiene y confort son el aseo de la persona y de su entorno y todo lo que le da bienestar físico y emocional. Una residencia de larga estadía es el lugar donde una persona mayor vive de forma permanente. Los principios son tres: la privacidad (cuidar su intimidad), la autonomía (que haga lo que pueda por sí misma) y la acogida (un trato cálido, por su nombre y con respeto).",
        "El grado de ayuda que necesita cada persona lo evalúa el equipo: poca ayuda, ayuda parcial o ayuda mayor. Con esa información se estima la carga de trabajo y se organizan los horarios. Ergonomía es cuidar la postura y el esfuerzo de quien trabaja; cómo se hace lo enseña un instructor. El técnico no realiza un cuidado sin consentimiento de la persona y avisa de cualquier cambio que observe, como una marca en la piel, un dolor o un ánimo distinto.",
        "Si la persona se cae, se desmaya o se siente mal durante un cuidado, se avisa de inmediato a la enfermera y a emergencias y no se actúa por cuenta propia." + LIM,
    ],
    vocab=[("larga estadía", "lugar donde una persona mayor vive de forma permanente"), ("privacidad", "cuidado de la intimidad de la persona"), ("autonomía", "capacidad de hacer lo que se puede por sí misma"), ("acogida", "trato cálido, por su nombre y con respeto"), ("grado de ayuda", "cuánta ayuda necesita la persona, evaluada por el equipo"), ("ergonomía", "cuidado de la postura y el esfuerzo de quien trabaja")],
    worked=[
        ("Estimar la carga", "En otra residencia de ejemplo hay 5 residentes con poca ayuda (20 minutos cada uno) y 4 con ayuda mayor (45 minutos cada uno). ¿Cuántos minutos suman en total?", ["5 × 20 = 100 minutos.", "4 × 45 = 180; total 100 + 180 = 280."], "280 minutos"),
        ("Respetar la privacidad", "Un técnico de ejemplo entra a una pieza sin golpear porque «la puerta estaba abierta». ¿Qué principio descuida?", ["La puerta abierta no autoriza a entrar sin avisar.", "Descuida la privacidad."], "La privacidad")],
    mistakes=[("Hacerle todo a una persona mayor «para apurarse» aunque pueda hacer parte por sí misma.", "Le quita autonomía y puede disminuir sus capacidades.", "Pregunta qué quiere hacer ella y apoya solo lo necesario."),
              ("No avisar de una marca roja en la piel de un residente porque «no parece grave».", "Solo el profesional evalúa su importancia, y avisar a tiempo evita complicaciones.", "Anota qué viste y dónde, y avisa a la enfermera.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la privacidad en el cuidado?", "Cuidar la intimidad de la persona", "Cerrar las puertas con llave siempre", "Hacer los cuidados rápidamente", "La privacidad protege la intimidad de la persona."),
        ("abc", "{F} ¿Cuántos residentes necesitan ayuda mayor?", "8", "12", "10", "La ficha indica 8 residentes con ayuda mayor."),
        ("=", "{F} ¿Cuántos minutos estimados se necesitan para los residentes con poca ayuda?", "12*20", "Se multiplican los residentes con poca ayuda por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos minutos estimados se necesitan para los residentes con ayuda parcial?", "10*30", "Se multiplican los residentes con ayuda parcial por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos minutos estimados se necesitan en total para los 30 residentes?", "12*20+10*30+8*45", "Se suman los minutos de los tres grupos de residentes.", " minutos"),
        ("=", "{F} Si los 900 minutos se reparten por igual entre los 4 técnicos, ¿cuántos minutos le corresponden a cada uno?", "(12*20+10*30+8*45)//4", "Se divide el total de minutos entre los técnicos.", " minutos"),
        ("abc", "{F} Una residente dice que hoy prefiere que su aseo sea más tarde, porque está cansada. ¿Qué hace el técnico?", "Respeta su preferencia, la registra y avisa a la enfermera si cambia lo programado", "Insiste en que se haga ahora, porque está en el horario", "Lo hace igual y no avisa a nadie", "La preferencia se respeta dentro de lo posible y se informa para reorganizar."),
        ("abc", "{F} Un técnico encuentra a un residente en el baño con una marca roja en la espalda que no había visto antes. ¿Qué hace?", "Anota lo observado, con lugar y hora, y avisa a la enfermera", "Le pone una crema de la bodega", "Le dice que no es nada", "Un cambio en la piel lo evalúa el profesional; el técnico observa y avisa."),
        ("abc", "{F} Un residente se resbala durante su aseo. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias, y no lo mueve", "Lo levanta enseguida para que no se enfríe", "Lo seca y lo acuesta", "Ante una caída se avisa de inmediato; mover a la persona puede agravar una lesión."),
        ("abc", "{F} Un compañero dice: «Con los residentes de ayuda mayor no hace falta preguntarles nada, porque no entienden». ¿Qué corresponde responder?", "Que siempre se les explica y se busca su consentimiento y su respuesta", "Que tiene razón, si están muy dependientes", "Que solo se les explica a los familiares", "Toda persona tiene derecho a ser informada y a participar en lo que le ocurre."),
        ("abc", "{F} Una técnica trabaja encorvada toda la mañana y le duele la espalda. ¿Qué corresponde?", "Avisar a su jefatura y pedir apoyo del instructor en ergonomía", "Seguir sin decir nada", "Dejar de atender a los residentes de ayuda mayor", "El cuidado de la propia postura es parte de la seguridad laboral."),
        ("=", "{F} Si un técnico tiene 3 residentes con poca ayuda, 3 con ayuda parcial y 2 con ayuda mayor, ¿cuántos minutos estimados le corresponden?", "3*20+3*30+2*45", "Se multiplican los residentes de cada grupo por sus minutos y se suman.", " minutos"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la acogida?", "Un trato cálido, por su nombre y con respeto", "Una actividad social en grupo", "La hora en que llega el equipo", "La acogida es la forma amable y respetuosa de recibir a la persona."),
    ],
    ctx=("abc", "{F} Un residente muy callado dice a la técnica que prefiere que lo ayude un técnico hombre porque le da vergüenza con ella. ¿Qué hace?", "Respeta su preferencia dentro de lo posible y avisa a la enfermera para reorganizar", "Le dice que debe aceptarlo porque son todos profesionales", "Hace el cuidado sin avisar", "Se respeta el pudor de la persona y se pide a la enfermera reorganizar el turno."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces antes de comenzar un cuidado?", "Golpeo, me presento, explico y pido su respuesta", "Así se respeta su privacidad y su consentimiento."),
        ("¿Qué haces si observas una marca nueva en la piel?", "La anoto y aviso a la enfermera", "El técnico observa y avisa; no evalúa."),
        ("¿Qué haces si una persona se cae durante el cuidado?", "Aviso de inmediato a la enfermera y a emergencias", "No muevo a la persona ni actúo por cuenta propia."),
    ],
    op=("Caso de ejemplo: en una residencia de larga estadía hay 20 personas: 8 con poca ayuda (20 minutos cada una), 8 con ayuda parcial (30 minutos) y 4 con ayuda mayor (45 minutos); trabajan 4 técnicos. Un residente dice que no quiere que lo ayuden hoy. "
        "Calcula: los minutos totales y los minutos por técnico si se reparten por igual. Escribe: qué hace el técnico ante la negativa del residente; qué observaría y avisaría si ve una marca nueva en la piel; y una frase de acogida.",
        "Total: 8×20 + 8×30 + 4×45 = 160 + 240 + 180 = 580; por técnico: 580 ÷ 4 = 145 minutos. Ante la negativa: respeta su decisión, ofrece más tarde y avisa a la enfermera. Marca nueva: anota lugar y hora y avisa a la enfermera. Frase: «Buenos días, don Mario, ¿le parece bien que le ayudemos con su aseo cuando usted quiera?».",
        ["calcula 580 y 145", "respeta la negativa y avisa", "anota y avisa la marca nueva", "la frase es respetuosa"],
        ["hoja con dos cálculos, una conducta ante la negativa, una observación y una frase de acogida"],
        ["insistir con el cuidado", "calcular mal el total", "no avisar la marca en la piel"],
        "Pregunta: «¿tu frase llama a la persona por su nombre y le da opciones?». Si no, pídele reescribirla."),
    reinforce="Escribe los tres principios del cuidado de higiene y confort y una conducta concreta de cada uno.",
    extend="Explica con un ejemplo inventado por qué dejar que la persona haga lo que puede es mejor que hacerlo todo por ella.",
)

# ============================================================ OAM-06, clase 2
F = ("Ficha 2 (plan de cuidados individual, de ejemplo). Aurora, autovalente: prefiere el aseo por la tarde, le gusta la música suave y quiere elegir su ropa. Bernardo, con ayuda parcial: prefiere afeitarse él mismo y necesita que le dejen el espejo a su alcance. "
     "Carlota, con ayuda mayor: tiene una pauta de cambios de posición cada 3 horas indicada por la enfermera; le gusta que le hablen por su nombre; su ropa de cama se mantiene limpia y sin arrugas. "
     "Confort ambiental: luz suave, ruido bajo, temperatura general agradable, objetos personales a su alcance y timbre de llamado al alcance de la mano.")
build(
    O6, 2, F,
    use="Aprenderé qué es un plan de cuidados individual, cómo se ve el confort del ambiente y qué es la prevención de lesiones por presión, solo como concepto.",
    prior=["Conozco los principios de higiene y confort.", "Sé leer una ficha.", "Sé calcular horarios sencillos."],
    explain=[
        "El plan de cuidados individual es un documento de cada residente donde la enfermera registra cómo cuidarlo: su grado de ayuda, sus horarios, sus preferencias y sus indicaciones. El técnico lo lee antes de cada cuidado y no lo cambia por su cuenta. Las preferencias, como el horario del aseo o la ropa que desea usar, se respetan dentro de lo posible. Si una preferencia no puede cumplirse, se explica con respeto y se avisa a la enfermera.",
        "El confort ambiental es que el entorno ayude al bienestar: luz suave, poco ruido, temperatura general agradable, ropa de cama limpia y sin arrugas, objetos personales y timbre de llamado al alcance. Las lesiones por presión son daños en la piel que pueden aparecer cuando una persona pasa mucho tiempo en la misma posición. Para prevenirlas, la enfermera puede indicar una pauta de cambios de posición con horarios. El técnico cumple la pauta indicada y avisa si observa algún cambio en la piel.",
        "Esta clase no enseña cómo se cambia de posición a una persona: eso lo enseña un instructor con práctica supervisada." + LIM,
    ],
    vocab=[("plan de cuidados individual", "documento de la enfermera con horarios, preferencias e indicaciones de cada residente"), ("preferencia", "lo que la persona elige o le gusta"), ("confort ambiental", "ambiente que ayuda al bienestar: luz, ruido, temperatura y orden"), ("lesión por presión", "daño en la piel por pasar mucho tiempo en la misma posición"), ("pauta de cambios de posición", "horarios indicados por la enfermera para cambiar de posición a una persona"), ("timbre de llamado", "aparato con que la persona avisa que necesita ayuda")],
    worked=[
        ("Calcular una pauta", "Una pauta de ejemplo indica un cambio de posición cada 4 horas durante 12 horas. ¿Cuántos cambios hay en ese tiempo?", ["Se divide el tiempo total entre el intervalo de la pauta.", "12 ÷ 4 = 3."], "3 cambios"),
        ("Respetar una preferencia", "En el plan de un residente de ejemplo dice «prefiere ducharse por la mañana». Hoy la mañana está llena de actividades. ¿Qué corresponde?", ["La preferencia se respeta dentro de lo posible.", "Se explica con respeto la dificultad y se avisa a la enfermera para reorganizar."], "Explicar con respeto y avisar a la enfermera para reorganizar")],
    mistakes=[("Poner el timbre de llamado lejos de la persona «para que no moleste».", "La persona no podrá pedir ayuda cuando la necesite.", "Déjalo siempre al alcance de la mano."),
              ("Decidir cambiar la hora de una pauta de posición porque «la persona está durmiendo».", "La pauta la define la enfermera; cambiarla puede aumentar el riesgo.", "Avisa a la enfermera y ella decide.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es el plan de cuidados individual?", "El documento de la enfermera con horarios, preferencias e indicaciones de cada residente", "La lista de residentes de la residencia", "El menú de la semana", "El plan es individual y lo escribe la enfermera."),
        ("abc", "{F} ¿Qué prefiere Aurora?", "El aseo por la tarde", "El aseo por la mañana", "Que le hagan todo", "La ficha dice que Aurora prefiere el aseo por la tarde."),
        ("abc", "{F} ¿Qué necesita Bernardo para afeitarse?", "Tener el espejo a su alcance", "Que otra persona lo afeite", "Evitar afeitarse", "Bernardo prefiere afeitarse él mismo y necesita el espejo a su alcance."),
        ("=", "{F} ¿Cuántos cambios de posición se hacen en 12 horas con la pauta de Carlota?", "12//3", "Se divide el tiempo entre el intervalo de la pauta.", " cambios"),
        ("=", "{F} ¿Cuántos cambios de posición se hacen en 24 horas con la pauta de Carlota?", "24//3", "Se divide el día de 24 horas entre el intervalo de la pauta.", " cambios"),
        ("=", "{F} Si la pauta de Carlota comienza a las 08:00, ¿a qué hora (en horas del día) es el tercer cambio?", "8+3+3", "Se suman 3 horas al inicio por cada cambio posterior al primero.", " horas"),
        ("abc", "{F} ¿Cuál de estos elementos forma parte del confort ambiental?", "Luz suave y ruido bajo", "El resultado de un examen", "La receta de un medicamento", "El confort ambiental incluye luz, ruido, temperatura y orden."),
        ("abc", "{F} El técnico ve que el timbre de Carlota quedó caído al piso, fuera de su alcance. ¿Qué hace?", "Lo vuelve a poner al alcance de su mano", "Lo deja para que la persona no lo use", "Espera a que la enfermera pase", "Que la persona pueda pedir ayuda es una condición de seguridad."),
        ("abc", "{F} Durante la tarde, el técnico nota que la piel de la espalda de Carlota está enrojecida. ¿Qué hace?", "Anota lo observado, con lugar y hora, y avisa a la enfermera", "Le pone una crema por su cuenta", "Le dice que es normal", "Un cambio en la piel lo evalúa el profesional; el técnico observa y avisa."),
        ("abc", "{F} Un compañero propone saltarse el cambio de las 14:00 de Carlota «porque duerme tranquila». ¿Qué corresponde?", "Avisar a la enfermera, que decide si se mantiene o se ajusta la pauta", "Saltarlo, porque descansa", "Cambiarlo para las 16:00 sin avisar", "La pauta es una indicación; solo la enfermera la modifica."),
        ("abc", "{F} Aurora quiere elegir su ropa, pero el técnico, por apuro, la viste con lo que tiene a mano. ¿Qué principio descuida?", "La autonomía y la preferencia de la persona", "El confort ambiental", "El timbre de llamado", "Elegir su ropa es parte de su autonomía y de su dignidad."),
        ("=", "{F} Si cada cuidado de Aurora, Bernardo y Carlota toma 20, 30 y 45 minutos respectivamente, ¿cuántos minutos suman los tres?", "20+30+45", "Se suman los minutos de cada cuidado.", " minutos"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es una lesión por presión?", "Un daño en la piel por pasar mucho tiempo en la misma posición", "Una herida por una caída", "Una alergia a un alimento", "Es un daño de la piel asociado a la presión sostenida."),
    ],
    ctx=("abc", "{F} Aurora le dice al técnico que hoy no quiere escuchar música y que prefiere silencio. En su plan figura que le gusta la música suave. ¿Qué hace?", "Respeta lo que dice hoy, registra el cambio de preferencia y avisa a la enfermera para actualizar el plan", "Pone la música, porque así dice el plan", "Le dice que debe elegir una de las dos cosas", "Las preferencias cambian y se respetan; se informa para actualizar el plan."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿quién define la pauta de cambios de posición?", "La enfermera", "El técnico cumple la pauta y no la modifica."),
        ("¿Dónde debe estar siempre el timbre de llamado?", "Al alcance de la mano de la persona", "Así puede pedir ayuda cuando la necesite."),
        ("¿Qué haces si la persona cambia una preferencia del plan?", "La respeto y aviso a la enfermera para actualizar el plan", "Las preferencias pueden cambiar con el tiempo."),
    ],
    op=("Plan de ejemplo: «Belisario, con ayuda mayor: pauta de cambios de posición cada 4 horas indicada por la enfermera, desde las 06:00; prefiere que lo llamen «don Beli»; le gusta tener su radio a mano; timbre al alcance. Dorotea, con ayuda parcial: prefiere el aseo después del almuerzo y elegir su ropa». "
        "Escribe: cuántos cambios de posición hay en 24 horas con la pauta de Belisario y a qué horas ocurren; tres cosas de confort que revisarías en su pieza; qué respetarías de las preferencias de Dorotea; y qué harías si notas la piel enrojecida de Belisario.",
        "24 ÷ 4 = 6 cambios; a las 06:00, 10:00, 14:00, 18:00, 22:00 y 02:00. Confort: timbre al alcance, radio a mano y ropa de cama limpia y sin arrugas. Dorotea: el aseo después del almuerzo y la elección de su ropa. Con la piel enrojecida: anotar lugar y hora y avisar a la enfermera, sin tratar por su cuenta.",
        ["calcula 6 cambios y las horas", "nombra tres elementos de confort", "respeta las preferencias de Dorotea", "avisa a la enfermera ante la piel enrojecida"],
        ["hoja con un cálculo, seis horas, tres elementos, dos preferencias y una conducta"],
        ["tratar la piel por cuenta propia", "cambiar la pauta sin avisar", "olvidar el timbre"],
        "Pregunta: «¿tu respuesta sobre la piel enrojecida dice avisar o tratar?». Debe decir avisar."),
    reinforce="Escribe tres elementos del confort ambiental y una preferencia de ejemplo de una persona mayor.",
    extend="Explica con un ejemplo inventado por qué una pauta de posición se cumple con respeto por el sueño de la persona.",
)

# ============================================================ OAM-06, clase 3
F = ("Ficha 3 (casos y pauta de acogida y respeto, de ejemplo). Pauta de cinco criterios: (1) golpea y se presenta; (2) explica lo que ofrece y respeta la respuesta de la persona; (3) cuida la privacidad; (4) estimula que haga lo que puede; (5) respeta preferencias y ritmo y avisa a la enfermera de cambios observados. "
     "Caso A: un técnico golpea, se presenta, explica, deja la cortina cerrada, anima a la residente a lavarse las manos ella misma, respeta su ritmo y avisa de una pequeña marca roja que vio en su brazo; cumple los cinco. "
     "Caso B: un técnico entra sin golpear, no explica y deja la puerta abierta de par en par mientras asiste a una residente; hace todo por ella y no avisa de nada; no cumple ninguno de los cinco criterios. "
     "Caso C: una técnica golpea, se presenta, explica y cuida la privacidad; la residente dice que hoy no quiere el aseo y la técnica insiste varias veces hasta que acepta; cumple los criterios 1, 2, 3 y 4. "
     "Caso D: un técnico golpea, explica, cuida la privacidad y estimula la autonomía, pero no avisa a la enfermera de que el residente tiene un moretón en el brazo; cumple los criterios 1, 2, 3 y 4.")
build(
    O6, 3, F,
    use="Aprenderé a analizar casos de cuidado con una pauta de acogida y respeto, a reconocer la conducta que falló y a decidir qué se avisa y a quién.",
    prior=["Conozco los principios de higiene y confort y el plan de cuidados individual.", "Sé calcular porcentajes de números enteros.", "Conozco la regla de avisar los cambios observados."],
    explain=[
        "Para analizar un caso de cuidado se compara lo ocurrido con una pauta. Los criterios son golpear y presentarse, explicar y respetar la respuesta, cuidar la privacidad, estimular la autonomía y respetar las preferencias y el ritmo, avisando a la enfermera de lo que se observa. Cada criterio cuida un derecho: el trato digno, la privacidad, la decisión de la persona y su seguridad.",
        "Insistir hasta que una persona acepta no es respetar su decisión: la presión le quita libertad, aunque el cuidado sea necesario. Si el cuidado es importante, el técnico informa a la enfermera, que evalúa cómo proceder. Avisar de lo que se observa, por ejemplo un moretón o una marca roja, también forma parte del cuidado, porque solo el profesional evalúa si es importante. Y se evita infantilizar o hablar de la persona como si no estuviera presente.",
        "El análisis es una forma de mejorar el equipo y no de culpar a una persona." + LIM,
    ],
    vocab=[("trato digno", "trato que reconoce a la persona como sujeto de derechos"), ("presión", "insistencia que le quita libertad a la persona para decidir"), ("moretón", "mancha de color en la piel que puede indicar un golpe"), ("estimular la autonomía", "animar a la persona a hacer lo que puede por sí misma"), ("pauta de acogida", "lista de conductas esperadas en el cuidado")],
    worked=[
        ("Aplicar un criterio", "Un técnico de ejemplo dice a una residente: «Usted no sabe, yo le hago todo». ¿Qué criterio descuida?", ["Le quita la posibilidad de hacer lo que puede.", "Descuida el criterio 4: estimular la autonomía."], "El criterio 4"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 3 de los 5 criterios. ¿Qué porcentaje es?", ["3 × 100 = 300.", "300 ÷ 5 = 60."], "60 %")],
    mistakes=[("Insistir con una residente porque «el aseo es parte del horario».", "Se vulnera su derecho a decidir; el horario no reemplaza su consentimiento.", "Respeta su respuesta, ofrece otro momento y avisa a la enfermera."),
              ("Comentar frente a otras personas el moretón de un residente «para hacerlo reír».", "Expone su intimidad y puede avergonzarlo.", "Habla del hallazgo en privado con la enfermera.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿por qué insistir hasta que la persona acepta no es respetar su decisión?", "Porque la presión le quita libertad para decidir", "Porque siempre debe aceptar", "Porque la insistencia es un trato cálido", "Insistir con presión no es respetar la decisión."),
        ("abc", "{F} ¿Cuántos criterios cumple el técnico del caso B?", "Ninguno", "Dos", "Cuatro", "No golpeó, no explicó, dejó la puerta abierta, hizo todo por ella y no avisó de nada."),
        ("abc", "{F} ¿Qué criterio incumple la técnica del caso C?", "El criterio 5: respetar la decisión y el ritmo, y avisar a la enfermera", "El criterio 1: golpear y presentarse", "El criterio 3: cuidar la privacidad", "Insistir hasta que acepta no respeta su respuesta."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso D?", "El criterio 5: avisar a la enfermera de los cambios observados", "El criterio 2: explicar", "El criterio 4: estimular la autonomía", "No avisó del moretón del residente."),
        ("abc", "{F} ¿Qué caso cumple los cinco criterios?", "El caso A", "El caso B", "El caso C", "El caso A cumple los cinco, según la ficha."),
        ("=", "{F} ¿Cuántos criterios cumplen en total los cuatro casos?", "5+0+4+4", "Se suman los criterios cumplidos por cada caso.", " criterios"),
        ("=", "{F} ¿Qué porcentaje del total de criterios (4 casos de 5) se cumplió?", "(5+0+4+4)*100//(4*5)", "Se multiplica el total cumplido por 100 y se divide entre los criterios evaluados.", " %"),
        ("=", "{F} ¿Cuántos criterios incumplen entre los casos B, C y D?", "(5-0)+(5-4)+(5-4)", "Se restan los criterios cumplidos de los 5 de cada caso y se suman las fallas.", " criterios"),
        ("abc", "{F} En el caso D, ¿qué debería informar el técnico a la enfermera?", "Que vio un moretón en el brazo del residente, con lugar y hora, sin suponer la causa", "Que el residente tuvo una caída", "Que alguien lo golpeó", "Se informa solo lo observado; la causa la evalúa el profesional."),
        ("abc", "{F} Un compañero dice: «En el caso C, como la residente aceptó, todo salió bien». ¿Qué corresponde responder?", "Que aceptar por insistencia no es un consentimiento libre", "Que sí, porque el aseo se realizó", "Que sí, porque el horario es lo primero", "Un consentimiento libre no se obtiene con presión."),
        ("abc", "{F} Una compañera de la técnica del caso C le dice «eres una persona poco respetuosa». ¿Qué corresponde?", "Describir lo ocurrido y proponer una mejora, sin juzgar a la persona", "Repetir el juicio frente al equipo", "No decir nada nunca", "La crítica con hechos permite aprender sin dañar."),
        ("=", "{F} Si el técnico del caso D hubiera avisado del moretón, ¿cuántos criterios habría cumplido?", "4+1", "Se suma el criterio 5 a los cuatro que ya cumplía.", " criterios"),
        ("abc", "{F} Una residente dice que le duele el brazo donde tiene un moretón y que no recuerda cómo se lo hizo. ¿Qué hace el técnico?", "Anota lo dicho y lo observado y avisa de inmediato a la enfermera", "Le dice que se lo debió dar una pieza de la cama", "Le masajea el brazo", "El técnico registra y avisa; no supone causas ni trata."),
    ],
    ctx=("abc", "{F} Un técnico va a ayudar a un residente que se niega a levantarse de la cama. Explicó lo que ofrece y el residente respondió que no. Está retrasado con la ronda. ¿Qué hace?", "Respeta su respuesta, ofrece volver más tarde y avisa a la enfermera", "Le dice que si no se levanta no habrá desayuno", "Lo levanta sin su acuerdo para cumplir el horario", "No se amenaza ni se fuerza: se respeta la respuesta y se informa."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces si una persona rechaza el cuidado?", "Respeto su respuesta y aviso a la enfermera", "Insistir con presión vulnera su derecho a decidir."),
        ("¿Qué haces si ves un moretón nuevo?", "Anoto lo observado y aviso a la enfermera", "El técnico no supone la causa; informa."),
        ("¿Cuántos criterios tiene la pauta de la ficha?", "5", "Presentarse, explicar, privacidad, autonomía y avisar cambios."),
    ],
    op=("Casos de ejemplo: «A: un técnico golpea, se presenta y pregunta a una residente si le parece bien que la ayude con su aseo; ella dice que sí; el técnico le ofrece que se lave la cara ella misma y cierra la cortina; al terminar anota que está más callada que de costumbre y se lo avisa a la enfermera. B: una técnica entra sin golpear y le dice a un residente «vamos, abuelito, que se nos acaba el tiempo», lo desviste sin preguntar y deja la puerta abierta; no avisa de nada». "
        "Usa la pauta de la ficha. Escribe: cuántos criterios cumple cada caso; qué criterios incumple B y cómo lo corregirías; y qué frase de acogida usarías en B.",
        "A cumple los cinco. B incumple los criterios 1 (no golpea ni se presenta), 2 (no explica), 3 (puerta abierta), 4 (le hace todo) y 5 (no avisa): cumple 0. Corrección: golpear y presentarse, explicar, cerrar la puerta, dejar que el residente haga lo que puede, respetar su ritmo y avisar de lo que observe. Frase: «Buenos días, don Mario, soy Ana; ¿le parece bien que lo ayude con su aseo ahora o prefiere más tarde?».",
        ["cuenta 5 criterios en A", "identifica los criterios incumplidos de B", "propone correcciones concretas", "la frase de acogida es respetuosa y no infantiliza"],
        ["hoja con criterios, correcciones y una frase de acogida"],
        ["mantener el trato infantilizado", "no mencionar la puerta abierta", "juzgar a la técnica"],
        "Pregunta: «¿tu frase de acogida llama a la persona por su nombre?». Si no, pídele reescribirla."),
    reinforce="Reescribe la frase «vamos, abuelito, que se nos acaba el tiempo» con una forma respetuosa.",
    extend="Explica con un ejemplo inventado por qué una persona mayor puede sentirse afectada cuando la tratan como a un niño.",
)

# ============================================================ OAM-06, clase 4
F = ("Ficha 4 (carga de trabajo, planilla de ejemplo). Residencia de 30 personas con cuatro técnicos. Tiempo estimado por residente: 20 minutos con poca ayuda, 30 con ayuda parcial y 45 con ayuda mayor. "
     "Residentes a cargo: técnico 1, 3 con poca ayuda, 3 con ayuda parcial y 2 con ayuda mayor; técnico 2, 3, 2 y 2; técnico 3, 3, 3 y 2; técnico 4, 3, 2 y 2. "
     "Regla del servicio (de ejemplo): cada técnico dedica como máximo 240 minutos del turno a higiene y confort. Si se supera, se avisa a la enfermera para reorganizar.")
build(
    O6, 4, F,
    use="Aprenderé a calcular la carga de trabajo de higiene y confort de cada técnico, a compararla con un máximo y a informar a la enfermera sin proponer cambios por cuenta propia.",
    prior=["Sé multiplicar, sumar y comparar números enteros.", "Conozco los grados de ayuda.", "Sé aplicar una regla de aviso."],
    explain=[
        "La carga de trabajo es el tiempo estimado que necesita cada técnico para los cuidados de las personas a su cargo. Se calcula multiplicando la cantidad de residentes de cada grupo por los minutos de ese grupo y sumando los resultados. Se compara con el máximo que fija el servicio para ese tipo de cuidados. Si la carga lo supera, se avisa a la enfermera, que reorganiza los grupos o pide apoyo.",
        "Los minutos son estimaciones de ejemplo para organizar; los reales cambian según cada persona y cada día. Una carga repartida de forma justa permite cuidar sin apuro y con respeto, mientras que una carga excesiva aumenta los errores y la fatiga. El técnico informa los datos y no cambia por su cuenta los residentes ni los horarios.",
        "Las cifras son inventadas y sirven solo para practicar la lectura de una planilla." + LIM,
    ],
    vocab=[("carga de trabajo", "tiempo estimado que necesita un técnico para sus cuidados"), ("estimación", "valor aproximado que se usa para organizar, no una medida exacta"), ("máximo del servicio", "tope de minutos que fija el servicio para ese tipo de cuidados"), ("reorganizar", "cambiar quién atiende a quién o cuándo, decidido por la enfermera"), ("apoyo", "ayuda adicional de otro técnico")],
    worked=[
        ("Calcular la carga", "Un técnico de ejemplo tiene 2 residentes con poca ayuda (20 minutos) y 1 con ayuda mayor (45 minutos). ¿Cuántos minutos suma su carga?", ["2 × 20 = 40.", "40 + 45 = 85."], "85 minutos"),
        ("Comparar con el máximo", "La carga de un técnico de ejemplo es 250 minutos y el máximo es 240. ¿Cuántos minutos sobrepasa?", ["Se resta el máximo de la carga.", "250 − 240 = 10."], "10 minutos")],
    mistakes=[("Cambiar un residente de un técnico a otro «para equilibrar» sin consultar.", "La asignación la define la enfermera; un cambio por cuenta propia puede dejar a alguien sin cuidado.", "Informa las cargas a la enfermera y espera su decisión."),
              ("Tomar los minutos como una medida exacta de cuánto tarda cada persona.", "Son estimaciones; cada día y persona cambia.", "Úsalos para organizar y adapta con calma, avisando si no alcanza.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la carga de trabajo?", "El tiempo estimado que necesita un técnico para sus cuidados", "El número de pacientes de la residencia", "La hora en que empieza el turno", "La carga es el tiempo estimado de trabajo de cada técnico."),
        ("=", "{F} ¿Cuántos minutos suma la carga del técnico 1?", "3*20+3*30+2*45", "Se multiplican los residentes de cada grupo por sus minutos y se suman.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma la carga del técnico 2?", "3*20+2*30+2*45", "Se multiplican los residentes de cada grupo por sus minutos y se suman.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma la carga del técnico 3?", "3*20+3*30+2*45", "Se multiplican los residentes de cada grupo por sus minutos y se suman.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma la carga del técnico 4?", "3*20+2*30+2*45", "Se multiplican los residentes de cada grupo por sus minutos y se suman.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma la carga de los cuatro técnicos?", "(3*20+3*30+2*45)+(3*20+2*30+2*45)+(3*20+3*30+2*45)+(3*20+2*30+2*45)", "Se suman las cargas de los cuatro técnicos.", " minutos"),
        ("abc", "{F} ¿Algún técnico supera el máximo de 240 minutos?", "No: la mayor carga es 240 minutos", "Sí: el técnico 1", "Sí: el técnico 3", "Las cargas son 240, 210, 240 y 210; ninguna supera el máximo."),
        ("=", "{F} ¿Cuántos minutos por debajo del máximo está el técnico 2?", "240-(3*20+2*30+2*45)", "Se resta la carga del técnico 2 del máximo.", " minutos"),
        ("abc", "{F} El técnico 1 tiene una carga igual al máximo y un residente está con fiebre y necesita más tiempo. ¿Qué corresponde?", "Avisar a la enfermera de inmediato para reorganizar o pedir apoyo", "Hacer menos de lo planificado en otros residentes sin avisar", "Seguir sin decir nada", "Si el tiempo no alcanza, se informa para reorganizar y no se improvisa."),
        ("abc", "{F} Un compañero dice que 45 minutos por residente con ayuda mayor son exactos y que no puede haber diferencias. ¿Qué corresponde responder?", "Que son estimaciones para organizar; el tiempo real varía según la persona", "Que tiene razón, porque están en la planilla", "Que son valores clínicos", "Las estimaciones sirven para planificar, no para medir con exactitud."),
        ("abc", "{F} El técnico 2 propone pasar uno de sus residentes con ayuda mayor al técnico 4. ¿Qué corresponde?", "Proponerlo a la enfermera y esperar su decisión", "Hacerlo, porque él conoce a los residentes", "Hacerlo, si el técnico 4 acepta", "La asignación la decide la enfermera."),
        ("=", "{F} Si el técnico 4 recibe un residente más con ayuda parcial, ¿cuántos minutos suma su carga?", "(3*20+2*30+2*45)+30", "Se suman 30 minutos a la carga del técnico 4.", " minutos"),
        ("abc", "{F} Con ese residente más, la carga del técnico 4 sería 240 minutos. ¿Se supera el máximo?", "No: queda justo en el máximo", "Sí: lo supera en 30", "Sí: lo supera en 10", "240 es igual al máximo, no lo supera."),
    ],
    ctx=("abc", "{F} Al terminar la ronda, un técnico se da cuenta de que no alcanzó a hacer los cuidados de una residente de ayuda mayor. ¿Qué hace?", "Lo informa de inmediato a la enfermera y lo registra con el motivo", "Lo anota como hecho", "Lo deja para el siguiente turno sin avisar", "Un cuidado pendiente se informa y se registra; anotarlo como hecho es falsear el registro."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cómo calculas la carga de un técnico?", "Residentes de cada grupo × minutos del grupo, y se suman", "Así se obtiene el tiempo total estimado."),
        ("¿Qué haces si la carga supera el máximo?", "Aviso a la enfermera para reorganizar", "El técnico no cambia la asignación por su cuenta."),
        ("¿Los minutos de la planilla son exactos?", "No, son estimaciones para organizar", "Cada persona y cada día es distinto."),
    ],
    op=("Planilla de ejemplo: «Máximo del servicio: 200 minutos por técnico. Tiempo por residente: 15 con poca ayuda, 25 con ayuda parcial, 40 con ayuda mayor. Técnico A: 4 poca ayuda, 2 parcial, 2 mayor. Técnico B: 3 poca ayuda, 3 parcial, 3 mayor». "
        "Calcula: la carga de cada técnico; si alguno supera el máximo y por cuántos minutos; y escribe qué informarías a la enfermera, sin proponer cambios por tu cuenta.",
        "Técnico A: 4×15 + 2×25 + 2×40 = 60 + 50 + 80 = 190, no supera el máximo (10 minutos por debajo). Técnico B: 3×15 + 3×25 + 3×40 = 45 + 75 + 120 = 240, supera el máximo en 40 minutos. Informaría a la enfermera: «El técnico B tiene 240 minutos estimados, 40 más que el máximo; consulto si se reorganiza o se pide apoyo».",
        ["calcula 190 y 240", "identifica que B supera por 40", "informa sin decidir cambios", "usa un aviso con datos"],
        ["hoja con dos cargas, una comparación y una frase de aviso"],
        ["calcular mal las cargas", "cambiar residentes por su cuenta", "no usar datos en el aviso"],
        "Pregunta: «¿tu aviso propone un cambio o consulta a la enfermera?». Debe consultar."),
    reinforce="Con 2 residentes de 20 minutos, 3 de 30 y 1 de 45, calcula la carga de un técnico.",
    extend="Explica con un ejemplo inventado por qué una carga excesiva puede afectar el trato a las personas.",
)

# ============================================================ OAM-06, clase 5
F = ("Ficha 5 (comparar alternativas, de ejemplo). Dos propuestas de horario de aseo para 30 residentes con 4 técnicos y 900 minutos de trabajo estimado en total. Propuesta A: todos los aseos entre las 07:00 y las 11:00. Propuesta B: aseos repartidos entre la mañana y la tarde, según las preferencias que cada persona declaró. "
     "Puntaje de 0 a 2 por criterio: A, respeto de preferencias 0, carga por técnico 1, privacidad 1, autonomía 1, confort ambiental 1; B, respeto de preferencias 2, carga por técnico 2, privacidad 2, autonomía 2, confort ambiental 1. "
     "Lista de verificación de calidad al terminar un cuidado (6 puntos): persona cómoda y bien acomodada; piel y ropa limpias y secas; ropa de cama ordenada; objetos personales y timbre a su alcance; registro del cuidado y de lo observado; aviso a la enfermera de cambios observados.")
build(
    O6, 5, F,
    use="Aprenderé a comparar horarios de cuidado con criterios, a elegir con justificación y a verificar la calidad de un cuidado con una lista antes de terminar.",
    prior=["Conozco el plan de cuidados, la pauta de acogida y la carga de trabajo.", "Sé sumar puntajes y dividir números enteros.", "Sé leer una lista de verificación."],
    explain=[
        "Para comparar dos propuestas de horario se les aplican los mismos criterios: el respeto de las preferencias, la carga por técnico, la privacidad, la autonomía y el confort ambiental. Se asigna un puntaje de 0 a 2 a cada criterio y se suman. Una propuesta con más puntos suele ser mejor, pero se revisa que ningún criterio de respeto a la persona quede en cero.",
        "Elegir un horario no termina el trabajo: al terminar cada cuidado se verifica con una lista que la persona esté cómoda, limpia y seca, que su cama esté ordenada, que tenga sus objetos y su timbre al alcance, que se haya registrado el cuidado y lo observado y que se haya avisado a la enfermera de cualquier cambio. La decisión final sobre el horario es de la enfermera, que considera la carga y la seguridad del servicio.",
        "Los puntajes son de ejemplo para practicar la comparación." + LIM,
    ],
    vocab=[("propuesta", "forma posible de organizar un horario"), ("criterio", "aspecto con que se compara una propuesta"), ("puntaje", "número que indica cuánto cumple un criterio"), ("lista de verificación de calidad", "puntos que se revisan al terminar un cuidado"), ("decisión final", "elección que hace la enfermera con los datos")],
    worked=[
        ("Sumar un puntaje", "Una propuesta de ejemplo tiene preferencias 2, carga 1, privacidad 2, autonomía 1 y confort 2. ¿Cuántos puntos suma?", ["Se suman los cinco puntajes.", "2 + 1 + 2 + 1 + 2 = 8."], "8 puntos"),
        ("Dividir una carga", "900 minutos de trabajo repartidos por igual entre 3 técnicos de ejemplo, ¿cuántos minutos le toca a cada uno?", ["Se divide el total entre los técnicos.", "900 ÷ 3 = 300."], "300 minutos")],
    mistakes=[("Elegir la propuesta con más puntaje aunque tenga 0 en respeto a las preferencias.", "El respeto a la persona es una condición, no un criterio más.", "Antes de sumar, revisa que ningún criterio de respeto esté en cero."),
              ("Marcar la lista de verificación sin mirar a la persona ni la cama.", "Una verificación sin observar no previene errores.", "Mira cada punto antes de marcar.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es una propuesta?", "Una forma posible de organizar algo, que se compara con otras", "La decisión final de la enfermera", "El horario de visitas", "Una propuesta es una alternativa que se evalúa con criterios."),
        ("=", "{F} ¿Cuántos puntos suma la propuesta A?", "0+1+1+1+1", "Se suman los cinco puntajes de la propuesta A.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la propuesta B?", "2+2+2+2+1", "Se suman los cinco puntajes de la propuesta B.", " puntos"),
        ("abc", "{F} ¿Cuál es la propuesta más conveniente según el puntaje?", "La propuesta B", "La propuesta A", "Ambas por igual", "La propuesta B suma más puntos y respeta las preferencias."),
        ("abc", "{F} ¿Por qué la propuesta A tiene un 0 en preferencias?", "Porque concentra los aseos en la mañana sin considerar lo que cada persona declaró", "Porque dura demasiado", "Porque necesita más técnicos", "Un horario único para todos no respeta las preferencias."),
        ("=", "{F} ¿Cuántos minutos le tocan a cada técnico si los 900 minutos se reparten por igual?", "900//4", "Se divide el total de minutos entre los 4 técnicos.", " minutos"),
        ("=", "{F} Si el máximo por técnico es 240 minutos, ¿cuántos minutos menos que el máximo tiene cada técnico con el reparto igual?", "240-900//4", "Se resta la carga por técnico del máximo.", " minutos"),
        ("abc", "{F} Al terminar el aseo de una residente, la técnica ve que su timbre quedó fuera de su alcance. ¿Qué corresponde?", "Dejarlo a su alcance antes de retirarse", "Retirarse y volver más tarde", "Pedirle que lo busque ella", "El timbre al alcance es parte de la verificación."),
        ("abc", "{F} Al verificar, la técnica nota que la ropa de cama de un residente quedó arrugada. ¿Qué corresponde?", "Ordenarla antes de retirarse, si le corresponde, o avisar", "Dejarla, porque es poco importante", "Marcar el punto como cumplido", "El ambiente ordenado forma parte del confort."),
        ("abc", "{F} Al terminar, un técnico se da cuenta de que la residente tiene una marca nueva en la espalda. ¿Qué hace?", "Anota lo observado, con lugar y hora, y avisa a la enfermera", "No dice nada, porque no es parte de su tarea", "Le pone una crema por su cuenta", "Cambios observados se informan; el técnico no trata por su cuenta."),
        ("abc", "{F} Un compañero dice: «Con la propuesta B hay más horarios diferentes, mejor hacemos todo por la mañana, que es más fácil». ¿Qué corresponde responder?", "Que la decisión es de la enfermera y que se consideran las preferencias de las personas", "Que tiene razón, porque es más fácil", "Que no se puede cambiar nada", "La facilidad del equipo no reemplaza el respeto de las preferencias."),
        ("=", "{F} Si 6 de los 30 residentes prefieren el aseo por la tarde, ¿cuántos prefieren la mañana (suponiendo que el resto elige la mañana)?", "30-6", "Se restan los que prefieren la tarde del total.", " residentes"),
        ("abc", "{F} La lista de verificación tiene 6 puntos y se cumplieron 5. ¿Qué corresponde?", "Revisar el punto que falta antes de retirarse y avisar a la enfermera si no puede resolverse", "Retirarse, porque casi está completo", "Marcar el punto como cumplido", "Un punto de la lista no cumplido se resuelve o se informa."),
    ],
    ctx=("abc", "{F} Una residente de ejemplo dice que prefiere que su aseo sea a las 17:00, pero la propuesta elegida por la enfermera lo programa a las 10:00. ¿Qué hace el técnico?", "Registra su preferencia, la comunica a la enfermera y mientras tanto cumple lo programado con respeto", "Cambia el horario por su cuenta", "Le dice que no se puede cambiar nunca", "Se informa la preferencia para que la enfermera decida; no se cambia el horario por cuenta propia."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cómo se elige entre dos propuestas?", "Se comparan con los mismos criterios y se suman los puntajes", "Se evita elegir por comodidad del equipo."),
        ("¿Qué verificas al terminar un cuidado?", "Que la persona esté cómoda y con su timbre al alcance", "Es parte de la lista de verificación."),
        ("¿Quién toma la decisión final del horario?", "La enfermera", "El técnico propone y entrega los datos."),
    ],
    op=("Propuestas de ejemplo: «P1, aseos solo por la mañana: preferencias 0, carga 1, privacidad 1, autonomía 1, confort 1. P2, aseos por la mañana y por la tarde según preferencias: preferencias 2, carga 2, privacidad 2, autonomía 2, confort 1». 24 residentes, 4 técnicos y 600 minutos de trabajo estimado en total. "
        "Calcula: los puntos de cada propuesta; los minutos por técnico con reparto igual; y escribe qué elegirías con una razón, tres puntos de la lista de verificación que revisarías al terminar un cuidado y a quién comunicarías tu propuesta.",
        "P1: 0+1+1+1+1 = 4 puntos. P2: 2+2+2+2+1 = 9 puntos. Minutos por técnico: 600 ÷ 4 = 150. Elegiría P2, porque respeta las preferencias y reparte mejor la carga. Puntos de verificación: persona cómoda y limpia, timbre y objetos al alcance, registro y aviso de cambios. Comunicaría la propuesta a la enfermera, que decide.",
        ["calcula 4 y 9 puntos", "calcula 150 minutos", "elige P2 con razón", "comunica la propuesta a la enfermera"],
        ["hoja con dos puntajes, un cálculo, una elección con razón, tres puntos y a quién se comunica"],
        ["elegir P1 por ser más simple", "sumar mal", "decidir sin la enfermera"],
        "Pregunta: «¿quién decide si se cambia el horario?». Debe responder la enfermera."),
    reinforce="Escribe seis puntos de una lista de verificación de calidad de un cuidado y marca cuáles revisarías primero.",
    extend="Explica con un ejemplo inventado por qué un horario flexible puede mejorar el ánimo de una persona mayor.",
)

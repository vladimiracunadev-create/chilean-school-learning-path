"""Atención de Enfermería, mención Enfermería (4.º medio TP): OAM-01 (acciones de apoyo al tratamiento y la rehabilitación: solo conceptos, documentos e identificación segura) y OAM-02 (monitoreo e información al personal de salud sobre pacientes críticos o con procedimientos invasivos: lectura de planillas y comunicación). Todo en papel: servicios, pacientes y cifras inventados y rotulados «de ejemplo»; sin técnicas clínicas ni procedimientos."""
from __future__ import annotations

from tp_enfe_common import LIM, build

O1 = "TP-ENFE-4-OAM-01"
O2 = "TP-ENFE-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (servicio de ejemplo, inventado). Servicio de medicina y cirugía de un hospital inventado, con 24 camas ocupadas y 8 técnicos en el turno. Cada paciente tiene en promedio 5 indicaciones por turno: controles, medicamentos, curaciones, muestras u otras tareas. "
     "Cada indicación la escribe el médico o la enfermera, con hora, y la realiza el personal autorizado y formado, según el protocolo y bajo supervisión. Se estima que cada indicación toma 10 minutos de trabajo. "
     "Regla del servicio: ante un cambio brusco, una alarma o una reacción adversa, se avisa de inmediato a la enfermera.")
build(
    O1, 1, F,
    use="Aprenderé qué es el apoyo al tratamiento y a la rehabilitación, qué tipos de pacientes se atienden, quién indica y quién realiza cada tarea y qué límites tiene el técnico en formación.",
    prior=["Conozco el trabajo del técnico en enfermería.", "Sé multiplicar y dividir números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería, mención Enfermería, el apoyo al tratamiento y a la rehabilitación son las acciones con que el equipo ayuda a que una persona cumpla su tratamiento y se recupere. Se atiende a pacientes pediátricos (niños) y adultos, ambulatorios (que vuelven a su casa el mismo día) y hospitalizados (que permanecen en el establecimiento). Las acciones pueden incluir controles de signos vitales, toma de muestras, medicamentos por distintas vías y curaciones básicas, siempre por indicación de un profesional.",
        "El médico o la enfermera escribe la indicación, con hora. La realiza el personal autorizado y formado, según el protocolo y bajo supervisión. Un técnico en formación aprende observando y colaborando en lo que le asignan, y no realiza por su cuenta ninguna tarea clínica. El técnico siempre verifica que la indicación y la persona coincidan, registra con hora y firma, y avisa de inmediato a la enfermera ante un cambio brusco, una alarma o una reacción adversa.",
        "Este cuaderno no enseña ninguna técnica ni procedimiento clínico: solo conceptos y lectura de documentos." + LIM,
    ],
    vocab=[("apoyo al tratamiento", "acciones con que el equipo ayuda a que la persona cumpla su tratamiento"), ("paciente ambulatorio", "persona que recibe atención y vuelve a su casa el mismo día"), ("paciente hospitalizado", "persona que permanece en el establecimiento por su tratamiento"), ("paciente pediátrico", "niño o niña"), ("indicación", "instrucción escrita de un profesional sobre una tarea, con hora"), ("protocolo", "reglas escritas que se siguen en un establecimiento")],
    worked=[
        ("Clasificar a un paciente", "Un adulto de ejemplo llega a un control por la mañana y se va a su casa a mediodía. ¿Es ambulatorio u hospitalizado?", ["Vuelve a su casa el mismo día.", "Es un paciente ambulatorio."], "Ambulatorio"),
        ("Contar indicaciones", "En otro servicio de ejemplo hay 10 pacientes con 4 indicaciones cada uno. ¿Cuántas indicaciones hay en el turno?", ["Se multiplican los pacientes por las indicaciones de cada uno.", "10 × 4 = 40."], "40 indicaciones")],
    mistakes=[("Hacer una tarea clínica «porque ya la vi hacer muchas veces».", "La tarea la hace personal autorizado y formado; ver no habilita.", "Observa, colabora en lo que te asignen y pregunta lo que no entiendas."),
              ("Cambiar la hora de una indicación porque «el paciente duerme».", "La hora la define el profesional; cambiarla puede afectar el tratamiento.", "Avisa a la enfermera y ella decide.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un paciente hospitalizado?", "Una persona que permanece en el establecimiento por su tratamiento", "Una persona que vuelve a su casa el mismo día", "Una persona que solo visita a otro paciente", "El paciente hospitalizado permanece en el establecimiento."),
        ("abc", "{F} ¿Quién escribe las indicaciones del servicio?", "El médico o la enfermera", "El técnico en formación", "Los familiares", "La ficha dice que las escribe el médico o la enfermera."),
        ("abc", "{F} ¿Quién realiza las tareas clínicas indicadas?", "El personal autorizado y formado, bajo supervisión", "Cualquier persona que esté en el servicio", "El paciente por sí mismo", "La ficha limita la realización al personal autorizado y formado."),
        ("=", "{F} ¿Cuántas indicaciones hay en el turno entre los 24 pacientes?", "24*5", "Se multiplican los pacientes por las indicaciones de cada uno.", " indicaciones"),
        ("=", "{F} Si las indicaciones se reparten por igual entre los 8 técnicos, ¿cuántas le tocan a cada uno?", "24*5//8", "Se dividen las indicaciones del turno entre los técnicos.", " indicaciones"),
        ("=", "{F} ¿Cuántos minutos de trabajo estimado suman las indicaciones de cada técnico con ese reparto?", "24*5//8*10", "Se multiplican las indicaciones de cada técnico por los minutos de cada una.", " minutos"),
        ("abc", "{F} Un técnico en formación ve que una enfermera prepara una tarea y le pide que mire para aprender. ¿Qué corresponde?", "Observar con respeto y preguntar después lo que no entienda", "Realizar la tarea mientras la enfermera se distrae", "Decirle cómo se hace mejor", "Un técnico en formación aprende observando; la tarea la hace el personal autorizado."),
        ("abc", "{F} Un paciente dice que siente un dolor muy fuerte y se pone pálido. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera o profesional responsable y a emergencias, y lo acompaña sin darle nada", "Le da un medicamento de la bodega", "Le dice que se calme y espere", "Un cambio brusco se avisa de inmediato; el técnico no trata por su cuenta."),
        ("abc", "{F} Una indicación dice «control a las 10:00» y a esa hora el técnico está con otro paciente. ¿Qué corresponde?", "Avisar a la enfermera para reorganizar y no dejarla sin hacer", "Anotarla como realizada", "Hacerla a las 12:00 sin avisar", "El retraso se informa para que se reorganice y no se falsea el registro."),
        ("abc", "{F} Una madre pregunta al técnico qué le indicaron a su hijo pediátrico. ¿Qué corresponde?", "Derivar su consulta a la enfermera o al médico", "Leerle la indicación, porque es su madre", "Decirle lo que cree que significa", "La información del tratamiento la entrega el profesional."),
        ("=", "{F} Si el servicio tuviera 6 técnicos en vez de 8, ¿cuántas indicaciones le tocarían a cada uno (con los mismos 24 pacientes)?", "24*5//6", "Se dividen las indicaciones del turno entre los 6 técnicos.", " indicaciones"),
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué debe verificar siempre el técnico antes de apoyar una tarea?", "Que la indicación y la persona coincidan", "Que el paciente le dé las gracias", "Que el turno termine temprano", "Verificar la coincidencia evita errores de persona."),
        ("abc", "{F} Un familiar le pide al técnico que le muestre la ficha clínica del paciente. ¿Qué corresponde?", "Derivar al familiar a la enfermera, porque la ficha es confidencial", "Mostrársela, porque es familia", "Mostrarle solo una parte", "El acceso a la ficha lo gestiona el profesional y la norma vigente."),
    ],
    ctx=("abc", "{F} A las 15:00, un paciente adulto hospitalizado se queja de mucha picazón en los brazos y le aparecen manchas en la piel después de recibir un medicamento por la tarde. El técnico en formación está solo en la sala. ¿Qué hace?", "Avisa de inmediato a la enfermera y a emergencias y acompaña al paciente sin darle nada", "Le pone una crema de la bodega", "Espera a que se pase", "Una posible reacción adversa se avisa de inmediato; el técnico no trata por su cuenta."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿quién indica un tratamiento?", "El médico o la enfermera", "Las tareas clínicas siempre tienen una indicación escrita."),
        ("¿Qué haces ante un cambio brusco de un paciente?", "Aviso de inmediato a la enfermera", "El técnico no decide ni trata por su cuenta."),
        ("¿Qué es un paciente ambulatorio?", "Quien vuelve a su casa el mismo día", "No permanece hospitalizado porque vuelve a su casa el mismo día."),
    ],
    op=("Caso de ejemplo: un servicio tiene 18 pacientes y cada uno tiene 4 indicaciones por turno; trabajan 6 técnicos y cada indicación toma 10 minutos. A las 11:00, una niña de ejemplo hospitalizada dice que tiene mucho mareo y se pone pálida. "
        "Calcula: cuántas indicaciones hay en el turno, cuántas le tocan a cada técnico y cuántos minutos de trabajo estimado son. Escribe qué haría el técnico en formación ante el mareo y una frase de registro con hora y hechos, sin diagnóstico.",
        "Indicaciones: 18 × 4 = 72; por técnico: 72 ÷ 6 = 12; minutos: 12 × 10 = 120. Ante el mareo: avisa de inmediato a la enfermera y acompaña a la niña sin darle nada ni actuar por su cuenta. Registro: «11:00, la paciente refiere mareo y se ve pálida; se avisó a la enfermera a las 11:01».",
        ["calcula 72, 12 y 120", "avisa de inmediato a la enfermera", "no trata ni da nada", "el registro no incluye diagnóstico"],
        ["hoja con tres cálculos, una conducta y una frase de registro"],
        ["tratar el mareo por cuenta propia", "escribir un diagnóstico", "no avisar de inmediato"],
        "Pregunta: «¿tu frase de registro dice qué observaste o qué piensas que tiene?». Si lo segundo, pídele reescribirla."),
    reinforce="Escribe la diferencia entre paciente ambulatorio y hospitalizado y quién escribe una indicación.",
    extend="Explica con un ejemplo inventado por qué un técnico en formación aprende observando antes de colaborar en una tarea.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (documentos de ejemplo). Orden de examen de ejemplo: paciente «Camila Soto de Ejemplo», ficha 4501, solicitud de un examen de sangre de ejemplo, indicada por el médico el 5 de marzo a las 08:00. "
     "Rótulo de muestra, datos obligatorios (seis): nombre completo del paciente; número de ficha; tipo de muestra; fecha; hora; firma de quien la tomó. "
     "Vías de administración de medicamentos (solo vocabulario): oral, intramuscular (en el músculo), endovenosa (en una vena), sobre la piel y sobre mucosas. Curación: cuidado de una herida por personal formado, con material estéril. "
     "Hoja de enfermería: registra lo realizado y lo observado, con hora y firma.")
build(
    O1, 2, F,
    use="Aprenderé el vocabulario del apoyo al tratamiento: vías, muestras, curaciones y los documentos con que se identifican y registran, sin aprender ninguna técnica.",
    prior=["Sé qué es una indicación.", "Sé leer una ficha.", "Sé contar elementos de una lista."],
    explain=[
        "El tratamiento se apoya en tareas con nombres precisos. Una muestra es una pequeña cantidad de sangre u otro material del cuerpo que se envía a analizar. Se rotula con seis datos: nombre completo, número de ficha, tipo de muestra, fecha, hora y firma de quien la tomó; si falta uno, la muestra puede confundirse con la de otra persona. Las vías de administración son los caminos por los que se da un medicamento: oral, intramuscular, endovenosa, sobre la piel y sobre mucosas.",
        "Una curación es el cuidado de una herida; la hace personal formado, con material estéril. Los documentos principales son la orden de examen, la hoja de indicaciones y la hoja de enfermería, donde se registra lo realizado y lo observado con hora y firma. El rótulo y la orden deben coincidir con la persona: es la regla de identificación segura.",
        "En esta clase se aprenden palabras y documentos; ninguna técnica ni procedimiento." + LIM,
    ],
    vocab=[("muestra", "pequeña cantidad de sangre u otro material del cuerpo que se envía a analizar"), ("rótulo", "etiqueta con los datos que identifican una muestra"), ("orden de examen", "documento del médico que solicita un examen"), ("vía endovenosa", "camino de administración por una vena, hecho por personal formado"), ("curación", "cuidado de una herida, hecho por personal formado con material estéril"), ("hoja de enfermería", "documento donde se registra lo realizado y lo observado"), ("material estéril", "material sin microbios, con su envase intacto; si el envase está roto, no se usa")],
    worked=[
        ("Revisar un rótulo", "Un rótulo de ejemplo tiene nombre, número de ficha, tipo de muestra, fecha y hora, pero no firma. ¿Cuántos de los seis datos faltan?", ["Se piden seis datos.", "Falta uno: la firma."], "Falta 1 dato: la firma"),
        ("Identificar una vía", "Una indicación de ejemplo dice «vía oral». ¿Por dónde se da?", ["Oral significa por la boca.", "No es por inyección."], "Por la boca")],
    mistakes=[("Rotular una muestra con solo el nombre «porque no hay otro paciente igual».", "Puede haber personas con el mismo nombre; el número de ficha lo distingue.", "Completa siempre los seis datos del rótulo."),
              ("Confundir «intramuscular» con «endovenosa».", "El primero es en el músculo y el segundo en una vena; la vía la define la indicación.", "Lee la indicación y consulta si no estás seguro.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es una muestra?", "Una pequeña cantidad de sangre u otro material del cuerpo que se envía a analizar", "Un medicamento de prueba", "Una orden del médico", "Una muestra es material del cuerpo que se analiza."),
        ("abc", "{F} ¿Cuántos datos obligatorios tiene el rótulo de una muestra?", "Seis", "Cuatro", "Ocho", "La ficha enumera nombre, ficha, tipo de muestra, fecha, hora y firma."),
        ("abc", "{F} ¿Qué número de ficha tiene el paciente de la orden de examen?", "4501", "5403", "4051", "La ficha dice que el número es 4501."),
        ("abc", "{F} ¿Qué es una vía endovenosa?", "Un camino de administración por una vena", "Un camino de administración por la boca", "Un camino de administración sobre la piel", "Endovenosa significa que se da en una vena, por personal formado."),
        ("=", "{F} Si un rótulo tiene todos los datos menos el número de ficha y la hora, ¿cuántos de los 6 datos tiene?", "6-2", "Se restan de los seis datos los dos que faltan.", " datos"),
        ("=", "{F} Si un servicio rotula 8 muestras, ¿cuántos datos obligatorios se escriben en total?", "8*6", "Se multiplican las muestras por los seis datos del rótulo.", " datos"),
        ("abc", "{F} Un rótulo dice «Camila Soto» sin número de ficha. ¿Qué corresponde?", "No usarlo y consultar a la enfermera, porque falta un dato de identificación", "Usarlo, porque el nombre es suficiente", "Completar el dato por su cuenta", "Falta un dato de identificación segura; se consulta antes de continuar."),
        ("abc", "{F} Un compañero dice: «La hora de la muestra no es importante». ¿Qué corresponde responder?", "Que la hora es uno de los datos obligatorios y puede ser clave para el examen", "Que tiene razón, porque no cambia el resultado", "Que solo importa si el examen es urgente", "El rótulo completo es una regla de seguridad; la hora forma parte."),
        ("abc", "{F} Un paciente pregunta al técnico qué significa el resultado de su examen. ¿Qué corresponde?", "Decirle que el médico o la enfermera se lo explicará", "Interpretar el resultado, porque conoce el examen", "Decirle que está todo bien", "La interpretación de exámenes le corresponde al profesional."),
        ("abc", "{F} Un técnico escribe en la hoja de enfermería «el paciente estuvo bien». ¿Qué falta?", "Hechos observables con hora y firma", "Una opinión sobre el tratamiento", "Un diagnóstico", "La hoja registra hechos observables, con hora y firma."),
        ("abc", "{F} La curación de una herida requiere material estéril. ¿Qué haría el técnico en formación al ver que un paquete tiene el envase roto?", "No usarlo y avisar a la enfermera", "Usarlo con cuidado", "Taparlo con cinta", "El material estéril con envase roto pierde la esterilidad y no se usa."),
        ("=", "{F} Si cada muestra se rotula con 6 datos y hay 5 muestras, ¿cuántos datos faltan si se completaron 26?", "5*6-26", "Se calculan los datos totales y se restan los completados.", " datos"),
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿para qué sirve el número de ficha?", "Para distinguir a personas con el mismo nombre", "Para saber la edad del paciente", "Para indicar el tratamiento", "El número de ficha identifica de forma única a la persona."),
    ],
    ctx=("abc", "{F} Un técnico en formación nota que la orden de examen dice «Camila Soto, ficha 4501» y la pulsera del paciente que está por examinarse dice «Camila Soto, ficha 4510». ¿Qué hace?", "No continúa, avisa de inmediato a la enfermera y espera su indicación", "Continúa, porque el nombre coincide", "Cambia el número de ficha de la orden", "Un número distinto puede ser otra persona; se verifica antes de continuar."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cuántos datos tiene el rótulo de una muestra?", "Seis", "Nombre, ficha, tipo, fecha, hora y firma."),
        ("¿Qué haces si falta un dato en un rótulo?", "No uso el rótulo y consulto a la enfermera", "Un dato faltante puede confundir a dos pacientes."),
        ("¿Quién interpreta un examen?", "El profesional", "El técnico no interpreta resultados: eso lo hace el profesional."),
    ],
    op=("Documentos de ejemplo: «Orden: paciente Lucas Rojas de Ejemplo, ficha 3002, examen de sangre de ejemplo, solicitada el 12 de abril a las 09:00. Rótulo A: Lucas Rojas, 3002, sangre, 12 de abril, 09:10, firma presente. Rótulo B: Lucas Rojas, sangre, 12 de abril, sin hora ni firma». "
        "Escribe: cuántos de los seis datos tiene cada rótulo; cuál se puede usar y por qué; qué harías con el otro; y qué documento usarías para registrar lo realizado.",
        "Rótulo A tiene los seis datos; rótulo B tiene tres (nombre, tipo de muestra y fecha) y le faltan tres: ficha, hora y firma. A se puede usar porque está completo y coincide con la orden. B no se usa: se avisa a la enfermera. Para registrar lo realizado: la hoja de enfermería.",
        ["cuenta seis y tres datos en los rótulos", "elige A con razón", "no usa B y avisa", "nombra la hoja de enfermería"],
        ["hoja con dos conteos, una elección, una conducta y un documento"],
        ["usar el rótulo incompleto", "completar los datos por su cuenta", "no avisar a la enfermera"],
        "Pregunta: «¿cuántos datos le faltan al rótulo B?». Debe responder tres: ficha, hora y firma."),
    reinforce="Escribe los seis datos de un rótulo y tres vías de administración con su significado.",
    extend="Explica con un ejemplo inventado por qué dos pacientes con el mismo nombre pueden confundirse si el rótulo está incompleto.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (identificación segura, de ejemplo). Pauta de cinco puntos: (1) usar dos datos de identificación, nombre completo y número de ficha; (2) comprobar que la orden, la pulsera y el rótulo coincidan; (3) registrar fecha y hora; (4) respetar la respuesta de la persona o de su representante y verificar su consentimiento cuando corresponde; (5) registrar lo que ocurrió y avisar de lo que no coincide. "
     "Caso A: el técnico revisa nombre y ficha en la orden, la pulsera y el rótulo, todo coincide, anota fecha y hora, el paciente acepta y registra; cumple los cinco. Caso B: el rótulo dice «Marta Pérez» y la orden dice «Marta Pérez Soto»; el técnico continúa sin consultar y no avisa; cumple los puntos 3 y 4. "
     "Caso C: el paciente dice que no quiere el examen; el técnico respeta su respuesta, lo registra y avisa a la enfermera; cumple los cinco. Caso D: el técnico comprueba solo el nombre y no el número de ficha; anota fecha y hora y registra; cumple los puntos 2, 3, 4 y 5.")
build(
    O1, 3, F,
    use="Aprenderé a analizar casos de identificación segura con una pauta, a reconocer el punto que falló y a decidir qué se informa y a quién.",
    prior=["Conozco el rótulo de una muestra y los documentos.", "Sé calcular porcentajes de números enteros.", "Conozco la regla de avisar lo que no coincide."],
    explain=[
        "La identificación segura es la regla de comprobar que la persona, los documentos y las muestras corresponden a una misma persona. La pauta tiene cinco puntos: usar dos datos de identificación, comprobar que orden, pulsera y rótulo coincidan, registrar fecha y hora, respetar la respuesta de la persona y registrar lo que ocurrió avisando lo que no coincide. Un error de identificación puede llevar a dar un tratamiento a quien no corresponde.",
        "Para analizar un caso se revisa cada punto y se marca si se cumplió. Cuando algo no coincide, por ejemplo un apellido distinto, no se continúa ni se corrige por cuenta propia: se avisa a la enfermera. La persona, o su representante cuando es menor de edad o no puede decidir, puede aceptar o rechazar una tarea; el rechazo se respeta, se registra y se informa.",
        "Esta clase no enseña a realizar ninguna tarea: solo a revisar la identificación y el registro." + LIM,
    ],
    vocab=[("identificación segura", "regla de comprobar que persona, documentos y muestras corresponden a la misma persona"), ("pulsera de identificación", "pulsera con los datos de la persona"), ("representante", "persona que decide por quien no puede hacerlo o es menor de edad"), ("coincidir", "ser iguales en todos los datos"), ("discrepancia", "diferencia entre dos datos que deberían ser iguales")],
    worked=[
        ("Detectar una discrepancia", "En un caso de ejemplo, la orden dice «Pablo Díaz, ficha 7801» y la pulsera dice «Pablo Díaz, ficha 7810». ¿Qué corresponde?", ["El número de ficha no coincide.", "No se continúa y se avisa a la enfermera."], "No continuar y avisar a la enfermera"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 4 de los 5 puntos de la pauta. ¿Qué porcentaje es?", ["4 × 100 = 400.", "400 ÷ 5 = 80."], "80 %")],
    mistakes=[("Corregir con lápiz el apellido de un rótulo que no coincide con la orden.", "Se puede asignar la muestra a otra persona sin darse cuenta.", "No corrijas por tu cuenta: avisa a la enfermera."),
              ("Verificar solo el nombre porque «es una persona conocida».", "El conocimiento personal no reemplaza los dos datos de identificación.", "Usa siempre nombre y número de ficha.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es la identificación segura?", "La regla de comprobar que persona, documentos y muestras corresponden a la misma persona", "El registro de la hora de ingreso", "La firma del médico", "La identificación segura evita errores de persona."),
        ("abc", "{F} ¿Qué punto incumple el técnico del caso B?", "El punto 2: comprobar que orden, pulsera y rótulo coincidan", "El punto 3: registrar fecha y hora", "El punto 4: respetar la respuesta de la persona", "El apellido del rótulo no coincide con el de la orden."),
        ("abc", "{F} ¿Qué punto incumple el técnico del caso D?", "El punto 1: usar dos datos de identificación", "El punto 5: registrar", "El punto 3: fecha y hora", "Usó solo el nombre y no el número de ficha."),
        ("abc", "{F} ¿Qué casos cumplen los cinco puntos?", "Los casos A y C", "Los casos B y D", "Solo el caso B", "La ficha dice que A y C cumplen los cinco puntos."),
        ("=", "{F} ¿Cuántos puntos cumplen en total los cuatro casos?", "5+2+5+4", "Se suman los puntos cumplidos por cada caso.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del total (4 casos de 5 puntos) se cumplió?", "(5+2+5+4)*100//(4*5)", "Se multiplica el total cumplido por 100 y se divide entre los puntos evaluados.", " %"),
        ("=", "{F} ¿Cuántos puntos incumplen entre los casos B y D?", "(5-2)+(5-4)", "Se restan los puntos cumplidos de los 5 de cada caso y se suman las fallas.", " puntos"),
        ("abc", "{F} En el caso B, ¿qué debió hacer el técnico al ver la diferencia de apellido?", "No continuar y avisar a la enfermera para verificar la identidad", "Corregir el rótulo con lápiz", "Continuar y ver después", "Una discrepancia se informa antes de continuar."),
        ("abc", "{F} En el caso C, el paciente no quiere el examen. ¿Qué hace bien el técnico?", "Respeta su respuesta, la registra y avisa a la enfermera", "Insiste hasta que acepta", "Le dice que es obligatorio", "El rechazo se respeta, se registra y se informa."),
        ("abc", "{F} Un compañero dice que en el caso D «no pasó nada, porque era la persona correcta». ¿Qué corresponde responder?", "Que el resultado correcto no justifica un método incorrecto; igual se necesitan dos datos de identificación", "Que tiene razón", "Que solo importa el resultado", "Una identificación incompleta puede fallar en otra ocasión."),
        ("abc", "{F} El paciente del caso A es un niño de ejemplo. ¿Quién debe aceptar o rechazar la tarea?", "Su representante, con respeto a la opinión del niño según su edad", "Cualquier adulto presente", "Nadie, porque es un niño", "Un menor es representado por un adulto responsable."),
        ("=", "{F} Si el técnico del caso B hubiera cumplido también el punto 2, ¿cuántos puntos habría cumplido?", "2+1", "Se suma el punto 2 a los dos que ya cumplía.", " puntos"),
        ("abc", "{F} Una discrepancia de datos aparece al final del turno, con la muestra ya en camino. ¿Qué corresponde?", "Avisar de inmediato a la enfermera para detener o revisar la muestra", "Callar, porque ya no se puede hacer nada", "Esperar al turno siguiente", "Un error detectado se avisa de inmediato para evitar daños."),
    ],
    ctx=("abc", "{F} El técnico en formación ve que la pulsera de un paciente dice «Ana Torres» y que en la hoja de indicaciones dice «Ana Torrez». Piensa que es un error de escritura. ¿Qué hace?", "Avisa a la enfermera para verificar la identidad antes de seguir", "Supone que es la misma persona", "Corrige la hoja", "No se asume que son la misma persona: se verifica con quien corresponde."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cuántos datos usas para identificar a una persona?", "Al menos dos: nombre completo y número de ficha", "Un solo dato puede confundir a dos personas."),
        ("¿Qué haces si dos datos no coinciden?", "No continúo y aviso a la enfermera", "No se corrige por cuenta propia."),
        ("¿Se puede obligar a un paciente a aceptar una tarea?", "No, se respeta su respuesta y se informa", "El rechazo se registra y lo evalúa la enfermera."),
    ],
    op=("Casos de ejemplo: «A: la pulsera dice Eva Muñoz, ficha 2203; la orden dice Eva Muñoz, ficha 2203; el rótulo, Eva Muñoz, ficha 2230, y el técnico sigue adelante sin consultar. B: la técnica revisa solo el nombre en voz alta y dice «¿usted es Eva?»; la paciente, adormecida, responde «sí»; no revisa nada más, pero anota la fecha y la hora, respeta la respuesta de la paciente y registra lo ocurrido». "
        "Usa la pauta de la ficha. Escribe: qué puntos incumple cada caso; cuántos puntos cumplen A y B si cada caso cumple los puntos que no aparecen como falla (A cumple 4 y B cumple 3); y cómo corregirías cada caso.",
        "A incumple el punto 2 (el rótulo tiene ficha 2230 y no 2203): no se continúa y se avisa a la enfermera. B incumple el punto 1 (un solo dato, y preguntado a una persona adormecida) y el punto 2 (no compara pulsera, orden y rótulo): verifica con nombre y número de ficha en pulsera, orden y rótulo. Cumplen 4 + 3 = 7 de 10. Corrección: usar dos datos y avisar ante discrepancias.",
        ["identifica la discrepancia del número de ficha", "identifica el punto 1 incumplido en B", "calcula 7 de 10", "propone correcciones"],
        ["hoja con puntos incumplidos, un total y correcciones"],
        ["corregir el rótulo por su cuenta", "aceptar la respuesta de una persona adormecida como identificación", "sumar mal"],
        "Pregunta: «¿basta preguntar al paciente si es quien dice la orden?». Debe responder que no."),
    reinforce="Escribe los cinco puntos de la pauta con tus palabras y un ejemplo de una discrepancia que obligue a avisar.",
    extend="Explica con un ejemplo inventado por qué preguntar solo el nombre en voz alta no es suficiente para identificar a una persona.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (planilla del turno, de ejemplo). Servicio de 24 pacientes. Indicaciones programadas en el turno: 120. Realizadas a la hora indicada: 108. Realizadas con atraso: 8. Pendientes: 4, con motivo registrado. "
     "Meta del servicio (de ejemplo): al menos 90 % de las indicaciones a la hora indicada. Muestras del turno: 20, de las cuales 18 se rotularon correctamente y 2 tuvieron un dato faltante y se informaron. "
     "Regla: un atraso o un pendiente se registra con su motivo y se informa a la enfermera; no se anota como realizado.")
build(
    O1, 4, F,
    use="Aprenderé a calcular el cumplimiento de las indicaciones de un turno y la calidad del rotulado con enteros, a compararlos con una meta y a informar con datos.",
    prior=["Sé calcular porcentajes de números enteros.", "Conozco la identificación segura y el rótulo.", "Sé leer una planilla."],
    explain=[
        "La planilla del turno resume cuánto se hizo de lo indicado. El cumplimiento a la hora indicada es las indicaciones realizadas a tiempo, multiplicadas por 100 y divididas por las programadas. Un atraso es una indicación realizada fuera de hora y un pendiente es una que no se realizó. Ambos se registran con su motivo y se informan a la enfermera; nunca se anotan como realizados a tiempo.",
        "También se calcula la calidad del rotulado: las muestras rotuladas correctamente sobre el total de muestras, en porcentaje. Un dato faltante en un rótulo se informa para corregir con la persona que lo hizo, sin buscar culpables. Los porcentajes se comparan con la meta del servicio y sirven para organizar mejor el trabajo.",
        "Los datos de esta clase son inventados y la meta es de ejemplo." + LIM,
    ],
    vocab=[("cumplimiento a la hora indicada", "indicaciones realizadas a tiempo respecto de las programadas, en porcentaje"), ("atraso", "indicación realizada fuera de la hora indicada"), ("pendiente", "indicación que no se realizó"), ("meta", "porcentaje que el servicio se propone alcanzar"), ("rotulado correcto", "muestra con los seis datos del rótulo completos")],
    worked=[
        ("Calcular el cumplimiento", "En otro turno de ejemplo se programaron 50 indicaciones y 40 se realizaron a la hora indicada. ¿Qué porcentaje es?", ["40 × 100 = 4.000.", "4.000 ÷ 50 = 80."], "80 %"),
        ("Contar los no realizados a tiempo", "En otro turno de ejemplo hubo 30 indicaciones, 24 a la hora indicada y 4 con atraso. ¿Cuántas quedaron pendientes?", ["24 + 4 = 28 realizadas.", "30 − 28 = 2 pendientes."], "2 pendientes")],
    mistakes=[("Anotar «hecho a la hora» una indicación realizada con atraso para que la planilla se vea mejor.", "Falsea el registro y no deja ver qué se debe mejorar.", "Anótala como atraso con el motivo e infórmala."),
              ("Descartar un rótulo con dato faltante sin avisar.", "El problema no se corrige y puede repetirse.", "Informa la falla a la enfermera para corregir el proceso.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un atraso?", "Una indicación realizada fuera de la hora indicada", "Una indicación que no se realizó", "Una indicación nueva", "El atraso es una indicación hecha fuera de hora."),
        ("=", "{F} ¿Qué porcentaje de las indicaciones se realizó a la hora indicada?", "108*100//120", "Se multiplican las realizadas a tiempo por 100 y se dividen entre las programadas.", " %"),
        ("abc", "{F} ¿Se alcanzó la meta del servicio?", "Sí: 90 % alcanza la meta de al menos 90 %", "No: faltan 2 puntos", "No: el servicio exige 100 %", "El cumplimiento de 90 % es igual a la meta."),
        ("=", "{F} ¿Cuántas indicaciones se realizaron en total, a tiempo o con atraso?", "108+8", "Se suman las realizadas a tiempo y las realizadas con atraso.", " indicaciones"),
        ("=", "{F} ¿Cuántas indicaciones no se realizaron a la hora indicada, entre atrasos y pendientes?", "8+4", "Se suman los atrasos y los pendientes.", " indicaciones"),
        ("=", "{F} ¿Qué porcentaje de las muestras se rotuló correctamente?", "18*100//20", "Se multiplican las muestras correctas por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Cuántos datos de rótulo se completaron en total, si cada muestra tiene 6 datos y las 2 muestras con falla tuvieron 1 dato faltante cada una?", "20*6-2", "Se calculan los datos de las 20 muestras y se restan los que faltaron.", " datos"),
        ("abc", "{F} ¿Cómo se debe anotar una indicación realizada con atraso?", "Como atraso, con su motivo, e informada a la enfermera", "Como realizada a tiempo", "No se anota", "La regla pide anotar el atraso con su motivo e informarlo."),
        ("abc", "{F} Un técnico dice que anotó «a tiempo» tres indicaciones que hizo con 20 minutos de atraso «porque casi estaban a tiempo». ¿Qué corresponde?", "Corregir con una línea, hora y firma, y avisar a la enfermera", "Dejarlo, porque la diferencia es pequeña", "Borrar las anotaciones", "Un dato falso se corrige con trazabilidad."),
        ("abc", "{F} Dos de las 20 muestras tuvieron un dato faltante. ¿Qué corresponde?", "Informar a la enfermera para corregir el proceso y evitar que se repita", "No decir nada, porque son pocas", "Culpar al técnico que las rotuló", "Un error se informa para mejorar, sin culpar."),
        ("=", "{F} Si el servicio hubiera tenido 12 indicaciones más a la hora indicada, ¿cuántas habrían sido a la hora indicada en total?", "108+12", "Se suman las indicaciones adicionales a las realizadas a tiempo.", " indicaciones"),
        ("abc", "{F} Las 4 pendientes tienen motivo registrado: dos por falta de insumos y dos porque el paciente estaba en examen. ¿Qué informa el técnico?", "Los motivos, con datos concretos, a la enfermera", "Solo que hubo pendientes", "Que el servicio es ineficiente", "El motivo permite que la enfermera tome decisiones."),
        ("abc", "{F} Un compañero propone no registrar los atrasos «para no tener problemas». ¿Qué corresponde responder?", "Que se registran siempre, porque sirven para mejorar y proteger a los pacientes", "Que sí, mientras no pase nada", "Que solo se registran los pendientes", "El registro fiel permite detectar causas y corregirlas."),
    ],
    ctx=("abc", "{F} Al cerrar el turno, la técnica en formación ve que una indicación aparece como «realizada» sin hora ni firma. No sabe quién la hizo. ¿Qué hace?", "Consulta a la enfermera y no completa el dato por suposición", "Pone su firma, porque estaba presente", "Pone una hora aproximada", "No se completa un dato ajeno por suposición."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cómo se calcula el cumplimiento a la hora indicada?", "Realizadas a tiempo × 100 ÷ programadas", "Se compara lo hecho a tiempo con lo programado."),
        ("¿Cómo se anota un pendiente?", "Con su motivo, e informado a la enfermera", "Un pendiente no se anota como realizado, sino con su motivo."),
        ("¿Qué porcentaje es 18 de 20 muestras?", "90 %", "18 × 100 ÷ 20 = 90."),
    ],
    op=("Planilla de ejemplo: «80 indicaciones programadas; 64 a la hora indicada; 12 con atraso; 4 pendientes con motivo. Meta: al menos 85 %. 25 muestras, 20 rotuladas correctamente». "
        "Calcula: el porcentaje a la hora indicada y si se alcanzó la meta; cuántas indicaciones no se realizaron a la hora; el porcentaje de muestras rotuladas correctamente. Escribe qué informarías a la enfermera.",
        "A la hora: 64×100÷80 = 80 %, no alcanza la meta de 85 %. No realizadas a la hora: 12+4 = 16. Rotulado correcto: 20×100÷25 = 80 %. Informaría a la enfermera: «80 % a la hora, 12 atrasos y 4 pendientes con motivo; 5 muestras con dato faltante».",
        ["calcula 80 % y la compara con la meta", "calcula 16", "calcula 80 % de rotulado", "informa con datos"],
        ["hoja con tres cálculos, una comparación y una frase de informe"],
        ["anotar atrasos como realizados", "calcular mal el porcentaje", "culpar a una persona"],
        "Pregunta: «¿tu informe dice cuántas muestras tuvieron falla?». Debe decir cinco."),
    reinforce="Con 50 indicaciones programadas y 40 realizadas a tiempo, calcula el cumplimiento y cuántas no se hicieron a tiempo.",
    extend="Explica con un ejemplo inventado por qué un registro fiel de atrasos ayuda a mejorar el servicio.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (comparar entregas de turno, de ejemplo). Lista de verificación de calidad de una entrega de turno, 8 puntos: (1) identificación de cada paciente con dos datos; (2) indicaciones realizadas con hora; (3) indicaciones pendientes con motivo; (4) cambios observados; (5) avisos ya realizados y a quién; (6) pacientes con riesgo especial informados; (7) sin opiniones ni diagnósticos; (8) firma de quien entrega y de quien recibe. "
     "Entrega A: contiene los puntos 1, 2, 3, 4, 5, 6, 7 y 8. Entrega B: dice «todo bien en general, el de la cama 3 estuvo raro y la señora de la 5 no quiso nada»; contiene solo el punto 8. "
     "Tiempo de entrega (de ejemplo): A, 15 minutos para 12 pacientes; B, 5 minutos para 12 pacientes.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos entregas de turno con una lista de verificación, a ver por qué una es más segura y a valorar el tiempo y la calidad juntos.",
    prior=["Conozco la identificación segura y la planilla del turno.", "Sé sumar puntos y calcular tiempos.", "Sé leer una lista de verificación."],
    explain=[
        "La entrega de turno es el momento en que quien termina informa a quien recibe cómo están los pacientes y qué quedó pendiente. Una buena entrega es completa y ordenada: identifica a cada paciente con dos datos, dice qué se realizó con hora, qué quedó pendiente con su motivo, qué cambios se observaron, qué avisos ya se hicieron, qué pacientes tienen un riesgo especial y quién firma. No incluye opiniones ni diagnósticos.",
        "Comparar dos entregas es aplicarles la misma lista y contar los puntos que cumple cada una. Una entrega más larga puede ser mejor si incluye lo necesario; una entrega muy corta ahorra tiempo pero puede dejar sin información importante a quien recibe, lo que es un riesgo para los pacientes. La calidad se verifica antes de dar por terminada la entrega, y las faltas se informan a la enfermera.",
        "Todos los datos son de ejemplo y el cuaderno no enseña ninguna tarea clínica." + LIM,
    ],
    vocab=[("entrega de turno", "informe que da quien termina el turno a quien lo recibe"), ("lista de verificación", "puntos que se revisan antes de dar por completa una entrega"), ("cambio observado", "hecho nuevo que se vio en el paciente durante el turno"), ("riesgo especial", "situación que requiere una vigilancia mayor, informada por la enfermera"), ("trazabilidad", "posibilidad de saber quién informó qué y cuándo")],
    worked=[
        ("Contar puntos cumplidos", "Una entrega de ejemplo cumple 6 de los 8 puntos. ¿Cuántos puntos le faltan?", ["8 − 6 = 2.", "Los dos puntos faltantes se completan antes de dar por terminada la entrega."], "2 puntos"),
        ("Calcular el tiempo por paciente", "En otra entrega de ejemplo se dedican 20 minutos para 10 pacientes. ¿Cuántos minutos corresponden a cada paciente?", ["Se divide el tiempo entre los pacientes.", "20 ÷ 10 = 2."], "2 minutos")],
    mistakes=[("Dar una entrega muy corta para terminar antes.", "Quien recibe puede quedar sin datos importantes y poner en riesgo a un paciente.", "Entrega todo lo necesario, de forma ordenada y con la lista de verificación."),
              ("Decir «estuvo raro» en la entrega.", "Es una opinión que no dice qué se observó.", "Describe el hecho: qué se vio, cuándo y cómo.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es la entrega de turno?", "El informe que da quien termina el turno a quien lo recibe", "La hora de salida del personal", "El registro de visitas", "La entrega de turno traspasa información sobre los pacientes."),
        ("abc", "{F} ¿Cuántos puntos tiene la lista de verificación de la entrega de turno?", "Ocho", "Seis", "Diez", "La ficha enumera ocho puntos de verificación."),
        ("abc", "{F} ¿Cuántos puntos cumple la entrega A?", "Los 8", "Solo 5", "Solo 3", "La ficha dice que la entrega A contiene los ocho puntos."),
        ("abc", "{F} ¿Qué punto cumple la entrega B?", "El punto 8: firma", "El punto 2: indicaciones con hora", "El punto 7: sin opiniones", "La ficha indica que B contiene solo el punto 8."),
        ("=", "{F} ¿Cuántos puntos de la lista incumple la entrega B?", "8-1", "Se resta el único punto cumplido del total de la lista.", " puntos"),
        ("=", "{F} ¿Cuántos segundos por paciente dedica la entrega A?", "15*60//12", "Se pasan los minutos a segundos y se dividen entre los pacientes.", " segundos"),
        ("=", "{F} ¿Cuántos minutos más que la entrega B dedica la entrega A?", "15-5", "Se restan los minutos de B de los de A.", " minutos"),
        ("abc", "{F} ¿Qué entrega es más segura para los pacientes?", "La entrega A, porque cumple todos los puntos", "La entrega B, porque es más corta", "Ambas por igual", "La entrega A da toda la información necesaria; B deja sin información importante."),
        ("abc", "{F} En la entrega B se dice «el de la cama 3 estuvo raro». ¿Qué punto incumple?", "El punto 7: sin opiniones, y el punto 4: cambios observados", "Solo el punto 8", "Ninguno", "«Raro» es una opinión y no describe qué se observó."),
        ("abc", "{F} Quien recibe la entrega B no entiende qué pasó con el paciente de la cama 3. ¿Qué corresponde?", "Pedir que le informen los hechos con detalle y avisar a la enfermera si no se aclara", "Suponer qué pasó", "Esperar a que el paciente lo cuente", "La información incompleta se aclara antes de recibir el turno."),
        ("abc", "{F} Un compañero dice que la entrega A es «demasiado larga y no vale la pena». ¿Qué corresponde responder?", "Que el tiempo de la entrega es parte de la seguridad de los pacientes", "Que tiene razón, porque hay mucho trabajo", "Que solo importa el tiempo", "La calidad de la entrega protege a los pacientes."),
        ("=", "{F} Si la entrega B se completara con los 7 puntos que le faltan y tomara 10 minutos más, ¿cuántos minutos duraría?", "5+10", "Se suman los minutos adicionales a los de la entrega B.", " minutos"),
        ("abc", "{F} En la entrega B se dice «la señora de la 5 no quiso nada». ¿Cómo se reescribe con un hecho?", "«La paciente de la cama 5 rechazó la bandeja de las 13:00 y dijo que no tenía hambre»", "«La paciente de la cama 5 es caprichosa»", "«La paciente de la cama 5 tiene un problema»", "Un hecho dice qué ocurrió, cuándo y qué dijo la persona."),
    ],
    ctx=("abc", "{F} Al recibir un turno, el técnico nota que quien entrega no menciona a un paciente que tiene un riesgo especial según la hoja de la enfermera. ¿Qué hace?", "Pregunta por ese paciente y avisa a la enfermera si no hay claridad", "Supone que no hay novedades", "Espera a que el paciente reclame", "Un dato omitido es un riesgo; se pregunta y se informa."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿qué debe incluir una buena entrega de turno?", "Identificación, indicaciones, pendientes, cambios, avisos y riesgos", "Es la información que necesita quien recibe."),
        ("¿Qué escribes en vez de «estuvo raro»?", "Un hecho: qué se observó, cuándo y cómo", "Los hechos permiten que otro entienda."),
        ("¿Quién firma la entrega?", "Quien entrega y quien recibe", "La firma da trazabilidad de quién informó y quién recibió."),
    ],
    op=("Entregas de ejemplo: «Entrega 1: 10 pacientes, 20 minutos; incluye identificación con dos datos, indicaciones con hora, pendientes con motivo, cambios observados con hechos, avisos y firma de ambos; sin opiniones. Entrega 2: 10 pacientes, 5 minutos; dice «cama 1 y 2 sin cambios, cama 3 mala, el resto igual»; solo tiene la firma de ambos». Usa la lista de ocho puntos de la ficha. "
        "Escribe: cuántos puntos cumple cada entrega (la 2 cumple 1 punto); los segundos por paciente de cada una; cuál es más segura y por qué; y cómo reescribirías «cama 3 mala».",
        "Entrega 1: 7 puntos (no menciona riesgo especial, el punto 6); entrega 2: 1 punto. Segundos por paciente: entrega 1, 20 × 60 ÷ 10 = 120; entrega 2, 5 × 60 ÷ 10 = 30. La entrega 1 es más segura porque da la información necesaria. «Cama 3 mala» se reescribe con hechos: «cama 3, a las 14:30 refirió dolor de cabeza y se avisó a la enfermera».",
        ["cuenta 7 y 1 puntos", "calcula 120 y 30 segundos", "elige la entrega 1 con razón", "reescribe con un hecho"],
        ["hoja con dos conteos, una elección con razón y una frase reescrita"],
        ["decir que la entrega más corta es mejor", "dejar la opinión en la entrega", "sumar mal"],
        "Pregunta: «¿tu frase reescrita dice qué ocurrió o solo cambia la palabra?». Si solo cambia la palabra, pídele agregar el hecho."),
    reinforce="Escribe los ocho puntos de la lista de la entrega de turno con tus palabras.",
    extend="Explica con un ejemplo inventado qué puede ocurrirle a un paciente si la entrega de turno omite información importante.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (unidad de ejemplo, inventada). Unidad de cuidados de mayor complejidad con 6 camas ocupadas, 3 enfermeras y 3 técnicos en un turno de 12 horas. Cada paciente tiene un monitor que muestra valores y suena una alarma cuando un valor sobrepasa los límites que programó la enfermera. "
     "Algunos pacientes tienen dispositivos, como una vía venosa o una sonda, que se mencionan solo por su nombre. Se anota en la hoja de monitoreo cada hora, con hora y firma; cada anotación toma 3 minutos de trabajo. "
     "Reglas: no se silencian ni se modifican alarmas ni equipos sin indicación; ante una alarma o un cambio, se avisa de inmediato a la enfermera; se informa con hechos y datos.")
build(
    O2, 1, F,
    use="Aprenderé qué es un paciente crítico, qué es monitorear, qué hacer ante una alarma y cómo se organiza el registro del monitoreo.",
    prior=["Conozco el apoyo al tratamiento.", "Sé multiplicar y dividir números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería, mención Enfermería, un paciente en condición crítica es una persona con riesgo vital que necesita una vigilancia continua. Un procedimiento invasivo es el que entra al cuerpo, por ejemplo una vía venosa o una sonda. Monitorear es observar de manera continua o frecuente el estado de la persona y sus valores, con la ayuda de equipos, y registrarlo en una hoja. El monitoreo sirve para detectar a tiempo cualquier cambio.",
        "Los equipos tienen alarmas. Una alarma es una señal que avisa que un valor sobrepasó el límite programado o que hay un problema. Los límites los programa la enfermera, y el técnico no los modifica ni silencia la alarma por cuenta propia. Ante una alarma o un cambio, el técnico avisa de inmediato a la enfermera, informa con hechos y datos y no toca los equipos ni los dispositivos del paciente.",
        "Este cuaderno no enseña a manejar monitores, sondas ni vías: solo enseña a leer los documentos y a comunicar con claridad." + LIM,
    ],
    vocab=[("paciente en condición crítica", "persona con riesgo vital que necesita vigilancia continua"), ("procedimiento invasivo", "procedimiento que entra al cuerpo, como una vía venosa"), ("monitoreo", "observación continua o frecuente del estado de la persona y de sus valores"), ("alarma", "señal del equipo que avisa que un valor superó el límite programado"), ("dispositivo", "elemento que se instala al paciente, como una sonda o una vía venosa"), ("hoja de monitoreo", "documento donde se registran los valores y las observaciones con hora y firma")],
    worked=[
        ("Reconocer una alarma", "Un monitor de ejemplo suena y el técnico ve que el valor sobrepasa el límite. ¿Qué hace?", ["La alarma es un aviso de que algo cambió.", "Avisa de inmediato a la enfermera y no la silencia."], "Avisar de inmediato a la enfermera, sin silenciar la alarma"),
        ("Registros por técnico", "En otra unidad de ejemplo hay 4 pacientes y 2 técnicos. Si se registra cada hora durante 6 horas, ¿cuántos registros hace cada técnico?", ["Cada técnico tiene 2 pacientes.", "2 pacientes × 6 registros = 12."], "12 registros")],
    mistakes=[("Silenciar una alarma «porque molesta a los otros pacientes».", "Se pierde el aviso de un posible peligro.", "Avisa de inmediato a la enfermera y no silencies sin indicación."),
              ("Cambiar el límite de la alarma para que no suene tanto.", "Los límites los define la enfermera; cambiarlos puede ocultar un cambio importante.", "Avisa a la enfermera y deja que ella decida.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un paciente en condición crítica?", "Una persona con riesgo vital que necesita vigilancia continua", "Una persona que vuelve a su casa el mismo día", "Una persona con una enfermedad leve", "La condición crítica implica riesgo vital y vigilancia continua."),
        ("abc", "{F} ¿Quién programa los límites de las alarmas?", "La enfermera", "El técnico", "La visita", "La ficha dice que los límites los programa la enfermera."),
        ("abc", "{F} Suena la alarma de la cama 3. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y no silencia ni modifica nada", "Silencia la alarma y espera a ver si se normaliza", "Cambia el límite de la alarma", "Ante una alarma se avisa de inmediato y no se toca el equipo."),
        ("=", "{F} ¿Cuántos pacientes tiene a su cargo cada técnico si se reparten por igual?", "6//3", "Se divide el total de pacientes entre los técnicos.", " pacientes"),
        ("=", "{F} ¿Cuántos registros hace cada técnico en el turno de 12 horas, con un registro por hora por paciente?", "6//3*12", "Se multiplican los pacientes de cada técnico por los registros del turno.", " registros"),
        ("=", "{F} ¿Cuántos registros se hacen en total en la unidad durante el turno?", "6*12", "Se multiplican los pacientes por los registros por paciente.", " registros"),
        ("=", "{F} ¿Cuántos minutos de trabajo suman los registros de cada técnico en el turno?", "6//3*12*3", "Se multiplican los registros de cada técnico por los minutos de cada uno.", " minutos"),
        ("abc", "{F} Un familiar pide al técnico que apague la alarma porque le molesta. ¿Qué corresponde?", "Explicar con respeto que las alarmas protegen al paciente y avisar a la enfermera", "Apagarla un momento mientras la enfermera no mira", "Decirle que no se meta", "Una alarma no se silencia por cuenta propia; se explica con respeto y se avisa."),
        ("abc", "{F} El técnico ve que un dispositivo del paciente de la cama 5 parece haberse movido de su lugar. ¿Qué hace?", "No lo toca y avisa de inmediato a la enfermera", "Lo vuelve a poner en su lugar", "Espera al siguiente registro", "Los dispositivos solo los maneja personal formado; el técnico avisa de inmediato."),
        ("abc", "{F} Un compañero silencia una alarma y no avisa. ¿Qué hace el técnico que lo ve?", "Le recuerda con respeto que debe avisar y, si es necesario, avisa a la enfermera", "No dice nada, para no incomodar", "Anota su nombre en la planilla para reprenderlo", "Silenciar sin avisar es un riesgo; se corrige con respeto y se informa si es necesario."),
        ("abc", "{F} Un paciente se queja de que le duele la zona donde tiene instalada una vía. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera con los hechos y no toca el dispositivo", "Le dice que se acostumbre", "Le saca el dispositivo", "El técnico no maneja dispositivos; observa, registra y avisa."),
        ("=", "{F} Si en el turno suenan 24 alarmas entre los 6 pacientes, ¿cuántas alarmas hay por hora, en promedio?", "24//12", "Se divide el total de alarmas entre las horas del turno.", " alarmas"),
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿para qué sirve la hoja de monitoreo?", "Para dejar un registro de valores y observaciones con hora y firma", "Para decidir el tratamiento", "Para reemplazar la alarma", "La hoja de monitoreo da trazabilidad y permite detectar cambios."),
    ],
    ctx=("abc", "{F} A las 03:00, suena la alarma de la cama 2 y el técnico ve que el valor del monitor es muy distinto al registrado a las 02:00. La enfermera está atendiendo en otra cama al otro extremo. ¿Qué hace?", "Avisa de inmediato a la enfermera, en voz alta o por el medio que indique el protocolo, y no toca nada", "Espera a que la enfermera termine", "Silencia la alarma para pensar", "Una alarma con un cambio importante se avisa de inmediato; no se toca el equipo."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿qué haces cuando suena una alarma?", "Aviso de inmediato a la enfermera", "No silencio ni modifico nada sin indicación."),
        ("¿Quién programa los límites de las alarmas?", "La enfermera", "El técnico no modifica los límites."),
        ("¿Qué es monitorear?", "Observar el estado de la persona de manera continua o frecuente y registrarlo", "Sirve para detectar cambios a tiempo."),
    ],
    op=("Caso de ejemplo: una unidad tiene 4 camas, 2 técnicos y un turno de 8 horas, con un registro por hora por paciente de 3 minutos cada uno. A las 14:00, suena la alarma de la cama 1 y un familiar pide que la silencien. "
        "Calcula: cuántos registros hace cada técnico y cuántos minutos suman. Escribe qué haría el técnico ante la alarma y ante el pedido del familiar, y una frase de registro con hora y hechos.",
        "Pacientes por técnico: 4 ÷ 2 = 2; registros: 2 × 8 = 16; minutos: 16 × 3 = 48. Ante la alarma: avisar de inmediato a la enfermera, sin silenciarla ni tocar el equipo. Ante el familiar: explicar con respeto que las alarmas protegen al paciente. Registro: «14:00, cama 1, suena la alarma; se avisó a la enfermera a las 14:01; un familiar pidió silenciarla y se le explicó que no se puede».",
        ["calcula 16 registros y 48 minutos", "avisa de inmediato", "explica con respeto al familiar", "el registro lleva hora y hechos"],
        ["hoja con dos cálculos, dos conductas y una frase de registro"],
        ["silenciar la alarma", "tocar el equipo", "escribir un diagnóstico"],
        "Pregunta: «¿tu respuesta ante la alarma dice qué hace el técnico con el equipo?». Debe decir que no lo toca y avisa."),
    reinforce="Escribe qué es una alarma, quién programa sus límites y qué hace el técnico cuando suena.",
    extend="Explica con un ejemplo inventado por qué silenciar una alarma sin avisar puede ser peligroso.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (balance hídrico y comunicación, de ejemplo; valores inventados que no sirven como referencia clínica). Balance hídrico de un paciente de ejemplo en cuatro períodos de 3 horas, en mililitros: ingresos (líquidos que recibe), 600, 700, 500 y 600; egresos (líquidos que elimina), 500, 600, 400 y 500. Balance = ingresos − egresos. "
     "Formato de comunicación en cuatro partes: situación (qué ocurre), antecedentes (desde cuándo y qué había antes), observación (valores y hechos) y petición (qué se solicita). "
     "Mensaje de ejemplo: «Cama 4, 10:15. La alarma de pulso suena desde hace 2 minutos. El monitor marca 118; a las 10:00 marcaba 90; el límite programado es 110. Pido que venga la enfermera».")
build(
    O2, 2, F,
    use="Aprenderé el balance hídrico como una cuenta de planilla y el formato de cuatro partes para comunicar con claridad lo que se observa al personal de salud.",
    prior=["Conozco el monitoreo y las alarmas.", "Sé sumar y restar números enteros.", "Sé leer una tabla."],
    explain=[
        "El balance hídrico es un registro de los líquidos que entran y salen del cuerpo de una persona en un período. Los ingresos son los líquidos que recibe y los egresos son los que elimina, y se miden en mililitros. El balance se calcula restando los egresos de los ingresos: si es positivo, entró más de lo que salió; si es negativo, salió más. Es solo una cuenta de planilla: el técnico la registra y la informa, pero no la interpreta.",
        "Para comunicar un cambio al personal de salud se usa un formato claro de cuatro partes: situación (qué ocurre), antecedentes (desde cuándo y qué había antes), observación (los valores y hechos) y petición (qué se solicita). Un mensaje con las cuatro partes ahorra tiempo y evita malentendidos. Se habla con calma, se dan datos y se pregunta si quedó claro.",
        "Los valores de esta clase son inventados y sirven solo para practicar el cálculo." + LIM,
    ],
    vocab=[("balance hídrico", "registro de líquidos que entran y salen del cuerpo en un período"), ("ingresos", "líquidos que la persona recibe, medidos en mililitros"), ("egresos", "líquidos que la persona elimina, medidos en mililitros"), ("mililitro (ml)", "unidad pequeña de volumen"), ("situación, antecedentes, observación y petición", "las cuatro partes de un mensaje claro"), ("límite programado", "valor fijado por la enfermera que activa la alarma")],
    worked=[
        ("Calcular un balance", "En un período de ejemplo, un paciente tuvo ingresos de 500 ml y egresos de 400 ml. ¿Cuál es el balance?", ["Balance = ingresos − egresos.", "500 − 400 = 100 ml."], "+100 ml"),
        ("Ubicar una parte del mensaje", "En un mensaje de ejemplo, el técnico dice: «Pido que venga la enfermera». ¿Qué parte del formato es?", ["Es lo que se solicita.", "Es la petición."], "La petición")],
    mistakes=[("Interpretar un balance diciendo «tiene un problema de líquidos».", "Es una interpretación clínica que le corresponde al profesional.", "Informa los datos: ingresos, egresos y balance."),
              ("Comunicar solo «está mal».", "No dice qué ocurre, desde cuándo ni qué se pide; la enfermera no puede decidir.", "Usa las cuatro partes: situación, antecedentes, observación y petición.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué son los ingresos en un balance hídrico?", "Los líquidos que la persona recibe", "Los líquidos que la persona elimina", "Las visitas que recibe", "Los ingresos son lo que entra; los egresos, lo que sale."),
        ("=", "{F} ¿Cuántos ml suman los ingresos de los cuatro períodos?", "600+700+500+600", "Se suman los ingresos de cada período.", " ml"),
        ("=", "{F} ¿Cuántos ml suman los egresos de los cuatro períodos?", "500+600+400+500", "Se suman los egresos de cada período.", " ml"),
        ("=", "{F} ¿Cuál es el balance total del paciente?", "(600+700+500+600)-(500+600+400+500)", "Se restan los egresos totales de los ingresos totales.", " ml"),
        ("=", "{F} ¿Cuál es el balance del segundo período?", "700-600", "Se restan los egresos de los ingresos del período.", " ml"),
        ("abc", "{F} ¿Cómo es el balance de cada uno de los cuatro períodos?", "Es de +100 ml en los cuatro períodos", "Es distinto en cada período", "Es negativo en el tercer período", "Al restar los egresos de los ingresos de cada período resulta +100 ml en los cuatro."),
        ("abc", "{F} ¿Cuál es la parte «situación» del mensaje de ejemplo?", "«La alarma de pulso suena desde hace 2 minutos»", "«Pido que venga la enfermera»", "«A las 10:00 marcaba 90»", "La situación dice qué ocurre: la alarma de pulso suena."),
        ("abc", "{F} ¿Cuál es la parte «petición» del mensaje de ejemplo?", "«Pido que venga la enfermera»", "«El monitor marca 118»", "«Cama 4, 10:15»", "La petición es lo que se solicita."),
        ("=", "{F} ¿Cuánto subió el valor del monitor entre las 10:00 y las 10:15?", "118-90", "Se resta el valor anterior del valor actual.", " unidades"),
        ("=", "{F} ¿Cuánto sobrepasa el límite programado el valor del monitor?", "118-110", "Se resta el límite programado del valor del monitor.", " unidades"),
        ("abc", "{F} Un técnico dice a la enfermera: «Cama 4, está mal». ¿Qué le falta al mensaje?", "Los antecedentes, la observación con datos y la petición", "Una opinión más larga", "Un diagnóstico", "Un mensaje claro tiene situación, antecedentes, observación y petición."),
        ("abc", "{F} Al comunicar el balance, el técnico dice: «el paciente tiene un problema de líquidos». ¿Qué corresponde?", "Decir solo los datos: ingresos, egresos y balance", "Dejar la frase, porque resume", "Agregar un diagnóstico", "La interpretación le corresponde al profesional."),
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿para qué se pregunta «¿quedó claro?» al terminar un mensaje?", "Para verificar que la otra persona entendió", "Para evitar que haga preguntas", "Para terminar rápido la conversación", "Verificar que lo entendieron evita malentendidos importantes."),
    ],
    ctx=("abc", "{F} A las 16:00, el técnico ve que el monitor de la cama 4 marca un valor distinto al de las 15:00 y la alarma suena. Tiene que informar a la enfermera que está a unos pasos. ¿Qué dice?", "«Cama 4, 16:00; suena la alarma de pulso desde hace un minuto; el monitor marca 118 y a las 15:00 marcaba 90; pido que venga»", "«Venga rápido, el de la cama 4 está mal»", "«Creo que el de la cama 4 tiene algo grave en el corazón»", "El mensaje con las cuatro partes da datos; no diagnostica."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cómo se calcula el balance hídrico?", "Ingresos menos egresos", "Es una resta de las cantidades de la planilla."),
        ("¿Cuáles son las cuatro partes de un mensaje claro?", "Situación, antecedentes, observación y petición", "Ordenan la información para el profesional."),
        ("¿Interpretas el balance ante la familia?", "No, solo informo los datos al profesional", "La interpretación la hace el profesional."),
    ],
    op=("Datos de ejemplo: «Balance de un paciente en tres períodos de 4 horas: ingresos, 800, 700 y 900 ml; egresos, 700, 800 y 600 ml. A las 20:30, cama 6: suena la alarma desde hace 3 minutos; el monitor marca 112; a las 20:00 marcaba 88; el límite programado es 105». "
        "Calcula: los ingresos totales, los egresos totales y el balance; el cambio del valor del monitor. Escribe el mensaje a la enfermera con las cuatro partes, sin diagnósticos.",
        "Ingresos: 2.400; egresos: 2.100; balance: +300 ml. Cambio: 112 − 88 = 24. Mensaje: «Situación: cama 6, 20:30, suena la alarma desde hace 3 minutos. Antecedentes: a las 20:00 marcaba 88. Observación: el monitor marca 112; el límite programado es 105. Petición: pido que venga la enfermera. ¿Quedó claro?».",
        ["calcula 2400, 2100 y +300", "calcula 24", "el mensaje tiene las cuatro partes", "no incluye diagnósticos"],
        ["hoja con cuatro cálculos y un mensaje de cuatro partes"],
        ["restar al revés", "interpretar el balance", "olvidar la petición"],
        "Pregunta: «¿tu mensaje incluye qué pides?». Si no, pídele agregar la petición."),
    reinforce="Escribe las cuatro partes de un mensaje claro y un ejemplo breve de cada una.",
    extend="Explica con un ejemplo inventado por qué dar datos concretos ayuda más a la enfermera que decir «está mal».",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (casos y pauta de monitoreo seguro, de ejemplo). Pauta de cinco puntos: (1) observa y registra a la hora indicada; (2) no silencia ni modifica alarmas ni equipos sin indicación; (3) avisa de inmediato de alarmas y cambios; (4) registra con hora y firma; (5) comunica con claridad y verifica que lo entendieron. "
     "Caso A: un técnico silencia una alarma, registra a la hora con firma y le dice a la enfermera «todo bien»; cumple los puntos 1 y 4. Caso B: suena una alarma, el técnico no toca nada, avisa de inmediato, registra con hora y firma, comunica con datos y pregunta si quedó claro; cumple los cinco. "
     "Caso C: a las 11:00 el valor del monitor no coincide con el de la hoja y el técnico lo anota sin avisar; cumple los puntos 1, 2 y 4. Caso D: el técnico ve enrojecimiento junto a un dispositivo, no lo toca, avisa de inmediato y registra; no pregunta si lo entendieron; cumple los puntos 1, 2, 3 y 4.")
build(
    O2, 3, F,
    use="Aprenderé a analizar casos de monitoreo con una pauta, a ver qué punto falló y a decidir qué corrección proponer y a quién avisar.",
    prior=["Conozco el monitoreo, las alarmas y el mensaje de cuatro partes.", "Sé calcular porcentajes de números enteros.", "Conozco la regla de avisar de inmediato."],
    explain=[
        "Para analizar un caso de monitoreo se compara con la pauta de cinco puntos: observar y registrar a la hora, no silenciar ni modificar equipos, avisar de inmediato, registrar con hora y firma y comunicar con claridad verificando que lo entendieron. Cada punto previene un error frecuente: dejar pasar un cambio, ocultar un riesgo, demorar un aviso, no dejar trazabilidad o dar un mensaje confuso.",
        "El error más grave es silenciar o ignorar una alarma. También es grave anotar un valor que no coincide sin avisar: puede haber un error en el equipo o en el registro, o un cambio real. Cuando algo no coincide, se avisa a la enfermera, que decide. El análisis posterior de un caso sirve para mejorar el proceso, no para culpar a una persona.",
        "Esta clase no enseña a manejar equipos: solo a registrar y comunicar con seguridad." + LIM,
    ],
    vocab=[("pauta de monitoreo seguro", "lista de conductas esperadas al monitorear a un paciente"), ("discrepancia", "diferencia entre dos datos que deberían coincidir"), ("silenciar una alarma", "apagar el aviso sonoro de un equipo, que solo se hace con indicación"), ("verificar la comprensión", "preguntar si el mensaje se entendió"), ("análisis del caso", "revisión posterior para mejorar el proceso")],
    worked=[
        ("Aplicar un punto", "Un técnico de ejemplo ve que una alarma se activa y espera cinco minutos para avisar. ¿Qué punto incumple?", ["Debe avisar de inmediato.", "Incumple el punto 3."], "El punto 3: avisar de inmediato"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 3 de los 5 puntos. ¿Qué porcentaje es?", ["3 × 100 = 300.", "300 ÷ 5 = 60."], "60 %")],
    mistakes=[("Anotar el valor de la hoja en vez del valor del monitor «para que coincida».", "Falsea el registro y puede ocultar un cambio.", "Anota el valor real y avisa a la enfermera de la discrepancia."),
              ("Decir «todo bien» cuando una alarma sonó y se silenció.", "Oculta un hecho importante.", "Informa la alarma, la hora y qué se observó.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es una discrepancia?", "Una diferencia entre dos datos que deberían coincidir", "Una orden del médico", "Una alarma del monitor", "La discrepancia se avisa a la enfermera."),
        ("abc", "{F} ¿Qué puntos incumple el técnico del caso A?", "Los puntos 2, 3 y 5", "Solo el punto 4", "Solo el punto 1", "Silenció la alarma, no avisó de inmediato y comunicó «todo bien» sin datos."),
        ("abc", "{F} ¿Qué punto incumple el técnico del caso C?", "El punto 3: avisar de inmediato de lo que no coincide", "El punto 1: registrar a la hora", "El punto 4: firma", "Anotó la discrepancia pero no avisó a la enfermera."),
        ("abc", "{F} ¿Qué punto incumple el técnico del caso D?", "El punto 5: verificar que lo entendieron", "El punto 2: no tocar equipos", "El punto 3: avisar de inmediato", "No preguntó si lo entendieron, que es el punto 5."),
        ("abc", "{F} ¿Qué caso cumple los cinco puntos?", "El caso B", "El caso A", "El caso C", "La ficha dice que el caso B cumple los cinco puntos."),
        ("=", "{F} ¿Cuántos puntos cumplen en total los cuatro casos?", "2+5+3+4", "Se suman los puntos cumplidos por cada caso.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del total (4 casos de 5 puntos) se cumplió?", "(2+5+3+4)*100//(4*5)", "Se multiplica el total cumplido por 100 y se divide entre los puntos evaluados.", " %"),
        ("=", "{F} ¿Cuántos puntos incumplen en total los casos A, C y D?", "(5-2)+(5-3)+(5-4)", "Se restan los puntos cumplidos de los 5 de cada caso y se suman las fallas.", " puntos"),
        ("abc", "{F} En el caso C, ¿qué debió hacer el técnico al ver que el valor del monitor no coincidía con la hoja?", "Anotar el valor real y avisar de inmediato a la enfermera", "Anotar el valor de la hoja", "Esperar a ver si se corrige solo", "La discrepancia se informa y el dato real se registra."),
        ("abc", "{F} En el caso D, ¿qué hace bien el técnico con el dispositivo?", "No lo toca y avisa de inmediato", "Lo ajusta con cuidado", "Lo cubre con cinta", "El dispositivo lo maneja personal formado; el técnico avisa."),
        ("abc", "{F} Una compañera dice que en el caso A «como no pasó nada, no importa». ¿Qué corresponde responder?", "Que silenciar una alarma sin avisar es un riesgo aunque no haya pasado nada", "Que tiene razón, porque no hubo daño", "Que solo importa si la enfermera se entera", "Un riesgo evitado por suerte sigue siendo un riesgo que se corrige."),
        ("=", "{F} Si el técnico del caso A hubiera cumplido también los puntos 3 y 5, ¿cuántos puntos habría cumplido?", "2+2", "Se suman los dos puntos corregidos a los dos que ya cumplía.", " puntos"),
        ("abc", "{F} Al analizar el caso A, la enfermera quiere culpar al técnico. ¿Qué corresponde?", "Revisar qué falló en el proceso y reforzar la capacitación, sin buscar culpables", "Sancionarlo de inmediato", "Ocultar el caso", "El análisis busca mejorar el proceso."),
    ],
    ctx=("abc", "{F} Una técnica en formación ve que un compañero escribió en la hoja un valor distinto al que muestra el monitor, y que ya está firmado. ¿Qué hace?", "Consulta a quien registró y avisa a la enfermera de la discrepancia", "Cambia el valor por el del monitor", "No dice nada, porque está firmado", "Una discrepancia se informa; no se corrige un dato ajeno por cuenta propia."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿puedo silenciar una alarma?", "No, aviso de inmediato a la enfermera", "Silenciar solo se hace con indicación."),
        ("¿Qué haces si un valor no coincide con la hoja?", "Anoto el valor real y aviso a la enfermera", "No se ajusta el dato para que coincida."),
        ("¿Cuántos puntos tiene la pauta de la ficha?", "5", "Observar, no tocar, avisar, registrar y comunicar."),
    ],
    op=("Casos de ejemplo: «A: suena una alarma; el técnico avisa de inmediato, no toca el equipo, registra con hora y firma y comunica con datos. B: el técnico ve que el monitor marca 20 unidades más de lo anotado en la hoja a la misma hora; anota su propio valor con hora y firma, pero no dice nada a nadie. C: suena una alarma y el técnico la silencia y, diez minutos después, avisa a la enfermera con un «venga, está mal»; no anota nada en la hoja». "
        "Usa la pauta de la ficha. Escribe: qué puntos incumple cada caso; cuántos puntos se cumplen en total si A cumple 5, B cumple 3 y C cumple 1; y cómo corregirías B y C.",
        "A cumple los cinco. B incumple el punto 3 (no avisa) y el 5 (no comunica). C incumple el 2 (silencia), el 3 (aviso tardío), el 4 y el 5. Total: 5+3+1 = 9 de 15. Corrección: en B, anotar el valor real y avisar de inmediato; en C, avisar de inmediato sin silenciar y registrar con hora y firma.",
        ["identifica puntos incumplidos en B y C", "calcula 9 de 15", "propone correcciones concretas", "no enseña manejo de equipos"],
        ["hoja con puntos incumplidos, un total y correcciones"],
        ["justificar silenciar la alarma", "no avisar la discrepancia", "sumar mal"],
        "Pregunta: «¿cuándo se avisa de una alarma?». Debe responder de inmediato."),
    reinforce="Escribe los cinco puntos de la pauta con tus palabras y una conducta que incumpla cada uno.",
    extend="Explica con un ejemplo inventado por qué anotar un valor distinto del real puede ser peligroso.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (planilla de monitoreo de 24 horas, de ejemplo; valores inventados que no sirven como referencia clínica). Paciente de ejemplo, cama 2. Ingresos de líquidos por turno, en ml: mañana 900, tarde 800, noche 700. Egresos por turno, en ml: mañana 700, tarde 900, noche 600. "
     "Alarmas registradas por turno: mañana 6, tarde 3, noche 9. Registros de monitoreo programados: uno por hora, 24 en el día; se realizaron 22 y 2 se omitieron con motivo registrado (paciente en traslado). "
     "Regla de la hoja (de ejemplo): avisar a la enfermera si el balance de un turno es mayor que +300 o menor que −300 ml, y ante toda alarma.")
build(
    O2, 4, F,
    use="Aprenderé a calcular balances por turno y totales, el promedio de alarmas y los registros omitidos con enteros, y a aplicar la regla de la hoja sin interpretar.",
    prior=["Conozco el balance hídrico y la hoja de monitoreo.", "Sé sumar, restar y dividir números enteros.", "Sé aplicar una regla de aviso."],
    explain=[
        "En una planilla de 24 horas se calcula el balance de cada turno restando los egresos de los ingresos, y el balance total sumando los de los turnos. El promedio de alarmas por turno se calcula dividiendo el total de alarmas entre la cantidad de turnos. Los registros omitidos son los programados que no se hicieron: se restan los realizados de los programados, y cada uno se anota con su motivo.",
        "La regla de la hoja dice cuándo avisar: si el balance de un turno supera el valor que escribió la enfermera, o ante toda alarma. El técnico aplica la regla, informa los datos con claridad y no interpreta lo que significan. Si un registro se omitió, se informa el motivo, y no se anota como hecho.",
        "Los valores son de ejemplo y no son referencias clínicas." + LIM,
    ],
    vocab=[("balance por turno", "ingresos menos egresos de un turno"), ("balance total", "suma de los balances de los turnos"), ("promedio de alarmas", "total de alarmas dividido por la cantidad de turnos"), ("registro omitido", "registro programado que no se hizo"), ("regla de la hoja", "criterio escrito por la enfermera que dice cuándo avisar")],
    worked=[
        ("Balance de un turno", "En un turno de ejemplo, los ingresos fueron 600 ml y los egresos 750 ml. ¿Cuál es el balance?", ["Balance = ingresos − egresos.", "600 − 750 = −150 ml."], "−150 ml"),
        ("Registros omitidos", "En un día de ejemplo se programaron 12 registros y se realizaron 10. ¿Cuántos se omitieron?", ["Se restan los realizados de los programados.", "12 − 10 = 2."], "2 registros")],
    mistakes=[("Anotar «hecho» un registro omitido porque «seguro estaba todo igual».", "Falsea el registro y deja un hueco en la vigilancia.", "Anótalo como omitido, con su motivo, e infórmalo."),
              ("Decir que un balance negativo significa que el paciente «está mal».", "Es una interpretación que no le corresponde al técnico.", "Informa el balance y la regla de la hoja; el profesional interpreta.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un registro omitido?", "Un registro programado que no se hizo", "Un registro hecho con atraso", "Un registro duplicado", "Un registro omitido es un registro programado que no se realizó."),
        ("=", "{F} ¿Cuál fue el balance del turno de la mañana?", "900-700", "Se restan los egresos de los ingresos del turno.", " ml"),
        ("=", "{F} ¿Cuál fue el balance del turno de la tarde?", "800-900", "Se restan los egresos de los ingresos del turno.", " ml"),
        ("=", "{F} ¿Cuál fue el balance del turno de la noche?", "700-600", "Se restan los egresos de los ingresos del turno.", " ml"),
        ("=", "{F} ¿Cuál fue el balance total del día?", "(900+800+700)-(700+900+600)", "Se restan los egresos totales de los ingresos totales.", " ml"),
        ("abc", "{F} ¿Algún turno supera la regla de avisar por balance (más de +300 o menos de −300 ml)?", "No: los tres balances están entre −300 y +300", "Sí: el turno de la tarde", "Sí: el turno de la mañana", "Los balances son +200, −100 y +100 ml; ninguno supera el límite."),
        ("=", "{F} ¿Cuántas alarmas hubo en total en el día?", "6+3+9", "Se suman las alarmas de los tres turnos.", " alarmas"),
        ("=", "{F} ¿Cuál fue el promedio de alarmas por turno?", "(6+3+9)//3", "Se divide el total de alarmas entre los tres turnos.", " alarmas"),
        ("abc", "{F} ¿Qué corresponde por cada alarma, según la regla de la hoja?", "Avisar a la enfermera siempre", "Avisar solo si son más de 6", "No avisar si el balance es normal", "La regla de la hoja pide avisar ante toda alarma."),
        ("=", "{F} Si durante 3 días seguidos se omitieran los mismos registros que ese día, ¿cuántos registros omitidos habría en total?", "(24-22)*3", "Se restan los realizados de los programados y se multiplica por los 3 días.", " registros"),
        ("abc", "{F} ¿Cómo debe anotarse un registro omitido por un traslado del paciente?", "Como omitido, con el motivo, e informado a la enfermera", "Como realizado", "No se anota", "Un registro omitido se anota con su motivo y se informa."),
        ("abc", "{F} El paciente de la cama 2 tuvo un balance de −100 ml en la tarde. Su familiar pregunta si es grave. ¿Qué corresponde?", "Derivar a la enfermera o al médico, que interpretan los datos", "Decirle que no es nada", "Decirle que es grave", "El técnico no interpreta ni tranquiliza con datos que no puede evaluar."),
        ("abc", "{F} Un compañero propone anotar una cifra distinta en el balance de la noche «para que cuadre con el total». ¿Qué corresponde?", "No cambiar datos y avisar a la enfermera de la diferencia, si la hay", "Anotarla, si ayuda a cuadrar", "Borrar el dato anterior", "Los datos se registran tal como son; la diferencia se informa."),
    ],
    ctx=("abc", "{F} Al cerrar el turno de la noche, la técnica se da cuenta de que no anotó 30 ml de líquido de un registro. Los egresos de la noche pasarían de 600 a 630 ml. ¿Qué hace?", "Anota el dato con la hora real y su firma, avisa a la enfermera del cambio y corrige con trazabilidad", "No lo anota, porque son pocos", "Cambia el total sin avisar", "Los datos faltantes se agregan con trazabilidad y se informan."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cómo se calcula el balance de un turno?", "Ingresos menos egresos", "Se restan los egresos de los ingresos."),
        ("¿Cómo calculas el promedio de alarmas por turno?", "Total de alarmas ÷ cantidad de turnos", "Resume varios turnos en un valor."),
        ("¿Qué haces con un registro omitido?", "Lo anoto como omitido, con motivo, y aviso a la enfermera", "Un pendiente no se anota como realizado, sino con su motivo."),
    ],
    op=("Planilla de ejemplo (valores inventados): «Ingresos por turno: 1.000, 900 y 800 ml; egresos: 900, 1.100 y 700 ml. Alarmas: 4, 2 y 6. Registros programados: 24; realizados: 21; omitidos con motivo: 3. Regla: avisar si el balance de un turno es mayor que +250 o menor que −250 ml, y ante toda alarma». "
        "Calcula: el balance de cada turno y el total; el promedio de alarmas; cuántos registros se omitieron. Escribe qué avisarías a la enfermera y cómo anotarías los registros omitidos.",
        "Balances: +100, −200 y +100; total: 0 ml. Ninguno supera ±250. Alarmas: 4+2+6 = 12; promedio: 12 ÷ 3 = 4. Omitidos: 24 − 21 = 3. Avisaría de las 12 alarmas, con la hora de cada una, y anotaría los 3 registros como omitidos con su motivo.",
        ["calcula los tres balances y el total", "calcula 4 alarmas por turno", "calcula 3 omitidos", "anota omitidos con motivo y avisa"],
        ["hoja con cuatro grupos de cálculos y una frase de aviso"],
        ["restar al revés", "anotar los omitidos como realizados", "interpretar los balances"],
        "Pregunta: «¿qué haces ante cada alarma?». Debe responder avisar a la enfermera."),
    reinforce="Con ingresos de 500, 600 y 700 ml y egresos de 400, 700 y 500 ml, calcula el balance de cada turno y el total.",
    extend="Explica con un ejemplo inventado por qué un registro omitido se informa y no se anota como hecho.",
)

# ============================================================ OAM-02, clase 5
F = ("Ficha 5 (comparar mensajes, de ejemplo). Lista de verificación de un mensaje al personal de salud, 6 puntos: (1) identifica a la persona y el lugar; (2) dice la hora; (3) dice qué observó, con datos; (4) dice desde cuándo; (5) dice qué pide; (6) verifica que lo entendieron. "
     "Mensaje A: «Cama 4, 10:15. La alarma de pulso suena desde hace 2 minutos. El monitor marca 118; a las 10:00 marcaba 90; el límite programado es 110. Pido que venga la enfermera. ¿Quedó claro?». "
     "Mensaje B: «Oiga, el de la cama cuatro está mal, la máquina suena, no sé desde cuándo, venga rápido». Duración al hablar: mensaje A, 30 segundos; mensaje B, 10 segundos. El mensaje B cumple los puntos 1 y 5.")
build(
    O2, 5, F,
    use="Aprenderé a comparar dos mensajes con una lista de verificación, a ver por qué uno es más seguro y a valorar el tiempo y la claridad juntos.",
    prior=["Conozco el mensaje de cuatro partes y el monitoreo.", "Sé sumar puntos y restar tiempos.", "Sé leer una lista de verificación."],
    explain=[
        "Comparar dos mensajes es aplicarles la misma lista: identificar a la persona y el lugar, decir la hora, decir qué se observó con datos, decir desde cuándo, decir qué se pide y verificar que lo entendieron. Un mensaje que cumple más puntos es más seguro, porque quien lo recibe puede decidir sin hacer preguntas. Un mensaje más corto ahorra segundos, pero si le faltan datos, puede demorar la decisión o llevar a un error.",
        "Cuando hay urgencia, el mensaje debe ser breve y claro, no incompleto. Se puede decir lo esencial en pocas palabras: dónde, qué ocurre, desde cuándo, qué dato se observó y qué se pide. Se verifica que lo entendieron con una pregunta corta o repitiendo lo acordado. Después se registra en la hoja con hora y firma, con los mismos datos.",
        "Los mensajes son de ejemplo y el cuaderno no enseña a manejar equipos." + LIM,
    ],
    vocab=[("mensaje claro", "mensaje con persona, lugar, hora, observación con datos, desde cuándo, petición y verificación"), ("urgencia", "situación que requiere avisar sin demora"), ("dato esencial", "información mínima necesaria para decidir"), ("verificar", "comprobar que la otra persona entendió"), ("lista de verificación", "puntos que se revisan en un mensaje")],
    worked=[
        ("Contar puntos", "Un mensaje de ejemplo cumple 4 de los 6 puntos de la lista. ¿Cuántos le faltan?", ["6 − 4 = 2.", "Los dos faltantes se agregan antes de enviar el mensaje."], "2 puntos"),
        ("Comparar tiempos", "Un mensaje de ejemplo dura 25 segundos y otro, 8 segundos. ¿Cuántos segundos más dura el primero?", ["Se resta el menor del mayor.", "25 − 8 = 17."], "17 segundos")],
    mistakes=[("Gritar «venga rápido» sin decir qué ocurre.", "La enfermera no sabe a qué prepararse ni qué priorizar.", "Di dónde, qué ocurre, qué dato observaste y qué pides."),
              ("Dar un mensaje largo y confuso cuando hay urgencia.", "Se pierde tiempo valioso.", "Usa frases cortas con datos, en el orden de la lista.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un dato esencial?", "La información mínima necesaria para decidir", "Una opinión del técnico", "El nombre del técnico", "Un dato esencial permite que el profesional decida."),
        ("abc", "{F} ¿Cuántos puntos tiene la lista de verificación de un mensaje?", "Seis", "Cuatro", "Ocho", "La ficha enumera seis puntos de verificación."),
        ("abc", "{F} ¿Cuántos puntos cumple el mensaje A?", "Los 6", "Solo 4", "Solo 2", "El mensaje A identifica, dice hora, datos, desde cuándo, petición y verifica."),
        ("=", "{F} ¿Cuántos puntos incumple el mensaje B?", "6-2", "Se restan los dos puntos que cumple del total de seis.", " puntos"),
        ("abc", "{F} ¿Qué puntos no cumple el mensaje B?", "Los puntos 2, 3, 4 y 6: hora, datos, desde cuándo y verificación", "Los puntos 1 y 5", "Solo el punto 3", "La ficha dice que B cumple solo los puntos 1 y 5."),
        ("=", "{F} ¿Cuántos segundos más dura el mensaje A que el mensaje B?", "30-10", "Se restan los segundos del mensaje B de los de A.", " segundos"),
        ("=", "{F} ¿Cuántas veces más dura el mensaje A que el mensaje B?", "30//10", "Se divide la duración de A entre la de B.", " veces"),
        ("abc", "{F} ¿Qué mensaje es más seguro para decidir?", "El mensaje A, porque da los datos necesarios", "El mensaje B, porque es más rápido", "Ambos por igual", "A permite que la enfermera sepa qué ocurre y se prepare."),
        ("abc", "{F} ¿Qué frase del mensaje A es la observación con datos?", "«El monitor marca 118; a las 10:00 marcaba 90; el límite programado es 110»", "«Pido que venga la enfermera»", "«¿Quedó claro?»", "Son los datos concretos que se observan en el monitor."),
        ("abc", "{F} Un compañero dice: «B es mejor, porque en una urgencia no hay tiempo». ¿Qué corresponde responder?", "Que se puede ser breve y completo; sin datos la enfermera pierde más tiempo", "Que tiene razón, porque 10 segundos es mejor", "Que solo importa la hora", "Con 30 segundos se dan datos que ahorran tiempo después."),
        ("abc", "{F} ¿Cómo mejorarías la frase «no sé desde cuándo» del mensaje B?", "Verificar desde cuándo suena la alarma y decirlo, o decir «recién la noto»", "Dejarla como está", "Quitar la frase sin reemplazarla", "Decir desde cuándo es un dato que ayuda a decidir."),
        ("=", "{F} Si el mensaje B se completara con los 4 puntos que le faltan y durara 15 segundos más, ¿cuántos segundos duraría?", "10+15", "Se suman los segundos adicionales a los de B.", " segundos"),
        ("abc", "{F} Después de enviar el mensaje A, ¿qué debe hacer el técnico?", "Registrar en la hoja los mismos datos con hora y firma", "No registrar nada, porque ya se dijo", "Anotar solo «avisé»", "Lo dicho se registra con los mismos datos para dejar trazabilidad."),
    ],
    ctx=("abc", "{F} A las 22:40 suena la alarma de la cama 3 y la enfermera está a gran distancia. El técnico solo puede decir una frase corta. ¿Qué dice?", "«Cama 3, 22:40: suena la alarma de pulso desde hace un minuto; marca 120; pido que venga»", "«¡Venga!»", "«Ya me parecía que algo iba a pasar con el de la 3»", "Una frase corta puede incluir lugar, hora, observación, desde cuándo y petición."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿qué debe tener un mensaje claro?", "Persona y lugar, hora, observación con datos, desde cuándo y petición", "Son los puntos de la lista de verificación."),
        ("¿Qué pasa si un mensaje es muy corto y sin datos?", "Puede demorar la decisión o llevar a un error", "La enfermera tendrá que preguntar lo que falta."),
        ("¿Qué haces después de avisar?", "Registro en la hoja con hora y firma", "El registro con hora y firma deja trazabilidad."),
    ],
    op=("Mensajes de ejemplo: «Mensaje 1: «Cama 5, 18:20. Suena la alarma de pulso desde hace 3 minutos. El monitor marca 125; a las 18:00 marcaba 95; el límite programado es 115. Pido que venga la enfermera. ¿Entendió?». Mensaje 2: «Está raro el de la cinco, suena una cosa». Duración: mensaje 1, 35 segundos; mensaje 2, 8 segundos». "
        "Usa la lista de seis puntos de la ficha. Escribe: cuántos puntos cumple cada mensaje (el 2 cumple 1); cuántos segundos más dura el mensaje 1; cuál es más seguro y por qué; y reescribe el mensaje 2 con las seis partes.",
        "Mensaje 1: cumple los 6 puntos; mensaje 2 cumple 1. Diferencia: 35 − 8 = 27 segundos. El mensaje 1 es más seguro porque da los datos para decidir. Mensaje 2 reescrito: «Cama 5, 18:20; suena la alarma de pulso desde hace 3 minutos; el monitor marca 125; pido que venga la enfermera. ¿Entendió?».",
        ["cuenta 6 y 1 puntos", "calcula 27 segundos", "elige el mensaje 1 con razón", "reescribe con las seis partes"],
        ["hoja con dos conteos, una resta, una elección con razón y un mensaje reescrito"],
        ["decir que el más corto es mejor", "no incluir la petición", "interpretar en el mensaje"],
        "Pregunta: «¿tu mensaje reescrito incluye qué pides y la verificación?». Si no, pídele agregarlos."),
    reinforce="Escribe los seis puntos de la lista de un mensaje claro y redacta uno breve para una alarma de ejemplo.",
    extend="Explica con un ejemplo inventado por qué verificar que lo entendieron puede evitar un error importante.",
)

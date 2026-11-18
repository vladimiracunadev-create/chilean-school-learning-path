"""Objetivos genéricos TP 3.º y 4.º medio, módulo C: OAG-07 (aprendizaje permanente), OAG-08 (tecnologías de la información y la comunicación) y OAG-09 (uso eficiente de insumos, desechos, eficiencia energética y cuidado ambiental).
Todo en papel: empresas, personas, equipos, consumos y cifras inventados y rotulados «de ejemplo». Sin software que instalar y sin procedimientos operativos con residuos o sustancias."""
from __future__ import annotations

from tp_gene_common import build

G7 = "TP-GENE-3y4-OAG-07"
G8 = "TP-GENE-3y4-OAG-08"
G9 = "TP-GENE-3y4-OAG-09"
LIM = " Este cuaderno trabaja en papel, con casos de ejemplo: no reemplaza a tu profesor, a tu jefatura ni a la norma vigente."

# ============================================================ OAG-07, clase 1
F = ("Ficha 25 (tres trabajadores de ejemplo en empresas ficticias). Inés, técnica en administración, hace un curso corto de 20 horas sobre atención de clientes que ofrece su empresa. "
     "Pablo, auxiliar de bodega, aprende a usar un nuevo registro de inventarios mirando y preguntando a un compañero con mucha experiencia. Carla estudia una carrera técnica en un instituto, con un plan de estudios de 4 semestres. "
     "Cambio en la empresa de ejemplo: en 3 meses se pasará de registrar en papel a registrar en un sistema digital.")
build(
    G7, 1, F,
    use="Aprenderé por qué el trabajo exige seguir aprendiendo toda la vida y cuáles son las formas de aprender: formal, no formal e informal.",
    prior=["Sé que la tecnología cambia.", "Sé sumar y multiplicar enteros.", "Sé que equivocarse ayuda a aprender."],
    explain=[
        "El aprendizaje permanente es seguir aprendiendo a lo largo de toda la vida laboral. Es necesario porque la tecnología, las normas, las herramientas y las necesidades de los clientes cambian. Una persona que deja de aprender corre el riesgo de quedar con conocimientos que ya no sirven. Aprender también abre opciones: mejores tareas, mayor responsabilidad y nuevas oportunidades de empleo.",
        "Hay tres formas de aprender. El aprendizaje formal sigue un plan de estudios y entrega una certificación o un título oficial, como un liceo técnico o una carrera. El aprendizaje no formal ocurre en cursos y capacitaciones organizados, con o sin certificado. El aprendizaje informal ocurre en el día a día: observando a un compañero, leyendo un manual, practicando y corrigiendo errores. Las tres formas se complementan.",
        "Aprender requiere ciertas actitudes: curiosidad, constancia, aceptar los errores como parte del proceso y pedir ayuda. Además de las habilidades técnicas del oficio, se aprenden habilidades blandas, como comunicarse, trabajar en equipo y organizarse." + LIM,
    ],
    vocab=[("aprendizaje permanente", "seguir aprendiendo a lo largo de toda la vida laboral"), ("aprendizaje formal", "el que sigue un plan de estudios y entrega una certificación o un título oficial"), ("aprendizaje no formal", "el que ocurre en cursos y capacitaciones organizados"), ("aprendizaje informal", "el que ocurre en el día a día, observando, practicando y preguntando"), ("certificación", "documento que acredita que alguien aprendió o logró algo"), ("habilidad blanda", "habilidad personal como comunicarse o trabajar en equipo")],
    worked=[
        ("Clasificar una forma de aprender", "Un cocinero de ejemplo aprende una técnica nueva observando a su jefe durante el servicio. ¿Qué tipo de aprendizaje es?", ["Ocurre en el día a día, sin plan de estudios.", "Es aprendizaje informal."], "Informal"),
        ("Calcular sesiones", "Un curso de ejemplo de 12 horas se divide en sesiones de 3 horas. ¿Cuántas sesiones tiene?", ["Se divide el total de horas entre las horas por sesión.", "12 ÷ 3 = 4."], "4 sesiones"),
    ],
    mistakes=[("Decir «ya terminé el liceo, no necesito aprender más».", "El oficio cambia con la tecnología y las normas, y lo aprendido puede quedar atrasado.", "Planifica seguir aprendiendo con cursos, práctica y lecturas."),
              ("Creer que solo cuenta lo que da un certificado.", "También se aprende mucho de forma informal y esos aprendizajes valen en el trabajo.", "Valora todas las formas de aprender y busca evidencias de lo aprendido.")],
    T=[
        ("abc", "En la vida laboral: ¿qué es el aprendizaje permanente?", "Seguir aprendiendo a lo largo de toda la vida laboral", "Estudiar solo mientras se está en el liceo", "Aprender solo con un título universitario", "El aprendizaje permanente no termina con el liceo ni depende de un único tipo de título."),
        ("abc", "{F} ¿Qué tipo de aprendizaje es el de Inés?", "No formal: un curso corto organizado por su empresa", "Formal: una carrera con plan de estudios", "Informal: aprendizaje sin organización", "Un curso corto organizado, con horas definidas, es aprendizaje no formal."),
        ("abc", "{F} ¿Qué tipo de aprendizaje es el de Pablo?", "Informal: observa y pregunta a un compañero", "Formal: sigue un plan de estudios", "No formal: asiste a un curso", "Pablo aprende en el día a día, sin un curso ni un plan de estudios."),
        ("abc", "{F} ¿Qué tipo de aprendizaje es el de Carla?", "Formal: carrera con plan de estudios", "Informal: lo hace por su cuenta", "No formal: un taller de un día", "La carrera técnica tiene un plan de estudios y una certificación oficial."),
        ("abc", "¿Qué distingue al aprendizaje formal de los otros?", "Sigue un plan de estudios y entrega una certificación o título oficial", "Se hace solo dentro del lugar de trabajo", "No requiere esfuerzo", "Lo propio del aprendizaje formal es el plan de estudios y la certificación oficial."),
        ("abc", "{F} ¿Qué cambio de la empresa hace necesario aprender algo nuevo?", "El paso del registro en papel a un sistema digital", "Que Inés haga un curso", "Que Carla estudie 4 semestres", "El nuevo sistema exige nuevas habilidades de registro."),
        ("=", "{F} Pablo practica el sistema nuevo 20 minutos al día, 5 días por semana. ¿Cuántos minutos practica en 3 semanas?", "20*5*3", "Se multiplican los minutos diarios por los días y por las semanas.", " minutos"),
        ("=", "{F} El curso de Inés dura 20 horas en sesiones de 4 horas. ¿Cuántas sesiones tiene?", "20//4", "Se divide el total de horas entre las horas de cada sesión.", " sesiones"),
        ("abc", "Un trabajador dice: «Ya terminé el liceo, no necesito aprender más». ¿Qué respuesta es adecuada?", "El oficio cambia, y seguir aprendiendo permite mantener las habilidades al día", "Tiene razón: ya sabe todo lo necesario", "Solo necesitan aprender los jefes", "Las herramientas y normas cambian, por lo que el aprendizaje debe continuar."),
        ("abc", "Un trabajador comete un error con el sistema nuevo y se siente avergonzado. ¿Qué actitud ayuda a aprender?", "Aceptar que equivocarse es parte de aprender, pedir ayuda y corregir", "Dejar de usar el sistema", "Esconder el error", "Reconocer el error y pedir ayuda permite aprender y evita que se repita."),
        ("abc", "¿Por qué las habilidades blandas, como comunicarse bien, también se deben aprender?", "Porque se practican y mejoran, y son clave para trabajar en equipo", "Porque nacen con la persona y no cambian", "Porque solo importan en cargos de jefatura", "Las habilidades blandas se desarrollan con práctica y retroalimentación."),
        ("abc", "{F} Un trabajador tiene tres meses, poco dinero y su empresa ofrece capacitación gratuita y un tutor. ¿Qué combinación conviene?", "Usar la capacitación de la empresa y practicar con el tutor", "Esperar a juntar dinero para un curso externo", "Aprender solo al final, cuando llegue el sistema", "La capacitación gratuita y la práctica guiada aprovechan los recursos disponibles."),
        ("=", "En una empresa de ejemplo hay 20 trabajadores y un curso con 8 cupos. ¿Cuántos trabajadores quedan sin cupo?", "20-8", "Al total de trabajadores se le restan los cupos disponibles.", " trabajadores"),
    ],
    ctx=("abc", "{F} A Inés le ofrecen la opción de hacer el curso de atención de clientes en horario de trabajo o fuera de él. ¿Qué debe considerar para elegir?", "Su carga de trabajo, su cansancio y el acuerdo con su jefatura sobre el horario", "Solo lo que prefiera su compañera", "Nada: da igual cuándo lo haga", "Una buena decisión de formación considera el tiempo disponible y el acuerdo con la empresa."),
    sc=[
        ("En la vida laboral: ¿qué es el aprendizaje informal?", "El que ocurre en el día a día", "Se aprende observando, practicando y preguntando."),
        ("¿Por qué hay que seguir aprendiendo en el trabajo?", "Porque la tecnología y las normas cambian", "Lo aprendido puede quedar atrasado si no se actualiza."),
        ("¿Qué haces si cometes un error al aprender?", "Pido ayuda y corrijo", "Los errores son parte natural del aprendizaje."),
    ],
    op=("Caso de ejemplo. En una clínica ficticia se instalará un nuevo sistema de fichas digitales. Trabajan allí Marta (auxiliar de admisión), Eduardo (técnico en enfermería) y Rocío (aseo y apoyo). La clínica ofrece un curso de 8 horas, un compañero tutor y manuales. "
        "Escribe: (1) una forma de aprendizaje formal, una no formal y una informal que podrían usar, (2) qué actitud necesitaría cada uno, (3) cuántas sesiones de 2 horas tiene el curso, (4) una habilidad blanda que también necesitarán.",
        "(1) Formal: estudiar una carrera técnica. No formal: el curso de 8 horas. Informal: aprender con el compañero tutor. (2) Curiosidad, constancia y pedir ayuda. (3) 8 ÷ 2 = 4 sesiones. (4) Comunicarse con las personas que atienden y trabajar en equipo.",
        ["distingue las tres formas de aprender", "nombra actitudes", "calcula las sesiones", "nombra una habilidad blanda"],
        ["hoja con cuatro respuestas"],
        ["confundir formal con no formal", "olvidar la actitud", "dividir mal las horas"],
        "Pregunta: «¿qué harías si el curso es en horario de atención?». Debe hablar de acordar con la jefatura cómo cubrir el servicio."),
    reinforce="Escribe tres cosas que has aprendido en forma formal, no formal e informal.",
    extend="Explica con un ejemplo por qué una persona que aprende informalmente también puede mostrar su aprendizaje con evidencias.",
)

# ============================================================ OAG-07, clase 2
F = ("Ficha 26 (plan de aprendizaje de ejemplo de Tomás, ayudante de taller en una empresa ficticia). Meta: aprender a leer los planos básicos de su área y explicar dos de ellos a su jefe en 6 semanas. "
     "Tiempo: 3 sesiones por semana de 40 minutos. Recursos: el manual de la empresa y un compañero tutor. Evaluación: explicar dos planos de ejemplo al final de la semana 6. Registro: marcar cada sesión realizada.")
build(
    G7, 2, F,
    use="Aprenderé a planificar mi propio aprendizaje con metas claras, plazos, recursos y seguimiento.",
    prior=["Conozco las formas de aprender.", "Sé calcular tiempos.", "Sé qué es un plazo."],
    explain=[
        "Un plan de aprendizaje es una guía para lograr algo que quieres aprender. Parte de una meta: qué quieres lograr. Una meta bien formulada es clara (dice qué), medible (se puede comprobar), tiene un plazo y es posible de lograr con tu tiempo y tus recursos. Por ejemplo, «aprender planos» es vaga; «leer dos planos básicos y explicarlos en seis semanas» es una meta concreta.",
        "Luego se define el tiempo que se dedicará, los recursos (manuales, personas que ayuden, cursos confiables) y la forma de evaluar si se logró. Se hace seguimiento con un registro de las sesiones realizadas. Si se ve que el plan no funciona, se ajusta: más tiempo, otro recurso o una meta más pequeña. Ajustar no es fracasar; es aprender a planificar mejor.",
        "Elige recursos confiables, como manuales de la empresa, cursos de instituciones reconocidas y personas con experiencia. Evita recursos de origen desconocido." + LIM,
    ],
    vocab=[("meta de aprendizaje", "lo que una persona quiere aprender, formulado de forma clara, medible y con plazo"), ("plan de aprendizaje", "guía con meta, tiempo, recursos y evaluación"), ("recurso", "material o persona que ayuda a aprender"), ("seguimiento", "revisión periódica de cuánto se ha avanzado"), ("ajustar", "cambiar el plan cuando no funciona")],
    worked=[
        ("Revisar una meta", "¿Es una buena meta «aprender inglés»? Compárala con «aprender 30 frases de atención al cliente en inglés en 5 semanas».", ["La segunda dice qué, cuánto y en qué plazo.", "La primera es vaga."], "La segunda es una meta clara, medible y con plazo"),
        ("Calcular horas de estudio", "Una persona estudia 2 sesiones por semana de 30 minutos durante 4 semanas. ¿Cuántos minutos son en total?", ["Se multiplican sesiones, minutos y semanas.", "2 × 30 × 4 = 240."], "240 minutos"),
    ],
    mistakes=[("Fijar una meta como «quiero aprender de todo».", "Es tan amplia que no se puede medir ni cumplir.", "Define una meta concreta, medible y con plazo."),
              ("Abandonar el plan al primer atraso.", "Un atraso se puede ajustar; abandonar hace perder lo avanzado.", "Revisa el registro, ajusta el calendario y sigue.")],
    T=[
        ("abc", "En planes de aprendizaje: ¿qué características tiene una meta bien formulada?", "Es clara, medible, tiene plazo y es posible de lograr", "Es muy amplia para que no se acabe nunca", "Se define sin plazo para no presionarse", "Una buena meta se puede comprobar y tiene un plazo realista."),
        ("abc", "{F} ¿Cuál es la meta de Tomás?", "Leer los planos básicos de su área y explicar dos a su jefe en 6 semanas", "Aprender de todo en el taller", "Convertirse en jefe de taller", "La meta de Tomás es concreta, con un producto y un plazo."),
        ("abc", "{F} ¿Cómo evaluará Tomás si logró su meta?", "Explicando dos planos de ejemplo al final de la semana 6", "Esperando a que su jefe lo note", "Con una nota que se pone él mismo sin comprobar", "Su plan define una evaluación concreta: explicar dos planos."),
        ("=", "{F} ¿Cuántas sesiones tendrá en total en las 6 semanas?", "3*6", "Se multiplican las sesiones por semana por las semanas.", " sesiones"),
        ("=", "{F} Si Tomás faltó a 4 sesiones, ¿cuántas sesiones realizó?", "3*6-4", "Al total de sesiones del plan se le restan las que faltó.", " sesiones"),
        ("abc", "¿Qué meta es mejor?", "Leer dos planos básicos y explicarlos en seis semanas", "Aprender de planos", "Ser el mejor del taller", "La primera tiene un resultado concreto y un plazo; las otras no se pueden medir."),
        ("abc", "{F} Tomás realizó 14 de las 18 sesiones. ¿Qué conclusión es adecuada?", "Cumplió la mayor parte; conviene revisar qué lo impidió y ajustar el calendario", "Fracasó y debe abandonar", "No hay que revisar nada porque ya avanzó", "Revisar causas y ajustar permite terminar bien el plan."),
        ("=", "{F} Si en vez de 40 minutos hiciera sesiones de 30 minutos, 3 por semana, ¿cuántos minutos menos estudiaría por semana?", "(40-30)*3", "Se calcula la diferencia por sesión y se multiplica por las sesiones semanales.", " minutos"),
        ("abc", "Tomás nota que 40 minutos son poco para su ritmo. ¿Qué es lo más razonable?", "Ajustar el plan: más tiempo o más semanas, y registrar el cambio", "Seguir igual aunque no avance", "Dejar el plan", "Un plan se ajusta cuando la realidad lo exige."),
        ("abc", "Un compañero dice: «Para qué planificar, aprendo cuando puedo». ¿Qué problema tiene esa idea?", "Sin meta, tiempo y seguimiento es difícil saber si se avanza y se posterga fácilmente", "Ninguno: planificar es una pérdida de tiempo", "Planificar impide aprender", "Un plan ayuda a mantener la constancia y a medir el avance."),
        ("abc", "{F} Tomás debe elegir un recurso adicional. ¿Cuál es el más confiable?", "El manual de la empresa o una persona con experiencia en planos", "Un video anónimo sin explicación", "Un resumen sin autor", "Los recursos confiables tienen autoría y respaldo en la experiencia."),
        ("abc", "{F} Tomás se da cuenta de que confundió dos símbolos del plano. ¿Qué hace?", "Lo anota en su registro, consulta a su tutor y corrige antes de seguir", "Lo ignora porque nadie lo notó", "Cambia de meta", "Registrar y consultar convierte el error en aprendizaje."),
        ("=", "{F} Si el plan se extiende 2 semanas más con las mismas sesiones de 40 minutos, ¿cuántos minutos totales de estudio tendría?", "(6+2)*3*40", "Se calculan las semanas totales y se multiplican por sesiones y minutos.", " minutos"),
    ],
    ctx=("abc", "{F} A la semana 3, Tomás lleva 7 de 9 sesiones y su tutor se ausentará una semana. ¿Qué hace?", "Reorganiza el calendario, usa el manual y consulta con otra persona de confianza", "Detiene el plan hasta que vuelva el tutor", "Cambia de meta sin avisar", "Reorganizar y usar otros recursos mantiene el avance."),
    sc=[
        ("En planes de aprendizaje: ¿qué es una meta medible?", "Una meta que se puede comprobar", "Permite saber si se logró o no."),
        ("¿Para qué sirve el registro de sesiones?", "Para hacer seguimiento del avance", "Muestra cuánto se ha cumplido del plan."),
        ("¿Qué haces si el plan no funciona?", "Lo ajusto", "Ajustar permite seguir avanzando sin abandonar."),
    ],
    op=("Caso de ejemplo. Verónica, ayudante de cocina en un casino ficticio, quiere aprender a leer etiquetas y fichas de productos de forma segura. Tiene 4 semanas, 2 sesiones por semana de 45 minutos, el manual de la cocina y una jefa de turno que puede orientarla. "
        "Escribe: (1) su meta, clara y con plazo, (2) cuántos minutos de estudio tendrá en total, (3) qué recursos usará, (4) cómo evaluará si cumplió, (5) qué haría si en la semana 2 falta a una sesión.",
        "(1) «Leer e interpretar cinco etiquetas de productos (contenido, vencimiento y almacenamiento) en 4 semanas». (2) 2 × 45 × 4 = 360 minutos. (3) El manual de la cocina y la jefa de turno. (4) Explicando a la jefa cinco etiquetas de ejemplo. (5) Reorganizar y recuperar la sesión en la semana siguiente.",
        ["formula una meta clara y con plazo", "calcula los minutos totales", "elige recursos confiables", "define una evaluación y un ajuste"],
        ["hoja con cinco respuestas"],
        ["meta vaga", "no calcular el total", "no definir cómo evaluar"],
        "Pregunta: «¿qué pasa si la jefa de turno no está?». Debe proponer otro recurso confiable, como otro compañero o el manual."),
    reinforce="Escribe una meta de aprendizaje para este mes con plazo y cómo medirás si la lograste.",
    extend="Explica por qué ajustar un plan es parte de planificar bien y no un fracaso.",
)

# ============================================================ OAG-07, clase 3
F = ("Ficha 27 (bitácora de aprendizaje de ejemplo de Gabriela, aprendiz de secretaría en una oficina ficticia). Semana 1: practicó 5 tareas de archivo y 4 salieron correctas; error: archivó dos carpetas por fecha y no por nombre; acción: releer la regla de archivo. "
     "Semana 2: 10 tareas y 9 correctas; error: olvidó firmar un registro; acción: crear un recordatorio. Semana 3: 10 tareas y 10 correctas; sin errores. "
     "Comentario de su tutora: «Mejoraste la precisión; ahora trabaja en la rapidez».")
build(
    G7, 3, F,
    use="Aprenderé a reflexionar sobre mi aprendizaje: llevar una bitácora, usar la retroalimentación y aprender de los errores.",
    prior=["Sé planificar una meta de aprendizaje.", "Sé calcular cuántos por cada 100.", "Sé recibir comentarios con respeto."],
    explain=[
        "Reflexionar sobre el aprendizaje es detenerse a pensar qué hice, qué resultó, por qué y qué cambiaré. Una bitácora es un cuaderno o registro donde se anotan las prácticas, los errores y las acciones de mejora de cada semana. Sirve como evidencia de lo aprendido y permite ver el progreso. Un portafolio reúne trabajos y comentarios que muestran lo que una persona sabe hacer.",
        "La retroalimentación es la información que otra persona te da sobre tu trabajo. Para aprovecharla, escucha sin interrumpir, pide ejemplos concretos y decide qué cambiar. La autoevaluación es revisar tu propio trabajo con una pauta: qué logré, qué me falta y qué haré. Los errores no son motivo de vergüenza: son datos que muestran qué ajustar. Si un error se repite, hay que buscar su causa y cambiar el método.",
        "Cuidar el descanso, organizar el tiempo y hacer pausas también ayudan a aprender mejor." + LIM,
    ],
    vocab=[("bitácora", "registro donde se anotan prácticas, errores y acciones de mejora"), ("portafolio", "conjunto de trabajos y comentarios que muestran lo que alguien sabe hacer"), ("retroalimentación", "información que se entrega sobre un trabajo para ayudar a mejorarlo"), ("autoevaluación", "revisión del propio trabajo con una pauta"), ("evidencia", "trabajo o registro que muestra lo aprendido")],
    worked=[
        ("Calcular el acierto", "En una semana de ejemplo, un aprendiz hizo 20 tareas y 16 salieron correctas. ¿Cuántas de cada 100 fueron correctas?", ["Se multiplica por 100 y se divide entre las tareas.", "16 × 100 ÷ 20 = 80."], "80 de cada 100"),
        ("Aprovechar un comentario", "Un tutor de ejemplo dice: «Tus informes están claros, pero llegan tarde». ¿Qué conviene pedirle?", ["Se piden ejemplos concretos y ayuda para mejorar.", "Por ejemplo, qué retrasa el informe."], "Ejemplos concretos de los atrasos y cómo mejorarlos"),
    ],
    mistakes=[("Responder a una crítica con «es que ahí no me explicaron».", "Se cierra a la retroalimentación y se pierde la oportunidad de mejorar.", "Escucha, pide ejemplos y decide qué cambiar."),
              ("Borrar de la bitácora las semanas con errores.", "Se pierde la evidencia del proceso y de lo que se aprendió de los errores.", "Conserva los errores y anota qué acción tomaste.")],
    T=[
        ("abc", "En el aprendizaje: ¿qué es una bitácora?", "Un registro de prácticas, errores y acciones de mejora", "Un diario con secretos personales", "Una lista de trabajos que no se hicieron", "La bitácora sirve para ver el proceso y mejorar."),
        ("abc", "{F} ¿Qué error cometió Gabriela en la semana 1?", "Archivó dos carpetas por fecha y no por nombre", "Olvidó firmar un registro", "No hizo ninguna tarea", "El error de la semana 1 está anotado en la bitácora."),
        ("abc", "{F} ¿Qué acción de mejora anotó para el olvido de firmar?", "Crear un recordatorio", "Releer la regla de archivo", "Cambiar de tutora", "La acción anotada en la semana 2 fue crear un recordatorio."),
        ("=", "{F} ¿Cuántas tareas practicó en total en las tres semanas?", "5+10+10", "Se suman las tareas de las tres semanas.", " tareas"),
        ("=", "{F} ¿Cuántas tareas salieron correctas en total en las tres semanas?", "4+9+10", "Se suman las tareas correctas de cada semana.", " tareas"),
        ("=", "{F} ¿Cuántas tareas de cada 100 salieron correctas en la semana 2?", "9*100//10", "Se multiplican las correctas por 100 y se divide entre las tareas de la semana.", " de cada 100"),
        ("abc", "{F} ¿Qué tendencia muestran los resultados de las tres semanas?", "Mejoraron cada semana", "Empeoraron cada semana", "Se mantuvieron iguales", "El porcentaje de aciertos subió de 80 a 90 y a 100 de cada 100."),
        ("abc", "{F} ¿Qué significa el comentario de la tutora?", "Que su precisión mejoró y que el siguiente desafío es hacerlo más rápido", "Que debe dejar de practicar", "Que ya no tiene nada que mejorar", "El comentario reconoce un logro y propone un nuevo objetivo."),
        ("abc", "¿Cómo es una buena autoevaluación?", "Revisar con una pauta qué logré, qué me falta y qué haré", "Ponerse una nota alta sin revisar", "Comparar solo con los demás", "La autoevaluación necesita criterios claros y propuestas de acción."),
        ("abc", "Gabriela recibe una crítica y se enoja. ¿Qué actitud ayuda a aprender?", "Escuchar, pedir ejemplos concretos y decidir qué cambiar", "Responder que la crítica es injusta", "Ignorar el comentario", "Escuchar y pedir ejemplos permite usar la retroalimentación para mejorar."),
        ("abc", "Una aprendiz ve que comete el mismo error tres semanas seguidas. ¿Qué conviene hacer?", "Buscar la causa y cambiar el método de trabajo", "Seguir igual porque ya lo sabe", "Anotar solo los aciertos", "Si un error se repite, hay que buscar su causa y cambiar el método."),
        ("abc", "{F} Un compañero propone que Gabriela borre la semana 1 de la bitácora por tener un error. ¿Qué responde?", "Que la bitácora debe mostrar todo el proceso y que los errores sirven para mejorar", "Que tiene razón, porque los errores quedan mal", "Que debe borrar también la semana 2", "El registro completo muestra cómo mejoró la persona."),
        ("=", "{F} Si en la semana 4 Gabriela hace 12 tareas y logra 11 correctas, ¿cuántas tareas correctas acumula en las cuatro semanas?", "4+9+10+11", "Se suman las tareas correctas de las cuatro semanas.", " tareas"),
    ],
    ctx=("abc", "{F} Gabriela debe preparar su portafolio para mostrar su aprendizaje. ¿Qué evidencia es más útil?", "La bitácora con sus mejoras, trabajos de ejemplo y el comentario de su tutora", "Solo una frase que dice «aprendí mucho»", "Un trabajo hecho por otra persona", "Una evidencia útil muestra lo que la persona realmente hizo y cómo mejoró."),
    sc=[
        ("En el aprendizaje: ¿para qué sirve la retroalimentación?", "Para saber qué mejorar", "Es información sobre el trabajo que ayuda a mejorarlo."),
        ("¿Qué haces con un error que se repite?", "Busco la causa y cambio el método", "Cambiar el método evita repetir el mismo error."),
        ("¿Qué incluye una bitácora de aprendizaje?", "Prácticas, errores y acciones de mejora", "Permite ver el proceso y el progreso."),
    ],
    op=("Caso de ejemplo. Matías, aprendiz de una cocina de casino ficticia, anotó en su bitácora: semana 1, 10 preparaciones y 6 con el punto correcto; semana 2, 10 preparaciones y 8 correctas; semana 3, 10 preparaciones y 9 correctas. Error repetido: no controlaba el tiempo y se pasaba. Su jefa le dijo: «Estás mejorando, controla mejor el tiempo». "
        "Escribe: (1) cuántas preparaciones salieron correctas en total, (2) cuántas de cada 100 en cada semana, (3) una causa posible del error y una acción de mejora, (4) cómo usarías el comentario de la jefa, (5) qué evidencias pondrías en tu portafolio.",
        "(1) 6 + 8 + 9 = 23. (2) 60, 80 y 90. (3) Causa: no hay un recordatorio del tiempo; acción: usar un temporizador y anotar cada vez. (4) Pedir ejemplos de cuándo se pasó y cuánto, y acordar una meta. (5) La bitácora, fotos o descripciones de preparaciones y el comentario de la jefa.",
        ["calcula totales y proporciones", "propone causa y acción", "usa la retroalimentación", "selecciona evidencias"],
        ["hoja con cinco respuestas"],
        ["no calcular por cada 100", "ocultar errores", "no proponer acción"],
        "Pregunta: «¿qué harías si en la semana 4 el resultado baja?». Debe pensar en causas posibles, como cansancio o cambio de tarea, y ajustar."),
    reinforce="Escribe una mini bitácora de tres líneas sobre algo que aprendiste esta semana: qué hiciste, qué error tuviste y qué cambiarás.",
    extend="Explica por qué una bitácora que solo incluye aciertos es menos útil para aprender.",
)

# ============================================================ OAG-07, clase 4
F = ("Ficha 28 (opciones de formación de ejemplo; entidades y montos inventados). Opción 1: curso corto de 40 horas, $120.000, con certificado de la entidad de capacitación. Opción 2: diplomado de 120 horas, $480.000, con certificado de un instituto. "
     "Opción 3: curso en línea de 30 horas, sin costo y sin certificado. Una persona de ejemplo dispone de 5 horas por semana para estudiar y de $200.000 de presupuesto.")
build(
    G7, 4, F,
    use="Aprenderé a comparar opciones de formación continua con datos de tiempo, costo y certificación, y a decidir según mis objetivos.",
    prior=["Sé planificar una meta de aprendizaje.", "Sé dividir y comparar costos.", "Conozco las formas de aprender."],
    explain=[
        "La formación continua incluye cursos, capacitaciones, certificaciones y programas que una persona puede hacer mientras trabaja. Para elegir entre opciones conviene comparar cuatro cosas: el objetivo (qué necesito aprender), el tiempo (cuántas horas y semanas requiere), el costo y el reconocimiento (si entrega un certificado válido para lo que busco). El costo por hora se calcula dividiendo el costo total entre las horas del curso.",
        "El tiempo necesario se calcula dividiendo las horas del curso entre las horas que se puede estudiar a la semana. Una opción barata no siempre es la mejor si no cumple el objetivo, y una cara no siempre es mejor si no se ajusta al tiempo. Evita ofertas que prometen resultados imposibles, como empleo asegurado, y revisa siempre en fuentes oficiales si la entidad y el certificado son reconocidos.",
        "Como evidencia de lo aprendido sirven los certificados, los trabajos realizados, las cartas de recomendación de la jefatura y el portafolio. Este cuaderno no recomienda instituciones ni cursos concretos; las decisiones se toman con información oficial y con tu orientador o jefatura." + LIM,
    ],
    vocab=[("formación continua", "cursos y programas que se hacen mientras se trabaja"), ("certificado", "documento que acredita que se hizo un curso"), ("costo por hora", "costo total dividido entre las horas del curso"), ("reconocimiento", "validez de un certificado para el objetivo que se busca"), ("presupuesto", "dinero disponible para un gasto")],
    worked=[
        ("Costo por hora", "Un curso de ejemplo cuesta $90.000 y dura 30 horas. ¿Cuánto cuesta cada hora?", ["Se divide el costo entre las horas.", "90.000 ÷ 30 = 3.000."], "$3.000 por hora"),
        ("Semanas necesarias", "Un curso de ejemplo de 24 horas y una persona que estudia 4 horas por semana. ¿Cuántas semanas necesita?", ["Se dividen las horas del curso entre las horas por semana.", "24 ÷ 4 = 6."], "6 semanas"),
    ],
    mistakes=[("Elegir un curso solo porque es gratuito.", "Puede no cumplir el objetivo ni dar el certificado que se necesita.", "Compara también el objetivo, el tiempo y el reconocimiento."),
              ("Creer una publicidad que promete empleo asegurado en una semana.", "Es una promesa que nadie puede garantizar y puede ser un engaño.", "Revisa la entidad y el certificado en fuentes oficiales.")],
    T=[
        ("abc", "{F} ¿Qué opción entrega un certificado de una entidad de capacitación?", "La opción 1", "La opción 2", "La opción 3", "La opción 1 incluye certificado de la entidad de capacitación; la 2 es de un instituto y la 3 no certifica."),
        ("=", "{F} ¿Cuántas semanas necesita la persona para terminar la opción 1?", "40//5", "Se dividen las horas del curso entre las horas semanales.", " semanas"),
        ("=", "{F} ¿Cuántas semanas necesita para terminar la opción 2?", "120//5", "Se dividen las horas del diplomado entre las horas semanales.", " semanas"),
        ("=", "{F} ¿Cuántas semanas necesita para terminar la opción 3?", "30//5", "Se dividen las horas del curso en línea entre las horas semanales.", " semanas"),
        ("abc", "{F} ¿Qué opciones caben en el presupuesto?", "Las opciones 1 y 3", "Las opciones 1 y 2", "Solo la opción 2", "La opción 2 cuesta $480.000, más que el presupuesto; las otras sí caben."),
        ("=", "{F} ¿Cuánto cuesta cada hora de la opción 1?", "120000//40", "Se divide el costo total entre las horas del curso.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada hora de la opción 2?", "480000//120", "Se divide el costo total entre las horas del diplomado.", " pesos"),
        ("abc", "{F} Si la persona necesita un certificado y debe ajustarse a su presupuesto, ¿qué opción cumple ambas condiciones?", "Solo la opción 1", "Solo la opción 2", "Solo la opción 3", "Es la única que entrega certificado y cuesta menos que el presupuesto."),
        ("=", "{F} Si elige la opción 1, ¿cuánto dinero le sobra del presupuesto?", "200000-120000", "Al presupuesto se le resta el costo de la opción elegida.", " pesos"),
        ("abc", "¿Por qué no basta con elegir la opción más barata?", "Porque también importan el objetivo, el reconocimiento y el tiempo", "Porque lo barato siempre es malo", "Porque el costo no tiene importancia", "La mejor decisión equilibra costo, objetivo, tiempo y reconocimiento."),
        ("abc", "Un aviso dice: «Empleo asegurado en una semana si hace nuestro curso». ¿Qué conviene hacer?", "Desconfiar, comparar y revisar la entidad en fuentes oficiales", "Pagar de inmediato para no perder el cupo", "Darle los datos personales y bancarios", "Nadie puede asegurar empleo; hay que verificar la entidad antes de pagar."),
        ("abc", "Una persona aprendió a hacer inventarios trabajando durante un año, sin curso formal. ¿Qué evidencias puede reunir para mostrar su aprendizaje?", "Registros de su trabajo, una carta de su jefatura y ejemplos de planillas", "Ninguna, porque sin curso no hay evidencia", "Solo su palabra", "Los trabajos y las cartas de recomendación son evidencias válidas del aprendizaje informal."),
        ("=", "{F} Si estudia 5 horas a la semana, ¿cuántas semanas necesita para hacer la opción 1 y luego la opción 3?", "40//5+30//5", "Se calculan las semanas de cada curso y se suman.", " semanas"),
    ],
    ctx=("abc", "{F} Una persona de ejemplo quiere formarse para ascender a encargada de turno. Su jefa le dice que se valora el certificado. ¿Qué decisión es más sensata?", "Elegir según su objetivo, tiempo y presupuesto, y verificar que el certificado sea reconocido", "Elegir el curso más largo, aunque no se relacione", "Elegir el gratuito sin mirar el certificado", "Una elección razonable combina objetivo, tiempo, costo y reconocimiento del certificado."),
    sc=[
        ("En formación continua: ¿cómo se calcula el costo por hora?", "Costo total dividido entre las horas", "Permite comparar cursos de distinta duración."),
        ("¿Cómo calculas las semanas que necesita un curso?", "Horas del curso divididas entre horas semanales", "Muestra si el curso cabe en el tiempo disponible."),
        ("¿Qué revisas antes de pagar un curso?", "Que la entidad y el certificado sean reconocidos", "Así evitas pagar por algo que no sirve."),
    ],
    op=("Caso de ejemplo. Una técnica en administración de una empresa ficticia quiere aprender atención de clientes. Opciones de ejemplo: A) curso de 24 horas, $96.000, con certificado; B) curso en línea de 20 horas, gratuito, sin certificado; C) diplomado de 100 horas, $500.000, con certificado. Tiene 4 horas semanales y $150.000. "
        "Escribe: (1) las semanas de cada opción, (2) el costo por hora de A y C, (3) qué opciones caben en el presupuesto, (4) cuál elegirías si necesita certificado y por qué, (5) una evidencia para su portafolio.",
        "(1) A: 24 ÷ 4 = 6; B: 20 ÷ 4 = 5; C: 100 ÷ 4 = 25 semanas. (2) A: 96.000 ÷ 24 = 4.000; C: 500.000 ÷ 100 = 5.000. (3) A y B. (4) A, porque tiene certificado y cabe en el presupuesto. (5) El certificado y un caso resuelto de atención de clientes.",
        ["calcula semanas y costo por hora", "compara con el presupuesto", "justifica la elección", "propone una evidencia"],
        ["hoja con cinco respuestas"],
        ["ignorar el presupuesto", "elegir sin justificar", "recomendar una entidad real"],
        "Pregunta: «¿qué cambiaría si el presupuesto fuera $600.000?». Debe notar que C cabría y comparar de nuevo con el tiempo y el objetivo."),
    reinforce="Inventa tres opciones de curso con horas y costo y calcula semanas y costo por hora de cada una.",
    extend="Explica por qué es importante verificar el reconocimiento de un certificado antes de pagar.",
)

# ============================================================ OAG-08, clase 1
F = ("Ficha 29 (tres mensajes de ejemplo recibidos en una oficina ficticia). Mensaje A (correo): «Su cuenta será bloqueada hoy. Ingrese su clave en este enlace para evitarlo». Remitente: soporte-cuentas@correo-falso.ejemplo. "
     "Mensaje B (correo): «Hola, adjunto la planilla de ventas que pediste ayer». Remitente: un compañero conocido, desde el correo de la empresa. "
     "Mensaje C (mensajería): «Soy el gerente, necesito una transferencia urgente; no se lo cuentes a nadie». Número desconocido. "
     "Contraseñas de ejemplo usadas en la oficina: P1 = 123456; P2 = sofia2008; P3 = una frase larga de siete palabras sin datos personales.")
build(
    G8, 1, F,
    use="Aprenderé a usar las tecnologías de la información y la comunicación en el trabajo de forma segura y responsable: contraseñas, mensajes engañosos, privacidad, respaldo y pausas.",
    prior=["Sé usar un correo electrónico.", "Sé multiplicar y restar.", "Sé qué son los datos personales."],
    explain=[
        "Las tecnologías de la información y la comunicación (TIC) son herramientas como el computador, el teléfono, el correo y las aplicaciones. Usarlas bien en el trabajo implica proteger la información. El phishing es un mensaje falso que se hace pasar por una persona o empresa para obtener claves, datos o dinero. Sus señales son la urgencia, el pedido de claves o transferencias, remitentes desconocidos y enlaces sospechosos. Ante la duda, no respondas ni abras enlaces: verifica por otro medio y avisa a la jefatura.",
        "Una contraseña segura es larga, única para cada cuenta y sin datos personales (nombre, fechas). Una frase larga es más fuerte que una palabra corta. Las claves son personales y no se comparten. Mantener actualizados los programas corrige fallas de seguridad, y hacer copias de respaldo de los archivos importantes en otro lugar evita perder información.",
        "También se cuida la privacidad: no se fotografían ni se comparten pantallas con datos de clientes. Para cuidar el cuerpo frente a la pantalla se hacen pausas cortas y se mantiene una postura cómoda." + LIM,
    ],
    vocab=[("TIC", "tecnologías de la información y la comunicación: computadores, teléfonos, correo y aplicaciones"), ("phishing", "mensaje falso que busca engañar para obtener claves, datos o dinero"), ("contraseña segura", "clave larga, única y sin datos personales"), ("respaldo", "copia de archivos guardada en otro lugar"), ("privacidad", "derecho a que los datos personales no se difundan"), ("actualización", "versión nueva de un programa que corrige fallas")],
    worked=[
        ("Reconocer una señal de engaño", "Un correo de ejemplo dice: «Gane un premio; entregue su clave bancaria hoy». ¿Qué señal de phishing tiene?", ["Pide una clave y mete urgencia.", "Es un intento de obtener datos."], "Pide una clave y presiona con urgencia"),
        ("Calcular pausas", "Una trabajadora de ejemplo hace una pausa de 5 minutos cada hora durante una jornada de 6 horas. ¿Cuántos minutos de pausa suma?", ["Se multiplican los minutos por las horas.", "5 × 6 = 30."], "30 minutos"),
    ],
    mistakes=[("Entregar la clave porque el mensaje dice que la cuenta se bloqueará hoy.", "La urgencia es una táctica del engaño; las empresas serias no piden claves por mensaje.", "No respondas ni abras el enlace; avisa a la jefatura."),
              ("Usar una misma contraseña con el nombre y el año de nacimiento en todas las cuentas.", "Es fácil de adivinar y, si se filtra, abre todas las cuentas.", "Usa una frase larga y distinta para cada cuenta.")],
    T=[
        ("abc", "En seguridad informática: ¿qué es el phishing?", "Un mensaje falso que busca engañar para obtener claves, datos o dinero", "Un programa que acelera el computador", "Una copia de respaldo de los archivos", "El phishing es un engaño; las otras opciones son herramientas legítimas."),
        ("abc", "{F} ¿Cuál de los tres mensajes es el más probable que sea legítimo?", "El mensaje B, de un compañero conocido desde el correo de la empresa", "El mensaje A, que pide la clave en un enlace", "El mensaje C, que pide una transferencia secreta", "A y C tienen urgencia, piden claves o dinero y vienen de remitentes desconocidos; B viene de un compañero conocido por el canal de la empresa y no pide nada riesgoso."),
        ("abc", "{F} ¿Qué señal de alerta tiene el mensaje A?", "Urgencia y pedido de la clave en un enlace", "Un adjunto de la planilla de ventas", "Que viene desde el correo de la empresa", "Los pedidos de claves bajo presión son señales típicas del phishing."),
        ("abc", "{F} ¿Cuál de las contraseñas de ejemplo es la más segura?", "P3, la frase larga sin datos personales", "P1, 123456", "P2, sofia2008", "La frase larga es más difícil de adivinar que los números simples o el nombre con año."),
        ("abc", "{F} ¿Por qué la contraseña P1 es débil?", "Es corta y muy fácil de adivinar", "Porque tiene números", "Porque la usa mucha gente en la empresa", "Una secuencia corta es de las primeras que se prueban al intentar adivinar claves."),
        ("abc", "{F} Recibes el mensaje C. ¿Qué haces?", "No transfiero nada, verifico por otro medio con el gerente real y aviso a la jefatura", "Hago la transferencia para no demorar", "Respondo pidiendo más datos al número desconocido", "Las órdenes urgentes y secretas de dinero son una señal de fraude; se verifica por otro medio."),
        ("=", "Una oficina de ejemplo recibió 9 correos sospechosos por día durante 5 días. Cada día el filtro bloqueó 6. ¿Cuántos correos sospechosos llegaron a las bandejas en la semana?", "(9-6)*5", "Se calculan los correos que pasan el filtro cada día y se multiplican por los días.", " correos"),
        ("=", "Un trabajador pasa 8 horas frente a una pantalla y hace una pausa de 5 minutos por cada hora (valor de ejemplo). ¿Cuántos minutos de pausa suma en la jornada?", "8*5", "Se multiplican los minutos de pausa por las horas de la jornada.", " minutos"),
        ("abc", "¿Qué práctica de respaldo es correcta?", "Guardar copia de los archivos importantes en otro lugar y comprobar que se puedan abrir", "Guardar todo solo en el mismo computador", "Hacer el respaldo una vez y no revisarlo nunca", "Una copia en otro lugar protege si falla el equipo, y debe comprobarse."),
        ("abc", "{F} Un compañero comparte su clave: «Es solo para que me reemplaces un rato». ¿Qué observación corresponde?", "Las claves son personales; conviene pedir un acceso autorizado para quien reemplaza", "Está bien si es de confianza", "Compartir claves ayuda a trabajar más rápido sin problema", "Con claves compartidas no se sabe quién hizo qué ni se protege la información."),
        ("abc", "Un técnico fotografía con su celular una pantalla con datos de clientes y la sube a un grupo de mensajería. ¿Qué problema tiene?", "Expone datos personales de clientes sin autorización", "Ninguno, porque es un grupo de trabajo", "Que la foto sale borrosa", "Los datos de clientes son confidenciales y no deben difundirse."),
        ("abc", "Un teléfono de la empresa tiene hace semanas una actualización pendiente. ¿Qué conviene?", "Instalar las actualizaciones oficiales, porque corrigen fallas de seguridad", "Ignorarlas, porque «si funciona, no se toca»", "Desinstalar el antivirus", "Las actualizaciones corrigen fallas que los delincuentes pueden aprovechar."),
        ("=", "Una clave numérica de 4 dígitos tiene 10.000 combinaciones posibles. Una clave numérica de 6 dígitos tiene 1.000.000. ¿Cuántas veces más combinaciones tiene la de 6 dígitos?", "1000000//10000", "Se divide el número de combinaciones de la clave larga entre el de la clave corta.", " veces"),
    ],
    ctx=("abc", "{F} Llega a la bandeja el mensaje A y una compañera ya hizo clic en el enlace, pero no escribió su clave. ¿Qué hace?", "Avisa de inmediato a la jefatura o a quien administra los sistemas, para que revisen la cuenta", "No cuenta nada para no meterse en problemas", "Escribe la clave para comprobar si es real", "Avisar rápido permite proteger la cuenta y revisar si hay riesgos."),
    sc=[
        ("En seguridad digital: ¿qué es una contraseña segura?", "Una clave larga, única y sin datos personales", "Es mucho más difícil de adivinar."),
        ("¿Qué haces con un mensaje que pide tu clave?", "No respondo y aviso a la jefatura", "Las empresas serias no piden claves por mensaje."),
        ("En el mundo del trabajo: ¿para qué sirve un respaldo?", "Para no perder archivos si algo falla", "Una copia en otro lugar protege la información."),
    ],
    op=("Caso de ejemplo. En una clínica ficticia, la recepcionista recibe este correo: «Estimada: su equipo tiene un virus. Instale este programa ahora o perderá todos los archivos de pacientes. Responda con su clave de acceso. Soporte». El remitente no es del correo de la clínica. "
        "Escribe: (1) tres señales de que es un engaño, (2) qué harías paso a paso, (3) cómo es una contraseña segura, (4) por qué los datos de los pacientes deben cuidarse especialmente.",
        "(1) Urgencia, pide la clave, remitente que no es de la clínica. (2) No hago clic ni respondo, aviso a la jefatura o a quien administra los sistemas, y borro el mensaje cuando me lo indiquen. (3) Larga, única y sin datos personales. (4) Son datos de salud, privados y confidenciales: su difusión puede dañar a las personas.",
        ["identifica señales de engaño", "propone una acción segura", "describe una contraseña segura", "explica la privacidad de datos de salud"],
        ["hoja con cuatro respuestas"],
        ["entregar la clave", "instalar el programa", "no avisar a la jefatura"],
        "Pregunta: «¿qué pasaría si respondieras con la clave?». Debe decir que podrían entrar a la cuenta y ver datos de pacientes."),
    reinforce="Escribe tres consejos que darías a un compañero nuevo para usar el correo de la empresa de forma segura.",
    extend="Explica por qué la urgencia es una táctica común en los mensajes engañosos.",
)

# ============================================================ OAG-08, clase 2
F = ("Ficha 30 (planilla de ejemplo de una tienda, columnas A, B, C y D, filas 1 a 5). Fila 1, títulos: A1 «Producto», B1 «Cantidad», C1 «Precio unitario», D1 «Total». "
     "Fila 2: Cuaderno, 12, 1.500. Fila 3: Lápiz, 30, 300. Fila 4: Goma, 20, 250. Fila 5: Carpeta, 8, 2.000. La celda D2 lleva la fórmula «=B2*C2» (cantidad por precio), copiada hacia abajo en D3, D4 y D5. "
     "Nombre sugerido del archivo: «ventas_semana_03_v2».")
build(
    G8, 2, F,
    use="Aprenderé para qué sirven las herramientas de oficina (procesador de texto, planilla, presentación, correo y agenda) y a leer y razonar una planilla de cálculo en papel.",
    prior=["Conozco las TIC.", "Sé multiplicar y sumar.", "Sé leer una tabla con filas y columnas."],
    explain=[
        "Las herramientas de oficina sirven para producir y organizar información. El procesador de texto se usa para cartas, informes y documentos. La planilla de cálculo organiza datos en filas y columnas, y permite hacer cálculos automáticos con fórmulas. Una celda se nombra con su columna y su fila, por ejemplo B3. Una fórmula empieza con el signo igual (=) y usa referencias a celdas: «=B2*C2» multiplica lo que hay en B2 por lo que hay en C2.",
        "La ventaja de la fórmula es que, si cambias un dato, el resultado se actualiza solo. Las presentaciones sirven para exponer ideas con pocas palabras por diapositiva. El correo y la agenda ayudan a coordinar reuniones y plazos. Para trabajar ordenado, los archivos se guardan en carpetas con nombres claros que indiquen tema, fecha y versión, y se comparten en PDF cuando no deben modificarse.",
        "Todo esto se puede aprender sin software: en este cuaderno razonamos planillas escritas en el enunciado." + LIM,
    ],
    vocab=[("planilla de cálculo", "herramienta que organiza datos en filas y columnas y calcula con fórmulas"), ("celda", "cuadro donde se cruzan una columna y una fila, como B3"), ("fórmula", "expresión que empieza con = y calcula con datos de otras celdas"), ("PDF", "formato de archivo que se comparte sin que cambie su aspecto"), ("versión", "etapa de un documento que se va corrigiendo"), ("referencia", "nombre de una celda usado en una fórmula")],
    worked=[
        ("Leer una celda", "En una planilla de ejemplo, la fila 2 es: Taza, 10, 800. ¿Qué dato está en C2 si la columna C es «Precio»?", ["C2 es el cruce de la columna C y la fila 2.", "El tercer dato de la fila es 800."], "800"),
        ("Aplicar una fórmula", "Con la fórmula «=B2*C2» y los datos B2 = 6 y C2 = 500, ¿cuál es el resultado?", ["Se multiplica B2 por C2.", "6 × 500 = 3.000."], "3.000"),
    ],
    mistakes=[("Escribir el total a mano en una celda y no usar fórmula.", "Si cambian la cantidad o el precio, el total queda desactualizado.", "Usa una fórmula que calcule el total con las celdas."),
              ("Guardar un archivo como «final final ahora sí».", "Nadie sabe qué contiene ni cuál es la versión vigente.", "Usa nombres claros con tema, fecha y versión.")],
    T=[
        ("abc", "En ofimática: ¿para qué sirve una planilla de cálculo?", "Para ordenar datos en filas y columnas y calcular con fórmulas", "Para escribir cartas largas con imágenes", "Para enviar mensajes a los clientes", "La planilla organiza y calcula datos; escribir cartas es tarea del procesador de texto."),
        ("abc", "{F} ¿Qué dato está en la celda B3?", "30", "Lápiz", "300", "B3 es el cruce de la columna B (cantidad) y la fila 3; 300 es el precio y «Lápiz» es el producto."),
        ("abc", "{F} ¿Qué calcula la fórmula «=B2*C2»?", "La cantidad por el precio unitario de la fila 2", "La suma de todos los productos", "El nombre del producto", "La fórmula multiplica la cantidad por el precio de la misma fila."),
        ("=", "{F} ¿Cuál es el resultado de D2?", "12*1500", "Se multiplica la cantidad por el precio unitario de la fila 2.", " pesos"),
        ("=", "{F} ¿Cuál es el resultado de D4?", "20*250", "Se multiplica la cantidad por el precio unitario de la fila 4.", " pesos"),
        ("=", "{F} ¿Cuál es el total de ventas sumando D2, D3, D4 y D5?", "12*1500+30*300+20*250+8*2000", "Se calcula cada total de fila y se suman los cuatro resultados.", " pesos"),
        ("abc", "¿Cuál es un nombre de archivo claro para una planilla de ventas?", "ventas_semana_03_v2", "documento1", "final final ahora sí", "Un nombre claro dice el tema, la fecha o semana y la versión."),
        ("abc", "¿Por qué conviene guardar un informe en PDF antes de enviarlo a un cliente?", "Para que no cambie su aspecto y evitar modificaciones accidentales", "Para que pese más y se vea más profesional", "Para impedir que el cliente lo lea", "El PDF mantiene el formato original del documento."),
        ("=", "{F} Si el precio de la carpeta sube $500 y se venden las mismas 8 unidades, ¿cuánto aumenta el total de la fila 5?", "8*500", "El aumento es la cantidad vendida por lo que subió el precio.", " pesos"),
        ("abc", "{F} Un compañero escribe el total de la fila 2, 18.000, a mano en D2. ¿Qué desventaja tiene frente a la fórmula?", "Si cambian la cantidad o el precio, el total no se actualiza solo", "Ninguna, porque da el mismo número", "Que no se puede leer", "La fórmula se actualiza al cambiar los datos; el número escrito no."),
        ("abc", "Una diapositiva de ejemplo tiene 15 líneas de texto con letra pequeña. ¿Qué se recomienda?", "Pocas ideas clave por diapositiva, con letra legible, y explicarlas en voz alta", "Poner todo el informe en una sola diapositiva", "Agregar más texto para que no falte nada", "Una presentación apoya la explicación y no debe sobrecargarse de texto."),
        ("abc", "{F} ¿Qué ocurre si se elimina la columna B?", "Las fórmulas que usan B2, B3, B4 y B5 dejan de calcular bien", "No pasa nada porque los totales ya están calculados", "Se borra solo la columna A", "Las fórmulas dependen de las celdas de B y sin ellas no pueden calcular."),
        ("=", "{F} Se agrega una fila con 15 unidades a $1.200 cada una. ¿Cuál sería el nuevo total de ventas?", "12*1500+30*300+20*250+8*2000+15*1200", "Se suma al total anterior el producto de la nueva fila.", " pesos"),
    ],
    ctx=("abc", "{F} La encargada pide el informe de ventas para una reunión y quiere que nadie lo modifique, pero que todos lo lean. ¿Qué formato elige?", "Guardarlo en PDF con un nombre claro, por ejemplo «ventas_semana_03_v2»", "Enviar la planilla editable con un nombre cualquiera", "Imprimir y borrar el archivo", "El PDF evita cambios accidentales y el nombre claro facilita encontrarlo."),
    sc=[
        ("En una planilla de ejemplo: ¿cómo se llama una celda ubicada en la columna C y la fila 4?", "C4", "El nombre combina la columna y la fila."),
        ("En el mundo del trabajo: ¿con qué signo empieza una fórmula?", "Con el signo igual", "Así la planilla sabe que debe calcular."),
        ("¿Qué ventaja tiene una fórmula frente a un total escrito a mano?", "Se actualiza al cambiar los datos", "El resultado se recalcula automáticamente al cambiar los datos."),
    ],
    op=("Caso de ejemplo. Una panadería ficticia anota: Pan de molde, 20 unidades, $2.500 cada una; Queque, 10 unidades, $3.000 cada una; Galletas, 40 unidades, $500 cada una. "
        "Escribe: (1) la planilla en papel con sus columnas A, B, C y D y sus títulos, (2) la fórmula para la celda D2, (3) el total de cada fila y el total general, (4) un nombre de archivo claro y en qué formato lo compartirías con el dueño.",
        "(1) A «Producto», B «Cantidad», C «Precio unitario», D «Total»; filas 2 a 4 con los tres productos. (2) =B2*C2. (3) 50.000; 30.000; 20.000; total general 100.000. (4) «ventas_panaderia_01_v1», en PDF.",
        ["arma la planilla con títulos", "escribe la fórmula correcta", "calcula los totales", "elige nombre y formato"],
        ["hoja con la planilla y las respuestas"],
        ["fórmula sin signo igual", "totales mal calculados", "nombre de archivo sin versión"],
        "Pregunta: «¿qué cambia si el queque sube a $3.500?». Debe recalcular D3 como 35.000 y el total como 105.000."),
    reinforce="Dibuja una planilla de tres filas y tres columnas con datos de tu especialidad y escribe una fórmula que calcule una fila.",
    extend="Explica por qué una fórmula es mejor que escribir los resultados a mano cuando los datos pueden cambiar.",
)

# ============================================================ OAG-08, clase 3
F = ("Ficha 31 (tres resultados de búsqueda de ejemplo sobre «qué elementos de protección personal se usan en una bodega de ejemplo»). Resultado 1: página de una entidad fiscalizadora de ejemplo, con institución como autora, fecha de actualización reciente y referencia a la norma vigente. "
     "Resultado 2: blog anónimo, sin fecha, que dice «yo lo hago así desde hace años». Resultado 3: un foro donde alguien escribió «me dijeron que no hace falta».")
build(
    G8, 3, F,
    use="Aprenderé a buscar información en línea, a evaluar si una fuente es confiable, a citarla y a usar herramientas digitales o de inteligencia artificial con responsabilidad.",
    prior=["Sé usar un buscador.", "Sé qué es un dato personal.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Al buscar información para el trabajo, no todo lo que aparece es confiable. Para evaluar una fuente revisa quién es el autor o la institución, la fecha de actualización, si se apoya en normas o en evidencia, y si otras fuentes confiables dicen lo mismo. Una página oficial de una institución que explica la norma vigente es más confiable que un blog anónimo o que un comentario de un foro. Contrastar es comparar el dato con al menos otra fuente confiable.",
        "Los textos, las imágenes y las ideas tienen autores. Presentar como propio un texto ajeno es plagio. Para citar una fuente se indican el autor o la institución, el título y la fecha. Las herramientas de inteligencia artificial pueden ayudar a ordenar ideas, pero pueden equivocarse o inventar datos: lo que producen se verifica en fuentes confiables. Nunca se escriben en ellas datos personales ni información confidencial de la empresa sin autorización.",
        "En tareas con riesgo, la información en línea no reemplaza al instructor ni a la norma vigente." + LIM,
    ],
    vocab=[("fuente confiable", "texto o sitio con autor o institución identificable, fecha y respaldo en normas o evidencia"), ("contrastar", "comparar un dato con al menos otra fuente confiable"), ("plagio", "presentar como propio un texto o una idea de otra persona sin citarla"), ("cita", "mención del autor o la institución, el título y la fecha de una fuente"), ("inteligencia artificial", "programa que genera textos o respuestas y puede equivocarse"), ("desinformación", "información falsa que circula como si fuera verdadera")],
    worked=[
        ("Evaluar una fuente", "Un sitio de ejemplo no muestra autor, fecha ni referencias. ¿Es una fuente confiable?", ["Para ser confiable debe tener autoría, fecha y respaldo.", "Este sitio no tiene ninguno."], "No, es poco confiable"),
        ("Contar fuentes", "Un equipo de ejemplo revisó 10 fuentes y descartó 4 por no ser confiables. ¿Cuántas quedaron?", ["Se resta lo descartado al total.", "10 − 4 = 6."], "6 fuentes"),
    ],
    mistakes=[("Copiar un párrafo de internet en el informe sin indicar de dónde viene.", "Es plagio y además no se sabe si la información es confiable.", "Redacta con tus palabras y cita la fuente."),
              ("Aceptar una cifra dada por una herramienta de inteligencia artificial sin comprobarla.", "Puede estar equivocada o inventada.", "Verifica el dato en una fuente confiable.")],
    T=[
        ("abc", "En búsqueda de información: ¿qué ayuda a evaluar una fuente?", "Saber quién la escribió, su fecha y en qué se apoya", "Que aparezca primera en el buscador", "Que tenga muchas imágenes", "Autor, fecha y respaldo permiten juzgar su confiabilidad; la posición en el buscador no."),
        ("abc", "{F} ¿Cuál resultado es el más confiable?", "El resultado 1, de una entidad fiscalizadora", "El resultado 2, del blog anónimo", "El resultado 3, del foro", "Solo el resultado 1 tiene institución autora, fecha reciente y referencia a la norma."),
        ("abc", "{F} ¿Por qué el resultado 2 es poco confiable?", "No tiene autor ni fecha y no se apoya en una norma", "Porque es un blog y los blogs siempre mienten", "Porque es demasiado breve", "No poder identificar quién escribe ni cuándo hace imposible comprobar el contenido."),
        ("abc", "{F} ¿Por qué el resultado 3 no sirve como evidencia?", "Es una opinión sin respaldo de una fuente identificable", "Porque está en un foro público", "Porque está escrito de manera coloquial", "«Me dijeron» no identifica quién lo dijo ni en qué se basa."),
        ("abc", "¿Qué es el plagio?", "Presentar como propio un texto o idea de otra persona sin citarla", "Citar bien a un autor", "Resumir con palabras propias y mencionar la fuente", "El plagio consiste en no reconocer la autoría ajena."),
        ("abc", "¿Qué datos se indican al citar una fuente?", "Autor o institución, título y fecha", "Solo el color de la página", "El nombre del buscador usado", "La cita permite a otros encontrar y comprobar la fuente."),
        ("=", "Un informe de ejemplo tiene 20 frases y 5 fueron copiadas sin citar. ¿Cuántas son propias o están bien citadas?", "20-5", "Al total de frases se le restan las copiadas sin citar.", " frases"),
        ("=", "Un equipo de ejemplo revisó 12 fuentes: 3 eran de instituciones, 4 eran anónimas y las demás tenían autor identificado. ¿Cuántas tenían autor identificado?", "12-3-4", "Al total se le restan las institucionales y las anónimas.", " fuentes"),
        ("abc", "Un dato importante aparece en una sola página. ¿Qué conviene hacer?", "Contrastarlo con al menos otra fuente confiable", "Usarlo igual porque salió en la búsqueda", "Preguntar a un desconocido en redes", "Contrastar reduce el riesgo de usar un dato falso."),
        ("abc", "Una compañera dice: «Lo dijo la inteligencia artificial, entonces es verdad». ¿Qué respuesta es correcta?", "Puede equivocarse o inventar datos; hay que verificar en una fuente confiable", "Tiene razón: la inteligencia artificial nunca se equivoca", "Solo hay que verificar si el dato es largo", "Estas herramientas pueden generar errores presentados con seguridad."),
        ("abc", "Un asistente quiere pegar en una herramienta en línea un texto con datos de clientes para que lo resuma. ¿Qué hace?", "Verifica si la empresa lo autoriza y quita los datos personales antes", "Lo pega completo, para ahorrar tiempo", "Lo pega y luego borra el historial", "Los datos de clientes son confidenciales y requieren autorización y cuidado."),
        ("abc", "{F} Un trabajador usa el resultado 1 para escribir un instructivo de uso de elementos de protección. ¿Qué es lo más adecuado?", "Citar la página oficial y consultar al instructor y la norma vigente antes de aplicar nada", "Copiar el texto sin cita y empezar a usar lo escrito", "Confiar solo en el blog porque es práctico", "En temas de seguridad la lectura se complementa con instructor y norma vigente."),
        ("=", "Verificar cada fuente toma 15 minutos y se verifican 4 fuentes. ¿Cuántos minutos en total?", "15*4", "Se multiplica el tiempo por fuente por la cantidad de fuentes.", " minutos"),
    ],
    ctx=("abc", "{F} Debes explicar a tu equipo, en una nota, cómo elegiste la fuente para un tema. ¿Qué escribes?", "«Elegí el resultado 1 porque la institución es la autora, está actualizado y se basa en la norma vigente»", "«Elegí el primero que apareció»", "«Elegí el más breve»", "Justificar con autoría, fecha y respaldo muestra criterio para evaluar fuentes."),
    sc=[
        ("En búsqueda de información: ¿qué significa contrastar un dato?", "Compararlo con otra fuente confiable", "Permite detectar errores o datos falsos."),
        ("¿Qué datos incluyes al citar?", "Autor o institución, título y fecha", "Así otros pueden encontrar la fuente."),
        ("¿Qué haces con un dato que entrega una inteligencia artificial?", "Lo verifico en una fuente confiable", "Estas herramientas pueden equivocarse o inventar."),
    ],
    op=("Caso de ejemplo. Debes preparar una nota para tus compañeros de cocina de un casino ficticio sobre el almacenamiento seguro de alimentos. Encuentras tres resultados: (1) una página de una entidad de salud de ejemplo, con fecha reciente y referencia a la norma vigente; (2) un video de un cocinero sin datos de autor; (3) un comentario anónimo en una red social. "
        "Escribe: (1) cuál fuente usarías y por qué, (2) cómo citarla, (3) qué harías antes de dar la nota por buena, (4) qué no pondrías nunca en una herramienta de inteligencia artificial.",
        "(1) La 1, por institución autora, fecha y norma. (2) Institución de ejemplo, título de la página y fecha. (3) Contrastar con otra fuente confiable y consultar con la jefa de cocina. (4) Datos personales de las personas o información confidencial de la empresa.",
        ["elige una fuente con criterios", "cita con los tres datos", "propone contrastar", "reconoce límites de privacidad"],
        ["hoja con cuatro respuestas"],
        ["elegir la fuente por comodidad", "no citar", "olvidar la privacidad"],
        "Pregunta: «¿qué harías si dos fuentes confiables se contradicen?». Debe proponer consultar a la jefa o al instructor y a la norma vigente."),
    reinforce="Elige un tema de tu especialidad y escribe dos preguntas que harías para saber si una página es confiable.",
    extend="Explica por qué un dato sin fuente identificable es difícil de comprobar.",
)

# ============================================================ OAG-08, clase 4
F = ("Ficha 32 (carpetas de la oficina de una empresa ficticia, tamaños de ejemplo). Contratos 600 MB; Fotos del local 1.500 MB; Planillas 300 MB; Informes 200 MB. "
     "Dispositivos de respaldo: un disco externo de 4.000 MB y un espacio en línea contratado de 1.000 MB. Regla de la empresa (ejemplo): los archivos con datos personales de clientes se guardan solo en el espacio autorizado, con acceso restringido.")
build(
    G8, 4, F,
    use="Aprenderé a planificar un respaldo de archivos con datos de tamaño y capacidad, y a cuidar los datos personales al usar dispositivos y servicios en línea.",
    prior=["Conozco el respaldo y la privacidad.", "Sé sumar y restar cantidades grandes.", "Sé qué es un dispositivo de almacenamiento."],
    explain=[
        "Un plan de respaldo decide qué archivos se copian, dónde, con qué frecuencia y cómo se comprueba. Primero se calcula el tamaño de lo que se debe copiar, sumando el tamaño de las carpetas. El tamaño de los archivos se mide en unidades como el MB (megabyte). Luego se compara con la capacidad del dispositivo: la diferencia indica si cabe todo y cuánto espacio sobra o falta.",
        "Una buena práctica es no guardar la copia en el mismo lugar que el original, porque un robo, un incendio o una falla podrían destruir ambos. También se comprueba periódicamente que la copia se pueda abrir. Los archivos con datos personales requieren más cuidado: solo se guardan en lugares autorizados, con acceso restringido, y no se copian a dispositivos personales sin permiso.",
        "Los respaldos son parte de la responsabilidad profesional: si se pierde información de clientes, el daño puede ser grande." + LIM,
    ],
    vocab=[("plan de respaldo", "decisión de qué archivos copiar, dónde, cada cuánto y cómo comprobar"), ("MB", "megabyte, unidad para medir el tamaño de los archivos"), ("capacidad", "cantidad máxima de archivos que cabe en un dispositivo"), ("acceso restringido", "acceso solo para personas autorizadas"), ("dispositivo personal", "equipo que pertenece a una persona y no a la empresa")],
    worked=[
        ("Calcular tamaño total", "Tres carpetas de ejemplo pesan 400, 250 y 150 MB. ¿Cuánto pesan en total?", ["Se suman los tamaños.", "400 + 250 + 150 = 800."], "800 MB"),
        ("Calcular espacio libre", "Un disco de ejemplo de 2.000 MB tiene 800 MB ocupados. ¿Cuánto espacio libre queda?", ["Se resta lo ocupado a la capacidad.", "2.000 − 800 = 1.200."], "1.200 MB"),
    ],
    mistakes=[("Guardar la copia de respaldo en el mismo escritorio y al lado del computador.", "Si hay un robo o un incendio, se pierde todo junto.", "Guarda la copia en otro lugar autorizado."),
              ("Copiar archivos con datos de clientes a un pendrive personal para avanzar en casa.", "Puede perderse o filtrarse y no está autorizado.", "Usa solo los espacios autorizados por la empresa.")],
    T=[
        ("=", "{F} ¿Cuántos MB suman en total las cuatro carpetas?", "600+1500+300+200", "Se suman los tamaños de las cuatro carpetas.", " MB"),
        ("=", "{F} Solo para calcular el espacio: si se copiara todo en el disco externo, ¿cuántos MB sobrarían?", "4000-(600+1500+300+200)", "A la capacidad del disco se le resta el tamaño total.", " MB"),
        ("abc", "{F} ¿Cabe todo el contenido en el espacio en línea?", "No, porque faltaría espacio", "Sí, porque 1.000 MB alcanzan para todo", "Sí, si se borran los informes", "El total pasa de 2.600 MB y el espacio en línea tiene 1.000 MB."),
        ("=", "{F} ¿Cuántos MB faltarían en el espacio en línea para guardar todo?", "(600+1500+300+200)-1000", "Al tamaño total se le resta la capacidad del espacio en línea.", " MB"),
        ("abc", "{F} ¿Qué carpetas caben juntas en el espacio en línea?", "Contratos y Planillas, que suman 900 MB", "Contratos y Fotos, que suman 2.100 MB", "Fotos y Planillas, que suman 1.800 MB", "Solo Contratos y Planillas suman menos de 1.000 MB."),
        ("abc", "{F} Los contratos incluyen datos personales de clientes. ¿Dónde se guardan según la regla?", "Solo en el espacio autorizado, con acceso restringido", "En el pendrive de la gerente", "En el correo personal de cada trabajador", "La regla de la empresa limita los datos personales a un lugar autorizado."),
        ("=", "{F} Si las fotos del local se comprimen a la mitad, ¿cuántos MB ocuparían?", "1500//2", "Se divide el tamaño original entre dos.", " MB"),
        ("abc", "¿Cada cuánto conviene hacer el respaldo?", "Con una frecuencia acordada según qué tan seguido cambian los archivos, y comprobando que se puedan abrir", "Una sola vez al comenzar", "Solo cuando se pierde algo", "Un respaldo útil es regular y se verifica."),
        ("=", "{F} Se hace un respaldo semanal de la carpeta Contratos durante 4 semanas y cada copia ocupa 600 MB. ¿Cuántos MB ocupan las 4 copias?", "600*4", "Se multiplica el tamaño de una copia por el número de copias.", " MB"),
        ("abc", "Una persona deja el disco de respaldo en el mismo cajón que el computador. ¿Qué riesgo hay?", "Si hay un robo o un incendio, se pierden el original y la copia", "Ninguno, porque está cerca y es cómodo", "Que el disco se llene antes", "Guardar la copia en otro lugar protege ante daños del lugar de trabajo."),
        ("abc", "Al comprobar un respaldo, se descubre que no se puede abrir. ¿Qué corresponde?", "Avisar y repetir el respaldo", "Seguir sin decir nada, porque «para eso es el respaldo»", "Borrar el original para ahorrar espacio", "Un respaldo que no se abre no protege; se avisa y se rehace."),
        ("abc", "{F} Un colega pide copiar la carpeta Contratos a su pendrive personal para avanzar en casa. ¿Qué corresponde?", "No hacerlo sin autorización: la regla exige guardar datos personales solo en el espacio autorizado", "Hacerlo, porque es solo por un día", "Hacerlo y borrarla después en secreto", "Los datos personales no se llevan a dispositivos personales sin autorización."),
        ("=", "{F} El disco externo tiene 2.600 MB ocupados con todo el respaldo y la información crece 200 MB por mes. ¿En cuántos meses se llenará el disco?", "(4000-2600)//200", "Se calcula el espacio libre y se divide entre lo que crece cada mes.", " meses"),
    ],
    ctx=("abc", "{F} A fin de mes, la encargada revisa el respaldo y nota que el disco externo está en el mismo escritorio que el computador. ¿Qué mejora propone?", "Guardarlo en otro lugar seguro y autorizado y comprobar periódicamente que se pueda abrir", "Dejarlo igual porque es cómodo", "Prestarlo a un trabajador para llevarlo a casa", "Separar la copia del original reduce el riesgo de perder ambos."),
    sc=[
        ("En un plan de respaldo de ejemplo: ¿cómo calculas si todo cabe en un disco?", "Sumo los tamaños y los comparo con la capacidad", "Así se sabe si sobra o falta espacio."),
        ("¿Dónde se guardan los archivos con datos de clientes?", "Solo en el espacio autorizado", "Los datos personales requieren acceso restringido."),
        ("¿Por qué no guardar la copia junto al original?", "Porque un daño podría perder ambos", "La separación protege ante robos o incendios."),
    ],
    op=("Caso de ejemplo. Una escuela de oficios ficticia debe respaldar: Matrículas 500 MB (con datos personales), Material de clases 1.200 MB, Fotos de eventos 900 MB y Registros de notas 400 MB (con datos personales). Tiene un disco de 3.000 MB y un espacio autorizado en línea de 1.000 MB. Regla de ejemplo: los datos personales se guardan solo en el espacio autorizado. "
        "Escribe: (1) el tamaño total, (2) cuántos MB sobran en el disco si guarda todo allí, (3) qué carpetas irían al espacio autorizado y si caben, (4) una medida para comprobar el respaldo.",
        "(1) 500 + 1.200 + 900 + 400 = 3.000 MB. (2) 3.000 − 3.000 = 0 MB: el disco queda justo lleno. (3) Matrículas y Registros de notas (900 MB), que caben en 1.000 MB. (4) Abrir una muestra de archivos cada mes para comprobar que se leen.",
        ["suma bien los tamaños", "compara con la capacidad", "aplica la regla de datos personales", "propone una comprobación"],
        ["hoja con cuatro respuestas"],
        ["guardar datos personales en el disco general", "no comparar con la capacidad", "no comprobar el respaldo"],
        "Pregunta: «¿qué harías si el disco queda lleno?». Debe proponer comprimir, depurar archivos innecesarios o ampliar la capacidad con autorización."),
    reinforce="Escribe una lista de cuatro tipos de archivo de tu especialidad y marca cuáles tienen datos personales.",
    extend="Explica por qué es importante comprobar que un respaldo se pueda abrir antes de necesitarlo.",
)

# ============================================================ OAG-09, clase 1
F = ("Ficha 33 (compra y uso de verduras en la cocina de un casino de ejemplo). Se compraron 100 kg de verduras. Al prepararlas quedaron 12 kg de cáscaras y partes no comestibles (merma) y 5 kg se echaron a perder por mala conservación (desperdicio); el resto se usó en los platos. "
     "Precio de ejemplo: $800 por kg.")
build(
    G9, 1, F,
    use="Aprenderé a usar los insumos de forma eficiente: distinguir merma y desperdicio, calcular su costo y proponer medidas para reducirlos.",
    prior=["Sé multiplicar y restar enteros.", "Conozco unidades como el kilogramo.", "Sé que los recursos tienen un costo."],
    explain=[
        "Los insumos son los materiales, el agua, la energía y otros recursos que se usan para producir un bien o prestar un servicio. Usarlos de forma eficiente significa usar la cantidad necesaria, evitar pérdidas y aprovechar lo que sirve. Eso ahorra dinero y reduce el impacto ambiental, porque cada insumo desperdiciado implica recursos y energía que se gastaron sin necesidad.",
        "La merma es la pérdida natural de un proceso, como las cáscaras al preparar verduras. El desperdicio es la pérdida evitable, como un producto que se echa a perder por mala conservación o por comprar de más. La merma se calcula y se considera en la planificación; el desperdicio se reduce con medidas como planificar las compras, almacenar según la etiqueta, usar primero lo que se compró antes, controlar las porciones y revisar los registros de consumo con frecuencia.",
        "Registrar lo que se usa y lo que se pierde permite detectar problemas a tiempo y tomar decisiones con datos." + LIM,
    ],
    vocab=[("insumo", "material, agua, energía u otro recurso que se usa para producir o prestar un servicio"), ("uso eficiente", "usar la cantidad necesaria, evitando pérdidas"), ("merma", "pérdida natural de un proceso"), ("desperdicio", "pérdida evitable de insumos"), ("rotación de productos", "usar primero lo que se compró antes"), ("registro de consumo", "anotación de lo que se usa y lo que se pierde")],
    worked=[
        ("Distinguir merma y desperdicio", "En una panadería de ejemplo, la harina que se queda pegada en el mesón al amasar es inevitable, y un saco que se humedeció por estar mal guardado se perdió. ¿Cuál es merma y cuál es desperdicio?", ["Lo inevitable del proceso es merma.", "Lo que se pierde por mal almacenamiento es desperdicio evitable."], "La harina pegada es merma; el saco humedecido es desperdicio"),
        ("Calcular el costo de una pérdida", "Un ingrediente de ejemplo cuesta $600 el kilo y se perdieron 4 kg. ¿Cuánto dinero se perdió?", ["Se multiplica el precio por los kilos perdidos.", "600 × 4 = 2.400."], "$2.400"),
    ],
    mistakes=[("Comprar el doble «por si acaso».", "Aumenta el riesgo de que los productos se echen a perder y se pierda dinero.", "Planifica las compras según el consumo real."),
              ("Llamar «merma» a todo lo que se pierde.", "Así se normaliza un desperdicio que sí se podría evitar.", "Separa lo inevitable (merma) de lo evitable (desperdicio) y actúa sobre este último.")],
    T=[
        ("abc", "En uso eficiente de recursos: ¿qué son los insumos?", "Materiales, agua, energía y otros recursos que se usan para producir o dar un servicio", "Solo el dinero que gasta la empresa", "Los productos terminados que se venden", "Insumo es todo recurso que entra al proceso; el producto terminado es lo que sale."),
        ("abc", "{F} ¿Qué parte es merma?", "Los 12 kg de cáscaras y partes no comestibles", "Los 5 kg echados a perder", "Los kg usados en los platos", "La merma es la pérdida natural del proceso, como las cáscaras."),
        ("abc", "{F} ¿Qué parte es un desperdicio evitable?", "Los 5 kg echados a perder por mala conservación", "Los 12 kg de cáscaras", "Los 100 kg comprados", "El desperdicio es la pérdida que se podría haber evitado almacenando bien."),
        ("=", "{F} ¿Cuántos kg de verduras se usaron en los platos?", "100-12-5", "Al total comprado se le restan la merma y el desperdicio.", " kg"),
        ("=", "{F} ¿Cuántos pesos costó la compra de las verduras?", "100*800", "Se multiplica el precio por kg por los kg comprados.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se perdieron por el desperdicio?", "5*800", "Se multiplican los kg desperdiciados por el precio por kg.", " pesos"),
        ("abc", "¿Qué medida reduce el desperdicio por mala conservación?", "Almacenar según la etiqueta y usar primero lo que se compró antes", "Comprar mayor cantidad para tener de sobra", "Guardar todo mezclado para ahorrar espacio", "La rotación de productos y el almacenamiento correcto evitan que se echen a perder."),
        ("=", "{F} Si con mejor conservación el desperdicio baja de 5 kg a 1 kg en cada compra, ¿cuántos pesos se ahorran en 4 compras?", "(5-1)*800*4", "Se calcula la reducción de kg por compra y se multiplica por el precio y las compras.", " pesos"),
        ("abc", "Un cocinero de ejemplo sirve siempre porciones más grandes que lo planificado «por si acaso». ¿Qué problema genera?", "Aumenta el consumo de insumos, el costo y el desperdicio", "Ninguno, porque el cliente queda más contento", "Reduce el costo del plato", "Servir más de lo necesario gasta insumos sin beneficio planificado."),
        ("abc", "{F} Un compañero dice: «Toda pérdida de verduras es culpa del cocinero». ¿Qué respuesta es correcta?", "Parte de la pérdida es natural (cáscaras); lo evitable es el desperdicio, que se reduce planificando y conservando bien", "Tiene razón: nada se puede evitar", "Nada se puede considerar natural", "Distinguir merma y desperdicio permite actuar sobre lo evitable."),
        ("abc", "Un taller de gráfica de ejemplo usa solo una cara de las hojas de borrador. ¿Qué medida de uso eficiente corresponde?", "Reutilizar el reverso de las hojas para borradores", "Comprar el doble de hojas", "Botar las hojas usadas por una cara", "Reutilizar permite aprovechar un insumo ya comprado."),
        ("abc", "Una empresa de ejemplo registra el consumo de insumos una sola vez al año. ¿Qué problema tiene?", "Detecta los desperdicios muy tarde; conviene registrar con frecuencia", "Ninguno, porque anotar más a menudo es una pérdida de tiempo", "Que el registro del año queda más corto", "Un registro periódico permite corregir a tiempo."),
        ("=", "{F} Con mejor planificación se compran 95 kg, la merma sigue siendo de 12 kg y no hay desperdicio. ¿Cuántos kg se usan en los platos?", "95-12", "A lo comprado se le resta solo la merma natural.", " kg"),
    ],
    ctx=("abc", "{F} La jefa de cocina quiere bajar el desperdicio y pide una propuesta con datos. ¿Cuál es la mejor?", "Medir el desperdicio cada semana, ajustar las compras y usar primero lo almacenado antes", "Comprar más para que nunca falte", "Dejar de registrar para ahorrar tiempo", "Medir, ajustar compras y rotar productos ataca directamente el desperdicio."),
    sc=[
        ("En uso eficiente de recursos: ¿qué es el desperdicio?", "Una pérdida evitable de insumos", "Se puede reducir con planificación y buena conservación."),
        ("En el mundo del trabajo: ¿qué es la merma?", "Una pérdida natural del proceso", "Es inevitable, aunque se puede medir y planificar."),
        ("¿Para qué sirve registrar el consumo de insumos?", "Para detectar pérdidas a tiempo", "Los datos permiten corregir antes de que el costo crezca."),
    ],
    op=("Caso de ejemplo. Una lavandería ficticia compra 200 litros de detergente líquido al mes. Se usan 170 litros en lavados, 10 litros se derraman al llenar los recipientes por apuro y 20 litros quedan con la fecha vencida. El litro cuesta $1.500 (valor de ejemplo). "
        "Escribe: (1) cuántos litros se desperdician, (2) cuánto dinero se pierde, (3) dos medidas para reducir el desperdicio, (4) qué registrarías cada semana.",
        "(1) 10 + 20 = 30 litros. (2) 30 × 1.500 = 45.000 pesos. (3) Comprar según el consumo real y usar primero lo más antiguo; usar medidas o dosificadores para evitar derrames. (4) Litros usados, litros perdidos y fechas de vencimiento.",
        ["calcula el desperdicio", "calcula el dinero perdido", "propone medidas concretas", "define un registro útil"],
        ["hoja con cuatro respuestas"],
        ["llamar merma a todo", "no calcular el costo", "proponer medidas vagas"],
        "Pregunta: «¿qué harías si el detergente vencido fuera peligroso para la piel?». Debe decir que no se manipula sin instrucciones, que se consulta a la persona encargada y que se sigue la norma vigente."),
    reinforce="Elige un insumo de tu especialidad y escribe una pérdida natural, una evitable y una medida para reducir la evitable.",
    extend="Explica por qué reducir el desperdicio ahorra dinero y también ayuda al ambiente.",
)

# ============================================================ OAG-09, clase 2
F = ("Ficha 34 (registro semanal de residuos de un centro de salud familiar ficticio; solo conceptos y cantidades de ejemplo). Residuos orgánicos (restos de comida): 40 kg. Papel y cartón limpio: 25 kg. Plásticos y envases limpios: 15 kg. "
     "Residuos peligrosos o especiales (por ejemplo, pilas, aceites usados o materiales con riesgo biológico): 6 kg. Residuos comunes no reciclables: 30 kg. "
     "Regla del centro: los residuos peligrosos se separan, se rotulan, se guardan en un lugar autorizado y los retira una empresa autorizada; no se mezclan con los comunes.")
build(
    G9, 2, F,
    use="Aprenderé a clasificar residuos, la jerarquía reducir-reutilizar-reciclar y por qué los residuos peligrosos requieren manejo autorizado.",
    prior=["Conozco el uso eficiente de insumos.", "Sé sumar enteros.", "Sé qué es reciclar."],
    explain=[
        "Los residuos son los materiales que quedan después de usar un producto o realizar una actividad. Se clasifican en orgánicos (restos de comida), reciclables (papel, cartón, vidrio, metal y plásticos limpios), comunes no reciclables y peligrosos o especiales, como pilas, aceites usados, productos químicos o materiales con riesgo biológico. Separar los residuos en el lugar donde se generan se llama separación en origen y facilita reciclar.",
        "La jerarquía para manejar los residuos pone primero reducir lo que se genera, luego reutilizar, después reciclar y valorizar (aprovechar el residuo como recurso, por ejemplo compostar los orgánicos) y, al final, la disposición final en un lugar autorizado. Los residuos peligrosos exigen un manejo especial según la norma vigente: solo los manipula personal capacitado y autorizado, se rotulan, se guardan en lugares autorizados y los retira una empresa autorizada. Nunca se mezclan con residuos comunes ni se vierten por el desagüe.",
        "Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente (por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar." + LIM,
    ],
    vocab=[("residuo", "material que queda después de usar un producto o hacer una actividad"), ("separación en origen", "separar los residuos donde se generan"), ("reducir", "generar menos residuos"), ("reutilizar", "volver a usar un objeto con el mismo u otro fin"), ("reciclar", "convertir un residuo en un material nuevo"), ("valorizar", "aprovechar un residuo como recurso"), ("residuo peligroso", "residuo que puede dañar a las personas o al ambiente")],
    worked=[
        ("Clasificar residuos", "En una cocina de ejemplo se juntan cáscaras de fruta y una botella plástica limpia. ¿Cómo se clasifica cada una?", ["La cáscara es un residuo orgánico.", "La botella limpia es reciclable."], "Cáscara: orgánico; botella: reciclable"),
        ("Total de residuos", "Una oficina de ejemplo genera 18 kg de papel y 7 kg de residuos comunes. ¿Cuántos kg suman?", ["Se suman las cantidades.", "18 + 7 = 25."], "25 kg"),
    ],
    mistakes=[("Mezclar pilas usadas con la basura común «para ahorrar bolsas».", "Los residuos peligrosos pueden contaminar y dañar a las personas.", "Sepáralas y entrégalas a la persona encargada para su manejo autorizado."),
              ("Botar un líquido desconocido por el desagüe.", "Puede contaminar el agua y reaccionar de forma peligrosa.", "No lo manipules: consulta la etiqueta y avisa a la persona encargada.")],
    T=[
        ("abc", "{F} ¿Qué tipo de residuo es el más abundante en la semana?", "Los orgánicos, con 40 kg", "Los comunes, con 30 kg", "El papel y cartón, con 25 kg", "La ficha indica 40 kg de orgánicos, la mayor cantidad."),
        ("=", "{F} ¿Cuántos kg de residuos se generaron en total en la semana?", "40+25+15+6+30", "Se suman las cinco categorías de la ficha.", " kg"),
        ("=", "{F} ¿Cuántos kg corresponden a residuos reciclables limpios (papel y cartón más plásticos y envases)?", "25+15", "Se suman las dos categorías reciclables.", " kg"),
        ("abc", "{F} ¿Cuál de estos es un residuo peligroso o especial según la ficha?", "Las pilas", "Los restos de comida", "El papel limpio", "La ficha menciona pilas, aceites usados y materiales con riesgo biológico como especiales."),
        ("abc", "En la jerarquía de manejo de residuos, ¿qué se hace primero?", "Reducir lo que se genera", "Reciclar todo lo que se genere", "Eliminar todo en un relleno", "Lo mejor es generar menos residuos antes de pensar en reciclar."),
        ("abc", "Una cocina de ejemplo bota restos de comida y botellas plásticas limpias en el mismo tacho. ¿Qué falla tiene?", "No hace separación en origen, por lo que se pierde material reciclable", "Usa un tacho demasiado grande", "Bota demasiado pocos residuos", "Mezclar residuos impide reciclar y complica el manejo."),
        ("=", "{F} ¿Cuántos kg de residuos no son peligrosos?", "40+25+15+30", "Se suman todas las categorías, excepto la de residuos peligrosos.", " kg"),
        ("=", "{F} Si el centro reduce el papel en 6 kg por semana durante 4 semanas, ¿cuántos kg en total deja de generar?", "6*4", "Se multiplica la reducción semanal por las semanas.", " kg"),
        ("abc", "¿Quién debe manipular residuos peligrosos?", "Personal capacitado y autorizado, según la norma vigente", "Cualquier persona que esté cerca", "Quien tenga más tiempo libre", "Los residuos peligrosos exigen formación y autorización."),
        ("abc", "{F} Un auxiliar nuevo mezcla pilas con la basura común «para ahorrar bolsas». ¿Qué problema genera?", "Pueden contaminar y dañar a personas; deben separarse y entregarse a una empresa autorizada", "Ninguno, porque son pocas pilas", "Que se llenen más rápido las bolsas", "Los residuos peligrosos tienen reglas de manejo para evitar daños."),
        ("abc", "¿Qué significa reutilizar?", "Volver a usar un objeto con el mismo u otro fin sin transformarlo", "Convertir un residuo en material nuevo", "Botar un objeto a un relleno", "Reutilizar prolonga la vida del objeto; reciclar lo transforma."),
        ("abc", "Un compañero propone verter por el desagüe un líquido de limpieza que no reconoce. ¿Qué corresponde?", "No hacerlo: consultar la etiqueta y avisar a la persona encargada", "Hacerlo con mucha agua para diluirlo", "Mezclarlo con otro líquido para neutralizarlo", "Un producto desconocido no se manipula ni se mezcla: se consulta con quien corresponde."),
        ("=", "{F} Si se valorizan 80 de cada 100 kg de residuos orgánicos, ¿cuántos kg se aprovechan?", "40*80//100", "Se aplica la proporción de aprovechamiento a los kg orgánicos.", " kg"),
    ],
    ctx=("abc", "{F} La encargada del centro pide un cartel simple para el patio con tres tachos: orgánicos, reciclables y comunes. Un auxiliar pregunta dónde van las pilas. ¿Qué responde?", "Que no van en ninguno de esos tachos: se entregan a la persona encargada de residuos peligrosos", "Que van en el tacho de reciclables", "Que van en el tacho común", "Las pilas son residuos peligrosos y tienen un manejo autorizado aparte."),
    sc=[
        ("En manejo de residuos: ¿qué es la separación en origen?", "Separar los residuos donde se generan", "Facilita reciclar y evita mezclas peligrosas."),
        ("¿Qué se hace primero en la jerarquía de residuos?", "Reducir lo que se genera", "Es la opción que más recursos ahorra."),
        ("¿Quién retira los residuos peligrosos?", "Una empresa autorizada", "Su manejo y su destino final están regulados."),
    ],
    op=("Caso de ejemplo. Un taller de confección ficticio genera en una semana: 20 kg de retazos de tela limpios, 8 kg de papel, 5 kg de restos de comida de la colación, 2 kg de envases de productos de limpieza vacíos con la etiqueta de advertencia y 10 kg de residuos comunes. "
        "Escribe: (1) cuántos kg se generan en total, (2) cómo clasificarías cada grupo, (3) una medida para reducir y una para reutilizar, (4) qué harías con los envases de productos de limpieza vacíos.",
        "(1) 20 + 8 + 5 + 2 + 10 = 45 kg. (2) Retazos limpios: reutilizables o reciclables según el taller; papel: reciclable; restos de comida: orgánicos; envases con advertencia: peligrosos o especiales; residuos comunes: no reciclables. (3) Reducir: aprovechar mejor el corte; reutilizar: usar retazos para otros trabajos. (4) No los mezclo ni los boto: los entrego a la persona encargada para su manejo autorizado.",
        ["suma los kg", "clasifica cada grupo", "propone reducir y reutilizar", "reconoce el manejo especial de envases con advertencia"],
        ["hoja con cuatro respuestas"],
        ["mezclar residuos peligrosos con comunes", "no sumar bien", "proponer medidas vagas"],
        "Pregunta: «¿qué pasaría si los envases se botan en el tacho común?». Debe mencionar riesgo de daño y contaminación y la necesidad de manejo autorizado."),
    reinforce="Haz una lista de cinco residuos de tu especialidad y clasifícalos en orgánicos, reciclables, comunes o peligrosos.",
    extend="Explica con un ejemplo por qué reducir es mejor que reciclar en la jerarquía de residuos.",
)

# ============================================================ OAG-09, clase 3
F = ("Ficha 35 (equipos de una oficina ficticia, datos de ejemplo). Ampolletas: 10 unidades de 20 W, encendidas 10 horas al día. Computadores: 5 unidades de 100 W, encendidos 8 horas al día. Estufa: 1 unidad de 1.500 W, 4 horas al día. "
     "Fórmula de ejemplo: energía en kWh = potencia total en W × horas ÷ 1.000. Precio de ejemplo: $150 por kWh.")
build(
    G9, 3, F,
    use="Aprenderé qué es la eficiencia energética, a calcular el consumo de energía de equipos con potencia y horas, y a proponer medidas seguras de ahorro.",
    prior=["Sé multiplicar y dividir enteros.", "Sé qué es la electricidad en el trabajo.", "Sé que no se manipulan instalaciones eléctricas sin autorización."],
    explain=[
        "La eficiencia energética es lograr el mismo resultado con menos energía. Todo equipo eléctrico tiene una potencia, que se mide en watts (W) y dice cuánta energía usa por unidad de tiempo. La energía consumida se mide en kilowatts-hora (kWh): se calcula multiplicando la potencia en W por las horas de uso y dividiendo por 1.000. Por ejemplo, un equipo de 2.000 W encendido 3 horas consume 6 kWh. Ese consumo, multiplicado por el precio del kWh, da el costo.",
        "Ahorrar energía es posible con medidas simples y seguras: apagar luces y equipos que no se usan, aprovechar la luz natural, usar equipos con buena eficiencia indicada en su etiqueta y planificar el uso de los equipos que más consumen. Las revisiones, las reparaciones y los cambios en una instalación eléctrica solo los hacen personas autorizadas; un trabajador no debe abrir tableros, tocar cables ni modificar instalaciones.",
        "Ahorrar energía reduce el costo de la empresa y también el impacto ambiental, porque generar energía implica usar recursos naturales." + LIM,
    ],
    vocab=[("eficiencia energética", "lograr el mismo resultado usando menos energía"), ("potencia", "energía que usa un equipo por unidad de tiempo, medida en watts (W)"), ("kWh", "kilowatt-hora, unidad de la energía consumida"), ("consumo", "energía que un equipo usa durante un tiempo"), ("etiqueta de eficiencia", "información en un equipo sobre cuánta energía usa"), ("personal autorizado", "persona con formación y permiso para intervenir una instalación")],
    worked=[
        ("Calcular energía", "Un equipo de ejemplo de 500 W funciona 4 horas. ¿Cuántos kWh consume?", ["Energía = potencia × horas ÷ 1.000.", "500 × 4 ÷ 1.000 = 2."], "2 kWh"),
        ("Calcular costo", "Con un precio de ejemplo de $100 por kWh, ¿cuánto cuestan 3 kWh?", ["Se multiplica el consumo por el precio.", "3 × 100 = 300."], "$300"),
    ],
    mistakes=[("Abrir un tablero eléctrico para «ver cuánto consume» un equipo.", "Es peligroso y solo lo hace personal autorizado.", "Consulta la etiqueta del equipo o pide el dato a la persona encargada."),
              ("Dejar encendidos equipos cuando nadie los usa «porque son pocos watts».", "Aunque sean pocos, el consumo se acumula por muchas horas.", "Apaga lo que no se usa y revisa el consumo total.")],
    T=[
        ("abc", "En eficiencia energética: ¿qué mide la potencia de un equipo?", "Cuánta energía usa por unidad de tiempo", "Cuántas horas puede funcionar", "Cuánto cuesta el equipo", "La potencia indica la rapidez con que el equipo usa energía."),
        ("abc", "¿En qué unidad se mide la energía que se cobra en el consumo?", "En kWh", "En watts", "En metros", "El consumo de energía se mide en kilowatts-hora."),
        ("=", "{F} ¿Cuántos watts suman las 10 ampolletas?", "10*20", "Se multiplica la potencia de una ampolleta por la cantidad.", " W"),
        ("=", "{F} ¿Cuántos kWh consumen las ampolletas en un día?", "10*20*10//1000", "Se multiplica la potencia total por las horas y se divide entre 1.000.", " kWh"),
        ("=", "{F} ¿Cuántos kWh consumen los computadores en un día?", "5*100*8//1000", "Se multiplica la potencia total de los equipos por las horas y se divide entre 1.000.", " kWh"),
        ("=", "{F} ¿Cuántos kWh consume la estufa en un día?", "1500*4//1000", "Se multiplica la potencia por las horas y se divide entre 1.000.", " kWh"),
        ("=", "{F} ¿Cuál es el consumo total de la oficina en un día?", "10*20*10//1000+5*100*8//1000+1500*4//1000", "Se suman los consumos de ampolletas, computadores y estufa.", " kWh"),
        ("=", "{F} ¿Cuánto cuesta el consumo total de un día?", "(10*20*10//1000+5*100*8//1000+1500*4//1000)*150", "Se multiplica el consumo diario por el precio del kWh.", " pesos"),
        ("=", "{F} Si la estufa se usara 2 horas menos al día, ¿cuántos kWh se ahorrarían?", "1500*2//1000", "Se calcula el consumo de las horas que se dejan de usar.", " kWh"),
        ("abc", "¿Qué medida de ahorro es segura y no exige conocimientos eléctricos?", "Apagar luces y equipos que no se están usando", "Abrir el tablero para revisar los cables", "Cambiar cables por cuenta propia para ahorrar", "Apagar es una medida simple y segura; intervenir instalaciones solo corresponde a personal autorizado."),
        ("abc", "{F} Un compañero dice que la estufa es la que más energía consume de los tres tipos de equipos. ¿Es correcto?", "Sí: consume 6 kWh al día, más que los computadores (4) y las ampolletas (2)", "No: las ampolletas consumen más porque son 10", "No: los computadores consumen más porque son 5", "Aunque la estufa es un solo equipo, su potencia es alta y consume más al día."),
        ("=", "{F} Si las 10 ampolletas de 20 W se cambian por otras de 10 W con la misma luz, ¿cuántos kWh por día se ahorran?", "(20-10)*10*10//1000", "Se calcula la reducción de potencia y se aplica a las horas de uso.", " kWh"),
        ("=", "{F} Con ese ahorro diario, ¿cuántos pesos se ahorran en 20 días de trabajo?", "((20-10)*10*10//1000)*150*20", "Se multiplica el ahorro diario por el precio y por los días.", " pesos"),
    ],
    ctx=("abc", "{F} En la oficina, un trabajador ve que el computador de una sala vacía sigue encendido todo el día. ¿Qué hace?", "Lo apaga si está autorizado a hacerlo, y propone un aviso para apagar los equipos al salir", "Lo deja encendido porque es poco consumo", "Abre el equipo para revisar su consumo", "Apagar lo que no se usa es una medida segura; abrir equipos no corresponde."),
    sc=[
        ("En eficiencia energética: ¿cómo se calcula la energía de un equipo en kWh?", "Potencia en W por horas, dividido por 1.000", "Ese cálculo traduce la potencia y el tiempo a kWh."),
        ("¿Qué haces con una instalación eléctrica que parece dañada?", "Aviso a la persona autorizada", "Solo el personal autorizado puede intervenir las instalaciones."),
        ("¿Qué medida simple ahorra energía?", "Apagar lo que no se usa", "Evita un consumo de energía sin beneficio alguno."),
    ],
    op=("Caso de ejemplo. Un taller de costura ficticio tiene: 12 lámparas de 25 W encendidas 10 horas al día; 4 planchas de 1.000 W usadas 3 horas al día; 1 hervidor de 2.000 W usado 1 hora al día. Precio de ejemplo: $120 por kWh. "
        "Escribe: (1) el consumo diario de cada grupo de equipos en kWh, (2) el consumo total, (3) el costo diario, (4) tres medidas seguras de ahorro y una cosa que no harías sin autorización.",
        "(1) Lámparas: 12 × 25 × 10 ÷ 1.000 = 3 kWh. Planchas: 4 × 1.000 × 3 ÷ 1.000 = 12 kWh. Hervidor: 2.000 × 1 ÷ 1.000 = 2 kWh. (2) 3 + 12 + 2 = 17 kWh. (3) 17 × 120 = 2.040 pesos. (4) Apagar lo que no se usa, planificar el uso de las planchas y aprovechar luz natural; no abriría tableros ni cambiaría cables.",
        ["calcula consumos", "suma el total", "calcula el costo", "propone medidas seguras"],
        ["hoja con cuatro respuestas"],
        ["no dividir entre 1.000", "proponer manipular instalaciones", "olvidar el costo"],
        "Pregunta: «¿qué grupo conviene revisar primero?». Debe decir que las planchas, porque consumen más."),
    reinforce="Elige tres equipos de tu especialidad y escribe qué medida segura ahorraría energía con cada uno.",
    extend="Explica por qué cambiar los hábitos de uso puede ahorrar más energía que comprar equipos nuevos.",
)

# ============================================================ OAG-09, clase 4
F = ("Ficha 36 (registro de consumos de una oficina ficticia, mes 1 y mes 2; datos de ejemplo). Agua: mes 1, 40 m³; mes 2, 36 m³. Papel: mes 1, 20 resmas; mes 2, 15 resmas. Electricidad: mes 1, 400 kWh; mes 2, 380 kWh. "
     "Medidas aplicadas entre ambos meses: imprimir por ambos lados, avisos para cerrar las llaves y apagar los equipos al salir. 1 m³ equivale a 1.000 litros. Precio de ejemplo de una resma: $4.000.")
build(
    G9, 4, F,
    use="Aprenderé a medir el efecto de medidas de cuidado ambiental con datos de consumo, calcular reducciones y proponer metas realistas.",
    prior=["Conozco el uso eficiente de insumos y de energía.", "Sé calcular cuántos por cada 100.", "Sé restar y multiplicar."],
    explain=[
        "Cuidar el ambiente en el trabajo significa reducir los efectos que nuestra actividad tiene sobre el entorno: usar menos recursos, generar menos residuos y evitar contaminar. La huella ambiental es ese efecto, medido por los recursos que se usan y los residuos que se generan. Se mide con registros de consumo de agua, papel, energía y residuos, comparados mes a mes.",
        "Para saber si una medida funcionó se calcula la reducción: consumo anterior menos consumo actual. Para compararla entre recursos con unidades distintas se expresa por cada 100: reducción multiplicada por 100 y dividida entre el consumo anterior. Una meta realista es aquella que se puede lograr con las medidas disponibles, con plazo y con registro. Cada medida debe tener responsables y comunicarse a todo el equipo.",
        "El cuidado ambiental también es una decisión ética: se hace aunque nadie lo vea. Las normas ambientales vigentes y las instrucciones de la empresa se consultan con la jefatura y con las entidades fiscalizadoras." + LIM,
    ],
    vocab=[("huella ambiental", "efecto de una actividad sobre el ambiente por los recursos que usa y los residuos que genera"), ("reducción", "diferencia entre el consumo anterior y el actual"), ("meta ambiental", "objetivo de reducir un consumo o un residuo en un plazo"), ("m³", "metro cúbico: 1.000 litros"), ("medida de mejora", "acción para reducir consumos o residuos"), ("responsable", "persona encargada de cumplir una medida")],
    worked=[
        ("Calcular una reducción", "El consumo de agua de un local de ejemplo bajó de 50 m³ a 45 m³. ¿Cuántos m³ se redujo?", ["Se resta el consumo actual al anterior.", "50 − 45 = 5."], "5 m³"),
        ("Reducción por cada 100", "En otro ejemplo, un consumo bajó de 200 a 180. ¿Cuántos por cada 100 se redujo?", ["La reducción es 200 − 180 = 20.", "20 × 100 ÷ 200 = 10."], "10 por cada 100"),
    ],
    mistakes=[("Cantar victoria porque el consumo bajó un mes, sin registrar los siguientes.", "Una baja puntual puede deberse a otras causas, como menos trabajo, y no a la medida.", "Registra varios meses y compara con la misma base."),
              ("Aplicar una medida sin avisar al equipo ni nombrar responsables.", "Nadie sabe qué hacer ni a quién preguntar y la medida se abandona.", "Comunica la medida, nombra responsables y revisa el avance.")],
    T=[
        ("=", "{F} ¿Cuántos m³ de agua se redujeron entre el mes 1 y el mes 2?", "40-36", "Al consumo del mes 1 se le resta el del mes 2.", " m³"),
        ("=", "{F} ¿Cuántos litros equivalen a la reducción de agua?", "(40-36)*1000", "Se multiplica la reducción en m³ por 1.000 litros.", " litros"),
        ("abc", "{F} ¿Qué medida aplicada explica mejor la baja en el consumo de papel?", "Imprimir por ambos lados", "Apagar los equipos al salir", "Cerrar las llaves", "Imprimir por ambos lados reduce directamente las hojas usadas."),
        ("=", "{F} ¿Cuántos por cada 100 bajó el consumo de agua?", "(40-36)*100//40", "Se calcula la reducción, se multiplica por 100 y se divide entre el consumo anterior.", " por cada 100"),
        ("=", "{F} ¿Cuántos por cada 100 bajó el consumo de papel?", "(20-15)*100//20", "Se calcula la reducción, se multiplica por 100 y se divide entre el consumo anterior.", " por cada 100"),
        ("=", "{F} ¿Cuántos por cada 100 bajó el consumo de electricidad?", "(400-380)*100//400", "Se calcula la reducción, se multiplica por 100 y se divide entre el consumo anterior.", " por cada 100"),
        ("abc", "{F} ¿Qué consumo bajó más en proporción?", "El papel", "El agua", "La electricidad", "El papel bajó 25 de cada 100, más que el agua (10) y la electricidad (5)."),
        ("=", "{F} Si cada resma cuesta $4.000, ¿cuánto dinero se ahorró en papel entre el mes 1 y el mes 2?", "(20-15)*4000", "Se multiplica la reducción de resmas por el precio de cada una.", " pesos"),
        ("abc", "¿Qué es la huella ambiental de una oficina?", "El efecto que tiene su actividad en el ambiente por los recursos que usa y los residuos que genera", "El tamaño del edificio", "El número de trabajadores", "La huella resume el efecto ambiental de los consumos y residuos."),
        ("abc", "{F} Un jefe dice: «Ahorrar solo sirve para gastar menos». ¿Qué respuesta es correcta?", "También reduce el impacto ambiental, además del gasto", "Tiene razón: el ambiente no se ve afectado", "Ahorrar es solo una moda", "Menos consumo implica menos uso de recursos y menos residuos."),
        ("abc", "El consumo de agua bajó un mes, pero ese mes hubo menos personas trabajando. ¿Qué conviene hacer antes de afirmar que la medida funcionó?", "Comparar con la misma cantidad de trabajo o registrar varios meses", "Afirmar que funcionó de inmediato", "Ignorar el dato", "Otras causas pueden explicar una baja, por eso se compara con una base similar."),
        ("abc", "{F} Para el mes 3 proponen bajar el agua otros 4 m³ y el papel otras 5 resmas. ¿Es una meta realista?", "Sí: es similar a lo logrado entre los meses 1 y 2 con las mismas medidas", "No: nunca se puede repetir una reducción", "No: las metas deben ser siempre mayores", "Una meta parecida a lo ya logrado, con las mismas medidas, es alcanzable."),
        ("=", "{F} Si el agua sigue bajando 4 m³ cada mes, ¿cuántos m³ consumirá en el mes 4, si el mes 2 fue de 36 m³?", "36-4*2", "Al consumo del mes 2 se le restan las reducciones de dos meses más.", " m³"),
    ],
    ctx=("abc", "{F} Para sostener los resultados, la encargada quiere que las medidas continúen cuando cambie el personal. ¿Qué es lo más útil?", "Dejar las medidas escritas, nombrar responsables y seguir registrando los consumos", "Confiar en que todos se acuerden", "Evitar registrar para no generar trabajo", "Las medidas documentadas y con responsables se mantienen en el tiempo."),
    sc=[
        ("En cuidado ambiental: ¿cómo se calcula una reducción?", "Consumo anterior menos consumo actual", "La diferencia muestra cuánto se ahorró."),
        ("¿Para qué se expresa la reducción por cada 100?", "Para comparar recursos con unidades distintas", "Así se elimina la diferencia entre las unidades de cada recurso."),
        ("¿Qué necesita una medida para mantenerse?", "Responsables y registro", "Sin ellos la medida tiende a abandonarse con el tiempo."),
    ],
    op=("Caso de ejemplo. Un liceo técnico ficticio registra su consumo en el taller de oficina: mes 1, agua 30 m³, papel 40 resmas y electricidad 500 kWh; mes 2, agua 27 m³, papel 30 resmas y electricidad 450 kWh. Precio de ejemplo de una resma: $4.500. "
        "Escribe: (1) la reducción de cada consumo, (2) cuántos por cada 100 bajó cada uno, (3) cuántos pesos se ahorraron en papel, (4) una meta para el mes 3 y dos medidas para lograrla, con responsables.",
        "(1) Agua: 3 m³; papel: 10 resmas; electricidad: 50 kWh. (2) Agua: 3 × 100 ÷ 30 = 10; papel: 10 × 100 ÷ 40 = 25; electricidad: 50 × 100 ÷ 500 = 10. (3) 10 × 4.500 = 45.000 pesos. (4) Meta: bajar el papel otras 5 resmas; medidas: impresión por ambos lados (responsable: profesora del taller) y revisar antes de imprimir (responsable: estudiantes de turno).",
        ["calcula las reducciones", "calcula por cada 100", "calcula el ahorro en pesos", "propone una meta con responsables"],
        ["hoja con cuatro respuestas"],
        ["no usar el consumo anterior como base", "meta sin responsables", "olvidar el ahorro en pesos"],
        "Pregunta: «¿qué pasaría si el mes 3 el consumo vuelve a subir?». Debe buscar causas posibles y revisar si las medidas se mantuvieron."),
    reinforce="Elige un consumo de tu casa o liceo y escribe una medida para reducirlo y cómo medirías el resultado.",
    extend="Explica con un ejemplo por qué una reducción debe medirse con registros y no con impresiones.",
)

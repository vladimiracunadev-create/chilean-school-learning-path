"""Creación y composición musical 3.º y 4.º medio HC: OAC-07 (relacionar habilidades y conocimientos de la asignatura con contextos laborales, profesionales y de desarrollo personal). Perfiles, fuentes y planes inventados; sin cifras de sueldos ni de empleo."""
from __future__ import annotations

from hc_ccmu_common import build

O7 = "AR-CCMU-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (cinco perfiles de ejemplo, inventados; no entregan sueldos ni cifras de empleo). "
     "P1, compositor/a para audiovisual: crea música que acompaña imágenes de cine, series o videojuegos; trabaja con plazos y con duraciones exactas en segundos; conversa con quien dirige el proyecto. "
     "P2, arreglista: adapta una obra existente a otro formato, como coro o banda; necesita conocer los instrumentos y sus rangos; respeta los derechos de la obra original. "
     "P3, técnico/a de sonido: cuida el volumen y la calidad del sonido en vivo y en grabación; conoce de acústica y equipos; cuida su audición y la del público. "
     "P4, docente de música: enseña a otras personas; comunica procesos y evalúa con criterios. "
     "P5, gestor/a cultural: organiza presentaciones y proyectos; diseña programas, calcula presupuestos y gestiona permisos y difusión.")
build(
    O7, 1, F,
    use="Aprenderé a reconocer contextos laborales y profesionales ligados a la creación y composición musical y a relacionar sus tareas con las habilidades que trabajo en este electivo.",
    prior=["Sé componer con un propósito.", "Sé diseñar y evaluar presentaciones.", "Sé que una investigación necesita fuentes."],
    explain=[
        "Un contexto laboral es un ámbito donde una actividad se hace como trabajo o profesión, con tareas, plazos y personas que colaboran. La creación musical se relaciona con muchos: componer para imágenes en cine, series o videojuegos; arreglar obras para otros formatos; cuidar el sonido en vivo y en grabación; enseñar música; organizar proyectos culturales. Muchas personas combinan varios roles, como componer y enseñar.",
        "Las habilidades de este electivo se reconocen en esos contextos. Componer con un propósito sirve a quien crea música para imágenes. Conocer los rangos de los instrumentos sirve a quien arregla. Cuidar el volumen y el oído sirve a quien trabaja con sonido. Comunicar el proceso y evaluar con criterios sirve a quien enseña. Diseñar programas, calcular presupuestos y gestionar permisos sirve a quien organiza proyectos.",
        "Las habilidades de la asignatura también sirven para el desarrollo personal aunque no se llegue a una profesión musical: creatividad, constancia, trabajo en equipo y comunicación se usan en muchos ámbitos. Los perfiles de esta clase son de ejemplo. Datos como sueldos, demanda de empleo o requisitos de estudio cambian con el tiempo y el lugar, y se consultan en fuentes confiables y actuales.",
    ],
    vocab=[("contexto laboral", "ámbito donde una actividad se hace como trabajo, con tareas y plazos"), ("arreglista", "persona que adapta una obra existente a otro formato"), ("técnico/a de sonido", "persona que cuida el volumen y la calidad del sonido"),
           ("gestor/a cultural", "persona que organiza proyectos y presentaciones culturales"), ("habilidad", "capacidad que se desarrolla con práctica"), ("desarrollo personal", "crecimiento de capacidades propias para la vida")],
    worked=[
        ("Relacionar tarea y habilidad", "Un perfil ficticio calcula cuánto durará una presentación de 6 piezas y pide permisos para usar el local. ¿Qué habilidades del electivo usa?",
         ["Calcular la duración de un programa es diseñar el programa de una presentación.", "Pedir permisos es gestionar la presentación; ambas habilidades pertenecen al diseño y gestión de presentaciones."],
         "Diseñar y gestionar presentaciones"),
        ("Calcular compases", "Una escena ficticia de 30 segundos necesita música a 120 pulsos por minuto. ¿Cuántos compases de 4 pulsos necesita?",
         ["A 120 pulsos por minuto hay 2 pulsos por segundo: en 30 segundos son 60 pulsos.", "60 ÷ 4 = 15 compases."],
         "15 compases"),
    ],
    mistakes=[("Pensar que solo hay un camino profesional ligado a la música.", "Se ignoran los oficios que usan sus habilidades.", "Revisa los contextos distintos y las habilidades que se repiten en ellos."),
              ("Dar por seguros datos como sueldos o cantidad de empleos.", "Esas cifras cambian con el tiempo y el lugar.", "Búscalas en fuentes confiables y actuales.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un contexto laboral?', 'Un ámbito donde una actividad se hace como trabajo, con tareas, plazos y personas que colaboran', 'Un lugar donde solo se ensaya sin ningún objetivo ni personas que colaboren', 'Un tipo de instrumento que usan quienes trabajan en música profesional', 'El contexto laboral describe dónde y cómo se realiza una actividad como trabajo.'),
        ('abc', '{F} ¿Qué crea una persona del perfil P1?', 'Música que acompaña imágenes de cine, series o videojuegos', 'Instrumentos de madera que se fabrican para conciertos de cámara', 'Listas de canciones para fiestas que se arman con música ya publicada', 'La ficha describe a P1 como compositor/a para audiovisual.'),
        ('abc', '{F} ¿Qué tarea es propia de P3?', 'Cuidar el volumen y la calidad del sonido', 'Adaptar una obra a otro formato', 'Calcular el presupuesto de un festival', 'La ficha describe a P3 como técnico/a de sonido.'),
        ('abc', '{F} ¿En qué se diferencia P2 de P1?', 'P2 adapta una obra existente y P1 crea música para imágenes', 'P2 crea siempre desde cero y P1 solo adapta obras que ya existen', 'No se diferencian, porque ambos trabajan exactamente de la misma manera', 'El arreglo parte de una obra ya existente.'),
        ('=', '{F} Una escena de 40 segundos pide música a 90 pulsos por minuto. ¿Cuántos compases de 4 pulsos necesita P1?', '40*90//60//4', 'Se calculan los pulsos de la escena y luego se agrupan en compases de 4 pulsos.', ' compases'),
        ('abc', '{F} ¿Qué habilidad del electivo usa P5 al armar el programa de una presentación?', 'Diseñar y gestionar presentaciones', 'Analizar estéticamente una obra', 'Componer una melodía de cuatro notas', 'Diseñar programas y presupuestos se relaciona con presentar.'),
        ('abc', '{F} ¿Qué habilidad del electivo usa P4 al evaluar con criterios el trabajo de un grupo?', 'Evaluar críticamente procesos y resultados', 'Crear un ostinato de bombo para un ambiente de baile', 'Cuidar el eco de un gimnasio durante una presentación', 'Evaluar con criterios es evaluar críticamente.'),
        ('abc', '{F} ¿Qué perfil necesita saber qué notas puede tocar cada instrumento?', 'P2, el arreglista', 'P5, el gestor cultural', 'P4, el docente', 'Adaptar una obra a otro formato exige conocer los rangos de los instrumentos.'),
        ('=', '{F} P5 arma un programa con 5 piezas de 4 minutos y 4 transiciones de 1 minuto. ¿Cuántos minutos dura?', '5*4+4*1', 'Se suman los minutos de las cinco piezas y los de las cuatro transiciones.', ' minutos'),
        ('abc', '{F} Un/a arreglista adapta una canción comercial sin pedir permiso porque «solo la adapta». ¿Qué falla?', 'Adaptar una obra de otra persona suele requerir la autorización de quien tiene los derechos; ante dudas conviene consultar a un especialista', 'Nada, porque adaptar una obra existente nunca necesita ningún permiso', 'Que las canciones de otras personas no se pueden adaptar bajo ninguna condición', 'La adaptación se apoya en la obra original y sus derechos.'),
        ('abc', 'Una estudiante dice que no puede dedicarse a la música si no toca en un escenario. ¿Qué es más preciso?', 'Hay muchos contextos, como enseñar, arreglar, cuidar el sonido o gestionar proyectos, que usan habilidades musicales', 'Es cierto: solo hay un camino y es tocar en un escenario ante un público', 'Nadie vive de la música, así que esas habilidades no sirven en ningún trabajo', 'Los contextos laborales ligados a la música son variados.'),
        ('abc', 'Una persona no quiere ser músico profesional. ¿Para qué le sirven las habilidades de este electivo?', 'Para su desarrollo personal: creatividad, constancia, trabajo en equipo y comunicación se usan en muchos ámbitos', 'Para nada, porque estas habilidades solo sirven a quienes llegan a ser profesionales', 'Solo para tocar en fiestas y reuniones familiares durante el tiempo libre', 'Las habilidades son transferibles a otros ámbitos.'),
        ('abc', 'Quieres saber cuánto se gana en un oficio de la ficha. ¿Qué haces?', 'Consultas fuentes confiables y actuales, porque ese dato cambia con el tiempo y el lugar', 'Usas la ficha como dato seguro, porque es la fuente más a mano', 'Inventas una cifra aproximada para que el trabajo quede completo', 'Los sueldos no están en la ficha y cambian; se consultan fuentes confiables.'),
    ],
    ctx=('abc', 'Una compañera quiere un camino en que combine componer y enseñar. ¿Qué relación con la ficha es la más acertada?', 'Combina el perfil P1, que compone, con el P4, que enseña, porque muchas personas combinan roles', 'No existe esa combinación, porque cada persona debe elegir un solo perfil', 'Solo puede elegir uno y abandonar el otro, porque ambos exigen dedicación total', 'Los roles pueden combinarse, como lo indican los perfiles de la ficha.'),
    sc=[
        ("En Composición musical: ¿qué es un arreglista?", "Una persona que adapta una obra existente a otro formato", "El arreglo parte de una obra ya existente."),
        ('abc', 'Cuidar el volumen y el oído de un público es tarea de:', 'Un/a técnico/a de sonido', 'Un/a arreglista, que adapta obras a otros formatos de interpretación', 'Un/a gestor/a cultural, que organiza programas y presupuestos de presentaciones', 'Controlar el sonido y la audición forma parte de su trabajo.'),
        ("¿Dónde se consultan los sueldos o la demanda de un oficio?", "En fuentes confiables y actuales", "Esos datos cambian y deben verificarse."),
    ],
    op=("Con la {F}, elige dos perfiles y, para cada uno, escribe una tarea de la ficha y la habilidad de este electivo que la sostiene. Después escribe una frase sobre cómo esas habilidades sirven a tu desarrollo personal, aunque no estudies música.",
        "P1: componer música de 40 segundos para una escena; habilidad: componer con un propósito y calcular compases. P3: cuidar el volumen en un concierto; habilidad: cuidar el oído y el equilibrio del sonido. Desarrollo personal: la constancia y el trabajo en equipo me sirven en cualquier estudio.",
        ["dos perfiles con tarea y habilidad", "habilidades del electivo bien relacionadas", "frase sobre desarrollo personal"],
        ["hoja con los perfiles, sus habilidades y la frase"],
        ["inventar sueldos o cifras", "no relacionar tarea y habilidad", "olvidar el desarrollo personal"],
        "Pregunta: «¿qué habilidad de este electivo usarías en ese oficio?». Si no sabe, pídele que nombre una tarea del perfil."),
    reinforce="Escribe tres oficios relacionados con la música que conozcas y una habilidad que se repite en dos de ellos.",
    extend="Explica con un ejemplo inventado cómo una habilidad que aprendiste al componer puede servirte en un trabajo no musical.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (guion de entrevista y fuentes de ejemplo, inventados). Guion con 5 preguntas para una persona de oficio: ¿qué hace en un día de trabajo?; ¿qué habilidades usa más?; ¿cómo se formó?; ¿qué dificultades enfrenta?; ¿qué consejo da a un estudiante? "
     "Plan: 3 entrevistas de 20 minutos, y 10 minutos de transcripción para cada una. "
     "Fuente A: entrevista con consentimiento a una persona que trabaja como técnica de sonido (nombre ficticio), con fecha reciente. "
     "Fuente B: página de una institución de formación ficticia, con fecha de actualización, que describe un programa de estudios. "
     "Fuente C: comentario sin autor ni fecha en un foro, que dice cuánto gana «todo el mundo» en el oficio.")
build(
    O7, 2, F,
    use="Aprenderé a investigar un contexto laboral con fuentes confiables, a preparar una entrevista y a registrar y contrastar lo que averiguo, cuidando la ética y la seguridad.",
    prior=["Sé qué contextos laborales tiene la música.", "Sé citar una fuente.", "Sé que los datos cambian con el tiempo."],
    explain=[
        "Investigar un contexto laboral es averiguar qué tareas tiene, qué habilidades pide, cómo se forma la gente que trabaja en él y qué dificultades enfrenta. Las fuentes pueden ser personas que trabajan en el oficio (entrevistas), páginas de instituciones de formación, ofertas de trabajo y libros. Una fuente es más confiable si tiene autor, fecha reciente y un propósito claro; un comentario sin autor ni fecha no sirve de evidencia.",
        "Se contrasta cada dato con al menos dos fuentes distintas antes de aceptarlo, porque una sola puede estar equivocada o desactualizada. Lo investigado se registra con la fuente (quién, qué título, cuándo). Las cifras como sueldos o cantidad de empleos cambian y se citan solo con fuente y fecha; si no hay una fuente confiable, no se usan.",
        "Una entrevista necesita cuidados: se pide consentimiento para entrevistar y para citar a la persona, no se piden datos personales ni sueldos exactos, y no se publica su nombre sin permiso. Antes de contactar a alguien que no conoces, avisa a una persona adulta o a tu docente, y haz la entrevista por un medio acordado y seguro. Este cuaderno trabaja con fuentes de ejemplo; las fuentes reales las buscas tú con apoyo del docente.",
    ],
    vocab=[("fuente confiable", "fuente con autor, fecha reciente y propósito claro"), ("contrastar", "comparar un dato con otras fuentes"), ("consentimiento", "autorización de una persona para entrevistarla o citarla"),
           ("entrevista", "conversación con una persona para obtener información"), ("transcripción", "paso a texto de lo conversado"), ("desactualizado", "dato que ya cambió")],
    worked=[
        ("Evaluar una fuente", "Una fuente ficticia es un mensaje sin autor ni fecha que dice que «todos ganan mucho en este oficio». ¿Sirve como evidencia?",
         ["No tiene autor ni fecha y no se puede verificar quién lo dice.", "No sirve como evidencia por sí sola; hay que contrastar con fuentes confiables."],
         "No sirve como evidencia"),
        ("Calcular tiempo de entrevistas", "Un grupo ficticio hará 4 entrevistas de 15 minutos y dedicará 10 minutos de transcripción a cada una. ¿Cuántos minutos necesita?",
         ["Cada entrevista ocupa 15 + 10 = 25 minutos.", "Son 4 entrevistas: 4 × 25 = 100 minutos."],
         "100 minutos"),
    ],
    mistakes=[("Aceptar un dato porque lo dice un solo comentario.", "No se contrasta ni se conoce a la persona que lo dijo.", "Contrasta con al menos dos fuentes con autor y fecha."),
              ("Entrevistar a alguien sin avisar a un adulto o sin su consentimiento.", "Se arriesga la seguridad y la privacidad de las personas.", "Pide consentimiento y avisa a tu docente o a una persona adulta antes de contactar.")],
    T=[
        ('abc', 'En Composición musical: ¿qué hace confiable a una fuente sobre un oficio?', 'Tener autor, fecha reciente y un propósito claro', 'Que tenga muchas imágenes y llame la atención de quien la lee', 'Que sea la primera que aparece en una búsqueda y tenga muchas visitas', 'La confiabilidad se apoya en quién escribe, cuándo y para qué.'),
        ('abc', '{F} ¿Qué fuente es la menos confiable?', 'La fuente C, porque no tiene autor ni fecha', 'La fuente A, porque tiene consentimiento', 'La fuente B, porque tiene fecha de actualización', 'La fuente C no se puede verificar.'),
        ('abc', '{F} ¿Qué fuente permite conocer el día a día de un oficio?', 'La fuente A, una entrevista a una persona que trabaja en él', 'La fuente B, que describe un programa de estudios', 'La fuente C, un comentario anónimo', 'Una persona del oficio cuenta su experiencia de primera mano.'),
        ('abc', '{F} ¿Qué fuente permite conocer cómo es un programa de estudios?', 'La fuente B, la página de una institución de formación', 'La fuente A, la entrevista a una persona técnica de sonido con consentimiento', 'La fuente C, el comentario sin autor ni fecha de un foro', 'La institución describe su propio programa de estudios.'),
        ('=', '{F} ¿Cuántos minutos necesita el plan de 3 entrevistas con su transcripción?', '3*(20+10)', 'Cada entrevista ocupa 20 minutos más 10 de transcripción, y son tres.', ' minutos'),
        ('abc', '{F} ¿Cuál de las preguntas del guion permite conocer cómo se formó la persona?', '¿Cómo se formó?', '¿Qué consejo da a un estudiante?', '¿Qué dificultades enfrenta?', 'La tercera pregunta se refiere a su formación.'),
        ('abc', '{F} ¿Qué se debe pedir antes de citar a la persona entrevistada en un trabajo?', 'Su consentimiento para entrevistarla y citarla', 'Su sueldo exacto, para poder comparar con el de otros trabajos', 'Sus datos personales completos, para poder contactarla después', 'Se pide autorización para usar sus palabras; no se piden datos personales.'),
        ('abc', '¿Por qué se contrasta un dato con dos fuentes distintas?', 'Porque una sola puede estar equivocada o desactualizada', 'Porque la segunda fuente siempre es más confiable que la primera', 'Porque con dos fuentes ya no hace falta anotar quién las escribió', 'Contrastar reduce el riesgo de aceptar un dato erróneo.'),
        ('abc', '{F} La fuente C dice cuánto gana «todo el mundo». ¿Qué conviene hacer con esa cifra?', 'No usarla sin una fuente confiable y actual', 'Citarla como dato seguro, porque la dijo una persona que parece saber', 'Promediarla con otra cifra sin fuente para que se vea más razonable', 'Las cifras de sueldos requieren fuente y fecha.'),
        ('abc', 'Quieres entrevistar a un técnico de sonido que no conoces. ¿Qué es lo más seguro?', 'Avisar primero a tu docente o a una persona adulta y acordar un medio seguro', 'Contactarlo en secreto para que nadie interfiera con la entrevista', 'Pedirle sus datos personales y su sueldo para empezar la conversación', 'Avisar a un adulto cuida tu seguridad y la de la otra persona.'),
        ('abc', '{F} Una estudiante anota «la técnica dice que se necesita estudiar en tal institución» y cita solo «una entrevista». ¿Qué le falta?', 'Anotar quién, cuándo y con qué consentimiento, y contrastar con otra fuente', 'Nada, porque una sola entrevista basta como fuente para un dato así', 'Quitar la fuente del trabajo para que no se pueda contradecir', 'Un registro completo permite verificar y contrastar.'),
        ('abc', '{F} La fuente B describe un programa de estudios con una fecha de actualización de hace varios años. ¿Qué conviene hacer?', 'Confirmar en una fuente más reciente, porque los programas cambian', 'Aceptarlo sin revisar, porque la página es de una institución y por eso siempre es actual', 'Usarlo como dato actual en el trabajo sin mencionar la fecha de la página', 'Los datos pueden haber cambiado; se confirman en fuentes actuales.'),
        ('abc', 'Un entrevistado dice que prefiere que no se publique su nombre. ¿Qué haces?', 'Respetas su decisión y lo citas como «una persona del oficio»', 'Publicas igual el nombre, porque la entrevista ya se hizo y es información útil', 'Borras la entrevista completa y no dices nada a la persona ni al grupo', 'Respetar la privacidad forma parte de la ética de la investigación.'),
    ],
    ctx=('=', 'Tu grupo hará 5 entrevistas de 15 minutos y dedicará 10 minutos de transcripción a cada una. ¿Cuántos minutos necesita?', '5*(15+10)', 'Cada entrevista ocupa 15 minutos más 10 de transcripción, y son cinco.', ' minutos'),
    sc=[
        ("En Composición musical: ¿qué es contrastar un dato?", "Compararlo con otras fuentes", "Contrastar permite comprobar si un dato se repite en fuentes confiables."),
        ('abc', 'Antes de entrevistar a una persona se pide:', 'Su consentimiento', 'Su dirección', 'Su sueldo exacto', 'El consentimiento autoriza la entrevista y la cita.'),
        ("¿Qué se hace antes de contactar a alguien que no conoces?", "Avisar a una persona adulta o al docente y acordar un medio seguro", "La seguridad exige que un adulto sepa del contacto."),
    ],
    op=("Con la {F}, escribe un plan de investigación sobre un oficio musical de tu interés: tres preguntas del guion, dos tipos de fuentes y dos cuidados éticos que respetarás. Calcula el tiempo de dos entrevistas con transcripción.",
        "Oficio: arreglista. Preguntas: ¿qué hace en un día de trabajo?; ¿qué habilidades usa más?; ¿cómo se formó? Fuentes: una entrevista y la página de una institución de formación. Cuidados: pido consentimiento y aviso a mi docente antes de contactar. Tiempo: 2 × (20 + 10) = 60 minutos.",
        ["tres preguntas relacionadas con el oficio", "dos tipos de fuentes", "dos cuidados éticos", "calcula el tiempo"],
        ["hoja con el plan de investigación y el cálculo"],
        ["pedir datos personales", "no incluir consentimiento", "no calcular el tiempo"],
        "Pregunta: «¿qué haces para contrastar un dato?». Si no tiene respuesta, pídele que nombre una segunda fuente."),
    reinforce="Escribe cuatro preguntas para entrevistar a una persona que trabaja con sonido, sin pedir datos personales.",
    extend="Explica con un ejemplo inventado cómo dos fuentes pueden contradecirse y cómo decidirías cuál usar.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (perfil de ejemplo, inventado). Lía, estudiante ficticia, tiene logradas estas habilidades: L1 componer con un propósito; L2 escribir en notación de texto; L3 trabajar en equipo; L4 evaluar críticamente; L5 cuidar el oído (volumen moderado y pausas). "
     "Las tiene en proceso: L6 presentar en público; L7 gestionar tiempos. Aún no desarrolla: L8 manejar equipo de sonido. "
     "Contextos y habilidades que piden: compositor/a para audiovisual: L1, L2, L3 y L7; técnico/a de sonido: L3, L5 y L8; docente de música: L3, L4 y L6; gestor/a cultural: L3, L6 y L7. "
     "Formas de seguir formándose, en general: estudios superiores en música o áreas afines, formación técnica, talleres y cursos, y práctica en proyectos propios con un portafolio. Los requisitos de ingreso y los planes de estudio cambian y se consultan en cada institución.")
build(
    O7, 3, F,
    use="Aprenderé a relacionar mis habilidades con distintos contextos laborales y a decidir próximos pasos de formación y práctica, con base en evidencia de lo que ya logro.",
    prior=["Conozco contextos laborales de la música.", "Sé investigar con fuentes.", "Sé evaluar mis habilidades con evidencia."],
    explain=[
        "Relacionar habilidades con contextos es comparar lo que una persona ya sabe hacer con lo que pide cada oficio. Se hace una lista de habilidades logradas, en proceso y por desarrollar, cada una con evidencia (por ejemplo, una pieza escrita o una bitácora). Luego se revisa, para cada contexto, cuántas de las habilidades que pide ya están logradas.",
        "Esa comparación no decide el futuro de nadie: indica por dónde empezar. Una habilidad en proceso se puede practicar, y una que aún no se tiene se puede aprender. Además de estudios superiores, hay otras formas de seguir formándose: formación técnica, talleres y cursos, y la práctica en proyectos propios, con un portafolio que muestre el trabajo. Las condiciones de ingreso y los planes de estudio cambian, por lo que se consultan en cada institución y no se suponen.",
        "Un buen plan combina lo que se disfruta, lo que se hace bien y lo que el contexto necesita. Conviene hablar con personas de confianza, como el docente o la familia, y con quienes trabajan en el oficio, sin comprometerse a una decisión definitiva. Estas decisiones también tienen que ver con el bienestar: cuidar el oído, descansar y no sobrecargarse.",
    ],
    vocab=[("habilidad lograda", "habilidad que ya se hace bien, con evidencia"), ("habilidad en proceso", "habilidad que se está desarrollando"), ("portafolio", "conjunto de trabajos que muestran lo que se sabe hacer"),
           ("trayectoria formativa", "camino de estudios y práctica"), ("coincidencia", "habilidad que se tiene y que el contexto pide"), ("evidencia", "trabajo o registro que muestra una habilidad")],
    worked=[
        ("Contar coincidencias", "Un contexto ficticio pide las habilidades A, B y C. Una persona tiene logradas A y C. ¿Cuántas coincidencias hay?",
         ["Se comparan las habilidades que pide con las que tiene logradas: A y C.", "Hay 2 coincidencias de 3."],
         "2 de 3"),
        ("Planificar práctica", "Para desarrollar una habilidad en proceso, una persona ficticia practica 25 minutos al día durante 4 días. ¿Cuántos minutos practica en total?",
         ["Se multiplican los minutos diarios por los días: 25 × 4.", "25 × 4 = 100 minutos."],
         "100 minutos"),
    ],
    mistakes=[("Pensar que una habilidad «en proceso» significa que no sirve para ese contexto.", "Se confunde estar en desarrollo con no tenerla.", "Planifica práctica para convertirla en habilidad lograda."),
              ("Suponer los requisitos de ingreso de una institución.", "Esos requisitos cambian.", "Consulta la información actual directamente en cada institución.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un portafolio?', 'Un conjunto de trabajos que muestran lo que una persona sabe hacer', 'Una lista de instrumentos del curso y de quienes los tocan', 'Una evaluación sin evidencia que dice cuánto sabe hacer una persona', 'El portafolio reúne evidencia del trabajo.'),
        ('abc', '{F} ¿Cuántas habilidades tiene Lía logradas?', '5 habilidades', '3 habilidades', '8 habilidades', 'La ficha enumera L1 a L5 como logradas.'),
        ('abc', '{F} ¿Qué habilidad tiene Lía en proceso?', 'Presentar en público', 'Manejar equipo de sonido', 'Componer con un propósito', 'L6 es presentar en público y está en proceso.'),
        ('abc', '{F} ¿Qué habilidades pide el contexto técnico/a de sonido?', 'L3, L5 y L8', 'L1, L2, L3 y L7', 'L3, L4 y L6', 'La ficha lo indica para ese contexto.'),
        ('abc', '{F} El contexto compositor/a para audiovisual pide L1, L2, L3 y L7. ¿Cuántas de ellas tiene Lía logradas?', '3 de 4: L1, L2 y L3', '4 de 4, porque L7 también está lograda por Lía', '2 de 4: solo L1 y L2, porque L3 aún está en proceso', 'L7 está en proceso, así que coinciden como logradas L1, L2 y L3.'),
        ('abc', '{F} ¿Cuántas habilidades logradas de Lía coinciden con el contexto técnico/a de sonido?', '2: L3 y L5', '3: L3, L5 y L8', '1: L8', 'L8 aún no está desarrollada; coinciden L3 y L5.'),
        ('abc', '{F} ¿Con qué contexto coinciden más habilidades logradas de Lía?', 'Compositor/a para audiovisual, con 3 coincidencias', 'Técnico/a de sonido, con 2 coincidencias', 'Gestor/a cultural, con 1 coincidencia', 'Compositor/a coincide en L1, L2 y L3; los otros contextos coinciden menos.'),
        ('abc', '{F} ¿Cuántas coincidencias logradas tiene Lía con el contexto gestor/a cultural, que pide L3, L6 y L7?', '1: solo L3', '2: L3 y L6', '3: L3, L6 y L7', 'L6 y L7 están en proceso, así que solo L3 coincide como lograda.'),
        ('=', '{F} Para pasar L6 de en proceso a lograda, Lía practica 20 minutos al día durante 5 días. ¿Cuántos minutos practica?', '20*5', 'Se multiplican los minutos diarios por los días.', ' minutos'),
        ('abc', '{F} Lía quiere acercarse al contexto compositor/a para audiovisual. ¿Qué habilidad le conviene practicar primero?', 'L7, gestionar tiempos, que ya está en proceso y es la que falta lograr', 'L8, manejar equipo de sonido, que ese contexto no pide', 'L5, cuidar el oído, que ya tiene lograda', 'L7 está en proceso y es la única que le falta en ese contexto.'),
        ('abc', 'Alguien dice que, como Lía no tiene L8, no puede dedicarse a nada ligado al sonido. ¿Qué es más preciso?', 'L8 se puede aprender; la ficha solo indica por dónde empezar', 'Es cierto: no puede dedicarse a nada ligado al sonido sin esa habilidad', 'L8 es innata y no se aprende, así que solo la tienen algunas personas', 'Las habilidades se desarrollan con práctica.'),
        ('abc', '{F} Lía averigua los requisitos de ingreso de una institución en la ficha. ¿Qué conviene hacer?', 'Consultarlos en la propia institución, porque cambian', 'Darlos por seguros, porque están escritos en la ficha de la clase', 'Pedirlos a un compañero sin verificar, porque seguro los conoce bien', 'La ficha dice que los requisitos cambian y se consultan en cada institución.'),
        ('abc', 'Lía tiene mucha carga de ensayos y siente cansancio y dolor de oídos. ¿Qué conviene?', 'Reducir el volumen, hacer pausas y conversar con una persona adulta de confianza', 'Seguir sin descanso para avanzar más rápido y compensar el tiempo perdido', 'Esconderlo porque es una molestia pequeña que pasará sola con el tiempo', 'Cuidar la audición y pedir apoyo es parte del desarrollo personal.'),
    ],
    ctx=('abc', 'Un estudiante tiene logradas dos habilidades que pide un oficio y cuatro en proceso. ¿Qué decisión es más razonable?', 'Planificar práctica para las que están en proceso y seguir recogiendo evidencia en su portafolio', 'Descartar el oficio porque no las tiene todas logradas todavía', 'Decidir su futuro definitivamente ahora, antes de seguir investigando', 'Las habilidades en proceso se pueden fortalecer con práctica y evidencia.'),
    sc=[
        ("En Composición musical: ¿qué es una habilidad en proceso?", "Una habilidad que se está desarrollando", "Se puede fortalecer con práctica y evidencia."),
        ('abc', 'Para mostrar una habilidad se usa:', 'Evidencia, como una pieza escrita o una bitácora', 'Solo la palabra «sé hacerlo»', 'La opinión de alguien que no te conoce', 'La evidencia respalda la habilidad ante otras personas.'),
        ("¿Dónde se consultan los requisitos de ingreso de una institución?", "En la propia institución, con información actual", "Los requisitos cambian con el tiempo y se confirman en la institución."),
    ],
    op=("Con la {F} como modelo, haz tu propia lista de cinco habilidades de este electivo, marcando cuáles tienes logradas, en proceso o por desarrollar, cada una con una evidencia. Elige un contexto laboral y cuenta cuántas coincidencias logradas tienes.",
        "Logradas: componer con propósito (pieza ABA de 12 compases); escribir en notación de texto (ficha de mi pieza). En proceso: presentar en público (guion de 6 minutos). Por desarrollar: manejar equipo de sonido. Contexto: compositor/a para audiovisual; coincidencias logradas: 2 de 4.",
        ["cinco habilidades con estado y evidencia", "elige un contexto laboral", "cuenta coincidencias correctamente"],
        ["hoja con la lista y el conteo de coincidencias"],
        ["no dar evidencia", "contar mal las coincidencias", "decidir el futuro de forma definitiva"],
        "Pregunta: «¿qué evidencia respalda cada habilidad lograda?». Si no tiene una, pídele que la marque como en proceso."),
    reinforce="Elige un contexto de la ficha y escribe qué habilidades pide, cuáles de ellas tienes logradas y cómo practicarías una.",
    extend="Explica con un ejemplo inventado cómo un portafolio puede reemplazar una lista de promesas al hablar con una institución.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (plan de ejemplo, inventado). Plan de desarrollo personal de 8 semanas de una estudiante ficticia. Meta: armar un portafolio con 3 piezas breves, una ficha de proceso y los créditos. "
     "Cada pieza tiene 16 compases de 4 pulsos a 96 pulsos por minuto. Dedicación: 3 horas por semana. Reparto del tiempo total: composición, 12 horas; registro y fichas, 6 horas; ensayo y presentación, 4 horas; revisión con pares, 2 horas. "
     "Hitos: semana 2, primera pieza; semana 5, segunda pieza; semana 8, tercera pieza y entrega del portafolio. "
     "Cuidados: volumen moderado y pausas de silencio en cada sesión; si algo del plan genera sobrecarga, conversarlo con una persona adulta de confianza.")
build(
    O7, 4, F,
    use="Aprenderé a diseñar un plan de desarrollo personal con metas, tiempos y evidencias, y a armar un portafolio que muestre mis habilidades de composición, presentación y evaluación.",
    prior=["Sé qué contextos laborales usan estas habilidades.", "Sé qué es un portafolio.", "Sé planificar el tiempo."],
    explain=[
        "Un plan de desarrollo personal es una forma de organizar el aprendizaje para lograr una meta. Tiene una meta clara, tiempos, hitos (puntos de control) y evidencias de lo logrado. Un portafolio es un conjunto de trabajos con su ficha de proceso: muestra el propósito de cada pieza, las decisiones, las versiones y los créditos. Sirve para presentar tus habilidades a otras personas, por ejemplo en un taller, un curso o una institución de formación.",
        "Para armar el plan se calcula el tiempo total y se reparte entre las tareas: componer, registrar, ensayar y revisar con pares. Cada hito tiene una fecha. Si el tiempo real se aleja del plan, se ajusta el plan, no se abandona. Un plan realista incluye descansos y cuidados: volumen moderado, pausas de silencio y avisar a una persona adulta de confianza si algo genera sobrecarga.",
        "El portafolio también es un ejercicio de ética: cada pieza lleva sus créditos, las fuentes que inspiraron la obra y los permisos de quienes participan. Todo se hace por escrito en este cuaderno, sin audio ni software real; la grabación y la edición del portafolio quedan como complemento del docente.",
    ],
    vocab=[("plan de desarrollo personal", "organización del aprendizaje para lograr una meta"), ("hito", "punto de control con una fecha"), ("portafolio", "conjunto de trabajos con su ficha de proceso"),
           ("ficha de proceso", "registro del propósito, decisiones y versiones de una pieza"), ("sobrecarga", "exceso de tareas que impide descansar"), ("meta", "lo que se quiere lograr en un plazo")],
    worked=[
        ("Calcular horas totales", "Un plan ficticio dura 6 semanas con 4 horas por semana. ¿Cuántas horas suma?",
         ["Se multiplican las semanas por las horas por semana: 6 × 4.", "6 × 4 = 24 horas."],
         "24 horas"),
        ("Revisar un reparto", "Un plan de 10 horas se reparte en 6 horas de composición y 3 de registro. ¿Cuántas horas faltan por asignar?",
         ["Lo asignado suma 6 + 3 = 9 horas.", "Faltan 10 − 9 = 1 hora."],
         "1 hora"),
    ],
    mistakes=[("Poner una meta sin tiempos ni hitos.", "No hay forma de saber si se avanza.", "Define fechas y puntos de control."),
              ("Abandonar el plan si se atrasa una semana.", "Se confunde ajustar con fracasar.", "Revisa el plan y reorganiza el tiempo restante.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un hito de un plan?', 'Un punto de control con una fecha', 'Una pieza que no se termina', 'Una persona del público', 'Un hito marca avances en fechas concretas.'),
        ('abc', '{F} ¿Cuál es la meta del plan?', 'Armar un portafolio con 3 piezas breves, una ficha de proceso y los créditos', 'Grabar un álbum completo de diez piezas con calidad de estudio', 'Tocar en un festival ante un público numeroso durante el verano', 'La ficha declara esa meta para el plan de ocho semanas.'),
        ('abc', '{F} ¿En qué semana se entrega el portafolio?', 'En la semana 8', 'En la semana 2', 'En la semana 5', 'La ficha indica la semana 8 para el hito final.'),
        ('=', '{F} ¿Cuántas horas suma el plan en total? Son 8 semanas de 3 horas por semana.', '8*3', 'Se multiplican las semanas por las horas por semana.', ' horas'),
        ('=', '{F} Suma el reparto del tiempo: composición, registro, ensayo y revisión. ¿Cuántas horas son?', '12+6+4+2', 'Se suman las horas asignadas a cada tarea.', ' horas'),
        ('abc', '{F} ¿Coincide el reparto de horas con el total del plan?', 'Sí, ambos suman 24 horas', 'No, el reparto suma 20 horas', 'No, el reparto suma 30 horas', 'El total de 8 × 3 y la suma del reparto dan 24.'),
        ('=', '{F} ¿Cuántos segundos dura cada pieza de 16 compases de 4 pulsos a 96 pulsos por minuto?', '16*4*60//96', 'Se calculan los pulsos de la pieza y se pasan a segundos.', ' s'),
        ('=', '{F} ¿Cuántos segundos duran las tres piezas juntas?', '3*(16*4*60//96)', 'Se calcula la duración de una pieza y se multiplica por tres.', ' s'),
        ('abc', '{F} ¿Qué hito está fijado para la semana 5?', 'La segunda pieza', 'La entrega del portafolio', 'La primera pieza', 'La ficha ubica la segunda pieza como hito de la semana 5.'),
        ('abc', '{F} La estudiante llega a la semana 3 sin haber terminado la primera pieza. ¿Qué es lo más razonable?', 'Revisar el plan y reorganizar el tiempo restante', 'Abandonar el plan, porque ya no se cumplirá como estaba escrito', 'Cambiar la meta sin decir nada a nadie, para que el atraso no se note', 'Ajustar el plan permite seguir avanzando.'),
        ('abc', '¿Por qué cada pieza del portafolio lleva sus créditos?', 'Porque reconoce a quienes participaron y a las fuentes que inspiraron la obra', 'Porque sirven para decidir cuál pieza es la mejor del portafolio', 'Porque reemplazan la necesidad de la ficha de proceso', 'Los créditos son una práctica ética del trabajo musical.'),
        ('abc', '{F} Una estudiante sigue el plan y siente dolor de oídos tras ensayar a volumen alto. ¿Qué decisión es adecuada?', 'Bajar el volumen, hacer una pausa y conversar con una persona adulta de confianza', 'Seguir igual para no atrasarse y cumplir con el hito de la semana', 'Ocultarlo para no preocupar a nadie, porque es una molestia pasajera', 'La salud auditiva es prioritaria y se cuida con apoyo.'),
        ('abc', 'Un estudiante quiere mostrar su portafolio a una institución de formación. ¿Qué lo hace más convincente?', 'Piezas con ficha de proceso, evidencia de decisiones y créditos claros', 'Una lista de promesas sobre lo que sabrá hacer en el futuro', 'Un solo trabajo sin explicación, para que quien lo vea saque sus conclusiones', 'La evidencia del proceso respalda lo que dice saber hacer.'),
    ],
    ctx=('abc', 'Quieres presentar tu portafolio en un taller del liceo. ¿Qué incluyes para mostrar lo que sabes hacer en composición, presentación y evaluación?', 'Tres piezas con fichas de proceso, un guion de presentación y una evaluación con evidencia', 'Solo el título de tus piezas, sin sus fichas ni su evaluación', 'Solo una lista de oficios que te gustan, sin trabajos que lo respalden', 'El portafolio reúne evidencias de varias habilidades.'),
    sc=[
        ("En Composición musical: ¿qué es una ficha de proceso?", "El registro del propósito, las decisiones y las versiones de una pieza", "Muestra cómo se llegó a la pieza."),
        ('abc', 'Si el tiempo real se aleja del plan, conviene:', 'Ajustar el plan y reorganizar el tiempo restante', 'Abandonar la meta porque ya hubo un atraso en la tercera semana', 'Ignorar el atraso y seguir como si nada hubiera pasado', 'Un plan se ajusta cuando cambia el tiempo real.'),
        ("¿Qué cuidados incluye un plan realista?", "Volumen moderado, pausas y avisar a una persona adulta de confianza si hay sobrecarga", "El bienestar es parte del plan."),
    ],
    op=("Con la {F} como modelo, diseña tu propio plan de desarrollo de 6 semanas con 4 horas por semana: tu meta, el reparto de las horas en cuatro tareas, dos hitos con semana y un cuidado de bienestar. Verifica que el reparto sume el total.",
        "Meta: portafolio con 2 piezas, una ficha de proceso y créditos. Total: 6 × 4 = 24 horas. Reparto: composición 10; registro 6; ensayo 5; revisión con pares 3 (suman 24). Hitos: semana 3, primera pieza; semana 6, segunda pieza y entrega. Cuidado: volumen moderado y pausas de silencio.",
        ["meta clara", "reparto que suma el total", "dos hitos con semana", "un cuidado de bienestar"],
        ["hoja con la meta, el reparto, los hitos y el cuidado"],
        ["reparto que no suma", "olvidar los hitos", "no incluir cuidados"],
        "Pregunta: «¿cuántas horas suma tu reparto y cuántas son en total?». Si no coinciden, pídele que lo ajuste."),
    reinforce="Haz un plan de 4 semanas con 3 horas por semana para terminar una pieza de 8 compases, con dos hitos.",
    extend="Explica con un ejemplo inventado cómo un portafolio puede servir para un taller, un curso o un trabajo distintos.",
)

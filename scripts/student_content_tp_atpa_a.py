"""Atención de Párvulos TP 3.º y 4.º medio: OAE-01 (realizar y evaluar actividades educativas con párvulos, creando ambientes pedagógicos según sus necesidades y su desarrollo) y OAE-02 (preparar, utilizar y almacenar material didáctico y de ambientación con criterios pedagógicos, estéticos y de equidad). Todo en papel: jardines, niños, niñas y familias inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_atpa_common import LIM, build

O1 = "TP-ATPA-3y4-OAE-01"
O2 = "TP-ATPA-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (jardín de ejemplo, inventado). «Jardín Arcoíris de Ejemplo» tiene sala cuna, nivel medio y nivel de transición. En cada sala trabajan una educadora a cargo y una técnica en párvulos que la apoya. "
     "La educadora deja por escrito la planificación de cada experiencia de aprendizaje. Bloque de la mañana del nivel medio: de 10:00 a 11:30, con 18 niños y niñas presentes; incluye una experiencia de aprendizaje de 40 minutos y 15 minutos para ordenar y lavarse las manos; el resto es juego libre.")
build(
    O1, 1, F,
    use="Aprenderé quién planifica y quién apoya una experiencia con niños y niñas, qué norma y qué riesgos hay que tener presentes y por qué todo se registra.",
    prior=["Sé leer una ficha con horarios.", "Sé sumar y restar.", "Sé qué es un jardín infantil."],
    explain=[
        "En Atención de Párvulos, una experiencia de aprendizaje es una actividad pensada para que niños y niñas aprendan jugando. La educadora a cargo la diseña y la deja escrita en una planificación: qué se hará, con qué materiales y cómo se observará lo que ocurre. La técnica en párvulos apoya esa planificación, acompaña a los niños y registra lo que observa, siempre con la educadora presente o supervisando.",
        "Los jardines infantiles atienden por niveles: sala cuna (los más pequeños), nivel medio y nivel de transición (los mayores). Cada nivel tiene necesidades distintas, por eso un material o una actividad adecuada para un nivel puede ser riesgosa en otro, por ejemplo con piezas pequeñas que podrían tragarse. Las Bases Curriculares de la Educación Parvularia orientan lo que se enseña, y la norma vigente fija las condiciones de seguridad.",
        "El principal riesgo es dar por bueno un resultado sin registro ni responsable. Por eso se anota lo observado con hechos, se avisa a la educadora ante cualquier duda y nunca se improvisa con material o espacios que no han sido autorizados." + LIM,
    ],
    vocab=[("experiencia de aprendizaje", "actividad pensada para que niños y niñas aprendan jugando"), ("planificación", "documento de la educadora que dice qué se hará, con qué material y cómo se observará"), ("técnica en párvulos", "persona que apoya a la educadora en la atención de niños y niñas"), ("nivel", "grupo del jardín según la edad: sala cuna, nivel medio o transición"), ("registro", "anotación escrita de hechos observados"), ("supervisión", "presencia y orientación de la educadora mientras la técnica trabaja")],
    worked=[
        ("Quién decide el cambio", "La planificación dice «cuento con títeres», pero la técnica cree que ese día convendría una canción. ¿Qué hace?", ["La planificación es responsabilidad de la educadora.", "La técnica propone su idea y espera la decisión de la educadora; mientras tanto sigue lo escrito."], "Propone el cambio a la educadora y no modifica la actividad por su cuenta"),
        ("Tiempo que queda", "Otro bloque de ejemplo va de 10:30 a 11:15 e incluye una experiencia de 25 minutos. ¿Cuántos minutos quedan para otras rutinas?", ["El bloque dura 45 minutos (de 10:30 a 11:15).", "45 − 25 = 20."], "20 minutos"),
    ],
    mistakes=[("Cambiar la actividad planificada porque «a los niños les gusta más otra».", "La educadora responde por los objetivos y por la seguridad de la experiencia; un cambio sin aviso rompe esa responsabilidad.", "Propón el cambio a la educadora y espera su decisión."),
              ("Anotar solo «el grupo estuvo inquieto» después de la experiencia.", "Sin hechos concretos la educadora no puede evaluar ni ajustar la planificación.", "Anota qué ocurrió, cuándo y con quién, sin etiquetas.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es la planificación de una experiencia de aprendizaje?", "El documento donde la educadora define qué se hará, con qué materiales y cómo se observará", "El registro diario de asistencia de niños y niñas", "La lista de compras de materiales de aseo del jardín", "La planificación es el plan de la educadora; la asistencia y las compras son otros documentos."),
        ("abc", "{F} ¿Quién está a cargo de la sala y decide la planificación?", "La educadora", "La técnica en párvulos", "Una persona de la familia de un niño", "La ficha dice que la educadora está a cargo y la técnica solo la apoya."),
        ("abc", "{F} ¿Qué hace la técnica en párvulos durante la experiencia?", "Apoya lo planificado y registra lo que observa", "Cambia la actividad si le parece mejor, sin avisar", "Decide sola qué niños participan", "La técnica apoya y registra; la decisión sobre la actividad es de la educadora."),
        ("=", "{F} ¿Cuántos minutos de juego libre quedan en el bloque de la mañana?", "(11*60+30)-(10*60)-40-15", "Al total del bloque se le restan la experiencia y el orden.", " minutos"),
        ("abc", "Al preparar la experiencia en una sala cuna, la técnica ve que el material planificado tiene piezas pequeñas que podrían tragarse. ¿Qué corresponde?", "Consultar a la educadora antes de usarlo", "Usarlo igual, porque estaba en la planificación", "Cambiarlo por otro material sin avisar", "El riesgo debe conocerlo quien planifica; por eso se consulta antes y no se improvisa."),
        ("abc", "{F} ¿Por qué se registra lo observado durante la experiencia?", "Para que la educadora pueda evaluar y ajustar lo planificado", "Para decidir qué niños no participarán la próxima vez", "Para poner una nota a cada niño que se entrega a su familia", "El registro sirve para evaluar la experiencia; no es para excluir ni para calificar."),
        ("=", "{F} Regla de ejemplo para este ejercicio: se forman grupos de 6 niños y cada grupo necesita un adulto cerca (la proporción real depende de la norma vigente). Con la educadora y la técnica como únicos adultos, ¿cuántos grupos quedan sin adulto?", "18//6-2", "Se calcula cuántos grupos hay y se restan los dos que tienen adulto.", " grupo"),
        ("abc", "{F} Al llegar, la técnica ve agua derramada en el piso de la sala donde irá la experiencia con recorrido en el suelo. ¿Qué hace?", "Avisa a la educadora y corrige el riesgo antes de comenzar", "Empieza igual y pide a los niños que caminen con cuidado", "Suspende la experiencia y no le cuenta a nadie", "El riesgo se corrige antes de empezar y se informa a la responsable de la sala."),
        ("abc", "Mañana la educadora faltará y llegará una reemplazante. ¿Qué debe hacer la técnica con la planificación?", "Entregarle la planificación escrita y apoyar según lo planificado", "Reemplazar a la educadora y decidir todo ella sola", "Guardar la planificación y hacer lo que recuerde", "La planificación escrita permite que otra persona responsable continúe la experiencia."),
        ("abc", "Un compañero dice: «Como la técnica conoce bien al grupo, puede cambiar la planificación cuando quiera». ¿Qué corresponde responder?", "Que puede proponer el cambio, pero decide la educadora, que responde por la sala", "Que sí, porque trabaja todos los días con los niños", "Que sí, siempre que lo anote al terminar el día", "Conocer al grupo permite proponer, pero la responsabilidad de planificar es de la educadora."),
        ("abc", "{F} Durante la experiencia, un niño llora y no quiere participar. ¿Qué es lo más adecuado?", "Acompañarlo con calma, respetar su ritmo y contar a la educadora lo observado", "Obligarlo a participar para que se acostumbre", "Dejarlo solo en un rincón hasta que termine", "Acompañar respeta su ritmo y la educadora puede decidir cómo ayudarlo."),
        ("=", "{F} Cada niño usa 3 hojas de papel y se agregan 6 hojas de repuesto. ¿Cuántas hojas se preparan para el bloque?", "18*3+6", "Se multiplican las hojas por cada niño presente y se suman las de repuesto.", " hojas"),
        ("abc", "Una técnica anota solo «la actividad salió bien». ¿Qué le falta para ser un buen registro?", "Hechos observables: quiénes participaron, qué hicieron y qué dificultades hubo", "Una opinión más larga sobre la forma de ser de cada niño", "Un posible diagnóstico de quienes participaron menos", "El registro útil describe hechos; opinar o diagnosticar sale del rol de la técnica."),
    ],
    ctx=("abc", "{F} La educadora deja planificada una experiencia con cajas de cartón para construir una casa grande entre todos. Al revisar el material, la técnica ve una caja con grapas sueltas en el borde. ¿Qué hace?", "Aparta esa caja, avisa a la educadora y usa solo cajas sin riesgo", "Deja la caja y dice a los niños que no la toquen", "Quita las grapas con las manos y sigue sin avisar", "El material riesgoso se aparta y se informa; confiar en que los niños no lo toquen no es suficiente."),
    sc=[
        ("En Atención de Párvulos: ¿quién responde por la planificación de la sala?", "La educadora a cargo", "La educadora diseña y responde por la experiencia; la técnica la apoya."),
        ("¿Qué haces si el material planificado parece riesgoso para la edad del grupo?", "Consulto a la educadora antes de usarlo", "La decisión sobre materiales riesgosos corresponde a quien planifica."),
        ("En el registro de una experiencia, ¿qué anotas?", "Hechos observados, sin etiquetas", "Los hechos permiten evaluar; las etiquetas y opiniones no."),
    ],
    op=("Planificación de ejemplo de la educadora: «Nivel medio, 10:00 a 10:40, 16 niños y niñas. Experiencia: jugar a clasificar hojas secas, ya limpias, en tres cajas según su tamaño. Material: 3 cajas bajas y una bolsa de hojas secas lavables». "
        "Escribe: dos tareas de la técnica antes de la experiencia, una durante y una después; un riesgo posible y a quién avisarías; y una frase de registro con un hecho observado.",
        "Antes: revisar que las hojas estén limpias y ordenar las cajas; avisar a la educadora si falta algo. Durante: acompañar a los niños y observar cómo clasifican. Después: ordenar y anotar lo ocurrido. Riesgo: que algún niño se lleve una hoja a la boca; aviso a la educadora. Registro: «Lía ordenó las hojas en tres cajas sin ayuda».",
        ["nombra tareas de antes, durante y después", "identifica un riesgo y avisa a la educadora", "el registro describe un hecho observable"],
        ["hoja con cuatro tareas, un riesgo con aviso y una frase de registro"],
        ["decidir cambiar la actividad sin consultar a la educadora", "anotar una opinión en vez de un hecho", "olvidar avisar el riesgo"],
        "Pregunta: «¿tu frase de registro dice qué hizo el niño o qué piensas tú de él?». Si opina, pídele reescribirla como hecho."),
    reinforce="Escribe tres cosas que hace la técnica y tres que decide solo la educadora en una experiencia de aprendizaje.",
    extend="Explica con un ejemplo inventado por qué registrar con hechos ayuda a mejorar la experiencia del día siguiente.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (áreas del desarrollo, de ejemplo). Cognitivo: agrupar objetos por color, contar, resolver encajes. Emocional: poner nombre a lo que se siente, calmarse con ayuda, expresar gusto o miedo. "
     "Social: esperar turno, compartir, jugar con otros. Psicomotor: gatear, caminar, saltar, ensartar argollas grandes, agarrar con los dedos.")
build(
    O1, 2, F,
    use="Aprenderé las cuatro áreas del desarrollo de niños y niñas, los momentos de una experiencia de aprendizaje y dos instrumentos simples para observar.",
    prior=["Sé qué hace la técnica y qué hace la educadora.", "Sé sumar y restar.", "Sé leer una ficha."],
    explain=[
        "El desarrollo de un niño o niña se observa en cuatro áreas que se influyen entre sí. El área cognitiva tiene que ver con pensar, comparar y resolver. El área emocional, con reconocer y expresar lo que se siente. El área social, con relacionarse con otros. El área psicomotora, con mover el cuerpo y usar las manos. Una misma experiencia suele trabajar más de un área.",
        "Una experiencia de aprendizaje tiene tres momentos: el inicio, que motiva y presenta el material; el desarrollo, donde los niños exploran y juegan; y el cierre, donde se comenta lo vivido y se ordena. Durante ella se observa con instrumentos simples. La lista de cotejo marca si una conducta ocurre o no. El registro anecdótico cuenta con pocas palabras un hecho tal como ocurrió.",
        "Las cuatro áreas no son un diagnóstico: son una manera de ordenar lo que se observa para que la educadora planifique mejor. La técnica nunca califica a un niño ni lo compara con otros." + LIM,
    ],
    vocab=[("área cognitiva", "pensar, comparar, contar y resolver problemas"), ("área emocional", "reconocer y expresar lo que se siente"), ("área social", "relacionarse y jugar con otros"), ("área psicomotora", "mover el cuerpo y usar las manos"), ("inicio, desarrollo y cierre", "los tres momentos de una experiencia de aprendizaje"), ("lista de cotejo", "instrumento que marca si una conducta ocurre o no"), ("registro anecdótico", "relato breve de un hecho observado, tal como ocurrió")],
    worked=[
        ("Ubicar una conducta en su área", "Un niño de ejemplo espera con paciencia que otro termine de usar la pala. ¿Qué área se observa?", ["Esperar y respetar el turno es relacionarse con otros.", "Corresponde al área social."], "Área social"),
        ("Completar los momentos", "Una experiencia de ejemplo dura 50 minutos: el inicio dura 10 y el cierre 15. ¿Cuánto dura el desarrollo?", ["Se suman inicio y cierre: 10 + 15 = 25.", "50 − 25 = 25."], "25 minutos"),
    ],
    mistakes=[("Pensar que una experiencia trabaja una sola área y que las demás «no cuentan».", "El desarrollo es integral: al saltar en grupo se trabaja el cuerpo, las reglas y la cooperación a la vez.", "Indica el área principal y nombra las otras que también aparecen."),
              ("Escribir en un registro anecdótico «es muy tímida».", "Es una etiqueta, no un hecho observado, y puede marcar a la niña.", "Escribe qué hizo o dijo: «Se quedó mirando el juego y no se acercó».")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué se observa en el área emocional?", "Cómo reconocen y expresan lo que sienten", "Cuánto pesan y miden", "Cuántos números cuentan en voz alta", "El área emocional trata de las emociones; peso y conteo son otros temas."),
        ("abc", "{F} Un niño dice «estoy enojado» y pide ayuda para calmarse. ¿Qué área se observa?", "Emocional", "Psicomotor", "Cognitivo", "Poner nombre a lo que se siente y calmarse con ayuda está en el área emocional de la ficha."),
        ("abc", "{F} Una niña salta con los dos pies sobre un aro dibujado en el piso. ¿Qué área se observa?", "Psicomotor", "Social", "Emocional", "Saltar es mover el cuerpo, que la ficha ubica en el área psicomotora."),
        ("abc", "La educadora pide que, antes de jugar, los niños vean el material y cuenten qué creen que harán. ¿Qué momento de la experiencia es?", "El inicio", "El desarrollo", "El cierre", "Presentar el material y motivar es lo que se hace al comienzo."),
        ("abc", "¿Qué diferencia a una lista de cotejo de un registro anecdótico?", "La lista marca si una conducta ocurre o no; el registro cuenta un hecho con pocas palabras", "La lista cuenta un hecho; el registro solo marca casillas", "No hay diferencia: los dos sirven para calificar con nota", "La lista usa marcas de sí o no y el registro es un relato breve."),
        ("abc", "{F} Un niño agrupa bloques rojos y azules en dos montones. ¿Qué área se trabaja principalmente?", "Cognitiva", "Social", "Psicomotora", "Agrupar objetos por color es un trabajo de pensar y comparar, es decir, cognitivo."),
        ("=", "Una experiencia de ejemplo dura 45 minutos: el inicio dura 10 y el desarrollo 25. ¿Cuántos minutos quedan para el cierre?", "45-10-25", "Al total se le restan el inicio y el desarrollo.", " minutos"),
        ("abc", "{F} La educadora quiere trabajar el área psicomotora con un grupo de nivel medio. ¿Qué experiencia calza mejor?", "Un circuito de aros en el piso para saltar con ambos pies", "Armar encajes de formas sobre una mesa", "Esperar el turno para usar un juguete compartido", "Saltar trabaja el cuerpo; los encajes son cognitivos y esperar turno es social."),
        ("abc", "Un objetivo dice: «Que los niños expresen con una carita cómo se sienten hoy». ¿Qué área trabaja principalmente?", "Emocional", "Cognitiva", "Psicomotora", "Expresar cómo se sienten es el centro del área emocional."),
        ("abc", "{F} Dos niños arman juntos una torre de bloques grandes y se turnan para ponerlos. ¿Qué áreas se observan?", "Psicomotora, cognitiva y social", "Solo psicomotora", "Solo emocional", "Mover los bloques, planear la torre y turnarse mezcla tres áreas a la vez."),
        ("abc", "Un compañero afirma: «El área emocional solo se trabaja cuando se lee un cuento». ¿Qué corresponde responder?", "Que se trabaja durante toda la jornada, por ejemplo al ayudar a nombrar lo que sienten", "Que sí, porque los cuentos son lo único que habla de emociones", "Que no se trabaja en el jardín, solo en la casa", "Las emociones aparecen en todo momento y la técnica puede acompañarlas siempre."),
        ("=", "En una lista de cotejo de ejemplo, de 15 niños, 11 logran la conducta A y 9 logran la conducta B. ¿Cuántos «no logran» entre las dos conductas sumadas?", "(15-11)+(15-9)", "Se restan los que logran de los 15 en cada conducta y se suman los resultados.", " casos"),
        ("abc", "La técnica quiere dejar escrito tal como ocurrió que Noa dijo «yo ayudo» y pasó el jabón a Tomás. ¿Qué instrumento usa?", "Un registro anecdótico", "Una lista de cotejo", "Un diagnóstico de conducta", "Un relato breve de un hecho es un registro anecdótico; la lista solo marca sí o no."),
    ],
    ctx=("abc", "{F} Durante el cierre de una experiencia, un niño de ejemplo dice que le dio miedo el ruido del tambor y se tapa los oídos. ¿Qué hace la técnica?", "Acompañarlo con calma, anotar el hecho sin etiquetas y contárselo a la educadora", "Decirle que no es nada y que se calme ya", "Anotar que es un niño miedoso", "Acompañar y registrar el hecho permite a la educadora ajustar sin etiquetar al niño."),
    sc=[
        ("En Atención de Párvulos: ¿qué área trabaja compartir un juguete?", "Social", "Compartir es relacionarse con otros, que es el área social."),
        ("¿Cuáles son los tres momentos de una experiencia de aprendizaje?", "Inicio, desarrollo y cierre", "Así se ordenan la motivación, el juego y el comentario final."),
        ("¿Qué instrumento marca si una conducta ocurre o no?", "La lista de cotejo", "La lista usa casillas de sí o no; el anecdótico narra un hecho."),
    ],
    op=("Una educadora de ejemplo planifica esta experiencia para el nivel de transición: «Representar con títeres de calcetín una historia inventada por el grupo y turnarse para hablar». "
        "Escribe: el área principal y otra área que también aparece, con una acción observable de cada una; qué ocurriría en el inicio, el desarrollo y el cierre; y un registro anecdótico de un hecho imaginado sin etiquetas.",
        "Área principal: social (turnarse). Otra: cognitiva (inventar una historia con orden). Acciones: espera su turno; cuenta qué pasó primero y qué después. Inicio: presentar los títeres y preguntar de qué trataría la historia. Desarrollo: los niños usan los títeres y turnan. Cierre: comentar qué parte les gustó y guardar. Registro: «Camila esperó su turno y dijo: ahora habla el lobo».",
        ["nombra dos áreas con acciones observables", "ordena inicio, desarrollo y cierre", "el registro es un hecho, sin etiquetas"],
        ["hoja con dos áreas y acciones, tres momentos y un registro anecdótico"],
        ["decir que solo se trabaja una área", "escribir en el registro una etiqueta como «es tímida»", "confundir los momentos de la experiencia"],
        "Pregunta: «¿tu registro podría verlo otra persona y entender qué pasó sin saber cómo es la niña?». Si no, pídele más hechos y menos opinión."),
    reinforce="Escribe una conducta de ejemplo para cada una de las cuatro áreas del desarrollo.",
    extend="Explica por qué ordenar lo observado en áreas no es lo mismo que hacer un diagnóstico de un niño o niña.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (planificación de la educadora, de ejemplo). Nivel de transición, 16 niños y niñas, de 11:00 a 11:45. Objetivo: expresar con dibujos algo que les gustó del fin de semana. "
     "Material disponible: hojas, 20 crayones gruesos, pintura lavable y 4 mesas. Nota de la educadora: Emilia usa silla de ruedas y necesita una mesa con espacio libre debajo; Mateo llegó hace una semana y aún habla poco.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso con una planificación escrita: leer el objetivo, organizar tiempos y grupos, cuidar a cada niño y avisar a la educadora.",
    prior=["Conozco las cuatro áreas del desarrollo.", "Conozco inicio, desarrollo y cierre.", "Sé repartir una cantidad en grupos iguales."],
    explain=[
        "Para analizar un caso de trabajo se lee primero el objetivo de la planificación: lo que los niños deben vivir o expresar. Luego se revisan los datos: cuántos niños son, cuánto tiempo hay, qué material existe y qué indicó la educadora sobre cada niño. Con eso se organiza la sala y se comprueba que la actividad cumple el objetivo, no solo que mantenga ocupados a los niños.",
        "La inclusión significa que todos los niños y niñas participan, cada uno con los apoyos que necesita. Si la educadora anota que una niña usa silla de ruedas, la técnica prepara una mesa donde pueda acercarse, sin hacer comentarios sobre su cuerpo. Si un niño habla poco, se lo invita sin presionarlo y se aceptan otras formas de expresarse, como señalar o dibujar.",
        "Todo lo que la educadora escribe sobre un niño se trata con reserva: se usa para ayudar en la sala y no se comenta con otras personas. La técnica no interpreta ni diagnostica; ante dudas pregunta a la educadora." + LIM,
    ],
    vocab=[("objetivo", "lo que se espera que los niños vivan, hagan o expresen en la experiencia"), ("inclusión", "participación de todos los niños y niñas con los apoyos que cada uno necesita"), ("apoyo", "ayuda o ajuste que permite participar a un niño o niña"), ("confidencialidad", "reserva con los datos y notas sobre un niño o su familia"), ("organizar la sala", "disponer mesas, materiales y grupos antes de empezar")],
    worked=[
        ("Revisar el cumplimiento del objetivo", "El objetivo de ejemplo es que los niños inventen una historia. Una propuesta pide que copien un cuento de la pizarra. ¿Cumple el objetivo?", ["El objetivo pide inventar, es decir, crear algo propio.", "Copiar no es inventar."], "No cumple: copiar no es inventar una historia"),
        ("Repartir material", "Hay 24 niños y se reparten en 4 mesas iguales. ¿Cuántos niños hay por mesa?", ["Se divide el total entre las mesas.", "24 ÷ 4 = 6."], "6 niños por mesa"),
    ],
    mistakes=[("Pedirle a Mateo que cuente frente a todos qué hizo el fin de semana, porque «así aprende a hablar».", "Lo expone sin su consentimiento y puede aumentar su inseguridad.", "Invítalo a dibujar y a mostrar su dibujo cuando quiera."),
              ("Sentar a Emilia en cualquier mesa y moverla después cuando moleste.", "No se preparó el espacio y se le señala como un problema.", "Antes de comenzar, deja lista la mesa con espacio libre, tal como indicó la educadora.")],
    T=[
        ("abc", "{F} ¿Cuál es el objetivo de la experiencia?", "Que los niños expresen con dibujos algo que les gustó del fin de semana", "Que los niños aprendan a copiar figuras", "Que los niños pinten todas las hojas disponibles", "El objetivo escrito habla de expresar con dibujos algo vivido, no de copiar ni de gastar material."),
        ("abc", "{F} ¿Cuántas mesas hay disponibles?", "4", "16", "20", "La ficha indica 4 mesas; 16 son los niños y 20 los crayones."),
        ("abc", "{F} ¿Qué necesita Emilia, según la nota de la educadora?", "Una mesa con espacio libre debajo", "Una actividad distinta a la de sus compañeros", "Que otro niño dibuje por ella", "La nota pide una mesa adecuada; no pide separarla ni reemplazarla."),
        ("=", "{F} Los 16 niños se reparten en partes iguales en las 4 mesas. ¿Cuántos niños hay en cada mesa?", "16//4", "Se divide el total de niños entre las mesas.", " niños"),
        ("abc", "{F} ¿Cómo debe invitar la técnica a Mateo a participar?", "Invitarlo a dibujar y a mostrar su dibujo solo si quiere", "Pedirle que cuente frente a todos su fin de semana", "No invitarlo, para no incomodarlo", "Se invita sin presionar; excluirlo o exponerlo no respeta su ritmo."),
        ("abc", "{F} Una propuesta es que cada niño coloree un dibujo ya impreso de un animal. ¿Cumple el objetivo?", "No, porque no expresan algo vivido por ellos", "Sí, porque usan los crayones", "Sí, porque todos terminan al mismo tiempo", "El objetivo pide expresar una vivencia propia, no colorear un dibujo ajeno."),
        ("=", "{F} Se organiza la experiencia: 10 minutos de inicio y 10 de cierre. ¿Cuántos minutos quedan para el desarrollo?", "(11*60+45)-(11*60)-10-10", "Se calcula la duración total y se restan inicio y cierre.", " minutos"),
        ("abc", "{F} ¿Cómo prepara la técnica la mesa de Emilia?", "Antes de empezar, deja libre el espacio bajo la mesa y coloca los materiales a su alcance", "La prepara cuando Emilia llega y avisa que no cabe", "Le entrega los materiales aparte en el piso", "Se prepara antes, tal como indicó la educadora, para que participe igual que todos."),
        ("abc", "{F} Una niña dibuja una casa y dice que en ella hay una tía. La técnica piensa «dibuja mucho a la familia, ¿pasará algo?». ¿Qué corresponde?", "Escuchar con interés sin sacar conclusiones; si dijera algo que preocupa, anotar sus palabras exactas y avisar a la educadora", "Preguntarle varias veces qué le pasa en su casa", "Anotar que probablemente tiene un problema familiar", "Un dibujo no es un diagnóstico; interpretar sin formación puede dañar a la niña y a su familia."),
        ("abc", "{F} Hay 20 crayones para 16 niños. Un compañero propone que cada niño tenga siempre 2 crayones. ¿Qué observación corresponde?", "No alcanza: 2 por niño son 32 y solo hay 20", "Sí alcanza, porque hay más crayones que niños", "Alcanza si se usan solo las mesas con menos niños", "Dos crayones por niño requieren 32; hay 20, así que se deben compartir."),
        ("abc", "{F} Mateo dibuja solo líneas y no quiere mostrar su dibujo. ¿Qué escribe la técnica en el registro?", "«Dibujó líneas de colores y no quiso mostrarlo»", "«Mateo no sabe dibujar»", "«Mateo tiene problemas para comunicarse»", "El registro cuenta lo que hizo; las otras frases son juicios sin respaldo."),
        ("=", "{F} Al comenzar, la técnica reparte 1 hoja a cada niño y deja 5 hojas de repuesto en cada mesa. ¿Cuántas hojas prepara en total?", "16+5*4", "Se suman las hojas por niño y las de repuesto de las 4 mesas.", " hojas"),
        ("abc", "{F} Otra técnica comenta con una vecina del jardín que Emilia usa silla de ruedas y que Mateo «es raro porque no habla». ¿Qué observación corresponde?", "No se comentan datos ni juicios sobre los niños con personas ajenas a la sala", "Es válido, mientras sea fuera del jardín", "Es válido, porque son datos que todos saben", "Las notas sobre los niños son confidenciales y los juicios no ayudan a nadie."),
    ],
    ctx=("abc", "{F} A mitad de la experiencia, el pincel de Emilia cae al piso y ella no alcanza a recogerlo. Otro niño dice en voz alta que «ella no puede». ¿Qué hace la técnica?", "Recoge el pincel con naturalidad, ofrece ayuda a quien la pida y recuerda que todos pueden pedir ayuda", "Pide que Emilia pinte desde su silla y no se mueva más", "Retira los pinceles para evitar que se caigan", "La ayuda se ofrece con respeto y se aclara que todos pueden pedirla; retirar el material excluye."),
    sc=[
        ("En Atención de Párvulos: ¿qué se lee primero al analizar una planificación?", "El objetivo", "El objetivo dice qué deben vivir los niños y orienta toda la organización."),
        ("¿Qué haces con una nota de la educadora sobre un niño?", "La uso para ayudar y no la comento con otras personas", "Las notas son confidenciales y solo sirven para atender mejor."),
        ("¿Cómo invitas a participar a un niño que habla poco?", "Con respeto, sin presionar, aceptando otras formas de expresarse", "Presionarlo lo expone; ofrecer opciones respeta su ritmo."),
    ],
    op=("Planificación de ejemplo: nivel medio, 12 niños y niñas, de 10:00 a 10:30. Objetivo: explorar sonidos con objetos de la sala y decir cuál les gustó más. Material: 6 cajas de cartón con tapa y 12 cucharas de madera lisas. "
        "Nota de la educadora: Amaru se asusta con los ruidos fuertes. "
        "Escribe: cómo organizarías 12 niños en 3 grupos con su material; cómo cuidarías a Amaru sin dejarlo fuera; qué observarías para saber si se cumplió el objetivo; y un registro con un hecho imaginado.",
        "Grupos de 4 niños con 2 cajas y 4 cucharas cada uno. Amaru: empezar con golpes suaves, dejarlo elegir su lugar y su ritmo y tener un rincón tranquilo si lo pide, sin comentarlo frente a otros. Observaría si cada niño explora sonidos y dice cuál le gustó. Registro: «Amaru golpeó una caja despacio y dijo: esta suena bonito».",
        ["divide a los niños y el material en partes iguales", "cuida a Amaru sin excluirlo ni etiquetarlo", "relaciona lo observado con el objetivo"],
        ["hoja con grupos y materiales, cuidado de Amaru, qué observar y un registro"],
        ["dejar a Amaru fuera de la actividad", "repartir mal el material", "escribir una etiqueta en lugar de un hecho"],
        "Pregunta: «¿qué pasaría si Amaru no quiere tocar ninguna caja?». Debe responder que se respeta su ritmo y se avisa a la educadora."),
    reinforce="Reparte 18 niños en 3 mesas iguales y escribe cuántos crayones tendría cada mesa si hay 27 en total.",
    extend="Explica con un ejemplo inventado cómo se prepara una experiencia para que participen niños con distintas necesidades sin que nadie se sienta distinto.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (circuito de ejemplo). Nivel medio, 20 niños y niñas presentes, en 4 estaciones con 5 niños en cada una; los grupos rotan cada 8 minutos hasta pasar por todas las estaciones. "
     "Estación 1: 5 pelotas blandas. Estación 2: 6 aros en el piso. Estación 3: un túnel de tela. Estación 4: 10 cojines grandes. Regla de ejemplo: un adulto por cada 10 niños en esta actividad (la proporción real depende de la norma vigente). Adultos: la educadora y la técnica.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: calcular grupos, tiempos, material y adultos necesarios antes de realizar una experiencia.",
    prior=["Sé dividir un total en grupos iguales.", "Conozco la planificación y el registro.", "Sé calcular minutos entre dos horas."],
    explain=[
        "Un criterio técnico es una regla que se puede comprobar con datos. Para organizar un circuito, la técnica calcula cuántos grupos se forman (niños presentes divididos por niños por estación), cuánto dura en total (estaciones por minutos de cada rotación) y si el material alcanza para cada grupo. Si los datos no cuadran, no improvisa: informa a la educadora, que decide el ajuste.",
        "También se revisa la supervisión. Los adultos se ubican de modo que, entre todos, vean a todos los niños durante toda la actividad, y el espacio queda libre de obstáculos. La regla de adultos por niños de este cuaderno es solo un ejemplo; en un jardín real se aplica la proporción que fija la norma vigente. Cuando falta un niño, el cálculo se rehace con los presentes.",
        "Una rotación es el cambio ordenado de cada grupo a la estación siguiente. Revisar los números antes de empezar evita que una estación quede sin material, que sobren o falten niños o que la actividad se pase del bloque." + LIM,
    ],
    vocab=[("criterio técnico", "regla que se puede comprobar con datos"), ("estación", "lugar de la sala con un material y una tarea"), ("rotación", "cambio ordenado de cada grupo a la estación siguiente"), ("proporción adulto-niños", "cantidad de adultos para una cantidad de niños, según la norma vigente"), ("ajuste", "cambio que decide la educadora cuando los datos no cuadran")],
    worked=[
        ("Calcular grupos", "En otro circuito de ejemplo hay 15 niños y cada estación recibe 3. ¿Cuántos grupos se forman?", ["Se divide el total entre los niños por estación.", "15 ÷ 3 = 5."], "5 grupos"),
        ("Calcular duración", "Un circuito de ejemplo tiene 3 estaciones y cada rotación dura 6 minutos. ¿Cuánto dura en total?", ["Cada grupo pasa por las 3 estaciones.", "3 × 6 = 18."], "18 minutos"),
    ],
    mistakes=[("Empezar el circuito sin contar cuántos niños llegaron hoy.", "El cálculo del día anterior ya no sirve y pueden quedar estaciones con demasiados niños o sin ellos.", "Cuenta a los presentes y recalcula los grupos antes de comenzar."),
              ("Ubicarse las dos adultas en la misma estación, de espaldas al resto de la sala.", "Hay niños que quedan sin supervisión visual.", "Ubícate donde, junto con la otra adulta, vean todas las estaciones.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es una rotación en un circuito de estaciones?", "El cambio ordenado de cada grupo a la estación siguiente", "La elección de los niños que no participarán", "El orden en que se guardan los materiales", "En un circuito cada grupo rota para pasar por todas las estaciones."),
        ("=", "{F} ¿Cuántos grupos de 5 niños se forman con los niños presentes?", "20//5", "Se divide el total de niños entre los niños por estación.", " grupos"),
        ("abc", "{F} En la estación 2 hay 6 aros y llegan 5 niños. ¿Qué ocurre con el material?", "Alcanza y sobra un aro", "Faltan aros", "Alcanza justo, sin sobrar", "6 aros para 5 niños alcanzan y sobra 1."),
        ("=", "{F} ¿Cuántos minutos dura el circuito completo, sin contar la explicación inicial?", "4*8", "Cada grupo pasa por 4 estaciones de 8 minutos cada una.", " minutos"),
        ("abc", "{F} Con la regla de ejemplo, ¿alcanzan los adultos para los niños presentes?", "Sí: 20 niños necesitan 2 adultos y hay 2", "No: 20 niños necesitan 3 adultos", "Sí, pero solo si la técnica se queda en una estación", "20 niños dividido por 10 da 2 adultos, que son la educadora y la técnica."),
        ("abc", "¿Por qué se calcula la duración total antes de empezar un circuito?", "Para comprobar que cabe en el bloque disponible", "Para decidir qué niños terminarán primero", "Para que la educadora no tenga que planificar", "El cálculo previo muestra si el circuito entra en el tiempo del bloque."),
        ("=", "{F} Hoy faltan 3 niños. Con los presentes se forman grupos completos de 5. ¿Cuántos niños quedan sin grupo completo?", "20-3-5*3", "Se restan los ausentes y los tres grupos completos de 5 al total.", " niños"),
        ("=", "{F} La explicación inicial dura 5 minutos y la preparación 3 minutos. Si se parte a las 10:00, ¿cuántos minutos después de las 10:00 termina el circuito completo?", "5+3+4*8", "Se suman explicación, preparación y las cuatro rotaciones.", " minutos"),
        ("abc", "{F} Un niño se sube a un montón alto de cojines y se balancea. ¿Qué hace la técnica?", "Se acerca, le pide con calma que baje, reordena los cojines y avisa a la educadora", "Lo mira desde lejos para no interrumpir", "Retira el circuito completo sin avisar", "Se interviene de inmediato y con calma, y se informa a la educadora."),
        ("=", "{F} Llegan 12 niños más y quedan 32 en la actividad. Con la regla de ejemplo, un adulto por cada 10 niños o fracción, ¿cuántos adultos se necesitan?", "(32+9)//10", "Se divide en grupos de 10 y se redondea hacia arriba, porque 2 niños sobrantes también necesitan adulto.", " adultos"),
        ("abc", "{F} Las dos adultas proponen ubicarse en la estación 3 porque es la más entretenida. ¿Qué observación corresponde?", "Deben ubicarse donde, entre las dos, vean todas las estaciones", "Está bien, porque el túnel es el mayor riesgo", "Está bien si los niños saben las reglas", "La supervisión debe cubrir a todos los niños, no solo la estación más atractiva."),
        ("=", "{F} Cada niño pasa dos veces por el túnel y tarda 1 minuto cada vez. Para el grupo de 5, ¿cuántos minutos faltan respecto de los 8 de la rotación?", "5*2-8", "Se calculan los minutos necesarios para los pases del grupo y se restan los 8 disponibles.", " minutos"),
        ("abc", "{F} El bloque disponible es de 30 minutos y el circuito completo dura 32. ¿Qué corresponde?", "Informar a la educadora y proponer acortar cada rotación, que ella decide", "Terminar a las apuradas dejando una estación sin visitar", "Alargar el bloque sin avisar a nadie", "Ante datos que no cuadran se informa; el ajuste lo decide la educadora."),
    ],
    ctx=("abc", "{F} Al comenzar, la técnica cuenta 18 niños en la sala porque dos se quedaron en la sala de al lado con otra adulta. ¿Qué hace antes de partir?", "Confirmar con la educadora cuántos participan realmente y rehacer los grupos con ese número", "Partir con 20 niños y dejar sin pasar a los demás", "Formar los grupos con los números de la ficha sin contar", "Los grupos se calculan con los niños que realmente están y se confirma con quien planifica."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se calcula cuántos grupos se forman?", "Dividiendo los niños presentes entre los niños por estación", "El número de grupos depende de cuántos niños hay y de cuántos caben por estación."),
        ("¿Qué haces si el circuito dura más que el bloque disponible?", "Informo a la educadora para que decida el ajuste", "Cambiar la planificación es una decisión de quien responde por la sala."),
        ("¿De dónde sale la proporción real de adultos por niños?", "De la norma vigente", "Los números de los ejemplos del cuaderno no son la norma."),
    ],
    op=("Datos de ejemplo: nivel de transición, 24 niños y niñas, bloque de 45 minutos. Circuito de 3 estaciones (cuerda en el piso para caminar sobre ella, cajas bajas para pasar por encima y pelotas blandas para pasarse en parejas) con grupos de 8 niños; cada rotación dura 10 minutos. Adultos: la educadora y la técnica. "
        "Escribe: cuántos grupos se forman, cuánto dura el circuito, si cabe en el bloque, cómo ubicarían los adultos para ver a todos y qué le dirías a la educadora si no cupiera.",
        "Grupos: 24 ÷ 8 = 3. Duración: 3 × 10 = 30 minutos; cabe en 45, y sobran 15 para explicar y ordenar. Los adultos se ubican en lados opuestos, de modo que entre los dos vean las tres estaciones. Si no cupiera: «El circuito dura más que el bloque; ¿acortamos las rotaciones o quitamos una estación?», para que ella decida.",
        ["calcula grupos y duración con los datos", "compara la duración con el bloque", "ubica a los adultos para ver a todos y propone consultar a la educadora"],
        ["hoja con tres cálculos y una frase de aviso a la educadora"],
        ["dividir mal el número de grupos", "no comparar con el bloque", "decidir el ajuste sin avisar a la educadora"],
        "Pregunta: «¿qué pasaría si faltan 4 niños?». Debe recalcular con 20 y avisar si hay un grupo incompleto."),
    reinforce="Inventa un circuito de 3 estaciones para 12 niños y calcula grupos y duración total con rotaciones de 5 minutos.",
    extend="Explica por qué la regla de adultos por niños de un ejemplo no puede usarse como norma en un jardín real.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (dos propuestas, de ejemplo). Objetivo: que el nivel de transición (16 niños y niñas) cuente hasta 10 jugando. Pauta de calidad (1 punto por criterio): C1 coincide con el objetivo; C2 es adecuada para la edad; C3 el material es seguro; C4 todos pueden participar; C5 tiene inicio, desarrollo y cierre. "
     "Propuesta A: lanzar una pelota blanda a una caja contando hasta 10; turnos de 4 niños de 5 minutos cada uno; una niña que usa silla de ruedas no alcanza la caja, que está sobre una mesa alta. Cumple C1, C2, C3 y C5. "
     "Propuesta B: ensartar cuentas pequeñas de plástico en un cordón y contar 10; no hay cierre. Cumple C1, C2 y C4.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos propuestas de experiencia con una pauta de calidad, a proponer mejoras y a informar lo observado después de aplicarla.",
    prior=["Sé organizar grupos y tiempos.", "Sé registrar hechos observables.", "Conozco los momentos de una experiencia."],
    explain=[
        "Comparar alternativas significa revisar cada propuesta con los mismos criterios. En este cuaderno se usa una pauta de calidad con cinco criterios: coincide con el objetivo, es adecuada para la edad, usa material seguro, permite que todos participen y tiene inicio, desarrollo y cierre. Se cuenta un punto por criterio cumplido; el puntaje ayuda a decidir, pero lo importante es entender por qué un criterio no se cumple.",
        "Verificar la calidad es comprobar con hechos que la experiencia funcionó. Después de aplicarla, la técnica cuenta cuántos niños lograron lo esperado, cuántos necesitaron ayuda y qué dificultades hubo. Con eso la educadora decide si repite la experiencia o la ajusta. La técnica puede proponer mejoras, como bajar la caja a una altura accesible, pero no impone su elección.",
        "Un puntaje alto no reemplaza el juicio de la educadora, y un puntaje bajo no significa que la propuesta se descarte siempre: muchas veces una mejora simple la corrige. El objetivo es que todos los niños y niñas aprendan de forma segura." + LIM,
    ],
    vocab=[("pauta de calidad", "lista de criterios para comparar propuestas"), ("criterio", "aspecto que se revisa en cada propuesta"), ("alternativa", "una de las propuestas que se pueden elegir"), ("verificar", "comprobar con hechos que algo funcionó"), ("mejora", "cambio simple que corrige un criterio no cumplido")],
    worked=[
        ("Calcular un puntaje", "Una propuesta de ejemplo cumple C1, C2, C4 y C5, pero no C3. ¿Cuántos puntos obtiene?", ["Se cuenta un punto por criterio cumplido.", "Son 4 criterios cumplidos."], "4 puntos"),
        ("Proponer una mejora", "Una propuesta de ejemplo usa una cuerda en alto para que los niños se cuelguen. No cumple C3. ¿Qué mejora se propone?", ["La mejora debe corregir el riesgo.", "Se propone reemplazar la actividad por saltar sobre una cuerda tendida en el piso y consultar a la educadora."], "Cambiar la cuerda a nivel del piso y consultar a la educadora"),
    ],
    mistakes=[("Elegir una propuesta porque «se ve más linda».", "Se decide por gusto y no por criterios que cuidan el aprendizaje y la seguridad.", "Aplica la pauta a ambas propuestas y compara los puntajes y sus razones."),
              ("Informar «el juego salió perfecto» sin contar cuántos niños lograron contar hasta 10.", "No hay datos para saber si se cumplió el objetivo.", "Informa cuántos lo lograron, cuántos necesitaron ayuda y qué pasó.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿para qué sirve una pauta de calidad?", "Para comparar propuestas con los mismos criterios", "Para calificar con nota a cada niño", "Para reemplazar la planificación de la educadora", "La pauta compara propuestas con criterios iguales; no califica niños ni reemplaza a la educadora."),
        ("abc", "{F} ¿Qué criterio no cumple la propuesta A?", "C4: todos pueden participar", "C1: coincide con el objetivo", "C3: el material es seguro", "La niña en silla de ruedas no alcanza la caja alta, así que no todos participan."),
        ("abc", "{F} ¿Por qué la propuesta B no cumple el criterio de material seguro?", "Porque las cuentas pequeñas podrían tragarse", "Porque el cordón es de color", "Porque hay 16 niños en el grupo", "Las piezas pequeñas pueden ser tragadas por niños, por eso no cumple C3."),
        ("=", "{F} ¿Cuántos minutos dura el desarrollo de la propuesta A, si los 16 niños lanzan en turnos de 4 niños de 5 minutos cada uno?", "16//4*5", "Se calcula la cantidad de turnos y se multiplica por los minutos de cada uno.", " minutos"),
        ("abc", "¿Qué significa verificar la calidad de una experiencia ya realizada?", "Comprobar con hechos cuántos niños lograron lo esperado y qué dificultades hubo", "Comprobar que los niños hayan terminado rápido", "Comprobar que la sala haya quedado ordenada", "Verificar es comparar el objetivo con lo que realmente ocurrió, con hechos."),
        ("abc", "{F} Una compañera elige la propuesta B porque «es más bonita». ¿Qué observación corresponde?", "Se decide con la pauta de criterios, no por gusto", "Está bien: lo bonito motiva a los niños", "Está bien si a la educadora también le gusta", "Una elección por gusto no considera la seguridad ni la participación."),
        ("abc", "{F} ¿Qué mejora simple corrige el problema de la propuesta A?", "Poner la caja a una altura que alcance cualquier niño", "Quitar a la niña del juego", "Pedirle a otro niño que lance por ella", "Bajar la caja permite que todos lancen, incluida la niña."),
        ("=", "{F} La propuesta A tiene 4 pelotas blandas en uso en cada turno y hay 6 en la sala. ¿Cuántas pelotas quedan de reserva?", "6-4", "A las pelotas de la sala se les restan las que se usan en cada turno.", " pelotas"),
        ("abc", "{F} Una propuesta C usa tijeras con filo para recortar números pequeños con 3 años de edad. ¿Qué criterio debería revisar primero la técnica?", "C3, el material seguro", "C1, el objetivo", "C5, el cierre", "Tijeras con filo en niños pequeños es un riesgo de seguridad."),
        ("=", "{F} La propuesta B cambia las cuentas pequeñas por argollas grandes y agrega un cierre. ¿Cuántos puntos tendría?", "3+1+1", "A los 3 puntos actuales se suman los criterios C3 y C5 ahora cumplidos.", " puntos"),
        ("abc", "{F} Tras aplicar A con la caja baja, 13 de 16 niños contaron hasta 10 sin ayuda y 3 necesitaron ayuda. ¿Qué informa la técnica a la educadora?", "Que 13 lo lograron sin ayuda y 3 necesitaron apoyo, con lo que observó en cada caso", "Que salió perfecto", "Que 3 niños no saben contar", "Informar con cifras y hechos permite decidir; las otras frases exageran o etiquetan."),
        ("=", "{F} En una segunda aplicación, 15 de los 16 niños contaron sin ayuda. ¿Cuántos niños más que en la primera aplicación (13) lo lograron?", "15-13", "Se restan los que lo lograron antes a los que lo lograron ahora.", " niños"),
        ("abc", "{F} La educadora decide aplicar la propuesta B ajustada, pero la técnica creía mejor la A. ¿Qué hace?", "Respeta la decisión y le entrega por escrito sus observaciones para la próxima vez", "Aplica la A sin avisar, porque obtuvo más puntos", "Se niega a participar en la experiencia", "La decisión es de la educadora; la técnica aporta sus observaciones."),
    ],
    ctx=("abc", "{F} La técnica ve que, en la propuesta A, un niño se frustra porque no acierta a la caja y deja de jugar. ¿Qué hace?", "Lo acompaña, le propone lanzar desde más cerca y anota lo ocurrido para la educadora", "Le dice que se esfuerce más para ser como los demás", "Lo deja sentado para que no moleste", "Se ajusta el desafío sin compararlo con otros y se registra el hecho."),
    sc=[
        ("En Atención de Párvulos: ¿cuántos puntos da la pauta por cada criterio cumplido?", "Un punto", "La pauta cuenta un punto por criterio cumplido."),
        ("¿Qué haces con una propuesta que no cumple un criterio?", "Busco una mejora simple y la consulto a la educadora", "Muchas veces un ajuste corrige el criterio sin descartar la propuesta."),
        ("¿Con qué se verifica que una experiencia cumplió su objetivo?", "Con hechos observados y cifras de los niños que lo lograron", "Los hechos y las cifras muestran qué ocurrió realmente."),
    ],
    op=("Dos propuestas de ejemplo para que el nivel medio (12 niños) explore texturas. Propuesta X: tocar con las manos telas suaves, rugosas y lisas, dentro de cajas, con inicio, desarrollo y cierre; todas las telas están limpias y sin hilos sueltos. Propuesta Y: oler y probar frutas diversas sin avisar a las familias; sin cierre. Pauta: C1 objetivo, C2 edad, C3 seguridad, C4 participación, C5 inicio-desarrollo-cierre. "
        "Escribe: el puntaje de cada propuesta con una razón por criterio no cumplido, cuál recomendarías a la educadora y una mejora para la otra.",
        "X cumple C1, C2, C3, C4 y C5 (5 puntos). Y: cumple C1 y C2, pero no C3 (probar alimentos sin conocer alergias ni avisar a las familias puede ser riesgoso), no C4 (si algún niño no puede comer algo, no participa) ni C5 (no tiene cierre): 2 puntos. Recomiendo X. Mejora para Y: usar solo olores con material lavable, sin probar nada, y agregar un cierre.",
        ["asigna puntajes coherentes con la pauta", "da una razón por cada criterio no cumplido", "recomienda sin decidir por la educadora y propone una mejora"],
        ["hoja con dos puntajes, razones, recomendación y una mejora"],
        ["decidir por gusto", "no explicar los criterios que no se cumplen", "proponer una mejora que no corrige el riesgo"],
        "Pregunta: «¿qué dirías si la educadora prefiere Y?». Debe respetar su decisión y ofrecer su observación."),
    reinforce="Aplica la pauta de cinco criterios a una actividad de ejemplo inventada y cuenta los puntos.",
    extend="Explica por qué un puntaje alto en la pauta no reemplaza el juicio de la educadora.",
)

# ============================================================ OAE-01, clase 6
F = ("Ficha 6 (registro de la experiencia, de ejemplo). Nivel medio, 14 niños y niñas presentes de 16 matriculados. Objetivo: explorar texturas con las manos. Hechos: 12 tocaron las tres telas; 2 tocaron solo la lisa; "
     "Sofía dijo «áspero» al tocar la tela rugosa; Bruno retiró la mano y miró a la técnica. Incidente: se derramó una bandeja con agua, nadie se golpeó y se secó el piso. Sugerencia de la técnica: más tiempo para la última tela.")
build(
    O1, 6, F,
    use="Aprenderé a registrar con hechos una experiencia ya realizada y a comunicar el resultado y las sugerencias a la educadora de forma clara y respetuosa.",
    prior=["Sé comparar propuestas con una pauta.", "Distingo hechos de opiniones.", "Sé sumar y restar."],
    explain=[
        "Un buen registro de una experiencia incluye: la fecha, el grupo, el objetivo, los hechos observados, los incidentes y las sugerencias. Los hechos se escriben tal como ocurrieron: quién hizo qué y cuántos niños lo lograron. Las interpretaciones, como «es miedoso», no van en el registro porque no se pueden comprobar y pueden marcar al niño.",
        "Comunicar el resultado es contarlo a la educadora de forma oportuna. Lo urgente, como un incidente o una situación de riesgo, se avisa de inmediato y de palabra. Lo demás se entrega por escrito, con lenguaje respetuoso y sin comparar niños entre sí. Si el registro tiene números, deben cuadrar: los presentes más los ausentes deben ser los matriculados.",
        "Los registros con nombres de niños son confidenciales: se guardan en el lugar indicado por el jardín y no se muestran a otras personas ni se publican." + LIM,
    ],
    vocab=[("hecho observable", "algo que ocurrió y que otra persona también podría ver"), ("interpretación", "opinión o explicación personal que no se puede comprobar"), ("incidente", "situación inesperada durante la experiencia"), ("sugerencia", "propuesta de mejora que se entrega a la educadora"), ("matriculados", "niños y niñas inscritos en el grupo, estén o no presentes hoy")],
    worked=[
        ("Hecho o interpretación", "¿Qué frase es un hecho: «Tomás empujó a Noa dos veces» o «Tomás es agresivo»?", ["Un hecho se puede ver y contar.", "«Es agresivo» es una opinión sobre cómo es él."], "«Tomás empujó a Noa dos veces»"),
        ("Revisar que los números cuadren", "Un registro dice: 15 matriculados, 12 presentes y 4 ausentes. ¿Cuadra?", ["Presentes más ausentes deben dar los matriculados.", "12 + 4 = 16, no 15."], "No cuadra: hay que revisar los datos"),
    ],
    mistakes=[("Escribir en el registro «Bruno es muy tímido».", "Es una etiqueta que no se puede comprobar y puede marcarlo.", "Escribe el hecho: «Bruno retiró la mano y miró a la técnica»."),
              ("Dejar el aviso de un incidente para el final de la semana.", "Lo urgente debe saberse enseguida para actuar a tiempo.", "Avisa de inmediato y de palabra, y luego déjalo por escrito.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es un hecho observable?", "Algo que ocurrió y que otra persona también podría ver", "Una opinión sobre cómo es un niño", "Una explicación de por qué ocurrió", "Un hecho observable se puede ver y contar; las opiniones y explicaciones no."),
        ("abc", "{F} ¿Cuál de estas frases del registro es un hecho?", "Bruno retiró la mano y miró a la técnica", "Bruno es inseguro", "Bruno no quiso participar", "Retirar la mano y mirar se puede ver; las otras frases interpretan."),
        ("abc", "{F} ¿Qué incidente se registró?", "Se derramó una bandeja con agua y nadie se golpeó", "Un niño se cayó y debió ir al hospital", "Un niño se perdió en el patio", "La ficha registra un derrame de agua sin lesiones."),
        ("=", "{F} ¿Cuántos niños matriculados no estaban presentes?", "16-14", "A los matriculados se les restan los presentes.", " niños"),
        ("=", "{F} Según el registro, ¿cuántos de los niños presentes no tocaron las tres telas?", "14-12", "A los presentes se les restan los que tocaron las tres telas.", " niños"),
        ("abc", "{F} Un compañero propone escribir «Sofía es muy inteligente porque dijo áspero». ¿Qué observación corresponde?", "Es mejor escribir el hecho: «Sofía dijo áspero al tocar la tela rugosa»", "Está bien, porque es una opinión positiva", "Está bien si lo dice la educadora", "Las opiniones, aunque sean positivas, no son hechos y sirven poco para evaluar."),
        ("abc", "{F} ¿Cómo comunica la técnica el derrame de agua?", "De inmediato y de palabra a la educadora, y después por escrito", "Solo en el informe del fin de mes", "Solo si algún niño se golpeó", "Un incidente se avisa enseguida, aunque no haya lesiones."),
        ("=", "{F} Una tabla de registro dice: presentes 14, ausentes 2. ¿Cuántos matriculados hay según esa tabla?", "14+2", "Los matriculados son la suma de presentes y ausentes.", " niños"),
        ("abc", "{F} ¿Qué sugerencia está escrita de forma útil para la educadora?", "Dar más tiempo para la última tela, porque 2 niños solo tocaron la lisa", "Cambiar a los 2 niños de grupo", "Evitar telas, porque no sirven", "Una sugerencia útil se apoya en un hecho y propone una mejora concreta."),
        ("abc", "{F} Otra técnica quiere subir el registro con los nombres de los niños a una red social «para mostrar el trabajo». ¿Qué corresponde responder?", "No, porque el registro es confidencial y se guarda donde indica el jardín", "Sí, si borra los apellidos", "Sí, si las familias no se enteran", "Los registros con nombres no se publican; son confidenciales."),
        ("abc", "{F} La técnica anota «el grupo B es más inteligente que el grupo A». ¿Qué falla?", "Compara grupos con un juicio que no se puede comprobar", "Nada, es una conclusión útil", "Debería haberlo escrito con mayúsculas", "Comparar y juzgar a niños no es parte del registro; solo se describen hechos."),
        ("=", "{F} Si el próximo día asisten los 16 matriculados y cada uno recibe 3 recortes de tela, ¿cuántos recortes se preparan en total?", "16*3", "Se multiplican los niños por los recortes de cada uno.", " recortes"),
        ("abc", "{F} Al terminar, Bruno se acerca y dice «no me gustó la tela rugosa». ¿Qué hace la técnica?", "Lo escucha, lo anota como lo dijo y no lo obliga a repetirla", "Le dice que debería gustarle y lo anima a insistir", "Anota que Bruno es un niño difícil", "Se respeta su opinión y se registra tal como la dijo."),
    ],
    ctx=("abc", "{F} Una madre pregunta a la técnica a la salida si su hijo «tuvo problemas hoy» y quiere detalles del registro. ¿Qué responde la técnica?", "Que la educadora podrá conversar con ella sobre su hijo y que el registro se maneja con reserva", "Le muestra el registro con los nombres de todos los niños", "Le dice lo que piensa que le pasa a su hijo", "El diálogo con las familias sobre un niño lo conduce la educadora; el registro con otros nombres es confidencial."),
    sc=[
        ("En Atención de Párvulos: ¿cuándo se avisa de un incidente?", "De inmediato, a la educadora", "Lo urgente no puede esperar, porque hay que actuar a tiempo."),
        ("¿Qué escribes en un registro: hechos o interpretaciones?", "Hechos", "Los hechos se pueden comprobar; las interpretaciones pueden marcar al niño."),
        ("Si en el registro presentes más ausentes no dan los matriculados, ¿qué haces?", "Reviso los datos antes de entregarlo", "Un registro con números que no cuadran no es confiable."),
    ],
    op=("Datos de ejemplo de una experiencia: nivel de transición, 18 matriculados y 16 presentes. Objetivo: armar torres de bloques grandes de tres pisos. Hechos: 13 niños armaron una torre; 2 la armaron con ayuda; 1 niño, Amaru, prefirió ordenar los bloques por tamaño. Incidente: una torre cayó, sin lesionados. "
        "Escribe un registro con: fecha ficticia, grupo, objetivo, tres hechos, el incidente y una sugerencia; y dos frases que dirías de palabra a la educadora.",
        "Fecha: lunes (ficticio). Grupo: transición, 16 de 18 presentes. Objetivo: armar torres de tres pisos. Hechos: 13 armaron una torre; 2 la armaron con ayuda; Amaru ordenó los bloques por tamaño. Incidente: una torre cayó, sin lesionados. Sugerencia: preparar bloques más livianos para quienes necesitan ayuda. De palabra: «Una torre cayó, sin lesionados» y «Dos niños necesitaron ayuda; ¿cómo prefieres que los apoye?».",
        ["incluye los seis elementos del registro", "los números cuadran y los hechos no interpretan", "avisa lo urgente de palabra"],
        ["hoja con el registro completo y dos frases de aviso"],
        ["escribir una etiqueta sobre un niño", "dejar números que no cuadran", "olvidar el incidente"],
        "Pregunta: «¿qué cambiarías si Amaru te contara por qué prefirió ordenar?». Debe anotar lo que dice textualmente y no su interpretación."),
    reinforce="Reescribe tres frases con etiquetas («es flojo», «es tímida», «es agresivo») como hechos observables.",
    extend="Explica con un ejemplo por qué un registro con hechos ayuda más a la educadora que una opinión.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (criterios para el material, de ejemplo). Pedagógico: sirve al objetivo y a la edad del grupo. Estético: está ordenado y limpio, sin exceso de adornos. Equidad: muestra niñas y niños en distintas actividades, familias de distintos tipos y diversidad cultural y de capacidades, sin estereotipos. "
     "Seguridad: sin bordes cortantes, sin piezas pequeñas que puedan tragarse en los niveles más pequeños y fácil de lavar, según la norma vigente.")
build(
    O2, 1, F,
    use="Aprenderé qué es el material didáctico y la ambientación, y los cuatro criterios para elegirlos: pedagógico, estético, de equidad y de seguridad.",
    prior=["Conozco la planificación de la educadora.", "Sé que cada nivel tiene necesidades distintas.", "Sé leer una ficha."],
    explain=[
        "En Atención de Párvulos, el material didáctico son los objetos que ayudan a que los niños aprendan jugando, como bloques, libros o telas. La ambientación es la forma en que se organiza y decora la sala: paneles, rincones, carteles y orden. Ambos se preparan con la educadora, que decide su uso según el objetivo y la edad del grupo.",
        "Para elegirlos se usan cuatro criterios. El criterio pedagógico pregunta si sirve al objetivo y a la edad. El estético pide orden, limpieza y pocos adornos. El de equidad busca que niños y niñas, familias y culturas distintas estén representados sin estereotipos de género, etnia o cultura, como decir que ciertos juguetes son «de niñas» o «de niños». El de seguridad revisa bordes, piezas pequeñas y facilidad de lavado.",
        "Cuando el material representa a un pueblo originario, se hace con respeto y con apoyo de la educadora o de personas de esa comunidad, sin caricaturas ni disfraces. Preparar material en papel es una forma segura de practicar estas decisiones." + LIM,
    ],
    vocab=[("material didáctico", "objeto que ayuda a que niños y niñas aprendan jugando"), ("ambientación", "orden y decoración de la sala para el aprendizaje"), ("criterio pedagógico", "el material sirve al objetivo y a la edad"), ("criterio estético", "orden, limpieza y pocos adornos"), ("equidad", "trato justo que reconoce diferencias y no usa estereotipos"), ("estereotipo", "idea fija y simplificada sobre un grupo de personas")],
    worked=[
        ("Aplicar el criterio de seguridad", "Un juego de ejemplo para sala cuna tiene botones pequeños pegados con cola. ¿Qué criterio revisa la técnica y qué concluye?", ["Revisa seguridad: un botón desprendido podría tragarse.", "En sala cuna no corresponde usar piezas pequeñas."], "Seguridad: no es adecuado para sala cuna"),
        ("Aplicar el criterio de equidad", "Un afiche de ejemplo muestra a niñas solo cocinando y a niños solo construyendo. ¿Qué criterio se incumple?", ["Muestra actividades reservadas a un género.", "Eso es un estereotipo."], "El de equidad"),
    ],
    mistakes=[("Decorar el panel con muchos adornos «para que se vea lindo».", "El exceso de adornos distrae y desordena; el criterio estético pide pocos y claros.", "Elige pocos elementos ordenados y que sirvan al objetivo."),
              ("Usar un afiche con una caricatura de plumas para representar a todos los pueblos originarios.", "Es una caricatura que simplifica y no respeta la diversidad cultural.", "Pide a la educadora material respetuoso, revisado por personas de esa comunidad.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es la ambientación de una sala?", "La forma de organizar y decorar la sala para el aprendizaje", "El horario de las experiencias del día", "La lista de niños que asisten", "La ambientación es el orden y la decoración del espacio, no el horario ni la lista."),
        ("abc", "{F} ¿Qué pide el criterio pedagógico?", "Que el material sirva al objetivo y a la edad del grupo", "Que el material sea muy caro", "Que el material tenga muchos colores", "Según la ficha, lo pedagógico es servir al objetivo y a la edad."),
        ("abc", "{F} ¿Qué pide el criterio de seguridad?", "Sin bordes cortantes ni piezas pequeñas que puedan tragarse, y fácil de lavar", "Que los niños no puedan tocarlo", "Que el adulto lo guarde bajo llave siempre", "La ficha define seguridad como bordes, piezas pequeñas y facilidad de lavado."),
        ("abc", "{F} Un panel de la sala tiene 30 adornos de distintos tamaños colgando del techo. ¿Qué criterio no cumple?", "El estético", "El de equidad", "El pedagógico", "El exceso de adornos desordena el espacio, que es lo que revisa el criterio estético."),
        ("abc", "{F} Un cuento de ejemplo dice que «las niñas son delicadas y los niños fuertes». ¿Qué criterio incumple?", "El de equidad", "El de seguridad", "El estético", "Asignar rasgos por género es un estereotipo, que el criterio de equidad evita."),
        ("abc", "{F} Una técnica quiere usar bolitas pequeñas de vidrio en la sala cuna. ¿Qué corresponde?", "No usarlas y consultar a la educadora por un material seguro", "Usarlas con mucho cuidado", "Usarlas solo con los niños más grandes de la sala cuna", "Las piezas pequeñas se pueden tragar y el vidrio puede cortar; se reemplazan."),
        ("abc", "{F} Se prepara una sala para un grupo de 3 años con un rincón de disfraces. ¿Qué elección cumple mejor el criterio de equidad?", "Ofrecer disfraces variados que cualquier niño o niña pueda elegir", "Poner los vestidos para niñas y los cascos para niños", "Retirar los disfraces para evitar discusiones", "Ofrecer opciones sin asignarlas por género respeta la equidad."),
        ("=", "{F} Un panel de ejemplo muestra 12 imágenes: 4 de familias con mamá y papá, 3 de familias con abuelos, 3 de familias con un solo adulto y el resto de otros tipos de familia. ¿Cuántas imágenes son de otros tipos?", "12-4-3-3", "Al total se le restan los tipos ya contados.", " imágenes"),
        ("abc", "{F} Un afiche representa a un pueblo originario con una caricatura de plumas. ¿Qué hace la técnica?", "Lo aparta y consulta a la educadora por material respetuoso", "Lo cuelga, porque es un afiche de colores", "Lo cuelga y añade un disfraz para los niños", "Una caricatura simplifica y no respeta la diversidad cultural; se consulta a quien planifica."),
        ("abc", "{F} Un libro de ejemplo para nivel de transición tiene solo páginas de texto con letras muy pequeñas y ninguna imagen, y el objetivo es que niños que aún no leen disfruten un cuento. ¿Qué criterio falla?", "El pedagógico, porque el libro no se ajusta a la edad ni al objetivo", "El de seguridad", "El estético, porque tiene colores", "Un libro solo de texto pequeño no sirve a niños que aún no leen y entienden con imágenes."),
        ("abc", "{F} La técnica ve que un puzle de ejemplo pasa por varias manos sin lavarse y tiene piezas pegajosas. ¿Qué criterio revisa primero?", "El de seguridad, por la facilidad de lavado y la higiene", "El estético, porque se ve sucio", "El pedagógico, porque tiene piezas", "Higiene y facilidad de lavado son parte del criterio de seguridad de la ficha."),
        ("=", "{F} Se revisan 20 materiales: 14 cumplen todos los criterios y 4 solo uno. ¿Cuántos tienen otro resultado?", "20-14-4", "Se restan los materiales ya clasificados al total revisado.", " materiales"),
        ("abc", "{F} La educadora pide un panel que muestre a las familias del grupo, pero algunas no quieren que aparezcan sus fotos. ¿Qué hace la técnica?", "Usa dibujos hechos por los niños y respeta que no haya fotos", "Cuelga las fotos de todos para que no haya diferencias", "Pide a esas familias que cambien de opinión", "Se respeta la decisión de las familias y se usan dibujos."),
    ],
    ctx=("abc", "{F} Una técnica prepara el rincón de lectura. Hay un cuento donde solo los niños son valientes y las niñas necesitan ayuda, y otro donde distintos personajes ayudan a resolver un problema. ¿Qué elección corresponde?", "Dejar el segundo y consultar a la educadora por el primero", "Dejar el primero porque es más antiguo", "Dejar los dos sin comentar nada", "El segundo cumple equidad; el primero refuerza un estereotipo y se consulta."),
    sc=[
        ("En Atención de Párvulos: ¿qué es el material didáctico?", "Un objeto que ayuda a aprender jugando", "Los materiales apoyan el objetivo de la experiencia."),
        ("¿Qué haces con un material que tiene piezas que se pueden tragar para sala cuna?", "No lo uso y consulto a la educadora", "El riesgo de atragantamiento se evita con la selección del material."),
        ("¿Cómo se representa respetuosamente a un pueblo originario?", "Con apoyo de la educadora o de personas de esa comunidad, sin caricaturas", "Evita la simplificación y respeta la diversidad cultural."),
    ],
    op=("Material de ejemplo para el rincón de juego de un nivel medio (14 niños y niñas): una caja de bloques de madera lisos; un cartel con la frase «juguetes para niñas» sobre las muñecas y «juguetes para niños» sobre los autos; un libro con familias distintas; una bolsa con botones pequeños; una colección de 30 recortes pegados en el panel. "
        "Escribe: qué materiales conservarías y por qué; cuáles retirarías o cambiarías y qué criterio incumplen; y cómo ordenarías el panel.",
        "Conservaría los bloques lisos (seguros y pedagógicos) y el libro de familias distintas (equidad). Retiraría el cartel por estereotipo de género (equidad); los botones pequeños por seguridad (se pueden tragar); y bajaría los 30 recortes del panel a pocos y ordenados (estético). Ordenaría el panel con pocos elementos claros y al alcance de la vista de los niños.",
        ["conserva y retira con criterios correctos", "nombra el criterio que cada elemento incumple", "propone un panel ordenado"],
        ["hoja con lista de materiales conservados, retirados y criterios"],
        ["conservar los botones pequeños", "no ver el estereotipo del cartel", "no dar la razón de cada decisión"],
        "Pregunta: «¿Qué harías si la educadora quiere conservar el cartel?». Debe explicar el estereotipo y respetar su decisión pidiendo conversarla."),
    reinforce="Escribe un ejemplo de material que cumpla los cuatro criterios y uno que incumpla alguno, con su razón.",
    extend="Explica con un ejemplo inventado por qué un estereotipo en un cuento infantil puede afectar a niñas y niños.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (inventario de ejemplo del nivel de transición). Bloques de madera lisos: 40 en buen estado y 3 con astillas. Rompecabezas de 12 piezas: 5 completos y 2 incompletos. Libros de cuentos: 18, de los cuales 2 tienen hojas sueltas. Pelotas blandas: 10. "
     "Cada caja lleva rótulo con el nombre del material y un dibujo, a la altura de los niños. Material de uso exclusivo de la educadora (tijeras de adulto, pegamento): se guarda en un mueble alto, fuera del alcance de los niños.")
build(
    O2, 2, F,
    use="Aprenderé qué es un inventario y un rótulo, cómo se guarda el material por categorías y cuándo un material se aparta para revisión.",
    prior=["Conozco los cuatro criterios para elegir material.", "Sé sumar y restar.", "Sé leer una tabla en texto."],
    explain=[
        "Almacenar el material es guardarlo de modo que se conserve, se encuentre fácil y sea seguro. Un inventario es la lista que dice qué material hay, cuántos hay y en qué estado. Se actualiza cuando se compra, se presta o se aparta algo. El rótulo es la etiqueta de cada caja, con el nombre y un dibujo, para que también los niños puedan ordenar solos.",
        "El material de uso diario se guarda a la altura de los niños, en cajas rotuladas por categorías, como bloques, libros o juegos de encaje. Los materiales de uso exclusivo del adulto, como tijeras de adulto o pegamentos, se guardan fuera de su alcance. El material roto, con astillas, con hojas sueltas o incompleto se aparta y se avisa a la educadora, que decide si se repara o se da de baja.",
        "Antes de guardar, el material se limpia según el protocolo de higiene del establecimiento. Un inventario al día evita comprar de más y permite saber qué reponer." + LIM,
    ],
    vocab=[("inventario", "lista de qué material hay, cuántos y en qué estado"), ("rótulo", "etiqueta de una caja con el nombre y un dibujo del material"), ("categoría", "grupo de materiales parecidos, como bloques o libros"), ("dar de baja", "retirar un material del uso porque ya no sirve, por decisión de la educadora"), ("reposición", "compra o reemplazo de material que falta o se apartó"), ("estado", "si el material está en buen estado, roto o incompleto")],
    worked=[
        ("Total de bloques", "Un inventario de ejemplo dice: 25 bloques en buen estado y 4 con astillas. ¿Cuántos bloques hay en total?", ["Se suman los dos estados.", "25 + 4 = 29."], "29 bloques"),
        ("Qué hacer con material roto", "Se encuentra un libro de ejemplo con hojas sueltas. ¿Qué hace la técnica?", ["No lo deja en el estante con los demás.", "Lo aparta y avisa a la educadora, que decide si se repara o se da de baja."], "Apartarlo y avisar a la educadora"),
    ],
    mistakes=[("Guardar las tijeras de adulto en una caja baja del estante de los niños.", "Las tijeras con filo son un riesgo si los niños llegan a ellas.", "Guárdalas en un mueble alto, fuera de su alcance."),
              ("Dejar el material con astillas en la caja de bloques «porque es solo uno».", "Un bloque astillado puede dañar a un niño; el inventario también quedaría equivocado.", "Apártalo, avísalo a la educadora y actualiza el inventario.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es un inventario?", "La lista de qué material hay, cuántos y en qué estado", "El horario de uso de la sala", "El dibujo que va en cada caja", "El inventario cuenta y describe el material; el dibujo es el rótulo."),
        ("abc", "{F} ¿Para qué sirve el rótulo con dibujo en cada caja?", "Para que los niños también puedan ordenar solos", "Para decorar la sala", "Para que solo la educadora sepa qué hay", "El dibujo permite que los niños que aún no leen reconozcan el material."),
        ("abc", "{F} ¿Dónde se guardan las tijeras de adulto y el pegamento?", "En un mueble alto, fuera del alcance de los niños", "En una caja rotulada a la altura de los niños", "En la mochila de cada niño", "Son material exclusivo del adulto y se guardan fuera del alcance."),
        ("=", "{F} ¿Cuántos bloques de madera hay en total, entre buenos y con astillas?", "40+3", "Se suman los bloques en buen estado y los que tienen astillas.", " bloques"),
        ("abc", "{F} ¿Qué se hace con los 3 bloques con astillas?", "Se apartan y se avisa a la educadora", "Se dejan en la caja si los niños no se quejan", "Se regalan a otra sala sin avisar", "Un bloque con astillas es un riesgo y se aparta; la decisión es de la educadora."),
        ("abc", "{F} ¿Cuántos rompecabezas completos hay para usar con los niños?", "5", "7", "2", "Solo 5 están completos; 2 están incompletos y se apartan, y 7 es el total."),
        ("=", "{F} ¿Cuántos libros de cuentos están en buen estado?", "18-2", "Al total de libros se le restan los que tienen hojas sueltas.", " libros"),
        ("=", "{F} El grupo tiene 16 niños y se quiere que cada uno tenga 3 bloques buenos. ¿Cuántos bloques buenos faltan?", "16*3-40", "Se calculan los bloques necesarios y se restan los bloques buenos que hay.", " bloques"),
        ("abc", "{F} ¿Cómo se ordena mejor el material de uso diario?", "En cajas rotuladas por categorías, a la altura de los niños", "Todo mezclado en una sola caja grande", "En un estante alto, para que dure más", "Las categorías y el rótulo facilitan encontrar y ordenar, y la altura permite la autonomía."),
        ("abc", "{F} Una técnica guarda el material sin limpiarlo porque «los niños se lavan las manos». ¿Qué falla?", "No se limpia el material según el protocolo de higiene del establecimiento", "Nada: con que los niños se laven las manos basta", "Debe guardarlo en un lugar húmedo", "El material compartido se limpia antes de guardarse, según el protocolo."),
        ("abc", "{F} El inventario dice 10 pelotas blandas, pero en la caja hay 8. ¿Qué hace la técnica?", "Busca las 2 faltantes, corrige el inventario con la educadora y anota la diferencia", "Anota 10 igual, para no alarmar", "Anota 8 sin avisar a nadie", "El inventario debe reflejar la realidad y las diferencias se comunican."),
        ("=", "{F} Se aparta todo el material en mal estado: 3 bloques, 2 rompecabezas incompletos y 2 libros con hojas sueltas. ¿Cuántos elementos o juegos se apartan?", "3+2+2", "Se suman las piezas apartadas de las tres categorías.", " elementos"),
        ("abc", "{F} Una compañera propone dar de baja los 2 rompecabezas incompletos hoy mismo, sin consultar. ¿Qué observación corresponde?", "Primero se aparta y se avisa; la educadora decide si se repara o se da de baja", "Está bien, porque son solo 2", "Está bien si se tiran por la noche", "Dar de baja es una decisión de la educadora, no de la técnica."),
    ],
    ctx=("abc", "{F} Un niño de ejemplo toma una tijera de adulto que quedó sobre una mesa y camina con ella. ¿Qué hace la técnica?", "Se acerca con calma, le pide que se la entregue, la guarda en el mueble alto y avisa a la educadora", "Corre y le grita para que la suelte", "Espera a ver si la deja sola", "Se retira el riesgo con calma y se informa; además se corrige el almacenamiento."),
    sc=[
        ("En Atención de Párvulos: ¿qué lleva el rótulo de una caja?", "El nombre del material y un dibujo", "Así lo reconocen los adultos y los niños que aún no leen."),
        ("¿Dónde se guarda el material de uso exclusivo del adulto?", "Fuera del alcance de los niños", "Es un material que puede ser riesgoso."),
        ("¿Qué haces con un material roto?", "Lo aparto y aviso a la educadora", "La educadora decide si se repara o se da de baja."),
    ],
    op=("Inventario de ejemplo de un nivel medio (12 niños): 30 bloques de goma espuma (28 buenos, 2 rotos); 15 libros (14 buenos, 1 con hojas sueltas); 10 vasitos plásticos (8 limpios, 2 con una grieta); 1 pegamento líquido de adulto. "
        "Escribe: el estado de cada categoría y cuántos elementos se apartan; cómo guardarías cada categoría (rótulo y altura); dónde irá el pegamento; y qué avisarías a la educadora.",
        "Se apartan 2 bloques, 1 libro y 2 vasitos: 5 elementos. Bloques, libros y vasitos en cajas rotuladas con dibujo, a la altura de los niños, por categorías. El pegamento va en un mueble alto, fuera del alcance. Aviso: «Aparté 2 bloques rotos, 1 libro con hojas sueltas y 2 vasitos agrietados; ¿los repararemos o los damos de baja?».",
        ["suma correctamente los elementos apartados", "propone rótulos y alturas adecuados", "avisa a la educadora sin decidir por ella"],
        ["hoja con cuentas, almacenamiento y aviso"],
        ["dejar el pegamento al alcance de los niños", "no apartar el material roto", "dar de baja sin consultar"],
        "Pregunta: «¿Qué cambiaría si no hubiera cajas rotuladas?». Debe decir que el material se encuentra peor y los niños no ordenan solos."),
    reinforce="Escribe un inventario de ejemplo de 5 materiales con cantidad y estado.",
    extend="Explica por qué un inventario al día ayuda a no comprar material de más y a mantener la seguridad.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (rincón de lectura, de ejemplo). Nivel de transición, 15 niños y niñas. Libros propuestos: L1, cuento sobre familias de distintos tipos (con abuelos, con un solo adulto, con hermanos mayores). L2, libro de animales de hojas gruesas y limpio. "
     "L3, libro con una hoja suelta y una grapa en el borde. L4, cuento donde solo los niños son valientes y las niñas cuidan a los demás. L5, leyenda de un pueblo originario escrita y revisada por personas de esa comunidad, entregada por la educadora. L6, seis cojines con funda lavable. El estante bajo tiene espacio para 12 libros.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso: elegir entre materiales con los cuatro criterios, cuidar la equidad en las imágenes y los cuentos, y comunicar la selección a la educadora.",
    prior=["Conozco los criterios pedagógico, estético, de equidad y de seguridad.", "Sé clasificar material por categorías.", "Sé dividir para formar turnos."],
    explain=[
        "Para analizar un caso de selección se mira cada material con los cuatro criterios y se registra qué se conserva, qué se aparta y por qué. Un buen rincón de lectura reúne libros que sirvan al objetivo, estén en buen estado, muestren a niños y niñas en distintos papeles y reflejen familias y culturas distintas. No se elige por tamaño o por precio, sino por criterios.",
        "La equidad se revisa en los textos y en las imágenes: quién aparece, qué hace y quién queda fuera. Si un cuento asigna a las niñas solo el cuidado y a los niños solo la valentía, refuerza un estereotipo. Si habla de un pueblo originario, se usa un texto escrito o revisado por personas de esa comunidad, que la educadora conoce, para no inventar ni simplificar.",
        "El espacio también cuenta: si hay menos cojines o asientos que niños, se organizan turnos para que todos puedan usar el rincón. La selección se entrega a la educadora por escrito, con sus razones." + LIM,
    ],
    vocab=[("selección", "elección de los materiales que se usarán y de los que se apartan"), ("turno", "momento asignado a un grupo para usar un espacio o material"), ("representación", "forma en que personas, familias y culturas aparecen en un libro o imagen"), ("revisado por la comunidad", "texto verificado por personas del pueblo del que habla"), ("objetivo de uso", "para qué se usará el material en la experiencia")],
    worked=[
        ("Elegir con equidad", "Entre un cuento de ejemplo donde solo los niños arreglan cosas y otro donde distintos personajes lo hacen, ¿cuál conviene?", ["El primero asigna una tarea según el género.", "El segundo muestra personajes diversos en el mismo papel."], "El segundo, porque respeta la equidad"),
        ("Formar turnos", "Un rincón de ejemplo tiene 4 asientos y deben pasar 10 niños. ¿Cuántos turnos se necesitan?", ["Se divide: 10 ÷ 4 = 2 y sobran 2 niños.", "Esos 2 niños necesitan un tercer turno."], "3 turnos"),
    ],
    mistakes=[("Quitar el libro de familias distintas porque «algunos niños no se parecen a esas familias».", "La diversidad de familias busca que todos se reconozcan; quitarla deja fuera a algunos niños.", "Conserva el libro y deja otros que muestren más tipos de familia."),
              ("Dejar en el estante el libro con una grapa en el borde «porque se puede cuidar».", "Una grapa puede lastimar y no se puede controlar siempre lo que hace cada niño.", "Aparta el libro y avisa a la educadora.")],
    T=[
        ("abc", "{F} ¿Cuál de estos libros cumple mejor el criterio de equidad respecto de las familias?", "L1, el de familias de distintos tipos", "L2, el de animales", "L6, los cojines", "L1 muestra distintos tipos de familia; los otros no tratan ese tema."),
        ("abc", "{F} ¿Qué se hace con L3?", "Se aparta y se avisa a la educadora", "Se deja en el estante si se arregla la hoja con cinta", "Se entrega a los niños que lo cuiden más", "La grapa puede lastimar y el libro tiene una hoja suelta; se aparta."),
        ("abc", "{F} ¿Por qué L4 no cumple el criterio de equidad?", "Porque asigna la valentía a los niños y el cuidado a las niñas", "Porque tiene demasiadas imágenes", "Porque es muy corto", "Asignar rasgos o tareas según el género es un estereotipo."),
        ("abc", "{F} ¿Cuántos niños pueden usar a la vez un cojín propio en el rincón?", "6", "15", "12", "La ficha dice que hay seis cojines; 15 son los niños y 12 el espacio para libros."),
        ("abc", "{F} ¿Por qué L5 es adecuado para hablar de un pueblo originario?", "Porque fue escrita y revisada por personas de esa comunidad", "Porque es una leyenda muy conocida en internet", "Porque tiene colores llamativos", "Un texto revisado por la comunidad evita inventar o simplificar su cultura."),
        ("=", "{F} Se aceptan L1, L2 y L5, con 3 ejemplares de cada título. ¿Cuántos espacios del estante quedan libres?", "12-3*3", "Se restan los libros guardados a los 12 espacios del estante.", " espacios"),
        ("=", "{F} Para que los 15 niños pasen por el rincón en turnos de 6, ¿cuántos turnos se necesitan?", "(15+5)//6", "Se divide en grupos de 6 y se redondea hacia arriba porque los niños que sobran necesitan turno.", " turnos"),
        ("abc", "{F} El objetivo de la experiencia es que los niños reconozcan distintos tipos de familia. ¿Qué libro conviene usar?", "L1", "L2", "L3", "L1 trata justo ese tema; L2 es de animales y L3 está en mal estado."),
        ("abc", "{F} ¿Qué criterio se cumple gracias a la funda lavable de L6?", "Seguridad, por la facilidad de lavado", "Equidad", "Estético, porque la funda es de colores", "Fácil de lavar es una condición de seguridad de la ficha de criterios."),
        ("abc", "{F} Una compañera propone reemplazar L1 por un cuento sobre «la familia tradicional» porque «así todos se identifican». ¿Qué observación corresponde?", "Los niños viven en familias distintas y L1 permite que cada uno se reconozca", "Es mejor, porque así hay un solo modelo de familia", "Es mejor, porque es más fácil de explicar", "La diversidad de familias refleja a todo el grupo, no solo a algunos."),
        ("abc", "{F} Un niño dice: «Ese libro de cuidar bebés es de niñas». ¿Qué responde la técnica?", "Que los libros son para todos y le propone mirarlo juntos", "Que tiene razón y lo guarda", "Que se calle y lea otro libro", "Responder con naturalidad desarma el estereotipo y respeta al niño."),
        ("=", "{F} Si cada libro se comparte entre 2 niños, ¿cuántos libros distintos se necesitan para que los 15 niños tengan uno?", "(15+1)//2", "Se divide en parejas y la pareja incompleta también necesita libro.", " libros"),
        ("abc", "{F} ¿Cómo entrega la técnica su selección a la educadora?", "Por escrito, con la lista de libros elegidos, los apartados y la razón de cada decisión", "Dejando los libros en el estante sin avisar", "Pidiendo que los niños voten qué libros se quedan", "La selección se informa con razones; la educadora decide."),
    ],
    ctx=("abc", "{F} Una familia pide que se retire L1 porque «sus hijos no necesitan ver otros tipos de familia». ¿Qué hace la técnica?", "Escucha con respeto y deriva la conversación a la educadora, que explica el proyecto del jardín", "Retira el libro de inmediato para evitar problemas", "Le dice a la familia que está equivocada y que no puede opinar", "Las conversaciones con familias las conduce la educadora; la técnica escucha y deriva."),
    sc=[
        ("En Atención de Párvulos: ¿qué se mira en un cuento para revisar la equidad?", "Quién aparece, qué hace y quién queda fuera", "Así se detectan los estereotipos antes de usar el cuento."),
        ("¿Qué haces con un libro que tiene una grapa en el borde?", "Lo aparto y aviso a la educadora", "Una grapa puede lastimar; el libro se retira del uso."),
        ("Si hay menos asientos que niños, ¿cómo se organiza el rincón?", "Con turnos", "Los turnos permiten que todos puedan usarlo."),
    ],
    op=("Libros propuestos de ejemplo para un nivel medio (12 niños y niñas): A, cuento sobre una niña astronauta y un niño que cocina; B, libro con una página rasgada y una cinta metálica suelta; C, cuento de una familia con una abuela y dos hermanos; D, libro de oficios donde solo hombres son bomberos y solo mujeres son enfermeras. "
        "Escribe: cuáles elegirías y cuáles apartarías, con el criterio de cada uno; cómo organizarías un estante que guarde 3 ejemplares de cada libro elegido; y qué dirías a la educadora.",
        "Elegiría A y C (equidad y diversidad de familias). Apartaría B por seguridad (cinta metálica suelta y página rasgada) y D por estereotipo de género en los oficios. Con A y C, 3 ejemplares de cada uno son 6 libros. Mensaje: «Dejé A y C; aparté B porque tiene una cinta suelta y D porque muestra oficios por género; ¿qué opinas?».",
        ["elige y aparta con criterios correctos", "calcula los libros guardados", "informa por escrito sin decidir por la educadora"],
        ["hoja con selección, cuenta de libros y mensaje a la educadora"],
        ["elegir el libro con estereotipos", "no revisar la seguridad", "no dar razones"],
        "Pregunta: «¿Qué cambiarías si la educadora quiere conservar D?». Debe respetar su decisión y proponer conversar el estereotipo con los niños."),
    reinforce="Revisa con los cuatro criterios tres libros de ejemplo que inventes y decide cuáles dejar.",
    extend="Explica por qué un cuento puede mostrar a niños y niñas en distintos papeles sin perder la historia.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (preparación de material, de ejemplo). Experiencia: pintar con esponjas, nivel medio, 18 niños y niñas. Cada niño usa 1 esponja lavable y 2 hojas; se preparan 2 esponjas de repuesto y 4 hojas de repuesto. "
     "Las esponjas se compran en paquetes de 6, a $2.400 el paquete (precio de ejemplo). La pintura lavable va en bandejas: 3 niños por bandeja. Caja para guardar esponjas, con espacio para 25. Presupuesto de ejemplo: $10.000.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos para preparar, usar y guardar el material de una experiencia: calcular cantidades, costo y almacenamiento.",
    prior=["Conozco inventario, rótulo y categorías.", "Sé multiplicar y dividir.", "Sé calcular un costo con precios de ejemplo."],
    explain=[
        "Preparar material es calcular qué se necesita antes de la experiencia: cuánto por niño, cuánto de repuesto y cuántas bandejas o mesas. Se multiplica lo que usa cada niño por el número de niños y se suma el repuesto. Si el material se compra en paquetes, se divide la cantidad necesaria entre el contenido del paquete y se redondea hacia arriba, porque no se puede comprar medio paquete.",
        "El costo se calcula multiplicando el número de paquetes por su precio y se compara con el presupuesto. Después de la experiencia, el material se lava y se seca antes de guardarlo, se cuenta, se rotula la caja y se anota en el inventario cuánto queda. Un material húmedo o sucio no se guarda.",
        "La ambientación también se prepara con criterio: los trabajos de los niños se exponen a su altura, mostrando el trabajo de cada uno y no solo el de «los mejores», para que todos se sientan parte del grupo." + LIM,
    ],
    vocab=[("repuesto", "material extra para reemplazar lo que se estropee o falte"), ("paquete", "conjunto de unidades que se compran juntas"), ("redondear hacia arriba", "tomar el número entero mayor cuando sobran unidades que igual se necesitan"), ("presupuesto", "dinero disponible para comprar el material"), ("exponer", "mostrar los trabajos de los niños en un lugar visible")],
    worked=[
        ("Cantidad necesaria", "En otra experiencia de ejemplo, 14 niños usan 2 pinceles gruesos cada uno y se agregan 3 de repuesto. ¿Cuántos pinceles se preparan?", ["Se multiplica por niño: 14 × 2 = 28.", "Se suman los repuestos: 28 + 3 = 31."], "31 pinceles"),
        ("Paquetes necesarios", "Se necesitan 20 unidades y el paquete trae 8. ¿Cuántos paquetes hay que comprar?", ["20 ÷ 8 = 2 y sobran 4.", "Esas 4 unidades necesitan un tercer paquete."], "3 paquetes"),
    ],
    mistakes=[("Comprar 3 paquetes de 6 esponjas porque «18 ÷ 6 = 3», sin sumar los repuestos.", "Si una esponja se estropea o falta, algún niño quedará sin ella.", "Suma primero el repuesto y luego calcula los paquetes."),
              ("Guardar las esponjas aún mojadas en la caja cerrada.", "El material húmedo se llena de hongos y no es higiénico.", "Lávalas, séalas bien y guárdalas secas.")],
    T=[
        ("=", "{F} ¿Cuántas esponjas se preparan en total, contando las de repuesto?", "18+2", "Se suma el repuesto a una esponja por cada niño.", " esponjas"),
        ("=", "{F} ¿Cuántas bandejas de pintura se necesitan?", "18//3", "Se divide el número de niños entre los niños por bandeja.", " bandejas"),
        ("abc", "{F} ¿Qué lleva el rótulo de la caja de las esponjas?", "El nombre del material y un dibujo, como «Esponjas para pintar»", "El nombre de cada niño que la usa", "Una foto de los niños pintando", "El rótulo identifica el material; no lleva nombres ni fotos de niños."),
        ("=", "{F} ¿Cuántos paquetes de esponjas hay que comprar para tener las que se necesitan?", "(20+5)//6", "Se divide las esponjas necesarias entre las del paquete y se redondea hacia arriba.", " paquetes"),
        ("=", "{F} ¿Cuánto cuestan los paquetes de esponjas que hay que comprar?", "4*2400", "Se multiplican los paquetes por el precio de cada uno.", " pesos"),
        ("abc", "{F} Al terminar la experiencia, las esponjas quedan húmedas. ¿Qué hace la técnica?", "Las lava y las seca antes de guardarlas", "Las guarda mojadas para que no se resequen", "Las deja en la bandeja de pintura", "El material se guarda limpio y seco por higiene."),
        ("=", "{F} Cada niño recibe 2 hojas y se agregan 4 de repuesto. ¿Cuántas hojas se preparan?", "18*2+4", "Se multiplican las hojas por niño y se suma el repuesto.", " hojas"),
        ("=", "{F} Se guardan las 24 esponjas compradas en la caja de 25. ¿Cuántos espacios libres quedan?", "25-24", "Se restan las esponjas guardadas a la capacidad de la caja.", " espacio"),
        ("abc", "{F} Durante la experiencia se derrama pintura en el piso. ¿Qué hace la técnica?", "Avisa a la educadora, limpia el piso y despeja a los niños de la zona", "Sigue la experiencia para no perder tiempo", "Pide a un niño que limpie solo", "Una zona resbalosa es un riesgo; se despeja, se limpia y se informa."),
        ("abc", "{F} Faltan 2 esponjas porque llegaron más niños. ¿Qué hace la técnica?", "Propone compartir esponjas y lo informa a la educadora", "Compra esponjas de inmediato sin avisar", "Excluye a los 2 últimos niños", "Compartir permite que todos participen y la educadora decide cómo seguir."),
        ("abc", "{F} Para exponer los trabajos, un compañero propone colgar solo los 5 «más bonitos». ¿Qué observación corresponde?", "Conviene exponer el trabajo de cada niño, a su altura", "Está bien, para que el panel se vea mejor", "Está bien, porque los demás aprenderán a esforzarse", "Exponer a todos respeta a cada niño; no se comparan ni se descartan trabajos."),
        ("=", "{F} Si se compran 4 paquetes, ¿cuánto dinero del presupuesto de ejemplo queda?", "10000-4*2400", "Se resta el costo de los paquetes al presupuesto.", " pesos"),
        ("abc", "{F} Después de la experiencia, ¿qué debe quedar actualizado?", "El inventario con cuánto material queda y en qué estado", "El horario de los niños que no asistieron", "El dibujo de cada niño", "El inventario refleja lo que realmente hay para la próxima experiencia."),
    ],
    ctx=("abc", "{F} La educadora cambia la experiencia a último momento y ahora asisten 20 niños, no 18. ¿Qué hace la técnica con la preparación?", "Recalcula esponjas, hojas y bandejas con 20 niños y avisa a la educadora si no alcanza", "Mantiene los cálculos de 18 niños", "Cancela la experiencia sin avisar", "Los cálculos dependen del número real de niños y las faltas se informan."),
    sc=[
        ("En Atención de Párvulos: ¿qué se suma al material por niño?", "El repuesto", "El repuesto cubre material que se estropea o falta."),
        ("¿Cómo se calcula cuántos paquetes comprar?", "Dividiendo lo necesario entre el contenido del paquete y redondeando hacia arriba", "No se puede comprar medio paquete."),
        ("¿Cómo se guarda el material de pintar?", "Limpio y seco, en una caja rotulada", "La higiene y el rótulo permiten su uso seguro después."),
    ],
    op=("Datos de ejemplo: nivel de transición, 22 niños y niñas. Experiencia: armar un cartel colectivo con retazos de tela. Cada niño usa 3 retazos y se agregan 5 de repuesto. Los retazos vienen en bolsas de 10 a $1.800 la bolsa (precio de ejemplo). Presupuesto: $6.000. Caja para guardar con espacio para 80 retazos. "
        "Escribe: cuántos retazos se necesitan, cuántas bolsas, cuánto cuestan, si alcanza el presupuesto, cómo guardarías lo que sobra y cómo expondrías los trabajos.",
        "Retazos: 22 × 3 + 5 = 71. Bolsas: 71 ÷ 10 = 7 y sobra 1, se compran 8. Costo: 8 × 1.800 = 14.400, que supera el presupuesto de 6.000, así que se informa a la educadora para ajustar. Lo que sobra se limpia y se guarda en la caja de 80 con rótulo. Se exponen los trabajos de cada niño, a su altura.",
        ["calcula retazos, bolsas y costo", "compara con el presupuesto e informa", "propone guardar y exponer con criterios"],
        ["hoja con cuatro cálculos y dos decisiones"],
        ["olvidar el repuesto", "no redondear hacia arriba las bolsas", "decidir el ajuste sin avisar a la educadora"],
        "Pregunta: «¿qué pasaría si compras 7 bolsas?». Debe ver que serían 70 retazos, insuficientes."),
    reinforce="Inventa una experiencia con 15 niños y calcula el material con repuesto y el costo de los paquetes.",
    extend="Explica por qué se redondea hacia arriba al calcular cuántos paquetes comprar.",
)

"""Interpretación musical 3.º y 4.º medio HC: OAC-04 (analizar estéticamente obras de distintas épocas y procedencias: lenguaje musical, procedimientos, técnicas, producción y contexto). Obras inventadas y descritas en texto."""
from __future__ import annotations

from hc_imus_common import build

O4 = "AR-IMUS-3y4-OAC-04"

OBRAS = ("Obra 1, «Danza de salón» (ejemplo inventado de una pieza de salón de una época pasada): piano y violín; 90 pulsos por minuto; compases de 3 pulsos; "
         "el violín canta la melodía en frases de 4 compases y el piano acompaña con acordes; forma A B A; dinámica entre p y mf. "
         "Obra 2, «Canción de faena» (ejemplo inventado de una canción de tradición oral de una zona rural): una voz solista y un coro que responde, con un tambor de mano; 100 pulsos por minuto; "
         "forma de pregunta y respuesta; ritmo constante y repetido; sin acordes de acompañamiento. "
         "Obra 3, «Paisaje de pulsos» (ejemplo inventado de una pieza electrónica reciente): sonidos grabados y sintetizados; 120 pulsos por minuto; un patrón rítmico de 4 pulsos que se repite (loop); "
         "los timbres cambian poco a poco; forma libre; un crescendo largo. ")

# ============================================================ OAC-04, clase 1
F = "Ficha 1 (tres obras de ejemplo; las obras reales las aporta tu docente). " + OBRAS
build(
    O4, 1, F,
    use="Aprenderé a reconocer los elementos del lenguaje musical (ritmo, melodía, armonía, timbre, forma, textura y dinámica) en obras de épocas y procedencias distintas y a describirlos con evidencia antes de interpretarlos.",
    prior=["Reconozco fraseo, ritmo, dinámica y acorde.", "Sé leer datos de una ficha.", "Sé distinguir una descripción de una opinión."],
    explain=[
        "Analizar una obra empieza por describir lo que se oye o se lee en ella. Los elementos del lenguaje musical son las piezas con las que una obra está construida: el ritmo (patrón de duraciones sobre el pulso), la melodía (sucesión de sonidos de distinta altura), la armonía (los acordes que acompañan), el timbre (el color del sonido), la dinámica (fuerza o suavidad), la forma (cómo se organizan las secciones, por ejemplo A B A) y la textura (cómo se combinan las partes que suenan a la vez).",
        "La textura puede ser de una sola voz, de una melodía con acompañamiento, o de varias capas. La forma puede ser de secciones que vuelven (A B A), de pregunta y respuesta, o libre. Cada obra combina los elementos de manera distinta, aunque sea de otra época o de otro lugar: se analizan con las mismas preguntas. Describir no es valorar: «tiene un patrón de 4 pulsos que se repite» es una descripción; «es aburrida» es una opinión.",
        "Para analizar con evidencia se cita el dato de la obra que respalda cada afirmación. Una tabla de dos columnas, con el elemento a la izquierda y la evidencia a la derecha, ordena el trabajo. Esta clase usa obras inventadas descritas en una ficha; las obras reales, con su autoría, las aporta tu docente. Si se escucha música en sala, el volumen es moderado y se hacen pausas de silencio.",
    ],
    vocab=[("lenguaje musical", "conjunto de elementos con que se construye una obra"), ("textura", "manera en que se combinan las partes que suenan a la vez"),
           ("forma", "organización de las secciones de una obra, como A B A"), ("loop", "patrón corto que se repite una y otra vez"),
           ("timbre", "color del sonido que distingue un instrumento o una voz"), ("evidencia", "dato de la obra que respalda una afirmación")],
    worked=[
        ("Describir con evidencia", "Una obra de ejemplo dice: violín que canta, piano que acompaña con acordes, forma A B A. Describe su textura y su forma.",
         ["La textura es melodía con acompañamiento: el violín lleva la melodía y el piano la acompaña.", "La forma es A B A: la primera sección vuelve al final."],
         "Textura de melodía con acompañamiento; forma A B A"),
        ("Distinguir descripción y opinión", "Dos comentarios sobre una obra: (a) «repite un patrón de 4 pulsos»; (b) «es muy linda». ¿Cuál describe?",
         ["El comentario (a) nombra un rasgo comprobable en la obra.", "El comentario (b) expresa una opinión que no se puede comprobar con un dato."],
         "El comentario (a)"),
    ],
    mistakes=[("Escribir «suena bonito» como si fuera un elemento del lenguaje musical.", "Es una opinión, no un elemento que se pueda comprobar.", "Nombra el elemento (ritmo, timbre, forma) y cita el dato que lo respalda."),
              ("Confundir la forma de una obra con su tempo.", "La forma organiza las secciones; el tempo es la velocidad del pulso.", "Pregunta: ¿cómo se organizan las secciones? Eso es la forma.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es la textura de una obra?', 'La manera en que se combinan las partes que suenan a la vez en la obra', 'El material con que está fabricado cada instrumento que suena en la obra', 'La cantidad de veces que se repite el título de la obra en el programa', 'La textura se refiere a cómo se combinan las voces o partes; no es material ni título.'),
        ('abc', '{F} ¿Qué instrumentos tiene la obra 1?', 'Piano y violín, con el violín a cargo de la melodía', 'Voz solista y coro, con un tambor de mano que marca el ritmo', 'Sonidos grabados y sintetizados, con un patrón repetido', 'La obra 1 usa piano y violín; las otras dos tienen instrumentación distinta.'),
        ('abc', '{F} ¿Qué forma tiene la obra 1?', 'A B A, porque la primera sección vuelve al final', 'Pregunta y respuesta, porque dialogan dos partes distintas', 'Libre, porque no repite ninguna sección en toda la obra', 'La ficha señala que la obra 1 tiene forma A B A.'),
        ('=', '{F} El patrón de 4 pulsos de la obra 3 se repite 8 veces seguidas. ¿Cuántos segundos dura esa repetición a 120 pulsos por minuto?', '8*4*60//120', 'Se multiplican las repeticiones por 4 pulsos y se pasa a segundos con el tempo.', ' s'),
        ('abc', '{F} ¿Cómo es la textura de la obra 2?', 'Una voz solista con respuesta de un coro y un tambor, sin acordes', 'Una melodía de violín con acordes de piano en el fondo de la sala', 'Capas de sonidos electrónicos que cambian de timbre poco a poco', 'La ficha describe una voz solista, un coro que responde y un tambor, sin acordes.'),
        ('abc', '{F} ¿Qué obra usa un loop y cuál es su rasgo de ritmo?', 'La obra 3, con un patrón de 4 pulsos que se repite', 'La obra 1, con un patrón de 3 pulsos que se repite en cada frase', 'La obra 2, con un patrón de 5 pulsos que se repite sin cambios', 'Solo la obra 3 tiene un patrón rítmico de 4 pulsos repetido, o sea un loop.'),
        ('=', '{F} Una frase de la obra 1 tiene 4 compases de 3 pulsos a 90 pulsos por minuto. ¿Cuántos segundos dura?', '4*3*60//90', 'Se multiplican los compases por los pulsos de cada uno y se pasa a segundos.', ' s'),
        ('abc', '{F} ¿Qué comentario sobre la obra 3 es una descripción con evidencia?', 'El timbre cambia poco a poco mientras el patrón de 4 pulsos se repite', 'Es una obra rara que no se parece a ninguna otra del programa del grupo', 'Es una obra muy moderna y por eso resulta superior a las otras dos', 'Un comentario descriptivo cita un dato comprobable de la ficha, como el cambio gradual de timbre.'),
        ('abc', '{F} Una estudiante dice que los ritmos de las obras 2 y 3 se parecen. ¿Qué respuesta es correcta?', 'Es válido: las dos repiten un patrón rítmico, aunque con timbres y tempos distintos', 'No es válido, porque la obra 2 no tiene ritmo al no usar acordes de acompañamiento', 'Es válido, porque las dos tienen exactamente el mismo tempo y el mismo timbre', 'La obra 2 tiene un ritmo constante y repetido y la 3 un loop; ambas repiten patrones, aunque con otros timbres y tempos.'),
        ('abc', '{F} ¿A qué elemento corresponde «frases de 4 compases en el violín»?', 'A la melodía y al fraseo de la obra 1', 'Al timbre de los sonidos sintetizados de la obra 3', 'A la forma de pregunta y respuesta de la obra 2', 'La frase de 4 compases es un dato de la melodía y el fraseo, y se ubica en la obra 1.'),
        ('abc', '{F} Se comparan la textura de las obras 1 y 2. ¿Cuál comparación es correcta?', 'La obra 1 tiene melodía con acompañamiento de acordes y la obra 2 no tiene acordes', 'La obra 1 tiene solo una voz sin acompañamiento y la obra 2 tiene acordes de piano', 'Las dos tienen exactamente la misma textura, hecha de capas electrónicas', 'La obra 1 usa piano con acordes y la obra 2 se acompaña con coro y tambor, sin acordes.'),
        ('abc', 'Dos estudiantes analizan la obra 3. Teo: «tiene un loop de 4 pulsos y un crescendo largo»; Lía: «es rarísima». ¿Quién hace un análisis con evidencia?', 'Teo, porque nombra elementos que se pueden comprobar', 'Lía, porque dice lo que le provoca la pieza', 'Los dos, porque cada uno dice lo que piensa', 'Un análisis usa datos comprobables; «rarísima» es una impresión sin dato.'),
        ('=', '{F} En la obra 2, la voz solista pregunta durante 4 pulsos y el coro responde durante 4 pulsos. ¿Cuántos pulsos hay en 6 intercambios de pregunta y respuesta?', '6*(4+4)', 'Cada intercambio suma 8 pulsos y se multiplica por 6 intercambios.', ' pulsos'),
    ],
    ctx=('abc', 'Tu docente te pide describir una obra desconocida antes de opinar sobre ella. ¿Qué paso corresponde primero?', 'Anotar elementos como tempo, timbre y forma con un dato de la obra para cada uno', 'Escribir si te gustó o no te gustó y justificar con tus propios recuerdos de otras obras', 'Buscar la opinión de otra persona y copiarla como tuya antes de escuchar', 'Primero se describe con evidencia; la opinión viene después y se apoya en esa descripción.'),
    sc=[
        ("En Interpretación musical: ¿qué es la forma de una obra?", "La organización de sus secciones, como A B A", "La forma dice cómo se ordenan las secciones."),
        ('abc', 'Una descripción con evidencia:', 'Cita un dato comprobable de la obra', 'Expresa si la obra gusta o no a la persona que escribe', 'Compara la obra con otra de memoria y sin datos', 'Describir es nombrar con datos lo que se puede comprobar.'),
        ("¿Qué haces si escuchas música en sala con volumen alto y sientes molestia en el oído?", "Pido bajar el volumen y hago una pausa de silencio", "El oído se cuida con volumen moderado y pausas."),
    ],
    op=("Con la {F}, elige dos obras y completa una tabla con cuatro elementos del lenguaje musical (tempo, textura, forma y timbre) y la evidencia de cada uno. Después escribe una frase que compare las dos obras en uno de esos elementos.",
        "Obras 1 y 3. Tempo: 90 pulsos por minuto y 120. Textura: melodía con acompañamiento y capas electrónicas. Forma: A B A y forma libre. Timbre: piano y violín, y sonidos grabados y sintetizados. Comparación: la obra 3 es más rápida (120) que la obra 1 (90).",
        ["completa cuatro elementos para dos obras", "cita una evidencia por elemento", "escribe una comparación con datos", "no mezcla descripción con opinión"],
        ["hoja con la tabla y la frase de comparación"],
        ["usar opiniones como evidencia", "olvidar un elemento", "comparar sin datos"],
        "Pregunta: «¿de dónde sacaste ese dato?». Si no lo cita, pídele que lo busque en la ficha."),
    reinforce="Describe una obra inventada con cuatro elementos del lenguaje musical y su evidencia, sin usar opiniones.",
    extend="Explica por qué obras de épocas y lugares muy distintos pueden analizarse con las mismas preguntas.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (dos versiones de una pieza de ejemplo «Paisaje de pulsos», inventadas). "
     "Versión acústica: tambor de mano, flauta y voz, tocadas en una sala, a 120 pulsos por minuto; el volumen depende de cómo se toca; se escucha el aire de la flauta y el roce de la mano en el tambor. "
     "Versión de estudio: los mismos sonidos, grabados con micrófonos, editados (se corta un patrón de 4 pulsos y se repite 8 veces), con un efecto de eco y mezclados (se ajusta el nivel de cada sonido: tambor medio, flauta bajo, voz alto). "
     "Procesos: grabar es captar el sonido con micrófono; editar es cortar, repetir o mover fragmentos; mezclar es ajustar el nivel de cada sonido; un efecto, como el eco, modifica el sonido original. "
     "Cuidado: quien edita escucha con audífonos a volumen moderado y descansa 5 minutos por cada 30.")
build(
    O4, 2, F,
    use="Aprenderé a reconocer procedimientos, técnicas y recursos de producción (grabación, edición, mezcla, efectos y amplificación) y a relacionarlos con el efecto estético de una obra, cuidando el oído.",
    prior=["Reconozco los elementos del lenguaje musical.", "Sé describir con evidencia.", "Sé que el volumen se cuida."],
    explain=[
        "Los procedimientos son maneras de organizar el material musical, como repetir un patrón o hacer un crescendo. Las técnicas son formas de tocar o producir un sonido, como el golpe suave en un tambor o el soplo en una flauta. Los recursos de la producción musical son las herramientas con que la obra llega a quien escucha: micrófonos, amplificación, grabación, edición, mezcla y efectos. Cada uno deja huellas audibles en el resultado.",
        "Grabar es captar el sonido con un micrófono. Editar es cortar, repetir o mover fragmentos grabados; por ejemplo, repetir un patrón de 4 pulsos 8 veces crea un loop. Mezclar es ajustar el nivel (qué tan fuerte suena cada parte respecto de las otras) para que la voz o un instrumento quede al frente o al fondo. Un efecto, como el eco, modifica un sonido: da sensación de un espacio más amplio. Una versión acústica, en cambio, suena como se toca en la sala.",
        "Analizar estéticamente es relacionar estos recursos con lo que provoca la obra. Un loop produce sensación de insistencia; un eco, de espacio; una voz al frente, de cercanía. Una afirmación se apoya en un dato de la ficha. Quien edita o mezcla escucha con audífonos a volumen moderado y descansa, porque un volumen alto y continuo puede dañar el oído.",
    ],
    vocab=[("procedimiento", "manera de organizar el material musical, como repetir"), ("técnica", "forma de tocar o producir un sonido"), ("edición", "corte, repetición o cambio de lugar de fragmentos grabados"),
           ("mezcla", "ajuste del nivel de cada sonido respecto de los otros"), ("efecto", "modificación del sonido original, como el eco"), ("nivel", "qué tan fuerte suena una parte respecto de las otras")],
    worked=[
        ("Reconocer un proceso", "En una versión de estudio de ejemplo, se sube la voz y se baja la guitarra para que se entienda mejor lo que se canta. ¿Qué proceso es?",
         ["Se está ajustando qué tan fuerte suena cada parte respecto de las otras.", "Ese ajuste de niveles se llama mezcla."],
         "Mezcla"),
        ("Relacionar recurso y efecto", "Una obra de ejemplo repite un patrón de 2 pulsos 16 veces seguidas. ¿Qué efecto estético puede producir y por qué?",
         ["Una repetición larga de un patrón es un loop, hecho por edición o por tocar siempre igual.", "Provoca sensación de insistencia o de trance, porque el oído se acostumbra al patrón."],
         "Insistencia: la repetición larga de un loop"),
    ],
    mistakes=[("Llamar «mezcla» al hecho de cortar y repetir un fragmento.", "Se confunden edición y mezcla.", "Cortar y repetir es edición; ajustar niveles es mezcla."),
              ("Afirmar que lo grabado «suena mejor» que lo acústico.", "Se valora sin criterio ni evidencia.", "Describe qué recurso cambió y qué efecto produjo, sin decir que uno es mejor.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es la mezcla?', 'El ajuste del nivel de cada sonido respecto de los otros', 'El corte y la repetición de fragmentos de una grabación de la sala', 'La captura del sonido con un micrófono en una sala de ensayo', 'Mezclar es equilibrar niveles; editar es cortar y repetir; grabar es captar.'),
        ('abc', '{F} ¿Qué proceso repite 8 veces el patrón de 4 pulsos?', 'La edición, que corta y repite un fragmento grabado', 'La mezcla, que ajusta el nivel de cada sonido grabado', 'La grabación, que capta el sonido con un micrófono en la sala', 'La ficha dice que se corta un patrón y se repite: eso es edición.'),
        ('abc', '{F} ¿Qué efecto se agrega en la versión de estudio?', 'Un eco', 'Una amplificación del tambor', 'Un cambio de instrumentos', 'La ficha dice que se aplica un efecto de eco al sonido.'),
        ('=', '{F} El patrón editado tiene 4 pulsos y se repite 8 veces a 120 pulsos por minuto. ¿Cuántos segundos dura?', '8*4*60//120', 'Se multiplican las repeticiones por los pulsos y se pasa a segundos con el tempo.', ' s'),
        ('abc', '{F} ¿Qué nivel tiene la voz en la mezcla de la versión de estudio?', 'Alto, es decir, al frente', 'Medio, igual que el tambor', 'Bajo, igual que la flauta', 'La ficha indica voz alta, tambor medio y flauta baja.'),
        ('abc', '{F} ¿Qué detalle se escucha solo en la versión acústica según la ficha?', 'El aire de la flauta y el roce de la mano en el tambor', 'El eco que alarga cada golpe del tambor en la sala', 'El patrón de 4 pulsos repetido ocho veces', 'La ficha señala que esos sonidos pequeños se oyen en la versión acústica de la sala.'),
        ('=', '{F} Quien edita trabaja 90 minutos con audífonos y descansa 5 minutos por cada 30 minutos. ¿Cuántos minutos de descanso suma en total?', '90//30*5', 'Se divide el tiempo de trabajo en bloques de 30 minutos y se multiplica por 5.', ' minutos'),
        ('abc', '{F} ¿Qué efecto estético puede provocar el eco de la versión de estudio?', 'Sensación de un espacio más amplio', 'Sensación de que el sonido se acerca al oído', 'Sensación de que la música es más lenta', 'El eco alarga el sonido y sugiere un espacio grande.'),
        ('abc', '{F} Una estudiante dice que la versión de estudio «suena mejor» que la acústica. ¿Qué observación corresponde?', 'Es una valoración sin evidencia; conviene decir qué recurso cambia y qué efecto produce', 'Es un análisis correcto, porque lo grabado siempre es de mejor calidad que lo que se toca en sala', 'Es un análisis incorrecto, porque lo acústico siempre es mejor que lo grabado en estudio', 'Un análisis estético describe recursos y efectos; «suena mejor» no ofrece evidencia.'),
        ('abc', '{F} Se desea que la flauta se oiga más cerca en la mezcla sin cambiar la grabación. ¿Qué proceso se usa?', 'La mezcla, subiendo el nivel de la flauta', 'La edición, cortando fragmentos de la flauta', 'La grabación, cambiando la flauta por otro instrumento', 'Subir un nivel es una decisión de mezcla; no es edición ni grabación.'),
        ('abc', '{F} Un grupo quiere un efecto de insistencia en una pieza. ¿Qué recurso de la ficha conviene?', 'La edición que repite un patrón corto, como un loop', 'La mezcla que baja la voz al fondo de la pieza', 'El eco que se aplica solo al final de la pieza grabada', 'La repetición larga de un patrón produce insistencia.'),
        ('abc', 'Un estudiante edita a todo volumen durante dos horas sin descansar, porque «así se oye mejor». ¿Qué falla?', 'No cuida el oído, que necesita volumen moderado y descansos', 'No usa suficientes efectos para que la pieza suene buena al público', 'No sube el volumen lo suficiente para escuchar bien todos los detalles', 'Un volumen alto sin descanso puede dañar el oído; conviene moderar y descansar.'),
        ('=', '{F} En la mezcla se suben 2 niveles de la flauta y se bajan 3 de la voz, partiendo de niveles iguales. ¿Cuántos niveles de diferencia hay entre ambas?', '2+3', 'La flauta sube 2 y la voz baja 3, por lo que la distancia entre ambas es la suma.', ' niveles'),
    ],
    ctx=('abc', 'Escuchas una pieza en la que cada golpe de tambor se repite alargado, como en un espacio grande. ¿Qué recurso de producción es el más probable?', 'Un efecto de eco aplicado al sonido', 'Una edición que corta la voz en pedazos', 'Una mezcla que baja el tambor de la obra', 'Un golpe alargado y repetido como en un espacio grande es el rasgo de un eco.'),
    sc=[
        ("En Interpretación musical: ¿qué es la edición?", "El corte, repetición o cambio de lugar de fragmentos grabados", "Editar es trabajar sobre fragmentos que ya fueron grabados."),
        ('abc', 'Un efecto es:', 'Una modificación del sonido original', 'Un instrumento nuevo que se suma a la obra', 'Un ajuste de volumen de toda la sala de escucha', 'El efecto cambia el sonido original, como un eco.'),
        ("¿Qué haces si trabajas con audífonos y sientes zumbido o molestia?", "Bajo el volumen, descanso y aviso a una persona adulta si sigue", "El oído se protege con moderación y descanso."),
    ],
    op=("Con la {F}, escribe un análisis estético de tres frases de la versión de estudio: una que nombre un proceso (edición, mezcla o efecto), otra que diga qué efecto produce y otra que compare con la versión acústica. Cada frase debe citar un dato de la ficha.",
        "El patrón de 4 pulsos se repite 8 veces por edición. Esa repetición produce sensación de insistencia, porque el oído escucha 8 veces el mismo patrón. En la versión acústica el patrón no está editado, y se oyen el aire de la flauta y el roce del tambor.",
        ["nombra un proceso con su dato", "relaciona el recurso con un efecto", "compara con la versión acústica", "no valora sin evidencia"],
        ["hoja con las tres frases de análisis"],
        ["confundir edición con mezcla", "valorar sin evidencia", "no citar un dato de la ficha"],
        "Pregunta: «¿qué dato de la ficha sostiene esa frase?». Si no lo cita, pídele que lo busque."),
    reinforce="Escribe tres parejas de «proceso de producción» y «efecto» para una pieza inventada.",
    extend="Explica cómo cambiaría la sensación de una pieza acústica si se grabara en una sala pequeña y en una grande.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (lecturas de una obra de ejemplo, inventada). Obra 2, «Canción de faena»: una voz solista y un coro que responde, con un tambor de mano; 100 pulsos por minuto; "
     "forma de pregunta y respuesta; ritmo constante y repetido; sin acordes de acompañamiento. "
     "Tres lecturas de ejemplo de lo que expresa: "
     "Lectura A: «expresa un trabajo compartido, porque la voz pregunta y el grupo responde, y el ritmo constante marca el esfuerzo continuo». "
     "Lectura B: «expresa soledad, porque la voz solista domina toda la obra». "
     "Lectura C: «expresa la elegancia de un baile de salón, porque tiene acordes y compases de 3 pulsos». "
     "Condición nueva: en una versión de ejemplo, el coro canta tan fuerte que tapa a la voz solista.")
build(
    O4, 3, F,
    use="Aprenderé a relacionar elementos del lenguaje musical con lo que una obra expresa, a elegir entre varias lecturas con dos evidencias y a revisar la lectura cuando cambia una condición.",
    prior=["Reconozco elementos del lenguaje musical.", "Sé relacionar recursos con efectos.", "Sé que una opinión necesita evidencia."],
    explain=[
        "Una lectura estética es una explicación de lo que una obra expresa o provoca, apoyada en sus elementos. No se trata de adivinar lo que «quiso decir» la persona que la hizo, sino de explicar qué producen los elementos que se oyen. Una lectura sólida relaciona cada afirmación con un elemento: «el ritmo constante y repetido produce sensación de continuidad».",
        "Cuando hay varias lecturas posibles, se comparan con evidencia. Se revisa cuál usa más elementos de la obra y cuál contradice algún dato. Una lectura que usa dos o más evidencias y no choca con ningún dato es más fuerte que una basada en un solo rasgo. Las lecturas pueden ser diferentes y a la vez válidas si todas se apoyan en la obra, pero una que contradice un dato (como decir «tiene acordes» cuando no los tiene) no se sostiene.",
        "Una lectura también se revisa si cambia una condición. Si en una versión nueva el coro tapa a la voz solista, la relación de pregunta y respuesta se oye menos, y la lectura de trabajo compartido puede volverse más débil. Revisar es parte del análisis: se anota qué cambió y cómo afecta a la lectura. Todo se hace con la ficha en la mano, sin necesidad de escuchar música.",
    ],
    vocab=[("lectura estética", "explicación de lo que una obra expresa, apoyada en sus elementos"), ("evidencia", "dato de la obra que respalda la lectura"), ("contradecir", "afirmar algo que choca con un dato de la obra"),
           ("expresar", "hacer sentir o comunicar una idea o emoción"), ("condición", "circunstancia que puede cambiar, como el volumen del coro"), ("sostener", "apoyar una lectura con datos")],
    worked=[
        ("Evaluar una lectura", "Una lectura de ejemplo dice: «la obra expresa velocidad, porque su pulso es de 60 por minuto». ¿Se sostiene?",
         ["Un pulso de 60 por minuto es lento: contradice la lectura de velocidad.", "No se sostiene, porque choca con el dato de la obra."],
         "No se sostiene: el dato contradice la lectura"),
        ("Revisar al cambiar la condición", "Una lectura dice que una obra expresa diálogo, porque una voz pregunta y otra responde. En una versión nueva, ambas voces suenan al mismo tiempo. ¿Qué pasa con la lectura?",
         ["La evidencia del diálogo era que se alternan las voces.", "Si suenan juntas, esa evidencia se pierde y la lectura se debilita."],
         "Se debilita, porque ya no se alternan las voces"),
    ],
    mistakes=[("Decir «el autor quiso expresar tristeza» sin ningún dato de la obra.", "No hay evidencia en los elementos.", "Explica qué elementos producen la sensación y cítalos."),
              ("Mantener la lectura aunque cambie la versión.", "Se olvida revisar la evidencia.", "Anota qué cambió y si la evidencia sigue valiendo.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una lectura estética de una obra?', 'Una explicación de lo que expresa, apoyada en sus elementos', 'Una lista de las notas que la obra utiliza de principio a fin', 'La opinión de la mayoría sobre si la obra gustó o no', 'La lectura estética se basa en elementos de la obra, no en una lista de notas ni en una votación.'),
        ('abc', '{F} ¿Qué evidencia usa la lectura A?', 'La pregunta y respuesta entre la voz y el coro, y el ritmo constante', 'Los acordes del piano y los compases de 3 pulsos de la obra 1', 'El loop de 4 pulsos y los sonidos sintetizados de la obra 3', 'La lectura A cita la pregunta y respuesta y el ritmo constante de la ficha.'),
        ('abc', '{F} ¿Qué dato de la ficha contradice la lectura C?', 'La obra no tiene acordes de acompañamiento', 'La obra usa un tambor de mano para marcar el ritmo', 'La obra tiene un coro que responde a la voz solista', 'La lectura C afirma que tiene acordes, y la ficha dice que no los tiene.'),
        ('abc', '{F} ¿Qué dato de la ficha apoya la lectura A?', 'El coro responde a la voz que pregunta', 'La voz solista domina siempre y nadie le responde', 'Los compases son de 3 pulsos, como en un baile', 'La alternancia entre voz y coro respalda la lectura de trabajo compartido.'),
        ('=', '{F} A 100 pulsos por minuto, ¿cuántos segundos duran 10 intercambios de 8 pulsos cada uno (pregunta y respuesta)?', '10*8*60//100', 'Se multiplican los intercambios por 8 pulsos y se pasa a segundos con el tempo.', ' s'),
        ('abc', '{F} ¿Qué lectura se sostiene mejor con dos evidencias y sin contradecir ningún dato?', 'La lectura A', 'La lectura B', 'La lectura C', 'La lectura A usa la pregunta y respuesta y el ritmo constante, y no choca con la ficha.'),
        ('abc', '{F} La lectura B dice que la obra expresa soledad porque la voz solista domina. ¿Qué dato la debilita?', 'Un coro responde a la voz solista en cada intercambio', 'El tambor de mano marca un ritmo repetido en toda la obra', 'El tempo de la obra es de 100 pulsos por minuto', 'La respuesta del coro contradice que la voz esté sola en la obra.'),
        ('=', '{F} El tempo de la obra es de 100 pulsos por minuto. ¿Cuántos pulsos hay en 30 segundos?', '100*30//60', 'Se multiplican los pulsos por minuto por los segundos y se divide por 60.', ' pulsos'),
        ('abc', '{F} En la versión de ejemplo, el coro canta tan fuerte que tapa la voz solista. ¿Qué pasa con la lectura A?', 'Se debilita, porque la pregunta y respuesta se oye menos', 'Se fortalece, porque el coro representa a todo el grupo', 'No cambia, porque el ritmo constante sigue siendo el mismo', 'Si no se oye la voz que pregunta, se pierde la evidencia de la pregunta y respuesta.'),
        ('abc', '{F} Un estudiante propone que A y B pueden ser válidas a la vez. ¿Qué observación es correcta?', 'B choca con un dato (el coro responde), así que no es válida en igual medida', 'Las dos son igual de válidas, porque toda lectura de una obra es correcta', 'Ninguna es válida, porque no se puede saber nunca lo que expresa una obra', 'Una lectura debe apoyarse en datos; la B contradice la respuesta del coro.'),
        ('abc', '{F} ¿Cuál es la mejor manera de revisar la lectura A con la nueva versión?', 'Anotar qué cambió (el coro tapa a la voz) y cómo afecta a la evidencia', 'Mantener la lectura sin cambios porque ya estaba escrita en el cuaderno', 'Eliminar la lectura y no escribir ninguna otra sobre la obra nueva', 'Revisar es comparar la nueva condición con la evidencia y anotar el efecto.'),
        ('abc', 'Una estudiante afirma que una obra «expresa nostalgia» sin citar ningún elemento. ¿Qué respuesta corresponde?', 'Pedirle qué elementos de la obra producen esa sensación', 'Aceptarla, porque nadie puede discutir lo que alguien siente', 'Rechazarla, porque las emociones no se pueden analizar', 'Una lectura estética necesita elementos citados; sentir algo no basta como evidencia.'),
        ('=', '{F} En una pasada de 12 segundos, a 100 pulsos por minuto, ¿cuántos pulsos marca el tambor de mano?', '12*100//60', 'Se multiplican los segundos por los pulsos por minuto y se divide por 60.', ' pulsos'),
    ],
    ctx=('abc', 'En clase escuchan una canción nueva y tu compañero dice «es triste», pero la canción va a 130 pulsos por minuto, en volumen fuerte y con ritmo saltarín. ¿Qué haces?', 'Preguntar qué elementos producen la tristeza y comparar con esos datos', 'Decirle que no tiene razón porque la música es siempre alegre y nunca triste', 'Aceptar sin preguntar nada para no discutir con él en clase', 'La lectura se revisa con los elementos; si no calzan, se pide la evidencia.'),
    sc=[
        ("En Interpretación musical: ¿cuándo se sostiene una lectura estética?", "Cuando se apoya en datos de la obra y no los contradice", "Una lectura necesita evidencia y coherencia con la obra."),
        ('abc', 'Si cambia una condición de la obra, la lectura:', 'Se revisa con la evidencia', 'Se mantiene igual', 'Se borra sin revisar', 'La condición nueva puede debilitar o fortalecer la evidencia.'),
        ("¿Por qué no basta decir «a mí me gustó» como análisis?", "Porque no cita ningún elemento ni dato de la obra", "El gusto personal no es evidencia sobre lo que la obra contiene."),
    ],
    op=("Con la {F}, elige una de las tres lecturas, cita dos evidencias que la sostienen o la debilitan y explica qué pasa con la lectura en la versión donde el coro tapa a la voz solista.",
        "Elijo la lectura A. Evidencia 1: la voz pregunta y el coro responde. Evidencia 2: el ritmo constante y repetido. En la versión donde el coro tapa a la voz, la pregunta y respuesta se oye menos y la lectura se debilita, porque pierde la evidencia 1.",
        ["elige una lectura", "cita dos evidencias de la ficha", "revisa la lectura con la nueva condición", "usa «porque» para justificar"],
        ["hoja con la lectura elegida, dos evidencias y la revisión"],
        ["citar una evidencia que no está en la ficha", "no revisar con la condición nueva", "elegir sin evidencia"],
        "Pregunta: «¿qué dato de la ficha sostiene eso?». Si no lo cita, pídele que lo busque."),
    reinforce="Escribe dos lecturas distintas de una obra inventada y marca cuál se sostiene mejor, con dos evidencias.",
    extend="Explica por qué dos lecturas diferentes de una misma obra pueden ser válidas a la vez si ambas se apoyan en datos.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (contexto de dos obras de ejemplo, inventadas; los datos de contexto de obras reales los aporta tu docente). "
     "Obra 1, «Danza de salón»: pieza de una época pasada (ejemplo), de ciudad; se tocaba para bailar en salones; compases de 3 pulsos y ritmo regular; piano y violín. "
     "Obra 2, «Canción de faena»: canción de tradición oral, de una zona rural (ejemplo); se cantaba durante tareas compartidas; voz solista y coro que responde; ritmo constante y repetido; sin acordes. "
     "Obra 3, «Paisaje de pulsos»: pieza electrónica reciente (ejemplo), hecha en un estudio; se escucha en sala o con audífonos; patrón repetido de 4 pulsos y timbres que cambian. "
     "Regla de análisis: se relaciona el contexto con los elementos de la obra, sin decir que una obra o tradición es mejor o más avanzada que otra.")
build(
    O4, 4, F,
    use="Aprenderé a relacionar aspectos contextuales (época, procedencia y función) con los elementos de una obra, a comparar dos obras con evidencia y a evitar juicios que pongan unas tradiciones sobre otras.",
    prior=["Sé describir los elementos de una obra.", "Sé relacionar recursos con efectos.", "Sé revisar una lectura con evidencia."],
    explain=[
        "El contexto de una obra son las circunstancias en que se hizo y se usó: la época (cuándo), la procedencia (dónde y en qué comunidad) y la función (para qué: bailar, trabajar en grupo, escuchar en sala, acompañar una celebración). Conocer el contexto ayuda a entender por qué los elementos de la obra son como son: una obra para bailar suele tener un ritmo regular y claro; una canción para acompañar una tarea compartida suele repetir un patrón.",
        "Relacionar contexto y elementos exige cuidado. Se dice «el ritmo regular de 3 pulsos se relaciona con su función de baile», pero no se inventan datos que la ficha no entrega. Tampoco se dice que una obra es «mejor» o «más avanzada» por ser de otra época o lugar: cada obra responde a sus circunstancias. Para pueblos y comunidades específicas, los datos y su sentido los aporta la persona que enseña esa tradición o tu docente.",
        "Comparar dos obras con evidencia significa elegir un criterio (por ejemplo, la función) y decir qué comparten y en qué se diferencian, citando un dato de cada una. Una comparación útil termina con una conclusión: «ambas repiten patrones, pero la obra 1 sirve al baile y la obra 2 a una tarea compartida». Todo se puede escribir en una tabla simple de dos columnas.",
    ],
    vocab=[("contexto", "circunstancias en que se hizo y se usó una obra"), ("procedencia", "lugar y comunidad de donde viene una obra"), ("función", "para qué se usaba o se usa una obra"),
           ("tradición oral", "música que se transmite de persona en persona sin partitura"), ("criterio de comparación", "aspecto elegido para comparar dos obras"), ("juicio de valor", "afirmación de que algo es mejor o peor que otra cosa")],
    worked=[
        ("Relacionar función y elemento", "Una obra de ejemplo, hecha para acompañar una procesión lenta, mantiene un pulso de 50 por minuto. ¿Qué relación hay entre su función y su pulso?",
         ["La función es acompañar un desplazamiento lento: pide un pulso estable y calmo.", "El pulso lento de 50 coincide con esa función."],
         "El pulso lento y estable se relaciona con acompañar un desplazamiento lento"),
        ("Evitar un juicio de valor", "Un comentario dice: «la canción de tradición oral es menos avanzada que la pieza electrónica». ¿Qué falla?",
         ["Dice que una es «menos avanzada», que es un juicio de valor sin criterio.", "Cada obra responde a su contexto y su función; no se comparan como mejor o peor."],
         "Pone una obra por debajo de otra sin criterio ni evidencia"),
    ],
    mistakes=[("Decir que una obra antigua es «peor» que una reciente.", "Se valora por la época y no por la obra.", "Compara con un criterio, como la función, y cita datos de cada obra."),
              ("Inventar datos de contexto que no se dieron.", "Se afirma algo sin fuente.", "Usa solo los datos de la ficha o los que aporte tu docente con su fuente.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es la función de una obra?', 'Para qué se usaba o se usa, como bailar o trabajar en grupo', 'La cantidad de instrumentos que participan en su interpretación', 'El año exacto en que fue escrita en una partitura', 'La función responde para qué sirve la obra; no es una cantidad ni una fecha.'),
        ('abc', '{F} ¿Cuál es la función de la obra 2?', 'Acompañar tareas compartidas, cantada en grupo', 'Acompañar un baile de salón de una ciudad y su gente', 'Escucharse en un estudio con audífonos o en una sala', 'La ficha dice que se cantaba durante tareas compartidas.'),
        ('abc', '{F} ¿Qué dato de procedencia tiene la obra 1?', 'Es de ciudad y se tocaba en salones', 'Es de una zona rural y de tradición oral', 'Se hizo en un estudio y es reciente', 'La obra 1 es de ciudad, según la ficha.'),
        ('abc', '{F} ¿Qué obra se hizo en un estudio?', 'La obra 3, «Paisaje de pulsos»', 'La obra 1, «Danza de salón»', 'La obra 2, «Canción de faena»', 'Solo la obra 3 indica que fue hecha en un estudio.'),
        ('abc', '{F} ¿Qué elemento de la obra 1 se relaciona con su función de baile?', 'El ritmo regular en compases de 3 pulsos', 'El loop de 4 pulsos y los timbres que cambian', 'La voz solista con un coro que responde', 'Un ritmo regular y claro facilita bailar, y es un elemento de la obra 1.'),
        ('abc', '{F} ¿Qué elemento de la obra 2 se relaciona con su función de tarea compartida?', 'El ritmo constante y repetido, y la pregunta y respuesta con el coro', 'Los acordes del piano y el violín que canta la melodía de la pieza', 'El crescendo largo y los sonidos sintetizados de estudio', 'Un patrón constante y repetido y la participación del coro se relacionan con trabajar en grupo.'),
        ('=', '{F} En la obra 2, un intercambio de pregunta y respuesta dura 8 pulsos a 100 pulsos por minuto. ¿Cuántos segundos duran 5 intercambios?', '5*8*60//100', 'Se multiplican los intercambios por 8 pulsos y se pasa a segundos con el tempo.', ' s'),
        ('=', '{F} Una frase de la obra 1 dura 4 compases de 3 pulsos a 90 pulsos por minuto. ¿Cuántos segundos duran 3 frases seguidas?', '3*4*3*60//90', 'Se multiplican las frases por los compases y por los pulsos, y se pasa a segundos.', ' s'),
        ('abc', '{F} Un comentario dice que la obra 3 «es más avanzada» que la obra 2 por ser reciente. ¿Qué observación corresponde?', 'Es un juicio de valor sin criterio; cada obra responde a su contexto', 'Es correcto, porque las obras recientes siempre son superiores a las tradicionales', 'Es incorrecto, porque las obras antiguas siempre son superiores a las recientes', 'Un juicio de valor basado solo en la época no es un análisis.'),
        ('abc', '{F} ¿Qué comparación entre las obras 1 y 2 usa un criterio y datos?', 'Ambas repiten patrones, pero la 1 sirve al baile y la 2 a una tarea compartida', 'La obra 1 es más elegante porque pertenece a una época pasada y a una ciudad', 'La obra 2 es más auténtica porque no usa partituras ni acordes de piano', 'La comparación usa un criterio (la función) y datos de cada ficha.'),
        ('abc', '{F} Una estudiante afirma que la obra 2 «se cantaba en una fiesta de una comunidad específica y para un rito». ¿Qué respuesta es correcta?', 'La ficha no entrega ese dato; hay que consultar a quien enseña esa tradición', 'Es correcto, porque todas las canciones rurales se usan en ritos de comunidades', 'Es correcto, porque la ficha dice que se cantaba en una fiesta de la comunidad', 'No se inventan datos de contexto ni de ritos; los aporta la persona que enseña la tradición.'),
        ('abc', '{F} Se compara la función de las obras 1 y 3. ¿Cuál afirmación se apoya en la ficha?', 'La obra 1 se tocaba para bailar y la obra 3 se escucha en sala o con audífonos', 'Las dos se tocaban para bailar en salones de la ciudad, con piano', 'Las dos se cantaban durante tareas compartidas del campo, con coro', 'La ficha asigna a cada obra una función distinta.'),
        ('=', '{F} A 90 pulsos por minuto, ¿cuántos compases de 3 pulsos de la obra 1 caben en 12 segundos?', '12*90//60//3', 'En 12 segundos suenan 18 pulsos a ese tempo, y se agrupan de a 3 pulsos.', ' compases'),
    ],
    ctx=('abc', 'Tu docente trae una grabación de una canción de una comunidad que no conoces y te pide analizarla. ¿Qué decisión respeta a la comunidad y al análisis?', 'Describir los elementos y consultar a tu docente sobre el sentido y la procedencia', 'Decidir tú sola qué significa la canción para la comunidad y su gente', 'Escribir que la canción es menos desarrollada que otras obras del programa', 'Se analiza lo que se oye y se consulta el contexto a quien lo conoce.'),
    sc=[
        ("En Interpretación musical: ¿qué es la procedencia de una obra?", "El lugar y la comunidad de donde viene", "La procedencia es parte del contexto de la obra."),
        ('abc', 'Un juicio de valor sobre una tradición:', 'No es un análisis, porque no usa un criterio', 'Siempre es un análisis válido si lo dice una persona con experiencia', 'Es lo más importante del análisis de una obra y de su contexto', 'Un análisis compara con criterio y evidencia.'),
        ("¿Quién aporta los datos de contexto de una tradición de un pueblo originario?", "La persona que enseña esa tradición o tu docente, con su fuente", "No se inventan datos sobre una tradición."),
    ],
    op=("Con la {F}, compara dos obras con un criterio a tu elección (función, procedencia o ritmo). Escribe una frase con un dato de cada una, una relación entre el contexto y un elemento, y una conclusión sin juicios de valor.",
        "Criterio: la función. Obra 1: se tocaba para bailar en salones. Obra 2: se cantaba en tareas compartidas. Relación: el ritmo regular de 3 pulsos de la obra 1 se relaciona con el baile. Conclusión: ambas repiten patrones, pero cada una responde a una función distinta.",
        ["elige un criterio de comparación", "cita un dato de cada obra", "relaciona contexto y elemento", "no hace juicios de valor"],
        ["hoja con el criterio, los datos, la relación y la conclusión"],
        ["decir que una obra es mejor", "no citar datos de la ficha", "inventar un dato de contexto"],
        "Pregunta: «¿qué dato de la ficha sostiene eso?». Si no hay ninguno, pídele que lo quite."),
    reinforce="Escribe una tabla de dos obras inventadas con época, procedencia y función, y una frase que relacione la función con un elemento.",
    extend="Explica por qué la misma obra puede cambiar de función cuando se toca en otro contexto, y qué análisis cambiarías.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (borrador de análisis y pauta, de ejemplo, inventados). Obra «Paisaje de pulsos»: sonidos grabados y sintetizados; 120 pulsos por minuto; patrón de 4 pulsos repetido (loop); timbres que cambian poco a poco; crescendo largo; pieza electrónica reciente, hecha en un estudio, para escuchar en sala o con audífonos. "
     "Borrador de Ana: (1) «Es una obra muy bonita». (2) «El patrón de 4 pulsos se repite y los timbres cambian poco a poco, lo que produce insistencia con variación». (3) «Se hizo en un estudio, y la edición permite repetir el patrón sin cansar a nadie». (4) «Es mejor que las canciones tradicionales porque es más moderna». "
     "Pauta: A, nombra elementos del lenguaje musical con evidencia; B, nombra un recurso de producción; C, incluye un dato de contexto; D, relaciona los elementos con un efecto estético; E, evita juicios de valor sobre épocas o tradiciones.")
build(
    O4, 5, F,
    use="Aprenderé a registrar y ajustar un análisis estético escrito: estructurarlo en cuatro partes, revisarlo con una pauta de cinco criterios y corregir lo que falta, sin juicios de valor.",
    prior=["Sé describir elementos y recursos de una obra.", "Sé relacionar contexto y elementos.", "Sé evitar juicios de valor."],
    explain=[
        "Un análisis estético escrito tiene cuatro partes. Primero, la descripción: elementos del lenguaje musical con su evidencia. Segundo, los recursos de producción o técnicas que se usan. Tercero, el contexto: época, procedencia y función, con datos entregados. Cuarto, la relación: cómo los elementos y recursos producen un efecto estético. Una quinta cosa es transversal: no hay juicios de valor sobre épocas o tradiciones.",
        "Para revisar un borrador se usa una pauta de criterios, como la de la ficha. Cada criterio se marca como «cumple» o «falta», con una evidencia: la frase del borrador que lo cumple o la frase que falta. Una frase que mezcla un dato con un juicio de valor se corrige quitando el juicio y dejando el dato. Un borrador mejora cuando se cambia un elemento por revisión y se vuelve a pasar la pauta.",
        "Registrar los ajustes ayuda a aprender de ellos. Se anota qué criterio faltaba, qué frase se cambió y por qué. Con este método se pueden analizar obras de cualquier época y procedencia, siempre con datos entregados o aportados por tu docente. Si el análisis se hace escuchando música, se cuida el volumen y se descansa entre audiciones.",
    ],
    vocab=[("borrador", "primera versión de un texto, que se revisa y mejora"), ("pauta", "lista de criterios para revisar un texto"), ("criterio", "aspecto que se evalúa, como incluir un dato de contexto"),
           ("ajuste", "cambio de un solo elemento para cumplir un criterio"), ("efecto estético", "sensación o impresión que produce una obra"), ("juicio de valor", "afirmación de que algo es mejor o peor, sin criterio")],
    worked=[
        ("Marcar un criterio", "Un borrador de ejemplo dice: «El patrón de 4 pulsos se repite». ¿Cumple el criterio «nombra elementos del lenguaje musical con evidencia»?",
         ["Nombra un elemento (el ritmo, con un patrón de 4 pulsos) y cita un dato (se repite).", "Cumple el criterio."],
         "Cumple"),
        ("Corregir una frase", "Una frase de ejemplo dice: «Es mejor que las tradicionales porque es moderna». ¿Cómo se corrige para cumplir el criterio sin juicios de valor?",
         ["Se quita la comparación de valor y se deja un dato comprobable.", "Una versión corregida: «Es de una época reciente y usa una producción en estudio»."],
         "«Es de una época reciente y usa una producción en estudio»"),
    ],
    mistakes=[("Corregir todo el borrador a la vez y no anotar qué se cambió.", "No se sabe qué ajuste cumplió cada criterio.", "Cambia un elemento por revisión y anótalo."),
              ("Dejar una frase con juicio de valor porque «es una opinión del autor».", "Un análisis estético no pone obras por encima de otras sin criterio.", "Reemplaza el juicio por un dato o por una comparación con criterio.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un efecto estético?', 'La sensación o impresión que produce una obra', 'El volumen que se usa en una sala de conciertos', 'La cantidad de instrumentos que tiene un conjunto', 'El efecto estético se refiere a lo que produce la obra; no es volumen ni instrumentos.'),
        ('abc', '{F} ¿Qué frase del borrador de Ana es un juicio de valor?', 'La frase 4, que dice que es mejor que las canciones tradicionales', 'La frase 2, que describe el patrón y los timbres de la obra', 'La frase 3, que cita el estudio y la edición del patrón', 'Solo la frase 4 pone una obra por encima de otras sin criterio.'),
        ('abc', '{F} ¿Qué criterio cumple la frase 2 del borrador?', 'El A: nombra elementos del lenguaje musical con evidencia', 'El C: incluye un dato de contexto de la obra en estudio', 'El E: evita juicios de valor sobre las épocas de las obras', 'La frase 2 nombra patrón repetido y timbres cambiantes con datos de la ficha.'),
        ('abc', '{F} ¿Qué criterio cumple la frase 3?', 'El B, porque nombra la edición, y el C, porque cita el estudio', 'El A, porque nombra el tempo de la obra y su duración', 'El D, porque relaciona un elemento con un efecto estético', 'La frase 3 cita la edición (recurso) y el estudio (contexto).'),
        ('abc', '{F} La frase 1 dice «es una obra muy bonita». ¿Qué criterio incumple?', 'El A, porque no nombra ningún elemento ni evidencia', 'El B, porque no menciona ningún recurso de producción', 'El E, porque compara épocas sin criterio', 'La frase solo expresa una opinión: no nombra elementos con evidencia.'),
        ('abc', '{F} Al pasar la pauta por el borrador de Ana, ¿cuántos criterios cumple y cuál falla?', 'Cumple cuatro (A, B, C y D) y falla el E por la frase 4', 'Cumple los cinco, porque la frase 4 es solo una opinión sin importancia', 'Cumple solo el A, porque las demás frases no citan datos de la obra', 'Las frases 2 y 3 cumplen de A a D; la frase 4 es un juicio de valor, así que falla E.'),
        ('abc', '{F} Ana escribe: «Esta obra es superior a una pieza de piano y violín porque usa sonidos sintetizados». ¿Cómo se corrige sin juicio de valor?', 'Usa sonidos grabados y sintetizados, a diferencia de una pieza de piano y violín', 'Es superior porque los sonidos sintetizados son más modernos y complejos', 'Es más avanzada que cualquier pieza acústica porque usa un estudio', 'Una frase sin juicio de valor deja solo datos comprobables de la obra.'),
        ('=', '{F} El patrón de 4 pulsos del loop se repite 6 veces. ¿Cuántos segundos dura a 120 pulsos por minuto?', '6*4*60//120', 'Se multiplican las repeticiones por los 4 pulsos y se pasa a segundos con el tempo.', ' s'),
        ('abc', '{F} ¿Qué criterio faltaría si el borrador no dijera nada del lugar ni de la función de la obra?', 'El C, dato de contexto', 'El B, recurso de producción', 'El A, elementos del lenguaje', 'El contexto incluye procedencia y función; si no aparecen, falta el criterio C.'),
        ('abc', '{F} Ana quiere cambiar tres frases del borrador a la vez. ¿Qué observación es correcta?', 'Conviene cambiar un elemento por revisión y anotarlo, para saber qué lo mejora', 'Conviene cambiarlas todas a la vez, porque así queda mejor', 'No conviene revisar un borrador antes de entregarlo al curso', 'Un ajuste por revisión permite saber cuál cumplió cada criterio.'),
        ('abc', '{F} Ana agrega: «El crescendo largo y el loop producen insistencia que crece». ¿Qué criterio cumple esa frase?', 'El D, porque relaciona elementos con un efecto', 'El C, porque cita el contexto de la obra y su función', 'El B, porque nombra el micrófono usado en el estudio', 'La frase vincula crescendo y loop con un efecto estético.'),
        ('abc', 'Un estudiante dice «mi borrador está listo porque lo escribí con cuidado». ¿Qué falla en esa conclusión?', 'No lo pasó por la pauta ni anotó qué criterios cumple', 'Escribió demasiadas frases para ser un análisis breve', 'No escribió el nombre de la obra en el título del texto', 'Un borrador se revisa con la pauta y se anota el resultado.'),
        ('=', '{F} Ana agrega un patrón de 2 pulsos que se repite 10 veces a 120 pulsos por minuto. ¿Cuántos segundos dura esa repetición?', '10*2*60//120', 'Se multiplican las repeticiones por los 2 pulsos y se pasa a segundos con el tempo.', ' s'),
    ],
    ctx=('abc', 'Debes entregar un análisis breve de una pieza y revisarlo antes. ¿Qué estrategia conviene?', 'Pasar la pauta, marcar «cumple» o «falta» y corregir un elemento por vez', 'Entregarlo sin releer, porque ya lo escribiste con mucho cuidado', 'Agregar frases largas sin datos para que el texto parezca completo', 'La revisión con pauta y ajustes de a uno mejora el texto de manera controlada.'),
    sc=[
        ("En Interpretación musical: ¿qué es un borrador?", "La primera versión de un texto, que se revisa y mejora", "El borrador se corrige con una pauta."),
        ('abc', 'Para corregir un juicio de valor se:', 'Reemplaza por un dato comprobable', 'Repite el juicio con otras palabras', 'Agrega otro juicio igual al anterior', 'El juicio de valor se cambia por una observación con evidencia.'),
        ("¿Por qué se anota cada ajuste que se hace al borrador?", "Para saber qué cambio cumplió cada criterio", "El registro permite aprender de lo que funcionó."),
    ],
    op=("Con la {F}, revisa el borrador de Ana con los cinco criterios (A a E), marca «cumple» o «falta» con la frase que lo respalda, y reescribe la frase 1 para que cumpla un criterio. Escribe qué ajuste hiciste y por qué.",
        "A cumple (frase 2). B cumple (frase 3, edición). C cumple (frase 3, estudio). D cumple: la frase 2 relaciona patrón y timbres con insistencia. E falta: la frase 4 es un juicio de valor. Reescribo la frase 1: «El patrón de 4 pulsos se repite a 120 pulsos por minuto». Ajuste: cambié una opinión por un dato, para cumplir A.",
        ["revisa los cinco criterios con evidencia", "reescribe la frase 1 con un dato", "anota un ajuste y su razón", "no agrega juicios de valor"],
        ["hoja con la pauta marcada y la frase reescrita"],
        ["marcar criterios sin evidencia", "reescribir con otro juicio de valor", "no anotar el ajuste"],
        "Pregunta: «¿qué frase respalda ese criterio?». Si no la encuentra, pídele que la subraye."),
    reinforce="Escribe un análisis de cuatro frases de una pieza inventada y revísalo con una pauta de tres criterios.",
    extend="Explica cómo cambiaría tu pauta si el análisis fuera de una obra de tradición oral de una comunidad específica.",
)

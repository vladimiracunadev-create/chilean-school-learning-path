"""Student material for 6.º básico Música, OA 06 (presentar el trabajo musical al curso y a la comunidad, en forma individual y grupal, con responsabilidad, dominio y musicalidad).

Todos los planes, programas y obras de los ejercicios son inventados para esta clase. Toda presentación es voluntaria en su formato: se puede presentar en grupo pequeño, con un rol de apoyo o grabada con permiso, sin forzar la exposición de nadie.
"""
from __future__ import annotations

from student_content_mu6_a import L, N
from student_lessons import arith, ex

OA6 = "MU06 OA 06"

# ---------------------------------------------------------------- OA 06 · clase 1 (preparar con responsabilidad)
L(
    OA6, 1,
    "Lápiz y papel. Todos los planes están escritos en los ejercicios. Puedes preparar tu presentación con tu voz, palmas o los instrumentos del colegio. Cuida el volumen.",
    "Aprenderé a preparar una presentación musical con responsabilidad: elegir la obra, repartir roles, planear los ensayos y cuidar los materiales. Sirve para llegar a la presentación con todo listo y sin sorpresas.",
    ["Sé cantar o tocar una pieza breve.", "Sé sumar y multiplicar para planear el tiempo.", "Sé trabajar en grupo con respeto."],
    [
        "Presentar con responsabilidad significa cumplir con lo que te comprometiste para que el grupo pueda mostrar su trabajo. Antes de ensayar se decide qué se va a presentar, quién tiene cada rol y qué se necesita: instrumentos, partitura o letra, un lugar y el tiempo disponible. Un rol puede ser tocar, cantar, dirigir con la mano, cuidar los instrumentos o presentar la obra al público.",
        "Luego se hace un plan de ensayos con fechas, duración y qué se practica en cada uno. Por ejemplo, 3 ensayos por semana de 20 minutos durante 2 semanas son 6 ensayos y 120 minutos. Lo mejor es dejar un día libre antes de la presentación para descansar y revisar los materiales. Si no puedes asistir a un ensayo, avisas con tiempo y practicas por tu cuenta.",
        "También hay responsabilidad con el cuidado: los instrumentos se guardan donde corresponde, se mantiene un volumen seguro, se respeta el turno de cada compañero y no se obliga a nadie a exponerse. Quien no quiere tocar frente al público puede tener otro rol: presentar, dirigir, cuidar el material o acompañar. Lo que importa es que todos aporten y que el grupo sepa en quién puede confiar.",
    ],
    [("responsabilidad", "cumplir lo que te comprometiste con el grupo"), ("rol", "tarea que tiene cada persona en una presentación"), ("plan de ensayos", "calendario de prácticas con duración y objetivo"), ("compromiso", "promesa de hacer una tarea a tiempo"), ("material", "instrumentos, partituras o letras que se necesitan")],
    [
        ("Calcular los ensayos", "Un grupo ensaya 3 veces por semana durante 2 semanas, 20 minutos cada vez. ¿Cuántos minutos ensaya en total?", ["Ensayos: 3 × 2 = 6.", "Minutos: 6 × 20 = 120."], "120 minutos"),
        ("Resolver un imprevisto", "El lunes un grupo se da cuenta de que falta un instrumento para el viernes. ¿Qué es más responsable: avisar al grupo y buscar una solución o esperar al viernes?", ["Avisar da tiempo a encontrar solución.", "Esperar puede dejar al grupo sin su instrumento."], "Avisar al grupo y buscar una solución"),
    ],
    [
        ("Dejar todo para el día antes.", "Sin tiempo para ensayar, aumentan los errores y el estrés.", "Haz un plan de ensayos con fechas."),
        ("Faltar al ensayo sin avisar.", "El grupo no puede ensayar su parte sin ti y pierde tiempo.", "Avisa con tiempo y practica por tu cuenta."),
    ],
    [
        ex("¿Qué debes hacer si no puedes ir a un ensayo: avisar con tiempo o no decir nada?", "Avisar con tiempo", "El grupo puede reorganizarse."),
        ex("Una persona no quiere tocar frente al público. ¿Se le obliga o se le propone otro rol?", "Se le propone otro rol", "Nadie debe ser obligado a exponerse."),
        ex("¿Dónde se guardan los instrumentos después del ensayo: en su lugar o en cualquier parte?", "En su lugar", "Cuidar el material es parte de la responsabilidad."),
    ],
    [
        ex("Un grupo tiene estos roles: Ana canta, Beto toca el metalófono, Carla dirige, Dani cuida los instrumentos y Eli presenta la obra. ¿Cuántas personas tienen un rol de apoyo (que no es cantar ni tocar)?", "3", "Carla, Dani y Eli."),
        ex("¿Qué debe incluir un plan de ensayos: fechas y duración o solo el nombre de la obra?", "Fechas y duración", "El plan se organiza en el tiempo."),
        ex("Si un grupo deja un día libre antes de la presentación, ¿para qué sirve: para descansar y revisar los materiales o para olvidar la obra?", "Para descansar y revisar los materiales", "Así llegan con todo listo."),
    ],
    [
        arith("Un curso ensaya 4 veces por semana durante 3 semanas, 15 minutos cada vez. ¿Cuántos minutos ensaya?", "4*3*15", "Se calculan primero los ensayos y luego los minutos.", " minutos"),
        arith("Quedan 14 días para la presentación y ensayan un día sí y un día no, empezando hoy. ¿Cuántos ensayos hacen?", "14//2", "Cada dos días hay un ensayo; en 14 días son 7.", " ensayos"),
        ex("Para la presentación necesitan 3 flautas, 2 metalófonos y 4 panderos, y el colegio tiene 5 flautas, 1 metalófono y 6 panderos. ¿Qué instrumento falta y cuántos?", "Falta 1 metalófono", "Necesitan 2 metalófonos y hay 1."),
    ],
    [
        ex("Tomás dice que cumplir el compromiso es llegar el día de la presentación. ¿Qué otra cosa incluye?", "Asistir a los ensayos y practicar su parte", "La responsabilidad comienza antes de la presentación."),
        ex("Un grupo reparte la tarea de llevar un instrumento a una persona que no avisó que lo haría. ¿Qué falló: el compromiso o el instrumento?", "El compromiso", "Nadie se comprometió con esa tarea."),
    ],
    [
        arith("Un grupo planea 6 ensayos de 25 minutos cada uno, y 1 ensayo general de 40 minutos. ¿Cuántos minutos son en total?", "6*25+40", "Se calcula el tiempo de los 6 ensayos y se suma el general.", " minutos"),
        arith("Si el plan tiene 150 minutos en 5 semanas con la misma cantidad por semana, ¿cuántos minutos ensayan cada semana?", "150//5", "Se reparte el tiempo en las semanas.", " minutos"),
    ],
    [ex("El día antes de presentar, una integrante del grupo se enferma y no podrá tocar. ¿Qué es más responsable: avisar de inmediato y reorganizar los roles o esperar a que se mejore?", "Avisar de inmediato y reorganizar los roles", "Así el grupo se prepara a tiempo.")],
    [ex("En Música: ¿Qué es un rol?", "Una tarea que tiene cada persona en la presentación", "Puede ser tocar, cantar, dirigir o apoyar."), ex("¿Qué se hace si no puedes ensayar un día?", "Avisar y practicar por tu cuenta", "Se cuida al grupo."), ex("¿Se obliga a alguien a exponerse?", "No", "Se propone otro rol.")],
    (
        "Prepara el plan de una presentación de tu grupo (o imagina un grupo de 5 personas). Elige una de estas obras para presentar: A) una ronda de 8 compases, B) un ritmo de percusión de 8 compases o C) una melodía con acompañamiento de 8 compases. Escribe: la obra elegida, 5 roles con una persona por rol, un plan de 6 ensayos con fecha y duración, y los materiales que necesitan. Calcula cuántos minutos ensayarán en total.",
        "Obra A, ronda de 8 compases. Roles: Ana canta, Beto canta, Carla dirige, Dani cuida el material, Eli presenta. Plan: 6 ensayos de 20 minutos (lunes, miércoles y viernes durante 2 semanas). Materiales: letra escrita y una mesa. Total: 6 × 20 = 120 minutos.",
        ["elige una obra y asigna roles", "arma un plan con fechas y duración", "calcula bien el tiempo"],
        ["plan escrito"],
        ["no incluir un plan de fechas", "no incluir roles de apoyo"],
        "Reconoce el plan y pide mostrar con el dedo cuándo se ensaya cada parte.",
    ),
    "Anota qué roles de apoyo podrías cumplir en una presentación de tu curso.",
    "Escribe una lista de verificación con cinco materiales que revisarías antes de presentar.",
)

# ---------------------------------------------------------------- OA 06 · clase 2 (dominio: ensayar con método)
L(
    OA6, 2,
    "Lápiz y papel; tu voz, palmas o un instrumento. Para practicar puedes marcar el pulso con palmas suaves. Cuida el volumen y descansa los oídos y la voz entre repeticiones.",
    "Aprenderé un método para ensayar y lograr dominio de mi parte: dividir en secciones, practicar lento, subir el tempo de a poco y juntar todo. Sirve para tocar o cantar con seguridad y pocos errores.",
    ["Sé que el tempo se mide en pulsos por minuto.", "Sé que una obra se divide en secciones.", "Sé calcular cuánto dura una pieza."],
    [
        "Dominar una obra es poder tocarla o cantarla con seguridad, a tiempo y sin detenerse. Para lograrlo no sirve repetir todo desde el comienzo cada vez. Un buen método tiene pasos: 1) escuchar o leer la obra completa; 2) dividirla en secciones de 4 compases; 3) practicar cada sección lento con pulso estable; 4) subir el tempo de a escalones; 5) juntar las secciones; 6) tocar la obra entera y revisar.",
        "Los escalones de tempo ayudan a no apurarse: por ejemplo, 60, 72, 84 y 96 pulsos por minuto. Solo se sube al siguiente cuando la sección sale 3 veces seguidas sin error. Si hay un error en un compás, se practica solo ese compás y los vecinos, lento, hasta que salga; luego se vuelve a la sección completa. Repetir un error rápido solo lo vuelve costumbre.",
        "El dominio también incluye cuidar el cuerpo y el oído: se descansa entre repeticiones, se mantiene una postura cómoda y se evita el volumen alto. Al final de cada práctica se anota qué quedó seguro y qué se trabajará la próxima vez. Así se ve el progreso y se evita estudiar al azar.",
    ],
    [("dominio", "seguridad para tocar o cantar a tiempo y sin detenerse"), ("sección", "parte de la obra que se practica por separado"), ("escalón de tempo", "tempo fijo al que se sube de a poco"), ("método de ensayo", "pasos ordenados para practicar bien"), ("registro de práctica", "anotación de lo logrado y lo pendiente")],
    [
        ("Contar secciones", "Una obra de 16 compases se divide en secciones de 4 compases. ¿Cuántas secciones tiene?", ["La obra tiene 16 compases.", "Cada sección tiene 4 compases, así que divido: 16 ÷ 4 = 4."], "4 secciones"),
        ("Contar escalones", "Subes el tempo desde 60 hasta 96 pulsos por minuto en escalones de 12. ¿Cuántos tempos practicarás, contando el primero y el último?", ["Escribo los tempos: 60, 72, 84 y 96.", "Los cuento, incluyendo el primero y el último: son 4."], "4 tempos"),
    ],
    [
        ("Repetir toda la obra desde el principio cada vez que se falla.", "Así se gasta tiempo en lo que ya sale bien.", "Practica solo el compás con error y sus vecinos."),
        ("Practicar rápido para terminar antes.", "Repetir rápido fija los errores.", "Practica lento y sube el tempo de a poco."),
    ],
    [
        ex("Para practicar un compás difícil, ¿conviene hacerlo lento o rápido?", "Lento", "Lento permite corregir antes de fijar el error."),
        ex("¿Cuántas veces seguidas sin error debe salir una sección antes de subir el tempo en el método de la clase?", "3", "El método usa tres veces seguidas sin error."),
        ex("¿Qué se anota al final de la práctica?", "Qué quedó seguro y qué se trabajará la próxima vez", "Eso es el registro de práctica."),
    ],
    [
        ex("Tienes un error en el compás 6 de una obra de 12 compases. ¿Qué practicas: solo los compases 5 a 7 lento o la obra entera rápido?", "Solo los compases 5 a 7 lento", "Se aísla el error y sus vecinos."),
        ex("Tu sección sale perfecta 3 veces seguidas a 72 pulsos por minuto. ¿Qué haces ahora?", "Subir al siguiente escalón de tempo, 84", "Cumpliste la condición de tres veces seguidas."),
        ex("¿Cuál es el paso 5 del método de la clase: juntar las secciones o dividir en secciones?", "Juntar las secciones", "Dividir es el paso 2."),
    ],
    [
        arith("Una sección de 4 compases de 4 pulsos va a 60 pulsos por minuto. ¿Cuántos segundos dura una vuelta?", "4*4*60//60", "Son 16 pulsos y cada pulso dura 1 segundo.", " segundos"),
        arith("Cada sección debe salir 3 veces seguidas sin error. Si cada vuelta dura 16 segundos, ¿cuántos segundos son 3 vueltas?", "3*16", "Se multiplican las vueltas por la duración de cada una.", " segundos"),
        arith("Una obra tiene 5 secciones y practicas cada una en 4 escalones de tempo. ¿Cuántas combinaciones sección-tempo practicas?", "5*4", "Cada sección se practica en cada escalón.", " combinaciones"),
    ],
    [
        ex("Pedro practica una obra rápida desde el principio hasta equivocarse y empieza de nuevo. Después de 20 minutos sigue equivocándose en el mismo compás. ¿Qué cambiarías: practicar solo ese compás lento o repetir más rápido?", "Practicar solo ese compás lento", "Repetir rápido fija el error."),
        ex("Una práctica dice: «Hoy repetí 10 veces la obra completa». Otra dice: «Hoy practiqué el compás 6, lento, 5 veces y logré 3 sin error». ¿Cuál registra mejor el progreso?", "La segunda", "Dice qué compás, cómo y qué logró."),
    ],
    [
        arith("Una obra de 12 compases de 3 pulsos va a 90 pulsos por minuto. ¿Cuántos segundos dura entera?", "12*3*60//90", "Son 36 pulsos y cada pulso dura dos tercios de segundo.", " segundos"),
        ex("Un escalón de tempo es 60, 72, 84, 96. ¿Cuántos pulsos por minuto se suben en cada escalón?", "12", "72 − 60 = 12, y la diferencia se repite."),
    ],
    [arith("Tu grupo tiene 20 minutos de ensayo. Dedican 5 minutos a calentar y 10 a trabajar un compás difícil, lento. El resto lo usan para tocar la obra entera. ¿Cuántos minutos dedican a tocar la obra entera?", "20-5-10", "Se restan del tiempo total el calentamiento y el trabajo del compás difícil.", " minutos")],
    [ex("¿Cuál es el primer paso del método?", "Escuchar o leer la obra completa", "Primero se conoce la obra."), ex("¿Qué se hace con un compás difícil?", "Practicarlo lento con sus vecinos", "Así se corrige antes de fijarlo."), ex("¿Para qué sirve el registro de práctica?", "Para ver el progreso y planear lo siguiente", "Anota lo logrado y lo pendiente.")],
    (
        "Aplica el método a esta obra inventada de 12 compases en 4/4: compases 1 a 4 (sección A), 5 a 8 (sección B), 9 a 12 (sección C). Tu plan: escoge una sección, practica con palmas o con la voz a 60 pulsos por minuto, luego a 72 y a 84. Anota en un registro: qué sección practicaste, a qué tempos, cuántas veces salió sin error y qué practicarás la próxima vez. Calcula cuántos segundos dura una vuelta de la obra entera a 72 pulsos por minuto.",
        "Practiqué la sección B a 60, 72 y 84; salió 3 veces seguidas sin error a 60 y a 72, pero a 84 fallé en el compás 7. Próxima vez: compases 6 a 8 lento. Una vuelta entera a 72: 12 compases × 4 pulsos = 48 pulsos; 48 × 60 ÷ 72 = 40 segundos.",
        ["divide en secciones y practica lento", "registra tempos y resultados", "calcula bien la duración"],
        ["registro escrito", "práctica realizada"],
        ["subir el tempo sin lograr tres veces seguidas", "repetir toda la obra rápido"],
        "Reconoce el registro y pide mostrar el compás difícil practicado lento.",
    ),
    "Divide una canción que conoces en secciones de 4 compases.",
    "Escribe tu propio método de seis pasos para ensayar una obra y compáralo con el de la clase.",
)

# ---------------------------------------------------------------- OA 06 · clase 3 (musicalidad)
MU3 = "musicalidad: pulso estable; dinámica y tempo coherentes con el propósito; frases con principio y final claros; atención y concentración durante la obra"

L(
    OA6, 3,
    f"Lápiz y papel; tu voz o un instrumento. Criterios de musicalidad de la clase: {MU3}. Cuida el volumen.",
    "Aprenderé qué es la musicalidad y cómo mostrarla al presentar: tocar o cantar con expresión, cuidando el pulso, la dinámica, las frases y el propósito. Sirve para que la obra no solo salga correcta sino que comunique algo.",
    ["Sé qué son la dinámica, el tempo y el propósito expresivo.", "Sé qué es una frase musical.", "Sé mantener un pulso estable."],
    [
        f"La musicalidad es la capacidad de dar vida a una obra al interpretarla. No basta con tocar las notas correctas: hay que expresar. En la clase usamos estos criterios: {MU3}. Cada criterio se puede observar y mejorar.",
        "Por ejemplo, si una obra es una canción de cuna, la musicalidad pide dinámica suave, tempo lento y frases que terminen con calma. Si es una marcha, pide pulso firme, dinámica fuerte y un final claro. Cada frase se toca como una oración: tiene comienzo, un punto más importante y un final; por eso, en el final de la frase se respira o se baja un poco el volumen.",
        "También se muestra musicalidad con la actitud: mirar al grupo, entrar a tiempo, concentrarse y terminar quieto, sin hacer gestos de vergüenza. Si te equivocas, sigues con el pulso y no te detienes. Para revisar tu musicalidad se pide a otra persona que marque cuántos criterios viste cumplidos, o se graba la práctica con permiso para escucharla después.",
    ],
    [("musicalidad", "interpretar con expresión, no solo con notas correctas"), ("fraseo", "dar a cada frase comienzo, punto importante y final"), ("coherencia", "que los recursos coincidan con el propósito"), ("concentración", "atención completa a lo que se interpreta"), ("final claro", "terminar la obra con una señal que se note")],
    [
        ("Decidir los recursos", "Para una canción de cuna, ¿qué recursos son más coherentes: dinámica suave y tempo lento o dinámica fuerte y tempo rápido?", ["Una cuna busca calma.", "Calma = suave y lento."], "Dinámica suave y tempo lento"),
        ("Contar criterios", "Una intérprete mantiene un pulso estable, usa dinámica coherente y termina con un final claro, pero se distrae a la mitad. ¿Cuántos de los 4 criterios cumple?", ["Pulso estable: sí.", "Dinámica coherente: sí.", "Frases con final claro: sí.", "Atención durante la obra: no."], "3 criterios"),
    ],
    [
        ("Pensar que tocar sin errores ya es tener musicalidad.", "La musicalidad también necesita expresión coherente con el propósito.", "Pregunta qué quiere decir la obra y cómo lo muestras."),
        ("Detenerse cuando hay un error.", "Detenerse rompe el pulso; seguir mantiene la obra.", "Sigue con el pulso y vuelve a entrar en el próximo compás."),
    ],
    [
        ex("¿Cuántos criterios de musicalidad usa la clase?", "4", "Son pulso, dinámica y tempo coherentes, frases y concentración."),
        ex("Si te equivocas durante una presentación, ¿sigues con el pulso o te detienes?", "Sigues con el pulso", "Así mantienes la obra."),
        ex("¿Una marcha pide dinámica fuerte o suave?", "Fuerte", "La marcha es firme y enérgica."),
    ],
    [
        ex("¿Qué recurso expresa mejor una despedida tranquila: un diminuendo final o un golpe fuerte al terminar?", "Un diminuendo final", "El volumen que baja da sensación de calma."),
        ex("En el fraseo, ¿qué se hace al final de una frase: respirar o bajar un poco el volumen, o seguir con el mismo volumen sin pausa?", "Respirar o bajar un poco el volumen", "Así se marca el final de la frase."),
        ex("Una persona toca con pulso estable pero sin variar el volumen en toda la obra, que expresa una tormenta. ¿Qué criterio le falta: dinámica coherente o final claro?", "Dinámica coherente", "Una tormenta pide cambios de volumen."),
    ],
    [
        arith("Un grupo de 20 personas se divide en 4 equipos iguales para evaluarse con los 4 criterios. ¿Cuántas personas tiene cada equipo?", "20//4", "Se reparte el grupo en partes iguales.", " personas"),
        ex("Una obra de 8 compases tiene dos frases de 4 compases. ¿En qué compases conviene respirar o bajar un poco el volumen?", "Al final de cada frase, en los compases 4 y 8", "Cada frase termina en esos compases."),
        ex("Una canción de despedida va a 60 pulsos por minuto y baja el volumen en el último compás. ¿Qué recursos usa para expresar calma: tempo lento y diminuendo, o tempo rápido y crescendo?", "Tempo lento y diminuendo", "60 es un tempo lento y bajar el volumen da sensación de calma."),
    ],
    [
        ex("Mara dice que la musicalidad solo la tienen quienes son muy talentosos. ¿Es cierto?", "No: se puede observar y mejorar con criterios", "Los criterios de la clase permiten practicarla."),
        ex("Dos intérpretes tocan las mismas notas: una con p y tempo lento y otra con f y tempo rápido, para una canción de cuna. ¿Quién mostró mayor musicalidad?", "La primera", "Sus recursos coinciden con el propósito de la cuna."),
    ],
    [
        ex("Una obra tiene 4 frases de 4 compases. Respiras al final de cada frase. ¿En qué compases respiras?", "4, 8, 12 y 16", "Cada frase termina cada 4 compases."),
        arith("Una presentación de 3 minutos tiene 36 compases y cada frase dura 4 compases. ¿Cuántas frases tiene?", "36//4", "Se reparten los compases entre las frases.", " frases"),
    ],
    [ex("Un coro presenta una canción alegre de fiesta. Un integrante canta distraído, conversando con quien tiene al lado, y otro canta atento, mirando al grupo y al público. ¿Quién muestra mejor la concentración y la actitud del criterio de la clase?", "El que canta atento", "La actitud también comunica el propósito.")],
    [ex("¿Qué agrega la musicalidad a tocar las notas correctas?", "Expresión coherente con el propósito", "Hace que la obra comunique algo."), ex("¿Qué se hace al terminar la obra?", "Un final claro", "Es uno de los criterios."), ex("¿Qué pasa si hay un error?", "Se sigue con el pulso", "No se detiene la obra.")],
    (
        f"Interpreta esta canción inventada de 8 compases: «Duerme, pajarito» para arrullar, con melodía de cuatro grupos de 4 notas, y cada grupo ocupa 2 compases: 3-3-2-1 | 3-3-2-1 | 5-5-4-3 | 3-2-1-1. Antes de tocarla o cantarla, decide dinámica, tempo y dónde respirarás. Interprétala dos veces, y pide a alguien (o grábate con permiso) que marque cuántos de los cuatro criterios ({MU3}) viste cumplidos. Anota qué mejorarías en la segunda vuelta.",
        "Dinámica p, tempo lento (60), respiro al final del compás 4 y del compás 8. La primera vuelta cumplió 3 criterios: me faltó concentración porque me reí. En la segunda vuelta me concentré en el pulso, mantuve el final con diminuendo, y cumplí los 4.",
        ["decide dinámica, tempo y respiraciones coherentes", "mantiene el pulso", "revisa los criterios y propone una mejora"],
        ["decisiones escritas", "interpretación realizada"],
        ["usar f y tempo rápido para una cuna", "detenerse al equivocarse"],
        "Reconoce la interpretación y pide señalar en cuál frase se notó mejor el propósito.",
    ),
    "Respira y baja el volumen al final de cada frase de una canción que conoces.",
    "Escribe un plan de musicalidad para una marcha: dinámica, tempo, frases y final.",
)

# ---------------------------------------------------------------- OA 06 · clase 4 (presentación grupal a la comunidad)
PROG = "programa de práctica: obra 1 (3 minutos), obra 2 (4 minutos), obra 3 (2 minutos), obra 4 (5 minutos); entre obra y obra hay 1 minuto para el cambio de lugar"

L(
    OA6, 4,
    f"Lápiz y papel. {PROG.capitalize()}. Todos los datos están en los ejercicios. Si hay presentación real, se hace en un lugar seguro y con volumen cuidado; grabar o fotografiar solo con permiso del curso y de las familias.",
    "Aprenderé a organizar y realizar una presentación grupal para el curso o la comunidad: armar el programa, calcular el tiempo, coordinar a los grupos y cuidar al público. Sirve para mostrar el trabajo musical con orden y respeto.",
    ["Sé preparar un plan de ensayos.", "Sé usar un método de ensayo.", "Sé interpretar con musicalidad."],
    [
        f"Una presentación grupal a la comunidad necesita un programa: la lista de obras en orden, con su duración. Con el {PROG}, el tiempo total es la suma de las obras más los cambios de lugar. El orden de las obras también comunica: se puede comenzar con una obra suave para captar la atención y dejar la más energética para el final.",
        "Además del programa, hay roles: alguien presenta cada obra con una frase corta (qué es y para qué se hizo), alguien cuida los instrumentos y alguien da la señal de entrada. Antes de la función se hace un ensayo general en el mismo lugar, con el mismo orden, para comprobar el tiempo, el volumen y los cambios. Los grupos esperan su turno en silencio.",
        "El público también tiene un papel: escucha en silencio, aplaude al terminar y respeta a todos los grupos. Después se hace una evaluación en grupo: ¿cumplimos el programa y el tiempo?, ¿se oyó el propósito de cada obra?, ¿qué haríamos distinto? Nadie es obligado a exponerse: quienes no quieren tocar pueden presentar, dirigir o cuidar los instrumentos. Así todos participan con seguridad.",
    ],
    [("programa", "lista ordenada de obras con su duración"), ("ensayo general", "ensayo completo en el lugar y con el orden de la función"), ("cambio de lugar", "tiempo para que un grupo se retire y entre otro"), ("público", "personas que escuchan la presentación"), ("evaluación grupal", "revisión que hace el grupo después de presentar")],
    [
        ("Calcular el tiempo", "Un programa tiene 3 obras de 3, 4 y 5 minutos, y 1 minuto de cambio entre una y otra. ¿Cuántos minutos dura en total?", ["Obras: 3 + 4 + 5 = 12 minutos.", "Hay 2 cambios: 2 minutos.", "12 + 2 = 14."], "14 minutos"),
        ("Ordenar el programa", "Un grupo tiene una obra suave y otra muy energética. Para captar la atención y terminar con fuerza, ¿cuál va primero?", ["Comenzar suave capta la atención.", "La energética queda para el final."], "La obra suave"),
    ],
    [
        ("No hacer ensayo general.", "Sin ensayo en el lugar real aparecen sorpresas de tiempo y volumen.", "Ensaya completo con el mismo orden."),
        ("Que el público converse mientras se toca.", "Quien interpreta pierde concentración y falta el respeto a sus compañeros.", "Pide silencio y aplauso al final."),
    ],
    [
        ex("En una función, ¿cómo se llama la lista ordenada de obras con su duración?", "Programa", "Organiza la función."),
        ex("¿Qué hace el público durante una obra: escucha en silencio o conversa?", "Escucha en silencio", "Así se respeta a quien interpreta."),
        ex("Si alguien no quiere tocar frente al público, ¿se le obliga o se le propone otro rol?", "Se le propone otro rol", "Puede presentar, dirigir o cuidar los instrumentos."),
    ],
    [
        ex(f"Con el {PROG}, ¿cuántas obras tiene?", "4", "Son las obras 1, 2, 3 y 4."),
        ex(f"Con el {PROG}, ¿cuántos cambios de lugar hay?", "3", "Hay un cambio entre cada par de obras seguidas."),
        ex(f"Con el {PROG}, ¿cuál obra es la más larga?", "La obra 4", "Dura 5 minutos."),
    ],
    [
        arith(f"Con el {PROG}, ¿cuántos minutos dura solo la música, sin contar los cambios?", "3+4+2+5", "Se suman las duraciones de las obras.", " minutos"),
        arith(f"Con el {PROG}, ¿cuántos minutos dura la función entera, con los cambios?", "3+4+2+5+3*1", "Se suma la música y 3 cambios de 1 minuto.", " minutos"),
        arith("El tiempo disponible es de 20 minutos y el programa dura 17 minutos. ¿Cuántos minutos sobran para la bienvenida?", "20-17", "Se resta el programa del tiempo disponible.", " minutos"),
    ],
    [
        ex("Un grupo termina su obra y el siguiente tarda 4 minutos en instalarse en vez de 1. ¿Qué pudo faltar: un ensayo general o más público?", "Un ensayo general", "El ensayo general comprueba los cambios de lugar."),
        ex("Ana dice que el público puede aplaudir en medio de una obra para animar al grupo. ¿Es lo mejor?", "No: se aplaude al terminar para no interrumpir", "Se respeta la concentración del grupo."),
    ],
    [
        arith("Una función tiene 5 grupos de 4 minutos y 4 cambios de 2 minutos. ¿Cuántos minutos dura?", "5*4+4*2", "Se suman la música y los cambios.", " minutos"),
        ex("Un programa de 17 minutos comienza a las 10:00. ¿A qué hora termina si no hay retraso?", "10:17", "Se suman 17 minutos a las 10:00."),
    ],
    [ex("Para la función de fin de semestre, un curso quiere presentar en 25 minutos. Con 4 obras de 4, 5, 3 y 6 minutos y 3 cambios de 1 minuto, ¿cabe en el tiempo? Responde sí o no.", "Sí", "La música suma 18 minutos y con 3 cambios son 21, que es menos de 25.")],
    [ex("¿Qué es un ensayo general?", "Un ensayo completo en el lugar y con el orden de la función", "Sirve para comprobar el tiempo."), ex("¿Cuándo aplaude el público?", "Al terminar la obra", "Así no interrumpe."), ex("¿Qué se hace después de presentar?", "Una evaluación grupal", "Se revisa qué salió bien y qué mejorar.")],
    (
        "Organiza el programa de una presentación de tu curso con estas cuatro obras inventadas: «Ronda del sol» (3 minutos, suave), «Marcha de los panderos» (2 minutos, enérgica), «Canción del mar» (4 minutos, tranquila) y «Fiesta final» (5 minutos, muy enérgica). Entre una y otra hay 1 minuto de cambio. Escribe el orden que propones, justifícalo con el propósito de cada obra, y calcula la duración total. Agrega un rol de presentador para cada obra con una frase de una línea.",
        "Orden: 1) Ronda del sol (suave, abre con calma), 2) Canción del mar (tranquila), 3) Marcha de los panderos (sube la energía), 4) Fiesta final (cierra con fuerza). Duración: 3 + 4 + 2 + 5 = 14 minutos de música y 3 cambios de 1 minuto: 17 minutos. Presentador: «Ahora cantamos la Ronda del sol, para saludar el día».",
        ["ordena las obras con una justificación", "calcula bien la duración total", "incluye frases de presentación"],
        ["programa escrito"],
        ["olvidar los cambios de lugar", "no justificar el orden"],
        "Reconoce el programa y pide mostrar el cálculo de los cambios de lugar.",
    ),
    "Escribe una frase de presentación de una línea para una obra que conozcas.",
    "Diseña la lista de verificación del ensayo general: tiempo, volumen, orden y cambios de lugar.",
)

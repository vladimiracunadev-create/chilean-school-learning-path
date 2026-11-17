"""Interpretación y creación en teatro 3.º y 4.º medio HC: OAC-07 (evaluación crítica de procesos y resultados propios y de pares, clases 1 a 5) y OAC-08 (habilidades de la asignatura y contextos laborales, profesionales y de desarrollo personal, clases 1 a 4). Piezas, datos y casos inventados."""
from __future__ import annotations

from hc_icte_common import build

O7 = "AR-ICTE-3y4-OAC-07"
O8 = "AR-ICTE-3y4-OAC-08"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (tabla de trazabilidad de ejemplo, inventada). Pieza «Mapa de silencios», de un grupo del curso. Propósito: que el público note cuánto se calla en una conversación cotidiana. "
     "Decisión D1: pausas largas antes de cada respuesta; efecto observado en el ensayo: el público de prueba contó las pausas y dijo que sintió incomodidad. "
     "Decisión D2: una música continua de fondo; efecto observado: nadie pudo oír las pausas. "
     "Decisión D3: un cartel con la hora de cada escena; efecto observado: dos personas del público no entendieron para qué estaba. "
     "Decisión D4: luz que baja un poco en cada pausa; efecto observado: el público dijo que notó el silencio con más claridad.")
build(
    O7, 1, F,
    use="Aprenderé a evaluar críticamente una pieza propia o ajena con trazabilidad: unir propósito, decisión y efecto con evidencia, y a distinguir si una decisión sirvió, no sirvió o no tiene evidencia suficiente.",
    prior=["Sé formular un propósito expresivo.", "Sé hacer una retroalimentación descriptiva.", "Sé analizar con evidencia y reconocer sesgos."],
    explain=[
        "Evaluar críticamente es emitir un juicio fundado sobre un proceso y un resultado, con criterios y evidencia, y estar dispuesto a revisarlo. No es criticar por criticar ni elogiar sin razones. Para evaluar una pieza teatral conviene la trazabilidad: seguir el hilo que va del propósito a cada decisión (qué se hizo y por qué) y de cada decisión a su efecto (qué se observó en el público o en el ensayo). Si la cadena se corta, la decisión no puede evaluarse bien.",
        "Una decisión puede servir al propósito, ir en contra o no tener evidencia suficiente para juzgarla. Para saberlo se mira el efecto con datos: qué dijo o hizo el público de prueba, qué se registró en la bitácora. Se evalúan dos cosas: el proceso (cómo se decidió, se probó y se corrigió) y el resultado (qué logró la pieza). Una pieza puede tener un buen proceso y un resultado limitado, o al revés, y es útil separarlos para mejorar.",
        "Evaluar con rigor no significa ser duro. Se habla de decisiones y no de personas, se reconocen los logros y se señala con precisión lo que falta. En el trabajo con pares se cuida el respeto y la privacidad, y nadie queda expuesto frente al curso sin quererlo. Si una evaluación genera incomodidad o malestar, se detiene la conversación y se avisa a una persona adulta de confianza.",
    ],
    vocab=[("evaluar críticamente", "emitir un juicio fundado con criterios y evidencia, y estar dispuesto a revisarlo"), ("trazabilidad", "hilo que une propósito, decisión y efecto"), ("proceso", "forma en que se decidió, probó y corrigió"), ("resultado", "lo que logró la pieza"), ("público de prueba", "grupo pequeño que ve un ensayo para dar información")],
    worked=[
        ("Seguir una cadena", "Propósito: mostrar apuro. Decisión: frases cortas y rápidas. Efecto observado: el público de prueba dijo que se sentía apurado. ¿Qué evaluación corresponde?", ["La decisión se vincula con el propósito y el efecto coincide.", "La decisión sirvió al propósito."], "La decisión sirvió"),
        ("Evidencia insuficiente", "Una decisión no tiene registro de efecto, porque nadie la observó. ¿Qué se puede decir?", ["Sin dato de efecto no se puede juzgar con rigor.", "Se declara «sin evidencia suficiente» y se planea observar en el siguiente ensayo."], "Sin evidencia suficiente; se observará en el siguiente ensayo"),
    ],
    mistakes=[("Evaluar una decisión por si gustó al grupo y no por su efecto en el propósito.", "El gusto del grupo no dice si la decisión logró lo que se quería.", "Compara el efecto observado con el propósito."),
              ("Mezclar proceso y resultado en un solo juicio.", "Se pierde información para saber qué mejorar.", "Evalúa cada uno por separado.")],
    T=[
        ('abc', 'En evaluación teatral, ¿qué es la trazabilidad?', 'El hilo que vincula propósito, decisión y efecto', 'La lista de las personas que participan en la pieza', 'La cantidad de ensayos realizados', 'Con trazabilidad se puede seguir por qué se decidió algo y qué produjo.'),
        ('abc', '{F} ¿Qué decisión sirvió al propósito, según el efecto observado?', 'D1, las pausas largas, que produjeron incomodidad', 'D2, la música continua, que tapó las pausas', 'D3, el cartel, que no se entendió', 'D1 provocó lo que el propósito buscaba: notar los silencios.'),
        ('abc', '{F} ¿Qué decisión fue en contra del propósito?', 'D2, la música continua que impidió oír las pausas', 'D4, la luz que baja un poco en cada pausa y que ayuda a notar el silencio', 'D1, las pausas largas antes de cada respuesta que produjeron incomodidad', 'Si no se oyen las pausas, el propósito se debilita.'),
        ('abc', '{F} ¿Qué decisión no tiene un efecto claro hacia el propósito?', 'D3, el cartel con la hora de cada escena', 'D1, las pausas largas', 'D4, la luz que baja en las pausas', 'D3 produjo confusión y no se vincula con el propósito.'),
        ('=', '{F} El público de prueba tiene 10 personas; 2 no entendieron el cartel. ¿Qué porcentaje no lo entendió?', '2*100//10', 'Se divide quienes no entendieron entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué recomendación tiene mejor respaldo en la tabla?', 'Quitar la música continua o bajarla para que se oigan las pausas', 'Agregar más música para hacer más atractivo el resultado', 'Quitar la luz que baja porque ayudó al propósito', 'La evidencia indica que la música impide el efecto buscado.'),
        ('abc', 'Un grupo evalúa su pieza y dice: «salió bien porque nos aplaudieron». ¿Qué falta?', 'Relacionar los efectos observados con el propósito, con evidencia de las decisiones', 'Más aplausos de otro curso que confirmen que la pieza tuvo una buena recepción', 'Una comparación con piezas de otros grupos del curso que hicieron algo parecido', 'El aplauso no muestra si se logró el propósito.'),
        ('abc', '{F} Una compañera dice «la música fue un error de la persona que la propuso». ¿Qué corrección corresponde?', 'Hablar de la decisión y su efecto, no de la persona', 'Repetir quién fue la persona que propuso la música para que asuma lo que ocurrió', 'Eliminar toda la evaluación, porque hablar de decisiones siempre termina en discusiones', 'Se evalúan decisiones y no personas.'),
        ('abc', 'El proceso de un grupo fue ordenado: probaron, registraron y corrigieron. Su resultado fue limitado. ¿Cómo se evalúa?', 'Se reconocen un buen proceso y un resultado limitado, y se busca qué mejorar', 'Se declara que el proceso fue malo porque el resultado de la pieza fue débil', 'Se omite el proceso y solo se evalúa el resultado final que ve el público', 'Evaluar por separado da información más útil.'),
        ('abc', '{F} El grupo decide cambiar D1, D2, D3 y D4 a la vez en el próximo ensayo. ¿Qué problema trae?', 'No sabrá qué cambio produjo el nuevo efecto', 'Ninguno, porque cuatro cambios dan más información que uno solo', 'Que no podrá anotar los cambios en la bitácora del ensayo', 'Con varios cambios juntos no hay trazabilidad.'),
        ('=', '{F} Si cada pausa de D1 dura 4 segundos y hay 9 pausas, ¿cuántos segundos de pausas tiene la pieza?', '9*4', 'Se multiplican las pausas por su duración.', ' segundos'),
        ('abc', 'Una estudiante cree que su evaluación de la pieza de un compañero es muy dura y teme que le caiga mal. ¿Qué paso conviene?', 'Reescribir con descripciones y sugerencias, y reconocer lo que sí funcionó', 'Eliminar la evaluación completa para evitar conflictos con el grupo que se evalúa', 'Decirla con firmeza frente a todo el curso para que el grupo entienda lo que opina', 'Una evaluación rigurosa puede ser respetuosa.'),
        ('abc', '{F} Con la evidencia disponible, ¿qué se puede decir de la decisión D4?', 'Que sirvió al propósito, porque el público dijo que notó más el silencio', 'Que no sirvió, porque en el ensayo no hubo aplausos cuando la luz bajó', 'Que no se puede decir nada de ella porque el público no entregó ningún comentario', 'Hay un efecto observado que coincide con el propósito.'),
    ],
    ctx=('abc', 'Un grupo tiene una pieza sobre la prisa. Su bitácora dice: «ensayo 1: probamos frases cortas; ensayo 2: sumamos música rápida; el público dijo que se sentía agobiado y sin poder escuchar el texto». ¿Qué evaluación es más precisa?', 'La música rápida pudo haber agobiado y tapado el texto; conviene probar de nuevo con una sola variable', 'La pieza es mala y debe cambiarse por completo antes del próximo ensayo del grupo', 'El público no entendió nada y no vale la pena revisar ninguna de las decisiones', 'Se atribuye con prudencia y se propone una nueva prueba.'),
    sc=[
        ("En Teatro: ¿qué se compara para saber si una decisión funcionó?", "El efecto observado con el propósito de la pieza", "Es lo que se quería lograr frente a lo que ocurrió."),
        ("¿Por qué se evalúan por separado el proceso y el resultado?", "Porque cada uno da información distinta sobre qué mejorar", "Pueden ser muy distintos entre sí."),
        ("¿Qué se evalúa en una pieza ajena?", "Las decisiones y sus efectos, no a las personas", "Se cuida el respeto y la precisión."),
    ],
    op=("Crea una tabla de trazabilidad de ejemplo para una pieza inventada (propósito neutro) con cuatro decisiones. Para cada una escribe el efecto observado (puede ser inventado, de un público de prueba) y tu evaluación: sirvió, no sirvió o sin evidencia. Cierra con una recomendación respaldada.",
        "Pieza «Conversación por mensajes». Propósito: mostrar la ansiedad de esperar una respuesta. D1 pantalla proyectada con puntos suspensivos: el público sintió la espera (sirvió). D2 música alegre: el público se confundió (no sirvió). D3 un reloj de pared: nadie lo mencionó (sin evidencia). D4 respiración audible: el público dijo que notó la tensión (sirvió). Recomendación: quitar la música alegre.",
        ["cuatro decisiones con efecto observado", "evaluación de cada decisión con una de las tres categorías", "recomendación respaldada por los datos", "habla de decisiones y no de personas"],
        ["tabla de cuatro decisiones y recomendación"],
        ["evaluar por gusto y no por efecto", "no marcar «sin evidencia» cuando falta el dato"],
        "Pregunta: «¿qué efecto se observó y quién lo observó?». Si no hay dato, pídele rotularla «sin evidencia»."),
    reinforce="Elige una actividad de tu semana, anota qué querías lograr, qué hiciste y qué efecto tuvo, y cierra con una evaluación breve.",
    extend="Explica por qué la trazabilidad evita culpar a personas y ayuda a mejorar una pieza, y da un ejemplo propio.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (borrador de pauta de evaluación, de ejemplo, con problemas). Pieza breve del curso. Criterios y niveles del borrador: "
     "Criterio A, «se ve bonito»: nivel 4 si gusta mucho, nivel 1 si no gusta. "
     "Criterio B, «actitud y claridad vocal y trabajo en equipo»: nivel 4 si todo está muy bien, nivel 1 si algo está mal. "
     "Criterio C, «claridad de la voz»: nivel 4 si cada frase se entiende desde el fondo; nivel 3 si se pierde una frase; nivel 2 si se pierden varias frases; nivel 1 si casi no se entiende. "
     "Criterio D, «coherencia entre decisiones y propósito»: nivel 4 si todas las decisiones apoyan el propósito; nivel 3 si casi todas; nivel 2 si algunas; nivel 1 si pocas. "
     "Ponderación propuesta: A, 10 %; B, 20 %; C, 30 %; D, 40 %.")
build(
    O7, 2, F,
    use="Aprenderé a diseñar una pauta de evaluación propia con criterios claros, niveles de logro con descriptores observables y ponderaciones razonables, y a revisarla para que mida lo que dice medir.",
    prior=["Sé evaluar una pieza con trazabilidad.", "Sé separar gusto de juicio.", "Sé calcular porcentajes."],
    explain=[
        "Una pauta es un instrumento con criterios (qué se evalúa) y niveles de logro (cuánto se cumple), cada uno con un descriptor, es decir, una frase que dice qué se observa en ese nivel. Un buen criterio evalúa una sola cosa; si mezcla varias (voz, actitud y trabajo en equipo), no se sabe qué mejorar. Un buen descriptor es observable y distinguible: «cada frase se entiende desde el fondo» se puede comprobar; «se ve bonito» o «gusta mucho» depende del gusto y no del trabajo.",
        "Una pauta es válida cuando mide lo que dice medir, y confiable cuando distintas personas llegan a puntajes parecidos al aplicarla. Para revisarla se prueba con una pieza y se compara con otra persona. La ponderación es el peso de cada criterio en el resultado total: los criterios más importantes para el propósito pesan más. Una ponderación se acuerda y se justifica, y la suma de pesos debe dar 100 %.",
        "Evaluar con pauta no reemplaza el diálogo: se acompaña de comentarios descriptivos. La pauta evalúa la pieza y las decisiones, no a las personas ni sus cuerpos. Antes de aplicarla a otras personas, se les muestra para que sepan con qué se las evaluará, y si algo les parece injusto, se revisa.",
    ],
    vocab=[("criterio", "aspecto que se evalúa"), ("descriptor", "frase que dice qué se observa en un nivel de logro"), ("nivel de logro", "grado en que se cumple un criterio"), ("ponderación", "peso que cada criterio tiene en el total"), ("validez", "capacidad de la pauta de medir lo que dice medir")],
    worked=[
        ("Reescribir un criterio", "El criterio «actitud y voz» mezcla dos cosas. ¿Cómo se corrige?", ["Se separan en dos criterios.", "Criterio 1: claridad de la voz. Criterio 2: disposición al trabajo del grupo, con sus propios descriptores."], "Dos criterios separados"),
        ("Calcular un total ponderado", "Un criterio pesa 60 % y otro 40 %. Con puntajes 3 y 4 (de 4), ¿cuál es el total ponderado?", ["60 % de 3 es 1,8 y 40 % de 4 es 1,6.", "Total: 3,4 de 4."], "3,4 de 4"),
    ],
    mistakes=[("Escribir descriptores como «bien», «regular» y «mal».", "No dicen qué se observa, por lo que cada persona los interpreta distinto.", "Usa hechos observables."),
              ("Dar el mismo peso a todos los criterios sin pensar en el propósito.", "Un detalle menor puede pesar tanto como lo esencial.", "Pondera según la importancia para el propósito.")],
    T=[
        ('abc', 'En una pauta, ¿qué es un descriptor?', 'Una frase que dice qué se observa en un nivel de logro', 'El nombre de la persona que evalúa la pieza y el curso al que pertenece', 'El puntaje total que obtuvo la pieza en la aplicación de la pauta de evaluación', 'El descriptor hace observable cada nivel.'),
        ('abc', '{F} ¿Qué problema tiene el criterio A?', 'Depende del gusto y no de una decisión observable de la pieza', 'Tiene demasiados niveles de logro, lo que hace muy difícil aplicarla en un ensayo', 'Evalúa dos cosas distintas a la vez, la voz y el trabajo en equipo del grupo', 'Se mide por si gusta y no por lo que se hizo.'),
        ('abc', '{F} ¿Qué problema tiene el criterio B?', 'Mezcla tres aspectos distintos y sus niveles no dicen qué se observa', 'Es demasiado preciso y por eso no deja ningún margen para opinar sobre la pieza', 'Tiene una ponderación mayor que la suma de las ponderaciones de todos los demás criterios', 'Un criterio debe evaluar una sola cosa con descriptores observables.'),
        ('abc', '{F} ¿Qué criterio está mejor formulado?', 'El criterio C, porque tiene descriptores observables y un solo aspecto', 'El criterio A, porque se entiende rápido y no necesita explicaciones del grupo', 'El criterio B, porque abarca más aspectos de la pieza dentro de un solo criterio', 'C evalúa una sola cosa con niveles distinguibles.'),
        ('=', '{F} ¿Cuánto suman las ponderaciones propuestas?', '10+20+30+40', 'Se suman los pesos de los cuatro criterios.', ' %'),
        ('abc', '{F} ¿Por qué tiene sentido que el criterio D pese 40 %?', 'Porque la coherencia con el propósito es lo más importante de la pieza', 'Porque es el único criterio que se puede medir sin errores', 'Porque debe haber un criterio que pese más sin importar el propósito', 'La ponderación refleja la importancia para el propósito.'),
        ('=', '{F} ¿Qué porcentaje del total pesan juntos los criterios C y D?', '30+40', 'Se suman las ponderaciones de los dos criterios.', ' %'),
        ('abc', '{F} Un compañero propone reemplazar los descriptores de C por «bien», «medio» y «mal». ¿Qué problema trae?', 'Pierden precisión y cada persona los interpretaría distinto', 'Los hace más largos y por eso se tarda más en leerlos durante la evaluación', 'Los hace más difíciles de aplicar a una pieza que dura pocos minutos en el escenario', 'Los descriptores deben ser observables y distinguibles entre sí.'),
        ('abc', 'Dos personas aplican la misma pauta a una pieza y obtienen puntajes muy distintos. ¿Qué conclusión es prudente?', 'La pauta podría tener descriptores poco claros y conviene revisarla', 'Una de las dos personas es mala evaluando y su puntaje debe descartarse del resultado', 'El resultado no importa, porque cada persona puede ver la pieza de manera distinta', 'La confiabilidad se revisa cuando los puntajes difieren mucho.'),
        ('abc', 'Antes de aplicar la pauta a otro grupo, ¿qué conviene hacer?', 'Mostrársela para que sepan con qué se evaluará y atender sus dudas', 'Aplicarla sin avisar para obtener resultados más espontáneos', 'Cambiar la pauta por una más simple sin explicar', 'Transparentar los criterios es parte de una evaluación justa.'),
        ('=', 'Una pauta tiene 5 criterios de 4 puntos máximo cada uno. ¿Cuál es el puntaje máximo total?', '5*4', 'Se multiplica el máximo por el número de criterios.', ' puntos'),
        ('abc', '{F} Un integrante propone agregar un criterio sobre «el aspecto físico del elenco». ¿Qué corresponde?', 'Rechazarlo, porque la pauta evalúa decisiones de la pieza y no cuerpos', 'Aceptarlo para tener una pauta más completa que incluya todos los aspectos visibles', 'Aplicarlo solo a algunas personas del elenco que acepten que se evalúe su aspecto', 'No se evalúa el cuerpo de nadie.'),
        ('abc', '{F} El grupo quiere medir mejor el criterio A. ¿Qué cambio lo mejora?', 'Reemplazarlo por un criterio observable, como «los colores del vestuario sostienen la emoción de la escena»', 'Mantener «se ve bonito» y agregar un puntaje más alto para las piezas que gusten', 'Eliminar los niveles de logro del criterio y dejar solo una nota general para la pieza', 'Debe medir una decisión observable y no el gusto.'),
    ],
    ctx=('abc', 'Un curso diseña una pauta para valorar piezas de otros cursos y cada grupo pide que su criterio favorito pese más. ¿Cómo se resuelve de forma justa?', 'Acordar los pesos en función del propósito de la actividad y justificarlos ante todos', 'Dar más peso a los criterios del grupo más numeroso, porque tiene más votos en el curso', 'Aplicar pesos distintos a cada grupo según la simpatía que cada integrante les tenga', 'La ponderación se acuerda por propósito y se justifica.'),
    sc=[
        ("En Teatro: ¿qué hace una pauta válida?", "Mide lo que dice medir", "La validez es medir lo que se propone."),
        ("¿Qué debe sumar la ponderación de todos los criterios?", "100 %", "Los pesos representan el total de la evaluación."),
        ("¿Por qué un criterio no debe mezclar varios aspectos?", "Porque no se sabría qué mejorar", "Cada criterio debe señalar una sola cosa."),
    ],
    op=("Diseña una pauta de tres criterios para evaluar una escena breve de ejemplo. Para cada criterio escribe un descriptor observable por nivel (1 a 4), una ponderación y la justificación de su peso. Verifica que los pesos sumen 100 % y que no evalúe cuerpos.",
        "Criterio 1, claridad de la voz (40 %): 4 si cada frase se entiende desde el fondo; 3 si se pierde una; 2 si se pierden varias; 1 si casi no se entiende. Criterio 2, coherencia con el propósito (40 %): 4 si todas las decisiones lo apoyan; 3 si casi todas; 2 si algunas; 1 si pocas. Criterio 3, uso del espacio (20 %): 4 si la marcación sostiene el foco; 3 si casi siempre; 2 si a veces; 1 si no. Suma: 100 %.",
        ["tres criterios con cuatro descriptores cada uno", "los descriptores son observables", "pesos que suman 100 %", "no evalúa cuerpos"],
        ["pauta de tres criterios con ponderaciones"],
        ["descriptores como «bien» y «mal»", "pesos que no suman 100 %"],
        "Pregunta: «¿cómo lo comprobarías mirando?». Si no se puede comprobar, pídele reformular el descriptor."),
    reinforce="Escribe una pauta de dos criterios para evaluar un plato de comida o un dibujo y pide a alguien que la aplique contigo.",
    extend="Explica por qué una pauta clara protege a quien es evaluado de juicios arbitrarios y da un ejemplo.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (comentarios de pares, de ejemplo, inventados) sobre una escena breve de «Mapa de silencios». "
     "C1: «Me encantó, porque somos amigos.» "
     "C2: «En el segundo cambio de escena, la voz de la persona del fondo no se oyó; eso restó claridad a la parte final; podrían probar proyectar desde el centro.» "
     "C3: «Nunca vas a ser buena para esto.» "
     "C4: «Como el primer ensayo fue excelente, el de hoy también lo fue, aunque no vi lo del cambio de luz.» "
     "C5: «Soy muy exigente: para mí, nada pasa de 4 sobre 7.» "
     "Protocolo del curso: pregunta de quien recibe, observación, efecto, sugerencia.")
build(
    O7, 3, F,
    use="Aprenderé a coevaluar el trabajo de pares con un protocolo (pregunta, observación, efecto y sugerencia), a reconocer sesgos de evaluación (amistad, halo, severidad y efecto reciente) y a recibir comentarios con apertura.",
    prior=["Sé usar una pauta con descriptores.", "Sé dar retroalimentación descriptiva.", "Conozco sesgos de apreciación."],
    explain=[
        "La coevaluación es la evaluación entre pares. Funciona mejor con un protocolo claro: quien recibe pide qué quiere que se observe (la pregunta), el par describe lo que vio (observación), indica qué efecto tuvo (efecto) y propone una posibilidad (sugerencia). Así la persona evaluada decide qué cambiar. Un comentario útil habla de una decisión o de un hecho observable, no de la persona ni de su capacidad.",
        "Hay sesgos que distorsionan la evaluación. El sesgo de amistad hace evaluar mejor a quienes se quiere y peor a quienes no. El efecto halo ocurre cuando una impresión general (una buena voz) tiñe todos los criterios. El efecto reciente da más peso a lo último que se vio. La severidad excesiva o la benevolencia excesiva ocurren cuando se evalúa siempre muy bajo o muy alto sin mirar la evidencia. Para reducirlos se usan pautas, se toman notas durante la observación y se separa lo que se vio de lo que se supone.",
        "Quien recibe comentarios tiene derecho a respeto y a decidir qué hacer con ellos. Escucha completo antes de responder y pide aclaraciones sin defenderse de inmediato. Los comentarios que descalifican a una persona o la humillan no son evaluación: se detienen y, si se repiten, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("coevaluación", "evaluación entre pares"), ("sesgo de amistad", "tendencia a evaluar mejor a quienes se quiere"), ("efecto halo", "una impresión general que tiñe todos los criterios"), ("efecto reciente", "dar más peso a lo último que se vio"), ("protocolo", "orden de pasos acordados para dar y recibir comentarios")],
    worked=[
        ("Aplicar el protocolo", "Observación: en la escena 2 hablaron dos personas a la vez. Escribe el comentario completo.", ["Observación: en la escena 2 hablaron dos personas a la vez.", "Efecto y sugerencia: el texto no se entendió; podrían marcar turnos."], "Observación, efecto y sugerencia completos"),
        ("Reconocer un sesgo", "«Como siempre actúa muy bien, no vi nada que mejorar hoy». ¿Qué sesgo es?", ["Una impresión general previa tiñe la evaluación.", "Es un efecto halo."], "Efecto halo"),
    ],
    mistakes=[("Comentar a la persona («eres desordenado») y no la decisión observada.", "Descalifica y no da información para cambiar.", "Describe el hecho observable y su efecto."),
              ("Defenderse apenas se recibe un comentario.", "Impide entender qué vio la otra persona.", "Escucha completo y pide aclaraciones.")],
    T=[
        ('abc', 'En coevaluación, ¿cuáles son los pasos del protocolo?', 'Pregunta, observación, efecto y sugerencia', 'Elogio, crítica, nota y comparación con otro grupo', 'Observación, nota, ranking y premio', 'Esos pasos van de lo pedido a lo observado, su efecto y una propuesta.'),
        ('abc', '{F} ¿Qué comentario sigue el protocolo?', 'C2, porque tiene observación, efecto y sugerencia', 'C1, porque es amable', 'C5, porque indica un criterio personal', 'C2 describe un hecho, su efecto y propone un cambio.'),
        ('abc', '{F} ¿Qué sesgo aparece en C1?', 'Sesgo de amistad', 'Efecto halo', 'Severidad excesiva', 'Evalúa por la relación y no por lo observado.'),
        ('abc', '{F} ¿Qué sesgo aparece en C4?', 'Efecto halo, porque el buen primer ensayo tiñe el juicio del segundo', 'Sesgo de amistad, porque evalúa mejor a quien conoce y con quien se lleva bien', 'Severidad excesiva, porque usa siempre puntajes bajos sin mirar lo que observó', 'Una impresión previa influye en el criterio actual.'),
        ('abc', '{F} ¿Qué sesgo aparece en C5?', 'Severidad excesiva, porque puntúa bajo siempre sin mirar la evidencia', 'Efecto reciente, porque da más peso a lo último que vio durante el ensayo', 'Sesgo de amistad, porque evalúa mejor a las personas con quienes se lleva bien', 'Su criterio personal no se apoya en lo observado.'),
        ('abc', '{F} ¿Por qué C3 no es una evaluación?', 'Descalifica a la persona y no describe ninguna decisión observable', 'Es demasiado breve para contener una evaluación completa de la escena del curso', 'Contiene una sugerencia para el siguiente ensayo que el grupo puede probar con tiempo', 'Un comentario evaluativo se centra en hechos y no en capacidades.'),
        ('=', '{F} Si C2 propone probar la proyección en 3 ensayos de 5 minutos, ¿cuántos minutos se necesitan?', '3*5', 'Se multiplican los ensayos por su duración.', ' minutos'),
        ('abc', '{F} ¿Cómo se reescribe C1 para seguir el protocolo?', '«En el primer cambio la luz marcó bien el foco; el público notó la tensión; podrían repetirlo en el cierre»', '«Me encantó, sigan así, porque se ve que se esfuerzan mucho en cada ensayo»', '«Estuvo mejor que el de otros grupos, y por eso merece una nota más alta»', 'Describe un hecho, su efecto y una sugerencia.'),
        ('abc', 'Quien recibe un comentario duro responde de inmediato diciendo que el par no sabe nada. ¿Qué conviene en su lugar?', 'Escuchar completo, pedir aclaraciones y decidir después qué cambiar', 'Ignorar todos los comentarios del par, porque no coinciden con lo que el grupo pensaba', 'Responder con otro comentario duro, para que el par entienda cómo se siente quien recibe', 'Escuchar y pedir aclaraciones permite usar lo útil.'),
        ('=', 'Un grupo recibe 10 comentarios: 7 siguen el protocolo completo. ¿Qué porcentaje lo sigue?', '7*100//10', 'Se divide los comentarios que lo siguen entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Un estudiante recibe C3 y se siente muy mal. ¿Qué corresponde?', 'Detener la conversación, no responder con otra agresión y avisar a una persona adulta si se repite', 'Seguir adelante con la conversación para demostrar que el comentario no le afecta nada', 'Pedir a más personas que comenten lo mismo en público para comparar opiniones', 'Un comentario humillante se corta y se informa.'),
        ('abc', 'Para reducir el efecto reciente al evaluar una función de 20 minutos, ¿qué se puede hacer?', 'Tomar notas durante toda la función y revisarlas antes de evaluar', 'Evaluar solo los últimos cinco minutos de la función, que es lo que mejor se recuerda', 'Evaluar por memoria al día siguiente, cuando ya se ha tenido tiempo de pensar', 'Las notas ayudan a considerar toda la función.'),
        ('abc', '{F} El curso propone que cada persona evalúe a una amiga y a una no amiga con la misma pauta. ¿Para qué sirve?', 'Para comparar si el sesgo de amistad cambia los puntajes', 'Para saber qué persona del curso es más exigente al evaluar', 'Para elegir a la mejor evaluadora del curso', 'Comparar puntajes ayuda a detectar sesgos.'),
    ],
    ctx=('abc', 'En una coevaluación de ensayos, un grupo recibe comentarios de otro y uno dice: «siempre hacen lo mismo». ¿Qué conviene pedir?', 'Que señale en qué escena y qué decisión observó, y qué efecto tuvo', 'Que deje de comentar porque no le gusta el grupo y no puede evaluar con justicia', 'Que repita el comentario más fuerte para que todos lo escuchen y lo tomen en cuenta', 'Se pide una observación concreta para poder trabajar.'),
    sc=[
        ("En Teatro: ¿qué es el efecto halo?", "Una impresión general que tiñe todos los criterios", "Distorsiona la evaluación de cada criterio por separado."),
        ("¿Cómo debe recibir una persona un comentario sobre su trabajo?", "Escuchando completo y pidiendo aclaraciones antes de responder", "Así entiende qué observó la otra persona."),
        ("¿Qué se hace con un comentario que humilla a alguien?", "Se detiene y, si se repite, se avisa a una persona adulta", "El respeto es condición de la coevaluación."),
    ],
    op=("Escribe tres comentarios de coevaluación para tres piezas breves inventadas (una sobre una despedida, una sobre un reclamo y una sobre un reencuentro). Cada comentario debe seguir el protocolo (observación, efecto y sugerencia). Agrega una frase que reconozca un sesgo tuyo posible al evaluar.",
        "Despedida: observé que la persona guarda la bufanda despacio; el efecto fue calma; sugiero repetir la acción con más pausa. Reclamo: observé que la voz sube en cada frase; el efecto fue tensión; sugiero variar el ritmo. Reencuentro: observé que se miran antes de hablar; el efecto fue cercanía; sugiero conservarlo. Sesgo posible: tiendo a evaluar mejor lo que se parece a mi estilo.",
        ["tres comentarios con observación, efecto y sugerencia", "los comentarios hablan de decisiones", "reconoce un sesgo propio", "es respetuoso"],
        ["tres comentarios y una frase sobre sesgo"],
        ["comentar a la persona y no a la decisión", "no incluir sugerencia"],
        "Pregunta: «¿qué viste exactamente?». Si no es observable, pídele reformular."),
    reinforce="Da a una persona de tu casa un comentario sobre algo que hizo, con observación, efecto y sugerencia, sin juicios sobre ella.",
    extend="Explica por qué reconocer el propio sesgo no lo elimina pero ayuda a reducirlo, y qué estrategias usarías en tu curso.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (datos de una función, de ejemplo, inventados). Pieza «Mapa de silencios». Propósito: que el público note cuánto se calla en una conversación. "
     "Asistencia: 32 de un aforo de 40. Encuesta voluntaria al salir, respondida por 16 personas, con una escala de 1 a 5 para «noté los silencios de la obra». "
     "Respuestas, en número de personas: 5 puntos, 7; 4 puntos, 4; 3 puntos, 3; 2 puntos, 2; 1 punto, 0. Suma de los puntos: 5×7 + 4×4 + 3×3 + 2×2 + 1×0 = 64. "
     "Comentarios escritos, resumidos: «las pausas fueron muy largas en la escena 3», «la música confundía», «me sentí incómoda, pero entendí por qué». "
     "Dato del proceso: se hicieron 5 ensayos, pero solo 1 con público de prueba.")
build(
    O7, 4, F,
    use="Aprenderé a evaluar el resultado de una pieza frente a su propósito usando datos del público (asistencia, encuestas y comentarios), a calcular porcentajes y promedios simples y a reconocer los límites de esos datos.",
    prior=["Sé evaluar con trazabilidad y pauta.", "Sé calcular porcentajes y promedios simples.", "Sé reconocer sesgos."],
    explain=[
        "Los datos del público ayudan a evaluar si una pieza logró su propósito. Los datos cuantitativos son números: asistencia, porcentaje de ocupación, respuestas a una escala. Los cualitativos son palabras: comentarios, descripciones, sugerencias. Los dos tipos se complementan: el número dice cuántas personas coinciden y el comentario dice por qué. El promedio de una escala se calcula sumando los puntos de todas las respuestas y dividiendo entre el número de respuestas.",
        "Todo dato tiene límites. Una encuesta voluntaria la responde solo una parte del público, y quienes responden pueden no representar a todos. Con pocas respuestas, un cambio pequeño modifica mucho el porcentaje. Un dato no explica por sí solo las causas: si el público notó los silencios, no se sabe sin más si fue por la luz, por las pausas o por el texto. Por eso se declara el límite, se evita generalizar y se vincula con la trazabilidad del proceso.",
        "El cuidado de las personas incluye la privacidad: las encuestas no piden nombres si no hace falta, ni datos personales, ni se publica quién respondió qué. Los comentarios se citan sin identificar a nadie. Si alguien escribe algo que revela malestar real, el grupo lo comunica a una persona adulta responsable y no lo comenta entre pares.",
    ],
    vocab=[("dato cuantitativo", "dato expresado en números"), ("dato cualitativo", "dato expresado en palabras o descripciones"), ("promedio", "suma de los puntos dividida entre el número de respuestas"), ("muestra", "parte del público que responde"), ("generalizar", "extender un resultado a todo el público sin tener datos suficientes")],
    worked=[
        ("Calcular un promedio", "Tres personas respondieron 5, 4 y 3 en una escala. ¿Cuál es el promedio?", ["Suma: 5 + 4 + 3 = 12.", "Se divide entre 3 respuestas: 4."], "4"),
        ("Reconocer un límite", "La encuesta fue voluntaria y la respondió una de cada dos personas del público. ¿Qué límite declaras?", ["Responden quienes quieren hacerlo.", "Quienes no respondieron podrían opinar distinto; no se generaliza a todo el público."], "No se puede generalizar a todo el público"),
    ],
    mistakes=[("Decir «al 100 % le gustó» con 3 respuestas.", "Con tan pocos datos el resultado es frágil y no representa al público.", "Declara cuántas personas respondieron y evita generalizar."),
              ("Atribuir un efecto a una causa sin evidencia.", "Los datos del público no dicen qué decisión produjo cada reacción.", "Vincula con el proceso y prueba la hipótesis.")],
    T=[
        ('abc', 'En evaluación, ¿qué es un dato cualitativo?', 'Un dato expresado en palabras, como un comentario del público', 'Un dato expresado solo en porcentajes, que se calcula a partir de las respuestas', 'Un dato que no puede registrarse, porque depende de lo que cada persona siente', 'Los comentarios son cualitativos, y los números, cuantitativos.'),
        ('=', '{F} ¿Qué porcentaje del aforo ocupó la asistencia?', '32*100//40', 'Se divide la asistencia entre el aforo y se pasa a porcentaje.', ' %'),
        ('=', '{F} ¿Qué porcentaje de los asistentes respondió la encuesta?', '16*100//32', 'Se divide las respuestas entre la asistencia y se pasa a porcentaje.', ' %'),
        ('=', '{F} ¿Cuál es el promedio de la escala (suma de puntos dividida entre respuestas)?', '64//16', 'Se divide la suma de puntos entre el número de respuestas.', ' puntos'),
        ('abc', '{F} ¿Cuántas personas dieron 4 o 5 puntos?', '11 personas', '7 personas', '16 personas', 'Siete dieron 5 puntos y cuatro dieron 4, es decir, once.'),
        ('=', '{F} ¿Cuántas personas dieron 3 puntos o menos?', '3+2+0', 'Se suman quienes dieron 3 puntos, 2 puntos y 1 punto.', ' personas'),
        ('abc', '{F} ¿Qué se puede afirmar con prudencia a partir de la encuesta?', 'Que entre quienes respondieron, la mayoría dijo notar los silencios', 'Que todo el público notó los silencios, aunque solo respondió una parte de él', 'Que los silencios son la causa de todos los comentarios que escribió el público', 'La encuesta es voluntaria y limitada; no se generaliza.'),
        ('abc', '{F} ¿Qué límite tiene este resultado?', 'Respondió solo la mitad de los asistentes, de forma voluntaria', 'La encuesta usó una escala de 1 a 5, que no permite expresar opiniones distintas', 'La pieza duró lo planificado, por lo que no hay ningún límite que mencionar', 'Quienes no respondieron podrían opinar distinto.'),
        ('abc', '{F} Un integrante dice: «los comentarios prueban que la música confundía a todo el público». ¿Qué corrección corresponde?', 'Decir que uno de los comentarios sugiere que la música pudo confundir, y probar quitarla', 'Mantener la afirmación porque hay un comentario que dice exactamente eso', 'Eliminar todos los comentarios porque son pocos y no permiten saber nada del público', 'Un comentario sugiere una hipótesis; no es prueba general.'),
        ('abc', '{F} El dato del proceso dice que solo 1 de 5 ensayos tuvo público de prueba. ¿Qué implica?', 'Que hubo poca evidencia previa y conviene probar más con público antes de decidir', 'Que el resultado final es inválido y debe repetirse la función completa con otro público', 'Que los ensayos sin público no sirven y no deben registrarse en la bitácora', 'Más pruebas con público darían mejor evidencia.'),
        ('=', 'Se aplicaron 3 encuestas con 16, 12 y 20 respuestas. ¿Cuántas respuestas hay en total?', '16+12+20', 'Se suman las respuestas de las tres encuestas.', ' respuestas'),
        ('abc', 'Una encuesta pide nombre y curso de cada persona que responde. ¿Qué conviene hacer?', 'No pedir datos personales si no son necesarios y evitar identificar a nadie', 'Pedir también el teléfono de cada persona para poder contactarla más adelante', 'Publicar los nombres junto a sus respuestas, para que se vea quién opinó cada cosa', 'La privacidad se cuida pidiendo solo lo necesario.'),
        ('abc', '{F} Un comentario escrito dice: «esa escena me hizo recordar algo muy triste de mi casa». ¿Qué hace el grupo?', 'Respetar la privacidad y comunicar el caso a una persona adulta responsable, sin comentarlo entre pares', 'Preguntar a la persona delante del curso qué fue lo que le pasó en su casa', 'Publicar el comentario para mostrar el impacto emocional que tuvo la pieza en el público', 'Un malestar real se comunica a un adulto responsable y no se expone.'),
    ],
    ctx=('abc', 'Un grupo recibe 5 respuestas de encuesta, todas de 5 puntos, y quiere anunciar «¡el 100 % del público la adoró!». ¿Qué corresponde?', 'Informar que respondieron 5 personas y que no se puede generalizar al total del público', 'Anunciarlo igual, porque el porcentaje es alto y eso demuestra el éxito de la pieza', 'Eliminar las respuestas de la encuesta para no exagerar los resultados del grupo', 'Un porcentaje con pocos datos exige declarar cuántas respuestas hay.'),
    sc=[
        ("En Teatro: ¿cómo se calcula el promedio de una escala?", "Sumando los puntos de todas las respuestas y dividiendo entre el número de respuestas", "Así se resume un conjunto de respuestas."),
        ("¿Qué límite tiene una encuesta voluntaria?", "Que respondan solo algunas personas, que pueden no representar a todo el público", "No se generaliza sin cuidado a todo el público."),
        ("¿Qué se hace con un comentario que revela un malestar real?", "Se comunica a una persona adulta responsable y no se comenta entre pares", "Se cuida la privacidad y el bienestar."),
    ],
    op=("Con los datos de la ficha de esta clase, escribe un breve informe de resultado de seis líneas: asistencia en porcentaje, porcentaje de respuestas, promedio de la escala, porcentaje de respuestas altas, un límite de los datos y una recomendación respaldada. Cuida no identificar a nadie.",
        "Asistencia: 80 % del aforo (32 de 40). Respondió el 50 % de los asistentes (16 de 32). Promedio de la escala: 4 puntos. Respuestas altas (4 o 5): 68 %. Límite: encuesta voluntaria con solo una parte del público. Recomendación: conservar las pausas y revisar la música, que un comentario señaló como confusa, con una prueba de público.",
        ["calcula los cuatro datos numéricos", "declara un límite de los datos", "propone una recomendación respaldada", "no identifica a personas"],
        ["informe de seis líneas con cálculos"],
        ["generalizar a todo el público", "no declarar el número de respuestas"],
        "Pregunta: «¿cuántas personas respondieron y qué falta saber?». Si no lo declara, pídele agregarlo."),
    reinforce="Haz una pregunta de una a cinco estrellas a cinco personas sobre una comida o una canción y calcula el promedio.",
    extend="Explica por qué un promedio alto con pocas respuestas es menos confiable que uno similar con muchas, y cómo lo informarías.",
)

# ============================================================ OAC-07, clase 5
F = ("Ficha 5 (hallazgos de una evaluación, de ejemplo, inventados) de la pieza «Mapa de silencios». "
     "H1: la música continua tapa las pausas (impacto 3, esfuerzo 1; escalas de 1 a 3). "
     "H2: la escena 3 tiene pausas demasiado largas (impacto 2, esfuerzo 1). "
     "H3: el cartel con la hora no se entiende (impacto 1, esfuerzo 1). "
     "H4: el vestuario se cambia en escena y retrasa el ritmo (impacto 2, esfuerzo 3). "
     "H5: dos integrantes dicen estar muy cansadas por los ensayos (impacto 3, esfuerzo 2; es un asunto de bienestar del equipo). "
     "Regla del grupo: se prioriza por impacto alto y esfuerzo bajo, y el bienestar siempre se atiende. Fecha de la próxima función: dentro de 10 días.")
build(
    O7, 5, F,
    use="Aprenderé a convertir una evaluación en un plan de mejora: priorizar hallazgos por impacto y esfuerzo, fijar metas verificables con responsable y plazo, hacer seguimiento y cerrar el ciclo, cuidando también el bienestar del equipo.",
    prior=["Sé evaluar con trazabilidad y datos.", "Sé dar y recibir retroalimentación.", "Sé planificar tareas con plazos."],
    explain=[
        "Evaluar sirve para mejorar. Un plan de mejora parte de los hallazgos, que son los problemas o logros que dejó la evaluación, y los prioriza. Una forma sencilla es comparar su impacto (cuánto mejora el propósito o el bienestar al resolverlo) con su esfuerzo (cuánto tiempo y recursos cuesta). Lo primero que se hace es lo de alto impacto y bajo esfuerzo; luego lo de alto impacto y alto esfuerzo, planificado; y lo de bajo impacto se deja para el final o se descarta.",
        "Cada acción del plan debe ser verificable: qué se hará, quién lo hará, para cuándo y cómo se sabrá que funcionó. Por ejemplo: «bajar la música a la mitad (responsable: regiduría, plazo: ensayo del jueves; verificación: el público de prueba oye las pausas)». Se hace seguimiento en ensayos posteriores y se cierra el ciclo: se compara el nuevo resultado con el anterior y se decide si la acción se mantiene, se ajusta o se descarta.",
        "El bienestar del equipo es parte de la evaluación del proceso. El cansancio extremo, la tensión entre integrantes o la presión excesiva no se tratan como detalles. Se acuerda una carga de trabajo razonable, descansos y formas de pedir ayuda, y se avisa a una persona adulta de confianza cuando alguien se siente mal. Una pieza no vale más que el cuidado de las personas que la hacen.",
    ],
    vocab=[("hallazgo", "problema o logro que deja una evaluación"), ("impacto", "cuánto mejora el propósito o el bienestar al resolver algo"), ("esfuerzo", "tiempo y recursos que cuesta resolver algo"), ("meta verificable", "acción con responsable, plazo y forma de comprobar su resultado"), ("cierre de ciclo", "comparar el nuevo resultado con el anterior y decidir qué se mantiene")],
    worked=[
        ("Priorizar", "Hallazgo X: impacto 3, esfuerzo 1. Hallazgo Y: impacto 3, esfuerzo 3. Hallazgo Z: impacto 1, esfuerzo 1. ¿Cuál se hace primero?", ["Se busca alto impacto y bajo esfuerzo.", "X tiene impacto 3 y esfuerzo 1."], "X"),
        ("Escribir una meta verificable", "Hallazgo: las transiciones son lentas. Escribe una meta.", ["Acción: acortar el cambio de utilería de 40 a 25 segundos.", "Responsable: regiduría; plazo: ensayo del viernes; verificación: se cronometra el cambio."], "Meta con acción, responsable, plazo y verificación"),
    ],
    mistakes=[("Escribir metas como «mejorar la voz».", "No se sabe qué hacer, quién, para cuándo ni cómo comprobarlo.", "Define acción, responsable, plazo y verificación."),
              ("Dejar el cansancio del equipo para el final porque «hay que terminar la obra».", "Un equipo agotado trabaja peor y puede enfermar o abandonar.", "Atiende el bienestar desde el comienzo del plan.")],
    T=[
        ('abc', 'En un plan de mejora, ¿qué es un hallazgo?', 'Un problema o logro que dejó la evaluación', 'La nota final que se pone a la pieza', 'La fecha de la función', 'Los hallazgos son lo que la evaluación encuentra.'),
        ('abc', '{F} Sin contar el bienestar, ¿qué hallazgos tienen esfuerzo bajo (1) e impacto de 2 o más, y se hacen primero?', 'H1 y H2, porque tienen esfuerzo 1 e impacto de 2 o más', 'H4, que tiene el mayor esfuerzo y por eso conviene dejarlo para el comienzo del plan', 'H3, que tiene el menor impacto y que se hace antes por ser el más fácil de todos', 'La regla pide impacto alto y esfuerzo bajo.'),
        ('abc', '{F} ¿Qué hallazgo tiene mayor impacto y menor esfuerzo?', 'H1, con impacto 3 y esfuerzo 1', 'H4, con impacto 2 y esfuerzo 3', 'H5, con impacto 3 y esfuerzo 2', 'H1 combina el máximo impacto con el esfuerzo más bajo.'),
        ('abc', '{F} ¿Cómo se trata el hallazgo H5?', 'Se atiende como asunto de bienestar y se conversa con una persona adulta de confianza', 'Se deja para después de la función, cuando ya no haya tareas pendientes en el plan', 'Se ignora porque es un asunto personal de las integrantes y no del equipo de trabajo', 'El bienestar del equipo siempre se atiende primero.'),
        ('abc', '{F} ¿Qué hallazgo se puede dejar para el final por su bajo impacto?', 'H3, el cartel con la hora', 'H1, la música que tapa las pausas', 'H5, el cansancio del equipo', 'Su impacto es 1, el más bajo de los hallazgos.'),
        ('=', '{F} Si la regla da puntos de prioridad igual a impacto menos esfuerzo, ¿cuántos puntos tiene H1?', '3-1', 'Se resta el esfuerzo al impacto.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos de prioridad (impacto menos esfuerzo) tiene H4?', '2-3', 'Se resta el esfuerzo al impacto, lo que da un valor negativo.', ' puntos'),
        ('abc', '¿Cuál es una meta verificable?', 'Bajar la música a la mitad antes del ensayo del jueves, con el público de prueba verificando que se oyen las pausas', 'Mejorar la música de la pieza para que el público la disfrute mucho más que antes', 'Hacerlo mejor la próxima vez, con más atención y cuidado en cada ensayo del grupo', 'Tiene una acción, un plazo y una verificación.'),
        ('abc', '{F} Quedan 10 días para la función. ¿Qué es lo más prudente con H4, que tiene esfuerzo 3?', 'Planificarlo con un responsable y probar una solución simple antes de la función', 'Ignorarlo porque es difícil y no hay tiempo para resolverlo antes de la función', 'Hacerlo la noche anterior a la función, cuando ya todo el equipo esté descansado', 'Alto esfuerzo se planifica con tiempo.'),
        ('abc', '¿Qué significa cerrar el ciclo de mejora?', 'Comparar el nuevo resultado con el anterior y decidir qué se mantiene, qué se ajusta y qué se descarta', 'Dar por terminada la pieza sin revisar nada de lo que se hizo en el proceso', 'Cambiar de propósito para empezar de nuevo con una pieza distinta y sin evaluación', 'El cierre vuelve a evaluar para decidir con evidencia.'),
        ('=', 'Un plan tiene 8 acciones; 6 se cumplieron en su plazo. ¿Qué porcentaje se cumplió?', '6*100//8', 'Se divide las acciones cumplidas entre el total y se pasa a porcentaje (se redondea hacia abajo).', ' %'),
        ('abc', '{F} Las dos integrantes cansadas piden descansar un ensayo. ¿Qué decisión respeta el plan?', 'Reprogramar el ensayo y repartir tareas, sin presionarlas', 'Obligarlas a asistir para no atrasarse, porque la fecha de la función está muy cerca', 'Eliminarlas de la pieza sin conversarlo, para que otras personas hagan sus tareas', 'El bienestar se atiende y el plan se ajusta.'),
        ('abc', 'Un grupo cumple su plan, pero en la nueva función el efecto no mejoró. ¿Qué conviene?', 'Revisar si la hipótesis era correcta y probar otro ajuste con evidencia', 'Culpar al equipo que ejecutó la acción por no haberla hecho de la manera correcta', 'Repetir la misma acción con más fuerza, para que el efecto sea más notorio', 'Un plan se ajusta con nuevos datos.'),
    ],
    ctx=('abc', 'Un curso termina una evaluación con diez hallazgos. Un integrante propone corregirlos todos en una semana. ¿Qué respuesta es más sensata?', 'Priorizar por impacto y esfuerzo, y fijar un número de acciones posibles con responsables y plazos', 'Hacer los diez hallazgos a la vez, sin responsables, para terminar en una sola semana', 'Elegir los hallazgos que le gustan más a cada integrante y trabajar en esos primero', 'La priorización evita sobrecargar al equipo y asegura resultados.'),
    sc=[
        ("En Teatro: ¿qué se prioriza primero en un plan de mejora?", "Lo de alto impacto y bajo esfuerzo", "Se obtiene más mejora con menos costo."),
        ("¿Qué tiene una meta verificable?", "Acción, responsable, plazo y forma de comprobar el resultado", "Así se puede saber si se cumplió."),
        ("¿Qué se hace si alguien del equipo se siente muy cansado o mal?", "Se atiende su bienestar y se avisa a una persona adulta de confianza", "El cuidado de las personas va antes que la pieza."),
    ],
    op=("Con los hallazgos de la ficha (o con otros de una pieza inventada), construye un plan de mejora de cuatro acciones: prioriza, escribe cada meta verificable (acción, responsable, plazo y verificación) y agrega una acción de bienestar del equipo. Indica cómo cerrarías el ciclo.",
        "1) Bajar la música a la mitad (regiduría, ensayo del jueves; el público de prueba oye las pausas). 2) Acortar las pausas de la escena 3 a 3 segundos (dirección, viernes; se cronometra). 3) Sacar el cartel de la hora (diseño, lunes; menos confusión en la encuesta). 4) Bienestar: ensayos de 60 minutos con descanso y una persona adulta como contacto. Cierre: comparar la encuesta de la función 2 con la función 1.",
        ["cuatro acciones priorizadas", "cada meta es verificable", "incluye una acción de bienestar", "indica cómo cerrar el ciclo"],
        ["plan de mejora de cuatro acciones"],
        ["metas sin plazo ni verificación", "dejar el bienestar fuera"],
        "Pregunta: «¿cómo sabrás que funcionó?». Si no hay respuesta, pídele agregar una verificación."),
    reinforce="Elige un hábito que quieras mejorar (estudio, sueño) y escribe una meta verificable con plazo.",
    extend="Explica por qué cerrar el ciclo de mejora vuelve a una evaluación más útil que solo detectar problemas.",
)

# ============================================================ OAC-08, clase 1
F = ("Ficha 1 (actividades y habilidades de ejemplo, inventadas). Un taller de teatro del curso hizo estas actividades: "
     "A1: ensayar una partitura de acciones con duración y tensión. "
     "A2: ponerse de acuerdo en el propósito de una pieza entre cinco personas. "
     "A3: llamar las pistas de luz y sonido durante una función, con el tiempo exacto. "
     "A4: recibir un comentario duro de un par y decidir qué cambiar. "
     "A5: hablar ante 40 personas con voz clara y sin forzarla. "
     "A6: armar un plan con presupuesto de $30.000 y fecha de estreno. "
     "Habilidades de ejemplo para vincular: H1, comunicación oral y cuidado de la voz; H2, trabajo en equipo y negociación; H3, atención al detalle y puntualidad; H4, recibir retroalimentación; H5, planificación y gestión de recursos; H6, precisión y repetición de una rutina.")
build(
    O8, 1, F,
    use="Aprenderé a reconocer qué habilidades desarrolla el trabajo teatral (comunicación, trabajo en equipo, escucha, gestión, creatividad, manejo de la presión) y a explicar cómo pueden transferirse a contextos laborales, profesionales y de desarrollo personal.",
    prior=["Sé evaluar una pieza y un proceso.", "Sé trabajar con roles en un montaje.", "Sé reconocer mis propias fortalezas y dificultades."],
    explain=[
        "Las habilidades son capacidades que se aprenden y se pueden usar en muchas situaciones. El trabajo teatral desarrolla varias: comunicación oral (hablar claro, cuidar la voz), escucha activa (atender para responder), trabajo en equipo y negociación (acordar con otras personas), creatividad y resolución de problemas, planificación y gestión de recursos (tiempo, dinero, materiales), precisión y disciplina (repetir una rutina con exactitud), y manejo de la presión (actuar o decidir con calma ante un público). Algunas son técnicas, propias del teatro, y otras son transversales, útiles en cualquier ámbito.",
        "Una habilidad es transferible cuando se puede usar en otro contexto. Por ejemplo, la comunicación oral sirve en una entrevista de trabajo, en una exposición de clase o en una reunión con vecinos; la planificación con presupuesto sirve para organizar un evento o un emprendimiento. Para saber si una habilidad es transferible se pregunta: ¿qué hacía yo en el taller, y en qué otra situación necesitaría hacer algo parecido? La respuesta debe nombrar una acción concreta, no una frase general como «soy bueno con la gente».",
        "Reconocer habilidades no significa exagerar ni compararse. Cada persona tiene un punto de partida distinto, y algunas habilidades se desarrollan más lentamente. Nadie está obligado a mostrar lo que le incomoda. Se habla de lo que se hace y se aprende, no de los cuerpos ni de las personas como mejores o peores.",
    ],
    vocab=[("habilidad", "capacidad que se aprende y puede usarse en muchas situaciones"), ("habilidad transferible", "habilidad que se puede usar en otro contexto"), ("escucha activa", "atención real a lo que dice otra persona para responderle"), ("resolución de problemas", "buscar y probar soluciones ante un obstáculo"), ("manejo de la presión", "capacidad de actuar con calma ante exigencias o público")],
    worked=[
        ("Vincular actividad y habilidad", "Actividad: llamar las pistas de luz con el tiempo exacto durante una función. ¿Qué habilidad desarrolla?", ["Exige estar atento y no equivocarse en el momento.", "Desarrolla atención al detalle y puntualidad."], "Atención al detalle y puntualidad"),
        ("Pensar en otro contexto", "La habilidad: acordar un propósito entre cinco personas. ¿Dónde sirve fuera del teatro?", ["Hay que escuchar, proponer y llegar a acuerdos.", "Sirve en un trabajo en equipo, en un proyecto del curso o en una junta de vecinos."], "En trabajos en equipo, proyectos o juntas de vecinos"),
    ],
    mistakes=[("Escribir «tengo buena actitud» como habilidad.", "Es una frase general que no dice qué se hace.", "Nombra una acción concreta y su evidencia."),
              ("Creer que solo sirven las habilidades de actuar.", "El trabajo de dirección, regiduría, diseño y producción desarrolla habilidades muy útiles.", "Mira todos los roles del montaje.")],
    T=[
        ('abc', 'En desarrollo personal, ¿qué es una habilidad transferible?', 'Una habilidad que se puede usar en otro contexto', 'Una habilidad que solo sirve en el teatro', 'Una habilidad que se hereda y no cambia con la práctica', 'Es transferible cuando sirve fuera del lugar donde se aprendió.'),
        ('abc', '{F} ¿Qué habilidad desarrolla A5, hablar ante 40 personas con voz clara y sin forzarla?', 'H1, comunicación oral y cuidado de la voz', 'H5, planificación y gestión de recursos', 'H6, precisión y repetición de una rutina', 'Hablar con claridad ante un público es comunicación oral.'),
        ('abc', '{F} ¿Qué habilidad desarrolla A2, ponerse de acuerdo en el propósito entre cinco personas?', 'H2, trabajo en equipo y negociación', 'H3, atención al detalle y puntualidad', 'H4, recibir retroalimentación', 'Llegar a acuerdos entre varias personas es trabajo en equipo.'),
        ('abc', '{F} ¿Qué habilidad desarrolla A4, recibir un comentario duro y decidir qué cambiar?', 'H4, recibir retroalimentación', 'H1, comunicación oral', 'H5, planificación', 'Escuchar y decidir qué hacer con un comentario es esa habilidad.'),
        ('abc', '{F} ¿Qué habilidad desarrolla A6, armar un plan con presupuesto y fecha?', 'H5, planificación y gestión de recursos', 'H2, trabajo en equipo y negociación entre varias personas del grupo', 'H3, atención al detalle y puntualidad en el momento de una función', 'Presupuesto y fechas son gestión de recursos.'),
        ('abc', '{F} ¿Qué habilidad desarrolla A1, ensayar la partitura con duración y tensión?', 'H6, precisión y repetición de una rutina', 'H4, recibir retroalimentación', 'H2, trabajo en equipo', 'Repetir una secuencia con exactitud entrena la precisión.'),
        ('=', '{F} El presupuesto de A6 es de $30.000. Si se gastan $18.500 en materiales y $6.000 en traslados, ¿cuánto queda?', '30000-18500-6000', 'Se restan los gastos al presupuesto.', ' pesos'),
        ('abc', '¿Cuál es una descripción concreta de una habilidad transferible?', 'Planifiqué los ensayos de un grupo de cinco personas con fechas y responsables', 'Soy una persona muy buena para todo lo que me propongo, y por eso me eligen', 'Me gusta mucho estar con gente y conversar con las personas del taller de teatro', 'Una descripción concreta nombra una acción y su contexto.'),
        ('abc', '{F} A3 exige llamar las pistas con el tiempo exacto. ¿En qué otro contexto sirve esa habilidad?', 'En un trabajo donde hay que coordinar tareas con horarios precisos', 'Solo en otra función de teatro, donde también se llamen pistas de luz y sonido', 'En ningún otro contexto, porque es una habilidad propia de quienes trabajan en escena', 'La puntualidad y la atención al detalle son transferibles.'),
        ('abc', 'Una estudiante dice: «yo no tengo habilidades porque no actúo». ¿Qué respuesta es adecuada?', 'Que dirigir, regir, diseñar o producir también desarrolla habilidades útiles', 'Que tiene razón, porque solo actuar desarrolla habilidades útiles para la vida adulta', 'Que debe aprender a actuar antes de poder decir que tiene habilidades teatrales', 'Cada rol del montaje desarrolla habilidades.'),
        ('abc', 'Un grupo compara habilidades diciendo que «los que actúan son mejores personas». ¿Qué corrección corresponde?', 'Hablar de las habilidades que se desarrollan y no clasificar a las personas como mejores o peores', 'Mantenerlo porque es una opinión mayoritaria del curso sobre quienes actúan en escena', 'Decirlo solo en voz baja para que nadie se sienta mal por la comparación entre roles', 'Las habilidades se describen y no jerarquizan a las personas.'),
        ('=', 'Una persona dedicó 4 horas semanales al taller durante 10 semanas. ¿Cuántas horas suman?', '4*10', 'Se multiplican las horas semanales por las semanas.', ' horas'),
        ('abc', '{F} Una compañera dice: «A5 me da miedo y no quiero hacerlo delante de todos». ¿Qué decisión respeta su proceso?', 'Empezar con grupos pequeños y ejercicios de voz suaves, sin forzarla', 'Obligarla a presentarse delante de todo el curso, para que supere pronto su miedo', 'Dejarla fuera del taller hasta que ya no sienta miedo de hablar ante otras personas', 'Las habilidades se desarrollan a un ritmo propio y sin exponer a nadie.'),
    ],
    ctx=('abc', 'Un estudiante escribe en su cuaderno: «gracias al teatro aprendí a hablar en público». ¿Cómo lo mejora para que sirva como evidencia?', 'Agregar una situación concreta, como «presenté el plan del montaje ante 30 personas y respondí preguntas»', 'Subrayarlo con otro color para que se vea más importante dentro del portafolio', 'Cambiarlo por «soy muy bueno hablando» para que suene más seguro ante quien lo lea', 'Una evidencia nombra una situación, una acción y un resultado.'),
    sc=[
        ("En Teatro: ¿qué es una habilidad transferible?", "Una habilidad que se puede usar en otros contextos", "Sirve más allá de donde se aprendió."),
        ("¿Qué es la escucha activa?", "Atender de verdad a lo que dice otra persona para responderle", "Es una habilidad útil dentro y fuera del teatro."),
        ("¿Se puede obligar a alguien a mostrar una habilidad que le incomoda?", "No, cada persona avanza a su ritmo y sin exponerse", "El respeto está antes que la exhibición."),
    ],
    op=("Haz un mapa de tres habilidades que hayas desarrollado o que quieras desarrollar con el teatro. Para cada una escribe una actividad concreta del taller, la habilidad con su nombre y dos contextos distintos (uno laboral o profesional y otro personal o de estudio) donde la usarías. No hables de cuerpos ni compares con otras personas.",
        "1) Actividad: llamar las pistas de una función. Habilidad: atención al detalle y puntualidad. Contextos: coordinar turnos en un trabajo; llegar a tiempo a un examen. 2) Actividad: acordar el propósito con el grupo. Habilidad: negociación. Contextos: una reunión de vecinos; un trabajo grupal. 3) Actividad: hablar ante el curso. Habilidad: comunicación oral. Contextos: una entrevista; defender una idea en casa.",
        ["tres actividades concretas", "habilidades bien nombradas", "dos contextos distintos por habilidad", "no compara con otras personas"],
        ["mapa de tres habilidades con contextos"],
        ["usar frases generales como «tengo buena actitud»", "compararse con otras personas"],
        "Pregunta: «¿qué hacías exactamente?». Si no es una acción concreta, pídele precisarla."),
    reinforce="Anota dos cosas que hiciste esta semana y qué habilidad desarrollaste en cada una.",
    extend="Explica por qué las habilidades de dirección o gestión de un montaje pueden ser tan valiosas como las de actuación.",
)

# ============================================================ OAC-08, clase 2
F = ("Ficha 2 (ficha de investigación de ejemplo, inventada). Pregunta: «¿qué trabajos existen alrededor del teatro y qué formación suelen pedir?». "
     "Fuente 1: sitio de orientación vocacional de una institución educativa, con autoría y fecha. "
     "Fuente 2: entrevista a una persona que trabaja como iluminadora, publicada con su permiso. "
     "Fuente 3: publicación anónima que dice «ser actor da mucha plata». "
     "Oficios y profesiones mencionados: actuación, dirección, dramaturgia, diseño de luz y sonido, regiduría, producción y gestión cultural, docencia y mediación cultural, teatro aplicado a educación o comunidad, locución y comunicación oral. "
     "Dato de ejemplo para practicar (no real): una persona hace 3 funciones al mes y recibe $40.000 por función.")
build(
    O8, 2, F,
    use="Aprenderé a investigar oficios y profesiones relacionados con el teatro con fuentes confiables, a distinguir roles artísticos, técnicos, de gestión y de educación o comunidad, y a anotar la formación y las condiciones de trabajo sin inventar datos.",
    prior=["Sé evaluar la confiabilidad de una fuente.", "Conozco los roles de un montaje.", "Sé que no se inventan cifras."],
    explain=[
        "Alrededor del teatro existen muchos trabajos. En el campo artístico están la actuación, la dirección y la dramaturgia. En el campo técnico están el diseño de luz y sonido, la escenografía, el vestuario y la regiduría. En gestión están la producción y la gestión cultural, que organizan recursos, permisos, presupuesto y comunicación. En educación y comunidad están la docencia, la mediación cultural y el teatro aplicado, que usa técnicas teatrales en escuelas, organizaciones o proyectos sociales. Las habilidades teatrales también se usan en locución, oratoria, comunicación y formación de equipos.",
        "Para investigar un oficio se usan fuentes confiables: sitios de instituciones educativas y de orientación vocacional, organismos públicos, asociaciones del sector y entrevistas hechas con permiso a personas que trabajan en él. Se anota qué hace esa persona, qué formación suele tener (estudios superiores, talleres, trayectoria en compañías), en qué lugares trabaja y cómo se organiza su trabajo, que a veces es por contrato, por honorarios o por proyectos. Los ingresos varían mucho; no se afirman cifras sin una fuente confiable, y se rotulan como «de ejemplo» cuando se practica.",
        "Una investigación honesta contrasta al menos dos fuentes y declara lo que no se pudo comprobar. Las entrevistas se hacen con consentimiento y sin pedir datos privados. Las ideas que «suenan bien» pero no tienen fuente, como que un oficio da mucho dinero o ninguno, se tratan como hipótesis. La elección de una carrera o un camino es personal y no se presiona a nadie.",
    ],
    vocab=[("oficio", "trabajo que se aprende y se ejerce con práctica"), ("profesión", "ocupación que suele requerir estudios formales"), ("gestión cultural", "organización de recursos y proyectos artísticos"), ("teatro aplicado", "uso de técnicas teatrales en educación, comunidad u organizaciones"), ("honorarios", "pago por un servicio o proyecto, sin contrato laboral permanente")],
    worked=[
        ("Ubicar un oficio", "«Persona que decide qué luz usar en cada escena». ¿Qué oficio es y en qué campo está?", ["Decide un aspecto técnico de la puesta en escena.", "Es diseño de luz, del campo técnico."], "Diseño de luz, campo técnico"),
        ("Tratar una afirmación sin fuente", "Una página anónima dice «los actores ganan millones». ¿Qué haces?", ["No tiene autoría ni evidencia.", "La trato como hipótesis y busco fuentes confiables."], "La trato como hipótesis y busco fuentes confiables"),
    ],
    mistakes=[("Afirmar cifras de sueldo sin fuente.", "Los ingresos varían mucho y las cifras inventadas pueden engañar a otra persona.", "Usa fuentes confiables o rotula como «de ejemplo»."),
              ("Pensar que trabajar en teatro es solo actuar.", "Hay muchos roles técnicos, de gestión y educativos.", "Investiga todo el campo antes de decidir.")],
    T=[
        ('abc', 'En el campo del teatro, ¿qué hace la gestión cultural?', 'Organiza recursos, permisos, presupuesto y comunicación de proyectos artísticos', 'Interpreta personajes en escena y se encarga de memorizar los textos de la obra', 'Escribe los textos dramáticos y decide qué ocurre en cada escena de la obra', 'La gestión organiza lo necesario para que un proyecto ocurra.'),
        ('abc', '{F} ¿Qué fuente es la más débil para saber cuánto gana una persona?', 'La fuente 3, porque es anónima y sin evidencia', 'La fuente 1, porque tiene autoría y fecha', 'La fuente 2, porque entrevista a una iluminadora', 'Una frase anónima no permite verificar.'),
        ('abc', '{F} ¿En qué campo está el diseño de luz y sonido?', 'En el campo técnico', 'En el campo artístico de la actuación', 'En el campo de la gestión cultural', 'La luz y el sonido son recursos técnicos de la puesta en escena.'),
        ('abc', '{F} ¿Qué oficio usa técnicas teatrales en una escuela o una organización?', 'Teatro aplicado', 'Regiduría', 'Dramaturgia', 'Es el uso de técnicas teatrales en educación o comunidad.'),
        ('=', '{F} Con el dato de ejemplo, ¿cuánto recibe una persona en un mes con 3 funciones de $40.000 cada una?', '3*40000', 'Se multiplica el número de funciones por el pago de cada una.', ' pesos'),
        ('abc', '{F} ¿Por qué el dato de ejemplo no sirve para afirmar cuánto gana un actor en la realidad?', 'Porque está rotulado como no real y solo sirve para practicar', 'Porque es un dato verdadero para todas las personas', 'Porque viene de una fuente oficial', 'Los datos de ejemplo no describen el mundo real.'),
        ('abc', '¿Qué fuente es más confiable para investigar un oficio?', 'Un sitio de orientación de una institución educativa, con autoría y fecha', 'Un comentario anónimo en una red social, que afirma cuánto gana la gente del teatro', 'Un video sin créditos ni fecha, que muestra a una persona que habla de su trabajo', 'La autoría y la fecha permiten verificar.'),
        ('abc', '{F} Quieres hacer una entrevista a una iluminadora de tu ciudad. ¿Qué paso corresponde?', 'Pedir su consentimiento, explicar para qué sirve y no preguntar datos privados', 'Grabarla sin avisarle, para que su respuesta sea más natural y no la prepare antes', 'Publicar sus datos de contacto en el informe para que otras personas puedan escribirle', 'La entrevista se hace con consentimiento y respeto por la privacidad.'),
        ('abc', 'Una persona trabaja por honorarios. ¿Qué significa?', 'Cobra por un servicio o proyecto, sin un contrato laboral permanente', 'Recibe un sueldo fijo todos los meses, con contrato y vacaciones pagadas por la institución', 'Trabaja sin cobrar, porque presta su servicio para ayudar a otras personas del medio', 'Los honorarios pagan servicios o proyectos puntuales.'),
        ('abc', '{F} Un compañero dice que «los trabajos del teatro no sirven para vivir». ¿Qué respuesta es más prudente?', 'Que depende de cada oficio y situación y que conviene revisar fuentes confiables', 'Que tiene razón y no vale la pena investigar más sobre este tipo de trabajos', 'Que todos los oficios del teatro ganan mucho dinero y no hace falta revisar fuentes', 'Una afirmación general se contrasta con datos.'),
        ('=', 'Una investigación revisó 8 fuentes y descartó 2 por no tener autoría. ¿Qué porcentaje de las fuentes usó?', '6*100//8', 'Se dividen las fuentes usadas entre el total y se pasa a porcentaje.', ' %'),
        ('abc', 'Una estudiante quiere estudiar teatro y su familia prefiere otra carrera. ¿Qué es lo más adecuado?', 'Conversar con calma, presentar lo que investigó y buscar apoyo de una persona adulta orientadora', 'Esconderles la información que investigó para evitar un conflicto con su familia', 'Decidir sin informarse, porque es una decisión personal y no hay nada que averiguar', 'La decisión es personal y se puede conversar con apoyo.'),
        ('abc', '{F} Un estudiante propone usar el dato de ejemplo para concluir que «todos los actores reciben $40.000 por función». ¿Qué problema tiene?', 'Generaliza un dato de ejemplo a toda una profesión', 'Está bien porque 40.000 es un valor razonable', 'Que $40.000 es una cifra demasiado baja para ser creíble', 'Un dato de ejemplo no describe la realidad.'),
    ],
    ctx=('abc', 'Un curso investiga «teatro y comunidad». Un grupo cita un sitio de una organización con fecha y autoría; otro cita un post sin fuente. ¿Cuál es mejor base para decidir qué incluir en su informe?', 'El sitio con autoría y fecha, y contrastarlo con otra fuente', 'El post, porque es más reciente', 'Ninguno, porque nada se puede investigar en línea', 'Las fuentes con autoría y fecha son mejores y se contrastan.'),
    sc=[
        ("En Teatro: ¿qué son los honorarios?", "El pago por un servicio o proyecto, sin contrato laboral permanente", "Es una forma común de pago en trabajos por proyecto."),
        ("¿Qué se hace con una cifra sin fuente?", "Se trata como hipótesis y se busca una fuente confiable", "No se afirman cifras sin respaldo."),
        ("¿Qué se pide antes de entrevistar a una persona?", "Su consentimiento", "Se respeta su voluntad y privacidad."),
    ],
    op=("Elige un oficio relacionado con el teatro (por ejemplo, regiduría, mediación cultural, dramaturgia o producción). Escribe una ficha de investigación con qué hace, en qué campo está, qué formación suele pedir (según una fuente que describas como de ejemplo), dos fuentes con su confiabilidad y una pregunta que quedaría pendiente. No inventes cifras de ingresos.",
        "Oficio: producción. Qué hace: organiza recursos, permisos, presupuesto y comunicación. Campo: gestión cultural. Formación: estudios superiores en gestión o artes, o experiencia en compañías (fuente de ejemplo: un sitio de orientación). Fuentes: un sitio institucional con autoría y fecha (confiable) y una entrevista con permiso (confiable). Pendiente: cómo se organizan los contratos en proyectos pequeños.",
        ["describe qué hace y su campo", "indica formación según una fuente rotulada", "evalúa la confiabilidad de dos fuentes", "no inventa cifras"],
        ["ficha de investigación de un oficio"],
        ["afirmar sueldos sin fuente", "no citar fuentes"],
        "Pregunta: «¿de qué fuente sacaste ese dato?». Si no tiene fuente, pídele quitarlo o rotularlo como hipótesis."),
    reinforce="Pregunta a una persona adulta de tu casa qué estudió y cómo llegó a su trabajo, y anota dos datos sin pedir su sueldo.",
    extend="Explica por qué contrastar fuentes protege de decidir una carrera por frases como «da mucho dinero» o «no sirve para nada».",
)

# ============================================================ OAC-08, clase 3
F = ("Ficha 3 (dos descripciones de un logro, de ejemplo, inventadas), escritas para un portafolio. "
     "Descripción 1: «Soy una persona muy responsable y buena para organizar.» "
     "Descripción 2: «En un montaje del curso fui regidora: llamé 18 pistas de luz y sonido en una función de 15 minutos, coordiné a 4 personas y la función comenzó a la hora prevista (situación, acción y resultado).» "
     "Materiales posibles del portafolio: la hoja técnica de la función (hecha por el grupo), el programa con créditos, una fotografía del equipo donde aparecen 5 personas, una reseña escrita por una persona del público (con su permiso) y una música usada en la función, compuesta por una compañera.")
build(
    O8, 3, F,
    use="Aprenderé a demostrar con evidencia mis habilidades teatrales (portafolio, currículum, método situación-acción-resultado), a pedir consentimiento para usar imágenes o trabajos de otras personas y a presentarme con honestidad.",
    prior=["Sé mapear habilidades transferibles.", "Sé investigar oficios.", "Sé pedir consentimiento y citar autoría."],
    explain=[
        "Una habilidad se demuestra con evidencia: algo que otra persona pueda ver o verificar. En un portafolio se reúnen muestras de trabajo, como una hoja técnica, un programa, un plan de producción, un guion escrito o una reseña. En un currículum se resumen estudios, experiencias y habilidades. Para describir un logro se usa el método situación-acción-resultado: qué situación había, qué hice yo y qué resultado se obtuvo, con datos cuando se pueda. «Llamé 18 pistas en una función de 15 minutos y la función comenzó a tiempo» es evidencia; «soy responsable» es solo una afirmación.",
        "Ser honesto es parte del trabajo profesional. Se describe lo que realmente se hizo, sin inflar el rol ni quitar mérito a otras personas. Cuando un trabajo fue colectivo, se dice cuál fue la parte propia. Si se incluye material de otras personas (una foto, una música, un texto), se pide su consentimiento y se cita su autoría. Las fotos de personas, especialmente de menores de 18 años, se incluyen solo con su consentimiento y el de su apoderado.",
        "El portafolio también cuida la privacidad: no incluye direcciones ni datos personales innecesarios, y se comparte solo con quien se decide compartirlo. Presentarse a oportunidades (estudios, prácticas, trabajos) implica a veces entrevistas; para prepararlas se ensaya con una persona de confianza y se cuenta la experiencia con ejemplos concretos.",
    ],
    vocab=[("evidencia", "muestra que otra persona puede ver o verificar"), ("portafolio", "conjunto de muestras de trabajo"), ("currículum", "resumen de estudios, experiencias y habilidades"), ("situación-acción-resultado", "método para describir un logro con contexto, lo hecho y lo logrado"), ("consentimiento", "permiso libre e informado para usar algo de una persona")],
    worked=[
        ("Reescribir con evidencia", "«Soy buena para hablar en público». Reescribe con situación, acción y resultado.", ["Situación: presenté un proyecto ante el curso.", "Acción y resultado: hablé 5 minutos, respondí 3 preguntas y el curso aprobó seguir con el plan."], "Presenté un proyecto 5 minutos ante el curso, respondí 3 preguntas y se aprobó el plan"),
        ("Decidir sobre una foto", "Una foto del equipo muestra a 5 personas, dos menores de 18 años. ¿Qué haces antes de incluirla?", ["Se necesita el consentimiento de las personas.", "Para las menores de 18 años también se pide la autorización de su apoderado."], "Pedir consentimiento a todas y autorización de apoderados para menores"),
    ],
    mistakes=[("Escribir «soy responsable» sin ningún ejemplo.", "Es una afirmación que no se puede verificar.", "Cuenta una situación, tu acción y el resultado."),
              ("Quedarse con el crédito de un trabajo colectivo.", "Es deshonesto y puede perjudicar tu credibilidad.", "Indica cuál fue tu parte y reconoce al equipo.")],
    T=[
        ('abc', 'En un portafolio, ¿qué es la evidencia?', 'Una muestra que otra persona puede ver o verificar', 'Una frase que dice que eres muy bueno en lo que haces, sin ningún dato que la respalde', 'La opinión de un amigo cercano sin ningún dato ni muestra de lo que hiciste', 'La evidencia permite verificar lo que se afirma.'),
        ('abc', '{F} ¿Qué descripción tiene evidencia?', 'La descripción 2, porque indica situación, acción y resultado con datos', 'La descripción 1, porque habla de ser responsable y buena para organizar cosas', 'Ninguna de las dos, porque una descripción de un logro no puede tener evidencia', 'La descripción 2 cuenta lo que hizo y lo logrado.'),
        ('=', '{F} En la descripción 2, la función dura 15 minutos y se llamaron 18 pistas. ¿Cuántos segundos hay en promedio por pista?', '15*60//18', 'Se pasan los 15 minutos a segundos y se divide entre las 18 pistas.', ' segundos'),
        ('abc', '{F} ¿Qué parte de la descripción 2 es la acción?', 'Llamé 18 pistas y coordiné a 4 personas', 'La función comenzó a la hora prevista', 'En un montaje del curso', 'La acción es lo que la persona hizo.'),
        ('abc', '{F} ¿Qué parte de la descripción 2 es el resultado?', 'La función comenzó a la hora prevista', 'Llamé 18 pistas y coordiné a 4 personas', 'En un montaje del curso fui regidora', 'El resultado es lo que se logró.'),
        ('abc', '{F} ¿Qué se necesita antes de incluir la fotografía del equipo en el portafolio?', 'Consentimiento de las cinco personas y, en caso de menores de 18 años, de su apoderado', 'Nada, porque es una foto del curso y todas las personas ya saben que aparecen en ella', 'Solo el permiso de quien tomó la foto, que es la persona dueña de la imagen', 'Cada persona decide sobre su imagen.'),
        ('abc', '{F} ¿Qué se debe hacer con la música compuesta por una compañera?', 'Pedirle permiso y citar su autoría', 'Usarla sin avisar porque se usó en la función', 'Decir que la compuso quien arma el portafolio', 'La autoría es de la compañera y se reconoce.'),
        ('abc', '{F} Una reseña escrita por una persona del público se incluye en el portafolio. ¿Qué corresponde?', 'Contar con su permiso y citar su autoría', 'Cambiarla para que sea más elogiosa', 'Quitar su nombre sin avisarle', 'No se modifica ni se usa sin permiso.'),
        ('=', 'Un portafolio tiene 5 materiales y 3 tienen autorización de uso. ¿Qué porcentaje tiene autorización?', '3*100//5', 'Se divide los materiales autorizados entre el total y se pasa a porcentaje.', ' %'),
        ('abc', 'En un trabajo grupal, una persona dice en su currículum que «dirigió la obra del curso» aunque fue una dirección compartida entre cuatro. ¿Qué problema tiene?', 'Infla su rol y no reconoce la parte de las demás personas', 'Está correcto, porque participó en la dirección', 'Que escribió la palabra dirección', 'Es honesto indicar el rol real y compartido.'),
        ('abc', 'Para una entrevista, una estudiante ensaya cómo contar su experiencia con ejemplos. ¿Qué es lo más útil?', 'Preparar una o dos historias con situación, acción y resultado', 'Aprender frases generales que impresionen, para repetirlas en cualquier entrevista', 'No ensayar para que la respuesta suene natural y no parezca algo aprendido de memoria', 'Los ejemplos concretos respaldan lo que se afirma.'),
        ('=', 'Una persona quiere presentar 8 muestras en su portafolio y ya obtuvo consentimiento para 5. ¿Cuántas le faltan?', '8-5', 'Se restan las muestras con permiso al total.', ' muestras'),
        ('abc', 'Una persona recibe una oferta de un supuesto casting que pide enviar fotos personales sin ropa «para evaluar la imagen». ¿Qué corresponde?', 'No enviar nada y contar lo ocurrido a una persona adulta de confianza', 'Enviar las fotos si el trabajo parece bueno y el productor promete mucha visibilidad', 'Pedir a una amiga que las envíe por ella, para no tener contacto directo con el productor', 'Una solicitud así es una señal de riesgo y se informa a un adulto de confianza.'),
    ],
    ctx=('abc', 'Un estudiante quiere incluir en su portafolio un video del ensayo general donde aparecen ocho personas, entre ellas menores de 18 años. ¿Qué paso corresponde?', 'Pedir consentimiento a cada persona y, para menores, autorización de su apoderado, o usar solo un fragmento sin ellas', 'Subirlo al portafolio porque fue una actividad del colegio y todas las personas lo saben', 'Subirlo primero y retirar el video si alguna persona lo pide más adelante', 'Se necesita consentimiento antes de difundir imágenes.'),
    sc=[
        ("En Teatro: ¿qué cuenta el método situación-acción-resultado?", "El contexto, lo que hice yo y lo que se logró", "Permite describir un logro con evidencia."),
        ("¿Qué se pide antes de incluir una foto de otras personas en un portafolio?", "Su consentimiento, y el de apoderados para menores de 18 años", "Cada persona decide sobre su imagen."),
        ("¿Qué se hace con un trabajo colectivo?", "Se indica cuál fue la parte propia y se reconoce al equipo", "Es honesto y respeta a las demás personas."),
    ],
    op=("Escribe tres descripciones de logros para tu portafolio usando situación, acción y resultado, a partir de actividades reales o inventadas del taller. Luego escribe una lista de tres materiales que incluirías, indicando cuál necesita consentimiento o autoría. No incluyas datos privados.",
        "1) Situación: ensayo de una escena de 10 minutos. Acción: llevé el registro de tiempos de 5 ensayos. Resultado: reduje en 2 minutos la duración. 2) Situación: función escolar. Acción: preparé la hoja técnica. Resultado: la función comenzó a la hora. 3) Situación: coevaluación. Acción: di comentarios con protocolo a 3 compañeros. Resultado: dos cambiaron su escena. Materiales: hoja técnica (propia), programa (créditos del grupo), foto del equipo (requiere consentimiento).",
        ["tres descripciones con situación, acción y resultado", "lista de materiales con consentimiento o autoría", "no infla su rol", "no incluye datos privados"],
        ["tres descripciones y una lista de materiales"],
        ["afirmaciones sin evidencia", "usar fotos sin consentimiento"],
        "Pregunta: «¿qué hiciste tú y qué se logró?». Si falta algo, pídele precisarlo."),
    reinforce="Cuenta a una persona de tu casa algo que lograste este año con situación, acción y resultado.",
    extend="Explica por qué una descripción con datos y una con adjetivos generan distinta confianza en quien las lee.",
)

# ============================================================ OAC-08, clase 4
F = ("Ficha 4 (casos de ejemplo, inventados). "
     "Caso A: una compañía ficticia ofrece a un grupo de estudiantes una función en un centro cultural y propone pagar «una exposición de su talento», sin contrato ni horarios escritos. "
     "Caso B: una escuela ofrece a una persona dar un taller de teatro de 8 sesiones de 90 minutos, pagando honorarios de $25.000 por sesión (cifra de ejemplo), con un acuerdo por escrito. "
     "Caso C: una persona recibe un mensaje de un supuesto productor que le pide enviar fotos personales sin ropa «para el casting» y le dice que no cuente a nadie. "
     "Datos del plan personal de ejemplo: ingresos del taller, 8 sesiones por $25.000; gastos para preparar el taller, $38.000. "
     "Bienestar: después de una función, una estudiante siente mucha ansiedad y no logra dormir.")
build(
    O8, 4, F,
    use="Aprenderé a relacionar las habilidades teatrales con contextos laborales y de desarrollo personal, a reconocer condiciones laborales justas (acuerdos por escrito, pagos, derechos de autor, seguridad) y ofertas engañosas, y a armar un plan personal de acción que cuide el bienestar.",
    prior=["Sé investigar oficios con fuentes.", "Sé demostrar habilidades con evidencia.", "Conozco el consentimiento y los derechos de autor."],
    explain=[
        "Las habilidades teatrales se usan en contextos laborales (compañías, escuelas, centros culturales, medios, empresas), profesionales (estudios superiores, trabajo independiente) y de desarrollo personal (confianza, expresión, manejo de nervios, vínculos). En el trabajo independiente es importante conocer las condiciones: un acuerdo por escrito con lo que se hará, cuándo, por cuánto y quién es dueño del trabajo; el pago de lo acordado; el respeto de los derechos de autor; y condiciones de seguridad. «Exposición» o «visibilidad» no reemplazan el pago de un trabajo si no se acordó así.",
        "Hay ofertas engañosas. Se sospecha de quien pide dinero para trabajar, de quien no entrega ningún acuerdo por escrito, de quien presiona para decidir rápido, de quien pide fotos o datos personales innecesarios, y especialmente de quien pide fotos sin ropa o que se guarde el secreto. En esos casos se dice que no, se guarda el mensaje como evidencia sin reenviar imágenes íntimas, se bloquea el contacto y se cuenta a una persona adulta de confianza. Nadie debe enfrentar esto solo.",
        "El desarrollo personal incluye el bienestar. La ansiedad antes o después de exponerse es frecuente; ayuda respirar lento, descansar, hablar con una persona de confianza y, si no mejora, pedir ayuda a una persona adulta responsable. Un plan personal de acción tiene una meta, pasos con plazos, recursos y una forma de revisar cómo va, y se ajusta a las condiciones de cada persona.",
    ],
    vocab=[("acuerdo por escrito", "documento que fija qué se hará, cuándo, por cuánto y quién es dueño del trabajo"), ("oferta engañosa", "propuesta que oculta condiciones o pide algo indebido"), ("plan personal de acción", "meta con pasos, plazos, recursos y revisión"), ("independiente", "persona que trabaja por su cuenta, por proyectos"), ("bienestar", "estado de cuidado físico y emocional")],
    worked=[
        ("Revisar una oferta", "Te ofrecen actuar en una función y pagar «con exposición». No hay contrato. ¿Qué pides?", ["Pedir que se escriban el trabajo, los horarios y el pago.", "Si no aceptan, es mejor no aceptar."], "Un acuerdo por escrito con trabajo, horarios y pago"),
        ("Calcular un resultado de un trabajo", "Taller de 4 sesiones, $20.000 por sesión (de ejemplo) y $15.000 de gastos. ¿Cuánto queda?", ["Ingresos: 4 × 20.000 = 80.000.", "Resultado: 80.000 − 15.000 = 65.000."], "$65.000"),
    ],
    mistakes=[("Aceptar un trabajo sin acuerdo escrito porque «es una buena oportunidad».", "Sin acuerdo no hay forma de exigir lo prometido.", "Pide un acuerdo por escrito antes de empezar."),
              ("Guardar en secreto una solicitud de fotos íntimas.", "Quien la pide suele querer que se calle; hay que contárselo a un adulto.", "No envíes nada, guarda el mensaje y avisa a una persona adulta de confianza.")],
    T=[
        ('abc', 'En trabajo independiente, ¿qué es un acuerdo por escrito?', 'Un documento que fija qué se hará, cuándo, por cuánto y quién es dueño del trabajo', 'Una conversación amistosa sin registro, donde se recuerdan los detalles por confianza', 'Una promesa verbal sin fecha, que se cumple cuando las dos partes tengan tiempo', 'El acuerdo escrito se puede revisar y exigir.'),
        ('abc', '{F} ¿Qué problema tiene el caso A?', 'No hay contrato, horarios ni pago, solo «exposición»', 'La función ocurre en un centro cultural que está lejos del colegio de los estudiantes', 'Se ofrece a estudiantes que todavía no han terminado sus estudios de teatro', 'Falta lo esencial de una oferta justa.'),
        ('abc', '{F} ¿Qué rasgo hace del caso B una oferta más justa?', 'Tiene un acuerdo escrito, honorarios y sesiones definidas', 'Ofrece trabajo en una escuela, que es un lugar seguro y de confianza para todas las personas', 'Es un taller de teatro, lo que siempre garantiza que las condiciones serán justas', 'Define trabajo, pago y duración por escrito.'),
        ('abc', '{F} ¿Qué es el caso C y qué se hace?', 'Una oferta peligrosa: no enviar nada, guardar el mensaje, bloquear y contar a una persona adulta de confianza', 'Un casting normal que se acepta si ofrece trabajo y la persona quiere la oportunidad', 'Una broma entre amigas que se ignora, porque no es necesario avisarle a nadie', 'Pedir fotos sin ropa y guardar secreto es una señal grave de riesgo.'),
        ('=', '{F} ¿Cuántos pesos suma el taller del caso B en ingresos?', '8*25000', 'Se multiplican las sesiones por el pago de cada una.', ' pesos'),
        ('=', '{F} Con los datos del plan personal de ejemplo, ¿cuánto queda después de los gastos?', '8*25000-38000', 'Se resta el gasto de preparación a los ingresos.', ' pesos'),
        ('abc', '{F} Si el taller es de 8 sesiones de 90 minutos, ¿cuántas horas de trabajo suma?', '12 horas', '8 horas', '15 horas', 'Ocho sesiones de una hora y media son doce horas.'),
        ('abc', '{F} En el caso A, un estudiante dice: «con exposición se consiguen más trabajos». ¿Qué respuesta es prudente?', 'La exposición puede ayudar, pero se acuerda por escrito y no reemplaza el pago si no se pactó así', 'Es cierto, y por eso no hace falta ningún acuerdo por escrito ni conversación previa', 'Es falso, porque la exposición nunca sirve para conseguir nuevos trabajos en el medio', 'Se puede valorar la exposición sin renunciar a un acuerdo claro.'),
        ('abc', 'Una compañía quiere usar un guion tuyo en su obra y dice «es un tema de todos». ¿Qué corresponde?', 'Acordar por escrito su uso, reconocer tu autoría y pactar las condiciones', 'Aceptar sin más porque es un tema común y cualquier persona puede escribir sobre él', 'Prohibirlo sin conversar ni escuchar qué es lo que la compañía necesita o propone', 'La autoría de tu texto se reconoce y se pacta su uso.'),
        ('abc', '{F} Una estudiante tiene mucha ansiedad después de una función y no logra dormir varios días. ¿Qué decisión la cuida?', 'Contárselo a una persona adulta de confianza y buscar apoyo, además de descansar', 'Aguantar sin decirle nada a nadie, para no preocupar a las personas que la rodean', 'Hacer otra función de inmediato para distraerse y que la ansiedad desaparezca por sí sola', 'Si la ansiedad persiste, se pide ayuda a un adulto responsable.'),
        ('=', 'Un plan personal para reunir $60.000 en 6 semanas propone ahorrar la misma cantidad cada semana. ¿Cuánto debe ahorrar por semana?', '60000//6', 'Se divide la meta entre las semanas.', ' pesos'),
        ('abc', '¿Qué parte tiene un plan personal de acción bien formulado?', 'Una meta, pasos con plazos, recursos y una forma de revisar cómo va', 'Una frase de motivación que anima a seguir adelante, sin fechas ni pasos definidos', 'La lista de lo que deberían hacer otras personas para que la meta se cumpla', 'Se puede ejecutar paso a paso y revisar.'),
        ('abc', '{F} Una persona recibe un mensaje como el del caso C y siente miedo de contarlo. ¿Qué mensaje le sirve más?', 'Contarlo no es una falta: es lo correcto, y una persona adulta de confianza puede ayudar', 'Mejor no decir nada a nadie para evitar problemas con quien envió el mensaje', 'Responder al mensaje con amenazas, para que el supuesto productor deje de escribir', 'Contar a un adulto de confianza protege y no es una falta.'),
    ],
    ctx=('abc', 'Un estudiante recibe una oferta para dar talleres de teatro en una organización. Le piden empezar mañana, sin acuerdo por escrito, y que no comente las condiciones. ¿Qué paso es más prudente?', 'Pedir un acuerdo por escrito con trabajo, horarios y pago, y consultarlo con una persona adulta de confianza antes de aceptar', 'Aceptar de inmediato para no perder la oportunidad antes de que la ofrezcan a otra persona', 'Aceptar y guardar el secreto, para no incomodar a la organización con muchas preguntas', 'La presión por decidir y el secreto son señales de alerta.'),
    sc=[
        ("En Teatro: ¿qué debe incluir un acuerdo de trabajo independiente?", "Qué se hará, cuándo, por cuánto y a quién pertenece el trabajo", "Protege a ambas partes del trabajo acordado."),
        ("¿Qué se hace ante la solicitud de fotos íntimas?", "No enviar nada, guardar el mensaje, bloquear y contar a una persona adulta de confianza", "Nadie debe enfrentarlo solo ni en secreto."),
        ("¿Qué incluye un plan personal de acción?", "Meta, pasos con plazos, recursos y una forma de revisar", "Permite avanzar con orden y ajustar después."),
    ],
    op=("Arma un plan personal de acción de seis a ocho líneas para un proyecto relacionado con el teatro (un taller breve, una pieza para una escuela, una investigación sobre oficios o prepararte para una entrevista). Incluye meta, tres pasos con plazos, recursos, una condición de trabajo justa que pedirías y una medida de bienestar. Si usas números, rotúlalos como de ejemplo.",
        "Meta: dar un taller de 4 sesiones a niños de 5.º básico, de ejemplo. Pasos: 1) Investigar en dos fuentes y hacer un plan de sesiones (semana 1). 2) Pedir un acuerdo por escrito con la escuela (semana 2). 3) Dictar las 4 sesiones (semanas 3 y 4). Recursos: sala, papel y una persona adulta que acompañe. Condición justa: acuerdo escrito con honorarios de ejemplo de $20.000 por sesión. Bienestar: descansar entre sesiones y contar a una persona adulta si me siento sobrepasada.",
        ["meta, tres pasos con plazos y recursos", "una condición de trabajo justa", "una medida de bienestar", "cifras rotuladas como de ejemplo"],
        ["plan personal de acción de seis a ocho líneas"],
        ["no pedir acuerdo por escrito", "no considerar el bienestar"],
        "Pregunta: «¿cómo sabrás si el plan va bien?». Si no tiene revisión, pídele agregarla."),
    reinforce="Escribe una meta pequeña para este mes (relacionada o no con el teatro) con tres pasos y fechas, y pide a una persona de confianza que la lea.",
    extend="Explica por qué contar a una persona adulta de confianza una oferta sospechosa es una decisión de cuidado y no una exposición innecesaria.",
)

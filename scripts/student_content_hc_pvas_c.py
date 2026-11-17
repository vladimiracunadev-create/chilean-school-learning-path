"""Promoción de estilos de vida activos y saludables, 3.º y 4.º medio HC: OAC-05 (mantener un estilo de vida activo con práctica regular) y OAC-06 (acciones y estrategias con tecnología y entorno). Hábitos, rutas, registros y campañas inventados «de ejemplo», descritos por escrito; sin aplicaciones ni mediciones reales."""
from __future__ import annotations

from hc_pvas_common import build

O5 = "EF-PVAS-3y4-OAC-05"
O6 = "EF-PVAS-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 18 (día de ejemplo, inventado, de Fabián, un estudiante ficticio). Minutos sentado: micro al colegio, 40; clases, 300; tareas en casa, 120; pantallas en la tarde, 180. "
     "Minutos activos: recreo con juego de pelota, 30 (esfuerzo 6); juego con amigos en la plaza, 40 (esfuerzo 6). "
     "Barreras que anota Fabián: B1) llego tarde y cansado a la casa; B2) no tengo con quién practicar; B3) en invierno oscurece temprano; B4) me da vergüenza equivocarme; B5) el gimnasio techado queda lejos. "
     "Facilitadores: F1) dos amistades quieren caminar; F2) hay una plaza a 5 cuadras; F3) un docente ofrece un taller los viernes.")
build(
    O5, 1, F,
    use="Aprenderé a diagnosticar, en privado, mis hábitos de movimiento y de tiempo sentado, y a reconocer barreras y facilitadores que influyen en que mantenga un estilo de vida activo saludable.",
    prior=["Sé clasificar actividades por intensidad.", "Sé llevar un registro personal.", "Sé que mi diagnóstico es privado."],
    explain=[
        "Un estilo de vida activo saludable es una forma de organizar los días en que el movimiento regular forma parte de la rutina. Se mantiene con hábitos, es decir, conductas que se repiten hasta hacerse parte del día. El opuesto de un día activo es el tiempo sedentario: largos periodos sentado o sin moverse, como en clases, tareas o pantallas. No se trata de eliminarlo, sino de equilibrarlo con movimiento y pausas.",
        "Diagnosticar los hábitos es anotar cuánto tiempo pasas sentado y cuánto activo en un día típico, y qué actividad puede sumarse. Después se identifican barreras, que son dificultades para practicar (cansancio, oscuridad, falta de compañía, vergüenza, distancia), y facilitadores, que son cosas que ayudan (amistades, lugares cercanos, talleres). El diagnóstico se centra en conductas y condiciones, no en juzgar a nadie.",
        "Las pausas activas son interrupciones breves de movimiento, por ejemplo 3 minutos cada 45 minutos de trabajo sentado, que ayudan a no pasar largos rato sin moverse. Si una barrera se relaciona con la vergüenza, el ánimo o el miedo, se conversa con una persona adulta de confianza; no es una falla personal.",
    ],
    vocab=[("hábito", "conducta que se repite hasta formar parte del día"), ("tiempo sedentario", "tiempo en que se está sentado o sin moverse"), ("barrera", "dificultad para practicar"), ("facilitador", "algo que ayuda a practicar"), ("pausa activa", "interrupción breve para moverse")],
    worked=[
        ("Sumar el tiempo sentado", "En un día de ejemplo, una persona está sentada 30 minutos en la micro, 280 en clases y 90 en pantallas. ¿Cuántos minutos suma?", ["Suma los tres tramos: 30 + 280 + 90.", "El total es 400 minutos."], "400 minutos"),
        ("Clasificar", "«Mi amiga quiere caminar conmigo los martes». ¿Barrera o facilitador?", ["Ayuda a practicar con compañía.", "Es un facilitador."], "Facilitador"),
    ],
    mistakes=[("Decir «soy flojo» al ver mucho tiempo sentado.", "Mezcla juicio personal con condiciones que se pueden cambiar.", "Anota el tiempo y busca una pausa o actividad posible."),
              ("Dar por hecho que toda barrera se resuelve con fuerza de voluntad.", "Muchas dependen del lugar, la luz o la compañía.", "Busca un cambio concreto en la condición.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un hábito?', 'Una conducta que se repite hasta formar parte del día', 'Una actividad que se hace solo una vez para probar', 'Un resultado que se obtiene en una competencia', 'Un hábito se forma por la repetición.'),
        ('abc', '{F} ¿Qué barrera de Fabián se relaciona con la luz del día?', 'B3, en invierno oscurece temprano', 'B2, no tengo con quién practicar', 'B5, el gimnasio techado queda lejos', 'B3 habla de la oscuridad en invierno.'),
        ('abc', '{F} ¿Cuál de los datos de la ficha es un facilitador?', 'F2, hay una plaza a 5 cuadras', 'B4, me da vergüenza equivocarme', 'B1, llego tarde y cansado a la casa', 'Un lugar cercano ayuda a practicar.'),
        ('=', '{F} ¿Cuántos minutos pasa Fabián sentado en el día?', '40+300+120+180', 'Se suman los cuatro tramos sentados: micro, clases, tareas y pantallas.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos activos moderados a vigorosos suma Fabián?', '30+40', 'Se suman el recreo y el juego en la plaza, ambos con esfuerzo 6.', ' minutos'),
        ('abc', '{F} ¿Qué actividad de la ficha podría ayudar a Fabián a sumar compañía?', 'Caminar con las dos amistades, F1', 'Quedarse en casa a descansar toda la tarde', 'Ir solo al gimnasio techado, B5', 'F1 es un facilitador que resuelve la falta de compañía.'),
        ('abc', 'En Educación Física: ¿qué es una pausa activa durante el tiempo sentado?', 'Una interrupción breve del tiempo sentado para moverse', 'Un día de descanso completo sin moverse', 'Una clase en que se practica un deporte durante toda la hora', 'La pausa activa corta el tiempo sedentario con movimiento breve.'),
        ('abc', '{F} Fabián quiere agregar pausas activas de 3 minutos cada 45 minutos durante sus 120 minutos de tareas. ¿Cuántas pausas cabrían, como máximo, completando bloques de 45 minutos?', '2 pausas', '4 pausas', '1 pausa', 'En 120 minutos caben dos bloques completos de 45 minutos y quedan 30.'),
        ('=', '{F} Si Fabián reemplaza 30 minutos de pantallas por 30 minutos de juego en la plaza con esfuerzo 6, ¿cuántos minutos moderados a vigorosos tendría en el día?', '30+40+30', 'A los 70 minutos activos de la ficha se agregan los 30 nuevos.', ' minutos'),
        ('abc', 'Una estudiante dice: «No me muevo porque soy floja». ¿Qué respuesta ayuda más?', 'Mirar qué condiciones influyen (tiempo, lugar, compañía) y probar un cambio', 'Estar de acuerdo, porque la pereza es una característica propia de la persona', 'Obligarse a moverse sin ningún plan hasta que cambie el ánimo de la persona', 'Las condiciones se pueden cambiar; el juicio personal no ayuda.'),
        ('abc', 'Dos diagnósticos: Ana anota «me muevo poco». Bruno anota «tareas 2 horas, pantallas 3 horas, sin pausas; plaza cerca; tengo vergüenza de ir solo». ¿Cuál permite proponer un cambio?', 'El de Bruno, porque tiene minutos, barreras y facilitadores', 'El de Ana, porque es breve y directo, y se entiende rápido', 'Los dos igual, porque ambos reconocen poco movimiento', 'Sin datos concretos no se puede decidir un cambio.'),
        ('abc', '{F} Fabián anota la barrera B4. ¿Qué respuesta es más adecuada?', 'Conversarlo con una persona adulta de confianza y buscar una actividad cómoda', 'Ocultarlo ante todas las personas para que nadie piense que le cuesta algo', 'Evitar toda actividad física para no sentir vergüenza', 'La vergüenza se puede conversar y se busca un entorno cómodo.'),
        ('abc', 'Un compañero pide leer en voz alta los diagnósticos de todos «para ver quién se mueve más». ¿Qué corresponde?', 'Mantener privado el propio diagnóstico y proponer un reto del curso sin nombres', 'Leerlos todos en voz alta, porque la presión del grupo ayuda a moverse más', 'Cambiar los datos del propio diagnóstico para quedar mejor frente al curso', 'El diagnóstico es privado; el reto grupal motiva sin exponer.'),
    ],
    ctx=('abc', 'Camila anota: «micro 50 minutos, clases 300, pantallas 120, caminata de 25 minutos con amigas (esfuerzo 5). En invierno oscurece temprano y no hay quién vaya conmigo los lunes». ¿Qué cambio es más coherente según su diagnóstico?', 'Caminar con una amiga a un horario con luz, aunque sean 20 minutos, y hacer pausas activas', 'Salir a caminar sola de noche para aprovechar mejor el poco tiempo libre que tiene', 'Eliminar toda actividad sentada del día para compensar el tiempo que pasa en pantallas', 'Responde a la barrera de luz y de compañía de forma segura.'),
    sc=[
        ("En Educación Física: ¿qué es el tiempo sedentario?", "El tiempo sentado o sin moverse", "Se diferencia del tiempo activo en que no hay movimiento."),
        ("¿Qué es una barrera para practicar?", "Una dificultad que reduce la práctica", "Puede ser de luz, tiempo, compañía o ánimo."),
        ("¿Qué hago si siento vergüenza o desánimo para practicar?", "Lo converso con una persona adulta de confianza", "Es normal y se puede apoyar."),
    ],
    op=("Anota en tu cuaderno un día típico de tu semana con los minutos sentado (traslado, clases, tareas, pantallas) y los minutos activos. Escribe tres barreras y dos facilitadores que influyen en que te muevas más. Elige una barrera y propón un cambio pequeño para probar esta semana. Tu diagnóstico es privado.",
        "Sentada: 50 min micro, 300 clases, 90 tareas, 120 pantallas = 560 min. Activa: 30 min de recreo. Barreras: oscurece temprano, cansancio, falta de compañía. Facilitadores: plaza cerca, amiga que camina. Cambio: caminar 20 min con mi amiga a las 17:00.",
        ["minutos sentado y activos sumados", "tres barreras y dos facilitadores", "un cambio pequeño y seguro"],
        ["diagnóstico con suma de minutos, barreras, facilitadores y un cambio"],
        ["decir «soy flojo» o similar", "no sumar minutos", "proponer un cambio inseguro"],
        "Pregunta: «¿qué barrera quieres cambiar y qué cambio concreto probarías?». Si dice «moverme más», pídele un horario y un lugar."),
    reinforce="Durante un día anota cada bloque en que estás sentado y cada bloque activo con sus minutos. Revisa una pausa activa posible.",
    extend="Explica por qué las barreras dependen muchas veces de condiciones que se pueden cambiar y no de la personalidad.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 19 (estrategias de ejemplo, inventadas). E1) Plan «si… entonces…»: «si llueve, hago 15 minutos de baile en casa». E2) Compañía: acordar con una amistad caminar juntas. "
     "E3) Horario fijo ligado a una rutina: «después de tomar once, camino 20 minutos». E4) Meta pequeña: empezar con 10 minutos y subir de a poco. "
     "E5) Pausas activas de 3 minutos cada 45 minutos de pantalla. E6) Esperar a tener ganas para empezar. "
     "Barreras de Fabián (de ejemplo): B1) llego cansado a la casa; B2) no tengo con quién practicar; B3) llueve en invierno y no hay dónde ir; B4) me da vergüenza equivocarme; B5) paso mucho rato sentado frente a la pantalla.")
build(
    O5, 2, F,
    use="Aprenderé a elegir estrategias concretas que me ayuden a sostener la práctica regular, relacionando cada barrera con una estrategia y rechazando las que no funcionan, de modo seguro y con interés propio.",
    prior=["Sé reconocer barreras y facilitadores.", "Sé qué es un hábito.", "Sé que mi diagnóstico es privado."],
    explain=[
        "Una estrategia para mantener la práctica regular es una acción concreta que responde a una barrera. Las más útiles son simples: un plan «si… entonces…» que decide con anticipación qué hacer cuando algo cambia, la compañía de una amistad, un horario fijo ligado a una rutina que ya existe, una meta pequeña que se sube de a poco y pausas activas durante el tiempo sentado.",
        "Elegir una estrategia es relacionarla con una barrera. Si la barrera es la lluvia, sirve un plan «si llueve, entonces…». Si es la falta de compañía, sirve acordar con otra persona. Si es el cansancio al llegar, sirve una meta pequeña. Esperar a tener ganas no es una estrategia, porque depende del ánimo del momento y no cambia la condición.",
        "Una estrategia debe ser segura, posible y de interés propio. Es posible si cabe en tu horario y tu espacio; es segura si no exige salir de noche solo, usar cargas ni saltos; y es de interés propio si te gusta o te resulta tolerable. Se prueba una semana y se revisa si funcionó.",
    ],
    vocab=[("estrategia", "acción concreta que responde a una barrera"), ("plan si… entonces…", "decisión anticipada de qué hacer cuando ocurre algo"), ("meta pequeña", "objetivo breve que se puede cumplir fácilmente"), ("rutina", "secuencia de actividades que se repite en el día"), ("de interés propio", "que te gusta o te resulta tolerable")],
    worked=[
        ("Relacionar barrera y estrategia", "La barrera es «no tengo con quién practicar». ¿Qué estrategia de la ficha responde?", ["Falta compañía.", "E2, acordar con una amistad caminar juntas."], "E2"),
        ("Rechazar una estrategia", "¿Sirve «esperaré a tener ganas» para mantener la práctica?", ["Depende del ánimo del momento y no cambia ninguna condición.", "No es una estrategia concreta."], "No sirve"),
    ],
    mistakes=[("Elegir una estrategia que no responde a la barrera.", "No cambia nada de lo que dificulta practicar.", "Relaciona cada barrera con una estrategia concreta."),
              ("Planear salir de noche sin compañía para aprovechar el horario.", "Es inseguro.", "Elige un horario con luz y compañía.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es una estrategia para mantener la práctica?', 'Una acción concreta que responde a una barrera', 'Una frase motivadora que se repite cada mañana', 'Un castigo para quien no practica', 'Una estrategia cambia una condición concreta.'),
        ('abc', '{F} ¿Qué estrategia responde a B3, la lluvia sin lugar para ir?', 'E1, plan «si llueve, hago 15 minutos de baile en casa»', 'E2, acordar con una amistad que caminen juntas por la plaza', 'E6, esperar a tener ganas para empezar a moverse cada día', 'El plan «si… entonces…» decide con anticipación qué hacer cuando llueve.'),
        ('abc', '{F} ¿Qué estrategia responde mejor a B1, llegar cansado a la casa?', 'E4, empezar con 10 minutos y subir de a poco', 'E1, plan «si llueve, hago 15 minutos de baile en casa»', 'E2, acordar con una amistad que caminen juntas', 'Una meta pequeña es posible incluso con cansancio; el plan de lluvia y la compañía responden a otras barreras.'),
        ('abc', '{F} ¿Qué estrategia responde a B5, mucho rato sentado frente a la pantalla?', 'E5, pausas activas de 3 minutos cada 45 minutos', 'E1, plan «si llueve, hago 15 minutos de baile en casa»', 'E3, horario fijo después de tomar la once, 20 minutos', 'E5 interrumpe el tiempo sentado con movimiento breve.'),
        ('abc', '{F} ¿Por qué E6 no sirve como estrategia?', 'Porque depende del ánimo del momento y no cambia ninguna condición', 'Porque exige demasiado tiempo cada día y casi nadie lo puede sostener', 'Porque solo funciona en invierno y no se puede usar en otras estaciones', 'Esperar sin plan no resuelve ninguna barrera concreta.'),
        ('abc', '¿Qué ventaja tiene ligar una actividad a una rutina que ya existe?', 'Se recuerda más fácilmente porque ya hay un momento fijo', 'Se evita siempre el cansancio del día, aunque la persona no descanse', 'Se cambia el horario cada día para no aburrirse de hacer lo mismo', 'La rutina existente sirve de señal para empezar.'),
        ('=', '{F} Fabián hace E3 durante 5 días en la semana, con 20 minutos cada vez. ¿Cuántos minutos suma?', '5*20', 'Se multiplica el número de días por los minutos de cada caminata.', ' minutos'),
        ('abc', '{F} Fabián combina E4 con 10 minutos al inicio. Si sube 5 minutos cada semana, ¿cuántos minutos hará en la semana 3?', '20 minutos', '25 minutos', '15 minutos', 'Semana 1: 10; semana 2: 15; semana 3: 20.'),
        ('=', '{F} En 135 minutos de pantalla con E5, ¿cuántas pausas completas de 3 minutos caben si se hace una cada 45 minutos?', '135/45', 'Se divide el tiempo total por el intervalo entre pausas.', ' pausas'),
        ('abc', '{F} Fabián tiene B1 y B4. Propone caminar 10 minutos con una amistad cercana, que lo entiende, a la hora de la once. ¿Qué evaluación es correcta?', 'Responde a las dos barreras: meta pequeña y compañía de confianza', 'No responde a ninguna, porque 10 minutos es muy poco tiempo', 'Responde solo a B4, porque la barrera B1 no se puede cambiar', 'Una meta pequeña ayuda con el cansancio y la amistad con la vergüenza.'),
        ('abc', 'Dos estrategias para la lluvia. Ana: «si llueve, no hago nada». Bruno: «si llueve, hago 15 minutos de baile en casa». ¿Cuál es una estrategia?', 'La de Bruno, porque decide con anticipación una acción concreta', 'La de Ana, porque descansar también forma parte de la rutina', 'Las dos, porque ambas contemplan lo que ocurre si llueve', 'Una estrategia define qué hacer; «no hacer nada» no lo cambia.'),
        ('abc', 'Una estudiante propone caminar sola a las 21:00 para mantener su hábito. ¿Qué corresponde?', 'Cambiar a un horario con luz y compañía, y avisar a una persona de su casa', 'Hacerlo igual, porque mantener el hábito es lo más importante de todo', 'Hacerlo con auriculares fuertes para sentirse acompañada durante el camino', 'La seguridad es parte de la estrategia; sin luz ni compañía no es adecuada.'),
        ('abc', '{F} Un compañero dice que Fabián debería «solo esforzarse más» en lugar de usar estrategias. ¿Qué respuesta es más adecuada?', 'Las estrategias cambian las condiciones; esforzarse sin plan dura poco', 'Tiene razón, porque la fuerza de voluntad es lo único que realmente importa', 'Debe exigirse más tiempo cada día para demostrar que de verdad tiene compromiso', 'Muchas barreras dependen de condiciones que se pueden cambiar con un plan.'),
    ],
    ctx=('abc', 'Ema quiere mantener su práctica. Sus barreras son: llueve mucho en invierno y no tiene compañía los miércoles. Con la ficha, ¿qué par de estrategias es el más coherente?', 'E1, un plan para los días de lluvia, y E2, acordar con una amistad los miércoles', 'E6, esperar a tener ganas, y E4, pero empezando con 60 minutos desde el primer día', 'E5, pausas activas, y E3, salir de noche sin compañía', 'Responde a las dos barreras de forma concreta y segura.'),
    sc=[
        ("En Educación Física: ¿qué estrategia sirve cuando llueve y no hay lugar para ir?", "Un plan «si llueve, entonces…»", "Decide con anticipación qué hacer ese día."),
        ("¿Cuál no es una estrategia?", "Esperar a tener ganas", "No cambia ninguna condición que dificulte practicar."),
        ("¿Qué debe cumplir toda estrategia?", "Ser segura, posible y de interés propio", "Si no cumple una de ellas, no se sostiene."),
    ],
    op=("Escribe tres barreras que podrías tener para mantener la práctica (por ejemplo: lluvia, cansancio, falta de compañía). Para cada una propón una estrategia concreta de la ficha o inventada, comprobando que sea segura, posible y de interés propio. Escribe cuándo probarás cada una.",
        "Barrera 1, lluvia: plan «si llueve, hago 15 minutos de baile en casa». Barrera 2, cansancio: meta de 10 minutos, después de la once. Barrera 3, sin compañía: acordar con una amiga caminar los jueves a las 17:00. Probaré todas esta semana.",
        ["tres barreras con estrategias concretas", "comprobación de seguridad, posibilidad e interés", "cuándo se probará cada una"],
        ["tres estrategias relacionadas con tres barreras y un momento de prueba"],
        ["estrategias que no cambian la barrera", "propuestas inseguras", "decir «me esforzaré más»"],
        "Pregunta: «¿qué cambia esa estrategia en la barrera?». Si no puede decirlo, pídele que sea más concreta."),
    reinforce="Elige una barrera de tu semana y escribe un plan «si… entonces…» para ella. Revísalo con una persona de tu casa.",
    extend="Explica por qué un plan «si… entonces…» es más eficaz que prometerse «lo haré si puedo».",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 20 (plan de 4 semanas de ejemplo, inventado, de Tania). Meta específica: practicar actividades que le gustan (baile y caminata) en 4 días por semana. "
     "Meta semanal de minutos moderados a vigorosos: semana 1, 80 minutos; semana 2, 100; semana 3, 120; semana 4, 80 (semana de menor carga, para recuperar). "
     "Días: lunes, miércoles, viernes y sábado. Reglas del plan: subir un poco cada semana, bajar en la cuarta, tener un plan «si… entonces…» para la lluvia y registrar al terminar cada día. "
     "Una buena meta es específica, medible, posible y con plazo.")
build(
    O5, 3, F,
    use="Aprenderé a aplicar un plan de 4 semanas para mantener la práctica, con metas específicas, medibles, posibles y con plazo, subiendo de a poco y dejando una semana de menor carga, y a calcular lo que se necesita cada día.",
    prior=["Sé elegir estrategias para barreras.", "Sé calcular promedios.", "Sé que hay que detenerse ante dolor o mareo."],
    explain=[
        "Un plan para mantener la práctica pone las estrategias en el calendario. Empieza con una meta buena: específica (qué actividad), medible (cuántos minutos o días), posible (que cabe en tu vida) y con plazo (por cuánto tiempo). «Moverme más» no es una buena meta; «caminar o bailar 90 minutos esta semana, en 4 días» sí lo es.",
        "El plan avanza de a poco: sube un poco cada semana y cada cierto tiempo incluye una semana de menor carga para recuperar. Se calcula cuántos minutos se necesitan por día (la meta semanal dividida por los días de práctica) y se anota el resultado de cada día. Así se ve si la meta es posible o conviene ajustarla.",
        "El plan es personal, de interés propio y flexible: si llueve, se cambia de lugar; si hay dolor, mareo o falta de aire inusual, se detiene y se avisa a una persona adulta. No se compara con el plan de otra persona.",
    ],
    vocab=[("meta específica", "meta que dice qué actividad se hará"), ("meta medible", "meta que se puede contar en minutos o días"), ("plazo", "tiempo en que se espera lograr la meta"), ("semana de menor carga", "semana con menos minutos para recuperarse"), ("flexible", "que se puede adaptar sin abandonarlo")],
    worked=[
        ("Revisar una meta", "Revisa la meta «voy a hacer más ejercicio» con los cuatro criterios.", ["No dice qué actividad ni cuántos minutos: no es específica ni medible.", "Tampoco tiene plazo."], "No cumple; falta actividad, cantidad y plazo"),
        ("Calcular minutos por día", "Una meta de ejemplo es 75 minutos en 3 días. ¿Cuántos minutos por día?", ["Divide la meta entre los días: 75 dividido por 3.", "Son 25 minutos por día."], "25 minutos por día"),
    ],
    mistakes=[("Subir mucho los minutos cada semana para llegar antes a la meta.", "Aumenta el riesgo de lesión y de abandono.", "Sube de a poco e incluye una semana de menor carga."),
              ("Fijar una meta sin plazo.", "No se puede saber cuándo evaluarla.", "Agrega cuánto tiempo durará la meta.")],
    T=[
        ('abc', 'En Educación Física: ¿qué características tiene una buena meta?', 'Es específica, medible, posible y con plazo', 'Es difícil, secreta y sin fecha para no sentir presión', 'Es igual a la de las demás personas del curso', 'Una buena meta se puede contar, lograr y evaluar en un plazo.'),
        ('abc', '{F} ¿Cuántos días por semana practica Tania?', '4 días', '3 días', '5 días', 'La ficha indica lunes, miércoles, viernes y sábado.'),
        ('abc', '{F} ¿Qué semana es la de menor carga?', 'La semana 4', 'La semana 1', 'La semana 2', 'La semana 4 baja a 80 minutos, menos que las anteriores.'),
        ('=', '{F} ¿Cuántos minutos por día debe hacer Tania en la semana 1?', '80/4', 'Se divide la meta semanal por los 4 días de práctica.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos por día debe hacer Tania en la semana 3?', '120/4', 'Se divide la meta de la semana 3 entre los 4 días de práctica.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos suma Tania en todo el plan de 4 semanas?', '80+100+120+80', 'Se suman las metas de las cuatro semanas.', ' minutos'),
        ('abc', '{F} ¿Por qué el plan baja a 80 minutos en la semana 4?', 'Para recuperar y mantener la práctica sin cansancio excesivo', 'Para terminar el plan de cuatro semanas más rápido de lo previsto', 'Porque la meta de la semana 3 estaba mal calculada desde el comienzo', 'La semana de menor carga ayuda a recuperar y a sostener la práctica.'),
        ('abc', '{F} Un día llueve y Tania no puede caminar. ¿Qué corresponde según su plan?', 'Usar el plan «si… entonces…» y bailar en casa', 'Saltarse el día y no compensarlo', 'Hacer el doble de minutos al día siguiente', 'El plan ya incluye una alternativa para la lluvia.'),
        ('=', '{F} Si Tania cumple la meta de la semana 2 en 4 días iguales, ¿cuántos minutos hace cada día? (la meta es de 100 minutos)', '100/4', 'Se divide la meta de la semana 2 entre los 4 días.', ' minutos'),
        ('abc', 'Dos metas: Ana, «voy a ser más activa». Bruno, «caminar 20 minutos, 4 días por semana, durante 4 semanas». ¿Cuál es mejor?', 'La de Bruno, porque es específica, medible, posible y con plazo', 'La de Ana, porque es amplia y no presiona a nadie con una cifra', 'Las dos, porque ambas buscan más actividad física en la semana', 'La meta de Bruno se puede contar y evaluar.'),
        ('abc', 'Una persona de ejemplo planea subir de 60 a 120 minutos semanales en la semana 2 «para recuperar el tiempo perdido». ¿Qué corresponde?', 'Subir de a poco y mantener una semana de menor carga', 'Hacerlo, porque cumplir la meta rápido es lo importante', 'Subir a 180 minutos si se siente con ganas', 'Un salto brusco aumenta el riesgo de lesión y de abandono.'),
        ('abc', 'Una compañera dice: «mi plan es mejor que el tuyo porque tiene más minutos». ¿Qué respuesta es más adecuada?', 'Cada plan es personal y se evalúa según los intereses de cada quien', 'Tiene razón, porque más minutos siempre es mejor que menos minutos en un plan', 'Hay que igualar el plan al de ella para no quedarse atrás en el curso', 'No se comparan planes entre personas; cada plan responde a una situación.'),
        ('abc', '{F} A mitad de la semana 3, Tania siente un dolor en la rodilla. ¿Qué hace?', 'Detenerse, descansar y avisar a una persona adulta antes de seguir', 'Seguir el plan con menos minutos y sin avisar a nadie de lo ocurrido', 'Cambiar a una actividad con saltos para fortalecer la rodilla lo antes posible', 'El dolor es señal de detención: se avisa antes de continuar.'),
    ],
    ctx=('abc', 'Joaquín arma su meta: «caminar rápido 25 minutos, 3 días por semana, durante 4 semanas; subir 5 minutos por día cada semana, excepto la última, que baja». ¿Cuántos minutos hará por día en la semana 3?', '35 minutos', '40 minutos', '30 minutos', 'Semana 1: 25; semana 2: 30; semana 3: 35; la semana 4 baja.'),
    sc=[
        ("En Educación Física: ¿cuáles son los cuatro criterios de una buena meta?", "Específica, medible, posible y con plazo", "Sirven para evaluarla después con datos concretos."),
        ("¿Para qué sirve una semana de menor carga?", "Para recuperar y sostener la práctica", "Evita el cansancio excesivo y el abandono del plan."),
        ("¿Qué hace una persona si llueve y su plan es caminar?", "Usa el plan «si… entonces…» y cambia de lugar", "El plan se adapta sin abandonarse."),
    ],
    op=("Arma un plan de 4 semanas para ti (con datos inventados si lo prefieres) con una meta específica, medible, posible y con plazo. Escribe los minutos de cada semana (sube de a poco y baja en la cuarta), los días de práctica, un plan «si… entonces…» y los minutos por día de la semana 2.",
        "Meta: bailar o caminar 4 días por semana durante 4 semanas. Minutos: 80, 100, 120, 80. Días: lunes, miércoles, viernes y domingo. Si llueve: 15 minutos de baile en casa. Semana 2: 100 dividido por 4, 25 minutos por día.",
        ["meta con los cuatro criterios", "minutos que suben de a poco y bajan en la cuarta", "plan «si… entonces…» y cálculo de minutos por día"],
        ["plan de cuatro semanas con meta, minutos, lluvia y cálculo"],
        ["meta sin plazo", "subir de golpe", "no incluir una alternativa para la lluvia"],
        "Pregunta: «¿cómo sabrás si cumpliste tu meta?». Si responde «lo sentiré», pídele minutos o días."),
    reinforce="Revisa una meta que hayas pensado antes y comprueba si cumple los cuatro criterios. Si no, reescríbela.",
    extend="Explica por qué una semana de menor carga puede ayudar a mantener la práctica en el largo plazo.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 21 (registro de 8 semanas de ejemplo, inventado, de Sergio). Meta de ejemplo: al menos 90 minutos moderados a vigorosos por semana. "
     "Minutos por semana: s1, 100; s2, 105; s3, 110; s4, 0 (resfrío; descansó y avisó a una persona adulta); s5, 55 (retomó con la mitad, aproximadamente, de lo que hacía antes del resfrío); s6, 90; s7, 100; s8, 110. "
     "Reglas de ejemplo del plan: ante enfermedad se descansa y se consulta si hace falta; no se deja pasar dos semanas seguidas sin práctica; se retoma con menos minutos y se sube de a poco; se celebran los logros de constancia, sin hablar del cuerpo.")
build(
    O5, 4, F,
    use="Aprenderé a registrar y regular la práctica a lo largo de varias semanas, interpretando pausas por enfermedad o cansancio, retomando de a poco y celebrando la constancia sin juzgar a las personas.",
    prior=["Sé armar un plan con metas posibles.", "Sé calcular totales y promedios.", "Sé que ante dolor o enfermedad se descansa y se avisa."],
    explain=[
        "Mantener un estilo de vida activo no significa no fallar nunca: significa volver. Un registro de varias semanas muestra el camino real: semanas de alta práctica, semanas de pausa y semanas de retorno. Sirve para ver si la práctica se sostiene, no para castigarse por una semana baja.",
        "Cuando hay una pausa por enfermedad, cansancio o exámenes, la regulación es: descansar si el cuerpo lo necesita, consultar a una persona adulta o profesional si hay síntomas, y retomar con menos minutos subiendo de a poco. La regla «nunca dos semanas seguidas sin práctica» ayuda a no abandonar el hábito, pero no obliga a practicar enfermo.",
        "Un registro se interpreta con cifras sencillas: total, promedio de las semanas de práctica, porcentaje de semanas que cumplieron la meta. También se anotan las razones de las semanas bajas. Se celebran los logros de constancia, como volver a empezar, y no se comenta ni se compara el cuerpo de nadie.",
    ],
    vocab=[("constancia", "mantener la práctica a lo largo del tiempo, incluso con pausas"), ("retomar", "volver a practicar después de una pausa"), ("recaída", "semana o periodo en que baja o se detiene la práctica"), ("porcentaje de cumplimiento", "semanas con meta cumplida sobre el total"), ("celebrar logros", "reconocer lo que se logró sin comparar con otras personas")],
    worked=[
        ("Calcular cumplimiento", "En un registro de 5 semanas con meta de 80 minutos, una persona hizo 90, 70, 85, 100 y 60. ¿En cuántas semanas cumplió la meta?", ["Cumplen las semanas de 90, 85 y 100.", "Son 3 semanas."], "3 de 5 semanas"),
        ("Retomar con cuidado", "Una persona de ejemplo hacía 120 minutos por semana antes de enfermarse. ¿Con cuántos minutos puede retomar si la regla es la mitad?", ["Calcula la mitad de 120.", "Son 60 minutos, y luego sube de a poco."], "60 minutos"),
    ],
    mistakes=[("Compensar una semana perdida con el doble de minutos.", "El salto brusco aumenta el riesgo de lesión.", "Retoma con menos minutos y sube de a poco."),
              ("Decir «lo arruiné todo» tras una semana en cero.", "Una pausa no borra el hábito, y lo importante es volver.", "Anota la razón y retoma al comenzar la próxima semana.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es la constancia?', 'Mantener la práctica en el tiempo, incluso con pausas', 'No faltar nunca a ninguna sesión sin importar la salud', 'Hacer más minutos cada semana sin descanso', 'La constancia incluye pausas y regresos.'),
        ('abc', '{F} ¿Qué semana fue de pausa por enfermedad?', 'La s4', 'La s1', 'La s6', 'La ficha señala la s4 con 0 minutos por resfrío.'),
        ('abc', '{F} ¿Con qué estrategia retomó Sergio en la s5?', 'Con aproximadamente la mitad de los minutos que hacía antes', 'Con el doble de minutos para compensar la semana que perdió', 'Sin registrar los minutos de la semana para no ver la baja', 'La s5 tuvo 55 minutos, cerca de la mitad de 110.'),
        ('=', '{F} ¿Cuántos minutos suma Sergio en las 8 semanas?', '100+105+110+0+55+90+100+110', 'Se suman los minutos de todas las semanas, incluida la de pausa.', ' minutos'),
        ('abc', '{F} ¿En cuántas semanas cumplió Sergio la meta de al menos 90 minutos?', '6 de 8', '5 de 8', '8 de 8', 'Cumplieron s1, s2, s3, s6, s7 y s8.'),
        ('=', '{F} ¿Cuál fue el promedio de minutos de las semanas 6, 7 y 8?', '(90+100+110)/3', 'Se suman las tres semanas y se dividen por tres.', ' minutos'),
        ('=', '{F} ¿Qué porcentaje de las 8 semanas cumplió la meta?', '6/8*100', 'Se divide las semanas cumplidas entre las 8 y se multiplica por 100.', ' %'),
        ('abc', '{F} ¿Qué decisión protege más la salud de Sergio en la s4?', 'Descansar y avisar a una persona adulta, sin forzar la práctica', 'Hacer el mismo plan con menos esfuerzo, aunque tenga fiebre', 'Hacer doble sesión cuando se sienta mejor', 'Con enfermedad se descansa y se consulta; no se fuerza.'),
        ('abc', '{F} ¿Qué dice la regla del plan sobre las semanas seguidas sin práctica?', 'No se deja pasar dos semanas seguidas sin práctica, salvo indicación de salud', 'Se deben dejar tres semanas completas para recuperar bien el hábito', 'No se registran las semanas sin práctica porque no aportan información', 'La regla busca que la pausa no se alargue, respetando la salud.'),
        ('abc', 'Ana anota «lo arruiné, falté una semana». Bruno anota «semana en cero por resfrío; retomo con la mitad». ¿Qué registro ayuda más a mantener la práctica?', 'El de Bruno, porque da una razón y un plan de retorno', 'El de Ana, porque reconoce la falta con sinceridad', 'Los dos igual, porque ambos hablan de la semana sin práctica', 'Un buen registro explica la pausa y define cómo retomar.'),
        ('abc', 'Una persona de ejemplo hacía 100 minutos semanales y se perdió 2 semanas por exámenes. Quiere volver con 200 minutos «para recuperar». ¿Qué corresponde?', 'Retomar con menos minutos y subir de a poco', 'Hacerlo, porque lo perdido se recupera con más práctica', 'No volver a practicar porque ya perdió el hábito', 'Un salto brusco aumenta el riesgo; se retoma gradualmente.'),
        ('abc', 'Un grupo propone dar un «premio» a quien tenga el cuerpo más delgado al terminar el plan. ¿Qué corresponde?', 'Cambiar el reconocimiento por uno que celebre la constancia', 'Aprobarlo, porque un premio así motiva mucho a los demás integrantes', 'Hacer una lista pública con el peso y las medidas de cada estudiante', 'Se celebra la constancia y no se compara ni se evalúa el cuerpo.'),
        ('abc', 'Una estudiante de ejemplo anota que lleva semanas sin ganas de nada, aunque ha practicado. ¿Qué es lo más adecuado?', 'Contárselo a una persona adulta de confianza o a un profesional', 'Dejar de anotar para no ver las semanas tan bajas del registro', 'Aumentar los minutos de práctica hasta volver a sentirse mejor', 'El desánimo sostenido se conversa; el ejercicio no reemplaza esa ayuda.'),
    ],
    ctx=('abc', 'Gabriela registra 6 semanas: 90, 95, 100, 0, 45, 90, con meta de 90. La semana en cero fue por una gripe. ¿Qué lectura y qué ajuste son más coherentes?', 'Cumplió 4 de 6 semanas; la pausa tuvo causa y retomó de a poco, así que conviene mantener el plan', 'Cumplió 2 de 6 semanas, así que debe cambiar la meta por una más baja y fácil de lograr', 'Cumplió las 6 semanas, porque en todas ellas hizo algún tipo de actividad física con su curso', 'Las semanas de 90, 95, 100 y 90 cumplen la meta; la pausa se explicó y retomó con la mitad.'),
    sc=[
        ("En Educación Física: ¿qué se hace al retomar la práctica después de una pausa?", "Se retoma con menos minutos y se sube de a poco", "Evita lesiones y el abandono del hábito."),
        ("¿Qué se hace ante un resfrío con fiebre o malestar fuerte?", "Descansar y avisar a una persona adulta", "La salud va antes de la meta de minutos."),
        ("¿Qué se celebra al terminar un plan?", "La constancia y el volver a empezar", "No se comenta ni se compara el cuerpo."),
    ],
    op=("Inventa un registro de 6 semanas con una pausa en una de ellas (enfermedad o exámenes). Anota los minutos de cada semana, la meta, el total, cuántas semanas cumplieron la meta y cómo retomarías después de la pausa. Escribe una forma de celebrar la constancia que no hable del cuerpo.",
        "Meta 80. Semanas: 85, 90, 0 (gripe), 40, 70, 85. Total 370. Cumplieron 3 de 6. Retomo con unos 40 minutos, cerca de la mitad de lo que hacía, y subo de a poco. Celebro con una caminata con amistades que no habla de cuerpos.",
        ["seis semanas con una pausa explicada", "total y semanas cumplidas calculados", "retorno gradual y una celebración respetuosa"],
        ["registro de seis semanas con pausa, cálculos y retorno"],
        ["compensar con el doble de minutos", "celebrar con comentarios sobre el cuerpo", "no explicar la pausa"],
        "Pregunta: «¿cómo retomarías después de la pausa y por qué así?». Si dice «con más ganas», pídele minutos y cuidado."),
    reinforce="Con tu registro, marca las semanas que cumplieron la meta y escribe cómo retomarías tras una pausa.",
    extend="Explica por qué «volver a empezar» es parte de mantener un estilo de vida activo.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 22 (entorno de ejemplo, inventado, de un barrio ficticio; las distancias son desde la casa de Valentina). "
     "L1) Plaza Los Aromos: 400 metros, gratis, iluminada hasta las 21:00, se llega con un cruce con semáforo. "
     "L2) Cancha del colegio: 600 metros, gratis, abierta los sábados con un docente a cargo. "
     "L3) Parque del cerro: 1.500 metros, gratis, sendero con pendiente, solo de día y con otras personas. "
     "L4) Gimnasio municipal: 2.000 metros, con entrada pagada. "
     "L5) Ciclovía de la avenida: 800 metros, gratis, con tránsito cercano; exige casco si se anda en bicicleta. "
     "Recursos que Valentina podría usar: un reloj o temporizador, un cuaderno y una persona de su casa que sabe dónde estará. "
     "Criterios de Valentina: gratis, cercano (menos de 1.000 metros), seguro de día y de tarde, y sin tránsito de vehículos cerca.")
build(
    O6, 1, F,
    use="Aprenderé a diagnosticar los espacios del entorno y los recursos que tengo para moverme, evaluando cercanía, costo, seguridad y horarios, y a proteger mi privacidad cuando uso recursos tecnológicos.",
    prior=["Sé reconocer barreras y facilitadores.", "Sé elegir estrategias para sostener la práctica.", "Sé que algunos datos personales son privados."],
    explain=[
        "El entorno es el conjunto de lugares y condiciones que rodean a una persona: plazas, canchas, parques, ciclovías, el patio del colegio. Un diagnóstico del entorno lista esos lugares y anota para cada uno la distancia desde la casa, el costo, el horario, si es seguro y quién está a cargo. Así se ve qué espacios son posibles y cuáles no.",
        "Un lugar seguro tiene buena luz en el horario que se usará, cruces con semáforo o paso peatonal, compañía de otras personas y, si se anda en bicicleta, casco. Una persona adulta de la casa debe saber dónde estás y a qué hora vuelves. Un lugar bonito pero lejano, de pago o peligroso en la tarde no cumple los criterios, aunque sea atractivo.",
        "También se diagnostican los recursos tecnológicos que ya se tienen: un reloj, un temporizador o un cuaderno bastan para planificar. Cuando se usan aparatos conectados, se cuida la privacidad: no se comparte la ubicación en tiempo real ni se publica el recorrido habitual, porque revela dónde estás y dónde vives.",
    ],
    vocab=[("entorno", "lugares y condiciones que rodean a una persona"), ("diagnóstico del entorno", "lista de los lugares con sus datos para decidir cuáles sirven"), ("espacio seguro", "lugar con luz, cruces seguros y compañía"), ("recurso", "cosa o persona que puede ayudar a practicar"), ("privacidad", "cuidado de los datos personales, como la ubicación")],
    worked=[
        ("Aplicar un criterio", "Con los criterios «gratis y a menos de 1.000 metros», ¿qué lugares de la ficha quedan descartados por distancia?", ["Revisa las distancias: el gimnasio está a 2.000 metros y el parque a 1.500.", "Ambos superan 1.000 metros."], "El gimnasio municipal y el parque del cerro"),
        ("Proteger la privacidad", "Una persona quiere publicar su recorrido de cada tarde. ¿Qué riesgo tiene y qué hace?", ["Mostrar siempre el mismo recorrido revela dónde está y dónde vive.", "No lo publica y, si quiere compartir, cuenta lo vivido sin la ubicación."], "No publicar el recorrido ni la ubicación"),
    ],
    mistakes=[("Elegir un lugar solo porque es el más bonito o famoso.", "Puede ser lejano, de pago o inseguro en el horario que se usará.", "Revisa distancia, costo, horario y seguridad."),
              ("Compartir la ubicación en tiempo real con desconocidos.", "Revela dónde está la persona y dónde vive.", "Comparte la ubicación solo con una persona adulta de confianza.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es el entorno para la actividad física?', 'Los lugares y condiciones que rodean a una persona', 'Los aparatos de tecnología que se guardan en una mochila', 'La opinión de las demás personas sobre un deporte', 'El entorno son los lugares y condiciones del lugar donde se vive.'),
        ('abc', '{F} ¿Qué lugar de la ficha es el único que se usa con entrada pagada?', 'L4, el gimnasio municipal', 'L1, la plaza Los Aromos', 'L5, la ciclovía de la avenida', 'La ficha indica entrada pagada solo para L4.'),
        ('abc', '{F} ¿Qué lugar exige casco si se anda en bicicleta?', 'L5, la ciclovía de la avenida', 'L2, la cancha del colegio', 'L3, el parque del cerro', 'La ficha lo indica para la ciclovía, por el tránsito cercano.'),
        ('abc', '{F} ¿Qué lugares cumplen los criterios de Valentina (gratis, a menos de 1.000 metros, seguro de día y de tarde)?', 'L1 y L2', 'L3 y L4', 'L4 y L5', 'L1 está a 400 metros y L2 a 600, ambos gratis y seguros.'),
        ('abc', '{F} ¿Por qué L3 no cumple los criterios de Valentina?', 'Porque está a 1.500 metros, más lejos que su límite', 'Porque tiene un costo de entrada que ella no puede pagar', 'Porque exige casco para poder entrar al sendero del cerro', 'La distancia supera los 1.000 metros.'),
        ('abc', '{F} Valentina quiere ir a la plaza a las 21:30. ¿Qué observación de la ficha hay que considerar?', 'La plaza está iluminada solo hasta las 21:00', 'La plaza está a más de 1.000 metros de la casa de ella', 'La plaza tiene entrada pagada para quienes llegan en la noche', 'A esa hora no habría luz en la plaza.'),
        ('=', '{F} ¿Cuántos metros recorre Valentina en un viaje de ida y vuelta a L1?', '400*2', 'Se duplica la distancia de ida para incluir la vuelta.', ' metros'),
        ('abc', '{F} Valentina quiere ir a L5 en bicicleta. ¿Qué condiciones debe cumplir para hacerlo con seguridad?', 'Usar casco, avisar a una persona adulta de su casa y quedarse en la ciclovía', 'Ir sin casco, porque la ciclovía está cerca y se llega en pocos minutos', 'Salir de noche, porque hay menos tránsito en la avenida a esa hora', 'La ficha indica casco y tránsito cercano; avisar y usar la ciclovía son medidas básicas.'),
        ('=', '{F} Si Valentina va a L2 los sábados y a L1 dos días en la semana, ¿cuántos metros recorre en total en una semana, contando ida y vuelta?', '2*600+2*2*400', 'Se calculan el ida y vuelta a la cancha (1.200 m) y dos ida y vuelta a la plaza (1.600 m) y se suman.', ' metros'),
        ('abc', 'Una estudiante dice: «Subí a las redes mi recorrido de cada tarde con mi ubicación». ¿Qué respuesta es más adecuada?', 'Que cuide su privacidad, porque la ubicación revela dónde está y dónde vive', 'Que lo siga haciendo, porque así motiva a otras personas a salir a caminar', 'Que lo haga, pero cambiando la hora del recorrido que publica cada día', 'La ubicación en tiempo real y el recorrido habitual exponen a la persona.'),
        ('abc', 'Dos estudiantes diagnostican su entorno. Ana anota «hay lugares cerca». Bruno anota «plaza a 300 metros, gratis, luz hasta las 21:00, semáforo en el cruce». ¿Qué diagnóstico sirve más?', 'El de Bruno, porque tiene distancia, costo, luz y cruce', 'El de Ana, porque es breve', 'Los dos igual, porque los dos nombran lugares cercanos', 'Un diagnóstico útil trae datos para decidir.'),
        ('abc', 'Un grupo decide ir a un cerro lejano un sábado sin avisar a una persona adulta, porque «es solo un paseo». ¿Qué corresponde?', 'Avisar a una persona adulta el lugar y la hora de regreso, y ojalá ir acompañados', 'Ir igual sin avisar, porque es de día y se trata de un paseo de poco riesgo', 'Ir solos para llegar más rápido y volver antes de que se haga de noche', 'Avisar dónde estarán es parte de la seguridad.'),
        ('abc', 'Un estudiante propone usar un lugar que solo conoce una persona, a las 22:00, para que nadie lo vea hacer ejercicio. ¿Qué respuesta es más adecuada?', 'No hacerlo de noche y solo; buscar un horario con luz y compañía de confianza', 'Hacerlo igual, porque la privacidad es más importante que cualquier otra cosa', 'Hacerlo, pero llevando un teléfono con los datos de ubicación apagados todo el tiempo', 'La seguridad y la compañía importan; la vergüenza se puede conversar con un adulto.'),
    ],
    ctx=('abc', 'Samuel quiere practicar tres tardes a la semana. Su barrio ofrece una plaza a 500 metros con luz hasta las 21:00, un gimnasio privado a 1.800 metros con entrada pagada y un cerro con sendero a 2.500 metros. No puede pagar y sale del colegio a las 18:00. ¿Qué decisión es más coherente?', 'Usar la plaza, con un plan para cuando llueva', 'Ir al gimnasio una vez por semana, aunque no pueda pagar', 'Ir al cerro los fines de semana solo y sin avisar', 'La plaza es gratis, cercana, con luz en su horario.'),
    sc=[
        ("En Educación Física: ¿qué se anota al diagnosticar un lugar para practicar?", "Distancia, costo, horario y seguridad", "Son los datos que permiten decidir."),
        ("¿Qué no se comparte con desconocidos al usar aparatos conectados?", "La ubicación en tiempo real", "Revela dónde está y dónde vive la persona."),
        ("¿A quién se avisa dónde estarás y a qué hora volverás?", "A una persona adulta de la casa", "Es una medida básica de seguridad."),
    ],
    op=("Anota en tu cuaderno tres lugares de tu entorno donde podrías practicar actividad física (o inventa tres de ejemplo). Para cada uno escribe distancia, costo, horario y una condición de seguridad. Elige uno según tres criterios propios y di a quién avisarías dónde estarás. No incluyas direcciones exactas.",
        "Plaza (400 m, gratis, hasta las 21:00, semáforo en el cruce); cancha del colegio (600 m, gratis, sábados con docente); parque del cerro (1.500 m, gratis, solo de día). Elijo la plaza: gratis, cercana y con luz en mi horario. Aviso a mi tía de la casa que estaré allí de 18:00 a 19:00.",
        ["tres lugares con distancia, costo, horario y seguridad", "elección con tres criterios propios", "una persona adulta a la que se avisa"],
        ["tres lugares diagnosticados y una elección justificada"],
        ["datos incompletos", "publicar la ubicación exacta", "elegir sin criterios"],
        "Pregunta: «¿qué dato de seguridad usaste para elegir el lugar?». Si responde «me gusta», pídele un dato (luz, cruce, compañía)."),
    reinforce="Con la ficha de la clase, escribe qué lugar usarías un día lluvioso y por qué. Revisa la privacidad de tu plan.",
    extend="Explica por qué avisar a una persona adulta dónde estarás es parte de un entorno seguro y no una pérdida de privacidad.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 23 (herramientas de ejemplo, inventadas). H1) Temporizador de reloj o celular: costo $0 si ya se tiene; funciona sin internet; no recoge datos personales; mide tiempo, no intensidad. "
     "H2) Contador de pasos del celular o de una pulsera: costo $0 si ya existe; funciona sin internet; según su configuración puede guardar la ubicación; cuenta de forma aproximada y no mide intensidad. "
     "H3) Planilla en papel: costo $0; sin internet; privada; hay que anotar a mano. "
     "H4) Aplicación con cuenta: puede ser de pago; exige internet y cuenta; comparte datos y ubicación con una empresa y puede mostrar rankings públicos. "
     "H5) Video de rutina en internet: gasta datos móviles; la rutina puede no ser segura ni adecuada para todas las personas y no hay quien corrija. "
     "Criterios de Valentina (de ejemplo): $0, sin internet, que no comparta su ubicación ni ranking público y que le sirva para anotar minutos.")
build(
    O6, 2, F,
    use="Aprenderé a elegir y usar recursos tecnológicos y de bajo costo para registrar y planificar mi práctica, comparando costo, conexión, privacidad y utilidad, y reconociendo sus límites.",
    prior=["Sé diagnosticar el entorno.", "Sé que mi ubicación es un dato privado.", "Sé llevar un registro de minutos."],
    explain=[
        "La tecnología puede ayudar a mantener un estilo de vida activo: un temporizador mide el tiempo de una sesión, un contador de pasos cuenta de forma aproximada los pasos del día y una planilla en papel registra minutos sin aparatos. Cada recurso sirve para algo distinto y tiene límites: un contador de pasos no mide la intensidad ni la salud, y un video no corrige la técnica.",
        "Para elegir una herramienta se comparan criterios: costo, si funciona sin internet, qué datos recoge, si exige cuenta o comparte la ubicación, y si sirve para lo que se quiere anotar. Una herramienta que obliga a compartir la ubicación o un ranking público no cumple el criterio de privacidad aunque sea popular. Los recursos más simples, como el papel y el temporizador, son suficientes y accesibles.",
        "Las herramientas ayudan, pero no reemplazan el criterio propio ni la compañía. Si una aplicación muestra datos que preocupan o genera presión por compararse, se conversa con una persona adulta y se puede dejar de usar. Nadie debe sentirse obligado a usar un aparato para ser activo.",
    ],
    vocab=[("herramienta tecnológica", "recurso que ayuda a registrar o planificar la práctica"), ("conexión", "uso de internet o datos móviles"), ("datos personales", "información que identifica o ubica a una persona"), ("ranking público", "lista que ordena a las personas por un resultado"), ("límite de una herramienta", "lo que la herramienta no puede medir o hacer")],
    worked=[
        ("Elegir una herramienta", "Una persona de ejemplo quiere anotar sus minutos sin internet y sin gastar. ¿Qué herramienta de la ficha sirve?", ["Revisa costo $0 y sin internet: H1 y H3 cumplen.", "Para anotar minutos a mano, la planilla en papel H3 es la más directa."], "H3, la planilla en papel"),
        ("Reconocer un límite", "Un contador de pasos marca 8.000 pasos. ¿Qué no dice ese dato?", ["Cuenta pasos de forma aproximada.", "No dice la intensidad ni si hubo ejercicio moderado a vigoroso."], "No dice la intensidad ni la salud"),
    ],
    mistakes=[("Elegir una aplicación solo porque la usa todo el curso.", "Puede compartir la ubicación y generar presión por compararse.", "Revisa costo, privacidad y utilidad antes de elegir."),
              ("Creer que el contador de pasos mide toda la actividad.", "No mide intensidad ni actividades como nadar o andar en bicicleta.", "Úsalo como una pista y anota también los minutos.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es una herramienta tecnológica de registro?', 'Un recurso que ayuda a anotar o planificar la práctica', 'Un deporte que se practica con aparatos electrónicos', 'Un premio que se entrega por completar el registro', 'Una herramienta de registro ayuda a anotar y planificar.'),
        ('abc', '{F} ¿Qué herramienta de la ficha mide tiempo pero no intensidad?', 'H1, el temporizador', 'H4, la aplicación con cuenta', 'H5, el video de rutina', 'La ficha dice que el temporizador mide tiempo.'),
        ('abc', '{F} ¿Qué herramienta exige cuenta, internet y puede mostrar rankings públicos?', 'H4, la aplicación con cuenta', 'H3, la planilla en papel', 'H2, el contador de pasos', 'La ficha lo indica para H4.'),
        ('abc', '{F} ¿Qué herramientas cumplen los criterios de Valentina?', 'H1 y H3', 'H2 y H4', 'H4 y H5', 'H1 y H3 son gratis, sin internet y no comparten ubicación.'),
        ('abc', '{F} ¿Por qué H2 no cumple del todo el criterio de privacidad?', 'Porque según su configuración puede guardar la ubicación', 'Porque cuesta mucho dinero y no todas las personas pueden pagarlo', 'Porque solo funciona si hay internet disponible en todo momento', 'La ficha advierte que puede guardar la ubicación.'),
        ('abc', '{F} ¿Qué riesgo tiene seguir un video de rutina en internet sin supervisión?', 'La rutina puede no ser segura ni adecuada para todas las personas', 'El video siempre cuesta dinero y hay que pagarlo cada mes de uso', 'El video no se puede ver sin tener una cuenta de la empresa', 'La ficha advierte que no hay quien corrija y puede no ser adecuada.'),
        ('=', '{F} Valentina usa H1 y registra en H3: 20, 25, 30 y 25 minutos en cuatro días. ¿Cuántos minutos suma?', '20+25+30+25', 'Se suman los minutos anotados en la planilla.', ' minutos'),
        ('abc', '{F} Valentina quiere saber cuánto camina en el día sin gastar y sin internet. ¿Qué herramienta responde mejor, con sus límites?', 'H2, el contador de pasos que ya tiene, sabiendo que es aproximado', 'H4, porque una aplicación con cuenta siempre mide con total exactitud', 'H5, porque un video de rutina cuenta los pasos que la persona dio', 'H2 cumple el costo y no exige internet; solo da una cifra aproximada.'),
        ('=', '{F} Una persona de ejemplo anota con H2 cinco días: 6.000, 7.000, 8.000, 5.000 y 9.000 pasos. ¿Cuál es el promedio diario?', '(6000+7000+8000+5000+9000)/5', 'Se suman los cinco días y se divide por cinco.', ' pasos'),
        ('abc', 'Dos estudiantes: Ana usa una aplicación con ranking público para «ganarle» a su curso. Bruno usa una planilla en papel y la comparte solo con su docente. ¿Qué elección respeta más la privacidad y el bienestar?', 'La de Bruno, porque no expone datos y evita compararse con otras personas', 'La de Ana, porque la competencia aumenta la motivación de todo el curso', 'Las dos igual, porque ambas sirven para anotar minutos', 'Un ranking público expone y presiona; la planilla es privada.'),
        ('abc', 'Alguien dice: «con un contador de pasos ya no hace falta anotar minutos de actividad». ¿Qué corresponde?', 'Los pasos no miden la intensidad; conviene anotar también los minutos', 'Tiene razón, porque los pasos miden toda la actividad que una persona hace', 'Hay que dejar de usar el contador de pasos por completo desde hoy', 'El contador es una pista aproximada y no mide intensidad.'),
        ('abc', 'Una aplicación de ejemplo muestra una lista de quién se movió menos y sube un mensaje burlón. ¿Qué corresponde?', 'Dejar de usarla y contárselo a una persona adulta de confianza', 'Seguir usándola y reírse del mensaje junto con las demás personas', 'Publicar el ranking en redes para que la empresa lo corrija pronto', 'La burla es una falta de respeto; se deja de usar y se avisa a un adulto.'),
        ('abc', 'Un estudiante quiere ir al parque a seguir un video de rutina sin docente, con saltos y cargas. ¿Qué corresponde?', 'No hacerlo así: consultar al docente para elegir una rutina segura', 'Hacerlo igual, porque un video de internet es una guía suficiente para todo', 'Hacerlo con más cargas todavía para que la rutina sea mucho más eficaz', 'Las rutinas sin supervisión pueden no ser seguras; se consulta.'),
    ],
    ctx=('abc', 'Marta quiere registrar su práctica durante un mes. No tiene datos móviles y comparte el celular con su familia. Quiere anotar minutos y cómo se sintió. ¿Qué plan de herramientas es más coherente?', 'Un temporizador del celular y una planilla en papel con minutos y ánimo', 'Una aplicación con cuenta, datos de ubicación y un ranking público de todos', 'Videos de rutina con datos móviles cada día, sin llevar ningún registro propio', 'Cumple costo cero, funciona sin internet y es privado.'),
    sc=[
        ("En Educación Física: ¿qué herramienta sirve para anotar minutos sin internet ni costo?", "La planilla en papel", "Es simple, privada y gratuita, y no necesita internet."),
        ("¿Qué mide un contador de pasos?", "Pasos, de forma aproximada, sin intensidad", "No reemplaza anotar los minutos de actividad."),
        ("¿Qué se hace si una aplicación expone o presiona a las personas?", "Dejar de usarla y avisar a una persona adulta", "La privacidad y el bienestar son lo primero."),
    ],
    op=("Elige tres herramientas (de la ficha o propias) para registrar tu práctica durante un mes. Para cada una escribe costo, si necesita internet, qué datos recoge y qué límite tiene. Compara con tres criterios tuyos, elige una combinación y escribe por qué cuida tu privacidad.",
        "Elijo temporizador del celular (costo $0, sin internet, no recoge datos; mide solo tiempo), planilla en papel ($0, sin internet, privada; anota a mano) y contador de pasos (costo $0, aproximado, puede guardar ubicación, lo desactivo). Criterios: gratis, privado, simple.",
        ["tres herramientas con costo, internet, datos y límite", "tres criterios y una combinación elegida", "cómo se protege la privacidad"],
        ["tres herramientas comparadas y una combinación justificada"],
        ["elegir solo porque la usa el curso", "no mencionar datos ni ubicación", "creer que el contador de pasos mide intensidad"],
        "Pregunta: «¿qué dato personal recoge esa herramienta y qué haces con él?». Si dice «no sé», pídele revisar la ficha."),
    reinforce="Elige una herramienta y escribe dos cosas que no puede medir. Si usas un celular, pide permiso a una persona adulta de tu casa.",
    extend="Explica por qué las herramientas más simples, como el papel y un temporizador, pueden ser suficientes para mantener un estilo de vida activo.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 24 (rutas de ejemplo, inventadas, de la casa al colegio de Rodrigo). Valor de ejemplo: caminando a paso firme se recorren 250 metros cada 3 minutos (es decir, 12 minutos por kilómetro). "
     "Ruta A: 1.000 metros, vereda ancha, calle iluminada, 2 cruces con semáforo. "
     "Ruta B: 750 metros, vereda angosta, poca luz en la tarde, un cruce sin semáforo en una curva. "
     "Reglas de seguridad de ejemplo: cruzar por el semáforo o el paso peatonal; con poca luz, evitar la ruta o ir con compañía; con bicicleta, usar casco; avisar a una persona adulta de la casa qué ruta se usará; no usar auriculares con volumen alto. "
     "Rodrigo va y vuelve 5 días por semana.")
build(
    O6, 3, F,
    use="Aprenderé a diseñar y aplicar una estrategia de transporte activo (caminar o andar en bicicleta al colegio), eligiendo una ruta segura, calculando tiempos y planificando cómo sumar minutos de actividad en el día.",
    prior=["Sé diagnosticar el entorno.", "Sé acumular minutos en bloques de al menos 10 minutos.", "Sé que debo avisar a una persona adulta dónde estaré."],
    explain=[
        "El transporte activo es usar caminata o bicicleta para trasladarse, por ejemplo, al colegio. Es una forma de sumar actividad en el día sin necesitar tiempo extra, y aprovecha el entorno. Para diseñarlo se elige una ruta, se calcula cuánto tarda y se revisan las condiciones de seguridad.",
        "La mejor ruta no siempre es la más corta. Se elige con criterios: cruces con semáforo o paso peatonal, buena luz en el horario de uso, veredas o ciclovías adecuadas y compañía. El tiempo se calcula con un valor de ejemplo, como 12 minutos por kilómetro a paso firme. Si un tramo seguido dura 10 minutos o más con esfuerzo de 5 o más, suma a los minutos moderados a vigorosos; si dura menos, es actividad ligera y se registra aparte.",
        "Las reglas de seguridad son parte del diseño: cruzar por el semáforo, usar casco en bicicleta, no usar auriculares con volumen alto y avisar a una persona adulta de la casa qué ruta usarás. Si hay clima peligroso, mala luz o un riesgo en el camino, se cambia de ruta o de medio, o se pide compañía.",
    ],
    vocab=[("transporte activo", "trasladarse caminando o en bicicleta"), ("ruta segura", "camino con luz, cruces seguros y compañía"), ("paso firme", "caminar rápido, con esfuerzo 5 o más"), ("ida y vuelta", "viaje al colegio y regreso a la casa"), ("casco", "protección obligatoria al andar en bicicleta")],
    worked=[
        ("Calcular el tiempo de una ruta", "Una ruta de ejemplo mide 500 metros. Con 250 metros cada 3 minutos, ¿cuánto tarda?", ["500 metros son dos tramos de 250 metros.", "Dos tramos de 3 minutos son 6 minutos."], "6 minutos"),
        ("Elegir una ruta", "Una ruta es 300 metros más corta, pero no tiene luz y cruza sin semáforo en una curva. ¿Se elige?", ["La seguridad pesa más que la distancia.", "Se elige la ruta más larga, con luz y semáforo."], "No: se elige la ruta segura aunque sea más larga"),
    ],
    mistakes=[("Elegir siempre la ruta más corta.", "Puede tener cruces o tramos inseguros.", "Elige la ruta con luz, semáforo y compañía."),
              ("Salir con auriculares fuertes para hacer más entretenido el trayecto.", "No se oyen los vehículos ni las alertas.", "Mantén el volumen bajo o no los uses.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es el transporte activo?', 'Trasladarse caminando o en bicicleta', 'Viajar en un vehículo más rápido que la micro', 'Practicar un deporte en un gimnasio', 'El transporte activo usa la caminata o la bicicleta para moverse.'),
        ('abc', '{F} ¿Qué ruta tiene un cruce sin semáforo en una curva?', 'La B', 'La A', 'Las dos rutas', 'La ficha indica ese cruce en la ruta B.'),
        ('abc', '{F} ¿Qué ruta es más segura según la ficha?', 'La A, con luz, vereda ancha y semáforos', 'La B, porque es más corta y se llega antes', 'Ninguna de las dos es más segura que la otra', 'La A cumple las condiciones de seguridad que la ficha menciona.'),
        ('=', '{F} ¿Cuántos minutos tarda Rodrigo en la ruta A, con el valor de ejemplo?', '1000/250*3', 'Se divide la distancia en tramos de 250 metros y se multiplica por 3 minutos.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos tarda Rodrigo en la ruta B?', '750/250*3', 'Son tres tramos de 250 metros, de 3 minutos cada uno.', ' minutos'),
        ('abc', '{F} ¿Por qué el trayecto de la ruta B no suma a los minutos moderados a vigorosos seguidos?', 'Porque dura menos de 10 minutos', 'Porque la ruta B no tiene veredas', 'Porque se hace en bicicleta', 'Un bloque suma si dura 10 minutos o más.'),
        ('abc', '{F} ¿Qué debe cumplir Rodrigo si anda en bicicleta?', 'Usar casco', 'Evitar los cruces con semáforo para no detenerse', 'Usar auriculares con volumen alto', 'La ficha lo establece como regla.'),
        ('=', '{F} Con la ruta A, ¿cuántos minutos de transporte activo suma Rodrigo en una semana, ida y vuelta, 5 días?', '5*2*12', 'Cada viaje dura 12 minutos; hay dos viajes por día durante 5 días.', ' minutos'),
        ('abc', '{F} Un día Rodrigo sale a las 19:00 en invierno y ya oscureció. ¿Qué decisión es más segura?', 'Ir en compañía por la ruta A o pedir que lo acompañen', 'Ir solo por la ruta B, para llegar antes a la casa', 'Apurar el paso para cruzar sin mirar la calle antes', 'Con poca luz se evita ir solo y se elige la ruta más segura.'),
        ('abc', 'Una estudiante dice que prefiere la ruta de 450 metros por un descampado oscuro en vez de la de 600 metros con luz. ¿Qué respuesta es más adecuada?', 'Elegir la ruta con luz, aunque sea más larga, y avisar a una persona adulta', 'Elegir la ruta corta, porque llega más rápido y gasta menos tiempo del día', 'Elegir la corta pero con auriculares fuertes, para no asustarse en el descampado', 'La seguridad pesa más que la distancia.'),
        ('abc', 'Dos estudiantes proponen caminar al colegio. Ana dice: «caminaré 20 minutos con mis amigas por la ruta con luz y se lo avisé a mi mamá». Bruno dice: «caminaré 20 minutos solo, por un atajo poco iluminado, sin avisar». ¿Cuál propuesta es mejor?', 'La de Ana, porque cuida la luz, la compañía y el aviso', 'La de Bruno, porque es un atajo más directo y ahorra tiempo', 'Las dos, porque ambas suman el mismo tiempo de caminata al día', 'Las dos suman igual, pero solo la de Ana es segura.'),
        ('abc', 'Un compañero pide que los demás caminen sin mirar la calle para llegar a la hora a una competencia entre cursos. ¿Qué corresponde?', 'No participar de esa competencia y proponer un reto de equipo sin prisa', 'Aceptar, porque competir ayuda a llegar más rápido a la hora de la prueba', 'Cruzar corriendo para ganar tiempo en los semáforos y llegar antes que los demás', 'Apurarse en la calle es peligroso; se cambia la actividad.'),
        ('abc', '{F} Rodrigo quiere sumar 10 minutos más de actividad al día, además de los trayectos. ¿Qué alternativa es coherente con el entorno y la seguridad?', 'Caminar 10 minutos más con compañía por la ruta A antes de la once', 'Salir a trotar a oscuras por la ruta B, que es la más corta de las dos', 'Practicar ejercicios con cargas en la vereda de la ruta de ida', 'Es una actividad posible, con luz y compañía.'),
    ],
    ctx=('abc', 'Paulina vive a 1.250 metros del colegio y puede ir a pie por una ruta iluminada con semáforos. Con el valor de ejemplo de la ficha (250 metros cada 3 minutos), ¿cuánto tarda en cada trayecto y qué conviene hacer?', '15 minutos; sirve como bloque de más de 10 minutos y avisa su ruta a alguien de su casa', '10 minutos; no sirve como bloque porque no llega al mínimo que se pide para sumar', '12 minutos; conviene correr una parte del trayecto para llegar antes a la sala de clases', '1.250 metros son cinco tramos de 250, o sea 15 minutos.'),
    sc=[
        ("En Educación Física: ¿qué se prioriza al elegir una ruta?", "La seguridad: luz, cruces seguros y compañía", "La seguridad pesa más que la distancia."),
        ("¿Cuántos minutos seguidos debe tener un bloque para sumar a los moderados a vigorosos?", "Al menos 10 minutos", "Es la regla de bloques usada en el cuaderno."),
        ("¿Qué se usa al andar en bicicleta?", "Casco", "Protege la cabeza en caso de caída."),
    ],
    op=("Diseña un plan de transporte activo para ir a un lugar de tu entorno (colegio, plaza o taller). Describe dos rutas posibles con distancia, luz y cruces. Calcula el tiempo de cada una con el valor de ejemplo de 250 metros cada 3 minutos. Elige una con criterios de seguridad y escribe a quién avisas y qué haces con poca luz.",
        "Ruta A: 750 m, luz y semáforo, 9 minutos. Ruta B: 500 m, poca luz y cruce sin semáforo, 6 minutos. Elijo la A: segura. Aviso a mi papá la ruta. Con poca luz voy con compañía o pido que me acompañen. Sin auriculares fuertes.",
        ["dos rutas con distancia y condiciones", "tiempos calculados correctamente", "elección segura, aviso y plan con poca luz"],
        ["plan de dos rutas con tiempos, elección y seguridad"],
        ["elegir la más corta sin mirar la seguridad", "calcular mal el tiempo", "no avisar a nadie"],
        "Pregunta: «¿por qué elegiste esa ruta y no la más corta?». Si dice «porque sí», pídele luz, semáforo o compañía."),
    reinforce="Calcula cuánto tardas en un trayecto de 500 metros y en uno de 1.000 metros con el valor de ejemplo y comprueba si cumple el bloque de 10 minutos.",
    extend="Explica por qué una ruta más larga pero segura puede ser mejor que una corta con riesgos.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 25 (registro de ejemplo, inventado, de Ignacio con un contador de pasos y una planilla). Pasos por día: lunes 6.200; martes 7.800; miércoles 5.000; jueves 8.400; viernes 7.000; sábado 9.600; domingo 5.000. "
     "Meta de ejemplo del curso: 7.000 pasos por día. "
     "Notas de Ignacio: el miércoles y el domingo dejó el celular cargando; el sábado jugó fútbol 40 minutos con esfuerzo 7. "
     "Límites de la herramienta: cuenta de forma aproximada, no mide la intensidad y no cuenta bien actividades como la bicicleta. "
     "Privacidad: Ignacio no comparte su ubicación y muestra su registro solo a una persona adulta de su casa y a su docente.")
build(
    O6, 4, F,
    use="Aprenderé a registrar mi actividad con una herramienta tecnológica y a interpretar los datos con sus límites, calculando promedios y cumplimiento de metas sin exponer mi privacidad.",
    prior=["Sé elegir herramientas por criterios.", "Sé calcular promedios.", "Sé que mi ubicación es privada."],
    explain=[
        "Registrar con tecnología es anotar datos que una herramienta entrega: pasos, minutos o distancia. Con esos datos se calcula el total, el promedio diario y cuántos días se cumplió una meta. Por ejemplo, si una meta de ejemplo es 7.000 pasos por día, se cuenta en cuántos días del registro se llegó o se superó esa cifra.",
        "Los datos de una herramienta tienen límites. Un contador de pasos cuenta de forma aproximada, puede dejar de contar si el celular no está encima, no mide la intensidad y no cuenta bien actividades como andar en bicicleta o nadar. Por eso se complementa con una anotación de minutos y de cómo se sintió la persona. Los datos de un día aislado no dicen mucho; se mira el patrón de varios días.",
        "La privacidad forma parte del registro: no se comparte la ubicación en tiempo real, se muestran los datos solo a personas de confianza y se evita publicar rankings que comparen a las personas. Si una herramienta genera presión o malestar, se deja de usar y se conversa con una persona adulta.",
    ],
    vocab=[("registro tecnológico", "datos entregados por una herramienta, como pasos o minutos"), ("promedio diario", "suma de los días dividida por la cantidad de días"), ("meta de ejemplo", "valor que se usa para comparar con los datos propios"), ("dato aislado", "cifra de un solo día que no basta para sacar conclusiones"), ("patrón", "comportamiento que se repite en varios días")],
    worked=[
        ("Calcular un promedio", "En tres días, una persona de ejemplo registra 6.000, 8.000 y 10.000 pasos. ¿Cuál es el promedio diario?", ["Suma: 6.000 + 8.000 + 10.000 = 24.000.", "Divide entre 3: 8.000."], "8.000 pasos por día"),
        ("Leer un dato con sus límites", "Un día aparece con 1.200 pasos, pero la persona hizo 45 minutos de bicicleta. ¿Qué se anota?", ["El contador no cuenta bien la bicicleta.", "Se anotan además los 45 minutos de bicicleta."], "Se anotan los 45 minutos de bicicleta aparte"),
    ],
    mistakes=[("Creer que un día con pocos pasos significa que no hubo actividad.", "El contador puede no estar contando.", "Revisa las condiciones y anota los minutos."),
              ("Publicar el registro con la ubicación para motivar a otras personas.", "Revela dónde está la persona y expone su rutina.", "Comparte los datos solo con personas de confianza.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un dato aislado?', 'La cifra de un solo día, que no basta para concluir', 'La suma de todos los días del mes de registro', 'Un dato que se anota en una planilla distinta a la anterior', 'Un solo día puede ser raro; se mira el patrón.'),
        ('abc', '{F} ¿Qué día tuvo más pasos?', 'El sábado, con 9.600', 'El jueves, con 8.400', 'El martes, con 7.800', 'El sábado superó a todos los demás.'),
        ('abc', '{F} ¿Por qué el miércoles y el domingo pudieron mostrar pocos pasos?', 'Porque dejó el celular cargando y el contador pudo no contar', 'Porque esos días no hizo ninguna actividad física en todo el día', 'Porque el contador solo cuenta los pasos de lunes a viernes', 'La nota de Ignacio explica que el aparato no estaba con él.'),
        ('=', '{F} ¿Cuántos pasos suma Ignacio en la semana?', '6200+7800+5000+8400+7000+9600+5000', 'Se suman los siete días del registro.', ' pasos'),
        ('=', '{F} ¿Cuál es el promedio diario de pasos de Ignacio en la semana?', '(6200+7800+5000+8400+7000+9600+5000)/7', 'Se divide el total de la semana por los 7 días.', ' pasos'),
        ('abc', '{F} ¿En cuántos días Ignacio llegó o superó la meta de 7.000 pasos?', '4 días', '3 días', '5 días', 'Cumplió martes, jueves, viernes y sábado.'),
        ('=', '{F} ¿Cuántos pasos más que el miércoles hizo Ignacio el sábado?', '9600-5000', 'Se resta el valor del miércoles del valor del sábado.', ' pasos'),
        ('abc', '{F} ¿Qué dato adicional conviene anotar el sábado, además de los pasos?', 'Los 40 minutos de fútbol con esfuerzo 7', 'Los pasos de un compañero, para compararse', 'La ubicación exacta de la cancha donde jugó', 'La actividad intensa aporta información que los pasos no muestran.'),
        ('abc', '{F} ¿Qué frase sobre el registro de Ignacio es más prudente?', 'Se observó que el promedio fue de 7.000 pasos y que hay límites', 'Quedó demostrado que Ignacio es la persona más activa de todo su curso', 'Los datos no sirven para nada porque el contador de pasos no es exacto', 'Es prudente dar el dato y reconocer los límites.'),
        ('=', 'En un registro de ejemplo, una persona tiene 5.000, 8.000, 10.000 y 13.000 pasos en cuatro días. ¿Cuál es el promedio diario?', '(5000+8000+10000+13000)/4', 'Se suman los cuatro días y se divide por cuatro.', ' pasos'),
        ('abc', 'Ana presume: «yo hice 10.000 pasos y tú 6.000, así que eres menos activo». ¿Qué respuesta es más adecuada?', 'Los pasos son aproximados y no miden la intensidad; cada quien se compara consigo', 'Tiene razón, porque los pasos miden toda la actividad física de cada persona', 'Hay que subir a 14.000 pasos diarios para superarla de forma clara', 'Comparar entre personas con un dato aproximado no es justo.'),
        ('abc', 'Un grupo quiere publicar en un grupo abierto el recorrido de cada integrante para «ver quién camina más». ¿Qué corresponde?', 'No publicarlo: la ubicación expone; se pueden compartir resultados sin nombres', 'Publicarlo, porque la presión del grupo motiva a caminar más a cada integrante', 'Publicarlo solo con los nombres de quienes caminan más que el resto del grupo', 'El recorrido revela dónde están las personas y es privado.'),
        ('abc', 'Ignacio siente que la herramienta lo hace sentir mal cuando no llega a la meta. ¿Qué es lo más adecuado?', 'Conversarlo con una persona adulta y considerar dejarla o cambiar la meta', 'Seguir usándola hasta llegar a la meta todos los días de la semana', 'Ocultar los días bajos del registro para sentirse mejor con sus resultados', 'Una herramienta no debe generar malestar; se conversa y se ajusta.'),
    ],
    ctx=('abc', 'Camila registra durante 5 días: 7.000, 5.000, 9.000, 6.000 y 8.000 pasos; el segundo día dejó el celular en su casillero. Su meta de ejemplo es 7.000. ¿Qué lectura es más coherente?', 'El promedio es 7.000 y cumplió la meta 3 de 5 días; un día pudo estar incompleto', 'El promedio es 8.000 y cumplió la meta todos los días del registro de la semana', 'No se puede leer nada, porque un contador de pasos no sirve para ningún análisis', 'La suma es 35.000 y el promedio, 7.000; llegó a la meta los días de 7.000, 9.000 y 8.000.'),
    sc=[
        ("En Educación Física: ¿qué no mide un contador de pasos?", "La intensidad de la actividad", "Por eso se anotan también los minutos."),
        ("¿Con quién se muestran los datos del registro?", "Solo con personas de confianza", "Así se protege la privacidad de la persona."),
        ("¿Qué se mira en lugar de un dato aislado?", "El patrón de varios días", "Un solo día puede ser raro."),
    ],
    op=("Inventa el registro de pasos de 6 días de una persona de ejemplo, con una meta propia. Calcula el total, el promedio diario y cuántos días cumplieron la meta. Anota dos límites de la herramienta y dos cuidados de privacidad que tendrías. Escribe una frase prudente sobre lo que observas.",
        "Pasos: 5.000, 6.000, 7.000, 8.000, 9.000, 7.000. Total 42.000, promedio 7.000, meta de 7.000: cumple 4 días. Límites: es aproximado y no mide la intensidad. Privacidad: no comparto la ubicación y solo muestro el registro a mi docente. Frase: «Se observó un promedio de 7.000 pasos y subió hacia el final de la semana».",
        ["total, promedio y días con meta calculados", "dos límites y dos cuidados de privacidad", "frase prudente"],
        ["registro de seis días con cálculos, límites, privacidad y frase"],
        ["publicar la ubicación", "olvidar los límites", "comparar con otra persona"],
        "Pregunta: «¿qué no te dice este registro sobre tu actividad?». Si responde «nada», pídele la intensidad o la bicicleta."),
    reinforce="Con una lista inventada de 5 días de pasos, calcula el promedio y cuántos días cumplen una meta que elijas.",
    extend="Explica por qué un registro tecnológico debe complementarse con anotaciones propias de minutos y de cómo te sentiste.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 26 (proyecto de ejemplo, inventado, «Semana activa del barrio», de un grupo de 3.º y 4.º medio). "
     "Objetivo: que más personas del barrio participen en actividades gratuitas de movimiento. Público: estudiantes y sus familias. "
     "Acciones: 3 caminatas grupales de 30 minutos y 2 talleres de baile al aire libre de 40 minutos. Presupuesto: $0 (se usan espacios públicos con autorización del colegio y de la municipalidad de ejemplo). "
     "Resultados de ejemplo, asistentes: caminata 1, 18; caminata 2, 24; caminata 3, 15 (llovió); taller 1, 30; taller 2, 12 (a las 15:00, en horario de trabajo de muchas familias). "
     "Reglas: las personas menores de edad participan con autorización y acompañadas por una persona adulta; las rutas son accesibles; los mensajes son honestos y no hablan del cuerpo.")
build(
    O6, 5, F,
    use="Aprenderé a diseñar, aplicar y evaluar un proyecto comunitario de promoción de actividad física usando el entorno y recursos tecnológicos simples, con indicadores, inclusión y seguridad, y a ajustarlo con los resultados.",
    prior=["Sé diagnosticar el entorno.", "Sé elegir herramientas por criterios.", "Sé evaluar un programa con indicadores y ajustes."],
    explain=[
        "Un proyecto comunitario de promoción es un conjunto de acciones organizadas para que más personas de un lugar se muevan con regularidad. Tiene un objetivo, un público al que se dirige, acciones con fecha y lugar, un presupuesto, reglas de seguridad y un indicador para evaluar, como la cantidad de asistentes. Se diseña con el entorno que existe (plazas, rutas, canchas) y con recursos simples, como un afiche en papel o un mensaje a las familias.",
        "Un proyecto honesto e inclusivo cuida varios aspectos: pide autorización del colegio y de las familias cuando participan personas menores de edad, elige rutas accesibles, usa mensajes que no hablan del cuerpo ni prometen resultados y ofrece horarios posibles para distintas personas. También cuida la privacidad: no publica fotos ni ubicaciones sin permiso.",
        "Al terminar, se evalúa con los asistentes y se ajusta. Si un taller tuvo pocas personas, se busca la causa (horario, clima, difusión) y se prueba otro horario. Se compara con los resultados de ejemplo, se celebra la participación y no se juzga a quienes no fueron. Si alguien cuenta que se siente mal o excluido, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("proyecto comunitario", "conjunto de acciones para un grupo de personas de un lugar"), ("público objetivo", "personas a las que se dirige el proyecto"), ("indicador de participación", "número de personas que asisten"), ("autorización", "permiso formal de una persona adulta o de una institución"), ("accesible", "que puede ser usado por distintas personas")],
    worked=[
        ("Calcular asistentes", "Un proyecto de ejemplo tuvo 20, 25 y 30 asistentes en tres actividades. ¿Cuántas personas en total?", ["Suma: 20 + 25 + 30.", "Son 75 asistentes."], "75 asistentes"),
        ("Ajustar con una causa", "Un taller a las 15:00 tuvo pocas personas porque muchas familias trabajan a esa hora. ¿Qué ajuste de una sola condición se propone?", ["La causa observada es el horario, así que se cambia el horario.", "Se propone moverlo a las 18:00."], "Mover el taller a un horario posible, como las 18:00"),
    ],
    mistakes=[("Planear una actividad en un espacio público sin avisar ni pedir autorización.", "Puede haber riesgos y falta de permiso.", "Pide autorización y acompañamiento de personas adultas."),
              ("Usar un mensaje como «ponte en forma antes del verano» para convocar.", "Habla del cuerpo y no informa un beneficio de salud.", "Usa un mensaje honesto con beneficios concretos.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un proyecto comunitario de promoción de actividad física?', 'Acciones organizadas para que más personas de un lugar se muevan con regularidad', 'Una competencia entre cursos con premios para las personas que ganan cada actividad', 'Una publicidad que ofrece productos para mejorar el cuerpo de quienes la ven', 'Es un conjunto de acciones, con objetivo e indicadores, para toda una comunidad.'),
        ('abc', '{F} ¿Cuál es el público al que se dirige el proyecto?', 'Estudiantes y sus familias', 'Solo estudiantes de 4.º medio', 'Solo personas adultas del barrio', 'La ficha indica estudiantes y familias.'),
        ('abc', '{F} ¿Qué indicador usa el proyecto para evaluar?', 'La cantidad de asistentes', 'El peso de las personas participantes', 'La velocidad al caminar', 'La ficha registra los asistentes de cada actividad.'),
        ('=', '{F} ¿Cuántas personas asistieron en total a las tres caminatas?', '18+24+15', 'Se suman los asistentes de las tres caminatas.', ' personas'),
        ('=', '{F} ¿Cuántas personas asistieron en total a los dos talleres de baile?', '30+12', 'Se suman los asistentes de los dos talleres.', ' personas'),
        ('abc', '{F} ¿A qué se atribuye la menor asistencia de la caminata 3?', 'A la lluvia', 'Al horario de trabajo', 'Al presupuesto', 'La ficha dice que llovió ese día.'),
        ('abc', '{F} ¿Por qué el taller 2 tuvo menos asistentes que el taller 1?', 'Se hizo a las 15:00, en horario de trabajo de muchas familias', 'Porque se hizo en un día de lluvia con poca gente en la calle', 'Porque era una actividad de pago y muchas personas no podían pagar', 'La ficha lo atribuye al horario.'),
        ('=', '{F} ¿Cuántos minutos de actividad ofrece el proyecto en total, sumando las 3 caminatas de 30 minutos y los 2 talleres de 40 minutos?', '3*30+2*40', 'Se multiplican actividades por minutos y se suman los dos resultados.', ' minutos'),
        ('abc', '{F} ¿Qué ajuste de una sola condición responde mejor a la causa de la caminata 3?', 'Prever un lugar techado o una fecha alternativa para los días de lluvia', 'Cambiar la caminata por una competencia con premios para quienes lleguen primero', 'Cobrar una entrada para financiar los gastos del proyecto del barrio', 'La causa observada fue la lluvia; se ajusta esa condición con un plan alternativo.'),
        ('=', '{F} Si el taller 2 pasa a tener 30 asistentes en el nuevo horario, ¿cuántas personas más asisten que antes?', '30-12', 'Se resta la asistencia anterior de la nueva.', ' personas'),
        ('abc', 'Un afiche del grupo dice: «Ponte en forma antes del verano; vendrás con tu mejor cuerpo». ¿Qué corresponde?', 'Cambiarlo por un mensaje honesto: «Moverte con otras personas puede ayudarte»', 'Dejarlo como está, porque llama la atención de mucha gente en la plaza del barrio', 'Agregar una foto de personas con cuerpos admirados para que el afiche sea más atractivo', 'El mensaje no debe hablar del cuerpo ni prometer resultados.'),
        ('abc', 'Alguien propone organizar una caminata por el cerro un domingo a las 20:00 sin avisar al colegio. ¿Qué respuesta es más adecuada?', 'No hacerlo así: cambiar a un horario con luz y pedir autorización', 'Hacerlo igual, porque es solo un paseo entre amistades y no necesita permisos', 'Hacerlo, pero llevando linternas pequeñas para todas las personas del grupo', 'Hay riesgo por la oscuridad y la falta de permiso; se organiza con autorización y luz.'),
        ('abc', '{F} Una asistente del taller 1 cuenta, sin dar detalles, que se siente muy sola y sin ganas de estar con otras personas. ¿Qué corresponde al grupo organizador?', 'Escucharla con respeto y avisar a una persona adulta de confianza', 'Prometerle que el ejercicio resolverá todo lo que le pasa en poco tiempo', 'Publicar su comentario en el diario mural para que otras personas la apoyen', 'La preocupación se comunica con respeto a un adulto; no se publica ni se promete una solución.'),
    ],
    ctx=('abc', 'Un grupo de ejemplo quiere organizar una «caminata de la plaza al parque» de 1.000 metros, con luz y semáforos. Con el valor de ejemplo de 250 metros cada 3 minutos, ¿cuánto dura el trayecto, y qué dos cuidados son los más importantes?', '12 minutos; avisar a las familias y contar con personas adultas acompañantes', '10 minutos; mostrar el recorrido en vivo en redes públicas para que se sumen', '15 minutos; cruzar sin semáforo en el camino para llegar un poco antes', '1.000 metros son cuatro tramos de 250, es decir, 12 minutos; la autorización y la compañía son clave.'),
    sc=[
        ("En Educación Física: ¿qué indicador usa un proyecto para evaluar su participación?", "La cantidad de asistentes", "Es un dato que se puede contar siempre igual."),
        ("¿Qué se pide para que participen personas menores de edad?", "Autorización y acompañamiento de personas adultas", "Es parte de la seguridad del proyecto."),
        ("¿Qué no deben mencionar los mensajes de la campaña?", "El cuerpo ni resultados prometidos", "Los mensajes deben ser honestos y respetuosos."),
    ],
    op=("Diseña un proyecto comunitario de ejemplo de una semana activa para tu barrio. Escribe el objetivo, el público, dos acciones con lugar, horario y duración, un mensaje honesto, una autorización necesaria y un indicador. Imagina resultados de ejemplo (asistentes) y propone un ajuste de una sola condición si una actividad tuviera pocas personas.",
        "Objetivo: que más personas del barrio caminen juntas. Público: estudiantes y familias. Acciones: caminata de 30 minutos el sábado a las 17:00 en la plaza; taller de baile el miércoles a las 18:00. Mensaje: «Moverte con otras personas puede ayudarte a sentirte mejor». Autorización: del colegio y de las familias. Indicador: asistentes. Si el taller tuviera 8 personas, lo cambiaría de horario.",
        ["objetivo, público y acciones con lugar y hora", "mensaje honesto, autorización e indicador", "ajuste de una sola condición"],
        ["proyecto comunitario de ejemplo con mensaje, seguridad, indicador y ajuste"],
        ["omitir la autorización", "mensajes sobre el cuerpo", "cambiar varias condiciones a la vez"],
        "Pregunta: «¿qué haría tu proyecto si una actividad tuviera pocas personas y cómo lo sabrías?». Si dice «insistir», pídele un indicador y una causa."),
    reinforce="Escribe un mensaje honesto para convocar a una caminata y revisa que no hable del cuerpo ni prometa resultados.",
    extend="Explica por qué un proyecto comunitario necesita autorización, seguridad y un indicador de participación.",
)

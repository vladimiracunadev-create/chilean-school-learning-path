"""Cuaderno del estudiante, 2.º medio Orientación: OA 10 (diseño flexible, coherente y perseverante del proyecto de vida)."""
from __future__ import annotations

from or_m2_common import M, T, W, lesson
from student_lessons import arith, ex

OA10 = "OR2M OA 10"

lesson(
    OA10, 1,
    "Una hoja y un lápiz. El caso de Elena, una estudiante inventada, está escrito en la clase y en los ejercicios. No necesitas contar tus propios planes.",
    "Aprenderé a examinar un caso ficticio de diseño de proyecto de vida con cinco elementos: habilidades, motivaciones, metas, posibilidades y limitaciones. Sirve para ver cómo se conectan antes de diseñar el mío.",
    ["Sé comparar alternativas de proyecto de vida (OA 1 y OA 9).", "Sé distinguir interés y capacidad."],
    [
        "Diseñar un proyecto de vida es ordenar qué quiero lograr y cómo hacerlo. Se apoya en cinco elementos. Las habilidades son lo que sé hacer o puedo aprender. Las motivaciones son las razones que me impulsan, como ayudar, crear o ser independiente. Las metas personales son lo que quiero lograr en un plazo. Las posibilidades son los apoyos y recursos que tengo. Las limitaciones son lo que dificulta el camino.",
        "Un buen diseño es coherente cuando las decisiones se relacionan con las metas y las motivaciones. Es perseverante cuando se sostiene con esfuerzo aunque haya dificultades. Y es flexible cuando se ajusta si cambian los datos. Estas tres cualidades se necesitan juntas: coherencia sin flexibilidad se rompe y perseverancia sin coherencia no lleva a ninguna parte.",
        "Para examinar un caso se anotan los cinco elementos con datos del caso, se revisa si las decisiones concuerdan con las metas y se piensa dónde hace falta apoyo. Un caso ficticio se analiza en tercera persona, sin exponer a nadie. Si una dificultad afecta mucho el ánimo, se avisa a una persona adulta de confianza.",
    ],
    [("motivación", "razón que impulsa a una persona a actuar"), ("meta personal", "lo que se quiere lograr en un plazo"), ("limitación", "dificultad que hace más difícil el camino"), ("coherente", "que las decisiones concuerdan con las metas"), ("perseverante", "que sigue esforzándose a pesar de las dificultades")],
    [
        W("Separar elementos", "Elena, personaje inventado, dice: «Me motiva ayudar a otros; quiero ser técnica en enfermería en tres años; mi liceo tiene taller de salud». ¿Cuál es la meta y cuál una posibilidad?", ["La meta es lo que quiere lograr en un plazo.", "El taller es un apoyo que ya tiene."], "Meta: ser técnica en enfermería en tres años; posibilidad: el taller del liceo"),
        W("Revisar la coherencia", "Elena quiere ser técnica en enfermería, pero no estudia ciencias ni asiste al taller. ¿Sus decisiones son coherentes con su meta?", ["La meta pide preparación en ciencias.", "Sus decisiones actuales no la apoyan."], "No, todavía no son coherentes"),
    ],
    [
        M("Creer que basta con tener una meta sin mirar las limitaciones.", "Se piensa que querer es suficiente.", "Anota también limitaciones y apoyos para planear."),
        M("Pensar que cambiar de meta es fracasar.", "Se confunde flexibilidad con rendirse.", "Ajustar la meta con nueva información es parte del diseño."),
    ],
    R=[
        ex("Lo que quiero lograr en un plazo es mi A) meta personal B) limitación", "A", "Esa es la definición."),
        ex("Una razón que me impulsa, como ayudar a otros, es una A) motivación B) condición", "A", "Explica por qué actúo."),
        ex("Un taller del liceo que me apoya, ¿es una posibilidad? Responde sí o no.", "Sí", "Es un recurso disponible."),
    ],
    U=[
        ex("Si mis decisiones concuerdan con mis metas, mi diseño es A) coherente B) flexible", "A", "Coherente significa que hay concordancia."),
        ex("Seguir esforzándome a pesar de las dificultades es A) perseverancia B) coherencia", "A", "Implica constancia frente a la dificultad."),
        ex("¿Por qué se necesitan coherencia, perseverancia y flexibilidad juntas? A) Porque se complementan B) Porque son lo mismo", "A", "Cada una compensa límites de las otras."),
    ],
    A=[
        ex("Clasifica con H (habilidad), M (motivación) o L (limitación): 1) Explicar con claridad. 2) Querer ayudar a otros. 3) Vivir lejos del instituto. Escribe las letras en orden.", "H, M, L", "Cada una tiene un rol distinto en el diseño."),
        ex("Elena se propone 3 años para su meta y lleva 1 año. ¿Cuántos años le faltan?", "2", "3 menos 1 son 2."),
        ex("Si Elena solo quiere estudiar y sus decisiones son faltar al taller, ¿qué elemento falla? A) La coherencia B) La motivación", "A", "Sus decisiones no apoyan la meta."),
    ],
    Z=[
        ex("¿Por qué una limitación no siempre cierra un camino?", "Porque a veces se puede reducir con apoyos, tiempo o un plan distinto", "Hay formas de superarla."),
        ex("Un compañero dice: «Si no tengo todo resuelto ahora, no sirve diseñar». ¿Qué respondes? A) Diseñar es avanzar con ajustes B) Tienes razón", "A", "Un proyecto se construye con el tiempo."),
    ],
    D=[
        arith("Elena anota 5 habilidades, 3 motivaciones y 2 metas. ¿Cuántos elementos anota?", "5+3+2", "Se suman los tres grupos."),
        arith("Una meta de 36 meses se divide en etapas iguales de 6 meses. ¿Cuántas etapas hay?", "36//6", "Se divide la meta entre la duración de cada etapa."),
    ],
    context=[ex("En una tutoría inventada, una estudiante dice que quiere ser veterinaria pero no le gustan las ciencias. ¿Qué conviene analizar? A) Si su motivación y su meta son coherentes con lo que requiere esa carrera B) Nada", "A", "Hay una posible falta de coherencia.")],
    selfcheck=[ex("En Orientación: ¿una meta personal es lo que quiero lograr en un plazo?", "Sí", "Tiene tiempo y propósito."), ex("¿La flexibilidad permite ajustar el proyecto?", "Sí", "Se adapta a nuevos datos."), ex("¿Una limitación puede reducirse con apoyos?", "Sí", "A veces sí.")],
    task=T("Lee el caso inventado: Tomás, de 16 años, es hábil para armar circuitos sencillos y aprende rápido; disfruta construir cosas, quiere ser técnico en electricidad y ayudar en su barrio, y sabe que su familia no puede pagar un instituto a mediano plazo. Tiene un tío electricista que puede enseñarle. Escribe: (1) dos habilidades, (2) una motivación, (3) una meta con plazo, (4) una posibilidad y (5) una limitación. Agrega una decisión coherente con su meta.", "Habilidades: armar circuitos y aprender rápido. Motivación: ayudar en su barrio. Meta: ser técnico en electricidad en tres años. Posibilidad: su tío electricista. Limitación: el costo. Decisión: asistir al taller y ahorrar o buscar becas.", ["dos habilidades", "una motivación y una meta con plazo", "una posibilidad y una limitación", "una decisión coherente"], ["texto escrito", "tabla"], ["meta sin plazo", "decisión que no se relaciona con la meta"], "Reconoce los cinco elementos y pregunta qué ajuste haría si cambia la limitación."),
    reinforce="Escribe los cinco elementos de un proyecto inventado de un personaje que quiere ser chef.",
    extend="Explica con un ejemplo inventado por qué la perseverancia sola no basta.",
)

lesson(
    OA10, 2,
    "Una hoja y un lápiz. Los ejemplos de metas y los datos de ejemplo están escritos en los ejercicios.",
    "Aprenderé a distinguir una meta bien formulada de una vaga, y limitaciones reales de aparentes, y a reconocer mitos sobre el proyecto de vida. Sirve para diseñar metas que se puedan lograr.",
    ["Sé reconocer los elementos del proyecto de vida.", "Sé qué es una limitación."],
    [
        "Una meta bien formulada es específica, medible y tiene plazo. Por ejemplo, «aprobar matemática con nota 5,0 o más al final del semestre» cumple las tres. «Ser mejor» no. Para saber si una meta es alcanzable, se revisa si hay pasos concretos que se puedan hacer con el tiempo y los recursos disponibles.",
        "Una limitación real es la que no se puede cambiar hoy, como una edad mínima de ingreso. Una limitación aparente parece fija, pero se puede reducir con apoyo, información o tiempo, como el costo, que a veces se cubre con becas. Distinguirlas evita rendirse antes de tiempo o insistir en lo imposible.",
        "Algunos mitos frenan el diseño: «hay una única vocación para cada persona», «hay que decidir todo ya» o «cambiar es fracasar». Un hecho es que las personas cambian de interés, aprenden nuevas habilidades y ajustan sus proyectos a lo largo de la vida. Y toda persona tiene derecho a decidir sobre su proyecto, sin discriminación.",
    ],
    [("específica", "que dice con claridad qué se quiere lograr"), ("medible", "que se puede comprobar con un dato"), ("plazo", "tiempo en el que se quiere lograr algo"), ("alcanzable", "que se puede lograr con los recursos disponibles"), ("vocación", "inclinación fuerte hacia una actividad")],
    [
        W("Revisar una meta", "«Mejorar en lenguaje» y «subir mi promedio de lenguaje de 5,0 a 5,5 antes de diciembre». ¿Cuál cumple específica, medible y con plazo?", ["La segunda dice cuánto y para cuándo.", "La primera es vaga."], "La segunda"),
        W("Limitación real o aparente", "Una joven inventada no puede pagar un curso de $60.000, pero existe una beca que lo cubre. ¿Es una limitación real o aparente?", ["Se puede reducir con una beca.", "Parece fija pero no lo es."], "Aparente"),
    ],
    [
        M("Escribir metas como «ser feliz» o «ser mejor».", "Se cree que una meta amplia basta.", "Hazla específica, medible y con plazo."),
        M("Creer que hay una sola vocación para toda la vida.", "Se piensa que decidir mal es irreversible.", "Los intereses y habilidades cambian; el proyecto se ajusta."),
    ],
    R=[
        ex("Una meta bien formulada es específica, medible y con A) plazo B) emoción", "A", "El plazo permite organizarla."),
        ex("«Ser mejor» ¿es una meta específica? Responde sí o no.", "No", "No dice qué ni cuánto."),
        ex("Un costo que una beca puede cubrir es una limitación A) aparente B) real", "A", "Se puede reducir con un apoyo."),
    ],
    U=[
        ex("¿Qué meta es medible? A) «Estudiar 3 horas por semana durante 8 semanas» B) «Estudiar más»", "A", "Tiene cantidad y tiempo."),
        ex("Una edad mínima exigida hoy es una limitación A) real hoy B) aparente", "A", "No se puede cambiar de inmediato."),
        ex("«Hay una única vocación para cada persona» es A) un mito B) un hecho", "A", "Las personas cambian de intereses."),
    ],
    A=[
        ex("Clasifica con B (bien formulada) o V (vaga): 1) «Aprobar matemática con 5,0 este semestre.» 2) «Ser mejor persona.» 3) «Leer 4 libros en 6 meses.» Escribe las letras en orden.", "B, V, B", "Las 1 y 3 tienen cantidad y plazo."),
        ex("Una meta de ahorro: $4.000 al mes durante 5 meses. ¿Cuánto habrá ahorrado?", "20.000", "4.000 por 5 son 20.000."),
        ex("Clasifica con R (real) o A (aparente): 1) No tengo computador en casa, pero el liceo presta uno. 2) El curso exige 18 años cumplidos y tengo 16. Escribe las letras en orden.", "A, R", "El computador se puede conseguir; la edad no se puede cambiar hoy."),
    ],
    Z=[
        ex("¿Por qué es útil que una meta sea medible?", "Porque permite comprobar el avance y ajustar el plan", "Se puede saber si se logra."),
        ex("Un compañero dice: «Si cambio de meta, perdí el tiempo». ¿Qué respondes? A) Lo aprendido sirve en el próximo camino B) Tienes razón", "A", "Cada experiencia aporta habilidades."),
    ],
    D=[
        arith("Una estudiante inventada se propone estudiar 40 minutos diarios, de lunes a viernes, durante 8 semanas. ¿Cuántos minutos estudiará en total?", "40*5*8", "Se multiplican los minutos por los días y por las semanas."),
        arith("Una meta de ejemplo: leer 24 páginas por semana durante 6 semanas. ¿Cuántas páginas serán?", "24*6", "Se multiplican las páginas por semana."),
    ],
    context=[ex("En una tutoría inventada, una estudiante dice «quiero estudiar medicina». ¿Qué meta es más específica? A) «Subir mi promedio de ciencias a 6,0 en dos semestres» B) «Ser muy buena»", "A", "Tiene cantidad y plazo.")],
    selfcheck=[ex("En Orientación: ¿una meta medible se puede comprobar?", "Sí", "Tiene un dato."), ex("¿Una limitación aparente se puede reducir?", "Sí", "Con apoyo o información."), ex("¿Hay una única vocación para toda la vida?", "No", "Los intereses cambian.")],
    task=T("Mejora estas tres metas inventadas para que sean específicas, medibles y con plazo: (a) «Estudiar más»; (b) «Ahorrar»; (c) «Mejorar mi inglés». Agrega una limitación y di si es real o aparente, con una razón.", "(a) «Estudiar 3 horas por semana durante 8 semanas.» (b) «Ahorrar $3.000 al mes por 6 meses.» (c) «Aprender 10 palabras nuevas por semana durante 2 meses.» Limitación: el costo de un curso; es aparente porque hay opciones gratuitas.", ["mejora las tres metas", "incluye cantidad y plazo", "agrega una limitación", "justifica real o aparente"], ["texto escrito", "tabla"], ["metas sin plazo", "no justificar"], "Reconoce las metas medibles y pregunta cómo comprobaría su avance."),
    reinforce="Escribe una meta específica, medible y con plazo para un personaje inventado.",
    extend="Explica por qué una limitación aparente no debe tratarse como definitiva.",
)

lesson(
    OA10, 3,
    "Una hoja y un lápiz. Las tres opciones de Raúl, un estudiante inventado, y la tabla están escritas en los ejercicios.",
    "Aprenderé a tomar decisiones coherentes con mis metas, comparando opciones con una tabla de coherencia, esfuerzo y consecuencias. Sirve para elegir lo que acerca a la meta y no solo lo que apetece hoy.",
    ["Sé formular una meta medible.", "Sé distinguir consecuencia inmediata y de largo plazo."],
    [
        "Una decisión es coherente cuando se relaciona con una meta. Para comparar opciones se usan tres preguntas: ¿me acerca a mi meta?, ¿puedo mantenerla con mi tiempo y energía? y ¿cuida mi bienestar? Cada sí vale 1 punto. La opción con más puntos suele ser la más coherente, pero se revisan los datos.",
        "A veces una opción cómoda hoy aleja de la meta mañana. Esa es una consecuencia de largo plazo. Otras veces una opción exigente hoy acerca a la meta pero daña el bienestar si se sostiene sin descanso. Por eso se equilibran el esfuerzo y el cuidado. Un proyecto que destruye la salud no es perseverante, es insostenible.",
        "También hay que decidir cuando otras personas presionan o cuando aparece una oportunidad inesperada. Ahí conviene volver a la meta y preguntar si la decisión la apoya. Si hay dudas, se conversa con una persona adulta de confianza. Decidir con calma es parte de ser autónomo.",
    ],
    [("coherencia", "relación entre las decisiones y las metas"), ("insostenible", "que no se puede mantener sin dañar algo importante"), ("equilibrar", "dar a cada cosa su medida"), ("oportunidad", "ocasión favorable para lograr algo"), ("presión", "empuje de otros para hacer algo")],
    [
        W("Puntuar una opción", "Raúl quiere ser técnico en mecánica. Evalúa asistir a un taller los sábados: me acerca a la meta sí, puedo mantenerla sí, cuida mi bienestar sí. ¿Cuántos puntos suma?", ["Hay tres síes.", "Cada sí vale 1."], "3 puntos"),
        W("Detectar lo insostenible", "Raúl piensa dormir 4 horas para asistir a tres talleres además del liceo. ¿Es sostenible?", ["Dormir tan poco daña el bienestar.", "No podría mantenerlo."], "No, es insostenible"),
    ],
    [
        M("Elegir lo más cómodo de hoy aunque aleje de la meta.", "Se prioriza la consecuencia inmediata.", "Pregunta cómo afecta a tu meta mañana."),
        M("Esforzarse sin descanso para llegar antes.", "Se cree que más sacrificio asegura más logro.", "Equilibra esfuerzo y bienestar."),
    ],
    R=[
        ex("Una decisión que concuerda con mi meta es A) coherente B) insostenible", "A", "Coherencia es concordancia."),
        ex("Dormir muy poco todas las noches para estudiar más, ¿es sostenible? Responde sí o no.", "No", "Daña el bienestar y no se puede mantener."),
        ex("Una opción con tres síes en la tabla, ¿cuántos puntos suma?", "3", "Se cuentan los síes."),
    ],
    U=[
        ex("¿Qué pregunta de la tabla cuida la salud? A) ¿Cuida mi bienestar? B) ¿Es la más fácil?", "A", "Evalúa el equilibrio personal."),
        ex("Ante una oportunidad inesperada, ¿qué haces? A) Vuelves a tu meta y preguntas si la apoya B) La tomas sin pensar", "A", "La meta orienta la decisión."),
        ex("Si te presionan para dejar un taller que te sirve, ¿qué conviene? A) Conversar con una persona adulta de confianza B) Dejarlo enseguida", "A", "Decidir con calma protege tu meta."),
    ],
    A=[
        ex("Raúl evalúa: (1) taller los sábados: sí, sí, sí. (2) Trabajar 40 horas semanales: no, no, no. (3) Estudiar 1 hora diaria: sí, sí, sí. ¿Cuál suma menos?", "La opción 2", "Suma 0, mientras las otras suman 3."),
        ex("Raúl dedica 5 horas por semana al taller y 7 al estudio durante 4 semanas. ¿Cuántas horas suma?", "48", "12 horas por semana por 4 semanas son 48."),
        ex("Clasifica con C (coherente) o N (no coherente) para la meta «ser técnico en mecánica»: 1) Asistir a un taller de mecánica. 2) Dejar de ir a clases de matemática. 3) Practicar con un tío mecánico. Escribe las letras en orden.", "C, N, C", "La 2 aleja de la preparación necesaria."),
    ],
    Z=[
        ex("¿Por qué una decisión cómoda hoy puede ser una mala decisión?", "Porque puede alejar de la meta en el largo plazo", "La comodidad inmediata no mide el futuro."),
        ex("Un compañero dice: «Si me esfuerzo sin parar, seguro logro mi meta». ¿Qué respondes? A) Sin descanso, el esfuerzo se vuelve insostenible B) Tienes razón", "A", "Sostener el proyecto exige cuidar el bienestar."),
    ],
    D=[
        arith("Raúl tiene 3 opciones con 3 preguntas cada una. ¿Cuántas respuestas da?", "3*3", "Se multiplican opciones por preguntas."),
        arith("Una semana de Raúl: 8 horas de liceo diarias por 5 días y 6 horas de taller. ¿Cuántas horas de actividades tiene?", "8*5+6", "Se suman las horas de liceo y de taller."),
    ],
    context=[ex("En un fin de semana inventado, Raúl puede ir al taller o a una fiesta de la que vuelve tarde y al día siguiente tiene una prueba. ¿Qué pregunta de la tabla debe revisar? A) Si lo acerca a su meta y cuida su bienestar B) Si es más divertido", "A", "Mira meta y bienestar a la vez.")],
    selfcheck=[ex("En Orientación: ¿una decisión coherente se relaciona con mi meta?", "Sí", "Es su definición."), ex("¿Un proyecto que daña la salud es sostenible?", "No", "No se puede mantener."), ex("¿Se puede conversar con una persona adulta de confianza ante presión?", "Sí", "Ayuda a decidir con calma.")],
    task=T("Compara estas tres decisiones de Camila, personaje inventado, que quiere entrar a una carrera técnica en un año: (1) estudiar 1 hora diaria de lunes a viernes; (2) estudiar 6 horas diarias durmiendo 4; (3) dejar de estudiar hasta ver qué pasa. Usa las tres preguntas (acerca a la meta, sostenible, cuida bienestar), suma puntos, elige y escribe una consecuencia de largo plazo de cada una.", "(1) sí, sí, sí = 3. (2) sí, no, no = 1. (3) no, sí, sí = 2. Elige la 1. Largo plazo: (1) preparación sostenida; (2) agotamiento; (3) menor preparación.", ["responde las tres preguntas por opción", "suma bien", "elige y justifica", "escribe consecuencias"], ["tabla escrita", "texto breve"], ["sumar mal", "elegir lo insostenible"], "Reconoce la tabla y pregunta cómo equilibraría el esfuerzo con el descanso."),
    reinforce="Compara con las tres preguntas dos formas de estudiar para una prueba inventada.",
    extend="Explica cómo cambiaría tu tabla si una oportunidad inesperada aparece.",
)

lesson(
    OA10, 4,
    "Una hoja y un lápiz. Los casos de esfuerzo y de bienestar están escritos en los ejercicios; los personajes son inventados.",
    "Aprenderé a perseverar de forma segura y sostenible, cuidando la salud y pidiendo ayuda cuando una dificultad me supera. Sirve para sostener un proyecto sin dañarme.",
    ["Sé tomar decisiones coherentes con una meta.", "Sé armar un mensaje de hecho, emoción y petición."],
    [
        "Perseverar es seguir trabajando por una meta aunque haya dificultades. Una perseverancia segura es la que se puede mantener sin dañar la salud. Eso incluye dormir lo suficiente, comer con regularidad, tener tiempo de descanso y mantener vínculos. Cuando se pierde el equilibrio, el esfuerzo se vuelve agotamiento y el proyecto corre riesgo.",
        "Hay señales de que una dificultad supera a la persona: cansancio constante, tristeza prolongada, pérdida de interés en todo o ganas de rendirse por completo. Ante ellas la acción segura es contarlo a una persona adulta de confianza y pedir apoyo, sin esperar a que pase solo. Si alguna vez piensas en hacerte daño, avisa de inmediato a una persona adulta de confianza. Pedir ayuda no es debilidad: es una estrategia para seguir.",
        "También ayuda dividir la meta en pasos pequeños, celebrar los avances y aceptar que habrá semanas más difíciles. Un tropiezo no borra lo logrado. Si el malestar es fuerte, el Fono Niños 147 puede orientar a adolescentes, siempre junto con el aviso a una persona adulta de confianza.",
    ],
    [("perseverar", "seguir esforzándose a pesar de las dificultades"), ("agotamiento", "cansancio extremo por exceso de esfuerzo"), ("señal", "indicio de que algo ocurre"), ("paso pequeño", "tarea breve que acerca a la meta"), ("tropiezo", "dificultad o error en el camino")],
    [
        W("Reconocer la señal", "Un estudiante inventado lleva tres semanas muy triste, sin ganas de nada y sin dormir bien. ¿Qué acción es segura?", ["Es un malestar prolongado.", "Necesita apoyo."], "Contarlo a una persona adulta de confianza"),
        W("Dividir la meta", "Una meta de leer 120 páginas en 6 semanas, ¿cuántas páginas por semana son si se reparten igual?", ["Se divide el total entre las semanas.", "120 dividido en 6."], "20 páginas por semana"),
    ],
    [
        M("Guardar el malestar para no preocupar a otros.", "Se cree que pedir ayuda molesta.", "Cuéntalo a una persona adulta de confianza."),
        M("Pensar que un tropiezo borra todo lo logrado.", "Se mira solo el último resultado.", "Reconoce los avances y ajusta el plan."),
    ],
    R=[
        ex("Seguir esforzándose a pesar de las dificultades es A) perseverar B) rendirse", "A", "Esa es la definición."),
        ex("Tristeza prolongada y sin ganas de nada, ¿es una señal para pedir apoyo? Responde sí o no.", "Sí", "Es un malestar que merece ayuda."),
        ex("Dormir lo suficiente, ¿ayuda a perseverar sin dañarse? Responde sí o no.", "Sí", "Mantiene la energía y el ánimo."),
    ],
    U=[
        ex("¿Qué hace segura a la perseverancia? A) Que se pueda mantener sin dañar la salud B) Que no tenga descansos", "A", "Debe ser sostenible."),
        ex("¿Por qué conviene dividir la meta en pasos pequeños? A) Porque es más fácil avanzar y celebrar B) Porque tarda más", "A", "Cada paso muestra avance."),
        ex("Si el malestar es fuerte, ¿qué se hace? A) Se cuenta a una persona adulta de confianza B) Se espera sin decir nada", "A", "Es la acción segura."),
    ],
    A=[
        ex("Clasifica con S (señal de pedir apoyo) o N (normal): 1) Cansancio después de un día intenso. 2) Tristeza durante semanas. 3) Querer rendirse por completo y no disfrutar nada. Escribe las letras en orden.", "N, S, S", "Los malestares prolongados necesitan apoyo."),
        ex("Una meta de 90 minutos de práctica por semana se reparte en 3 días iguales. ¿Cuántos minutos por día?", "30", "90 dividido en 3 son 30."),
        ex("Un tropiezo en una prueba, ¿qué conviene? A) Revisar qué falló y ajustar el plan B) Abandonar la meta", "A", "Se aprende del resultado."),
    ],
    Z=[
        ex("¿Por qué pedir ayuda es una estrategia de perseverancia?", "Porque permite seguir con apoyo cuando una dificultad es más grande de lo que se puede manejar solo", "La ayuda sostiene el esfuerzo."),
        ex("Un compañero dice: «Quien pide ayuda no es perseverante». ¿Qué respondes? A) Quien pide ayuda puede seguir más tiempo B) Tienes razón", "A", "Pedir apoyo evita el agotamiento."),
    ],
    D=[
        arith("Un estudiante de ejemplo planea 4 pasos pequeños y completa 3 en el mes. ¿Cuántos pasos le faltan?", "4-3", "Al total se le restan los completados."),
        arith("Una meta de 240 minutos de estudio en la semana se reparte entre 6 días. ¿Cuántos minutos por día?", "240//6", "Se divide el total entre los días."),
    ],
    context=[ex("Una estudiante inventada cuenta a su profesora jefe que lleva semanas muy cansada y triste. ¿Qué hace la profesora? A) Escucha y la ayuda a conectar con apoyo adecuado B) Le dice que es una exageración", "A", "Un malestar prolongado merece atención.")],
    selfcheck=[ex("En Orientación: ¿perseverar exige cuidar la salud?", "Sí", "Debe ser sostenible."), ex("¿Pedir ayuda es una estrategia?", "Sí", "Ayuda a seguir."), ex("¿Un tropiezo borra lo logrado?", "No", "Los avances siguen.")],
    task=T("Lee el caso inventado: Sara se propone entrar a una carrera técnica el próximo año. En las últimas semanas duerme poco, se siente muy cansada y piensa que no vale la pena seguir. Escribe: (1) dos señales que aparecen, (2) una acción segura inmediata, (3) un paso pequeño para retomar su plan y (4) a qué persona adulta le contaría.", "Señales: cansancio y pensamiento de que no vale la pena. Acción segura: contarlo a una persona adulta de confianza. Paso pequeño: estudiar 30 minutos diarios. Persona adulta: de su casa, el profesor jefe o la orientadora.", ["dos señales", "una acción segura", "un paso pequeño", "una persona adulta"], ["texto escrito", "tabla"], ["guardar el secreto", "paso demasiado grande"], "Reconoce las señales y pregunta cómo celebraría el primer avance."),
    reinforce="Divide en tres pasos pequeños una meta inventada de leer un libro en un mes.",
    extend="Explica por qué dividir una meta ayuda a perseverar.",
)

lesson(
    OA10, 5,
    "Una hoja y un lápiz. Las frases para presentar y pedir apoyo están escritas en los ejercicios.",
    "Aprenderé a comunicar mi proyecto de forma clara a una persona adulta y a pedir el apoyo que necesito. Sirve para recibir orientación en vez de decidir solo.",
    ["Sé formular una meta medible.", "Sé pedir ayuda con hecho, emoción y petición."],
    [
        "Comunicar un proyecto de vida es explicar con claridad qué quiero lograr, por qué y qué apoyo necesito. Un esquema simple tiene cuatro partes: la meta con su plazo, la motivación, los pasos que ya doy y la petición concreta. Por ejemplo: «Quiero ser técnica en enfermería en tres años porque me gusta ayudar; ya asisto al taller de salud; necesito información sobre becas».",
        "Conviene elegir bien a quién se lo cuentas. Puede ser una persona de tu casa, un profesor, la persona orientadora o un profesional del trabajo que te interesa. Lo ideal es pedir una conversación con tiempo y llevar tus preguntas escritas. Escuchar consejos no obliga a seguirlos todos, pero sí a considerarlos con respeto.",
        "Si alguien dice que tu proyecto «no sirve», no lo tomes como un hecho. Pide razones, revisa si hay datos útiles y, si hay un prejuicio, busca otra opinión. Y si una presión te angustia, cuéntalo a una persona adulta de confianza. Un proyecto es tuyo, pero se construye mejor con apoyo.",
    ],
    [("petición concreta", "pedido claro de algo específico"), ("orientación", "ayuda para tomar decisiones informadas"), ("consejo", "opinión de otra persona para ayudar a decidir"), ("preguntas escritas", "dudas anotadas antes de una conversación"), ("prejuicio", "opinión sin base sobre una persona o grupo")],
    [
        W("Armar el mensaje", "Un estudiante dice: «Quiero ser técnico en electricidad en tres años porque me gusta construir; ya asisto a un taller; necesito saber qué becas existen». ¿Cuál es la petición?", ["La petición dice lo que necesita.", "Es la última parte."], "Saber qué becas existen"),
        W("Responder a un prejuicio", "Alguien le dice: «Eso no es para ti». ¿Qué responde con respeto?", ["Pide razones.", "Busca otra opinión si no hay datos."], "«¿Qué datos tienes?», y consultar a la orientadora"),
    ],
    [
        M("Pedir ayuda sin decir qué se necesita.", "Se supone que el otro adivinará.", "Incluye una petición concreta."),
        M("Creer que hay que seguir todos los consejos.", "Se confunde escuchar con obedecer.", "Escucha, evalúa y decide tú."),
    ],
    R=[
        ex("¿Qué parte del mensaje dice qué apoyo necesito? A) La petición concreta B) La motivación", "A", "Es lo que se pide."),
        ex("Llevar las preguntas escritas a una conversación, ¿ayuda? Responde sí o no.", "Sí", "Ordena la conversación."),
        ex("Escuchar un consejo, ¿obliga a seguirlo? Responde sí o no.", "No", "Se considera, pero decides tú."),
    ],
    U=[
        ex("¿Qué incluye un buen mensaje de proyecto? A) Meta con plazo, motivación, pasos y petición B) Solo quejas", "A", "Son las cuatro partes."),
        ex("Si te dicen «no sirve» sin razones, ¿qué haces? A) Pides razones y revisas datos B) Abandonas", "A", "Evalúas si es un hecho o un prejuicio."),
        ex("¿A quién puedes pedir una conversación? A) A una persona adulta de confianza o a la orientadora B) A nadie", "A", "Son fuentes de apoyo."),
    ],
    A=[
        ex("Ordena con letras las partes: (a) «Necesito información sobre becas.» (b) «Quiero ser técnica en enfermería en tres años.» (c) «Ya asisto al taller de salud.» ¿Cuál es la petición?", "a", "Dice lo que se necesita."),
        ex("Clasifica con M (meta), P (pasos que ya doy) o S (petición): 1) «Asisto al taller de salud.» 2) «Quiero entrar a una carrera técnica en dos años.» 3) «Necesito información sobre becas.» Escribe las letras en orden.", "P, M, S", "Cada frase cumple una función."),
        ex("Un estudiante lleva 6 preguntas escritas y la orientadora responde 4. ¿Cuántas quedan?", "2", "6 menos 4 son 2."),
    ],
    Z=[
        ex("¿Por qué distinguir un hecho de un prejuicio en un comentario sobre tu proyecto?", "Porque un hecho tiene datos y un prejuicio solo una opinión sin base", "Permite decidir mejor."),
        ex("Un compañero dice: «Mi proyecto es mío, no necesito a nadie». ¿Qué respondes? A) Es tuyo, pero el apoyo lo fortalece B) Tienes razón", "A", "Pedir orientación no quita autonomía."),
    ],
    D=[
        arith("Una conversación dura 30 minutos: 10 para presentar el proyecto y el resto para preguntas. ¿Cuántos minutos son para preguntas?", "30-10", "Al total se le restan los minutos de presentación."),
        arith("Un grupo de ejemplo ensaya su presentación 3 veces de 5 minutos. ¿Cuántos minutos ensaya?", "3*5", "Se multiplican las veces por los minutos."),
    ],
    context=[ex("Un estudiante inventado quiere hablar con su profesor jefe sobre su proyecto. ¿Qué frase abre mejor? A) «Necesito conversar con usted sobre mi proyecto y pedirle orientación.» B) «No sé nada.»", "A", "Pide atención y orientación concreta.")],
    selfcheck=[ex("En Orientación: ¿un mensaje de proyecto incluye una petición concreta?", "Sí", "Así queda claro el apoyo."), ex("¿Escuchar un consejo obliga a seguirlo?", "No", "La decisión final es tuya."), ex("¿Pedir orientación quita autonomía?", "No", "La fortalece con más información.")],
    task=T("Escribe un mensaje de proyecto de cuatro partes (meta con plazo, motivación, pasos que ya das y petición) para este personaje inventado: Daniel quiere ser técnico en gastronomía en dos años, le gusta cocinar para su familia y ya practica los fines de semana. Elige a quién se lo contaría, escribe una frase para abrir la conversación y qué respondería si alguien le dice que «eso no es para ti».", "«Necesito conversar contigo sobre mi proyecto. Quiero ser técnico en gastronomía en dos años porque me gusta cocinar para mi familia. Ya practico los fines de semana. Necesito información sobre institutos y becas.» Respuesta al prejuicio: «¿Qué datos tienes?» y consultar a la orientadora.", ["cuatro partes", "elige a una persona adulta", "frase de apertura", "responde al prejuicio con respeto"], ["texto escrito", "ensayo oral"], ["omitir la petición", "aceptar el prejuicio sin revisar"], "Reconoce el mensaje completo y pregunta qué dato sumaría."),
    reinforce="Escribe una petición concreta para un personaje inventado que busca orientación vocacional.",
    extend="Explica cómo cambiaría tu mensaje si hablaras con una persona de tu casa.",
)

lesson(
    OA10, 6,
    "Una hoja y un lápiz. El personaje, Benjamín, es inventado y sus datos están en el enunciado. No escribas nada sobre ti.",
    "Aprenderé a transferir lo aprendido diseñando, sin exposición personal, un proyecto de vida de un personaje inventado con metas, pasos, indicadores y revisión. Sirve para practicar el método antes de aplicarlo a mi caso.",
    ["Sé formular metas medibles.", "Sé perseverar con equilibrio."],
    [
        "Un diseño de proyecto de vida completo reúne seis partes: habilidades y motivaciones, una meta con plazo, pasos intermedios, posibilidades y limitaciones, indicadores y revisión. Un indicador es un dato que muestra si avanzas, como horas de estudio, notas o ahorro. La revisión es un momento fijo para mirar los indicadores y ajustar.",
        "Para transferir el método se aplica a un personaje inventado: se anotan sus habilidades y motivaciones, se propone una meta, se divide en pasos y se piensa qué apoyos y obstáculos hay. Esto permite practicar sin contar nada privado. Luego, cada persona podrá aplicar lo mismo a su propio caso, con quien ella elija.",
        "Un buen diseño es coherente, perseverante y flexible. Dice qué hacer ahora, qué hacer si algo falla y a quién pedir ayuda. Y no se compromete a un único camino, sino a un proceso que se revisa. Si el personaje enfrenta una dificultad fuerte, la revisión incluye avisar a una persona adulta de confianza.",
    ],
    [("indicador", "dato que muestra si se avanza"), ("revisión", "momento para mirar el avance y ajustar"), ("paso intermedio", "tarea entre el inicio y la meta"), ("proceso", "serie de pasos que se repiten y mejoran"), ("transferir", "aplicar lo aprendido a otro caso")],
    [
        W("Elegir un indicador", "Benjamín, personaje inventado, quiere subir su nota de matemática. ¿Qué indicador sirve: sus notas de las pruebas o el color de su cuaderno?", ["Un indicador muestra avance.", "Las notas se comparan en el tiempo."], "Sus notas de las pruebas"),
        W("Fijar la revisión", "Benjamín se propone revisar su avance el último viernes de cada mes. ¿Eso es una revisión?", ["Es un momento fijo.", "Sirve para mirar los indicadores."], "Sí"),
    ],
    [
        M("Diseñar una meta sin indicadores.", "Se cree que bastan las ganas.", "Define un dato para saber si avanzas."),
        M("Hacer un plan rígido que no se revisa nunca.", "Se confunde constancia con inflexibilidad.", "Fija momentos de revisión y ajusta."),
    ],
    R=[
        ex("Un dato que muestra si se avanza es un A) indicador B) obstáculo", "A", "Esa es su función."),
        ex("Un momento fijo para mirar el avance y ajustar es la A) revisión B) limitación", "A", "Permite corregir el plan."),
        ex("Aplicar lo aprendido a otro caso es A) transferir B) olvidar", "A", "Esa es la definición."),
    ],
    U=[
        ex("¿Por qué un personaje inventado sirve para practicar? A) Porque no expone datos privados B) Porque es más fácil mentir", "A", "Se aprende el método con seguridad."),
        ex("¿Qué debe incluir un diseño además de la meta? A) Pasos, indicadores y revisión B) Solo un deseo", "A", "Son partes del diseño."),
        ex("Si el personaje tiene una dificultad fuerte, ¿qué incluye la revisión? A) Avisar a una persona adulta de confianza B) Ignorarla", "A", "El bienestar es parte del proyecto."),
    ],
    A=[
        ex("Clasifica con I (indicador) o L (limitación) para Benjamín: 1) Horas de estudio por semana. 2) No tiene computador en su casa. 3) Notas de las pruebas del mes. Escribe las letras en orden.", "I, L, I", "Las 1 y 3 miden avance; la 2 dificulta el camino."),
        ex("Benjamín quiere pasar de 4,8 a 5,6 en 4 meses subiendo lo mismo cada mes en décimas. ¿Cuántas décimas sube por mes?", "2", "Hay 8 décimas de diferencia y 8 dividido en 4 son 2."),
        ex("Si en la revisión el indicador no mejora, ¿qué conviene? A) Ajustar el plan o pedir apoyo B) Abandonar de inmediato", "A", "La revisión sirve para corregir."),
    ],
    Z=[
        ex("¿Por qué el diseño debe decir qué hacer si algo falla?", "Porque así el proyecto se puede ajustar sin abandonarlo", "Un plan para imprevistos da flexibilidad."),
        ex("Un compañero dice: «Con una buena meta no hace falta revisar». ¿Qué respondes? A) Revisar permite ajustar al cambiar los datos B) Tienes razón", "A", "Los proyectos son flexibles."),
    ],
    D=[
        arith("Benjamín registra 3 indicadores por mes durante 6 meses. ¿Cuántos registros hace?", "3*6", "Se multiplican indicadores por meses."),
        arith("Su plan tiene 8 pasos intermedios y ya cumplió 5. ¿Cuántos faltan?", "8-5", "Al total se le restan los cumplidos."),
    ],
    context=[ex("En una feria de proyectos, un grupo muestra el diseño de un personaje inventado con meta, pasos, indicadores y revisión. ¿Qué parte demuestra flexibilidad? A) La revisión periódica con ajustes B) La meta final", "A", "Permite cambiar según los datos.")],
    selfcheck=[ex("En Orientación: ¿un indicador muestra avance?", "Sí", "Es un dato medible."), ex("¿Un plan debe revisarse?", "Sí", "Así se ajusta."), ex("¿Un personaje inventado protege la privacidad?", "Sí", "No se usan datos reales.")],
    task=T("Diseña un proyecto de vida completo para el personaje inventado Benjamín (16 años), a quien le gusta la tecnología, es bueno explicando, quiere trabajar en informática y no tiene computador propio. Incluye: (1) dos habilidades y una motivación, (2) una meta con plazo, (3) tres pasos intermedios, (4) una posibilidad y una limitación, (5) un indicador y (6) cuándo revisará y a quién pediría apoyo.", "Habilidades: explicar y aprender tecnología. Motivación: trabajar en informática. Meta: terminar el módulo de computación del liceo con nota 6,0 en un año. Pasos: usar el laboratorio, hacer práctica semanal, buscar taller. Posibilidad: laboratorio del liceo. Limitación: no tiene computador. Indicador: horas de práctica por semana. Revisión: último viernes de cada mes con el profesor jefe.", ["seis partes completas", "meta con plazo", "indicador y revisión", "persona de apoyo"], ["plan escrito", "tabla"], ["omitir indicadores", "plan que no se revisa"], "Reconoce el diseño completo y pregunta qué ajuste haría si el indicador no mejora."),
    reinforce="Escribe un indicador y una fecha de revisión para una meta inventada de ahorro.",
    extend="Explica por qué practicar con un personaje inventado antes de aplicar el método a tu propio proyecto.",
)

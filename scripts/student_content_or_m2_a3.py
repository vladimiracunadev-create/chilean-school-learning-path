"""Cuaderno del estudiante, 2.º medio Orientación: OA 04 (acciones autónomas para una vida saludable)."""
from __future__ import annotations

from or_m2_common import M, T, W, lesson
from student_lessons import arith, ex

OA4 = "OR2M OA 04"

lesson(
    OA4, 1,
    "Una hoja y un lápiz. El caso de Gabriela, una estudiante inventada, está escrito en la clase y en los ejercicios. No necesitas contar tus hábitos.",
    "Aprenderé a examinar un caso ficticio de vida saludable con cuatro áreas: alimentación, estrés, tiempo de ocio y seguridad personal. Sirve para reconocer qué hábitos cuidan y cuáles desgastan.",
    ["Sé que mis decisiones influyen en mi bienestar (1.º medio).", "Sé que puedo pedir ayuda a una persona adulta de confianza."],
    [
        "Una vida saludable es el conjunto de hábitos que cuidan el cuerpo, las emociones y los vínculos. En este nivel se miran cuatro áreas. La alimentación, que es lo que comemos y con qué regularidad. El manejo del estrés, que es cómo reaccionamos ante la presión. El uso del tiempo de ocio, que es lo que hacemos cuando no estudiamos ni trabajamos. Y la seguridad personal, que es evitar riesgos en situaciones de todos los días.",
        "Actuar de manera autónoma significa decidir y hacer por iniciativa propia, pensando en el cuidado de sí mismo y de los demás. No significa hacerlo todo solo: una persona autónoma también sabe cuándo pedir ayuda. Un hábito saludable es una acción que se repite y que favorece el bienestar, como dormir lo suficiente o moverse un rato cada día.",
        "Para examinar un caso se anotan los hechos de cada área, se distingue qué hábito cuida y cuál desgasta, y se piensa qué cambio pequeño y posible haría diferencia. Un cambio pequeño y constante vale más que uno grande que no se sostiene. Y si algo afecta mucho el ánimo o la salud, se avisa a una persona adulta de confianza.",
    ],
    [("hábito", "acción que se repite y afecta el bienestar"), ("autonomía", "capacidad de decidir y actuar por iniciativa propia"), ("estrés", "tensión del cuerpo y la mente ante una presión"), ("ocio", "tiempo libre que se usa en actividades elegidas"), ("seguridad personal", "evitar riesgos en situaciones cotidianas")],
    [
        W("Clasificar un hábito", "En el caso, Gabriela se acuesta a las 2 de la madrugada casi todos los días y le cuesta levantarse. ¿Es un hábito que cuida o que desgasta?", ["Dormir poco afecta la energía y la concentración.", "Se repite casi todos los días."], "Es un hábito que desgasta"),
        W("Elegir un cambio posible", "Gabriela quiere cambiar muchas cosas a la vez y se agota. ¿Qué cambio conviene proponerle?", ["Un cambio pequeño es más fácil de sostener.", "Por ejemplo, acostarse 15 minutos antes."], "Un cambio pequeño y constante"),
    ],
    [
        M("Pensar que ser autónomo es no pedir ayuda nunca.", "Se confunde independencia con aislarse.", "Una persona autónoma decide, pero también pide apoyo cuando hace falta."),
        M("Intentar cambiar todos los hábitos de golpe.", "Se piensa que un gran cambio es más serio.", "Parte por uno pequeño y mantenlo varias semanas."),
    ],
    R=[
        ex("Dormir lo suficiente cada noche, ¿es un hábito que cuida o que desgasta?", "Que cuida", "Favorece la energía y el bienestar."),
        ex("¿Qué es el ocio? A) El tiempo libre que se usa en actividades elegidas B) El tiempo de las tareas del colegio", "A", "Se refiere al tiempo que no está dedicado a obligaciones."),
        ex("En Orientación: ¿ser autónomo incluye saber cuándo pedir ayuda?", "Sí", "La autonomía no significa hacerlo todo solo."),
    ],
    U=[
        ex("Gabriela se come el almuerzo mirando el celular y casi no lo prueba. ¿En qué área de vida saludable cae? A) Alimentación B) Seguridad personal", "A", "Habla de cómo y qué come."),
        ex("Gabriela siente que el corazón le late rápido antes de una prueba. ¿A qué área pertenece? A) Manejo del estrés B) Tiempo de ocio", "A", "Es una reacción corporal ante una presión."),
        ex("¿Por qué conviene un cambio pequeño y constante? A) Porque se puede sostener en el tiempo B) Porque no sirve para nada", "A", "Lo que se mantiene produce efecto."),
    ],
    A=[
        ex("Clasifica con A (alimentación), E (estrés) u O (ocio): 1) Gabriela practica vóleibol los viernes. 2) Se salta el desayuno. 3) Respira lento antes de rendir una prueba. Escribe las letras en orden.", "O, A, E", "El vóleibol es ocio, el desayuno es alimentación y respirar lento maneja el estrés."),
        ex("Gabriela duerme 5 horas cada noche de lunes a viernes. ¿Cuántas horas duerme en esos 5 días?", "25", "5 horas por noche durante 5 noches son 25 horas."),
        ex("Si Gabriela cuenta que se siente triste hace semanas y sin energía, ¿qué paso corresponde? A) Conversarlo con una persona adulta de confianza B) Guardarlo para que nadie se preocupe", "A", "Un malestar prolongado requiere apoyo."),
    ],
    Z=[
        ex("¿Por qué un hábito como moverse un rato al día ayuda tanto al estrés como al ánimo?", "Porque el movimiento libera tensión del cuerpo y mejora cómo nos sentimos", "El cuerpo y las emociones están conectados."),
        ex("Un compañero dice: «Cuidarme es egoísta». ¿Qué respondes? A) Cuidarme me permite también cuidar a otros B) Tiene razón, es egoísta", "A", "Estar bien permite apoyar a los demás."),
    ],
    D=[
        arith("Gabriela se propone caminar 20 minutos al día durante 6 días. ¿Cuántos minutos camina en total?", "20*6", "Se multiplican los minutos por los días."),
        ex("Gabriela anotó cuatro hábitos: dormir tarde, caminar, saltarse el desayuno y conversar con un amigo. ¿Cuántos son hábitos que cuidan? A) 2 B) 4", "A", "Caminar y conversar con un amigo cuidan; los otros dos desgastan."),
    ],
    context=[ex("En una charla escolar, una estudiante cuenta un caso inventado: Andrés pasa 6 horas seguidas en videojuegos y no come a su hora. ¿Qué área de vida saludable está más afectada? A) El uso del tiempo de ocio y la alimentación B) La seguridad personal únicamente", "A", "El tiempo libre sin límite desordena la comida.")],
    selfcheck=[ex("En Orientación: ¿un hábito es una acción que se repite y afecta el bienestar?", "Sí", "Puede cuidar o desgastar."), ex("¿Un cambio pequeño y constante puede ser mejor que uno grande?", "Sí", "Se sostiene más tiempo."), ex("¿Avisar a una persona adulta de confianza forma parte de cuidarse?", "Sí", "Pedir ayuda es una decisión autónoma.")],
    task=T("Lee el caso inventado: Sebastián, de 16 años, duerme poco por estudiar de noche, almuerza lo que hay en el quiosco, se siente muy tenso antes de las pruebas y casi no sale de su casa los fines de semana. Escribe: (1) un hábito que cuida o desgasta en cada una de las cuatro áreas (alimentación, estrés, ocio, seguridad personal si aparece), (2) un cambio pequeño para una de ellas y (3) a qué persona adulta le contaría que se siente muy tenso.", "Alimentación: almuerza lo que hay, desgasta. Estrés: tensión antes de pruebas, desgasta. Ocio: casi no sale, desgasta. Cambio pequeño: acostarse 15 minutos antes. Persona adulta: de su casa o la orientadora.", ["analiza al menos tres áreas", "propone un cambio pequeño y posible", "indica a una persona adulta de confianza", "no cuenta datos personales"], ["texto escrito", "tabla"], ["proponer cambios enormes", "olvidar pedir apoyo"], "Reconoce el análisis por áreas y pregunta cómo sostendría el cambio durante un mes."),
    reinforce="Anota un hábito que cuida y uno que desgasta de un personaje inventado, sin usar tu vida.",
    extend="Explica con un ejemplo inventado cómo pedir ayuda puede ser parte de ser autónomo.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. Los datos de las etiquetas y de los horarios son de ejemplo y están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos, mitos y límites sobre alimentación, sueño, estrés y seguridad, usando información confiable. Sirve para decidir sin dejarme llevar por modas ni rumores.",
    ["Sé examinar un caso con cuatro áreas de vida saludable.", "Sé qué es una fuente confiable."],
    [
        "Un hecho en vida saludable es una información que se respalda en fuentes confiables, como un centro de salud, un nutricionista o el Ministerio de Salud. Un mito es una creencia popular sin respaldo. Por ejemplo, «los alimentos con sellos negros son malos para siempre» es una simplificación. En Chile los envases llevan sellos de advertencia «ALTO EN» cuando un producto tiene mucho azúcar, sodio, grasas saturadas o calorías, y sirven para decidir con más información.",
        "Hay hechos útiles para la edad. Dormir lo suficiente, que en la adolescencia suele ser entre 8 y 10 horas, ayuda a concentrarse y a manejar el ánimo. Tomar agua, comer con regularidad y moverse a diario son hábitos que cuidan. El estrés ocasional es normal, pero si es muy intenso o dura mucho tiempo conviene hablarlo con una persona adulta de confianza.",
        "En seguridad personal hay límites que protegen: usar casco en bicicleta, abrocharse el cinturón en un auto, cruzar por el paso de peatones y avisar a alguien de casa a dónde se va. Los límites no son castigos, son cuidados. Y toda persona tiene derecho a acceder a información y atención de salud.",
    ],
    [("sello de advertencia", "símbolo negro que indica que un producto tiene mucho de un nutriente"), ("nutricionista", "profesional que orienta sobre alimentación"), ("hecho", "información respaldada en una fuente confiable"), ("mito", "creencia popular sin respaldo"), ("límite de seguridad", "norma que cuida a las personas, como el casco")],
    [
        W("Leer un sello", "Una galleta de ejemplo trae un sello «ALTO EN azúcares». ¿Qué significa?", ["El sello es una advertencia de nutrientes.", "Indica mucha cantidad de azúcares."], "Que tiene mucha cantidad de azúcares"),
        W("Detectar un mito", "Un video dice: «Dormir 4 horas es lo mejor para rendir más». ¿Es un hecho o un mito?", ["Dormir poco afecta la concentración.", "No tiene respaldo en fuentes de salud."], "Es un mito"),
    ],
    [
        M("Pensar que un sello de advertencia significa que nunca se puede comer ese producto.", "Se confunde la advertencia con una prohibición.", "El sello informa: se decide cuánto y con qué frecuencia."),
        M("Creer que usar casco es solo para quienes andan rápido.", "Se piensa que el riesgo depende solo de la velocidad.", "Una caída puede ocurrir a cualquier velocidad; el casco protege siempre."),
    ],
    R=[
        ex("Un sello «ALTO EN sodio» advierte que el producto tiene mucha sal. ¿Es una advertencia o una prohibición?", "Una advertencia", "Informa para que cada persona decida."),
        ex("¿Cuántas horas suelen recomendarse de sueño en la adolescencia? A) Entre 8 y 10 horas B) Entre 3 y 4 horas", "A", "Es el rango habitual recomendado."),
        ex("Usar casco en bicicleta, ¿es un límite que cuida? Responde sí o no.", "Sí", "Protege la cabeza en una caída."),
    ],
    U=[
        ex("¿Dónde conviene preguntar por una dieta? A) A un nutricionista o centro de salud B) En un video sin autor", "A", "Profesionales dan información comprobada."),
        ex("Una tarjeta dice: «Tomar agua durante el día ayuda al cuerpo». ¿Es un hecho o un mito? A) Un hecho B) Un mito", "A", "Es una recomendación de salud respaldada."),
        ex("El estrés intenso que dura semanas, ¿qué requiere? A) Hablarlo con una persona adulta de confianza B) Ignorarlo", "A", "Un malestar prolongado merece apoyo."),
    ],
    A=[
        ex("Clasifica con H (hecho) o M (mito): 1) «Saltarse comidas siempre ayuda a bajar de peso sano.» 2) «Moverse a diario ayuda al ánimo.» 3) «Cruzar por el paso peatonal reduce el riesgo.» Escribe las letras en orden.", "M, H, H", "La 1 es una creencia sin respaldo; la 2 y la 3 son hábitos de cuidado."),
        ex("Dos jugos de ejemplo: el A trae 2 sellos «ALTO EN» y el B trae 0. Si buscas la opción con menos advertencias, ¿cuál eliges?", "El B", "No tiene ningún sello de advertencia."),
        ex("Un adolescente sale en bicicleta de noche. ¿Qué límite de seguridad conviene? A) Usar casco y luces visibles B) Ir más rápido para llegar antes", "A", "Protege la cabeza y mejora la visibilidad."),
    ],
    Z=[
        ex("¿Por qué un límite de seguridad como el cinturón no es un castigo?", "Porque su finalidad es cuidar a las personas, no controlarlas", "El límite protege la integridad."),
        ex("Un compañero dice: «Si el sello dice ALTO EN, igual lo como todos los días». ¿Qué respondes? A) El sello informa para decidir con qué frecuencia comerlo B) Los sellos no sirven", "A", "La información ayuda a elegir con criterio."),
    ],
    D=[
        arith("Una persona duerme 7 horas de lunes a jueves y 9 horas de viernes a domingo. ¿Cuántas horas duerme en la semana?", "7*4+9*3", "Se suman 4 noches de 7 horas y 3 noches de 9 horas."),
        arith("Un grupo de ejemplo anota 45 minutos diarios de movimiento durante 5 días. ¿Cuántos minutos suma?", "45*5", "Se multiplican los minutos por los días."),
    ],
    context=[ex("En el kiosco del liceo se ofrece una barra con tres sellos «ALTO EN». Una estudiante duda. ¿Qué información le entrega el sello? A) Que tiene mucha cantidad de nutrientes que conviene limitar B) Que está caducada", "A", "Los sellos indican exceso de ciertos nutrientes.")],
    selfcheck=[ex("En Orientación: ¿un sello «ALTO EN» entrega información para decidir?", "Sí", "Es una advertencia."), ex("¿Es un mito que dormir muy poco ayuda a rendir más?", "Sí", "Dormir poco afecta la concentración."), ex("¿Los límites de seguridad cuidan a las personas?", "Sí", "Como el casco o el cinturón.")],
    task=T("Lee estas frases inventadas: (a) «Un sello ALTO EN azúcares advierte de mucho azúcar»; (b) «Si como poco, tengo más energía»; (c) «El casco en bicicleta protege la cabeza»; (d) «Pedir ayuda por estrés es perder el tiempo». Clasifícalas como hecho o mito y escribe una razón breve para cada una.", "(a) Hecho: es la función del sello. (b) Mito: comer poco baja la energía. (c) Hecho: protege en una caída. (d) Mito: el estrés intenso merece apoyo.", ["clasifica las cuatro frases", "da una razón para cada una", "usa información confiable", "no cuenta experiencias personales"], ["tabla escrita", "explicación oral"], ["llamar hecho a un mito", "no dar razón"], "Reconoce las razones claras y pregunta qué fuente usaría para comprobar la frase más dudosa."),
    reinforce="Anota un mito que hayas oído sobre alimentación en general y dónde lo comprobarías.",
    extend="Explica por qué un sello de advertencia no prohíbe un alimento, sino que informa.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. El horario de Renata, una estudiante inventada, y sus opciones están escritos en los ejercicios.",
    "Aprenderé a comparar opciones de uso del tiempo de ocio y de manejo del estrés con criterios de bienestar, tiempo y costo. Sirve para armar un plan semanal realista.",
    ["Sé distinguir hechos y mitos de vida saludable.", "Sé sumar horas y minutos."],
    [
        "Cuando una persona tiene tiempo libre, puede elegir entre varias actividades. Para compararlas sirven tres preguntas: ¿me hace bien al cuerpo o al ánimo?, ¿cabe en mi horario? y ¿puedo pagarla o hacerla sin gastar? Cada sí suma 1 punto. Así se elige con datos y no solo por costumbre.",
        "El uso positivo del ocio incluye actividades que recargan energía y que se comparten con otros: deporte, arte, juego, voluntariado, lectura o salir a caminar. No hay una sola actividad correcta. El uso desgastante es el que se vuelve excesivo, deja sin dormir o reemplaza vínculos y obligaciones, aunque al comienzo sea entretenido.",
        "Para manejar el estrés también hay opciones: pausar y respirar lento, moverse un rato, ordenar las tareas por prioridad, conversar con alguien de confianza o descansar. Una buena rutina combina varias. Y si el estrés no baja, se le cuenta a una persona adulta de confianza, porque pedir ayuda también es una estrategia.",
    ],
    [("ocio positivo", "tiempo libre usado en actividades que recargan energía"), ("prioridad", "lo que se hace primero porque es más importante"), ("estrategia", "forma de actuar para lograr algo"), ("rutina", "conjunto de hábitos que se repiten"), ("excesivo", "que se pasa del límite que cuida")],
    [
        W("Puntuar una actividad", "Renata evalúa un taller de teatro del liceo los jueves: le hace bien, cabe en su horario y es gratis. ¿Cuántos puntos suma si cada sí vale 1?", ["Hay tres respuestas afirmativas.", "Cada una vale 1 punto."], "3 puntos"),
        W("Ordenar por prioridad", "Renata tiene una prueba mañana, una tarea para el viernes y quiere ver una serie. ¿Qué hace primero?", ["La prueba es lo más cercano.", "La serie puede ir después, como descanso."], "Estudiar para la prueba"),
    ],
    [
        M("Pensar que el ocio solo es mirar pantallas.", "Se reduce el tiempo libre a una sola opción.", "Considera actividades de movimiento, creatividad y comunidad."),
        M("Creer que descansar es perder tiempo.", "Se mide el valor solo por la productividad.", "El descanso es parte del cuidado y mejora el rendimiento."),
    ],
    R=[
        ex("Una actividad que sí te hace bien, sí cabe en tu horario y es gratis, ¿cuántos puntos suma? Responde con un número.", "3", "Hay tres respuestas afirmativas."),
        ex("¿Una caminata con un amigo puede ser ocio positivo? A) Sí B) No", "A", "Mueve el cuerpo y comparte con otra persona."),
        ex("En Orientación: ¿ordenar tareas por prioridad ayuda a bajar el estrés?", "Sí", "Reduce la sensación de desorden."),
    ],
    U=[
        ex("¿Cuándo el ocio se vuelve desgastante? A) Cuando es excesivo y reemplaza el sueño o los vínculos B) Cuando es corto", "A", "El exceso desordena otras áreas."),
        ex("Renata respira lento durante un minuto antes de una prueba. ¿Qué estrategia usa? A) Pausa y respiración B) Ordenar tareas", "A", "Es una forma de bajar la tensión."),
        ex("Si el estrés no baja con las estrategias personales, ¿qué conviene? A) Contarle a una persona adulta de confianza B) Esforzarse más en silencio", "A", "Pedir ayuda también es una estrategia."),
    ],
    A=[
        ex("Renata compara dos actividades con tres preguntas (bien, horario, costo). Fútbol: sí, sí, sí. Videojuegos: no, sí, no. ¿Cuál suma más?", "Fútbol", "Fútbol suma 3 y videojuegos suma 1."),
        ex("Renata tiene 3 horas libres el sábado. Dedica 90 minutos a caminar con una amiga y el resto a leer. ¿Cuántos minutos dedica a leer?", "90", "3 horas son 180 minutos y 180 − 90 son 90 minutos."),
        ex("Ordena por prioridad: (a) ver una serie, (b) estudiar para la prueba de mañana, (c) ordenar el closet. ¿Cuál va primero?", "b", "Es lo más cercano y con más consecuencias."),
    ],
    Z=[
        ex("¿Por qué una buena rutina de manejo del estrés combina varias estrategias?", "Porque distintas situaciones requieren distintas respuestas y una sola puede no alcanzar", "Variar aumenta las formas de cuidarse."),
        ex("Un compañero dice: «Si me divierto mucho, no importa cuánto tiempo». ¿Qué respondes? A) El tiempo excesivo puede quitarle espacio al sueño y a los vínculos B) Tienes razón, la diversión no se mide", "A", "El equilibrio también es parte del cuidado."),
    ],
    D=[
        arith("Renata propone 45 minutos de deporte, 30 de lectura y 25 de conversación con su familia el domingo. ¿Cuántos minutos suma su plan?", "45+30+25", "Se suman las tres actividades."),
        arith("Un taller cuesta $3.000 por sesión. Renata asiste a 4 sesiones al mes. ¿Cuánto paga al mes?", "3000*4", "Se multiplica el costo por las sesiones.", " pesos"),
    ],
    context=[ex("En el Consejo de Curso proponen una tarde de actividades sin costo: fútbol, dibujo y juegos de mesa. ¿Qué criterio cumple mejor esta propuesta? A) Que casi todos pueden participar sin gastar B) Que es obligatoria", "A", "Se cumple el criterio de costo y participación.")],
    selfcheck=[ex("En Orientación: ¿el ocio positivo recarga energía?", "Sí", "Es su característica central."), ex("¿Descansar es parte del cuidado?", "Sí", "Mejora el bienestar."), ex("¿Se puede combinar varias estrategias para el estrés?", "Sí", "Una rutina variada ayuda más.")],
    task=T("Arma un plan de ocio de tres actividades para un fin de semana de un personaje inventado, Camilo, con estas opciones: salir a andar en bicicleta con casco (gratis), un taller de dibujo ($2.000 por sesión) y estar seis horas en videojuegos. Evalúa cada opción con tres preguntas (bien, horario, costo), suma los puntos y elige un plan de dos actividades. Agrega una estrategia para el estrés si se siente muy tenso.", "Bicicleta: bien sí, horario sí, costo sí = 3. Dibujo: sí, sí, no = 2. Videojuegos seis horas: no, no, sí = 1. Plan: bicicleta con casco y taller de dibujo. Estrategia: respirar lento y contarle a una persona adulta de confianza.", ["evalúa las tres opciones", "suma bien los puntos", "elige un plan de dos actividades", "incluye una estrategia de estrés"], ["tabla escrita", "plan semanal"], ["sumar mal", "elegir sin criterio"], "Reconoce el uso de criterios y pregunta qué ajustaría si cambia el horario."),
    reinforce="Escribe tres actividades de ocio positivo que no cuesten dinero.",
    extend="Explica cómo cambiaría tu plan si una semana tienes muchas pruebas.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Los casos de seguridad personal están escritos en los ejercicios; los personajes son inventados.",
    "Aprenderé a elegir una acción segura frente a riesgos de todos los días, como el trayecto a casa, la bicicleta, los lugares concurridos y el uso del celular en la calle. Sirve para prevenir accidentes y pedir ayuda a tiempo.",
    ["Sé que los límites de seguridad cuidan.", "Sé el orden: seguridad, alejarse y avisar."],
    [
        "La seguridad personal se cuida con prevención, que es anticiparse a los riesgos. En el trayecto a casa conviene avisar a una persona de tu casa la hora a la que llegarás, ir por lugares iluminados y concurridos cuando sea posible, y estar atento al entorno. En bicicleta o en patineta, se usa casco y se respetan las señales de tránsito.",
        "Mirar el celular mientras se camina o se cruza una calle reduce la atención y aumenta el riesgo de accidente. Cruzar por el paso de peatones y esperar la luz verde es una acción autónoma que cuida. En lugares con mucha gente, como estadios o ferias, se acuerda de antemano un punto de encuentro por si el grupo se separa.",
        "Si alguien te incomoda o te sigue, la acción segura es dirigirse a un lugar con personas, como una tienda o una farmacia, y avisar a una persona adulta de confianza. No se discute ni se enfrenta a esa persona. Y si te sientes en peligro inmediato, se pide ayuda a cualquier persona adulta presente y se avisa después a una persona adulta de confianza.",
    ],
    [("prevención", "anticiparse a un riesgo para evitarlo"), ("entorno", "lo que rodea a una persona en un lugar"), ("punto de encuentro", "lugar acordado para reunirse si el grupo se separa"), ("distracción", "falta de atención por mirar o escuchar otra cosa"), ("paso de peatones", "zona marcada para cruzar la calle")],
    [
        W("Elegir dónde ir", "Una estudiante inventada nota que un desconocido la sigue por una calle poco iluminada. ¿Qué hace?", ["Va a un lugar con personas, como una tienda.", "Después avisa a una persona adulta."], "Entrar a un lugar con personas y avisar a una persona adulta"),
        W("Prevenir una distracción", "Un joven de ejemplo cruza mirando el celular. ¿Qué conviene cambiar?", ["La atención al entorno baja al mirar la pantalla.", "Cruzar exige mirar la calle."], "Guardar el celular y cruzar por el paso de peatones mirando"),
    ],
    [
        M("Cruzar rápido mirando el celular para ahorrar tiempo.", "Se prioriza la rapidez sobre la atención.", "Guarda el celular y cruza por el paso de peatones con la luz verde."),
        M("Discutir con quien te sigue para que se vaya.", "Se cree que enfrentar resuelve el riesgo.", "Dirígete a un lugar con personas y avisa a una persona adulta."),
    ],
    R=[
        ex("Avisar a una persona de tu casa a qué hora llegarás, ¿es prevención? Responde sí o no.", "Sí", "Permite que alguien sepa dónde estás."),
        ex("Si un desconocido te sigue, ¿a dónde conviene ir? A) A un lugar con personas B) A una calle sin gente", "A", "Más personas aumentan la seguridad."),
        ex("En bicicleta, ¿qué elemento reduce el daño de una caída? A) El casco B) La música alta", "A", "Protege la cabeza."),
    ],
    U=[
        ex("¿Por qué no se debe mirar el celular al cruzar? A) Porque baja la atención al entorno B) Porque se gasta batería", "A", "La distracción aumenta el riesgo de accidente."),
        ex("¿Para qué sirve un punto de encuentro en un lugar concurrido? A) Para reunirse si el grupo se separa B) Para esconderse", "A", "Facilita encontrarse sin peligro."),
        ex("¿Qué conviene hacer ante una persona que te incomoda en la calle? A) Dirigirte a un lugar con personas y avisar a un adulto B) Enfrentarla", "A", "Evita aumentar el riesgo."),
    ],
    A=[
        ex("Clasifica con S (segura) o N (no segura): 1) Cruzar con luz verde por el paso peatonal. 2) Cruzar corriendo por entre autos. 3) Avisar a una persona de casa que llegarás a las 18:00. Escribe las letras en orden.", "S, N, S", "La 1 y la 3 previenen riesgos; la 2 expone a un accidente."),
        ex("Un grupo de ejemplo va a un evento con mucha gente. ¿Qué acuerdan antes de entrar? A) Un punto de encuentro B) Que cada uno vaya por su lado", "A", "Si se separan, saben dónde encontrarse."),
        ex("Ana sale a las 18:00 del liceo y tarda 25 minutos en llegar. Avisa que llegará a las 18:25. Si llegara a las 18:50, ¿cuántos minutos más tardó?", "25", "De 18:25 a 18:50 hay 25 minutos de diferencia."),
    ],
    Z=[
        ex("¿Por qué la prevención es mejor que reaccionar cuando ya hay un riesgo?", "Porque evita que el daño ocurra y da tiempo para decidir con calma", "Anticipar protege más que improvisar."),
        ex("Un compañero dice: «Nunca me pasa nada, no necesito casco». ¿Qué respondes? A) Los accidentes ocurren cuando no se esperan B) Tienes razón", "A", "El riesgo existe aunque no se haya vivido."),
    ],
    D=[
        arith("Un grupo de 28 estudiantes practica el punto de encuentro en 4 equipos iguales. ¿Cuántos integrantes tiene cada equipo?", "28//4", "Se divide el total entre los equipos."),
        arith("Una calle de ejemplo mide 600 metros y un estudiante la recorre a 100 metros por minuto. ¿Cuántos minutos tarda?", "600//100", "Se divide la distancia entre la velocidad."),
    ],
    context=[ex("Una vecina de ejemplo cuenta que, al volver de noche, se acerca un auto y siente miedo. ¿Qué acción es más segura? A) Entrar a un local abierto y avisar a una persona adulta B) Seguir caminando sola por la calle oscura", "A", "Busca un lugar con personas y conecta con ayuda.")],
    selfcheck=[ex("En Orientación: ¿prevenir es anticiparse a un riesgo?", "Sí", "Evita que ocurra el daño."), ex("¿Mirar el celular al cruzar es seguro?", "No", "Baja la atención."), ex("¿Conviene ir a un lugar con personas si alguien te sigue?", "Sí", "Aumenta tu seguridad.")],
    task=T("Escribe un plan de seguridad para el trayecto del liceo a casa de un personaje inventado, Matías: sale a las 19:00 de un taller, va en bicicleta por una calle con poca luz y suele ir mirando el celular. Incluye: (1) dos riesgos que detectas, (2) tres acciones de prevención y (3) qué hace si alguien lo sigue y a quién avisa.", "Riesgos: poca luz y distracción con el celular. Acciones: casco y luz en la bicicleta, guardar el celular, avisar a una persona de su casa la hora de llegada. Si lo siguen: ir a un local con personas y avisar a una persona adulta de confianza.", ["detecta dos riesgos", "propone tres acciones", "explica qué hace si lo siguen", "indica a quién avisa"], ["plan escrito", "tabla"], ["proponer enfrentar a quien lo sigue", "ignorar el celular"], "Reconoce el uso de la prevención y pregunta qué cambiaría si fuera de noche."),
    reinforce="Escribe tres acciones de prevención para ir a un evento masivo imaginario.",
    extend="Explica por qué avisar a una persona de tu casa es una acción de autonomía y no de dependencia.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. Los mensajes de ejemplo para pedir apoyo están escritos en los ejercicios.",
    "Aprenderé a comunicar una necesidad de salud o de bienestar a una persona adulta de confianza y a proponer una acción propia. Sirve para pedir apoyo sin sentir vergüenza.",
    ["Sé armar un mensaje de tres partes.", "Sé que las redes de apoyo existen."],
    [
        "Comunicar una necesidad de bienestar es decir con claridad lo que pasa y lo que se necesita. Por ejemplo: «Hace una semana duermo mal y me cuesta concentrarme; quiero ver si puedo cambiar mi horario». Un buen mensaje incluye el hecho, la emoción y la petición, y también una acción propia que la persona ya está dispuesta a hacer.",
        "Hablar de la alimentación, del estrés o del ánimo no es debilidad. Una persona adulta de confianza puede ser alguien de tu casa, un profesor, la persona orientadora o un profesional de un centro de salud. Si la primera persona no puede ayudar, se busca otra. Y si el malestar es fuerte o dura semanas, se pide apoyo profesional.",
        "La autonomía también se muestra al cumplir los compromisos que uno se pone. Si decides dormir 30 minutos antes, anotas la hora, lo pruebas una semana y evalúas. Contar tu plan a otra persona ayuda a sostenerlo. El Fono Niños 147 está disponible para niños, niñas y adolescentes, siempre junto con el aviso a una persona adulta.",
    ],
    [("compromiso", "decisión que una persona se propone cumplir"), ("evaluar", "revisar si un plan está funcionando"), ("apoyo profesional", "ayuda de una persona formada en salud o bienestar"), ("acción propia", "paso concreto que la persona decide hacer"), ("petición", "lo que se pide a la otra persona")],
    [
        W("Completar el mensaje", "Un estudiante inventado escribe: «Duermo poco y estoy agotado». ¿Qué le falta para ser un buen mensaje de apoyo?", ["Tiene el hecho y la emoción.", "No dice qué necesita."], "Una petición y una acción propia"),
        W("Evaluar un plan", "Una joven de ejemplo se acostó 30 minutos antes durante 5 de 7 noches. ¿Cumplió todos los días?", ["Son 5 noches de 7.", "Quedaron 2 sin cumplir."], "No, cumplió 5 de 7"),
    ],
    [
        M("Callarse el malestar para no preocupar a otros.", "Se cree que pedir ayuda molesta.", "Quienes te quieren prefieren saberlo; cuéntalo a una persona adulta de confianza."),
        M("Esperar que otra persona note el problema sin decirlo.", "Se supone que los demás adivinan.", "Di con claridad qué pasa y qué necesitas."),
    ],
    R=[
        ex("Un buen mensaje de apoyo incluye hecho, emoción y petición. ¿Cuál de estas es una petición? A) «Quiero que me ayudes a ordenar mis horarios.» B) «Estoy muy cansado.»", "A", "Dice lo que se necesita de la otra persona."),
        ex("¿Hablar del estrés con una persona adulta de confianza es una debilidad? Responde sí o no.", "No", "Es una forma de cuidarse."),
        ex("¿El Fono Niños 147 reemplaza el aviso a una persona adulta de confianza? Responde sí o no.", "No", "Se usa junto con ese aviso."),
    ],
    U=[
        ex("Si la primera persona adulta no puede ayudar, ¿qué haces? A) Buscas a otra persona adulta de confianza B) Te quedas sin pedir ayuda", "A", "El apoyo se puede buscar en otra persona."),
        ex("¿Por qué conviene anotar y evaluar un compromiso personal? A) Para ver si está funcionando B) Para olvidarlo", "A", "Medir permite ajustarlo."),
        ex("Si un malestar dura semanas y es fuerte, ¿qué corresponde? A) Pedir apoyo profesional con ayuda de una persona adulta B) Esperar a que desaparezca", "A", "Un malestar prolongado necesita atención."),
    ],
    A=[
        ex("Ordena las partes del mensaje con letras hecho (H), emoción (E) y petición (P): (1) «Quiero que me acompañes al centro de salud.» (2) «Me siento preocupado.» (3) «Llevo dos semanas con dolor de cabeza todos los días.» Escribe las letras en orden de 1, 2, 3.", "P, E, H", "La 1 pide algo, la 2 dice cómo se siente y la 3 cuenta lo que pasa."),
        ex("Una estudiante de ejemplo se propone tomar agua en cada recreo. De 10 recreos, lo cumplió 7 veces. ¿Cuántos recreos no lo cumplió?", "3", "A los 10 se les restan los 7 cumplidos."),
        ex("¿Qué frase abre mejor una conversación sobre bienestar? A) «Necesito conversar contigo de algo que me preocupa.» B) «No me hagas preguntas.»", "A", "Invita al diálogo y pide atención."),
    ],
    Z=[
        ex("¿Por qué contar un plan personal a otra persona ayuda a cumplirlo?", "Porque otra persona puede apoyar, recordar y celebrar los avances", "El apoyo social sostiene los hábitos."),
        ex("Un compañero dice: «Si pido ayuda, pierdo mi autonomía». ¿Qué respondes? A) La autonomía incluye saber cuándo pedir ayuda B) Tienes razón", "A", "Decidir pedir apoyo es una decisión propia."),
    ],
    D=[
        arith("Un grupo de ejemplo se propone caminar 15 minutos cada día durante dos semanas. ¿Cuántos minutos caminan en total?", "15*14", "Dos semanas son 14 días."),
        ex("De un mensaje: «Hace dos semanas duermo mal. Estoy preocupado. Quiero que me ayudes a revisar mis horarios». ¿Cuál es la acción propia más adecuada para agregar? A) «Voy a apagar las pantallas 30 minutos antes de dormir.» B) «Voy a ver qué pasa.»", "A", "Es concreta, posible y medible."),
    ],
    context=[ex("En tutoría, una estudiante inventada quiere decirle a su profesor jefe que está agobiada por las pruebas. ¿Qué frase es más clara? A) «Estoy muy agobiada con las pruebas y quiero ver cómo organizarme; ¿me ayudas?» B) «Todo me sale mal.»", "A", "Incluye emoción, hecho y petición.")],
    selfcheck=[ex("En Orientación: ¿un compromiso personal se puede evaluar?", "Sí", "Ayuda a ajustarlo."), ex("¿Pedir ayuda es parte de la autonomía?", "Sí", "Decidir pedir apoyo es una decisión propia."), ex("¿Un malestar fuerte y prolongado necesita apoyo profesional?", "Sí", "Necesita atención de profesionales.")],
    task=T("Escribe un mensaje de apoyo para este caso inventado: Ignacio duerme poco por estudiar de noche, se siente cansado y a veces se salta el desayuno. Incluye hecho, emoción, petición y una acción propia medible para una semana. Elige a quién se lo diría. Luego explica cómo evaluará si funcionó.", "«Necesito conversar contigo. Llevo dos semanas durmiendo muy poco y estoy cansado. Me siento preocupado. Quiero que me ayudes a organizar mis horarios. Me propongo acostarme a las 23:00 de lunes a viernes.» A quién: persona de su casa o profesor jefe. Evaluación: anotar cuántas noches lo cumplió de 5.", ["incluye hecho, emoción y petición", "agrega una acción propia medible", "elige una persona adulta", "explica cómo evaluará"], ["texto escrito", "ensayo oral"], ["no pedir nada concreto", "acción propia vaga"], "Reconoce el mensaje completo y pregunta cómo celebraría un avance."),
    reinforce="Escribe una acción propia medible para una semana de un personaje inventado.",
    extend="Explica cómo contar un plan a otra persona puede ayudarte a cumplirlo.",
)

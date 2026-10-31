"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 18 (derechos, deberes y bien común) y OA 19 (proteger a las personas cuando no se respetan sus derechos)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA18, OA19 = "HI06 OA 18", "HI06 OA 19"

# ================================================================ OA 18 · clase 1
lesson(
    OA18, 1,
    "Aprenderé a ubicar los deberes que acompañan a los derechos en distintos espacios y momentos: la casa, la escuela, el barrio y el país. Sirve para entender que cada derecho que tengo implica algo que debo hacer.",
    ["Sé que todas las personas tienen derechos.", "Sé que los derechos deben ser respetados por los pares, la comunidad y el Estado."],
    [
        "Cada derecho genera deberes y responsabilidades. Un deber es algo que debo hacer porque lo exige una regla, una ley o la convivencia. Una responsabilidad es hacerme cargo de lo que hago y de lo que prometí. Por ejemplo, el derecho a la educación genera el deber de asistir a clases y de respetar a mis compañeros y profesores. El derecho a opinar genera el deber de escuchar las opiniones de los demás.",
        "Los deberes aparecen en distintos espacios. En la escuela, hay que respetar los horarios y cuidar los materiales. En el barrio, hay que mantener limpias las plazas y no hacer ruido en la noche. En el país, hay que cumplir las leyes y respetar los símbolos patrios. También las instituciones tienen deberes: una escuela debe cuidar a sus estudiantes y el Estado debe garantizar la educación.",
        "El tiempo también importa: un deber se cumple en un plazo. Entregar una tarea el viernes, llegar a la hora a clases o devolver un libro de la biblioteca en una semana son responsabilidades con fecha. Cumplirlas permite que todos convivamos bien y busquemos el bien común, que son las condiciones que ayudan a que todos podamos vivir bien.",
    ],
    [("deber", "algo que debo hacer porque lo exige una regla, una ley o la convivencia"), ("responsabilidad", "hacerme cargo de lo que hago y de lo que prometí"), ("convivencia", "vivir juntos respetándose"), ("bien común", "condiciones que ayudan a que todos podamos vivir bien"), ("plazo", "tiempo dentro del cual debe cumplirse algo")],
    [
        ("Emparejar derecho y deber", "El derecho a opinar en el curso. ¿Qué deber lo acompaña: escuchar las opiniones de los demás o gritar más fuerte?", ["Opinar implica que otros también opinan.", "Debo escucharlos.", "El deber es escuchar."], "Escuchar las opiniones de los demás"),
        ("Cumplir un plazo", "Una biblioteca presta un libro por 7 días. Lo retiraste el lunes 3. ¿Qué día debes devolverlo?", ["Sumo 7 días al día 3.", "3 más 7 es 10.", "El día 10, que es lunes."], "El lunes 10"),
    ],
    [
        ("Creer que los derechos no traen deberes.", "Cada derecho exige respetar los derechos de los demás.", "Para cada derecho, pregunta qué debo hacer yo."),
        ("Pensar que solo las personas tienen deberes.", "Las instituciones, como la escuela o el Estado, también tienen deberes.", "Incluye a las instituciones en tu lista."),
    ],
    [
        ("El derecho a la educación, ¿genera el deber de asistir a clases o el de faltar cuando uno quiera?", "El deber de asistir a clases", "Asistir permite ejercer el derecho a aprender."),
        ("Entregar una tarea el viernes, ¿es una responsabilidad con plazo o un derecho?", "Una responsabilidad con plazo", "Es algo que me comprometo a hacer en una fecha."),
        ("Mantener limpia una plaza del barrio, ¿es un deber de convivencia o de transporte?", "De convivencia", "Ayuda a que todos usen bien el espacio."),
    ],
    [
        ("¿Por qué los derechos generan deberes?", "Porque ejercer mi derecho no debe dañar los derechos de los demás", "Los derechos de todos valen igual."),
        ("¿Qué diferencia hay entre deber y responsabilidad?", "El deber lo exige una regla; la responsabilidad es hacerme cargo de lo que hago", "Así se definieron en el vocabulario."),
        ("¿Por qué también las instituciones tienen deberes?", "Porque deben cuidar y garantizar los derechos de las personas", "Una escuela cuida a sus estudiantes; el Estado garantiza la educación."),
    ],
    [
        ("Una escuela de ejemplo tiene 30 estudiantes por curso y 6 cursos. Debe cuidar a todos. ¿Cuántos estudiantes cuida?", "180", "6 por 30 es 180.", "6*30"),
        ("Situación: un compañero usa el celular a todo volumen en la biblioteca. ¿Qué deber incumple: respetar la convivencia o entregar tareas?", "Respetar la convivencia", "Molesta a quienes quieren leer."),
        ("El derecho a un recreo seguro, ¿qué deber tiene la escuela: cuidar el patio o prohibir los recreos?", "Cuidar el patio", "Debe garantizar que el recreo sea seguro."),
    ],
    [
        ("Luis dice: «Tengo derecho a opinar, así que puedo interrumpir a todos». ¿Qué error comete?", "El derecho a opinar exige escuchar a los demás", "Interrumpir daña el derecho de los otros."),
        ("Pía dice: «Los deberes son solo para los niños». ¿Qué error comete?", "También los adultos y las instituciones tienen deberes", "Los deberes son de todos."),
    ],
    [
        ("Ordena de menor a mayor espacio en que se cumple el deber: A) cumplir las leyes del país, B) cuidar los materiales del curso, C) mantener limpia la plaza del barrio.", "B, C, A", "El curso es lo más pequeño, luego el barrio y por último el país."),
        ("Una profesora promete devolver las pruebas corregidas en 5 días. Las entrega 3 días después de ese plazo. ¿Cuántos días pasaron en total desde la prueba?", "8", "5 más 3 es 8.", "5+3"),
    ],
    [("Un curso de ejemplo tiene el derecho a usar la sala de computación y el deber de cuidarla. Un grupo deja las sillas desordenadas y el siguiente curso no puede trabajar. ¿Qué deber no se cumplió?", "Cuidar y ordenar la sala", "El grupo no se hizo cargo de lo que usó.")],
    [("En Historia: ¿qué es un deber?", "Algo que debo hacer porque lo exige una regla, una ley o la convivencia", "Es la definición de la clase."), ("¿Qué es el bien común?", "Condiciones que ayudan a que todos podamos vivir bien", "Es la definición de la clase."), ("¿Solo las personas tienen deberes?", "No, también las instituciones", "La escuela y el Estado también.")],
    (
        "Completa esta tabla con una frase por casilla: derecho / deber que lo acompaña / espacio donde se cumple (casa, escuela, barrio o país). Derechos: a la educación, a opinar, a jugar en una plaza limpia, a un recreo seguro. Luego escribe una responsabilidad que tengas hoy con fecha de cumplimiento.",
        "Educación / asistir a clases / escuela. Opinar / escuchar / curso. Mi responsabilidad: traer el libro de la biblioteca el lunes 10.",
        ["empareja cada derecho con un deber lógico", "ubica el espacio", "incluye una responsabilidad con fecha"],
        ["tabla de cuatro filas y una frase"],
        ["poner un deber que no se relaciona con el derecho", "no incluir plazo"],
        "Muestra tu tabla a una persona de tu casa y pídele que agregue otro deber que ella cumple.",
    ),
    "Escribe un deber que cumples en tu casa y qué derecho de otra persona protege.",
    "Escribe un deber que tenga tu escuela con sus estudiantes.",
)

# ================================================================ OA 18 · clase 2
lesson(
    OA18, 2,
    "Aprenderé a leer un reglamento o una norma y a identificar los derechos y los deberes que aparecen. Sirve para revisar de dónde vienen las reglas de convivencia y quién las hizo.",
    ["Sé que los derechos generan deberes.", "Sé que una fuente tiene una procedencia."],
    [
        "Las reglas de convivencia aparecen en fuentes como el reglamento de una escuela, los estatutos de una junta de vecinos o las leyes. Un reglamento es un texto que dice qué se puede y qué no se puede hacer en un lugar. La procedencia nos dice quién lo escribió, cuándo y para qué. Un buen reglamento se hace con la participación de la comunidad y busca que todos convivan bien.",
        "En un reglamento encontramos tres tipos de frases: derechos, que dicen lo que las personas pueden exigir; deberes, que dicen lo que deben hacer; y sanciones, que dicen qué consecuencia hay si no se cumple. Por ejemplo: «Todos los estudiantes pueden opinar» es un derecho. «Los estudiantes deben respetar los turnos de palabra» es un deber. «Quien dañe un mural debe repararlo» es una consecuencia, también llamada medida formativa.",
        "Al leer, separamos lo que el texto dice de lo que interpretamos. Si el reglamento dice que debemos llegar a las 8:00, no podemos concluir que cada profesor tiene la misma regla en todos los colegios. Para eso habría que leer el reglamento de cada colegio.",
    ],
    [("reglamento", "texto que dice qué se puede y qué no se puede hacer en un lugar"), ("sanción", "consecuencia por no cumplir una regla"), ("medida formativa", "consecuencia que busca que la persona aprenda y repare el daño"), ("estatuto", "reglas con que se organiza un grupo, como una junta de vecinos"), ("procedencia", "quién hizo la fuente, cuándo y para qué")],
    [
        ("Clasificar una frase", "Frase de un reglamento de ejemplo: «Todos los estudiantes deben cuidar los libros de la biblioteca». ¿Es un derecho, un deber o una sanción?", ["Dice lo que deben hacer.", "No dice una consecuencia ni algo que puedan exigir.", "Es un deber."], "Un deber"),
        ("Leer la procedencia", "Un reglamento escolar fue escrito por el consejo de profesores con ayuda de estudiantes y apoderados. ¿Quiénes participaron en su elaboración?", ["Nombra a los grupos.", "Profesores, estudiantes y apoderados.", "Esa es la procedencia."], "Profesores, estudiantes y apoderados"),
    ],
    [
        ("Pensar que un reglamento es igual en todos los colegios.", "Cada comunidad escolar escribe el suyo.", "Revisa la procedencia y el nombre del colegio."),
        ("Creer que toda sanción debe ser un castigo.", "Muchas medidas son formativas: buscan reparar y aprender.", "Pregunta si la medida ayuda a reparar el daño."),
    ],
    [
        ("«Los estudiantes pueden pedir ayuda a un profesor», ¿es un derecho o un deber?", "Un derecho", "Dice lo que pueden hacer."),
        ("«Quien rompa un vidrio deberá ayudar a repararlo», ¿es un derecho o una consecuencia?", "Una consecuencia", "Dice qué ocurre si no se cumple una regla."),
        ("Un reglamento, ¿dice qué se puede y qué no se puede hacer en un lugar o cuenta un cuento?", "Dice qué se puede y qué no se puede hacer", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué un reglamento hecho con participación de la comunidad suele cumplirse mejor?", "Porque las personas sienten que sus ideas fueron consideradas", "Participar da sentido a la regla."),
        ("¿Qué busca una medida formativa?", "Que la persona aprenda y repare el daño", "Así se definió en el vocabulario."),
        ("¿Por qué conviene preguntar quién escribió un reglamento?", "Para saber con qué propósito se hizo y a quién obliga", "La procedencia ayuda a entender la regla."),
    ],
    [
        ("Reglamento de ejemplo: 1) «Todos pueden participar en el consejo de curso». 2) «Cada estudiante debe llegar a las 8:00». 3) «Si alguien rompe un material, la medida es reponerlo». ¿Cuántas frases son deberes?", "1", "Solo la 2 dice lo que se debe hacer; la 1 es un derecho y la 3 una consecuencia.", None),
        ("Con el mismo reglamento: ¿qué frase corresponde a un derecho: la 1, la 2 o la 3?", "La 1", "Dice lo que los estudiantes pueden hacer."),
        ("Con el mismo reglamento: ¿qué frase señala una consecuencia?", "La 3", "Indica qué ocurre si se rompe un material."),
    ],
    [
        ("Teo lee en el reglamento de su colegio que se debe llegar a las 8:00 y dice: «En todos los colegios es igual». ¿Qué error comete?", "Cada colegio tiene su propio reglamento", "Un texto describe solo su comunidad."),
        ("Un reglamento dice «Los estudiantes pueden opinar» pero nunca los escuchan. ¿Qué falta: el texto del derecho o que se cumpla?", "Que se cumpla", "El texto existe, pero no se respeta en la práctica."),
    ],
    [
        ("Ordena los pasos para usar un reglamento: A) decidir qué hacer, B) leer quién lo hizo, C) buscar la frase sobre el problema.", "B, C, A", "Primero la procedencia, luego el contenido y al final la decisión."),
        ("Reglamento de ejemplo: «Quien ensucie el patio debe limpiarlo durante un recreo». Un estudiante lo ensució en 2 recreos distintos y debe limpiar 1 recreo por cada vez. ¿Cuántos recreos limpiará?", "2", "Limpia un recreo por cada una de las 2 veces.", None),
    ],
    [("En una junta de vecinos de ejemplo, el estatuto dice: «Los socios tienen derecho a opinar y el deber de asistir a las reuniones». ¿Cuál es el deber que aparece en el estatuto?", "Asistir a las reuniones", "Es lo que los socios deben hacer.")],
    [("¿Qué es un reglamento?", "Un texto que dice qué se puede y qué no se puede hacer en un lugar", "Es la definición de la clase."), ("¿Qué es una medida formativa?", "Una consecuencia que busca que se aprenda y se repare el daño", "Es la definición de la clase."), ("¿Qué tipos de frases hay en un reglamento?", "Derechos, deberes y sanciones", "Así se enseñó en la clase.")],
    (
        "Lee este reglamento inventado de un curso: «1) Todos pueden opinar en el consejo de curso. 2) Cada estudiante debe cuidar su sala y su mesa. 3) Quien dañe un material debe repararlo con ayuda del grupo. 4) Los estudiantes pueden pedir ayuda a su profesora jefe». Clasifica cada frase en derecho, deber o consecuencia y escribe una pregunta de procedencia.",
        "1 derecho, 2 deber, 3 consecuencia, 4 derecho. Pregunta: ¿quién escribió el reglamento y cuándo?",
        ["clasifica bien las cuatro frases", "justifica una clasificación", "formula una pregunta de procedencia"],
        ["cuatro clasificaciones y una pregunta"],
        ["confundir derecho con deber", "no preguntar por la procedencia"],
        "Pide a una persona de tu casa que clasifique las frases sin mirar tu respuesta y compara.",
    ),
    "Escribe una regla de tu casa y di si es un derecho, un deber o una consecuencia.",
    "Escribe una pregunta que le harías al director sobre cómo se hizo el reglamento de tu colegio.",
)

# ================================================================ OA 18 · clase 3
lesson(
    OA18, 3,
    "Aprenderé a relacionar qué pasa cuando las personas y las instituciones cumplen o no cumplen sus deberes. Sirve para entender por qué cumplirlos mejora la convivencia y el bien común.",
    ["Sé que los derechos generan deberes.", "Sé identificar derechos y deberes en un reglamento."],
    [
        "Cuando las personas cumplen sus deberes, la consecuencia es una buena convivencia y se logra el bien común. Por ejemplo, si todos cuidan los espacios compartidos, todos pueden usarlos. Cuando alguien no cumple, la consecuencia puede afectar a otros: la basura en una plaza impide que otros jueguen, y no devolver un libro deja sin lectura a otro compañero.",
        "Los actores son todos los que participan: estudiantes, profesores, familias, vecinos, la escuela y el Estado. Las instituciones también tienen deberes. Si una municipalidad no recoge la basura, los vecinos se ven perjudicados. Si una escuela no cuida el patio, un niño puede sufrir un accidente. Por eso se pide a todos hacerse responsables de sus actos.",
        "Para reparar un daño hay que reconocerlo, pedir disculpas, reparar lo que se pueda y buscar que no se repita. Esto fortalece la confianza. Una cadena puede ser: no se cumple un deber, se afecta el derecho de otro, hay una consecuencia, se repara el daño y se mejora la convivencia.",
    ],
    [("consecuencia", "lo que ocurre después de un hecho"), ("reparar", "arreglar un daño o compensarlo"), ("confianza", "seguridad de que otros cumplirán lo que prometen"), ("espacio compartido", "lugar que usan muchas personas, como un patio o una plaza"), ("actor", "persona o institución que participa en un hecho")],
    [
        ("Armar la cadena", "Un grupo no limpia la mesa del taller y el siguiente curso no puede trabajar. Nombra el deber, el derecho afectado y la consecuencia.", ["Deber: dejar el espacio ordenado.", "Derecho afectado: usar el taller.", "Consecuencia: el otro curso pierde tiempo."], "Deber: ordenar; derecho afectado: usar el taller; consecuencia: se pierde tiempo"),
        ("Reparar el daño", "Un estudiante rompió sin querer el cuaderno de otro. Nombra una acción para reparar.", ["Reconoce lo que ocurrió.", "Pide disculpas.", "Ofrece reponerlo o ayudar."], "Pedir disculpas y reponerlo o ayudar"),
    ],
    [
        ("Creer que no cumplir un deber no afecta a nadie.", "Casi siempre afecta el derecho de otra persona.", "Pregunta a quién afecta."),
        ("Pensar que reparar es solo pedir disculpas.", "También hay que arreglar lo dañado y evitar que se repita.", "Incluye reparación y compromiso."),
    ],
    [
        ("La basura en una plaza, ¿afecta el derecho de otros a jugar o no afecta a nadie?", "Afecta el derecho de otros a jugar", "Otros no pueden usar el espacio limpio."),
        ("Un compañero no devuelve un libro a la biblioteca. ¿Qué afecta: el derecho de otros a leerlo o el clima?", "El derecho de otros a leerlo", "El libro no está disponible."),
        ("Si la municipalidad no recoge la basura, ¿qué actor no cumple su deber: la municipalidad o un vecino?", "La municipalidad", "Es la encargada de recogerla."),
    ],
    [
        ("¿Por qué cumplir los deberes ayuda al bien común?", "Porque permite que todos usen los espacios y ejerzan sus derechos", "Cada deber cumplido protege a los demás."),
        ("¿Por qué una escuela que no cuida el patio incumple un deber?", "Porque debe proteger la seguridad de sus estudiantes", "Un accidente puede afectar su derecho a un recreo seguro."),
        ("¿Por qué reparar un daño fortalece la confianza?", "Porque muestra que la persona se hace responsable", "Los demás ven que puede cumplir."),
    ],
    [
        ("Ordena la reparación: A) pedir disculpas, B) reconocer lo que ocurrió, C) arreglar el daño.", "B, A, C", "Primero reconocer, luego disculparse y después reparar."),
        arith("Una escuela de ejemplo tiene 4 patios y debe revisar cada uno 3 veces por semana para cuidar la seguridad. ¿Cuántas revisiones hace por semana?", "4*3", "Se multiplica el número de patios por las revisiones de cada uno.", " revisiones"),
        ("Un vecino no recoge las heces de su perro en la plaza. ¿Qué derecho de otros afecta: jugar en un lugar limpio o votar?", "Jugar en un lugar limpio", "El espacio queda sucio."),
    ],
    [
        ("Rosa dice: «Si nadie me ve, no pasa nada si no cumplo». ¿Qué error comete?", "Igual afecta a otros y a la confianza", "Los efectos existen aunque no los vea nadie."),
        ("Un grupo cumple todos sus deberes del trabajo, pero un integrante no. ¿Quién es perjudicado: todo el grupo o solo quien no cumplió?", "Todo el grupo", "El trabajo final depende de todos."),
    ],
    [
        ("Ordena la cadena: A) la convivencia mejora, B) el grupo conversa y repara, C) alguien incumple un deber y daña a otro.", "C, B, A", "Primero el hecho, luego la reparación y después la mejora."),
        ("Una escuela de ejemplo cuidó su patio, evitó accidentes y los niños jugaron seguros. ¿Qué deber de la institución se cumplió: cuidar la seguridad de los estudiantes o aumentar las tareas?", "Cuidar la seguridad de los estudiantes", "Eso permitió el recreo seguro."),
    ],
    [("En un barrio de ejemplo los vecinos acuerdan limpiar la plaza cada sábado en turnos. Una vecina no va un sábado y avisa antes. ¿Qué deber cumplió al avisar: la responsabilidad de comunicar o la de limpiar?", "La responsabilidad de comunicar", "Informó que no podía asistir y así el grupo se reorganizó.")],
    [("¿Qué consecuencia tiene cumplir los deberes?", "Se logra una buena convivencia y bien común", "Todos pueden ejercer sus derechos."), ("¿Qué significa reparar?", "Arreglar un daño o compensarlo", "Es la definición de la clase."), ("¿Las instituciones tienen deberes?", "Sí", "Deben cuidar los derechos de las personas.")],
    (
        "Elige uno de estos casos y escribe la cadena: deber incumplido, derecho afectado, actores, consecuencia y una forma de reparar. Caso a) un grupo deja encendidas las luces del taller; caso b) un compañero no entrega su parte del trabajo grupal; caso c) un vecino bota basura en la plaza.",
        "Caso b: deber: entregar su parte; derecho afectado: el grupo a presentar bien; actores: compañeros y profesora; consecuencia: nota más baja; reparación: entregar y pedir disculpas.",
        ["nombra el deber y el derecho afectado", "incluye al menos dos actores", "propone una forma de reparar"],
        ["cinco frases escritas"],
        ["no ver a quién se afecta", "proponer solo un castigo"],
        "Lee tu cadena a una persona de tu casa y pídele que diga si la reparación es justa.",
    ),
    "Escribe una acción que harías si dañaras algo de un compañero.",
    "Escribe un deber de tu escuela hacia ti y cómo lo reconoces.",
)

# ================================================================ OA 18 · clase 4
lesson(
    OA18, 4,
    "Aprenderé a comparar situaciones en que se cumplen o no se cumplen los deberes y a reconocer perspectivas distintas. Sirve para decidir qué hacer pensando en el bien común y no solo en lo que yo quiero.",
    ["Sé que cumplir deberes mejora la convivencia.", "Sé que comparar exige criterios iguales."],
    [
        "Comparar dos situaciones es ver en qué se parecen y en qué se diferencian. Usamos criterios iguales: qué derecho está en juego, qué deber corresponde, quién lo cumple y qué consecuencia tiene. Así evitamos juzgar a la ligera.",
        "Veamos dos cursos de ejemplo. En el curso 6.º A, todos guardan sus cosas y dejan la sala ordenada; el curso siguiente trabaja sin perder tiempo. En el curso 6.º B, nadie ordena y el curso siguiente pierde 10 minutos limpiando antes de empezar. El derecho en juego es el mismo: usar la sala. En A se cumple el deber y en B no.",
        "Cada persona mira desde su situación, y eso se llama perspectiva. Una profesora quiere clases sin interrupciones. Un estudiante cansado quiere irse rápido. Un vecino quiere dormir sin ruido y un joven quiere escuchar música. Cuando las perspectivas chocan, buscamos una solución pensando en el bien común: que todos puedan ejercer sus derechos con las menores molestias posibles.",
    ],
    [("criterio", "regla igual para comparar dos cosas"), ("perspectiva", "mirada de una persona según su situación"), ("bien común", "condiciones que ayudan a que todos podamos vivir bien"), ("acuerdo", "solución que aceptan las personas que conversaron"), ("semejanza", "algo en que dos situaciones se parecen")],
    [
        ("Comparar con criterios", "En 6.º A dejan la sala ordenada; en 6.º B no. Compara el criterio «cumplen su deber de orden».", ["A lo cumple.", "B no lo cumple.", "La diferencia es el cumplimiento."], "6.º A cumple el deber y 6.º B no"),
        ("Dos perspectivas", "Un vecino quiere dormir tranquilo y un joven quiere ensayar música. ¿Son perspectivas iguales o distintas?", ["Cada uno quiere algo distinto.", "Sus necesidades chocan.", "Son distintas."], "Distintas"),
    ],
    [
        ("Elegir siempre lo que quiero yo.", "Los derechos de los demás también valen.", "Busca una solución pensando en todos."),
        ("Creer que una perspectiva es la única válida.", "Cada persona mira según su situación.", "Escucha al menos dos miradas."),
    ],
    [
        ("En el curso 6.º B, ¿se cumple o no se cumple el deber de ordenar?", "No se cumple", "Allí nadie ordena la sala."),
        ("¿Quién pierde tiempo en la situación de 6.º B: el curso siguiente o el director?", "El curso siguiente", "Debe limpiar antes de empezar."),
        ("Un criterio de comparación, ¿es una regla igual para ambos casos o una opinión?", "Una regla igual para ambos casos", "Así se compara con justicia."),
    ],
    [
        ("¿Por qué el vecino y el joven tienen perspectivas distintas?", "Porque sus necesidades en ese momento son diferentes", "Uno quiere descansar y el otro ensayar."),
        ("¿Por qué es útil buscar un acuerdo?", "Porque permite respetar los derechos de todos con pocas molestias", "Es una solución común."),
        ("¿Por qué comparar con criterios iguales ayuda a no juzgar a la ligera?", "Porque se mide lo mismo en cada caso", "Así se evitan prejuicios."),
    ],
    [
        arith("En 6.º B el curso siguiente pierde 10 minutos cada día. ¿Cuántos minutos pierde en 5 días de la semana?", "10*5", "Se multiplica el tiempo diario por los días.", " minutos"),
        ("Tabla de ejemplo: 6.º A deja la sala ordenada los 5 días; 6.º B la deja ordenada 1 día. ¿Cuántos días más cumplió A?", "4", "5 menos 1 es 4.", "5-1"),
        ("Acuerdo posible: el joven ensaya solo entre las 17:00 y las 19:00, y el vecino duerme desde las 22:00. ¿Se respeta el horario de sueño del vecino: sí o no?", "Sí", "El ensayo termina tres horas antes de que duerma."),
    ],
    [
        ("Marta dice: «6.º B es peor porque son más desordenados». ¿Qué error comete al comparar?", "Juzga sin criterios; hay que mirar el deber, el derecho y la consecuencia", "Comparar no es poner etiquetas."),
        ("Un estudiante dice que no limpia porque ya está cansado, y la profesora dice que la sala debe quedar limpia. ¿Qué perspectiva está pensando en el bien común?", "La de la profesora", "Busca que el curso siguiente pueda usar la sala."),
    ],
    [
        ("Ordena de mayor a menor cumplimiento del deber: A) ordenan 5 días de 5, B) ordenan 1 día de 5, C) ordenan 3 días de 5.", "A, C, B", "5 es mayor que 3 y este que 1."),
        arith("Dos cursos comparten una cancha durante un recreo de 60 minutos y acuerdan turnos iguales. ¿Cuántos minutos usa cada curso?", "60//2", "Se reparten los 60 minutos entre 2 cursos.", " minutos"),
    ],
    [("Dos cursos deben usar el mismo patio los viernes. Uno propone que el primero juegue 40 minutos y el otro 10. ¿Qué criterio permite saber si la solución es justa: que ambos tengan el mismo tiempo o que uno tenga más tiempo?", "Que ambos tengan el mismo tiempo", "Es lo equitativo para dos cursos con el mismo derecho.")],
    [("¿Para qué sirve un acuerdo?", "Para respetar los derechos de todos con pocas molestias", "Es una solución común."), ("¿Qué es una perspectiva?", "La mirada de una persona según su situación", "Es la definición de la clase."), ("¿Qué criterio compara cumplimiento de deberes?", "Si cada grupo cumple el deber que le corresponde", "Así se enseñó en la clase.")],
    (
        "Completa una tabla para comparar estas dos situaciones inventadas con los criterios derecho en juego, deber que corresponde, quién lo cumple y consecuencia. Situación 1: en un edificio, todos recogen su basura y el pasillo queda limpio. Situación 2: en otro edificio, algunos dejan basura y los vecinos no pueden usar el pasillo. Luego escribe la perspectiva de una vecina y la de un niño y un acuerdo posible.",
        "Derecho: usar el pasillo. Deber: mantenerlo limpio. Situación 1 lo cumple; la 2 no. Acuerdo: horarios de limpieza.",
        ["usa los cuatro criterios en ambas", "escribe dos perspectivas", "propone un acuerdo que respete a todos"],
        ["tabla de cuatro filas, dos frases y un acuerdo"],
        ["comparar con criterios distintos", "proponer algo que daña a alguien"],
        "Lee tu acuerdo a una persona de tu casa y pídele que diga si respeta a todos.",
    ),
    "Escribe un problema de convivencia que conozcas y dos perspectivas sobre él.",
    "Escribe una pregunta para entender la perspectiva de alguien que piensa distinto.",
)

# ================================================================ OA 19 · clase 1
lesson(
    OA19, 1,
    "Aprenderé a ubicar a qué personas o instituciones se puede acudir, según el lugar y el momento, cuando no se respetan los derechos. Sirve para saber dónde pedir ayuda: en la escuela, en la comuna, en la región y en el país.",
    ["Sé que los derechos generan deberes.", "Sé qué hacen los tres poderes del Estado."],
    [
        "Cuando no se respetan los derechos de una persona, la sociedad tiene formas de protegerla. Algunas son personales: contarlo a una persona adulta de confianza, como un familiar o un profesor. Otras son institucionales: acudir a quien tiene la responsabilidad de ayudar. Cada una actúa en un lugar distinto.",
        "En la escuela, se puede acudir al profesor jefe, a la inspectoría o al encargado de convivencia escolar. En la comuna, existen la municipalidad y la comisaría de Carabineros más cercana. En el país hay tribunales, Carabineros, la Policía de Investigaciones, la Defensoría de los Derechos de la Niñez y el Instituto Nacional de Derechos Humanos. Para los problemas de consumo, como un cobro injusto, está el Servicio Nacional del Consumidor (Sernac). Si una escuela no cumple sus obligaciones, se puede reclamar a la Superintendencia de Educación.",
        "También importa el momento. Primero, contarlo a una persona adulta de confianza. Luego, conversar o denunciar ante quien corresponda. Si no hay solución, se puede acudir a un tribunal. Y si hay peligro inmediato, se pide ayuda de inmediato a Carabineros u otra persona adulta cercana. La protección se organiza en tres niveles: escuela, comuna y país.",
    ],
    [("denunciar", "avisar a una autoridad que no se respetó un derecho"), ("tribunal", "institución que resuelve conflictos aplicando la ley"), ("convivencia escolar", "forma de relacionarse y tratarse en la escuela"), ("persona adulta de confianza", "adulto que cuida de ti y a quien le puedes contar un problema"), ("nivel", "ámbito donde actúa una institución: escuela, comuna o país")],
    [
        ("Ubicar la institución", "Un compañero te trata mal una y otra vez en el patio. ¿A quién acudes primero en la escuela: al encargado de convivencia o a un tribunal?", ["El problema ocurre en la escuela.", "La escuela tiene a una persona encargada.", "Acudo al encargado de convivencia."], "Al encargado de convivencia escolar"),
        ("Ubicar el nivel", "Un negocio te cobró de más por un producto. ¿Qué institución nacional protege a los consumidores?", ["Es un problema de consumo.", "Esa función la cumple el Sernac.", "El Sernac."], "El Sernac"),
    ],
    [
        ("Creer que hay que guardar silencio cuando algo no es justo.", "Contarlo a una persona adulta de confianza es el primer paso.", "Busca a alguien que pueda ayudar."),
        ("Pensar que cualquier institución resuelve cualquier problema.", "Cada una tiene funciones propias.", "Pregunta cuál corresponde al problema."),
    ],
    [
        ("¿Quién resuelve conflictos aplicando la ley: un tribunal o un diario?", "Un tribunal", "Es el Poder Judicial."),
        ("¿Qué institución protege a los consumidores: el Sernac o un tribunal de familia?", "El Sernac", "Su función es el consumo."),
        ("Si hay peligro inmediato, ¿se pide ayuda de inmediato o se espera una semana?", "De inmediato", "El peligro no puede esperar."),
    ],
    [
        ("¿Por qué el primer paso suele ser contárselo a una persona adulta de confianza?", "Porque puede ayudar a decidir y a buscar la institución correcta", "Una persona de confianza orienta."),
        ("¿Por qué existen instituciones en la escuela, la comuna y el país?", "Porque los problemas ocurren en distintos lugares y tienen distinto tamaño", "Cada nivel atiende lo que le corresponde."),
        ("¿Por qué no basta una sola institución para todos los problemas?", "Porque cada una tiene funciones propias", "Un problema de consumo no es de convivencia escolar."),
    ],
    [
        ("Situación: te burlan por tu acento en tu curso. ¿Qué persona de la escuela puede ayudarte: el profesor jefe o la municipalidad?", "El profesor jefe", "Es quien acompaña a tu curso."),
        ("Situación: una escuela no entrega los servicios que declara y varios apoderados reclaman. ¿A qué institución nacional pueden dirigirse: la Superintendencia de Educación o el Sernac?", "La Superintendencia de Educación", "Fiscaliza a las escuelas."),
        ("Situación: hay peligro inmediato en la calle. ¿A qué institución se llama: Carabineros o el Servel?", "Carabineros", "Es la institución policial que responde a emergencias."),
    ],
    [
        ("Luis dice: «Si me pasa algo injusto, lo mejor es no contárselo a nadie». ¿Qué error comete?", "Contárselo a una persona adulta de confianza ayuda a protegerse", "Callar deja el problema sin solución."),
        ("Una vecina dice que el Sernac debe resolver el ruido de la noche en su calle. ¿Qué error comete?", "El Sernac atiende problemas de consumo", "El ruido es un asunto de convivencia en la comuna."),
    ],
    [
        ("Ordena de menor a mayor alcance: A) tribunales del país, B) profesor jefe, C) municipalidad.", "B, C, A", "El curso es lo más pequeño, la comuna sigue y el país es lo más amplio."),
        ("Ordena los pasos: A) acudir a un tribunal si no hay solución, B) contarlo a un adulto de confianza, C) hablar o denunciar ante quien corresponde.", "B, C, A", "Primero el apoyo personal, luego la institución y por último el tribunal."),
    ],
    [("Dos hermanos ven que un adulto cobró de más a su vecina en una tienda. ¿Qué pueden hacer primero: avisar a una persona adulta de confianza o ignorar el problema?", "Avisar a una persona adulta de confianza", "Es el primer paso para orientarse.")],
    [("¿Qué hace un tribunal?", "Resuelve conflictos aplicando la ley", "Es la definición de la clase."), ("¿A quién se acude primero en un problema personal?", "A una persona adulta de confianza", "Es el primer paso."), ("¿Qué institución protege a los consumidores?", "El Sernac", "Esa es su función.")],
    (
        "Elige uno de estos casos y escribe a qué nivel (escuela, comuna o país) corresponde y a quién acudirías primero, después y por último. Caso a) en tu curso hay burlas constantes; caso b) en una tienda te cobraron de más; caso c) tu escuela no cumple una obligación y varias familias reclaman.",
        "Caso a: nivel escuela; primero profesor jefe, después encargado de convivencia, por último la Superintendencia de Educación si no se resuelve.",
        ["identifica el nivel", "ordena a quién acudir", "usa instituciones adecuadas al problema"],
        ["tres pasos escritos"],
        ["elegir una institución que no corresponde", "omitir a una persona de confianza"],
        "Muestra tus pasos a una persona de tu casa y pídele que diga si agregaría alguno.",
    ),
    "Escribe el nombre de una persona adulta de tu confianza en tu escuela.",
    "Escribe una pregunta que le harías a un encargado de convivencia escolar.",
)

# ================================================================ OA 19 · clase 2
lesson(
    OA19, 2,
    "Aprenderé a leer fuentes sobre cómo se protegen los derechos, como leyes, folletos de instituciones y noticias, y a preguntar quién las hizo. Sirve para saber qué ayuda existe y cuál es confiable.",
    ["Sé a qué instituciones se puede acudir.", "Sé que una fuente tiene una procedencia."],
    [
        "Las fuentes sobre protección de derechos son la ley, los sitios y folletos de las instituciones, las noticias y los testimonios. Una ley dice qué se debe hacer y qué sanción hay si no se cumple. Un folleto de una institución explica cómo pedir ayuda. Una noticia cuenta un caso concreto. Un testimonio cuenta lo que vivió una persona.",
        "Para evaluar una fuente preguntamos su procedencia: quién la hizo, cuándo y para qué. Un folleto de una institución del Estado busca informar. Un aviso de una empresa que ofrece ayuda busca atraer clientes. Una noticia puede mostrar un solo caso. Un testimonio no representa a todos.",
        "También hay que separar lo que la fuente dice de lo que interpretamos. Si un folleto dice que una institución atiende reclamos, no podemos concluir que resuelva todos los casos. Una buena práctica es comparar al menos dos fuentes y buscar la información en las instituciones oficiales.",
    ],
    [("ley", "regla que debe cumplir toda la sociedad"), ("folleto informativo", "hoja que explica cómo hacer algo"), ("testimonio", "relato de una persona sobre lo que vivió"), ("reclamo", "aviso de que algo no se hizo bien"), ("fuente oficial", "fuente hecha por una institución del Estado")],
    [
        ("Evaluar la procedencia", "Folleto de ejemplo: «El Sernac atiende reclamos de consumidores. Puedes escribir indicando qué compraste y qué ocurrió». ¿Quién lo hizo y para qué?", ["Lo hace una institución del Estado.", "Su propósito es informar.", "Es una fuente oficial."], "Una institución del Estado, para informar"),
        ("Separar lo que dice", "El folleto anterior dice que el Sernac atiende reclamos. ¿Dice que los resuelve todos?", ["Dice que los atiende.", "No dice que los resuelva todos.", "No se puede concluir eso."], "No"),
    ],
    [
        ("Creer que un aviso de una empresa es igual de confiable que uno oficial.", "La empresa puede buscar clientes, no solo informar.", "Revisa quién lo hizo."),
        ("Concluir con un solo testimonio lo que ocurre siempre.", "Un testimonio muestra una experiencia.", "Busca otras fuentes."),
    ],
    [
        ("Un folleto de una institución del Estado, ¿busca informar o vender?", "Informar", "Su función es explicar cómo pedir ayuda."),
        ("Un testimonio, ¿cuenta lo que vivió una persona o los datos de todo el país?", "Lo que vivió una persona", "Es una experiencia concreta."),
        ("¿Una ley dice qué se debe hacer o cuenta un cuento?", "Qué se debe hacer", "Es una regla para toda la sociedad."),
    ],
    [
        ("¿Por qué conviene comparar al menos dos fuentes?", "Porque cada una muestra una parte y así se comprueba la información", "Una sola puede dejar cosas fuera."),
        ("¿Por qué un aviso de una empresa que ofrece ayuda es menos neutral?", "Porque quiere atraer clientes", "Su propósito es comercial."),
        ("¿Por qué una noticia sobre un caso no basta para hablar de todos?", "Porque muestra solo un caso", "No representa a todas las situaciones."),
    ],
    [
        ("Fuente A: folleto de una institución estatal. Fuente B: aviso de una empresa privada que cobra por tramitar reclamos. ¿Cuál se hizo con fines de cobro?", "La B", "Una empresa que cobra busca clientes."),
        ("Noticia de ejemplo: «En una escuela, 3 de 10 estudiantes dijeron que habían sufrido burlas». ¿Cuántos estudiantes no dijeron haberlas sufrido?", "7", "10 menos 3 es 7.", "10-3"),
        ("Folleto de ejemplo: «Si no puedes resolver el problema en la escuela, puedes reclamar en la Superintendencia de Educación». ¿Qué paso sugiere antes de reclamar allí?", "Intentar resolverlo en la escuela", "El folleto dice «si no puedes resolver en la escuela»."),
    ],
    [
        ("Ema lee el testimonio de una persona a la que la ayudaron rápido y concluye: «Siempre ayudan rápido». ¿Qué error comete?", "Un testimonio no demuestra que siempre ocurra", "Es un solo caso."),
        ("Un aviso dice «Garantizamos que tus derechos serán respetados». ¿Qué pregunta de procedencia debe hacer?", "Quién lo hizo y con qué datos lo respalda", "Sin respaldo, es solo una promesa."),
    ],
    [
        ("Ordena los pasos para usar una fuente: A) usarla para decidir, B) revisar su procedencia, C) comparar con otra fuente.", "B, C, A", "Primero la procedencia, luego la comparación y al final la decisión."),
        ("Dos fuentes sobre un mismo reclamo: un folleto oficial dice «El reclamo demora 15 días» y un testimonio dice «A mí me tomó 30 días». ¿Cuántos días de diferencia hay?", "15", "30 menos 15 es 15.", "30-15"),
    ],
    [("Un niño ve un aviso en internet que dice «Te cobro menos por tramitar tu reclamo». Su abuela le dice que primero busque la información en una institución oficial. ¿Por qué es buen consejo?", "Porque la información oficial no busca cobrar", "La institución del Estado tiene el deber de informar.")],
    [("¿Qué es un testimonio?", "Un relato de una persona sobre lo que vivió", "Es la definición de la clase."), ("¿Qué es una fuente oficial?", "Una fuente hecha por una institución del Estado", "Es la definición de la clase."), ("¿Por qué comparar dos fuentes?", "Para comprobar la información", "Cada una muestra una parte.")],
    (
        "Lee estas dos fuentes inventadas. Fuente 1 (folleto de una institución del Estado): «Si crees que un derecho no se respetó, cuéntalo a una persona adulta de confianza y consulta la institución que corresponde». Fuente 2 (aviso de una empresa): «Resolvemos todo, ¡llámanos!». Escribe qué fuente es más confiable y por qué, qué dice cada una y una pregunta de procedencia para la fuente 2.",
        "La fuente 1 es más confiable porque la hace una institución del Estado para informar. La fuente 2 promete resolver todo sin pruebas. Pregunta: ¿cuánto cobran?",
        ["compara las dos fuentes", "justifica cuál es más confiable", "formula una pregunta de procedencia"],
        ["cuatro frases escritas"],
        ["creer la promesa sin pruebas", "no mirar quién hizo la fuente"],
        "Lee tus frases a una persona de tu casa y pídele que diga si coincide en cuál fuente es más confiable.",
    ),
    "Pide a una persona adulta de confianza que te cuente a quién acudiría ella si no respetaran un derecho suyo.",
    "Escribe una pregunta que te permita comprobar si una institución realmente ayuda.",
)

# ================================================================ OA 19 · clase 3
lesson(
    OA19, 3,
    "Aprenderé a relacionar las causas por las que no se respetan los derechos con las acciones de protección y sus consecuencias. Sirve para proponer soluciones que ataquen el problema de fondo.",
    ["Sé a qué instituciones acudir.", "Sé evaluar fuentes sobre protección de derechos."],
    [
        "Un derecho puede no respetarse por varias causas: falta de conocimiento, prejuicios, abuso de poder, falta de normas o falta de recursos. Para proteger a las personas, la sociedad usa distintas formas. Algunas previenen, como enseñar los derechos en la escuela o hacer campañas. Otras sancionan, como las leyes y los tribunales. Otras reparan, como ayudar a la persona afectada. Y otras acompañan, como los profesionales y las organizaciones.",
        "Los actores que protegen son muchos: las familias, las escuelas, el Estado y las organizaciones de la comunidad, como las juntas de vecinos o las fundaciones. También los medios de comunicación, que pueden informar. Cada actor aporta algo distinto. Una propuesta eficaz combina varias formas y tiene un plazo.",
        "La acción de protección tiene consecuencias: la persona afectada se siente apoyada, la comunidad aprende y se evita que el problema se repita. Pero si la solución llega tarde o solo castiga, el daño puede quedar sin reparar. Por eso conviene pensar en la prevención, la sanción y la reparación al mismo tiempo.",
    ],
    [("prevención", "acciones para evitar que ocurra un problema"), ("sanción", "consecuencia por no cumplir una regla o ley"), ("reparación", "acciones para compensar el daño sufrido"), ("organización de la comunidad", "grupo de personas que se une para ayudar a su barrio o escuela"), ("campaña", "conjunto de acciones para informar o convencer")],
    [
        ("Clasificar una acción", "Una escuela hace una campaña para enseñar los derechos a los estudiantes. ¿Es una acción de prevención, de sanción o de reparación?", ["Enseña antes de que ocurra un problema.", "No castiga ni compensa.", "Es prevención."], "Prevención"),
        ("Causa y consecuencia", "Un grupo se burla de un compañero porque no conoce su cultura. Nombra la causa.", ["Se burlan por una idea que no conocen bien.", "Eso es un prejuicio por falta de conocimiento.", "La causa es el desconocimiento."], "El desconocimiento o prejuicio"),
    ],
    [
        ("Creer que castigar es la única forma de proteger.", "También se puede prevenir, reparar y acompañar.", "Combina varias formas."),
        ("Pensar que un solo actor puede proteger a todos.", "Se necesitan familias, escuelas, el Estado y la comunidad.", "Nombra varios actores."),
    ],
    [
        ("Una campaña para informar los derechos antes de un problema, ¿es prevención o sanción?", "Prevención", "Actúa antes de que ocurra."),
        ("Una multa a una empresa que no cumple la ley, ¿es sanción o reparación?", "Sanción", "Es una consecuencia por incumplir."),
        ("Ayudar a una persona a recuperar lo que perdió, ¿es reparación o prevención?", "Reparación", "Busca compensar el daño."),
    ],
    [
        ("¿Por qué conviene combinar prevención, sanción y reparación?", "Porque cada una cumple un papel distinto", "Previene, castiga la falta y compensa el daño."),
        ("¿Por qué las organizaciones de la comunidad son actores importantes?", "Porque conocen el barrio y ayudan de forma cercana", "Pueden actuar rápido en su entorno."),
        ("¿Qué pasa si una solución llega muy tarde?", "El daño puede quedar sin reparar", "El retraso complica la reparación."),
    ],
    [
        ("Problema: en una escuela hay burlas por la apariencia. Una acción preventiva es hacer talleres de respeto. ¿Qué causa busca atacar: el prejuicio o el clima?", "El prejuicio", "El taller enseña a respetar las diferencias."),
        ("Una junta de vecinos recibe una queja de una familia que no tiene agua. ¿Qué acción de acompañamiento puede hacer: escribir a la municipalidad o ignorar el caso?", "Escribir a la municipalidad", "Acompaña a la familia y busca una solución."),
        ("En una campaña se reparten 120 folletos entre 4 cursos por igual. ¿Cuántos folletos recibe cada curso?", "30", "120 dividido en 4 es 30.", "120//4"),
    ],
    [
        ("Teo dice: «Con una multa se arregla todo». ¿Qué error comete?", "La multa sanciona, pero no repara ni previene por sí sola", "Faltan reparación y prevención."),
        ("Una escuela hace talleres cuando ya hubo un problema grave, pero antes no hacía nada. ¿Qué forma de protección faltó?", "La prevención", "Debieron actuar antes del problema."),
    ],
    [
        ("Ordena la cadena de protección: A) la comunidad aprende y el problema se evita, B) se denuncia el hecho, C) la institución actúa y repara.", "B, C, A", "Primero la denuncia, luego la acción y después el aprendizaje."),
        ("Una escuela quiere evitar las burlas que nacen del prejuicio. Propone: A) talleres de respeto en todos los cursos, B) un reglamento con sanciones, pero sin talleres. ¿Cuál ataca mejor la causa del problema?", "A", "Los talleres enseñan a respetar las diferencias; las sanciones solas no cambian la idea equivocada."),
    ],
    [("Un barrio sufre robos por falta de iluminación. Los vecinos piden más luces a la municipalidad. ¿Qué causa buscan atacar: la falta de iluminación o los vecinos?", "La falta de iluminación", "Es lo que facilita los robos.")],
    [("¿Qué es una acción de prevención?", "Una acción para evitar que ocurra un problema", "Es la definición de la clase."), ("¿Qué es una reparación?", "Acciones para compensar el daño sufrido", "Es la definición de la clase."), ("¿Se necesita un solo actor para proteger los derechos?", "No", "Se necesitan varios.")],
    (
        "Elige uno de estos casos y escribe la causa, tres actores, una acción de prevención, una de sanción y una de reparación. Caso a) burlas por el origen de un compañero; caso b) un barrio sin iluminación; caso c) una tienda que cobra de más a clientes.",
        "Caso b: causa: falta de luz; actores: vecinos, municipalidad, junta de vecinos; prevención: instalar luces nuevas; sanción: reclamar a quien no repara las luminarias; reparación: apoyar a quienes sufrieron robos.",
        ["identifica la causa", "nombra tres actores", "incluye prevención, sanción y reparación"],
        ["seis frases escritas"],
        ["olvidar la causa", "proponer solo castigos"],
        "Lee tus propuestas a una persona de tu casa y pídele que elija la más fácil de aplicar.",
    ),
    "Escribe una acción de prevención que pueda hacer tu curso esta semana.",
    "Escribe una pregunta para saber si una solución realmente repara el daño.",
)

# ================================================================ OA 19 · clase 4
lesson(
    OA19, 4,
    "Aprenderé a comparar dos propuestas para proteger derechos y a fundamentar cuál es mejor con criterios y evidencia. Sirve para proponer y defender una solución justa y realista.",
    ["Sé distinguir prevención, sanción, reparación y acompañamiento.", "Sé que un argumento tiene afirmación, evidencia y razón."],
    [
        "Para comparar dos propuestas usamos criterios iguales: a quién protege, qué causa ataca, quién la aplica, cuánto cuesta y cuánto tarda. Una propuesta es mejor si cumple los criterios que importan más en el caso. Por ejemplo, si el daño es urgente, la rapidez pesa más que el costo.",
        "Fundamentar es explicar por qué elegimos una propuesta, con evidencia y razones. Una fundamentación tiene tres partes: la afirmación (esta propuesta es mejor), la evidencia (datos, hechos, criterios) y la razón (por qué esa evidencia apoya la afirmación). También se reconocen los límites: no hay propuesta perfecta.",
        "Las perspectivas también cuentan. Una persona afectada quiere una solución rápida. Una autoridad piensa en el costo y la ley. Un vecino busca que no se repita. Una buena propuesta escucha a todos y busca el bien común. Si hay perspectivas distintas, se conversa y se buscan acuerdos.",
    ],
    [("propuesta", "idea para resolver un problema"), ("criterio", "regla igual para comparar dos propuestas"), ("fundamentar", "explicar por qué se elige algo con evidencia y razones"), ("costo", "lo que hay que gastar o esforzarse para lograr algo"), ("urgente", "que no puede esperar")],
    [
        ("Comparar con criterios", "Propuesta 1: talleres de respeto (tarda 2 semanas, cuesta poco). Propuesta 2: contratar una charla externa (tarda 2 meses, cuesta más). Si el problema es urgente, ¿cuál conviene según el criterio «tiempo»?", ["Comparo 2 semanas con 2 meses.", "2 semanas es menos.", "Conviene la 1 por ser más rápida."], "La propuesta 1"),
        ("Fundamentar una elección", "Elijo la propuesta 1 porque tarda 2 semanas y el daño es urgente. ¿Cuál es la evidencia?", ["La afirmación es elegir la 1.", "La evidencia es el tiempo de 2 semanas.", "La razón es que el daño es urgente."], "Que tarda 2 semanas"),
    ],
    [
        ("Elegir la propuesta que a mí me gusta sin criterios.", "No se puede defender sin evidencia.", "Compara con criterios y fundamenta."),
        ("Creer que existe una propuesta perfecta.", "Toda propuesta tiene límites.", "Reconoce qué no resuelve."),
    ],
    [
        ("Una propuesta, ¿es una idea para resolver un problema o un insulto?", "Una idea para resolver un problema", "Así se definió en el vocabulario."),
        ("Un daño urgente, ¿puede esperar mucho tiempo o necesita rapidez?", "Necesita rapidez", "Urgente es lo que no puede esperar."),
        ("Para comparar dos propuestas, ¿se usan criterios iguales o distintos?", "Iguales", "Así se compara lo mismo."),
    ],
    [
        ("¿Por qué la rapidez pesa más cuando el daño es urgente?", "Porque el daño sigue mientras se espera", "Una solución tardía no ayuda a tiempo."),
        ("¿Por qué conviene reconocer los límites de una propuesta?", "Porque ninguna resuelve todo", "Eso permite mejorarla."),
        ("¿Por qué escuchar a varias perspectivas ayuda a elegir mejor?", "Porque muestra necesidades que uno solo no ve", "Cada actor conoce una parte del problema."),
    ],
    [
        ("Propuesta A: instalar un buzón de reclamos en la escuela (cuesta $20.000, tarda 1 día). Propuesta B: contratar a un especialista (cuesta $200.000, tarda 1 mes). ¿Cuántas veces más cuesta B que A?", "10", "200.000 dividido en 20.000 es 10.", "200000//20000"),
        ("Con las mismas propuestas: ¿cuál es más rápida según el criterio «tiempo»: A o B?", "A", "1 día es menos que 1 mes."),
        ("Con las mismas propuestas: si solo hay $50.000, ¿cuál se puede pagar?", "La A", "$20.000 es menor que $50.000 y $200.000 no."),
    ],
    [
        ("Rosa dice: «Elijo B porque es más cara y por eso mejor». ¿Qué error comete?", "El precio no prueba que sea mejor", "Hay que comparar con criterios."),
        ("Un vecino dice que la propuesta A no basta, porque solo recibe reclamos pero no los resuelve. ¿Es un límite válido?", "Sí", "Un buzón no soluciona por sí solo el problema."),
    ],
    [
        ("Ordena una fundamentación: A) razón, B) afirmación, C) evidencia.", "B, C, A", "Primero se afirma, luego se da el dato y al final se explica."),
        ("Dos propuestas para proteger a niños en la calle: A) más iluminación y señalización, B) campañas de conversación. Si el peligro es el tránsito de noche, ¿cuál ataca mejor la causa?", "A", "La iluminación reduce el riesgo en la noche."),
    ],
    [("Una escuela debe elegir entre un taller de convivencia que dura 4 semanas y un reglamento nuevo que tarda 1 semana. Hay un problema de burlas que ocurre todos los días. ¿Qué criterio inclina la decisión hacia el reglamento nuevo?", "La rapidez", "El problema es diario y el reglamento tarda menos.")],
    [("¿Qué es fundamentar?", "Explicar por qué se elige algo con evidencia y razones", "Es la definición de la clase."), ("¿Qué criterios sirven para comparar propuestas?", "A quién protege, qué causa ataca, costo y tiempo", "Así se enseñó."), ("¿Existe una propuesta perfecta?", "No", "Toda propuesta tiene límites.")],
    (
        "Problema inventado: en un colegio hay burlas constantes por el acento de algunos estudiantes. Propuesta A: talleres semanales de respeto durante un mes. Propuesta B: sanciones de un día de suspensión a quien se burle. Escribe cuál elegirías, con afirmación, evidencia (al menos dos criterios), razón y un límite, y la perspectiva de un estudiante afectado.",
        "Elijo A. Evidencia: ataca la causa (prejuicio) y no excluye a nadie. Razón: educa. Límite: tarda un mes. Perspectiva: quiere que paren las burlas rápido.",
        ["elige una propuesta", "usa al menos dos criterios", "reconoce un límite", "incluye una perspectiva"],
        ["párrafo con afirmación, evidencia, razón y límite"],
        ["no usar criterios", "no reconocer el límite"],
        "Lee tu párrafo a una persona de tu casa y pídele que diga si la evidencia convence.",
    ),
    "Escribe una propuesta para proteger algún derecho en tu curso y cuánto tardaría.",
    "Escribe qué dato necesitarías para saber si tu propuesta funciona.",
)

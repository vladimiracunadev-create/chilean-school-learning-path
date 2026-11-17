"""Participación y argumentación en democracia (electivo HC, 3.º y 4.º medio): OAC-01 (construir acuerdos y conclusiones en discusiones argumentadas), clases 1 a 4, y OAC-02 (dialogar con relaciones lógicas válidas), clases 1 a 4. Casos ficticios, textos originales y datos de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, ficha o tabla está escrito en el enunciado. "
             "Todos los casos son ficticios (comuna «Villa Alerce», «Liceo Los Pinos») y los datos son de ejemplo. Las posturas se presentan con sus razones y sin tomar partido: "
             "tu tarea es evaluar y construir argumentos, no adivinar cuál postura es «la correcta». Si un tema te afecta personalmente, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O1 = "LL-PADM-3y4-OAC-01"
O2 = "LL-PADM-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso ficticio). En el Liceo Los Pinos se propone prohibir el uso de celulares durante las clases. En la reunión se dijeron cuatro frases. "
     "Frase 1: «El curso que ya tiene el celular prohibido sacó mejor promedio en la última prueba.» Frase 2: «Que nos quiten el celular es faltarnos el respeto.» "
     "Frase 3: «Mejor que prohibir es guardar los celulares en una caja al comenzar la clase.» Frase 4: «El reglamento interno del liceo tiene 12 páginas.»")
build(
    O1, 1, F,
    use="Aprenderé a distinguir qué tipo de desacuerdo hay en un tema controversial (de hechos, de valores o de medios) y qué significa participar y deliberar, para poder construir acuerdos con razones.",
    prior=["Sé que una opinión puede apoyarse en razones.", "Conozco la diferencia entre un dato y una valoración.", "He participado en una reunión de curso o de grupo."],
    explain=[
        "Un tema controversial es un asunto sobre el que personas razonables piensan distinto. Antes de discutir conviene saber en qué se desacuerda. Hay tres tipos: de hechos (si algo ocurre o no, y se resuelve con datos), de valores (qué es más importante, como la libertad o el orden, y no se resuelve contando datos) y de medios (cómo lograr un fin que ya se comparte).",
        "En democracia, participar es mucho más que votar: es informarse, escuchar, argumentar, proponer, decidir y revisar lo decidido. Deliberar es discutir con razones, atendiendo a posturas distintas, antes de llegar a un acuerdo. Un acuerdo es una decisión que el grupo acepta; puede lograrse por consenso (nadie la rechaza con razones fuertes) o por votación.",
        "Separar los tipos de desacuerdo ahorra discusiones inútiles. Un desacuerdo de hechos no se zanja votando: se resuelve con mejor información. Un desacuerdo de valores exige explicar por qué algo importa más. Uno de medios se resuelve comparando alternativas para el mismo fin. En un tema real suelen mezclarse los tres, y un buen grupo los separa antes de decidir.",
    ],
    vocab=[("tema controversial", "asunto sobre el que personas razonables tienen posturas distintas"), ("desacuerdo de hechos", "discrepancia sobre si algo ocurre o no, que se resuelve con datos"), ("desacuerdo de valores", "discrepancia sobre qué es más importante"), ("desacuerdo de medios", "discrepancia sobre cómo lograr un fin compartido"), ("deliberar", "discutir con razones, escuchando posturas distintas, antes de decidir"), ("consenso", "acuerdo que nadie rechaza con razones fuertes")],
    worked=[
        ("Clasificar una frase", "En un consejo vecinal ficticio alguien dice: «El año pasado se registraron más reclamos por ruido que este año». ¿Qué tipo de afirmación es?",
         ["Se pregunta si se puede comprobar con datos: sí, comparando los registros de reclamos.", "Describe lo que ocurre, no lo que es mejor ni cómo actuar."],
         "Es una afirmación de hechos: se resuelve con datos"),
        ("Separar hechos y valores", "Una estudiante dice: «Si el recreo se acorta, estaremos peor y eso es injusto». ¿Qué parte es un hecho por comprobar y cuál un valor?",
         ["«Estaremos peor» predice un efecto que se podría medir: hecho por comprobar.", "«Es injusto» es una valoración sobre lo que importa: valor."],
         "Hecho por comprobar: estaremos peor. Valor: es injusto"),
    ],
    mistakes=[("Creer que participar es solo votar cada cierto tiempo.", "Se confunde la decisión final con todo el proceso que la precede.", "Recuerda que también se participa informándose, escuchando, argumentando y revisando."),
              ("Resolver un desacuerdo de hechos votando.", "Se piensa que la mayoría decide lo verdadero.", "Un hecho se comprueba con datos; la votación sirve para decidir qué hacer, no para saber qué ocurre.")],
    T=[
        ("abc", "{F} La frase 1 afirma algo que se podría comprobar con las notas del curso. ¿Qué tipo de desacuerdo permite?", "De hechos: se resuelve con datos", "De valores: depende de lo que cada uno considere importante", "De medios: propone una forma de actuar", "Es una afirmación sobre lo que ocurre, comprobable con notas."),
        ("abc", "{F} La frase 2 dice que quitar el celular falta el respeto. ¿Qué tipo de desacuerdo muestra?", "De valores: se discute qué importa más", "De hechos: se comprueba con una medición", "De medios: ofrece otra manera de lograr el mismo fin", "Hablar de «respeto» es una valoración y no un dato medible."),
        ("abc", "{F} La frase 3 propone guardar los celulares en una caja. ¿Qué tipo de afirmación es?", "De medios: propone una manera de lograr el fin", "De hechos: describe algo que ya ocurre", "De valores: dice qué es más justo", "Plantea una forma de actuar para lograr el mismo fin."),
        ("{F} ¿Cuál de las cuatro frases deja de ser tema de debate porque basta contar las páginas del reglamento?", "La frase 4", "Se puede comprobar directamente contando páginas, sin discusión de valores."),
        ("abc", "Dos vecinas discuten si el parque nuevo bajó el ruido de la calle. Cada una trae una medición distinta. ¿Qué tipo de desacuerdo es principalmente?", "De hechos: se resuelve con mejores mediciones", "De valores: el ruido es una cuestión de gustos", "De medios: se trata de elegir una herramienta", "Discuten si el ruido bajó o no, algo que se comprueba con datos."),
        ("abc", "Un grupo quiere más seguridad en la plaza. Una persona propone más luces y otra, más rondas de vigilancia. ¿Qué tipo de desacuerdo es?", "De medios: comparten el fin pero difieren en cómo lograrlo", "De hechos: discuten si la plaza existe", "De valores: no comparten el fin de la seguridad", "Coinciden en el fin (más seguridad) y discrepan en cómo lograrlo."),
        ("ab", "¿Qué describe mejor participar en democracia?", "Informarse, escuchar, argumentar, decidir y revisar con otros", "Votar cada cierto tiempo y no opinar entremedio", "Participar incluye todo el proceso, no solo el voto final."),
        ("abc", "En esta asignatura, ¿qué es deliberar?", "Discutir con razones, atendiendo a posturas distintas, antes de decidir", "Votar rápido para ahorrar tiempo", "Repetir la propia postura hasta que los demás cedan", "Deliberar es razonar en conjunto, no imponer ni apurar la decisión."),
        ("abc", "¿Cuál es la mejor pregunta para iniciar un debate sobre las distracciones en clase?", "¿Cómo reducir las distracciones sin perder el trabajo con tecnología?", "¿No es obvio que los celulares arruinan las clases?", "¿Quién tiene la culpa de que el curso se distraiga?", "Es abierta, neutral y apunta al problema, mientras las otras dan la respuesta por hecha o buscan culpables."),
        ("abc", "Tres grupos quieren mejores notas. Uno cree que el celular las baja; otro, que ayuda a investigar; el tercero, que depende del uso. ¿Qué conviene hacer primero?", "Separar lo que se puede comprobar con datos de lo que depende de valores", "Votar de inmediato para no perder tiempo", "Darle la razón al grupo más numeroso", "Primero se aclara qué es comprobable; si no, la votación decidiría hechos."),
        ("abc", "{F} Una estudiante dice: «Como el curso sin celular tuvo mejor promedio, prohibir es lo justo». ¿Qué mezcla esa frase?", "Un hecho (el promedio) con un valor (lo justo): el dato solo no decide lo justo", "Dos hechos distintos que se comprueban igual", "Dos medios para lograr el mismo fin", "El promedio es un dato, pero «lo justo» es una valoración que requiere razones propias."),
        ("Ana dice: «La tarea debe eliminarse porque el descanso vale más que la nota». Beto responde: «Si se elimina, baja el rendimiento». ¿Qué dos tipos de desacuerdo hay entre ambos?", "Uno de valores (Ana) y uno de hechos (Beto)", "Ana habla del valor del descanso y Beto de un efecto que se puede comprobar con datos."),
        ("abc", "¿Por qué no basta votar para zanjar un desacuerdo de hechos?", "Porque la mayoría puede equivocarse: un hecho se comprueba con datos, no con votos", "Porque votar está prohibido en los cursos", "Porque los hechos no existen en los temas controversiales", "La votación decide qué hacer, no qué es verdadero."),
    ],
    ctx=("abc", "En un consejo vecinal ficticio de Villa Alerce, Marta dice: «Si cerramos la calle Central los sábados, bajarán las ventas del almacén». ¿Qué tipo de afirmación es?", "Una predicción de hechos, comprobable con datos de ventas", "Un valor sobre lo que importa más", "Un medio para lograr un fin compartido", "Anuncia un efecto que podría medirse, aunque todavía no ocurre."),
    sc=[
        ("En Participación y argumentación: ¿cómo se llama el desacuerdo que se resuelve con datos?", "De hechos", "Si algo ocurre o no se comprueba con información, no con opiniones."),
        ("En Participación y argumentación: ¿qué tipo de desacuerdo hay cuando todos quieren lo mismo pero discrepan en cómo conseguirlo?", "De medios", "El fin es compartido y se comparan las maneras de lograrlo."),
        ("¿Por qué participar en democracia es más que votar?", "Porque incluye informarse, escuchar, argumentar y revisar lo decidido", "El voto es solo una parte del proceso de participación."),
    ],
    op=("Elige uno. Caso 1: el liceo usa el patio para una cancha, y un grupo propone convertir la mitad en huerto. Caso 2: una propuesta de iniciar las clases 30 minutos más tarde. "
        "Frases ya dichas en el caso 1: «Un huerto vale más que media cancha», «Hay solo una cancha y 400 estudiantes» y «Es mejor turnar el patio por días». Si eliges el caso 2, inventa tú una frase de cada tipo. "
        "Clasifica cada frase (hecho, valor o medio), explica por qué y escribe una pregunta de debate abierta y neutral para el caso elegido.",
        "Caso 1. «Un huerto vale más que media cancha»: valor (qué importa más). «Hay solo una cancha y 400 estudiantes»: hecho, se cuenta. «Turnar el patio por días»: medio. Pregunta: ¿cómo usar el patio para que haya huerto y deporte?",
        ["clasifica correctamente las tres frases", "explica cada clasificación con una razón", "formula una pregunta abierta, neutral y centrada en el problema"],
        ["hoja con tres clasificaciones razonadas y una pregunta de debate"],
        ["clasificar por lo que le parece cierto y no por el tipo de afirmación", "escribir una pregunta que ya contiene la respuesta", "mezclar dos tipos de desacuerdo en una sola frase"],
        "Pregunta: «¿esta frase se resuelve con datos, con razones sobre lo que importa o comparando maneras de actuar?». Si duda, pídele separarla en dos."),
    reinforce="Con la ficha, escribe una frase nueva de cada tipo (hecho, valor y medio) sobre el uso de celulares y comprueba con una compañera si coinciden en clasificarlas.",
    extend="Elige un tema de tu comuna y explica qué parte del desacuerdo es de hechos, cuál de valores y cuál de medios, y qué información faltaría para decidir.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (caso ficticio). El consejo vecinal de Villa Alerce estudia cerrar al tráfico la calle Central los sábados, de 10:00 a 18:00. "
     "Información disponible (de ejemplo): un conteo municipal registró 300 autos por hora en esa calle los sábados; 14 almacenes están en la calle; "
     "en una encuesta informal de 40 vecinos, 22 se mostraron a favor, 12 en contra y 6 sin opinión; no existe medición de ruido ni de ventas.")
build(
    O1, 2, F,
    use="Aprenderé a preparar una discusión sobre un caso público: formular la pregunta, ordenar la información disponible y detectar lo que falta, para que la conclusión del grupo tenga bases.",
    prior=["Sé distinguir desacuerdos de hechos, de valores y de medios.", "Sé que un dato necesita una fuente y una fecha.", "Sé calcular un porcentaje simple."],
    explain=[
        "Investigar un caso público comienza por formular una pregunta de debate clara, abierta y neutral, que no dé por resuelta la respuesta. Luego se ordena la información: qué datos existen, de dónde vienen, qué miden y qué no. Un dato útil tiene fuente identificable, fecha y una definición clara de lo que cuenta. Un dato sin esas características es solo una pista.",
        "También hay que reconocer lo que falta. En el caso, no se sabe cuánto ruido hay ni cuánto venden los almacenes, y esas ausencias importan porque las posturas dependen de ellas. Una buena discusión anota tres columnas: lo que sabemos, lo que creemos y lo que necesitamos averiguar. Con eso se evita decidir como si se supiera más de lo que se sabe.",
        "Una conclusión colectiva puede tener distintas formas: una solución, un acuerdo, una pregunta pendiente o una hipótesis. Una hipótesis es una explicación o predicción provisional que se puede poner a prueba, como «si cerramos un sábado, las ventas bajarán menos del 10 %». Cuando falta información, una conclusión honesta puede ser un acuerdo de probar y medir.",
    ],
    vocab=[("pregunta de debate", "pregunta abierta y neutral que orienta la discusión"), ("fuente", "origen identificable de un dato"), ("hipótesis", "predicción o explicación provisional que se puede poner a prueba"), ("muestra", "parte de un grupo a la que se le pregunta"), ("dato faltante", "información necesaria para decidir que aún no existe"), ("ensayo piloto", "prueba breve y acotada antes de una decisión definitiva")],
    worked=[
        ("Ordenar lo que se sabe", "Con la ficha, separa lo que se sabe de lo que se cree: «Los comerciantes perderían clientes», «Pasan 300 autos por hora los sábados».",
         ["El conteo municipal respalda el segundo dato: es lo que sabemos.", "Lo de los clientes es una predicción sin medición: es lo que creemos y debe averiguarse."],
         "Se sabe: 300 autos por hora. Se cree: que los comerciantes perderían clientes"),
        ("Formular una hipótesis comprobable", "Escribe una hipótesis sobre el efecto en las ventas que pueda ponerse a prueba con un sábado de cierre.",
         ["Define qué se medirá: las ventas de los almacenes ese sábado, comparadas con un sábado normal.", "Escribe la predicción con un criterio: «Las ventas de ese sábado serán al menos el 90 % de las de un sábado normal»."],
         "Hipótesis: las ventas ese sábado serán al menos el 90 % de las de un sábado normal"),
    ],
    mistakes=[("Tratar una encuesta informal de 40 personas como si dijera lo que piensa toda la comuna.", "Se olvida que una muestra pequeña y no elegida al azar puede no representar al conjunto.", "Presenta el resultado como una pista y anota el tamaño y la forma de la muestra."),
              ("Decidir como si faltaran pocos datos, ocultando que no hay medición de ruido ni de ventas.", "Se quiere cerrar rápido la discusión.", "Anota los datos faltantes y propone cómo conseguirlos o probar a pequeña escala.")],
    T=[
        ("abc", "{F} ¿Cuál es la mejor pregunta de debate para este caso?", "¿Cómo equilibrar el uso peatonal de la calle Central con las necesidades de los comercios?", "¿Por qué los vecinos quieren perjudicar a los comerciantes?", "¿No es evidente que hay que cerrar la calle?", "Es abierta y neutral; las otras suponen culpables o dan la respuesta por hecha."),
        ("{F} Según la encuesta informal, ¿cuántos vecinos de los 40 estaban a favor o en contra, sin contar a quienes no opinaron?", "34", "22 a favor más 12 en contra suman 34; los 6 sin opinión quedan fuera."),
        ("abc", "{F} ¿Cuál de estos datos NO existe aún en el caso?", "La medición del ruido de la calle", "El conteo de autos por hora", "La cantidad de almacenes", "La ficha dice que no hay medición de ruido ni de ventas."),
        ("=", "{F} ¿Cuántos autos pasarían en 6 horas del horario de cierre si se mantuviera el conteo de 300 por hora?", "300*6", "Se multiplica el conteo por hora por las seis horas consideradas.", " autos"),
        ("abc", "{F} El conteo de 300 autos por hora, ¿qué tipo de información es?", "Un dato de fuente identificable (conteo municipal)", "Una opinión vecinal sin método", "Una hipótesis por comprobar", "Es un registro con fuente, aunque solo mide autos y no el ruido."),
        ("abc", "{F} Una vecina concluye: «La mayoría de la comuna está a favor, porque 22 de 40 lo están». ¿Qué problema tiene?", "La muestra es pequeña e informal y no representa necesariamente a toda la comuna", "22 es menor que 40, así que no hay mayoría", "La encuesta no tenía a ningún vecino", "Una encuesta informal de 40 personas es una pista, no una medida de toda la comuna."),
        ("ab", "Ante un dato que falta para decidir, ¿qué hace un grupo que delibera bien?", "Lo anota y propone cómo averiguarlo o probar a pequeña escala", "Decide igual y no menciona que falta", "Anotar lo que falta evita decidir como si se supiera más de lo que se sabe."),
        ("abc", "{F} ¿Cuál es una hipótesis que se puede poner a prueba con el cierre de un sábado?", "El ruido medido bajará al menos 10 % durante el cierre", "La calle Central es la más linda de la comuna", "Los vecinos merecen una plaza mejor", "Solo la primera predice algo medible con un criterio claro."),
        ("{F} Con 14 almacenes en la calle, si 3 aceptan participar en una medición de ventas, ¿qué porcentaje del total son? Responde en porcentaje entero aproximado.", "Cerca del 21 %", "3 de 14 es 0,214…, es decir, cerca de 21 %."),
        ("abc", "{F} El grupo no puede ponerse de acuerdo porque faltan datos de ventas y ruido. ¿Qué conclusión colectiva es más honesta?", "Acordar un sábado de prueba y medir ruido y ventas antes de decidir", "Decidir por votación cuál lado tiene la razón", "Cerrar la discusión porque faltan datos", "Una prueba acotada permite decidir con información en vez de suposiciones."),
        ("abc", "Alguien propone medir el ruido, pero con aparatos de su amigo, sin explicar cómo ni cuándo midió. ¿Qué falta para que el dato sea útil al grupo?", "Fuente, fecha y forma de medir identificables", "Que lo diga con seguridad", "Que lo repitan más personas sin explicar el método", "Un dato necesita origen y método claros para poder evaluarlo."),
        ("{F} Para una hipótesis sobre ventas con un sábado de prueba, nombra qué dos cosas deben compararse.", "Las ventas del sábado de cierre y las de un sábado normal", "Sin una comparación con un sábado normal no se sabe si bajaron o subieron."),
        ("abc", "{F} Un participante dice: «Las encuestas informales siempre mienten; descartemos todo dato». ¿Cuál es el mejor comentario?", "Conviene usarlas como pista, declarando su límite, y buscar datos más sólidos", "Tiene razón: sin datos perfectos no se puede decidir", "Conviene tomar la encuesta como si fuera un censo", "Un dato débil no es inútil, pero se presenta con su limitación."),
    ],
    ctx=("abc", "El Liceo Los Pinos pregunta a 30 estudiantes de 3.º A, elegidos porque estaban en el patio, si quieren recreos más largos; 24 dicen que sí. ¿Qué se puede afirmar con cuidado?", "Que 24 de los 30 consultados quieren recreos más largos, sin generalizar a todo el liceo", "Que el 80 % de todo el liceo quiere recreos más largos", "Que los recreos largos son mejores para el aprendizaje", "Solo se describe a quienes se consultó; no se sabe qué piensa el resto ni qué efecto tendría."),
    sc=[
        ("En Participación y argumentación: ¿qué es una hipótesis?", "Una predicción o explicación provisional que se puede poner a prueba", "La hipótesis aún no está comprobada y debe poder contrastarse con datos."),
        ("¿Qué tres columnas ayudan a ordenar la información de un caso?", "Lo que sabemos, lo que creemos y lo que necesitamos averiguar", "Separar esas columnas evita decidir con más certeza de la que se tiene."),
        ("ab", "¿Cuál es una hipótesis comprobable sobre un sábado de cierre de calle?", "En una nueva encuesta, al menos 6 de cada 10 vecinos dirán que usaron la calle peatonal", "El sábado será más agradable para todos", "Solo la primera permite medir y comparar con un criterio claro."),
    ],
    op=("Elige uno. Caso 1: cambiar los vasos plásticos de la feria de Villa Alerce por vasos reutilizables. Información de ejemplo: la feria vende 200 bebidas por fin de semana, el municipio tiene un puesto de lavado disponible dos días por semana y no existe estimación del costo de los vasos reutilizables. "
        "Caso 2: abrir la biblioteca los domingos. Información de ejemplo: la abren 5 días por semana, hay 2 funcionarios y no se sabe cuántos estudiantes irían. "
        "Escribe una pregunta de debate neutral, una tabla de «sabemos / creemos / falta averiguar» con al menos dos filas por columna y una hipótesis comprobable.",
        "Caso 1. Pregunta: ¿cómo reducir los vasos desechables de la feria sin dificultar la venta? Sabemos: 200 bebidas por fin de semana; hay lavado dos días. Creemos: que los clientes aceptarían devolver el vaso. Falta: costo de los vasos y de la devolución. Hipótesis: en un fin de semana de prueba, al menos 8 de cada 10 vasos serán devueltos.",
        ["la pregunta es abierta y neutral", "la tabla separa saber, creer y falta con al menos dos filas por columna", "la hipótesis es comprobable e incluye un criterio medible"],
        ["una pregunta, una tabla y una hipótesis escritas"],
        ["incluir en «sabemos» una creencia sin datos", "formular una hipótesis imposible de medir", "no declarar lo que falta"],
        "Pregunta: «¿cómo sabríamos que tu hipótesis es falsa?». Si no se puede responder, ayúdala a agregar una medida."),
    reinforce="Elige una afirmación de la ficha y clasifícala como lo que sabemos, lo que creemos o lo que falta averiguar, explicando por qué.",
    extend="Escribe cómo mejorarías la encuesta informal para que represente mejor a la comuna (a quién preguntar, cuántos y cómo elegirlos).",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (caso ficticio). El Liceo Los Pinos debate el horario de inicio de clases. Postura A: iniciar a las 8:30 en vez de las 8:00, porque las y los estudiantes llegarían más descansados y habría menos atrasos. "
     "Postura B: mantener las 8:00, porque las familias organizan su trabajo y el transporte según ese horario y porque terminar más tarde recorta las actividades de la tarde. "
     "Ambas posturas dicen querer que el estudiantado aprenda mejor.")
build(
    O1, 3, F,
    use="Aprenderé a contrastar posturas distintas: reformular con justicia lo que otra persona sostiene, distinguir postura de interés y encontrar puntos de acuerdo para construir conclusiones comunes.",
    prior=["Sé qué es un argumento: razones que apoyan una conclusión.", "Sé distinguir desacuerdos de hechos, de valores y de medios.", "Sé escuchar sin interrumpir."],
    explain=[
        "Contrastar perspectivas es poner lado a lado lo que sostienen las distintas partes. La postura es lo que alguien defiende («iniciar a las 8:30»); el interés es lo que busca detrás («que los estudiantes lleguen descansados»). Dos posturas opuestas pueden compartir intereses, y eso abre la posibilidad de un acuerdo que ninguna había pensado.",
        "Para contrastar bien, primero se reformula la postura ajena de manera que su dueño diga «sí, eso es lo que pienso». Reformular no es estar de acuerdo: es comprobar que se entendió. Lo contrario es la caricatura, que distorsiona la postura para refutarla con facilidad. Luego se listan los puntos de acuerdo, los de desacuerdo y las preguntas abiertas.",
        "Con ese mapa se pueden construir conclusiones colectivas: un acuerdo que atienda los intereses compartidos, una solución intermedia o una pregunta pendiente. Una conclusión sólida reconoce qué razones de cada lado fueron consideradas y por qué se eligió una salida. No todo se resuelve por una vía intermedia: a veces hay que decidir entre dos valores que no caben juntos.",
    ],
    vocab=[("postura", "lo que una persona o grupo defiende en un tema"), ("interés", "lo que busca o necesita detrás de su postura"), ("reformular", "decir con otras palabras lo que sostiene otra persona, de modo fiel"), ("caricatura de una postura", "versión distorsionada que facilita refutarla"), ("punto de acuerdo", "aspecto en el que las partes coinciden"), ("solución intermedia", "propuesta que recoge parte de lo que busca cada lado")],
    worked=[
        ("Postura e interés", "En la ficha, ¿cuál es la postura de B y cuál un interés que la sostiene?",
         ["La postura de B es mantener las 8:00.", "Un interés detrás: que las familias puedan organizar su trabajo y el transporte."],
         "Postura: mantener las 8:00. Interés: que las familias organicen su trabajo y transporte"),
        ("Reformulación fiel", "Reformula la postura A de manera que sus defensores la reconozcan.",
         ["Incluye la propuesta: iniciar a las 8:30.", "Incluye sus razones: llegar más descansados y menos atrasos, sin añadir intenciones que no declaró."],
         "«A propone iniciar a las 8:30 para que lleguen más descansados y haya menos atrasos»"),
    ],
    mistakes=[("Reformular la postura ajena en versión exagerada: «A quiere que nadie se levante temprano jamás».", "Se hace más fácil rebatir una versión débil.", "Reformula con las palabras y razones que la otra parte usó, y pregúntale si la reconoce."),
              ("Creer que si dos posturas son opuestas no hay nada en común.", "Se mira solo la postura y no el interés que la origina.", "Pregunta qué busca cada parte; si coinciden en el interés, hay base para acordar.")],
    T=[
        ("abc", "{F} ¿Cuál es la postura de A?", "Iniciar las clases a las 8:30", "Que las familias organicen su transporte", "Terminar más tarde las actividades", "La postura es lo que se defiende explícitamente: iniciar a las 8:30."),
        ("abc", "{F} ¿Qué interés comparten A y B según la ficha?", "Que el estudiantado aprenda mejor", "Iniciar más tarde", "Mantener las 8:00", "La ficha dice que ambas posturas buscan un mejor aprendizaje."),
        ("abc", "{F} ¿Cuál es una razón que da B?", "Las familias organizan trabajo y transporte según ese horario", "Los estudiantes llegarían más descansados", "Habría menos atrasos", "La razón de B es la organización familiar; las otras pertenecen a A."),
        ("abc", "¿Qué reformulación de la postura B es más fiel?", "B propone mantener las 8:00 porque las familias organizan su trabajo según ese horario", "B quiere que los estudiantes sufran levantándose temprano", "B no se preocupa por el aprendizaje", "Solo la primera usa las razones que B declaró; las otras le atribuyen intenciones."),
        ("ab", "Reformular la postura ajena sirve para:", "Comprobar que se entendió, aunque no se comparta", "Aceptar la postura de la otra parte", "Reformular es verificar la comprensión, no adherir a la postura."),
        ("abc", "¿Qué es una caricatura de una postura?", "Una versión distorsionada que se refuta con facilidad", "Un resumen fiel con otras palabras", "Un dibujo que acompaña el acta", "Se distorsiona la postura para que parezca más débil de lo que es."),
        ("abc", "{F} ¿Cuál es un punto de acuerdo entre A y B?", "Ambas quieren que el estudiantado aprenda mejor", "Ambas quieren iniciar a las 8:30", "Ambas piensan que no hay atrasos", "La ficha afirma el objetivo compartido de aprender mejor."),
        ("abc", "{F} ¿Cuál sería una solución intermedia razonable?", "Iniciar a las 8:15 como prueba y comparar atrasos y organización familiar", "Adoptar de inmediato el horario de A sin considerar el transporte de las familias", "Adoptar de inmediato el horario de B sin considerar el descanso del estudiantado", "Recoge parte de lo que preocupa a cada lado y se puede comprobar; las otras ignoran las razones de una parte."),
        ("{F} Si el liceo tiene 600 estudiantes y A calcula 30 atrasos por semana, cada uno de una persona distinta, ¿qué porcentaje del liceo llega atrasado en una semana?", "5 %", "30 de 600 es 30 ÷ 600 = 0,05, es decir 5 %."),
        ("abc", "{F} Una participante dice: «B solo quiere que todo siga igual por flojera». ¿Qué problema tiene?", "Atribuye una intención no declarada y deforma la postura de B", "Es una reformulación fiel con otras palabras", "Es un punto de acuerdo", "B dio razones concretas, y esta frase las ignora para descalificar."),
        ("abc", "Dos grupos discrepan en cuándo reunirse: uno propone mañana y otro, tarde. Ambos buscan que asista la mayor cantidad de gente. ¿Qué conviene hacer?", "Preguntar cuándo puede asistir cada integrante, que es el interés compartido", "Elegir al azar la hora", "Dejar que el grupo más fuerte decida", "El interés común (asistencia) permite buscar una hora que sirva a más personas."),
        ("{F} Escribe una pregunta abierta que quede pendiente porque aún no hay datos para zanjar la postura A.", "¿Cuánto mejora el descanso del estudiantado si se inicia a las 8:30?", "Es una pregunta sobre un hecho no medido que, de responderse, aportaría a decidir."),
        ("abc", "{F} Si, tras contrastar, el grupo concluye «probar durante un mes con inicio 8:15 y comparar atrasos», ¿qué refleja esa conclusión?", "Una solución intermedia que se pone a prueba con datos", "Un empate resuelto al azar", "El triunfo de una de las posturas", "Combina parte de lo que busca cada lado y acuerda medir su efecto."),
    ],
    ctx=("abc", "En una asamblea ficticia del liceo, el centro de estudiantes propone crear un espacio de estudio en la biblioteca durante el almuerzo; la inspectoría teme que quede sin supervisión. Ambos dicen querer que el estudiantado esté seguro y estudie. ¿Qué punto de acuerdo permite avanzar?", "Ambos comparten el interés de seguridad y estudio, por lo que se puede diseñar un espacio con supervisión", "Hay que descartar una de las dos posturas", "No hay nada en común, así que se vota sin hablar", "El interés compartido permite buscar una propuesta que atienda a ambos."),
    sc=[
        ("En Participación y argumentación: ¿qué diferencia hay entre postura e interés?", "La postura es lo que se defiende; el interés es lo que se busca detrás", "Dos posturas distintas pueden responder al mismo interés."),
        ("¿Qué es reformular con fidelidad la postura de otra persona?", "Decirla con otras palabras, de modo que su dueño la reconozca", "Se verifica la comprensión sin deformar ni agregar intenciones."),
        ("¿Qué se hace con los puntos de desacuerdo que quedan después de contrastar?", "Se registran como preguntas abiertas o se decide con razones entre valores", "Un buen balance reconoce lo que sigue en discusión."),
    ],
    op=("Elige uno. Caso 1: el centro de estudiantes de un liceo ficticio discute si las pruebas importantes deben agendarse con dos semanas de anticipación (postura X) o si los docentes deben poder tomarlas según avance la materia (postura Z). X dice que así se organizan mejor; Z, que se evalúa lo realmente enseñado. "
        "Caso 2: un barrio ficticio debate si poner pasto sintético o dejar tierra en la cancha (X: menos mantención, Z: menos calor y menos plástico). "
        "Reformula cada postura con fidelidad, escribe sus intereses, dos puntos de acuerdo y una solución intermedia o una pregunta abierta.",
        "Caso 1. X: agendar con dos semanas para organizarse; interés: previsibilidad. Z: flexibilidad para evaluar lo enseñado; interés: evaluar bien. Acuerdos: ambos quieren evaluaciones justas y que no se junten muchas el mismo día. Solución intermedia: agendar con una semana de anticipación y evitar más de dos pruebas por día.",
        ["reformula cada postura con fidelidad", "distingue postura e interés", "propone puntos de acuerdo reales", "plantea una solución intermedia o una pregunta abierta"],
        ["ficha con dos posturas reformuladas, intereses, acuerdos y propuesta"],
        ["caricaturizar una postura", "confundir postura con interés", "proponer una salida que ignora a una de las partes"],
        "Pregunta: «¿la persona que defiende esa postura diría que la entendiste?». Si no, repite con sus propias razones."),
    reinforce="Elige una postura de la ficha y escribe su reformulación fiel en una oración, indicando una razón que la sustente.",
    extend="Explica una situación en la que dos posturas con el mismo interés no admiten solución intermedia, y cómo se decidiría con razones.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (caso ficticio). El consejo de curso de 3.º A (30 estudiantes presentes) debe decidir cómo usar un espacio del patio: huerto o cancha. "
     "Procedimiento acordado: 1) cada grupo expone sus razones; 2) se hacen preguntas y objeciones; 3) se ajusta la propuesta; 4) se busca consenso y, si no hay, se vota. "
     "En este cuaderno, mayoría absoluta significa más de la mitad de las personas presentes y dos tercios significa dos de cada tres de las presentes. "
     "Votación de ejemplo sobre la propuesta ajustada: 17 a favor, 9 en contra y 4 abstenciones.")
build(
    O1, 4, F,
    use="Aprenderé a deliberar paso a paso hasta construir un acuerdo: proponer, objetar, ajustar y decidir, y a dejar registrado qué se acordó, por qué y qué queda pendiente.",
    prior=["Sé qué es un consenso y qué es una votación.", "Sé separar posturas de intereses.", "Sé contar votos y calcular fracciones simples."],
    explain=[
        "Un acuerdo bien construido sigue un camino: se presenta una propuesta con sus razones, se escuchan objeciones, se ajusta la propuesta para atender las objeciones válidas y recién después se decide. Saltarse las objeciones y votar de inmediato suele dejar acuerdos frágiles, que luego nadie quiere cumplir. Deliberar también implica aceptar que la mejor razón puede venir de otra persona.",
        "La decisión puede ser por consenso o por votación. El consenso exige que nadie tenga una objeción fuerte sin atender; la votación decide cuando no hay consenso. Importa fijar antes qué mayoría se necesita: mayoría absoluta (más de la mitad de las presentes) o dos tercios para decisiones más importantes. Las abstenciones cuentan como presentes, pero no como votos a favor ni en contra.",
        "Un buen registro (acta) incluye la conclusión acordada, las razones principales, las objeciones que quedaron pendientes, quién hará qué y cuándo se revisará la decisión. Así lo decidido se puede evaluar y corregir. Un acuerdo no es eterno: si aparecen nuevos datos, el grupo puede volver a deliberar. Una conclusión puede ser también una pregunta pendiente o una hipótesis para probar.",
    ],
    vocab=[("objeción", "razón que cuestiona una propuesta"), ("ajustar una propuesta", "modificarla para atender objeciones válidas"), ("mayoría absoluta", "en este cuaderno, más de la mitad de las personas presentes"), ("dos tercios", "en este cuaderno, dos de cada tres de las personas presentes"), ("abstención", "no votar a favor ni en contra, quedando como presente"), ("acta", "registro de lo acordado, sus razones y lo pendiente")],
    worked=[
        ("Mayoría absoluta", "En un consejo con 30 presentes, ¿cuántos votos a favor hacen falta como mínimo para mayoría absoluta?",
         ["La mitad de 30 es 15, y se necesita más de la mitad.", "Por lo tanto, 16 votos."],
         "16 votos a favor"),
        ("Ajustar tras una objeción", "Propuesta: «Todo el espacio será huerto». Objeción: «No habrá dónde jugar el recreo». Ajusta la propuesta.",
         ["La objeción es válida: el espacio es compartido.", "Se modifica: la mitad del espacio será huerto y la mitad quedará libre para juegos."],
         "Mitad huerto y mitad libre para juegos"),
    ],
    mistakes=[("Votar apenas se presenta la propuesta, sin escuchar objeciones.", "Se quiere ahorrar tiempo y se confunde votar con deliberar.", "Antes de votar, pide objeciones y ajusta la propuesta cuando sean válidas."),
              ("Contar las abstenciones como votos a favor o en contra.", "Se piensa que quien no opina apoya o rechaza.", "Las abstenciones quedan fuera de ambos lados y cuentan solo como presentes.")],
    T=[
        ("=", "{F} Si en lugar de 30 hubiera 40 personas presentes, ¿cuántos votos serían la mayoría absoluta mínima?", "40//2+1", "Más de la mitad de 40 es 21, no 20.", " votos"),
        ("abc", "{F} ¿Cuál es el primer paso del procedimiento acordado?", "Cada grupo expone sus razones", "Se vota de inmediato", "Se redacta el acta final", "El procedimiento comienza con la exposición de razones."),
        ("abc", "{F} ¿Qué hay que hacer antes de votar si aparece una objeción válida?", "Ajustar la propuesta para atenderla", "Ignorarla para no perder tiempo", "Votar primero la objeción sola", "El paso 3 del procedimiento es ajustar la propuesta."),
        ("=", "{F} ¿Cuántas personas se abstuvieron o votaron en contra en la votación de ejemplo (9 en contra y 4 abstenciones)?", "9+4", "Se suman los 9 votos en contra y las 4 abstenciones.", " personas"),
        ("abc", "{F} Con 17 votos a favor, ¿se logra la mayoría absoluta de los 30 presentes?", "Sí, porque 17 es más de 15", "No, porque faltan 13 votos", "No, porque las abstenciones cuentan como en contra", "Más de la mitad de 30 es 16 o más, y 17 lo supera."),
        ("=", "{F} Si hiciera falta dos tercios de los 30 presentes, ¿cuántos votos serían?", "30*2//3", "Dos tercios de 30 equivalen a 30 ÷ 3 = 10, multiplicado por 2.", " votos"),
        ("abc", "{F} Con 17 votos a favor, ¿se alcanzan los dos tercios de los 30 presentes?", "No, porque se necesitan 20 y hay 17", "Sí, porque 17 supera la mitad de 30", "Sí, porque 17 más 4 abstenciones suman 21", "Dos tercios de 30 son 20 y 17 no los alcanza."),
        ("ab", "Una abstención se cuenta como:", "Persona presente que no vota a favor ni en contra", "Un voto a favor de la propuesta", "No se suma a ningún lado, aunque la persona siga presente."),
        ("abc", "¿Por qué conviene fijar antes de votar qué mayoría se necesita?", "Para que la regla no cambie según el resultado que convenga", "Para poder repetir la votación hasta que salga el resultado esperado", "Porque la mayoría necesaria es siempre la misma en cualquier grupo", "Una regla acordada de antemano evita manipular la decisión."),
        ("abc", "El grupo decide por mayoría absoluta, pero la minoría tiene una objeción nueva y fuerte: la propuesta deja sin patio a quienes usan silla de ruedas. ¿Qué conviene?", "Reabrir la deliberación para atender la objeción antes de aplicar la decisión", "Aplicar la decisión porque ganó la votación", "Pedir a la minoría que acepte, porque ya se votó", "Una objeción fuerte, aunque aparezca tarde, amerita ajustar el acuerdo."),
        ("abc", "{F} ¿Cuál de estos elementos NO corresponde al acta de este consejo?", "El nombre de quien habló más fuerte", "La conclusión acordada", "Las objeciones que quedaron pendientes", "El acta registra lo acordado y lo pendiente, no quién impuso su volumen."),
        ("abc", "{F} El curso decide «probar un mes con huerto en la mitad del espacio y evaluar si hay más conflictos». ¿Qué tipo de conclusión es?", "Un acuerdo de prueba que se revisa con datos", "Una decisión inamovible", "Un empate resuelto por azar", "Incluye una evaluación posterior, así que el acuerdo puede corregirse."),
        ("{F} Si una propuesta recibe 14 votos a favor y 12 en contra, con 4 abstenciones, ¿tiene mayoría absoluta de los 30 presentes? Responde sí o no.", "No", "Necesita más de 15 votos a favor y las abstenciones cuentan como presentes."),
    ],
    ctx=("abc", "Una junta de vecinos ficticia de 24 personas presentes decide pintar un mural. Por mayoría absoluta se necesitan más de la mitad de las presentes. ¿Cuántos votos a favor hacen falta como mínimo?", "13", "12", "14", "La mitad de 24 es 12, y se necesita más que eso, es decir 13."),
    sc=[
        ("En Participación y argumentación: ¿en qué orden se construye un acuerdo?", "Propuesta, objeciones, ajuste y decisión", "El orden asegura que las objeciones se atiendan antes de decidir."),
        ("¿Qué contiene un acta útil?", "Lo acordado, sus razones, lo pendiente, responsables y fecha de revisión", "Así se puede cumplir, evaluar y corregir el acuerdo."),
        ("=", "En un grupo de 21 personas presentes, ¿cuántos votos son dos tercios?", "21*2//3", "Un tercio de 21 es 7 y dos tercios son 14."),
    ],
    op=("Elige uno. Caso 1: tu curso (32 personas presentes) debe elegir entre hacer la fiesta de fin de año en el gimnasio o en un parque cercano; hay objeciones de lluvia y de transporte. "
        "Caso 2: un centro de estudiantes ficticio (18 presentes) decide si destina el dinero recaudado a una salida o a materiales del taller. "
        "Redacta un acta breve con: propuesta inicial, una objeción válida, el ajuste, la regla de decisión elegida (con el número de votos necesarios) y una pregunta pendiente.",
        "Caso 1. Propuesta: fiesta en el parque. Objeción: si llueve no hay dónde ir. Ajuste: parque con plan B en el gimnasio. Regla: mayoría absoluta, 17 votos de 32. Pendiente: ¿cómo se financia el transporte?",
        ["incluye propuesta, objeción y ajuste coherentes", "calcula correctamente el número de votos necesarios", "deja una pregunta o tarea pendiente concreta"],
        ["acta de cinco líneas con el cálculo de la mayoría"],
        ["calcular mal la mayoría absoluta", "ajustar sin relación con la objeción", "no dejar pendientes ni responsables"],
        "Pregunta: «¿qué objeción atendiste y cómo cambió la propuesta?». Si no cambió, pide que la ajuste."),
    reinforce="Con 25 presentes, calcula los votos de mayoría absoluta y los de dos tercios (redondeando hacia arriba), y escribe con tus palabras cuándo usarías cada regla.",
    extend="Explica por qué un acuerdo por votación puede ser legítimo y aun así dejar objeciones pendientes, y qué haría un grupo responsable con ellas.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 5 (textos de ejemplo). Texto 1: «Las bibliotecas deben abrir los sábados, porque muchos estudiantes trabajan de lunes a viernes y solo pueden estudiar ese día.» "
     "Texto 2: «Me encantan los sábados.» "
     "Texto 3: «El lago se congeló porque la temperatura bajó de 0 °C.» "
     "Texto 4: «Todas las aves vuelan. Los pingüinos son aves. Por lo tanto, los pingüinos vuelan.»")
build(
    O2, 1, F,
    use="Aprenderé a reconocer un argumento (premisas y conclusión), a distinguirlo de opiniones y explicaciones y a separar validez de verdad, base del diálogo argumentativo.",
    prior=["Sé que una opinión puede apoyarse en razones.", "Sé leer un texto breve e identificar su idea central.", "Conozco palabras como «porque» y «por lo tanto»."],
    explain=[
        "Un argumento es un conjunto de afirmaciones donde unas, las premisas, buscan apoyar otra, la conclusión. Hay palabras que suelen señalarlos: «porque», «ya que» y «dado que» anuncian premisas; «por lo tanto», «entonces» y «en consecuencia» anuncian la conclusión. Una opinión sin razones no es un argumento, y una explicación aclara por qué ocurrió algo ya aceptado, sin intentar probarlo.",
        "Dos ideas distintas se evalúan en un argumento. La validez se refiere a la lógica: un argumento es válido si, en caso de que las premisas fueran verdaderas, la conclusión tendría que serlo. La verdad se refiere a cada afirmación y a si coincide con los hechos. Un argumento puede ser válido y tener una premisa falsa, y entonces no convence.",
        "Un argumento sólido es válido y además tiene todas sus premisas verdaderas. En el diálogo argumentativo conviene privilegiar la razón: preguntar cuáles son las premisas, si son aceptables y si de ellas se sigue la conclusión. Así el debate se centra en las razones y no en quién habla o con qué fuerza lo dice.",
    ],
    vocab=[("argumento", "premisas que buscan apoyar una conclusión"), ("premisa", "afirmación que sirve de razón"), ("conclusión", "afirmación que se pretende apoyar"), ("validez", "cualidad de un argumento cuya conclusión se sigue necesariamente de las premisas"), ("argumento sólido", "argumento válido con todas sus premisas verdaderas"), ("explicación", "texto que aclara por qué ocurrió algo ya aceptado")],
    worked=[
        ("Premisa y conclusión", "En el texto 1, ¿cuál es la conclusión y cuál es una premisa?",
         ["La palabra «porque» anuncia la razón: muchos estudiantes trabajan de lunes a viernes.", "Lo que se quiere apoyar es que las bibliotecas deben abrir los sábados."],
         "Conclusión: las bibliotecas deben abrir los sábados. Premisa: muchos estudiantes trabajan de lunes a viernes"),
        ("Validez y verdad", "El texto 4, ¿es válido? ¿Es sólido?",
         ["Si fueran verdaderas las dos premisas, la conclusión se seguiría: es válido.", "La primera premisa es falsa (hay aves que no vuelan), así que no es sólido."],
         "Es válido, pero no sólido"),
    ],
    mistakes=[("Pensar que un argumento con conclusión verdadera es siempre válido.", "Se confunde que la conclusión sea cierta con que se siga de las premisas.", "Revisa si las premisas, de ser verdaderas, obligan a aceptar la conclusión."),
              ("Tomar cualquier frase con «porque» como un argumento.", "Hay explicaciones que usan «porque» sin intentar convencer.", "Pregunta si busca probar algo discutible o aclarar por qué ocurrió algo ya aceptado.")],
    T=[
        ("abc", "{F} ¿Cuál es la conclusión del texto 1?", "Las bibliotecas deben abrir los sábados", "Muchos estudiantes trabajan", "Solo pueden estudiar de lunes a viernes", "La conclusión es lo que se quiere apoyar, anunciado antes de «porque»."),
        ("abc", "{F} En el texto 1, ¿qué palabra anuncia la premisa?", "porque", "deben", "sábados", "«Porque» introduce la razón que apoya la conclusión."),
        ("abc", "{F} El texto 2, ¿es un argumento?", "No: expresa un gusto sin premisas ni conclusión", "Sí: la conclusión es que le encantan los sábados", "Sí: la premisa es que existen los sábados", "No ofrece razones que apoyen una afirmación discutible."),
        ("abc", "{F} El texto 3, ¿qué es principalmente?", "Una explicación de por qué ocurrió algo", "Una opinión sin razones", "Un argumento que busca convencer de un hecho discutible", "Aclara la causa de un hecho que se da por aceptado."),
        ("{F} ¿Cuántas premisas tiene el texto 4?", "Dos", "Las premisas son que todas las aves vuelan y que los pingüinos son aves; la conclusión viene tras «por lo tanto»."),
        ("{F} ¿Qué palabras del texto 4 anuncian la conclusión?", "Por lo tanto", "Esas palabras indican que lo que sigue se presenta como consecuencia de las premisas."),
        ("abc", "«Todos los planetas giran alrededor del Sol. Marte es un planeta. Por lo tanto, Marte gira alrededor del Sol». ¿Es válido?", "Sí: si las premisas fueran verdaderas, la conclusión se seguiría", "No: porque Marte está muy lejos", "No: porque tiene dos premisas", "La validez se refiere a la forma, no a la distancia ni al número de premisas."),
        ("abc", "«Todos los peces viven en el agua. Las ballenas viven en el agua. Por lo tanto, las ballenas son peces». ¿Es válido?", "No: vivir en el agua no obliga a ser pez", "Sí: las dos premisas son verdaderas", "Sí: tiene conclusión", "Que las premisas sean verdaderas no basta: la conclusión no se sigue de ellas."),
        ("abc", "«Los gatos son mamíferos. Los mamíferos tienen pelo en algún momento de su vida. Por lo tanto, los gatos tienen pelo en algún momento de su vida». ¿Qué se puede decir?", "Es válido y, con premisas verdaderas, también sólido", "Es inválido porque tiene tres afirmaciones", "Es válido, pero no puede ser sólido", "La conclusión se sigue de las premisas, y estas son verdaderas."),
        ("abc", "«Todos los estudiantes del curso usan lentes. María está en el curso. Por lo tanto, María usa lentes». Si la primera premisa fuera falsa, ¿qué ocurre?", "Sigue siendo válido, pero deja de ser sólido", "Deja de ser válido", "La conclusión pasa a ser falsa siempre", "La validez depende de la relación entre premisas y conclusión, no de su verdad."),
        ("abc", "«Algunos vecinos faltan a las reuniones. Pedro es vecino. Por lo tanto, Pedro falta a las reuniones». ¿Es válido?", "No: que algunos falten no obliga a que Pedro falte", "Sí: la conclusión es verdadera", "Sí: tiene dos premisas", "Las premisas permiten que Pedro sea de los que sí asisten."),
        ("ab", "Un compañero dice: «Mi conclusión es verdadera, así que mi argumento es válido». ¿Qué le responderías?", "La verdad de la conclusión no basta: debe seguirse de las premisas", "Tiene razón: si la conclusión es verdadera, siempre es válido", "Se puede llegar a una conclusión verdadera con un argumento inválido."),
        ("abc", "En el diálogo argumentativo, ¿qué conviene preguntar primero ante una afirmación discutible?", "¿Qué razones la apoyan y se siguen de ellas?", "¿Quién la dijo con más firmeza?", "¿Cuántas personas la repiten?", "Privilegiar la razón significa examinar premisas y su relación con la conclusión."),
    ],
    ctx=("abc", "En un consejo vecinal, alguien dice: «Hay que arreglar la luminaria de pasaje Los Olmos porque lleva dos meses apagada y los vecinos no ven al caminar de noche». ¿Cuál es la conclusión?", "Hay que arreglar la luminaria de pasaje Los Olmos", "Los vecinos no ven al caminar de noche", "La luminaria lleva dos meses apagada", "La frase que sigue a «porque» da razones; lo que se quiere apoyar es la propuesta de arreglar."),
    sc=[
        ("En Participación y argumentación: ¿qué es un argumento?", "Premisas que buscan apoyar una conclusión", "Las razones y la conclusión forman la estructura argumentativa."),
        ("¿Qué diferencia hay entre un argumento válido y uno sólido?", "El sólido es válido y además tiene todas sus premisas verdaderas", "La validez no exige premisas verdaderas, la solidez sí."),
        ("Nombra una palabra que anuncie una premisa.", "Porque", "También sirven «ya que» y «dado que», que introducen razones."),
    ],
    op=("Lee estos dos textos de ejemplo. Texto A: «Debería haber más bebederos en el liceo, ya que en verano hace calor y muchos estudiantes no traen suficiente agua.» Texto B: «Hoy el patio estaba lleno porque no había clases de Educación Física.» "
        "Para cada texto, di si es un argumento, una explicación o una opinión sin razones; si es un argumento, escribe su conclusión y sus premisas en forma ordenada y di si lo consideras válido.",
        "Texto A: argumento. Conclusión: debería haber más bebederos. Premisas: en verano hace calor; muchos estudiantes no traen suficiente agua. Es válido si se acepta que hay que dar acceso al agua a quien lo necesita. Texto B: explicación de por qué el patio estaba lleno.",
        ["distingue argumento y explicación", "identifica conclusión y premisas con orden", "distingue validez de verdad en su comentario"],
        ["tabla con los dos textos clasificados y el argumento reconstruido"],
        ["tomar «porque» como señal infalible de argumento", "confundir validez con verdad", "dejar la conclusión sin formular"],
        "Pregunta: «¿qué afirmación discutible se está apoyando?». Si no hay, no es un argumento."),
    reinforce="Escribe un argumento breve de dos premisas y una conclusión sobre algún tema de tu liceo y marca cada parte.",
    extend="Construye un argumento válido con una premisa falsa y explica por qué no es sólido.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 6 (texto de ejemplo, columna del diario del liceo). «La plaza de Villa Alerce necesita más luminarias. Hace un mes, dos vecinos tuvieron que volver a oscuras por el sendero, y un lugar mal iluminado es un lugar inseguro. Por eso el municipio debería instalar luminarias.» "
     "Argumento B: «Esta bolsa no es biodegradable; por lo tanto, no deberíamos usarla en la feria.»")
build(
    O2, 2, F,
    use="Aprenderé a reconstruir un argumento que aparece en un texto: separar premisas y conclusión, encontrar la premisa implícita y representarlo en un esquema para evaluar sus relaciones lógicas.",
    prior=["Sé qué es una premisa y una conclusión.", "Sé que un argumento puede ser válido sin ser sólido.", "Sé resumir un párrafo."],
    explain=[
        "Reconstruir un argumento significa escribirlo de forma ordenada: primero las premisas, luego la conclusión. En los textos reales las frases no vienen en ese orden y hay palabras de más. Se subraya lo que apoya y lo que se quiere apoyar, y se deja fuera lo que no aporta razones, como ejemplos de adorno o ataques personales.",
        "Muchos argumentos tienen una premisa implícita, que no se dice pero se necesita para que la conclusión se siga. En «esta bolsa no es biodegradable; por lo tanto, no deberíamos usarla», falta la premisa «no deberíamos usar lo que no es biodegradable». Hacerla explícita permite discutirla: puede ser aceptable, discutible o demasiado general.",
        "Un esquema simple ayuda: P1 + P2 → Conclusión. Si hay dos razones que apoyan por separado, se dibujan dos flechas; si las premisas solo funcionan juntas, se unen con un signo más. Al reconstruir se debe ser fiel al texto: se completa lo que falta con la lectura más razonable, y se señala que es un supuesto, no una cita.",
    ],
    vocab=[("reconstruir un argumento", "ordenar premisas y conclusión a partir de un texto"), ("premisa implícita", "razón necesaria que el texto no dice"), ("esquema argumentativo", "diagrama con premisas que apuntan a la conclusión"), ("premisas conjuntas", "premisas que solo apoyan la conclusión al unirse"), ("supuesto", "idea que se acepta sin demostrarla"), ("lectura caritativa", "interpretación más razonable y fuerte del argumento ajeno")],
    worked=[
        ("Reconstruir la columna", "Reconstruye el argumento de la columna de la ficha.",
         ["Premisa 1: dos vecinos tuvieron que volver a oscuras por el sendero. Premisa 2: un lugar mal iluminado es un lugar inseguro.", "Conclusión: el municipio debería instalar luminarias en la plaza."],
         "P1 y P2 → el municipio debería instalar luminarias"),
        ("Premisa implícita", "En el argumento B de la ficha, ¿qué premisa implícita se necesita?",
         ["La conclusión pide no usar la bolsa por no ser biodegradable.", "Para que se siga, hace falta: no deberíamos usar lo que no es biodegradable en la feria."],
         "No deberíamos usar en la feria lo que no es biodegradable"),
    ],
    mistakes=[("Incluir como premisa una frase que solo adorna el texto.", "Se copia todo el párrafo sin preguntar qué apoya a qué.", "Pregunta de cada frase: ¿es razón de la conclusión o es un detalle?"),
              ("Inventar una premisa implícita que el autor probablemente no aceptaría.", "Se completa a conveniencia para refutar con facilidad.", "Escribe la premisa más razonable y señala que es un supuesto.")],
    T=[
        ("abc", "{F} En la columna, ¿cuál es la conclusión?", "El municipio debería instalar luminarias", "La plaza queda en Villa Alerce", "Dos vecinos volvieron a oscuras", "La conclusión es lo que se quiere apoyar, anunciado con «por eso»."),
        ("abc", "{F} ¿Cuál es una premisa de la columna?", "Un lugar mal iluminado es un lugar inseguro", "El municipio debería instalar luminarias", "La plaza necesita más luminarias", "Es una razón general que apoya la conclusión."),
        ("{F} ¿Qué palabras de la columna anuncian la conclusión?", "Por eso", "«Por eso» indica que lo que sigue se presenta como consecuencia de lo anterior."),
        ("abc", "{F} En el argumento B, ¿cuál es la conclusión?", "No deberíamos usar la bolsa en la feria", "La bolsa no es biodegradable", "La feria existe", "La conclusión está después de «por lo tanto»."),
        ("abc", "«La biblioteca cierra a las 20:00; por lo tanto, no podremos sacar libros a las 21:00». ¿Qué premisa implícita hace que la conclusión se siga?", "No se sacan libros cuando la biblioteca está cerrada", "Todas las bibliotecas tienen el mismo horario", "Los libros se leen mejor de noche", "Conecta el horario de cierre con la imposibilidad de sacar libros a esa hora."),
        ("ab", "Una premisa implícita:", "es una razón necesaria que el texto no dice", "es una frase que está de más en el texto", "Es lo que falta para que la conclusión se siga del resto."),
        ("abc", "{F} En la columna, ¿qué función cumple «Hace un mes, dos vecinos tuvieron que volver a oscuras»?", "Es una premisa que da un caso concreto", "Es la conclusión", "Es un ataque personal", "Aporta un hecho que respalda la necesidad de más luz."),
        ("abc", "{F} ¿Qué esquema representa mejor la columna?", "P1 + P2 → debería instalar luminarias", "Conclusión → P1 → P2", "P1 → P2, sin conclusión", "Las premisas se orientan a la conclusión."),
        ("abc", "Texto: «Los talleres deberían ser gratis, ya que cuestan poco al municipio y benefician a muchas familias, y además la gente los pide». ¿Cuántas razones independientes hay?", "Tres: cuestan poco, benefician a muchas familias y la gente los pide", "Una sola, porque hay una conclusión", "Dos, porque «y además» une todo", "Cada razón apoya por separado la conclusión de que sean gratis."),
        ("abc", "Texto: «Una persona puede inscribirse en el taller si tiene más de 15 años y tiene la autorización firmada. Ana tiene 16 años y tiene la autorización firmada. Por lo tanto, Ana puede inscribirse». Las dos premisas sobre Ana, ¿cómo apoyan la conclusión?", "Solo juntas: la regla exige ambas condiciones", "Por separado: cualquiera de las dos basta", "Solo la autorización importa; la edad es un dato de adorno", "La regla pide cumplir las dos condiciones a la vez, por lo que las premisas son conjuntas."),
        ("abc", "{F} Para el argumento «El huerto escolar debe mantenerse, porque los estudiantes aprenden a cuidar plantas», ¿cuál es la premisa implícita más ajustada al texto?", "Lo que enseña a cuidar plantas merece mantenerse", "Todo lo que existe en el liceo merece mantenerse", "Las plantas son seres vivos", "Conecta la razón dada con la conclusión sin generalizar de más ni cambiar de tema."),
        ("abc", "{F} Un compañero reconstruye así el argumento B: «Quien usa bolsas no biodegradables es irresponsable». ¿Qué problema tiene?", "Introduce una premisa que el texto no dijo y ataca a las personas", "Es fiel al texto original", "Es una buena premisa implícita", "El texto habla de la bolsa y del uso en la feria, no de personas irresponsables."),
        ("abc", "{F} La premisa implícita del argumento B, ¿es discutible?", "Sí: alguien podría objetar que no hay alternativas o que depende del uso", "No: nunca se puede discutir una premisa implícita", "No: todas las premisas implícitas son verdaderas", "Hacerla explícita permite objetarla, por ejemplo si no hay alternativas."),
    ],
    ctx=("abc", "Un vecino ficticio escribe: «El club deportivo debe recibir más horas de cancha, porque tiene más socios que los demás y sus socios participan en torneos». ¿Qué premisa implícita hace falta para que la conclusión se siga?", "A quien tiene más socios y participa más se le deben dar más horas de cancha", "Todos los clubes deben tener las mismas horas", "La cancha es del municipio", "Conecta la razón (más socios y participación) con la decisión sobre las horas."),
    sc=[
        ("En Participación y argumentación: ¿qué es una premisa implícita?", "Una razón necesaria que el texto no dice", "Sin ella la conclusión no se seguiría del resto."),
        ("¿Qué es una lectura caritativa de un argumento?", "Interpretarlo de la manera más razonable y fuerte antes de criticarlo", "Se evalúa la mejor versión del argumento y no una caricatura."),
        ("¿Qué se escribe primero al reconstruir un argumento?", "Las premisas, y luego la conclusión", "Ese orden permite ver si la conclusión se sigue de las premisas."),
    ],
    op=("Elige uno de estos textos de ejemplo. Texto 1: «El gimnasio debería abrir en vacaciones, porque en el barrio hay pocos lugares cubiertos para hacer deporte, y los niños se quedarían en la calle.» "
        "Texto 2: «No hay que cobrar entrada a la feria del libro, ya que el objetivo es que lean más personas.» "
        "Reconstruye el argumento (premisas y conclusión), escribe la premisa implícita y dibuja el esquema con flechas. Luego comenta si la premisa implícita te parece aceptable y por qué.",
        "Texto 2. Premisa: el objetivo de la feria es que lean más personas. Conclusión: no hay que cobrar entrada. Implícita: lo que dificulta el acceso va contra el objetivo y no debe hacerse. Esquema: P → C. Comentario: es aceptable, pero habría que ver si la entrada financia la feria.",
        ["separa premisas y conclusión con fidelidad", "formula una premisa implícita razonable", "comenta la aceptabilidad de la premisa implícita"],
        ["reconstrucción escrita con esquema de flechas y comentario"],
        ["copiar el texto completo como si fuera una sola premisa", "inventar una premisa que cambia el sentido", "dibujar una flecha que apunta a una premisa"],
        "Pregunta: «¿la conclusión se sigue de tus premisas sin la implícita?». Si sí, no era necesaria; si no, ya la tienes."),
    reinforce="Reconstruye este argumento y señala una premisa implícita posible: «Hay que arreglar la luminaria de pasaje Los Olmos porque lleva dos meses apagada y los vecinos no ven al caminar de noche».",
    extend="Escribe un argumento de tres premisas encadenadas y dibuja un esquema que muestre cuáles son conjuntas.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 7 (formas de argumento; p y q son afirmaciones). Forma 1: «Si p, entonces q. p. Por lo tanto, q.» Forma 2: «Si p, entonces q. No q. Por lo tanto, no p.» "
     "Forma 3: «Si p, entonces q. q. Por lo tanto, p.» Forma 4: «Si p, entonces q. No p. Por lo tanto, no q.» "
     "Las formas 1 y 2 son válidas; las formas 3 y 4 son inválidas. Ejemplo: «Si llueve, el patio se moja» (p: llueve; q: el patio se moja).")
build(
    O2, 3, F,
    use="Aprenderé a reconocer formas de razonamiento válidas e inválidas con «si… entonces…» y a comprobar con ejemplos si una conclusión se sigue, para dialogar con relaciones lógicas correctas.",
    prior=["Sé qué es un argumento válido.", "Sé distinguir premisa y conclusión.", "Sé que una condición «si p entonces q» dice que p basta para q."],
    explain=[
        "Un enunciado condicional «si p, entonces q» dice que cuando p ocurre, q también ocurre. Con él hay dos formas válidas. Si además se afirma p, se concluye q (forma 1). Si se niega q, se concluye que p no ocurrió (forma 2): si el patio no está mojado, no llovió. Son válidas porque la conclusión no puede ser falsa si las premisas son verdaderas.",
        "Hay dos formas inválidas muy comunes. Afirmar q y concluir p es un error: el patio mojado no prueba que llovió, pues alguien pudo regarlo. Negar p y concluir que no q también es un error: si no llovió, el patio puede estar mojado por otra causa. Para detectar una forma inválida basta un contraejemplo: un caso en que las premisas sean verdaderas y la conclusión falsa.",
        "Estas formas ayudan en el diálogo a ver si una conclusión se sigue, sin discutir primero si las premisas son ciertas. Cuando alguien dice «si cobran entrada, va menos gente; fue poca gente, luego cobraron entrada», se puede responder: «eso afirma q para concluir p; pudo ir poca gente por otra razón». Así se corrige el razonamiento sin atacar a nadie.",
    ],
    vocab=[("condicional", "enunciado «si p, entonces q»"), ("afirmar el antecedente", "afirmar p para concluir q (forma válida)"), ("negar el consecuente", "negar q para concluir no p (forma válida)"), ("afirmar el consecuente", "afirmar q para concluir p (forma inválida)"), ("negar el antecedente", "negar p para concluir no q (forma inválida)"), ("contraejemplo", "caso con premisas verdaderas y conclusión falsa")],
    worked=[
        ("Reconocer una forma válida", "«Si el taller se llena, se abre un segundo grupo. El taller se llenó. Por lo tanto, se abre un segundo grupo.» ¿Qué forma es?",
         ["p: el taller se llena. q: se abre un segundo grupo.", "Se afirma p y se concluye q: forma 1."],
         "Forma 1, válida"),
        ("Detectar una forma inválida con contraejemplo", "«Si estudio, apruebo. Aprobé. Por lo tanto, estudié.» ¿Es válida?",
         ["Es la forma 3: afirma q para concluir p.", "Contraejemplo: alguien pudo aprobar con una buena base sin estudiar esa vez, y las premisas siguen verdaderas."],
         "Inválida: afirma el consecuente"),
    ],
    mistakes=[("Pensar que si el patio está mojado, entonces llovió.", "Se invierte el condicional y se toma q como prueba de p.", "Pregunta si podría haber otra causa de q: si la hay, la forma es inválida."),
              ("Creer que un argumento inválido tiene siempre una conclusión falsa.", "Se mezcla validez con verdad.", "Una forma inválida puede llevar a una conclusión verdadera por azar, pero no la prueba.")],
    T=[
        ("abc", "{F} «Si p, entonces q. p. Por lo tanto, q.» ¿Cuál es su nombre?", "Afirmar el antecedente (válida)", "Afirmar el consecuente (inválida)", "Negar el antecedente (inválida)", "Se afirma p y se concluye q."),
        ("abc", "«Si el proyecto se aprueba, recibe fondos. No recibió fondos. Por lo tanto, no se aprobó.» ¿Qué forma es?", "Negar el consecuente (válida)", "Afirmar el consecuente (inválida)", "Negar el antecedente (inválida)", "Se niega q (no recibió fondos) para concluir no p, como la forma 2."),
        ("abc", "«Si el celular se cae al agua, deja de funcionar. Dejó de funcionar. Por lo tanto, se cayó al agua.» ¿Qué ocurre?", "Es inválida: pudo dejar de funcionar por otra causa", "Es válida: afirma q", "Es válida: todo celular que falla se cayó al agua", "Es la forma 3: la batería o un golpe también pueden causar la falla."),
        ("abc", "{F} «Si p, entonces q. No p. Por lo tanto, no q.» ¿Qué forma es?", "Negar el antecedente (inválida)", "Negar el consecuente (válida)", "Afirmar el antecedente (válida)", "Se niega p y se concluye no q, que es la forma 4."),
        ("abc", "«Si la plaza se riega, el pasto crece. La plaza se regó. Por lo tanto, el pasto crece.» ¿Es válido?", "Sí, afirma el antecedente", "No, afirma el consecuente", "No, niega el antecedente", "Se afirma p (la plaza se regó) para concluir q."),
        ("abc", "«Si hay quórum, la reunión comienza. No comenzó la reunión. Por lo tanto, no hubo quórum.» ¿Es válido?", "Sí, niega el consecuente", "No, afirma el consecuente", "No, niega el antecedente", "Se niega q (no comenzó) para concluir no p (no hubo quórum)."),
        ("abc", "«Si el bus pasa por la plaza, llego a tiempo. Llegué a tiempo. Por lo tanto, el bus pasó por la plaza.» ¿Qué error tiene?", "Afirma el consecuente: pude llegar a tiempo por otro medio", "Niega el antecedente", "No tiene error", "Llegar a tiempo puede deberse a otro bus, a caminar o a otra causa."),
        ("abc", "«Si falta una firma, el trámite se rechaza. Tiene todas las firmas. Por lo tanto, el trámite no se rechaza.» ¿Qué error tiene?", "Niega el antecedente: puede rechazarse por otro motivo", "Afirma el antecedente", "Niega el consecuente", "Hay otros motivos de rechazo además de la firma faltante."),
        ("abc", "Alguien dice: «Si p, entonces q. q. Por lo tanto, p». Para refutar esa forma basta:", "Un contraejemplo con premisas verdaderas y conclusión falsa", "Repetir la conclusión con más fuerza", "Decir que la conclusión es muy extraña", "Un contraejemplo muestra que la forma no garantiza la conclusión."),
        ("Escribe un contraejemplo a este razonamiento: «Si hay clases, el liceo está abierto. El liceo está abierto. Por lo tanto, hay clases».", "El liceo está abierto un sábado para un taller y no hay clases", "Las premisas son verdaderas y la conclusión «hay clases» es falsa."),
        ("abc", "«Si el ahorro crece, hay fondos para el viaje. Hay fondos para el viaje. Por lo tanto, el ahorro creció». Si los fondos vinieron de una rifa, ¿qué muestra esto?", "Que la forma es inválida porque q pudo ocurrir por otra causa", "Que la forma es válida", "Que el ahorro no existe", "La rifa es un contraejemplo: q ocurre sin p."),
        ("abc", "¿Cuál de estas respuestas corrige un razonamiento sin atacar a la persona que lo dijo?", "Eso afirma q para concluir p; pudo haber otras causas", "Eso lo dices porque no entiendes de lógica", "Nadie te hará caso con ese argumento", "Señala la forma del razonamiento y no a la persona."),
        ("abc", "«Si el árbol es un pino, tiene hojas en forma de aguja. Este árbol no es un pino. Por lo tanto, no tiene hojas en forma de aguja». ¿Se sigue la conclusión?", "No: otros árboles también pueden tener hojas en aguja", "Sí: niega el antecedente", "Sí: afirma el consecuente", "Es la forma 4; no ser pino no impide tener hojas en aguja."),
    ],
    ctx=("abc", "En una junta de vecinos ficticia alguien dice: «Si la comunidad se organiza, se limpia la quebrada. La quebrada está limpia. Por lo tanto, la comunidad se organizó». ¿Qué respuesta es correcta?", "Se afirma el consecuente; la quebrada pudo limpiarla otra institución", "Es válido: la quebrada limpia prueba la organización", "Es válido: afirma el antecedente", "Una quebrada limpia puede deberse a otras causas, por lo que la conclusión no se sigue."),
    sc=[
        ("En Participación y argumentación: ¿cuáles son las dos formas condicionales válidas?", "Afirmar el antecedente y negar el consecuente", "Las dos garantizan la conclusión si las premisas son verdaderas."),
        ("¿Qué es un contraejemplo?", "Un caso con premisas verdaderas y conclusión falsa", "Muestra que la forma del argumento no es válida."),
        ("«Si p, entonces q. q.» ¿Qué se puede concluir válidamente sobre p?", "Nada: afirmar q no prueba p", "Hay otras causas posibles de q."),
    ],
    op=("Estas son tres frases de una discusión de ejemplo. Frase 1: «Si bajan los precios, suben las ventas. Subieron las ventas, así que bajaron los precios.» Frase 2: «Si un grupo cumple las reglas, puede usar el salón. El grupo B no puede usar el salón, así que no cumplió las reglas.» "
        "Frase 3: «Si hay lluvia, se suspende el taller. No hay lluvia, así que no se suspende.» Para cada una escribe la forma, di si es válida y, si no lo es, escribe un contraejemplo.",
        "Frase 1: afirma el consecuente; inválida; contraejemplo: subieron las ventas por una campaña, sin cambio de precios. Frase 2: niega el consecuente; válida. Frase 3: niega el antecedente; inválida; contraejemplo: se suspende por falta de monitor.",
        ["identifica la forma de cada frase", "decide su validez con razón", "escribe contraejemplos verosímiles"],
        ["tabla con forma, validez y contraejemplo para cada frase"],
        ["aceptar una forma por parecerle verdadera la conclusión", "dar contraejemplos que contradicen las premisas", "confundir negar el consecuente con negar el antecedente"],
        "Pregunta: «¿tu contraejemplo mantiene verdaderas las premisas y hace falsa la conclusión?». Si no, no sirve."),
    reinforce="Inventa un condicional sobre tu liceo y escribe las cuatro formas con él, marcando cuáles son válidas.",
    extend="Explica por qué la forma 2 (negar el consecuente) es válida usando el ejemplo del patio y un esquema.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 8 (diálogo de ejemplo). Camila: «Debemos cerrar la calle Central los sábados, porque así habría menos ruido y más gente caminando.» "
     "Diego: «Los comerciantes dicen que bajarían las ventas, y si bajan las ventas se pierden empleos.» "
     "Camila: «Es posible, pero no sabemos cuánto bajarían. Propongo cerrar un solo sábado y medir las ventas antes de decidir.» "
     "Diego: «Con una medición clara, acepto probar.»")
build(
    O2, 4, F,
    use="Aprenderé a dialogar argumentando: responder objeciones con razones, conceder lo que corresponde, graduar la fuerza de una conclusión y llegar a conclusiones razonadas sin imponerlas.",
    prior=["Sé reconstruir un argumento.", "Conozco formas válidas e inválidas con «si… entonces…».", "Sé escuchar y reformular."],
    explain=[
        "Dialogar argumentativamente es intercambiar razones para acercarse a una conclusión mejor, no para ganar. Ante una objeción hay cuatro respuestas razonables: rechazar una premisa con una razón, mostrar que la conclusión no se sigue, aceptar la objeción y matizar la conclusión, o proponer una prueba que aclare el punto. Responder con volumen o con insultos no aporta razones y no es argumentar.",
        "Las conclusiones tienen distinta fuerza. Un argumento deductivo válido garantiza la conclusión si las premisas son verdaderas. Un argumento basado en datos, como «en tres sábados de prueba bajó el ruido», apoya la conclusión con cierta probabilidad, pero no la garantiza. Por eso se usan matices: «probablemente», «en la mayoría de los casos». Un matiz honesto muestra hasta dónde llegan las razones.",
        "Una buena conclusión razonada indica qué razones la apoyan, qué objeciones quedan y con qué fuerza se sostiene. Concesión no es derrota: reconocer una objeción válida mejora el argumento. Y la conclusión no se impone: se propone al grupo, que puede aceptarla, ajustarla o pedir más pruebas. Dialogar así hace que los acuerdos se sostengan en razones que todos pueden examinar.",
    ],
    vocab=[("objeción", "razón que cuestiona una premisa o la conclusión"), ("concesión", "reconocer que una objeción tiene parte de razón"), ("matiz", "palabra que gradúa la fuerza de una conclusión"), ("argumento deductivo", "el que, si es válido, garantiza la conclusión con premisas verdaderas"), ("argumento inductivo", "el que apoya la conclusión con cierta probabilidad a partir de casos o datos"), ("prueba aclaratoria", "medición o ensayo que ayuda a zanjar un punto dudoso")],
    worked=[
        ("Clasificar una respuesta", "En la ficha, Camila responde: «Es posible, pero no sabemos cuánto bajarían». ¿Qué tipo de respuesta es?",
         ["Reconoce que la objeción tiene parte de razón: concesión.", "Luego señala un límite de la objeción: falta información sobre cuánto bajarían."],
         "Concesión con matiz, que apunta a medir"),
        ("Graduar una conclusión", "Con datos de tres sábados de prueba en que el ruido bajó, ¿qué conclusión con matiz es más honesta?",
         ["Tres casos apoyan pero no garantizan: argumento inductivo.", "Se formula con matiz: «probablemente el ruido baja cuando se cierra la calle»."],
         "Probablemente el ruido baja cuando se cierra la calle"),
    ],
    mistakes=[("Responder a una objeción repitiendo la conclusión con más fuerza.", "Se confunde firmeza con razón.", "Responde con una razón nueva, una concesión o una propuesta de prueba."),
              ("Presentar una conclusión basada en pocos casos como si fuera segura.", "Se ignora la diferencia entre garantizar y apoyar.", "Usa matices («probablemente», «en estos casos») y ofrece cómo ponerla a prueba.")],
    T=[
        ("abc", "{F} Diego dice que si bajan las ventas se pierden empleos. ¿Qué hace?", "Presenta una objeción con una consecuencia posible", "Acepta la propuesta sin condiciones", "Insulta a Camila", "Aporta una razón en contra que Camila puede evaluar."),
        ("abc", "{F} Diego dice al final: «Con una medición clara, acepto probar». ¿Qué hace?", "Acepta la propuesta con una condición razonada", "Rechaza la propuesta sin razones", "Repite su objeción con más fuerza", "Concede, pero pide una medición que responda a su objeción."),
        ("abc", "{F} ¿Qué propone Camila para aclarar el punto?", "Cerrar un solo sábado y medir las ventas", "Cerrar todos los sábados sin medir", "No cerrar nunca la calle", "Propone una prueba aclaratoria con medición."),
        ("abc", "{F} ¿Por qué Diego acepta probar al final?", "Porque la propuesta incluye una medición clara", "Porque Camila habló más fuerte", "Porque se cansó de discutir", "La medición responde a su objeción con datos."),
        ("ab", "Ante una objeción válida, ¿qué mejora el argumento?", "Conceder lo que corresponde y ajustar la conclusión", "Repetir la conclusión sin cambios", "Reconocer una objeción válida fortalece la credibilidad de la argumentación."),
        ("abc", "¿Cuál de estas respuestas a una objeción aporta razones?", "Tu objeción supone que los comercios dependen de los autos; ¿qué datos lo muestran?", "Eso es una tontería", "Nadie piensa como tú", "La primera cuestiona una premisa y pide evidencia."),
        ("abc", "Un argumento deductivo válido con premisas verdaderas:", "Garantiza la conclusión", "La hace probable, sin garantía", "No dice nada sobre ella", "La validez asegura que la conclusión sigue de las premisas."),
        ("abc", "«En los dos cursos que probaron el huerto, bajaron los conflictos del patio. Por lo tanto, el huerto baja los conflictos.» Lo más correcto es decir que es:", "Un argumento inductivo: apoya la conclusión sin garantizarla", "Un argumento deductivo que la garantiza", "Una explicación sin conclusión", "Dos casos son pocos para garantizar una regla general."),
        ("abc", "{F} ¿Qué matiz es más honesto para una conclusión basada en una sola prueba de un sábado?", "En esta prueba, las ventas bajaron menos de lo temido", "Está probado que nunca bajan las ventas", "Todos los comercios ganarán", "Un solo caso apoya un resultado limitado, no una regla general."),
        ("abc", "Un participante dice: «Como en tres reuniones nadie faltó, nadie faltará jamás». ¿Qué problema tiene?", "Convierte tres casos en una regla segura", "Es una forma deductiva válida", "Niega el antecedente", "Pocos casos no garantizan lo que ocurrirá siempre."),
        ("{F} Escribe una pregunta que Diego podría hacer para aclarar qué se mediría en la prueba.", "¿Qué ventas compararemos y con qué sábado de referencia?", "La pregunta pide precisar el criterio de medición."),
        ("abc", "{F} Si después del sábado de prueba las ventas bajaron un poco y el ruido bajó mucho, ¿cuál es una conclusión razonada?", "Cerrar un sábado parece reducir el ruido con un costo moderado, aunque convendría repetir la prueba", "Está probado que cerrar es lo mejor", "Está probado que hay que abrir siempre", "Reconoce la evidencia y su límite sin dar certeza."),
        ("abc", "Alguien concluye con un matiz: «probablemente conviene repetir la prueba». ¿Qué comunica?", "Hasta dónde llegan las razones y que falta evidencia", "Que no tiene opinión", "Que quiere evitar el debate", "El matiz muestra la fuerza real de la conclusión."),
    ],
    ctx=("abc", "En un consejo estudiantil ficticio alguien propone un taller de música en el recreo; otra persona objeta que el ruido molestaría a las salas. ¿Cuál es una respuesta argumentativa adecuada?", "Concedo que puede haber ruido; propongo usar el gimnasio y probar dos semanas", "Estás en contra de la música", "Si no te gusta, no vengas", "Reconoce la objeción, ofrece un ajuste y propone una prueba."),
    sc=[
        ("En Participación y argumentación: ¿qué es una concesión?", "Reconocer que una objeción tiene parte de razón", "Concesión no es derrota: mejora la credibilidad del argumento."),
        ("¿Qué diferencia hay entre garantizar y apoyar una conclusión?", "Garantizar es propio de un deductivo válido; apoyar es dar probabilidad con datos", "Los casos o datos pueden apoyar pero no garantizar."),
        ("Nombra un matiz que gradúe una conclusión.", "Probablemente", "Otros matices son «en general» o «en estos casos»."),
    ],
    op=("Elige uno. Caso 1: una compañera propone que el curso venda galletas para financiar la salida y alguien objeta que habría que cocinar y que algunos no pueden. Caso 2: se propone que cada curso tenga un día de limpieza de patio y alguien objeta que roba tiempo de clases. "
        "Escribe un diálogo de cuatro intervenciones con propuesta, objeción, respuesta (con concesión o contraargumento) y una conclusión con matiz, indicando si el argumento final es más deductivo o inductivo.",
        "Caso 1. A: «Vendamos galletas, porque así reunimos plata sin pedirla a las familias.» B: «Habría que cocinar y no todos pueden.» A: «Es cierto; propongo comprar las galletas hechas y ver cuánto se vende en una semana.» Conclusión: probablemente reunamos lo necesario; es inductivo porque se basa en una prueba breve.",
        ["incluye propuesta, objeción y respuesta con razones", "usa una concesión o contraargumento y no ataca a personas", "gradúa la conclusión con un matiz coherente"],
        ["diálogo de cuatro intervenciones con conclusión matizada"],
        ["responder a la objeción con otra afirmación sin razones", "atacar a la persona", "presentar una conclusión inductiva como segura"],
        "Pregunta: «¿qué razón nueva aporta tu respuesta a la objeción?». Si ninguna, pide una concesión o una prueba."),
    reinforce="Reescribe la última intervención de Diego de la ficha con otra objeción que Camila podría responder con una razón.",
    extend="Explica cuándo un acuerdo debería reabrirse si aparecen nuevos datos, y cómo se comunicaría sin culpar a nadie.",
)

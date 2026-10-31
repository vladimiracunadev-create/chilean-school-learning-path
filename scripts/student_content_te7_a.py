"""Cuaderno del estudiante, 7.º básico Tecnología: OA 01 (necesidades de reparación, adaptación o mejora), clases 1 a 4.

Seguridad: solo papel, cartón, cinta, cordel, pegamento en barra y tijeras de punta roma; nada de cortadores, fuego, vidrio, electricidad de red ni herramientas con filo.
Cifras enteras. Los casos son inventados para practicar y no nombran marcas ni personas reales.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "TE07 OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    def conv(i):
        return i if isinstance(i, dict) else ex(*i)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [conv(i) for i in R], "understand": [conv(i) for i in C], "apply": [conv(i) for i in A], "reason": [conv(i) for i in Z], "challenge": [conv(i) for i in D]},
        context=[conv(ctx)], selfcheck=[conv(i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 01, clase 1
reg(
    OA1, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus respuestas.",
    use="Aprenderé a distinguir si una necesidad pide reparar, adaptar o mejorar, y si es personal o de un grupo. Sirve para elegir bien el tipo de solución antes de diseñar.",
    prior=["Sé que una necesidad es algo que falta o que no funciona bien.", "Sé que un usuario es quien usa un objeto.", "Sé que un criterio es una condición que se puede comprobar."],
    explain=[
        "En Tecnología, muchas soluciones responden a una de tres necesidades. Reparar es devolverle su función a algo que se dañó o dejó de funcionar. Adaptar es modificar un objeto o un lugar para que lo use otra persona o sirva para un uso distinto. Mejorar es hacer que algo que ya funciona sirva mejor, sea más cómodo o dure más.",
        "Para clasificar una necesidad hazte tres preguntas. ¿Dejó de funcionar? Entonces se repara. ¿Debe servir a otra persona o para otro uso? Entonces se adapta. ¿Funciona, pero podría servir mejor? Entonces se mejora. Comprar un objeto nuevo no es reparar, porque el objeto original se descarta.",
        "Una necesidad puede ser personal, si afecta a una sola persona, o grupal, si afecta a varias, como un curso, una familia o un barrio. Se llama entorno cercano a los lugares que conoces y usas todos los días: tu casa, tu sala, el patio, la calle de tu cuadra. Ahí es más fácil observar y comprobar si una solución resultó.",
    ],
    vocab=[("reparar", "devolver su función a algo que se dañó"), ("adaptar", "modificar algo para otra persona o para otro uso"), ("mejorar", "hacer que algo que funciona sirva mejor"), ("necesidad grupal", "necesidad que afecta a varias personas"), ("entorno cercano", "lugares que usas a diario, como tu casa, tu sala o tu barrio")],
    worked=[
        ("Clasificar una necesidad personal", "El cierre de la mochila de Camila se trabó y ya no cierra. ¿Es reparar, adaptar o mejorar? ¿Es personal o grupal?", ["Pregunto: ¿dejó de funcionar? Sí, el cierre ya no cierra.", "Solo afecta a Camila."], "Es reparar, y es una necesidad personal"),
        ("Clasificar una necesidad grupal", "En una sala, el estante de los libros está tan alto que un compañero en silla de ruedas no alcanza los de arriba. ¿Qué tipo de necesidad es?", ["El estante funciona, pero no sirve para todas las personas del curso.", "Debe servir a otro usuario: se trata de adaptar. Afecta a varias personas de la sala, así que es grupal."], "Es adaptar, y es una necesidad grupal"),
    ],
    mistakes=[
        ("Pensar que reparar es comprar uno nuevo.", "Se confunde arreglar con reemplazar; el objeto original no se conserva.", "Reparar conserva el objeto y arregla la parte dañada."),
        ("Creer que mejorar es solo cambiar el color o la apariencia.", "Un cambio de apariencia no hace que el objeto sirva mejor.", "Mejorar cambia algo que hace que el uso sea más cómodo, seguro o durable."),
    ],
    R=[
        ("La rueda de una mochila con ruedas se salió y ya no gira. ¿Es una necesidad de reparar, adaptar o mejorar?", "Reparar", "El objeto dejó de funcionar y hay que devolverle su función."),
        ("Un curso quiere más luz natural en su sala de estudio, que ya se puede usar. ¿Es reparar, adaptar o mejorar?", "Mejorar", "La sala ya funciona; se busca que sirva mejor."),
        ("A un compañero con poca fuerza en la mano le cuesta sujetar un lápiz delgado, y se le pone una funda gruesa de espuma. ¿Es reparar, adaptar o mejorar?", "Adaptar", "El lápiz funciona, pero se modifica para que lo use otra persona."),
    ],
    C=[
        ("¿Cuál es una necesidad grupal del entorno cercano? A «a Joaquín se le perdió una zapatilla», B «en el patio del curso no hay dónde sentarse a la sombra».", "B", "B afecta a todo el curso; A afecta solo a una persona."),
        ("Pablo dice: «Reparar es comprar uno nuevo para reemplazar al roto». ¿Tiene razón?", "No", "Reparar arregla el objeto original; comprar uno nuevo lo descarta."),
        ("¿Cuál pregunta ayuda a reconocer una adaptación? A «¿Debe servir a otra persona o para otro uso?», B «¿Dejó de funcionar del todo?».", "A", "La adaptación cambia el objeto para otro usuario o uso; si dejó de funcionar, la necesidad es de reparar."),
    ],
    A=[
        arith("Un curso de 32 estudiantes anotó sus necesidades: 11 son de reparar y 9 de adaptar; todas las demás son de mejorar. ¿Cuántas son de mejorar?", "32-11-9", "Se restan las de reparar y adaptar del total.", " necesidades"),
        ("Clasifica con R (reparar), M (mejorar) o AD (adaptar), en orden: (1) un cajón que se salió del riel, (2) un cajón que funciona pero se abre con ruido, (3) un cajón con una perilla baja para una niña de 4 años.", "1 R, 2 M, 3 AD", "El primero dejó de funcionar, el segundo funciona pero puede servir mejor y el tercero se modifica para otra usuaria."),
        ("¿Cuál redacta la necesidad sin nombrar la solución? A «ver el pizarrón desde cualquier puesto de la sala», B «comprar un pizarrón más grande».", "A", "A dice qué lograr; B ya propone el objeto."),
    ],
    Z=[
        ("Una vecina dice que necesita «un paraguas nuevo». Otra dice que necesita «volver a protegerse de la lluvia al caminar». ¿Cuál formulación deja más opciones para reparar, adaptar o mejorar?", "La segunda", "No nombra el objeto y permite arreglar el paraguas, adaptar otra cosa o mejorar."),
        ("Una puerta de ropero no cierra porque la bisagra se soltó. Idea 1: reemplazar el ropero. Idea 2: volver a apretar la bisagra. Idea 3: agregar una segunda puerta. ¿Cuál es una reparación?", "La idea 2", "Solo ella devuelve la función al objeto original; la 1 lo descarta y la 3 lo modifica."),
    ],
    D=[
        arith("Un curso de 36 estudiantes forma 6 equipos iguales. Cada equipo anota 5 necesidades, pero 8 de ellas se repiten entre equipos. ¿Cuántas necesidades distintas quedan?", "6*5-8", "Se calcula el total anotado y se descuentan las repetidas.", " necesidades"),
        ("El curso prioriza la necesidad que afecta a más personas y, si hay empate, la que se resuelve en menos días. X: 12 personas, 3 días. Y: 5 personas, 1 día. Z: 12 personas, 1 día. ¿Cuál se elige?", "Z", "X y Z empatan en 12 personas, y Z se resuelve en menos días."),
    ],
    ctx=("En tu casa, el cordel de una cortina se cortó y no sube, y un niño de 6 años que visita tu casa no alcanza a tirar de él. Indica qué parte es reparar y qué parte es adaptar.", "Reparar: reponer el cordel cortado. Adaptar: dejarlo a una altura que alcance una persona más pequeña", "Se repara lo que dejó de funcionar y se adapta lo que debe servir a otro usuario."),
    sc=[
        ("¿Qué significa adaptar un objeto?", "Modificarlo para que lo use otra persona o sirva para otro uso", "Es la definición de adaptar."),
        ("¿Una necesidad que afecta a todo un curso es personal o grupal?", "Grupal", "Afecta a varias personas."),
        ("¿Comprar un objeto nuevo para reemplazar el roto cuenta como reparar?", "No", "La reparación conserva y arregla el objeto original."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: una banca del patio perdió una tabla del asiento y se hunde. Caso 2: en la entrada de la sala hay un escalón alto y una compañera con muletas entra con dificultad. Caso 3: la mochila de un compañero funciona, pero sus tirantes finos le molestan en los hombros. Escribe el tipo de necesidad (reparar, adaptar o mejorar), si es personal o grupal, quién es el usuario y una frase que diga qué se debe lograr, sin nombrar el objeto de la solución.",
        "Caso 2: es adaptar y es grupal; usuaria: la compañera con muletas. Se debe lograr que cualquier persona pueda entrar a la sala sin esfuerzo ni riesgo",
        ["clasifica el tipo de necesidad", "indica si es personal o grupal", "nombra al usuario", "redacta la necesidad sin nombrar la solución"],
        ["ficha con tipo, alcance, usuario y necesidad"],
        ["confundir reparar con reemplazar", "nombrar el objeto de la solución dentro de la necesidad"],
        "Pregunta: «¿esta frase dice qué lograr o ya dice qué construir?». Si dice qué construir, pídele reescribirla.",
    ),
    reinforce="Mira tres objetos de tu casa y di, para cada uno, si podrían necesitar reparar, adaptar o mejorar.",
    extend="Piensa en un objeto del curso que sirva bien a unas personas y mal a otras, y explica qué adaptación lo haría más justo.",
)

# ------------------------------------------------------------------ OA 01, clase 2
reg(
    OA1, 2,
    materials="Hoja, lápiz y las tablas escritas en este cuaderno. Para practicar, un recreo o un momento en tu casa para observar.",
    use="Aprenderé a descubrir necesidades observando y preguntando, a registrar lo que veo en una tabla y a decidir cuál conviene resolver primero. Sirve para elegir una necesidad real y no una imaginada.",
    prior=["Sé que una necesidad puede ser de reparar, adaptar o mejorar.", "Sé leer una tabla simple.", "Sé sumar y calcular un promedio."],
    explain=[
        "Las necesidades se encuentran mirando el entorno con atención. Observar es mirar con un propósito y anotar qué ocurre, dónde y cuántas veces. Conversar con las personas que usan el lugar o el objeto, que son los usuarios, entrega lo que tú no ves. Una pregunta abierta, como «¿qué te molesta al usarlo?», da más información que una pregunta de sí o no.",
        "Lo que observas se registra en una tabla de conteo: una fila por situación y una columna por día o momento. Con los datos puedes sumar o calcular un promedio, que es la suma dividida entre la cantidad de datos. Así tienes evidencia: datos que apoyan tu decisión, y no solo opiniones.",
        "Si encuentras varias necesidades, hay que priorizar, es decir, decidir cuál resolver primero. Se usan criterios claros: cuántas personas afecta, si hay riesgo de daño y qué tan posible es resolverla con el tiempo y los materiales que hay. Al observar y preguntar, respeta a las personas: no anotes nombres y pide permiso antes de preguntar.",
    ],
    vocab=[("observar", "mirar con un propósito y anotar lo que ocurre"), ("pregunta abierta", "pregunta que no se responde con sí o no"), ("evidencia", "datos que apoyan una decisión"), ("priorizar", "decidir qué se resuelve primero"), ("promedio", "suma de los datos dividida entre la cantidad de datos")],
    worked=[
        ("Calcular un promedio de observación", "Durante 4 recreos se anotó cuántas veces la pelota cayó a la canaleta del patio: 3, 2, 4 y 3. ¿Cuál es el promedio por recreo?", ["Sumo: 3 + 2 + 4 + 3 = 12.", "Divido 12 entre 4."], "3 veces por recreo"),
        ("Convertir una pregunta cerrada en abierta", "Para investigar el banco del patio, un grupo preguntó: «¿Te gusta el banco?». ¿Cómo la mejoras?", ["Con «sí» o «no» no sé qué falla.", "Pregunto algo que obligue a explicar: «¿Qué te molesta al sentarte en el banco?»."], "«¿Qué te molesta al sentarte en el banco?»"),
    ],
    mistakes=[
        ("Preguntar «¿no cree que el banco está muy incómodo?».", "La pregunta empuja a una respuesta y no entrega información real.", "Haz preguntas abiertas y neutras, como «¿cómo es usar el banco?»."),
        ("Elegir la necesidad que más me gusta, sin mirar los datos.", "La decisión queda en una preferencia y no en evidencia.", "Prioriza con criterios y con los números de la tabla."),
    ],
    R=[
        ("Observar, ¿es mirar con un propósito y anotar, o solo mirar por mirar?", "Mirar con un propósito y anotar", "Observar en Tecnología exige registrar lo que ocurre."),
        ("¿Cuál es una pregunta abierta? A «¿Qué te molesta al usar tu mochila?», B «¿Tu mochila es incómoda, sí o no?».", "A", "A obliga a explicar; B se responde con sí o no."),
        ("Al priorizar, ¿se decide qué se resuelve primero o qué se olvida para siempre?", "Qué se resuelve primero", "Priorizar es ordenar las necesidades."),
    ],
    C=[
        ("¿Por qué conviene conversar con quienes usan un lugar? A «porque ven detalles que yo no veo», B «porque ellos deciden cuál es la solución final».", "A", "Los usuarios aportan información que la observación sola no entrega."),
        ("Una compañera dice: «Anotar en la tabla que fueron 12 caídas es solo una opinión». ¿Tiene razón?", "No", "Un conteo es evidencia, no una opinión."),
        ("Antes de preguntar a otras personas sobre un lugar, ¿qué debes hacer?", "Pedir permiso y no anotar sus nombres", "Se respeta su privacidad."),
    ],
    A=[
        arith("En 5 días se contó cuántos estudiantes esperaron más de 10 minutos para usar el bebedero: 4, 6, 5, 7 y 8. ¿Cuántos fueron en total?", "4+6+5+7+8", "Se suman los datos de los cinco días.", " estudiantes"),
        arith("La tabla de la pelota en la canaleta marca 6 caídas en el primer recreo, 2 en el segundo y 4 en el tercero. ¿Cuál es el promedio por recreo?", "(6+2+4)//3", "Se suman los datos y se divide entre 3.", " caídas"),
        ("Criterios del curso, con 1 punto por cada «sí»: afecta a más de 10 personas, hay riesgo de golpes y se resuelve con cartón. Necesidad P: sí, no, sí. Necesidad Q: sí, sí, no. Necesidad R: no, sí, sí. Necesidad S: sí, sí, sí. ¿Cuál se prioriza?", "S", "S suma 3 puntos y las demás suman 2."),
    ],
    Z=[
        ("Un grupo observó un solo recreo y anotó: «los estudiantes no usan el banco». Otro grupo observó 4 recreos y anotó 0, 1, 0 y 1 estudiantes sentados. ¿Cuál tiene mejor evidencia y por qué?", "El segundo, porque observó varias veces", "Una sola observación puede ser casual."),
        ("Para saber si el estante del curso está muy alto, ¿qué sirve más? A medir la altura de la repisa más alta y preguntar a 10 estudiantes si la alcanzan, B preguntar solo a quien está sentado cerca.", "A", "A reúne una medida y varias opiniones; B solo tiene una opinión."),
    ],
    D=[
        arith("Un curso de 30 estudiantes responde una pregunta abierta. 12 mencionan que la sala es muy fría, 9 que el pizarrón brilla y el resto no menciona problemas. ¿Cuántos no mencionan problemas?", "30-12-9", "Se restan los que mencionaron problemas del total.", " estudiantes"),
        arith("La tabla de observación dice que el recreo largo dura 25 minutos y que en cada uno se pierden 5 minutos buscando la pelota. Si hay 4 recreos largos en la semana, ¿cuántos minutos de juego se pierden en total?", "5*4", "Se multiplican los 5 minutos perdidos por los 4 recreos.", " minutos"),
    ],
    ctx=("En tu casa quieres descubrir una necesidad en la entrada: durante 4 días anotas cuántas veces alguien no encuentra dónde dejar las llaves: 2, 3, 3 y 4. Calcula el promedio por día y escribe una pregunta abierta para quienes viven ahí.", "Promedio: 3 veces por día. Pregunta: «¿Qué te molesta cuando buscas dónde dejar las llaves?»", "Se suma 2 + 3 + 3 + 4 = 12 y se divide entre 4, y la pregunta no se responde con sí o no."),
    sc=[
        ("¿Qué es una pregunta abierta?", "Una pregunta que no se responde con sí o no", "Pide explicar y entrega más información."),
        ("¿Para qué sirve la tabla de conteo?", "Para registrar cuántas veces ocurre algo", "Los datos sirven de evidencia."),
        ("¿Qué criterios sirven para priorizar?", "Cuántas personas afecta, el riesgo y si es posible resolverla", "Son criterios comprobables."),
    ],
    open_task=(
        "Escoge un registro. Registro 1 (veces que alguien se queda sin lugar en las bancas del patio en 4 recreos): 5, 7, 6 y 6. Registro 2 (veces que se atasca la puerta de la sala en 5 días): 2, 0, 3, 1 y 4. Calcula el total y el promedio, escribe una pregunta abierta para quienes usan el lugar y di si priorizarías esa necesidad, con una razón basada en los datos.",
        "Registro 2: total 10 y promedio 2 por día. Pregunta: «¿Qué te pasa cuando intentas abrir la puerta?». La priorizo porque se atasca casi todos los días y puede pillar dedos",
        ["calcula bien total y promedio", "formula una pregunta abierta", "decide con una razón basada en los datos", "respeta la privacidad de las personas"],
        ["hoja con cálculo, pregunta y decisión"],
        ["preguntar con sí o no", "decidir sin mirar los datos"],
        "Pregunta: «¿qué número de la tabla apoya tu decisión?». Si no cita ninguno, pídele volver a los datos.",
    ),
    reinforce="Durante dos días cuenta cuántas veces algo en tu casa te molesta o falla y anota los números en una tabla.",
    extend="Escribe tres preguntas abiertas para descubrir qué necesitan las personas que usan el patio de tu escuela.",
)

# ------------------------------------------------------------------ OA 01, clase 3
reg(
    OA1, 3,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a escribir una necesidad con su usuario, sus criterios y sus restricciones, y a revisar si está bien formulada. Sirve para que el diseño tenga una meta clara antes de dibujar.",
    prior=["Sé clasificar una necesidad como reparar, adaptar o mejorar.", "Sé que priorizar es elegir qué se resuelve primero.", "Sé medir en centímetros y gramos."],
    explain=[
        "Una necesidad bien escrita tiene tres partes. Primero el usuario, que es quien usará la solución. Segundo, la necesidad misma, que dice qué se debe lograr sin nombrar el objeto de la solución. Tercero, los criterios, que son condiciones que se pueden comprobar, como «se arma en menos de 20 minutos» o «aguanta 2 kilos».",
        "Además se anotan las restricciones, que son los límites del problema: el dinero disponible, el tamaño máximo, el tiempo o los materiales que hay. Los criterios dicen cómo debe ser una buena solución; las restricciones dicen hasta dónde se puede llegar. Si dos criterios chocan, por ejemplo «muy resistente» y «muy liviano», hay que decidir cuál pesa más.",
        "Para revisar tu texto pregúntate si cada criterio se puede contar, medir u observar. «Que sea cómodo» no se puede comprobar; «que se pueda usar con una sola mano» sí. Escribir bien la necesidad evita construir algo que no sirve a quien lo iba a usar.",
    ],
    vocab=[("usuario", "persona que usará la solución"), ("criterio", "condición comprobable que debe cumplir la solución"), ("restricción", "límite del problema, como dinero, tiempo o tamaño"), ("comprobable", "que se puede contar, medir u observar"), ("formular", "escribir con claridad una idea o un problema")],
    worked=[
        ("Escribir una necesidad completa", "Los cuadernos del curso se mojan en la mochila los días de lluvia. Escribe usuario, necesidad y un criterio.", ["Usuario: los estudiantes del curso.", "Necesidad (sin nombrar el objeto): mantener secos los cuadernos al transportarlos.", "Criterio comprobable: un cuaderno queda seco tras 5 minutos bajo una lluvia de prueba con un regador."], "Usuario: estudiantes. Necesidad: mantener secos los cuadernos. Criterio: queda seco tras 5 minutos de lluvia de prueba"),
        ("Separar criterio de restricción", "Un grupo escribe: «debe costar menos de $3.000», «debe resistir 2 kilos» y «debe caber en un cajón de 30 cm de ancho». ¿Cuáles son criterios y cuáles restricciones?", ["Resistir 2 kilos describe cómo debe funcionar: es un criterio.", "El costo máximo y el ancho del cajón son límites del problema: son restricciones."], "Criterio: resistir 2 kilos. Restricciones: costar menos de $3.000 y caber en un cajón de 30 cm de ancho"),
    ],
    mistakes=[
        ("Escribir «necesito una repisa» como necesidad.", "Nombra la solución antes de entender qué se debe lograr.", "Escribe qué hay que lograr: «ordenar los libros para que se encuentren rápido»."),
        ("Escribir el criterio «que quede bonito».", "No se puede contar ni medir y cada persona lo entiende distinto.", "Cámbialo por algo observable, como «usa solo 2 colores»."),
    ],
    R=[
        ("¿Cómo se llama la persona que usará la solución?", "Usuario", "Es quien usa lo que se diseña."),
        ("«Cuesta menos de $2.000», ¿es una restricción o una necesidad?", "Una restricción", "El dinero disponible es un límite del problema."),
        ("¿Una necesidad bien escrita nombra el objeto de la solución o dice qué se debe lograr?", "Dice qué se debe lograr", "Nombrar el objeto cierra las opciones demasiado pronto."),
    ],
    C=[
        ("¿Cuál criterio se puede comprobar? A «sostiene 3 libros sin doblarse», B «se ve bien».", "A", "A se prueba poniendo 3 libros; B es opinión."),
        ("Un grupo escribe «necesitamos una caja con tapa». ¿Qué le falta a esa frase para ser una buena necesidad?", "Decir qué se debe lograr, sin nombrar la caja", "Está nombrando la solución."),
        ("¿Por qué anotar las restricciones antes de diseñar? A «para saber hasta dónde se puede llegar», B «para que la necesidad quede más corta».", "A", "Las restricciones delimitan lo posible."),
    ],
    A=[
        arith("Un organizador debe sostener 4 libros de 600 g cada uno. ¿Cuántos gramos como mínimo debe sostener?", "4*600", "Se multiplica la cantidad de libros por el peso de cada uno.", " g"),
        ("Restricción: ancho máximo de 40 cm. La propuesta P mide 35 cm, la Q 41 cm y la R 40 cm. ¿Cuáles cumplen?", "P y R", "35 y 40 no superan 40; 41 sí lo supera."),
        ("Reescribe con una frase de necesidad sin nombrar un objeto: «Los vecinos necesitan una luz para el pasaje». ¿Cuál la reescribe bien? A «poder ver por dónde caminar en el pasaje de noche», B «instalar una luz grande en el pasaje».", "A", "A dice qué lograr; B repite la solución."),
    ],
    Z=[
        ("Dos criterios del mismo diseño: «debe ser muy resistente» y «debe pesar menos de 200 g». El grupo nota que lo más resistente pesa 350 g. ¿Qué debe hacer?", "Decidir cuál criterio importa más o buscar otro material", "Los criterios chocan y hay que resolver la tensión con una decisión explicada."),
        ("Camila escribe como criterio «dura mucho tiempo». Elena escribe «sigue sirviendo después de 50 aperturas». ¿Cuál es mejor y por qué?", "El de Elena, porque se puede contar", "Tiene un número que se puede comprobar."),
    ],
    D=[
        arith("El presupuesto es de $6.000. Ya se gastaron $2.500 en cartón y $1.500 en cinta. ¿Cuánto dinero queda?", "6000-2500-1500", "Se restan los gastos del presupuesto total.", " pesos"),
        ("Restricciones: cuesta $4.000 o menos y mide 30 cm o menos de alto. Criterio: sostiene 5 lápices. Opción 1: $3.800, 28 cm, 5 lápices. Opción 2: $3.500, 33 cm, 6 lápices. Opción 3: $4.200, 25 cm, 5 lápices. ¿Cuál cumple todo?", "La opción 1", "La 2 pasa el alto y la 3 pasa el costo."),
    ],
    ctx=("Los útiles de arte del curso se mezclan en una caja y se pierden 6 minutos de cada clase buscándolos. Escribe usuario, necesidad sin nombrar un objeto, un criterio comprobable y una restricción.", "Usuario: el curso. Necesidad: encontrar cada útil rápidamente. Criterio: se encuentra cualquier útil en menos de 1 minuto. Restricción: usar solo cajas y cartón que ya hay en la escuela", "Reúne usuario, necesidad sin objeto, criterio con número y un límite."),
    sc=[
        ("¿Cuáles son las tres partes de una necesidad bien escrita?", "Usuario, necesidad y criterios", "Son las partes que se explican en la clase."),
        ("¿En qué se diferencia un criterio de una restricción?", "El criterio dice cómo debe ser la solución; la restricción es un límite", "Uno describe lo deseado y la otra lo posible."),
        ("¿Cómo sabes si un criterio es comprobable?", "Se puede contar, medir u observar", "Así se puede decidir si se cumple."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: el curso debe llevar 12 botellas plásticas vacías al punto de reciclaje y se le caen por el camino. Caso 2: una familia quiere dejar a la vista el calendario de la semana sin que se arrugue. Caso 3: un compañero con visión reducida lee con dificultad los carteles de la sala. Escribe el usuario, la necesidad sin nombrar un objeto, dos criterios comprobables y dos restricciones.",
        "Caso 1: usuario: el curso. Necesidad: transportar las botellas sin que se caigan. Criterios: caben las 12 botellas; no se cae ninguna en un recorrido de 20 pasos. Restricciones: gastar menos de $2.000; usar materiales que ya hay",
        ["nombra al usuario", "necesidad sin nombrar el objeto", "dos criterios comprobables", "dos restricciones claras"],
        ["ficha con usuario, necesidad, criterios y restricciones"],
        ["nombrar la solución en la necesidad", "criterios que no se pueden comprobar"],
        "Pregunta: «¿cómo contarías o medirías este criterio?». Si no sabe, pídele agregar un número o una acción.",
    ),
    reinforce="Elige un objeto de tu casa y escribe una necesidad sobre él sin nombrar un objeto nuevo.",
    extend="Escribe dos criterios que choquen entre sí en el diseño de una mochila y explica cuál elegirías primero.",
)

# ------------------------------------------------------------------ OA 01, clase 4
reg(
    OA1, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Si quieres, una persona de tu casa para comentar tus ideas.",
    use="Aprenderé a reflexionar sobre los aportes que podría hacer una solución, a prever quién puede salir perjudicado y a planificar los riesgos antes de empezar. Sirve para decidir si una solución vale la pena.",
    prior=["Sé escribir usuario, necesidad y criterios.", "Sé que una restricción es un límite.", "Sé multiplicar y sumar."],
    explain=[
        "Reflexionar sobre los aportes es preguntarse qué cambia en la vida de las personas si la solución funciona. Un aporte puede ser personal, como ahorrar tiempo o dolor; grupal, como un patio más seguro para todo el curso; o ambiental, como botar menos residuos. Conviene escribir el aporte con un número cuando se puede: «ahorra 5 minutos por día».",
        "Toda solución también puede traer un costo o un efecto no buscado. Por ejemplo, una rampa ayuda a quien usa silla de ruedas, pero puede ocupar el espacio por donde pasa otro grupo. Piensa quiénes se benefician, quiénes podrían salir perjudicados y cómo se podría reducir el perjuicio. Esta reflexión forma parte del diseño.",
        "Antes de empezar a construir también se planifica la seguridad. Para cada paso escribe el riesgo y cómo evitarlo: usar tijeras de punta roma, trabajar sobre una mesa despejada, recoger el pelo y lavarse las manos al terminar. Las herramientas con filo o con motor las usa solo una persona adulta. Un paso riesgoso se cambia por otro más seguro.",
    ],
    vocab=[("aporte", "cambio positivo que produce una solución"), ("efecto no buscado", "consecuencia que nadie planeó"), ("beneficiarse", "recibir un aporte o una ventaja"), ("perjuicio", "daño o molestia que sufre alguien"), ("riesgo", "posibilidad de que ocurra un daño")],
    worked=[
        ("Medir un aporte con un número", "Un curso pierde 5 minutos de cada clase de Educación Física buscando conos mezclados. Tiene 3 clases a la semana. Si la solución elimina la búsqueda, ¿cuántos minutos ahorra en una semana?", ["Cada clase pierde 5 minutos.", "Son 3 clases: multiplico 5 × 3."], "15 minutos a la semana"),
        ("Quién se beneficia y quién se perjudica", "El curso quiere pegar un mueble de cartón en el pasillo para guardar zapatillas. ¿A quién ayuda y a quién podría perjudicar?", ["Ayuda al curso, que ordena sus zapatillas.", "El mueble ocupa espacio del pasillo y podría estorbar a quien pasa."], "Ayuda al curso; podría estorbar a quienes circulan por el pasillo, y se reduce dejando espacio libre"),
    ],
    mistakes=[
        ("Pensar que una buena solución no puede perjudicar a nadie.", "Toda solución cambia algo y puede afectar a otras personas.", "Pregunta siempre «¿a quién podría molestar?» y busca cómo reducirlo."),
        ("Planificar la seguridad solo después de que alguien se lastima.", "El daño ya ocurrió y se pudo evitar.", "Escribe el riesgo y su prevención antes de cada paso."),
    ],
    R=[
        ("Un patio con menos pelotas perdidas, ¿es un aporte personal, grupal o ambiental?", "Grupal", "Beneficia a todo el curso."),
        ("Quien usa una solución y sale ganando, ¿se beneficia o se perjudica?", "Se beneficia", "Recibe un aporte."),
        ("¿Las herramientas con filo o con motor las usa un estudiante solo o una persona adulta?", "Una persona adulta", "Tienen riesgo de corte o de accidente."),
    ],
    C=[
        ("Un compañero dice: «Mi idea no tiene ningún efecto negativo». ¿Qué debes responder? A «piensa quiénes podrían salir perjudicados, porque toda solución cambia algo», B «tienes razón, si la idea es buena no cambia nada para nadie».", "A", "Revisar los efectos es parte del diseño."),
        ("¿Cuál aporte está escrito de forma más útil? A «sirve mucho», B «ahorra 10 minutos por clase».", "B", "B tiene un número que se puede comprobar."),
        ("¿Por qué se planifican los riesgos antes de empezar a construir?", "Para evitar accidentes en vez de lamentarlos", "Prevenir es más seguro que reparar un daño."),
    ],
    A=[
        arith("Una solución ahorra 4 minutos cada día de clases. El curso tiene clases 5 días a la semana. ¿Cuántos minutos ahorra en una semana?", "4*5", "Se multiplica el ahorro diario por los días.", " minutos"),
        arith("Un curso desecha 18 botellas plásticas cada semana. Con una solución se reutilizan 11. ¿Cuántas botellas se siguen desechando?", "18-11", "Se restan las reutilizadas del total.", " botellas"),
        ("Tarea de armado: cortar cartón grueso con un cortador. ¿Qué cambio es más seguro? A pedir que una persona adulta corte, B dejar que un estudiante use el cortador con mucho cuidado.", "A", "Las herramientas con filo las usa una persona adulta; tener cuidado no basta para que un estudiante las use."),
    ],
    Z=[
        ("Una rampa ayuda a una compañera con muletas, pero ocupa la mitad del pasillo. Opción 1: dejarla igual. Opción 2: moverla a una pared lateral donde no estorbe. ¿Cuál reduce el perjuicio sin perder el aporte?", "La opción 2", "Mantiene la ayuda y despeja el paso."),
        ("Mateo dice: «Anotar los riesgos hace perder tiempo». Elena responde: «Un accidente hace perder más tiempo». ¿Quién tiene mejor argumento?", "Elena", "Prevenir cuesta menos que atender un accidente."),
    ],
    D=[
        arith("Un curso de 30 estudiantes ahorra 3 minutos por estudiante al día gracias a un mejor orden de los materiales. ¿Cuántos minutos ahorra el curso en un día?", "30*3", "Se multiplica el ahorro por la cantidad de estudiantes.", " minutos"),
        ("Dos soluciones para el mismo problema. Solución A: ahorra 20 minutos por semana y no tiene riesgos. Solución B: ahorra 25 minutos por semana y exige usar un cortador con filo. Si el curso decide no usar herramientas con filo, ¿cuál elige?", "La solución A", "B pide una herramienta que los estudiantes no usan."),
    ],
    ctx=("Tu familia deja los zapatos a la entrada y cada día alguien tropieza con ellos. Propones un zapatero de cartón. Escribe un aporte con número, un posible perjuicio y un riesgo al armarlo con su prevención.", "Aporte: se evitan los tropiezos de varias personas cada día. Perjuicio: puede ocupar el paso en un pasillo angosto. Riesgo: cortarse con las tijeras, que se evita usando tijeras de punta roma y cortando lejos de los dedos", "Nombra un aporte, un perjuicio posible y un riesgo con su prevención."),
    sc=[
        ("¿Qué es un aporte de una solución?", "Un cambio positivo que produce", "El aporte es lo que gana el usuario."),
        ("¿Una solución puede perjudicar a alguien sin que se haya querido?", "Sí", "Existen efectos no buscados."),
        ("¿Cuándo se planifica la seguridad?", "Antes de empezar", "Así se previenen los accidentes."),
    ],
    open_task=(
        "Escoge una solución. Solución 1: una bandeja con tapas de colores para ordenar las 30 tijeras de punta roma de la sala. Solución 2: un cartel con letras grandes pegado en la puerta de la sala para quienes ven poco. Solución 3: una caja de cartón con asas para llevar 10 libros de la biblioteca de aula de un lado a otro de la sala. Escribe un aporte con un número, quién se beneficia, quién podría salir perjudicado y una forma de reducirlo, y un riesgo al construirla con su prevención.",
        "Solución 3: aporte: se llevan 10 libros en un viaje en vez de 5 viajes con 2 libros cada uno. Se beneficia el curso. Podría perjudicar a quien camina por el pasillo; se reduce guardando la caja en un lugar que no estorbe. Riesgo: cortarse al cortar cartón; se evita usando tijera de punta roma y cortando lejos de los dedos",
        ["aporte con un número", "nombra quién se beneficia y quién podría perjudicarse", "propone cómo reducir el perjuicio", "riesgo con prevención segura"],
        ["hoja con aporte, perjuicio y riesgo"],
        ["decir que no hay ningún perjuicio", "riesgo sin forma de evitarlo"],
        "Pregunta: «¿a quién podría molestar tu solución?». Si dice que a nadie, pídele pensar en las personas que usan el mismo lugar.",
    ),
    reinforce="Cuenta cuántos minutos pierdes al día por algo desordenado en tu casa y escribe cómo cambiaría con una solución.",
    extend="Elige una solución que conozcas y escribe un aporte y un efecto no buscado que haya tenido.",
)

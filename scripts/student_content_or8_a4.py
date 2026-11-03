"""Cuaderno del estudiante, 8.º básico Orientación: OA 07 (intereses compartidos, colaboración y metas comunes) y OA 08 (acuerdos y participación democrática del curso)."""
from __future__ import annotations

from student_content_or8_a import M, T, W, lesson
from student_lessons import arith, ex

OA7, OA8 = "OR08 OA 07", "OR08 OA 08"

# ================================================================ OA 07
lesson(
    OA7, 1,
    "Una hoja y un lápiz. La encuesta de ejemplo del 8.º A y todos los datos están escritos en los ejercicios. Los números son de ejemplo, no reales.",
    "Aprenderé a reconocer intereses, inquietudes, problemas o necesidades que comparte mi grupo y a convertirlos en una meta común. Sirve para trabajar en equipo con un propósito claro.",
    ["Conozco mis intereses y capacidades.", "Sé que cada persona aporta de manera distinta."],
    [
        "Un grupo de pertenencia es aquel al que sientes que perteneces: tu curso, un taller, un equipo deportivo, una banda. Los integrantes comparten cosas. Un interés es lo que les gusta. Una inquietud es algo que les preocupa. Un problema es algo que les causa dificultades. Una necesidad es algo que les hace falta. Reconocerlos permite que el grupo avance unido.",
        "Para descubrir lo que comparte un grupo se puede hacer una encuesta breve: cada persona responde y se cuentan las respuestas. Una respuesta compartida por muchos señala algo importante. Luego se escribe una meta común: algo que el grupo quiere lograr junto, por ejemplo «decorar la sala antes del 30 de abril». Una buena meta es clara, posible y tiene un plazo.",
        "El trabajo en equipo valora los aportes de todos. Algunos aportan ideas, otros organizan, dibujan, buscan datos o cuidan que todos puedan hablar. Un equipo funciona mejor cuando reconoce el aporte de cada miembro y no solo el de quien habla más. Los intereses distintos no son un obstáculo: pueden enriquecer la meta.",
    ],
    [("grupo de pertenencia", "grupo al que una persona siente que pertenece, como su curso"), ("inquietud", "algo que preocupa a una persona o grupo"), ("necesidad", "algo que le hace falta a una persona o grupo"), ("meta común", "algo que un grupo quiere lograr junto"), ("aporte", "lo que cada integrante da al equipo")],
    [
        W("Elegir la respuesta más compartida", "Encuesta de ejemplo del 8.º A (30 estudiantes). Interés principal: deporte 12, música 10, arte 8. ¿Cuál es el más compartido?", ["Compara 12, 10 y 8.", "El mayor es 12.", "Es el deporte."], "El deporte, con 12 respuestas"),
        W("Formular una meta común", "El 8.º A comparte la inquietud de que la sala está desordenada. Escribe una meta común con plazo.", ["Dice qué se quiere lograr: sala ordenada.", "Dice cómo es posible: turnos de orden.", "Incluye un plazo: hasta fin de mes."], "«Mantener la sala ordenada con turnos de orden hasta fin de mes»"),
    ],
    [
        M("Creer que un interés compartido por pocos no vale.", "Se mira solo la mayoría.", "Un grupo puede tener varios intereses y metas."),
        M("Pensar que una meta como «ser mejores» es suficiente.", "Es vaga y sin plazo.", "Una buena meta es clara, posible y con plazo."),
    ],
    R=[
        ex("Lo que le gusta a un grupo, ¿es un interés o una necesidad?", "Un interés", "Habla de gustos."),
        ex("Algo que le hace falta a un grupo, ¿es una necesidad o un interés?", "Una necesidad", "Se refiere a lo que falta."),
        ex("Tu curso, ¿es un grupo de pertenencia, sí o no?", "Sí", "Es un grupo al que perteneces."),
    ],
    U=[
        ex("¿Qué tiene una buena meta común? A) Es clara, posible y con plazo. B) Es grande y sin fecha.", "A", "Esas son sus características."),
        ex("Una encuesta ayuda a ¿conocer lo que comparte el grupo o a elegir un líder?", "A conocer lo que comparte el grupo", "Cuenta respuestas de todos."),
        ex("Dos estudiantes tienen intereses distintos, ¿pueden trabajar juntos, sí o no?", "Sí", "Los intereses distintos pueden enriquecer la meta."),
    ],
    A=[
        ex("Encuesta de ejemplo (30 personas), problema principal: ruido 11, desorden 9, falta de materiales 6, otros 4. ¿Cuál es el problema más compartido?", "El ruido", "Tiene el mayor número de respuestas, 11."),
        ex("¿Qué meta común es mejor? A) «Juntar 40 libros para la biblioteca antes del 15 de junio». B) «Ser un curso excelente».", "A", "Es clara, medible y con plazo."),
        ex("Un curso tiene dos intereses fuertes: música y fútbol. ¿Qué meta podría integrarlos?", "Organizar una tarde de música y juegos", "Une ambos intereses."),
    ],
    Z=[
        ex("¿Por qué es importante contar las respuestas de la encuesta en vez de decidir al azar?", "Porque muestra qué comparte el grupo", "Los datos reflejan a todos, no solo a unos pocos."),
        ex("Un compañero dice: «Mi aporte es chico, no vale». ¿Qué le responderías?", "Que cada aporte suma al equipo", "El trabajo en equipo valora todos los aportes."),
    ],
    D=[
        arith("En la encuesta de ejemplo, 30 estudiantes eligieron: deporte 12, música 9 y arte 5. El resto no respondió. ¿Cuántos no respondieron?", "30-12-9-5", "Al total se le restan las respuestas dadas."),
        arith("Para la meta de juntar 40 libros, el curso se organiza en 8 grupos. ¿Cuántos libros debe juntar cada grupo?", "40//8", "Se divide el total entre los grupos."),
    ],
    context=[ex("El delegado de 8.º B comenta que todos hablan de lo cansador que es el patio sin sombra. ¿Cómo se puede convertir esa inquietud en meta común?", "Proponer juntos una solución, como pedir toldos con una fecha", "Convierte la inquietud en una meta clara y con plazo.")],
    selfcheck=[ex("En Orientación: ¿un grupo de pertenencia comparte intereses?", "Sí", "Los integrantes tienen cosas en común."), ex("¿Una buena meta tiene plazo?", "Sí", "Permite saber si se logró."), ex("¿Solo aporta quien habla más?", "No", "Cada integrante aporta de manera distinta.")],
    task=T("Lee la encuesta de ejemplo del 8.º C (28 estudiantes): problema principal: pocas actividades en recreo 10, ruido 8, desorden 6, otros 4. Interés principal: baile 9, ajedrez 7, fútbol 12. Escribe: el problema más compartido, el interés más compartido y una meta común clara, posible y con plazo que los relacione.", "Problema: pocas actividades en recreo (10). Interés: fútbol (12). Meta: organizar un campeonato de fútbol en los recreos desde el 5 de mayo hasta fin de mes.", ["identifica el problema y el interés más compartidos", "la meta es clara y posible", "tiene plazo", "relaciona los datos de la encuesta"], ["texto escrito"], ["meta vaga", "no usar los datos"], "Reconoce la lectura de datos y pregunta cómo se integrarían los otros intereses."),
    reinforce="Escribe un interés, una inquietud y una necesidad de un grupo inventado.",
    extend="Explica por qué los intereses distintos pueden enriquecer una meta común.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. El caso del equipo del afiche de 8.º y el registro de tareas están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a distinguir hechos, emociones, derechos y límites en el trabajo en equipo. Sirve para valorar los aportes y cuidar que nadie quede sobrecargado ni excluido.",
    ["Sé qué es una meta común.", "Sé que cada integrante aporta."],
    [
        "En un equipo hay hechos, emociones, derechos y límites. Un hecho es lo que ocurrió y se puede comprobar: «María investigó tres fuentes». Una emoción es lo que sienten los integrantes: orgullo, enojo, vergüenza, cansancio. Un derecho es lo que cada integrante merece: ser escuchado, aportar y recibir reconocimiento. Un límite es lo que el equipo no acepta: gritar, ridiculizar, cargar a una sola persona.",
        "Para valorar los aportes conviene registrar qué hizo cada uno, sin competir. Un registro permite ver si el trabajo se reparte de forma justa. Si una persona hace mucho más que las otras, hay un desequilibrio y el equipo debe conversar. Si alguien no participa, primero se pregunta por qué: puede haber dudas, miedo o falta de tiempo, y no siempre es flojera.",
        "Los desacuerdos son normales. Lo importante es expresar las ideas con respeto, escuchar a los demás y llegar a acuerdos. Cada integrante tiene derecho a opinar, a pedir ayuda y a que se reconozca su trabajo. También tiene el deber de cumplir lo que prometió.",
    ],
    [("equipo", "grupo de personas que trabajan juntas por una meta"), ("registro", "anotación de lo que hizo cada integrante"), ("desequilibrio", "reparto desigual del trabajo"), ("reconocimiento", "valorar y agradecer el aporte de alguien"), ("deber", "compromiso que cada integrante debe cumplir")],
    [
        W("Detectar un desequilibrio", "En un trabajo de 12 tareas, Lucía hizo 7, Pablo 3 y Camila 2. ¿Hay desequilibrio?", ["Lucía hizo más de la mitad.", "Las otras hicieron mucho menos.", "Hay desequilibrio."], "Sí: Lucía hizo 7 de 12"),
        W("Separar hecho y emoción", "Pablo dice: «Estoy enojado porque no me toman en cuenta». ¿Cuál es la emoción y qué hecho debería comprobarse?", ["La emoción es enojo.", "El hecho: ¿realmente no lo tomaron en cuenta?", "Se revisa el registro de lo que hizo."], "Emoción: enojo. Hecho por comprobar: si lo tomaron en cuenta"),
    ],
    [
        M("Creer que quien no participa es flojo.", "Se supone sin preguntar.", "Primero pregunta por qué; puede haber miedo o dudas."),
        M("Pensar que si alguien hace más, es porque quiere.", "Se ignora el desequilibrio.", "Conversa para repartir de forma justa."),
    ],
    R=[
        ex("«Ana investigó tres fuentes» ¿es un hecho o una emoción?", "Un hecho", "Se puede comprobar."),
        ex("Sentir enojo porque no te escuchan, ¿es una emoción o un derecho?", "Una emoción", "Es lo que siente."),
        ex("Tener derecho a opinar en el equipo, ¿es un derecho o un límite?", "Un derecho", "Es algo que cada integrante merece."),
    ],
    U=[
        ex("¿Por qué conviene registrar quién hizo qué? A) Para ver si el trabajo se reparte de forma justa. B) Para castigar a alguien.", "A", "El registro muestra el reparto."),
        ex("Si una persona del equipo no participa, ¿qué conviene hacer primero?", "Preguntarle por qué", "Puede haber dudas, miedo o falta de tiempo."),
        ex("Gritar a un integrante, ¿es un límite que el equipo debe poner, sí o no?", "Sí", "No se acepta el maltrato."),
    ],
    A=[
        ex("Tareas: Marta 5, Beto 5, Lía 4, Ian 2 (total 16). ¿Quién hizo menos?", "Ian", "Con 2 tareas es quien menos hizo."),
        ex("Hugo se siente sobrecargado porque hizo la mitad del trabajo. ¿Qué derecho puede pedir? A) Que se reparta mejor. B) Que los demás no hablen.", "A", "Tiene derecho a un reparto justo."),
        ex("Un equipo se ríe de la idea de Camila. ¿Qué límite corresponde poner?", "No ridiculizar las ideas", "Todos tienen derecho a opinar sin burlas."),
    ],
    Z=[
        ex("¿Por qué el reconocimiento de los aportes ayuda al equipo?", "Porque motiva y hace sentir valorados a todos", "Reconocer el trabajo mejora la colaboración."),
        ex("Un equipo dice: «El que hizo más manda». ¿Qué principio no respeta?", "El derecho de todos a opinar", "Todos aportan y tienen voz."),
    ],
    D=[
        arith("En un trabajo de 20 tareas, Ema hizo 8 y Rafa 7. Un tercero hizo el resto. ¿Cuántas hizo el tercero?", "20-8-7", "Al total se le restan las tareas de los otros dos."),
        arith("Un equipo de 5 personas se reparte 15 tareas por igual. ¿Cuántas tareas hace cada uno?", "15//5", "Se divide el total entre los integrantes."),
    ],
    context=[ex("En un equipo de ciencias, Tomás nunca entrega su parte y los demás se enojan. Antes de acusarlo, ¿qué deberían hacer?", "Preguntarle qué le pasa", "Puede haber una dificultad detrás.")],
    selfcheck=[ex("En Orientación: ¿todos los integrantes tienen derecho a opinar?", "Sí", "Es un derecho en el equipo."), ex("¿Un registro ayuda a repartir de forma justa?", "Sí", "Muestra el trabajo de cada uno."), ex("¿Está bien ridiculizar una idea?", "No", "Rompe un límite de respeto.")],
    task=T("Lee el registro de ejemplo de un trabajo de 14 tareas: Noelia 6, Ismael 5, Sofía 2, Joaquín 1. Escribe un cuadro: un hecho, una emoción posible, un derecho y un límite. Agrega una propuesta de reparto más justo para la próxima vez.", "Hecho: Noelia e Ismael hicieron 11 de 14 tareas. Emoción: cansancio de ellos y vergüenza de Joaquín. Derecho: reparto justo y ser escuchados. Límite: no acusar sin preguntar. Propuesta: cada uno 3 o 4 tareas.", ["distingue hecho, emoción, derecho y límite", "usa los datos del registro", "propone un reparto justo", "no culpa a nadie"], ["cuadro escrito"], ["culpar a alguien sin preguntar", "no usar el registro"], "Reconoce el uso de datos y pregunta cómo conversarían con Joaquín."),
    reinforce="Escribe un hecho, una emoción, un derecho y un límite de un equipo de cuento.",
    extend="Explica por qué conviene preguntar a quien no participa antes de acusarlo.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. El proyecto «Feria de ciencias» y las opciones de reparto están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a comparar formas de repartir el trabajo en un equipo y sus consecuencias. Sirve para elegir una que valore los aportes y ayude a lograr la meta común.",
    ["Sé que cada integrante aporta.", "Sé detectar un desequilibrio."],
    [
        "Para repartir el trabajo hay varias opciones. Una persona hace todo: es rápido, pero la sobrecarga y los demás no aprenden. Se sortean las tareas: es justo en el azar, pero puede dar una tarea que una persona no sabe hacer. Se reparte según las fortalezas: cada uno hace lo que mejor sabe, y el trabajo suele salir bien, pero algunos no practican lo que les cuesta. Se rota: cada vez alguien distinto hace cada tarea, lo que reparte el esfuerzo y permite aprender.",
        "Para comparar, mira las consecuencias: ¿se cumple la meta?, ¿se valora el aporte de todos?, ¿se aprende?, ¿hay sobrecarga? Muchas veces una mezcla funciona mejor: se asignan tareas según fortalezas y se pide a cada uno intentar una tarea nueva con apoyo.",
        "Antes de repartir, el equipo debe escribir su meta, listar las tareas y estimar cuánto tiempo toma cada una. Así se evita que alguien se quede con demasiado. Y después de repartir, se acuerda cuándo revisarán el avance. El trabajo en equipo mejora cuando todos conocen sus tareas y los plazos.",
    ],
    [("sobrecarga", "exceso de trabajo en una persona"), ("sorteo", "elegir al azar"), ("fortaleza", "cosa que una persona hace bien"), ("rotar", "cambiar de turno o de tarea entre integrantes"), ("estimar", "calcular de forma aproximada")],
    [
        W("Comparar dos repartos", "Opción 1: Ana hace todo en 3 horas. Opción 2: cuatro personas hacen una tarea cada una en 1 hora. ¿Cuál valora el aporte de todos?", ["En la opción 1 Ana hace todo.", "En la 2 cada uno aporta.", "Todos se involucran."], "La opción 2"),
        W("Estimar tiempos", "Un equipo tiene tres tareas: investigar (2 horas), dibujar (3 horas) y escribir (1 hora). ¿Cuántas horas de trabajo hay en total?", ["Suma 2 + 3 + 1.", "El total es 6.", "Se reparte entre integrantes."], "6 horas"),
    ],
    [
        M("Elegir siempre al más rápido para todas las tareas.", "Se prioriza la velocidad.", "También cuenta aprender y valorar los aportes."),
        M("Creer que el sorteo es siempre la opción más justa.", "Se ignoran las fortalezas.", "Puedes combinar sorteo con fortalezas."),
    ],
    R=[
        ex("Hacer cada vez una tarea distinta, ¿es rotar o sortear?", "Rotar", "Cambia el turno entre integrantes."),
        ex("Una persona que hace todo, ¿está sobrecargada, sí o no?", "Sí", "Tiene exceso de trabajo."),
        ex("Repartir según lo que cada uno hace mejor, ¿usa las fortalezas, sí o no?", "Sí", "Aprovecha lo que cada uno sabe."),
    ],
    U=[
        ex("¿Qué desventaja tiene que una persona haga todo? A) Sobrecarga y los demás no aprenden. B) Es demasiado justo.", "A", "No reparte el esfuerzo ni el aprendizaje."),
        ex("¿Por qué conviene estimar el tiempo de cada tarea antes de repartir?", "Para evitar que alguien se quede con demasiado", "Permite un reparto equilibrado."),
        ex("Una mezcla de fortalezas y tareas nuevas, ¿puede ser una buena opción, sí o no?", "Sí", "Se logra la meta y se aprende."),
    ],
    A=[
        ex("Cuatro tareas: investigar (2 h), dibujar (3 h), escribir (2 h), presentar (1 h). El equipo tiene 4 personas y reparte una tarea por persona. ¿Quién tiene la tarea más larga?", "Quien dibuja", "Dibujar toma 3 horas, la más larga."),
        ex("Un equipo sortea las tareas y a Pía le toca presentar, que le da pánico. ¿Qué podría hacer el equipo? A) Cambiarle la tarea o apoyarla. B) Obligarla sin ayuda.", "A", "Ofrece apoyo o ajusta el reparto."),
        ex("El equipo decide rotar la tarea de presentar cada semana. ¿Qué beneficio tiene?", "Todos practican y comparten el esfuerzo", "La rotación reparte las oportunidades."),
    ],
    Z=[
        ex("¿Por qué combinar fortalezas y tareas nuevas ayuda al aprendizaje?", "Porque se logra la meta y todos prueban cosas nuevas", "Se cuida el resultado y el crecimiento de cada uno."),
        ex("Un joven dice: «Mejor que lo haga el que sabe y listo». ¿Qué ventaja y qué desventaja tiene su idea?", "Rapidez, pero los demás no aprenden", "Prioriza el resultado y descuida el aprendizaje."),
    ],
    D=[
        arith("Un equipo de 4 personas tiene tareas de 2, 3, 2 y 1 horas. ¿Cuántas horas suman?", "2+3+2+1", "Se suman las horas de cada tarea."),
        arith("Si ese trabajo de 8 horas se reparte por igual entre 4 personas, ¿cuántas horas hace cada una?", "8//4", "Se divide el total entre los integrantes."),
    ],
    context=[ex("Para una feria de ciencias, el curso de 36 estudiantes debe armar 6 puestos. ¿Cuántos estudiantes trabajan en cada puesto si se reparten por igual?", "6", "36 dividido en 6 puestos da 6 por puesto.", calc="36//6")],
    selfcheck=[ex("En Orientación: ¿rotar reparte el esfuerzo?", "Sí", "Cada uno hace tareas distintas."), ex("¿Conviene estimar el tiempo antes de repartir?", "Sí", "Evita sobrecargas en el equipo."), ex("¿Una sola persona haciendo todo valora el aporte de todos?", "No", "No reparte el trabajo.")],
    task=T("Lee el caso inventado: el equipo de Valentina, Tomás, Ema y Nico debe armar un video de 3 minutos para el curso en una semana. Tareas: guion (3 h), grabación (4 h), edición (4 h) y música (1 h). Escribe una tabla con tres formas de repartir (una persona hace todo, por fortalezas, rotación), una consecuencia de cada una y elige la mejor justificando.", "Una persona: 12 h para uno, sobrecarga. Fortalezas: Valentina guion, Tomás grabación, Ema edición, Nico música; rápido, pero Nico hace poco. Rotación: cambia el turno cada semana; reparte esfuerzo. Elijo fortalezas con apoyo para Nico en edición.", ["compara tres formas", "anota consecuencias", "elige una y justifica", "usa los datos de las tareas"], ["tabla escrita"], ["no ver la sobrecarga", "ignorar el aprendizaje"], "Reconoce la comparación y pregunta cuándo revisarían el avance."),
    reinforce="Escribe dos formas de repartir un trabajo y una ventaja de cada una.",
    extend="Explica por qué estimar tiempos ayuda a repartir mejor.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. Los problemas del equipo y las opciones están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a elegir una acción segura y respetuosa cuando un equipo tiene problemas: alguien no participa, alguien domina o hay presión para hacer algo indebido. Sirve para sostener la meta común sin dañar a nadie.",
    ["Sé comparar formas de repartir el trabajo.", "Sé que debo respetar a todos."],
    [
        "Un equipo puede tener problemas. Alguien no participa: se le pregunta qué le pasa y se le ofrece una tarea posible. Alguien domina y no deja hablar: se acuerdan turnos de palabra. Hay desacuerdos: se escucha a todos y se busca una solución. Si algo no se resuelve, se pide ayuda al profesor jefe o a la persona que guía el trabajo.",
        "Hay una situación distinta: la presión para hacer algo indebido, como copiar de internet sin citar, mentir sobre quién hizo qué o excluir a un compañero. Una acción segura es negarse con respeto, proponer otra manera y, si insisten, avisar a una persona adulta. Cuidar la honestidad del equipo es parte de trabajar bien.",
        "Una acción segura en el equipo respeta a todos, ayuda a lograr la meta, y no pone a nadie en riesgo ni lo humilla. Usa frases claras: «Necesitamos que cada uno cumpla su parte», «Vamos por turnos», «No podemos copiar, hagámoslo con nuestras palabras». Y reconoce lo bueno: agradecer también motiva.",
    ],
    [("turnos de palabra", "orden acordado para que todos puedan hablar"), ("indebido", "que no corresponde o no es correcto"), ("honestidad", "actuar con verdad y sin engañar"), ("citar", "indicar de dónde viene una idea o texto"), ("acuerdo", "decisión que el equipo acepta")],
    [
        W("Elegir ante quien no participa", "Mateo no entrega su parte hace dos semanas. ¿Qué es lo más adecuado primero?", ["Preguntarle qué le pasa.", "Ofrecerle una tarea posible.", "Pedir ayuda adulta si no cambia."], "Preguntarle qué le pasa y ofrecerle una tarea posible"),
        W("Responder a una presión", "Un integrante propone copiar un texto de internet. ¿Qué hace el equipo?", ["Se niega con respeto.", "Propone redactar con sus palabras y citar.", "Avisa a un adulto si insisten."], "Negarse con respeto, redactar con sus palabras y citar"),
    ],
    [
        M("Callar para no generar conflicto cuando proponen copiar.", "Se prefiere agradar.", "Niégate con respeto y propone otra opción."),
        M("Acusar públicamente a quien no participa.", "Se busca culpar.", "Pregunta primero y ofrece una tarea posible."),
    ],
    R=[
        ex("Si alguien no participa, ¿le preguntas qué le pasa o lo acusas?", "Le preguntas qué le pasa", "Puede haber una dificultad."),
        ex("Copiar sin citar, ¿es honesto o indebido?", "Indebido", "Engaña sobre quién hizo el trabajo."),
        ex("Acordar turnos de palabra, ¿ayuda a que todos hablen, sí o no?", "Sí", "Evita que alguien domine."),
    ],
    U=[
        ex("¿Qué haces si alguien domina la conversación? A) Proponer turnos de palabra. B) Callarte.", "A", "Garantiza que todos puedan hablar."),
        ex("Si el equipo insiste en hacer algo indebido, ¿a quién se avisa?", "A una persona adulta", "Puede guiar y proteger la honestidad."),
        ex("Agradecer el aporte de alguien, ¿motiva al equipo, sí o no?", "Sí", "Reconocer fortalece la colaboración."),
    ],
    A=[
        ex("Cuatro respuestas ante un integrante que no entrega: 1) «Eres un flojo»; 2) «¿Qué te complica? Te propongo hacer la parte de dibujos»; 3) hacer su parte sin decir nada; 4) sacarlo del grupo. ¿Cuál es la más adecuada?", "La 2", "Pregunta y ofrece una tarea posible."),
        ex("Dos integrantes quieren hablar a la vez. ¿Qué acuerdo sirve? A) Levantar la mano y hablar por turnos. B) Que hable el más fuerte.", "A", "Los turnos respetan a todos."),
        ex("Un compañero propone decir que hizo más de lo que hizo. ¿Qué principio rompe?", "La honestidad", "Engaña sobre el reparto real."),
    ],
    Z=[
        ex("¿Por qué acusar en público a quien no participa puede empeorar el problema?", "Porque lo avergüenza y puede alejarse más", "La presión pública rara vez motiva."),
        ex("¿Por qué negarse a copiar también cuida al equipo?", "Porque evita sanciones y protege su aprendizaje", "La honestidad evita problemas y permite aprender."),
    ],
    D=[
        arith("En un equipo de 6, 2 no han entregado su parte de 12 tareas. Si cada uno debía hacer 2 tareas, ¿cuántas tareas faltan?", "2*2", "Se multiplican los integrantes que no entregaron por sus tareas."),
        arith("En un curso hay 7 equipos de trabajo y 5 tuvieron problemas con la entrega. ¿Cuántos no tuvieron problemas?", "7-5", "Al total de equipos se le restan los que tuvieron problemas."),
    ],
    context=[ex("Un grupo debe presentar mañana y falta la mitad del trabajo. Camilo propone copiar. Rocío cree que no. ¿Qué acción segura puede proponer Rocío?", "Pedir más plazo al profesor y repartir lo que falta", "Mantiene la honestidad y busca una solución viable.")],
    selfcheck=[ex("En Orientación: ¿se pregunta primero a quien no participa?", "Sí", "Puede haber una dificultad."), ex("¿Copiar sin citar es honesto?", "No", "Eso engaña a otros."), ex("¿Se puede pedir ayuda al profesor jefe?", "Sí", "Es una opción si no se resuelve.")],
    task=T("Lee los tres problemas inventados de un equipo: (a) Sofía no responde en el chat del grupo; (b) Joaquín habla todo el tiempo y no deja opinar; (c) Pablo propone copiar un trabajo de otro curso. Para cada uno escribe una acción segura con la frase exacta que dirías y cuándo pedirías ayuda a un adulto.", "(a) «Sofía, ¿qué te complica? ¿Te sirve hacer los dibujos?»; adulto si sigue sin responder. (b) «Hagamos turnos de palabra»; adulto si no lo respeta. (c) «No podemos copiar, redactemos con nuestras palabras»; adulto si insisten.", ["completa los tres problemas", "las frases son respetuosas", "indica cuándo pedir ayuda", "no humilla a nadie"], ["tabla escrita"], ["acusar en público", "aceptar copiar"], "Valora las frases y pregunta cómo agradecerían los avances."),
    reinforce="Escribe una frase respetuosa para pedirle a un compañero que cumpla su parte.",
    extend="Explica por qué la honestidad también es parte del trabajo en equipo.",
)

lesson(
    OA7, 5,
    "Una hoja y un lápiz. La reunión de ejemplo, el acta y las frases están escritas en los ejercicios. Todo es inventado.",
    "Aprenderé a conducir una reunión de equipo, a pedir y ofrecer ayuda y a reconocer los aportes. Sirve para comunicar bien y mantener la colaboración hacia la meta común.",
    ["Sé repartir tareas y poner límites.", "Sé que el reconocimiento motiva."],
    [
        "Una reunión de equipo breve tiene cuatro momentos: saludar y recordar la meta; revisar el avance (qué se hizo y qué falta); decidir los próximos pasos (quién, qué y para cuándo); y cerrar reconociendo aportes. Alguien registra lo acordado en un acta: un resumen escrito con las decisiones. Así nadie tiene que recordar de memoria.",
        "Para comunicar bien en un equipo se usan frases claras. Para pedir ayuda: «Me cuesta esta parte, ¿me ayudas con…?». Para ofrecer ayuda: «Terminé mi parte, ¿necesitas apoyo?». Para reconocer: «Gracias por reunir los datos, nos sirvió mucho». Para dar una crítica útil: «Esta parte podría quedar más clara si…». Evita las frases que atacan a la persona.",
        "Si el equipo se bloquea, una persona adulta puede orientar. Pedir ayuda a tiempo evita que el problema crezca. Y cuando la meta se cumple, conviene celebrar: reconocer lo que cada uno aportó refuerza el sentido de equipo.",
    ],
    [("acta", "resumen escrito de lo que se acordó en una reunión"), ("avance", "parte de la tarea que ya se hizo"), ("crítica útil", "comentario que ayuda a mejorar sin atacar"), ("próximo paso", "acción concreta que sigue"), ("celebrar", "reconocer con alegría un logro")],
    [
        W("Escribir un acta", "En la reunión se acordó que Ema escribe el guion el jueves y Nico busca imágenes el viernes. ¿Cómo queda el acta?", ["Anota quién.", "Anota qué.", "Anota cuándo."], "«Ema: guion, jueves. Nico: imágenes, viernes»"),
        W("Dar una crítica útil", "El texto de Lía es largo y confuso. ¿Qué frase es útil?", ["No ataca a la persona.", "Dice qué mejorar.", "Propone cómo."], "«Esta parte podría quedar más clara si usamos frases más cortas»"),
    ],
    [
        M("Hacer reuniones sin registrar los acuerdos.", "Se confía en la memoria.", "Anota un acta con quién, qué y cuándo."),
        M("Dar críticas como «esto está malísimo».", "Se ataca el trabajo y a la persona.", "Di qué mejorar y cómo."),
    ],
    R=[
        ex("Un acta, ¿resume lo acordado o es un chiste del grupo?", "Resume lo acordado", "Registra las decisiones."),
        ex("«Gracias por reunir los datos» ¿es una frase de reconocimiento, sí o no?", "Sí", "Valora un aporte."),
        ex("Pedir ayuda a tiempo, ¿evita que el problema crezca, sí o no?", "Sí", "Se resuelve antes."),
    ],
    U=[
        ex("¿Qué debe tener un próximo paso? A) Quién, qué y para cuándo. B) Solo un deseo.", "A", "Para poder cumplirse."),
        ex("¿Cuál es una crítica útil: «Esto es horrible» o «Esta parte quedaría mejor con un ejemplo»?", "«Esta parte quedaría mejor con un ejemplo»", "Dice qué mejorar."),
        ex("Cerrar la reunión reconociendo aportes, ¿refuerza el sentido de equipo, sí o no?", "Sí", "Valora el trabajo de cada integrante."),
    ],
    A=[
        ex("Acta: Ema guion jueves, Nico imágenes viernes, Sofía música sábado. ¿Cuántas tareas hay?", "3", "Hay tres tareas anotadas con responsable y día."),
        ex("Pía no entiende cómo editar. ¿Qué frase sirve para pedir ayuda? A) «Me cuesta editar, ¿me ayudas?». B) «No sirvo para nada».", "A", "Dice qué necesita sin descalificarse."),
        ex("Beto terminó antes que los demás. ¿Qué puede decir?", "«Terminé mi parte, ¿necesitas apoyo?»", "Ofrece ayuda concreta."),
    ],
    Z=[
        ex("¿Por qué el acta evita malentendidos?", "Porque deja por escrito quién, qué y cuándo", "Todos pueden revisar lo acordado."),
        ex("Un joven dice: «Mejor no pido ayuda para que no piensen que soy torpe». ¿Qué le responderías?", "Que pedir ayuda es parte de trabajar en equipo", "Todos necesitan apoyo en algo."),
    ],
    D=[
        arith("Una reunión de 40 minutos se divide en 4 momentos iguales. ¿Cuántos minutos dura cada uno?", "40//4", "Se divide el total entre los momentos."),
        arith("El equipo acordó 3 tareas por semana durante 4 semanas. ¿Cuántas tareas acordó en total?", "3*4", "Se multiplican las tareas por las semanas."),
    ],
    context=[ex("En el acta del 8.º B dice «hacer el afiche». ¿Qué le falta para ser un buen próximo paso?", "Quién lo hace y para cuándo", "Debe tener responsable y plazo.")],
    selfcheck=[ex("En Orientación: ¿un acta registra quién, qué y cuándo?", "Sí", "Es su función."), ex("¿Una crítica útil ataca a la persona?", "No", "Dice qué mejorar."), ex("¿Conviene reconocer aportes?", "Sí", "Motiva al equipo.")],
    task=T("Lee el caso inventado: el equipo de Ámbar, Ismael y Rosario debe organizar una colecta de útiles escolares. Escribe: (1) los cuatro momentos de una reunión de 30 minutos con su tiempo; (2) un acta con tres próximos pasos (quién, qué y cuándo); (3) una frase para pedir ayuda, una para ofrecer ayuda y una para reconocer.", "Momentos: saludo y meta 5 min; avance 10 min; próximos pasos 10 min; cierre y reconocimiento 5 min. Acta: Ámbar, afiche, miércoles; Ismael, lista de útiles, jueves; Rosario, caja de recolección, viernes. Frases: «¿Me ayudas con la lista?», «¿Necesitas apoyo?», «Gracias, el afiche quedó claro».", ["cuatro momentos con tiempos", "acta con quién, qué y cuándo", "tres frases adecuadas", "tono respetuoso"], ["texto escrito"], ["acta sin responsables", "frases que atacan"], "Reconoce la estructura y pregunta cuándo revisarán el avance."),
    reinforce="Escribe una frase de reconocimiento y una de ayuda para un compañero de un equipo de cuento.",
    extend="Explica por qué una reunión necesita un acta.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. El caso del 8.º A, que debe decidir cómo usar $60.000 del curso, y todos los datos están escritos en los ejercicios. El curso y las cifras son inventados.",
    "Aprenderé qué son los espacios de participación del curso (Consejo de Curso, asamblea y reuniones de directiva) y para qué sirven. Sirve para tomar decisiones entre todos y de manera democrática.",
    ["Sé qué es una meta común.", "Sé que todos tienen derecho a opinar."],
    [
        "La democracia es una forma de decidir en que todas las personas participan y sus opiniones cuentan. En el curso, la participación ocurre en espacios organizados. El Consejo de Curso es la reunión semanal o periódica donde el curso conversa y decide asuntos propios. Una asamblea es una reunión de todos los integrantes para decidir algo importante. La directiva del curso la forman los representantes elegidos por sus compañeros, como presidente o presidenta, secretario o secretaria y tesorero o tesorera.",
        "Cada espacio tiene un propósito. En el Consejo se plantean propuestas, se debate y se llega a acuerdos. En una asamblea se decide algo importante con la participación de todos. La directiva organiza las reuniones, registra los acuerdos y representa al curso. Los representantes no mandan: sirven al curso y deben rendir cuentas.",
        "Participar es un derecho de hombres y mujeres por igual. Significa informarse, opinar con respeto, escuchar otras opiniones y cumplir los acuerdos. Cuando se decide en democracia, no siempre se obtiene lo que cada uno quería, pero todos tuvieron la oportunidad de participar.",
    ],
    [("democracia", "forma de decidir en que todos participan y sus opiniones cuentan"), ("Consejo de Curso", "reunión periódica del curso para conversar y decidir"), ("asamblea", "reunión de todos los integrantes para decidir algo"), ("directiva", "representantes elegidos por el curso"), ("representante", "persona elegida para actuar en nombre de otros")],
    [
        W("Elegir el espacio", "El 8.º A debe decidir cómo usar $60.000 del curso. ¿Qué espacio es adecuado?", ["Es una decisión importante para todos.", "Participan todos los estudiantes.", "Una asamblea o el Consejo de Curso sirven."], "El Consejo de Curso o una asamblea"),
        W("Identificar roles", "La directiva anota los acuerdos de la reunión. ¿Qué cargo cumple esa función?", ["Registrar acuerdos es escribir.", "Eso hace el secretario o secretaria.", "Es el cargo de secretaría."], "El secretario o la secretaria"),
    ],
    [
        M("Creer que el presidente o la presidenta decide por todos.", "Se confunde representar con mandar.", "Los representantes sirven al curso y respetan los acuerdos."),
        M("Pensar que en democracia gana siempre lo que quiero.", "Se olvidan las otras opiniones.", "Todos participan y se aceptan los acuerdos."),
    ],
    R=[
        ex("El Consejo de Curso, ¿es un espacio de participación, sí o no?", "Sí", "Es una reunión donde se conversa y se decide."),
        ex("La directiva, ¿está formada por representantes elegidos, sí o no?", "Sí", "Los elige el curso."),
        ex("Participar, ¿es un derecho de hombres y mujeres por igual, sí o no?", "Sí", "Todos pueden participar."),
    ],
    U=[
        ex("¿Qué es una asamblea? A) Reunión de todos los integrantes para decidir algo. B) Una fiesta del curso.", "A", "Esa es su definición."),
        ex("¿Qué función tiene la tesorería: registrar acuerdos o cuidar el dinero del curso?", "Cuidar el dinero del curso", "El tesorero o la tesorera administra los fondos."),
        ex("Los representantes, ¿mandan al curso o lo sirven?", "Lo sirven", "Actúan en nombre de los demás."),
    ],
    A=[
        ex("Cuatro situaciones: 1) votar cómo gastar los fondos; 2) un solo estudiante decide el paseo; 3) el secretario lee el acta; 4) se escucha la opinión de todas las personas. ¿Cuántas son democráticas?", "3", "La 1, la 3 y la 4 respetan la participación; en la 2 decide uno solo."),
        ex("El curso debe decidir cómo usar los $60.000. ¿Qué paso parece correcto primero? A) Informarse y proponer opciones. B) Gastar el dinero rápido.", "A", "La decisión requiere información."),
        ex("Un estudiante propone: «Que decida el mejor amigo del presidente». ¿Es democrático, sí o no?", "No", "Excluye la participación del curso."),
    ],
    Z=[
        ex("¿Por qué los representantes deben rendir cuentas?", "Porque actúan en nombre de todos", "Los demás tienen derecho a saber lo que hacen."),
        ex("¿Por qué es importante que los acuerdos se anoten?", "Para recordarlos y poder revisarlos", "Un acuerdo escrito evita confusiones."),
    ],
    D=[
        arith("El curso tiene $60.000. Gasta $25.000 en un paseo y $15.000 en material. ¿Cuánto le queda?", "60000-25000-15000", "Al total se le restan los gastos."),
        arith("En una asamblea participan 33 de los 40 estudiantes. ¿Cuántos no participaron?", "40-33", "Al total se le restan los presentes."),
    ],
    context=[ex("El 8.º A debe decidir si usa sus fondos en un paseo o en material para la sala. ¿Qué espacio de participación conviene y por qué?", "El Consejo de Curso o una asamblea, porque deciden todos", "Es una decisión importante que afecta a todo el curso.")],
    selfcheck=[ex("En Orientación: ¿la democracia hace que todos participen?", "Sí", "Todos pueden opinar."), ex("¿El tesorero cuida el dinero del curso?", "Sí", "Esa es su función."), ex("¿La directiva manda al curso?", "No", "Solo lo representa.")],
    task=T("Lee el caso inventado del 8.º A: tienen $60.000, dos propuestas (paseo o material) y una directiva con presidenta, secretario y tesorera. Escribe: el espacio donde decidirán, qué hará cada cargo y cómo se asegurará la participación de todos.", "Espacio: asamblea del curso. Presidenta: conduce la reunión. Secretario: anota los acuerdos. Tesorera: informa los fondos. Participación: todos pueden opinar por turnos y votar.", ["elige el espacio", "describe el rol de cada cargo", "asegura la participación de todos", "usa los datos del caso"], ["texto escrito"], ["decir que la presidenta decide", "no incluir a todos"], "Reconoce los roles y pregunta cómo registrarán el acuerdo."),
    reinforce="Escribe un ejemplo de decisión que se tome en el Consejo de Curso.",
    extend="Explica por qué los representantes no mandan, sino que sirven al curso.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Las intervenciones de la asamblea del 8.º B están escritas en los ejercicios. Todo es inventado.",
    "Aprenderé a distinguir hechos de opiniones en un debate, a respetar la diversidad de opiniones y el derecho de hombres y mujeres a participar. Sirve para debatir sin ofender y para decidir con información.",
    ["Conozco los espacios de participación.", "Sé que todos tienen derecho a opinar."],
    [
        "En un debate se mezclan hechos y opiniones. Un hecho se puede comprobar: «El curso tiene $60.000». Una opinión es lo que cada uno piensa: «El paseo es mejor que el material». Las dos son útiles, pero no valen lo mismo para decidir: los hechos ayudan a comprobar, las opiniones muestran lo que importa a cada uno. Conviene separarlos antes de votar.",
        "La diversidad de opiniones es normal y valiosa. Hombres y mujeres tienen el mismo derecho a opinar y a que su opinión se escuche con igual atención. Las emociones aparecen en los debates: entusiasmo, enojo, vergüenza. Se pueden sentir, pero no deben llevar a gritar ni a ofender.",
        "Hay límites claros: se respeta el turno de palabra, no se interrumpe, no se insulta ni se ridiculiza a quien piensa distinto, y se critica la idea, no a la persona. Si alguien incumple, quien dirige el debate le recuerda las reglas. Un buen debate termina con una decisión que todos puedan aceptar, aunque no fuera su primera elección.",
    ],
    [("hecho", "dato que se puede comprobar"), ("opinión", "lo que una persona piensa o prefiere"), ("diversidad de opiniones", "existencia de ideas distintas dentro de un grupo"), ("turno de palabra", "orden acordado para hablar"), ("debate", "conversación organizada donde se defienden ideas")],
    [
        W("Hecho u opinión", "En la asamblea alguien dice: «Tenemos $60.000» y otro dice: «El paseo es lo mejor». ¿Cuál es hecho y cuál opinión?", ["Los $60.000 se pueden comprobar.", "«Lo mejor» es una preferencia.", "Hay un hecho y una opinión."], "Hecho: tenemos $60.000. Opinión: el paseo es lo mejor"),
        W("Aplicar un límite", "Pablo interrumpe a Sofía diciendo «eso es tontería». ¿Qué regla se rompe y qué corresponde?", ["Interrumpe y ridiculiza.", "Se rompen el turno y el respeto.", "Quien dirige le recuerda las reglas."], "Se rompe el turno y el respeto; quien dirige recuerda las reglas"),
    ],
    [
        M("Creer que una opinión repetida muchas veces es un hecho.", "Se confunde repetición con comprobación.", "Un hecho se comprueba."),
        M("Pensar que las mujeres deben hablar menos o después.", "Se repite un estereotipo.", "Hombres y mujeres tienen el mismo derecho a opinar."),
    ],
    R=[
        ex("«El curso tiene 40 estudiantes» ¿es un hecho o una opinión?", "Un hecho", "Se puede comprobar con la lista del curso."),
        ex("«El mejor paseo es el parque» ¿es hecho u opinión?", "Opinión", "Expresa una preferencia."),
        ex("¿Se respeta el turno de palabra, sí o no?", "Sí", "Es una regla del debate."),
    ],
    U=[
        ex("¿Qué se critica en un buen debate? A) La idea. B) A la persona.", "A", "Se evita ofender."),
        ex("¿Hombres y mujeres tienen el mismo derecho a opinar, sí o no?", "Sí", "Todos tienen voz."),
        ex("Si alguien insulta, ¿quién recuerda las reglas: el que dirige el debate o nadie?", "El que dirige el debate", "Cuida que se respeten."),
    ],
    A=[
        ex("Intervenciones: 1) «Hay $60.000»; 2) «El paseo es lo mejor»; 3) «El material cuesta $35.000»; 4) «Todos quieren paseo». ¿Cuáles son hechos comprobables?", "1 y 3", "Son datos que se pueden comprobar; la 2 y la 4 son opiniones."),
        ex("Una estudiante pide la palabra hace rato y nadie la escucha por ser mujer. ¿Qué principio se rompe? A) La igualdad. B) La puntualidad.", "A", "Se le niega la voz por su género."),
        ex("Un compañero dice «Tu idea es ridícula». ¿Qué frase respetuosa sirve mejor? A) «No comparto tu idea porque…». B) «Eres tonto».", "A", "Critica la idea con razones."),
    ],
    Z=[
        ex("¿Por qué conviene separar hechos y opiniones antes de votar?", "Porque se decide con datos y se respetan las preferencias", "Los hechos ayudan a comparar y las opiniones muestran lo que importa."),
        ex("¿Por qué la diversidad de opiniones es valiosa para un curso?", "Porque muestra más ideas y puntos de vista", "Decidir con varias perspectivas mejora las decisiones."),
    ],
    D=[
        arith("En una asamblea hablaron 12 estudiantes: 7 hombres y el resto mujeres. ¿Cuántas mujeres hablaron?", "12-7", "Al total se le restan los hombres."),
        arith("Cada intervención dura 2 minutos y hay 9 intervenciones. ¿Cuántos minutos dura el debate?", "2*9", "Se multiplican los minutos por las intervenciones."),
    ],
    context=[ex("En el Consejo de Curso, Matías dice que «las niñas no saben de fútbol» y quiere que no opinen sobre el campeonato. ¿Qué regla del debate se rompe?", "La igualdad de derecho a opinar", "Todos tienen el mismo derecho a participar.")],
    selfcheck=[ex("En Orientación: ¿un hecho se puede comprobar?", "Sí", "Una opinión no."), ex("¿Mujeres y hombres opinan por igual?", "Sí", "Es un derecho igual."), ex("¿Se puede ridiculizar a quien piensa distinto?", "No", "Rompe el respeto.")],
    task=T("Lee las seis intervenciones inventadas de una asamblea: (a) «Hay $60.000»; (b) «El paseo es mejor»; (c) «El material cuesta $35.000»; (d) «Las mujeres no entienden de números»; (e) «Me gustaría que decidamos por voto»; (f) «Eso es tontería». Clasifica cada una como hecho, opinión o falta de respeto y reescribe las faltas de respeto de forma adecuada.", "(a) Hecho. (b) Opinión. (c) Hecho. (d) Falta de respeto, estereotipo: «Todos podemos opinar sobre los números». (e) Opinión. (f) Falta de respeto: «No comparto esa idea, porque…».", ["clasifica las seis", "reescribe las faltas de respeto", "usa lenguaje respetuoso", "defiende la igualdad"], ["tabla de clasificación"], ["aceptar estereotipos", "confundir hechos y opiniones"], "Reconoce las clasificaciones y pregunta cómo moderaría el debate."),
    reinforce="Escribe un hecho y una opinión sobre una decisión del curso inventado.",
    extend="Explica por qué se critica la idea y no a la persona.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Los votos de la asamblea del 8.º C están escritos en los ejercicios. Todas las cifras son inventadas.",
    "Aprenderé a comparar formas de tomar decisiones en el curso: consenso, votación por mayoría y decisión de una sola persona, y sus consecuencias. Sirve para elegir la forma más democrática.",
    ["Sé distinguir hechos y opiniones.", "Sé que hay turnos de palabra."],
    [
        "Hay tres formas de decidir. En el consenso todos acuerdan una misma decisión después de conversar; es ideal, pero puede tardar. En la votación se cuenta cuántos apoyan cada opción y gana la que tiene más votos. La decisión de una sola persona no es democrática, porque no toma en cuenta a los demás.",
        "En la votación hay dos tipos de mayoría. La mayoría simple es la opción con más votos que las demás. La mayoría absoluta es la que obtiene más de la mitad de los votos de quienes votan. Por ejemplo, con 30 votantes, la mayoría absoluta exige al menos 16 votos. Si no hay mayoría absoluta, se puede hacer una segunda votación entre las dos más votadas.",
        "Cada forma tiene consecuencias. El consenso deja a casi todos conformes, pero toma tiempo. La votación es rápida, pero deja una minoría que perdió: es importante respetar su derecho a opinar y cumplir lo decidido. La decisión de una sola persona es rápida, pero daña la confianza. Al comparar, pregunta: ¿participaron todos?, ¿se respetó la opinión de la minoría?",
    ],
    [("consenso", "acuerdo en que todos están de acuerdo"), ("votación", "forma de decidir contando los votos"), ("mayoría simple", "opción con más votos que las demás"), ("mayoría absoluta", "opción con más de la mitad de los votos"), ("minoría", "grupo que obtuvo menos votos")],
    [
        W("Contar votos", "En el 8.º C votan 30 estudiantes: paseo 14, material 11, taller 5. ¿Cuál gana por mayoría simple?", ["Compara 14, 11 y 5.", "La mayor es 14.", "Gana el paseo."], "El paseo, con 14 votos"),
        W("Verificar mayoría absoluta", "En esa votación, ¿el paseo tiene mayoría absoluta?", ["Hay 30 votantes.", "La mitad es 15.", "14 no supera 15, entonces no hay mayoría absoluta."], "No: necesita al menos 16 votos"),
    ],
    [
        M("Creer que mayoría simple y absoluta son lo mismo.", "Se confunde tener más con tener más de la mitad.", "Absoluta es más de la mitad de los votos."),
        M("Pensar que, tras la votación, la minoría ya no cuenta.", "Se ignora a quienes perdieron.", "La minoría mantiene sus derechos y se respeta."),
    ],
    R=[
        ex("Votar y contar quién tiene más votos, ¿es una votación o un consenso?", "Una votación", "Se cuentan votos."),
        ex("La decisión de una sola persona, ¿es democrática, sí o no?", "No", "No toma en cuenta a los demás."),
        ex("La mayoría absoluta, ¿es más de la mitad de los votos, sí o no?", "Sí", "Esa es su definición."),
    ],
    U=[
        ex("¿Qué ventaja tiene el consenso? A) La mayoría queda conforme. B) Es muy rápido.", "A", "Todos participaron en el acuerdo."),
        ex("Una votación entre 40 personas, ¿cuántos votos exige la mayoría absoluta como mínimo?", "21", "La mitad es 20, más de la mitad exige 21.", calc="40//2+1"),
        ex("¿Qué se hace si nadie logra mayoría absoluta: una segunda votación o dejar que decida uno?", "Una segunda votación entre las dos más votadas", "Mantiene la participación."),
    ],
    A=[
        arith("En una votación de 36 estudiantes, ¿cuántos votos son la mitad?", "36//2", "Se divide el total entre 2."),
        ex("Resultados: A 13, B 12, C 5 (total 30). ¿Hay mayoría absoluta, sí o no?", "No", "Ninguno supera 15 votos."),
        ex("Resultados: Paseo 21, Material 9 (total 30). ¿El paseo tiene mayoría absoluta, sí o no?", "Sí", "21 es más de la mitad de 30."),
    ],
    Z=[
        ex("¿Por qué la minoría debe ser respetada aunque haya perdido la votación?", "Porque sigue teniendo derecho a opinar y ser tratada con respeto", "La democracia protege a todos, no solo a la mayoría."),
        ex("¿Por qué el consenso puede tardar más que una votación?", "Porque requiere que todos se pongan de acuerdo", "Hay que conversar hasta que todos acepten."),
    ],
    D=[
        arith("En una votación de 30 estudiantes, A tiene 14 votos y B tiene 11. ¿Cuántos votaron por otras opciones?", "30-14-11", "Al total se le restan los votos de A y B."),
        arith("Si en una asamblea de 28 se necesitan más de la mitad de votos, ¿cuántos votos exige como mínimo la mayoría absoluta?", "28//2+1", "La mitad es 14, y se necesita uno más."),
    ],
    context=[ex("El 8.º C vota para elegir el nombre de su equipo: Halcones 11, Pumas 10, Delfines 9 (total 30). ¿Quién gana por mayoría simple?", "Halcones", "Tiene el mayor número de votos, 11.")],
    selfcheck=[ex("En Orientación: ¿la mayoría absoluta es más de la mitad?", "Sí", "Esa es su definición."), ex("¿La decisión de un solo estudiante es democrática?", "No", "No toma en cuenta a los demás."), ex("¿Se respeta a la minoría?", "Sí", "Mantiene sus derechos.")],
    task=T("Lee los resultados inventados de dos votaciones del 8.º C. Votación 1 (30 votantes): paseo 14, material 11, taller 5. Votación 2 (30 votantes): nombre Halcones 21, Pumas 9. Para cada una escribe quién gana por mayoría simple, si hay mayoría absoluta y cómo se trataría a quienes perdieron.", "V1: gana paseo (14), no hay mayoría absoluta (se necesitan 16); se hace segunda votación entre paseo y material. V2: gana Halcones (21), hay mayoría absoluta; se respeta a quienes votaron Pumas con participación en el diseño del nombre.", ["calcula las mayorías", "interpreta los resultados", "describe cómo respetar a la minoría", "usa los datos"], ["texto escrito"], ["confundir simple con absoluta", "ignorar a la minoría"], "Reconoce los cálculos y pregunta cómo integrar las ideas de la minoría."),
    reinforce="Escribe la diferencia entre mayoría simple y mayoría absoluta con un ejemplo inventado.",
    extend="Explica una ventaja y una desventaja de decidir por consenso.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. Los candidatos, los votos y la situación están escritos en los ejercicios. Los nombres son inventados.",
    "Aprenderé cómo se elige democráticamente a los representantes del curso y qué hacer si algo no es justo en la elección. Sirve para participar con responsabilidad y respetar los resultados.",
    ["Sé comparar formas de decidir.", "Sé contar votos y mayorías."],
    [
        "Elegir representantes de forma democrática tiene pasos. Primero, se abren candidaturas: cada persona que quiere el cargo se presenta. Segundo, los candidatos presentan sus propuestas con respeto, sin descalificar a otros. Tercero, se vota de forma secreta, para que nadie se sienta presionado. Cuarto, se hace el escrutinio, que es contar los votos delante del curso. Quinto, se proclama a quien tiene la mayoría.",
        "Los candidatos pueden ser mujeres u hombres: ambos tienen el mismo derecho a postular y a ser elegidos. Una campaña respetuosa usa propuestas y no ofensas; no promete lo imposible ni da regalos a cambio de votos. Votar de forma informada significa conocer las propuestas y decidir por lo que ayuda al curso, no por amistad ni por presión.",
        "Después de la elección, el curso respeta el resultado y apoya al representante. Si ocurre algo injusto, como presiones o votos contados mal, se le cuenta al profesor jefe o a la persona que guía la elección para revisarlo. Una elección es limpia cuando todos pudieron participar con libertad y el conteo fue transparente.",
    ],
    [("candidatura", "postulación de una persona a un cargo"), ("voto secreto", "voto que nadie más ve"), ("escrutinio", "conteo de votos delante de todos"), ("campaña", "presentación de propuestas para ser elegido"), ("transparente", "que se hace a la vista de todos")],
    [
        W("Ordenar la elección", "Ordena: escrutinio, candidaturas, voto secreto, propuestas.", ["Primero se presentan candidaturas.", "Luego las propuestas.", "Después el voto secreto y el escrutinio."], "Candidaturas, propuestas, voto secreto, escrutinio"),
        W("Reconocer una irregularidad", "Una candidata regala dulces a cambio de votos. ¿Es una campaña respetuosa?", ["Da regalos a cambio de votos.", "Eso presiona a los votantes.", "No es correcto."], "No: es una irregularidad"),
    ],
    [
        M("Votar por la persona más simpática sin conocer sus propuestas.", "Se vota por amistad.", "Vota por las propuestas."),
        M("Descalificar al candidato rival en la campaña.", "Se piensa que ofender gana votos.", "Presenta tus propuestas con respeto."),
    ],
    R=[
        ex("El voto secreto, ¿lo ve todo el curso o nadie más?", "Nadie más", "Protege la libertad de elegir."),
        ex("El escrutinio, ¿es contar los votos delante de todos, sí o no?", "Sí", "Así se asegura la transparencia."),
        ex("Mujeres y hombres, ¿pueden postular al mismo cargo, sí o no?", "Sí", "Tienen el mismo derecho."),
    ],
    U=[
        ex("¿Por qué el voto es secreto? A) Para que nadie sea presionado. B) Para que sea más lento.", "A", "Protege la libertad de decidir."),
        ex("Regalar dulces para ganar votos, ¿es una conducta correcta, sí o no?", "No", "Condiciona la libertad de votar."),
        ex("Tras la elección, ¿el curso respeta al ganador o lo ignora?", "Lo respeta", "Aceptar el resultado es parte de la democracia."),
    ],
    A=[
        ex("Votos: Ana 14, Lucas 12, Ema 4 (total 30). ¿Quién es elegido por mayoría simple?", "Ana", "Tiene más votos, 14."),
        ex("Rodrigo ve que cuentan los votos y se equivocaron en la suma. ¿Qué debe hacer? A) Avisar al profesor jefe y pedir una revisión. B) Callar.", "A", "Un conteo mal hecho debe revisarse."),
        ex("Un compañero dice a otro: «Vota por mí o no eres mi amigo». ¿Qué principio se rompe?", "La libertad de elegir", "Es presión para votar."),
    ],
    Z=[
        ex("¿Por qué el escrutinio debe ser público?", "Porque da confianza en el resultado", "Todos ven que el conteo es correcto."),
        ex("¿Por qué votar por propuestas es mejor que votar por simpatía?", "Porque beneficia al curso y no a una amistad", "Las propuestas muestran qué hará el representante."),
    ],
    D=[
        arith("En una elección de 32 votantes, Lía obtuvo 15 votos, Pablo 10 y Sol el resto. ¿Cuántos votos obtuvo Sol?", "32-15-10", "Al total se le restan los otros votos."),
        arith("Para una segunda vuelta entre dos personas, 35 votantes, ¿cuántos votos exige la mayoría absoluta?", "35//2+1", "La mitad de 35 es 17,5; se necesita al menos 18, es decir 17 + 1."),
    ],
    context=[ex("En el 8.º D, tres estudiantes quieren ser presidente o presidenta. Una de ellas promete «no habrá pruebas nunca». ¿Es una promesa responsable?", "No, porque no puede cumplirla", "Una campaña respetuosa no promete lo imposible.")],
    selfcheck=[ex("En Orientación: ¿el voto es secreto?", "Sí", "Protege la libertad."), ex("¿Se puede regalar algo a cambio de votos?", "No", "Condiciona el voto."), ex("¿Se respeta el resultado?", "Sí", "Es parte de la democracia.")],
    task=T("Lee el caso inventado: el 8.º A elige presidenta o presidente. Hay tres candidaturas (Ema, Rafael, Camila). Resultados: Ema 13, Rafael 12, Camila 5 (30 votos). Escribe los cinco pasos de la elección con ejemplos del caso, quién gana por mayoría simple, si hay mayoría absoluta y qué haría el curso con el resultado.", "Pasos: candidaturas, propuestas, voto secreto, escrutinio, proclamación. Gana Ema por mayoría simple (13). No hay mayoría absoluta (se necesitan 16): segunda vuelta entre Ema y Rafael. El curso respeta el resultado.", ["escribe los cinco pasos", "interpreta los votos", "decide si hay segunda vuelta", "respeta el resultado"], ["texto escrito"], ["olvidar el voto secreto", "no revisar la mayoría"], "Reconoce los pasos y pregunta cómo apoyarán a quien gane."),
    reinforce="Escribe tres reglas de una campaña respetuosa.",
    extend="Explica por qué la transparencia del conteo da confianza en la elección.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. La propuesta del curso, el acta y las frases están escritas en los ejercicios. Todo es inventado.",
    "Aprenderé a presentar una propuesta, a debatir con respeto y a redactar un acuerdo del curso con acta. Sirve para participar en el Consejo de Curso y lograr fines compartidos.",
    ["Sé elegir representantes.", "Sé distinguir hechos y opiniones."],
    [
        "Para presentar una propuesta al curso conviene seguir cuatro pasos: decir qué se propone, explicar por qué (con hechos), indicar qué se necesita y para cuándo, y preguntar si hay dudas. Por ejemplo: «Propongo juntar $2.000 por persona para pintar la sala; hay 30 estudiantes y la pintura cuesta $60.000; lo necesitamos antes del 30 de junio. ¿Tienen dudas?».",
        "En el debate, se pide la palabra, se escucha sin interrumpir y se responde con argumentos, no con ofensas. Un buen argumento tiene una idea y una razón: «Estoy de acuerdo porque ayuda a cuidar la sala». Cuando se llega a una decisión, el secretario o secretaria escribe el acta con tres datos: qué se acordó, quién lo hará y para cuándo.",
        "Un acuerdo del curso tiene sentido si todos pueden cumplirlo, y se revisa en una fecha. Si hay dudas o un conflicto sobre el acuerdo, se vuelve a conversar en el Consejo y, si es necesario, se pide ayuda al profesor jefe. Participar de forma democrática es también cumplir lo acordado y apoyar a los representantes.",
    ],
    [("propuesta", "idea que se presenta para que el curso la discuta"), ("argumento", "razón que apoya una idea"), ("acta", "texto que registra los acuerdos"), ("plazo", "fecha límite para cumplir algo"), ("revisar", "mirar si un acuerdo se cumplió")],
    [
        W("Armar una propuesta", "Datos: pintar la sala cuesta $60.000; hay 30 estudiantes; plazo: 30 de junio. ¿Cuánto debe aportar cada uno?", ["Se reparte $60.000 entre 30.", "60.000 ÷ 30 = 2.000.", "Cada uno aporta $2.000."], "$2.000 por estudiante"),
        W("Escribir un acta", "Se acordó que Lía compra la pintura el lunes. ¿Cómo queda el acta?", ["Anota qué se acordó.", "Quién lo hará.", "Para cuándo."], "«Comprar la pintura; responsable: Lía; para el lunes»"),
    ],
    [
        M("Presentar una idea sin explicar su razón.", "Se cree que basta con proponer.", "Explica con hechos por qué conviene."),
        M("Dejar los acuerdos sin responsable ni plazo.", "Se supone que alguien lo hará.", "Anota quién, qué y para cuándo."),
    ],
    R=[
        ex("Una propuesta debe explicar por qué conviene, ¿verdadero o falso?", "Verdadero", "El argumento convence con razones."),
        ex("El acta registra los acuerdos, ¿sí o no?", "Sí", "Es su función."),
        ex("Pedir la palabra antes de hablar, ¿respeta el debate, sí o no?", "Sí", "Se respetan los turnos."),
    ],
    U=[
        ex("¿Qué tiene un buen argumento? A) Una idea y una razón. B) Una opinión dicha con mucha fuerza.", "A", "Así se convence con respeto."),
        ex("¿Qué tres datos lleva el acta?", "Qué se acordó, quién lo hará y para cuándo", "Permiten cumplir y revisar."),
        ex("Si hay dudas sobre un acuerdo, ¿se vuelve a conversar en el Consejo o se ignora?", "Se vuelve a conversar en el Consejo", "Es el espacio para resolverlo."),
    ],
    A=[
        arith("Una propuesta pide $1.500 por estudiante para 32 estudiantes. ¿Cuánto se reúne en total?", "1500*32", "Se multiplica el aporte por el número de estudiantes."),
        ex("Propuesta: «Que se compre una radio». ¿Qué le falta para ser clara? A) Razón, costo y plazo. B) Un nombre más original.", "A", "Una propuesta incluye por qué, cuánto y cuándo."),
        ex("Un estudiante dice «Estoy de acuerdo porque ayuda a cuidar la sala». ¿Qué tiene su intervención?", "Una idea y una razón", "Es un argumento completo."),
    ],
    Z=[
        ex("¿Por qué un acuerdo sin plazo se cumple menos?", "Porque no hay fecha para revisarlo", "El plazo permite saber si se cumplió."),
        ex("¿Por qué conviene que el acuerdo lo pueda cumplir todo el curso?", "Porque si no, algunos quedarán excluidos", "Un acuerdo realista incluye a todos."),
    ],
    D=[
        arith("El curso de 36 reúne $1.000 por estudiante para un paseo. ¿Cuánto reúne en total?", "1000*36", "Se multiplica el aporte por los estudiantes."),
        arith("Si el paseo cuesta $48.000 y reúnen $36.000, ¿cuánto falta?", "48000-36000", "Al costo se le resta lo reunido."),
    ],
    context=[ex("En el Consejo de Curso, Camila propone una rifa para juntar fondos, pero no dice cuánto necesitan ni para cuándo. ¿Qué dos datos faltan?", "El monto y la fecha", "Una propuesta debe incluir cuánto y para cuándo.")],
    selfcheck=[ex("En Orientación: ¿una propuesta explica por qué conviene?", "Sí", "Debe tener razones."), ex("¿El acta lleva responsable y plazo?", "Sí", "Permite cumplir el acuerdo."), ex("¿Se insulta en el debate?", "No", "Se debate con respeto.")],
    task=T("Lee el caso inventado: el 8.º B quiere comprar 4 cojines para la sala de lectura a $5.000 cada uno antes del 20 de mayo y son 25 estudiantes. Redacta: (1) la propuesta en cuatro partes; (2) un argumento a favor y una duda respetuosa; (3) el acta con el acuerdo.", "Propuesta: comprar 4 cojines ($20.000) para la sala de lectura, cada estudiante aporta $800; plazo 20 de mayo; ¿dudas? Argumento: ayuda a leer cómodos. Duda: ¿y si alguien no puede aportar? Acta: comprar cojines; responsable: Ema; para el 20 de mayo.", ["propuesta en cuatro partes", "argumento y duda respetuosa", "acta con qué, quién y cuándo", "cálculos correctos"], ["texto escrito"], ["propuesta sin razón", "acta sin plazo"], "Reconoce la estructura y pregunta qué harán si alguien no puede aportar."),
    reinforce="Escribe una propuesta breve para mejorar el patio del colegio con razón y plazo.",
    extend="Explica por qué cumplir los acuerdos también es participar.",
)

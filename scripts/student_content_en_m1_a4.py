"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 04 (lectura integrada de textos literarios y no literarios).

Todos los textos son originales y están escritos en el enunciado, con pista en español. Los datos de tablas y gráficos son «de ejemplo».
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA4 = "EN1M OA 04"
MATR = "Los textos y tablas escritos en cada ejercicio; lápiz y hoja para subrayar y anotar."

# ================================================================ OA 04 · clase 1: cuento (personajes, entorno, trama, conflicto)
STORY = "«Tomás had a small boat named Luna. Every Sunday he fished near the rocks of his village. One cloudy day, a strong wind pushed Luna away from the coast. Tomás was afraid, but he remembered his grandfather's advice: Stay calm and follow the lighthouse. He rowed slowly toward the light. At night, he arrived home safe. From that day, he always checked the weather before going out.» (boat = bote, fished = pescaba, rocks = rocas, village = caleta, cloudy = nublado, wind = viento, afraid = con miedo, advice = consejo, lighthouse = faro, rowed = remó, safe = a salvo, checked = revisaba)"

lesson(
    OA4, 1, MATR,
    "Aprenderé a reconocer en un cuento el propósito, el tema, los personajes, el entorno, la trama (inicio, desarrollo y final) y el conflicto. Sirve para entender una historia en inglés y explicar de qué trata sin traducirla.",
    ["Sé leer oraciones simples en pasado.", "Conozco las palabras but, then y after."],
    [
        "Un texto literario cuenta una historia. Sus elementos son: los personajes (characters), que son quienes actúan (Tomás y su abuelo); el entorno (setting), que es el lugar y el tiempo (una caleta, un domingo, un día nublado); y la trama (plot), que son los hechos en orden: inicio (Tomás pesca cada domingo), desarrollo (el viento aleja el bote) y final (llega a casa a salvo). El conflicto (conflict) es el problema que mueve la historia: aquí, el viento que aleja el bote de la costa.",
        "El tema (theme) es la idea general del texto, como una enseñanza: estar preparado y mantener la calma ante un problema. No se dice siempre en forma directa; se descubre al ver cómo se resuelve el conflicto. Los sentimientos de un personaje (afraid) y la palabra but muestran cambios: «was afraid, but he remembered» indica que el miedo no lo paralizó.",
        "Para leer un cuento, subraya primero nombres y lugares (personajes y entorno), luego los verbos de acción en pasado (pushed, rowed, arrived) para seguir la trama y busca la frase del problema. El propósito de un cuento suele ser entretener y dejar una enseñanza. La caracterización (characterization) es cómo conocemos a un personaje por lo que hace, dice y siente: Tomás es prudente porque, después del susto, revisa el clima antes de salir.",
    ],
    [("character", "personaje: quien actúa en la historia"), ("setting", "entorno: lugar y tiempo"), ("plot", "trama: hechos en orden (inicio, desarrollo, final)"), ("conflict", "conflicto: el problema de la historia"), ("theme", "tema: idea general o enseñanza"), ("advice", "consejo")],
    [
        ("Personajes y entorno", STORY + " ¿Quiénes son los personajes y cuál es el entorno?", ["Busco nombres: Tomás y su abuelo (grandfather).", "Busco lugares: la caleta y el mar cerca de las rocas.", "El tiempo: un domingo y un día nublado."], "Personajes: Tomás y su abuelo. Entorno: una caleta junto al mar, un domingo nublado"),
        ("Conflicto y final", STORY + " ¿Cuál es el conflicto y cómo termina?", ["El conflicto aparece cuando un viento fuerte empuja el bote lejos de la costa.", "Tomás recuerda el consejo y rema hacia el faro.", "Llega a casa a salvo."], "Conflicto: el viento aleja el bote. Final: llega a casa a salvo"),
    ],
    [
        ("Confundir el entorno con los personajes.", "Se mezclan quién actúa y dónde ocurre.", "Los personajes son seres; el entorno es lugar y tiempo."),
        ("Dar como tema un hecho suelto («Tomás pescaba»).", "Se confunde un hecho con la enseñanza.", "Formula el tema como idea general: cómo se enfrenta un problema."),
    ],
    [
        (STORY + " ¿Qué muestra que Tomás es un personaje prudente al final? A) revisa el clima antes de salir B) pesca todos los domingos", "A) revisa el clima antes de salir", "Revisar el clima es una acción cuidadosa; pescar los domingos es solo su costumbre."),
        (STORY + " ¿Dónde ocurre la historia? A) en una caleta junto al mar B) en un desierto", "A) en una caleta junto al mar", "Dice his village y menciona la coast y las rocas."),
        (STORY + " ¿Qué día pescaba Tomás habitualmente?", "Los domingos", "El texto dice Every Sunday."),
    ],
    [
        (STORY + " ¿Qué hizo Tomás para volver a casa? A) remó despacio hacia la luz del faro B) esperó quieto a que el viento parara", "A) remó despacio hacia la luz del faro", "El texto dice He rowed slowly toward the light."),
        (STORY + " ¿Qué sentimiento tiene Tomás cuando el bote se aleja?", "Miedo", "El texto dice Tomás was afraid."),
        (STORY + " ¿Cuándo llegó Tomás a casa? A) de noche B) al mediodía", "A) de noche", "El texto dice At night, he arrived home safe."),
    ],
    [
        (STORY + " Ordena los hechos con letras. A) The wind pushed Luna away. B) Tomás fished near the rocks. C) He arrived home safe. D) He rowed toward the light.", "B, A, D, C", "Primero pesca, luego el viento, después rema y al final llega."),
        (STORY + " ¿Qué consejo recordó Tomás?", "Mantener la calma y seguir el faro", "El texto dice Stay calm and follow the lighthouse."),
        (STORY + " ¿Qué hizo Tomás desde ese día?", "Revisó siempre el clima antes de salir", "Dice he always checked the weather."),
    ],
    [
        (STORY + " ¿Quién da el consejo? A) su abuelo B) su madre", "A) su abuelo", "El texto dice his grandfather's advice."),
        (STORY + " ¿Cuál es el tema? A) estar preparado y mantener la calma ante un problema B) pescar es peligroso siempre", "A) estar preparado y mantener la calma ante un problema", "La solución del conflicto está en la calma y la preparación posterior."),
    ],
    [
        (STORY + " ¿Qué muestra la palabra but en «was afraid, but he remembered»? A) que el miedo no lo paralizó B) que se rindió", "A) que el miedo no lo paralizó", "But introduce un contraste: el miedo y la acción."),
        (STORY + " Un lector dice que Tomás pierde el bote. ¿Qué dato lo corrige? A) Tomás llega a casa a salvo con su bote B) el viento sopla fuerte", "A) Tomás llega a casa a salvo con su bote", "El texto dice he arrived home safe, y no habla de pérdida."),
    ],
    [("Un cómic tiene cuatro cuadros. Cuadro 1: Girl: «My phone is at two percent.» Cuadro 2: Boy: «Use my charger.» Cuadro 3: Girl: «Thanks!» Cuadro 4: Boy: «In exchange, you carry my backpack.» (charger = cargador, in exchange = a cambio, carry = llevar, backpack = mochila). ¿Qué pide el chico a cambio del cargador?", "Que ella lleve su mochila", "El cuadro 4 dice you carry my backpack.")],
    [
        ("En Inglés: ¿Qué es el conflicto de una historia?", "El problema que mueve los hechos", "Sin conflicto no hay desarrollo."),
        ("¿Qué partes tiene la trama?", "Inicio, desarrollo y final", "Muestran los hechos en orden."),
        ("¿Qué es el entorno?", "El lugar y el tiempo de la historia", "Responde dónde y cuándo."),
    ],
    task("Lee este cuento breve original: «Valentina was nervous about her first day in a new school. In the yard, she did not know anyone. A girl named Isidora offered her a seat on the bench. They shared an apple and talked about music. At the end of the day, Valentina smiled. Tomorrow, she would find a friend for another new student.» (nervous = nerviosa, offered = ofreció, bench = banca, shared = compartieron, smiled = sonrió). En tu hoja escribe: personajes, entorno, conflicto, final y tema.", "Personajes: Valentina e Isidora. Entorno: el patio de un colegio nuevo, el primer día. Conflicto: Valentina no conoce a nadie y está nerviosa. Final: sonríe y quiere ayudar a otro estudiante nuevo. Tema: un gesto amable ayuda a integrarse.", ["nombra personajes y entorno correctos", "identifica el conflicto y el final", "formula un tema como idea general"], ["hoja con cinco respuestas", "subrayado del texto"], ["dar un hecho suelto como tema", "mezclar entorno y personajes"], "Reconoce los elementos acertados y ayuda a reformular el tema como una idea general."),
    "Vuelve a leer el cuento de Tomás y subraya con un color los personajes y con otro el entorno.",
    "Escribe en español el inicio, el desarrollo y el final de un cuento propio de cuatro líneas.",
)

# ---------------------------------------------------------------- clase 2: artículo de revista, tablas y gráficos
ART = "«Why teenagers need breaks. Studying for hours without rest does not help. The brain works better after a short break. For example, a ten-minute walk after fifty minutes of study can improve focus. However, many students check their phones during the break, and this does not rest the brain. A better idea is to stretch, drink water or look out of the window.» (breaks = pausas, rest = descanso, focus = concentración, check = revisar, stretch = estirarse, look out = mirar por)"
SCREEN = "Tiempo diario de pantalla de un curso (datos de ejemplo): lunes 3 horas, martes 2 horas, miércoles 4 horas, jueves 3 horas, viernes 5 horas."

lesson(
    OA4, 2, MATR,
    "Aprenderé a leer un artículo de revista y una tabla para encontrar el propósito, la idea principal, los datos y las relaciones de contraste y problema-solución. Sirve para estudiar y comparar información en textos reales.",
    ["Sé leer un cuento y reconocer su trama.", "Sé que however significa «sin embargo»."],
    [
        "Un texto no literario informa o explica. Un artículo de revista (magazine article) trata un tema y suele tener título, idea principal y ejemplos. La idea principal (main idea) es lo más importante que dice el texto; aquí, que los adolescentes necesitan pausas para estudiar mejor. Los detalles (details) la apoyan: un paseo de diez minutos después de cincuenta de estudio.",
        "Las relaciones entre ideas se anuncian con palabras. For example introduce un ejemplo. However marca un contraste: una idea que se opone a la anterior. Un problema-solución aparece cuando el texto presenta una dificultad (estudiar sin descanso no ayuda) y luego propone qué hacer (pausas cortas, estirarse, beber agua). Si ves la frase «A better idea is…», sigue una solución.",
        "Un gráfico o una tabla muestran datos con números. Para leerlos, mira el título, las unidades (horas) y el valor más alto y el más bajo. Puedes sumar los valores o compararlos. Recuerda que los datos de un ejemplo no representan a nadie en particular: sirven para practicar.",
    ],
    [("main idea", "idea principal"), ("detail", "detalle que apoya la idea"), ("for example", "por ejemplo"), ("however", "sin embargo"), ("table", "tabla: datos en filas y columnas"), ("solution", "solución")],
    [
        ("Idea principal", ART + " ¿Cuál es la idea principal?", ["El título dice Why teenagers need breaks.", "El texto explica cómo las pausas mejoran la concentración.", "La idea principal es que las pausas ayudan a estudiar."], "Los adolescentes necesitan pausas cortas para estudiar mejor"),
        ("Leer una tabla", SCREEN + " ¿Qué día hay más horas de pantalla?", ["Comparo los valores: 3, 2, 4, 3, 5.", "El mayor es 5.", "Corresponde al viernes."], "El viernes, con 5 horas"),
    ],
    [
        ("Elegir un ejemplo como idea principal.", "Se toma un detalle por el mensaje.", "La idea principal vale para todo el texto; el ejemplo solo la apoya."),
        ("Leer una tabla sin mirar las unidades.", "Se comparan números sin saber qué miden.", "Lee el título y las unidades antes de comparar."),
    ],
    [
        (ART + " ¿Qué palabra introduce un ejemplo? A) for example B) however", "A) for example", "For example significa por ejemplo."),
        (ART + " ¿Cuántos minutos dura el paseo recomendado?", "10 minutos", "El texto dice a ten-minute walk."),
        (SCREEN + " ¿Qué día hay menos horas de pantalla?", "El martes, con 2 horas", "Es el valor más bajo de la tabla."),
    ],
    [
        (ART + " ¿Cuál es el problema que plantea? A) estudiar horas sin descanso no ayuda B) los adolescentes duermen demasiado", "A) estudiar horas sin descanso no ayuda", "Es la primera idea del artículo."),
        (ART + " ¿Cuál es el propósito del texto? A) informar y recomendar B) contar un cuento", "A) informar y recomendar", "Explica un tema y propone ideas."),
        (SCREEN + " ¿Qué día tuvo 4 horas de pantalla?", "El miércoles", "Es el valor 4 de la tabla."),
    ],
    [
        arith(SCREEN + " ¿Cuántas horas de pantalla suma la semana de lunes a viernes?", "3+2+4+3+5", "Se suman los cinco valores."),
        (ART + " ¿Qué hacen muchos estudiantes durante la pausa y por qué es un problema? A) revisan el celular y el cerebro no descansa B) duermen y no estudian", "A) revisan el celular y el cerebro no descansa", "Lo dice la frase que sigue a However."),
        arith(SCREEN + " ¿Cuántas horas más de pantalla hay el viernes que el martes?", "5-2", "Se resta el valor más bajo del más alto."),
    ],
    [
        (ART + " ¿Qué relación marca However? A) contraste B) ejemplo", "A) contraste", "Opone el descanso real al uso del celular."),
        (ART + " ¿Qué solución propone el texto? A) estirarse, beber agua o mirar por la ventana B) estudiar más horas", "A) estirarse, beber agua o mirar por la ventana", "La frase A better idea is… presenta la solución."),
    ],
    [
        (ART + " Un lector dice que el texto recomienda mirar el celular en la pausa. ¿Qué parte lo corrige? A) this does not rest the brain B) a ten-minute walk", "A) this does not rest the brain", "El texto dice que el celular no descansa el cerebro."),
        (SCREEN + " Un compañero dice que el jueves hay más horas que el miércoles. ¿Es correcto? A) no, el jueves tiene 3 y el miércoles 4 B) sí", "A) no, el jueves tiene 3 y el miércoles 4", "Se comparan los valores de la tabla."),
    ],
    [("Lee este aviso de revista: «Reading club for teenagers. Meet every Thursday at 5 p.m. at the public library. Free entry. This month's book is a short mystery.» (reading club = club de lectura, entry = entrada, mystery = misterio). ¿Qué día se reúne el club?", "Los jueves", "El aviso dice every Thursday.")],
    [
        ("¿Qué es la idea principal de un texto?", "Lo más importante que dice", "Los detalles la apoyan."),
        ("¿Qué indica la expresión for example?", "Que viene un ejemplo", "Concreta una idea."),
        ("¿Qué mirar primero en una tabla?", "El título y las unidades", "Dicen qué datos hay."),
    ],
    task("Lee este fragmento de artículo original: «Why do we need to drink water? Water helps the body stay at the right temperature. However, many people forget to drink it during the day. A simple solution is to keep a bottle on the desk. For example, you can finish one bottle before lunch.» (temperature = temperatura, forget = olvidar, keep = mantener, desk = escritorio, finish = terminar). En tu hoja escribe: la idea principal, un problema, una solución y un ejemplo.", "Idea principal: el agua ayuda al cuerpo a mantener su temperatura. Problema: muchas personas olvidan beber agua. Solución: tener una botella en el escritorio. Ejemplo: terminar una botella antes del almuerzo.", ["escribe una idea principal general", "separa problema, solución y ejemplo", "usa datos del texto"], ["hoja con cuatro respuestas", "subrayado del texto"], ["tomar el ejemplo como idea principal", "inventar una solución que no está en el texto"], "Valora la separación de las ideas y repasa las palabras however y for example."),
    "Vuelve a leer el artículo de las pausas y subraya con colores el problema y las soluciones.",
    "Escribe en español un problema de estudio que tengas y una solución, imitando la estructura del artículo.",
)

# ---------------------------------------------------------------- clase 3: colocaciones, conectores y palabras derivadas
lesson(
    OA4, 3, MATR,
    "Aprenderé a reconocer colocaciones, conectores y palabras formadas con los prefijos ir- y dis- y los sufijos -er, -ist, -ess y -ful. Sirve para deducir el significado de palabras nuevas al leer.",
    ["Sé que un prefijo va al inicio de la palabra y un sufijo al final.", "Conozco palabras como teacher, careful y regular."],
    [
        "Muchas palabras nuevas se forman agregando partes a una palabra conocida. Los prefijos cambian el sentido: dis- indica lo contrario (agree → disagree, honest → dishonest, appear → disappear) e ir- también indica negación delante de algunas palabras (regular → irregular, responsible → irresponsible). Los sufijos indican la clase de palabra: -er y -ist nombran a una persona según su ocupación (teach → teacher, piano → pianist, art → artist), -ess nombra a una mujer en algunas ocupaciones (actor → actress, waiter → waitress) y -ful significa «lleno de» (care → careful, help → helpful).",
        "Las combinaciones frecuentes (collocations) se reconocen porque las palabras suelen ir juntas: make a decision, take a photo, do homework, have a shower, heavy rain. Los conectores muestran la relación: later (después), last (por último), so that (para que), although (aunque) y both (los dos). Leerlos en bloque ayuda a entender rápido.",
        "Cuando encuentres una palabra desconocida, descomponla: ¿hay un prefijo o un sufijo?, ¿qué palabra conocida queda? Por ejemplo, irresponsible = ir- (no) + responsible (responsable): «no responsable». Luego comprueba si el significado encaja en la oración.",
    ],
    [("prefix", "prefijo: parte al inicio (dis-, ir-)"), ("suffix", "sufijo: parte al final (-er, -ist, -ess, -ful)"), ("dis-", "indica lo contrario: disagree"), ("ir-", "indica negación: irregular"), ("-ful", "lleno de: careful"), ("collocation", "combinación frecuente de palabras")],
    [
        ("Prefijo dis-", "En «Mateo disagrees with Ana», ¿qué significa disagrees?", ["Separo el prefijo dis- de agree.", "Agree significa estar de acuerdo.", "Dis- indica lo contrario: no estar de acuerdo."], "No está de acuerdo"),
        ("Sufijo -ful", "En «Be careful with the hot soup», ¿qué significa careful?", ["Separo care + -ful.", "Care es cuidado y -ful es lleno de.", "Careful significa lleno de cuidado."], "Con cuidado, cuidadoso"),
    ],
    [
        ("Creer que disagree significa lo mismo que agree.", "No se mira el prefijo dis-, que invierte el significado.", "Dis- más una palabra da su opuesto: agree → disagree."),
        ("Pensar que toda ocupación de mujer lleva -ess (como «teacheress»).", "Se generaliza -ess a todas las palabras.", "-er y -ist sirven para cualquier persona; -ess solo en algunas palabras como actress o waitress."),
    ],
    [
        ("¿Qué significa irregular? A) no regular B) muy regular", "A) no regular", "El prefijo ir- indica negación."),
        ("¿Qué significa dishonest? A) no honesto B) muy honesto", "A) no honesto", "Dis- indica lo contrario."),
        ("Forma una palabra: help + ful =", "helpful", "El sufijo -ful agrega el sentido de «lleno de»."),
    ],
    [
        ("¿Qué es una pianist? A) una persona que toca piano B) un instrumento", "A) una persona que toca piano", "El sufijo -ist nombra a quien practica algo."),
        ("¿Qué es una actress? A) una actriz B) un actor", "A) una actriz", "El sufijo -ess marca una mujer en esa ocupación."),
        ("¿Cuál palabra significa «la persona que enseña»? A) teacher B) teachist", "A) teacher", "Teach + -er nombra a quien enseña."),
    ],
    [
        ("Lee: «It was an irresponsible decision to leave the door open.» ¿Qué significa irresponsible? A) no responsable B) muy responsable", "A) no responsable", "El prefijo ir- cambia responsible a su opuesto."),
        ("Une cada palabra con su significado. 1) colorful 2) disappear 3) scientist Significados: a) lleno de color b) persona que hace ciencia c) dejar de verse", "1-a, 2-c, 3-b", "Color + ful, dis + appear y science + ist."),
        ("Completa con la colocación: «She needs to ____ a decision today.» A) make B) do", "A) make", "En inglés se dice make a decision."),
    ],
    [
        ("Lee: «Lucas is a careful driver so that his passengers feel safe.» ¿Para qué es cuidadoso? A) para que los pasajeros se sientan seguros B) para ir más rápido", "A) para que los pasajeros se sientan seguros", "So that introduce el propósito."),
        ("Lee: «Both Camila and Fabián are artists.» ¿Cuántas personas son artistas? A) dos B) una", "A) dos", "Both se refiere a las dos personas nombradas."),
    ],
    [
        ("Lee: «Although the weather was cold, the waitress smiled.» ¿Qué contraste hay? A) hacía frío y ella sonrió B) hacía calor y ella lloró", "A) hacía frío y ella sonrió", "Although opone el frío a la sonrisa."),
        ("¿Cuál de estas palabras NO está formada con un prefijo de negación? A) disagree B) careful", "B) careful", "Careful lleva el sufijo -ful, no un prefijo de negación."),
    ],
    [("En un anuncio leíste: «We need a helpful waiter or waitress for the weekend. Do not be irresponsible: we start at nine.» (weekend = fin de semana, start = empezar). ¿Qué cualidad piden?", "Que sea servicial o útil", "Helpful es help + ful.")],
    [
        ("¿Qué indica el prefijo dis-?", "Lo contrario", "Cambia el sentido al opuesto."),
        ("¿Qué sufijo nombra a una persona que toca el piano?", "-ist", "Pianist: piano + ist."),
        ("¿Qué significa el sufijo -ful?", "Lleno de", "Careful: lleno de cuidado."),
    ],
    task("Lee este anuncio original: «Our school band needs a pianist, a singer and an actress for the musical. We are looking for helpful and colorful students. Both beginners and experts are welcome. Do not be shy: audition on Friday at four.» (musical = obra musical, beginners = principiantes, experts = expertos, shy = tímido, audition = audición). En tu hoja escribe: dos palabras con sufijo y su significado, la palabra que usa -ful y su sentido, y qué significa both.", "Pianist: quien toca el piano (piano + ist). Singer: quien canta (sing + er). Helpful: servicial. Both: los dos tipos de estudiantes (principiantes y expertos).", ["identifica dos palabras con sufijo y las explica", "da el sentido de una palabra con -ful", "explica both con el texto"], ["hoja con cuatro respuestas", "subrayado del anuncio"], ["no separar la palabra de su sufijo", "traducir both como «ninguno»"], "Reconoce la descomposición lograda y practica con otras tres palabras."),
    "Haz una tabla de dos columnas con las palabras con prefijo y con sufijo de esta clase.",
    "Escribe en español cinco palabras en inglés de tu colegio que tengan -er, -ist o -ful y su significado.",
)

# ---------------------------------------------------------------- clase 4: correo, catálogo y página web con vacío de información
MAIL = "Correo de Daniela al Sr. Torres: «Hello, Mr. Torres. We need a bus for 38 students and two teachers. We want to travel on a Friday morning. Our budget is two hundred thousand pesos. Can you recommend a bus?» (need = necesitamos, budget = presupuesto, recommend = recomendar)"
CAT = "Catálogo del Sr. Torres: «Bus A: 30 seats, 150,000 pesos. Bus B: 45 seats, 190,000 pesos. Bus C: 60 seats, 260,000 pesos.» (seats = asientos)"
WEB = "Página web de un museo: «Open Tuesday to Sunday, 10 a.m. to 6 p.m. Students: 2,000 pesos. Guided tours at 11 a.m. and 3 p.m. Closed on Mondays.» (open = abierto, guided tours = visitas guiadas, closed = cerrado)"
ASK = "Mensaje de Pablo al museo: «Hello. We are a group of thirty students. Can we visit on a Monday afternoon with a guide?» (group = grupo, visit = visitar, guide = guía)"

lesson(
    OA4, 4, "Dos textos que se complementan, escritos en cada ejercicio (un correo y un catálogo, o una página web y un mensaje); lápiz y hoja.",
    "Aprenderé a combinar la información de dos textos (un correo con una necesidad y un catálogo o página web con opciones) para tomar una decisión. Sirve para resolver situaciones reales, como elegir un bus o planificar una visita.",
    ["Sé leer correos y avisos simples.", "Sé comparar cantidades."],
    [
        "Un correo (email) tiene asunto, saludo, cuerpo y despedida, y comunica una necesidad: en este caso, un bus para 40 personas con un presupuesto. Un catálogo (catalog) lista opciones con sus características: asientos y precios. Una página web (web page) informa horarios y reglas. Estos textos son no literarios y se leen buscando datos.",
        "El vacío de información (information gap) aparece cuando un texto tiene la pregunta y otro tiene la respuesta. Para resolverlo: primero marca los requisitos del correo (38 estudiantes + 2 profesores = 40 personas; menos de 200.000 pesos). Luego revisa cada opción del catálogo y descarta las que no cumplan: Bus A no tiene suficientes asientos; Bus C supera el presupuesto; Bus B cumple las dos condiciones.",
        "Si no hay una opción que cumpla, el mensaje debe decirlo y pedir otra solución. Por ejemplo, el museo está cerrado los lunes: la visita de Pablo no se puede hacer ese día. Escribe tu decisión con una razón: «Bus B, because it has 45 seats and costs 190,000 pesos».",
    ],
    [("email", "correo electrónico"), ("catalog", "catálogo: lista de opciones"), ("budget", "presupuesto: dinero disponible"), ("closed", "cerrado"), ("guided tour", "visita guiada"), ("requirement", "requisito: condición que se debe cumplir")],
    [
        ("Requisitos de un correo", MAIL + " ¿Cuántas personas viajan en total?", ["Los estudiantes son 38.", "Los profesores son dos.", "38 + 2 = 40."], "40 personas"),
        ("Decidir con dos textos", MAIL + " " + CAT + " ¿Qué bus conviene y por qué?", ["Se necesita lugar para 40 y un máximo de 200.000 pesos.", "Bus A tiene 30 asientos: no alcanza. Bus C cuesta 260.000: se pasa.", "Bus B tiene 45 asientos y cuesta 190.000."], "Bus B, porque tiene 45 asientos y cuesta 190.000 pesos"),
    ],
    [
        ("Elegir el bus más barato sin revisar los asientos.", "Se mira un solo requisito.", "Revisa todos los requisitos antes de decidir."),
        ("Leer solo uno de los dos textos.", "Se olvida que la información está repartida.", "Subraya en cada texto el dato que completa al otro."),
    ],
    [
        (MAIL + " ¿Cuál es el presupuesto?", "200.000 pesos", "El correo dice two hundred thousand pesos."),
        (CAT + " ¿Cuántos asientos tiene el Bus C?", "60", "El catálogo dice 60 seats."),
        (WEB + " ¿Qué días está cerrado el museo? A) los lunes B) los domingos", "A) los lunes", "La página dice Closed on Mondays."),
    ],
    [
        (MAIL + " " + CAT + " ¿Por qué no sirve el Bus A? A) tiene solo 30 asientos B) es muy caro", "A) tiene solo 30 asientos", "Se necesitan 40 asientos."),
        (MAIL + " " + CAT + " ¿Por qué no sirve el Bus C? A) cuesta más que el presupuesto B) tiene pocos asientos", "A) cuesta más que el presupuesto", "Cuesta 260.000 y el presupuesto es de 200.000."),
        (WEB + " ¿A qué horas hay visitas guiadas? A) a las 11 y a las 15 B) a las 10 y a las 18", "A) a las 11 y a las 15", "La página dice 11 a.m. y 3 p.m."),
    ],
    [
        arith(MAIL + " " + CAT + " ¿Cuántos pesos le sobran del presupuesto si contrata el Bus B?", "200000-190000", "Se resta el precio del presupuesto."),
        arith(MAIL + " " + CAT + " ¿Cuántos asientos quedan libres en el Bus B?", "45-40", "Se restan las 40 personas de los 45 asientos."),
        (WEB + " " + ASK + " ¿Pueden visitar el museo el lunes? A) no, porque está cerrado los lunes B) sí, con guía", "A) no, porque está cerrado los lunes", "La página dice Closed on Mondays."),
    ],
    [
        (WEB + " " + ASK + " ¿Qué día de la semana podrían proponer a Pablo? A) un martes por la tarde B) un lunes por la mañana", "A) un martes por la tarde", "El museo abre de martes a domingo y hay visita a las 3 p.m."),
        arith(WEB + " " + ASK + " Pablo viaja con treinta estudiantes que pagan la entrada de estudiante. ¿Cuántos pesos pagan por las entradas?", "30*2000", "30 entradas de 2.000 pesos cada una."),
    ],
    [
        (MAIL + " " + CAT + " Si el presupuesto fuera de 160.000 pesos, ¿qué bus alcanzaría para las 40 personas? A) ninguno B) el Bus B", "A) ninguno", "El Bus A cuesta 150.000 pero tiene 30 asientos; los otros cuestan más de 160.000."),
        (WEB + " Un grupo quiere visitar el museo con visita guiada a las 11. ¿Qué día no puede ir? A) lunes B) sábado", "A) lunes", "El museo está cerrado los lunes."),
    ],
    [("Lee: «Sports center. Pool: Monday to Friday, 7 a.m. to 9 p.m. Students pay 3,000 pesos. Children under 6 are free.» (pool = piscina, under = menores de). Una niña de 5 años quiere entrar. ¿Cuánto paga?", "Nada: es gratis", "Los menores de 6 años no pagan.")],
    [
        ("¿Para qué se compara un correo con un catálogo?", "Para decidir con la información de ambos", "Cada texto aporta un dato."),
        ("¿Qué haces con una opción que no cumple un requisito?", "La descarto", "Ya no es una solución válida."),
        ("En Inglés: ¿Qué es un presupuesto?", "El dinero disponible para algo", "Limita el precio de la opción."),
    ],
    task("Lee estos dos textos. Correo de Lucía a una pastelería: «We need a cake for twelve people for Saturday. Our budget is thirty thousand pesos. We do not eat nuts.» (cake = torta, nuts = frutos secos). Catálogo: «Cake 1: 8 people, 18,000 pesos, no nuts. Cake 2: 15 people, 26,000 pesos, with nuts. Cake 3: 14 people, 28,000 pesos, no nuts.» En tu hoja escribe qué torta conviene, cuál razón la elige y por qué descartas las otras dos.", "Conviene la torta 3: alcanza para 14 personas, cuesta 28.000 (dentro del presupuesto) y no lleva frutos secos. La 1 es para 8 personas. La 2 lleva frutos secos.", ["elige la torta 3", "explica los tres requisitos que cumple", "justifica el descarte de las otras dos"], ["hoja con la decisión y razones", "subrayado de los requisitos"], ["elegir la torta 2 por ser más barata", "olvidar el requisito de los frutos secos"], "Valora los requisitos usados y propone revisar de nuevo los que se pasaron por alto."),
    "Vuelve a leer el correo del bus y subraya los tres requisitos; luego tacha las opciones que no los cumplen.",
    "Escribe en español dos requisitos que tendría un correo pidiendo una sala para un taller y una opción que los cumpla.",
)

# ---------------------------------------------------------------- clase 5: poema, reseña y biografía (lectura independiente)
POEM = "«Rain on the Roof. / Drip, drop, the rain is here, / Tapping soft, but sound is clear. / My dog sleeps near the door, / Dreaming of the sun once more. / I drink hot tea and read, / Rain is all I need.» (roof = techo, drip drop = gota a gota, tapping = golpeteando, softly = suave, clear = claro, door = puerta, once more = otra vez, need = necesito)"
REVIEW = "«Review: The Silent Library. This mystery novel for teenagers has an interesting plot. A group of students finds a secret room in an old library. The characters are realistic, and the ending is surprising. However, the first chapters are slow. I recommend it for readers who like mysteries. Rating: 4 out of 5.» (review = reseña, plot = trama, secret room = habitación secreta, realistic = realistas, surprising = sorprendente, slow = lentos, rating = puntaje)"
BIO = "«Biography (fictional): Marina Soto was born in a small town in the south of Chile. As a child, she loved insects. She studied biology and became a scientist. Later, she wrote a book for young readers about butterflies. Today, she teaches students how to protect the forest.» (born = nació, insects = insectos, studied = estudió, became = se convirtió en, wrote = escribió, butterflies = mariposas, forest = bosque)"

lesson(
    OA4, 5, MATR,
    "Aprenderé a leer por mi cuenta un poema, una reseña y una biografía e identificar propósito, tema, ideas, personajes o datos y relaciones entre ideas. Sirve para comprobar que ya puedo leer textos literarios y no literarios sin ayuda.",
    ["Sé reconocer la idea principal.", "Sé las palabras however, later y both."],
    [
        "Un poema (poem) usa versos cortos, rima y palabras que crean imágenes y sentimientos. En «Rain on the Roof», la rima de here / clear y door / more crea musicalidad. El tema es la tranquilidad de una tarde de lluvia en casa. Una reseña (review) opina sobre un libro o una película: da datos (género, trama), valoraciones (interesting, slow) y una recomendación con puntaje. Una biografía (biography) cuenta la vida de una persona en orden: nace, estudia, trabaja y logra algo.",
        "Para leer sin ayuda, sigue siempre los mismos pasos: mira el título para predecir; lee una vez para el tema y el propósito; luego busca datos con una pregunta en mente; y revisa los conectores (however, later, both). En una reseña, However anuncia una crítica. En una biografía, Later marca el paso del tiempo. En un poema, observa las palabras repetidas y las que riman.",
        "Cada formato tiene un propósito. El poema busca emocionar o crear una imagen, la reseña busca orientar a quien va a leer o ver algo, y la biografía busca informar y a veces inspirar. Responde siempre con una pista del texto: una palabra, una frase o un dato.",
    ],
    [("poem", "poema"), ("review", "reseña: opinión sobre una obra"), ("biography", "biografía: vida de una persona"), ("rating", "puntaje, valoración"), ("rhyme", "rima"), ("recommend", "recomendar")],
    [
        ("Tema de un poema", POEM + " ¿Qué ambiente muestra el poema?", ["Las palabras son rain, tea, dog, read.", "Todo transmite calma en casa.", "El ambiente es una tarde tranquila de lluvia."], "Una tarde tranquila y acogedora de lluvia en casa"),
        ("Opinión en una reseña", REVIEW + " ¿Qué crítica hace el reseñista?", ["However introduce una crítica.", "Dice que los primeros capítulos son lentos.", "Es lo que no le gustó."], "Que los primeros capítulos son lentos"),
    ],
    [
        ("Leer el poema como si fuera una noticia.", "No se atiende al tono ni a las imágenes.", "Busca cómo suena y qué sentimientos crean las palabras."),
        ("Confundir la opinión del reseñista con un dato de la trama.", "No se separa qué se opina y qué se cuenta.", "Los adjetivos como interesting y slow son opiniones."),
    ],
    [
        (POEM + " ¿Qué hace el perro? A) duerme cerca de la puerta B) corre en la lluvia", "A) duerme cerca de la puerta", "El poema dice My dog sleeps near the door."),
        (REVIEW + " ¿Qué puntaje le da al libro?", "4 de 5", "Dice Rating: 4 out of 5."),
        (BIO + " ¿Dónde nació Marina Soto? A) en un pueblo pequeño del sur de Chile B) en una gran ciudad", "A) en un pueblo pequeño del sur de Chile", "El texto dice a small town in the south of Chile."),
    ],
    [
        (POEM + " ¿Qué palabras riman al final de los primeros versos? A) here y clear B) rain y tea", "A) here y clear", "Los versos 1 y 2 terminan en here y clear."),
        (REVIEW + " ¿A quién recomienda el libro? A) a lectores a quienes les gustan los misterios B) a quienes buscan comedias", "A) a lectores a quienes les gustan los misterios", "Dice I recommend it for readers who like mysteries."),
        (BIO + " ¿Qué amaba Marina cuando era niña?", "Los insectos", "El texto dice she loved insects."),
    ],
    [
        (REVIEW + " ¿Cuál es el propósito del texto? A) orientar a quien piensa leer el libro B) contar la vida de la autora", "A) orientar a quien piensa leer el libro", "Una reseña opina y recomienda."),
        (BIO + " ¿Qué hace hoy Marina? A) enseña a proteger el bosque B) escribe cuentos de misterio", "A) enseña a proteger el bosque", "Dice Today, she teaches students how to protect the forest."),
        (POEM + " ¿Qué bebe la persona del poema? A) té caliente B) jugo frío", "A) té caliente", "Dice I drink hot tea."),
    ],
    [
        (BIO + " Ordena los hechos con letras. A) She wrote a book about butterflies. B) She studied biology. C) She loved insects as a child. D) She teaches students.", "C, B, A, D", "La biografía sigue el orden de la vida."),
        (REVIEW + " ¿Qué palabra señala una crítica? A) However B) Review", "A) However", "However anuncia un punto en contra."),
    ],
    [
        (REVIEW + " Un compañero dice que el reseñista odia el libro. ¿Qué dato lo corrige? A) le pone 4 de 5 y lo recomienda B) dice que es un misterio", "A) le pone 4 de 5 y lo recomienda", "Una opinión mayormente positiva no es odio."),
        (POEM + " ¿Cuál es el mejor resumen? A) una persona disfruta una tarde de lluvia en casa con su perro y su té B) una persona sale a trabajar bajo la lluvia", "A) una persona disfruta una tarde de lluvia en casa con su perro y su té", "Reúne las imágenes del poema."),
    ],
    [("Lee esta reseña: «Review: The Last Goal. This football movie for families has great action. The players are funny, and the music is fun. However, the ending is predictable. Rating: 3 out of 5.» (movie = película, predictable = predecible). ¿Qué puntaje le da la reseña?", "3 de 5", "El texto dice Rating: 3 out of 5.")],
    [
        ("¿Qué busca una reseña?", "Opinar y orientar a posibles lectores", "Da valoraciones y recomendación."),
        ("¿En qué orden cuenta una biografía la vida?", "Cronológico", "Sigue los hechos en el tiempo."),
        ("¿Qué elementos crean musicalidad en un poema?", "La rima y la repetición", "Dan ritmo al texto."),
    ],
    task("Lee esta reseña original: «Review: Sky Garden. This comic for teenagers tells the story of two friends who build a garden on a roof. The drawings are colorful, and the characters are funny. However, the story is a little short. I recommend it for readers who like friendship stories. Rating: 4 out of 5.» (comic = historieta, build = construir, drawings = dibujos, short = corta, friendship = amistad). En tu hoja escribe: el propósito de la reseña, dos aspectos positivos, la crítica y a quién la recomienda.", "Propósito: opinar y orientar a quienes piensan leer la historieta. Positivos: dibujos coloridos y personajes divertidos. Crítica: la historia es un poco corta. Recomendación: lectores a quienes les gustan las historias de amistad.", ["indica el propósito con una palabra del texto", "separa aspectos positivos y crítica", "nombra a quién se recomienda"], ["hoja con cuatro respuestas", "subrayado del texto"], ["tomar la crítica como positivo", "no citar el texto"], "Celebra la separación de opinión y datos y repasa el uso de however."),
    "Lee de nuevo el poema de la lluvia y subraya las palabras que riman.",
    "Escribe en español cuatro líneas de una reseña de una película que conozcas, con una crítica y una recomendación.",
)

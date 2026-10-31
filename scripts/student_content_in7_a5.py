"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 05 (presentar información en forma oral con recursos
multimodales: propósito y audiencia, organización, imágenes, apoyo en palabras clave, ensayo y sonidos /z/ /s/ /h/ /g/ /dʒ/).
El estudiante practica en voz alta con una persona de su casa; los ejercicios cerrados se resuelven con lo escrito.
"""
from __future__ import annotations

from student_content_in7_a import ADULT, arith, lesson, task

OA5 = "IN07 OA 05"
MAT = "Los textos y datos escritos en cada ejercicio, lápiz y una persona de tu casa que te escuche cuando practiques en voz alta."

CLUB = "«Good morning, everyone. Today I will talk about our board game club. First, we meet on Thursday at four o'clock. Second, we play games like chess and dominoes. Third, everyone helps to put the games away. In short, the club is fun and free. Thank you for listening.» (board game = juego de mesa, meet = nos juntamos, dominoes = dominó, put away = guardar, in short = en resumen, free = gratis)"
PETS = "Gráfico de barras descrito: perros 8, gatos 6, peces 3, pájaros 2 (mascotas de un curso)."
GARDEN = "«Our school garden has tomatoes, lettuce and carrots. Students water the plants every morning. In summer, we make a salad with the vegetables.» (garden = huerto, lettuce = lechuga, carrots = zanahorias, water = regar, salad = ensalada, vegetables = verduras)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA5, 1, MAT,
    "Aprenderé a decidir para qué voy a presentar (propósito) y a quién (audiencia) antes de preparar una exposición oral. Sirve para escoger las palabras y los recursos adecuados.",
    ["Sé presentarme y decir de qué voy a hablar.", "Conozco palabras como explain, tell y teacher."],
    [
        "Toda presentación oral tiene un propósito (purpose) y una audiencia (audience). El propósito es lo que quieres lograr: explicar cómo se hace algo (explain), convencer de una idea (persuade), contar lo que ocurrió (tell a story) o informar sobre un tema (inform). La audiencia son las personas que te escuchan: compañeros, niños más pequeños o la directora del colegio.",
        "Decidir esto primero cambia todo lo demás. Para niños pequeños usarás frases cortas, palabras simples, gestos e imágenes grandes: Hi, kids! Look at this big fish! Para la directora usarás un lenguaje más formal: Good morning, Mrs. Mena. Thank you for listening. Para convencer, darás una razón y un ejemplo: We need a recycling bin because plastic is a problem.",
        "Antes de escribir tus ideas, hazte tres preguntas: ¿para qué hablo?, ¿quiénes me escuchan? y ¿qué quiero que recuerden? Las respuestas te ayudan a elegir el tema, el tono y los recursos. Una misma información, como cuidar un pez, se presenta distinto a niños de seis años que a compañeros de tu edad.",
    ],
    [("purpose", "propósito: lo que quiero lograr"), ("audience", "audiencia: quienes me escuchan"), ("explain", "explicar"), ("persuade", "convencer"), ("inform", "informar"), ("formal", "formal: cuidadoso y respetuoso")],
    [
        ("Propósito por la frase", "Frase: «Today I will explain how to wash your hands.» ¿Cuál es el propósito?", ["Miro el verbo explain.", "Explain significa explicar.", "El propósito es explicar pasos."], "Explicar cómo hacer algo"),
        ("Audiencia por el lenguaje", "Frase: «Dear teachers, we would like to ask for a new basketball hoop.» (dear = estimados, hoop = aro). ¿Qué audiencia tiene?", ["Dear teachers se dirige a los profesores.", "El lenguaje es respetuoso.", "La audiencia son los profesores."], "Profesores"),
    ],
    [
        ("Usar el mismo lenguaje para cualquier audiencia.", "No se pensó en quién escucha.", "Adapta el vocabulario, el tono y los recursos."),
        ("Preparar las ideas antes de decidir el propósito.", "Se junta información sin saber para qué.", "Primero decide para qué hablas y a quién."),
    ],
    [
        ("«Today I will explain how to wash your hands.» ¿Cuál es el propósito? a) explicar pasos b) convencer", "a) explicar pasos", "Explain significa explicar."),
        ("«Dear teachers, we would like to ask for a new basketball hoop.» ¿A quién se dirige? a) a los profesores b) a niños más pequeños", "a) a los profesores", "Dear teachers nombra a la audiencia."),
        ("¿Qué frase sirve para convencer? a) We need a recycling bin because plastic is a problem. b) First, fold the paper.", "a) We need a recycling bin because plastic is a problem.", "Da una razón con because."),
    ],
    [
        ("«Hi, kids! Look at this big blue fish!» (look at = mira). ¿Qué audiencia es la más probable? a) niños pequeños b) la directora del colegio", "a) niños pequeños", "El saludo y las frases simples son para niños."),
        ("«Let me tell you what happened last summer.» (last summer = el verano pasado). ¿Cuál es el propósito? a) contar una historia b) dar instrucciones", "a) contar una historia", "Tell you what happened anuncia un relato."),
        ("«Please vote for our class project because it saves water.» (vote = votar, saves = ahorra). ¿Cuál es el propósito?", "Convencer", "Pide votar y da una razón."),
    ],
    [
        ("Presentarás ante la directora. ¿Qué apertura es adecuada? a) Good morning, Mrs. Mena. Thank you for listening. b) Hi guys, what's up?", "a) Good morning, Mrs. Mena. Thank you for listening.", "Es respetuoso y formal."),
        ("Vas a explicar a niños de seis años cómo funciona un contenedor de reciclaje. ¿Qué recurso ayuda más? a) imágenes grandes y frases cortas b) mucho texto técnico", "a) imágenes grandes y frases cortas", "Los niños pequeños necesitan lenguaje simple e imágenes."),
        ("Antes de preparar una presentación, ¿qué debes decidir primero? a) para qué hablas y a quién b) cuántas diapositivas hacer", "a) para qué hablas y a quién", "Esas decisiones guían el resto."),
    ],
    [
        ("Una persona presenta el mismo tema a su curso y a niños de primero básico. ¿Qué cambia más? a) las palabras y los ejemplos b) el tema", "a) las palabras y los ejemplos", "El tema es el mismo, pero se adapta al público."),
        ("Si tu propósito es convencer, ¿cuál es mejor? a) dar una razón y un ejemplo b) repetir muchas veces el título", "a) dar una razón y un ejemplo", "Convencer requiere razones."),
    ],
    [
        ("¿Cuántas de estas frases sirven para convencer? 1) We should recycle. 2) The bus leaves at six. 3) It is important to save water. 4) I like green tea.", "2", "Las frases 1 y 3 proponen una idea con valor; las otras son datos o gustos."),
        ("«Thank you for listening. Are there any questions?» ¿Para qué sirve? a) para cerrar e invitar a preguntar b) para comenzar", "a) para cerrar e invitar a preguntar", "Se dice al final de una presentación."),
    ],
    [("Debes presentar a niños de diez años cómo cuidar un pez. ¿Cuál es el propósito y qué lenguaje usarías?", "Explicar; palabras simples y frases cortas", "La audiencia es infantil y se necesitan pasos claros.")],
    [
        ("En Inglés de 7.º (OA 5, clase 1): ¿Qué es la audiencia?", "Las personas que me escuchan", "Define el lenguaje de la presentación."),
        ("En Inglés de 7.º (OA 5, clase 1): ¿Qué es el propósito?", "Lo que quiero lograr al hablar", "Puede ser explicar, convencer, informar o contar."),
        ("¿Cuál es la primera decisión al preparar una exposición?", "Para qué hablo y a quién", "Guía el tema y el tono."),
    ],
    task("Elige una de estas tres situaciones y escribe en tu hoja el propósito, la audiencia y una frase en inglés para comenzar. Situación A: explicar a niños de seis años cómo regar una planta. Situación B: convencer a tu curso de ahorrar agua. Situación C: contar a tus compañeros un paseo.", "A: propósito explicar; audiencia niños; frase: Hi, kids! Today I will show you how to water a plant. B: convencer; compañeros; We should save water because it is important.", ["indica un propósito coherente", "indica la audiencia", "escribe una frase adecuada al público"], ["hoja con tres respuestas", "nota de la persona que escucha"], ["usar lenguaje formal con niños pequeños", "no relacionar la frase con el propósito"], "Reconoce lo que acertó y revisa con la persona de tu casa si la frase suena natural para ese público."),
    "Lee en voz alta la frase de la directora y la de los niños, y nota cómo cambia tu tono.",
    "Escribe dos aperturas distintas para el mismo tema, una para niños pequeños y otra para profesores.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA5, 2, MAT,
    "Aprenderé a organizar una presentación en apertura, ideas y cierre, usando conectores. Sirve para que el público siga mi mensaje paso a paso.",
    ["Sé el propósito y la audiencia de mi presentación.", "Conozco first, second, third y finally."],
    [
        "Una presentación clara tiene tres partes. La apertura (opening) saluda, nombra el tema y despierta el interés: Good morning, everyone. Today I will talk about our board game club. El desarrollo (body) presenta las ideas principales en orden, cada una con un dato o ejemplo. El cierre (closing) repite la idea más importante y agradece: In short, the club is fun and free. Thank you for listening.",
        "Los conectores guían al público. First, second y third indican el orden de las ideas. Finally indica la última. In short significa «en resumen» y anuncia el cierre. Con tres o cuatro ideas basta; si pones demasiadas, el público se pierde. Cada idea debe relacionarse con el tema que anunciaste en la apertura.",
        "Para revisar tu organización, pregúntate: ¿mi apertura dice el tema?, ¿mis ideas siguen un orden?, ¿mi cierre recuerda lo principal? Si falta una de las partes, la presentación se siente incompleta. Escribe cada parte en una tarjeta y practica pasando de una a otra.",
    ],
    [("opening", "apertura: saludo y tema"), ("body", "desarrollo: ideas principales"), ("closing", "cierre: resumen y agradecimiento"), ("in short", "en resumen"), ("first / second / third", "primero / segundo / tercero"), ("thank you for listening", "gracias por escuchar")],
    [
        ("Reconocer la apertura", CLUB + " ¿Cuál es la apertura?", ["La primera parte saluda y nombra el tema.", "Dice Good morning, everyone. Today I will talk about our board game club.", "Eso es la apertura."], "Good morning, everyone. Today I will talk about our board game club."),
        ("Contar las ideas", CLUB + " ¿Cuántas ideas principales presenta?", ["Busco First, Second y Third.", "Cada una trae una idea.", "Son tres."], "3"),
    ],
    [
        ("Empezar a hablar sin presentar el tema.", "El público no sabe de qué trata la exposición.", "Nombra el tema en la apertura."),
        ("Terminar sin cierre, con la última idea.", "La presentación queda cortada.", "Agrega un resumen y un agradecimiento."),
    ],
    [
        (CLUB + " ¿Cuál es la apertura? a) Good morning, everyone. Today I will talk about our board game club. b) In short, the club is fun and free.", "a) Good morning, everyone. Today I will talk about our board game club.", "Saluda y presenta el tema."),
        (CLUB + " ¿Cuál es el cierre? a) In short, the club is fun and free. Thank you for listening. b) First, we meet on Thursday.", "a) In short, the club is fun and free. Thank you for listening.", "Resume y agradece."),
        (CLUB + " ¿Cuántas ideas principales tiene el desarrollo?", "3", "Se marcan con First, Second y Third."),
    ],
    [
        (CLUB + " ¿Qué conector introduce la segunda idea?", "Second", "Dice Second, we play games like chess and dominoes."),
        (CLUB + " ¿Qué hace «In short»? a) anuncia un resumen b) presenta una idea nueva", "a) anuncia un resumen", "In short significa en resumen."),
        (CLUB + " ¿Qué parte nombra el tema? a) la apertura b) el cierre", "a) la apertura", "Dice Today I will talk about our board game club."),
    ],
    [
        ("Ordena. A) Thank you for listening. B) Today I will talk about my pet. C) My dog is brown and friendly.", "B, C, A", "Primero el tema, luego la idea y por último el agradecimiento."),
        ("Una presentación tiene apertura y tres ideas, pero no termina con un resumen. ¿Qué parte falta? a) el cierre b) el saludo", "a) el cierre", "El cierre resume y agradece."),
        ("Elige la mejor apertura. a) Hello, everyone. Today I will talk about recycling. b) Recycling. Thank you for listening.", "a) Hello, everyone. Today I will talk about recycling.", "Saluda y nombra el tema; la otra opción es un cierre, no una apertura."),
    ],
    [
        (CLUB + " ¿Cuántas oraciones tiene la presentación completa, si cuentas cada punto final?", "7", "Hay dos de apertura, tres de desarrollo y dos de cierre."),
        ("¿Por qué conviene cerrar una presentación con un resumen? a) para recordar la idea más importante b) para empezar otro tema", "a) para recordar la idea más importante", "El cierre refuerza el mensaje."),
    ],
    [
        ("En una presentación con cuatro ideas, ¿qué conector de esta clase marca la última idea?", "Finally", "Finally marca la última idea."),
        (CLUB + " Una compañera mueve la frase «Third, everyone helps to put the games away» al comienzo. ¿Qué parte se desordena? a) el orden de las ideas b) el cierre", "a) el orden de las ideas", "La tercera idea ya no aparece tercera."),
    ],
    [("Tu curso presentará en 1 minuto el proyecto del huerto. Tienes tres tarjetas: A) saludo y tema, B) tres ideas, C) resumen y gracias. ¿Cuál es el orden correcto? Escribe las letras en orden.", "A, B, C", "Primero la apertura, luego el desarrollo y por último el cierre.")],
    [
        ("En Inglés de 7.º (OA 5, clase 2): ¿Cuáles son las tres partes de una presentación?", "Apertura, desarrollo y cierre", "Dan una estructura clara."),
        ("¿Qué significa «in short»?", "En resumen", "Anuncia el cierre."),
        ("¿Para qué sirven first, second y third?", "Para ordenar las ideas", "Guían al público."),
    ],
    task("Prepara una presentación de cuatro frases en inglés sobre tu comida favorita. Escribe una apertura que nombre el tema, dos ideas con First y Second, y un cierre con In short. Practica en voz alta frente a una persona de tu casa.", "Good morning, everyone. Today I will talk about pizza. First, it is hot and tasty. Second, we can share it. In short, pizza is a great meal. Thank you.", ["escribe apertura, dos ideas y cierre", "usa al menos dos conectores", "presenta en voz alta"], ["hoja con las frases", "nota de la persona que escuchó"], ["olvidar el cierre", "no nombrar el tema en la apertura"], "Reconoce las partes que aparecen y señala con la persona de tu casa cuál conector hace falta para ordenar mejor."),
    "Lee en voz alta la presentación del club y marca con un lápiz dónde termina cada parte.",
    "Agrega una cuarta idea con Finally a tu presentación de la comida favorita.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA5, 3, MAT,
    "Aprenderé a usar imágenes, gráficos y objetos que agreguen significado a mi presentación. Sirve para que el público entienda mejor y recuerde lo que digo.",
    ["Sé organizar una presentación en tres partes.", "Sé leer un gráfico de barras sencillo."],
    [
        "Un recurso multimodal (multimodal resource) combina palabras con imágenes, gráficos, mapas, objetos o gestos. No se usa para decorar: debe agregar información. Un gráfico de barras sobre las mascotas del curso muestra cuántos tienen perro, gato, pez o pájaro; un mapa muestra dónde queda el colegio. Si la imagen no ayuda a entender, mejor no usarla.",
        "Una buena diapositiva o cartulina tiene pocas palabras, una imagen grande y letra legible. No copies tu discurso en ella. Mientras muestras el gráfico, describe lo que se ve: Eight students have dogs. Six students have cats. There are more dogs than cats. Señalar con la mano el dato que mencionas ayuda al público a seguirte.",
        "Para describir un gráfico usa números y comparaciones: more than (más que), fewer than (menos que), the same as (lo mismo que). Practica con el gráfico antes de la presentación: ¿qué datos quieres destacar?, ¿qué frase dirás para cada uno? Así tu voz y tu recurso van juntos.",
    ],
    [("multimodal", "que usa varios medios: palabras, imágenes, gestos"), ("chart", "gráfico"), ("more than", "más que"), ("fewer than", "menos que"), ("the same as", "lo mismo que"), ("point to", "señalar")],
    [
        ("Imagen que aporta", "¿Qué imagen aporta más para hablar de las mascotas de tu curso: un gráfico de barras con cada mascota o una foto de un paisaje?", ["Pienso qué dato necesita el público.", "Necesita saber cuántas mascotas de cada tipo hay.", "El gráfico lo muestra."], "El gráfico de barras"),
        ("Describir un gráfico", PETS + " ¿Qué frase en inglés describe bien el gráfico?", ["Miro el dato de perros: 8.", "La frase Eight students have dogs coincide.", "Es una descripción correcta."], "Eight students have dogs"),
    ],
    [
        ("Poner una imagen solo para decorar.", "La imagen no agrega información.", "Elige imágenes que expliquen o muestren datos."),
        ("Llenar la diapositiva con texto.", "El público lee en vez de escuchar.", "Usa pocas palabras y una imagen grande."),
    ],
    [
        (PETS + " ¿Cuántos estudiantes tienen perro?", "8", "Es el dato de la barra de perros."),
        (PETS + " ¿Qué mascota es la menos común?", "Los pájaros", "Tiene la barra más baja: 2."),
        ("¿Qué imagen aporta más para hablar de las mascotas del curso? a) un gráfico de barras con cada mascota b) una foto de un paisaje", "a) un gráfico de barras con cada mascota", "Muestra datos del tema."),
    ],
    [
        (PETS + " ¿Cuál frase describe bien el gráfico? a) Eight students have dogs. b) Eight students have fish.", "a) Eight students have dogs.", "Los perros son 8 y los peces 3."),
        arith(PETS + " ¿Cuántos estudiantes tienen gatos o peces?", "6+3", "Se suman los gatos y los peces.", " estudiantes"),
        ("Una diapositiva tiene mucho texto. ¿Qué conviene? a) pocas palabras y una imagen grande b) copiar todo el discurso", "a) pocas palabras y una imagen grande", "El público debe poder leer y escuchar."),
    ],
    [
        ("Vas a decir «Look at the map: our school is near the park». ¿Qué imagen sirve? a) un mapa con el colegio y el parque b) una foto de una torta", "a) un mapa con el colegio y el parque", "La imagen debe coincidir con la frase."),
        arith(PETS + " ¿Cuántas mascotas hay en total?", "8+6+3+2", "Se suman todas las barras.", " mascotas"),
        arith(PETS + " ¿Cuántos perros más que pájaros hay?", "8-2", "Se resta la barra de pájaros a la de perros.", " perros más"),
    ],
    [
        ("¿Por qué una imagen debe agregar información y no solo decorar? a) porque ayuda al público a entender un dato b) porque llena espacio", "a) porque ayuda al público a entender un dato", "El recurso debe tener una función."),
        (PETS + " Un compañero dice «There are more dogs than cats». Según el gráfico, ¿es cierto? Responde sí o no.", "Sí", "Hay 8 perros y 6 gatos."),
    ],
    [
        arith(PETS + " ¿Cuántas veces cabe la cantidad de pájaros en la de perros?", "8//2", "Se divide la cantidad de perros por la de pájaros: 8 ÷ 2.", " veces"),
        (PETS + " ¿Es cierta la frase «More than half of the pets are dogs or cats»? Responde sí o no.", "Sí", "Hay 14 perros y gatos de 19, y la mitad de 19 es 9,5."),
    ],
    [("Vas a presentar cómo llegan tus compañeros a la escuela. ¿Qué recurso conviene?", "Un gráfico de barras con las formas de llegar", "Muestra cuántos llegan caminando, en bus o en auto.")],
    [
        ("¿Para qué sirve una imagen en una presentación?", "Para agregar información", "No es solo decoración."),
        ("En Inglés de 7.º (OA 5, clase 3): ¿Qué significa «fewer than»?", "Menos que", "Se usa para comparar."),
        ("¿Cuánto texto debe llevar una diapositiva?", "Pocas palabras", "Así el público te escucha."),
    ],
    task("Observa este dato: en un curso, 5 estudiantes llegan a pie, 7 en bus y 3 en auto. Dibuja en tu hoja un gráfico de barras con esos datos y escribe tres frases en inglés que lo describan, usando more than, fewer than o the same as. Preséntalo en voz alta a una persona de tu casa.", "Seven students come by bus. Five students come on foot. There are more students by bus than by car.", ["gráfico con los tres datos correctos", "tres frases coherentes con el gráfico", "señala el dato al hablar"], ["hoja con gráfico y frases", "nota de la persona que escuchó"], ["datos que no coinciden con el gráfico", "frases demasiado largas"], "Reconoce lo que acertó y revisa con la persona de tu casa si las frases coinciden con el dibujo."),
    "Practica decir en voz alta las tres frases del gráfico mientras señalas cada barra.",
    "Busca un gráfico de una revista o del colegio y escribe dos frases en inglés que lo describan.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA5, 4, MAT,
    "Aprenderé a hablar apoyándome en palabras clave y no a leer mi texto completo. Sirve para sonar natural, mirar al público y recordar mejor mis ideas.",
    ["Sé organizar una presentación y usar imágenes.", "Sé identificar palabras clave en un texto."],
    [
        "Leer todo el texto hace que hables sin pausas, sin mirar al público y con voz monótona. Una alternativa es hablar desde palabras clave (key words). Una palabra clave es la que resume una idea completa: garden (huerto), water (regar), salad (ensalada). Con tres a cinco palabras por tarjeta tienes suficiente apoyo para recordar lo que sigue.",
        "Para elegir palabras clave, subraya los sustantivos y los verbos más importantes de cada idea y deja fuera las palabras pequeñas como the, a o our. Luego practica convertir cada palabra en una frase completa. Con garden y tomatoes puedes decir: Our garden has tomatoes. Con water puedes decir: Students water the plants every morning.",
        "Si olvidas una palabra, mira tu tarjeta y sigue con la siguiente idea; no te detengas. Practica varias veces: cada vez dirás la frase un poco distinta, y eso es normal. Cuida también los sonidos: garden comienza con /g/ como en «gato» y healthy comienza con el soplido /h/. Hablar con claridad es parte de hablar con confianza.",
    ],
    [("key word", "palabra clave: resume una idea"), ("card", "tarjeta de apoyo"), ("eye contact", "contacto visual"), ("monotone", "monótono: sin cambios de voz"), ("garden", "huerto"), ("healthy", "saludable")],
    [
        ("Elegir palabras clave", GARDEN + " ¿Cuál lista sirve mejor como tarjeta: garden – water – salad o the – our – a?", ["Las palabras pequeñas no resumen ideas.", "Garden, water y salad resumen las tres ideas.", "La lista correcta es la primera."], "garden – water – salad"),
        ("De palabra clave a frase", "Tu tarjeta dice «garden – tomatoes». ¿Qué frase dirías?", ["Uso las dos palabras.", "Construyo una oración completa.", "Our garden has tomatoes."], "Our garden has tomatoes"),
    ],
    [
        ("Poner el discurso completo en la tarjeta.", "Se termina leyendo.", "Escribe solo tres a cinco palabras por idea."),
        ("Detenerse por completo al olvidar una palabra.", "Se pierde el hilo.", "Mira la tarjeta y continúa con la idea siguiente."),
    ],
    [
        ("¿Cuál es una lista de palabras clave? a) garden – water – salad b) the – a – our", "a) garden – water – salad", "Resumen ideas completas."),
        ("¿Qué conviene escribir en una tarjeta? a) tres a cinco palabras clave b) el texto completo", "a) tres a cinco palabras clave", "Así evitas leer."),
        (GARDEN + " ¿Qué palabra clave resume «Students water the plants every morning»?", "water", "Regar es la acción principal de esa idea."),
    ],
    [
        ("Tu tarjeta dice «garden – water». ¿Qué frase dirías? a) Students water the plants in our garden. b) Garden the water students plants.", "a) Students water the plants in our garden.", "Es una oración completa y ordenada."),
        (GARDEN + " ¿Qué palabra clave resume «In summer, we make a salad with the vegetables»?", "salad", "La ensalada es el resultado de la idea."),
        ("¿Qué lista sirve mejor para «Every Friday, our class cleans the beach. We collect plastic bottles and bags. Then we sort them in bins.» (sort = clasificar)? a) beach – plastic – bins b) every – then – we", "a) beach – plastic – bins", "Resumen lugar, objeto y acción final."),
    ],
    [
        ("Tu tarjeta dice «recycle – paper – box». ¿Qué frase dirías? a) We recycle paper in a box. b) Box the recycle paper we.", "a) We recycle paper in a box.", "Es una oración ordenada que usa las tres palabras."),
        arith("Tu presentación tiene tres ideas y haces una tarjeta por idea, con un máximo de cinco palabras clave cada una. ¿Cuántas palabras clave puedes escribir en total como máximo?", "3*5", "Tres tarjetas de cinco palabras: 3 × 5.", " palabras"),
        (GARDEN + " ¿Qué palabra clave del texto indica un tiempo del año?", "summer", "In summer dice cuándo se hace la ensalada."),
    ],
    [
        ("¿Por qué no conviene leer el texto completo? a) porque pierdes contacto visual y suenas monótono b) porque es más rápido", "a) porque pierdes contacto visual y suenas monótono", "El público conecta mejor con quien lo mira."),
        ("Olvidaste una palabra durante la exposición. ¿Qué haces? a) miro la tarjeta y continúo con la idea siguiente b) me quedo en silencio hasta recordarla", "a) miro la tarjeta y continúo con la idea siguiente", "Seguir evita perder el ritmo."),
    ],
    [
        ("¿Cómo suena la g inicial de garden: /g/ o /dʒ/?", "/g/", "Suena como la g de «gato»."),
        ("¿Se pronuncia la h de healthy? Responde sí o no.", "Sí", "Comienza con el soplido /h/."),
    ],
    [("Debes presentar el proyecto de reciclaje de tu colegio: papel, plástico y vidrio. ¿Cuál tarjeta de tres palabras sirve? a) paper – plastic – glass b) the – and – our", "a) paper – plastic – glass", "Resumen los tres materiales.")],
    [
        ("En Inglés de 7.º (OA 5, clase 4): ¿Qué es una palabra clave?", "La que resume una idea completa", "Ayuda a recordar."),
        ("¿Cuántas palabras clave por tarjeta conviene?", "De tres a cinco", "Más palabras te llevan a leer."),
        ("En Inglés de 7.º (OA 5, clase 4): ¿Qué haces si olvidas una palabra?", "Miro la tarjeta y continúo", "No me detengo."),
    ],
    task("Lee este texto: «Our class has a recycling corner. We put paper in the blue box and plastic in the yellow box. Every Friday, two students take the boxes to the recycling center. We want to reduce rubbish.» (corner = rincón, box = caja, center = centro, reduce = reducir, rubbish = basura). Escribe una tarjeta con tres a cinco palabras clave y luego di las tres ideas en voz alta sin leer el texto.", "Palabras: recycling corner – blue box – yellow box – Friday – rubbish. Frases: We have a recycling corner. We put paper in the blue box...", ["elige tres a cinco palabras clave", "dice las ideas sin leer", "usa frases completas"], ["tarjeta escrita", "nota de la persona que escuchó"], ["escribir oraciones completas en la tarjeta", "detenerse al olvidar"], "Reconoce lo que acertó y ayuda a elegir las palabras más importantes."),
    "Practica con una persona de tu casa diciendo las tres ideas desde la tarjeta, mirando a quien te escucha.",
    "Elige un tema que te guste y prepara una tarjeta con cinco palabras clave para hablar un minuto.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA5, 5, MAT,
    "Aprenderé a ensayar mi presentación y a mejorar la claridad de mi voz, mi ritmo y mi pronunciación de sonidos como /z/, /s/, /h/, /g/ y /dʒ/. Sirve para presentar con seguridad.",
    ["Sé preparar una presentación con tarjetas.", "Sé distinguir los sonidos /z/ y /s/, /g/ y /dʒ/."],
    [
        "Ensayar (to rehearse) es practicar en voz alta antes de presentar. Pide a una persona de tu casa que te escuche y que observe cuatro cosas: el volumen (¿se oye bien?), el ritmo (¿hablas ni muy rápido ni muy lento?), el contacto visual (¿miras al público?) y la pronunciación. Después del ensayo, anota un cambio concreto para mejorar, por ejemplo: «hacer pausas».",
        "Los sonidos del inglés necesitan práctica. El sonido /z/ de zoo vibra en la garganta; el /s/ de sad no vibra. El sonido inicial /h/ de hot es un soplido suave; la h de hour no se pronuncia. El sonido /g/ de go y egg es como la g de «gato»; el sonido /dʒ/ de jacket, general y age es como una «ch» con voz. En los plurales, la s final suena /z/ después de un sonido con voz (dogs, bags) y /s/ después de p, t o k (cats, cups). Practica estas palabras en frases cortas.",
        "Ensaya varias veces y mide el tiempo. Si tu presentación dura más de lo permitido, quita detalles, no aceleres. Si te equivocas en una palabra, corrige y sigue: los errores son parte de la práctica. Con cada ensayo la voz sale más clara y el miedo escénico disminuye.",
    ],
    [("rehearse", "ensayar"), ("volume", "volumen de voz"), ("pace", "ritmo: velocidad al hablar"), ("pause", "pausa"), ("eye contact", "contacto visual"), ("silent h", "h muda (hour)")],
    [
        ("Corregir el ritmo", "Un compañero habla muy rápido en su ensayo. ¿Cómo puede mejorar?", ["Hablar rápido dificulta entender.", "Debe hacer pausas entre ideas.", "Así el público alcanza a seguirlo."], "Haciendo pausas entre ideas"),
        ("Corregir un sonido", "Tomás dice «giraffe» con el sonido /g/. ¿Cómo se corrige?", ["Giraffe comienza con g.", "Esa g suena /dʒ/.", "Debe decirla como jirafa con voz."], "Debe usar el sonido /dʒ/, como en jacket"),
    ],
    [
        ("Hablar más rápido para terminar a tiempo.", "Se sacrifica la claridad.", "Quita detalles en vez de acelerar."),
        ("Ensayar solo en silencio, en la mente.", "No se prueba la voz ni el tiempo.", "Practica en voz alta frente a una persona."),
    ],
    [
        ("Si hablas muy rápido, ¿cómo mejoras? a) haciendo pausas b) hablando más rápido", "a) haciendo pausas", "Las pausas dan tiempo al público."),
        ("¿Qué sonido tiene la g de general?", "/dʒ/", "General comienza con /dʒ/."),
        ("¿Qué sonido tiene la letra inicial de hot?", "/h/", "Es un soplido suave."),
    ],
    [
        ("Tomás dice «giraffe» con /g/. ¿Cómo se corrige? a) con /dʒ/ b) con /z/", "a) con /dʒ/", "Giraffe comienza con /dʒ/."),
        ("¿Qué conviene hacer con el contacto visual? a) mirar al público b) mirar solo el papel", "a) mirar al público", "Así el mensaje llega mejor."),
        ("La última fila no te escucha. ¿Qué haces?", "Subo el volumen sin gritar", "El volumen debe alcanzar a todo el público."),
    ],
    [
        ("Un ensayo anota: 1) habla muy rápido, 2) buen contacto visual, 3) dice hour con /h/, 4) cierre claro. ¿Cuántos problemas hay?", "2", "Hablar rápido y pronunciar la h de hour son los problemas."),
        ("¿Cuál es la pronunciación correcta de hour? a) sin h b) con h", "a) sin h", "La h de hour no se pronuncia."),
        ("Una compañera dice zoo con /s/ (suena «soo»). ¿Cuál es la corrección? a) hacer vibrar la garganta con /z/ b) decirlo más fuerte", "a) hacer vibrar la garganta con /z/", "Zoo comienza con /z/."),
    ],
    [
        ("¿Para qué ensayar frente a una persona? a) para detectar y corregir errores b) para memorizar todo", "a) para detectar y corregir errores", "Quien escucha ve lo que tú no notas."),
        ("Después del ensayo, ¿qué es mejor? a) anotar un cambio concreto b) decir solo «estuvo bien»", "a) anotar un cambio concreto", "Un cambio concreto permite mejorar."),
    ],
    [
        ("En la frase «A giant jacket in the gym», ¿cuántas palabras tienen el sonido /dʒ/?", "3", "Giant, jacket y gym comienzan con /dʒ/."),
        ("En «An honest hungry horse has a hat», ¿cuántas palabras comienzan con el sonido /h/ pronunciado?", "4", "Hungry, horse, has y hat; honest comienza con vocal."),
    ],
    [("Tu ensayo duró 3 minutos, pero tienes 2 minutos. ¿Qué haces?", "Quito detalles y dejo las ideas principales", "Acelerar baja la claridad.")],
    [
        ("¿Qué cuatro cosas observa quien te escucha?", "Volumen, ritmo, contacto visual y pronunciación", "Esos aspectos hacen clara una exposición."),
        ("¿Qué sonido tiene la s de dogs?", "/z/", "Viene después de g, que tiene voz."),
        ("En Inglés de 7.º (OA 5, clase 5): ¿Se pronuncia la h de honest?", "No", "Honest comienza con vocal."),
    ],
    task("Elige una de estas tres frases y prepárala para decirla en voz alta con claridad: A) «The zoo has a giant giraffe.» B) «My hungry hamster eats an egg.» C) «An honest guide gave us a gift.» Practica tres veces ante una persona de tu casa y anota qué sonido mejoró.", "Frase A: zoo con /z/, giant y giraffe con /dʒ/. Mejoré el sonido /dʒ/ de giraffe.", ["dice la frase con pausas y volumen adecuado", "pronuncia al menos un sonido de la clase", "anota un cambio concreto"], ["hoja con el sonido practicado", "nota de la persona que escuchó"], ["pronunciar la h de honest", "decir zoo con /s/"], "Reconoce el sonido que mejoró y elige con la persona de tu casa el próximo que trabajarás."),
    "Ensaya tu presentación de la comida favorita frente a una persona de tu casa y mide el tiempo.",
    "Graba tu voz si puedes y compara el primer ensayo con el último; anota dos mejoras.",
)

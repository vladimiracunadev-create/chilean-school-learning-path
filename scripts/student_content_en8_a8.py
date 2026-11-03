"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 08 (presentación oral multimodal).

Todos los textos, esquemas y datos están escritos en cada ejercicio, con pista en español. Los datos numéricos son de ejemplo.
Las clases del plan tienen títulos genéricos; aquí cada clase trabaja un aspecto de la presentación que nombra el OA.
Los sonidos se practican con una persona de la casa; no hay audio.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA8 = "EN08 OA 08"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: audiencia, contexto y propósito
OPEN_KIDS = "«Hello, kids! Today I will show you three easy ways to help the planet. Look at my pictures!»"
OPEN_ADULTS = "«Good evening. Today I will present data about waste in our school and three proposals to reduce it.»"

lesson(
    OA8, 1,
    "Los comienzos de presentaciones escritos en cada ejercicio y lápiz.",
    "Aprenderé a tener conciencia de la audiencia, el contexto y el propósito al preparar una presentación oral. Sirve para elegir las palabras, el tono y los apoyos que mejor funcionan para quien me escucha.",
    ["Sé presentar información simple en inglés.", "Conozco los saludos y las palabras today y I will."],
    [
        "Antes de presentar, hazte tres preguntas. ¿Quién me escucha? Es la audiencia (audience): niños pequeños, compañeros, profesores o apoderados. ¿Dónde y cuándo presento? Es el contexto (context): una sala, un auditorio o una videollamada. ¿Para qué presento? Es el propósito (purpose): informar, explicar, convencer o entretener. Las respuestas cambian lo que dices y cómo lo dices.",
        "Con una audiencia de niños pequeños, usa frases cortas, palabras sencillas, imágenes y un tono alegre: «Look at my pictures!». Con adultos, usa un tono más formal, datos y términos precisos: «I will present data about waste». El contexto también importa: en un auditorio grande hablas más fuerte y más lento; en una sala pequeña, puedes acercarte a los oyentes.",
        "El propósito define la estructura. Para informar, presenta hechos. Para convencer, agrega razones y una petición final. Para entretener, usa una historia. Un error común es preparar la misma presentación para todos. Ajusta el vocabulario, la longitud y los apoyos a la audiencia, y recuerda que la comprensión del oyente es lo más importante.",
    ],
    [("audience", "audiencia: quienes escuchan"), ("context", "contexto: lugar y situación"), ("purpose", "propósito: para qué presento"), ("formal", "formal: cuidadoso y respetuoso"), ("tone", "tono: la manera de hablar"), ("persuade", "convencer")],
    [
        ("Reconocer la audiencia", "Presentación: " + OPEN_KIDS + " (planet = planeta, easy = fáciles). ¿A qué audiencia se dirige?", ["Veo kids, que significa niños.", "También usa Look at my pictures!, un recurso para atraer a los pequeños.", "La audiencia son niños."], "A niños pequeños"),
        ("Reconocer el propósito", "Presentación: " + OPEN_ADULTS + " (waste = residuos, proposals = propuestas, reduce = reducir). ¿Cuál es el propósito?", ["Dice present data, o sea, presentar datos.", "También habla de proposals.", "Informa y propone soluciones."], "Informar con datos y proponer soluciones"),
    ],
    [
        ("Usar el mismo texto para niños y adultos.", "No se piensa en la audiencia.", "Adapta palabras, tono y apoyos a quién escucha."),
        ("Usar palabras difíciles con niños pequeños.", "Se olvida su nivel.", "Elige palabras sencillas y frases cortas."),
    ],
    [
        # rec
        ("Presentación: " + OPEN_KIDS + " ¿Qué usa para atraer a los niños? a) imágenes b) cifras complejas", "a) imágenes", "Dice Look at my pictures."),
        ("Presentación: " + OPEN_ADULTS + " ¿Qué presentará? a) datos y propuestas b) un cuento", "a) datos y propuestas", "Dice present data… and three proposals."),
        ("¿Quién es la audiencia en una presentación? a) quienes escuchan b) quien presenta", "a) quienes escuchan", "Audience significa audiencia."),
    ],
    [
        # und
        ("Vas a presentar ante estudiantes de 1.º básico sobre los animales. ¿Qué frase eliges? a) Look, a big cat! b) The feline has carnivorous habits.", "a) Look, a big cat!", "Es corta y sencilla."),
        ("Vas a presentar ante el director sobre un proyecto. ¿Qué frase eliges? a) Good morning. I will present our project. b) Hi, guys! Look at this!", "a) Good morning. I will present our project.", "Es un tono formal adecuado."),
        ("¿Qué propósito tiene una presentación que termina con «Please recycle!»? a) convencer b) contar un cuento", "a) convencer", "La petición final busca que la audiencia actúe."),
    ],
    [
        # app
        ("Audiencia: niños de 5.º básico. Tema: reciclaje. ¿Qué apoyo es mejor? a) fotos de contenedores de colores b) una tabla de 50 cifras", "a) fotos de contenedores de colores", "Las imágenes se entienden rápido."),
        ("Contexto: una sala pequeña con 10 personas. ¿Qué haces? a) hablo con voz clara y me acerco un poco b) grito como en un estadio", "a) hablo con voz clara y me acerco un poco", "La sala pequeña no necesita gritar."),
        ("Propósito: convencer a los apoderados de ahorrar energía. ¿Qué incluyes? a) razones y una petición final b) solo un dibujo", "a) razones y una petición final", "Convencer necesita argumentos."),
    ],
    [
        # rea
        ("Una compañera usa las mismas palabras difíciles para niños y adultos. ¿Qué debe hacer? a) adaptar su vocabulario a cada audiencia b) hablar más rápido", "a) adaptar su vocabulario a cada audiencia", "Cada audiencia necesita su nivel."),
        ("Un compañero presenta con una videollamada. ¿Qué cambia respecto de una sala? a) debe cuidar la cámara y el sonido b) no debe decir hola", "a) debe cuidar la cámara y el sonido", "El contexto cambia las condiciones."),
    ],
    [
        # cha
        ("¿Cuál es un saludo formal para presentar ante profesores? a) Good morning. Today I will present… b) Hi, guys! Look at this!", "a) Good morning. Today I will present…", "Good morning y I will present son formales."),
        ("¿Qué frase atrae a niños pequeños con imágenes? a) Look at my pictures! b) I will present data.", "a) Look at my pictures!", "Es una invitación sencilla y visual."),
    ],
    [
        # context
        ("Vas a explicar a niños de 3.º básico cómo cuidar el agua. ¿Cuál es la mejor idea? a) un dibujo de una llave cerrada y una frase corta b) un informe de 20 páginas", "a) un dibujo de una llave cerrada y una frase corta", "Lo visual y breve funciona con niños.")
    ],
    [
        # selfcheck
        ("¿Qué es la audiencia?", "Las personas que escuchan", "Es a quienes se dirige la presentación."),
        ("¿Qué es el contexto?", "El lugar y la situación de la presentación", "Cambia cómo se presenta."),
        ("¿Qué es el propósito?", "Para qué presento", "Informar, convencer o entretener."),
    ],
    task("Elige uno de estos temas para tu presentación: «the school garden» o «a hobby». Escribe en tu hoja la audiencia (niños, compañeros o profesores), el contexto, el propósito, una frase de saludo en inglés y un apoyo visual que usarías. Si no eliges ninguno, usa «how to recycle paper».", "Tema: the school garden. Audiencia: niños de 3.º. Contexto: la sala. Propósito: informar. Saludo: Hello, kids! Today I will show you our garden. Apoyo: una foto de las plantas.", ["indica audiencia, contexto y propósito", "escribe un saludo coherente con la audiencia", "elige un apoyo visual adecuado"], ["hoja con cinco respuestas", "nota del adulto"], ["usar un saludo formal con niños", "no elegir ningún apoyo"], "Reconoce lo que acertó y ayuda a revisar si el saludo coincide con la audiencia."),
    "Practica el mismo saludo ante una persona de tu casa dos veces: una como si hablaras a niños y otra a profesores.",
    "Escribe en español cómo cambia una presentación del mismo tema para un abuelo y para un niño de 6 años.",
)

# ---------------------------------------------------------------- clase 2: contenido y coherencia en la organización
HOBBY = "Plan de presentación «My hobby: skating». Parte A: «Hello, I am Daniela and my hobby is skating.» Parte B: «First, I will explain what I need: a skateboard, a helmet and knee pads.» Parte C: «Second, I will show three basic moves.» Parte D: «My cat is gray and likes fish.» Parte E: «In conclusion, skating is fun and good exercise. Thank you for listening.» (hobby = pasatiempo, skateboard = patineta, helmet = casco, knee pads = rodilleras, moves = movimientos, exercise = ejercicio)"

lesson(
    OA8, 2,
    "El plan de presentación escrito en cada ejercicio y lápiz.",
    "Aprenderé a mostrar que conozco el contenido y a organizar mis ideas de forma coherente, con introducción, desarrollo y cierre, y conectores como first, second y in conclusion. Sirve para que mi presentación sea clara y fácil de seguir.",
    ["Sé usar first, then y finally.", "Distingo la idea principal y los detalles."],
    [
        "Una presentación coherente (coherent) tiene tres partes. La introducción (introduction) saluda, dice el tema y anuncia qué vas a explicar: «Hello, I am Daniela and my hobby is skating». El desarrollo (body) explica las ideas principales con datos y ejemplos. El cierre (conclusion) resume y agradece: «In conclusion, skating is fun. Thank you for listening». Si falta una parte, la audiencia se pierde.",
        "Todas las ideas del desarrollo deben tratar del tema. Una idea que no corresponde, como «My cat is gray», rompe la coherencia. Los conectores (connectors) ordenan: first (primero), second (segundo), next (luego), finally (por último) y in conclusion (para concluir). También sirven also (además), so (así que) y because (porque).",
        "Para demostrar que conoces el contenido, usa datos precisos y ejemplos reales. No lo leas todo: usa palabras clave en tu apoyo y explica con tus palabras. Antes de presentar, revisa tu plan con una lista: ¿tiene introducción?, ¿cada idea es del tema?, ¿usa conectores?, ¿cierra con una conclusión? Si respondes sí a las cuatro, tu organización es coherente.",
    ],
    [("introduction", "introducción"), ("body", "desarrollo"), ("conclusion", "conclusión"), ("coherent", "coherente: las ideas se relacionan"), ("connector", "conector"), ("topic", "tema")],
    [
        ("Reconocer la introducción", READ + HOBBY + " ¿Cuál es la parte que funciona como introducción?", ["Busco el saludo y el tema.", "La parte A dice Hello, I am Daniela and my hobby is skating.", "Esa parte presenta a la persona y el tema."], "La parte A"),
        ("Detectar una idea fuera de tema", READ + HOBBY + " ¿Qué parte no corresponde al tema?", ["Reviso cada parte.", "La parte D habla de un gato.", "No tiene relación con el patinaje."], "La parte D"),
    ],
    [
        ("Incluir ideas que no son del tema.", "Se agrega información sin pensar en el objetivo.", "Revisa que cada idea responda al tema."),
        ("Terminar sin conclusión.", "Se corta la presentación de golpe.", "Cierra con un resumen y un agradecimiento."),
    ],
    [
        # rec
        (READ + HOBBY + " ¿Cuál es el pasatiempo de Daniela? a) patinar b) cocinar", "a) patinar", "La parte A dice my hobby is skating."),
        (READ + HOBBY + " ¿Qué parte es la conclusión? a) la parte E b) la parte C", "a) la parte E", "Empieza con In conclusion."),
        (READ + HOBBY + " ¿Qué conector usa para la segunda idea? a) Second b) Finally", "a) Second", "La parte C empieza con Second."),
    ],
    [
        # und
        (READ + HOBBY + " ¿Qué necesita Daniela para patinar? a) patineta, casco y rodilleras b) bicicleta y guantes", "a) patineta, casco y rodilleras", "La parte B lo explica."),
        (READ + HOBBY + " ¿Cuántos movimientos básicos mostrará? a) tres b) cinco", "a) tres", "La parte C dice three basic moves."),
        (READ + HOBBY + " ¿Qué dice para cerrar? a) Thank you for listening b) See you tomorrow", "a) Thank you for listening", "Es la frase de cierre."),
    ],
    [
        # app
        (READ + HOBBY + " Ordena las partes que sí corresponden: A) conclusion B) introduction C) first idea D) second idea.", "B, C, D, A", "El orden es introducción, ideas y conclusión."),
        ("Completa: «___, I will explain the rules. Second, I will show the moves». Elige: First / Finally.", "First", "La segunda idea sigue a la primera."),
        (READ + HOBBY + " Cuenta cuántas partes del plan son coherentes con el tema.", "4", "Son A, B, C y E; la parte D no corresponde."),
    ],
    [
        # rea
        (READ + HOBBY + " Una compañera quita la parte D. ¿Qué mejora? a) la coherencia b) el largo", "a) la coherencia", "Se elimina una idea fuera de tema."),
        ("Un estudiante empieza la presentación con la conclusión. ¿Qué problema hay? a) el orden no es coherente b) habla muy bajo", "a) el orden no es coherente", "La conclusión va al final."),
    ],
    [
        # cha
        ("¿Qué frase anuncia tres ideas en la introducción? a) In this presentation, I will talk about three ideas b) Thank you for listening", "a) In this presentation, I will talk about three ideas", "Anuncia el contenido de la presentación."),
        ("Escribe un conector para añadir una idea: Also / Because.", "Also", "Also significa además y suma ideas."),
    ],
    [
        # context
        ("Vas a presentar «My family». Plan: A) Hello, this is my family. B) My mother is a nurse. C) My dog is brown. D) In conclusion, I love my family. ¿Qué parte puede quedar fuera si el tema es solo personas? a) la parte C b) la parte B", "a) la parte C", "Un perro no es persona.")
    ],
    [
        # selfcheck
        ("¿Cuántas partes tiene una presentación coherente?", "Tres: introducción, desarrollo y conclusión", "Cada una cumple una función."),
        ("¿Qué significa «in conclusion»?", "Para concluir", "Anuncia el cierre."),
        ("¿Qué haces con una idea fuera de tema?", "La quito", "Rompe la coherencia."),
    ],
    task("Elige un tema (a hobby, my favorite place o a sport). Con una hoja, escribe un plan de presentación con cinco partes: saludo y tema, dos ideas, un ejemplo y una conclusión. Usa al menos tres conectores (first, second, finally o in conclusion). Marca con rojo cualquier idea que no sea del tema. Si no eliges tema, usa «my favorite place».", "Plan: Hello, my favorite place is the beach. First, it is big and clean. Second, I swim there. For example, last summer I swam every day. In conclusion, the beach is relaxing. Thank you.", ["incluye introducción, desarrollo y conclusión", "usa al menos tres conectores", "todas las ideas son del tema"], ["hoja con plan", "nota del adulto"], ["incluir ideas fuera de tema", "no tener conclusión"], "Reconoce lo que acertó y ayuda a quitar las ideas que no pertenecen al tema."),
    "Presenta tu plan a una persona de tu casa usando solo palabras clave.",
    "Escribe en español cómo sabes si una idea de tu presentación pertenece o no al tema.",
)

# ---------------------------------------------------------------- clase 3: recursos multimodales
SLIDE = "Diapositiva A, con una frase larga de 40 palabras en letra pequeña. Diapositiva B, con una foto grande de un parque y tres palabras clave: «park, trees, benches». Diapositiva C, con 12 viñetas de texto. (trees = árboles, benches = bancas)"

lesson(
    OA8, 3,
    "Las descripciones de diapositivas y de recursos escritas en cada ejercicio y lápiz.",
    "Aprenderé a usar recursos multimodales (imágenes, gráficos, gestos, objetos y diapositivas) que refuercen el mensaje de forma creativa. Sirve para que mi audiencia entienda mejor y recuerde lo que presento.",
    ["Sé que las imágenes ayudan a explicar.", "Conozco palabras clave de un tema."],
    [
        "Un recurso multimodal (multimodal resource) es cualquier apoyo que usa más de un canal: lo que se ve, lo que se oye y lo que se hace. Una foto muestra cómo es algo. Un gráfico de barras compara cantidades. Un mapa ubica lugares. Una línea de tiempo (timeline) ordena hechos. Un objeto real se puede mostrar. Los gestos (gestures), como abrir los brazos para mostrar «big», refuerzan lo que dices.",
        "Elige el recurso según el mensaje. Si comparas cantidades, un gráfico. Si describes un lugar, una foto o un mapa. Si explicas pasos, un dibujo con números. Si cuentas una historia en orden, una línea de tiempo. Los recursos deben reforzar lo que dices, no repetirlo palabra por palabra ni distraer. En una diapositiva, usa pocas palabras clave y letra grande.",
        "La creatividad (creativity) ayuda: un cartel hecho a mano, un objeto de tu casa, un título llamativo. Pero la claridad va primero. Una buena diapositiva se lee en cinco segundos. Si la audiencia debe leer mucho, deja de escucharte. Practica con tus recursos antes: saber dónde está cada imagen evita pausas largas.",
    ],
    [("multimodal", "con varios canales: imagen, sonido, gesto"), ("slide", "diapositiva"), ("graph", "gráfico"), ("timeline", "línea de tiempo"), ("gesture", "gesto"), ("creativity", "creatividad")],
    [
        ("Elegir la mejor diapositiva", READ + SLIDE + " ¿Qué diapositiva es mejor para presentar un parque?", ["Comparo las tres.", "La B tiene foto grande y tres palabras clave.", "Es clara y se lee rápido."], "La diapositiva B"),
        ("Elegir un recurso", "Mensaje: compararás cuántos estudiantes hay en tres cursos. ¿Qué recurso eliges? Elige: un gráfico de barras / un mapa.", ["Comparar cantidades se ve bien en barras.", "El mapa sirve para ubicar lugares.", "El mejor recurso es el gráfico."], "Un gráfico de barras"),
    ],
    [
        ("Llenar la diapositiva de texto y leerla.", "Se cree que más texto es mejor.", "Usa pocas palabras clave y tu voz explica el resto."),
        ("Usar una imagen que no tiene relación con el mensaje.", "Se elige por decoración.", "Elige imágenes que refuercen lo que dices."),
    ],
    [
        # rec
        ("Quieres mostrar dónde queda una ciudad. ¿Qué recurso usas? a) un mapa b) un gráfico de barras", "a) un mapa", "El mapa ubica lugares."),
        ("Quieres mostrar hechos en orden. ¿Qué recurso usas? a) una línea de tiempo b) una foto", "a) una línea de tiempo", "La línea ordena hechos."),
        ("Quieres mostrar el tamaño «big» con las manos. ¿Qué recurso usas? a) un gesto b) un gráfico", "a) un gesto", "Abrir los brazos refuerza la palabra."),
    ],
    [
        # und
        (READ + SLIDE + " ¿Por qué la diapositiva C no es buena? a) tiene demasiado texto b) tiene una foto", "a) tiene demasiado texto", "Doce viñetas se leen con dificultad."),
        (READ + SLIDE + " ¿Qué palabras clave tiene la B? a) park, trees, benches b) market, shoes, bags", "a) park, trees, benches", "Describe el parque."),
        ("¿Qué recurso sirve para comparar cantidades? a) un gráfico b) un dibujo del cielo", "a) un gráfico", "Permite ver las diferencias."),
    ],
    [
        # app
        ("Presentas «How to wash hands». ¿Qué recurso eliges? a) dibujos numerados de los pasos b) un mapa de Chile", "a) dibujos numerados de los pasos", "Los pasos se entienden con imágenes en orden."),
        ("Presentas «My trip to the south». ¿Qué recurso eliges? a) fotos y un mapa b) una receta", "a) fotos y un mapa", "Muestran el lugar."),
        arith("Presentas «Our class pets». Datos de ejemplo: 12 estudiantes tienen perros, 8 gatos y 4 peces. ¿Cuántas mascotas hay en total?", "12+8+4", "Se suman las mascotas de cada tipo."),
    ],
    [
        # rea
        ("Un compañero lee la diapositiva palabra por palabra. ¿Qué le recomiendas? a) usar palabras clave y explicar con su voz b) leer más rápido", "a) usar palabras clave y explicar con su voz", "Así mantiene la atención."),
        ("¿Qué recurso refuerza «the box is very heavy»? a) mostrar una caja y gestos de esfuerzo b) mostrar un mapa", "a) mostrar una caja y gestos de esfuerzo", "Muestra lo que significa heavy."),
    ],
    [
        # cha
        ("Dibujas una línea de tiempo con tres hechos de tu año escolar. ¿Qué orden usas? a) del más antiguo al más reciente b) al azar", "a) del más antiguo al más reciente", "Una línea de tiempo sigue el orden del tiempo."),
        ("¿Cuál es una palabra clave para una diapositiva sobre el mar? a) sea b) keyboard", "a) sea", "Sea significa mar."),
    ],
    [
        # context
        ("Vas a presentar ante 5.º básico sobre insectos. ¿Qué recurso crea más interés? a) mostrar un dibujo grande de una abeja con la palabra bee b) leer una lista de nombres", "a) mostrar un dibujo grande de una abeja con la palabra bee", "Lo visual atrae a los pequeños.")
    ],
    [
        # selfcheck
        ("¿Qué es un recurso multimodal?", "Un apoyo con imagen, sonido o gesto", "Refuerza el mensaje."),
        ("¿Cuántas palabras debe tener una buena diapositiva?", "Pocas, solo las clave", "Se lee en pocos segundos."),
        ("¿Qué recurso sirve para comparar?", "Un gráfico", "Muestra diferencias de cantidades."),
    ],
    task("Elige un tema (my pet, my school o a recipe). Escribe en tu hoja el mensaje que quieres comunicar, tres palabras clave para una diapositiva, un recurso visual que usarías y un gesto que reforzaría tu mensaje. Si no eliges, usa «my school».", "Mensaje: my school is friendly. Palabras clave: school, teachers, friends. Recurso: una foto del patio. Gesto: abrir los brazos para decir big.", ["escribe un mensaje claro", "elige tres palabras clave", "elige un recurso y un gesto coherentes"], ["hoja con mensaje, palabras, recurso y gesto", "nota del adulto"], ["elegir un recurso que no se relaciona con el mensaje", "escribir demasiado texto"], "Reconoce lo que acertó y ayuda a reducir el texto de la diapositiva."),
    "Haz un dibujo de una diapositiva con una imagen y tres palabras clave y muéstrala a una persona de tu casa.",
    "Escribe en español qué recurso te resulta más útil para presentar y por qué.",
)

# ---------------------------------------------------------------- clase 4: funciones del lenguaje y vocabulario temático
PARK = "«Torres del Paine is a national park in the south of Chile. It has high mountains, blue lakes and big glaciers. The park receives about three hundred thousand visitors every year (example data). First, tourists walk along the trails. Then they take photos of the views. In my opinion, it is the most beautiful place in Chile.» (national park = parque nacional, lakes = lagos, glaciers = glaciares, receives = recibe, visitors = visitantes, trails = senderos, views = vistas)"

lesson(
    OA8, 4,
    "El texto de presentación escrito en cada ejercicio y lápiz.",
    "Aprenderé a usar las funciones del lenguaje del año, el vocabulario temático y expresiones de uso común en una presentación: describir, expresar cantidades, ordenar con first y then, y opinar. Sirve para que mi presentación sea precisa y natural.",
    ["Sé describir lugares con adjetivos.", "Conozco first, then y In my opinion."],
    [
        "En una presentación usas varias funciones del lenguaje (language functions). Describir: «It has high mountains and blue lakes». Expresar cantidades: «about three hundred thousand visitors». Ordenar acciones: «First, tourists walk. Then they take photos». Opinar: «In my opinion, it is the most beautiful place». Dar información adicional: «The park, which is in the south, is huge».",
        "El vocabulario temático (thematic vocabulary) son las palabras propias del tema. Para un parque: mountains, lakes, trails, views, visitors. Para una receta: ingredients, bowl, stir. Antes de presentar, haz una lista de diez palabras de tu tema. Las expresiones de uso común (common expressions) ayudan a hablar con naturalidad: «As you can see», «Let me show you», «For example», «Thank you for listening».",
        "Para sonar natural, combina las funciones con conectores y expresiones. Evita traducir palabra por palabra desde el español. Si dudas de una palabra, usa otra que conozcas: si no recuerdas «glacier», di «a big ice mountain». Siempre revisa que las cifras sean exactas y que las opiniones tengan una razón.",
    ],
    [("language function", "función del lenguaje: lo que haces al hablar"), ("thematic vocabulary", "vocabulario del tema"), ("As you can see", "como pueden ver"), ("Let me show you", "déjenme mostrarles"), ("For example", "por ejemplo"), ("visitors", "visitantes")],
    [
        ("Reconocer una función", READ + PARK + " «It has high mountains, blue lakes and big glaciers» ¿qué función cumple?", ["La frase dice cómo es el parque.", "Usa adjetivos como high, blue y big.", "Es una descripción."], "Describir"),
        ("Reconocer una cantidad", READ + PARK + " ¿Qué cantidad se menciona?", ["Busco un número.", "Dice about three hundred thousand visitors.", "Es 300.000 visitantes o más."], "Unos 300.000 visitantes al año (dato de ejemplo)"),
    ],
    [
        ("Traducir «tengo catorce años» como «I have fourteen years».", "Se traduce palabra por palabra.", "Se dice I am fourteen years old."),
        ("No usar vocabulario del tema.", "Se hablan en general.", "Prepara una lista de palabras clave del tema antes de presentar."),
    ],
    [
        # rec
        (READ + PARK + " ¿Dónde está el parque? a) en el sur de Chile b) en el norte de Chile", "a) en el sur de Chile", "El texto dice in the south of Chile."),
        (READ + PARK + " ¿Qué hacen primero los turistas? a) caminan por los senderos b) sacan fotos", "a) caminan por los senderos", "Dice First, tourists walk along the trails."),
        (READ + PARK + " ¿Qué opinión se da? a) que es el lugar más hermoso de Chile b) que es el lugar más caro", "a) que es el lugar más hermoso de Chile", "Dice In my opinion, it is the most beautiful place."),
    ],
    [
        # und
        (READ + PARK + " ¿Qué función tiene «In my opinion»? a) opinar b) contar cantidades", "a) opinar", "Introduce un punto de vista."),
        ("¿Qué expresión sirve para mostrar una imagen? a) Let me show you b) Thank you for listening", "a) Let me show you", "Introduce un recurso visual."),
        ("¿Qué expresión sirve para ejemplificar? a) For example b) In conclusion", "a) For example", "Presenta un ejemplo."),
    ],
    [
        # app
        (READ + PARK + " Completa: «The park has high ___». Elige: mountains / kitchens.", "mountains", "Es parte del vocabulario del parque."),
        (READ + PARK + " Completa: «Tourists walk first and ___ take photos». Elige: then / because.", "then", "Then marca el orden de las acciones."),
        arith(READ + PARK + " Si el parque recibe 300.000 visitantes al año, ¿cuántos recibe en dos años si la cifra es constante?", "300000*2", "Se duplica la cifra de un año."),
    ],
    [
        # rea
        ("Dices «I have fifteen years». ¿Cuál es la forma correcta? a) I am fifteen years old b) I have fifteen age", "a) I am fifteen years old", "En inglés la edad se dice con to be."),
        (READ + PARK + " ¿Qué vocabulario del tema aparece? a) mountains, lakes y trails b) kitchen, bed y sofa", "a) mountains, lakes y trails", "Son palabras del parque."),
    ],
    [
        # cha
        ("¿Qué expresión significa «como pueden ver»? a) As you can see b) For example", "a) As you can see", "Introduce algo que se muestra."),
        ("¿Cómo se dice «unos trescientos mil visitantes»? a) about three hundred thousand visitors b) about three hundred thousands visitors", "a) about three hundred thousand visitors", "Thousand no lleva -s después de un número."),
    ],
    [
        # context
        ("Presentas una receta. ¿Qué vocabulario necesitas? a) bowl, spoon y mix b) mountains, lakes y trails", "a) bowl, spoon y mix", "Son palabras del tema de cocina.")
    ],
    [
        # selfcheck
        ("¿Qué es el vocabulario temático?", "Las palabras propias del tema", "Hacen más precisa la presentación."),
        ("¿Qué expresión usas para mostrar algo?", "Let me show you", "Introduce un recurso."),
        ("¿Cómo se dice la edad en inglés?", "I am … years old", "Se usa to be."),
    ],
    task("Elige un tema (my city, a sport o a food). Escribe en tu hoja una introducción de tres oraciones: una descripción, una cantidad y una opinión con In my opinion, usando también diez palabras de vocabulario del tema. Si no eliges, usa «my city».", "My city is big and clean. It has two hundred thousand inhabitants. In my opinion, it is a nice place to live. Vocabulario: street, park, square, school, bus, river, market, mountain, beach, library.", ["incluye descripción, cantidad y opinión", "usa In my opinion", "lista diez palabras del tema"], ["hoja con introducción y lista", "nota del adulto"], ["traducir palabra por palabra", "dar una cantidad sin sentido"], "Reconoce lo que acertó y ayuda a mejorar cada oración con vocabulario del tema."),
    "Ensaya tu introducción ante una persona de tu casa usando As you can see.",
    "Escribe en español tres expresiones de uso común que te gustaría usar al presentar.",
)

# ---------------------------------------------------------------- clase 5: sonidos del idioma y revisión final
SOUND = "Sonidos de la clase: /θ/ (sin voz, lengua entre los dientes): thirty, Thursday, thousand, month, mouth. /ð/ (con voz): that, they, brother, together, weather. /w/ (labios redondeados): window, winter, world, why. /r/ (sin vibrar): rice, river, read, really. Terminaciones de verbos regulares en pasado: /t/ después de p, k, f, s, sh, ch (jumped, cooked, danced, washed), /d/ en los demás casos (opened, called, enjoyed) y /ɪd/ después de t o d (waited, painted, needed)."

lesson(
    OA8, 5,
    "Las listas de palabras y la rúbrica escritas en cada ejercicio y lápiz.",
    "Aprenderé a usar los sonidos /ð/, /θ/, /w/, /r/ y las terminaciones /d/, /t/ e /ɪd/ en mi presentación, y a revisar mi desempeño con una rúbrica. Sirve para que me entiendan mejor y para mejorar con mi propia revisión.",
    ["Sé que -ed forma el pasado de verbos regulares.", "Conozco las partes de una presentación."],
    [
        SOUND,
        "Para practicar, repite en voz alta con una persona de tu casa. Pon la lengua entre los dientes para /θ/ y /ð/; para /w/ redondea los labios; para /r/ levanta la lengua sin tocar el paladar. En los verbos en pasado, no leas la -ed como una sílaba extra salvo después de t o d: walked suena /wɔːkt/, no /wɔːkɪd/. Si dudas de la pronunciación, pregúntale a tu profesor o consulta un diccionario con sonido.",
        "Una rúbrica (rubric) es una lista de criterios con puntos. Puedes usarla para revisar tu presentación: contenido, organización, lenguaje, sonidos y conciencia de la audiencia. Cada criterio vale de 1 a 4 puntos. Sumar los puntos muestra qué mejorar. Al terminar, escribe una meta: «Next time, I will practice /θ/ in thirty and Thursday».",
    ],
    [("rubric", "rúbrica: criterios con puntos"), ("pronunciation", "pronunciación"), ("sound", "sonido"), ("goal", "meta"), ("rehearse", "ensayar"), ("self-assessment", "autoevaluación")],
    [
        ("Clasificar un sonido", "La palabra «thirty» ¿empieza con /θ/ o con /ð/?", ["En thirty, th se dice sin voz.", "El sonido sin voz es /θ/.", "Thirty empieza con /θ/."], "/θ/"),
        ("Clasificar -ed", "El verbo «jumped» ¿termina con /t/, /d/ o /ɪd/?", ["La letra antes de -ed es p.", "Después de p, -ed suena /t/.", "Jumped termina con /t/."], "/t/"),
    ],
    [
        ("Pronunciar /w/ como «gu» del español.", "Se transfiere un sonido del español.", "Redondea los labios y suelta el aire: window."),
        ("Leer -ed como sílaba extra en walked.", "Se lee la letra, no el sonido.", "Solo suena /ɪd/ después de t o d."),
    ],
    [
        # rec
        ("¿Con qué sonido empieza «that»? a) /ð/ b) /θ/", "a) /ð/", "En that, th tiene voz."),
        ("¿Con qué sonido empieza «river»? a) /r/ b) /w/", "a) /r/", "River empieza con r."),
        ("¿Con qué sonido empieza «window»? a) /w/ b) /r/", "a) /w/", "Window empieza con w."),
    ],
    [
        # und
        ("¿Qué terminación tiene «enjoyed»? a) /d/ b) /ɪd/", "a) /d/", "Después de y suena /d/."),
        ("¿Qué terminación tiene «painted»? a) /ɪd/ b) /t/", "a) /ɪd/", "Después de t suena /ɪd/."),
        ("¿Qué terminación tiene «danced»? a) /t/ b) /d/", "a) /t/", "Después de s suena /t/."),
    ],
    [
        # app
        ("Une cada palabra con el sonido de su th o de su w. 1) Thursday (th) 2) brother (th) 3) world (w). Sonidos: a) /θ/ b) /ð/ c) /w/", "1-a, 2-b, 3-c", "Thursday tiene /θ/ sin voz, brother tiene /ð/ con voz y world empieza con /w/."),
        ("Clasifica por terminación. 1) cooked 2) opened 3) needed. Terminaciones: a) /t/ b) /d/ c) /ɪd/", "1-a, 2-b, 3-c", "Después de k es /t/; tras n es /d/; tras d es /ɪd/."),
        ("Palabra: «together». ¿Cuál es el sonido de la th? a) /ð/ b) /θ/", "a) /ð/", "En together, th suena con voz."),
    ],
    [
        # rea
        ("Una compañera dice «wanted» con -ed como /t/. ¿Qué debe corregir? a) debe decir /ɪd/ porque termina en t b) debe decir /d/", "a) debe decir /ɪd/ porque termina en t", "Después de t o d, -ed suena /ɪd/."),
        ("Una compañera dice «thirty» como «sirty». ¿Qué sonido cambió? a) /θ/ por /s/ b) /r/ por /l/", "a) /θ/ por /s/", "Falta poner la lengua entre los dientes."),
    ],
    [
        # cha
        arith("Rúbrica de ejemplo: contenido 3 puntos, organización 4, lenguaje 3, sonidos 2, audiencia 4. ¿Cuántos puntos suma en total?", "3+4+3+2+4", "Se suman los puntos de los cinco criterios."),
        ("Con esa rúbrica, ¿qué criterio tiene menos puntos y debe mejorar? a) sonidos b) contenido", "a) sonidos", "Tiene 2 puntos."),
    ],
    [
        # context
        ("Antes de presentar, practicas cuatro palabras: thirty, that, window y river. ¿Cuántos sonidos distintos hay al inicio: /θ/, /ð/, /w/ y /r/?", "4", "Cada palabra empieza con un sonido distinto.")
    ],
    [
        # selfcheck
        ("¿Dónde pones la lengua para /θ/?", "Entre los dientes", "Soplas aire sin voz."),
        ("¿Cuándo suena /ɪd/ en -ed?", "Después de t o d", "Forma una sílaba más."),
        ("¿Para qué sirve una rúbrica?", "Para revisar mi desempeño con criterios", "Muestra qué mejorar."),
    ],
    task("Con una persona de tu casa, ensaya en voz alta estas seis palabras: «thirty, brother, window, river, jumped, painted». Marca en tu hoja el sonido de cada una (/θ/, /ð/, /w/, /r/, /t/ o /ɪd/) y completa una rúbrica de 5 criterios con puntos de 1 a 4. Escribe una meta con Next time, I will…", "thirty /θ/, brother /ð/, window /w/, river /r/, jumped /t/, painted /ɪd/. Rúbrica: contenido 3, organización 3, lenguaje 3, sonidos 2, audiencia 3 (total 14). Meta: Next time, I will practice /θ/.", ["marca correctamente los seis sonidos", "completa la rúbrica con puntos", "escribe una meta concreta"], ["hoja con sonidos, rúbrica y meta", "nota de la persona"], ["confundir /θ/ y /ð/", "no escribir una meta"], "Reconoce lo que acertó y ensaya con la persona solo los dos sonidos más difíciles."),
    "Graba tu voz o pide a una persona que te escuche decir las seis palabras tres veces cada una.",
    "Escribe en español qué sonido te cuesta más y cómo lo practicarías esta semana.",
)

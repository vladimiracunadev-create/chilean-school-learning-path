"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 05: presentación oral multimodal coherente para una audiencia.

Las clases del plan son genéricas; aquí se aplican a: audiencia y propósito, organización coherente y contenido, recursos
multimodales, lenguaje y sonidos del nivel (con notas de dos compañeros) y planificación y autoevaluación. Los datos de las
tablas son «de ejemplo». Todo lo que se pregunta está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 05"
MAT = "Los textos, tablas y notas escritos en cada ejercicio, lápiz, una hoja para planificar y, si quieres, una persona de tu casa como audiencia."


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ clase 1: audiencia, contexto y propósito
lesson(
    OA, 1, MAT,
    "Aprenderé a pensar en quién escucha mi presentación, dónde la daré y para qué, y a elegir un saludo, un propósito y un cierre adecuados. Sirve para que mi mensaje llegue a la audiencia.",
    ["Sé saludar y presentarme en inglés.", "Conozco verbos como explain, show y tell."],
    [
        "Una presentación oral (oral presentation) siempre tiene una audiencia (audience): las personas que escuchan. Tu audiencia cambia lo que dices y cómo lo dices. Ante niños pequeños usas palabras simples y ejemplos cotidianos. Ante una autoridad usas un saludo formal, como Good morning, Mrs Rojas, y un tono respetuoso. Ante tus compañeros puedes ser más cercano, pero sin lenguaje descuidado.",
        "El contexto (context) es la situación: dónde, cuándo y cuánto tiempo tienes. En dos minutos conviene preparar dos o tres ideas, no diez. El propósito (purpose) es lo que quieres lograr: explicar (I will explain), mostrar (I'd like to show you), contar (Let me tell you about...) o convencer (I would like to convince you that...). El propósito se dice con claridad al comienzo.",
        "Para planificar, responde tres preguntas: ¿quiénes escuchan?, ¿en qué situación?, ¿para qué hablo? Luego elige el saludo, el vocabulario y el cierre. Un cierre fuerte repite la idea principal y agradece: Thank you for listening. Si tu propósito es convencer, agrega una petición clara, como Please vote for the new recycling point.",
    ],
    [("audience", "audiencia: quienes escuchan"), ("context", "contexto: la situación de la presentación"), ("purpose", "propósito: lo que quiero lograr"), ("I'd like to show you...", "me gustaría mostrarte..."), ("Let me tell you about...", "déjame contarte sobre..."), ("Thank you for listening.", "Gracias por escuchar.")],
    [
        ("Adaptar a la audiencia", "Presentarás cómo cuidar una planta ante niños de ocho años. ¿Qué frase eliges? A) Plants need sun, water and air. B) Photosynthesis requires chlorophyll to transform carbon dioxide.", ["Pienso en la audiencia: niños de ocho años.", "Necesito palabras simples y conocidas.", "La frase A usa sun, water y air."], "A) Plants need sun, water and air."),
        ("Elegir un saludo formal", "Hablarás ante la directora en una reunión formal. ¿Qué saludo eliges? A) Good morning, Mrs Rojas. Thank you for your time. B) Hey, what's up? Listen!", ["La audiencia es una autoridad.", "El contexto es formal.", "El saludo A es respetuoso y claro."], "A) Good morning, Mrs Rojas. Thank you for your time."),
    ],
    [
        ("Usar el mismo lenguaje para todas las audiencias.", "Se piensa en el tema y no en quién escucha.", "Antes de escribir, responde quiénes escuchan, dónde y para qué."),
        ("Preparar demasiadas ideas para poco tiempo.", "Se cree que más información es mejor.", "Elige dos o tres ideas principales con un ejemplo cada una."),
    ],
    [
        ("Hablarás ante el alcalde en el aniversario del colegio. ¿Qué inicio es más adecuado? A) Good afternoon, Mr Soto. Thank you for coming. B) Hello, hello, can you hear me? Okay, okay.", "A) Good afternoon, Mr Soto. Thank you for coming.", "Es respetuoso y claro para una autoridad en un acto formal."),
        ("Un estudiante comienza: «Dear teachers, I would like to convince you that we need a recycling point in the patio.» ¿Cuál es su propósito? A) convencer B) contar una anécdota", "A) convencer", "Dice would like to convince you."),
        ("Tu audiencia son niños de seis años. ¿Qué ejemplo es más cercano? A) Rain is water that falls from the clouds. B) Precipitation is the condensation of atmospheric vapour.", "A) Rain is water that falls from the clouds.", "Usa palabras que conocen y una idea simple."),
    ],
    [
        ("«Good morning, everyone. Today I will explain how to take care of a plant.» ¿Cuál es el propósito? A) explicar B) vender plantas", "A) explicar", "I will explain anuncia el propósito."),
        ("«Let me tell you about the day I met a famous swimmer.» ¿Qué propósito tiene? A) contar una experiencia B) dar instrucciones", "A) contar una experiencia", "Let me tell you about... introduce un relato."),
        ("Tienes dos minutos para presentar. ¿Cuántas ideas principales conviene preparar? A) dos o tres B) diez", "A) dos o tres", "Con poco tiempo se explican pocas ideas con ejemplo."),
    ],
    [
        ("Hablarás en una reunión de madres, padres y apoderados. ¿Qué saludo eliges? A) Good evening, everyone. Thank you for coming. B) Hi, kids! Let's play!", "A) Good evening, everyone. Thank you for coming.", "El saludo se adapta a una audiencia adulta."),
        ("Tu propósito es mostrar tu proyecto de ciencias. ¿Qué frase usas al comienzo? A) I'd like to show you my science project. B) I would like to buy a science project.", "A) I'd like to show you my science project.", "Show es mostrar y coincide con el propósito."),
        ("Terminas una presentación para convencer. ¿Qué cierre es mejor? A) Please vote for the new recycling point. Thank you! B) That's all, I forgot the rest.", "A) Please vote for the new recycling point. Thank you!", "Repite la petición y agradece."),
    ],
    [
        ("Hay dos planes para hablar de seguridad en bicicleta ante niños de seis años. Plan 1: palabras simples, un dibujo de un casco y una rima corta. Plan 2: lenguaje técnico y estadísticas de accidentes. ¿Qué plan corresponde? A) el Plan 1 B) el Plan 2", "A) el Plan 1", "Se adapta a la edad con palabras simples y una imagen."),
        ("Tu propósito es convencer al curso de organizar una campaña, pero tu plan solo tiene datos y ninguna petición. ¿Qué falta? A) una petición clara al final, como Please join the campaign B) más saludos al inicio", "A) una petición clara al final, como Please join the campaign", "Para convencer se necesita una petición."),
    ],
    [
        ("Presentarás el mismo tema en la sala con imágenes y luego en una radio, sin imágenes. ¿Qué debes cambiar en la radio? A) describir con palabras lo que mostrabas en las imágenes B) hablar más rápido", "A) describir con palabras lo que mostrabas en las imágenes", "Sin imágenes, el mensaje visual debe pasar a la voz."),
        ("Un compañero dice «I'd like to inform you that the canteen opens at eight» y otro «I'd like to convince you that the canteen should open at seven». ¿Quién quiere persuadir? A) el segundo B) el primero", "A) el segundo", "Convince you that... busca cambiar la opinión o la acción."),
    ],
    [("Te invitan a hablar en una reunión de vecinos adultos sobre una campaña de limpieza. ¿Qué es lo más adecuado? A) saludar con Good evening, neighbours, explicar el propósito y usar vocabulario claro B) hablar solo con tus amigos del curso", "A) saludar con Good evening, neighbours, explicar el propósito y usar vocabulario claro", "Se adapta el saludo y el lenguaje a la audiencia y al contexto.")],
    [
        ("En Inglés de 1.º medio (OA 5, clase 1): ¿qué es la audiencia de una presentación?", "Las personas que escuchan", "Define cómo se adapta el mensaje."),
        ("En Inglés de 1.º medio (OA 5, clase 1): ¿qué es el propósito de una presentación?", "Lo que quieres lograr: explicar, mostrar, contar o convencer", "Se dice con claridad al inicio."),
        ("En Inglés de 1.º medio (OA 5, clase 1): ¿qué incluye un buen cierre?", "Repite la idea principal y agradece, y pide algo si se quiere convencer", "Cierra el mensaje."),
    ],
    task("Elige una opción. (a) Pedir a la directora instalar un bebedero en el patio. (b) Explicar a niños de siete años cómo cuidar una planta. Escribe en inglés tres frases: un saludo, una frase de propósito y un cierre adecuados a la audiencia de tu opción.", "Opción (a): Good morning, Mrs Rojas. Thank you for your time. / I would like to ask you to install a water fountain in the patio. / Thank you for listening. I hope you can help us.", ["el saludo corresponde a la audiencia", "la frase de propósito dice qué se quiere lograr", "el cierre agradece y, si corresponde, pide algo"], ["hoja con tres frases", "lectura en voz alta a una persona de tu casa"], ["usar un saludo informal con una autoridad", "no decir el propósito"], "Reconoce lo adecuado de cada frase y pide ajustar el saludo o el vocabulario si no calza con la audiencia."),
    "Escribe en español a quién le explicarías hoy un tema y cómo cambiarías tus palabras para esa persona.",
    "Escribe dos saludos distintos para la misma presentación: uno para niños y otro para una autoridad.",
)

# ------------------------------------------------------------------ clase 2: organización coherente y contenido
lesson(
    OA, 2, MAT,
    "Aprenderé a organizar una presentación en introducción, desarrollo y conclusión, a ordenar ideas con conectores y a usar datos correctos. Sirve para que mi presentación sea clara y creíble.",
    ["Sé el propósito y la audiencia de una presentación.", "Conozco conectores como first, then y finally."],
    [
        "Una presentación coherente tiene tres partes. La introducción (introduction) saluda, dice el tema y el propósito: Hello, everyone. I'll talk about my neighbourhood park. El desarrollo (body) presenta dos o tres ideas principales, cada una con un ejemplo o un dato. La conclusión (conclusion) resume y agradece: In conclusion, the park needs more trees. Thank you for listening.",
        "Los conectores (connectors) ordenan las ideas: First, Second y Also presentan ideas; For example introduce un ejemplo; However muestra un contraste; Finally o In conclusion cierran. La coherencia (coherence) significa que todas las ideas se relacionan con el tema. Una idea fuera de tema, como hablar de tu primo guitarrista en una charla sobre perros, rompe la coherencia.",
        "El conocimiento del contenido (content knowledge) se nota en datos correctos. Si una tabla dice que 12 estudiantes desayunan cereal y 5 fruta, no puedes decir que la fruta es lo más común. Antes de hablar, revisa cada dato con tu fuente y usa palabras como the most common, the biggest part y more than half con cuidado.",
    ],
    [("introduction / body / conclusion", "introducción / desarrollo / conclusión"), ("First, Second, Finally", "primero, segundo, finalmente"), ("For example", "por ejemplo"), ("the most common", "lo más común"), ("more than half", "más de la mitad"), ("coherence", "coherencia: todo se relaciona con el tema")],
    [
        ("Ordenar una presentación", "Ordena con letras estas frases de una presentación sobre dormir bien: (a) In conclusion, sleep helps us learn. (b) Good morning. Today I will talk about sleep. (c) First, sleep helps memory. (d) Second, sleep gives us energy.", ["La introducción es la que saluda y dice el tema: (b).", "El desarrollo usa First y Second: (c) y (d).", "La conclusión cierra: (a)."], "b, c, d, a"),
        ("Usar datos con cuidado", "Datos de ejemplo del reciclaje del curso: papel 40 kg, plástico 25 kg, latas 15 kg. ¿Es correcto decir The biggest part is paper?", ["Comparo los tres números.", "40 es mayor que 25 y que 15.", "Por eso paper es la parte más grande."], "Sí, el papel es la parte más grande"),
    ],
    [
        ("Incluir una idea que no tiene relación con el tema.", "Se agrega un dato interesante pero fuera de tema.", "Pregunta si cada idea apoya el tema y el propósito."),
        ("Afirmar algo que los datos no muestran.", "Se recuerda un número, no el conjunto de datos.", "Compara todos los datos antes de usar palabras como the most."),
    ],
    [
        ("¿Qué parte de una presentación contiene el saludo y el tema? A) la introducción B) la conclusión", "A) la introducción", "Ahí se dice quién habla y de qué."),
        ("¿Qué palabra abre una lista de ideas? A) First B) Finally", "A) First", "First introduce la primera idea; Finally cierra."),
        ("¿Qué frase pertenece a la conclusión? A) In conclusion, our park needs more trees. B) Hello, everyone, I'm Mario.", "A) In conclusion, our park needs more trees.", "In conclusion resume y cierra."),
    ],
    [
        ("Datos de ejemplo: desayuno de 30 estudiantes: cereal 12, pan con palta 10, fruta 5, nada 3. ¿Qué afirmación es correcta? A) The most common breakfast is cereal. B) The most common breakfast is fruit.", "A) The most common breakfast is cereal.", "Cereal tiene el número más alto: 12."),
        ("Ordena con letras las frases de una presentación sobre el parque del barrio: (a) Finally, the park needs more trees. (b) Hello, everyone. I'll talk about my neighbourhood park. (c) First, the park has a playground. (d) Second, many families go there on weekends. (e) Thank you for listening.", "b, c, d, a, e", "Introducción, dos ideas con First y Second, idea final y cierre."),
        ("En una charla sobre perros, un estudiante dice: «Dogs need food, water and walks. Also, my cousin plays the guitar. Finally, dogs need love.» ¿Qué frase rompe la coherencia? A) Also, my cousin plays the guitar. B) Dogs need food, water and walks.", "A) Also, my cousin plays the guitar.", "No se relaciona con el tema de los perros."),
    ],
    [
        arith("Con los datos de ejemplo del desayuno (cereal 12, pan con palta 10, fruta 5, nada 3), ¿cuántos de los 30 estudiantes desayunan algo?", "30-3", "A 30 estudiantes se les quitan los 3 que no desayunan.", " estudiantes"),
        arith("Con esos mismos datos (cereal 12, pan con palta 10), ¿cuántos estudiantes desayunan cereal o pan con palta?", "12+10", "Se suman los dos grupos.", " estudiantes"),
        ("Completa: «___, the park needs more trees.» Es la última idea de la lista. A) Finally B) First", "A) Finally", "Finally marca la última idea."),
    ],
    [
        ("Un compañero dice «Five students eat fruit, so fruit is the most common breakfast». Los datos de ejemplo son cereal 12, pan con palta 10, fruta 5, nada 3. ¿Es coherente? A) no: 5 es menos que 12 y que 10 B) sí: 5 es un número importante", "A) no: 5 es menos que 12 y que 10", "La afirmación contradice los datos."),
        ("En una presentación sobre el parque, ¿qué idea va antes de In conclusion? A) un argumento con ejemplo, como Second, many families go there B) el saludo inicial", "A) un argumento con ejemplo, como Second, many families go there", "El desarrollo va entre la introducción y la conclusión."),
    ],
    [
        ("Datos de ejemplo del reciclaje del curso: papel 32 kg, plástico 18 kg, latas 10 kg. ¿Qué frase es correcta? A) Paper is more than half of the total. B) Cans are the biggest part.", "A) Paper is more than half of the total.", "El total es 60 kg y 32 es más que 30."),
        arith("Con esos datos (papel 32 kg, plástico 18 kg, latas 10 kg), ¿cuántos kilos recicló el curso en total?", "32+18+10", "Se suman las tres cantidades.", " kg"),
    ],
    [("Preparas una charla de dos minutos sobre cómo ahorrar agua. Tienes cuatro ideas: ducha corta, cerrar la llave al lavarse los dientes, regar las plantas de noche y tu cantante favorito. ¿Cuál eliminas para mantener la coherencia? A) tu cantante favorito B) cerrar la llave al lavarse los dientes", "A) tu cantante favorito", "No se relaciona con el ahorro de agua.")],
    [
        ("En Inglés de 1.º medio (OA 5, clase 2): ¿qué partes tiene una presentación coherente?", "Introducción, desarrollo y conclusión", "Cada parte cumple una función."),
        ("En Inglés de 1.º medio (OA 5, clase 2): ¿para qué sirve For example?", "Para introducir un ejemplo", "Apoya una idea."),
        ("En Inglés de 1.º medio (OA 5, clase 2): ¿qué significa coherencia en una presentación?", "Que todas las ideas se relacionan con el tema", "Ninguna idea queda fuera."),
    ],
    task("Datos de ejemplo de una encuesta a 20 estudiantes sobre su deporte favorito: fútbol 9, vóleibol 6, básquetbol 5. Escribe en inglés una presentación de tres a cinco frases con introducción (saludo y tema), dos ideas con First y Second y una conclusión. Usa los datos con cuidado.", "Hello, everyone. I'll talk about our favourite sports. First, football is the most popular sport: nine students chose it. Second, six students prefer volleyball and five prefer basketball. In conclusion, football is our favourite. Thank you.", ["incluye introducción, desarrollo y conclusión", "usa First y Second", "los datos que menciona coinciden con la tabla"], ["hoja con la presentación", "lectura en voz alta a una persona"], ["decir que el vóleibol es el más popular", "agregar una idea fuera de tema"], "Reconoce la estructura y revisa cada número con la tabla; si hay un error, sugiere cambiar la frase y no el dato."),
    "Toma tres frases de la presentación de esta clase y subraya el conector de cada una.",
    "Prepara una presentación de cuatro frases sobre tu comida favorita con First, Second y In conclusion.",
)

# ------------------------------------------------------------------ clase 3: recursos multimodales
lesson(
    OA, 3, MAT,
    "Aprenderé a elegir imágenes, gráficos, palabras clave, gestos y la voz para reforzar lo que digo en una presentación. Sirve para que la audiencia entienda y recuerde mi mensaje.",
    ["Sé organizar una presentación.", "Conozco palabras como slide, chart y picture."],
    [
        "Un recurso multimodal (multimodal resource) es cualquier medio que refuerza el mensaje además de las palabras: una imagen (image), un gráfico (chart), palabras clave (key words), un objeto, un gesto, la voz o un video. La regla de oro es que el recurso refuerce lo que dices, no que lo reemplace. Si lees la diapositiva completa, el recurso sobra.",
        "Elige según el mensaje. Para comparar cantidades, usa un gráfico de barras (bar chart). Para mostrar cómo es algo, usa una imagen. Para mostrar el orden de hechos, usa una línea de tiempo (timeline). Para mostrar tres ideas, usa tres palabras clave: Water – Light – Air. En una diapositiva escribe pocas palabras, en letra grande, y no más de cinco o seis por línea.",
        "La voz y el cuerpo también comunican. Haz una pausa después de una idea importante, varía el volumen, mira a la audiencia y usa gestos simples: levantar tres dedos para tres ideas, mostrar dos manos para un contraste. Si no tienes proyector, usa un cartel o un objeto. Antes de presentar, revisa que todo se vea y se oiga desde el fondo.",
    ],
    [("slide", "diapositiva"), ("bar chart", "gráfico de barras"), ("timeline", "línea de tiempo"), ("key words", "palabras clave"), ("gesture", "gesto"), ("pause", "pausa")],
    [
        ("Elegir un recurso para comparar", "Quieres mostrar que 9 estudiantes prefieren fútbol, 6 vóleibol y 5 básquetbol. ¿Qué recurso es más claro?", ["El mensaje compara cantidades.", "Un gráfico de barras muestra diferencias de tamaño.", "Una foto no compara números."], "Un gráfico de barras"),
        ("Elegir texto para una diapositiva", "Quieres decir que una planta necesita agua, luz y aire. ¿Qué texto pones en la diapositiva? A) Water – Light – Air B) un párrafo de diez líneas sobre cómo crecen las plantas", ["La diapositiva debe tener pocas palabras.", "Las palabras clave apoyan lo que se dice.", "A es corto y claro."], "A) Water – Light – Air"),
    ],
    [
        ("Leer la diapositiva completa en voz alta.", "Se cree que la diapositiva es el guion.", "Usa solo palabras clave y explica con tus propias palabras."),
        ("Poner texto muy pequeño o una imagen borrosa.", "No se revisa cómo se ve desde el fondo.", "Prueba tu recurso a distancia antes de presentar."),
    ],
    [
        ("Quieres comparar cantidades. ¿Qué recurso eliges? A) un gráfico de barras B) una canción", "A) un gráfico de barras", "Muestra diferencias de tamaño con claridad."),
        ("Quieres mostrar cómo es un casco de bicicleta. ¿Qué recurso eliges? A) una imagen o el objeto B) una lista de números", "A) una imagen o el objeto", "Se ve su forma directamente."),
        ("Quieres indicar tres ideas con un gesto. ¿Qué haces? A) levantar tres dedos B) cruzar los brazos", "A) levantar tres dedos", "El gesto coincide con la cantidad."),
    ],
    [
        ("Una diapositiva tiene seis líneas largas de texto. ¿Qué es mejor? A) dejar solo tres palabras clave y explicar oralmente B) leerla completa", "A) dejar solo tres palabras clave y explicar oralmente", "El recurso refuerza; la explicación va en la voz."),
        ("Terminas una idea importante. ¿Qué haces con la voz? A) una pausa breve B) hablar más rápido", "A) una pausa breve", "La pausa da tiempo a la audiencia para procesar."),
        ("«Never read the slide» significa que debes: A) explicar con tus palabras usando las palabras clave B) apagar el proyector", "A) explicar con tus palabras usando las palabras clave", "La diapositiva es un apoyo, no un guion."),
    ],
    [
        ("Quieres mostrar los pasos de un proceso en orden de tiempo. ¿Qué recurso sirve? A) una línea de tiempo B) una foto única", "A) una línea de tiempo", "Muestra una secuencia de hechos."),
        ("Quieres expresar un contraste entre dos ideas. ¿Qué gesto ayuda? A) mostrar una mano para una idea y la otra mano para la segunda B) esconder las manos", "A) mostrar una mano para una idea y la otra mano para la segunda", "El gesto separa visualmente las dos ideas."),
        ("Presentas ante un grupo pequeño en una sala sin proyector. ¿Qué alternativa mantiene el apoyo visual? A) un cartel de cartulina con imágenes y palabras clave B) leer un texto largo", "A) un cartel de cartulina con imágenes y palabras clave", "Es un recurso visual sin tecnología."),
    ],
    [
        ("Una foto tiene letras tan pequeñas que no se leen desde el fondo. ¿Qué cambias? A) hacerlas más grandes o dejar solo una palabra clave B) agregar más letras pequeñas", "A) hacerlas más grandes o dejar solo una palabra clave", "El recurso debe verse desde el fondo."),
        ("Un compañero pone en la diapositiva las mismas frases que dice y las lee a la misma velocidad. ¿Qué mejora? A) la diapositiva muestra palabras clave y él explica con sus palabras B) más texto en la diapositiva", "A) la diapositiva muestra palabras clave y él explica con sus palabras", "Así el recurso suma información en vez de repetirla."),
    ],
    [
        ("Datos de ejemplo de una encuesta a 24 estudiantes: ir a pie 10, bus 8, bicicleta 6. ¿Qué gráfico muestra mejor cómo llegan al colegio? A) uno de barras con tres barras B) uno con una sola barra enorme", "A) uno de barras con tres barras", "Tres categorías comparables se muestran con tres barras."),
        ("En una charla sobre el reciclaje, el estudiante muestra un tarro de latas reales. ¿Qué cumple ese objeto? A) refuerza lo que dice, porque la audiencia ve de qué habla B) reemplaza la explicación", "A) refuerza lo que dice, porque la audiencia ve de qué habla", "Un objeto concreto apoya el mensaje."),
    ],
    [("Hablas con una persona de tu casa como audiencia y quieres que recuerde tres ideas. ¿Qué recurso combinado es mejor? A) tres palabras clave en un cartel, tres dedos y una pausa tras cada idea B) un texto largo y hablar muy rápido", "A) tres palabras clave en un cartel, tres dedos y una pausa tras cada idea", "Combina palabra, gesto y voz para reforzar el mensaje.")],
    [
        ("En Inglés de 1.º medio (OA 5, clase 3): ¿qué es un recurso multimodal?", "Un medio que refuerza el mensaje además de las palabras, como imagen, gráfico, gesto o voz", "Refuerza, no reemplaza."),
        ("En Inglés de 1.º medio (OA 5, clase 3): ¿qué gráfico sirve para comparar cantidades?", "Un gráfico de barras", "Muestra diferencias de tamaño."),
        ("En Inglés de 1.º medio (OA 5, clase 3): ¿cuántas palabras conviene poner por línea en una diapositiva?", "Pocas: cinco o seis como máximo", "El texto largo no se lee desde el fondo."),
    ],
    task("Datos de ejemplo de una encuesta a 18 estudiantes sobre su mascota favorita: perro 8, gato 6, pez 4. Prepara una diapositiva en tu hoja con un título en inglés, un gráfico de barras sencillo y una palabra clave por barra. Escribe también una frase en inglés que dirías mientras muestras el gráfico y un gesto que usarías.", "Título: Our favourite pets. Barras: dog 8, cat 6, fish 4. Frase: As you can see, dogs are the most popular pets. Gesto: señalo la barra más alta con la mano.", ["el gráfico tiene las barras con la altura correcta", "la diapositiva tiene pocas palabras", "la frase y el gesto refuerzan el gráfico"], ["hoja con la diapositiva", "frase escrita"], ["poner un párrafo en la diapositiva", "dibujar barras que no coinciden con los datos"], "Reconoce lo claro del gráfico y comprueba que las alturas calcen con los datos; si hay mucho texto, sugiere dejar solo palabras clave."),
    "Revisa una presentación que hayas visto y anota qué recursos usó y cuál reforzó mejor el mensaje.",
    "Dibuja dos diapositivas sobre el mismo tema: una con mucho texto y otra con palabras clave, y compara cuál se entiende mejor.",
)

# ------------------------------------------------------------------ clase 4: lenguaje, sonidos y notas de dos compañeros
lesson(
    OA, 4, MAT,
    "Aprenderé a armar una presentación juntando las notas de dos compañeros y a cuidar sonidos del nivel, como -tion, /j/ y /tr/. Sirve para presentar con datos completos y con una pronunciación clara.",
    ["Sé organizar una presentación y elegir recursos.", "Conozco los sonidos largos y cortos y el sonido -tion."],
    [
        "A veces cada persona tiene una parte de la información, como dos compañeros que preparan una exposición. Para hacer una buena presentación, juntas las notas (notes) de ambas y las conviertes en frases completas. Escribe qué dato aporta cada persona, elimina lo repetido y ordena: tema, lugar, fecha, quién participa y para qué.",
        "Las frases de una presentación usan funciones del lenguaje del nivel: There are eight students in the team. It starts every Friday. We have worked here since March. No copies las notas tal cual: transforma palabras sueltas en oraciones con verbo. Por ejemplo, de Topic: school radio puedes decir I'd like to talk about our school radio.",
        "Cuida también los sonidos. En presentation y information la terminación -tion se dice /ʃən/ y la fuerza cae antes: pre-sen-TA-tion, in-for-MA-tion. En young y year, el inicio es /j/. En tree y train, el grupo /tr/ va junto y suena casi como «ch» + r. Antes de presentar, subraya las palabras difíciles y practícalas en voz alta.",
    ],
    [("notes", "apuntes"), ("team", "equipo"), ("since March", "desde marzo"), ("presentation", "presentación (fuerza en -ta-)"), ("information", "información (fuerza en -ma-)"), ("young", "joven (inicio /j/)")],
    [
        ("Combinar notas", "Compañero A: «Topic: school radio. Day: every Friday. Place: room 6.» Compañero B: «Team: eight students. Since: March. Aim: share news.» Une los datos en dos frases para una presentación.", ["De A tomo el tema, el día y el lugar.", "De B tomo el equipo, la fecha de inicio y el objetivo.", "Escribo dos frases con verbo."], "Our school radio is every Friday in room 6. Eight students have worked in the team since March to share news."),
        ("Cuidar la pronunciación", "En la frase «The young team gave information about the radio», ¿qué palabras tienen el sonido /j/ inicial y el final -tion?", ["Busco una palabra que empiece como year.", "Young empieza con /j/.", "Information termina en -tion /ʃən/."], "Young (/j/) e information (-tion)"),
    ],
    [
        ("Copiar las notas tal cual, sin verbos.", "Se leen palabras sueltas y la audiencia no entiende la relación.", "Convierte cada nota en una oración completa."),
        ("Decir -tion como ti-on.", "Se pronuncia como en español.", "Di una sola sílaba suave /ʃən/ y marca la fuerza antes."),
    ],
    [
        ("¿Qué palabra termina con el sonido -tion /ʃən/? A) presentation B) present", "A) presentation", "Presentation termina en -tion."),
        ("Notas del compañero B: «Team: eight students. Since: March.» ¿Qué dato aporta B sobre el equipo? A) cuántos son y desde cuándo trabajan B) el día y la sala", "A) cuántos son y desde cuándo trabajan", "Eight students y since March describen al equipo."),
        ("¿Qué palabra empieza con el sonido /j/? A) year B) tree", "A) year", "Year empieza con /j/; tree empieza con /tr/."),
    ],
    [
        ("Proyecto «book swap» (intercambio de libros). Compañero A: «Dates: 3 to 7 June. Where: the library.» Compañero B: «You bring one book and take one book. No money.» ¿Qué dato aporta B? A) cómo participar y que es gratis B) las fechas y el lugar", "A) cómo participar y que es gratis", "Bring one book, take one book y no money son de B."),
        ("En presentation, ¿qué sílaba suena más fuerte? A) -ta- B) pre-", "A) -ta-", "Es pre-sen-TA-tion, con la fuerza antes de -tion."),
        ("¿Cuál es la frase completa mejor para la nota «Topic: book swap»? A) I'd like to talk about our book swap. B) Topic book swap.", "A) I'd like to talk about our book swap.", "Convierte la nota en una oración con verbo."),
    ],
    [
        ("Con las notas del book swap (A: «Dates: 3 to 7 June. Where: the library.» B: «You bring one book and take one book. No money.»), ¿qué frase para la presentación es correcta? A) The book swap is in the library from 3 to 7 June, and it is free. B) The book swap costs a lot of money.", "A) The book swap is in the library from 3 to 7 June, and it is free.", "Junta lugar, fechas y no money de ambos compañeros."),
        ("En «The young trainer drew a tree for the information desk», ¿cuántas palabras empiezan con /tr/? A) 2 B) 3", "A) 2", "Trainer y tree empiezan con /tr/; drew empieza con /dr/."),
        ("Notas de A: «Show: robots. Day: Thursday.» Notas de B: «Place: lab two. Entry: free.» ¿Qué dato aporta B? A) el lugar y que la entrada es gratis B) el día de la muestra", "A) el lugar y que la entrada es gratis", "Place: lab two y Entry: free son de B."),
    ],
    [
        ("Notas de A: «Project: school garden. Where: behind the gym.» Notas de B: «Plants: lettuce and tomatoes. Since: March.» ¿Qué frase junta los datos de ambos? A) The school garden is behind the gym, and we have grown lettuce and tomatoes since March. B) The school garden is in the library.", "A) The school garden is behind the gym, and we have grown lettuce and tomatoes since March.", "Une lugar, plantas y fecha de inicio."),
        ("¿Qué pregunta le haces a B si A no dijo cuántos son en el equipo? A) How many students are in the team? B) Where is the gym?", "A) How many students are in the team?", "How many pregunta por la cantidad."),
    ],
    [
        ("La nota de A dice «Day: Friday» y la de B dice «Time: five o'clock». ¿Qué frase junta ambos datos? A) The meeting is on Friday at five o'clock. B) The meeting is at Friday five.", "A) The meeting is on Friday at five o'clock.", "Se usa on con el día y at con la hora."),
        ("Quieres practicar la frase «Our young team has useful information». ¿Qué palabras pronuncias con más cuidado por su sonido? A) young (/j/) e information (-tion) B) team y has", "A) young (/j/) e information (-tion)", "Son las palabras con los sonidos trabajados en esta unidad."),
    ],
    [("En «Our presentation has useful information about the young team», ¿qué dos palabras terminan en -tion? A) presentation e information B) useful e young", "A) presentation e information", "Ambas terminan en -tion /ʃən/.")],
    [
        ("En Inglés de 1.º medio (OA 5, clase 4): ¿qué haces con las notas de dos compañeros?", "Juntas los datos, evitas repetir y los conviertes en oraciones completas", "Así la presentación queda coherente."),
        ("En Inglés de 1.º medio (OA 5, clase 4): ¿cómo se pronuncia -tion en information?", "/ʃən/, una sílaba suave, con la fuerza en -ma-", "El acento cae antes de -tion."),
        ("En Inglés de 1.º medio (OA 5, clase 4): ¿cuál es el sonido inicial de young?", "/j/", "Es una consonante, como en year."),
    ],
    task("Notas del compañero A: «Topic: recycling club. Day: Wednesday. Place: the patio.» Notas del compañero B: «Members: twelve students. Since: April. Aim: collect paper.» Escribe una introducción de tres frases en inglés que junte los datos de ambos. Luego lee en voz alta las palabras con -tion o /j/ que uses (por ejemplo, information, young, year) y subraya la sílaba fuerte de una.", "Hello, everyone. I'd like to talk about our recycling club. We meet on Wednesday in the patio. Twelve students have worked here since April to collect paper. (Palabra practicada: in-for-MA-tion.)", ["junta los datos de A y de B", "escribe oraciones con verbo", "practica una palabra con -tion o /j/"], ["hoja con tres frases", "lectura en voz alta a una persona"], ["omitir un dato de B", "pronunciar -tion como ti-on"], "Reconoce los datos reunidos y revisa que no falte uno; practica la sílaba fuerte con ella."),
    "Practica en voz alta cinco palabras con -tion y marca la sílaba fuerte con un lápiz.",
    "Pide a un compañero o a una persona de tu casa que te dicte notas de un tema y conviértelas en tres oraciones completas.",
)

# ------------------------------------------------------------------ clase 5: planificar, presentar y autoevaluarse
lesson(
    OA, 5, MAT,
    "Aprenderé a planificar una presentación de principio a fin y a evaluarla con una lista de criterios. Sirve para presentar con confianza y saber qué mejorar la próxima vez.",
    ["Sé audiencia, propósito, organización, recursos y sonidos.", "Sé combinar notas de dos personas."],
    [
        "Una presentación independiente se planifica en pasos. Primero: audiencia, contexto y propósito. Segundo: dos o tres ideas con un dato o ejemplo cada una. Tercero: un recurso que refuerce cada idea. Cuarto: ensayo en voz alta, controlando el tiempo. Como referencia, si hablas unas 100 palabras por minuto, una presentación de dos minutos tiene alrededor de 200 palabras.",
        "Para evaluar, usa criterios (criteria): contenido correcto, organización con introducción, desarrollo y conclusión, lenguaje y vocabulario apropiados, sonidos claros, recursos que refuerzan, y atención a la audiencia. Una buena evaluación dice qué ya está logrado y propone una meta (goal) concreta, como pronounce -tion words with /ʃən/ in my next talk.",
        "Después de presentar, escribe tu autoevaluación en tres pasos: qué hice bien, qué debo mejorar y cuál es mi meta. Registrar tus errores y buscar cómo corregirlos con ayuda de recursos, como un diccionario o una grabación, te permite avanzar. Pedir comentarios a la audiencia también ayuda, si los aceptas con calma.",
    ],
    [("criteria", "criterios: lo que se evalúa"), ("goal", "meta"), ("rehearse", "ensayar"), ("self-assessment", "autoevaluación"), ("feedback", "comentarios para mejorar"), ("minute", "minuto")],
    [
        ("Aplicar criterios a un texto", "Una estudiante presenta: «Good morning. Today I will explain how to make a paper plane. First, fold the paper in half. Second, fold the corners. Finally, throw it gently. Thank you.» ¿Qué criterio de organización cumple?", ["Tiene saludo y tema al inicio.", "Usa First, Second y Finally.", "Termina con Thank you."], "Cumple la organización: introducción, desarrollo con conectores y cierre"),
        ("Calcular el tiempo", "Si hablas unas 100 palabras por minuto (dato de ejemplo), ¿cuántas palabras debe tener una presentación de 2 minutos?", ["Multiplico 100 por 2.", "100 × 2 = 200.", "Es una aproximación para planificar."], "Unas 200 palabras"),
    ],
    [
        ("Evaluar solo con me gustó o no me gustó.", "No se usan criterios concretos.", "Evalúa cada criterio por separado y propone una meta."),
        ("Planificar el tiempo sin ensayar en voz alta.", "Se cree que leer en silencio basta.", "Ensaya con un reloj y ajusta."),
    ],
    [
        ("Una presentación dice: «Hello. I talk about dogs. Dogs are good. Thank you.» ¿Qué falta en el desarrollo? A) ejemplos o datos que expliquen las ideas B) un saludo", "A) ejemplos o datos que expliquen las ideas", "Solo repite que son buenos, sin evidencia."),
        ("¿Qué criterio mide si usas palabras como the most common con datos correctos? A) el contenido B) los sonidos", "A) el contenido", "Evalúa si lo que dices es correcto."),
        ("¿Qué meta es más útil? A) Pronounce -tion words with /ʃən/ in my next talk. B) Be better.", "A) Pronounce -tion words with /ʃən/ in my next talk.", "Es concreta y se puede comprobar."),
    ],
    [
        ("Una autoevaluación dice: «I used three key words on my slide, but I read it aloud.» ¿Qué debe mejorar? A) explicar con sus palabras sin leer la diapositiva B) usar más palabras en la diapositiva", "A) explicar con sus palabras sin leer la diapositiva", "El recurso refuerza si no se lee completo."),
        ("Quieres ensayar y te quedan 5 minutos. ¿Qué es lo más útil? A) decir la presentación en voz alta con un reloj B) leerla en silencio una vez", "A) decir la presentación en voz alta con un reloj", "Se controla el tiempo y se practican los sonidos."),
        ("Tu audiencia son niños de siete años. ¿Qué criterio revisas especialmente? A) que el vocabulario sea simple B) que uses datos muy técnicos", "A) que el vocabulario sea simple", "Se adapta el lenguaje a la audiencia."),
    ],
    [
        ("Una presentación usa tres palabras clave en un cartel, habla claro, cumple el tiempo y no tiene conclusión. ¿Qué meta propones? A) agregar una conclusión que resuma la idea principal B) usar más carteles", "A) agregar una conclusión que resuma la idea principal", "Es lo único que falta de la estructura."),
        ("Un compañero te da este comentario: «Your idea is good, but add one example after each idea.» ¿Qué acción corresponde? A) agregar un ejemplo después de cada idea B) quitar las ideas", "A) agregar un ejemplo después de cada idea", "Así aplicas el comentario."),
        arith("Una presentación de ejemplo dura 2 minutos y tiene 200 palabras. ¿Cuántas palabras por minuto habla, en promedio?", "200//2", "Se divide el total de palabras por los minutos.", " palabras por minuto"),
    ],
    [
        ("Una presentación de ejemplo dura 3 minutos y habla 100 palabras por minuto (dato de ejemplo). ¿Cuántas palabras tiene aproximadamente? A) 300 B) 200", "A) 300", "100 palabras × 3 minutos = 300."),
        ("Autoevalúas así: (1) saludo y tema claros, (2) dos ideas con conectores, (3) sin conclusión, (4) sonidos claros. ¿Cuántos criterios se cumplen completamente? A) 3 B) 4", "A) 3", "Faltó la conclusión, así que se cumplen tres de cuatro."),
    ],
    [
        ("Una presentación tiene saludo, tres ideas sin ejemplos, un gráfico claro y conclusión. ¿Qué meta es más precisa? A) add one example for each idea B) talk more", "A) add one example for each idea", "La meta es concreta y comprobable."),
        ("Tu compañero dice que hablaste muy rápido. ¿Qué registras para corregir? A) speed: pause after each idea B) topic: change the topic", "A) speed: pause after each idea", "El error es la velocidad y la corrección es una pausa."),
    ],
    [("Antes de presentar a una persona de tu casa, ¿cuál es el mejor orden de pasos? A) audiencia y propósito, ideas con ejemplo, recurso, ensayo con reloj B) ensayo, audiencia, recurso, ideas", "A) audiencia y propósito, ideas con ejemplo, recurso, ensayo con reloj", "Se planifica antes de ensayar.")],
    [
        ("En Inglés de 1.º medio (OA 5, clase 5): ¿para qué sirven los criterios?", "Para evaluar una presentación de forma concreta", "Cada criterio mide una parte distinta."),
        ("En Inglés de 1.º medio (OA 5, clase 5): ¿cómo es una buena meta?", "Concreta y fácil de comprobar", "Por ejemplo, pronunciar -tion con /ʃən/."),
        ("En Inglés de 1.º medio (OA 5, clase 5): ¿qué tres pasos tiene una autoevaluación?", "Qué hice bien, qué debo mejorar y cuál es mi meta", "Sirve para avanzar."),
    ],
    task("Prepara y presenta durante un minuto a una persona de tu casa: «My favourite place in my city or town» (mi lugar favorito). Usa saludo, dos ideas con First y Second, un cierre y un recurso (un dibujo o tres palabras clave). Luego completa en tu hoja: qué hiciste bien, qué debes mejorar y tu meta, con una frase en inglés.", "Hello, everyone. I'd like to talk about my favourite place: the park. First, it has many trees. Second, I can play football there. Thank you for listening. Autoevaluación: Hice bien la estructura. Debo mejorar la pausa. Meta: I will pause after each idea.", ["incluye saludo, dos ideas y cierre", "usa un recurso que refuerza", "completa la autoevaluación con una meta concreta"], ["hoja con el plan y la autoevaluación", "comentario de la persona oyente"], ["no incluir una meta", "leer toda la presentación sin mirar a la audiencia"], "Reconoce lo bien hecho y ayuda a precisar la meta para que se pueda comprobar."),
    "Escribe tres criterios de una buena presentación y marca cuáles ya cumples con facilidad.",
    "Graba o ensaya tu presentación otra vez con la meta de la clase y compara con la primera versión.",
)

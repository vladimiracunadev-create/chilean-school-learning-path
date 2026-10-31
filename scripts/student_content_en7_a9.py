"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 09 (interacción y reparación del significado).

Los diálogos y las fichas están escritos en cada enunciado, con pista en español. Las prácticas de habla se hacen en voz alta
con una persona de la casa o frente a un espejo; no se necesita ningún material especial.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA9 = "EN07 OA 09"

# ---------------------------------------------------------------- clase 1: antes de hablar
CAFE = "Situación: pides una bebida en una cafetería escolar. Frases útiles (chunks): «I'd like a…, please.» (quisiera un…), «How much is it?» (¿cuánto cuesta?), «Can I have…?» (¿me da…?), «Here you are.» (aquí tiene). Palabras que podrías necesitar: juice, milk, water, sandwich, cheese."
TOPIC = "Situación: vas a hablar sobre tu fin de semana. Frases útiles: «I'm going to talk about…» (voy a hablar de…), «First…, then…, finally…» (primero…, luego…, finalmente…), «I really like…» (me gusta mucho…), «In my opinion…» (en mi opinión…)."
LIBR = "Situación: preguntas en la biblioteca por un libro. Frases útiles: «Excuse me, do you have…?» (disculpe, ¿tiene…?), «Where can I find…?» (¿dónde puedo encontrar…?), «Can I borrow it?» (¿puedo pedirlo prestado?), «Thank you for your help.» (gracias por su ayuda)."

lesson(
    OA9, 1,
    "Las fichas de situación con frases útiles escritas en cada ejercicio, lápiz y un espejo o una persona de tu casa para practicar.",
    "Aprenderé estrategias para antes de hablar: practicar mi presentación, repetir, predecir el vocabulario clave y usar frases hechas (chunks). Sirve para empezar a hablar con más seguridad y fluidez.",
    ["Sé saludar y pedir cosas con please.", "Conozco palabras de comida y de la biblioteca."],
    [
        "Hablar bien comienza antes de abrir la boca. Practicar (practice) tu presentación en voz alta, varias veces, te ayuda a recordar y a sonar natural. Repetir (repeat) también sirve: di la frase, escucha cómo suena y vuelve a decirla. Una buena rutina es leer una vez, repetir tres veces y decirlo sin mirar.",
        "Predecir el vocabulario clave significa pensar qué palabras necesitarás. Si vas a pedir algo en una cafetería, piensas en juice, milk, sandwich y price. También prepara expresiones de uso común, llamadas chunks o bloques: frases completas que se aprenden juntas, como I'd like… o Where can I find…?. Un chunk te permite hablar con más rapidez porque no armas la frase palabra por palabra.",
        "Antes de hablar, también prepara un apoyo organizacional (por ejemplo, un esquema con palabras clave) y un apoyo visual (una imagen, un dibujo o una lista). Revisa cuánto tiempo tienes y anota el orden de lo que dirás. Si te equivocas al practicar, anótalo y repite la parte corregida. Practicar con una persona o frente a un espejo ayuda a controlar los gestos y el ritmo.",
    ],
    [("practice", "practicar: decir en voz alta varias veces"), ("repeat", "repetir"), ("chunk", "bloque o frase hecha que se aprende junta"), ("key vocabulary", "vocabulario clave"), ("predict", "predecir: pensar lo que necesitaré"), ("I'd like…", "quisiera…")],
    [
        ("Reconocer un chunk", "¿Cuál es un chunk útil para pedir algo? a) I'd like a juice, please b) Juice I like.", ["Un chunk es una frase completa y natural.", "La opción a se usa en la vida real.", "La opción b tiene el orden incorrecto."], "a) I'd like a juice, please."),
        ("Predecir vocabulario", "Vas a preguntar por un libro en la biblioteca. Predice dos palabras que necesitarás.", ["Pienso en lo que se dice allí.", "Palabras: book y borrow.", "También sirven library y find."], "book y borrow (o library, find)"),
    ],
    [
        ("Leer una frase una vez y creer que ya está lista.", "No se repite ni se practica.", "Repítela al menos tres veces en voz alta."),
        ("Traducir palabra por palabra en vez de usar un chunk.", "Suena poco natural.", "Aprende frases completas como Can I have…?"),
    ],
    [
        (CAFE + " ¿Qué chunk usas para saber el precio? a) «How much is it?» b) «Here you are.»", "a) How much is it?", "Pregunta cuánto cuesta."),
        (LIBR + " ¿Qué chunk usas para pedir un libro prestado? a) «Can I borrow it?» b) «Thank you for your help.»", "a) Can I borrow it?", "Borrow significa pedir prestado."),
        (TOPIC + " ¿Qué chunk usas para anunciar el tema? a) I'm going to talk about… b) In my opinion…", "a) I'm going to talk about…", "Anuncia de qué vas a hablar."),
    ],
    [
        (CAFE + " ¿Cuál de estas palabras predices para esta situación? a) sandwich b) passport", "a) sandwich", "Se relaciona con una cafetería."),
        (LIBR + " ¿Qué frase usas para empezar con cortesía? a) «Excuse me, do you have…?» b) «Give me…»", "a) Excuse me, do you have…?", "Es una forma cortés."),
        (TOPIC + " ¿Qué chunk sirve para ordenar las ideas? a) First…, then…, finally… b) Here you are.", "a) First…, then…, finally…", "Ordena la secuencia de ideas."),
    ],
    [
        (CAFE + " Ordena la conversación. A) «Here you are.» (la persona que vende te entrega la bebida) B) «I'd like a juice, please.» C) «How much is it?»", "B, C, A", "Se pide, se pregunta el precio y se entrega."),
        (TOPIC + " Armas tu práctica: lees una vez, repites 3 veces y la dices sin mirar. ¿Cuántas veces dices la frase en total contando todas las repeticiones, incluida la última sin mirar?", "5", "Una lectura, tres repeticiones y una última vez sin mirar.", "1+3+1"),
        (LIBR + " Completa: «Where can I ___ the book?» Elige find o found.", "find", "Después de can el verbo va en forma base."),
    ],
    [
        ("Un compañero dice que no hace falta practicar porque ya leyó la frase. ¿Qué le respondes? a) Practicar en voz alta ayuda a recordar y a hablar con fluidez b) Practicar es una pérdida de tiempo", "a) Practicar en voz alta ayuda a recordar y a hablar con fluidez", "Repetir mejora la fluidez."),
        (CAFE + " Si predices «cheese» y vas a pedir un sándwich, ¿la predicción es adecuada? Responde sí o no.", "Sí", "El queso es un ingrediente de un sándwich."),
    ],
    [
        ("Tienes 6 minutos para practicar y cada ensayo dura 2 minutos. ¿Cuántos ensayos completos puedes hacer?", "3", "Se reparten los minutos entre la duración de cada ensayo.", "6//2"),
        (TOPIC + " Si tu presentación tiene 4 chunks y aprendes 2 por día, ¿cuántos días necesitas?", "2", "Se divide el total de chunks entre los que aprendes cada día.", "4//2"),
    ],
    [("Antes de presentar, escribes en una tarjeta las palabras airport, passport y ticket. ¿Qué estrategia usas? a) predecir vocabulario clave b) improvisar sin preparar", "a) predecir vocabulario clave", "Piensas qué palabras necesitarás.")],
    [
        ("Al prepararte para hablar, ¿qué es un chunk?", "Una frase hecha que se aprende junta", "Facilita hablar con rapidez."),
        ("¿Qué conviene hacer antes de hablar?", "Practicar en voz alta", "Se gana fluidez."),
        ("¿Qué significa «I'd like…»?", "Quisiera…", "Es una forma cortés de pedir."),
    ],
    task("Elige una de estas situaciones y prepárate con las frases ya dadas: A) pedir ayuda a una persona para encontrar una sala, con «Excuse me, where is…?» y «Thank you»; B) pedir un helado, con «I'd like… please» y «How much is it?». Escribe un diálogo de cuatro líneas con tus chunks, predice cuatro palabras que necesitarás y practícalo tres veces en voz alta con una persona de tu casa.", "A) Excuse me, where is room twelve? — Go up the stairs. — Thank you! Palabras: room, stairs, up, thank you.", ["usa al menos dos chunks de la lista", "predice cuatro palabras coherentes con la situación", "practica tres veces en voz alta"], ["diálogo escrito", "nota de la persona que escuchó"], ["escribir el diálogo sin los chunks dados", "no practicar en voz alta"], "Reconoce lo que acertó y repasa con la persona los chunks hasta que los diga sin mirar."),
    "Practica frente a un espejo la situación de la biblioteca y fíjate en tus gestos.",
    "Escribe otra situación (por ejemplo, comprar un boleto) y tres chunks para ella.",
)

# ---------------------------------------------------------------- clase 2: apoyo organizacional y visual
CARD1 = "Ficha de ejemplo A: «Topic: My weekend. 1) Saturday: football, park. 2) Sunday: family lunch, cinema. 3) Favorite: cinema, why: fun story.» (weekend = fin de semana, cinema = cine, favorite = favorito)"
CARD2 = "Ficha de ejemplo B: «Hello. Today I will talk about my weekend. On Saturday I played football in the park with my friends and then we went to a place to eat and we talked for a long time. On Sunday I had lunch with my family and then in the afternoon I went to the cinema to see a very funny film with an interesting story.»"
VIS = "Apoyos visuales posibles: una foto del parque, un dibujo de una pelota, un boleto de cine de ejemplo, un calendario con sábado y domingo marcados."

lesson(
    OA9, 2,
    "Las fichas de ejemplo escritas en cada ejercicio, tarjetas de papel, lápiz y colores.",
    "Aprenderé a preparar un apoyo organizacional (un esquema o tarjeta con palabras clave) y un apoyo visual (imagen, dibujo, objeto) para hablar con claridad y fluidez. Sirve para no perderme ni leer toda la presentación.",
    ["Sé organizar ideas con first, then y finally.", "Conozco palabras como weekend, cinema y favorite."],
    [
        "El apoyo organizacional (organizational support) es un esquema o una tarjeta de notas (cue card) que te recuerda el orden de lo que vas a decir. Una buena tarjeta tiene el tema, 3 o 4 ideas con palabras clave y una conclusión. No escribas todo el discurso: si lees un párrafo largo, pierdes contacto con el público y suenas poco natural. Usa palabras clave, números y símbolos.",
        "El apoyo visual (visual support) es algo que el público puede ver: una imagen, un dibujo, un objeto, una tabla o un calendario. Ayuda a explicar una idea y también a ti a recordarla. Elige un apoyo que se relacione con el contenido y que se vea desde lejos. En variados formatos, puedes usar papel, pizarra o una diapositiva; lo importante es que apoye lo que dices.",
        "Para armar tu tarjeta: escribe el tema arriba; luego numera tus ideas en el orden que las dirás; agrega una palabra o imagen de apoyo para cada una; por último, escribe una frase de cierre. Practica con la tarjeta en la mano, mirando al público la mayor parte del tiempo y a la tarjeta solo cuando necesites recordar. Si te pierdes, respira, mira la tarjeta y retoma.",
    ],
    [("cue card", "tarjeta con palabras clave"), ("organizational support", "apoyo que ordena las ideas"), ("visual support", "apoyo visual"), ("keyword", "palabra clave"), ("outline", "esquema"), ("eye contact", "contacto visual con el público")],
    [
        ("Elegir la mejor tarjeta", CARD1 + " " + CARD2 + " ¿Qué ficha es una buena tarjeta de apoyo: la A o la B?", ["La A tiene palabras clave.", "La B es un párrafo largo.", "La mejor es la A."], "La A"),
        ("Apoyo visual", "Vas a hablar de tu deporte favorito. ¿Qué apoyo visual usarías: un dibujo del deporte o una página de números sin relación?", ["El apoyo debe relacionarse con el tema.", "Un dibujo del deporte lo ilustra.", "Una página de números sin relación no ayuda."], "Un dibujo del deporte"),
    ],
    [
        ("Escribir en la tarjeta todo el discurso palabra por palabra.", "Se termina leyendo y se pierde contacto visual.", "Anota solo palabras clave y el orden."),
        ("Usar una imagen que no se relaciona con el tema.", "Distrae.", "Elige un apoyo que refuerce la idea."),
    ],
    [
        (CARD1 + " ¿Cuántas ideas numeradas tiene la ficha A? a) 3 b) 5", "a) 3", "Son 1, 2 y 3."),
        (CARD1 + " ¿Cuál es el tema? a) My weekend b) My school", "a) My weekend", "Dice Topic: My weekend."),
        (VIS + " ¿Qué apoyo sirve para mostrar los dos días de tu fin de semana? a) un calendario con sábado y domingo marcados b) un dibujo de una pelota", "a) un calendario con sábado y domingo marcados", "Muestra el orden de los dos días."),
    ],
    [
        (CARD1 + " ¿Qué actividad tiene el sábado?", "Fútbol en el parque", "Dice Saturday: football, park."),
        (CARD1 + " ¿Por qué el hablante eligió el cine como favorito?", "Porque la historia es entretenida", "Dice why: fun story."),
        (VIS + " ¿Qué apoyo usarías para explicar la idea del cine? a) un boleto de cine de ejemplo b) la foto del parque", "a) un boleto de cine de ejemplo", "Se relaciona con ir al cine."),
    ],
    [
        (CARD2 + " ¿Por qué esta ficha no sirve como tarjeta? a) es un párrafo largo que se tendría que leer b) tiene muchas imágenes", "a) es un párrafo largo que se tendría que leer", "Una tarjeta debe tener palabras clave."),
        ("Quieres hablar del reciclaje. ¿Qué palabras clave pones en la tarjeta? a) paper, plastic, glass b) rice, tomato, soup", "a) paper, plastic, glass", "Son las palabras del tema."),
        ("¿Dónde miras la mayor parte del tiempo al presentar? a) al público b) a la tarjeta", "a) al público", "Eso es contacto visual."),
    ],
    [
        ("Un compañero dice que los apoyos visuales solo sirven al público. ¿Qué le respondes? a) también ayudan a recordar lo que se dice b) no sirven para nada", "a) también ayudan a recordar lo que se dice", "Sirven tanto al público como al hablante."),
        (CARD1 + " Si agregas la palabra «lunch» en la idea 2, ¿qué estás agregando? a) una palabra clave b) un párrafo", "a) una palabra clave", "Lunch es una palabra, no un párrafo."),
    ],
    [
        (CARD1 + " La ficha A tiene 3 ideas y cada una dura 1 minuto. Con una introducción de 1 minuto y una conclusión de 1 minuto, ¿cuánto dura la presentación?", "5", "Se suman las tres ideas y las dos partes de cierre.", "3+1+1"),
        ("Si cada tarjeta tiene 4 ideas y preparas 3 tarjetas, ¿cuántas ideas preparas en total?", "12", "Se multiplican las ideas de cada tarjeta por las tarjetas.", "4*3"),
    ],
    [("Preparas una presentación sobre tu mascota. En la tarjeta escribes: «Dog – name: Luna – food: meat, water – walk: park – favorite: ball». ¿Qué tipo de apoyo es? a) organizacional b) visual", "a) organizacional", "Es un esquema de palabras clave.")],
    [
        ("¿Qué debe tener una tarjeta de apoyo?", "Palabras clave en orden", "Recuerda las ideas sin leerlas todas."),
        ("¿Qué es un apoyo visual?", "Algo que el público puede ver", "Puede ser una imagen o un objeto."),
        ("¿Hacia dónde miras la mayor parte del tiempo?", "Hacia el público", "Así mantienes el contacto visual."),
    ],
    task("Prepara una tarjeta para hablar de este tema: «My favorite food». Usa esta lista de palabras ya dada: name of the food, ingredients, who makes it, when you eat it, why you like it. Escribe una tarjeta con el tema y cuatro ideas con palabras clave (no oraciones) y decide qué apoyo visual usarías. Practica diciendo el discurso a una persona de tu casa mirando la tarjeta solo dos veces.", "Topic: My favorite food. 1) Name: empanada. 2) Ingredients: meat, onion. 3) When: weekends. 4) Why: tasty. Visual: dibujo de una empanada.", ["la tarjeta tiene tema y cuatro ideas con palabras clave", "elige un apoyo visual que se relaciona", "practica mirando el apoyo pocas veces"], ["tarjeta", "nota de la persona que escuchó"], ["escribir oraciones largas en la tarjeta", "elegir un apoyo visual sin relación"], "Reconoce lo que acertó y ayuda a la persona a convertir las oraciones en palabras clave."),
    "Haz una tarjeta con cuatro palabras clave para el tema «My school» y úsala para hablar un minuto.",
    "Dibuja un apoyo visual para cada idea de la tarjeta B.",
)

# ---------------------------------------------------------------- clase 3: rellenos y gestos
DIALOG1 = "Diálogo: A: «What do you want to eat?» B: «Well… I'm not sure. Let me think.» A: «We have pizza or soup.» B: «Okay… I'll take the soup.» (let me think = déjame pensar, I'm not sure = no estoy seguro, I'll take = me quedo con)"
DIALOG2 = "Diálogo: A: «Why were you late?» B: «So… my bus was late. Well, it was stuck in traffic.» A: «Okay, no problem.» (stuck in traffic = atrapado en el tráfico)"
DIALOG3 = "Diálogo: A: «Do you like the new school rule?» B: «Hmm… I think it's good, but… you know, it's difficult sometimes.» A: «I agree.» (rule = regla, difficult = difícil, agree = estar de acuerdo)"

lesson(
    OA9, 3,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de tu casa para practicar.",
    "Aprenderé a usar gestos y rellenos temporales (well…, okay, so…) mientras hablo, para ganar tiempo y sonar natural cuando necesito pensar. Sirve para no quedarme en silencio y mantener la conversación.",
    ["Sé responder preguntas simples.", "Conozco expresiones como I think y I'm not sure."],
    [
        "Cuando hablas, a veces necesitas tiempo para pensar. En vez de quedarte en silencio, puedes usar rellenos temporales (fillers): well… (bueno…), okay… (está bien…), so… (entonces…), hmm… (mmm…), let me think (déjame pensar) y you know (sabes). Estas palabras no cambian el significado, pero muestran que sigues hablando y evitan pausas incómodas.",
        "Los gestos también ayudan. Un gesto de pensar (tocarte la barbilla) muestra que estás buscando una idea. Mover las manos para marcar una cantidad o un tamaño refuerza el mensaje. Asentir con la cabeza muestra que estás de acuerdo. Los gestos deben ser naturales y pocos; mucho movimiento distrae. Mirar a la persona mientras hablas muestra interés.",
        "Usa los rellenos con medida. Si dices «well» en cada oración, suena desordenado. Úsalo al comienzo de una respuesta o cuando necesitas pensar. Después de pensar, continúa con tu idea. Combina el relleno con una frase: «Well… I think it's good, but…». Con la práctica, los rellenos y los gestos te ayudan a hablar con más fluidez.",
    ],
    [("filler", "relleno que da tiempo para pensar"), ("well… / hmm…", "bueno… / mmm…"), ("so…", "entonces…"), ("let me think", "déjame pensar"), ("gesture", "gesto: movimiento que acompaña lo que dices"), ("you know", "sabes, ¿entiendes?")],
    [
        ("Identificar un relleno", "En «Well… I'm not sure», ¿cuál es el relleno?", ["Busco la palabra que da tiempo.", "Well no cambia el significado.", "Es el relleno."], "Well"),
        ("Elegir un relleno", "Te preguntan: «What is your favorite color?» y necesitas pensar. ¿Qué dices primero: «Hmm… let me think…» o «Yes, no, green»?", ["Necesito un relleno.", "Hmm… let me think da tiempo.", "La segunda opción es desordenada."], "Hmm… let me think…"),
    ],
    [
        ("Quedarse callado sin ninguna señal cuando se necesita pensar.", "Parece que no se entendió la pregunta.", "Usa un relleno como well… o let me think."),
        ("Repetir «well» en cada oración.", "Suena desordenado.", "Úsalo solo al comenzar o cuando necesitas pensar."),
    ],
    [
        (DIALOG1 + " ¿Qué dice B mientras piensa? a) Well… Let me think b) Pizza, pizza.", "a) Well… Let me think.", "Son rellenos para ganar tiempo."),
        (DIALOG2 + " ¿Qué relleno usa B al inicio? a) So… b) Hmm…", "a) So…", "B empieza con So…"),
        (DIALOG3 + " ¿Qué expresión muestra una duda? a) Hmm… b) I agree.", "a) Hmm…", "Hmm muestra que está pensando."),
    ],
    [
        (DIALOG1 + " ¿Qué elige B para comer?", "La sopa", "Dice I'll take the soup."),
        (DIALOG2 + " ¿Por qué llegó tarde B?", "Porque su bus estaba atrapado en el tráfico", "Dice my bus was late y stuck in traffic."),
        (DIALOG3 + " ¿Qué piensa B de la regla? a) que es buena pero a veces difícil b) que es inútil", "a) que es buena pero a veces difícil", "Dice I think it's good, but it's difficult sometimes."),
    ],
    [
        ("Un compañero se queda pensando 10 segundos. ¿Cuál es el mejor relleno? a) Let me think… b) Goodbye.", "a) Let me think…", "Da tiempo sin cerrar la conversación."),
        ("¿Qué gesto indica que estás pensando? a) tocarte la barbilla b) saludar con la mano", "a) tocarte la barbilla", "Es un gesto común de pensar."),
        ("Quieres mostrar que algo es muy grande. ¿Qué gesto usas? a) abrir los brazos b) cruzar los brazos", "a) abrir los brazos", "El gesto refuerza el tamaño."),
    ],
    [
        (DIALOG2 + " Completa: «___, my bus was late.» Elige So o Goodbye.", "So", "So es un relleno que comienza una explicación."),
        (DIALOG1 + " Un compañero dice que los rellenos cambian el significado. ¿Tiene razón? Responde sí o no.", "No", "Solo dan tiempo para pensar."),
    ],
    [
        ("Cuenta cuántos rellenos tiene esta respuesta: «Well… hmm… I think it's nice, you know, but… so… it's expensive.»", "4", "Son well, hmm, you know y so."),
        ("Una respuesta tiene 10 palabras y 3 son rellenos. ¿Cuántas palabras dicen la idea?", "7", "Se restan los rellenos del total.", "10-3"),
    ],
    [("Te preguntan: «What do you do after school?» No sabes cómo responder. ¿Qué dices? a) Well… let me think. I usually do my homework b) Nothing.", "a) Well… let me think. I usually do my homework.", "Usas un relleno y luego respondes.")],
    [
        ("¿Para qué sirve un relleno?", "Para ganar tiempo al pensar", "Evita silencios incómodos."),
        ("¿Qué significa «let me think»?", "Déjame pensar", "Es una frase para ganar tiempo."),
        ("¿Se deben usar en cada oración?", "No", "Solo cuando hace falta."),
    ],
    task("Trabaja con una persona de tu casa. Ella te hace estas tres preguntas en inglés: «What is your favorite season?», «What do you eat for breakfast?» y «Where do you want to travel?». Antes de cada respuesta usa un relleno de esta lista ya dada: well…, hmm…, so…, let me think. Escribe tus tres respuestas con su relleno y anota un gesto que usaste.", "Well… I like summer because it is sunny. Hmm… I eat bread and an egg. So… I want to travel to the beach. Gesto: toqué mi barbilla al pensar.", ["usa un relleno diferente antes de cada respuesta", "responde con una oración completa", "anota al menos un gesto"], ["hoja con tres respuestas", "nota de la persona que escuchó"], ["quedarse en silencio", "usar el mismo relleno siempre"], "Reconoce lo que acertó y practica con la persona respuestas más largas después del relleno."),
    "Mira en un espejo cómo se ve tu cara cuando piensas y practica un gesto natural.",
    "Escribe cinco preguntas que tu familia podría hacerte y responde usando rellenos distintos.",
)

# ---------------------------------------------------------------- clase 4: parafrasear, sinónimos y conectores
TEXT1 = "«I want to buy a refrigerator, but I forgot the word. I say: the big machine that keeps food cold.» (refrigerator = refrigerador, forgot = olvidé, machine = máquina, keeps = mantiene)"
TEXT2 = "«My friend is happy. She is glad because she won the game, and she feels great. After the game, we began to dance. First, we sang, and then we ate cake. We love the party too.» (won = ganó, feels great = se siente genial, began = comenzamos, cake = torta)"
TEXT3 = "«Can you help me? How do you say 'paraguas' in English? What does 'umbrella' mean in Spanish? Could you repeat that, please? Do you mean the red one?» (help = ayudar, repeat = repetir, mean = significar)"

lesson(
    OA9, 4,
    "Los textos breves escritos en cada ejercicio y lápiz.",
    "Aprenderé a parafrasear (decir algo con otras palabras), usar sinónimos y conectores, y a pedir ayuda cuando no sé una palabra. Sirve para seguir hablando aunque me falte vocabulario.",
    ["Sé conectores como and, but y because.", "Conozco preguntas como What does… mean?"],
    [
        "Cuando no recuerdas una palabra, no te detengas: parafrasea (paraphrase). Parafrasear es explicar con otras palabras lo que querías decir. Si olvidas refrigerator, puedes decir the big machine that keeps food cold. El oyente entiende y tú sigues hablando. También puedes usar un sinónimo (synonym), que es una palabra con significado parecido: happy y glad, big y large, begin y start.",
        "Los conectores (connectors) unen tus ideas y hacen tu mensaje más fluido: and (y), but (pero), because (porque), first, then, after that, finally, too (también), or (o). En lugar de decir frases cortas sueltas, une dos ideas: «I like pizza, and my brother likes pizza too». Los conectores muestran el orden y la relación de ideas.",
        "Si de verdad no sabes cómo decir algo, pide ayuda (ask for help): «How do you say… in English?» (¿cómo se dice… en inglés?), «What does… mean?» (¿qué significa…?), «Could you repeat that, please?» (¿puedes repetir?), «Do you mean…?» (¿quieres decir…?). Pedir ayuda es una estrategia, no un fracaso. Además, puedes usar un apoyo visual: dibujar o señalar la cosa.",
    ],
    [("paraphrase", "parafrasear: decir con otras palabras"), ("synonym", "sinónimo: palabra de significado parecido"), ("connector", "conector: une ideas"), ("ask for help", "pedir ayuda"), ("How do you say…?", "¿Cómo se dice…?"), ("Do you mean…?", "¿Quieres decir…?")],
    [
        ("Parafrasear", "No recuerdas la palabra «bicycle». ¿Qué puedes decir? a) the vehicle with two wheels that you pedal b) the red thing", ["Debo explicar con otras palabras.", "La opción a describe qué es.", "La opción b no es específica."], "a) the vehicle with two wheels that you pedal"),
        ("Sinónimo", "¿Qué palabra es sinónimo de «big»? Elige large o tiny.", ["Busco una palabra de significado parecido.", "Large también significa grande.", "Tiny significa diminuto."], "large"),
    ],
    [
        ("Detenerse en silencio cuando falta una palabra.", "Se interrumpe la conversación.", "Parafrasea o pide ayuda con How do you say…?"),
        ("Usar solo oraciones cortas sin conectores.", "El mensaje suena entrecortado.", "Une ideas con and, but o because."),
    ],
    [
        (TEXT1 + " ¿Qué hace el hablante cuando olvida la palabra? a) la explica con otras palabras b) se queda callado", "a) la explica con otras palabras", "Parafrasea: the big machine that keeps food cold."),
        (TEXT2 + " ¿Qué sinónimo de happy aparece? a) glad b) great", "a) glad", "Dice she is glad."),
        (TEXT3 + " ¿Qué frase sirve para pedir que repitan? a) «Could you repeat that, please?» b) «Do you mean the red one?»", "a) Could you repeat that, please?", "Pide con cortesía que repitan."),
    ],
    [
        (TEXT2 + " ¿Qué conector muestra el motivo de que esté contenta? a) because b) too", "a) because", "Dice she is glad because she won the game."),
        (TEXT2 + " ¿Qué conectores ordenan la secuencia? a) first y then b) and y or", "a) first y then", "Ordenan lo que hicieron."),
        (TEXT3 + " ¿Qué frase usas para confirmar un color? a) «Do you mean the red one?» b) «How do you say…?»", "a) Do you mean the red one?", "Confirma que entendiste."),
    ],
    [
        ("Completa con un conector: «I like tea ___ I don't like coffee.» Elige but o because.", "but", "Une dos ideas opuestas."),
        ("Completa con un sinónimo de «begin»: «Let's ___ the class.» Elige start o stop.", "start", "Start es sinónimo de begin."),
        ("No sabes la palabra «fridge». ¿Qué pides? a) «How do you say «refrigerador» in English?» b) «Give me fridge.»", "a) How do you say «refrigerador» in English?", "Pide ayuda con una pregunta cortés."),
    ],
    [
        (TEXT1 + " Un compañero dice que parafrasear es lo mismo que equivocarse. ¿Qué respondes? a) Es una estrategia para seguir comunicando b) Siempre es un error", "a) Es una estrategia para seguir comunicando", "El oyente entiende el mensaje."),
        ("Une las ideas con un conector: «I am tired. I want to play.» a) I am tired, but I want to play b) I am tired, because I want to play.", "a) I am tired, but I want to play.", "Las dos ideas se oponen."),
    ],
    [
        ("Cuenta cuántos conectores hay en esta oración: «First I read, and then I wrote, but I didn't finish because I was tired.»", "5", "Son first, and, then, but y because."),
        (TEXT2 + " Si en la fiesta hay 12 personas y cada una come 2 trozos de torta, ¿cuántos trozos se comen? Dato de ejemplo.", "24", "Se multiplican las personas por los trozos de cada una.", "12*2"),
    ],
    [("No conoces la palabra «mechanic». Tu amigo mecánico arregla autos. ¿Qué puedes decir? a) the person who repairs cars b) the thing", "a) the person who repairs cars", "Es una paráfrasis clara.")],
    [
        ("Si olvidas una palabra al hablar, ¿qué es parafrasear?", "Decir lo mismo con otras palabras", "Permite seguir hablando."),
        ("¿Qué significa «How do you say…?»", "¿Cómo se dice…?", "Se usa para pedir una palabra."),
        ("Al hablar en inglés, ¿qué es un synonym?", "Una palabra de significado parecido", "Por ejemplo, happy y glad."),
    ],
    task("Lee estas tres situaciones: 1) no recuerdas la palabra «pencil sharpener», 2) quieres unir dos ideas: «I like dogs. I have a cat.», 3) no entendiste lo que te dijeron. Escribe en inglés qué dirías en cada caso, usando: una paráfrasis, el conector but y una frase para pedir ayuda. Lista de apoyo ya dada: «the small tool that makes a pencil sharp», «but», «Could you repeat that, please?».", "1) The small tool that makes a pencil sharp. 2) I like dogs, but I have a cat. 3) Could you repeat that, please?", ["parafrasea sin usar la palabra olvidada", "une las ideas con un conector adecuado", "usa una frase de ayuda cortés"], ["hoja con tres respuestas"], ["usar and en lugar de but", "decir solo «what?»"], "Reconoce lo que acertó y practica con la persona frases corteses para pedir ayuda."),
    "Escribe tres pares de sinónimos y dos conectores nuevos en tu cuaderno.",
    "Explica en inglés, sin decir la palabra, qué es un «bus».",
)

# ---------------------------------------------------------------- clase 5: después de hablar, registrar errores
ERR1 = "Registro de errores de ejemplo: «I goed to the park.» → «I went to the park.» (verbo irregular). «She don't like soup.» → «She doesn't like soup.» (tercera persona). «I am agree.» → «I agree.» (no se usa am)."
ERR2 = "Frases de práctica de otra persona: «He have a red bike.» «They was happy.» «I have twelve years.» (have = tener, was = fue o estuvo, twelve years = doce años)"
LOG = "Tabla de registro: columna 1: lo que dije. Columna 2: lo correcto. Columna 3: la regla. Ejemplo: «I buyed a book» → «I bought a book» → buy es irregular."

lesson(
    OA9, 5,
    "Las frases y las tablas de errores escritas en cada ejercicio, lápiz y una persona de tu casa o tu cuaderno.",
    "Aprenderé a registrar mis errores después de hablar y a corregirlos con ayuda del profesor o de recursos como el diccionario o este cuaderno. Sirve para aprender de mis errores y hablar mejor la próxima vez.",
    ["Sé que algunos verbos son irregulares: go, went.", "Conozco las formas he has y she doesn't."],
    [
        "Después de hablar (after speaking), es útil registrar tus errores. Un error (mistake) no es un fracaso: muestra qué debes practicar. Anota la frase que dijiste, la frase correcta y la regla. Ese registro se llama error log. Ejemplo: «I goed to the park» → «I went to the park», porque go es un verbo irregular y su pasado es went.",
        "Los errores comunes de hablantes de español son: usar los verbos regulares con -ed en verbos irregulares (goed, buyed); olvidar la -s o does en la tercera persona (she don't → she doesn't; he have → he has); decir «I am agree» o «I have twelve years» por traducir del español (lo correcto es I agree y I am twelve years old). También se confunden was y were: they were happy.",
        "Para corregir, pide ayuda a tu profesor o consulta un recurso: un diccionario, una lista de verbos irregulares o este cuaderno. Corrige la frase y repítela tres veces en voz alta con la forma correcta. Después, léela en tu registro cada semana. Así transformas los errores en aprendizaje.",
    ],
    [("mistake", "error"), ("error log", "registro de errores: dije, correcto y regla"), ("irregular verb", "verbo irregular: go – went"), ("third person", "tercera persona: he, she, it"), ("correct", "corregir"), ("rule", "regla")],
    [
        ("Corregir un verbo irregular", "Corrige: «I runned to the bus stop.»", ["Run es irregular.", "Su pasado es ran.", "Queda I ran to the bus stop."], "I ran to the bus stop."),
        ("Corregir la tercera persona", "Corrige: «She go to school every day.»", ["Con she se agrega -es al verbo go.", "Cambio go por goes.", "Queda She goes to school every day."], "She goes to school every day."),
    ],
    [
        ("Ignorar un error después de hablar.", "Se vuelve a repetir.", "Anótalo en el registro y practica la forma correcta."),
        ("Corregir sin entender la regla.", "El error reaparece.", "Anota la regla en la tercera columna."),
    ],
    [
        (ERR1 + " ¿Cuál es la forma correcta de «I goed»? a) I went b) I gone", "a) I went", "Went es el pasado de go."),
        (ERR1 + " ¿Cuál es la forma correcta de «She don't like soup»? a) She doesn't like soup b) She not like soup.", "a) She doesn't like soup.", "Con she se usa doesn't."),
        (ERR2 + " Corrige la primera frase. a) He has a red bike b) He haves a red bike.", "a) He has a red bike.", "Has es la forma de have con he."),
    ],
    [
        (ERR2 + " Corrige: «They was happy.»", "They were happy.", "Con they se usa were."),
        (ERR2 + " Corrige: «I have twelve years.» a) I am twelve years old b) I has twelve years.", "a) I am twelve years old.", "En inglés la edad se dice con I am."),
        (LOG + " ¿Cuál es la regla del ejemplo «buyed → bought»? a) buy es un verbo irregular b) buy no existe", "a) buy es un verbo irregular", "Su pasado es bought."),
    ],
    [
        ("Una compañera dijo «I am agree». ¿Qué corrección haces? a) I agree b) I am agrees.", "a) I agree.", "Agree ya es un verbo."),
        ("¿Qué error tiene «Does she plays?» a) «falta quitar la -s: Does she play?» b) «falta agregar did»", "a) falta quitar la -s: Does she play?", "Después de does el verbo va en forma base."),
        ("Clasifica el error «She don't»: ¿tercera persona o verbo irregular?", "Tercera persona", "Con she se usa doesn't."),
    ],
    [
        ("Completa tu registro: Dije «I eated pizza.» Correcto: ___. Elige ate o eaten.", "ate", "Eat es irregular y su pasado es ate."),
        ("Completa: Dije «They is friends.» Correcto: ___. Elige They are friends o They be friends.", "They are friends", "Con they se usa are."),
    ],
    [
        ("Un registro tiene 5 errores. Si corriges 2 por día, ¿cuántos días necesitas para corregir todos?", "3", "Cinco errores a dos por día requieren tres días (el último día corriges uno).", "(5+1)//2"),
        ("Un compañero registró 4 errores el lunes y 3 el martes. ¿Cuántos errores registró en total?", "7", "Se suman los errores de los dos días.", "4+3"),
    ],
    [("Hablaste y dijiste «She have a cat». Anotas en tu registro: «She have → She has (tercera persona)». ¿Qué estrategia usas? a) registrar y corregir errores b) olvidar el error", "a) registrar y corregir errores", "Anotas la frase, la forma correcta y la regla.")],
    [
        ("¿Cómo se pasa a pasado el verbo go?", "went", "Es un verbo irregular."),
        ("¿Qué columnas tiene un error log?", "Lo que dije, lo correcto y la regla", "Así aprendes del error."),
        ("¿Qué recursos ayudan a corregir?", "El profesor, el diccionario y este cuaderno", "Dan la forma correcta."),
    ],
    task("Lee esta lista de frases dichas por un compañero al hablar, ya dadas: 1) «I goed to school.», 2) «He don't like fish.», 3) «We was in the park.», 4) «I am agree.». Crea una tabla de tres columnas (lo que dijo, lo correcto, la regla) y corrige las cuatro frases. Después escribe tus propias dos frases con errores comunes y su corrección.", "1) I went to school (go es irregular). 2) He doesn't like fish (tercera persona). 3) We were in the park (con we se usa were). 4) I agree (agree ya es verbo).", ["corrige las cuatro frases con la forma correcta", "anota una regla en cada fila", "agrega dos frases propias"], ["tabla con tres columnas"], ["corregir sin anotar la regla", "mantener «I am agree»"], "Reconoce lo que acertó y revisa con la persona las reglas que faltan en la tabla."),
    "Lee en voz alta las cuatro correcciones tres veces cada una.",
    "Escribe un registro de errores con cinco frases que sueles decir y su corrección.",
)

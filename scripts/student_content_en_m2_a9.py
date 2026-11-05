"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 09: estrategias para interactuar y exponer con claridad y fluidez.

Diálogos y textos originales y ficticios, con pista en español; todo lo que una pregunta nombra está escrito en el enunciado.
Los títulos de clase del plan son genéricos; aquí cada clase trabaja un grupo de estrategias del OA: antes de hablar
(practicar, organizar, conectar); al hablar (parafrasear, sinónimos, chunks); rellenos temporales y conectores; autocorrección
y apoyo visual; y después de hablar (debilidades, metas, registro de errores). La producción oral se evalúa en las tareas abiertas.
"""
from __future__ import annotations

from en_m2_a_common import MAT_SPEAK, arith, lesson, task

OA = "EN2M OA 09"

# ================================================== clase 1: antes de hablar
PLAN1 = "Ficha de ejemplo para una exposición sobre «Public Libraries». Diagrama: centro «Public Libraries»; rama 1 «services: books, computers, workshops»; rama 2 «who uses them: students, families, older people»; rama 3 «my experience: I visited one last month». Conexión propia: «In my neighbourhood there is a small library near the bus stop.»"
PLAN2 = "Ficha de ejemplo para una conversación sobre «A weekend plan». Palabras clave: place, time, friends, food. Frases útiles: «Would you like to…?», «How about…?», «What time is good for you?». Práctica: ensayar dos veces en voz alta."

lesson(
    OA, 1, MAT_SPEAK,
    "Aprenderé estrategias para antes de hablar: practicar la presentación, organizar las ideas clave en un diagrama y hacer conexiones. Sirve para sentir más seguridad y hablar con orden en una conversación o exposición.",
    ["Sé organizar una presentación con inicio, desarrollo y cierre.", "Sé frases como I think y In my opinion."],
    [
        "Antes de hablar (before speaking), prepárate con tres estrategias. Primero, practica (practise): di tu presentación en voz alta, de pie, dos o tres veces, y mide el tiempo. Segundo, organiza la información clave (key information) en un diagrama: pon el tema en el centro y las ideas alrededor, con palabras clave y no con oraciones completas. Tercero, establece conexiones (make connections): relaciona el tema con tu experiencia, con otra asignatura o con algo que sabes.",
        "Un diagrama ayuda a ver el orden de tus ideas y a no olvidar nada. Puedes dibujar una red de ideas (idea web), un esquema de tres partes o una tabla. Cada rama tiene una palabra clave y un ejemplo. Si sabes que vas a conversar, prepara también preguntas y frases útiles (useful phrases), como Would you like to…? o How about…?, para participar con confianza.",
        "Practicar no significa memorizar todo. Si memorizas, te bloqueas al olvidar una palabra. Es mejor recordar las ideas y decirlas con tus palabras. Practica con una persona que te escuche y te diga qué entendió. Si algo no se entiende, simplifica la frase. Una buena preparación reduce los nervios y mejora la fluidez.",
    ],
    [("practise", "practicar"), ("key information", "información clave"), ("idea web", "red de ideas"), ("make connections", "hacer conexiones"), ("useful phrases", "frases útiles"), ("fluency", "fluidez")],
    [
        ("Organizar", "Vas a exponer sobre tu pasatiempo. ¿Qué escribes primero en el diagrama? A) el tema en el centro B) todos los detalles", ["El tema va en el centro.", "Después añades ramas.", "La A."], "A"),
        ("Conexión", "Tu tema es «Libraries». ¿Qué es una conexión? A) I visited a library last month. B) Libraries are buildings.", ["Una conexión se relaciona con mi experiencia.", "La A cuenta algo propio.", "La A."], "A"),
    ],
    [
        ("Memorizar todo el texto palabra por palabra.", "Si olvidas una palabra, te bloqueas.", "Recuerda las ideas clave y dilas con tus palabras."),
        ("Preparar solo el inicio de la exposición.", "El resto sale sin orden.", "Organiza todas las ideas en un diagrama."),
    ],
    [
        ("Lee: " + PLAN1 + " ¿Cuál es el tema en el centro del diagrama? A) Public Libraries B) My experience", "A", "El centro dice Public Libraries."),
        ("Lee: " + PLAN1 + " ¿Cuántas ramas tiene el diagrama? A) tres B) cinco", "A", "Hay rama 1, rama 2 y rama 3."),
        ("Lee: " + PLAN2 + " ¿Cuántas veces se recomienda ensayar? A) dos B) diez", "A", "La ficha dice ensayar dos veces en voz alta."),
    ],
    [
        ("Lee: " + PLAN1 + " ¿Qué ejemplo personal aparece? A) visitó una biblioteca el mes pasado B) trabaja en una biblioteca", "A", "Dice I visited one last month."),
        ("Lee: " + PLAN2 + " ¿Qué frase sirve para proponer un plan? A) How about…? B) I disagree", "A", "How about…? sugiere una opción."),
        ("Lee: " + PLAN1 + " ¿Qué conexión propia tiene el diagrama? A) una biblioteca pequeña cerca del paradero B) una librería grande", "A", "Dice there is a small library near the bus stop."),
    ],
    [
        ("Lee: " + PLAN1 + " ¿Qué rama explica a los usuarios? A) la rama 2 B) la rama 3", "A", "La rama 2 dice who uses them."),
        ("Lee: " + PLAN2 + " ¿Qué palabra clave de la ficha se refiere a la hora? A) time B) food", "A", "Time es hora."),
        ("Lee: " + PLAN1 + " ¿Qué servicio se menciona? A) talleres B) conciertos", "A", "El diagrama dice workshops."),
    ],
    [
        ("Lee: " + PLAN1 + " Una estudiante dice que el diagrama debería tener oraciones completas. ¿Qué responde mejor? A) que las palabras clave bastan para recordar las ideas B) que sí, que necesita todo escrito", "A", "Un diagrama usa palabras clave."),
        ("Lee: " + PLAN2 + " ¿Por qué conviene practicar en voz alta? A) para escuchar si se entiende B) para memorizar", "A", "Practicar en voz alta permite corregir."),
    ],
    [
        ("Ordena las estrategias de preparación: a) practicar en voz alta b) organizar las ideas en un diagrama c) hacer conexiones con mi experiencia", "b, c, a", "Primero se organizan las ideas, luego se conectan con la experiencia y por último se practica."),
        ("Lee: " + PLAN2 + " Ordena los pasos de la conversación: a) proponer un plan b) saludar c) acordar la hora", "b, a, c", "Saludar, proponer y acordar son un orden lógico."),
    ],
    [("Lee: «Marta tiene 10 minutos para practicar. Dedica 3 minutos al diagrama de ideas, 4 minutos a practicar en voz alta y el resto a las conexiones.» ¿Cuántos minutos dedica a las conexiones?", "3", "10 menos 3 y menos 4 son 3.")],
    [
        ("¿Qué estrategias se usan antes de hablar?", "Practicar, organizar y hacer conexiones", "Preparan la exposición."),
        ("¿Qué se escribe en un diagrama?", "Palabras clave", "No oraciones completas."),
        ("¿Por qué no hay que memorizar todo?", "Porque si se olvida una palabra uno se bloquea", "Es mejor recordar las ideas."),
    ],
    task("Elige un tema: A) «My favourite game» o B) «A place I like». Haz un diagrama con el tema al centro y tres ramas con palabras clave. Agrega una conexión personal con una frase en inglés y dos frases útiles para empezar y cerrar. Practica en voz alta dos veces y pide a una persona de tu casa que te diga qué entendió.", "Ejemplo: Centro: my favourite game (chess). Ramas: rules, where I play, why I like it. Conexión: I play with my cousin on Sundays. Frases: Today I want to talk about…; Thank you for listening.", ["el diagrama tiene tema y tres ramas con palabras clave", "incluye una conexión personal", "practica dos veces en voz alta"], ["diagrama dibujado", "comentario de la persona que escuchó"], ["escribir oraciones completas en el diagrama", "omitir la práctica"], "Pregunta a la persona qué parte entendió mejor y cuál le costó."),
    "Haz un diagrama para una conversación que tendrás mañana en clase.",
    "Prepara una exposición de un minuto con un diagrama, una conexión y dos frases útiles.",
)

# ================================================== clase 2: parafrasear, sinónimos y chunks
DIAL2 = "«Ben: I think the exam was very difficult. Lía: What do you mean by difficult? Ben: I mean it was hard, and I did not have enough time. Lía: Ah, so you ran out of time. Ben: Exactly. Lía: In other words, the problem was the time. Ben: Yes, and some questions were confusing.»\n(exam = prueba, difficult = difícil, hard = duro, enough = suficiente, ran out of time = se quedó sin tiempo, confusing = confusas)"
DIAL3 = "«Teacher: Please explain what a ‘habit’ is. Student: It is something you do many times, like brushing your teeth. Teacher: Can you say it with other words? Student: It is a regular action, a routine. Teacher: Good. And a synonym? Student: A custom, maybe.»\n(habit = hábito, brushing = lavarse, regular = regular, routine = rutina, synonym = sinónimo, custom = costumbre)"

lesson(
    OA, 2, MAT_SPEAK,
    "Aprenderé a parafrasear, a usar sinónimos y a emplear expresiones de uso frecuente (chunks) al hablar. Sirve para explicar una idea con otras palabras cuando no recuerdo la palabra exacta y mantener la conversación.",
    ["Sé que una palabra puede tener un sinónimo.", "Sé frases como I mean y for example."],
    [
        "Parafrasear (paraphrase) es decir la misma idea con otras palabras. Se usa cuando no recuerdas una palabra o cuando quieres confirmar que entendiste. Frases útiles: In other words… (en otras palabras…), I mean… (quiero decir…), What do you mean by…? (¿qué quieres decir con…?) y So you mean that… (entonces quieres decir que…). Parafrasear muestra que escuchas y ayuda a aclarar ideas.",
        "Un sinónimo (synonym) es una palabra con significado parecido: difficult y hard; big y large; begin y start. Si no te acuerdas de una palabra, usa otra más simple o describe: «a place where you borrow books» en vez de library. Los chunks son grupos de palabras que se usan juntos y se aprenden como una unidad: by the way, in my opinion, as soon as, a lot of, I’d like to, Do you mind if…?",
        "Los chunks te dan fluidez porque no tienes que construir cada frase palabra por palabra. Aprende los chunks con su situación: para pedir (Could you…?), para opinar (I think that…), para contrastar (on the other hand). Cuando hables, elige un chunk y completa con tus ideas. Así hablas más rápido y con menos errores.",
    ],
    [("paraphrase", "parafrasear: decir lo mismo con otras palabras"), ("synonym", "sinónimo"), ("chunk", "grupo de palabras que se usa junto"), ("In other words", "en otras palabras"), ("I mean", "quiero decir"), ("What do you mean by…?", "¿Qué quieres decir con…?")],
    [
        ("Sinónimo", "¿Qué palabra es sinónimo de hard (difícil)? A) difficult B) soft", ["Busco una palabra con significado parecido.", "Difficult significa difícil.", "La A."], "A"),
        ("Parafrasear", "Alguien dice: «The film is boring.» ¿Cómo lo parafraseas? A) In other words, it is not interesting. B) It is expensive.", ["Debe decir lo mismo.", "Boring es no interesante.", "La A."], "A"),
    ],
    [
        ("Quedarse en silencio cuando falta una palabra.", "Se corta la conversación.", "Usa un sinónimo o describe con otras palabras."),
        ("Parafrasear cambiando el significado.", "Ya no se dice lo mismo.", "Mantén la idea y cambia solo las palabras."),
    ],
    [
        ("Lee: " + DIAL2 + " ¿Qué palabra usa Ben como sinónimo de difficult? A) hard B) fast", "A", "Dice I mean it was hard."),
        ("Lee: " + DIAL3 + " ¿Qué ejemplo da el estudiante para habit? A) lavarse los dientes B) dormir", "A", "Dice like brushing your teeth."),
        ("Lee: " + DIAL3 + " ¿Qué sinónimo propone para habit? A) custom B) place", "A", "Dice A custom, maybe."),
    ],
    [
        ("Lee: " + DIAL2 + " ¿Qué frase usa Lía para parafrasear? A) In other words, the problem was the time. B) What is your name?", "A", "Repite la idea con otras palabras."),
        ("Lee: " + DIAL2 + " ¿Qué significa ran out of time? A) se quedó sin tiempo B) tuvo mucho tiempo", "A", "Ran out of significa se acabó."),
        ("Lee: " + DIAL3 + " ¿Qué palabra usa como sinónimo de regular action? A) routine B) holiday", "A", "Dice It is a regular action, a routine."),
    ],
    [
        ("Lee: " + DIAL2 + " ¿Qué pregunta hace Lía para aclarar? A) What do you mean by difficult? B) Why are you late?", "A", "Pide aclarar una palabra."),
        ("Lee: " + DIAL3 + " ¿Qué hace la profesora cuando dice Can you say it with other words? A) pide una paráfrasis B) corrige la ortografía", "A", "Pide decirlo de otro modo."),
        ("Completa con un chunk: «___ the way, my brother is coming tomorrow.» A) By B) On", "A", "El chunk es by the way."),
    ],
    [
        ("Lee: " + DIAL2 + " Un compañero dice que Lía cambió la idea de Ben. ¿Qué lo contradice? A) Ben dice Exactly, aceptando su paráfrasis B) Lía habla de otro tema", "A", "Exactly confirma que repite bien la idea."),
        ("Lee: " + DIAL3 + " ¿Qué estrategia usa el estudiante cuando no tiene una palabra exacta? A) describe con otras palabras B) se queda callado", "A", "Dice It is something you do many times."),
    ],
    [
        ("Une cada palabra con su sinónimo. 1) big 2) begin 3) happy. Sinónimos: a) start b) glad c) large", "1-c, 2-a, 3-b", "Big y large, begin y start, happy y glad."),
        ("Elige el chunk correcto para pedir permiso: A) Do you mind if I open the window? B) Do you mind I opening window?", "A", "El chunk completo es Do you mind if I…?"),
    ],
    [("Lee: «I don’t remember the word ‘umbrella’. I say: It is something you use when it rains.» (rains = llueve). ¿Qué estrategia usa?", "Describe la palabra", "Dice que es algo que se usa cuando llueve.")],
    [
        ("¿Qué es parafrasear (en Inglés, 2.º medio)?", "Decir lo mismo con otras palabras", "Mantiene la idea."),
        ("¿Qué es un chunk (en Inglés, 2.º medio)?", "Un grupo de palabras que se usa junto", "Da más fluidez al hablar."),
        ("¿Qué haces si no recuerdas una palabra?", "Uso un sinónimo o describo", "Así sigo hablando."),
    ],
    task("Hay tres palabras: tired, enjoy, small. Para cada una, escribe un sinónimo o una descripción en inglés. Luego escribe un diálogo de cuatro líneas con In other words y What do you mean by…? y represéntalo con una persona de tu casa.", "Ejemplo: tired = exhausted (o: I need to sleep). enjoy = like (o: it makes me happy). small = little (o: not big). Diálogo: A: The test was tough. B: What do you mean by tough? A: It was difficult. B: In other words, it was hard.", ["da un sinónimo o descripción para cada palabra", "usa In other words y What do you mean by", "mantiene la idea original"], ["hoja con las tres palabras y el diálogo"], ["usar un sinónimo con otro significado", "dejar el diálogo sin una aclaración"], "Pregunta a la persona qué palabra le costó entender y cámbiala por otro sinónimo."),
    "Escribe una lista de diez sinónimos y úsalos en frases.",
    "Elige cinco chunks que quieras aprender y escribe una situación para cada uno.",
)

# ================================================== clase 3: rellenos temporales y conectores
CONV3 = "«Teo: So, are you coming to the match on Saturday? Rita: Well, I am not sure. I have to finish a project. Teo: Of course, the project is important. Anyway, the match is at five. Rita: Right, five is fine. Let me think. Teo: Sure. Take your time. Rita: Okay. I will come, as soon as I finish the first part.»\n(match = partido, sure = seguro, project = proyecto, take your time = tómate tu tiempo, finish = terminar)"

lesson(
    OA, 3, MAT_SPEAK,
    "Aprenderé a usar rellenos temporales (anyway, of course, right) y conectores mientras hablo. Sirve para ganar tiempo para pensar, mantener la conversación y unir mis ideas con naturalidad.",
    ["Sé conectores como and, but y because.", "Sé responder preguntas simples."],
    [
        "Los rellenos temporales (fillers) son palabras o frases cortas que se usan mientras piensas: well (bueno), let me think (déjame pensar), you know (sabes), I mean (quiero decir). Las palabras anyway (de todos modos), of course (por supuesto) y right (claro, de acuerdo) sirven también para reaccionar y para pasar a otra idea. Usados con moderación, hacen que tu habla suene natural.",
        "Los conectores (connectors) unen ideas: and (suma), but (contraste), because (causa), so (consecuencia), first y then (orden), though (aunque) y as soon as (tan pronto como). Si los usas, tu mensaje se entiende como un conjunto y no como frases separadas. Por ejemplo: I will come, as soon as I finish the project.",
        "Cuidado con el exceso. Repetir um, uh o well todo el tiempo cansa a quien escucha. Elige uno o dos rellenos y úsalos cuando realmente necesites tiempo. Una pausa corta también funciona. Después del relleno, completa tu idea con un conector claro y una razón. Escucha cómo lo hacen otras personas y copia sus frases.",
    ],
    [("filler", "relleno: palabra para ganar tiempo"), ("anyway", "de todos modos"), ("of course", "por supuesto"), ("right", "claro; de acuerdo"), ("well", "bueno"), ("let me think", "déjame pensar")],
    [
        ("Elegir relleno", "Te preguntan algo y necesitas un segundo para pensar. ¿Qué dices? A) Well, let me think. B) Goodbye.", ["Necesito tiempo.", "Well y let me think sirven.", "La A."], "A"),
        ("Conector", "Completa: «I was tired, ___ I went to bed early.» A) so B) but", ["La segunda idea es consecuencia.", "So muestra consecuencia.", "La A."], "A"),
    ],
    [
        ("Repetir um y uh sin parar.", "El mensaje se pierde y cansa.", "Usa un relleno claro y luego completa la idea."),
        ("No usar ningún conector.", "Las ideas quedan separadas.", "Une las ideas con and, but, because o so."),
    ],
    [
        ("Lee: " + CONV3 + " ¿Cuándo es el partido? A) el sábado B) el viernes", "A", "Dice the match on Saturday."),
        ("Lee: " + CONV3 + " ¿A qué hora es el partido? A) a las cinco B) a las siete", "A", "Dice the match is at five."),
        ("Lee: " + CONV3 + " ¿Qué debe terminar Rita? A) un proyecto B) la tarea de inglés", "A", "Dice I have to finish a project."),
    ],
    [
        ("Lee: " + CONV3 + " ¿Qué relleno usa Rita para empezar su respuesta? A) Well B) Anyway", "A", "Dice Well, I am not sure."),
        ("Lee: " + CONV3 + " ¿Qué quiere decir Of course aquí? A) por supuesto, acepta que el proyecto es importante B) no está de acuerdo", "A", "Teo reconoce la razón de Rita."),
        ("Lee: " + CONV3 + " ¿Qué hace Teo con Anyway? A) pasa a otro tema, la hora del partido B) termina la conversación", "A", "Dice Anyway, the match is at five."),
    ],
    [
        ("Lee: " + CONV3 + " ¿Qué muestra as soon as? A) un momento: tan pronto como termine B) un contraste", "A", "Rita vendrá cuando termine la primera parte."),
        ("Lee: " + CONV3 + " ¿Qué dice Rita para ganar tiempo? A) Let me think. B) I disagree.", "A", "Es un relleno de tiempo."),
        ("Completa: «I like football, ___ I don’t like running.» A) but B) so", "A", "Las dos ideas son contrarias."),
    ],
    [
        ("Lee: " + CONV3 + " ¿Qué muestra Right en la respuesta de Rita? A) acuerdo con la hora B) enojo", "A", "Right significa claro, de acuerdo."),
        ("Lee: " + CONV3 + " Un compañero dice que Rita no quiere ir. ¿Qué lo contradice? A) al final dice I will come B) dice Well", "A", "Rita termina aceptando ir."),
    ],
    [
        ("Une cada frase con su función. 1) Well, let me think. 2) Anyway, back to the topic. 3) I will call you as soon as I arrive. Funciones: a) ganar tiempo b) marcar un momento c) volver al tema", "1-a, 2-c, 3-b", "Let me think gana tiempo; anyway cambia al tema y as soon as marca el momento."),
        ("Ordena una respuesta fluida: a) Because I have to study. b) Well, I am not sure. c) So I will answer tomorrow.", "b, a, c", "Relleno, razón y consecuencia forman una respuesta natural."),
    ],
    [("Lee: «Pia: Do you want to come to the cinema? Max: Of course! Anyway, what time is it? Pia: At seven.» ¿A qué hora es la función?", "A las siete", "Dice At seven.")],
    [
        ("¿Para qué sirven los rellenos (en Inglés, 2.º medio)?", "Para ganar tiempo al pensar", "Hacen más natural el habla."),
        ("¿Qué significa of course?", "Por supuesto", "Acepta una idea."),
        ("¿Qué conector muestra consecuencia?", "So", "Une causa y resultado."),
    ],
    task("Representa con una persona de tu casa este diálogo: tú invitas a un amigo a hacer algo el fin de semana y él tiene dudas. Escribe primero tres respuestas del amigo con well, let me think, of course o anyway, y dos conectores (because, so, but, though, as soon as). Luego ensáyalo dos veces.", "Ejemplo: Well, I am not sure because I have homework. Of course I like the idea, but I have to ask my mother. Anyway, I will tell you as soon as I know.", ["usa dos rellenos temporales", "usa dos conectores", "la respuesta se entiende y suena natural"], ["hoja con las respuestas", "comentario de la persona que escuchó"], ["repetir un relleno diez veces", "no usar conectores"], "Pregunta a la persona qué relleno sonó más natural."),
    "Escucha a alguien en un video y anota qué rellenos usa.",
    "Escribe un diálogo de ocho líneas con tres rellenos y tres conectores.",
)

# ================================================== clase 4: autocorrección y apoyo visual
SELF = "«I go to the zoo yesterday… sorry, I went to the zoo yesterday. There were two elephants and a tigers… I mean, a tiger. The tiger is very big, I mean, it was very big. It was the best day, no, one of the best days of the year.»\n(zoo = zoológico, yesterday = ayer, elephants = elefantes, tiger = tigre, best = mejor)"
VIS = "Cuadro de apoyo visual en tres formatos para presentar su fin de semana: 1) una foto de una pista de patinaje, 2) un gráfico de barras con «10 min walking, 20 min cycling, 60 min skating» (de ejemplo) y 3) una tarjeta con las palabras skate, friends, helmet."

lesson(
    OA, 4, MAT_SPEAK,
    "Aprenderé a autocorregirme con ayuda y a usar apoyo visual en distintos formatos al hablar. Sirve para mejorar lo que digo en el momento y para que mi audiencia entienda mejor con imágenes, gráficos o tarjetas.",
    ["Sé usar el pasado simple de verbos comunes.", "Sé leer un gráfico simple."],
    [
        "Autocorregirse (self-correct) es notar un error mientras hablas y arreglarlo. Se usan frases como sorry, I mean, no o let me say that again. Por ejemplo: I go to the zoo yesterday… sorry, I went to the zoo yesterday. Autocorregirse no es mala señal: muestra que escuchas tu propio mensaje. La corrección puede venir de ti o de otra persona que te ayuda con una pregunta o una pista.",
        "Para autocorregirte con ayuda, escucha a quien te escucha: si frunce el ceño o repite tu frase, puede que haya un error. Puedes pedir ayuda: Is that correct? o How do you say…? Los errores más comunes son el tiempo verbal (go en vez de went), el plural (a tigers) y la concordancia (the tiger is, the tigers are). No te detengas demasiado: corrige y sigue.",
        "El apoyo visual (visual support) ayuda a hablar con claridad: una foto, un gráfico, una tarjeta con palabras clave, un mapa o un objeto. Cada formato cumple una función: la foto muestra un lugar, el gráfico compara datos, la tarjeta recuerda las palabras clave. Elige el formato que mejor sirva a tu idea y míralo mientras hablas, pero sin darle la espalda a tu audiencia.",
    ],
    [("self-correct", "autocorregirse"), ("I mean", "quiero decir (para corregir)"), ("Is that correct?", "¿Es correcto?"), ("visual support", "apoyo visual"), ("graph", "gráfico"), ("keyword card", "tarjeta con palabras clave")],
    [
        ("Autocorrección", "Dices: «She go to school.» ¿Cómo te corriges? A) Sorry, she goes to school. B) She go.", ["Noté un error de concordancia.", "Se usa goes.", "La A."], "A"),
        ("Formato", "Quieres mostrar cuántos minutos practicas cada deporte. ¿Qué apoyo conviene? A) un gráfico de barras B) una foto del colegio", ["Son datos para comparar.", "El gráfico compara.", "La A."], "A"),
    ],
    [
        ("Seguir hablando sin corregir un error que se nota.", "El mensaje puede cambiar de sentido.", "Usa sorry o I mean y arregla la frase."),
        ("Mirar solo el apoyo visual y no a la audiencia.", "Se pierde contacto.", "Mira a las personas y usa la imagen solo como apoyo."),
    ],
    [
        ("Lee: " + SELF + " ¿Cómo corrige go? A) went B) goes", "A", "Dice I go to the zoo yesterday… sorry, I went."),
        ("Lee: " + SELF + " ¿Qué animal vio, según la corrección? A) un tigre B) dos tigres", "A", "Se corrige a tigers… I mean, a tiger."),
        ("Lee: " + VIS + " ¿Qué muestra el gráfico? A) minutos de cada actividad B) precios", "A", "El gráfico muestra minutos."),
    ],
    [
        ("Lee: " + SELF + " ¿Qué frase usa para corregirse? A) I mean B) goodbye", "A", "Dice I mean, a tiger."),
        ("Lee: " + VIS + " ¿Qué muestra la foto? A) una pista de patinaje B) un gimnasio", "A", "La foto es de una pista de patinaje."),
        ("Lee: " + VIS + " ¿Qué función tiene la tarjeta de palabras clave? A) recordar palabras importantes B) mostrar un lugar", "A", "Skate, friends y helmet son palabras clave."),
    ],
    [
        ("Lee: " + SELF + " ¿Qué tiempo verbal se corrige a it was very big? A) el pasado B) el futuro", "A", "Se pasa de is a was."),
        arith("Lee: " + VIS + " En el gráfico, ¿cuántos minutos suman las tres actividades?", "10+20+60", "Se suman los minutos de caminar, andar en bicicleta y patinar."),
        ("Lee: " + VIS + " ¿Qué actividad ocupa más tiempo? A) skating B) walking", "A", "60 minutos es la cifra más alta."),
    ],
    [
        ("Lee: " + SELF + " Una compañera dice que el estudiante no sabe usar el pasado. ¿Qué lo contradice? A) se corrige y usa went y it was B) usa pocas palabras", "A", "Muestra que reconoce el error y lo arregla."),
        ("Lee: " + VIS + " ¿Por qué un gráfico es mejor que un texto para comparar tiempos? A) porque permite ver rápido cuál es mayor B) porque es más largo", "A", "La barra más alta muestra el mayor valor."),
    ],
    [
        ("Lee: " + SELF + " Ordena la autocorrección: a) sorry, I went b) I go to the zoo c) yesterday", "b, c, a", "Primero el error, luego yesterday y por último la corrección."),
        ("Lee: " + VIS + " Elige el mejor apoyo para describir un lugar nuevo: A) una foto B) un gráfico de barras", "A", "Una foto muestra cómo es un lugar."),
    ],
    [("Lee: «She have two brothers… sorry, she has two brothers.» ¿Qué error corrige?", "La concordancia: have por has", "Con she se usa has.")],
    [
        ("¿Qué es autocorregirse?", "Notar un error y arreglarlo al hablar", "Muestra que escucho mi mensaje."),
        ("¿Qué frase sirve para corregirse?", "Sorry, I mean…", "Anuncia la corrección."),
        ("¿Qué apoyo visual compara datos?", "Un gráfico", "Las barras muestran valores."),
    ],
    task("Lee en voz alta a una persona de tu casa: «Yesterday I go to the park with my friends. We play football and we eat a sandwich. It was a great day.» Hay tres errores de verbo. En tu hoja escribe cómo te autocorregirías con sorry o I mean. Luego elige un apoyo visual (foto, gráfico o tarjeta) y explica por qué sirve para contar tu día.", "Corrección: Yesterday I went to the park… sorry, we played football and we ate a sandwich. Apoyo: una foto del parque para mostrar el lugar.", ["corrige los tres verbos en pasado", "usa sorry o I mean", "justifica el apoyo visual"], ["hoja con las correcciones", "comentario de la persona que escuchó"], ["dejar los verbos en presente", "elegir un apoyo sin justificar"], "Pregunta a la persona si notó los errores antes de que te corrigieras."),
    "Graba una frase con un error y corrígela en voz alta.",
    "Prepara una exposición de un minuto con dos tipos de apoyo visual diferentes.",
)

# ================================================== clase 5: después de hablar
LOG = "Registro de ejemplo de errores de una estudiante. Error 1: «I have 15 years» (corrección: I am 15 years old). Error 2: «She don’t like fish» (corrección: She doesn’t like fish). Error 3: «I am agree» (corrección: I agree). Meta: cometer menos de tres errores en la próxima conversación. Recurso: un diccionario en línea y una lista de verbos."
FEED = "Comentarios de un compañero tras una exposición: «Your pronunciation of ‘student’ was clear. You spoke too fast at the end. You used a good example. You forgot to look at the audience.»\n(pronunciation = pronunciación, fast = rápido, example = ejemplo, audience = audiencia)"

lesson(
    OA, 5, MAT_SPEAK,
    "Aprenderé a evaluar lo que dije después de hablar: identificar debilidades, establecer metas y registrar errores con su corrección usando recursos de ayuda. Sirve para mejorar de una presentación a la siguiente.",
    ["Sé usar estrategias antes y durante la exposición.", "Sé usar un diccionario."],
    [
        "Después de hablar (after speaking), reflexiona sobre cómo te fue. Primero identifica tus fortalezas (strengths) y debilidades (weaknesses): ¿qué hice bien?, ¿qué me costó? Puedes usar la ayuda de otra persona, una grabación o una lista de verificación (checklist). Segundo, establece una meta (goal) concreta, medible y alcanzable: Next time I will speak more slowly o I will use two connectors.",
        "Registrar errores (record errors) es anotar lo que dijiste mal y su corrección: I have 15 years → I am 15 years old. Tener un registro te permite ver si repites los mismos errores. Para corregirlos usa recursos (resources): un diccionario en línea, una tabla de verbos irregulares, un libro o tu profesor. Después, practica la forma correcta en una frase nueva.",
        "Una buena meta no dice «hablar mejor», sino algo concreto: «usar el pasado correctamente en tres frases» o «mirar al público cada cinco segundos». Revisa tus metas después de la siguiente presentación y escribe si las lograste. Así avanzas paso a paso.",
    ],
    [("strength", "fortaleza"), ("weakness", "debilidad"), ("goal", "meta"), ("checklist", "lista de verificación"), ("record", "registrar"), ("resource", "recurso de ayuda")],
    [
        ("Meta concreta", "¿Cuál es una meta concreta? A) Next time I will use two connectors. B) I want to be better.", ["Debe ser medible.", "Dos conectores se puede contar.", "La A."], "A"),
        ("Registrar error", "Error: «He have a dog.» ¿Cuál es la corrección? A) He has a dog. B) He haves a dog.", ["La tercera persona usa has.", "La A es correcta.", "La B no existe."], "A"),
    ],
    [
        ("Escribir una meta general como «hablar mejor».", "No se puede comprobar si se logró.", "Escribe una meta que se pueda contar o medir."),
        ("Anotar el error sin su corrección.", "No sirve para aprender.", "Escribe siempre el error y la forma correcta."),
    ],
    [
        ("Lee: " + LOG + " ¿Cuántos errores registró? A) tres B) cinco", "A", "Aparecen Error 1, Error 2 y Error 3."),
        ("Lee: " + FEED + " ¿Qué dijo el compañero que estuvo claro? A) la pronunciación de student B) el volumen", "A", "Dice Your pronunciation of student was clear."),
        ("Lee: " + LOG + " ¿Qué recurso nombra el registro? A) un diccionario en línea B) una radio", "A", "Dice Recurso: un diccionario en línea."),
    ],
    [
        ("Lee: " + FEED + " ¿Qué debilidad señala el compañero? A) habló muy rápido al final B) habló muy bajo", "A", "Dice You spoke too fast at the end."),
        ("Lee: " + LOG + " ¿Cuál es la corrección de I am agree? A) I agree B) I am agreed", "A", "En inglés se dice I agree."),
        ("Lee: " + LOG + " ¿Cuál es la meta registrada? A) cometer menos de tres errores en la próxima conversación B) hablar más fuerte", "A", "La meta está escrita en el registro."),
    ],
    [
        ("Lee: " + FEED + " ¿Qué fortaleza aparece además de la pronunciación? A) un buen ejemplo B) mucho contacto visual", "A", "Dice You used a good example."),
        ("Lee: " + FEED + " ¿Qué meta se desprende de Forgot to look at the audience? A) mirar a la audiencia en cada idea B) hablar más rápido", "A", "La debilidad se convierte en una meta concreta."),
        ("Lee: " + LOG + " Corrige: «She don’t like fish.» A) She doesn’t like fish. B) She not like fish.", "A", "Con she se usa doesn’t."),
    ],
    [
        ("Lee: " + LOG + " ¿Por qué el registro ayuda? A) permite ver si se repiten los errores B) permite olvidar los errores", "A", "Anotar errores y correcciones muestra patrones."),
        ("Lee: " + FEED + " Una estudiante dice que no tiene debilidades. ¿Qué dato lo contradice? A) el compañero señaló que habló rápido y que no miró a la audiencia B) el compañero dijo que habló fuerte", "A", "Hay dos debilidades señaladas."),
    ],
    [
        ("Ordena el ciclo de mejora: a) establecer una meta b) identificar una debilidad c) practicar con un recurso", "b, a, c", "Primero se identifica el problema, luego se fija una meta y después se practica."),
        ("Lee: " + LOG + " Elige la corrección de «I have 15 years»: A) I am 15 years old. B) I have 15 old.", "A", "En inglés la edad se dice con to be."),
    ],
    [("Lee: «Goal: I will check my verbs in the past before the next speaking activity.» (check = revisar). ¿Qué hará la estudiante antes de la próxima actividad?", "Revisar los verbos en pasado", "Dice I will check my verbs in the past.")],
    [
        ("¿Qué se registra en un registro de errores?", "El error y su corrección", "Sirve para aprender."),
        ("¿Qué características tiene una buena meta?", "Es concreta y medible", "Se puede comprobar."),
        ("¿Qué recurso puede ayudar a corregir?", "Un diccionario en línea", "Ayuda con palabras y formas."),
    ],
    task("Después de tu última presentación o conversación en inglés (si no tienes una, habla un minuto sobre tu día a una persona de tu casa), escribe: dos fortalezas, dos debilidades, una meta concreta y un registro de dos errores con su corrección. Indica qué recurso usaste para corregir.", "Ejemplo: Fortalezas: buen volumen, ejemplos claros. Debilidades: hablé rápido, olvidé el pasado. Meta: usaré tres verbos en pasado. Error: I go yesterday → I went yesterday. Recurso: tabla de verbos.", ["dice dos fortalezas y dos debilidades", "la meta es concreta", "registra errores con corrección y recurso"], ["hoja con las respuestas"], ["escribir una meta general", "no incluir la corrección"], "Guarda tu registro y revísalo después de tu próxima presentación."),
    "Escribe un registro de cinco errores comunes y su corrección.",
    "Compara tu meta con la de otro compañero y escribe cómo medir si la lograste.",
)

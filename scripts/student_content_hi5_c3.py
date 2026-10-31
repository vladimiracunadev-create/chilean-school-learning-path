"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 22 (informarse y opinar con periódicos y TIC)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA22 = "HI05 OA 22"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA22, 1,
    materials="Este cuaderno y un lápiz. Las noticias de ejemplo son inventadas y están escritas en los ejercicios. Si quieres, usa un periódico o un sitio de noticias con ayuda de una persona de tu casa.",
    use="Aprenderé a leer una noticia y a ubicar sus partes y sus datos básicos: qué pasó, quién, dónde, cuándo y en qué sección va. Sirve para informarme sobre temas del país y del mundo.",
    prior=["Sé ubicar un tema en el tiempo y el espacio.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Un periódico es una publicación que informa sobre lo que ocurre, en papel o en internet. Se ordena en secciones, que son partes por tema: política, medioambiente, deportes, arte y música, mundo y país. Las tecnologías de la información y la comunicación, llamadas TIC, incluyen sitios de internet, radio, televisión y aplicaciones. Con ellas podemos informarnos y también opinar.",
        "Una noticia tiene partes. El titular es el título corto. La bajada es una frase que amplía el titular. El cuerpo cuenta los detalles. También indica la fecha y el lugar. Para leerla bien respondo cinco preguntas: ¿qué pasó?, ¿quiénes participaron?, ¿dónde?, ¿cuándo? y ¿por qué ocurrió? Así ubico la información en el tiempo y el espacio, igual que con cualquier tema de la asignatura.",
        "Ejemplo inventado: «Ciudad Sol planta 500 árboles. El municipio de Ciudad Sol (comuna inventada) plantó 500 árboles el sábado en el parque central, con ayuda de 40 vecinos». Está en la sección medioambiente. Qué: plantó árboles. Quiénes: municipio y vecinos. Dónde: parque central de Ciudad Sol. Cuándo: el sábado. Con esta ficha entiendo la noticia y puedo opinar sobre ella con fundamentos.",
    ],
    vocab=[("periódico", "publicación que informa sobre lo que ocurre"), ("sección", "parte del periódico dedicada a un tema"), ("titular", "título corto de una noticia"), ("bajada", "frase que amplía el titular"), ("TIC", "tecnologías de la información y la comunicación")],
    worked=[
        W("Ubicar la sección", "Noticia: «Equipo de ciudad inventada gana la copa de natación». ¿En qué sección va: deportes o arte y música?",
          ["El tema es una competencia.", "La natación es un deporte.", "La sección es deportes."], "Deportes"),
        W("Responder las preguntas", "«Ciudad Sol planta 500 árboles el sábado en el parque central, con 40 vecinos». ¿Cuándo y quiénes?",
          ["Cuándo: busco la fecha.", "Dice el sábado.", "Quiénes: el municipio y 40 vecinos."], "El sábado; el municipio y 40 vecinos"),
    ],
    mistakes=[
        M("Leer solo el titular y creer que ya sé todo.", "El titular es corto y deja afuera detalles.", "Lee el cuerpo y responde las cinco preguntas."),
        M("Confundir la sección con el lugar donde ocurre el hecho.", "La sección es el tema; el lugar es otro dato.", "Pregunta por separado de qué tema es y dónde ocurre."),
    ],
    tiers=tiers(
        [ex("¿Qué es un periódico?", "Una publicación que informa sobre lo que ocurre", "Puede ser de papel o de internet."),
         ex("¿Cómo se llama el título corto de una noticia?", "Titular", "Es la primera parte que se lee."),
         ex("¿Qué significan las siglas TIC?", "Tecnologías de la información y la comunicación", "Incluyen internet, radio y televisión.")],
        [ex("¿Qué hace la bajada de una noticia?", "Amplía el titular", "Da un poco más de información."),
         ex("¿Para qué sirven las secciones de un periódico?", "Para ordenar las noticias por tema", "Facilitan encontrar lo que interesa."),
         ex("De las cinco preguntas para leer una noticia, ¿cuál pide la fecha o el momento del hecho?", "¿Cuándo?", "Pregunta por el tiempo.")],
        [ex("Noticia inventada: «Una banda de ciudad inventada da un concierto de música en la plaza». ¿En qué sección va: política o arte y música?", "Arte y música", "El tema es un concierto."),
         ex("«Vecinos de Ciudad Sol limpian la orilla del río el domingo». ¿Cuándo ocurrió?", "El domingo", "Es el dato de tiempo."),
         arith("En el parque central de Ciudad Sol se plantaron 500 árboles y antes había 120. ¿Cuántos árboles hay ahora?", "500+120", "Se suman los nuevos y los que había.", unit=" árboles")],
        [ex("Un compañero lee solo el titular «Ciudad Sol gana el campeonato» y dice que sabe quiénes jugaron y dónde. ¿Qué le sugieres?", "Leer el cuerpo de la noticia", "El titular no entrega todos los detalles."),
         ex("Un lector dice: «La noticia está en la sección medioambiente, así que ocurrió en un lugar llamado Medioambiente». ¿Qué confusión tiene?", "Confunde la sección con el lugar", "La sección es el tema.")],
        [ex("Ordena las partes de una noticia desde lo que se lee primero: A) cuerpo, B) titular, C) bajada.", "B, C, A", "Primero el titular, luego la bajada y al final el cuerpo."),
         ex("Noticia inventada: «El domingo, 30 estudiantes presentaron una obra de teatro en el centro cultural de Ciudad Sol». ¿Qué pregunta responde el dato «30 estudiantes»?", "¿Quiénes participaron?", "Nombra a quienes participaron.")],
    ),
    context=[ex("Escuchas en la radio: «El concejo de una comuna inventada aprobó el presupuesto del próximo año». ¿Qué sección corresponde: política, deportes o arte y música?", "Política", "Trata de una decisión de autoridades.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es una sección de un periódico?", "Una parte dedicada a un tema", "Ordena las noticias."), ex("¿Qué son las TIC?", "Tecnologías de la información y la comunicación", "Permiten informarse y opinar."), ex("¿Qué cinco preguntas se responden al leer una noticia?", "Qué, quiénes, dónde, cuándo y por qué", "Ubican la información.")],
    open_task=task("Lee esta noticia inventada: «Vecinos de Ciudad Sol limpian el río. El sábado, 60 vecinos recogieron 200 bolsas de basura de la orilla del río Claro, organizados por el club de scouts, porque la orilla estaba llena de basura». Responde las cinco preguntas, escribe en qué sección iría y escribe una opinión con una razón.", "Qué: recogieron 200 bolsas de basura. Quiénes: 60 vecinos y el club de scouts. Dónde: orilla del río Claro. Cuándo: el sábado. Por qué: la orilla estaba llena de basura. Sección: medioambiente. Opino que fue buena idea porque el río quedó más limpio.", ["cinco preguntas", "sección correcta", "opinión con razón"], ["ficha de la noticia y opinión"], ["leer solo el titular", "confundir sección con lugar"], "Lee una noticia real con una persona de tu casa y completa la misma ficha."),
    reinforce="Con ayuda de una persona de tu casa, mira los titulares de hoy y di en qué sección irían.",
    extend="Inventa una noticia corta de deportes y escribe sus cinco datos.",
)

register(
    OA22, 2,
    materials="Este cuaderno y un lápiz. Las notas de ejemplo son inventadas y están escritas en los ejercicios. Si usas internet, hazlo con una persona de tu casa.",
    use="Aprenderé a distinguir noticia de opinión, a revisar de dónde viene la información y a usar las TIC con cuidado. Sirve para informarme sin creer cualquier cosa y para proteger mis datos.",
    prior=["Sé leer una noticia y responder las cinco preguntas.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Los medios de comunicación entregan información de varias formas. Una noticia cuenta un hecho con datos. Una columna o editorial entrega la opinión de una persona o del medio. Una carta al director es la opinión de un lector. Por eso, al leer, pregunto: ¿esto cuenta un hecho o da una opinión? Una opinión puede tener buenas razones, pero no es lo mismo que un hecho comprobado.",
        "Para decidir si confío en una información reviso la procedencia: ¿qué medio la publicó?, ¿quién firma?, ¿hay fecha?, ¿da datos y fuentes? Desconfío de titulares muy exagerados, de mensajes sin autor y de los que piden compartir rápido. Si es importante, comparo con otro medio. Cuando dos medios independientes cuentan lo mismo con datos parecidos, la información es más confiable.",
        "En internet debo cuidarme. No comparto nombre completo, dirección, teléfono ni fotos de mi casa. Si un sitio pide datos personales, consulto con una persona adulta. Al comentar, escribo con respeto, como lo haría frente a la persona. Y si algo me parece peligroso, falso o me incomoda, aviso a una persona adulta de confianza.",
    ],
    vocab=[("noticia", "relato de un hecho con datos"), ("editorial", "texto que entrega la opinión de un medio"), ("carta al director", "texto en que un lector da su opinión"), ("desinformación", "información falsa o engañosa que circula como verdadera"), ("datos personales", "información que identifica a una persona")],
    worked=[
        W("Noticia u opinión", "«El municipio abrió ayer una plaza con 20 bancas». «La plaza nueva es horrible». ¿Cuál es noticia y cuál opinión?",
          ["La primera cuenta un hecho con datos.", "La segunda dice cómo se ve para alguien.", "Se clasifican."], "La primera es noticia y la segunda es opinión"),
        W("Revisar la procedencia", "Mensaje sin autor ni fecha: «¡Urgente! Reparten mochilas gratis, comparte ya». ¿Qué haces?",
          ["No sé quién lo escribió.", "Pide compartir con prisa.", "Pregunto a una persona adulta antes de compartir."], "No lo comparto y consulto a una persona adulta"),
    ],
    mistakes=[
        M("Compartir un mensaje solo porque llama la atención.", "Puede ser desinformación.", "Revisa la fuente y consulta a una persona adulta."),
        M("Poner mis datos personales en un comentario o formulario.", "Cualquiera podría usarlos.", "Pide ayuda antes de escribir datos."),
    ],
    tiers=tiers(
        [ex("¿Qué es una noticia?", "El relato de un hecho con datos", "Cuenta lo que ocurrió."),
         ex("¿Qué es una carta al director?", "Un texto en que un lector da su opinión", "Se publica en el medio."),
         ex("¿Qué es la desinformación?", "Información falsa o engañosa que circula como verdadera", "Engaña a quienes la leen.")],
        [ex("¿Qué diferencia hay entre una noticia y un editorial?", "La noticia cuenta un hecho y el editorial da una opinión", "Tienen funciones distintas."),
         ex("¿Por qué conviene desconfiar de un mensaje sin autor que pide compartir rápido?", "Porque puede ser desinformación", "No se puede comprobar su origen."),
         ex("¿Qué haces si un sitio te pide tu dirección y tu teléfono?", "Consultar a una persona adulta antes", "Protege tus datos.")],
        [ex("Elige el hecho: A) «La plaza nueva es lo mejor del barrio.» B) «La plaza nueva tiene 20 bancas.»", "B", "Se puede comprobar contando."),
         ex("Dos medios distintos cuentan que una corrida familiar terminó el domingo con 300 participantes. ¿Esa información es más o menos confiable?", "Más confiable", "Coinciden en datos."),
         ex("Elige el dato personal que no debes compartir: A) tu dirección de casa, B) tu color favorito.", "A", "Identifica dónde vives.")],
        [ex("Un amigo dice: «Lo vi en un mensaje y mucha gente lo compartió, entonces es verdad». ¿Qué le respondes?", "Que mucha gente lo comparta no prueba que sea verdad", "Compartir no comprueba hechos."),
         ex("Una columna dice «Este equipo es el mejor del país». ¿Es una noticia o una opinión? Responde y da una razón.", "Una opinión, porque dice «el mejor» y eso depende de quien opina", "No se mide con un dato.")],
        [ex("Ordena para revisar una información dudosa: A) comparar con otro medio, B) mirar quién firma y la fecha, C) decidir si la comparto o no.", "B, A, C", "Primero la procedencia, luego comparar y al final decidir."),
         ex("Un titular dice «¡Increíble! Todos los niños de Chile dejarán de ir al colegio». ¿Qué parte te hace desconfiar?", "El tono exagerado y la palabra «todos»", "Los titulares exagerados suelen engañar.")],
    ),
    context=[ex("Te llega un mensaje que dice «gana un premio, escribe tu nombre completo y tu dirección». ¿Qué haces?", "No contestar y avisar a una persona adulta", "Pide datos personales de manera sospechosa.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es un editorial?", "Un texto con la opinión de un medio", "No es una noticia."), ex("¿Qué se revisa en la procedencia?", "Qué medio, quién firma y la fecha", "Permite confiar o no."), ex("¿Qué datos no debo compartir en internet?", "Nombre completo, dirección y teléfono", "Protegen mi seguridad.")],
    open_task=task("Lee estas dos frases inventadas del mismo medio. Frase 1: «El sábado se corrió una corrida familiar de 5 km con 300 personas». Frase 2: «Esta corrida fue la más emocionante de todas». Escribe cuál es noticia y cuál opinión, qué preguntas de procedencia harías y una regla para cuidar tus datos si comentas en internet.", "Frase 1 es noticia porque tiene fecha y cifras. Frase 2 es opinión porque dice «la más emocionante». Preguntaría quién firma y la fecha. Regla: no escribir mi dirección ni mi nombre completo.", ["noticia y opinión separadas", "dos preguntas de procedencia", "una regla de seguridad"], ["clasificación y reglas"], ["compartir sin revisar", "dar datos personales"], "Comenta tus respuestas con una persona de tu casa y verifica si coinciden."),
    reinforce="Con una persona de tu casa, di una frase de noticia y una de opinión sobre tu comida favorita.",
    extend="Inventa un titular exagerado y reescríbelo con datos para que informe mejor.",
)

register(
    OA22, 3,
    materials="Este cuaderno y un lápiz. Las noticias son inventadas y están escritas en los ejercicios.",
    use="Aprenderé a leer una noticia buscando causas, actores y consecuencias, tanto del país como del mundo. Sirve para entender por qué pasan las cosas y qué cambia después.",
    prior=["Sé responder las cinco preguntas de una noticia.", "Sé distinguir noticia de opinión."],
    explain=[
        "Las noticias hablan de temas muy distintos: política, medioambiente, deportes, arte y música. En todas puedo buscar causas, actores y consecuencias. La causa responde por qué ocurrió. Los actores son quienes participan, como autoridades, vecinos, deportistas o artistas. La consecuencia es lo que cambia o se espera que cambie. Esas tres cosas convierten un dato suelto en una explicación.",
        "Ejemplo inventado de medioambiente: «Ciudad Sol prohíbe las bolsas plásticas en los negocios desde el 1 de marzo, porque llegaban muchas al río». Causa: las bolsas llegaban al río. Actor: el municipio y los negocios. Consecuencia esperada: menos basura en el río. Ejemplo de política local: «El centro de estudiantes organiza una votación para elegir un juego del recreo». Actores: estudiantes. Consecuencia: el juego más votado se usará.",
        "Hay noticias del país y del mundo. Una noticia del país sucede en Chile y afecta a personas cercanas. Una noticia del mundo sucede en otros países, y a veces también afecta a Chile, por ejemplo si cambia el precio de algo que se compra en otro lugar. Al leer, pregunto: ¿a quién afecta este hecho?, ¿hay efectos que ocurren pronto y otros que ocurren después? Así preparo una opinión mejor fundamentada.",
    ],
    vocab=[("causa", "razón por la que ocurre un hecho"), ("consecuencia", "lo que cambia a raíz del hecho"), ("actor", "persona o grupo que participa"), ("local", "de un lugar cercano"), ("internacional", "de otros países o que involucra a más de un país")],
    worked=[
        W("Causa y consecuencia en una noticia", "«Ciudad Sol prohíbe las bolsas plásticas porque llegaban muchas al río». ¿Cuál es la causa y cuál la consecuencia esperada?",
          ["La causa es lo que explica la prohibición.", "Llegaban bolsas al río.", "Se espera menos basura en el río."], "Causa: las bolsas llegaban al río; consecuencia: menos basura en el río"),
        W("Nombrar actores", "«El centro de estudiantes organiza una votación para elegir un juego del recreo». ¿Quiénes son los actores?",
          ["Busco quién organiza.", "Organiza el centro de estudiantes.", "Votan los estudiantes."], "El centro de estudiantes y los estudiantes que votan"),
    ],
    mistakes=[
        M("Pensar que la noticia solo cuenta lo que pasó y no sus causas.", "Se pierde la explicación.", "Pregunta por qué ocurrió y quiénes participaron."),
        M("Opinar sin pensar en quién se ve afectado.", "La opinión queda parcial.", "Nombra a los actores y a los afectados antes de opinar."),
    ],
    tiers=tiers(
        [ex("En una noticia, ¿qué responde la causa?", "Por qué ocurrió el hecho", "La causa explica el origen."),
         ex("En una noticia, ¿qué es un actor?", "Una persona o grupo que participa", "Hay actores en cada hecho."),
         ex("En Ciencias Sociales: ¿qué es una noticia internacional?", "La que trata de otros países o involucra a más de un país", "Sale de los límites de un solo país.")],
        [ex("¿Por qué conviene buscar la causa de un hecho de la noticia?", "Para entender por qué ocurrió", "La causa explica el hecho."),
         ex("¿Qué diferencia hay entre una noticia local y una internacional?", "La local ocurre cerca y la internacional trata de otros países o de varios a la vez", "Cambia la escala del hecho."),
         ex("¿Por qué hay que pensar en quién se ve afectado antes de opinar?", "Porque una opinión debe considerar a las personas que viven el hecho", "Así no es parcial.")],
        [ex("«El municipio de la comuna inventada de Mar Azul prohíbe tirar basura en la playa porque el año pasado se recogieron muchos desechos». ¿Cuál es la causa?", "Que el año pasado se recogieron muchos desechos", "Explica la prohibición."),
         ex("«Un equipo cambia su horario de entrenamiento por el calor». ¿Cuál es la causa del cambio?", "El calor", "Explica la decisión."),
         ex("En «El centro de estudiantes organiza una votación para elegir un juego del recreo», ¿cuál es la consecuencia esperada?", "Se usará el juego más votado", "Es lo que cambia después.")],
        [ex("Un lector dice que «esa prohibición de bolsas perjudica a todos» sin nombrar a nadie. ¿Qué le preguntas?", "A quiénes perjudica y por qué", "Pide actores y consecuencias."),
         ex("Una noticia dice que un festival de música cambió de fecha. El lector solo opina «qué mal». ¿Qué le falta para fundamentar su opinión?", "Saber la causa y a quiénes afecta", "Una opinión necesita razones.")],
        [ex("Ordena la explicación: A) menos basura llega al río, B) llegaban muchas bolsas al río, C) el municipio prohíbe las bolsas plásticas.", "B, C, A", "Primero la causa, luego la decisión y al final la consecuencia."),
         arith("En una noticia de medioambiente de un pueblo inventado, 8 vecinos plantaron 5 árboles cada uno. ¿Cuántos árboles plantaron en total?", "8*5", "Se multiplica el número de vecinos por los árboles de cada uno.", unit=" árboles")],
    ),
    context=[ex("Una noticia internacional inventada dice que un país vecino tuvo una sequía muy larga. ¿Qué pregunta te ayuda a ver si afecta a Chile?", "A quién afecta y si hay efectos en Chile", "Conecta el hecho con el país.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es una consecuencia en una noticia?", "Lo que cambia a raíz del hecho", "Ocurre después del hecho."), ex("¿Qué es un actor?", "Una persona o grupo que participa", "Hay varios actores."), ex("¿Qué pregunta busca la causa?", "Por qué ocurrió", "Se responde en la noticia.")],
    open_task=task("Lee esta noticia inventada: «Mar Azul crea una ciclovía en la costanera desde mayo, porque muchos vecinos se movían en bicicleta y no había un lugar seguro. El municipio y un club de ciclistas ayudaron a planificarla». Escribe una causa, dos actores y una consecuencia esperada. Después escribe tu opinión con una razón basada en una consecuencia.", "Causa: no había lugar seguro para bicicletas. Actores: municipio y club de ciclistas. Consecuencia: viajes más seguros. Opino que fue buena idea porque protege a quienes usan bicicleta.", ["una causa", "dos actores", "una consecuencia", "opinión con razón"], ["lista de causa, actores y consecuencia y una opinión"], ["opinar sin razón", "no nombrar actores"], "Busca una noticia con una persona de tu casa y completa la misma lista."),
    reinforce="Inventa una noticia de deportes y di su causa y su consecuencia.",
    extend="Explica un ejemplo de noticia del mundo que podría afectar a Chile.",
)

register(
    OA22, 4,
    materials="Este cuaderno y un lápiz. Las dos notas de ejemplo son inventadas y están escritas en los ejercicios.",
    use="Aprenderé a comparar cómo dos medios cuentan lo mismo y a expresar mi opinión con respeto en cartas, comentarios y foros. Sirve para participar con ideas bien apoyadas, de forma segura, en la vida pública.",
    prior=["Sé buscar causas, actores y consecuencias en una noticia.", "Sé revisar la procedencia de una fuente y cuidar mis datos."],
    explain=[
        "Dos medios pueden contar el mismo hecho de manera distinta. Cambian el titular, los datos que destacan o a quién escuchan. Por ejemplo, ante un nuevo paseo en la costanera, un medio puede destacar la seguridad y otro el ruido para los vecinos. Para compararlos anoto: qué hecho cuentan, qué datos comparten, qué datos son distintos y a quién escuchan. Así veo si falta alguna perspectiva.",
        "Después formo mi opinión. Primero separo los hechos que coinciden de las partes que son opinión. Luego decido qué pienso y por qué, con razones y datos de las dos notas. Puedo cambiar de opinión si encuentro un dato nuevo. No tengo que estar de acuerdo con ningún medio, pero sí debo explicar mis razones.",
        "Para expresar mi opinión puedo usar una carta al director, un comentario con ayuda de una persona adulta, un foro del curso o una exposición oral. Reglas para opinar con respeto: critico la idea y no a la persona, uso palabras claras, no comparto datos personales, no repito rumores y cito la fuente de mis datos. Si veo mensajes ofensivos, no respondo con otro ofensivo y aviso a una persona adulta.",
    ],
    vocab=[("perspectiva", "manera de mirar un tema según quién lo cuenta"), ("destacar", "poner en primer plano un dato"), ("foro", "espacio donde varias personas conversan sobre un tema"), ("citar la fuente", "decir de dónde viene un dato"), ("respeto", "consideración hacia quien piensa distinto")],
    worked=[
        W("Comparar dos notas", "Medio A: «Nueva ciclovía en Mar Azul: más seguridad para ciclistas». Medio B: «Nueva ciclovía en Mar Azul: vecinos reclaman por ruido». ¿Qué destaca cada uno?",
          ["Miro cada titular.", "A destaca la seguridad.", "B destaca el reclamo de vecinos."], "A destaca la seguridad y B el reclamo por el ruido"),
        W("Opinar con respeto", "Quieres comentar la noticia de la ciclovía. Escribe una frase respetuosa con una razón.",
          ["Doy mi opinión.", "Agrego una razón.", "No ofendo a nadie."], "Creo que la ciclovía es buena porque protege a quienes usan bicicleta, aunque entiendo la preocupación por el ruido"),
    ],
    mistakes=[
        M("Creer que un medio cuenta todo el hecho.", "Cada medio puede destacar solo una parte.", "Compara al menos dos notas antes de opinar."),
        M("Responder con insultos a un comentario que me molesta.", "Eso no argumenta y puede ser dañino.", "Responde con una razón o avisa a una persona adulta."),
    ],
    tiers=tiers(
        [ex("¿Qué significa «destacar» un dato en una noticia?", "Ponerlo en primer plano", "Es una elección del medio."),
         ex("¿Qué es un foro?", "Un espacio donde varias personas conversan sobre un tema", "Puede ser en internet o en la sala."),
         ex("¿Qué es citar la fuente de un dato?", "Decir de dónde viene el dato", "Permite comprobar el dato.")],
        [ex("¿Por qué conviene comparar dos notas sobre el mismo hecho?", "Porque cada medio puede mostrar solo una parte", "Así se ve la información completa."),
         ex("¿Qué cuatro cosas anotas para comparar dos notas?", "Qué hecho cuentan, qué datos comparten, cuáles son distintos y a quién escuchan", "Ordenan la comparación."),
         ex("¿Qué haces si ves un mensaje ofensivo?", "No respondo con otro ofensivo y aviso a una persona adulta", "Evita que el conflicto crezca.")],
        [ex("Medio A: «Hay 40 bicicletas en la ciclovía cada hora». Medio B: «Hay 40 bicicletas por hora y 3 vecinos se quejaron». ¿Qué dato extra tiene B?", "Que 3 vecinos se quejaron", "Aparece solo en B."),
         ex("Elige el comentario respetuoso: A) «Esos reclamos son una tontería.» B) «Entiendo el reclamo por ruido, pero creo que la seguridad es más importante.»", "B", "Critica la idea sin ofender."),
         ex("Una opinión tuya cita: «Según el informe del municipio de Mar Azul, hay 40 bicicletas por hora». ¿Qué parte es la fuente?", "El informe del municipio de Mar Azul", "Dice de dónde sale el dato.")],
        [ex("Un compañero dice: «Mi medio favorito siempre tiene la razón». ¿Qué error tiene?", "Ningún medio cuenta todo ni siempre acierta", "Hay que comparar fuentes."),
         ex("Alguien comenta un rumor sin decir de dónde salió. ¿Qué debes hacer antes de repetirlo?", "Buscar la fuente y comprobarlo", "Un rumor sin fuente puede ser falso.")],
        [ex("Ordena una carta al director: A) cito una razón con datos, B) saludo y presento el tema, C) cierro con una propuesta respetuosa.", "B, A, C", "Presenta, argumenta y propone."),
         ex("Quieres citar la fuente de «Hay 40 bicicletas por hora». ¿Qué comienzo sirve: A) «Según el conteo del municipio de Mar Azul, …» o B) «Dicen por ahí que …»?", "A", "Dice quién entrega el dato.")],
    ),
    context=[ex("En el foro del curso alguien escribe «el recreo largo es una pérdida de tiempo». Tú no estás de acuerdo. ¿Cómo respondes: con una razón o con un insulto?", "Con una razón", "Un debate respetuoso usa argumentos.")],
    selfcheck=[ex("En Ciencias Sociales: ¿qué es una perspectiva?", "Una manera de mirar un tema según quién lo cuenta", "Cambia entre medios."), ex("¿Qué es una carta al director?", "Una carta en que un lector da su opinión", "Es una forma de participar."), ex("¿Cómo opino con respeto?", "Critico la idea, doy razones y cito la fuente", "Evita ofender a otras personas.")],
    open_task=task("Lee estas dos notas inventadas. Nota A: «Plaza nueva en Mar Azul tiene 20 bancas y juegos para niños». Nota B: «Vecinos de Mar Azul reclaman por falta de sombra en la plaza nueva». Escribe qué destaca cada una, qué dato comparten y un comentario respetuoso de tres frases con tu opinión, una razón y una propuesta.", "A destaca bancas y juegos; B destaca la falta de sombra. Comparten que la plaza es nueva. Comentario: Creo que la plaza es útil porque tiene juegos. Entiendo que falta sombra. Propongo plantar árboles.", ["comparación de dos notas", "dato compartido", "comentario respetuoso con razón y propuesta"], ["comparación y comentario de tres frases"], ["insultar", "usar datos personales"], "Lee tu comentario a una persona de tu casa y pídele que diga si es respetuoso."),
    reinforce="Con una persona de tu casa, di dos formas de contar un mismo recreo.",
    extend="Escribe una regla más para participar con respeto en un foro del curso.",
)

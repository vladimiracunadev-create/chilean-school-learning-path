"""Cuaderno del estudiante, 6.º básico Orientación: OA 05 (drogas: causas, consecuencias y prevención) y OA 06 (solidaridad y respeto)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or6_a import M, T, W, lesson

OA5, OA6 = "OR06 OA 05", "OR06 OA 06"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. Las listas y los casos de personajes inventados están escritos en los ejercicios. Nadie debe contar experiencias personales.",
    "Aprenderé qué son las drogas más comunes (tabaco, alcohol y marihuana), por qué alguien podría consumirlas y qué consecuencias traen. Sirve para decidir con información y cuidarme.",
    ["Sé que mi cuerpo y mi cerebro necesitan cuidado.", "Sé que puedo pedir ayuda a un adulto de confianza."],
    [
        "Una droga es una sustancia que, al entrar al cuerpo, cambia cómo funciona el cerebro y el resto del organismo. El tabaco contiene nicotina, que genera dependencia: el cuerpo la pide y cuesta dejarla. El alcohol es una droga legal para adultos, pero su venta a menores de edad está prohibida. La marihuana afecta la atención, la memoria y el aprendizaje, y en menores de edad es especialmente dañina porque el cerebro todavía está en desarrollo.",
        "Las personas pueden empezar a consumir por distintas causas: curiosidad, presión de amigos o del grupo, imitar a adultos, querer calmar el estrés o la tristeza, o por no tener información. Todas estas causas se pueden enfrentar de otra forma. Las consecuencias pueden ser físicas (daño a pulmones, hígado o cerebro), emocionales (ansiedad o cambios de ánimo), escolares (menos atención y más faltas) y sociales (problemas con la familia y los amigos). Además, el consumo puede llevar a la dependencia, que es no poder dejarlo aunque se quiera.",
        "Conocer las causas y consecuencias ayuda a decidir bien. Que algo sea común o aparezca en películas no significa que sea inofensivo. Si alguien cercano consume o tú tienes dudas, puedes hablar con un adulto de confianza o llamar a una línea de ayuda como el Fono Drogas y Alcohol 1412.",
    ],
    [("droga", "sustancia que cambia el funcionamiento del cerebro y del cuerpo"), ("dependencia", "necesidad del cuerpo de seguir consumiendo y dificultad para dejarlo"), ("nicotina", "sustancia del tabaco que genera dependencia"), ("consecuencia", "lo que ocurre después de una decisión"), ("causa", "razón por la que algo ocurre")],
    [
        W("Relacionar causa y consecuencia", "Un primo inventado empezó a fumar porque sus amigos lo hacían. Ahora le cuesta dejarlo. ¿Cuál fue la causa y cuál la consecuencia?", ["Empezó por presión de amigos: esa es la causa.", "Ahora le cuesta dejarlo: eso es la dependencia.", "La dependencia es la consecuencia."], "Causa: presión de amigos. Consecuencia: dependencia"),
        W("Corregir una idea falsa", "Un compañero dice: «El alcohol no hace daño porque es legal». ¿Es correcto?", ["Es legal solo para adultos.", "Puede dañar el hígado y el cerebro.", "Que sea legal no lo hace inofensivo."], "No es correcto"),
    ],
    [
        M("Pensar que lo que es legal para adultos no daña a nadie.", "Se confunde permiso legal con seguridad.", "Recuerda que legal no significa inofensivo, y que a menores se les prohíbe."),
        M("Creer que probar una sola vez no tiene riesgo.", "Se piensa que el daño solo viene con mucho consumo.", "Algunas sustancias generan dependencia o dañan el cerebro en desarrollo."),
    ],
    R=[
        ex("¿Qué sustancia del tabaco genera dependencia: la nicotina o el agua?", "La nicotina", "Es la sustancia que hace que el cuerpo la pida."),
        ex("La dependencia, ¿es poder dejar una sustancia cuando uno quiere o dificultad para dejarla?", "Dificultad para dejarla", "El cuerpo la pide aunque la persona quiera dejarla."),
        ex("¿La venta de alcohol a menores de edad está permitida en Chile? Responde sí o no.", "No", "La ley chilena lo prohíbe."),
    ],
    U=[
        ex("¿Por qué la marihuana es especialmente dañina para menores de edad?", "Porque su cerebro aún está en desarrollo", "Afecta la atención, la memoria y el aprendizaje."),
        ex("¿Por qué una película que muestra consumo no prueba que sea inofensivo?", "Porque una película no es una fuente de salud", "Muestra una historia, no los daños reales."),
        ex("Una causa del consumo es la presión de amigos. ¿Es una causa o una consecuencia?", "Una causa", "Es una razón por la que alguien podría empezar."),
    ],
    A=[
        ex("Lista: 1) daño en pulmones; 2) presión de amigos; 3) dificultad para dejarlo; 4) curiosidad; 5) faltas al colegio. ¿Cuántas son consecuencias?", "3", "Las consecuencias son daño en pulmones, dificultad para dejarlo y faltas al colegio; la presión y la curiosidad son causas."),
        ex("Clasifica «menos atención en clases por consumir marihuana»: ¿es una consecuencia escolar o una causa?", "Una consecuencia escolar", "Afecta el aprendizaje después del consumo."),
        ex("Una persona dice que fuma para calmar el estrés. ¿Qué causa del consumo es? A) Presión de grupo. B) Querer calmar una emoción o el estrés. C) Falta de información.", "B", "Fuma para sentirse mejor frente al estrés."),
    ],
    Z=[
        ex("¿Por qué «todos lo hacen» no es una buena razón para consumir?", "Porque no es cierto ni prueba que sea seguro", "Que muchos lo hagan no elimina los daños."),
        ex("¿Por qué conocer las consecuencias ayuda a decidir mejor?", "Porque permite prever los daños antes de actuar", "Con información se elige con más libertad."),
    ],
    D=[
        arith("En un curso de 34 estudiantes, 9 dicen que la presión de amigos es la causa más común. ¿Cuántos opinan algo distinto?", "34-9", "Se restan los que eligieron esa causa al total."),
        arith("Una persona inventada gasta $3.000 por semana en cigarrillos. ¿Cuánto gasta en 4 semanas?", "3000*4", "Se multiplica el gasto semanal por las semanas."),
    ],
    context=[ex("Un joven de 15 años inventado dice: «Yo solo fumo con mis amigos los fines de semana y no me pasa nada». Cuatro meses después, le cuesta dejar de fumar y se agita al correr. ¿Qué consecuencias aparecieron?", "Dependencia y menos aguante físico", "Le cuesta dejarlo y se agita al correr, señales de dependencia y daño respiratorio.")],
    selfcheck=[ex("En Orientación: ¿la nicotina genera dependencia?", "Sí", "Por eso cuesta dejar el tabaco."), ex("¿Una sustancia legal para adultos es inofensiva para todos?", "No", "Puede dañar, y a menores se les prohíbe."), ex("¿Conocer las consecuencias ayuda a decidir mejor?", "Sí", "Permite elegir con información.")],
    task=T("Completa una tabla para los tres casos de personajes inventados: (1) Leo prueba tabaco por curiosidad; (2) Sofi bebe alcohol porque sus primos lo hacen; (3) Teo prueba marihuana para calmar el estrés. Para cada caso escribe la causa, una consecuencia posible y qué podría hacer en vez de consumir.", "(1) Causa: curiosidad; consecuencia: dependencia a la nicotina; alternativa: preguntar a un adulto o buscar información confiable. (2) Causa: imitar o presión; consecuencia: pérdida de coordinación y daño; alternativa: decir no y proponer otra actividad. (3) Causa: estrés; consecuencia: problemas de atención; alternativa: respirar, practicar deporte o hablar con un adulto.", ["identifica la causa en cada caso", "nombra una consecuencia real", "propone una alternativa segura", "no cuenta una vivencia propia"], ["tabla escrita"], ["decir que no hay riesgo", "culpar a la persona"], "Reconoce la tabla y pregunta qué otra alternativa sana podría elegir cada personaje."),
    reinforce="Escribe tres causas posibles del consumo y una alternativa sana para cada una.",
    extend="Explica por qué la dependencia hace más difícil dejar el consumo aunque la persona quiera.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los mitos, hechos y frases de rechazo están escritos en los ejercicios. Todos los casos son inventados.",
    "Aprenderé a distinguir mitos de hechos sobre las drogas y a decir «no» ante la presión con firmeza y respeto. Sirve para proteger mi decisión sin perder a mis amigos.",
    ["Sé qué son la nicotina y la dependencia.", "Sé reconocer la presión de grupo."],
    [
        "Hay ideas falsas, llamadas mitos, que circulan sobre las drogas. «Solo me hace daño si consumo mucho» es un mito: algunas sustancias generan dependencia o dañan el cerebro en desarrollo aunque se use poco. «El cigarro electrónico no hace daño» también es un mito, porque suele contener nicotina. «Quien consume es una mala persona» es otro mito: hay personas con problemas que necesitan ayuda y no juicio.",
        "Un hecho es algo que se puede comprobar con fuentes confiables. Para distinguir mito y hecho, pregunta: ¿quién lo dice?, ¿lo confirma una fuente de salud?, ¿tiene pruebas? Si no, trátalo con cuidado. También conviene reconocer las emociones que aparecen cuando alguien te ofrece algo: miedo a quedar fuera, curiosidad, vergüenza. Sentirlas es normal; lo importante es decidir con calma.",
        "Para decir «no» con firmeza puedes seguir cuatro pasos: decirlo claro («No, gracias»), dar una razón breve («no me interesa»), proponer algo distinto («¿vamos a jugar?») y, si insisten, irte. No necesitas justificarte ni pelear. Un buen amigo respeta tu decisión. Y si la presión continúa, puedes contárselo a un adulto de confianza.",
    ],
    [("mito", "idea falsa que mucha gente repite"), ("hecho", "dato que se puede comprobar con fuentes confiables"), ("presión", "insistencia para que haga algo que no quiero"), ("firmeza", "decir algo con seguridad sin agredir"), ("alternativa", "otra opción distinta que propongo")],
    [
        W("Distinguir mito y hecho", "Frase: «Probar una sola vez nunca hace daño». ¿Es mito o hecho?", ["No toda sustancia afecta igual, pero algunas generan dependencia o dañan el cerebro.", "No se puede asegurar que no haga daño.", "Es un mito."], "Mito"),
        W("Decir no con firmeza", "Un compañero le ofrece un cigarro a Ema y le dice «no seas aburrida». ¿Qué respuesta firme y respetuosa sirve?", ["Dice «no» claro.", "Da una razón breve.", "Propone algo distinto."], "«No, gracias, no me interesa. ¿Vamos a jugar?»"),
    ],
    [
        M("Pensar que si digo no me dejarán solo.", "Se teme perder amigos.", "Un buen amigo respeta tu decisión; busca grupos que te respeten."),
        M("Creer que el cigarro electrónico es inofensivo.", "Se confunde 'sin humo' con 'sin daño'.", "Suele tener nicotina, que genera dependencia."),
    ],
    R=[
        ex("«Solo daña si consumo mucho». ¿Es mito o hecho?", "Mito", "Algunas sustancias dañan o generan dependencia aunque se usen poco."),
        ex("¿Un hecho se puede comprobar con fuentes confiables? Responde sí o no.", "Sí", "Esa es la diferencia con un mito."),
        ex("«No, gracias» dicho con claridad, ¿es una forma firme de decir no? Responde sí o no.", "Sí", "Dice la decisión sin agredir."),
    ],
    U=[
        ex("¿Por qué «quien consume es una mala persona» es un mito?", "Porque puede ser alguien que necesita ayuda", "Juzgarlo no ayuda; apoyarlo sí."),
        ex("¿Por qué proponer una alternativa («¿vamos a jugar?») ayuda a decir no?", "Porque cambia la situación sin pelear", "Ofrece otra opción que mantiene la relación."),
        ex("Si alguien insiste después de tu «no», ¿qué haces: irte o ceder?", "Irme", "Mantiene tu decisión y evita seguir presionando."),
    ],
    A=[
        ex("Frases: 1) «Probar una sola vez nunca tiene riesgo»; 2) «La nicotina genera dependencia»; 3) «Si lo hace mi hermano, no hay riesgo»; 4) «El alcohol se prohíbe a menores». ¿Cuántas son hechos?", "2", "Los números 2 y 4 son hechos comprobables; 1 y 3 son mitos."),
        ex("Ordena los pasos para decir no: A) irme si insisten; B) decir «No, gracias»; C) dar una razón breve; D) proponer algo distinto. ¿Cuál va último?", "A", "El orden es B, C, D, A: irse es el último recurso."),
        ex("Un amigo te ofrece algo que no quieres y dice «solo esta vez». ¿Cuál es la mejor respuesta? A) «Ya, solo esta vez». B) «No, gracias; no me interesa». C) «Si me das algo a cambio».", "B", "Es firme, breve y respetuosa."),
    ],
    Z=[
        ex("Un mito dice: «Si todos lo hacen, es seguro». ¿Qué pregunta revela el error?", "¿Lo confirma una fuente de salud?", "Que muchos lo hagan no comprueba que sea seguro."),
        ex("¿Por qué un amigo que respeta tu decisión es mejor que uno que te presiona?", "Porque te cuida y no te obliga", "La amistad se basa en el respeto."),
    ],
    D=[
        arith("De 40 frases sobre drogas, 15 eran mitos, 18 eran hechos y el resto eran opiniones. ¿Cuántas eran opiniones?", "40-15-18", "Al total se le restan mitos y hechos."),
        arith("Una estudiante practicó decir «no» 3 veces por día durante 5 días. ¿Cuántas veces lo practicó en total?", "3*5", "Se multiplican las veces por los días."),
    ],
    context=[ex("En una reunión, a Luz le ofrecen un cigarro. Ella dice: «No, gracias, no me interesa. ¿Pedimos jugo?» y sigue conversando. ¿Usó una respuesta firme y respetuosa?", "Sí", "Dijo no, dio una razón breve y propuso una alternativa.")],
    selfcheck=[ex("En Orientación: ¿un mito es una idea falsa que mucha gente repite?", "Sí", "No se puede comprobar."), ex("¿Puedo decir no sin dar muchas explicaciones?", "Sí", "No tengo que justificarme."), ex("¿Un buen amigo respeta mi decisión?", "Sí", "Así se muestra el respeto.")],
    task=T("Lee tres frases de un chat inventado: A) «El cigarro electrónico no hace daño»; B) «Si lo pruebas, serás más popular»; C) «El tabaco genera dependencia». Para cada una escribe si es mito o hecho y por qué. Después escribe una respuesta firme y respetuosa para cuando alguien te ofrezca un cigarro, con una razón breve y una alternativa.", "A: mito, suele tener nicotina. B: mito, la popularidad no depende de eso. C: hecho, la nicotina genera dependencia. Respuesta: «No, gracias, no me interesa. ¿Jugamos a otra cosa?»", ["clasifica las tres frases", "explica cada clasificación", "escribe una respuesta firme con razón y alternativa", "no cuenta una vivencia propia"], ["lista escrita o dramatizada"], ["aceptar un mito sin revisar", "responder con insultos"], "Reconoce la respuesta y pregunta qué haría si la persona insiste."),
    reinforce="Escribe tres mitos sobre las drogas y el hecho que los corrige.",
    extend="Explica por qué importa más tu decisión que la opinión del grupo.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. Las tablas de factores y los casos están escritos en los ejercicios.",
    "Aprenderé a identificar factores que previenen el consumo (factores protectores) y los que lo facilitan (de riesgo). Sirve para elegir entornos y hábitos que me cuidan.",
    ["Sé qué causas pueden llevar a consumir.", "Sé decir no con firmeza."],
    [
        "Un factor de riesgo es algo que aumenta la probabilidad de consumir drogas, como tener amistades que presionan, vivir en un lugar donde es fácil conseguirlas, sentirse muy solo o no tener actividades que gusten. Un factor protector es algo que disminuye esa probabilidad. Ayudan la buena comunicación con la familia, una autoestima positiva, amistades sanas, actividades como deporte, arte o música, conocer las consecuencias y tener metas para el futuro.",
        "Tener un factor de riesgo no significa que alguien vaya a consumir, y tener factores protectores no da una garantía total, pero ayudan mucho. Lo bueno es que muchos factores protectores se pueden fortalecer: se puede conversar más con la familia, sumarse a un taller, elegir compañías sanas y aprender a manejar emociones. Cada decisión tiene consecuencias y las opciones que fortalecen los factores protectores cuidan tu futuro.",
        "También hay factores del entorno, como las normas del colegio, la información disponible y los adultos que acompañan. Si notas que un amigo está en riesgo, puedes ofrecerle compañía y animarlo a hablar con un adulto de confianza. No tienes que resolverlo solo, ni juzgarlo.",
    ],
    [("factor de riesgo", "algo que aumenta la probabilidad de consumir drogas"), ("factor protector", "algo que disminuye esa probabilidad"), ("autoestima", "valoración que tengo de mí mismo"), ("entorno", "lugares y personas que me rodean"), ("proyecto de vida", "metas que quiero lograr en el futuro")],
    [
        W("Clasificar factores", "«Tener un taller de teatro al que le gusta ir» y «tener amistades que presionan a consumir». ¿Cuál es protector y cuál de riesgo?", ["El taller es una actividad sana que le gusta.", "Las amistades que presionan facilitan el consumo.", "Uno protege y el otro es de riesgo."], "El taller es protector; las amistades que presionan son de riesgo"),
        W("Fortalecer un factor protector", "Ian siente que habla poco con su familia. ¿Qué acción fortalece un factor protector: conversar 15 minutos al día con una persona adulta de su casa o aislarse más?", ["La comunicación con la familia protege.", "Aislarse aumenta el riesgo.", "Conversar fortalece un factor protector."], "Conversar 15 minutos al día con una persona adulta de su casa"),
    ],
    [
        M("Pensar que tener un factor de riesgo significa que seguro voy a consumir.", "Se confunde probabilidad con certeza.", "Los riesgos se pueden reducir fortaleciendo los factores protectores."),
        M("Creer que prevenir es solo decir 'no' en el momento.", "Se olvida que la prevención empieza antes.", "Fortalece actividades, vínculos y metas con anticipación."),
    ],
    R=[
        ex("«Hacer deporte con un equipo». ¿Es un factor protector o de riesgo?", "Un factor protector", "Es una actividad sana que disminuye la probabilidad de consumir."),
        ex("«Tener amistades que presionan a consumir». ¿Es un factor protector o de riesgo?", "Un factor de riesgo", "Aumenta la probabilidad de consumir."),
        ex("¿Una buena comunicación con la familia es un factor protector? Responde sí o no.", "Sí", "Ayuda a pedir apoyo a tiempo."),
    ],
    U=[
        ex("¿Por qué las actividades que a uno le gustan protegen del consumo?", "Porque dan sentido y buenas formas de pasar el tiempo", "Ocupan el tiempo de manera sana."),
        ex("¿Tener un factor de riesgo asegura que una persona consumirá? Responde sí o no.", "No", "Solo aumenta la probabilidad."),
        ex("¿Cuál es un factor protector: tener metas para el futuro o sentirse siempre solo?", "Tener metas para el futuro", "Las metas motivan a cuidarse."),
    ],
    A=[
        ex("Lista: 1) taller de música; 2) amistades que presionan; 3) conversar con la familia; 4) sentirse solo y sin actividades; 5) tener metas para el futuro. ¿Cuántos son factores protectores?", "3", "Los números 1, 3 y 5 protegen; 2 y 4 son riesgos."),
        ex("Sofi quiere fortalecer factores protectores. ¿Cuál de estas acciones lo hace? A) Quedarse sola en su pieza todos los días. B) Inscribirse en un taller de pintura. C) Dejar de hablar con sus amigas.", "B", "Aporta una actividad sana y vínculos con otros."),
        ex("Un amigo está muy solo últimamente. ¿Qué acción lo ayuda más? A) Burlarse de él. B) Invitarlo a una actividad y animarlo a hablar con un adulto de confianza. C) Ignorarlo.", "B", "Ofrece compañía y apoyo adulto."),
    ],
    Z=[
        ex("¿Por qué es útil fortalecer factores protectores desde antes de que haya un problema?", "Porque previene en vez de reaccionar tarde", "Prevenir es más eficaz que corregir después."),
        ex("Dos estudiantes tienen amigos que presionan. Una tiene taller, buena comunicación con la familia y metas; el otro está solo y sin actividades. ¿Quién tiene más protección?", "La que tiene taller, comunicación y metas", "Tiene más factores protectores."),
    ],
    D=[
        arith("Una estudiante anotó 8 factores de su vida: 5 son protectores y el resto de riesgo. ¿Cuántos son de riesgo?", "8-5", "Se restan los protectores al total."),
        arith("Una estudiante entrena fútbol 3 veces por semana durante 6 semanas. ¿Cuántos entrenamientos hace en total?", "3*6", "Se multiplican las veces por las semanas."),
    ],
    context=[ex("Valentina notó que su amiga Maite se aleja del grupo y abandonó el taller de baile. Le dice: «Te extraño en el taller; ¿quieres ir juntas esta semana? Si algo te pasa, podemos hablarlo con la orientadora». ¿Ayudó a fortalecer un factor protector?", "Sí", "Ofreció compañía, una actividad sana y apoyo adulto.")],
    selfcheck=[ex("En Orientación: ¿los factores protectores disminuyen la probabilidad de consumo?", "Sí", "Ese es su efecto."), ex("¿Los factores de riesgo aseguran el consumo?", "No", "Solo lo hacen más probable."), ex("¿Se pueden fortalecer los factores protectores?", "Sí", "Con actividades, comunicación y metas.")],
    task=T("Haz una tabla de dos columnas para un personaje inventado llamado Tomás: factores de riesgo (amigos que presionan, poca comunicación en casa) y factores protectores (le gusta el fútbol, quiere ser kinesiólogo). Agrega dos acciones concretas para fortalecer sus factores protectores esta semana.", "Riesgo: amigos que presionan, poca comunicación en casa. Protector: fútbol y meta de ser kinesiólogo. Acciones: inscribirse en el entrenamiento del colegio los martes y jueves; conversar 10 minutos cada noche con una persona adulta de su casa.", ["ordena los factores en las dos columnas", "propone dos acciones concretas y posibles", "no cuenta una vivencia propia"], ["tabla escrita"], ["poner acciones vagas", "confundir riesgo con protección"], "Reconoce la tabla y pregunta qué factor protector le parece más fácil de fortalecer."),
    reinforce="Escribe cinco factores protectores que pueden estar al alcance de un estudiante de tu edad.",
    extend="Explica por qué el apoyo de un adulto de confianza es un factor protector.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Los horarios y las listas de hábitos están escritos en los ejercicios.",
    "Aprenderé a proponer estrategias para enfrentar el consumo: hábitos de vida saludable, manejo del estrés y pedir ayuda. Sirve para cuidar mi cuerpo y mi ánimo.",
    ["Sé qué factores protegen del consumo.", "Sé respirar para calmarme y pedir ayuda."],
    [
        "Una estrategia es un plan para enfrentar un problema. Para prevenir el consumo de drogas, una estrategia es mantener hábitos de vida saludable: dormir entre 9 y 11 horas, comer variado, moverse todos los días y tener momentos de descanso y recreación. Un cuerpo descansado y activo maneja mejor las emociones y las tareas.",
        "Otra estrategia es aprender a manejar el estrés, que es la tensión que sentimos cuando creemos que no podemos con lo que nos piden. Algunas formas son organizar el tiempo para no dejar todo para el final, hacer pausas, respirar lento, conversar con alguien de confianza, practicar un deporte o escuchar música. No todo funciona igual para todos, por eso conviene probar y elegir lo que ayuda sin dañarte.",
        "Si sientes que no puedes con el estrés o que un amigo o familiar necesita ayuda por consumo, la estrategia más importante es pedir apoyo. Puedes hablar con un adulto de confianza, con el orientador del colegio o llamar al Fono Drogas y Alcohol 1412. Pedir ayuda a tiempo es una decisión valiente. Un plan semanal escrito te ayuda a cumplirlo.",
    ],
    [("estrategia", "plan para enfrentar un problema"), ("hábito saludable", "costumbre diaria que cuida el cuerpo y la mente"), ("estrés", "tensión que siento cuando creo que no puedo con lo que me piden"), ("descanso", "tiempo para dormir o relajarse"), ("recreación", "actividad que disfruto para pasarlo bien")],
    [
        W("Elegir una estrategia para el estrés", "Camila está estresada porque tiene tres trabajos para el viernes y no los ha empezado. ¿Qué estrategia ayuda: organizar un horario con 40 minutos diarios o dejarlo todo para el jueves?", ["Dividir el trabajo baja la tensión.", "Dejarlo para el final aumenta el estrés.", "El horario es la estrategia útil."], "Organizar un horario con 40 minutos diarios"),
        W("Pedir ayuda", "Un compañero inventado le cuenta a Ian que su hermano mayor consume y está preocupado. ¿Qué estrategia le sugiere Ian?", ["No es algo para resolver solo.", "Un adulto de confianza puede orientar.", "También existe una línea de ayuda."], "Hablar con un adulto de confianza o llamar a una línea de ayuda"),
    ],
    [
        M("Creer que el estrés se quita consumiendo algo.", "Se busca alivio rápido sin ver las consecuencias.", "Usa estrategias seguras: pausas, respirar, deporte, conversar."),
        M("Pensar que pedir ayuda por un familiar es traicionarlo.", "Se confunde ayudar con acusar.", "Pedir ayuda busca cuidar a la persona."),
    ],
    R=[
        ex("¿Dormir entre 9 y 11 horas es un hábito saludable para un niño de 11 años? Responde sí o no.", "Sí", "El descanso suficiente cuida el cuerpo y el ánimo."),
        ex("¿Respirar lento es una estrategia para manejar el estrés? Responde sí o no.", "Sí", "Calma el cuerpo."),
        ex("Si un familiar tiene problemas de consumo, ¿conviene hablar con un adulto de confianza? Responde sí o no.", "Sí", "Un adulto puede orientar y buscar apoyo."),
    ],
    U=[
        ex("¿Por qué organizar el tiempo ayuda a manejar el estrés?", "Porque evita dejar todo para el último momento", "Distribuir el trabajo baja la tensión."),
        ex("¿Por qué consumir una sustancia para calmar el estrés es mala idea?", "Porque trae consecuencias y no resuelve el problema", "Alivia un momento y puede generar dependencia."),
        ex("¿Una estrategia funciona igual para todas las personas? Responde sí o no.", "No", "Cada persona debe probar cuál le ayuda."),
    ],
    A=[
        ex("Lista: 1) dormir 10 horas; 2) comer solo golosinas; 3) caminar 30 minutos al día; 4) pasar todo el día frente a una pantalla; 5) hacer pausas al estudiar. ¿Cuántos son hábitos saludables?", "3", "Los números 1, 3 y 5 cuidan el cuerpo y la mente."),
        arith("Un plan semanal incluye 20 minutos de deporte el lunes, 20 el miércoles y 20 el viernes. ¿Cuántos minutos de deporte son en la semana?", "20*3", "Son tres días de 20 minutos."),
        ex("Camila tiene mucha tarea y siente tensión. ¿Qué estrategia es más segura? A) Estudiar sin parar toda la noche. B) Hacer pausas de 5 minutos cada 25 minutos y respirar lento. C) Quedarse despierto toda la noche usando el celular.", "B", "Las pausas y la respiración bajan el estrés sin riesgo."),
    ],
    Z=[
        ex("¿Por qué un plan semanal escrito ayuda a mantener hábitos saludables?", "Porque se puede revisar y cumplir", "Escrito, el plan se vuelve claro y medible."),
        ex("Un estudiante dice que no necesita ayuda aunque lleva semanas sin dormir bien y muy estresado. ¿Qué conviene recomendarle?", "Hablar con un adulto de confianza", "El estrés prolongado merece apoyo."),
    ],
    D=[
        arith("Una estudiante duerme 9 horas por noche durante 5 noches de colegio. ¿Cuántas horas duerme en esas noches?", "9*5", "Se multiplican las horas por las noches."),
        arith("Un estudiante camina 25 minutos al día durante 6 días. ¿Cuántos minutos camina en total?", "25*6", "Se multiplican los minutos por los días."),
    ],
    context=[ex("Antes de una prueba difícil, Ema siente mucho estrés. Hace una pausa de 5 minutos, respira lento 10 veces, toma agua y luego revisa sus apuntes. ¿Usó una estrategia saludable?", "Sí", "Calmó su cuerpo con acciones seguras antes de estudiar.")],
    selfcheck=[ex("En Orientación: ¿el deporte puede ayudar a manejar el estrés?", "Sí", "Mueve el cuerpo y ayuda a liberar tensión."), ex("¿Consumir drogas es una buena estrategia para el estrés?", "No", "Trae daños y no resuelve."), ex("¿Pedir ayuda es parte de las estrategias?", "Sí", "Permite recibir apoyo a tiempo.")],
    task=T("Arma un plan de la semana para Rocío, una estudiante inventada que tiene mucho estrés. Incluye: horas de sueño por noche, dos momentos de actividad física, una pausa diaria para respirar o relajarse, una forma de organizar sus tareas y a quién le pedirá ayuda si el estrés es muy fuerte.", "Dormir 9 horas cada noche; actividad física martes y jueves 30 minutos; pausa diaria de 5 minutos para respirar; organizar tareas con una lista y horario; si el estrés es muy fuerte, hablar con la orientadora o con una persona adulta de su casa.", ["incluye sueño, actividad, pausa, organización y ayuda", "es posible de cumplir", "no cuenta una vivencia propia"], ["plan escrito"], ["plan imposible", "no incluir ayuda"], "Reconoce el plan y pregunta qué ajuste haría si no alcanza el tiempo."),
    reinforce="Haz una lista de cinco estrategias seguras para manejar el estrés y marca dos que podrías probar.",
    extend="Explica por qué cuidar el sueño y la actividad física puede ser una forma de prevención.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. Los casos de Dani y de Luz, personajes inventados, y las frases de buen trato están escritos en los ejercicios.",
    "Aprenderé a actuar con empatía y a usar un buen trato (saludar, despedirse, pedir por favor). Sirve para que todos se sientan respetados y para convivir mejor.",
    ["Sé nombrar emociones.", "Sé armar un mensaje «yo»."],
    [
        "La empatía es ponerse en el lugar del otro: imaginar y entender lo que siente y por qué. No significa estar de acuerdo con todo, sino reconocer su emoción. Para actuar con empatía puedes observar, escuchar sin interrumpir y preguntar: «¿cómo te sientes?, ¿qué necesitas?». Con eso entiendes mejor y respondes con cuidado.",
        "El buen trato son las conductas que muestran respeto en el día a día: saludar al llegar, despedirse, pedir las cosas por favor, dar las gracias, pedir disculpas cuando uno se equivoca y hablar sin gritar ni burlarse. Un buen trato crea un ambiente en que se aprende y se convive mejor. No cuesta nada y vale mucho.",
        "La empatía y el buen trato van juntos. Si Dani ve que Luz está triste porque no tiene con quién jugar, puede acercarse, saludar y preguntar si quiere unirse. Eso es solidaridad: ayudar a otros porque entiendo lo que sienten. También es empatía reconocer cuando alguien necesita estar solo y respetarlo.",
    ],
    [("empatía", "ponerse en el lugar del otro y entender lo que siente"), ("buen trato", "conductas que muestran respeto, como saludar o pedir por favor"), ("solidaridad", "ayudar a otros porque entiendo que lo necesitan"), ("escuchar", "prestar atención sin interrumpir"), ("disculpa", "reconocer que me equivoqué y repararlo")],
    [
        W("Reconocer una respuesta empática", "Luz dice: «Hoy no tengo con quién jugar». ¿Qué respuesta es empática: «Yo te acompaño, ¿jugamos?» o «No es para tanto»?", ["La primera reconoce lo que siente.", "La segunda minimiza su sentimiento.", "La empatía reconoce y acompaña."], "«Yo te acompaño, ¿jugamos?»"),
        W("Identificar buen trato", "Un estudiante entra a la sala y dice «Buenos días», pide «por favor» un lápiz y dice «gracias». ¿Cuántas conductas de buen trato usó?", ["Saludó con «Buenos días».", "Pidió con «por favor».", "Agradeció con «gracias»."], "Tres"),
    ],
    [
        M("Decir 'no es para tanto' para animar a alguien.", "Se minimiza lo que siente sin darse cuenta.", "Reconoce la emoción primero: «veo que estás triste»."),
        M("Creer que el buen trato es solo para los adultos.", "Se piensa que entre compañeros no hace falta.", "El buen trato se usa con todos, en todo momento."),
    ],
    R=[
        ex("Ponerse en el lugar del otro para entender lo que siente, ¿es empatía o enojo?", "Empatía", "Es entender lo que el otro vive."),
        ex("¿Saludar y despedirse son parte del buen trato? Responde sí o no.", "Sí", "Son conductas de respeto diarias."),
        ex("¿Pedir por favor y dar las gracias son formas de buen trato? Responde sí o no.", "Sí", "Demuestran respeto hacia otros."),
    ],
    U=[
        ex("¿Por qué decir «no es para tanto» a alguien triste no es empático?", "Porque minimiza lo que siente", "No reconoce su emoción."),
        ex("¿Qué pregunta ayuda a actuar con empatía: «¿cómo te sientes?» o «¿por qué lloras tanto?»", "«¿Cómo te sientes?»", "Pregunta con cuidado y sin juzgar."),
        ex("¿Respetar que alguien necesita estar solo puede ser empatía? Responde sí o no.", "Sí", "Reconoce lo que la otra persona necesita."),
    ],
    A=[
        ex("Conductas: 1) saludar; 2) gritar una orden; 3) pedir disculpas tras empujar sin querer; 4) burlarse de una respuesta; 5) decir gracias. ¿Cuántas son buen trato?", "3", "Los números 1, 3 y 5 son buen trato."),
        ex("Dani ve que Tomás se quedó solo en el recreo. ¿Qué acción es solidaria? A) Pasar de largo. B) Acercarse y preguntar si quiere jugar. C) Mirarlo y reírse.", "B", "Se acerca para ayudar."),
        ex("Un compañero inventado olvida su colación. ¿Qué respuesta es empática? A) «Me preocupa que tengas hambre; ¿compartimos?» B) «Bueno, olvídalo y no molestes».", "A", "Reconoce su necesidad y ofrece ayuda."),
    ],
    Z=[
        ex("¿Por qué el buen trato ayuda también a aprender mejor?", "Porque crea un ambiente tranquilo y respetuoso", "Con respeto, todos se concentran y participan."),
        ex("Ema se equivocó y empujó sin querer a una compañera. ¿Qué es lo más respetuoso?", "Pedir disculpas", "Reconoce el error y repara el daño."),
    ],
    D=[
        arith("Un curso de 30 estudiantes se propuso que cada uno salude a sus compañeros al llegar, una vez por día, durante 5 días. ¿Cuántos saludos se esperan en total?", "30*5", "Se multiplican los estudiantes por los días."),
        arith("De 28 estudiantes, 19 dijeron «gracias» al menos una vez en un recreo. ¿Cuántos no lo dijeron?", "28-19", "Se restan los que lo dijeron al total."),
    ],
    context=[ex("Una compañera nueva se sienta sola en la sala. Mati le sonríe, la saluda, se presenta y le pregunta si quiere sentarse con su grupo. ¿Actuó con empatía y buen trato?", "Sí", "La saludó, reconoció su situación y la invitó.")],
    selfcheck=[ex("En Orientación: ¿empatía es entender lo que siente el otro?", "Sí", "Es ponerse en su lugar."), ex("¿Pedir por favor es buen trato?", "Sí", "Muestra respeto a los demás."), ex("¿Reírse de alguien que se equivoca es solidario?", "No", "Hiere al otro.")],
    task=T("Lee el caso de Teo, un estudiante inventado: perdió el partido de su equipo y está callado en un rincón. Escribe qué sentirá probablemente, una frase empática que podría decirle un compañero y dos conductas de buen trato que podrían ayudar a que se sienta mejor.", "Teo probablemente siente tristeza y frustración. Frase: «Veo que te sientes mal; ¿quieres que me quede contigo?» Buen trato: saludarlo con amabilidad y no burlarse del resultado.", ["nombra una emoción posible", "escribe una frase empática", "incluye dos conductas de buen trato", "no cuenta una vivencia propia"], ["texto escrito o dramatizado"], ["minimizar su emoción", "burlarse"], "Reconoce la frase y pregunta qué haría si Teo prefiere estar solo."),
    reinforce="Escribe tres frases empáticas para una persona que está triste, enojada o nerviosa.",
    extend="Explica la diferencia entre empatía y estar de acuerdo con todo lo que hace el otro.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. Las situaciones están escritas en los ejercicios. No uses nombres reales de compañeros.",
    "Aprenderé a distinguir una broma, una ofensa, una discriminación y una agresión, y a rechazar toda forma de violencia y discriminación. Sirve para convivir con respeto y proteger a quien lo necesita.",
    ["Sé actuar con empatía.", "Sé que todas las personas tienen dignidad."],
    [
        "La discriminación es tratar a una persona peor o excluirla por una característica suya, como su etnia, su género, su religión, su nacionalidad, su apariencia o su manera de hablar. Es injusta porque nadie elige esas características y todas las personas tienen los mismos derechos. La violencia es cualquier acción que daña a otra persona: física (golpear, empujar), verbal (insultar, amenazar), psicológica (humillar, excluir) o digital (burlarse en un chat).",
        "A veces cuesta distinguir. Una broma es algo que hace reír a todos, incluida la persona de la que se habla. Si alguien se siente herido, deja de ser broma y pasa a ser ofensa. Si la ofensa se basa en una característica de la persona, es discriminación; si además se repite, es hostigamiento. Una agresión es cuando hay daño físico o amenaza. Para decidir, pregúntate: ¿alguien se siente herido?, ¿se burla de una característica de la persona?, ¿se repite?",
        "Rechazar la violencia y la discriminación significa no participar, no reírse, avisar a un adulto y, solo si te sientes seguro, decir con calma «eso no está bien». Lo más seguro es acompañar a quien lo sufre y pedir ayuda adulta. También significa defender el respeto de todos: nadie debe quedar excluido de un juego, de un grupo o de la clase por ser distinto.",
    ],
    [("discriminación", "tratar peor o excluir a alguien por una característica suya"), ("violencia", "acción que daña a otra persona, de forma física, verbal, psicológica o digital"), ("ofensa", "palabra o gesto que hiere a otra persona"), ("etnia", "grupo de personas con una cultura y orígenes compartidos"), ("nacionalidad", "país al que pertenece una persona")],
    [
        W("Clasificar una situación", "Un grupo dice que no dejará jugar a un compañero porque nació en otro país. ¿Es discriminación?", ["Lo excluyen por una característica suya: su nacionalidad.", "Nadie elige dónde nace.", "Es discriminación."], "Sí, es discriminación"),
        W("Distinguir broma y ofensa", "Un chiste hace reír a todos, pero el compañero de quien hablan baja la cabeza y se aleja. ¿Es broma o ofensa?", ["La persona aludida se siente herida.", "Ya no hace reír a todos.", "Es una ofensa."], "Ofensa"),
    ],
    [
        M("Creer que si es 'solo una broma' nadie puede enojarse.", "Se piensa que la intención basta.", "Si alguien se siente herido, para y pide disculpas."),
        M("Pensar que no hacer nada cuando se discrimina no es mi problema.", "Se confunde no participar con no ayudar.", "Di con calma que no está bien y avisa a un adulto."),
    ],
    R=[
        ex("Tratar peor a alguien por su religión, ¿es discriminación o amistad?", "Discriminación", "Lo trata peor por una característica suya."),
        ex("Una broma que hace reír a todos, incluida la persona de la que se habla, ¿puede ser una broma? Responde sí o no.", "Sí", "Nadie se siente herido."),
        ex("Humillar a alguien en un chat del curso, ¿es violencia digital? Responde sí o no.", "Sí", "Daña a la persona por medios digitales."),
    ],
    U=[
        ex("¿Por qué excluir a alguien por su manera de hablar es injusto?", "Porque no es algo que se elija y todos tienen los mismos derechos", "Trata peor a una persona sin una razón válida."),
        ex("¿Qué pregunta ayuda a distinguir broma y ofensa: «¿alguien se siente herido?» o «¿quién lo dijo?»", "«¿Alguien se siente herido?»", "El efecto en el otro define si es broma u ofensa."),
        ex("Si presencias discriminación, ¿puedes decir con calma «eso no está bien»? Responde sí o no.", "Sí", "Es una forma de rechazarla sin violencia."),
    ],
    A=[
        ex("Situaciones: 1) insultar por su apariencia; 2) invitar a todos a un juego; 3) no dejar sentar a alguien por su etnia; 4) empujar para quitar un puesto; 5) saludar al llegar. ¿Cuántas son violencia o discriminación?", "3", "Los números 1, 3 y 4 dañan o excluyen; 2 y 5 son respetuosos."),
        ex("Una compañera de otro país habla con un acento distinto y algunos imitan cómo habla. ¿Qué haces? A) Reírte. B) Decir con calma «no está bien burlarse» y acercarte a ella. C) Imitarla.", "B", "Rechaza la burla y acompaña."),
        ex("Un grupo envía un mensaje burlándose de un compañero por su religión. ¿Qué haces? A) Reenviarlo. B) No reenviar, guardar prueba y avisar a un adulto. C) Responder con otro insulto.", "B", "No participa y busca ayuda adulta."),
    ],
    Z=[
        ex("¿Por qué una broma repetida sobre la nacionalidad de alguien deja de ser broma?", "Porque lo hiere y lo excluye por una característica suya", "Se convierte en discriminación."),
        ex("¿Por qué no reírse también es una forma de rechazar la discriminación?", "Porque deja de apoyar la burla", "La risa del grupo refuerza el daño."),
    ],
    D=[
        arith("De 36 estudiantes, 27 dijeron que han visto burlas en el curso. ¿Cuántos no las han visto?", "36-27", "Se restan los que las han visto al total."),
        arith("Un curso registró 4 situaciones de exclusión la primera semana y 7 la segunda. ¿Cuántas fueron en total?", "4+7", "Se suman las situaciones de cada semana."),
    ],
    context=[ex("En el recreo, algunos comienzan a llamar con un apodo despectivo a un compañero por su origen. Rocío dice: «Eso no está bien; todos merecemos respeto» y avisa a la profesora. ¿Actuó como se espera?", "Sí", "Rechazó la discriminación con calma y pidió ayuda adulta.")],
    selfcheck=[ex("En Orientación: ¿discriminar es tratar peor por una característica de la persona?", "Sí", "Esa es su definición."), ex("¿Una broma que hiere puede seguir siendo broma?", "No", "Pasa a ser ofensa."), ex("¿Avisar a un adulto ante violencia es cuidar a otros?", "Sí", "Ayuda a detener el daño.")],
    task=T("Lee las tres situaciones inventadas: (1) un grupo no deja jugar a un compañero por el color de su piel; (2) dos amigos bromean entre ellos y se ríen los dos; (3) alguien empuja a un compañero para quitarle el puesto. Para cada una escribe: es discriminación, violencia, broma o ninguna, y qué harías para rechazarla o detenerla.", "(1) Discriminación: digo con calma que no está bien y aviso a un adulto. (2) Broma: nadie se siente herido; no hago nada. (3) Violencia: aviso a un adulto y acompaño al compañero.", ["clasifica las tres situaciones", "propone una acción para cada una cuando corresponde", "no cuenta una vivencia propia"], ["tabla escrita"], ["no distinguir broma de ofensa", "no actuar ante violencia"], "Reconoce la clasificación y pregunta cómo cambiaría su respuesta si fuera por chat."),
    reinforce="Escribe cuatro frases que podrías decir para rechazar una burla sin agredir.",
    extend="Explica por qué la discriminación daña a toda la comunidad y no solo a quien la sufre.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. Los casos de debate y las frases están escritos en los ejercicios.",
    "Aprenderé a respetar el derecho de todos a expresar sus opiniones y a ser diferentes. Sirve para conversar sin pelear cuando pensamos distinto.",
    ["Sé actuar con empatía y buen trato.", "Sé rechazar la discriminación."],
    [
        "Todas las personas tienen derecho a expresar su opinión y a ser diferentes. Pensar distinto no es un problema, es parte de vivir en comunidad. Una opinión es lo que una persona piensa o siente sobre un tema y puede cambiar. Un hecho se puede comprobar. Para conversar con respeto, escucha primero, pide aclaraciones y habla de ideas, no de personas. Frases como «yo pienso que…» o «no estoy de acuerdo porque…» ayudan a mantener el respeto.",
        "Respetar una opinión no significa estar de acuerdo, pero sí escucharla y no burlarse. Tampoco todo vale: el derecho a opinar no incluye insultar, discriminar o dañar. Si alguien expresa algo que hiere a otros, se puede decir con calma «esa opinión discrimina y no es aceptable». Y quien opina también debe poder escuchar la crítica.",
        "Ser diferente también incluye gustos, formas de vestir, de hablar, de jugar o de celebrar. Mientras no dañe a otros, cada persona tiene derecho a ser quien es. Una buena conversación termina con más comprensión, aunque no haya un acuerdo. Los turnos para hablar y el volumen moderado ayudan.",
    ],
    [("opinión", "lo que una persona piensa o siente sobre un tema"), ("diferencia", "algo que hace distinta a una persona"), ("respeto", "tratar con cuidado a quien piensa distinto"), ("aclarar", "pedir que expliquen mejor una idea"), ("debate", "conversación en que se defienden ideas distintas")],
    [
        W("Responder a otra opinión", "Ana opina que el curso debería ir a un museo y Beto prefiere un parque. ¿Qué frase respeta la opinión de Ana: «No estoy de acuerdo porque queda lejos» o «Qué idea tonta»?", ["La primera dice la diferencia con una razón.", "La segunda insulta la idea.", "Se debe hablar de ideas, no de personas."], "«No estoy de acuerdo porque queda lejos»"),
        W("Distinguir opinión y hecho", "«Mi curso tiene 30 estudiantes» y «la clase de arte es la mejor». ¿Cuál es hecho y cuál opinión?", ["El número de estudiantes se puede contar.", "Que sea la mejor depende del gusto.", "El primero es hecho y el segundo opinión."], "Hecho: tiene 30 estudiantes. Opinión: la clase de arte es la mejor"),
    ],
    [
        M("Creer que respetar una opinión es estar de acuerdo.", "Se confunde escuchar con aceptar.", "Escucha y responde con respeto, aunque pienses distinto."),
        M("Pensar que mi opinión vale más porque soy mayor o más fuerte.", "Se confunde poder con razón.", "Las razones, no la fuerza, apoyan una opinión."),
    ],
    R=[
        ex("«Mi curso tiene 30 estudiantes». ¿Es un hecho o una opinión?", "Un hecho", "Se puede contar y comprobar."),
        ex("«Esa película es la más entretenida». ¿Es un hecho o una opinión?", "Una opinión", "Depende del gusto de cada persona."),
        ex("¿Todas las personas tienen derecho a expresar su opinión? Responde sí o no.", "Sí", "Es parte de convivir con respeto."),
    ],
    U=[
        ex("¿Por qué respetar una opinión no significa estar de acuerdo?", "Porque se puede escuchar sin aceptarla", "Respetar es escuchar y no burlarse."),
        ex("¿Por qué insultar no es parte del derecho a opinar?", "Porque daña a otra persona", "El derecho a opinar no incluye herir."),
        ex("¿Qué frase mantiene el respeto: «yo pienso que…» o «tú siempre te equivocas»?", "«Yo pienso que…»", "Habla de mi idea sin atacar."),
    ],
    A=[
        ex("Frases: 1) «Una semana tiene 7 días»; 2) «El fútbol es el mejor deporte»; 3) «Hay 4 estaciones en el año»; 4) «Esa canción es lindísima». ¿Cuántas son hechos?", "2", "Las frases 1 y 3 se pueden comprobar; 2 y 4 son opiniones."),
        ex("Dos estudiantes piensan distinto sobre el lugar de un paseo. ¿Qué conviene? A) Escuchar los argumentos y buscar un acuerdo. B) Insistir con gritos. C) Ignorar al otro.", "A", "Escuchar y buscar acuerdo respeta a todos."),
        ex("Un compañero dice algo que discrimina por nacionalidad y dice «es mi opinión». ¿Qué respuesta es adecuada? A) Decir con calma que eso discrimina y contárselo a la profesora. B) «Tienes derecho a lo que quieras». C) Reírse.", "A", "El derecho a opinar no incluye discriminar."),
    ],
    Z=[
        ex("Marta y Julia opinan distinto, pero después de escucharse, ambas entienden mejor el tema. ¿Fue una buena conversación aunque no hayan llegado a acuerdo?", "Sí", "Aumentó la comprensión."),
        ex("¿Por qué conviene hablar de ideas y no de personas?", "Porque así no se hiere a nadie", "Atacar a la persona provoca defensa."),
    ],
    D=[
        arith("En un debate de 5 estudiantes, cada uno habló 3 minutos. ¿Cuántos minutos duró en total?", "5*3", "Se multiplican los estudiantes por los minutos."),
        arith("Una votación de opinión tuvo 28 participantes: 15 a favor y 9 en contra, el resto no opinó. ¿Cuántos no opinaron?", "28-15-9", "Al total se le restan los dos grupos."),
    ],
    context=[ex("En una reunión de curso, Sofi propone hacer una feria de libros y Bruno prefiere una feria de juegos. Bruno dice: «Yo prefiero juegos porque participa más gente; ¿podemos votar?». ¿Respetó la opinión de Sofi?", "Sí", "Dio su razón sin atacar y propuso una forma justa de decidir.")],
    selfcheck=[ex("En Orientación: ¿todas las personas pueden opinar distinto?", "Sí", "Es parte de convivir."), ex("¿Se puede opinar insultando?", "No", "Daña a otros."), ex("¿Una opinión puede cambiar?", "Sí", "Depende de nuevas razones.")],
    task=T("Lee este caso de debate inventado: el curso debe elegir si su paseo de fin de año será a un museo o a un parque. Escribe dos razones a favor de una opción y una pregunta para entender la razón de quien piensa distinto. Luego escribe una frase para responder con respeto si alguien dice una idea que no te gusta.", "Razones a favor del parque: se puede jugar al aire libre y es más barato. Pregunta: «¿Por qué prefieres el museo?» Respuesta respetuosa: «No estoy de acuerdo porque hay que pagar entrada, pero entiendo tu punto».", ["escribe dos razones", "formula una pregunta para entender al otro", "escribe una frase respetuosa", "no cuenta una vivencia propia"], ["texto escrito o dramatizado"], ["insultar la idea", "no dar razones"], "Reconoce las razones y pregunta cómo llegarían a un acuerdo."),
    reinforce="Escribe cuatro frases para expresar desacuerdo con respeto.",
    extend="Explica por qué escuchar a quien piensa distinto puede hacernos cambiar de idea sin perder dignidad.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. Las situaciones de ayuda están escritas en los ejercicios. Todos los casos son inventados.",
    "Aprenderé a prestar ayuda, sobre todo a quien la necesita, y a actuar como testigo activo ante el maltrato. Sirve para apoyar a otros sin ponerme en peligro.",
    ["Sé actuar con empatía y rechazar la discriminación.", "Sé pedir ayuda a un adulto."],
    [
        "Ayudar es una forma de solidaridad. Hay muchos modos: compartir materiales, explicar algo, acompañar a alguien que está solo, o avisar a un adulto cuando hay peligro. La ayuda es mejor cuando se ofrece con respeto y se pregunta antes: «¿quieres que te ayude?». Así la persona decide si la acepta.",
        "Cuando alguien sufre maltrato, hay testigos: quienes lo ven. Un testigo puede ser pasivo (mira y no hace nada), cómplice (se ríe o participa) o activo (ayuda de forma segura). Un testigo activo no necesita pelear. Puede acompañar a la persona, no compartir la burla, avisar a un adulto y, solo si se siente seguro, decir con calma «basta». Si la situación es peligrosa, la prioridad es la seguridad: no te pongas en riesgo y busca ayuda de inmediato.",
        "Ayudar también significa reconocer cuándo necesito ayuda yo. Pedirla no te hace menos. Ayudar y ser ayudado construyen una comunidad donde todos se sienten acogidos.",
    ],
    [("solidaridad", "ayudar a otros porque entiendo que lo necesitan"), ("testigo", "persona que ve algo que le ocurre a otra"), ("testigo activo", "testigo que ayuda de forma segura"), ("complicidad", "participar o reírse de lo que daña a otro"), ("seguridad", "estar a salvo de un daño")],
    [
        W("Clasificar un testigo", "Ema ve que se burlan de una compañera, se ríe y graba el momento. ¿Qué tipo de testigo es?", ["Participa de la burla.", "No ayuda a la compañera.", "Es cómplice."], "Cómplice"),
        W("Elegir ayuda segura", "Ian ve que un compañero mayor empuja a uno menor. ¿Qué acción es más segura: acercarse a pelear o avisar de inmediato a un adulto?", ["Pelear puede ser peligroso.", "Avisar a un adulto detiene la agresión.", "La seguridad es la prioridad."], "Avisar de inmediato a un adulto"),
    ],
    [
        M("Pensar que ayudar es meterse donde no me llaman.", "Se confunde ayudar con entrometerse.", "Pregunta «¿quieres que te ayude?» y respeta la respuesta."),
        M("Creer que un testigo que mira no tiene responsabilidad.", "Se olvida que mirar sin hacer nada deja solo a quien sufre.", "Haz algo seguro: acompaña, no te rías, avisa a un adulto."),
    ],
    R=[
        ex("Un testigo que mira y no hace nada, ¿es pasivo o activo?", "Pasivo", "No ayuda a la persona."),
        ex("Avisar a un adulto ante una agresión, ¿es una forma de ayuda? Responde sí o no.", "Sí", "Permite detener el daño."),
        ex("Reírse de una burla, ¿es complicidad o ayuda?", "Complicidad", "Apoya a quien daña."),
    ],
    U=[
        ex("¿Por qué conviene preguntar «¿quieres que te ayude?»", "Porque la persona decide si acepta la ayuda", "Respeta su autonomía."),
        ex("¿Qué es lo primero que debe cuidar un testigo ante una situación peligrosa?", "Su seguridad", "No debe ponerse en riesgo."),
        ex("¿Un testigo activo necesita pelear? Responde sí o no.", "No", "Puede ayudar de formas seguras."),
    ],
    A=[
        ex("Acciones de testigos: 1) decir «basta» con calma; 2) filmar para reírse; 3) acompañar a la persona; 4) avisar a un adulto; 5) mirar y quedarse callado. ¿Cuántas son de un testigo activo?", "3", "Las acciones 1, 3 y 4 ayudan de forma segura."),
        ex("Mati ve que a una compañera le tiraron su cuaderno al suelo. ¿Qué acción es de testigo activo? A) Pasar de largo. B) Ayudar a recoger y preguntar cómo está. C) Reírse con los demás.", "B", "Ayuda y se preocupa por ella."),
        ex("Un compañero está llorando solo. ¿Qué respuesta ofrece ayuda con respeto? A) «¿Quieres que me quede contigo?» B) «Deja de llorar». C) Mirarlo y alejarse.", "A", "Pregunta y respeta lo que decida."),
    ],
    Z=[
        ex("¿Por qué un testigo activo no necesita enfrentarse físicamente al agresor?", "Porque puede ayudar de forma segura", "Avisar y acompañar son opciones seguras."),
        ex("¿Por qué pedir ayuda cuando uno la necesita también es solidaridad?", "Porque permite que otros ayuden y fortalece la comunidad", "La ayuda circula en ambos sentidos."),
    ],
    D=[
        arith("De 32 estudiantes, 20 dijeron que ayudarían a un compañero que lo necesite. ¿Cuántos no lo dijeron?", "32-20", "Se restan los que ayudarían al total."),
        arith("Un grupo ofreció ayuda 3 veces el lunes, 2 el martes y 4 el miércoles. ¿Cuántas veces ofreció ayuda?", "3+2+4", "Se suman las veces de cada día."),
    ],
    context=[ex("Durante el recreo, un grupo se burla de Bruno por su ropa. Valentina dice «basta», se sienta con Bruno y luego avisa a la inspectora. ¿Actuó como testigo activo?", "Sí", "Frenó la burla con calma, acompañó y avisó a un adulto.")],
    selfcheck=[ex("En Orientación: ¿un testigo puede ayudar sin pelear?", "Sí", "Con calma y avisando a un adulto."), ex("¿Reírse de una burla es complicidad?", "Sí", "Apoya a quien daña."), ex("¿Pedir ayuda es parte de la solidaridad?", "Sí", "Fortalece a la comunidad.")],
    task=T("Lee el caso de Leo, un estudiante inventado: tres compañeros esconden la mochila de un niño de otro curso y se ríen. Escribe tres acciones seguras que podría hacer un testigo activo, una frase para decirle al niño y a qué adulto avisarías.", "Acciones: decir «basta» con calma, acompañar al niño, avisar a un adulto. Frase: «¿Quieres que te ayude a buscar tu mochila?» Adulto: la inspectora o el profesor jefe.", ["escribe tres acciones seguras", "escribe una frase respetuosa para la víctima", "nombra un adulto", "no cuenta una vivencia propia"], ["lista escrita o dramatizada"], ["proponer pelear", "no avisar a un adulto"], "Reconoce las acciones y pregunta cuál sería más segura si el grupo fuera grande."),
    reinforce="Escribe dos frases que podrías decir para ayudar sin pelear.",
    extend="Explica la diferencia entre ser un testigo cómplice y uno activo.",
)

lesson(
    OA6, 5,
    "Una hoja y un lápiz. Las situaciones del aula están escritas en los ejercicios.",
    "Aprenderé a respetar el ambiente de aprendizaje: los turnos, el ruido, el trabajo de otros y el uso de aparatos. Sirve para que todos puedan estudiar y participar.",
    ["Sé actuar con empatía y buen trato.", "Sé que mis acciones afectan a otros."],
    [
        "El ambiente de aprendizaje es el conjunto de condiciones que permite a todos concentrarse, participar y sentirse seguros en la sala. Incluye el clima de respeto, el orden, el nivel de ruido, los turnos para hablar y el uso adecuado de materiales y aparatos. Cuando una persona lo altera, afecta a todo el curso.",
        "Algunas conductas que lo cuidan son levantar la mano para hablar, hablar en volumen bajo durante el trabajo, no interrumpir al que expone, mantener los aparatos electrónicos guardados si no se usan para la clase, mantener limpio el espacio y cuidar los materiales de todos. Otras conductas lo dañan: gritar, empujar, esconder las cosas de otros o usar el celular para distraerse en medio de una explicación.",
        "Respetar el ambiente no es obedecer por miedo; es cuidar un espacio común. Si algo lo altera, puedes recordar con respeto el acuerdo del curso: «Quedamos en hablar bajo cuando trabajamos». Si el problema continúa, pide ayuda al docente. Los acuerdos del curso, hechos por todos, funcionan mejor que las órdenes.",
    ],
    [("ambiente de aprendizaje", "condiciones que permiten concentrarse, participar y sentirse seguro"), ("turno", "momento que le corresponde a cada persona para hablar o actuar"), ("acuerdo de curso", "norma decidida entre todos"), ("interrumpir", "cortar a alguien cuando está hablando"), ("distracción", "algo que me saca de la tarea")],
    [
        W("Identificar una conducta que daña", "Durante una exposición, un estudiante habla fuerte con su compañero de atrás. ¿Qué pasa con el ambiente de aprendizaje?", ["El ruido distrae a la clase.", "Quien expone se pierde.", "Se daña el ambiente."], "Se daña: distrae y perjudica al que expone"),
        W("Recordar un acuerdo", "El curso acordó hablar en voz baja al trabajar en grupo. Un compañero está gritando. ¿Qué frase respetuosa sirve: «Quedamos en hablar bajo; ¿puedes bajar la voz?» o «Cállate»?", ["La primera recuerda el acuerdo.", "La segunda es una orden agresiva.", "El respeto cuida a todos."], "«Quedamos en hablar bajo; ¿puedes bajar la voz?»"),
    ],
    [
        M("Creer que si no me castigan, entonces no molesto.", "Se mide el comportamiento por la sanción y no por el efecto.", "Pregúntate si lo que hago deja que otros aprendan."),
        M("Usar el celular 'solo un rato' mientras el profesor explica.", "Se subestima la distracción.", "Guarda el aparato si no es para la clase."),
    ],
    R=[
        ex("Levantar la mano para hablar, ¿cuida el ambiente de aprendizaje? Responde sí o no.", "Sí", "Ordena los turnos."),
        ex("Gritar durante una exposición, ¿cuida o daña el ambiente de aprendizaje?", "Daña", "Distrae a todos."),
        ex("¿Los acuerdos del curso se hacen entre todos? Responde sí o no.", "Sí", "Por eso funcionan mejor."),
    ],
    U=[
        ex("¿Por qué interrumpir a alguien que expone daña el ambiente?", "Porque le quita la concentración", "Le impide hacer su trabajo."),
        ex("¿Por qué usar el celular para otra cosa durante la clase afecta también a otros?", "Porque distrae y da mal ejemplo", "Otros pueden distraerse también."),
        ex("¿Qué conviene hacer si un compañero rompe un acuerdo del curso: recordarlo con respeto o gritarle?", "Recordarlo con respeto", "Cuida la relación y el acuerdo."),
    ],
    A=[
        ex("Conductas: 1) pedir la palabra; 2) esconder el lápiz de otro; 3) hablar bajo en grupo; 4) revisar el celular durante una explicación; 5) dejar limpio el puesto. ¿Cuántas cuidan el ambiente de aprendizaje?", "3", "Los números 1, 3 y 5 lo cuidan; 2 y 4 lo dañan."),
        ex("Una compañera termina antes y se pone a conversar fuerte. ¿Qué acción cuida mejor el ambiente? A) Leer un libro en silencio. B) Conversar bajito con alguien. C) Gritar para que la miren.", "A", "No molesta a quienes aún trabajan."),
        ex("Beto tiene el celular guardado y solo lo usa cuando la profesora lo permite para buscar información. ¿Cuida el ambiente? Responde sí o no.", "Sí", "Usa el aparato para la clase y no distrae."),
    ],
    Z=[
        ex("¿Por qué los acuerdos que hace todo el curso se cumplen mejor que las órdenes impuestas?", "Porque todos participaron y se sienten responsables", "Se respetan más las normas en las que se participa."),
        ex("Si un solo estudiante hace ruido, ¿afecta solo a él? Responde sí o no.", "No", "Afecta a todo el curso."),
    ],
    D=[
        arith("Una clase dura 90 minutos y se perdieron 12 por interrupciones. ¿Cuántos minutos se pudo trabajar?", "90-12", "Se restan los minutos perdidos al total."),
        arith("En 5 clases de 90 minutos, ¿cuántos minutos de aprendizaje hay en total?", "90*5", "Se multiplican los minutos por las clases."),
    ],
    context=[ex("Durante una prueba, Tomás nota que un compañero conversa en voz baja. Tomás levanta la mano y le dice a la profesora: «Estoy perdiendo la concentración; ¿podemos pedir silencio?». ¿Cuidó el ambiente de forma respetuosa?", "Sí", "Pidió ayuda de forma calmada para proteger el trabajo de todos.")],
    selfcheck=[ex("En Orientación: ¿el ambiente de aprendizaje es responsabilidad de todos?", "Sí", "Todos lo cuidan o lo dañan."), ex("¿Interrumpir cuida el ambiente?", "No", "Quita la concentración."), ex("¿Un acuerdo del curso se puede recordar con respeto?", "Sí", "Así se mantiene.")],
    task=T("Escribe cuatro acuerdos para un curso inventado que quiere cuidar su ambiente de aprendizaje: uno sobre el ruido, uno sobre los turnos, uno sobre los aparatos electrónicos y uno sobre el cuidado de materiales. Luego escribe una frase para recordar un acuerdo con respeto.", "1) Hablamos en voz baja al trabajar. 2) Levantamos la mano para hablar. 3) Los celulares quedan guardados salvo que la profesora los pida. 4) Dejamos limpio el espacio y cuidamos los materiales. Frase: «Quedamos en hablar bajo; ¿puedes bajar la voz?»", ["cuatro acuerdos claros", "cada acuerdo es posible de cumplir", "una frase respetuosa", "no cuenta una vivencia propia"], ["lista escrita"], ["acuerdos imposibles", "frase agresiva"], "Reconoce los acuerdos y pregunta cómo harían para evaluarlos en dos semanas."),
    reinforce="Escribe tres conductas que cuidan el ambiente de aprendizaje y tres que lo dañan.",
    extend="Explica por qué un buen ambiente de aprendizaje es un derecho de todos y una responsabilidad de todos.",
)

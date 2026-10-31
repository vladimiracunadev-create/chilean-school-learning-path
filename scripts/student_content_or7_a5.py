"""Cuaderno del estudiante, 7.º básico Orientación: OA 09 (intereses, aprendizaje y proyecto personal) y OA 10 (metas progresivas y gestión autónoma del aprendizaje)."""
from __future__ import annotations

from student_content_or7_a import M, T, W, lesson
from student_lessons import arith, ex

OA9, OA10 = "OR07 OA 09", "OR07 OA 10"

# ================================================================ OA 09
lesson(
    OA9, 1,
    "Una hoja y un lápiz. El perfil de Fernanda, una estudiante inventada, y las frases para clasificar están escritos en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a distinguir mis intereses, motivaciones, necesidades y capacidades. Sirve para conocerme mejor y para pensar qué quiero aprender y hacer en los próximos años.",
    ["Sé que el autoconcepto tiene características, motivaciones, intereses y capacidades.", "Sé que mi opinión sobre mí necesita hechos."],
    [
        "Para pensar en un proyecto personal conviene conocer cuatro cosas de ti. Los intereses son los temas o actividades que te llaman la atención, como los animales, la música o la tecnología. Las motivaciones son las razones que te mueven a actuar: ayudar a otros, ganar autonomía, aprender, ser reconocido. Las necesidades son lo que requieres para estar bien y avanzar, como tiempo de estudio, apoyo o materiales. Las capacidades son lo que puedes hacer hoy o puedes aprender a hacer con práctica.",
        "Estas cuatro cosas se relacionan. Una persona puede tener interés en los animales (interés), querer cuidar su salud (motivación), necesitar libros y tiempo para estudiar (necesidades) y tener buena paciencia para observar (capacidad). Conocerlas te ayuda a elegir actividades, talleres o estudios con más sentido. Y como cambian, conviene revisarlas de vez en cuando.",
        "Para reconocerlas hay pistas. Fíjate en qué haces cuando eres libre, qué aprendes con facilidad, qué te cuesta pero quieres mejorar y qué te hace sentir orgullo. También pregúntate por qué haces algo: la respuesta suele mostrar tu motivación. Usa hechos: «construí un comedero para pájaros» es mejor que «me gustan los animales».",
    ],
    [("interés", "tema o actividad que llama mi atención"), ("motivación", "razón que me mueve a actuar"), ("necesidad", "lo que requiero para estar bien y avanzar"), ("capacidad", "lo que puedo hacer o aprender a hacer"), ("proyecto personal", "plan de lo que quiero lograr y cómo")],
    [
        W("Clasificar", "Fernanda, una estudiante inventada, dice: «Quiero entender cómo viven los animales para ayudar a cuidarlos». ¿Qué parte nombra una motivación?", ["La razón que la mueve es ayudar a cuidarlos.", "Los animales son el interés.", "La motivación es ayudar a cuidarlos."], "Ayudar a cuidarlos"),
        W("Usar hechos", "¿Cuál frase usa mejor un hecho: «Me gusta la tecnología» o «Armé un circuito simple con una pila y una ampolleta»?", ["La segunda cuenta algo que hizo.", "La primera es general.", "La segunda usa un hecho."], "«Armé un circuito simple con una pila y una ampolleta»"),
    ],
    [
        M("Pensar que mis intereses son para siempre.", "Se cree que lo que me gusta hoy no cambiará.", "Los intereses cambian y está bien revisarlos."),
        M("Creer que una necesidad es lo mismo que un capricho.", "Se mezclan lo que quiero con lo que requiero.", "Una necesidad es lo que permite estar bien y avanzar."),
    ],
    R=[
        ex("«Me llama la atención la música». ¿Es un interés o una necesidad?", "Un interés", "Es un tema que le llama la atención."),
        ex("«Necesito un lugar tranquilo para estudiar». ¿Es una necesidad o una capacidad?", "Una necesidad", "Es algo que requiere para avanzar."),
        ex("«Puedo explicar fracciones a otros». ¿Es una capacidad o una motivación?", "Una capacidad", "Es algo que puede hacer."),
    ],
    U=[
        ex("¿Por qué conviene revisar de vez en cuando los intereses?", "Porque pueden cambiar", "Con el tiempo aparecen nuevos intereses."),
        ex("¿Qué pista te muestra tu motivación: qué haces cuando eres libre o por qué haces algo?", "Por qué haces algo", "La razón muestra lo que te mueve."),
        ex("¿Una capacidad se puede mejorar con práctica, sí o no?", "Sí", "Se puede aprender y fortalecer."),
    ],
    A=[
        ex("Frases de Fernanda: 1) «Me gustan los animales»; 2) «Quiero cuidarlos»; 3) «Necesito libros y tiempo»; 4) «Soy paciente observando». ¿Cuántas son capacidades?", "1", "Solo la 4 muestra algo que puede hacer."),
        ex("Un estudiante escribe «Me gusta el fútbol porque siento que trabajo en equipo». ¿Qué parte es la motivación? A) Trabajar en equipo. B) El fútbol.", "A", "La razón que lo mueve es trabajar en equipo; el fútbol es el interés."),
        ex("Fernanda no tiene un computador en casa y necesita buscar información. ¿Qué necesidad aparece?", "Acceso a información o a un computador", "Requiere un recurso para avanzar."),
    ],
    Z=[
        ex("Tomás dice: «No tengo intereses». ¿Qué pregunta le ayudaría a descubrirlos?", "¿Qué haces cuando eres libre y qué te hace sentir orgullo?", "Las actividades libres suelen mostrar intereses."),
        ex("¿Por qué es mejor una frase con hechos que una general al describir tus intereses?", "Porque muestra lo que realmente haces", "Un hecho se puede comprobar."),
    ],
    D=[
        arith("Fernanda anotó 12 ideas sobre sí misma: 4 intereses, 3 motivaciones, 2 necesidades y el resto capacidades. ¿Cuántas son capacidades?", "12-4-3-2", "Al total se le restan los otros tres grupos."),
        arith("Si escribe 2 hechos por cada una de las 4 partes, ¿cuántos hechos escribe?", "4*2", "Se multiplican partes por hechos."),
    ],
    context=[ex("En una actividad del curso piden escribir «Mi interés, mi motivación, mi necesidad y mi capacidad». Pablo escribe «interés: ganar dinero». ¿Qué le falta para que sea un interés claro?", "Un tema o actividad concreta", "Ganar dinero es un fin, no un tema que le llame la atención.")],
    selfcheck=[ex("En Orientación: ¿mis intereses pueden cambiar?", "Sí", "Es normal en la adolescencia."), ex("¿Una necesidad es lo que requiero para avanzar?", "Sí", "Por ejemplo tiempo de estudio."), ex("¿Las capacidades se pueden mejorar?", "Sí", "Se fortalecen con práctica.")],
    task=T("Lee el perfil inventado de Benjamín: construyó un cohete de papel con una amiga, le gusta preguntar cómo funcionan las cosas, quiere ser ingeniero para ayudar a otros, y necesita más tiempo para leer. Escribe un interés, una motivación, una necesidad y una capacidad de Benjamín, cada una con su hecho.", "Interés: ciencia. Motivación: ayudar a otros. Necesidad: más tiempo para leer. Capacidad: construir, porque hizo un cohete de papel.", ["escribe las cuatro partes", "cada una con un hecho del perfil", "no confunde interés con capacidad", "no cuenta nada personal"], ["cuadro escrito"], ["confundir partes", "no usar hechos"], "Reconoce el cuadro y pregunta qué parte sería más fácil de cambiar con el tiempo."),
    reinforce="Escribe cuatro frases de un personaje de cuento: un interés, una motivación, una necesidad y una capacidad.",
    extend="Explica por qué conocer tus necesidades te ayuda a elegir un proyecto.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. El caso de Matías, un estudiante inventado, y la tabla de conexiones entre intereses y asignaturas están escritos en los ejercicios.",
    "Aprenderé por qué el aprendizaje escolar ordenado ayuda a desarrollar mis intereses y capacidades. Sirve para ver el sentido de lo que estudio y para no dejar de lado mi derecho a aprender.",
    ["Sé reconocer intereses, motivaciones, necesidades y capacidades.", "Sé separar hechos de opiniones."],
    [
        "El aprendizaje escolar sistemático es aprender de forma ordenada y progresiva: se parte de lo básico y se avanza, con práctica, apoyo y evaluación. Es distinto de aprender solo lo que aparece por casualidad en videos o redes. Ver videos puede despertar un interés, pero la escuela entrega bases que permiten comprender y crear, como leer con atención, escribir con claridad, calcular o usar métodos científicos.",
        "Casi todos los intereses conectan con varias asignaturas. Matías, un estudiante inventado, quiere hacer videojuegos. Para ello usa Matemática (coordenadas, cálculos), Lenguaje (guion, argumentos), Inglés (muchos recursos están en inglés), Artes (diseño) y Tecnología (programación). Un interés se desarrolla mejor si se construyen las bases. Además, estudiar es un derecho: todas las personas tienen derecho a aprender.",
        "A veces el estudio produce aburrimiento, ansiedad o frustración. Esas emociones son normales. En lugar de abandonar, puedes buscar la conexión con tu interés, pedir otra forma de aprender o partir por una meta pequeña. Y distingue los hechos («sacó 11 de 20») de las opiniones («esto no sirve»). Con hechos se decide mejor.",
    ],
    [("sistemático", "ordenado y progresivo, con práctica y evaluación"), ("bases", "conocimientos que permiten seguir aprendiendo"), ("conexión", "relación entre dos cosas"), ("derecho a aprender", "derecho de toda persona a educarse"), ("frustración", "emoción cuando algo no sale como esperábamos")],
    [
        W("Conectar interés y asignatura", "Matías quiere hacer videojuegos. ¿Qué asignatura le sirve para escribir un guion?", ["El guion es un texto.", "Se escribe y se argumenta.", "Lenguaje."], "Lenguaje y Comunicación"),
        W("Separar hecho y opinión", "Matías dice: «Matemática no sirve». Su nota fue 11 de 20 en una prueba. ¿Cuál es el hecho?", ["La nota se puede comprobar.", "«No sirve» es una opinión.", "El hecho es 11 de 20."], "Sacó 11 de 20 en una prueba"),
    ],
    [
        M("Pensar que aprender solo lo que me gusta es suficiente.", "Se cree que las bases no importan.", "Las bases escolares permiten avanzar en mi interés."),
        M("Creer que si algo me aburre, no sirve.", "Se confunde emoción con utilidad.", "Busca la conexión con tu interés."),
    ],
    R=[
        ex("Escribir un guion de videojuego, ¿se relaciona con Lenguaje o con Educación Física?", "Con Lenguaje", "Se escribe y se argumenta."),
        ex("Calcular las coordenadas de un personaje, ¿se relaciona con Matemática, sí o no?", "Sí", "Usa números y posiciones."),
        ex("¿Estudiar es un derecho de todas las personas, sí o no?", "Sí", "Todos tienen derecho a aprender."),
    ],
    U=[
        ex("¿Por qué el aprendizaje escolar entrega bases para desarrollar un interés?", "Porque enseña de forma ordenada y progresiva", "Las bases permiten seguir aprendiendo."),
        ex("¿Qué se puede hacer ante el aburrimiento: conectar con mi interés o abandonar?", "Conectar con mi interés", "Se busca darle sentido."),
        ex("¿Un video puede reemplazar totalmente el aprendizaje escolar, sí o no?", "No", "Falta orden, práctica y evaluación."),
    ],
    A=[
        ex("Conexiones: 1) cálculo de coordenadas; 2) guion; 3) leer instrucciones en inglés; 4) dibujar personajes. ¿Cuántas se relacionan con Matemática o Inglés?", "2", "La 1 es de Matemática y la 3 de Inglés."),
        ex("Valentina quiere ser veterinaria. Opciones: A) Reforzar Ciencias y Matemática. B) Dejar de estudiar porque aprende en videos.", "A", "Son bases que necesitará."),
        ex("Un estudiante dice «Esta materia no me sirve». ¿Qué pregunta le ayuda a darle sentido?", "¿En qué de mi interés se usa?", "Conecta lo que estudia con lo que le importa."),
    ],
    Z=[
        ex("Rodrigo dice: «Si sé jugar, no necesito estudiar». ¿Qué error hay?", "Jugar no reemplaza las bases para crear", "Para crear se necesita Matemática, Lenguaje y otras bases."),
        ex("¿Por qué conviene tener una meta pequeña cuando algo se hace difícil?", "Porque da avances posibles", "Una meta pequeña se puede lograr."),
    ],
    D=[
        ex("Matías dice que sus videos de juegos le enseñan todo lo que necesita. ¿Qué hay en la escuela que esos videos no entregan?", "Práctica ordenada, apoyo y evaluación", "El aprendizaje sistemático avanza paso a paso y se evalúa."),
        arith("En una prueba de 25 puntos, Matías sacó 14. ¿Cuántos puntos le faltaron?", "25-14", "Se resta lo obtenido al total."),
    ],
    context=[ex("En el curso, Josefa dice que quiere ser cantante y que la escuela no le sirve. Su profesora le muestra que debe aprender a leer partituras, a hablar en público y a escribir letras. ¿Qué enseña eso?", "Que su interés se conecta con lo que se aprende en la escuela", "Las bases escolares apoyan su meta.")],
    selfcheck=[ex("En Orientación: ¿los intereses se conectan con varias asignaturas?", "Sí", "Casi todos los intereses usan varias asignaturas."), ex("¿Aprender es un derecho?", "Sí", "De toda persona."), ex("En Orientación: ¿Una opinión es lo mismo que un hecho?", "No", "La opinión no se comprueba.")],
    task=T("Lee el caso inventado de Isabel: le encantan los animales y quiere ser veterinaria, pero dice que Matemática y Lenguaje «no sirven». Escribe tres conexiones entre su interés y asignaturas, un hecho y una opinión del caso, y una meta pequeña para que Matemática tenga más sentido.", "Conexiones: Ciencias (anatomía), Matemática (dosis y cuentas), Lenguaje (informes). Hecho: quiere ser veterinaria. Opinión: «no sirven». Meta: resolver 5 problemas de proporciones con ejemplos de animales.", ["escribe tres conexiones", "separa hecho y opinión", "propone una meta pequeña", "no cuenta nada personal"], ["texto escrito"], ["no conectar con su interés", "confundir hecho y opinión"], "Reconoce las conexiones y pregunta cuál asignatura le costaría más conectar."),
    reinforce="Conecta un interés inventado con tres asignaturas.",
    extend="Explica la diferencia entre aprender por casualidad y aprender de forma sistemática.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. El caso de Camilo, un estudiante inventado, y las opciones de exploración están escritos en los ejercicios.",
    "Aprenderé a comparar formas de explorar un interés y a anticipar sus consecuencias. Sirve para elegir qué hacer con mi tiempo y dar pasos reales hacia un proyecto personal.",
    ["Sé conectar intereses con asignaturas.", "Sé que cada decisión tiene consecuencias."],
    [
        "Cuando tienes un interés puedes explorarlo de varias maneras. Puedes participar en un taller o club del colegio, que ofrece práctica y compañeros. Puedes leer o ver material confiable, que da información pero sin práctica. Puedes conversar con alguien que trabaje en eso, como un familiar adulto o un profesor, que te da una visión real. Puedes practicar en casa con tareas seguras. Cada opción tiene ventajas y límites, y tiempo que cuesta.",
        "Para comparar, mira cuatro cosas: cuánto tiempo requiere, qué aprendes, si es seguro y accesible y cómo se relaciona con tus capacidades. Por ejemplo, Camilo quiere explorar la fotografía. En el taller aprende con apoyo; leyendo aprende teoría; practicando en la casa mira la luz; hablando con un fotógrafo adulto conoce la profesión. Combinar dos opciones suele dar mejores resultados que usar una sola.",
        "Ten en cuenta el tiempo: tienes 24 horas al día y debes estudiar, descansar y convivir. Un proyecto personal debe caber en tu semana sin quitar sueño ni estudio. Y cuida tu seguridad: en actividades en línea, no compartas datos personales y avisa a un adulto de tu casa.",
    ],
    [("explorar", "probar y conocer algo para ver si me interesa"), ("taller", "actividad en que se aprende practicando"), ("accesible", "que se puede alcanzar con los recursos que hay"), ("combinar", "usar dos o más opciones juntas"), ("tiempo disponible", "horas que puedo dedicar sin afectar estudio ni descanso")],
    [
        W("Comparar dos opciones", "Camilo quiere explorar la fotografía. Opción A: un taller semanal en el colegio. Opción B: leer un libro. ¿Cuál le da práctica con apoyo?", ["El taller ofrece práctica.", "También hay un guía.", "La opción A."], "El taller semanal"),
        W("Calcular el tiempo", "Camilo tiene 4 horas libres a la semana. El taller ocupa 2 horas. ¿Cuántas le quedan para otras cosas?", ["Se restan las horas del taller.", "4 − 2 = 2.", "Le quedan 2 horas."], "2 horas"),
    ],
    [
        M("Pensar que explorar un interés exige hacer todo a la vez.", "Se cree que más actividades es mejor.", "Elige una o dos opciones que quepan en tu semana."),
        M("Creer que solo leer sobre algo basta para saber si me gusta.", "Se olvida la práctica.", "Practicar ayuda a comprobar el interés."),
    ],
    R=[
        ex("Un taller semanal, ¿ofrece práctica, sí o no?", "Sí", "Se aprende haciendo."),
        ex("Conversar con un adulto que trabaja en eso, ¿da una visión real, sí o no?", "Sí", "Cuenta cómo es en la vida real."),
        ex("¿Debe un proyecto quitar horas de sueño, sí o no?", "No", "Debe caber sin afectar el descanso."),
    ],
    U=[
        ex("¿Por qué combinar dos opciones suele ayudar?", "Porque se suman práctica e información", "Cada opción aporta algo distinto."),
        ex("¿Qué cuatro cosas conviene mirar al comparar?", "Tiempo, qué aprendo, seguridad y relación con mis capacidades", "Permiten decidir con criterio."),
        ex("En línea, ¿debes compartir tus datos personales para explorar un interés, sí o no?", "No", "Hay que cuidar la seguridad."),
    ],
    A=[
        ex("Opciones: 1) taller; 2) leer; 3) practicar en casa; 4) dejar de dormir y de estudiar para dedicar todo el tiempo al interés. ¿Cuántas son razonables?", "3", "Las tres primeras caben en la semana; la cuarta quita sueño y estudio."),
        ex("Camilo tiene 5 horas libres y el taller dura 2 horas y la práctica en casa 2 horas. A) Le sobra 1 hora. B) Le faltan 2 horas.", "A", "5 menos 4 es 1."),
        ex("Una persona mayor que no conoces te ofrece enseñarte a cambio de que no avises a nadie. ¿Qué haces?", "No acepto y aviso a un adulto de confianza", "Un secreto así es una señal de peligro."),
    ],
    Z=[
        ex("Tomás dice: «Si no pruebo todo, pierdo oportunidades». ¿Qué respondes?", "Que probar una o dos opciones bien es más útil", "Hacer todo a la vez agota y no profundiza."),
        ex("¿Por qué es importante revisar si la opción es accesible?", "Porque debe poder realizarse con lo que tengo", "Una opción imposible no ayuda."),
    ],
    D=[
        arith("En una semana de 7 días, si Camilo dedica 2 horas al taller y 1 hora diaria de práctica los 5 días hábiles, ¿cuántas horas dedica en total?", "2+1*5", "Se suma el taller más la práctica de los 5 días."),
        arith("De 25 horas libres al mes, usó 18. ¿Cuántas le quedan?", "25-18", "Se restan las horas usadas."),
    ],
    context=[ex("En el colegio hay talleres de música, robótica y teatro. Isidora tiene tiempo para uno. Le interesan los instrumentos. ¿Cuál elegiría?", "Música", "Se relaciona con su interés.")],
    selfcheck=[ex("En Orientación: ¿conviene comparar opciones para explorar un interés?", "Sí", "Permite decidir mejor."), ex("¿Un proyecto debe respetar mi tiempo de descanso?", "Sí", "No debe quitar sueño."), ex("¿Debo avisar a un adulto si alguien me pide secreto en línea?", "Sí", "Es una señal de alerta.")],
    task=T("Lee el caso inventado de Sofía: le interesa la astronomía y tiene 4 horas libres a la semana. Opciones: club de ciencias (2 horas), leer sobre el cielo (1 hora), observar la luna desde su casa un rato (1 hora). Compara las tres opciones, elige una combinación que quepa en las 4 horas y explica por qué.", "Combina club (2 h), lectura (1 h) y observación (1 h): suman 4 horas. Club da apoyo y práctica; lectura, información; observación, práctica real. Cabe sin quitar descanso.", ["compara las tres opciones", "elige una combinación que cabe", "explica por qué", "no cuenta nada personal"], ["texto escrito"], ["pasarse del tiempo", "no justificar"], "Reconoce la combinación y pregunta qué dejaría si tuviera menos tiempo."),
    reinforce="Escribe tres formas de explorar un interés de un personaje y una ventaja de cada una.",
    extend="Explica por qué es importante dejar tiempo libre al planificar un proyecto.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. El esquema de proyecto personal y el caso de Antonia, una estudiante inventada, están escritos en los ejercicios.",
    "Aprenderé a armar un proyecto personal inicial con meta, pasos y apoyos, y a revisar mis decisiones si mis intereses cambian. Sirve para dar un primer plan realista y seguro para los próximos años.",
    ["Sé explorar intereses y comparar opciones.", "Sé que el aprendizaje escolar es una base."],
    [
        "Un proyecto personal es un plan de lo que quieres lograr y cómo. Para armarlo, usa un esquema de cinco partes: la meta (lo que quieres lograr), por qué te importa (tu motivación), los pasos (acciones concretas), los apoyos (personas y recursos que te ayudan) y la revisión (cuándo verás cómo vas). Una meta puede ser cercana, como aprender a tocar tres canciones este año, o más lejana, como decidir qué estudiar después del colegio.",
        "Es normal que tus intereses cambien. Revisar tu proyecto no es fracasar, es ajustarlo a lo que aprendiste de ti. También es válido tener dudas. Si tu familia o tus amigos esperan algo distinto de lo que quieres, puedes conversar con respeto, mostrar tus razones y escuchar las suyas. Una persona orientadora del colegio puede ayudarte.",
        "Una acción segura al armar tu proyecto es compartirlo con una persona adulta de confianza, no publicar datos personales, no aceptar propuestas de desconocidos y cuidar que tus pasos no pongan en riesgo tu salud ni tus estudios. Un proyecto es una guía, no una obligación rígida.",
    ],
    [("meta", "lo que quiero lograr, con claridad"), ("paso", "acción concreta para acercarme a mi meta"), ("apoyo", "persona o recurso que me ayuda"), ("revisión", "momento en que veo cómo voy"), ("orientador", "profesional del colegio que ayuda a pensar el futuro")],
    [
        W("Completar el esquema", "Antonia quiere aprender a dibujar cómics. Escribe su meta con un paso, un apoyo y una revisión.", ["Meta: dibujar un cómic de 4 páginas.", "Paso: practicar 20 minutos diarios.", "Apoyo: su profesora de Artes. Revisión: cada mes."], "Meta: un cómic de 4 páginas; paso: 20 minutos diarios; apoyo: profesora de Artes; revisión: cada mes"),
        W("Ajustar el proyecto", "Antonia descubre que le gusta más escribir las historias que dibujarlas. ¿Qué hace con su proyecto?", ["Cambiar de interés no es fracasar.", "Puede ajustar la meta.", "Puede centrarse en el guion."], "Ajusta su meta y se centra en escribir historias"),
    ],
    [
        M("Pensar que mi proyecto debe ser perfecto desde el inicio.", "Se confunde un plan con una promesa fija.", "Un proyecto se ajusta con lo que aprendes."),
        M("Creer que cambiar de interés significa que fracasé.", "Se ve el cambio como error.", "Cambiar de interés es parte de conocerse."),
    ],
    R=[
        ex("¿Un proyecto personal tiene meta, pasos, apoyos y revisión, sí o no?", "Sí", "Son parte del esquema."),
        ex("Cambiar un interés, ¿significa fracasar, sí o no?", "No", "Es normal y permite ajustar."),
        ex("¿Se puede conversar con la familia si piensan distinto de mí, sí o no?", "Sí", "Con respeto y razones."),
    ],
    U=[
        ex("¿Por qué conviene incluir apoyos en el proyecto?", "Porque nadie logra todo solo", "Las personas y recursos ayudan a avanzar."),
        ex("¿Por qué es útil la revisión?", "Porque permite ajustar", "Se ve qué funciona y qué no."),
        ex("¿Debe un proyecto poner en riesgo mi salud o mis estudios, sí o no?", "No", "Debe cuidar ambos."),
    ],
    A=[
        ex("Partes: 1) meta; 2) paso; 3) apoyo; 4) revisión. «Practicar 20 minutos diarios» es: A) un paso. B) una revisión.", "A", "Es una acción concreta."),
        ex("Antonia quiere publicar sus dibujos con su nombre completo y colegio en una cuenta pública. ¿Qué consejo le darías?", "No publicar datos personales y avisar a un adulto", "Debe cuidar su seguridad."),
        ex("Una meta es «ser buena en Artes». ¿Qué le falta para ser clara?", "Algo medible y un plazo", "Debe decir qué hará y cuándo."),
    ],
    Z=[
        ex("Lucas dice: «Si mi familia quiere otra cosa, no puedo opinar». ¿Qué respondes?", "Puedes conversar con respeto y explicar tus razones", "Tus intereses también importan."),
        ex("¿Por qué un proyecto con una sola gran meta lejana puede desanimar?", "Porque se ve difícil de alcanzar", "Conviene dividirlo en pasos."),
    ],
    D=[
        arith("Antonia practica 15 minutos al día durante 5 días hábiles. ¿Cuántos minutos practica en una semana?", "15*5", "Se multiplican minutos por días."),
        arith("En 4 semanas, ¿cuántos minutos de práctica suma si mantiene ese ritmo?", "15*5*4", "Se multiplica por las semanas."),
    ],
    context=[ex("Un tío de Antonia le dice que debe estudiar contabilidad «porque tiene futuro», aunque a ella le gusta el arte. ¿Qué puede hacer?", "Conversar con respeto, escuchar sus razones y explicar las suyas", "Es una decisión que se conversa.")],
    selfcheck=[ex("En Orientación: ¿puedo ajustar mi proyecto personal?", "Sí", "Es parte de conocerme."), ex("¿Es bueno compartir mi proyecto con un adulto de confianza?", "Sí", "Ayuda a orientarme."), ex("¿Debo publicar mis datos personales para mi proyecto?", "No", "Puede ser riesgoso.")],
    task=T("Arma el proyecto personal inventado de Joaquín, que quiere aprender a tocar guitarra este año: escribe la meta, por qué le importa, tres pasos, un apoyo y cuándo revisará. Agrega una acción de seguridad.", "Meta: tocar tres canciones sencillas en diciembre. Por qué: le gusta la música. Pasos: practicar 20 minutos diarios, aprender acordes, ensayar con un compañero. Apoyo: profesor de música. Revisión: cada mes. Seguridad: no publicar datos personales.", ["incluye las cinco partes", "los pasos son concretos", "incluye una acción de seguridad", "no cuenta nada personal"], ["esquema escrito"], ["meta vaga", "olvidar la revisión"], "Reconoce el esquema y pregunta qué cambiaría si la guitarra no le gusta."),
    reinforce="Escribe una meta, un paso y un apoyo para un personaje de cuento.",
    extend="Explica por qué un proyecto personal puede cambiar sin que sea un fracaso.",
)

# ================================================================ OA 10
lesson(
    OA10, 1,
    "Una hoja y un lápiz. El caso de Isidora, una estudiante inventada, y las metas de ejemplo están escritos en los ejercicios.",
    "Aprenderé qué es una meta progresiva y sus cuatro partes: meta, línea de acción, monitoreo y redefinición. Sirve para gestionar de manera autónoma mi aprendizaje en el colegio.",
    ["Sé escribir una meta clara.", "Sé que el aprendizaje avanza con práctica."],
    [
        "Gestionar tu propio aprendizaje es hacerte cargo de cómo estudias y avanzas. Para ello se usan cuatro partes. La meta es lo que quieres lograr, con claridad y plazo. Una meta progresiva se divide en pasos que suben poco a poco, como pasar de resolver 5 ejercicios a 10 y luego a 15. La línea de acción es lo que harás para lograrla: cuándo estudias, qué método usas y qué ayuda pides. El monitoreo es revisar cuánto avanzas, con datos. La redefinición es ajustar la meta o las acciones si es necesario.",
        "Una meta bien escrita responde: ¿qué logrará?, ¿en cuánto tiempo?, ¿cómo lo sabré? Por ejemplo: «En 6 semanas, resolveré bien 12 de 15 ejercicios de ecuaciones». Eso se puede revisar. En cambio «mejorar en Matemática» es vaga. Las metas progresivas son mejores que una sola gran meta, porque cada avance motiva y permite corregir.",
        "Isidora, una estudiante inventada, tiene dificultad en Matemática. Define metas: semana 2, resolver 6 de 10 ejercicios; semana 4, 8 de 10; semana 6, 9 de 10. Su línea de acción es estudiar 20 minutos diarios y preguntar en clases. Cada semana anota su avance. Si no llega, ajusta tiempos o pide apoyo.",
    ],
    [("meta progresiva", "meta dividida en pasos que suben poco a poco"), ("línea de acción", "lo que haré para lograr la meta"), ("monitoreo", "revisar con datos cuánto avanzo"), ("redefinir", "ajustar la meta o las acciones"), ("autónomo", "que se hace cargo de sí mismo")],
    [
        W("Reconocer una buena meta", "¿Cuál es una buena meta: «Mejorar en Matemática» o «En 6 semanas, resolver bien 12 de 15 ejercicios de ecuaciones»?", ["La primera es vaga.", "La segunda dice cuánto y en cuánto tiempo.", "La segunda es mejor."], "«En 6 semanas, resolver bien 12 de 15 ejercicios de ecuaciones»"),
        W("Clasificar partes", "Isidora anota cada semana cuántos ejercicios resolvió bien. ¿Qué parte es?", ["Revisa su avance.", "Usa datos.", "Es el monitoreo."], "El monitoreo"),
    ],
    [
        M("Pensar que una sola gran meta es mejor que varias pequeñas.", "Se cree que más grande motiva más.", "Las metas progresivas dan avances y permiten corregir."),
        M("Creer que si cambio la meta, me rendí.", "Se confunde ajustar con abandonar.", "Redefinir es parte de gestionar bien."),
    ],
    R=[
        ex("«Estudiar 20 minutos diarios», ¿es una línea de acción o un monitoreo?", "Una línea de acción", "Es lo que hará."),
        ex("Anotar cuántos ejercicios resolvió, ¿es monitoreo o redefinición?", "Monitoreo", "Revisa su avance con datos."),
        ex("Ajustar la meta si no se logra, ¿es redefinir, sí o no?", "Sí", "Es cambiar la meta o las acciones."),
    ],
    U=[
        ex("¿Por qué una meta progresiva ayuda a no desanimarse?", "Porque cada avance se logra por pasos", "Se ven resultados a corto plazo."),
        ex("¿Qué tiene una meta bien escrita?", "Qué, cuánto y en cuánto tiempo", "Así se puede revisar."),
        ex("¿Gestionar autónomamente es hacerse cargo del propio aprendizaje, sí o no?", "Sí", "Esa es la definición."),
    ],
    A=[
        arith("Metas de Rafael en ejercicios bien resueltos: semana 2, 5; semana 4, 8; semana 6, 12. ¿Cuántos más debe resolver bien en la semana 6 que en la semana 2?", "12-5", "Se resta la meta inicial a la final."),
        ex("Frases: 1) «Seré mejor»; 2) «En 4 semanas, leeré 3 capítulos»; 3) «Haré lo que pueda»; 4) «Resolveré 5 ejercicios por día durante 2 semanas». ¿Cuántas son metas claras?", "2", "La 2 y la 4 dicen qué, cuánto y en cuánto tiempo."),
        ex("Isidora llegó a 5 de 10 en la semana 2, y su meta era 6. ¿Qué hace? A) Revisa su línea de acción y la ajusta. B) Se rinde.", "A", "Redefinir permite seguir."),
    ],
    Z=[
        ex("Daniel dice: «Si no cumplo la meta una vez, no sirvo para esto». ¿Qué responderías?", "Que redefinir y ajustar es parte de aprender", "Un resultado no define a la persona."),
        ex("¿Por qué el monitoreo necesita datos y no solo sensaciones?", "Porque los datos muestran el avance real", "Las sensaciones pueden engañar."),
    ],
    D=[
        arith("Isidora quiere pasar de 6 a 9 ejercicios correctos en pasos iguales de 1 por semana. ¿Cuántas semanas necesita?", "9-6", "Cada semana suma 1; la diferencia es el número de semanas."),
        arith("Si estudia 20 minutos al día los 5 días hábiles de la semana, ¿cuántos minutos son a la semana?", "20*5", "Se multiplican minutos por días."),
    ],
    context=[ex("Un curso se propone leer un libro entero en un mes. Algunos dicen que es mucho. ¿Cómo lo vuelven progresivo?", "Dividiendo en capítulos por semana", "Se avanza por pasos.")],
    selfcheck=[ex("En Orientación: ¿una meta progresiva se divide en pasos?", "Sí", "Va subiendo poco a poco."), ex("¿El monitoreo usa datos?", "Sí", "Para ver el avance."), ex("¿Redefinir es fracasar?", "No", "Es ajustar para seguir avanzando.")],
    task=T("Lee el caso inventado de Rodrigo: tiene 8 de 20 en vocabulario de Inglés y quiere llegar a 16 en 8 semanas. Escribe tres metas progresivas (semana 3, 6 y 8), una línea de acción y cómo monitoreará su avance.", "Metas: semana 3, 11 de 20; semana 6, 14 de 20; semana 8, 16 de 20. Línea: estudiar 10 palabras nuevas por semana en tarjetas. Monitoreo: anotar el puntaje de una mini prueba cada semana.", ["escribe tres metas progresivas", "incluye una línea de acción", "incluye un monitoreo", "no cuenta nada personal"], ["texto escrito"], ["metas vagas", "sin monitoreo"], "Reconoce las metas y pregunta cuál sería la primera acción."),
    reinforce="Divide una meta grande en tres metas progresivas con fecha.",
    extend="Explica por qué las metas progresivas ayudan a no desanimarse.",
)

lesson(
    OA10, 2,
    "Una hoja y un lápiz. El registro de estudio de Valentina, una estudiante inventada, está escrito en los ejercicios.",
    "Aprenderé a monitorear mi avance con datos, a distinguir hechos de emociones y a poner límites para no sobrecargarme. Sirve para ajustar a tiempo y cuidar mi bienestar.",
    ["Sé que una meta progresiva tiene monitoreo.", "Sé separar hechos, emociones e interpretaciones."],
    [
        "Monitorear es mirar cuánto avanzas con datos concretos. Un buen registro anota la fecha, lo que hiciste y el resultado, por ejemplo «lunes: 20 minutos; 6 de 10 ejercicios bien». Con varios datos puedes ver si vas mejorando o si te estancaste. Un dato es un hecho que se puede comprobar; una impresión como «siento que estoy peor» necesita contrastarse con los datos.",
        "Los resultados despiertan emociones: alegría si avanzas, desánimo si retrocedes. Reconócelas, pero no las confundas con los hechos. Por ejemplo, tras una semana difícil puedes pensar «no sirvo». El registro puede mostrar que subiste de 4 a 7 ejercicios correctos en dos semanas, y que esa semana fue más baja porque dormiste poco. Entender la causa te permite corregirla.",
        "También hay límites. No conviene llenar el horario de estudio sin descanso. Debes respetar tu sueño, tu comida, tu tiempo libre y tu familia, y tienes derecho a descansar. Una meta que te agota no es una buena meta. Si el monitoreo muestra que no alcanzas los resultados, cambia el método o pide ayuda antes de aumentar horas sin pausa.",
    ],
    [("registro", "anotación de fecha, lo hecho y el resultado"), ("dato", "hecho que se puede comprobar"), ("estancarse", "dejar de avanzar"), ("causa", "razón por la que algo ocurre"), ("sobrecarga", "tener más trabajo del que se puede hacer sin agotarse")],
    [
        W("Leer un registro", "Registro de Valentina: lunes 4 ejercicios; martes 5; miércoles 7. ¿Está mejorando?", ["Los números suben.", "4, 5 y 7 aumentan.", "Sí, mejora."], "Sí, sube de 4 a 7 ejercicios"),
        W("Separar emoción y hecho", "Valentina piensa: «Esta semana me fue mal, no sirvo». El registro muestra que durmió solo 5 horas dos noches. ¿Qué hecho explica el bajo resultado?", ["Dormir poco afecta la atención.", "Es un hecho que puede corregir.", "El hecho es que durmió poco."], "Que durmió solo 5 horas dos noches"),
    ],
    [
        M("Pensar que mi impresión basta para saber si avanzo.", "Se ignoran los datos.", "Anota resultados y compara."),
        M("Creer que estudiar más horas sin descanso siempre mejora.", "Se confunde cantidad con calidad.", "Respeta el descanso y revisa el método."),
    ],
    R=[
        ex("Anotar la fecha y el resultado de cada día, ¿es un registro, sí o no?", "Sí", "Esa es la definición."),
        ex("«Siento que estoy peor», ¿es un dato o una impresión?", "Una impresión", "Se contrasta con datos."),
        ex("¿Tienes derecho a descansar mientras estudias, sí o no?", "Sí", "El descanso es parte del bienestar."),
    ],
    U=[
        ex("¿Por qué conviene contrastar mi impresión con datos?", "Porque las impresiones pueden engañar", "Los datos muestran lo real."),
        ex("¿Por qué entender la causa de un mal resultado ayuda?", "Porque permite corregirla", "Se actúa sobre la razón."),
        ex("¿Una meta que me agota es una buena meta, sí o no?", "No", "Debe ser posible y cuidar mi bienestar."),
    ],
    A=[
        ex("Registro: semana 1, 3 de 10; semana 2, 5 de 10; semana 3, 4 de 10; semana 4, 7 de 10. ¿En qué semana bajó el resultado?", "En la semana 3", "Pasó de 5 a 4."),
        ex("Valentina tiene sueño en clases y estudia hasta las 23 h. Opciones: A) Estudiar menos tarde y dormir más. B) Estudiar hasta más tarde.", "A", "El descanso mejora la atención."),
        ex("Un estudiante dice: «Mi meta es estudiar 6 horas diarias». ¿Qué problema hay?", "Que puede sobrecargar y quitar descanso", "Una meta debe ser posible."),
    ],
    Z=[
        ex("Camilo dice: «Mejoré 2 puntos; no es nada». ¿Qué opinas?", "Que cada avance cuenta y muestra progreso", "Los pasos pequeños suman."),
        ex("¿Por qué el descanso es parte de una buena gestión del aprendizaje?", "Porque sin descanso baja la atención", "El cerebro necesita pausas para aprender."),
    ],
    D=[
        arith("Valentina pasó de 4 ejercicios correctos a 9 en cuatro semanas. ¿Cuántos ejercicios mejoró en total?", "9-4", "Se resta el inicial al final."),
        ex("Valentina dice que su meta es estudiar 6 horas diarias y que así subirá más rápido. Su registro muestra que con 1 hora diaria ya subió de 4 a 9. ¿Qué dato apoya mantener el ritmo actual?", "Que ya sube con 1 hora diaria", "Los datos muestran que el método actual funciona; más horas podrían sobrecargarla."),
    ],
    context=[ex("Un curso lleva un registro de lectura: semana 1, 20 páginas; semana 2, 25; semana 3, 22. ¿En qué semana bajó la lectura?", "En la semana 3", "Pasó de 25 a 22 páginas.")],
    selfcheck=[ex("En Orientación: ¿un registro anota fecha, lo hecho y el resultado?", "Sí", "Así permite monitorear el avance."), ex("¿Una impresión es un dato?", "No", "No se puede comprobar."), ex("¿Puedo descansar sin culpa?", "Sí", "Es parte del bienestar.")],
    task=T("Lee el registro inventado de Esteban: lunes 3 de 10, martes 4 de 10, miércoles 6 de 10, jueves 5 de 10, viernes 8 de 10. Dice: «Esta semana me fue mal». Escribe qué muestran los datos, qué día bajó, una causa posible y un ajuste que no lo sobrecargue.", "Los datos muestran avance: de 3 a 8. Bajó el jueves (de 6 a 5). Causa posible: durmió poco. Ajuste: dormir a su hora y repasar 15 minutos más.", ["lee el registro", "identifica el día que bajó", "propone una causa", "propone un ajuste sin sobrecarga"], ["texto escrito"], ["usar solo la impresión", "proponer más horas sin pausa"], "Reconoce el análisis y pregunta qué dato le gustaría tener además."),
    reinforce="Crea un registro de 5 días para una meta inventada.",
    extend="Explica por qué conviene mirar los datos antes de decir que algo no funciona.",
)

lesson(
    OA10, 3,
    "Una hoja y un lápiz. El caso de Gabriel, un estudiante inventado, y las estrategias de estudio están escritos en los ejercicios.",
    "Aprenderé a comparar líneas de acción para estudiar y a anticipar cuál ayuda más a lograr mi meta. Sirve para elegir métodos que funcionan y evitar los que parecen cómodos pero rinden poco.",
    ["Sé monitorear mi avance con datos.", "Sé que cada decisión tiene consecuencias."],
    [
        "Hay distintas estrategias para estudiar, y no todas rinden igual. Releer el cuaderno una y otra vez es cómodo, pero suele dar la impresión de saber sin que se aprenda de verdad. Hacer preguntas y responderlas sin mirar es más efectivo, porque obliga a recordar. Estudiar un rato todos los días, con pausas, rinde más que estudiar muchas horas el día anterior a la prueba. Explicar a otro lo que aprendiste también ayuda, porque descubres lo que no entiendes.",
        "Para comparar líneas de acción, evalúa cuatro cosas: cuánto tiempo toma, si exige recordar sin mirar, si se puede repetir varias veces en la semana y si tiene un resultado visible. Por ejemplo, Gabriel debe aprender 20 palabras de Inglés. Opción A: leer la lista cinco veces. Opción B: hacer tarjetas y practicar cada día con autoevaluación. La B exige recordar y se puede repetir, por eso suele funcionar mejor.",
        "También importan las condiciones: un lugar tranquilo, el celular lejos, los materiales a mano. Y cuida la honestidad: copiar o pedir que otro haga tu trabajo no te enseña y te perjudica a ti. Elegir bien la estrategia es parte de gestionar tu aprendizaje de forma autónoma.",
    ],
    [("estrategia", "forma de hacer algo para lograr una meta"), ("autoevaluación", "preguntarme y responder sin mirar para ver si aprendí"), ("distribuido", "repartido en varios días"), ("condiciones", "lugar y materiales que facilitan estudiar"), ("honestidad", "actuar con verdad y sin copiar")],
    [
        W("Comparar estrategias", "Gabriel debe aprender 20 palabras. A) Leer la lista cinco veces. B) Hacer tarjetas y practicar cada día sin mirar. ¿Cuál exige recordar?", ["En B debe responder sin mirar.", "En A solo lee.", "B exige recordar."], "B: tarjetas con práctica diaria"),
        W("Elegir distribuido", "La prueba es el viernes. Gabriel puede estudiar 3 horas el jueves o 40 minutos desde el lunes. ¿Cuál suele rendir más?", ["Repartir permite repasar varias veces.", "Una sesión larga cansa.", "La segunda rinde más."], "Estudiar 40 minutos desde el lunes"),
    ],
    [
        M("Pensar que releer muchas veces es lo mismo que aprender.", "Se confunde familiaridad con dominio.", "Practica recordando sin mirar."),
        M("Creer que copiar me ahorra tiempo.", "Se ve el resultado y no el aprendizaje.", "Copiar no enseña y puede traer sanciones."),
    ],
    R=[
        ex("Responder preguntas sin mirar, ¿exige recordar, sí o no?", "Sí", "Obliga a traer la información de la memoria."),
        ex("Estudiar un rato cada día, ¿es una estrategia distribuida, sí o no?", "Sí", "Reparte el estudio en varios días."),
        ex("Copiar la tarea de otro, ¿ayuda a aprender, sí o no?", "No", "No practicas lo que debes aprender."),
    ],
    U=[
        ex("¿Por qué releer puede dar una falsa sensación de saber?", "Porque se reconoce lo leído sin recordarlo", "No se prueba si se puede recordar."),
        ex("¿Por qué explicar a otro lo aprendido ayuda?", "Porque muestra lo que aún no entiendo", "Aparecen los vacíos."),
        ex("¿Qué condiciones ayudan a estudiar: un lugar tranquilo o el celular al lado?", "Un lugar tranquilo", "Se evitan distracciones."),
    ],
    A=[
        ex("Estrategias: 1) leer la lista; 2) tarjetas con autoevaluación; 3) explicar a un compañero; 4) copiar. ¿Cuántas ayudan a aprender?", "2", "Las estrategias 2 y 3 exigen recordar y explicar."),
        ex("Gabriel tiene 4 días antes de otra prueba y 24 palabras. Opciones: A) Aprender 6 palabras por día. B) Aprender las 24 la noche anterior.", "A", "Distribuir facilita recordar."),
        ex("Un amigo le ofrece pasarle su tarea resuelta. ¿Qué elige Gabriel?", "Rechazarla y hacerla él mismo", "Copiar no enseña y es deshonesto."),
    ],
    Z=[
        ex("Bruno dice: «Si estudio toda la noche antes de la prueba, igual me va bien». ¿Qué problema hay?", "Cansancio y poca retención", "Una sesión larga rinde menos que estudiar repartido."),
        ex("¿Por qué una estrategia útil para una persona puede no serlo para otra?", "Porque cada persona aprende distinto", "Hay que probar y revisar con datos."),
    ],
    D=[
        arith("Gabriel aprende 5 palabras por día durante 4 días. ¿Cuántas palabras aprende?", "5*4", "Se multiplican palabras por días."),
        arith("De 24 palabras, ya sabe 15. ¿Cuántas le faltan?", "24-15", "Se restan las sabidas del total."),
    ],
    context=[ex("Valeria dice que estudia con la tele prendida porque «no le molesta». Su registro muestra que recuerda poco. ¿Qué cambio de condiciones puede probar?", "Estudiar en un lugar sin televisión", "Se reducen las distracciones.")],
    selfcheck=[ex("En Orientación: ¿recordar sin mirar ayuda a aprender?", "Sí", "Fortalece la memoria."), ex("¿Estudiar repartido rinde más que hacerlo todo el día anterior?", "Sí", "Permite repasar varias veces."), ex("¿Copiar es una estrategia válida?", "No", "No enseña y es deshonesto.")],
    task=T("Lee el caso inventado de Daniela: debe aprender 18 fechas para una prueba en 6 días. Compara dos líneas de acción: leer todo el último día, o aprender 3 fechas por día con autoevaluación. Escribe la ventaja y el límite de cada una, elige y explica cómo monitoreará su avance.", "Leer el último día: rápido pero poca retención. Tres fechas por día: más repetición y recuerdo. Elige la segunda. Monitoreo: anotar cuántas recordó sin mirar cada día.", ["compara las dos líneas de acción", "elige y justifica", "incluye cómo monitorear", "no cuenta nada personal"], ["texto escrito"], ["elegir copiar", "no monitorear"], "Reconoce la comparación y pregunta qué haría si un día no cumple."),
    reinforce="Escribe dos estrategias para aprender vocabulario y compara cuál exige recordar.",
    extend="Explica por qué la autoevaluación sirve para monitorear el aprendizaje.",
)

lesson(
    OA10, 4,
    "Una hoja y un lápiz. El caso de Paula, una estudiante inventada, con su registro de avances, está escrito en los ejercicios.",
    "Aprenderé a redefinir mi meta o mis acciones cuando no resultan, y a elegir una acción segura que cuide mi bienestar. Sirve para seguir aprendiendo sin culparme ni abandonar.",
    ["Sé comparar líneas de acción.", "Sé monitorear mi avance con datos."],
    [
        "Redefinir significa cambiar la meta o la línea de acción cuando el monitoreo muestra que no funcionan. Primero, mira los datos: ¿cuánto avanzaste y qué quedó pendiente? Segundo, busca la causa: poco tiempo, un método que no sirve, falta de apoyo o una meta demasiado alta. Tercero, ajusta una sola cosa a la vez, para saber si funcionó. Por ejemplo, si la meta era 12 ejercicios y llegaste a 8, puedes mantener la meta y agregar 10 minutos al día, o bajar a 10 por un tiempo.",
        "No es útil culparte. «Soy malo» no corrige nada; «me faltó repasar a la hora» sí. Tampoco conviene abandonar ante el primer problema. Redefinir es una señal de autonomía, no de debilidad. Pide ayuda cuando los ajustes no bastan o cuando el desánimo dura mucho tiempo.",
        "Una acción segura incluye cuidar tu bienestar. Si estudias hasta muy tarde, te sientes muy ansioso o tienes ganas de abandonar todo, conversa con una persona adulta de confianza o con la orientadora. Tu salud emocional y tu descanso importan tanto como tus notas. Si alguna vez piensas en hacerte daño, avísale de inmediato a un adulto; también puedes llamar gratis al Fono Niños 147.",
    ],
    [("redefinir", "cambiar la meta o la línea de acción"), ("pendiente", "lo que falta por lograr"), ("culparse", "echarse la culpa de forma dura"), ("ajuste", "cambio pequeño y concreto"), ("bienestar emocional", "estar tranquilo y con ánimo")],
    [
        W("Redefinir con datos", "Paula quería resolver 12 ejercicios y llegó a 8. ¿Qué ajuste puede hacer?", ["Mantiene la meta y agrega tiempo.", "O baja temporalmente la meta.", "Cambia una sola cosa."], "Agregar 10 minutos diarios o bajar la meta a 10 por un tiempo"),
        W("Evitar la culpa", "Paula piensa: «Soy mala». ¿Qué frase la ayuda más: «Me faltó repasar a la hora» o «Nunca aprendo»?", ["La primera describe una causa.", "La segunda es una etiqueta.", "La primera ayuda a corregir."], "«Me faltó repasar a la hora»"),
    ],
    [
        M("Cambiar varias cosas a la vez para arreglarlo rápido.", "Se pierde saber cuál funcionó.", "Cambia una cosa a la vez."),
        M("Culparme cuando no logro la meta.", "Se confunde un resultado con quien soy.", "Describe la causa y ajusta."),
    ],
    R=[
        ex("Ajustar una sola cosa a la vez, ¿ayuda a saber qué funcionó, sí o no?", "Sí", "Permite comparar antes y después."),
        ex("Culparme con dureza, ¿ayuda a mejorar, sí o no?", "No", "No corrige la causa."),
        ex("Pedir ayuda cuando el desánimo dura mucho, ¿es una acción segura, sí o no?", "Sí", "Cuida el bienestar."),
    ],
    U=[
        ex("¿Por qué conviene buscar la causa antes de ajustar?", "Porque el ajuste debe resolver la causa", "Si no, no mejora."),
        ex("¿Redefinir es una señal de autonomía o de debilidad?", "De autonomía", "Es gestionar el propio aprendizaje."),
        ex("¿Qué hacer si el ajuste no basta: rendirse o pedir ayuda?", "Pedir ayuda", "Otra persona puede orientar."),
    ],
    A=[
        ex("Pasos: 1) mirar datos; 2) buscar causa; 3) ajustar una cosa; 4) volver a medir. ¿Qué va después de buscar la causa?", "3", "Se hace el ajuste."),
        ex("Paula hace muchas actividades y duerme poco. Opciones: A) Reducir una actividad para descansar y estudiar mejor. B) Seguir igual y dormir menos.", "A", "El descanso mejora el aprendizaje."),
        ex("Paula siente ganas de abandonar todo desde hace dos semanas. ¿Qué acción segura corresponde?", "Conversar con un adulto de confianza o la orientadora", "Un desánimo prolongado necesita apoyo."),
    ],
    Z=[
        ex("Tomás dice: «Si cambio la meta, quedo mal». ¿Qué respondes?", "Redefinir es parte de gestionar bien", "Se ajusta a lo que aprendiste."),
        ex("¿Por qué cambiar una sola cosa permite aprender del ajuste?", "Porque se ve qué la hizo funcionar", "Si cambian varias, no se sabe cuál influyó."),
    ],
    D=[
        arith("Otra semana, Paula quería 15 ejercicios y logró 11. ¿Cuánto le faltó?", "15-11", "Se resta lo logrado a la meta."),
        arith("Si agrega 10 minutos diarios durante 5 días, ¿cuántos minutos más estudia en la semana?", "10*5", "Se multiplican minutos por días."),
    ],
    context=[ex("Un curso se propuso leer 20 páginas diarias y la mayoría solo llegó a 10. ¿Cuál es una forma razonable de redefinir?", "Bajar a 12 páginas y subir despacio", "Se ajusta la meta a un nivel alcanzable.")],
    selfcheck=[ex("En Orientación: ¿redefinir es ajustar la meta o la acción?", "Sí", "Se cambia lo que no funcionó."), ex("¿Debo culparme con dureza?", "No", "La culpa dura no corrige nada."), ex("¿Puedo pedir ayuda si me siento muy ansioso?", "Sí", "Es una acción segura.")],
    task=T("Lee el caso inventado de Rodrigo: su meta era leer 25 páginas por día y llegó a 14. Escribe qué dicen los datos, una causa posible, un ajuste de una sola cosa y una acción de cuidado de su bienestar.", "Datos: llegó a 14 de 25. Causa: la meta es muy alta. Ajuste: bajar a 15 páginas y subir cada semana. Bienestar: dormir sus horas y avisar a un adulto si se siente muy agobiado.", ["lee los datos", "propone una causa", "propone un ajuste", "incluye bienestar"], ["texto escrito"], ["culparse", "cambiar todo a la vez"], "Reconoce el análisis y pregunta cuándo volvería a medir."),
    reinforce="Escribe un ajuste para una meta que no se logró de un personaje de cuento.",
    extend="Explica por qué cuidar el descanso es parte de una buena gestión del aprendizaje.",
)

lesson(
    OA10, 5,
    "Una hoja y un lápiz. El mensaje de ayuda de Camila, una estudiante inventada, y la lista de apoyos del colegio están escritos en los ejercicios.",
    "Aprenderé a pedir ayuda con claridad a profesores, compañeros y familia, y a ofrecer ayuda a otros. Sirve para recibir apoyo a tiempo y aprender en comunidad.",
    ["Sé redefinir metas y acciones.", "Sé hablar con mensajes yo."],
    [
        "Pedir ayuda es una habilidad del aprendizaje autónomo. Para hacerlo bien, prepara tu pedido. Primero, di lo que intentaste: «Estudié las fracciones con ejemplos». Segundo, di dónde te trabaste: «No entiendo cuando los denominadores son distintos». Tercero, di qué necesitas: «¿Puede mostrarme un ejemplo paso a paso?». Con esa información, la otra persona sabe cómo ayudarte.",
        "En el colegio hay distintos apoyos: el profesor de la asignatura, que puede explicar de otra forma; el profesor jefe, que orienta tu organización; orientación, que ayuda con el bienestar y la motivación; un compañero tutor, que explica entre pares, y la biblioteca, con materiales. En casa, alguien de tu familia puede ayudarte a organizar horarios, aunque no sepa el contenido.",
        "También puedes ayudar. Explicar a un compañero lo que entendiste fortalece tu aprendizaje y el suyo. Pero ayudar no es hacerle la tarea: es mostrar el camino. Cuando agradezcas la ayuda y compartas tus avances, se fortalece una comunidad de aprendizaje en el curso.",
    ],
    [("pedir ayuda", "contar qué necesito para recibir apoyo"), ("tutor", "compañero que explica a otro lo que sabe"), ("pregunta concreta", "pregunta que dice exactamente qué no entiendo"), ("comunidad de aprendizaje", "grupo que aprende junto y se apoya"), ("mostrar el camino", "explicar cómo se llega a la respuesta")],
    [
        W("Armar el pedido", "Camila no entiende fracciones con denominadores distintos. Redacta su pedido a la profesora con las tres partes.", ["Qué intentó: estudió con ejemplos.", "Dónde se trabó: denominadores distintos.", "Qué necesita: un ejemplo paso a paso."], "«Estudié con ejemplos; no entiendo cuando los denominadores son distintos; ¿puede mostrarme un ejemplo paso a paso?»"),
        W("Ayudar sin hacer la tarea", "Un compañero le pide a Camila que le pase su tarea resuelta. ¿Qué hace?", ["Pasarla no le enseña.", "Puede explicarle cómo resolverla.", "Muestra el camino."], "Explicarle cómo resolverla sin pasarle la tarea"),
    ],
    [
        M("Decir solo «no entiendo nada» al pedir ayuda.", "Es una frase muy general.", "Di dónde te trabaste y qué necesitas."),
        M("Creer que ayudar es pasar mi tarea.", "Se confunde ayudar con hacer por el otro.", "Ayuda mostrando el camino."),
    ],
    R=[
        ex("Una pregunta concreta, ¿dice exactamente qué no entiendes, sí o no?", "Sí", "Así es más fácil ayudar."),
        ex("Un compañero tutor, ¿explica entre pares, sí o no?", "Sí", "Ayuda a aprender."),
        ex("Pasar mi tarea resuelta, ¿es mostrar el camino, sí o no?", "No", "No enseña cómo se resuelve."),
    ],
    U=[
        ex("¿Por qué conviene decir lo que intentaste antes de pedir ayuda?", "Porque ayuda a entender dónde estás", "La otra persona sabe cómo apoyar."),
        ex("¿Qué puede hacer orientación por tu aprendizaje: ayudar con la motivación o resolver tu prueba?", "Ayudar con la motivación", "Orienta el bienestar y la organización."),
        ex("¿Explicar a otro lo que aprendiste fortalece también tu aprendizaje, sí o no?", "Sí", "Descubres lo que aún no entiendes."),
    ],
    A=[
        ex("Pedidos: 1) «No entiendo nada»; 2) «Intenté la suma, pero no entiendo cuando los denominadores son distintos; ¿me muestra un ejemplo?»; 3) «Hágalo usted»; 4) «Estoy cansada». ¿Cuál es el pedido mejor armado?", "2", "Dice lo intentado, la dificultad y lo que necesita."),
        ex("Camila se siente muy agobiada con las pruebas. A) Conversar con la orientadora. B) Callar para no preocupar.", "A", "Es una persona que ayuda con el bienestar."),
        ex("Un compañero tutor explica a Camila, pero ella no entiende. ¿Qué hace? A) Pregunta de nuevo y dice dónde se pierde. B) Finge entender.", "A", "Decir dónde se pierde permite una mejor explicación."),
    ],
    Z=[
        ex("Gabriel dice: «Si pido ayuda, parezco tonto». ¿Qué argumento le darías?", "Pedir ayuda es parte de aprender", "Todos necesitan apoyo."),
        ex("¿Por qué agradecer la ayuda fortalece una comunidad de aprendizaje?", "Porque motiva a seguir ayudando", "El agradecimiento reconoce el esfuerzo."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 6 son tutores. Si cada uno ayuda a 3 compañeros, ¿cuántos reciben ayuda?", "6*3", "Se multiplican tutores por compañeros."),
        arith("De los 30, ¿cuántos no son tutores ni reciben ayuda de tutor?", "30-6-18", "Al total se restan tutores y ayudados."),
    ],
    context=[ex("Antes de una prueba, Pablo escribe a su profesora: «No entiendo nada». Ella le responde: «¿Qué parte, exactamente?». ¿Qué le faltó al mensaje de Pablo?", "Decir dónde se trabó y qué necesita", "Una pregunta concreta facilita la ayuda.")],
    selfcheck=[ex("En Orientación: ¿pedir ayuda es una habilidad?", "Sí", "Se aprende y se practica."), ex("¿Ayudar es hacer la tarea del otro?", "No", "Es mostrar el camino."), ex("¿Puedo agradecer la ayuda recibida?", "Sí", "Fortalece al grupo.")],
    task=T("Escribe un pedido de ayuda de tres partes para el caso inventado de Matías, que no entiende cómo hacer un resumen de un texto de Historia. Escribe además una forma de ayudar a una compañera sin hacerle la tarea y una persona del colegio a la que acudirías si te sintieras agobiado con las pruebas.", "Pedido: «Leí el texto dos veces; no sé qué ideas son las principales; ¿me muestra cómo subrayar?». Ayuda: explicarle cómo se subraya. Persona: la orientadora.", ["escribe las tres partes del pedido", "propone una ayuda que muestre el camino", "nombra a una persona del colegio", "no cuenta nada personal"], ["texto escrito"], ["pedido vago", "pasar la tarea"], "Reconoce el pedido y pregunta a quién se lo haría primero."),
    reinforce="Redacta un pedido de ayuda con tres partes para otra materia inventada.",
    extend="Explica cómo puede un compañero ayudar sin hacerte la tarea.",
)

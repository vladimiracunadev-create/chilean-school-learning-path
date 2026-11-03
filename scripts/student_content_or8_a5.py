"""Cuaderno del estudiante, 8.º básico Orientación: OA 09 (intereses, aprendizaje y proyectos personales) y OA 10 (metas progresivas y gestión autónoma del aprendizaje)."""
from __future__ import annotations

from student_content_or8_a import M, T, W, lesson
from student_lessons import arith, ex

OA9, OA10 = "OR08 OA 09", "OR08 OA 10"

# ================================================================ OA 09
lesson(
    OA9, 1,
    "Una hoja y un lápiz. El perfil de Camila, una estudiante inventada, y las frases para clasificar están escritos en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a distinguir intereses, motivaciones, necesidades y capacidades, y a ver cómo el aprendizaje escolar sistemático ayuda a desarrollarlos. Sirve para pensar mis proyectos personales.",
    ["Conozco mi autoconcepto y mis capacidades.", "Sé que aprender en el colegio es un proceso."],
    [
        "Para conocerte mejor conviene separar cuatro ideas. Los intereses son lo que te gusta y te llama la atención, como la astronomía. Las motivaciones son las razones que te mueven a actuar, como querer ayudar a otros. Las necesidades son lo que te hace falta para aprender o estar bien, como más práctica en una materia o un lugar tranquilo para estudiar. Las capacidades son lo que puedes hacer, o aprender a hacer, con práctica.",
        "El aprendizaje escolar sistemático es el que se hace de manera ordenada y progresiva, año tras año, en las asignaturas. Es relevante porque te da herramientas para explorar tus intereses y desarrollar tus capacidades. Por ejemplo, a quien le interesa construir robots le sirven matemática, ciencias y tecnología; a quien quiere contar historias le sirven lenguaje, historia y arte.",
        "Un proyecto personal es un plan para lograr algo que te importa, a corto, mediano o largo plazo. Puede ser aprender a tocar un instrumento este año, participar en un taller o estudiar una carrera en el futuro. Lo que se logra en semanas o meses es un proyecto a corto plazo; lo que toma varios años, como una carrera, es a largo plazo. Un buen proyecto parte de lo que eres hoy y se apoya en lo que el colegio te ofrece. No necesitas tener todo definido: puedes explorar, cambiar de idea y seguir aprendiendo.",
    ],
    [("interés", "lo que a una persona le gusta y le llama la atención"), ("motivación", "razón que mueve a una persona a actuar"), ("necesidad", "algo que le hace falta a una persona para aprender o estar bien"), ("capacidad", "lo que una persona puede hacer o aprender a hacer"), ("proyecto personal", "plan para lograr algo importante para una persona")],
    [
        W("Clasificar una frase", "Camila escribe: «Quiero entender cómo funcionan los robots». ¿Es interés, motivación, necesidad o capacidad?", ["Dice lo que quiere conocer.", "Habla de lo que le llama la atención.", "Es un interés."], "Un interés"),
        W("Relacionar con asignaturas", "A Camila le interesa construir un robot. ¿Qué asignaturas del colegio le sirven?", ["Para calcular medidas: matemática.", "Para entender fuerzas y circuitos: ciencias.", "Para armar y programar: tecnología."], "Matemática, ciencias y tecnología"),
    ],
    [
        M("Creer que el colegio no sirve para los intereses personales.", "Se ve el estudio como obligación sin relación.", "El aprendizaje escolar da herramientas para explorar intereses."),
        M("Pensar que un proyecto personal debe estar definido para siempre.", "Se cree que cambiar de idea es fracasar.", "Se puede explorar y ajustar el proyecto."),
    ],
    R=[
        ex("«Me gusta dibujar mapas» ¿es un interés o una necesidad?", "Un interés", "Dice lo que le gusta."),
        ex("«Necesito más práctica para resolver ecuaciones» ¿es una necesidad o una capacidad?", "Una necesidad", "Indica lo que le hace falta para aprender."),
        ex("«Quiero ayudar a mis compañeros» ¿es una motivación o un interés?", "Una motivación", "Es una razón que la mueve a actuar."),
    ],
    U=[
        ex("¿Qué es el aprendizaje escolar sistemático? A) El que se hace de forma ordenada y progresiva. B) El que se hace al azar.", "A", "Avanza año a año con orden."),
        ex("Quien quiere contar historias, ¿puede apoyarse en lenguaje y arte, sí o no?", "Sí", "Esas asignaturas ayudan a narrar y expresar."),
        ex("Un proyecto personal, ¿es un plan para lograr algo que te importa, sí o no?", "Sí", "Esa es su definición."),
    ],
    A=[
        ex("Frases de Camila: 1) «me gusta la astronomía»; 2) «quiero ayudar a otros»; 3) «necesito un lugar tranquilo para estudiar»; 4) «puedo explicar un tema a otros». ¿Cuál es la necesidad?", "La 3", "Dice lo que le hace falta."),
        ex("A Tomás le interesa cuidar el medio ambiente. ¿Qué asignatura puede ayudarlo a entender cómo funcionan los ecosistemas? A) Ciencias Naturales. B) Educación Física.", "A", "Ciencias estudia los ecosistemas."),
        ex("Estudiar una carrera después de terminar el colegio, ¿es un proyecto a corto o a largo plazo?", "A largo plazo", "Toma varios años."),
    ],
    Z=[
        ex("¿Por qué una necesidad puede convertirse en una oportunidad de aprendizaje?", "Porque al reconocerla se puede buscar cómo cubrirla", "Saber qué falta permite pedir apoyo y practicar."),
        ex("Un joven dice: «Matemática no sirve para mi interés en la música». ¿Qué le responderías?", "Que ayuda a entender ritmo, compases y proporciones", "Hay relaciones entre ambas áreas."),
    ],
    D=[
        arith("Camila anotó 20 frases sobre sí misma: 6 intereses, 5 motivaciones, 4 necesidades y el resto capacidades. ¿Cuántas capacidades anotó?", "20-6-5-4", "Al total se le restan los otros tres grupos."),
        arith("Un curso de 36 estudiantes se divide en grupos de 4 para explorar sus proyectos. ¿Cuántos grupos se forman?", "36//4", "Se divide el total entre los integrantes de cada grupo."),
    ],
    context=[ex("En Orientación, Matías dice que su interés es el fútbol y no sabe para qué le sirve estudiar. ¿Qué asignatura puede conectarse con su interés y cómo?", "Educación Física o matemática, para entender entrenamiento y estadísticas", "Hay relaciones entre su interés y el estudio.")],
    selfcheck=[ex("En Orientación: ¿una necesidad es lo que te hace falta para aprender?", "Sí", "Esa es su definición."), ex("¿El colegio ofrece herramientas para tus intereses?", "Sí", "Las asignaturas se relacionan con ellos."), ex("¿Un proyecto personal es inamovible?", "No", "Se puede ajustar.")],
    task=T("Lee el perfil de Nicolás, un estudiante inventado: le gusta el cine; quiere mostrar historias de su barrio; necesita practicar la redacción; puede editar videos con un programa básico. Escribe una tabla con interés, motivación, necesidad y capacidad, y dos asignaturas del colegio que le ayudarían a desarrollar su proyecto de un corto de cine.", "Interés: el cine. Motivación: mostrar historias del barrio. Necesidad: practicar la redacción. Capacidad: editar videos. Asignaturas: Lenguaje y Artes Visuales.", ["completa los cuatro elementos", "usa los datos del perfil", "nombra dos asignaturas relevantes", "no cuenta datos personales"], ["tabla escrita"], ["confundir interés con motivación", "no relacionar con el colegio"], "Reconoce las clasificaciones y pregunta qué otra asignatura sumaría."),
    reinforce="Escribe un interés, una motivación, una necesidad y una capacidad de un personaje de cuento.",
    extend="Explica cómo una asignatura del colegio puede ayudar a un interés personal.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. El caso de Sofía y los datos de sus logros están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a distinguir hechos de creencias sobre mis capacidades, a reconocer mi derecho a aprender y a poner límites ante presiones o estereotipos. Sirve para construir proyectos personales con confianza.",
    ["Sé separar intereses, motivaciones, necesidades y capacidades.", "Sé que el colegio ofrece herramientas."],
    [
        "Cuando piensas en tus capacidades, conviene separar los hechos de las creencias. Un hecho es un dato comprobable, como «en la última prueba respondí 14 de 20 preguntas bien». Una creencia es una idea que tienes, como «no soy bueno para matemática». Las creencias pueden ser verdaderas, pero a veces se basan en pocas experiencias. Revisar los hechos ayuda a ver si una creencia es justa.",
        "Las emociones influyen: el entusiasmo anima a probar; el miedo a fracasar puede frenar. Son normales y se pueden manejar con pequeños pasos y apoyo. Todos tienen derecho a aprender, a equivocarse y a explorar sus intereses, sin importar si son hombres o mujeres. Las ideas como «esa carrera es solo para hombres» o «eso no es para mujeres» son estereotipos que limitan.",
        "También hay límites: nadie debe presionarte para elegir por ti ni ridiculizar tus intereses. Puedes escuchar opiniones, pero la decisión sobre tu proyecto se construye con información y apoyo. Si sientes presión, puedes hablar con tu familia, tu profesor jefe o el orientador.",
    ],
    [("hecho", "dato que se puede comprobar"), ("creencia", "idea que una persona tiene sobre algo"), ("estereotipo", "idea fija y generalizada sobre un grupo de personas"), ("explorar", "probar y conocer cosas nuevas"), ("presión", "empuje de otros para que alguien elija algo")],
    [
        W("Revisar una creencia con hechos", "Sofía cree: «Soy mala en ciencias». Datos: en tres pruebas obtuvo 12, 14 y 16 de 20 puntos. ¿Los hechos apoyan la creencia?", ["Los puntajes suben.", "16 de 20 es un buen resultado.", "La creencia no es justa."], "No: sus puntajes mejoran"),
        W("Responder a un estereotipo", "Un compañero le dice a Sofía: «Ingeniería es para hombres». ¿Qué respuesta respeta su derecho a explorar?", ["Hombres y mujeres pueden estudiar ingeniería.", "Es un estereotipo.", "Sofía puede explorar lo que le interese."], "«Hombres y mujeres pueden estudiar ingeniería»"),
    ],
    [
        M("Creer que una nota baja define lo que puedes lograr.", "Se generaliza a partir de pocos hechos.", "Mira varios datos y el avance."),
        M("Aceptar un estereotipo porque «siempre fue así».", "Se confunde costumbre con regla.", "Tienes derecho a explorar tus intereses."),
    ],
    R=[
        ex("«Respondí 14 de 20 bien» ¿es un hecho o una creencia?", "Un hecho", "Se puede comprobar."),
        ex("«Soy malo para todo» ¿es un hecho o una creencia?", "Una creencia", "Es una idea sin datos."),
        ex("¿Tienes derecho a explorar tus intereses aunque sea una actividad poco habitual para tu género, sí o no?", "Sí", "Los intereses no dependen del género."),
    ],
    U=[
        ex("¿Qué ayuda a revisar una creencia? A) Mirar varios hechos. B) Repetirla más fuerte.", "A", "Los datos permiten ver si es justa."),
        ex("El miedo a fracasar, ¿es una emoción normal, sí o no?", "Sí", "Todos la sienten a veces."),
        ex("Un estereotipo, ¿es una idea fija sobre un grupo o un dato comprobado?", "Una idea fija sobre un grupo", "No se basa en cada persona."),
    ],
    A=[
        ex("Las notas de Lucas en tres pruebas fueron 5, 5 y 6 en una escala de 1 a 7. Él cree que «le va mal». ¿Cuál es el hecho más justo?", "Sus notas son buenas: 5, 5 y 6", "Los datos no apoyan la creencia."),
        ex("Una profesora dice a una alumna: «Eso es para hombres». ¿Qué principio se rompe? A) La igualdad. B) La rapidez.", "A", "Se limita su derecho por ser mujer."),
        ex("Un familiar presiona a Tomás para elegir una carrera que no le interesa. ¿Qué puede hacer primero? A) Conversar con él y pedir información al orientador. B) Obedecer sin pensar.", "A", "Busca información y apoyo para decidir."),
    ],
    Z=[
        ex("¿Por qué una sola nota baja no define tus capacidades?", "Porque hay otros resultados y puedes mejorar", "Una capacidad se desarrolla con práctica."),
        ex("¿Por qué los estereotipos limitan los proyectos de las personas?", "Porque hacen creer que algunas cosas no son para ellas", "Frenan la exploración de intereses."),
    ],
    D=[
        arith("Sofía respondió 12, 14 y 16 preguntas bien en tres pruebas de 20. ¿Cuántas preguntas bien respondió en total?", "12+14+16", "Se suman las respuestas correctas de cada prueba."),
        arith("De 20 preguntas de una prueba, Sofía respondió bien 16. ¿Cuántas respondió mal?", "20-16", "Al total se le restan las correctas."),
    ],
    context=[ex("Matilda quiere inscribirse en el taller de robótica, pero le dicen que «es de hombres». ¿Qué derecho puede recordar y a quién puede recurrir?", "Su derecho a explorar; al profesor jefe u orientador", "Puede pedir apoyo para que la acepten.")],
    selfcheck=[ex("En Orientación: ¿una creencia se revisa con hechos?", "Sí", "Los datos ayudan a ver si es justa."), ex("¿Hay carreras solo para hombres o solo para mujeres?", "No", "Todas son para todas las personas."), ex("¿Puedes hablar con el orientador si sientes presión?", "Sí", "Es una persona de apoyo.")],
    task=T("Lee el caso inventado de Ismael: cree que «no sirve para escribir» y le atrae ser periodista. Sus datos: en tres trabajos de lenguaje obtuvo 10, 13 y 16 de 20 puntos; un compañero le dijo que «periodismo es para mujeres». Escribe: la creencia, los hechos que la revisan, el estereotipo y una respuesta que defienda su derecho a explorar.", "Creencia: no sirve para escribir. Hechos: sus puntajes suben de 10 a 16. Estereotipo: periodismo es para mujeres. Respuesta: «Cualquier persona puede ser periodista».", ["distingue creencia y hechos", "identifica el estereotipo", "defiende el derecho a explorar", "usa los datos"], ["texto escrito"], ["aceptar el estereotipo", "ignorar los datos"], "Reconoce la revisión con datos y pregunta qué paso daría Ismael ahora."),
    reinforce="Escribe una creencia y los hechos que la revisan para un personaje de cuento.",
    extend="Explica por qué todas las personas tienen derecho a explorar sus intereses.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. Las tres opciones de Valentina y la tabla de horas están escritas en los ejercicios. Todo es inventado.",
    "Aprenderé a comparar opciones para desarrollar un interés y a prever sus consecuencias, mostrando cómo el estudio sistemático ayuda a un proyecto personal. Sirve para elegir caminos realistas.",
    ["Sé revisar creencias con hechos.", "Sé relacionar intereses con asignaturas."],
    [
        "Para desarrollar un interés hay varias opciones. Valentina quiere ser veterinaria. Puede (1) esperar a ver qué pasa, (2) mejorar en ciencias y matemática y leer sobre animales, o (3) dejar de estudiar y solo mirar videos. Cada opción tiene consecuencias. Esperar no avanza. Mirar solo videos entretiene, pero no desarrolla las capacidades necesarias. Estudiar de forma ordenada y practicar construye una base para su proyecto.",
        "Al comparar opciones, mira cuatro cosas: ¿se acerca a mi meta?, ¿puedo hacerla ahora con lo que tengo?, ¿cuánto tiempo requiere?, ¿qué ganó y qué dejo de hacer? Ninguna opción es perfecta: elegir una significa renunciar a otras. Una buena decisión es informada y se puede revisar más adelante.",
        "El aprendizaje escolar sistemático es valioso porque lo que aprendes en cada nivel se apoya en lo anterior. Por ejemplo, entender proporciones en matemática ayuda a interpretar tablas y gráficos en ciencias, y leer comprensivamente ayuda a estudiar cualquier tema. Sin esa base, avanzar hacia un proyecto se vuelve más difícil.",
    ],
    [("opción", "camino posible entre varios"), ("consecuencia", "efecto que sigue a una decisión"), ("sistemático", "ordenado y progresivo"), ("base", "conocimientos previos sobre los que se construye"), ("renunciar", "dejar algo para elegir otra cosa")],
    [
        W("Comparar opciones", "Valentina quiere ser veterinaria. Opción A: esperar. Opción B: estudiar ciencias y matemática y leer sobre animales. ¿Cuál se acerca más a su meta?", ["A no hace nada.", "B construye una base.", "B es la que avanza."], "La opción B"),
        W("Calcular tiempo", "Valentina dedica 3 horas a la semana a ciencias y 2 a matemática. ¿Cuántas horas semanales estudia entre ambas?", ["Suma 3 + 2.", "Da 5 horas.", "Es su tiempo de estudio dedicado."], "5 horas por semana"),
    ],
    [
        M("Pensar que mirar videos de un tema ya equivale a aprenderlo.", "Se confunde entretención con aprendizaje.", "Combina ver, leer, practicar y estudiar."),
        M("Creer que una decisión es para siempre.", "Se teme equivocarse.", "Se puede revisar y ajustar."),
    ],
    R=[
        ex("Estudiar ciencias y matemática de forma ordenada, ¿ayuda a un proyecto de veterinaria, sí o no?", "Sí", "Construye una base."),
        ex("Esperar sin hacer nada, ¿acerca a una meta, sí o no?", "No", "No avanza hacia nada."),
        ex("Elegir una opción, ¿implica renunciar a otras, sí o no?", "Sí", "No se puede hacer todo a la vez."),
    ],
    U=[
        ex("¿Por qué el estudio sistemático ayuda a un proyecto? A) Porque cada aprendizaje se apoya en el anterior. B) Porque se hace en el colegio y ya.", "A", "Los conocimientos se construyen en etapas."),
        ex("De las cuatro preguntas para comparar opciones, ¿cuál se refiere al tiempo?", "¿Cuánto tiempo requiere?", "Ayuda a planificar."),
        ex("Una decisión informada, ¿se puede revisar más adelante, sí o no?", "Sí", "Los proyectos pueden ajustarse."),
    ],
    A=[
        ex("Rodrigo quiere aprender inglés para viajar. Opciones: 1) mirar una serie sin subtítulos una vez; 2) practicar 20 minutos diarios en tareas; 3) esperar a tener 18 años. ¿Cuál se acerca más a su meta?", "La 2", "Es constante y practicable."),
        ex("Para estudiar un tema, ¿qué mezcla de acciones es mejor? A) Leer, practicar y repasar. B) Solo ver un video.", "A", "Combina varias formas de aprender."),
        ex("Camila quiere ser ilustradora. ¿Qué asignatura puede ayudarla con composición y color?", "Artes Visuales", "Trabaja esos contenidos."),
    ],
    Z=[
        ex("¿Por qué conviene estudiar de forma ordenada y no a última hora?", "Porque lo aprendido se asienta y se apoya en lo anterior", "El aprendizaje progresivo es más sólido."),
        ex("Un joven dice: «Si solo veo videos, aprendo igual». ¿Qué falta?", "Practicar y comprobar lo aprendido", "Practicar ayuda a retener y aplicar."),
    ],
    D=[
        arith("Valentina estudia 2 horas de ciencias y 3 de matemática por semana. En 4 semanas, ¿cuántas horas estudia en total?", "(2+3)*4", "Se suman las horas semanales y se multiplican por las semanas."),
        arith("Un plan de 30 horas se reparte en 6 semanas por igual. ¿Cuántas horas por semana son?", "30//6", "Se divide el total entre las semanas."),
    ],
    context=[ex("A Matías le interesa ser programador. Tiene dos opciones: practicar matemática y lógica 3 veces por semana o ver tutoriales sin practicar. ¿Cuál lo acerca más a su meta y por qué?", "Practicar, porque desarrolla capacidades", "La práctica constante construye habilidades.")],
    selfcheck=[ex("En Orientación: ¿elegir una opción implica renunciar a otras?", "Sí", "No se puede todo a la vez."), ex("¿El estudio ordenado construye una base?", "Sí", "Cada aprendizaje se apoya en otro."), ex("¿Una decisión puede revisarse?", "Sí", "Los proyectos se ajustan.")],
    task=T("Lee el caso inventado de Bruno: quiere ser chef. Tiene tres opciones: (1) ver videos de cocina; (2) estudiar matemática para medidas y proporciones, ciencias para entender alimentos y practicar una receta simple cada semana; (3) esperar a ser mayor. Haz una tabla con cada opción: qué gana, qué deja de hacer y cuánto se acerca a su meta. Elige una y justifica con tu lectura del aprendizaje escolar.", "(1) Gana entretención; no desarrolla capacidades. (2) Gana base y práctica; requiere tiempo. (3) No avanza. Elijo la 2 porque matemática y ciencias aportan a proporciones y a entender alimentos.", ["compara las tres opciones", "anota qué gana y qué deja", "elige una y justifica", "relaciona asignaturas con la meta"], ["tabla escrita"], ["ver solo entretención", "no considerar el tiempo"], "Reconoce la comparación y pregunta cómo organizará su semana."),
    reinforce="Escribe dos opciones para desarrollar un interés y una consecuencia de cada una.",
    extend="Explica por qué lo que se aprende en el colegio se apoya en lo anterior.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. El proyecto de Emilia, la ficha y la lista de fuentes de apoyo están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a elegir un proyecto personal realista a corto plazo, con pasos, apoyo y fuentes confiables. Sirve para empezar a construir mi proyecto sin presiones y con información.",
    ["Sé comparar opciones y consecuencias.", "Sé que el estudio sistemático ayuda a mis proyectos."],
    [
        "Elegir un proyecto personal es decidir qué quieres lograr y cómo. Un proyecto realista a corto plazo cumple cinco condiciones: es de tu interés, es posible con lo que tienes, tiene pasos concretos, tiene un plazo y cuenta con apoyo. Por ejemplo: «Aprender a hacer un huerto en macetas en dos meses, con ayuda de una persona de mi casa y un libro de la biblioteca».",
        "Para decidir con información usa fuentes confiables: el orientador del colegio, tus profesores, libros de la biblioteca, sitios oficiales del Ministerio de Educación y personas que trabajan en lo que te interesa. Evita decidir solo por lo que se ve en redes sociales. Recuerda que puedes cambiar: un proyecto es una guía y no una condena.",
        "Para elegir con seguridad, evita proyectos que te pongan en riesgo, que dependan de que otros te presionen o que te lleven a descuidar tu salud y tus estudios. Si dudas, consulta a una persona adulta de confianza. Un buen proyecto cuida tu bienestar mientras te acerca a lo que te importa.",
    ],
    [("realista", "que se puede lograr con lo que se tiene"), ("paso concreto", "acción clara que se puede hacer"), ("plazo", "tiempo para lograr algo"), ("apoyo", "ayuda de personas o recursos"), ("fuente confiable", "persona o texto con información comprobable")],
    [
        W("Evaluar un proyecto", "Emilia propone: «Aprender a hacer un huerto en macetas en dos meses, con ayuda de una persona de mi casa». ¿Cumple las cinco condiciones?", ["Es su interés.", "Es posible, con un plazo y con apoyo.", "Tiene un paso concreto: hacer el huerto."], "Sí, cumple las cinco condiciones"),
        W("Detectar un proyecto poco realista", "Otro proyecto dice: «Ser famoso en un mes». ¿Es realista?", ["No tiene pasos concretos.", "El plazo es demasiado corto.", "No depende solo de ella."], "No: es poco realista"),
    ],
    [
        M("Elegir un proyecto solo porque está de moda.", "Se decide por lo que hacen otros.", "Elige por tus intereses y posibilidades."),
        M("Pensar que si eliges algo no podrás cambiar.", "Se ve el proyecto como obligación.", "Un proyecto puede ajustarse."),
    ],
    R=[
        ex("Un proyecto realista, ¿se puede lograr con lo que se tiene, sí o no?", "Sí", "Esa es su característica."),
        ex("El orientador, ¿es una fuente confiable para decidir, sí o no?", "Sí", "Tiene formación para orientar."),
        ex("Un proyecto que te pone en riesgo, ¿es adecuado, sí o no?", "No", "Debe cuidar tu bienestar."),
    ],
    U=[
        ex("¿Qué debe tener un proyecto a corto plazo? A) Pasos concretos y un plazo. B) Un sueño sin fecha.", "A", "Eso permite avanzar."),
        ex("¿Dónde conviene buscar información: en el orientador o en un rumor?", "En el orientador", "Es una fuente confiable."),
        ex("¿Un proyecto puede cambiar con el tiempo, sí o no?", "Sí", "Es una guía que se ajusta."),
    ],
    A=[
        ex("Cuatro proyectos: 1) aprender a tocar una canción simple en guitarra en dos meses con clases; 2) ser campeón mundial en un mes; 3) leer 6 libros en el año con ayuda de la biblioteca; 4) dejar el colegio para ser famoso. ¿Cuáles son realistas?", "1 y 3", "Tienen pasos, plazo y apoyo."),
        ex("Ema quiere aprender a programar. ¿Qué apoyo adecuado puede buscar? A) Un taller del colegio o un libro de la biblioteca. B) Un desconocido por internet que le ofrece clases privadas.", "A", "Son fuentes confiables y seguras."),
        ex("El proyecto de Pablo exige estudiar 8 horas diarias y dormir 4. ¿Es adecuado, sí o no?", "No", "Pone en riesgo su salud."),
    ],
    Z=[
        ex("¿Por qué conviene tener apoyo de otras personas en un proyecto?", "Porque ayudan a orientar, a corregir y a motivar", "Otros aportan información y ánimo."),
        ex("¿Por qué decidir solo por lo que se ve en redes puede ser un error?", "Porque muestra una parte y no siempre es real", "No todo lo que se ve es confiable."),
    ],
    D=[
        arith("El proyecto de Emilia dura 8 semanas y dedica 3 horas por semana. ¿Cuántas horas dedica en total?", "8*3", "Se multiplican las semanas por las horas."),
        arith("En un taller de orientación vocacional, 40 estudiantes eligieron: huerto 12, música 15, deporte 8 y el resto robótica. ¿Cuántos eligieron robótica?", "40-12-15-8", "Al total se le restan los otros grupos."),
    ],
    context=[ex("Gabriela quiere probar un taller de teatro, pero su amiga le dice que «no sirve para nada». ¿Qué fuente confiable puede consultar y qué decisión le conviene?", "Al orientador, y probar el taller antes de decidir", "Una fuente confiable y la experiencia directa ayudan a elegir.")],
    selfcheck=[ex("En Orientación: ¿un proyecto necesita pasos y plazo?", "Sí", "Eso permite avanzar."), ex("¿Se puede cambiar de proyecto?", "Sí", "Es una guía."), ex("¿Se decide solo por lo que se ve en redes?", "No", "Se necesita información confiable.")],
    task=T("Lee los datos del caso inventado de Joaquín: le gusta la fotografía; el colegio tiene un taller los jueves; en la biblioteca hay un libro de fotografía básica; tiene un celular con cámara. Diseña un proyecto a corto plazo de seis semanas con: objetivo, tres pasos concretos, apoyo, fuentes confiables y plazo.", "Objetivo: tomar y presentar 10 fotos del barrio en seis semanas. Pasos: ir al taller los jueves; leer un capítulo semanal; sacar 2 fotos por semana. Apoyo: profesor del taller. Fuentes: libro de la biblioteca. Plazo: seis semanas.", ["objetivo claro", "tres pasos concretos", "apoyo y fuentes confiables", "plazo y datos del caso"], ["ficha del proyecto"], ["proyecto sin plazo", "fuentes dudosas"], "Reconoce la ficha y pregunta cómo sabrá si va bien."),
    reinforce="Escribe un proyecto de dos meses con pasos y apoyo para un personaje de cuento.",
    extend="Explica por qué un proyecto personal debe cuidar tu bienestar.",
)

# ================================================================ OA 10
lesson(
    OA10, 1,
    "Una hoja y un lápiz. El caso de Rodrigo, un estudiante inventado, y los resultados de sus prácticas están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a distinguir un deseo de una meta, a formular metas progresivas y a identificar sus partes: línea de acción, monitoreo y redefinición. Sirve para gestionar mi propio aprendizaje.",
    ["Sé qué es un proyecto personal.", "Sé que el aprendizaje se construye por etapas."],
    [
        "Un deseo es algo que quieres, como «ojalá me vaya mejor en matemática». Una meta es un deseo convertido en un objetivo claro: específico, medible y con plazo. Por ejemplo: «Pasar de 12 a 16 respuestas correctas de 20 en la práctica de matemática en seis semanas». Una meta clara te dice qué quieres, cuánto y para cuándo.",
        "Las metas progresivas son escalones: metas pequeñas que te llevan a una meta mayor. Por ejemplo, de 12 a 14 en dos semanas, luego a 15 y luego a 16. Subir de a poco es más realista y motiva al ver avances. Gestionar de manera autónoma tu aprendizaje significa conducirlo tú: fijar la meta, elegir las acciones, mirar los resultados y ajustar el plan.",
        "El ciclo tiene cuatro pasos: establecer la meta, definir las líneas de acción (qué harás: por ejemplo, practicar 20 minutos diarios), monitorear los logros (anotar los resultados) y redefinir las acciones si no resultan. Este ciclo no es un castigo: es una forma de aprender a aprender.",
    ],
    [("deseo", "algo que se quiere sin un plan claro"), ("meta", "objetivo claro, medible y con plazo"), ("meta progresiva", "meta pequeña que forma parte de una meta mayor"), ("línea de acción", "lo que haré para lograr una meta"), ("monitorear", "revisar los resultados para ver si se avanza")],
    [
        W("Convertir un deseo en meta", "Rodrigo desea «mejorar en matemática». Su práctica actual: 12 de 20 correctas. ¿Cómo lo convierte en meta?", ["Dice cuánto quiere lograr: 16 de 20.", "Dice cuándo: en seis semanas.", "Es medible y con plazo."], "«Llegar a 16 de 20 en seis semanas»"),
        W("Armar metas progresivas", "De 12 a 16 en seis semanas. Propón escalones.", ["De 12 a 14 en dos semanas.", "De 14 a 15 en cuatro semanas.", "De 15 a 16 en seis semanas."], "12 a 14, luego 15 y luego 16"),
    ],
    [
        M("Creer que una meta es lo mismo que un deseo.", "Se piensa que querer basta.", "Una meta es clara, medible y con plazo."),
        M("Fijar una meta enorme sin escalones.", "Se quiere llegar de golpe.", "Divide la meta en pasos pequeños."),
    ],
    R=[
        ex("«Ojalá me vaya mejor» ¿es un deseo o una meta?", "Un deseo", "No tiene cantidad ni plazo."),
        ex("«Llegar a 16 de 20 en seis semanas» ¿es una meta clara, sí o no?", "Sí", "Tiene cantidad y plazo."),
        ex("Una línea de acción, ¿es lo que haré para lograr la meta, sí o no?", "Sí", "Esa es su definición."),
    ],
    U=[
        ex("¿Para qué sirven las metas progresivas? A) Para avanzar por escalones. B) Para llegar de golpe a la meta mayor.", "A", "Dividen una meta grande en pasos."),
        ex("Monitorear es: ¿revisar los resultados o ignorarlos?", "Revisar los resultados", "Permite saber si se avanza."),
        ex("Gestionar autónomamente el aprendizaje, ¿significa conducirlo tú, sí o no?", "Sí", "Tú fijas, actúas, revisas y ajustas."),
    ],
    A=[
        ex("Cuatro frases: 1) «Quiero ser mejor»; 2) «Quiero leer 5 libros en 10 semanas»; 3) «Ojalá me vaya bien»; 4) «Quiero pasar de 10 a 15 respuestas correctas en un mes». ¿Cuáles son metas claras?", "2 y 4", "Tienen cantidad y plazo."),
        ex("Rodrigo anota sus resultados cada semana en una tabla. ¿Qué paso del ciclo cumple? A) Monitorear. B) Establecer el deseo.", "A", "Revisa sus logros."),
        ex("Meta: pasar de 8 a 14 palabras correctas de inglés en una prueba. ¿Qué escalón intermedio sirve? A) Llegar a 11. B) Llegar a 20.", "A", "Es un paso intermedio realista."),
    ],
    Z=[
        ex("¿Por qué las metas pequeñas motivan?", "Porque se ven avances y se logran más rápido", "Los logros frecuentes dan confianza."),
        ex("¿Por qué una meta sin plazo es débil?", "Porque no se sabe cuándo revisar si se cumplió", "El plazo permite monitorear."),
    ],
    D=[
        arith("Rodrigo quiere pasar de 12 a 16 respuestas correctas. ¿Cuántas debe mejorar en total?", "16-12", "Se resta lo actual de lo que quiere lograr."),
        arith("Si mejora 1 respuesta cada 2 semanas, ¿en cuántas semanas llegará de 12 a 16?", "(16-12)*2", "Debe mejorar 4 respuestas y cada una toma 2 semanas."),
    ],
    context=[ex("Valeria dice: «Voy a estudiar más». ¿Cómo puede convertirlo en una meta clara en lenguaje?", "«Leer y resumir 3 textos por semana durante un mes»", "Tiene cantidad y plazo.")],
    selfcheck=[ex("En Orientación: ¿una meta tiene cantidad y plazo?", "Sí", "Es una meta medible."), ex("¿Las metas progresivas son escalones?", "Sí", "Dividen una meta mayor."), ex("¿Se puede ajustar el plan?", "Sí", "Se redefinen las acciones.")],
    task=T("Lee el caso inventado de Ana: desea «mejorar en inglés». Hoy responde bien 8 de 20 preguntas de vocabulario. Convierte su deseo en una meta clara para cuatro semanas y escribe tres metas progresivas, una línea de acción y cómo monitoreará sus resultados.", "Meta: llegar a 14 de 20 en cuatro semanas. Progresivas: 10 en la semana 1, 12 en la 2 y 14 en la 4. Acción: practicar 15 minutos diarios. Monitoreo: anotar el resultado de una prueba corta cada viernes.", ["meta con cantidad y plazo", "tres escalones", "línea de acción y monitoreo", "usa los datos del caso"], ["texto o tabla"], ["meta vaga", "sin monitoreo"], "Reconoce los escalones y pregunta cómo ajustaría el plan."),
    reinforce="Escribe una meta clara con cantidad y plazo para un personaje de cuento.",
    extend="Explica el ciclo meta, acción, monitoreo y redefinición.",
)

lesson(
    OA10, 2,
    "Una hoja y un lápiz. El registro semanal de Rodrigo y sus mensajes están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a distinguir hechos de sensaciones al monitorear mi aprendizaje, a manejar emociones como la frustración y a respetar el descanso. Sirve para revisar mi avance con datos y cuidar mi bienestar.",
    ["Sé formular metas progresivas.", "Sé que monitorear es revisar resultados."],
    [
        "Monitorear es mirar los resultados con datos. Un hecho es un dato registrado: «esta semana respondí 13 de 20». Una sensación es lo que sientes: «siento que no avanzo». Las sensaciones importan, pero los datos permiten comprobarlas. Muchas veces se avanza más de lo que se siente. Un registro semanal, aunque sea simple, ayuda a ver el progreso.",
        "Las emociones aparecen en el camino. La frustración surge cuando algo no sale; el orgullo, cuando se logra. Son normales. Equivocarse es parte de aprender y tienes derecho a pedir apoyo. Un error es información: muestra qué ajustar. Si la frustración es muy fuerte, conviene hacer una pausa y conversar con alguien de confianza.",
        "También hay límites: el descanso, el juego y el sueño son necesarios. Una meta que te obligue a estudiar sin parar o a dormir poco te perjudica y baja tu rendimiento. Un buen plan incluye pausas, tiempo libre y horarios de sueño. Gestionar tu aprendizaje es cuidar tu bienestar mientras avanzas.",
    ],
    [("registro", "anotación de resultados a lo largo del tiempo"), ("sensación", "lo que una persona siente o piensa que ocurre"), ("frustración", "malestar cuando algo no sale como se esperaba"), ("pausa", "descanso breve entre actividades"), ("rendimiento", "resultado de lo que se logra al estudiar o trabajar")],
    [
        W("Comprobar una sensación con datos", "Rodrigo siente que no avanza. Sus resultados: semana 1: 12; semana 2: 13; semana 3: 14. ¿Qué dicen los datos?", ["Los números suben cada semana.", "Mejoró 2 respuestas en total.", "Sí avanza, aunque lento."], "Sí avanza: subió de 12 a 14"),
        W("Manejar la frustración", "En la semana 4 Rodrigo obtiene 12 y se siente frustrado. ¿Qué puede hacer?", ["Un error es información.", "Puede hacer una pausa y revisar qué ajustar.", "Puede pedir apoyo."], "Hacer una pausa, revisar qué falló y pedir apoyo"),
    ],
    [
        M("Creer que si no se siente avance, no lo hay.", "Se confunde sensación con dato.", "Mira el registro."),
        M("Pensar que descansar es perder tiempo.", "Se cree que más horas siempre es mejor.", "El descanso mejora el rendimiento."),
    ],
    R=[
        ex("«Obtuve 14 de 20» ¿es un hecho o una sensación?", "Un hecho", "Es un dato registrado."),
        ex("«Siento que no avanzo» ¿es un hecho o una sensación?", "Una sensación", "Es lo que siente."),
        ex("¿Un error puede ser información para mejorar, sí o no?", "Sí", "Muestra qué ajustar."),
    ],
    U=[
        ex("¿Para qué sirve un registro semanal? A) Para ver el progreso con datos. B) Para castigarse.", "A", "Muestra el avance real."),
        ex("Si la frustración es muy fuerte, ¿conviene seguir sin parar o hacer una pausa?", "Hacer una pausa", "Permite calmarse y pensar."),
        ex("Dormir bien, ¿es parte de un buen plan de estudio, sí o no?", "Sí", "El descanso mejora el rendimiento."),
    ],
    A=[
        ex("Resultados semanales de Camila: 10, 12, 11, 14. ¿Cuál fue la mejor semana?", "La cuarta", "Tuvo 14, el mayor valor."),
        ex("Pía siente que «todo le sale mal», pero su registro muestra 9, 11 y 13. ¿Qué conviene decirle? A) Que sus datos muestran mejora. B) Que no se preocupe.", "A", "Los datos corrigen la sensación."),
        ex("Tomás planea estudiar 6 horas seguidas sin pausa los sábados. ¿Qué ajuste conviene?", "Hacer pausas y dividir en bloques", "Evita el agotamiento."),
    ],
    Z=[
        ex("¿Por qué es injusto juzgarte solo por una semana mala?", "Porque hay otros datos y puedes mejorar", "Una semana no representa todo el proceso."),
        ex("¿Por qué el descanso es parte de la meta?", "Porque ayuda a aprender y cuidar el bienestar", "El cuerpo y la mente rinden mejor con descanso."),
    ],
    D=[
        arith("Los resultados de Rodrigo fueron 12, 13, 14 y 15. ¿Cuántas respuestas mejoró desde la primera semana hasta la cuarta?", "15-12", "Se resta el primer resultado del último."),
        arith("Un plan incluye 3 bloques de 40 minutos de estudio con pausas de 10 minutos entre ellos (2 pausas). ¿Cuántos minutos dura el plan completo?", "3*40+2*10", "Se suman los tiempos de estudio y de pausa."),
    ],
    context=[ex("Antes de una prueba, Nicolás duerme 4 horas para estudiar más. Al día siguiente rinde peor. ¿Qué aprendió del descanso?", "Que dormir poco baja el rendimiento", "El sueño ayuda a rendir.")],
    selfcheck=[ex("En Orientación: ¿un registro ayuda a monitorear?", "Sí", "Muestra el avance con datos."), ex("¿Equivocarse es parte de aprender?", "Sí", "El error informa."), ex("¿Dormir poco mejora el rendimiento?", "No", "Lo baja bastante.")],
    task=T("Lee el registro inventado de Sofía: semana 1: 9 de 20; semana 2: 11 de 20; semana 3: 10 de 20; semana 4: 13 de 20. Ella dice: «Siento que no sirvo». Escribe: lo que dicen los datos, la emoción que puede sentir, un derecho que tiene, un límite de descanso y una acción para la próxima semana.", "Datos: subió de 9 a 13 con una baja. Emoción: frustración. Derecho: equivocarse y pedir apoyo. Límite: dormir 8 horas y hacer pausas. Acción: repasar los errores de la semana 3.", ["interpreta los datos", "nombra emoción y derecho", "incluye un límite de descanso", "propone una acción"], ["texto escrito"], ["ignorar los datos", "descuidar el descanso"], "Reconoce el uso de datos y pregunta cómo pediría apoyo."),
    reinforce="Escribe un registro de cuatro semanas para un personaje de cuento y una conclusión con datos.",
    extend="Explica por qué la sensación debe contrastarse con datos.",
)

lesson(
    OA10, 3,
    "Una hoja y un lápiz. Los dos planes de Lucía y la tabla de horas están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a comparar líneas de acción para lograr una meta y a prever sus consecuencias en tiempo y resultados. Sirve para elegir el plan que mejor se ajusta a mi vida.",
    ["Sé monitorear con datos.", "Sé cuidar el descanso."],
    [
        "Para lograr una meta suele haber más de una línea de acción. Lucía quiere mejorar su lectura en inglés. Plan A: estudiar 2 horas seguidas el domingo. Plan B: practicar 20 minutos al día. Ambos suman tiempo, pero tienen consecuencias distintas. La práctica distribuida, es decir, repartida en el tiempo, suele ayudar más a recordar que concentrar todo en una sola sesión.",
        "Para comparar planes calcula el tiempo semanal, mira si se ajusta a tu horario y si puedes mantenerlo. El plan A suma 120 minutos y el plan B 140 minutos en una semana de 7 días. Pero el mejor plan no es solo el que suma más: es el que puedes cumplir y te ayuda a recordar. Si un plan es demasiado exigente, abandonarlo es probable.",
        "Una buena decisión considera cuatro cosas: el tiempo, la constancia, los resultados esperados y el bienestar. Puedes probar un plan una o dos semanas, monitorear y ajustarlo. Esto es parte de gestionar de manera autónoma tu aprendizaje: eliges, pruebas, miras datos y decides.",
    ],
    [("línea de acción", "lo que se hace para lograr una meta"), ("práctica distribuida", "práctica repartida en varios momentos"), ("constancia", "mantener una acción en el tiempo"), ("exigente", "que pide mucho esfuerzo o tiempo"), ("ajustar", "cambiar algo para que funcione mejor")],
    [
        W("Calcular el tiempo semanal", "Plan A: 2 horas el domingo. Plan B: 20 minutos al día durante 7 días. ¿Cuántos minutos suma cada uno?", ["A: 2 horas = 120 minutos.", "B: 20 × 7 = 140 minutos.", "B suma más."], "A: 120 minutos. B: 140 minutos"),
        W("Elegir con criterios", "Lucía tiene actividades el domingo y poco tiempo libre. ¿Cuál plan es más viable?", ["El plan B se reparte en la semana.", "No exige un bloque largo.", "Es más fácil de mantener."], "El plan B"),
    ],
    [
        M("Pensar que estudiar muchas horas seguidas siempre es mejor.", "Se confunde tiempo con aprendizaje.", "La práctica distribuida ayuda a recordar."),
        M("Elegir el plan más exigente para «ir más rápido».", "Se subestima el cansancio.", "Elige un plan que puedas cumplir."),
    ],
    R=[
        ex("Practicar un poco cada día, ¿es práctica distribuida o concentrada?", "Distribuida", "Reparte el estudio en el tiempo."),
        ex("Un plan demasiado exigente, ¿es más fácil de abandonar, sí o no?", "Sí", "Cuesta mucho mantenerlo."),
        ex("Probar un plan una o dos semanas y ajustarlo, ¿es una buena estrategia, sí o no?", "Sí", "Permite mejorar con datos."),
    ],
    U=[
        ex("¿Qué plan suele ayudar más a recordar? A) Practicar un poco cada día. B) Estudiar solo la noche anterior.", "A", "La práctica distribuida ayuda a recordar."),
        ex("De los cuatro criterios (tiempo, constancia, resultados, bienestar), ¿cuál se refiere al cansancio?", "El bienestar", "Cuida que el plan no te agote."),
        ex("¿El mejor plan es solo el que suma más minutos, sí o no?", "No", "También debe poder cumplirse."),
    ],
    A=[
        arith("Plan C: 25 minutos al día de lunes a viernes. ¿Cuántos minutos suma en la semana?", "25*5", "Se multiplican los minutos por los días."),
        ex("Marcos tiene 30 minutos libres cada tarde y fútbol los miércoles. ¿Qué plan le conviene? A) 20 minutos diarios. B) 3 horas el miércoles.", "A", "Se ajusta a sus tardes y a su fútbol."),
        ex("Una estudiante prueba un plan dos semanas y ve que no avanza. ¿Qué debe hacer?", "Monitorear y ajustar el plan", "Los datos guían el cambio."),
    ],
    Z=[
        ex("¿Por qué conviene considerar el bienestar al elegir un plan?", "Porque un plan que agota se abandona", "El plan debe ser sostenible."),
        ex("Un joven dice: «Mejor estudiar todo el domingo y listo». ¿Qué ventaja y desventaja tiene su idea?", "Ahorra días, pero cansa y se recuerda menos", "La concentración puede agotar y no ayuda a recordar."),
    ],
    D=[
        arith("Lucía estudia 20 minutos al día durante 6 días. ¿Cuántos minutos suma?", "20*6", "Se multiplican los minutos por los días."),
        arith("Si su meta es juntar 280 minutos de práctica en 2 semanas, ¿cuántos minutos por semana necesita?", "280//2", "Se divide el total entre las semanas."),
    ],
    context=[ex("Pablo quiere mejorar su lectura. Compara dos planes: leer 15 minutos diarios o 105 minutos el sábado. ¿Suman lo mismo en la semana y cuál es más sostenible?", "Suman lo mismo; el diario es más sostenible", "15 × 7 = 105; repartido es más fácil de mantener.")],
    selfcheck=[ex("En Orientación: ¿la práctica distribuida ayuda a recordar?", "Sí", "Reparte el esfuerzo."), ex("¿El plan más largo siempre es mejor?", "No", "Debe poder cumplirse."), ex("¿Se puede probar un plan y ajustarlo?", "Sí", "Se aprende con los datos.")],
    task=T("Lee el caso inventado de Rafael: quiere llegar de 10 a 16 palabras correctas de vocabulario en 4 semanas. Plan A: estudiar 90 minutos el sábado. Plan B: 15 minutos diarios, 6 días. Calcula el tiempo semanal de cada plan, compara ventajas y desventajas, elige uno y explica cómo monitoreará.", "A: 90 minutos. B: 15 × 6 = 90 minutos. Mismo tiempo; B reparte la práctica y ayuda a recordar. Elijo B. Monitoreo: una prueba corta cada sábado y ajustar si no sube.", ["calcula el tiempo semanal", "compara ventajas y desventajas", "elige y justifica", "explica el monitoreo"], ["texto o tabla"], ["elegir solo por el tiempo", "olvidar monitorear"], "Reconoce los cálculos y pregunta qué ajuste haría si no avanza."),
    reinforce="Escribe dos planes distintos para una misma meta y calcula el tiempo semanal de cada uno.",
    extend="Explica por qué la práctica distribuida suele ayudar a recordar.",
)

lesson(
    OA10, 4,
    "Una hoja y un lápiz. Los resultados de Nicolás y las cuatro posibles modificaciones están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a elegir con criterio cómo redefinir mis acciones cuando los resultados no llegan, sin renunciar a la meta. Sirve para ajustar mi plan de forma sensata y segura.",
    ["Sé comparar líneas de acción.", "Sé monitorear con datos."],
    [
        "Redefinir significa cambiar las acciones, y no necesariamente la meta, cuando los datos muestran que no se avanza. Antes de cambiar, conviene diagnosticar: ¿qué dicen los resultados?, ¿qué parte del plan no se cumplió?, ¿qué dificulta avanzar? Puede ser falta de tiempo, una técnica que no sirve, cansancio o una duda de contenido sin resolver.",
        "Una buena redefinición cambia una sola cosa a la vez, para saber si funcionó. Por ejemplo, si Nicolás no mejora con 15 minutos de lectura, puede probar subrayar ideas centrales, pedir que le expliquen un tema difícil o ajustar el horario a un momento en que esté más descansado. Si en dos semanas el cambio no funciona, prueba otro.",
        "A veces la meta misma debe ajustarse: si era muy ambiciosa o el plazo era muy corto, se puede ampliar el plazo o dividirla en escalones más pequeños. No se trata de rendirse, sino de ser realista. Una redefinición segura no incluye hacer trampa, copiar ni sacrificar el sueño: incluye pedir ayuda a una persona adulta o a un compañero de confianza si lo necesitas.",
    ],
    [("redefinir", "cambiar las acciones del plan al ver los resultados"), ("diagnosticar", "analizar por qué algo no funciona"), ("ambicioso", "que pide mucho en poco tiempo"), ("técnica de estudio", "forma de estudiar, como resumir o hacer esquemas"), ("sacrificar", "renunciar a algo importante")],
    [
        W("Diagnosticar", "Nicolás practica 15 minutos al día, pero sigue en 10 de 20. Descubre que se cansa porque estudia al final del día. ¿Qué cambia?", ["La causa es el cansancio.", "Conviene cambiar el horario.", "Cambia una sola cosa."], "Cambiar el horario a un momento en que esté más descansado"),
        W("Ajustar la meta", "La meta de Nicolás era llegar de 10 a 18 en dos semanas. Avanzó a 12. ¿Qué ajuste realista puede hacer?", ["La meta era ambiciosa.", "Puede ampliar el plazo.", "O dividirla en escalones."], "Ampliar el plazo o dividir la meta en escalones"),
    ],
    [
        M("Cambiar muchas cosas a la vez.", "Se quiere arreglar todo rápido.", "Cambia una cosa y observa."),
        M("Hacer trampa para cumplir la meta.", "Se prioriza el resultado.", "El aprendizaje real requiere honestidad."),
    ],
    R=[
        ex("Cuando no hay avance, ¿primero se diagnostica o se abandona la meta?", "Se diagnostica", "Hay que entender qué falla."),
        ex("Cambiar una sola cosa a la vez, ¿ayuda a saber qué funcionó, sí o no?", "Sí", "Permite comprobar el efecto."),
        ex("Copiar para cumplir la meta, ¿es una redefinición segura, sí o no?", "No", "No es honesto ni enseña."),
    ],
    U=[
        ex("¿Qué es una meta demasiado ambiciosa? A) La que pide mucho en poco tiempo. B) La que es clara.", "A", "Esa es su definición."),
        ex("Si el cansancio es la causa, ¿qué conviene ajustar: el horario o el color del cuaderno?", "El horario", "Se ataca la causa."),
        ex("¿Ampliar el plazo puede ser una redefinición sensata, sí o no?", "Sí", "Hace la meta más realista."),
    ],
    A=[
        ex("Resultados de Ema: 10, 10, 11. Estudia 20 minutos diarios. Dice que le cuesta entender el vocabulario. ¿Qué cambio es más razonable? A) Pedir que le expliquen las palabras difíciles. B) Dejar de estudiar.", "A", "Atiende la causa: la comprensión."),
        ex("Un estudiante prueba subrayar ideas centrales por dos semanas y sus resultados suben de 10 a 13. ¿Qué debe hacer? A) Mantener el cambio. B) Abandonarlo.", "A", "Los datos muestran que funcionó."),
        ex("Pía cambia horario, técnica y cantidad de horas a la vez y no sabe qué ayudó. ¿Qué error cometió?", "Cambió muchas cosas a la vez", "No puede identificar el efecto de cada cambio."),
    ],
    Z=[
        ex("¿Por qué redefinir no es lo mismo que rendirse?", "Porque se mantiene la meta y se cambia el camino", "Se busca una forma que funcione."),
        ex("¿Por qué es mejor pedir ayuda que copiar para cumplir una meta?", "Porque copiar no enseña y la ayuda sí", "El aprendizaje requiere comprender."),
    ],
    D=[
        arith("La meta era llegar a 18 desde 10 en dos semanas. Nicolás llegó a 12. ¿Cuántas respuestas le faltan?", "18-12", "A la meta se le resta lo alcanzado."),
        arith("Si Nicolás amplía el plazo de 2 a 5 semanas, ¿cuántas semanas agrega?", "5-2", "Se resta el plazo original del nuevo."),
    ],
    context=[ex("Tomás no entiende un tema de ciencias y sus resultados no suben. Decide pedirle a su profesora un ejemplo. ¿Qué tipo de redefinición es?", "Pedir ayuda sobre la causa", "Atiende una duda de contenido sin resolver.")],
    selfcheck=[ex("En Orientación: ¿redefinir es cambiar las acciones?", "Sí", "Se ajusta el camino."), ex("¿Se deben cambiar muchas cosas a la vez?", "No", "Mejor una a la vez."), ex("¿Copiar es una buena redefinición?", "No", "Copiar no enseña.")],
    task=T("Lee el caso inventado de Emilia: su meta era 16 de 20 en comprensión lectora en tres semanas. Resultados: 10, 11, 11. Estudia por la noche, cansada, y evita preguntar dudas. Escribe un diagnóstico con dos causas, dos cambios para probar (uno por vez, con su plazo) y cómo sabrá si funcionó.", "Causas: estudia cansada y no pregunta dudas. Cambios: 1) estudiar en la tarde por dos semanas; 2) preguntar una duda por día a la profesora. Sabrá si funcionó si sus resultados suben a 13 o más en dos semanas.", ["diagnóstica dos causas", "propone cambios de a uno con plazo", "dice cómo comprobará", "no sacrifica el descanso ni copia"], ["texto escrito"], ["cambiar todo a la vez", "abandonar la meta"], "Reconoce el diagnóstico y pregunta a quién pediría apoyo."),
    reinforce="Escribe dos posibles causas de que no suban los resultados y un cambio para cada una.",
    extend="Explica por qué cambiar una cosa a la vez permite saber qué funcionó.",
)

lesson(
    OA10, 5,
    "Una hoja y un lápiz. Los mensajes, el plan y la lista de apoyos están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a pedir apoyo, a comunicar mi plan de aprendizaje a mi familia o a mis profesores y a usar recursos del colegio. Sirve para gestionar mi aprendizaje con ayuda cuando la necesito.",
    ["Sé formular y ajustar metas.", "Sé pedir ayuda con claridad."],
    [
        "Gestionar tu aprendizaje de forma autónoma no es hacerlo solo. Es saber cuándo y a quién pedir apoyo. Puedes recurrir a tus profesores, a compañeros que te ayuden, a una persona adulta de tu casa, a la biblioteca del colegio y a tutorías o talleres de refuerzo si existen. Pedir apoyo es una estrategia de estudiantes responsables.",
        "Para pedir apoyo, sé concreto: di qué meta tienes, qué has hecho, qué resultado has obtenido y qué necesitas. Por ejemplo: «Mi meta es llegar a 16 de 20 en comprensión lectora. He leído 15 minutos diarios y estoy en 11. Me cuesta encontrar la idea principal. ¿Puede darme un ejemplo?». Un mensaje así permite que te ayuden mejor.",
        "También conviene compartir tu plan con alguien de confianza que te recuerde tus metas y celebre tus logros. Una conversación semanal de cinco minutos, con la familia o un compañero, mantiene la constancia. Y recuerda que el apoyo no reemplaza tu esfuerzo: tú conduces tu aprendizaje, y los demás te acompañan.",
    ],
    [("apoyo", "ayuda de personas o recursos"), ("tutoría", "apoyo individual o en grupo pequeño para aprender"), ("concreto", "con datos claros y precisos"), ("estrategia", "forma planificada de lograr algo"), ("constancia", "mantener una acción en el tiempo")],
    [
        W("Armar una petición de ayuda", "Meta: 16 de 20 en comprensión lectora. Hecho: 15 minutos diarios, resultado 11. Dificultad: idea principal. Arma el mensaje.", ["Dice la meta.", "Dice lo que hizo y el resultado.", "Dice qué necesita."], "«Mi meta es 16 de 20; leo 15 minutos diarios y estoy en 11; me cuesta la idea principal, ¿me da un ejemplo?»"),
        W("Elegir el apoyo", "Elena no entiende un tema de matemática. ¿A quién puede acudir primero?", ["Al profesor de la asignatura.", "A una tutoría de refuerzo.", "A un compañero que lo entienda."], "Al profesor de matemática, a una tutoría o a un compañero"),
    ],
    [
        M("Pensar que pedir ayuda es no poder solo.", "Se cree que lo autónomo es aislado.", "Autónomo significa conducir tu aprendizaje y pedir apoyo."),
        M("Pedir ayuda de forma vaga: «no entiendo nada».", "No se dice qué parte cuesta.", "Di la meta, lo que hiciste y qué necesitas."),
    ],
    R=[
        ex("La biblioteca del colegio, ¿es un recurso de apoyo, sí o no?", "Sí", "Ofrece libros y espacio de estudio."),
        ex("Pedir apoyo, ¿es una estrategia de estudiantes responsables, sí o no?", "Sí", "Ayuda a lograr la meta."),
        ex("¿Un mensaje concreto dice qué necesitas o solo «no entiendo»?", "Dice qué necesitas", "Permite que te ayuden mejor."),
    ],
    U=[
        ex("¿Qué debe decir una buena petición de ayuda? A) Meta, lo que hice, resultado y qué necesito. B) Solo mi nota.", "A", "Esos datos orientan la ayuda."),
        ex("Una conversación semanal de cinco minutos con alguien de confianza, ¿ayuda a la constancia, sí o no?", "Sí", "Recuerda las metas y celebra logros."),
        ex("¿El apoyo reemplaza tu esfuerzo, sí o no?", "No", "Tú conduces tu aprendizaje."),
    ],
    A=[
        ex("Cuatro mensajes: 1) «No entiendo»; 2) «Mi meta es 14; estudié 20 minutos diarios; llegué a 11; no entiendo las fracciones. ¿Me ayuda?»; 3) «Ayúdame»; 4) «Me da lata». ¿Cuál es concreto?", "El 2", "Tiene meta, acciones, resultado y necesidad."),
        ex("Tomás quiere contarle a su familia su plan de lectura. ¿Qué incluye? A) Meta, acciones y fecha de revisión. B) Solo que leerá.", "A", "Así pueden apoyarlo."),
        ex("Un estudiante nota que una tutoría de refuerzo es los jueves a las 15:00. ¿Qué debe hacer para usarla?", "Inscribirse e ir ese día", "Aprovecha un recurso del colegio."),
    ],
    Z=[
        ex("¿Por qué ser concreto al pedir ayuda mejora la respuesta?", "Porque quien ayuda entiende qué necesitas", "Con datos precisos puede orientarte mejor."),
        ex("Un joven dice: «Si pido ayuda, el profesor pensará que soy torpe». ¿Qué le responderías?", "Que pedir ayuda muestra responsabilidad", "Los docentes valoran el interés."),
    ],
    D=[
        arith("Un plan de apoyo incluye 3 conversaciones de 5 minutos por semana durante 6 semanas. ¿Cuántos minutos suma?", "3*5*6", "Se multiplican las conversaciones, los minutos y las semanas."),
        arith("De 32 estudiantes, 20 usan alguna tutoría y el resto no. ¿Cuántos no usan tutoría?", "32-20", "Al total se le restan los que sí usan."),
    ],
    context=[ex("Valentina tiene una duda de ciencias a una semana de la prueba. ¿Qué dos recursos del colegio puede usar y cuál debe hacer primero?", "El profesor y la tutoría; primero preguntar la duda", "Preguntar a tiempo evita que el problema crezca.")],
    selfcheck=[ex("En Orientación: ¿pedir apoyo es parte de gestionar tu aprendizaje?", "Sí", "Es una estrategia."), ex("¿Una petición concreta incluye lo que necesitas?", "Sí", "Permite que te ayuden."), ex("¿El apoyo reemplaza tu esfuerzo?", "No", "Tú conduces tu aprendizaje.")],
    task=T("Lee el caso inventado de Ismael: su meta es pasar de 9 a 15 de 20 en vocabulario de inglés en seis semanas; practica 15 minutos diarios, lleva tres semanas y está en 11; no entiende cómo memorizar. Escribe: un mensaje de petición de ayuda al profesor, una lista de tres recursos de apoyo y cómo compartirá su plan con alguien de confianza.", "Mensaje: «Mi meta es 15 de 20 en seis semanas; practico 15 minutos diarios, estoy en 11; me cuesta memorizar. ¿Puede orientarme?». Recursos: tutoría, biblioteca, compañero. Compartir: una conversación semanal de cinco minutos con una persona de su casa.", ["mensaje con meta, acciones, resultado y necesidad", "tres recursos", "forma de compartir el plan", "tono respetuoso"], ["texto escrito"], ["mensaje vago", "pensar que el apoyo reemplaza el esfuerzo"], "Reconoce el mensaje concreto y pregunta cuándo revisará su avance."),
    reinforce="Escribe un mensaje concreto para pedirle ayuda a una profesora con una meta de lectura.",
    extend="Explica por qué pedir ayuda forma parte de ser autónomo.",
)

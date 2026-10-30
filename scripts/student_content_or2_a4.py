"""Cuaderno del estudiante, 2.º básico Orientación: OA 07 (pertenencia y participación en grupos) y OA 08 (hábitos y motivación para aprender)."""
from __future__ import annotations

from student_content_or2_a import lesson, T, W, M
from student_lessons import ex

OA7, OA8 = "OR02 OA 07", "OR02 OA 08"

# ================================================================ OA 07
lesson(
    OA7, 1,
    "Una hoja y lápiz. Las descripciones de grupos están escritas en los ejercicios. Cada familia es distinta y todas valen; no tienes que contar nada privado.",
    "Aprenderé qué grupos forman parte de mi vida: familia, curso y amigos. Sirve para reconocer dónde pertenezco y valorar que los grupos son distintos.",
    ["Sé que vivo con personas que me cuidan.", "Sé que tengo un curso."],
    [
        "Un grupo es un conjunto de personas que comparten algo. Pertenecer a un grupo es sentirse parte de él. Tres grupos importantes son tu familia, tu curso y tus pares, es decir, los niños y niñas de tu edad con los que juegas o estudias.",
        "Los grupos son diversos. Hay familias con mamá, con papá, con ambos, con dos mamás o dos papás, con abuelos, con tíos, con hermanos mayores o con otras personas que cuidan. Todas son familias y todas valen. Los cursos tienen niños y niñas con distintos gustos, habilidades y formas de ser.",
        "Pertenecer no depende de ser igual a los demás. Depende de ser parte, de ser cuidado y de aportar. Una persona pertenece a un curso aunque sea más callada o más movida. Cada grupo tiene sus costumbres, y podemos conocerlas y respetarlas.",
    ],
    [("grupo", "conjunto de personas que comparten algo"), ("pertenecer", "sentirse parte de un grupo"), ("familia", "personas que se cuidan y viven juntas"), ("curso", "grupo de estudiantes que aprenden juntos"), ("pares", "niños y niñas de mi edad")],
    [
        W("Reconocer grupos", "Tomás pertenece a su familia, a su curso y a un equipo de fútbol con amigos. ¿Cuántos grupos nombró?", ["Familia: 1.", "Curso: 2.", "Equipo con amigos: 3."], "3 grupos"),
        W("Familias diversas", "Ema vive con su abuela y Beto vive con su mamá y su papá. ¿Cuál es una familia?", ["Ema vive con quien la cuida.", "Beto también.", "Las dos son familias."], "Las dos son familias"),
    ],
    [
        M("Pensar que mi familia es la «normal» y las otras no.", "Conocemos mejor la nuestra.", "Todas las familias valen y son distintas."),
        M("Creer que para pertenecer hay que ser igual a todos.", "Queremos encajar.", "Pertenecer es ser parte y aportar siendo uno mismo."),
    ],
    R=[
        ex("¿El curso es un grupo?", "Sí", "Reúne a niños y niñas que aprenden juntos."),
        ex("¿Una familia puede estar formada por una abuela y su nieta?", "Sí", "Quienes se cuidan forman una familia."),
        ex("¿Tus amigos de tu edad son tus pares?", "Sí", "Par significa de la misma edad."),
    ],
    U=[
        ex("¿Qué es pertenecer a un grupo?", "Sentirse parte de él", "Pertenecer es ser parte de algo."),
        ex("¿Todas las familias son iguales?", "No", "Hay muchas formas de familia."),
        ex("¿Hay que ser igual a los demás para pertenecer?", "No", "Se pertenece siendo uno mismo."),
    ],
    A=[
        ex("Rosa nombra su familia, su curso y su taller de dibujo. ¿Cuántos grupos nombró?", "3", "Nombró tres grupos distintos."),
        ex("Una niña vive con su tío y su prima. Un niño vive con su madre y su padre. ¿Qué tienen en común?", "Los dos viven con personas que los cuidan", "Eso es lo que forma una familia."),
        ex("Elige cuál es un grupo de pares: tus compañeros de curso o los adultos de tu casa.", "Tus compañeros de curso", "Son de tu edad."),
    ],
    Z=[
        ex("Un niño dice: «Mi familia es mejor porque somos más». ¿Qué dato falta?", "Que el número no hace mejor a una familia", "Las familias valen por el cuidado, no por el tamaño."),
        ex("Una niña es más callada que el resto. ¿Deja de pertenecer al curso?", "No", "Pertenece aunque sea distinta."),
    ],
    D=[
        ex("Si un curso tiene 12 niñas y 14 niños, ¿cuántos estudiantes hay?", "26", "12 más 14 es 26."),
        ex("Si perteneces a 3 grupos y te unes a 1 más, ¿a cuántos perteneces?", "4", "3 más 1 es 4."),
    ],
    context=[ex("En el curso de Camila, cada niño dibujó su familia. Hubo dibujos con abuelos, con hermanos, con una mamá sola y con papás. La profesora dijo: «Todas son familias». ¿Tiene razón?", "Sí", "Una familia se forma por el cuidado entre sus integrantes.")],
    selfcheck=[ex("¿Pertenecer es ser parte de un grupo?", "Sí", "Es sentirse parte."), ex("¿Las familias son distintas?", "Sí", "Hay muchas formas de familia."), ex("¿Hay que ser igual para pertenecer?", "No", "Se pertenece siendo uno mismo.")],
    task=T("Dibuja o escribe tres grupos a los que perteneces: tu familia (o con quienes vives), tu curso y un grupo de pares (amigos, equipo, taller). Para cada grupo, escribe una palabra que lo describa. No tienes que contar datos privados.", "Familia: cariñosa. Curso: bullicioso. Equipo de baile: alegre.", ["tres grupos", "una palabra para cada uno", "sin datos privados"], ["dibujo o lista"], ["comparar familias", "dar datos privados"], "Reconoce los grupos y pregunta qué le gusta de cada uno."),
    reinforce="Nombra a una persona de cada uno de tus grupos.",
    extend="Escribe qué tienen en común dos grupos distintos a los que perteneces.",
)

lesson(
    OA7, 2,
    "Una hoja y lápiz. Las fichas de personas están escritas en los ejercicios. No tienes que contar nada privado.",
    "Aprenderé a describir a las personas de mis grupos, sus características y los vínculos que tengo con ellas. Sirve para conocer y valorar a quienes me rodean.",
    ["Sé describir características con dos datos.", "Sé qué grupos forman parte de mi vida."],
    [
        "Un grupo está formado por personas. Cada una tiene sus características: cómo es, qué le gusta y qué sabe hacer. Para conocer a alguien de tu grupo, puedes observar y preguntar. «¿Qué te gusta hacer?» es una buena pregunta para empezar.",
        "Entre las personas hay vínculos, es decir, relaciones. Un vínculo puede ser de familia, de amistad o de compañeros. Cada vínculo tiene cuidados distintos. Con un hermano o una hermana compartes la casa. Con tu amiga compartes juegos. Con tu profesora aprendes.",
        "Cada persona cumple un papel en el grupo, pero nadie es solo un papel. Una abuela puede cocinar y también contar cuentos. Una compañera puede ser buena en matemática y también muy divertida. Valorar es notar lo que cada una aporta.",
    ],
    [("vínculo", "relación entre personas"), ("compañero", "persona con quien comparto un grupo"), ("observar", "mirar con atención"), ("aportar", "dar algo que ayuda al grupo"), ("papel", "lo que una persona hace en un grupo")],
    [
        W("Describir con dos datos", "Pía dice: «Mi abuelo cuenta cuentos y le gusta pescar». ¿Qué dos datos dio?", ["Dato 1: cuenta cuentos.", "Dato 2: le gusta pescar.", "Ambos son características."], "Cuenta cuentos y le gusta pescar"),
        W("Tipos de vínculo", "Luis dice: «Beto es mi compañero de banco». ¿Qué tipo de vínculo es?", ["Comparten el curso.", "Es una relación entre compañeros.", "No es de familia."], "Vínculo de compañeros"),
    ],
    [
        M("Pensar que conozco a una persona con un solo dato.", "Vemos solo una parte.", "Descubre más datos preguntando."),
        M("Creer que cada persona hace una sola cosa.", "Las vemos siempre en el mismo papel.", "Todos tenemos varias características."),
    ],
    R=[
        ex("¿Un hermano o una hermana tiene un vínculo de familia?", "Sí", "Son parte de la misma familia."),
        ex("¿Qué se puede preguntar para conocer a alguien?", "¿Qué te gusta hacer?", "Ayuda a conocer sus intereses."),
        ex("Un compañero de curso, ¿es un vínculo de compañeros?", "Sí", "Comparten el curso."),
    ],
    U=[
        ex("¿Qué es un vínculo?", "Una relación entre personas", "Une a las personas de un grupo."),
        ex("¿Una persona tiene un solo rasgo?", "No", "Cada persona tiene muchos."),
        ex("¿Para qué sirve valorar a las personas del grupo?", "Para notar lo que aportan", "Reconoce su aporte."),
    ],
    A=[
        ex("Ficha: Rosa es ordenada y le gusta cantar. Escribe una frase con los dos datos.", "Rosa es ordenada y le gusta cantar", "Usa los dos datos de la ficha."),
        ex("Ficha: Dani cocina con su mamá y ayuda a poner la mesa. ¿Qué aporta Dani en su casa?", "Ayuda a cocinar y a poner la mesa", "Son aportes concretos."),
        ex("Elige el vínculo: amiga del barrio, tía, compañero de curso. ¿Cuál es de familia?", "Tía", "Una tía es parte de la familia."),
    ],
    Z=[
        ex("Un niño dice: «Mi compañera solo sabe dibujar». ¿Qué le falta considerar?", "Que tiene otras características que no conoce", "Una persona tiene muchas."),
        ex("Dos niñas son amigas y compañeras de curso. ¿Tienen un solo vínculo?", "No, tienen más de uno", "Pueden ser amigas y compañeras."),
    ],
    D=[
        ex("Si en tu grupo de 5 personas conoces 3 características de cada una, ¿cuántas conoces?", "15", "3 más 3 más 3 más 3 más 3 es 15."),
        ex("Si anotas 2 características de tu amigo y 2 de tu amiga, ¿cuántas anotaste?", "4", "2 más 2 es 4."),
    ],
    context=[ex("La profesora pide: «Cada uno diga algo que le gusta de un compañero». Beto dice: «Me gusta cómo explica Ema». ¿Valoró a Ema?", "Sí", "Dijo algo concreto que ella aporta.")],
    selfcheck=[ex("¿Un vínculo es una relación?", "Sí", "Une a las personas."), ex("¿Una persona tiene muchos rasgos?", "Sí", "Nadie tiene uno solo."), ex("¿Puedo preguntar para conocer?", "Sí", "Preguntar ayuda a conocer.")],
    task=T("Elige a una persona de tu familia o de tu curso (o usa a Rosa: ordenada, le gusta cantar). Escribe o dibuja dos características suyas, el tipo de vínculo que tienes con ella y una pregunta que le harías para conocerla más.", "Persona: mi compañera Ema. Características: ordenada y le gusta cantar. Vínculo: compañera. Pregunta: «¿Qué canción te gusta?»", ["dos características", "tipo de vínculo", "una pregunta para conocer"], ["ficha escrita o dibujada"], ["una sola característica", "datos privados"], "Reconoce la ficha y pregunta qué otra característica descubriría."),
    reinforce="Hazle hoy una pregunta a alguien de tu grupo para conocerlo mejor.",
    extend="Escribe qué aporta cada persona de tu familia.",
)

lesson(
    OA7, 3,
    "Una hoja y lápiz. Las tareas de orden y las adaptaciones están escritas en los ejercicios.",
    "Aprenderé a participar en mis grupos ayudando en el orden de la casa y de la sala de formas que todos puedan hacer. Sirve para que todos aporten y nadie quede fuera.",
    ["Sé que cada persona aporta algo a su grupo.", "Sé ordenar mis cosas."],
    [
        "Participar activamente es hacer algo para el grupo. En la casa puedes ayudar a poner la mesa, a guardar los juguetes o a regar una planta. En la sala puedes limpiar la pizarra, ordenar los libros o repartir materiales. Son tareas pequeñas que ayudan a todos.",
        "Las tareas deben poder hacerse. Una tarea accesible es la que una persona puede realizar con su cuerpo, su edad y sus apoyos. Si una tarea es muy pesada, puedes elegir una parte. Alguien que no camina bien puede repartir hojas desde su lugar. Alguien que habla poco puede ayudar ordenando.",
        "Compartir las tareas ayuda a que no sean siempre las mismas personas. Una tabla de turnos muestra quién hace qué cada día. Si una tarea te cuesta, puedes decir «necesito ayuda» o proponer otra. Participar con alegría hace que el grupo sea más agradable.",
    ],
    [("participar", "hacer algo junto con el grupo"), ("tarea", "trabajo que me corresponde"), ("accesible", "que todos pueden hacer"), ("turno", "momento en que me toca"), ("apoyo", "ayuda para poder hacer algo")],
    [
        W("Elegir una tarea posible", "Ana tiene el brazo enyesado. ¿Qué tarea puede hacer en la sala: cargar una caja pesada o repartir hojas con la mano sana?", ["Cargar una caja pesada es difícil con yeso.", "Repartir hojas con una mano es posible.", "Elige lo que se puede."], "Repartir hojas con la mano sana"),
        W("Usar una tabla de turnos", "En la tabla, el lunes limpia Rosa y el martes limpia Luis. ¿Quién limpia el martes?", ["Busca el día martes.", "Martes dice Luis.", "Es Luis."], "Luis"),
    ],
    [
        M("Pensar que solo algunos deben ordenar.", "A veces siempre lo hacen los mismos.", "Usa turnos para que todos participen."),
        M("Creer que si una tarea me cuesta, no puedo participar.", "Vemos solo la tarea completa.", "Puedo hacer una parte o pedir apoyo."),
    ],
    R=[
        ex("Guardar los juguetes, ¿es participar en el orden de la casa?", "Sí", "Ayuda a mantener el lugar ordenado."),
        ex("Borrar la pizarra, ¿es una tarea de la sala?", "Sí", "Ayuda a todo el curso."),
        ex("¿Todos pueden participar de alguna forma?", "Sí", "Siempre hay una forma posible."),
    ],
    U=[
        ex("¿Qué es una tarea accesible?", "La que una persona puede hacer con sus apoyos", "Se adapta a la persona."),
        ex("¿Para qué sirve una tabla de turnos?", "Para repartir las tareas entre todos", "Así nadie hace siempre lo mismo."),
        ex("¿Qué puedes decir si una tarea te cuesta?", "Necesito ayuda", "Pedir apoyo es parte de participar."),
    ],
    A=[
        ex("Tabla: lunes Pía, martes Dani, miércoles Tomás. ¿Quién ordena el miércoles?", "Tomás", "Miércoles está asignado a Tomás."),
        ex("Beto usa silla de ruedas. Elige una tarea que puede hacer en la sala: repartir lápices desde su lugar o subir a un estante alto.", "Repartir lápices desde su lugar", "Es una tarea posible para él."),
        ex("Escribe una tarea que puedes hacer hoy en tu casa.", "Poner la mesa", "Es concreta y posible."),
    ],
    Z=[
        ex("Un niño dice: «Yo no ordeno porque soy chico». ¿Qué tarea pequeña podría hacer?", "Guardar sus juguetes", "Siempre hay una tarea a su medida."),
        ex("Una niña siempre limpia sola la sala. ¿Qué podría proponer el curso?", "Una tabla de turnos", "Reparte el trabajo."),
    ],
    D=[
        ex("Un curso se reparte en 4 equipos y cada equipo tiene 6 niños. ¿Cuántos niños tiene el curso?", "24", "6 más 6 más 6 más 6 es 24."),
        ex("Si hay 5 tareas y cada día se hacen 2, ¿cuántas faltan al día siguiente?", "3", "5 menos 2 es 3."),
    ],
    context=[ex("En el curso de Rosa se arma una tabla de turnos para la sala: regar la planta, ordenar libros, borrar la pizarra y repartir hojas. Luis tiene una pierna lesionada. ¿Qué tarea puede hacer?", "Repartir hojas desde su lugar o regar la planta con ayuda", "Puede participar con una tarea adaptada.")],
    selfcheck=[ex("¿Participar es ayudar al grupo?", "Sí", "Aporta a todos."), ex("¿Las tareas pueden adaptarse?", "Sí", "Así todos pueden participar."), ex("¿Una tabla de turnos reparte el trabajo?", "Sí", "Evita que sean siempre los mismos.")],
    task=T("Arma una tabla de turnos de cuatro tareas del hogar o de la sala (por ejemplo: poner la mesa, guardar juguetes, regar plantas, ordenar libros) para cuatro días. Anota a quién le toca cada una (usa nombres inventados si prefieres) y una adaptación para alguien que no puede hacer una de ellas.", "Lunes: poner la mesa (Ema). Martes: guardar juguetes (Luis). Miércoles: regar (Rosa). Jueves: ordenar libros (Pía). Adaptación: si Luis tiene un yeso, guarda solo los livianos.", ["cuatro tareas", "una persona por tarea", "una adaptación"], ["tabla escrita o dibujada"], ["una persona para todas", "sin adaptación"], "Reconoce la tabla y revisa que las tareas sean posibles para todos."),
    reinforce="Hoy haz una tarea para el orden de tu casa sin que te la pidan.",
    extend="Propone una tarea nueva para el orden de tu sala y escribe quién podría hacerla.",
)

lesson(
    OA7, 4,
    "Una hoja y lápiz. Las escenas de grupos están escritas en los ejercicios.",
    "Aprenderé a valorar mis grupos y a la vez a decidir por mí mismo cuando algo no me parece bien. Sirve para pertenecer sin perder lo que soy.",
    ["Sé qué grupos son importantes para mí.", "Sé decir no gracias."],
    [
        "Pertenecer a un grupo da seguridad y compañía. En un grupo aprendemos, jugamos y nos ayudamos. Valorar tu grupo es notar lo bueno que te da y lo que tú aportas. Puedes decir cosas como «en mi curso me ayudan» o «en mi familia me escuchan».",
        "Pertenecer no significa hacer todo lo que otros piden. Tienes autonomía: puedes pensar y decidir por ti. Si el grupo te pide algo que te incomoda, que daña a otro o que te da miedo, puedes decir «no». Un buen grupo respeta tu no y no te deja afuera por eso.",
        "Hay grupos que excluyen o presionan: dicen «si no lo haces, no eres de los nuestros». Eso no es buen trato. Si te pasa, avisa a un adulto de confianza. Y también puedes ser tú quien invite a un compañero que está solo, para que todos pertenezcan.",
    ],
    [("valorar", "reconocer lo bueno de algo"), ("autonomía", "capacidad de decidir por mí"), ("presionar", "obligar a alguien a hacer algo"), ("excluir", "dejar a alguien afuera"), ("invitar", "pedirle a alguien que se una")],
    [
        W("Decir no a una presión", "Un grupo le dice a Tomás: «Si no te burlas de Luis, no juegas con nosotros». ¿Qué puede hacer Tomás?", ["Burlarse daña a Luis.", "Tomás puede decir no.", "También puede avisar a un adulto y jugar con otros."], "Decir no y avisar a un adulto"),
        W("Invitar", "Rosa ve a un compañero solo en el recreo. ¿Qué puede decirle?", ["Puede acercarse.", "Puede invitarlo.", "Por ejemplo: «¿Quieres jugar con nosotros?»."], "«¿Quieres jugar con nosotros?»"),
    ],
    [
        M("Hacer lo que el grupo pide aunque me incomode, para no quedarme solo.", "Tenemos miedo a quedar fuera.", "Puedo decir no y buscar a un adulto o a otros amigos."),
        M("Creer que el grupo es dueño de mis decisiones.", "Queremos ser parte.", "Pertenezco y a la vez decido por mí."),
    ],
    R=[
        ex("¿Un grupo da compañía y seguridad?", "Sí", "En un buen grupo nos ayudamos."),
        ex("Si un grupo te pide dañar a otro, ¿puedes decir no?", "Sí", "Tienes derecho a decidir por ti."),
        ex("¿Invitar a alguien que está solo ayuda a que pertenezca?", "Sí", "Así se siente parte del grupo."),
    ],
    U=[
        ex("¿Qué es autonomía?", "Poder decidir por mí", "Cada persona decide."),
        ex("¿Pertenecer significa hacer todo lo que piden?", "No", "Puedo decir no."),
        ex("Si un grupo te presiona, ¿a quién avisas?", "A un adulto de confianza", "Un adulto puede ayudar."),
    ],
    A=[
        ex("Un amigo te dice: «Llévate algo que no es tuyo o no eres de los nuestros». Escribe qué responderías.", "No, eso no está bien", "Dice no sin pelear."),
        ex("Dani ve a una niña sola en el patio. Elige la mejor acción: invitarla a jugar o mirar sin hacer nada.", "Invitarla a jugar", "Incluye a quien está sola."),
        ex("Escribe algo bueno que te da un grupo al que perteneces.", "Compañía y ayuda", "Valora el grupo."),
    ],
    Z=[
        ex("Un niño dice: «Mi grupo me excluye si no hago lo que dicen». ¿Es buen trato?", "No", "No respeta su decisión."),
        ex("Una niña dice no a una burla y el grupo la ignora. ¿Hizo mal?", "No", "Actuó con respeto; puede buscar un adulto."),
    ],
    D=[
        ex("Si tienes 3 amigos en tu grupo y se une 1 niño nuevo, ¿cuántos hay?", "4", "3 más 1 es 4."),
        ex("Si un grupo de 6 niños invita a 2 más, ¿cuántos son?", "8", "6 más 2 es 8."),
    ],
    context=[ex("En el recreo, un grupo se ríe de Beto porque usa lentes. Camila no se ríe y le dice a Beto: «Ven con nosotras». ¿Qué hizo Camila?", "Incluyó a Beto y no se burló", "Aplicó el buen trato y la inclusión.")],
    selfcheck=[ex("¿Puedo decir no a una presión?", "Sí", "Puedo decidir por mí mismo."), ex("¿Un grupo bueno respeta mi no?", "Sí", "Respeta mis decisiones."), ex("¿Puedo invitar a alguien solo?", "Sí", "Ayuda a que pertenezca.")],
    task=T("Completa dos frases sobre un grupo al que perteneces (tu familia, tu curso o un grupo de amigos): «Lo que valoro de mi grupo es…» y «Si mi grupo me pide algo que me incomoda, yo…». Añade una forma de invitar a alguien que esté solo.", "Valoro que me ayudan. Si me piden algo que me incomoda, digo no y aviso a un adulto. Invito: «¿Quieres jugar conmigo?»", ["valora su grupo", "sabe decir no", "propone una invitación"], ["frases escritas o dichas"], ["aceptar presiones", "burlarse"], "Reconoce lo que valora y refuerza que decir no es válido."),
    reinforce="Esta semana invita a alguien a jugar.",
    extend="Escribe una frase para decir no a un grupo con respeto y sin pelear.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y lápiz. La lista de útiles y los horarios están escritos en los ejercicios. Si algo no se tiene, se pide ayuda a la profesora, y eso está bien.",
    "Aprenderé a preparar lo que necesito antes de una tarea y a pensar alternativas si algo falta. Sirve para empezar sin apuro y aprender mejor.",
    ["Sé qué útiles uso en clases.", "Sé que ordenar ayuda."],
    [
        "Un hábito es algo que haces seguido hasta que se vuelve parte de tu día. Un buen hábito de aprendizaje es preparar lo necesario antes de empezar. Revisa tu horario y piensa: ¿qué materiales necesito mañana? Así evitas olvidar cosas.",
        "Puedes usar una lista de verificación. Escribe lo que necesitas, como cuaderno, lápiz, goma y estuche. Antes de dormir marca cada uno cuando lo pongas en la mochila. Es mejor preparar la noche anterior que a la hora de salir.",
        "A veces algo falta o se pierde. Tener alternativas ayuda. Si no tienes la goma, puedes pedir una prestada con respeto. Si no tienes un material y no puedes conseguirlo, avisa a tu profesora: pedir ayuda está bien y ella buscará una solución.",
    ],
    [("hábito", "algo que hago seguido y ya es parte de mi día"), ("útiles", "materiales que uso en clases"), ("lista", "papel con las cosas que necesito"), ("alternativa", "otra opción si algo falta"), ("organizar", "poner en orden lo que necesito")],
    [
        W("Revisar la lista", "Mañana hay Artes. Lista: cuaderno, lápiz, témpera, pincel. En la mochila hay cuaderno, lápiz y pincel. ¿Qué falta?", ["Compara lista y mochila.", "Témpera no está en la mochila.", "Falta la témpera."], "La témpera"),
        W("Pensar una alternativa", "Luis olvidó la goma. ¿Qué puede hacer?", ["Puede pedir una prestada.", "Puede avisar a la profesora.", "No debe quedarse sin intentar."], "Pedir una prestada o avisar a la profesora"),
    ],
    [
        M("Dejar la mochila para el último minuto.", "Pensamos que es rápido.", "Prepárala la noche anterior con una lista."),
        M("No decir que me falta algo por vergüenza.", "Sentimos que fallamos.", "Avisar a la profesora ayuda a encontrar una solución."),
    ],
    R=[
        ex("¿Es mejor preparar la mochila la noche anterior?", "Sí", "Evita olvidos y apuros."),
        ex("Una lista de útiles sirve para recordar lo que necesito, ¿verdad?", "Sí", "Ayuda a no olvidar."),
        ex("Si algo falta, ¿puedes avisar a tu profesora?", "Sí", "Ella puede ayudar."),
    ],
    U=[
        ex("En Orientación: ¿Qué es un hábito?", "Algo que hago seguido y ya es parte de mi día", "Se repite hasta ser costumbre."),
        ex("En Orientación: ¿Qué es una alternativa?", "Otra opción si algo falta", "Permite seguir trabajando igual."),
        ex("¿Por qué conviene revisar el horario?", "Para saber qué materiales necesito", "Cada día hay materias distintas."),
    ],
    A=[
        ex("Lista: cuaderno, lápiz, goma, estuche, libro. En la mochila hay 3 de ellos. ¿Cuántos faltan?", "2", "5 menos 3 es 2."),
        ex("Mañana hay Educación Física. Elige qué preparar: zapatillas o una caja de témperas.", "Zapatillas", "En Educación Física se necesita calzado para moverse."),
        ex("Escribe una alternativa si olvidaste tu lápiz.", "Pedir uno prestado a un compañero", "Permite seguir trabajando."),
    ],
    Z=[
        ex("Un niño dice: «No necesito lista, me acuerdo de todo». Un día olvida su cuaderno. ¿Qué le ayudaría?", "Una lista de verificación", "La lista evita olvidos."),
        ex("Una niña no tiene un material y no puede comprarlo. ¿Qué puede hacer?", "Avisar a su profesora", "Hay forma de resolverlo sin culpa."),
    ],
    D=[
        ex("Si preparas 4 materiales cada noche, ¿cuántos preparas en 5 días?", "20", "4 por 5 es 20."),
        ex("Si una lista tiene 8 útiles y ya guardaste 5, ¿cuántos faltan?", "3", "8 menos 5 es 3."),
    ],
    context=[ex("Mañana es martes: Lenguaje, Matemática y Artes. Ema revisa su horario y arma su lista: cuaderno de lenguaje, cuaderno de matemática, estuche y témpera. ¿Hizo bien?", "Sí", "Revisó el horario y preparó la lista.")],
    selfcheck=[ex("¿Preparar la noche anterior ayuda?", "Sí", "Evita olvidos y apuros."), ex("¿Una lista ayuda a recordar?", "Sí", "Marca lo que falta."), ex("¿Se puede avisar si falta algo?", "Sí", "Pedir ayuda está bien.")],
    task=T("Arma tu lista de verificación para mañana con cinco útiles (por ejemplo: cuaderno, lápiz, goma, estuche, botella de agua). Marca los que ya tienes y escribe una alternativa para uno que podría faltar.", "Lista: cuaderno ✓, lápiz ✓, goma ✗, estuche ✓, agua ✓. Alternativa para la goma: pedir una prestada.", ["lista de cinco útiles", "marca lo que tiene", "alternativa para uno"], ["lista escrita o dibujada"], ["no incluir alternativa", "olvidar revisar"], "Reconoce la lista y sugiere preparar la noche anterior."),
    reinforce="Esta noche prepara tu mochila con tu lista.",
    extend="Escribe una lista para una actividad del fin de semana, como ir a la plaza.",
)

lesson(
    OA8, 2,
    "Una hoja y lápiz. Las escenas de salas y mesas están escritas en los ejercicios.",
    "Aprenderé que mantener el orden de la sala y de mis materiales me ayuda a trabajar mejor. Sirve para encontrar lo que necesito y concentrarme.",
    ["Sé guardar mis útiles.", "Sé que las tareas se reparten."],
    [
        "El orden ayuda a aprender. Si tus cosas tienen un lugar, las encuentras rápido y no pierdes tiempo. Un lugar para el cuaderno, uno para el estuche y otro para el libro. Cuando terminas, cada cosa vuelve a su lugar.",
        "Para ordenar, sigue tres pasos. Primero, saca solo lo que usarás. Segundo, al terminar, guarda cada cosa en su lugar. Tercero, mira tu mesa para ver que quedó despejada. Esto se puede hacer en un minuto si lo haces todos los días.",
        "La sala es de todos. Si cada uno ordena su espacio y ayuda con los materiales comunes, la sala se mantiene agradable. A veces se suelta un lápiz o se cae un papel. Recogerlo es parte del orden. Si el desorden te cuesta, pide ayuda y prueba un método más simple.",
    ],
    [("orden", "cada cosa en su lugar"), ("despejado", "sin cosas que estorben"), ("material", "cosa que uso para aprender"), ("método", "forma de hacer algo paso a paso"), ("común", "de todos")],
    [
        W("Los tres pasos", "Pía sacó solo lo que necesitaba para dibujar. Ahora termina y tiene lápices, hojas y un estuche sobre la mesa. ¿Qué dos pasos le faltan para ordenar?", ["El primer paso, sacar solo lo que usa, ya lo hizo.", "Segundo: guarda cada cosa en su lugar.", "Tercero: revisa la mesa."], "Guardar cada cosa en su lugar y revisar que la mesa quedó despejada"),
        W("Encontrar rápido", "Tomás guarda su estuche siempre en el mismo bolsillo de la mochila. ¿Por qué lo encuentra rápido?", ["Siempre está en el mismo sitio.", "No tiene que buscar.", "Tiene un lugar asignado."], "Porque siempre está en su lugar"),
    ],
    [
        M("Dejar los materiales sobre la mesa pensando «los guardo después».", "El desorden parece pequeño.", "Guárdalos en cuanto termines."),
        M("Pensar que el orden de la sala es solo de la profesora.", "Creemos que ella ordena.", "Todos ayudan a mantener la sala."),
    ],
    R=[
        ex("¿Cada cosa debe tener un lugar?", "Sí", "Así se encuentra rápido."),
        ex("¿Se guarda lo que se terminó de usar?", "Sí", "Mantiene la mesa despejada."),
        ex("¿La sala es de todos?", "Sí", "Entre todos la cuidamos."),
    ],
    U=[
        ex("¿Cuáles son los tres pasos para ordenar?", "Sacar solo lo que uso, guardar al terminar y revisar la mesa", "Son los pasos de la explicación."),
        ex("¿Por qué ayuda el orden a aprender?", "Porque encuentro rápido lo que necesito", "Ahorra tiempo y distracciones."),
        ex("¿Recoger un papel del piso es parte del orden?", "Sí", "Mantiene la sala cuidada."),
    ],
    A=[
        ex("En la mesa de Ana hay 6 cosas y guarda 4. ¿Cuántas quedan sobre la mesa?", "2", "6 menos 4 es 2."),
        ex("Rosa sacó solo el cuaderno de Lenguaje para la clase. ¿Hizo bien?", "Sí", "Sacó solo lo que necesita."),
        ex("Elige dónde guardar el estuche: en la mochila o en el piso.", "En la mochila", "Es su lugar."),
    ],
    Z=[
        ex("Dos niños tienen la mesa con 10 cosas cada uno. Uno encuentra su lápiz en 5 segundos y otro en 2 minutos. ¿Quién tiene mejor orden?", "El que lo encontró en 5 segundos", "Encontró más rápido."),
        ex("Un niño con dificultades para ordenar pide un método más simple. ¿Está bien?", "Sí", "Cada uno puede necesitar un método distinto."),
    ],
    D=[
        ex("Si ordenar toma 1 minuto cada día, ¿cuántos minutos son en 5 días?", "5", "1 más 1 más 1 más 1 más 1 es 5."),
        ex("Si se pierde un lápiz por cada día de desorden, ¿cuántos se pierden en 3 días?", "3", "1 más 1 más 1 es 3."),
    ],
    context=[ex("Al terminar la clase de arte, Luis deja los pinceles, los papeles y las pinturas sobre la mesa. El curso siguiente llega y no tiene dónde trabajar. ¿Qué debió hacer Luis?", "Guardar y limpiar su espacio", "El espacio es compartido.")],
    selfcheck=[ex("¿El orden ayuda a aprender?", "Sí", "Se encuentra rápido lo que se necesita."), ex("¿La sala la ordenan solo los adultos?", "No", "Todos ayudan a ordenar."), ex("¿Cada cosa tiene su lugar?", "Sí", "Así se evita perderla.")],
    task=T("Dibuja o escribe un plan de orden para tu mesa de estudio o tu mochila con tres pasos y un lugar para cada cosa (cuaderno, estuche, libro). Si no tienes mesa, usa el lugar donde haces tus tareas.", "Paso 1: saco solo el cuaderno. Paso 2: al terminar guardo cada cosa. Paso 3: reviso la mesa. Lugares: cuaderno en el bolsillo grande, estuche en el pequeño.", ["tres pasos", "un lugar para cada cosa", "método posible de repetir"], ["plan escrito o dibujado"], ["pasos demasiado largos", "no asignar lugares"], "Reconoce el plan y sugiere probarlo tres días seguidos."),
    reinforce="Hoy ordena tu mesa con los tres pasos.",
    extend="Anota cuánto tiempo toma ordenar y si bajó después de tres días.",
)

lesson(
    OA8, 3,
    "Una hoja y lápiz. Las situaciones con útiles y préstamos están escritas en los ejercicios. Cada familia tiene posibilidades distintas, y eso se respeta.",
    "Aprenderé a cuidar mis útiles y los de otros, y a devolver lo prestado a tiempo. Sirve para que los materiales duren y para confiar entre compañeros.",
    ["Sé que debo pedir permiso para usar algo ajeno.", "Sé que ordenar ayuda."],
    [
        "Cuidar tus útiles significa usarlos con cuidado: tapar los plumones, guardar los lápices, no morder la goma y no rayar los libros. Algunos útiles conviene marcarlos con tu nombre, así si se pierden pueden volver a ti.",
        "Cuando pides prestado, cuidas y devuelves. Di cuándo lo devolverás y cumple. Si se te olvida, devuélvelo apenas lo recuerdes y pide disculpas. Si algo se rompe, avisa y ofrece ayuda. No todos los útiles son nuevos o iguales, y eso no importa: lo importante es cuidarlos.",
        "Cada familia tiene posibilidades distintas. No te burles de los útiles de otros ni los compares. Si te falta un útil o se te gastó y no puedes reponerlo, avisa a tu profesora. Ella puede buscar una solución. Pedir ayuda es una forma responsable de cuidar tu aprendizaje.",
    ],
    [("cuidar", "usar con atención para que no se dañe"), ("marcar", "poner el nombre en un útil"), ("prestar", "dejar que otro use algo mío"), ("devolver", "entregar de vuelta lo prestado"), ("reponer", "conseguir otro igual")],
    [
        W("Cumplir con la devolución", "Beto pidió prestada una regla hasta el miércoles. Hoy es jueves. ¿Qué debe hacer?", ["Se pasó un día.", "Debe devolverla hoy.", "Y pedir disculpas."], "Devolverla hoy y pedir disculpas"),
        W("Marcar útiles", "Ema tiene un estuche igual al de otros. ¿Cómo puede reconocerlo?", ["Puede ponerle su nombre.", "Así no se confunde.", "También sirve un adhesivo con su nombre."], "Poniéndole su nombre"),
    ],
    [
        M("Prestar y no recordar a quién.", "No lo anoto.", "Anota o recuerda a quién prestaste."),
        M("Burlarme de los útiles gastados de otro.", "Comparo con lo nuevo.", "Cuida lo tuyo y respeta lo de los demás."),
    ],
    R=[
        ex("¿Se deben cuidar los útiles?", "Sí", "Así duran más."),
        ex("Si pides algo prestado, ¿lo devuelves?", "Sí", "Es una forma de respeto."),
        ex("¿Poner el nombre ayuda a no perder?", "Sí", "Puede volver a su dueño."),
    ],
    U=[
        ex("¿Qué haces si se te olvida devolver algo?", "Lo devuelvo apenas lo recuerdo y pido disculpas", "Repara el descuido."),
        ex("¿Está bien comparar los útiles de unos con los de otros para burlarse?", "No", "Cada familia tiene posibilidades distintas."),
        ex("Si te falta un útil y no puedes reponerlo, ¿qué haces?", "Aviso a mi profesora", "Ella puede buscar una solución."),
    ],
    A=[
        ex("Pedro prestó 3 lápices y le devolvieron 2. ¿Cuántos faltan?", "1", "3 menos 2 es 1."),
        ex("Rosa tapa el plumón después de usarlo. ¿Hizo bien?", "Sí", "Así no se seca."),
        ex("Escribe una frase para pedir prestada una tijera y decir cuándo la devolverás.", "¿Me prestas tu tijera hasta el recreo?", "Pide y dice cuándo la devuelve."),
    ],
    Z=[
        ex("Un niño dice: «Si pierdo algo, no digo nada». ¿Qué pasa si no avisa?", "No se puede buscar ni arreglar", "Avisar ayuda a encontrar o reparar."),
        ex("Una niña usa una mochila muy gastada y alguien ríe. ¿Qué falta en esa risa?", "Respeto", "Burlarse no es buen trato."),
    ],
    D=[
        ex("Si el curso tiene 20 gomas y 5 están marcadas, ¿cuántas no están marcadas?", "15", "20 menos 5 es 15."),
        ex("Si cada día devuelves 2 útiles prestados, ¿cuántos devuelves en 2 días?", "4", "2 más 2 es 4."),
    ],
    context=[ex("Camila pidió prestado el libro de Luis hasta el viernes. El viernes lo devolvió con una hoja doblada. Luis dijo «gracias». ¿Cumplió Camila?", "Sí, aunque debería cuidarlo más", "Lo devolvió a tiempo.")],
    selfcheck=[ex("¿Hay que cuidar lo prestado?", "Sí", "Es de otra persona."), ex("¿Se devuelve a tiempo?", "Sí", "Cumple lo acordado."), ex("¿Puedo avisar si me falta un útil?", "Sí", "La profesora puede ayudar.")],
    task=T("Escribe tres acciones para cuidar tus útiles y una frase para pedir algo prestado diciendo cuándo lo devolverás. Si hay un útil que te falta, escribe cómo se lo dirías a tu profesora.", "Acciones: tapar los plumones, marcar mi estuche, guardar los lápices. Frase: «¿Me prestas tu goma hasta el recreo?» Profesora: «Me falta un cuaderno, ¿me puede ayudar?»", ["tres acciones de cuidado", "frase para prestar con plazo", "frase para pedir ayuda"], ["frases escritas o dichas"], ["no mencionar el plazo", "burlarse de otros útiles"], "Reconoce las acciones y refuerza que pedir ayuda es responsable."),
    reinforce="Marca con tu nombre un útil que aún no lo tenga.",
    extend="Escribe una regla del curso para préstamos de materiales.",
)

lesson(
    OA8, 4,
    "Una hoja y lápiz. Las listas de antes y ahora están escritas en los ejercicios.",
    "Aprenderé a reconocer lo que he aprendido comparando mi antes con mi ahora. Sirve para sentirme motivado y ver mi progreso.",
    ["Sé que las habilidades se aprenden con práctica.", "Sé comparar conmigo mismo."],
    [
        "Un aprendizaje es algo que ahora sabes o puedes hacer y antes no. Puede ser leer una palabra nueva, restar 10 menos 4, atarte los cordones o conversar en inglés con un saludo. Reconocer tus aprendizajes te da ganas de seguir.",
        "Para verlos, usa la pregunta «antes y ahora». Antes no podía contar de 5 en 5. Ahora sí puedo. Compara contigo mismo, no con los demás. Cada persona avanza a su ritmo y en distintas cosas. Tu avance es tuyo.",
        "También ayuda anotar tus logros. Un cuaderno de aprendizajes puede tener tres columnas: qué aprendí, cómo lo aprendí y cómo me sentí. Mirar esa lista cuando algo cuesta te recuerda que ya lograste cosas parecidas. Eso se llama motivación.",
    ],
    [("aprendizaje", "algo que ahora sé y antes no sabía"), ("progreso", "avance que se nota"), ("logro", "algo que conseguí"), ("motivación", "ganas de seguir aprendiendo"), ("antes y ahora", "forma de comparar mi avance")],
    [
        W("Antes y ahora", "Antes Pía leía una palabra por minuto. Ahora lee 5 palabras por minuto. ¿Cuántas más lee?", ["Ahora: 5.", "Antes: 1.", "5 menos 1 es 4."], "4 palabras más por minuto"),
        W("Qué aprendí", "Tomás dice: «Aprendí a restar con los dedos y con dibujos». ¿Qué aprendizaje nombra?", ["Habla de restar.", "Dice cómo lo aprendió.", "Aprendió a restar."], "Aprendió a restar"),
    ],
    [
        M("Decir «no aprendí nada» porque no soy el mejor.", "Comparo con otros.", "Mira tu antes y tu ahora."),
        M("Pensar que solo cuenta lo que sale perfecto.", "Esperamos resultados grandes.", "Los avances pequeños también son aprendizaje."),
    ],
    R=[
        ex("¿Un aprendizaje es algo que ahora sé y antes no?", "Sí", "Esa es la idea."),
        ex("Para reconocer lo que aprendí, ¿comparo con otro o conmigo?", "Conmigo", "Mi antes y mi ahora."),
        ex("¿Los avances pequeños cuentan?", "Sí", "Todo avance es aprendizaje."),
    ],
    U=[
        ex("¿Qué es la motivación?", "Ganas de seguir aprendiendo", "Me anima a seguir."),
        ex("¿Qué tres columnas puede tener un cuaderno de aprendizajes?", "Qué aprendí, cómo lo aprendí y cómo me sentí", "Reúne la información."),
        ex("Si algo me cuesta, ¿ayuda recordar lo que ya logré?", "Sí", "Recuerda que puedo aprender."),
    ],
    A=[
        ex("Antes Ema saltaba la cuerda 2 veces y ahora 7. ¿Cuántas más salta?", "5", "7 menos 2 es 5."),
        ex("Escribe un aprendizaje tuyo con «antes… ahora…».", "Antes no sabía atarme los cordones; ahora sí", "Muestra el avance."),
        ex("Un niño anota: «Aprendí a sumar con apoyo de dibujos». ¿Qué columna llenó: qué aprendí o cómo lo aprendí?", "Ambas", "Dice qué aprendió y cómo."),
    ],
    Z=[
        ex("Un niño leyó 1 libro este mes y dice: «No aprendí nada porque otros leyeron 3». ¿Es cierto?", "No", "Leer un libro también es un aprendizaje, y el avance se compara con uno mismo."),
        ex("Una niña ve que no ha mejorado en una cosa pero sí en otra. ¿Qué puede decir?", "En esta avancé y en esta todavía practico", "Reconoce avances y lo pendiente."),
    ],
    D=[
        ex("Si anotas 2 aprendizajes por semana, ¿cuántos anotas en 4 semanas?", "8", "2 más 2 más 2 más 2 es 8."),
        ex("Si el mes pasado tenías 5 aprendizajes anotados y ahora 9, ¿cuántos más?", "4", "9 menos 5 es 4."),
    ],
    context=[ex("Luis dice: «Matemática me cuesta». Su profesora le muestra su cuaderno de hace dos meses y el de ahora: antes sumaba hasta 10 y ahora suma hasta 20. ¿Qué descubre Luis?", "Que avanzó", "Compara su antes y su ahora.")],
    selfcheck=[ex("¿Comparo mi avance conmigo?", "Sí", "Con mi antes."), ex("¿Cuentan los avances pequeños?", "Sí", "Todo avance vale."), ex("¿Anotar logros motiva?", "Sí", "Recuerda lo que ya logré.")],
    task=T("Arma tu cuaderno de aprendizajes con tres filas. En cada una escribe: qué aprendí, cómo lo aprendí y cómo me sentí. Si no se te ocurre, usa estas ideas: leer una palabra nueva, restar, atarme los cordones, hacer un amigo.", "Aprendí a atarme los cordones. Lo aprendí practicando con mi papá. Me sentí orgullosa.", ["tres aprendizajes", "tres columnas", "compara consigo mismo"], ["tabla escrita o dibujada"], ["compararse con otros", "solo anotar cosas perfectas"], "Reconoce cada aprendizaje y pregunta cuál le dio más orgullo."),
    reinforce="Cada día anota un aprendizaje, aunque sea pequeño.",
    extend="Elige un aprendizaje del año pasado y compáralo con lo que sabes hoy.",
)

lesson(
    OA8, 5,
    "Una hoja y lápiz. Las metas de ejemplo y las situaciones están escritas en los ejercicios.",
    "Aprenderé a elegir un próximo paso pequeño para seguir aprendiendo y a mantener mi motivación. Sirve para continuar con ganas y sin apuro.",
    ["Sé reconocer lo que he aprendido.", "Sé armar un plan de pasos pequeños."],
    [
        "Después de reconocer lo que aprendiste, puedes elegir qué aprender a continuación. Se llama próximo paso. Un buen próximo paso es pequeño, claro y posible esta semana. Por ejemplo: «Voy a leer una página de un libro cada día».",
        "Una meta tiene tres características. Es concreta: dice qué harás. Es medible: puedes ver si la lograste. Y es posible: la puedes hacer con tu tiempo y tus apoyos. «Ser el mejor» no es una meta posible. «Aprender la tabla del 2» sí lo es.",
        "Mantener la motivación es más fácil si celebras los avances, practicas un poco cada día y pides ayuda cuando la necesitas. Si te cansas, descansa y vuelve. Si una meta resulta muy grande, la divides en pasos más chicos. Equivocarse es parte del camino.",
    ],
    [("meta", "lo que quiero lograr"), ("próximo paso", "lo siguiente que voy a hacer"), ("concreta", "que dice exactamente qué haré"), ("medible", "que puedo ver si la logré"), ("celebrar", "alegrarme por un avance")],
    [
        W("Meta concreta", "¿Cuál es una meta concreta: «Ser mejor» o «Leer una página cada día»?", ["«Ser mejor» no dice qué haré.", "«Leer una página cada día» dice qué y cuánto.", "Elige la que se puede ver."], "«Leer una página cada día»"),
        W("Dividir una meta", "Sofía quiere aprender las tablas del 2, del 5 y del 10, pero es mucho. ¿Cómo puede empezar?", ["La meta es grande.", "Puede dividirla.", "Primero la tabla del 2."], "Empezar por la tabla del 2"),
    ],
    [
        M("Elegir una meta enorme que no puedo cumplir.", "Queremos lograr todo rápido.", "Elige un paso pequeño para esta semana."),
        M("Rendirme el primer día que no me sale.", "Esperamos resultados inmediatos.", "Descansa, vuelve y celebra los avances pequeños."),
    ],
    R=[
        ex("¿Un buen próximo paso es pequeño?", "Sí", "Así se puede cumplir."),
        ex("¿Se puede celebrar un avance pequeño?", "Sí", "Ayuda a mantener la motivación."),
        ex("Si una meta es muy grande, ¿se divide?", "Sí", "En pasos más chicos."),
    ],
    U=[
        ex("¿Cuáles son las tres características de una meta buena?", "Concreta, medible y posible", "Así se puede lograr."),
        ex("¿Qué haces si te cansas?", "Descanso y vuelvo", "Descansar no es rendirse."),
        ex("¿Pedir ayuda sirve para mantener la motivación?", "Sí", "Con apoyo es más fácil seguir."),
    ],
    A=[
        ex("Ema lee 2 páginas cada día durante 5 días. ¿Cuántas páginas lee en total?", "10", "2 más 2 más 2 más 2 más 2 es 10."),
        ex("Elige la meta concreta: «Escribir mi nombre completo sin mirar» o «Ser genial».", "«Escribir mi nombre completo sin mirar»", "Dice qué haré y se puede ver."),
        ex("Escribe un próximo paso pequeño para aprender a restar.", "Hacer 3 restas al día", "Es concreto y posible."),
    ],
    Z=[
        ex("Un niño dice: «Mi meta es sacarme siempre un 7». ¿Qué le falta a la meta?", "Ser concreta sobre qué hará para lograrlo", "Dice un resultado, no una acción."),
        ex("Una niña no logró su meta esta semana. ¿Qué puede hacer?", "Revisar si era muy grande y hacerla más pequeña", "Ajustar ayuda a avanzar."),
    ],
    D=[
        ex("Si practicas 5 minutos al día durante 6 días, ¿cuántos minutos practicaste?", "30", "5 más 5 más 5 más 5 más 5 más 5 es 30."),
        ex("Si tu meta es leer 12 páginas y llevas 7, ¿cuántas faltan?", "5", "12 menos 7 es 5."),
    ],
    context=[ex("Pablo quiere aprender a andar en bicicleta. Su papá le propone: «Esta semana, 10 minutos al día en el patio con tus zapatillas». ¿Es una buena meta?", "Sí", "Es concreta, medible y posible.")],
    selfcheck=[ex("¿Un próximo paso es pequeño?", "Sí", "Para poder cumplirlo."), ex("¿Una meta es concreta?", "Sí", "Dice qué haré."), ex("¿Puedo celebrar avances?", "Sí", "Mantiene la motivación.")],
    task=T("Elige tu próximo paso para aprender algo (leer, matemática, un deporte, cantar, dibujar). Escribe tu meta con las tres características, el primer paso, cómo sabrás que la lograste y cómo la celebrarás.", "Meta: leer una página cada día. Primer paso: leer hoy después de la once. La logré si marco 5 días. Celebro: se lo cuento a mi familia.", ["meta concreta", "medible", "posible", "celebración"], ["meta escrita o dibujada"], ["meta enorme", "sin forma de medir"], "Reconoce la meta y sugiere revisarla en una semana."),
    reinforce="Cumple hoy el primer paso de tu meta.",
    extend="Escribe cómo cambiarías tu meta si la semana te resulta difícil.",
)

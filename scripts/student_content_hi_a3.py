"""Material del estudiante de 1.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (símbolos y conmemoraciones) y OA 06 (expresiones culturales)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA5, OA6 = "HI01 OA 05", "HI01 OA 06"

FLAG = ("Descripción de la bandera de Chile: tiene dos franjas horizontales iguales; la de arriba es blanca y la de abajo es roja; "
        "arriba a la izquierda hay un cuadrado azul con una estrella blanca de cinco puntas.")
ESC = ("Descripción del escudo de Chile: tiene un escudo en el centro dividido en una parte azul y otra roja, con una estrella blanca de cinco puntas; "
       "a los lados hay un cóndor y un huemul; sobre el escudo hay tres plumas, una azul, una blanca y una roja; abajo se lee el lema «Por la razón o la fuerza».")

# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Lápiz, papel y lápices de colores azul, rojo y negro. Las descripciones de los símbolos están escritas en cada ejercicio.",
    use="Aprenderé a reconocer la bandera, el escudo y el himno de Chile. Sirve para saber qué cosas representan a nuestro país.",
    prior=["Sé nombrar los colores.", "Sé contar hasta 5."],
    explain=[
        "Un símbolo es un objeto o una canción que representa algo. Los símbolos que representan a Chile son tres: la bandera, el escudo y el himno nacional. Los vemos en las escuelas, en los edificios públicos y en las fiestas del país.",
        "La bandera tiene tres colores: azul, blanco y rojo. Tiene una estrella blanca de cinco puntas. El escudo tiene un cóndor y un huemul, que son animales de Chile, y una cinta con el lema «Por la razón o la fuerza». El himno es una canción con letra y música.",
        "La letra del himno nacional actual la escribió Eusebio Lillo y la música la compuso Ramón Carnicer. Cuando suena el himno nacional, las personas se ponen de pie en señal de respeto. Es una forma de mostrar que cuidamos lo que nos une como país.",
    ],
    vocab=[("símbolo", "algo que representa a otra cosa"), ("bandera", "tela con colores y dibujos que representa a un país"), ("escudo", "dibujo con animales y figuras que representa al país"), ("himno", "canción que representa a un país"), ("lema", "frase corta que acompaña un escudo")],
    worked=[
        {"title": "Reconocer la bandera", "problem": f"{FLAG} ¿De qué color es la franja de abajo?", "steps": ["Leo la descripción.", "Dice que la franja de abajo es roja."], "answer": "Roja"},
        {"title": "Reconocer el escudo", "problem": f"{ESC} ¿Qué animales tiene?", "steps": ["Busco la parte que habla de los lados.", "Hay un cóndor y un huemul."], "answer": "Un cóndor y un huemul"},
    ],
    mistakes=[
        {"wrong": "Confundir bandera y escudo.", "why": "Los dos tienen la estrella y los colores.", "fix": "La bandera es de tela con franjas; el escudo tiene animales y un lema."},
        {"wrong": "Decir que el himno es un dibujo.", "why": "Se piensa que todos los símbolos se ven.", "fix": "El himno se escucha o se canta: es música con letra."},
    ],
    tiers={
        "recovery": [
            ex(f"{FLAG} ¿Cuántos colores tiene la bandera?", "3", "Tiene azul, blanco y rojo."),
            ex(f"{FLAG} ¿Cuántas puntas tiene la estrella?", "5", "La descripción dice cinco puntas."),
            ex("¿Cuál de estos tres símbolos de Chile es una canción: bandera, escudo o himno?", "himno", "El himno es música con letra."),
        ],
        "understand": [
            ex("En Historia: ¿Qué es un símbolo?", "Algo que representa a otra cosa", "Una bandera, por ejemplo, representa a un país."),
            ex(f"{ESC} ¿Cuántos animales aparecen en el escudo?", "2", "Son el cóndor y el huemul."),
            ex("¿Qué hacen las personas cuando suena el himno nacional?", "Se ponen de pie en señal de respeto", "Es una forma de honrar un símbolo del país."),
        ],
        "apply": [
            ex(f"{FLAG} ¿Dónde está el cuadrado azul?", "arriba a la izquierda", "Así lo dice la descripción."),
            ex(f"{ESC} ¿Qué frase aparece escrita abajo?", "Por la razón o la fuerza", "Es el lema del escudo."),
            ex("¿Quién escribió la letra del himno nacional actual: Eusebio Lillo o Ramón Carnicer?", "Eusebio Lillo", "Carnicer compuso la música."),
        ],
        "reason": [
            ex(f"{FLAG} Mateo dice que la bandera tiene una franja negra. ¿Tiene razón?", "No; sus colores son azul, blanco y rojo", "No aparece el negro."),
            ex("Una niña dibuja una bandera con un cóndor y un huemul. ¿Dibujó la bandera o el escudo?", "el escudo", "Los animales están en el escudo."),
        ],
        "challenge": [
            ex(f"{FLAG} Si pintas la franja de abajo y el cuadrado, ¿qué dos colores necesitas?", "rojo y azul", "La franja de abajo es roja y el cuadrado es azul."),
            arith("En la bandera hay 1 estrella y en el escudo hay 1 estrella. ¿Cuántas estrellas hay entre los dos símbolos?", "1+1", "Se suma la estrella de cada símbolo."),
        ],
    },
    context=[ex("En el acto de la escuela, los niños se ponen de pie y cantan una canción que representa a Chile. ¿Qué símbolo patrio están cantando?", "el himno nacional", "El himno es la canción de Chile.")],
    selfcheck=[
        ex("¿Cuántos símbolos de Chile estudiamos hoy?", "3", "Son bandera, escudo e himno."),
        ex(f"{FLAG} ¿De qué color es la franja de arriba?", "blanca", "La descripción dice que la de arriba es blanca."),
        ex("¿Qué lema aparece en el escudo de Chile?", "Por la razón o la fuerza", "Es la frase de la cinta."),
    ],
    open_task=task("Dibuja la bandera de Chile con estas indicaciones: dos franjas horizontales (arriba blanca, abajo roja), un cuadrado azul arriba a la izquierda y una estrella blanca de cinco puntas dentro del cuadrado. Escribe debajo el nombre de los otros dos símbolos patrios.", "Bandera dibujada con franja blanca arriba, franja roja abajo, cuadrado azul y estrella blanca. Debajo: escudo e himno nacional.", ["dos franjas correctas", "cuadrado azul con estrella", "nombra escudo e himno"], ["dibujo de la bandera con su leyenda"], ["poner la franja roja arriba", "estrella de seis puntas"], "Pide que señale con el dedo cada color y diga cuántas puntas tiene la estrella."),
    reinforce="Busca en tu casa o en la calle una bandera y cuenta cuántos colores tiene.",
    extend="Dibuja el escudo siguiendo la descripción y escribe el lema.",
)

register(
    OA5, 2,
    materials="Lápiz y papel. Las descripciones de la bandera y el escudo están escritas en cada ejercicio.",
    use="Aprenderé a describir lo que veo en la bandera y el escudo sin inventar significados. Sirve para hablar con exactitud de los símbolos.",
    prior=["Sé nombrar los símbolos patrios.", "Sé describir colores y formas."],
    explain=[
        "Para describir un símbolo, primero decimos lo que vemos: colores, formas, cuántos hay y dónde están. Eso son observaciones y se pueden comprobar mirando. Por ejemplo: «La estrella de la bandera es blanca y tiene cinco puntas». Una opinión es lo que alguien piensa o siente, como «es la más linda»; no se puede comprobar mirando.",
        "Después hay significados: lo que ese elemento quiere decir. Muchos significados se enseñan en la escuela: por ejemplo, tradicionalmente se dice que el azul recuerda el cielo, y que el blanco recuerda la nieve de la cordillera de los Andes. Pero esos significados no se ven en el dibujo; se aprenden de una fuente.",
        "No inventes significados. Si no sabes qué quiere decir un color, di «no lo sé» y pregunta a un adulto o busca en un libro. En la bandera se ve una estrella; el escudo muestra un cóndor y un huemul, dos animales que viven en el territorio de Chile.",
    ],
    vocab=[("observar", "mirar con atención y decir lo que se ve"), ("describir", "decir cómo es algo"), ("significado", "lo que algo quiere decir"), ("inventar", "decir algo sin saber si es cierto"), ("fuente", "libro o persona de donde viene la información")],
    worked=[
        {"title": "Observación", "problem": "«La franja de abajo de la bandera es roja». ¿Es una observación o un significado?", "steps": ["Se puede comprobar mirando la bandera.", "Entonces es una observación."], "answer": "Es una observación"},
        {"title": "Significado", "problem": "«El blanco recuerda la nieve de la cordillera». ¿Se ve en el dibujo o se aprende de una fuente?", "steps": ["En el dibujo solo se ve el color blanco.", "Que recuerda la nieve se aprende de un libro o de un adulto."], "answer": "Se aprende de una fuente"},
    ],
    mistakes=[
        {"wrong": "Decir lo que el color significa sin saberlo.", "why": "Se quiere responder rápido.", "fix": "Si no lo sabes, di «no lo sé» y averigua en una fuente."},
        {"wrong": "Mezclar lo que se ve con lo que se cree.", "why": "Se habla de ambos como si fueran lo mismo.", "fix": "Primero describe lo que ves; después, di el significado y de dónde viene."},
    ],
    tiers={
        "recovery": [
            ex(f"{FLAG} ¿Cuántas franjas tiene la bandera?", "2", "La descripción dice dos franjas."),
            ex("«La estrella de la bandera tiene cinco puntas». ¿Se puede comprobar mirando?", "Sí", "Se cuentan las puntas en el dibujo."),
            ex(f"{ESC} ¿De qué colores son las tres plumas?", "azul, blanco y rojo", "Así lo dice la descripción."),
        ],
        "understand": [
            ex("En Historia: ¿Qué es una observación?", "Lo que se ve y se puede comprobar", "Se afirma mirando."),
            ex("¿Qué es un significado?", "Lo que algo quiere decir", "No siempre se ve en el dibujo."),
            ex("¿Por qué no se debe inventar el significado de un color?", "Porque puede ser falso", "Hay que usar una fuente."),
        ],
        "apply": [
            ex("Clasifica como observación u opinión: «La bandera tiene tres colores».", "observación", "Se cuenta mirando la bandera."),
            ex("Clasifica como observación u opinión: «La bandera es la más linda del mundo».", "opinión", "Es lo que alguien piensa, no se comprueba."),
            ex("Clasifica como observación o significado: «El escudo tiene un cóndor y un huemul».", "observación", "Se puede comprobar mirando el escudo."),
        ],
        "reason": [
            ex("Una niña dice: «El rojo de la bandera significa que todos somos valientes». Nadie le enseñó eso. ¿Qué debería decir?", "Que no lo sabe y que lo pregunta a una fuente", "No se deben inventar significados."),
            ex(f"{FLAG} Un niño dice que la estrella está abajo. ¿Qué lo corrige: observación o significado?", "observación", "Mirando la bandera se ve que la estrella está arriba."),
        ],
        "challenge": [
            ex(f"{ESC} Escribe dos observaciones del escudo.", "Tiene un cóndor y un huemul; tiene tres plumas", "Son cosas que se pueden comprobar mirando."),
            ex("Se enseña que el blanco de la bandera recuerda la nieve de los Andes. ¿Es una observación o un significado enseñado?", "un significado enseñado", "No se ve en el dibujo."),
        ],
    },
    context=[ex("La profesora pregunta: «¿Qué ven en el escudo?». Camila dice «un cóndor». Pedro dice «el cóndor es el rey de los animales». ¿Cuál respuesta es una observación?", "la de Camila", "Se ve un cóndor; lo de Pedro es una idea.")],
    selfcheck=[
        ex("¿Describir es decir cómo es algo?", "Sí", "Se usan colores, formas y número."),
        ex(f"{FLAG} Escribe una observación sobre la bandera.", "Por ejemplo: tiene una estrella de cinco puntas", "Es algo que se ve."),
        ex("Si no sabes qué significa un símbolo, ¿qué haces?", "pregunto a una fuente", "Así no invento."),
    ],
    open_task=task("Completa una tabla con dos columnas: lo que veo y lo que me enseñaron. Para la bandera, anota en la primera columna estas tres observaciones: tiene dos franjas, hay una estrella de cinco puntas, hay un cuadrado azul. En la segunda columna anota un significado que te hayan enseñado y quién te lo enseñó (por ejemplo: mi profesora me dijo que el blanco recuerda la nieve de los Andes).", "Veo: dos franjas; estrella de cinco puntas; cuadrado azul. Me enseñaron: el blanco recuerda la nieve de la cordillera (mi profesora).", ["tres observaciones", "un significado con su fuente", "no inventa"], ["tabla de dos columnas"], ["poner opiniones en la columna de observaciones", "no indicar la fuente"], "Pide que explique cómo sabe cada observación."),
    reinforce="Mira tu bandera de la escuela y describe tres cosas que ves.",
    extend="Pregunta a un adulto qué le enseñaron sobre los colores de la bandera y anótalo con su nombre.",
)

register(
    OA5, 3,
    materials="Lápiz y papel. La cronología de las conmemoraciones está escrita en cada ejercicio.",
    use="Aprenderé qué se recuerda en Fiestas Patrias, el 12 de octubre y el 21 de mayo, y que cada hecho se puede ver desde distintas perspectivas. Sirve para entender por qué celebramos esos días.",
    prior=["Sé leer fechas con día, mes y año.", "Sé que hay días especiales en el año."],
    explain=[
        "Una conmemoración es un día en que recordamos un hecho importante. Tres conmemoraciones de Chile son: las Fiestas Patrias del 18 y 19 de septiembre, el Día del Descubrimiento de dos mundos o Encuentro de Dos Mundos el 12 de octubre, y el Combate Naval de Iquique el 21 de mayo.",
        "El 18 de septiembre de 1810 se formó en Santiago la Primera Junta Nacional de Gobierno. Se recuerda como un paso hacia la independencia. El 12 de octubre de 1492 el navegante Cristóbal Colón llegó a una isla de América. El 21 de mayo de 1879, frente a Iquique, la corbeta chilena Esmeralda (un tipo de barco), al mando de Arturo Prat, fue atacada por el Huáscar, un barco peruano. Fue durante la Guerra del Pacífico.",
        "Una cronología simple ordena esos hechos por fecha: 12 de octubre de 1492, 18 de septiembre de 1810 y 21 de mayo de 1879. Un mismo hecho se puede mirar desde distintas perspectivas: los pueblos que ya vivían en América, los europeos que llegaron, y las personas de otros países cuentan la historia de distinta manera. Aprender a escuchar varias voces nos ayuda a entender mejor.",
    ],
    vocab=[("conmemoración", "día en que se recuerda un hecho importante"), ("cronología", "hechos ordenados por fecha"), ("perspectiva", "forma en que una persona mira un hecho"), ("Fiestas Patrias", "conmemoración de septiembre"), ("combate", "lucha entre dos grupos")],
    worked=[
        {"title": "Ordenar por fecha", "problem": "Ordena de más antiguo a más nuevo: 21 de mayo de 1879, 12 de octubre de 1492, 18 de septiembre de 1810.", "steps": ["Miro primero los años: 1492, 1810 y 1879.", "El menor es el más antiguo."], "answer": "12 de octubre de 1492; 18 de septiembre de 1810; 21 de mayo de 1879"},
        {"title": "Perspectivas", "problem": "El 12 de octubre de 1492 los europeos dicen que «descubrieron» tierras. ¿Qué pueden decir los pueblos que ya vivían aquí?", "steps": ["Esos pueblos ya conocían esas tierras.", "Para ellos no fue un descubrimiento, sino la llegada de personas nuevas."], "answer": "Que esas tierras ya eran conocidas y habitadas"},
    ],
    mistakes=[
        {"wrong": "Creer que hay una sola forma de contar un hecho.", "why": "Se escucha una sola voz.", "fix": "Pregunta: ¿quién cuenta? ¿Qué cuentan otras personas?"},
        {"wrong": "Mezclar las fechas de las conmemoraciones.", "why": "Todas se parecen en que hay feriado.", "fix": "Asocia cada fecha con un hecho: 18 de septiembre, Primera Junta; 21 de mayo, Combate de Iquique."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué mes son las Fiestas Patrias?", "septiembre", "Se celebran el 18 y el 19 de septiembre."),
            ex("¿En qué mes se recuerda el Combate Naval de Iquique?", "mayo", "Fue el 21 de mayo de 1879."),
            ex("¿En qué mes es el 12 de octubre?", "octubre", "El mes aparece en el nombre de la fecha."),
        ],
        "understand": [
            ex("¿Qué es una conmemoración?", "Un día en que se recuerda un hecho importante", "Se hace para no olvidar lo que pasó."),
            ex("¿Qué barco chileno participó en el Combate Naval de Iquique?", "la corbeta Esmeralda", "Estaba al mando de Arturo Prat."),
            ex("¿Qué es una perspectiva?", "La forma en que una persona mira un hecho", "Dos personas pueden verlo distinto."),
        ],
        "apply": [
            ex("¿Qué año es mayor: 1810 o 1879?", "1879", "1879 viene después de 1810 en la línea de tiempo."),
            ex("¿Qué hecho ocurrió primero: la llegada de Colón (1492) o la Primera Junta (1810)?", "la llegada de Colón", "1492 es un año menor que 1810, por eso fue antes."),
            ex("Ordena de más antiguo a más nuevo: Combate Naval de Iquique, Primera Junta (1810), llegada de Colón (1492).", "llegada de Colón, Primera Junta, Combate Naval de Iquique", "Se ordenan por años: 1492, 1810 y 1879."),
        ],
        "reason": [
            ex("Nina dice que el Combate Naval de Iquique ocurrió antes que la Primera Junta. ¿Tiene razón?", "No; fue en 1879, después de 1810", "1879 es mayor que 1810."),
            ex("Dos personas cuentan el 12 de octubre de 1492: un navegante europeo y una persona de un pueblo originario. ¿Dirán exactamente lo mismo?", "Probablemente no", "Cada uno vivió el hecho de otra manera."),
        ],
        "challenge": [
            ex("El Combate Naval de Iquique fue entre una corbeta de Chile y un barco peruano. ¿Los chilenos y los peruanos lo recuerdan de la misma manera?", "No necesariamente", "Cada país tiene su perspectiva."),
            ex("¿Qué dos días seguidos de septiembre son Fiestas Patrias?", "18 y 19", "El 18 se recuerda la Primera Junta y el 19 las Glorias del Ejército."),
        ],
    },
    context=[ex("Una familia prepara una ramada con empanadas, baile de cueca y banderas para el 18 de septiembre. ¿Qué conmemoración celebran?", "las Fiestas Patrias", "Septiembre y la cueca son parte de esa celebración.")],
    selfcheck=[
        ex("¿Qué fecha se recuerda el Combate Naval de Iquique?", "21 de mayo", "Fue el 21 de mayo de 1879."),
        ex("¿Qué es una cronología?", "Hechos ordenados por fecha", "Va del más antiguo al más nuevo."),
        ex("¿Hay una sola perspectiva para ver un hecho?", "No", "Cada persona lo ve a su manera."),
    ],
    open_task=task("Haz una línea de tiempo con tres conmemoraciones y sus fechas exactas: 12 de octubre de 1492 (llegada de Colón a América), 18 de septiembre de 1810 (Primera Junta Nacional de Gobierno) y 21 de mayo de 1879 (Combate Naval de Iquique). Dibuja un símbolo pequeño al lado de cada una.", "1492: barco, 12 de octubre. 1810: bandera, 18 de septiembre. 1879: barco con ancla, 21 de mayo.", ["tres fechas en orden", "años correctos", "un dibujo por fecha"], ["línea de tiempo dibujada"], ["poner 1879 antes de 1810", "cambiar el día de una fecha"], "Pide que lea las tres fechas en voz alta de izquierda a derecha."),
    reinforce="Pregunta a un adulto cómo celebra su familia el 18 de septiembre.",
    extend="Averigua qué conmemoración hay en tu comuna y busca su fecha.",
)

register(
    OA5, 4,
    materials="Lápiz y papel. Los relatos de actos escolares imaginarios y las listas de actividades están escritos en cada ejercicio.",
    use="Aprenderé que mujeres y hombres participan de muchas maneras en las conmemoraciones de Chile. Sirve para valorar los aportes de todos.",
    prior=["Sé qué son las Fiestas Patrias.", "Sé qué fue el Combate Naval de Iquique."],
    explain=[
        "En las conmemoraciones participan mujeres y hombres, niñas y niños. En Fiestas Patrias hay quienes cocinan empanadas, quienes bailan cueca, quienes cantan, quienes cuelgan banderas y quienes preparan juegos como la rayuela. Todos hacen que la fiesta sea posible.",
        "En el Combate Naval de Iquique, el 21 de mayo de 1879, la tripulación de la Esmeralda estaba formada por hombres. Durante la Guerra del Pacífico (1879 a 1884) también participaron mujeres, por ejemplo cuidando a los heridos y acompañando a las tropas, aunque muchas veces sus nombres se recuerdan menos.",
        "Para no olvidar a nadie, cuando leas una historia pregúntate: ¿quiénes participaron? ¿Qué hacían? ¿Hay personas que casi no se nombran? Reconocer los aportes de todos ayuda a entender que la historia de Chile se hizo entre muchas personas.",
    ],
    vocab=[("participar", "tomar parte en una actividad"), ("aporte", "algo que una persona da o hace por los demás"), ("tripulación", "grupo de personas que trabajan en un barco"), ("cueca", "baile nacional de Chile, que se baila en pareja"), ("herido", "persona que sufrió daño y necesita cuidado")],
    worked=[
        {"title": "Quiénes participan", "problem": "En un acto de Fiestas Patrias, Ana baila cueca, Beto cuelga banderas, la abuela prepara empanadas y el abuelo canta. ¿Cuántas personas participan?", "steps": ["Cuento a cada persona: Ana, Beto, abuela, abuelo.", "Son cuatro."], "answer": "4 personas"},
        {"title": "Aportes distintos", "problem": "¿Todos hacen lo mismo en una fiesta?", "steps": ["Unos cocinan, otros bailan, otros cantan.", "Cada uno aporta algo distinto."], "answer": "No, cada uno aporta algo distinto"},
    ],
    mistakes=[
        {"wrong": "Pensar que en las fiestas solo trabajan las mujeres en la cocina.", "why": "Se repite una idea fija.", "fix": "Hombres y mujeres pueden cocinar, bailar, cantar y organizar."},
        {"wrong": "Creer que solo importan las personas con nombre famoso.", "why": "Se recuerdan solo los nombres que están en los libros.", "fix": "Pregunta también por las personas que ayudaron y casi no se nombran."},
    ],
    tiers={
        "recovery": [
            ex("En una fiesta, Lía cocina empanadas y Tomás cuelga banderas. ¿Cuántas personas participan?", "2", "Son Lía y Tomás."),
            ex("¿La cueca se baila en pareja o sola?", "en pareja", "Es un baile de pareja."),
            ex("¿Participan solo los adultos en las Fiestas Patrias o también los niños?", "también los niños", "Los niños juegan y ayudan."),
        ],
        "understand": [
            ex("¿Qué es un aporte?", "Algo que una persona da o hace por los demás", "Es ayudar a que algo salga bien."),
            ex("¿Qué hacían muchas mujeres en la Guerra del Pacífico?", "Cuidaban a los heridos y acompañaban a las tropas", "Fue un aporte importante."),
            ex("¿Por qué conviene preguntar por las personas que casi no se nombran?", "Para no olvidar sus aportes", "Muchas personas contribuyeron aunque su nombre no se recuerde."),
        ],
        "apply": [
            ex("Lista de una fiesta: bailar cueca, cantar, hacer empanadas, colgar banderas, jugar rayuela. ¿Cuántas actividades hay?", "5", "Son cinco actividades."),
            ex("Beto cocina pastel de choclo y Ana arregla la ramada. ¿Está mal que un niño cocine y una niña arregle?", "No", "Cualquier persona puede hacer cualquier tarea."),
            arith("En un acto, 3 niñas y 2 niños bailan cueca. ¿Cuántas personas bailan en total?", "3+2", "Se suman las niñas y los niños."),
        ],
        "reason": [
            ex("Nico dice: «En el 21 de mayo solo participaron hombres porque en el barco no había mujeres». ¿Qué le faltó considerar?", "Que otras personas también participaron en la guerra y en la memoria", "La historia incluye a quienes ayudaron en tierra y en la sociedad."),
            ex("Una profesora cuenta una historia en que no aparecen mujeres. ¿Qué pregunta puedes hacer?", "¿Participaron mujeres y qué hicieron?", "Así se busca a quienes casi no se nombran."),
        ],
        "challenge": [
            arith("En una fiesta, 4 personas cocinan, 3 bailan y 2 cantan. Nadie hace dos cosas. ¿Cuántas personas hay en total?", "4+3+2", "Se suman los tres grupos."),
            ex("Dos amigos cuentan lo que hicieron en la fiesta: Lola colgó banderas y Mateo hizo empanadas. ¿Quién cocinó?", "Mateo", "Cocinar es hacer las empanadas."),
        ],
    },
    context=[ex("En el acto del 21 de mayo, la escuela invita a un abuelo a contar la historia del Combate Naval y a una abuela a contar cómo era cuidar a las personas heridas en una guerra. ¿Qué logra la escuela con esto?", "Mostrar varios aportes y voces", "Se escuchan personas distintas.")],
    selfcheck=[
        ex("¿Participan mujeres y hombres en las conmemoraciones?", "Sí", "Ambos aportan a la fiesta."),
        ex("Beto cuelga banderas y Ana baila cueca. ¿Cuántos aportes distintos hay?", "2", "Colgar banderas y bailar son dos aportes."),
        ex("¿Qué baile se baila en pareja en Fiestas Patrias?", "la cueca", "Es el baile nacional."),
    ],
    open_task=task("Dibuja una escena de Fiestas Patrias con cuatro personas distintas haciendo cuatro actividades diferentes. Elige las actividades entre: bailar cueca, cocinar empanadas, colgar banderas, cantar, jugar rayuela, elevar volantines. Escribe un nombre inventado y la actividad bajo cada persona.", "Ana baila cueca. Beto cocina empanadas. Lía cuelga banderas. Tomás eleva un volantín.", ["cuatro personas", "cuatro actividades distintas", "hombres y mujeres en tareas variadas"], ["dibujo con leyendas"], ["repetir la misma actividad", "tareas solo por sexo"], "Pide que explique cómo cada persona ayuda a la fiesta."),
    reinforce="Pregunta en tu casa quién cocina en las fiestas y quién baila.",
    extend="Escribe qué aporte tuyo podría ayudar en una fiesta del curso.",
)

register(
    OA5, 5,
    materials="Lápiz y papel. Los símbolos y los relatos de pertenencia están descritos en cada ejercicio.",
    use="Aprenderé a explicar cómo un símbolo o una conmemoración nos une como país, aunque seamos distintos. Sirve para valorar lo que compartimos.",
    prior=["Sé nombrar los símbolos de Chile.", "Sé que hay conmemoraciones nacionales."],
    explain=[
        "Un símbolo une a las personas cuando todas lo reconocen. La bandera es la misma para todos: la ve una niña en el norte y un niño en el sur. Aunque vivamos lejos y seamos distintos, compartimos la bandera, el escudo y el himno.",
        "Eso es la unidad nacional: sentirnos parte de un mismo país. La identidad nacional es lo que nos hace sentir chilenos: símbolos, fiestas, comidas y recuerdos. Pero la unidad no significa que seamos todos iguales. En Chile hay personas de pueblos originarios, de otras regiones y de otros países que también forman parte de la comunidad.",
        "Una conmemoración, como las Fiestas Patrias, une porque mucha gente celebra al mismo tiempo. Para explicar cómo un símbolo nos une, usa tres ideas: qué es el símbolo, quiénes lo reconocen y qué sentimos o hacemos juntos cuando aparece.",
    ],
    vocab=[("unidad", "estar juntos en algo que compartimos"), ("identidad nacional", "lo que nos hace sentir parte de un país"), ("compartir", "tener o usar algo entre varios"), ("comunidad", "grupo de personas que viven o trabajan juntas"), ("diversidad", "gran variedad de personas y costumbres")],
    worked=[
        {"title": "Un símbolo que une", "problem": "¿Por qué la bandera une a niños que viven lejos?", "steps": ["La bandera es la misma en todo Chile.", "Todos la reconocen aunque vivan lejos.", "Eso crea un sentimiento de unidad."], "answer": "Porque todos la reconocemos como propia"},
        {"title": "Unidad y diversidad", "problem": "¿Unidad significa que todos somos iguales?", "steps": ["Hay personas con costumbres distintas.", "Aun así, comparten símbolos del país."], "answer": "No; somos distintos y compartimos símbolos"},
    ],
    mistakes=[
        {"wrong": "Pensar que ser chileno es tener las mismas costumbres.", "why": "Se piensa que la unidad es igualdad.", "fix": "Podemos ser diferentes y compartir símbolos y fiestas."},
        {"wrong": "Decir «porque sí» al explicar por qué un símbolo nos une.", "why": "No se da una razón.", "fix": "Usa tres ideas: qué es, quiénes lo reconocen y qué hacemos juntos."},
    ],
    tiers={
        "recovery": [
            ex("¿La bandera es la misma en el norte y en el sur de Chile?", "Sí", "Es un símbolo de todo el país."),
            ex("¿Qué palabra significa «estar juntos en algo que compartimos»: unidad o lejanía?", "unidad", "La unidad nos junta."),
            ex("Nombra un símbolo que comparten todos los chilenos.", "la bandera", "También son símbolos el escudo y el himno."),
        ],
        "understand": [
            ex("¿Qué es la identidad nacional?", "Lo que nos hace sentir parte de un país", "Incluye símbolos, fiestas y recuerdos."),
            ex("¿Por qué una fiesta nacional une a las personas?", "Porque muchas personas celebran juntas", "Compartir una fiesta crea unión."),
            ex("¿Significa unidad que todos seamos iguales?", "No", "Podemos ser distintos y compartir lo mismo."),
        ],
        "apply": [
            ex("Completa: la bandera une porque todos la ___ como símbolo de Chile.", "reconocemos", "Reconocerla es lo que nos une."),
            ex("En una escuela, niños de tres lugares distintos cantan el himno. ¿Qué comparten?", "el himno", "Todos conocen la misma canción."),
            ex("Una niña mapuche y un niño de una familia de Perú levantan la bandera juntos en el acto. ¿Qué muestra eso sobre la diversidad?", "Que personas distintas comparten un símbolo", "Cada uno tiene su historia y todos participan."),
        ],
        "reason": [
            ex("Pedro dice: «Para ser chileno hay que comer lo mismo». ¿Es correcto?", "No; hay costumbres distintas en cada lugar", "La unidad no exige ser iguales."),
            ex("Ana explica: «La bandera nos une porque es de todos y la vemos en la escuela, en la plaza y en las fiestas». ¿Usó las ideas de la clase?", "Sí", "Dijo qué es, quiénes la reconocen y dónde la vemos."),
        ],
        "challenge": [
            ex("Dos niños viven uno en Arica y otro en Punta Arenas, a miles de kilómetros. ¿Qué símbolo pueden compartir aunque estén lejos?", "la bandera, el escudo o el himno", "Cualquiera de los tres símbolos."),
            ex("En un curso hay 10 niños: 6 comen empanadas en las fiestas, 4 comen pastel de choclo, y todos cantan el himno. ¿Cuántos comparten el himno?", "10", "Todos lo cantan aunque coman distinto."),
        ],
    },
    context=[ex("Un grupo de niños hace una guirnalda con banderas pequeñas para el 18 de septiembre, cada una decorada a su manera. ¿Qué muestra la guirnalda: unidad, diversidad o las dos cosas?", "las dos cosas", "Hay una bandera compartida y adornos distintos.")],
    selfcheck=[
        ex("¿Qué símbolo une a un niño del norte y a uno del sur?", "la bandera", "Es la misma bandera para todos."),
        ex("¿La diversidad impide la unidad?", "No", "Podemos ser distintos y estar unidos."),
        ex("¿Qué es una comunidad?", "Un grupo de personas que viven o trabajan juntas", "Comparten un lugar o una meta."),
    ],
    open_task=task("Escribe tres frases que expliquen cómo un símbolo nos une. Elige un símbolo (bandera, escudo o himno) y responde: qué es, quiénes lo reconocen, qué hacemos juntos con él. Ejemplo de inicio: «La bandera es…».", "La bandera es un símbolo de Chile. Todos los chilenos la reconocen. En las Fiestas Patrias la colgamos juntos.", ["tres frases", "dice qué es, quiénes lo reconocen y qué hacemos", "usa un símbolo correcto"], ["texto de tres frases"], ["decir «porque sí»", "confundir símbolos"], "Pide que lea sus tres frases y que señale la que muestra unión."),
    reinforce="Cuenta a alguien de tu casa qué símbolo de Chile te gusta más y por qué.",
    extend="Explica cómo se pueden respetar las costumbres distintas y compartir la misma bandera.",
)

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Lápiz y papel. Las listas de expresiones culturales de Chile están escritas en cada ejercicio.",
    use="Aprenderé a reconocer comidas, flores, animales, música y juegos típicos de Chile y de mi entorno. Sirve para valorar lo que nos identifica.",
    prior=["Sé nombrar comidas y juegos que conozco.", "Sé clasificar cosas en grupos."],
    explain=[
        "Las expresiones culturales son las cosas que hacen especial a un lugar: comidas, música, juegos, flores, animales y fiestas. Son parte de la cultura, que es la forma de vivir de un grupo de personas.",
        "En Chile hay comidas típicas como la empanada, la cazuela, el pastel de choclo, las humitas y las sopaipillas. La flor nacional es el copihue. Animales típicos son el cóndor y el huemul, que están en el escudo. La cueca es el baile nacional. Juegos tradicionales son la rayuela, el trompo y el volantín.",
        "Cada lugar de Chile tiene también sus propias expresiones. Las que se conocen en una zona pequeña son locales, y las que se conocen en todo el país son nacionales. Para reconocerlas, pregunta: ¿qué es?, ¿dónde se conoce?, ¿quién me la mostró?",
    ],
    vocab=[("cultura", "forma de vivir de un grupo de personas"), ("expresión cultural", "comida, música, juego, fiesta o costumbre de un lugar"), ("típico", "propio de un lugar"), ("copihue", "flor nacional de Chile"), ("cueca", "baile nacional de Chile")],
    worked=[
        {"title": "Clasificar", "problem": "Clasifica en comida, juego o animal: empanada, rayuela, cóndor.", "steps": ["La empanada se come: comida.", "La rayuela se juega: juego.", "El cóndor es un ave: animal."], "answer": "Empanada: comida; rayuela: juego; cóndor: animal"},
        {"title": "Nacional o local", "problem": "El baile de la cueca se conoce en todo Chile. ¿Es nacional o local?", "steps": ["Se baila en todo el país.", "Por eso es nacional."], "answer": "Nacional"},
    ],
    mistakes=[
        {"wrong": "Creer que una comida de mi casa es típica de todo Chile.", "why": "Se piensa que lo que conozco lo conocen todos.", "fix": "Pregunta si se conoce en todo el país o solo en tu zona."},
        {"wrong": "Mezclar flor y animal en la lista.", "why": "No se mira qué es cada cosa.", "fix": "Pregúntate: ¿crece, se come, se baila o se juega?"},
    ],
    tiers={
        "recovery": [
            ex("¿La empanada es una comida o un juego?", "comida", "La empanada se come."),
            ex("¿El copihue es una flor o un animal?", "una flor", "Es la flor nacional de Chile."),
            ex("¿La cueca es un baile o una comida?", "un baile", "Se baila en pareja."),
        ],
        "understand": [
            ex("¿Qué es una expresión cultural?", "Una comida, música, juego o fiesta propia de un lugar", "Hace especial a un lugar."),
            ex("¿Cuáles de estos son juegos: rayuela, trompo, cazuela?", "rayuela y trompo", "La cazuela es una comida."),
            ex("¿Qué dos animales aparecen en el escudo de Chile?", "el cóndor y el huemul", "Son animales típicos del país."),
        ],
        "apply": [
            ex("Clasifica en comida, juego, música o animal: sopaipillas.", "comida", "Las sopaipillas se comen."),
            ex("Clasifica en comida, juego, música o animal: huemul.", "animal", "Es un animal de Chile."),
            ex("Clasifica en comida, juego, música o animal: cueca.", "música", "Es música y baile."),
        ],
        "reason": [
            ex("Pedro dice que el volantín es un animal. ¿Tiene razón?", "No; es un juego", "Se elevan volantines en el cielo."),
            ex("Lola dice que la sopaipilla se come solo en su casa. Su profesora dice que se come en muchas partes de Chile. ¿Es local o nacional?", "nacional", "Se conoce en muchos lugares del país."),
        ],
        "challenge": [
            ex("Lista: empanada, cueca, rayuela, copihue, cóndor, cazuela. ¿Cuántas son comidas?", "2", "Son la empanada y la cazuela."),
            ex("En la misma lista, ¿cuántas son seres vivos (flor o animal)?", "2", "Son el copihue y el cóndor."),
        ],
    },
    context=[ex("En el cumpleaños de Sofía hay empanadas, un baile de cueca y un juego de trompos. ¿Cuántas expresiones culturales distintas hay?", "3", "Una comida, un baile y un juego.")],
    selfcheck=[
        ex("¿Cuál es la flor nacional de Chile?", "el copihue", "Lo vimos en la clase: el copihue es la flor nacional."),
        ex("¿Cuál es el baile nacional de Chile?", "la cueca", "Se baila en Fiestas Patrias."),
        ex("¿Qué es la cultura?", "La forma de vivir de un grupo de personas", "Incluye comidas, música y fiestas."),
    ],
    open_task=task("Haz una tabla de cuatro filas: comida, juego, música y animal. En cada fila escribe una expresión de Chile o de tu entorno. Puedes elegir entre: comidas (empanada, cazuela, humitas), juegos (rayuela, trompo, volantín), música (cueca) y animales (cóndor, huemul).", "Comida: empanada. Juego: rayuela. Música: cueca. Animal: cóndor.", ["cuatro filas", "una expresión por fila", "clasificación correcta"], ["tabla completa"], ["poner un animal en la fila de comidas", "dejar filas vacías"], "Pide que cuente cuál conoce mejor y cómo la conoció."),
    reinforce="Pregunta a un adulto cuál es su comida típica favorita.",
    extend="Averigua una flor o un animal típico de tu región y dibújalo.",
)

register(
    OA6, 2,
    materials="Lápiz y papel. Los datos de cada fiesta están escritos en cada ejercicio.",
    use="Aprenderé a describir fiestas y tradiciones de Chile y a decir cuándo y dónde ocurren. Sirve para entender por qué son importantes para las personas.",
    prior=["Sé qué es una expresión cultural.", "Sé leer fechas."],
    explain=[
        "Una fiesta o tradición tiene un lugar, una fecha y personas que participan. La Fiesta de La Tirana se celebra el 16 de julio en el pueblo de La Tirana, en el norte de Chile, en la Región de Tarapacá: hay bailes religiosos para honrar a la Virgen del Carmen.",
        "La Fiesta de San Pedro es el 29 de junio. Es una fiesta de pescadores: sacan la imagen de San Pedro en una procesión por el mar en lanchas. La Fiesta de Cuasimodo se hace el domingo después de Pascua de Resurrección: huasos a caballo o en bicicleta acompañan al sacerdote que lleva la comunión a las personas enfermas.",
        "Otras tradiciones son las carreras a la chilena, en que dos caballos corren en una pista recta; el rodeo, que se hace en una medialuna; y la vendimia, que celebra la cosecha de la uva, en verano y otoño. También hay fiestas por el aniversario de la fundación de un pueblo o ciudad; por ejemplo, Santiago se fundó el 12 de febrero de 1541. Algunas personas piensan distinto sobre el rodeo, porque se habla del cuidado de los animales; es bueno escuchar con respeto las distintas opiniones.",
    ],
    vocab=[("fiesta", "celebración con personas reunidas por un motivo"), ("tradición", "costumbre que pasa de generación en generación"), ("procesión", "grupo de personas que camina junto, a veces con una imagen"), ("vendimia", "fiesta de la cosecha de la uva"), ("fundación", "momento en que se crea un pueblo o ciudad")],
    worked=[
        {"title": "Lugar y fecha", "problem": "¿Cuándo y dónde se celebra la Fiesta de La Tirana?", "steps": ["Se celebra el 16 de julio.", "Es en el pueblo de La Tirana, en el norte de Chile."], "answer": "16 de julio, en La Tirana, norte de Chile"},
        {"title": "Quiénes participan", "problem": "En la Fiesta de San Pedro, ¿quiénes participan en la procesión en el mar?", "steps": ["Es una fiesta de pescadores.", "Van en lanchas."], "answer": "Pescadores y sus familias"},
    ],
    mistakes=[
        {"wrong": "Creer que todas las fiestas se celebran en la misma fecha.", "why": "Se piensa que son todas en septiembre.", "fix": "Cada fiesta tiene su propia fecha y su lugar."},
        {"wrong": "Decir que una tradición es mejor que otra.", "why": "Se compara para elegir.", "fix": "Cada tradición tiene su historia y se respeta."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué mes es la Fiesta de La Tirana?", "julio", "Se celebra el 16 de julio."),
            ex("¿Qué mes es la Fiesta de San Pedro: junio o julio?", "junio", "Es el 29 de junio."),
            ex("¿Qué se cosecha en la vendimia?", "uva", "La vendimia celebra la cosecha de la uva."),
        ],
        "understand": [
            ex("¿Quiénes celebran la Fiesta de San Pedro?", "los pescadores", "Es una fiesta de pescadores."),
            ex("¿Qué hace el sacerdote en la Fiesta de Cuasimodo?", "lleva la comunión a las personas enfermas", "Los huasos lo acompañan."),
            ex("¿Cuándo se celebra Cuasimodo?", "el domingo después de Pascua de Resurrección", "Así lo dice la tradición."),
        ],
        "apply": [
            ex("Une cada fiesta con su lugar: La Tirana, San Pedro. Lugares: norte de Chile (pueblo de La Tirana), caletas de pescadores.", "La Tirana: norte de Chile; San Pedro: caletas de pescadores", "Cada fiesta ocurre en su propio lugar."),
            ex("Ordena por fecha en el año: San Pedro (29 de junio), La Tirana (16 de julio).", "San Pedro, La Tirana", "Junio viene antes que julio."),
            arith("¿Cuántos días hay entre el 29 de junio y el 16 de julio? Junio tiene 30 días: del 29 al 30 de junio es 1 día y del 30 de junio al 16 de julio son 16 días.", "1+16", "Se suman los días de junio y los de julio."),
        ],
        "reason": [
            ex("Nico dice que la Fiesta de La Tirana es en el sur de Chile. ¿Es correcto?", "No; es en el norte", "La Tirana está en la Región de Tarapacá."),
            ex("Dos amigos opinan distinto sobre el rodeo. ¿Cómo deben conversar?", "Con respeto, escuchando al otro", "Cada persona puede tener otra opinión."),
        ],
        "challenge": [
            ex("Santiago se fundó el 12 de febrero de 1541. Si la ciudad celebra su aniversario cada 12 de febrero, ¿en qué mes cae el aniversario?", "febrero", "El mes aparece en la fecha."),
            ex("¿Cuál de estas tradiciones es de caballos: carreras a la chilena, vendimia, procesión de San Pedro?", "carreras a la chilena", "Dos caballos corren en pista recta."),
        ],
    },
    context=[ex("Una familia de Valparaíso va el 29 de junio al muelle a ver una procesión de lanchas con la imagen de San Pedro. ¿Qué fiesta es?", "Fiesta de San Pedro", "Es la fiesta de los pescadores.")],
    selfcheck=[
        ex("¿Qué fiesta es el 16 de julio?", "Fiesta de La Tirana", "Fue la fecha del enunciado."),
        ex("¿En qué se parece una tradición a una costumbre?", "En que se repite con el tiempo", "Una tradición pasa de generación en generación."),
        ex("¿Qué es una procesión?", "Un grupo que camina junto, a veces con una imagen", "Se hace en algunas fiestas."),
    ],
    open_task=task("Elige una de estas fiestas y escribe cuatro datos: nombre, fecha, lugar y qué se hace. (a) La Tirana: 16 de julio, pueblo de La Tirana, bailes religiosos; (b) San Pedro: 29 de junio, caletas, procesión de lanchas; (c) Cuasimodo: domingo después de Pascua, campos y pueblos, huasos acompañan al sacerdote.", "Fiesta de San Pedro. 29 de junio. Caletas de pescadores. Se saca la imagen de San Pedro en lanchas por el mar.", ["cuatro datos", "fecha y lugar correctos", "describe qué se hace"], ["ficha de cuatro datos"], ["mezclar datos de dos fiestas", "inventar la fecha"], "Pide que cuente a un adulto de qué trata la fiesta."),
    reinforce="Escribe la fecha de una fiesta de tu comuna.",
    extend="Compara dos fiestas del texto y escribe una semejanza y una diferencia.",
)

register(
    OA6, 3,
    materials="Lápiz y papel. La tabla de zonas de Chile y sus expresiones está escrita en cada ejercicio.",
    use="Aprenderé a distinguir expresiones locales de nacionales y a ver semejanzas y diferencias entre zonas. Sirve para ubicar las tradiciones en el mapa de Chile.",
    prior=["Sé nombrar fiestas de Chile.", "Sé que Chile tiene norte, centro y sur."],
    explain=[
        "Una expresión es local cuando se vive en un lugar pequeño, como un pueblo o una región. Es nacional cuando se conoce en todo el país. Una misma expresión puede ser local en su origen y volverse conocida en todo Chile.",
        "Imagina un mapa de Chile largo y delgado. En el norte, en Tarapacá, está La Tirana. En el centro están la vendimia, el rodeo y la cueca. En el sur, en la isla de Chiloé, hay comidas como el curanto y también mingas, donde los vecinos se ayudan a mover una casa o a hacer un trabajo. En Isla de Pascua o Rapa Nui, en febrero, se celebra la Tapati Rapa Nui.",
        "Al comparar dos zonas, buscamos semejanzas, como que ambas tienen fiestas con música y comida, y diferencias, como el clima y los alimentos. Comparar nos enseña que Chile es un país diverso.",
    ],
    vocab=[("local", "de un lugar pequeño"), ("nacional", "de todo el país"), ("zona", "parte de un territorio"), ("Rapa Nui", "isla en el océano Pacífico, parte de Chile"), ("minga", "trabajo comunitario en Chiloé donde los vecinos se ayudan")],
    worked=[
        {"title": "Local o nacional", "problem": "La Fiesta de La Tirana se hace en un pueblo del norte. ¿Es local o nacional?", "steps": ["Se vive principalmente en La Tirana.", "Es una expresión local."], "answer": "Local"},
        {"title": "Una semejanza", "problem": "En La Tirana y en San Pedro hay música y personas reunidas. ¿Qué tienen en común?", "steps": ["Ambas son fiestas religiosas.", "Ambas reúnen a muchas personas."], "answer": "Son fiestas religiosas que reúnen a muchas personas"},
    ],
    mistakes=[
        {"wrong": "Decir que todo lo que conoce mi comuna es nacional.", "why": "Se generaliza desde la propia experiencia.", "fix": "Pregunta si se conoce en todo el país."},
        {"wrong": "Ubicar Rapa Nui en el sur en el mapa de tierra firme.", "why": "No se mira que es una isla lejana en el Pacífico.", "fix": "Rapa Nui es una isla en el océano Pacífico, lejos de la costa."},
    ],
    tiers={
        "recovery": [
            ex("La Tirana está en el norte de Chile. ¿Es una expresión local o nacional?", "local", "Se vive en un lugar específico."),
            ex("La cueca se baila en todo Chile. ¿Es local o nacional?", "nacional", "Se conoce en todo el país."),
            ex("¿Rapa Nui es una isla o una ciudad?", "una isla", "Está en el océano Pacífico."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre local y nacional?", "Local es de un lugar pequeño y nacional es de todo el país", "Cambia el tamaño del lugar."),
            ex("¿Qué es una minga?", "Un trabajo en que los vecinos se ayudan", "Se hace en Chiloé."),
            ex("¿En qué mes se celebra la Tapati Rapa Nui?", "febrero", "Se celebra en febrero en la isla."),
        ],
        "apply": [
            ex("Tabla. Norte: La Tirana. Centro: vendimia. Sur: minga en Chiloé. ¿Qué expresión es del sur?", "la minga", "La minga es de Chiloé."),
            ex("Tabla. Norte: La Tirana. Centro: vendimia. Sur: minga en Chiloé. ¿Qué zona celebra la vendimia?", "el centro", "Está en la columna del centro."),
            ex("Tabla. Norte: La Tirana, 16 de julio. Centro: vendimia, febrero a abril. ¿Qué fiesta es en verano y otoño?", "la vendimia", "Es de febrero a abril."),
        ],
        "reason": [
            ex("Un niño dice: «Todos en Chile hacen mingas». ¿Qué error comete?", "Generaliza una costumbre de Chiloé a todo el país", "La minga es una tradición local."),
            ex("La cueca nació en un lugar, pero hoy se baila en todo Chile. ¿Qué la hizo nacional?", "Que se extendió y se conoce en todo el país", "Una expresión local puede llegar a ser nacional."),
        ],
        "challenge": [
            ex("Compara La Tirana (norte, bailes religiosos) y San Pedro (caletas, procesión en el mar). Escribe una semejanza.", "Ambas son fiestas religiosas con procesión", "En las dos hay personas que honran un símbolo religioso."),
            ex("Compara La Tirana y San Pedro. Escribe una diferencia.", "Una es en un pueblo del norte y la otra es de pescadores en el mar", "Los lugares son distintos."),
        ],
    },
    context=[ex("Una niña de Chiloé cuenta que en su isla los vecinos se juntan para mover una casa con bueyes. Un niño de Santiago nunca lo vio. ¿Es una expresión local o nacional?", "local", "Es una tradición de la isla.")],
    selfcheck=[
        ex("¿Qué fiesta del norte estudiaste?", "La Tirana", "Es en la Región de Tarapacá."),
        ex("¿Rapa Nui es parte de Chile?", "Sí", "Es una isla chilena en el Pacífico."),
        ex("¿La cueca es local o nacional?", "nacional", "Se baila en todo Chile."),
    ],
    open_task=task("Dibuja un mapa muy simple de Chile como una línea vertical larga. Marca tres puntos: norte, centro y sur. Escribe al lado una expresión de cada zona, eligiendo de esta lista: norte (La Tirana), centro (vendimia, cueca), sur (minga en Chiloé). Aparte, dibuja un círculo en el océano y escribe «Rapa Nui».", "Norte: La Tirana. Centro: vendimia. Sur: minga en Chiloé. Círculo aparte: Rapa Nui.", ["tres zonas marcadas", "expresiones correctas en cada zona", "Rapa Nui como isla aparte"], ["mapa con rótulos"], ["poner La Tirana en el sur", "poner Rapa Nui pegada al continente"], "Pide que lea las zonas de norte a sur."),
    reinforce="Pregunta a un adulto qué tradición de tu comuna se conoce solo en tu zona.",
    extend="Averigua qué expresión nacional también se vive en tu región.",
)

register(
    OA6, 4,
    materials="Lápiz y papel. Los tres testimonios de personas imaginarias están escritos en cada ejercicio.",
    use="Aprenderé a usar relatos de personas y a no decir «todos» cuando solo sé de algunos. Sirve para hablar con exactitud de las culturas.",
    prior=["Sé qué es una fuente.", "Sé nombrar fiestas y tradiciones."],
    explain=[
        "Para saber de una tradición, podemos escuchar a quienes la viven. Aquí tienes tres voces imaginarias. Elena, de Chiloé: «En mi isla hacemos mingas para ayudar a los vecinos». Pedro, de La Tirana: «Mi familia baila todos los años el 16 de julio». Camila, de Santiago: «En mi casa celebramos el 18 con empanadas».",
        "Cada voz cuenta solo lo que conoce. Elena no habla por todo Chile, Pedro no habla por todos los bailarines y Camila no habla por todos los santiaguinos. Si decimos «todos los chilenos hacen mingas», estamos generalizando, es decir, diciendo «todos» sin saber.",
        "Una buena forma de hablar es citar a quién lo dijo: «Según Elena, en Chiloé se hacen mingas». También conviene preguntar a más de una persona. Así evitamos repetir una idea fija sobre un lugar o un pueblo.",
    ],
    vocab=[("testimonio", "lo que cuenta una persona sobre lo que vive"), ("generalizar", "decir «todos» sin saber"), ("voz", "persona que cuenta su experiencia"), ("citar", "decir quién dijo algo"), ("idea fija", "creencia sobre un grupo que se repite sin comprobar")],
    worked=[
        {"title": "Citar la fuente", "problem": "Elena de Chiloé dice que en su isla hacen mingas. ¿Cómo lo dices bien?", "steps": ["Digo quién lo contó y dónde.", "«Según Elena, en Chiloé se hacen mingas»."], "answer": "Según Elena, en Chiloé se hacen mingas"},
        {"title": "Detectar una generalización", "problem": "«Todos en Chile bailan en La Tirana». ¿Es correcto?", "steps": ["Pedro solo habla de su familia y de La Tirana.", "No sabemos de todos los chilenos."], "answer": "No, generaliza"},
    ],
    mistakes=[
        {"wrong": "Decir «todos» cuando solo hablé con una persona.", "why": "Se cree que una voz representa a muchas.", "fix": "Di «según [nombre]» y busca otras voces."},
        {"wrong": "No citar a quién me contó algo.", "why": "Se piensa que da igual.", "fix": "Siempre di quién lo contó."},
    ],
    tiers={
        "recovery": [
            ex("Elena dice: «En Chiloé hacemos mingas». ¿Qué cuenta Elena: mingas o fiestas de septiembre?", "mingas", "Eso dice su testimonio."),
            ex("Pedro dice que baila el 16 de julio. ¿Qué mes dice?", "julio", "Es el mes de su fecha."),
            ex("Camila dice que celebra el 18 con empanadas. ¿Qué come?", "empanadas", "Lo dice en su testimonio."),
        ],
        "understand": [
            ex("¿Qué es generalizar?", "Decir «todos» sin saberlo", "Se afirma más de lo que se sabe."),
            ex("¿Por qué es mejor decir «según Elena»?", "Porque dice de dónde viene la información", "Se cita la fuente."),
            ex("¿Una sola persona habla por todo un lugar?", "No", "Cada voz cuenta lo que conoce."),
        ],
        "apply": [
            ex("Reescribe bien: «Todos hacen mingas». Usa «según Elena».", "Según Elena, en Chiloé se hacen mingas", "Se cita la fuente y el lugar."),
            ex("Reescribe bien: «Todos celebran con empanadas». Usa «según Camila».", "Según Camila, en su casa celebran con empanadas", "Se limita a lo que Camila dijo."),
            ex("Reescribe bien: «Todos bailan el 16 de julio». Usa «según Pedro».", "Según Pedro, su familia baila el 16 de julio", "Se limita a su familia."),
        ],
        "reason": [
            ex("Un niño dice: «Camila vive en Santiago y come empanadas, así que todos los de Santiago son iguales». ¿Qué error hace?", "Generaliza desde una sola persona", "Camila no representa a todos."),
            ex("¿Qué podrías hacer para saber más de las mingas, además de escuchar a Elena?", "Preguntar a otras personas de Chiloé", "Más voces dan más información."),
        ],
        "challenge": [
            ex("Tres frases: A) «Según Elena, en Chiloé hay mingas». B) «Todos los chilenos bailan en La Tirana». C) «Según Camila, ella celebra con empanadas». ¿Cuáles citan su fuente?", "A y C", "B afirma «todos» sin fuente."),
            ex("De las tres frases anteriores, ¿cuál generaliza?", "B", "Dice «todos los chilenos» sin saber."),
        ],
    },
    context=[ex("Para el diario mural, tres niños traen cada uno el relato de un familiar sobre una fiesta distinta. ¿Cuántas voces tiene el diario?", "3", "Cada niño trae una voz.")],
    selfcheck=[
        ex("¿Qué palabra usamos para decir quién nos contó algo?", "según", "«Según Elena…» cita la fuente."),
        ex("Un testimonio, ¿cuenta la experiencia de quién?", "de una persona", "Es lo que vive quien cuenta."),
        ex("¿Se puede decir «todos» si solo hablé con una persona?", "No", "Eso sería generalizar."),
    ],
    open_task=task("Escribe tres frases que citen la voz de las personas imaginarias de esta clase: Elena (mingas en Chiloé), Pedro (baile el 16 de julio en La Tirana) y Camila (empanadas el 18). Usa «según» en cada una y no uses la palabra «todos».", "Según Elena, en Chiloé se hacen mingas. Según Pedro, su familia baila el 16 de julio. Según Camila, en su casa se come empanadas el 18.", ["tres frases", "usa «según»", "no generaliza"], ["tres frases escritas"], ["usar «todos»", "mezclar voces"], "Pide que lea una frase y diga quién habla."),
    reinforce="Pregunta a un adulto qué fiesta celebra su familia y escribe «según…».",
    extend="Compara dos voces sobre la misma tradición y busca diferencias.",
)

register(
    OA6, 5,
    materials="Lápiz y papel. Las reglas de la muestra y las situaciones están escritas en cada ejercicio.",
    use="Aprenderé a presentar una expresión cultural con respeto y a explicar por qué da sentido de pertenencia. Sirve para compartir sin burlarse ni inventar.",
    prior=["Sé nombrar expresiones culturales.", "Sé citar la fuente."],
    explain=[
        "Una muestra cultural es una presentación de expresiones culturales: una comida, un baile, un juego, una canción. Cuando una expresión nos hace sentir parte de un grupo, decimos que da sentido de pertenencia. Por ejemplo, bailar cueca en Fiestas Patrias hace que nos sintamos parte de Chile.",
        "Para presentar con respeto: pide permiso a quienes la practican, di de dónde viene la expresión, cuéntala tal como te la explicaron y no uses disfraces que se burlen de otros. Si la expresión es de un pueblo originario o de una comunidad, quien la enseña de verdad es esa comunidad.",
        "Al terminar la muestra, explica por qué esa expresión es importante: ¿qué sentimos al verla?, ¿a quiénes une?, ¿qué nos enseña? Así tu presentación no es solo un adorno: cuenta quiénes la viven y por qué.",
    ],
    vocab=[("muestra cultural", "presentación de expresiones culturales"), ("pertenencia", "sentirse parte de un grupo"), ("respeto", "tratar bien a otros y a sus costumbres"), ("burla", "reírse de otros para herirlos"), ("comunidad", "grupo de personas con algo en común")],
    worked=[
        {"title": "Una regla de respeto", "problem": "Quiero presentar una danza de un pueblo originario. ¿Qué debo hacer primero?", "steps": ["La danza pertenece a una comunidad.", "Debo pedir permiso y aprender con quienes la practican."], "answer": "Pedir permiso y aprender con la comunidad"},
        {"title": "Pertenencia", "problem": "¿Por qué bailar cueca en Fiestas Patrias da sentido de pertenencia?", "steps": ["Muchas personas la bailan.", "Nos hace sentir parte de la misma fiesta."], "answer": "Porque nos hace sentir parte de la misma fiesta"},
    ],
    mistakes=[
        {"wrong": "Disfrazarme de forma exagerada para hacer reír.", "why": "Se piensa que es solo un juego.", "fix": "Presenta con seriedad y sin burlarte."},
        {"wrong": "Inventar cómo se hace un baile o un rito de otro pueblo.", "why": "Se quiere completar lo que no se sabe.", "fix": "Di solo lo que te contó la comunidad o una fuente confiable."},
    ],
    tiers={
        "recovery": [
            ex("¿Se debe pedir permiso a quienes practican una expresión cultural?", "Sí", "Es una forma de respeto."),
            ex("¿Es correcto burlarse de un baile de otro pueblo?", "No", "La burla hiere."),
            ex("¿Qué palabra significa «sentirse parte de un grupo»?", "pertenencia", "Eso es pertenencia."),
        ],
        "understand": [
            ex("¿Qué es una muestra cultural?", "Una presentación de expresiones culturales", "Puede tener comidas, bailes o juegos."),
            ex("¿Por qué no se inventa cómo se hace un rito de otro pueblo?", "Porque solo la comunidad lo conoce bien", "Se puede cambiar su sentido."),
            ex("¿Qué debes decir al presentar una expresión: de dónde viene o nada?", "de dónde viene", "Se cuenta su origen."),
        ],
        "apply": [
            ex("Reglas: A) pedir permiso, B) burlarse, C) citar de dónde viene. ¿Cuáles son respetuosas?", "A y C", "Burlarse hiere a otros."),
            ex("Una niña va a presentar una comida típica del sur. ¿Qué dos datos debe decir?", "Qué es y de dónde viene", "Así se entiende su origen."),
            ex("Beto va a bailar cueca en la muestra. ¿Qué pertenencia le da la cueca?", "Sentirse parte de las Fiestas Patrias de Chile", "La cueca es un baile nacional."),
        ],
        "reason": [
            ex("Un grupo planea disfrazarse para hacer reír de un pueblo originario. ¿Qué deberían hacer?", "Cambiar el plan y presentar con respeto", "La burla no es respeto."),
            ex("¿Por qué una muestra cultural no es un simple adorno?", "Porque cuenta quiénes viven esa expresión y por qué es importante", "Tiene sentido para una comunidad."),
        ],
        "challenge": [
            arith("En una muestra hay 3 comidas, 2 juegos y 1 baile. ¿Cuántas expresiones se presentan?", "3+2+1", "Se suman las comidas, los juegos y el baile."),
            arith("En la muestra, 4 niños presentan una comida y 2 un baile. Nadie presenta dos cosas. ¿Cuántos niños presentan?", "4+2", "Se suman los dos grupos."),
        ],
    },
    context=[ex("En la muestra, Lola enseña el juego del trompo y dice: «Mi abuelo me enseñó este juego; es muy conocido en muchas partes de Chile». ¿Qué hizo bien Lola?", "Citó de dónde viene lo que sabe", "Dijo quién se lo enseñó.")],
    selfcheck=[
        ex("¿Qué es pertenencia?", "Sentirse parte de un grupo", "Es sentir que uno forma parte."),
        ex("¿Se debe pedir permiso a la comunidad para presentar su baile?", "Sí", "Es una regla de respeto."),
        ex("¿Qué debemos evitar en una muestra cultural?", "La burla", "Hiere a otras personas."),
    ],
    open_task=task("Planea una mini muestra cultural de tres cosas del curso: una comida típica (empanada, sopaipilla o humita), un juego (rayuela, trompo o volantín) y un baile o música (cueca). Para cada una, escribe una frase que diga qué es y de dónde viene. Agrega una regla de respeto que seguirás. Si presentas algo de un pueblo originario, pide ayuda a su comunidad o a un educador tradicional.", "Empanada: comida típica de Chile. Rayuela: juego que se juega en el patio. Cueca: baile nacional. Regla: no me burlaré de nadie.", ["tres expresiones", "una frase para cada una", "una regla de respeto"], ["plan escrito con las tres frases"], ["burlarse", "inventar el origen"], "Pide que explique por qué cada expresión da sentido de pertenencia."),
    reinforce="Cuenta a alguien de tu casa qué expresión cultural te hace sentir más parte de Chile.",
    extend="Escribe dos reglas más de respeto para una muestra cultural.",
)

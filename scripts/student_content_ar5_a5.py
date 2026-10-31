"""Cuaderno del estudiante de 5.º básico Artes Visuales: AR05 OA 05 (describir y comparar trabajos personales y de pares)."""
from __future__ import annotations

from student_content_ar5_a import lesson, m, task, w
from student_lessons import ex

OA5 = "AR05 OA 05"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Hoja y lápiz. Los dos trabajos de ejemplo (de Ana y de Luis) están descritos en esta clase; también puedes usar uno de tus propios trabajos y, si quieres, el de un compañero con su permiso.",
    "Aprenderé a describir un trabajo de arte o diseño con cuatro criterios: materiales y procedimientos, lenguaje visual, propósito expresivo, y fortalezas y aspectos a mejorar. Sirve para hablar de mi trabajo y del de otras personas con datos y respeto.",
    ["Sé separar una observación de una opinión.", "Sé que cada trabajo tiene una intención."],
    [
        "Describir un trabajo es decir qué tiene, con datos que se ven, sin opinar si es bonito o feo. Para hacerlo bien uso cuatro criterios. El primero son los materiales y procedimientos: con qué y cómo se hizo. El segundo es el lenguaje visual: qué colores, líneas, formas, texturas, luz y sombra tiene. El tercero es el propósito expresivo: qué quiso comunicar su autor. El cuarto son las fortalezas y los aspectos a mejorar.",
        "Una fortaleza es algo que funciona bien y ayuda al propósito. Un aspecto a mejorar es algo que podría funcionar mejor. Los dos se explican con datos del trabajo. Por ejemplo, si el propósito es calma, las líneas largas y horizontales son una fortaleza. Un manchón oscuro que rompe la calma es un aspecto a mejorar. Hablo del trabajo, nunca de las personas.",
        "Trabajo de Ana: un paisaje de lago en témpera con mucha agua. Tiene colores celestes y verdes claros, líneas largas y horizontales. Su propósito es mostrar calma. El cielo tiene grumos de pintura y un manchón oscuro en una esquina. Trabajo de Luis: un volcán de cartón y arcilla, con base ancha y textura rugosa, de colores rojo y negro. Su propósito es mostrar fuerza. Una parte del cartón se despegó. Usaré estas dos descripciones para practicar.",
    ],
    [("describir", "decir qué tiene un trabajo, con datos que se ven"), ("propósito expresivo", "lo que su autor quiso comunicar con el trabajo"), ("fortaleza", "algo que funciona bien y ayuda al propósito"), ("aspecto a mejorar", "algo que podría funcionar mejor"), ("criterio", "regla que uso para mirar y decidir")],
    [
        w("Describir con los cuatro criterios", "Describe el trabajo de Luis con los cuatro criterios.", ["Materiales y procedimientos: cartón y arcilla.", "Lenguaje visual: base ancha, textura rugosa, rojo y negro.", "Propósito: mostrar fuerza. Fortaleza: la base ancha ayuda a sostenerlo. A mejorar: se despegó una parte del cartón."], "Cartón y arcilla; base ancha, textura rugosa, rojo y negro; fuerza; fortaleza: la base ancha; a mejorar: el cartón despegado"),
        w("Fortaleza o aspecto a mejorar", "En el trabajo de Ana hay un manchón oscuro en una esquina del cielo y su propósito es la calma. ¿Qué es el manchón?", ["Miro el propósito: calma.", "El manchón oscuro rompe la calma.", "Entonces es un aspecto a mejorar."], "Un aspecto a mejorar"),
    ],
    [
        m("Decir «es lindo» o «es feo» como si fuera una descripción.", "Es una opinión y no dice qué tiene el trabajo.", "Describe materiales, colores, líneas y propósito."),
        m("Hablar de la persona en lugar de su trabajo («Ana pinta mal»).", "No se refiere a datos del trabajo y puede ofender.", "Habla del trabajo con datos."),
    ],
    [
        ex("Trabajo de Ana: paisaje de lago en témpera, de colores celestes y verdes claros, con líneas largas y horizontales y propósito de calma. ¿Qué material usó?", "Témpera", "La descripción dice que está hecho en témpera."),
        ex("Trabajo de Luis: volcán de cartón y arcilla, con propósito de fuerza. ¿Qué propósito tiene?", "Mostrar fuerza", "La descripción lo dice."),
        ex("En el trabajo de Ana, ¿qué colores usó: celestes y verdes claros o rojo y negro?", "Celestes y verdes claros", "Esos son los colores de su lago."),
    ],
    [
        ex("«Líneas largas y horizontales» en el trabajo de Ana, ¿es un dato de lenguaje visual o de materiales?", "De lenguaje visual", "Las líneas son un elemento del lenguaje visual."),
        ex("«Una parte del cartón se despegó» en el trabajo de Luis, ¿es una fortaleza o un aspecto a mejorar?", "Un aspecto a mejorar", "Es un problema técnico del trabajo."),
        ex("La base ancha del volcán de Luis ayuda a que se sostenga. ¿Es una fortaleza o un aspecto a mejorar?", "Una fortaleza", "Ayuda a que el trabajo funcione."),
    ],
    [
        ex("¿Cuál NO es uno de los cuatro criterios de la clase: el nombre del autor, el propósito expresivo o el lenguaje visual?", "El nombre del autor", "Los criterios son materiales y procedimientos, lenguaje visual, propósito y fortalezas o aspectos a mejorar."),
        ex("¿Cuál es una buena descripción del volcán de Luis? A: «Es horrible». B: «Volcán de cartón y arcilla, con base ancha y textura rugosa».", "B", "La B nombra materiales y rasgos que se ven."),
        ex("Quieres describir tu propio trabajo. ¿Qué haces primero: mirarlo y anotar datos o decir si te gustó?", "Mirarlo y anotar datos", "La descripción se apoya en datos."),
    ],
    [
        ex("Ana quería mostrar calma y Luis quería mostrar fuerza. Un compañero dice que el trabajo de Ana es mejor porque tiene colores más claros. ¿Es una buena razón, si los propósitos son distintos?", "No", "Cada propósito pide decisiones distintas."),
        ex("El volcán de Luis busca mostrar fuerza y es rugoso, rojo y negro. ¿Esas decisiones ayudan a su propósito?", "Sí", "La textura rugosa y los colores intensos dan sensación de fuerza."),
    ],
    [
        ex("El manchón oscuro en el cielo del lago de Ana, ¿ayuda al propósito de calma o se opone a él?", "Se opone a él", "Un manchón oscuro rompe la sensación de calma."),
        ex("Para describir tu propio trabajo con honestidad, ¿incluyes solo lo que salió bien o lo que salió bien y lo que puedes mejorar?", "Lo que salió bien y lo que puedes mejorar", "Así la descripción es completa y honesta."),
    ],
    ex("Un niño de tu curso te muestra un perro de plasticina con bigotes de lana y dice que quiso mostrar alegría. ¿Cuál es el propósito expresivo del trabajo?", "Mostrar alegría", "El autor lo dijo."),
    [
        ex("Verdadero o falso: describir es decir si el trabajo me gusta.", "Falso", "Es decir qué tiene el trabajo con datos."),
        ex("¿Cuántos criterios usa la clase para describir un trabajo?", "Cuatro", "Materiales y procedimientos, lenguaje visual, propósito, y fortalezas y aspectos a mejorar."),
        ex("Verdadero o falso: hablo del trabajo y no de la persona.", "Verdadero", "Los comentarios se refieren a lo que hay en el trabajo."),
    ],
    task(
        "Elige UN trabajo para describir. A) el de Ana; B) el de Luis; C) uno tuyo. Escribe una ficha con los cuatro criterios: materiales y procedimientos; lenguaje visual; propósito expresivo; una fortaleza y un aspecto a mejorar, cada uno con un dato que se vea.",
        "Elegí el trabajo de Ana. Materiales: témpera con mucha agua. Lenguaje visual: celestes y verdes claros, líneas largas y horizontales. Propósito: mostrar calma. Fortaleza: las líneas largas y horizontales ayudan a la calma. A mejorar: el manchón oscuro del cielo rompe la calma.",
        ["usa los cuatro criterios", "da datos que se ven", "explica fortaleza y aspecto a mejorar según el propósito", "habla del trabajo y no de la persona"],
        ["ficha de cuatro criterios", "una fortaleza y un aspecto a mejorar"],
        ["opinar sin datos", "hablar de la persona"],
        "Destaca la ficha con datos más claros y pregunta qué dato apoya la fortaleza elegida.",
    ),
    "Mira un trabajo tuyo y di en voz alta un dato de cada criterio.",
    "Describe dos trabajos tuyos de fechas distintas con la misma ficha de cuatro criterios.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Hoja y lápiz. Los trabajos de Ana y de Luis están descritos en esta clase. Puedes hacer una tabla de dos columnas en tu hoja.",
    "Aprenderé a comparar dos trabajos mirando un criterio a la vez y a escribir parecidos y diferencias con datos. Sirve para entender mejor cada trabajo sin decir que uno vale más que el otro.",
    ["Sé describir un trabajo con cuatro criterios.", "Sé que cada trabajo tiene un propósito propio."],
    [
        "Comparar es mirar dos trabajos juntos para ver en qué se parecen y en qué se diferencian. Para hacerlo ordenado, uso un criterio a la vez: primero los materiales y procedimientos, luego el lenguaje visual, luego el propósito. Una tabla de dos columnas ayuda: en cada fila anoto el criterio y los datos de cada trabajo.",
        "Trabajo de Ana: témpera con mucha agua, colores celestes y verdes claros, líneas largas y horizontales, propósito de calma, con grumos y un manchón oscuro. Trabajo de Luis: cartón y arcilla, base ancha, textura rugosa, colores rojo y negro, propósito de fuerza, con una parte despegada. Comparados por materiales, son distintos. Por propósito, son distintos. Por tener un aspecto técnico por mejorar, son parecidos.",
        "Al comparar no digo «este es mejor». Digo en qué se parecen y en qué se diferencian, y luego si cada uno logra su propósito. Un material no es mejor que otro en general: depende de lo que quiero comunicar. Si los propósitos son distintos, comparo si cada trabajo cumple el suyo. Así la comparación es justa.",
    ],
    [("comparar", "mirar dos trabajos para ver en qué se parecen y en qué se diferencian"), ("semejanza", "algo parecido entre dos trabajos"), ("diferencia", "algo distinto entre dos trabajos"), ("tabla comparativa", "tabla con un criterio por fila y los datos de cada trabajo"), ("justo", "que usa el mismo criterio para los dos trabajos")],
    [
        w("Comparar por un criterio", "Compara los colores de Ana (celestes y verdes claros) y de Luis (rojo y negro).", ["Los colores de Ana son claros y fríos.", "Los de Luis son oscuros e intensos.", "La diferencia: claros y suaves frente a oscuros e intensos."], "Ana usa colores claros y suaves; Luis usa colores oscuros e intensos"),
        w("Comparar el cumplimiento del propósito", "Ana quiere calma y usa colores claros y líneas largas. Luis quiere fuerza y usa rojo, negro y textura rugosa. ¿Cuál logra mejor su propósito?", ["Cada uno tiene un propósito distinto.", "Comparo cada uno con el suyo.", "Las decisiones de ambos ayudan a su propósito."], "Los dos lo logran en sus decisiones principales"),
    ],
    [
        m("Decir «el de Ana es mejor porque la témpera es mejor que el cartón».", "Un material no es mejor en general.", "Compara si el material ayuda al propósito de cada trabajo."),
        m("Comparar un trabajo por un criterio y el otro por otro.", "La comparación no es justa.", "Usa el mismo criterio para los dos."),
    ],
    [
        ex("Trabajo de Ana: témpera, colores claros. Trabajo de Luis: cartón y arcilla, rojo y negro. ¿Qué trabajo usa témpera?", "El de Ana", "La descripción dice que Ana usó témpera."),
        ex("¿Qué trabajo tiene textura rugosa: el de Ana o el de Luis?", "El de Luis", "El volcán de Luis es rugoso."),
        ex("Para comparar, ¿miras un criterio a la vez o todos mezclados?", "Un criterio a la vez", "Así la comparación es ordenada."),
    ],
    [
        ex("Los propósitos de Ana (calma) y de Luis (fuerza), ¿son parecidos o distintos?", "Distintos", "Calma y fuerza son propósitos diferentes."),
        ex("¿Qué trabajo usa colores más oscuros: el de Ana o el de Luis?", "El de Luis", "Rojo y negro son más oscuros que celeste y verde claro."),
        ex("Ana tiene grumos y un manchón oscuro; Luis tiene una parte de cartón despegada. ¿Qué tienen en común ambos trabajos: un detalle técnico por mejorar o ninguno?", "Un detalle técnico por mejorar", "Los dos tienen un aspecto técnico que se puede mejorar."),
    ],
    [
        ex("¿Qué trabajo tiene mayor contraste entre sus colores: el de Ana (celeste y verde claro) o el de Luis (rojo y negro)?", "El de Luis", "El rojo y el negro se diferencian mucho."),
        ex("Quieres comparar «témpera» con «cartón y arcilla». ¿Qué criterio usas: materiales y procedimientos o propósito?", "Materiales y procedimientos", "Se comparan los materiales."),
        ex("¿Cuál es una frase comparativa válida? A: «Ana usa colores claros y Luis usa rojo y negro». B: «Ana es mejor que Luis».", "A", "La A compara con datos; la B no explica nada."),
    ],
    [
        ex("Comparas por el criterio de material y dices: «Ana es mejor porque la témpera es mejor que el cartón». ¿Es un buen argumento?", "No", "Un material no es mejor que otro en general; depende del propósito."),
        ex("Ana y Luis tienen propósitos distintos. Para saber si cada uno logra su propósito, ¿usas el propósito de cada uno o el mismo propósito para los dos?", "El propósito de cada uno", "Cada trabajo se compara con lo que quería comunicar."),
    ],
    [
        ex("Quieres comparar tu trabajo de hace un mes con el de ahora para ver cuánto avanzaste. ¿Usas los mismos criterios en los dos?", "Sí", "Con criterios distintos no se puede comparar."),
        ex("Una tabla comparativa tiene una fila por criterio y una columna por trabajo. Con 3 criterios y 2 trabajos, ¿cuántas casillas de datos tiene?", "6", "Multiplica 3 criterios por 2 trabajos.", calc="3*2"),
    ],
    ex("En clase, dos compañeros muestran un dibujo con témpera y otro con lápices. La profesora pregunta en qué se parecen. ¿Qué respondes: que ambos usan color o que uno es más lindo?", "Que ambos usan color", "Una semejanza se dice con un dato."),
    [
        ex("Verdadero o falso: comparar es decir cuál trabajo vale más.", "Falso", "Comparar es ver semejanzas y diferencias."),
        ex("¿Qué se usa para organizar la comparación?", "Una tabla comparativa", "Cada fila tiene un criterio."),
        ex("Verdadero o falso: se compara cada trabajo con su propio propósito.", "Verdadero", "Así la comparación es justa."),
    ],
    task(
        "Elige UNA pareja de trabajos. A) el de Ana y el de Luis. B) dos trabajos tuyos de fechas distintas. C) uno tuyo y el de Ana o Luis. Haz una tabla con tres filas (materiales y procedimientos, lenguaje visual y propósito) y escribe una semejanza y una diferencia en cada una. Cierra con una frase: cuál logra su propósito y por qué.",
        "Elegí A. Materiales: Ana usa témpera, Luis usa cartón y arcilla (diferencia). Lenguaje visual: los colores son distintos (diferencia); los dos usan solo dos colores principales (semejanza). Propósito: calma frente a fuerza (diferencia). Cada uno logra su propósito porque sus colores y texturas combinan con él.",
        ["usa un criterio por fila", "escribe semejanzas y diferencias con datos", "compara cada trabajo con su propósito", "no dice que uno vale más"],
        ["tabla de tres filas", "una frase de cierre"],
        ["comparar con criterios distintos", "decir cuál es mejor sin razón"],
        "Destaca la tabla más clara y pregunta qué semejanza fue más difícil de encontrar.",
    ),
    "Mira dos objetos de tu casa y di una semejanza y una diferencia en su material.",
    "Compara tres trabajos tuyos y ordénalos según cuánto cumplen su propósito, explicando cada decisión.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Hoja y lápiz. Los trabajos están descritos en esta clase. Si quieres, usa un trabajo tuyo reciente para mirar cómo usaste los materiales.",
    "Aprenderé a evaluar cómo se usaron los materiales y procedimientos en un trabajo, identificando fortalezas y aspectos a mejorar, y a proponer cambios concretos. Sirve para mejorar la técnica sin cambiar la idea.",
    ["Sé describir y comparar dos trabajos.", "Sé qué es una fortaleza y un aspecto a mejorar."],
    [
        "Cuando miro cómo se usaron los materiales y procedimientos, me pregunto: ¿ayudaron al propósito?, ¿se usaron con cuidado?, ¿hay problemas técnicos que se puedan corregir? Un problema técnico es un detalle de ejecución, como pegamento visible, pintura chorreada, cortes chuecos o piezas que se despegan. Tiene una causa y una solución.",
        "Veamos dos ejemplos. Trabajo C: una pintura con témpera en la que el estudiante esperó que cada capa se secara; los colores se ven limpios. Es una fortaleza: la técnica ayuda a que se vean los colores. Trabajo D: un afiche con papeles pegados con mucho pegamento; el papel quedó arrugado y con bultos. Es un aspecto a mejorar. La causa es demasiado pegamento, y la solución es usar una capa fina y repartirla parejo.",
        "Un buen comentario técnico nombra el problema, su causa y una sugerencia. «Está mal pegado» no ayuda. «El papel tiene bultos por demasiado pegamento; prueba con una capa fina» sí ayuda. Así quien recibe el comentario sabe qué hacer. También reconozco las fortalezas técnicas: cortes parejos, colores limpios, buena unión, orden en el trabajo. La técnica se mejora con práctica, y todos pueden mejorarla.",
    ],
    [("problema técnico", "detalle de ejecución que se puede corregir, como pegamento visible o cortes chuecos"), ("causa", "razón por la que ocurre un problema"), ("sugerencia", "propuesta concreta para mejorar"), ("ejecución", "cómo se realizó un trabajo"), ("capa fina", "una cantidad pequeña y pareja de pegamento o pintura")],
    [
        w("Problema, causa y sugerencia", "En el trabajo D, el papel quedó arrugado y con bultos. Escribe problema, causa y sugerencia.", ["Problema: papel arrugado con bultos.", "Causa: demasiado pegamento.", "Sugerencia: una capa fina, repartida parejo."], "Papel arrugado; demasiado pegamento; usar una capa fina"),
        w("Reconocer una fortaleza", "En el trabajo C, la persona esperó que cada capa se secara. ¿Qué fortaleza técnica hay?", ["Miro el resultado: colores limpios.", "Esperar el secado evita que se mezclen.", "Es una fortaleza de procedimiento."], "Esperó el secado y los colores se ven limpios"),
    ],
    [
        m("Decir solo «está mal hecho» sin explicar.", "No sirve para mejorar.", "Di el problema, la causa y una sugerencia."),
        m("Pensar que un problema técnico significa que la idea es mala.", "La idea y la ejecución son cosas distintas.", "Separa la idea de cómo se hizo."),
    ],
    [
        ex("Trabajo C: pintura en la que cada capa esperó el secado y los colores se ven limpios. ¿Esperar el secado es una fortaleza o un aspecto a mejorar?", "Una fortaleza", "Ayuda a que los colores se vean limpios."),
        ex("Trabajo D: papeles pegados con mucho pegamento, quedó arrugado y con bultos. ¿Qué falló: la cantidad de pegamento o el color del papel?", "La cantidad de pegamento", "El exceso de pegamento arruga el papel."),
        ex("Un problema técnico, ¿es un detalle de ejecución que se puede corregir o la idea del trabajo?", "Un detalle de ejecución que se puede corregir", "No es la idea, sino cómo se hizo."),
    ],
    [
        ex("Para mejorar el trabajo D, ¿qué sugerencia sirve: usar una capa fina de pegamento o usar más pegamento?", "Usar una capa fina de pegamento", "Menos pegamento evita bultos y arrugas."),
        ex("Un cartel de témpera tiene la pintura chorreada hacia abajo. ¿Cuál es la causa probable: demasiada agua o muy poca agua?", "Demasiada agua", "Mucha agua hace que la pintura corra."),
        ex("Una pieza de arcilla se rompió al unirla seca con otra. ¿Qué sugerencia ayuda: unirlas cuando aún están blandas, rayando y humedeciendo, o unirlas cuando están duras?", "Unirlas cuando aún están blandas, rayando y humedeciendo", "Así las piezas quedan unidas."),
    ],
    [
        ex("Quieres pintar los detalles finos del ojo de un animal. ¿Es adecuado un pincel muy grueso?", "No", "Para detalles finos conviene un pincel fino."),
        ex("Un trabajo de cartón tiene un corte chueco. ¿El problema está en el material o en la ejecución?", "En la ejecución", "El corte se mejora con una línea guía y regla."),
        ex("Escribes un comentario técnico. ¿Qué incluyes: problema, causa y sugerencia o solo si te gusta?", "Problema, causa y sugerencia", "Eso ayuda a mejorar."),
    ],
    [
        ex("Dos comentarios sobre el afiche D. Comentario 1: «Está mal pegado». Comentario 2: «El papel tiene bultos por demasiado pegamento; prueba con una capa fina». ¿Cuál es más útil?", "El 2", "Dice problema, causa y sugerencia."),
        ex("Dos estudiantes pintan con la misma témpera y el mismo papel. Uno espera que cada capa se seque y sus colores quedan limpios; el otro pinta sobre la capa mojada y se ensucian. ¿La diferencia se debe al material o al procedimiento?", "Al procedimiento", "Usaron el mismo material; cambió cómo lo usaron."),
    ],
    [
        ex("Para saber si el material ayudó al propósito de «suavidad», ¿miras el efecto en el trabajo o el precio del material?", "El efecto en el trabajo", "Se evalúa si logra el propósito."),
        ex("Un volcán de cartón se cae porque su base es angosta. ¿Qué parte del trabajo cambias para mejorarlo sin cambiar la idea: la base o el tema?", "La base", "El problema es técnico y la idea sigue igual."),
    ],
    ex("Tu compañera te muestra su trabajo y pregunta qué puede mejorar. ¿Qué dices: «El papel tiene bultos por mucho pegamento; usa una capa fina» o «Se ve feo»?", "El papel tiene bultos por mucho pegamento; usa una capa fina", "Es específico y propone una mejora."),
    [
        ex("Verdadero o falso: un problema técnico siempre significa que la idea es mala.", "Falso", "La idea y la ejecución son distintas."),
        ex("¿Qué tres partes tiene un comentario técnico útil?", "Problema, causa y sugerencia", "Con eso se sabe qué hacer."),
        ex("Verdadero o falso: esperar el secado de la pintura es parte de un buen procedimiento.", "Verdadero", "Evita que se mezclen los colores."),
    ],
    task(
        "Elige UN trabajo para evaluar su técnica. A) el afiche D: papeles bien cortados y ordenados, pegados con mucho pegamento, arrugado y con bultos. B) un trabajo tuyo reciente. C) esta escena: «un volcán de cartón con textura rugosa bien lograda y una base angosta que se cae». Escribe una fortaleza técnica y un problema técnico con su causa y una sugerencia concreta. Si es tu trabajo, aplica la sugerencia.",
        "Elegí el afiche D. Fortaleza: los papeles están ordenados y bien cortados. Problema: papel arrugado con bultos. Causa: demasiado pegamento. Sugerencia: usar una capa fina de pegamento y repartirla parejo.",
        ["nombra una fortaleza técnica", "nombra un problema con su causa", "da una sugerencia concreta", "no cambia la idea del trabajo"],
        ["una fortaleza", "problema, causa y sugerencia"],
        ["decir «está mal» sin explicar", "mezclar la idea con la técnica"],
        "Destaca la sugerencia más concreta y pregunta cómo se sabría que funcionó.",
    ),
    "Mira un objeto hecho a mano en tu casa y di una cosa bien hecha y una que se podría mejorar.",
    "Revisa un trabajo tuyo y escribe tres comentarios técnicos con problema, causa y sugerencia.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Un trabajo tuyo reciente (o el trabajo de Ana descrito en esta clase), lápiz, colores y una hoja para anotar. Si mejoras el trabajo en papel, guarda una copia del antes.",
    "Aprenderé a hacer un plan de mejora para mi propio trabajo, aplicar un cambio y comparar el antes y el después. Sirve para mejorar de manera concreta y comprobar que el cambio funcionó.",
    ["Sé describir mi trabajo con cuatro criterios.", "Sé escribir un problema técnico con causa y sugerencia."],
    [
        "Un plan de mejora dice qué voy a cambiar, cómo y para qué. Debe ser concreto, es decir, que se pueda ver, y realizable en el tiempo que tengo. «Quiero que se vea mejor» no es un plan. «Voy a pintar el cielo de nuevo con la pintura bien mezclada para evitar grumos» sí lo es. Primero elijo un aspecto a mejorar de mi descripción, el que más afecta a mi propósito.",
        "Luego aplico el cambio y cambio solo una cosa a la vez, para saber si funcionó. Si cambio el cielo y también el tema, no sabré cuál cambio causó la mejora. Al final comparo el antes y el después con los mismos criterios y escribo si mejoró y por qué. Si el cambio altera mi propósito, ya no es una mejora sino una nueva intención.",
        "Veamos el trabajo de Ana: lago en témpera, colores claros, propósito de calma, con grumos en el cielo y un manchón oscuro. Un plan de mejora: «Cubriré el manchón oscuro con celeste claro para que no rompa la calma». Después de aplicarlo, ella compara: el cielo se ve más parejo y el propósito se nota mejor. Mejorar es un proceso, no un fracaso.",
    ],
    [("plan de mejora", "decisión concreta de qué, cómo y para qué voy a cambiar"), ("antes y después", "comparación del trabajo antes y después del cambio"), ("concreto", "que se puede ver y comprobar"), ("realizable", "que se puede hacer en el tiempo y con los materiales que tengo"), ("proceso", "serie de pasos para hacer o mejorar un trabajo")],
    [
        w("Plan concreto", "Dos planes para el lago de Ana. Plan 1: «que se vea mejor». Plan 2: «cubrir el manchón oscuro del cielo con celeste claro». ¿Cuál es concreto?", ["Reviso qué se puede ver y comprobar.", "El plan 2 dice qué, cómo y para qué.", "El plan 1 es vago."], "El plan 2"),
        w("Comparar el antes y el después", "Antes: cielo con manchón oscuro. Después: cielo celeste parejo. El propósito es calma. ¿Mejoró?", ["Miro el propósito: calma.", "El cielo parejo ayuda a la calma.", "Entonces mejoró."], "Sí, mejoró"),
    ],
    [
        m("Cambiar muchas cosas al mismo tiempo y creer que sabes cuál ayudó.", "No se sabe qué cambio funcionó.", "Cambia una cosa a la vez y compara."),
        m("Cambiar el propósito del trabajo y decir que mejoró.", "Es otra intención, no una mejora.", "Mantén tu propósito al mejorar."),
    ],
    [
        ex("¿Cuál plan de mejora es concreto? A: «que quede mejor». B: «pintar el cielo de nuevo con la pintura bien mezclada para evitar grumos».", "B", "La B dice qué, cómo y para qué."),
        ex("Después de mejorar, ¿comparas con el trabajo anterior o no?", "Sí, comparas con el anterior", "Así se sabe si funcionó."),
        ex("Para saber si una mejora funcionó, ¿cambias una cosa o muchas a la vez?", "Una cosa", "Así se sabe qué produjo el cambio."),
    ],
    [
        ex("Aplicar una capa fina de pegamento, ¿es una mejora de materiales y procedimientos o del propósito?", "De materiales y procedimientos", "Cambia cómo se hizo el trabajo."),
        ex("Cubrir un manchón oscuro con celeste en un lago que busca calma, ¿mejora el lenguaje visual o el material?", "El lenguaje visual", "Cambia el color del cielo."),
        ex("Un plan realizable es el que se puede hacer en el tiempo que tienes. ¿Qué es más realizable en 30 minutos: repintar una esquina o rehacer todo un mural grande?", "Repintar una esquina", "Es una tarea corta."),
    ],
    [
        ex("Ordena los pasos: A) comparar el antes y el después, B) elegir una mejora concreta, C) aplicar la mejora. Escribe las tres letras en orden.", "B, C, A", "Primero eliges, luego aplicas y después comparas."),
        ex("Antes: cielo con grumos. Después: cielo liso, y el propósito de calma se nota más. ¿Hubo mejora?", "Sí", "El cambio ayudó al propósito."),
        ex("Tu cambio pasó el trabajo de calma a miedo. ¿Es una mejora o un cambio de intención?", "Un cambio de intención", "El propósito original era otro."),
    ],
    [
        ex("Luis aumentó la base de su volcán porque la base angosta se caía. ¿Es una mejora relacionada con un aspecto real a mejorar?", "Sí", "La base angosta era un problema técnico."),
        ex("Mejoraste el cielo y además cambiaste el tema a otra escena. ¿Puedes saber si el cambio del cielo funcionó?", "No", "Cambiaste demasiadas cosas a la vez."),
    ],
    [
        ex("Tienes 5 aspectos por mejorar y tiempo para 2. ¿Eliges los 2 que más afectan al propósito o los 2 más fáciles?", "Los 2 que más afectan al propósito", "Así la mejora tiene mayor efecto."),
        ex("Tu plan dice: «Cambiaré el pincel grueso por uno fino para los detalles del árbol». ¿Es un plan concreto?", "Sí", "Dice qué, cómo y para qué."),
    ],
    ex("Quieres mejorar un dibujo para el diario mural. Tienes una copia del antes. ¿Qué haces después de aplicar el cambio: lo comparas con la copia o lo guardas sin mirar?", "Lo comparas con la copia", "Así ves con evidencia si mejoró."),
    [
        ex("Verdadero o falso: un plan de mejora debe ser concreto.", "Verdadero", "Debe decir qué, cómo y para qué."),
        ex("¿Qué se compara al final de la mejora?", "El antes y el después", "Es la forma de comprobar el cambio."),
        ex("Verdadero o falso: mejorar un trabajo es lo mismo que cambiar su intención.", "Falso", "Se mejora la ejecución, no el propósito."),
    ],
    task(
        "Elige UN trabajo. A) el lago de Ana (grumos y un manchón oscuro; propósito: calma). B) un trabajo tuyo. Escribe tu plan de mejora con tres partes: qué cambias, cómo y para qué. Aplica UN cambio. Compara el antes y el después en una frase y di si mejoró.",
        "Elegí el lago de Ana. Plan: cubrir el manchón oscuro del cielo (qué) con celeste claro aplicado con poca agua (cómo) para no romper la calma (para qué). Después de aplicar el cambio, el cielo se ve parejo y la calma se nota más. Mejoró.",
        ["elige un aspecto concreto", "escribe qué, cómo y para qué", "cambia una cosa a la vez", "compara el antes y el después"],
        ["plan de tres partes", "trabajo mejorado", "frase de comparación"],
        ["plan vago", "cambiar el propósito"],
        "Destaca el plan más concreto y pregunta cómo se vería el cambio sin la copia del antes.",
    ),
    "Piensa en un trabajo tuyo y di en voz alta un cambio concreto que harías.",
    "Haz una segunda mejora en el mismo trabajo y compara los tres momentos: original, primera mejora, segunda mejora.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA5, 5,
    "Hoja y lápiz. Los trabajos de Ana y de Luis están descritos en esta clase; también puedes usar un trabajo tuyo o el de un compañero con su permiso.",
    "Aprenderé a dar y recibir retroalimentación respetuosa y fundamentada: una fortaleza, un aspecto a mejorar y una sugerencia, con datos del trabajo. Sirve para ayudarnos a mejorar sin dañar a nadie.",
    ["Sé describir y comparar trabajos.", "Sé hacer un plan de mejora concreto."],
    [
        "La retroalimentación es decirle a alguien qué veo en su trabajo para ayudarle a mejorar. Una buena retroalimentación tiene tres partes. Primero, una fortaleza con su razón: «Las líneas largas y horizontales ayudan a mostrar calma». Segundo, un aspecto a mejorar con datos: «El manchón oscuro del cielo rompe esa calma». Tercero, una sugerencia concreta: «Podrías cubrirlo con celeste claro».",
        "Es importante que sea respetuosa. Hablo del trabajo y no de la persona. No digo «eres malo», digo «en este trabajo se ve…». No comparo a las personas ni digo quién es mejor. Uso el propósito del autor como guía: no pido lo que yo haría, sino lo que ayuda a lo que él o ella quiere comunicar. Y no escribo nombres ni datos personales en comentarios que otras personas puedan ver.",
        "Cuando recibo un comentario, lo escucho con calma y pienso si se relaciona con mi propósito. Puedo usarlo, adaptarlo o descartarlo, pero con una razón. Agradecer también es parte del respeto. Por ejemplo, si me dicen «agrega rojo fuerte» y mi propósito es calma, puedo decidir que no lo uso porque contradice mi idea. Dar y recibir retroalimentación es una forma de aprender entre todos.",
    ],
    [("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("respetuosa", "que cuida a la persona y habla del trabajo"), ("específica", "que nombra datos concretos del trabajo"), ("sugerencia", "propuesta concreta para mejorar"), ("descartar", "decidir no usar un comentario, con una razón")],
    [
        w("Armar la retroalimentación", "Arma una retroalimentación para el lago de Ana (colores claros, líneas largas, propósito de calma, manchón oscuro en el cielo).", ["Fortaleza: las líneas largas y horizontales ayudan a la calma.", "Aspecto a mejorar: el manchón oscuro del cielo rompe la calma.", "Sugerencia: cubrirlo con celeste claro."], "Líneas largas ayudan a la calma; el manchón oscuro la rompe; podrías cubrirlo con celeste claro"),
        w("Decidir qué usar", "Tu propósito es calma y alguien dice: «Agrega rayos rojos». ¿Qué haces?", ["Pienso en mi propósito: calma.", "Los rayos rojos dan tensión.", "Decido descartar el comentario y lo agradezco."], "Descartarlo con una razón y agradecer"),
    ],
    [
        m("Decir «eres malo para el arte» o «tu trabajo es feo».", "Daña a la persona y no ayuda a mejorar.", "Habla de datos del trabajo y propone una sugerencia."),
        m("Usar todos los comentarios sin pensar si ayudan a mi propósito.", "Puedo perder mi idea.", "Decide con una razón qué comentario usar."),
    ],
    [
        ex("«Tu trabajo tiene líneas largas que dan calma». ¿Es un comentario sobre el trabajo o sobre la persona?", "Sobre el trabajo", "Habla de las líneas del trabajo."),
        ex("«Eres malo para el arte». ¿Es un comentario respetuoso?", "No", "Habla de la persona y la daña."),
        ex("¿Cuál NO es una parte de una retroalimentación: la fortaleza, la sugerencia o el nombre completo del autor?", "El nombre completo del autor", "Las partes son fortaleza, aspecto a mejorar y sugerencia."),
    ],
    [
        ex("«Podrías mezclar bien la pintura para evitar los grumos». ¿Es una fortaleza o una sugerencia?", "Una sugerencia", "Propone un cambio concreto."),
        ex("¿Qué comentario nombra un dato del trabajo? A: «Me gustó». B: «Los colores claros ayudan a la calma».", "B", "La B nombra colores y los relaciona con el propósito."),
        ex("Un comentario dice: «Los rayos rojos van contra la calma». ¿Qué tipo de parte es: fortaleza o aspecto a mejorar?", "Aspecto a mejorar", "Señala algo que rompe el propósito."),
    ],
    [
        ex("Quieres comentar el lago de Ana. ¿Qué comentario es respetuoso y específico? A: «Esto está horrible». B: «El manchón oscuro del cielo rompe la calma; podrías cubrirlo con celeste claro».", "B", "Habla del trabajo, da un dato y propone un cambio."),
        ex("Recibes un comentario que no se relaciona con tu propósito. ¿Debes usarlo obligatoriamente?", "No", "Tú decides con una razón."),
        ex("Quieres escribir tu comentario en un mural donde todos lo verán. ¿Escribes el nombre y la dirección del autor?", "No", "No se deben publicar datos personales."),
    ],
    [
        ex("Tu propósito es calma y te piden «más rojo fuerte». ¿Aplicas ese comentario sin pensarlo?", "No", "Contradice la calma; conviene descartarlo con una razón."),
        ex("Dos comentarios sobre el volcán de Luis. 1: «Tu volcán es mejor que el mío». 2: «La base ancha ayuda a sostenerlo y la textura rugosa muestra fuerza». ¿Cuál describe el trabajo con criterios?", "El 2", "Habla de datos del trabajo y su propósito."),
    ],
    [
        ex("Un comentario dice solo: «Podrías mejorar». ¿Qué le falta?", "Decir qué mejorar y cómo", "Debe ser específico y dar una sugerencia."),
        ex("Recibes un comentario útil. ¿Qué haces: agradecerlo y pensar cómo usarlo o enojarte?", "Agradecerlo y pensar cómo usarlo", "Es parte de la retroalimentación respetuosa."),
    ],
    ex("Un compañero te muestra su trabajo y no sabe qué cambiar. Su propósito es fuerza y el volcán se cae por una base angosta. ¿Qué dices: «La textura rugosa muestra fuerza; la base angosta lo hace caerse; podrías ensancharla» o «No me gusta»?", "La textura rugosa muestra fuerza; la base angosta lo hace caerse; podrías ensancharla", "Tiene fortaleza, aspecto a mejorar y sugerencia."),
    [
        ex("Verdadero o falso: la retroalimentación habla del trabajo y no de la persona.", "Verdadero", "Es parte de ser respetuoso."),
        ex("¿Qué partes tiene una buena retroalimentación?", "Fortaleza, aspecto a mejorar y sugerencia", "Con eso se ayuda a mejorar."),
        ex("Verdadero o falso: debo usar todos los comentarios que me dan.", "Falso", "Decido con una razón según mi propósito."),
    ],
    task(
        "Elige UN trabajo. A) el lago de Ana. B) el volcán de Luis. C) un trabajo tuyo o de un compañero (con su permiso). Escribe una retroalimentación de tres partes: una fortaleza con su razón, un aspecto a mejorar con un dato y una sugerencia concreta. No uses nombres ni datos personales. Luego escribe cómo podría responder el autor al recibir el comentario.",
        "Elegí el volcán de Luis (propósito: fuerza). Fortaleza: la textura rugosa y los colores rojo y negro muestran fuerza. Aspecto a mejorar: una parte del cartón se despegó. Sugerencia: pegarla con una capa fina de pegamento y esperar que seque. El autor podría agradecerlo y aplicar la sugerencia.",
        ["escribe fortaleza, aspecto a mejorar y sugerencia", "usa datos del trabajo", "habla del trabajo y no de la persona", "no incluye datos personales"],
        ["retroalimentación de tres partes", "respuesta del autor"],
        ["hablar de la persona", "comentar sin datos"],
        "Destaca el comentario más específico y pregunta cómo sonaría recibirlo.",
    ),
    "Piensa en un trabajo que hayas visto y di en voz alta una fortaleza y una sugerencia para él.",
    "Pídele a una persona de tu casa que te dé una retroalimentación de tres partes sobre un trabajo tuyo y anota qué usarías.",
)

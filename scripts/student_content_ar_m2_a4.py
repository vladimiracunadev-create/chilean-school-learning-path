"""Cuaderno del estudiante de 2.º medio Artes Visuales: AR2M OA 04 (criterios estéticos y juicio crítico) y AR2M OA 05 (evaluación fundamentada)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA4 = "AR2M OA 04"
OA5 = "AR2M OA 05"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# =============================================================== OA 04
# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Hojas y lápiz. Las fichas de las obras de ejemplo (inventadas) están escritas en la clase: no necesitas buscar obras reales.",
    "Aprenderé a distinguir un criterio estético de una opinión y a nombrar criterios como composición, originalidad, expresividad, oficio y pertinencia. Sirve para argumentar por qué valoro una manifestación visual.",
    ["Sé separar descripción, interpretación y juicio.", "Sé que contexto, lenguaje visual y propósito ayudan a observar."],
    [
        "Un criterio estético es una razón que uso para valorar una manifestación visual. «Me gusta» no es un criterio, porque no se puede comprobar. Algunos criterios son: la composición (cómo se ordenan los elementos), la originalidad (qué tiene de nuevo o propio), la expresividad (cuánta emoción o idea comunica), el oficio (el cuidado en el manejo de la técnica y el material) y la pertinencia (si responde a su contexto y a su propósito).",
        "Las manifestaciones visuales son diversas: un afiche, un mural, una fotografía, una pieza de cerámica de uso diario, un diseño de ropa. No todo se valora con los mismos criterios. En una taza, la función y el oficio pesan mucho; en un afiche, la lectura a distancia; en una fotografía documental, la fidelidad a lo que se muestra. Elegir criterios adecuados al tipo de obra es parte del juicio.",
        "Un juicio crítico bien armado tiene tres partes: un rasgo que se ve (la evidencia), el criterio con que lo miro y la conclusión. Por ejemplo: «Las letras amarillas contrastan con el fondo azul (evidencia); por eso cumple el criterio de lectura a distancia (criterio); luego es pertinente para un muro de calle (conclusión)». Puedo valorar distinto que otra persona, pero debo dar razones.",
    ],
    [("criterio estético", "razón comprobable con que se valora una manifestación visual"), ("composición", "cómo se ordenan los elementos en la imagen"), ("originalidad", "aporte propio o nuevo de una obra"), ("expresividad", "capacidad de comunicar emoción o idea"), ("pertinencia", "ajuste de una obra a su contexto y propósito")],
    [
        w("Del gusto al criterio", "Una persona dice sobre un afiche de ejemplo: «Me gusta mucho». Reescribe la frase con criterio y evidencia. Datos: el afiche tiene un texto de 3 palabras en letras negras gruesas sobre fondo amarillo y se pega en un paradero.", ["Evidencia: texto corto, letras negras gruesas sobre amarillo.", "Criterio: lectura a distancia.", "Juicio: se lee rápido desde lejos, por eso es pertinente para un paradero."], "Se lee a distancia por el contraste de las letras negras sobre amarillo; es pertinente para un paradero"),
        w("Criterio según tipo de obra", "Dos fichas de ejemplo: una taza de cerámica de uso diario y un mural de calle. ¿Qué criterio pesa más en cada una?", ["Taza: se usa en la mano, importan función y oficio.", "Mural: se ve de lejos, importa la lectura a distancia.", "Cada obra pide criterios distintos."], "Taza: función y oficio; mural: lectura a distancia"),
    ],
    [
        m("Pensar que «me gusta» o «es bonito» ya es un criterio.", "No se puede comprobar mirando la obra.", "Nombra un rasgo visible y el criterio con que lo juzgas."),
        m("Aplicar los mismos criterios a cualquier manifestación.", "Un afiche, una taza y una fotografía cumplen funciones distintas.", "Elige criterios que correspondan al tipo de obra."),
    ],
    [
        ex("¿Qué es un criterio estético? A. Una razón comprobable para valorar una obra B. Un gusto personal sin razones.", "A", "El criterio se puede comprobar en la obra."),
        ex("¿Cuál es un criterio? A. Originalidad B. «Me cae bien el autor».", "A", "La originalidad se puede argumentar con rasgos de la obra."),
        ex("¿Qué es la composición? A. Cómo se ordenan los elementos en la imagen B. Los materiales con que se hizo.", "A", "Es la organización dentro del encuadre o del espacio."),
    ],
    [
        ex("Para valorar una taza de uso diario, ¿qué criterio importa mucho? A. La función B. La lectura a distancia.", "A", "La taza se usa en la mano."),
        ex("Dato: «los colores del mural son brillantes y contrastan con el muro gris». ¿Es evidencia o criterio? A. Evidencia B. Criterio.", "A", "Es un rasgo que se ve; el criterio sería, por ejemplo, la lectura a distancia."),
        ex("¿Qué criterio se refiere a si la obra responde a su contexto y propósito? A. Pertinencia B. Oficio.", "A", "Pertinencia es ajuste al contexto."),
    ],
    [
        ex("Ficha de ejemplo: fotografía de un patio vacío al amanecer, tomada de lejos, con un solo banco al centro. Frase: «La foto es expresiva porque el patio vacío y el banco solo podrían sugerir soledad». ¿Qué criterio usa? A. Expresividad B. Oficio.", "A", "Apoya la interpretación en lo que comunica."),
        ex("Obra de ejemplo: la costura de una chaqueta es pareja y sin hilos sueltos. ¿Qué criterio permite valorar eso? A. Oficio B. Originalidad.", "A", "El cuidado de la técnica es oficio."),
        ex("Un afiche de ejemplo repite una fórmula conocida, sin ningún aporte distinto. ¿Qué criterio resulta débil? A. Originalidad B. Composición.", "A", "Falta un aporte nuevo o propio."),
    ],
    [
        ex("Un compañero dice: «Ese cuadro es el mejor porque es caro». ¿Es un criterio estético? Responde sí o no.", "No", "El precio no describe rasgos visuales ni el cumplimiento de un criterio."),
        ex("Dos fichas de ejemplo: X es una pieza de cerámica bien terminada, pero sin aporte propio; Y es una pieza con un diseño nuevo, pero con bordes disparejos. Si valoras el oficio, ¿cuál destaca? A. X B. Y.", "A", "X tiene mejor manejo de la técnica."),
    ],
    [
        ex("Un mural de ejemplo tiene letras pequeñas y claras sobre fondo blanco y se mira desde 20 metros. ¿Qué criterio resulta débil? A. Lectura a distancia B. Originalidad.", "A", "Las letras pequeñas y claras no se leen desde lejos."),
        ex("Un amigo dice: «Todo el mundo opina que el afiche es excelente, así que lo es». ¿Qué le falta? A. Rasgos visibles y un criterio B. Más personas opinando.", "A", "Un juicio necesita evidencia y criterio, no solo la cantidad de opiniones."),
    ],
    ex("Ves en el patio de tu liceo un cartel que invita a una actividad. ¿Qué criterio revisas primero si se lee desde la puerta? A. Lectura a distancia B. Oficio de la técnica.", "A", "El cartel debe leerse desde donde la gente pasa."),
    [
        ex("Nombra tres criterios estéticos de la clase.", "Composición, originalidad y expresividad", "También sirven oficio y pertinencia."),
        ex("Verdadero o falso: un criterio puede ser «me gusta».", "Falso", "Un criterio es una razón comprobable."),
        ex("¿Qué tres partes tiene un juicio crítico?", "Evidencia, criterio y conclusión", "Así se argumenta con razones."),
    ],
    task(
        "Elige UNA ficha de ejemplo. A) Afiche «Cuida el agua»: letras blancas gruesas sobre fondo azul y una gota central, pegado en un baño. B) Taza «Mañana»: cerámica blanca con un asa firme y un dibujo de sol, pensada para usarse a diario. C) Fotografía «Banco»: un banco solo en un patio vacío al amanecer, tomada de lejos. Elige dos criterios que sean adecuados a ese tipo de obra y escribe un juicio con evidencia, criterio y conclusión.",
        "Elegí B. Criterios: función y oficio. Evidencia: el asa es firme y la taza tiene un borde parejo. Criterio: función. Conclusión: cumple su función porque se sostiene bien con la mano. Segunda evidencia: el dibujo del sol está centrado, pero no aporta mucho nuevo; eso me hace dudar de la originalidad.",
        ["elige criterios adecuados al tipo de obra", "separa evidencia, criterio y conclusión", "no usa «me gusta» como criterio", "da razones comprobables"],
        ["juicio con evidencia y criterio", "dos criterios nombrados"],
        ["usar «me gusta»", "los mismos criterios para todo"],
        "Pregunta qué rasgo de la ficha respalda cada criterio y si el criterio corresponde al tipo de obra.",
    ),
    "Mira un objeto de tu casa y escribe un criterio y un rasgo visible que lo respalda.",
    "Explica con tres frases por qué «me gusta» no basta como argumento.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Hojas y lápiz. Las fichas de las obras de ejemplo son inventadas y están escritas en la clase.",
    "Aprenderé a comparar dos manifestaciones visuales de ejemplo con el mismo criterio y a elegir criterios según el tipo de manifestación. Sirve para argumentar juicios con referentes diversos.",
    ["Sé nombrar criterios como composición, originalidad, expresividad, oficio y pertinencia.", "Sé que un juicio tiene evidencia, criterio y conclusión."],
    [
        "Para comparar dos obras uso el mismo criterio con ambas. Si comparo una con «oficio» y la otra con «originalidad», la comparación no es justa. Primero decido el criterio, después busco en cada obra un rasgo que lo muestre y por último concluyo cuál lo cumple mejor, o si lo cumplen igual pero de maneras distintas.",
        "Los referentes pueden venir de ámbitos diversos: arte de galería, diseño gráfico, artesanía, fotografía, arte de calle o vestuario. Cada ámbito tiene sus propios propósitos. Un objeto de artesanía puede valorarse por su oficio y su función, y un mural por su mensaje y su lectura a distancia. Por eso la selección de criterios depende de la obra y del contexto donde vive.",
        "Una comparación sirve para afinar mi mirada, no para decidir que una obra es «mejor» que otra en todo. Puedo concluir que una es más expresiva y la otra más precisa en su técnica. Todas las fichas de esta clase son de ejemplo y se describen por escrito. En la vida real, las obras y los autores reales se estudian con fuentes confiables que el docente aporta.",
    ],
    [("comparar", "mirar dos obras con el mismo criterio"), ("referente", "obra que sirve de modelo o de punto de comparación"), ("ámbito", "campo de la creación visual, como diseño, artesanía o fotografía"), ("oficio", "cuidado en el manejo de la técnica y el material"), ("fuente confiable", "texto o persona experta que informa con datos comprobables")],
    [
        w("Comparar con un criterio", "Criterio: expresividad. Obra X de ejemplo: fotografía de un abrigo colgado en una puerta vacía, con una luz fría; podría sugerir ausencia. Obra Y de ejemplo: fotografía de un abrigo en una percha, con luz pareja, sin otros elementos. ¿Cuál cumple mejor el criterio?", ["En X, la luz fría y la puerta vacía sugieren una idea (ausencia).", "En Y no hay elementos que sugieran una idea.", "Conclusión: X es más expresiva."], "La obra X, porque sugiere una idea con su luz y su puerta vacía"),
        w("Elegir criterios por ámbito", "Dos referentes de ejemplo: un banco de madera hecho por un artesano y un afiche de una campaña escolar. ¿Qué criterios eliges para cada uno?", ["Banco: función, oficio.", "Afiche: mensaje, lectura a distancia.", "Cada ámbito exige criterios propios."], "Banco: función y oficio; afiche: mensaje y lectura a distancia"),
    ],
    [
        m("Comparar dos obras con criterios distintos para cada una.", "La comparación deja de ser justa.", "Escoge un solo criterio y aplícalo a ambas."),
        m("Concluir que una obra es «mejor» en todo.", "Cada obra puede destacar en un criterio distinto.", "Di en qué criterio destaca cada una."),
    ],
    [
        ex("Para comparar dos obras con justicia, ¿qué debes usar? A. El mismo criterio para ambas B. Un criterio distinto para cada una.", "A", "Así la comparación es equivalente."),
        ex("¿Qué es un ámbito de la creación visual? A. Un campo, como el diseño o la artesanía B. Una técnica, como el esténcil.", "A", "Agrupa manifestaciones con propósitos parecidos."),
        ex("Un banco de madera hecho por un artesano, ¿qué criterio pesa mucho? A. Función y oficio B. Solo la lectura a distancia.", "A", "Se usa y depende de la técnica."),
    ],
    [
        ex("Dos obras de ejemplo: X tiene un rasgo que muestra expresividad y Y no. Con el criterio «expresividad», ¿qué concluyes? A. X cumple mejor el criterio B. Ambas lo cumplen igual.", "A", "Solo X tiene el rasgo."),
        ex("¿Cuál es una fuente confiable para estudiar una obra real? A. Un texto de un museo o de un especialista que aporta tu docente B. Un comentario anónimo.", "A", "Una fuente confiable informa con datos comprobables."),
        ex("Obra de ejemplo: un mural con letras negras sobre amarillo. ¿Qué criterio muestra con claridad? A. Lectura a distancia B. Función de la cerámica.", "A", "El contraste ayuda a leerlo desde lejos."),
    ],
    [
        ex("Comparas dos afiches de ejemplo con el criterio «lectura a distancia». P: letras de 15 cm, contraste fuerte. Q: letras de 2 cm, contraste débil. Se verán desde 8 m. ¿Cuál cumple mejor? A. P B. Q.", "A", "Las letras grandes y con contraste se leen desde más lejos."),
        ex("Comparas dos afiches de ejemplo, P (letras de 15 cm, contraste fuerte) y Q (letras de 2 cm, contraste débil), con el criterio «lectura a distancia». ¿Qué conclusión respeta que la comparación es sobre un solo criterio? A. «En lectura a distancia, P cumple mejor porque sus letras de 15 cm contrastan; en otro criterio, Q podría destacar» B. «P es mejor que Q».", "A", "Limita la conclusión al criterio y deja abierta la valoración con otros criterios."),
        ex("Comparas una fotografía de ejemplo y una pieza de cerámica de ejemplo con el criterio «función». ¿Es una comparación adecuada? Responde sí o no.", "No", "La fotografía no tiene una función de uso como la cerámica."),
    ],
    [
        ex("Un compañero concluye: «El afiche X es mejor que el banco de madera». ¿Qué le falta? A. Un criterio común y evidencia B. Más adjetivos.", "A", "Sin criterio común no hay comparación válida."),
        ex("Dos obras de ejemplo cumplen igual el criterio «oficio». ¿Qué conclusión es válida? A. Ambas lo cumplen de forma equivalente, y se pueden distinguir por otro criterio B. Una es mejor porque sí.", "A", "Un empate se rompe con otro criterio, no con una opinión."),
    ],
    [
        ex("Un museo de tu ciudad tiene una obra que no conoces y la quieres comparar con otra. ¿Qué haces primero? A. Leer su ficha técnica o pedir información al docente B. Opinar sin leer.", "A", "Necesitas datos comprobables."),
        ex("Comparas dos chaquetas de ejemplo con el criterio «oficio». La chaqueta K tiene 6 costuras y 4 están parejas; la chaqueta L tiene 6 y 5 están parejas. ¿Cuál cumple mejor? A. La L B. La K.", "A", "L tiene más costuras parejas, que es el rasgo que muestra el oficio."),
    ],
    ex("Quieres elegir una taza para regalar entre dos de ejemplo: M tiene borde parejo y asa firme; N tiene un dibujo más original pero el asa es floja. ¿Qué criterio decide si debe usarse todos los días? A. Función B. Originalidad.", "A", "Un asa floja afecta el uso diario."),
    [
        ex("¿Qué debe ser igual al comparar dos obras?", "El criterio", "Así se mide con la misma vara."),
        ex("Verdadero o falso: dos obras diferentes pueden destacar en criterios distintos.", "Verdadero", "Cada una puede ser fuerte en algo distinto."),
        ex("¿Qué tipo de fuente conviene usar para datos de obras reales?", "Una fuente confiable", "Así los datos son comprobables."),
    ],
    task(
        "Compara DOS obras de ejemplo con el mismo criterio. Opción 1: criterio «lectura a distancia» entre el afiche P (letras de 15 cm, negras sobre amarillo, texto de 4 palabras) y el afiche Q (letras de 3 cm, grises sobre blanco, texto de 25 palabras). Opción 2: criterio «oficio» entre la taza M (borde parejo, asa firme, sin goteos) y la taza N (borde disparejo, asa suelta). Opción 3: criterio «expresividad» entre las fotos X (abrigo colgado en una puerta vacía, luz fría) e Y (abrigo en una percha, luz pareja). Escribe un rasgo de cada una, una conclusión y qué criterio distinto podría cambiar el resultado.",
        "Elegí la opción 2. Rasgo de M: borde parejo y asa firme. Rasgo de N: borde disparejo y asa suelta. Conclusión: con el criterio «oficio», M cumple mejor. Otro criterio: si valoro la originalidad, N podría destacar si su diseño fuera distinto, aunque su oficio sea menor.",
        ["usa un mismo criterio para ambas", "da un rasgo comprobable de cada una", "concluye con razones", "reconoce que otro criterio podría cambiar el resultado"],
        ["comparación con un criterio común", "conclusión argumentada"],
        ["usar criterios distintos", "decir que una es mejor en todo"],
        "Pregunta qué rasgo respalda la conclusión y qué otro criterio podría dar un resultado distinto.",
    ),
    "Compara dos objetos de tu casa con un mismo criterio y anota un rasgo de cada uno.",
    "Escribe tres frases que expliquen por qué compara con justicia quien usa el mismo criterio en ambas obras.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Hojas, lápiz y calculadora si quieres. Las tablas y los puntajes están escritos en la clase.",
    "Aprenderé a seleccionar mis propios criterios estéticos y a ordenarlos por importancia. Sirve para ver cómo cambian mis juicios cuando cambio mis criterios.",
    ["Sé comparar dos obras con un mismo criterio.", "Sé que cada tipo de obra pide criterios distintos."],
    [
        "Una selección personal de criterios es la lista de razones que elijo para valorar y el orden de importancia que les doy. Dos personas pueden elegir criterios distintos y llegar a juicios distintos, y ambas pueden tener razón si explican su elección. Lo que no vale es cambiar de criterio solo para que mi obra preferida gane.",
        "Para probar mi selección uso una tabla con puntajes. Elijo tres criterios, les doy un peso (3 al más importante, 2 al siguiente y 1 al último) y pongo un puntaje de 1 a 5 a cada obra. Multiplico cada puntaje por su peso y sumo. Por ejemplo, con pesos 3, 2 y 1 y puntajes 4, 5 y 2, el total es 4×3 + 5×2 + 2×1 = 24.",
        "Después compruebo si el resultado tiene sentido. Si una obra que considero débil queda primera, reviso si los pesos o los puntajes están mal puestos, o si cambió mi opinión por buenas razones. Una selección personal no es caprichosa: se explica y se puede revisar. Si me afecta un tema de la obra, lo converso con una persona adulta de confianza.",
    ],
    [("peso", "importancia que se da a un criterio, con un número"), ("puntaje", "nota que se da a una obra en un criterio"), ("selección personal", "lista de criterios elegidos con razones"), ("ponderar", "dar más importancia a unos criterios que a otros"), ("revisar", "volver a mirar el juicio para ver si tiene sentido")],
    [
        w("Calcular un total ponderado", "Criterios con pesos: oficio 3, originalidad 2, expresividad 1. Una obra de ejemplo recibe 5 en oficio, 3 en originalidad y 4 en expresividad. ¿Cuál es el total?", ["Oficio: 5 × 3 = 15.", "Originalidad: 3 × 2 = 6. Expresividad: 4 × 1 = 4.", "Suma: 15 + 6 + 4 = 25."], "25 puntos"),
        w("Cambiar los pesos", "Con otros pesos (originalidad 3, expresividad 2, oficio 1), la misma obra suma 3×3 + 4×2 + 5×1. ¿Cuánto da?", ["Originalidad: 3 × 3 = 9.", "Expresividad: 4 × 2 = 8. Oficio: 5 × 1 = 5.", "Suma: 9 + 8 + 5 = 22."], "22 puntos; cambiar los pesos cambia el resultado"),
    ],
    [
        m("Cambiar los pesos después de ver cuál obra gana, solo para que gane la favorita.", "El resultado deja de ser un juicio y pasa a ser un capricho.", "Fija los criterios y los pesos antes de puntuar."),
        m("Creer que un total más alto significa que la obra «vale más» como persona o artista.", "El total solo dice cómo cumple mis criterios.", "Habla de cómo la obra cumple cada criterio."),
    ],
    [
        ex("¿Qué es el peso de un criterio? A. La importancia que se le da B. El tamaño de la obra.", "A", "Pondera unos criterios más que otros."),
        ex("En la selección personal, ¿qué criterio recibe el peso mayor? A. El que consideras más importante B. El último de la lista.", "A", "El peso más alto va al criterio más importante para ti."),
        ex("¿Se pueden elegir criterios distintos a los de otra persona? A. Sí, si se explican las razones B. No, nunca.", "A", "La selección personal se argumenta."),
    ],
    [
        arith("Pesos: oficio 3, originalidad 2, expresividad 1. Una obra de ejemplo recibe 4 en oficio, 4 en originalidad y 3 en expresividad. ¿Cuál es el total?", "4 * 3 + 4 * 2 + 3 * 1", "Se multiplica cada puntaje por su peso y se suman.", " puntos"),
        ex("Una persona fija estos pesos: originalidad 3, oficio 2 y función 1. ¿Qué valora más? A. La originalidad B. La función.", "A", "El peso mayor se da al criterio más importante para quien juzga."),
        ex("Cambias los pesos justo después de ver que tu obra favorita perdió. ¿Es un juicio sólido? A. No, porque los pesos se fijan antes B. Sí, siempre.", "A", "Cambiarlos después solo busca favorecer a una obra."),
    ],
    [
        arith("Pesos: expresividad 3, composición 2, oficio 1. Una obra de ejemplo recibe 5, 2 y 4. ¿Cuál es el total?", "5 * 3 + 2 * 2 + 4 * 1", "Cada puntaje se multiplica por el peso de su criterio.", " puntos"),
        ex("Dos personas puntúan las mismas obras y llegan a ganadoras distintas porque usan pesos distintos. ¿Qué muestra eso? A. Que los pesos expresan lo que cada persona valora, y por eso hay que explicarlos B. Que una de las dos puntuó mal.", "A", "Los pesos reflejan una selección personal; lo importante es que cada una la justifique."),
        ex("Tabla con pesos oficio 3, expresividad 2, originalidad 1. Obra A: 5, 2, 2. Obra B: 3, 5, 3. A suma 21 y B suma 22. Si solo te importara el oficio, ¿cuál elegirías? A. A B. B.", "A", "A tiene 5 en oficio y B solo 3."),
    ],
    [
        ex("Una amiga puntúa dos obras con el criterio «originalidad» pero luego dice: «gana la mía porque es mía». ¿Qué falla? A. Cambia la razón de su juicio B. Nada.", "A", "Ya no usa el criterio que dijo."),
        ex("Con pesos 3, 2 y 1, una obra de ejemplo tiene puntajes 5, 5 y 5. ¿Cuál es su total? A. 30 B. 15.", "A", "5 × 3 + 5 × 2 + 5 × 1 = 30."),
    ],
    [
        ex("Tabla con pesos función 3, oficio 2, originalidad 1. Obra M: puntajes 5, 4, 1. Obra N: 3, 4, 5. M suma 24 y N suma 22. Si cambias los pesos a originalidad 3, oficio 2, función 1, ¿quién gana? A. N B. M.", "A", "N suma 5×3 + 4×2 + 3×1 = 26; M suma 1×3 + 4×2 + 5×1 = 16."),
        ex("Dos amigos puntúan la misma obra con los mismos pesos y obtienen 20 y 14. ¿Qué es lo más razonable? A. Comparar sus puntajes criterio por criterio y sus razones B. Promediar y no conversar.", "A", "Así se descubre en qué criterio difieren y por qué."),
    ],
    ex("Debes elegir entre dos mochilas de ejemplo para la clase de arte. M: cierre fuerte, color común. N: dibujo original, cierre que falla. Para uso diario, ¿qué criterio pondrías primero? A. Función B. Originalidad.", "A", "Un cierre que falla impide el uso diario."),
    [
        ex("¿Cuándo se fijan los pesos de los criterios?", "Antes de puntuar las obras", "Así no se favorece a una obra."),
        ex("Verdadero o falso: dos personas con criterios distintos pueden argumentar bien.", "Verdadero", "Importa que expliquen sus razones."),
        ex("¿Qué debe acompañar a una selección personal de criterios para ser válida?", "Razones que la expliquen", "Dos personas pueden elegir distinto si ambas argumentan su elección."),
    ],
    task(
        "Arma tu selección personal con tres criterios. Elige UNA obra de ejemplo para puntuar de 1 a 5: A) Afiche «Cuida el agua» (letras blancas gruesas sobre azul, gota central, texto de 3 palabras); B) Taza «Mañana» (cerámica blanca, asa firme, dibujo de sol simple); C) Fotografía «Banco» (un banco solo en un patio vacío, luz de amanecer). Escribe tus tres criterios, sus pesos (3, 2 y 1), el puntaje de la obra en cada uno con una razón, y calcula el total.",
        "Elegí la taza. Criterios y pesos: función 3, oficio 2, originalidad 1. Puntajes: función 5 (asa firme); oficio 4 (borde parejo); originalidad 2 (dibujo simple). Total: 5×3 + 4×2 + 2×1 = 15 + 8 + 2 = 25.",
        ["elige tres criterios adecuados al tipo de obra", "fija los pesos antes de puntuar", "da una razón por puntaje", "calcula bien el total"],
        ["tabla con criterios, pesos y puntajes", "cálculo del total"],
        ["cambiar los pesos al final", "no dar razones del puntaje"],
        "Pregunta por qué ese criterio tiene el mayor peso y si el cálculo está bien hecho.",
    ),
    "Elige tres criterios para valorar una mochila y ordénalos del 3 al 1 según su importancia para ti.",
    "Escribe dos frases que expliquen por qué se fijan los pesos antes de puntuar.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Hojas y lápiz. El texto breve de la obra de ejemplo está escrito en la clase.",
    "Aprenderé a escribir un juicio crítico argumentado con afirmación, evidencia, criterio y conclusión. Sirve para defender mi valoración con razones claras.",
    ["Sé elegir y ponderar criterios.", "Sé separar descripción, interpretación y juicio."],
    [
        "Un juicio crítico argumentado tiene cuatro partes. La afirmación es lo que sostengo («esta obra es pertinente a su lugar»). La evidencia es el rasgo que se ve que la respalda. El criterio es la razón con que miro ese rasgo. La conclusión cierra la idea y dice qué se deduce. Las cuatro juntas forman un párrafo breve que otra persona puede revisar.",
        "Para que sea claro uso conectores: «porque», «por eso», «en cambio», «sin embargo». Ejemplo: «El mural es pertinente a su lugar porque sus letras amarillas grandes se leen desde la calle (evidencia). El criterio es la lectura a distancia. Por eso, cumple su propósito de informar a quienes pasan (conclusión)». Evito palabras vagas como «lindo» o «raro».",
        "También puedo mostrar que mi juicio tiene límites. Si el mural está bien en lectura pero repite fórmulas conocidas, lo digo: «Sin embargo, su originalidad es menor». Reconocer un punto débil hace más creíble mi argumento. Hablo de la obra y no de las personas, y no uso burlas.",
    ],
    [("afirmación", "idea que sostengo sobre la obra"), ("evidencia", "rasgo visible que respalda la afirmación"), ("conector", "palabra que une ideas, como porque o sin embargo"), ("conclusión", "cierre que dice qué se deduce"), ("argumento", "conjunto de afirmación, evidencia, criterio y conclusión")],
    [
        w("Ordenar un argumento", "Fragmentos: (1) «Por eso cumple su propósito de informar». (2) «Las letras amarillas grandes se leen desde la calle». (3) «El mural es pertinente a su lugar». (4) «El criterio es la lectura a distancia». ¿Cuál es el orden de afirmación, evidencia, criterio y conclusión?", ["Afirmación: el (3).", "Evidencia: el (2). Criterio: el (4).", "Conclusión: el (1). Orden: 3, 2, 4, 1."], "3, 2, 4, 1"),
        w("Corregir una frase vaga", "Frase: «La cerámica es linda». Reescríbela como argumento usando este dato de ejemplo: borde parejo y esmalte sin burbujas.", ["Afirmación: la cerámica tiene buen oficio.", "Evidencia: borde parejo y esmalte sin burbujas.", "Conclusión: está bien terminada."], "La cerámica tiene buen oficio porque su borde es parejo y su esmalte no tiene burbujas"),
    ],
    [
        m("Escribir solo la afirmación: «es un mural muy bueno».", "Sin evidencia ni criterio no hay argumento.", "Agrega un rasgo visible, el criterio y una conclusión."),
        m("Usar burlas contra la obra o contra quien la hizo.", "Una crítica argumentada se centra en la obra.", "Describe rasgos y propone una mejora."),
    ],
    [
        ex("¿Qué parte del argumento es el rasgo visible que lo respalda? A. La evidencia B. La conclusión.", "A", "La evidencia se puede comprobar en la obra."),
        ex("¿Qué conector sirve para dar una razón? A. Porque B. Sin embargo.", "A", "«Porque» introduce la razón."),
        ex("¿Qué palabra es vaga y conviene evitar? A. «Lindo» B. «Contraste».", "A", "«Lindo» no dice qué rasgo se mira."),
    ],
    [
        ex("En «El afiche destaca porque sus letras negras contrastan con el fondo amarillo», ¿cuál es la evidencia? A. Las letras negras contrastan con el fondo amarillo B. El afiche destaca.", "A", "Es el rasgo que se ve."),
        ex("¿Qué conector sirve para mostrar un límite o una excepción? A. Sin embargo B. Por eso.", "A", "«Sin embargo» introduce un contraste."),
        ex("Una frase dice: «Es lo peor que he visto». ¿Se centra en la obra? A. No, es una burla sin rasgos B. Sí, describe la técnica.", "A", "No menciona rasgos ni criterio."),
    ],
    [
        ex("Obra de ejemplo: una fotografía de un patio vacío, con un banco al centro y luz tenue. Elige el argumento mejor armado. A. «Es expresiva porque el patio vacío y el banco solo podrían sugerir soledad; por eso comunica emoción» B. «Es expresiva porque sí».", "A", "Tiene evidencia, criterio y conclusión."),
        ex("Quieres agregar un límite a tu argumento sobre un mural de letras claras. ¿Qué frase sirve? A. «Sin embargo, repite una fórmula conocida y su originalidad es menor» B. «Además, es bonito».", "A", "Reconoce un punto débil con evidencia."),
        ex("Una persona escribe: «La taza tiene buen oficio, por eso la valoro». ¿Qué le falta? A. La evidencia visible B. Un adjetivo más.", "A", "No dice qué rasgo muestra el oficio."),
    ],
    [
        ex("Texto de ejemplo: «El afiche es pertinente porque su texto corto se lee en el paradero. Sin embargo, las letras claras sobre fondo blanco se leen mal. Por eso, mejora si usa letras oscuras». ¿Cuál frase introduce el límite? A. «Sin embargo, las letras claras sobre fondo blanco se leen mal» B. «Por eso, mejora si usa letras oscuras».", "A", "«Sin embargo» marca el punto débil; «por eso» introduce la conclusión."),
        ex("Dos argumentos sobre el mismo mural: X dice «es genial»; Y dice «las letras amarillas se leen desde la calle, por eso cumple su propósito». ¿Cuál es más sólido? A. Y B. X.", "A", "Tiene evidencia, criterio y conclusión."),
    ],
    [
        ex("Una amiga muestra un dibujo suyo y pregunta si es bueno. ¿Qué respuesta ayuda más? A. «Los colores cálidos del fondo hacen resaltar la figura; en cambio, las líneas del borde están poco claras» B. «Está bien, supongo».", "A", "Da evidencia y un punto a mejorar."),
        ex("Un párrafo dice: «El afiche tiene buena composición. Por eso es el mejor». ¿Qué falta entre ambas frases? A. La evidencia visible y el criterio B. Un título más largo.", "A", "Sin rasgo ni criterio la conclusión no se deduce."),
    ],
    ex("Quieres comentar el cartel de una actividad escolar. ¿Qué haces primero? A. Elegir un criterio y mirar un rasgo B. Decir qué piensas de quien lo hizo.", "A", "El juicio se centra en la obra."),
    [
        ex("Nombra las cuatro partes de un argumento.", "Afirmación, evidencia, criterio y conclusión", "Son las cuatro partes de un juicio argumentado."),
        ex("Verdadero o falso: reconocer un punto débil debilita el argumento.", "Falso", "Lo hace más creíble."),
        ex("En Artes: ¿Qué conector introduce una razón?", "Porque", "Une la afirmación con la evidencia."),
    ],
    task(
        "Escribe un párrafo argumentado de entre 4 y 6 líneas sobre UNA obra de ejemplo. A) Afiche «Cuida el agua»: letras blancas gruesas sobre azul, gota central, texto de 3 palabras, pegado en un baño. B) Taza «Mañana»: cerámica blanca, asa firme, dibujo de sol, borde parejo. C) Fotografía «Banco»: banco solo en un patio vacío, luz de amanecer. Incluye afirmación, evidencia, criterio, un límite con «sin embargo» y conclusión.",
        "Elegí A. El afiche es pertinente a su lugar porque sus letras blancas grandes se leen sobre el fondo azul desde el lavamanos (evidencia). El criterio es la lectura a distancia. Sin embargo, la gota no aporta algo nuevo, así que su originalidad es menor. Por eso cumple su propósito de recordar cerrar la llave, aunque podría innovar más.",
        ["tiene afirmación, evidencia, criterio y conclusión", "incluye un límite con «sin embargo»", "usa conectores", "habla de la obra y no de las personas"],
        ["párrafo argumentado", "límite reconocido"],
        ["solo opinar", "burlarse de la obra"],
        "Pregunta qué frase es la evidencia y cuál es el límite del argumento.",
    ),
    "Escribe una frase con «porque» sobre un objeto de tu casa y señala cuál es la evidencia.",
    "Reescribe en tres frases la afirmación «ese afiche es bonito» con evidencia, criterio y conclusión.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA4, 5,
    "Hojas y lápiz. Los argumentos de ejemplo están escritos en la clase.",
    "Aprenderé a contrastar mi juicio con criterios de claridad y evidencia, a reconocer falacias frecuentes y a revisarlo o mantenerlo con razones. Sirve para que mis juicios resistan preguntas.",
    ["Sé escribir un argumento con afirmación, evidencia, criterio y conclusión.", "Sé poner pesos a mis criterios."],
    [
        "Contrastar un juicio es revisarlo con preguntas: ¿hay evidencia visible?, ¿el criterio corresponde al tipo de obra?, ¿la conclusión se deduce de lo anterior?, ¿reconoce algún límite? Si una respuesta es «no», mejoro el juicio. Una buena revisión no busca tener razón siempre, sino que el juicio esté bien apoyado.",
        "Algunas falacias, es decir, razones que parecen buenas pero no lo son, aparecen mucho. «Es famosa, entonces es buena» apela a la fama. «A todos les gusta» apela a la cantidad. «Es cara» apela al precio. «Mi amigo la hizo» apela a la amistad. Ninguna habla de rasgos de la obra. Las reemplazo por evidencia visible y un criterio.",
        "También puedo cambiar de opinión, y es una buena señal si tengo razones. Si alguien me muestra un rasgo que yo no había visto, puedo corregir mi juicio y decirlo: «Antes pensaba que… ahora veo que…». Si mi juicio resiste las preguntas, lo mantengo. El respeto es clave: valoro la obra, no ridiculizo a quien la hizo.",
    ],
    [("falacia", "razón que parece buena pero no habla de la obra"), ("contrargumento", "razón que apunta en sentido contrario"), ("revisar", "volver sobre el juicio para mejorarlo"), ("sólido", "bien apoyado en evidencia y criterio"), ("respeto", "valorar la obra sin ridiculizar a las personas")],
    [
        w("Detectar una falacia", "Frase: «El mural es el mejor porque lo pintó alguien muy conocido». ¿Qué falacia es y cómo la reemplazas?", ["Apela a que el autor es conocido, no a rasgos del mural.", "Reemplazo: elijo un criterio y un rasgo visible.", "Nueva frase: «Es pertinente porque sus letras grandes se leen desde la calle»."], "Apela a la fama; se reemplaza por evidencia y criterio"),
        w("Revisar un juicio", "Juicio: «El afiche tiene buena composición». Un compañero muestra que el texto está cortado en el borde. ¿Qué haces?", ["Verifico el rasgo: el texto sí está cortado.", "Corrijo el juicio: la composición tiene un problema en el borde.", "Lo digo con razones y propongo mover el texto."], "Corregir el juicio con la nueva evidencia"),
    ],
    [
        m("Defender un juicio solo para no dar la razón al otro.", "Importa que el juicio esté bien apoyado, no ganar.", "Revisa la evidencia y cambia o mantén el juicio con razones."),
        m("Usar «a todos les gusta» como prueba de calidad.", "Es una falacia: no habla de rasgos de la obra.", "Cita un rasgo visible y un criterio."),
    ],
    [
        ex("«Es famosa, entonces es buena», ¿qué tipo de razón es? A. Una falacia B. Una evidencia visible.", "A", "No habla de rasgos de la obra."),
        ex("¿Qué se revisa en un juicio? A. Evidencia, criterio y conclusión B. Solo la ortografía.", "A", "Esas son sus partes."),
        ex("Si te muestran un rasgo que no habías visto y cambia tu juicio, ¿qué haces? A. Corrigo el juicio con razones B. Lo mantengo aunque sea falso.", "A", "Cambiar con razones es buena señal."),
    ],
    [
        ex("«A todos les gusta» apela a… A. La cantidad de gente B. Un rasgo visible.", "A", "No explica qué hace buena a la obra."),
        ex("Un juicio dice «el mural es pertinente porque lo vio mucha gente». ¿Es sólido? A. No, usa la cantidad de público B. Sí, es un criterio.", "A", "La cantidad de gente no es un rasgo ni un criterio."),
        ex("¿Qué pregunta ayuda a revisar la conclusión? A. ¿Se deduce de la evidencia y del criterio? B. ¿Quién la leyó primero?", "A", "La conclusión debe salir de lo anterior."),
    ],
    [
        ex("Juicio: «La taza es mejor porque cuesta más». ¿Qué falacia es? A. Apela al precio B. Apela a la amistad.", "A", "El precio no describe rasgos de la obra."),
        ex("Juicio revisado: «Antes pensaba que el afiche se leía bien; ahora veo que las letras claras sobre blanco no se leen de lejos». ¿Qué hizo la persona? A. Corrigió su juicio con evidencia B. Cambió de opinión sin razones.", "A", "Dio un rasgo visible como razón."),
        ex("Fotografía de ejemplo: la persona que juzga dice que su prima la tomó, por eso la defiende. ¿Qué debería hacer? A. Buscar rasgos y criterios B. Seguir defendiéndola por cariño.", "A", "El cariño no es evidencia de calidad."),
    ],
    [
        ex("Dos argumentos sobre el mismo afiche. P: «es perfecto porque lo hicieron mis amigos». Q: «sus letras negras grandes se leen en el paradero, por eso es pertinente». ¿Cuál resiste mejor una pregunta crítica? A. Q B. P.", "A", "Tiene evidencia y criterio."),
        ex("Un compañero te pregunta: «¿qué rasgo prueba eso?». ¿Qué tipo de pregunta hace? A. Pide evidencia B. Ridiculiza.", "A", "Es una pregunta para revisar el juicio."),
    ],
    [
        ex("Un amigo tiene un criterio distinto al tuyo sobre un mural y respeta las razones del otro. ¿Qué actitud tiene? A. Respeta que valoren con razones distintas B. Se burla de tu opinión.", "A", "El respeto permite debatir con razones."),
        ex("Un compañero dice: «Mi juicio es sólido porque lo pensé mucho». ¿Qué le falta? A. Evidencia visible y un criterio B. Más tiempo de reflexión.", "A", "Un juicio sólido se apoya en evidencia y criterio."),
    ],
    ex("Tu juicio sobre un trabajo escolar dice «es horrible». ¿Cómo lo reescribes? A. «Las líneas del borde son poco claras; mejoraría con trazos más firmes» B. «Es feo, rehazlo».", "A", "Da evidencia y propone una mejora."),
    [
        ex("Menciona dos falacias de la clase.", "Apelar a la fama y apelar a la cantidad", "También el precio y la amistad."),
        ex("Verdadero o falso: cambiar de opinión con razones es una buena señal.", "Verdadero", "Muestra que se revisa el juicio con evidencia."),
        ex("¿Qué se debe valorar: la obra o a quien la hizo?", "La obra", "El juicio se centra en rasgos de la obra."),
    ],
    task(
        "Revisa UN juicio de ejemplo y contrástalo con criterios. A) «El afiche es el mejor porque a todos les gusta». B) «La taza es excelente porque costó mucho». C) «La foto es buena porque la tomó mi amigo». Escribe qué falacia contiene, qué pregunta de revisión le harías, y reescríbelo con afirmación, evidencia, criterio y conclusión usando datos de ejemplo que inventes y rotules como «de ejemplo».",
        "Revisé A. Falacia: apela a la cantidad. Pregunta: ¿qué rasgo del afiche lo hace bueno? Reescritura: «El afiche es pertinente porque sus letras negras grandes se leen desde el paradero (dato de ejemplo). El criterio es la lectura a distancia. Por eso cumple su propósito».",
        ["identifica la falacia", "formula una pregunta de revisión", "reescribe con las cuatro partes", "rotula los datos inventados como «de ejemplo»"],
        ["juicio original y reescrito", "pregunta de revisión"],
        ["mantener la falacia", "burlarse del autor"],
        "Pregunta qué rasgo respalda la nueva versión y si la conclusión se deduce de él.",
    ),
    "Escucha o lee un comentario sobre algo que viste y detecta si usa fama, precio, cantidad o amistad como razón.",
    "Escribe tres frases para explicar por qué cambiar de opinión con razones fortalece tu argumento.",
)

# =============================================================== OA 05
# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Hojas y lápiz. Las fichas de proyectos de ejemplo están escritas en la clase.",
    "Aprenderé a elegir criterios de análisis según el tipo de trabajo o proyecto visual que evalúo, y a distinguir evaluar el proceso de evaluar el producto. Sirve para evaluar mi trabajo y el de mis pares con fundamento.",
    ["Sé argumentar un juicio con evidencia y criterio.", "Sé que un tipo de obra pide criterios distintos."],
    [
        "Evaluar es juzgar un trabajo con criterios claros y evidencia. Lo hago sobre mi propio trabajo (autoevaluación) y sobre el de mis pares (coevaluación). El criterio depende del tipo de proyecto. En un proyecto de escultura miro estabilidad, materiales y relación con el desafío; en un video, planos, ritmo, sonido y permisos; en un afiche, la lectura a distancia y el mensaje; en un mural, el lugar y la escala.",
        "Se puede evaluar el producto (lo que quedó terminado) y el proceso (cómo se llegó a él). El proceso se ve en los bocetos, las pruebas, los cambios y las decisiones anotadas. Un producto muy limpio con un proceso sin registros se evalúa distinto de uno con muchos cambios bien explicados. Ambos se miran con criterios, pero no son lo mismo.",
        "Antes de evaluar escribo la pregunta que quiero responder: «¿este proyecto cumple su propósito?». Luego elijo tres o cuatro criterios que correspondan al tipo de trabajo y busco evidencia para cada uno. Evalúo la obra y no a la persona. Los proyectos de esta clase son de ejemplo: no describen trabajos reales de nadie.",
    ],
    [("autoevaluación", "evaluación del propio trabajo"), ("coevaluación", "evaluación del trabajo de un par"), ("producto", "trabajo terminado"), ("proceso", "pasos y decisiones para llegar al producto"), ("tipo de proyecto", "clase de trabajo, como escultura, video, afiche o mural")],
    [
        w("Elegir criterios por proyecto", "Proyecto de ejemplo: video de 30 s sobre el reciclaje, que se verá en el teléfono. ¿Qué cuatro criterios eliges?", ["Es un video: planos, ritmo, sonido.", "Se verá en el teléfono: imágenes simples y texto grande.", "Elijo: planos, ritmo, sonido y lectura en pantalla pequeña."], "Planos, ritmo, sonido y lectura en pantalla pequeña"),
        w("Producto o proceso", "Un grupo presenta un afiche terminado, pero no guardó bocetos ni pruebas. ¿Qué puede evaluarse y qué no?", ["Producto: sí, está terminado.", "Proceso: no hay bocetos ni pruebas, no hay evidencia.", "Se evalúa el producto y se anota la falta de registro."], "Se evalúa el producto; el proceso no tiene evidencia"),
    ],
    [
        m("Usar los mismos criterios para un video y para una escultura.", "Cada tipo de proyecto tiene cualidades propias.", "Elige criterios según el tipo de proyecto."),
        m("Evaluar solo el producto y olvidar el proceso.", "El proceso muestra decisiones y aprendizaje.", "Pide bocetos, pruebas y cambios como evidencia."),
    ],
    [
        ex("¿Qué es la autoevaluación? A. Evaluar el propio trabajo B. Evaluar el trabajo de un compañero.", "A", "El prefijo auto indica uno mismo."),
        ex("¿Qué es el proceso de un proyecto? A. Los pasos y decisiones para llegar al producto B. Solo el trabajo terminado.", "A", "Incluye bocetos, pruebas y cambios."),
        ex("¿Cuál criterio sirve para evaluar un video? A. El ritmo B. La función de una taza.", "A", "El ritmo es propio de los videos."),
    ],
    [
        ex("Evalúas una escultura de ejemplo de cartón. ¿Qué criterio es adecuado? A. Estabilidad B. Ritmo de cortes.", "A", "La estabilidad es propia de una obra con volumen."),
        ex("Evalúas un afiche de ejemplo para un paradero. ¿Qué criterio es adecuado? A. Lectura a distancia B. Duración de los planos.", "A", "El afiche se lee de paso."),
        ex("La coevaluación es… A. La evaluación del trabajo de un par B. La evaluación de un proyecto de otro curso.", "A", "El prefijo co indica que se hace con otras personas."),
    ],
    [
        ex("Un mural de ejemplo se pintó en un muro de una cancha. ¿Qué criterio es propio de los murales? A. El lugar y la escala B. La duración en segundos.", "A", "Un mural se ve en un espacio, con cierta escala."),
        ex("¿Qué grupo de criterios corresponde a evaluar un video? A. Planos, ritmo, sonido y permisos B. Estabilidad, base, materiales y relación con el desafío.", "A", "El segundo grupo es propio de una escultura."),
        ex("Un grupo muestra un video terminado y un cuaderno con tres versiones del guion y notas de cambios. ¿Qué evidencia de proceso hay? A. El cuaderno con versiones y notas B. Solo el video.", "A", "El cuaderno documenta decisiones."),
    ],
    [
        ex("Un compañero evalúa su video con el criterio «estabilidad». ¿Es un criterio adecuado? A. No, es más propio de objetos con volumen B. Sí, siempre.", "A", "Para un video conviene ritmo, plano o sonido."),
        ex("¿Por qué evaluar también el proceso? A. Porque muestra decisiones y aprendizaje B. Porque es más fácil.", "A", "El proceso explica cómo se llegó al producto."),
    ],
    [
        ex("Vas a evaluar el afiche de tu compañera para el kiosco del liceo. ¿Qué haces primero? A. Elegir criterios adecuados a un afiche B. Decir si te cae bien.", "A", "Los criterios deben corresponder al tipo de trabajo."),
        ex("Un proyecto de ejemplo tiene un producto muy limpio, pero su cuaderno de proceso está vacío. ¿Qué anotas al evaluar? A. Que el producto tiene evidencia y el proceso no B. Que el proyecto no se puede evaluar.", "A", "Sin bocetos ni pruebas no hay evidencia de proceso."),
    ],
    ex("Quieres evaluar un trabajo en equipo donde cada persona hizo una parte. ¿Qué pides? A. Evidencia de la parte de cada persona B. Solo el producto final.", "A", "Así se reconoce la autoría de cada parte."),
    [
        ex("¿Cuál de estos criterios es propio de un video y no de una escultura? A. Ritmo B. Estabilidad C. Peso de la base.", "A", "El ritmo depende de los planos y los cortes; los otros dos son de obras con volumen."),
        ex("Verdadero o falso: se evalúa a la obra y no a la persona.", "Verdadero", "El juicio se centra en rasgos del trabajo."),
        ex("¿Qué se mira en el proceso?", "Bocetos, pruebas y cambios", "Son la evidencia de cómo se llegó al producto."),
    ],
    task(
        "Elige UN proyecto de ejemplo y decide cómo evaluarlo. A) Escultura de cartón de 45 cm que sirve de banca, con maqueta y pruebas. B) Video de 40 s con guion gráfico y permisos. C) Afiche de una campaña escolar con tres bocetos. Escribe el propósito del proyecto, cuatro criterios adecuados, qué evidencia de proceso buscarías y qué evidencia del producto buscarías.",
        "Elegí B. Propósito: mostrar el reciclaje en la casa. Criterios: planos, ritmo, sonido y cuidado ético. Proceso: guion gráfico, pruebas de 10 s y cambios. Producto: el video final de 40 s. Evidencia ética: notas de permiso.",
        ["define un propósito", "elige cuatro criterios adecuados al tipo de proyecto", "distingue proceso y producto", "nombra evidencias concretas"],
        ["criterios elegidos", "evidencias de proceso y producto"],
        ["usar criterios que no corresponden", "olvidar el proceso"],
        "Pregunta por qué cada criterio corresponde al tipo de proyecto y cuál sería la evidencia.",
    ),
    "Elige un trabajo que hayas hecho y anota tres criterios para evaluarlo según su tipo.",
    "Explica en tres frases la diferencia entre evaluar el proceso y evaluar el producto.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Hojas, regla y lápiz. La rúbrica de ejemplo está escrita en la clase.",
    "Aprenderé a leer y armar una rúbrica con niveles de logro y descriptores observables. Sirve para evaluar con fundamento y comunicar por qué un trabajo está en un nivel.",
    ["Sé elegir criterios según el tipo de proyecto.", "Sé distinguir proceso y producto."],
    [
        "Una rúbrica es una tabla con criterios en filas y niveles de logro en columnas. Los niveles de logro pueden ser: insuficiente (1), básico (2), logrado (3) y destacado (4). Cada celda tiene un descriptor, que es una frase observable. Por ejemplo, en «lectura a distancia»: 1 = no se lee desde 3 m; 2 = se lee con esfuerzo; 3 = se lee con claridad; 4 = se lee con claridad desde más de 8 m.",
        "Un buen descriptor se puede comprobar con un hecho o una medida, no con una impresión. «Se ve bonito» no sirve; «las letras miden más de 10 cm y contrastan con el fondo» sí. Evito los términos vagos como «bien», «mal» o «poco». Cuando uso una rúbrica pongo un nivel por criterio y escribo la evidencia que lo respalda.",
        "Si varios criterios son más importantes que otros, puedo darles pesos. Por ejemplo, el cuidado ético podría pesar el doble. Calculo el total multiplicando cada nivel por su peso. La rúbrica debe conocerse antes de hacer el trabajo, para que todos sepan qué se espera. Si un descriptor no se puede comprobar, lo reescribo.",
    ],
    [("rúbrica", "tabla de criterios con niveles de logro"), ("nivel de logro", "grado que alcanza un trabajo en un criterio"), ("descriptor", "frase observable que define un nivel"), ("observable", "que se puede comprobar con un hecho o una medida"), ("peso", "importancia que se da a un criterio con un número")],
    [
        w("Leer una rúbrica", "Criterio «lectura a distancia», niveles de ejemplo: 1 no se lee desde 3 m; 2 se lee con esfuerzo desde 3 m; 3 se lee con claridad desde 3 m; 4 se lee con claridad desde 8 m. Un afiche de ejemplo se lee bien desde 4 m, pero con esfuerzo desde 8 m. ¿Qué nivel le asignas?", ["Se lee con claridad desde 3 m y desde 4 m.", "Desde 8 m solo con esfuerzo, no con claridad.", "Nivel 3."], "Nivel 3"),
        w("Mejorar un descriptor", "Descriptor: «el video se ve bien». Reescríbelo con un dato observable sobre el ritmo.", ["Elijo un hecho medible: duración de los planos.", "Redacto: «ningún plano dura más de 8 s».", "Ahora se puede comprobar con un reloj."], "Ningún plano dura más de 8 s"),
    ],
    [
        m("Escribir descriptores vagos como «está bien hecho».", "No se pueden comprobar y cada persona los entiende distinto.", "Usa un hecho o una medida que cualquiera pueda verificar."),
        m("Mostrar la rúbrica solo después de que el trabajo está hecho.", "Nadie sabe qué se espera.", "Entrégala antes de comenzar."),
    ],
    [
        ex("¿Qué es una rúbrica? A. Una tabla de criterios con niveles de logro B. Un tipo de pintura.", "A", "Organiza qué se evalúa y cómo."),
        ex("¿Qué es un descriptor observable? A. Una frase que se puede comprobar B. Una opinión personal.", "A", "Se verifica con hechos o medidas."),
        ex("En una rúbrica de cuatro niveles, ¿cuál es el nivel más alto? A. Destacado B. Insuficiente.", "A", "Es el nivel 4 de logro."),
    ],
    [
        ex("¿Cuál descriptor es observable? A. «Las letras miden más de 10 cm» B. «Se ve lindo».", "A", "Se puede medir con una regla."),
        ex("¿Cuándo debe conocerse la rúbrica? A. Antes de hacer el trabajo B. Después de evaluarlo.", "A", "Así se sabe qué se espera."),
        ex("Un descriptor dice «el texto tiene menos de 8 palabras». ¿Es comprobable? A. Sí, contando palabras B. No.", "A", "Se verifica contando."),
    ],
    [
        ex("Una rúbrica tiene criterios en filas y niveles en columnas. Para sumar el criterio «sonido», ¿qué agregas? A. Una fila nueva B. Una columna nueva.", "A", "Cada criterio ocupa una fila; las columnas son los niveles de logro."),
        arith("Rúbrica con pesos: cuidado ético vale el doble. Niveles de un proyecto de ejemplo: ética 3 (peso 2), ritmo 2 (peso 1), sonido 4 (peso 1). ¿Cuál es el total?", "3 * 2 + 2 * 1 + 4 * 1", "Cada nivel se multiplica por su peso.", " puntos"),
        ex("Con la rúbrica de la clase (nivel 2: se lee con esfuerzo desde 3 m; nivel 3: se lee con claridad desde 3 m), un afiche de ejemplo solo se lee con esfuerzo desde 3 m. ¿Qué nivel tiene? A. Nivel 2 B. Nivel 3.", "A", "Cumple el descriptor del nivel 2, no el del 3."),
    ],
    [
        ex("Un descriptor de nivel 4 dice «muy buen ritmo». ¿Qué problema tiene? A. Es vago y no se puede comprobar B. Es demasiado largo.", "A", "No dice cómo se comprueba."),
        ex("Reescribe: «El mural se ve bien desde lejos». ¿Qué versión es mejor? A. «Las letras se leen desde 10 m» B. «Se ve muy bonito de lejos».", "A", "Tiene una medida."),
    ],
    [
        ex("Tu equipo recibe una rúbrica a media tarea. ¿Qué haces? A. Revisar lo hecho contra los descriptores y ajustar B. Ignorarla.", "A", "La rúbrica orienta mejoras aun en el proceso."),
        ex("En una rúbrica la ética vale el doble. Un proyecto de ejemplo tiene ética 1 (peso 2), ritmo 4 (peso 1) y sonido 4 (peso 1). ¿Qué corriges primero? A. La ética B. El ritmo.", "A", "Es el criterio más bajo y el de mayor peso."),
    ],
    ex("Evalúas un trabajo y no sabes qué nivel poner porque el descriptor es vago. ¿Qué haces? A. Pides reescribirlo con un dato observable B. Pones un nivel al azar.", "A", "Un descriptor claro permite evaluar con fundamento."),
    [
        ex("¿Qué dos partes tiene una rúbrica?", "Criterios y niveles de logro", "Son las filas y las columnas."),
        ex("Verdadero o falso: «se ve bien» es un descriptor observable.", "Falso", "No se puede comprobar con un dato."),
        ex("¿Qué se escribe junto al nivel elegido?", "La evidencia", "Respalda por qué se puso ese nivel."),
    ],
    task(
        "Arma una mini rúbrica para UN proyecto de ejemplo. A) Escultura de cartón: criterio estabilidad. B) Video de 30 s: criterio ritmo. C) Afiche: criterio lectura a distancia. Escribe cuatro niveles (insuficiente, básico, logrado y destacado) con un descriptor observable para cada uno (con una medida o un hecho). Luego evalúa un trabajo de ejemplo que inventes y rotules como «de ejemplo», con el nivel y la evidencia.",
        "Elegí B, ritmo del video. 1: la mayoría de los planos dura más de 15 s. 2: la mayoría dura entre 10 y 15 s. 3: la mayoría dura entre 5 y 10 s. 4: la mayoría dura entre 3 y 6 s con cortes que acompañan el sonido. Trabajo de ejemplo: planos de 6, 7, 5 y 8 s. Nivel 3, porque la mayoría está entre 5 y 10 s.",
        ["cada nivel tiene un descriptor observable", "evita palabras vagas", "elige un nivel con evidencia", "rotula los datos como «de ejemplo»"],
        ["rúbrica de cuatro niveles", "evaluación con evidencia"],
        ["descriptores vagos", "nivel sin evidencia"],
        "Pregunta si el descriptor se puede comprobar con un reloj o una regla y qué dato respalda el nivel.",
    ),
    "Reescribe la frase «el trabajo está bien» con un dato que se pueda contar o medir.",
    "Escribe tres descriptores observables para el criterio «lectura a distancia» de un afiche.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Hojas y lápiz. Los trabajos de ejemplo y las frases a mejorar están escritos en la clase.",
    "Aprenderé a dar retroalimentación respetuosa y fundamentada a un par con la estructura «veo, valoro, sugiero». Sirve para ayudar a mejorar un trabajo sin ofender.",
    ["Sé armar un descriptor observable.", "Sé evaluar con una rúbrica y evidencia."],
    [
        "La retroalimentación es un comentario que ayuda a mejorar un trabajo. Una estructura útil tiene tres pasos: «veo» (un rasgo observable), «valoro» (qué logra ese rasgo según un criterio) y «sugiero» (un cambio posible, dicho como propuesta). Ejemplo: «Veo que las letras son de 3 cm; el criterio es la lectura a distancia, y desde 5 m no se leen. Sugiero probar letras de 10 cm».",
        "También puedo agregar una pregunta: «¿qué querías provocar con el color rojo?». La pregunta invita a explicar la decisión y no la juzga. Evito los comentarios generales («está mal», «es feo»), las comparaciones con otras personas y las burlas. Hablo de la obra, no de la persona, y empiezo por lo que sí funciona.",
        "Quien recibe la retroalimentación decide qué incorporar, porque la autoría es suya. Puede agradecer, preguntar y explicar sus razones. Si un comentario de un compañero me incomoda o es una burla, se lo cuento a una persona adulta de confianza. En esta clase los trabajos de ejemplo son inventados y no corresponden a personas reales.",
    ],
    [("retroalimentación", "comentario para ayudar a mejorar un trabajo"), ("sugerencia", "propuesta de cambio dicha con respeto"), ("autoría", "decisiones que pertenecen a quien hizo el trabajo"), ("pregunta de indagación", "pregunta que invita a explicar una decisión"), ("respeto", "valorar el trabajo sin ofender a la persona")],
    [
        w("Armar la retroalimentación", "Trabajo de ejemplo: afiche con letras de 3 cm para un paradero; se lee desde 2 m. Escribe «veo, valoro, sugiero».", ["Veo: letras de 3 cm, se leen desde 2 m.", "Valoro: criterio de lectura a distancia; en un paradero la gente pasa a más distancia.", "Sugiero: probar letras de 10 cm."], "Veo letras de 3 cm; el criterio es lectura a distancia; sugiero letras de 10 cm"),
        w("Mejorar un comentario", "Comentario: «Tu video es un desastre». Reescríbelo con respeto usando este dato de ejemplo: los planos duran entre 15 y 20 s y el propósito es dar energía.", ["Veo: planos de 15 a 20 s.", "Valoro: el propósito es energía y el ritmo es lento.", "Sugiero: probar planos de 4 a 6 s."], "Veo planos de 15 a 20 s; para dar energía sugiero probar planos de 4 a 6 s"),
    ],
    [
        m("Decir «está feo» o «está mal» sin explicar.", "No dice qué rasgo mejorar ni cómo.", "Usa «veo, valoro, sugiero» con un dato observable."),
        m("Comparar el trabajo con el de otra persona: «el de ella es mejor».", "No ayuda a mejorar y puede herir.", "Compara con el criterio y no con personas."),
    ],
    [
        ex("¿Qué es la retroalimentación? A. Un comentario para ayudar a mejorar un trabajo B. Una calificación sin explicación.", "A", "Su fin es mejorar."),
        ex("¿Qué se escribe en el paso «veo»? A. Un rasgo observable B. Una burla.", "A", "Se parte de lo que se ve."),
        ex("¿Cómo se formula una sugerencia? A. Como propuesta respetuosa B. Como orden.", "A", "Quien recibe decide qué incorporar."),
    ],
    [
        ex("¿Cuál comentario sigue la estructura «veo, valoro, sugiero»? A. «Veo que el texto tiene 25 palabras; para un paradero conviene un mensaje corto; sugiero reducirlo a 5» B. «El texto es largo y malo».", "A", "Tiene dato, criterio y propuesta."),
        ex("¿Qué función tiene una pregunta de indagación? A. Invitar a explicar la decisión B. Juzgar la decisión.", "A", "Abre el diálogo sin acusar."),
        ex("Quien recibe la retroalimentación, ¿qué decide? A. Qué incorporar a su trabajo B. Nada, debe aceptar todo.", "A", "La autoría es suya."),
    ],
    [
        ex("Trabajo de ejemplo: mural en una pared de cancha con letras de 5 cm que se miran desde 15 m. ¿Qué sugerencia es adecuada? A. Agrandar las letras para que se lean desde lejos B. Cambiar de compañero de equipo.", "A", "Responde a la lectura a distancia."),
        ex("Reescribe con respeto: «Ese guion no sirve». A. «Veo que el guion no indica la duración de los planos; sugiero agregarla para calcular el total» B. «No sirve, rehazlo».", "A", "Ofrece dato y propuesta."),
        ex("Retroalimentación sobre un video que busca calma, pero tiene cortes cada 1 s. ¿Qué sugerencia es adecuada? A. Alargar los planos a unos 6 u 8 s B. Agregar más cortes.", "A", "Planos largos dan un ritmo lento, propio de la calma."),
    ],
    [
        ex("Un compañero dice: «Te sugiero cambiar el color porque el de Camila es mejor». ¿Qué falla? A. Compara con una persona y no con un criterio B. Usa «sugiero».", "A", "La comparación con personas no ayuda a mejorar."),
        ex("Recibes un comentario que no entiendes. ¿Qué haces? A. Pides un ejemplo o un dato que lo respalde B. Lo ignoras sin preguntar.", "A", "Preguntar permite aprender del comentario."),
    ],
    [
        ex("Un compañero se burla de tu trabajo delante del curso. ¿Qué haces? A. Se lo cuento a una persona adulta de confianza B. Respondo con otra burla.", "A", "Una burla no es retroalimentación; conviene avisar a una persona adulta."),
        ex("Al dar retroalimentación escribes: «te sugiero que tu afiche sea como el de Valentina». ¿Qué corriges? A. Cambiar la comparación por un criterio y un dato B. Nada.", "A", "Comparar con personas no dice qué mejorar."),
    ],
    ex("Tu primo te muestra un dibujo suyo y te pide opinión. ¿Cómo empiezas? A. Con lo que sí funciona, y luego sugieres B. Con lo que está mal.", "A", "Empezar por lo logrado facilita escuchar."),
    [
        ex("¿Cuáles son los tres pasos de la retroalimentación?", "Veo, valoro y sugiero", "Estructuran un comentario útil."),
        ex("Verdadero o falso: se debe aceptar todo comentario sin preguntar.", "Falso", "La autoría permite decidir y preguntar."),
        ex("¿Qué evitas en un comentario?", "Burlas y comparaciones con personas", "No ayudan a mejorar."),
    ],
    task(
        "Escribe retroalimentación para UN trabajo de ejemplo. A) Afiche con letras de 2 cm, fondo gris y letras grises, para un paradero. B) Video de 40 s con 2 planos de 20 s y música fuerte, para mostrar energía. C) Escultura de cajas apiladas de 90 cm con base de 8 cm que se tambalea. Redacta «veo, valoro, sugiero», agrega una pregunta de indagación y evita comparaciones y burlas.",
        "Elegí B. Veo: dos planos de 20 s y música fuerte. Valoro: el ritmo es lento para la energía que se busca. Sugiero: probar planos de 4 a 6 s. Pregunta: ¿qué querías provocar con la música fuerte?",
        ["usa la estructura veo, valoro, sugiero", "parte de un dato observable", "agrega una pregunta de indagación", "no compara con personas ni se burla"],
        ["comentario de tres pasos", "pregunta de indagación"],
        ["comentarios vagos", "comparar con personas"],
        "Pregunta qué dato respalda cada paso y si la sugerencia respeta la autoría.",
    ),
    "Escribe un «veo, valoro, sugiero» sobre un objeto de tu casa.",
    "Explica en tres frases por qué una burla no es retroalimentación.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Hojas y lápiz. El proyecto de ejemplo y su rúbrica están escritos en la clase.",
    "Aprenderé a autoevaluar un trabajo con una rúbrica y a escribir un plan de mejora con acciones concretas. Sirve para valorar mi trabajo con honestidad y saber qué cambiar.",
    ["Sé armar una rúbrica con descriptores observables.", "Sé dar retroalimentación con veo, valoro y sugiero."],
    [
        "La autoevaluación es mirar mi propio trabajo con los mismos criterios que usaría para el de otra persona. Reviso cada criterio de la rúbrica, elijo un nivel y escribo una evidencia. Ser honesto significa reconocer lo logrado y lo que falta, sin exagerar ni disminuir mi trabajo. Si dudo entre dos niveles, vuelvo al descriptor y me pregunto qué dato lo prueba.",
        "Un plan de mejora transforma la evaluación en acciones. Cada acción debe ser concreta, medible y tener un plazo. «Mejorar el ritmo» es vago. «Acortar los planos de más de 10 s a menos de 8 s antes del viernes» es concreto. Ordeno las acciones por impacto: empiezo por el criterio más bajo o más importante.",
        "El resultado de la autoevaluación no es una nota para castigarme. Es información para decidir. Puedo calcular mi avance con la rúbrica: si antes sumaba 9 y ahora 12, avancé 3 puntos. Guardo la autoevaluación y el plan junto con el proyecto como evidencia del proceso. Si no puedo avanzar por falta de material especial o de taller, lo anoto para que lo resuelva el docente.",
    ],
    [("autoevaluación", "evaluación del propio trabajo con criterios"), ("plan de mejora", "lista de acciones concretas para mejorar un trabajo"), ("concreto", "que dice qué, cuánto y cuándo"), ("plazo", "fecha o momento límite de una acción"), ("avance", "diferencia entre dos puntajes en el tiempo")],
    [
        w("Autoevaluar con evidencia", "Rúbrica de 3 criterios con niveles de 1 a 4. Proyecto de ejemplo, afiche: lectura a distancia 3 (letras de 12 cm, se lee desde 4 m); mensaje 4 (texto de 4 palabras); originalidad 2 (usa una fórmula conocida). ¿Cuánto suma y qué criterio mejorar?", ["Suma: 3 + 4 + 2 = 9 de 12.", "El criterio más bajo es originalidad, con 2.", "Mejoro la originalidad."], "9 de 12; mejorar la originalidad"),
        w("Escribir una acción concreta", "Convierte «mejorar la originalidad» en una acción concreta con plazo.", ["Dice qué: probar dos dibujos distintos a la gota conocida.", "Dice cuánto: dos bocetos nuevos.", "Dice cuándo: antes del jueves."], "Hacer dos bocetos de un dibujo distinto a la gota antes del jueves"),
    ],
    [
        m("Ponerse el nivel máximo en todo sin evidencia o el mínimo por modestia.", "La autoevaluación debe ser honesta y comprobable.", "Cita un dato que respalde cada nivel."),
        m("Escribir un plan de mejora con frases vagas como «hacerlo mejor».", "No se sabe qué hacer ni cuándo.", "Escribe qué, cuánto y cuándo."),
    ],
    [
        ex("¿Qué es un plan de mejora? A. Una lista de acciones concretas para mejorar un trabajo B. Una nota final.", "A", "Transforma la evaluación en acciones."),
        ex("¿Qué significa ser honesto al autoevaluarse? A. Reconocer lo logrado y lo que falta B. Poner siempre el nivel máximo.", "A", "La honestidad evita exagerar o disminuir."),
        ex("¿Cuál acción es concreta? A. «Hacer dos bocetos nuevos antes del jueves» B. «Mejorar».", "A", "Dice qué, cuánto y cuándo."),
    ],
    [
        ex("¿Qué criterio conviene mejorar primero? A. El de menor puntaje o mayor importancia B. El que más te guste.", "A", "Así el plan tiene más impacto."),
        ex("¿Qué debe tener cada nivel elegido en una autoevaluación? A. Una evidencia B. Un adjetivo.", "A", "La evidencia respalda el nivel."),
        ex("La autoevaluación sirve para… A. Decidir qué cambiar B. Castigarse.", "A", "Entrega información para mejorar."),
    ],
    [
        ex("Alguien te dice «ponte 4 en originalidad para subir tu total», pero tu afiche usa un dibujo común. ¿Qué haces? A. Mantengo el nivel que respalda mi evidencia B. Me pongo 4 para llegar a un total mayor.", "A", "La autoevaluación debe ser honesta y comprobable."),
        arith("Antes de aplicar el plan, un proyecto de ejemplo sumaba 9 puntos. Después suma 12. ¿Cuántos puntos avanzó?", "12 - 9", "El avance es la diferencia entre los dos puntajes.", " puntos"),
        ex("Rúbrica con niveles de 1 a 4 y un proyecto de ejemplo con 2, 2 y 4. ¿Qué acción conviene primero? A. Mejorar uno de los criterios con 2 B. Mejorar el criterio con 4.", "A", "Hay más margen de avance en los más bajos."),
    ],
    [
        ex("Una persona se pone 4 en originalidad sin dar evidencia, pero su afiche usa un dibujo de internet. ¿Qué falla? A. El nivel no está respaldado B. El plazo.", "A", "No hay evidencia que respalde el nivel."),
        ex("Un plan dice «mejorar el ritmo». Elige la mejor reescritura. A. «Acortar los planos de 15 s a menos de 8 s antes del lunes» B. «Hacer lo mejor posible».", "A", "Es concreta y tiene plazo."),
    ],
    [
        ex("Tu equipo tiene 30 minutos para mejorar un afiche. ¿Qué acción es realista? A. Probar letras más grandes en un boceto B. Rehacer todo el proyecto con material nuevo.", "A", "La acción cabe en el tiempo disponible."),
        ex("Un plan de mejora tiene 5 acciones y solo hay tiempo para 3. ¿Cuáles eliges? A. Las que mejoran los criterios más bajos o más importantes B. Las más fáciles aunque no cambien nada.", "A", "El tiempo limitado se usa donde más impacto tiene."),
    ],
    ex("Quieres mejorar una escultura, pero necesitas una herramienta de taller que no tienes en casa. ¿Qué haces? A. Anotarlo y pedir apoyo al docente B. Usar un cuchillo de cocina.", "A", "Evita riesgos y deja la parte de taller para el docente."),
    [
        ex("¿Qué debe decir una acción concreta?", "Qué, cuánto y cuándo", "Así se puede cumplir y comprobar."),
        ex("Verdadero o falso: la autoevaluación debe ser siempre el nivel máximo.", "Falso", "Debe ser honesta."),
        ex("¿Qué se guarda junto al proyecto como evidencia del proceso?", "La autoevaluación y el plan de mejora", "Muestran cómo se decidieron los cambios."),
    ],
    task(
        "Autoevalúa UN proyecto de ejemplo con la rúbrica de tres criterios (niveles 1 a 4). A) Afiche con letras de 12 cm que se leen desde 4 m, un texto de 20 palabras y un dibujo común. B) Video de 30 s con 3 planos de 10 s, sonido propio y sin personas. C) Escultura de 50 cm con base de 6 cm que se tambalea y materiales reutilizados. Elige un nivel por criterio con evidencia, suma el total y escribe un plan de mejora con dos acciones concretas (qué, cuánto y cuándo).",
        "Elegí C. Criterios: estabilidad 1 (se tambalea), sustentabilidad 4 (todo reutilizado), autoría 3 (diseño propio). Total: 1 + 4 + 3 = 8 de 12. Plan: 1) ensanchar la base de 6 cm a 12 cm antes del miércoles; 2) probar tres empujones suaves con el dedo antes del jueves.",
        ["elige un nivel por criterio con evidencia", "suma bien el total", "escribe dos acciones concretas con plazo", "es honesto con lo logrado y lo que falta"],
        ["autoevaluación con evidencia", "plan de dos acciones"],
        ["niveles sin evidencia", "acciones vagas"],
        "Pregunta qué dato respalda cada nivel y si las acciones se pueden cumplir en el plazo.",
    ),
    "Escribe una acción concreta con plazo para mejorar un trabajo tuyo reciente.",
    "Explica en tres frases por qué un plan de mejora debe tener plazos.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA5, 5,
    "Hojas y lápiz. Las autoevaluaciones y coevaluaciones de ejemplo están escritas en la clase.",
    "Aprenderé a contrastar mi autoevaluación con la coevaluación de un par y a decidir con evidencia qué nivel mantener. Sirve para evaluar con equilibrio y aprender de las diferencias.",
    ["Sé autoevaluar con una rúbrica y evidencia.", "Sé dar retroalimentación respetuosa."],
    [
        "Contrastar la autoevaluación con la coevaluación es comparar el nivel que me puse con el que me pone otra persona, criterio por criterio. Si coinciden, es una buena señal. Si difieren, calculo la diferencia y busco la causa: ¿vieron la misma evidencia?, ¿entendieron igual el descriptor?, ¿hay un dato que yo no consideré? La diferencia es información, no una pelea.",
        "Cuando hay una diferencia de un nivel o más, conversamos con la rúbrica en la mano. Cada uno muestra la evidencia en que se apoya. Si el compañero muestra un dato que yo no vi, puedo corregir mi nivel. Si mi evidencia es más fuerte, mantengo el nivel y explico por qué. Decido yo, porque la autoría es mía, pero con razones.",
        "También reviso el tono de la coevaluación: debe hablar de la obra y no de la persona. Si el comentario es una burla o me incomoda, se lo cuento a una persona adulta de confianza. Al final escribo qué aprendí: qué criterio vi distinto, qué cambié y qué mantengo. Los proyectos de esta clase son de ejemplo y no representan a personas reales.",
    ],
    [("coincidir", "ponerse de acuerdo en un nivel"), ("diferencia", "resta entre dos niveles o puntajes"), ("evidencia", "dato que respalda un nivel"), ("criterio", "razón con que se evalúa"), ("decisión fundamentada", "decisión apoyada en razones comprobables")],
    [
        w("Comparar niveles", "Autoevaluación de un proyecto de ejemplo: ritmo 4, sonido 3, ética 4. Coevaluación: ritmo 3, sonido 3, ética 2. Calcula la diferencia en cada criterio y di dónde conversar.", ["Ritmo: 4 − 3 = 1.", "Sonido: 3 − 3 = 0. Ética: 4 − 2 = 2.", "La mayor diferencia está en ética."], "Ritmo 1, sonido 0, ética 2; conversar sobre ética"),
        w("Decidir con evidencia", "En ética, el compañero dice que falta el permiso de una persona que aparece. ¿Qué haces si es cierto?", ["Reviso las notas de permiso.", "Si falta el permiso, corrijo mi nivel.", "Pido el permiso antes de mostrar el video."], "Corregir el nivel y pedir el permiso"),
    ],
    [
        m("Discutir quién tiene razón sin mirar la evidencia.", "Sin datos no se puede decidir.", "Pon la rúbrica y la evidencia sobre la mesa."),
        m("Aceptar el nivel del compañero para evitar conflicto.", "Una decisión sin razones no es evaluación.", "Compara evidencias y decide con razones."),
    ],
    [
        ex("Cuando la autoevaluación y la coevaluación difieren, ¿qué se hace? A. Se busca la causa con la evidencia B. Se pelea.", "A", "La diferencia es información."),
        ex("¿Qué se calcula al comparar dos niveles? A. La diferencia B. El promedio de edad.", "A", "Resta el menor del mayor."),
        ex("¿Quién decide el nivel final de su propio trabajo? A. Quien lo hizo, con razones B. Cualquiera sin razones.", "A", "La autoría exige decisiones fundamentadas."),
    ],
    [
        ex("Dos personas ponen niveles distintos en ritmo: una midió con «planos de menos de 8 s» y la otra con «planos de menos de 5 s». ¿Cuál es la causa probable de la diferencia? A. Entendieron distinto el descriptor B. Una de las dos no vio el video.", "A", "Los descriptores distintos explican resultados distintos; por eso se contrastan antes de decidir."),
        ex("Tu compañero te pone nivel 2 en sonido y tú te pusiste 3. ¿Qué haces primero? A. Pedir su evidencia y mostrar la tuya B. Cambiar tu nivel de inmediato.", "A", "Se contrastan las evidencias antes de decidir."),
        ex("Tu compañero muestra un dato que no habías visto y confirma el nivel 2. ¿Qué corresponde? A. Corregir tu nivel B. Mantener 3.", "A", "El nuevo dato cambia la evidencia."),
    ],
    [
        arith("Autoevaluación de un proyecto de ejemplo: 4, 3 y 4. Coevaluación: 3, 3 y 2. ¿Cuántos puntos suman en total las diferencias (sin signo)?", "(4 - 3) + (3 - 3) + (4 - 2)", "Se suman las diferencias de los tres criterios.", " puntos"),
        ex("La autoevaluación suma 11 y la coevaluación suma 8. ¿Qué conviene hacer? A. Comparar criterio por criterio, porque el total no dice dónde está la diferencia B. Quedarse con el promedio de ambos totales.", "A", "La diferencia se entiende viendo en qué criterios y con qué evidencia se separan."),
        ex("Tú mantienes tu nivel 3 en lectura a distancia porque el afiche se lee desde 4 m; tu compañero dice 2 sin dar datos. ¿Qué haces? A. Mantienes 3 y pides su evidencia B. Cambias a 2.", "A", "Tu evidencia es medible y la suya no está dada."),
    ],
    [
        ex("Una persona cambia su nivel solo porque su amiga se lo pidió. ¿Es una decisión fundamentada? A. No, no usó evidencia B. Sí.", "A", "Un cambio sin razones no es evaluación."),
        ex("Las dos evaluaciones difieren en 0 en todos los criterios. ¿Qué conviene todavía? A. Revisar si ambas tienen evidencia suficiente B. Dar por perfecta la evaluación.", "A", "Coincidir no garantiza que haya evidencia."),
    ],
    [
        ex("Un compañero comenta tu video de ejemplo: «Tu video es flojo». ¿Qué le pides? A. Que lo diga con veo, valoro y sugiero B. Que no lo comente.", "A", "Un comentario fundamentado ayuda a mejorar."),
        ex("Dos personas se ponen el mismo nivel 4 en originalidad y ninguna dice por qué. ¿Qué falta para considerarlo fundamentado? A. La evidencia B. Otro nivel.", "A", "Coincidir no basta sin datos que lo respalden."),
    ],
    ex("Recibes una coevaluación que se burla de tu trabajo. ¿Qué haces? A. Se lo cuento a una persona adulta de confianza B. Respondes con otra burla.", "A", "La burla no es evaluación; conviene avisar a una persona adulta."),
    [
        ex("¿Qué se hace con la diferencia entre dos evaluaciones?", "Se busca la causa con la evidencia", "La diferencia es información."),
        ex("Verdadero o falso: se debe aceptar siempre el nivel del compañero.", "Falso", "Se decide con razones."),
        ex("¿Qué se escribe al final del contraste?", "Qué se aprendió, qué se cambió y qué se mantiene", "Cierra el proceso de evaluación."),
    ],
    task(
        "Contrasta una autoevaluación con una coevaluación de ejemplo. Caso A (video): autoevaluación ritmo 4, sonido 3, ética 4; coevaluación ritmo 3, sonido 3, ética 2 porque falta el permiso de una persona que aparece. Caso B (afiche): autoevaluación lectura 3, mensaje 4, originalidad 3; coevaluación lectura 2, mensaje 4, originalidad 3 porque desde 5 m no se lee. Elige un caso, calcula las diferencias, decide qué nivel mantienes o cambias con evidencia y escribe qué aprendiste.",
        "Elegí el caso B. Diferencias: lectura 1, mensaje 0, originalidad 0. La diferencia está en lectura. El compañero dice que desde 5 m no se lee; yo medí que se lee desde 4 m. Mantengo 3 si mi criterio exige 3 m; si exige 5 m, cambio a 2. Aprendí que debo acordar la distancia del descriptor antes de evaluar.",
        ["calcula las diferencias por criterio", "decide con evidencia", "explica por qué mantiene o cambia", "escribe qué aprendió"],
        ["tabla de diferencias", "decisión fundamentada"],
        ["cambiar el nivel sin razones", "discutir sin evidencia"],
        "Pregunta qué dato justifica la decisión y qué cambiaría en la rúbrica para evitar la diferencia.",
    ),
    "Escribe dos niveles distintos para un mismo criterio de un trabajo tuyo y la evidencia que usarías para defender cada uno.",
    "Explica en tres frases por qué una diferencia entre evaluaciones puede ser información útil.",
)

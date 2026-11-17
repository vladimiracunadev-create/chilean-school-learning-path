"""Estética (electivo HC, 3.º y 4.º medio): OAC-01 (textos filosóficos sobre belleza, demarcación del arte, experiencia estética, percepción sensible y propósitos de la creación) y OAC-02 (evaluar posiciones de escuelas y sus métodos de razonamiento), clases 1 a 5 de cada OA. Obras y casos ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, caso o ficha está escrito en el enunciado. "
             "Los textos filosóficos son resúmenes originales de posturas y las obras de arte son casos ficticios descritos con palabras: no se reproducen obras con derechos ni se usan imágenes o audio. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es analizar y evaluar. Si tu docente propone mirar o escuchar una obra real, hazlo en sala y con las pautas que él o ella indique. "
             "En los temas de moral, política o bienestar emocional se usan casos ficticios; si algo te afecta, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O1 = "FI-ESTE-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso original). En una feria de barrio se exhibe «El huerto de Rosa», un cuadro ficticio de colores intensos que muestra un huerto, pintado por una aficionada. Tres visitantes opinan. "
     "Ana: «Es bello porque todos los que pasan se detienen a mirarlo; la belleza está en el cuadro.» "
     "Beto: «Para mí es bello porque me recuerda a mi abuela; a otra persona quizá no le pase lo mismo.» "
     "Carla: «Lo medí: tiene 40 por 50 centímetros. Eso es un dato, no es una belleza.»")
build(
    O1, 1, F,
    use="Aprenderé a plantear un problema estético a partir de un caso, a distinguir un juicio de hecho de un juicio estético y a reconocer dos respuestas clásicas a la pregunta por dónde está la belleza.",
    prior=["Sé distinguir un hecho de una opinión.", "Sé identificar la tesis de un texto breve.", "Conozco el vocabulario básico de argumentación de Filosofía."],
    explain=[
        "La estética es la parte de la filosofía que se pregunta por la belleza, por el arte y por el modo en que los sentimos y los juzgamos. Un problema estético es una pregunta de ese campo que no se resuelve con una medición, por ejemplo: ¿la belleza está en el objeto o en quien lo mira?",
        "Un juicio de hecho afirma algo que puede comprobarse con una medida o una observación compartida, como «el cuadro mide 40 por 50 centímetros». Un juicio estético valora cómo algo se nos presenta a los sentidos, como «el cuadro es bello». Confundir ambos lleva a discusiones sin salida.",
        "Frente al problema de dónde está la belleza hay dos respuestas clásicas. El objetivismo estético sostiene que la belleza es una propiedad del objeto, aunque nadie lo mire. El subjetivismo estético sostiene que depende de quien mira y de su experiencia. Ambas se evalúan con razones, no con gritos.",
    ],
    vocab=[("estética", "parte de la filosofía que estudia la belleza, el arte y la experiencia de ambos"), ("problema estético", "pregunta sobre la belleza o el arte que no se resuelve midiendo"), ("juicio de hecho", "afirmación que se puede comprobar con una medida u observación compartida"), ("juicio estético", "valoración de cómo algo se presenta a los sentidos, por ejemplo «es bello»"), ("objetivismo estético", "postura según la cual la belleza está en el objeto"), ("subjetivismo estético", "postura según la cual la belleza depende de quien mira")],
    worked=[
        ("Clasificar dos frases", "Una vecina dice sobre una escultura ficticia: «Pesa 12 kilos» y luego: «Es una escultura armoniosa». Clasifica cada frase.",
         ["Pregunta si puede comprobarse con una medida: el peso sí se puede pesar.", "Pregunta si valora cómo se presenta a los sentidos: «armoniosa» valora la forma percibida."],
         "«Pesa 12 kilos» es un juicio de hecho; «es armoniosa» es un juicio estético"),
        ("Reconocer una postura", "Un joven afirma: «Un atardecer sigue siendo bello aunque no haya nadie para mirarlo». ¿Qué postura expresa?",
         ["Busca dónde ubica la belleza: en el atardecer mismo y no en quien lo mira.", "Esa ubicación en el objeto corresponde al objetivismo estético."],
         "Objetivismo estético"),
    ],
    mistakes=[("Creer que si la belleza depende de cada persona, entonces no se puede razonar sobre ella.", "Se confunde que el gusto sea personal con que no admita razones.", "Aun siendo personal, se pueden dar y comparar razones sobre lo que se percibe."),
              ("Tratar «mide 40 por 50 centímetros» como si respondiera si el cuadro es bello.", "Se mezcla un juicio de hecho con uno estético.", "Separa lo medible de lo que se valora y pregunta qué relación hay entre ambos.")],
    T=[
        ("abc", "{F} ¿Qué comentario de la ficha afirma algo que se puede comprobar con una huincha?", "El de Carla, sobre las medidas del cuadro", "El de Ana, sobre la gente que se detiene", "El de Beto, sobre el recuerdo de su abuela", "Solo las medidas se pueden comprobar con una huincha; los otros dos comentarios valoran o recuerdan."),
        ("abc", "{F} ¿Dónde ubica Beto la belleza del cuadro?", "En la experiencia y el recuerdo de quien lo mira", "En el cuadro mismo, aunque nadie lo mire", "En el número de personas que lo miran", "Beto dice que es bello por lo que le recuerda y que otros quizá no lo sientan igual."),
        ("En Estética: ¿cómo se llama la postura que ubica la belleza en el objeto, con independencia de quien lo mire?", "Objetivismo estético", "Es el nombre de la postura que hace de la belleza una propiedad del objeto."),
        ("abc", "¿Cuál de estas preguntas es un problema estético en el sentido de la clase?", "¿Está la belleza en las cosas o en quien las mira?", "¿Cuántos kilos pesa una escultura de bronce?", "¿Cuántos centímetros mide un lienzo?", "Las otras dos se responden pesando o consultando un precio; la primera no se resuelve midiendo."),
        ("abc", "{F} Ana justifica su opinión diciendo que todos se detienen a mirar. ¿Qué hace Ana?", "Da una razón de comportamiento para apoyar su tesis de que la belleza está en el cuadro", "Mide el cuadro con una huincha", "Cuenta un recuerdo personal", "Ana ofrece un hecho observable, la gente se detiene, como razón de su tesis objetivista."),
        ("ab", "¿Qué hace un juicio estético?", "Valora cómo algo se presenta a los sentidos", "Informa una medida exacta del objeto", "El juicio estético valora lo percibido, mientras que una medida exacta es un juicio de hecho."),
        ("abc", "Un vecino dice sobre una silla ficticia: «La silla tiene cuatro patas», «es elegante» y «pesa tres kilos». ¿Cuál de las frases es un juicio estético?", "«Es elegante»", "«Tiene cuatro patas»", "«Pesa tres kilos»", "Elegante valora la forma percibida; contar patas y pesar son comprobaciones de hecho."),
        ("abc", "¿Cuál de estas frases expresa una postura subjetivista?", "«Lo bello es lo que cada persona siente como bello»", "«La belleza es una propiedad del objeto aunque nadie lo mire»", "«El cuadro mide 40 por 50 centímetros»", "Solo la primera hace depender la belleza de quien siente."),
        ("abc", "{F} ¿Cuál de estas preguntas resume el desacuerdo entre Ana y Beto?", "¿La belleza está en el objeto o en quien lo mira?", "¿Qué técnica se usó para pintar el cuadro?", "¿Cuántas personas visitaron la feria?", "Ana ubica la belleza en el cuadro y Beto en la experiencia de quien mira."),
        ("abc", "{F} Carla dice que su medición no habla de belleza. ¿Se equivocan Ana y Beto por eso?", "No: el tamaño es un dato distinto y no decide por sí solo si es bello", "Sí: si el cuadro mide 40 por 50 ya no puede ser bello", "Sí: las medidas siempre prueban la belleza", "La medida es un juicio de hecho y no resuelve el juicio estético; por eso no refuta a Ana ni a Beto."),
        ("abc", "{F} Beto dice que a otra persona quizá no le pase lo mismo. ¿Qué podría mostrar Ana para responderle con evidencia?", "Que personas con recuerdos muy distintos también se detienen y valoran el cuadro", "Que Ana se detuvo mucho rato frente al cuadro", "Que el cuadro mide 40 por 50 centímetros", "Si el aprecio aparece también en personas con recuerdos distintos, la explicación de Beto pierde fuerza."),
        ("abc", "Un amigo dice: «Si la belleza depende de cada uno, no tiene sentido discutir de arte». ¿Es sólido ese razonamiento?", "No: aunque el gusto sea personal, se pueden dar y comparar razones sobre lo que se percibe", "Sí: lo que depende de cada uno no admite razones", "Sí: discutir de arte siempre termina en medir", "Del carácter personal del gusto no se sigue que sea imposible razonar sobre él."),
        ("abc", "Un jurado dice: «Como los cinco jueces votaron por esta escultura ficticia, la belleza está en la escultura para siempre». ¿Qué falla?", "Un acuerdo de cinco personas en un momento no prueba que la belleza sea una propiedad permanente del objeto", "Que fueron muy pocos jueces para votar", "Que los jueces votaron por escrito", "El acuerdo de un grupo es una evidencia limitada: no demuestra una propiedad permanente."),
    ],
    ctx=("abc", "En un liceo deben elegir entre dos afiches ficticios para una exposición. Un estudiante propone medir con regla cuál es más bello. ¿Qué conviene responderle?", "La regla mide tamaño, que es un hecho; para decidir cuál es más bello hay que dar razones sobre lo que se percibe", "Tiene razón: lo bello se mide con regla", "No se puede decidir nada, porque todo es personal", "Medir sirve para datos como el tamaño, pero el juicio estético necesita razones sobre colores, formas y efecto en quien mira."),
    sc=[
        ("En Estética: ¿qué es un juicio de hecho?", "Una afirmación que se puede comprobar con una medida u observación compartida", "Se distingue del juicio estético porque admite comprobación objetiva."),
        ("¿Qué sostiene el subjetivismo estético?", "Que la belleza depende de quien mira y de su experiencia", "Es la postura que ubica la belleza en el sujeto y no en el objeto."),
        ("¿Por qué «el gusto es personal» no implica que sea imposible dar razones?", "Porque se pueden dar y comparar razones sobre lo que se percibe", "Que una experiencia sea propia no impide describirla y justificarla."),
    ],
    op=("Elige una de estas frases y analízala: (1) «La música de las plazas siempre es hermosa». (2) «Esta mesa de roble mide 120 centímetros». (3) «Ese mural es feo, aunque lo pintaron muchas personas». "
        "Para la que elijas, escribe si es un juicio de hecho o estético, qué problema estético plantea, qué postura (objetivista o subjetivista) parece suponer y una razón a favor y otra en contra.",
        "Frase 1: es un juicio estético; plantea si la belleza está en la música o en quien la oye; parece objetivista porque dice «siempre». A favor: muchas personas se detienen a escucharla. En contra: alguien podría estar cansado y no disfrutarla.",
        ["clasifica correctamente la frase", "formula el problema como una pregunta", "reconoce la postura que supone", "da una razón a favor y una en contra"],
        ["ficha con clasificación, problema, postura y dos razones"],
        ["tratar una medida como si fuera un juicio de belleza", "responder solo «es subjetivo» sin dar razones", "dar solo razones a favor"],
        "Pregunta: «¿puedes comprobar tu frase con una medida o necesitas hablar de lo que se percibe?». Pídele que subraye la razón en contra."),
    reinforce="Anota cinco frases que oíste esta semana sobre cosas bellas o feas y marca cuáles son juicios de hecho y cuáles juicios estéticos.",
    extend="Explica con tus palabras por qué una persona objetivista y una subjetivista podrían describir de forma distinta el desacuerdo entre Ana y Beto.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (casos originales y glosario). Caso 1: Lucía escucha una pieza de guitarra en la plaza y, mientras suena, deja de pensar en sus tareas y atiende a cada nota hasta que termina. "
     "Caso 2: Mateo pone la misma pieza solo para que su hermana pequeña se duerma y no presta atención a la música. "
     "Caso 3: Tamara dice: «Veo un cuadro con mucho azul y una figura inclinada», y después añade: «Parece triste». "
     "Glosario: percepción sensible = conocer algo por los sentidos (ver, oír, tocar); experiencia estética = atender con interés a cómo algo se presenta a los sentidos, por sí mismo y no solo por su utilidad.")
build(
    O1, 2, F,
    use="Aprenderé a definir belleza, experiencia estética, percepción sensible, demarcación del arte y propósitos de la creación artística, y a usarlas para analizar fragmentos de textos filosóficos.",
    prior=["Distingo juicio de hecho de juicio estético.", "Reconozco el objetivismo y el subjetivismo estético.", "Sé definir un concepto con mis palabras."],
    explain=[
        "Percepción sensible es el conocimiento que obtenemos por los sentidos. Es distinta de la interpretación, que añade un significado, como cuando de un cuadro con mucho azul se concluye que «es triste». La experiencia estética es una forma especial de percepción: se atiende con interés a cómo algo se presenta, por sí mismo y no solo por su utilidad.",
        "La belleza es la cualidad que valoramos en lo que nos produce agrado o admiración al percibirlo. Algunas posturas la vinculan con la forma (proporción, armonía), otras con el sentimiento que despierta. La demarcación del arte es el problema de encontrar un criterio que permita decidir qué cuenta como obra de arte y qué no.",
        "Los propósitos de la creación artística son las razones por las que alguien crea: expresar un sentimiento, representar la realidad, comunicar una idea, celebrar, criticar o decorar. Un mismo objeto puede tener varios propósitos a la vez, y quienes lo miran pueden descubrir otros que el autor no pensó. Definir bien estos conceptos permite leer un texto filosófico sin confundirlos.",
    ],
    vocab=[("percepción sensible", "conocimiento que se obtiene por los sentidos"), ("experiencia estética", "atención interesada a cómo algo se presenta a los sentidos, por sí mismo"), ("belleza", "cualidad valorada en lo que agrada o admira al percibirlo"), ("demarcación del arte", "problema de hallar un criterio para decidir qué cuenta como arte"), ("propósito de la creación artística", "razón por la que alguien crea una obra"), ("interpretación", "significado que se añade a lo percibido")],
    worked=[
        ("Aplicar el concepto de experiencia estética", "Caso: Julián mira un bordado ficticio y se queda largo rato siguiendo cómo cambian los hilos de color, sin pensar en para qué sirve. ¿Es una experiencia estética?",
         ["Pregunta si atiende a cómo se presenta el objeto: sí, sigue los hilos y el color.", "Pregunta si lo hace por sí mismo y no por su utilidad: sí, no piensa en para qué sirve."],
         "Sí, es una experiencia estética"),
        ("Separar percepción e interpretación", "Una frase dice: «Veo una línea roja que cruza la hoja y siento miedo». ¿Qué parte es percepción y qué parte interpretación o reacción?",
         ["La percepción es lo que se ve: una línea roja que cruza la hoja.", "El miedo es una reacción y un significado que se añade a lo percibido."],
         "Percepción: la línea roja que cruza la hoja; interpretación o reacción: el miedo"),
    ],
    mistakes=[("Llamar experiencia estética a cualquier uso de un objeto bello.", "Se olvida que la experiencia estética atiende al objeto por sí mismo.", "Pregunta si se está atendiendo a cómo se presenta o solo a su utilidad."),
              ("Dar por percibido lo que en realidad se interpreta, como «el cuadro es triste».", "Se mezcla lo que se ve con el significado que se le añade.", "Primero describe lo que ven los sentidos y después indica qué interpretas de ello.")],
    T=[
        ("abc", "{F} ¿En cuál caso hay experiencia estética según el glosario?", "En el caso 1, de Lucía, que atiende a cada nota por sí misma", "En el caso 2, de Mateo, que usa la música para dormir a su hermana", "En ninguno de los dos casos", "Solo Lucía atiende a cómo se presenta la música por sí misma."),
        ("abc", "{F} En el caso 3, ¿qué parte de lo dicho por Tamara es percepción?", "«Un cuadro con mucho azul y una figura inclinada»", "«Parece triste»", "Las dos frases por igual", "Lo azul y la figura inclinada se ven; «triste» es un significado que se añade."),
        ("En Estética: ¿cómo se llama el problema de encontrar un criterio para decidir qué cuenta como obra de arte?", "Demarcación del arte", "Ese es el nombre que recibe el problema de trazar la frontera entre arte y no arte."),
        ("abc", "¿Cuál es un propósito de la creación artística según la explicación?", "Expresar un sentimiento", "Calcular un área", "Ahorrar tiempo en la tarea", "Expresar, representar, comunicar, celebrar, criticar o decorar son propósitos; las otras opciones no lo son."),
        ("abc", "Una pintora ficticia hace un mural para mostrar su orgullo por el barrio. ¿Qué propósito principal tiene?", "Expresar y celebrar", "Informar un horario", "Advertir de un peligro", "Quiere mostrar un orgullo y festejar el barrio, es decir, expresar y celebrar."),
        ("ab", "Una persona mira un jarrón ficticio y piensa solo en cuántas flores le caben. ¿Es una experiencia estética?", "No: atiende a su utilidad y no a cómo se presenta", "Sí: cualquier mirada a un jarrón lo es", "Piensa solo en la capacidad del jarrón, por lo que no atiende a cómo se presenta."),
        ("abc", "Una frase dice: «Escucho tres notas agudas seguidas y siento alegría». ¿Qué es la alegría en el sentido de la clase?", "Una reacción o interpretación que se añade a lo percibido", "La percepción sensible misma", "Un propósito de la creación artística", "Las notas se oyen; la alegría es la reacción que se añade a lo percibido."),
        ("abc", "{F} Si Mateo, de repente, se detuviera a escuchar con interés cómo se entrelazan las notas, ¿qué cambiaría?", "Pasaría a tener una experiencia estética", "Seguiría usando la música solo por su utilidad", "Perdería interés en la pieza", "Atender con interés a cómo se presenta la música por sí misma es lo que define la experiencia estética."),
        ("abc", "Una tesis dice: «Un objeto es arte cuando alguien lo creó para provocar una experiencia estética». ¿A qué problema responde?", "A la demarcación del arte", "A la técnica con que se pinta", "A la historia de los museos", "Propone un criterio para decidir qué cuenta como arte."),
        ("abc", "{F} Tamara dice «parece triste». ¿Qué debería hacer para sostenerlo con evidencia?", "Señalar qué elementos percibidos, como el azul y la figura inclinada, apoyan esa interpretación", "Preguntar a más personas si a ellas también les parece triste", "Decir que el azul siempre significa tristeza", "Una interpretación se sostiene con elementos percibidos de la obra."),
        ("abc", "Un cartel de seguridad ficticio es muy claro y sus colores llaman la atención. Alguien dice: «Es bello, luego es arte». ¿Qué falla?", "Que algo sea bello no basta para que cuente como arte según un criterio de demarcación", "Que un cartel no puede ser bello", "Que ser arte depende del tamaño del objeto", "Belleza y arte son conceptos distintos: la demarcación pide un criterio adicional."),
        ("abc", "Una escultora ficticia dice: «Hice esta figura para criticar el despilfarro, no para que sea bonita». ¿Qué muestra?", "Que el propósito de una obra puede no ser que sea bella", "Que toda obra debe ser bonita", "Que no tiene propósito", "Criticar es un propósito legítimo distinto de producir belleza."),
        ("abc", "Dos lectores dicen: «El poema ficticio habla de duelo» y «yo lo leí como esperanza». ¿Qué ejemplifica?", "Que a una obra se le puede añadir más de una interpretación", "Que uno de los dos leyó mal el poema", "Que el poema es un juicio de hecho", "Interpretaciones distintas pueden surgir de lo mismo que se percibe."),
    ],
    ctx=("abc", "Un guía de museo ficticio muestra una vasija antigua y dice: «Esta vasija sirvió para guardar agua y hoy la miramos por su forma». ¿Qué cambio de actitud describe?", "Pasa de verla por su utilidad a atenderla por cómo se presenta, es decir, con experiencia estética", "Pasa de usarla a regalarla", "Pasa de una experiencia estética a un uso práctico", "Mirarla por su forma, y no solo por el uso que tuvo, es atender a cómo se presenta: experiencia estética."),
    sc=[
        ("En Estética: ¿qué es la experiencia estética?", "Atender con interés a cómo algo se presenta a los sentidos, por sí mismo", "No se reduce a usar el objeto, sino a atender a su modo de presentarse."),
        ("¿En qué se diferencian percepción e interpretación?", "La percepción es lo que captan los sentidos y la interpretación añade un significado", "Lo percibido es la base y el significado se agrega después."),
        ("¿Qué busca resolver la demarcación del arte?", "Un criterio para decidir qué cuenta como obra de arte", "Es el problema de la frontera entre arte y no arte."),
    ],
    op=("Elige uno de estos objetos ficticios: (1) una jarra de greda con dibujos de aves, (2) una melodía que se toca con una flauta, (3) un cartel con un poema corto. "
        "Escribe: qué percibirían los sentidos, una interpretación posible, un propósito que pudo tener quien lo creó y cómo sería una experiencia estética con él, distinguida de un simple uso.",
        "Objeto 1. Percepción: dibujos de aves de color oscuro sobre greda clara. Interpretación: parece hablar de libertad. Propósito: decorar y celebrar la vida del campo. Experiencia estética: detenerme a seguir la línea de las aves sin pensar en servir agua; uso: solo servir agua.",
        ["separa lo percibido de la interpretación", "indica un propósito de creación posible", "distingue experiencia estética de uso", "usa los términos de la clase con sentido"],
        ["ficha con percepción, interpretación, propósito y diferencia entre experiencia y uso"],
        ["incluir la interpretación como si fuera percepción", "confundir propósito con interpretación", "decir que usar el objeto ya es experiencia estética"],
        "Pregunta: «¿esa frase la ven los ojos o la agregas tú?». Pídele que marque con distinto color lo percibido y lo interpretado."),
    reinforce="Elige un objeto de tu casa y escribe primero lo que perciben tus sentidos y después una interpretación que añadas.",
    extend="Explica con un ejemplo propio por qué un mismo objeto puede servir a la vez para un uso y para una experiencia estética.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (resúmenes originales de dos posturas; no son citas). Texto A (postura formalista): «Una obra vale por su forma: por cómo se organizan sus líneas, colores o sonidos. Si para entenderla necesitas conocer la vida de quien la hizo, estás hablando del autor y no de la obra. Por eso dos personas que atienden a la forma pueden coincidir en que una pieza es bella aunque no sepan nada de quién la creó.» "
     "Texto B (postura expresivista): «Una obra es arte cuando transmite un sentimiento de modo que otros puedan sentirlo. Una figura perfecta pero sin sentimiento es solo un ejercicio. Por eso saber qué quiso expresar quien creó la obra ayuda a comprenderla.»")
build(
    O1, 3, F,
    use="Aprenderé a reconstruir una perspectiva filosófica a partir de un texto: su pregunta, su tesis, sus razones y sus supuestos, sin mezclarla con mi opinión.",
    prior=["Reconozco juicios de hecho y estéticos.", "Defino experiencia estética y percepción sensible.", "Sé distinguir una tesis de sus razones."],
    explain=[
        "Reconstruir una perspectiva es explicar con claridad lo que un texto sostiene, aunque no estemos de acuerdo. Se hace en cuatro pasos: la pregunta a la que responde el texto, su tesis (lo que afirma), sus razones (por qué lo afirma) y sus supuestos (ideas que da por ciertas sin decirlo).",
        "En estética hay posturas que ponen el centro en la forma de la obra, como el formalismo. Otras lo ponen en el sentimiento que se expresa, como el expresivismo. Otras, en lo que la obra representa de la realidad, como la postura de la imitación. Cada una responde de manera distinta a qué es el arte y a qué importa en una obra.",
        "Al reconstruir conviene usar frases como «el texto sostiene que…» o «según esta postura…», para no mezclar lo que dice el texto con lo que pienso yo. Después se puede evaluar, pero eso es otro paso. Un buen resumen no repite el texto: lo reordena en pregunta, tesis, razones y supuesto.",
    ],
    vocab=[("tesis", "lo que un texto o una persona afirma como idea central"), ("razón", "afirmación que se da para apoyar una tesis"), ("supuesto", "idea que un texto da por cierta sin decirla"), ("formalismo", "postura que pone el valor de una obra en su forma"), ("expresivismo", "postura que pone el valor de una obra en el sentimiento que expresa"), ("reconstruir una perspectiva", "explicar la pregunta, tesis, razones y supuestos de un texto sin mezclar opinión propia")],
    worked=[
        ("Reconstruir el Texto A", "Reconstruye en cuatro pasos el Texto A de una ficha parecida: «Una obra vale por su forma. Para entenderla no hace falta conocer al autor».",
         ["Pregunta: ¿qué hace valiosa a una obra?", "Tesis: lo que vale es su forma. Razón: entender la obra no requiere conocer al autor. Supuesto: lo que no se percibe en la obra no cuenta para valorarla."],
         "Pregunta: qué hace valiosa a una obra; tesis: su forma; razón: no hace falta conocer al autor; supuesto: solo cuenta lo que se percibe en la obra"),
        ("Distinguir tesis y razón", "En «Una obra es arte cuando transmite un sentimiento, porque el arte sirve para comunicarnos», ¿qué es la tesis y qué es la razón?",
         ["Busca la afirmación central: una obra es arte cuando transmite un sentimiento.", "Busca lo que la apoya, que viene después de «porque»: el arte sirve para comunicarnos."],
         "Tesis: una obra es arte cuando transmite un sentimiento; razón: el arte sirve para comunicarnos"),
    ],
    mistakes=[("Resumir un texto agregando lo que uno piensa de él.", "Se mezcla reconstruir con evaluar.", "Reconstruye primero con «el texto sostiene que…» y evalúa después en un párrafo aparte."),
              ("Tomar una razón como si fuera la tesis.", "Se confunde la idea central con lo que la apoya.", "Pregunta: ¿esto es lo que se afirma o la razón por la que se afirma?")],
    T=[
        ("abc", "{F} ¿Qué sostiene el Texto A sobre lo que hace valiosa una obra?", "Su forma, es decir, cómo se organizan líneas, colores o sonidos", "El sentimiento del autor", "La vida de quien la creó", "La tesis del Texto A es que la obra vale por su forma."),
        ("abc", "{F} ¿Qué sostiene el Texto B sobre cuándo una obra es arte?", "Cuando transmite un sentimiento de modo que otros puedan sentirlo", "Cuando su forma es perfecta", "Cuando se vende bien", "El Texto B liga el arte con transmitir un sentimiento."),
        ("En Estética: ¿cómo se llama la postura que pone el valor de una obra en su forma?", "Formalismo", "Es el nombre de la postura que privilegia la forma de la obra."),
        ("abc", "{F} Según el Texto A, ¿por qué conocer la vida del autor no es necesario?", "Porque eso habla del autor y no de la obra", "Porque la vida del autor es un secreto", "Porque las obras no tienen autor", "La razón del texto es que conocer la vida del autor es hablar del autor y no de la obra."),
        ("abc", "{F} Según el Texto B, ¿por qué saber qué quiso expresar el autor ayuda a comprender la obra?", "Porque la obra transmite un sentimiento y conocer el propósito ayuda a captarlo", "Porque la forma de la obra siempre es perfecta", "Porque el sentimiento es independiente de quien creó la obra", "El texto liga la comprensión con el sentimiento que quiso expresar el autor."),
        ("ab", "En «La música sirve para comunicar emociones, por eso es arte», ¿cuál es la razón?", "«La música sirve para comunicar emociones»", "«Es arte»", "La razón es lo que apoya la tesis, y la tesis es que la música es arte."),
        ("abc", "{F} ¿Qué supuesto sin decir parece tener el Texto B?", "Que un sentimiento puede pasar de quien crea la obra a quienes la miran", "Que la forma de una obra no se puede percibir", "Que el arte siempre debe representar la realidad", "Si una obra «transmite» un sentimiento «de modo que otros puedan sentirlo», se supone que ese traspaso es posible."),
        ("abc", "{F} Una estudiante resume: «El Texto B tiene razón, y por eso una obra es arte si transmite un sentimiento». ¿Qué falla como reconstrucción?", "Mezcla su acuerdo con lo que dice el texto en lugar de solo explicarlo", "Es demasiado breve", "Cambia la tesis del texto", "Una reconstrucción separa lo que el texto sostiene de la valoración propia."),
        ("abc", "{F} Un estudiante dice que el Texto A afirma que el sentimiento no existe. ¿Qué error comete?", "Atribuye al texto algo que no dice: solo afirma que la valoración de la obra se centra en la forma", "Nada: es una buena lectura del Texto A", "Confunde formalismo con expresivismo", "El texto no niega el sentimiento; centra el valor de la obra en la forma."),
        ("abc", "{F} Dos obras ficticias tienen la misma forma, pero una nació de una tristeza real y la otra fue un ejercicio de taller. ¿Qué diría cada texto?", "A: tienen el mismo valor porque la forma es la misma; B: la primera expresa un sentimiento y es más arte", "A: no pueden compararse; B: la segunda vale más", "A y B: tienen distinto valor en ambos casos", "El formalismo mira la forma; el expresivismo, el sentimiento transmitido."),
        ("abc", "{F} ¿Qué pregunta puede decirse que respondería el Texto B?", "¿Qué hace que una obra sea arte?", "¿Qué obras se exhiben en un museo?", "¿Cuánto tiempo tarda en pintarse una obra?", "El texto propone un criterio de qué cuenta como arte, es decir, responde a esa pregunta."),
        ("abc", "{F} Un alumno dice: «Ambos textos hablan de lo mismo, la forma». ¿Qué corrección corresponde?", "Solo el Texto A pone el centro en la forma; el B lo pone en el sentimiento transmitido", "Solo el Texto B habla de la forma", "Ambos ponen el centro en el sentimiento", "Los textos responden con criterios distintos: forma o sentimiento."),
        ("abc", "{F} Si alguien quisiera cuestionar el supuesto del Texto A, ¿qué podría preguntar?", "¿No importan la época y las intenciones para comprender una obra?", "¿Cuánto mide la obra?", "¿Quién compra las obras?", "Cuestionar el supuesto es dudar de que solo cuente lo percibido en la obra."),
    ],
    ctx=("abc", "En un taller, una guía lee los dos textos de la ficha y pide un resumen de cada uno antes de opinar. Una estudiante entrega: «A dice que lo central es la forma; B dice que lo central es el sentimiento transmitido; yo creo que A se equivoca». ¿Qué hay que corregir?", "Separar su juicio personal del resumen: la última frase pertenece a la evaluación, no a la reconstrucción", "Que A y B digan lo mismo", "Agregar una cita de cada texto", "Reconstruir es exponer lo que sostiene cada texto; el desacuerdo se deja para el paso de evaluar."),
    sc=[
        ("En Estética: ¿qué es el expresivismo?", "La postura que pone el valor de una obra en el sentimiento que expresa", "Se opone al formalismo, que mira la forma."),
        ("¿Cuáles son los cuatro pasos para reconstruir una perspectiva?", "Pregunta, tesis, razones y supuestos", "Son los pasos que ordenan el contenido del texto."),
        ("¿Qué es un supuesto?", "Una idea que el texto da por cierta sin decirla", "Se descubre preguntando qué tendría que ser cierto para que el razonamiento funcione."),
    ],
    op=("Lee este texto original (postura de la imitación): «El arte nos enseña a mirar la realidad con atención. Una pintura de un puerto vale cuando permite reconocer cómo es un puerto, aunque lo haga a su manera. Por eso las obras que representan bien el mundo ayudan a conocerlo.» "
        "Reconstrúyelo en cuatro pasos: pregunta, tesis, razón y un supuesto. Después añade, aparte, una frase de evaluación propia.",
        "Pregunta: ¿qué valor tiene el arte? Tesis: el arte vale cuando representa bien el mundo. Razón: ayuda a conocer la realidad. Supuesto: que representar la realidad es lo principal del arte. Evaluación (aparte): no explica el arte abstracto.",
        ["formula la pregunta del texto", "distingue la tesis de la razón", "explicita un supuesto razonable", "separa la evaluación propia del resumen"],
        ["resumen en cuatro pasos y una evaluación separada"],
        ["escribir la evaluación dentro del resumen", "repetir el texto sin ordenarlo", "confundir tesis y razón"],
        "Pregunta: «¿en qué frase estás diciendo lo que opinas tú y en cuál lo que dice el texto?». Pídele que marque cada una con un color."),
    reinforce="Reconstruye en cuatro pasos un párrafo breve de tu libro de Filosofía o de un artículo de opinión que te hayan dado.",
    extend="Compara por escrito el supuesto del Texto A de la ficha con el supuesto del texto de imitación de la actividad y explica en qué se oponen.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (argumentos originales). Argumento 1: «Todo objeto hecho para expresar un sentimiento es arte. La canción de cumpleaños de Tomás fue hecha para expresar su cariño. Por lo tanto, la canción es arte.» "
     "Argumento 2: «El ensayo de Sara sobre la belleza no vale nada, porque ella nunca ha pintado un cuadro.» "
     "Argumento 3: «A la mayoría de los vecinos les gusta el afiche, así que el afiche es bello para todo el mundo.» "
     "Argumento 4: «Si una obra es bella, alguien la mira con placer. El cuadro del pasillo es mirado con placer por Inés. Por lo tanto, el cuadro es bello.»")
build(
    O1, 4, F,
    use="Aprenderé a formular un argumento con premisas y conclusión y a evaluarlo con criterios: si la conclusión se sigue, si las premisas son aceptables y si no cae en falacias.",
    prior=["Reconstruyo tesis y razones de un texto.", "Conozco juicio de hecho y juicio estético.", "Sé qué es una conclusión."],
    explain=[
        "Un argumento es un conjunto de afirmaciones, las premisas, que se ofrecen para apoyar otra, la conclusión. Para evaluarlo se hacen dos preguntas: ¿la conclusión se sigue de las premisas? y ¿las premisas son aceptables? Un argumento es válido cuando, si las premisas fueran verdaderas, la conclusión tendría que serlo; es sólido si además sus premisas son aceptables.",
        "Una falacia es un error de razonamiento que parece convincente. El ataque a la persona consiste en rechazar una tesis por rasgos de quien la dice y no por sus razones. La apelación a la mayoría sostiene que algo es cierto o bello solo porque a muchos les gusta. La afirmación del consecuente concluye «A» solo porque se cumple lo que «A» implicaría.",
        "En estética estos errores son frecuentes, porque se discute de gustos y hay tentación de zanjar la discusión con la fama de quien opina o con la cantidad de gente. Una buena argumentación estética describe lo que se percibe, da razones y deja abierta la posibilidad de que otra persona perciba otra cosa.",
    ],
    vocab=[("premisa", "afirmación que se ofrece como apoyo de la conclusión"), ("conclusión", "afirmación que se quiere justificar con las premisas"), ("argumento válido", "aquel cuya conclusión se sigue si las premisas son verdaderas"), ("argumento sólido", "argumento válido cuyas premisas son aceptables"), ("falacia", "error de razonamiento que parece convincente"), ("ataque a la persona", "rechazar una tesis por rasgos de quien la dice y no por sus razones"), ("apelación a la mayoría", "afirmar que algo es cierto o bello solo porque a muchos les gusta")],
    worked=[
        ("Separar premisas y conclusión", "Identifica premisas y conclusión: «Toda obra que produce una experiencia estética merece atención. Esta danza ficticia produjo una experiencia estética en el público. Por lo tanto, merece atención».",
         ["Busca la palabra «por lo tanto»: lo que viene después es la conclusión, que la danza merece atención.", "Las dos frases anteriores son las premisas que la apoyan."],
         "Premisas: toda obra que produce experiencia estética merece atención; esta danza la produjo. Conclusión: merece atención"),
        ("Detectar una falacia", "«Su teoría de la música no vale, porque él nunca aprobó un examen de piano». ¿Qué falacia es?",
         ["Mira qué se rechaza: la teoría.", "Mira por qué se rechaza: por un rasgo de la persona y no por las razones de la teoría, lo cual es un ataque a la persona."],
         "Ataque a la persona"),
    ],
    mistakes=[("Creer que si las premisas son verdaderas el argumento ya es bueno.", "Se olvida que la conclusión debe seguirse de ellas.", "Comprueba también si la conclusión se sigue de las premisas."),
              ("Descalificar un argumento diciendo «tú no sabes de arte».", "Se ataca a la persona en lugar de examinar las razones.", "Examina las premisas y la conclusión, sin referirte a quien las dice.")],
    T=[
        ("abc", "{F} En el Argumento 1, ¿cuál es la conclusión?", "La canción es arte", "Todo objeto hecho para expresar un sentimiento es arte", "La canción es de cumpleaños", "La conclusión es lo que se quiere justificar, que la canción es arte."),
        ("abc", "{F} ¿Qué falacia comete el Argumento 2?", "Ataque a la persona", "Apelación a la mayoría", "Afirmación del consecuente", "Rechaza el ensayo por algo de quien lo escribió y no por sus razones."),
        ("abc", "{F} ¿Qué falacia comete el Argumento 3?", "Apelación a la mayoría", "Ataque a la persona", "Afirmación del consecuente", "Pasa de que a muchos les gusta a que es bello para todos."),
        ("abc", "En Estética: ¿qué es una premisa?", "Una afirmación que se ofrece como apoyo de la conclusión", "La afirmación final que se quiere justificar", "Un error de razonamiento", "Las premisas apoyan la conclusión; la conclusión es lo que se quiere probar."),
        ("abc", "{F} En el Argumento 1, ¿por qué la conclusión se sigue de las premisas?", "Porque si todo objeto hecho para expresar un sentimiento es arte y la canción lo fue, la canción es arte", "Porque Tomás compuso la canción él mismo", "Porque la canción se cantó en una fiesta", "Es válido: aplica una regla general a un caso que cumple la condición."),
        ("ab", "{F} Alguien dice: «La premisa 1 del Argumento 1 es discutible: un grito de rabia expresa un sentimiento y no es arte». ¿Qué cuestiona?", "Que las premisas sean aceptables, aun siendo válido el argumento", "Que la conclusión no se siga de las premisas", "El grito muestra que la regla general es discutible, no que el argumento sea inválido."),
        ("abc", "{F} Evalúa el Argumento 4: ¿qué falla en su forma?", "Concluye que el cuadro es bello solo porque se cumple lo que la belleza implicaría, mirarlo con placer", "Usa una premisa que nadie entiende", "Apela a que muchos miran el cuadro", "Es la afirmación del consecuente: otras cosas, como un buen café, también se miran o se disfrutan con placer."),
        ("abc", "Un joven dice: «Ese crítico de cine ficticio es antipático, así que su crítica sobre esta película está equivocada». ¿Qué falacia es?", "Ataque a la persona", "Apelación a la mayoría", "Afirmación del consecuente", "Rechaza la crítica por un rasgo del crítico y no por sus razones."),
        ("abc", "¿Cuál es una mejor manera de responder a una crítica de arte con la que no estás de acuerdo?", "Examinar las razones que da y señalar cuál no te convence", "Decir que quien la escribió no sabe nada", "Contar cuánta gente piensa como tú", "Se discute con razones; las otras dos opciones son falacias."),
        ("abc", "Un grupo dice: «Hoy esa canción tiene un millón de reproducciones ficticias, así que es la mejor música». ¿Qué falla?", "Que la cantidad de reproducciones no prueba que la música sea mejor", "Que las canciones con muchas reproducciones nunca pueden ser buenas", "Que la música no se puede comparar con ninguna otra", "El éxito masivo describe popularidad, no valor estético."),
        ("abc", "{F} Se propone corregir el Argumento 3 para que no sea falaz. ¿Cuál es la mejor corrección?", "«A la mayoría de los vecinos les gusta el afiche; eso muestra que tiene un atractivo amplio, aunque no prueba que todos lo vean igual»", "«A nadie le gusta el afiche, así que es feo»", "«El afiche es bello porque lo dije yo»", "La corrección reconoce lo que muestra el dato y sus límites."),
        ("abc", "{F} Se discute si el Argumento 1 es sólido. ¿Qué habría que revisar?", "Si la premisa de que todo objeto hecho para expresar un sentimiento es arte es aceptable", "Si el argumento es válido, algo que ya está confirmado", "Si Tomás es una persona cariñosa", "Un argumento válido solo es sólido si sus premisas son aceptables."),
        ("abc", "Alguien argumenta: «Si un cuadro es caro, es bello; este cuadro es caro; entonces es bello». La conclusión se sigue de las premisas. ¿Qué conviene cuestionar?", "La primera premisa, porque el precio es un hecho de mercado y no prueba la belleza", "La conclusión, porque no se sigue de las premisas", "A la persona, porque seguramente no es experta en arte", "El precio informa sobre el mercado; no alcanza para concluir un juicio estético."),
    ],
    ctx=("abc", "En un foro del liceo, un estudiante escribe: «Sofía opina que esa obra de teatro ficticia es aburrida, pero Sofía siempre llega tarde a clases, así que no hay que hacerle caso». ¿Cuál es la mejor respuesta?", "Pedirle que examine las razones de Sofía y evitar descalificarla por algo ajeno a esas razones", "Aceptar su conclusión porque suena firme", "Decir que Sofía debe callarse", "Se responde a las razones; descalificar a la persona es un ataque a la persona."),
    sc=[
        ("En Estética: ¿qué es una falacia?", "Un error de razonamiento que parece convincente", "Puede parecer buen argumento pero no sostiene la conclusión."),
        ("¿Cuándo es sólido un argumento?", "Cuando es válido y sus premisas son aceptables", "No basta con que la conclusión se siga: las premisas deben ser aceptables."),
        ("¿Por qué la popularidad no prueba belleza?", "Porque que a muchos les guste no demuestra que sea bello para todos", "La popularidad es un dato de gusto, no una prueba del valor estético."),
    ],
    op=("Elige una de estas tesis y escribe un argumento de tres partes con dos premisas y una conclusión: (1) «Un mural en el patio mejora la experiencia estética del liceo». (2) «Una canción puede ser arte aunque no se venda». (3) «Un objeto cotidiano bien diseñado puede producir una experiencia estética». "
        "Después evalúalo: ¿la conclusión se sigue?, ¿cuál de tus premisas es la más discutible? y ¿qué falacia evitaste?",
        "Tesis 2. Premisa 1: si algo se crea para producir una experiencia estética, puede ser arte. Premisa 2: una canción compuesta para eso sigue siendo así aunque no se venda. Conclusión: una canción puede ser arte aunque no se venda. La conclusión se sigue. Premisa discutible: la 1. Evité apelar a la mayoría.",
        ["la conclusión es clara", "las premisas apoyan la conclusión", "señala la premisa más discutible", "nombra al menos una falacia evitada o posible"],
        ["argumento de dos premisas y conclusión, con evaluación"],
        ["usar premisas que repiten la conclusión", "dar como premisa la fama o la cantidad", "no señalar qué premisa es discutible"],
        "Pregunta: «si cambias la premisa 1, ¿la conclusión sigue en pie?». Pídele que subraye la premisa más débil."),
    reinforce="Busca un comentario de opinión sobre una película o canción, pásalo a premisas y conclusión y di si hay alguna falacia.",
    extend="Explica por qué un argumento puede ser válido y a la vez poco convincente. Usa un ejemplo de estética.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (definición y objeciones originales). Definición D: «Arte es todo objeto hecho por una persona para ser mirado por otras.» "
     "Objeción 1: «Un letrero de «Prohibido pasar» es un objeto hecho por una persona para ser mirado por otras, pero nadie diría que es arte.» "
     "Objeción 2: «Una pintora ficticia, Clara, dejó cuadros guardados en una caja y nunca quiso mostrarlos. ¿Dejan de ser arte por eso?» "
     "Réplica propuesta a la Objeción 1: «Agregaré que la persona debe hacerlo para provocar una experiencia estética, no solo para informar.»")
build(
    O1, 5, F,
    use="Aprenderé a responder a objeciones: reconocer un contraejemplo, decidir si una definición es demasiado amplia o estrecha, y formular una réplica que mejore la tesis sin perder su idea central.",
    prior=["Reconstruyo y evalúo argumentos.", "Conozco el problema de la demarcación del arte.", "Distingo ataque a la persona de crítica a las razones."],
    explain=[
        "Una objeción es una razón o un caso que muestra un problema en una tesis. Un contraejemplo es un caso concreto que cumple lo que dice la definición pero que, claramente, no debería caer bajo ella, o que no la cumple pero sí debería. Sirve para mostrar que una definición falla.",
        "Una definición puede ser demasiado amplia, si incluye cosas que no deberían entrar, como un letrero en una definición de arte. O puede ser demasiado estrecha, si deja afuera cosas que sí deberían entrar, como obras que nunca se mostraron. Al objetar conviene decir qué falla: si la definición incluye de más o excluye de menos.",
        "Responder a una objeción es una réplica. Se puede responder de tres maneras: aceptar la objeción y corregir la tesis, negar que el caso sea un verdadero contraejemplo, o mostrar que no afecta lo esencial. Una buena réplica no cambia de tema ni ataca a quien objeta; mejora la tesis y explica por qué.",
    ],
    vocab=[("objeción", "razón o caso que muestra un problema en una tesis"), ("contraejemplo", "caso concreto que muestra que una definición falla"), ("definición demasiado amplia", "definición que incluye cosas que no deberían entrar"), ("definición demasiado estrecha", "definición que excluye cosas que sí deberían entrar"), ("réplica", "respuesta que se da a una objeción"), ("demarcación del arte", "problema de trazar la frontera entre arte y no arte")],
    worked=[
        ("Clasificar una objeción", "Para la definición D de una ficha parecida, un joven objeta: «Un semáforo cumple D y no es arte». ¿La definición resulta demasiado amplia o demasiado estrecha?",
         ["Mira si el caso entra en la definición: sí, el semáforo cumple la condición.", "Mira si debería entrar: no. Entonces la definición incluye de más."],
         "Demasiado amplia"),
        ("Formular una réplica", "Una definición dice: «Arte es todo objeto bello». Un compañero objeta: «Un cielo estrellado es bello y no es obra de nadie». Formula una réplica que acepte la objeción y corrija la tesis.",
         ["Reconoce el punto: hay cosas bellas que no son arte.", "Corrige: «Arte es todo objeto bello hecho por una persona con intención de que se lo contemple»."],
         "Acepto la objeción y agrego que sea hecho por una persona con intención de que se lo contemple"),
    ],
    mistakes=[("Responder a una objeción repitiendo la tesis con más fuerza.", "No se examina el caso que muestra el problema.", "Analiza el caso y decide si corriges la tesis, niegas el contraejemplo o muestras que no afecta."),
              ("Cambiar tanto la tesis que ya no responde a la pregunta original.", "Se pierde la idea central al intentar evitar toda objeción.", "Corrige solo lo necesario y comprueba que la tesis sigue respondiendo a la pregunta.")],
    T=[
        ("abc", "{F} ¿Qué muestra la Objeción 1 sobre la Definición D?", "Que es demasiado amplia, porque incluye un letrero que no es arte", "Que es demasiado estrecha", "Que no se puede objetar", "Un letrero cumple D y no debería ser arte, así que D incluye de más."),
        ("abc", "{F} ¿Qué muestra la Objeción 2 sobre la Definición D?", "Que podría ser demasiado estrecha, porque excluye obras que nunca se mostraron", "Que es demasiado amplia", "Que no tiene relación con la definición", "Los cuadros guardados de Clara no cumplen D, aunque quizá sí sean arte."),
        ("En Estética: ¿cómo se llama el caso concreto que muestra que una definición falla?", "Contraejemplo", "Es el nombre del caso que cumple o incumple la definición de forma problemática."),
        ("abc", "{F} ¿Qué hace la réplica propuesta a la Objeción 1?", "Corrige la definición agregando una condición: que se haga para provocar una experiencia estética", "Niega que exista el letrero", "Ataca a quien objeta", "La réplica acepta el problema y agrega un criterio para dejar afuera los letreros."),
        ("abc", "{F} Con la réplica propuesta, ¿entra el letrero de «Prohibido pasar» en la definición corregida?", "No, porque se hizo para informar y no para provocar una experiencia estética", "Sí, porque lo mira mucha gente", "Sí, porque lo hizo una persona", "La corrección exige propósito estético, que el letrero no tiene."),
        ("ab", "{F} Un joven dice: «La Objeción 2 es un buen contraejemplo si aceptamos que Clara hizo arte». ¿Qué necesita aceptar?", "Que algo puede ser arte aunque nunca se muestre", "Que todo lo guardado en cajas es arte", "Solo si se acepta que puede ser arte sin mostrarse, la definición resulta estrecha."),
        ("abc", "Alguien define: «Arte es todo lo que expresa un sentimiento». Se objeta: «Un grito de enojo expresa un sentimiento y no es arte». ¿La definición resulta demasiado amplia o estrecha?", "Demasiado amplia", "Demasiado estrecha", "Perfecta", "El grito entra en la definición y no debería: incluye de más."),
        ("abc", "Alguien define: «Arte es solo lo que se expone en un museo». Se objeta: «Un mural ficticio en una plaza no está en un museo, pero muchos lo considerarían arte». ¿Qué falla?", "Es demasiado estrecha, porque excluye casos que parecen arte", "Es demasiado amplia", "Es perfecta", "El mural queda afuera aunque debería entrar: la definición excluye de más."),
        ("abc", "{F} Una estudiante responde a la Objeción 1: «El letrero no es un caso válido: se hizo para ser leído y obedecido, no para ser mirado». ¿Qué tipo de réplica es?", "Niega que el caso sea un verdadero contraejemplo", "Acepta la objeción y corrige la tesis", "Muestra que la objeción no afecta lo esencial", "No cambia la definición: sostiene que el letrero no cae bajo ella."),
        ("abc", "Un amigo responde a una objeción: «Tú no entiendes nada de arte». ¿Qué problema tiene su respuesta?", "Ataca a quien objeta en lugar de examinar el contraejemplo", "Es demasiado larga", "Usa una definición", "No contesta el caso planteado; ataca a la persona."),
        ("abc", "{F} Si alguien aceptara ambas objeciones, ¿qué tendría que hacer con D?", "Reformularla para dejar afuera los letreros y no exigir que las obras se muestren", "Mantenerla sin cambios", "Eliminar toda definición de arte", "Las dos objeciones señalan un exceso y una carencia; ambas deben considerarse al corregir."),
        ("abc", "{F} Al reformular D, alguien propone: «Arte es todo objeto hecho por una persona para provocar una experiencia estética». ¿Qué problema de la Objeción 2 queda resuelto?", "Que se exija que las obras sean mostradas a otras personas", "Que los letreros sean arte", "Que el arte deba ser caro", "La nueva definición ya no exige que el objeto se muestre, de modo que los cuadros guardados de Clara pueden contar."),
        ("abc", "Una definición reformulada puede recibir nuevas objeciones. ¿Qué dice eso del trabajo filosófico?", "Que definir es un proceso de ensayo y corrección con ayuda de objeciones", "Que filosofar no sirve", "Que ninguna definición es mejor que otra", "Las objeciones permiten afinar las tesis, aunque sin garantía de definiciones perfectas."),
    ],
    ctx=("abc", "En una clase ficticia, una estudiante afirma: «Una obra es arte cuando se vende». Otro objeta: «Un poema ficticio regalado a una amiga no se vendió, pero parece arte». ¿Cuál es la mejor réplica?", "Aceptar el caso y corregir: ser vendible puede ser una señal, pero no es la condición del arte", "Decir que el poema no existe", "Insistir sin mirar el caso", "El caso muestra que vender no es condición necesaria; la réplica correcta la corrige en vez de ignorarla."),
    sc=[
        ("En Estética: ¿qué es un contraejemplo?", "Un caso concreto que muestra que una definición falla", "Sirve para probar que una definición incluye de más o excluye de menos."),
        ("¿Cuándo una definición es demasiado estrecha?", "Cuando deja afuera cosas que sí deberían entrar", "Excluye casos que se esperaba incluir."),
        ("¿Qué tres tipos de réplica hay?", "Aceptar y corregir, negar que el caso sea contraejemplo, o mostrar que no afecta lo esencial", "Son las tres maneras razonadas de responder a una objeción."),
    ],
    op=("Toma esta definición: «Arte es todo objeto que produce placer al mirarlo». Escribe dos objeciones (una que muestre que es demasiado amplia y otra que sea demasiado estrecha), una réplica para cada una y una definición reformulada que las resuelva. "
        "Puedes usar estos casos de apoyo: un helado de chocolate produce placer; una obra ficticia hecha para incomodar al público produce incomodidad.",
        "Objeción amplia: un helado produce placer y no es arte. Objeción estrecha: una obra que incomoda no produciría placer y podría ser arte. Réplicas: acepto ambas. Nueva definición: arte es todo objeto hecho para provocar una experiencia estética, sea placentera o no.",
        ["propone una objeción de cada tipo", "responde a cada objeción", "reformula la definición", "la nueva definición sigue respondiendo a la pregunta original"],
        ["dos objeciones, dos réplicas y una definición reformulada"],
        ["ofrecer dos objeciones del mismo tipo", "rechazar el caso sin analizarlo", "cambiar de tema en la reformulación"],
        "Pregunta: «¿tu nueva definición deja afuera tu caso del helado y deja entrar tu obra que incomoda?». Pídele que lo compruebe."),
    reinforce="Elige otra definición de arte, por ejemplo «arte es lo que gusta a la gente», y escribe un contraejemplo y una réplica.",
    extend="Explica por qué una definición demasiado amplia y una demasiado estrecha se corrigen en direcciones opuestas.",
)

O2 = "FI-ESTE-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 6 (caso original). El municipio ficticio de Villa Alameda debe renovar su plaza y dos concejales discuten. "
     "Pía: «Hagamos una plaza simétrica y de proporciones sencillas, porque lo bello es lo que tiene orden y medida.» "
     "Raúl: «Consultemos a vecinos y a personas con mucha experiencia en arte, porque la belleza se juzga mejor con un gusto educado por la experiencia.» "
     "Cuatro cuestiones principales de la estética: (a) qué es la belleza, (b) qué es el arte, (c) cómo se juzga una obra, (d) qué valor tiene la experiencia estética.")
build(
    O2, 1, F,
    use="Aprenderé a plantear las cuestiones principales de la estética a partir de un caso, a reconocer posiciones de escuelas distintas ante ellas y a ver qué consecuencias tienen en la vida cotidiana.",
    prior=["Reconstruyo la tesis y las razones de un texto.", "Distingo juicio de hecho de juicio estético.", "Sé evaluar un argumento sencillo."],
    explain=[
        "Las cuestiones principales de la estética son preguntas que se repiten en su historia: qué es la belleza, qué es el arte, cómo se juzga una obra y qué valor tiene la experiencia estética. Cada una admite varias respuestas, y las respuestas organizadas con razones forman posiciones filosóficas.",
        "Una escuela de filosofía es un conjunto de pensadoras y pensadores que comparten tesis centrales y una manera de razonar. Evaluar posiciones de escuelas significa, primero, reconstruir sus respuestas y, después, juzgarlas con criterios como su claridad, su coherencia y la evidencia que las apoya, no por simpatía.",
        "Las posiciones estéticas tienen implicancias en la vida cotidiana: influyen en cómo se diseña una plaza, qué obras se compran para un colegio, qué se enseña en una clase de arte o cómo se decide qué merece atención. Por eso conviene preguntarse no solo qué dice una posición, sino qué haríamos si la aceptáramos.",
    ],
    vocab=[("cuestión principal de la estética", "pregunta que se repite en su historia, como qué es la belleza"), ("posición filosófica", "respuesta a una cuestión, defendida con razones"), ("escuela de filosofía", "conjunto de pensadores con tesis y modo de razonar compartidos"), ("implicancia", "consecuencia práctica de aceptar una tesis"), ("criterio de evaluación", "regla para juzgar una posición, como claridad o coherencia")],
    worked=[
        ("Ubicar la cuestión", "Una joven ficticia dice: «Un cuadro es arte si fue hecho para provocar una experiencia estética». ¿A cuál de las cuatro cuestiones responde?",
         ["Mira qué intenta definir: cuándo algo cuenta como arte.", "Esa pregunta es la cuestión (b), qué es el arte."],
         "A la cuestión (b), qué es el arte"),
        ("Derivar una implicancia", "Si un liceo ficticio acepta que «la belleza se juzga con un gusto educado», ¿qué decisión práctica tomaría para elegir un mural?",
         ["Ubica la tesis: el juicio es mejor cuando lo hacen personas con gusto educado.", "Deriva: pedirá la opinión de personas con experiencia en arte, junto con la comunidad."],
         "Consultaría a personas con experiencia en arte, además de a la comunidad"),
    ],
    mistakes=[("Creer que una posición solo vale por quien la defiende.", "Se evalúa a la persona y no sus razones.", "Evalúa la posición con criterios, sin depender de la fama de quien la sostiene."),
              ("Olvidar que una posición tiene consecuencias prácticas.", "Se discute en abstracto y no se mira qué cambiaría en la vida diaria.", "Pregunta qué haríamos, en un caso concreto, si aceptáramos esa posición.")],
    T=[
        ("abc", "{F} ¿Qué criterio propone Pía para saber qué es bello?", "El orden y la medida", "La opinión de las personas con más experiencia", "La cantidad de personas que visita la plaza", "Pía dice que lo bello es lo que tiene orden y medida."),
        ("abc", "{F} ¿En qué confía Raúl para juzgar la belleza?", "En un gusto educado por la experiencia", "En una votación entre todos los vecinos", "En la simetría de los planos", "Raúl propone consultar a personas con experiencia y gusto formado."),
        ("abc", "{F} Cuando Pía dice «lo bello es lo que tiene orden y medida», ¿a qué cuestión responde?", "A la cuestión (a), qué es la belleza", "A la cuestión (b), qué es el arte", "A la cuestión (d), qué valor tiene la experiencia", "Define en qué consiste lo bello, es decir, responde qué es la belleza."),
        ("abc", "{F} Cuando Raúl dice que la belleza se juzga mejor con gusto educado, ¿a qué cuestión responde?", "A la cuestión (c), cómo se juzga una obra", "A la cuestión (a), qué es la belleza", "A la cuestión (b), qué es el arte", "Habla de quién y cómo juzga, que es la cuestión de cómo se juzga una obra."),
        ("abc", "En Estética: ¿qué es una escuela de filosofía?", "Un conjunto de pensadores que comparten tesis centrales y un modo de razonar", "Un colegio donde se enseña Filosofía", "Un tipo de argumento sin fallas", "La palabra «escuela» designa una tradición de pensamiento, no un lugar."),
        ("ab", "¿Qué es una implicancia de una posición estética?", "Una consecuencia práctica de aceptarla", "Una prueba definitiva de que es verdadera", "Es lo que se seguiría en la práctica si se aceptara, no una prueba de su verdad."),
        ("abc", "Una profesora ficticia propone que, para juzgar un cuento, se comparen muchos cuentos y se escuche a lectores con experiencia. ¿Con cuál concejal se parece más?", "Con Raúl", "Con Pía", "Con ambos por igual", "Apela a la experiencia y al gusto formado, como Raúl."),
        ("abc", "Un diseñador ficticio defiende: «Un banco es bello si sus partes guardan proporciones sencillas y ordenadas». ¿Con cuál concejal se parece más?", "Con Pía", "Con Raúl", "Con ambos por igual", "Valora el orden y las proporciones, como Pía."),
        ("abc", "{F} Si el municipio aceptara la posición de Pía, ¿qué haría para renovar la plaza?", "Elegiría un diseño simétrico y de proporciones sencillas", "Haría una votación entre todos los vecinos sin otro criterio", "Pediría a un artista famoso que decida a su gusto", "Esa es la implicancia práctica de la posición de Pía: orden y medida."),
        ("abc", "{F} Un vecino dice: «Pía y Raúl responden exactamente lo mismo». ¿Qué corrección es mejor?", "Pía responde sobre qué es la belleza y Raúl sobre cómo se juzga; sus respuestas son distintas y podrían combinarse", "Tienen razón, porque ambos hablan de plazas", "Ambos responden solo a la cuestión (d)", "Cada concejal responde a una cuestión distinta de la ficha."),
        ("abc", "{F} Un vecino dice: «No hay manera de saber qué es lo bello, así que da lo mismo lo que decidan». ¿Qué se le puede responder?", "Que hay posiciones con razones que se pueden comparar y que sus consecuencias sí importan", "Que tiene toda la razón y nada se puede discutir", "Que lo decida el concejal de más edad", "Aunque no haya una respuesta definitiva, se pueden contrastar las razones y sus implicancias."),
        ("abc", "{F} ¿Qué evidencia ayudaría a elegir entre la posición de Pía y la de Raúl?", "Ver si las plazas con proporciones sencillas gustan también a personas con experiencia", "Saber qué concejal propuso primero su idea", "Saber cuál de los dos habla con más seguridad", "Contrastar ambas posiciones con casos concretos permite comparar su capacidad de explicar."),
        ("abc", "Dos escuelas llegan a la misma conclusión: «ese mural es bello». Una razona por proporciones y otra por consulta a expertos. ¿Por qué importa contrastar sus métodos?", "Porque cada método puede fallar en casos distintos y eso afecta cuánto confiar en la conclusión", "Porque si llegan a lo mismo no hay nada que contrastar", "Porque el método solo sirve para decidir qué conclusión es más popular", "Aunque coincidan, el modo de razonar determina en qué casos podría equivocarse."),
    ],
    ctx=("abc", "Un liceo ficticio debe elegir pinturas para sus pasillos. Una profesora propone elegir las más simétricas y ordenadas; otra, hacer una votación con estudiantes y con una pintora de la zona. ¿Qué conviene hacer antes de decidir?", "Reconocer qué criterio de belleza supone cada propuesta y qué consecuencias tendría cada una", "Elegir la propuesta de la profesora con más años de servicio", "Elegir la que a la mayoría le parezca mejor, sin pedir razones", "Las propuestas suponen posiciones estéticas distintas; evaluarlas con criterio exige ver qué implican."),
    sc=[
        ("En Estética: ¿cuáles son las cuatro cuestiones principales que vimos?", "Qué es la belleza, qué es el arte, cómo se juzga una obra y qué valor tiene la experiencia estética", "Son las preguntas que organizan las posiciones de la estética."),
        ("¿Qué es una implicancia?", "Una consecuencia práctica de aceptar una posición", "Pregunta qué cambiaría en la vida diaria si la posición fuera aceptada."),
        ("¿Por qué evaluar una posición no es lo mismo que simpatizar con quien la defiende?", "Porque se evalúa con criterios y razones, no con simpatía", "La simpatía no es evidencia a favor ni en contra."),
    ],
    op=("Elige una de estas decisiones ficticias: (1) cómo decorar una biblioteca escolar, (2) cómo elegir la música de una ceremonia, (3) qué obras mostrar en una feria de arte del barrio. "
        "Escribe qué cuestión de la estética aparece, dos posiciones posibles (con una razón cada una) y la implicancia práctica de cada una.",
        "Decisión 1. Cuestión: cómo se juzga una obra. Posición A: elegir carteles con colores ordenados, porque el orden es bello. Posición B: preguntar a lectores jóvenes, porque su gusto importa. Implicancia A: se elige por diseño; implicancia B: se hace una consulta.",
        ["identifica una cuestión de la estética", "presenta dos posiciones distintas con una razón cada una", "indica una implicancia práctica por posición", "no toma partido sin argumento"],
        ["ficha con cuestión, dos posiciones con razones y dos implicancias"],
        ["dar dos posiciones que son la misma", "no indicar razones", "describir una implicancia que no se sigue de la posición"],
        "Pregunta: «si aceptáramos la posición A, ¿qué haríamos distinto que con B?». Pídele que lo escriba con un verbo concreto."),
    reinforce="Escribe una decisión estética de tu casa o tu barrio (por ejemplo, cómo pintar una pared) y las dos posiciones que podrían guiarla.",
    extend="Explica por qué dos posiciones pueden responder a cuestiones distintas y, aun así, producir decisiones prácticas opuestas.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 7 (casos originales). Tres investigadoras ficticias quieren saber qué hace valiosa una pieza de música. "
     "Elena analiza con cuidado qué significan las palabras «armonía» y «orden» y deduce consecuencias a partir de esas definiciones: es un método conceptual. "
     "Mario entrevista a 40 oyentes de ejemplo y compara sus respuestas para ver qué tienen en común: es un método empírico. "
     "Nora describe, paso a paso y en primera persona, lo que vive mientras escucha la pieza: es un método descriptivo de la experiencia. "
     "Una escuela es un grupo de pensadores con tesis y método compartidos.")
build(
    O2, 2, F,
    use="Aprenderé a definir qué es un método de razonamiento en estética, a reconocer el método conceptual, el empírico y el descriptivo de la experiencia y a contrastar escuelas por sus métodos.",
    prior=["Conozco las cuestiones principales de la estética.", "Reconstruyo tesis y razones.", "Sé qué es una implicancia."],
    explain=[
        "Un método de razonamiento es el camino que sigue una persona para llegar a una conclusión. En estética se usan, entre otros, tres. El método conceptual analiza el significado de las palabras y deduce consecuencias. El método empírico observa casos y reacciones y busca lo que tienen en común. El método descriptivo de la experiencia relata con detalle cómo se vive algo.",
        "Cada método tiene fortalezas y límites. El conceptual da claridad, pero puede quedar lejos de los casos reales. El empírico se apoya en datos, pero lo que muchos prefieren no prueba lo que es valioso. El descriptivo muestra la riqueza de lo vivido, pero depende de lo que cada persona pueda decir de su experiencia.",
        "Contrastar métodos es preguntar cómo llegó cada escuela a su conclusión y dónde podría fallar. Dos escuelas con tesis opuestas pueden usar el mismo método, y dos con la misma tesis, métodos distintos. Por eso evaluar bien exige mirar tanto lo que se afirma como el modo de llegar a ello.",
    ],
    vocab=[("método de razonamiento", "camino que se sigue para llegar a una conclusión"), ("método conceptual", "analiza el significado de las palabras y deduce consecuencias"), ("método empírico", "observa casos y reacciones y busca lo que tienen en común"), ("método descriptivo de la experiencia", "relata con detalle cómo se vive algo"), ("contrastar", "comparar para ver semejanzas, diferencias y límites")],
    worked=[
        ("Reconocer un método", "Una estudiante ficticia pregunta a 30 compañeros de ejemplo qué murales prefieren y compara las respuestas. ¿Qué método usa?",
         ["Mira cómo obtiene su conclusión: observa preferencias de muchas personas.", "Eso corresponde al método empírico."],
         "Método empírico"),
        ("Señalar un límite", "Una escuela usa solo el método conceptual para definir belleza. ¿Qué límite puede tener?",
         ["Identifica la fortaleza: da claridad al definir.", "Identifica el límite: puede quedar lejos de los casos reales y de lo que la gente efectivamente siente."],
         "Puede quedar lejos de los casos reales"),
    ],
    mistakes=[("Creer que un método da la verdad sin límites.", "Se olvida que cada método puede fallar en ciertos casos.", "Pregunta qué casos serían difíciles para ese método."),
              ("Confundir el método con la conclusión.", "Se mezcla el camino con el lugar al que se llega.", "Distingue «cómo llegó» de «a qué llegó».")],
    T=[
        ("abc", "{F} ¿Qué método usa Elena?", "El método conceptual", "El método empírico", "El método descriptivo de la experiencia", "Elena analiza el significado de las palabras y deduce consecuencias."),
        ("abc", "{F} ¿Qué método usa Mario?", "El método empírico", "El método conceptual", "El método descriptivo de la experiencia", "Mario observa respuestas de oyentes y busca lo común."),
        ("abc", "{F} ¿Qué método usa Nora?", "El método descriptivo de la experiencia", "El método conceptual", "El método empírico", "Nora relata en primera persona lo que vive al escuchar."),
        ("En Estética: ¿cómo se llama el método que analiza el significado de las palabras y deduce consecuencias?", "Método conceptual", "Es el nombre del método que parte de definiciones y conceptos."),
        ("abc", "Un joven ficticio anota con mucho detalle lo que siente cada minuto al mirar un cuadro y lo ordena en un relato. ¿Qué método usa?", "El método descriptivo de la experiencia", "El método empírico", "El método conceptual", "Su trabajo central es relatar lo vivido en primera persona."),
        ("ab", "Una filósofa ficticia define «belleza» como «armonía de las partes» y deduce que una pieza desordenada no puede ser bella. ¿Qué método usa?", "Conceptual", "Empírico", "Parte de una definición y deduce consecuencias, lo que es propio del método conceptual."),
        ("abc", "{F} ¿Qué límite puede tener el método empírico de Mario?", "Que lo que muchos prefieren no prueba lo que es valioso", "Que no se apoya en ningún dato", "Que solo analiza definiciones", "Que muchos prefieran algo describe preferencias, no demuestra valor."),
        ("abc", "{F} ¿Qué límite puede tener el método descriptivo de Nora?", "Que depende de lo que cada persona pueda decir de su experiencia", "Que solo analiza definiciones", "Que no usa la experiencia", "El relato en primera persona queda ligado a la experiencia y a la capacidad de expresarla."),
        ("abc", "{F} Si Elena concluye que «solo es bella la música ordenada», pero un oyente ficticio vive como bella una pieza muy desordenada, ¿qué muestra ese caso?", "Que la definición de Elena podría quedar lejos de los casos reales", "Que Elena analizó mal el significado de «orden»", "Que el método conceptual no sirve para nada", "El caso real pone a prueba la conclusión deducida de una definición."),
        ("abc", "Dos escuelas ficticias concluyen que la música tradicional es valiosa. Una lo deduce de una definición; la otra, de una encuesta. ¿Qué se puede decir?", "Coinciden en la tesis, pero sus métodos son distintos y fallan en lugares distintos", "Una de las dos escuelas se equivoca necesariamente", "Usan el mismo método", "Una tesis puede alcanzarse por caminos distintos."),
        ("abc", "{F} ¿Cuál es una pregunta útil para contrastar el método de Mario con el de Elena?", "¿Qué casos quedarían mal explicados por cada método?", "¿Cuál de los dos publicó primero?", "¿Cuál de los dos tiene más seguidores?", "Preguntar por los casos difíciles revela los límites de cada método."),
        ("abc", "{F} Se dice: «Como Mario encuestó a 40 oyentes, su resultado prueba qué es la belleza». ¿Qué falla?", "Que preferencias de 40 oyentes no bastan para definir qué es la belleza", "Que Mario no tomó en cuenta lo que él mismo siente al escuchar", "Que una encuesta no puede aplicarse a la música", "Una muestra de preferencias no establece una definición de belleza."),
        ("abc", "Una escuela afirma: «Basta con describir lo que se siente: no hace falta analizar conceptos». ¿Qué podría objetársele?", "Que sin analizar conceptos es difícil comparar las descripciones de distintas personas", "Que describir lo vivido obliga a abandonar la experiencia", "Que analizar conceptos impide sentir", "Los conceptos permiten ordenar y comparar lo descrito."),
    ],
    ctx=("abc", "En un taller ficticio de la biblioteca, un grupo quiere decidir si una escultura nueva es valiosa. Una persona propone definir antes qué significa «valiosa»; otra, sondear a visitantes; otra, narrar la experiencia de ver la escultura. ¿Qué conviene?", "Combinar los tres métodos, sabiendo qué aporta y qué límite tiene cada uno", "Usar solo la definición porque es más precisa", "Usar solo la descripción porque es más sincera", "Cada método ofrece algo distinto, y reconocer sus límites mejora la decisión."),
    sc=[
        ("En Estética: ¿qué es el método empírico?", "El que observa casos y reacciones y busca lo que tienen en común", "Se apoya en observaciones y no solo en definiciones."),
        ("¿Qué caracteriza al método descriptivo de la experiencia?", "Relatar con detalle cómo se vive algo", "Ordena en palabras la experiencia en primera persona."),
        ("¿Por qué contrastar métodos mejora la evaluación de una escuela?", "Porque muestra cómo llegó a su conclusión y dónde podría fallar", "Evalúa el camino y no solo el punto de llegada."),
    ],
    op=("Elige una pregunta: (1) ¿por qué nos conmueve una canción de cuna? (2) ¿por qué nos atrae una ciudad desde un mirador? (3) ¿qué hace valiosa una pintura de paisaje? "
        "Describe cómo la abordaría una persona con cada uno de los tres métodos (conceptual, empírico y descriptivo de la experiencia), con una frase para cada uno, y un límite posible por método.",
        "Pregunta 2. Conceptual: definir qué es «amplitud» y deducir por qué atrae. Empírico: preguntar a visitantes de ejemplo qué miran primero. Descriptivo: narrar lo que siento al subir. Límites: el conceptual puede olvidar casos; el empírico, que lo común no prueba valor; el descriptivo, que es personal.",
        ["describe los tres métodos con acciones concretas", "cada método responde a la pregunta elegida", "indica un límite plausible por método", "no confunde método con conclusión"],
        ["tres frases de método y tres límites"],
        ["atribuir al mismo método dos acciones distintas", "no indicar el límite", "dar solo la conclusión"],
        "Pregunta: «¿qué haces concretamente con ese método: definir, preguntar o describir?». Pídele que subraye el verbo."),
    reinforce="Describe un caso de tu vida donde alguien juzgue algo (comida, música, ropa) y di qué método usa: conceptual, empírico o descriptivo.",
    extend="Explica por qué, si dos escuelas coinciden en una tesis, aún puede ser importante contrastar sus métodos.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 8 (resúmenes originales de dos posiciones; no son citas). Posición R (racionalista de la proporción): «Lo bello es un orden que la razón puede conocer: proporciones, simetría, armonía entre las partes. Por eso la belleza está en el objeto y se puede explicar con conceptos. Quien ve bien, ve ese orden.» "
     "Posición E (empirista del gusto): «No hay un orden de belleza que la razón pueda deducir sin mirar. Se descubre en la experiencia: con práctica, comparando muchas obras, un gusto se educa. Los mejores jueces son quienes tienen sensibilidad fina, práctica y ausencia de prejuicios, y su veredicto común sirve como patrón.» "
     "Tabla de reconstrucción: dónde está la belleza / cómo se conoce / método / implicancia cotidiana.")
build(
    O2, 3, F,
    use="Aprenderé a reconstruir y comparar dos posiciones filosóficas sobre la belleza en una tabla, indicando dónde ubica la belleza cada una, cómo se conoce, qué método usa y qué implicancias tiene.",
    prior=["Conozco los métodos conceptual y empírico.", "Reconstruyo tesis, razones y supuestos.", "Comprendo implicancia práctica."],
    explain=[
        "Comparar posiciones filosóficas exige ordenar la información con las mismas preguntas para ambas. Cuatro útiles son: dónde ubica la belleza, cómo se conoce, qué método usa y qué implicancias tiene en la vida cotidiana. Una tabla permite ver de un vistazo en qué coinciden y en qué se separan.",
        "La posición R, racionalista de la proporción, ubica la belleza en el orden del objeto y confía en la razón para conocerlo. Usa más bien un método conceptual. La posición E, empirista del gusto, sostiene que la belleza se descubre mirando y comparando muchas obras, y que un gusto bien educado sirve de patrón. Usa más bien un método empírico.",
        "Las implicancias son distintas. Quien acepta R tenderá a enseñar reglas de composición y a medir proporciones. Quien acepta E tenderá a formar el gusto con muchas experiencias y a valorar la opinión de personas con práctica. Comparar no significa elegir todavía; significa dejar claro qué dice cada posición.",
    ],
    vocab=[("racionalismo de la proporción", "posición que ve la belleza como un orden que la razón puede conocer"), ("empirismo del gusto", "posición que ve la belleza como algo que se descubre en la experiencia con un gusto educado"), ("patrón de gusto", "criterio compartido que surge del juicio de buenos jueces"), ("tabla comparativa", "cuadro que ordena dos posiciones con las mismas preguntas")],
    worked=[
        ("Llenar la fila «dónde está la belleza»", "Según la Posición R de una ficha parecida, ¿dónde está la belleza y cómo se conoce?",
         ["Busca la frase donde dice dónde está: en el orden del objeto.", "Busca la frase de cómo se conoce: con la razón."],
         "En el orden del objeto; se conoce con la razón"),
        ("Llenar la fila «implicancia»", "Si una escuela acepta la Posición E, ¿qué haría para formar el gusto de estudiantes?",
         ["Recuerda que el gusto se educa con experiencia y comparación.", "Entonces propondría que vean y comparen muchas obras con guía."],
         "Propondría ver y comparar muchas obras con orientación"),
    ],
    mistakes=[("Llenar una tabla con opiniones propias en lugar de lo que dice cada posición.", "Se mezcla reconstruir con evaluar.", "Cada celda debe poder justificarse con una frase del texto."),
              ("Presentar una posición como si fuera la caricatura de la otra.", "Se exagera para que parezca débil.", "Reconstruye cada posición en su versión más razonable.")],
    T=[
        ("abc", "{F} Según la Posición R, ¿qué tipo de explicación se puede dar de por qué algo es bello?", "Una explicación con conceptos, señalando proporciones, simetría y armonía entre las partes", "Una encuesta que muestre qué prefiere la mayoría", "Un relato de lo que cada persona siente al mirarlo", "La ficha dice que la belleza «se puede explicar con conceptos»."),
        ("abc", "{F} Según la Posición E, ¿cómo se llega a un buen juicio de belleza?", "Con un gusto educado por la práctica y la comparación de muchas obras", "Aplicando una regla de proporciones fija", "Preguntando a cualquier persona de la calle por igual", "La Posición E sostiene que el gusto se educa en la experiencia."),
        ("abc", "{F} ¿Qué método usa más bien la Posición R?", "El método conceptual", "El método empírico", "Ambos por igual", "Parte de conceptos de orden y proporción conocidos por la razón."),
        ("abc", "{F} ¿Qué método usa más bien la Posición E?", "El método empírico", "El método conceptual", "Ambos por igual", "Parte de la experiencia y la comparación de casos."),
        ("En Estética: ¿cómo se llama la posición que ve la belleza como un orden que la razón puede conocer?", "Racionalismo de la proporción", "Así llamamos aquí a la posición R, centrada en el orden de las partes."),
        ("ab", "{F} ¿Quiénes son, según la Posición E, los mejores jueces?", "Quienes tienen sensibilidad fina, práctica y ausencia de prejuicios", "Quienes han estudiado solo las reglas de proporción", "La ficha los describe por sensibilidad, práctica y falta de prejuicios, no por saber solo reglas."),
        ("abc", "{F} Una escuela ficticia decide enseñar a dibujar con reglas de proporciones y simetría. ¿Qué posición implícita tiene?", "La Posición R", "La Posición E", "Ninguna", "Cree que el orden y la proporción son lo bello y se pueden enseñar."),
        ("abc", "{F} Otra escuela ficticia organiza visitas guiadas a muchas exposiciones para que el estudiantado compare. ¿Qué posición implícita tiene?", "La Posición E", "La Posición R", "Ninguna", "Apuesta por educar el gusto con experiencia y comparación."),
        ("abc", "{F} Completa la fila «implicancia cotidiana» de la Posición R.", "Enseñar reglas de composición y medir proporciones", "Preguntar solo a la mayoría", "Evitar toda regla", "Si lo bello es un orden conocible, se pueden enseñar y aplicar reglas."),
        ("abc", "{F} Un estudiante resume: «R dice que la belleza es opinión y E que es un número». ¿Qué falla?", "Caricaturiza a ambas posiciones y no refleja lo que dicen", "Resume con fidelidad ambas posiciones", "Olvida mencionar los métodos", "Ninguna de las dos dice eso; una buena reconstrucción respeta lo que cada una afirma."),
        ("abc", "{F} ¿Qué punto en común podrían reconocer ambas posiciones?", "Que se puede razonar sobre la belleza y no solo opinar", "Que la belleza depende solo de la opinión de cada persona", "Que ninguna necesita casos para sostenerse", "Las dos ofrecen criterios para juzgar la belleza con razones."),
        ("abc", "{F} Según R, quien no percibe el orden de una obra ficticia no ve bien. ¿Cómo podría responder E?", "Que no hay un orden que se deduzca sin mirar: el patrón sale de la experiencia compartida de buenos jueces", "Que R tiene razón: sin percibir el orden no hay juicio posible", "Que la belleza es solo una opinión personal y no admite criterios", "E descarta un orden deducible sin mirar y apoya el juicio en la experiencia de buenos jueces."),
        ("abc", "{F} ¿Qué diferencia fundamental permite distinguir R de E?", "R busca la belleza en un orden conocible por la razón; E la descubre con la experiencia", "R solo estudia la música y E solo la pintura", "R niega que la belleza se pueda conocer y E lo afirma", "La diferencia está en dónde ubican y cómo conocen la belleza."),
    ],
    ctx=("abc", "Un diseñador ficticio debe escoger el color y la forma de una banca de plaza. Una colega le dice que siga reglas de proporción; otro, que pruebe prototipos con vecinas y vecinos y observe cuál prefieren. ¿Qué posiciones representan?", "La primera, la Posición R; el segundo, la Posición E", "La primera, la Posición E; el segundo, la Posición R", "Ambos representan la Posición R", "Seguir reglas de proporción es R; probar y observar preferencias con experiencia es E."),
    sc=[
        ("En Estética: ¿qué es el empirismo del gusto?", "La posición que ve la belleza como algo que se descubre en la experiencia con un gusto educado", "Acentúa la experiencia y la comparación."),
        ("¿Qué cuatro filas tiene la tabla comparativa de la clase?", "Dónde está la belleza, cómo se conoce, qué método usa y qué implicancia cotidiana tiene", "Son las mismas preguntas aplicadas a ambas posiciones."),
        ("¿Por qué no hay que caricaturizar una posición al reconstruirla?", "Porque entonces no se la evalúa en su versión razonable", "Una evaluación justa parte de la versión más razonable."),
    ],
    op=("Completa una tabla comparativa de las posiciones R y E de la ficha con las cuatro filas (dónde está la belleza, cómo se conoce, método, implicancia cotidiana) y escribe una frase que diga en qué coinciden y otra en qué se oponen.",
        "R: en el orden del objeto; con la razón; conceptual; enseñar reglas de composición. E: se descubre en la experiencia; con gusto educado; empírico; formar el gusto con muchas obras. Coinciden en que se puede razonar. Se oponen en cómo se conoce la belleza.",
        ["completa las cuatro filas para ambas posiciones", "cada celda se apoya en la ficha", "indica una coincidencia", "indica una oposición clara"],
        ["tabla de 4 filas y 2 columnas, más dos frases"],
        ["mezclar opiniones propias en la tabla", "dejar celdas vacías", "decir que no coinciden en nada"],
        "Pregunta: «¿qué frase de la ficha respalda esa celda?». Pídele que la subraye."),
    reinforce="Haz otra tabla con dos opiniones de familiares sobre qué hace bonita una casa, con las mismas cuatro filas.",
    extend="Explica por qué una persona podría aceptar parte de R y parte de E, y qué ganaría y qué perdería.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 9 (criterios y casos originales). Cinco criterios para evaluar una posición filosófica: claridad (se entiende qué sostiene), coherencia (no se contradice), apoyo en casos (se sostiene ante ejemplos), poder explicativo (explica muchos casos, incluidos los difíciles) y consecuencias aceptables (lo que implica no resulta absurdo). "
     "Caso difícil 1 para la Posición R de la clase anterior: una obra ficticia abstracta, sin simetría ni proporciones clásicas, es considerada muy bella por jueces experimentados que coinciden en su veredicto. "
     "Caso difícil 2 para la Posición E: dos grupos de jueces con experiencia y sensibilidad fina dan veredictos opuestos sobre una misma obra ficticia.")
build(
    O2, 4, F,
    use="Aprenderé a evaluar posiciones filosóficas con criterios explícitos (claridad, coherencia, apoyo en casos, poder explicativo y consecuencias) y a formular un argumento de evaluación.",
    prior=["Reconstruyo posiciones con una tabla.", "Sé qué es un argumento sólido.", "Distingo método y conclusión."],
    explain=[
        "Evaluar una posición no es decir si nos gusta. Es aplicar criterios que cualquier persona pueda revisar. Cinco criterios son: claridad, coherencia, apoyo en casos, poder explicativo y consecuencias aceptables. Una posición es mejor cuanto más cumple estos criterios, aunque ninguna los cumple perfectamente.",
        "Un caso difícil es un ejemplo que pone a prueba una posición. Si la posición no puede explicarlo sin forzarlo, pierde parte de su poder explicativo. Si logra explicarlo con un ajuste razonable, gana fuerza. Por ejemplo, una obra abstracta muy valorada es un caso difícil para quien ve la belleza solo en la simetría.",
        "Un argumento de evaluación tiene la forma: «La posición X cumple (o no cumple) el criterio Y porque Z». Debe indicar el criterio, la razón y el caso. Una evaluación honesta también reconoce lo que la posición hace bien. Evaluar no es descalificar: es mostrar con razones qué tan bien resiste una posición.",
    ],
    vocab=[("criterio de evaluación", "regla que permite juzgar una posición"), ("coherencia", "no contradecirse"), ("poder explicativo", "capacidad de explicar muchos casos, incluidos los difíciles"), ("caso difícil", "ejemplo que pone a prueba una posición"), ("argumento de evaluación", "razonamiento que muestra cómo una posición cumple o no un criterio")],
    worked=[
        ("Aplicar un criterio", "Para la Posición R, el Caso difícil 1 muestra una obra abstracta, sin proporciones clásicas, muy bella para jueces expertos. ¿Qué criterio pone a prueba?",
         ["Mira qué hace el caso: pone a prueba si la posición explica los casos difíciles.", "Ese criterio es el poder explicativo."],
         "El poder explicativo"),
        ("Redactar una evaluación", "Redacta una frase de evaluación con la forma «X cumple/no cumple el criterio Y porque Z» para la Posición E y el Caso difícil 2.",
         ["Identifica el criterio: poder explicativo y coherencia ante veredictos opuestos.", "Redacta: la Posición E no cumple del todo el criterio de poder explicativo porque no dice qué hacer cuando buenos jueces discrepan."],
         "La Posición E no cumple del todo el criterio de poder explicativo porque no explica qué hacer cuando buenos jueces discrepan"),
    ],
    mistakes=[("Evaluar una posición diciendo «no me convence» sin criterio.", "Se confunde una impresión con una evaluación.", "Nombra el criterio y la razón por la que la posición lo cumple o no."),
              ("Descartar una posición completa por un solo caso difícil.", "Se olvida que puede ajustarse.", "Evalúa también si la posición puede ajustarse de manera razonable.")],
    T=[
        ("abc", "{F} ¿Qué criterio se refiere a que una posición no se contradiga?", "Coherencia", "Claridad", "Consecuencias aceptables", "Coherencia consiste en no contradecirse a sí misma."),
        ("abc", "{F} El Caso difícil 1 es la obra abstracta muy valorada por jueces expertos. ¿Contra cuál posición está dirigido?", "Contra la Posición R", "Contra la Posición E", "Contra ambas por igual", "La obra no tiene simetría ni proporciones clásicas, algo difícil de explicar para R."),
        ("abc", "{F} El Caso difícil 2 muestra dos grupos de jueces expertos con veredictos opuestos. ¿Contra cuál posición está dirigido?", "Contra la Posición E", "Contra la Posición R", "Contra ambas por igual", "E confía en el veredicto común de los buenos jueces, que aquí no existe."),
        ("En Estética: ¿cómo se llama el ejemplo que pone a prueba una posición?", "Caso difícil", "Es el ejemplo que muestra si una posición resiste ante situaciones complicadas."),
        ("abc", "{F} Una estudiante escribe: «La Posición R no cumple el poder explicativo, porque no explica la obra abstracta». ¿Qué tiene de bueno su evaluación?", "Nombra un criterio y da una razón con un caso", "Rechaza a R por ser una posición antigua", "Repite que R es una mala posición", "Una buena evaluación indica criterio, razón y caso."),
        ("ab", "{F} Un compañero dice: «Como R tiene un caso difícil, ya no vale nada». ¿Es sólido ese razonamiento?", "No: R podría ajustarse de manera razonable para explicar ese caso", "Sí: un solo caso refuta cualquier posición para siempre", "Una posición puede ajustarse, por lo que un caso difícil no la anula por sí solo."),
        ("abc", "{F} ¿Cómo podría ajustarse R para explicar el Caso difícil 1?", "Admitiendo que hay otros órdenes distintos de la simetría clásica, como el equilibrio de color", "Negando que la obra exista", "Diciendo que los jueces se equivocan siempre", "Ampliar su noción de orden es un ajuste razonable."),
        ("abc", "{F} ¿Cómo podría ajustarse E para explicar el Caso difícil 2?", "Aclarando cuándo un grupo de jueces cuenta como competente y reconociendo que a veces no hay veredicto común", "Negando que existan jueces", "Diciendo que cualquiera juzga igual", "Precisar el patrón y reconocer sus límites mantiene la idea central."),
        ("abc", "Una posición ficticia afirma: «Es bello lo que gusta y es bello lo que no gusta». ¿Qué criterio incumple más claramente?", "La coherencia", "La claridad, porque está bien explicada", "Las consecuencias aceptables", "Afirma una cosa y su opuesta."),
        ("abc", "Una posición ficticia concluye que ninguna persona puede opinar sobre arte nunca. ¿Qué criterio incumple más claramente?", "Consecuencias aceptables", "Claridad", "Coherencia", "La consecuencia, que nadie pueda opinar, resulta difícil de aceptar."),
        ("abc", "{F} Un argumento de evaluación dice: «R es mejor que E porque tiene más seguidores». ¿Qué falla?", "Usa una razón que no es un criterio de evaluación de la posición", "Contradice la Posición R", "Pide demasiada evidencia", "El número de seguidores no es un criterio de evaluación de la posición."),
        ("abc", "{F} Evalúa: «E cumple la claridad porque explica con sencillez quiénes son los buenos jueces». ¿Qué le falta para ser completa?", "Reconocer también cómo le va con los criterios de poder explicativo y coherencia", "Quitar todas las razones", "Cambiar la conclusión sin explicar", "Una evaluación completa examina varios criterios y no solo uno."),
        ("abc", "{F} Dos estudiantes evalúan las mismas posiciones: una dice que gana R y la otra que gana E, pero ambas usan los cinco criterios y razones. ¿Qué se puede concluir?", "Que puede haber desacuerdo razonable, cuyo valor está en las razones que cada una ofrece", "Que una de las dos evaluó mal los criterios", "Que los criterios no sirven", "Con criterios compartidos, el desacuerdo puede ser fructífero."),
    ],
    ctx=("abc", "Una cooperativa ficticia debe elegir entre dos guías para formar su taller de arte: una enseña reglas de proporciones; otra, comparar muchas obras. Un socio dice: «Elijamos la que mejor resista casos difíciles y no se contradiga». ¿Qué hace?", "Propone usar criterios de evaluación en lugar de elegir por simpatía", "Propone elegir la guía más barata", "Propone elegir la que más personas conocen", "Usa coherencia y poder explicativo, criterios revisables por todos."),
    sc=[
        ("En Estética: ¿qué es un caso difícil?", "Un ejemplo que pone a prueba una posición", "Muestra si la posición resiste o debe ajustarse."),
        ("¿Cuál es la forma de un argumento de evaluación?", "La posición X cumple o no cumple el criterio Y porque Z", "Debe llevar criterio, razón y caso."),
        ("¿Por qué conviene evaluar con varios criterios y no con uno?", "Porque una posición puede ser clara pero incoherente, o explicativa pero con consecuencias difíciles", "Un solo criterio da una imagen parcial."),
    ],
    op=("Evalúa la Posición R o la Posición E de la ficha con tres de los cinco criterios. Para cada criterio escribe una frase con la forma «X cumple/no cumple el criterio Y porque Z», usando los casos difíciles de la ficha si te sirven. Termina con una frase que reconozca algo que la posición hace bien.",
        "Posición E. Claridad: cumple, porque explica en pocas palabras quiénes son buenos jueces. Poder explicativo: no cumple del todo, porque no explica qué hacer cuando buenos jueces discrepan. Coherencia: cumple, porque su idea central se mantiene. Hace bien: reconoce el papel de la experiencia.",
        ["usa tres criterios de la ficha", "cada frase tiene criterio y razón", "incluye al menos un caso difícil", "reconoce una fortaleza"],
        ["tres frases de evaluación y una de fortaleza"],
        ["decir solo «no me convence»", "usar criterios sin razón", "no reconocer ninguna fortaleza"],
        "Pregunta: «¿qué criterio de la ficha estás usando en esta frase?». Pídele que lo escriba entre paréntesis."),
    reinforce="Evalúa con dos criterios una regla de convivencia de tu curso, como si fuera una posición filosófica.",
    extend="Explica por qué dos personas que usan los mismos criterios pueden llegar a evaluaciones distintas de una posición.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 10 (evaluación y objeciones originales). Evaluación de Lía: «La Posición E es mejor que la R, porque explica por qué personas con experiencia valoran obras muy distintas de las clásicas.» "
     "Objeción 1: «Pero E no explica qué pasa cuando los jueces discrepan, y R sí da una regla.» "
     "Objeción 2: «Evaluar posiciones es un prejuicio: cada persona tiene su gusto y no hay nada que evaluar.» "
     "Réplica de Lía a la Objeción 1: «Acepto que E tiene ese límite; propongo que se exija más de un grupo de jueces antes de hablar de patrón.» "
     "Tres ámbitos de la vida cotidiana: diseño de espacios, redes sociales, enseñanza del arte.")
build(
    O2, 5, F,
    use="Aprenderé a responder objeciones a una evaluación filosófica y a mostrar las implicancias cotidianas de aceptar una posición estética, como en el diseño, las redes y la enseñanza.",
    prior=["Evalúo posiciones con criterios.", "Sé formular una réplica.", "Reconozco implicancias prácticas."],
    explain=[
        "Una evaluación filosófica también puede recibir objeciones. Hay objeciones al contenido, que cuestionan si se aplicó bien un criterio, y objeciones al sentido, que cuestionan que se evalúe. Frente a las primeras se responde revisando razones y casos. Frente a las segundas, mostrando por qué evaluar es posible y útil.",
        "Una réplica sólida reconoce la parte correcta de la objeción, explica qué parte no afecta la evaluación y, si corresponde, corrige. Responder bien no es ganar; es dejar claro hasta dónde llega la evaluación. «Cada uno tiene su gusto» no impide evaluar razones, porque se pueden comparar las razones, no los gustos.",
        "Las posiciones estéticas se notan en la vida cotidiana. En el diseño de espacios, deciden si se siguen reglas o se consulta a usuarios. En las redes sociales, influyen en cuánto pesan los «me gusta» al juzgar algo. En la enseñanza del arte, definen si se enseñan reglas o se educa el gusto con experiencias. Hacer visibles esas implicancias ayuda a decidir con más conciencia.",
    ],
    vocab=[("objeción al contenido", "cuestiona si se aplicó bien un criterio"), ("objeción al sentido", "cuestiona que tenga sentido evaluar"), ("réplica", "respuesta razonada a una objeción"), ("implicancia cotidiana", "consecuencia en la vida diaria de aceptar una posición")],
    worked=[
        ("Clasificar una objeción", "Un compañero dice: «Evaluar posiciones es imposible: todo es gusto personal». ¿Qué tipo de objeción es?",
         ["Mira si cuestiona la aplicación de un criterio: no, cuestiona que sea posible evaluar.", "Entonces es una objeción al sentido."],
         "Objeción al sentido"),
        ("Dar una réplica", "Responde a la objeción al sentido de la clase usando que se pueden comparar razones y no gustos.",
         ["Reconoce el punto: el gusto es personal.", "Responde: lo que se evalúa son las razones que se dan a favor de una posición, y esas razones se pueden comparar."],
         "El gusto es personal, pero se pueden comparar las razones"),
    ],
    mistakes=[("Responder a una objeción repitiendo la evaluación original.", "No se hace cargo del problema planteado.", "Reconoce qué parte de la objeción tiene razón y responde a esa parte."),
              ("Creer que una objeción buena obliga a abandonar toda la evaluación.", "Se olvida que se puede corregir un punto sin perder lo demás.", "Ajusta lo necesario y conserva lo que sigue en pie.")],
    T=[
        ("abc", "{F} ¿Cuál es la evaluación de Lía?", "Que la Posición E es mejor que la R porque explica obras distintas de las clásicas", "Que la Posición R es mejor", "Que la Posición E explica peor las obras clásicas", "Lía afirma que E explica mejor la diversidad de obras valoradas."),
        ("abc", "{F} ¿Qué tipo de objeción es la Objeción 1?", "Objeción al contenido", "Objeción al sentido", "Es una réplica", "Cuestiona cómo se aplicó el criterio de poder explicativo, no que se evalúe."),
        ("abc", "{F} ¿Qué tipo de objeción es la Objeción 2?", "Objeción al sentido", "Objeción al contenido", "Es una réplica", "Cuestiona que tenga sentido evaluar posiciones."),
        ("abc", "{F} ¿Qué hace la réplica de Lía a la Objeción 1?", "Acepta el límite y propone ajustar la posición", "Niega que haya un límite", "Ataca a quien objeta", "Reconoce que E tiene ese problema y sugiere un ajuste."),
        ("ab", "{F} Para responder a la Objeción 2 con un ejemplo, ¿cuál sirve más?", "Dos personas con gustos distintos comparan si sus argumentos sobre un mural son claros y se apoyan en casos", "Dos personas con gustos distintos dejan de hablar del mural", "Aunque los gustos difieran, los argumentos sí se pueden comparar con criterios."),
        ("abc", "Una diseñadora ficticia basa su trabajo en reglas de proporción. Otra consulta a usuarios. ¿En qué ámbito de la ficha se nota la diferencia?", "En el diseño de espacios", "En las redes sociales", "En la enseñanza del arte", "Es una decisión de diseño de espacios."),
        ("abc", "Un grupo de estudiantes ficticio decide qué fotos son buenas solo contando «me gusta». ¿Con cuál posición se parece más?", "Con una versión de E que confunde preferencia masiva con gusto educado", "Con la Posición R", "Con ambas por igual", "Toma el parecer de muchos como patrón, sin exigir competencia de los jueces."),
        ("abc", "{F} Un profesor ficticio de arte decide que sus estudiantes copien proporciones de modelos clásicos durante todo el año. ¿Qué posición parece guiar su enseñanza?", "La Posición R", "La Posición E", "Ambas por igual", "Cree que el orden y la proporción son lo central y se pueden enseñar."),
        ("abc", "{F} Una profesora ficticia organiza visitas a muchas exposiciones para que el estudiantado compare. ¿Qué implicancia cotidiana tiene su posición?", "Educar el gusto con experiencias diversas", "Enseñar solo reglas fijas", "Decidir por votación de seguidores", "Se corresponde con la Posición E."),
        ("abc", "{F} Un amigo dice: «La objeción 1 es tan buena que la evaluación de Lía ya no vale nada». ¿Qué responder?", "Que la evaluación podía ajustarse y que Lía lo hace en su réplica", "Que la objeción no dice nada sobre la Posición E", "Que Lía no debió evaluar", "Un límite señalado puede corregirse sin abandonar toda la evaluación."),
        ("abc", "{F} Una réplica a la Objeción 1 dice: «R da una regla, pero la regla falla con la obra abstracta del Caso difícil 1». ¿Qué hace esta réplica?", "Responde mostrando que la ventaja de R tiene su propio límite", "Ignora la objeción", "Acepta la objeción sin más", "Contesta que la regla de R no es una ventaja sin costo."),
        ("abc", "Alguien dice: «Si aceptamos que una canción es buena porque la mayoría la escucha, entonces las canciones poco conocidas valen menos». ¿Qué implicancia cotidiana señala?", "Que el éxito pasa a ser criterio del valor, con consecuencias para lo poco conocido", "Que lo popular siempre es peor", "Que el éxito mide la calidad de forma exacta", "Muestra una consecuencia práctica de tomar la popularidad como criterio."),
        ("abc", "{F} Evalúa: «Aceptar R o E no cambia nada en la vida cotidiana». ¿Cuál es la mejor objeción?", "Cambia cómo se diseñan espacios, cómo se juzgan publicaciones y cómo se enseña arte", "Tienes razón, porque ambas posiciones llevan a lo mismo", "Solo cambia la decoración de los locales", "Las tres áreas de la ficha muestran decisiones distintas según la posición."),
    ],
    ctx=("abc", "En un centro cultural ficticio, un concurso de afiches se decidirá por el número de «me gusta». Una socia objeta que eso confunde popularidad con valor estético. Otro responde que eso es opinar sin criterio. ¿Qué respuesta aporta más?", "Proponer criterios explícitos, como claridad y apoyo en casos, y combinarlos con la votación", "Eliminar el concurso", "Contar solo los «me gusta»", "Los criterios hacen revisable la decisión y reconocen el valor de la participación."),
    sc=[
        ("En Estética: ¿qué es una objeción al sentido?", "La que cuestiona que tenga sentido evaluar", "Se responde mostrando que las razones sí se pueden comparar."),
        ("¿Qué debe hacer una réplica sólida?", "Reconocer la parte correcta de la objeción y explicar qué parte no afecta la evaluación", "No busca ganar sino precisar hasta dónde llega la evaluación."),
        ("¿Cuáles son tres ámbitos cotidianos donde se notan las posiciones estéticas?", "Diseño de espacios, redes sociales y enseñanza del arte", "Son los tres ámbitos de la ficha."),
    ],
    op=("Elige un ámbito cotidiano (diseño de espacios, redes sociales o enseñanza del arte). Describe un caso breve, indica qué posición (R o E) guía la decisión y qué implicaría para esa decisión. "
        "Luego escribe una objeción posible a tu evaluación de esa posición y una réplica que reconozca algo de la objeción.",
        "Redes sociales. Caso: un colectivo juzga fotos solo por «me gusta». Posición: se parece a E, pero sin exigir jueces competentes. Implicancia: lo popular desplaza a lo poco conocido. Objeción: los «me gusta» sí reflejan gusto compartido. Réplica: reflejan preferencia, no necesariamente gusto educado.",
        ["describe un caso breve y concreto", "asocia el caso con una posición", "indica una implicancia", "formula una objeción y una réplica que reconoce algo de ella"],
        ["caso, posición, implicancia, objeción y réplica"],
        ["describir un caso sin relación con la posición", "responder la objeción repitiendo lo anterior", "ignorar la parte correcta de la objeción"],
        "Pregunta: «¿qué parte de la objeción reconoces como cierta?». Pídele que la escriba antes de la réplica."),
    reinforce="Busca en tu vida diaria una decisión sobre belleza, como elegir una foto de perfil, y di qué posición parece guiarla.",
    extend="Explica por qué «hay que respetar todos los gustos» es compatible con evaluar las razones que se dan a favor de una posición.",
)

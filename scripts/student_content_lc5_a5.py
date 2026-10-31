"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 17 (manifestaciones artísticas y cosmovisión indígena).

Los poemas, cantos, danzas y obras de teatro de este módulo son textos ORIGINALES del autor del cuaderno,
atribuidos a comunidades y artistas INVENTADOS. No se reproduce ninguna obra real ni se describe ninguna danza,
canto o ceremonia de un pueblo real: eso lo enseñan la comunidad y el educador/a tradicional. Los movimientos
propuestos son simples y seguros (sin giros, saltos, volteos ni desplazamientos de espaldas).
"""
from __future__ import annotations

from student_content_lc5_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA17 = "LC05 OA 17"

POEMA = ("Poema inventado de doña Inés, de Río Hondo: «El río me habla de noche, / y yo escucho sin hablar. / Lleva en su agua mi nombre / hasta el lago grande y quieto. // "
         "Mi abuela teje la lana / como el río teje el camino; / entre hilos y corriente / aprendo de dónde vengo.»")
CANTO = ("Canto de la siembra, inventado en Ladera Verde: «Baja el agua, baja el agua, / despierta la semilla. / Sube el sol, sube el sol, / crece la huerta chiquita.»")

L(
    OA17, 1, materials=MAT + " Los poemas, cantos y obras de teatro de este cuaderno son textos originales e inventados.",
    use="Aprenderé a situar una manifestación artística de una comunidad: qué es, quién la crea, con qué permiso y qué comunica sobre su visión de mundo. Sirve para valorar el arte indígena como medio para mantener viva una cultura.",
    prior=["Sé situar una fuente con su ficha.", "Sé que la cosmovisión es la manera en que un pueblo entiende el mundo."],
    explain=[
        "Una manifestación artística es una forma de expresión que usa el cuerpo, la voz, las palabras o los objetos para comunicar algo. Algunas son la danza, el baile, la poesía, el canto y el teatro. Los pueblos indígenas tienen sus propias manifestaciones artísticas, tradicionales y actuales, y las usan para contar su historia y su manera de ver el mundo.",
        "La cosmovisión es la manera en que un pueblo entiende el mundo, la naturaleza y la vida. El arte la comunica: un canto puede hablar del agua, un poema del río, una obra de teatro de la historia de la comunidad. Así, el arte ayuda a mantener viva la cultura, porque pasa de una generación a otra.",
        "Para situar una manifestación artística preguntamos: ¿cuál es?, ¿quién la crea o la enseña?, ¿de qué comunidad?, ¿tiene permiso para compartirse?, ¿qué comunica? y ¿qué parte no se comparte? Las obras de este cuaderno son inventadas. Las manifestaciones de un pueblo real las enseñan sus artistas, su comunidad y su educador o educadora tradicional.",
    ],
    vocab=[("manifestación artística", "forma de expresión con el cuerpo, la voz, las palabras o los objetos"), ("cosmovisión", "manera en que un pueblo entiende el mundo y la vida"), ("tradicional", "que viene de generaciones anteriores"), ("actual", "que se crea o practica hoy"), ("expresarse", "comunicar lo que se piensa o siente")],
    worked=[
        W("Clasificar manifestaciones", "Clasifica: a) un canto sobre la siembra b) una obra donde personas actúan la historia de su comunidad.", ["El canto usa la voz.", "La obra usa personas actuando: es teatro.", "Son manifestaciones distintas."], "a es canto; b es teatro."),
        W("Situar una obra", CANTO + " ¿Qué comunica sobre la visión de mundo?", ["Habla del agua, del sol y de la semilla.", "Relaciona la naturaleza con el crecimiento de la huerta.", "Es mi interpretación, marcada como tal."], "Según el canto inventado, el agua y el sol hacen despertar y crecer la semilla. Yo pienso que comunica que la naturaleza y el trabajo humano se necesitan."),
    ],
    mistakes=[
        M("Pensar que el arte indígena es solo del pasado.", "Los pueblos también crean arte actual.", "Incluye manifestaciones tradicionales y actuales."),
        M("Copiar un canto o una danza de un pueblo real sin permiso.", "Es apropiarse de una obra ajena.", "Pide autorización y aprende con el educador tradicional."),
    ],
    R=[
        ex("Canto inventado: «Baja el agua, baja el agua, despierta la semilla». ¿Qué despierta?", "La semilla", "El verso lo dice."),
        ex("¿Qué manifestación artística usa la voz? A) el canto B) la pintura", "A", "Cantar usa la voz."),
        ex("¿Se puede copiar el canto de un pueblo real sin permiso? Responde Sí o No.", "No", "Hace falta autorización."),
    ],
    C=[
        ex("Verdadero o falso: una manifestación artística puede comunicar la cosmovisión de un pueblo.", "Verdadero", "Es una de sus funciones."),
        ex("¿Qué es la cosmovisión? A) la manera en que un pueblo entiende el mundo y la vida B) un instrumento musical", "A", "Es la definición de la clase."),
        ex("Verdadero o falso: el arte indígena existe solo en el pasado.", "Falso", "También hay arte actual."),
    ],
    A=[
        ex("Clasifica en DANZA, POESÍA o TEATRO: a) un texto en versos sobre un río b) un grupo que representa una historia con personajes.", "a poesía, b teatro", "Los versos son poesía; representar personajes es teatro."),
        ex("Una ficha trae el nombre del canto y de la comunidad, pero no dice si hay permiso. ¿Puedes usarla? Responde Sí o No.", "No", "Falta el permiso."),
        ex("Clasifica en TRADICIONAL o ACTUAL: a) un canto que los abuelos enseñaron a los nietos b) un grupo joven que cuenta la historia de su comunidad en una canción nueva.", "a tradicional, b actual", "La primera viene de generaciones; la segunda se crea hoy."),
    ],
    Z=[
        ex("Mauricio dice: «Un canto no sirve para conocer una cultura, solo para entretener». ¿Qué error comete?", "No ve que el arte comunica la cosmovisión", "El arte transmite la manera de ver el mundo."),
        ex("¿Por qué el arte ayuda a mantener viva una cultura? A) porque pasa de una generación a otra B) porque es caro", "A", "Se transmite y se renueva."),
    ],
    D=[
        ex("Dos fichas inventadas: un canto de la siembra (Ladera Verde) y un poema del río (Río Hondo). Alguien escribe «el agua lleva mi nombre». ¿De cuál viene el verso?", "Del poema del río", "El poema de doña Inés tiene ese verso."),
        ex("Quieres incluir en tu trabajo una danza de un pueblo real que viste en un video. ¿Qué haces? A) pido a la comunidad o al educador autorización y explicación B) la copio", "A", "La danza de un pueblo real la enseña su comunidad."),
    ],
    context=[ex("Tu escuela prepara una muestra artística. Alguien quiere imitar una danza de un pueblo real para el acto. ¿Qué es mejor? A) invitar a quienes la practican o al educador tradicional B) imitarla", "A", "Se aprende con sus portadores.")],
    selfcheck=[
        ex("Nombra tres manifestaciones artísticas.", "Tres entre: danza, baile, poesía, canto, teatro", "Están en la explicación."),
        ex("Verdadero o falso: el arte puede mantener viva una cultura.", "Verdadero", "Transmite la cosmovisión."),
        ex("¿Quién enseña las manifestaciones de un pueblo real? A) su comunidad y su educador tradicional B) cualquiera", "A", "Ellos son la fuente."),
    ],
    task=T("Lee: «Poema inventado de doña Inés, de Río Hondo: «El río me habla de noche, y yo escucho sin hablar»». Haz una ficha con: manifestación artística, comunidad, autora, qué parece comunicar sobre la naturaleza (con «yo pienso que…»), si es tradicional o actual (según la ficha: no lo dice) y qué no sabes. Escribe una pregunta para el educador tradicional sobre el arte de tu zona.",
           "Manifestación: poesía. Comunidad: Río Hondo. Autora: doña Inés. Yo pienso que comunica que el río es parte de su vida y que ella lo escucha con respeto. Tradicional o actual: la ficha no lo dice. No sé qué otros poemas hay. Pregunta: ¿qué cantos o poemas de nuestra zona se pueden compartir en la escuela?",
           ["completa la ficha", "marca su interpretación", "reconoce lo que la ficha no dice"], ["ficha de seis campos", "pregunta"], ["inventar datos de la autora", "decir que es del pasado sin fuente"],
           "Pedir que muestre la frase del poema que apoya su interpretación."),
    reinforce="Dibuja el río del poema y escribe debajo el verso que más te llamó la atención.",
    extend="Escribe dos manifestaciones artísticas de tu barrio y si son tradicionales o actuales.",
)

L(
    OA17, 2, materials=MAT,
    use="Aprenderé a leer un poema o un canto con límites: qué dice, qué imágenes usa y qué no sé de su significado. Sirve para apreciar el arte de otras comunidades sin inventar lo que significa.",
    prior=["Sé situar una manifestación artística.", "Sé separar fuente e interpretación."],
    explain=[
        "Un poema se organiza en versos, que son cada línea, y en estrofas, que son grupos de versos. Por ejemplo, un poema de dos estrofas de cuatro versos tiene ocho versos. Para leerlo con atención buscamos las imágenes, es decir, las palabras que nos hacen ver o sentir algo, como «el río teje el camino».",
        "Cuando una autora o una comunidad no explica el significado de su obra, no lo inventamos. Escribimos lo que dice el poema, lo que yo imagino con «yo pienso que» y lo que no sé. Hay obras con partes que no se comparten y se respetan igual que en un relato.",
        "Un canto o un poema de una comunidad real se lee o se canta con permiso y se aprende de quien lo enseña. No lo cambiamos, no lo mezclamos con otro y no decimos que su sentido es uno solo. El educador o educadora tradicional puede decirnos qué se puede compartir.",
    ],
    vocab=[("verso", "cada línea de un poema"), ("estrofa", "grupo de versos"), ("imagen poética", "palabras que hacen ver o sentir algo"), ("significado", "lo que quiere decir una obra"), ("interpretar", "dar una idea propia sobre una obra")],
    worked=[
        W("Contar versos y estrofas", POEMA + " ¿Cuántas estrofas y cuántos versos tiene?", ["La primera estrofa tiene 4 versos.", "La segunda estrofa tiene 4 versos.", "En total 8 versos."], "2 estrofas y 8 versos."),
        W("Separar tres cosas", "En el verso «Mi abuela teje la lana / como el río teje el camino» separa lo que dice, lo que imagino y lo que no sé.", ["Dice: la abuela teje lana y el río teje el camino.", "Imagino: yo pienso que une el tejido con el río.", "No sé: qué significa el tejido para su comunidad."], "Dice que teje la lana; imagino que une tejido y río; no sé qué significa el tejido para su comunidad."),
    ],
    mistakes=[
        M("Decir que el poema «quiere decir» solo una cosa.", "Una obra puede tener varias lecturas.", "Marca tu idea con «yo pienso que»."),
        M("Cambiar versos de un canto de una comunidad.", "Se modifica su obra.", "Cántalo como lo enseña quien lo comparte."),
    ],
    R=[
        ex("Poema inventado: «El río me habla de noche, / y yo escucho sin hablar». ¿Cuántos versos hay en estas dos líneas?", "2", "Cada línea es un verso."),
        ex("Un poema tiene dos estrofas de cuatro versos cada una. ¿Cuántos versos tiene en total? Responde con un número.", "8", "2 × 4 = 8."),
        ex("¿Qué es un verso? A) cada línea de un poema B) un grupo de versos", "A", "El grupo de versos es la estrofa."),
    ],
    C=[
        ex("Verdadero o falso: una estrofa es un grupo de versos.", "Verdadero", "Es la definición de la clase."),
        ex("¿Qué es una imagen poética? A) palabras que hacen ver o sentir algo B) un dibujo", "A", "Despiertan una imagen en la mente."),
        ex("Verdadero o falso: puedo cambiar los versos de un canto de una comunidad.", "Falso", "Se modificaría su obra."),
    ],
    A=[
        ex("Poema inventado: «Lleva en su agua mi nombre / hasta el lago grande y quieto». ¿Qué lleva el agua?", "Mi nombre", "El verso lo dice."),
        ex("Clasifica en DICE EL POEMA o YO PIENSO QUE: a) «Mi abuela teje la lana» b) el tejido recuerda a la familia.", "a dice el poema, b yo pienso que", "La primera está escrita; la segunda es una idea mía."),
        arith("Una canción inventada tiene 3 estrofas de 4 versos cada una. ¿Cuántos versos tiene en total?", "3*4", "Se repite 4 versos tres veces."),
    ],
    Z=[
        ex("Lorena dice: «El poema de Río Hondo significa que la gente es triste». ¿Qué error comete?", "Afirma un significado que el poema no dice", "El poema no habla de tristeza."),
        ex("¿Por qué conviene marcar «yo pienso que» en una interpretación? A) porque otras personas pueden leerlo distinto B) porque es más largo", "A", "Una obra admite varias lecturas."),
    ],
    D=[
        ex("Dos lecturas del verso «entre hilos y corriente aprendo de dónde vengo». 1) «Yo pienso que habla de aprender de la familia y del río». 2) «Significa exactamente que el río es sagrado». ¿Cuál es adecuada?", "La primera", "La segunda afirma algo que el poema no dice."),
        ex("Una comunidad dice que una parte de su canto no se comparte. ¿Qué escribes en tu trabajo? A) esa parte no se comparte B) una estrofa inventada", "A", "Se respeta lo que la comunidad decidió."),
    ],
    context=[ex("En el taller de poesía de la escuela, una compañera quiere cambiar dos versos del poema de doña Inés para que rimen. ¿Qué es mejor? A) respetar el poema y escribir uno propio B) cambiarlo", "A", "No se cambia la obra de otra persona.")],
    selfcheck=[
        ex("Explica con tus palabras qué es una estrofa.", "Un grupo de versos", "Es la definición de la clase."),
        ex("Verdadero o falso: una obra puede tener varias lecturas.", "Verdadero", "Por eso se marca la interpretación."),
        ex("¿Qué haces con las partes que una comunidad no comparte? A) las respeto B) las invento", "A", "Lo reservado se respeta."),
    ],
    task=T("Lee este canto inventado de Ladera Verde: «Baja el agua, baja el agua, / despierta la semilla. / Sube el sol, sube el sol, / crece la huerta chiquita.» Responde: ¿cuántos versos tiene?, ¿cuáles son las dos imágenes que más te gustan?, ¿qué crees que comunica (con «yo pienso que…»)? y ¿qué no sabes de su significado? No cambies ni agregues versos.",
           "Tiene 4 versos. Imágenes: «despierta la semilla» y «crece la huerta chiquita». Yo pienso que comunica que el agua y el sol ayudan a crecer a la huerta. No sé cuándo se canta ni qué significa para la comunidad.",
           ["cuenta bien los versos", "elige imágenes del canto", "marca su interpretación y un límite"], ["respuestas de cuatro preguntas"], ["cambiar los versos", "inventar cuándo se canta"],
           "Pedir que muestre en el canto cada respuesta."),
    reinforce="Subraya en el poema de doña Inés las dos imágenes que más te gusten.",
    extend="Escribe tu propia interpretación de un verso del poema y márcala con «yo pienso que».",
)

L(
    OA17, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre una manifestación artística, la cosmovisión y el territorio, y entre lo tradicional y lo actual. Sirve para valorar el arte como medio de comunicar la visión de mundo.",
    prior=["Sé leer un poema o canto con límites.", "Sé que la cosmovisión es la manera en que un pueblo entiende el mundo."],
    explain=[
        "El arte indígena se relaciona con tres cosas. Con el territorio: nombra ríos, cerros, mares o animales. Con la cosmovisión: muestra cómo se relacionan las personas, la naturaleza y la comunidad. Y con el tiempo: lo tradicional se transmite de generación en generación, y lo actual lo renueva con nuevas formas.",
        "Por ejemplo, el canto inventado de Ladera Verde nombra el agua, el sol y la semilla, y el poema de Río Hondo nombra el río y el lago. Un grupo joven inventado de Isla Niebla cuenta en una canción actual la historia de su comunidad. Todos muestran formas de comunicar la visión de mundo.",
        "Lo actual no es menos válido que lo tradicional, ni lo tradicional es solo del pasado. Un artista puede usar un instrumento nuevo y seguir contando lo que su comunidad cuida. Las relaciones se anotan con la fuente, y las ideas propias se marcan con «puedo pensar que».",
    ],
    vocab=[("tradición", "costumbre que pasa de generación en generación"), ("renovar", "dar forma nueva a algo antiguo"), ("territorio", "lugar donde vive la comunidad"), ("cosmovisión", "manera de entender el mundo"), ("canción actual", "canción creada hoy")],
    worked=[
        W("Relacionar una obra con el territorio", POEMA + " ¿Qué elementos del territorio aparecen?", ["Aparecen el río y el lago.", "También el tejido de la lana.", "Son elementos del territorio de Río Hondo."], "El río, el lago y la lana tejida."),
        W("Tradicional y actual", "Un grupo joven inventado de Isla Niebla canta la historia de su comunidad en una canción nueva. ¿Es menos válido que un canto antiguo?", ["Es una forma actual.", "Sigue comunicando la historia de la comunidad.", "Tiene el mismo valor."], "No: tiene el mismo valor; es una forma actual de comunicar."),
    ],
    mistakes=[
        M("Pensar que el arte indígena actual no es auténtico.", "Los pueblos crean y renuevan su arte hoy.", "Valora las formas tradicionales y actuales."),
        M("Decir que una obra muestra la cosmovisión de todo un pueblo.", "Una obra muestra una mirada de su autor o autora.", "Escribe «en esta obra, según la fuente…»."),
    ],
    R=[
        ex("Poema inventado: «Lleva en su agua mi nombre / hasta el lago grande y quieto». ¿Qué lugar del territorio se nombra? A) el lago B) la montaña", "A", "El verso lo dice."),
        ex("Canto inventado: «Baja el agua, baja el agua». ¿Qué elemento de la naturaleza aparece?", "El agua", "El verso lo dice."),
        ex("Un grupo joven canta la historia de su comunidad en una canción nueva. ¿Es tradicional o actual?", "Actual", "Se crea hoy."),
    ],
    C=[
        ex("Verdadero o falso: el arte actual de un pueblo tiene menos valor que el tradicional.", "Falso", "Ambos tienen valor."),
        ex("Verdadero o falso: una obra puede nombrar lugares del territorio y comunicar la cosmovisión.", "Verdadero", "Es una de sus funciones."),
        ex("¿Qué es renovar una tradición? A) darle forma nueva sin perder su sentido B) olvidarla", "A", "Así la tradición continúa viva."),
    ],
    A=[
        ex("Une: 1) el río y el lago del poema 2) un grupo joven que canta a su comunidad con sus propios instrumentos a) territorio b) arte actual", "1-a, 2-b", "El primero nombra lugares; el segundo es una forma nueva."),
        ex("Clasifica en TERRITORIO o COSMOVISIÓN: a) el poema nombra el río b) el poema relaciona el tejido de la abuela con el río, según doña Inés.", "a territorio, b cosmovisión", "La primera nombra un lugar; la segunda muestra una relación entre vida, familia y naturaleza."),
        ex("Una niña dice que la obra de doña Inés «muestra cómo piensa todo su pueblo». ¿Qué corriges? A) muestra su mirada, no la de todo su pueblo B) tiene razón", "A", "Una obra no representa a todos."),
    ],
    Z=[
        ex("Pedro dice: «Si usan instrumentos nuevos, ya no es cultura indígena». ¿Qué error comete?", "Cree que la cultura no cambia", "Las culturas se renuevan."),
        ex("¿Por qué conviene nombrar quién creó una obra? A) para reconocer su autoría B) para ocupar espacio", "A", "Reconoce a la persona o comunidad."),
    ],
    D=[
        ex("Dos obras inventadas: un canto antiguo de la siembra (Ladera Verde) y una canción nueva sobre la caleta (Isla Niebla). Alguien dice que son «iguales». ¿Qué respondes? A) son distintas pero ambas comunican la visión de su comunidad B) son exactamente iguales", "A", "Cambian la forma y el territorio."),
        ex("Quieres usar la melodía de un canto de un pueblo real en tu trabajo. ¿Qué haces? A) pido permiso y explicación a la comunidad B) la uso", "A", "El canto pertenece a su comunidad."),
    ],
    context=[ex("Tu curso hace un mural sobre el río. Una compañera sugiere usar versos del poema de doña Inés (inventada). ¿Qué es lo correcto? A) citar y nombrar a la autora B) decir que son tuyos", "A", "Se reconoce la autoría.")],
    selfcheck=[
        ex("Nombra las tres cosas con que se relaciona el arte.", "El territorio, la cosmovisión y el tiempo", "Están en la explicación."),
        ex("Verdadero o falso: lo actual y lo tradicional son válidos.", "Verdadero", "Ambos comunican la cosmovisión."),
        ex("¿Qué haces con una idea tuya sobre una obra? A) la marco con «puedo pensar que» B) la presento como de la autora", "A", "Así no se atribuye."),
    ],
    task=T("Lee dos obras inventadas. Canto de Ladera Verde: «Baja el agua, baja el agua, despierta la semilla». Canción actual de un grupo joven de Isla Niebla: «Salimos con el bote al amanecer, la caleta nos espera». Haz una tabla con tres criterios: qué lugar o elemento del territorio aparece, qué cosmovisión puedo pensar que comunica (con «puedo pensar que…») y si es tradicional o actual. Escribe una semejanza y una diferencia.",
           "Canto: el agua y la semilla; puedo pensar que comunica que la naturaleza ayuda a crecer; tradicional o actual: la ficha no lo dice. Canción: el bote y la caleta; puedo pensar que comunica el trabajo de la pesca; actual. Semejanza: ambas hablan del territorio. Diferencia: una trata de la siembra y la otra de la pesca.",
           ["completa la tabla", "marca interpretaciones", "no jerarquiza"], ["tabla de tres criterios", "dos frases"], ["decir cuál es más auténtica", "inventar datos"],
           "Pedir que indique la frase de cada obra que usó."),
    reinforce="Une con flechas cada obra con el lugar del territorio que nombra.",
    extend="Escribe una pregunta para el educador tradicional sobre el arte que se practica hoy en tu zona.",
)

L(
    OA17, 4, materials=MAT + " Las propuestas de movimiento son simples: sin giros, saltos ni desplazamientos de espaldas, y con espacio libre.",
    use="Aprenderé a expresarme con una manifestación artística propia (poesía, canto, teatro o movimiento) inspirada en lo que aprendí, atribuyendo la inspiración y sin copiar obras ajenas. Sirve para comunicar lo que valoro y mantener viva la cultura.",
    prior=["Sé leer obras con límites y relacionarlas con el territorio.", "Sé reconocer y atribuir fuentes."],
    explain=[
        "Expresarse es comunicar lo que pensamos y sentimos. Puedes hacerlo con un poema, un canto, una escena de teatro o una secuencia de movimientos. Para hacerlo con respeto, tu obra debe ser tuya y puede estar inspirada en lo que aprendiste, pero no debe copiar una obra ajena ni imitar una ceremonia o danza de un pueblo real.",
        "Tu obra tiene cuatro partes: qué quieres comunicar, qué forma elegiste, de qué te inspiraste (con la fuente) y qué límites respetaste. Por ejemplo, un poema propio sobre el agua puede decir «inspirado en el poema inventado de doña Inés». Así reconoces la fuente y no te apropias.",
        "Si eliges movimiento, usa pasos simples y seguros, con espacio libre y sin giros, saltos ni desplazamientos de espaldas. Si eliges teatro, representa una escena inventada y no una ceremonia real. Al final, muestras tu obra a tu curso y al educador tradicional, que puede sugerir cambios.",
    ],
    vocab=[("inspirarse", "tomar una idea de otra obra para crear algo propio"), ("copiar", "repetir una obra ajena como si fuera propia"), ("escena", "parte breve de una obra de teatro"), ("secuencia", "serie de movimientos en orden"), ("autoría", "reconocimiento de quién creó algo")],
    worked=[
        W("Escribir un poema propio inspirado", "Escribe dos versos propios inspirados en el poema de doña Inés, sin copiarlo.", ["Elijo un tema: el agua.", "Escribo mis propios versos.", "Anoto la inspiración."], "«El agua canta bajito / cuando pasa por mi calle». Inspirado en el poema inventado de doña Inés, de Río Hondo."),
        W("Revisar la seguridad de un movimiento", "Una secuencia dice: «Girar rápido cuatro veces y caminar de espaldas». ¿Es segura?", ["Girar rápido puede marear.", "Caminar de espaldas puede causar caídas.", "No es segura."], "No es segura; debe cambiarse por pasos simples hacia adelante o al costado."),
    ],
    mistakes=[
        M("Copiar un poema o canto ajeno y presentarlo como propio.", "Es apropiarse de la obra de otra persona.", "Crea tu obra y anota la inspiración."),
        M("Imitar una ceremonia o danza de un pueblo real como actuación.", "Puede faltar al respeto a lo sagrado.", "Usa una escena inventada y movimientos simples."),
    ],
    R=[
        ex("¿Cuántas partes tiene tu obra según esta clase? Escribe el número.", "4", "Qué comunicar, forma, inspiración y límites."),
        ex("¿Qué debes anotar si tu obra se inspira en otra? A) la fuente de inspiración B) nada", "A", "Reconoce la autoría."),
        ex("¿Puedes imitar una ceremonia de un pueblo real en tu obra? Responde Sí o No.", "No", "Puede faltar al respeto."),
    ],
    C=[
        ex("Verdadero o falso: inspirarse en una obra es lo mismo que copiarla.", "Falso", "Inspirarse es crear algo propio."),
        ex("Verdadero o falso: un movimiento seguro evita giros, saltos y desplazarse de espaldas.", "Verdadero", "Reduce el riesgo de caídas."),
        ex("¿Qué elegirías para representar con teatro? A) una escena inventada B) una ceremonia real", "A", "No se imita lo sagrado."),
    ],
    A=[
        ex("Clasifica en PROPIA E INSPIRADA o COPIA: a) «El agua canta bajito / cuando pasa por mi calle», inspirada en el poema de doña Inés b) el poema de doña Inés escrito con otro nombre.", "a propia e inspirada, b copia", "La primera es nueva; la segunda repite la obra de otra persona."),
        ex("¿Cuál secuencia de movimientos es segura? A) tres pasos al frente, un aplauso y tres pasos al costado B) girar rápido y saltar", "A", "Es simple y sin riesgos."),
        arith("Una secuencia tiene 4 pasos al frente, 3 aplausos y 2 pasos al costado. ¿Cuántos movimientos tiene en total?", "4+3+2", "Se suman todos los movimientos."),
    ],
    Z=[
        ex("Alonso dice: «Si cambio una palabra de un poema ajeno, ya es mío». ¿Qué error comete?", "Sigue copiando la obra ajena", "Cambiar una palabra no la hace propia."),
        ex("¿Por qué se muestra la obra al educador tradicional? A) para que sugiera cambios si algo no es respetuoso B) para ganar premios", "A", "Él o ella orienta."),
    ],
    D=[
        ex("Tres propuestas para una escena: 1) representar una ceremonia real con disfraces 2) representar la historia inventada de la Abuela Niebla con personajes 3) copiar una obra de teatro de un libro. ¿Cuál es adecuada?", "La segunda", "Es inventada y propia."),
        ex("Tu secuencia de movimientos necesita 12 pasos y los repartes en 3 partes iguales. ¿Cuántos pasos tiene cada parte? Responde con un número.", "4", "12 ÷ 3 = 4."),
    ],
    context=[ex("Para el acto de la escuela quieres cantar un canto de un pueblo real que aprendiste de un video. ¿Qué haces? A) pido a un educador o a la comunidad su permiso y enseñanza B) lo canto igual", "A", "El canto es de su comunidad.")],
    selfcheck=[
        ex("Nombra las cuatro partes de tu obra.", "Qué comunicar, forma, inspiración y límites", "Están en la explicación."),
        ex("Verdadero o falso: debo anotar la inspiración de mi obra.", "Verdadero", "Reconoce la fuente."),
        ex("¿Qué haces si un movimiento puede ser peligroso? A) lo cambio por uno simple B) lo hago igual", "A", "La seguridad es primero."),
    ],
    task=T("Crea una obra propia de 4 a 6 líneas (poema, canto o escena de teatro) sobre el agua o el territorio, inspirada en el poema inventado de doña Inés («El río me habla de noche, y yo escucho sin hablar») o en el canto inventado de la siembra. Escribe las cuatro partes: qué quieres comunicar, qué forma elegiste, de qué te inspiraste y qué límites respetaste. No copies versos y no imites ceremonias reales. Si añades movimiento, usa solo pasos simples, sin giros, saltos ni desplazamientos de espaldas.",
           "Quiero comunicar que el agua nos cuida. Forma: poema. Inspirado en el poema inventado de doña Inés. Versos: «El agua canta bajito / cuando pasa por mi calle, / me cuenta que viene de lejos / y que todos la esperamos». Límites: no copié versos ni imité ceremonias.",
           ["obra original", "cuatro partes", "reconoce la inspiración"], ["obra de 4 a 6 líneas", "las cuatro partes"], ["copiar versos", "imitar una ceremonia"],
           "Pedir que lea la obra y explique en qué se inspiró."),
    reinforce="Marca con color los versos propios y con otro la idea que tomaste de la obra inspiradora.",
    extend="Prepara una breve presentación (30 segundos) de tu obra para tu curso, con permiso para compartirla.",
)

L(
    OA17, 5, materials=MAT,
    use="Aprenderé a contrastar manifestaciones artísticas de distintas comunidades y de otras culturas, tradicionales y actuales, sin decir que una es más auténtica o mejor. Sirve para valorar la variedad de formas de comunicar la visión de mundo.",
    prior=["Sé relacionar arte, territorio y cosmovisión.", "Sé comparar sin jerarquizar."],
    explain=[
        "Contrastar manifestaciones artísticas es ver cómo se parecen y cómo se diferencian. Usamos criterios iguales: qué forma usan, qué elemento del territorio nombran y qué comunican sobre la visión de mundo. Comparamos el canto de Ladera Verde, el poema de Río Hondo, la canción actual de Isla Niebla y una obra de teatro inventada de Costa Lejana.",
        "Las cuatro obras usan la palabra, pero en formas distintas: canto, poesía, canción actual y teatro. Tres nombran elementos de la naturaleza y la cuarta cuenta la historia de una comunidad. Todas comunican algo sobre cómo viven, entienden y cuidan su lugar. Esas son semejanzas y diferencias, no puntajes.",
        "Contrastar no es decir cuál obra es más auténtica, más bella o más tradicional. Tampoco decimos que una cultura es mejor porque su arte es más antiguo. Incluimos obras de otras culturas significativas para nuestro contexto, con su fuente y su permiso. Las conclusiones valen solo para las obras leídas.",
    ],
    vocab=[("contrastar", "ver semejanzas y diferencias"), ("auténtico", "que se considera verdadero o propio; no se usa para ordenar obras"), ("criterio", "punto igual para comparar"), ("forma artística", "tipo de obra: canto, poema, teatro, danza"), ("valorar", "reconocer la importancia de algo")],
    worked=[
        W("Contrastar con un criterio", "Criterio «qué forma usa». Ladera Verde: canto. Río Hondo: poema. Isla Niebla: canción actual. Costa Lejana: teatro. ¿Qué diferencia hay?", ["Las cuatro usan formas distintas.", "Todas comunican con palabras.", "La diferencia es la forma."], "Cada obra usa una forma distinta: canto, poema, canción actual y teatro."),
        W("Evitar la jerarquía", "Un niño dice: «El canto de Ladera Verde es más auténtico que la canción de Isla Niebla porque es más antiguo». ¿Qué corriges?", ["Lo antiguo no es más auténtico.", "Ambas comunican su visión del mundo.", "No se ordenan."], "Corrijo: ambas son válidas y no se ordenan."),
    ],
    mistakes=[
        M("Decir que una obra es más auténtica por ser más antigua.", "La antigüedad no mide el valor.", "Compara con criterios iguales."),
        M("Dejar fuera una obra de otra cultura significativa.", "El OA pide mirar el aporte de varias culturas.", "Inclúyela con su fuente y permiso."),
    ],
    R=[
        ex("Canto inventado: «Baja el agua, baja el agua». ¿Qué forma artística es? A) canto B) teatro", "A", "Es un canto porque se canta."),
        ex("Obra inventada de Costa Lejana: unas personas representan la historia de su comunidad. ¿Qué forma artística es?", "Teatro", "Representar con personajes es teatro."),
        ex("¿Qué forma artística tiene versos y estrofas? A) la poesía B) el teatro", "A", "Los poemas se organizan en versos y estrofas."),
    ],
    C=[
        ex("Verdadero o falso: contrastar obras es decir cuál es más auténtica.", "Falso", "Contrastar es comparar sin ordenar."),
        ex("¿Qué es un criterio? A) un punto igual para comparar todas las obras B) una opinión", "A", "Así la comparación es justa."),
        ex("Verdadero o falso: las conclusiones valen solo para las obras que leímos.", "Verdadero", "No se generaliza."),
    ],
    A=[
        ex("Criterio «qué elemento del territorio aparece». Canto de Ladera Verde: el agua y la semilla. Poema de Río Hondo: el río y el lago. ¿Qué semejanza hay? A) ambos nombran elementos del agua B) ambos nombran un cerro", "A", "Los dos hablan del agua."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) las cuatro obras comunican algo de su comunidad b) una es canto y otra es poema.", "a semejanza, b diferencia", "La primera es común; la segunda cambia."),
        ex("Una niña pregunta cuál de las cuatro obras es la más bella. ¿Qué respondes? A) la belleza no se ordena aquí; cada obra comunica algo distinto B) la del poema", "A", "No se jerarquiza."),
    ],
    Z=[
        ex("Hernán concluye: «Todo el arte indígena habla del agua». ¿Qué error comete?", "Generaliza desde pocas obras", "Cuatro obras no representan todo el arte de los pueblos."),
        ex("¿Por qué se incluye una obra de otra cultura significativa para el contexto? A) para valorar distintas formas de comunicar la visión de mundo B) para ocupar espacio", "A", "El OA lo pide."),
    ],
    D=[
        ex("Cuadro con el criterio «tradicional o actual»: canto de la siembra, la ficha no lo dice; canción de Isla Niebla, actual. ¿Qué escribes para el canto? A) la ficha no lo dice B) tradicional", "A", "No se inventa."),
        ex("Quieres comparar con el arte del pueblo que corresponde a tu escuela. ¿Qué necesitas? A) una muestra autorizada por el educador tradicional B) una suposición", "A", "Hace falta fuente y permiso."),
    ],
    context=[ex("En la exposición de arte de la escuela hay un cartel que dice «La mejor obra». ¿Qué propones? A) cambiarlo por «Cuatro formas de comunicar» B) dejarlo", "A", "No se jerarquiza.")],
    selfcheck=[
        ex("Nombra dos criterios para contrastar obras artísticas.", "Dos entre: qué forma usa, qué elemento del territorio nombra, qué comunica", "Están en la explicación."),
        ex("Verdadero o falso: puedo decir que una obra es más auténtica que otra.", "Falso", "Eso jerarquiza las obras."),
        ex("¿Qué escribes si la ficha no dice si una obra es tradicional o actual? A) la ficha no lo dice B) tradicional", "A", "No se inventa."),
    ],
    task=T("Compara dos obras inventadas con tres criterios: forma, elemento del territorio y qué puedo pensar que comunica. Obra 1 (Río Hondo, poema): «Lleva en su agua mi nombre / hasta el lago grande y quieto». Obra 2 (Costa Lejana, teatro): «Narradora: Cada noche, las familias cuelgan linternas frente a su casa. Vecino: Así sabemos que estamos juntos». Escribe una semejanza, una diferencia y una frase que diga qué no puedes concluir.",
           "Obra 1: poema; el agua y el lago; puedo pensar que comunica el vínculo con el río. Obra 2: teatro; las linternas y las casas; puedo pensar que comunica estar juntos. Semejanza: ambas hablan de la vida de una comunidad. Diferencia: una es poema y la otra es teatro. No puedo concluir que todo el arte indígena sea así.",
           ["usa tres criterios iguales", "semejanza y diferencia", "no jerarquiza ni generaliza"], ["tabla de tres criterios", "tres frases"], ["decir cuál es más bella", "generalizar"],
           "Pedir que muestre la frase de cada obra para cada criterio."),
    reinforce="Pinta de verde las semejanzas y de azul las diferencias en tu tabla.",
    extend="Agrega una tercera obra de tu barrio, con permiso, y revisa si tu semejanza sigue valiendo.",
)

"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS04 (escribir oraciones y textos breves en castellano, incorporando conceptos en lengua indígena, en situaciones
como ceremonias, rogativas y salidas a terreno), OA LS05 (explicar el sentido de la revitalización y/o fortalecimiento
de su lengua para su propia identidad, reconociendo préstamos lingüísticos de uso cotidiano) y OA LS06 (producir
creaciones audiovisuales o escritas, en castellano, incorporando palabras en lengua indígena, con recursos TIC, para
contar situaciones personales, familiares o comunitarias).

Criterio de autoría: las situaciones, comunidades, museos, personas y fichas son inventados para practicar y están
rotulados como tales. Las palabras en lengua indígena son solo las muy atestiguadas: mari mari y chaltumay (mapuzugun),
iorana y maururu (rapa nui), los nombres de las lenguas, y palabras de origen indígena que ya son parte del castellano de
Chile (copihue y curanto, del mapuzugun; guagua, palta, choclo, poroto, cancha, pampa, puma, papa, del quechua; tomate y
chicle, del náhuatl; maíz y canoa, del taíno). No se inventa gramática, grafía, pronunciación ni significados rituales.
Las ceremonias y rogativas solo se mencionan como situaciones en las que se escribe un aviso, una invitación o un
agradecimiento; nunca se describe lo que ocurre en su interior. Cada tarea abierta remite al educador/a tradicional.
"""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_lc6_c import L, M, T, W

LS4 = "LC06 OA LS04"
LS5 = "LC06 OA LS05"
LS6 = "LC06 OA LS06"

LIS = "Lista de conceptos entregada por una fuente (la situación es inventada; las palabras son reales y conocidas): «mari mari», saludo en mapuzugun. «Chaltumay», agradecimiento en mapuzugun. «Mapuzugun», lengua del pueblo mapuche. «Copihue», flor; palabra de origen mapuzugun usada en el castellano de Chile. «Curanto», comida tradicional del sur de Chile; palabra de origen mapuzugun usada en el castellano de Chile."

# ============================================================ LS04 clase 1 · situar la situación y el concepto
S1 = "Situación 1 (inventada para practicar): el curso visitará el Museo Ejemplo, donde un guía del pueblo mapuche explicará una exposición de lana teñida. El guía pidió una nota de agradecimiento escrita en castellano, sin fotos de las personas."
S2 = "Situación 2 (inventada): la Escuela Ejemplo invita a las familias a una ceremonia abierta de una comunidad. Los organizadores piden una invitación breve en castellano y avisan que lo que ocurre dentro de la ceremonia lo cuentan solo ellos."
S3 = "Situación 3 (inventada): una comunidad avisa que realizará una rogativa, una ceremonia de petición, cerca de la escuela. Pide un aviso de respeto en castellano para la entrada: que se guarde silencio y que no se tomen fotos. Nada más."

L(
    LS4, 1,
    materials="Lápiz y hoja. Las tres situaciones y la lista de conceptos están escritas aquí y son inventadas para practicar. No necesitas dispositivos.",
    use="Aprenderé a situar un texto breve en castellano que incluye conceptos en lengua indígena: a quién escribo, para qué, qué concepto puedo incluir y de qué fuente viene. Sirve para escribir notas, invitaciones y avisos que respetan a las comunidades.",
    prior=["Sé que cada pueblo tiene su lengua, como el mapuzugun del pueblo mapuche.", "Sé que una expresión en lengua se usa solo si una fuente la entregó y la autorizó."],
    explain=[
        "Un texto en castellano puede incluir conceptos en lengua indígena: palabras o expresiones breves que una fuente me entregó, como el saludo «mari mari» o el agradecimiento «chaltumay». Para escribirlo primero preciso la situación: quién escribe, a quién, para qué y dónde se leerá. Una nota de agradecimiento, una invitación y un aviso de respeto son textos distintos.",
        "Después reviso los conceptos disponibles en mi lista. «Mari mari» sirve para saludar al comienzo; «chaltumay» sirve para agradecer. Hay también palabras de origen indígena que ya forman parte del castellano de Chile, como «copihue» y «curanto». Esas se escriben como cualquier palabra del castellano. En cambio, las expresiones como «mari mari» se destacan con comillas.",
        "En ceremonias y rogativas escribo solo lo que me piden: una invitación o un aviso. No describo lo que ocurre dentro ni invento su significado. Si la comunidad dice «nada más», agrego nada más. Si me falta un dato, lo anoto como «por preguntar» y lo consulto con el educador o la educadora tradicional.",
    ],
    vocab=[("concepto", "palabra o expresión con un sentido que se usa en un tema"), ("rogativa", "ceremonia de petición"), ("aviso de respeto", "texto breve que pide una conducta respetuosa"), ("destacar", "marcar una palabra para que se note, por ejemplo con comillas"), ("castellano de Chile", "el castellano que se habla en Chile")],
    worked=[
        W("Elegir el concepto", S1 + " " + LIS + " ¿Qué concepto sirve para agradecer al guía en la nota?", ["Necesito un agradecimiento.", "El guía es del pueblo mapuche y la fuente entregó «chaltumay».", "«Chaltumay» es el agradecimiento en mapuzugun."], "chaltumay"),
        W("Respetar lo que se pide", S3 + " ¿Qué debe decir el aviso de respeto?", ["Releo qué pidió la comunidad.", "Que se guarde silencio y que no se tomen fotos.", "No debo agregar descripciones de la ceremonia."], "que se guarde silencio y que no se tomen fotos, y nada más"),
    ],
    mistakes=[
        M("Agregar al aviso de la rogativa una explicación de para qué sirve la ceremonia.", "No la conozco y la comunidad pidió «nada más».", "Escribo solo lo que pidieron."),
        M("Usar «iorana» en la nota para un guía mapuche.", "«Iorana» es del rapa nui, no del mapuzugun.", "Uso las expresiones mapuzugun de la lista."),
    ],
    R=[
        ex(S1 + " ¿A quién va dirigida la nota de la situación 1?", "al guía del pueblo mapuche", "La situación lo dice."),
        ex(S2 + " ¿Qué texto piden los organizadores en la situación 2?", "una invitación breve", "Así lo dice la situación 2."),
        ex(LIS + " ¿Qué lengua es el mapuzugun: la del pueblo mapuche o la del pueblo aymara?", "la del pueblo mapuche", "La lista lo dice."),
    ],
    C=[
        ex(S3 + " ¿Qué dos conductas debe pedir el aviso de respeto?", "guardar silencio y no tomar fotos", "La situación 3 las nombra."),
        ex(LIS + " ¿Qué palabras de la lista ya son parte del castellano de Chile?", "copihue y curanto", "La lista las describe así."),
        ex("Verdadero o falso: en el aviso de una rogativa se puede explicar para qué sirve la ceremonia aunque la comunidad no lo haya pedido.", "Falso", "Se escribe solo lo que la comunidad pidió."),
    ],
    A=[
        ex(S1 + " Ordena los pasos para preparar la nota. A) escribir el borrador con el concepto elegido. B) responder quién, a quién, para qué y dónde. C) mostrar la nota al educador o a la educadora tradicional. Escribe las letras en orden.", "B, A, C", "Se entiende la situación, se escribe y se valida."),
        ex(LIS + " " + S2 + " Une cada necesidad con su concepto. 1) saludar a la comunidad al comienzo de la invitación. 2) agradecer al final. Opciones: A) chaltumay. B) mari mari. Escribe los dos pares.", "1-B, 2-A", "El saludo es «mari mari» y el agradecimiento es «chaltumay»."),
        arith(S2 + " La invitación debe tener como máximo 5 oraciones. Ya hay 2 sobre el día y el lugar, y 1 de saludo. ¿Cuántas oraciones más caben?", "5-2-1", "Se restan las ya escritas del máximo."),
    ],
    Z=[
        ex(S2 + " Un compañero propone describir en la invitación los pasos de la ceremonia. ¿Es correcto? Sí o No.", "No", "Lo que ocurre dentro lo cuentan solo los organizadores."),
        ex(S1 + " Otro compañero escribe la nota sin nombrar al guía. ¿Qué pregunta de las cuatro responde mal?", "a quién le escribe", "Debe dirigirse al guía."),
    ],
    D=[
        ex(LIS + " Un estudiante quiere agregar a la nota otra palabra en mapuzugun que oyó en una película. ¿Está en la lista? Sí o No.", "No", "Solo se usan los conceptos que la fuente entregó."),
        ex(S3 + " Dos versiones del aviso. A) «Hoy hay una rogativa cerca de la escuela. Por favor, guarde silencio y no tome fotos». B) «Hoy hay una rogativa para pedir lluvia; guarde silencio y no tome fotos». ¿Cuál agrega algo que la comunidad no pidió? Escribe la letra.", "B", "Dice para qué es la rogativa, y eso no lo sé ni me lo pidieron."),
    ],
    context=[ex("Tu curso escribirá una nota para una comunidad que lo recibió en una salida a terreno. ¿Qué haces primero: responder quién, a quién, para qué y dónde, o buscar frases en lengua para decorar?", "responder quién, a quién, para qué y dónde", "Primero se entiende la situación.")],
    selfcheck=[
        ex("¿«Copihue» se destaca con comillas o se escribe como cualquier palabra del castellano?", "se escribe como cualquier palabra del castellano", "Ya es parte del castellano de Chile."),
        ex("¿Una rogativa es una ceremonia de petición o un paseo?", "una ceremonia de petición", "Así se definió."),
        ex("Si me falta un dato, ¿lo invento o lo anoto «por preguntar»?", "lo anoto «por preguntar»", "Se consulta con la fuente."),
    ],
    task=T(
        "Lee esta situación inventada: «La Escuela Ejemplo visitará la feria de lana de la Comunidad Muestra, del pueblo mapuche. Una artesana recibirá al curso y autorizó que se la salude con «mari mari» y se le agradezca con «chaltumay». No se pueden tomar fotos de las personas.» En tu cuaderno escribe una nota de agradecimiento en castellano de tres oraciones que incluya los dos conceptos entre comillas, y debajo responde: ¿a quién le escribes y para qué?",
        "«Mari mari», estimada artesana. Gracias por recibir a nuestro curso en la feria de lana. «Chaltumay» por enseñarnos su trabajo. A quién: a la artesana. Para qué: agradecer su recibimiento.",
        ["incluye «mari mari» y «chaltumay» como la fuente los autorizó", "está escrita en castellano con los conceptos destacados con comillas", "responde a quién y para qué", "no agrega frases en lengua ni datos que no se entregaron"],
        ["nota de tres oraciones", "dos respuestas escritas"],
        ["agregar frases en lengua que no se entregaron", "contar algo no autorizado"],
        "Si agrega frases en lengua, pídele que revise la lista de conceptos y deje solo los autorizados.",
    ),
    reinforce="Vuelve a leer las tres situaciones y subraya qué texto se pide en cada una.",
    extend="Escribe una situación inventada de salida a terreno con quién escribe, a quién, para qué y dónde, y marca qué concepto de la lista usarías.",
)

# ============================================================ LS04 clase 2 · leer un modelo con conceptos
MOD4 = "Texto modelo (inventado para practicar): «Estimado guía: «mari mari». Hoy, en el Museo Ejemplo, aprendimos cómo se tiñe la lana con plantas. Nos gustó el color de una lana que usted llama copihue, por la flor. Después de la visita, comimos un curanto en la plaza con nuestras familias. «Chaltumay» por su recibimiento. No contaremos lo que usted nos pidió reservar. Curso 6.º C, Escuela Ejemplo.»"

L(
    LS4, 2,
    materials="Lápiz y hoja. El texto modelo está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta en voz alta.",
    use="Aprenderé a leer un texto en castellano con conceptos en lengua indígena, a distinguir cuáles son expresiones entregadas por una fuente y cuáles son palabras ya incorporadas al castellano, y a reconocer los límites que respeta. Sirve para escribir mis propios textos sin errores.",
    prior=["Sé situar un texto y elegir el concepto de la lista.", "Sé que las expresiones como «mari mari» se destacan con comillas."],
    explain=[
        "En el texto modelo hay dos tipos de conceptos. Primero están las expresiones en lengua que una fuente entregó, como «mari mari» y «chaltumay». Se copian tal cual y se destacan con comillas. Segundo están las palabras de origen indígena que ya son parte del castellano de Chile, como «copihue» y «curanto». Esas se escriben sin comillas, como cualquier otra palabra.",
        "En el texto, «copihue» aparece como nombre de un color de lana, por la flor, y «curanto» como una comida que se comió con las familias. Ambas palabras se usan con su significado habitual en castellano. No necesito explicar qué quieren decir si el lector las conoce; si sospecho que no, agrego una explicación breve, una glosa, entre comas o paréntesis.",
        "El texto también declara un límite: «No contaremos lo que usted nos pidió reservar». Ese límite protege lo que el guía no quiso compartir. Un buen texto muestra lo que se vivió y lo que se aprendió, pero no revela lo que se pidió guardar. Si aparece una palabra que no entiendo, la anoto para preguntar y no la traduzco por mi cuenta.",
    ],
    vocab=[("glosa", "explicación breve de una palabra puesta entre comas o paréntesis"), ("comillas", "signos « » que destacan una palabra o una cita"), ("reservar", "mantener algo sin contar"), ("recibimiento", "forma en que se recibe a alguien"), ("teñir", "dar color a una tela o lana")],
    worked=[
        W("Distinguir los dos tipos", MOD4 + " ¿«Mari mari» o «copihue» es una expresión que debe destacarse con comillas?", ["«Mari mari» es una expresión en lengua entregada por la fuente.", "«Copihue» ya es parte del castellano de Chile.", "Por eso las comillas se usan en «mari mari»."], "«mari mari»"),
        W("Reconocer el límite", MOD4 + " ¿Qué límite respeta el curso?", ["Busco la frase que promete no contar algo.", "Dice que no contarán lo que el guía pidió reservar.", "Ese es el límite."], "no contar lo que el guía pidió reservar"),
    ],
    mistakes=[
        M("Escribir «copihue» entre comillas como si fuera una expresión de la fuente.", "Es una palabra ya incorporada al castellano.", "La escribo sin comillas."),
        M("Traducir por mi cuenta una palabra que no entiendo.", "Puedo equivocarme y cambiar el sentido.", "La anoto y pregunto al educador o a la educadora tradicional."),
    ],
    R=[
        ex(MOD4 + " ¿Dónde se hizo la visita?", "en el Museo Ejemplo", "El texto lo dice."),
        ex(MOD4 + " ¿Con qué se tiñe la lana según el texto?", "con plantas", "El texto lo dice."),
        ex(MOD4 + " ¿Qué comieron en la plaza con sus familias?", "un curanto", "El texto lo dice."),
    ],
    C=[
        ex(MOD4 + " ¿Qué nombre le da el guía a un color de lana?", "copihue", "El texto lo dice."),
        ex(MOD4 + " ¿Qué dos expresiones en lengua entregó la fuente?", "mari mari y chaltumay", "Son las que están entre comillas."),
        ex(MOD4 + " Verdadero o falso: el texto cuenta lo que el guía pidió reservar.", "Falso", "Declara que no lo contará."),
    ],
    A=[
        ex(MOD4 + " Clasifica cada palabra como E (expresión de la fuente, con comillas) o C (palabra incorporada al castellano, sin comillas). 1) mari mari. 2) copihue. 3) chaltumay. 4) curanto. Escribe las cuatro letras.", "1 E, 2 C, 3 E, 4 C", "Mari mari y chaltumay son expresiones de la fuente; copihue y curanto ya son castellano de Chile."),
        arith(MOD4 + " El texto tiene 4 palabras de origen indígena en total: 2 expresiones de la fuente y las demás ya incorporadas al castellano. ¿Cuántas son palabras ya incorporadas al castellano?", "4-2", "Se restan las expresiones de la fuente del total."),
        ex(MOD4 + " Ordena las partes del texto. A) límite. B) agradecimiento. C) saludo. D) lo aprendido. E) firma. Escribe las letras en orden.", "C, D, B, A, E", "El texto saluda, cuenta lo aprendido, agradece, declara el límite y firma."),
    ],
    Z=[
        ex(MOD4 + " Un compañero propone agregar a la nota: «y también nos mostraron una ceremonia». ¿Puede agregarse esa oración? Sí o No.", "No", "No está en el texto y una ceremonia no se cuenta sin permiso."),
        ex(MOD4 + " Un niño dice que «curanto» es una expresión de la fuente y que debe ir entre comillas. ¿Tiene razón? Sí o No.", "No", "Es una palabra ya incorporada al castellano de Chile."),
    ],
    D=[
        ex("Una niña no sabe si cierta palabra mapuzugun que oyó en la visita es un saludo o una despedida. ¿Qué debe hacer: usarla en su nota por si acaso o consultarla con la fuente?", "consultarla con la fuente", "No se usa una expresión de significado dudoso."),
        ex(MOD4 + " Elige la mejor glosa para «curanto» si el lector no la conoce. A) «curanto (comida tradicional del sur de Chile)». B) «curanto (un invento de nuestro curso)». Escribe la letra.", "A", "La glosa debe decir lo que la palabra significa de verdad."),
    ],
    context=[ex("Escribes un informe de una salida a terreno y una persona te pidió que no cuentes una historia. ¿La cuentas con otras palabras o la dejas fuera y lo dices?", "la dejas fuera y lo dices", "Respetas el límite que te pidió.")],
    selfcheck=[
        ex("¿Qué palabras llevan comillas: las expresiones de la fuente o las palabras ya incorporadas al castellano?", "las expresiones de la fuente", "Así se destacan."),
        ex("Una glosa, ¿explica una palabra brevemente o la borra?", "explica una palabra brevemente", "Esa es su función."),
        ex("¿Debo traducir por mi cuenta lo que no entiendo? Sí o No.", "No", "Se consulta a la fuente."),
    ],
    task=T(
        "Lee este texto inventado: «Querida artesana: «mari mari». Hoy, en el taller de tejido, aprendimos a teñir lana con plantas. Compartimos una merienda con curanto en el patio. «Chaltumay» por enseñarnos. No contaremos lo que usted nos pidió reservar. Curso 6.º D.» En tu cuaderno marca con una E las expresiones de la fuente, con una C las palabras incorporadas al castellano y con una L el límite. Después escribe una frase que explique por qué «curanto» va sin comillas.",
        "E: «mari mari» y «chaltumay». C: curanto. L: «No contaremos lo que usted nos pidió reservar». Explicación: «Curanto» va sin comillas porque ya es una palabra del castellano de Chile.",
        ["marca E, C y L correctamente", "explica por qué curanto no lleva comillas", "no agrega expresiones ni datos nuevos"],
        ["texto marcado en el cuaderno", "una frase de explicación"],
        ["marcar curanto como expresión de la fuente", "olvidar el límite"],
        "Si marca mal, pídele que relea la definición de las dos clases de palabras.",
    ),
    reinforce="Copia el texto modelo y pon una E, una C o una L al lado de cada palabra o frase que corresponda.",
    extend="Escribe una nota de dos oraciones con una palabra incorporada al castellano y una glosa para ella.",
)

# ============================================================ LS04 clase 3 · relacionar conceptos con pueblos y usos
TAB = "Tabla de conceptos (las palabras y orígenes son reales y muy conocidos): «mari mari» y «chaltumay» son expresiones del mapuzugun, la lengua del pueblo mapuche. «Iorana» y «maururu» son expresiones del rapa nui, la lengua del pueblo rapa nui. «Copihue» y «curanto» son palabras de origen mapuzugun que ya se usan en el castellano de Chile. «Guagua» y «palta» son palabras de origen quechua que ya se usan en el castellano de Chile."

L(
    LS4, 3,
    materials="Lápiz y hoja. La tabla de conceptos está escrita aquí. No necesitas dispositivos.",
    use="Aprenderé a relacionar cada concepto en lengua indígena con su pueblo, su origen y su uso en un texto en castellano. Sirve para elegir bien el concepto según la comunidad a la que escribo y para no mezclar lenguas de pueblos distintos.",
    prior=["Sé distinguir expresiones de la fuente y palabras incorporadas al castellano.", "Sé que un saludo va al comienzo y un agradecimiento al final."],
    explain=[
        "Cada concepto de la tabla tiene tres datos: de qué lengua o pueblo viene, qué significa o para qué sirve y cómo se escribe en un texto en castellano. «Mari mari» y «chaltumay» son del mapuzugun: un saludo y un agradecimiento. «Iorana» y «maururu» son del rapa nui: también un saludo y un agradecimiento. Cada pareja se usa con la comunidad de su pueblo.",
        "Algunas palabras de origen indígena ya viajaron al castellano. «Copihue» y «curanto» vienen del mapuzugun. «Guagua» y «palta» vienen del quechua. Las usamos todos los días sin pensarlo. Se escriben sin comillas, porque ya son castellano de Chile. Pero conocer su origen ayuda a valorar que las lenguas indígenas están presentes en la vida cotidiana.",
        "Relacionar también es pensar en el respeto. Usar «mari mari» en una nota para una comunidad mapuche muestra atención a su lengua. Usarla para una comunidad rapa nui sería un error, porque cada pueblo tiene sus propias expresiones. Y compararlas con mis saludos de casa no es jerarquizar: puedo decir qué se parece y qué cambia.",
    ],
    vocab=[("origen", "lengua de donde viene una palabra"), ("quechua", "lengua del pueblo quechua"), ("uso cotidiano", "uso de todos los días"), ("pareja de expresiones", "saludo y agradecimiento de una misma lengua"), ("comunidad", "grupo de personas que comparten un lugar y una cultura")],
    worked=[
        W("Relacionar con un pueblo", TAB + " Escribes a una comunidad rapa nui. ¿Qué pareja de expresiones eliges?", ["Necesito expresiones del rapa nui.", "La tabla da «iorana» y «maururu».", "Una es saludo y la otra agradecimiento."], "iorana y maururu"),
        W("Reconocer una palabra de uso cotidiano", TAB + " ¿De qué lengua viene «palta»?", ["Busco «palta» en la tabla.", "Dice que es de origen quechua.", "Ya se usa en el castellano de Chile."], "del quechua"),
    ],
    mistakes=[
        M("Escribir «mari mari» en una nota para una comunidad rapa nui.", "Esa expresión es del mapuzugun.", "Uso «iorana» si la fuente lo entregó."),
        M("Poner «guagua» entre comillas como si fuera una expresión de la fuente.", "Es una palabra ya incorporada al castellano.", "La escribo sin comillas."),
    ],
    R=[
        ex(TAB + " ¿De qué lengua es «mari mari»?", "del mapuzugun", "La tabla lo dice."),
        ex(TAB + " ¿Qué es «maururu» en rapa nui?", "una expresión de agradecimiento", "La tabla lo indica."),
        ex(TAB + " ¿De qué lengua viene «guagua»?", "del quechua", "La tabla lo dice."),
    ],
    C=[
        ex(TAB + " ¿Qué palabras de la tabla vienen del mapuzugun y ya son parte del castellano de Chile?", "copihue y curanto", "La tabla lo dice."),
        ex(TAB + " ¿Qué lengua es el rapa nui: la del pueblo rapa nui o la del pueblo mapuche?", "la del pueblo rapa nui", "La tabla lo dice."),
        ex("Verdadero o falso: «guagua» y «palta» deben escribirse entre comillas como expresiones de una fuente.", "Falso", "Ya son parte del castellano de Chile."),
    ],
    A=[
        ex(TAB + " Une cada palabra con su lengua. Palabras: A) chaltumay, B) iorana, C) palta, D) copihue. Lenguas: 1) quechua, 2) mapuzugun, 3) rapa nui. Escribe los cuatro pares.", "A-2, B-3, C-1, D-2", "Chaltumay y copihue vienen del mapuzugun, iorana es del rapa nui y palta es del quechua."),
        arith(TAB + " La tabla nombra 8 conceptos en total. De ellos, 4 son expresiones de la fuente. ¿Cuántos son palabras ya incorporadas al castellano?", "8-4", "Se restan las expresiones de la fuente del total."),
        ex(TAB + " Escribes una nota de bienvenida a una comunidad mapuche. ¿Qué dos conceptos de la tabla usas para saludar y para agradecer?", "mari mari y chaltumay", "Son la pareja del mapuzugun."),
    ],
    Z=[
        ex(TAB + " Un compañero dice que si «copihue» viene del mapuzugun, entonces ya no es castellano. ¿Tiene razón? Sí o No.", "No", "Una palabra de origen indígena puede ser parte del castellano."),
        ex(TAB + " Escribes a una comunidad aymara. ¿La tabla te entrega una expresión del aymara? Sí o No.", "No", "La tabla no incluye ninguna del aymara; habría que consultarla con una fuente."),
    ],
    D=[
        ex("Una niña compara: «En mi casa se saluda con un abrazo y en una comunidad mapuche se saluda con mari mari; cambia la forma y en ambos casos se reconoce a la otra persona». ¿Compara sin jerarquizar? Sí o No.", "Sí", "Dice qué cambia y qué se parece."),
        ex("Un joven dice: «Los que usan palabras indígenas en castellano son más auténticos». ¿Es correcto? Sí o No.", "No", "Eso jerarquiza y no se apoya en datos."),
    ],
    context=[ex("Alguien dice «guagua» y otra persona dice «bebé». ¿Cuál es incorrecta? Responde: ninguna, o la que viene del quechua.", "ninguna", "Ambas son palabras válidas del castellano de Chile.")],
    selfcheck=[
        ex("¿«Iorana» es del mapuzugun o del rapa nui?", "del rapa nui", "La tabla lo dice."),
        ex("¿«Palta» necesita comillas? Sí o No.", "No", "Ya es castellano de Chile."),
        ex("¿Cada pueblo tiene sus propias expresiones? Sí o No.", "Sí", "Por eso no se mezclan."),
    ],
    task=T(
        "Lee esta situación inventada: «El curso escribirá dos notas: una para una comunidad mapuche que lo recibió en un taller y otra para un guía rapa nui de un museo.» Con la tabla de la clase, escribe en tu cuaderno dos notas de dos oraciones cada una en castellano: una con «mari mari» y «chaltumay», y la otra con «iorana» y «maururu». Agrega a cada nota una palabra de uso cotidiano de la tabla (por ejemplo «palta» o «copihue») sin comillas.",
        "Nota 1: «Mari mari», artesana. Gracias por mostrarnos su copihue pintado en la lana. «Chaltumay». Nota 2: «Iorana», guía. «Maururu» por mostrarnos el museo; nos gustó la palta del cuadro de frutas.",
        ["usa cada pareja con su pueblo", "destaca las expresiones de la fuente con comillas", "escribe las palabras incorporadas sin comillas", "no mezcla lenguas"],
        ["dos notas escritas"],
        ["mezclar expresiones de pueblos distintos", "poner comillas a palabras ya incorporadas"],
        "Si mezcla lenguas, pídele que vuelva a la tabla y coloque cada pareja con su pueblo.",
    ),
    reinforce="Haz una tabla de dos columnas, «expresiones de la fuente» y «palabras ya incorporadas», y copia las de la clase.",
    extend="Averigua con una persona mayor de tu casa otras dos palabras de uso cotidiano que vengan de una lengua indígena y anótalas.",
)

# ============================================================ LS04 clase 4 · un informe atribuido
FV4 = "Ficha de la visita (inventada para practicar): Lugar: taller de cerámica de la Comunidad Ejemplo, pueblo mapuche. Persona que recibió al curso: una alfarera. Autorizó contar: que el taller funciona los martes y que las personas aprenden a modelar greda. Saludo autorizado: «mari mari». Agradecimiento autorizado: «chaltumay». Pidió no contar: las conversaciones que se tuvieron dentro del taller."

L(
    LS4, 4,
    materials="Lápiz y hoja. La ficha de la visita está escrita aquí y es inventada para practicar.",
    use="Aprenderé a escribir un informe breve en castellano que incorpora conceptos en lengua indígena, atribuye lo aprendido a su fuente y respeta lo que no se debe contar. Sirve para dar cuenta de una salida a terreno sin inventar.",
    prior=["Sé distinguir expresiones de la fuente y palabras incorporadas al castellano.", "Sé que «según» atribuye lo dicho a su fuente."],
    explain=[
        "Un informe breve tiene cuatro partes. Saluda, con la expresión autorizada. Cuenta lo aprendido diciendo quién lo enseñó, con «según». Agradece con la expresión autorizada. Y declara el límite: que no cuenta lo que no se autorizó. Todo en castellano, con los conceptos en lengua destacados con comillas.",
        "La ficha de la visita contiene todo lo que puedo usar. Por ejemplo, puedo decir que el taller funciona los martes y que las personas aprenden a modelar greda, porque la alfarera lo autorizó. No puedo decir cuánto tiempo hace que existe el taller ni qué tipo de piezas se hacen, porque eso no está en la ficha.",
        "Cada oración debe poder comprobarse en la ficha. Si me gustaría agregar algo, lo escribo como pregunta para la alfarera. Y antes de entregar el informe, se lo leo al educador o a la educadora tradicional para que confirme que respeté lo que se autorizó. Así no hablo en nombre de la comunidad ni invento.",
    ],
    vocab=[("informe", "texto que cuenta lo que se vio y aprendió"), ("alfarera", "persona que modela objetos de greda"), ("greda", "tierra suave con que se hacen objetos de cerámica"), ("comprobar", "revisar que algo es verdadero"), ("atribuir", "decir de quién viene la información")],
    worked=[
        W("Armar la oración del saludo", FV4 + " Escribe una oración de saludo.", ["Uso el saludo autorizado entre comillas.", "Nombro a la persona que recibió al curso.", "Escribo la oración."], "«Mari mari», estimada alfarera."),
        W("Atribuir lo aprendido", FV4 + " Escribe una oración con lo autorizado y su fuente.", ["Elijo un dato autorizado: el taller funciona los martes.", "Empiezo con «Según…» y nombro a la alfarera y la comunidad.", "Escribo la oración."], "Según una alfarera de la Comunidad Ejemplo, el taller funciona los martes."),
    ],
    mistakes=[
        M("Escribir «el taller existe hace cien años».", "Ese dato no está en la ficha.", "Escribo solo lo que dice la ficha."),
        M("Poner el agradecimiento sin comillas en «chaltumay».", "Es una expresión de la fuente y se destaca.", "La escribo entre comillas."),
    ],
    R=[
        ex(FV4 + " ¿Qué día funciona el taller?", "los martes", "La ficha lo dice."),
        ex(FV4 + " ¿Qué aprenden las personas en el taller?", "a modelar greda", "La ficha lo dice."),
        ex(FV4 + " ¿Qué agradecimiento autorizó la alfarera?", "chaltumay", "La ficha lo dice."),
    ],
    C=[
        ex(FV4 + " ¿Qué pidió la alfarera que no se contara?", "las conversaciones dentro del taller", "La ficha lo dice como límite."),
        ex(FV4 + " ¿Dónde se hizo la visita?", "en un taller de cerámica de la Comunidad Ejemplo", "La ficha lo dice."),
        ex(FV4 + " Verdadero o falso: la ficha dice cuántos años tiene el taller.", "Falso", "No incluye ese dato."),
    ],
    A=[
        ex("Ordena las cuatro partes del informe. A) límite. B) agradecimiento. C) saludo. D) lo aprendido con «según». Escribe las letras en orden.", "C, D, B, A", "Saludo, lo aprendido, agradecimiento y límite."),
        ex(FV4 + " Elige la mejor oración. A) «Según una alfarera de la Comunidad Ejemplo, el taller funciona los martes». B) «Todos los talleres de los mapuche funcionan los martes». Escribe la letra.", "A", "Atribuye y no generaliza."),
        arith("El informe debe tener 4 oraciones y un estudiante escribió 1. ¿Cuántas oraciones le faltan?", "4-1", "Se restan las escritas de las cuatro pedidas."),
    ],
    Z=[
        ex(FV4 + " Una niña escribe: «La alfarera nos mostró cómo se hacen las vasijas rituales». ¿Está en la ficha? Sí o No.", "No", "La ficha no habla de vasijas rituales."),
        ex(FV4 + " Un niño quiere contar una conversación que oyó dentro del taller. ¿Respeta el límite? Sí o No.", "No", "La alfarera pidió no contarlas."),
    ],
    D=[
        ex(FV4 + " Dos versiones del cierre. A) «No contaremos las conversaciones que tuvimos dentro del taller». B) «Tal vez más adelante contemos las conversaciones». ¿Cuál respeta lo que pidió la alfarera? Escribe la letra.", "A", "La B deja abierta la posibilidad de contarlas."),
        ex("Al revisar tu informe notas que usaste una palabra en lengua que la ficha no tiene. ¿Qué haces: la dejas o la sacas y consultas a la fuente?", "la sacas y consultas a la fuente", "Solo se usan los conceptos autorizados."),
    ],
    context=[ex("Tu curso presenta un informe de la visita a un taller. Alguien de la comunidad te dijo en privado una anécdota. ¿La incluyes en el informe o la dejas fuera?", "la dejas fuera", "Lo dicho en privado no se cuenta sin permiso.")],
    selfcheck=[
        ex("¿Cuántas partes tiene el informe breve de esta clase?", "4", "Saludo, lo aprendido, agradecimiento y límite."),
        ex("¿Qué palabra uso para nombrar la fuente: «según» o «siempre»?", "según", "La palabra según atribuye lo dicho."),
        ex("Antes de entregar, ¿se lo leo a la fuente o al educador tradicional? Sí o No.", "Sí", "Así confirmo que respeté lo autorizado."),
    ],
    task=T(
        "Lee esta ficha inventada: «Lugar: sala de radio de la Comunidad Muestra, pueblo rapa nui. Persona que recibió al curso: una locutora comunitaria. Autorizó contar: que el programa se transmite los domingos. Saludo autorizado: «iorana». Agradecimiento autorizado: «maururu». Pidió no contar: los nombres de quienes llaman al programa.» En tu cuaderno escribe un informe de cuatro oraciones en castellano (saludo, lo aprendido con «según», agradecimiento y límite) usando solo lo que está en la ficha.",
        "«Iorana», estimada locutora. Según una locutora comunitaria de la Comunidad Muestra, el programa se transmite los domingos. «Maururu» por recibir a nuestro curso. No contaremos los nombres de quienes llaman al programa.",
        ["tiene las cuatro partes", "usa los conceptos autorizados entre comillas", "atribuye con «según»", "declara el límite y no agrega datos"],
        ["informe de cuatro oraciones"],
        ["agregar datos que no están en la ficha", "olvidar el límite"],
        "Pide que marque en la ficha cada dato que usó; lo no marcado debe salir.",
    ),
    reinforce="Copia las cuatro oraciones del ejemplo y rotula cada una con su función.",
    extend="Escribe una segunda versión del informe para un cartel de pasillo de dos oraciones, con el límite.",
)

# ============================================================ LS04 clase 5 · contrastar dos textos
TXA = "Texto A (inventado): ««Mari mari», artesana. Gracias por recibirnos en el taller. «Chaltumay». No contaremos lo que usted nos pidió reservar.» (nota del 6.º A a una artesana de una comunidad mapuche)."
TXB = "Texto B (inventado): ««Iorana», guía. «Maururu» por mostrarnos el museo. Comimos un curanto después de la visita.» (nota del 6.º B a un guía de una comunidad rapa nui)."

L(
    LS4, 5,
    materials="Lápiz y hoja. Los dos textos están escritos aquí y son inventados para practicar.",
    use="Aprenderé a comparar dos textos en castellano con conceptos en lengua indígena usando los mismos criterios, diciendo qué se parece y qué cambia sin decir que uno sea mejor por la lengua o el pueblo. Sirve para valorar la diversidad.",
    prior=["Sé armar un informe atribuido.", "Sé que jerarquizar es decir que algo vale más que otra cosa."],
    explain=[
        "Comparar es mirar dos textos con los mismos criterios. Para estos textos puedo usar: a quién va dirigido, qué expresiones de la fuente usa, si declara un límite y si incluye palabras ya incorporadas al castellano. Respondo cada criterio para cada texto y después escribo qué se parece y qué cambia.",
        "El texto A es una nota a una artesana mapuche con «mari mari» y «chaltumay», y declara un límite. El texto B es una nota a un guía rapa nui con «iorana» y «maururu», y no declara ningún límite, pero usa la palabra «curanto», ya incorporada al castellano. Esas son diferencias y semejanzas comprobables.",
        "No jerarquizo. No digo «el texto A es más respetuoso porque es mapuche» ni «el B es más moderno». Sí puedo decir, con un dato, que el texto A cumple un paso que el B no incluye: declarar un límite. Cierro con una frase que diga una semejanza y una diferencia, sin palabras como «mejor» o «más auténtico».",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian"), ("jerarquizar", "decir que algo vale más que otra cosa"), ("incorporada", "que ya forma parte del castellano")],
    worked=[
        W("Comparar con un criterio", TXA + " " + TXB + " Compara a quién va dirigido cada texto.", ["El texto A va a una artesana de una comunidad mapuche.", "El texto B va a un guía de una comunidad rapa nui.", "Los destinatarios son distintos."], "A va a una artesana mapuche y B a un guía rapa nui"),
        W("Reconocer una jerarquización", "Alguien dice: «El texto A es mejor porque usa una lengua más importante». ¿Compara o jerarquiza?", ["La frase dice que una lengua es más importante.", "Ninguna lengua vale más que otra.", "Pone un texto sobre otro."], "jerarquiza"),
    ],
    mistakes=[
        M("Escribir «el texto del mapuzugun es más auténtico que el del rapa nui».", "No se jerarquizan lenguas.", "Comparo con criterios: destinatario, expresiones, límite."),
        M("Comparar un texto con un criterio y el otro con otro distinto.", "Así no se puede comparar.", "Uso los mismos criterios para ambos."),
    ],
    R=[
        ex(TXA + " ¿Qué saludo usa el texto A?", "mari mari", "Es la primera expresión del texto A."),
        ex(TXB + " ¿Qué agradecimiento usa el texto B?", "maururu", "Aparece en la segunda oración."),
        ex(TXB + " ¿Qué palabra ya incorporada al castellano usa el texto B?", "curanto", "Aparece en la tercera oración."),
    ],
    C=[
        ex(TXA + " " + TXB + " ¿Cuál de los dos textos declara un límite?", "el texto A", "Dice «No contaremos lo que usted nos pidió reservar»."),
        ex(TXA + " " + TXB + " ¿A qué pueblo se dirige cada nota?", "A al pueblo mapuche y B al pueblo rapa nui", "Cada texto lo indica."),
        ex("Verdadero o falso: es correcto decir que un texto es mejor porque su lengua es más importante.", "Falso", "No se jerarquizan lenguas."),
    ],
    A=[
        ex(TXA + " " + TXB + " Completa con A o B: el texto ___ declara un límite; el texto ___ usa una palabra ya incorporada al castellano. Escribe las dos letras en orden.", "A, B", "El A declara el límite y el B usa curanto."),
        arith(TXA + " " + TXB + " Cada texto usa 2 expresiones de la fuente entre comillas. ¿Cuántas expresiones de la fuente hay entre los dos textos?", "2+2", "Se suman las expresiones de los dos textos."),
        ex("Clasifica cada frase como C (compara) o J (jerarquiza). 1) «Los dos textos saludan y agradecen con las expresiones de su comunidad». 2) «El texto B es más moderno». 3) «Solo el A declara un límite». Escribe las tres letras.", "1 C, 2 J, 3 C", "Solo la frase 2 pone un texto sobre otro."),
    ],
    Z=[
        ex(TXA + " " + TXB + " Una compañera dice que el texto B debería haber declarado un límite. ¿Eso es una observación comparable con el texto A? Sí o No.", "Sí", "Se basa en una diferencia de contenido entre los textos."),
        ex(TXA + " " + TXB + " Otro dice que los dos textos son del mismo pueblo porque tienen un saludo. ¿Es correcto? Sí o No.", "No", "Uno es del pueblo mapuche y el otro del pueblo rapa nui."),
    ],
    D=[
        ex(TXA + " " + TXB + " Elige la mejor frase de cierre. A) «Los dos textos saludan y agradecen con las expresiones de su comunidad; el A declara un límite y el B incluye una palabra ya incorporada al castellano». B) «El texto A es el mejor». Escribe la letra.", "A", "Dice semejanza y diferencia con datos."),
        ex("Dudas si una expresión de uno de los textos está bien escrita. ¿La corriges por tu cuenta o la consultas con el educador o la educadora tradicional?", "la consultas con el educador o la educadora tradicional", "Solo quien conoce la lengua puede confirmarla."),
    ],
    context=[ex("Dos cursos hicieron notas para comunidades distintas. Te piden decir cuál nota es mejor. ¿Explicas qué se parece y qué cambia o eliges una sin razones?", "explicas qué se parece y qué cambia", "Comparar con criterios evita jerarquizar.")],
    selfcheck=[
        ex("¿Cuántos textos se comparan en esta clase?", "2", "Son el texto A y el texto B."),
        ex("¿«Más auténtico» compara o jerarquiza?", "jerarquiza", "Pone una cosa sobre otra."),
        ex("¿Se usan los mismos criterios para los dos textos? Sí o No.", "Sí", "Así se compara de manera justa."),
    ],
    task=T(
        "Lee estos textos inventados. Texto 1: ««Mari mari», educadora. Gracias por la visita al huerto. «Chaltumay». Contaremos solo lo autorizado.» Texto 2: ««Iorana», bailarín. «Maururu» por su visita a la escuela. Compartimos un curanto con las familias.» En tu cuaderno haz una tabla con filas: destinatario, expresiones de la fuente, límite y palabra ya incorporada al castellano. Luego escribe una frase de cierre con una semejanza y una diferencia, sin jerarquizar.",
        "Destinatario: educadora / bailarín. Expresiones: mari mari y chaltumay / iorana y maururu. Límite: sí / no. Palabra incorporada: no hay / curanto. Cierre: «Los dos textos saludan y agradecen con las expresiones de su comunidad; el primero declara un límite y el segundo incluye la palabra curanto.»",
        ["completa las cuatro filas para ambos textos", "usa los mismos criterios", "escribe semejanza y diferencia", "no jerarquiza"],
        ["tabla de comparación", "frase de cierre"],
        ["decir que un texto es mejor", "dejar una fila sin completar"],
        "Si aparece una jerarquización, pídele que cambie esa palabra por un dato de la tabla.",
    ),
    reinforce="Copia los textos A y B y subraya en cada uno las expresiones entre comillas.",
    extend="Compara uno de los textos de la clase con una nota de agradecimiento escrita por ti para tu familia, sin jerarquizar.",
)


# ============================================================ LS05 clase 1 · situar identidad y revitalización
FI = "Ficha de testimonio (inventada para practicar): Pueblo: mapuche. Comunidad Ejemplo. Fuente: una joven de la comunidad, que habla poco su lengua y participa en un taller de lengua. Autorización: permite contar lo que dijo en la sala. Dijo: «Aprender la lengua de mi pueblo me hace sentir más cerca de mi familia. Nadie deja de ser de nuestro pueblo por hablar poco la lengua». Habla solo por ella y su comunidad."

L(
    LS5, 1,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a situar un testimonio sobre identidad y lengua: de qué pueblo y comunidad habla, quién es la fuente y con qué permiso. Sirve para explicar por qué la revitalización importa para la identidad sin hablar por todas las personas.",
    prior=["Sé qué significan revitalizar y fortalecer una lengua.", "Sé que la pertenencia a un pueblo no se mide por hablar su lengua."],
    explain=[
        "La identidad es lo que una persona o un pueblo reconoce como propio: su historia, su territorio, su familia, sus costumbres y, muchas veces, su lengua. Revitalizar la lengua es hacer que vuelva a usarse en más lugares y por más personas. Para una persona, aprender o usar su lengua puede ser una forma de sentirse cerca de su familia y de su pueblo.",
        "Pero no todas las personas viven la lengua del mismo modo. Hay quienes la hablan todos los días, quienes la entienden poco y quienes están aprendiéndola. Todas siguen siendo parte de su pueblo. Por eso, al explicar el sentido de la revitalización para la identidad, nunca digo que alguien «es menos» de su pueblo por hablar poco su lengua.",
        "Antes de explicar, ubico el testimonio: pueblo, comunidad, fuente, permiso y límite. En la ficha, la joven habla de su experiencia y aclara que habla solo por ella y su comunidad. Eso significa que su testimonio vale como un ejemplo, no como una regla para todos. Cuido su voz citándola con «según» y sin agregar lo que no dijo.",
    ],
    vocab=[("identidad", "lo que una persona o un pueblo reconoce como propio"), ("testimonio", "relato de lo que una persona vivió"), ("sentirse cerca", "tener un vínculo afectivo con alguien"), ("experiencia", "lo que una persona vive o ha vivido"), ("pertenencia", "ser parte de un pueblo o una comunidad")],
    worked=[
        W("Leer la ficha", FI + " ¿Quién es la fuente y de qué habla?", ["Busco la línea «Fuente».", "Es una joven de la Comunidad Ejemplo que participa en un taller de lengua.", "Habla de cómo aprender su lengua la acerca a su familia."], "una joven de la Comunidad Ejemplo que cuenta cómo aprender la lengua la acerca a su familia"),
        W("Reconocer el límite", FI + " ¿Qué límite declara la joven?", ["Busco la frase final de la ficha.", "Dice que habla solo por ella y su comunidad.", "Ese es el límite."], "habla solo por ella y su comunidad"),
    ],
    mistakes=[
        M("Escribir «los jóvenes mapuche necesitan hablar la lengua para ser parte del pueblo».", "La joven dijo lo contrario.", "Cito su frase y mantengo su sentido."),
        M("Contar el testimonio como si fuera de todas las comunidades.", "La joven habló solo por ella y su comunidad.", "Digo «según una joven de la Comunidad Ejemplo»."),
    ],
    R=[
        ex(FI + " ¿De qué pueblo es la comunidad de la ficha?", "mapuche", "La línea «Pueblo» lo dice."),
        ex(FI + " ¿En qué participa la joven?", "en un taller de lengua", "La ficha lo dice."),
        ex("La identidad, ¿es lo que una persona o un pueblo reconoce como propio o un documento de la escuela?", "lo que una persona o un pueblo reconoce como propio", "Así se definió."),
    ],
    C=[
        ex(FI + " ¿Qué le hace sentir aprender la lengua de su pueblo a la joven?", "más cerca de su familia", "Lo dice en su testimonio."),
        ex(FI + " Verdadero o falso: la joven dice que quien habla poco la lengua deja de ser parte del pueblo.", "Falso", "Dice lo contrario."),
        ex(FI + " ¿Quién autoriza contar el testimonio en la sala?", "la joven", "La línea «Autorización» lo dice."),
    ],
    A=[
        ex("Ordena para explicar con el testimonio. A) declaro el límite. B) nombro pueblo, comunidad y fuente. C) cuento lo que dijo con «según». Escribe las letras en orden.", "B, C, A", "Primero ubico, luego cuento y al final declaro el límite."),
        arith(FI + " El taller de lengua se reúne 2 veces por semana. ¿Cuántas veces se reúne en 3 semanas?", "2*3", "Dos veces por semana durante tres semanas."),
        ex(FI + " Elige la mejor frase. A) «Según una joven de la Comunidad Ejemplo, aprender la lengua la hace sentir más cerca de su familia». B) «Los jóvenes mapuche sienten lo mismo». Escribe la letra.", "A", "Atribuye y no generaliza."),
    ],
    Z=[
        ex(FI + " Un compañero dice que, como la joven habla poco su lengua, no pertenece a su pueblo. ¿Es correcto? Sí o No.", "No", "La pertenencia no se mide por hablar la lengua."),
        ex(FI + " ¿La ficha permite decir que todas las personas jóvenes de la comunidad sienten lo mismo que la joven? Sí o No.", "No", "Ella habla solo por sí misma y su comunidad."),
    ],
    D=[
        ex(FI + " Dos formas de empezar la explicación. A) «Según una joven de la Comunidad Ejemplo…». B) «Todo el mundo sabe que…». ¿Cuál atribuye? Escribe la letra.", "A", "Nombra a la fuente."),
        ex("Una persona de tu comunidad te cuenta cómo su lengua la acerca a su familia y te pide que no lo cuentes en el curso. ¿Lo cuentas o respetas su petición?", "respetas su petición", "Los testimonios se cuentan con permiso."),
    ],
    context=[ex("Un familiar te dice que está aprendiendo la lengua de su pueblo y que lo hace sentir cerca de sus abuelos. Quieres contarlo en tu curso. ¿Qué haces primero: pedirle permiso o contarlo igual?", "pedirle permiso", "Un testimonio se cuenta con autorización.")],
    selfcheck=[
        ex("¿Quién decide cómo vive su lengua cada persona: otra persona o ella misma?", "ella misma", "Cada persona vive su identidad a su manera."),
        ex("Hablar poco la lengua de mi pueblo, ¿me hace menos parte de él? Sí o No.", "No", "La pertenencia no se mide así."),
        ex("¿Qué palabra uso para citar la fuente: «según» o «siempre»?", "según", "La palabra según atribuye lo dicho."),
    ],
    task=T(
        "Lee esta ficha inventada: «Pueblo: aymara. Comunidad Muestra. Fuente: un joven que participa en un grupo de lectura en la lengua. Autorización: puede contarse en la sala. Dijo: «Leer en nuestra lengua me ayuda a conocer mejor la historia de mi familia. Nadie debería sentirse menos por no hablarla». Habla solo por él.» En tu cuaderno completa una ficha con cinco líneas (pueblo y comunidad, fuente, permiso, qué dijo, límite) y escribe dos oraciones que cuenten su testimonio con «según», sin agregar nada.",
        "Pueblo: aymara; Comunidad Muestra. Fuente: un joven del grupo de lectura. Permiso: sí. Dijo: leer en la lengua lo ayuda a conocer la historia de su familia y nadie debería sentirse menos por no hablarla. Límite: habla solo por él. Oraciones: «Según un joven de la Comunidad Muestra, leer en la lengua lo ayuda a conocer mejor la historia de su familia. Él habla solo por sí mismo.»",
        ["completa las cinco líneas", "cuenta con «según»", "no agrega datos", "declara el límite"],
        ["ficha de cinco líneas", "dos oraciones"],
        ["generalizar a todos los jóvenes", "agregar datos que la ficha no dice"],
        "Si generaliza, pídele que agregue «según un joven de la Comunidad Muestra» al comienzo.",
    ),
    reinforce="Relee la ficha del testimonio y subraya con colores el pueblo, la fuente y el límite.",
    extend="Escribe una ficha inventada de testimonio sobre lengua e identidad con las cinco líneas y márcala como inventada.",
)

# ============================================================ LS05 clase 2 · escuchar un relato con límites
REL = "Relato oral (inventado para practicar; lo lee una persona adulta): «Mi abuelo me cuenta que cuando él era niño la lengua se hablaba más en la casa. Yo la escucho en el taller de los jueves y en un programa de radio. Pienso que, si más personas la escuchan, habrá más ganas de aprenderla. En mi curso usamos palabras como guagua y palta, que vienen de lenguas indígenas, y eso me hace pensar que las lenguas se mezclan. Hablo solo de mi casa y de mi taller». (Una niña de la Comunidad Muestra, inventada)."

L(
    LS5, 2,
    materials="Lápiz y hoja. El relato oral está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta en voz alta.",
    use="Aprenderé a escuchar un relato sobre cómo vive una persona su lengua y a separar los hechos que cuenta, las opiniones que da y los límites que declara. Sirve para explicar el sentido de la revitalización con fidelidad.",
    prior=["Sé situar un testimonio sobre identidad y lengua.", "Sé que algunos préstamos del castellano vienen de lenguas indígenas."],
    explain=[
        "Al escuchar un relato personal sobre la lengua anoto tres cosas: los hechos que cuenta, las opiniones que da y los límites que declara. Los hechos son lo que ocurre o ha ocurrido, como que hay un taller los jueves y un programa de radio. Las opiniones son lo que la persona cree, como «habrá más ganas de aprenderla si más personas la escuchan». Los límites son los avisos, como «hablo solo de mi casa y de mi taller».",
        "En el relato aparece también una idea sobre las palabras: la niña dice que en su curso usan «guagua» y «palta», que vienen de lenguas indígenas, y que eso le hace pensar que las lenguas se mezclan. Es una observación suya y la cito como suya. «Guagua» y «palta» son préstamos del quechua al castellano de Chile, y eso se puede decir como dato general.",
        "No uso el relato para decir qué pasa en todas las casas ni para decir que la lengua «ya está salvada». Tampoco agrego opiniones mías como si fueran suyas. Si algo me genera dudas, lo anoto para preguntárselo a ella o al educador o la educadora tradicional.",
    ],
    vocab=[("relato oral", "historia que se cuenta en voz alta"), ("hecho", "algo que ocurre u ocurrió"), ("opinión", "lo que alguien cree o piensa"), ("préstamo", "palabra que una lengua toma de otra"), ("quechua", "lengua del pueblo quechua")],
    worked=[
        W("Separar hecho y opinión", REL + " ¿«Hay un taller los jueves» es hecho u opinión?", ["Busco la frase en el relato.", "La niña lo cuenta como algo que ocurre.", "No usa «pienso» ni «creo»."], "es un hecho que cuenta la niña"),
        W("Reconocer el límite", REL + " ¿Qué límite declara la niña?", ["Busco la última frase.", "Dice que habla solo de su casa y de su taller.", "Ese es el límite."], "habla solo de su casa y de su taller"),
    ],
    mistakes=[
        M("Escribir «la niña dice que ya hay muchas personas que hablan la lengua».", "Ella no dijo eso.", "Cito solo lo que dijo."),
        M("Contar su observación sobre palabras como si fuera un dato de todos los pueblos.", "Es una observación suya.", "La atribuyo con «según»."),
    ],
    R=[
        ex(REL + " ¿Qué día es el taller de la niña?", "los jueves", "El relato lo dice."),
        ex(REL + " ¿Dónde se hablaba más la lengua cuando el abuelo era niño?", "en la casa", "El relato lo dice."),
        ex(REL + " ¿Qué dos palabras menciona la niña que vienen de lenguas indígenas?", "guagua y palta", "El relato las nombra."),
    ],
    C=[
        ex(REL + " ¿«Habrá más ganas de aprenderla si más personas la escuchan» es un hecho o una opinión de la niña?", "una opinión de la niña", "Empieza con «pienso»."),
        ex(REL + " ¿Qué límite declara la niña al final?", "que habla solo de su casa y de su taller", "Lo dice con esas palabras."),
        ex(REL + " Verdadero o falso: el relato dice que la lengua ya está salvada.", "Falso", "No lo dice."),
    ],
    A=[
        ex(REL + " Clasifica cada frase como H (hecho), O (opinión) o L (límite). 1) Escucha la lengua en un programa de radio. 2) Cree que habrá más ganas de aprenderla. 3) Habla solo de su casa y su taller. Escribe las tres letras.", "1 H, 2 O, 3 L", "Cada frase cumple una de las tres funciones."),
        arith("Una niña anotó 10 frases de un relato. 6 son hechos, 3 son opiniones y el resto son límites. ¿Cuántas frases son límites?", "10-6-3", "Se restan hechos y opiniones del total."),
        ex(REL + " Ordena lo que haces al escuchar. A) declaro el límite. B) anoto lo que cuenta. C) anoto lo que pienso yo. Escribe las letras en orden.", "B, C, A", "Primero lo dicho, luego lo mío y al final el límite."),
    ],
    Z=[
        ex(REL + " Un compañero escribe: «En todos los talleres de lengua se escuchan palabras como guagua y palta». ¿Respeta el límite? Sí o No.", "No", "La niña habla solo de su casa y su taller."),
        ex(REL + " ¿Qué conviene si no entiendes por qué la niña dice que las lenguas se mezclan: adivinar o preguntarle?", "preguntarle", "Adivinar puede cambiar lo que quiso decir."),
    ],
    D=[
        ex(REL + " Elige el mejor resumen. A) «Según una niña de la Comunidad Muestra, escucha la lengua en un taller y en la radio; cree que más personas escuchándola darán más ganas de aprenderla; habla solo de su casa y su taller». B) «La lengua se salvó gracias a la radio». Escribe la letra.", "A", "Atribuye, distingue opinión y mantiene el límite."),
        ex("Una persona mayor te cuenta cómo cambió el uso de su lengua en su familia y te pide que no repitas una parte. ¿Cómo la tratas al escribir: la incluyes o la dejas fuera?", "la dejas fuera", "Se respeta lo que pidió."),
    ],
    context=[ex("Una vecina te dice: «Antes se usaba más la lengua; ahora hay un programa de radio». Al contarlo, ¿empiezas con «según una vecina…» o lo cuentas como un dato de toda la región?", "empiezas con «según una vecina…»", "Se atribuye a su fuente y se mantiene el alcance.")],
    selfcheck=[
        ex("¿«Pienso que» introduce un hecho o una opinión?", "una opinión", "Muestra lo que alguien piensa."),
        ex("¿«Guagua» es un préstamo del quechua al castellano? Sí o No.", "Sí", "Es una palabra de origen quechua usada en el castellano de Chile."),
        ex("Si la fuente dice «hablo solo de mi casa», ¿puedo hablar por otras casas con su relato? Sí o No.", "No", "Ese es su límite."),
    ],
    task=T(
        "Una persona adulta te lee este relato inventado: «Un joven de la Comunidad Ejemplo cuenta que en su casa se usa la lengua para saludar y que su club de lectura se reúne dos veces al mes. Cree que la lengua se fortalece cuando se usa en cosas de hoy, como los juegos. Dice que en su curso dicen «choclo» y «poroto», palabras que vienen de lenguas indígenas. Aclara que habla solo por su casa y su club.» En tu cuaderno haz tres listas: hechos, opiniones y límites. Luego escribe una frase con «según» que respete su límite.",
        "Hechos: en su casa se saluda con la lengua; el club se reúne dos veces al mes; en su curso dicen choclo y poroto. Opinión: la lengua se fortalece cuando se usa en cosas de hoy. Límite: habla solo por su casa y su club. Frase: «Según un joven de la Comunidad Ejemplo, su club de lectura se reúne dos veces al mes; él habla solo por su casa y su club.»",
        ["separa hechos, opinión y límite", "usa «según»", "no agrega datos", "respeta el límite"],
        ["tres listas escritas", "frase con «según»"],
        ["mezclar opinión con hechos", "borrar el límite"],
        "Si mezcla, pídele que subraye verbos como «cree» y vea a qué lista llevan.",
    ),
    reinforce="Relee el relato de la niña y subraya con tres colores hechos, opinión y límite.",
    extend="Escribe un relato breve de cuatro oraciones sobre cómo usas palabras de origen indígena en tu día, con un hecho, una opinión y un límite.",
)

# ============================================================ LS05 clase 3 · préstamos de uso cotidiano
PRE = "Lista de palabras de uso cotidiano en Chile (los orígenes son reales y muy conocidos): guagua (quechua), palta (quechua), choclo (quechua), poroto (quechua), cancha (quechua), pampa (quechua), puma (quechua), copihue (mapuzugun), curanto (mapuzugun), tomate (náhuatl), chicle (náhuatl), maíz (taíno), canoa (taíno), fútbol (inglés), clic (inglés)."

L(
    LS5, 3,
    materials="Lápiz y hoja. La lista de palabras está escrita aquí. No necesitas dispositivos.",
    use="Aprenderé a reconocer préstamos de uso cotidiano que el castellano tomó de lenguas indígenas y de otras lenguas, y a explicar por qué su existencia no resta valor a ninguna lengua. Sirve para entender que las lenguas conviven y se renuevan.",
    prior=["Sé qué es un préstamo y qué es un neologismo.", "Sé que cada lengua pertenece a un pueblo."],
    explain=[
        "Un préstamo lingüístico es una palabra que una lengua toma de otra. El castellano de Chile tiene muchos préstamos de lenguas indígenas: «guagua», «palta», «choclo», «poroto» y «cancha» vienen del quechua; «copihue» y «curanto» vienen del mapuzugun; «tomate» y «chicle» vienen del náhuatl; «maíz» y «canoa» vienen del taíno. También hay préstamos del inglés, como «fútbol» y «clic».",
        "Estos préstamos son de uso cotidiano: los decimos en la casa, en la escuela y en la feria. Reconocerlos permite ver que las lenguas indígenas están presentes en nuestra vida diaria. Sin embargo, usar palabras indígenas en castellano no reemplaza hablar la lengua de un pueblo. Aprender la lengua es una tarea de revitalización que cada comunidad decide y organiza.",
        "Las lenguas conviven y se renuevan. Cuando una lengua toma palabras de otra, no pierde valor ni deja de ser suya. Al explicar esto, no digo que unas lenguas sean más importantes que otras. Solo describo de dónde vienen las palabras y qué nos muestra eso: que los pueblos y las lenguas han estado en contacto durante mucho tiempo.",
    ],
    vocab=[("préstamo lingüístico", "palabra que una lengua toma de otra"), ("náhuatl", "lengua de pueblos de México"), ("taíno", "lengua de pueblos del Caribe"), ("quechua", "lengua del pueblo quechua"), ("convivir", "existir juntas y relacionarse")],
    worked=[
        W("Reconocer el origen", PRE + " ¿De qué lengua viene «choclo»?", ["Busco «choclo» en la lista.", "Dice quechua.", "Ya se usa en el castellano de Chile."], "del quechua"),
        W("Explicar por qué importan", PRE + " ¿Qué nos muestra que «copihue» y «curanto» vengan del mapuzugun?", ["Son palabras de uso cotidiano en Chile.", "Vienen de la lengua de un pueblo.", "Muestran que las lenguas indígenas están presentes en la vida diaria."], "que el mapuzugun está presente en la vida diaria del castellano de Chile"),
    ],
    mistakes=[
        M("Decir que usar «palta» ya es hablar quechua.", "Una palabra no equivale a hablar una lengua.", "Digo que es un préstamo que el castellano tomó del quechua."),
        M("Decir que el castellano es más importante porque tomó palabras de otras lenguas.", "No se jerarquizan lenguas.", "Explico que las lenguas conviven y se renuevan."),
    ],
    R=[
        ex(PRE + " ¿De qué lengua viene «guagua»?", "del quechua", "La lista lo dice."),
        ex(PRE + " ¿De qué lengua viene «copihue»?", "del mapuzugun", "La lista lo dice."),
        ex(PRE + " ¿De qué lengua viene «fútbol»?", "del inglés", "La lista lo dice."),
    ],
    C=[
        ex(PRE + " ¿De qué lengua viene «tomate»?", "del náhuatl", "La lista lo dice."),
        ex(PRE + " ¿De qué lengua viene «canoa»?", "del taíno", "La lista lo dice."),
        ex("Verdadero o falso: un préstamo lingüístico hace que una lengua deje de ser suya.", "Falso", "Las lenguas toman palabras y siguen siendo suyas."),
    ],
    A=[
        ex(PRE + " Clasifica cada palabra por origen: Q (quechua), M (mapuzugun) o I (inglés). 1) pampa. 2) curanto. 3) clic. 4) puma. Escribe las cuatro letras.", "1 Q, 2 M, 3 I, 4 Q", "Pampa y puma vienen del quechua, curanto del mapuzugun y clic del inglés."),
        arith(PRE + " La lista tiene 15 palabras y 2 de ellas vienen del inglés. ¿Cuántas NO vienen del inglés?", "15-2", "Se restan las del inglés del total."),
        ex(PRE + " Cuenta las palabras de la lista que vienen del quechua: guagua, palta, choclo, poroto, cancha, pampa, puma. ¿Cuántas son?", "7", "Son siete palabras.", "1+1+1+1+1+1+1"),
    ],
    Z=[
        ex("Un compañero dice: «Como decimos palta, ya estamos revitalizando el quechua». ¿Es correcto? Sí o No.", "No", "Usar una palabra no equivale a revitalizar una lengua."),
        ex(PRE + " Una niña dice que el castellano de Chile es más importante que el quechua porque tiene palabras de él. ¿Está comparando sin jerarquizar? Sí o No.", "No", "Dice que una lengua vale más que otra."),
    ],
    D=[
        ex(PRE + " Elige la mejor explicación. A) «Los préstamos como guagua, palta y copihue muestran que las lenguas indígenas están presentes en el castellano de Chile y que las lenguas conviven». B) «Los préstamos indican que el castellano no tiene palabras propias». Escribe la letra.", "A", "Describe sin jerarquizar."),
        ex("Una persona mayor te dice que una palabra de tu región viene de una lengua indígena, pero no está en la lista. ¿La anotas como dato de la persona o la afirmas como seguro?", "la anotas como dato de la persona", "Se atribuye hasta confirmarla con una fuente."),
    ],
    context=[ex("En la feria oyes «choclo», «palta» y «poroto». Alguien dice que son palabras «sin origen». ¿Qué le dices: que vienen del quechua o que no tienen origen?", "que vienen del quechua", "La lista dice su origen.")],
    selfcheck=[
        ex("¿«Maíz» viene del taíno o del inglés?", "del taíno", "La lista lo dice."),
        ex("¿Un préstamo hace menos valiosa a una lengua? Sí o No.", "No", "Todas las lenguas toman y crean palabras."),
        ex("¿Usar palabras de origen indígena en castellano reemplaza aprender la lengua de un pueblo? Sí o No.", "No", "Son cosas distintas."),
    ],
    task=T(
        "Usa la lista de palabras de esta clase. En tu cuaderno haz una tabla de tres columnas: palabra, lengua de origen y una oración en castellano con esa palabra, para cinco palabras de la lista (por ejemplo: choclo, copihue, tomate, canoa, clic). Luego escribe dos oraciones que expliquen por qué usar palabras indígenas en castellano no reemplaza la revitalización de una lengua y por qué un préstamo no resta valor a una lengua.",
        "Choclo, quechua, «Comimos choclo en la feria». Copihue, mapuzugun, «El copihue es una flor». Tomate, náhuatl, «Compramos tomates». Canoa, taíno, «Había una canoa en la laguna». Clic, inglés, «Hice clic en el dibujo». Explicación: «Decir una palabra no es hablar la lengua; la revitalización la organizan las comunidades. Un préstamo no resta valor porque todas las lenguas toman palabras y siguen siendo suyas.»",
        ["completa cinco filas con origen correcto", "escribe oraciones en castellano", "explica por qué no reemplaza la revitalización", "no jerarquiza lenguas"],
        ["tabla de tres columnas", "dos oraciones de explicación"],
        ["afirmar un origen que no está en la lista", "jerarquizar lenguas"],
        "Si duda de un origen, pídele que lo busque en la lista de la clase.",
    ),
    reinforce="Copia la lista de palabras y colorea con un color distinto cada lengua de origen.",
    extend="Pregunta en tu casa por tres palabras que se usen mucho y compara con la lista para ver si alguna aparece.",
)

# ============================================================ LS05 clase 4 · explicación atribuida
FX = "Ficha de explicación (inventada para practicar): Fuente: una educadora tradicional de la Escuela Ejemplo, pueblo mapuche. Autorización: puede contarse en la sala. Dijo: «En el taller de lengua aprendemos saludos y juegos. Muchos niños sienten que, al usar la lengua, se acercan a sus familias. También usamos palabras como copihue y curanto, que vienen de nuestra lengua y hoy forman parte del castellano de Chile. Hablo solo de mi escuela»."

L(
    LS5, 4,
    materials="Lápiz y hoja. La ficha de explicación está escrita aquí y es inventada para practicar.",
    use="Aprenderé a escribir una explicación de cinco oraciones sobre el sentido que tiene revitalizar o fortalecer una lengua para la propia identidad, con ejemplos de préstamos de uso cotidiano y con atribución y límite. Sirve para explicar sin generalizar.",
    prior=["Sé separar hechos, opiniones y límites.", "Sé reconocer préstamos de uso cotidiano."],
    explain=[
        "Una explicación atribuida tiene cinco partes. Primero nombra la fuente con «según». Segundo, cuenta qué hace la comunidad por su lengua. Tercero, explica el sentido para la identidad usando lo que dijo la fuente, por ejemplo que los niños se acercan a sus familias. Cuarto, da un ejemplo de préstamo de uso cotidiano de la ficha o del cuadro de la clase. Quinto, declara el límite.",
        "Un ejemplo de préstamo debe salir de la ficha o de la lista de la clase, no de mi memoria. En la ficha, la educadora nombra «copihue» y «curanto», que vienen del mapuzugun y hoy forman parte del castellano de Chile. Puedo usarlos como ejemplos. No agrego palabras en lengua indígena que la ficha no entregó.",
        "Mi opinión va aparte, marcada con «yo pienso». Puedo escribir «yo pienso que usar la lengua en muchos lugares ayuda a que más personas se acerquen a ella», pero sin decir que lo dijo la educadora. Antes de entregar, le pido a la educadora tradicional que lea mi explicación y confirme que respeta lo que enseñó.",
    ],
    vocab=[("sentido", "razón o propósito de una acción"), ("identidad", "lo que una persona o un pueblo reconoce como propio"), ("atribuir", "decir de quién viene la información"), ("ejemplo", "caso concreto que aclara una idea"), ("límite", "aviso de hasta dónde vale lo dicho")],
    worked=[
        W("Escribir la primera oración", FX + " Escribe una oración que nombre la fuente y lo que hace la comunidad.", ["Tomo los datos de la ficha: educadora tradicional de la Escuela Ejemplo; taller de lengua con saludos y juegos.", "Empiezo con «Según…».", "Escribo la oración."], "Según una educadora tradicional de la Escuela Ejemplo, en el taller de lengua se aprenden saludos y juegos."),
        W("Elegir el ejemplo de préstamo", FX + " ¿Qué ejemplos de préstamos da la educadora?", ["Busco palabras que vienen de su lengua y están en el castellano de Chile.", "La ficha nombra «copihue» y «curanto».", "Esos son los ejemplos."], "copihue y curanto"),
    ],
    mistakes=[
        M("Agregar «y todos los niños del taller hablan fluido».", "La ficha no lo dice.", "Escribo solo lo que dijo la educadora."),
        M("Terminar sin el límite.", "Parece que vale para todas las escuelas.", "Cierro con «ella habla solo de su escuela»."),
    ],
    R=[
        ex(FX + " ¿Qué aprenden en el taller de lengua?", "saludos y juegos", "La educadora lo dice."),
        ex(FX + " ¿Qué dos palabras menciona como parte de su lengua que hoy son castellano de Chile?", "copihue y curanto", "La ficha las nombra."),
        ex(FX + " ¿De qué escuela es la educadora?", "de la Escuela Ejemplo", "La ficha la nombra."),
    ],
    C=[
        ex(FX + " ¿Qué sienten muchos niños al usar la lengua según la educadora?", "que se acercan a sus familias", "La ficha lo dice."),
        ex(FX + " ¿Cuál es el límite que declara la educadora?", "habla solo de su escuela", "Cierra con esa frase."),
        ex(FX + " Verdadero o falso: la ficha dice que todos los pueblos hacen talleres de lengua.", "Falso", "No lo dice."),
    ],
    A=[
        ex("Ordena las cinco partes de la explicación. A) límite. B) ejemplo de préstamo. C) fuente con «según». D) sentido para la identidad. E) lo que hace la comunidad. Escribe las letras en orden.", "C, E, D, B, A", "Se parte por la fuente y se cierra con el límite."),
        ex(FX + " Elige la mejor oración del sentido. A) «Según la educadora, muchos niños sienten que, al usar la lengua, se acercan a sus familias». B) «Todos los niños indígenas sienten lo mismo». Escribe la letra.", "A", "Atribuye y no generaliza."),
        arith("Una explicación debe tener 5 partes. Un grupo escribió la fuente y el ejemplo. ¿Cuántas partes faltan?", "5-2", "Se restan las escritas de las cinco pedidas."),
    ],
    Z=[
        ex(FX + " Una niña agrega: «y los niños que no hablan la lengua no pertenecen al pueblo». ¿La ficha lo dice o lo respeta? Responde Sí o No a si es correcto escribirlo.", "No", "La pertenencia no se mide por hablar la lengua."),
        ex(FX + " Un niño escribe «yo pienso que usar la lengua en muchos lugares ayuda a que más personas se acerquen». ¿Marcó su idea como propia? Sí o No.", "Sí", "Empieza con «yo pienso»."),
    ],
    D=[
        ex(FX + " Dos versiones del cierre. A) «La educadora habla solo de su escuela». B) «Así son todas las escuelas mapuche». ¿Cuál respeta el límite? Escribe la letra.", "A", "La B generaliza."),
        ex("Al revisar tu explicación notas una palabra mapuzugun que la ficha no entregó. ¿La dejas o la sacas y consultas?", "la sacas y consultas", "Solo se usan las palabras que la fuente entregó."),
    ],
    context=[ex("Tu curso presentará qué hace una comunidad por su lengua. Una persona mayor te dio su permiso. ¿Empiezas con «Según…» y su comunidad, o lo presentas como tu propia investigación?", "empiezas con «Según…» y su comunidad", "Se atribuye a quien lo entregó.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Cuántas partes tiene la explicación de esta clase?", "5", "Fuente, acción, sentido, ejemplo y límite."),
        ex("¿Puedo agregar palabras en lengua que la ficha no tiene? Sí o No.", "No", "No se inventa lengua."),
        ex("¿Qué marca mi opinión: «yo pienso» o «según»?", "yo pienso", "«Según» atribuye a la fuente."),
    ],
    task=T(
        "Lee esta ficha inventada: «Fuente: un educador tradicional de la Escuela Muestra, pueblo rapa nui. Autorización: puede contarse en la sala. Dijo: «En el taller de lengua hacemos canciones nuevas. Los jóvenes dicen que así sienten más suya la lengua. En el castellano de Chile usamos palabras como canoa, que viene del taíno, y es parte de la vida diaria. Hablo solo de mi taller»». En tu cuaderno escribe una explicación de cinco oraciones con estas partes: fuente, lo que hace la comunidad, sentido para la identidad, ejemplo de préstamo y límite. No agregues palabras en lengua indígena que la ficha no tenga.",
        "Según un educador tradicional de la Escuela Muestra, del pueblo rapa nui, en el taller de lengua se hacen canciones nuevas. Los jóvenes dicen que así sienten más suya la lengua. Un ejemplo de préstamo de uso cotidiano es «canoa», que viene del taíno. Él habla solo de su taller. Yo pienso que cantar ayuda a que la lengua se sienta cercana.",
        ["nombra la fuente y el pueblo", "usa el ejemplo de la ficha", "explica el sentido para la identidad", "declara el límite y marca lo propio"],
        ["explicación de cinco oraciones"],
        ["inventar palabras en lengua", "olvidar el límite"],
        "Pide que subraye en la ficha cada dato que usó; todo lo no subrayado debe llevar «yo pienso» o salir.",
    ),
    reinforce="Copia las cinco oraciones del ejemplo y rotula cada una con el número de su parte.",
    extend="Escribe una segunda explicación del mismo taller para las familias, con las cinco partes.",
)


# ============================================================ LS06 clase 1 · situar la creación
IDEA1 = "Idea 1 (inventada para practicar): un audio de 90 segundos en el que un estudiante cuenta cómo prepara el desayuno con su familia, usando las palabras «palta» y «choclo». Aparece la voz de un familiar. Se graba con la grabadora del celular de la casa."
IDEA2 = "Idea 2 (inventada): un cartel dibujado en papel sobre la feria del barrio, que incluye «mari mari» como saludo en la parte de arriba, autorizado por el educador tradicional. No aparece ninguna persona."
IDEA3 = "Idea 3 (inventada): un video sobre una ceremonia que el grupo vio en la escuela. Quiere mostrar la ceremonia con detalle y no tiene el permiso de quienes la organizaron."

L(
    LS6, 1,
    materials="Lápiz y hoja. Las tres ideas están escritas aquí y son inventadas para practicar. No necesitas ningún dispositivo.",
    use="Aprenderé a situar una creación audiovisual o escrita en castellano que incorpora palabras en lengua indígena: qué situación personal, familiar o comunitaria cuenta, con qué recurso, con qué palabras y con qué permisos. Sirve para comenzar un trabajo creativo con respeto.",
    prior=["Sé que cada palabra en lengua indígena necesita una fuente.", "Sé que la voz y la imagen de una persona se usan con su permiso."],
    explain=[
        "Una creación en castellano puede incorporar palabras en lengua indígena. Pueden ser palabras ya incorporadas al castellano, como «palta» o «choclo», o expresiones que una fuente me entregó, como «mari mari». Antes de crear me hago cuatro preguntas: ¿qué situación cuento?, ¿con qué recurso?, ¿qué palabras uso y de dónde vienen?, ¿a quién muestro y con qué permiso?",
        "Los recursos TIC son los que están disponibles: la grabadora de un celular, un computador de la escuela o, si no hay nada de eso, papel y lápices. Una creación en papel vale igual. Lo importante es que cuente una situación auténtica y respete a las personas.",
        "Hay cosas que no se muestran sin permiso: la voz o la cara de una persona, los datos personales y las ceremonias. Si una idea depende de mostrar algo sin permiso, la cambio o la detengo. También cuido que las palabras en lengua vengan de una fuente, y no de una página que vi, porque pueden estar mal escritas.",
    ],
    vocab=[("creación", "trabajo que hago para contar algo, como un audio o un cartel"), ("TIC", "recursos tecnológicos para informar y comunicar"), ("situación auténtica", "algo real de mi vida, mi familia o mi comunidad"), ("permiso", "autorización de una persona para mostrar su voz, cara o nombre"), ("recurso disponible", "lo que tengo a mano para crear")],
    worked=[
        W("Analizar una idea completa", IDEA1 + " ¿Qué situación cuenta y qué permiso necesita?", ["Cuenta una situación familiar: el desayuno.", "Aparece la voz de un familiar.", "Necesita el permiso de ese familiar."], "una situación familiar y el permiso del familiar cuya voz aparece"),
        W("Detectar lo que falta", IDEA3 + " ¿Por qué esta idea no puede seguir así?", ["Busco qué permiso falta.", "No tiene el permiso de quienes organizaron la ceremonia.", "Una ceremonia no se muestra sin su permiso."], "porque falta el permiso de quienes organizaron la ceremonia"),
    ],
    mistakes=[
        M("Grabar primero y pedir permiso después.", "Ya se usó la voz o la imagen sin autorización.", "Pido el permiso antes de grabar."),
        M("Poner una palabra en lengua porque la vi escrita en internet.", "Puede estar mal o ser de otro pueblo.", "Uso solo palabras que una fuente me entregó."),
    ],
    R=[
        ex(IDEA1 + " ¿Cuántos segundos dura el audio de la idea 1?", "90", "La idea lo dice."),
        ex(IDEA2 + " ¿Qué recurso usa la idea 2?", "papel", "Es un cartel dibujado en papel."),
        ex(IDEA2 + " ¿Qué saludo incluye el cartel?", "mari mari", "La idea lo dice."),
    ],
    C=[
        ex(IDEA1 + " ¿Qué dos palabras usa la idea 1?", "palta y choclo", "La idea las nombra."),
        ex(IDEA3 + " ¿Qué permiso falta en la idea 3?", "el de quienes organizaron la ceremonia", "La idea lo dice."),
        ex("Verdadero o falso: si no hay celular ni computador, no se puede hacer esta creación.", "Falso", "Un cartel en papel también sirve."),
    ],
    A=[
        ex("Ordena los pasos para comenzar una creación. A) pedir los permisos. B) elegir el recurso. C) decidir la situación que cuento. D) elegir las palabras en lengua con su fuente. Escribe las letras en orden.", "C, B, D, A", "Primero qué cuento y con qué, luego las palabras y los permisos."),
        arith(IDEA1 + " El audio de la idea 1 tiene 3 escenas de 30 segundos cada una. ¿Cuántos segundos dura en total?", "3*30", "Tres escenas de treinta segundos."),
        ex(IDEA1 + " " + IDEA2 + " " + IDEA3 + " ¿Cuál de las tres ideas puede seguir sin cambiar nada de lo que dice: la idea 2 o la idea 3?", "la idea 2", "Tiene saludo autorizado y no muestra personas."),
    ],
    Z=[
        ex(IDEA3 + " Un compañero propone seguir con el video y conseguir el permiso después. ¿Es correcto? Sí o No.", "No", "El permiso va antes."),
        ex(IDEA1 + " ¿«Palta» y «choclo» necesitan permiso de una fuente para usarse? Sí o No.", "No", "Ya son palabras del castellano de Chile."),
    ],
    D=[
        ex(IDEA2 + " El grupo quiere agregar otra frase en mapuzugun a su cartel. El educador solo autorizó «mari mari». ¿Qué debe hacer: agregarla o consultarlo?", "consultarlo", "La autorización cubre solo la expresión revisada."),
        arith("De 28 estudiantes, 17 trajeron el permiso de su familia para un audio. ¿Cuántos faltan?", "28-17", "Se restan los permisos entregados del total."),
    ],
    context=[ex("Quieres hacer un audio sobre una comida de tu familia con una persona mayor hablando. ¿Qué haces antes de grabar: le pides permiso a esa persona o lo grabas y se lo cuentas después?", "le pides permiso a esa persona", "La voz de una persona se graba con su permiso.")],
    selfcheck=[
        ex("¿Una creación puede hacerse en papel? Sí o No.", "Sí", "Se usan los recursos disponibles."),
        ex("¿Dónde consigo una expresión en lengua indígena: de una fuente o de cualquier página?", "de una fuente", "La fuente confirma que está bien."),
        ex("¿Pido el permiso antes o después de grabar?", "antes", "Así no se usa nada sin autorización."),
    ],
    task=T(
        "Lee esta idea inventada: «Una estudiante quiere hacer un cartel digital o dibujado sobre la feria de su barrio. Quiere usar «choclo» y «copihue» en el texto y el saludo «mari mari», que todavía no sabe si el educador tradicional se lo autoriza. En la feria hay una vendedora que tal vez salga en una foto.» En tu cuaderno responde cuatro preguntas: qué situación cuenta, qué recurso usará, qué palabras necesitan una fuente y qué permiso necesita. Escribe también dos cosas que debe hacer antes de crear.",
        "Situación: comunitaria, la feria del barrio. Recurso: papel o el computador de la escuela. Palabras que necesitan fuente: «mari mari»; «choclo» y «copihue» ya son castellano de Chile. Permiso: el de la vendedora si sale su imagen. Antes de crear: consultar al educador tradicional por «mari mari» y pedir permiso a la vendedora, o usar un dibujo en vez de foto.",
        ["responde las cuatro preguntas", "distingue palabras que necesitan fuente", "pide el permiso", "no inventa lengua"],
        ["cuatro respuestas escritas", "lista de dos pasos"],
        ["usar una foto sin permiso", "usar «mari mari» sin consultar"],
        "Si propone usar la foto de la vendedora sin permiso, ofrécele cambiarla por un dibujo.",
    ),
    reinforce="Vuelve a leer las tres ideas y escribe al lado de cada una si puede seguir o debe cambiar y por qué.",
    extend="Escribe una idea tuya de creación que cuente una situación familiar, con las cuatro preguntas respondidas.",
)

# ============================================================ LS06 clase 2 · leer un texto narrado modelo con límites
NAR = "Texto narrado modelo (inventado para practicar): audio de 60 segundos con tres partes. Parte 1 (15 segundos): «Mari mari. Soy una estudiante del 6.º E.» (el educador tradicional autorizó el saludo). Parte 2 (30 segundos): «En mi casa los sábados comemos choclo y palta en la plaza con una persona de mi casa. Después jugamos a la cancha.» Parte 3 (15 segundos): «Chaltumay por escucharme.» (también autorizado). No se dan nombres completos ni direcciones."

L(
    LS6, 2,
    materials="Lápiz y hoja. El texto narrado modelo está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta.",
    use="Aprenderé a leer un texto narrado en castellano que incluye palabras en lengua indígena, para ver sus partes, el tiempo de cada una, las palabras autorizadas y los datos que no se publican. Sirve para escribir y grabar mi propio texto.",
    prior=["Sé situar una creación con recurso, palabras y permisos.", "Sé que «palta», «choclo» y «cancha» son palabras ya incorporadas al castellano."],
    explain=[
        "Un texto narrado es el texto que alguien dice en voz alta para un audio o un video. Para planificarlo lo divido en partes con su duración. El modelo tiene tres: saludo de 15 segundos, relato de 30 y agradecimiento de 15. Con la duración puedo calcular el total y ajustar el texto si es muy largo.",
        "Después busco las palabras en lengua indígena. «Mari mari» y «chaltumay» son expresiones autorizadas por el educador tradicional. «Choclo», «palta» y «cancha» son palabras de origen quechua ya incorporadas al castellano de Chile, y no necesitan autorización. Cada tipo de palabra se trata distinto: las expresiones se copian tal como la fuente las entregó.",
        "También busco lo que protege a las personas. El modelo no da nombres completos ni direcciones, y la persona de la casa no se identifica. Un buen texto narrado cuenta una experiencia sin entregar datos personales. Si el relato necesita algo que no está autorizado, cambio la frase o la dejo fuera.",
    ],
    vocab=[("texto narrado", "texto que se dice en voz alta en un audio o video"), ("duración", "tiempo que dura algo"), ("dato personal", "dato que identifica a una persona, como su dirección"), ("segundo", "unidad de tiempo; 60 segundos son un minuto"), ("autorizado", "con permiso de la fuente")],
    worked=[
        W("Calcular el tiempo", NAR + " ¿Cuántos segundos suman las tres partes?", ["Anoto las duraciones: 15, 30 y 15.", "Sumo 15 más 30 más 15.", "El total es 60 segundos."], "60 segundos"),
        W("Clasificar palabras", NAR + " ¿«Choclo» es una expresión de la fuente o una palabra ya incorporada al castellano?", ["Busco «choclo» en el texto.", "Es una palabra de origen quechua usada en el castellano de Chile.", "No necesita autorización."], "una palabra ya incorporada al castellano"),
    ],
    mistakes=[
        M("Agregar al texto la dirección de la plaza donde comen.", "Es un dato personal que no se publica.", "Digo «en la plaza» sin dar la dirección."),
        M("Cambiar «chaltumay» por una versión que suena parecida.", "Cambiar la palabra puede alterarla.", "La copio igual que la fuente la entregó."),
    ],
    R=[
        ex(NAR + " ¿Cuántas partes tiene el texto narrado?", "3", "El texto lo dice."),
        ex(NAR + " ¿Qué dura 30 segundos?", "la parte 2, el relato", "El texto lo indica."),
        ex(NAR + " ¿Qué saludo autorizó el educador tradicional?", "mari mari", "El texto lo dice."),
    ],
    C=[
        ex(NAR + " ¿Qué comen en la plaza?", "choclo y palta", "La parte 2 lo dice."),
        ex(NAR + " ¿Se dan nombres completos o direcciones?", "no", "El texto avisa que no."),
        ex(NAR + " Verdadero o falso: «cancha» es una expresión que necesita autorización de la fuente.", "Falso", "Ya es una palabra del castellano de Chile."),
    ],
    A=[
        arith(NAR + " Si se agrega una parte 4 de 20 segundos, ¿cuántos segundos duraría todo el audio?", "60+20", "Se suman los 60 segundos y los 20 nuevos."),
        ex(NAR + " Clasifica cada palabra como E (expresión de la fuente) o C (ya incorporada al castellano). 1) mari mari. 2) choclo. 3) chaltumay. 4) cancha. Escribe las cuatro letras.", "1 E, 2 C, 3 E, 4 C", "Mari mari y chaltumay las entrega la fuente; choclo y cancha ya son castellano."),
        ex(NAR + " Ordena las partes: A) agradecimiento. B) relato. C) saludo. Escribe las letras en orden.", "C, B, A", "Se saluda, se cuenta y se agradece."),
    ],
    Z=[
        ex(NAR + " Un compañero quiere agregar «mi dirección es la calle Sol 123» a la parte 2. ¿Es buena idea? Sí o No.", "No", "Es un dato personal."),
        ex(NAR + " ¿Debe el curso consultar al educador antes de decir «choclo»? Sí o No.", "No", "Es una palabra ya incorporada al castellano."),
    ],
    D=[
        ex(NAR + " Un estudiante cambia la parte 3 por «Maururu por escucharme». ¿Respeta lo autorizado? Sí o No.", "No", "El educador autorizó «chaltumay»."),
        ex(NAR + " Elige la mejor mejora. A) pedir al educador que lea el texto y confirme las expresiones. B) agregar una frase nueva en lengua que alguien dijo en la calle. Escribe la letra.", "A", "Así se confirma que respeta lo autorizado."),
    ],
    context=[ex("Preparas un audio sobre una celebración familiar y quieres nombrar a todos los invitados con su nombre completo. ¿Lo haces o dices «mis familiares»?", "dices «mis familiares»", "Los datos personales no se publican.")],
    selfcheck=[
        ex("¿Cuántos segundos tiene un minuto?", "60", "Un minuto equivale a 60 segundos.", "60"),
        ex("¿Una expresión de la fuente se copia o se cambia a gusto?", "se copia", "Se usa tal como la entregó la fuente."),
        ex("¿Una dirección se publica? Sí o No.", "No", "Es un dato personal."),
    ],
    task=T(
        "Lee este texto narrado inventado: «Audio de 45 segundos. Parte 1 (10 segundos): «Mari mari. Soy un estudiante del 6.º F» (saludo autorizado). Parte 2 (25 segundos): «Los domingos mi familia cocina porotos con choclo y vamos a la pampa a jugar» (una persona de mi casa). Parte 3 (10 segundos): «Chaltumay por escucharme» (autorizado).» En tu cuaderno escribe: las partes con su duración y el total, las expresiones de la fuente, las palabras ya incorporadas al castellano y un dato personal que NO debería agregarse.",
        "Partes: 10 + 25 + 10 = 45 segundos. Expresiones de la fuente: mari mari y chaltumay. Ya incorporadas: porotos, choclo, pampa. Dato personal que no debe agregarse: el nombre completo o la dirección.",
        ["suma correctamente la duración", "separa expresiones de la fuente y palabras incorporadas", "nombra un dato personal", "no inventa expresiones"],
        ["respuestas escritas en el cuaderno"],
        ["confundir palabras incorporadas con expresiones de la fuente", "olvidar los datos personales"],
        "Si confunde los dos tipos, pídele que busque «mari mari» y «chaltumay» en el texto y vea quién las autorizó.",
    ),
    reinforce="Copia el texto narrado modelo en una tabla de tres filas con parte, segundos y qué se dice.",
    extend="Escribe un texto narrado propio de tres partes de 10 segundos cada una, sin ninguna expresión de la fuente, sobre cómo llegas a la escuela.",
)

# ============================================================ LS06 clase 3 · relacionar palabras e imágenes
PAL = "Lista de imágenes y palabras (inventada para practicar), para una creación sobre «El almuerzo del domingo en mi casa»: 1) un dibujo propio de un choclo sobre la mesa, con la palabra «choclo». 2) una foto de un desconocido con un disfraz de «indígena». 3) un dibujo propio de una palta partida, con la palabra «palta». 4) una foto de una ceremonia sacada de internet. 5) un dibujo propio de la mesa servida con la palabra «curanto»."

L(
    LS6, 3,
    materials="Lápiz y hoja. La lista de imágenes y palabras está escrita aquí y es inventada para practicar.",
    use="Aprenderé a relacionar las palabras en lengua indígena que uso con imágenes que las representan de forma respetuosa, y a evitar estereotipos. Sirve para que mi creación cuente una situación real sin caricaturas ni usos indebidos.",
    prior=["Sé planificar una creación con recurso, palabras y permisos.", "Sé que un estereotipo es una imagen simplificada de un grupo de personas."],
    explain=[
        "Cada palabra de mi creación debe relacionarse con una imagen o un sonido que la ayude a entenderse. Si digo «choclo», dibujo un choclo. Si digo «palta», dibujo una palta. La relación entre palabra e imagen debe ser clara y directa, para que quien mire entienda de qué hablo.",
        "Hay imágenes que no debo usar. Un disfraz «de indígena» es un estereotipo: muestra a un pueblo de manera simplificada y como si solo existiera en disfraces. Una foto de una ceremonia sacada de internet puede ser de un acto reservado y yo no tengo el permiso de las personas ni sé de qué pueblo es. Prefiero dibujos propios o fotos de objetos cotidianos.",
        "Además miro que la creación cuente la situación que dije que contaba. Si la creación habla del almuerzo del domingo, las imágenes deben ser del almuerzo, no de cosas que no tienen relación. Y siempre pienso si una imagen respeta a las personas de los pueblos que menciono; si dudo, consulto al educador o a la educadora tradicional.",
    ],
    vocab=[("estereotipo", "imagen simplificada y repetida de un grupo de personas"), ("representar", "mostrar algo con imágenes o palabras"), ("relación", "vínculo claro entre dos cosas"), ("cotidiano", "de todos los días"), ("caricatura", "dibujo exagerado que simplifica a una persona o grupo")],
    worked=[
        W("Relacionar palabra e imagen", PAL + " ¿La imagen 1 se relaciona bien con su palabra?", ["La imagen 1 es un dibujo de un choclo.", "Su palabra es «choclo».", "Imagen y palabra coinciden."], "sí, el dibujo del choclo coincide con la palabra «choclo»"),
        W("Detectar un estereotipo", PAL + " ¿Por qué la imagen 2 no sirve?", ["La imagen 2 muestra un disfraz de «indígena».", "Un disfraz simplifica a un pueblo.", "Eso es un estereotipo."], "porque es un estereotipo: un disfraz no representa a las personas reales"),
    ],
    mistakes=[
        M("Usar una foto de ceremonia de internet porque «se ve muy bien».", "No sé quién la tomó ni si hubo permiso.", "Uso dibujos propios o fotos de objetos cotidianos."),
        M("Decorar con plumas o disfraces para que «se note» lo indígena.", "Es un estereotipo.", "Muestro la situación real con dibujos propios."),
    ],
    R=[
        ex(PAL + " ¿Qué muestra el dibujo de la imagen 3?", "una palta partida", "La lista lo dice."),
        ex(PAL + " ¿Qué palabra acompaña la imagen 5?", "curanto", "La lista lo dice."),
        ex("Un estereotipo, ¿es una imagen simplificada y repetida de un grupo de personas o una foto muy clara?", "una imagen simplificada y repetida de un grupo de personas", "Así se definió."),
    ],
    C=[
        ex(PAL + " ¿Qué imagen es un estereotipo?", "la 2", "El disfraz simplifica a un pueblo."),
        ex(PAL + " ¿Qué imagen puede ser de un acto reservado y no tiene permiso?", "la 4", "Es una foto de ceremonia sacada de internet."),
        ex("Verdadero o falso: una imagen respetuosa se relaciona de forma clara con la palabra que acompaña.", "Verdadero", "Ayuda a entender de qué se habla."),
    ],
    A=[
        ex(PAL + " Escribe los números de las dos imágenes que no se deben usar.", "la 2 y la 4", "Una es un estereotipo y la otra una foto sin permiso."),
        arith(PAL + " La lista tiene 5 imágenes y 2 no se pueden usar. ¿Cuántas imágenes se pueden usar?", "5-2", "Se restan las dos del total."),
        ex(PAL + " Une cada palabra con su imagen. Palabras: 1) choclo. 2) palta. Imágenes: A) dibujo de la mesa servida. B) dibujo de una palta partida. C) dibujo de un choclo sobre la mesa. Escribe los dos pares.", "1-C, 2-B", "Cada palabra se relaciona con la imagen que la muestra."),
    ],
    Z=[
        ex(PAL + " Un compañero defiende la imagen 2 porque es colorida. ¿Resuelve eso el problema del estereotipo? Sí o No.", "No", "El problema es que simplifica a un pueblo."),
        ex("Para mostrar una celebración familiar, ¿conviene más un dibujo propio de la mesa o un disfraz comprado? Escribe cuál.", "un dibujo propio de la mesa", "Cuenta la situación real."),
    ],
    D=[
        ex(PAL + " Pedro dice que puede usar la imagen 4 si escribe debajo «foto de internet». ¿Resuelve el permiso esa nota? Sí o No.", "No", "La nota no da el permiso de las personas."),
        ex("Quieres incluir una palabra en lengua indígena que no sabes cómo dibujar. ¿La ilustras con lo que imaginas o consultas al educador o a la educadora tradicional?", "consultas al educador o a la educadora tradicional", "No se ilustra con suposiciones algo cuyo sentido no se conoce."),
    ],
    context=[ex("Haces un cartel sobre la feria y alguien propone pintar caras con rayas «indígenas». ¿Lo haces o muestras la feria como realmente es?", "muestras la feria como realmente es", "Evita el estereotipo.")],
    selfcheck=[
        ex("¿Un disfraz representa a las personas de un pueblo o una idea simplificada?", "una idea simplificada", "Es un estereotipo."),
        ex("¿Palabra e imagen deben relacionarse? Sí o No.", "Sí", "Así se entiende mejor."),
        ex("¿Una foto de ceremonia sin permiso se puede usar? Sí o No.", "No", "Falta el permiso."),
    ],
    task=T(
        "Lee esta lista inventada de imágenes y palabras para una creación sobre «La merienda en mi casa»: 1) dibujo propio de un bebé con la palabra «guagua». 2) foto de unas personas que no conoces con ropa «tradicional» sacada de internet. 3) dibujo propio de unos porotos con la palabra «poroto». 4) un dibujo propio de la mesa con la palabra «mapuzugun» sin explicación. En tu cuaderno marca las imágenes que no se deben usar y por qué, y corrige una imagen que se puede mejorar, con un dibujo y una palabra que se relacionen.",
        "No se debe usar la imagen 2 porque es de personas desconocidas sin permiso. La imagen 4 se puede mejorar: la palabra «mapuzugun» no se relaciona con una mesa; mejor poner un dibujo de un libro de la lengua con una glosa «mapuzugun, lengua del pueblo mapuche».",
        ["marca la imagen 2 con su razón", "propone una mejora para la 4", "relaciona palabra e imagen", "no usa personas sin permiso"],
        ["marca y razón escritas", "mejora propuesta"],
        ["aceptar la imagen 2", "relacionar mal palabra e imagen"],
        "Si acepta la imagen 2, pídele que relea la razón sobre el permiso.",
    ),
    reinforce="Vuelve a leer la lista de la clase y escribe una S o una N al lado de cada imagen.",
    extend="Haz un dibujo propio para una de las palabras de la clase y escribe una frase que lo acompañe.",
)

# ============================================================ LS06 clase 4 · texto narrado propio con créditos
CRD = "Créditos modelo (inventados para practicar): Creación: audio «Mi domingo». Autor: una estudiante del 6.º G. Expresiones de la fuente: «mari mari» y «chaltumay», entregadas y autorizadas por el educador tradicional de la Escuela Ejemplo. Palabras ya incorporadas al castellano: choclo y palta. Permiso de voz: un familiar que aparece, con permiso. Recursos: la grabadora del celular de su familia. Aviso: la creación cuenta una casa y no a todas las familias."

L(
    LS6, 4,
    materials="Lápiz y hoja. Los créditos modelo están escritos aquí y son inventados para practicar.",
    use="Aprenderé a escribir un texto narrado propio de tres partes y sus créditos, que reconocen quién entregó las expresiones en lengua, quién dio permiso y qué recursos se usaron. Sirve para terminar mi creación con honestidad y respeto.",
    prior=["Sé leer un texto narrado modelo y sus partes.", "Sé distinguir expresiones de la fuente y palabras ya incorporadas."],
    explain=[
        "Mi texto narrado tiene tres partes: saludo, relato y agradecimiento. Cada una dura unos segundos y entre las tres suman el tiempo del audio. Escribo el relato con una situación auténtica de mi vida, sin datos personales, y lo escribo en castellano con las palabras en lengua indígena que puedo usar: las expresiones que una fuente me entregó y las palabras ya incorporadas al castellano.",
        "Los créditos son el texto final que dice quién hizo la creación y quiénes colaboraron. Incluyen al autor, las expresiones de la fuente, las palabras ya incorporadas, el permiso de voz, los recursos y un aviso de límite. Así reconozco a quienes aportaron y no me apropio de lo que no es mío.",
        "Escribir los créditos ayuda a revisar mi propio trabajo. Si no puedo completar una línea, por ejemplo la del permiso de voz, significa que me falta algo y debo detenerme. Antes de mostrar la creación se la leo a la fuente, al educador o a la educadora tradicional y a la persona cuya voz aparece, para que confirmen que está bien.",
    ],
    vocab=[("créditos", "texto que dice quién hizo y quién colaboró en una creación"), ("colaborar", "ayudar con un aporte"), ("apropiarse", "presentar como propio algo ajeno"), ("aviso de límite", "frase que dice hasta dónde vale lo que se cuenta"), ("autor", "persona que hace una creación")],
    worked=[
        W("Completar una línea de créditos", CRD + " ¿Quién entregó y autorizó las expresiones en lengua?", ["Busco la línea de expresiones de la fuente.", "Dice que las entregó y autorizó el educador tradicional de la Escuela Ejemplo.", "Esa es la fuente."], "el educador tradicional de la Escuela Ejemplo"),
        W("Reconocer el aviso de límite", CRD + " ¿Cuál es el aviso de límite?", ["Busco la última línea.", "Dice que la creación cuenta una casa y no a todas las familias.", "Ese es el aviso."], "la creación cuenta una casa y no a todas las familias"),
    ],
    mistakes=[
        M("No poner en los créditos a quien entregó las expresiones.", "Parece que las inventé yo.", "Nombro a la fuente y escribo que las autorizó."),
        M("Escribir créditos sin aclarar que mi creación cuenta solo mi casa.", "Parece que hablo de todas las familias.", "Agrego el aviso de límite."),
    ],
    R=[
        ex(CRD + " ¿Cómo se llama la creación de los créditos modelo?", "Mi domingo", "Aparece en la primera línea."),
        ex(CRD + " ¿Qué recurso se usó?", "la grabadora del celular de su familia", "La línea de recursos lo dice."),
        ex(CRD + " ¿Qué palabras ya incorporadas al castellano aparecen en los créditos?", "choclo y palta", "La línea correspondiente las nombra."),
    ],
    C=[
        ex(CRD + " ¿Quién dio permiso de voz?", "un familiar", "La línea de permiso lo dice."),
        ex(CRD + " ¿Cuántas líneas tienen los créditos modelo?", "7", "Creación, autor, expresiones, palabras incorporadas, permiso, recursos y aviso."),
        ex("Verdadero o falso: se pueden poner créditos sin nombrar a la fuente de las expresiones en lengua.", "Falso", "La fuente debe nombrarse."),
    ],
    A=[
        ex("Ordena las partes del texto narrado. A) agradecimiento. B) relato. C) saludo. Escribe las letras en orden.", "C, B, A", "Se saluda, se cuenta y se agradece."),
        arith(CRD + " Los créditos tienen 7 líneas. Un estudiante escribió 5. ¿Cuántas líneas le faltan?", "7-5", "Se restan las escritas de las siete pedidas."),
        arith("Un audio tiene saludo de 10 segundos, relato de 40 segundos y agradecimiento de 10 segundos. ¿Cuántos segundos dura en total?", "10+40+10", "Se suman las tres partes."),
    ],
    Z=[
        ex(CRD + " Un estudiante dice que no hace falta poner al familiar en los créditos porque no lo pidió. ¿Es correcto? Sí o No.", "No", "Se reconoce a quien aportó."),
        ex(CRD + " ¿Qué indica que falta algo en los créditos: una línea que no se puede completar o una creación muy corta?", "una línea que no se puede completar", "Si no puedo completar una línea, me detengo."),
    ],
    D=[
        ex("Rosa escribe «Fuente de las expresiones: mi imaginación». Nico escribe «Fuente: educador tradicional que autorizó». ¿Quién atribuyó bien?", "Nico", "Las expresiones las entrega una fuente identificada."),
        ex("El familiar que aparece en tu audio pide que no aparezca su nombre. ¿Escribes «un familiar» o su nombre completo?", "un familiar", "Respetas lo que pidió."),
    ],
    context=[ex("Terminaste un audio con ayuda de tu curso y de una vecina. ¿Pones los créditos o los dejas fuera para que sea más corto?", "pones los créditos", "Reconoces a quienes aportaron.")],
    selfcheck=[
        ex("¿Los créditos nombran a la fuente de las expresiones en lengua? Sí o No.", "Sí", "Es una de sus líneas."),
        ex("¿Qué palabra describe presentar como propio algo ajeno: «colaborar» o «apropiarse»?", "apropiarse", "Es la definición."),
        ex("¿Qué hago si no puedo completar una línea de los créditos?", "me detengo", "Falta algo necesario."),
    ],
    task=T(
        "Escribe en tu cuaderno un texto narrado de tres partes (saludo, relato, agradecimiento) para un audio de 50 segundos que cuente un recuerdo familiar de la merienda, con las palabras «palta» y «poroto» ya incorporadas al castellano y las expresiones «mari mari» y «chaltumay», que autorizó un educador tradicional. Después escribe los créditos con siete líneas: creación, autor, expresiones de la fuente, palabras ya incorporadas, permiso de voz, recursos y aviso de límite. Reparte los 50 segundos entre las tres partes.",
        "Saludo (10 s): «Mari mari. Soy un estudiante del 6.º H». Relato (30 s): «En mi casa merendamos pan con palta y porotos los fines de semana, con una persona de mi casa». Agradecimiento (10 s): «Chaltumay por escucharme». Créditos: Creación «La merienda». Autor: un estudiante del 6.º H. Expresiones: mari mari y chaltumay, autorizadas por el educador tradicional. Palabras incorporadas: palta y poroto. Permiso de voz: una persona de mi casa. Recursos: grabadora de un celular. Aviso: cuenta solo mi casa.",
        ["tiene saludo, relato y agradecimiento con duración que suma 50 segundos", "usa las expresiones autorizadas con comillas", "escribe los créditos de siete líneas", "no incluye datos personales"],
        ["texto narrado de tres partes", "créditos de siete líneas"],
        ["no sumar 50 segundos", "olvidar el aviso"],
        "Si los segundos no suman 50, pídele que sume de nuevo y ajuste el relato.",
    ),
    reinforce="Copia los créditos modelo y pon al lado de cada línea el nombre de la persona o recurso que menciona.",
    extend="Escribe un segundo texto narrado de 30 segundos sobre tu camino a la escuela, con los mismos créditos adaptados.",
)

# ============================================================ LS06 clase 5 · contrastar dos versiones
VA = "Versión A (inventada para practicar): un audio de 60 segundos que cuenta el almuerzo del sábado, dice «mari mari» y «chaltumay» autorizados por el educador tradicional, tiene créditos completos y avisa que cuenta solo una casa."
VB = "Versión B (inventada): un audio de 60 segundos que cuenta el mismo almuerzo, dice «mari mari» pero no dice quién lo autorizó, no tiene créditos y muestra la dirección de la casa."

L(
    LS6, 5,
    materials="Lápiz y hoja. Las dos versiones están descritas aquí y son inventadas para practicar.",
    use="Aprenderé a comparar dos versiones de una misma creación con los mismos criterios y a decir cuál cumple mejor lo pedido, apoyándome en datos y sin juzgar a las personas. Sirve para revisar mi propia creación y mejorarla.",
    prior=["Sé armar un texto narrado con créditos.", "Sé que jerarquizar personas o pueblos no corresponde."],
    explain=[
        "Dos versiones de una creación pueden contar lo mismo y diferir en aspectos importantes. Para compararlas uso los mismos criterios: si las expresiones en lengua tienen fuente, si hay créditos, si hay datos personales y si declara un límite. Respondo cada criterio para cada versión y escribo qué se parece y qué cambia.",
        "En este caso comparo creaciones, no personas. Puedo decir con un dato que la versión A cumple mejor lo pedido porque nombra a la fuente y tiene créditos; la versión B no. No digo que quien hizo la B sea una mala persona. Si la versión B muestra la dirección de la casa, señalo que eso es un dato personal que conviene sacar.",
        "Comparar sirve para mejorar. Después de comparar, escribo qué cambios necesita la versión B: nombrar la fuente, agregar créditos y sacar la dirección. Y cierro con una frase que diga lo que las dos versiones tienen en común y en qué se diferencian, sin juzgar a las personas.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("versión", "forma en que está hecha una creación"), ("mejorar", "hacer que algo quede mejor"), ("dato personal", "dato que identifica a una persona"), ("cumplir", "hacer lo que se pide")],
    worked=[
        W("Comparar con un criterio", VA + " " + VB + " Compara si las expresiones tienen fuente.", ["La versión A dice que el educador tradicional las autorizó.", "La versión B no dice quién autorizó «mari mari».", "Hay diferencia."], "A nombra a la fuente y B no"),
        W("Proponer una mejora", VB + " ¿Qué cambio necesita la versión B por tener la dirección de la casa?", ["La dirección es un dato personal.", "No debe publicarse.", "Hay que sacarla."], "sacar la dirección"),
    ],
    mistakes=[
        M("Escribir «quien hizo la versión B es una persona descuidada».", "Se juzga a la persona y no a la creación.", "Digo qué le falta a la creación y cómo mejorarla."),
        M("Comparar un criterio en una versión y otro distinto en la otra.", "La comparación no es justa.", "Uso los mismos criterios para las dos."),
    ],
    R=[
        ex(VA + " ¿Cuánto dura la versión A?", "60 segundos", "La descripción lo dice."),
        ex(VB + " ¿Qué dato personal muestra la versión B?", "la dirección de la casa", "La descripción lo dice."),
        ex(VA + " ¿Qué expresiones usa la versión A?", "mari mari y chaltumay", "La descripción las nombra."),
    ],
    C=[
        ex(VA + " " + VB + " ¿Cuál de las dos versiones tiene créditos completos?", "la versión A", "La B no tiene créditos."),
        ex(VA + " " + VB + " ¿Cuál de las dos versiones avisa que cuenta solo una casa?", "la versión A", "La B no incluye aviso."),
        ex("Verdadero o falso: al comparar versiones se debe decir que quien hizo la peor es una mala persona.", "Falso", "Se compara la creación, no a la persona."),
    ],
    A=[
        ex(VA + " " + VB + " Completa con A o B: la versión ___ nombra a la fuente de las expresiones; la versión ___ muestra un dato personal. Escribe las dos letras en orden.", "A, B", "A nombra la fuente; B muestra la dirección."),
        arith(VA + " " + VB + " Las dos versiones duran 60 segundos cada una. Si se escuchan seguidas, ¿cuántos segundos duran juntas?", "60+60", "Se suman las dos duraciones."),
        ex("Clasifica cada frase como C (compara con un dato) o J (juzga a la persona). 1) «La A tiene créditos y la B no». 2) «Quien hizo la B no tiene cuidado». 3) «La B muestra la dirección y la A no». Escribe las tres letras.", "1 C, 2 J, 3 C", "Solo la frase 2 juzga a una persona."),
    ],
    Z=[
        ex(VA + " " + VB + " ¿Qué tienen en común las dos versiones según las descripciones?", "cuentan el mismo almuerzo", "Las dos cuentan el almuerzo del sábado."),
        ex(VB + " ¿Qué cambios necesita la versión B en total, además de sacar la dirección: nombrar la fuente y agregar créditos, o solo cambiar la música?", "nombrar la fuente y agregar créditos", "Eso es lo que le falta."),
    ],
    D=[
        ex(VA + " " + VB + " Elige la mejor frase de cierre. A) «Las dos versiones cuentan el mismo almuerzo; la A nombra la fuente y tiene créditos, y la B necesita nombrarla, agregar créditos y sacar la dirección». B) «La B es pésima». Escribe la letra.", "A", "Dice semejanza y diferencia con datos y propone mejoras."),
        ex("Descubres que la versión de tu amigo muestra una dirección. ¿Qué haces: se lo cuentas con respeto y propones sacarla o lo publicas como está?", "se lo cuentas con respeto y propones sacarla", "Se cuida a las personas y se ayuda a mejorar."),
    ],
    context=[ex("Dos compañeros hicieron versiones distintas de un audio sobre su barrio. Te piden decir cuál es mejor. ¿Comparas con los mismos criterios y propones mejoras, o dices solo cuál te gustó más?", "comparas con los mismos criterios y propones mejoras", "Así comparas con datos.")],
    selfcheck=[
        ex("¿Se comparan creaciones o personas?", "creaciones", "No se juzga a las personas."),
        ex("¿Una dirección es un dato personal? Sí o No.", "Sí", "Identifica a una persona."),
        ex("¿Se usan los mismos criterios para las dos versiones? Sí o No.", "Sí", "Así la comparación es justa."),
    ],
    task=T(
        "Lee estas dos versiones inventadas de un cartel sobre «Mi merienda». Versión 1: usa «mari mari» (saludo autorizado por el educador tradicional), tiene créditos y no muestra personas. Versión 2: usa «mari mari» (sin fuente), no tiene créditos y muestra la foto de un vecino sin su permiso. En tu cuaderno haz una tabla con estas filas: fuente de la expresión, créditos, personas que aparecen y permiso. Luego escribe una frase de cierre con una semejanza y una diferencia, y una lista de dos cambios que necesita la versión 2.",
        "Fuente: educador tradicional / sin fuente. Créditos: sí / no. Personas: ninguna / un vecino. Permiso: no hace falta / falta. Cierre: «Los dos carteles cuentan una merienda y usan mari mari; el primero tiene fuente, créditos y no muestra personas, y el segundo no». Cambios para la versión 2: nombrar la fuente y retirar la foto o pedir permiso.",
        ["completa las cuatro filas para ambas versiones", "usa los mismos criterios", "escribe semejanza y diferencia", "propone dos cambios sin juzgar a personas"],
        ["tabla de comparación", "frase de cierre", "lista de dos cambios"],
        ["juzgar a la persona que hizo la versión 2", "dejar una fila sin completar"],
        "Si juzga a la persona, pídele que reescriba hablando solo de la creación.",
    ),
    reinforce="Copia las dos versiones del ejemplo y subraya en cada una lo que tiene y lo que le falta.",
    extend="Escribe cómo mejorarías tu propia creación de esta unidad con los mismos cuatro criterios.",
)
